"""STEP 3 -- is the desingularised order-4 left multiple L-tilde a telescoper of
T.w for ANY weight w in the bare span?  (a-direction fixed = L-tilde's)"""
import sys, os, pickle
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
os.chdir('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
import o_scan
import bare, frw, ltilde, run_frw

if __name__ == '__main__':
    ns = [int(x) for x in sys.argv[1].split(',')]
    dname = sys.argv[2]; slack = int(sys.argv[3])
    p = int(sys.argv[4]) if len(sys.argv) > 4 else frw.P
    B, tops = bare.span_w3(maxdeg=2)
    J = len(B)
    K = np.load('K_d2_p%d.npy' % p)
    cur = None
    for n in ns:
        a = ltilde.avec(n, p)
        out = frw.run(n, 4, dname, slack, avec=a, p=p, maxdeg=2, verbose=True)
        W = out['inter']
        cur = W if cur is None else o_scan.intersect([cur, W], J, p)
        run_frw.analyse(cur, K, B, p, tag='   L-tilde cumulative through n=%d :' % n)
        pickle.dump(np.array(cur, dtype=np.int64),
                    open('Wcum_ltilde_%s_s%d_p%d.pkl' % (dname, slack, p), 'wb'))
        sys.stdout.flush()
