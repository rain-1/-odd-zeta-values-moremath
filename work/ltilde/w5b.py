import json, math
from fractions import Fraction as F
from math import gcd
from mpmath import mp, mpf, zeta, log as mlog, polyroots
W='/home/ubuntu/fable-episode-2/zeta-math/worthiness/falsify_data/'
d={k:json.load(open(W+'ladder_%s.json'%k)) for k in ('Q','P','Ph')}
def g(k,n):
    v=d[k][str(n)]
    return F(int(v[0]),int(v[1])) if isinstance(v,(list,tuple)) else F(str(v))
N=360
def dlcm(n):
    L=1
    for i in range(1,n+1): L=L*i//gcd(L,i)
    return L
print("=== W5 TRUE kappa: den(P_n), den(Ph_n) vs d_n^5  (361 EXACT terms) ===")
print("  n   log den(P)/n  log den(Ph)/n  log(d_n^5)/n   P|d^5?  Ph|d^5?  ratio P/d^5")
for n in [40,80,120,160,200,240,280,320,355]:
    dP=g('P',n).denominator; dH=g('Ph',n).denominator; D=dlcm(n); D5=D**5
    print(f"  {n:3d}   {math.log(dP)/n:11.5f}  {math.log(dH)/n:12.5f}  {5*math.log(D)/n:12.5f}"
          f"    {'Y' if D5%dP==0 else 'N'}       {'Y' if D5%dH==0 else 'N'}     {math.log(dP)/(5*math.log(D)):9.4f}")
print("\n=== W5 RATES (precision scaled with n) ===")
rts=sorted([mp.re(x) for x in polyroots([4,-2368,-188,1],maxsteps=400,extraprec=400)],key=abs)
def F2(x): return mpf(x.numerator)/mpf(x.denominator)
def rate(kind,n):
    mp.dps=int(4.0*n)+120
    z2,z3,z5=zeta(2),zeta(3),zeta(5)
    Q,P,Ph=F2(g('Q',n)),F2(g('P',n)),F2(g('Ph',n))
    return {'prim':Q*z5-P,'comp':Q*z3-Ph,'full':(Q*z5-P)+z2*(Q*z3-Ph),'full-':(Q*z5-P)-z2*(Q*z3-Ph)}[kind]
print("  n |  -log|X_{n+1}/X_n|  for  prim=Qz5-P | comp=Qz3-Ph | prim+z2*comp | prim-z2*comp")
for n in [50,100,150,200,250,300,340]:
    row=f"  {n:3d} |"
    for k in ('prim','comp','full','full-'):
        a,b=rate(k,n),rate(k,n+1)
        mp.dps=60
        row+=f"  {mp.nstr(-mlog(abs(b/a)),10):>14}"
    print(row)
mp.dps=30
print("\n  -log|roots| :  small 0.0050038 -> %s   middle -0.0843843 -> %s   large 592.079 -> %s"%
      tuple(mp.nstr(-mlog(abs(x)),10) for x in rts))
print("  gamma.py's recorded C0 (symmetric point) = -2.47237372   -> matches MIDDLE root")
print("  zeta(5) threshold e^-5 = %s ; small root %s < threshold => small root WOULD PASS"%
      (mp.nstr(mp.e**-5,8), mp.nstr(rts[0],8)))
