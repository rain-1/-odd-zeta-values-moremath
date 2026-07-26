import sys,json
from fractions import Fraction as Fr
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import mindens, wtools as W, cert4
p=W.P1
d=json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
w=W.to_p([Fr(c) for c in d['coeffs']],p)
for n in [0,1,2,3,4,5]:
    try:
        r=cert4.build(n,w,W.B,'M0',8,'M0',12,p=p,vnpts=200,verbose=False,bbot=False)
        print('  n=%d : nbadL=%d nbad0=%d  fresh-point failures: %s'%(n,r['nbadL'],r['nbad0'],
              'NONE' if not r['bad'] else r['bad']),flush=True)
    except Exception as e:
        print('  n=%d : ERROR %s'%(n,e),flush=True)
