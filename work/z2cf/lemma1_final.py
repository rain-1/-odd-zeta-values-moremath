"""LEMMA 1, complete: L(Sum_k S w_cl) = 0 for n>=2.
Chain: (M) miracle shifts -> (SPLIT) -> (CERT) LS=Delta G_D (shell form, all k)
-> Abel -> (LAM) one alternating binomial sum identity -> beta-atoms."""
from fractions import Fraction as F
from math import comb, factorial as fact
import sympy as sp

def S(n,k):
    if k<0 or k>n: return 0
    return comb(n,k)**2*comb(n+k,k)
def lam0(n): return 11*n*n+11*n+3
def e(n): return sum(F((-1)**(m-1),m*m) for m in range(1,n+1))
def g(n,m): return F(1, m*m*comb(n,m)*comb(n+m,m))
def tau(n,k): return sum(F((-1)**(n+m-1))*g(n,m) for m in range(1,min(k,n)+1))
def wcl(n,k): return 2*e(n)+tau(n,k)
def rho_D(n,k): return k*k+k*(1+6*n)-4-15*n-11*n*n
def GDs(n,k):   # shell form, defined for 0<=k<=n+1 (and 0 beyond via C(n+1,k))
    if k<0: return F(0)
    return F(k**3*rho_D(n,k)*comb(n+1,k)**2*comb(n+k-1,k), n*(n+1)**2)
def U(n,k):
    if k<0 or k>n: return F(0)
    return F((-1)**(n+k)*comb(n,k))
def LS(n,k):
    return F((n+1)**2)*S(n+1,k)-lam0(n)*S(n,k)-F(n*n)*S(n-1,k)
def LFcl(n,k):
    return F((n+1)**2)*S(n+1,k)*wcl(n+1,k) - lam0(n)*S(n,k)*wcl(n,k) \
           - F(n*n)*S(n-1,k)*wcl(n-1,k)

# (CERT) LS = Delta GDs pointwise for ALL 0<=k<=n+2
bad=[(n,k) for n in range(2,15) for k in range(0,n+3) if LS(n,k)!=GDs(n,k+1)-GDs(n,k)]
print("CERT LS=DeltaG_D cellwise fails (all k):", len(bad), bad[:4])
# symbolic: single rational identity (interior polynomial identity)
n_,k_=sp.symbols('n k', positive=True)
rhoS=k_**2+k_*(1+6*n_)-4-15*n_-11*n_**2
lamS=11*n_**2+11*n_+3
lhs_poly = ((n_+1)**2*(n_+k_)*(n_+k_+1)/(n_*(n_+1)) - lamS*(n_+1-k_)**2*(n_+k_)/((n_+1)**2*n_)
            - (n_+1-k_)**2*(n_-k_)**2/((n_+1)**2))
rhs_poly = ((n_+1-k_)**2*(n_+k_)*rhoS.subs(k_,k_+1) - k_**3*rhoS)/(n_*(n_+1)**2)
print("CERT symbolic (rational identity):", sp.cancel(lhs_poly-rhs_poly)==0)

# (LAM): Sum_{k=0}^{n}(-1)^k C(n,k) W(n,k) = sigma*(2(n+1)^2 - Bd(n)),
#   W = 2(n+1)^2/(n+1-k)^2 - 2(n-k)/(n+k) + k*rho_D(n,k)/((n+1-k)^2*(n+k))
def W(n,k):
    return F(2*(n+1)**2,(n+1-k)**2)-F(2*(n-k),n+k)+F(k*rho_D(n,k),(n+1-k)**2*(n+k))
def Bd(n):   # boundary cells k=n and k=n+1 of LF_cl - LS*wcl
    out=F(0)
    for k in (n,n+1):
        out += LFcl(n,k)-LS(n,k)*wcl(n,k)
    return out
lamfail=[]
for n in range(2,26):
    sg=F((-1)**n)
    lhs=sum(F((-1)**k*comb(n,k))*W(n,k) for k in range(n+1))
    if sg*lhs != -(Bd(n) - 2*(n+1)**2)*F(1)*sp.Integer(1) if False else None: pass
    # direct assembly check: Lv=0 decomposition
    Lv = sum(LFcl(n,k) for k in range(n+2))
    abel = -sum(GDs(n,k+1)*(tau(n,k+1)-tau(n,k)) for k in range(n+1))
    usum = sum(U(n,k)*W(n,k) for k in range(n)) \
           - sum(U(n,j)*F(j*rho_D(n,j),(n+1-j)**2*(n+j)) for j in range(n)) # subtract to re-split
    # simpler: verify Lv == abel + sum_{k<n} U*RHSU + Bd  (RHSU part of W)
    rhsu_sum = sum(U(n,k)*(F(2*(n+1)**2,(n+1-k)**2)-F(2*(n-k),n+k)) for k in range(n))
    if Lv != abel + rhsu_sum + Bd(n): lamfail.append(('assembly',n))
    if Lv != 0: lamfail.append(('Lv',n))
    # abel-to-U conversion: -Sum GDs(k+1)*Dtau(k) == Sum_{j=1..n} U(n,j)*j*rho_D(n,j)/((n+1-j)^2 (n+j))
    conv = sum(U(n,j)*F(j*rho_D(n,j),(n+1-j)**2*(n+j)) for j in range(1,n+1))
    if abel != conv: lamfail.append(('conv',n))
print("assembly/Lv/conversion fails n=2..25:", lamfail[:6], "count",len(lamfail))

# hence (LAM): Sum_{k=0}^{n-1} U*RHSU + Sum_{j=1}^n U*RDpart + Bd(n) = 0. Verify:
lam2=[]
for n in range(2,31):
    tot = sum(U(n,k)*(F(2*(n+1)**2,(n+1-k)**2)-F(2*(n-k),n+k)) for k in range(n)) \
        + sum(U(n,j)*F(j*rho_D(n,j),(n+1-j)**2*(n+j)) for j in range(1,n+1)) + Bd(n)
    if tot!=0: lam2.append(n)
print("(LAM) exact n=2..30 fails:", lam2)

# Bd closed form: derive from miracle. Verify candidate:
#   Bd(n) = 2(n+1)^2 + (n+1)^2*C(2n+2,n+1)*[2sig/(n+1)^2 + tau(n+1,n+1)-tau(n,n)]... 
# just record numeric Bd and its sigma-normalized rational form:
for n in range(2,9):
    sg=F((-1)**n)
    b1 = LFcl(n,n)-LS(n,n)*wcl(n,n)
    b2 = LFcl(n,n+1)-LS(n,n+1)*wcl(n,n+1)
    # predicted: b1 = 2(n+1)^2 ; b2 = (n+1)^2 C(2n+2,n+1) [wcl(n+1,n+1)-wcl(n,n+1)]
    pred2 = F((n+1)**2*comb(2*n+2,n+1))*(wcl(n+1,n+1)-wcl(n,n+1))
    print(n, "b1==2(n+1)^2:", b1==2*(n+1)**2, " b2 pred:", b2==pred2,
          " b2*sg=", sg*b2)
