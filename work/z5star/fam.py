"""JOB 1 step A -- recover the ADMISSIBLE AFFINE FAMILY as an explicit object.

work/z5rep/joint.py computes the lam-space (13-dim inside the 17-dim
ws-coordinates  ws = [w0, u_1..u_16],  u_i a basis of W_tel & K) but only saves
one member.  Here we save the whole cumulative lam-space, so that JOB 1 can
optimise over it.

Output:  famlam_p<P>.pkl   {lam: [vectors in ws-coords], ws: [17 weight vectors],
                            ns: the n used, B: the 109-monomial basis}
"""
import sys, os, time, pickle
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
os.chdir('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
import joint          # MUST precede frw: frw prepends ../z5la, which also has a joint.py
assert joint.__file__.endswith('z5rep/joint.py'), joint.__file__
import o_scan
import bare, frw, extract

OUT = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'


def build_ws(B, p):
    J = len(B)
    Wc = pickle.load(open('Wcum_m3_F1_s16_p%d_d2.pkl' % p, 'rb'))
    K = np.load('K_d2_p%d.npy' % p)
    wh = np.array(bare.el_to_vec(B, bare.w3hat_el(), p), dtype=np.int64)
    w0, nb = extract.candidate(list(Wc), list(K), wh, p, J)
    assert nb == 0
    free = extract.wk_basis(list(Wc), list(K), p)
    ws = [w0] + [np.array(u, dtype=np.int64) for u in free]
    return ws, np.array(K, dtype=np.int64)


if __name__ == '__main__':
    ns = [int(x) for x in sys.argv[1].split(',')]
    slackL = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    slack0 = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    p = int(sys.argv[4]) if len(sys.argv) > 4 else frw.P
    B, tops = bare.span_w3(maxdeg=2)
    ws, K = build_ws(B, p)
    nw = len(ws)
    print('ws: %d vectors (1 base + %d free directions in W_tel & K)' % (nw, nw - 1),
          flush=True)
    # calibration: the control weight w = 1 (Q row) must close
    ctrl = np.zeros(len(B), dtype=np.int64); ctrl[B.index(())] = 1
    lc, _ = joint.run(ns[0], [ctrl], B, slackL, slack0, p=p)
    print('   CONTROL w=1 : %s' % ('ansatz ADEQUATE' if lc else '*** TOO SMALL ***'),
          flush=True)
    cur = None
    for n in ns:
        t0 = time.time()
        lam, nb = joint.run(n, ws, B, slackL, slack0, p=p)
        cur = lam if cur is None else o_scan.intersect([cur, lam], nw, p)
        good = [v for v in cur if v[0] % p]
        print('   >>> cumulative through n=%d : dim %d ; lam_0 != 0 : %s  [%.0fs]'
              % (n, len(cur), 'YES' if good else 'NO', time.time() - t0), flush=True)
        pickle.dump(dict(lam=[np.array(v) for v in cur], ws=ws, ns=ns, p=p,
                         B=B, nw=nw),
                    open(os.path.join(OUT, 'famlam_p%d.pkl' % p), 'wb'))
    print('saved famlam_p%d.pkl' % p, flush=True)
