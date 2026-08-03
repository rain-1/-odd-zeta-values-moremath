"""
Stage 2: scalar pre-operator route for the Catalan companion certificate.

Direct telescoping of the cell fails in the (s*Hk, s*H2) sector (see
certificate.py).  Following work/z2cf/lean_certificate.py, seek
    P = p0(n) + p1(n) E + p2(n) E^2      (E : n -> n+1)
such that  sum_i p_i(n) C(n+i,k)  telescopes cellwise:
    Psi(n,k+1) - Psi(n,k) = sum_i p_i(n) C(n+i,k).
Summing over k then gives  p2 g(n+2) + p1 g(n+1) + p0 g(n) = 0  for the defect
g(n) = (n+1)^2 B(n+1) - (12n^2+12n+4) B(n) + 32 n^2 B(n-1); with g(1)=g(2)=0
and p2 nonvanishing this forces g == 0.

All solves are linear: p_i enter the obstructed-sector equations linearly and
are determined jointly with the certificate cofactors.
"""
import sympy as sp
import pickle, sys, os

SP = os.path.dirname(os.path.abspath(__file__)) + '/'
src = open(SP + 'certificate.py').read()
# reuse the algebra + cell + solver up to (not including) the graded solve
exec(src.split("# ---------------------------------------------------------------- graded solve")[0])

ORDER = int(sys.argv[1]) if len(sys.argv) > 1 else 2
ps = sp.symbols('p0:%d' % (ORDER + 1))

# S(n+i,k)/S(n,k)
def sig(i):
    out = sp.Integer(1)
    for t in range(i):
        out *= rho_p.subs(n, n + t)
    return sp.cancel(out)

# rebase element from letters at (n+i) to letters at n: only K1b moves.
# K1b(n+i) = K1b(n) + s*e*sum_{t=0}^{i-1} (-1)^t/(2n-2k+2t+1)
def rebase(el, i):
    if i == 0:
        return el
    delta = sum((-1)**t * sp.Rational(1) / (2*n - 2*k + 2*t + 1) for t in range(i))
    out = {}
    for m, c in el.items():
        if m[4] == 0:
            out[m] = out.get(m, 0) + c
        else:
            out[m] = out.get(m, 0) + c
            m0 = ((m[0] + 1) % 2,) + m[1:4] + (0,) + (m[5],)
            out[m0] = out.get(m0, 0) + c * e * delta
    return {m: sp.cancel(c) for m, c in out.items() if sp.cancel(c) != 0}

def cell_at(i):
    """C(n+i,k)/S(n,k) as an element in base letters at (n,k)."""
    el = {m: sp.cancel(c.subs(n, n + i).subs(e, (-1)**i * e)) for m, c in CELL.items()}
    el = rebase(el, i)
    return escale(el, sig(i))

CELLS = [cell_at(i) for i in range(ORDER + 1)]

# ---- sequential graded solve, per shift i, deferring obstructed monomials ----
OBSTRUCTED = {(1, 1, 0, 0, 0, 0), (1, 0, 1, 0, 0, 0)}

def graded_reduce(cellel, tag):
    """peel solvable monomials from the top; return (cert_dict, residual)."""
    residual = dict(cellel)
    cert = {}
    while residual:
        solvable = [m for m in residual if m not in OBSTRUCTED]
        if not solvable:
            break
        m = max(solvable, key=weight)
        # never solve a lower-weight monomial while an obstructed one of higher
        # or equal weight still has unresolved couplings INTO it -- couplings go
        # downward in weight, and obstructed ones are weight 1, so only solve
        # weight <=1 non-obstructed after obstructed handled.  Here we defer any
        # monomial of weight < 1?  Couplings from obstructed (weight-1) go to
        # weight-0; defer those too.
        if weight(m) < 1 or (weight(m) == 1 and any(weight(mo) > 1 for mo in residual if mo in OBSTRUCTED)):
            pass
        if weight(m) <= 0 or weight(m) == 1:
            # defer everything at weight <= 1 that could still receive couplings
            # from the obstructed sector solved later
            break
        g = residual.pop(m)
        diag = -1 if m[0] else 1
        phi = solve_first_order(diag, g)
        assert phi is not None, (tag, m)
        cert[m] = phi
        contrib = delta_of(phi, m)
        contrib.pop(m, None)
        for mm, cc in contrib.items():
            residual[mm] = sp.cancel(residual.get(mm, 0) - cc)
            if residual[mm] == 0:
                residual.pop(mm)
    return cert, residual

def delta_of(cm, m):
    shifted = shift_element({m: cm})
    return eadd(escale(shifted, r), {m: -cm})

certs = []
residuals = []
for i, cel in enumerate(CELLS):
    c_, res_ = graded_reduce(cel, 'cell%d' % i)
    certs.append(c_)
    residuals.append(res_)
    print('cell%d: solved %d weight-2 monomials; residual monomials %s'
          % (i, len(c_), sorted(res_, key=weight, reverse=True)))

# combined residual with unknown p_i
combined = {}
for i, res_ in enumerate(residuals):
    for m, c in res_.items():
        combined[m] = combined.get(m, 0) + ps[i] * c

print('\ncombined residual monomials:', sorted(combined, key=weight, reverse=True))
pickle.dump({'ps': ps, 'certs': certs, 'combined': {m: sp.together(c) for m, c in combined.items()},
             'ORDER': ORDER},
            open(SP + 'stage2_state.pkl', 'wb'))
print('state saved.')
