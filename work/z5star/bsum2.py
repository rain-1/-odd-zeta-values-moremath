"""In the (B-bot)-satisfying gauge (cert5), the 16 classes vanish identically;
the residual boundary obligation is the () class alone.  Check it is zero."""
import sys, json
from fractions import Fraction as Fr
from math import comb
import numpy as np
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import mindens, wtools as W, cert5
p=W.P1
dc=json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
w=W.to_p([Fr(c) for c in dc['coeffs']],p)
def Phi(n,k,l,p):
    N=n+3
    T=comb(N+k,N)*comb(N,k)**2*comb(N+l,N)*comb(N,l)**2*comb(N+k+l,N)
    d=1
    for j in (1,2,3): d*=(n+j)*(n+k+j)*(n+l+j)*(n+k+l+j)
    return T%p*pow(d%p,p-2,p)%p
for n in [1,2,3,5,7,9,11,13]:
    r=cert5.build(n,w,W.B,'M0',8,'M0',12,p=p,vnpts=0,verbose=False)
    if r['nbad0'] or r['nbadL']:
        print('n=%d : system inconsistent'%n); continue
    bad=cert5.bbot_verify(n,w,W.B,r,p,npt=25,verbose=False)
    ans0=r['ans0']; x0=r['x0']; tot=0
    for l in range(0,n+4): tot=(tot+Phi(n,0,l,p)*ans0.eval_r(x0,n,0,l,p))%p
    for k in range(0,n+4): tot=(tot+Phi(n,k,0,p)*ans0.eval_s(x0,n,k,0,p))%p
    print('n=%2d : 16 classes violations=%d ; residual () boundary sum = %s  %s'
          %(n,len(bad),tot,'ZERO' if tot==0 else '*** NONZERO ***'),flush=True)
