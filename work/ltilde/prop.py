"""Exact rational propagation of the weight-7 ladder through the certified operator L.
L = sum_{k=0}^{4} c_k(n) S^k ,  c_k deg-19 integer polys.
Forward:  X_{n+4} = -(sum_{k<4} c_k(n) X_{n+k}) / c_4(n)
Index-3 unlock at n=-1 (c_0(-1)=0):  X_3 = -(c1(-1)X0 + c2(-1)X1 + c3(-1)X2)/c4(-1)
"""
import json, sys
from fractions import Fraction as F

W='/home/ubuntu/fable-episode-2/zeta-math/worthiness/'
R=json.load(open(W+'zeta7_q_recurrence.json'))
C=R['Cpoly']                      # C[k][j] = coeff of n^j in c_k(n)
def c(k,n):
    s=0
    for j in range(len(C[k])-1,-1,-1):
        s=s*n+C[k][j]
    return s

# ---- exact q_n ground truth ----
qs={}
for line in open(W+'zeta7_lc_terms.txt'):
    line=line.strip()
    if line.startswith('q_'):
        a,b=line.split('=')
        qs[int(a.strip()[2:])]=int(b.strip())
NQ=max(qs)+1
print(f"exact q_n loaded: {NQ} terms (n=0..{NQ-1}), q_73 has {len(str(qs[73]))} digits")

# ---- re-certify L on the exact q_n ----
bad=0
for n in range(0,NQ-4):
    if sum(c(k,n)*qs[n+k] for k in range(5))!=0: bad+=1
print(f"CERTIFY: annihilation relations n=0..{NQ-5}: {NQ-4} tested, {bad} nonzero")
print("c_k(-1) =",[c(k,-1) for k in range(5)])

def unlock3(X0,X1,X2):
    assert c(0,-1)==0
    return F(-(c(1,-1)*X0 + c(2,-1)*X1 + c(3,-1)*X2), c(4,-1))

def propagate(X0,X1,X2,X3,N):
    X=[F(X0),F(X1),F(X2),F(X3)]
    for n in range(0,N-4+1):
        if c(4,n)==0: raise RuntimeError(f"c4 vanishes at n={n}")
        X.append(F(-sum(c(k,n)*X[n+k] for k in range(4)), c(4,n)))
    return X

# anchors (BZ printed)
anch = {
 'q' : (F(1),F(61),F(52921)),
 's' : (F(0),F(300),F(261153)),
 'P' : (F(0),F(220),F(6021219,32)),
 'Ph': (F(0),F(152),F(535857,4)),
}
print()
for nm,(a0,a1,a2) in anch.items():
    x3=unlock3(a0,a1,a2)
    print(f"  {nm}_3 (n=-1 unlock) = {x3}")

# ================= DENOMINATOR AUDIT =================
from math import gcd
def dlcm(n):
    L=1
    for i in range(1,n+1): L=L*i//gcd(L,i)
    return L
def factor(m):
    f={}; d=2
    while d*d<=m:
        while m%d==0: f[d]=f.get(d,0)+1; m//=d
        d+=1 if d==2 else 2
    if m>1: f[m]=f.get(m,0)+1
    return f

N=int(sys.argv[1]) if len(sys.argv)>1 else 60
lad={}
for nm,(a0,a1,a2) in anch.items():
    lad[nm]=propagate(a0,a1,a2,unlock3(a0,a1,a2),N)
print(f"\npropagated to n={N}")
# q cross-check against exact
bad=sum(1 for n in range(min(N+1,NQ)) if lad['q'][n]!=qs[n])
print(f"q-propagation vs {min(N+1,NQ)} exact terms: {bad} mismatches")

KAP={'s':5,'Ph':5,'P':7}
print("\n n | den(s_n) primes>3? | ord3 s | den(Ph) vs d^5 | den(P) vs d^7")
for n in list(range(3,12))+list(range(15,N+1,5)):
    d=dlcm(n); row=[f"{n:3d}"]
    for nm in ('s','Ph','P'):
        den=lad[nm][n].denominator
        k=KAP[nm]; dk=d**k
        big=[p for p in factor(den) if p>3]
        ok = (dk % den == 0)
        row.append(f"{nm}:{'OK' if ok else 'FAIL'}{'' if not big else ' big='+str(big[:2])+('..' if len(big)>2 else '')}")
    print("  ".join(row))
