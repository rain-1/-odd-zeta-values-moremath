"""Fine minimal-ansatz measurement: which DENOMINATOR and which BIDEGREE do the
letter blocks actually need, with (B-bot) imposed?  Measured, not guessed."""
import sys, os
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import wtools as W
import cert2
import bare, frw, ordm, solve
from solve import Ansatz

LOG = '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star'


def dens3(m=3):
    K1, L1 = ordm.K1, ordm.L1
    NK, NL, NKL = ordm.NK, ordm.NL, ordm.NKL
    KL = [(j, 0, 1, 1) for j in range(0, 12)]
    for _j in range(12):
        solve.NAMES[KL[_j]] = 'k+l+%d' % _j
    out = {}
    # H-family: strip G0 down one factor at a time
    out['H0'] = [(K1, 3), (L1, 3), (KL[1], 1), (KL[2], 1)] \
        + [(NK[j], 1) for j in range(1, 4)] + [(NL[j], 1) for j in range(1, 4)]
    out['H1'] = out['H0'] + [(NKL[1], 1)]                       # = G0
    out['H2'] = [(K1, 3), (L1, 3), (KL[1], 1), (KL[2], 1)] \
        + [(NK[j], 1) for j in range(1, 4)] + [(NL[j], 1) for j in range(1, 4)] \
        + [(NKL[j], 1) for j in range(1, 4)]
    out['H3'] = [(K1, 3), (L1, 3), (KL[1], 1)] \
        + [(NK[j], 1) for j in range(1, 4)] + [(NL[j], 1) for j in range(1, 4)]
    out['H4'] = [(K1, 4), (L1, 4), (KL[1], 1), (KL[2], 1)] \
        + [(NK[j], 1) for j in range(1, 4)] + [(NL[j], 1) for j in range(1, 4)] \
        + [(NKL[1], 1)]
    out['H5'] = [(K1, 3), (L1, 3), (KL[1], 1), (KL[2], 1)] \
        + [(NK[j], 2) for j in range(1, 4)] + [(NL[j], 2) for j in range(1, 4)] \
        + [(NKL[1], 1)]
    return out


cert2._dens3 = dens3
_orig = cert2.dens2


def dens2(m=3):
    out = dict(_orig(m))
    out.update(dens3(m))
    return out


cert2.dens2 = dens2


if __name__ == '__main__':
    import json
    p = W.P1
    ns = [int(x) for x in sys.argv[1].split(',')]
    d = json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
    wQ = [Fr(c) for c in d['coeffs']]
    w = W.to_p(wQ, p)
    B = W.B
    for n in ns:
        print('=== n = %d ===' % n, flush=True)
        for dname in ['H3', 'H0', 'H1', 'H2', 'H4', 'H5']:
            for slack in range(0, 15):
                r = cert2.letters_only(n, w, B, dname, slack, 1, p=p, verbose=False)
                if r['nfail'] == 0:
                    ans = r['ans']
                    print('   %-3s : FIRST SOLVES at slack=%d  bidegree=(%d,%d) '
                          'nc=%d rank=%d ker=%d'
                          % (dname, slack, ans.par[0], ans.par[1], ans.nc,
                             r['rank'], ans.nc - r['rank']), flush=True)
                    break
            else:
                print('   %-3s : does not solve up to slack 14' % dname, flush=True)
