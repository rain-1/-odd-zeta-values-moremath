"""verify.py -- all numerical checks asserted in main.tex. Exact (Fraction)."""
import sys
from fractions import Fraction as F
from math import comb
sys.path.insert(0,'/home/ubuntu/fable-episode-2/zeta-math-2/work/z5eps')
import sympy as sp
import eps48_modular_nome as M
from eps48_modular_nome import smul,sinv,sexp,srevert,compose,eta_quot,N

th=sp.symbols('th')
a,b,c,d=17,5,1,0

# --- 1. a_n two ways -------------------------------------------------------
def a_sum(n): return sum(comb(n,k)**2*comb(n+k,k)**2 for k in range(n+1))
A=[F(1)]
for n in range(0,30):
    if n==0: A.append(F(5))
    else: A.append((F((2*n+1)*(17*n*n+17*n+5))*A[n]-F(n**3)*A[n-1])/F((n+1)**3))
print('CHECK1 a_n sum==recurrence n<=25:', all(A[n]==a_sum(n) for n in range(26)))
print('  a_0..a_6 =',[int(A[n]) for n in range(7)])

# --- 2. b_n classical closed form vs recurrence ----------------------------
def b_cl(n):
    H=sum(F(1,m**3) for m in range(1,n+1))
    tot=F(0)
    for k in range(n+1):
        inner=sum(F((-1)**(m-1),2*m**3*comb(n,m)*comb(n+m,m)) for m in range(1,k+1))
        tot+=comb(n,k)**2*comb(n+k,k)**2*(H+inner)
    return tot
B6=[b_cl(n) for n in range(26)]
rec_ok=all(F((n+1)**3)*B6[n+1]==F((2*n+1)*(17*n*n+17*n+5))*B6[n]-F(n**3)*B6[n-1] for n in range(1,25))
print('CHECK2 b_n closed form satisfies recurrence 1<=n<=24:', rec_ok, '| b_0,b_1=',B6[0],B6[1])
n0=F(1**3)*B6[1]-F(5)*B6[0]
print('  n=0 instance defect: 1^3 b_1 - 5 b_0 =',n0,'(=6, so L(y_b)=6t)')
print('  b_0..b_6 =',[str(x) for x in B6[:7]])
import mpmath as mp
mp.mp.dps=40
print('CHECK3 b_25/a_25 vs zeta(3):', mp.mpf(B6[25].numerator)/mp.mpf(B6[25].denominator)/mp.mpf(A[25].numerator), 'vs', mp.zeta(3))

# --- 3. Frobenius / nome / eta ---------------------------------------------
Aser=A[:N+3]
Pj=[th**3,-sp.expand((2*th+1)*(a*th**2+a*th+b)),sp.expand((th+1)*(c*(th+1)**2+d))]
y0=Aser[:N+1]
g=M.gseries(Pj,y0)
print('  g(t) coeffs t^1..t^5:',[str(x) for x in g[1:6]])
ratio=smul(g,sinv(y0))
qser=smul([F(0),F(1)]+[F(0)]*(N-1),sexp(ratio))
tq=srevert(qser); Fq=compose(y0,tq)
print('  q(t) to t^6:',[str(x) for x in qser[:7]])
print('  t(q) to q^7:',[str(x) for x in tq[:8]])
print('  F(q) to q^7:',[str(x) for x in Fq[:8]])
t_known=smul([F(0),F(1)]+[F(0)]*(N-1),eta_quot({1:12,6:12,2:-12,3:-12}))
F_known=eta_quot({2:7,3:7,1:-5,6:-5})
print('CHECK4 t(q)==q(eta1 eta6/eta2 eta3)^12 to q^%d:'%N, tq==t_known)
print('CHECK5 F(q)==(eta2 eta3)^7/(eta1 eta6)^5 to q^%d:'%N, Fq==F_known)

# --- 4. companion formula ---------------------------------------------------
T=[tq[i+1] for i in range(N)]+[F(0)]
thT=[F(i)*T[i] for i in range(len(T))]
corr=smul(thT,sinv(T))
sigma=list(corr); sigma[0]=F(1)+corr[0]
t2=smul(tq,tq)
P3=[F(-2*a)*tq[i]+F(c)*t2[i] for i in range(N+1)]; P3[0]=F(1)
print('  sigma to q^5:',[str(x) for x in sigma[:6]])
sig3=smul(sigma,smul(sigma,sigma))
Psi=smul(smul(tq,sig3),smul(sinv(P3),sinv(Fq)))
print('  Psi to q^8:',[str(x) for x in Psi[:9]])
Theta=[F(0)]+[Psi[m]/F(m)**3 for m in range(1,N+1)]
yq=smul(Fq,Theta)
bt=compose(yq,qser)
B1=[F(0),F(1)]
for n in range(1,N+1):
    B1.append((F((2*n+1)*(a*n*n+a*n+b))*B1[n]-F(n*(c*n*n+d))*B1[n-1])/F((n+1)**3))
print('CHECK6 companion formula == B(n) (B0=0,B1=1) n<=%d:'%N, all(bt[n]==B1[n] for n in range(N+1)))
print('CHECK7 b_n == 6 B(n) n<=25:', all(B6[n]==6*B1[n] for n in range(26)))
print('  B(n) n<=6:',[str(x) for x in B1[:7]])
print('  [t^n]F.Theta n<=6:',[str(x) for x in bt[:7]])

