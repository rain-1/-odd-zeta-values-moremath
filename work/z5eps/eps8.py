"""eps8.py -- pure-Psi branch, per-order tests with maximal freedom.

At S1=0, alpha = 2*Psi = (-3,1,2), g from E2, (y,beta) = t*ker (E3):
  [eps^4] = SigmaT( S4 + A1A3 + 1/2 S2^2 + 1/2 A2^2 + 1/2 A1^2 S2 + 1/24 A1^4 )
     unknowns z (S4), gamma (A3), rows; plus tau = t^2 column.   (already FAILED)
  [eps^5] = SigmaT( S5 + A1A4 + S2S3 + A2A3 + 1/2 A1^2 S3 + A1S2A2 + 1/6 A1^3 A2 )
     unknowns w (S5), delta (A4), gamma' = t*gamma (A2A3 columns), rows.
     RHS proportional to t -> normalise t = 1.
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
from eps2 import rref_solve, rr
from eps6 import Pipe

def run(p, alpha=(-3,1,2)):
    pi = Pipe(p)
    print('prime', p)
    s1c = [0]*5; a1c = [0,0]+list(alpha)
    x2 = pi.E2(s1c, a1c, verbose=False)
    g9 = list(x2[:6]) + [0,0,0]
    x3, null3 = pi.E3(s1c, a1c, g9, verbose=False)
    ker = null3[0]
    yhat9 = list(ker[:6]) + [0,0,0]
    bhat9 = [0]*6 + list(ker[6:9])
    i2, i6 = pi.inv(2), pi.inv(6)
    nr = pi.nr

    # E5 columns: M5sym(6) + A1w4 delta(3) + betahat.w2 x w3_j gamma'(3) + rows(3)
    cols = pi.stage_cols2(5, 4, alpha)          # 6 + 3
    for j in range(3):
        e9 = [0]*9; e9[6+j] = 1
        cols.append(pi.momHH([], bhat9, 2, e9, 3))   # SigmaT A2hat * w3_j
    cols += pi.rowcols()
    t_s2s3 = pi.momHH([], g9, 2, yhat9, 3)
    t_a12s3 = pi.momH([a1c, a1c], 3, yhat9)
    t_a1s2a2 = pi.momHH([a1c], g9, 2, bhat9)
    t_a13a2 = pi.momH([a1c]*3, 2, bhat9)
    rhs = [(-(t_s2s3[n] + i2*t_a12s3[n] + t_a1s2a2[n] + i6*t_a13a2[n])) % p
           for n in range(nr)]
    A = [[c[n] for c in cols] for n in range(nr)]
    ok, x, null, rk = rref_solve(A, rhs, p)
    print('E5 per-order (t=1): ok=%s rank=%d/15 null=%d excess=%d'
          % (ok, rk, len(null) if ok else -1, nr - rk))
    if ok:
        w, dlt, gp = x[:6], x[6:9], x[9:12]
        u5, s5, t5 = x[12], x[13], x[14]
        print('  (u5, s5, t5) = (%s, %s, %s)' % (rr(u5,p), rr(s5,p), rr(t5,p)))
        print('  w      =', [rr(v,p) for v in w])
        print('  delta  =', [rr(v,p) for v in dlt])
        print('  gamma\' =', [rr(v,p) for v in gp])
        if null:
            for v in null: print('  null:', [rr(u,p) for u in v])

for p in (2147483647, 2147483629):
    run(p); print('-'*60)
