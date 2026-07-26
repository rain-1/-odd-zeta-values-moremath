"""Exact coefficient check of the Barnes decomposition against compact sums.

Finite verification only.  The final proof must establish the resulting
kernel identities for symbolic n.
"""

from __future__ import annotations

import sys
from fractions import Fraction as Q

import sympy as sp

sys.path.insert(0, "../lb5")

from core import Hs, T
import universal as univ


def sr(x):
    return sp.Rational(x.numerator, x.denominator)


def reduce_mzv(expr):
    poly = sp.Poly(sp.expand(expr), univ.z2, univ.z3, univ.z4,
                   univ.z5, univ.z23)
    out = 0
    for mon, c in poly.terms():
        e2, e3, e4, e5, e23 = mon
        if (e2, e3) == (2, 0):
            out += c * sp.Rational(5, 2) * univ.z4
        elif (e2, e3) == (1, 1):
            out += c * univ.z23
        else:
            out += (c * univ.z2**e2 * univ.z3**e3 * univ.z4**e4
                    * univ.z5**e5 * univ.z23**e23)
    return sp.expand(out)


def compact(n, k, l):
    A = lambda r, x: Hs(n + x, r) - Hs(x, r)
    B = lambda r, x: Hs(n - x, r) - Hs(x, r)
    alpha = A(1, k) - A(1, l)
    beta = B(1, k) - B(1, l)
    psi = alpha / 2 + beta
    c = (A(2, k) + A(2, l)) / 4 - alpha * psi / 2
    w3 = ((Hs(n + k, 3) + Hs(n + l, 3)) / 2
          - psi * (Hs(n + k, 2) - Hs(n + l, 2)) / 2)
    w5 = ((Hs(n + k, 5) + Hs(n + l, 5)) / 2
          + (alpha - beta) * (Hs(n + k, 4) - Hs(n + l, 4)) / 4
          + c * (Hs(n + k, 3) + Hs(n + l, 3)) / 2)
    return w3, w5


def local_difference(n, k, l):
    A = lambda r, x: Hs(n + x, r) - Hs(x, r)
    B = lambda r, x: Hs(n - x, r) - Hs(x, r)
    c1 = Hs(n + k + l, 1) - Hs(k + l, 1)
    c2 = Hs(n + k + l, 2) - Hs(k + l, 2)
    lk = -A(1, k) - c1 - 2 * B(1, k)
    ll = -A(1, l) - c1 - 2 * B(1, l)
    wb = (
        univ.universal(k, l, 2, 2)
        + sr(lk) * univ.universal(k, l, 1, 2)
        + sr(ll) * univ.universal(k, l, 2, 1)
        + sr(lk * ll - c2) * univ.universal(k, l, 1, 1)
    )
    w3, w5 = compact(n, k, l)
    expected = (2 * univ.z5 + 4 * univ.z23
                - 4 * sr(w3) * univ.z2 - 2 * sr(w5))
    return reduce_mzv(wb - expected)


def main(nmax):
    for n in range(nmax + 1):
        total = 0
        for k in range(n + 1):
            for l in range(n + 1):
                total += T(n, k, l) * local_difference(n, k, l)
        total = sp.expand(total)
        print("n=%d: %s" % (n, "PASS" if total == 0 else total), flush=True)
        if total != 0:
            raise SystemExit(1)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
