"""Quick consistency probe: pick W, target, symbol subset, degree cap, N."""
import sys, os, time, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from design2 import build, monomials, sym_orbits, monname, rref
from bare import Q1, Q2, lad_mod

W = int(sys.argv[1]); KEY = sys.argv[2]; DMAX = int(sys.argv[3])
SY = tuple(int(x) for x in sys.argv[4].split(','))
N = int(sys.argv[5]); q = int(sys.argv[6]) if len(sys.argv) > 6 else Q1
t0 = time.time()
mons = sym_orbits(monomials(W, DMAX, SY))
_, M = build(W, N, q, mons=mons)
b = np.array([lad_mod(KEY, n, q) for n in range(N + 1)], dtype=np.int64)
_, rA, _ = rref(M, q)
_, rAb, _ = rref(np.hstack([M, b[:, None]]), q)
print('W=%d %s deg<=%d syms=%s N=%d q=%d : cols=%d rank(A)=%d rank(A|b)=%d excess=%d -> %s (%.1fs)'
      % (W, KEY, DMAX, SY, N, q, len(mons), rA, rAb, N + 1 - rA,
         'CONSISTENT' if rA == rAb else 'INCONSISTENT', time.time() - t0), flush=True)
