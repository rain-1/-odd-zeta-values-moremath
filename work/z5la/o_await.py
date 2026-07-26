"""poll the growing a-sweep and attempt the lift each time a prime completes."""
import os, time, pickle, sys
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('MKL_NUM_THREADS', '1')
import o_alift

if __name__ == '__main__':
    tries = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    seen = -1
    for _ in range(tries):
        D = {}
        for fn in ('a_sweep.pkl', 'a_big.pkl'):
            if os.path.exists(fn):
                try: D.update(pickle.load(open(fn, 'rb')))
                except Exception: pass
        cnt = 0
        for p in set(q for (nn, q) in D):
            if sum(1 for (nn, q) in D if q == p and D[(nn, q)] is not None) >= 150:
                cnt += 1
        if cnt > seen:
            seen = cnt
            print('--- %d usable primes ---' % cnt, flush=True)
            try:
                Z, ps = o_alift.try_lift(verbose=True)
            except Exception as e:
                print('  error: %r' % (e,), flush=True); Z = None
            if Z is not None:
                pickle.dump(dict(Z=Z, ps=[p for p, _ in ps]), open('a_lift.pkl', 'wb'))
                for i in range(5):
                    print('a_%d : deg %d, max |coef| %d bits'
                          % (i, len(Z[i]) - 1, max(abs(c) for c in Z[i]).bit_length()),
                          flush=True)
                print('LIFT SUCCESS', flush=True)
                break
        time.sleep(60)
