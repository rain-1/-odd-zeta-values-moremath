import sympy as sp

h = sp.symbols('h')
N = 9
Cs = sp.symbols('C0:%d' % (N + 2))

def Cval(k):
    return Cs[k]

def S(nn):
    return sum(sp.binomial(nn, k) * (-h) ** (nn - k) * Cval(k) for k in range(nn + 1))

def rec_lhs(k):
    return (k + 1) ** 2 * Cval(k + 1) - h * (3 * k ** 2 + 3 * k + 1) * Cval(k) + 3 * h ** 2 * k ** 2 * Cval(k - 1)

def trec_defect(nn):
    return sp.expand(nn ** 2 * S(nn) + h ** 3 * (nn - 2) * (nn - 1) * S(nn - 3) - (-h) ** (nn - 1))

for nn in range(3, 7):
    expr = trec_defect(nn)
    deg_h_bound = nn + 2
    us = {}
    combo = 0
    for k in range(1, nn):
        poly_c = 0
        for d in range(0, deg_h_bound + 1):
            u = sp.Symbol(f'u_{k}_{d}')
            us[(k, d)] = u
            poly_c += u * h ** d
        combo += poly_c * rec_lhs(k)
    # extra freedom: boundary terms p(h)*C0 + q(h)*(C1-1)
    for d in range(0, deg_h_bound + 1):
        u = sp.Symbol(f'p_{d}')
        us[('p', d)] = u
        combo += u * h ** d * Cval(0)
    for d in range(0, deg_h_bound + 1):
        u = sp.Symbol(f'q_{d}')
        us[('q', d)] = u
        combo += u * h ** d * (Cval(1) - 1)
    diff = sp.expand(expr - combo)
    polydiff = sp.Poly(diff, h, *Cs)
    eqs = [c for _, c in polydiff.terms()]
    unknowns = list(us.values())
    sol = sp.linsolve(eqs, unknowns)
    print(nn, 'num eqs', len(eqs), 'num unknowns', len(unknowns), 'solved:', sol != sp.EmptySet)

print()
print("=== extracting explicit certificate for n=6 ===")
nn = 6
expr = trec_defect(nn)
deg_h_bound = nn + 2
us = {}
combo = 0
for k in range(1, nn):
    poly_c = 0
    for d in range(0, deg_h_bound + 1):
        u = sp.Symbol(f'u_{k}_{d}')
        us[(k, d)] = u
        poly_c += u * h ** d
    combo += poly_c * rec_lhs(k)
for d in range(0, deg_h_bound + 1):
    u = sp.Symbol(f'p_{d}')
    us[('p', d)] = u
    combo += u * h ** d * Cval(0)
for d in range(0, deg_h_bound + 1):
    u = sp.Symbol(f'q_{d}')
    us[('q', d)] = u
    combo += u * h ** d * (Cval(1) - 1)
diff = sp.expand(expr - combo)
polydiff = sp.Poly(diff, h, *Cs)
eqs = [c for _, c in polydiff.terms()]
unknowns = list(us.values())
sol = list(sp.linsolve(eqs, unknowns))[0]
assign = dict(zip(unknowns, sol))
for k in range(1, nn):
    poly_c = sum(assign.get(us[(k, d)], 0) * h ** d for d in range(deg_h_bound + 1))
    poly_c = sp.factor(sp.expand(poly_c))
    if poly_c != 0:
        print(f'  c_{k}(h) =', poly_c)
pcoef = sp.factor(sp.expand(sum(assign.get(us[('p', d)], 0) * h ** d for d in range(deg_h_bound + 1))))
qcoef = sp.factor(sp.expand(sum(assign.get(us[('q', d)], 0) * h ** d for d in range(deg_h_bound + 1))))
print('  p(h) [coeff of C0] =', pcoef)
print('  q(h) [coeff of (C1-1)] =', qcoef)
