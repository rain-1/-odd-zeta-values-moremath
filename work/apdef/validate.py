"""Instrument validation on the KNOWN answers before any new computation.

 (V1) recurrence ladders == direct sums,           n <= 40
 (V2) Theorem 2  p^3 b_{ap+r} = b_a a_r  (mod p),  p = 5..23, all a,r<p
 (V3) master form v_p(p^3 b_n a_q - b_q a_n) >= 3, floor exactly 3
 (V4) Lucas for a_n:  a_{ap+r} = a_a a_r (mod p)
"""
from fractions import Fraction as F
from core import av, bv, a_direct, b_direct, vp, modp, BIG

PRIMES = [5, 7, 11, 13, 17, 19, 23]

print('== V1: ladders vs direct sums, n<=40 ==')
bad = 0
for n in range(41):
    if av(n) != a_direct(n):
        print('  a mismatch n=%d' % n); bad += 1
    if bv(n) != b_direct(n):
        print('  b mismatch n=%d' % n); bad += 1
print('   a_0..a_5 =', [av(n) for n in range(6)])
print('   b_0..b_5 =', [str(bv(n)) for n in range(6)])
print('   mismatches:', bad)

print('\n== V2: Theorem 2, p^3 b_{ap+r} = b_a a_r mod p ==')
for p in PRIMES:
    fails = 0
    minv = BIG
    for a in range(p):
        for r in range(p):
            n = a * p + r
            d = F(p) ** 3 * bv(n) - bv(a) * av(r)
            v = vp(d, p)
            if v < 1:
                fails += 1
            if a >= 1:
                minv = min(minv, v)
    print('   p=%-3d fails=%d   min v_p over a>=1: %s' % (p, fails, minv))

print('\n== V3: master form floor, v_p(p^3 b_n a_q - b_q a_n), q=n//p ==')
for p in PRIMES:
    mn = BIG
    for n in range(1, p * p):
        q = n // p
        d = F(p) ** 3 * bv(n) * av(q) - bv(q) * av(n)
        mn = min(mn, vp(d, p))
    print('   p=%-3d floor=%s' % (p, mn))

print('\n== V4: Lucas for a_n mod p, and depth ==')
for p in PRIMES:
    mn = BIG
    for a in range(1, p):
        for r in range(p):
            d = av(a * p + r) - av(a) * av(r)
            mn = min(mn, vp(d, p))
    print('   p=%-3d floor of a_{ap+r}-a_a a_r = %s' % (p, mn))
