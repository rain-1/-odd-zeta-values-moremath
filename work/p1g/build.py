"""P1g E1 step 1: build and cache the R-extended design matrix
      M[i] = row(n_i)  ,  b[i] = P_{n_i} mod q ,   n_i = 1..N .
Usage:  python3 build.py N q [useD]
"""
import sys, time, os
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from rfit import (Q1, Q2, KL, CL, DL, NL, build_basis, row, lad_ext)

N = int(sys.argv[1])
q = int(sys.argv[2])
useD = len(sys.argv) > 3 and sys.argv[3] == 'D'
tag = ('RD' if useD else 'R') + '_%d_%d' % (N, q)
OUT = '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g/M_%s.npy' % tag

B = build_basis(kletters=KL, cletters=CL + (DL if useD else []),
                nletters=NL, useD=useD)
NC = len(B)
print('basis %d columns, %d k-monomials, %d c-monomials' % (NC, len(B.km), len(B.cm)),
      flush=True)

M = np.zeros((N, NC), dtype=np.int64)
Y = lad_ext('P', N + 1, q)
b = np.zeros(N, dtype=np.int64)
t0 = time.time()
for i, n in enumerate(range(1, N + 1)):
    M[i] = row(n, q, B, useD=useD)
    b[i] = Y[n]
    if n % 100 == 0:
        print('  n=%d  %.1f s' % (n, time.time() - t0), flush=True)
np.save(OUT, M)
np.save(OUT.replace('M_', 'b_'), b)
print('saved %s  (%.1f s)' % (OUT, time.time() - t0), flush=True)
