import sys, os, json, pickle
from fractions import Fraction as Fr
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star')
import mindens, wtools as W, cert3
p = int(sys.argv[4]) if len(sys.argv)>4 else W.P1
ns=[int(x) for x in sys.argv[1].split(',')]
d0=sys.argv[2]; s0=int(sys.argv[3])
dc=json.load(open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep/wjoint_p4194301_Q.json'))
w=W.to_p([Fr(c) for c in dc['coeffs']],p)
for n in ns:
    r=cert3.build(n,w,W.B,'M0',8,d0,s0,p=p,vnpts=400)
    cert3.bbot_check(n,w,W.B,r,p)
    pickle.dump(dict(coefL=r['coefL'],x0=r['x0'],act=r['act'],forces=r['forces'],
                     n=n,p=p,bad=r['bad'],nbad0=r['nbad0'],nbadL=r['nbadL'],
                     dL='M0',sL=8,d0=d0,s0=s0),
        open('/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star/cof_n%d_p%d.pkl'%(n,p),'wb'))
