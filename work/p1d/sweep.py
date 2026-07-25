"""Required verification:  ord_p(P_n) >= kappa - 5L  (kappa = v_p C(2n,n)) for p_n = C(2n,n)P_n,
   equivalently ord_p(P_n) >= -5L.   n <= 360 exact ladders; n <= 3000 via the certified recurrence."""
import sys
from fractions import Fraction as F
from math import comb
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import P, Q, Ph, vp, c0,c1,c2,c3

PRIMES=[5,7,11,13,17,19,23,29,31]
def L(n,p):
    e=0; q=n
    while q>=p: q//=p; e+=1
    return e

# ---- (S1) exact ladder sweep n<=360
bad=0; cells=0; worst=(99,None)
for p in PRIMES:
    for n in range(1,361):
        cells+=1
        m = vp(P(n),p)+5*L(n,p)
        if m<worst[0]: worst=(m,(p,n))
        if m<0: bad+=1; print('FAIL p=%d n=%d'%(p,n))
print('(S1) exact ladder n<=360, p in %s: cells=%d failures=%d  min(ord_p P_n + 5L)=%d at %s'%(PRIMES,cells,bad,worst[0],worst[1]))

# also in the (CB) form ord_p(p_n) >= kappa-5L with p_n = C(2n,n) P_n
bad2=0
for p in PRIMES:
    for n in range(1,361):
        kap=vp(comb(2*n,n),p)
        if vp(comb(2*n,n)*P(n),p) < kap-5*L(n,p): bad2+=1
print('(S1b) (CB) form  ord_p(p_n) >= kappa-5L : failures=%d'%bad2)

# ---- (S2) extend exactly to n=3000 by the certified order-3 recurrence, spot-check
import time
t0=time.time()
Pv={n:P(n) for n in (0,1,2)}
for n in range(0,3000):
    Pv[n+3]=-(c0(n)*Pv[n]+c1(n)*Pv[n+1]+c2(n)*Pv[n+2])/F(c3(n))
    if n%500==0: print('   extend n=%d  %.0fs'%(n,time.time()-t0),flush=True)
mis=sum(1 for n in range(0,361) if Pv[n]!=P(n))
print('(S2) recurrence extension cross-check against exact ladder n<=360: mismatches=%d'%mis)
bad3=0; cells3=0; worst3=(99,None)
STEP=1   # full sweep
for p in PRIMES:
    for n in range(1,3001,STEP):
        cells3+=1
        m=vp(Pv[n],p)+5*L(n,p)
        if m<worst3[0]: worst3=(m,(p,n))
        if m<0: bad3+=1; print('FAIL(3000) p=%d n=%d'%(p,n))
print('(S2) n<=3000 sweep: cells=%d failures=%d min(ord_p P_n+5L)=%d at %s'%(cells3,bad3,worst3[0],worst3[1]))
