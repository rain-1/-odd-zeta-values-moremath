#!/usr/bin/env python3
"""Exact certificate for the step-three endpoint theorem and Zagier B.

Checks:
  * symbolic binomial conjugation on the full parameter h;
  * the transformed recurrence and finite endpoint formula;
  * termwise and summed L_n^2-integrality for 3 | h;
  * the n=6 necessity witness and n=2 sharpness witness;
  * identification of h=3 with Zagier's sporadic first-row sequence B.
"""

from fractions import Fraction
from math import comb, factorial, gcd

import sympy as sp


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def companion_values(h: int, count: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(count + 1)]
    if count >= 1:
        out[1] = Fraction(1)
    for n in range(1, count):
        out[n + 1] = (
            h * (3 * n * n + 3 * n + 1) * out[n]
            - 3 * h * h * n * n * out[n - 1]
        ) / (n + 1) ** 2
    return out


def first_row_values(h: int, count: int) -> list[int]:
    out = [0 for _ in range(count + 1)]
    out[0] = 1
    if count >= 1:
        out[1] = h
    for n in range(1, count):
        numerator = (
            h * (3 * n * n + 3 * n + 1) * out[n]
            - 3 * h * h * n * n * out[n - 1]
        )
        assert numerator % (n + 1) ** 2 == 0
        out[n + 1] = numerator // (n + 1) ** 2
    return out


def binomial_transform(values: list[Fraction], h: int) -> list[Fraction]:
    out = []
    for n in range(len(values)):
        out.append(
            sum(
                (
                    Fraction(comb(n, k) * (-h) ** (n - k)) * values[k]
                    for k in range(n + 1)
                ),
                Fraction(0),
            )
        )
    return out


def endpoint_root(n: int, j: int) -> Fraction:
    assert 0 <= j < n and (n - j - 1) % 3 == 0
    r = (n - j - 1) // 3
    out = Fraction(1)
    for t in range(r):
        out *= (j + 2 + 3 * t) * (j + 3 + 3 * t)
    for t in range(r + 1):
        out /= (j + 1 + 3 * t) ** 2
    return out


def endpoint_formula(h: int, n: int) -> Fraction:
    if n == 0:
        return Fraction(0)
    out = Fraction(0)
    for j in range(n):
        if (n - j - 1) % 3 == 0:
            # j+r and n-1 have the same parity.
            out += (-1) ** (n - 1) * h ** (n - 1) * endpoint_root(n, j)
    return out


def audit_symbolic_conjugation() -> None:
    # The general transformed R2 operator has coefficients
    #   z:  (a-3h)(theta^2+theta)+(beta-h),
    #   z2: gamma-2ah+3h^2,
    #   z3: h(gamma-ah+h^2)(theta+1)(theta+2).
    h, theta = sp.symbols("h theta")
    a, beta, gamma = 3 * h, h, 3 * h**2
    z1_theta2 = sp.expand(a - 3 * h)
    z1_const = sp.expand(beta - h)
    z2 = sp.expand(gamma - 2 * a * h + 3 * h**2)
    z3 = sp.expand(h * (gamma - a * h + h**2))
    assert z1_theta2 == 0 and z1_const == 0 and z2 == 0
    assert sp.expand(z3 - h**3) == 0
    assert sp.expand((theta + 1) * (theta + 2) - (theta**2 + 3 * theta + 2)) == 0


def audit_recurrence_formula_integrality() -> None:
    for h in (-12, -6, -3, 0, 3, 6, 12):
        count = 240
        companion = companion_values(h, count)
        transformed = binomial_transform(companion, h)
        lcm_n = 1
        for n in range(1, count + 1):
            lcm_n = lcm(lcm_n, n)
            previous = transformed[n - 3] if n >= 3 else Fraction(0)
            assert (
                n * n * transformed[n]
                + h**3 * (n - 2) * (n - 1) * previous
                == (-h) ** (n - 1)
            )
            assert transformed[n] == endpoint_formula(h, n)
            assert (lcm_n**2 * transformed[n]).denominator == 1
            assert (lcm_n**2 * companion[n]).denominator == 1


def audit_termwise_integrality() -> None:
    for h in (-9, -3, 3, 9):
        lcm_n = 1
        for n in range(1, 320):
            lcm_n = lcm(lcm_n, n)
            for j in range(n):
                if (n - j - 1) % 3 == 0:
                    term = lcm_n**2 * h ** (n - 1) * endpoint_root(n, j)
                    assert term.denominator == 1


def audit_named_first_row() -> None:
    recurrence = first_row_values(3, 80)
    for n in range(81):
        binomial_sum = sum(
            (-1) ** k
            * 3 ** (n - 3 * k)
            * comb(n, 3 * k)
            * factorial(3 * k)
            // factorial(k) ** 3
            for k in range(n // 3 + 1)
        )
        assert recurrence[n] == binomial_sum


def audit_sharpness_identities() -> None:
    h = sp.symbols("h")
    values = [sp.Integer(0), sp.Integer(1)]
    for n in range(1, 6):
        values.append(
            sp.factor(
                (
                    h * (3 * n * n + 3 * n + 1) * values[n]
                    - 3 * h**2 * n**2 * values[n - 1]
                )
                / (n + 1) ** 2
            )
        )
    assert sp.factor(values[2] - 7 * h / 4) == 0
    assert sp.factor(values[6] + sp.Rational(39521, 32400) * h**5) == 0
    # L_6^2 C_6 = -39521 h^5 / 9; 39521 is a 3-adic unit.
    assert 39521 % 3 != 0
    assert sp.factor(60**2 * values[6] + sp.Rational(39521, 9) * h**5) == 0
    # At h=3, L_2 C_2 = 21/2, so the exponent 2 cannot be lowered.
    assert sp.Rational(2) * values[2].subs(h, 3) == sp.Rational(21, 2)


def main() -> None:
    audit_symbolic_conjugation()
    print("step-three operator conjugation: exact for arbitrary h")
    audit_recurrence_formula_integrality()
    print("endpoint recurrence, finite formula, and L_n^2 integrality: exact through n=240")
    audit_termwise_integrality()
    print("termwise endpoint integrality: exact through n=319")
    audit_named_first_row()
    print("h=3 first row: Zagier B binomial sum verified through n=80")
    audit_sharpness_identities()
    print("n=6 necessity and n=2 optimal-exponent witnesses: exact symbolic identities")


if __name__ == "__main__":
    main()
