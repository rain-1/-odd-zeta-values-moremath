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
for n in [3,5,7,9,11,13]:
    r=cert5.build(n,w,W.B,'M0',8,'M0',12,p=p,vnpts=0,verbose=False)
    ans0=r['ans0']; x0=r['x0']
    Rfull={j:(ans0.eval_r(x0,n,0,j,p)+ans0.eval_s(x0,n,j,0,p))%p for j in range(0,n+5)}
    tot=sum(Phi(n,0,j,p)*Rfull[j] for j in range(0,n+4))%p
    R=bnd.Rvals_from_x0(x0,ans0,n,p)
    x,rk,nbad,nj=bnd.solve_Nu(n,p,R)
    def uval(j):
        num=sum(int(x[u])*pow(j%p,u,p) for u in range(bnd.NUNK))%p
        return num*pow(bnd.Dj(n,j,p),p-2,p)%p
    # CELLWISE check of Delta_j G = Phi*R on the REAL range j = 0..n+3
    cell=0
    for j in range(0,n+4):
        lhs=(Phi(n,0,j+1,p)*uval(j+1)-Phi(n,0,j,p)*uval(j))%p
        if (lhs-Phi(n,0,j,p)*Rfull[j])%p: cell+=1
    print('n=%2d: sum Phi*R over j=0..n+3 = %s ; Nu unique rank %d/13 ; u(n,0)=%s ; Phi(n,0,n+4)=%s ; cellwise Delta_j G = Phi*R : %d/%d bad'
          %(n,tot,rk,uval(0),Phi(n,0,n+4,p),cell,n+4),flush=True)
