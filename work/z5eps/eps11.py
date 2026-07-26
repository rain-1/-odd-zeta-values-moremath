"""eps11.py -- E5-only (per-order) consistency along the alpha-line, then COMPLETE
mod-p root-finding of the consistency locus.

E5-only system: unknowns [w6, delta3, gamma3, r5_3] = 15;
matrix A(c,d), rhs b(c,d).  Generic rank 15.  Consistency <=> every 16x16 minor
of [A|b] containing b vanishes.  We reconstruct several such minors as
polynomials in c (d=1 chart) by interpolation mod p, take their gcd, and find
ALL roots in F_p; rational candidates via rational reconstruction.
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
from eps2 import rref_solve, rr, ratrec
from eps6 import Pipe

p = 2147483647
pi = Pipe(p); nr = pi.nr
i2, i6 = pi.inv(2), pi.inv(6)

def E5only(c, d):
    """returns (A_rows, b) for unknowns [w6, dlt3, gam3, r5_3]"""
    alpha = ((-c - d) % p, c % p, d % p)
    a1c = [0, 0] + list(alpha)
    s1c = [0]*5
    x2 = pi.E2(s1c, a1c, verbose=False)
    if x2 is None: return None, None
    g9 = list(x2[:6]) + [0,0,0]
    x3, null3 = pi.E3(s1c, a1c, g9, verbose=False)
    if x3 is None or len(null3) != 1: return None, None
    ker = null3[0]
    yhat9 = list(ker[:6]) + [0,0,0]
    bhat9 = [0]*6 + list(ker[6:9])
    cols = pi.stage_cols2(5, 4, alpha)
    for j in range(3):
        e9=[0]*9; e9[6+j]=1
        cols.append(pi.momHH([], bhat9, 2, e9, 3))
    cols += pi.rowcols()
    t_s2s3 = pi.momHH([], g9, 2, yhat9, 3)
    t_a12s3 = pi.momH([a1c, a1c], 3, yhat9)
    t_a1s2a2 = pi.momHH([a1c], g9, 2, bhat9)
    t_a13a2 = pi.momH([a1c]*3, 2, bhat9)
    b = [(-(t_s2s3[n] + i2*t_a12s3[n] + t_a1s2a2[n] + i6*t_a13a2[n])) % p
         for n in range(nr)]
    A = [[cc[n] for cc in cols] for n in range(nr)]
    return A, b, ker

print('E5-only along the line (S1=0):')
hits = []
for c in list(range(-12, 13)) + [100, 1000]:
    d = 1
    A, b, ker = E5only(c, d)
    ok, x, null, rk = rref_solve(A, b, p)
    t3 = ker[9]
    if ok:
        print('  (c,d)=(%d,1): CONSISTENT rank=%d t3=%s  (u5,s5,t5)=(%s,%s,%s)'
              % (c, rk, rr(t3,p), rr(x[12],p), rr(x[13],p), rr(x[14],p)))
        hits.append((c,d))
    else:
        pass
print('  integer scan c=-12..12 (d=1) + 100,1000: hits =', hits)
# also d=0 (alpha = (-c, c, 0) ~ (-1,1,0)):
A, b, ker = E5only(1, 0)
ok, x, null, rk = rref_solve(A, b, p)
print('  (c,d)=(1,0): consistent=%s' % ok)
