"""T4: the region functionals of (V3)_0, and the annihilator of the target.

At L=0 (n<p, q=p-n) the s=2 locus is
   I  : k<q, l>=q          (alpha,gamma,kappa)=(0,1,1)
   II : k>=q, l<q                             (1,0,1)      [mirror of I]
   III: k,l>=q, p<=k+l<p+q                    (1,1,0)
and (V3)_0 is   sum_{I} + sum_{II} + sum_{III}  of (T/p^2)*K_3^pattern  ==  0  in F_p.

Here we compute, for each region rho and each weight-2 monomial m in the LEVEL-0 letters,
    Lam(rho, m) = sum_{cells in rho} (T/p^2) * m   mod p,
so that the target is  c . V  with c = the K_3 coefficient vector (from kform.py).
"""
import sys
from fractions import Fraction as F
from math import comb
from itertools import combinations_with_replacement

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1f')
from kform import kforms

W1 = ['A1k', 'A1l', 'B1k', 'B1l', 'C1', 'N1']
W2 = ['A2k', 'A2l', 'B2k', 'B2l', 'C2', 'N2']
MONS = [tuple(sorted(t)) for t in combinations_with_replacement(W1, 2)] + [(x,) for x in W2]
MIDX = {m: i for i, m in enumerate(MONS)}
NM = len(MONS)

SWAP = {'A1k': 'A1l', 'A1l': 'A1k', 'B1k': 'B1l', 'B1l': 'B1k',
        'A2k': 'A2l', 'A2l': 'A2k', 'B2k': 'B2l', 'B2l': 'B2k',
        'C1': 'C1', 'C2': 'C2', 'N1': 'N1', 'N2': 'N2'}


def symname(s):
    """kform symbol ('A',r,'k') / ('C',r) / ('N',r) -> our monomial letter name"""
    if len(s) == 3:
        return '%s%d%s' % (s[0], s[1], s[2])
    return '%s%d' % (s[0], s[1])


def kvec(pat):
    """K_3 of pattern pat as a coefficient vector over MONS (Fractions)."""
    K = kforms(pat)
    v = [F(0)] * NM
    for sym, c in K.get(3, {}).items():
        key = tuple(sorted(symname(s) for s in sym))
        v[MIDX[key]] += c
    return v


def hsums(p, N):
    """H'^(m)_j mod p for j=0..N, m=1,2  (p-free harmonic sums)."""
    h1 = [0] * (N + 1)
    h2 = [0] * (N + 1)
    inv = [0] * (max(N, p) + 1)
    for j in range(1, max(N, p) + 1):
        if j % p:
            inv[j] = pow(j % p, -1, p)
    for j in range(1, N + 1):
        h1[j] = h1[j - 1]
        h2[j] = h2[j - 1]
        if j % p:
            h1[j] = (h1[j] + inv[j]) % p
            h2[j] = (h2[j] + inv[j] * inv[j]) % p
    return h1, h2


def regions(n, p):
    q = p - n
    I = [(k, l) for k in range(0, q) for l in range(q, n + 1)]
    II = [(k, l) for k in range(q, n + 1) for l in range(0, q)]
    III = [(k, l) for k in range(q, n + 1) for l in range(q, n + 1)
           if p <= k + l < p + q]
    return I, II, III


def Vvec(n, p, h1, h2):
    """returns [Lam(I,*), Lam(II,*), Lam(III,*)] each a list of NM residues."""
    out = [[0] * NM for _ in range(3)]
    p2 = p * p
    Bn = [comb(n, i) for i in range(n + 1)]          # C(n,k)
    Cn = [comb(n + i, n) for i in range(2 * n + 1)]  # C(n+m,n)
    for ri, R in enumerate(regions(n, p)):
        for (k, l) in R:
            T = (Cn[k] * Bn[k] ** 2 * Cn[l] * Bn[l] ** 2 * Cn[k + l])
            w = (T // p2) % p
            if w == 0:
                continue
            val = {
                'A1k': (h1[n + k] - h1[k]) % p, 'A1l': (h1[n + l] - h1[l]) % p,
                'B1k': (h1[n - k] - h1[k]) % p, 'B1l': (h1[n - l] - h1[l]) % p,
                'C1': (h1[n + k + l] - h1[k + l]) % p, 'N1': h1[n] % p,
                'A2k': (h2[n + k] - h2[k]) % p, 'A2l': (h2[n + l] - h2[l]) % p,
                'B2k': (h2[n - k] - h2[k]) % p, 'B2l': (h2[n - l] - h2[l]) % p,
                'C2': (h2[n + k + l] - h2[k + l]) % p, 'N2': h2[n] % p,
            }
            for i, m in enumerate(MONS):
                x = w
                for s in m:
                    x = x * val[s] % p
                out[ri][i] = (out[ri][i] + x) % p
    return out


def rref(M, p):
    M = [row[:] for row in M]
    rows, cols = len(M), len(M[0])
    piv = []
    r = 0
    for c in range(cols):
        pr = None
        for i in range(r, rows):
            if M[i][c] % p:
                pr = i
                break
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        iv = pow(M[r][c], -1, p)
        M[r] = [x * iv % p for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(cols)]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return M[:r], piv


def nullspace(M, p, ncols):
    R, piv = rref(M, p)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for f in free:
        v = [0] * ncols
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-R[i][f]) % p
        basis.append(v)
    return basis


if __name__ == '__main__':
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 31
    cI = kvec((0, 1, 1, 1))
    cII = kvec((1, 0, 1, 1))
    cIII = kvec((1, 1, 0, 1))
    print('K_3 support: I=%d II=%d III=%d monomials (of %d)'
          % (sum(1 for x in cI if x), sum(1 for x in cII if x),
             sum(1 for x in cIII if x), NM))
    h1, h2 = hsums(p, 3 * p + 5)
    def red(x):
        return (x.numerator % p) * pow(x.denominator % p, -1, p) % p
    c = [red(x) for x in cI] + [red(x) for x in cII] + [red(x) for x in cIII]
    rows = []
    for n in range((p + 1) // 2, p):
        V = Vvec(n, p, h1, h2)
        flat = V[0] + V[1] + V[2]
        val = sum(c[i] * flat[i] for i in range(3 * NM)) % p
        rows.append(flat)
        print('p=%d n=%3d  target = %d %s' % (p, n, val, '' if val == 0 else '   <-- FAIL'))
    ns = nullspace(rows, p, 3 * NM)
    print('p=%d  #constraints=%d  ncols=%d  rank=%d  nullity=%d'
          % (p, len(rows), 3 * NM, 3 * NM - len(ns), len(ns)))
