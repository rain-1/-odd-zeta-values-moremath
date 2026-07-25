import sys, time, numpy as np
from fit import *
from run_fit import build_basis
name=sys.argv[1]; N=int(sys.argv[2])
sets={'ACN':(['A%d'%r for r in range(1,6)],['C%d'%r for r in range(1,6)],['N%d'%r for r in range(1,6)]),
      'ABCN':(['A%d'%r for r in range(1,6)]+['B%d'%r for r in range(1,6)],['C%d'%r for r in range(1,6)],['N%d'%r for r in range(1,6)]),
      'ABN':(['A%d'%r for r in range(1,6)]+['B%d'%r for r in range(1,6)],[],['N%d'%r for r in range(1,6)]),
      'ACNM':(['A%d'%r for r in range(1,6)],['C%d'%r for r in range(1,6)],['N%d'%r for r in range(1,6)]+['M%d'%r for r in range(1,6)])}
kl,cl,nl=sets[name]
B=build_basis(5,False,5,2,2,maxr=5,kletters=kl,cletters=cl,nletters=nl)
Y=lad_ext('P',N+1,Q1)
M=np.zeros((N,len(B)),dtype=np.int64); b=np.zeros(N,dtype=np.int64)
for i,n in enumerate(range(1,N+1)):
    M[i]=row(n,Q1,B,depth2=False,maxr=5); b[i]=Y[n]
r,piv,inc,A=rref(M,b,Q1); rM,_,_,_=rref(M,np.zeros(N,dtype=np.int64),Q1)
print('ALPHA=%s basis=%d N=%d rank=%d INCONSISTENT=%s excess=%d'%(name,len(B),N,rM,inc,N-rM),flush=True)
