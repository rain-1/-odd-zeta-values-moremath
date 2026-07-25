"""Verify (F1): for s,t <= r,
     T(n,bp+s,cp+t)  ==  T(a,b,c) * T(r,s,t) * (1 + p*(a*Phi_a + b*Phi_b + c*Phi_c))
   modulo p^{2+vT}, vT = v_p(T(a,b,c));   and (F2): for s>r or t>r,
     v_p(T(n,bp+s,cp+t)) >= 2 + min(vT,2).
All exact rational arithmetic (Fractions), p small.
"""
import sys
from fractions import Fraction as F
from core import Hs, T, vp

def phis(r, s, t):
    Pb = Hs(r+s,1) + Hs(r+s+t,1) - 3*Hs(s,1) + 2*Hs(r-s,1) - Hs(s+t,1)
    Pc = Hs(r+t,1) + Hs(r+s+t,1) - 3*Hs(t,1) + 2*Hs(r-t,1) - Hs(s+t,1)
    Pa = (Hs(r+s,1) + Hs(r+t,1) + Hs(r+s+t,1) + Hs(r,1)
          - 2*Hs(r-s,1) - 2*Hs(r-t,1))
    return Pa, Pb, Pc

def run(p):
    minF1 = 99; minF2 = 99; nF1 = nF2 = 0
    worstF1 = worstF2 = None
    for a in range(1, p):
        for b in range(a+1):
            for c in range(a+1):
                Tabc = T(a,b,c)
                vT = vp(Tabc, p) if Tabc else 99
                if Tabc == 0: continue
                for r in range(p):
                    n = a*p + r
                    for s in range(p):
                        for t in range(p):
                            k, l = b*p+s, c*p+t
                            if k > n or l > n:
                                Tn = 0
                            else:
                                Tn = T(n,k,l)
                            if s <= r and t <= r:
                                Trst = T(r,s,t)
                                Pa,Pb,Pc = phis(r,s,t)
                                pred = Tabc*Trst*(1 + p*(a*Pa + b*Pb + c*Pc))
                                D = F(Tn) - pred
                                v = vp(D,p) if D != 0 else 99
                                sl = v - (2+vT)
                                if sl < minF1:
                                    minF1 = sl; worstF1=(a,b,c,r,s,t,vT,v)
                                if sl < 0: nF1 += 1
                            else:
                                v = vp(Tn,p) if Tn != 0 else 99
                                sl = v - (2+min(vT,2))
                                if sl < minF2:
                                    minF2 = sl; worstF2=(a,b,c,r,s,t,vT,v)
                                if sl < 0: nF2 += 1
    return minF1,nF1,worstF1,minF2,nF2,worstF2

for p in [int(x) for x in sys.argv[1:]] or [5,7]:
    m1,n1,w1,m2,n2,w2 = run(p)
    print('p=%d  F1: min slack=%d failures=%d worst(a,b,c,r,s,t,vT,v)=%s' % (p,m1,n1,w1))
    print('      F2: min slack=%d failures=%d worst(a,b,c,r,s,t,vT,v)=%s' % (m2,n2,w2), flush=True)
