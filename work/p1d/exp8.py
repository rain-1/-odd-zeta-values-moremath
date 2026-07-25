"""Lemma B for GENERAL a:  T(n,k,l) = T(a,b,c) T(r,s,t) Pi Ghat  with Ghat in 1+pZ_p,
   in-regime s<=r, t<=r.   Test Ghat := T(n,k,l)/(T(a,b,c)T(r,s,t)Pi)  has v_p(Ghat-1)>=1."""
import sys
from fractions import Fraction as F
from math import comb
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import vp
def Tl(n,k,l):
    if k>n or l>n or k<0 or l<0: return 0
    return comb(n+k,n)*comb(n,k)**2*comb(n+l,n)*comb(n,l)**2*comb(n+k+l,n)
bad=0; tested=0; badpi=0
for p in (5,7,11):
    for a in range(1,3*p+2):
        for r in range(p):
            n=a*p+r
            for b in range(a+1):
                for c in range(a+1):
                    for s in range(r+1):
                        for t in range(r+1):
                            k=b*p+s; l=c*p+t
                            if k>n or l>n: continue
                            Ta=Tl(a,b,c); Tr=Tl(r,s,t)
                            if Ta==0 or Tr==0: continue
                            e1=1 if r+s>=p else 0; e2=1 if r+t>=p else 0
                            e3=(r+s+t)//p; e4=1 if s+t>=p else 0
                            Pi=F(comb(a+b+e1,e1)*comb(a+c+e2,e2)*comb(a+b+c+e3,e3), comb(b+c+e4,e4))
                            G=F(Tl(n,k,l))/(Ta*Tr*Pi)
                            tested+=1
                            if vp(G-1,p)<1:
                                bad+=1
                                if bad<4: print('  Ghat FAIL p=%d a=%d r=%d b=%d c=%d s=%d t=%d G=%s'%(p,a,r,b,c,s,t,G))
print('Lemma B (general a) test: %d in-regime cells, Ghat-1 not in pZ_p: %d'%(tested,bad))
