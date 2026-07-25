"""g_opt.py -- how much of the denominator budget can the weight-3 Rhin-Viola
group remove?  Scale-free maximisation of  delta / (2 m1 + m2).

The number that matters for zeta_5(3):  the p-adic weight-3 construction has
budget d_n^3 (= 3 per n at direction scale 1) and a margin deficit of 0.586.
A group saving of  delta_norm := 3 * delta/(2 m1 + m2)  is what the orbit method
contributes at that budget.  We need delta_norm > 0.586 (plus whatever the
smallness/growth ratio loses when leaving the symmetric point).
"""

import itertools
import sys
from fractions import Fraction as F

from g_group import (GROUP, F_IDX, c_matrix, admissible, m_params,
                     delta_limit, orbit_F_multisets)


def sweep(total_max=40, report_top=12, sigma_min=0):
    """All integral directions with sum(alpha)=sum(beta)=S <= total_max."""
    best = []
    seen = set()
    for S in range(sigma_min, total_max + 1):
        # beta_1 = 0 wlog (translation invariance of c is NOT available, but
        # RV's optimum has beta_1 = 0 and shifting all params keeps c fixed)
        for b2 in range(0, S + 1):
            for b3 in range(b2 + 1, S + 1):
                b4 = S - 0 - b2 - b3
                if b4 < b3:
                    continue
                beta = (0, b2, b3, b4)
                lo, hi = b2, b3
                if hi - lo < 2:
                    continue
                # alpha strictly between b2 and b3, summing to S
                rng = range(lo + 1, hi)
                for a in itertools.combinations_with_replacement(rng, 4):
                    if sum(a) != S:
                        continue
                    alpha = a
                    if not admissible(alpha, beta):
                        continue
                    key = (tuple(sorted(alpha)), beta)
                    if key in seen:
                        continue
                    seen.add(key)
                    m0, m1, m2, m3 = m_params(alpha, beta)
                    budget = 2 * m1 + m2
                    d, _, _ = delta_limit(alpha, beta)
                    best.append((d / budget, d, budget, alpha, beta, m1, m2))
    best.sort(reverse=True)
    return best


def main():
    total_max = int(sys.argv[1]) if len(sys.argv) > 1 else 34
    res = sweep(total_max)
    print(f"directions with sum <= {total_max}: {len(res)} admissible shapes")
    print(f"{'ratio':>10} {'delta':>10} {'budget':>7}  {'x3 (=budget-3 saving)':>22}"
          f"   alpha ; beta")
    for r, d, bu, al, be, m1, m2 in res[:15]:
        print(f"{r:10.6f} {d:10.5f} {bu:7d}  {3*r:22.6f}   {al} ; {be}")
    print()
    # explicit check of the RV point inside the sweep
    rv = [x for x in res if tuple(sorted(x[3])) == (16, 17, 18, 19)
          and x[4] == (0, 7, 31, 32)]
    if rv:
        print(f"RV optimum in sweep: ratio={rv[0][0]:.6f}, delta={rv[0][1]:.5f}")
    top = res[0]
    print(f"\nBEST ratio = {top[0]:.6f} at alpha={top[3]}, beta={top[4]}")
    print(f"   delta = {top[1]:.6f}, budget = {top[2]}")
    print(f"   => saving available at a budget-3 (weight-3) configuration: "
          f"{3*top[0]:.6f}")
    print(f"   target deficit for zeta_5(3): 0.586")


if __name__ == "__main__":
    main()
