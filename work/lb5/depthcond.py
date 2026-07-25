"""(GAP-5) route A, step 1: the p-INDEPENDENT linear depth conditions on w5.

Setting.  p >= 5, 1 <= a < p, 0 <= b,c <= a.  Level-a letters:
   A_r(b) = H^(r)_{a+b} - H^(r)_b      pole  <=>  a+b >= p   (then = p^-r + Z_p)
   B_r(b) = H^(r)_{a-b} - H^(r)_b      never a pole (both args < p)
   C_r    = H^(r)_{a+b+c} - H^(r)_{b+c}  pole <=> kappa := v_p C(a+b+c,a) = 1,
            and then C_r = theta^-r p^-r + Z_p,  theta = 1 + floor((b+c)/p) in {1,2}
   N_r    = H^(r)_a                    never a pole.
So with u := p^-1 every letter is  (pole residue) * u^r  +  (a Z_p symbol),
and w5(a,b,c) - H^(5)_a = sum_{j=0}^{5} K_j u^j with K_j in Z_p.
d5 <= J  is IMPLIED by  K_j = 0 for all j > J  (identically in the Z_p symbols).

This script builds those linear conditions on the 448 basis coefficients.
"""
import sys, json
from fractions import Fraction as F
from collections import defaultdict
from itertools import product

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from run_fit import build_basis
from fit import Q1, Q2

KL = ['A%d' % r for r in range(1, 6)] + ['B%d' % r for r in range(1, 6)]
CL = ['C%d' % r for r in range(1, 6)]
NL = ['N%d' % r for r in range(1, 6)]


def basis():
    return build_basis(5, False, 5, 2, 2, maxr=5, kletters=KL, cletters=CL, nletters=NL)


# ---------------------------------------------------------------- u-polynomials
# an element is a dict {(upow, symkey): Fraction}; symkey a sorted tuple of symbols
def pmul(P, Q):
    R = defaultdict(F)
    for (u1, s1), c1 in P.items():
        for (u2, s2), c2 in Q.items():
            R[(u1 + u2, tuple(sorted(s1 + s2)))] += c1 * c2
    return {k: v for k, v in R.items() if v}


ONE = {(0, ()): F(1)}


def letter(name, slot, alpha, gamma, kappa, theta):
    """slot in {'b','c'} = which level-a argument this letter instance is evaluated at."""
    t, r = name[0], int(name[1])
    if t == 'A':
        res = alpha if slot == 'b' else gamma
        P = {(0, (('a', r, slot),)): F(1)}
        if res:
            P[(r, ())] = F(1)
        return P
    if t == 'B':
        return {(0, (('b', r, slot),)): F(1)}
    if t == 'C':
        P = {(0, (('c', r),)): F(1)}
        if kappa:
            P[(r, ())] = F(1, theta ** r)
        return P
    if t == 'N':
        return {(0, (('n', r),)): F(1)}
    raise ValueError(name)


def elem_expansion(B, e, pat):
    """u-expansion of the basis element's value at (a,b,c) under pole pattern pat."""
    alpha, gamma, kappa, theta = pat
    i, j, ci, ni = e
    f, g = B.km[i][0], B.km[j][0]
    h, s = B.cm[ci][0], B.nm[ni][0]
    base = ONE
    for nm in h:
        base = pmul(base, letter(nm, None, alpha, gamma, kappa, theta))
    for nm in s:
        base = pmul(base, letter(nm, None, alpha, gamma, kappa, theta))

    def side(fm, gm):
        P = ONE
        for nm in fm:
            P = pmul(P, letter(nm, 'b', alpha, gamma, kappa, theta))
        for nm in gm:
            P = pmul(P, letter(nm, 'c', alpha, gamma, kappa, theta))
        return P
    tot = side(f, g)
    if f != g:
        R = side(g, f)
        acc = defaultdict(F)
        for k, v in tot.items():
            acc[k] += v
        for k, v in R.items():
            acc[k] += v
        tot = {k: v for k, v in acc.items() if v}
    return pmul(tot, base)


# ---------------------------------------------------------------- pole patterns
def kummer_v(a, b, c, p):
    from math import comb

    def v(x):
        n = 0
        while x % p == 0:
            x //= p
            n += 1
        return n
    return v(comb(a + b, a)) + v(comb(a + c, a)) + v(comb(a + b + c, a))


def patterns(primes=(5, 7, 11, 13, 17, 19, 23)):
    """reachable (alpha,gamma,kappa,theta) with the MINIMAL depth cap 1+min(vT,2)."""
    caps = {}
    for p in primes:
        for a in range(1, p):
            for b in range(a + 1):
                for c in range(a + 1):
                    al = 1 if a + b >= p else 0
                    ga = 1 if a + c >= p else 0
                    eps = (b + c) // p
                    ka = 1 if a + b + c >= (eps + 1) * p else 0
                    th = eps + 1
                    if not ka:
                        th = 1
                    vT = kummer_v(a, b, c, p)
                    assert vT == al + ga + ka, (p, a, b, c, vT, al, ga, ka)
                    cap = 1 + min(vT, 2)
                    key = (al, ga, ka, th)
                    caps[key] = min(caps.get(key, 99), cap)
    return caps


if __name__ == '__main__':
    B = basis()
    print('basis size', len(B), flush=True)
    caps = patterns()
    print('reachable pole patterns (alpha,gamma,kappa,theta) -> min depth cap:')
    for k in sorted(caps):
        print('   ', k, '->', caps[k])
