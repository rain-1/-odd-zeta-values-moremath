"""Block-by-block check of the (here proved) structure theorem for

    Atil_a = lim_s a_{a p^s} = 1 + sum_{i>=0} sum_{0<j<=a p^i, p !| j}
                                    [ c_p(a p^i, j) c_p(a p^i + j, j) ]^2 ,

for a = 1 AND a = 2 (Paper C verifies a = 1 only).  Exact arithmetic throughout:
a_n is built as an exact integer from the double sum, the Kazandzidis limits from
lam.kaz_batch.
"""
import os, sys
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lam import kaz_batch, P, unit_prod_batch, binom_mod, _needed   # noqa: E402


def apery_a(n):
    return sum(comb(n, k) ** 2 * comb(n + k, k) ** 2 for k in range(n + 1))


def Atil(a, p, K, smax):
    """lim_s a_{a p^s} to 3(smax+1) certified digits (Beukers-Coster, 3/level)."""
    vals = [P(p, 0, apery_a(a * p ** s) % p ** (K + 6), K + 6) for s in range(smax + 1)]
    ag = [vals[s].agree(vals[s - 1]) for s in range(1, smax + 1)]
    return vals[-1].trunc(3 * (smax + 1)), ag


def blocks(a, p, K, imax):
    idx = []
    for i in range(imax + 1):
        for j in range(1, a * p ** i + 1):
            if j % p:
                idx.append((i, j))
    pairs = set()
    for (i, j) in idx:
        A = a * p ** i
        if A > j:
            pairs.add((A, j))
        pairs.add((A + j, j))
    C, _ = kaz_batch(sorted(pairs), p, K)
    one = P.from_frac(p, 1, K)
    out = {}
    tot = one
    for i in range(imax + 1):
        for j in range(1, a * p ** i + 1):
            if j % p == 0:
                continue
            A = a * p ** i
            c1 = one if A == j else C[(A, j)]
            c2 = C[(A + j, j)]
            t = (c1 * c2)
            tot = tot + t * t
        out[i] = tot
    return out


if __name__ == "__main__":
    K = 12
    for p in [int(x) for x in sys.argv[1:]] or [5, 7]:
        smax = {5: 4, 7: 3, 11: 3, 13: 2}[p]
        print("=" * 74)
        for a in (1, 2):
            At, ag = Atil(a, p, K, smax)
            print("p=%-3d a=%d   Atil = %s   (v=%d, per-level agreement %s)"
                  % (p, a, " ".join(map(str, At.digits(8))), At.v, ag))
            bl = blocks(a, p, K, 1)
            for i, val in sorted(bl.items()):
                d = At - val
                print("      blocks i<=%d : first discrepancy at v_p = %s   (theory: >= %d)"
                      % (i, "none" if d.is_zero() else d.v, 2 * (i + 1)))
