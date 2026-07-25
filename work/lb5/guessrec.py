"""Guess minimal-order recurrences (mod q) for the five component sums of Theorem B.

  U1 = sum T A3(k)   U2 = sum T A2(k)A1(k)   U3 = sum T A2(k)B1(k)
  U4 = sum T A2(k)C1 U5 = sum T A2(k)A1(l)   R  = the full sum T*w3hat

Tells us (i) how big the telescopers coming out of creative telescoping should be,
(ii) whether the lclm finish of the decomposition route is affordable, and
(iii) re-confirms that the full combination R is annihilated by the order-3 L_BZ.
"""
import sys, time
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from fit import Q1, htables
from math import comb

q = Q1
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200

t0 = time.time()
H, _ = htables(3 * NMAX + 4, q, maxr=3)
print('htables %.1fs' % (time.time() - t0), flush=True)

vals = {name: [] for name in ('U1', 'U2', 'U3', 'U4', 'U5', 'R', 'Q')}
for n in range(NMAX + 1):
    k = np.arange(n + 1)
    bnk = np.array([comb(n + i, n) % q for i in range(n + 1)], dtype=np.int64)
    bn_k = np.array([comb(n, i) % q for i in range(n + 1)], dtype=np.int64)
    t = bnk * bn_k % q * bn_k % q
    coup = np.array([comb(n + i, n) % q for i in range(2 * n + 1)], dtype=np.int64)
    T = t[:, None] * t[None, :] % q * coup[k[:, None] + k[None, :]] % q
    A = {r: (H[r][n + k] - H[r][k]) % q for r in (1, 2, 3)}
    B1 = (H[1][n - k] - H[1][k]) % q
    C1 = (H[1][n + np.arange(2 * n + 1)] - H[1][np.arange(2 * n + 1)]) % q
    ones = np.ones(n + 1, dtype=np.int64)
    Ssum = lambda f, g: int(f @ T % q @ g % q)
    Cw = T * C1[k[:, None] + k[None, :]] % q
    u1 = Ssum(A[3], ones)
    u2 = Ssum(A[2] * A[1] % q, ones)
    u3 = Ssum(A[2] * B1 % q, ones)
    u4 = int(A[2] @ Cw % q @ ones % q)
    u5 = Ssum(A[2], A[1])
    Qn = Ssum(ones, ones)
    R = (int(H[3][n]) * Qn + 2 * u1 - pow(2, q - 2, q) * u2
         - 3 * pow(2, q - 2, q) * u3 - 3 * pow(4, q - 2, q) * u4
         - pow(4, q - 2, q) * u5) % q
    for nm, v in zip(('U1', 'U2', 'U3', 'U4', 'U5', 'R', 'Q'),
                     (u1, u2, u3, u4, u5, R, Qn)):
        vals[nm].append(v % q)
print('values %.1fs' % (time.time() - t0), flush=True)


def guess(seq, rmax=12, dmax=30):
    """smallest (r,d) with sum_{j<=r} p_j(n) y_{n+j} = 0, deg p_j <= d, verified on
    all remaining equations."""
    N = len(seq)
    for r in range(1, rmax + 1):
        for d in range(0, dmax + 1):
            nunk = (r + 1) * (d + 1)
            neq = N - r
            if neq < nunk + 8:
                continue
            rows = []
            for n in range(N - r):
                row = []
                for j in range(r + 1):
                    for e in range(d + 1):
                        row.append(pow(n, e, q) * seq[n + j] % q)
                rows.append(row)
            M = np.array(rows, dtype=np.int64) % q
            ns = nullspace(M, q)
            if ns:
                return r, d, len(ns)
    return None


def nullspace(A, q):
    A = A.copy() % q
    rows, cols = A.shape
    piv = []
    rr = 0
    for c in range(cols):
        nz = np.nonzero(A[rr:, c])[0]
        if nz.size == 0:
            continue
        p = rr + int(nz[0])
        if p != rr:
            A[[rr, p]] = A[[p, rr]]
        A[rr] = A[rr] * pow(int(A[rr, c]), q - 2, q) % q
        col = A[:, c].copy(); col[rr] = 0
        m = col != 0
        if m.any():
            A[m] = (A[m] - col[m, None] * A[rr][None, :]) % q
        piv.append(c); rr += 1
        if rr == rows:
            break
    free = [c for c in range(cols) if c not in piv]
    out = []
    for f in free:
        v = np.zeros(cols, dtype=np.int64); v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-A[i, f]) % q
        out.append(v)
    return out


for nm in ('Q', 'U1', 'U2', 'U3', 'U4', 'U5', 'R'):
    t1 = time.time()
    g = guess(vals[nm])
    print('%-3s  N=%d  ->  %s   (%.0fs)' % (nm, NMAX + 1, g, time.time() - t1), flush=True)
