"""Test the (Phi-VANISH) identities that make the fibre sum rank-1 mod p^2.

In-regime (s<=r, t<=r, r+s+t<p) the p-adic block factorisation gives
   T(n,bp+s,cp+t) = T(a,b,c) * T(r,s,t) * (1 + p*D1 + p^2*D2 + ...)
with D1 = a*Phi_a + b*Phi_b + c*Phi_c and
   Phi_b(s,t) = A1(s) + 2 B1(s) + C1,   Phi_c(s,t) = A1(t) + 2 B1(t) + C1
(letters at level r).  Rank-1 mod p^2 needs  sum_{s,t} T(r,s,t) Phi_b = 0 (mod p).
Here: is it 0 EXACTLY?
"""
from fractions import Fraction as F
from math import comb
from core import Hs, T

def phis(r, s, t):
    A1s = Hs(r + s, 1) - Hs(s, 1)
    B1s = Hs(r - s, 1) - Hs(s, 1)
    A1t = Hs(r + t, 1) - Hs(t, 1)
    B1t = Hs(r - t, 1) - Hs(t, 1)
    C1 = Hs(r + s + t, 1) - Hs(s + t, 1)
    Phi_b = A1s + 2 * B1s + C1
    Phi_c = A1t + 2 * B1t + C1
    Phi_a = (Hs(r + s, 1) + Hs(r + t, 1) + Hs(r + s + t, 1) + Hs(r, 1)
             - 2 * Hs(r - s, 1) - 2 * Hs(r - t, 1))
    return Phi_a, Phi_b, Phi_c

print("r :  sum T*Phi_a           sum T*Phi_b        sum T*Phi_c       Q_r")
for r in range(0, 11):
    Sa = Sb = Sc = F(0); Qr = 0
    for s in range(r + 1):
        for t in range(r + 1):
            Trst = T(r, s, t)
            Qr += Trst
            pa, pb, pc = phis(r, s, t)
            Sa += Trst * pa; Sb += Trst * pb; Sc += Trst * pc
    print(r, ':', Sa, ' | ', Sb, ' | ', Sc, ' | ', Qr)
