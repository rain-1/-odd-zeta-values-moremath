"""Targeted: impose ONE collapse class at a time on the joint system."""
import sys, os, json
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import mindens, wtools as W, cert4, cert2, cert3
import bare, frw, cert, family, joint, fastlin, ratrec, qrow
from solve import dval
p=W.P1; n=int(sys.argv[1]); m=3; B=W.B
d0=sys.argv[2]; s0=int(sys.argv[3]); sL=int(sys.argv[4]) if len(sys.argv)>4 else 8
maximal,letters,zero_j=cert2.blocks_of(B)
dc=json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
w=W.to_p([Fr(c) for c in dc['coeffs']],p)
act=[j for j in letters if any(cert.divide(B[j],B[jj]) is not None and w[jj] for jj in range(len(B)))]
ansL=cert3.mk('M0',sL,0,0); ans0=cert3.mk(d0,s0,0,0)
nrL=len(ansL.mons_r); nr0=len(ans0.mons_r)
avec=[1]
nptsL=int(1.4*ansL.nc)+60
pdL=frw.PD(p,n,m,nptsL,B,avec,seed=1234); MscL=frw.scal_mat(pdL,ansL)
H=np.array(ratrec.nullspace(MscL,p),dtype=np.int64); nk=H.shape[0]
rvL=np.zeros((len(B),nptsL),dtype=np.int64); svL=np.zeros((len(B),nptsL),dtype=np.int64)
for j in maximal: rvL[j]=int(w[j])*pdL.RQ1%p; svL[j]=int(w[j])*pdL.SQ1%p
RHS=np.zeros((nptsL,len(act)),dtype=np.int64)
for c,j in enumerate(act): RHS[:,c]=family.block_rhs(pdL,w,B,maximal,B[j],rvL,svL)
XP,rkL,piv,_=fastlin.solve(MscL,RHS,p)
ncols=ans0.nc+len(act)*nk; npts0=int(1.35*ncols)+40
pd0=frw.PD(p,n,m,npts0,B,avec,seed=555); Msc0=frw.scal_mat(pd0,ans0)
R1L,R0L,S1L,S0L=cert.evalmats(pd0,ansL)
Hr=np.ascontiguousarray(H[:,:nrL].T); Hs=np.ascontiguousarray(H[:,nrL:].T)
KR=joint.matmul(R1L,Hr,p); KS=joint.matmul(S1L,Hs,p)
G=np.zeros((npts0,len(act)*nk),dtype=np.int64)
rv=np.zeros((len(B),npts0),dtype=np.int64); sv=np.zeros((len(B),npts0),dtype=np.int64)
for j in maximal: rv[j]=int(w[j])*pd0.RQ1%p; sv[j]=int(w[j])*pd0.SQ1%p
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
z,rk,piv2,nbad=fastlin.solve(LHS,rhs0,p)
print('base joint system: cols=%d rows=%d rank=%d nbad=%d'%(LHS.shape[1],npts0,rk,nbad))
idxm={j:c for c,j in enumerate(act)}
rng=np.random.default_rng(4242+n)
NB=max(b for a,b in ans0.mons_r+ansL.mons_r)+8
def rows_for(which,js):
    out=[];rhsl=[]
    rf,sf=qrow.make_evals(n,p)
    pts=[]
    while len(pts)<NB:
        v=int(rng.integers(2,p-2))
        pts.append((0,v) if which=='k' else (v,0))
    for (kk,ll) in pts:
        row=np.zeros(LHS.shape[1],dtype=np.int64); const=0
        for j in js:
            if j in maximal:
                if not w[j]: continue
                v=(rf(0,kk,ll) if which=='k' else sf(0,kk,ll)); const=(const+int(w[j])*v)%p
            elif j==zero_j:
                mons=ans0.mons_r if which=='k' else ans0.mons_s
                off=0 if which=='k' else nr0
                D=ans0.Dr if which=='k' else ans0.Ds
                iD=pow(dval(D,n,kk,ll,p),p-2,p)
                for u,(a,b) in enumerate(mons):
                    row[off+u]=(row[off+u]+pow(kk%p,a,p)*pow(ll%p,b,p)%p*iD)%p
            else:
                c=idxm[j]; mons=ansL.mons_r if which=='k' else ansL.mons_s
                off=0 if which=='k' else nrL
                D=ansL.Dr if which=='k' else ansL.Ds
                iD=pow(dval(D,n,kk,ll,p),p-2,p)
                vec=np.zeros(ansL.nc,dtype=np.int64)
                for u,(a,b) in enumerate(mons): vec[off+u]=pow(kk%p,a,p)*pow(ll%p,b,p)%p*iD%p
                const=(const+int((vec.astype(object)@XP[:,c].astype(object))%p))%p
                contrib=(H.astype(object)@vec.astype(object))%p
                base=ans0.nc+c*nk
                row[base:base+nk]=(row[base:base+nk]+contrib.astype(np.int64))%p
        out.append(row); rhsl.append((-const)%p)
    return np.array(out,dtype=np.int64)%p, np.array(rhsl,dtype=np.int64)%p
allrows=[];allrhs=[]
for which in ('k','l'):
    cls=cert4.classes(B,which)
    for key,js in cls.items():
        js2=[j for j in js if j in idxm or j==zero_j or j in maximal]
        if not js2 or all(j in maximal for j in js2): continue
        A1,b1=rows_for(which,js2)
        L2=np.concatenate([LHS,A1],axis=0); r2=np.concatenate([rhs0,b1])
        _,rk2,_,nb2=fastlin.solve(L2,r2,p)
        print('   %s-dir class %-12s members %-34s : %s'%(which,'*'.join(key) if key else '1',
              ','.join('*'.join(B[j]) if B[j] else '1' for j in js2),
              'FEASIBLE' if nb2==0 else 'INFEASIBLE (%d rows bad)'%nb2),flush=True)
        allrows.append(A1); allrhs.append(b1)
A=np.concatenate(allrows,axis=0); bb=np.concatenate(allrhs)
L3=np.concatenate([LHS,A],axis=0); r3=np.concatenate([rhs0,bb])
_,rk3,_,nb3=fastlin.solve(L3,r3,p)
print('ALL classes together: %s (%d bad of %d Bbot rows)'%('FEASIBLE' if nb3==0 else 'INFEASIBLE',nb3,A.shape[0]))
