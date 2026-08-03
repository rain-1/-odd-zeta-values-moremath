#!/usr/bin/env python3
"""Exact partial-fraction audit for the Brown--Zudilin zeta(5) companion.

The script works only with fractions.  It reconstructs the pole coefficients of
Zudilin's two rational functions, purifies the zeta(3) coefficient, and checks
the reflection and vanishing-moment identities of the resulting rational
function.  It also checks the experimentally stronger 2- and 3-adic congruence
which implies the low-prime part of the sharp-12 denominator theorem.
"""

from fractions import Fraction
from math import comb, factorial


def mul(a, b, trunc=6):
    out = [Fraction(0) for _ in range(min(trunc, len(a) + len(b) - 1))]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j < trunc:
                out[i + j] += x * y
    return out


def linear_power(a, exponent, trunc=6):
    """Taylor series of (a+x)^exponent, where a is nonzero."""
    if exponent >= 0:
        out = [Fraction(0) for _ in range(min(trunc, exponent + 1))]
        for m in range(len(out)):
            out[m] = Fraction(comb(exponent, m) * a ** (exponent - m))
        return out
    # binom(-r,m)=(-1)^m binom(r+m-1,m)
    r = -exponent
    return [Fraction((-1) ** m * comb(r + m - 1, m), a ** (r + m))
            for m in range(trunc)]


def pole_coefficients(n):
    """Return A[s][j] in R_n(k)=sum A[s][j]/(k+j)^s."""
    fact = factorial(n) ** 4
    A = [[Fraction(0) for _ in range(n + 1)] for _ in range(7)]
    for j in range(n + 1):
        series = [Fraction(fact)]
        # k+n/2 at k=-j+x
        series = mul(series, [Fraction(n, 2) - j, Fraction(1)])
        for r in range(1, n + 1):
            series = mul(series, linear_power(-j - r, 1))
        for r in range(1, n + 1):
            series = mul(series, linear_power(n + r - j, 1))
        for r in range(n + 1):
            if r != j:
                series = mul(series, linear_power(r - j, -6))
        for m, value in enumerate(series):
            A[6 - m][j] = value
    return A


def purified_coefficients(n):
    """Return A, tilde-A, and C for S=tilde(w)R-w tilde(R)."""
    A = pole_coefficients(n)
    At = [[Fraction(0) for _ in range(n + 1)] for _ in range(7)]
    # tilde R(k)=-k(k+n)R(k), expanded at k=-j.
    for s in range(1, 7):
        for j in range(n + 1):
            At[s][j] = (j * (n - j) * A[s][j]
                        + (2 * j - n) * (A[s + 1][j] if s < 6 else 0)
                        - (A[s + 2][j] if s < 5 else 0))
    w = sum(A[3])
    wt = sum(At[3])
    C = [[Fraction(0) for _ in range(n + 1)] for _ in range(7)]
    for s in range(1, 7):
        for j in range(n + 1):
            C[s][j] = wt * A[s][j] - w * At[s][j]
    return A, At, C


def harmonic(j, s):
    return sum((Fraction(1, k ** s) for k in range(1, j + 1)), Fraction(0))


def qp(n):
    _, _, C = purified_coefficients(n)
    q = sum(C[5])
    p = sum(C[s][j] * harmonic(j, s)
            for s in range(1, 7) for j in range(n + 1))
    return q, p, C


def vp_int(x, prime):
    if x == 0:
        return 10 ** 9
    x = abs(x)
    out = 0
    while x % prime == 0:
        out += 1
        x //= prime
    return out


def vp(x, prime):
    return vp_int(x.numerator, prime) - vp_int(x.denominator, prime)


def floor_log(n, prime):
    out = 0
    while n >= prime:
        n //= prime
        out += 1
    return out


def check_structure(n):
    q, _, C = qp(n)
    # Oddness S(-n-k)=-S(k).
    for s in range(1, 7):
        for j in range(n + 1):
            assert C[s][n - j] == (-1) ** (s + 1) * C[s][j]
    # Purity: only the zeta(5) coefficient survives.
    for s in range(1, 7):
        assert sum(C[s]) == (q if s == 5 else 0)
    # S(k)=O(k^(-4n-3)).  The coefficient of k^(-r) vanishes below that order.
    for r in range(1, 4 * n + 3):
        moment = sum(C[s][j] * (-1) ** (r - s) * comb(r - 1, r - s)
                     * j ** (r - s)
                     for s in range(1, min(6, r) + 1)
                     for j in range(n + 1))
        assert moment == 0


def check_low_prime_congruence(n):
    q, p, _ = qp(n)
    central = comb(2 * n, n)
    # Q=(-1)^(n+1)q/C and P=(-1)^(n+1)p/C, so signs cancel.
    for prime, a in ((2, 2), (3, 1)):
        exponent = a + 5 * floor_log(n, prime)
        assert vp(prime ** exponent * p + q, prime) >= a + vp_int(central, prime)


def main(bound=20):
    for n in range(bound + 1):
        check_structure(n)
        if n:
            check_low_prime_congruence(n)
    print(f"reflection, purity, and all forced moments: exact through n={bound}")
    print(f"strong low-prime congruence: exact through n={bound}")


if __name__ == "__main__":
    main()
