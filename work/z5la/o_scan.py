"""Order-m telescoper scan,  L = A . L_BZ,  A = sum_{t=0}^{m-3} a_t S_n^t.

STRUCTURE EXPLOITED.  (S^k)_{ij} != 0  iff  M_i divides M_j.  With the supp(w)
blocks fixed in closed form by Theorem R, seven of the eight residual weight-3
blocks -- the six single-letter blocks and ('u2',) -- have equations that involve
ONLY their own cofactor pair and Theorem-R-fixed blocks.  Each is therefore a
STANDALONE scalar problem, linear in the unknowns (r_i, s_i, a_0..a_{m-3}):

        gk r_i(k+1,l) - r_i + gl s_i(k,l+1) - s_i  +  A_i(k,l) . a  =  0.

For each block the set of admissible a is  { a : A_i a in Im(M_i) }, obtained
exactly by eliminating [M_i | A_i] with pivots restricted to the M_i columns and
taking the null space of the leftover (rows-rank) x (m-2) block.  A telescoper
needs a NONZERO a in the intersection over all seven blocks -- a necessary
condition, decided by a system of size (npts x nc) per block instead of the full
(J*npts x 8*nc) joint system.
"""
import sys, time
import numpy as np
import zla, solve, fastlin, ratrec, ordm
from solve import Ansatz, dval, dstr

P = 4194301
P2 = 4194287


def scal_mat(pd, ans):
    """the scalar operator matrix  gk r(k+1,l) - r + gl s(k,l+1) - s  in the
    ansatz basis.  IDENTICAL for every standalone block -- only A_i differs."""
    p, n, npts = pd.p, pd.n, pd.npts
    nc, nr = ans.nc, len(ans.mons_r)
    M = np.zeros((npts, nc), dtype=np.int64)
    dmax = max(max(a, b) for a, b in ans.mons_r + ans.mons_s) + 2
    for t, (k, l) in enumerate(pd.pts):
        gk = int(pd.gk[t]); gl = int(pd.gl[t])
        iDr = pow(dval(ans.Dr, n, k, l, p), p - 2, p)
        iDrk = pow(dval(ans.Dr, n, k + 1, l, p), p - 2, p)
        iDs = pow(dval(ans.Ds, n, k, l, p), p - 2, p)
        iDsl = pow(dval(ans.Ds, n, k, l + 1, p), p - 2, p)
        kp = [pow(k % p, a, p) for a in range(dmax)]
        lp = [pow(l % p, b, p) for b in range(dmax)]
        k1 = [pow((k + 1) % p, a, p) for a in range(dmax)]
        l1 = [pow((l + 1) % p, b, p) for b in range(dmax)]
        for u, (a, b) in enumerate(ans.mons_r):
            M[t, u] = (gk * k1[a] % p * lp[b] % p * iDrk - kp[a] * lp[b] % p * iDr) % p
        for u, (a, b) in enumerate(ans.mons_s):
            M[t, nr + u] = (gl * kp[a] % p * l1[b] % p * iDsl - kp[a] * lp[b] % p * iDs) % p
    return M


def asubspaces(M, As, p, nb=64):
    """for each A in As, { a : A a in Im(M) }.  One elimination for all."""
    rows, nc = M.shape
    na = As[0].shape[1]
    nA = len(As)
    G = np.empty((rows, nc + nA * na))
    G[:, :nc] = M % p
    for t, A in enumerate(As):
        G[:, nc + t * na: nc + (t + 1) * na] = A % p
    rank, piv = fastlin.elim(G, p, nc, nb)
    out = []
    for t in range(nA):
        Z = (G[rank:, nc + t * na: nc + (t + 1) * na].astype(np.int64)) % p
        if Z.shape[0] == 0:
            ns = [np.eye(na, dtype=np.int64)[j] for j in range(na)]
        else:
            ns = ratrec.nullspace(Z, p)
        out.append(ns)
    return out, rank


def intersect(subs, na, p):
    """intersection of a list of subspaces given by spanning sets."""
    cur = np.eye(na, dtype=np.int64)          # rows = basis of current space
    for ns in subs:
        if not ns:
            return []
        B = np.array(ns, dtype=np.int64) % p  # rows span the block's subspace
        # intersection: solve  x^T cur = y^T B  -> nullspace of [cur^T | -B^T]
        Ccat = np.concatenate([cur.T % p, (-B.T) % p], axis=1)
        kerv = ratrec.nullspace(Ccat, p)
        if not kerv: return []
        newrows = []
        for v in kerv:
            newrows.append((v[:cur.shape[0]] @ cur) % p)
        Rr = np.array(newrows, dtype=np.int64) % p
        # row-reduce to a basis
        Rr, piv, _ = solve.rref(Rr.copy(), p)
        Rr = Rr[:len(piv)]
        if Rr.shape[0] == 0: return []
        cur = Rr
    return [cur[j] for j in range(cur.shape[0])]


# ------------------------------------------------------------ ansatz zoo ----

