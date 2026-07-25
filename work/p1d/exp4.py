"""Where does the -1 deficit live, and does it cancel in partial sums?"""
import sys
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/p1d')
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from w5eval import v5, Tl, load
import w5eval
from core import vp
from fractions import Fraction as F

for fn in ['w5_allp.json','w5_canon2.json','w5_dm_nB_desc.json']:
    w5eval.TERMS = load('/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/'+fn)
    for p in [5,7,11]:
        worst=99
        for a in range(1,p):
            for b in range(a+1):
                for c in range(a+1):
                    V=v5(a,b,c); d5=max(0,-vp(V,p)) if V else 0
                    worst=min(worst, vp(Tl(a,b,c),p)-d5)
        print('%-22s p=%2d  min(vT-d5)=%d'%(fn,p,worst),flush=True)

# partial sums, w5_allp
w5eval.TERMS = load()
print('--- partial sums over c (fixed b), and over b,c: v_p ---')
for p in [5,7,11,13]:
    minrow=99; mintot=99
    for a in range(1,p):
        tot=F(0)
        for b in range(a+1):
            rowsum=F(0)
            for c in range(a+1):
                rowsum += Tl(a,b,c)*v5(a,b,c)
            minrow=min(minrow, vp(rowsum,p) if rowsum else 99)
            tot += rowsum
        mintot=min(mintot, vp(tot,p) if tot else 99)
    print('p=%2d  min_a,b v_p(sum_c T v5)=%d   min_a v_p(W_a)=%d'%(p,minrow,mintot),flush=True)
