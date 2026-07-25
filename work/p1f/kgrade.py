"""P1f: exact u-graded expansion  v5(n,k,l) = sum_j K_j(n,k,l) u^j,  u = 1/p.

Lemma U (PHASE2_INDUCTION 2.1):  H^(m)_N = sum_{e>=0} u^{e m} Sig_e^{(m)}(N),
    Sig_e^{(m)}(N) = sum_{j <= floor(N/p^e), p nmid j} j^{-m}  in Z_(p).

Each letter X_m = H^(m)_{N1} - H^(m)_{N2}  therefore expands as a polynomial in u
supported on exponents {0, m, 2m, ..., Mm}.  A weight-5 monomial multiplies these,
so v5 is a polynomial in u of degree <= 5M.  All coefficients lie in Z_(p).

This module returns the FULL exact list [K_0, ..., K_{5M}] of Fractions.
"""
import sys, json, functools
from fractions import Fraction as F
from math import comb

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1d')
from core import vp, T, Hs

W5DIR = '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/'


def load(fn=W5DIR + 'w5_allp.json'):
    d = json.load(open(fn))
    terms = []
    for lab, (num, den) in d.items():
        fg, rest = lab.split(']x')
        f, g = fg[1:].split('|')
        h, s = rest.split('x')
        sp = lambda x: [] if x == '1' else x.split('*')
        terms.append((F(num, den), sp(f), sp(g), sp(h), sp(s)))
    return terms


TERMS = load()

# ---------------------------------------------------------------- Sigma_e^{(m)}
_SIG = {}


def Sig(N, m, e, p):
    """sum_{j <= N//p^e, p nmid j} j^{-m}."""
    if N <= 0:
        return F(0)
    M = N // p ** e
    key = (M, m, p)
    v = _SIG.get(key)
    if v is None:
        v = F(0)
        for j in range(1, M + 1):
            if j % p:
                v += F(1, j ** m)
        _SIG[key] = v
    return v


# ---------------------------------------------------------------- u-polynomials
def lpoly(N1, N2, m, p, M):
    """u-expansion of H^(m)_{N1} - H^(m)_{N2} truncated at level M (exact: levels > M vanish)."""
    d = {}
    for e in range(M + 1):
        v = Sig(N1, m, e, p) - Sig(N2, m, e, p)
        if v:
            d[e * m] = d.get(e * m, F(0)) + v
    return d


def pmul(A, B, cap):
    R = {}
    for i, x in A.items():
        for j, y in B.items():
            if i + j <= cap:
                R[i + j] = R.get(i + j, F(0)) + x * y
            else:
                # a term of u-degree > 5M cannot occur (weights sum to 5, e<=M)
                raise AssertionError('u-degree overflow %d > %d' % (i + j, cap))
    return {k: v for k, v in R.items() if v}


def v5_upoly(n, k, l, p, terms=None):
    """Exact list [K_0,...,K_{5M}] with v5(n,k,l) = sum K_j p^{-j}."""
    terms = terms or TERMS
    L = 0
    q = n
    while q >= p:
        q //= p
        L += 1
    M = L + 1
    cap = 5 * M

    def LET(nm, i):
        t, r = nm[0], int(nm[1])
        if t == 'A':
            return lpoly(n + i, i, r, p, M)
        if t == 'B':
            return lpoly(n - i, i, r, p, M)
        raise ValueError(nm)

    tot = {}
    for cf, f, g, h, s in terms:
        base = {0: cf}
        for nm in h:
            base = pmul(base, lpoly(n + k + l, k + l, int(nm[1]), p, M), cap)
        for nm in s:
            base = pmul(base, lpoly(n, 0, int(nm[1]), p, M), cap)

        def side(fm, gm):
            P = {0: F(1)}
            for nm in fm:
                P = pmul(P, LET(nm, k), cap)
            for nm in gm:
                P = pmul(P, LET(nm, l), cap)
            return P
        acc = side(f, g)
        if f != g:
            for kk, vv in side(g, f).items():
                acc[kk] = acc.get(kk, F(0)) + vv
        acc = pmul(acc, base, cap)
        for kk, vv in acc.items():
            tot[kk] = tot.get(kk, F(0)) + vv
    # subtract H^(5)_n  (v5 = w5 - H^(5)_n)
    for kk, vv in lpoly(n, 0, 5, p, M).items():
        tot[kk] = tot.get(kk, F(0)) - vv
    out = [F(0)] * (cap + 1)
    for kk, vv in tot.items():
        out[kk] = vv
    return out, L, M


def pattern(n, k, l, p, M):
    P = p ** M
    al = 1 if n + k >= P else 0
    ga = 1 if n + l >= P else 0
    eps = (k + l) // P
    ka = 1 if n + k + l >= (eps + 1) * P else 0
    th = eps + 1 if ka else 1
    return (al, ga, ka, th)
