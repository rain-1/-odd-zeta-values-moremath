"""The sum map  w |-> ( sum_{k,l=0}^n T(n,k,l) w(n,k,l) )_n  for ANY degree
(3 or 4) weight-5 bare span.

Two devices make degree 4 (J = 3325) affordable:

 (a) PREFIX GROUPING.  A monomial of degree d is (prefix of length d-1) * (last
     letter), and the prefix products are shared: PP3[(a,b,c)] = PP2[(a,b)]*Lv[c].
     Each degree contributes ONE matrix product (n_prefixes x ncells) @ (ncells x
     n_lastletters), so the whole design row costs
        (18*36 + 126*27 + 165*9) = 5535 multiply-adds per cell
     instead of enumerating 3325 monomials.

 (b) THE k <= l HALF GRID.  T(n,k,l) = T(n,l,k), so with
        half[j]  = sum_{k<=l} T M_j ,   diag[j] = sum_{k=l} T M_j
     one has, since sigma fixes the diagonal (n+k = n+l, n-k = n-l there),
        FULL[j] = half[j] + half[sigma j] - diag[j] .
     Halves the cell count.  [PROVED]

Exactness of the float64 accumulation: the left factor is split into two 11-bit
halves, so a single dgemm may accumulate up to 2^20 cells; cells are chunked.
"""
import sys, time
import numpy as np
import w5span as W

P1 = 4194301
P2 = 4194287
CHUNK = 100000


def hvals(r, xmax, p):
    out = np.zeros(xmax + 2, dtype=np.int64)
    s = 0
    for x in range(1, xmax + 2):
        s = (s + pow(pow(x, r, p), p - 2, p)) % p
        out[x] = s
    return out


def mm(A, B, p):
    """(A @ B.T) mod p, A: a x N, B: b x N int64 in [0,p), exact for N <= 2^20."""
    A1 = (A >> 11).astype(np.float64)
    A0 = (A & 2047).astype(np.float64)
    Bf = B.astype(np.float64)
    hi = (A1 @ Bf.T) % p
    lo = (A0 @ Bf.T) % p
    return ((hi * 2048.0) % p + lo).astype(np.int64) % p


class Plan:
    """prefix / last-letter tables for the span B"""
    def __init__(self, B):
        self.B = B
        self.idx = {m: j for j, m in enumerate(B)}
        self.letters = sorted({L for m in B for L in m})
        self.li = {L: i for i, L in enumerate(self.letters)}
        self.D = max(len(m) for m in B)
        self.pref = {}       # d -> {prefix tuple: row}
        self.last = {}       # d -> {letter: col}
        self.cells = {}      # d -> [(j, row, col)]
        for d in range(2, self.D + 1):
            pr, la, ce = {}, {}, []
            for m in B:
                if len(m) != d:
                    continue
                pfx = m[:d - 1]
                if pfx not in pr:
                    pr[pfx] = len(pr)
                if m[-1] not in la:
                    la[m[-1]] = len(la)
                ce.append((self.idx[m], pr[pfx], la[m[-1]]))
            self.pref[d], self.last[d], self.cells[d] = pr, la, ce
        self.deg1 = [(self.idx[(L,)], self.li[L]) for L in self.letters
                     if (L,) in self.idx]
        self.jzero = self.idx.get((), None)
        self.sig = np.array([self.idx[W.sigma_mono(m)] for m in B], dtype=np.int64)


