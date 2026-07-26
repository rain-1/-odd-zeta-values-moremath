"""GUARD 1 at degree 4: the end-to-end weight-3 control run through the
DEGREE-4 code path (sum5d4.design + scan5 + affine).  It must still return YES
with 0 inconsistency rows, otherwise the degree-4 negative means nothing."""
import sys, pickle
import numpy as np
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/z5w5')
import solve, fastlin, ratrec
import w5span as W
import sum5d4, pd5, scan5, affine

p = int(sys.argv[1]) if len(sys.argv) > 1 else pd5.P1
N = int(sys.argv[2]) if len(sys.argv) > 2 else 220
B, T = W.span_w5(None, 3, 2)
J = len(B)
A3 = sum5d4.design(B, N, p, verbose=False)          # <-- the degree-4 code path
_, piv, _ = solve.rref(A3.copy(), p)
print('weight-3 sum map through sum5d4: J=%d rank=%d dim K=%d excess rows=%d'
      % (J, len(piv), J - len(piv), N + 1 - len(piv)))
w3 = np.array(W.el_to_vec(B, W.w3hat_el(), p), dtype=np.int64)
b3 = (A3.astype(object) @ w3.astype(object) % p).astype(np.int64)
affine.check_row(b3, p, 'b3 (= Phat)')
r = scan5.run(9, 'F1', 16, p=p, Wt=3, maxdeg=2)
Wb = np.array(r['ns'], dtype=np.int64) % p
# same, on the SYMMETRIC subspace (the degree-4 gate is run there)
idx = {m: j for j, m in enumerate(B)}
orb = []; seen = set()
for m in B:
    if m in seen: continue
    sm = W.sigma_mono(m); seen.add(m); seen.add(sm)
    orb.append((idx[m],) if sm == m else (idx[m], idx[sm]))
S = np.zeros((J, len(orb)), dtype=np.int64)
for t, o in enumerate(orb):
    for j in o: S[j, t] = 1
for lab, M, target in (('full space', Wb, None),):
    Mt = affine.mmod(A3, M.T, p)
    x, rank, pv, nbad = fastlin.solve(Mt, b3 % p, p)
    print('   %-12s dim W = %d ; rows = %d ; rank = %d ; nbad = %d -> %s'
          % (lab, M.shape[0], A3.shape[0], rank, nbad, 'YES' if nbad == 0 else '*** NO -- CONTROL FAILED ***'))
C = np.concatenate([Wb.T % p, (-S) % p], axis=1)
ker = ratrec.nullspace(C, p)
rows = [(v[:Wb.shape[0]].astype(object) @ Wb.astype(object)) % p for v in ker]
Ws = np.array(rows, dtype=np.int64) % p
R, pv2, _ = solve.rref(Ws.copy(), p); Ws = R[:len(pv2)]
Mt = affine.mmod(A3, Ws.T, p)
x, rank, pv, nbad = fastlin.solve(Mt, b3 % p, p)
print('   symmetric   dim W^sym = %d ; rows = %d ; ratio = %.2f ; rank = %d ; nbad = %d -> %s'
      % (Ws.shape[0], A3.shape[0], A3.shape[0] / Ws.shape[0], rank, nbad,
         'YES  (control PASSES)' if nbad == 0 else '*** NO -- CONTROL FAILED ***'))
