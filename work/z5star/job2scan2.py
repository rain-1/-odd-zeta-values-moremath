import sys, os, json
from fractions import Fraction as Fr
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import mindens, wtools as W, cert2
p=W.P1
n=int(sys.argv[1])
dcand=json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
w=W.to_p([Fr(c) for c in dcand['coeffs']],p)
for force in [0,1]:
  for dL,sL in [('M0',8),('M0',12),('M0',16),('M0',20),('F1',8)]:
    for d0,s0 in [('M0',12),('M0',16),('F1',10)]:
        r=cert2.build(n,w,W.B,dL,sL,d0,s0,force,p=p,vnpts=0,verbose=False)
        print('  force=%d letters %s/s%-2d (nc=%d ker=%d)  () %s/s%-2d (nc=%d) : nbadL=%d nbad0=%d'
              %(force,dL,sL,r['ansL'].nc,r['nk'],d0,s0,r['ans0'].nc,r['nbadL'],r['nbad0']),flush=True)
