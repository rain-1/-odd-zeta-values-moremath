"""(BASE) sweep:  ord_p(P_n) >= 0 for every prime 5 <= p <= 367 and every n < min(p,361)."""
import sys
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import P, vp
def primes(N):
    s=[True]*(N+1); s[0]=s[1]=False
    for i in range(2,int(N**.5)+1):
        if s[i]:
            for j in range(i*i,N+1,i): s[j]=False
    return [i for i in range(N+1) if s[i]]
bad=0; tot=0; worst=(99,None)
for p in primes(367):
    if p<5: continue
    for n in range(1,min(p,361)):
        tot+=1
        v=vp(P(n),p)
        if v<worst[0]: worst=(v,(p,n))
        if v<0: bad+=1; print('BASE FAIL p=%d n=%d v=%d'%(p,n,v))
print('(BASE) primes 5..367, n<min(p,361): cells=%d failures=%d min v_p(P_n)=%d at %s'%(tot,bad,worst[0],worst[1]))
