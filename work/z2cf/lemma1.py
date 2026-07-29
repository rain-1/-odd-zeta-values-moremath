"""LEMMA 1: L(Sum_k S w_cl) = 0 via Psi = G_D*(2e+tau) + U*u.  See ledger."""
from fractions import Fraction as F
from math import comb, factorial as fact
import json, random

def S(n,k):
    if k<0 or k>n: return 0
    return comb(n,k)**2*comb(n+k,k)
def lam0(n): return 11*n*n+11*n+3
def e(n): return sum(F((-1)**(m-1),m*m) for m in range(1,n+1))
def g(n,m): return F(1, m*m*comb(n,m)*comb(n+m,m))
def tau(n,k): return sum(F((-1)**(n+m-1))*g(n,m) for m in range(1,min(k,n)+1))
def wcl(n,k): return 2*e(n)+tau(n,k)
def gam(n,k): return F((-1)**k*fact(k)**2*fact(n-k), fact(n+k+1))
def rho_D(n,k): return k*k+k*(1+6*n)-4-15*n-11*n*n
def GD(n,k):
    if k<0 or k>n: return F(0)
    return S(n,k)*F(k**3*rho_D(n,k), (n+1-k)**2*(n+k))
def U(n,k):
    if k<0 or k>n: return F(0)
    return F((-1)**(n+k)*comb(n,k))
def LFcl(n,k):
    return F((n+1)**2)*S(n+1,k)*wcl(n+1,k) - lam0(n)*S(n,k)*wcl(n,k) \
           - F(n*n)*S(n-1,k)*wcl(n-1,k)
def LS(n,k):
    return F((n+1)**2)*S(n+1,k)-lam0(n)*S(n,k)-F(n*n)*S(n-1,k)

B=[F(0),F(1)]
for n in range(1,32): B.append((lam0(n)*B[n]+n*n*B[n-1])/F((n+1)**2))
print("w_cl gives 5B (n<=25):",
      all(sum(S(n,k)*wcl(n,k) for k in range(n+1))==5*B[n] for n in range(26)))

bad=0
for n in range(1,16):
    sg=F((-1)**n)
    for k in range(0,n+1):
        if tau(n+1,k)-tau(n,k) != sg*F(2,n+1)*(gam(n,k)-F(1,n+1)): bad+=1
    for k in range(0,n):
        if tau(n-1,k)-tau(n,k) != sg*F(2,n)*(gam(n-1,k)-F(1,n)): bad+=1
print("miracle shifts cellwise fails:", bad)

# split: LF_cl == LS*(2e+tau) + U*RHS_U  on 0<=k<=n-1
def RHSU(n,k): return F(2*(n+1)**2,(n+1-k)**2)-F(2*(n-k),n+k)
bad=0
for n in range(2,14):
    for k in range(0,n):
        if LFcl(n,k) != LS(n,k)*wcl(n,k)+U(n,k)*RHSU(n,k): bad+=1
print("split identity fails (0<=k<=n-1):", bad)

# certificate equation (E2'): -(n-k)u(k+1)/(k+1) - u(k) = T(n,k) :=
#   RHS_U + rho_D(n,k+1)/((n-k)(n+k+1))
def T(n,k): return RHSU(n,k)+F(rho_D(n,k+1),(n-k)*(n+k+1))

def solve(rows,nc):
    M=[list(r)+[b] for r,b in rows]; piv=[];r=0
    for c in range(nc):
        p=None
        for i in range(r,len(M)):
            if M[i][c]!=0: p=i;break
        if p is None: continue
        M[r],M[p]=M[p],M[r]; iv=F(1)/M[r][c]; M[r]=[x*iv for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[a-f*b for a,b in zip(M[i],M[r])]
        piv.append(c); r+=1
    for i in range(r,len(M)):
        if M[i][nc]!=0: return None
    x=[F(0)]*nc
    for i,c in enumerate(piv): x[c]=M[i][nc]
    return x

random.seed(3)
pts=set()
while len(pts)<70:
    n=random.randint(4,24); k=random.randint(0,n-1); pts.add((n,k))
pts=sorted(pts)
found=None
for dn,dk,den,tag in [
    (2,3, lambda n,k:F((n+1-k)*(n+k+1)), "K1"),
    (3,4, lambda n,k:F((n+1-k)*(n+k)*(n+k+1)), "K2"),
    (4,6, lambda n,k:F(((n+1-k)*(n+k+1))**2), "K3"),
    (5,7, lambda n,k:F(((n+1-k)*(n+k)*(n+k+1))**2), "K4"),
]:
    mons=[(i,j) for i in range(dn+1) for j in range(dk+1)]
    rows=[]
    for (n,k) in pts:
        d1=den(n,k+1); d0=den(n,k)
        co=[F(-(n-k),k+1)*F(n**i*(k+1)**j,1)/d1 - F(n**i*k**j,1)/d0 for i,j in mons]
        rows.append((co,T(n,k)))
    x=solve(rows,len(mons))
    print(f"[{tag}] solved:", x is not None)
    if x is not None:
        uco={m:c for m,c in zip(mons,x) if c}
        def uval(n,k,uc=uco,dd=den): return sum(c*F(n)**i*F(k)**j for (i,j),c in uc.items())/dd(n,k)
        bad=0;tot=0
        for n in range(25,31):
            for k in range(0,n):
                tot+=1
                if F(-(n-k),k+1)*uval(n,k+1)-uval(n,k)!=T(n,k): bad+=1
        print(f"  holdout bad {bad}/{tot}, monoms {len(uco)}")
        if bad==0:
            found=(tag,dn,dk,uco,den); break
if found:
    tag,dn,dk,uco,den=found
    json.dump({"tag":tag,"u":[[m[0],m[1],str(c)] for m,c in uco.items()]},
              open("work/z2cf/cert_lemma1.json","w"))
    def uval(n,k): return sum(c*F(n)**i*F(k)**j for (i,j),c in uco.items())/den(n,k)
    # FULL cell certificate check incl. ALL boundary cells k=0..n+2, n=2..16:
    #   LF_cl(n,k) =? Psi(n,k+1)-Psi(n,k),  Psi = GD*(2e+tau)+U*u
    def Psi(n,k):
        base=GD(n,k)*wcl(n,k) if 0<=k<=n else F(0)
        ub = U(n,k)*uval(n,k) if 0<=k<=n else F(0)
        return base+ub
    bad=[]
    for n in range(2,17):
        for k in range(0,n+3):
            if LFcl(n,k)!=Psi(n,k+1)-Psi(n,k): bad.append((n,k))
    print("full-cell certificate fails:", len(bad), bad[:8])
    # boundary values
    print("u(n,0)==0 for n=2..12:", all(uval(n,0)==0 for n in range(2,13)))
    # assembly: L v = 0
    def v(n): return sum(S(n,k)*wcl(n,k) for k in range(n+1))
    print("L v == 0 n=2..25:",
          all(F((n+1)**2)*v(n+1)-lam0(n)*v(n)-F(n*n)*v(n-1)==0 for n in range(2,26)))
