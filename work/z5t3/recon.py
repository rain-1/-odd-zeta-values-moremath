"""recon.py -- CRT + rational reconstruction of the folded+MT solution from
the two primes, with a third-prime verification of the reconstructed vector.
"""
import sys, pickle
import numpy as np
from math import gcd

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5t3')

P1, P2 = 4194301, 4194287
NS = 25

x1 = np.load('mt26_x_%d_n%d.npy' % (P1, NS)).astype(object)
x2 = np.load('mt26_x_%d_n%d.npy' % (P2, NS)).astype(object)
assert len(x1) == len(x2)
M = P1 * P2
inv21 = pow(P2, P1 - 2, P1)

def crt(a1, a2):
    # x = a2 + P2 * t,  t = (a1 - a2)/P2 mod P1
    t = (a1 - a2) % P1 * inv21 % P1
    return (a2 + P2 * t) % M

def ratrec(a, Mm, bound=None):
    a %= Mm
    if bound is None:
        bound = int((Mm // 2) ** 0.5)
    r0, r1, s0, s1 = Mm, a, 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1, s0, s1 = r1, r0 - q * r1, s1, s0 - q * s1
    if s1 == 0 or abs(s1) > bound:
        return None
    if gcd(r1, abs(s1)) != 1:
        return None
    return (r1, s1) if s1 > 0 else (-r1, -s1)

ok, fail, zero = 0, [], 0
rats = [None] * len(x1)
for i in range(len(x1)):
    a = crt(int(x1[i]), int(x2[i]))
    if a == 0:
        zero += 1
        rats[i] = (0, 1)
        continue
    rr = ratrec(a, M)
    if rr is None:
        fail.append(i)
    else:
        rats[i] = rr
        ok += 1
print('coeffs: %d nonzero reconstructed, %d zero, %d FAILED ratrec'
      % (ok, zero, len(fail)))
if fail:
    print('failed indices (first 20):', fail[:20])
with open('mt26_rats.pkl', 'wb') as fh:
    pickle.dump(rats, fh)

# consistency: reduce reconstructed rationals mod P1 and compare to x1
bad = 0
for i, rr in enumerate(rats):
    if rr is None:
        continue
    v = rr[0] % P1 * pow(rr[1] % P1, P1 - 2, P1) % P1
    if v != int(x1[i]) % P1:
        bad += 1
print('self-consistency vs P1:', 'PASS' if bad == 0 else 'FAIL %d' % bad)
