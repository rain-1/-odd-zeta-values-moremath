"""Project the Barnes zeta(2)-coefficient to the bare weight-3 alphabet.

This identifies the contour-native symmetric representative as a closed
harmonic expression, independently of the sequence-level fitting used in
work/z5rep/.
"""

from __future__ import annotations

import sys
from fractions import Fraction as Q
from functools import lru_cache

import sympy as sp

sys.path.insert(0, "../z5rep")
sys.path.insert(0, "../lb5")

import bare
from core import Hs
import universal as univ


def rat(x) -> Q:
    x = sp.Rational(x)
    return Q(int(x.p), int(x.q))


def reduced_coeff(expr, target):
    """Coefficient after z2^2=(5/2)z4 and z2*z3=z23."""
    poly = sp.Poly(sp.expand(expr), univ.z2, univ.z3, univ.z4,
                   univ.z5, univ.z23)
    out = 0
    for mon, c in poly.terms():
        e2, e3, e4, e5, e23 = mon
        if (e2, e3) == (2, 0):
            term = c * sp.Rational(5, 2) * univ.z4
        elif (e2, e3) == (1, 1):
            term = c * univ.z23
        else:
            term = (c * univ.z2**e2 * univ.z3**e3 * univ.z4**e4
                    * univ.z5**e5 * univ.z23**e23)
        out += term
    return rat(sp.expand(out).coeff(target))


@lru_cache(None)
def icoeff(k, l, p, q, target_name):
    target = {"z2": univ.z2, "one": 1}[target_name]
    e = univ.universal(k, l, p, q)
    if target_name == "one":
        return rat(sp.expand(e).subs({
            univ.z2: 0, univ.z3: 0, univ.z4: 0,
            univ.z5: 0, univ.z23: 0}))
    return reduced_coeff(e, target)


def barnes_w3(n, k, l):
    A = lambda r, x: Hs(n + x, r) - Hs(x, r)
    B = lambda r, x: Hs(n - x, r) - Hs(x, r)
    C1 = Hs(n + k + l, 1) - Hs(k + l, 1)
    C2 = Hs(n + k + l, 2) - Hs(k + l, 2)
    Lk = -A(1, k) - C1 - 2 * B(1, k)
    Ll = -A(1, l) - C1 - 2 * B(1, l)
    z2c = (
        icoeff(k, l, 2, 2, "z2")
        + Lk * icoeff(k, l, 1, 2, "z2")
        + Ll * icoeff(k, l, 2, 1, "z2")
        + (Lk * Ll - C2) * icoeff(k, l, 1, 1, "z2")
    )
    return -z2c / 4


def mon_value(mon, n, k, l):
    out = Q(1)
    for name in mon:
        r, arg = bare.LETTERS[name]
        cn, ck, cl = bare.ARGS[arg]
        out *= Hs(cn * n + ck * k + cl * l, r)
    return out


def main(nmax=7):
    _, tops = bare.span_w3(maxdeg=2)
    basis = sorted(tops)
    triples = [(n, k, l) for n in range(nmax + 1)
               for k in range(n + 1) for l in range(n + 1)]
    rows = [[mon_value(m, n, k, l) for m in basis] for n, k, l in triples]
    rhs = [barnes_w3(n, k, l) for n, k, l in triples]
    A = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row]
                   for row in rows])
    b = sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in rhs])
    try:
        sol, params = A.gauss_jordan_solve(b)
    except ValueError:
        print("cells", len(triples), "basis", len(basis))
        print("INCONSISTENT: the local Barnes zeta(2) coefficient is not in",
              "the degree-<=2 bare weight-3 span")
        return
    print("cells", len(triples), "basis", len(basis), "rank", A.rank(),
          "parameters", params.rows)
    # Canonicalise free parameters to zero.
    zeroed = sol.subs({x: 0 for x in params})
    el = {m: Q(int(c.p), int(c.q)) for m, c in zip(basis, zeroed) if c != 0}
    print("support", len(el))
    for mon, c in sorted(el.items()):
        print(c, "*", "*".join(mon))
    bad = []
    for n in range(nmax + 1, nmax + 4):
        for k in range(n + 1):
            for l in range(n + 1):
                got = sum((c * mon_value(m, n, k, l) for m, c in el), Q(0))
                want = barnes_w3(n, k, l)
                if got != want:
                    bad.append((n, k, l, got - want))
    print("held-out:", "PASS" if not bad else bad[:3])


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
