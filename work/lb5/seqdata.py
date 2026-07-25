"""Exact rational values of the component sums of Theorem B, for the
initial-value finish and for recurrence-order bookkeeping."""
import json, sys
from fractions import Fraction as F
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import T, Hs, Ph, P, Q

NMAX = int(sys.argv[1]) if len(sys.argv)>1 else 45

def letters(n,k,l):
    A=lambda r,x: Hs(n+x,r)-Hs(x,r)
    B=lambda r,x: Hs(n-x,r)-Hs(x,r)
    C1=Hs(n+k+l,1)-Hs(k+l,1)
    return A,B,C1

out={}
for n in range(NMAX+1):
    U=[F(0)]*5
    tot=F(0)
    for k in range(n+1):
        for l in range(n+1):
            t=T(n,k,l)
            A,B,C1=letters(n,k,l)
            U[0]+=t*A(3,k)
            U[1]+=t*A(2,k)*A(1,k)
            U[2]+=t*A(2,k)*B(1,k)
            U[3]+=t*A(2,k)*C1
            U[4]+=t*A(2,k)*A(1,l)
    R = Hs(n,3)*Q(n) + 2*U[0] - F(1,2)*U[1] - F(3,2)*U[2] - F(3,4)*U[3] - F(1,4)*U[4]
    ok = (R == Ph(n))
    out[n]={'U':[str(u) for u in U],'R':str(R),'ok':ok}
    print(n, ok, flush=True)
    if not ok:
        print('MISMATCH at n=%d'%n); break
json.dump(out, open('seqdata.json','w'))
print('done, all ok:', all(v['ok'] for v in out.values()))
