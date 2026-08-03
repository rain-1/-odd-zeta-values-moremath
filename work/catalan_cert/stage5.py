"""
Stage 5: grand joint linear solve.  For a given pre-operator order (argv[1],
default 3) and parity e=+-1, solve simultaneously for
    p_1..p_ORDER  and  cofactors phi_m for m in {sHk, sH2, K1a, K1b, s}
such that  Delta_k [ S * (sum_i p_i cert2_i + sum_m phi_m M_m) ] matches
sum_i p_i C(n+i,k)  in every letter monomial.  cert2_i (weight-2 cofactors per
shift, computed in preop.py) already match the weight-2 sector; 'combined' from
preop.py is the p-weighted lower-weight residual.  All equations are linear in
the unknowns.
"""
import sympy as sp
import pickle, os, sys

SP = os.path.dirname(os.path.abspath(__file__)) + '/'
src = open(SP + 'certificate.py').read()
exec(src.split("# ---------------------------------------------------------------- graded solve")[0])

st2 = pickle.load(open(SP + 'stage2_state.pkl', 'rb'))
ps = list(st2['ps'])[1:]          # p0 dropped: shifts 1..ORDER only?  keep p0!
ps = list(st2['ps'])
ORDER = st2['ORDER']
combined = st2['combined']

SHK = (1, 1, 0, 0, 0, 0); SH2 = (1, 0, 1, 0, 0, 0)
K1A = (0, 0, 0, 1, 0, 0); K1B = (0, 0, 0, 0, 1, 0)
S1m = S1
SECTORS = [SHK, SH2, K1A, K1B, S1m]
DIAG = {SHK: -1, SH2: -1, K1A: 1, K1B: 1, S1m: -1}

# couplings INTO S1 from each weight-1 sector: Delta(phi M) contains
# coup_m(k) * phi(k+1) * s-monomial, with:
COUP = {SHK: -r / (k + 1),
        SH2: -r * (1/(2*k + 1) + 1/(2*k + 2)),
        K1A: r / (2*k + 1),
        K1B: r * e / (2*n - 2*k - 1)}

DZ = int(sys.argv[2]) if len(sys.argv) > 2 else 24

def univ(diag, denshape):
    An, Ad = sp.fraction(sp.cancel(diag * r))
    A = sp.expand(An * denshape); B = sp.expand(-Ad * denshape)
    return univ_denominator(A, B, J=ORDER + 10)

results = {}
for EPS in (1, -1):
    g = {m: sp.cancel(sp.together(c.subs(e, EPS))) for m, c in combined.items()}
    # denominators / universal denominators per sector
    u = {}
    for m in (SHK, SH2, K1A, K1B):
        u[m] = univ(DIAG[m], sp.fraction(g.get(m, sp.Integer(0)))[1])
    # S1 rhs denominator shape: own target + couplings phi_m(k+1)*coup
    dens = [sp.fraction(g.get(S1m, sp.Integer(0)))[1]]
    for m in (SHK, SH2, K1A, K1B):
        cpl = sp.cancel(COUP[m].subs(e, EPS))
        dens.append(sp.expand(u[m].subs(k, k + 1) * sp.fraction(cpl)[1]))
    denS = sp.Integer(1)
    for d in dens:
        denS = sp.lcm(sp.Poly(denS, k, domain='QQ(n)'), sp.Poly(d, k, domain='QQ(n)')).as_expr()
    u[S1m] = univ(DIAG[S1m], denS)

    unknowns = list(ps)
    phi = {}
    for si, m in enumerate(SECTORS):
        zs = sp.symbols('z%d_0:%d' % (si, DZ + 1))
        unknowns += list(zs)
        phi[m] = sum(c * k**i for i, c in enumerate(zs)) / u[m]

    # equations
    eqs = []
    for m in SECTORS:
        lhs = DIAG[m] * r * phi[m].subs(k, k + 1) - phi[m]
        rhs = g.get(m, sp.Integer(0))
        if m == S1m:
            for mm in (SHK, SH2, K1A, K1B):
                rhs = rhs + sp.cancel(COUP[mm].subs(e, EPS)) * phi[mm].subs(k, k + 1)
        num = sp.fraction(sp.cancel(sp.together(lhs - rhs)))[0]
        eqs += [sp.cancel(c) for c in sp.Poly(sp.expand(num), k).all_coeffs()]

    sol = sp.solve([sp.Eq(c, 0) for c in eqs], unknowns, dict=True)
    assert sol, ('no solution branch', EPS)
    s0 = sol[0]
    pv = [sp.cancel(sp.Symbol(str(p)).subs(s0)) for p in ps]
    free = sorted({f for x in pv for f in x.free_symbols if str(f)[0] in 'pz'}, key=str)
    print('parity %+d: free params in p: %s' % (EPS, free))
    for i, x in enumerate(pv):
        print('  p%d =' % i, sp.factor(x))
    results[EPS] = {'sol': s0, 'phi': phi, 'u': u, 'unknowns': unknowns}
pickle.dump(results, open(SP + 'stage5_state.pkl', 'wb'))
print('saved stage5_state.pkl')
