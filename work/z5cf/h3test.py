"""(H3) digit compatibility on the TRUE surviving set  { (k,l) : p does not divide T(n,k,l) }."""
import sys, os
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import T

ARG = {'n': lambda n, k, l: n, 'k': lambda n, k, l: k, 'l': lambda n, k, l: l,
       'n+k': lambda n, k, l: n + k, 'n+l': lambda n, k, l: n + l,
       'n-k': lambda n, k, l: n - k, 'n-l': lambda n, k, l: n - l,
       'k+l': lambda n, k, l: k + l, 'n+k+l': lambda n, k, l: n + k + l}

print('(H3)  floor(x(n,k,l)/p) == x(a,b,c)  for every cell with p | T(n,k,l) FALSE')
print('  n = ap+r, k = bp+s, l = cp+t,  1 <= a < p,  0 <= r,s,t < p')
for p in (5, 7, 11, 13):
    bad = {}
    tot = 0
    surv_cond = 0
    for a in range(1, p):
        for r in range(p):
            n = a * p + r
            for k in range(n + 1):
                for l in range(n + 1):
                    if T(n, k, l) % p == 0:
                        continue
                    tot += 1
                    b, s = divmod(k, p)
                    c, t = divmod(l, p)
                    if r + s + t < p:
                        surv_cond += 1
                    for nm, f in ARG.items():
                        if f(n, k, l) // p != f(a, b, c):
                            bad[nm] = bad.get(nm, 0) + 1
    print('  p=%-3d surviving cells=%-8d (of which r+s+t<p: %d)  violations: %s'
          % (p, tot, surv_cond, bad if bad else 'NONE for any of the nine arguments'))
