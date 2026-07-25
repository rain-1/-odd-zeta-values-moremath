"""Cellwise ledger  vT - d5 + 5L,  stratified by L = floor(log_p n)."""
import sys
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/p1d')
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from w5eval import v5
from core import vp, T
JOBS=[(5,1,60),(7,1,60),(11,1,50),(13,1,40)]
for p,n0,n1 in JOBS:
    byL={}
    for n in range(n0,n1+1):
        L=0; q=n
        while q>=p: q//=p; L+=1
        PM=p**(L+1)
        for k in range(n+1):
            for l in range(n+1):
                al=1 if n+k>=PM else 0; ga=1 if n+l>=PM else 0
                eps=(k+l)//PM; ka=1 if n+k+l>=(eps+1)*PM else 0
                vT=vp(T(n,k,l),p)
                V=v5(n,k,l); d5=max(0,-vp(V,p)) if V else 0
                cur=vT-d5+5*L
                if L not in byL or cur<byL[L][0]: byL[L]=(cur,(n,k,l,vT,d5,al+ga+ka))
    print('p=%2d  '%p + '   '.join('L=%d: min(vT-d5+5L)=%d at %s'%(L,byL[L][0],byL[L][1]) for L in sorted(byL)),flush=True)
