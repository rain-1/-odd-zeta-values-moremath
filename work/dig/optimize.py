"""DIG-1  T4 : margin(params; p, w) and the exhaustive rank-1 optimiser (for DIG-3).

A configuration is (p, r, A, m, delta, shift-multiset).  Everything else -- the
regime, the surviving weights, the rank, the denominator cost E, alpha, beta and
the margin -- is derived in ledger.py.

RANK-1 (a two-term form in 1 and a single zeta value, the only kind that yields an
irrationality measure) forces:
   regime S   (phi(p^r) = 2, i.e. (p,r) in {(2,2),(3,1)}) :  A = 2, delta = 0, w = m+3
   regime S2  (p = 2, r = 1)                              :  m even -> A in {2,3}, w = m+3
                                                             m odd  -> A in {3,4}, w = m+4
   regime T   (everything else)                           :  same parity rule as S2
   plus the degree condition  delta <= A - 2.
"""
import sys, os, math
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ledger import Config, regime, euler_phi, vp_frac


def rank1_configs(p, w, rmax=3, Amax=6, Dcap=60):
    """All rank-1 configurations of weight w at prime p.

    Rank 1 pins the derivative order: the single surviving index is i=2 (m even,
    w = m+3) or i=3 (m odd, w = m+4), so m in {w-3, w-4}.
    Deeper shifts are capped by Dcap: in regime T raising r multiplies the number
    of cosets at which the SAME form must be small, and the worst-case rate can
    only drop (T4.4), so the optimum never sits at large r there; in regime S,
    phi(p^r)=2 already forces p^r in {3,4}.
    """
    out = []
    for r in range(1, rmax + 1):
        D = p ** r
        if D > Dcap:
            continue
        units = [j for j in range(1, D) if j % p]
        spreads = sorted({min(k, len(units)) for k in (1, 2, 3, len(units))})
        for A in range(2, Amax + 1):
            for m in {w - 3, w - 4}:
                if m < 0:
                    continue
                for delta in (0, 1):
                    if delta > A - 2:
                        continue
                    for spread in spreads:
                        # A copies spread over `spread` distinct target cosets
                        shifts = [Fr((D - units[i % spread]) % D, D) for i in range(A)]
                        shifts = [s if s != 0 else Fr(1, D) for s in shifts]
                        c = Config("p%d r%d A%d m%d d%d s%d" % (p, r, A, m, delta, spread),
                                   p=p, r=r, shifts=shifts, A=A, m=m, delta=delta)
                        if c.rank != 1 or c.weights[0] != w:
                            continue
                        out.append(c)
    return out


def best(p, w, **kw):
    cs = rank1_configs(p, w, **kw)
    if not cs:
        return None
    return max(cs, key=lambda c: c.margin())


if __name__ == "__main__":
    print("=" * 78)
    print("T4  best rank-1 margin over the WHOLE parameter space, per (p, weight)")
    print("=" * 78)
    print("  p    w   regime  r  A  m  d   G          E   margin      mu bound   status")
    known = {(2, 3), (3, 3), (2, 5)}
    for p in (2, 3, 5, 7, 11, 13):
        for w in (3, 5, 7, 9):
            c = best(p, w)
            if c is None:
                print("  %-3d  %-3d  (no rank-1 configuration)" % (p, w))
                continue
            mu = c.mu()
            st = "KNOWN" if (p, w) in known else ("=> WOULD BE NEW" if c.margin() > 0 else "gap %.4f" % -c.margin())
            print("  %-3d  %-3d  %-6s  %d  %d  %d  %d   %-9.4f  %-3d %+9.4f   %-10s %s"
                  % (p, w, c.regime, c.r, c.A, c.m, c.delta, c.G(), c.E, c.margin(),
                     ("%.4f" % mu) if mu else "--", st))

    print("\n" + "=" * 78)
    print("T4  sanity anchors and the CORRECTED deficits")
    print("=" * 78)
    for (p, w, tag) in [(2, 3, "zeta_2(3)"), (3, 3, "zeta_3(3)"), (2, 5, "zeta_2(5)"),
                        (2, 7, "zeta_2(7)"), (3, 5, "zeta_3(5)"), (5, 3, "zeta_5(3)"),
                        (7, 3, "zeta_7(3)"), (5, 5, "zeta_5(5)")]:
        c = best(p, w)
        fit = {"zeta_5(3)": -0.5858, "zeta_3(5)": -0.6056}.get(tag)
        extra = ("   [PADIC_SEAM fitted law said %+.4f]" % fit) if fit else ""
        print("  %-10s best margin = %+.4f   (regime %s, r=%d A=%d m=%d)%s"
              % (tag, c.margin(), c.regime, c.r, c.A, c.m, extra))

    print("\n" + "=" * 78)
    print("T4  freedom map: d(margin)/d(parameter) at the LSZ point (p=2,r=1,A=4,m=1,d=1)")
    print("=" * 78)
    base = Config("base", p=2, r=1, shifts=[Fr(1, 2)] * 4, A=4, m=1, delta=1)
    print("   baseline: G=%.4f  E=%d  margin=%+.4f  rank=%d  weights=%s"
          % (base.G(), base.E, base.margin(), base.rank, base.weights))
    variants = [
        ("A -> 5 (one more Pochhammer/pole)", Config("v", p=2, r=1, shifts=[Fr(1, 2)] * 5, A=5, m=1, delta=1)),
        ("A -> 6 (two more)", Config("v", p=2, r=1, shifts=[Fr(1, 2)] * 6, A=6, m=1, delta=1)),
        ("m -> 3 (deeper derivative)", Config("v", p=2, r=1, shifts=[Fr(1, 2)] * 4, A=4, m=3, delta=1)),
        ("delta -> 0 (drop well-poised)", Config("v", p=2, r=1, shifts=[Fr(1, 2)] * 4, A=4, m=1, delta=0)),
        ("r -> 2 (deeper shift, 1/4)", Config("v", p=2, r=2, shifts=[Fr(3, 4)] * 4, A=4, m=1, delta=1)),
        ("asymmetric shifts (2 at 1/2, 2 at 1/4-class)",
         Config("v", p=2, r=2, shifts=[Fr(3, 4)] * 2 + [Fr(1, 4)] * 2, A=4, m=1, delta=1)),
    ]
    for name, c in variants:
        print("   %-46s G=%-8.4f E=%-3d rank=%d w=%s margin=%+.4f"
              % (name, c.G(), c.E, c.rank, c.weights, c.margin()))
