import numpy as np, time, sys
from fit import *
from run_fit import build_basis
q = Q2
kl=['A%d'%r for r in range(1,6)]+['B%d'%r for r in range(1,6)]
cl=['C%d'%r for r in range(1,6)]
nl=['N%d'%r for r in range(1,6)]+['M%d'%r for r in range(1,6)]
B=build_basis(5, False, 3,2,2, maxr=5, kletters=kl, cletters=cl, nletters=nl)
N=900
Y=lad_ext('P',N+1,q)
M=np.zeros((N,len(B)),dtype=np.int64); b=np.zeros(N,dtype=np.int64)
t=time.time()
for i,n in enumerate(range(1,N+1)):
    M[i]=row(n,q,B,depth2=False,maxr=5); b[i]=Y[n]
print('built %.0fs'%(time.time()-t),flush=True)
r,piv,inc,A=rref(M,b,q); rM,_,_,_=rref(M,np.zeros(N,dtype=np.int64),q)
print('PRIME Q2: basis=%d N=%d rank(M)=%d rank([M|b])=%d INCONSISTENT=%s'%(len(B),N,rM,r,inc))
# also: what if we fit Ph (weight 3 target) in the weight-5 basis? sanity: should be inconsistent too
