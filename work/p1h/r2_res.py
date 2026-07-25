import sympy as sp
nu = sp.symbols('nu')
a0 = 41218*nu**3 + 198849*nu**2 + 320790*nu + 173057
B8 = (3874492*nu**8+59373972*nu**7+394148190*nu**6+1481084196*nu**5+3447878810*nu**4
      +5095855458*nu**3+4673546679*nu**2+2433871008*nu+551502039)
B9 = (48802112*nu**9+967468896*nu**8+8488000862*nu**7+43246197636*nu**6+140983768422*nu**5
      +304912330849*nu**4+437406946975*nu**3+401272692378*nu**2+213593890911*nu+50257929339)
sub=lambda f,x: sp.expand(f.subs(nu,x))
c1m=sp.expand(-2*(nu+1)*sub(B8,nu-1)); c2m=sp.expand(-2*sub(B9,nu-1))
c3m=sp.expand(2*(nu+2)**5*(2*nu+3)*sub(a0,nu-1))
print('irreducible a_0 ?', sp.factor_list(a0))
print('disc(a_0) =', sp.factorint(sp.discriminant(a0)))
print('lead(a_0) = 41218 =', sp.factorint(41218))
g=0
for nm,f in (('c1(nu-1)',c1m),('c2(nu-1)',c2m),('c3(nu-1)',c3m)):
    r=sp.resultant(a0,f,nu); g=sp.gcd(g,r)
    print('  Res(a_0, %s) has prime factors'%nm, sorted(sp.factorint(int(r)).keys())[:14],'...' )
print('GCD of the three resultants =', sp.factorint(int(g)))
print('  -> V(nu) can vanish mod p at a root of a_0 only for p in', sorted(sp.factorint(int(g)).keys()))
# special values
print()
print('a_0(-5/2) =', sp.Rational(sp.nsimplify(a0.subs(nu,sp.Rational(-5,2)))), '=', sp.factorint(30143))
print('a_0(-3/2) =', a0.subs(nu,sp.Rational(-3,2)), ' (=343/2, so 2nu+3 & a_0 clash only at p=7)')
print('a_0(0)    =', a0.subs(nu,0), '=', sp.factorint(173057))
