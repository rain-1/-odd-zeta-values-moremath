"""Sharper test at p = 2, 3: does Theorem 4.1 survive when a is allowed to run
past p (so the sample is no longer 2 or 6 cells)?

Two readings of the law are tested for n = a*p + r, 0 <= r < p, a = 1..AMAX:

  (i)  "digit" reading  : RHS built from a_a, b_a  and the SAME u(a,r)
  (ii) restricted a < p : the theorem as stated

We print, for each p, the minimum of v_p(LHS-RHS) over all cells at each order,
and the first cell where it drops below the claimed floor.
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/apdef')
from fractions import Fraction as F
from core import A, av, bv, vp
from gap_core import sigmas, Xi, Ur

AMAX = 60


def X(p, r):
    return sigmas(r)[0] + Xi(p, r)


def ar(r):
    return sum(A(r, s) for s in range(r + 1))


for p in (2, 3, 5, 7, 11):
    mins = {0: (99, None), 1: (99, None), 2: (99, None)}
    for a in range(1, AMAX + 1):
        for r in range(p):
            n = a * p + r
            us = [F(ar(r))]
            us.append(us[0] + 2 * p * a * Ur(r))
            us.append(us[1] + p ** 2 * a ** 2 * X(p, r))
            for name, Ln, La in (("a", F(av(n)), F(av(a))),
                                 ("b", p ** 3 * bv(n), bv(a))):
                for i, u in enumerate(us):
                    v = vp(Ln - La * u, p)
                    if v < mins[i][0]:
                        mins[i] = (v, (a, r, name))
    print(f"p = {p:>2}   a = 1..{AMAX}, all r < p   "
          f"(claimed floors: 1 / 2 / 3)")
    for i, need in ((0, 1), (1, 2), (2, 3)):
        v, cell = mins[i]
        ok = "ok " if v >= need else "*** BELOW FLOOR ***"
        print(f"        order p^{i+1}: min v_p = {v:>3}  {ok}  worst cell (a,r,row) = {cell}")
