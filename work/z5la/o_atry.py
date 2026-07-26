"""Exhaustive lift attempt: several LLL dimensions, several coefficient samples,
one or two reserved primes.  (o_await.py runs the default configuration.)"""
import os, pickle, sys, time
os.environ.setdefault('OMP_NUM_THREADS', '1')
import numpy as np
import o_alift, ratrec


def run(minsamp=150, dbound=70):
    D = {}
    for fn in ('a_sweep.pkl', 'a_big.pkl'):
        if os.path.exists(fn): D.update(pickle.load(open(fn, 'rb')))
    ps = []
    for p in sorted(set(q for (nn, q) in D), reverse=True):
        ns = sorted(nn for (nn, q) in D if q == p and D[(nn, q)] is not None)
        if len(ns) >= minsamp: ps.append((p, ns))
    print('%d usable primes' % len(ps), flush=True)
    Vs = []
    for p, ns in ps:
        V, inf = o_alift.vec_mod_p(D, p, ns, dbound)
        if V is None: print('  p=%d %s' % (p, inf)); return None
        Vs.append(V)
    degs = [len(v) for v in Vs[0]]
    flat = [(i, j) for i in range(5) for j in range(degs[i])]
    for nres in (2, 1):
        nfit = len(ps) - nres
        xs = [0] * len(flat); M = 1
        for u in range(nfit):
            p = ps[u][0]
            for t, (i, j) in enumerate(flat):
                xs[t], _ = o_alift.crt_pair(xs[t], M, Vs[u][i][j] % p, p)
            M *= p
        for kl in (12, 16, 24, 32):
            for seed in range(1, 6):
                cands = o_alift.common_den(xs, M, k=kl, seed=seed)
                from math import gcd
                for bits, d, us in cands:
                    Z = [[0] * degs[i] for i in range(5)]
                    for t, (i, j) in enumerate(flat): Z[i][j] = us[t]
                    g = 0
                    for row in Z:
                        for c in row: g = gcd(g, c)
                    if g == 0: continue
                    if g > 1: Z = [[c // g for c in row] for row in Z]
                    if Z[0][-1] < 0: Z = [[-c for c in row] for row in Z]
                    if all(o_alift._check_mod(Z, Vs[u], ps[u][0])
                           for u in range(nfit, len(ps))):
                        print('LIFTED  nres=%d k=%d seed=%d  M=%d bits  max|coef|=%d bits'
                              % (nres, kl, seed, M.bit_length(),
                                 max(max(abs(c) for c in r) for r in Z).bit_length()),
                              flush=True)
                        pickle.dump(dict(Z=Z, ps=[p for p, _ in ps]),
                                    open('a_lift.pkl', 'wb'))
                        return Z
            print('  nres=%d k=%d : no lift (M = %d bits)' % (nres, kl, M.bit_length()),
                  flush=True)
    return None


if __name__ == '__main__':
    Z = run()
    if Z:
        for i in range(5):
            print('a_%d : deg %d, max |coef| %d bits'
                  % (i, len(Z[i]) - 1, max(abs(c) for c in Z[i]).bit_length()))
        print('LIFT SUCCESS')
