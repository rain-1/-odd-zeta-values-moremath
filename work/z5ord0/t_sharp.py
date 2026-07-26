"""SHARP index ranges for the three vanishing facts.

Objects (Barnes-translated, x = s+n+1, y = t+n+1):

  R_n(x,y) = prod_{i=1}^n (x-i)(y-i)(x+y-i) / [prod_{i=0}^n (x+i)^2 (y+i)^2]

  g_l(x) = lim_{y->-l}(y+l)^2 R_n(x,y)          (the DOUBLE-y coefficient)
         = c_l P1(x) P2(x) / prod_{i=0}^n (x+i)^2
         P1(x) = prod_{r=1}^n (x-r),  P2(x) = prod_{r=1}^n (x-l-r)
         c_l   = prod_{r=1}^n(-l-r) / prod_{i!=l}(i-l)^2   (nonzero)

  q_l(x) = d/dy[(y+l)^2 R_n]|_{y=-l}            (the SIMPLE-y coefficient)
         = g_l(x) Lambda_l(x),
         Lambda_l(x) = -sum_{i=1}^n 1/(l+i) + sum_{i=1}^n 1/(x-l-i)
                       - 2 sum_{i=0,i!=l}^n 1/(i-l)

Partial fractions:
  g_l(x) = sum_k [A_kl/(x+k)^2 + C_kl/(x+k)]
  q_l(x) = sum_k [C_kl/(x+k)^2 + D_kl/(x+k)]        (C_kl = B_lk, D symmetric)

PREDICTED SHARP RANGES (0 <= l <= n):

 (P1) ZEROS OF P1:  {1,...,n}.        ZEROS OF P2: {l+1,...,l+n}.
      Their union is exactly {1,...,n+l} (because l <= n), their intersection
      is exactly {l+1,...,n} (empty when l = n).

 (V1) g_l(j) = 0   EXACTLY for 1 <= j <= n+l.
      Sharp: g_l(n+l+1) != 0.

 (V2) g_l'(j) = 0  EXACTLY for l+1 <= j <= n  (the DOUBLE-zero overlap).
      Sharp: g_l'(j) != 0 at j = l (l>=1, simple zero of P1 only) and at
      j = n+1 (l>=1, simple zero of P2 only).

 (V3) q_l(j) = 0   EXACTLY for 1 <= j <= n -- the WHOLE first-factor range,
      not just 1 <= j <= l.  Reason: on 1 <= j <= l, g_l has a simple zero and
      Lambda_l(j) is finite; on l < j <= n, g_l has a DOUBLE zero while
      Lambda_l has a SIMPLE POLE (the diagonal log pole at x = l+i, i = j-l),
      so the product still vanishes to order one.
      Sharp: q_l(j) != 0 for n < j <= n+l, where g_l has only a simple zero
      against that same simple pole.
"""
import sys
from fractions import Fraction as Fr

import t_struct as S


def gval(n, l, x):
    return S.g(n, l, x)


def gprime(n, l, x):
    """g_l'(x) from the partial fractions -- the form used in the argument."""
    v = Fr(0)
    for k in range(n + 1):
        A, B, C, D = S.coefs(n, k, l)
        v += -2 * A / Fr(x + k) ** 3 - B / Fr(x + k) ** 2
    return v


def qval(n, l, x):
    """q_l(x) from the partial fractions sum_k [C/(x+k)^2 + D/(x+k)]."""
    v = Fr(0)
    for k in range(n + 1):
        A, B, C, D = S.coefs(n, k, l)
        v += C / Fr(x + k) ** 2 + D / Fr(x + k)
    return v


def qval_prod(n, l, x):
    """q_l(x) = g_l(x) Lambda_l(x), valid where Lambda_l has no pole."""
    return S.g(n, l, x) * S.Lam(n, l, x)


