"""Extract an explicit candidate representative  w in W_tel & (what3 + K)  and
run the FULL certificate (including the coupling () block) on it."""
import sys, os, pickle
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
os.chdir('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
import solve, fastlin
import bare, frw, cert


def candidate(W, K, target, p, J, prefer_zero=()):
    """find w = target - u  with u in K and w in span(W).
    i.e. solve  target = W a + K b ; return w = W a.
    prefer_zero: list of coordinate indices we try to force to 0."""
    W = np.array(W, dtype=np.int64) % p
    K = np.array(K, dtype=np.int64) % p
    M = np.concatenate([W, K], axis=0).T % p          # J x (|W|+|K|)
    x, rank, piv, nbad = fastlin.solve(M, target % p, p)
    if nbad:
        return None, nbad
    w = (x[:W.shape[0]].astype(object) @ W.astype(object)) % p
    return w.astype(np.int64), 0


def wk_basis(W, K, p):
    """basis of W & K (the freedom inside the admissible affine family)"""
    import ratrec
    W = np.array(W, dtype=np.int64) % p
    K = np.array(K, dtype=np.int64) % p
    C = np.concatenate([W.T % p, (-K.T) % p], axis=1)
    ker = ratrec.nullspace(C, p)
    out = []
    for v in ker:
        out.append((v[:W.shape[0]].astype(object) @ W.astype(object)) % p)
    if not out:
        return []
    R, piv, _ = solve.rref(np.array(out, dtype=np.int64) % p, p)
    return [R[i] for i in range(len(piv))]


if __name__ == '__main__':
    m = int(sys.argv[1]); dname = sys.argv[2]; slack = int(sys.argv[3])
    p = int(sys.argv[4]) if len(sys.argv) > 4 else frw.P
    maxdeg = int(sys.argv[5]) if len(sys.argv) > 5 else 2
    nlist = [int(x) for x in sys.argv[6].split(',')] if len(sys.argv) > 6 else [9]
    cslack = int(sys.argv[7]) if len(sys.argv) > 7 else slack
    B, tops = bare.span_w3(maxdeg=maxdeg)
    J = len(B)
    Wc = pickle.load(open('Wcum_m%d_%s_s%d_p%d_d%d.pkl' % (m, dname, slack, p, maxdeg), 'rb'))
    K = np.load('K_d%d_p%d.npy' % (maxdeg, p))
    wh = np.array(bare.el_to_vec(B, bare.w3hat_el(), p), dtype=np.int64)
    w, nbad = candidate(list(Wc), list(K), wh, p, J)
    if w is None:
        print('NO candidate: what3 not in W_tel + K (nbad=%d)' % nbad)
        sys.exit(1)
    free = wk_basis(list(Wc), list(K), p)
    print('candidate w found;  dim of the admissible affine family = %d' % len(free))
    nz = [B[j] for j in range(J) if w[j]]
    print('candidate support: %d monomials' % len(nz))
    # sanity: sum T*w = Phat ?
    A = np.load('A_d%d_p%d.npy' % (maxdeg, p)); b = np.load('b_d%d_p%d.npy' % (maxdeg, p))
    r = (A.astype(object) @ w.astype(object) - b) % p
    print('sum T*w - Phat : %d nonzero of %d rows  %s'
          % (int(np.count_nonzero(r)), len(b), '<-- REPRESENTATIVE OK' if not r.any() else '<-- BAD'))
    np.save('cand_m%d_%s_s%d_p%d_d%d.npy' % (m, dname, slack, p, maxdeg), w)
    for n in nlist:
        print('--- full cascade at n=%d ---' % n, flush=True)
        cert.run_cert(n, m, dname, cslack, w, B, p=p)
        sys.stdout.flush()
