"""Single-component scalar sweep: with the top-degree cofactors FIXED to
w_j*r_Q (proved exact), each remaining component is a standalone scalar WZ
problem  f_i = gk r(k+1,l) - r + gl s(k,l+1) - s  with f_i fully known."""
import numpy as np, zla, solve, fastlin, qrow
from solve import Ansatz, KL1, KL2, NK, NL, MK, ML, dval, dstr
p = 4194301; n = 5
NKL=[(j,1,1,1) for j in range(0,5)]
for j in range(5): solve.NAMES[NKL[j]]='n+k+l+%d'%j
NPTS = 2600
pd = solve.PointData('w3', p, n, npts=NPTS, base={})
J=pd.J; B=pd.B; F=pd.F
rf,sf = qrow.make_evals(n,p)
w = zla.weight_element(F,'w3'); fixedidx={B.index(m):int(w[m]) for m in w}
# precompute f_i at all sample points
fvals = np.zeros((J, NPTS), dtype=np.int64)
for t,(k,l) in enumerate(pd.pts):
    gk=int(pd.gk[t]); gl=int(pd.gl[t])
    Sk=(pd.Nk[t]+np.eye(J,dtype=np.int64))%p; Sl=(pd.Nl[t]+np.eye(J,dtype=np.int64))%p
    for i in range(J):
        tot=int(pd.bvec[t,i])
        for j,wj in fixedidx.items():
            a=int(Sk[i,j])-(1 if i==j else 0); b=int(Sl[i,j])-(1 if i==j else 0)
            if a%p: tot=(tot-gk*(a%p)%p*(wj*rf(n,k+1,l)%p))%p
            if b%p: tot=(tot-gl*(b%p)%p*(wj*sf(n,k,l+1)%p))%p
        fvals[i,t]=tot%p
def scalmat(A):
    nc=A.nc; nr=len(A.mons_r)
    M=np.zeros((NPTS,nc),dtype=np.int64)
    dmax=max(max(a,b) for a,b in A.mons_r+A.mons_s)+2
    for t,(k,l) in enumerate(pd.pts):
        gk=int(pd.gk[t]); gl=int(pd.gl[t])
        iDr=pow(dval(A.Dr,n,k,l,p),p-2,p); iDrk=pow(dval(A.Dr,n,k+1,l,p),p-2,p)
        iDs=pow(dval(A.Ds,n,k,l,p),p-2,p); iDsl=pow(dval(A.Ds,n,k,l+1,p),p-2,p)
        kp=[pow(k%p,a,p) for a in range(dmax)]; lp=[pow(l%p,b,p) for b in range(dmax)]
        k1=[pow((k+1)%p,a,p) for a in range(dmax)]; l1=[pow((l+1)%p,b,p) for b in range(dmax)]
        for u,(a,b) in enumerate(A.mons_r): M[t,u]=(gk*k1[a]%p*lp[b]%p*iDrk - kp[a]*lp[b]%p*iDr)%p
        for u,(a,b) in enumerate(A.mons_s): M[t,nr+u]=(gl*kp[a]%p*l1[b]%p*iDsl - kp[a]*lp[b]%p*iDs)%p
    return M
base = [(KL1,1),(NK[1],1),(NK[2],1),(NL[2],1)]
Ds = {
 'D1': base,
 'D2': base+[(NK[3],1),(NL[3],1)],
 'D3': base+[(NK[3],1),(NL[3],1)]+[(MK[j],1) for j in (0,1,2,3)]+[(ML[j],1) for j in (0,1,2,3)],
 'D4': base+[(NK[3],1),(NL[3],1),(KL2,1),(NKL[1],1),(NKL[2],1)],
 'D5': [(KL1,2),(NK[1],2),(NK[2],2),(NK[3],2),(NL[2],2),(NL[3],2)],
}
targets=[B.index(('xk',)), B.index(())]
for lab,D in Ds.items():
    dk0=sum(m*abs(f[2]) for f,m in D); dl0=sum(m*abs(f[3]) for f,m in D)
    for slack in (6,10,14,18,24):
        A=Ansatz(D,D,dk0+slack,dl0+slack,dk0+slack,dl0+slack,force_k=1,force_l=1)
        if A.nc>0.85*NPTS: continue
        M=scalmat(A)
        out=[]
        for i in targets:
            X,rank,piv,nbad = fastlin.solve(M,fvals[i].copy(),p,nb=64)
            out.append((str(B[i]),rank,nbad))
        print('%-3s deg=(%d,%d) nc=%4d : %s'%(lab,dk0+slack,dl0+slack,A.nc,
              '  '.join('%s rank=%d nbad=%d%s'%(a,b,c,' ***OK***' if c==0 else '') for a,b,c in out)), flush=True)
