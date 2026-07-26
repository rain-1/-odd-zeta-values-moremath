"""reconstruction: F_p samples in n  ->  rational function of n  ->  exact Q."""
from fractions import Fraction as Fr
import numpy as np
import ratrec


def rat_in_n(vals, ns, p, maxdeg=None):
    """(num, den) with den monic; num(n) = val(n)*den(n) at every sample."""
    M = len(ns)
    if maxdeg is None: maxdeg = (M - 2) // 2
    r = ratrec.null_min_deg(vals, ns, p, maxdeg)
    if r is None: return None
    num, den = r
    lead = den[-1] % p
    if lead == 0: return None
    iv = pow(lead, p - 2, p)
    num = [x * iv % p for x in num]
    den = [x * iv % p for x in den]
    return ratrec.trim(num), ratrec.trim(den)


def crt(res, mods):
    x, M = 0, 1
    for r, m in zip(res, mods):
        # solve y = x mod M, y = r mod m
        g = pow(M % m, -1, m)
        t = (r - x) % m * g % m
        x += M * t
        M *= m
    return x, M


def rat_from_crt(x, M):
    """smallest a/b with a = x*b mod M"""
    a0, a1 = M, x % M
    b0, b1 = 0, 1
    while a1 * a1 > M:
        q = a0 // a1
        a0, a1 = a1, a0 - q * a1
        b0, b1 = b1, b0 - q * b1
    if b1 == 0: return None
    if b1 < 0: a1, b1 = -a1, -b1
    if a1 * a1 > M: return None
    return Fr(a1, b1)


def lift_poly(polys, primes):
    """polys[i] = coefficient list mod primes[i]; all same length.
    returns list of Fractions or None on failure"""
    L = len(polys[0])
    if any(len(q) != L for q in polys): return None
    out = []
    for t in range(L):
        x, M = crt([q[t] for q in polys], primes)
        v = rat_from_crt(x, M)
        if v is None: return None
        out.append(v)
    return out
