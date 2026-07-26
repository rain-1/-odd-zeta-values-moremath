"""Exact low-weight evaluation of the universal Brown--Zudilin sine kernel.

This is discovery/checking code, not yet the final proof certificate.

For a,b >= 0 and p,q in {1,2}, I(a,b,p,q) denotes the universal integral

  (2 pi i)^-2 int int
    (s+a)^-p (t+b)^-q
    pi/sin(pi s) pi/sin(pi t) pi/sin(pi(s+t)) ds dt.

Brown--Zudilin express it as a piecewise integral over (0,1)^2.  The formulas
below evaluate that integral exactly in the basis

  1, zeta(2), zeta(3), zeta(4), zeta(5), zeta(2) zeta(3).

All finite harmonic sums are evaluated in Q.  Multiple zeta values of weight
at most five are reduced by the standard double-shuffle identities.
"""

from __future__ import annotations

from fractions import Fraction as Q
from math import comb, factorial

import sympy as sp

z2, z3, z4, z5, z23 = sp.symbols("z2 z3 z4 z5 z2z3")


def harm(n: int, r: int) -> Q:
    return sum((Q(1, j**r) for j in range(1, n + 1)), Q(0))


def zeta(r: int):
    return {2: z2, 3: z3, 4: z4, 5: z5}[r]


def ztail(r: int, start: int):
    """Regularised sum from start to infinity of j^-r.

    At r=1 the common divergent constant is discarded.  It cancels in the
    Brown--Zudilin combination, leaving -H_{start-1}.
    """
    if r == 1:
        return -sp.Rational(harm(start - 1, 1).numerator,
                            harm(start - 1, 1).denominator)
    h = harm(start - 1, r)
    return zeta(r) - sp.Rational(h.numerator, h.denominator)


def mzv(m: int, r: int):
    """zeta(m,r) for the convergent cases of total weight 3,4,5 used here."""
    table = {
        (2, 1): z3,
        (3, 1): z4 / 4,
        (2, 2): 3 * z4 / 4,
        (4, 1): 2 * z5 - z23,
        (3, 2): 3 * z23 - sp.Rational(11, 2) * z5,
        (2, 3): sp.Rational(9, 2) * z5 - 2 * z23,
    }
    return table[(m, r)]


def shifted_product_sum(r: int, m: int, h: int):
    """Sum_{t>=1} 1/(t^r (t+h)^m), reduced by partial fractions."""
    assert r >= 1 and m >= 1 and h >= 1
    ans = 0
    # Principal part at t=0.
    aa = {}
    for i in range(1, r + 1):
        aa[i] = Q((-1) ** (r - i) * comb(m + r - i - 1, r - i),
                  h ** (m + r - i))
    # Principal part at t=-h.
    bb = {}
    for j in range(1, m + 1):
        bb[j] = Q((-1) ** r * comb(r + m - j - 1, m - j),
                  h ** (r + m - j))

    # The divergent harmonic constants cancel because aa[1] + bb[1] = 0.
    assert aa[1] + bb[1] == 0
    ans -= sp.Rational(bb[1].numerator, bb[1].denominator) * sp.Rational(
        harm(h, 1).numerator, harm(h, 1).denominator)
    for i in range(2, r + 1):
        ans += sp.Rational(aa[i].numerator, aa[i].denominator) * zeta(i)
    for j in range(2, m + 1):
        hj = harm(h, j)
        ans += sp.Rational(bb[j].numerator, bb[j].denominator) * (
            zeta(j) - sp.Rational(hj.numerator, hj.denominator))
    return sp.expand(ans)


def euler_harmonic_sum(r: int):
    """Sum_{t>=1} H_t/t^r for r=2,3 (the only cases required)."""
    return {2: 2 * z3, 3: sp.Rational(5, 4) * z4}[r]


def coupled_tail(r: int, m: int, start: int, gap: int):
    """Sum_{t>=start} t^-r * Z_m(t+gap), with Z_1 regularised."""
    assert start >= 1 and gap >= 1
    if m == 1:
        # Z_1(t+gap) = -H_{t+gap-1}.
        full = euler_harmonic_sum(r)
        for h in range(1, gap):
            full += shifted_product_sum(r, 1, h)
        prefix = 0
        for t in range(1, start):
            hh = harm(t + gap - 1, 1)
            prefix += sp.Rational(hh.numerator, hh.denominator) / t**r
        return sp.expand(-full + prefix)

    ans = mzv(m, r)
    for h in range(1, gap):
        ans -= shifted_product_sum(r, m, h)
    for t in range(1, start):
        ans -= sp.Rational(1, t**r) * ztail(m, t + gap)
    return sp.expand(ans)


def triangle(a: int, b: int, p: int, q: int):
    """Contribution from 0<u<v<1 after u=xv."""
    assert a >= 0 and b >= 0 and p in (1, 2) and q in (1, 2)
    start = a + 1
    gap = b + 1
    ans = 0

    # First term of f: log(xv), hence total power (log(xv))^p.
    for i in range(p + 1):
        r = i + 1
        m = p - i + q
        coeff = ((-1) ** (p + q - 1) * comb(p, i)
                 * factorial(i) * factorial(p - i + q - 1))
        ans += coeff * coupled_tail(r, m, start, gap)

    # Second term of f: -log(x).
    dstart = a + b + 1
    for i in range(p):
        r = i + 2
        m = p + q - 1 - i
        coeff = ((-1) ** (p + q) * comb(p - 1, i)
                 * factorial(i + 1) * factorial(p + q - 2 - i))
        ans += coeff * ztail(r, start) * ztail(m, dstart)
    return sp.expand(ans)


def universal(a: int, b: int, p: int, q: int):
    # 1/(t+a)^p = Gamma(p)^-1 int_0^1
    # u^(t+a) (-log u)^(p-1) du/u.  The printed BZ display writes log
    # rather than -log; comparison with the defining contour integral fixes
    # the factor below (and changes only the (1,2)/(2,1) cases).
    laplace_sign = (-1) ** (p + q - 2)
    return sp.expand(laplace_sign
                     * (triangle(a, b, p, q) + triangle(b, a, q, p))
                     / (factorial(p - 1) * factorial(q - 1)))


if __name__ == "__main__":
    for a in range(1, 4):
        for b in range(1, 4):
            print("a,b =", a, b)
            for p in (1, 2):
                for q in (1, 2):
                    print(" ", p, q, sp.collect(universal(a, b, p, q),
                                                [z2, z3, z4, z5, z23]))
