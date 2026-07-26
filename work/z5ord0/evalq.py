"""Exact rational evaluation of module elements and of the T-weighted sums."""
from fractions import Fraction as Fr
from math import comb

import o0core as C

_H = {}


def Hs(m, r):
    if m <= 0:
        return Fr(0)
    key = (m, r)
    v = _H.get(key)
    if v is None:
        v = Hs(m - 1, r) + Fr(1, m ** r)
        _H[key] = v
    return v


def letter_val(L, n, k, l):
    r, a = C.parse(L)
    cn, ck, cl = C.ARGS[a]
    return Hs(cn * n + ck * k + cl * l, r)


def el_val(el, n, k, l):
    tot = Fr(0)
    for m, c in el.items():
        v = Fr(c)
        for L in m:
            v *= letter_val(L, n, k, l)
        tot += v
    return tot


def T(n, k, l):
    return (comb(n + k, n) * comb(n, k) ** 2 * comb(n + l, n)
            * comb(n, l) ** 2 * comb(n + k + l, n))


def weighted_sum(el, n):
    return sum(T(n, k, l) * el_val(el, n, k, l)
               for k in range(n + 1) for l in range(n + 1))
