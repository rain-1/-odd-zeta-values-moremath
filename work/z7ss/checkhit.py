"""Exact check of a candidate shape against all 74 q_n."""
import sys
from fractions import Fraction
from math import factorial
from qdata import Q


def evalshape(terms, z, n, kmax=None):
    """terms = [(a,b,e)], F(n,k) = z^k prod ((a n + b k)!)^e ; sum over k."""
    if kmax is None:
        kmax = 8 * n + 8
    tot = Fraction(0)
    for k in range(-kmax, kmax + 1):
        val = Fraction(1)
        zero = False
        for (a, b, e) in terms:
            L = a * n + b * k
            if L < 0:
                if e < 0:
                    zero = True
                    break
                raise ValueError("numerator factorial of negative argument at n=%d k=%d" % (n, k))
            f = factorial(L)
            val *= Fraction(f) ** e
        if zero:
            continue
        tot += val * Fraction(z) ** k if k >= 0 else val / Fraction(z) ** (-k)
    return tot


HIT = [(0, 1, -1), (0, 2, -1), (0, 4, -1), (2, 2, 1), (2, 4, -1),
       (4, -3, -2), (4, 1, 1), (4, 2, 1)]

if __name__ == "__main__":
    print("shape:", HIT, " sum e =", sum(e for _, _, e in HIT),
          " sum e*a =", sum(e * a for a, _, e in HIT),
          " sum e*b =", sum(e * b for _, b, e in HIT))
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    ok = True
    for n in range(NMAX + 1):
        v = evalshape(HIT, 1, n)
        good = (v == Q[n])
        ok &= good
        print("n=%2d  cand=%s  q_n=%s  %s" % (n, v, Q[n], "MATCH" if good else "*** MISMATCH ***"))
        if not good:
            break
    print("verdict:", "matches so far" if ok else "REFUTED")
