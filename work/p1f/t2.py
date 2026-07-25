"""T2: the residue density R(k,l) := (p * T * v5 mod p) in F_p, at L = 0.

Cellwise v_p(T v5) >= -1  (DEPTH + Lemma K).  So (BASE) at level n < p is EXACTLY
        sum_{k,l} R(k,l) == 0 in F_p .
Map out where R != 0 and look for pairing structure.
"""
import sys
from fractions import Fraction as F
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1f')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1d')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from w5eval import v5, Tl
from core import vp
from kgrade import pattern


def resid(x, p):
    """x a Fraction with v_p(x) >= 0 -> x mod p in {0..p-1}"""
    a, b = x.numerator, x.denominator
    assert b % p, x
    return (a * pow(b, -1, p)) % p


def cell_R(n, k, l, p):
    V = v5(n, k, l)
    if V == 0:
        return 0
    x = F(p) * Tl(n, k, l) * V
    assert vp(x, p) >= 0, (n, k, l, vp(x, p))
    return resid(x, p)


if __name__ == '__main__':
    PR = [int(x) for x in (sys.argv[1:] or ['5', '7', '11', '13'])]
    for p in PR:
        for n in range(1, p):
            R = {}
            for k in range(n + 1):
                for l in range(n + 1):
                    r = cell_R(n, k, l, p)
                    if r:
                        R[(k, l)] = r
            tot = sum(R.values()) % p
            print('p=%2d n=%2d  nonzero cells=%3d  SUM=%d' % (p, n, len(R), tot))
            if R:
                for (k, l), r in sorted(R.items()):
                    pat = pattern(n, k, l, p, 1)
                    print('        (k,l)=(%2d,%2d) R=%2d  pat=%s' % (k, l, r, pat))
