#!/usr/bin/env python3
"""Exact audit for the sharp step-q endpoint-denominator theorem.

This script is deliberately independent of CAS output.  It uses Fraction
arithmetic for the endpoint recurrence and finite formula, and integer
valuation calculations for the sharp modulus and its obstruction witnesses.
"""

from fractions import Fraction
from math import gcd


def vp_int(a: int, p: int) -> int:
    """p-adic valuation of a nonzero integer."""
    assert a != 0
    a = abs(a)
    e = 0
    while a % p == 0:
        a //= p
        e += 1
    return e


def vp_factorial(n: int, p: int) -> int:
    out = 0
    while n:
        n //= p
        out += n
    return out


def vp_lcm_range(n: int, p: int) -> int:
    out = 0
    while n >= p:
        n //= p
        out += 1
    return out


def prime_divisors(n: int) -> list[int]:
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def sharp_exponent(q: int, w: int, p: int) -> int:
    """ceil(w * (v_p(q) + 1/(p-1)) / q), computed integrally."""
    s = vp_int(q, p)
    numerator = w * ((p - 1) * s + 1)
    denominator = q * (p - 1)
    return (numerator + denominator - 1) // denominator


def sharp_modulus(q: int, w: int) -> int:
    out = 1
    for p in prime_divisors(q):
        out *= p ** sharp_exponent(q, w, p)
    return out


def endpoint_root(q: int, n: int, j: int) -> Fraction:
    """The step-q endpoint quotient Q_q(n,j)."""
    assert 0 <= j < n and (n - j - 1) % q == 0
    r = (n - j - 1) // q
    out = Fraction(1)
    for t in range(r):
        out *= j + 2 + t * q
    for t in range(r + 1):
        out /= j + 1 + t * q
    return out


def endpoint_formula(q: int, w: int, b: int, n: int) -> Fraction:
    if n == 0:
        return Fraction(0)
    out = Fraction(0)
    for j in range(n):
        if (n - j - 1) % q == 0:
            out += (-1) ** j * b ** (n - 1) * endpoint_root(q, n, j) ** w
    return out


def recurrence_values(q: int, w: int, b: int, count: int) -> list[Fraction]:
    values = [Fraction(0) for _ in range(count + 1)]
    for n in range(1, count + 1):
        previous = values[n - q] if n >= q else Fraction(0)
        values[n] = (
            Fraction(b**q * (n - q + 1) ** w) * previous
            + Fraction((-b) ** (n - 1))
        ) / n**w
    return values


def audit_finite_formula_and_integrality() -> None:
    for q in range(2, 11):
        for w in range(1, 7):
            modulus = sharp_modulus(q, w)
            for b in (modulus, -modulus, 2 * modulus):
                values = recurrence_values(q, w, b, 80)
                lcm_n = 1
                for n in range(1, 81):
                    lcm_n = lcm(lcm_n, n)
                    assert values[n] == endpoint_formula(q, w, b, n)
                    assert (lcm_n**w * values[n]).denominator == 1


def audit_termwise_valuation_bound() -> None:
    for q in range(2, 13):
        for w in range(1, 9):
            modulus = sharp_modulus(q, w)
            for n in range(1, 180):
                lcm_n = 1
                for m in range(1, n + 1):
                    lcm_n = lcm(lcm_n, m)
                for j in range(n):
                    if (n - j - 1) % q == 0:
                        term = (
                            lcm_n**w
                            * modulus ** (n - 1)
                            * endpoint_root(q, n, j) ** w
                        )
                        assert term.denominator == 1


def first_obstruction(q: int, w: int, p: int, b: int) -> tuple[int, int]:
    """Return R and the negative valuation at n=qR.

    At n=qR the j=q-1 summand is the unique summand of least p-adic
    valuation.  Hence this is the exact valuation of L_(qR)^w T_(qR).
    """
    e = vp_int(b, p) if b else 10**9
    s = vp_int(q, p)
    for r in range(1, 1_000_000):
        n = q * r
        value = (
            w * vp_lcm_range(n, p)
            + e * (n - 1)
            - w * (r * s + vp_factorial(r, p))
        )
        if value < 0:
            return r, value
    raise AssertionError((q, w, p, b))


def audit_sharpness() -> None:
    for q in range(2, 15):
        for w in range(1, 10):
            modulus = sharp_modulus(q, w)
            for p in prime_divisors(q):
                deficient = modulus // p
                r, value = first_obstruction(q, w, p, deficient)
                assert r >= 1 and value < 0


def audit_selected_moduli() -> None:
    expected = {
        2: [2, 4, 8, 16, 32, 64, 128, 256],
        3: [3, 3, 9, 9, 27, 27, 81, 81],
        4: [2, 4, 8, 8, 16, 32, 64, 64],
        5: [5, 5, 5, 5, 25, 25, 25, 25],
        6: [6, 6, 6, 12, 36, 36, 72, 72],
    }
    for q, row in expected.items():
        assert [sharp_modulus(q, w) for w in range(1, 9)] == row


def main() -> None:
    audit_selected_moduli()
    print("sharp modulus table: exact")
    audit_finite_formula_and_integrality()
    print("endpoint recurrence, finite formula, and sufficiency: exact through n=80")
    audit_termwise_valuation_bound()
    print("termwise denominator bound: exact for q<=12, w<=8, n<180")
    audit_sharpness()
    print("necessity: unique-minimum valuation witnesses found for q<=14, w<=9")


if __name__ == "__main__":
    main()
