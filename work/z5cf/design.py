"""Vectorised design matrices for bare-symbol harmonic fits on the BZ double sum.

Column indexed by a weight-W monomial  prod_i H^(r_i)_{alpha_i}, alpha_i one of the
nine bare symbols.  Row indexed by n.  Entry = sum_{k,l} T(n,k,l) * monomial, mod q.
"""
import numpy as np
from math import comb
import itertools, os, sys, json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bare import Q1, Q2, lad_mod, SYMS, SYMNAME

NS = 9  # the nine bare symbols


def partitions(W, maxparts=None):
    """multisets of positive integers summing to W (the r-signature)"""
    out = []

    def rec(rem, mx, cur):
        if rem == 0:
            out.append(tuple(cur))
            return
        for a in range(min(rem, mx), 0, -1):
            rec(rem - a, a, cur + [a])
    rec(W, W, [])
    return out


def monomials(W, maxdeg=None):
    """list of monomials; each = sorted tuple of (r, symbol index).
    A monomial is a multiset of (r, alpha) pairs with sum r = W."""
    mons = []
    for sig in partitions(W):
        if maxdeg is not None and len(sig) > maxdeg:
            continue
        # sig is a non-increasing tuple of r's; group equal r's -> multiset of symbols
        groups = []
        i = 0
        while i < len(sig):
            j = i
            while j < len(sig) and sig[j] == sig[i]:
                j += 1
            groups.append((sig[i], j - i))
            i = j
        choices = [list(itertools.combinations_with_replacement(range(NS), c))
                   for (_, c) in groups]
        for combo in itertools.product(*choices):
            m = []
            for (r, _), syms in zip(groups, combo):
                for s in syms:
                    m.append((r, s))
            mons.append(tuple(sorted(m)))
    return mons


SIGMA = {0: 0, 1: 2, 2: 1, 3: 4, 4: 3, 5: 6, 6: 5, 7: 7, 8: 8}  # k<->l on symbols


def sym_image(m):
    return tuple(sorted((r, SIGMA[s]) for (r, s) in m))


def sym_orbits(mons):
    """representatives of k<->l orbits, plus a map mon->rep"""
    seen = {}
    reps = []
    for m in mons:
        if m in seen:
            continue
        im = sym_image(m)
        reps.append(m)
        seen[m] = m
        seen[im] = m
    return reps, seen


def monname(m):
    from collections import Counter
    c = Counter(m)
    parts = []
    for (r, s), e in sorted(c.items()):
        t = 'H%d[%s]' % (r, SYMNAME[s])
        parts.append(t if e == 1 else '%s^%d' % (t, e))
    return '*'.join(parts) if parts else '1'


def htab(M, q, maxr):
    inv = np.zeros(M + 2, dtype=np.int64)
    for m in range(1, M + 2):
        inv[m] = pow(m, q - 2, q)
    H = {}
    for r in range(1, maxr + 1):
        h = np.zeros(M + 1, dtype=np.int64)
        s = 0
        for m in range(1, M + 1):
            s = (s + pow(int(inv[m]), r, q)) % q
            h[m] = s
        H[r] = h
    return H


def build(W, N, q, maxdeg=None, symmetric=True, verbose=True):
    mons = monomials(W, maxdeg)
    if symmetric:
        mons, _ = sym_orbits(mons)
    Hm = htab(4 * N + 4, q, W)
    rows = []
    for n in range(0, N + 1):
        kk, ll = np.meshgrid(np.arange(n + 1), np.arange(n + 1), indexing='ij')
        kk = kk.ravel(); ll = ll.ravel()
        Tv = np.array([comb(n + int(a), n) * comb(n, int(a)) ** 2
                       * comb(n + int(b), n) * comb(n, int(b)) ** 2
                       * comb(n + int(a) + int(b), n) % q
                       for a, b in zip(kk, ll)], dtype=np.int64)
        idx = [np.full(kk.shape, n), kk, ll, n + kk, n + ll, n - kk, n - ll,
               kk + ll, n + kk + ll]
        hv = {r: [Hm[r][i] for i in idx] for r in range(1, W + 1)}
        row = np.zeros(len(mons), dtype=np.int64)
        for j, m in enumerate(mons):
            v = Tv
            for (r, s) in m:
                v = v * hv[r][s] % q
            row[j] = int(v.sum() % q)
        rows.append(row)
        if verbose and n % 10 == 0:
            print('   n=%d' % n, flush=True)
    return mons, np.array(rows, dtype=np.int64)
