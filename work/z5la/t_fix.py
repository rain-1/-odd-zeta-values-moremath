import numpy as np, sys, zla, solve, fastlin, jfix, qrow
from solve import Ansatz, KL1, KL2, NK, NL, MK, ML
p = 4194301; n = 5
pd = solve.PointData('w3', p, n, npts=900, base={})
J=pd.J; B=pd.B
rf, sf = qrow.make_evals(n, p)
w = zla.weight_element(zla.Fp(p), 'w3')
fixedidx = [B.index(m) for m in w]
print('fixed blocks:', [str(B[j]) for j in fixedidx], flush=True)
fr={}; fs={}
for j in fixedidx:
    wj = int(w[B[j]])
    fr[j]=(np.array([wj*rf(n,k,l)%p for k,l in pd.pts],dtype=np.int64),
           np.array([wj*rf(n,k+1,l)%p for k,l in pd.pts],dtype=np.int64))
    fs[j]=(np.array([wj*sf(n,k,l)%p for k,l in pd.pts],dtype=np.int64),
           np.array([wj*sf(n,k,l+1)%p for k,l in pd.pts],dtype=np.int64))
free=[j for j in range(J) if j not in fixedidx]
print('free blocks (%d):'%len(free), [str(B[j]) for j in free], flush=True)
for D,lab in (([],'poly'),([(KL1,1)],'kl'),([(KL1,1),(NL[2],1),(NL[3],1)],'kl+nl23'),
              ([(KL1,1)]+[(NK[j],1) for j in (1,2,3)]+[(NL[j],1) for j in (1,2,3)],'kl+nk+nl'),
              ([(KL1,1)]+[(MK[j],1) for j in (1,2,3)]+[(ML[j],1) for j in (1,2,3)],'kl+mk+ml')):
    dk0=sum(m*abs(f[2]) for f,m in D); dl0=sum(m*abs(f[3]) for f,m in D)
    for slack in (8,10,12):
        A=Ansatz(D,D,dk0+slack,dl0+slack,dk0+slack,dl0+slack,force_k=1,force_l=1)
        cols=len(free)*A.nc
        if cols > 1.1*J*pd.npts:
            print('%-10s slack=%2d skip cols=%d'%(lab,slack,cols), flush=True); continue
        M,rhs = jfix.build(pd,A,free,fr,fs)
        X,rank,piv,nbad = fastlin.solve(M,rhs,p,nb=64)
        print('%-10s slack=%2d nc=%4d cols=%5d rows=%5d rank=%5d nbad=%5d %s'
              %(lab,slack,A.nc,cols,M.shape[0],rank,nbad,'*** CONSISTENT ***' if nbad==0 else ''), flush=True)
