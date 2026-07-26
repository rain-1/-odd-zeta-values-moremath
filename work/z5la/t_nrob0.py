"""robustness of the scalar obstruction across n and p"""
import numpy as np, zla, solve, fastlin, qrow
from solve import Ansatz, KL1, KL2, NK, NL, MK, ML, dval
NPTS=1500
D = [(KL1,1),(NK[1],1),(NK[2],1),(NK[3],1),(NL[1],1),(NL[2],1),(NL[3],1)] \
    +[(MK[j],1) for j in (0,1,2,3)]+[(ML[j],1) for j in (0,1,2,3)]
dk0=sum(m*abs(f[2]) for f,m in D); dl0=sum(m*abs(f[3]) for f,m in D)
for p in (4194301,):
  for n in (5,):
    F=zla.Fp(p)
    pd = solve.PointData('w3', p, n, npts=NPTS, base={})
    J=pd.J; B=pd.B
    rf,sf = qrow.make_evals(n,p)
    w = zla.weight_element(F,'w3'); fixedidx={B.index(m):int(w[m]) for m in w}
    fv=np.zeros((J,NPTS),dtype=np.int64)
    for t,(k,l) in enumerate(pd.pts):
        gk=int(pd.gk[t]); gl=int(pd.gl[t])
        Sk=(pd.Nk[t]+np.eye(J,dtype=np.int64))%p; Sl=(pd.Nl[t]+np.eye(J,dtype=np.int64))%p
        for i in range(J):
            tot=int(pd.bvec[t,i])
            for j,wj in fixedidx.items():
                a=(int(Sk[i,j])-(1 if i==j else 0))%p; b=(int(Sl[i,j])-(1 if i==j else 0))%p
                if a: tot=(tot-gk*a%p*(wj*rf(n,k+1,l)%p))%p
                if b: tot=(tot-gl*b%p*(wj*sf(n,k,l+1)%p))%p
            fv[i,t]=tot%p
    slack=12
    A=Ansatz(D,D,dk0+slack,dl0+slack,dk0+slack,dl0+slack,force_k=0,force_l=0)
    nc=A.nc; nr=len(A.mons_r)
    M=np.zeros((NPTS,nc),dtype=np.int64)
    dmax=max(max(a,b) for a,b in A.mons_r+A.mons_s)+2
    for t,(k,l) in enumerate(pd.pts):
        gk=int(pd.gk[t]); gl=int(pd.gl[t])
        iDr=pow(dval(A.Dr,n,k,l,p),p-2,p); iDrk=pow(dval(A.Dr,n,k+1,l,p),p-2,p)
        iDs=pow(dval(A.Ds,n,k,l,p),p-2,p); iDsl=pow(dval(A.Ds,n,k,l+1,p),p-2,p)
        kp=[pow(k%p,a,p) for a in range(dmax)]; lp=[pow(l%p,b,p) for b in range(dmax)]
        k1=[pow((k+1)%p,a,p) for a in range(dmax)]; l1=[pow((l+1)%p,b,p) for b in range(dmax)]
        for u,(a,b) in enumerate(A.mons_r): M[t,u]=(gk*k1[a]%p*lp[b]%p*iDrk-kp[a]*lp[b]%p*iDr)%p
        for u,(a,b) in enumerate(A.mons_s): M[t,nr+u]=(gl*kp[a]%p*l1[b]%p*iDsl-kp[a]*lp[b]%p*iDs)%p
    out=[]
    for i in [B.index(('xk',)),B.index(('u2',)),B.index(())]:
        X,rank,piv,nbad = fastlin.solve(M,fv[i].copy(),p,nb=64)
        out.append('%s nbad=%d'%(str(B[i]),nbad))
    print('p=%d n=%2d nc=%d rank=%d : %s'%(p,n,nc,rank,'  '.join(out)), flush=True)
