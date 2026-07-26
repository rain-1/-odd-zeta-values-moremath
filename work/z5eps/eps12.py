"""eps12.py -- mixed branch: S1 = a*X + b*Y != 0, A1 = alpha on the E2-line.
E3 is inhomogeneous; scan (a,b,c,d) for E3-consistency, then E5-only at hits.
Parameters projective; scan primitive tuples.
"""
import sys
from math import gcd
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
from eps2 import rref_solve, rr
from eps6 import Pipe

p = 2147483647
pi = Pipe(p); nr = pi.nr
i2, i6 = pi.inv(2), pi.inv(6)

def E3test(a, b, c, d):
    alpha = ((-c - d) % p, c % p, d % p)
    a1c = [0, 0] + list(alpha)
    s1c = [a % p, b % p, 0, 0, 0]
    x2 = pi.E2(s1c, a1c, verbose=False)
    if x2 is None: return None
    g9 = list(x2[:6]) + [0,0,0]
    x3, null3 = pi.E3(s1c, a1c, g9, verbose=False)
    if x3 is None: return None
    return x2, x3, null3

H = 5
cands = []
tried = 0
for a in range(-H, H+1):
    for b in range(-H, H+1):
        if (a, b) == (0, 0): continue
        for c in range(-H, H+1):
            for d in range(0, H+1):
                if (c, d) == (0, 0): continue
                if d == 0 and c != 1: continue
                if gcd(gcd(abs(a), abs(b)), gcd(abs(c), abs(d))) > 1: continue
                tried += 1
                R = E3test(a, b, c, d)
                if R is not None:
                    x2, x3, null3 = R
                    t3, s3, v3 = x3[9], x3[10], x3[11]
                    cands.append((a, b, c, d, t3, s3, v3, len(null3)))
print('scanned %d points; E3-consistent: %d' % (tried, len(cands)))
for (a,b,c,d,t3,s3,v3,nd) in cands[:40]:
    print('  (a,b,c,d)=(%d,%d,%d,%d)  (t3,s3,v3)=(%s,%s,%s) null=%d'
          % (a,b,c,d, rr(t3,p), rr(s3,p), rr(v3,p), nd))
