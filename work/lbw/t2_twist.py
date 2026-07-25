"""At the failing primes (chi(p)=-1), test candidate repairs:
 (S+) p^w B_n A_q + B_q A_n            (sign flip)
 (2S) p^{2w} B_n A_{q2} - eps B_{q2} A_n , q2 = floor(n/p^2)   (two-step / Frob^2 descent)
"""
import math
from fractions import Fraction as F
from sporadic import SEQS, gen_A, gen_B

W = {'A':2,'B':2,'C':2,'D':2,'E':2,'F':2,'alpha':3,'gamma':3,'delta':3,'eps':3,
     'zeta':3,'eta':3,'s7':2,'s10':2,'s18':2}
CHI = {'B':(-3,), 'C':(-3,), 'F':(-3,), 'zeta':(-3,), 's18':(-3,), 'E':(-4,), 'eta':(5,)}
INF = 10**6
def vp_int(x, p):
    if x == 0: return INF
    v = 0
    while x % p == 0: x //= p; v += 1
    return v
def vp(x, p):
    if x == 0: return INF
    return vp_int(x.numerator, p) - vp_int(x.denominator, p)
def kron(d, p):
    if d == -3: return 1 if p % 3 == 1 else (-1 if p % 3 == 2 else 0)
    if d == -4: return 1 if p % 4 == 1 else -1
    if d == 5:  return 1 if p % 5 in (1,4) else (-1 if p % 5 in (2,3) else 0)

PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31]
for lab, fam, par, fn, note in SEQS:
    if lab not in CHI: continue
    d = CHI[lab][0]; w = W[lab]
    N = 1500
    A = gen_A(fam, par, N); B = gen_B(fam, par, N)
    print(f'=== {lab}  w={w}  chi = ({d}|.)')
    for p in PRIMES:
        c = kron(d, p)
        if c != -1: continue
        M2 = min(N, p*p - 1)          # 2-digit range: q < p
        M3 = min(N, p**3 - 1)         # 3-digit range: q2 < p
        pw = F(p)**w; p2w = F(p)**(2*w)
        f_minus = min(vp(pw*B[n]*A[n//p] - B[n//p]*A[n], p) for n in range(1, M2+1))
        f_plus  = min(vp(pw*B[n]*A[n//p] + B[n//p]*A[n], p) for n in range(1, M2+1))
        g_minus = min(vp(p2w*B[n]*A[n//p**2] - B[n//p**2]*A[n], p) for n in range(1, M3+1))
        g_plus  = min(vp(p2w*B[n]*A[n//p**2] + B[n//p**2]*A[n], p) for n in range(1, M3+1))
        print(f'  p={p:3d} (chi=-1)  1-step[-]={f_minus:>4} 1-step[+]={f_plus:>4}   '
              f'2-step[-]={g_minus:>4} 2-step[+]={g_plus:>4}   (target w={w}, 2w={2*w}) n<={M3}')
    # control: a chi=+1 prime
    for p in PRIMES:
        if kron(d, p) != 1: continue
        M3 = min(N, p**3 - 1); p2w = F(p)**(2*w)
        g_minus = min(vp(p2w*B[n]*A[n//p**2] - B[n//p**2]*A[n], p) for n in range(1, M3+1))
        print(f'  p={p:3d} (chi=+1 control)  2-step[-]={g_minus:>4}')
        break
    print(flush=True)
