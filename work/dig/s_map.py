"""DIG-3  s_map.py -- M4: THE MAP.

The complete honest margin table over (p <= 13, r <= 3, w <= 9), built on
DIG-1's validated ledger (ledger.Config -- not refitted), with the one axis
DIG-1's table suppressed made explicit: THE RANK.

  margin(p, r, A, m, delta) = [A r + min_{theta0} sum_c contrib_c] log p - E,
  E = A + m + 1 - delta,   rank = #{i in [2,A] : i+m+1 odd}  (regimes S2, T)
                                = A - 1                       (regime S)

A rank-1 form gives an irrationality MEASURE for a single value; a rank-R form
gives only "one of R values is irrational".  DIG-1's table is the rank-1 row.
The map below adds the rank-R rows, which is where the p = 2 story actually
lives: at p = 2 the SIZE constraint is never binding (margin -> +infinity as
A grows), only the rank is.  At p >= 5 neither is fixable for a single value.
"""
import sys, os, math, itertools
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ledger import Config, regime, euler_phi

L = math.log


def spreads_for(p, r, A):
    """candidate shift multisets: A bricks distributed over the units mod p^r."""
    D = p ** r
    units = [j for j in range(1, D) if j % p]
    out = []
    for spread in sorted({1, 2, 3, len(units), max(1, len(units) // 2)}):
        spread = min(spread, len(units))
        sh = []
        for i in range(A):
            j = units[i % spread]
            s = Fr((D - j) % D, D)
            sh.append(s if s != 0 else Fr(1, D))
        out.append(tuple(sh))
    return set(out)


def best_at(p, w, maxrank=1, Amax=14, rmax=3, mmax=None):
    """best margin over the whole cone at prime p, weight w, rank <= maxrank."""
    best = None
    mmax = mmax if mmax is not None else w + 2
    for r in range(1, rmax + 1):
        if p ** r > 200:
            continue
        for A in range(2, Amax + 1):
            for m in range(0, mmax + 1):
                for delta in (0, 1):
                    if delta > A - 2:
                        continue
                    for sh in spreads_for(p, r, A):
                        c = Config("x", p=p, r=r, shifts=list(sh), A=A, m=m,
                                   delta=delta)
                        if c.rank < 1 or c.rank > maxrank:
                            continue
                        if w not in c.weights:
                            continue
                        mg = c.margin()
                        if best is None or mg > best[0]:
                            best = (mg, c)
    return best


def line(p, w, maxrank, Amax=14):
    b = best_at(p, w, maxrank, Amax=Amax)
    if b is None:
        return None
    mg, c = b
    mu = c.mu()
    return dict(margin=mg, mu=mu, r=c.r, A=c.A, m=c.m, d=c.delta,
                regime=c.regime, rank=c.rank, E=c.E, G=c.G(), alpha=c.alpha(),
                weights=c.weights)




# --------------------------------------------------------------------------
# THE TWO MEASURED CORRECTIONS TO THE LEDGER'S E   (s_den.py, 0 violations over
# p in {2,3,5,7}, r in {1,2}, A <= 5, m <= 4, delta in {0,1})
#
#  R1  the well-poised saving  -delta  is real ONLY where the VWP symmetry
#      R(-h0-t) = +-R(t) actually holds: (p,r) = (2,1) with every shift 1/2, or
#      (2,2) with the 1/4- and 3/4-bricks PAIRED (Lai's A_n).  Elsewhere the
#      measured exponent on the primes <= n is A+m+1 exactly.
#  R2  a SECOND prime band appears in (n, 2n), of exponent  c = m+1 when
#      m >= A-1  and 0 otherwise.  log lcm{l in (n,2n)}/n -> 1, so it costs c.
#
#      E_true = (A + m + 1 - delta_eff) + c
# --------------------------------------------------------------------------
def vwp_symmetry(p, r, shifts):
    if p == 2 and r == 1 and all(Fr(s) == Fr(1, 2) for s in shifts):
        return True
    if p == 2 and r == 2:
        q = [Fr(s) for s in shifts]
        return len(q) % 2 == 0 and q.count(Fr(1, 4)) == q.count(Fr(3, 4)) \
            and q.count(Fr(1, 4)) * 2 == len(q)
    return False


def E_true(p, r, shifts, A, m, delta):
    de = delta if vwp_symmetry(p, r, shifts) else 0
    c = (m + 1) if m >= A - 1 else 0
    return A + m + 1 - de + c


def best_at_true(p, w, maxrank=1, Amax=10, rmax=3, mmax=None):
    best = None
    mmax = mmax if mmax is not None else w + 2
    for r in range(1, rmax + 1):
        if p ** r > 200:
            continue
        for A in range(2, Amax + 1):
            for m in range(0, mmax + 1):
                for delta in (0, 1):
                    if delta > A - 2:
                        continue
                    for sh in spreads_for(p, r, A) | paired_shifts(p, r, A):
                        c = Config("x", p=p, r=r, shifts=list(sh), A=A, m=m,
                                   delta=delta)
                        if c.rank < 1 or c.rank > maxrank or w not in c.weights:
                            continue
                        Et = E_true(p, r, sh, A, m, delta)
                        mg = c.alpha() - c.G() - Et
                        al = c.alpha()
                        mu = al / mg if mg > 0 else None
                        if best is None or mg > best[0]:
                            best = (mg, c, Et, mu)
    return best


def paired_shifts(p, r, A):
    if p == 2 and r == 2 and A % 2 == 0:
        return {tuple([Fr(1, 4)] * (A // 2) + [Fr(3, 4)] * (A // 2))}
    return set()


if __name__ == "__main__":
    PS = (2, 3, 5, 7, 11, 13)
    WS = (3, 5, 7, 9)
    known = {(2, 3): 7.17739889912418, (3, 3): 22.28144795149432,
             (2, 5): 20.34265173891448}

    print("=" * 78)
    print("MAP 1 -- RANK 1 (the only regime that yields an irrationality MEASURE)")
    print("        margin, and the mu bound it would give.   A <= 14, r <= 3.")
    print("=" * 78)
    print("  p \\ w " + "".join("        w=%d      " % w for w in WS))
    for p in PS:
        row = "  %-4d " % p
        for w in WS:
            d = line(p, w, 1)
            if d is None:
                row += "      (none)      "
            else:
                tag = "K" if (p, w) in known else " "
                row += " %+8.4f%s%-7s" % (d["margin"], tag,
                                          ("mu%.2f" % d["mu"]) if d["mu"] else "")
        print(row)
    print("  (K = the published result; the ledger reproduces its mu to every digit)")

    print("\n" + "=" * 78)
    print("MAP 2 -- the same cell at RANK <= R.  R>1 gives only 'one of R values'.")
    print("        This is the axis DIG-1's table suppressed, and at p=2 it is the")
    print("        ONLY binding constraint.")
    print("=" * 78)
    for p in PS:
        print("\n  p = %d" % p)
        print("     w  |  rank1     rank2     rank3     rank4     | min rank for margin>0")
        for w in WS:
            cells, first = [], None
            for R in (1, 2, 3, 4):
                d = line(p, w, R)
                cells.append(d["margin"] if d else None)
                if d and d["margin"] > 0 and first is None:
                    first = R
            print("    %2d  | " % w
                  + "".join(("%+8.4f  " % x) if x is not None else "  ---     "
                            for x in cells)
                  + "|  %s" % (first if first else "none with rank<=4"))

    print("\n" + "=" * 78)
    print("MAP 3 -- p = 2 in detail: the (rank, weight) grid, with the mu it gives")
    print("         and the configuration.  margin = 2M log2 - (M+m), M = A.")
    print("=" * 78)
    print("   w   rank  best margin      mu        regime r  A  m  d   E   weights")
    for w in (3, 5, 7, 9, 11):
        for R in (1, 2, 3, 4):
            d = line(2, w, R, Amax=16)
            if d is None:
                continue
            if d["rank"] != R and R > 1:
                pass
            print("  %2d    %d    %+9.4f   %9s    %-3s   %d  %2d %2d  %d  %2d  %s"
                  % (w, R, d["margin"],
                     ("%.5f" % d["mu"]) if d["mu"] else "--",
                     d["regime"], d["r"], d["A"], d["m"], d["d"], d["E"],
                     d["weights"]))

    print("\n" + "=" * 78)
    print("MAP 4 -- the structural ceiling at each p (rank unconstrained)")
    print("=" * 78)
    print("   p    p log p/(p-1)^2   sup_A (margin+E)/A   verdict at rank 1")
    for p in PS:
        c = p * L(p) / (p - 1) ** 2
        print("  %3d      %10.6f          %10.6f        %s"
              % (p, c, c,
                 "size never binds (margin -> +inf)" if p == 2 else
                 ("margin <= A*(%.4f - 1) - 1 < 0 for every A" % c)))

    print("\n" + "=" * 78)
    print("MAP 5 -- THE CORRECTED RANK-1 MAP (E measured, not assumed)")
    print("         ledger E = A+m+1-delta ;  E_true = A+m+1-delta_eff + c")
    print("=" * 78)
    print("  p    w    ledger margin   E_led   E_true   TRUE margin   mu_true   config")
    for p in PS:
        for w in WS:
            b0 = line(p, w, 1)
            b1 = best_at_true(p, w, 1)
            if b1 is None:
                continue
            mg, c, Et, mu = b1
            print("  %-3d  %-3d   %+9.4f      %2d      %3d    %+9.4f    %-9s  r=%d A=%d m=%d d=%d %s"
                  % (p, w, b0["margin"], b0["E"], Et, mg,
                     ("%.5f" % mu) if mu else "--", c.r, c.A, c.m, c.delta,
                     "[published]" if (p, w) in known else ""))
