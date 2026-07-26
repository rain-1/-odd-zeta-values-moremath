"""THE COMBINED TWO-VARIABLE OBJECT at lattice points -- evaluation tools for
target 3 that do NOT split the sum.

Everything below is about the single object

  R_n(x,y) = prod_{i=1}^n (x-i)(y-i)(x+y-i) / [prod_{i=0}^n (x+i)^2 (y+i)^2]

whose bivariate partial fractions are

  R_n(x,y) = sum_{k,l} [ A_kl/((x+k)^2 (y+l)^2) + B_kl/((x+k)(y+l)^2)
                       + C_kl/((x+k)^2 (y+l)) + D_kl/((x+k)(y+l)) ]      (PF2)

and which collapses, one variable at a time, to the residue families

  R_n(x,y) = sum_{l=0}^{n} [ g_l(x)/(y+l)^2 + q_l(x)/(y+l) ]             (L2)

  g_l(x) = lim_{y->-l}(y+l)^2 R_n,   q_l(x) = d/dy[(y+l)^2 R_n]|_{y=-l}.

(L2) is THE identity that expresses a whole row of the residue sum in terms of
g and q without touching the individual terms.  The point of this file is that
the numerator of R_n carries a THIRD product, prod(x+y-i), which is invisible in
g_l or q_l separately and which is exactly the anti-diagonal cancellation:

 (L1) for POSITIVE INTEGERS i,j:  R_n(i,j) = 0  <=>  min(i,j) <= n.
      (prod(x-i') kills i<=n, prod(y-i') kills j<=n, prod(x+y-i') kills i+j<=n
       -- and i+j<=n already implies min<=n, so the criterion is just min<=n.)

 (L3) for 1 <= j <= n, R_n(x,j) == 0 IDENTICALLY in x, hence
        sum_l [ g_l(x)/(j+l)^2 + q_l(x)/(j+l) ] == 0
      for EVERY x -- in particular at x = i > n, where NOT ONE summand vanishes.
      This is a cancellation that lives only in the combination.

 (L4) differentiating (L3): for 1 <= j <= n and every x,
        sum_l [ g_l'(x)/(j+l)^2 + q_l'(x)/(j+l) ] == 0.

 (L5) ANTI-DIAGONAL, the genuinely two-variable family: for 1 <= m <= n,
      R_n(x, m-x) == 0 identically in x, hence
        sum_l [ g_l(x)/(m-x+l)^2 + q_l(x)/(m-x+l) ] == 0.
      The pole locations move with x, so this is NOT a consequence of the
      one-variable facts (V1)/(V3) by partial fractions in x.
"""
import sys
from fractions import Fraction as Fr

import t_struct as S
import t_sharp as TS


def R(n, x, y):
    v = Fr(1)
    for i in range(1, n + 1):
        v *= Fr(x - i) * Fr(y - i) * Fr(x + y - i)
    for i in range(0, n + 1):
        v /= Fr(x + i) ** 2 * Fr(y + i) ** 2
    return v


def R_pf2(n, x, y):
    """R from the FULL bivariate partial fractions (PF2)."""
    v = Fr(0)
    for k in range(n + 1):
        for l in range(n + 1):
            A, B, C, D = S.coefs(n, k, l)
            v += (A / (Fr(x + k) ** 2 * Fr(y + l) ** 2)
                  + B / (Fr(x + k) * Fr(y + l) ** 2)
                  + C / (Fr(x + k) ** 2 * Fr(y + l))
                  + D / (Fr(x + k) * Fr(y + l)))
    return v


def row(n, x, y):
    """sum_l [ g_l(x)/(y+l)^2 + q_l(x)/(y+l) ]   -- the (L2) right-hand side."""
    v = Fr(0)
    for l in range(n + 1):
        v += S.g(n, l, x) / Fr(y + l) ** 2 + TS.qval(n, l, x) / Fr(y + l)
    return v


def row_prime(n, x, y):
    """sum_l [ g_l'(x)/(y+l)^2 + q_l'(x)/(y+l) ]"""
    v = Fr(0)
    for l in range(n + 1):
        v += TS.gprime(n, l, x) / Fr(y + l) ** 2 + qprime(n, l, x) / Fr(y + l)
    return v


