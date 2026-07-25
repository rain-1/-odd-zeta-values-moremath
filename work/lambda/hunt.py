"""LLL-based p-adic integer-relation hunting, with honest noise floors.
Wraps the exact-Fraction LLL of ../padic_seam/lll.py.
A relation  sum c_i x_i = 0 mod p^K  found among m values is MEANINGFUL only if its
height is well below the noise floor p^{K/m} (heuristic: random lattices give shortest
vectors of that size)."""
import sys, os
from fractions import Fraction as Fr
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "padic_seam"))
from lll import lll, padic_relation, rat_recon
from pnum import P

def relation(vals, p, K, names=None, top=3, verbose=True, tag=""):
    """vals: list of ints mod p^K (already p-integral, scaled).  Returns list of
       (height, coeffs)."""
    m = len(vals)
    out = padic_relation([v % p**K for v in vals], p, K)
    floor = float(p)**(K/float(m))
    res = []
    for norm, c, chk in out[:top]:
        h = max(abs(x) for x in c)
        res.append((h, c))
    if verbose:
        nm = names or ["x%d" % i for i in range(m)]
        best = res[0] if res else None
        if best:
            print("   %-38s m=%d K=%-3d best height %.3e   floor %.3e  %s"
                  % (tag or "+".join(nm), m, K, float(best[0]), floor,
                     "**CANDIDATE**" if best[0] < floor/50 else "noise"))
            if best[0] < floor/50:
                print("        ", dict(zip(nm, best[1])))
    return res, floor

def scale(xs):
    """list of P -> (list of ints mod p^K, K) at the common certified precision."""
    p = xs[0].p
    v0 = min(x.v for x in xs)
    K = min(x.v + x.prec for x in xs) - v0
    return [(x.u * p**(x.v - v0)) % p**K for x in xs], K

def alg_test(x, deg, p, tag="", top=3):
    """is x algebraic of degree <= deg over Q?  test on (1, x, x^2, ..., x^deg)."""
    pw = [P.from_frac(p, 1, x.prec)]
    for i in range(deg):
        pw.append(pw[-1] * x)
    vals, K = scale(pw)
    return relation(vals, p, K, ["1"] + ["x^%d" % i for i in range(1, deg+1)],
                    tag=tag or "alg deg %d" % deg, top=top)

def selftest(p, K):
    """validate the finder on a KNOWN relation: log_p(4) = 2 log_p(2)."""
    from zoo import iwasawa_log
    l2 = iwasawa_log(2, p, K)
    l4 = iwasawa_log(4, p, K)
    vals, KK = scale([l2, l4])
    print("  selftest log_p(4) - 2log_p(2):")
    r, fl = relation(vals, p, KK, ["log2", "log4"], tag="selftest (log2,log4)")
    l3 = iwasawa_log(3, p, K)
    l6 = iwasawa_log(6, p, K)
    vals, KK = scale([l2, l3, l6])
    relation(vals, p, KK, ["log2", "log3", "log6"], tag="selftest (log2,log3,log6)")
    # a planted 3-term relation with a genuine constant
    from zoo import zeta_p_val
    z3 = zeta_p_val(3, p, K)
    one = P.from_frac(p, 1, K)
    planted = (z3 * 7 + one * 3) / P.from_frac(p, 5, K)
    vals, KK = scale([one, z3, planted])
    relation(vals, p, KK, ["1", "z3", "planted"], tag="selftest planted (1,z3,(7z3+3)/5)")
