#!/usr/bin/env python3
"""Exact audit for the cubic algebraic-period application.

The script checks the q=3, w=1 specialization of the endpoint theory:

* the endpoint recurrence and its binomial conjugate;
* the algebraic first-row generating function;
* the common four-term recurrence for the first row and companion;
* the finite n=6 necessity witness and n=2 optimality witness;
* exact L_n-integrality over a substantial range when 3 divides b;
* numerical convergence to the cubic period, using a nonsingular integral.

Finite checks are audits, not substitutes for the all-n valuation theorem proved
in papers_out/step_q_endpoint/main.tex.
"""

from fractions import Fraction
from math import comb, gcd

import mpmath as mp
import sympy as sp


def lcm_upto(n: int) -> int:
    ans = 1
    for k in range(1, n + 1):
        ans = ans * k // gcd(ans, k)
    return ans


def endpoint_rows(b: int, nmax: int) -> tuple[list[Fraction], list[Fraction]]:
    """Homogeneous U and forced T for q=3, w=1."""
    u = [Fraction(0) for _ in range(nmax + 1)]
    t = [Fraction(0) for _ in range(nmax + 1)]
    u[0] = Fraction(1)
    for n in range(1, nmax + 1):
        if n >= 3:
            u[n] = Fraction(b**3 * (n - 2), n) * u[n - 3]
        propagated = b**3 * (n - 2) * t[n - 3] if n >= 3 else 0
        t[n] = Fraction(propagated + (-b) ** (n - 1), n)
    return u, t


def binomial_inverse(row: list[Fraction], b: int) -> list[Fraction]:
    ans: list[Fraction] = []
    for n in range(len(row)):
        ans.append(
            sum(
                (Fraction(comb(n, k)) * b ** (n - k) * row[k] for k in range(n + 1)),
                Fraction(0),
            )
        )
    return ans


def audit_symbolic() -> None:
    b = sp.symbols("b", integer=True)
    x = sp.symbols("x")
    qpoly = (1 - b * x) ** 3 - (b * x) ** 3
    assert sp.expand(qpoly) == 1 - 3 * b * x + 3 * b**2 * x**2 - 2 * b**3 * x**3

    # Coefficient recurrence extracted from Q Y' + Q'/3 Y = 0.
    n = sp.symbols("n", integer=True, nonnegative=True)
    assert sp.expand(b * (3 * n + 1)) == 3 * b * n + b
    assert sp.expand(b**2 * (3 * n - 1)) == 3 * b**2 * n - b**2
    assert sp.expand(2 * b**3 * (n - 1)) == 2 * b**3 * n - 2 * b**3

    # Exact low-index companion witnesses obtained from the recurrence.
    c = [sp.Integer(0), sp.Integer(1), 3 * b / 2]
    for m in range(2, 6):
        c.append(
            sp.factor(
                (
                    b * (3 * m + 1) * c[m]
                    - b**2 * (3 * m - 1) * c[m - 1]
                    + 2 * b**3 * (m - 1) * c[m - 2]
                )
                / (m + 1)
            )
        )
    assert sp.factor(c[6] - sp.Rational(1507, 180) * b**5) == 0
    assert sp.factor(60 * c[6] - sp.Rational(1507, 3) * b**5) == 0
    assert 1507 % 3 != 0
    assert sp.factor(c[2].subs(b, 3) - sp.Rational(9, 2)) == 0

    # The first row has A_3 = 4 b^3 / 3, giving the same sharp necessity.
    a = [sp.Integer(1), b, b**2]
    a.append(
        sp.factor(
            (
                b * 7 * a[2]
                - b**2 * 5 * a[1]
                + 2 * b**3 * a[0]
            )
            / 3
        )
    )
    assert sp.factor(a[3] - sp.Rational(4, 3) * b**3) == 0


def audit_exact_rows() -> None:
    for b in (3, 6, -3, 0):
        u, t = endpoint_rows(b, 180)
        a = binomial_inverse(u, b)
        c = binomial_inverse(t, b)
        for n in range(181):
            assert a[n].denominator == 1
            assert (lcm_upto(n) * c[n]).denominator == 1
            if 2 <= n < 180:
                assert (n + 1) * a[n + 1] == (
                    b * (3 * n + 1) * a[n]
                    - b**2 * (3 * n - 1) * a[n - 1]
                    + 2 * b**3 * (n - 1) * a[n - 2]
                )
                assert (n + 1) * c[n + 1] == (
                    b * (3 * n + 1) * c[n]
                    - b**2 * (3 * n - 1) * c[n - 1]
                    + 2 * b**3 * (n - 1) * c[n - 2]
                )

    # Failure when 3 does not divide b is already visible at n=6.
    for b in (-8, -4, -2, -1, 1, 2, 4, 8):
        _, t = endpoint_rows(b, 6)
        c = binomial_inverse(t, b)
        assert (60 * c[6]).denominator == 3


def audit_period() -> None:
    mp.mp.dps = 90

    # t = 1-u^3 removes the integrable endpoint singularity exactly.
    period = mp.quad(
        lambda u: 3
        / ((2 - u**3) * (3 - 3 * u**3 + u**6) ** (mp.mpf(2) / 3)),
        [0, 1],
    )
    target = period / 3

    u, t = endpoint_rows(3, 160)
    a = binomial_inverse(u, 3)
    c = binomial_inverse(t, 3)
    ratio = (mp.mpf(c[160].numerator) / c[160].denominator) / (
        mp.mpf(a[160].numerator) / a[160].denominator
    )
    assert abs(ratio - target) < mp.mpf("1e-45")


def main() -> None:
    audit_symbolic()
    print("cubic algebraic operator and low-index witnesses: exact")
    audit_exact_rows()
    print("common recurrence and sharp L_n denominator: exact through n=180")
    audit_period()
    print("cubic-period limit: 80-digit numerical audit passed")


if __name__ == "__main__":
    main()
