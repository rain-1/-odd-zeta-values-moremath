"""Growth constant of a given factorial-ratio single sum, and its full set of
characteristic roots (= the exp of the phase at every critical point).

shape = (z, [(a,b,e), ...])   ->   F(n,k) = z^k prod ((a n + b k)!)^e
"""
import numpy as np
from math import log, exp
import sympy as sp

t = sp.symbols('t', real=True)


def check_balance(sh):
    z, terms = sh
    return sum(e * a for a, b, e in terms), sum(e * b for a, b, e in terms)


def phase(sh):
    z, terms = sh
    f = sum(e * (a + b * t) * sp.log(a + b * t) for a, b, e in terms) + t * sp.log(z)
    return f


def crit_values(sh, tol=1e-9):
    """All critical points of f and the corresponding exp(f)."""
    z, terms = sh
    # f'(t) = sum e*b*(1+log(a+bt)) + log z = sum e*b*log(a+bt) + log z  (since sum e*b=0)
    # critical eq:  prod (a+bt)^{e*b} = 1/z
    num = sp.Integer(1)
    den = sp.Integer(1)
    for a, b, e in terms:
        p = e * b
        if p > 0:
            num *= (a + b * t) ** p
        elif p < 0:
            den *= (a + b * t) ** (-p)
    eq = sp.expand(sp.Integer(z) * num - den)
    poly = sp.Poly(eq, t)
    roots = np.roots([complex(c) for c in poly.all_coeffs()])
    out = []
    fl = sp.lambdify(t, phase(sh), 'numpy')
    for r in roots:
        try:
            v = complex(fl(complex(r)))
            out.append((complex(r), complex(np.exp(v))))
        except Exception:
            pass
    return poly.degree(), out


def growth(sh, tmax=6.0, N=200001):
    """max over the real support of exp(f(t))."""
    z, terms = sh
    ts = np.linspace(1e-9, tmax, N)
    L = {}
    val = np.zeros_like(ts)
    ok = np.ones_like(ts, dtype=bool)
    for a, b, e in terms:
        x = a + b * ts
        ok &= (x >= -1e-12)
        xx = np.where(x > 0, x, 1.0)
        val += e * xx * np.log(xx)
    val += ts * log(abs(z))
    val = np.where(ok, val, -np.inf)
    i = int(np.argmax(val))
    return exp(val[i]), ts[i]


APERY3 = (1, [(1, 1, 2), (0, 1, -4), (1, -1, -2)])
APERY2 = (1, [(1, 0, 1), (1, 1, 1), (0, 1, -3), (1, -1, -2)])

if __name__ == "__main__":
    import sys
    print("Apery zeta(3):", growth(APERY3), " expect 33.9705627 = (1+sqrt2)^4")
    d, cv = crit_values(APERY3)
    print("  crit poly degree", d, "values", [f"{abs(v):.6g}" for _, v in cv])
    print("Apery zeta(2):", growth(APERY2), " expect 11.09017 = phi^5")
    d, cv = crit_values(APERY2)
    print("  crit poly degree", d, "values", [f"{abs(v):.6g}" for _, v in cv])
    mu = max(np.roots([1, -6340, 67974, -6340, 1]).real)
    print("TARGET mu =", mu, " log =", log(mu))
    # some plausible high-weight shapes
    cands = {
        "sum C(n,k)^3 C(n+k,k)^3": (1, [(1, 1, 3), (0, 1, -6), (1, -1, -3)]),
        "sum C(n,k)^4 C(n+k,k)^4": (1, [(1, 1, 4), (0, 1, -8), (1, -1, -4)]),
        "sum C(n,k)^2 C(n+k,k)^4": (1, [(1, 1, 4), (0, 1, -6), (1, -1, -2), (1, 0, -2)]),
        "sum C(2n,k)^2C(n+k,k)^2 (?)": (1, [(2, 0, 2), (1, 1, 2), (0, 1, -4), (2, -1, -2), (1, 0, -2)]),
        "sum C(3n,k)C(n+k,k)^3": (1, [(3, 0, 1), (1, 1, 3), (0, 1, -4), (3, -1, -1), (1, 0, -3)]),
    }
    for name, sh in cands.items():
        print(f"{name}: balance={check_balance(sh)} growth={growth(sh)}")
