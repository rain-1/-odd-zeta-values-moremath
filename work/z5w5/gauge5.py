"""The standalone-block scan WITH the MAXIMAL blocks' trivial-pair (curl) gauge
freedom offered to each block.

Theorem R fixes a maximal block's cofactor pair only up to a CURL
    (rho, sigma)  with  gk rho(k+1,l) - rho + gl sigma(k,l+1) - sigma = 0,
i.e. up to  ker(Msc).  Taking the Theorem-R particular solution throws that
freedom away and can only SHRINK the admissible weight space -- which is exactly
the trap Z5CF_REP 4.1 records at weight 3 (where 5832 gauge columns of rank 106
were the whole difference between NO and YES).

Here every standalone block M is offered the full curl freedom of ALL of its
maximal multiples, with the freedoms treated as INDEPENDENT per block.  That is
a RELAXATION of the true system (a maximal monomial divides up to three
standalone blocks and must use one curl for all of them), so the admissible
space computed here CONTAINS the true one:  a negative here is a negative for
the true system, within the stated ansatz bound on the curls.

The curl contribution of the maximal block M*L into the M-block equation is
    gk inc_k(L) rho(k+1,l) + gl inc_l(L) sigma(k,l+1)
which depends only on the LETTER L, so one basis  KR = R1 H_r, KS = S1 H_s  of
the curl images serves every block, and the nine letters of the complementary
weight give  9 * nk  extra columns.
"""
import sys, os, time, pickle
from collections import Counter
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5w5')
import solve, fastlin, ratrec
import w5span as W
import pd5
import scan5


def kernel_basis(Msc, p):
    """basis of ker(Msc) as an (nk x nc) integer matrix."""
    rank, piv = fastlin.rank_only(Msc, p)
    nc = Msc.shape[1]
    free = [c for c in range(nc) if c not in set(piv)]
    if not free:
        return np.zeros((0, nc), dtype=np.int64), rank
    RHS = (-Msc[:, free]) % p
    X, rk2, piv2, nbad = fastlin.solve(Msc, RHS, p)
    H = np.zeros((len(free), nc), dtype=np.int64)
    for t, f in enumerate(free):
        H[t] = X[:, t] % p
        H[t, f] = 1
    return H, rank


def matmul(A, Bm, p):
    out = np.zeros((A.shape[0], Bm.shape[1]), dtype=np.int64)
    blk = 400
    for i in range(0, A.shape[1], blk):
        out = (out + (A[:, i:i + blk].astype(np.float64)
                      @ Bm[i:i + blk].astype(np.float64)).astype(np.int64)) % p
    return out


