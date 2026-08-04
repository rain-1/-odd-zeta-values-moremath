"""eps53_z5_deep.py -- deep probe of the BZ zeta(5) 5-block.

Sections (run: python3 eps53_z5_deep.py [dwork|qside|factor|all]):
  A. Frobenius tower f0..f4 of the unipotent block (exact, any order).
  B. DWORK: F(q) =? F_{<p}(q) * F(q^p) mod p for p = 5, 7.
  C. QSIDE: mirror avatars of the rows: s3 = theta^3(Phat(t)/Q(t) in q),
     s5 = theta^5(P(t)/Q(t) in q); CONTROL: same for Apery zeta(3)
     (gamma family), where the classical answer is a weight-4 Eisenstein
     form on Gamma_0(6).  Also the q-Frobenius normal form ghat2 and the
     Yukawa-type series theta^2(Y2/Y0) integrality test.
  D. FACTOR: order-5 right factor of the order-9 operator killing the
     block (mod-p linear solve over t-degree J, then exact reconstruct).
All arithmetic exact Fractions unless stated mod p.
"""

import sys
from fractions import Fraction as F

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import core
import sympy as sp
from eps48_modular_nome import smul, sinv, sexp, srevert, compose

NN = 32          # series order for most computations

# ---------------- operator (as in eps50) ----------------
x = sp.symbols('x')
a0 = lambda z: 41218*z**3 + 198849*z**2 + 320790*z + 173057
B8 = (3874492*x**8 + 59373972*x**7 + 394148190*x**6 + 1481084196*x**5
      + 3447878810*x**4 + 5095855458*x**3 + 4673546679*x**2
      + 2433871008*x + 551502039)
B9 = (48802112*x**9 + 967468896*x**8 + 8488000862*x**7 + 43246197636*x**6
      + 140983768422*x**5 + 304912330849*x**4 + 437406946975*x**3
      + 401272692378*x**2 + 213593890911*x + 50257929339)
c0x = sp.expand((x + 1)**5*(x + 2)*a0(x + 1))
c1x = sp.expand(-2*(x + 2)*B8)
c2x = sp.expand(-2*B9)
c3x = sp.expand(2*(x + 3)**5*(2*x + 5)*a0(x))
PJ = [sp.Poly(sp.expand(c3x.subs(x, x - 3)), x),
      sp.Poly(sp.expand(c2x.subs(x, x - 2)), x),
      sp.Poly(sp.expand(c1x.subs(x, x - 1)), x),
      sp.Poly(c0x, x)]
PJD = [[sp.Poly(sp.diff(p.as_expr(), x, i), x) for p in PJ] for i in range(6)]

def apply_op_deriv(i, f, n=NN):
    """(1/i!) L^{(i)}(theta) f as series, L = sum_j t^j P_j(theta)."""
    from math import factorial
    out = [F(0)] * (n + 1)
    for j in range(4):
        Pji = PJD[i][j]
        for m in range(0, n + 1 - j):
            if f[m]:
                out[m + j] += F(int(Pji.eval(m)), factorial(i)) * f[m]
    return out

def frobenius_tower(y0, kmax=4, n=NN):
    """f0..f_kmax with L(f_k) = -sum_{i=1}^k (1/i!) L^(i) f_{k-i}."""
    fs = [list(y0[:n + 1])]
    for k in range(1, kmax + 1):
        R = [F(0)] * (n + 1)
        for i in range(1, k + 1):
            ci = apply_op_deriv(i, fs[k - i], n)
            for m in range(n + 1):
                R[m] -= ci[m]
        f = [F(0)] * (n + 1)
        for Nn in range(1, n + 1):
            acc = R[Nn]
            for j in range(1, 4):
                if Nn - j >= 0:
                    acc -= F(int(PJ[j].eval(Nn - j))) * f[Nn - j]
            f[Nn] = acc / F(int(PJ[0].eval(Nn)))
        fs.append(f)
    return fs

# ---------------- shared series ----------------
Qs = [F(core.Q(n)) for n in range(NN + 1)]
Ps = [F(core.P(n)) for n in range(NN + 1)]
Phs = [F(core.Ph(n)) for n in range(NN + 1)]

