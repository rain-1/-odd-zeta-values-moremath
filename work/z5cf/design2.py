"""Fast design matrices: T mod q from factorial tables, numpy int64 throughout."""
import numpy as np, itertools, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bare import Q1, Q2, lad_mod, SYMNAME

NS = 9
SIGMA = {0: 0, 1: 2, 2: 1, 3: 4, 4: 3, 5: 6, 6: 5, 7: 7, 8: 8}


def partitions(W):
    out = []

    def rec(rem, mx, cur):
        if rem == 0:
            out.append(tuple(cur)); return
        for a in range(min(rem, mx), 0, -1):
            rec(rem - a, a, cur + [a])
    rec(W, W, [])
    return out


def monomials(W, maxdeg=None, syms=None):
    syms = list(range(NS)) if syms is None else list(syms)
    mons = []
    for sig in partitions(W):
        if maxdeg is not None and len(sig) > maxdeg:
            continue
        groups, i = [], 0
        while i < len(sig):
            j = i
            while j < len(sig) and sig[j] == sig[i]:
                j += 1
            groups.append((sig[i], j - i)); i = j
        choices = [list(itertools.combinations_with_replacement(syms, c)) for (_, c) in groups]
        for combo in itertools.product(*choices):
            m = []
            for (r, _), ss in zip(groups, combo):
                m.extend((r, s) for s in ss)
            mons.append(tuple(sorted(m)))
    return mons


def sym_image(m):
    return tuple(sorted((r, SIGMA[s]) for (r, s) in m))


def sym_orbits(mons):
    seen, reps = set(), []
    for m in mons:
        if m in seen:
            continue
        reps.append(m); seen.add(m); seen.add(sym_image(m))
    return reps


def monname(m):
    from collections import Counter
    c = Counter(m)
    ps = []
    for (r, s), e in sorted(c.items()):
        t = 'H%d[%s]' % (r, SYMNAME[s])
        ps.append(t if e == 1 else '%s^%d' % (t, e))
    return '*'.join(ps) if ps else '1'


class Eng:
    def __init__(self, N, q, maxr):
        self.N, self.q = N, q
        M = 4 * N + 8
        f = np.ones(M + 1, dtype=np.int64)
        for i in range(1, M + 1):
            f[i] = f[i - 1] * i % q
        self.f = f
        fi = np.ones(M + 1, dtype=np.int64)
        fi[M] = pow(int(f[M]), q - 2, q)
        for i in range(M, 0, -1):
            fi[i - 1] = fi[i] * i % q
        self.fi = fi
        inv = np.zeros(M + 1, dtype=np.int64)
        for i in range(1, M + 1):
            inv[i] = f[i - 1] * fi[i] % q
        self.H = {}
        for r in range(1, maxr + 1):
            h = np.zeros(M + 1, dtype=np.int64)
            s = 0
            pw = 1
            for m in range(1, M + 1):
                pw = pow(int(inv[m]), r, q)
                s = (s + pw) % q
                h[m] = s
            self.H[r] = h

    def cells(self, n):
        q, f, fi = self.q, self.f, self.fi
        kk, ll = np.meshgrid(np.arange(n + 1), np.arange(n + 1), indexing='ij')
        kk = kk.ravel(); ll = ll.ravel()
        # C(n+k,n)=f[n+k]fi[n]fi[k]
        t = f[n + kk] * fi[n] % q * fi[kk] % q
        c = f[n] * fi[kk] % q * fi[n - kk] % q
        t = t * c % q * c % q
        t = t * (f[n + ll] * fi[n] % q * fi[ll] % q) % q
        c = f[n] * fi[ll] % q * fi[n - ll] % q
        t = t * c % q * c % q
        t = t * (f[n + kk + ll] * fi[n] % q * fi[kk + ll] % q) % q
        idx = [np.full(kk.shape, n, dtype=np.int64), kk, ll, n + kk, n + ll,
               n - kk, n - ll, kk + ll, n + kk + ll]
        return t, idx


def build(W, N, q, maxdeg=None, symmetric=True, syms=None, verbose=False, mons=None):
    if mons is None:
        mons = monomials(W, maxdeg, syms)
        if symmetric:
            mons = sym_orbits(mons)
    E = Eng(N, q, W)
    rows = np.zeros((N + 1, len(mons)), dtype=np.int64)
    for n in range(N + 1):
        Tv, idx = E.cells(n)
        hv = {r: [E.H[r][i] for i in idx] for r in range(1, W + 1)}
        for j, m in enumerate(mons):
            v = Tv
            for (r, s) in m:
                v = v * hv[r][s] % q
            rows[n, j] = int(v.sum() % q)
        if verbose and n % 25 == 0:
            print('   n=%d' % n, flush=True)
    return mons, rows


# ---------------- modular linear algebra (numpy, vectorised) ----------------
def rref(A, q):
    A = A.copy() % q
    rows, cols = A.shape
    r = 0
    piv = []
    for c in range(cols):
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
        if r == rows:
            break
    return A, r, piv
