"""Standalone exact verification of the saved w5 against the BZ ladder.
Reads w5_canon.json (labels '[f|g]xhxs') and rebuilds everything from scratch."""
import json, sys
from fractions import Fraction as F
from math import comb
from core import P, Hs

d = json.load(open('w5_canon.json'))
terms = []
for lab, (num, den) in d.items():
    fg, rest = lab.split(']x'); f, g = fg[1:].split('|'); h, s = rest.split('x')
    sp = lambda x: [] if x == '1' else x.split('*')
    terms.append((F(num, den), sp(f), sp(g), sp(h), sp(s)))
print('loaded %d terms' % len(terms))

def run(n):
    A = {r: [Hs(n+k, r) - Hs(k, r) for k in range(n+1)] for r in range(1, 6)}
    B = {r: [Hs(n-k, r) - Hs(k, r) for k in range(n+1)] for r in range(1, 6)}
    C = {r: [Hs(n+m, r) - Hs(m, r) for m in range(2*n+1)] for r in range(1, 6)}
    N = {r: Hs(n, r) for r in range(1, 6)}
    def L(nm, idx):
        t, r = nm[0], int(nm[1])
        return A[r][idx] if t == 'A' else B[r][idx]
    tot = F(0)
    for k in range(n+1):
        tk = comb(n+k, n) * comb(n, k)**2
        for l in range(n+1):
            T = tk * comb(n+l, n) * comb(n, l)**2 * comb(n+k+l, n)
            w = F(0)
            for cf, f, g, h, s in terms:
                v = cf
                for nm in h: v *= C[int(nm[1])][k+l]
                for nm in s: v *= N[int(nm[1])]
                pf = F(1)
                for nm in f: pf *= L(nm, k)
                for nm in g: pf *= L(nm, l)
                pb = F(1)
                for nm in f: pb *= L(nm, l)
                for nm in g: pb *= L(nm, k)
                w += v * (pf if f == g else pf + pb)
            tot += T * w
    return tot

for n in [int(x) for x in sys.argv[1:]]:
    got = run(n); want = P(n)
    print('n=%2d  %s' % (n, 'OK' if got == want else 'MISMATCH diff=%s' % (got - want)), flush=True)
