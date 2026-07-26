import sys, json
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import mindens, wtools as W, cert5, bnd
from math import comb
p=W.P1
dc=json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
w=W.to_p([Fr(c) for c in dc['coeffs']],p)
def Phi(n,k,l,p):
    N=n+3
    T=comb(N+k,N)*comb(N,k)**2*comb(N+l,N)*comb(N,l)**2*comb(N+k+l,N)
    d=1
    for j in (1,2,3): d*=(n+j)*(n+k+j)*(n+l+j)*(n+k+l+j)
    return T%p*pow(d%p,p-2,p)%p
for n in [5,9,11]:
    r=cert5.build(n,w,W.B,'M0',8,'M0',12,p=p,vnpts=0,verbose=False)
    ans0=r['ans0']; x0=r['x0']
    # Phi symmetry spot-check
    sym=all(Phi(n,a,b,p)==Phi(n,b,a,p) for a in range(0,n+5) for b in range(0,n+5))
    R=bnd.Rvals_from_x0(x0,ans0,n,p)
    x,rk,nbad,nj=bnd.solve_Nu(n,p,R)
    # fresh-point verification of the Delta identity at j never used in the fit
    used=sorted(R)[:49]; fresh=[j for j in sorted(R) if j not in used][:20]
    bad=0
    for j in fresh:
        u1=sum(int(x[u])*pow((j+1)%p,u,p) for u in range(bnd.NUNK))%p*pow(bnd.Dj(n,j+1,p),p-2,p)%p
        u0=sum(int(x[u])*pow(j%p,u,p) for u in range(bnd.NUNK))%p*pow(bnd.Dj(n,j,p),p-2,p)%p
        if (bnd.gj(n,j,p)*u1-u0-R[j])%p: bad+=1
    # u(n,0) = 0 ?
    u0z=int(x[0])%p
    # telescoped total
    tot=0
    for j in range(0,n+4): tot=(tot+Phi(n,0,j,p)*R[j])%p if j in R else tot
    print('n=%2d: Phi symmetric=%s ; Nu solve rank=%d/%d nbad=%d rows=%d ; fresh Delta-check %d/%d bad ; Nu(n,0)=%s ; sum Phi*R = %s'
          %(n,sym,rk,bnd.NUNK,nbad,nj,bad,len(fresh),u0z,tot),flush=True)
