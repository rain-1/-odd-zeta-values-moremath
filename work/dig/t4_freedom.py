"""DIG-1  T4 : the freedom map and the margin function ready for DIG-3's optimiser.

margin(params; p, w) with params = (r, shift multiset, A, m, E, regime).

Two regimes, decided by the NON-VANISHING / purity bookkeeping (T1):

 (S) single-shift regime.  The form S_{theta0} is a form in 1 and the Hurwitz values
     zeta_p(u+1, theta0), u = i+m, i = 1..A.  It is a *two-term form in 1 and
     zeta_p(w)* only if
        (i)  every surviving Hurwitz weight is odd, and
        (ii) zeta_p(w, a/p^r) is a rational multiple of zeta_p(w),
     and (ii) holds iff phi(p^r) = 2, i.e. p^r in {3,4}  <=>  (p,r) in {(3,1),(2,2)},
     plus the exceptional p = 2, r = 1 point where Int dt/(t+1/2)^u is the FULL
     zeta_2 (LSZ Lemma 9), so that the even weights vanish for free.
     margin = A*(r + 1/(p-1))*log p - E          (all copies alignable)

 (T) twisted-sum regime.  One must sum S_{theta0} over all phi(p^r) shifts to
     (a) assemble zeta_p from the Hurwitz values and (b) kill the even weights.
     Then |S|_p is controlled by the WORST shift, and a numerator Pochhammer
     aligns with exactly one shift:
     margin = [A*r + min_theta0 sum_c contrib_c(theta0)]*log p - E
            <= A * p*log p/(p-1)^2 - E .
"""
import sys, os, math
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from family import Family, vp
from ledger import Config, vp_frac

BAR = "=" * 78


def phi(n):
    r, m = n, n
    p = 2
    while p * p <= m:
        if m % p == 0:
            r -= r // p
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        r -= r // m
    return r


# ---------------------------------------------------------------- alignment law
def margin_rate(p, r, shifts, A, theta0):
    """[A*r + sum_c contrib_c(theta0)]  in units of log p."""
    tot = Fr(A * r)
    for s in shifts:
        v = vp_frac(Fr(s) + Fr(theta0), p)
        tot += Fr(1, p - 1) if (v is None or v >= 0) else Fr(v)
    return tot


