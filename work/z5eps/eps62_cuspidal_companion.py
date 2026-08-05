"""eps62_cuspidal_companion.py -- Sol Project D: the first deliberately
CUSPIDAL companion, built on Apery's own zeta(3) curve (family gamma, level 6).

S_4(Gamma_0(6)) is one-dimensional, spanned by f = (eta_1 eta_2 eta_3 eta_6)^2
= q - 2q^2 - 3q^3 + 4q^4 + 6q^5 + 6q^6 - 16q^7 + ...  (newform 6.4.a.a).

Construction: y^f = F_gamma * theta_q^{-3} f, expanded in t = t_gamma:
  L_gamma(y^f) = P(t) F f / sigma^3 = t * f/Phi_gamma =: R(t)
so B^f(n) := [t^n] y^f satisfies the Apery zeta(3) recurrence with the
inhomogeneous right side given by R's coefficients.

Deliverables:
  1. exact B^f(n), n <= N;
  2. rational reconstruction of R(t) (Pade over exact series);
  3. denominator profile of B^f(n) (vs d_n^3 for Apery's own companion);
  4. the fold connection value xi_f = Theta_f(q_c) + F Theta_f'/F' and PSLQ
     against the critical L-values L(f,1), L(f,2), L(f,3) and pi powers.

Run with EPS48_N=60 for the numeric part.
"""
import sys, os
from fractions import Fraction as F_
from math import gcd, lcm
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import eps48_modular_nome as M
N = M.N
from eps48_modular_nome import smul, sinv, sexp, srevert, compose, gseries, eta_quot
import sympy as sp
th = sp.symbols('th')

def gamma_data():
    a, b, c = 17, 5, 1
    Pj = [th**3, -sp.expand((2*th+1)*(a*th**2 + a*th + b)),
          sp.expand((th+1)*(c*(th+1)**2))]
    A = [F_(1), F_(5)]
    for n in range(1, N+2):
        A.append((F_((2*n+1)*(a*n*n + a*n + b))*A[n]
                  - F_(n*(c*n*n))*A[n-1]) / F_((n+1)**3))
    y0 = A[:N+1]
    g = gseries(Pj, y0)
    qser = smul([F_(0), F_(1)] + [F_(0)]*(N-1), sexp(smul(g, sinv(y0))))
    tq = srevert(qser)
    Fq = compose(y0, tq)
    return tq, Fq, qser

def cusp_f():
    """(eta1 eta2 eta3 eta6)^2 with q-prefactor q^{(1+2+3+6)*2/24}=q^1."""
    ser = eta_quot({1: 2, 2: 2, 3: 2, 6: 2}, N)
    out = [F_(0)]*(N+1)
    for i in range(N):
        out[i+1] = ser[i]
    return out

def theta_inv(ser, r):
    return [F_(0)] + [ser[m]/F_(m)**r for m in range(1, len(ser))]

def pade_reconstruct(ser, dmax=8):
    """find polys U,V (deg<=dmax) with ser = U/V exactly to q^N."""
    t = sp.symbols('t')
    S = sum(sp.Rational(x.numerator, x.denominator)*t**i
            for i, x in enumerate(ser))
    for dv in range(0, dmax+1):
        for du in range(0, dmax+1):
            # solve V*S - U = O(t^{du+dv+2}) with enough check margin
            vc = sp.symbols('v0:%d' % (dv+1))
            uc = sp.symbols('u0:%d' % (du+1))
            V = sum(vc[i]*t**i for i in range(dv+1))
            U = sum(uc[i]*t**i for i in range(du+1))
            E = sp.expand(V*S - U)
            eqs = [E.coeff(t, k) for k in range(0, N+1)]
            sol = sp.solve(eqs + [vc[0]-1], list(vc)+list(uc), dict=True)
            if sol:
                s = sol[0]
                return (sp.expand(U.subs(s)), sp.expand(V.subs(s)))
    return None

if __name__ == '__main__':
    tq, Fq, qser = gamma_data()
    f = cusp_f()
    Th = theta_inv(f, 3)
    y = smul(Fq, Th)
    Bf = compose(y, qser)            # coefficients in t
    print('B^f(n), n=0..12:')
    for n in range(13):
        print('  %2d  %s' % (n, Bf[n]))
    dens = [Bf[n].denominator for n in range(N+1)]
    print('denominators n=1..20:', dens[1:21])
    # compare with d_n^3 (lcm(1..n)^3)
    from sympy import primefactors
    dn = 1
    prof = []
    for n in range(1, min(N, 24)+1):
        dn = lcm(dn, n)
        q_, r_ = divmod(dn**3, dens[n])
        prof.append((n, 'd_n^3/den in Z' if r_ == 0 else 'NO'))
    print('d_n^3 * B^f(n) integral?', all(p[1] != 'NO' for p in prof))
    bad = [p for p in prof if p[1] == 'NO']
    if bad: print('   fails at', bad[:6])
    # inhomogeneity R(t) = t * f/Phi ; series in q then to t
    sigma_num = None
    T = [tq[i+1] for i in range(N)] + [F_(0)]
    thT = [F_(i)*T[i] for i in range(len(T))]
    corr = smul(thT, sinv(T))
    sigma = list(corr); sigma[0] = F_(1) + corr[0]
    P = [F_(0)]*(N+1); P[0] = F_(1)
    t2 = smul(tq, tq)
    for i in range(N+1):
        P[i] += F_(-34)*tq[i] + t2[i]
    s3 = smul(sigma, smul(sigma, sigma))
    Rq = smul(smul(P, smul(Fq, f)), sinv(s3))
    Rt = compose(Rq, qser)
    print('R(t) series:', [str(x) for x in Rt[:10]])
    pr = pade_reconstruct(Rt[:min(N+1, 30)], dmax=6)
    print('R(t) rational reconstruction:', pr)
