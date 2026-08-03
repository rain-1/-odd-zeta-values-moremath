import sympy as sp

A, B, D, E, c, m = sp.symbols('A B D E c m')
Tm, Tm1, Tm2, Tm3 = sp.symbols('T_m T_m1 T_m2 T_m3')
Vm, Vm1, Vm2 = sp.symbols('V_m V_m1 V_m2')
Wm, Wm1 = sp.symbols('W_m W_m1')
Ym = sp.symbols('Y_m')

# succ relation residuals (= 0 when true): eq_i := LHS - RHS
r1 = Tm1 - (c*Tm + Vm)         # catalanT_succ(m)      [Tm1 = T(m+1)]
r2 = Tm2 - (c*Tm1 + Vm1)       # catalanT_succ(m+1)
r3 = Tm3 - (c*Tm2 + Vm2)       # catalanT_succ(m+2)
r4 = Vm1 - (c*Vm + Wm)         # catalanV_succ(m)
r5 = Vm2 - (c*Vm1 + Wm1)       # catalanV_succ(m+1)
r6 = Wm1 - (c*Wm + Ym)         # catalanW_succ(m)

wayA = (m+2)*(m+1)*Ym + 3*(m+2)*Wm1 + Vm2
wayB = A*(m+2)*(m+1)*Wm + (A+B)*(m+2)*Vm1 + D*Tm2 - E*(m+2)*(m+1)*Vm - E*(m+2)*Tm1 + c**(m+2)

target = sp.expand(wayB - wayA)   # we want target = sum mu_i * r_i  (mirroring hB - hA + ... pattern)

mu1, mu2, mu3, mu4, mu5, mu6 = sp.symbols('mu1 mu2 mu3 mu4 mu5 mu6')
combo = mu1*r1 + mu2*r2 + mu3*r3 + mu4*r4 + mu5*r5 + mu6*r6
diff = sp.expand(target - combo)

unknowns_syms = [Tm, Tm1, Tm2, Tm3, Vm, Vm1, Vm2, Wm, Wm1, Ym]
polydiff = sp.Poly(diff, *unknowns_syms)
eqs = [co for _, co in polydiff.terms()]
sol = sp.solve(eqs, [mu1, mu2, mu3, mu4, mu5, mu6], dict=True)
print(sol)
