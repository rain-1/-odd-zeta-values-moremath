"""T7: the graded (V2)/(V3) at digit level L=1 (n >= p), via kgrade."""
import sys
from fractions import Fraction as F
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/p1f')
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/p1d')
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from kgrade import v5_upoly, pattern
from core import vp, T
p=int(sys.argv[1]); n0=int(sys.argv[2]); n1=int(sys.argv[3])
for n in range(n0,n1+1):
    L=0;q=n
    while q>=p: q//=p; L+=1
    M=L+1; cap=5*M
    S=[F(0)]*(cap+1); badcap=0; badint=0
    for k in range(n+1):
        for l in range(n+1):
            K,LL,MM=v5_upoly(n,k,l,p)
            al,ga,ka,th=pattern(n,k,l,p,MM); s=al+ga+ka
            J=0 if s==0 else 1+min(s,2)
            for j in range(5*L+J+1,cap+1):
                if K[j]: badcap+=1
            for j in range(cap+1):
                if K[j] and vp(K[j],p)<0: badint+=1
            t=T(n,k,l)
            for j in range(cap+1): S[j]+=t*K[j]
    fails=[j for j in range(cap+1) if S[j] and vp(S[j],p)<j-5*L]
    print('p=%d n=%2d L=%d  capviol=%d nonint=%d  v_p(S_j)-(j-5L) fails at j=%s   [S_%d..: %s]'
          %(p,n,L,badcap,badint,fails,5*L+1,[vp(S[j],p) if S[j] else None for j in range(5*L+1,cap+1)]),flush=True)
