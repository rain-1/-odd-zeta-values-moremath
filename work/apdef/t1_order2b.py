"""Identify the rank-1 SECOND-order defect  D2 = f(a) g(r).

(1) is it SCALAR, i.e. f_b(a)/f_a(a) = b_a/a_a ?  (then one scalar u(a,r) serves
    both rows to depth 3)
(2) what is f(a)/a_a ?          candidates 1, a, a^2, a^3, ...
(3) what is g(r) ?              fit in a basis of level-r functionals, demanding
    the SAME rational coefficients at every prime.
"""
from fractions import Fraction as F
from core import av, bv, A, Hs, vp, modp, rank_fp, BIG
from series import Adef

PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31]

_U = {}
def U(r):
    if r not in _U:
        _U[r] = sum((A(r, s) * (Hs(r + s, 1) - Hs(r - s, 1))
                     for s in range(r + 1)), F(0))
    return _U[r]


def kappa(p, r):
    """carry functional: sum over the region r+s>=p, which is 0 mod p^2"""
    t = sum(A(r, s) for s in range(r + 1) if r + s >= p)
    assert t % p ** 2 == 0
    return F(t, p ** 2)


def D2(p, row):
    M = {}
    for a in range(1, p):
        for r in range(p):
            n = a * p + r
            u = av(r) + 2 * p * a * U(r)
            d = (av(n) - av(a) * u) if row == 'a' else (F(p) ** 3 * bv(n) - bv(a) * u)
            M[(a, r)] = modp(d / p ** 2, p)
    return M


def factor(p, M):
    """rank-1 factorisation M(a,r)=f(a)g(r), normalised g(r0)=1 at a pivot"""
    piv = next(((a, r) for a in range(1, p) for r in range(p) if M[(a, r)]), None)
    if piv is None:
        return None
    a0, r0 = piv
    inv = pow(M[(a0, r0)], -1, p)
    g = {r: M[(a0, r)] * inv % p for r in range(p)}          # g(r0)=1
    f = {a: M[(a, r0)] for a in range(1, p)}                 # f(a0)=M(a0,r0)
    for a in range(1, p):
        for r in range(p):
            if (f[a] * g[r] - M[(a, r)]) % p:
                return 'NOTRANK1'
    return f, g


print('=' * 78)
print('(1) SCALARITY of the second-order correction')
print('=' * 78)
for p in PRIMES:
    fa, ga = factor(p, D2(p, 'a'))
    fb, gb = factor(p, D2(p, 'b'))
    # g's are normalised at possibly different pivots; compare up to scalar
    ok_g = rank_fp([[ga[r] for r in range(p)], [gb[r] for r in range(p)]], p) == 1
    # scalarity: f_b(a) * a_a == c * f_a(a) * b_a  for one constant c
    rat = set()
    good = True
    for a in range(1, p):
        L = fb[a] * av(a) % p
        R = fa[a] * modp(bv(a), p) % p
        if R == 0:
            if L:
                good = False
            continue
        rat.add(L * pow(R, -1, p) % p)
    print(' p=%-3d g_a ~ g_b : %-5s   f_b*a_a ~ f_a*b_a : %-5s  (ratios %s)'
          % (p, ok_g, good and len(rat) <= 1, sorted(rat)))

print('\n' + '=' * 78)
print('(2) the level-a factor  phi(a) = f(a)/a_a  -- is it proportional to a^j ?')
print('=' * 78)
for p in PRIMES:
    fa, ga = factor(p, D2(p, 'a'))
    line = []
    for j in range(4):
        rat = set(); good = True
        for a in range(1, p):
            L = fa[a]
            R = pow(a, j, p) * av(a) % p
            if R == 0:
                if L:
                    good = False
                continue
            rat.add(L * pow(R, -1, p) % p)
        line.append('a^%d:%s' % (j, ('YES c=%d' % rat.pop()) if good and len(rat) == 1
                                 else 'no'))
    print(' p=%-3d %s' % (p, '   '.join(line)))
