"""The COMBINED nested (Euler/coupled) contribution for target 3.

sum_{k,l} [ A r22 + 2B r12 + D r11 + 2A w5sym ] = 0  is target 3 (using
C_kl = B_lk, r21(k,l) = r12(l,k), D symmetric).  Its Euler/coupled part, read
off the fitted r-forms and folded with the k<->l symmetry of A and D, is

  N = 12 sum A (U14(k,l) - S14(k))
    +  4 sum A (U23(k,l) - S23(k))
    +  4 sum B S13(l)
    -  2 sum B U22(k,l)
    +  2 sum D U12(k,l).
"""
from fractions import Fraction as Fr
import t_struct as S
from alpha import S as Sum, U

for n in range(0, 7):
    t = [Fr(0)] * 5
    for k in range(n + 1):
        for l in range(n + 1):
            A, B, C, D = S.coefs(n, k, l)
            t[0] += 12 * A * (U(k, l, 1, 4) - Sum(k, 1, 4))
            t[1] += 4 * A * (U(k, l, 2, 3) - Sum(k, 2, 3))
            t[2] += 4 * B * Sum(l, 1, 3)
            t[3] += -2 * B * U(k, l, 2, 2)
            t[4] += 2 * D * U(k, l, 1, 2)
    print('n=%d' % n, flush=True)
    for nm, v in zip(['12 sA(U14-S14)', ' 4 sA(U23-S23)', ' 4 sB S13(l)  ',
                      '-2 sB U22     ', ' 2 sD U12     '], t):
        print('   %s = %s' % (nm, v), flush=True)
    print('   N              = %s' % sum(t, Fr(0)), flush=True)
