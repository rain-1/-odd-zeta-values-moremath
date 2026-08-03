"""
Numeric joint nullspace scan (fast, pure-Fraction linear algebra).

For pre-operator order ORDER, parity EPS, numeric n0: unknowns are
  - p_0..p_ORDER (pre-operator values at n0),
  - cofactor numerators z_m for every basis monomial m (phi_m = z_m/u_m),
and the equations say  Delta_k [S * sum_m phi_m M_m] = sum_i p_i C(n+i,k)
graded by monomial.  Everything is linear; we sample k at thirds and compute
the exact nullspace.

Usage: python3 scan2.py ORDER EPS n0 [n0...]
"""
import sympy as sp
import sys, os
from fractions import Fraction as F

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
EXTRA = 12

def frac_of(expr, k0):
    v = expr.subs(k, sp.Rational(k0.numerator, k0.denominator))
    v = sp.nsimplify(v)
    return F(int(sp.fraction(v)[0]), int(sp.fraction(v)[1]))

def run(n0):
    sub = {n: sp.Integer(n0), e: sp.Integer(EPS)}
    rl = sp.cancel(r.subs(sub))
    # cells
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

    # shift expansion of each basis monomial at numeric n (symbolic in k)
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
    SHIFT = {m: shift_monomial_l(m) for m in BASIS}

    # universal denominators, cascading down in weight
    An, Ad = sp.fraction(sp.cancel(rl))
    uu = {}
    denshape = {}
    for m in BASIS:
        ds = sp.Integer(1)
        for i in range(ORDER + 1):
            if m in cells[i]:
                ds = sp.lcm(sp.Poly(ds, k), sp.Poly(sp.fraction(sp.cancel(cells[i][m]))[1], k)).as_expr()
        for mprev in BASIS:
            if mprev == m or mprev not in uu:
                continue
            cc = SHIFT[mprev].get(m)
            if cc is not None:
                dd = sp.expand(sp.fraction(sp.cancel(rl * cc))[1] * uu[mprev].subs(k, k + 1))
                ds = sp.lcm(sp.Poly(ds, k), sp.Poly(dd, k)).as_expr()
        denshape[m] = ds
        A = sp.expand(DIAGSIGN[m] * An * ds); B = sp.expand(-Ad * ds)
        uu[m] = univ_denominator(A, B, J=ORDER + 12)

    nz = {m: sp.Poly(uu[m], k).degree() + EXTRA + 1 for m in BASIS}
    cols = []          # (kind, m, idx)
    for i in range(ORDER + 1):
        cols.append(('p', i, 0))
    for m in BASIS:
        for j in range(nz[m]):
            cols.append(('z', m, j))
    ncols = len(cols)
    colindex = {c: i for i, c in enumerate(cols)}

    # sample points
    NS = 90
    rows = []
    for m in BASIS:
        # identity for sector m:
        #   diag * r(k) * phi_m(k+1) - phi_m(k)
        # + sum_{m'} r(k) * SHIFT[m'][m](k) * phi_{m'}(k+1)   (m' != m)
        # - sum_i p_i cells[i][m](k)  = 0
        um = uu[m]; um1 = um.subs(k, k + 1)
        senders = [(mp, sp.cancel(rl * SHIFT[mp][m])) for mp in BASIS
                   if mp != m and m in SHIFT[mp]]
        diag_extra = sp.cancel(rl * (SHIFT[m][m] - DIAGSIGN[m]))
        assert diag_extra == 0
        for t in range(NS):
            k0 = F(3*t + 1, 3)
            row = [F(0)] * ncols
            umv = frac_of(um, k0); um1v = frac_of(um1, k0)
            rv = frac_of(rl, k0)
            for j in range(nz[m]):
                kp = k0 + 1
                row[colindex[('z', m, j)]] += DIAGSIGN[m] * rv * (kp**j) / um1v - (k0**j) / umv
            for mp, coup in senders:
                cv = frac_of(coup, k0)
                ump1 = frac_of(uu[mp].subs(k, k + 1), k0)
                for j in range(nz[mp]):
                    row[colindex[('z', mp, j)]] += cv * ((k0 + 1)**j) / ump1
            for i in range(ORDER + 1):
                if m in cells[i]:
                    row[colindex[('p', i, 0)]] -= frac_of(cells[i][m], k0)
            rows.append(row)

    # exact nullspace via Gaussian elimination
    mat = [row[:] for row in rows]
    pivots = {}
    prow = 0
    for c in range(ncols):
        pr = None
        for rr in range(prow, len(mat)):
            if mat[rr][c] != 0:
                pr = rr; break
        if pr is None:
            continue
        mat[prow], mat[pr] = mat[pr], mat[prow]
        pv = mat[prow][c]
        mat[prow] = [x / pv for x in mat[prow]]
        for rr in range(len(mat)):
            if rr != prow and mat[rr][c] != 0:
                f = mat[rr][c]
                mat[rr] = [a - f * b for a, b in zip(mat[rr], mat[prow])]
        pivots[c] = prow
        prow += 1
    freecols = [c for c in range(ncols) if c not in pivots]
    print('n=%d: nullspace dim %d' % (n0, len(freecols)))
    for fc in freecols:
        vec = [F(0)] * ncols
        vec[fc] = F(1)
        for c, pr in pivots.items():
            vec[c] = -mat[pr][fc]
        pvals = [vec[colindex[('p', i, 0)]] for i in range(ORDER + 1)]
        print('   free col %s -> p = %s' % (cols[fc], pvals))

for n0 in NVALS:
    run(n0)
