"""eps48_modular_nome.py -- modular-anchor probe for sporadic families.

For a 3-term Apery-like recurrence (MUM at t=0), compute exactly:
  y0(t)   = sum A(n) t^n            (analytic Frobenius solution)
  y1(t)   = y0 log t + g(t)         (log solution; g from L(g) = -L'(theta)y0)
  q(t)    = t exp(g/y0),  invert -> t(q), F(q) := y0(t(q))
Integrality of t(q) (after an optional rational rescale q -> lam q) is the
modularity signal; identification of F(q) against eta-quotients /
chi-twisted Eisenstein series names the parametrization and its letters.

Control: gamma = Apery zeta(3), known t,F eta-products on Gamma_0(6).
Targets: B (9,3,27, w=2), delta (7,3,81,0, w=3), zeta (9,3,-27,0, w=3).
All arithmetic exact (Fraction).  N terms configurable.
"""

import sys
from fractions import Fraction as F
from math import comb

N = 26   # series order

# ---------------- series helpers (lists of Fractions, index = power) ----------
def smul(a, b, n=N):
    out = [F(0)] * (n + 1)
    for i, x in enumerate(a[:n + 1]):
        if x == 0:
            continue
        for j, y in enumerate(b[:n + 1 - i]):
            if y:
                out[i + j] += x * y
    return out

def sinv(a, n=N):
    assert a[0] != 0
    out = [F(0)] * (n + 1)
    out[0] = 1 / a[0]
    for k in range(1, n + 1):
        out[k] = -sum(a[j] * out[k - j] for j in range(1, k + 1)) / a[0]
    return out

def sexp(a, n=N):
    assert a[0] == 0
    out = [F(0)] * (n + 1)
    out[0] = F(1)
    # exp' = a' exp
    for k in range(1, n + 1):
        out[k] = sum(F(j) * a[j] * out[k - j] for j in range(1, k + 1)) / k
    return out

def srevert(a, n=N):
    """functional inverse of a = q + O(q^2) (a[0]=0, a[1]=1 not required:
    a[1] != 0)."""
    assert a[0] == 0 and a[1] != 0
    # Lagrange-free iterative: t(q) with a(t(q)) = q
    t = [F(0)] * (n + 1)
    t[1] = 1 / a[1]
    for k in range(2, n + 1):
        # coefficient of q^k in a(t) must be 0 for k>1
        comp = compose(a, t, k)
        t[k] = -comp[k] / a[1]
    return t

def compose(a, b, n=N):
    """a(b(q)) with b[0]=0, up to order n."""
    out = [F(0)] * (n + 1)
    out[0] = a[0]
    bp = [F(0)] * (n + 1)
    bp[0] = F(1)
    for i in range(1, n + 1):
        bp = smul(bp, b, n)
        if i < len(a) and a[i]:
            for k in range(n + 1):
                out[k] += a[i] * bp[k]
    return out

# ---------------- family data ----------------
def A_seq_R2(a, b, c, n_top):
    A = [F(1)]
    for n in range(n_top):
        if n == 0:
            A.append(F(b, 1))  # (1)^2 A1 = b A0
        else:
            A.append((F(a * n * n + a * n + b) * A[n]
                      - F(c * n * n) * A[n - 1]) / F((n + 1) ** 2))
    return A

def A_seq_R3(a, b, c, d, n_top):
    A = [F(1)]
    for n in range(n_top):
        if n == 0:
            A.append(F(b))
        else:
            A.append((F((2 * n + 1) * (a * n * n + a * n + b)) * A[n]
                      - F(n * (c * n * n + d)) * A[n - 1]) / F((n + 1) ** 3))
    return A

def gseries(Pj, y0, n=N):
    """solve L(g) = -sum_j t^j Pj'(theta) y0, L = sum_j t^j Pj(theta);
    Pj given as coefficient lists of polynomials in theta."""
    import sympy as sp
    th = sp.symbols('th')
    P = [sp.Poly(p, th) for p in Pj]
    Pd = [sp.Poly(sp.diff(p.as_expr(), th), th) for p in P]
    def ev(poly, m):
        return F(int(poly.eval(m)))
    R = [F(0)] * (n + 1)
    for j in range(len(Pj)):
        for m in range(0, n + 1 - j):
            R[m + j] -= ev(Pd[j], m) * y0[m]
    g = [F(0)] * (n + 1)
    for Nn in range(1, n + 1):
        acc = R[Nn]
        for j in range(1, len(Pj)):
            if Nn - j >= 0:
                acc -= ev(P[j], Nn - j) * g[Nn - j]
        p0 = ev(P[0], Nn)
        g[Nn] = acc / p0
    return g

def nome(fam, w, Pj, Aser):
    y0 = Aser[:N + 1]
    g = gseries(Pj, y0)
    ratio = smul(g, sinv(y0))
    qser = smul([F(0), F(1)] + [F(0)] * (N - 1), sexp(ratio))  # t*exp(g/y0)
    tq = srevert(qser)
    Fq = compose(y0, tq)
    return tq, Fq

