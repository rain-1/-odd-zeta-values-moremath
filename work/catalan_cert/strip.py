"""
Boundary strip identity: with literal (combinatorial) shells,
   sum_{k=0}^{infty} sum_{i=0}^{4} p_i(n) C(n+i,k)
 = Psi(n,n)  +  sum_{t>=0} [rhs at k=n+t]   (telescoping over k=0..n-1)
and the claim is that this total vanishes identically in n, per parity.
Everything at k=n+t reduces to the alphabet {Hn, H2n, K12n, K22n} with
rational(n) coefficients; we normalize by S(n,n)=C(2n,n) and check that every
monomial coefficient cancels.  sigma = (-1)^k at k=n+t is e*(-1)^t.
"""
import sympy as sp, pickle
n, k, e = sp.symbols('n k e')
data = pickle.load(open('final_certificate.pkl','rb'))

Hn, H2n, K12n, K22n = sp.symbols('Hn H2n K12n K22n')

def chi_shift(j):     # chi(2n+j) for j>=1 as multiple of e=(-1)^n
    if j % 2 == 0: return 0
    return e * (-1)**((j - 1) // 2)

def Hn_at(t):        # H_{n+t}
    return Hn + sum(sp.Rational(1, 1)/(n + j) for j in range(1, t + 1))
def H2n_at(t):       # H_{2n+2t}
    return H2n + sum(sp.Rational(1, 1)/(2*n + j) for j in range(1, 2*t + 1))
def K12n_at(t):      # K1_{2n+2t}
    return K12n + sum(chi_shift(j)/(2*n + j) for j in range(1, 2*t + 1))
def K22n_at(t):
    return K22n + sum(chi_shift(j)/(2*n + j)**2 for j in range(1, 2*t + 1))
def K1const(m):      # K1_{2m} for small m>=0 (exact rational, chi values literal)
    tot = sp.Rational(0)
    for j in range(1, 2*m + 1):
        c = 0 if j % 2 == 0 else (1 if j % 4 == 1 else -1)
        tot += sp.Rational(c, j)
    return tot

def Cbin_ratio(N, t):
    """S(N, n+t)/C(2n,n) for N = n+d (d=0..5), t<=d: product of rationals in n.
       S(N,K)=C(N,K)C(2K,K)C(2N-2K,N-K), K=n+t."""
    d = N  # here N is the offset: actual index n+d
    # C(n+d, n+t) = C(n+d, d-t): polynomial in n
    from sympy import binomial, Rational
    c1 = sp.binomial(n + d, d - t)  # sympy expands to poly/(d-t)!
    c1 = sp.simplify(sp.expand(sp.together(sp.gamma(n + d + 1)/(sp.gamma(n + t + 1)*sp.gamma(d - t + 1)))))
    # C(2n+2t, n+t)/C(2n, n) = prod_{j=1}^{2t}(2n+j) / prod_{j=1}^{t}(n+j)^2
    c2 = sp.prod([2*n + j for j in range(1, 2*t + 1)]) / sp.prod([(n + j)**2 for j in range(1, t + 1)])
    c3 = sp.binomial(2*(d - t), d - t)   # constant
    return sp.cancel(c1 * c2 * c3)

def w_at(N_off, t):
    """w(n+N_off, n+t) in the alphabet; K1b = K1_{2(N_off-t)} constant."""
    return (sp.Rational(1,2)*K22n_at(t)
            + (sp.Rational(3,4)*Hn_at(t) - sp.Rational(1,2)*H2n_at(t))
              * (K12n_at(t) - K1const(N_off - t)))

def cell_at_strip(i, t):
    """C(n+i, n+t)/C(2n,n): three shell terms, keep only supported ones."""
    tot = sp.Integer(0)
    # term S(n+i+1, n+t): supported iff t <= i+1
    if t <= i + 1:
        tot += (n + i + 1)**2 * Cbin_ratio(i + 1, t) * w_at(i + 1, t)
    if t <= i:
        tot -= (12*(n + i)**2 + 12*(n + i) + 4) * Cbin_ratio(i, t) * w_at(i, t)
    if t <= i - 1:
        tot += 32*(n + i)**2 * Cbin_ratio(i - 1, t) * w_at(i - 1, t)
    return sp.expand(tot)

MONS = [(0,0,0,0)] + [(1,0,0,0),(0,1,0,0),(0,0,1,0)] + [(0,0,0,1),(2,0,0,0),(1,1,0,0),(1,0,1,0),(0,2,0,0),(0,1,1,0),(0,0,2,0)]
def coeffs_in_alphabet(expr):
    expr = sp.expand(expr)
    d = {}
    poly = sp.Poly(expr, Hn, H2n, K12n, K22n)
    for mono, c in poly.terms():
        d[mono] = d.get(mono, 0) + c
    return d

for EPS in (1, -1):
    PV = data[EPS]['PV']; cert = data[EPS]['cert']
    total = sp.Integer(0)
    for i in range(5):
        for t in range(0, i + 2):
            total += PV[i] * cell_at_strip(i, t).subs(e, EPS)
    # Psi(n,n) = S(n,n) * sum_m c_m(n,n) letters(k=n); K1b(k=n)=0, sigma=e
    psi_nn = sp.Integer(0)
    for m, c in cert.items():
        if m[4]:      # contains K1b -> 0
            continue
        cv = sp.cancel(c.subs(k, n))
        lv = (EPS**m[0]) * Hn**m[1] * H2n**m[2] * K12n**m[3] * K22n**m[5]
        psi_nn += cv * lv
    # check Psi(n,0) == 0 as well: only weight-0 sigma monomial survives
    psi_0 = sp.Integer(0)
    for m, c in cert.items():
        if m[1] or m[2] or m[3] or m[5] or m[4]:
            continue
        psi_0 += sp.cancel(c.subs(k, 0))
    print('parity %+d: Psi(n,0) coefficient = %s' % (EPS, sp.cancel(psi_0)))
    grand = sp.expand(sp.together(total + psi_nn))
    grand = sp.cancel(sp.together(grand))
    cd = coeffs_in_alphabet(sp.expand(grand))
    allzero = True
    for mono, c in cd.items():
        cc = sp.cancel(sp.together(c))
        if cc != 0:
            allzero = False
            print('  parity %+d: NONZERO coeff at %s: %s' % (EPS, mono, sp.factor(cc)))
    print('parity %+d: strip + Psi(n,n) identity:' % EPS, 'HOLDS' if allzero else 'FAILS')
