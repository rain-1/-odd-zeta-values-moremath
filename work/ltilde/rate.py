import json,sys
from fractions import Fraction as F
from math import gcd, log
from mpmath import mp, mpf, zeta, log as mlog
exec(open('prop.py').read().split('# ================= DENOMINATOR AUDIT')[0].replace("N=int",'#'))

N=int(sys.argv[1]) if len(sys.argv)>1 else 70
lad={nm:propagate(a0,a1,a2,unlock3(a0,a1,a2),N) for nm,(a0,a1,a2) in anch.items()}

def dlcm(n):
    L=1
    for i in range(1,n+1): L=L*i//gcd(L,i)
    return L
print("\n=== A. DENOMINATOR LEDGER: is the ladder genuine? ===")
print(" n   den(s_n)|d^5  den(Ph_n)|d^5   EXCESS of den(P_n) over d^7 (digits)")
for n in list(range(3,10))+list(range(10,N+1,5)):
    d=dlcm(n)
    r=[]
    for nm,k in (('s',5),('Ph',5)):
        den=lad[nm][n].denominator
        r.append("YES" if (d**k)%den==0 else "NO ")
    denP=lad['P'][n].denominator
    exc=denP//gcd(denP,dlcm(n)**7)
    print(f"{n:3d}   {r[0]}          {r[1]}            {len(str(exc)):5d} digits   ({'bounded' if exc<10**6 else 'GROWING'})")

# ---------- rate of I'' ----------
print("\n=== B. RATE OF I''  (exact rationals -> mpmath) ===")
Ipp={}
for n in range(N+1):
    mp.dps = int(4.9*n)+80
    z3,z5=zeta(3),zeta(5)
    Ipp[n]=-9*mpf(lad['q'][n].numerator)/lad['q'][n].denominator*z5 \
           +2*mpf(lad['s'][n].numerator)/lad['s'][n].denominator*z3 \
           -mpf(lad['Ph'][n].numerator)/lad['Ph'][n].denominator
mp.dps=50
print(" n   I''_n                      ratio I''_{n+1}/I''_n     log|I''_n|/n")
for n in list(range(0,10))+list(range(10,N+1,5)):
    r = Ipp[n+1]/Ipp[n] if n+1<=N else None
    print(f"{n:3d}  {mp.nstr(Ipp[n],10):>24}  {(mp.nstr(r,10) if r is not None else ''):>20}   {mp.nstr(mlog(abs(Ipp[n]))/n,10) if n else ''}")
import pickle; pickle.dump({n:str(Ipp[n]) for n in Ipp}, open('ipp.pkl','wb'))
pickle.dump({nm:[(x.numerator,x.denominator) for x in lad[nm]] for nm in lad}, open('lad.pkl','wb'))
