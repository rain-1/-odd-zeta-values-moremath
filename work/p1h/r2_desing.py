"""P1h: EXPLICIT desingularisation of L_BZ.

K := Q[nu]/(a_0)  is a field (a_0 irreducible).  In K, U=(c_0,c_1,c_2)(nu) and
V=(c_1,c_2,c_3)(nu-1) are proportional (all 2x2 minors vanish mod a_0), V != 0.
Let lambda = U_0/V_0 in K.  Then  Ltil := row(nu) - lambda*row(nu-1) , divided by a_0(nu),
is an order-4 operator on (Y_{nu-1},...,Y_{nu+3}) with leading coefficient EXACTLY
    2(nu+3)^5(2nu+5)     -- a_0 has disappeared.
"""
import sympy as sp
nu = sp.symbols('nu')
a0p = sp.Poly(41218*nu**3+198849*nu**2+320790*nu+173057, nu)
a0  = a0p.as_expr()
B8 = (3874492*nu**8+59373972*nu**7+394148190*nu**6+1481084196*nu**5+3447878810*nu**4
      +5095855458*nu**3+4673546679*nu**2+2433871008*nu+551502039)
B9 = (48802112*nu**9+967468896*nu**8+8488000862*nu**7+43246197636*nu**6+140983768422*nu**5
      +304912330849*nu**4+437406946975*nu**3+401272692378*nu**2+213593890911*nu+50257929339)
s=lambda f,x: sp.expand(f.subs(nu,x))
c=[lambda x:(x+1)**5*(x+2)*s(a0,x+1), lambda x:-2*(x+2)*s(B8,x), lambda x:-2*s(B9,x),
   lambda x:2*(x+3)**5*(2*x+5)*s(a0,x)]
C  = [sp.expand(f(nu))   for f in c]
Cm = [sp.expand(f(nu-1)) for f in c]
# lambda = C[0] / Cm[0]  in K
inv = sp.invert(sp.Poly(Cm[0],nu), a0p)                     # inverse of c_1(nu-1) in K
lam = sp.rem(sp.expand(sp.Poly(C[0],nu).as_expr()*inv.as_expr()), a0, nu)
lam = sp.expand(lam)
print('lambda in K (deg<=2):'); sp.pprint(sp.nsimplify(lam))
den = sp.lcm([sp.fraction(sp.together(t))[1] for t in sp.Add.make_args(lam)] or [1])
print('\ndenominator of lambda:', sp.factorint(int(den)))
# the order-4 row: coefficients of Y_{nu-1..nu+3}
row = [ -lam*Cm[0]+0, -lam*Cm[1]+C[0], -lam*Cm[2]+C[1], -lam*Cm[3]+C[2], C[3] ]
# careful: row(nu-1) acts on (Y_{nu-1},Y_nu,Y_{nu+1},Y_{nu+2}) ; row(nu) on (Y_nu..Y_{nu+3})
row = [ sp.expand(-lam*Cm[0]), sp.expand(-lam*Cm[1]+C[0]), sp.expand(-lam*Cm[2]+C[1]),
        sp.expand(-lam*Cm[3]+C[2]), sp.expand(C[3]) ]
print('\n--- divide each by a_0(nu) ---')
til=[]
for i,r in enumerate(row):
    q_, rem_ = sp.div(sp.Poly(r,nu), a0p)
    til.append(q_.as_expr())
    print('  d_%d : deg %-3s  remainder=%s' % (i, sp.Poly(r,nu).degree() if r!=0 else '-', sp.simplify(rem_.as_expr())))
print('\nLEADING COEFFICIENT d_4 =', sp.factor(til[4]))
print('  equals 2(nu+3)^5(2nu+5) ?', sp.simplify(til[4] - 2*(nu+3)**5*(2*nu+5))==0)
# clear denominators of the whole operator
D = sp.lcm([sp.fraction(sp.together(sp.expand(t)))[1] for t in til])
print('\ncommon denominator D of the order-4 operator:', sp.factorint(int(D)))
tilI = [sp.expand(D*t) for t in til]
cont = 0
for t in tilI:
    for co in sp.Poly(t,nu).all_coeffs(): cont = sp.gcd(cont, co)
print('integer content:', sp.factorint(int(cont)) if cont else 0)
tilI=[sp.expand(t/cont) for t in tilI]
print('\nnormalised leading coefficient d_4 =', sp.factor(tilI[4]))
print('BAD PRIMES of the desingularised operator (denominators of lambda):',
      sorted(sp.factorint(int(den)).keys()))
import json
json.dump({'lambda':sp.srepr(lam),'d':[sp.srepr(t) for t in tilI],'D':int(D),'cont':int(cont)},
          open('desing.json','w'))
