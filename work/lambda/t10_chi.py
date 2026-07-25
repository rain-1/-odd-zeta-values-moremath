"""T4b: the chi-twist and the RATE LAW.

Claim (from the structure theorem):  the tower limit is
    Lambda_a = r * h^{chi,w}_p(a)  +  (blocks built from Kazandzidis limits c_p(a,b)),
so the convergence rate is
    rate = min( 3 , rate of the chi-twisted harmonic tower ),
the "3" being Kazandzidis' p^3 for C(ap^t,bp^t) and the second term being
    h^{chi,w}_p(a) = sum_{i>=0} (chi(p) p^{-w})^{-i} ... i.e. the tower of
    S^chi_i(a) = sum_{k<=a p^i, p!|k} chi(k) k^{-w}.
For trivial chi, S_i -> 0 fast (extra digits), so the rate is the Kazandzidis 3.
For nontrivial chi, S^chi_i tends to a NONZERO p-adic L-value, so the rate is exactly w.
Also: when chi(p) = -1 the tower must be normalised by chi(p)^{-s}, else it does not
converge at all.
"""
import sys
from fractions import Fraction as Fr
from pnum import P
from core import gen_mod, vp_fact
from t9_family import FAM, towers

def kron(D, n):
    """Kronecker symbol (D/n), D a fundamental discriminant, n any integer."""
    if n == 0:
        return 1 if D in (1, -1) else 0
    res = 1
    if n < 0:
        n = -n
        if D < 0: res = -res
    # factor out 2's: (D/2) = 0 if D even, 1 if D=+-1 mod 8, -1 if D=+-3 mod 8
    while n % 2 == 0:
        n //= 2
        if D % 2 == 0: return 0
        res *= 1 if D % 8 in (1, 7) else -1
    from sympy import jacobi_symbol
    return res * int(jacobi_symbol(D, n))

CHI = {"1": None, "chi-3": -3, "chi-4": -4, "chi5": 5}

def chi_val(name, n):
    D = CHI[name]
    if D is None: return 1
    return kron(D, n)

def rate_table(p, N=20000):
    print("p = %d   rate with the chi(p)^{-s} normalisation" % p)
    print("%-14s %-2s %-6s %-8s %s" % ("family", "w", "chi", "chi(p)", "rate (a=1) raw | twisted"))
    for (lab, kind, par, w, chi, lim) in FAM:
        cp = chi_val(chi, p)
        T = towers(p, N, kind, par, w, amax=1)
        rows = [r for r in T[1] if r is not None]
        raw = [rows[i].agree(rows[i-1]) - min(rows[i].v, rows[i-1].v) for i in range(1, len(rows))]
        tw = []
        for i in range(1, len(rows)):
            x = rows[i-1] * P.from_frac(p, cp**(i-1), 40)
            y = rows[i] * P.from_frac(p, cp**i, 40)
            tw.append(y.agree(x) - min(x.v, y.v))
        print("%-14s %-2d %-6s %-8d %s   |   %s" % (lab, w, chi, cp,
              ",".join(map(str, raw)), ",".join(map(str, tw))))

def harm_tower(p, w, chiname, a, smax, K):
    """S^chi_i and the tower h_s = sum_{i<=s} (chi(p)p^{-w})^{... } -- we simply form
       p^{ws} chi(p)^{-s} H^chi_w(a p^s) and measure its rate."""
    out = []
    tot = P.zero(p)
    cp = chi_val(chiname, p)
    for s in range(smax+1):
        n = a*p**s
        acc = Fr(0)
        for m in range(1, n+1):
            c = chi_val(chiname, m) if m % p or True else 0
            if c:
                acc += Fr(c, m**w)
        out.append(P.from_frac(p, acc * Fr(p**(w*s)) * Fr(cp**s), K))
    return out

if __name__ == "__main__":
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    rate_table(p)
    print("\n  chi-twisted harmonic towers  p^{ws}chi(p)^s H^chi_w(a p^s), a=1:")
    for (w, chin) in ((2, "1"), (3, "1"), (2, "chi-3"), (3, "chi-3"), (2, "chi-4"), (3, "chi5")):
        smax = 4 if p <= 7 else 3
        H = harm_tower(p, w, chin, 1, smax, 25)
        ag = [H[i].agree(H[i-1]) - min(H[i].v, H[i-1].v) for i in range(1, len(H))]
        print("     w=%d chi=%-6s chi(p)=%-3d  v=%-3d  rate: %s"
              % (w, chin, chi_val(chin, p), H[-1].v, ",".join(map(str, ag))))
