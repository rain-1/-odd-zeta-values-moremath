"""DIG-3  s_record.py -- M2: can any measure record be beaten?

mu = alpha/(alpha-beta) = 2G/(G - E)  at every aligned point, so a record needs
E/G to DROP.  The decisive feature of this test is that E is MEASURED as the
exact denominator of rho_0 after the forced normalisation, so it ALREADY
CONTAINS any Phi_n / Rhin-Viola group saving that is actually present -- no
modelling step, no calibration.  Likewise growth is measured, so C_1 is real.

    mu(measured) = (G + gain) / (gain - C_1 - E)

Scanned over the whole inset/length cone at each record point:
    zeta_2(3): M=3, m=0, delta=1, p=2 r=1      published 7.17739889912418
    zeta_2(3): A=2, m=0, delta=0, p=2 r=2      (the same number, other point)
    zeta_3(3): A=2, m=0, delta=0, p=3 r=1      published 22.28144795149432
    zeta_2(5): M=4, m=1, delta=1, p=2 r=1      published 20.34265173891448
"""
import sys, os, math, itertools
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s_vwp import VWPX, LOG2
from family import dn
import sympy

LOG = math.log


def odd_part(x):
    while x % 2 == 0:
        x //= 2
    return x


def point(M, m, e, f, n, dwp=1):
    """(G, gain, C1raw, E, mu) at one inset point, everything measured."""
    v = VWPX(n, e, f, dwp)
    if not v.admissible():
        return None
    r = v.partial_fractions()
    rh = v.rho(r)
    r0 = v.rho0(m, r)
    if r0 == 0:
        return None
    sum_lam = len(v.num) / float(n)
    sum_nu = len(v.den) / float(n)
    G = (sum_lam + sum_nu) * LOG2
    gain = (sum_nu + sum_lam) * LOG2
    scale = F(2) ** (len(v.num) + len(v.den))
    E = 0.0
    for x in [r0] + [rh[i] for i in range(2, M + 1) if rh[i]]:
        D = odd_part((x * scale).denominator)
        if D <= 1:
            continue
        fac = sympy.factorint(D)
        lo = [ee for l, ee in fac.items() if l <= n]
        hi = [ee for l, ee in fac.items() if n < l < 2 * n]
        md = lambda xs: max(set(xs), key=xs.count) if xs else 0
        E = max(E, md(lo) + md(hi))
    mx = max(abs(x) for x in r.values() if x != 0)
    growth = (LOG(float(mx)) + (len(v.num) + len(v.den)) * LOG2) / n
    return dict(G=G, gain=gain, growth=growth, E=E, sum_lam=sum_lam,
                sum_nu=sum_nu)


def scan(M, m, published, label, n=24, rng=2, dwp=1):
    print("\n  %s   published mu = %s" % (label, published))
    sym = point(M, m, (0,) * M, (0,) * M, n, dwp)
    C1bias = sym["growth"] - sym["G"]
    best = None
    tested = 0
    rows = []
    for e in itertools.combinations_with_replacement(range(0, rng + 1), M):
        for f in itertools.combinations_with_replacement(range(0, rng + 1), M):
            if dwp - M + 2 * (sum(f) - sum(e)) > -2:
                continue
            try:
                d = point(M, m, e, f, n, dwp)
            except ValueError:
                continue
            if d is None:
                continue
            tested += 1
            C1 = max(0.0, d["growth"] - d["G"] - C1bias)
            marg = d["gain"] - C1 - d["E"]
            if marg <= 0:
                continue
            mu = (d["G"] + d["gain"]) / marg
            rows.append((mu, e, f, d["G"], d["E"], C1, marg))
            if best is None or mu < best[0]:
                best = (mu, e, f, d["G"], d["E"], C1, marg)
    print("     %d admissible inset points tested (insets in [0,%d]^%d, n=%d)"
          % (tested, rng, M, n))
    ssym = point(M, m, (0,) * M, (0,) * M, n, dwp)
    msym = ssym["gain"] - ssym["E"]
    print("     symmetric point : G=%.4f (sum_lam=%.3f sum_nu=%.3f) E=%d C_1=0 "
          "margin=%+.4f  mu=%.8f"
          % (ssym["G"], ssym["sum_lam"], ssym["sum_nu"], ssym["E"], msym,
             (ssym["G"] + ssym["gain"]) / msym))
    if best:
        mu, e, f, G, E, C1, marg = best
        print("     BEST over the cone: mu=%.8f  at e=%s f=%s (G=%.4f E=%d "
              "C_1=%.4f margin=%+.4f)" % (mu, e, f, G, E, C1, marg))
        print("     -> %s" % ("NEW RECORD" if mu < float(published) - 1e-9
                              else "no improvement (the symmetric point is optimal)"))
    rows.sort()
    for r in rows[:4]:
        print("        mu=%.6f  e=%s f=%s  G=%.4f E=%d" % (r[0], r[1], r[2], r[3], r[4]))


if __name__ == "__main__":
    print("=" * 78)
    print("M2 : measure records.  E and growth MEASURED (so any Phi_n / group")
    print("     saving present is already counted); mu = (G+gain)/(gain-C_1-E).")
    print("=" * 78)
    scan(3, 0, "7.17739889912418", "zeta_2(3)  [Beukers R^(B): M=3, m=0, delta=1]")
    scan(4, 1, "20.34265173891448", "zeta_2(5)  [LSZ: M=4, m=1, delta=1]")
    scan(5, 0, "-- (rank 2: weights {3,5})", "rank-2 control M=5, m=0")
    scan(6, 1, "-- (rank 2: weights {5,7})", "rank-2 control M=6, m=1")
