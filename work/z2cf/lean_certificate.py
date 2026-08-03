"""
Exact certificate for the LEAN proof of the minimal Apery zeta(2) companion formula.

    B_n = (1/5) sum_k S(n,k) [ H^(2)_n + H_k (2H_k - H_{n-k} - H_n) ],
    S(n,k) = C(n,k)^2 C(n+k,k).

Run with:

    python3 work/z2cf/lean_certificate.py

Every displayed CHECK must be zero / True.  All arithmetic is exact (sympy rationals and
polynomials, and Python Fractions for the cellwise audit).  No floating point is used.

--------------------------------------------------------------------------------------
WHY THIS FILE EXISTS
--------------------------------------------------------------------------------------
`work/z2cf/parameter_proof.mac` proves the formula by a two-parameter creative telescope
plus an Ore-operator elimination.  That route is not directly formalizable: it needs
generic parameters (u,v), an order-three operator, and right division in an Ore algebra.

This file certifies an equivalent *finite, scalar* route designed for Lean:

  (0) There is NO single telescope.  Splitting the cell identity along the letter
      monomials forces the coefficients of H_k^2, H_k H_{n-k}, H_k H_n, H^(2)_n in the
      antidifference to be 2X, -X, -X, X for the unique X with Delta_k(S X) = L[S(.,k)];
      the H_{n-k} and H_n components then both require a rational solution of
          r(k) phi(k+1) - phi(k) = rho(n,k+1)/(k+1),   r(k) = S(n,k+1)/S(n,k),
      and Gosper's algorithm certifies that none exists.  (CHECK 0 below.)

  (1) Applying first the SCALAR order-two pre-operator P = p0 + p1 E + p2 E^2 below,
      the combination DOES telescope cellwise, with antidifference

          Psi(n,k) = W(n,k) w(n,k) + S(n,k) ( beta H_k + gamma (H_{n-k} + H_n) + alpha ),
          W(n,k)   = sum_{i=0}^{2} p_i(n) G(n+i+1,k),

      G the zeta(2) Zeilberger certificate and alpha,beta,gamma the explicit rational
      functions emitted below.

  (2) Summing gives a scalar order-two recurrence for the defect E_m = (L D)_{m+1},
      D_n = sum_k S(n,k) w(n,k).  With E_0 = E_1 = 0 and p2 never vanishing, E == 0,
      hence L D = 0, hence D = 5B.

The Lean development is `lean/ZetaLucas/Z2Shell.lean` (stage 1) and
`lean/ZetaLucas/Z2Minimal.lean` (stage 2).
"""
import sympy as sp
from fractions import Fraction as F
from math import comb
import os
import pickle

n, k = sp.symbols('n k')

rho = lambda N, K: K**2 + K*(1 + 6*N) - 4 - 15*N - 11*N**2
Pz = lambda x: 11*x**2 + 11*x + 3
Qz = lambda x: 625*x**4 + 7250*x**3 + 31245*x**2 + 59264*x + 41752

# ---------------------------------------------------------------- the pre-operator
p = [sp.expand((n + 1)*(n + 2)*Qz(n)),
     sp.expand(6875*n**6 + 100375*n**5 + 597195*n**4 + 1849309*n**3
               + 3136850*n**2 + 2758284*n + 981880),
     sp.expand(-(n + 3)*(n + 4)*Qz(n - 1))]

# ------------------------------------------------------------- shell ratios at (n,k)
r = (n - k)**2*(n + k + 1)/(k + 1)**3            # S(n,k+1)/S(n,k)


def sig(j):                                       # S(n+j,k)/S(n,k)
    e = sp.Integer(1)
    for t in range(1, j + 1):
        e *= (n + t)*(n + t + k)/(n + t - k)**2
    return e


# forward Apery operator at index n:  (L u)_{n+1} = sum_j Lc[j] u_{n+j}
Lc = [-(n + 1)**2, -Pz(n + 1), (n + 2)**2]
m_ = []
for j in range(5):
    e = sp.Integer(0)
    for i in range(3):
        if 0 <= j - i <= 2:
            e += p[i]*Lc[j - i].subs(n, n + i)
    m_.append(sp.expand(e))

chi = sp.cancel(sum(p[i]*sig(i + 1)*k**3*rho(n + i + 1, k)
                    / ((n + i + 2 - k)**2*(n + i + 1 + k)) for i in range(3)))
chip = sp.cancel(chi.subs(k, k + 1))
Sig = sp.cancel(sum(m_[j]*sig(j) for j in range(5)))

