"""JOB 2 -- the full order-3 certificate for w* with (B-bot) imposed, at the
MEASURED minimal ansatz, verified at fresh points."""
import sys, os, json, pickle, time
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import mindens
import wtools as W, cert2

p = int(sys.argv[4]) if len(sys.argv)>4 else W.P1
ns = [int(x) for x in sys.argv[1].split(',')]
d0 = sys.argv[2]; s0 = int(sys.argv[3])
dcand = json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
wQ = [Fr(c) for c in dcand['coeffs']]
w = W.to_p(wQ, p)
for n in ns:
    r = cert2.build(n, w, W.B, 'M0', 8, d0, s0, 1, p=p, vnpts=400)
    pickle.dump(dict(coefL=r['coefL'], x0=r['x0'], act=r['act'], n=n, p=p,
                     bad=r['bad'], nbad0=r['nbad0'], nbadL=r['nbadL']),
                open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star/cof_n%d_p%d.pkl'%(n,p),'wb'))
