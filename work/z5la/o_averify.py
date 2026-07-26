"""Independent verification of the lifted A(n) in Z[n].

Evaluates the EXACT integer polynomials a_0..a_4 at (n, p) combinations that
took no part in any fit -- fresh n AND fresh prime -- and compares with the
a-direction recomputed from scratch by the order-7 scan.
"""
import os, sys, pickle, time
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('MKL_NUM_THREADS', '1')


def pev(c, x, p):
    v = 0
    for a in reversed(c): v = (v * x + a) % p
    return v


def check(Z, jobs, nproc=6):
    from multiprocessing import Pool
    import o_areco
    out = []
    with Pool(nproc) as pool:
        for nn, p, v in pool.imap_unordered(o_areco.one, jobs):
            if v is None:
                out.append((nn, p, 'a-direction not 1-dimensional')); continue
            a = [pev(Z[t], nn, p) for t in range(5)]
            if a[0] == 0:
                out.append((nn, p, 'a_0(n) = 0 mod p -- inconclusive')); continue
            inv = pow(a[0], p - 2, p)
            a = [x * inv % p for x in a]
            out.append((nn, p, 'MATCH' if a == list(v) else 'MISMATCH %s vs %s' % (a, list(v))))
    return out


if __name__ == '__main__':
    import o_asweep
    Z = pickle.load(open('a_lift.pkl', 'rb'))['Z']
    used = set(pickle.load(open('a_lift.pkl', 'rb'))['ps'])
    fresh_p = [p for p in o_asweep.primes_below(4194304, 40) if p not in used][-8:]
    ns = [503, 617, 733, 881]
    jobs = [(nn, p) for p in fresh_p[:3] for nn in ns]
    t0 = time.time()
    res = check(Z, jobs)
    ok = sum(1 for r in res if r[2] == 'MATCH')
    for r in sorted(res): print('  n=%-5d p=%-8d %s' % r)
    print('%d/%d MATCH at fresh (n,p), primes %s  [%.0fs]'
          % (ok, len(res), fresh_p[:3], time.time() - t0))
