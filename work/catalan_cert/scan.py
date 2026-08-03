"""
Numeric scan: for pre-operator order ORDER and parity EPS, instantiate n = n0
and solve the full joint linear system (weight-2 solves + all lower sectors +
p_i) exactly over Q.  Reports the nullspace dimension and the p-vector (scaled).

Usage: python3 scan.py ORDER EPS n0 [n0 ...]
"""
import sympy as sp
import sys, os

SP = os.path.dirname(os.path.abspath(__file__)) + '/'
src = open(SP + 'certificate.py').read()
exec(src.split("print('cell monomials (by weight):')")[0])

# rational-solver part (k-only after n substitution)
exec(src.split("# ---------------------------------------------------------------- rational solver")[1]
        .split("# ---------------------------------------------------------------- graded solve")[0])

ORDER = int(sys.argv[1]); EPS = int(sys.argv[2])
NVALS = [sp.Integer(x) for x in sys.argv[3:]]

SHK = (1, 1, 0, 0, 0, 0); SH2 = (1, 0, 1, 0, 0, 0)
K1A = (0, 0, 0, 1, 0, 0); K1B = (0, 0, 0, 0, 1, 0)
SECTORS = [SHK, SH2, K1A, K1B, S1]
DIAG = {SHK: -1, SH2: -1, K1A: 1, K1B: 1, S1: -1}

