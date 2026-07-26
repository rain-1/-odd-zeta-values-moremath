"""The sum-map  V -> (sequences in n),   w  |->  ( sum_{k,l=0}^n T(n,k,l) w(n,k,l) )_n
over the bare WEIGHT-5 span, its rank, its kernel K5, and the P row.

    T(n,k,l) = C(n+k,n) C(n,k)^2 C(n+l,n) C(n,l)^2 C(n+k+l,n)

Everything mod a large prime.  Exactness of the float64 BLAS accumulation is
guaranteed by splitting the left factor into two 11-bit halves, so a single
dgemm may accumulate up to 2^20 cells.
"""
import sys, time
import numpy as np
import w5span as W

P1 = 4194301
P2 = 4194287


def hvals(r, xmax, p):
    out = np.zeros(xmax + 2, dtype=np.int64)
    s = 0
    for x in range(1, xmax + 2):
        s = (s + pow(pow(x, r, p), p - 2, p)) % p
        out[x] = s
    return out


def mm(A, B, p):
    """(A @ B.T) mod p, A: a x N, B: b x N, both int64 in [0,p).  Exact for
    N <= 2^20 provided p < 2^22."""
    A1 = (A >> 11).astype(np.float64)
    A0 = (A & 2047).astype(np.float64)
    Bf = B.astype(np.float64)
    hi = (A1 @ Bf.T) % p
    lo = (A0 @ Bf.T) % p
    return ((hi * 2048.0) % p + lo).astype(np.int64) % p


def design(B, N, p=P1, verbose=True):
    """A[n, j] = sum_{k,l=0}^{n} T(n,k,l) * B[j](n,k,l)  mod p"""
    J = len(B)
    idx = {m: j for j, m in enumerate(B)}
    letters = sorted({L for m in B for L in m})
    nl = len(letters)
    li = {L: i for i, L in enumerate(letters)}
    xmax = 3 * N + 5
    Hs = {r: hvals(r, xmax, p) for r in range(1, W.WMAX + 1)}
    fmax = 4 * N + 8
    fact = np.ones(fmax + 1, dtype=np.int64)
    for i in range(1, fmax + 1):
        fact[i] = fact[i - 1] * i % p
    inv = np.ones(fmax + 1, dtype=np.int64)
    inv[fmax] = pow(int(fact[fmax]), p - 2, p)
    for i in range(fmax, 0, -1):
        inv[i - 1] = inv[i] * i % p

    # monomial groups
    g1 = [(idx[(L,)], li[L]) for L in letters if (L,) in idx]
    g2 = []          # (j, i1, i2)
    g3 = []          # (j, pairkey, i3)  handled below
    for m in B:
        if len(m) == 2:
            g2.append((idx[m], li[m[0]], li[m[1]]))
    # degree 3: group by the first two letters
    pairkeys = {}
    for m in B:
        if len(m) == 3:
            key = (m[0], m[1])
            if key not in pairkeys:
                pairkeys[key] = len(pairkeys)
            g3.append((idx[m], pairkeys[key], li[m[2]]))
    pk_list = [None] * len(pairkeys)
    for key, t in pairkeys.items():
        pk_list[t] = (li[key[0]], li[key[1]])
    jzero = idx[()] if () in idx else None

    A = np.zeros((N + 1, J), dtype=np.int64)
    t0 = time.time()
    for n in range(N + 1):
        kk = np.arange(n + 1)
        Cnk = fact[n + kk] * inv[n] % p * inv[kk] % p
        Cn_k = fact[n] * inv[kk] % p * inv[n - kk] % p
        rowk = Cnk * Cn_k % p * Cn_k % p
        K2, L2 = np.meshgrid(kk, kk, indexing='ij')
        Ckl = fact[n + K2 + L2] * inv[n] % p * inv[K2 + L2] % p
        Tg = (rowk[:, None] * rowk[None, :] % p * Ckl % p).ravel()
        nc = Tg.size
        Lv = np.zeros((nl, nc), dtype=np.int64)
        for L in letters:
            r, a = W.LETTERS[L]
            cn, ck, cl = W.ARGS[a]
            X = (cn * n + ck * K2 + cl * L2).ravel()
            Lv[li[L]] = Hs[r][X]
        acc = np.zeros(J, dtype=np.int64)
        if jzero is not None:
            acc[jzero] = int(Tg.sum() % p)
        TL = Tg[None, :] * Lv % p                      # nl x nc
        M1 = mm(TL[:, :].copy(), np.ones((1, nc), dtype=np.int64), p)
        for j, i in g1:
            acc[j] = M1[i, 0]
        M2 = mm(TL, Lv, p)                             # nl x nl
        for j, i1, i2 in g2:
            acc[j] = M2[i1, i2]
        if pk_list:
            PP = np.zeros((len(pk_list), nc), dtype=np.int64)
            for t, (i1, i2) in enumerate(pk_list):
                PP[t] = TL[i1] * Lv[i2] % p
            M3 = mm(PP, Lv, p)
            for j, t, i3 in g3:
                acc[j] = M3[t, i3]
        A[n] = acc
        if verbose and n % 50 == 0:
            print('   n=%d  [%.0fs]' % (n, time.time() - t0), flush=True)
    return A


if __name__ == '__main__':
    sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
    import solve, ratrec
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    p = int(sys.argv[2]) if len(sys.argv) > 2 else P1
    syms = None if (len(sys.argv) <= 3 or sys.argv[3] == '9') else W.SIX
    B, T = W.span_w5(syms)
    J = len(B)
    t0 = time.time()
    A = design(B, N, p)
    print('design %d x %d built in %.0fs (p=%d)' % (A.shape[0], J, time.time() - t0, p))
    _, piv, _ = solve.rref(A.copy(), p)
    rk = len(piv)
    print('rank of the sum-map = %d  ->  dim K5 = %d  (excess rows %d)'
          % (rk, J - rk, N + 1 - rk))
    w5 = np.array(W.el_to_vec(B, W.w5_el(), p), dtype=np.int64)
    b = (A.astype(object) @ w5.astype(object) % p).astype(np.int64)
    np.save('A5_p%d.npy' % p, A)
    np.save('b5_p%d.npy' % p, b)
    np.save('w5vec_p%d.npy' % p, w5)
    ns = ratrec.nullspace(A, p)
    np.save('K5_p%d.npy' % p, np.array(ns, dtype=np.int64))
    print('K5 basis saved: %d vectors in dimension %d' % (len(ns), J))
    # antisymmetric subspace must be inside K5
    anti = []
    seen = set()
    for j, m in enumerate(B):
        sm = W.sigma_mono(m)
        if sm == m or (m, sm) in seen or (sm, m) in seen:
            continue
        seen.add((m, sm))
        v = np.zeros(J, dtype=np.int64)
        v[j] = 1
        v[B.index(sm)] = p - 1
        anti.append(v)
    Aanti = (A.astype(object) @ np.array(anti, dtype=object).T % p)
    print('antisym directions: %d ; A @ antisym nonzero entries: %d'
          % (len(anti), int(np.count_nonzero(Aanti))))
