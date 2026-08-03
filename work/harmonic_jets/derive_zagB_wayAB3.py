import sympy as sp

A, B, D, E, c, m = sp.symbols('A B D E c m')
Tm, Tm1, Tm2, Tm3 = sp.symbols('T_m T_m1 T_m2 T_m3')
Vm, Vm1, Vm2 = sp.symbols('V_m V_m1 V_m2')
Wm, Wm1 = sp.symbols('W_m W_m1')
Ym = sp.symbols('Y_m')

r1 = Tm1 - (c*Tm + Vm)
r2 = Tm2 - (c*Tm1 + Vm1)
r3 = Tm3 - (c*Tm2 + Vm2)
r4 = Vm1 - (c*Vm + Wm)
r5 = Vm2 - (c*Vm1 + Wm1)
r6 = Wm1 - (c*Wm + Ym)

wayA = (m+2)*(m+1)*Ym + 3*(m+2)*Wm1 + Vm2
wayB = A*(m+2)*(m+1)*Wm + (A+B)*(m+2)*Vm1 + D*Tm2 - E*(m+2)*(m+1)*Vm - E*(m+2)*Tm1 + c**(m+2)

target = sp.expand(wayB - wayA)

deg = 2
rs = [r1, r2, r3, r4, r5, r6]
names = ['mu1','mu2','mu3','mu4','mu5','mu6']
syms = {}
combo = 0
for nm, r in zip(names, rs):
    poly = 0
    for d in range(deg+1):
        u = sp.Symbol(f'{nm}_{d}')
        syms[(nm,d)] = u
        poly += u*m**d
    combo += poly*r

diff = sp.expand(target - combo)
unknowns_syms = [Tm, Tm1, Tm2, Tm3, Vm, Vm1, Vm2, Wm, Wm1, Ym]
polydiff = sp.Poly(diff, *unknowns_syms)
eqs = [co for _, co in polydiff.terms()]
unknowns = list(syms.values())
sol = sp.linsolve(eqs, unknowns)
print('solved:', sol != sp.EmptySet)
if sol != sp.EmptySet:
    assign = dict(zip(unknowns, list(sol)[0]))
    for nm in names:
        val = sp.expand(sum(assign.get(syms[(nm,d)],0)*m**d for d in range(deg+1)))
        print(nm, '=', sp.factor(val))
