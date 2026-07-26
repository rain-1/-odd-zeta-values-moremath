"""FINAL compact forms, stated in the Psi-normalisation, verified exactly."""
import sys
from fractions import Fraction as F
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import T, Hs, Ph, P, rec_residual

def L(n,k,l):
    A1k=Hs(n+k,1)-Hs(k,1); A1l=Hs(n+l,1)-Hs(l,1)
    B1k=Hs(n-k,1)-Hs(k,1); B1l=Hs(n-l,1)-Hs(l,1)
    A2k=Hs(n+k,2)-Hs(k,2); A2l=Hs(n+l,2)-Hs(l,2)
    al=A1k-A1l; be=B1k-B1l
    return al, be, F(1,2)*al+be, A2k+A2l

def w3(n,k,l):
    al,be,Psi,S2 = L(n,k,l)
    return Hs(n+k,3) - Psi*Hs(n+k,2)

def w5(n,k,l):
    al,be,Psi,S2 = L(n,k,l)
    return (Hs(n+k,5) + F(1,2)*(al-be)*Hs(n+k,4)
            + (F(1,4)*S2 - F(1,2)*al*Psi)*Hs(n+k,3))

S=lambda n,w: sum(T(n,k,l)*w(n,k,l) for k in range(n+1) for l in range(n+1))
S3={}; S5={}; b3=[]; b5=[]
for n in range(0,35):
    S3[n]=S(n,w3); S5[n]=S(n,w5)
    if S3[n]!=Ph(n): b3.append(n)
    if S5[n]!=P(n):  b5.append(n)
print('w3 = H3[n+k] - Psi*H2[n+k]                       -> Phat :',
      'ALL PASS n=0..34' if not b3 else 'FAIL %s'%b3)
print('w5 = H5[n+k] + (al-be)/2 H4[n+k] + (S2/4 - al*Psi/2) H3[n+k] -> P :',
      'ALL PASS n=0..34' if not b5 else 'FAIL %s'%b5)
r3=[n for n in range(32) if rec_residual(lambda m:S3[m],n)!=0]
r5=[n for n in range(32) if rec_residual(lambda m:S5[m],n)!=0]
print('L_BZ annihilates both, n=0..31 :', 'YES' if not r3 and not r5 else (r3,r5))
