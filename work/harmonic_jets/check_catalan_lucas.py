#!/usr/bin/env python3
"""Exact audit of the full-digit Catalan companion congruence.

The paper proves the half-digit range termwise and all digits at unit-digit
primes by a Casoratian argument.  At primes with a zero first-solution digit,
this script supplies exact evidence for the remaining zero--pole cancellation.
"""

from fractions import Fraction


def primes_through(bound):
    for n in range(2, bound + 1):
        if all(n % d for d in range(2, int(n**0.5) + 1)):
            yield n


def sequences(count):
    first = [1, 4]
    second = [Fraction(0), Fraction(1)]
    for n in range(1, count - 1):
        coefficient = 12*n*n + 12*n + 4
        first.append((coefficient*first[n] - 32*n*n*first[n - 1]) // (n + 1)**2)
        second.append((coefficient*second[n] - 32*n*n*second[n - 1]) / (n + 1)**2)
    return first, second


def integer_valuation(value, prime):
    if value == 0:
        return 10**9
    value = abs(value)
    answer = 0
    while value % prime == 0:
        answer += 1
        value //= prime
    return answer


def valuation(value, prime):
    return (integer_valuation(value.numerator, prime)
            - integer_valuation(value.denominator, prime))


def main():
    for prime in primes_through(31):
        if prime == 2:
            continue
        first, second = sequences(prime*prime + 1)
        character = 1 if prime % 4 == 1 else -1
        zero_digits = [j for j in range(prime) if first[j] % prime == 0]
        for a in range(prime):
            for r in range(prime):
                difference = (prime**2*second[a*prime + r]
                              - character*second[a]*first[r])
                assert valuation(difference, prime) >= 1, (prime, a, r, difference)
        status = "unit-digit theorem applies" if not zero_digits else f"zero digits {zero_digits}"
        print(f"p={prime}: all {prime**2} digit pairs pass; {status}")
    print("full-digit congruence audited exactly for every odd prime p <= 31")


if __name__ == "__main__":
    main()
