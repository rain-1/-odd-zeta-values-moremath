"""
Modular sector-sequential nullspace scan for the Catalan pre-operator.

For order ORDER, parity EPS, numeric n0: work mod P = 2^127-1.  Maintain the
subspace of admissible p-vectors, processing sectors top-down in weight; each
sector solve is a small modular linear system.  Output: final nullspace
dimension and the p-vector(s) mod P (exact rationals via rational
reconstruction when dim = 1).

Usage: python3 scan3.py ORDER EPS n0 [n0...]
"""
import sympy as sp
import sys, os
from fractions import Fraction as F

P = 2**127 - 1

SP = os.path.dirname(os.path.abspath(__file__)) + '/'
src = open(SP + 'certificate.py').read()
exec(src.split("print('cell monomials (by weight):')")[0])
exec(src.split("# ---------------------------------------------------------------- rational solver")[1]
        .split("def solve_first_order")[0])

ORDER = int(sys.argv[1]); EPS = int(sys.argv[2])
NVALS = [int(x) for x in sys.argv[3:]]

W2 = [(0, 0, 0, 0, 0, 1), (0, 1, 0, 1, 0, 0), (0, 1, 0, 0, 1, 0),
      (0, 0, 1, 1, 0, 0), (0, 0, 1, 0, 1, 0)]
SHK = (1, 1, 0, 0, 0, 0); SH2 = (1, 0, 1, 0, 0, 0)
K1A = (0, 0, 0, 1, 0, 0); K1B = (0, 0, 0, 0, 1, 0)
BASIS = W2 + [SHK, SH2, K1A, K1B, S1]
DIAGSIGN = {m: (-1 if m[0] else 1) for m in BASIS}
EXTRA = 10

def inv(a):
    return pow(a % P, P - 2, P)

def ratfun_mod(expr):
    """expr rational in k -> (numcoeffs, dencoeffs) as int lists mod P (asc)."""
    nu, de = sp.fraction(sp.cancel(sp.together(expr)))
    def coeffs(p):
        pl = sp.Poly(p, k)
        cs = []
        for c in reversed(pl.all_coeffs()):
            q = sp.Rational(c)
            cs.append(int(q.p) % P * inv(int(q.q)) % P)
        return cs
    return coeffs(nu), coeffs(de)

def horner(cs, x):
    v = 0
    for c in reversed(cs):
        v = (v * x + c) % P
    return v

def evalrat(nc_dc, x):
    ncs, dcs = nc_dc
    d = horner(dcs, x)
    return horner(ncs, x) * inv(d) % P

def rat_reconstruct(a):
    """rational reconstruction of a mod P (|num|,|den| < sqrt(P/2))."""
    a %= P
    r0, r1 = P, a
    s0, s1 = 0, 1
    bound = int(P**0.5) // 2
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if s1 == 0:
        return None
    return F(r1 if s1 > 0 else -r1, abs(s1))

