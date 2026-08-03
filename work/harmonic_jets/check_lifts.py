#!/usr/bin/env python3
"""Exact checks for the harmonic-jet lifts used in the paper."""

from fractions import Fraction
from math import comb, factorial


def H(m, r=1):
    return sum((Fraction(1, j**r) for j in range(1, m + 1)), Fraction())


def chi4(j):
    if j % 2 == 0:
        return 0
    return 1 if j % 4 == 1 else -1


def K4(m, r=1):
    return sum((Fraction(chi4(j), j**r) for j in range(1, m + 1)), Fraction())


def shell(n, k):
    return comb(n, k) * comb(2 * k, k) * comb(2 * (n - k), n - k)


def weight(n, k):
    return (Fraction(1, 2) * K4(2 * k, 2)
            + (Fraction(3, 4) * H(k) - Fraction(1, 2) * H(2 * k))
            * (K4(2 * k) - K4(2 * n - 2 * k)))


def companion(n):
    return sum((shell(n, k) * weight(n, k) for k in range(n + 1)), Fraction())


def apery_recurrence(values):
    for n in range(1, len(values) - 1):
        lhs = (n + 1) ** 2 * values[n + 1]
        rhs = (12 * n * n + 12 * n + 4) * values[n] - 32 * n * n * values[n - 1]
        assert lhs == rhs, (n, lhs, rhs)


def main():
    vals = [companion(n) for n in range(31)]
    assert vals[:4] == [0, 1, 7, Fraction(404, 9)]
    apery_recurrence(vals)

    # If log F has u-derivative A, v-derivative D and mixed derivative C,
    # then F_uv/F = A*D+C.  These are the three derivatives of the compact
    # Catalan lift in Theorem 5.1.
    for n in range(20):
        for k in range(n + 1):
            a = Fraction(3, 4) * H(k) - Fraction(1, 2) * H(2 * k)
            d = K4(2 * k) - K4(2 * n - 2 * k)
            c = Fraction(1, 2) * K4(2 * k, 2)
            assert a * d + c == weight(n, k)

    print("Catalan lift: exact mixed-derivative identity checked for n <= 19")
    print("Catalan companion: exact recurrence checked for 1 <= n <= 29")
    print("initial values:", ", ".join(str(x) for x in vals[:8]))


if __name__ == "__main__":
    main()