def _accumulate(pl, Tg, Lv, p, acc):
    """add the contribution of one cell chunk to acc (length J)."""
    nc = Tg.size
    if pl.jzero is not None:
        acc[pl.jzero] = (acc[pl.jzero] + int(Tg.sum() % p)) % p
    TL = Tg[None, :] * Lv % p
    if pl.deg1:
        one = np.ones((1, nc), dtype=np.int64)
        M1 = mm(TL, one, p)
        for j, i in pl.deg1:
            acc[j] = (acc[j] + int(M1[i, 0])) % p
    PPprev = None
    for d in range(2, pl.D + 1):
        pr, la, ce = pl.pref[d], pl.last[d], pl.cells[d]
        PP = np.zeros((len(pr), nc), dtype=np.int64)
        for pfx, r in pr.items():
            if d == 2:
                PP[r] = TL[pl.li[pfx[0]]]
            else:
                PP[r] = PPprev[pl.pref[d - 1][pfx[:-1]]] * Lv[pl.li[pfx[-1]]] % p
        LS = np.zeros((len(la), nc), dtype=np.int64)
        for L, c in la.items():
            LS[c] = Lv[pl.li[L]]
        Mp = mm(PP, LS, p)
        for j, r, c in ce:
            acc[j] = (acc[j] + int(Mp[r, c])) % p
        PPprev = PP
    return acc


def design(B, N, p=P1, verbose=True, chunk=CHUNK):
    pl = Plan(B)
    J = len(B)
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
    A = np.zeros((N + 1, J), dtype=np.int64)
    t0 = time.time()
    nl = len(pl.letters)
    for n in range(N + 1):
        kk = np.arange(n + 1)
        Cnk = fact[n + kk] * inv[n] % p * inv[kk] % p
        Cn_k = fact[n] * inv[kk] % p * inv[n - kk] % p
        rowk = Cnk * Cn_k % p * Cn_k % p
        ii, jj = np.triu_indices(n + 1)                 # k <= l
        half = np.zeros(J, dtype=np.int64)
        diag = np.zeros(J, dtype=np.int64)
        for grid, acc in ((None, half), ('d', diag)):
            if grid is None:
                Kv, Lvv = ii, jj
            else:
                Kv = Lvv = kk
            tot = Kv.size
            for s in range(0, tot, chunk):
                K2 = Kv[s:s + chunk]; L2 = Lvv[s:s + chunk]
                Ckl = fact[n + K2 + L2] * inv[n] % p * inv[K2 + L2] % p
                Tg = rowk[K2] * rowk[L2] % p * Ckl % p
                Lvm = np.zeros((nl, K2.size), dtype=np.int64)
                for L in pl.letters:
                    r, a = W.LETTERS[L]
                    cn, ck, cl = W.ARGS[a]
                    Lvm[pl.li[L]] = Hs[r][cn * n + ck * K2 + cl * L2]
                _accumulate(pl, Tg, Lvm, p, acc)
        A[n] = (half + half[pl.sig] - diag) % p
        if verbose and n % 50 == 0:
            print('   n=%d  [%.0fs]' % (n, time.time() - t0), flush=True)
    return A


if __name__ == '__main__':
    sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
    import solve, ratrec
    N = int(sys.argv[1]); p = int(sys.argv[2]); Wt = int(sys.argv[3])
    md = int(sys.argv[4]); tag = sys.argv[5] if len(sys.argv) > 5 else ''
    B, T = W.span_w5(None, Wt, md)
    J = len(B)
    t0 = time.time()
    A = design(B, N, p)
    print('design %d x %d built in %.0fs (p=%d, W=%d, maxdeg=%d)'
          % (A.shape[0], J, time.time() - t0, p, Wt, md))
    np.save('Ad%d%s_p%d.npy' % (md, tag, p), A)
    if Wt == 5:
        w = np.array(W.el_to_vec(B, W.w5_el(), p), dtype=np.int64)
    else:
        w = np.array(W.el_to_vec(B, W.w3hat_el(), p), dtype=np.int64)
    b = (A.astype(object) @ w.astype(object) % p).astype(np.int64)
    np.save('bd%d%s_p%d.npy' % (md, tag, p), b)
    np.save('wd%d%s_p%d.npy' % (md, tag, p), w)
    _, piv, _ = solve.rref(A.copy(), p)
    print('rank of the sum map = %d  (excess rows %d) -> dim K = %d'
          % (len(piv), N + 1 - len(piv), J - len(piv)))
