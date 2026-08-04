# BROWN26_MINING — what the Mellin/transfinite-diameter paper gives this program

**Source:** `papers/21-brown-2026-mellin-transfinite-diameter-rational-approx/NewDetCritReSubmit.tex`
("A multi-parameter irrationality criterion", Brown, resubmitted 2026-04).
**Mined:** 2026-08-04 (Fable fork).  Verdict up front: **one directly
load-bearing tool** (the contiguity-matrix appendix — it *is* the parametric
certificate our variational tower needs, worked out completely in the ζ(2)
toy), one strong conceptual home for our denominator work (p-adic
transfinite diameter), and a large body of machinery (transfinite-diameter
estimation) that is genuinely orthogonal to the bridge/companion questions.

## (a) What the paper actually does

* Objects: algebraic Mellin integrals `I(s₁..s_r) = ∫_σ f₁^{s₁}…f_r^{s_r} ω`
  on affine `X/ℚ` (§`setup`, eq. `introIs`); finite-dimensionality of de Rham
  cohomology ⇒ every `I(n̲)` is a ℚ-linear form in fixed periods `ξ₁..ξ_m`.
* New invariant: the **supremal transfinite diameter** (eq. `intro:suptau`)
  of the image `f(σ)` inside the "anciliary image variety" `V_f ⊆ 𝔸^r`
  (Zariski closure of `f(X)`), measured against a filtered ℤ-module `𝒩` of
  polynomials via generalized Vandermonde determinants (§4–5).
* Construction: positive-definite Gram matrices
  `Q^σ_N = (∫_σ 𝔣_i𝔣_j ω)` whose determinant is bounded by
  `t_𝒩(fσ)²` (§3); Minkowski then extracts a small *nonzero* integer linear
  form in the `ξ_i` (thm `smalllinearform`).  **Irrationality criterion:**
  `Sup²_𝒩(fσ)·δ_𝒩 < 1` (crit. `intro: limitcrit`).
* Philosophy (intro): *decouple denominators from asymptotics* — fill `Q`
  with many small-denominator integrals from the whole `r`-parameter family
  (not one Rhin–Viola line) and let the geometry of numbers find the small
  combination.  Proof-of-principle worked for ζ(2)/`M_{0,5}` (§8):
  predicted determinant asymptotics match experiment; a "2-dimensional"
  irrationality proof of ζ(2) is comfortably within the criterion.
* Explicitly *not* new-integral exotica: the integrals are the same
  dinner-party periods; the new content is what is done with the *family*.

## (b) Variational-tower objects: the paper's appendix is our missing infrastructure

The paper never differentiates in the parameters (it only ever *shifts* them
by integers).  But the appendix (§"Fast computation of I(h,i,j,k,l)",
ll. 2122–2250) constructs exactly the object our tower program needs:

* The de Rham bundle `𝓜_dR = H²_dR(M_{0,5}; (𝒪, ∇))` with
  `∇ = d + Σ s_i dlog u_i` over `k = ℚ(s₁..s₅)`, rank 2, basis
  `[ω₁] = dxdy/(1−xy)`, `[ω₀] = dxdy`; computed "by iterated higher direct
  images" relative to `M_{0,5} → M_{0,4} → M_{0,3}` (*method promised to be
  explained elsewhere* — watch for that paper).
