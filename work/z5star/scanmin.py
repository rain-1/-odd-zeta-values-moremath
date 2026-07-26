"""Minimal-ansatz measurement (JOB 2/3 prerequisite).

For a given weight, scan (denominator family, slack, force) and report which
LETTER blocks still solve.  The point is to MEASURE the denominator and the
bidegree rather than inherit the search ansatz (F1, slack 16, nc = 2178), which
was sized for a free-weight elimination and is 10^3 times larger than anything
Lean could carry.

Calibration carried in every run (the discipline of Z5CF_REP 3.1):
   * the control weight w = 1 (the Q row): its letter block set is empty, so
     instead we carry the ('h2_pk',) block of w3hat, whose answer is known to be
     SOLVABLE at order 3 (Z5CF_CERT), and the ('h1_k',) block of w3hat, whose
     answer is known to be UNSOLVABLE.
"""
import sys, os, json
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import wtools as W
import cert2
import bare, frw


def wp(v, p):
    return W.to_p(v, p)


def calib(n, B, p, dname, slack, force):
    """w3hat: h2_pk block must SOLVE, h1_k block must FAIL -- at order 3."""
    wh = wp([Fr(bare.w3hat_el().get(m, 0)) for m in B], p)
    r = cert2.letters_only(n, wh, B, dname, slack, force, p=p, verbose=False)
    d = dict(r['nb'])
    return d.get('h2_pk'), d.get('h1_k')


if __name__ == '__main__':
    import pickle
    p = W.P1
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    fam = pickle.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star/familyQ.pkl', 'rb')) \
        if os.path.exists('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star/familyQ.pkl') else None
    which = sys.argv[2] if len(sys.argv) > 2 else 'wstar'
    if which == 'wstar':
        d = json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
        wQ = [Fr(c) for c in d['coeffs']]
    else:
        wQ = pickle.load(open(which, 'rb'))
    B = W.B
    w = wp(wQ, p)
    W.show(wQ, which)
    grid = []
    for dname in ['G0', 'G3', 'G1', 'G2', 'F1']:
        for slack in [0, 2, 4, 6, 8]:
            grid.append((dname, slack))
    for force in [1]:
        for dname, slack in grid:
            try:
                r = cert2.letters_only(n, w, B, dname, slack, force, p=p)
            except Exception as e:
                print('   %s slack=%d force=%d : ERROR %s' % (dname, slack, force, e))
                continue
            if r['nfail'] == 0:
                a, b = calib(n, B, p, dname, slack, force)
                print('        CALIB w3hat: h2_pk nbad=%s (want 0), h1_k nbad=%s (want >0)'
                      % (a, b), flush=True)
