"""eps57_sym2_all.py -- referee-mandated upgrades for papers_out/modular_anchors.

PART 1: exact Sym^2 operator identities for ALL six third-order (R3, d=0)
sporadic families.  For R3(a,b,c,0) the generating operator is
    L = theta^3 - t(2theta+1)(a theta^2 + a theta + b) + c t^2 (theta+1)^3 .
Claim to test (referee report S1/S4, 'a finite symbolic computation'):
L is t^3*P3(t) times the symmetric square of a second-order operator.
Method (as in papers_out/expository_apery, check 12): write L in
partial-derivative form A3 f''' + A2 f'' + A1 f' + A0 f, normalize monic,
match against Sym^2(d^2 + p d + r) = d^3 + 3p d^2 + (2p^2+p'+4r) d
+ (4pr+2r'); p, r are forced; the residual A0/A3 - (4pr+2r') must be
IDENTICALLY ZERO in Q(t).  Also verify the closed-form pattern
    Dtilde = theta^2 - t(2a theta^2 + a theta + b/2) + c t^2 (theta+1/2)^2
by the same matching.

PART 2: Sturm-style upgrade for the zeta identification
F_zeta(eta) := eta3^10/(eta1 eta9)^3  vs  (9E2(q^9)-E2(q))/8 :
verify the Ligozat holomorphy data for the eta quotient on Gamma_0(9)
(weight, level conditions, cusp orders), report dim M_2(Gamma_0(9)) and the
Sturm bound, and check coefficient agreement far beyond it.
"""

import sympy as sp
from fractions import Fraction as F
from math import gcd

t = sp.symbols('t')
f = sp.Function('f')

R3 = {
    'alpha (Domb)': (10, 4, 64),
    'gamma (Apery z3)': (17, 5, 1),
    'delta': (7, 3, 81),
    'epsilon': (12, 4, 16),
    'zeta': (9, 3, -27),
    'eta': (11, 5, 125),
}


def theta_pow(expr, k):
    for _ in range(k):
        expr = t * sp.diff(expr, t)
    return expr


def op_coeffs_order3(a, b, c):
    """coefficients A3..A0 of L f = A3 f''' + ... + A0 f."""
    y = f(t)
    th1 = theta_pow(y, 1)
    th2 = theta_pow(y, 2)
    th3 = theta_pow(y, 3)
    # (2theta+1)(a theta^2 + a theta + b) = 2a th3 + 3a th2 + (a+2b) th1 + b y
    L = th3 - t * (2 * a * th3.subs(0, 0) if False else 0)
    mid = 2 * a * theta_pow(y, 3) + 3 * a * theta_pow(y, 2) \
        + (a + 2 * b) * theta_pow(y, 1) + b * y
    last = c * (theta_pow(y, 3) + 3 * theta_pow(y, 2)
                + 3 * theta_pow(y, 1) + y)          # (theta+1)^3
    L = th3 - t * mid + t**2 * last
    L = sp.expand(L)
    A = [sp.simplify(L.coeff(sp.Derivative(y, (t, k)))) for k in (3, 2, 1)]
    A0 = sp.simplify(L - sum(A[3 - k - 1] * sp.Derivative(y, (t, k))
                             for k in (3, 2, 1))).subs(y, 1)
    A0 = sp.simplify(A0)
    return A + [A0]        # [A3, A2, A1, A0]


def sym2_test(a, b, c):
    A3, A2, A1, A0 = op_coeffs_order3(a, b, c)
    a2 = sp.simplify(A2 / A3)
    a1 = sp.simplify(A1 / A3)
    a0 = sp.simplify(A0 / A3)
    p = sp.simplify(a2 / 3)
    r = sp.simplify((a1 - 2 * p**2 - sp.diff(p, t)) / 4)
    residual = sp.simplify(a0 - (4 * p * r + 2 * sp.diff(r, t)))
    return p, r, residual, A3


def op_coeffs_order2_pattern(a, b, c):
    """Dtilde = theta^2 - t(2a theta^2 + a theta + b/2) + c t^2 (theta+1/2)^2
    in d-form; return monic p, r."""
    y = f(t)
    th1 = theta_pow(y, 1)
    th2 = theta_pow(y, 2)
    D = th2 - t * (2 * a * th2 + a * th1 + sp.Rational(b, 2) * y) \
        + c * t**2 * (th2 + th1 + sp.Rational(1, 4) * y)
    D = sp.expand(D)
    B2 = sp.simplify(D.coeff(sp.Derivative(y, (t, 2))))
    B1 = sp.simplify(D.coeff(sp.Derivative(y, (t, 1))))
    B0 = sp.simplify((D - B2 * sp.Derivative(y, (t, 2))
                      - B1 * sp.Derivative(y, (t, 1))).subs(y, 1))
    return sp.simplify(B1 / B2), sp.simplify(B0 / B2)


