"""The DIGIT-DEFORMED Apery number.

  A_Gamma(n,k) = [ Gamma(n+k+1) / ( Gamma(k+1)^2 Gamma(n-k+1) ) ]^2

With  Pi(t) = prod_{i=1}^{t} (1 + eps/i)  and  Pib(t) = prod_{i=1}^{t} (1 - eps/i),
the Gamma(1+eps) factors CANCEL and everything is rational:

  s <= r :  A_Gamma(r+eps, s)     = A(r,s) * Pi(r+s)^2 / Pi(r-s)^2
  s = r+m :  A_Gamma(r+eps, r+m)  = eps^2 * C(r,m) * Pi(2r+m)^2 * Pib(m-1)^2
             C(r,m) = ( (2r+m)! (m-1)! / ((r+m)!)^2 )^2

So the terms with k-digit s > r are present but of order eps^2: they are exactly
the "borrow" region of the p-adic expansion.  Define

  Adig(p, r; eps) := sum_{s=0}^{p-1} A_Gamma(r+eps, s)          (FULL digit range)

Its eps-Taylor coefficients are rational and p-dependent (through the cut-off p-1).
"""
from fractions import Fraction as F
from math import comb, factorial
from core import A


def smul(x, y, M):
    z = [F(0)] * (M + 1)
    for i, xi in enumerate(x):
        if xi == 0:
            continue
        lim = min(len(y), M + 1 - i)
        for j in range(lim):
            if y[j]:
                z[i + j] += xi * y[j]
    return z


def _cum(M, sign, tmax):
    """cumulative products of (1 + sign*eps/i), i=1..t, for t=0..tmax"""
    out = [[F(1)] + [F(0)] * M]
    for i in range(1, tmax + 1):
        f = [F(0)] * (M + 1)
        f[0] = F(1)
        if M >= 1:
            f[1] = F(sign, i)
        out.append(smul(out[-1], f, M))
    return out


def _cuminv(M, tmax):
    """cumulative products of (1+eps/i)^{-1} = sum_j (-eps/i)^j"""
    out = [[F(1)] + [F(0)] * M]
    for i in range(1, tmax + 1):
        f = [F((-1) ** j, i ** j) for j in range(M + 1)]
        out.append(smul(out[-1], f, M))
    return out


_cache = {}


def Adig(p, r, M):
    """eps-Taylor coefficients c_0..c_M of sum_{s=0}^{p-1} A_Gamma(r+eps,s)"""
    key = (p, r, M)
    if key in _cache:
        return _cache[key]
    tmax = 2 * p + 2
    PI = _cum(M, 1, tmax)
    PB = _cum(M, -1, tmax)
    PV = _cuminv(M, tmax)
    tot = [F(0)] * (M + 1)
    for s in range(min(r, p - 1) + 1):
        t = smul(smul(PI[r + s], PI[r + s], M), smul(PV[r - s], PV[r - s], M), M)
        ars = A(r, s)
        for i in range(M + 1):
            if t[i]:
                tot[i] += ars * t[i]
    for m in range(1, p - r):            # s = r+m <= p-1
        C = F(factorial(2 * r + m) * factorial(m - 1), factorial(r + m) ** 2) ** 2
        t = smul(smul(PI[2 * r + m], PI[2 * r + m], M),
                 smul(PB[m - 1], PB[m - 1], M), M)
        for i in range(M - 1):
            if t[i]:
                tot[i + 2] += C * t[i]
    _cache[key] = tot
    return tot


def Adig_at(p, r, eps, M, order=None):
    c = Adig(p, r, M)
    o = M if order is None else order
    tot = F(0); pw = F(1)
    for j in range(o + 1):
        tot += c[j] * pw
        pw *= eps
    return tot
