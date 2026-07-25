"""(DEPTH-gen) test at multi-digit level:  d5(n,k,l) <= 5L + 1 + min(alpha+gamma+kappa,2)
   and vT >= alpha+gamma+kappa, and the cellwise ledger vT - d5 + 5L."""
import sys
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/p1d')
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from w5eval import v5
from core import vp, T
import sys

JOBS = [(5,1,40),(7,1,55),(11,1,45),(13,1,45)]
for p,n0,n1 in JOBS:
    badA=0; badB=0; minledger=99; argL=None; minslack=99; argS=None
    cells=0
    for n in range(n0,n1+1):
        L=0; q=n
        while q>=p: q//=p; L+=1
        PM = p**(L+1)
        for k in range(n+1):
            for l in range(n+1):
                cells+=1
                al = 1 if n+k>=PM else 0
                ga = 1 if n+l>=PM else 0
                eps = (k+l)//PM
                ka = 1 if n+k+l >= (eps+1)*PM else 0
                s = al+ga+ka
                vT = vp(T(n,k,l),p)
                if vT < s: badB+=1
                V = v5(n,k,l)
                d5 = max(0,-vp(V,p)) if V else 0
                cap = 5*L + 1 + min(s,2)
                if d5 > cap: badA+=1; print('  DEPTH-gen VIOLATION p=%d n=%d k=%d l=%d d5=%d cap=%d'%(p,n,k,l,d5,cap))
                sl = cap-d5
                if sl<minslack: minslack=sl; argS=(n,k,l,d5,cap)
                led = vT-d5+5*L
                if led<minledger: minledger=led; argL=(n,k,l,vT,d5,L,s)
    print('p=%2d n=%d..%d cells=%d  DEPTHgen-violations=%d  vT<a+g+k count=%d  min(vT-d5+5L)=%d at %s  minslack=%d at %s'
          %(p,n0,n1,cells,badA,badB,minledger,argL,minslack,argS),flush=True)