s1 = lambda j: sum(sp.Integer(1)/(n + t - k) for t in range(1, j + 1))
tt = lambda j: sum(sp.Integer(1)/(n + t) for t in range(1, j + 1))
s2 = lambda j: sum(sp.Integer(1)/(n + t)**2 for t in range(1, j + 1))
A1 = sp.cancel(-sum(m_[j]*sig(j)*(s1(j) + tt(j)) for j in range(5)))
A0 = sp.cancel(sum(m_[j]*sig(j)*s2(j) for j in range(5)))
u, v = 1/(k + 1), 1/(n - k)


# ------------------------------------------------------------------ solve a component
def solve(T, D, deg, tag):
    cs = sp.symbols('%s0:%d' % (tag, deg + 1))
    phi = sum(cs[i]*k**i for i in range(deg + 1))/D
    e = sp.cancel(sp.together(r*phi.subs(k, k + 1) - phi - T))
    M, b = sp.linear_eq_to_matrix(sp.Poly(sp.expand(sp.numer(e)), k).all_coeffs(), cs)
    sol = sp.linsolve((M, b), cs)
    assert sol and sol is not sp.EmptySet, tag
    vals = list(sol)[0]
    free = set()
    for x in vals:
        free |= (set(x.free_symbols) & set(cs))
    vals = [sp.cancel(x.subs({f: 0 for f in free})) for x in vals]
    return sp.cancel(phi.subs(dict(zip(cs, vals))))


print("CHECK chi (Zeilberger antidifference of the pre-operated row) =",
      sp.simplify(r*chip - chi - Sig))

gamma = solve(sp.cancel(r*chip*u), ((n+1-k)*(n+2-k)*(n+3-k))**2, 9, 'g')
beta = solve(sp.cancel(A1 - 4*r*chip*u - r*chip*v),
             ((n+1-k)*(n+2-k)*(n+3-k)*(n+4-k))**3, 15, 'b')
Ta = sp.cancel(A0 - 2*r*chip*u**2 - r*chip*u*v
               - r*beta.subs(k, k+1)*u + r*gamma.subs(k, k+1)*v)
alpha = solve(Ta, ((n+1-k)*(n+2-k)*(n+3-k))**3*(n+4-k)**2, 14, 'a')

print("CHECK gamma component =",
      sp.simplify(r*gamma.subs(k, k+1) - gamma - sp.cancel(r*chip*u)))
print("CHECK beta  component =",
      sp.simplify(r*beta.subs(k, k+1) - beta
                  - sp.cancel(A1 - 4*r*chip*u - r*chip*v)))
print("CHECK alpha component =",
      sp.simplify(r*alpha.subs(k, k+1) - alpha - Ta))

# ------------------------------------------------- CHECK 0: no single telescope exists
# The H_{n-k} / H_n component of the *unpre-operated* problem is rho(n,k+1)/(k+1).
# Gosper (implemented below) certifies it is not Gosper-summable.
def gosper(R, kk, maxdeg=12):
    R = sp.cancel(sp.together(R))
    an, bd = sp.fraction(R)
    a, b = sp.Poly(sp.expand(an), kk), sp.Poly(sp.expand(bd), kk)
    pp, j = sp.Poly(1, kk), sp.Symbol('j')
    while True:
        res = sp.Poly(sp.expand(sp.resultant(a.as_expr(),
                                             b.as_expr().subs(kk, kk + j), kk)), j)
        Z = sorted([int(x) for x in sp.roots(res)
                    if getattr(x, 'is_Integer', False) and x >= 0])
        prog = False
        for jj in Z:
            g = sp.Poly(sp.gcd(a.as_expr(), b.as_expr().subs(kk, kk + jj)), kk)
            if g.degree() < 1:
                continue
            a = sp.Poly(sp.cancel(a.as_expr()/g.as_expr()), kk)
            b = sp.Poly(sp.cancel(b.as_expr()/g.as_expr().subs(kk, kk - jj)), kk)
            for i in range(1, jj + 1):
                pp = sp.Poly(sp.expand(pp.as_expr()*g.as_expr().subs(kk, kk - i)), kk)
            prog = True
            break
        if not prog:
            break
    A_, B_, P_ = a.as_expr(), b.as_expr(), pp.as_expr()
    for d in range(maxdeg + 1):
        cs = sp.symbols('q0:%d' % (d + 1))
        X = sum(cs[i]*kk**i for i in range(d + 1))
        eq = sp.expand(A_*X.subs(kk, kk + 1) - B_.subs(kk, kk - 1)*X - P_)
        M, bb = sp.linear_eq_to_matrix(sp.Poly(eq, kk).all_coeffs(), cs)
        sol = sp.linsolve((M, bb), cs)
        if not sol or sol is sp.EmptySet:
            continue
        vals = list(sol)[0]
        free = set()
        for x in vals:
            free |= (set(x.free_symbols) & set(cs))
        vals = [x.subs({f: 0 for f in free}) for x in vals]
        Xs = sp.expand(X.subs(dict(zip(cs, vals))))
        if Xs != 0:
            return sp.cancel(B_.subs(kk, kk - 1)*Xs/P_)
    return None