def run(n0):
    sub = {n: n0, e: EPS}
    rl = sp.cancel(r.subs(sub))
    rhopl = sp.cancel(rho_p.subs(sub))
    INCl = {L: {m: sp.cancel(c.subs(sub)) for m, c in d.items()} for L, d in INC.items()}

    def shift_monomial_l(m):
        out = {ONE: sp.Integer(1)}
        for i, L in enumerate(LETTERS[1:], start=1):
            base = {tuple(1 if j == i else 0 for j in range(6)): sp.Integer(1)}
            term = eadd(base, INCl[L])
            for _ in range(m[i]):
                out = emul(out, term)
        if m[0]:
            out = emul(out, {S1: sp.Integer(1)})
        return {mm: (-c if mm[0] else c) for mm, c in out.items()}

    def shift_element_l(el):
        out = {}
        for m, c in el.items():
            cs = sp.cancel(c.subs(k, k + 1))
            for mm, cc in shift_monomial_l(m).items():
                out[mm] = out.get(mm, 0) + cs * cc
        return {m: sp.cancel(c) for m, c in out.items() if sp.cancel(c) != 0}

    def delta_l(cm, m):
        return eadd(escale(shift_element_l({m: cm}), rl), {m: -cm})

    def solve_fo(diag, g, extra=8):
        g = sp.cancel(sp.together(g))
        if g == 0:
            return sp.Integer(0)
        An, Ad = sp.fraction(sp.cancel(diag * rl))
        Gn, Gd = sp.fraction(g)
        A = sp.expand(An * Gd); B = sp.expand(-Ad * Gd); C = sp.expand(Gn * Ad)
        u = univ_denominator(A, B, J=ORDER + 10)
        u1 = u.subs(k, k + 1)
        lhsA = sp.expand(A * u); lhsB = sp.expand(B * u1); rhs = sp.expand(C * u * u1)
        dz = max(sp.Poly(rhs, k).degree() - max(sp.Poly(lhsA, k).degree(),
                                                sp.Poly(lhsB, k).degree()), 0) + extra
        cs = sp.symbols('q0:%d' % (dz + 1))
        z = sum(c * k**i for i, c in enumerate(cs))
        eq = sp.expand(lhsA * z.subs(k, k + 1) + lhsB * z - rhs)
        sol = sp.solve([sp.Eq(c, 0) for c in sp.Poly(eq, k).all_coeffs()], cs, dict=True)
        if not sol:
            return None
        zz = z.subs(sol[0]).subs({c: 0 for c in cs})
        return sp.cancel(zz / u)

    # cells at n0
    def sig_i(i):
        out = sp.Integer(1)
        for t in range(i):
            out *= rhopl.subs(n, n0 + t).subs(k, k) if False else sp.cancel(rho_p.subs({n: n0 + t, e: EPS}))
        return sp.cancel(out)

    def cell_at(i):
        el = {m: sp.cancel(c.subs({n: n0 + i, e: (-1)**i * EPS})) for m, c in CELL.items()}
        if i:
            delta = sum((-1)**t * sp.Rational(1) / (2*(n0) - 2*k + 2*t + 1) for t in range(i))
            out = {}
            for m, c in el.items():
                out[m] = out.get(m, 0) + c
                if m[4]:
                    m0 = ((m[0] + 1) % 2,) + m[1:4] + (0,) + (m[5],)
                    out[m0] = out.get(m0, 0) + c * EPS * delta
            el = {m: sp.cancel(c) for m, c in out.items() if sp.cancel(c) != 0}
        return escale(el, sig_i(i))

    ps = sp.symbols('p0:%d' % (ORDER + 1))
    residuals = []
    for i in range(ORDER + 1):
        resid = dict(cell_at(i))
        while True:
            top = [m for m in resid if weight(m) == 2]
            if not top:
                break
            m = top[0]
            phi = solve_fo(1, resid.pop(m))
            assert phi is not None, ('w2', i, m)
            contrib = delta_l(phi, m); contrib.pop(m, None)
            for mm, cc in contrib.items():
                resid[mm] = sp.cancel(resid.get(mm, 0) - cc)
                if resid[mm] == 0:
                    resid.pop(mm)
        residuals.append(resid)

    g = {}
    for i, resd in enumerate(residuals):
        for m, c in resd.items():
            g[m] = g.get(m, 0) + ps[i] * c
    g = {m: sp.cancel(sp.together(c)) for m, c in g.items()}

    # joint system over sectors
    COUP = {SHK: -rl / (k + 1), SH2: -rl * (1/(2*k + 1) + 1/(2*k + 2)),
            K1A: rl / (2*k + 1), K1B: rl * EPS / (2*n0 - 2*k - 1)}
    unknowns = list(ps)
    phi = {}
    uu = {}
    An, Ad = sp.fraction(sp.cancel(rl))
    for si, m in enumerate(SECTORS):
        gd = sp.fraction(g.get(m, sp.Integer(0)))[1]
        if m == S1:
            for mm in (SHK, SH2, K1A, K1B):
                gd = sp.lcm(sp.Poly(gd, k), sp.Poly(sp.expand(
                    sp.fraction(sp.cancel(COUP[mm]))[1] * uu[mm].subs(k, k + 1)), k)).as_expr()
        A = sp.expand(DIAG[m] * An * gd); B = sp.expand(-Ad * gd)
        um = univ_denominator(A, B, J=ORDER + 10)
        uu[m] = um
        zs = sp.symbols('z%d_0:%d' % (si, 26))
        unknowns += list(zs)
        phi[m] = sum(c * k**i for i, c in enumerate(zs)) / um
    eqs = []
    for m in SECTORS:
        lhs = DIAG[m] * rl * phi[m].subs(k, k + 1) - phi[m]
        rhs = g.get(m, sp.Integer(0))
        if m == S1:
            for mm in (SHK, SH2, K1A, K1B):
                rhs = rhs + sp.cancel(COUP[mm]) * phi[mm].subs(k, k + 1)
        num = sp.fraction(sp.cancel(sp.together(lhs - rhs)))[0]
        eqs += [c for c in sp.Poly(sp.expand(num), k).all_coeffs()]
    sol = sp.solve([sp.Eq(c, 0) for c in eqs], unknowns, dict=True)
    if not sol:
        print('n=%s: NO solution' % n0)
        return
    s0 = sol[0]
    pv = [sp.Symbol(str(p)).subs(s0) for p in ps]
    freeps = sorted({f for x in pv for f in x.free_symbols}, key=str)
    print('n=%s: p = %s   free: %s' % (n0, pv, freeps))

for n0 in NVALS:
    run(n0)
