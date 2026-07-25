"""Independent check: Sum_{k,l} T * vtilde satisfies L_BZ exactly (order 3, the (3,9)
box), and equals Phat.  Uses core.rec_residual, i.e. the certified V6b coefficients."""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import T, Hs, Ph, rec_residual

def vt(n,k,l):
    A=lambda r,x: Hs(n+x,r)-Hs(x,r); B=lambda r,x: Hs(n-x,r)-Hs(x,r)
    Psik = A(1,k) + 3*B(1,k)
    return Hs(n,3) + 2*A(3,k) + F(1,2)*(A(2,l)-A(2,k))*Psik

def S(n):
    return sum(T(n,k,l)*vt(n,k,l) for k in range(n+1) for l in range(n+1))

vals={n:S(n) for n in range(0,34)}
bad=[n for n in vals if vals[n]!=Ph(n)]
print('Sum T*vtilde == Phat for n=0..33 :', 'ALL PASS' if not bad else 'FAIL %s'%bad)
r=[n for n in range(0,31) if rec_residual(lambda m: vals[m], n)!=0]
print('L_BZ * (Sum T*vtilde) == 0 for n=0..30 :', 'ALL ZERO' if not r else 'FAIL %s'%r)
print('vtilde(3,1,2) =', vt(3,1,2), '   Phat(5) =', Ph(5))
