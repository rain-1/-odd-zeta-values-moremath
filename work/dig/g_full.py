"""g_full.py -- COMPLETE search for transfer identities in the very-well-poised
half-integer family, and classification of which points are p-adically usable.

Family (h_0 in Z, h_j in (1/2)Z, j = 1..q):

    R(h;t) = (h_0+2t) * prod_{j=1}^{q} Gamma(h_j+t)/Gamma(1+h_0-h_j+t)

  brick j is a DENOMINATOR brick  1/(t+h_j)_{1+h_0-2h_j}      if h_j <= (1+h_0)/2
  brick j is a NUMERATOR   brick  (t+1+h_0-h_j)_{2h_j-1-h_0}  if h_j >  (1+h_0)/2

p-ADIC ADMISSIBILITY (Volkenborn at shift theta = 1/2, p = 2):
  (R1) every pole of R must be at an integer   -> denominator h_j in Z
  (R2) every numerator factor must be p-integral after the shift, i.e. the
       numerator brick must sit at a half-integer shift -> h_j in Z + 1/2
  (both required; (R2) failing costs l per factor instead of gaining 1/(p-1)).

Two points carry a transfer identity iff their linear forms are exactly
PROPORTIONAL.  We canonicalise the spectral vector
    V(h) = ( rho_{c,i} )_{c in Q/Z, i>=1} together with the rational part
and bucket by the normalised vector -- so the search is linear, not quadratic,
and therefore EXHAUSTIVE over the enumerated shapes.
"""

import itertools
import sys
from fractions import Fraction as F
from collections import defaultdict

from g_verify import partial_fractions


def bricks(h0, hs):
    num, den = [], []
    for hj in hs:
        if 2 * hj <= h0 + 1:
            L = 1 + h0 - 2 * hj
            if L < 1:
                return None
            den += [F(hj) + i for i in range(int(L))]
        else:
            L = 2 * hj - 1 - h0
            if L < 1:
                return None
            s = F(1 + h0) - hj
            num += [s + i for i in range(int(L))]
    return num, den


def spectral(h0, hs):
    b = bricks(h0, hs)
    if b is None:
        return None
    num, den = b
    deg = 1 + len(num) - len(den)
    if deg > -2:
        return None
    if not den:
        return None
    try:
        r = partial_fractions(num, den, (h0, 2))
    except Exception:
        return None
    if not r:
        return None
    rho = defaultdict(F)
    B = F(0)
    for (i, k), v in r.items():
        cls = F(k) - (F(k).numerator // F(k).denominator)
        rho[(cls, i)] += v
        k0 = cls if cls != 0 else F(1)
        m = int(F(k) - k0)
        if m < 0:
            return None
        B -= v * sum(F(1) / (k0 + l) ** i for l in range(m))
    rho[("B", 0)] = B
    return dict(rho)


def canon(vec):
    keys = sorted(vec, key=lambda t: (str(t[0]), t[1]))
    piv = None
    for k in keys:
        if vec[k] != 0:
            piv = vec[k]
            break
    if piv is None:
        return None
    return tuple((str(k), vec[k] / piv) for k in keys if vec[k] != 0)


def padic_ok(h0, hs):
    """(R1) + (R2) for theta = 1/2."""
    for hj in hs:
        if 2 * hj <= h0 + 1:
            if hj != int(hj):
                return False               # pole at a half-integer -> forbidden
        else:
            s = F(1 + h0) - hj             # numerator brick shift
            if (s - int(s)) != F(1, 2):
                return False               # numerator not aligned with -theta
    return True


def main():
    h0max = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    qs = [int(x) for x in (sys.argv[2].split(",") if len(sys.argv) > 2
                           else ["4", "5", "6"])]
    buckets = defaultdict(list)
    total = 0
    for h0 in range(2, h0max + 1):
        vals = [F(v, 2) for v in range(1, 2 * h0 + 1)]
        for q in qs:
            for hs in itertools.combinations_with_replacement(vals, q):
                vec = spectral(h0, hs)
                if vec is None:
                    continue
                c = canon(vec)
                if c is None:
                    continue
                total += 1
                buckets[c].append((h0, hs))
    print(f"enumerated {total} valid VWP shapes (h0 <= {h0max}, q in {qs})")
    multi = {k: v for k, v in buckets.items() if len(v) > 1}
    print(f"proportionality classes with >1 member: {len(multi)}")

    # Now: how many of those classes contain a p-adically admissible point?
    n_padic_pts = 0
    n_padic_with_partner = 0
    examples = []
    for h0 in range(2, h0max + 1):
        pass
    for c, mem in buckets.items():
        pads = [m for m in mem if padic_ok(*m)]
        n_padic_pts += len(pads)
        if pads and len(mem) > 1:
            n_padic_with_partner += len(pads)
            if len(examples) < 8:
                examples.append((pads[0], [m for m in mem if m != pads[0]][:3]))
    print(f"p-adically admissible shapes enumerated: {n_padic_pts}")
    print(f"   ... of which have a NON-trivial transfer partner: "
          f"{n_padic_with_partner}")
    for a, part in examples:
        print(f"   {a}  <->  {part}")

    # sanity: show a few non-trivial classes (should include the RV orbit)
    shown = 0
    for c, mem in sorted(multi.items(), key=lambda kv: -len(kv[1])):
        if shown >= 5:
            break
        shown += 1
        print(f"   class size {len(mem)}: {mem[:6]}"
              f"{'...' if len(mem) > 6 else ''}")


if __name__ == "__main__":
    main()