def run(n0):
    sub = {n: sp.Integer(n0), e: sp.Integer(EPS)}
    rl = sp.cancel(r.subs(sub))
    def cell_at(i):
        el = {m: sp.cancel(c.subs({n: sp.Integer(n0 + i), e: sp.Integer((-1)**i * EPS)}))
              for m, c in CELL.items()}
        if i:
            delta = sum(sp.Integer((-1)**t) / (2*n0 - 2*k + 2*t + 1) for t in range(i))
            out = {}
            for m, c in el.items():
                out[m] = out.get(m, 0) + c
                if m[4]:
                    m0 = ((m[0] + 1) % 2,) + m[1:4] + (0,) + (m[5],)
                    out[m0] = out.get(m0, 0) + c * EPS * delta
            el = {m: sp.cancel(c) for m, c in out.items() if sp.cancel(c) != 0}
        s = sp.Integer(1)
        for t in range(i):
            s *= sp.cancel(rho_p.subs({n: sp.Integer(n0 + t)}))
        return escale(el, sp.cancel(s))
    cells = [cell_at(i) for i in range(ORDER + 1)]

    INCl = {L: {m: sp.cancel(c.subs(sub)) for m, c in d.items()} for L, d in INC.items()}
    def shift_monomial_l(m):
        out = {ONE: sp.Integer(1)}
        for i, L in enumerate(LETTERS[1:], start=1):
            base = {tuple(1 if j == i else 0 for j in range(6)): sp.Integer(1)}
            term = eadd(base, INCl[L])
            for _ in range(m[i]):
                out = emul(out, term)
        if m[0]:
            out = emul(out, {S1: sp.Integer(-1)})
        return out
    SHIFT = {m: shift_monomial_l(m) for m in BASIS}

    An, Ad = sp.fraction(sp.cancel(rl))
    uu = {}
    for m in BASIS:
        ds = sp.Integer(1)
        for i in range(ORDER + 1):
            if m in cells[i]:
                ds = sp.lcm(sp.Poly(ds, k), sp.Poly(sp.fraction(sp.cancel(cells[i][m]))[1], k)).as_expr()
        for mprev in BASIS:
            if mprev == m or mprev not in uu:
                continue
            if SHIFT[mprev].get(m) is not None:
                dd = sp.expand(sp.fraction(sp.cancel(rl * SHIFT[mprev][m]))[1]
                               * uu[mprev].subs(k, k + 1))
                ds = sp.lcm(sp.Poly(ds, k), sp.Poly(dd, k)).as_expr()
        A = sp.expand(DIAGSIGN[m] * An * ds); B = sp.expand(-Ad * ds)
        uu[m] = univ_denominator(A, B, J=ORDER + 8)

    # modular data
    RL = ratfun_mod(rl)
    UM = {m: ratfun_mod(uu[m]) for m in BASIS}
    UM1 = {m: ratfun_mod(uu[m].subs(k, k + 1)) for m in BASIS}
    CE = {(i, m): ratfun_mod(cells[i][m]) for i in range(ORDER + 1) for m in cells[i]}
    CP = {(mp, m): ratfun_mod(rl * SHIFT[mp][m]) for mp in BASIS for m in SHIFT[mp]
          if m != mp and m in [b for b in BASIS]}
    NZ = {m: sp.Poly(uu[m], k).degree() + EXTRA + 1 for m in BASIS}

    third = inv(3)
    # state: q-dimension d; pbasis[(i)][t]; phis[m][t] = z-coeff list (len NZ[m])
    d = ORDER + 1
    pbasis = [[1 if i == t else 0 for t in range(d)] for i in range(ORDER + 1)]
    phis = {}

    for m in BASIS:
        nz = NZ[m]
        nsamp = nz + d + 40
        # rows: sample equations; cols: z_0..z_{nz-1}, q_0..q_{d-1}
        rows = []
        for tsm in range(nsamp):
            x = (tsm * 3 + 1) * third % P
            x1 = (x + 1) % P
            rv = evalrat(RL, x)
            umv = evalrat(UM, x) if False else evalrat(UM[m], x)
            um1v = evalrat(UM1[m], x)
            row = [0] * (nz + d)
            xp = 1
            x1p = 1
            iu = inv(umv); iu1 = inv(um1v)
            for j in range(nz):
                row[j] = (DIAGSIGN[m] * rv * x1p % P * iu1 - xp * iu) % P
                xp = xp * x % P; x1p = x1p * x1 % P
            # rhs: sum_t q_t * [ sum_i pbasis[i][t] cells_i[m](x)
            #                    - sum_senders coup(x) * phi_mp,t(x+1) ]
            for t in range(d):
                val = 0
                for i in range(ORDER + 1):
                    if (i, m) in CE and pbasis[i][t]:
                        val = (val + pbasis[i][t] * evalrat(CE[(i, m)], x)) % P
                for mp in BASIS:
                    if mp == m or mp not in phis or (mp, m) not in CP:
                        continue
                    cv = evalrat(CP[(mp, m)], x)
                    zt = phis[mp][t]
                    um1p = evalrat(UM1[mp], x)
                    val = (val - cv * horner(zt, x1) % P * inv(um1p)) % P
                row[nz + t] = (-val) % P
            rows.append(row)
        # eliminate
        ncols = nz + d
        mat = rows
        pivots = {}
        prow = 0
        for c in range(ncols):
            pr = next((rr for rr in range(prow, len(mat)) if mat[rr][c]), None)
            if pr is None:
                continue
            mat[prow], mat[pr] = mat[pr], mat[prow]
            iv = inv(mat[prow][c])
            mat[prow] = [x * iv % P for x in mat[prow]]
            piv = mat[prow]
            for rr in range(len(mat)):
                if rr != prow and mat[rr][c]:
                    f = mat[rr][c]
                    mr = mat[rr]
                    mat[rr] = [(a - f * b) % P for a, b in zip(mr, piv)]
            pivots[c] = prow
            prow += 1
        # q-columns that are pivots => those q-combinations forced to relations
        qpivots = [c - nz for c in pivots if c >= nz]
        freeq = [t for t in range(d) if t + nz not in pivots]
        dnew = len(freeq)
        # new q params = old q restricted: for pivot q-col t: q_t = -sum over free
        qmap = [[0] * dnew for _ in range(d)]     # old q index x new
        for a, t in enumerate(freeq):
            qmap[t][a] = 1
        for c, pr in pivots.items():
            if c >= nz:
                t = c - nz
                for a, tf in enumerate(freeq):
                    qmap[t][a] = (-mat[pr][nz + tf]) % P
        # z solution for this sector in terms of new q
        znew = [[0] * dnew for _ in range(nz)]
        for c, pr in pivots.items():
            if c < nz:
                for a, tf in enumerate(freeq):
                    znew[c][a] = (-mat[pr][nz + tf]) % P
        # update pbasis and stored phis to new q parametrization
        pbasis = [[sum(pbasis[i][t] * qmap[t][a] for t in range(d)) % P
                   for a in range(dnew)] for i in range(ORDER + 1)]
        for mp in list(phis):
            phis[mp] = [[sum(phis[mp][t][j] * qmap[t][a] for t in range(d)) % P
                         for j in range(NZ[mp])]
                        for a in range(dnew)]
        phis[m] = [[znew[j][a] for j in range(nz)] for a in range(dnew)]
        d = dnew
        if d == 0:
            print('n=%d: dim 0 (failed at sector %s)' % (n0, (m,)))
            return
    print('n=%d: final dim %d' % (n0, d))
    for a in range(d):
        pv = [pbasis[i][a] for i in range(ORDER + 1)]
        nrm = next((x for x in reversed(pv) if x), None)
        pvn = [x * inv(nrm) % P for x in pv]
        rec = [rat_reconstruct(x) for x in pvn]
        print('   p (normalized, reconstructed) =', rec)
        print('   praw', n0, pvn)

for n0 in NVALS:
    run(n0)