def best_distribution(p, r, A):
    """spread A copies over the phi(p^r) shift classes as evenly as possible;
       return (shifts, worst margin_rate)."""
    D = p ** r
    units = [j for j in range(1, D) if j % p != 0]
    shifts = []
    for i in range(A):
        j = units[i % len(units)]
        shifts.append(Fr((D - j) % D, D) if (D - j) % D else Fr(1, D))
    worst = min(margin_rate(p, r, shifts, A, Fr(j, D)) for j in units)
    return shifts, worst


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print(BAR)
    print("T4.1  the alignment law, verified numerically at p = 5 (two classes)")
    print(BAR)
    # 4 copies: two aligned to theta0=1/5 (shift 4/5), two to theta0=2/5 (shift 3/5)
    shifts = [Fr(4, 5)] * 2 + [Fr(3, 5)] * 2
    for t0 in (Fr(1, 5), Fr(2, 5)):
        pred = margin_rate(5, 1, shifts, 4, t0)
        vC = sum(max(0, -vp_frac(s, 5)) for s in shifts) + Fr(4, 4)
        alpha_pred = float(vC + pred)
        F = Family(p=5, theta0=t0, shifts=shifts, A=4, m=0, delta=0)
        rows = []
        for n in (6, 12, 18):
            S, rho0, Jc, rho = F.S_value(n, int(12 * (n + 3)) + 30)
            rows.append((n, vp(S, 5), vp(S, 5) / n))
        print("  theta0=%s  predicted alpha/log5 = v_5(C)+rate = %s+%s = %s ;  measured v_5(S_n)/n: %s"
              % (t0, vC, pred, alpha_pred, ["%d:%.2f" % (n, x) for n, _, x in rows]))
    print("  (both shifts give the same rate here by symmetry; the sum over shifts inherits the min)")

    print("\n  contrast: ALL four copies aligned to a single shift (Beukers-style, p=5)")
    shifts1 = [Fr(4, 5)] * 4
    for t0 in (Fr(1, 5), Fr(2, 5)):
        pred = margin_rate(5, 1, shifts1, 4, t0)
        vC = Fr(4) + Fr(4, 4)
        F = Family(p=5, theta0=t0, shifts=shifts1, A=4, m=0, delta=0)
        S, rho0, Jc, rho = F.S_value(12, 12 * 15 + 30)
        print("    theta0=%s : predicted alpha/log5 = %s ; measured v_5(S_12)/12 = %.2f"
              % (t0, float(vC + pred), vp(S, 5) / 12))
    print("  -> a form small at 1/5 is NOT small at 2/5: the twisted sum inherits the worse one.")

    print("\n" + BAR)
    print("T4.2  which (p, r) admit a TWO-TERM form in 1 and zeta_p(w)?  phi(p^r) = 2")
    print(BAR)
    print("   p    r   p^r  phi(p^r)  #reflection classes  two-term form possible?")
    for p in (2, 3, 5, 7, 11, 13):
        for r in (1, 2, 3):
            q = p ** r
            f = phi(q)
            ok = (f == 2)
            extra = ""
            if p == 2 and r == 1:
                extra = "  (LSZ Lemma 9: shift 1/2 IS the full zeta_2 -> even weights vanish)"
                ok = True
            print("  %3d  %3d  %4d  %6d  %14d       %s%s" %
                  (p, r, q, f, max(1, f // 2), "YES" if ok else "no", extra))

    print("\n" + BAR)
    print("T4.3  margin at the LSZ / Beukers anchors and the corrected deficits")
    print(BAR)
    L = lambda p: math.log(p)

    def single_shift_margin(p, r, A, E):
        return A * (r + 1.0 / (p - 1)) * L(p) - E

    rows = [
        ("zeta_2(3)  p=2 r=2 A=2 m=0 E=3   [known]", single_shift_margin(2, 2, 2, 3)),
        ("zeta_3(3)  p=3 r=1 A=2 m=0 E=3   [known]", single_shift_margin(3, 1, 2, 3)),
        ("zeta_2(5)  p=2 r=1 A=4 m=1 E=5   [known]", single_shift_margin(2, 1, 4, 5)),
        ("zeta_2(7)  p=2 r=1 A=6 m=1 E=7   [?]", single_shift_margin(2, 1, 6, 7)),
        ("zeta_2(7)  p=2 r=2 A=2 m=4 E=7   [?]", single_shift_margin(2, 2, 2, 7)),
        ("zeta_3(5)  p=3 r=1 A=2 m=2 E=5   [best single-shift]", single_shift_margin(3, 1, 2, 5)),
        ("zeta_3(5)  p=3 r=1 A=4 m=1 E=5   [needs twisted sum]", None),
    ]
    for name, m in rows:
        print("   %-46s margin = %s" % (name, "%+.4f" % m if m is not None else "see T4.4"))

    print("\n" + BAR)
    print("T4.4  the twisted-sum regime: margin for every p >= 3, all A, all r")
    print(BAR)
    print("   p     p*log p/(p-1)^2   sup_A [margin + E] / A     verdict")
    for p in (2, 3, 5, 7, 11, 13, 17, 19):
        c = p * L(p) / (p - 1) ** 2
        print("  %3d   %14.6f   %20.6f     %s" %
              (p, c, c, "margin can be > 0 (E ~ A)" if c > 1 else "margin < 0 for EVERY A, r, m"))
    print("\n   (E >= A always: E = A+m+1 minus a saving <= 1, m >= 0.  So in the twisted-sum")
    print("    regime  margin <= A*(p log p/(p-1)^2 - 1) - 1 < 0 for every p >= 3.)")

    print("\n   explicit optimum over (r, A) at fixed p, twisted-sum regime, weight 3 (E = A+1):")
    print("     p    r    A    worst rate    margin")
    for p in (5, 7, 11):
        best = None
        for r in (1, 2):
            for A in (2, 3, 4, 6, 8, 12, 20, 40):
                sh, w = best_distribution(p, r, A)
                mg = float(w) * L(p) - (A + 1)
                if best is None or mg > best[0]:
                    best = (mg, r, A, w)
        mg, r, A, w = best
        print("   %4d  %3d %4d   %10s   %+.4f" % (p, r, A, str(w), mg))

    print("\n" + BAR)
    print("T4.5  margin(params) for DIG-3: the exported function")
    print(BAR)
    print("""   margin(p, r, shifts, A, m, E, regime):
       regime 'S' (phi(p^r)=2 or (p,r)=(2,1)):  A*(r + 1/(p-1))*log p - E
       regime 'T' (otherwise):  [A*r + min_theta0 sum_c contrib_c]*log p - E
       E = A + m + 1 - saving,  saving in {0,1} (well-poised/Phi_n),
       weight w = A + m + 1 if that is odd, else A + m  (even zeta_p vanish, regime S at p=2
       and regime T always).""")