# --- 5. extras for the tables ----------------------------------------------
print('  b_n/a_n n=1..8:',[mp.nstr(mp.mpf(B6[n].numerator)/mp.mpf(B6[n].denominator)/mp.mpf(A[n].numerator),12) for n in range(1,9)])
print('  Theta to q^6:',[str(x) for x in Theta[:7]])
print('  P3 = 1-34t+t^2; leading theta^3 coeff check:', sp.expand((th**3).coeff(th,3)))
# direct: L applied to y_B series in t
def Lapply(y):
    out=[F(0)]*(N+1)
    for n in range(N+1):
        v=F(n**3)*y[n]
        if n>=1: v-=F((2*(n-1)+1)*(a*(n-1)**2+a*(n-1)+b))*y[n-1]
        if n>=2: v+=F((n-1)*(c*(n-1)**2+d))*y[n-2]
        out[n]=v
    return out
Ly=Lapply(bt)
print('CHECK8 L(y_B) == t exactly (all other coeffs 0, to t^%d):'%N,
      Ly[1]==1 and all(Ly[n]==0 for n in range(N+1) if n!=1))
print('CHECK9 L(y_0) == 0 to t^%d:'%N, all(x==0 for x in Lapply(y0)))

# --- 6. sigma as an Eisenstein combination (valid to q^25; q^26 is the
#        truncation edge of the sigma construction) ---------------------------
def E2(m,n=N):
    o=[F(0)]*(n+1); o[0]=F(1)
    for k in range(1,n//m+1):
        o[m*k]=F(-24*sum(dd for dd in range(1,k+1) if k%dd==0))
    return o
sig=[(E2(1)[i]+6*E2(6)[i]-2*E2(2)[i]-3*E2(3)[i])/2 for i in range(N+1)]
print('CHECK11 sigma == (E2(q)+6E2(q^6)-2E2(q^2)-3E2(q^3))/2 to q^25:',
      sig[:N]==sigma[:N])

# --- 7. CHECK12: L = Sym^2(D), exactly ------------------------------------
# (a) symbolic residual over Q(t)
tt=sp.symbols('t'); yy=sp.Function('y')
def thr(e,k=1):
    for _ in range(k): e=sp.expand(tt*sp.diff(e,tt))
    return e
Y=yy(tt)
def _P1(e): 
    e2=a*thr(e,2)+a*thr(e,1)+b*e; return 2*thr(e2,1)+e2
def _P2(e):
    e1=thr(e,1)+e; return c*(thr(e1,2)+2*thr(e1,1)+e1)+d*e1
Lx=sp.expand(thr(Y,3)-tt*_P1(Y)+tt**2*_P2(Y))
cs=[sp.simplify(Lx.coeff(sp.diff(Y,tt,k))) for k in range(1,4)]
c0=sp.simplify(Lx-sum(cs[k-1]*sp.diff(Y,tt,k) for k in range(1,4))).coeff(Y)
C=[c0]+cs
Am=[sp.cancel(C[k]/C[3]) for k in range(3)]
pp=sp.cancel(Am[2]/3); qq=sp.cancel((Am[1]-2*pp**2-sp.diff(pp,tt))/4)
resid=sp.simplify(sp.cancel(Am[0]-(4*pp*qq+2*sp.diff(qq,tt))))
print('CHECK12a L = Sym^2(D) residual over Q(t):', resid, '(0 == exact identity)')
print('  D = d^2 + p d + q,  p =',sp.factor(pp),' q =',sp.factor(qq))

# (b) D in theta form: theta^2 - t(34 th^2+17 th+5/2) + t^2 (th+1/2)^2;
#     u = holomorphic solution, v = u log t + w.  Check u^2 = y0, u w = g.
Q=[th**2, -sp.expand(34*th**2+17*th+sp.Rational(5,2)),
   sp.expand((th+sp.Rational(1,2))**2)]
Qp=[sp.Poly(sp.diff(x,th),th) for x in Q]; Qo=[sp.Poly(x,th) for x in Q]
def evp(P,m): return F(sp.Rational(P.eval(sp.Rational(m))))
u=[F(0)]*(N+1); u[0]=F(1)
for n in range(1,N+1):
    u[n]=-sum(evp(Qo[j],n-j)*u[n-j] for j in (1,2) if n-j>=0)/F(n*n)
R=[F(0)]*(N+1)
for j in range(3):
    for m in range(N+1-j): R[m+j]-=evp(Qp[j],m)*u[m]
w=[F(0)]*(N+1)
for n in range(1,N+1):
    w[n]=(R[n]-sum(evp(Qo[j],n-j)*w[n-j] for j in (1,2) if n-j>=0))/F(n*n)
print('CHECK12b u^2 == y_0 to t^%d:'%N, smul(u,u)[:N+1]==y0[:N+1])
print('CHECK12c u*w == g to t^%d:'%N, smul(u,w)[:N+1]==g[:N+1])
print('  u = ', [str(x) for x in u[:5]])
