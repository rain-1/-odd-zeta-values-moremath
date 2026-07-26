"""The BOUNDARY certificate, in the (B-bot)-satisfying gauge.

Z5_ORDER0 §7: Phi is k<->l symmetric, so the two bottom-boundary sums collapse to

    Sum_{j=0}^{n+3} Phi(n,0,j) * R(n,j) = 0 ,   R(n,j) = rho_()(n,0,j) + sigma_()(n,j,0)

and this telescopes with  G(n,j) = Phi(n,0,j) * u(n,j),  u = Nu/[(j+1)(n+j+1)(n+j+2)(n+j+3)]:

    g(j) u(n,j+1) - u(n,j) = R(n,j) ,   g(j) = Phi(n,0,j+1)/Phi(n,0,j)
                                             = (n+3-j)^2 (n+j+1)^2 / (j+1)^4 .

deg_j Nu = 12, so 13 unknowns and one linear solve per (n,p).  R is read straight
out of the sweep vector -- x0 is its last ans0.nc entries -- so no re-solve is
needed and the boundary certificate rides along on the cofactor lift for free.
"""
import os, sys, time, pickle
os.environ.setdefault('OMP_NUM_THREADS', '1')
from fractions import Fraction as Fr
import numpy as np
HERE = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'
sys.path.insert(0, HERE)
sys.path.insert(1, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import mindens, wtools as W, cert3
import fastlin

DEGJ = 12                        # deg_j Nu, per Z5_ORDER0 §7
NUNK = DEGJ + 1


def Dj(n, j, p):
    return ((j + 1) % p) * ((n + j + 1) % p) % p * ((n + j + 2) % p) % p \
        * ((n + j + 3) % p) % p


def gj(n, j, p):
    num = pow((n + 3 - j) % p, 2, p) * pow((n + j + 1) % p, 2, p) % p
    den = pow((j + 1) % p, 4, p)
    return num * pow(den, p - 2, p) % p


def solve_Nu(n, p, Rvals, npts=49):
    """Rvals: dict j -> R(n,j) mod p.  Returns (coefficients c_0..c_12, nbad)."""
    js = [j for j in sorted(Rvals) if Dj(n, j, p) and Dj(n, j + 1, p)][:npts]
    A = np.zeros((len(js), NUNK), dtype=np.int64)
    b = np.zeros(len(js), dtype=np.int64)
    for t, j in enumerate(js):
        g = gj(n, j, p)
        i1 = pow(Dj(n, j + 1, p), p - 2, p)
        i0 = pow(Dj(n, j, p), p - 2, p)
        for u in range(NUNK):
            A[t, u] = (g * pow((j + 1) % p, u, p) % p * i1
                       - pow(j % p, u, p) * i0) % p
        b[t] = Rvals[j] % p
    x, rk, piv, nbad = fastlin.solve(A, b, p)
    return x, rk, nbad, len(js)


def Rvals_from_x0(x0, ans0, n, p, jmax=60):
    out = {}
    for j in range(0, jmax):
        if not (Dj(n, j, p) and Dj(n, j + 1, p) and (n + 3 - j) % p):
            continue
        out[j] = (ans0.eval_r(x0, n, 0, j, p) + ans0.eval_s(x0, n, j, 0, p)) % p
    return out


def one(args):
    n, p, vec, nc0 = args
    ans0 = cert3.mk('M0', 12, 0, 0)
    x0 = np.asarray(vec[-nc0:], dtype=np.int64)
    R = Rvals_from_x0(x0, ans0, n, p)
    x, rk, nbad, nj = solve_Nu(n, p, R)
    return (n, p, None if nbad else x.astype(np.int64), rk, nbad, nj)


if __name__ == '__main__':
    from multiprocessing import Pool
    fn = sys.argv[1] if len(sys.argv) > 1 else 'nsweepB_0_24.pkl'
    nproc = int(sys.argv[2]) if len(sys.argv) > 2 else 11
    d = pickle.load(open(os.path.join(HERE, fn), 'rb'))
    data, ns, ps = d['data'], d['ns'], d['ps']
    ans0 = cert3.mk('M0', 12, 0, 0)
    nc0 = ans0.nc
    jobs = [(n, p, data[(n, p)], nc0) for p in ps for n in ns
            if data.get((n, p)) is not None]
    print('boundary solve: %d (n,p) jobs, %d unknowns' % (len(jobs), NUNK), flush=True)
    t0 = time.time()
    out = {}
    nfail = 0
    ranks = set()
    with Pool(nproc) as pool:
        for n, p, x, rk, nbad, nj in pool.imap_unordered(one, jobs, chunksize=4):
            out[(n, p)] = x
            ranks.add(rk)
            if x is None:
                nfail += 1
                if nfail <= 3:
                    print('   FAIL n=%d p=%d nbad=%d (rows %d)' % (n, p, nbad, nj),
                          flush=True)
    print('boundary solve: %d failures, ranks seen %s  [%.0fs]'
          % (nfail, sorted(ranks), time.time() - t0), flush=True)
    pickle.dump(dict(data=out, ns=ns, ps=ps, DEGJ=DEGJ),
                open(os.path.join(HERE, 'bndsweep.pkl'), 'wb'))
