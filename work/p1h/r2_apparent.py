"""P1h: the a_0-root steps are apparent -- as a POLYNOMIAL IDENTITY.

At a step nu with a_0(nu) == 0 (mod p):
   row(nu-1):  c_0(nu-1)Y_{nu-1}+c_1(nu-1)Y_nu+c_2(nu-1)Y_{nu+1}+c_3(nu-1)Y_{nu+2}=0
   and c_0(nu-1) = nu^5(nu+1)a_0(nu) == 0 (mod p), so if Y_{nu-1} in Z_p,
       c_1(nu-1)Y_nu + c_2(nu-1)Y_{nu+1} + c_3(nu-1)Y_{nu+2} == 0 (mod p).      (*)
   the obligation at nu is
       c_0(nu)Y_nu + c_1(nu)Y_{nu+1} + c_2(nu)Y_{nu+2} == 0 (mod p).            (**)
(**) follows from (*) for EVERY p-integral solution iff
       (c_0,c_1,c_2)(nu)  is proportional to  (c_1,c_2,c_3)(nu-1)   mod a_0(nu).
Test: does a_0(nu) divide all three 2x2 minors, as polynomials in Q[nu]?
"""
import sympy as sp
nu = sp.symbols('nu')
a0 = 41218*nu**3 + 198849*nu**2 + 320790*nu + 173057
def A0(x): return a0.subs(nu,x)
B8 = (3874492*nu**8+59373972*nu**7+394148190*nu**6+1481084196*nu**5+3447878810*nu**4
      +5095855458*nu**3+4673546679*nu**2+2433871008*nu+551502039)
B9 = (48802112*nu**9+967468896*nu**8+8488000862*nu**7+43246197636*nu**6+140983768422*nu**5
      +304912330849*nu**4+437406946975*nu**3+401272692378*nu**2+213593890911*nu+50257929339)
def c0(x): return sp.expand(((x+1)**5*(x+2)*A0(x+1)))
def c1(x): return sp.expand(-2*(x+2)*B8.subs(nu,x))
def c2(x): return sp.expand(-2*B9.subs(nu,x))
def c3(x): return sp.expand(2*(x+3)**5*(2*x+5)*A0(x))

U = [c0(nu), c1(nu), c2(nu)]
V = [c1(nu-1), c2(nu-1), c3(nu-1)]
print('a_0(nu) =', sp.factor(a0))
print('check c_0(nu-1) = nu^5(nu+1)a_0(nu):', sp.simplify(c0(nu-1) - nu**5*(nu+1)*a0) == 0)
ok = True
for (i,j) in ((0,1),(0,2),(1,2)):
    m = sp.expand(U[i]*V[j] - U[j]*V[i])
    quo, rem = sp.div(sp.Poly(m,nu), sp.Poly(a0,nu))
    print('  minor(%d,%d): deg %2d ; remainder mod a_0 = %s'
          %(i,j,sp.Poly(m,nu).degree(), sp.factor(rem.as_expr())))
    if rem.as_expr()!=0: ok=False
print('ALL MINORS DIVISIBLE BY a_0 :', ok)
if ok:
    # the proportionality factor
    lam = sp.cancel(U[0]/V[0])
    print('proportionality factor (c_0(nu)/c_1(nu-1)) mod a_0:')
    q,r = sp.div(sp.Poly(sp.expand(U[0]),nu), sp.Poly(a0,nu)); print('   c_0(nu) mod a_0 :', sp.factor(r.as_expr()))
    q,r = sp.div(sp.Poly(sp.expand(V[0]),nu), sp.Poly(a0,nu)); print('   c_1(nu-1) mod a_0:', sp.factor(r.as_expr()))