def main(nmax=12):
    bad = {k: [] for k in ('pf', 'v1', 'v1s', 'v2', 'v2s', 'v3', 'v3s')}
    cells = {k: 0 for k in bad}
    for n in range(nmax + 1):
        for l in range(n + 1):
            # --- q_l from partial fractions == g_l * Lambda_l (generic x)
            for x in (Fr(1, 3), Fr(9, 4), Fr(-2, 7), Fr(23, 5)):
                cells['pf'] += 1
                if qval(n, l, x) != qval_prod(n, l, x):
                    bad['pf'].append((n, l, x))
            # --- (V1) g_l(j) = 0 for 1 <= j <= n+l ; != 0 at n+l+1
            for j in range(1, n + l + 1):
                cells['v1'] += 1
                if gval(n, l, j) != 0:
                    bad['v1'].append((n, l, j))
            cells['v1s'] += 1
            if gval(n, l, n + l + 1) == 0:
                bad['v1s'].append((n, l, n + l + 1))
            # --- (V2) g_l'(j) = 0 exactly on l < j <= n
            for j in range(l + 1, n + 1):
                cells['v2'] += 1
                if gprime(n, l, j) != 0:
                    bad['v2'].append((n, l, j))
            for j in list(range(1, l + 1)) + list(range(n + 1, n + l + 1)):
                cells['v2s'] += 1
                if gprime(n, l, j) == 0:
                    bad['v2s'].append((n, l, j))
            # --- (V3) q_l(j) = 0 exactly on 1 <= j <= n
            for j in range(1, n + 1):
                cells['v3'] += 1
                if qval(n, l, j) != 0:
                    bad['v3'].append((n, l, j))
            for j in range(n + 1, n + l + 1):
                cells['v3s'] += 1
                if qval(n, l, j) == 0:
                    bad['v3s'].append((n, l, j))
    lab = {
        'pf':  'q_l from partial fractions == g_l * Lambda_l (generic x)',
        'v1':  '(V1) g_l(j)  = 0 on 1 <= j <= n+l',
        'v1s': '(V1 sharp) g_l(n+l+1) != 0',
        'v2':  "(V2) g_l'(j) = 0 on l < j <= n",
        'v2s': "(V2 sharp) g_l'(j) != 0 on 1<=j<=l and n<j<=n+l",
        'v3':  '(V3) q_l(j)  = 0 on 1 <= j <= n   <-- WHOLE first-factor range',
        'v3s': '(V3 sharp) q_l(j) != 0 on n < j <= n+l',
    }
    print('SHARP RANGES, exact over Q, n = 0..%d' % nmax)
    ok = True
    for k in ('pf', 'v1', 'v1s', 'v2', 'v2s', 'v3', 'v3s'):
        good = not bad[k]
        ok = ok and good
        print('  %-58s cells=%5d  %s' % (lab[k], cells[k],
                                         'PASS' if good else
                                         'FAIL %s' % bad[k][:4]))
    # a concrete witness at the boundary
    n, l = 6, 3
    print()
    print('  witnesses at n=%d, l=%d:' % (n, l))
    print('    g_l(n+l)   = %s   (last zero)' % gval(n, l, n + l))
    print('    g_l(n+l+1) = %s' % gval(n, l, n + l + 1))
    print("    g_l'(l)     = %s   (just below the overlap)" % gprime(n, l, l))
    print("    g_l'(l+1)   = %s   (first double zero)" % gprime(n, l, l + 1))
    print("    g_l'(n)     = %s   (last double zero)" % gprime(n, l, n))
    print("    g_l'(n+1)   = %s   (just above)" % gprime(n, l, n + 1))
    print('    q_l(n)     = %s   (last zero)' % qval(n, l, n))
    print('    q_l(n+1)   = %s' % qval(n, l, n + 1))
    print()
    print('OVERALL: %s' % ('ALL SHARP RANGES CONFIRMED' if ok else 'FAILURE'))
    return ok


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 12)
