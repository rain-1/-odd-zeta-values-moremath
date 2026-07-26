"""How small can the ansatz be and still solve the 18 letter blocks?
(Needed so that the JOINT solve  {18 letter blocks + () block}  -- which is what
resolves the trivial-pair / curl gauge freedom -- becomes affordable.)"""
import sys, os, time, pickle
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
os.chdir('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
import fastlin
from solve import Ansatz
import bare, frw, cert, extract

if __name__ == '__main__':
    n = int(sys.argv[1]); dname = sys.argv[2]
    p = frw.P; m = 3; maxdeg = 2
    B, tops = bare.span_w3(maxdeg=maxdeg)
    J = len(B)
    Wc = pickle.load(open('Wcum_m3_F1_s16_p%d_d2.pkl' % p, 'rb'))
    K = np.load('K_d2_p%d.npy' % p)
    wh = np.array(bare.el_to_vec(B, bare.w3hat_el(), p), dtype=np.int64)
    w, _ = extract.candidate(list(Wc), list(K), wh, p, J)
    maximal = [j for j in range(J) if len(bare.upset(B, B[j])) == 1]
    letters = [j for j in range(J) if len(B[j]) == 1 and j not in maximal]
    for slack in [int(x) for x in sys.argv[3].split(',')]:
        D = frw.dens(m)[dname]
        dk = sum(mu * abs(f[2]) for f, mu in D) + slack
        dl = sum(mu * abs(f[3]) for f, mu in D) + slack
        ans = Ansatz(D, D, dk, dl, dk, dl, force_k=0, force_l=0)
        npts = int(1.4 * ans.nc) + 40
        t0 = time.time()
        pd = frw.PD(p, n, m, npts, B, [1], seed=99)
        Msc = frw.scal_mat(pd, ans)
        rv = np.zeros((J, npts), dtype=np.int64); sv = np.zeros((J, npts), dtype=np.int64)
        for j in maximal:
            rv[j] = int(w[j]) * pd.RQ1 % p
            sv[j] = int(w[j]) * pd.SQ1 % p
        RHS = np.zeros((npts, len(letters)), dtype=np.int64)
        import family
        for c, j in enumerate(letters):
            RHS[:, c] = family.block_rhs(pd, w, B, maximal, B[j], rv, sv)
        X, rank, piv, _ = fastlin.solve(Msc, RHS, p)
        nb = []
        for c, j in enumerate(letters):
            r = (cert.mv(Msc, X[:, c], p) - RHS[:, c]) % p
            nb.append(int(np.count_nonzero(r)))
        print('slack %2d deg=(%d,%d) nc=%4d npts=%4d rank=%4d ker=%4d : '
              'blocks failing = %d / %d  [%.0fs]'
              % (slack, dk, dl, ans.nc, npts, rank, ans.nc - rank,
                 sum(1 for x in nb if x), len(letters), time.time() - t0), flush=True)
