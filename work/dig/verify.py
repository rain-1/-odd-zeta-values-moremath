"""DIG-1  T3 : exact-arithmetic verification that the ledger components are REAL.

Checks, all exact:
  A. LSZ anchor: regenerate their rho_{n,0}, rho_{n,3} from the partial fractions and
     match their printed values, recursion, Casoratian, integrality, purity.
  B. alpha  : measured v_p(S_n) vs the predicted alpha*n/log p.
  C. beta   : measured archimedean growth of the coefficients vs G = v_p(C) log p.
  D. E      : measured d_n-content of rho_0 vs the predicted E.
  E. the p=3 Beukers configuration re-derived in the Volkenborn language,
     including the J_2 <-> zeta_3(3) identification against the independent
     Kubota-Leopoldt implementation in work/padic_seam/padic.py.
"""
import sys, math, os
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "padic_seam"))
from family import Family, vp, dn

BAR = "-" * 74


def measure(fam, ns, prec_mult=None, label=""):
    """returns per-n: v_p(S_n), log max|rho|, d_n-exponent of rho_0."""
    rows = []
    for n in ns:
        r = fam.partial_fractions(n)
        prec = int((prec_mult or (fam.vpC() * 2 + 4)) * (n + 3)) + 30
        S, rho0, Jc, rho = fam.S_value(n, prec, r)
        vS = vp(S, fam.p)
        coeffs = [rho0] + [c for c in Jc.values()]
        mx = max(abs(float(c)) if abs(c) < Fr(10) ** 300 else float("inf") for c in coeffs)
        lg = (math.log(abs(float(mx))) if mx > 0 else 0.0)
        if mx == float("inf"):
            lg = float(len(str(max(abs(c.numerator) for c in coeffs))) * math.log(10))
        # d_n exponent needed to clear rho0
        den = rho0.denominator
        e = 0
        d = dn(n) if n > 0 else 1
        while den > 1 and e < 20:
            g = math.gcd(den, d)
            if g == 1:
                break
            den //= g
            e += 1
        rows.append((n, vS, lg, e, den == 1, rho0, Jc, rho))
    return rows


def hdr(t):
    print("\n" + "=" * 74 + "\n" + t + "\n" + "=" * 74)


# ---------------------------------------------------------------------------
hdr("A.  LSZ (arXiv:2505.05005) anchor -- exact regeneration")
# R_n = 2^{8n}(2t+n)(t+1/2)_n^4/(t)_{n+1}^4 ,  S_n = -Int R_n'(t+1/2) dt
lsz = Family(p=2, theta0=Fr(1, 2), shifts=[Fr(1, 2)] * 4, A=4, m=1, delta=1)
print("forced v_2(C) =", lsz.vpC(), " (LSZ use C = 2^8)")
ok = True
for n in (0, 1, 2, 3):
    r = lsz.partial_fractions(n)
    rho0, Jc, rho = lsz.form(n, r)
    # LSZ's S_n = -(our S).  Their rho_{n,3} = 384*sum_k r_{n,3,k}; rho_{n,0} = -(our rho0)
    rho_n3 = 384 * rho[3]
    rho_n0 = -rho0
    print("  n=%d : rho_{n,3} = %-12s rho_{n,0} = %-14s  sum_k r_{1,k} = %s" %
          (n, rho_n3, rho_n0, rho[1]))
    if n == 0:
        ok &= (rho_n3 == 768 and rho_n0 == 0)
    if n == 1:
        ok &= (rho_n3 == 73728 and rho_n0 == -1024)
    ok &= (rho[1] == 0)
print("  LSZ printed rho_{0,3}=768, rho_{1,3}=73728, rho_{0,0}=0, rho_{1,0}=-1024 :",
      "MATCH" if ok else "MISMATCH")
print("  purity  sum_k r_{n,1,k} = 0  (kills the zeta_2(3) term, deg R_n = -3):",
      "MATCH" if ok else "MISMATCH")

# recursion + Casoratian + integrality
seq = {}
for n in range(0, 13):
    r = lsz.partial_fractions(n)
    rho0, Jc, rho = lsz.form(n, r)
    seq[n] = (-rho0, 384 * rho[3])
recok = casok = intok = True
for n in range(1, 12):
    for i in (0, 1):
        lhs = ((n + 1) ** 5 * seq[n + 1][i]
               - 32 * (2 * n + 1) * (8 * n ** 4 + 16 * n ** 3 + 20 * n ** 2 + 12 * n + 3) * seq[n][i]
               + 2 ** 16 * n ** 5 * seq[n - 1][i])
        recok &= (lhs == 0)
for n in range(0, 12):
    cas = seq[n][0] * seq[n + 1][1] - seq[n + 1][0] * seq[n][1]
    casok &= (cas == Fr(3 * 2 ** (16 * n + 18), (n + 1) ** 5))
for n in range(1, 13):
    intok &= (seq[n][1].denominator == 1)
    intok &= ((Fr(dn(n)) ** 5 * seq[n][0]).denominator == 1)
