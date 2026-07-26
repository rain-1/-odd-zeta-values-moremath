"""Does a LARGER letter-block gauge rescue the () block's (B-bot)?"""
import sys,os,json
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import mindens, wtools as W, cert4
p=W.P1; n=int(sys.argv[1])
dc=json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
w=W.to_p([Fr(c) for c in dc['coeffs']],p)
for sL,d0,s0 in [(12,'M0',12),(16,'M0',12),(16,'M0',16),(20,'M0',16)]:
    r=cert4.build(n,w,W.B,'M0',sL,d0,s0,p=p,vnpts=0,verbose=False,bbot=True)
    print('  letters M0/s%-2d (nc=%d ker=%d)  () %s/s%-2d nc=%-5d : nbadL=%d  Bbot-augmented nbad0=%d %s'
          %(sL,r['ansL'].nc,r['nk'],d0,s0,r['ans0'].nc,r['nbadL'],r['nbad0'],
            '<<< (B-bot) ACHIEVED' if r['nbad0']==0 else ''),flush=True)
