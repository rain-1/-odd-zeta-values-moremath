"""WEIGHT-5 CALIBRATION: does the campaign's sector logic give the KNOWN-CORRECT answer
on the BZ M_{0,8} zeta(5) family, where we have 361 EXACT ladder terms?"""
import json
from fractions import Fraction as F
from mpmath import mp, mpf, zeta, log as mlog, polyroots
mp.dps=400
W='/home/ubuntu/fable-episode-2/zeta-math/worthiness/falsify_data/'
d={k:json.load(open(W+'ladder_%s.json'%k)) for k in ('Q','P','Ph')}
def g(k,n):
    v=d[k][str(n)]
    return F(int(v[0]),int(v[1])) if isinstance(v,(list,tuple)) else F(str(v))
N=360
print("first terms: Q",[str(g('Q',n)) for n in range(4)])
print("             P",[str(g('P',n)) for n in range(4)])
print("             Ph",[str(g('Ph',n)) for n in range(4)])
rts=sorted([mp.re(x) for x in polyroots([4,-2368,-188,1],maxsteps=300,extraprec=300)],key=abs)
print("\nzeta(5) char roots (4L^3-2368L^2-188L+1):",[mp.nstr(x,10) for x in rts])
print("  -log|root| :",[mp.nstr(-mlog(abs(x)),10) for x in rts])
z2,z3,z5=zeta(2),zeta(3),zeta(5)
def F2mp(x): return mpf(x.numerator)/mpf(x.denominator)
# candidate primitive / companion forms
forms={
 'Q*z5 - P      ':lambda n: F2mp(g('Q',n))*z5-F2mp(g('P',n)),
 'Q*z3 - Ph     ':lambda n: F2mp(g('Q',n))*z3-F2mp(g('Ph',n)),
}
print("\n n    log|Q_n|/n     rate(Q z5 - P)    rate(Q z3 - Ph)")
prev={}
for n in [20,40,80,120,160,200,240,280,320,355]:
    row=f"{n:4d}  {mp.nstr(mlog(F2mp(g('Q',n)))/n,10):>12}"
    for k,f in forms.items():
        v=f(n); row+=f"   {mp.nstr(mlog(abs(v))/n,10):>15}"
    print(row)
print("\n=== ratio-based (decisive): -log|X_{n+1}/X_n| with Richardson ===")
for k,f in forms.items():
    Lg={n:-mlog(abs(f(n+1)/f(n))) for n in range(2,N)}
    R1=lambda n:2*Lg[2*n]-Lg[n]
    print(f"  {k}: raw(n=350)={mp.nstr(Lg[350],10)}  Rich1(100,200)={mp.nstr(R1(100),10)}  Rich1(175,350)={mp.nstr(R1(175),10)}")
    print(f"      signs: {'ALTERNATING' if all((f(n)>0)!=(f(n+1)>0) for n in range(5,20)) else 'constant/other'}")
