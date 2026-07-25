"""For each candidate prime, does a_0 actually have a root nu in [1,p-4] with V(nu)==0 mod p?"""
def a0(n): return 41218*n**3+198849*n**2+320790*n+173057
def B8(n): return (3874492*n**8+59373972*n**7+394148190*n**6+1481084196*n**5+3447878810*n**4
                   +5095855458*n**3+4673546679*n**2+2433871008*n+551502039)
def B9(n): return (48802112*n**9+967468896*n**8+8488000862*n**7+43246197636*n**6+140983768422*n**5
                   +304912330849*n**4+437406946975*n**3+401272692378*n**2+213593890911*n+50257929339)
def c1(n): return -2*(n+2)*B8(n)
def c2(n): return -2*B9(n)
def c3(n): return 2*(n+3)**5*(2*n+5)*a0(n)
for p in (7,11,29,37,557,543606522303979):
    roots=[]
    if p<10**6:
        roots=[v for v in range(p) if a0(v)%p==0]
    else:
        # Cantor-Zassenhaus-free: use sympy ground roots
        import sympy as sp
        x=sp.symbols('x')
        roots=[int(r) for r in sp.polys.polytools.Poly(a0(x),x,modulus=p).ground_roots()]
        roots=[r%p for r in roots]
    hits=[]
    for v in roots:
        if not (1<=v<=p-4): continue
        V=(c1(v-1)%p, c2(v-1)%p, c3(v-1)%p)
        hits.append((v,V,'V==0' if V==(0,0,0) else 'V!=0'))
    print('p=%-18d roots of a_0 in [1,p-4]: %s'%(p,hits if hits else 'NONE in range'))
