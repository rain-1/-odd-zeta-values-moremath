"""The measured minimal denominator M0, shared by cert2 users."""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import cert2, ordm, solve
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
EXTRA={'M0':D(0,0,1,3,3,0),'M1':D(0,0,0,3,3,0),'M2':D(0,0,2,3,3,0),'M3':D(1,1,1,3,3,0),
       'M4':D(0,0,1,3,3,1),'M5':D(1,1,2,3,3,0),'M6':D(0,0,2,3,3,1),'M7':D(2,2,2,3,3,1)}
_o = cert2.dens2
def dens2(m=3):
    o=dict(_o(m)); o.update(EXTRA); return o
cert2.dens2 = dens2