T0 = rho(n, k + 1)/(k + 1)
print("CHECK 0  no single telescope (Gosper returns None):",
      gosper(sp.cancel(r*T0.subs(k, k + 1)/T0), k) is None)

# ------------------------------------------------------ cellwise audit, Lean semantics
NUM, DEN = {}, {}
for tag, e in (('alpha', alpha), ('beta', beta), ('gamma', gamma)):
    a_, b_ = sp.fraction(sp.cancel(e))
    NUM[tag], DEN[tag] = sp.Poly(sp.expand(a_), k, n), sp.Poly(sp.expand(b_), k, n)

pf = [sp.lambdify(n, p[i], 'math') for i in range(3)]
pI = [sp.Poly(p[i], n) for i in range(3)]


def H(y, rr=1):
    return sum(F(1, j**rr) for j in range(1, y + 1))


def C(a, b):
    return comb(a, b) if 0 <= b <= a else 0


def S2(N, K):
    return C(N, K)**2 * C(N + K, K)


def wf(N, K):
    return H(N, 2) + H(K)*(2*H(K) - H(max(N - K, 0)) - H(N))


def rat(tag, N, K):                      # Lean's total division: x/0 = 0
    d = F(int(DEN[tag].eval({k: K, n: N})))
    return F(0) if d == 0 else F(int(NUM[tag].eval({k: K, n: N})))/d


def G(N, K):
    if N < 1:
        return F(0)
    return (F(C(N + 1, K)**2 * C(N - 1 + K, K), N**2*(N + 1)**2)
            * F(N)*F(K**3)*F(int(rho(N, K))))


def W(N, K):
    return sum(F(int(pI[i].eval(N)))*G(N + i + 1, K) for i in range(3))


def Psi(N, K):
    return (W(N, K)*wf(N, K)
            + F(S2(N, K))*(rat('beta', N, K)*H(K)
                           + rat('gamma', N, K)*(H(max(N - K, 0)) + H(N))
                           + rat('alpha', N, K)))


def summand(N, K):
    tot = F(0)
    for i in range(3):
        j = N + i
        tot += F(int(pI[i].eval(N)))*(
            F((j + 2)**2)*F(S2(j + 2, K))*wf(j + 2, K)
            - F(int(Pz(j + 1)))*F(S2(j + 1, K))*wf(j + 1, K)
            - F((j + 1)**2)*F(S2(j, K))*wf(j, K))
    return tot


gen_ok, bnd_ok, psi0_ok = True, True, True
for N in range(1, 11):
    psi0_ok &= (Psi(N, 0) == 0)
    for K in range(0, N):                                   # generic cells k <= n-1
        gen_ok &= (summand(N, K) == Psi(N, K + 1) - Psi(N, K))
    bnd_ok &= (Psi(N, N) - Psi(N, 0)
               + sum(summand(N, K) for K in range(N, N + 7)) == 0)
print("CHECK generic cells k<=n-1 (n<=10)      :", gen_ok)
print("CHECK Psi(n,0) = 0                      :", psi0_ok)
print("CHECK boundary closure at k=n..n+4      :", bnd_ok)

# ---------------------------------------------------------------- the theorem itself
B = [F(0), F(1)]
for N in range(1, 14):
    B.append((F(11*N*N + 11*N + 3)*B[N] + F(N*N)*B[N - 1])/F((N + 1)**2))
thm = all(sum(F(S2(N, K))*wf(N, K) for K in range(N + 1)) == 5*B[N]
          for N in range(0, 12))
print("CHECK minimal formula D_n = 5 B_n (n<=11):", thm)

# --------------------------------------------------------------- emit for Lean
HERE = os.path.dirname(os.path.abspath(__file__))
pickle.dump({t: sp.srepr(e) for t, e in
             (('chi', chi), ('gamma', gamma), ('beta', beta), ('alpha', alpha))},
            open(os.path.join(HERE, 'cert.pkl'), 'wb'))
out = os.path.join(HERE, 'cert_lean.txt')
with open(out, 'w') as fh:
    for tag, e in (('chi', chi), ('gamma', gamma), ('beta', beta), ('alpha', alpha)):
        a_, b_ = sp.fraction(sp.cancel(e))
        fh.write('-- %s\nnumerator:\n%s\n\ndenominator:\n%s\n\n%s\n\n'
                 % (tag, sp.factor(a_), sp.factor(b_), '-'*78))
print("certificate written to", out)
print("LEAN CERTIFICATE AUDIT COMPLETE")
