"""eps14.py -- the special point (a,b,c,d)=(-1,0,1,2): joint E4+E5 with shared
(z, gamma); row-coefficient uniqueness; null structure.  Both primes.
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
from eps2 import rref_solve, rr
from eps6 import Pipe

def joint_at(pi, a, b, c, d, tval, verbose=True):
    p = pi.p; nr = pi.nr
    i2, i6, i24, i120 = pi.inv(2), pi.inv(6), pi.inv(24), pi.inv(120)
    alpha = ((-c-d) % p, c % p, d % p)
    a1c = [0,0] + list(alpha)
    s1c = [a % p, b % p, 0, 0, 0]
    x2 = pi.E2(s1c, a1c, verbose=False)
    g9 = list(x2[:6]) + [0,0,0]
    s2u2v2 = x2[6:9]
    x3, null3 = pi.E3(s1c, a1c, g9, verbose=False)
    ker = null3[0]
    y  = [(x3[i] + tval*ker[i]) % p for i in range(6)]
    bt = [(x3[6+i] + tval*ker[6+i]) % p for i in range(3)]
    t3, s3, v3 = [(x3[9+i] + tval*ker[9+i]) % p for i in range(3)]
    y9 = y + [0,0,0]; b9 = [0]*6 + bt
    if verbose:
        print('E2 rows (u2,s2,v2):', [rr(v,p) for v in s2u2v2])
        print('E3: (t3,s3,v3) = (%s,%s,%s)' % (rr(t3,p), rr(s3,p), rr(v3,p)))
        print('E3: y =', [rr(v,p) for v in y], ' beta =', [rr(v,p) for v in bt])
        print('E2: g =', [rr(v,p) for v in g9[:6]])

    # ---------- joint E4 + E5 ----------
    # unknowns: [z6, gam3, r4_3, w6, dlt3, r5_3] = 24
    rows = pi.rowcols()
    # E4 columns
    colsz = pi.stage_cols2(4, 3, alpha)     # M4sym(6) + A1w3(3): z, gamma-in-E4
    # E4 RHS (all forced; includes beta-quadratics)
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
    # E5 columns
    colsw = pi.stage_cols2(5, 4, alpha)     # M5sym(6) + A1w4(3): w, delta
    gcols5 = []
    for j in range(3):
        e9=[0]*9; e9[6+j]=1
        c1 = pi.momHH([], b9, 2, e9, 3)
        c2 = pi.momH([s1c, a1c], 3, e9)
        gcols5.append([(c1[n]+c2[n]) % p for n in range(nr)])
    zcols5 = []
    for cix in range(6):
        e9=[0]*9; e9[cix]=1
        zcols5.append(pi.momH([s1c], 4, e9))
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
    rhs5 = [(-(t_s2s3[n] + i2*(t_s12s3[n]+t_a12s3[n])
               + i2*(t_s1s2s2[n]+t_s1a2a2[n]) + t_a1s2a2[n]
               + i6*(t_s13s2[n]+3*t_s1a12s2[n]+3*t_s12a1a2[n]+t_a13a2[n])
               + i120*(t_s15[n]+10*t_s13a12[n]+5*t_s1a14[n]))) % p
            for n in range(nr)]
    NU = 24
    A, bb = [], []
    for n in range(nr):     # E4 block
        row = [0]*NU
        for j in range(9): row[j] = colsz[j][n]
        for j in range(3): row[9+j] = rows[j][n]
        A.append(row); bb.append(rhs4[n])
    for n in range(nr):     # E5 block
        row = [0]*NU
        for j in range(3): row[6+j] = gcols5[j][n]      # shared gamma
        for j in range(6): row[j] = zcols5[j][n] if False else row[j]
        # careful: z is shared too (S1S4 term in E5)
        for j in range(6): row[j] = (row[j] + zcols5[j][n]) % p
        for j in range(9): row[12+j] = colsw[j][n]
        for j in range(3): row[21+j] = rows[j][n]
        A.append(row); bb.append(rhs5[n])
    ok, x, null, rk = rref_solve(A, bb, p)
    print('JOINT E4+E5 at t=%d: ok=%s rank=%d/24 null=%d' % (tval, ok, rk, len(null) if ok else -1))
    if ok:
        print('  (u4,s4,v4)=(%s,%s,%s)  (u5,s5,t5)=(%s,%s,%s)'
              % tuple(rr(x[i],p) for i in (9,10,11,21,22,23)))
        # do null vectors touch the row coefficients?
        touch4 = any(any(v[i] % p for i in (9,10,11)) for v in null)
        touch5 = any(any(v[i] % p for i in (21,22,23)) for v in null)
        print('  null touches r4:', touch4, '  null touches r5:', touch5)
    return ok

for p in (2147483647, 2147483629):
    print('='*64); print('prime', p)
    pi = Pipe(p)
    for t in (1, 2, -1, 5):
        joint_at(pi, -1, 0, 1, 2, t, verbose=(t == 1))
        print()
