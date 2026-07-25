"""P1g E3a: the full verification battery for an R-extended representative.

  (V1) exact-Q ladder identity      P_n = sum_{k,l} T(n,k,l) w(n,k,l),  n = 1..NMAX
  (V2) depth sweep, ALL cells       d5(a,b,c) <= cap(pattern),  cap = 2 on the s=2
                                    patterns (the STRONG requirement)  -- and the
                                    cell-wise (BASE) bound  d5 <= v_pT
  (V3) (BASE) directly              v_p( sum_{k,l} T(n,k,l) w(n,k,l) ) >= 0 for n < p
  (V4) p-integrality of the coefficients

Usage: python3 e3_verify.py FILE.json [V1MAX] [primes...]
"""
import sys, json
from fractions import Fraction as F
from math import comb
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import P, Hs, vp
from rw5eval import load, w5, Tl

FN = sys.argv[1]
V1MAX = int(sys.argv[2]) if len(sys.argv) > 2 else 34
PRIMES = [int(x) for x in sys.argv[3:]] or [5, 7, 11, 13, 17]
terms = load(FN)
print('%s : %d terms' % (FN, len(terms)), flush=True)

# ---------------------------------------------------------------- (V4)
bad4 = []
for _, f, g, h, s in []:
    pass
d = json.load(open(FN))
for lab, (num, den) in d.items():
    dd = den
    for p in (2, 3):
        while dd % p == 0:
            dd //= p
    if dd != 1:
        bad4.append((lab, den))
print('--- (V4) coefficient denominators outside {2,3}: %d  %s'
      % (len(bad4), bad4[:5]), flush=True)

# ---------------------------------------------------------------- (V1)
print('--- (V1) exact ladder identity ---', flush=True)
bad1 = 0
for n in range(1, V1MAX + 1):
    tot = F(0)
    for k in range(n + 1):
        tk = comb(n + k, n) * comb(n, k) ** 2
        for l in range(n + 1):
            T = tk * comb(n + l, n) * comb(n, l) ** 2 * comb(n + k + l, n)
            tot += T * w5(n, k, l, terms)
    if tot != P(n):
        bad1 += 1
        print('   n=%d MISMATCH' % n, flush=True)
print('   n=1..%d : %d mismatches' % (V1MAX, bad1), flush=True)

# ---------------------------------------------------------------- (V2)/(V3)
print('--- (V2) depth sweep (strong cap) + (V3) (BASE) ---', flush=True)
bad2 = bad3 = 0
for p in PRIMES:
    ncell = 0; viol_strong = 0; viol_base = 0; mx = 0; slack = 99
    worstbase = None
    for a in range(1, p):
        tot = F(0)
        for b in range(a + 1):
            for c in range(a + 1):
                ncell += 1
                vT = vp(Tl(a, b, c), p)
                W = w5(a, b, c, terms) - Hs(a, 5)
                d5 = max(0, -vp(W, p)) if W else 0
                mx = max(mx, d5)
                capF = 1 + min(vT, 2)
                capS = 2 if vT == 2 else capF          # the vt2 strengthening
                slack = min(slack, capS - d5)
                if d5 > capS:
                    viol_strong += 1
                if d5 > vT:                            # cell-wise (BASE) requirement
                    viol_base += 1
                    if worstbase is None:
                        worstbase = (a, b, c, vT, d5)
                tot += Tl(a, b, c) * (W + Hs(a, 5))
        v = vp(tot, p) if tot else 99
        if v < 0:
            bad3 += 1
            print('   p=%d n=%d  v_p(sum T w) = %d  < 0' % (p, a, v), flush=True)
    bad2 += viol_strong
    print('   p=%2d cells=%5d max d5=%d  vt2-cap violations=%d  min slack=%d ;'
          '  cell-wise d5<=vT violations=%d %s'
          % (p, ncell, mx, viol_strong, slack, viol_base, worstbase or ''), flush=True)
print('   (V3) levels with v_p(P_n) < 0 : %d' % bad3, flush=True)
print('VERDICT: V1=%d V2=%d V3=%d V4=%d -> %s'
      % (bad1, bad2, bad3, len(bad4),
         'ALL CLEAN' if bad1 + bad2 + bad3 + len(bad4) == 0 else 'FAILURES'), flush=True)
