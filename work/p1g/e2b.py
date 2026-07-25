"""P1g: rank + consistency of [fit ; depth-conditions] for an ARBITRARY sub-alphabet.

Usage:  python3 e2b.py MODE KSPEC CSPEC NSPEC N q
  MODE    base | strong | vt2 | vt2:I | vt2:III | vt2:I+II | ...
  KSPEC   comma list of k-letters   (A*,B*,R*,Y**)   or the shorthand AB / ABR / ABY / ABRY
  CSPEC   comma list of coupling letters (C*,D*,V**) or C / CD / CV / CDV
  NSPEC   comma list of n-letters   (N*,Z**)         or N / NZ
  N       levels 1..N ;  q  prime
"""
import sys, time
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from rfit import (Q1, Q2, AB, KL, CL, DL, NL, YL, VL, ZL,
                  build_basis, row, rref, lad_ext)
import rdepth

SH = {'AB': AB, 'ABR': KL, 'ABY': AB + YL, 'ABRY': KL + YL,
      'C': CL, 'CD': CL + DL, 'CV': CL + VL, 'CDV': CL + DL + VL,
      'N': NL, 'NZ': NL + ZL}

MODE = sys.argv[1]
kl = SH.get(sys.argv[2], sys.argv[2].split(','))
cl = SH.get(sys.argv[3], sys.argv[3].split(','))
nl = SH.get(sys.argv[4], sys.argv[4].split(','))
N = int(sys.argv[5])
q = int(sys.argv[6])
useD = any(x[0] == 'D' for x in cl)
nested = any(x[0] in 'YVZ' for x in kl + cl + nl)

B = build_basis(kletters=kl, cletters=cl, nletters=nl, useD=useD, nested=nested)
NC = len(B)
print('K=%s C=%s N=%s MODE=%s basis=%d cols (km=%d cm=%d nm=%d) N=%d q=%d'
      % (sys.argv[2], sys.argv[3], sys.argv[4], MODE, NC,
         len(B.km), len(B.cm), len(B.nm), N, q), flush=True)

caps = rdepth.caps_for(MODE, refine_eps=useD)
t0 = time.time()
C = rdepth.condition_rows(B, caps)
print('condition rows: %d x %d  (%.1f s)' % (len(C), NC, time.time() - t0), flush=True)

Y = lad_ext('P', N + 1, q)
M = np.zeros((N, NC), dtype=np.int64)
b = np.zeros(N, dtype=np.int64)
t0 = time.time()
for i, n in enumerate(range(1, N + 1)):
    M[i] = row(n, q, B, useD=useD, nested=nested)
    b[i] = Y[n]
print('design matrix built (%.1f s)' % (time.time() - t0), flush=True)

Cq = (np.array([[int(v) % q for v in r] for r in C], dtype=np.int64) if C
      else np.zeros((0, NC), np.int64))
rM, _, incM, _ = rref(M, b, q)
rC, _, _, _ = rref(Cq, np.zeros(len(Cq), np.int64), q)
A = np.concatenate([M, Cq], axis=0)
rhs = np.concatenate([b, np.zeros(len(Cq), np.int64)])
rA, piv, inc, _ = rref(A, rhs, q)
rAug, _, _, _ = rref(np.concatenate([A, rhs.reshape(-1, 1)], axis=1),
                     np.zeros(len(rhs), np.int64), q)
print('rank(fit)=%d rank(cond)=%d rank(joint)=%d nullity=%d INCONSISTENT=%s DEFECT=%d'
      % (rM, rC, rA, NC - rA, inc, rAug - rA), flush=True)
