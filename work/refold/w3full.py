"""P1e-refold, stage 1: the FULL (unsymmetrised = folded) weight-3 fitting space.

    Phat_n  =  sum_{k,l=0}^{n} T(n,k,l) * w(n,k,l) ,
    T(n,k,l) = C(n+k,n)C(n,k)^2 C(n+l,n)C(n,l)^2 C(n+k+l,n) .

Basis monomial:   f(k) * g(l) * c(k+l) * s(n),   total weight 3,
    f, g  monomials in  A_r(x) = H^(r)_{n+x} - H^(r)_x ,  B_r(x) = H^(r)_{n-x} - H^(r)_x
    c     monomial in   C_r    = H^(r)_{n+k+l} - H^(r)_{k+l}
    s     monomial in   N_r    = H^(r)_n
(r <= 3 throughout).

WHY UNSYMMETRISED.  Every k<->l symmetric form has the same VALUE as its folded
representative (PHASE2_CERTS 5.2), and the folded representative is what the
Annihilator actually sees -- v, not w3hat.  Folding is what took w3hat from 19
monomials to 12 and (as the symbol census shows) it is also what can delete l-side
symbols entirely.  So the search space is the full unsymmetrised span, whose image
under V is the same as the symmetric one.

    value(f,g,c,s)(n) = s(n) * sum_{k,l} T(n,k,l) f(k) g(l) c(k+l)
                      = s(n) * ( F_f . W_c . F_g )     with W_c[k,l] = T[k,l] c(k+l).

SYMBOL CENSUS (the cost driver, PHASE2_CERTS 18.17): a "symbol" is a distinct pair
(argument, r) of HarmonicNumber.  A_r(k) -> {H^(r)_{n+k}, H^(r)_k},
B_r(k) -> {H^(r)_{n-k}, H^(r)_k}, C_r -> {H^(r)_{n+k+l}, H^(r)_{k+l}}, N_r -> {H^(r)_n}.
The folded w3hat `v` carries 12; E(v) carries 9; the target is <= 4.
"""
import sys
import numpy as np
from math import comb
from collections import defaultdict

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from fit import Q1, Q2, alphabet, lad_ext, lad_mod          # noqa

WMAX = 3
KNAMES = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3']
CNAMES = ['C1', 'C2', 'C3']
NNAMES = ['N1', 'N2', 'N3']
WT = {x: int(x[1]) for x in KNAMES + CNAMES + NNAMES}


def monos(names, wmax):
    """all multisets (sorted tuples) of `names` with total weight <= wmax"""
    out = {(): 0}
    frontier = [((), 0)]
    while frontier:
        nxt = []
        for m, w in frontier:
            start = names.index(m[-1]) if m else 0
            for i in range(start, len(names)):
                ww = WT[names[i]]
                if w + ww <= wmax:
                    nm = m + (names[i],)
                    if nm not in out:
                        out[nm] = w + ww
                        nxt.append((nm, w + ww))
        frontier = nxt
    return out


class FullBasis:
    def __init__(self, W=WMAX, knames=None, cnames=None, nnames=None):
        kn = knames if knames is not None else KNAMES
        self.km = sorted(monos(kn, W).items())
        self.cm = sorted(monos(cnames if cnames is not None else CNAMES, W).items())
        self.nm = sorted(monos(nnames if nnames is not None else NNAMES, W).items())
        self.W = W
        els = []
        for i, (f, fw) in enumerate(self.km):
            for j, (g, gw) in enumerate(self.km):
                for ci, (c, cw) in enumerate(self.cm):
                    for ni, (s, sw) in enumerate(self.nm):
                        if fw + gw + cw + sw == W:
                            els.append((i, j, ci, ni))
        self.els = els

    def __len__(self):
        return len(self.els)

    def label(self, e):
        i, j, ci, ni = e
        p = (['%s(k)' % x for x in self.km[i][0]]
             + ['%s(l)' % x for x in self.km[j][0]]
             + list(self.cm[ci][0]) + list(self.nm[ni][0]))
        return '*'.join(p) or '1'

    def degree(self, e):
        i, j, ci, ni = e
        return (len(self.km[i][0]) + len(self.km[j][0])
                + len(self.cm[ci][0]) + len(self.nm[ni][0]))

    def letters(self, e):
        i, j, ci, ni = e
        return (frozenset('%s(k)' % x for x in self.km[i][0])
                | frozenset('%s(l)' % x for x in self.km[j][0])
                | frozenset(self.cm[ci][0]) | frozenset(self.nm[ni][0]))


