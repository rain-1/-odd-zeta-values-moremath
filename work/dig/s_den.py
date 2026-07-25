"""DIG-3  s_den.py -- the TRUE denominator cost E, measured prime by prime.

DIG-1's ledger uses  E = A + m + 1 - delta,  [VERIFIED] against LSZ (m=1),
Beukers (m=0), Lai B_n (m=0,1) and Lai A_n (m=0,1).  Every anchor has m <= 1.

Here E is measured for m >= 2 as well, by factoring the exact denominator of
rho_0 (after the forced normalisation C^n = p^{v_p(C) n} is applied) and reading
off the exponent as a function of ell/n.  The result:

    ell <= n            exponent = A + m + 1 - delta      (the ledger, confirmed)
    n < ell < 2n        exponent = c(m)  --  ZERO for m <= 1, POSITIVE for m >= 3

so the true cost is  E_true = (A+m+1-delta) + c(m),  because
log lcm{ell : n < ell < 2n} / n -> 1.  The extra block comes from the
half-integer sums T_{k,u} = sum_{nu<k} (nu+theta)^{-u}, whose denominators run
over the ODD numbers up to 2n; for m <= 1 they cancel, for m >= 3 they do not.
"""
import sys, os, math
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from family import Family, dn, vp
import sympy

LOG = math.log


def true_E(p, r, shifts, A, m, delta, n, verbose=False):
    """(E_low, E_high, rate) : exponents on primes <= n and in (n, 2n), and the
    measured rate log(denom)/n after removing the p-part (paid by C^n)."""
    fam = Family(p=p, theta0=F(1, p ** r), shifts=shifts, A=A, m=m, delta=delta)
    rr = fam.partial_fractions(n)
    rho0, Jc, rho = fam.form(n, rr)
    if rho0 == 0:
        return None
    vC = fam.vpC()
    y = rho0 * F(p) ** int(math.ceil(float(vC) * n))
    D = y.denominator
    while D % p == 0:
        D //= p
    if D == 1:
        return (0, 0, 0.0, {})
    fac = sympy.factorint(D)
    low = [e for l, e in fac.items() if l <= n]
    high = [e for l, e in fac.items() if n < l < 2 * n]
    top = [(l, e) for l, e in fac.items() if l >= 2 * n]
    rate = sum(e * LOG(l) for l, e in fac.items()) / n
    # the modal exponent in each band (the plateau)
    def mode(xs):
        if not xs:
            return 0
        return max(set(xs), key=xs.count)
    return (mode(low), mode(high), rate, dict(top=top, nlow=len(low),
                                              nhigh=len(high)))


if __name__ == "__main__":
    print("=" * 78)
    print("s_den : the TRUE denominator exponent, per prime band.")
    print("        ledger E = A+m+1-delta ;  E_true = E_ledger + c, c = the")
    print("        exponent on the primes in (n, 2n)  (each worth 1 per n).")
    print("=" * 78)
    N = 48
    cases = [
        # (label, p, r, shifts, A, m, delta, is-a-published-anchor)
        ("Beukers R^(B)  zeta_2(3)", 2, 1, [F(1, 2)] * 3, 3, 0, 1, True),
        ("Beukers F=4    zeta_2(3)", 2, 2, [F(3, 4)] * 2, 2, 0, 0, True),
        ("LSZ 2025       zeta_2(5)", 2, 1, [F(1, 2)] * 4, 4, 1, 1, True),
        ("Beukers F=3    zeta_3(3)", 3, 1, [F(2, 3)] * 2, 2, 0, 0, True),
        ("Lai B_n s=1    (m=1)", 2, 2, [F(3, 4)] * 3, 3, 1, 0, True),
        ("Lai B_n s=2    (m=2)", 2, 2, [F(3, 4)] * 4, 4, 2, 0, False),
        ("Lai B_n s=3    (m=3)", 2, 2, [F(3, 4)] * 5, 5, 3, 0, False),
        ("--- the map's rank-1 optima with m >= 2 ---", None, 0, [], 0, 0, 0, False),
        ("zeta_2(7)  r=1 A=4 m=3 d=1", 2, 1, [F(1, 2)] * 4, 4, 3, 1, False),
        ("zeta_2(7)  r=1 A=3 m=4 d=1", 2, 1, [F(1, 2)] * 3, 3, 4, 1, False),
        ("zeta_2(7)  r=2 A=2 m=4 d=0", 2, 2, [F(3, 4)] * 2, 2, 4, 0, False),
        ("zeta_2(9)  r=1 A=4 m=5 d=1", 2, 1, [F(1, 2)] * 4, 4, 5, 1, False),
        ("zeta_3(5)  r=1 A=2 m=2 d=0", 3, 1, [F(2, 3)] * 2, 2, 2, 0, False),
        ("zeta_3(7)  r=1 A=2 m=4 d=0", 3, 1, [F(2, 3)] * 2, 2, 4, 0, False),
        ("zeta_5(3)  r=1 A=2 m=0 d=0", 5, 1, [F(4, 5)] * 2, 2, 0, 0, False),
        ("zeta_5(5)  r=1 A=4 m=1 d=1", 5, 1, [F(4, 5)] * 4, 4, 1, 1, False),
    ]
    print("\n  config                        E_led  exp(l<=n)  exp(n<l<2n)  E_true  "
          "rate  ledger-margin  TRUE margin")
    for (lab, p, r, sh, A, m, d, anch) in cases:
        if p is None:
            print("\n  %s" % lab)
            continue
        res = true_E(p, r, sh, A, m, d, N)
        Eled = A + m + 1 - d
        if res is None:
            print("  %-28s  %3d   rho_0 == 0 (degenerate)" % (lab, Eled))
            continue
        lo, hi, rate, extra = res
        Etrue = lo + hi
        fam = Family(p=p, theta0=F(1, p ** r), shifts=sh, A=A, m=m, delta=d)
        vC = float(fam.vpC())
        G = vC * LOG(p)
        # alpha - G at the aligned single-coset point:
        gain = (A * r + len(sh) * 1.0 / (p - 1)) * LOG(p)
        print("  %-28s  %3d      %3d         %3d        %3d   %5.2f    %+8.4f     %+8.4f%s"
              % (lab, Eled, lo, hi, Etrue, rate, gain - Eled, gain - Etrue,
                 "   [ANCHOR]" if anch else ""))
