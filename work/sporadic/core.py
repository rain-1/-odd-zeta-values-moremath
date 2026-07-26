"""BARE-alphabet harmonic-decomposition harness for the 15 sporadic Apery-like families.

Ansatz:   B(n) = sum_cells S(n, k[, l]) * w(n, k[, l])
with      w = sum_j c_j * prod_t L_{j t}(x_{j t}),
letters   L = H^{(r)}(x) = sum_{m<=x} 1/m^r         (bare, NOT a difference)
          L = K_chi^{(r)}(x) = sum_{m<=x} chi(m)/m^r
arguments x = integer linear forms in (n, k[, l]).

Everything modular is done with numpy int64 mod primes < 2^31 (products < 2^62).
Exact verification is done with fractions.Fraction.
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lbw'))
from sporadic import SEQS, gen_A, gen_B          # noqa: E402

# ---------------------------------------------------------------- primes
PRIMES = [1073741789, 1073741783, 1073741741, 1073741723, 1073741719, 1073741717,
          1073741689, 1073741671]


def chi(D, m):
    if D is None or D == 1:
        return 1
    if D == -3:
        return 0 if m % 3 == 0 else (1 if m % 3 == 1 else -1)
    if D == -4:
        return 0 if m % 2 == 0 else (1 if m % 4 == 1 else -1)
    if D == 5:
        return 0 if m % 5 == 0 else (1 if m % 5 in (1, 4) else -1)
    if D == -7:   # chi_{-7}, conductor 7, QRs mod 7 = {1,2,4}
        return 0 if m % 7 == 0 else (1 if m % 7 in (1, 2, 4) else -1)
    if D == 8:
        return 0 if m % 2 == 0 else (1 if m % 8 in (1, 7) else -1)
    if D == -8:
        return 0 if m % 2 == 0 else (1 if m % 8 in (1, 3) else -1)
    if D == 12:
        return 0 if m % 6 in (0, 2, 3, 4) else (1 if m % 12 in (1, 11) else -1)
    raise ValueError('unknown discriminant %r' % (D,))


# ---------------------------------------------------------------- letters
# a letter key is ('H', r) or ('K', D, r).  weight(key) = r = key[-1].

def lname(key):
    return 'H%d' % key[1] if key[0] == 'H' else 'K%s^%d' % (key[1], key[2])


class Tab:
    """modular partial-sum tables, index 0..M (index -1 .. -inf -> value 0)."""

    def __init__(self, M, q, keys):
        self.M, self.q = M, q
        inv = np.zeros(M + 2, dtype=np.int64)
        for i in range(1, M + 2):
            inv[i] = pow(i, q - 2, q)
        self.t = {}
        for key in keys:
            r = key[-1]
            arr = np.zeros(M + 2, dtype=np.int64)
            s = 0
            for m in range(1, M + 2):
                c = 1 if key[0] == 'H' else chi(key[1], m)
                if c:
                    s = (s + c * pow(int(inv[m]), r, q)) % q
                arr[m] = s % q
            self.t[key] = arr

    def vals(self, key, idx):
        """idx: int64 array of arguments; out-of-range (<0) -> 0, (>M) -> raise."""
        a = np.asarray(idx, dtype=np.int64)
        if a.size and a.max() > self.M:
            raise ValueError('argument %d exceeds table bound %d' % (a.max(), self.M))
        safe = np.where(a < 0, 0, a)
        v = self.t[key][safe]
        return np.where(a < 0, 0, v)


class ETab:
    """exact Fraction partial-sum tables."""

    def __init__(self, M, keys):
        self.M = M
        self.t = {}
        for key in keys:
            r = key[-1]
            arr = [Fr(0)] * (M + 2)
            s = Fr(0)
            for m in range(1, M + 2):
                c = 1 if key[0] == 'H' else chi(key[1], m)
                if c:
                    s += Fr(c, m ** r)
                arr[m] = s
            self.t[key] = arr

    def val(self, key, x):
        if x < 0:
            return Fr(0)
        if x > self.M:
            raise ValueError('argument %d exceeds exact table bound %d' % (x, self.M))
        return self.t[key][x]


# ---------------------------------------------------------------- monomials
def monomials(keys, args, w, maxdeg=None, chi_hom=None):
    """all monomials of total weight w in letters (key, argname).

    chi_hom: if not None, keep only monomials with exactly chi_hom chi-letters
             (hypothesis (H5) of Theorem LB).
    """
    letters = [(k, a) for k in keys for a in args]
    bywt = {}
    for L in letters:
        bywt.setdefault(L[0][-1], []).append(L)

    def parts(rem, mx):
        if rem == 0:
            yield ()
            return
        for a in range(min(rem, mx), 0, -1):
            for rest in parts(rem - a, a):
                yield (a,) + rest

    out = []
    for sig in parts(w, w):
        if maxdeg is not None and len(sig) > maxdeg:
            continue
        groups, i = [], 0
        while i < len(sig):
            j = i
            while j < len(sig) and sig[j] == sig[i]:
                j += 1
            groups.append((sig[i], j - i))
            i = j
        ok = True
        choices = []
        for (r, c) in groups:
            pool = bywt.get(r, [])
            if not pool:
                ok = False
                break
            choices.append(list(itertools.combinations_with_replacement(pool, c)))
        if not ok:
            continue
        for combo in itertools.product(*choices):
            m = []
            for ss in combo:
                m.extend(ss)
            m = tuple(sorted(m, key=lambda L: (str(L[0]), L[1])))
            if chi_hom is not None:
                ne = sum(1 for (k, _) in m if k[0] == 'K')
                if ne != chi_hom:
                    continue
            out.append(m)
    return sorted(set(out), key=lambda m: (len(m), tuple(str(x) for x in m)))


def mname(m):
    from collections import Counter
    c = Counter(m)
    ps = []
    for (k, a), e in sorted(c.items(), key=lambda t: (str(t[0][0]), t[0][1])):
        s = '%s[%s]' % (lname(k), a)
        ps.append(s if e == 1 else '%s^%d' % (s, e))
    return '*'.join(ps) if ps else '1'


# ---------------------------------------------------------------- families
class Family:
    """label, weight w, cell generator, argument forms."""

    def __init__(self, label, w, D, cells, args, note=''):
        self.label, self.w, self.D, self.cells, self.args, self.note = \
            label, w, D, cells, args, note

    def maxarg(self, N):
        mx = 0
        for n in (N, max(0, N - 1)):
            _, idx = self.cells(n)
            for a in self.args:
                if idx[a].size:
                    mx = max(mx, int(idx[a].max()))
        return mx


# ---------------------------------------------------------------- design
def design(fam, mons, N, q, tab, nmin=1, ncells=None):
    """rows n = nmin..N, cols = mons; entry sum_cells S * prod letters (mod q)."""
    rows = np.zeros((N - nmin + 1, len(mons)), dtype=np.int64)
    for n in range(nmin, N + 1):
        S, idx = fam.cells(n)
        if S.size == 0:
            continue
        Sm = np.mod(S, q)
        cache = {}
        for j, m in enumerate(mons):
            v = Sm
            for L in m:
                if L not in cache:
                    cache[L] = tab.vals(L[0], idx[L[1]])
                v = v * cache[L] % q
            rows[n - nmin, j] = int(v.sum() % q)
        if ncells is not None:
            ncells.append(S.size)
    return rows


def rref(A, q, augment=None):
    """returns (rank, pivots, reduced) ; A modified copy."""
    A = np.mod(A.copy(), q)
    nr, nc = A.shape
    r, piv = 0, []
    for c in range(nc):
        if r >= nr:
            break
        nz = np.nonzero(A[r:, c])[0]
        if nz.size == 0:
            continue
        p = r + int(nz[0])
        if p != r:
            A[[r, p]] = A[[p, r]]
        A[r] = A[r] * pow(int(A[r, c]), q - 2, q) % q
        col = A[:, c].copy()
        col[r] = 0
        nzr = np.nonzero(col)[0]
        if nzr.size:
            A[nzr] = (A[nzr] - np.outer(col[nzr], A[r])) % q
        piv.append(c)
        r += 1
    return r, piv, A


def consistency(A, b, q):
    """returns dict(rank, rank_aug, consistent, excess, pivots, sol)."""
    nr, nc = A.shape
    M = np.concatenate([A, b.reshape(-1, 1)], axis=1)
    r, piv, R = rref(M, q)
    consistent = (nc not in piv)
    rank = r - (0 if consistent else 1)
    sol = None
    if consistent:
        sol = np.zeros(nc, dtype=np.int64)
        for i, c in enumerate(piv):
            sol[c] = R[i, nc]
    return dict(rank=rank, rank_aug=r, consistent=consistent,
                excess=nr - rank, pivots=[c for c in piv if c < nc], sol=sol,
                nrows=nr, ncols=nc)


# ---------------------------------------------------------------- CRT / recon
def crt(rs, ms):
    x, M = 0, 1
    for r, m in zip(rs, ms):
        g = pow(M % m, -1, m)
        t = (r - x) % m * g % m
        x += M * t
        M *= m
    return x % M, M


def ratrecon(a, M):
    bound = int((M // 2) ** 0.5)
    r0, r1, s0, s1 = M, a % M, 0, 1
    while r1 > bound:
        qq = r0 // r1
        r0, r1 = r1, r0 - qq * r1
        s0, s1 = s1, s0 - qq * s1
    if s1 == 0 or abs(s1) > bound:
        return None
    return Fr(r1, s1) if s1 > 0 else Fr(-r1, -s1)


def bmod(x, q):
    return x.numerator % q * pow(x.denominator % q, q - 2, q) % q


# ---------------------------------------------------------------- exact check
def exact_check(fam, terms, Bn, ns, etab):
    """terms = [(Fraction c, monomial)]; returns list of failing n."""
    bad = []
    for n in ns:
        S = fam.Sexact(n)
        idx = fam.idx(n)
        tot = Fr(0)
        for i in range(len(S)):
            s = int(S[i])
            if s == 0:
                continue
            v = Fr(0)
            for c, m in terms:
                p = c
                for (k, a) in m:
                    p *= etab.val(k, int(idx[a][i]))
                    if p == 0:
                        break
                v += p
            tot += s * v
        if tot != Bn[n]:
            bad.append(n)
    return bad
