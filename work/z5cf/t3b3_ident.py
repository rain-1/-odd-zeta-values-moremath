"""T3b, part 3: identify the rank-1 factorisations  Delta(a,r) = f(a) g(r).

For each row we extract f and g (normalised) from the digit matrix and match them
against a library of level-a / level-r sequences, mod p, for several primes.
A match must hold at EVERY prime with the SAME rational constant.
"""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import Q, P, Ph, Hs, vp

PRIMES = [7, 11, 13, 17, 19, 23]
NMAX = 360


def modp(x, p):
    a, b = x.numerator, x.denominator
    if b % p == 0:
        return None
    return a % p * pow(b % p, p - 2, p) % p


DEFECTS = {
    'Qrow  (Q_n - Q_a Q_r)/p':
        lambda p, a, r, n: (Q(n) - Q(a) * Q(r)) / p,
    'w3    p^3 Phat_n - Phat_a Q_r':
        lambda p, a, r, n: F(p) ** 3 * Ph(n) - Ph(a) * Q(r),
    'w5    (p^5 P_n - P_a Q_r)/p':
        lambda p, a, r, n: (F(p) ** 5 * P(n) - P(a) * Q(r)) / p,
}

# ---- libraries of candidate factors -------------------------------------
def libA(p, a):
    """level-a candidates (p-integral)"""
    d = {'Q_a': Q(a), 'P_a': P(a), 'pPhat_a': p * Ph(a), 'a*Q_a': a * Q(a),
         'a': F(a), 'one': F(1),
         'Q_a*H1a': Q(a) * Hs(a, 1), 'Q_a*H2a': Q(a) * Hs(a, 2),
         'Q_a*H3a': Q(a) * Hs(a, 3), 'Q_a*H5a': Q(a) * Hs(a, 5),
         'Phat_a-int': (Ph(a) if vp(Ph(a), p) >= 0 else None)}
    return d


def libR(p, r):
    d = {'Q_r': Q(r), 'P_r': P(r), 'pPhat_r': p * Ph(r), 'r*Q_r': r * Q(r),
         'r': F(r), 'one': F(1),
         'Q_r*H1r': Q(r) * Hs(r, 1), 'Q_r*H2r': Q(r) * Hs(r, 2),
         'Q_r*H3r': Q(r) * Hs(r, 3), 'Q_r*H5r': Q(r) * Hs(r, 5),
         'Phat_r': Ph(r)}
    return d


def extract(p, fn):
    """return (A list, R list, f vector, g vector) with Delta(a,r)=f(a)g(r) mod p"""
    A = [a for a in range(1, p) if a * p + p - 1 <= NMAX]
    if not A:
        A = [a for a in range(1, p) if a * p <= NMAX]
    R = list(range(0, p))
    M = {}
    for a in A:
        for r in R:
            n = a * p + r
            if n > NMAX:
                return None
            v = fn(p, a, r, n)
            m = modp(v, p)
            if m is None:
                return None
            M[(a, r)] = m
    # find a pivot cell
    piv = None
    for a in A:
        for r in R:
            if M[(a, r)]:
                piv = (a, r); break
        if piv:
            break
    if piv is None:
        return None
    a0, r0 = piv
    g = {r: M[(a0, r)] for r in R}                       # g scaled so g = Delta(a0,.)
    inv = pow(M[(a0, r0)], p - 2, p)
    f = {a: M[(a, r0)] * inv % p for a in A}             # f(a0) = 1
    # check rank 1
    for a in A:
        for r in R:
            if (f[a] * g[r] - M[(a, r)]) % p:
                return 'NOTRANK1'
    return A, R, f, g


print('=' * 78)
for name, fn in DEFECTS.items():
    print('\n### %s' % name)
    for side in ('f(a)', 'g(r)'):
        print('  matching %s:' % side)
        hits = {}
        for p in PRIMES:
            e = extract(p, fn)
            if e is None or e == 'NOTRANK1':
                print('    p=%d : %s' % (p, e)); continue
            A, R, f, g = e
            lib = {}
            if side == 'f(a)':
                for a in A:
                    for k, v in libA(p, a).items():
                        lib.setdefault(k, {})[a] = v
                vec, dom = f, A
            else:
                for r in R:
                    for k, v in libR(p, r).items():
                        lib.setdefault(k, {})[r] = v
                vec, dom = g, R
            for k, tab in lib.items():
                ratios = set()
                ok = True
                for x in dom:
                    cv = tab.get(x)
                    if cv is None:
                        ok = False; break
                    cm = modp(cv, p)
                    if cm is None:
                        ok = False; break
                    if cm == 0:
                        if vec[x] % p:
                            ok = False; break
                        continue
                    ratios.add(vec[x] * pow(cm, p - 2, p) % p)
                if ok and len(ratios) == 1:
                    hits.setdefault(k, []).append((p, ratios.pop()))
        for k, v in sorted(hits.items()):
            if len(v) == len(PRIMES):
                print('    %-12s MATCHES at all primes; ratios %s' % (k, [x[1] for x in v]))
        for k, v in sorted(hits.items()):
            if len(v) != len(PRIMES):
                print('    %-12s matches only at %s' % (k, [x[0] for x in v]))
