"""JOB 3 -- the n-sweep.

For each n and each prime, solve the whole order-3 certificate at the MEASURED
minimal ansatz and record the canonical (pivot-)solution.  fastlin.solve takes
the lexicographically first independent pivot set, which is the same for generic
n and p, so each coefficient is a well-defined rational function of n and can be
reconstructed by Cauchy interpolation mod p and then lifted to Q by CRT.
"""
import os, sys, time, pickle
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('MKL_NUM_THREADS', '1')
import numpy as np

HERE = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'
sys.path.insert(0, HERE)

PRIMES = [4194301, 4194287, 4194277, 4194271, 4194247, 4194217, 4194199, 4194191,
          4194187, 4194181, 4194173, 4194167, 4194143, 4194137, 4194131, 4194107,
          4194103, 4194023, 4194011, 4194007, 4193977, 4193971, 4193963, 4193957]
DL, SL, D0, S0 = 'M0', 8, 'M0', 12


def one(args):
    n, p = args
    import json
    from fractions import Fraction as Fr
    import mindens, wtools as W, cert4
    d = json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
    w = W.to_p([Fr(c) for c in d['coeffs']], p)
    try:
        r = cert4.build(n, w, W.B, DL, SL, D0, S0, p=p, vnpts=0, verbose=False,
                        bbot=False)
    except Exception as e:
        return (n, p, None, str(e))
    if r['nbadL'] or r['nbad0']:
        return (n, p, None, 'nbadL=%d nbad0=%d' % (r['nbadL'], r['nbad0']))
    vec = np.concatenate([r['coefL'][j] for j in r['act']] + [r['x0']])
    return (n, p, vec.astype(np.int64), '')


if __name__ == '__main__':
    from multiprocessing import Pool
    ns = [int(x) for x in sys.argv[1].split(',')] if ',' in sys.argv[1] else \
        list(range(int(sys.argv[1].split(':')[0]), int(sys.argv[1].split(':')[1])))
    nprimes = int(sys.argv[2]) if (len(sys.argv) > 2 and ':' not in sys.argv[2]) else 1
    if ':' in sys.argv[2]:
        a,b = sys.argv[2].split(':'); ps = PRIMES[int(a):int(b)]
    else:
        ps = PRIMES[:nprimes]
    nproc = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    jobs = [(n, p) for p in ps for n in ns]
    t0 = time.time()
    out = {}
    nfail = 0
    with Pool(nproc) as pool:
        for n, p, v, msg in pool.imap_unordered(one, jobs):
            out[(n, p)] = v
            if v is None:
                nfail += 1
                print('   FAIL n=%d p=%d : %s' % (n, p, msg), flush=True)
    print('sweep done: %d jobs, %d failures  [%.0fs]'
          % (len(jobs), nfail, time.time() - t0), flush=True)
    pickle.dump(dict(data=out, ns=ns, ps=ps, DL=DL, SL=SL, D0=D0, S0=S0),
                open(os.path.join(HERE, 'nsweep_%s.pkl' % sys.argv[2].replace(':','_')), 'wb'))