* **Explicit contiguity matrices `M_i(s) ∈ M₂(ℚ(s))`** (§"Explicit
  formulae"), rational in the *continuous* parameters, satisfying the
  integrability relation `M_i(τ_i s)M_j(s) = M_j(τ_j s)M_i(s)`
  (eq. `Mconsistency`), with `I(τ_i s̲)`-vectors computed by matrix products
  applied to the **anchor vector `v = (ζ(2), 1)ᵀ`** (eq. `computeIs`).

Why this is load-bearing for us:

1. `M_i(s)` rational in `s` **is** a parametric certificate: our eps46
   identity (`L_BZ(Q̇) = −Σc_i′Q(n+i)`) is what differentiating a chain of
   such matrices in `s` produces.  In the `M_{0,5}` toy everything is
   explicit: `∂_{s_j} I(n̲)` = product-rule sum over the contiguity chain —
   a **closed, anchored evaluation of parameter-derivatives** (each term:
   matrices with one `∂M/∂s` insertion, applied to `v`).  This is precisely
   the "evaluation anchor for derivatives" that the Barnes view lacks:
   anchoring comes not from `I(a)` at non-integer `a` but from
   differentiating the *rational* transport equations and anchoring at the
   base point.
2. The ζ(5) analogue is the BZ 8-parameter family on `M_{0,8}`:
   `∇ = d + Σ s_i dlog u_i` in dihedral coordinates, `𝓜_dR` of small rank
   (periods `1, ζ(2), ζ(3), ζ(5)+2ζ(2)ζ(3)`), and contiguity matrices
   `M_i(s)` computable by the same iterated-direct-image method (or
   CMF-style hypergeometric derivation, which the appendix says is
   "presumably equivalent").  **Those matrices are the one-time cost of the
   ε⁵-attachment program**, and this paper shows exactly what they look
   like and how to validate them (integrability relation + reproduction of
   integer-point values).
3. Companions: not discussed as such, but the structure predicts where
   they live — the derivative of the transport chain inserts
   `∂M/∂s`-factors, so `∂I` is a linear form in the *same* periods with
   new rational coefficients: sequences satisfying the differentiated
   transport = inhomogeneous recurrences — i.e. exactly the
   second-solution/quasi-period data of eps46.  The `M_{0,5}` toy should
   exhibit the Apéry-ζ(2) companion `b_n`-weights as `∂I` data; this is a
   sharp, checkable prediction.

## (c) Weight-graded visibility / curve-blindness

Not addressed; nothing in the paper contradicts or anticipates the
Veronese-coupling phenomenon.  Two adjacent remarks worth noting: the
cohomological-determinant section (§`Cohomological determinants`, l. 1517)
formalizes "the de Rham matrix is the invariant; cycles are interchangeable
pairings" — the same forms-vs-cycles split our ε-machinery found
empirically; and pairing `det Q^dR` with crystalline Frobenius
(§`subsect:padic`) is the natural home for the program's Frobenius-spike
`diag(1,p³,p⁵)` observations.  Orthogonal to blindness per se.

## (d) Borrowable tools, with pointers

| tool | where | use for us |
|---|---|---|
| Explicit `M_i(s)` for `M_{0,5}` + integrability + anchor recursion | app. ll. 2129–2250, eqs. `Mconsistency`, `computeIs` | validate the variational tower end-to-end in a rank-2 toy; template for the BZ `M_{0,8}` matrices |
| Iterated-direct-image computation of `(𝒪,∇)`-cohomology | l. 2131 (method "to be explained elsewhere") | the systematic route to the BZ parametric certificate; watch for Brown's follow-up |
| Pole-vector denominator bound `d_{m₁}d_{m₂}I ∈ ℤ+ℤζ(2)` via orders of poles along `E ⊂ 𝓜̄_{0,5}` | eqs. `IM05denominatorbounds`, `p1-5vectors`, §8.1 | the geometric mechanism behind all the program's denominators; the ζ(5)-family version is what sharp-12 refines |
| p-adic transfinite diameter; `δ_n ~ Π_p |det Q^p_n|_p`; "congruences in de Rham cohomology improve denominators" | §`subsect:padic`, rem. `zeta2padic`, ll. 206, 1445 | conceptual home for sharp-12/crystal-Frobenius results; **export opportunity**: our proved endpoint congruences are exactly the input Brown says is missing |
| Multi-parameter criterion `Sup²·δ < 1`; fill `Q` with small-denominator off-line integrals | intro crit. `intro:crit`, §7 | long-term: worthiness beyond 0.86 for ζ(5) using the full 8-parameter family with *our* denominator theorems as the δ-input |
| Hankel/holonomic nonvanishing of `det Q` | §`Beyond positivity` | minor; alternative to positivity assumptions |

**Ignore for our purposes:** §§4–6 transfinite-diameter estimation
machinery (tensor/direct-sum bounds, hyperbola region) — analysis tooling
for the criterion's left factor, orthogonal to bridge/companions.

## Next actions (concrete)

1. **Toy-validate the tower** (small, decisive): implement the five
   `M_i(s)` from the appendix; check integrability and `I(0,0,1,0,1) = ζ(2)−1`;
   then compute `∂_{s_j}I(n,n,n,n,n)` two ways — differentiated contiguity
   products vs. harmonic-weighted double sums — and check the ζ(2)-Apéry
   companion weight appears.  This proves the "companions = anchored first
   variations" mechanism in a fully explicit rank-2 case.
2. **Build the BZ `M_i(s)`** for the 8-parameter `M_{0,8}` family
   (iterated direct images, or parametric telescoping on the Barnes
   representation) — the parametric certificate for the ε⁵ attachment.
   Before investing: check whether Brown's "to be explained elsewhere"
   method has appeared.
3. **Export sharp-12 into the determinant framework**: state the
   endpoint-congruence results as de Rham congruences / p-adic valuations
   of `det Q^p` for the ζ(5) family, and estimate how much they improve
   `δ_𝒩` versus the naive `d_n`-power bounds — this is where the program's
   arithmetic could buy worthiness, not just irrationality bookkeeping.

**Bottom line:** not orthogonal — the appendix alone justifies the mining.
The paper supplies the exact formal object (rational contiguity transport
with a period anchor) that turns our variational-tower observation into a
provable calculus, a worked toy to validate it on, and a denominator
framework that our sharp-12 results can feed.
