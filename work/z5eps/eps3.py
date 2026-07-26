"""eps3.py -- E3 obstruction locus over (a:b), exactly.

E3: exists (y, t3, s3, v3):  M3.y - t3*Ph - s3*Q - v3*P = -( L1L2 + L1^3/6 )
with g(a,b) the unique E2 solution (rank(M2)=6).  RHS is homogeneous cubic in
(a,b): RHS = a^3 c0 + a^2 b c1 + a b^2 c2 + b^3 c3.  Reduce c_m against the
9-dim column space; the residuals span dim d.  d=4 -> no (a:b) works. d<4 ->
intersect null space with the twisted cubic.
"""
import sys
from math import comb
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import core
from eps2 import sweep, rref_solve, rr, NMAX

def run(p):
    print('prime', p)
    S = sweep(p, NMAX)
    lad = core.ladders()
    fm = lambda fr: fr.numerator % p * pow(fr.denominator % p, p - 2, p) % p
    Qs  = [fm(lad['Q'][n])  for n in range(NMAX + 1)]
    Phs = [fm(lad['Ph'][n]) for n in range(NMAX + 1)]
    Ps  = [fm(lad['P'][n])  for n in range(NMAX + 1)]
    i2 = pow(2, p - 2, p); i6 = pow(6, p - 2, p)
    R2, R3, P_ = S['R2'], S['R3'], S['P']
    nrows = NMAX + 1

    # E2 particular solutions for the three quadratic monomials
    A2 = [R2[(0,0)][n][:] for n in range(nrows)]
    gs = {}
    for key, mom in (('20',(2,0)), ('11',(1,1)), ('02',(0,2))):
        fac = 2 if key == '11' else 1   # L1^2 = a^2 P20 + 2ab P11 + b^2 P02
        b = [(-i2 * fac * P_[mom][n]) % p for n in range(nrows)]
        ok, g, null, r = rref_solve(A2, b, p)
        assert ok and not null, (ok, len(null) if null else None, r)
        gs[key] = g
    print('E2 solved: g20,g11,g02 unique (rank 6)')

    # cubic coefficient vectors c_m(n)
    c = [[0]*nrows for _ in range(4)]
    for n in range(nrows):
        r10 = R2[(1,0)][n]; r01 = R2[(0,1)][n]
        c[0][n] = (sum(gs['20'][j]*r10[j] for j in range(6)) + i6*P_[(3,0)][n]) % p
        c[1][n] = (sum(gs['11'][j]*r10[j] + gs['20'][j]*r01[j] for j in range(6))
                   + 3*i6*P_[(2,1)][n]) % p
        c[2][n] = (sum(gs['02'][j]*r10[j] + gs['11'][j]*r01[j] for j in range(6))
                   + 3*i6*P_[(1,2)][n]) % p
        c[3][n] = (sum(gs['02'][j]*r01[j] for j in range(6)) + i6*P_[(0,3)][n]) % p

    # A3 columns: M3 (6), -Ph, -Q, -P
    A3 = [[R3[(0,0)][n][j] for j in range(6)] + [(-Phs[n])%p, (-Qs[n])%p, (-Ps[n])%p]
          for n in range(nrows)]
    # eliminate: stack [A3 | c0..c3], rref on A3 part
    M = [A3[n][:] + [c[m][n] for m in range(4)] for n in range(nrows)]
    r = 0
    for col in range(9):
        pr = next((i for i in range(r, nrows) if M[i][col] % p), None)
        if pr is None: continue
        M[r], M[pr] = M[pr], M[r]
        inv = pow(M[r][col], p-2, p)
        M[r] = [v*inv % p for v in M[r]]
        for i in range(nrows):
            if i != r and M[i][col]:
                f = M[i][col]
                M[i] = [(v - f*w) % p for v, w in zip(M[i], M[r])]
        r += 1
    print('rank(A3) =', r, 'of 9')
    Cres = [row[9:] for row in M[r:] if any(v % p for v in row[9:])]
    print('nonzero residual rows:', len(Cres), ' of', nrows - r)
    ok, x, null, d = rref_solve(Cres, [0]*len(Cres), p) if Cres else (True,[0]*4,[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],0)
    print('residual span dim d = %d  (d=4 means NO (a:b) works)' % d)
    if d == 4:
        print('=> E3 EXCLUDED for every L1 in N1, k<->l symmetric space')
        return
    print('null space of conditions (allowed cubic-monomial vectors):')
    for v in null: print('   ', [rr(u, p) for u in v])
    # intersect with twisted cubic (m0 m2 = m1^2, m1 m3 = m2^2, m0 m3 = m1 m2)
    # parametrise from null space depending on dim
    print('... intersecting with twisted cubic: dim null =', len(null))

for p in (2147483647, 2147483629):
    run(p)
    print('-'*60)
