"""
Stage 4 (rewritten): complete the certificate with the order-2 pre-operator

    P = p0(n) + p1(n) E + p2(n) E^2,
    p0 = -16 n (n+1) (3n^3+14n^2+19n+7)
    p1 = -4 (2n^3+10n^2+14n+5)
    p2 = (n+2)^2 (3n^3+5n^2-1)

found in stage 3 (nullspace of the sign-sector solvability system; parity
independent).  Solve every sector sequentially with p fixed, keeping e = (-1)^n
symbolic, and save the complete certificate.
"""
import sympy as sp
import pickle, os

SP = os.path.dirname(os.path.abspath(__file__)) + '/'
src = open(SP + 'certificate.py').read()
exec(src.split("# ---------------------------------------------------------------- graded solve")[0])

p0 = -16*n*(n + 1)*(3*n**3 + 14*n**2 + 19*n + 7)
p1 = -4*(2*n**3 + 10*n**2 + 14*n + 5)
p2 = (n + 2)**2*(3*n**3 + 5*n**2 - 1)
PV = [p0, p1, p2]

def delta_of(cm, m):
    return eadd(escale(shift_element({m: cm}), r), {m: -cm})

def sig(i):
    out = sp.Integer(1)
    for t in range(i):
        out *= rho_p.subs(n, n + t)
    return sp.cancel(out)

def rebase(el, i):
    if i == 0:
        return el
    delta = sum((-1)**t * sp.Rational(1) / (2*n - 2*k + 2*t + 1) for t in range(i))
    out = {}
    for m, c in el.items():
        out[m] = out.get(m, 0) + c
        if m[4]:
            m0 = ((m[0] + 1) % 2,) + m[1:4] + (0,) + (m[5],)
            out[m0] = out.get(m0, 0) + c * e * delta
    return {m: sp.cancel(c) for m, c in out.items() if sp.cancel(c) != 0}

def cell_at(i):
    el = {m: sp.cancel(c.subs(n, n + i).subs(e, (-1)**i * e)) for m, c in CELL.items()}
    return escale(rebase(el, i), sig(i))

target = {}
for i in range(3):
    for m, c in cell_at(i).items():
        target[m] = sp.cancel(target.get(m, 0) + PV[i] * c)
target = {m: c for m, c in target.items() if c != 0}

cert = {}
residual = dict(target)
while residual:
    m = max(residual, key=lambda mm: (weight(mm), mm))
    g = residual.pop(m)
    diag = -1 if m[0] else 1
    phi = solve_first_order(diag, g, maxdeg_extra=10)
    assert phi is not None, ('OBSTRUCTION', m, sp.factor(sp.together(g)))
    cert[m] = phi
    contrib = delta_of(phi, m)
    chk = sp.cancel(contrib.pop(m) - g)
    assert chk == 0, ('diag mismatch', m)
    for mm, cc in contrib.items():
        residual[mm] = sp.cancel(residual.get(mm, 0) - cc)
        if residual[mm] == 0:
            residual.pop(mm)
    print('solved sector', m)

print('\nCERTIFICATE COMPLETE.  Cofactors:')
for m in sorted(cert, key=weight, reverse=True):
    print(' ', m, '=', sp.factor(cert[m]))
pickle.dump({'PV': PV, 'cert': cert}, open(SP + 'final_certificate.pkl', 'wb'))
print('saved final_certificate.pkl')
