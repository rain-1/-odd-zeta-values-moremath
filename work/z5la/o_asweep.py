"""Long multi-prime n-sweep of the a-direction, resumable.

Extends o_areco.sweep: writes incrementally to a_big.pkl so that the
reconstruction (o_alift.py) can be started on whatever is finished.
"""
import os, sys, time, pickle
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('MKL_NUM_THREADS', '1')

STORE = 'a_big.pkl'


def primes_below(hi, cnt):
    """the `cnt` largest primes < hi (hi <= 2^22 keeps fastlin's float64 exact)"""
    out = []
    x = hi - 1
    while len(out) < cnt:
        if x > 2 and all(x % d for d in range(2, int(x ** .5) + 1)):
            out.append(x)
        x -= 1
    return out


PRIMES = primes_below(4194304, 16)


def load():
    d = {}
    for fn in ('a_sweep.pkl', STORE):
        if os.path.exists(fn):
            try:
                d.update(pickle.load(open(fn, 'rb')))
            except Exception:
                pass
    return d


if __name__ == '__main__':
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 199
    nprimes = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    nproc = int(sys.argv[3]) if len(sys.argv) > 3 else 11
    import o_areco
    from multiprocessing import Pool
    ps = PRIMES[:nprimes]
    ns = list(range(3, nmax + 1))
    have = load()
    jobs = [(n, p) for p in ps for n in ns if (n, p) not in have]
    print('primes %s' % (ps,), flush=True)
    print('%d n-values, %d already cached, %d jobs to run' %
          (len(ns), len(ns) * len(ps) - len(jobs), len(jobs)), flush=True)
    t0 = time.time()
    done = 0
    with Pool(nproc) as pool:
        for n, p, v in pool.imap_unordered(o_areco.one, jobs, chunksize=1):
            have[(n, p)] = v
            done += 1
            if done % 100 == 0:
                pickle.dump(have, open(STORE + '.tmp', 'wb'))
                os.replace(STORE + '.tmp', STORE)
                print('  %d/%d  [%.0fs]' % (done, len(jobs), time.time() - t0), flush=True)
    pickle.dump(have, open(STORE + '.tmp', 'wb'))
    os.replace(STORE + '.tmp', STORE)
    for p in ps:
        ok = sorted(n for (n, q) in have if q == p and have[(n, q)] is not None)
        print('p=%d : %d good samples, n=%d..%d' % (p, len(ok), min(ok), max(ok)), flush=True)
    print('total [%.0fs]' % (time.time() - t0), flush=True)
