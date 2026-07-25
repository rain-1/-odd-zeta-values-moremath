"""Exact check of the harmonic cell-wise weight for Apery's zeta(3)."""
import sys
from fractions import Fraction as F
from math import comb
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g')
from core import Hs, vp
from rlet import R_exact
import numpy as np
# solve exactly over Q in the 22-col harmonic basis, with the u^3 condition
LET=['A1','A2','A3','B1','B2','B3']
def monos(letters,wmax,maxfac):
    wt={a:int(a[1]) for a in letters}; names=sorted(wt); res={():0}; cur=[((),0)]
    for _ in range(maxfac):
        nxt=[]
        for mono,w in cur:
            st=names.index(mono[-1]) if mono else 0
            for i in range(st,len(names)):
                if w+wt[names[i]]<=wmax:
                    nm=mono+(names[i],)
                    if nm not in res: res[nm]=w+wt[names[i]]; nxt.append((nm,w+wt[names[i]]))
        cur=nxt
    return res
KM=sorted(monos(LET,3,3).items()); NM=sorted(monos(['N1','N2','N3'],3,3).items())
ELS=[(i,j) for i,(_,wk) in enumerate(KM) for j,(_,wn) in enumerate(NM) if wk+wn==3]
def kl(nm,n,k):
    t,r=nm[0],int(nm[1])
    return (Hs(n+k,r)-Hs(k,r)) if t=='A' else (Hs(n-k,r)-Hs(k,r))
def val(e,n):
    i,j=e; tot=F(0)
    for k in range(n+1):
        v=F(comb(n,k)**2*comb(n+k,k)**2)
        for nm in KM[i][0]: v*=kl(nm,n,k)
        tot+=v
    for nm in NM[j][0]: tot*=Hs(n,int(nm[1]))
    return tot
def a_exact(n):
    return sum(comb(n,k)**2*comb(n+k,k)**2*(Hs(n,3)+F(1,2)*R_exact(n,k,3)) for k in range(n+1))
# exact rational rref
NLV=14
rows=[[val(e,n) for e in ELS]+[a_exact(n)] for n in range(1,NLV+1)]
# u^3 condition: coefficient sum over monomials of u-degree 3 at alpha=1 (A3, A1*A2, A1*A1*A1)
cond=[F(0)]*len(ELS)+[F(0)]
for c,(i,j) in enumerate(ELS):
    mono=KM[i][0]
    if NM[j][0]: continue
    d=sum(int(m[1]) for m in mono if m[0]=='A')
    if d==3: cond[c]+=F(1)
rows.append(cond)
Mx=[r[:] for r in rows]; nc=len(ELS); piv=[]; r=0
for c in range(nc):
    pr=None
    for i in range(r,len(Mx)):
        if Mx[i][c]!=0: pr=i;break
    if pr is None: continue
    Mx[r],Mx[pr]=Mx[pr],Mx[r]
    pv=Mx[r][c]; Mx[r]=[x/pv for x in Mx[r]]
    for i in range(len(Mx)):
        if i!=r and Mx[i][c]!=0:
            f=Mx[i][c]; Mx[i]=[a-f*b for a,b in zip(Mx[i],Mx[r])]
    piv.append(c); r+=1
inc=any(all(x==0 for x in row[:-1]) and row[-1]!=0 for row in Mx)
print('exact-Q rank=%d inconsistent=%s'%(r,inc))
x=[F(0)]*nc
for i,c in enumerate(piv): x[c]=Mx[i][-1]
lab=lambda e:'[%s]x[%s]'%('*'.join(KM[e[0]][0]) or '1','*'.join(NM[e[1]][0]) or '1')
sol={lab(ELS[c]):x[c] for c in range(nc) if x[c]!=0}
print('solution:',sol)
def w3(n,k):
    tot=F(0)
    for c in range(nc):
        if x[c]==0: continue
        i,j=ELS[c]; v=x[c]
        for nm in KM[i][0]: v*=kl(nm,n,k)
        for nm in NM[j][0]: v*=Hs(n,int(nm[1]))
        tot+=v
    return tot
bad=0
for n in range(1,25):
    if sum(comb(n,k)**2*comb(n+k,k)**2*w3(n,k) for k in range(n+1))!=a_exact(n): bad+=1;print('  MISMATCH n=',n)
print('exact identity n=1..24 : %d mismatches'%bad)
tot=0
for p in (5,7,11,13,17,19,23):
    v=0
    for n in range(1,p):
        for k in range(n+1):
            TA=comb(n,k)**2*comb(n+k,k)**2
            W=w3(n,k)-Hs(n,3)
            d=max(0,-vp(W,p)) if W else 0
            if d>vp(TA,p): v+=1
    tot+=v; print('  p=%2d cellwise d3<=vT violations: %d'%(p,v))
print('TOTAL cellwise violations: %d'%tot)
