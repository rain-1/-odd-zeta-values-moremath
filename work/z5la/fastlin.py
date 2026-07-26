"""Blocked Gaussian elimination over F_p using float64 BLAS.

p must satisfy  nb * (p-1)^2 < 2^53  so that every dgemm accumulation is exact
in float64;  nb = 192, p < 2^20  gives  192*1.1e12 = 2.1e14 << 9.0e15.

solve(A, B, p) -> (X, rank, pivcols, nbad)
  canonical solution of A X = B with all non-pivot unknowns set to 0
  (columns are scanned left to right, so the pivot-column set is the
  lexicographically first independent set -- the same for generic n and p,
  which is what makes the answer a well-defined rational function of n).
"""
import numpy as np

NB = 192

def _inv(a, p):
    return pow(int(a) % p, p - 2, p)

def elim(M, p, ncols_A, nb=NB):
    """in-place forward elimination of the augmented matrix M (float64, mod p).
    Only the first ncols_A columns are searched for pivots.
    returns (rank, pivcols, pivrows-as-0..rank-1 in place)"""
    rows, cols = M.shape
    r = 0
    pivcols = []
    c = 0
    while c < ncols_A and r < rows:
        cend = min(c + nb, ncols_A)
        r0 = r
        mults = []                      # multiplier columns, one per pivot
        while c < cend and r < rows:
            col = M[r:, c]
            nz = np.nonzero(col)[0]
            if nz.size == 0:
                c += 1
                continue
            i = r + int(nz[0])
            if i != r:
                tmp = M[r].copy(); M[r] = M[i]; M[i] = tmp
                for mv in mults:
                    mv[r], mv[i] = mv[i], mv[r]
            iv = _inv(M[r, c], p)
            mv = np.zeros(rows)
            if r + 1 < rows:
                mv[r + 1:] = M[r + 1:, c] * iv % p
                sub = np.outer(mv[r + 1:], M[r, c:cend])
                M[r + 1:, c:cend] = (M[r + 1:, c:cend] - sub) % p
            mults.append(mv)
            pivcols.append(c)
            r += 1
            c += 1
        k = len(mults)
        if k == 0 or cend >= cols:
            continue
        # --- trailing update on columns cend.. ---
        L = np.empty((rows - r0, k))
        for m in range(k):
            L[:, m] = mults[m][r0:]
        Y = M[r0:r0 + k, cend:].copy()
        for m in range(k):
            if m:
                Y[m] = (Y[m] - L[m, :m] @ Y[:m]) % p
            # L[r0+m, m] entries below are used for the block update
        M[r0:r0 + k, cend:] = Y
        if rows > r0 + k:
            upd = L[k:, :] @ Y
            M[r0 + k:, cend:] = (M[r0 + k:, cend:] - upd) % p
    return r, pivcols


def solve(A, B, p, nb=NB):
    """A: (rows x cols) int array mod p;  B: (rows x nrhs) or (rows,)"""
    A = np.asarray(A)
    single = (B.ndim == 1)
    Bm = B.reshape(-1, 1) if single else B
    rows, cols = A.shape
    nrhs = Bm.shape[1]
    M = np.empty((rows, cols + nrhs))
    M[:, :cols] = np.asarray(A, dtype=np.float64) % p
    M[:, cols:] = np.asarray(Bm, dtype=np.float64) % p
    rank, pivcols = elim(M, p, cols, nb)
    # consistency: rows rank.. must be zero in the RHS
    nbad = int(np.count_nonzero(M[rank:, cols:] % p))
    # back substitution on the pivot columns (free unknowns = 0)
    X = np.zeros((cols, nrhs))
    U = M[:rank][:, pivcols]                     # rank x rank upper triangular
    R = M[:rank, cols:].copy()
    for i in range(rank - 1, -1, -1):
        if i + 1 < rank:
            R[i] = (R[i] - U[i, i + 1:] @ R[i + 1:]) % p
        R[i] = R[i] * _inv(U[i, i], p) % p
    for t, cc in enumerate(pivcols):
        X[cc] = R[t]
    X = X.astype(np.int64)
    if single: X = X[:, 0]
    return X, rank, pivcols, nbad


def rank_only(A, p, nb=NB):
    M = np.asarray(A, dtype=np.float64) % p
    M = M.copy()
    rank, piv = elim(M, p, A.shape[1], nb)
    return rank, piv
