"""eps7.py -- pure-Psi branch: treat tau = t^2 as an unknown at E4 and E5.

E4:  cols.x + tau*C2 = -C0   where rhs(t) = -(C0 + t^2 C2)
E5:  rhs(t) = -(t D1 + t^3 D3);  divide by t:  cols.x' + tau*D3 = -D1
Both stages must deliver the SAME tau.
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
from eps2 import rref_solve, rr
from eps6 import Pipe

def run(p, alpha=(-3, 1, 2)):
    pi = Pipe(p)
    print('prime', p, 'alpha', alpha)
    s1c = [0]*5
    a1c = [0, 0] + list(alpha)
    x2 = pi.E2(s1c, a1c, verbose=False)
    g9 = list(x2[:6]) + [0,0,0]
    x3, null3 = pi.E3(s1c, a1c, g9, verbose=False)
    ker = null3[0]
    yhat9 = list(ker[:6]) + [0,0,0]         # y = t*yhat
    bhat9 = [0]*6 + list(ker[6:9])          # beta = t*bhat
    i2, i6, i24 = pi.inv(2), pi.inv(6), pi.inv(24)
    nr = pi.nr

    # ---- E4: C0 and C2 ----
    t_s2s2 = pi.momHH([], g9, 2, g9)
    t_a12s2 = pi.momH([a1c, a1c], 2, g9)
    t_a14 = pi.mom([a1c]*4)
    C0 = [ (i2*t_s2s2[n] + i2*t_a12s2[n] + i24*t_a14[n]) % p for n in range(nr) ]
    t_a2a2 = pi.momHH([], bhat9, 2, bhat9)
    C2 = [ i2*t_a2a2[n] % p for n in range(nr) ]
    cols4 = pi.stage_cols2(4, 3, alpha) + pi.rowcols()
    # append C2 column (coefficient tau), rhs = -C0
    cols4t = cols4 + [C2]
    A = [[c[n] for c in cols4t] for n in range(nr)]
    ok, x, null, rk = rref_solve(A, [(-v) % p for v in C0], p)
    print('E4+tau: ok=%s rank=%d/13 null=%d' % (ok, rk, len(null) if ok else -1))
    if not ok:
        # diagnose: is C2 in colspan(cols4)?  rank with/without
    	A0 = [[c[n] for c in cols4] for n in range(nr)]
    	_,_,_, rk0 = rref_solve(A0, [0]*nr, p)
    	print('   rank(cols4) = %d; rank with C2 = %d; rank with C0 = ?' % (rk0, rk))
    	return None
    tau = x[12]
    z = x[:6]; gam = x[6:9]
    print('E4: tau = %s   (u4,s4,v4)=(%s,%s,%s)' % (rr(tau,p), rr(x[9],p), rr(x[10],p), rr(x[11],p)))
    print('E4: z=%s gamma_hat-part...' % ([rr(v,p) for v in z],))
    # NOTE gamma solved at this tau is gamma(t) with mixed parity!  Care:
    # E4's antisym unknown gamma couples via A1*A3 (t-even RHS) so gamma is even in t. fine.
    # ---- E5 ----
    # gamma = even solution; but z, gamma depend on tau linearly? no: solution at the found tau.
    z9 = list(z) + [0,0,0]
    c9 = [0]*6 + list(gam)
    # E5 rhs = t*(D1 + tau*D3-ish) -- compute by evaluating full rhs at t=1,2 with tau known?
    # Instead: E5 terms with S1=0:
    #  t_s2s3 = g.y ~ t ; t_a2a3 = beta.gamma ~ t ; t_a12s3 ~ t ; t_a1s2a2 ~ t ; t_a13a2 ~ t^3
    #  i2*t_s1a2a2=0 ; others 0.   z-term t_s1s4 = 0.
    # BUT gamma itself contains tau-dependence; we already fixed tau, so gamma is a number.
    # rhs(t) = t*D1 + t^3*Dcube with
    t_s2s3 = pi.momHH([], g9, 2, yhat9, 3)
    t_a2a3 = pi.momHH([], bhat9, 2, c9, 3)
    t_a12s3 = pi.momH([a1c, a1c], 3, yhat9)
    t_a1s2a2 = pi.momHH([a1c], g9, 2, bhat9)
    t_a13a2 = pi.momH([a1c]*3, 2, bhat9)
    D1v = [ (t_s2s3[n] + t_a2a3[n] + i2*t_a12s3[n] + t_a1s2a2[n]) % p for n in range(nr) ]
    D3v = [ i6*t_a13a2[n] % p for n in range(nr) ]
    cols5 = pi.stage_cols2(5, 4, alpha) + pi.rowcols()
    # rhs/t = -(D1 + tau*D3): solve with SAME tau -> consistency check; also solve tau free
    rhs5 = [(-(D1v[n] + tau*D3v[n])) % p for n in range(nr)]
    ok, x5, null5, rk5 = rref_solve([[c[n] for c in cols5] for n in range(nr)], rhs5, p)
    print('E5 at E4-tau: ok=%s rank=%d/12 null=%d' % (ok, rk5, len(null5) if ok else -1))
    if ok:
        print('E5: w=%s delta=%s (u5,s5,t5)=(%s,%s,%s)' %
              ([rr(v,p) for v in x5[:6]], [rr(v,p) for v in x5[6:9]],
               rr(x5[9],p), rr(x5[10],p), rr(x5[11],p)))
    else:
        cols5t = [[c[n] for c in cols5] for n in range(nr)]
        for row, D in zip(cols5t, D3v): row.append(D)
        ok2, x5b, null5b, rk5b = rref_solve(cols5t, [(-v)%p for v in D1v], p)
        print('E5 with free tau: ok=%s rank=%d/13' % (ok2, rk5b))
        if ok2:
            print('   E5 wants tau =', rr(x5b[12], p), ' vs E4 tau =', rr(tau, p))
    return tau

for p in (2147483647, 2147483629):
    run(p)
    print('-'*60)
