"""DIG-1  T2/T3 : the exact cost ledger of the p-adic Volkenborn / Pade construction.

Every component is DERIVED (see work/DIG_LEDGER.md for the derivations and the
source lines each is checked against).  Nothing here is fitted.

CONFIGURATION (the free parameter tuple), cf. T1:
    p          prime
    r          depth of the *integration* shift theta0 = a/p^r   (v_p(theta0) = -r)
    shifts     multiset of numerator Pochhammer shifts theta'_c (as Fractions),
               one entry per Pochhammer copy   (|shifts| = M copies)
    A          pole order of (t)_{n+1}^A        (denominator copies)
    m          derivative order applied before integrating  (m = -1 : primitive)
    E          denominator cost exponent  (power of d_n ~ e^n that must be cleared),
               E = A + m + 1 naively, minus any well-poised/Phi_n saving
    classes    the set of integration shifts at which the SAME form must be small
               (for zeta_p:  the phi(q_p)/2 reflection classes; for a single
               Hurwitz value: one shift)

LEDGER (all quantities are the coefficient of n, i.e. exponential rates):

  G   := v_p(C) * log p ,  v_p(C) = sum_c l'_c + A/(p-1)      [normalisation = arch. growth]
  alpha  = [ v_p(C) + A*r + sum_c contrib_c(theta0) ] * log p   minimised over theta0 in classes
  beta   = G + E
  margin = alpha - beta = [ A*r + sum_c contrib_c ] * log p - E
  mu    <= alpha/(alpha-beta)                                    [Bel's lemma]

  contrib_c(theta0) = +1/(p-1)        if theta'_c + theta0 in Z_p   ("aligned")
                    = -l''            otherwise, l'' = -v_p(theta'_c + theta0)

In the fully aligned case (all M = A copies of depth l' = r aligned):
  alpha = 2G,  beta = G + E,  margin = G - E,  mu <= 2G/(G-E).
"""
from fractions import Fraction as Fr
import mpmath as mp

mp.mp.dps = 40


def vp_frac(x, p):
    """p-adic valuation of a Fraction (0 -> None)."""
    if x == 0:
        return None
    num, den = x.numerator, x.denominator
    v = 0
    while num % p == 0:
        num //= p
        v += 1
    while den % p == 0:
        den //= p
        v -= 1
    return v


def euler_phi(n):
    r, m, q = n, n, 2
    while q * q <= m:
        if m % q == 0:
            r -= r // q
            while m % q == 0:
                m //= q
        q += 1
    if m > 1:
        r -= r // m
    return r


def regime(p, r):
    """'S' = single-shift (the Hurwitz value at a/p^r is a rational multiple of
    zeta_p), 'S2' = the exceptional p=2,r=1 point (LSZ Lemma 9: the shift 1/2
    already IS the full zeta_2, so even weights vanish), 'T' = twisted sum."""
    if p == 2 and r == 1:
        return "S2"
    return "S" if euler_phi(p ** r) == 2 else "T"


def rank_and_weight(p, r, A, m):
    """Which zeta/Hurwitz values actually occur (i=1 is killed by deg R <= -2).
    Returns (list of weights, rank)."""
    reg = regime(p, r)
    ws = []
    for i in range(2, A + 1):
        w = i + m + 1
        if reg in ("S2", "T") and w % 2 == 0:
            continue                      # zeta_p(even) = 0  (full zeta only)
        ws.append(w)
    return ws, len(ws)


