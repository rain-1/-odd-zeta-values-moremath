"""Does Lemma F generalise to MULTI-DIGIT a ?
   test:  v_p( Tcal(b,c) - Tcal(0,0)*T(a,b,c) )  >=  2 + min(vT,2)   (Lemma F, verbatim)
   and    >= 1 + min(vT,2)                                            (the weak form we need)
"""
import sys
from math import comb
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')

def Tl(n,k,l):
    if k>n or l>n or k<0 or l<0: return 0
    return comb(n+k,n)*comb(n,k)**2*comb(n+l,n)*comb(n,l)**2*comb(n+k+l,n)

def vpmod(x,p,cap):
    if x==0: return cap
    v=0
    while x%p==0 and v<cap: x//=p; v+=1
    return v

JOBS=[(5,1,24),(7,1,20),(11,1,14),(13,1,12)]
for p,a0,a1 in JOBS:
    CAP=10; MOD=p**CAP
    bad2=0; bad1=0; worst=(99,None); cells=0
    for a in range(a0,a1+1):
        for r in range(p):
            n=a*p+r
            Tc={}
            for b in range(a+1):
                for c in range(a+1):
                    s_=0
                    for s in range(p):
                        k=b*p+s
                        if k>n: continue
                        for t in range(p):
                            l=c*p+t
                            if l>n: continue
                            s_+=Tl(n,k,l)
                    Tc[(b,c)]=s_%MOD
            mu=Tc[(0,0)]
            for b in range(a+1):
                for c in range(a+1):
                    Ta=Tl(a,b,c)
                    vT=vpmod(Ta,p,CAP)
                    diff=(Tc[(b,c)]-mu*Ta)%MOD
                    v=vpmod(diff,p,CAP)
                    cells+=1
                    need2=2+min(vT,2); need1=1+min(vT,2)
                    if v<need2: bad2+=1
                    if v<need1:
                        bad1+=1
                        if v-need1<worst[0]: worst=(v-need1,(a,r,b,c,vT,v))
    print('p=%2d a=%d..%d cells=%d  FAIL LemmaF(2+min)=%d   FAIL weak(1+min)=%d  worst=%s'
          %(p,a0,a1,cells,bad2,bad1,worst),flush=True)
