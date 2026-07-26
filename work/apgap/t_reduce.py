"""TEST 2: the two statements the gap reduces to.

From t_regions.py (0 failures, 7 primes, all cells):

  D2(a,r) == a^2 m0 Sa2 + a m1 Sac + m2 Scc + (a^2 m0 - 2 a m1 + m2) Xi   (mod p)

and the target law is D2 == a^2 m0 X_p(r) with X_p(r) = Sa2 + Xi.  Subtracting:

  a m1 (Sac - 2 Xi) + m2 (Scc + Xi) == 0                                  (*)

Sufficient (and, if (a m1)_a and (m2)_a are independent mod p, necessary):

  R1:  Sac(r) + 2 Scc(r) = 0          -- candidate RATIONAL identity in r
  R2:  Scc(r) + Xi_p(r) == 0 (mod p)  -- the genuine congruence

(R1 & R2 give Sac - 2Xi = -2Scc - 2Xi == 0 and Scc + Xi == 0.)
"""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/apdef')
from fractions import Fraction as F
from core import modp
from gap_core import sigmas, Xi

PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

if __name__ == '__main__':
    print('=== R1:  Sac(r) + 2 Scc(r) = 0  over QQ ===')
    bad1 = [r for r in range(41) if sigmas(r)[1] + 2 * sigmas(r)[2] != 0]
    print('r = 0..40  failures:', bad1 if bad1 else 'NONE')
    print('  sample Sac :', [sigmas(r)[1] for r in range(5)])
    print('  sample Scc :', [sigmas(r)[2] for r in range(5)])
    print('  sample Sa2 :', [sigmas(r)[0] for r in range(5)])

    print('\n=== R2:  Scc(r) + Xi_p(r) == 0 (mod p) ===')
    tot = badn = 0
    for p in PRIMES:
        bad = [r for r in range(p) if modp(sigmas(r)[2] + Xi(p, r), p) != 0]
        tot += p; badn += len(bad)
        print('p=%-3d cells %-3d failures: %s' % (p, p, bad if bad else 'NONE'))
    print('total cells %d, failures %d' % (tot, badn))
