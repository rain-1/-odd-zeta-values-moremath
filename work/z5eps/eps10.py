"""eps10.py -- joint E4+E5 linear system along the alpha-line, S1 = 0 branch.

For alpha = (-(c+d), c, d):
  E2 -> g ; E3 kernel -> (yhat, bhat, t3,s3,v3), deformation scale t (tau = t^2).
Joint unknowns  X = [z(6), gamma(3), r4(3), w(6), delta(3), r5(3), tau]  (25)
  E4: M4.z + (A1w3).gamma - rows.r4 + tau*C2 = -C0
  E5: M5.w + (A1w4).delta + (A2hat w3).gamma - rows.r5 = -D1
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
from eps2 import rref_solve, rr
from eps6 import Pipe

def joint(pi, c, d, verbose=False):
    p = pi.p; nr = pi.nr
    i2, i6, i24 = pi.inv(2), pi.inv(6), pi.inv(24)
    alpha = ((-c - d) % p, c % p, d % p)
    a1c = [0, 0] + list(alpha)
    s1c = [0]*5
    x2 = pi.E2(s1c, a1c, verbose=False)
    if x2 is None: return dict(fail='E2')
    g9 = list(x2[:6]) + [0,0,0]
    x3, null3 = pi.E3(s1c, a1c, g9, verbose=False)
    if x3 is None: return dict(fail='E3')
    if len(null3) != 1: return dict(fail='E3dim%d' % len(null3))
    ker = null3[0]
    yhat9 = list(ker[:6]) + [0,0,0]
    bhat9 = [0]*6 + list(ker[6:9])
    t3, s3, v3 = ker[9], ker[10], ker[11]

    # E4 pieces
    cols4z = pi.stage_cols2(4, 3, alpha)      # 6 M4sym + 3 A1w3
    rows = pi.rowcols()
    t_s2s2 = pi.momHH([], g9, 2, g9)
    t_a12s2 = pi.momH([a1c, a1c], 2, g9)
    t_a14 = pi.mom([a1c]*4)
    C0 = [ (i2*(t_s2s2[n] + t_a12s2[n]) + i24*t_a14[n]) % p for n in range(nr) ]
    t_a2a2 = pi.momHH([], bhat9, 2, bhat9)
    C2 = [ i2*t_a2a2[n] % p for n in range(nr) ]
    # E5 pieces
    cols5w = pi.stage_cols2(5, 4, alpha)      # 6 M5sym + 3 A1w4
    gcols5 = []
    for j in range(3):
        e9 = [0]*9; e9[6+j] = 1
        gcols5.append(pi.momHH([], bhat9, 2, e9, 3))   # SigmaT A2hat*w3_j
    t_s2s3 = pi.momHH([], g9, 2, yhat9, 3)
    t_a12s3 = pi.momH([a1c, a1c], 3, yhat9)
    t_a1s2a2 = pi.momHH([a1c], g9, 2, bhat9)
    t_a13a2 = pi.momH([a1c]*3, 2, bhat9)
    D1 = [ (t_s2s3[n] + i2*t_a12s3[n] + t_a1s2a2[n] + i6*t_a13a2[n]) % p
           for n in range(nr) ]

    # assemble: unknowns [z6, gam3, r4_3, w6, dlt3, r5_3, tau]
    NU = 25
    A, b = [], []
    for n in range(nr):
        row = [0]*NU
        for j in range(9): row[j] = cols4z[j][n]
        for j in range(3): row[9+j] = rows[j][n]
        row[24] = C2[n]
        A.append(row); b.append((-C0[n]) % p)
    for n in range(nr):
        row = [0]*NU
        for j in range(9): row[12+j] = cols5w[j][n]
        for j in range(3): row[21+j] = rows[j][n]
        for j in range(3): row[3+j] = gcols5[j][n]     # shared gamma
        A.append(row); b.append((-D1[n]) % p)
    ok, x, null, rk = rref_solve(A, b, p)
    out = dict(ok=ok, rank=rk, ndim=len(null) if ok else -1,
               t3=t3, s3=s3, v3=v3)
    if ok:
        out.update(tau=x[24], r4=x[9:12], r5=x[21:24],
                   z=x[:6], gamma=x[3:6], w=x[12:18], delta=x[18:21])
    return out

if __name__ == '__main__':
    p = 2147483647
    pi = Pipe(p)
    pts = [(1,2),(1,0),(0,1),(1,1),(1,-1),(2,1),(3,1),(1,3),(2,3),(3,2),
           (5,7),(17,-5),(1,-2),(2,-1),(4,1),(1,4),(5,1),(1,5),(7,3),(9,-2),
           (11,5),(13,-7),(3,-4),(8,3)]
    print('joint E4+E5 along the line, S1=0.  (u4,s4,v4)=r4, (u5,s5,t5)=r5')
    for (c,d) in pts:
        R = joint(pi, c, d)
        if not R.get('ok'):
            print('  (c,d)=(%3d,%3d): FAIL %s  kernel(t3,s3,v3)=(%s,%s,%s)'
                  % (c, d, R.get('fail', 'joint-inconsistent'),
                     rr(R['t3'],p) if 't3' in R else '?',
                     rr(R['s3'],p) if 's3' in R else '?',
                     rr(R['v3'],p) if 'v3' in R else '?'))
        else:
            print('  (c,d)=(%3d,%3d): OK rank=%d null=%d tau=%s r4=%s r5=%s t3=%s'
                  % (c, d, R['rank'], R['ndim'], rr(R['tau'],p),
                     [rr(v,p) for v in R['r4']], [rr(v,p) for v in R['r5']],
                     rr(R['t3'],p)))
