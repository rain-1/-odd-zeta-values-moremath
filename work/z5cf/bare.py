"""Bare-symbol harmonic fitting for the Brown-Zudilin rows.

The BZ campaigns (work/PHASE2_*, work/REFOLD.md) searched an alphabet of
DIFFERENCES
      A_r(x)=H^(r)_{n+x}-H^(r)_x, B_r(x)=H^(r)_{n-x}-H^(r)_x,
      C_r  =H^(r)_{n+k+l}-H^(r)_{k+l}, N_r=H^(r)_n .
The Apery minimal form  b_n = sum_k A(n,k)(2H^(3)_n - H^(3)_k)  is NOT in the
span of such differences (H^(3)_k alone is not a difference).  This module
fits in the BARE symbol alphabet

      H^(r)_alpha ,  alpha in {n,k,l,n+k,n+l,n-k,n-l,k+l,n+k+l}   (the nine
      symbols produced by differentiating the five binomials of T),

which is what the Apery precedent actually uses.

Arithmetic mod a prime q.
"""
import numpy as np
from math import comb
from fractions import Fraction as F
import json, functools, sys

Q1 = 33554393
Q2 = 33554467
LAD = '/home/ubuntu/fable-episode-2/zeta-math/worthiness/falsify_data/'


@functools.lru_cache(maxsize=None)
def ladders():
    out = {}
    for k in ('Q', 'P', 'Ph'):
        d = json.load(open(LAD + 'ladder_%s.json' % k))
        out[k] = {int(n): (int(v[0]), int(v[1])) for n, v in d.items()}
    return out


def lad_mod(key, n, q):
    a, b = ladders()[key][n]
    return a % q * pow(b % q, q - 2, q) % q


def lad_exact(key, n):
    a, b = ladders()[key][n]
    return F(a, b)


def T(n, k, l):
    return (comb(n + k, n) * comb(n, k) ** 2 * comb(n + l, n) * comb(n, l) ** 2
            * comb(n + k + l, n))


# ---------------------------------------------------------------- symbols
# alpha(n,k,l) -> index of the harmonic number
SYMS = [
    ('n',       lambda n, k, l: n),
    ('k',       lambda n, k, l: k),
    ('l',       lambda n, k, l: l),
    ('n+k',     lambda n, k, l: n + k),
    ('n+l',     lambda n, k, l: n + l),
    ('n-k',     lambda n, k, l: n - k),
    ('n-l',     lambda n, k, l: n - l),
    ('k+l',     lambda n, k, l: k + l),
    ('n+k+l',   lambda n, k, l: n + k + l),
]
SYMNAME = [s[0] for s in SYMS]
NS = len(SYMS)

# optional extras (2nd tier); enable with EXTRA=1
EXTRA_SYMS = [
    ('2n',      lambda n, k, l: 2 * n),
    ('2n+k',    lambda n, k, l: 2 * n + k),
    ('2n+l',    lambda n, k, l: 2 * n + l),
    ('n+k-l',   lambda n, k, l: n + k - l),
    ('n-k+l',   lambda n, k, l: n - k + l),
    ('2n-k',    lambda n, k, l: 2 * n - k),
    ('2n-l',    lambda n, k, l: 2 * n - l),
    ('2n+k+l',  lambda n, k, l: 2 * n + k + l),
    ('2n-k-l',  lambda n, k, l: 2 * n - k - l),
]


def htab(M, q, maxr):
    """H[r][m] mod q, m = 0..M."""
    inv = [0] * (M + 2)
    for m in range(1, M + 2):
        inv[m] = pow(m, q - 2, q)
    H = {}
    for r in range(1, maxr + 1):
        h = [0] * (M + 1)
        s = 0
        for m in range(1, M + 1):
            s = (s + pow(inv[m], r, q)) % q
            h[m] = s
        H[r] = h
    return H


class Sums:
    """S[(r1,a1),(r2,a2),...] (n) = sum_{k,l} T(n,k,l) * prod H^(r_i)_{alpha_i}"""

    def __init__(self, N, q, maxr=5, extra=False):
        self.N, self.q = N, q
        self.syms = SYMS + (EXTRA_SYMS if extra else [])
        self.H = htab(4 * N + 4, q, maxr)

    def cells(self, n):
        q = self.q
        out = []
        for k in range(n + 1):
            for l in range(n + 1):
                out.append((k, l, T(n, k, l) % q))
        return out

    @functools.lru_cache(maxsize=None)
    def _cells(self, n):
        return self.cells(n)

    def eval(self, n, monos):
        """monos: list of tuples of (r, symbol-index). returns list of sums mod q"""
        q = self.q
        res = [0] * len(monos)
        for (k, l, t) in self._cells(n):
            if t == 0:
                continue
            idx = [f(n, k, l) for _, f in self.syms]
            for j, m in enumerate(monos):
                v = t
                for (r, si) in m:
                    v = v * self.H[r][idx[si]] % q
                res[j] = (res[j] + v) % q
        return res


# ------------------------------------------------------------ linear algebra
def rref_mod(M, q):
    """in-place RREF of list-of-lists mod q; returns (rank, pivots)"""
    rows = len(M)
    cols = len(M[0]) if rows else 0
    r = 0
    piv = []
    for c in range(cols):
        p = None
        for i in range(r, rows):
            if M[i][c] % q:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        iv = pow(M[r][c], q - 2, q)
        M[r] = [x * iv % q for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % q for j in range(cols)]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return r, piv


def consistent(A, b, q):
    """A: rows x cols list-of-lists; b: rows. Return (ok, rankA, rankAb, solution)"""
    rows = len(A)
    M1 = [row[:] for row in A]
    rA, _ = rref_mod(M1, q)
    M2 = [A[i][:] + [b[i]] for i in range(rows)]
    rAb, piv = rref_mod(M2, q)
    sol = None
    if rA == rAb:
        cols = len(A[0])
        x = [0] * cols
        for i, c in enumerate(piv):
            if c < cols:
                x[c] = M2[i][cols]
        sol = x
    return (rA == rAb), rA, rAb, sol
