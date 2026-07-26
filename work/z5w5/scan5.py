"""FREE-WEIGHT scan at weight 5 over the STANDALONE blocks.

For the fixed operator L = L_BZ the certificate system is linear in the WEIGHT
as well as in the cofactors, so instead of testing representatives one at a time
we solve for the weight and the certificate simultaneously (Z5CF_REP 1).

A block M is STANDALONE when every strict multiple of M in the closure basis is
maximal, hence fixed in closed form by Theorem R.  Its equation is then

      gk rho(k+1,l) - rho + gl sigma(k,l+1) - sigma  =  A_M(k,l) . w ,

A_M known, supported on the |up(M)| coordinates of w.  The admissible set is
{ w : A_M w in Im(Msc) } and, since Msc is the SAME matrix for every block, ONE
elimination of  [ Msc | A_{M_1} | ... | A_{M_B} ]  with pivots restricted to the
Msc columns serves all of them: the rows past the rank give, per block, a
condition matrix Z_M of at most |up(M)| independent rows.

    W_tel  =  { w : Z_M w|_{up(M)} = 0  for every standalone block M }.

ADEQUACY CALIBRATION built in: codim(block) = rank(Z_M).  If the ansatz is too
small, NOTHING is admissible and codim = |up(M)| exactly, for every block --
that is the signature Z5CF_REP 3.1 records ("dim 99 = 109-10").  A run in which
every codim equals |up(M)| is an ARTEFACT, not a result.
"""
import sys, os, time, pickle
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5w5')
import solve, fastlin, ratrec
import w5span as W
import pd5


def rowspace(Z, p):
    """basis of the row space of Z (few columns), as a list of rows."""
    R, piv, _ = solve.rref(Z.copy() % p, p)
    return R[:len(piv)], len(piv)


def run(n, dname, slack, p=pd5.P1, Wt=5, maxdeg=3, symbols=None, npts=None,
        seed=4242, verbose=True, ratio=1.40):
    B, T = W.span_w5(symbols, Wt, maxdeg)
    J = len(B)
    maxi, stand, coup, us = W.blocks(B)
    ans, dk, dl = pd5.ansatz(dname, slack)
    if npts is None:
        npts = int(ratio * ans.nc) + 400
    t0 = time.time()
    pd = pd5.PD5(p, n, npts, B, seed=seed)
    t1 = time.time()
    Msc = pd5.scal_mat(pd, ans)
    Acs = pd5.Acols_standalone(pd, B, stand, us)
    t2 = time.time()
    nc = ans.nc
    width = sum(A.shape[1] for _, _, A in Acs)
    G = np.empty((npts, nc + width))
    G[:, :nc] = Msc % p
    off = nc
    spans = []
    for j, cols, A in Acs:
        G[:, off:off + A.shape[1]] = A % p
        spans.append((j, cols, off, A.shape[1]))
        off += A.shape[1]
    del Msc
    rank, piv = fastlin.elim(G, p, nc)
    t3 = time.time()
    # per-block conditions
    conds = []
    codims = []
    byblock = {}
    for j, cols, o, wdt in spans:
        Z = G[rank:, o:o + wdt].astype(np.int64) % p
        if Z.shape[0] == 0:
            codims.append(0)
            continue
        R, cd = rowspace(Z, p)
        codims.append(cd)
        rows_j = []
        for i in range(cd):
            row = np.zeros(J, dtype=np.int64)
            row[cols] = R[i]
            conds.append(row)
            rows_j.append(row)
        byblock[j] = rows_j
    del G
    C = np.array(conds, dtype=np.int64) if conds else np.zeros((0, J), dtype=np.int64)
    ns = ratrec.nullspace(C, p) if C.shape[0] else [np.eye(J, dtype=np.int64)[i]
                                                   for i in range(J)]
    t4 = time.time()
    from collections import Counter
    cc = Counter(codims)
    upmax = max(len(us[j]) for j in stand)
    dead = cc.get(upmax, 0)
    if verbose:
        print('n=%d p=%d W=%d %s slack=%d bideg=(%d,%d) nc=%d J=%d blocks=%d '
              'rows=%d ratio=%.2f rank(Msc)=%d  [pd %.0fs sys %.0fs elim %.0fs ns %.0fs]'
              % (n, p, Wt, dname, slack, dk, dl, nc, J, len(stand), npts,
                 npts / (nc + upmax), rank, t1 - t0, t2 - t1, t3 - t2, t4 - t3),
              flush=True)
        print('   per-block codim histogram %s   (|up| = %d; codim == |up| means '
              'NOTHING admissible)' % (dict(sorted(cc.items())), upmax), flush=True)
        print('   blocks with codim == |up| : %d of %d  --> %s'
              % (dead, len(stand),
                 '*** ANSATZ TOO SMALL, result is an artefact ***' if dead == len(stand)
                 else 'ansatz responds'), flush=True)
        print('   >>> dim W_tel(n=%d) = %d   (of J = %d)' % (n, len(ns), J), flush=True)
    return dict(B=B, ns=ns, codims=codims, stand=stand, rank=rank, npts=npts,
                nc=nc, J=J, ans=ans, dead=dead, us=us, byblock=byblock)


def intersect(sp1, sp2, J, p):
    if sp1 is None:
        return sp2
    A = np.array(sp1, dtype=np.int64) % p
    Bm = np.array(sp2, dtype=np.int64) % p
    if A.shape[0] == 0 or Bm.shape[0] == 0:
        return []
    Ccat = np.concatenate([A.T % p, (-Bm.T) % p], axis=1)
    ker = ratrec.nullspace(Ccat, p)
    if not ker:
        return []
    rows = [(v[:A.shape[0]].astype(object) @ A.astype(object)) % p for v in ker]
    R, piv, _ = solve.rref(np.array(rows, dtype=np.int64) % p, p)
    return [R[i] for i in range(len(piv))]


if __name__ == '__main__':
    ns_ = [int(x) for x in sys.argv[1].split(',')]
    dname = sys.argv[2]
    slack = int(sys.argv[3])
    p = int(sys.argv[4]) if len(sys.argv) > 4 else pd5.P1
    Wt = int(sys.argv[5]) if len(sys.argv) > 5 else 5
    maxdeg = int(sys.argv[6]) if len(sys.argv) > 6 else 3
    tag = sys.argv[7] if len(sys.argv) > 7 else ''
    cur = None
    B = None
    for n in ns_:
        r = run(n, dname, slack, p=p, Wt=Wt, maxdeg=maxdeg)
        B = r['B']; J = r['J']
        cur = intersect(cur, r['ns'], J, p)
        print('   cumulative dim W_tel through n=%d : %d' % (n, len(cur)), flush=True)
        sys.stdout.flush()
    if B is not None:
        fn = 'Wcum_W%d_%s_s%d_p%d%s.pkl' % (Wt, dname, slack, p, tag)
        pickle.dump([np.array(x) for x in cur], open(fn, 'wb'))
        print('saved %s  (dim %d)' % (fn, len(cur)))
