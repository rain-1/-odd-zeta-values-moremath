"""d5(b,c) = max(0, -v_p(w5(a,b,c))) for the saved 130-term w5, at level a<p.
Check the depth bound  d5 <= 1 + min(vT, 2),  vT = v_p(T(a,b,c)).
Also recompute d3 for w3hat as a control."""
import json, sys
from fractions import Fraction as F
from math import comb
from core import Hs, vp, w3hat

d = json.load(open('w5_solution_abcn.json'))
terms = []
for lab, (num, den) in d.items():
    fg, rest = lab.split(']x'); f, g = fg[1:].split('|'); h, s = rest.split('x')
    sp = lambda x: [] if x == '1' else x.split('*')
    terms.append((F(num, den), sp(f), sp(g), sp(h), sp(s)))

def w5(n, k, l):
    def L(nm, idx):
        t, r = nm[0], int(nm[1])
        return (Hs(n+idx,r)-Hs(idx,r)) if t == 'A' else (Hs(n-idx,r)-Hs(idx,r))
    tot = F(0)
    for cf, f, g, h, s in terms:
        v = cf
        for nm in h: v *= Hs(n+k+l,int(nm[1])) - Hs(k+l,int(nm[1]))
        for nm in s: v *= Hs(n,int(nm[1]))
        pf = F(1)
        for nm in f: pf *= L(nm, k)
        for nm in g: pf *= L(nm, l)
        pb = F(1)
        for nm in f: pb *= L(nm, l)
        for nm in g: pb *= L(nm, k)
        tot += v * (pf if f == g else pf + pb)
    return tot

def Tl(a,b,c):
    return comb(a+b,a)*comb(a,b)**2*comb(a+c,a)*comb(a,c)**2*comb(a+b+c,a)

for p in [int(x) for x in sys.argv[1:]] or [5,7,11,13]:
    bad5 = bad3 = 0; mx5 = mx3 = 0; slack5 = 99; slack3 = 99
    for a in range(1, p):
        for b in range(a+1):
            for c in range(a+1):
                vT = vp(Tl(a,b,c), p)
                cap = 1 + min(vT, 2)
                W5 = w5(a,b,c) - Hs(a,5)      # drop the constant letter (the H-layer)
                W3 = w3hat(a,b,c) - Hs(a,3)
                d5 = max(0, -vp(W5,p)) if W5 else 0
                d3 = max(0, -vp(W3,p)) if W3 else 0
                mx5 = max(mx5,d5); mx3 = max(mx3,d3)
                slack5 = min(slack5, cap-d5); slack3 = min(slack3, cap-d3)
                if d5 > cap: bad5 += 1
                if d3 > cap: bad3 += 1
    print('p=%2d  max d5=%d  violations(d5>1+min(vT,2))=%d  min slack=%d   |  max d3=%d viol=%d min slack=%d'
          % (p, mx5, bad5, slack5, mx3, bad3, slack3), flush=True)
