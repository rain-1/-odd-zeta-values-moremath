#!/usr/bin/env python3
"""Exact audit of the low-prime endpoint-residue law for the compact w5 form.

This is evidence for the finite-state Endpoint Residue Lemma recorded in
ENDPOINT_BREAKTHROUGH.md.  It is deliberately independent of floating point and
checks every cell in the stated range.
"""

from fractions import Fraction
from functools import lru_cache
from math import comb


@lru_cache(maxsize=None)
def harmonic(n, weight):
    if n <= 0:
        return Fraction(0)
    return harmonic(n - 1, weight) + Fraction(1, n ** weight)


def shell(n, k, ell):
    return (comb(n + k, n) * comb(n, k) ** 2
            * comb(n + ell, n) * comb(n, ell) ** 2
            * comb(n + k + ell, n))


def compact_w5(n, k, ell):
    a1k = harmonic(n + k, 1) - harmonic(k, 1)
    a1l = harmonic(n + ell, 1) - harmonic(ell, 1)
    b1k = harmonic(n - k, 1) - harmonic(k, 1)
    b1l = harmonic(n - ell, 1) - harmonic(ell, 1)
    a2k = harmonic(n + k, 2) - harmonic(k, 2)
    a2l = harmonic(n + ell, 2) - harmonic(ell, 2)
    alpha = a1k - a1l
    beta = b1k - b1l
    return (harmonic(n + k, 5)
            + Fraction(1, 2) * (alpha - beta) * harmonic(n + k, 4)
            + Fraction(1, 4) * (a2k + a2l - alpha ** 2 - 2 * alpha * beta)
            * harmonic(n + k, 3))


def vp_integer(value, prime):
    if value == 0:
        return 10 ** 9
    value = abs(value)
    out = 0
    while value % prime == 0:
        out += 1
        value //= prime
    return out


def vp(value, prime):
    value = Fraction(value)
    return vp_integer(value.numerator, prime) - vp_integer(value.denominator, prime)


def unit_residue(value, prime, modulus):
    """Residue modulo modulus after removing the exact prime valuation."""
    value = Fraction(value)
    value /= prime ** vp(value, prime)
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def prime_power_floor(n, prime):
    power = 1
    while power * prime <= n:
        power *= prime
    return power


def ternary_ones(n):
    out = 0
    while n:
        out += n % 3 == 1
        n //= 3
    return out


def check_two(n):
    power = prime_power_floor(n, 2)
    level = power.bit_length() - 1
    deficient = []
    total = Fraction(0)
    for k in range(n + 1):
        for ell in range(n + 1):
            cell = shell(n, k, ell) * compact_w5(n, k, ell)
            total += cell
            normalized_v = vp(cell, 2) + 2 + 5 * level
            assert normalized_v >= -2
            if normalized_v < 0:
                deficient.append((k, ell, normalized_v,
                                  unit_residue(2 ** (5 * level + 4) * cell, 2, 4)))
    assert deficient == [(power, 0, -2, 3), (power, power, -2, 1)]
    assert vp(2 ** (2 + 5 * level) * total, 2) >= 0


def check_three(n):
    power = prime_power_floor(n, 3)
    level = 0
    q = power
    while q > 1:
        q //= 3
        level += 1
    deficient = []
    total = Fraction(0)
    for k in range(n + 1):
        for ell in range(n + 1):
            cell = shell(n, k, ell) * compact_w5(n, k, ell)
            total += cell
            normalized_v = vp(cell, 3) + 1 + 5 * level
            assert normalized_v >= -1
            if normalized_v < 0:
                deficient.append((k, ell,
                                  unit_residue(3 ** (5 * level + 2) * cell, 3, 3)))
    leading, tail = divmod(n, power)
    expected_count = 0 if leading == 1 else 3 ** (1 + ternary_ones(tail))
    assert len(deficient) == expected_count
    assert all(residue == 2 for _, _, residue in deficient)
    assert vp(3 ** (1 + 5 * level) * total, 3) >= 0


def main(bound=80):
    for n in range(1, bound + 1):
        check_two(n)
        check_three(n)
    print(f"compact endpoint-residue law: every cell exact through n={bound}")
    print("p=2: two endpoint defects with residues (-1,+1) mod 4")
    print("p=3: 3^(1 + number of ternary 1-digits) defects, all -1 mod 3")


if __name__ == "__main__":
    main()
