"""Does the admissible weight space W_tel meet the AFFINE SET of representatives
of the P row,  w5 + K5 ?

   K5 = { w : sum_{k,l} T(n,k,l) w(n,k,l) = 0 for every n }   (sum5.py)
   the question is  { w in W_tel : A5 w = b5 }  with  b5 = (P_n)_n .
"""
import sys, pickle
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5w5')
import solve, fastlin, ratrec, zla
import w5span as W
import pd5


def mmod(A, B, p):
    A = np.asarray(A, dtype=np.int64) % p
    B = np.asarray(B, dtype=np.int64) % p
    out = np.zeros((A.shape[0], B.shape[1]), dtype=np.int64)
    blk = 400
    for i in range(0, A.shape[1], blk):
        out = (out + (A[:, i:i + blk].astype(np.float64)
                      @ B[i:i + blk].astype(np.float64)).astype(np.int64)) % p
    return out


def check_row(b, p, name='b5'):
    """L_BZ . b == 0 ?"""
    bad = 0
    for n in range(len(b) - 3):
        c = zla.cc(n)
        v = sum((c[i] % p) * int(b[n + i]) for i in range(4)) % p
        if v:
            bad += 1
    print('   L_BZ . %s = 0 for n = 0..%d : %d nonzero of %d'
          % (name, len(b) - 4, bad, len(b) - 3))
    return bad


def run(wfile, p=pd5.P1, Wt=5, maxdeg=3, symbols=None):
    B, T = W.span_w5(symbols, Wt, maxdeg)
    J = len(B)
    A5 = np.load('A5_p%d.npy' % p)
    b5 = np.load('b5_p%d.npy' % p)
    K5 = np.load('K5_p%d.npy' % p)
    w5 = np.load('w5vec_p%d.npy' % p)
    Wc = pickle.load(open(wfile, 'rb'))
    Wb = np.array(Wc, dtype=np.int64) % p if len(Wc) else np.zeros((0, J), np.int64)
    print('J=%d  rows of A5=%d  dim K5=%d  dim W_tel=%d' % (J, A5.shape[0], len(K5), Wb.shape[0]))
    check_row(b5, p)
    r = (mmod(A5, w5.reshape(-1, 1), p).ravel() - b5) % p
    print('   A5 w5 - b5 : %d nonzero rows (must be 0)' % int(np.count_nonzero(r)))
    if Wb.shape[0] == 0:
        print('   W_tel is ZERO -> no representative')
        return
    Mt = mmod(A5, Wb.T, p)                       # (N+1) x dimW
    x, rank, piv, nbad = fastlin.solve(Mt, b5 % p, p)
    print('   rank(A5 W_tel^T) = %d of %d columns ; inconsistency rows nbad = %d'
          % (rank, Wb.shape[0], nbad))
    if nbad:
        print('   >>> NO: W_tel does NOT meet the affine representative set')
        print('   >>> excess rows available for the verdict: %d' % (A5.shape[0] - rank))
        return None
    w = (x.astype(object) @ Wb.astype(object)) % p
    w = w.astype(np.int64)
    rr = (mmod(A5, w.reshape(-1, 1), p).ravel() - b5) % p
    print('   >>> YES: found w in W_tel with A5 w = b5 ; residual %d nonzero'
          % int(np.count_nonzero(rr)))
    print('   support of w : %d monomials of %d' % (int(np.count_nonzero(w)), J))
    # freedom = W_tel & K5
    C = np.concatenate([Wb.T % p, (-np.array(K5, dtype=np.int64).T) % p], axis=1)
    ker = ratrec.nullspace(C, p)
    free = []
    for v in ker:
        free.append((v[:Wb.shape[0]].astype(object) @ Wb.astype(object)) % p)
    if free:
        R, pv, _ = solve.rref(np.array(free, dtype=np.int64) % p, p)
        free = [R[i] for i in range(len(pv))]
    print('   dim (W_tel & K5) = %d  -> the admissible affine family is %d-dimensional'
          % (len(free), len(free)))
    np.save(wfile.replace('.pkl', '_w.npy'), w)
    pickle.dump([np.array(u) for u in free], open(wfile.replace('.pkl', '_free.pkl'), 'wb'))
    return w, free


if __name__ == '__main__':
    run(sys.argv[1], p=int(sys.argv[2]) if len(sys.argv) > 2 else pd5.P1,
        Wt=int(sys.argv[3]) if len(sys.argv) > 3 else 5,
        maxdeg=int(sys.argv[4]) if len(sys.argv) > 4 else 3)
