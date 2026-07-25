"""P1g: build and SAVE (design matrix, rhs, column labels, condition rows) for one alphabet.

Usage: python3 buildsave.py TAG MODE KSPEC CSPEC NSPEC N q
Saves  S_<TAG>.npz  with  M, b, labels (object array), C (condition rows, int64 mod q).

Because the depth-condition matrix is BLOCK DIAGONAL with respect to
"which new letters a monomial uses" (Prop 5.1 of PHASE2_RLETTER.md), several such files can
be merged column-wise by label (merge.py) to test the union alphabet *minus mixed monomials*
without ever building the (much larger) mixed design matrix.
"""
import sys, time
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from rfit import (AB, KL, CL, DL, NL, YL, VL, ZL, build_basis, row, lad_ext)
import rdepth

SH = {'AB': AB, 'ABR': KL, 'ABY': AB + YL, 'ABRY': KL + YL,
      'C': CL, 'CD': CL + DL, 'CV': CL + VL, 'CDV': CL + DL + VL,
      'N': NL, 'NZ': NL + ZL}

TAG = sys.argv[1]
MODE = sys.argv[2]
kl = SH.get(sys.argv[3], sys.argv[3].split(','))
cl = SH.get(sys.argv[4], sys.argv[4].split(','))
nl = SH.get(sys.argv[5], sys.argv[5].split(','))
N = int(sys.argv[6])
q = int(sys.argv[7])
useD = any(x[0] == 'D' for x in cl)
nested = any(x[0] in 'YVZ' for x in kl + cl + nl)

B = build_basis(kletters=kl, cletters=cl, nletters=nl, useD=useD, nested=nested)
NC = len(B)
labels = np.array([B.label(e) for e in B.els], dtype=object)
print('%s: %d cols, N=%d, q=%d' % (TAG, NC, N, q), flush=True)

C = rdepth.condition_rows(B, rdepth.caps_for(MODE, refine_eps=useD))
Cq = (np.array([[int(v) % q for v in r] for r in C], dtype=np.int64) if C
      else np.zeros((0, NC), np.int64))
print('  %d condition rows' % len(C), flush=True)

Y = lad_ext('P', N + 1, q)
M = np.zeros((N, NC), dtype=np.int64)
b = np.zeros(N, dtype=np.int64)
t0 = time.time()
for i, n in enumerate(range(1, N + 1)):
    M[i] = row(n, q, B, useD=useD, nested=nested)
    b[i] = Y[n]
print('  design matrix built (%.1f s)' % (time.time() - t0), flush=True)
np.savez_compressed('/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g/S_%s.npz' % TAG,
                    M=M, b=b, labels=labels, C=Cq, q=q, N=N)
print('  saved S_%s.npz' % TAG, flush=True)