def qprime(n, l, x):
    v = Fr(0)
    for k in range(n + 1):
        A, B, C, D = S.coefs(n, k, l)
        v += -2 * C / Fr(x + k) ** 3 - D / Fr(x + k) ** 2
    return v


GEN = (Fr(1, 3), Fr(9, 4), Fr(-2, 7), Fr(23, 5), Fr(17, 6))


def main(nmax=8):
    bad = {k: [] for k in ('pf2', 'l2', 'l1', 'l1s', 'l3', 'l4', 'l5')}
    cells = {k: 0 for k in bad}
    for n in range(nmax + 1):
        # --- (PF2) and (L2) at generic rational points
        for x in GEN:
            for y in GEN:
                cells['pf2'] += 1
                if R_pf2(n, x, y) != R(n, x, y):
                    bad['pf2'].append((n, x, y))
                cells['l2'] += 1
                if row(n, x, y) != R(n, x, y):
                    bad['l2'].append((n, x, y))
        # --- (L1) lattice vanishing, sharp
        for i in range(1, n + 4):
            for j in range(1, n + 4):
                v = R(n, i, j)
                if min(i, j) <= n:
                    cells['l1'] += 1
                    if v != 0:
                        bad['l1'].append((n, i, j))
                else:
                    cells['l1s'] += 1
                    if v == 0:
                        bad['l1s'].append((n, i, j))
        # --- (L3), (L4): j in 1..n, x generic AND x = i > n
        for j in range(1, n + 1):
            for x in list(GEN) + [Fr(n + 1), Fr(n + 2), Fr(2 * n + 3)]:
                cells['l3'] += 1
                if row(n, x, j) != 0:
                    bad['l3'].append((n, j, x))
                cells['l4'] += 1
                if row_prime(n, x, j) != 0:
                    bad['l4'].append((n, j, x))
        # --- (L5) anti-diagonal
        for m in range(1, n + 1):
            for x in GEN:
                cells['l5'] += 1
                if row(n, x, m - x) != 0:
                    bad['l5'].append((n, m, x))
    lab = {
        'pf2': '(PF2) full bivariate partial fractions == R_n',
        'l2':  '(L2)  R_n(x,y) = sum_l [g_l(x)/(y+l)^2 + q_l(x)/(y+l)]',
        'l1':  '(L1)  R_n(i,j) = 0 for positive integers with min(i,j) <= n',
        'l1s': '(L1 sharp) R_n(i,j) != 0 when min(i,j) > n',
        'l3':  '(L3)  row(x, j) = 0 for 1<=j<=n, EVERY x (incl. x>n)',
        'l4':  "(L4)  row'(x, j) = 0 for 1<=j<=n, EVERY x",
        'l5':  '(L5)  row(x, m-x) = 0 for 1<=m<=n  [ANTI-DIAGONAL]',
    }
    print('COMBINED-OBJECT EVALUATION TOOLS, exact over Q, n = 0..%d' % nmax)
    ok = True
    for k in ('pf2', 'l2', 'l1', 'l1s', 'l3', 'l4', 'l5'):
        good = not bad[k]
        ok = ok and good
        print('  %-56s cells=%5d  %s'
              % (lab[k], cells[k], 'PASS' if good else 'FAIL %s' % bad[k][:4]))
    # --- demonstrate that (L3) has NO vanishing summand
    n, j, x = 6, 3, Fr(9)
    print()
    print('  (L3) with NO vanishing summand: n=%d, j=%d, x=%d' % (n, j, x))
    tot = Fr(0)
    for l in range(n + 1):
        a = S.g(n, l, x) / Fr(x * 0 + j + l) ** 2
        b = TS.qval(n, l, x) / Fr(j + l)
        tot += a + b
        print('     l=%d : g_l(x)/(j+l)^2 = %-28s  q_l(x)/(j+l) = %s'
              % (l, a, b))
    print('     ---------------- sum = %s' % tot)
    print()
    print('OVERALL: %s' % ('ALL COMBINED-OBJECT TOOLS CONFIRMED' if ok
                           else 'FAILURE'))
    return ok


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 8)
