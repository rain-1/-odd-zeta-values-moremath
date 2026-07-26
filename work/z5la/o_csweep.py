"""n-sweep of the eight residual COFACTOR blocks at fixed (n,p).

Extends o_final.build: same ansatz, same normalisation, but the verification is
dropped and the raw coefficient vectors are kept.

  X   : (nc1 x 7)  the seven standalone blocks, ansatz E1 slack 18
  Xz  : (nc0,)     the () block,                ansatz Z3 slack 16

The a-vector is taken from the a-sweep (normalisation a_0 = 1), so every
cofactor coefficient is a well-defined rational function of n -- PROVIDED the
pivot-column set of the two solves is the same at every n.  That is recorded and
checked.
"""
import os, sys, time, pickle
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('MKL_NUM_THREADS', '1')
import numpy as np

M = 7
DN1, SL1 = 'E1', 18
DN0, SL0 = 'Z3', 16
FORCE = (1, 1)


def ansatzes(m=M, rev=False):
    """rev=True reverses the monomial order, hence the PIVOT SET, hence the
    gauge in which the (518-dimensional) cofactor freedom is fixed.  Used to
    test whether the n-degree of the canonical representative is intrinsic or an
    artefact of the gauge."""
    import o_scan
    from solve import Ansatz
    D = o_scan.dens(m)[DN1]
    dk = sum(mu * abs(f[2]) for f, mu in D) + SL1
    dl = sum(mu * abs(f[3]) for f, mu in D) + SL1
    ans = Ansatz(D, D, dk, dl, dk, dl, force_k=FORCE[0], force_l=FORCE[1])
    D0 = o_scan.dens(m)[DN0]
    ek = sum(mu * abs(f[2]) for f, mu in D0) + SL0
    el = sum(mu * abs(f[3]) for f, mu in D0) + SL0
    ans0 = Ansatz(D0, D0, ek, el, ek, el, force_k=FORCE[0], force_l=FORCE[1])
    if rev:
        for a in (ans, ans0):
            a.mons_r = a.mons_r[::-1]; a.mons_s = a.mons_s[::-1]
    return ans, ans0


def one(args):
    n, p, avec = args[:3]
    do_z = args[3] if len(args) > 3 else True
    rev = args[4] if len(args) > 4 else False
    import numpy as np
    import ordm, o_scan, o_zero, fastlin
    m = M
    ans, ans0 = ansatzes(m, rev)
    na = m - 2
    nfit = int(1.35 * (ans.nc + na)) + 20
    nfit0 = int(1.35 * ans0.nc) + 20
    npts = max(nfit, nfit0) if do_z else nfit
    pd = ordm.PDm('w3', p, n, m, npts)
    Acol = ordm.acols(pd)
    stand = [j for j in pd.free if len(pd.B[j]) > 0]
    zj = [j for j in pd.free if len(pd.B[j]) == 0][0]
    R0, R1, S0, S1, Mm = o_zero.design(pd, ans)
    avec = np.asarray(avec, dtype=np.int64) % p
    rhsS = np.zeros((npts, len(stand)), dtype=np.int64)
    for u, j in enumerate(stand):
        rhsS[:, u] = [int(x) for x in
                      (-(Acol[j * npts:(j + 1) * npts].astype(object)
                         @ avec.astype(object))) % p]
    X, rk1, piv1, nb1 = fastlin.solve(Mm[:nfit].astype(np.int64), rhsS[:nfit], p, nb=64)
    if nb1: return (n, p, None, None, None, None, 'nb1=%d' % nb1)
    if not do_z:
        return (n, p, X.astype(np.int32), None, hash(tuple(piv1)), 0, None)
    rv1 = {}; sv1 = {}
    for u, j in enumerate(stand):
        rv1[j] = o_zero.matmul_mod(R1, X[:, u:u + 1], p)[:, 0]
        sv1[j] = o_zero.matmul_mod(S1, X[:, u:u + 1], p)[:, 0]
    R0z, R1z, S0z, S1z, Mz = o_zero.design(pd, ans0)
    gkf = pd.gk.astype(np.float64); glf = pd.gl.astype(np.float64)
    rhs = np.array([int(x) for x in
                    (-(Acol[zj * npts:(zj + 1) * npts].astype(object)
                       @ avec.astype(object))) % p], dtype=np.float64)
    for j in stand:
        ck = pd.Sk[:, zj, j].astype(np.float64); cl = pd.Sl[:, zj, j].astype(np.float64)
        rhs = (rhs - ((gkf * ck) % p) * rv1[j] - ((glf * cl) % p) * sv1[j]) % p
    Xz, rk2, piv2, nb2 = fastlin.solve(Mz[:nfit0].astype(np.int64),
                                       rhs[:nfit0].astype(np.int64), p, nb=64)
    if nb2: return (n, p, None, None, None, None, 'nb2=%d' % nb2)
    return (n, p, X.astype(np.int32), Xz.astype(np.int32),
            hash(tuple(piv1)), hash(tuple(piv2)), None)


def save(store, res):
    d = {'%d_%d_X' % k: v[0] for k, v in res.items()}
    d.update({'%d_%d_Z' % k: v[1] for k, v in res.items() if v[1] is not None})
    np.savez_compressed(store + '.npz', **d)


def run(ns, ps, nproc=11, store='c_sweep', do_z=True):
    from multiprocessing import Pool
    import o_asweep
    A = o_asweep.load()
    jobs = []
    for p in ps:
        for n in ns:
            v = A.get((n, p))
            if v is None:
                print('  no a-vector for (n=%d,p=%d) -- skipped' % (n, p), flush=True)
                continue
            jobs.append((n, p, v, do_z))
    print('%d cofactor solves' % len(jobs), flush=True)
    t0 = time.time(); done = 0
    res = {}
    pivs = set()
    with Pool(nproc) as pool:
        for n, p, X, Xz, h1, h2, err in pool.imap_unordered(one, jobs, chunksize=1):
            done += 1
            if err:
                print('  (n=%d,p=%d) FAILED %s' % (n, p, err), flush=True); continue
            pivs.add((h1, h2))
            res[(n, p)] = (X, Xz)
            if done % 25 == 0:
                print('  %d/%d  [%.0fs]  distinct pivot sets: %d'
                      % (done, len(jobs), time.time() - t0, len(pivs)), flush=True)
                save(store, res)
    save(store, res)
    print('done %d, distinct pivot sets %d  [%.0fs]' % (len(res), len(pivs), time.time() - t0),
          flush=True)
    return res


if __name__ == '__main__':
    import o_asweep
    lo = int(sys.argv[1]); hi = int(sys.argv[2]); nprimes = int(sys.argv[3])
    nproc = int(sys.argv[4]) if len(sys.argv) > 4 else 11
    store = sys.argv[5] if len(sys.argv) > 5 else 'c_sweep'
    do_z = (sys.argv[6] != '0') if len(sys.argv) > 6 else True
    run(list(range(lo, hi + 1)), o_asweep.PRIMES[:nprimes], nproc, store, do_z)
