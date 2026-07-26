"""Exact region decomposition of A(ap+r, cp+s) mod p^3.

Notation (n = ap+r, k = cp+s, 0<=a,c,r,s<p):

  R(M,t) := prod_{i=1}^{t} (Mp+i) = t! * prod_{i<=t}(1 + Mp/i)
  W(M)   := prod_{j=0}^{M-1} prod_{t=1}^{p-1}(jp+t)   ==  ((p-1)!)^M  (mod p^3)

EXACT factorisations (no Lucas, no congruence):

  c<=a, s<=r:   C(ap+r,cp+s)      = C(a,c) * W(a)/(W(c)W(a-c)) * R(a,r)/(R(c,s)R(a-c,r-s))
  any a,c,r,s:  C((a+c)p+r+s,cp+s) = C(a+c,c)* W(a+c)/(W(c)W(a)) * R(a+c,r+s)/(R(c,s)R(a,r))

so for c<=a, s<=r (NO constraint r+s<p or a+c<p):

  A(ap+r,cp+s) = A(a,c) * A(r,s) * Rat(a,c;r,s) * (Wpart)^2,  Wpart == 1 mod p^3,
  Rat = [ prod_{i<=r+s}(1+(a+c)p/i) / ( prod_{i<=s}(1+cp/i)^2 prod_{i<=r-s}(1+(a-c)p/i) ) ]^2

Three regions contribute mod p^3:

  I     s<=r, r+s<p    : Rat = 1 + 2p*L1 + p^2*(2 L1^2 - L2) + O(p^3)
  II-a  s<=r, r+s>=p   : A(r,s) has v_p = 2; Rat -> (1+a+c)^2 ; term = p^2 A(a,c)(1+a+c)^2 D(r,s)
  II-b  s=r+m>r, 2r+m<p: term = p^2 (a-c)^2 A(a,c) C(r,m)

with  D(r,s) = A(r,s)/p^2 == ((r+s-p)!/(s!^2 (r-s)!))^2   (mod p)
      C(r,m) = ((2r+m)! (m-1)! / ((r+m)!)^2)^2.
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/apdef')
from fractions import Fraction as F
from math import comb, factorial
from functools import lru_cache
from core import A, Hs, av, vp, modp, modpk


# ------------------------------------------------------------------ channels
@lru_cache(maxsize=None)
def sigmas(r):
    """the three (a,c)-channel sums over the FULL s<=r range (rationals in r only)"""
    a2 = ac = cc = F(0)
    for s in range(r + 1):
        Ars = A(r, s)
        u = Hs(r + s, 1) - Hs(r - s, 1)
        v = Hs(r + s, 1) + Hs(r - s, 1) - 2 * Hs(s, 1)
        a2 += Ars * (2 * u * u - (Hs(r + s, 2) - Hs(r - s, 2)))
        ac += Ars * (4 * u * v - 2 * (Hs(r + s, 2) + Hs(r - s, 2)))
        # NB sign: [c^2] Lam2 = H2_{r+s} - 2 H2_s - H2_{r-s}   (apdef/channels.py
        # and the paper both print +H2_{r-s}; that is a typo, see t_cellwise.py)
        cc += Ars * (2 * v * v - (Hs(r + s, 2) - 2 * Hs(s, 2) - Hs(r - s, 2)))
    return a2, ac, cc


@lru_cache(maxsize=None)
def Cfun(r, m):
    """C(r,m) = ((2r+m)!(m-1)!/((r+m)!)^2)^2  -- the eps^2 weight of the borrow term"""
    return F(factorial(2 * r + m) * factorial(m - 1), factorial(r + m) ** 2) ** 2


def Xi(p, r):
    """Xi_r = sum_{m>=1, r+m<=p-1} C(r,m)   (terms with 2r+m>=p are 0 mod p)"""
    return sum((Cfun(r, m) for m in range(1, p - r)), F(0))


def Delta(p, r):
    """Delta_r = sum_{s<=r, r+s>=p} A(r,s)/p^2   (exact rational; p-integral)"""
    tot = F(0)
    for s in range(r + 1):
        if r + s >= p:
            tot += F(A(r, s), p ** 2)
    return tot


# ------------------------------------------------------------------ moments
@lru_cache(maxsize=None)
def moments(a):
    """a_a, a'_a = sum c A(a,c), a''_a = sum c^2 A(a,c)"""
    m0 = sum(A(a, c) for c in range(a + 1))
    m1 = sum(c * A(a, c) for c in range(a + 1))
    m2 = sum(c * c * A(a, c) for c in range(a + 1))
    return m0, m1, m2


@lru_cache(maxsize=None)
def Ur(r):
    return sum((A(r, s) * (Hs(r + s, 1) - Hs(r - s, 1)) for s in range(r + 1)), F(0))


@lru_cache(maxsize=None)
def Vr(r):
    return sum((A(r, s) * (Hs(r + s, 1) + Hs(r - s, 1) - 2 * Hs(s, 1))
                for s in range(r + 1)), F(0))