print("  three-term recursion (eq:rec) for both rows, n=1..11 :", "MATCH" if recok else "MISMATCH")
print("  Casoratian = 3*2^{16n+18}/(n+1)^5 (LSZ Lemma 15b), n=0..11 :", "MATCH" if casok else "MISMATCH")
print("  rho_{n,3} in Z and d_n^5 rho_{n,0} in Z (their (den-con)), n<=12 :",
      "MATCH" if intok else "MISMATCH")

hdr("B/C/D.  measured alpha, growth and denominator cost")
print("%-26s %4s %8s %10s %9s %8s" % ("family", "n", "v_p(S_n)", "alpha_meas", "G_meas", "E_meas"))


def sweep(fam, label, ns, alpha_pred, G_pred, E_pred):
    rows = measure(fam, ns)
    for (n, vS, lg, e, cleared, rho0, Jc, rho) in rows:
        am = vS * math.log(fam.p) / n if n else 0
        gm = lg / n if n else 0
        print("%-26s %4d %8s %10.4f %9.4f %8d" % (label, n, vS, am, gm, e))
    n, vS, lg, e = rows[-1][0], rows[-1][1], rows[-1][2], rows[-1][3]
    print("   predicted: alpha = %.4f   G = %.4f   E = %d" % (alpha_pred, G_pred, E_pred))
    return rows


L2 = math.log(2)
L3 = math.log(3)
sweep(lsz, "LSZ zeta_2(5)", [8, 16, 24, 32], 16 * L2, 8 * L2, 5)

# Lai B_n family (arXiv:2304.00816 (3.2)):  2^{(3s+6)n}(t+3/4)_n^{s+2}/(t)_{n+1}^{s+2}
for s in (0, 1):
    B = Family(p=2, theta0=Fr(1, 4), shifts=[Fr(3, 4)] * (s + 2), A=s + 2, m=s, delta=0)
    sweep(B, "Lai B_n s=%d" % s, [8, 16, 24], (6 * s + 12) * L2, (3 * s + 6) * L2, 2 * s + 3)

# Lai A_n family:  2^{(6s+12)n}(4t+2n)^d (t+1/4)_n^{s+2}(t+3/4)_n^{s+2}/(t)_{n+1}^{2s+4}
for s in (0, 1):
    A = Family(p=2, theta0=Fr(1, 4), shifts=[Fr(1, 4)] * (s + 2) + [Fr(3, 4)] * (s + 2),
               A=2 * s + 4, m=s, delta=1)
    sweep(A, "Lai A_n s=%d" % s, [8, 16, 24], (10 * s + 20) * L2, (6 * s + 12) * L2, 2 * s + 3)

hdr("E.  the p=3 configuration in the Volkenborn language (Beukers' F=3 point)")
B3 = Family(p=3, theta0=Fr(1, 3), shifts=[Fr(2, 3)] * 2, A=2, m=0, delta=0)
print("forced v_3(C) =", B3.vpC(), "-> C = 3^3 = 27 ; predicted alpha = 6 log 3, G = 3 log 3, E = 3")
sweep(B3, "Beukers zeta_3(3)", [8, 16, 24, 32], 6 * L3, 3 * L3, 3)

# reflection + Kubota-Leopoldt cross-check
print("\n  reflection  zeta_3(3,1/3) = zeta_3(3,2/3)  <=>  J_2(1/3) = J_2(2/3):")
J13 = B3.J(2, 40)
B3b = Family(p=3, theta0=Fr(2, 3), shifts=[Fr(1, 3)] * 2, A=2, m=0, delta=0)
J23 = B3b.J(2, 40)
d = J13 - J23
print("    v_3(J_2(1/3) - J_2(2/3)) =", vp(d, 3), " (>= 40 means equal to the cutoff)")
try:
    import padic as KL
    prec = 30
    z3 = KL.zeta_p(3, 3, prec)                       # zeta_3(3) mod 3^prec, validated 980/980
    lhs = KL.frac_mod(J13, 3, prec)
    rhs = (27 * z3) % 3 ** prec
    print("    J_2(1/3) =? 27*zeta_3(3)  (Lemma 12 with D=3, i=3):",
          "MATCH" if lhs == rhs else "MISMATCH (%s vs %s)" % (lhs, rhs))
    # LSZ Lemma 9 at p=2: Int dt/(t+1/2)^{s-1} = (s-1) 2^s zeta_2(s)
    z25 = KL.zeta_p(5, 2, prec)
    J4 = lsz.J(4, prec + 10)
    print("    LSZ Lemma 9   J_4(1/2) =? 4*2^5*zeta_2(5):",
          "MATCH" if KL.frac_mod(J4, 2, prec) == (128 * z25) % 2 ** prec else "MISMATCH")
except Exception as ex:                                    # pragma: no cover
    print("    [KL cross-check skipped:", ex, "]")
