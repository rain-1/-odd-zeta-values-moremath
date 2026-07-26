"""Pin the degrees of a_t(n)/a_0(n) with a long single-prime n-sweep."""
import os, pickle, time
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
import o_areco

if __name__ == '__main__':
    p = o_areco.PRIMES[0]
    old = pickle.load(open('a_sweep.pkl', 'rb'))
    have = set(n for (n, q) in old if q == p and old[(n, q)] is not None)
    ns = [n for n in range(3, 320) if n not in have]
    t0 = time.time()
    d = o_areco.sweep([p], ns)
    old.update(d)
    pickle.dump(old, open('a_sweep2.pkl', 'wb'))
    ok = sorted(n for (n, q) in old if q == p and old[(n, q)] is not None)
    print('samples for p=%d : %d (n=%d..%d)  [%.0fs]'
          % (p, len(ok), min(ok), max(ok), time.time() - t0), flush=True)
    for t in range(1, 5):
        vals = [old[(n, p)][t] for n in ok]
        r = o_areco.ratfun(vals, ok, p, maxdeg=200)
        if r is None:
            print('a_%d/a_0 : reconstruction FAILED (degree > %d)' % (t, len(ok) // 2 - 1),
                  flush=True)
        else:
            num, den = r
            print('a_%d/a_0 : deg num = %d,  deg den = %d' % (t, len(num) - 1, len(den) - 1),
                  flush=True)
