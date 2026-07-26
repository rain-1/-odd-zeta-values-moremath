"""compute and cache W_tel(n) for a list of n, then intersect."""
import sys, os, time, pickle
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5la')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
os.chdir('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep')
import solve, o_scan
import bare, frw, run_frw


def tag(n, m, dname, slack, p, maxdeg, avec):
    a = '-' if avec is None else ','.join(str(x) for x in avec)
    return 'W_n%d_m%d_%s_s%d_p%d_d%d_a%s.pkl' % (n, m, dname, slack, p, maxdeg, a)


def getW(n, m, dname, slack, p, maxdeg, avec, force=False):
    f = tag(n, m, dname, slack, p, maxdeg, avec)
    if os.path.exists(f) and not force:
        return pickle.load(open(f, 'rb'))
    t0 = time.time()
    out = frw.run(n, m, dname, slack, avec=avec, p=p, maxdeg=maxdeg, verbose=False)
    d = dict(W=[np.array(x, dtype=np.int64) for x in out['inter']],
             info=out['info'], nc=out['nc'], npts=out['npts'], rank=out['rank'],
             blocks=out['blocks'], secs=time.time() - t0)
    pickle.dump(d, open(f, 'wb'))
    return d


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
        d = getW(n, m, dname, slack, p, maxdeg, avec)
        print('n=%3d  nc=%d rows=%d rank=%d [%.0fs]  dim W_tel(n) = %d'
              % (n, d['nc'], d['npts'], d['rank'], d['secs'], len(d['W'])), flush=True)
        # per-block detail, first n only
        if n == ns[0]:
            names = [nm for nm, _ in bare.testvecs()]
            print('      %-8s %5s  ' % ('block', 'dim') + ' '.join('%-11s' % x for x in names))
            for L, dd, fl in d['info']:
                print('      %-8s %5d  ' % (L, dd)
                      + ' '.join('%-11s' % ('YES' if a else '.') for a in fl))
        cur = d['W'] if cur is None else o_scan.intersect([cur, d['W']], J, p)
        run_frw.analyse(cur, K, B, p, tag='   cumulative through n=%d :' % n)
        pickle.dump(np.array(cur, dtype=np.int64),
                    open('Wcum_m%d_%s_s%d_p%d_d%d.pkl' % (m, dname, slack, p, maxdeg), 'wb'))
        sys.stdout.flush()
