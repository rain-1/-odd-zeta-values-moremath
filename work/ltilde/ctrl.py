"""CONTROL: how big are denominators of a GENERIC solution of L?  (calibrates the
strength of the 'den(s_n),den(Ph_n) | d_n^5' certificate)"""
import sys, math
from fractions import Fraction as F
from math import gcd
exec(open('prop.py').read().split('# ================= DENOMINATOR AUDIT')[0].replace("N=int",'#'))
def dlcm(n):
    L=1
    for i in range(1,n+1): L=L*i//gcd(L,i)
    return L
N=60
print("  n |  log10 den(X_n)  for: s (true)  Ph (true) | generic1  generic2  generic3 | log10 d_n^5")
gen=[(F(1),F(0),F(0),F(0)),(F(0),F(1),F(0),F(0)),(F(1),F(7),F(3),F(5))]
seqs={'s':propagate(*anch['s'],unlock3(*anch['s']),N),
      'Ph':propagate(*anch['Ph'],unlock3(*anch['Ph']),N)}
for i,g0 in enumerate(gen): seqs['g%d'%i]=propagate(*g0,N)
for n in [10,20,30,40,50,60]:
    d5=math.log10(dlcm(n)**5)
    r=[math.log10(seqs[k][n].denominator) if seqs[k][n].denominator>1 else 0.0 for k in ('s','Ph','g0','g1','g2')]
    print(f"  {n:3d} |   {r[0]:8.1f}  {r[1]:8.1f}  |  {r[2]:8.1f} {r[3]:8.1f} {r[4]:8.1f}  |  {d5:8.1f}")
print("\n  smooth-ness: does den(X_n) | d_n^5 ?  (n=0..%d)"%N)
for k in ('s','Ph','g0','g1','g2'):
    ok=sum(1 for n in range(N+1) if (dlcm(n)**5)%seqs[k][n].denominator==0)
    print(f"    {k:3s}: {ok:3d}/{N+1}")
