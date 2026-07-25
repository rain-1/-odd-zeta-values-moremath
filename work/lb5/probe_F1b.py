"""Stratified probe of (F1)/(F2) by the carry pattern (e1,e2,e3,e4,h1,h2).
   e1=[r+s>=p] e2=[r+t>=p] e3=floor((r+s+t)/p) e4=[s+t>=p] h1=[s>r] h2=[t>r]
Target precision: 2 + min(vT,2).   Reports min slack per stratum.
"""
import sys
from fractions import Fraction as F
from collections import defaultdict
from core import Hs, T, vp

def phis(r, s, t):
    Pb = Hs(r+s,1) + Hs(r+s+t,1) - 3*Hs(s,1) + 2*Hs(r-s,1) - Hs(s+t,1)
    Pc = Hs(r+t,1) + Hs(r+s+t,1) - 3*Hs(t,1) + 2*Hs(r-t,1) - Hs(s+t,1)
    Pa = (Hs(r+s,1) + Hs(r+t,1) + Hs(r+s+t,1) + Hs(r,1)
          - 2*Hs(r-s,1) - 2*Hs(r-t,1))
    return Pa, Pb, Pc

def run(p):
    st = defaultdict(lambda: [99, 0])
    for a in range(1, p):
        for b in range(a+1):
            for c in range(a+1):
                Tabc = T(a,b,c)
                if Tabc == 0: continue
                vT = vp(Tabc, p)
                tgt = 2 + min(vT, 2)
                for r in range(p):
                    n = a*p + r
                    for s in range(p):
                        for t in range(p):
                            k, l = b*p+s, c*p+t
                            Tn = T(n,k,l) if (k <= n and l <= n) else 0
                            Trst = T(r,s,t) if (s <= r and t <= r) else 0
                            if Trst:
                                Pa,Pb,Pc = phis(r,s,t)
                                pred = Tabc*Trst*(1 + p*(a*Pa + b*Pb + c*Pc))
                            else:
                                pred = F(0)
                            D = F(Tn) - pred
                            v = vp(D,p) if D != 0 else 99
                            key = (int(s>r), int(t>r), int(r+s>=p), int(r+t>=p),
                                   (r+s+t)//p, int(s+t>=p))
                            e = st[key]
                            e[0] = min(e[0], v - tgt); e[1] += 1
    return st

for p in [int(x) for x in sys.argv[1:]] or [5,7]:
    st = run(p)
    print('p=%d  key=(h1,h2,e1,e2,e3,e4) -> [min slack, count]' % p)
    for k in sorted(st):
        print('   ', k, st[k])
    print(flush=True)
