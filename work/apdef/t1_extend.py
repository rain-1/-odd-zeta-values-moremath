"""Extend the range of the four T1 headline claims to p <= 47 (13 primes).

 (1) first-order defect rank 1, both rows
 (2) first-order law  E = 2 a b_a U_r,  e = 2 a a_a U_r  (mod p)
 (3) second-order defect rank 1, both rows, scalar with a-side factor a^2
 (4) scalar law  (a_n, p^3 b_n) = (a_a,b_a) Adig(p,r;pa)|_{eps^2}  floor exactly 3
 (5) third-order split: rank(D3a)=2, rank(D3b)=3, rank(D3b - a_a b_r)=2
"""
from fractions import Fraction as F
from core import av, bv, A, Hs, vp, modp, rank_fp, rref_fp, BIG
from dseries import Adig_at, Adig

PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

_U = {}
def U(r):
    if r not in _U:
        _U[r] = sum((A(r, s) * (Hs(r + s, 1) - Hs(r - s, 1))
                     for s in range(r + 1)), F(0))
    return _U[r]

print('%-5s %6s %6s %6s %6s %6s %8s %6s %6s %6s %6s' %
      ('p', 'rk1a', 'rk1b', 'law', 'rk2a', 'rk2b', 'scalar', 'fl_a', 'fl_b',
       'rk3a', 'rk3b'))
for p in PRIMES:
    M1a, M1b, M2a, M2b, M3a, M3b, M3c = [], [], [], [], [], [], []
    lawfail = 0
    fla = flb = BIG
    a2ok = True
    for a in range(1, p):
        r1a, r1b, r2a, r2b, r3a, r3b, r3c = [], [], [], [], [], [], []
        for r in range(p):
            n = a * p + r
            u1 = av(r) + 2 * p * a * U(r)
            u2 = Adig_at(p, r, F(p * a), 4, order=2)
            e1 = (av(n) - av(a) * av(r)) // p
            E1 = modp((F(p) ** 3 * bv(n) - bv(a) * av(r)) / p, p)
            r1a.append(e1 % p); r1b.append(E1)
            if (e1 - 2 * a * av(a) * modp(U(r), p)) % p:
                lawfail += 1
            if (E1 - 2 * a * modp(bv(a) * U(r), p)) % p:
                lawfail += 1
            r2a.append(modp((av(n) - av(a) * u1) / p ** 2, p))
            r2b.append(modp((F(p) ** 3 * bv(n) - bv(a) * u1) / p ** 2, p))
            da = av(n) - av(a) * u2
            db = F(p) ** 3 * bv(n) - bv(a) * u2
            fla = min(fla, vp(da, p)); flb = min(flb, vp(db, p))
            r3a.append(modp(da / p ** 3, p)); r3b.append(modp(db / p ** 3, p))
            r3c.append((modp(db / p ** 3, p) - av(a) % p * modp(bv(r), p)) % p)
        M1a.append(r1a); M1b.append(r1b); M2a.append(r2a); M2b.append(r2b)
        M3a.append(r3a); M3b.append(r3b); M3c.append(r3c)
    # scalarity of the 2nd order correction: a-side factor exactly a^2 * row
    for M, row in ((M2a, av), (M2b, bv)):
        piv = next((r for r in range(p) if any(M[a - 1][r] for a in range(1, p))), None)
        rat = set()
        for a in range(1, p):
            R = a * a % p * (modp(row(a), p)) % p
            if R == 0:
                if M[a - 1][piv]:
                    a2ok = False
                continue
            rat.add(M[a - 1][piv] * pow(R, -1, p) % p)
        if len(rat) > 1:
            a2ok = False
    print('%-5d %6d %6d %6d %6d %6d %8s %6s %6s %6d %6d'
          % (p, rank_fp(M1a, p), rank_fp(M1b, p), lawfail,
             rank_fp(M2a, p), rank_fp(M2b, p), 'a^2 OK' if a2ok else 'FAIL',
             fla, flb, rank_fp(M3a, p),
             '%d/%d' % (rank_fp(M3b, p), rank_fp(M3c, p))
             if False else rank_fp(M3b, p)))
    assert rank_fp(M3c, p) == 2, (p, rank_fp(M3c, p))
    st = rank_fp(M3a + M3c, p)
    assert st == 2, (p, st)
print('\n  rank(D3b - a_a b_r) = 2 and it shares the a-row r-space: asserted, all p')
