"""Truncated exact power series in eps over Q, and the Gamma-deformation

   A_eps(n,k) = [ Gamma(n+eps+k+1) / ( Gamma(k+1)^2 Gamma(n+eps-k+1) ) ]^2
              = A(n,k) * exp( sum_{j>=1} lam_j(n,k) eps^j )
   lam_j(n,k) = (2 (-1)^j / j) ( H^(j)_{n-k} - H^(j)_{n+k} )        (all zeta(j) cancel)

   Adef(n; eps) = sum_k A_eps(n,k)   -- coefficients c_j(n) are RATIONAL.
"""
from fractions import Fraction as F
from core import A, Hs

M_DEFAULT = 8


def smul(x, y, M):
    z = [F(0)] * (M + 1)
    for i, xi in enumerate(x):
        if xi == 0:
            continue
        for j, yj in enumerate(y):
            if i + j > M:
                break
            if yj:
                z[i + j] += xi * yj
    return z


def sexp(x, M):
    """exp of a series with x[0] == 0"""
    assert x[0] == 0
    out = [F(0)] * (M + 1)
    out[0] = F(1)
    term = [F(0)] * (M + 1)
    term[0] = F(1)
    fact = F(1)
    for m in range(1, M + 1):
        term = smul(term, x, M)
        fact *= m
        for i in range(M + 1):
            if term[i]:
                out[i] += term[i] / fact
    return out


def lam(n, k, M):
    """the series sum_j lam_j eps^j, as a list of length M+1"""
    out = [F(0)] * (M + 1)
    for j in range(1, M + 1):
        out[j] = (F(2 * (-1) ** j, j)
                  * (Hs(n - k, j) - Hs(n + k, j)))
    return out


_cache = {}


def Adef(n, M=M_DEFAULT):
    """Taylor coefficients c_0..c_M of sum_k A_eps(n,k) in eps"""
    if (n, M) in _cache:
        return _cache[(n, M)]
    tot = [F(0)] * (M + 1)
    for k in range(n + 1):
        e = sexp(lam(n, k, M), M)
        ak = A(n, k)
        for i in range(M + 1):
            if e[i]:
                tot[i] += ak * e[i]
    _cache[(n, M)] = tot
    return tot


def Adef_at(n, eps, M=M_DEFAULT, order=None):
    """evaluate the truncated series at eps, keeping terms up to eps^order"""
    c = Adef(n, M)
    o = M if order is None else order
    tot = F(0)
    pw = F(1)
    for j in range(o + 1):
        tot += c[j] * pw
        pw *= eps
    return tot


# the b-analogue: the same deformation applied to the weighted sum
def Bdef(n, M=M_DEFAULT):
    """Taylor coefficients of sum_k A_eps(n,k) (2 H3_{n+eps} - H3_k) -- NOT used
    for the scalar law; kept for T2 experiments."""
    raise NotImplementedError
