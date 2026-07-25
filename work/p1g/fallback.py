"""P1g E3b fallback (PHASE2_CANCEL 7.2): the recurrence route to (BASE).

For each prime p, (BASE) for n < p follows by forward induction from P_0,P_1,P_2 except at
the steps 0 <= n <= p-4 where p | c_3(n) = 2(n+3)^5(2n+5)a_0(n).  Since 1 <= n+3 <= p-1,
that means p | (2n+5)*a_0(n).  This script

  (a) enumerates the exceptional steps per prime,
  (b) measures the slack  v_p(c_0 P_n + c_1 P_{n+1} + c_2 P_{n+2}) - v_p(c_3(n))  at each,
  (c) separates the "genuine" step n0 = (p-5)/2 from the a_0-root steps, and reports
      whether the a_0-root steps are automatically satisfied (apparent singularities).
"""
import sys
from fractions import Fraction as F
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import P, Ph, vp, a0, B8, B9, c0, c1


def c2(n):
    return -2 * B9(n)


def c3(n):
    return 2 * (n + 3) ** 5 * (2 * n + 5) * a0(n)


def report(seq, name, PRIMES):
    print('--- %s ---' % name, flush=True)
    stats = {'genuine_tight': 0, 'genuine_slack': 0, 'a0_tight': 0, 'a0_slack': 0,
             'FAIL': 0}
    for p in PRIMES:
        exc = [n for n in range(0, p - 3) if c3(n) % p == 0]
        for n in exc:
            num = c0(n) * seq(n) + c1(n) * seq(n + 1) + c2(n) * seq(n + 2)
            v = vp(num, p) if num else 99
            need = vp(c3(n), p)
            kind = 'genuine' if (2 * n + 5) % p == 0 else 'a0'
            if v < need:
                stats['FAIL'] += 1
                print('   p=%3d n=%3d [%s] v_p(num)=%d < v_p(c3)=%d  -> level %d'
                      % (p, n, kind, v, need, n + 3), flush=True)
            elif v == need:
                stats[kind + '_tight'] += 1
            else:
                stats[kind + '_slack'] += 1
    print('   %s' % stats, flush=True)
    return stats


PRIMES = [p for p in range(5, 200) if all(p % d for d in range(2, int(p ** .5) + 1))]
print('primes 5..199 : %d' % len(PRIMES), flush=True)
sP = report(P, 'P-row (the (BASE) obligation)', PRIMES)
sPh = report(Ph, 'P-hat row (known to FAIL -- the control)', PRIMES)

print()
print('(REC-*) localisation: the single genuine step is n0=(p-5)/2, producing P_{(p+1)/2}.')
for p in PRIMES[:8]:
    n0 = (p - 5) // 2
    num = c0(n0) * P(n0) + c1(n0) * P(n0 + 1) + c2(n0) * P(n0 + 2)
    print('   p=%3d n0=%3d  v_p(num)=%d  v_p(c3)=%d  slack=%d  (level (p+1)/2 = %d)'
          % (p, n0, vp(num, p), vp(c3(n0), p), vp(num, p) - vp(c3(n0), p), (p + 1) // 2),
          flush=True)
