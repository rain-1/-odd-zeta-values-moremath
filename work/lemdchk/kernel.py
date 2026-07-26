"""T3c: is the target statement decomposition-dependent, and can ANY admissible weight
repair the two-layer split?

The decomposition w is NOT unique: the fitting system has a large kernel, so the full
admissible set is  w_0 + Ker,  Ker = { kappa : sum_k S(n,k) kappa(n,k) = 0 for all n }.

Pole-free reformulation of the base-level defect.  On the surviving b-set at level a
(i.e. p !| S(a,b)) every argument x(a,b) is < p (measured below), so w(a,b) is p-integral
there and

    Delta(a) == 0 (mod p)   <==>   sum_{b : p !| S(a,b)} S(a,b) w(a,b)  ==  B(a) (mod p).

Both sides are p-integral and LINEAR in the coefficients of w.  So for each p the question
"is there an admissible w with Delta == 0 for every a < p?" is a linear system over F_p in
the kernel coordinates.  This script:

  (1) computes an exact Q-basis of Ker (RREF mod 4 primes + CRT + rational reconstruction),
      and VERIFIES each basis vector exactly (sum_k S(n,k) kappa(n,k) == 0, Fractions);
  (2) confirms w_0 (LBW's decomposition) lies in the affine solution set;
  (3) shows Delta(a) mod p CHANGES under kernel perturbation (=> the target is
      decomposition-dependent);
  (4) decides, per prime, whether the system  L_{p,a}(w) == B(a)  (all a<p) is solvable.
"""
import os
import sys
from fractions import Fraction as F

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'lbw'))
sys.path.insert(0, os.path.join(HERE, '..', 'sporadic'))

from sporadic import SEQS, gen_A, gen_B                        # noqa: E402
import core                                                    # noqa: E402
from core import PRIMES, monomials, mname, rref, crt, ratrecon, bmod  # noqa: E402
from fams import FAMS as SFAMS, Fac                            # noqa: E402
from decs import FAMS, ARG                                     # noqa: E402
from pad import vp_binom, vp_int                               # noqa: E402

PAR = {l: (f, p) for l, f, p, _, _ in SEQS}

ALPHABET = {
    'alpha': (['k', 'n-k', '2k', '2n-2k'], 3, (), None),
    'eps':   (['k', 'n-k', '2k', '2k-n'], 3, (), None),
    's7':    (['n', 'k', 'n-k', '2k'], 2, (), None),
    'E':     (['k', 'n-k', '2k', '2n-2k'], 2, (-4,), 1),
}
SEQOF = {'alpha': 'alpha', 'eps': 'eps', 's7': 's7', 'E': 'E'}


# ---------------------------------------------------------------- exact letters
_T = {}


def Lex(kind, r, y):
    t = _T.setdefault((kind, r), [F(0)])
    while len(t) <= y:
        m = len(t)
        c = 1 if kind == 'H' else (0 if m % 2 == 0 else (1 if m % 4 == 1 else -1))
        t.append(t[-1] + F(c, m ** r))
    return t[y]


def keyof(L):
    return ('H', L[0][1]) if L[0][0] == 'H' else ('K', L[0][2])


def mon_eval_exact(m, n, k):
    v = F(1)
    for L in m:
        kind = 'H' if L[0][0] == 'H' else 'K'
        r = L[0][-1]
        y = ARG[L[1]](n, k)
        if y < 0:
            return F(0)
        v *= Lex(kind, r, y)
    return v


def w_from_coeffs(co, mons, n, k):
    tot = F(0)
    for c, m in zip(co, mons):
        if c:
            tot += c * mon_eval_exact(m, n, k)
    return tot


# ---------------------------------------------------------------- kernel over Q
def design(lab, mons, N, q):
    SF = SFAMS[lab if lab != 'eps' else 'eps']
    M = SF.maxtop * N + 8
    fac = Fac(M, q)
    keys = sorted({L[0] for m in mons for L in m})
    tab = core.Tab(M, q, keys)
    rows = np.zeros((N, len(mons)), dtype=np.int64)
    for n in range(1, N + 1):
        S = SF.Smod(n, fac)
        if S.size == 0:
            continue
        ix = SF.idx(n)
        cache = {}
        for j, m in enumerate(mons):
            v = S
            for L in m:
                if L not in cache:
                    cache[L] = tab.vals(L[0], ix[L[1]])
                v = v * cache[L] % q
            rows[n - 1, j] = int(v.sum() % q)
    return rows


def kernel_exact(lab, N=200, nprimes=4):
    args, w, discs, hom = ALPHABET[lab]
    keys = [('H', r) for r in range(1, w + 1)] + \
           [('K', d, r) for d in discs for r in range(1, w + 1)]
    mons = monomials(keys, args, w, None, hom)
    bases = []
    for q in PRIMES[:nprimes]:
        A = design(lab, mons, N, q)
        r, piv, R = rref(A, q)
        free = [c for c in range(len(mons)) if c not in piv]
        B = []
        for fcol in free:
            v = [0] * len(mons)
            v[fcol] = 1
            for i, c in enumerate(piv):
                v[c] = (-int(R[i, fcol])) % q
            B.append(v)
        bases.append((B, piv, free, q))
    piv0, free0 = bases[0][1], bases[0][2]
    for B, piv, free, q in bases[1:]:
        assert piv == piv0 and free == free0, 'pivot pattern differs between primes'
    ker = []
    ms = [b[3] for b in bases]
    for i in range(len(free0)):
        vec = []
        for j in range(len(mons)):
            a, MM = crt([b[0][i][j] for b in bases], ms)
            f = ratrecon(a, MM)
            if f is None:
                return None, mons, 'ratrecon failed'
            vec.append(f)
        ker.append(vec)
    return ker, mons, 'ok'


