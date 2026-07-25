"""P1g E1/E2: rank + consistency of  [fit ; depth-conditions]  in a chosen alphabet.

Usage:  python3 e2.py MODE ALPHABET N q
  MODE     base | vt2 | strong
  ALPHABET ctrl (A,B,C,N)  |  R (A,B,R,C,N)  |  RD (A,B,R,C,D,N)
  N        number of levels n = 1..N
  q        prime
Design matrices are cached as M_<tag>.npy by build.py; ctrl is built on the fly.
"""
import sys, time, os
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from rfit import Q1, Q2, KL, CL, DL, NL, build_basis, row, rref, lad_ext
import rdepth

MODE = sys.argv[1]
ALPH = sys.argv[2]
N = int(sys.argv[3])
q = int(sys.argv[4])

useD = (ALPH == 'RD')
kl = [x for x in KL if x[0] != 'R'] if ALPH == 'ctrl' else KL
cl = CL + (DL if useD else [])
B = build_basis(kletters=kl, cletters=cl, nletters=NL, useD=useD)
NC = len(B)
print('ALPHABET=%s MODE=%s  basis %d cols, N=%d, q=%d' % (ALPH, MODE, NC, N, q), flush=True)

caps = rdepth.caps_for(MODE, refine_eps=useD)
print('caps:', {k: caps[k] for k in sorted(caps)}, flush=True)

t0 = time.time()
C = rdepth.condition_rows(B, caps)
print('condition rows: %d x %d   (%.1f s)' % (len(C), NC, time.time() - t0), flush=True)

tag = ('RD' if useD else ('R' if ALPH == 'R' else 'ctrl'))
fn = '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g/M_%s_%d_%d.npy' % (tag, N, q)
if os.path.exists(fn):
    M = np.load(fn)
    b = np.load(fn.replace('M_', 'b_'))
    print('loaded cached design matrix %s' % fn, flush=True)
else:
    Y = lad_ext('P', N + 1, q)
    M = np.zeros((N, NC), dtype=np.int64)
    b = np.zeros(N, dtype=np.int64)
    for i, n in enumerate(range(1, N + 1)):
        M[i] = row(n, q, B, useD=useD)
        b[i] = Y[n]
    np.save(fn, M); np.save(fn.replace('M_', 'b_'), b)
    print('built design matrix (%.1f s)' % (time.time() - t0), flush=True)

Cq = np.array([[int(v) % q for v in r] for r in C], dtype=np.int64) if C else np.zeros((0, NC), np.int64)
t0 = time.time()
rM, _, incM, _ = rref(M, b, q)
rC, _, _, _ = rref(Cq, np.zeros(len(Cq), np.int64), q)
A = np.concatenate([M, Cq], axis=0)
rhs = np.concatenate([b, np.zeros(len(Cq), np.int64)])
rA, piv, inc, _ = rref(A, rhs, q)
# defect = rank[A|rhs] - rank[A]  (0 iff consistent; 1 = a single obstructing functional)
rAug, _, _, _ = rref(np.concatenate([A, rhs.reshape(-1, 1)], axis=1),
                     np.zeros(len(rhs), np.int64), q)
print('rank(fit)=%d  fit-alone inconsistent=%s' % (rM, incM), flush=True)
print('rank(cond)=%d  rank(joint)=%d  nullity=%d  INCONSISTENT=%s  DEFECT=%d   (%.1f s)'
      % (rC, rA, NC - rA, inc, rAug - rA, time.time() - t0), flush=True)
