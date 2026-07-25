"""P1h R2: the critical level n=(p+1)/2 -- region III collapses to THREE CORNER CELLS.

q=(p-1)/2, n=q+1.  III = {(k,l): k,l>=q, p<=k+l<p+q}  =  {(q,q+1),(q+1,q),(q+1,q+1)}
                                                      =  {(n-1,n),(n,n-1),(n,n)}.
Check: cell-wise residues, the k<->l symmetry, the predicted T/p^2 values (2,2,24),
and Sum_III = 0 (mod p).
"""
import sys, json
from fractions import Fraction as F
from math import comb
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g')
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import P, Hs, vp
from rw5eval import load, w5, Tl

FN = sys.argv[1] if len(sys.argv)>1 else '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g/w5_exIII_allp.json'
terms = load(FN)
PRIMES=[p for p in (5,7,11,13,17,19,23,29,31)]
print('rep:',FN.split('/')[-1])
for p in PRIMES:
    n=(p+1)//2; q=p-n
    III=[(k,l) for k in range(n+1) for l in range(n+1)
         if k>=q and l>=q and p<=k+l<p+q]
    print('p=%2d n=%2d q=%2d  III=%s'%(p,n,q,III))
    tot=F(0)
    for (k,l) in III:
        T=Tl(n,k,l); v5=w5(n,k,l,terms)-Hs(n,5); x=T*v5
        tot+=x
        # predicted T/p^2 mod p
        print('    (k,l)=(%2d,%2d)  v_p(T)=%d  v_p(T*v5)=%s  (T/p^2 mod p)=%s'
              %(k,l,vp(T,p),vp(x,p) if x else 'inf',
                (T//p**2)%p if vp(T,p)>=2 else 'n/a'))
    print('    Sum_III: v_p=%s   v_p(P_n)=%s   [need >=0]'
          %(vp(tot,p) if tot else 'inf', vp(P(n),p) if P(n) else 'inf'))
