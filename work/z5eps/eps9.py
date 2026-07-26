"""eps9.py -- structural measurements:
 (1) rank([M1 | Q Ph P])  -- any extra L1 freedom via row-valued [eps^1]?
 (2) the E2 alpha-locus: quadrics rho_ij = resid(SigmaT U_iU_j), their span dim,
     and the full solution variety of Sum alpha_i alpha_j rho_ij = 0 in P^2.
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
from eps2 import rref_solve, rr
from eps6 import Pipe

def run(p):
    pi = Pipe(p); nr = pi.nr
    print('prime', p)
    # (1) [M1 | rows]
    cols = []
    for c in range(6):
        e9=[0]*9; e9[c]=1
        cols.append(None)
    # antisym M1 letters: SigmaT w1_j  (should be 0 identically)
    for j in range(3):
        e9=[0]*9; e9[6+j]=1
        v = None
        assert all(x==0 for x in v), 'antisym w1 sum nonzero?!'
    cols += pi.rowcols()
    A=[[c[n] for c in cols] for n in range(nr)]
    ok,x,null,rk = rref_solve(A,[0]*nr,p)
    print('(1) rank[M1(6)|rows(3)] = %d of 9, null dim %d' % (rk, len(null)))
    for v in null: print('    null:', [rr(u,p) for u in v])

    # (2) E2 quadrics
    cols2 = []
    for c in range(6):
        e9=[0]*9; e9[c]=1
        cols2.append(pi.momH([], 2, e9))
    cols2 += pi.rowcols()
    # moment vectors SigmaT U_iU_j  (i<=j)
    UU = {}
    for i in range(3):
        for j in range(i,3):
            v1=[0]*5; v1[2+i]=1
            v2=[0]*5; v2[2+j]=1
            UU[(i,j)] = pi.mom([v1,v2])
    # reduce against cols2: build matrix [cols2 | UU...] and rref on cols2 part
    keys = sorted(UU)
    M = [[c[n] for c in cols2] + [UU[k][n] for k in keys] for n in range(nr)]
    r=0
    for col in range(9):
        pr = next((i for i in range(r,nr) if M[i][col]%p), None)
        if pr is None: continue
        M[r],M[pr]=M[pr],M[r]
        inv=pow(M[r][col],p-2,p)
        M[r]=[v*inv%p for v in M[r]]
        for i in range(nr):
            if i!=r and M[i][col]:
                f=M[i][col]
                M[i]=[(v-f*w)%p for v,w in zip(M[i],M[r])]
        r+=1
    res = [row[9:] for row in M[r:] if any(v%p for v in row[9:])]
    ok,x,null,d = rref_solve(res,[0]*len(res),p) if res else (True,None,[],0)
    print('(2) rank(cols2)=%d; quadric-condition count d = %d (of 6 possible)' % (r, d))
    # the d independent conditions: rows of rref of res
    # solve system of quadrics q_m(alpha)=0.  coordinates order keys=(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)
    # with q(alpha) = sum_{i<=j} c_{ij} alpha_i alpha_j (c includes symmetry factor already since
    # mom([v1,v2]) with i!=j counts UU once; alpha_i alpha_j coefficient must be 2*UU_ij)
    okr, xr, nullr, dr = rref_solve(res, [0]*len(res), p)
    # get independent condition rows:
    conds = []
    Mm = [row[:] for row in res]
    rr_=0
    for col in range(6):
        pr = next((i for i in range(rr_,len(Mm)) if Mm[i][col]%p), None)
        if pr is None: continue
        Mm[rr_],Mm[pr]=Mm[pr],Mm[rr_]
        inv=pow(Mm[rr_][col],p-2,p)
        Mm[rr_]=[v*inv%p for v in Mm[rr_]]
        for i in range(len(Mm)):
            if i!=rr_ and Mm[i][col]:
                f=Mm[i][col]
                Mm[i]=[(v-f*w)%p for v,w in zip(Mm[i],Mm[rr_])]
        rr_+=1
    conds = Mm[:rr_]
    print('    independent quadric conditions:')
    for cd in conds:
        print('      ', {k: rr(v,p) for k,v in zip(keys,cd) if v%p})
    # evaluate at Psi = (-3,1,2):
    Psi=(-3,1,2)
    for m,cd in enumerate(conds):
        val = 0
        for (i,j),cv in zip(keys,cd):
            f = 1 if i==j else 2
            val = (val + cv*f*Psi[i]*Psi[j]) % p
        print('    q_%d(Psi) = %d' % (m, val))
    # brute solve in chart a3=1 and a3=0, via gcd of polys in one var:
    # substitute a1=s, a2=u, a3=1: each cond -> poly in (s,u) deg 2; do resultant scan:
    # simple approach: for each cond pair, iterate s over roots of resultant? Instead:
    # small search: solve cond0=cond1=0 by sweeping s in F_p is too big; use sympy-free
    # elimination: treat cond0, cond1 as quadratics in u: resultant in u -> quartic in s.
    def poly_in_u(cd, s):
        # returns coeffs [u^2, u^1, u^0] with a1=s, a2=u, a3=1
        # keys: (0,0)->s^2 ; (0,1)->2 s u ; (0,2)-> 2 s ; (1,1)->u^2 ; (1,2)->2u ; (2,2)->1
        c = dict(zip(keys, cd))
        A2 = c.get((1,1),0)
        A1 = (2*s*c.get((0,1),0) + 2*c.get((1,2),0)) % p
        A0 = (s*s%p*c.get((0,0),0) + 2*s*c.get((0,2),0) + c.get((2,2),0)) % p
        return A2%p, A1%p, A0%p
    if len(conds) >= 2:
        sols = []
        import random
        # resultant of two quadratics in u: Res = (A2*B0 - A0*B2)^2 - (A2*B1-A1*B2)(A1*B0-A0*B1)
        # find roots s of Res by... Res is quartic in s: reconstruct coefficients by interpolation
        def res_at(s):
            A2,A1,A0 = poly_in_u(conds[0], s)
            B2,B1,B0 = poly_in_u(conds[1], s)
            return ((A2*B0 - A0*B2)**2 - (A2*B1 - A1*B2)*(A1*B0 - A0*B1)) % p
        xs = list(range(9))
        ys = [res_at(s) for s in xs]
        # interpolate degree-8 poly (safe upper bound), then find rational roots by trial
        # Lagrange coefficients:
        import itertools
        def interp_coeffs(xs, ys, p, deg):
            # Vandermonde solve
            A=[[pow(x,i,p) for i in range(deg+1)] for x in xs[:deg+1]]
            ok,c,null,r = rref_solve(A, ys[:deg+1], p)
            return c
        c8 = interp_coeffs(xs, ys, p, 8)
        # check on extra point
        s=11; val=sum(c8[i]*pow(s,i,p) for i in range(9))%p
        assert val==res_at(s)%p
        print('    resultant poly coeffs (u-elim, chart a3=1):', [rr(v,p) for v in c8])
    return

for p in (2147483647,):
    run(p)
