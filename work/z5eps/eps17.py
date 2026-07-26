"""eps17.py -- hardening:
 (A) null-invariance of e5tot and e4tot at the special point (zeta-forcing)
 (B) family 2 (-2,-1,0,1;t=2) at both primes: data + row coeffs
 (C) extended-range verification of family 1 (t=1): [eps^m] identities mod p, n <= 80
 (D) per-letter e_m table (printed for the doc)
"""
import sys
from math import comb
from fractions import Fraction as F
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5')
sys.path.insert(0, '/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import core
from eps2 import rref_solve, rr
from eps6 import Pipe

# ---------- (A) null-invariance ----------
p = 2147483647
pi = Pipe(p); nr = pi.nr
a,b,c,d = -1,0,1,2
alpha = ((-c-d)%p, c%p, d%p); a1c=[0,0]+list(alpha); s1c=[a%p,b%p,0,0,0]
x2 = pi.E2(s1c,a1c,verbose=False); g9=list(x2[:6])+[0,0,0]
x3, null3 = pi.E3(s1c,a1c,g9,verbose=False); ker=null3[0]
tval=1
y9=[(x3[i]+tval*ker[i])%p for i in range(6)]+[0,0,0]
b9=[0]*6+[(x3[6+i]+tval*ker[6+i])%p for i in range(3)]
i2,i6,i120 = pi.inv(2),pi.inv(6),pi.inv(120)
cols = pi.stage_cols2(5,4,alpha)
for j in range(3):
    e9=[0]*9; e9[6+j]=1
    c1=pi.momHH([],b9,2,e9,3); c2=pi.momH([s1c,a1c],3,e9)
    cols.append([(c1[n]+c2[n])%p for n in range(nr)])
for cix in range(6):
    e9=[0]*9; e9[cix]=1
    cols.append(pi.momH([s1c],4,e9))
cols += pi.rowcols()
A5=[[cc[n] for cc in cols] for n in range(nr)]
ok,x,null,rk = rref_solve(A5,[0]*nr,p)
mult=[1,2,2,2,1,1]
print('(A) E5 null space dim %d; per null vector: Sum mult*w, Sum mult*z:' % len(null))
for v in null:
    sw = sum(mult[cc]*v[cc] for cc in range(6)) % p
    sz = sum(mult[cc]*v[12+cc] for cc in range(6)) % p
    print('    Sum mult*w =', rr(sw,p), '  Sum mult*z =', rr(sz,p))

# ---------- (B) family 2 at both primes ----------
for pp in (2147483647, 2147483629):
    pj = Pipe(pp)
    from eps13 import E5ext as _E5   # E5ext bound to module-level pi (p1) -- rebuild inline instead
for pp in (2147483647, 2147483629):
    pj = Pipe(pp); nrj = pj.nr
    aa,bb_,cc_,dd = -2,-1,0,1
    al = ((-cc_-dd)%pp, cc_%pp, dd%pp); a1=[0,0]+list(al); s1=[aa%pp,bb_%pp,0,0,0]
    x2j = pj.E2(s1,a1,verbose=False); g9j=list(x2j[:6])+[0,0,0]
    x3j, n3j = pj.E3(s1,a1,g9j,verbose=False); kerj=n3j[0]
    t2=2
    print('(B) family2 p=%d: g=%s' % (pp,[rr(v,pp) for v in x2j[:6]]))
    print('    y(t=2)=%s beta=%s t3=%s' %
          ([rr((x3j[i]+t2*kerj[i])%pp,pp) for i in range(6)],
           [rr((x3j[6+i]+t2*kerj[6+i])%pp,pp) for i in range(3)],
           rr((x3j[9]+t2*kerj[9])%pp,pp)))

# ---------- (C) extended-range mod-p verification of family 1, t=1 ----------
NBIG = 80
DATA = dict(
  ALPHA=(F(-3),F(1),F(2)), AB=(F(-1),F(0)),
  G=[F(-4),F(1),F(-3),F(4),F(2),F(-2)], BETA=[F(-9),F(-5,4),F(-4)],
  Y=[F(0),F(12),F(-5,6),F(-32,3),F(8,3),F(-8,3)], GAM=[F(-12),F(5,6),F(32,3)],
  Z=[F(0),F(0),F(0),F(0),F(4),F(-4)], DLT=[F(-68),F(31,32),F(-64)],
  W=[F(0),F(528,5),F(37,40),F(-512,5),F(32,5),F(-32,5)])
D1VEC=[0,-3,1,2,-2,2]
for pp in (2147483647, 2147483629):
    fm = lambda fr: fr.numerator % pp * pow(fr.denominator % pp, pp-2, pp) % pp
    dv = {k:( [fm(x) for x in v] if isinstance(v,list) else tuple(fm(x) for x in v))
          for k,v in DATA.items()}
    HM=3*NBIG+2
    Ht=[[0]*(HM+1) for _ in range(6)]
    for m in range(1,HM+1):
        im=pow(m,pp-2,pp); acc=im
        Ht[1][m]=(Ht[1][m-1]+acc)%pp
        for r in range(2,6):
            acc=acc*im%pp; Ht[r][m]=(Ht[r][m-1]+acc)%pp
    lad=core.ladders()
    inv2,inv6,inv24,inv120 = (pow(x,pp-2,pp) for x in (2,6,24,120))
    badcnt = {1:0,2:0,3:0,5:0}
    for n in range(NBIG+1):
        acc=[0]*5
        for k in range(n+1):
            ck = comb(n+k,n)*comb(n,k)**2
            for l in range(n+1):
                t = (ck*comb(n+l,n)*comb(n,l)**2*comb(n+k+l,n)) % pp
                s=[[0]*6 for _ in range(6)]; an=[[0]*3 for _ in range(6)]
                for r in range(1,6):
                    s[r]=[Ht[r][n],(Ht[r][k]+Ht[r][l])%pp,(Ht[r][n+k]+Ht[r][n+l])%pp,
                          (Ht[r][n-k]+Ht[r][n-l])%pp,Ht[r][k+l],Ht[r][n+k+l]]
                    an[r]=[(Ht[r][k]-Ht[r][l])%pp,(Ht[r][n+k]-Ht[r][n+l])%pp,
                           (Ht[r][n-k]-Ht[r][n-l])%pp]
                X = sum(D1VEC[cc2]*s[1][cc2] for cc2 in range(6)) % pp
                L1 = (dv['AB'][0]*X + sum(dv['ALPHA'][j]*an[1][j] for j in range(3))) % pp
                L2 = (sum(dv['G'][cc2]*s[2][cc2] for cc2 in range(6))
                      + sum(dv['BETA'][j]*an[2][j] for j in range(3))) % pp
                L3 = (sum(dv['Y'][cc2]*s[3][cc2] for cc2 in range(6))
                      + sum(dv['GAM'][j]*an[3][j] for j in range(3))) % pp
                L4 = (sum(dv['Z'][cc2]*s[4][cc2] for cc2 in range(6))
                      + sum(dv['DLT'][j]*an[4][j] for j in range(3))) % pp
                L5 = sum(dv['W'][cc2]*s[5][cc2] for cc2 in range(6)) % pp
                B1=L1
                B2=(L2+inv2*L1*L1)%pp
                B3=(L3+L1*L2+inv6*pow(L1,3,pp))%pp
                B4=(L4+L1*L3+inv2*L2*L2+inv2*L1*L1%pp*L2+inv24*pow(L1,4,pp))%pp
                B5=(L5+L1*L4+L2*L3+inv2*L1*L1%pp*L3+inv2*L1*L2%pp*L2
                    +inv6*pow(L1,3,pp)*L2+inv120*pow(L1,5,pp))%pp
                for m_,Bv in ((0,B1),(1,B2),(2,B3),(3,B4),(4,B5)):
                    acc[m_]=(acc[m_]+t*Bv)%pp
        if acc[0]%pp: badcnt[1]+=1
        if acc[1]%pp: badcnt[2]+=1
        if (acc[2]-fm(lad['Ph'][n]))%pp: badcnt[3]+=1
        t5=fm(F(33,4))
        if (acc[4]-t5*fm(lad['P'][n]))%pp: badcnt[5]+=1
    print('(C) p=%d n<=%d: failures  [e1]=%d [e2]=%d [e3-Phat]=%d [e5-(33/4)P]=%d'
          % (pp, NBIG, badcnt[1],badcnt[2],badcnt[3],badcnt[5]))

# ---------- (D) per-letter table ----------
G,BETA,Y,GAM,Z,DLT,W = (DATA[k] for k in ('G','BETA','Y','GAM','Z','DLT','W'))
def row(name, sym_i, anti_j, sgn):
    c1 = {'n':F(0),'k':F(0),'l':F(6),'n+k':F(0),'n+l':F(-2),'n-k':F(0),'n-l':F(-4),
          'k+l':F(2),'n+k+l':F(-2)}[name]
    c2 = G[sym_i] + (sgn*BETA[anti_j] if anti_j is not None else 0)
    c3 = Y[sym_i] + (sgn*GAM[anti_j] if anti_j is not None else 0)
    c4 = Z[sym_i] + (sgn*DLT[anti_j] if anti_j is not None else 0)
    c5 = W[sym_i]
    return c1, -2*c2, 3*c3, -4*c4, 5*c5
print()
print('(D) per-letter exponent power sums e_m(L), t=1 :  L | e1 e2 e3 e4 e5')
for name, si, aj, sg in (('n',0,None,0),('k',1,0,1),('l',1,0,-1),('n+k',2,1,1),
                         ('n+l',2,1,-1),('n-k',3,2,1),('n-l',3,2,-1),
                         ('k+l',4,None,0),('n+k+l',5,None,0)):
    e = row(name,si,aj,sg)
    print('   %7s : %s' % (name, '  '.join(str(v) for v in e)))
