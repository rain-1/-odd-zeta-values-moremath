"""(F-gen-weak):  v_p( Tcal(b,c) - Q_r * T(a,b,c) ) >= 1 + min(alpha_a+gamma_a+kappa_a, 2)
   for MULTI-DIGIT a.  alpha_a = [a+b >= p^{L(a)+1}], etc."""
import sys
from math import comb
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import Q

def Tl(n,k,l):
    if k>n or l>n or k<0 or l<0: return 0
    return comb(n+k,n)*comb(n,k)**2*comb(n+l,n)*comb(n,l)**2*comb(n+k+l,n)
def vpm(x,p,cap):
    if x==0: return cap
    v=0
    while x%p==0 and v<cap: x//=p; v+=1
    return v

JOBS=[(5,1,30),(7,1,22),(11,1,15),(13,1,13)]
for p,a0,a1 in JOBS:
    CAP=8; MOD=p**CAP
    bad=0; cells=0; worst=(99,None); minslack=99
    for a in range(a0,a1+1):
        La=0; qq=a
        while qq>=p: qq//=p; La+=1
        PM=p**(La+1)
        for r in range(p):
            n=a*p+r; Qr=int(Q(r))
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
                    Ta=Tl(a,b,c)
                    al=1 if a+b>=PM else 0; ga=1 if a+c>=PM else 0
                    eps=(b+c)//PM; ka=1 if a+b+c>=(eps+1)*PM else 0
                    need=1+min(al+ga+ka,2)
                    v=vpm((s_-Qr*Ta)%MOD,p,CAP)
                    cells+=1
                    if v-need<minslack: minslack=v-need; worst=(a,r,b,c,al+ga+ka,v,need)
                    if v<need: bad+=1
    print('p=%2d a=%d..%d cells=%d  (F-gen-weak) failures=%d  min slack=%d at (a,r,b,c,s_a,v,need)=%s'
          %(p,a0,a1,cells,bad,minslack,worst),flush=True)
