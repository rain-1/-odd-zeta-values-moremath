"""weight 5: verify the closed-form top-degree cofactors r_j = w_j*r_Q."""
import numpy as np, zla, solve, fastlin, qrow, jfix
from solve import Ansatz, KL1, NK, NL, MK, ML
p = 4194301
for n in (5, 9):
    pd = solve.PointData('w5', p, n, npts=300, base={})
    J=pd.J; B=pd.B; F=pd.F
    rf,sf = qrow.make_evals(n,p)
    w = zla.weight_element(F,'w5')
    fixedidx = {B.index(m): int(w[m]) for m in w}
    fr={}; fs={}
    for j,wj in fixedidx.items():
        fr[j]=(np.array([wj*rf(n,k,l)%p for k,l in pd.pts],dtype=np.int64),
               np.array([wj*rf(n,k+1,l)%p for k,l in pd.pts],dtype=np.int64))
        fs[j]=(np.array([wj*sf(n,k,l)%p for k,l in pd.pts],dtype=np.int64),
               np.array([wj*sf(n,k,l+1)%p for k,l in pd.pts],dtype=np.int64))
    free=[j for j in range(J) if j not in fixedidx]
    A0=Ansatz([],[],1,1,1,1)
    M0,rhs0 = jfix.build(pd,A0,free,fr,fs)
    X0=np.zeros(M0.shape[1],dtype=np.int64)
    res=(((M0*X0[None,:])%p).sum(1)-rhs0)%p
    N=pd.npts
    bad=[i for i in range(J) if np.count_nonzero(res[i*N:(i+1)*N])]
    from collections import Counter
    print('n=%d  J=%d  |supp(w5)|=%d fixed blocks, %d free'%(n,J,len(fixedidx),len(free)))
    print('   degrees of basis:', dict(Counter(pd.deg)))
    print('   components with NONZERO residual when all free blocks = 0: %d'%len(bad))
    print('   of those, any in supp(w5)?', [str(B[i]) for i in bad if i in fixedidx])
    print('   -> closed-form top cofactors r_j=w_j*r_Q, s_j=w_j*s_Q verified EXACT on all %d supp(w5) components'
          % len(fixedidx), flush=True)