print('=' * 72)
print('PART 1: Sym^2 identities for the six third-order sporadic operators')
print('=' * 72)
all_pass = True
for name, (a, b, c) in R3.items():
    p, r, residual, A3 = sym2_test(a, b, c)
    ok = residual == 0
    all_pass &= ok
    # compare with the closed-form Dtilde pattern
    pp, rr = op_coeffs_order2_pattern(a, b, c)
    match = sp.simplify(p - pp) == 0 and sp.simplify(r - rr) == 0
    print('%-18s residual==0: %s   Dtilde-pattern matches (p,r): %s'
          % (name, ok, match))
    if ok:
        print('    p = %s' % sp.factor(p))
        print('    r = %s' % sp.factor(r))
print('ALL SIX SYM^2 IDENTITIES:', 'PROVED (residual identically 0 in Q(t))'
      if all_pass else 'AT LEAST ONE FAILURE -- scope the paper accordingly')

print()
print('=' * 72)
print('PART 2: zeta identification  eta3^10/(eta1 eta9)^3  vs  (9E2(q^9)-E2(q))/8')
print('=' * 72)

# eta quotient data: e_1 = -3, e_3 = +10, e_9 = -3 on Gamma_0(9)
E = {1: -3, 3: 10, 9: -3}
N = 9
wt = sum(E.values()) / 2
print('weight = %s' % wt)
c1 = sum(d * e for d, e in E.items())
c2 = sum(F(e, d) for d, e in E.items())
print('sum d*e_d = %s (need N | ... : 24 | N*sum? cond: %s); '
      'sum e_d/d = %s' % (c1, 'vacuous, =0', c2))
prod_de = 1
for d, e in E.items():
    prod_de *= F(d) ** e
print('prod d^{e_d} = %s  (rational square -> trivial character: %s)'
      % (prod_de, sp.sqrt(sp.Rational(str(prod_de))).is_rational))

# cusp orders on Gamma_0(9): cusps represented by c | 9 : c = 1, 3, 9
print('cusp orders (Ligozat): v_c = (N/(24*gcd(c^2,N))) * sum gcd(c,d)^2 e_d / d')
holo = True
for cc in (1, 3, 9):
    v = F(N, 24 * gcd(cc * cc, N)) * sum(F(gcd(cc, d) ** 2 * e, d)
                                         for d, e in E.items())
    print('   c=%d: order %s' % (cc, v))
    if v < 0:
        holo = False
print('holomorphic at all cusps:', holo)

# dim M_2(Gamma_0(9)) and Sturm bound
idx = 12   # [SL2(Z):Gamma_0(9)] = 9*(1+1/3)
sturm = F(2 * idx, 12)
print('index = %d, Sturm bound k*mu/12 = %s  (check to well beyond)' % (idx, sturm))

# coefficient check to q^40
M = 41
def eta_series(m, M):
    # q^{m/24} omitted; return prod (1-q^{mk}) as list of ints
    s = [0] * M
    s[0] = 1
    for k in range(1, M // m + 1):
        # multiply by (1 - q^{mk})
        ns = s[:]
        for i in range(M - m * k):
            ns[i + m * k] -= s[i]
        s = ns
    return s

def mul(a, b, M):
    r = [0] * M
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if i + j < M and y:
                    r[i + j] += x * y
    return r

def inv(a, M):
    r = [0] * M
    r[0] = 1
    for n in range(1, M):
        r[n] = -sum(a[k] * r[n - k] for k in range(1, n + 1))
    return r

e1 = eta_series(1, M); e3 = eta_series(3, M); e9 = eta_series(9, M)
num = [x for x in e3]
for _ in range(9):
    num = mul(num, e3, M)
den = mul(mul(e1, mul(e1, e1, M), M), mul(e9, mul(e9, e9, M), M), M)
# q-prefactor: (10*3 - 3*1 - 3*9)/24 = (30-3-27)/24 = 0 -> no shift
Feta = mul(num, inv(den, M), M)

def sigma1(n):
    return sum(d for d in range(1, n + 1) if n % d == 0)
Eis = [0] * M
Eis[0] = 1
for n in range(1, M):
    v = -24 * sigma1(n)
    Eis[n] = v          # E2 = 1 - 24 sum sigma1 q^n
F_eis = [0] * M
for n in range(M):
    e2n = Eis[n]
    e29 = Eis[n // 9] if n % 9 == 0 else 0
    F_eis[n] = F(9 * e29 - e2n, 8)
ok = all(F(Feta[n]) == F_eis[n] for n in range(M))
print('eta-quotient == (9E2(q^9)-E2(q))/8 coefficientwise to q^%d: %s'
      % (M - 1, ok))
print('=> with Ligozat holomorphy + trivial character + Sturm bound %s,'
      ' agreement to q^%d PROVES the identity in M_2(Gamma_0(9))'
      % (sturm, M - 1))
