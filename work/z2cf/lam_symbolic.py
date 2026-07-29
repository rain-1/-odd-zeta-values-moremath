"""(LAM) symbolic proof: W(n,k) = P(n,k) - 3(n+1)/(n+1-k), P polynomial in k;
then Sum (-1)^k C(n,k) W = 3(-1)^{n+1} via two classical atoms."""
import sympy as sp
n,k=sp.symbols('n k')
rho = k**2+k*(1+6*n)-4-15*n-11*n**2
W = 2*(n+1)**2/(n+1-k)**2 - 2*(n-k)/(n+k) + k*rho/((n+1-k)**2*(n+k))
Wc = sp.cancel(sp.together(W))
num,den = sp.fraction(Wc)
print("denominator factored:", sp.factor(den))
ap = sp.apart(Wc, k)
print("apart in k:", ap)
# check claim
P = sp.expand(ap + 3*(n+1)/(n+1-k))
print("P polynomial in k?:", sp.simplify(sp.together(P)), "->",
      sp.fraction(sp.cancel(sp.together(P)))[1])
# atom check: with P = c0 + c1 k + c2 k^2 (say), alternating sums vanish for n>deg
Pp = sp.Poly(sp.cancel(sp.together(P)), k)
print("P coeffs (in n):", [sp.factor(c) for c in Pp.all_coeffs()])
