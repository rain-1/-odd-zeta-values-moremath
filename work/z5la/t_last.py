import numpy as np, zla, solve, fastlin, qrow, sub2
from solve import Ansatz, KL1, NK, NL, MK, ML
p = 4194301; n = 5; NPTS=2400
pd = solve.PointData('w3', p, n, npts=NPTS, base={})
J=pd.J; B=pd.B; F=pd.F
i1=B.index(('xk',)); j2=B.index(('u2','xk'))
rf,sf = qrow.make_evals(n,p)
w = zla.weight_element(F,'w3'); fixedidx={B.index(m):int(w[m]) for m in w}
# (a) MIRROR Q-row certificate: rho'(n,k,l)=sigma(n,l,k), sigma'(n,k,l)=rho(n,l,k)
def rfM(nn,k,l): return sf(nn,l,k)
def sfM(nn,k,l): return rf(nn,l,k)
D = [(KL1,1),(NK[1],1),(NK[2],1),(NK[3],1),(NL[1],1),(NL[2],1),(NL[3],1)] \
    +[(MK[j],1) for j in (0,1,2,3)]+[(ML[j],1) for j in (0,1,2,3)]
dk0=sum(m*abs(f[2]) for f,m in D); dl0=sum(m*abs(f[3]) for f,m in D)
for lab,(RF,SF) in (('Qrow',(rf,sf)),('mirror',(rfM,sfM))):
    ok = True
    for slack in (6,10):
        A=Ansatz(D,D,dk0+slack,dl0+slack,dk0+slack,dl0+slack,force_k=1,force_l=1)
        if A.nc>0.9*NPTS: continue
        nc=A.nc; nr=len(A.mons_r)
        from solve import dval
        M=np.zeros((NPTS,nc),dtype=np.int64); rhs=np.zeros(NPTS,dtype=np.int64)
        dmax=max(max(a,b) for a,b in A.mons_r+A.mons_s)+2
        for t,(k,l) in enumerate(pd.pts):
            gk=int(pd.gk[t]); gl=int(pd.gl[t])
            iDr=pow(dval(A.Dr,n,k,l,p),p-2,p); iDrk=pow(dval(A.Dr,n,k+1,l,p),p-2,p)
            iDs=pow(dval(A.Ds,n,k,l,p),p-2,p); iDsl=pow(dval(A.Ds,n,k,l+1,p),p-2,p)
            kp=[pow(k%p,a,p) for a in range(dmax)]; lp=[pow(l%p,b,p) for b in range(dmax)]
            k1=[pow((k+1)%p,a,p) for a in range(dmax)]; l1=[pow((l+1)%p,b,p) for b in range(dmax)]
            for u,(a,b) in enumerate(A.mons_r): M[t,u]=(gk*k1[a]%p*lp[b]%p*iDrk-kp[a]*lp[b]%p*iDr)%p
            for u,(a,b) in enumerate(A.mons_s): M[t,nr+u]=(gl*kp[a]%p*l1[b]%p*iDsl-kp[a]*lp[b]%p*iDs)%p
            Sk=(pd.Nk[t]+np.eye(J,dtype=np.int64))%p; Sl=(pd.Nl[t]+np.eye(J,dtype=np.int64))%p
            tot=int(pd.bvec[t,i1])
            for j,wj in fixedidx.items():
                a=(int(Sk[i1,j])-(1 if i1==j else 0))%p; b=(int(Sl[i1,j])-(1 if i1==j else 0))%p
                if a: tot=(tot-gk*a%p*(wj*RF(n,k+1,l)%p))%p
                if b: tot=(tot-gl*b%p*(wj*SF(n,k,l+1)%p))%p
            rhs[t]=tot%p
        X,rank,nb1,nbad = fastlin.solve(M,rhs,p,nb=64)
        print('%-8s slack=%2d nc=%4d rank=%4d nbad=%4d %s'%(lab,slack,nc,rank,nbad,'*** OK ***' if nbad==0 else ''), flush=True)
# (b) joint: top block FREE (its own equation imposed) + xk block, both with D
for slack in (6,10):
    A=Ansatz(D,D,dk0+slack,dl0+slack,dk0+slack,dl0+slack,force_k=1,force_l=1)
    if 2*A.nc>1.05*2*NPTS: continue
    M,rhs = sub2.build(pd,A,i1,j2)
    X,rank,piv,nbad = fastlin.solve(M,rhs,p,nb=64)
    res=(((M*X[None,:])%p).sum(1)-rhs)%p
    print('joint2   slack=%2d nc=%4d cols=%d rank=%5d nbad=%4d bad(xk)=%4d %s'
          %(slack,A.nc,2*A.nc,rank,nbad,int(np.count_nonzero(res[NPTS:])),'*** OK ***' if nbad==0 else ''), flush=True)
