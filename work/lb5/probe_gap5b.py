"""DECISIVE (GAP-5) test: cell-by-cell, is  v_p(Tcal(b,c) - Lambda T(a,b,c)) >= 1 + d5(b,c) ?
(That is what the weight-5 ledger needs termwise; Lemma F's UNIFORM bound 2+min(vT,2) may be
beaten at the deep cells.)  Also reports the aggregate (W5-MID) residue."""
import json, sys
from fractions import Fraction as F
from math import comb
from core import Hs, vp, Q
from t2_lemFplus import fibre_table, Tlevel, vp_mod, CAP

FN = sys.argv[1]
d = json.load(open(FN))
terms = []
for lab,(num,den) in d.items():
    fg, rest = lab.split(']x'); f,g = fg[1:].split('|'); h,s = rest.split('x')
    sp = lambda x: [] if x=='1' else x.split('*')
    terms.append((F(num,den), sp(f), sp(g), sp(h), sp(s)))

def w5(n,k,l):
    def L(nm,i):
        t,r = nm[0], int(nm[1])
        return (Hs(n+i,r)-Hs(i,r)) if t=='A' else (Hs(n-i,r)-Hs(i,r))
    tot=F(0)
    for cf,f,g,h,s in terms:
        v=cf
        for nm in h: v*= Hs(n+k+l,int(nm[1]))-Hs(k+l,int(nm[1]))
        for nm in s: v*= Hs(n,int(nm[1]))
        pf=F(1); pb=F(1)
        for nm in f: pf*=L(nm,k)
        for nm in g: pf*=L(nm,l)
        for nm in f: pb*=L(nm,l)
        for nm in g: pb*=L(nm,k)
        tot += v*(pf if f==g else pf+pb)
    return tot

for p in [int(x) for x in sys.argv[2:]] or [5,7,11,13]:
    M = p**CAP
    ncell=0; nbad=0; worst=None; midbad=0; midn=0
    for a in range(1,p):
        Qa = int(Q(a))
        if Qa % p == 0: continue
        Ta = {(b,c): Tlevel(a,b,c) for b in range(a+1) for c in range(a+1)}
        V5 = {}
        for b in range(a+1):
            for c in range(a+1):
                V5[(b,c)] = w5(a,b,c) - Hs(a,5)
        d5 = {bc: (max(0,-vp(V5[bc],p)) if V5[bc] else 0) for bc in V5}
        for r in range(p):
            n = a*p+r
            if n > 360: continue
            tab = fibre_table(p,a,r,M)
            Qn = sum(tab.values()) % M
            Lam = Qn * pow(Qa % M, -1, M) % M
            Qr = int(Q(r))
            mid = F(0)
            for bc,val in tab.items():
                ncell += 1
                diff = (val - Lam*Ta[bc]) % M
                v = vp_mod(diff,p)
                if v < 1 + d5[bc]:
                    nbad += 1
                    sl = v - (1+d5[bc])
                    if worst is None or sl < worst[0]: worst=(sl,a,r,bc,d5[bc],v)
                # aggregate (W5-MID) term:  v5(a,b,c) * (Tcal - Qr*T(a,b,c))
                dq = (val - Qr*Ta[bc]) % M
                mid += V5[bc]*F(dq if dq < M//2 else dq-M)
            midn += 1
            num,den = mid.numerator, mid.denominator
            if den % p == 0 or (num % p != 0 if den % p else True):
                pass
            if vp(mid,p) < 1 if mid else False:
                midbad += 1
    print('p=%2d  cells=%5d  cells FAILING v_p(diff)>=1+d5: %d  worst(slack,a,r,bc,d5,v)=%s'
          % (p, ncell, nbad, worst), flush=True)
