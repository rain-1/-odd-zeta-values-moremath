"""P1g: the R-extended fitting system for  P_n = sum_{k,l} T(n,k,l) w(n,k,l).

Alphabet
  k-slot :  A_r(k)=H^(r)_{n+k}-H^(r)_k , B_r(k)=H^(r)_{n-k}-H^(r)_k ,
            R_r(k)=sum_{m<=k}(-1)^{m-1}/(m^r C(n,m)C(n+m,m))            [NEW]
  coupling: C_r  =H^(r)_{n+k+l}-H^(r)_{k+l} ,
            D_r  =sum_{j<=k+l}(-1)^{j-1}/(j^r C(n+j,j))                 [NEW, optional]
  n-slot  : N_r  =H^(r)_n

Basis element = ({f,g} unordered pair of k-monomials) x c-monomial x n-monomial,
total weight 5; value = sum_{k,l} T [f(k)g(l)+f(l)g(k)] h(k+l) s   (halved if f==g).

Speed: modular matmul via a 13-bit float64 split (2 dgemms), exact for the sizes used.
"""
import sys
import numpy as np
from math import comb

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from fit import Q1, Q2, monos, Basis, mono_scalar, lad_mod, lad_ext   # noqa
from rlet import R_tab, D_tab

MAXR = 5
AB = ['A%d' % r for r in range(1, 6)] + ['B%d' % r for r in range(1, 6)]
KL = AB + ['R%d' % r for r in range(1, 6)]
CL = ['C%d' % r for r in range(1, 6)]
DL = ['D%d' % r for r in range(1, 6)]
NL = ['N%d' % r for r in range(1, 6)]
# nested (depth-2) INTERVAL letters, weight a+b, pole order max(a,b) < a+b :
#   Y_ab(k)   = sum_{k < m2 < m1 <= n+k}    m1^-a m2^-b     (k-slot, indicator alpha)
#   V_ab(k+l) = sum_{k+l < m2 < m1 <= n+k+l} m1^-a m2^-b    (coupling, indicator kappa)
#   Z_ab      = sum_{1 <= m2 < m1 <= n}      m1^-a m2^-b     (n-slot, no pole)
PAIRS = [(a, b) for a in range(1, 5) for b in range(1, 5) if 2 <= a + b <= 5]
YL = ['Y%d%d' % ab for ab in PAIRS]
VL = ['V%d%d' % ab for ab in PAIRS]
ZL = ['Z%d%d' % ab for ab in PAIRS]

SPLIT = 8192.0          # 2^13


def mmod(A, B, q):
    """(A @ B) mod q for int64 arrays with entries in [0,q), q < 2^25."""
    Af = A.astype(np.float64)
    Ah = np.floor(Af * (1.0 / SPLIT))
    Al = Af - Ah * SPLIT
    Bf = B.astype(np.float64)
    Ch = np.mod(Ah @ Bf, q).astype(np.int64)
    Cl = np.mod(Al @ Bf, q).astype(np.int64)
    return (Ch * 8192 + Cl) % q


def _htab(M, q, maxr=MAXR, nested=False):
    inv = np.zeros(M + 1, dtype=np.int64)
    for m in range(1, M + 1):
        inv[m] = pow(int(m), q - 2, q)
    pw = {r: np.zeros(M + 1, dtype=np.int64) for r in range(1, maxr + 1)}
    for r in range(1, maxr + 1):
        for m in range(1, M + 1):
            pw[r][m] = pow(int(inv[m]), r, q)
    H = {}
    for r in range(1, maxr + 1):
        h = np.zeros(M + 1, dtype=np.int64)
        acc = 0
        for m in range(1, M + 1):
            acc = (acc + int(pw[r][m])) % q
            h[m] = acc
        H[r] = h
    if not nested:
        return H, None
    ZZ = {}
    for (a, b) in PAIRS:
        z = np.zeros(M + 1, dtype=np.int64)
        acc = 0
        for m1 in range(2, M + 1):
            acc = (acc + int(pw[a][m1]) * int(H[b][m1 - 1])) % q
            z[m1] = acc
        ZZ[(a, b)] = z
    return H, ZZ


def alphabet(n, q, maxr=MAXR, useD=True, nested=False):
    H, ZZ = _htab(3 * n + 2, q, maxr, nested=nested)
    k = np.arange(n + 1)
    m = np.arange(2 * n + 1)
    Lk, Lc, Ln = {}, {}, {}
    for r in range(1, maxr + 1):
        Lk['A%d' % r] = (r, (H[r][n + k] - H[r][k]) % q)
        Lk['B%d' % r] = (r, (H[r][n - k] - H[r][k]) % q)
        Lc['C%d' % r] = (r, (H[r][n + m] - H[r][m]) % q)
        Ln['N%d' % r] = (r, int(H[r][n]))
    Rt = R_tab(n, q, maxr)
    for r in range(1, maxr + 1):
        Lk['R%d' % r] = (r, Rt[r] % q)
    if useD:
        Dt = D_tab(n, q, maxr)
        for r in range(1, maxr + 1):
            Lc['D%d' % r] = (r, Dt[r] % q)
    if nested:
        for (a, b), z in ZZ.items():
            w = a + b
            Lk['Y%d%d' % (a, b)] = (w, ((z[n + k] - z[k])
                                        - (H[a][n + k] - H[a][k]) * H[b][k]) % q)
            Lc['V%d%d' % (a, b)] = (w, ((z[n + m] - z[m])
                                        - (H[a][n + m] - H[a][m]) * H[b][m]) % q)
            Ln['Z%d%d' % (a, b)] = (w, int(z[n]))
    return Lk, Lc, Ln


