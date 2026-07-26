"""Candidate family members + their minimal-ansatz probe."""
import sys, os, json, pickle, itertools
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import wtools as W, opt, cert2, ordm, solve
import bare

HERE='/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'
K1,L1=ordm.K1,ordm.L1; NK,NL,NKL=ordm.NK,ordm.NL,ordm.NKL
KL=[(j,0,1,1) for j in range(0,12)]
for _j in range(12): solve.NAMES[KL[_j]]='k+l+%d'%_j
def D(k1,l1,kl,nk,nl,nkl):
    out=[]
    if k1: out.append((K1,k1))
    if l1: out.append((L1,l1))
    for j in range(1,kl+1): out.append((KL[j],1))
    for j in range(1,nk+1): out.append((NK[j],1))
    for j in range(1,nl+1): out.append((NL[j],1))
    for j in range(1,nkl+1): out.append((NKL[j],1))
    return out
CAND={'M0':D(0,0,1,3,3,0),'M1':D(0,0,0,3,3,0),'M2':D(0,0,2,3,3,0),'M3':D(1,1,1,3,3,0)}
orig=cert2.dens2
def dens2(m=3):
    o=dict(orig(m)); o.update(CAND); return o
cert2.dens2=dens2

d=pickle.load(open(os.path.join(HERE,'familyQ.pkl'),'rb'))
bQ,UQ=d['base'],d['U']
J=W.J109
# --- candidate members
members={}
members['wstar'] = list(bQ)
members['wsym']  = W.symQ(bQ)
# min-support: greedily zero as many movable coordinates as possible
mov=[j for j in range(J) if any(u[j]!=0 for u in UQ)]
cur=list(bQ); zeroed=[]
for j in sorted(mov, key=lambda j: -abs(Fr(bQ[j]))):
    trial=zeroed+[j]
    w,ok=opt.zero_set(bQ,UQ,trial+opt.FORB_IDX)
    if ok:
        zeroed=trial; cur=w
members['wmin']=cur
# min-support among SYMMETRIC members
symU=[W.symQ(u) for u in UQ]
def sym_family_member(extra):
    # symmetric members = sym(base) + span(sym(U)); zero the coords in `extra`
    A=[[symU[i][j] for i in range(len(symU))] for j in extra]
    rhs=[-Fr(W.symQ(bQ)[j]) for j in extra]
    x,ok=W.solveQ(A,rhs) if A else ([],True)
    if not ok: return None
    w=W.symQ(bQ)
    for i,c in enumerate(x):
        if c: w=[w[t]+c*symU[i][t] for t in range(J)]
    return w if all(w[j]==0 for j in extra) else None
cur2=W.symQ(bQ); z2=[]
for j in sorted(mov, key=lambda j: -abs(Fr(W.symQ(bQ)[j]))):
    t=z2+[j]
    w=sym_family_member(t+opt.FORB_IDX)
    if w is not None: z2=t; cur2=w
members['wsymmin']=cur2

p=W.P1
for nm,w in members.items():
    st=W.show(w,nm)
    okrep=W.check_rep(w,10,verbose=False)
    pint=any(w[j]!=0 for j in opt.FORB_IDX)
    dens=sorted({Fr(c).denominator for c in w if c!=0})
    print('     representative: %s ; violates (P-int): %s ; coefficient denominators %s'%(okrep,pint,dens))
    pickle.dump(w,open(os.path.join(HERE,'w_%s.pkl'%nm),'wb'))
print()
print('minimal-ansatz probe (force=1, n=9):')
for nm,w in members.items():
    wp=W.to_p(w,p)
    best=None
    for dn in ['M1','M0','M3','M2']:
        for slack in range(0,16):
            r=cert2.letters_only(9,wp,W.B,dn,slack,1,p=p,verbose=False)
            if r['nfail']==0:
                a=r['ans']
                if best is None or a.nc<best[3]: best=(dn,a.par[0],a.par[1],a.nc,slack,len(r['act']),a.nc-r['rank'])
                break
    print('   %-8s -> %s bidegree (%d,%d) nc=%d [slack %d] blocks=%d ker=%d'%(nm,best[0],best[1],best[2],best[3],best[4],best[5],best[6]))
