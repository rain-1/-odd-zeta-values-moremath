"""Is the a_0-root exceptional step of L_BZ an APPARENT singularity?

At an exceptional step n (p | c_3(n)) the forward induction needs
    c_0(n)Y_n + c_1(n)Y_{n+1} + c_2(n)Y_{n+2} = 0  (mod p).
If no exceptional step precedes n, then (Y_n,Y_{n+1},Y_{n+2}) mod p is an F_p-LINEAR image of
the initial data (Y_0,Y_1,Y_2) mod p, so the requirement is a linear functional
    phi_n : F_p^3 -> F_p .
The step is APPARENT (automatic for every p-integral solution) iff phi_n == 0.
We evaluate phi_n on the three basis solutions.
"""
import sys
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import a0, c0, c1, B9
def c2(n): return -2*B9(n)
def c3(n): return 2*(n+3)**5*(2*n+5)*a0(n)
PR=[p for p in range(5,600) if all(p%d for d in range(2,int(p**.5)+1))]
tot=0; app=0; nonapp=0; skipped=0; genuine_nonapp=0; genuine_app=0
for p in PR:
    exc=[n for n in range(0,p-3) if c3(n)%p==0]
    if not exc: continue
    first=min(exc)
    # propagate the three basis solutions mod p up to index first+2
    sols=[]
    for e in ((1,0,0),(0,1,0),(0,0,1)):
        Y=[e[0]%p,e[1]%p,e[2]%p]
        ok=True
        for n in range(0,first):
            cc3=c3(n)%p
            if cc3==0: ok=False;break
            Y.append((-(c0(n)*Y[n]+c1(n)*Y[n+1]+c2(n)*Y[n+2]))%p*pow(cc3,p-2,p)%p)
        if not ok: sols=None;break
        sols.append(Y)
    if sols is None: skipped+=1; continue
    n=first
    phi=[(c0(n)*s[n]+c1(n)*s[n+1]+c2(n)*s[n+2])%p for s in sols]
    kind='genuine' if (2*n+5)%p==0 else 'a0'
    tot+=1
    if all(x==0 for x in phi):
        app+=1
        if kind=='genuine': genuine_app+=1
    else:
        nonapp+=1
        if kind=='genuine': genuine_nonapp+=1
        if kind=='a0':
            print('   p=%d  FIRST exceptional step n=%d is an a0-root and is NOT apparent: phi=%s'%(p,n,phi))
print('primes 5..599 with a first exceptional step analysed: %d'%tot)
print('  APPARENT (phi identically 0): %d   NOT apparent: %d'%(app,nonapp))
print('  of the non-apparent ones, genuine (2n+5) steps: %d ; apparent genuine: %d'%(genuine_nonapp,genuine_app))
# how often is the FIRST exceptional step an a0 root?
c=0
for p in PR:
    exc=[n for n in range(0,p-3) if c3(n)%p==0]
    if exc and (2*min(exc)+5)%p!=0: c+=1
print('  primes whose FIRST exceptional step is an a0 root: %d'%c)
