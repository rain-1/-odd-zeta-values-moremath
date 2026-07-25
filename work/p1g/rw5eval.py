"""P1g: exact (Fraction) evaluation and verification of an R-extended weight-5
representative, saved in the same label format as work/lb5/w5_allp.json:

    "[f|g]xhxs" : [num, den]     f,g  k-monomials  ('*'-joined, '1' = empty)
                                 h    coupling monomial, s  n-monomial
Letters: A r / B r / R r  in f,g ;  C r / D r  in h ;  N r  in s.
"""
import sys, json
from fractions import Fraction as F
from math import comb

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import Hs, vp
from rlet import R_exact, D_exact


def load(fn):
    d = json.load(open(fn))
    terms = []
    for lab, (num, den) in d.items():
        fg, rest = lab.split(']x')
        f, g = fg[1:].split('|')
        h, s = rest.split('x')
        sp = lambda x: [] if x == '1' else x.split('*')
        terms.append((F(num, den), sp(f), sp(g), sp(h), sp(s)))
    return terms


_Rc = {}


def _R(n, i, r):
    key = (n, i, r)
    v = _Rc.get(key)
    if v is None:
        v = R_exact(n, i, r)
        _Rc[key] = v
    return v


_Dc = {}


def _D(n, m, r):
    key = (n, m, r)
    v = _Dc.get(key)
    if v is None:
        v = D_exact(n, m, r)
        _Dc[key] = v
    return v


_Yc = {}


def _Y(n, i, a, b):
    """sum_{i < m2 < m1 <= n+i} m1^-a m2^-b   (nested interval letter)"""
    key = (n, i, a, b)
    v = _Yc.get(key)
    if v is None:
        v = F(0)
        for m1 in range(i + 2, n + i + 1):
            for m2 in range(i + 1, m1):
                v += F(1, m1 ** a * m2 ** b)
        _Yc[key] = v
    return v


def kletter(nm, n, i):
    t = nm[0]
    if t == 'Y':
        return _Y(n, i, int(nm[1]), int(nm[2]))
    r = int(nm[1])
    if t == 'A':
        return Hs(n + i, r) - Hs(i, r)
    if t == 'B':
        return Hs(n - i, r) - Hs(i, r)
    if t == 'R':
        return _R(n, i, r)
    raise ValueError(nm)


def w5(n, k, l, terms):
    tot = F(0)
    for cf, f, g, h, s in terms:
        v = cf
        for nm in h:
            if nm[0] == 'V':
                v *= _Y(n, k + l, int(nm[1]), int(nm[2]))
                continue
            r = int(nm[1])
            v *= (Hs(n + k + l, r) - Hs(k + l, r)) if nm[0] == 'C' else _D(n, k + l, r)
        for nm in s:
            v *= _Y(n, 0, int(nm[1]), int(nm[2])) if nm[0] == 'Z' else Hs(n, int(nm[1]))
        if v == 0:
            continue
        pf = F(1)
        for nm in f:
            pf *= kletter(nm, n, k)
        for nm in g:
            pf *= kletter(nm, n, l)
        if f == g:
            tot += v * pf
        else:
            pb = F(1)
            for nm in f:
                pb *= kletter(nm, n, l)
            for nm in g:
                pb *= kletter(nm, n, k)
            tot += v * (pf + pb)
    return tot


def Tl(a, b, c):
    return (comb(a + b, a) * comb(a, b) ** 2 * comb(a + c, a) * comb(a, c) ** 2
            * comb(a + b + c, a))


def vT(a, b, c, p):
    return vp(Tl(a, b, c), p)
