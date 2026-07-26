import sys, os, json
from fractions import Fraction as Fr
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import mindens, wtools as W, cert2
p=W.P1
n=int(sys.argv[1])
dcand=json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
w=W.to_p([Fr(c) for c in dcand['coeffs']],p)
for d0 in ['M0','M2','M4','M6','M5','M7','G0','G1','F1']:
    for s0 in [8,10,12,14,16]:
        try:
            r=cert2.build(n,w,W.B,'M0',8,d0,s0,1,p=p,vnpts=0,verbose=False)
        except Exception as e:
            print('  %s s=%d ERROR %s'%(d0,s0,e)); continue
        print('  ()-ansatz %-3s slack=%-3d nc=%-5d  nbad0=%d'%(d0,s0,r['ans0'].nc,r['nbad0']),flush=True)
        if r['nbad0']==0:
            break
