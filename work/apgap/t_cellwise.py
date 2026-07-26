"""Cell-by-cell check of the three regional formulas for A(ap+r, cp+s) mod p^3."""
import sys
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/apdef')
from fractions import Fraction as F
from math import factorial
from core import A, Hs, vp, modpk
from gap_core import Cfun


def Lam1(a, c, r, s):
    u = Hs(r + s, 1) - Hs(r - s, 1)
    v = Hs(r + s, 1) + Hs(r - s, 1) - 2 * Hs(s, 1)
    return a * u + c * v


def Lam2(a, c, r, s):
    return ((a + c) ** 2 * Hs(r + s, 2) - 2 * c ** 2 * Hs(s, 2)
            - (a - c) ** 2 * Hs(r - s, 2))


def region1(p, a, c, r, s):
    L1 = Lam1(a, c, r, s); L2 = Lam2(a, c, r, s)
    return A(a, c) * A(r, s) * (1 + 2 * p * L1 + p * p * (2 * L1 * L1 - L2))


def region2a(p, a, c, r, s):
    rho = r + s - p
    D = F(factorial(rho), factorial(s) ** 2 * factorial(r - s)) ** 2
    return p * p * A(a, c) * (1 + a + c) ** 2 * D


def region2b(p, a, c, r, m):
    return p * p * (a - c) ** 2 * A(a, c) * Cfun(r, m)


def check(p, verbose=False):
    bad = {'I': 0, 'IIa': 0, 'IIb': 0, 'other': 0}
    tot = {'I': 0, 'IIa': 0, 'IIb': 0, 'other': 0}
    ex = []
    for a in range(p):
        for r in range(p):
            n = a * p + r
            for c in range(a + 1):
                for s in range(p):
                    k = c * p + s
                    if k > n:
                        continue
                    true = A(n, k)
                    if s <= r and r + s < p:
                        tag, pred = 'I', region1(p, a, c, r, s)
                    elif s <= r:
                        tag, pred = 'IIa', region2a(p, a, c, r, s)
                    elif s > r and 2 * r + (s - r) < p:
                        tag, pred = 'IIb', region2b(p, a, c, r, s - r)
                    else:
                        tag, pred = 'other', 0
                    tot[tag] += 1
                    if vp(F(true) - pred, p) < 3:
                        bad[tag] += 1
                        if len(ex) < 6:
                            ex.append((tag, a, c, r, s))
    return bad, tot, ex


if __name__ == '__main__':
    for p in [5, 7, 11, 13]:
        bad, tot, ex = check(p)
        print('p=%-3d  bad/total:  I %d/%d   IIa %d/%d   IIb %d/%d   other %d/%d'
              % (p, bad['I'], tot['I'], bad['IIa'], tot['IIa'],
                 bad['IIb'], tot['IIb'], bad['other'], tot['other']))
        if ex:
            print('   examples (tag,a,c,r,s):', ex)
