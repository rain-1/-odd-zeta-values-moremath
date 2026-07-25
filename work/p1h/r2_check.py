"""Cross-check the symbolic K_3 against exact p-adic arithmetic, and probe how much
of the identity is representative-independent."""
import sys, json
from fractions import Fraction as F
import sympy as sp
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g')
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
from core import P, Hs, vp
from rw5eval import load as eload, w5 as w5num, Tl
from r2_K3 import load, w5sym, letters, H, u, two

REPS = ['/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g/w5_exIII_allp.json',
        '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g/w5_I.json',
        '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g/w5_exIII_b.json',
        '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/w5_allp.json']

for FN in REPS:
    try: terms = load(FN)
    except Exception as e: print(FN,'SKIP',e); continue
    K3 = {}
    for cell in ('A','B'):
        v5 = sp.expand(w5sym(cell,terms) - (H[5]+two(5)))
        K3[cell] = sp.expand(sp.Poly(v5,u).coeff_monomial(u**3))
    tgt = sp.expand(4*K3['A'] + 24*K3['B'])
    print('%-22s K3(A)=%-14s K3(B)=%-14s  4K3(A)+24K3(B)=%s'
          %(FN.split('/')[-1], sp.simplify(K3['A']), sp.simplify(K3['B']), sp.simplify(tgt)))

print()
print('--- exact numeric cross-check (p*T*v5 mod p at the 3 corner cells) ---')
terms = eload(REPS[0])
for p in (7,11,13,17,19,23,29,31,37,41,43,47):
    n=(p+1)//2; q=p-n
    vals=[]
    for (k,l) in [(q,q+1),(q+1,q),(q+1,q+1)]:
        T=Tl(n,k,l); x=T*(w5num(n,k,l,terms)-Hs(n,5))
        px=F(p)*x            # in Z_p
        num,den=px.numerator,px.denominator
        vals.append(num*pow(den,p-2,p)%p)
    tot=sum(vals)%p
    pred=[6%p,6%p,(-12)%p]
    print('  p=%3d  residues=%-18s predicted (2*3,2*3,24*(-1/2))=%-18s sum=%d %s'
          %(p,vals,pred,tot,'OK' if vals==pred and tot==0 else '*** MISMATCH ***'))
