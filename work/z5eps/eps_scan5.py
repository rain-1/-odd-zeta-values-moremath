import sys
from math import gcd
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
from eps2 import rref_solve, rr
from eps13 import E5ext, pi, p
H = 5
hits = []
tried = 0
for a in range(-H, H+1):
    for b in range(-H, H+1):
        for c in range(-H, H+1):
            for d in range(0, H+1):
                if (c, d) == (0, 0): continue
                if d == 0 and c != 1: continue
                gg = gcd(gcd(abs(a), abs(b)), gcd(abs(c), abs(d)))
                if gg > 1: continue
                for tval in (1, 2):
                    tried += 1
                    R = E5ext(a, b, c, d, tval)
                    if R is None: continue
                    if R[0] == 'OK' and any(v % p for v in R[2:5]):
                        hits.append((a, b, c, d, tval) + R[1:])
print('tried %d; NONTRIVIAL hits (some row coeff != 0): %d' % (tried, len(hits)))
for h in hits:
    a, b, c, d, tval, t3, u5, s5, t5 = h[:9]
    print('  (a,b,c,d;t)=(%d,%d,%d,%d;%d) t3=%s (u5,s5,t5)=(%s,%s,%s)'
          % (a, b, c, d, tval, rr(t3,p), rr(u5,p), rr(s5,p), rr(t5,p)))
