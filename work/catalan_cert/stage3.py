"""
Stage 3: joint solve of the obstructed sector, determining the pre-operator.
"""
import sympy as sp
import pickle, os, sys

SP = os.path.dirname(os.path.abspath(__file__)) + '/'
src = open(SP + 'certificate.py').read()
exec(src.split("# ---------------------------------------------------------------- graded solve")[0])

st = pickle.load(open(SP + 'stage2_state.pkl', 'rb'))
ps = st['ps']; combined = st['combined']; ORDER = st['ORDER']

def delta_of(cm, m):
    shifted = shift_element({m: cm})
    return eadd(escale(shifted, r), {m: -cm})

SHK = (1, 1, 0, 0, 0, 0); SH2 = (1, 0, 1, 0, 0, 0)

# ---- joint homogeneous solve for (phi_SHK, phi_SH2, p) --------------------
def build_eq(diag, phi_num_coeffs, u, g):
    """polynomial identity for  diag*r*phi(k+1) - phi(k) = g, phi = z/u."""
    z = sum(c * k**i for i, c in enumerate(phi_num_coeffs))
    lhs = sp.together(diag * r * z.subs(k, k + 1) / u.subs(k, k + 1) - z / u - g)
    return sp.fraction(sp.cancel(lhs))[0]

# universal denominator: from the diagonal equation A phi(k+1) + B phi(k) = ...
# with denominators of g folded in.
def univ_for(diag, g):
    An, Ad = sp.fraction(sp.cancel(diag * r))
    Gn, Gd = sp.fraction(sp.cancel(sp.together(g)))
    A = sp.expand(An * Gd); B = sp.expand(-Ad * Gd)
    return univ_denominator(A, B)

gK = combined[SHK]; gH = combined[SH2]
uK = univ_for(-1, gK); uH = univ_for(-1, gH)
print('universal denominators:')
print('  sHk:', sp.factor(uK))
print('  sH2:', sp.factor(uH))

DZ = 14
zK = sp.symbols('a0:%d' % DZ); zH = sp.symbols('b0:%d' % DZ)
eqK = build_eq(-1, zK, uK, gK)
eqH = build_eq(-1, zH, uH, gH)

unknowns = list(zK) + list(zH) + list(ps)
eqs = []
for eq in (eqK, eqH):
    eqs += [sp.cancel(c) for c in sp.Poly(sp.expand(eq), k).all_coeffs()]
sol = sp.solve([sp.Eq(c, 0) for c in eqs], unknowns, dict=True)
print('solution branches:', len(sol))
s0 = sol[0]
psol = [sp.cancel(sp.Symbol(str(p)).subs(s0)) for p in ps]
print('p (unnormalized):')
for i, p in enumerate(psol):
    print('  p%d =' % i, sp.factor(p))
free = sorted({f for p in psol for f in p.free_symbols if str(f)[0] in 'abp'},
              key=str)
print('free symbols in p:', free)
pickle.dump({'sol': s0, 'zK': zK, 'zH': zH, 'uK': uK, 'uH': uH, 'ps': ps},
            open(SP + 'stage3_state.pkl', 'wb'))
