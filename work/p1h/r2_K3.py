"""P1h R2 (decisive): closed-form K_3 at the two corner cells of the critical level.

p >= 7 prime, q=(p-1)/2, n=q+1=(p+1)/2.  Region III at level n = {(q,q+1),(q+1,q),(q+1,q+1)}.
T/p^2 == (2,2,24) mod p (proved separately).  So (BASE) at n=(p+1)/2 reads

     4*K_3(A) + 24*K_3(B) == 0  (mod p),      A=(k,l)=(q,q+1) , B=(q+1,q+1).

Letter expansions mod p (u = 1/p ; h_r := H^(r)_q mod p ; (q+1)^-1==2, (q+2)^-1==2/3 ;
Sum_{j<p} j^-r == 0 for 1<=r<=5, p>=7):

  cell A (k=q, l=q+1):  A_r(k)=u^r - h_r          B_r(k)=1-h_r
                        A_r(l)=u^r + 1-h_r-2^r    B_r(l)=-h_r-2^r
                        C_r = h_r+2^r             N_r = h_r+2^r
  cell B (k=l=q+1):     A_r   =u^r + 1-h_r-2^r    B_r  =-h_r-2^r
                        C_r = h_r+2^r+(2/3)^r-1   N_r = h_r+2^r
"""
import sys, json
import sympy as sp

u  = sp.symbols('u')
h  = sp.symbols('h1 h2 h3 h4 h5')
H  = {r: h[r-1] for r in range(1,6)}

def two(r):   return sp.Rational(2)**r
def tt(r):    return sp.Rational(2,3)**r

def letters(cell):
    """return dict slot->(letter fn)  slot in {'k','l','c','n'}"""
    if cell == 'A':
        Ak = lambda r: u**r - H[r]
        Bk = lambda r: 1 - H[r]
        Al = lambda r: u**r + 1 - H[r] - two(r)
        Bl = lambda r: -H[r] - two(r)
        C  = lambda r: H[r] + two(r)
        N  = lambda r: H[r] + two(r)
    else:
        Ak = Al = lambda r: u**r + 1 - H[r] - two(r)
        Bk = Bl = lambda r: -H[r] - two(r)
        C  = lambda r: H[r] + two(r) + tt(r) - 1
        N  = lambda r: H[r] + two(r)
    return dict(Ak=Ak,Bk=Bk,Al=Al,Bl=Bl,C=C,N=N)

def evalmono(names, slot, L):
    v = sp.Integer(1)
    for nm in names:
        t, r = nm[0], int(nm[1])
        if t == 'A': v *= L['A'+slot](r)
        elif t == 'B': v *= L['B'+slot](r)
        elif t == 'C': v *= L['C'](r)
        elif t == 'N': v *= L['N'](r)
        else: raise ValueError(nm)
    return v

def load(fn):
    d = json.load(open(fn)); out=[]
    for lab,(num,den) in d.items():
        fg, rest = lab.split(']x'); f,g = fg[1:].split('|'); hh,s = rest.split('x')
        sp_ = lambda x: [] if x=='1' else x.split('*')
        out.append((sp.Rational(num,den), sp_(f), sp_(g), sp_(hh), sp_(s)))
    return out

def w5sym(cell, terms):
    L = letters(cell); tot = sp.Integer(0)
    for cf,f,g,hh,s in terms:
        v = cf*evalmono(hh,'',L)*evalmono(s,'',L)
        if v == 0: continue
        pf = evalmono(f,'k',L)*evalmono(g,'l',L)
        if f == g: tot += v*pf
        else:      tot += v*(pf + evalmono(g,'k',L)*evalmono(f,'l',L))
    return sp.expand(tot)

FN = sys.argv[1] if len(sys.argv)>1 else '/home/ubuntu/fable-episode-2/zeta-math-2/work/p1g/w5_exIII_allp.json'
terms = load(FN)
alph = set()
for _,f,g,hh,s in terms: alph |= set(f)|set(g)|set(hh)|set(s)
print('rep:',FN.split('/')[-1],' #terms',len(terms),' alphabet:',sorted(alph))

res = {}
for cell in ('A','B'):
    w = w5sym(cell, terms)
    # subtract H^(5)_n = H^(5)_{q+1} = h5 + 2^5   (no pole)
    v5 = sp.expand(w - (H[5] + two(5)))
    P = sp.Poly(v5, u)
    Ks = {j: sp.expand(P.coeff_monomial(u**j)) for j in range(0,6)}
    res[cell] = Ks
    print('\n--- cell %s ---'%cell)
    for j in range(5,-1,-1):
        e = sp.simplify(Ks[j].subs({H[2]:0,H[4]:0}))
        print('  K_%d = %s'%(j, sp.factor(sp.expand(e))))

tgt = sp.expand(4*res['A'][3] + 24*res['B'][3])
print('\n=== TARGET  4*K_3(A) + 24*K_3(B) ===')
print('  raw :', sp.factor(sp.expand(tgt)))
print('  with h2=h4=0 :', sp.factor(sp.expand(tgt.subs({H[2]:0,H[4]:0}))))
