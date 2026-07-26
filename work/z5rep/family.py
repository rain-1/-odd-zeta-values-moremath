"""The () block over the WHOLE admissible representative family.

The 18 letter blocks are solved for every member of the affine family
   w(lam) = w_0 + sum_{i>=1} lam_i u_i ,   u_i a basis of W_tel & K,
and the resulting () -block right-hand side is LINEAR in lam.  So the question
"is there a member of the family for which the () block also closes?" is one
more instance of  { lam : A lam in Im(Msc) } -- one elimination.

Control (ansatz adequacy): the weight w = 1 (the Q row).  Its whole cascade must
close exactly; if it does not, the ansatz is too small and every other zero is
an artefact.
"""
import sys, os, time, pickle
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
os.chdir('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
import solve, fastlin, ratrec, o_scan
from solve import Ansatz
import bare, frw, cert, extract


def block_rhs(pd, w, B, maximal, mi, rv, sv):
    p = pd.p
    rhs = cert.Ewphi(pd, w, mi, B)
    for jj in maximal:
        rest = cert.divide(mi, B[jj])
        if rest is None:
            continue
        sk, sl = cert.shiftpair(pd, rest)
        rhs = (rhs - pd.gk * sk % p * rv[jj] - pd.gl * sl % p * sv[jj]) % p
    return rhs


def run(n, m, dname, slack, ws, B, p=frw.P, npts=None, seed=777, avec=None,
        verbose=True):
    """ws: list of weight vectors.  Returns the () -block A-matrix (npts x len(ws))
    and the admissible lam-subspace."""
    J = len(B)
    D = frw.dens(m)[dname]
    dk = sum(mu * abs(f[2]) for f, mu in D) + slack
    dl = sum(mu * abs(f[3]) for f, mu in D) + slack
    ans = Ansatz(D, D, dk, dl, dk, dl, force_k=0, force_l=0)
    if npts is None:
        npts = int(1.4 * ans.nc) + 40
    if avec is None:
        avec = [1] + [0] * (m - 3)
    nr = len(ans.mons_r)
    maximal = [j for j in range(J) if len(bare.upset(B, B[j])) == 1]
    idx = {mm: j for j, mm in enumerate(B)}
    zero_j = idx[()]
    letters = [j for j in range(J) if len(B[j]) == 1 and j not in maximal]
    t0 = time.time()
    pd = frw.PD(p, n, m, npts, B, avec, seed=seed)
    Msc = frw.scal_mat(pd, ans)
    R1, S1 = None, None
    R1m, R0m, S1m, S0m = cert.evalmats(pd, ans)
    nw = len(ws)
    # --- letter blocks for every weight, one elimination
    RHS = np.zeros((npts, nw * len(letters)), dtype=np.int64)
    RV = [np.zeros((J, npts), dtype=np.int64) for _ in range(nw)]
    SV = [np.zeros((J, npts), dtype=np.int64) for _ in range(nw)]
    for a, w in enumerate(ws):
        for j in maximal:
            RV[a][j] = int(w[j]) * pd.RQ1 % p
            SV[a][j] = int(w[j]) * pd.SQ1 % p
        for c, j in enumerate(letters):
            RHS[:, a * len(letters) + c] = block_rhs(pd, w, B, maximal, B[j],
                                                     RV[a], SV[a])
    X, rank, piv, _ = fastlin.solve(Msc, RHS, p)
    nbadL = 0
    for a in range(nw):
        for c, j in enumerate(letters):
            col = a * len(letters) + c
            resid = (cert.mv(Msc, X[:, col], p) - RHS[:, col]) % p
            nbadL += int(np.count_nonzero(resid))
            RV[a][j] = cert.mv(R1m, X[:nr, col], p)
            SV[a][j] = cert.mv(S1m, X[nr:, col], p)
    # --- the () block RHS for every weight
    A = np.zeros((npts, nw), dtype=np.int64)
    for a, w in enumerate(ws):
        rhs = cert.Ewphi(pd, w, (), B)
        for jj in range(J):
            if jj == zero_j:
                continue
            sk, sl = cert.shiftpair(pd, B[jj])
            rhs = (rhs - pd.gk * sk % p * RV[a][jj] - pd.gl * sl % p * SV[a][jj]) % p
        A[:, a] = rhs
    subs, rk = o_scan.asubspaces(Msc, [A], p)
    lam = subs[0]
    if verbose:
        print('n=%d m=%d %s slack=%d nc=%d npts=%d ratio=%.2f rank(Msc)=%d '
              'letter-block residuals=%d  [%.0fs]'
              % (n, m, dname, slack, ans.nc, npts, npts / (ans.nc + nw), rk,
                 nbadL, time.time() - t0), flush=True)
        print('    () -block admissible lam-directions: %d of %d' % (len(lam), nw),
              flush=True)
    return dict(lam=lam, A=A, Msc=Msc, ans=ans, pd=pd, npts=npts, nbadL=nbadL,
                rank=rk)


if __name__ == '__main__':
    m = int(sys.argv[1]); dname = sys.argv[2]; slack = int(sys.argv[3])
    p = int(sys.argv[4]); maxdeg = int(sys.argv[5])
    ns = [int(x) for x in sys.argv[6].split(',')]
    cslack = int(sys.argv[7]) if len(sys.argv) > 7 else slack
    B, tops = bare.span_w3(maxdeg=maxdeg)
    J = len(B)
    Wc = pickle.load(open('Wcum_m%d_%s_s%d_p%d_d%d.pkl' % (m, dname, slack, p, maxdeg), 'rb'))
    K = np.load('K_d%d_p%d.npy' % (maxdeg, p))
    wh = np.array(bare.el_to_vec(B, bare.w3hat_el(), p), dtype=np.int64)
    w0, nb = extract.candidate(list(Wc), list(K), wh, p, J)
    free = extract.wk_basis(list(Wc), list(K), p)
    ws = [w0] + [np.array(u, dtype=np.int64) for u in free]
    # control: the constant weight  w = 1  (the Q row) -- its cascade must close
    ctrl = np.zeros(J, dtype=np.int64); ctrl[B.index(())] = 1
    print('family size %d (1 base + %d free directions)' % (len(ws), len(free)))
    nw = len(ws)
    cur = None
    for n in ns:
        rc = run(n, m, dname, cslack, [ctrl], B, p=p)
        print('    CONTROL w=1 (Q row): () -block admissible = %s   %s'
              % (len(rc['lam']), 'ansatz ADEQUATE' if rc['lam'] else
                 '*** ANSATZ TOO SMALL -- zeros below are artefacts ***'), flush=True)
        r = run(n, m, dname, cslack, ws, B, p=p)
        lam = r['lam']
        cur = lam if cur is None else o_scan.intersect([cur, lam], nw, p)
        good = [v for v in cur if v[0] % p]
        print('    cumulative lam-space through n=%d : dim %d ; with lam_0 != 0 : %s'
              % (n, len(cur), 'YES -> CERTIFICATE CANDIDATE' if good else
                 'NO member of the family closes ()'), flush=True)
        if good:
            v = good[0]
            iv = pow(int(v[0]) % p, p - 2, p)
            wnew = np.zeros(J, dtype=np.int64)
            for a in range(nw):
                wnew = (wnew + int(v[a]) * iv % p * ws[a]) % p
            np.save('wgood_m%d_%s_s%d_p%d_d%d.npy' % (m, dname, cslack, p, maxdeg), wnew)
            pickle.dump(dict(lam=[np.array(x) for x in cur], ws=ws),
                        open('lamcum_m%d_%s_s%d_p%d_d%d.pkl' % (m, dname, cslack, p, maxdeg), 'wb'))
            print('    saved wgood (support %d)' % int(np.count_nonzero(wnew)), flush=True)
        sys.stdout.flush()