def eta_quot(exps, n=N):
    """prod_m prod_k (1-q^{mk})^{e_m}; exps dict m->e."""
    out = [F(0)] * (n + 1)
    out[0] = F(1)
    for m, e in exps.items():
        for k in range(1, n // m + 1):
            base = [F(0)] * (n + 1)
            base[0] = F(1)
            base[m * k] = F(-1)
            pw = power(base, e, n)
            out = smul(out, pw, n)
    return out

def power(a, e, n=N):
    out = [F(0)] * (n + 1)
    out[0] = F(1)
    b = a
    ee = abs(e)
    while ee:
        if ee & 1:
            out = smul(out, b, n)
        b = smul(b, b, n)
        ee >>= 1
    if e < 0:
        out = sinv(out)
    return out

def chi3(d):
    return [0, 1, -1][d % 3]

def E1_chi3(n=N):
    out = [F(0)] * (n + 1)
    out[0] = F(1)
    for m in range(1, n + 1):
        out[m] = F(6 * sum(chi3(d) for d in range(1, m + 1) if m % d == 0))
    return out

def report(name, tq, Fq, upto=18):
    from math import gcd
    dens = [x.denominator for x in tq[:upto + 1]]
    print('%s: t(q) coeffs (n<=%d):' % (name, min(10, upto)),
          [str(x) for x in tq[:11]])
    print('   t(q) denominator profile:', dens[:upto + 1])
    print('   F(q) coeffs:', [str(x) for x in Fq[:13]])

if __name__ == '__main__':
    import sympy as sp
    # ---- control: gamma = Apery zeta(3): R3 (17? no: gamma is (17,5,1,0)) --
    # NOTE core table: gamma row (17,5,1,0): recurrence
    # (n+1)^3 u_{n+1} = (2n+1)(17n^2+17n+5) u_n - n(1*n^2+0) u_{n-1} -- Apery.
    a, b, c, d = 17, 5, 1, 0
    Aser = A_seq_R3(a, b, c, d, N + 2)
    # sanity: Apery numbers 1,5,73,1445
    assert [int(x) for x in Aser[:4]] == [1, 5, 73, 1445], Aser[:4]
    th = sp.symbols('th')
    Pj = [th**3,
          -sp.expand((2 * th + 1) * (a * th**2 + a * th + b)),
          sp.expand((th + 1) * (c * (th + 1)**2 + d))]
    tq, Fq = nome('gamma', 3, Pj, Aser)
    report('gamma (Apery z3, control)', tq, Fq)
    t_known = smul([F(0), F(1)] + [F(0)] * (N - 1),
                   eta_quot({1: 12, 6: 12, 2: -12, 3: -12}))
    F_known = eta_quot({2: 7, 3: 7, 1: -5, 6: -5})
    print('   control t(q) == eta-quotient (G0(6)):',
          tq[:N + 1] == t_known[:N + 1])
    print('   control F(q) == eta-quotient:', Fq[:N + 1] == F_known[:N + 1])

    # ---- target B: R2 (9,3,27), weight 2 ----
    a, b, c = 9, 3, 27
    AB = A_seq_R2(a, b, c, N + 2)
    assert [int(x) for x in AB[:4]] == [1, 3, 9, 21], AB[:4]
    PjB = [th**2, -sp.expand(a * th**2 + a * th + b),
           sp.expand(c * (th + 1)**2)]
    tqB, FqB = nome('B', 2, PjB, AB)
    report('B (Zagier f)', tqB, FqB)
    E = E1_chi3()
    print('   F(q) == E_{1,chi-3}(q)?', FqB[:N + 1] == E[:N + 1])
    # try eta-based hauptmodul guesses for level 9
    t9 = smul([F(0), F(1)] + [F(0)] * (N - 1), eta_quot({1: 12, 9: -12}))
    print('   t(q) == q*eta(q)^12/eta(q^9)^12?', tqB[:N + 1] == t9[:N + 1])
    t9b = smul([F(0), F(1)] + [F(0)] * (N - 1), eta_quot({1: 3, 9: -3}))
    print('   t(q) == q*eta(q)^3/eta(q^9)^3?', tqB[:N + 1] == t9b[:N + 1])

    # ---- target delta: R3 (7,3,81,0), weight 3 ----
    a, b, c, d = 7, 3, 81, 0
    AD = A_seq_R3(a, b, c, d, N + 2)
    PjD = [th**3, -sp.expand((2 * th + 1) * (a * th**2 + a * th + b)),
           sp.expand((th + 1) * (c * (th + 1)**2 + d))]
    tqD, FqD = nome('delta', 3, PjD, AD)
    report('delta', tqD, FqD)

    # ---- target zeta: R3 (9,3,-27,0), weight 3 ----
    a, b, c, d = 9, 3, -27, 0
    AZ_ = A_seq_R3(a, b, c, d, N + 2)
    PjZ = [th**3, -sp.expand((2 * th + 1) * (a * th**2 + a * th + b)),
           sp.expand((th + 1) * (c * (th + 1)**2 + d))]
    tqZ, FqZ = nome('zeta', 3, PjZ, AZ_)
    report('zeta', tqZ, FqZ)
