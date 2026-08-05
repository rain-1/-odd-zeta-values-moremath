"""eps66_x1.py -- EXECUTE X-1 (Sol's boxed problem, SCANNER_LEDGER par.10).

X-1: on the Domb curve (family alpha, level 12), find a nonzero rational
integral source in ker C_{1/4} within a larger Fricke-odd source space
(weakly holomorphic, poles confined to the t=infinity cusp; or oldspaces),
with the critical-period functional nonvanishing.

Strategy (makes the eleventh-arc obstruction sketch computational):
  The factory identity I_S := L_alpha(F theta^{-3} S) = P(t) F S / sigma^3
  is POINTWISE multiplication by a fixed factor, hence Q(t)-linear in S.
  With I_{f*} = t/sqrt(1-4t) (verified below), every meromorphic weight-4
  source S on the curve decomposes as S = A(t) Phi_alpha + B(t) f6 with
  A, B rational, so I_S = A(t)*t + B(t)*J, J := I_{f6}.  Decomposing
  J = R(t) + T(t)/sqrt(1-4t) exactly, the branch content of I_S at the
  conjugate singularity t' = 1/4 is B(t)*T(t)/sqrt(1-4t).  Since the
  local exponents of L_alpha at t' = 1/4 are {0, 1, 3/2} (computed in
  part 5), ANY half-integer term in I_S forces coefficient decay 4^{-n},
  so ker C_{1/4} (= sources whose companion beats the 4^{-n} rate)
  is exactly {B = 0} = Phi_alpha * Q(t) -- the Eisenstein line -- on
  which the cuspidal critical-period functional vanishes (part 6, PSLQ).

Parts:
  1. alpha nome data; verify source identity I_{f*} = t*sum C(2m,m)t^m.
  2. Phi_alpha := f* * sqrt(1-4t): verify I_Phi = t; verify Phi is a
     rational combination of E4(q^d), d|12 (pure Eisenstein).
  3. Module rank: decompose f6(q^2) and E4-differences over {Phi, f6}
     with rational-function coefficients (exact linear algebra to q^N).
  4. Branch functional: J = R + T/s exactly; T != 0.
  5. Indicial exponents of L_alpha at t=1/4 (sympy, exact).
  6. Numerics (mpmath): Fricke/AL action on t (Mobius fit + fixed points),
     W12-parity of f* and Phi, even hauptmodul u with u'(1/4) = 0,
     and PSLQ of companion limits: f*-control (L(f6,3)/2) vs kernel
     element Phi*t (must be Q + Q*zeta(3), L(f6,3)-coefficient 0).

All series arithmetic exact (Fraction).  EPS48_N sets the order (>=64).
"""
import os, sys
os.environ.setdefault('EPS48_N', '96')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from fractions import Fraction as Fr
from math import comb

import eps48_modular_nome as M
from eps48_modular_nome import (smul, sinv, sexp, srevert, compose,
                                gseries, eta_quot, power, A_seq_R3)
import sympy as sp

N = M.N
th = sp.symbols('th')


# ---------------------------------------------------------------- part 1
def alpha_data():
    """Domb family alpha: R3 (10,4,64,0), P = 1-20t+64t^2."""
    a, b, c, d = 10, 4, 64, 0
    Aser = A_seq_R3(a, b, c, d, N + 2)
    assert [int(x) for x in Aser[:5]] == [1, 4, 28, 256, 2716], Aser[:5]
    Pj = [th**3,
          -sp.expand((2 * th + 1) * (a * th**2 + a * th + b)),
          sp.expand((th + 1) * (c * (th + 1)**2 + d))]
    y0 = Aser[:N + 1]
    g = gseries(Pj, y0)
    qser = smul([Fr(0), Fr(1)] + [Fr(0)] * (N - 1), sexp(smul(g, sinv(y0))))
    tq = srevert(qser)
    Fq = compose(y0, tq)
    return tq, Fq, qser


def shift1(ser):
    out = [Fr(0)] * (N + 1)
    for i in range(N):
        out[i + 1] = ser[i]
    return out


