"""Intersect the admissible weight subspaces W_tel(n) over several n (the weight
coefficients are CONSTANTS, so a certificate valid for all n needs w in the
intersection), then test  w3hat in (cap_n W_tel(n)) + K."""
import sys, time, pickle
import numpy as np
sys.path.insert(0, '../z5la')
import solve, o_scan
import bare, frw, run_frw

if __name__ == '__main__':
    ns = [int(x) for x in sys.argv[1].split(',')]
    m = int(sys.argv[2]); dname = sys.argv[3]; slack = int(sys.argv[4])
    p = int(sys.argv[5]) if len(sys.argv) > 5 else frw.P
    maxdeg = int(sys.argv[6]) if len(sys.argv) > 6 else 2
    avec = None
    if len(sys.argv) > 7 and sys.argv[7] != '-':
        avec = [int(x) for x in sys.argv[7].split(',')]
    B, tops = bare.span_w3(maxdeg=maxdeg)
    J = len(B)
    K = np.load('K_d%d_p%d.npy' % (maxdeg, p))
    cur = None
    for n in ns:
        out = frw.run(n, m, dname, slack, avec=avec, p=p, maxdeg=maxdeg,
                      verbose=False)
        W = out['inter']
        print('n=%3d  nc=%d rows=%d  dim W_tel(n) = %d' % (n, out['nc'], out['npts'], len(W)),
              flush=True)
        cur = W if cur is None else o_scan.intersect([cur, W], J, p)
        run_frw.analyse(cur, K, B, p, tag='   cumulative through n=%d :' % n)
        pickle.dump(np.array(cur, dtype=np.int64),
                    open('Wcum_m%d_%s_s%d_p%d_d%d.npy' % (m, dname, slack, p, maxdeg), 'wb'))
