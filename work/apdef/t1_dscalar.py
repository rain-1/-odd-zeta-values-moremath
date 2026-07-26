"""THE TWO-LEVEL SCALAR LAW, digit-deformed version.

    ( a_{ap+r} , p^3 b_{ap+r} )  =  ( a_a , b_a ) * Adig(p, r; p a)  mod p^{?}

Adig truncated at eps^m.  Report the floor for m = 0..M.
Also: check X_p(r) = [eps^2] Adig  exactly (mod p).
"""
from fractions import Fraction as F
from core import av, bv, A, Hs, vp, modp, BIG
from dseries import Adig, Adig_at

PRIMES = [5, 7, 11, 13, 17, 19, 23]
MMAX = 6

print('=' * 78)
print('CHECK: X_p(r) == [eps^2] Adig(p,r)  mod p ?')
print('=' * 78)
_U = {}
def U(r):
    if r not in _U:
        _U[r] = sum((A(r, s) * (Hs(r + s, 1) - Hs(r - s, 1))
                     for s in range(r + 1)), F(0))
    return _U[r]

for p in PRIMES:
    ok = True
    for r in range(p):
        c = Adig(p, r, 2)
        # c1 must be 2 U_r
        if c[1] != 2 * U(r):
            ok = False; print('  p=%d r=%d  c1 != 2U_r' % (p, r))
        vals = set()
        for a in range(1, p):
            if av(a) % p == 0:
                continue
            n = a * p + r
            u = av(r) + 2 * p * a * U(r)
            d = (av(n) - av(a) * u) / p ** 2
            vals.add(modp(d, p) * pow(a * a % p * (av(a) % p) % p, -1, p) % p)
        X = vals.pop() if len(vals) == 1 else None
        if X is None or (X - modp(c[2], p)) % p:
            ok = False
            print('  p=%d r=%d  X=%s  [eps^2]Adig=%s' % (p, r, X, modp(c[2], p)))
    print('  p=%-3d  %s' % (p, 'MATCHES for all r' if ok else 'mismatch'))

print('\n' + '=' * 78)
print('DEPTH:  floor of v_p( X_n - X_a * Adig(p,r; pa) )  truncated at eps^m')
print('=' * 78)
print('%-5s %-6s %s' % ('p', 'row', '  '.join('m=%d' % m for m in range(MMAX + 1))))
for p in PRIMES:
    for tag in ('a', 'b'):
        fl = []
        for m in range(MMAX + 1):
            mn = BIG
            for a in range(1, p):
                for r in range(p):
                    n = a * p + r
                    u = Adig_at(p, r, F(p * a), MMAX, order=m)
                    d = (av(n) - av(a) * u) if tag == 'a' else (F(p) ** 3 * bv(n) - bv(a) * u)
                    mn = min(mn, vp(d, p))
            fl.append(mn)
        print('%-5d %-6s %s' % (p, tag, '  '.join('%3s' % ('inf' if f >= BIG else f)
                                                 for f in fl)))
