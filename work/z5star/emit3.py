"""JOB 3/4 -- the full lift: merge every sweep file, interpolate in parallel,
CRT over all primes, rational-lift to Q, then clear to Z."""
import os, sys, time, pickle
os.environ.setdefault('OMP_NUM_THREADS', '1')
from fractions import Fraction as Fr
import numpy as np
HERE = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'
sys.path.insert(0, HERE)
from emit import DN, dn_val, interp, crt, ratlift


def job(args):
    p, fit, cols = args
    dnv = [dn_val(n) % p for n in fit]
    out = {}
    for c, col in cols.items():
        if not any(col):
            out[c] = [0]
            continue
        ys = [int(col[i]) * dnv[i] % p for i in range(len(fit))]
        out[c] = interp(fit, ys, p)
    return (p, out)


def main(files, nhold=8, nproc=11):
    from multiprocessing import Pool
    data = {}
    ps = []
    for fn in files:
        d = pickle.load(open(os.path.join(HERE, fn), 'rb'))
        data.update(d['data'])
        ps += [p for p in d['ps'] if p not in ps]
    xs_all = sorted({n for (n, p) in data if data[(n, p)] is not None})
    fit = xs_all[:-nhold]; hold = xs_all[-nhold:]
    NCOL = len(data[(fit[0], ps[0])])
    print('primes %d, fit points %d, held out %d, coefficients %d'
          % (len(ps), len(fit), len(hold), NCOL), flush=True)
    jobs = []
    for p in ps:
        cols = {c: [int(data[(n, p)][c]) for n in fit] for c in range(NCOL)}
        jobs.append((p, fit, cols))
    t0 = time.time()
    polys = {}
    with Pool(nproc) as pool:
        for p, out in pool.imap_unordered(job, jobs):
            polys[p] = out
            print('   prime %d done [%.0fs]' % (p, time.time() - t0), flush=True)
    bad = 0
    for p in ps:
        for n in hold:
            v = data.get((n, p))
            if v is None:
                continue
            for c in range(NCOL):
                acc = 0
                for a in reversed(polys[p][c]):
                    acc = (acc * n + a) % p
                if acc != int(v[c]) * dn_val(n) % p:
                    bad += 1
    print('HELD-OUT: %d mismatches over %d x %d x %d = %d identities'
          % (bad, len(hold), NCOL, len(ps), len(hold) * NCOL * len(ps)), flush=True)
    degs = {}
    mism = 0
    for c in range(NCOL):
        ls = {len(polys[p][c]) for p in ps}
        if len(ls) > 1:
            mism += 1
        degs[c] = max(ls) - 1
    print('degree mismatch across primes: %d coefficients' % mism, flush=True)
    out = {}
    unl = 0
    tot = 0
    for c in range(NCOL):
        vec = []
        for j in range(degs[c] + 1):
            rs = [polys[p][c][j] if j < len(polys[p][c]) else 0 for p in ps]
            x, M = crt(rs, ps)
            q = ratlift(x, M)
            tot += 1
            if q is None:
                unl += 1
            vec.append(q)
        out[c] = vec
    print('unliftable: %d of %d coefficients  [%.0fs]' % (unl, tot, time.time() - t0),
          flush=True)
    pickle.dump(dict(out=out, degs=degs, fit=fit, hold=hold, ps=ps),
                open(os.path.join(HERE, 'lift_Q.pkl'), 'wb'))


if __name__ == '__main__':
    main(sys.argv[1:] or ['nsweep_6p.pkl', 'nsweep_6_24.pkl'])
