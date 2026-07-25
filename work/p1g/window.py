"""Localise the obstruction: how few LEVELS n suffice to make [fit ; depth] inconsistent?
U := M . ker(C) is the value space of the depth-conditioned forms.  We ask for the smallest
window of levels on which  P|window  is already outside U|window."""
import sys, numpy as np
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g')
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from rfit import AB, CL, NL, KL, build_basis, rref
import rdepth

MODE=sys.argv[1] if len(sys.argv)>1 else 'vt2'
ALPH=sys.argv[2] if len(sys.argv)>2 else 'ctrl'
q=33554393
if ALPH=='ctrl':
    B=build_basis(kletters=AB,cletters=CL,nletters=NL)
    M=np.load('M_ctrl_600_33554393.npy'); b=np.load('b_ctrl_600_33554393.npy')
else:
    B=build_basis(kletters=KL,cletters=CL,nletters=NL)
    M=np.load('M_R_1300_33554393.npy'); b=np.load('b_R_1300_33554393.npy')
NC=len(B)
C=rdepth.condition_rows(B, rdepth.caps_for(MODE))
Cq=np.array([[int(v)%q for v in r] for r in C],dtype=np.int64)
print('%s %s: %d cols, %d condition rows'%(ALPH,MODE,NC,len(C)),flush=True)
lo,hi=1,M.shape[0]
# binary search on the prefix length L such that levels 1..L already obstruct
def inconsistent(L):
    A=np.concatenate([M[:L],Cq],axis=0)
    rhs=np.concatenate([b[:L],np.zeros(len(Cq),np.int64)])
    r,_,inc,_=rref(A,rhs,q)
    return inc
while lo<hi:
    mid=(lo+hi)//2
    if inconsistent(mid): hi=mid
    else: lo=mid+1
print('  smallest PREFIX of levels n=1..L that is already inconsistent: L = %d'%lo,flush=True)
# now the smallest window [n0, n0+w-1] for that width
best=None
for w in range(1,lo+1):
    for n0 in range(0,M.shape[0]-w+1):
        A=np.concatenate([M[n0:n0+w],Cq],axis=0)
        rhs=np.concatenate([b[n0:n0+w],np.zeros(len(Cq),np.int64)])
        _,_,inc,_=rref(A,rhs,q)
        if inc:
            best=(w,n0+1,n0+w); break
    if best: break
print('  smallest WINDOW of consecutive levels that is inconsistent: width %d, levels %d..%d'%best if best else '  none',flush=True)
