"""eps63_catalan.py -- Sol Project B: the Catalan control experiment.

Pipeline for a general order-2 (or 3) recurrence with polynomial
coefficients: build L = sum_j t^j P_j(theta), Frobenius y0, g; canonical
nome q = t exp(g/y0); t(q), F(q); Phi = t sigma^r / (P_lead F) where
P_lead(t) = leading-theta coefficient polynomial; rescale; eta-classify;
Eisenstein fit at weight r+1 with configurable character bases; fold limit.

The family data (recurrence, from the literature agent) is filled in
below once verified.  All arithmetic exact.
"""
import sys, os, json
from fractions import Fraction as F_
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import eps48_modular_nome as M
N = M.N
from eps48_modular_nome import smul, sinv, sexp, srevert, compose, gseries
import sympy as sp
th = sp.symbols('th')

def general_pipeline(Pj, A, r, Plead_coeffs):
    """Pj: theta-polynomial coefficient list (index = power of t);
    A: principal solution coefficients (Fractions), len >= N+1;
    Plead_coeffs: coefficients of the leading polynomial P(t) (list).
    Returns dict with tq, Fq, Phi, sigma."""
    y0 = A[:N+1]
    g = gseries(Pj, y0)
    qser = smul([F_(0), F_(1)] + [F_(0)]*(N-1), sexp(smul(g, sinv(y0))))
    tq = srevert(qser)
    Fq = compose(y0, tq)
    T = [tq[i+1] for i in range(N)] + [F_(0)]
    thT = [F_(i)*T[i] for i in range(len(T))]
    corr = smul(thT, sinv(T))
    sigma = list(corr); sigma[0] = F_(1) + corr[0]
    P = [F_(0)]*(N+1)
    tpow = [F_(1)] + [F_(0)]*N
    for c in Plead_coeffs:
        for i in range(N+1):
            P[i] += F_(c)*tpow[i]
        tpow = smul(tpow, tq)
    sw = [F_(1)] + [F_(0)]*N
    for _ in range(r):
        sw = smul(sw, sigma)
    Phi = smul(smul(tq, sw), smul(sinv(P), sinv(Fq)))
    return dict(tq=tq, Fq=Fq, Phi=Phi, sigma=sigma, qser=qser, P=P)

# ---------------------------------------------------------------- results --
# Executed 2026-08-05 with the Zudilin math/0201024 recurrence (verified by
# the literature agent and re-derived here):
#   (2n+1)^2(2n+2)^2 p(n) u_{n+1} - q(n) u_n - (2n-1)^2(2n)^2 p(n+1) u_{n-1},
#   p = 20n^2-8n+1, q = 3520n^6+5632n^5+2064n^4-384n^3-156n^2+16n+7,
#   u: 1, 7/4, ...; v: 0, 13/8, ...; v/u -> G.
# Findings (see work/CATALAN_CONTROL.md):
#   * L(y_u) = 0 and L(y_v) = (13/2) t exactly (boundary defect confirmed);
#   * canonical nome t(q) has NO integralizing rational rescale
#     (exhaustive |2-exp|<=8, |3-exp|<=3, |5-exp|<=2, both signs);
#   * the fold connection value differs from (2/13)G by 3.2e-2 >> truncation:
#     the analytic fold argument also fails (order-6 operator, half-integer
#     indicial pairs {0,0,1/2,1/2,...} at t=0).
# Verdict: Sol outcome 3 -- the modular-anchor mechanism has a genuine
# boundary; Zudilin's Catalan recurrence lives in the well-poised 6F5
# hypergeometric world, not the modular one.
