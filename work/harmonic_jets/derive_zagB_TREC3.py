import sympy as sp

h, n, k = sp.symbols('h n k')

# Mirror CatalanEndpoint.lean's catalanM construction, but for zagC/zagS with weight -h
# (instead of -4) and zagC's k-dependent recurrence coefficients.
#
# Auxiliary sum:  M_n := sum_{k=0}^n C(n,k) (-h)^{n-k} (k+1)^2 C_{k+1}
#
# Way A (pure Pascal shift, no recurrence): peel k=0 term, reindex, apply weight-k and
# weight-k(k-1) Pascal reductions to a := C∘succ.  This expresses M_{m+2} (using n=m+2)
# in terms of genTrC-shift-tower objects V (shift 1), W (shift 2), i.e. exactly the
# catalanM_wayA shape but generalized to weight c=-h:
#   M_{m+2} = (m+2)(m+1) W_m + 3(m+2) V_{m+1}... etc  (mirrors catalanM_wayA up to c).
#
# Way B (uses zagC_rec): substitute (k+1)^2 C_{k+1} = h(3k^2+3k+1) C_k - 3h^2k^2 C_{k-1}
# for k>=1, and C_1=1 for k=0.  Unlike catalanB_rec (constant coefficients 12,32), here
# the coefficients h(3k^2+3k+1) and 3h^2k^2 are QUADRATIC in k, so Way B needs
# weight-k, weight-k^2, weight-k^3, weight-k^4 Pascal reductions on both a := C (shift 0)
# and a := C∘pred (shift -1) -- i.e., substantially more machinery than CatalanEndpoint
# needed (which only needed weight up to k(k-1), degree 2, because 12,32 were constant).
#
# This script does NOT attempt the Lean-side algebra; it instead confirms, purely
# symbolically (treating C_j as free symbols, only using the recurrence to eliminate),
# that M_n reduces consistently and extracts the exact k-polynomial weights needed, to
# scope the Lean lemmas required.

print("Coefficients appearing in zagC_rec, as polynomials in k (to be Pascal-reduced):")
print("  h * (3k^2+3k+1)  -- degree 2 in k")
print("  3h^2 * k^2        -- degree 2 in k")
print()
print("Way B substitutes these into (k+1)^2 C_{k+1}, so after weighting by")
print("C(n,k)(-h)^{n-k}, we get terms of the form C(n,k)(-h)^{n-k} * k^d * C_k  for")
print("d = 0,1,2 (from k^2 term) and similarly shifted for C_{k-1}. Since C(n,k) k^2")
print("is NOT simply proportional to C(n-1,k) or C(n-2,k) alone (needs k(k-1)+k decomposition),")
print("we need genTrCW1 (weight k) and genTrCW2 (weight k(k-1)) as in CatalanEndpoint,")
print("applied THIS time to two different base sequences at once (C and C shifted by -1),")
print("with an extra additive split 3k^2+3k+1 = 3k(k-1) + 6k + 1 to reuse weight-k(k-1) and")
print("weight-k reductions already built (genTrCW2_eq, genTrCW1_eq) instead of new degree-2")
print("machinery -- i.e. Way B is expressible using exactly the same two Pascal-reduction")
print("primitives as CatalanEndpoint (weight-k, weight-k(k-1)), just applied more times.")
print()
print("Decomposition check: 3k^2+3k+1 = 3*k*(k-1) + 6*k + 1  ->",
      sp.expand(3*sp.symbols('k')**2+3*sp.symbols('k')+1 - (3*sp.symbols('k')*(sp.symbols('k')-1)+6*sp.symbols('k')+1)))
print("Decomposition check: k^2 = k*(k-1) + k                ->",
      sp.expand(sp.symbols('k')**2 - (sp.symbols('k')*(sp.symbols('k')-1)+sp.symbols('k'))))
