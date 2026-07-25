"""Symbolic K_j at level M=1: K_j as a form in the LEVEL-0 parts of the letters.

Letter X_m at level a (a<p), cell (b,c):   X_m = X_m^(0) + rho(X;pi) * u^m,
   rho(A_m(b)) = alpha, rho(A_m(c)) = gamma, rho(B_*) = rho(N_*) = 0,
   rho(C_m)    = kappa * theta^{-m}.
So v5 = sum_j K_j u^j with K_j a polynomial in the symbols X^(0).
"""
import sys, json
from fractions import Fraction as F
from collections import defaultdict

W5DIR = '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/'


def load(fn=W5DIR + 'w5_allp.json'):
    d = json.load(open(fn))
    terms = []
    for lab, (num, den) in d.items():
        fg, rest = lab.split(']x')
        f, g = fg[1:].split('|')
        h, s = rest.split('x')
        sp = lambda x: [] if x == '1' else x.split('*')
        terms.append((F(num, den), sp(f), sp(g), sp(h), sp(s)))
    return terms


def pmul(P, Q):
    R = defaultdict(F)
    for (u1, s1), c1 in P.items():
        for (u2, s2), c2 in Q.items():
            R[(u1 + u2, tuple(sorted(s1 + s2)))] += c1 * c2
    return {k: v for k, v in R.items() if v}


ONE = {(0, ()): F(1)}


def letter(name, slot, pat):
    alpha, gamma, kappa, theta = pat
    t, r = name[0], int(name[1])
    if t == 'A':
        res = alpha if slot == 'k' else gamma
        P = {(0, (('A', r, slot),)): F(1)}
        if res:
            P[(r, ())] = F(res)
        return P
    if t == 'B':
        return {(0, (('B', r, slot),)): F(1)}
    if t == 'C':
        P = {(0, (('C', r),)): F(1)}
        if kappa:
            P[(r, ())] = F(1, theta ** r)
        return P
    if t == 'N':
        return {(0, (('N', r),)): F(1)}
    raise ValueError(name)


def kforms(pat, terms=None):
    """returns {j: {symbol-multiset: coeff}} for v5 = sum_j K_j u^j."""
    terms = terms or load()
    tot = defaultdict(F)
    for cf, f, g, h, s in terms:
        base = {(0, ()): cf}
        for nm in h:
            base = pmul(base, letter(nm, None, pat))
        for nm in s:
            base = pmul(base, letter(nm, None, pat))

        def side(fm, gm):
            P = ONE
            for nm in fm:
                P = pmul(P, letter(nm, 'k', pat))
            for nm in gm:
                P = pmul(P, letter(nm, 'l', pat))
            return P
        acc = defaultdict(F)
        for k, v in side(f, g).items():
            acc[k] += v
        if f != g:
            for k, v in side(g, f).items():
                acc[k] += v
        acc = pmul({k: v for k, v in acc.items() if v}, base)
        for k, v in acc.items():
            tot[k] += v
    tot[(0, (('N', 5),))] -= F(1)
    out = defaultdict(dict)
    for (j, sym), v in tot.items():
        if v:
            out[j][sym] = v
    return dict(out)


PATS = [(0, 0, 0, 1), (0, 0, 1, 1), (1, 0, 1, 1), (0, 1, 1, 1),
        (1, 1, 0, 1), (1, 1, 1, 1), (1, 1, 1, 2)]

if __name__ == '__main__':
    terms = load(sys.argv[1] if len(sys.argv) > 1 else W5DIR + 'w5_allp.json')
    for pat in PATS:
        K = kforms(pat, terms)
        print('pattern', pat, ' s =', pat[0] + pat[1] + pat[2])
        for j in sorted(K):
            print('    K_%d : %d monomials' % (j, len(K[j])))
