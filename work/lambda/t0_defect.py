"""T0 (probe): is the descent defect  D(n) := p^3 f(n) - f(floor(n/p))  structured?
Candidate structures: constant; function of r = n mod p only; f(r)-affine; ...
Exact rationals only."""
from fractions import Fraction as Fr
from core import apery_exact, vp, frac_mod, dstr

N = 200
A, B = apery_exact(N)
f = [Fr(B[n], A[n]) for n in range(N+1)]

for p in (5, 7, 11, 13):
    print("=" * 70)
    print("p =", p)
    # D(n) for n < p^2 : n = a*p + r
    print("  D(n) = p^3 f(n) - f(q),  v_p and value; rows a, cols r")
    rows = {}
    for n in range(p, min(N, p*p)+1):
        q = n // p
        D = Fr(p)**3 * f[n] - f[q]
        rows.setdefault(q, {})[n % p] = D
    for a in sorted(rows):
        vs = [vp(rows[a][r], p) for r in sorted(rows[a])]
        print("   a=%-3d v_p(D):" % a, vs)
    # test: does D(ap+r)/p^3 depend only on r?
    print("  --- test  D(a p + r) = p^3 * g(r) ?  (compare across a, mod p^4)")
    for r in range(p):
        vals = []
        for a in sorted(rows):
            if r in rows[a]:
                D = rows[a][r] / Fr(p)**3
                if vp(D, p) is not None and vp(D, p) >= 0:
                    vals.append(frac_mod(D, p, 3))
                else:
                    vals.append(None)
        print("     r=%-2d  D/p^3 mod p^3 across a=%s:" % (r, sorted(rows)[:6]), vals[:6],
              "ALL-EQUAL" if len(set(vals)) == 1 else "differ")
