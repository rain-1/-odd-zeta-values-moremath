"""Exact-mod-q linear fitting machinery for harmonic decompositions

    Y_n = sum_{k,l=0}^n T(n,k,l) * w(n,k,l),
    T(n,k,l) = C(n+k,n)C(n,k)^2 C(n+l,n)C(n,l)^2 C(n+k+l,n),

w a Q-linear combination of SYMMETRIC monomials in an alphabet of harmonic
letters.  Every letter depends on k only, l only, k+l only, or n only, so

    sum_{k,l} T f(k) g(l) h(k+l) = f^T W_h g ,   W_h[k,l] = T[k,l] h(k+l),

and all basis values for one coupling monomial h come from ONE product
(F W_h) F^T.   Arithmetic mod a prime q < 2^25 (int64 numpy matmul safe).
"""
import numpy as np
from math import comb
import json

Q1 = 33554393      # prime < 2^25
Q2 = 33554467      # prime < 2^25

LAD = '/home/ubuntu/fable-episode-2/zeta-math/worthiness/falsify_data/'
_lad = None
def ladder(key):
    global _lad
    if _lad is None:
        _lad = {}
        for kk in ('Q', 'P', 'Ph'):
            d = json.load(open(LAD + 'ladder_%s.json' % kk))
            _lad[kk] = {int(n): (int(v[0]), int(v[1])) for n, v in d.items()}
    return _lad[key]

def lad_mod(key, n, q):
    a, b = ladder(key)[n]
    return a % q * pow(b % q, q - 2, q) % q

# ------ extension of the ladders mod q by the certified order-3 BZ recurrence ------
def _a0(n): return 41218*n**3 + 198849*n**2 + 320790*n + 173057
def _B8(n):
    return (3874492*n**8 + 59373972*n**7 + 394148190*n**6 + 1481084196*n**5
            + 3447878810*n**4 + 5095855458*n**3 + 4673546679*n**2
            + 2433871008*n + 551502039)
def _B9(n):
    return (48802112*n**9 + 967468896*n**8 + 8488000862*n**7 + 43246197636*n**6
            + 140983768422*n**5 + 304912330849*n**4 + 437406946975*n**3
            + 401272692378*n**2 + 213593890911*n + 50257929339)

_ext = {}
def lad_ext(key, N, q):
    """{n: Y_n mod q} for n=0..N, by forward recursion; cross-checked vs the exact
    ladder on n<=360."""
    ck = (key, q)
    if ck in _ext and len(_ext[ck]) > N:
        return _ext[ck]
    Y = {n: lad_mod(key, n, q) for n in (0, 1, 2)}
    for n in range(0, N - 2):
        c3 = 2 * (n+3)**5 * (2*n+5) * _a0(n) % q
        if c3 == 0:
            raise RuntimeError('leading coeff vanishes mod q at n=%d' % n)
        c0 = (n+1)**5 * (n+2) * _a0(n+1) % q
        c1 = (-2*(n+2)*_B8(n)) % q
        c2 = (-2*_B9(n)) % q
        Y[n+3] = (-(c0*Y[n] + c1*Y[n+1] + c2*Y[n+2])) % q * pow(c3, q-2, q) % q
    # cross-check against the exact ladder
    for n in range(0, min(N, 360) + 1):
        assert Y[n] == lad_mod(key, n, q), 'ladder mismatch at n=%d' % n
    _ext[ck] = Y
    return Y

# -------------------------------------------------------------- harmonic data
def htables(M, q, maxr=5):
    """H[r][m], m=0..M ; ZZ[(a,b)][m] = sum_{m>=m1>m2>=1} m1^-a m2^-b, 3<=a+b<=5."""
    inv = [0] * (M + 1)
    for m in range(1, M + 1):
        inv[m] = pow(m, q - 2, q)
    pw = {r: [0] * (M + 1) for r in range(1, maxr + 1)}
    for r in range(1, maxr + 1):
        for m in range(1, M + 1):
            pw[r][m] = pow(inv[m], r, q)
    H = {}
    for r in range(1, maxr + 1):
        h = np.zeros(M + 1, dtype=np.int64); acc = 0
        for m in range(1, M + 1):
            acc = (acc + pw[r][m]) % q; h[m] = acc
        H[r] = h
    ZZ = {}
    for a in range(1, 5):
        for b in range(1, 5):
            if not (3 <= a + b <= 5) or a > maxr or b > maxr:
                continue
            z = np.zeros(M + 1, dtype=np.int64); acc = 0
            for m1 in range(2, M + 1):
                acc = (acc + pw[a][m1] * int(H[b][m1 - 1])) % q
                z[m1] = acc
            ZZ[(a, b)] = z
    return H, ZZ

