#!/usr/bin/env python3
"""Exact audit of the conjecturally sharp Catalan-companion denominator.

The harmonic formula proves 4*lcm(1,...,2*n)^2 * B_E(n) is integral.
Exact recurrence arithmetic suggests the substantially sharper statement
lcm(1,...,n)^2 * B_E(n) is integral.
"""

from fractions import Fraction
from math import lcm


def main(bound=500):
    second = [Fraction(0), Fraction(1)]
    running_lcm = 1
    for n in range(1, bound):
        coefficient = 12*n*n + 12*n + 4
        second.append((coefficient*second[n] - 32*n*n*second[n - 1])
                      / (n + 1)**2)

    for n, value in enumerate(second):
        if n:
            running_lcm = lcm(running_lcm, n)
        assert (running_lcm*running_lcm*value).denominator == 1, (n, value)

    print(f"L_n^2 * B_E(n) is integral for every 0 <= n <= {bound}")


if __name__ == "__main__":
    main()
