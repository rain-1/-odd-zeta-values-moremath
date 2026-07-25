"""P1g: verification battery for a PARTIAL cell-wise representative.

Usage: python3 verify_partial.py FILE.json EXEMPT V1MAX [primes...]
  EXEMPT = III   (cells outside region III must be cell-wise p-integral)
         = I     (cells outside regions I and II must be)

Checks
  (V1) exact-Q ladder identity  P_n = sum_{k,l} T(n,k,l) w5(n,k,l),  n = 1..V1MAX
  (V2) cell-wise  v_p( T(n,k,l) * (w5 - H^(5)_n) ) >= 0  for every NON-exempt cell
  (V3) the reduction: v_p(P_n) >= 0  <=>  v_p( sum over EXEMPT cells of T*v5 ) >= 0
  (V4) coefficient denominators (bad primes)
"""
import sys, json
from fractions import Fraction as F
from math import comb
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import P, Hs, vp
from rw5eval import load, w5, Tl

FN = sys.argv[1]
EXEMPT = sys.argv[2]
V1MAX = int(sys.argv[3])
PRIMES = [int(x) for x in sys.argv[4:]] or [5, 7, 11, 13, 17]
terms = load(FN)
d = json.load(open(FN))
bad = sorted({p for _, de in d.values() for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
              if de % p == 0} - {2, 3})
dens = set()
for _, de in d.values():
    x = de
    for p in (2, 3):
        while x % p == 0:
            x //= p
    if x != 1:
        dens.add(x)
print('%s : %d terms ; denominator primes beyond {2,3}: %s' % (FN, len(terms), sorted(dens)),
      flush=True)


def pattern(n, k, l, p):
    al = 1 if n + k >= p else 0
    ga = 1 if n + l >= p else 0
    eps = (k + l) // p
    ka = 1 if n + k + l >= (eps + 1) * p else 0
    return (al, ga, ka, eps + 1 if ka else 1)


EX = {'III': [(1, 1, 0, 1)], 'I': [(0, 1, 1, 1), (1, 0, 1, 1)]}[EXEMPT]

print('--- (V1) exact ladder identity ---', flush=True)
bad1 = 0
for n in range(1, V1MAX + 1):
    tot = F(0)
    for k in range(n + 1):
        tk = comb(n + k, n) * comb(n, k) ** 2
        for l in range(n + 1):
            tot += tk * comb(n + l, n) * comb(n, l) ** 2 * comb(n + k + l, n) * w5(n, k, l, terms)
    if tot != P(n):
        bad1 += 1
        print('   n=%d MISMATCH' % n, flush=True)
print('   n=1..%d : %d mismatches' % (V1MAX, bad1), flush=True)

print('--- (V2)/(V3) cell-wise outside region(s) %s ---' % EXEMPT, flush=True)
bad2 = bad3 = 0
for p in PRIMES:
    if any(de % p == 0 for _, de in d.values()):
        print('   p=%2d SKIPPED (p divides a coefficient denominator)' % p, flush=True)
        continue
    viol = 0; ncell = 0; nex = 0; worst = None
    for n in range(1, p):
        S_ex = F(0); S_out = F(0)
        for k in range(n + 1):
            for l in range(n + 1):
                ncell += 1
                T = Tl(n, k, l)
                v5 = w5(n, k, l, terms) - Hs(n, 5)
                x = T * v5
                if pattern(n, k, l, p) in EX:
                    nex += 1
                    S_ex += x
                else:
                    S_out += x
                    if x and vp(x, p) < 0:
                        viol += 1
                        if worst is None:
                            worst = (n, k, l, vp(T, p), vp(x, p))
        # the reduction
        vtot = vp(P(n), p) if P(n) else 99
        vex = vp(S_ex, p) if S_ex else 99
        vout = vp(S_out, p) if S_out else 99
        if vout < 0:
            bad3 += 1
        if min(vex, 0) != min(vtot, 0) and not (vex >= 0 and vtot >= 0):
            bad3 += 1
            print('   p=%d n=%d reduction mismatch: v(P)=%d v(S_III)=%d' % (p, n, vtot, vex),
                  flush=True)
    bad2 += viol
    print('   p=%2d cells=%5d (exempt %4d)  non-exempt cell-wise violations=%d %s'
          % (p, ncell, nex, viol, worst or ''), flush=True)
print('VERDICT: V1=%d  V2=%d  V3=%d  ->  %s'
      % (bad1, bad2, bad3, 'ALL CLEAN' if bad1 + bad2 + bad3 == 0 else 'FAILURES'), flush=True)
