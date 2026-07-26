import sys, os, json
from fractions import Fraction as Fr
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import mindens, wtools as W, cert5
p = int(sys.argv[2]) if len(sys.argv)>2 else W.P1
dc=json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
w=W.to_p([Fr(c) for c in dc['coeffs']],p)
for n in [int(x) for x in sys.argv[1].split(',')]:
    r=cert5.build(n,w,W.B,'M0',8,'M0',12,p=p,vnpts=400)
    cert5.bbot_verify(n,w,W.B,r,p)
