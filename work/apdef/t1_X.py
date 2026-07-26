"""Pin down  X_p(r)  in    a_n = a_a [ a_r + 2pa U_r + p^2 a^2 X_p(r) ]  mod p^3.

X_p(r) := D2(a,r) / (a^2 a_a) mod p   (independent of a -- checked).
Fit X_p against candidate level-r functionals with p-INDEPENDENT rational
coefficients.
"""
from fractions import Fraction as F
from core import av, bv, A, Hs, vp, modp, rank_fp, rref_fp, BIG
from series import Adef

PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31]

_c = {}
def sums(r):
    """assorted level-r functionals"""
    if r in _c:
        return _c[r]
    U = P2 = Q2 = F(0)
    for s in range(r + 1):
        Ars = A(r, s)
        d1 = Hs(r + s, 1) - Hs(r - s, 1)
        d2 = Hs(r - s, 2) - Hs(r + s, 2)
        U += Ars * d1
        P2 += Ars * d1 ** 2
        Q2 += Ars * d2
    _c[r] = (U, P2, Q2)
    return _c[r]


def kappa(p, r):
    t = sum(A(r, s) for s in range(r + 1) if r + s >= p)
    assert t % p ** 2 == 0
    return F(t, p ** 2)


def Xp(p):
    """X_p(r) for r = 0..p-1, plus a consistency check over a"""
    U = {r: sums(r)[0] for r in range(p)}
    out = {}
    for r in range(p):
        vals = set()
        for a in range(1, p):
            if av(a) % p == 0:
                continue
            n = a * p + r
            u = av(r) + 2 * p * a * U[r]
            d = (av(n) - av(a) * u) / p ** 2
            m = modp(d, p)
            vals.add(m * pow(a * a % p * (av(a) % p) % p, -1, p) % p)
        assert len(vals) == 1, (p, r, vals)
        out[r] = vals.pop()
    return out


print('=' * 78)
print('X_p(r)  (the second-order level-r factor), and candidate fits')
print('=' * 78)
BASIS = ['c2', 'kappa', 'a_r', 'U_r', 'P2', 'Q2', 'one']
sols = {}
for p in PRIMES:
    X = Xp(p)
    cols = []
    for r in range(p):
        U, P2, Q2 = sums(r)
        c2 = Adef(r, 4)[2]
        cols.append([modp(c2, p), modp(kappa(p, r), p), av(r) % p,
                     modp(U, p), modp(P2, p), modp(Q2, p), 1])
    # solve  cols . x = X   over F_p   (least-structure: full solution space)
    Maug = [cols[r] + [X[r]] for r in range(p)]
    R, piv = rref_fp(Maug, p)
    ncol = len(BASIS)
    inconsistent = any(pc == ncol for pc in piv)
    print(' p=%-3d rank(A)=%d rank(A|b)=%d  %s'
          % (p, rank_fp([c[:ncol] for c in cols], p), len(R),
             'INCONSISTENT' if inconsistent else 'consistent'))
    if not inconsistent:
        # particular solution
        sol = [0] * ncol
        for row, pc in zip(R, piv):
            sol[pc] = row[ncol]
        sols[p] = sol
        print('       particular sol %s   free cols %s'
              % ({BASIS[i]: sol[i] for i in range(ncol) if sol[i]},
                 [BASIS[i] for i in range(ncol) if i not in piv]))

print('\n--- X_p(r) tables ---')
for p in (5, 7, 11, 13):
    X = Xp(p)
    print(' p=%-3d %s' % (p, ' '.join('%3d' % X[r] for r in range(p))))
print('\n--- candidate columns at p=11 (for eyeballing) ---')
for name, i in zip(BASIS, range(len(BASIS))):
    p = 11
    row = []
    for r in range(p):
        U, P2, Q2 = sums(r)
        c2 = Adef(r, 4)[2]
        v = [modp(c2, p), modp(kappa(p, r), p), av(r) % p, modp(U, p),
             modp(P2, p), modp(Q2, p), 1][i]
        row.append(v)
    print('  %-6s %s' % (name, ' '.join('%3d' % x for x in row)))
