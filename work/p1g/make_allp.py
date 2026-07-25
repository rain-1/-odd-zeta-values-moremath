"""P1g: CRT-combine two representatives with DISJOINT bad primes into one that is
p-integral for every p >= 5 (the PHASE2_FINAL §2.4 construction).

  x = x1 + t*(x2 - x1),   t = 1 mod P1^{e1+1},  t = 0 mod P2^{e2+1}.

Usage: python3 make_allp.py A.json B.json OUT.json
"""
import sys, json
from fractions import Fraction as F
from sympy import factorint


def load(fn):
    return {k: F(v[0], v[1]) for k, v in json.load(open(fn)).items()}


def bad(x):
    out = {}
    for v in x.values():
        for p, e in factorint(v.denominator).items():
            if p >= 5:
                out[p] = max(out.get(p, 0), e)
    return out


A, B = load(sys.argv[1]), load(sys.argv[2])
bA, bB = bad(A), bad(B)
print('bad primes: %s = %s ; %s = %s' % (sys.argv[1], bA, sys.argv[2], bB), flush=True)
if set(bA) & set(bB):
    sys.exit('bad prime sets are NOT disjoint -- pick another pivot order')
M1 = 1
for p, e in bA.items():
    M1 *= p ** (e + 1)
M2 = 1
for p, e in bB.items():
    M2 *= p ** (e + 1)
t = 0 if M1 == 1 else pow(M2, -1, M1) * M2 % (M1 * M2)   # t = 1 mod M1, 0 mod M2
assert (M1 == 1 or t % M1 == 1) and (M2 == 1 or t % M2 == 0)
keys = set(A) | set(B)
X = {k: A.get(k, F(0)) + t * (B.get(k, F(0)) - A.get(k, F(0))) for k in keys}
X = {k: v for k, v in X.items() if v != 0}
print('t = %d ; combined has %d terms ; bad primes now: %s' % (t, len(X), bad(X)), flush=True)
json.dump({k: [v.numerator, v.denominator] for k, v in X.items()}, open(sys.argv[3], 'w'))
print('wrote %s' % sys.argv[3], flush=True)
