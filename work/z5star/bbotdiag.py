"""Which (B-bot) collapse class is infeasible?  One augmented solve per class."""
import sys, os, json
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import mindens, wtools as W, cert4, cert2, cert3
import bare, frw, cert, family, joint, fastlin, ratrec, qrow
from solve import dval
p=W.P1; n=int(sys.argv[1]); m=3
dc=json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
w=W.to_p([Fr(c) for c in dc['coeffs']],p)
B=W.B
# rebuild the joint system exactly as cert4.build does, then test class by class
import types
orig=cert4.bbot_rows
store={}
def patched(n,w,B,act,maximal,zero_j,ansL,ans0,XP,H,p,nbpts):
    store.update(dict(act=act,maximal=maximal,zero_j=zero_j,ansL=ansL,ans0=ans0,XP=XP,H=H))
    return orig(n,w,B,act,maximal,zero_j,ansL,ans0,XP,H,p,nbpts)
cert4.bbot_rows=patched
r=cert4.build(n,w,B,'M0',8,sys.argv[2],int(sys.argv[3]),p=p,vnpts=0,verbose=True,bbot=True)
# now per class
act=store['act']; ansL=store['ansL']; ans0=store['ans0']; XP=store['XP']; H=store['H']
maximal=store['maximal']; zero_j=store['zero_j']
nrL=len(ansL.mons_r); nr0=len(ans0.mons_r); nk=H.shape[0]
avec=[1]
ncols=ans0.nc+len(act)*nk
npts0=int(1.35*ncols)+40
pd0=frw.PD(p,n,m,npts0,B,avec,seed=555)
Msc0=frw.scal_mat(pd0,ans0)
R1L,R0L,S1L,S0L=cert.evalmats(pd0,ansL)
Hr=np.ascontiguousarray(H[:,:nrL].T); Hs=np.ascontiguousarray(H[:,nrL:].T)
KR=joint.matmul(R1L,Hr,p); KS=joint.matmul(S1L,Hs,p)
G=np.zeros((npts0,len(act)*nk),dtype=np.int64)
rv=np.zeros((len(B),npts0),dtype=np.int64); sv=np.zeros((len(B),npts0),dtype=np.int64)
for j in maximal:
    rv[j]=int(w[j])*pd0.RQ1%p; sv[j]=int(w[j])*pd0.SQ1%p
for c,j in enumerate(act):
    sk,sl=cert.shiftpair(pd0,B[j])
    G[:,c*nk:(c+1)*nk]=((pd0.gk*sk%p)[:,None]*KR+(pd0.gl*sl%p)[:,None]*KS)%p
    rv[j]=cert.mv(R1L,XP[:nrL,c],p); sv[j]=cert.mv(S1L,XP[nrL:,c],p)
rhs0=cert.Ewphi(pd0,w,(),B)
for jj in range(len(B)):
    if jj==zero_j: continue
    sk,sl=cert.shiftpair(pd0,B[jj])
    rhs0=(rhs0-pd0.gk*sk%p*rv[jj]-pd0.gl*sl%p*sv[jj])%p
LHS=np.concatenate([Msc0,G],axis=1)
Ab,bb=orig(n,w,B,act,maximal,zero_j,ansL,ans0,XP,H,p,None)
# regroup rows by class: re-derive the row blocks
nb=Ab.shape[0]
print('total Bbot rows',nb)
# brute: test each contiguous chunk of `npts` rows (one class, one direction)
from cert4 import classes
idx=0; report=[]
for which in ('k','l'):
    cls=classes(B,which)
    dlmax=max(b for a,b in ans0.mons_r+ansL.mons_r)+2
    nbpts=dlmax+6
    for key,js in cls.items():
        js2=[j for j in js if j in act or j==zero_j or j in maximal]
        if not js2 or all(j in maximal for j in js2): continue
        blk=Ab[idx:idx+nbpts]; bblk=bb[idx:idx+nbpts]; idx+=nbpts
        L2=np.concatenate([LHS,blk],axis=0); r2=np.concatenate([rhs0,bblk])
        z,rk,piv,nbad=fastlin.solve(L2,r2,p)
        if nbad: report.append((which,key,[str(B[j]) for j in js2],nbad))
print('rows consumed',idx)
print('INFEASIBLE classes:')
for x in report: print('   ',x)
if not report: print('    none -- every class is individually feasible')
