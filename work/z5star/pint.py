"""(P-int) MEASURED: are the coefficients of E_w/Phi finite at k = n+1,n+2,n+3 ?

Each (E_w/Phi)_i is a rational function of (n,k,l) (the harmonic letters are
atoms), so it can be evaluated at RATIONAL k.  Evaluate at k = n+j + eps for
eps = 1/10, 1/100, 1/1000: a genuine pole of order r blows up like eps^-r, a
cancelled one converges.  Compared against a control weight that deliberately
VIOLATES (P-int) (the monomial h1_mk*h2_mk)."""
import sys, json, itertools
from fractions import Fraction as Fr
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
sys.path.insert(1,'/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import wtools as W, bare, zla
M=3
def Pm(n,k,l,i):
    v=Fr(1)
    for j in range(1,i+1): v*= (n+j)*(n+k+j)*(n+l+j)*(n+k+l+j)
    a=Fr(1); b=Fr(1)
    for j in range(i+1,M+1): a*=(n+j-k); b*=(n+j-l)
    return v*a*a*b*b
def incn(L,n,k,l,aa):
    r,a=bare.LETTERS[L]; cn,ck,cl=bare.ARGS[a]; d=bare.delta(L,M)
    if cn==0: return Fr(0)
    tot=Fr(0)
    if aa>d:
        for ii in range(d,aa): tot+=Fr(1,1)/ (cn*(n+ii)+ck*k+cl*l+1)**r
    elif aa<d:
        for ii in range(aa,d): tot-=Fr(1,1)/ (cn*(n+ii)+ck*k+cl*l+1)**r
    return tot
def divide(mi,mj):
    rest=list(mj)
    for L in mi:
        if L in rest: rest.remove(L)
        else: return None
    return tuple(sorted(rest))
def Ewphi(wQ,mi,n,k,l):
    cc=zla.cc(n); s=Fr(0)
    for mj,wj in wQ.items():
        rest=divide(mi,mj)
        if rest is None: continue
        for u in range(4):
            pr=Pm(n,k,l,u)
            for L in rest: pr*=incn(L,n,k,l,u)
            s+=wj*Fr(cc[u])*pr
    return s
d=json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
wQ={(() if nm=='1' else tuple(nm.split('*'))):Fr(c) for nm,c in zip(d['basis'],d['coeffs']) if Fr(c)!=0}
clo=sorted({tuple(sorted(s)) for m in wQ for r in range(len(m)+1) for s in itertools.combinations(m,r)})
ctrl={tuple(sorted(('h1_mk','h2_mk'))):Fr(1)}
cclo=sorted({tuple(sorted(s)) for m in ctrl for r in range(len(m)+1) for s in itertools.combinations(m,r)})
n=5; l=3
for name,(ww,cl_) in (('w*',(wQ,clo)),('CONTROL h1_mk*h2_mk',(ctrl,cclo))):
    worst=0; where=None
    for j in (1,2,3):
        prev=None
        for E in (Fr(1,10),Fr(1,100),Fr(1,1000)):
            k=n+j+E
            mx=0
            for mi in cl_:
                v=abs(Ewphi(ww,mi,n,k,l))
                mx=max(mx,v)
            if prev is not None:
                ratio=float(mx/prev) if prev else 0
                if ratio>worst: worst=ratio; where=(j,)
            prev=mx
    print('%-22s : max |(E_w/Phi)_i| growth factor per 10x closer approach to k=n+j : %.3g  %s'
          %(name,worst,'FINITE (no pole)' if worst<20 else '<<< POLE'))
