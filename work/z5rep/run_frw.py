"""driver: run the free-weight scan, save the admissible subspace, and compare
it with the kernel K and with the affine representative set  what3 + K."""
import sys, time, pickle
import numpy as np
sys.path.insert(0, '../z5la')
import solve
import bare, frw


def rank(M, p):
    if len(M) == 0:
        return 0
    return len(solve.rref(np.array(M, dtype=np.int64).copy() % p, p)[1])


def analyse(W, K, B, p, tag=''):
    J = len(B)
    tv = [(nm, np.array(bare.el_to_vec(B, el, p), dtype=np.int64))
          for nm, el in bare.testvecs()]
    rW = rank(W, p); rK = rank(K, p)
    both = list(W) + list(K)
    rWK = rank(both, p)
    print('%s dim W_tel = %d   dim K = %d   dim(W+K) = %d   dim(W&K) = %d'
          % (tag, rW, rK, rWK, rW + rK - rWK))
    for nm, v in tv:
        inW = rank(list(W) + [v], p) == rW
        inWK = rank(both + [v], p) == rWK
        print('   %-7s in W_tel: %-3s   in W_tel+K: %-3s'
              % (nm, 'YES' if inW else 'no', 'YES' if inWK else 'no'))
    return rW, rK, rWK


if __name__ == '__main__':
    n = int(sys.argv[1]); m = int(sys.argv[2]); dname = sys.argv[3]
    slack = int(sys.argv[4])
    p = int(sys.argv[5]) if len(sys.argv) > 5 else frw.P
    maxdeg = int(sys.argv[6]) if len(sys.argv) > 6 else 2
    avec = None
    if len(sys.argv) > 7:
        avec = [int(x) for x in sys.argv[7].split(',')]
    out = frw.run(n, m, dname, slack, avec=avec, p=p, maxdeg=maxdeg)
    B = out['B']
    W = out['inter']
    K = np.load('K_d%d_p%d.npy' % (maxdeg, p)) if p == frw.P else None
    if K is None:
        import sumrows
        A = sumrows.design(B, 220, p)
        K = np.array(sumrows.nullsp(A, p), dtype=np.int64)
    analyse(W, K, B, p, tag='n=%d m=%d %s s=%d p=%d :' % (n, m, dname, slack, p))
    pickle.dump(dict(W=[np.array(x) for x in W],
                     info=out['info'], blocks=out['blocks'],
                     nc=out['nc'], npts=out['npts'], rank=out['rank']),
                open('frw_n%d_m%d_%s_s%d_p%d.pkl' % (n, m, dname, slack, p), 'wb'))
