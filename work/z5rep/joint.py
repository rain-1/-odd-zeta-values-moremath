"""JOINT solve of the 18 letter blocks AND the () block, with the letter blocks'
full TRIVIAL-PAIR (curl) gauge freedom offered to the () block.

Cascading block by block and taking the canonical solution in each letter block
throws away  dim ker(Msc)  directions per block -- pairs (rho,sigma) with
   gk rho(k+1,l) - rho + gl sigma(k,l+1) - sigma = 0
which still solve the letter block but change the () block's right-hand side.
Here they are kept:  unknowns are  x_0 (the ()-cofactor), h_j in ker(Msc) for
each of the 18 letter blocks, and lam (the position inside the admissible
representative family).  One elimination decides.
"""
import sys, os, time, pickle
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
os.chdir('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
import fastlin, ratrec, o_scan, solve
from solve import Ansatz
import bare, frw, cert, extract, family


def kernel_basis(pd, ans, p):
    """basis of { (rho,sigma) in the ansatz : gk rho(k+1,l)-rho+gl sigma(k,l+1)-sigma = 0 }"""
    Msc = frw.scal_mat(pd, ans)
    ns = ratrec.nullspace(Msc, p)
    return np.array(ns, dtype=np.int64) if ns else np.zeros((0, ans.nc), dtype=np.int64)


def run(n, ws, B, slackL, slack0, dname='F1', p=frw.P, m=3, ratio=1.32,
        verbose=True):
    J = len(B)
    D = frw.dens(m)[dname]
    dk0 = sum(mu * abs(f[2]) for f, mu in D)
    dl0 = sum(mu * abs(f[3]) for f, mu in D)
    ansL = Ansatz(D, D, dk0 + slackL, dl0 + slackL, dk0 + slackL, dl0 + slackL,
                  force_k=0, force_l=0)
    ans0 = Ansatz(D, D, dk0 + slack0, dl0 + slack0, dk0 + slack0, dl0 + slack0,
                  force_k=0, force_l=0)
    maximal = [j for j in range(J) if len(bare.upset(B, B[j])) == 1]
    letters = [j for j in range(J) if len(B[j]) == 1 and j not in maximal]
    idx = {mm: j for j, mm in enumerate(B)}
    zero_j = idx[()]
    nw = len(ws)
    avec = [1] + [0] * (m - 3)
    # ---- 1. the letter ansatz kernel, measured on its own point set
    nptsL = int(1.4 * ansL.nc) + 60
    pdL = frw.PD(p, n, m, nptsL, B, avec, seed=1234)
    t0 = time.time()
    H = kernel_basis(pdL, ansL, p)
    nk = H.shape[0]
    MscL = frw.scal_mat(pdL, ansL)
    # canonical particular solutions of the 18 letter blocks
    rvL = np.zeros((J, nptsL), dtype=np.int64); svL = np.zeros((J, nptsL), dtype=np.int64)
    XP = np.zeros((ansL.nc, nw * len(letters)), dtype=np.int64)
    nbadL = 0
    RHS = np.zeros((nptsL, nw * len(letters)), dtype=np.int64)
    for a, w in enumerate(ws):
        for j in maximal:
            rvL[j] = int(w[j]) * pdL.RQ1 % p
            svL[j] = int(w[j]) * pdL.SQ1 % p
        for c, j in enumerate(letters):
            RHS[:, a * len(letters) + c] = family.block_rhs(pdL, w, B, maximal,
                                                            B[j], rvL, svL)
    XP, rkL, piv, _ = fastlin.solve(MscL, RHS, p)
    for col in range(RHS.shape[1]):
        r = (cert.mv(MscL, XP[:, col], p) - RHS[:, col]) % p
        nbadL += int(np.count_nonzero(r))
    # ---- 2. the () system on a big fresh point set
    ncols = ans0.nc + len(letters) * nk + nw
    npts0 = int(ratio * ncols) + 40
    pd0 = frw.PD(p, n, m, npts0, B, avec, seed=555)
    Msc0 = frw.scal_mat(pd0, ans0)
    R1L, R0L, S1L, S0L = cert.evalmats(pd0, ansL)
    nrL = len(ansL.mons_r)
    if verbose:
        print('n=%d  letters: nc=%d rank=%d ker=%d nbad=%d ; () : nc=%d '
              'cols=%d rows=%d ratio=%.2f  [%.0fs]'
              % (n, ansL.nc, rkL, nk, nbadL, ans0.nc, ncols, npts0,
                 npts0 / ncols, time.time() - t0), flush=True)
    # per-letter-block shift coefficients into the () row
    G = np.zeros((npts0, len(letters) * nk), dtype=np.int64)
    Hr = np.ascontiguousarray(H[:, :nrL].T)      # nrL x nk
    Hs = np.ascontiguousarray(H[:, nrL:].T)
    KR = np.zeros((npts0, nk), dtype=np.int64)
    KS = np.zeros((npts0, nk), dtype=np.int64)
    for c in range(0, nk, 64):
        KR[:, c:c + 64] = matmul(R1L, Hr[:, c:c + 64], p)
        KS[:, c:c + 64] = matmul(S1L, Hs[:, c:c + 64], p)
    for c, j in enumerate(letters):
        sk, sl = cert.shiftpair(pd0, B[j])
        G[:, c * nk:(c + 1) * nk] = ((pd0.gk * sk % p)[:, None] * KR
                                     + (pd0.gl * sl % p)[:, None] * KS) % p
    # the () RHS for each weight, with the canonical letter solutions in place
    A = np.zeros((npts0, nw), dtype=np.int64)
    for a, w in enumerate(ws):
        rv = np.zeros((J, npts0), dtype=np.int64); sv = np.zeros((J, npts0), dtype=np.int64)
        for j in maximal:
            rv[j] = int(w[j]) * pd0.RQ1 % p
            sv[j] = int(w[j]) * pd0.SQ1 % p
        for c, j in enumerate(letters):
            col = a * len(letters) + c
            rv[j] = cert.mv(R1L, XP[:nrL, col], p)
            sv[j] = cert.mv(S1L, XP[nrL:, col], p)
        rhs = cert.Ewphi(pd0, w, (), B)
        for jj in range(J):
            if jj == zero_j:
                continue
            sk, sl = cert.shiftpair(pd0, B[jj])
            rhs = (rhs - pd0.gk * sk % p * rv[jj] - pd0.gl * sl % p * sv[jj]) % p
        A[:, a] = rhs
    # solve:  [ Msc0 | G ] z = A lam  consistent for which lam?
    LHS = np.concatenate([Msc0, G], axis=1)
    subs, rk = o_scan.asubspaces(LHS, [A], p)
    lam = subs[0]
    if verbose:
        print('   rank[Msc0|G] = %d of %d cols ; admissible lam-directions: %d of %d'
              % (rk, LHS.shape[1], len(lam), nw), flush=True)
    return lam, nbadL


def matmul(Aa, Bb, p):
    out = np.zeros((Aa.shape[0], Bb.shape[1]), dtype=np.int64)
    blk = 400
    for i in range(0, Aa.shape[1], blk):
        out = (out + (Aa[:, i:i + blk].astype(np.float64)
                      @ Bb[i:i + blk].astype(np.float64)).astype(np.int64)) % p
    return out


if __name__ == '__main__':
    ns = [int(x) for x in sys.argv[1].split(',')]
    slackL = int(sys.argv[2]); slack0 = int(sys.argv[3])
    p = int(sys.argv[4]) if len(sys.argv) > 4 else frw.P
    B, tops = bare.span_w3(maxdeg=2)
    J = len(B)
    Wc = pickle.load(open('Wcum_m3_F1_s16_p%d_d2.pkl' % p, 'rb'))
    K = np.load('K_d2_p%d.npy' % p)
    wh = np.array(bare.el_to_vec(B, bare.w3hat_el(), p), dtype=np.int64)
    w0, _ = extract.candidate(list(Wc), list(K), wh, p, J)
    free = extract.wk_basis(list(Wc), list(K), p)
    ws = [w0] + [np.array(u, dtype=np.int64) for u in free]
    ctrl = np.zeros(J, dtype=np.int64); ctrl[B.index(())] = 1
    cur = None
    for n in ns:
        if n == ns[0]:
            lc, _ = run(n, [ctrl], B, slackL, slack0, p=p)
            print('   CONTROL w=1 : %s' % ('ansatz ADEQUATE' if lc else
                                           '*** TOO SMALL ***'), flush=True)
        lam, nb = run(n, ws, B, slackL, slack0, p=p)
        cur = lam if cur is None else o_scan.intersect([cur, lam], len(ws), p)
        good = [v for v in cur if v[0] % p]
        print('   >>> cumulative through n=%d : dim %d ; lam_0 != 0 : %s'
              % (n, len(cur), 'YES  *** FULL CERTIFICATE EXISTS ***' if good else 'NO'),
              flush=True)
        if good:
            v = good[0]; iv = pow(int(v[0]) % p, p - 2, p)
            wn = np.zeros(J, dtype=np.int64)
            for a in range(len(ws)):
                wn = (wn + int(v[a]) * iv % p * ws[a]) % p
            np.save('wjoint_p%d.npy' % p, wn)
            print('   saved wjoint, support %d' % int(np.count_nonzero(wn)), flush=True)
        sys.stdout.flush()
