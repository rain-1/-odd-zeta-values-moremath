import sympy as sp

h, m = sp.symbols('h m')
c = -h
Tm, Tm1, Tm2, Tm3 = sp.symbols('T_m T_m1 T_m2 T_m3')
r1, r2, r3, r4, r5, r6 = sp.symbols('r1 r2 r3 r4 r5 r6')

Vm  = Tm1 - c*Tm - r1
Vm1 = Tm2 - c*Tm1 - r2
Vm2 = Tm3 - c*Tm2 - r3
Wm  = Vm1 - c*Vm - r4
Wm1 = Vm2 - c*Vm1 - r5
Ym  = Wm1 - c*Wm - r6

A, B, D, E = 3*h, 3*h, h, 3*h**2
wayA = (m+2)*(m+1)*Ym + 3*(m+2)*Wm1 + Vm2
wayB = A*(m+2)*(m+1)*Wm + (A+B)*(m+2)*Vm1 + D*Tm2 - E*(m+2)*(m+1)*Vm - E*(m+2)*Tm1 + c**(m+2)

target = sp.expand(wayA - wayB)
poly = sp.Poly(target, r1, r2, r3, r4, r5, r6)
# constant term (r_i = 0) is the clean T-identity
const_term = poly.as_expr()
for ri in [r1,r2,r3,r4,r5,r6]:
    const_term = const_term.subs(ri, 0)
print("Clean T-identity part (should match (m+3)^2 T_{m+3} + h^3(m+1)(m+2)T_m - (-h)^{m+2}):")
print(sp.simplify(const_term))
print()
print("Coefficients of r_i (these are the linear_combination multipliers, with sign: target = clean + sum coeff_i * r_i):")
for ri, name in zip([r1,r2,r3,r4,r5,r6], ['r1(Tsucc m)','r2(Tsucc m+1)','r3(Tsucc m+2)','r4(Vsucc m)','r5(Vsucc m+1)','r6(Wsucc m)']):
    coeff = sp.diff(target, ri)
    print(name, '=', sp.factor(coeff))
