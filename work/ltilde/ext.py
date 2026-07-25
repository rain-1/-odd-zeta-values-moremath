import sys, pickle
from fractions import Fraction as F
from math import gcd
from mpmath import mp, mpf, log as mlog
exec(open('prop.py').read().split('# ================= DENOMINATOR AUDIT')[0].replace("N=int",'#'))
N=140
lad={nm:propagate(a0,a1,a2,unlock3(a0,a1,a2),N) for nm,(a0,a1,a2) in anch.items()}
def dlcm(n):
    L=1
    for i in range(1,n+1): L=L*i//gcd(L,i)
    return L
# ---- denominator ledger to n=140 (the ladder-genuineness certificate) ----
okS=okP=0
for n in range(N+1):
    d5=dlcm(n)**5
    if d5%lad['s'][n].denominator==0: okS+=1
    if d5%lad['Ph'][n].denominator==0: okP+=1
print(f"LEDGER n=0..{N}:  den(s_n) | d_n^5 : {okS}/{N+1}      den(Ph_n) | d_n^5 : {okP}/{N+1}")
# ---- TRUE kappa of the descent ladder: log den / n , and log d_n^5 / n ----
print("\n=== TRUE denominator exponent (kappa) of the weight-5 descent ladder ===")
print("  n   log den(s_n)/n   log den(Ph_n)/n   log(d_n^5)/n [=5*psi]   ord-ratio Ph/d^5")
for n in [20,40,60,80,100,120,140]:
    ds=lad['s'][n].denominator; dp=lad['Ph'][n].denominator; d=dlcm(n)
    import math
    ls=math.log(ds)/n if ds>1 else 0.0; lp=math.log(dp)/n; ld=5*math.log(d)/n
    print(f"  {n:3d}   {ls:12.6f}   {lp:14.6f}   {ld:18.6f}   {lp/ld:16.4f}")
# ---- I'' to n=140 ----
Ipp={}
for n in range(N+1):
    mp.dps=int(4.9*n)+100
    z3,z5=mp.zeta(3),mp.zeta(5)
    Ipp[n]=(-9*mpf(lad['q'][n].numerator)/lad['q'][n].denominator*z5
            +2*mpf(lad['s'][n].numerator)/lad['s'][n].denominator*z3
            -mpf(lad['Ph'][n].numerator)/lad['Ph'][n].denominator)
pickle.dump({n:str(Ipp[n]) for n in Ipp},open('ipp140.pkl','wb'))
mp.dps=60
Lg={n:-mlog(abs(Ipp[n+1]/Ipp[n])) for n in range(N)}
print("\n=== RATE: two DISJOINT windows, raw + Richardson(n,2n) + Richardson2 ===")
def R1(n): return 2*Lg[2*n]-Lg[n]
def R2(n): return (4*R1(2*n)-R1(n))/3
print("   n |     raw      |  Rich1(n,2n) |  Rich2")
for n in [10,20,30,35,40,50,60,65,69]:
    r1=R1(n) if 2*n in Lg else None
    r2=R2(n) if 4*n in Lg else None
    print(f"  {n:3d} | {mp.nstr(Lg[n],11):>12} | {(mp.nstr(r1,11) if r1 else '-'):>12} | {(mp.nstr(r2,11) if r2 else '-'):>12}")
tgt=-mlog(mpf(1)/mpf('10.645366')) if False else None
print("\n  sector B  -log rho_B = ", end='')
import mpmath
rts=mpmath.polyroots([1,-6340,67974,-6340,1],maxsteps=200,extraprec=200)
rts=sorted([mp.re(x) for x in rts])
print(mp.nstr(-mlog(rts[1]),12), "   (rho_B =",mp.nstr(rts[1],12),")")
print("  the four candidate -log(root) values:", [mp.nstr(-mlog(x),10) for x in rts])
