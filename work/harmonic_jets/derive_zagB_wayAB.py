import sympy as sp

# General framework mirroring CatalanEndpoint.lean's catalanM_wayA / catalanM_wayB /
# catalanT_rec_aux, for a general order-2 recurrence
#   (n+1)^2 f(n+1) = (A n^2 + B n + D) f(n) - E n^2 f(n-1),   f(0)=0, f(1)=1
# and transform T(n) = sum_k C(n,k) c^{n-k} f(k)  (c = weight).
#
# Shift towers: V(n) = genTr(f o succ, n), W(n) = genTr(f o (+2), n), Y(n) = genTr(f o (+3), n).
# Succ relations (from genTr_succ, exact, no recurrence used):
#   T(n+1) = c T(n) + V(n)
#   V(n+1) = c V(n) + W(n)
#   W(n+1) = c W(n) + Y(n)
#
# catalanM(n) := sum_k C(n,k) c^{n-k} (k+1)^2 f(k+1)
# Way A (pure Pascal, independent of A,B,D,E):
#   M(m+2) = (m+2)(m+1) Y(m) + 3(m+2) W(m+1) + V(m+2)
# Way B (uses recurrence once):
#   M(m+2) = A(m+2)(m+1)W(m) + (A+B)(m+2)V(m+1) + D T(m+2)
#            - E(m+2)(m+1)V(m) - E(m+2)T(m+1) + c^{m+2}
#
# Goal: eliminate Y(m), W(m+1), W(m), V(m+2), V(m+1), V(m) using the succ relations
# (evaluated at appropriate points) to get a pure-T relation among T(m), T(m+1), T(m+2), T(m+3).

A, B, D, E, c, m = sp.symbols('A B D E c m')

Tm, Tm1, Tm2, Tm3 = sp.symbols('T_m T_m1 T_m2 T_m3')   # T(m), T(m+1), T(m+2), T(m+3)
Vm, Vm1, Vm2 = sp.symbols('V_m V_m1 V_m2')               # V(m), V(m+1), V(m+2)
Wm, Wm1 = sp.symbols('W_m W_m1')                          # W(m), W(m+1)
Ym = sp.symbols('Y_m')                                    # Y(m)

# succ relations:
eqs = [
    sp.Eq(Tm1, c*Tm + Vm),
    sp.Eq(Tm2, c*Tm1 + Vm1),
    sp.Eq(Tm3, c*Tm2 + Vm2),
    sp.Eq(Vm1, c*Vm + Wm),
    sp.Eq(Vm2, c*Vm1 + Wm1),
    sp.Eq(Wm1, c*Wm + Ym),
]

wayA = (m+2)*(m+1)*Ym + 3*(m+2)*Wm1 + Vm2
wayB = A*(m+2)*(m+1)*Wm + (A+B)*(m+2)*Vm1 + D*Tm2 - E*(m+2)*(m+1)*Vm - E*(m+2)*Tm1 + c**(m+2)

# Solve succ relations for Vm, Vm1, Vm2, Wm, Wm1, Ym in terms of Tm,Tm1,Tm2,Tm3
sol = sp.solve(eqs, [Vm, Vm1, Vm2, Wm, Wm1, Ym], dict=True)[0]

wayA_sub = sp.expand(wayA.subs(sol))
wayB_sub = sp.expand(wayB.subs(sol))

relation = sp.expand(wayA_sub - wayB_sub)
relation = sp.collect(relation, [Tm, Tm1, Tm2, Tm3])
print("General elimination (Way A - Way B = 0), collected in T's:")
print(relation)

print()
print("=== Substituting zagC's coefficients A=3h,B=3h,D=h,E=3h^2,c=-h ===")
h = sp.symbols('h')
subs_zag = {A: 3*h, B: 3*h, D: h, E: 3*h**2, c: -h}
rel_zag = sp.expand(relation.subs(subs_zag))
rel_zag = sp.collect(rel_zag, [Tm, Tm1, Tm2, Tm3])
print(rel_zag)

print()
print("=== Substituting catalanB's coefficients A=12,B=12,D=4,E=32,c=-4 (sanity check) ===")
subs_cat = {A: 12, B: 12, D: 4, E: 32, c: -4}
rel_cat = sp.expand(relation.subs(subs_cat))
rel_cat = sp.collect(rel_cat, [Tm, Tm1, Tm2, Tm3])
print(rel_cat)
