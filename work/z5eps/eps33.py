"""eps33.py -- stress the A7 saturation: is sym(Delta5) still in sym(ker Phi5)
when the row set is pushed far beyond the saturation range?

Test (as in eps22): exists antisym a with Phi5.(sym(Delta5) + a) = 0, i.e.
rank[A | b] == rank[A] where A = Phi5 restricted to the antisym subspace and
b = -Phi5.sym(Delta5).  Run at n <= 75 (2926 rows), two primes.
A failure here would prove the missing dimension is NOT per-row realisable.
"""
import sys, time
import numpy as np

sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
from eps22 import MON, MIDX, NM, SIG, DELTA5, build_rows

def run(p, NROWS):
    t0 = time.time()
    rows, info = build_rows(p, NROWS)
    print('rows:', rows.shape, '%.0fs' % (time.time() - t0), flush=True)
    fm = lambda fr: fr.numerator % p * pow(fr.denominator % p, p - 2, p) % p
    d5 = np.zeros(NM, dtype=np.int64)
    for m, cc in DELTA5.items():
        d5[MIDX[m]] = fm(cc)
    i2 = pow(2, p - 2, p)
    d5s = (d5 + d5[SIG]) * i2 % p
    b = (-(rows.dot(d5s)) % p)

    # antisym subspace: columns rows[:,i] - rows[:,sig i], i < sig i
    pairs = [(i, int(SIG[i])) for i in range(NM) if i < SIG[i]]
    A = np.zeros((len(pairs), rows.shape[0]), dtype=np.int64)   # A^T layout
    for t_, (i, j) in enumerate(pairs):
        A[t_] = (rows[:, i] - rows[:, j]) % p
    t1 = time.time()
    import eps28
    r1 = eps28.elim_rank(A.copy(), p)
    r2 = eps28.elim_rank(np.vstack([A, b[None, :]]), p)
    ok = r1 == r2
    print('p=%d NROWS=%d: rank(A)=%d, with b: %d -> membership %s (%.0fs)'
          % (p, NROWS, r1, r2, 'HOLDS' if ok else '*** FAILS ***',
             time.time() - t1), flush=True)
    return ok

if __name__ == '__main__':
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 4194301
    NROWS = int(sys.argv[2]) if len(sys.argv) > 2 else 75
    run(p, NROWS)
