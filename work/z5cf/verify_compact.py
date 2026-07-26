"""INDEPENDENT exact verification of the compact closed forms.

Written directly from the closed formulas (not from the fitted coefficient vectors),
in exact Fraction arithmetic, using core.T / core.Hs and the exact BZ ladders.

    alpha := A1(k) - A1(l),   beta := B1(k) - B1(l)
    A_r(x) = H^(r)_{n+x} - H^(r)_x ,  B_r(x) = H^(r)_{n-x} - H^(r)_x

  w3(n,k,l) = 2 H^(3)_k - H^(3)_{n+k} - 2 beta H^(2)_k - (1/2) alpha H^(2)_{n+k}
  w5(n,k,l) = H^(5)_{n+k} + (1/2)(alpha-beta) H^(4)_{n+k}
              + (1/4)[ A2(k) + A2(l) - alpha^2 - 2 alpha beta ] H^(3)_{n+k}

  claim:  sum_{k,l=0}^{n} T(n,k,l) w3 = Phat_n ,  sum T w5 = P_n .
"""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import T, Hs, Ph, P, Q, rec_residual

NS = list(range(0, 35))


def parts(n, k, l):
    A1k = Hs(n + k, 1) - Hs(k, 1)
    A1l = Hs(n + l, 1) - Hs(l, 1)
    B1k = Hs(n - k, 1) - Hs(k, 1)
    B1l = Hs(n - l, 1) - Hs(l, 1)
    A2k = Hs(n + k, 2) - Hs(k, 2)
    A2l = Hs(n + l, 2) - Hs(l, 2)
    return A1k - A1l, B1k - B1l, A2k, A2l


def w3(n, k, l):
    al, be, _, _ = parts(n, k, l)
    return (2 * Hs(k, 3) - Hs(n + k, 3)
            - 2 * be * Hs(k, 2) - F(1, 2) * al * Hs(n + k, 2))


def w5(n, k, l):
    al, be, A2k, A2l = parts(n, k, l)
    return (Hs(n + k, 5)
            + F(1, 2) * (al - be) * Hs(n + k, 4)
            + F(1, 4) * (A2k + A2l - al * al - 2 * al * be) * Hs(n + k, 3))


def S(n, w):
    return sum(T(n, k, l) * w(n, k, l) for k in range(n + 1) for l in range(n + 1))


print('EXACT verification of the compact forms')
print(' %-4s %-10s %-10s' % ('n', 'w3 -> Phat', 'w5 -> P'))
bad3, bad5 = [], []
S3, S5 = {}, {}
for n in NS:
    v3 = S(n, w3); v5 = S(n, w5)
    S3[n], S5[n] = v3, v5
    ok3 = (v3 == Ph(n)); ok5 = (v5 == P(n))
    if not ok3:
        bad3.append(n)
    if not ok5:
        bad5.append(n)
    print(' %-4d %-10s %-10s' % (n, 'OK' if ok3 else 'FAIL', 'OK' if ok5 else 'FAIL'), flush=True)
print('\nw3: %s      w5: %s'
      % ('ALL PASS n=0..%d' % NS[-1] if not bad3 else 'FAIL %s' % bad3,
         'ALL PASS n=0..%d' % NS[-1] if not bad5 else 'FAIL %s' % bad5))

print('\nOPERATOR CHECK: L_BZ applied to the summed sequences (order 3, needs n..n+3)')
r3 = [n for n in NS[:-3] if rec_residual(lambda m: S3[m], n) != 0]
r5 = [n for n in NS[:-3] if rec_residual(lambda m: S5[m], n) != 0]
print('  L_BZ[sum T w3] = 0 for n = 0..%d : %s' % (NS[-4], 'ALL ZERO' if not r3 else 'nonzero at %s' % r3))
print('  L_BZ[sum T w5] = 0 for n = 0..%d : %s' % (NS[-4], 'ALL ZERO' if not r5 else 'nonzero at %s' % r5))