# ------------------------------------------------------------------ symbols
def symbols_of_letter(lt):
    """distinct HarmonicNumber symbols (argument, r) a letter introduces"""
    t, r = lt[0], int(lt[1])
    if lt.endswith('(k)'):
        x = 'k'
    elif lt.endswith('(l)'):
        x = 'l'
    else:
        x = None
    if t == 'A':
        return frozenset({('n+%s' % x, r), (x, r)})
    if t == 'B':
        return frozenset({('n-%s' % x, r), (x, r)})
    if t == 'C':
        return frozenset({('k+l', r), ('n+k+l', r)})
    if t == 'N':
        return frozenset({('n', r)})
    raise ValueError(lt)


ALL_LETTERS = (['%s(%s)' % (a, x) for x in 'kl' for a in KNAMES]
               + CNAMES + NNAMES)
LSYM = {lt: symbols_of_letter(lt) for lt in ALL_LETTERS}
ALL_SYMBOLS = sorted(set().union(*LSYM.values()))
SYMIDX = {s: i for i, s in enumerate(ALL_SYMBOLS)}
LMASK = {lt: sum(1 << SYMIDX[s] for s in LSYM[lt]) for lt in ALL_LETTERS}


def symbols_of(letterset):
    return frozenset().union(*[LSYM[x] for x in letterset]) if letterset else frozenset()


# ------------------------------------------------------------ design matrix
def row(n, q, B):
    Lk, Lc, Ln = alphabet(n, q, depth2=False, maxr=3)
    k = np.arange(n + 1)
    b1 = np.array([comb(n + i, n) % q for i in range(n + 1)], dtype=np.int64)
    b2 = np.array([comb(n, i) % q for i in range(n + 1)], dtype=np.int64)
    t = b1 * b2 % q * b2 % q
    coup = np.array([comb(n + i, n) % q for i in range(2 * n + 1)], dtype=np.int64)
    T = t[:, None] * t[None, :] % q * coup[k[:, None] + k[None, :]] % q
    F = np.ones((len(B.km), n + 1), dtype=np.int64)
    for i, (m, w) in enumerate(B.km):
        v = np.ones(n + 1, dtype=np.int64)
        for nm in m:
            v = v * Lk[nm][1] % q
        F[i] = v
    out = np.zeros(len(B), dtype=np.int64)
    bycoup = defaultdict(list)
    for idx, (i, j, ci, ni) in enumerate(B.els):
        bycoup[ci].append((idx, i, j, ni))
    for ci, lst in bycoup.items():
        cm = B.cm[ci][0]
        if cm:
            h = np.ones(2 * n + 1, dtype=np.int64)
            for nm in cm:
                h = h * Lc[nm][1] % q
            W = T * h[k[:, None] + k[None, :]] % q
        else:
            W = T
        G = (F @ W % q) @ F.T % q
        for idx, i, j, ni in lst:
            s = 1
            for nm in B.nm[ni][0]:
                s = s * Ln[nm][1] % q
            out[idx] = G[i, j] * s % q
    return out


def design(B, N, q, n0=1, target='Ph'):
    Y = lad_ext(target, N + 1, q)
    M = np.zeros((N - n0 + 1, len(B)), dtype=np.int64)
    b = np.zeros(N - n0 + 1, dtype=np.int64)
    for i, n in enumerate(range(n0, N + 1)):
        M[i] = row(n, q, B)
        b[i] = Y[n]
    return M, b


# ------------------------------------------------------------ linear algebra
def rref_aug(M, b, q):
    """row-reduce [M|b]; return (rank, pivots, inconsistent, A)"""
    A = np.concatenate([M % q, (b % q).reshape(-1, 1)], axis=1).astype(np.int64)
    rows, cols = A.shape
    piv, r = [], 0
    for c in range(cols - 1):
        if r >= rows:
            break
        nz = np.nonzero(A[r:, c])[0]
        if nz.size == 0:
            continue
        p = r + int(nz[0])
        if p != r:
            A[[r, p]] = A[[p, r]]
        A[r] = A[r] * pow(int(A[r, c]), q - 2, q) % q
        col = A[:, c].copy()
        col[r] = 0
        mask = col != 0
        if mask.any():
            A[mask] = (A[mask] - col[mask, None] * A[r][None, :]) % q
        piv.append(c)
        r += 1
    zerorow = ~(A[:, :-1] != 0).any(axis=1)
    inconsistent = bool((zerorow & (A[:, -1] != 0)).any())
    return r, piv, inconsistent, A


def solve(M, b, q):
    """particular solution (free vars 0) + kernel basis, or (None, ...) if inconsistent"""
    r, piv, inc, A = rref_aug(M, b, q)
    nc = M.shape[1]
    if inc:
        return None, None, r
    x = np.zeros(nc, dtype=np.int64)
    for i, c in enumerate(piv):
        x[c] = A[i, -1] % q
    free = [c for c in range(nc) if c not in set(piv)]
    K = np.zeros((len(free), nc), dtype=np.int64)
    for a, fc in enumerate(free):
        K[a, fc] = 1
        for i, c in enumerate(piv):
            K[a, c] = (-A[i, fc]) % q
    return x, K, r
