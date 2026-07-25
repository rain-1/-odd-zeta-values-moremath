"""P1g: the p-independent depth conditions in the R-extended alphabet.

Pole calculus at level a = n < p, cells 0 <= b,c <= a  (u := p^-1):

  A_r(b) = alpha * u^r + Z_p        (residue is the CONSTANT 1)
  B_r(b) = Z_p
  C_r    = kappa * theta^-r u^r + Z_p
  N_r    = Z_p
  R_r(b) = alpha * rho_{r,b} u   + Z_p   [NEW]  pole order 1 at EVERY weight r,
                                                indicator alpha, residue a Z_p SYMBOL
  D_r    = kappa * delta_r u     + Z_p   [NEW, eps = 0 only]
           (for eps = 1 the pole order of D_r is r -- so D-letters need the refined
            pattern census that carries eps; see patterns(refine_eps=True))

Treating the R/D residues as free symbols is a *strengthening* (it is sufficient for
the depth bound and costs generality only in the direction that makes the answer safe).

Conditions: for each reachable pole pattern pi with cap J(pi) and each u-power j > J,
the coefficient K_j must vanish identically in the Z_p symbols.
"""
import sys
from fractions import Fraction as F
from collections import defaultdict

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from math import comb

ONE = {(0, ()): F(1)}


def pmul(P, Q):
    R = defaultdict(F)
    for (u1, s1), c1 in P.items():
        for (u2, s2), c2 in Q.items():
            R[(u1 + u2, tuple(sorted(s1 + s2)))] += c1 * c2
    return {k: v for k, v in R.items() if v}


def letter(name, slot, pat):
    """pat = (alpha, gamma, kappa, theta[, eps])."""
    alpha, gamma, kappa, theta = pat[:4]
    eps = pat[4] if len(pat) > 4 else theta - 1
    t, r = name[0], int(name[1])
    if t == 'A':
        res = alpha if slot == 'b' else gamma
        P = {(0, (('a', r, slot),)): F(1)}
        if res:
            P[(r, ())] = F(1)
        return P
    if t == 'B':
        return {(0, (('b', r, slot),)): F(1)}
    if t == 'R':
        res = alpha if slot == 'b' else gamma
        P = {(0, (('R', r, slot),)): F(1)}
        if res:
            P[(1, (('rho', r, slot),))] = F(1)
        return P
    if t == 'C':
        P = {(0, (('c', r),)): F(1)}
        if kappa:
            P[(r, ())] = F(1, theta ** r)
        return P
    if t == 'D':
        P = {(0, (('D', r),)): F(1)}
        if eps == 0:
            if kappa:
                P[(1, (('del', r),))] = F(1)
        else:
            # eps = 1: the j = p term contributes a pole of order exactly r
            for j in range(1, r + 1):
                P[(j, (('delE', r, j),))] = F(1)
        return P
    if t == 'N':
        return {(0, (('n', r),)): F(1)}
    if t in 'YVZ':
        a, b = int(name[1]), int(name[2])
        if t == 'Z':                                   # n-slot nested: no pole
            return {(0, (('Z', a, b),)): F(1)}
        if t == 'Y':                                   # k-slot nested, indicator alpha/gamma
            res, th = (alpha if slot == 'b' else gamma), 1
            P = {(0, (('Y', a, b, slot),)): F(1)}
            key_lo, key_hi = ('ylo', b, slot), ('yhi', a, slot)
        else:                                          # V: coupling nested, indicator kappa
            res, th = kappa, theta
            P = {(0, (('V', a, b),)): F(1)}
            key_lo, key_hi = ('vlo', b), ('vhi', a)
        if res:
            # the single multiple of p in the interval is  th*p ; it is either m1 or m2
            P[(a, (key_lo,))] = P.get((a, (key_lo,)), F(0)) + F(1, th ** a)
            P[(b, (key_hi,))] = P.get((b, (key_hi,)), F(0)) + F(1, th ** b)
        return {kk: v for kk, v in P.items() if v}
    raise ValueError(name)


