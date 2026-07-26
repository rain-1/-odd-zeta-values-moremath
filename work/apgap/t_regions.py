"""TEST 1: does the region decomposition reproduce the measured second-order defect?

  D2(a,r) := ( a_{ap+r} - a_a (a_r + 2p a U_r) ) / p^2   mod p

Predicted (derivation in gap_core docstring; all Delta terms cancel identically):

  D2 == a^2 m0 Sa2 + a m1 Sac + m2 Scc + (a^2 m0 - 2 a m1 + m2) Xi     (mod p)

with m0,m1,m2 = sum_c c^j A(a,c) and Sa2,Sac,Scc the three channel sums over s<=r.
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/apdef')
from fractions import Fraction as F
from core import A, av, modp, vp
from gap_core import sigmas, Xi, Delta, moments, Ur, Vr

PRIMES = [5, 7, 11, 13, 17, 19, 23]


def measured_D2(p, a, r):
    n = a * p + r
    val = av(n) - av(a) * av(r) - 2 * p * a * av(a) * Ur(r)
    q = F(val, p ** 2)
    return modp(q, p)


def predicted_D2(p, a, r):
    m0, m1, m2 = moments(a)
    Sa2, Sac, Scc = sigmas(r)
    X = Xi(p, r)
    q = a * a * m0 * Sa2 + a * m1 * Sac + m2 * Scc + (a * a * m0 - 2 * a * m1 + m2) * X
    return modp(q, p)


if __name__ == '__main__':
    print('p    cells  mismatches')
    allok = True
    for p in PRIMES:
        bad = []
        for a in range(p):
            for r in range(p):
                if measured_D2(p, a, r) != predicted_D2(p, a, r):
                    bad.append((a, r))
        allok &= not bad
        print('%-4d %-6d %s' % (p, p * p, len(bad) if bad else 'NONE'))
        if bad:
            print('   first few:', bad[:8])
    print('\nregion decomposition exact mod p^3 :', allok)