# -------------------------------------------------------------- alphabet
def alphabet(n, q, depth2=True, maxr=5, raw=False):
    """Lk: name -> (weight, array over k=0..n)
       Lc: name -> (weight, array over m=0..2n)
       Ln: name -> (weight, scalar)"""
    H, ZZ = htables(3 * n + 2, q, maxr=maxr)
    k = np.arange(n + 1); m = np.arange(2 * n + 1)
    Lk, Lc, Ln = {}, {}, {}
    for r in range(1, maxr + 1):
        Lk['A%d' % r] = (r, (H[r][n + k] - H[r][k]) % q)
        Lk['B%d' % r] = (r, (H[r][n - k] - H[r][k]) % q)
        Lc['C%d' % r] = (r, (H[r][n + m] - H[r][m]) % q)
        Ln['N%d' % r] = (r, int(H[r][n]))
        Ln['M%d' % r] = (r, int(H[r][2 * n]))
    if depth2:
        for (a, b), z in ZZ.items():
            w = a + b
            Lk['ZA%d%d' % (a, b)] = (w, (z[n + k] - z[k]) % q)
            Lk['ZB%d%d' % (a, b)] = (w, (z[n - k] - z[k]) % q)
            Lc['ZC%d%d' % (a, b)] = (w, (z[n + m] - z[m]) % q)
            Ln['ZN%d%d' % (a, b)] = (w, int(z[n]))
            Ln['ZM%d%d' % (a, b)] = (w, int(z[2 * n]))
    if depth2:
        # INTERVAL nested letters: the true depth-2 analogue of A_r(k)/C_r --
        #   YA_{a,b}(k) = sum_{k < m2 < m1 <= n+k} m1^-a m2^-b
        #               = ZA_{a,b}(k) - A_a(k) * H^{(b)}_k
        #   YC_{a,b}    = sum_{k+l < m2 < m1 <= n+k+l} m1^-a m2^-b
        for (a, b), z in ZZ.items():
            w = a + b
            Lk['YA%d%d' % (a, b)] = (w, ((z[n + k] - z[k])
                                         - (H[a][n + k] - H[a][k]) * H[b][k]) % q)
            Lc['YC%d%d' % (a, b)] = (w, ((z[n + m] - z[m])
                                         - (H[a][n + m] - H[a][m]) * H[b][m]) % q)
    if raw:
        # raw (undifferenced) harmonic letters: adjoining these makes the span equal to
        # ALL monomials in H^{(r)}_x, x in {k,n+k,n-k, l,n+l,n-l, k+l,n+k+l, n, 2n}
        for r in range(1, maxr + 1):
            Lk['R%d' % r] = (r, H[r][k].copy())
            Lc['RC%d' % r] = (r, H[r][m].copy())
        if depth2:
            for (a, b), z in ZZ.items():
                Lk['ZR%d%d' % (a, b)] = (a + b, z[k].copy())
                Lc['ZRC%d%d' % (a, b)] = (a + b, z[m].copy())
    return Lk, Lc, Ln

# -------------------------------------------------------------- monomials
def monos(weights, wmax, maxfac):
    """multisets of names, total weight <= wmax, <= maxfac factors -> {mono: weight}"""
    names = sorted(weights)
    res = {(): 0}
    cur = [((), 0)]
    for _ in range(maxfac):
        nxt = []
        for mono, w in cur:
            start = names.index(mono[-1]) if mono else 0
            for i in range(start, len(names)):
                ww = weights[names[i]]
                if w + ww <= wmax:
                    nm = mono + (names[i],)
                    if nm not in res:
                        res[nm] = w + ww
                        nxt.append((nm, w + ww))
        cur = nxt
    return res

def mono_val(mono, L, q, shape=None):
    if not mono:
        return None            # means "1"
    v = None
    for nm in mono:
        a = L[nm][1]
        v = a.copy() if v is None else v * a % q
    return v

def mono_scalar(mono, Ln, q):
    v = 1
    for nm in mono:
        v = v * Ln[nm][1] % q
    return v

