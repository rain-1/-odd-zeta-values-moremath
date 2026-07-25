"""P1h R1: fresh sweep of (REC-*) in normalized form.

(REC-*)   11907*P_{n0} - 334374*P_{n0+1} - 19292*P_{n0+2} == 0  (mod p),  n0=(p-5)/2.

Also: tightness (exact v_p of the combination), the same for Q and Phat (controls),
and the excess valuation of c3(n0).
"""
import sys
from fractions import Fraction as F
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import P, Ph, Q, vp, a0, c0, c1, c2, c3

R = (11907, -334374, -19292)
PRIMES=[p for p in range(7,200) if all(p%d for d in range(2,int(p**.5)+1))]

def phi(seq,n0):
    return R[0]*seq(n0)+R[1]*seq(n0+1)+R[2]*seq(n0+2)

print('%4s %4s | %-8s %-8s %-8s | %-6s %-8s %-8s'%('p','n0','v(phiP)','v(phiQ)','v(phiPh)','v(c3)','v(a0(n0))','v(P_{n0..+2}) min'))
bad=[]; nontight=[]
for p in PRIMES:
    n0=(p-5)//2
    vP=vp(phi(P,n0),p); vQ=vp(phi(Q,n0),p); vH=vp(phi(Ph,n0),p)
    vc3=vp(c3(n0),p); va0=vp(a0(n0),p)
    mn=min(vp(P(n0+s),p) for s in range(3))
    print('%4d %4d | %-8s %-8s %-8s | %-6d %-8d %-8d'%(p,n0,
          ('inf' if vP>10**8 else vP),('inf' if vQ>10**8 else vQ),('inf' if vH>10**8 else vH),
          vc3,va0,mn))
    if vP<1: bad.append(p)
    if vP!=1: nontight.append((p,vP,vc3))
print()
print('FAILURES (v_p(phi(P))<1):',bad)
print('non-tight (v_p(phi(P)) != 1):',nontight)
print('primes swept:',len(PRIMES))
