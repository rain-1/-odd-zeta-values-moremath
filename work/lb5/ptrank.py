"""Is the 135-dim kernel of the w5 fitting system POINTWISE trivial?

The fitting system is  P_n = sum_{k,l} T(n,k,l) w5(n,k,l)  over the 448-element
symmetric monomial basis B (weight 5, letters A1..A5,B1..B5 in k/l, C1..C5 in k+l,
N1..N5 in n).  rank(design) = 313, so ker has dim 135.

If two representatives w, w' of the family differ by z in ker(design), the claim
"certifying one representative certifies all" needs  sum_{k,l} T z = 0 identically
in n.  That is FREE if z vanishes POINTWISE, i.e. z(n,k,l) = 0 as a function.

So: compute the rank of the CELL-level matrix (rows = cells (n,k,l), columns =
basis elements, entry = the value of the symmetrised monomial at that cell).
  rank_cell = 448  ->  no pointwise relations; ker(design) is a genuine
                       summation kernel and is NOT free.
  rank_cell = 313  ->  ker(design) = pointwise relations; claim is PROVED.
"""
import sys
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from fit import Q1, alphabet, mono_scalar
from depthcond import basis

q = Q1
B = basis()
NC = len(B.els)
print('basis size', NC, flush=True)

rows = []
for n in (17, 18, 19, 20, 21, 22):
    Lk, Lc, Ln = alphabet(n, q, depth2=False, maxr=5)
    k = np.arange(n + 1)
    # k-monomial value tables
    Fm = np.ones((len(B.km), n + 1), dtype=np.int64)
    for i, (mono, w) in enumerate(B.km):
        v = np.ones(n + 1, dtype=np.int64)
        for nm in mono:
            v = v * Lk[nm][1] % q
        Fm[i] = v
    Cm = np.ones((len(B.cm), 2 * n + 1), dtype=np.int64)
    for ci, (mono, w) in enumerate(B.cm):
        v = np.ones(2 * n + 1, dtype=np.int64)
        for nm in mono:
            v = v * Lc[nm][1] % q
        Cm[ci] = v
    Ns = [mono_scalar(mono, Ln, q) for mono, w in B.nm]
    ii, jj = np.triu_indices(n + 1)          # cells 0<=k<=l<=n
    blk = np.zeros((len(ii), NC), dtype=np.int64)
    for idx, (i, j, ci, ni) in enumerate(B.els):
        f, g = Fm[i], Fm[j]
        if i == j:
            val = f[ii] * g[jj] % q
        else:
            val = (f[ii] * g[jj] + f[jj] * g[ii]) % q
        val = val * Cm[ci][ii + jj] % q * Ns[ni] % q
        blk[:, idx] = val
    rows.append(blk)
    print('  n=%d cells=%d' % (n, len(ii)), flush=True)

M = np.concatenate(rows, axis=0)
print('cell matrix', M.shape, flush=True)


def rank_mod(A, q):
    A = A.astype(np.int64) % q
    r = 0
    nrow, ncol = A.shape
    for c in range(ncol):
        nz = np.nonzero(A[r:, c])[0]
        if nz.size == 0:
            continue
        p = r + int(nz[0])
        if p != r:
            A[[r, p]] = A[[p, r]]
        inv = pow(int(A[r, c]), q - 2, q)
        A[r] = A[r] * inv % q
        col = A[r + 1:, c].copy()
        mask = col != 0
        if mask.any():
            A[r + 1:][mask] = (A[r + 1:][mask] - col[mask, None] * A[r][None, :]) % q
        r += 1
        if r == nrow:
            break
    return r


print('RANK of cell matrix =', rank_mod(M, q), flush=True)
print('(448 => no pointwise relations; 313 => kernel is pointwise-trivial)')