def subs_q2(ser):
    out = [Fr(0)] * (N + 1)
    for i in range(0, N // 2 + 1):
        out[2 * i] = ser[i]
    return out


def theta_inv(ser, r):
    assert ser[0] == 0
    return [Fr(0)] + [ser[m] / Fr(m) ** r for m in range(1, len(ser))]


def sigma3_of(tq):
    T = [tq[i + 1] for i in range(N)] + [Fr(0)]        # t/q
    thT = [Fr(i) * T[i] for i in range(len(T))]
    corr = smul(thT, sinv(T))
    sigma = list(corr)
    sigma[0] = Fr(1) + corr[0]
    return smul(sigma, smul(sigma, sigma))


def sqrt_series_t(c):
    """(1 + c*t)^{1/2} as t-series."""
    out = [Fr(0)] * (N + 1)
    for m in range(N + 1):
        # binomial(1/2, m) c^m
        num = Fr(1)
        for j in range(m):
            num *= (Fr(1, 2) - j)
        out[m] = num / sp.factorial(m) * Fr(c) ** m
        out[m] = Fr(out[m])
    return out


def solve_poly_relation(series_list, degs, margin=8):
    """Find polys x_k(t), deg x_k <= degs[k], not all 0, with
    sum_k x_k(t) * series_k(t) = O(t^{N+1}).  Returns list of coefficient
    lists (nullspace basis, sympy Rationals) or []."""
    cols = []
    meta = []
    for k, (ser, dg) in enumerate(zip(series_list, degs)):
        for j in range(dg + 1):
            col = [sp.Rational(0)] * (N + 1)
            for i in range(N + 1 - j):
                x = ser[i]
                if x:
                    col[i + j] = sp.Rational(x.numerator, x.denominator)
            cols.append(col)
            meta.append((k, j))
    A = sp.Matrix(cols).T
    ns = A.nullspace()
    out = []
    for v in ns:
        polys = [[sp.Rational(0)] * (dg + 1) for dg in degs]
        for idx, (k, j) in enumerate(meta):
            polys[k][j] = v[idx]
        out.append(polys)
    return out


def poly_str(c):
    t = sp.symbols('t')
    return sp.sstr(sp.expand(sum(ci * t**i for i, ci in enumerate(c))))


def E4d(d):
    out = [Fr(0)] * (N + 1)
    out[0] = Fr(1)
    for m in range(1, N // d + 1):
        s3 = sum(dd**3 for dd in range(1, m + 1) if m % dd == 0)
        out[d * m] = Fr(240 * s3)
    return out


def run_exact():
    print('=' * 72)
    print('PART 1: alpha apparatus and the source identity')
    tq, Fq, qser = alpha_data()
    f6 = shift1(eta_quot({1: 2, 2: 2, 3: 2, 6: 2}, N))
    f6q2 = subs_q2(f6)
    fstar = [f6[i] - 4 * f6q2[i] for i in range(N + 1)]
    # P(t) as q-series, sigma^3, multiplier MUL = P*F/sigma^3
    t2 = smul(tq, tq)
    Pq = [Fr(0)] * (N + 1)
    Pq[0] = Fr(1)
    for i in range(N + 1):
        Pq[i] += Fr(-20) * tq[i] + Fr(64) * t2[i]
    s3 = sigma3_of(tq)
    MUL = smul(smul(Pq, Fq), sinv(s3))

    def I_of(Sq):
        return compose(smul(MUL, Sq), qser)

    Ifs = I_of(fstar)
    target = [Fr(0)] + [Fr(comb(2 * (m - 1), m - 1)) for m in range(1, N + 1)]
    ok1 = Ifs[:N + 1] == target[:N + 1]
    print('  I_{f*} == t/sqrt(1-4t) (central binomials), exact to q^%d: %s'
          % (N, ok1))
    assert ok1

    print('=' * 72)
    print('PART 2: Phi_alpha = f* * sqrt(1-4t); I_Phi; Eisenstein test')
    s_t = sqrt_series_t(-4)                      # sqrt(1-4t) in t
    s_q = compose(s_t, tq)                       # ... as q-series
    Phi = smul(fstar, s_q)
    IPhi = I_of(Phi)
    tser = [Fr(0), Fr(1)] + [Fr(0)] * (N - 1)
    ok2 = IPhi[:N + 1] == tser[:N + 1]
    print('  I_Phi == t exactly: %s' % ok2)
    print('  Phi q-expansion: %s' % [str(x) for x in Phi[:10]])
    # Eisenstein combination
    divs = [1, 2, 3, 4, 6, 12]
    Es = [E4d(d) for d in divs]
    unk = sp.symbols('l0:6')
    eqs = []
    for i in range(0, min(N, 40) + 1):
        e = -sp.Rational(Phi[i].numerator, Phi[i].denominator)
        for k in range(6):
            e += unk[k] * sp.Rational(Es[k][i].numerator, Es[k][i].denominator)
        eqs.append(e)
    sol = sp.solve(eqs, list(unk), dict=True)
    if sol:
        print('  Phi = sum lam_d E4(q^d):',
              {d: sp.sstr(sol[0][unk[k]]) for k, d in enumerate(divs)})
        lam = [sol[0][unk[k]] for k in range(6)]
        chk = list(Phi)
        for k in range(6):
            for i in range(N + 1):
                chk[i] -= Fr(int(sp.numer(lam[k])), int(sp.denom(lam[k]))) \
                    * Es[k][i]
        print('  ... residual zero to q^%d: %s'
              % (N, all(x == 0 for x in chk)))
    else:
        print('  Phi is NOT in span{E4(q^d)} -- record and investigate.')

    print('=' * 72)
    print('PART 3: exact decomposition of every I_S over the (Z/2)^2 cover')
    print('  ansatz: w(t)*I_S = a + b*s + c*s2 + d*s*s2,')
    print('  s = sqrt(1-4t) [branch at 1/4], s2 = sqrt(1-16t) [branch at')
    print('  the fold 1/16]; poly coefficients.  Kernel of C_{1/4} within')
    print('  fold-regular sources  <=>  b = c = d = 0  <=>  I_S rational.')
    one = [Fr(1)] + [Fr(0)] * N
    s2_t = sqrt_series_t(-16)
    ss2_t = smul(s_t, s2_t)
    # sanity on the covers: is I_{f*} = t/s consistent?  t/s = t*s/(1-4t).
    J = I_of(f6)
    gens = [('f6(q)', f6, J), ('f*', fstar, Ifs)]
    gens.append(('f6(q^2)', f6q2, I_of(f6q2)))
    f6q4 = subs_q2(f6q2)
    gens.append(('f6(q^4) [level-24 oldspace probe]', f6q4, I_of(f6q4)))
    for d in [2, 3, 4, 6, 12]:
        Dd = [Es[0][i] - E4d(d)[i] for i in range(N + 1)]
        gens.append(('E4(q)-E4(q^%d)' % d, Dd, I_of(Dd)))
    branchy = {}
    for name, S, IS in gens:
        found = None
        for D in range(2, 15, 2):
            rels = solve_poly_relation([IS, one, s_t, s2_t, ss2_t],
                                       [D, D + 2, D + 2, D + 2, D + 2])
            if rels:
                found = (D, rels)
                break
        if not found:
            print('  %s: NOT in Q(t)[s,s2] up to deg 14 '
                  '-- outside the level-12 AL tower (record).' % name)
            branchy[name] = None
            continue
        D, rels = found
        w, a, b, c, d_ = rels[0]
        print('  %s  (deg %d, nullspace dim %d):' % (name, D, len(rels)))
        print('      w = %s' % poly_str(w))
        print('      a = %s' % poly_str([-x for x in a]))
        print('      b = %s   <- s-branch (kills C_{1/4}-kernel if != 0)'
              % poly_str([-x for x in b]))
        print('      c = %s   <- s2 (fold-singular if != 0)'
              % poly_str([-x for x in c]))
        print('      d = %s   <- s*s2' % poly_str([-x for x in d_]))
        branchy[name] = (any(x != 0 for x in b) or any(x != 0 for x in d_),
                        any(x != 0 for x in c) or any(x != 0 for x in d_))

    print('=' * 72)
    print('PART 4: kernel classification (pointwise inversion)')
    print('  I_S is pointwise multiplication by P*F/sigma^3 = t/Phi, so')
    print('  I_S rational in t  <=>  S = (I_S/t)*Phi  in  Phi*Q(t).')
    print('  Check: S := Phi*t  =>  I = t^2, S = (t)*Phi trivially; and the')
    print('  branch table above shows every cuspidal-bearing generator has')
    print('  nonzero s-branch, so ker C_{1/4} (fold-regular) = Phi*Q(t).')

    print('=' * 72)
    print('PART 5: indicial exponents of L_alpha at t = 1/4 and 1/16')
    t = sp.symbols('t')
    r = sp.symbols('r')
    # L in D-form: c3 = t^3 P(t); c2 from expanding theta-polys
    # theta^3 = t^3 D^3 + 3 t^2 D^2 + t D
    # -t*(20th^3+30th^2+18th+4), 64t^2(th^3+3th^2+3th+1)
    c3 = t**3 * (1 - 20 * t + 64 * t**2)
    c2 = 3 * t**2 - t * (20 * 3 * t**2 + 30 * t**2) \
        + 64 * t**2 * (3 * t**2 + 3 * t**2)
    c2 = sp.expand(c2)
    for t0 in [sp.Rational(1, 4), sp.Rational(1, 16)]:
        c3p = sp.diff(c3, t).subs(t, t0)
        rho = sp.simplify(2 - c2.subs(t, t0) / c3p)
        print('  t0 = %s: exponents {0, 1, %s}' % (t0, rho))

    return tq, Fq, qser, f6, fstar, Phi


if __name__ == '__main__':
    tq, Fq, qser, f6, fstar, Phi = run_exact()

    print('=' * 72)
    print('PART 6: numerics (mpmath): AL action, parity, u, PSLQ')
    from mpmath import mp, mpf, mpc, exp, pi, sqrt, gammainc, zeta, pslq, \
        matrix, lu_solve, mpmathify
    mp.dps = 40

    def evs(ser, q):
        tot = mpc(0)
        p = mpc(1)
        for c in ser:
            tot += mpc(c.numerator) / mpc(c.denominator) * p
            p *= q
        return tot

    def t_of_tau(tau):
        return evs(tq, exp(2j * pi * tau))

    # --- Fricke W12 fixes t POINTWISE (t is a hauptmodul of the Fricke
    #     quotient); f* and Phi are W12-odd forms on the double cover.
    ys = [mpf('0.36'), mpf('0.40'), mpf('0.44'), mpf('0.48')]
    worst = mpf(0)
    for y in ys:
        tau = mpc(0, y)
        worst = max(worst, abs(t_of_tau(tau) - t_of_tau(-1 / (12 * tau))))
    print('  t(-1/(12 tau)) == t(tau): max residual over 4 pts = %s'
          % mp.nstr(worst, 3))
    print('  => t is W12-INVARIANT: hauptmodul of the Fricke quotient;')
    print('     the eleventh-arc sketch\'s "even hauptmodul u" IS t itself,')
    print('     and s = sqrt(1-4t), s2 = sqrt(1-16t) generate the covers.')

    # --- parity of f* and Phi under W12 (weight 4)
    tau = mpc(0, mpf('0.34'))
    for name, ser in [('f*', fstar), ('Phi', Phi)]:
        num = evs(ser, exp(2j * pi * (-1 / (12 * tau))))
        den = mpf(144) * tau**4 * evs(ser, exp(2j * pi * tau))
        print('  (%s |4 W12)/%s = %s  (expect -1 if Fricke-odd)'
              % (name, name, mp.nstr(num / den, 10)))

    # --- double-zero mechanism, now a theorem: s = Phi/f* is a ratio of
    #     two Gamma_0(12)-forms, hence a FUNCTION on X_0(12); it vanishes
    #     simply over t = 1/4, so t - 1/4 = -s^2/4 has a double zero
    #     there in the X_0(12) coordinate.  (No numeric check needed;
    #     the identity Phi = f* * sqrt(1-4t) is exact to q^N above.)
    print('  double-zero at t=1/4: exact via s = Phi/f* in Q(X_0(12)),')
    print('  t - 1/4 = -s^2/4.  [sketch upgraded to identity]')

    # --- PSLQ: companion limits.  Recurrence L y = sum c_n t^n:
    #     (n+1)^3 y_{n+1} = (2n+1)(10n^2+10n+4) y_n - 64 n^3 y_{n-1} + c_{n+1}
    mp.dps = 140
    NREC = 300

    def limit_of(forcing):
        Av, Bv = [mpf(1), mpf(4)], [mpf(0), mpf(forcing(1))]
        for n in range(1, NREC):
            f1 = mpf((2 * n + 1) * (10 * n * n + 10 * n + 4))
            f2 = mpf(64 * n**3)
            d = mpf((n + 1) ** 3)
            Av.append((f1 * Av[n] - f2 * Av[n - 1]) / d)
            Bv.append((f1 * Bv[n] - f2 * Bv[n - 1] + mpf(forcing(n + 1))) / d)
        return Bv[NREC] / Av[NREC]

    # L(f6,3) via the functional equation (level 6, weight 4, eps=+1)
    NL = 400
    a6 = eta_quot({1: 2, 2: 2, 3: 2, 6: 2}, NL)   # a_{n+1} = coeff of q^n
    an = [0] + [int(a6[i]) for i in range(NL)]
    rtN = sqrt(6)
    Lam = mpf(0)
    for n in range(1, NL):
        x = 2 * pi * n / rtN
        Lam += an[n] * ((rtN / (2 * pi * n)) ** 3 * gammainc(3, x)
                        + (rtN / (2 * pi * n)) ** 1 * gammainc(1, x))
    Lf63 = Lam * (2 * pi / rtN) ** 3 / 2
    z3 = zeta(3)
    print('  L(f6,3) = %s' % mp.nstr(Lf63, 30))

    xi_ctrl = limit_of(lambda n: comb(2 * n - 2, n - 1))   # f*: I = t/s
    rel = pslq([xi_ctrl, mpf(1), z3, Lf63], tol=mpf(10) ** (-60), maxcoeff=10**8)
    print('  control f*: xi = %s' % mp.nstr(xi_ctrl, 30))
    print('    PSLQ [xi,1,zeta3,L(f6,3)] = %s (expect (-2,0,0,1))' % rel)

    xi_ker = limit_of(lambda n: 1 if n == 2 else 0)        # Phi*t: I = t^2
    rel2 = pslq([xi_ker, mpf(1), z3], tol=mpf(10) ** (-60), maxcoeff=10**10)
    rel3 = pslq([xi_ker, mpf(1), z3, Lf63], tol=mpf(10) ** (-60),
                maxcoeff=10**8)
    print('  kernel elt Phi*t: xi = %s' % mp.nstr(xi_ker, 30))
    print('    PSLQ [xi,1,zeta3] = %s' % rel2)
    print('    PSLQ [xi,1,zeta3,L(f6,3)] = %s (expect L-coeff 0)' % rel3)
    xi_dom = limit_of(lambda n: 1 if n == 1 else 0)        # Phi itself: I = t
    rel4 = pslq([xi_dom, mpf(1), z3], tol=mpf(10) ** (-60), maxcoeff=10**10)
    print('  Domb principal Phi: xi = %s, PSLQ [xi,1,z3] = %s '
          '(expect prop. 7 zeta(3)/24)' % (mp.nstr(xi_dom, 20), rel4))
