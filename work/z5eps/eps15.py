"""eps15.py -- consolidation at the special point (-1,0,1,2):
 (a) E5-only: null touches rows?  ->  uniqueness of (u5,s5,t5)
 (b) E4-only consistency (z,gamma free)   [expect FAIL]
 (c) full rational data at t=1: E5 particular solution (w,dlt,gam,z)
 (d) e_m letter tables and totals; zeta bookkeeping
 (e) t5(t) fit check at t=5,10
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
from eps2 import rref_solve, rr
from eps6 import Pipe
from eps13 import E5ext
from fractions import Fraction as F

p = 2147483647
pi = Pipe(p); nr = pi.nr
i2, i6, i24 = pi.inv(2), pi.inv(6), pi.inv(24)
a, b, c, d = -1, 0, 1, 2
alpha = ((-c-d) % p, c % p, d % p)
a1c = [0,0] + list(alpha)
s1c = [a % p, b % p, 0, 0, 0]

x2 = pi.E2(s1c, a1c, verbose=False)
g9 = list(x2[:6]) + [0,0,0]
x3, null3 = pi.E3(s1c, a1c, g9, verbose=False)
ker = null3[0]
print('E3 particular: y_p =', [rr(v,p) for v in x3[:6]], ' beta_p =', [rr(v,p) for v in x3[6:9]],
      ' (t3,s3,v3)_p =', [rr(v,p) for v in x3[9:12]])
print('E3 kernel    : y_k =', [rr(v,p) for v in ker[:6]], ' beta_k =', [rr(v,p) for v in ker[6:9]],
      ' (t3,s3,v3)_k =', [rr(v,p) for v in ker[9:12]])

# (e) t5 fit
for tval in (5, 10):
    R = E5ext(a, b, c, d, tval)
    print('t=%2d: %s t3=%s (u5,s5,t5)=(%s,%s,%s)   [fit t^2/4+8t = %s]'
          % (tval, R[0], rr(R[1],p), rr(R[2],p), rr(R[3],p), rr(R[4],p),
             F(tval,1)**2/4 + 8*tval))

# (a) E5-only at t=1 with null inspection -- rebuild the system as in eps13
def E5sys(tval):
    y = [(x3[i] + tval*ker[i]) % p for i in range(6)]
    bt = [(x3[6+i] + tval*ker[6+i]) % p for i in range(3)]
    y9 = y + [0,0,0]; b9 = [0]*6 + bt
    cols = pi.stage_cols2(5, 4, alpha)
    for j in range(3):
        e9=[0]*9; e9[6+j]=1
        c1 = pi.momHH([], b9, 2, e9, 3)
        c2 = pi.momH([s1c, a1c], 3, e9)
        cols.append([(c1[n]+c2[n])%p for n in range(nr)])
    for cix in range(6):
        e9=[0]*9; e9[cix]=1
        cols.append(pi.momH([s1c], 4, e9))
    cols += pi.rowcols()
    i120 = pi.inv(120)
    t_s2s3 = pi.momHH([], g9, 2, y9, 3)
    t_s12s3 = pi.momH([s1c,s1c], 3, y9)
    t_a12s3 = pi.momH([a1c,a1c], 3, y9)
    t_s1s2s2 = pi.momHH([s1c], g9, 2, g9)
    t_s1a2a2 = pi.momHH([s1c], b9, 2, b9)
    t_a1s2a2 = pi.momHH([a1c], g9, 2, b9)
    t_s13s2 = pi.momH([s1c]*3, 2, g9)
    t_s1a12s2 = pi.momH([s1c,a1c,a1c], 2, g9)
    t_s12a1a2 = pi.momH([s1c,s1c,a1c], 2, b9)
    t_a13a2 = pi.momH([a1c]*3, 2, b9)
    t_s15 = pi.mom([s1c]*5)
    t_s13a12 = pi.mom([s1c]*3+[a1c]*2)
    t_s1a14 = pi.mom([s1c]+[a1c]*4)
    rhs = [(-(t_s2s3[n] + i2*(t_s12s3[n]+t_a12s3[n])
              + i2*(t_s1s2s2[n]+t_s1a2a2[n]) + t_a1s2a2[n]
              + i6*(t_s13s2[n]+3*t_s1a12s2[n]+3*t_s12a1a2[n]+t_a13a2[n])
              + i120*(t_s15[n]+10*t_s13a12[n]+5*t_s1a14[n]))) % p
           for n in range(nr)]
    A = [[cc[n] for cc in cols] for n in range(nr)]
    return A, rhs

A, rhs = E5sys(1)
ok, x, null, rk = rref_solve(A, rhs, p)
print()
print('(a) E5-only t=1: ok=%s rank=%d/21 null=%d' % (ok, rk, len(null)))
touch = [any(v[i] % p for i in (18,19,20)) for v in null]
print('    null vectors touching rows (u5,s5,t5):', touch)
print('    solution: w =', [rr(v,p) for v in x[:6]])
print('              delta =', [rr(v,p) for v in x[6:9]])
print('              gamma =', [rr(v,p) for v in x[9:12]])
print('              z =', [rr(v,p) for v in x[12:18]])
print('              (u5,s5,t5) =', [rr(v,p) for v in x[18:21]])

# (b) E4-only with z,gamma free
y9 = [(x3[i] + ker[i]) % p for i in range(6)] + [0,0,0]
b9 = [0]*6 + [(x3[6+i] + ker[6+i]) % p for i in range(3)]
cols4 = pi.stage_cols2(4, 3, alpha) + pi.rowcols()
t_s1s3 = pi.momH([s1c], 3, y9)
t_s2s2 = pi.momHH([], g9, 2, g9)
t_a2a2 = pi.momHH([], b9, 2, b9)
t_s12s2 = pi.momH([s1c,s1c], 2, g9)
t_a12s2 = pi.momH([a1c,a1c], 2, g9)
t_s1a1a2 = pi.momH([s1c,a1c], 2, b9)
t_s14 = pi.mom([s1c]*4)
t_s12a12 = pi.mom([s1c,s1c,a1c,a1c])
t_a14 = pi.mom([a1c]*4)
rhs4 = [(-(t_s1s3[n] + i2*(t_s2s2[n]+t_a2a2[n]) + i2*(t_s12s2[n]+t_a12s2[n])
          + t_s1a1a2[n] + i24*(t_s14[n]+6*t_s12a12[n]+t_a14[n]))) % p
        for n in range(nr)]
ok4, x4, null4, rk4 = rref_solve([[cc[n] for cc in cols4] for n in range(nr)], rhs4, p)
print()
print('(b) E4-only t=1 (z,gamma free): ok=%s rank=%d/12' % (ok4, rk4))

# (d) e_m totals: multiplicities (n:1, k:2, n+k:2, n-k:2, k+l:1, n+k+l:1)
mult = [1,2,2,2,1,1]
# e2 = -2g (class); antisym parts cancel in totals
e2tot = (-2) * sum(F(rr_int) * m for rr_int, m in zip([-4,1,-3,4,2,-2], mult))
print()
print('(d) e2_total =', e2tot)
