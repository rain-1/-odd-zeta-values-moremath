import pickle, json
from fractions import Fraction as F
from math import gcd
from mpmath import mp, mpf, log as mlog
lad=pickle.load(open('lad.pkl','rb')); ipp=pickle.load(open('ipp.pkl','rb'))
N=max(ipp)
def dlcm(n):
    L=1
    for i in range(1,n+1): L=L*i//gcd(L,i)
    return L
def fac(m):
    f={};d=2
    while d*d<=m:
        while m%d==0: f[d]=f.get(d,0)+1; m//=d
        d+=1 if d==2 else 2
    if m>1: f[m]=f.get(m,0)+1
    return f
print("=== excess of den(P_n^{L-prop}) over d_n^7 : ACTUAL VALUE ===")
vals=set()
for n in range(3,N+1):
    den=lad['P'][n][1]; e=den//gcd(den,dlcm(n)**7); vals.add(e)
print("  distinct excess values over n=3..%d:"%N, sorted(vals), "  -> factor:", {v:fac(v) for v in sorted(vals)})

print("\n=== SIGN STRUCTURE ===")
mp.dps=40
neg=sum(1 for n in range(N+1) if mpf(ipp[n])<0)
print(f"  I''_n < 0 for {neg} of {N+1} indices n=0..{N}   (all-negative: {neg==N+1})")
print("  I_n  > 0 for all n : RIGOROUS (all-positive 4-fold series, ZETA7_STATE 1.7)")
print("  => I'_n = I_n - z2*I''_n = I_n + z2*|I''_n| :  NO CANCELLATION, |I'_n| >= z2*|I''_n|")

print("\n=== RATE OF |I''| : raw, Aitken, Richardson  (target -log rho_B = 2.36504926...) ===")
mp.dps=60
r={n: mpf(ipp[n+1])/mpf(ipp[n]) for n in range(N)}
L={n: -mlog(abs(mpf(ipp[n+1])/mpf(ipp[n]))) for n in range(N)}   # -log ratio -> -log rho
def rich(seq,ks):  # assume a_n = L + c/n : Richardson  2*a_{2n}-a_n  etc; use 1st+2nd order
    out={}
    for n in ks:
        if 2*n in seq: out[n]=2*seq[2*n]-seq[n]
    return out
def aitken(seq,ks):
    out={}
    for n in ks:
        if n+2 in seq:
            d1=seq[n+1]-seq[n]; d2=seq[n+2]-2*seq[n+1]+seq[n]
            if d2!=0: out[n]=seq[n]-d1*d1/d2
    return out
R1=rich(L,range(5,N//2)); A1=aitken(L,range(0,N-2)); A2=aitken(A1,range(0,max(A1)-2))
print("  n | -log(I''_{n+1}/I''_n) |  Richardson(n,2n) |  Aitken^1  |  Aitken^2")
for n in [5,10,15,20,25,30,33,34]:
    f=lambda d: (mp.nstr(d[n],12) if n in d else '-')
    print(f"  {n:3d} |   {f(L):>18} | {f(R1):>16} | {f(A1):>12} | {f(A2):>12}")
print("\n  target: -log(0.0939374) =", mp.nstr(-mlog(mpf('0.0939374')),12))
