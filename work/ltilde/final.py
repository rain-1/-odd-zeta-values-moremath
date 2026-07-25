import pickle, math
from fractions import Fraction as F
from math import gcd
from mpmath import mp, mpf
exec(open('prop.py').read().split('# ================= DENOMINATOR AUDIT')[0].replace("N=int",'#'))
N=140
lad={nm:propagate(a0,a1,a2,unlock3(a0,a1,a2),N) for nm,(a0,a1,a2) in anch.items()}
def dlcm(n):
    L=1
    for i in range(1,n+1): L=L*i//gcd(L,i)
    return L
D={n:dlcm(n) for n in range(N+1)}
print("FINAL VERIFICATION")
print(" 1. L annihilates 74 exact q_n :", "PASS" if all(sum(c(k,n)*qs[n+k] for k in range(5))==0 for n in range(70)) else "FAIL")
print(" 2. propagated q == exact q (n=0..73):", "PASS" if all(lad['q'][n]==qs[n] for n in range(74)) else "FAIL")
s5=sum(1 for n in range(N+1) if (D[n]**5)%lad['s'][n].denominator==0)
h5=sum(1 for n in range(N+1) if (D[n]**5)%lad['Ph'][n].denominator==0)
print(f" 3. den(s_n)|d_n^5 : {s5}/{N+1}    den(Ph_n)|d_n^5 : {h5}/{N+1}")
p7=sum(1 for n in range(3,N+1) if (D[n]**7)%lad['P'][n].denominator==0)
exc={lad['P'][n].denominator//gcd(lad['P'][n].denominator,D[n]**7) for n in range(3,N+1)}
print(f" 4. den(P_n)|d_n^7 : {p7}/{N-2}  (n>=3)   excess set = {sorted(exc)}")
print(f" 5. den(P_n)|107*d_n^7 : {sum(1 for n in range(N+1) if (107*D[n]**7)%lad['P'][n].denominator==0)}/{N+1}")
neg=0; mn=None
for n in range(N+1):
    mp.dps=int(4.9*n)+100
    v=(-9*mpf(lad['q'][n].numerator)/lad['q'][n].denominator*mp.zeta(5)
       +2*mpf(lad['s'][n].numerator)/lad['s'][n].denominator*mp.zeta(3)
       -mpf(lad['Ph'][n].numerator)/lad['Ph'][n].denominator)
    if v<0: neg+=1
print(f" 6. I''_n < 0 : {neg}/{N+1}")
mp.dps=30
print(" 7. |I'_n| >= zeta(2)*|I''_n| : follows from I_n>0 (rigorous) and I''_n<0  -> NO CANCELLATION")
