"""g_search.py -- empirical discovery of transfer identities in the parametrised
p-adic (Volkenborn) family.

DECISIVE TEST.  Two parameter points h, h' give *proportional* linear forms
    S(h)  = rho_0(h)  + rho_zeta(h)  * zeta_p(w)
    S(h') = rho_0(h') + rho_zeta(h') * zeta_p(w)
iff the 2x2 determinant
    rho_0(h) rho_zeta(h') - rho_0(h') rho_zeta(h)
vanishes EXACTLY.  That is the signature of a Rhin-Viola transfer identity
    S(h') = kappa(h,h') * S(h),  kappa in Q,
and it is checked in exact rational arithmetic -- no numerics, no guessing.

If proportionality holds we then report kappa and factor it, to see whether it
is a ratio of factorials (which is what the arithmetic method needs).
"""

import itertools
import sys
from fractions import Fraction as F
from collections import defaultdict

from g_forms import VWP


def factor_int(x):
    """Return dict p -> exponent for |x| (x a non-zero int), trial division."""
    x = abs(int(x))
    out = {}
    d = 2
    while d * d <= x:
        while x % d == 0:
            out[d] = out.get(d, 0) + 1
            x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def fact_str(fr):
    """Readable prime factorisation of a Fraction."""
    if fr == 0:
        return "0"
    n, d = abs(fr.numerator), fr.denominator
    fn, fd = factor_int(n) if n != 1 else {}, factor_int(d) if d != 1 else {}
    for p, e in fd.items():
        fn[p] = fn.get(p, 0) - e
    sgn = "-" if fr < 0 else ""
    parts = [f"{p}^{e}" if e != 1 else f"{p}" for p, e in sorted(fn.items())]
    return sgn + ("*".join(parts) if parts else "1")


def enum_points(h0, M=4, theta=F(1, 2), emax=None, fmax=None):
    """All admissible (e, f) up to permutation (sorted tuples)."""
    if emax is None:
        emax = h0 // 2
    if fmax is None:
        fmax = h0 // 2
    es = [t for t in itertools.combinations_with_replacement(range(emax + 1), M)]
    fs = [t for t in itertools.combinations_with_replacement(range(fmax + 1), M)]
    pts = []
    for e in es:
        if any(h0 - 2 * x < 0 for x in e):
            continue
        for f in fs:
            if any(h0 + 1 - 2 * x < 1 for x in f):
                continue
            v = VWP(h0, e, f, theta)
            if not v.admissible():
                continue
            pts.append((e, f))
    return pts


def data_for(h0, M=4, theta=F(1, 2), **kw):
    """Compute (rho_0, rho_zeta) exactly for every admissible point."""
    out = {}
    for (e, f) in enum_points(h0, M, theta, **kw):
        v = VWP(h0, e, f, theta)
        r = v.partial_fractions()
        rho = v.rho(r)
        out[(e, f)] = (v.rho0(r), rho[M - 1], v.deg)   # rho_zeta ~ rho_{M-1}
    return out


def proportional_pairs(data, verbose=True):
    """All pairs of points whose linear forms are exactly proportional."""
    keys = [k for k in data if data[k][1] != 0]
    hits = []
    for i in range(len(keys)):
        r0i, rzi, _ = data[keys[i]]
        for j in range(i + 1, len(keys)):
            r0j, rzj, _ = data[keys[j]]
            if r0i * rzj - r0j * rzi == 0:
                hits.append((keys[i], keys[j], rzj / rzi))
    return hits


def main():
    theta = F(1, 2)
    M = 4
    for h0 in (3, 4, 5, 6):
        data = data_for(h0, M, theta)
        print(f"\n=== h0={h0}, M={M}, theta={theta}: {len(data)} admissible points ===")
        # group by proportionality class
        hits = proportional_pairs(data)
        # build classes
        parent = {k: k for k in data}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b, _ in hits:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
        classes = defaultdict(list)
        for k in data:
            if data[k][1] != 0:
                classes[find(k)].append(k)
        nontriv = {k: v for k, v in classes.items() if len(v) > 1}
        print(f"  proportional pairs: {len(hits)};  non-singleton classes: {len(nontriv)}")
        shown = 0
        for root, mem in sorted(nontriv.items(), key=lambda kv: -len(kv[1])):
            if shown >= 6:
                break
            shown += 1
            base = mem[0]
            print(f"  class of size {len(mem)}:")
            for m in mem:
                kap = data[m][1] / data[base][1]
                print(f"     e={m[0]} f={m[1]} deg={data[m][2]}  kappa={fact_str(kap)}")


if __name__ == "__main__":
    main()
