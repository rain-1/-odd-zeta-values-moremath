#!/usr/bin/env python3
"""Exact audit of the endpoint transform proving the sharp denominator theorem.

For the normalized Catalan companion B, put

    T[n] = sum(binomial(n,k) * (-4)**(n-k) * B[k], k=0..n).

The paper proves that T satisfies a decoupled inhomogeneous recurrence and that
(-1)^(n-1) T[n] is a sum of explicit rational squares.  This script checks all
identities with exact integer/rational arithmetic and audits the termwise
denominator assertion behind L_n^2 B[n] in Z.
"""

from fractions import Fraction
from math import comb, lcm


def catalan_companion(bound):
    values = [Fraction(0), Fraction(1)]
    for n in range(1, bound):
        values.append(
            ((12*n*n + 12*n + 4)*values[n] - 32*n*n*values[n - 1])
            / (n + 1)**2
        )
    return values[:bound + 1]


def catalan_first_solution(bound):
    values = [1, 4]
    for n in range(1, bound):
        numerator = (12*n*n + 12*n + 4)*values[n] - 32*n*n*values[n - 1]
        assert numerator % (n + 1)**2 == 0
        values.append(numerator // (n + 1)**2)
    return values[:bound + 1]


def binomial_transform(values, c):
    return [
        sum(
            (Fraction(comb(n, k)) * (-c)**(n-k) * values[k]
             for k in range(n + 1)),
            Fraction(0),
        )
        for n in range(len(values))
    ]


def square_root_term(n, j):
    """R_{n,j}; admissible indices satisfy 0 <= j < n and n-j odd."""
    assert 0 <= j < n and (n - j) % 2 == 1
    value = Fraction(2**(n - 1), 1)
    for numerator in range(j + 2, n, 2):
        value *= Fraction(numerator, numerator - 1)
    # The loop includes denominators j+1,...,n-2.  Supply the final n.
    value /= n
    return value


def main(bound=300):
    first = catalan_first_solution(bound)
    companion = catalan_companion(bound)
    transformed = binomial_transform(companion, 4)

    # Audit the complete one-parameter transport recurrence.
    for c in range(9):
        for epsilon, source in ((0, first), (1, companion)):
            values = binomial_transform(source, c)
            for n in range(bound):
                u_nm1 = values[n - 1] if n >= 1 else Fraction(0)
                u_nm2 = values[n - 2] if n >= 2 else Fraction(0)
                residual = (
                    (n + 1)**2*values[n + 1]
                    - (4 - c)*(3*n*n + 3*n + 1)*values[n]
                    + (32 - 24*c + 3*c*c)*n*n*u_nm1
                    + c*(4 - c)*(8 - c)*n*(n - 1)*u_nm2
                )
                assert residual == epsilon*(-c)**n, (c, epsilon, n, residual)

    for n in range(bound):
        previous = transformed[n - 1] if n else Fraction(0)
        residual = (n + 1)**2*transformed[n + 1] - 16*n*n*previous
        assert residual == (-4)**n, (n, residual)

    running_lcm = 1
    for n in range(1, bound + 1):
        running_lcm = lcm(running_lcm, n)
        roots = [square_root_term(n, j) for j in range(n - 1, -1, -2)]
        square_sum = (-1)**(n - 1) * sum((r*r for r in roots), Fraction(0))
        assert square_sum == transformed[n], (n, square_sum, transformed[n])
        assert all((running_lcm*r).denominator == 1 for r in roots), n
        assert (running_lcm**2*transformed[n]).denominator == 1, n
        assert (running_lcm**2*companion[n]).denominator == 1, n

    print(f"endpoint recurrence and square formula verified through n={bound}")
    print(f"general c-transform recurrence verified for 0 <= c <= 8 through n={bound}")
    print(f"termwise L_n divisibility of every R_(n,j) verified through n={bound}")
    print(f"L_n^2 * B_E(n) is integral through n={bound}")


if __name__ == "__main__":
    main()
