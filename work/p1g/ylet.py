"""P1g: exact nested INTERVAL letters and verification of their pole structure.

  Y_ab(n,k)   = sum_{k   < m2 < m1 <= n+k}     m1^-a m2^-b
  V_ab(n,m)   = sum_{m   < m2 < m1 <= n+m}     m1^-a m2^-b     (m = k+l <= 2n)
  Z_ab(n)     = sum_{1  <= m2 < m1 <= n}       m1^-a m2^-b
Claim: for p>=5, n<p the open interval carries at most ONE multiple of p, hence
  pole order = max(a,b) (NOT a+b), with indicator alpha (resp. kappa).
"""
import sys
from fractions import Fraction as F
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import vp

def Y(n,k,a,b):
    s=F(0)
    for m1 in range(k+2, n+k+1):
        for m2 in range(k+1, m1):
            s += F(1, m1**a * m2**b)
    return s

def V(n,m,a,b):
    return Y(n,m,a,b)

PAIRS=[(a,b) for a in range(1,5) for b in range(1,5) if 2<=a+b<=5]
PR=[5,7,11,13,17,19]
print('Y_ab (k-slot): pole order vs max(a,b), indicator alpha')
badY=0
for (a,b) in PAIRS:
    mx=0; off=0; over=0
    for p in PR:
        for n in range(1,p):
            for k in range(n+1):
                v=Y(n,k,a,b); d=max(0,-vp(v,p)) if v else 0
                mx=max(mx,d)
                if d>0 and n+k<p: off+=1
                if d>max(a,b): over+=1
    badY+=off+over
    print('   (a,b)=(%d,%d) w=%d : max order=%d (bound max(a,b)=%d) ; off-alpha=%d ; over-bound=%d'
          %(a,b,a+b,mx,max(a,b),off,over))
print('V_ab (coupling): pole order vs max(a,b), indicator kappa')
badV=0
for (a,b) in PAIRS:
    mx=0; off=0; over=0
    for p in PR:
        for n in range(1,p):
            for m in range(2*n+1):
                eps=m//p
                v=V(n,m,a,b); d=max(0,-vp(v,p)) if v else 0
                mx=max(mx,d)
                ka = 1 if n+m >= (eps+1)*p else 0
                if d>0 and not ka: off+=1
                if d>max(a,b): over+=1
    badV+=off+over
    print('   (a,b)=(%d,%d) w=%d : max order=%d (bound %d) ; off-kappa=%d ; over-bound=%d'
          %(a,b,a+b,mx,max(a,b),off,over))
print('TOTAL violations: Y=%d V=%d'%(badY,badV))
