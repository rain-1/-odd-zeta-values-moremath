"""Quantify (GAP-5): per-vT max depth d5 vs the precision Lemma F supplies (2+min(vT,2))."""
import json, sys
from fractions import Fraction as F
from math import comb
from core import Hs, vp, w3hat

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
        pf=F(1)
        for nm in f: pf*=L(nm,k)
        for nm in g: pf*=L(nm,l)
        pb=F(1)
        for nm in f: pb*=L(nm,l)
        for nm in g: pb*=L(nm,k)
        tot += v*(pf if f==g else pf+pb)
    return tot

def Tl(a,b,c): return comb(a+b,a)*comb(a,b)**2*comb(a+c,a)*comb(a,c)**2*comb(a+b+c,a)

print('file =', FN)
for p in [int(x) for x in sys.argv[2:]] or [5,7,13]:
    mx = {}
    for a in range(1,p):
        for b in range(a+1):
            for c in range(a+1):
                vT = vp(Tl(a,b,c),p)
                W = w5(a,b,c)-Hs(a,5)
                d5 = max(0,-vp(W,p)) if W else 0
                mx[vT] = max(mx.get(vT,0), d5)
    print(' p=%2d' % p, ' | '.join('vT=%d: max d5=%d, LemmaF gives p^%d, need p^%d, SHORT BY %d'
          % (v, mx[v], 2+min(v,2), 1+mx[v], max(0, 1+mx[v]-(2+min(v,2)))) for v in sorted(mx)), flush=True)
