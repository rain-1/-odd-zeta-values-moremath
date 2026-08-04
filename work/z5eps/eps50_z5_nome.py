"""eps50_z5_nome.py -- Golyshev-style modularity probe for the Brown-Zudilin
zeta(5) recurrence L_BZ itself.

The 4-term recurrence c0(n)Y_n + c1(n)Y_{n+1} + c2(n)Y_{n+2} + c3(n)Y_{n+3}=0
(work/lb5/core.py) gives, for U(t) = sum_n Y_n t^n, the operator
    L = sum_{j=0}^{3} t^j P_j(theta),   theta = t d/dt,
with  P0(x) = c3(x-3),  P1(x) = c2(x-2),  P2(x) = c1(x-1),  P3(x) = c0(x).
deg P0 = 9, so the ODE has order 9; its indicial polynomial at t=0 is
P0(x) = 2 x^5 (2x-1) a0(x-3):  exponent 0 with multiplicity FIVE, one
exponent 1/2, and the three (irrational) roots of a0(x-3).

Probe:
  (1) exponent structure (exact);
  (2) Frobenius pair inside the unipotent block: y0 = Q(t),
      y1 = y0 log t + g via L(g) = -L'(theta) y0; nome q = t exp(g/y0);
      invert; integrality profiles of t(q), F(q)=y0(t(q)) with rescalings;
  (3) root tests: are Q(t)^{1/2} (Sym^2 signal) or Q(t)^{1/4} (Sym^4 signal,
      the natural weight-5 shape) coefficient-integral after rescaling?
  (4) identification attempts only if a signal appears.
All arithmetic exact (Fraction).
"""

import sys
from fractions import Fraction as F

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import core
import sympy as sp
from eps48_modular_nome import (smul, sinv, sexp, srevert, compose,
                                eta_quot, N)

# ---------------- the operator ----------------
x = sp.symbols('x')
a0 = lambda z: 41218*z**3 + 198849*z**2 + 320790*z + 173057
P0 = sp.expand(2*x**5*(2*x - 1)*a0(x - 3))
B8 = (3874492*x**8 + 59373972*x**7 + 394148190*x**6 + 1481084196*x**5
      + 3447878810*x**4 + 5095855458*x**3 + 4673546679*x**2
      + 2433871008*x + 551502039)
B9 = (48802112*x**9 + 967468896*x**8 + 8488000862*x**7 + 43246197636*x**6
      + 140983768422*x**5 + 304912330849*x**4 + 437406946975*x**3
      + 401272692378*x**2 + 213593890911*x + 50257929339)
c1x = sp.expand(-2*(x + 2)*B8)
c2x = sp.expand(-2*B9)
c0x = sp.expand((x + 1)**5*(x + 2)*a0(x + 1))
P1 = sp.expand(c2x.subs(x, x - 2))
P2 = sp.expand(c1x.subs(x, x - 1))
P3 = sp.expand(c0x)
Pj = [sp.Poly(P0, x), sp.Poly(P1, x), sp.Poly(P2, x), sp.Poly(P3, x)]

# sanity: recurrence reproduces the ladder
Qs = [core.Q(n) for n in range(N + 3)]
for Nn in range(3, N + 3):
    s = sum(F(int(Pj[j].eval(Nn - j))) * Qs[Nn - j] for j in range(4))
    assert s == 0, Nn
print('operator check: sum_j P_j(N-j) Q_{N-j} = 0 for N <= %d: PASS' % (N + 2))

print('indicial polynomial P0(x) = 2 x^5 (2x-1) a0(x-3)')
print('  exponents at t=0: 0 (multiplicity 5), 1/2, roots of a0(x-3):')
r = sp.Poly(a0(x - 3), x).all_roots()
print('   ', [sp.nsimplify(sp.N(z, 8)) for z in r])
print('  -> NOT MUM as an order-9 operator; 5-dim unipotent block at 0')
for Nn in range(1, N + 1):
    assert Pj[0].eval(Nn) != 0
print('  P0(N) != 0 for 1<=N<=%d: log-solution g exists uniquely' % N)

# ---------------- Frobenius pair and nome ----------------
def gser():
    Pd = [sp.Poly(sp.diff(p.as_expr(), x), x) for p in Pj]
    R = [F(0)] * (N + 1)
    for j in range(4):
        for m in range(0, N + 1 - j):
            R[m + j] -= F(int(Pd[j].eval(m))) * Qs[m]
    g = [F(0)] * (N + 1)
    for Nn in range(1, N + 1):
        acc = R[Nn]
        for j in range(1, 4):
            if Nn - j >= 0:
                acc -= F(int(Pj[j].eval(Nn - j))) * g[Nn - j]
        g[Nn] = acc / F(int(Pj[0].eval(Nn)))
    return g

y0 = [F(x_) for x_ in Qs[:N + 1]]
g = gser()
ratio = smul(g, sinv(y0))
qser = smul([F(0), F(1)] + [F(0)] * (N - 1), sexp(ratio))
tq = srevert(qser)
Fq = compose(y0, tq)

def denprofile(ser, upto=20):
    return [ser[i].denominator for i in range(min(upto, len(ser) - 1) + 1)]

print('\nnome inversion:')
print('  t(q) coeffs 1..8:', [str(tq[i]) for i in range(1, 9)])
print('  t(q) denominators:', denprofile(tq))
print('  F(q) coeffs 0..8:', [str(Fq[i]) for i in range(9)])
print('  F(q) denominators:', denprofile(Fq))

# rescaling tests q -> lam q : t(q) -> coefficients tq[k]*lam^k
def rescale_integral(ser, lams):
    out = {}
    for lam in lams:
        ok = all((ser[k] * F(lam) ** k).denominator == 1
                 for k in range(1, N + 1))
        out[lam] = ok
    return out

lams = [1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256,
        384, 512, 576, 1024, 2048, 4096]
ri = rescale_integral(tq, lams)
hits = [l for l, ok in ri.items() if ok]
print('  integral t(lam q) for lam in tested set:', hits if hits else 'NONE')

# denominator growth diagnostic: 2-adic and 3-adic valuations of tq
def vp(q_, p):
    if q_ == 0:
        return 0
    v = 0
    d = q_.denominator
    while d % p == 0:
        d //= p
        v += 1
    return -v

print('  v2(den t_k):', [vp(tq[k], 2) for k in range(1, 21)])
print('  v3(den t_k):', [vp(tq[k], 3) for k in range(1, 21)])

# ---------------- root tests ----------------
def root_series(a, r_, n=N):
    """a^{1/r} with a[0]=1."""
    out = [F(0)] * (n + 1)
    out[0] = F(1)
    inv_r = F(1, r_)
    # (a^{1/r})' * a = (1/r) a' * a^{1/r}  -> Newton-style recursion
    for k in range(1, n + 1):
        acc = inv_r * F(k) * a[k]
        for j in range(1, k):
            acc += (inv_r * F(j) - F(k - j)) * a[j] * out[k - j]
        out[k] = acc / F(k)
    return out

for r_ in (2, 4):
    u = root_series(y0, r_)
    print('\nQ(t)^{1/%d} coeffs 1..8:' % r_,
          [str(u[i]) for i in range(1, 9)])
    print('  denominators:', denprofile(u))
    hits = [l for l, ok in rescale_integral(u, lams).items() if ok]
    print('  integral after t -> t/lam rescale, lam in set:',
          hits if hits else 'NONE')
