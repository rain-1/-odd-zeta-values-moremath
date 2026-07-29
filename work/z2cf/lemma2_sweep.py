"""LEMMA 2 target: Sum_k S*j = 0, S*j := LF_X + S(n+1,k) + S(n-1,k),
X = h1(2h1-h2-h3). Enlarged null library: levels n-1,n,n+1; rho in
{1,z,z^2,z^3,P,zP,Q,zQ}; cell certificate over ALL19 channels."""
import sys, os, json, random
sys.path.insert(0, "work/z2cf")
from fractions import Fraction as F
from math import comb
import numpy as np
from z2direct import shift_expr, mono_val, S, lam0
P0=2147483647
def inv(a,p=P0): return pow(int(a)%p,p-2,p)
def fm(fr,p=P0): return (fr.numerator%p)*inv(fr.denominator,p)%p

def eadd(*es):
    out={}
    for e in es:
        for m,c in e.items(): out[m]=out.get(m,F(0))+c
    return {m:c for m,c in out.items() if c!=0}
def emul(e1,e2):
    out={}
    for m1,c1 in e1.items():
        for m2,c2 in e2.items():
            m=tuple(sorted(m1+m2)); out[m]=out.get(m,F(0))+c1*c2
    return out
def esc(e,c): return {m:cc*c for m,cc in e.items()}
L=lambda s:{(s,):F(1)}

def Xexpr():
    h1=L('h1')
    return emul(h1, eadd(esc(h1,F(2)),esc(L('h2'),F(-1)),esc(L('h3'),F(-1))))
XE=Xexpr()

def LFX_over_S(n,k):
    rp=F((n+1)**2*S(n+1,k),S(n,k)); r0=F(lam0(n)); rm=F(n*n*S(n-1,k),S(n,k))
    xp=shift_expr(XE,n,k,+1,0); x0=XE; xm=shift_expr(XE,n,k,-1,0)
    j = eadd(esc(xp,rp),esc(x0,-r0),esc(xm,-rm))
    j = eadd(j, {(): F(S(n+1,k)+S(n-1,k), S(n,k))})
    return j

# null library at level N (letters at (N,k) re-expressed at base (n,k) via shifts)
def nulls_level(n,k,N):
    # letters for level N: lam etc use args (N,k): express via shift from (n,k): dn=N-n
    dn=N-n
    def sh(e): return shift_expr(e,n,k,dn,0)
    lam  = eadd(L('h4'),esc(L('h1'),F(-3)),esc(L('h2'),F(2)))
    lam2 = eadd(esc(L('s1'),F(3)),esc(L('s2'),F(2)),esc(L('s4'),F(-1)))
    Pex=eadd(L('h4'),esc(L('h1'),F(-1))); Ppr=eadd(L('s1'),esc(L('s4'),F(-1)))
    Qk=eadd(L('h1'),esc(L('h2'),F(-1))); Qkpr=eadd(esc(L('s1'),F(-1)),esc(L('s2'),F(-1)))
    lam,lam2,Pex,Ppr,Qk,Qkpr = sh(lam),sh(lam2),sh(Pex),sh(Ppr),sh(Qk),sh(Qkpr)
    C1={():F(1)}
    nus=[lam,
         eadd(esc(lam,F(k)),C1),
         eadd(esc(lam,F(k*k)),esc(C1,F(2*k))),
         eadd(esc(lam,F(k**3)),esc(C1,F(3*k*k))),
         eadd(Ppr,emul(Pex,lam)),
         eadd(esc(eadd(Ppr,emul(Pex,lam)),F(k)),Pex),
         eadd(esc(eadd(emul(lam,lam),lam2),F(1,2)),emul(lam,Qk),Qkpr),
        ]
    nus.append(eadd(esc(nus[6],F(k)),lam,Qk))
    # weight ratio S(N,k)/S(n,k)
    w = F(S(N,k),S(n,k)) if S(n,k) else F(0)
    return [esc(nu,w) for nu in nus]

ALL19=[()]+[(l,) for l in ['h1','h2','h3','h4','s1','s2','s3','s4']]+\
 [tuple(sorted((a,b))) for i,a in enumerate(['h1','h2','h3','h4']) for b in ['h1','h2','h3','h4'][i:]]

def solve(dn,dk,den,mudeg,pts,hold,tag,p=P0):
    polymons=[(i,j) for i in range(dn+1) for j in range(dk+1)]
    NP=len(polymons); NM=len(ALL19); NNU=8*3
    U0=NM*NP; Utot=U0+NNU*(mudeg+1)
    def rows_for(ptlist):
        rows=[];rhs=[]
        for (n,k) in ptlist:
            lf=LFX_over_S(n,k)
            r=fm(F(S(n,k+1),S(n,k)))
            d1=fm(den(n,k+1)); d0=fm(den(n,k))
            mv1=[pow(n,i,p)*pow(k+1,j,p)%p for (i,j) in polymons]
            mv0=[pow(n,i,p)*pow(k,j,p)%p for (i,j) in polymons]
            shexp={m:shift_expr({m:F(1)},n,k,0,1) for m in ALL19}
            nuall=[]
            for N in (n-1,n,n+1):
                nuall+=nulls_level(n,k,N)
            chans=set(lf.keys())
            for m in ALL19: chans|=set(shexp[m].keys()); chans.add(m)
            for nu in nuall: chans|=set(nu.keys())
            for C in sorted(chans,key=lambda m:(len(m),m)):
                row=np.zeros(Utot,dtype=np.int64)
                for mi,m in enumerate(ALL19):
                    cC=shexp[m].get(C,F(0))
                    a1=r*fm(cC)%p*d1%p if cC else 0
                    a0=d0 if C==m else 0
                    if a1 or a0:
                        b=mi*NP
                        for pj in range(NP):
                            v=(a1*mv1[pj]-a0*mv0[pj])%p
                            if v: row[b+pj]=v
                for j,nu in enumerate(nuall):
                    cC=nu.get(C,F(0))
                    if cC:
                        a=fm(cC)
                        for t in range(mudeg+1):
                            row[U0+j*(mudeg+1)+t]=a*pow(n,t,p)%p
                rows.append(row); rhs.append(fm(lf.get(C,F(0))))
        return np.array(rows,dtype=np.int64),np.array(rhs,dtype=np.int64)
    A,b=rows_for(pts)
    Ab=np.concatenate([A%p,(b%p).reshape(-1,1)],axis=1)
    nr,nc=A.shape; piv=[];r=0
    for c in range(nc):
        nz=np.nonzero(Ab[r:,c])[0]
        if len(nz)==0: continue
        i=r+nz[0]; Ab[[r,i]]=Ab[[i,r]]
        Ab[r]=Ab[r]*inv(Ab[r,c])%p
        mask=np.nonzero(Ab[:,c])[0]; mask=mask[mask!=r]
        if len(mask): Ab[mask]=(Ab[mask]-np.outer(Ab[mask,c],Ab[r]))%p
        piv.append(c); r+=1
        if r==nr: break
    bad=sum(1 for i in range(r,nr) if Ab[i,nc]%p)
    print(f"[{tag}] rows={nr} cols={nc} rank={r} bad={bad}",flush=True)
    return bad

if __name__=="__main__":
    random.seed(9)
    pts=set()
    while len(pts)<130:
        n=random.randint(6,26); k=random.randint(2,n-2); pts.add((n,k))
    pts=sorted(pts); hold=[]
    D3=lambda n,k: F(((n+1-k)*(n-k)*(n+k)*(k+1)*(n+k+1))**2)
    solve(7,10,D3,6,pts,hold,"L2-3level")
