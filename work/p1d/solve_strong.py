"""Is the STRONG depth system  d5 <= vT  (cap'(pat) = alpha+gamma+kappa) consistent
with the fitting system P_n = sum T w5 ?   Only the rank test is run."""
import sys, time
import numpy as np
from fractions import Fraction as F
from collections import defaultdict
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from fit import Q1, Q2, row, rref, lad_ext
from depthcond import basis, patterns, elem_expansion

MODE = sys.argv[1] if len(sys.argv)>1 else 'strong'
N = 600
B = basis()
caps0 = patterns()      # {(al,ga,ka,th): 1+min(vT,2)}
caps = {}
for pat in caps0:
    al,ga,ka,th = pat
    vT = al+ga+ka
    if MODE=='strong':   caps[pat] = vT                 # d5 <= vT
    elif MODE=='vt2':    caps[pat] = caps0[pat] if vT!=2 else 2   # only strengthen vT=2
    else:                caps[pat] = caps0[pat]
print('MODE',MODE,'caps',{k:caps[k] for k in sorted(caps)},flush=True)

def key(e):
    i,j,ci,ni = e
    mons = list(B.km[i][0])+list(B.km[j][0])+list(B.cm[ci][0])+list(B.nm[ni][0])
    return (len(mons), sum(1 for m in mons if m[0]=='B'), sum(1 for m in mons if m[0]=='C'),
            sum(1 for m in mons if m[0]=='N'), -max([int(m[1]) for m in mons],default=0), B.label(e))
B.els = sorted(B.els,key=key); NC=len(B.els)
rows = defaultdict(lambda:[F(0)]*NC)
for ci,e in enumerate(B.els):
    for pat,cap in caps.items():
        if pat==(0,0,0,1): continue
        for (u,sym),v in elem_expansion(B,e,pat).items():
            if u>cap: rows[(pat,u,sym)][ci]+=v
C=[]
for k,vec in rows.items():
    if not any(vec): continue
    den=1
    for v in vec: den = den*v.denominator//np.gcd(den,v.denominator)
    iv=[int(v*den) for v in vec]
    g=0
    for v in iv: g=np.gcd(g,abs(v))
    if g: iv=[v//int(g) for v in iv]
    C.append(iv)
C=np.array(C,dtype=object)
print('nonzero condition rows: %d x %d'%C.shape,flush=True)

for q in (Q1,Q2):
    Y = lad_ext('P',N+1,q)
    M=np.zeros((N,NC),dtype=np.int64); b=np.zeros(N,dtype=np.int64)
    for i,n in enumerate(range(1,N+1)):
        M[i]=row(n,q,B,depth2=False,maxr=5); b[i]=Y[n]
    Cq=np.array([[int(v)%q for v in r] for r in C],dtype=np.int64)
    rM,_,_,_ = rref(M,np.zeros(N,dtype=np.int64),q)
    rC,_,_,_ = rref(Cq,np.zeros(len(Cq),dtype=np.int64),q)
    A=np.concatenate([M,Cq],axis=0); rhs=np.concatenate([b,np.zeros(len(Cq),dtype=np.int64)])
    r,piv,inc,R = rref(A,rhs,q)
    rA,_,_,_ = rref(A,np.zeros(len(rhs),dtype=np.int64),q)
    print('q=%d rank(fit)=%d rank(cond)=%d rank(joint)=%d rank(aug)=%d INCONSISTENT=%s'
          %(q,rM,rC,rA,r,inc),flush=True)