def dens(m):
    K1, L1, KL1, KL2, KL3 = ordm.K1, ordm.L1, ordm.KL1, ordm.KL2, ordm.KL3
    NK, NL, NKL, MK, ML = ordm.NK, ordm.NL, ordm.NKL, ordm.MK, ordm.ML
    core = [(KL1, 1), (KL2, 1)] + [(NK[j], 1) for j in range(1, m + 1)] \
        + [(NL[j], 1) for j in range(1, m + 1)]
    out = {}
    out['E1'] = [(K1, 1), (L1, 1)] + core
    out['E2'] = [(K1, 1), (L1, 1), (KL1, 2), (KL2, 2)] \
        + [(NK[j], 2) for j in range(1, m + 1)] + [(NL[j], 2) for j in range(1, m + 1)]
    out['E3'] = [(K1, 3), (L1, 3), (KL1, 1), (KL2, 1), (KL3, 1)] \
        + [(NK[j], 1) for j in range(1, m + 2)] + [(NL[j], 1) for j in range(1, m + 2)] \
        + [(NKL[j], 1) for j in range(1, m + 1)]
    out['E4'] = [(K1, 1), (L1, 1)] + core \
        + [(MK[j], 1) for j in range(0, m + 1)] + [(ML[j], 1) for j in range(0, m + 1)]
    # families sized for the () block, whose right-hand side carries the
    # denominators of the seven blocks solved before it, shifted by one
    K2, L2, KL4 = ordm.K2, ordm.L2, ordm.KL4
    out['Z0'] = [(K1, 2), (L1, 2), (KL1, 2), (KL2, 2)] \
        + [(NK[j], 2) for j in range(1, m + 2)] + [(NL[j], 2) for j in range(1, m + 2)]
    out['Z1'] = [(K1, 4), (K2, 2), (L1, 4), (L2, 2), (KL1, 3), (KL2, 2), (KL3, 2)] \
        + [(NK[j], 2) for j in range(1, m + 2)] + [(NL[j], 2) for j in range(1, m + 2)]
    out['Z2'] = [(K1, 4), (K2, 2), (L1, 4), (L2, 2), (KL1, 3), (KL2, 3), (KL3, 2), (KL4, 1)] \
        + [(NK[j], 3) for j in range(1, m + 2)] + [(NL[j], 3) for j in range(1, m + 2)]
    # Z3 = exactly the MEASURED denominator of the () right-hand side
    out['Z3'] = [(K1, 2), (L1, 2), (KL1, 1), (KL2, 1), (KL3, 1)] \
        + [(NK[j], 2) for j in range(1, m + 1)] + [(NL[j], 2) for j in range(1, m + 1)]
    out['Z4'] = [(K1, 3), (L1, 3), (KL1, 2), (KL2, 2), (KL3, 2), (KL4, 1)] \
        + [(NK[j], 2) for j in range(1, m + 2)] + [(NL[j], 2) for j in range(1, m + 2)]
    return out


def run(which, n, m, dname, slack, npts=None, p=P, blocks=None, verbose=True):
    D = dens(m)[dname]
    dk0 = sum(mu * abs(f[2]) for f, mu in D)
    dl0 = sum(mu * abs(f[3]) for f, mu in D)
    dk, dl = dk0 + slack, dl0 + slack
    ans = Ansatz(D, D, dk, dl, dk, dl, force_k=0, force_l=0)
    na = m - 2
    if npts is None:
        npts = int(1.35 * (ans.nc + na)) + 20
    t0 = time.time()
    pd = ordm.PDm(which, p, n, m, npts)
    Acol = ordm.acols(pd)
    if blocks is None:
        blocks = [j for j in pd.free if len(pd.B[j]) > 0]      # the 7 standalone
    M = scal_mat(pd, ans)
    As = [Acol[i * npts:(i + 1) * npts] for i in blocks]
    subs, rank = asubspaces(M, As, p)
    info = [(str(pd.B[i]), rank, len(subs[t])) for t, i in enumerate(blocks)]
    inter = intersect(subs, na, p)
    if verbose:
        print('%s n=%d m=%2d %s deg=(%d,%d) nc=%d rows=%d ratio=%.2f  [%.0fs]'
              % (which, n, m, dname, dk, dl, ans.nc, npts,
                 npts / (ans.nc + na), time.time() - t0), flush=True)
        print('    ' + '  '.join('%s:rk%d,dim%d' % t for t in info), flush=True)
        print('    >>> COMMON a-directions: %d %s' % (len(inter),
              '  *** TELESCOPER CANDIDATE ***' if len(inter) else ''), flush=True)
    return dict(m=m, dname=dname, nc=ans.nc, npts=npts, info=info,
                inter=inter, na=na, ans=ans, pd=pd, Acol=Acol)


if __name__ == '__main__':
    which = sys.argv[1]; n = int(sys.argv[2]); dname = sys.argv[3]
    slack = int(sys.argv[4]); ms = [int(x) for x in sys.argv[5:]]
    for m in ms:
        run(which, n, m, dname, slack)
