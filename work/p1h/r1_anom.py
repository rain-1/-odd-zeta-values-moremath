"""Diagnose the reported p=13 anomaly and the small-prime edge cases."""
import sys
from fractions import Fraction as F
from math import gcd
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import P, Ph, Q, vp, a0, c0, c1, c2, c3
R=(11907,-334374,-19292)
print('2^9 * c_i(-5/2) =', [F(2)**9*c for c in (F(83349,128),F(-1170309,64),F(-33761,32))])
print('  = 28 * R  ->  c_i(n0) == 28*2^-9 * R_i (mod p);  content 28=2^2*7 kills the row only at p=7')
print()
print('%4s %4s %-10s %-10s %-9s %-9s %-9s'%('p','n0','v_p(gcd c)','v_p(numRaw)','v_p(c3)','P1g slack','v_p(phi_R)'))
for p in [p for p in range(5,200) if all(p%d for d in range(2,int(p**.5)+1))]:
    n0=(p-5)//2
    cc=(c0(n0),c1(n0),c2(n0))
    g=gcd(gcd(cc[0],cc[1]),cc[2])
    raw=cc[0]*P(n0)+cc[1]*P(n0+1)+cc[2]*P(n0+2)
    phi=R[0]*P(n0)+R[1]*P(n0+1)+R[2]*P(n0+2)
    vr=vp(raw,p) if raw else 99
    vph=vp(phi,p) if phi else 99
    print('%4d %4d %-10d %-10s %-9d %-9d %-9s'%(p,n0,vp(g,p),vr,vp(c3(n0),p),vr-vp(c3(n0),p),vph))
    if p>47: break
