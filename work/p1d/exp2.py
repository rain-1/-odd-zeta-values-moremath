"""Cellwise:  min over (b,c) of  vT - d5   at level a < p  (M=1)."""
import sys
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/p1d')
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from w5eval import v5, Tl
from core import vp
PR=[5,7,11,13,17,19]
for p in PR:
    worst=99; arg=None; bypat={}
    for a in range(1,p):
        for b in range(a+1):
            for c in range(a+1):
                vT = vp(Tl(a,b,c),p)
                V = v5(a,b,c)
                d5 = max(0,-vp(V,p)) if V else 0
                al = 1 if a+b>=p else 0; ga = 1 if a+c>=p else 0
                eps=(b+c)//p; ka = 1 if a+b+c>=(eps+1)*p else 0
                key=(al,ga,ka,eps+1 if ka else 1)
                cur = vT-d5
                bypat[key]=min(bypat.get(key,99),cur)
                if cur<worst: worst=cur; arg=(a,b,c,vT,d5)
    print("p=%2d  min(vT-d5)=%d at (a,b,c)=%s"%(p,worst,arg))
    for k in sorted(bypat): print("      pat %s -> min(vT-d5)=%d"%(k,bypat[k]))
