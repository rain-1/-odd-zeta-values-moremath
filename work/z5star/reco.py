"""JOB 3 -- reconstruct every cofactor coefficient as a rational function of n,
then measure the degrees.  Step 1 of the lift; the size table depends on it."""
import os, sys, time, pickle
os.environ.setdefault('OMP_NUM_THREADS', '1')
import numpy as np
HERE = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'
sys.path.insert(0, HERE)
sys.path.insert(1, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
import ratrec


def reconstruct(vals, xs, p, maxdeg=55):
    return ratrec.null_min_deg(vals, xs, p, maxdeg)


def one(args):
    idx, vals, xs, p, maxdeg = args
    r = reconstruct(vals, xs, p, maxdeg)
    if r is None:
        return (idx, None, None)
    num, den = r
    return (idx, len(num) - 1, len(den) - 1)


if __name__ == '__main__':
    from multiprocessing import Pool
    fn = sys.argv[1] if len(sys.argv) > 1 else 'nsweep_1p.pkl'
    nproc = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    d = pickle.load(open(os.path.join(HERE, fn), 'rb'))
    data, ns, ps = d['data'], d['ns'], d['ps']
    p = ps[0]
    xs = [n for n in ns if data.get((n, p)) is not None]
    Mv = np.array([data[(n, p)] for n in xs], dtype=np.int64)
    NC = Mv.shape[1]
    print('samples %d, coefficients %d' % (len(xs), NC), flush=True)
    nz = [j for j in range(NC) if np.count_nonzero(Mv[:, j])]
    print('identically-zero coefficients: %d of %d' % (NC - len(nz), NC), flush=True)
    t0 = time.time()
    jobs = [(j, list(Mv[:, j]), xs, p, 55) for j in nz]
    res = {}
    with Pool(nproc) as pool:
        for idx, dn, dd in pool.imap_unordered(one, jobs, chunksize=8):
            res[idx] = (dn, dd)
    bad = [j for j in nz if res[j][0] is None]
    print('reconstruction failed for %d coefficients  [%.0fs]'
          % (len(bad), time.time() - t0), flush=True)
    dn = [res[j][0] for j in nz if res[j][0] is not None]
    dd = [res[j][1] for j in nz if res[j][0] is not None]
    import collections
    print('deg(num) distribution:', dict(sorted(collections.Counter(dn).items())), flush=True)
    print('deg(den) distribution:', dict(sorted(collections.Counter(dd).items())), flush=True)
    print('MAX deg_n(num) = %d , MAX deg_n(den) = %d' % (max(dn), max(dd)), flush=True)
    pickle.dump(dict(res=res, nz=nz, xs=xs, p=p), open(os.path.join(HERE, 'reco_degs.pkl'), 'wb'))
