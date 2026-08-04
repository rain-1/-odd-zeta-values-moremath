"""eps49b_borwein_asd.py -- Tasks 2 and 3 of the modular follow-up.

Task 2: identify family B's weight-1 form against the level-3/9/27 cubic
objects: Borwein a(q), b(q) (= eta(t)^3/eta(3t)), their q->q^3, q->q^9
rescalings, and eta(9t)^3/eta(3t) (integral series).  Exact linear solve.

Task 3: ASD probe for zeta: verify the twisted Lucas law (eq LB)
    p^3 B(ap+r) == chi_{-3}(p)^e B(a) A(r)  (mod p),  1<=a<p, 0<=r<p,
at p = 5, 7, 11, 13 for e = 0 and e = 1 (discriminating primes: 5, 11
where chi = -1), using exact rational arithmetic and p-adic valuations.
"""

import sys
from fractions import Fraction as F_
from math import comb

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
from eps48_modular_nome import (smul, sinv, eta_quot, power, A_seq_R2,
                                A_seq_R3, gseries, srevert, sexp, compose, N)
import sympy as sp

# ---------------- Task 2 ----------------
def borwein_a(n=N):
    out = [0] * (n + 1)
    B = int(n ** 0.5) + 2
    for m in range(-B, B + 1):
        for k in range(-B, B + 1):
            v = m * m + m * k + k * k
            if v <= n:
                out[v] += 1
    return [F_(x) for x in out]

def rescale(a, d, n=N):
    out = [F_(0)] * (n + 1)
    for i, x in enumerate(a):
        if i * d <= n:
            out[i * d] = x
    return out

if __name__ == '__main__':
    # F_B from the nome machinery
    th = sp.symbols('th')
    a_, b_, c_ = 9, 3, 27
    AB = A_seq_R2(a_, b_, c_, N + 2)
    PjB = [th**2, -sp.expand(a_ * th**2 + a_ * th + b_),
           sp.expand(c_ * (th + 1)**2)]
    y0 = AB[:N + 1]
    g = gseries(PjB, y0)
    qser = smul([F_(0), F_(1)] + [F_(0)] * (N - 1),
                sexp(smul(g, sinv(y0))))
    tq = srevert(qser)
    FB = compose(y0, tq)

    aq = borwein_a()
    bq = eta_quot({1: 3, 3: -1})            # eta(t)^3/eta(3t)
    c93 = smul([F_(0), F_(1)] + [F_(0)] * (N - 1),
               eta_quot({9: 3, 3: -1}))     # q prod (1-q^9n)^3/(1-q^3n)
    cands = {
        'a(q)': aq, 'a(q3)': rescale(aq, 3), 'a(q9)': rescale(aq, 9),
        'b(q)': bq, 'b(q3)': rescale(bq, 3), 'b(q9)': rescale(bq, 9),
        'eta9^3/eta3': c93,
    }
    names = list(cands)
    NEQ = 20
    rows = [[cands[nm][i] for nm in names] for i in range(NEQ)]
    rhs = [FB[i] for i in range(NEQ)]
    Msys = sp.Matrix(rows)
    v = sp.Matrix(rhs)
    sol, params = Msys.gauss_jordan_solve(Msys, v, freevar=True) \
        if False else (None, None)
    # simple exact least-structure solve via sympy linsolve
    xs = sp.symbols('x0:%d' % len(names))
    eqs = [sum(xs[j] * rows[i][j] for j in range(len(names))) - rhs[i]
           for i in range(NEQ)]
    solset = sp.linsolve(eqs, list(xs))
    print('Task 2: F_B against cubic dictionary:')
    if not solset:
        print('  NO exact combination in {%s}' % ', '.join(names))
    else:
        s = list(solset)[0]
        if any(x.free_symbols for x in s):
            # pick particular: free params -> 0
            subs = {sym: 0 for x in s for sym in x.free_symbols}
            s = [sp.simplify(x.subs(subs)) for x in s]
        # verify on ALL N coefficients
        okall = all(sum(F_(int(sp.nsimplify(s[j]).p), int(sp.nsimplify(s[j]).q))
                        * cands[names[j]][i] for j in range(len(names)))
                    == FB[i] for i in range(N + 1)) \
            if all(sp.nsimplify(x).is_rational for x in s) else False
        print('  combination:', {names[j]: str(s[j]) for j in range(len(names))
                                 if s[j] != 0})
        print('  verified on all %d coefficients: %s' % (N + 1, okall))

    # ---------------- Task 3 ----------------
    print('\nTask 3: ASD / twisted Lucas for zeta (w=3, chi_{-3})')
    def Azeta(n):
        return sum(comb(n, k)**2 * comb(n, l) * comb(k, l) * comb(k + l, n)
                   for k in range(n + 1) for l in range(n + 1))
    a3, b3, c3, d3 = 9, 3, -27, 0
    NTOP = 13 * 13 + 13
    A = [Azeta(n) for n in range(NTOP + 1)]
    B = [F_(0), F_(1)]
    for n in range(1, NTOP):
        B.append((F_((2 * n + 1) * (a3 * n * n + a3 * n + b3)) * B[n]
                  - F_(n * (c3 * n * n + d3)) * B[n - 1]) / F_((n + 1) ** 3))
    def chi3(m):
        return [0, 1, -1][m % 3]
    def vp(x, p):
        if x == 0:
            return 999
        num, den = x.numerator, x.denominator
        v = 0
        while num % p == 0:
            num //= p; v += 1
        while den % p == 0:
            den //= p; v -= 1
        return v
    def modp(x, p):
        num, den = x.numerator % p, x.denominator % p
        return num * pow(den, p - 2, p) % p
    for p in (5, 7, 11, 13):
        verdict = {0: True, 1: True}
        for aa in range(1, p):
            for r in range(p):
                lhs = F_(p) ** 3 * B[aa * p + r]
                if vp(lhs, p) < 0:
                    verdict[0] = verdict[1] = None
                    continue
                L = modp(lhs, p)
                R0 = modp(B[aa] * F_(A[r]), p) if vp(B[aa], p) >= 0 else None
                for e in (0, 1):
                    if R0 is None:
                        verdict[e] = None
                        continue
                    R = R0 * (chi3(p) ** e % p) % p
                    if L != R % p:
                        verdict[e] = False
        print('  p=%2d chi(p)=%2d :  e=0 %s   e=1 %s'
              % (p, chi3(p), verdict[0], verdict[1]))