def elem_expansion(B, e, pat):
    i, j, ci, ni = e
    f, g = B.km[i][0], B.km[j][0]
    h, s = B.cm[ci][0], B.nm[ni][0]
    base = ONE
    for nm in h:
        base = pmul(base, letter(nm, None, pat))
    for nm in s:
        base = pmul(base, letter(nm, None, pat))

    def side(fm, gm):
        P = ONE
        for nm in fm:
            P = pmul(P, letter(nm, 'b', pat))
        for nm in gm:
            P = pmul(P, letter(nm, 'c', pat))
        return P
    tot = side(f, g)
    if f != g:
        acc = defaultdict(F)
        for k, v in tot.items():
            acc[k] += v
        for k, v in side(g, f).items():
            acc[k] += v
        tot = {k: v for k, v in acc.items() if v}
    return pmul(tot, base)


def kummer_v(a, b, c, p):
    def v(x):
        n = 0
        while x % p == 0:
            x //= p
            n += 1
        return n
    return v(comb(a + b, a)) + v(comb(a + c, a)) + v(comb(a + b + c, a))


def patterns(primes=(5, 7, 11, 13, 17, 19, 23), refine_eps=False):
    """reachable pole patterns -> Lemma-F cap 1+min(vT,2)."""
    caps = {}
    for p in primes:
        for a in range(1, p):
            for b in range(a + 1):
                for c in range(a + 1):
                    al = 1 if a + b >= p else 0
                    ga = 1 if a + c >= p else 0
                    eps = (b + c) // p
                    ka = 1 if a + b + c >= (eps + 1) * p else 0
                    th = eps + 1 if ka else 1
                    vT = kummer_v(a, b, c, p)
                    assert vT == al + ga + ka
                    key = (al, ga, ka, th) + ((eps,) if refine_eps else ())
                    caps[key] = min(caps.get(key, 99), 1 + min(vT, 2))
    return caps


def caps_for(mode, refine_eps=False):
    """mode = base | strong | vt2[:SEL] ; SEL a subset of {I,II,III} joined by '+',
    naming which s=2 patterns get the tightened cap 2:
        I = (0,1,1,1)   II = (1,0,1,1)   III = (1,1,0,1)."""
    NAME = {(0, 1, 1, 1): 'I', (1, 0, 1, 1): 'II', (1, 1, 0, 1): 'III'}
    sel = None
    if mode.startswith('vt2:'):
        sel = set(mode.split(':', 1)[1].split('+'))
        mode = 'vt2'
    base = patterns(refine_eps=refine_eps)
    out = {}
    for pat, cap in base.items():
        vT = pat[0] + pat[1] + pat[2]
        if mode == 'base':
            out[pat] = cap
        elif mode == 'vt2':
            nm = NAME.get(pat[:4])
            out[pat] = 2 if (vT == 2 and (sel is None or nm in sel)) else cap
        elif mode == 'strong':
            out[pat] = vT
        elif mode == 'exIII':
            # cell-wise cap d5 <= vT everywhere EXCEPT pattern III, left at the Lemma-F cap
            out[pat] = cap if pat[:4] == (1, 1, 0, 1) else vT
        elif mode == 'exI':
            # cell-wise cap everywhere EXCEPT patterns I and II
            out[pat] = cap if pat[:4] in ((0, 1, 1, 1), (1, 0, 1, 1)) else vT
        else:
            raise ValueError(mode)
    return out


def condition_rows(B, caps):
    """Exact-Q condition rows (list of integer lists) over the basis columns."""
    import numpy as np
    NC = len(B.els)
    rows = defaultdict(lambda: [F(0)] * NC)
    for ci, e in enumerate(B.els):
        for pat, cap in caps.items():
            for (u, sym), v in elem_expansion(B, e, pat).items():
                if u > cap:
                    rows[(pat, u, sym)][ci] += v
    C = []
    for k, vec in rows.items():
        if not any(vec):
            continue
        den = 1
        for v in vec:
            d = v.denominator
            den = den * d // np.gcd(den, d)
        iv = [int(v * den) for v in vec]
        g = 0
        for v in iv:
            g = np.gcd(g, abs(v))
        if g:
            iv = [v // int(g) for v in iv]
        C.append(iv)
    return C
