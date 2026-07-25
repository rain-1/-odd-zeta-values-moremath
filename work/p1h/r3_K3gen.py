"""K_3 with the Fermat sums s_r := Sum_{j=1}^{p-1} j^-r kept as FREE symbols.
If K_3 is free of s_4,s_5 then Lemma 2.4 needs only s_1=s_2=s_3=0, i.e. p>=5 (not p>=7)."""
import sys, json, sympy as sp
u = sp.symbols('u')
h = sp.symbols('h1 h2 h3 h4 h5'); H={r:h[r-1] for r in range(1,6)}
S = sp.symbols('s1 s2 s3 s4 s5');  Sy={r:S[r-1] for r in range(1,6)}
two=lambda r: sp.Rational(2)**r
tt  =lambda r: sp.Rational(2,3)**r
def letters(cell):
    if cell=='A':
        return dict(Ak=lambda r:u**r+Sy[r]-H[r], Bk=lambda r:1-H[r],
                    Al=lambda r:u**r+Sy[r]+1-H[r]-two(r), Bl=lambda r:-H[r]-two(r),
                    C =lambda r:H[r]+two(r),       N=lambda r:H[r]+two(r))
    f=lambda r:u**r+Sy[r]+1-H[r]-two(r); g=lambda r:-H[r]-two(r)
    return dict(Ak=f,Al=f,Bk=g,Bl=g, C=lambda r:H[r]+two(r)+tt(r)-1, N=lambda r:H[r]+two(r))
def ev(names,slot,L):
    v=sp.Integer(1)
    for nm in names:
        t,r=nm[0],int(nm[1])
        v*= L['A'+slot](r) if t=='A' else L['B'+slot](r) if t=='B' else L['C'](r) if t=='C' else L['N'](r)
    return v
def load(fn):
    d=json.load(open(fn)); out=[]
    for lab,(nu_,de) in d.items():
        fg,rest=lab.split(']x'); f,g=fg[1:].split('|'); hh,s=rest.split('x')
        q=lambda x: [] if x=='1' else x.split('*')
        out.append((sp.Rational(nu_,de),q(f),q(g),q(hh),q(s)))
    return out
terms=load('/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g/w5_exIII_allp.json')
K3={}
for cell in ('A','B'):
    L=letters(cell); tot=sp.Integer(0)
    for cf,f,g,hh,s in terms:
        v=cf*ev(hh,'',L)*ev(s,'',L)
        if v==0: continue
        pf=ev(f,'k',L)*ev(g,'l',L)
        tot += v*pf if f==g else v*(pf+ev(g,'k',L)*ev(f,'l',L))
    v5=sp.expand(sp.expand(tot)-(H[5]+two(5)))
    K3[cell]=sp.expand(sp.Poly(v5,u).coeff_monomial(u**3))
    fv=K3[cell].free_symbols
    print('cell %s : K_3 free symbols = %s'%(cell, sorted(map(str,fv)) or 'NONE (constant)'))
    print('          K_3 = %s'%sp.simplify(K3[cell]))
    print('          with s1=s2=s3=0 : %s'%sp.simplify(K3[cell].subs({Sy[1]:0,Sy[2]:0,Sy[3]:0})))
tg=sp.expand(4*K3['A']+24*K3['B'])
print('\n4*K_3(A)+24*K_3(B) (all s_r free)     =', sp.simplify(tg))
print('4*K_3(A)+24*K_3(B) with s1=s2=s3=0    =', sp.simplify(tg.subs({Sy[1]:0,Sy[2]:0,Sy[3]:0})))
