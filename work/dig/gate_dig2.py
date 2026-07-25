"""DIG-1 x DIG-2 : THE GATE.

DIG-2 asks for one number: (alpha_p - growth) at alpha=(25,26,27,28), beta=(1,8,48,49),
p = 5, weight 3, to be compared with budget - delta = 48.459296.

LEDGER EXTENDED TO UNEQUAL BRICK LENGTHS  [DERIVED here; the equal-length case is
verified exactly in verify.py].  In Zudilin's normalised-brick gauge (llm/04 (2.4)-(2.5))

    R(t) = prod_{j=1,2} (t+b_j)_{lam_j n}/(lam_j n)!   *   prod_{j=3,4} (nu_j n-1)!/(t+a_j)_{nu_j n}
    lam_j = alpha_j - beta_j  (numerator bricks),   nu_j = beta_j - alpha_j  (pole bricks)

and with a p-adic integration shift theta0 of depth r:

    numerator brick, aligned    (sigma + theta0 in Z_p) :  + lam/(p-1) - lam/(p-1) = 0
    numerator brick, misaligned                        :  - (r + 1/(p-1)) lam
    pole brick                                         :  + (r + 1/(p-1)) nu

    ==>  alpha_p - growth = (r + 1/(p-1)) log p * [ sum nu - sum_{mis} lam ]  -  C_1

The last term is the crux: Bel's p-adic criterion (llm/18 Lemma 4) requires
alpha > beta = growth + denominators, so the ARCHIMEDEAN COEFFICIENT GROWTH C_1 is
subtracted.  The archimedean Rhin-Viola criterion only requires C_0 > C_2 and never
pays C_1 (it only enters the measure).  At the totally symmetric p-adic points C_1 = 0
  -- Beukers Prop 11.1(3): |q_n|,|p_n| < e^{eps n};  LSZ Lemma 20: max|rho| <= 2^{8n+o(n)}
  (Poincare, double root) --
and DIG-2 proved delta = 0 there.  So delta > 0 and C_1 = 0 have disjoint support.
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from g_cal import taus, f0
from g_group import m_params, delta_limit

L = math.log


def bricks(alpha, beta):
    lam, nu = [], []
    for a, b in zip(alpha, beta):
        (lam if a >= b else nu).append(abs(a - b))
    return lam, nu


def padic_rate(alpha, beta, p, r, aligned_mask):
    """(alpha_p - growth) without the C_1 term, in absolute units (per n)."""
    lam, nu = bricks(alpha, beta)
    mis = sum(l for l, k in zip(lam, aligned_mask) if not k)
    return (r + 1.0 / (p - 1)) * L(p) * (sum(nu) - mis)


def C1(alpha, beta):
    t = taus(alpha, beta)
    a = sorted(alpha)
    hi = [x for x in t if x > a[3]]
    return f0(alpha, beta, hi[-1])


def report(alpha, beta, p, r=1, label=""):
    lam, nu = bricks(alpha, beta)
    m0, m1, m2, m3 = m_params(alpha, beta)
    budget = 2 * m1 + m2
    d, _, _ = delta_limit(alpha, beta)
    c1 = C1(alpha, beta)
    cp = max(1, (p - 1) // 2)                      # reflection classes of cosets
    print("\n  %s   p=%d  r=%d" % (label, p, r))
    print("    numerator brick lengths lam = %s   pole brick lengths nu = %s" % (lam, nu))
    print("    budget = 2m1+m2 = %d,  delta = %.6f,  C_2 = budget-delta = %.6f" % (budget, d, budget - d))
    print("    C_1 (archimedean coefficient growth) = %.6f" % c1)
    print("    cosets to cover simultaneously for zeta_p: phi(p)/2 = %d" % cp)
    # best alignment: put the LONGEST bricks on distinct classes; worst coset keeps the rest
    order = sorted(range(len(lam)), key=lambda i: -lam[i])
    best = None
    for keep in range(len(lam)):
        # brick `keep` is the one aligned at the worst coset
        mis = sum(lam) - lam[keep]
        val = (r + 1.0 / (p - 1)) * L(p) * (sum(nu) - mis)
        if best is None or val > best[0]:
            best = (val, keep)
    single = (r + 1.0 / (p - 1)) * L(p) * sum(nu)          # Hurwitz value: all aligned
    print("    alpha_p - growth  (single Hurwitz coset, all bricks aligned)  = %+.4f" % (single - c1))
    print("    alpha_p - growth  (zeta_p: worst coset, best split)           = %+.4f"
          % (best[0] - c1))
    print("    REQUIREMENT (DIG-2 composition rule): > C_2 = %.4f" % (budget - d))
    ok = (best[0] - c1) > budget - d
    print("    VERDICT: %s   (shortfall %.4f)" % ("PASS" if ok else "FAIL", budget - d - (best[0] - c1)))
    # most generous variant
    gen = (r + 1.0 / (p - 1)) * L(p) * sum(nu) / cp
    print("    most generous accounting (ideal even split, C_1 ignored): %.4f vs %.4f -> %s"
          % (gen, budget - d, "PASS" if gen > budget - d else "FAIL"))
    return best[0] - c1, budget - d


if __name__ == "__main__":
    print("=" * 78)
    print("THE GATE: DIG-2's crossing configuration, evaluated by the DIG-1 ledger")
    print("=" * 78)
    report((25, 26, 27, 28), (1, 8, 48, 49), p=5, r=1, label="DIG-2 crossing point")
    report((18, 17, 16, 19), (0, 7, 31, 32), p=5, r=1, label="Rhin-Viola optimum")
    report((1, 1, 1, 1), (0, 0, 2, 2), p=5, r=1, label="Apery/Ball symmetric direction")

    print("\n" + "=" * 78)
    print("why: the two terms DIG-2's model omits")
    print("=" * 78)
    for lab, al, be in [("symmetric", (1, 1, 1, 1), (0, 0, 2, 2)),
                        ("RV optimum", (18, 17, 16, 19), (0, 7, 31, 32)),
                        ("crossing", (25, 26, 27, 28), (1, 8, 48, 49))]:
        lam, nu = bricks(al, be)
        m0, m1, m2, m3 = m_params(al, be)
        bud = 2 * m1 + m2
        d, _, _ = delta_limit(al, be)
        c1 = C1(al, be)
        print("  %-12s  C_1/budget = %6.4f   coset defect (best) = %6.4f of sum(nu)"
              % (lab, c1 / bud, (sum(lam) - max(lam)) / sum(nu)))
    print("""
  Term 1  C_1/budget: zero exactly at the p-adic totally symmetric points (Beukers
          Prop 11.1(3), LSZ Lemma 20) -- which is precisely where DIG-2 proved
          delta = 0.  Buying group savings switches C_1 on, and the p-adic criterion
          (unlike the archimedean one) must pay it.
  Term 2  coset defect: for zeta_p with p >= 5 a numerator brick can be aligned to
          one coset only, so the worst coset loses all but one brick's length.""")
