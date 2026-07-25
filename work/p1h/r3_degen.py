"""Uniform treatment of the fully-degenerate a_0 steps (row(nu-1) == 0 mod p).
The three cases in existence (r2_res2.py): (7,2), (11,6), (543606522303979, 416574044722681)."""
def a0(n): return 41218*n**3+198849*n**2+320790*n+173057
def B8(n): return (3874492*n**8+59373972*n**7+394148190*n**6+1481084196*n**5+3447878810*n**4
                   +5095855458*n**3+4673546679*n**2+2433871008*n+551502039)
def B9(n): return (48802112*n**9+967468896*n**8+8488000862*n**7+43246197636*n**6+140983768422*n**5
                   +304912330849*n**4+437406946975*n**3+401272692378*n**2+213593890911*n+50257929339)
c=[lambda n:(n+1)**5*(n+2)*a0(n+1), lambda n:-2*(n+2)*B8(n), lambda n:-2*B9(n),
   lambda n:2*(n+3)**5*(2*n+5)*a0(n)]
def v(x,p):
    if x==0: return 99
    k=0
    while x%p==0: x//=p; k+=1
    return k
def rank(M,p,ncol=5):
    M=[r[:] for r in M]; r=0
    for ci in range(ncol):
        piv=next((i for i in range(r,len(M)) if M[i][ci]%p),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]; iv=pow(M[r][ci],p-2,p); M[r]=[x*iv%p for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][ci]%p:
                f=M[i][ci]; M[i]=[(a-f*b)%p for a,b in zip(M[i],M[r])]
        r+=1
    return r
for (p,nu) in ((7,2),(11,6),(543606522303979,416574044722681)):
    rm1=[f(nu-1) for f in c]; rm2=[f(nu-2) for f in c] if nu>=2 else None
    print('p=%-18d nu=%-18d  (p-3)/2=%d  needed-range: %s'
          %(p,nu,(p-3)//2, (p-3)//2<=nu<=p-4))
    print('   v_p(row(nu-1)) =',[v(x,p) for x in rm1],
          ' v_p(c_3(nu)) =',v(c[3](nu),p))
    if rm2 is None: print('   nu<2, no row(nu-2)'); continue
    M=[[rm2[0]%p,rm2[1]%p,rm2[2]%p,rm2[3]%p,0],
       [0,(rm1[0]//p)%p,(rm1[1]//p)%p,(rm1[2]//p)%p,(rm1[3]//p)%p],
       [0,0,c[0](nu)%p,c[1](nu)%p,c[2](nu)%p]]
    r2_,r3_=rank(M[:2],p),rank(M,p)
    print('   c_3(nu-2) unit? %s ; c_3(nu-1)/p unit? %s'
          %(rm2[3]%p!=0, (rm1[3]//p)%p!=0))
    print('   rank[row(nu-2);row(nu-1)/p] = %d ; with U appended = %d  -> %s'
          %(r2_,r3_,'APPARENT (U in span)' if r2_==r3_ else 'NOT in span'))
