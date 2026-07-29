from fractions import Fraction as F
from math import comb
import json, random, sys

def A(n,k):
    if k<0 or k>n: return 0
    return comb(n,k)**2*comb(n+k,k)**2
def H3(m): return sum(F(1,j**3) for j in range(1,m+1))
def lam(n): return (2*n+1)*(17*n*n+17*n+5)
d=json.load(open("sol1.json"))
mons1=[tuple(m) for m in d["mons"]]; sol1=[F(a,b) for a,b in d["sol"]]
def N1(n,k): return sum(c*F(n)**i*F(k)**j for (i,j),c in zip(mons1,sol1) if c)
def den1(n,k): return F(((n+1-k)*(n+k))**2)
def R1(n,k): return N1(n,k)/den1(n,k)
def Gval(n,k):
    if 0<=k<=n: return A(n,k)*R1(n,k)
    if k==n+1: return F(comb(2*n+1,n+1)**2)*N1(n,n+1)/F((n+1)**2*(2*n+1)**2)
    return F(0)
def LAval(n,k):
    return F((n+1)**3*A(n+1,k)-lam(n)*A(n,k)+n**3*A(n-1,k))
# where does pointwise LA = DeltaG fail?
for n in range(2,8):
    bad=[(k, LAval(n,k)-(Gval(n,k+1)-Gval(n,k))) for k in range(0,n+3)]
    bad=[(k,v) for k,v in bad if v!=0]
    print(n,"bad cells:",bad)
# boundary value Glim
for n in range(2,8):
    print(n,"Glim=",Gval(n,n+1), " N(n,n+1)=",N1(n,n+1))
