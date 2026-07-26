"""Decisive test: is P-hat_n in the span of  sum_{k,l} T * (weight-3 monomial in the
nine bare symbols), degree <= 3?   143 symmetric columns -> need > 143 rows."""
import sys, os, time, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from design2 import build, monname, rref
from bare import Q1, Q2, lad_mod

W = int(sys.argv[1]); KEY = sys.argv[2]; N = int(sys.argv[3])
q = int(sys.argv[4]) if len(sys.argv) > 4 else Q1
t0 = time.time()
mons, M = build(W, N, q, verbose=True)
print('%d symmetric monomials, %d rows (%.1fs)' % (len(mons), N + 1, time.time() - t0), flush=True)
b = np.array([lad_mod(KEY, n, q) for n in range(N + 1)], dtype=np.int64)
_, rA, _ = rref(M, q)
_, rAb, _ = rref(np.hstack([M, b[:, None]]), q)
print('rank(A)=%d  rank(A|b)=%d  ->  %s' % (rA, rAb, 'CONSISTENT' if rA == rAb else 'INCONSISTENT'),
      flush=True)
print('excess equations: %d' % (N + 1 - rA))
np.savez_compressed(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'DF_W%d_%s_%d_%d.npz' % (W, KEY, N, q)),
                    M=M, b=b, mons=np.array([monname(m) for m in mons]))
