"""T3 -- the two-layer split of LBW_GENERAL's Theorem LB, executed for the compact forms.

    p^w Y_n = SUM_{p | T(n,k,l)} T w  +  SUM_{p nmid T} T w        (times p^w)
                 "vanishing layer"          "surviving layer"

Theorem LB needs (i) the vanishing layer  == 0 (mod p)  -- this is what (H4) tameness
buys, and (H4) FAILS here (arguments n+k, n+l reach 2n) -- and (ii) the surviving
layer  == Y_a Q_r (mod p), which follows from (H1),(H2),(H3),(H5), all verified.
So the whole question is (i).  Measured exactly.
"""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import T, Hs, Ph, P, Q, vp

BIG = 10 ** 9


def vpF(x, p):
    return vp(x, p) if x != 0 else BIG


def fmt(v):
    return 'inf' if v >= BIG else str(v)


def w3(n, k, l):
    al = (Hs(n + k, 1) - Hs(k, 1)) - (Hs(n + l, 1) - Hs(l, 1))
    be = (Hs(n - k, 1) - Hs(k, 1)) - (Hs(n - l, 1) - Hs(l, 1))
    return Hs(n + k, 3) - (F(1, 2) * al + be) * Hs(n + k, 2)


def w5(n, k, l):
    al = (Hs(n + k, 1) - Hs(k, 1)) - (Hs(n + l, 1) - Hs(l, 1))
    be = (Hs(n - k, 1) - Hs(k, 1)) - (Hs(n - l, 1) - Hs(l, 1))
    A2k = Hs(n + k, 2) - Hs(k, 2)
    A2l = Hs(n + l, 2) - Hs(l, 2)
    return (Hs(n + k, 5) + F(1, 2) * (al - be) * Hs(n + k, 4)
            + F(1, 4) * (A2k + A2l - al * al - 2 * al * be) * Hs(n + k, 3))


CASES = [('w3 -> Phat', w3, 3, Ph), ('w5 -> P', w5, 5, P)]
print('two-layer split, n = ap+r, 1 <= a < p, 0 <= r < p')
print(' %-11s %-4s %8s %14s %14s %14s' %
      ('form', 'p', 'cells', 'v(p^w*VANISH)', 'v(p^w*SURV -', 'v(p^w Y_n -'))
print(' %-11s %-4s %8s %14s %14s %14s' % ('', '', '', '(want >= 1)', ' Y_a Q_r)', ' Y_a Q_r)'))
for name, wf, wt, LAD in CASES:
    for p in (5, 7, 11):
        mv = ms = mt = BIG
        cells = 0
        NLIM = {5: 24, 7: 48, 11: 120}[p]
        for a in range(1, p):
            for r in range(p):
                n = a * p + r
                if n > NLIM:
                    continue
                cells += 1
                van = F(0); sur = F(0)
                for k in range(n + 1):
                    for l in range(n + 1):
                        t = T(n, k, l)
                        v = t * wf(n, k, l)
                        if t % p == 0:
                            van += v
                        else:
                            sur += v
                pw = F(p) ** wt
                mv = min(mv, vpF(pw * van, p))
                ms = min(ms, vpF(pw * sur - LAD(a) * Q(r), p))
                mt = min(mt, vpF(pw * LAD(n) - LAD(a) * Q(r), p))
        print(' %-11s %-4d %8d %14s %14s %14s'
              % (name, p, cells, fmt(mv), fmt(ms), fmt(mt)), flush=True)
