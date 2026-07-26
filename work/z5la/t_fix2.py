import numpy as np, sys, zla, solve, fastlin, jfix, qrow
from solve import Ansatz, KL1, NK, NL, MK, ML
p = 4194301; n = 5
pd = solve.PointData('w3', p, n, npts=760, base={})
J=pd.J; B=pd.B
rf, sf = qrow.make_evals(n, p)
w = zla.weight_element(zla.Fp(p), 'w3')
fixedidx = [B.index(m) for m in w]
fr={}; fs={}
for j in fixedidx:
    wj = int(w[B[j]])
    fr[j]=(np.array([wj*rf(n,k,l)%p for k,l in pd.pts],dtype=np.int64),
           np.array([wj*rf(n,k+1,l)%p for k,l in pd.pts],dtype=np.int64))
    fs[j]=(np.array([wj*sf(n,k,l)%p for k,l in pd.pts],dtype=np.int64),
           np.array([wj*sf(n,k,l+1)%p for k,l in pd.pts],dtype=np.int64))
free=[j for j in range(J) if j not in fixedidx]
# --- diagnostic: are the FIXED components' own equations satisfied exactly? ---
A0 = Ansatz([],[],2,2,2,2)
M0,rhs0 = jfix.build(pd,A0,free,fr,fs)
X0 = np.zeros(M0.shape[1],dtype=np.int64)
res0 = (((M0*X0[None,:])%p).sum(1) - rhs0) % p
N=pd.npts
print('per-component residual with ALL free blocks = 0 (i.e. is r_j = w_j r_Q exact on supp(w)?):', flush=True)
for i in range(J):
    nz = int(np.count_nonzero(res0[i*N:(i+1)*N]))
    print('   %-16s %s  bad=%d'%(str(B[i]), 'FIXED' if i in fixedidx else 'free ', nz), flush=True)
# --- bigger ansatz for the free blocks ---
D = [(KL1,1)]+[(MK[j],1) for j in (0,1,2,3)]+[(ML[j],1) for j in (0,1,2,3)] \
    +[(NK[j],1) for j in (1,2,3)]+[(NL[j],1) for j in (1,2,3)]
dk0=sum(m*abs(f[2]) for f,m in D); dl0=sum(m*abs(f[3]) for f,m in D)
print('D deg=(%d,%d)'%(dk0,dl0), flush=True)
for slack in (6,8,10):
    A=Ansatz(D,D,dk0+slack,dl0+slack,dk0+slack,dl0+slack,force_k=1,force_l=1)
    cols=len(free)*A.nc
    if cols > 1.05*J*N: print('slack',slack,'skip cols',cols, flush=True); continue
    M,rhs = jfix.build(pd,A,free,fr,fs)
    X,rank,piv,nbad = fastlin.solve(M,rhs,p,nb=64)
    res=(((M*X[None,:])%p).sum(1)-rhs)%p
    per=[int(np.count_nonzero(res[i*N:(i+1)*N])) for i in range(J)]
    print('slack=%2d nc=%4d cols=%5d rank=%5d nbad=%5d %s'%(slack,A.nc,cols,rank,nbad,
          '*** CONSISTENT ***' if nbad==0 else 'per-comp bad: '+str({str(B[i]):per[i] for i in range(J) if per[i]})), flush=True)
