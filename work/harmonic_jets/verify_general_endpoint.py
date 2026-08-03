#!/usr/bin/env python3
"""Exact certificate for the general endpoint-denominator classification.

The symbolic part proves the generating-function conjugation for an arbitrary
parameter b.  The rational part checks the recurrence, endpoint formula, sharp
denominator theorem for sample multiples of four, and the two necessity witnesses.
"""

from fractions import Fraction
from math import comb, lcm

import sympy as sp


def symbolic_certificate():
    # First certify the complete four-parameter conjugation displayed in the
    # endpoint-locus remark.
    z, alpha, beta, gamma, h = sp.symbols("z alpha beta gamma h")
    v = sp.Function("V")(z)
    w = z/(1 + h*z)

    def theta_w_general(expr):
        return sp.expand(z*(1 + h*z)*sp.diff(expr, z))

    def theta_z_general(expr):
        return sp.expand(z*sp.diff(expr, z))

    original_series = (1 + h*z)*v
    general_original = (
        theta_w_general(theta_w_general(original_series))
        - w*(alpha*theta_w_general(theta_w_general(original_series))
             + alpha*theta_w_general(original_series) + beta*original_series)
        + gamma*w*w*(
            theta_w_general(theta_w_general(original_series))
            + 2*theta_w_general(original_series) + original_series
        )
    )
    general_conjugate = (
        theta_z_general(theta_z_general(v))
        - z*((alpha - 3*h)
             *(theta_z_general(theta_z_general(v)) + theta_z_general(v))
             + (beta - h)*v)
        + z*z*(gamma - 2*alpha*h + 3*h*h)
        *(theta_z_general(theta_z_general(v)) + 2*theta_z_general(v) + v)
        + z**3*h*(gamma - alpha*h + h*h)
        *(theta_z_general(theta_z_general(v)) + 3*theta_z_general(v) + 2*v)
    )
    assert sp.simplify(general_original - general_conjugate) == 0

    # Specialize to the endpoint-decoupling locus.
    z, b = sp.symbols("z b")
    v = sp.Function("V")(z)
    w = z/(1 + b*z)

    def theta_w(expr):
        return sp.expand(z*(1 + b*z)*sp.diff(expr, z))

    def theta_z(expr):
        return sp.expand(z*sp.diff(expr, z))

    original_series = (1 + b*z)*v
    original = (
        theta_w(theta_w(original_series))
        - b*w*(3*theta_w(theta_w(original_series))
               + 3*theta_w(original_series) + original_series)
        + 2*b*b*w*w*(theta_w(theta_w(original_series))
                     + 2*theta_w(original_series) + original_series)
    )
    endpoint = (
        theta_z(theta_z(v))
        - b*b*z*z*(theta_z(theta_z(v)) + 2*theta_z(v) + v)
    )
    assert sp.simplify(original - endpoint) == 0


def companion(parameter, bound):
    values = [Fraction(0), Fraction(1)]
    b = parameter
    for n in range(1, bound):
        values.append(
            (b*(3*n*n + 3*n + 1)*values[n]
             - 2*b*b*n*n*values[n - 1])/(n + 1)**2
        )
    return values[:bound + 1]


def transform(values, parameter):
    b = parameter
    return [
        sum(
            (Fraction(comb(n, k))*(-b)**(n-k)*values[k]
             for k in range(n + 1)),
            Fraction(0),
        )
        for n in range(len(values))
    ]


def parity_quotient(n, j):
    value = Fraction(1)
    for numerator in range(j + 2, n, 2):
        value *= Fraction(numerator, numerator - 1)
    value /= n
    return value


def rational_certificate(bound=120):
    for b in (-20, -12, -8, -4, 0, 4, 8, 12, 20):
        values = companion(b, bound)
        endpoint = transform(values, b)
        running_lcm = 1
        for n in range(bound):
            previous = endpoint[n - 1] if n else Fraction(0)
            assert ((n + 1)**2*endpoint[n + 1]
                    - b*b*n*n*previous) == (-b)**n
            if n:
                running_lcm = lcm(running_lcm, n)
            assert (running_lcm**2*values[n]).denominator == 1
            if n:
                rhs = (-1)**(n - 1)*b**(n - 1)*sum(
                    (parity_quotient(n, j)**2
                     for j in range(n - 1, -1, -2)),
                    Fraction(0),
                )
                assert endpoint[n] == rhs

    b = sp.symbols("b")
    values = [sp.Integer(0), sp.Integer(1)]
    for n in range(1, 8):
        values.append(sp.cancel(
            (b*(3*n*n + 3*n + 1)*values[n]
             - 2*b*b*n*n*values[n - 1])/(n + 1)**2
        ))
    assert sp.cancel(values[4] - sp.Rational(2603, 576)*b**3) == 0
    assert sp.cancel(
        values[8] - sp.Rational(6802537507, 180633600)*b**7
    ) == 0


if __name__ == "__main__":
    symbolic_certificate()
    rational_certificate()
    print("general four-parameter binomial conjugation: exact")
    print("symbolic endpoint conjugation: exact for arbitrary b")
    print("endpoint recurrence and finite formula: verified through n=120")
    print("L_n^2 integrality: verified for sample b divisible by 4")
    print("necessity witnesses B_4 and B_8: exact symbolic identities")