def run(n, dname, slack, p=pd5.P1, Wt=5, maxdeg=3, symbols=None, npts=None,
        seed=909, verbose=True, ratio=1.32, groups=None):
    B, T = W.span_w5(symbols, Wt, maxdeg)
    J = len(B)
    maxi, stand, coup, us = W.blocks(B)
    ans, dk, dl = pd5.ansatz(dname, slack)
    nc = ans.nc
    nr = len(ans.mons_r)
    syms = W.ARGORDER if symbols is None else list(symbols)
    # group standalone blocks by the WEIGHT of their complementary letter
    bygrp = {}
    for j in stand:
        wc = 5 - sum(W.LWT[L] for L in B[j])
        bygrp.setdefault(wc, []).append(j)
    if groups is not None:
        bygrp = {k: v for k, v in bygrp.items() if k in groups}
    # kernel needs the same point set as the elimination
    t0 = time.time()
    probe_pts = int(1.4 * nc) + 200
    pdk = pd5.PD5(p, n, probe_pts, B, seed=seed + 1)
    Mk = pd5.scal_mat(pdk, ans)
    H, rank0 = kernel_basis(Mk, p)
    nk = H.shape[0]
    del Mk, pdk
    if npts is None:
        npts = int(ratio * (nc + 9 * nk + 12)) + 200
    if verbose:
        print('n=%d p=%d %s slack=%d nc=%d rank(Msc)=%d ker=%d ; gauge cols/blk=%d'
              ' ; rows=%d  [%.0fs]'
              % (n, p, dname, slack, nc, rank0, nk, 9 * nk, npts, time.time() - t0),
              flush=True)
    pd = pd5.PD5(p, n, npts, B, seed=seed)
    Msc = pd5.scal_mat(pd, ans)
    R1, R0, S1, S0 = pd5.evalmats(pd, ans)
    KR = matmul(R1, np.ascontiguousarray(H[:, :nr].T), p)     # npts x nk
    KS = matmul(S1, np.ascontiguousarray(H[:, nr:].T), p)
    del R1, R0, S1, S0
    Acs = {j: (cols, A) for j, cols, A in pd5.Acols_standalone(pd, B, stand, us)}
    out_conds = []
    out_codims = {}
    for wc, blks in sorted(bygrp.items()):
        letters = [W.lname(wc, a) for a in syms]
        ng = len(letters)
        width = ng * nk
        awidth = sum(Acs[j][1].shape[1] for j in blks)
        G = np.empty((npts, nc + width + awidth))
        G[:, :nc] = Msc % p
        for t, L in enumerate(letters):
            i = pd.li[L]
            sk = pd.inck[:, i]; sl = pd.incl[:, i]
            col = ((pd.gk * sk % p)[:, None] * KR + (pd.gl * sl % p)[:, None] * KS) % p
            G[:, nc + t * nk: nc + (t + 1) * nk] = col
        off = nc + width
        spans = []
        for j in blks:
            cols, A = Acs[j]
            G[:, off:off + A.shape[1]] = A % p
            spans.append((j, cols, off, A.shape[1]))
            off += A.shape[1]
        t1 = time.time()
        rank, piv = fastlin.elim(G, p, nc + width)
        cc = Counter()
        for j, cols, o, wdt in spans:
            Z = G[rank:, o:o + wdt].astype(np.int64) % p
            if Z.shape[0] == 0:
                cc[0] += 1; out_codims[j] = 0; continue
            R, cd = scan5.rowspace(Z, p)
            cc[cd] += 1
            out_codims[j] = cd
            for i in range(cd):
                row = np.zeros(J, dtype=np.int64)
                row[cols] = R[i]
                out_conds.append(row)
        del G
        if verbose:
            print('   complementary weight %d : %d blocks, gauge %d cols, '
                  'rank[Msc|G] = %d (was %d, +%d) ; codim histogram %s  [%.0fs]'
                  % (wc, len(blks), width, rank, rank0, rank - rank0,
                     dict(sorted(cc.items())), time.time() - t1), flush=True)
    C = (np.array(out_conds, dtype=np.int64) if out_conds
         else np.zeros((0, J), dtype=np.int64))
    ns = ratrec.nullspace(C, p) if C.shape[0] else [np.eye(J, dtype=np.int64)[i]
                                                   for i in range(J)]
    if verbose:
        print('   >>> dim W_tel^gauge(n=%d) = %d  (of J = %d)' % (n, len(ns), J),
              flush=True)
    return dict(ns=ns, codims=out_codims, B=B)


if __name__ == '__main__':
    ns_ = [int(x) for x in sys.argv[1].split(',')]
    dname = sys.argv[2]; slack = int(sys.argv[3])
    p = int(sys.argv[4]) if len(sys.argv) > 4 else pd5.P1
    tag = sys.argv[5] if len(sys.argv) > 5 else ''
    grps = None
    if len(sys.argv) > 6:
        grps = [int(x) for x in sys.argv[6].split(',')]
    cur = None
    for n in ns_:
        r = run(n, dname, slack, p=p, groups=grps)
        cur = scan5.intersect(cur, r['ns'], len(r['B']), p)
        print('   cumulative dim W_tel^gauge through n=%d : %d' % (n, len(cur)),
              flush=True)
    fn = 'Wgauge_W5_%s_s%d_p%d%s.pkl' % (dname, slack, p, tag)
    pickle.dump([np.array(x) for x in cur], open(fn, 'wb'))
    print('saved %s (dim %d)' % (fn, len(cur)))
