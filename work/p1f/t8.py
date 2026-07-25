"""T8: the Apery control, and the pole order of Apery-type letters.

(a) Apery zeta(3) with the CLASSICAL weight
        c(n,k) = H^(3)_n + sum_{m<=k} (-1)^{m-1} / (2 m^3 C(n,m) C(n+m,m))
    on T_A = C(n,k)^2 C(n+k,k)^2 : the base case n < p is CELL-WISE, min v_p(T_A c) = 0,
    no cancellation is used at all.  This is the mechanism (BASE) is missing.

(b) The letters R^(a)(n,k) = sum_{m<=k} (-1)^{m-1}/(m^a C(n,m) C(n+m,m)) have pole order
    exactly <= 1 for EVERY weight a, with pole indicator alpha = [n+k >= p] -- the same
    indicator as A_a(k) but 1/a of the depth.  This is Proposition 7.2 of PHASE2_CANCEL.md.
"""
import sys
from fractions import Fraction as F
from math import comb
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import vp, Hs

PR = [5, 7, 11, 13, 17, 19]


def c(n, k):
    s = Hs(n, 3)
    for m in range(1, k + 1):
        s += F((-1) ** (m - 1), 2 * m ** 3 * comb(n, m) * comb(n + m, m))
    return s


def R(n, k, a):
    s = F(0)
    for m in range(1, k + 1):
        s += F((-1) ** (m - 1), m ** a * comb(n, m) * comb(n + m, m))
    return s


print('(a) Apery zeta(3), classical weight: cell-wise v_p(T_A * c) for n < p')
for p in PR:
    worst, arg, wdep = 99, None, 0
    for n in range(1, p):
        for k in range(n + 1):
            TA = comb(n, k) ** 2 * comb(n + k, k) ** 2
            v = c(n, k)
            d = max(0, -vp(v, p)) if v else 0
            wdep = max(wdep, d)
            x = vp(TA, p) - d
            if x < worst:
                worst, arg = x, (n, k, vp(TA, p), d)
    print('    p=%2d  min = %d at (n,k,vT,depth)=%s ; max depth = %d' % (p, worst, arg, wdep))

print('(b) pole order of R^(a)(n,k), and its pole indicator')
for a in range(1, 6):
    mx, off = 0, 0
    for p in PR:
        for n in range(1, p):
            for k in range(n + 1):
                v = R(n, k, a)
                d = max(0, -vp(v, p)) if v else 0
                mx = max(mx, d)
                if d > 0 and n + k < p:
                    off += 1
    print('    a=%d : max pole order = %d ; poles with alpha = 0 : %d' % (a, mx, off))