def verify_kernel(lab, ker, mons, NS=range(1, 22)):
    fam = FAMS[lab]
    bad = 0
    for vec in ker:
        for n in NS:
            tot = F(0)
            for k in fam.ks(n):
                s = fam.S(n, k)
                if s:
                    tot += s * w_from_coeffs(vec, mons, n, k)
            if tot != 0:
                bad += 1
                break
    return bad


def w0_coeffs(lab, mons):
    """LBW's decomposition expressed in the monomial basis (None if not representable)."""
    fam = FAMS[lab]
    idx = {}
    for j, m in enumerate(mons):
        key = tuple(sorted((('H', L[0][1]) if L[0][0] == 'H' else ('K', L[0][2]), L[1])
                           for L in m))
        idx[key] = j
    co = [F(0)] * len(mons)
    for c, mo in fam.W:
        key = tuple(sorted(((kind, r), ag) for kind, r, ag in mo))
        if key not in idx:
            return None, key
        co[idx[key]] += c
    return co, None


# ---------------------------------------------------------------- the F_p system
def surviving_args_ok(lab, p):
    """on the surviving b-set at level a, is every argument < p?"""
    fam = FAMS[lab]
    args = ALPHABET[lab][0]
    mx = -1
    for a in range(1, p):
        for b in fam.ks(a):
            bins = fam.BIN(a, b)
            if any(bb < 0 or t < bb for t, bb in bins):
                continue
            if sum(vp_binom(t, bb, p) for t, bb in bins) == 0:
                for ag in args:
                    mx = max(mx, ARG[ag](a, b))
    return mx


def fp_system(lab, p, co0, ker, mons):
    """rows a=1..p-1 :  sum_i c_i L_{p,a}(kappa_i)  ==  B(a) - L_{p,a}(w_0)  (mod p)."""
    fam = FAMS[lab]
    f, par = PAR[SEQOF[lab]]
    Bsm = gen_B(f, par, p + 2)

    def Lp(coeffs, a):
        tot = F(0)
        for b in fam.ks(a):
            bins = fam.BIN(a, b)
            if any(bb < 0 or t < bb for t, bb in bins):
                continue
            if sum(vp_binom(t, bb, p) for t, bb in bins) != 0:
                continue
            tot += fam.S(a, b) * w_from_coeffs(coeffs, mons, a, b)
        return tot

    def red(x):
        if x.denominator % p == 0:
            return None
        return x.numerator % p * pow(x.denominator % p, -1, p) % p

    rows, rhs = [], []
    for a in range(1, p):
        r = []
        ok = True
        for kv in ker:
            v = red(Lp(kv, a))
            if v is None:
                ok = False
                break
            r.append(v)
        if not ok:
            return None
        b0 = red(Bsm[a] - Lp(co0, a))
        if b0 is None:
            return None
        rows.append(r)
        rhs.append(b0)
    A = np.array(rows, dtype=np.int64)
    b = np.array(rhs, dtype=np.int64)
    Aug = np.concatenate([A, b.reshape(-1, 1)], axis=1)
    rA, _, _ = rref(A, p)
    rAug, pivAug, _ = rref(Aug, p)
    return dict(rank=rA, rank_aug=rAug, consistent=(rA == rAug),
                nrows=len(rows), ncols=len(ker),
                inhom_zero=bool(np.all(b % p == 0)))


if __name__ == '__main__':
    labs = sys.argv[1].split(',') if len(sys.argv) > 1 else ['alpha', 'eps', 's7', 'E']
    primes = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 \
        else [5, 7, 11, 13, 17, 19, 23]
    for lab in labs:
        args, w, discs, hom = ALPHABET[lab]
        ker, mons, st = kernel_exact(lab)
        if ker is None:
            print('%s: kernel extraction failed (%s)' % (lab, st))
            continue
        nb = verify_kernel(lab, ker, mons)
        co0, miss = w0_coeffs(lab, mons)
        print('=== %-6s alphabet %s  w=%d disc=%s  cols=%d  kernel dim=%d  '
              '(exact-Q kernel check: %d bad of %d)'
              % (lab, args, w, discs, len(mons), len(ker), nb, len(ker)))
        if co0 is None:
            print('    LBW w_0 NOT representable in this basis: missing %s' % (miss,))
            continue
        # sanity: w_0 reproduces B(n)
        fam = FAMS[lab]
        f, par = PAR[SEQOF[lab]]
        Bn = gen_B(f, par, 30)
        badw = [n for n in range(1, 21)
                if sum(fam.S(n, k) * w_from_coeffs(co0, mons, n, k) for k in fam.ks(n))
                != Bn[n]]
        print('    w_0 in basis reproduces B(n) for n=1..20: %s' % ('YES' if not badw
                                                                    else 'NO %s' % badw))
        for p in primes:
            mx = surviving_args_ok(lab, p)
            R = fp_system(lab, p, co0, ker, mons)
            if R is None:
                print('    p=%-3d  (coefficients not p-integral -- skipped)' % p)
                continue
            print('    p=%-3d  max arg on surviving b-set = %-3d (p=%d)  |  F_p system '
                  '%d x %d  rank=%d rank_aug=%d  ->  %s%s'
                  % (p, mx, p, R['nrows'], R['ncols'], R['rank'], R['rank_aug'],
                     'SOLVABLE' if R['consistent'] else 'UNSOLVABLE',
                     '   (w_0 already works)' if R['inhom_zero'] else ''), flush=True)
        print()
