"""CLOSED FORM of the rational part [1] I^{p,q}_{k,l}, derived from section 8
of Z5CF_BARNES (the uniform evaluation lemma), not fitted.

Notation:
  H^(r)_x                      ordinary harmonic numbers
  S_{s,j}(x) = sum_{h=1}^{x} H^(j)_h / h^s              (univariate Euler sum)
  U_{r,m}(a,b) = sum_{t=1}^{a} H^(m)_{t+b} / t^r        (bivariate coupled sum)

Section 8 gives, with A=a+1, d=b+1,

  F^{p,q}_{a,b} = (-1)^(p+q-1) sum_{i=0}^{p} C(p,i) i! (p-i+q-1)! S_{i+1,p-i+q}(A,d)
                + (-1)^(p+q)   sum_{i=0}^{p-1} C(p-1,i)(i+1)!(p+q-2-i)!
                               Z_{i+2}(A) Z_{p+q-1-i}(A+d-1)

and  I^{p,q}_{a,b} = (-1)^(p+q-2) (F^{p,q}_{a,b} + F^{q,p}_{b,a}) / ((p-1)!(q-1)!).

Rational parts:
  [1] Z_m(N) = -H^(m)_{N-1}, so [1] Z_i(A) Z_j(A+d-1) = H^(i)_a H^(j)_{a+b};
  [1] S_{r,m}(A,d) = (-1)^r sum_{j=1}^{m} C(r+m-j-1, m-j) S_{r+m-j, j}(b)
                     + U_{r,m}(a,b).

The second line is the whole content: the divergent harmonic constants cancel
inside U_{r,m}(h) (section 8), and the only surviving rational objects are a
univariate Euler sum in b alone and ONE bivariate coupled sum.
"""
from fractions import Fraction as Fr
from math import comb, factorial

from alpha import H, S, U


def rat_S(r, m, a, b):
    """[1] S_{r,m}(a+1, b+1)"""
    out = Fr(0)
    for j in range(1, m + 1):
        out += Fr((-1) ** r * comb(r + m - j - 1, m - j)) * S(b, r + m - j, j)
    return out + U(a, b, r, m)


def rat_F(p, q, a, b):
    out = Fr(0)
    sgn1 = (-1) ** (p + q - 1)
    for i in range(0, p + 1):
        c = comb(p, i) * factorial(i) * factorial(p - i + q - 1)
        out += sgn1 * c * rat_S(i + 1, p - i + q, a, b)
    sgn2 = (-1) ** (p + q)
    for i in range(0, p):
        c = comb(p - 1, i) * factorial(i + 1) * factorial(p + q - 2 - i)
        out += sgn2 * c * H(a, i + 2) * H(a + b, p + q - 1 - i)
    return out


def rat_I(p, q, k, l):
    sgn = (-1) ** (p + q - 2)
    return Fr(sgn, factorial(p - 1) * factorial(q - 1)) * (
        rat_F(p, q, k, l) + rat_F(q, p, l, k))


# ------------------------------------------------------------ explicit I22 --
def rat_I22_explicit(k, l):
    """the hand-collected form of [1] I^{2,2}:

      6 [S_{1,4}(k)+S_{1,4}(l)] + 2 [S_{2,3}(k)+S_{2,3}(l)]
      - 6 [U_{1,4}(k,l)+U_{1,4}(l,k)]
      - 4 [U_{2,3}(k,l)+U_{2,3}(l,k)]
      - 2 [U_{3,2}(k,l)+U_{3,2}(l,k)]
      + 2 [H2_k H3_{k+l} + H3_k H2_{k+l} + H2_l H3_{k+l} + H3_l H2_{k+l}]
    """
    out = 6 * (S(k, 1, 4) + S(l, 1, 4)) + 2 * (S(k, 2, 3) + S(l, 2, 3))
    out -= 6 * (U(k, l, 1, 4) + U(l, k, 1, 4))
    out -= 4 * (U(k, l, 2, 3) + U(l, k, 2, 3))
    out -= 2 * (U(k, l, 3, 2) + U(l, k, 3, 2))
    out += 2 * (H(k, 2) * H(k + l, 3) + H(k, 3) * H(k + l, 2)
                + H(l, 2) * H(k + l, 3) + H(l, 3) * H(k + l, 2))
    return out