class Config:
    """A point in the parameter space of the construction."""

    def __init__(self, name, p, r, shifts, A, m, E=None, delta=0, classes=None, note=""):
        self.name, self.p, self.r, self.A, self.m, self.note = name, p, r, A, m, note
        self.delta = delta
        self.shifts = [Fr(s) for s in shifts]
        self.M = len(self.shifts)
        # DERIVED denominator cost:  d_n^{A+m+1}, minus 1 for the well-poised factor
        self.E = (A + m + 1 - delta) if E is None else E
        self.regime = regime(p, r)
        self.weights, self.rank = rank_and_weight(p, r, A, m)
        # degree condition  deg R = delta + M n - A(n+1) <= -2
        self.deg_ok = (self.M <= A) and (delta - A <= -2 or self.M < A)
        # integration shifts at which smallness is simultaneously required
        if classes is None:
            D = p ** r
            classes = ([Fr(1, D)] if self.regime in ("S", "S2")
                       else [Fr(j, D) for j in range(1, D) if j % p])
        self.classes = [Fr(c) for c in classes]

    # ---- ledger components -------------------------------------------------
    def vpC(self):
        """v_p of the forced normalisation constant C (per n).
        = (fractional content of the numerator Pochhammers) + (factorial content
          of the (k!(n-k)!)^A from the poles)."""
        return sum(max(0, -vp_frac(s, self.p)) for s in self.shifts) + Fr(self.A, self.p - 1)

    def G(self):
        """archimedean growth rate of the coefficients = log C  (balanced case)."""
        return float(self.vpC()) * mp.log(self.p)

    def contribs(self, theta0):
        """per-copy p-adic contribution at a given integration shift."""
        out = []
        for s in self.shifts:
            sig = s + theta0
            v = vp_frac(sig, self.p)
            if v is None or v >= 0:            # aligned: sigma in Z_p
                out.append(Fr(1, self.p - 1))
            else:
                out.append(Fr(v))              # = -l''
        return out

    def margin_rate(self, theta0):
        """[A*r + sum contrib] : the margin BEFORE subtracting E, in units of log p."""
        return Fr(self.A * self.r) + sum(self.contribs(theta0))

    def worst_class(self):
        return min(self.classes, key=lambda t0: self.margin_rate(t0))

    def alpha(self):
        t0 = self.worst_class()
        return float(self.vpC() + self.margin_rate(t0)) * mp.log(self.p)

    def beta(self):
        return self.G() + self.E

    def margin(self):
        return self.alpha() - self.beta()

    def mu(self):
        a, b = self.alpha(), self.beta()
        if a <= b:
            return None
        return a / (a - b)

    def report(self):
        t0 = self.worst_class()
        al = [c for c in self.contribs(t0)]
        return dict(name=self.name, p=self.p, r=self.r, A=self.A, m=self.m, E=self.E,
                    M=self.M, vpC=self.vpC(), worst_shift=t0, contribs=al,
                    G=self.G(), alpha=self.alpha(), beta=self.beta(),
                    margin=self.margin(), mu=self.mu(), note=self.note)


# ---------------------------------------------------------------------------
#  The published configurations (T3 anchors).  Every parameter is read off the
#  source; the measures are NOT used as input anywhere.
# ---------------------------------------------------------------------------
def published():
    """The published anchors.  ONLY (p, r, shifts, A, m, delta) go in;
    E, the regime, the rank and the weight are DERIVED."""
    cfgs = []

    # 1. zeta_2(3):  Beukers 2008 (arXiv math/0603277) Cor. 11.3/11.4 with F = 4,
    #    T_2(1/4) = 4^3 zeta_2(3) (Prop 5.2.1).  Pade denominators q_n = coefficients
    #    of (1-z)^{2a/F-1} 2F1(a/F,a/F,1,z)^2  ->  TWO Pochhammer copies of shift a/F
    #    = 1/4 (depth r = 2); poles of order A = 2; weight-3 object, cost lcm^3.
    #    Equivalently (LSZ final remarks / Lai 2304.00816 (3.2) at s=0):
    #      R_n = 2^{6n} (t+3/4)_n^2/(t)_{n+1}^2 , integrated at theta0 = 1/4.
    cfgs.append(Config("zeta_2(3)  [Beukers F=4 / Lai B_n s=0]", p=2, r=2,
                       shifts=[Fr(3, 4), Fr(3, 4)], A=2, m=0, delta=0,
                       note="phi(4)=2: one reflection class, H_2(3,1,4)=H_2(3,3,4)"))
    # the SAME measure from a different parameter point: Beukers' R^{(B)} =
    # 2^{6n}(2t+n)(t+1/2)^3_n/(t)^3_{n+1} at theta0 = 1/2  (LSZ final remarks:
    # "these linear forms coincide") -- an internal consistency check of the ledger.
    cfgs.append(Config("zeta_2(3)  [Beukers R^(B), r=1]", p=2, r=1,
                       shifts=[Fr(1, 2)] * 3, A=3, m=0, delta=1,
                       note="p=2,r=1: even weights vanish, so A=3 still has rank 1"))

    # 2. zeta_3(3):  Beukers Cor. 11.4 with F = 3, T_3(1/3) = 3^3 zeta_3(3) (Prop 5.2.2).
    #    Two copies of shift a/F (depth r = 1), A = 2, weight 3, cost lcm^3.
    cfgs.append(Config("zeta_3(3)  [Beukers F=3]", p=3, r=1,
                       shifts=[Fr(2, 3), Fr(2, 3)], A=2, m=0, delta=0,
                       note="phi(q_3)/2 = 1 reflection class: H_3(3,1,3)=H_3(3,2,3)"))

    # 3. zeta_2(5):  Lai-Sprang-Zudilin 2025 (arXiv 2505.05005) Def. 10/11:
    #    R_n = 2^{8n}(2t+n)(t+1/2)^4_n/(t)^4_{n+1}, S_n = -Int R_n'(t+1/2)dt.
    #    A = 4, m = 1, four copies of shift 1/2 (depth 1), theta0 = 1/2 (r=1).
    #    E: Lemma 16 gives d_n^6, Lemma 19 the Phi_n saving -> e^{5n} (= their beta-3).
    cfgs.append(Config("zeta_2(5)  [LSZ 2025]", p=2, r=1,
                       shifts=[Fr(1, 2)] * 4, A=4, m=1, delta=1,
                       note="A+m+1 = 6 naive, Phi_n saving 1 -> E = 5 (their (den-con))"))
    return cfgs


