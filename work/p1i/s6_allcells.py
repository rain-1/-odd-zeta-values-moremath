"""Phase 5: the WHOLE descent term (I), both regimes, cell by cell:

      v_p( T(n,k,l) * E(n,k,l) )  >=  -5(L-1)      for EVERY cell 0<=k,l<=n,
      E = p^5 v5(n,k,l) - v5(a, k//p, l//p).

Reports in-regime and off-regime separately (the in-regime half is
PHASE2_INDUCTION Sec.4.3 [PROVED]; the off-regime half is the (GAP-DESC) node).
Also aggregates  v_p( sum_{k,l} T*E )  -- the quantity the induction actually needs.
"""
import sys, collections
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1i')
from pad import Ctx, Level, load_w5
from kummer import car, logp

W5 = '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/w5_allp.json'
TERMS = load_w5(W5)


def run(p, n, K=48):
    L = logp(n, p); a, r = divmod(n, p)
    ctx = Ctx(p, K)
    lev_n = Level(ctx, n, TERMS); lev_a = Level(ctx, a, TERMS)
    v5a = [[lev_a.v5(b, c) for c in range(a + 1)] for b in range(a + 1)]
    tgt = -5 * (L - 1)
    cn = [car(n, k, p) for k in range(n + 1)]
    dk = [car(k, n - k, p) for k in range(n + 1)]
    cj = [car(n, j, p) for j in range(2 * n + 1)]
    res = {'in': [0, 0, 99], 'off': [0, 0, 99]}     # cells, failures, minslack
    acc = ctx.zero(ctx.K)                            # sum_{k,l} T * E  (all cells)
    for k in range(n + 1):
        b, s = divmod(k, p)
        e1 = 1 if r + s >= p else 0
        for l in range(n + 1):
            c, t = divmod(l, p)
            e2 = 1 if r + t >= p else 0
            e3 = (r + s + t) // p
            e4 = 1 if s + t >= p else 0
            off = (s > r or t > r or e1 or e2 or e3 or e4)
            x = lev_n.v5(k, l); x = (x[0] + 5, x[1], x[2])
            E = ctx.sub(x, v5a[b][c])
            v = cn[k] + 2 * dk[k] + cn[l] + 2 * dk[l] + cj[k + l]
            slack = v + E[0] - tgt
            key = 'off' if off else 'in'
            res[key][0] += 1
            if slack < 0:
                res[key][1] += 1
                if res[key][1] <= 3:
                    print('   FAIL[%s] p=%d n=%d (k,l)=(%d,%d) vT=%d v(E)=%d tgt=%d'
                          % (key, p, n, k, l, v, E[0], tgt))
            res[key][2] = min(res[key][2], slack)
            acc = ctx.add(acc, ctx.mul(ctx.fromint(1, K), (E[0] + v, E[1], E[2])))
    print('p=%2d n=%4d L=%d : in-regime cells=%6d fail=%d minslack=%d | off-regime cells=%6d '
          'fail=%d minslack=%d | v_p(sum T*E) >= %d (target %d)'
          % (p, n, L, res['in'][0], res['in'][1], res['in'][2],
             res['off'][0], res['off'][1], res['off'][2], acc[0], tgt), flush=True)
    return res


if __name__ == '__main__':
    JOBS = [(5, 25), (5, 26), (5, 33), (5, 44), (5, 60), (5, 99), (5, 124),
            (7, 49), (7, 50), (7, 62), (7, 97), (7, 150),
            (11, 121), (11, 130), (11, 200), (13, 169), (13, 180),
            (5, 125), (5, 130), (7, 343)]
    tin = tof = fin = fof = 0; msin = msof = 99
    for p, n in JOBS:
        r = run(p, n)
        tin += r['in'][0]; fin += r['in'][1]; msin = min(msin, r['in'][2])
        tof += r['off'][0]; fof += r['off'][1]; msof = min(msof, r['off'][2])
    print('TOTAL in-regime: %d cells, %d failures, min slack %d' % (tin, fin, msin))
    print('TOTAL off-regime: %d cells, %d failures, min slack %d' % (tof, fof, msof))
