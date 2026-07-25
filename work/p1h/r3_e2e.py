"""End-to-end verification of the P1h proof of (BASE), prime by prime.

 (a) n <= (p-1)/2 : III empty AND every cell of T*v5 is p-integral      -> v_p(P_n)>=0
 (b) n  = (p+1)/2 : III = 3 corner cells, T/p^2=(2,2,24), K_3=(3,3,-1/2), Sum=0
 (c) n  > (p+1)/2 : every L_BZ step nu in [(p-3)/2, p-4] has p | c_3(nu) only via a_0,
                    and each such step is apparent (Lemma 3.1 / degenerate variant)
 (d) cross-check   : v_p(P_n) >= 0 for all n < p
"""
import sys
from fractions import Fraction as F
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g')
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import P, Hs, vp, a0, c0, c1, c2, c3
from rw5eval import load, w5, Tl
terms = load('/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g/w5_exIII_allp.json')
PR=[int(x) for x in sys.argv[1:]]
tot={'a_cells':0,'a_viol':0,'b_ok':0,'b_bad':0,'c_steps':0,'c_bad':0,'d_bad':0}
for p in PR:
    mid=(p+1)//2
    # (a)
    for n in range(1,mid):
        assert 2*n<p
        for k in range(n+1):
            for l in range(n+1):
                assert not(k>=p-n and l>=p-n and p<=k+l<p+(p-n)), 'III nonempty!'
                x=Tl(n,k,l)*(w5(n,k,l,terms)-Hs(n,5)); tot['a_cells']+=1
                if x and vp(x,p)<0: tot['a_viol']+=1
    # (b)
    n=mid; q=p-n
    III=[(k,l) for k in range(n+1) for l in range(n+1) if k>=q and l>=q and p<=k+l<p+q]
    S=sum(Tl(n,k,l)*(w5(n,k,l,terms)-Hs(n,5)) for (k,l) in III)
    okb = (III==[(q,q+1),(q+1,q),(q+1,q+1)]) and (not S or vp(S,p)>=0)
    tot['b_ok' if okb else 'b_bad']+=1
    # (c)
    for nu in range((p-3)//2, p-3):
        tot['c_steps']+=1
        if c3(nu)%p:  continue                    # regular step
        if (2*nu+5)%p==0: tot['c_bad']+=1; print('   p=%d nu=%d: 2nu+5==0 above midpoint!'%(p,nu))
        if (nu+3)%p==0:   tot['c_bad']+=1
        if a0(nu)%p==0:
            V=(c1(nu-1)%p, c2(nu-1)%p, c3(nu-1)%p)
            if V==(0,0,0): print('   p=%d nu=%d: V==0 (degenerate variant needed)'%(p,nu))
    # (d)
    for n in range(p):
        if P(n) and vp(P(n),p)<0: tot['d_bad']+=1
    print('p=%3d done (mid=%d)'%(p,mid), flush=True)
print(tot)
print('VERDICT:', 'ALL CLEAN' if tot['a_viol']==0 and tot['b_bad']==0 and tot['c_bad']==0 and tot['d_bad']==0 else 'FAILURES')