# -------------------------------------------------------------- basis spec
class Basis:
    """A basis element = ({f,g} unordered pair of k-monomials) x c-monomial x n-monomial,
    total weight = W.  Value = sum_{k,l} T [f(k)g(l)+f(l)g(k)] h(k+l) s   (halved if f==g)."""
    def __init__(self, kmonos, cmonos, nmonos, W):
        self.km = sorted(kmonos.items())       # list of (mono, weight)
        self.cm = sorted(cmonos.items())
        self.nm = sorted(nmonos.items())
        self.W = W
        els = []
        for ci, (cmono, cw) in enumerate(self.cm):
            for ni, (nmono, nw) in enumerate(self.nm):
                rest = W - cw - nw
                if rest < 0:
                    continue
                for i, (f, fw) in enumerate(self.km):
                    for j in range(i, len(self.km)):
                        g, gw = self.km[j]
                        if fw + gw == rest:
                            els.append((i, j, ci, ni))
        self.els = els
    def __len__(self):
        return len(self.els)
    def label(self, e):
        i, j, ci, ni = e
        f = '*'.join(self.km[i][0]) or '1'
        g = '*'.join(self.km[j][0]) or '1'
        c = '*'.join(self.cm[ci][0]) or '1'
        s = '*'.join(self.nm[ni][0]) or '1'
        return '[%s|%s]x%sx%s' % (f, g, c, s)

def row(n, q, basis, depth2=True, maxr=5, raw=False):
    """Row of the design matrix at level n (mod q), plus nothing else."""
    Lk, Lc, Ln = alphabet(n, q, depth2=depth2, maxr=maxr, raw=raw)
    k = np.arange(n + 1)
    # T grid
    binom_nk_n = np.array([comb(n + i, n) % q for i in range(n + 1)], dtype=np.int64)
    binom_n_k = np.array([comb(n, i) % q for i in range(n + 1)], dtype=np.int64)
    t = binom_nk_n * (binom_n_k % q) % q * (binom_n_k % q) % q      # t(k)
    coup = np.array([comb(n + i, n) % q for i in range(2 * n + 1)], dtype=np.int64)
    T = t[:, None] * t[None, :] % q * coup[k[:, None] + k[None, :]] % q
    # F matrix over k-monomials
    F = np.ones((len(basis.km), n + 1), dtype=np.int64)
    for i, (mono, w) in enumerate(basis.km):
        v = np.ones(n + 1, dtype=np.int64)
        for nm in mono:
            v = v * Lk[nm][1] % q
        F[i] = v
    out = np.zeros(len(basis), dtype=np.int64)
    # group elements by coupling monomial
    from collections import defaultdict
    bycoup = defaultdict(list)
    for idx, (i, j, ci, ni) in enumerate(basis.els):
        bycoup[ci].append((idx, i, j, ni))
    for ci, lst in bycoup.items():
        cmono = basis.cm[ci][0]
        if cmono:
            h = np.ones(2 * n + 1, dtype=np.int64)
            for nm in cmono:
                h = h * Lc[nm][1] % q
            W = T * h[k[:, None] + k[None, :]] % q
        else:
            W = T
        FW = F @ W % q
        G = FW @ F.T % q
        for idx, i, j, ni in lst:
            s = mono_scalar(basis.nm[ni][0], Ln, q)
            v = G[i, j] if i == j else 2 * G[i, j] % q
            out[idx] = v * s % q
    return out

# -------------------------------------------------------------- linear algebra
def rref(M, b, q):
    """Row-reduce [M|b] mod q with numpy int64. Returns (rank, pivots, inconsistent, A)."""
    A = np.concatenate([M % q, (b % q).reshape(-1, 1)], axis=1).astype(np.int64)
    rows, cols = A.shape
    piv = []
    r = 0
    for c in range(cols - 1):
        nz = np.nonzero(A[r:, c])[0]
        if nz.size == 0:
            continue
        p = r + int(nz[0])
        if p != r:
            A[[r, p]] = A[[p, r]]
        inv = pow(int(A[r, c]), q - 2, q)
        A[r] = A[r] * inv % q
        col = A[:, c].copy()
        col[r] = 0
        mask = col != 0
        if mask.any():
            A[mask] = (A[mask] - col[mask, None] * A[r][None, :]) % q
        piv.append(c); r += 1
        if r == rows:
            break
    zerorow = ~(A[:, :-1] != 0).any(axis=1)
    inconsistent = bool((zerorow & (A[:, -1] != 0)).any())
    return r, piv, inconsistent, A

def solve_particular(M, b, q):
    """Return a particular solution x (free vars = 0) or None if inconsistent."""
    r, piv, inc, A = rref(M, b, q)
    if inc:
        return None, r, piv
    x = np.zeros(M.shape[1], dtype=np.int64)
    for i, c in enumerate(piv):
        x[c] = A[i, -1] % q
    return x, r, piv
