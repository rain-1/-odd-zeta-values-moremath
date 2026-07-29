"""Two-stage CT proof of b_n = Sum_k C(n,k)^2 C(n+k,k)^2 (2H3_n - H3_k).

Stage 0: sanity, c_n == b_n exactly n<=30.
Stage 1: find Zeilberger certificate R(n,k) for a_n summand A(n,k):
   (n+1)^3 A(n+1,k) - lam(n) A(n,k) + n^3 A(n-1,k) = Delta_k [A R].
Stage 2: with W(n,k)=2H3_n - H3_k, LF = Delta_k[A R W] + A*rho, where
   rho = rA(n,k)*R(n,k+1)/(k+1)^3 + 2[ (n+1+k)^2/(n+1-k)^2 - (n-k)^2/(n+k)^2 ]
   (rA = A(n,k+1)/A(n,k)); find Gosper sigma with rho = rA*sigma(k+1)-sigma(k).
Then Sum_k A*rho = 0 telescopes and L c_n = 0; initial values c_0=0,c_1=6 finish it.
"""
from fractions import Fraction as F
from math import comb
import itertools, sys

def A(n,k):
    if k<0 or k>n: return 0
    return comb(n,k)**2*comb(n+k,k)**2
def H3(m): return sum(F(1,j**3) for j in range(1,m+1))
def lam(n): return (2*n+1)*(17*n*n+17*n+5)

# stage 0
b=[F(0),F(6)]
for n in range(1,30):
    b.append((lam(n)*b[n]-n**3*b[n-1])/F((n+1)**3))
ok0=all(sum(A(n,k)*(2*H3(n)-H3(k)) for k in range(n+1))==b[n] for n in range(30))
print("stage0 c_n==b_n n<30:",ok0)

# generic exact linear solver (Gaussian elimination over Fraction)
def solve(rows, ncols):
    # rows: list of (coeffs list, rhs). returns particular solution or None
    M=[list(r)+[rhs] for r,rhs in rows]
    piv=[]
    r=0
    for c in range(ncols):
        p=None
        for i in range(r,len(M)):
            if M[i][c]!=0: p=i;break
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        inv=F(1)/M[r][c]
        M[r]=[x*inv for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                f=M[i][c]
                M[i]=[a-f*bb for a,bb in zip(M[i],M[r])]
        piv.append(c); r+=1
        if r==len(M): break
    # consistency
    for i in range(r,len(M)):
        if M[i][ncols]!=0: return None
    sol=[F(0)]*ncols
    for i,c in enumerate(piv): sol[c]=M[i][ncols]
    return sol

def find_rat(target, deg_n, deg_k, den, pts):
    """find polynomial N(n,k) with N/den(n,k) satisfying:
       target(n,k) = rA(n,k)*X(n,k+1) - X(n,k), X=N/den, at all pts.
       monomials n^i k^j, i<=deg_n, j<=deg_k."""
    mons=[(i,j) for i in range(deg_n+1) for j in range(deg_k+1)]
    rows=[]
    for (n,k) in pts:
        rA=F(((n-k)*(n+k+1))**2,(k+1)**4)
        d1=den(n,k+1); d0=den(n,k)
        if d1==0 or d0==0: continue
        co=[rA*F(n**i*(k+1)**j,1)/d1 - F(n**i*k**j,1)/d0 for i,j in mons]
        rows.append((co, target(n,k)))
    sol=solve(rows,len(mons))
    return mons,sol

# Stage 1: certificate for a_n. target1 = LA/A
def target1(n,k):
    return F((n+1)**3*(n+1+k)**2,(n+1-k)**2) - lam(n) + F(n**3*(n-k)**2,(n+k)**2)
den1=lambda n,k: F(((n+1-k)*(n+k))**2)
pts=[(n,k) for n in range(3,26) for k in range(1,n) if k!=n]  # avoid poles
import random
random.seed(1); pts=random.sample(pts,140)
mons1,sol1=find_rat(target1,5,8,den1,pts)
print("stage1 solved:",sol1 is not None)
if sol1 is None: sys.exit(1)

def Npoly(mons,sol,n,k): return sum(c*n**i*k**j for (i,j),c in zip(mons,sol) if c)
def R1(n,k): return Npoly(mons1,sol1,n,k)/den1(n,k)

# verify stage1 identity on fresh grid (out of sample)
bad=0
for n in range(26,34):
    for k in range(1,n):
        if target1(n,k)!=F(((n-k)*(n+k+1))**2,(k+1)**4)*R1(n,k+1)-R1(n,k): bad+=1
print("stage1 holdout mismatches:",bad)
# boundary: G_a(n,k)=A(n,k)R1(n,k) must vanish at k=0 and k=n+1 limit
print("k=0: N(n,0)==0 for n in 3..12:",all(Npoly(mons1,sol1,n,0)==0 for n in range(3,13)))
# k-degree structure / k^4 divisibility check
print("k^j coeffs j<4 all zero:",all(c==0 for (i,j),c in zip(mons1,sol1) if j<4))

import json
json.dump({"mons":[list(m) for m in mons1],"sol":[[c.numerator,c.denominator] for c in sol1]},open("sol1.json","w"))

# Stage 2: rho
def rho(n,k):
    # rA(n,k)*R1(n,k+1) simplifies to N(n,k+1)/(k+1)^4 (denominator cancels exactly)
    return Npoly(mons1,sol1,n,k+1)/F((k+1)**7) + 2*(F((n+1+k)**2,(n+1-k)**2)-F((n-k)**2,(n+k)**2))
# check Sum_k A rho == 0
ok2=all(sum(A(n,k)*rho(n,k) for k in range(n+1))==0 for n in range(2,16))
print("stage2 Sum A*rho==0 n=2..15:",ok2)

# Gosper for rho: rho = rA*sigma(k+1)-sigma(k)
for dn,dk,denf,tag in [(6,10,lambda n,k:F(((n+1-k)*(n+k))**2*(k if k>0 else 1)**0),"d1"),
                       (7,12,lambda n,k:F(((n+1-k)*(n+k))**2*k**3) if k!=0 else F(0),"d2"),
                       (7,12,lambda n,k:F(((n+1-k)*(n+k))**2*(k+n)**0*(k**2 if k else 1)),"d3")]:
    pts2=[(n,k) for n in range(3,30) for k in range(1,n)]
    pts2=random.sample(pts2,240)
    mons2,sol2=find_rat(rho,dn,dk,denf,pts2)
    print("stage2 gosper",tag,"solved:",sol2 is not None)
    if sol2 is not None:
        def R2(n,k,m=mons2,s=sol2,d=denf): return Npoly(m,s,n,k)/d(n,k)
        bad=0
        for n in range(30,36):
            for k in range(1,n):
                rA=F(((n-k)*(n+k+1))**2,(k+1)**4)
                if rho(n,k)!=rA*R2(n,k+1)-R2(n,k): bad+=1
        print("  holdout mismatches:",bad)
        nz=[( (i,j),c) for (i,j),c in zip(mons2,sol2) if c]
        print("  nonzero monomials:",len(nz))
        break
