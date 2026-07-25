"""P1e-refold stage 3: the same search with POLYNOMIAL coefficients.

The stage-1/2 space was weight-3 homogeneous with CONSTANT rational coefficients.
That is a real restriction: a certificate-side representative may carry coefficients
that are rational functions of (n,k,l), and such coefficients cost NOTHING in symbols.
Here the space is enlarged to

    w = sum_mu  p_mu(n,k,l) * mu ,      p_mu in Q[n,k,l], deg <= dp,
    mu a monomial of letter-degree <= Dm in the letters allowed by a symbol mask,

which drops both the weight grading and the constant-coefficient restriction.

Column spec = (kmono, lmono, cmono, a, b, c) meaning
    n^a * k^b * l^c * kmono(k) * lmono(l) * cmono(k+l).
Value at level n = n^a * ( F_row . W_c . F_col )  with
    F_row[k] = k^b kmono(k) T-half ... (assembled exactly as in w3full.row).
"""
import sys, os, time
import numpy as np
from math import comb
from collections import defaultdict
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from fit import alphabet, lad_ext, Q1, Q2                    # noqa
from w3full import LSYM, ALL_SYMBOLS, SYMIDX, rref_aug       # noqa

SPLIT = 8192.0


def mmod(A, Bm, q):
    Af = A.astype(np.float64)
    Ah = np.floor(Af * (1.0 / SPLIT))
    Al = Af - Ah * SPLIT
    Bf = Bm.astype(np.float64)
    Ch = np.mod(Ah @ Bf, q).astype(np.int64)
    Cl = np.mod(Al @ Bf, q).astype(np.int64)
    return (Ch * 8192 + Cl) % q


class PolySpec:
    """column list for one symbol mask"""

    def __init__(self, letters, dp, Dm, deg_min=0, deg_max=None, extra_free=None):
        """letters: allowed letter names.  Monomials of letter-degree in
        [deg_min, deg_max] built from them, times n^a k^b l^c with a+b+c <= dp."""
        kl = [x for x in letters if x.endswith('(k)')]
        ll = [x for x in letters if x.endswith('(l)')]
        cl = [x for x in letters if x[0] == 'C']
        nl = [x for x in letters if x[0] == 'N']
        if deg_max is None:
            deg_max = Dm

        def mono(names, d):
            out = [()]
            cur = [()]
            for _ in range(d):
                nx = []
                for m in cur:
                    st = names.index(m[-1]) if m else 0
                    for i in range(st, len(names)):
                        nm = m + (names[i],)
                        if nm not in out:
                            out.append(nm)
                            nx.append(nm)
                cur = nx
            return out

        self.cols = []
        for f in mono([x[:2] for x in kl], Dm):
            for g in mono([x[:2] for x in ll], Dm):
                for c in mono(cl, Dm):
                    for s in mono(nl, Dm):
                        d = len(f) + len(g) + len(c) + len(s)
                        if not (deg_min <= d <= deg_max):
                            continue
                        for a in range(dp + 1):
                            for bb in range(dp + 1 - a):
                                for cc in range(dp + 1 - a - bb):
                                    self.cols.append((f, g, c, s, a, bb, cc))
        if extra_free:
            self.cols += extra_free
        # index tables
        self.km = sorted({(c[0], c[5]) for c in self.cols})
        self.lm = sorted({(c[1], c[6]) for c in self.cols})
        self.cm = sorted({c[2] for c in self.cols})
        self.kmi = {x: i for i, x in enumerate(self.km)}
        self.lmi = {x: i for i, x in enumerate(self.lm)}

    def __len__(self):
        return len(self.cols)


def prow(n, q, spec):
    Lk, Lc, Ln = alphabet(n, q, depth2=False, maxr=3)
    k = np.arange(n + 1)
    b1 = np.array([comb(n + i, n) % q for i in range(n + 1)], dtype=np.int64)
    b2 = np.array([comb(n, i) % q for i in range(n + 1)], dtype=np.int64)
    t = b1 * b2 % q * b2 % q
    coup = np.array([comb(n + i, n) % q for i in range(2 * n + 1)], dtype=np.int64)
    T = t[:, None] * t[None, :] % q * coup[k[:, None] + k[None, :]] % q
    kp = np.ones((max(c[5] for c in spec.cols) + 1, n + 1), dtype=np.int64)
    for e in range(1, kp.shape[0]):
        kp[e] = kp[e - 1] * k % q

    def build(monos):
        F = np.ones((len(monos), n + 1), dtype=np.int64)
        for i, (m, e) in enumerate(monos):
            v = kp[e].copy()
            for nm in m:
                v = v * Lk[nm][1] % q
            F[i] = v
        return F

    FK = build(spec.km)
    FL = build(spec.lm)
    G = {}
    for cm in spec.cm:
        if cm:
            h = np.ones(2 * n + 1, dtype=np.int64)
            for nm in cm:
                h = h * Lc[nm][1] % q
            W = T * h[k[:, None] + k[None, :]] % q
        else:
            W = T
        G[cm] = mmod(mmod(FK, W, q), np.ascontiguousarray(FL.T), q)
    np_pow = [1]
    for _ in range(max(c[4] for c in spec.cols)):
        np_pow.append(np_pow[-1] * n % q)
    out = np.zeros(len(spec), dtype=np.int64)
    for j, (f, g, c, s, a, bb, cc) in enumerate(spec.cols):
        v = G[c][spec.kmi[(f, bb)], spec.lmi[(g, cc)]]
        for nm in s:
            v = v * Ln[nm][1] % q
        out[j] = v * np_pow[a] % q
    return out


def pdesign(spec, N, q, n0=1, target='Ph'):
    Y = lad_ext(target, N + 1, q)
    M = np.zeros((N - n0 + 1, len(spec)), dtype=np.int64)
    b = np.zeros(N - n0 + 1, dtype=np.int64)
    for i, n in enumerate(range(n0, N + 1)):
        M[i] = prow(n, q, spec)
        b[i] = Y[n]
    return M, b


def consistent(spec, N, q):
    M, b = pdesign(spec, N, q)
    r, piv, inc, A = rref_aug(M, b, q)
    return (not inc), r, M.shape
