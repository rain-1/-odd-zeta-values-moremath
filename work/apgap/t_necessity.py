"""TEST 6: are R1,R2 also NECESSARY?

From the proved assembly, "D2 == a^2 m0 X_p(r) for all a" is equivalent to

    a m1(a) * (Sac - 2 Xi)  +  m2(a) * (Scc + Xi)  ==  0   for all a,

so if the vectors { (a m1(a), m2(a)) : 0<=a<p } span F_p^2 then the measured
a-side-exactly-a^2 forces  Sac == 2 Xi  and  Scc == -Xi  (mod p).  Check the span,
for the a-row weight (omega=1) and the b-row weight (omega = 2H3_a - H3_c).
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/apdef')
from core import A, Hs, modp, rank_fp
from gap_core import moments

PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def bmom(a):
    w = [2 * Hs(a, 3) - Hs(c, 3) for c in range(a + 1)]
    return (sum(c * A(a, c) * w[c] for c in range(a + 1)),
            sum(c * c * A(a, c) * w[c] for c in range(a + 1)))


if __name__ == '__main__':
    print('%-4s %-14s %-14s' % ('p', 'rank a-row', 'rank b-row'))
    for p in PRIMES:
        Ma = [[modp(a * moments(a)[1], p), modp(moments(a)[2], p)] for a in range(p)]
        Mb = [[modp(a * bmom(a)[0], p), modp(bmom(a)[1], p)] for a in range(p)]
        print('%-4d %-14d %-14d' % (p, rank_fp(Ma, p), rank_fp(Mb, p)))