def lai_families(smax=3):
    """Lai arXiv:2304.00816 -- two genuinely parametrised families (cross-checks).
       B_n(t) = 2^{(3s+6)n} (t+3/4)_n^{s+2}/(t)_{n+1}^{s+2},  T_n = Int B_n^{(s)}(t+1/4)
       A_n(t) = 2^{(6s+12)n}(4t+2n)^d (t+1/4)_n^{s+2}(t+3/4)_n^{s+2}/(t)_{n+1}^{2s+4}
    """
    out = []
    for s in range(smax + 1):
        out.append(("B", s,
                    Config("Lai B_n s=%d" % s, p=2, r=2, shifts=[Fr(3, 4)] * (s + 2),
                           A=s + 2, m=s, delta=0)))
        out.append(("A", s,
                    Config("Lai A_n s=%d" % s, p=2, r=2,
                           shifts=[Fr(1, 4)] * (s + 2) + [Fr(3, 4)] * (s + 2),
                           A=2 * s + 4, m=s, delta=1)))
    return out


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 78)
    print("T3 GATE : published irrationality measures from the first-principles ledger")
    print("=" * 78)
    PUB = {"zeta_2(3)  [Beukers F=4 / Lai B_n s=0]": "7.177398",
           "zeta_2(3)  [Beukers R^(B), r=1]": "7.177398",
           "zeta_3(3)  [Beukers F=3]": "22.281447",
           "zeta_2(5)  [LSZ 2025]": "20.342651"}
    ok = True
    for c in published():
        R = c.report()
        mu = R["mu"]
        s = mp.nstr(mu, 16)
        hit = s.startswith(PUB[c.name])
        ok &= hit
        print("\n%s   [%s]" % (c.name, "MATCH" if hit else "MISMATCH"))
        print("   params: p=%d r=%d A=%d m=%d delta=%d  shifts=%s" %
              (c.p, c.r, c.A, c.m, c.delta, [str(x) for x in c.shifts]))
        print("   DERIVED: regime %s | weights %s | rank %d | E = A+m+1-delta = %d"
              % (c.regime, c.weights, c.rank, c.E))
        print("   v_p(C) = %s   contribs at worst shift %s : %s" %
              (R["vpC"], R["worst_shift"], [str(x) for x in R["contribs"]]))
        print("   alpha  = %s" % mp.nstr(R["alpha"], 14))
        print("   beta   = %s   (= G + E, G = %s)" % (mp.nstr(R["beta"], 14), mp.nstr(R["G"], 12)))
        print("   margin = %s" % mp.nstr(R["margin"], 12))
        print("   mu    <= %s      published: %s..." % (s, PUB[c.name]))
    print("\n" + "=" * 78)
    print("T3 VERDICT:", "PASS - all three published measures reproduced" if ok else "FAIL")
    print("=" * 78)

    print("\nCross-check on Lai's parametrised families (arXiv:2304.00816):")
    print("  family  s   alpha/log2 (pred)   Lai's printed rate    margin (pred)   Lai's printed")
    for fam, s, c in lai_families(3):
        a_rate = c.alpha() / mp.log(2)
        marg = c.margin()
        if fam == "B":
            lai_alpha = 6 * s + 12                      # |d_n^{2s+3} T_n|_2 <= 2^{-(6s+12)n}
            lai_margin = -( (2 - 3 * mp.log(2)) * s + 3 - 6 * mp.log(2) )
        else:
            lai_alpha = 10 * s + 20                     # |Phi^{-s-2}d^{3s+5} S_n|_2 <= 2^{-(10s+20)n}
            lai_margin = -( (4 - 6 * mp.log(2)) * s + 7 - 12 * mp.log(2) )
        print("   %s    %d   %18s   %18s   %13s  %13s" %
              (fam, s, mp.nstr(a_rate, 10), lai_alpha,
               mp.nstr(marg, 10), mp.nstr(lai_margin, 10)))
