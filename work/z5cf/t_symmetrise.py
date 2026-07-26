"""Check River's k<->l symmetrisation of the compact BZ weights, exactly over Q.

  X_r = H^(r)_{n+k},  Y_r = H^(r)_{n+l}
  A_r(x) = H^(r)_{n+x} - H^(r)_x,  B_r(x) = H^(r)_{n-x} - H^(r)_x
  alpha = A1(k)-A1(l),  beta = B1(k)-B1(l),  Psi = alpha/2 + beta     (all ANTIsymmetric)
  C = (A2(k)+A2(l))/4 - alpha*Psi/2                                    (SYMMETRIC)

  w3     = X3 - Psi*X2
  w3sym  = (X3+Y3)/2 - (Psi/2)(X2 - Y2)
  w5     = X5 + (alpha-beta)/2 * X4 + C*X3
  w5sym  = (X5+Y5)/2 + (alpha-beta)/4 * (X4-Y4) + (C/2)(X3+Y3)

Claims tested:
  (1) w3sym is the k<->l symmetrisation of w3, and likewise w5sym / w5   [algebra]
  (2) sum_{k,l} T*w3sym = sum T*w3 = Phat_n, same for w5 / P_n          [the point]
  (3) the ANTIsymmetric part of any weight is annihilated by the double sum
  (4) T(n,k,l) = T(n,l,k)
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from fractions import Fraction as F
from core import T, Hs

NMAX = 12


def letters(n, k, l):
    A = lambda r, x: Hs(n + x, r) - Hs(x, r)
    B = lambda r, x: Hs(n - x, r) - Hs(x, r)
    al = A(1, k) - A(1, l)
    be = B(1, k) - B(1, l)
    Ps = al / 2 + be
    C = (A(2, k) + A(2, l)) / 4 - al * Ps / 2
    return al, be, Ps, C


def w3(n, k, l):
    _, _, Ps, _ = letters(n, k, l)
    return Hs(n + k, 3) - Ps * Hs(n + k, 2)


def w5(n, k, l):
    al, be, Ps, C = letters(n, k, l)
    return Hs(n + k, 5) + (al - be) / 2 * Hs(n + k, 4) + C * Hs(n + k, 3)


def w3sym(n, k, l):
    _, _, Ps, _ = letters(n, k, l)
    X3, Y3 = Hs(n + k, 3), Hs(n + l, 3)
    X2, Y2 = Hs(n + k, 2), Hs(n + l, 2)
    return (X3 + Y3) / 2 - Ps / 2 * (X2 - Y2)


def w5sym(n, k, l):
    al, be, Ps, C = letters(n, k, l)
    X5, Y5 = Hs(n + k, 5), Hs(n + l, 5)
    X4, Y4 = Hs(n + k, 4), Hs(n + l, 4)
    X3, Y3 = Hs(n + k, 3), Hs(n + l, 3)
    return (X5 + Y5) / 2 + (al - be) / 4 * (X4 - Y4) + C / 2 * (X3 + Y3)


def dsum(n, w):
    return sum((F(T(n, k, l)) * w(n, k, l)
                for k in range(n + 1) for l in range(n + 1)), F(0))


bad = {k: 0 for k in ('Tsym', 'alg3', 'alg5', 'sum3', 'sum5', 'anti3', 'anti5')}
for n in range(NMAX + 1):
    for k in range(n + 1):
        for l in range(n + 1):
            if T(n, k, l) != T(n, l, k):
                bad['Tsym'] += 1
            # (1) symmetrisation identity, cell by cell
            if w3sym(n, k, l) != (w3(n, k, l) + w3(n, l, k)) / 2:
                bad['alg3'] += 1
            if w5sym(n, k, l) != (w5(n, k, l) + w5(n, l, k)) / 2:
                bad['alg5'] += 1
    # (2) the double sums agree
    s3, s3s = dsum(n, w3), dsum(n, w3sym)
    s5, s5s = dsum(n, w5), dsum(n, w5sym)
    if s3 != s3s:
        bad['sum3'] += 1
    if s5 != s5s:
        bad['sum5'] += 1
    # (3) antisymmetric parts are in the kernel of the double sum
    a3 = dsum(n, lambda N, K, L: (w3(N, K, L) - w3(N, L, K)) / 2)
    a5 = dsum(n, lambda N, K, L: (w5(N, K, L) - w5(N, L, K)) / 2)
    if a3 != 0:
        bad['anti3'] += 1
    if a5 != 0:
        bad['anti5'] += 1
    if n <= 4:
        print(f"  n={n}:  Phat = {s3}   (sym form: {s3s})")
        print(f"         P    = {s5}   (sym form: {s5s})")

print()
print(f"n = 0..{NMAX}, all cells.  Failures:")
for key, v in bad.items():
    print(f"   {key:>6}: {v}")
