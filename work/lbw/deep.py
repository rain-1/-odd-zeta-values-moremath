import math
from fractions import Fraction as F
from sporadic import SEQS, gen_A, gen_B
W = {'A':2,'B':2,'C':2,'D':2,'E':2,'F':2,'alpha':3,'gamma':3,'delta':3,'eps':3,'zeta':3,'eta':3,'s7':2,'s10':2,'s18':2}
DISC={'A':1,'B':-3,'C':-3,'D':1,'E':-4,'F':-3,'alpha':1,'gamma':1,'delta':1,'eps':1,'zeta':-3,'eta':5,'s7':1,'s10':1,'s18':-3}
INF=10**6
def vpi(x,p):
    if x==0: return INF
    v=0
    while x%p==0: x//=p; v+=1
    return v
def vp(x,p):
    if x==0: return INF
    return vpi(x.numerator,p)-vpi(x.denominator,p)
def chi(D,p):
    if D==1: return 1
    if D==-3: return 1 if p%3==1 else (-1 if p%3==2 else 0)
    if D==-4: return 1 if p%4==1 else -1
    if D==5: return 1 if p%5 in(1,4) else (-1 if p%5 in(2,3) else 0)
N=1200
PR=[5,7,11,67,71,73,79,83,89,97,101,103]
for lab,fam,par,fn,note in SEQS:
    A=gen_A(fam,par,N); B=gen_B(fam,par,N); w=W[lab]; D=DISC[lab]
    out=[]
    for p in PR:
        c=chi(D,p); pw=F(p)**w
        M=N if p<20 else 400
        fl=INF; nf=0
        for n in range(1,M+1):
            q=n//p
            v=vp(pw*B[n]*A[q]-c*B[q]*A[n],p)
            fl=min(fl,v)
            if v<w: nf+=1
        out.append((p,c,fl,nf,int(math.log(M,p))+1))
    print(lab,'w=',w,'| (p,chi,floor,#fail,#digits):',out, flush=True)
