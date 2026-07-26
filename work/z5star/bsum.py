"""Consistency: with the 16 non-() (B-bot) classes imposed, is the residual
boundary obligation  Sum_l Phi(n,0,l) rho_() + Sum_k Phi(n,k,0) sigma_()  = 0 ?"""
import sys, json
from fractions import Fraction as Fr
from math import comb
import numpy as np
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import mindens, wtools as W, gosper, fastlin
p=W.P1
dc=json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
w=W.to_p([Fr(c) for c in dc['coeffs']],p)
def Phi(n,k,l,p):
    N=n+3
    T=comb(N+k,N)*comb(N,k)**2*comb(N+l,N)*comb(N,l)**2*comb(N+k+l,N)
    d=1
    for j in (1,2,3):
        d*=(n+j)*(n+k+j)*(n+l+j)*(n+k+l+j)
    return T%p*pow(d%p,p-2,p)%p
for n in [1,2,3,8,9,10,11,12,13]:
    S=gosper.build_joint(n,w,W.B,'M0',8,'M0',12,p)
    A1,b1=gosper.class_rows(S,exclude_empty=True)
    L2=np.concatenate([S['LHS'],A1],axis=0); r2=np.concatenate([S['rhs0'],b1])
    z,rk,piv,nbad=fastlin.solve(L2,r2,p)
    if nbad: print('n=%d : 16-class system INCONSISTENT'%n); continue
    ans0=S['ans0']; x0=z[:ans0.nc]
    tot=0
    for l in range(0,n+4):
        tot=(tot+Phi(n,0,l,p)*ans0.eval_r(x0,n,0,l,p))%p
    for k in range(0,n+4):
        tot=(tot+Phi(n,k,0,p)*ans0.eval_s(x0,n,k,0,p))%p
    print('n=%2d : 16 classes consistent ; residual boundary sum = %s  %s'
          %(n,tot,'ZERO -- the boundary obligation IS satisfied' if tot==0 else 'NONZERO'),flush=True)
