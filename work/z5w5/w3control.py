"""END-TO-END CONTROL: run the weight-5 pipeline verbatim on WEIGHT 3, where the
answer is known (Z5CF_REP: dim W_tel = 37, and what3 IS in W_tel + K, i.e. a
representative of the Phat row with L_BZ as a telescoper EXISTS).
If this control returns NO, the weight-5 NO is a bug, not a result."""
import sys, pickle, time
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5w5')
import solve, fastlin, ratrec, zla
import w5span as W
import sum5, pd5, affine

p = int(sys.argv[1]) if len(sys.argv) > 1 else pd5.P1
N = int(sys.argv[2]) if len(sys.argv) > 2 else 220
B, T = W.span_w5(None, 3, 2)
J = len(B)
print('weight-3 span J =', J)
A3 = sum5.design(B, N, p, verbose=False)
_, piv, _ = solve.rref(A3.copy(), p)
print('rank of the weight-3 sum-map = %d -> dim K3 = %d (excess rows %d)'
      % (len(piv), J - len(piv), N + 1 - len(piv)))
w3 = np.array(W.el_to_vec(B, W.w3hat_el(), p), dtype=np.int64)
b3 = (A3.astype(object) @ w3.astype(object) % p).astype(np.int64)
affine.check_row(b3, p, 'b3 (= Phat)')
Wc = pickle.load(open(sys.argv[3], 'rb')) if len(sys.argv) > 3 else \
     pickle.load(open('Wcum_W3_F1_s16_p4194301_calib.pkl', 'rb'))
Wb = np.array(Wc, dtype=np.int64) % p
print('dim W_tel =', Wb.shape[0])
Mt = affine.mmod(A3, Wb.T, p)
x, rank, pv, nbad = fastlin.solve(Mt, b3 % p, p)
print('rank(A3 W_tel^T) = %d of %d cols ; nbad = %d  -> %s'
      % (rank, Wb.shape[0], nbad,
         'YES, W_tel MEETS the affine representative set  (control PASSES)'
         if nbad == 0 else 'NO  *** CONTROL FAILED -- the pipeline is broken ***'))
if nbad == 0:
    w = (x.astype(object) @ Wb.astype(object) % p).astype(np.int64)
    r = (affine.mmod(A3, w.reshape(-1,1), p).ravel() - b3) % p
    print('   recovered w: support %d, sum-map residual %d nonzero'
          % (int(np.count_nonzero(w)), int(np.count_nonzero(r))))
    np.save('w3star_control_p%d.npy' % p, w)
