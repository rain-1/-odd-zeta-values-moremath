"""eps13.py -- E5-only extended test on the mixed branch.

Unknowns [w6, delta3, gamma3, z6, r5_3] = 21.
gamma-columns: SigmaT A2(t)*w3_j + SigmaT S1*A1*w3_j;  z-columns: SigmaT S1*h4[c].
RHS: all forced products of (S1, A1, S2=g, S3=y(t), A2=beta(t)).
Scan grid x t; report consistency and t5.
"""
import sys
from math import gcd
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
from eps2 import rref_solve, rr
from eps6 import Pipe

p = 2147483647
pi = Pipe(p); nr = pi.nr
i2, i6, i120 = pi.inv(2), pi.inv(6), pi.inv(120)

def E5ext(a, b, c, d, tval):
    alpha = ((-c - d) % p, c % p, d % p)
    a1c = [0, 0] + list(alpha)
    s1c = [a % p, b % p, 0, 0, 0]
    x2 = pi.E2(s1c, a1c, verbose=False)
    if x2 is None: return None
    g9 = list(x2[:6]) + [0, 0, 0]
    x3, null3 = pi.E3(s1c, a1c, g9, verbose=False)
    if x3 is None: return None
    ker = null3[0] if null3 else [0]*12
    y = [(x3[i] + tval*ker[i]) % p for i in range(6)]
    bt = [(x3[6+i] + tval*ker[6+i]) % p for i in range(3)]
    t3 = (x3[9] + tval*ker[9]) % p
    y9 = y + [0, 0, 0]
    b9 = [0]*6 + bt

    cols = pi.stage_cols2(5, 4, alpha)               # w6 + delta3
    for j in range(3):                               # gamma columns
        e9 = [0]*9; e9[6+j] = 1
        col1 = pi.momHH([], b9, 2, e9, 3)            # A2*w3_j
        col2 = pi.momH([s1c, a1c], 3, e9)            # S1*A1*w3_j
        cols.append([(col1[n] + col2[n]) % p for n in range(nr)])
    for cix in range(6):                             # z columns: S1*h4[c]
        e9 = [0]*9; e9[cix] = 1
        cols.append(pi.momH([s1c], 4, e9))
    cols += pi.rowcols()
    # forced RHS
    t_s2s3 = pi.momHH([], g9, 2, y9, 3)
    t_s12s3 = pi.momH([s1c, s1c], 3, y9)
    t_a12s3 = pi.momH([a1c, a1c], 3, y9)
    t_s1s2s2 = pi.momHH([s1c], g9, 2, g9)
    t_s1a2a2 = pi.momHH([s1c], b9, 2, b9)
    t_a1s2a2 = pi.momHH([a1c], g9, 2, b9)
    t_s13s2 = pi.momH([s1c]*3, 2, g9)
    t_s1a12s2 = pi.momH([s1c, a1c, a1c], 2, g9)
    t_s12a1a2 = pi.momH([s1c, s1c, a1c], 2, b9)
    t_a13a2 = pi.momH([a1c]*3, 2, b9)
    t_s15 = pi.mom([s1c]*5)
    t_s13a12 = pi.mom([s1c]*3 + [a1c]*2)
    t_s1a14 = pi.mom([s1c] + [a1c]*4)
    rhs = []
    for n in range(nr):
        v = (t_s2s3[n]
             + i2*(t_s12s3[n] + t_a12s3[n])
             + i2*(t_s1s2s2[n] + t_s1a2a2[n]) + t_a1s2a2[n]
             + i6*(t_s13s2[n] + 3*t_s1a12s2[n] + 3*t_s12a1a2[n] + t_a13a2[n])
             + i120*(t_s15[n] + 10*t_s13a12[n] + 5*t_s1a14[n]))
        rhs.append((-v) % p)
    A = [[cc[n] for cc in cols] for n in range(nr)]
    ok, x, null, rk = rref_solve(A, rhs, p)
    if not ok: return ('FAIL', t3)
    return ('OK', t3, x[18], x[19], x[20], rk, len(null))   # r5 = (u5,s5,t5)

H = 3
hits = []
tried = 0
tvals = (0, 1, -1, 2, 3)
import sys as _s
for a in range(-H, H+1):
    for b in range(-H, H+1):
        for c in range(-H, H+1):
            for d in range(0, H+1):
                if (c, d) == (0, 0): continue
                if d == 0 and c != 1: continue
                gg = gcd(gcd(abs(a), abs(b)), gcd(abs(c), abs(d)))
                if gg > 1: continue
                for tval in tvals:
                    if (a, b, tval) == (0, 0, 0): continue
                    tried += 1
                    R = E5ext(a, b, c, d, tval)
                    if R is None: continue
                    if R[0] == 'OK':
                        hits.append((a, b, c, d, tval) + R[1:])
print('tried %d (point,t) combos; E5-consistent hits: %d' % (tried, len(hits)))
for h in hits[:60]:
    a, b, c, d, tval, t3, u5, s5, t5 = h[:9]
    print('  (a,b,c,d;t)=(%d,%d,%d,%d;%d)  t3=%s  (u5,s5,t5)=(%s,%s,%s) rk=%d null=%d'
          % (a, b, c, d, tval, rr(t3, p), rr(u5, p), rr(s5, p), rr(t5, p), h[9], h[10]))
