"""Diagnose the failing (sequence,prime) pairs: what is v_p(B_n) really?
Is the pole absent (=> the correct local weight is different)?"""
import math
from fractions import Fraction as F
from sporadic import SEQS, gen_A, gen_B

PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
N = 200
W = {'A':2,'B':2,'C':2,'D':2,'E':2,'F':2,'alpha':3,'gamma':3,'delta':3,'eps':3,
     'zeta':3,'eta':3,'s7':2,'s10':2,'s18':2}
INF = 10**6
def vp_int(x, p):
    if x == 0: return INF
    v = 0
    while x % p == 0: x //= p; v += 1
    return v
def vp(x, p):
    if x == 0: return INF
    return vp_int(x.numerator, p) - vp_int(x.denominator, p)

print("For each sequence & prime: wloc := -min_{n<p^2} v_p(B_n)  (observed local pole depth),")
print("then master floor with that wloc.  chi columns: (-3/p), (-4/p), (5/p)\n")
for lab, fam, par, fn, note in SEQS:
    A = gen_A(fam, par, N); B = gen_B(fam, par, N); w = W[lab]
    line = []
    for p in PRIMES:
        M = min(N, p*p - 1)
        wloc = -min(vp(B[n], p) for n in range(1, M+1))
        wloc = max(wloc, 0)
        # master floor using local weight wloc, over n <= min(N, p^2-1) (single digit q<p)
        pw = F(p)**wloc
        fl = min(vp(pw*B[n]*A[n//p] - B[n//p]*A[n], p) for n in range(1, M+1))
        # global master floor over all n<=N using nominal w
        pwn = F(p)**w
        flg = min(vp(pwn*B[n]*A[n//p] - B[n//p]*A[n], p) for n in range(1, N+1))
        c3 = 1 if p % 3 == 1 else (-1 if p % 3 == 2 else 0)
        c4 = 1 if p % 4 == 1 else -1
        c5 = 1 if p % 5 in (1, 4) else (-1 if p % 5 in (2, 3) else 0)
        line.append((p, wloc, fl, flg, c3, c4, c5))
    print(f'--- {lab:6s} (nominal w={w})   {note}')
    print('    p      :', ' '.join(f'{t[0]:>4}' for t in line))
    print('    wloc   :', ' '.join(f'{t[1]:>4}' for t in line))
    print('    SDfloor:', ' '.join(f'{t[2]:>4}' for t in line))
    print('    Mfloor :', ' '.join(f'{t[3]:>4}' for t in line))
    print('    (-3|p) :', ' '.join(f'{t[4]:>4}' for t in line))
    print('    (-4|p) :', ' '.join(f'{t[5]:>4}' for t in line))
    print('    ( 5|p) :', ' '.join(f'{t[6]:>4}' for t in line))
    print()
