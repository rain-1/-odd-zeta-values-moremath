"""Build a single depth-minimal w5 whose coefficient denominators are supported on {2,3},
hence p-integral for EVERY prime p >= 5, out of two representatives with disjoint bad primes.

If x1, x2 lie in the (affine) depth-conditioned solution family and x1 is p-integral for all
p >= 5 except p = P1, x2 for all p >= 5 except p = P2 (P1 != P2), put d = x2 - x1 and pick an
integer t with
        t == 1  (mod P1^(e1+1)),      t == 0  (mod P2^(e2+1)),
where e_i is the largest power of P_i in a denominator of x_i.  Then x = x1 + t*d lies in the
family and is p-integral for every p >= 5:
  * p = P1:  x = x2 - (1-t) d,  v_{P1}((1-t)d) >= (e1+1) - e1 = 1;
  * p = P2:  x = x1 + t d,      v_{P2}(t d)    >= (e2+1) - e2 = 1;
  * other p >= 5: x1, d are p-integral and t is an integer.

Usage: python3 make_allp.py file1.json file2.json out.json
"""
import sys, json
from fractions import Fraction as F

f1, f2, out = sys.argv[1], sys.argv[2], sys.argv[3]
d1 = {k: F(v[0], v[1]) for k, v in json.load(open(f1)).items()}
d2 = {k: F(v[0], v[1]) for k, v in json.load(open(f2)).items()}
labs = sorted(set(d1) | set(d2))
x1 = [d1.get(k, F(0)) for k in labs]
x2 = [d2.get(k, F(0)) for k in labs]


def badprimes(x):
    S = {}
    for c in x:
        d = c.denominator
        p = 2
        while p * p <= d:
            while d % p == 0:
                d //= p
                if p >= 5:
                    S[p] = S.get(p, 0) + 0
            p += 1
        if d > 1 and d >= 5:
            S[d] = 0
    # recompute exact exponents
    E = {}
    for c in x:
        d = c.denominator
        for p in list(S):
            e = 0
            while d % p == 0:
                d //= p
                e += 1
            E[p] = max(E.get(p, 0), e)
    return E


E1, E2 = badprimes(x1), badprimes(x2)
print('%s bad primes %s' % (f1, E1))
print('%s bad primes %s' % (f2, E2))
assert len(E1) == 1 and len(E2) == 1, 'need exactly one bad prime each'
P1, e1 = list(E1.items())[0]
P2, e2 = list(E2.items())[0]
assert P1 != P2
M1, M2 = P1 ** (e1 + 1), P2 ** (e2 + 1)
# CRT: t == 1 mod M1, t == 0 mod M2
t = M2 * pow(M2 % M1, -1, M1) % (M1 * M2)
assert t % M1 == 1 % M1 and t % M2 == 0
print('t = %d   (mod %d)' % (t, M1 * M2))

x = [a + t * (b - a) for a, b in zip(x1, x2)]
dens = set()
for c in x:
    d = c.denominator
    p = 2
    while p * p <= d:
        while d % p == 0:
            d //= p
            dens.add(p)
        p += 1
    if d > 1:
        dens.add(d)
print('resulting denominator primes:', sorted(dens))
assert all(p <= 3 for p in dens), 'FAILED: still has a bad prime'
res = {k: [c.numerator, c.denominator] for k, c in zip(labs, x) if c != 0}
print('%d nonzero terms; max numerator digits %d'
      % (len(res), max(len(str(abs(v[0]))) for v in res.values())))
json.dump(res, open(out, 'w'), indent=1)
print('written', out)
