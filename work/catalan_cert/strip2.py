import sympy as sp, pickle, sys
n, k, e = sp.symbols('n k e')
data = pickle.load(open('final_certificate.pkl','rb'))
Hn, H2n, K12n, K22n = sp.symbols('Hn H2n K12n K22n')
ALPH = (Hn, H2n, K12n, K22n)

def chi_shift(j):
    if j % 2 == 0: return 0
    return e * (-1)**((j - 1) // 2)

def lin(base, extra):     # dict {alphabet monomial: coeff} for letter+rational
    return {base: sp.Integer(1), (0,0,0,0): extra}

def dmul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = tuple(x + y for x, y in zip(ma, mb))
            out[m] = out.get(m, 0) + ca * cb
    return out

def dscale(a, f):
    return {m: c * f for m, c in a.items()}

def dadd(a, b):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, 0) + c
    return out

def Hn_at(t):   return lin((1,0,0,0), sum(sp.Rational(1)/(n+j) for j in range(1, t+1)))
def H2n_at(t):  return lin((0,1,0,0), sum(sp.Rational(1)/(2*n+j) for j in range(1, 2*t+1)))
def K12n_at(t): return lin((0,0,1,0), sum(chi_shift(j)/(2*n+j) for j in range(1, 2*t+1)))
def K22n_at(t): return lin((0,0,0,1), sum(chi_shift(j)/(2*n+j)**2 for j in range(1, 2*t+1)))
def K1const(m):
    tot = sp.Rational(0)
    for j in range(1, 2*m+1):
        c = 0 if j%2==0 else (1 if j%4==1 else -1)
        tot += sp.Rational(c, j)
    return tot

def Cbin_ratio(d, t):
    c1 = (sp.Integer(1) * sp.prod([n + t + j for j in range(1, d - t + 1)])) / sp.factorial(d - t)
    c2 = (sp.Integer(1) * sp.prod([2*n + j for j in range(1, 2*t+1)])) / (sp.Integer(1) * sp.prod([(n + j)**2 for j in range(1, t+1)]))
    c3 = sp.binomial(2*(d - t), d - t)
    return sp.cancel(c1 * c2 * c3)

def w_at(N_off, t):
    A = dadd(dscale(Hn_at(t), sp.Rational(3,4)), dscale(H2n_at(t), sp.Rational(-1,2)))
    Bm = dadd(K12n_at(t), {(0,0,0,0): -K1const(N_off - t)})
    return dadd(dscale(K22n_at(t), sp.Rational(1,2)), dmul(A, Bm))

def cell_strip(i, t):
    tot = {}
    if t <= i + 1:
        tot = dadd(tot, dscale(w_at(i+1, t), (n+i+1)**2 * Cbin_ratio(i+1, t)))
    if t <= i:
        tot = dadd(tot, dscale(w_at(i, t), -(12*(n+i)**2 + 12*(n+i) + 4) * Cbin_ratio(i, t)))
    if t <= i - 1:
        tot = dadd(tot, dscale(w_at(i-1, t), 32*(n+i)**2 * Cbin_ratio(i-1, t)))
    return tot

for EPS in (1, -1):
    PV = data[EPS]['PV']; cert = data[EPS]['cert']
    total = {}
    for i in range(5):
        for t in range(0, i + 2):
            total = dadd(total, dscale(cell_strip(i, t), PV[i]))
    for m, c in cert.items():
        if m[4]:
            continue
        cv = sp.cancel(c.subs(k, n))
        mono = (m[1], m[2], m[3], m[5])
        sgn = EPS**m[0]
        total = dadd(total, {mono: sgn * cv})
    total = {m: c.subs(e, EPS) if hasattr(c, 'subs') else c for m, c in total.items()}
    ok = True
    for m, c in sorted(total.items()):
        cc = sp.cancel(sp.together(c))
        if cc != 0:
            ok = False
            print('parity %+d: NONZERO at %s: %s' % (EPS, m, sp.factor(cc)))
    # Psi(n,0):
    p0c = sum(sp.cancel(c.subs(k, 0)) for m, c in cert.items()
              if not any(m[1:]) )
    print('parity %+d: Psi(n,0)/S = %s ; strip identity %s'
          % (EPS, sp.cancel(p0c), 'HOLDS' if ok else 'FAILS'))
    sys.stdout.flush()