fs = frobenius_tower(Qs, 4, NN)
y0 = fs[0]
g1 = fs[1]
ratio = smul(g1, sinv(y0), NN)
qser = smul([F(0), F(1)] + [F(0)] * (NN - 1), sexp(ratio, NN), NN)
tq = srevert(qser, NN)
Fq = compose(y0, tq, NN)

def theta(a, n=NN):
    return [F(k) * a[k] for k in range(n + 1)]

def theta_series(a, times, n=NN):
    out = a
    for _ in range(times):
        out = theta(out, n)
    return out

def hprofile(ser, upto=16):
    return [ser[i].denominator for i in range(upto + 1)]

# ================= B. DWORK =================
def dwork(p):
    """test F(q) == F_{<p}(q) * F(q^p) mod p, coefficientwise to NN."""
    Ftrunc = [Fq[i] if i < p else F(0) for i in range(NN + 1)]
    Fqp = [F(0)] * (NN + 1)
    for i in range(NN // p + 1):
        Fqp[i * p] = Fq[i]
    rhs = smul(Ftrunc, Fqp, NN)
    ok = True
    for i in range(NN + 1):
        d = Fq[i] - rhs[i]
        if d.denominator % p == 0 or d.numerator % p != 0:
            ok = False
            print('   p=%d first failure at q^%d: diff=%s' % (p, i, d))
            break
    print('  DWORK p=%d: F(q) == F_{<p}(q)*F(q^p) mod %d to q^%d: %s'
          % (p, p, NN, 'PASS' if ok else 'FAIL'))
    return ok

# ================= C. QSIDE =================
def qside():
    print('\n== C. q-side avatars ==')
    # --- control: Apery zeta(3) ---
    from eps48_modular_nome import A_seq_R3
    a_, b_, c_, d_ = 17, 5, 1, 0
    A = A_seq_R3(a_, b_, c_, d_, NN + 2)[:NN + 1]
    # second solution: B(0)=0, B(1)=6 (Apery zeta3 numerators normalization
    # b_n; use recurrence with same coefficients)
    B = [F(0), F(6)]
    for n in range(1, NN):
        B.append((F((2 * n + 1) * (a_ * n * n + a_ * n + b_)) * B[n]
                  - F(n * (c_ * n * n + d_)) * B[n - 1]) / F((n + 1) ** 3))
    th = sp.symbols('th')
    Pjg = [sp.Poly(th**3, th),
           sp.Poly(-sp.expand((2*th + 1)*(a_*th**2 + a_*th + b_)), th),
           sp.Poly(sp.expand((th + 1)*(c_*(th + 1)**2 + d_)), th)]
    # gamma nome
    def gser_generic(Pj, y0_, n=NN):
        Pd = [sp.Poly(sp.diff(p.as_expr(), th), th) for p in Pj]
        R = [F(0)] * (n + 1)
        for j in range(len(Pj)):
            for m in range(0, n + 1 - j):
                R[m + j] -= F(int(Pd[j].eval(m))) * y0_[m]
        gg = [F(0)] * (n + 1)
        for Nn in range(1, n + 1):
            acc = R[Nn]
            for j in range(1, len(Pj)):
                if Nn - j >= 0:
                    acc -= F(int(Pj[j].eval(Nn - j))) * gg[Nn - j]
            gg[Nn] = acc / F(int(Pj[0].eval(Nn)))
        return gg
    gg = gser_generic(Pjg, A)
    qg = smul([F(0), F(1)] + [F(0)] * (NN - 1),
              sexp(smul(gg, sinv(A, NN), NN), NN), NN)
    tqg = srevert(qg, NN)
    ratio_g = smul(B, sinv(A, NN), NN)          # B(t)/A(t)
    rg_q = compose(ratio_g, tqg, NN)
    s3g = theta_series(rg_q, 3, NN)
    print(' CONTROL gamma: s3 = theta_q^3(B/A):')
    print('   coeffs 1..10:', [str(s3g[i]) for i in range(1, 11)])
    print('   denominators:', hprofile(s3g))
    # classical: should be (up to scale 6) an integral weight-4 form; test
    # s3g/6 integral
    s3g6 = [v / 6 for v in s3g]
    print('   s3/6 integral to q^%d:' % NN,
          all(v.denominator == 1 for v in s3g6))
    # identify vs Eisenstein basis sigma3(n) n^3 q^n/(1-q^n) at levels 1,2,3,6
    def sig3(n=NN):
        out = [F(0)] * (n + 1)
        for m in range(1, n + 1):
            out[m] = F(sum(d**3 for d in range(1, m + 1) if m % d == 0))
        return out
    s = sig3()
    cols = []
    for d_lev in (1, 2, 3, 6):
        col = [F(0)] * (NN + 1)
        for i in range(NN // d_lev + 1):
            col[i * d_lev] = s[i]
        cols.append(col)
    # solve s3g = sum c_d col_d + c0*[n=0] over first rows, verify rest
    import itertools
    M = [[cols[j][i] for j in range(4)] for i in range(1, 6)]
    rhs = [s3g[i] for i in range(1, 6)]
    A4 = sp.Matrix(4, 4, lambda r, c: M[r][c])
    r4 = sp.Matrix([rhs[r] for r in range(4)])
    try:
        sol = A4.solve(r4)
        ok = all(sum(sol[j] * cols[j][i] for j in range(4)) == s3g[i]
                 for i in range(1, NN + 1))
        print('   Eisenstein fit c_(1,2,3,6) =', [str(v) for v in sol],
              ' verified to q^%d:' % NN, ok)
    except Exception as e:
        print('   Eisenstein fit failed:', e)

    # --- BZ family ---
    print(' BZ zeta(5): s3 = theta_q^3(Phat/Q), s5 = theta_q^5(P/Q):')
    for name, row, k in (('Phat', Phs, 3), ('P', Ps, 5)):
        rat = smul(row, sinv(y0, NN), NN)
        rq = compose(rat, tq, NN)
        sk = theta_series(rq, k, NN)
        print('  %s: theta^%d coeffs 1..8:' % (name, k),
              [str(sk[i]) for i in range(1, 9)])
        print('     denominators:', hprofile(sk))
        for lam in (1, 2, 4, 8, 16, 32, 3, 6, 12, 24, 48):
            if all((sk[i] * lam).denominator == 1 for i in range(NN + 1)):
                print('     %d*s is INTEGRAL to q^%d' % (lam, NN))
                break
        else:
            print('     no integral rescale in tested set')

    # --- q-Frobenius normal form and Yukawa-type series ---
    print(' q-Frobenius: ghat2 and theta^2(Y2/Y0):')
    rho = compose(ratio, tq, NN)            # (g1/y0)(t(q)) = log t - log q
    f0q = compose(fs[0], tq, NN)
    f1q = compose(fs[1], tq, NN)
    f2q = compose(fs[2], tq, NN)
    # ghat1 = f1q - f0q*rho  (should vanish)
    gh1 = [f1q[i] - smul(f0q, rho, NN)[i] for i in range(NN + 1)]
    print('   ghat1 == 0:', all(v == 0 for v in gh1))
    rho2 = smul(rho, rho, NN)
    gh2 = [f2q[i] - smul(f1q, rho, NN)[i]
           + smul(f0q, rho2, NN)[i] / 2 for i in range(NN + 1)]
    yuk = theta_series(smul(gh2, sinv(f0q, NN), NN), 2, NN)
    print('   K(q) = theta^2(ghat2/F): coeffs 1..8:',
          [str(yuk[i]) for i in range(1, 9)])
    print('   denominators:', hprofile(yuk))
    for lam in (1, 2, 3, 4, 6, 8, 12, 24):
        if all((yuk[i] * lam).denominator == 1 for i in range(NN + 1)):
            print('   %d*K integral to q^%d' % (lam, NN))
            break
    else:
        print('   no integral rescale of K in tested set')

# ================= D. FACTOR =================
def factor(p=4194301, Jmax=10, NF=40):
    print('\n== D. order-5 right factor (mod %d search) ==' % p)
    fsF = frobenius_tower(Qs if NF <= NN else
                          [F(core.Q(n)) for n in range(NF + 1)], 4, NF)
    from math import factorial
    # unknown L5 = sum_{j=0}^J t^j S_j(theta), S_0 = theta^5 fixed,
    # deg S_j <= 5.  Condition: L5 kills the block <=> slot equations
    # for k = 0..4:  sum_{i=0}^k (1/i!) L5^{(i)}(theta) f_{k-i} = 0.
    for J in range(1, Jmax + 1):
        unk = 6 * J          # S_j coefficients, j=1..J
        rows = []
        # build equations mod p
        def Sj_eval(coefvec, j, m, deriv):
            # S_j(x) = sum_d coef[j][d] x^d ; return (1/deriv!) S_j^{(deriv)}(m)
            tot = 0
            for d_ in range(deriv, 6):
                cbin = 1
                # d_!/(d_-deriv)!/deriv! * m^{d_-deriv} * deriv! /deriv!  ->
                # binom(d_,deriv)*m^(d_-deriv)
                from math import comb as C_
                tot += coefvec[(j - 1) * 6 + d_] * C_(d_, deriv) \
                    * pow(m, d_ - deriv, p)
            return tot % p
        # S_0 = x^5 contributes known terms
        eqs = []
        rhs = []
        fmod = [[int(fsF[k][m] % p if isinstance(fsF[k][m], int) else
                     (fsF[k][m].numerator * pow(fsF[k][m].denominator,
                                                p - 2, p)) % p)
                 for m in range(NF + 1)] for k in range(5)]
        from math import comb as C_
        for k in range(5):
            for Nn in range(0, NF + 1 - J):
                # coefficient of t^Nn in slot k
                # known part from S_0 = x^5: (1/i!)d^i x^5 at m: C(5,i) m^{5-i}
                kn = 0
                for i in range(0, k + 1):
                    m = Nn
                    kn = (kn + C_(5, i) * pow(m, 5 - i, p)
                          * fmod[k - i][m]) % p
                row = [0] * unk
                for j in range(1, J + 1):
                    m = Nn - j
                    if m < 0:
                        continue
                    for i in range(0, k + 1):
                        for d_ in range(i, 6):
                            row[(j - 1) * 6 + d_] = (
                                row[(j - 1) * 6 + d_]
                                + C_(d_, i) * pow(m, d_ - i, p)
                                * fmod[k - i][m]) % p
                eqs.append(row)
                rhs.append((-kn) % p)
        import numpy as np
        Mx = np.array(eqs, dtype=np.int64) % p
        b = np.array(rhs, dtype=np.int64) % p
        # solve least-squares style: gaussian elimination
        Aug = np.concatenate([Mx, b[:, None]], axis=1)
        mrows, ncols = Aug.shape
        r = 0
        piv = []
        for c in range(unk):
            nz = np.nonzero(Aug[r:, c] % p)[0]
            if not len(nz):
                continue
            pr = r + nz[0]
            if pr != r:
                Aug[[r, pr]] = Aug[[pr, r]]
            Aug[r] = Aug[r] * pow(int(Aug[r, c]), p - 2, p) % p
            col = Aug[:, c].copy()
            col[r] = 0
            nzr = np.nonzero(col)[0]
            if len(nzr):
                Aug[nzr] = (Aug[nzr] - col[nzr, None] * Aug[r][None, :]) % p
            piv.append(c)
            r += 1
        consistent = not Aug[r:, unk].any()
        print('  J=%d: unknowns %d, equations %d, rank %d, consistent: %s'
              % (J, unk, len(eqs), r, consistent))
        if consistent:
            xsol = [0] * unk
            for t_, c in enumerate(piv):
                xsol[c] = int(Aug[t_, unk])
            print('   SOLUTION FOUND at t-degree J=%d (mod p).' % J)
            print('   S_j coefficient table (mod p, rows j=1..%d, cols x^0..x^5):' % J)
            for j in range(1, J + 1):
                print('    j=%d:' % j, xsol[(j - 1) * 6:(j - 1) * 6 + 6])
            return J, xsol
    print('  no order-5 right factor with t-degree <= %d (mod p)' % Jmax)
    return None, None

if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if what in ('dwork', 'all'):
        print('== B. Dwork congruences ==')
        dwork(5)
        dwork(7)
    if what in ('qside', 'all'):
        qside()
    if what in ('factor', 'all'):
        factor()
