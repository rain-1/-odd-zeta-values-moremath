import numpy as np, sys, zla, solve, fastlin, joint
from solve import Ansatz, KL1, KL2, NK, NL, MK, ML
p = 4194301; n = 5
D = [(KL1,1)]+[(NK[j],1) for j in (1,2,3)]+[(NL[j],1) for j in (1,2,3)]
dk0=4; dl0=4
cfg = [(8,400),(14,760)] if len(sys.argv)<2 else [(int(sys.argv[1]),int(sys.argv[2]))]
for slack,npts in cfg:
    pd = solve.PointData('w3', p, n, npts=npts, base={})
    A = Ansatz(D,D,dk0+slack,dl0+slack,dk0+slack,dl0+slack,force_k=1,force_l=1)
    M,rhs,ncols = joint.build(pd,A)
    J=pd.J; F=pd.F
    mmax=6
    W=np.zeros((J*npts,mmax+1),dtype=np.int64)
    for t,(k,l) in enumerate(pd.pts):
        for a in range(mmax+1):
            el=zla.w_shift_mixed(F,pd.w,a,n,k,l,{})
            v=zla.el_to_vec(F,pd.B,zla.el_scale(F,el,F.cst(zla.Pi(n,k,l,a))))
            for i in range(J): W[i*npts+t,a]=v[i]
    X,rank,piv,nbad = fastlin.solve(M,rhs,p,nb=64)
    print('L_BZ inhomogeneous: nc=%d cols=%d rows=%d rank=%d nbad=%d %s'
          %(A.nc,ncols,M.shape[0],rank,nbad,'CONSISTENT' if nbad==0 else 'INCONSISTENT'), flush=True)
    R0=rank
    for m in (3,4,5,6):
        R1,_ = fastlin.rank_only(np.concatenate([M,(-W[:,:m+1])%p],axis=1),p)
        print('   free-d order<=%d : rank=%d -> %d telescoper direction(s)'%(m,R1,(m+1)-(R1-R0)), flush=True)