def build_basis(W=5, maxfac_k=5, maxfac_c=2, maxfac_n=2,
                kletters=None, cletters=None, nletters=None, useD=False, nested=False):
    Lk, Lc, Ln = alphabet(6, Q1, useD=useD, nested=nested)
    wk = {a: v[0] for a, v in Lk.items()}
    wc = {a: v[0] for a, v in Lc.items()}
    wn = {a: v[0] for a, v in Ln.items()}
    if kletters is not None:
        wk = {a: v for a, v in wk.items() if a in kletters}
    if cletters is not None:
        wc = {a: v for a, v in wc.items() if a in cletters}
    if nletters is not None:
        wn = {a: v for a, v in wn.items() if a in nletters}
    return Basis(monos(wk, W, maxfac_k), monos(wc, W, maxfac_c),
                 monos(wn, W, maxfac_n), W)


def row(n, q, basis, useD=False, nested=False):
    """Design-matrix row at level n, mod q."""
    Lk, Lc, Ln = alphabet(n, q, useD=useD, nested=nested)
    k = np.arange(n + 1)
    b1 = np.array([comb(n + i, n) % q for i in range(n + 1)], dtype=np.int64)
    b2 = np.array([comb(n, i) % q for i in range(n + 1)], dtype=np.int64)
    t = b1 * b2 % q * b2 % q
    coup = np.array([comb(n + i, n) % q for i in range(2 * n + 1)], dtype=np.int64)
    # U[i,k] = f_i(k) * t(k)
    U = np.ones((len(basis.km), n + 1), dtype=np.int64)
    for i, (mono, w) in enumerate(basis.km):
        v = t.copy()
        for nm in mono:
            v = v * Lk[nm][1] % q
        U[i] = v
    idx = k[:, None] + k[None, :]
    out = np.zeros(len(basis), dtype=np.int64)
    from collections import defaultdict
    bycoup = defaultdict(list)
    for j, (i1, i2, ci, ni) in enumerate(basis.els):
        bycoup[ci].append((j, i1, i2, ni))
    UT = np.ascontiguousarray(U.T)
    for ci, lst in bycoup.items():
        cmono = basis.cm[ci][0]
        h = coup.copy()
        for nm in cmono:
            h = h * Lc[nm][1] % q
        Wm = h[idx]
        G = mmod(mmod(U, Wm, q), UT, q)
        for j, i1, i2, ni in lst:
            s = mono_scalar(basis.nm[ni][0], Ln, q)
            v = G[i1, i2] if i1 == i2 else 2 * G[i1, i2] % q
            out[j] = v * s % q
    return out


def rref(M, b, q):
    """Row-reduce [M|b] mod q.  Returns (rank, pivots, inconsistent, A)."""
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
        piv.append(c)
        r += 1
        if r == rows:
            break
    zerorow = ~(A[:, :-1] != 0).any(axis=1)
    inconsistent = bool((zerorow & (A[:, -1] != 0)).any())
    return r, piv, inconsistent, A


if __name__ == '__main__':
    import time
    # sanity: mmod vs int64 matmul
    rng = np.random.default_rng(0)
    A = rng.integers(0, Q1, (37, 91)).astype(np.int64)
    B = rng.integers(0, Q1, (91, 53)).astype(np.int64)
    assert np.array_equal(mmod(A, B, Q1), (A @ B) % Q1), 'mmod mismatch'
    print('mmod OK', flush=True)

    B0 = build_basis(kletters=KL, cletters=CL, nletters=NL)
    print('R-extended basis size (k-slot R only): %d   (k-monomials %d)'
          % (len(B0), len(B0.km)), flush=True)
    B1 = build_basis(kletters=KL, cletters=CL + DL, nletters=NL, useD=True)
    print('R+D-extended basis size: %d  (c-monomials %d)' % (len(B1), len(B1.cm)), flush=True)
    Bold = build_basis(kletters=[x for x in KL if x[0] != 'R'], cletters=CL, nletters=NL)
    print('control (A,B,C,N only) basis size: %d' % len(Bold), flush=True)

    # cross-check the control row against work/lb5/fit.row
    from fit import row as row_old
    from run_fit import build_basis as bb_old
    Bc = bb_old(5, False, 5, 2, 2, maxr=5,
                kletters=[x for x in KL if x[0] != 'R'], cletters=CL, nletters=NL)
    for n in (3, 7, 12):
        r1 = row(n, Q1, Bold)
        r2 = row_old(n, Q1, Bc, depth2=False, maxr=5)
        assert np.array_equal(r1, r2), 'row mismatch at n=%d' % n
    print('row() cross-check vs lb5/fit.row: OK (n=3,7,12)', flush=True)

    for n in (100, 300, 600):
        t0 = time.time()
        row(n, Q1, B0)
        print('  row(n=%d) in extended basis: %.2f s' % (n, time.time() - t0), flush=True)
