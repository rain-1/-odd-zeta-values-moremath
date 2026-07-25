"""Does the refold vtilde satisfy the weight-3 depth bound  d3 <= 1 + min(v_pT,2) ?
(PHASE2_ENDGAME 35-60 / PHASE2_THEOREM's middle-row leaf.)  Control column: v."""
import sys, os
from fractions import Fraction as F
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import T, Hs, vp, w3hat
from sympy import primerange
def vt(n,k,l):
    A=lambda r,x: Hs(n+x,r)-Hs(x,r); B=lambda r,x: Hs(n-x,r)-Hs(x,r)
    return 2*A(3,k) + F(1,2)*(A(2,l)-A(2,k))*(A(1,k)+3*B(1,k))     # vtilde - H^(3)_n
def vv(n,k,l): return w3hat(n,k,l) - Hs(n,3)                       # the control
for name,f in (('vtilde', vt), ('v = w3hat - H3n (control)', vv)):
    worst=0; viol=0; cells=0
    for p in primerange(5,32):
        for n in range(1,p):
            for k in range(n+1):
                for l in range(n+1):
                    d=max(0,-vp(f(n,k,l),p)); vT=vp(T(n,k,l),p); cells+=1
                    worst=max(worst,d)
                    if d > 1+min(vT,2): viol+=1
    print('%-28s max d3 = %d ; cells = %d ; violations of d3 <= 1+min(vT,2) : %d'
          % (name, worst, cells, viol), flush=True)
