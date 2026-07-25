"""Phase 2 (exact p-adic): the ACTUAL (GAP-DESC) statement, off-regime, multi-digit a.

   E(n,k,l) := p^5 v5(n,k,l) - v5(a, k//p, l//p),      a = n//p
   claim    :  v_p( T(n,k,l) * E(n,k,l) )  >=  -5 (L-1),   L = floor(log_p n)

Sweeps every OFF-REGIME cell (s>r or t>r or e1+e2+e3+e4>0) of the requested levels.
Also records, per cell, the slack, and the slack of the crude bound.
Usage:  python3 s3_exact.py [jobfile-tag]
"""
import sys, collections, time
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1i')
from pad import Ctx, Level, load_w5
from kummer import car, logp, Jcap, vT

W5 = sys.argv[2] if len(sys.argv) > 2 else \
    '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/w5_allp.json'
TERMS = load_w5(W5)


def run(p, n, K=48, report=True):
    L = logp(n, p)
    assert L >= 1
    a, r = divmod(n, p)
    ctx = Ctx(p, K)
    lev_n = Level(ctx, n, TERMS)
    lev_a = Level(ctx, a, TERMS)
    v5a = [[lev_a.v5(b, c) for c in range(a + 1)] for b in range(a + 1)]
    tgt = -5 * (L - 1)
    cn = [car(n, k, p) for k in range(n + 1)]
    dk = [car(k, n - k, p) for k in range(n + 1)]
    cj = [car(n, j, p) for j in range(2 * n + 1)]
    nfail = 0; ncell = 0; minslack = 10 ** 9; arg = None
    slackhist = collections.Counter()
    for k in range(n + 1):
        b, s = divmod(k, p)
        e1 = 1 if r + s >= p else 0
        for l in range(k, n + 1):
            c, t = divmod(l, p)
            e2 = 1 if r + t >= p else 0
            e3 = (r + s + t) // p
            e4 = 1 if s + t >= p else 0
            if not (s > r or t > r or e1 or e2 or e3 or e4):
                continue
            ncell += 1
            x = lev_n.v5(k, l)
            x = (x[0] + 5, x[1], x[2])
            E = ctx.sub(x, v5a[b][c])
            vE = E[0]                      # exact if E[1]!=0, else a lower bound
            v = cn[k] + 2 * dk[k] + cn[l] + 2 * dk[l] + cj[k + l]
            slack = v + vE - tgt
            slackhist[min(slack, 9)] += 1
            if slack < minslack:
                minslack = slack; arg = (n, k, l, b, c, s, t, (e1, e2, e3, e4), v, vE)
            if slack < 0:
                nfail += 1
                if nfail <= 5:
                    print('   FAIL p=%d n=%d (k,l)=(%d,%d) b,c=%d,%d s,t=%d,%d e=%s '
                          'vT=%d v(E)=%d target=%d' %
                          (p, n, k, l, b, c, s, t, (e1, e2, e3, e4), v, vE, tgt))
    if report:
        print('p=%2d n=%4d L=%d a=%3d r=%d : off-regime cells(k<=l)=%6d  failures=%d '
              ' min slack=%d at %s' % (p, n, L, a, r, ncell, nfail, minslack, arg), flush=True)
    return ncell, nfail, minslack, slackhist


JOBSETS = {
 'lvl1': [(5, n) for n in range(5, 25)] + [(7, n) for n in range(7, 49, 2)]
         + [(11, n) for n in range(11, 121, 5)] + [(13, n) for n in range(13, 169, 7)],
 'lvl2': [(5, n) for n in (25, 26, 29, 30, 31, 49, 50, 62, 63, 99, 100, 119, 124)]
         + [(7, n) for n in (49, 50, 55, 56, 97, 98, 146, 171, 342)]
         + [(11, n) for n in (121, 122, 131, 132, 181, 242, 605)]
         + [(13, n) for n in (169, 170, 181, 182, 253, 338)],
 'lvl3': [(5, n) for n in (125, 126, 129, 130, 149, 249, 250, 312, 373, 374, 624)]
         + [(7, n) for n in (343, 344, 350, 400, 686)]
         + [(11, n) for n in (1331, 1332, 1342)],
 'lvl4': [(5, n) for n in (625, 626, 630, 750, 1250)],
}

if __name__ == '__main__':
    tag = sys.argv[1] if len(sys.argv) > 1 else 'lvl1'
    tot = totf = 0; gmin = 10 ** 9; hist = collections.Counter()
    t0 = time.time()
    for p, n in JOBSETS[tag]:
        c, f, ms, h = run(p, n)
        tot += c; totf += f; gmin = min(gmin, ms); hist.update(h)
        if time.time() - t0 > 5400:
            print('   [time budget reached]'); break
    print('== %s: off-regime cells checked = %d, FAILURES = %d, global min slack = %d'
          % (tag, tot, totf, gmin))
    print('   slack histogram (9 = >=9):', dict(sorted(hist.items())))
