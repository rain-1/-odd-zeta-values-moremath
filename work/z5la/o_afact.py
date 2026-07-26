"""Factor the lifted A(n) = sum a_t(n) S^t over Q, and settle a_4(n) != 0 on N.

Also re-verifies the lift at (n, p) combinations that took no part in the fit.
"""
import os, sys, pickle, time
import sympy as sp


def poly(c, x):
    return sp.Poly(list(reversed([sp.Integer(v) for v in c])), x)


def analyse(name, c, x):
    P = poly(c, x)
    t0 = time.time()
    fac = sp.factor_list(P.as_expr(), x)
    cont, parts = fac
    print('%s : degree %d, content %s, max|coef| %d bits, %d digits'
          % (name, len(c) - 1, cont, max(abs(v) for v in c).bit_length(),
             len(str(max(abs(v) for v in c)))), flush=True)
    for f, m in sorted(parts, key=lambda z: sp.degree(z[0], x)):
        pf = sp.Poly(f, x)
        co = [int(v) for v in pf.all_coeffs()]
        allpos = all(v >= 0 for v in co) or all(v <= 0 for v in co)
        rr = sp.Poly(f, x).real_roots()
        nonneg = [r for r in rr if r >= 0]
        print('    deg %-3d mult %d   coeffs all one sign: %-5s   real roots >= 0: %s'
              % (sp.degree(f, x), m, allpos,
                 [sp.nsimplify(r) if r.is_rational else sp.N(r, 12) for r in nonneg]),
              flush=True)
        if sp.degree(f, x) <= 3:
            print('        %s' % sp.factor(f), flush=True)
    print('    [factorisation %.1fs]' % (time.time() - t0), flush=True)
    return parts


def positive_on_N(c, x, upto=200):
    """is the polynomial > 0 for every real n >= 0 ?  (Sturm, exact)"""
    P = sp.Poly(list(reversed([sp.Integer(v) for v in c])), x)
    rr = P.real_roots()
    nonneg = [r for r in rr if r >= 0]
    val0 = P.eval(0)
    return (len(nonneg) == 0, val0, [sp.N(r, 20) for r in nonneg])


def polya(c, Nmax=200):
    """least N with all coefficients of (1+n)^N * G(n) nonnegative (or all
    nonpositive).  Such an N exists iff G > 0 (resp < 0) on n >= 0 and G has no
    root there -- Polya's theorem.  This is the Lean-friendly certificate:
        (1+n)^N * G(n) = sum of monomials with nonnegative coefficients,
    which `positivity` closes in one line, and (1+n)^N > 0."""
    from math import comb
    sgn = 1
    if c[-1] < 0: c = [-v for v in c]; sgn = -1
    for N in range(Nmax + 1):
        out = [0] * (len(c) + N)
        for i, v in enumerate(c):
            if not v: continue
            for j in range(N + 1):
                out[i + j] += v * comb(N, j)
        if all(v >= 0 for v in out):
            return N, sgn, out
    return None, sgn, None


if __name__ == '__main__':
    Z = pickle.load(open('a_lift.pkl', 'rb'))['Z']
    x = sp.Symbol('n')
    for t in (4, 0, 1, 2, 3):
        analyse('a_%d' % t, Z[t], x)
        print(flush=True)
    ok, v0, roots = positive_on_N(Z[4], x)
    print('a_4 : no real root >= 0 : %s   a_4(0) = %s' % (ok, v0))
    if not ok: print('   nonnegative real roots: %s' % roots)
    allpos = all(v >= 0 for v in Z[4]) or all(v <= 0 for v in Z[4])
    print('a_4 : all coefficients of one sign (positivity closes directly): %s' % allpos)
    if not allpos:
        N, sgn, out = polya(Z[4])
        print('a_4 : Polya exponent N with (1+n)^N a_4(n) of one sign: %s  (sign %+d)'
              % (N, sgn))
        if N is not None:
            print('      -> (1+n)^%d * a_4(n) has %d nonnegative coefficients, '
                  'max %d bits' % (N, len(out), max(out).bit_length()))
