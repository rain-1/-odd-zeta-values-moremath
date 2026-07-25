"""DIG-1  T2/T4 : the 'free factorial' parameter direction, and the Lai-Lupu-Sprang
(arXiv:2505.23088) p >= 5 theorem as a sixth validation of the ledger.

A numerator factor n!^S (instead of a Pochhammer) is a copy with
    fractional depth l' = 0,      p-adic contribution +1/(p-1)   (v_p(n!) = n/(p-1)),
    archimedean cost  + log 2 per copy   (the binomial saddle max_k binom(n,k) = 2^n),
and it raises the pole order A by one (hence E by one).  Net per copy:
    d(margin) = [ 1/(p-1) + r ] log p - log 2 - 1.

LLS's own object (their Definition 3.1):
    R_n(t) = p^{pn} n!^s t^{M_0} prod_{j=1}^{p-1}(t+j/p)_n / (t)_{n+1}^{p-1+s}
i.e. p-1 Pochhammer copies at the p-1 shifts j/p (r = 1), s free factorials,
pole order A = p-1+s, primitive (m = -1, so E = A), summed over all p-1 cosets.
The ledger then gives

    margin(s) = (s+1) * p log p/(p-1) - s(1 + log 2) - p + 1 ,

so a positive margin needs
    s > [ p - 1 - p log p/(p-1) ] / [ p log p/(p-1) - 1 - log 2 ],
whose DENOMINATOR is exactly LLS's  (p/(p-1)) log p - 1 - log 2 .
"""
import math

print("=" * 78)
print("free-factorial direction: d(margin)/d(one n! copy) = [1/(p-1)+r] log p - log2 - 1")
print("=" * 78)
print("   p     r=1      r=2      (positive => extra factorials buy margin)")
for p in (2, 3, 5, 7, 11, 13):
    row = []
    for r in (1, 2):
        row.append((1.0 / (p - 1) + r) * math.log(p) - math.log(2) - 1)
    print("  %3d  %+7.4f  %+7.4f" % (p, row[0], row[1]))

print("\n" + "=" * 78)
print("LLS (arXiv:2505.23088) Theorem 1.1 reproduced from the ledger")
print("=" * 78)
print("   p    ledger margin(s) > 0 needs s >    top weight A+1 = p+s     LLS c_p (their Cor 1.2)")
for p in (5, 7, 11, 13, 17, 19):
    num = p - 1 - p * math.log(p) / (p - 1)
    den = p * math.log(p) / (p - 1) - 1 - math.log(2)
    s0 = num / den
    lls = p + p / math.log(p) + 5
    print("  %3d   %22.4f   %18.1f     %10.1f" % (p, s0, p + max(0.0, s0), lls))
print("""
   The DENOMINATOR  p log p/(p-1) - 1 - log 2  is LLS's exactly; the numerator differs
   only because they replace the crude binomial saddle log 2 by the exact constant
   varpi_p = psi(1/p) + 2p - 1 + gamma + p(log p - sum_{j<=p} 1/j).  Structure, the
   p/(p-1) coset factor and the 1 + log 2 Ball-Rivoal cost all come out of the ledger.
""")

print("=" * 78)
print("consequence: rank is what binds, not size")
print("=" * 78)
print("""   Each free factorial adds ~ +0.3 to +0.9 of margin at p >= 5 but also raises the
   pole order, hence the number of surviving odd weights: rank ~ A/2.  A positive
   margin at p >= 5 therefore always comes with rank >= 2, i.e. a 'one of
   zeta_p(3),...,zeta_p(c_p)' statement -- never an individual value, never a measure.
   At rank 1 (the only configuration that yields an irrationality measure) the best
   possible margin at p >= 5 is exactly -E (see optimize.py): the p-adic smallness
   cancels the archimedean growth to the last digit and the whole d_n^E denominator
   cost goes unpaid.""")
