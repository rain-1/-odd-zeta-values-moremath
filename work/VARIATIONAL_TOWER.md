# VARIATIONAL_TOWER — the jet/contiguity program for ΣT·B₅ = (33/4)P_n
# (state after the first build session, 2026-08-04; fork of the Fable session)

Labels per programme convention.  Scripts: `work/z5eps/eps46_variation.py`
(parent session), `eps47_tower2.py` (this fork).  Read-only companions:
`work/CURVE_BLINDNESS.md`, `BRIDGE_CAMPAIGN_2026-08-03.md`.

## 1. The anchor mechanism is already in Brown–Zudilin `[CITED]`

CellZeta (2026-01-26 tex):

* l.729: *"any ℚ-linear relations between the integrals I(a) deduced from
  manipulating the integrand (for example, contiguity relations) also hold
  for I′(a), I″(a) and the rational coefficients Q(a), P̂(a), P(a)."* —
  the **transfer principle**: integrand-level identities descend to each
  coefficient row separately.  This is the license that turns any proved
  contiguity/variational identity into a statement about `P(a)` alone.
* l.424, l.1472: BZ explicitly flag the *absence* of computed contiguity
  relations / de Rham machinery for the 8-parameter family as the missing
  tool.  The tower program is precisely a proposal to build the minimal
  slice of it.

## 2. Rung 1, proved discretely `[PROOF SKETCH, sound; verification exact ℚ n ≤ 18]`

The eps46 identity `L_BZ(Q̇) = −Σᵢ cᵢ′(n)Q(n+i)`, `Q̇ = ΣT·Λ₁^{(n)}`,
has a purely discrete proof that avoids analytic continuation entirely:

1. The Zeilberger certificate for `Q_n` is a rational-function identity
   `L(T)(n,k,l) = Δ_k(T G₁) + Δ_l(T G₂)` in `(n,k,l)` `[CITED: BZ via
   Koutschan; certificate not re-derived here — the one assumption]`.
2. Differentiate it formally in `n` (rational identity ⇒ differentiable):
   `L(Ṫ) + L̇(T) = Δ_k(Ṫ G₁ + T Ġ₁) + Δ_l(…)` with `Ṫ = T·Λ₁`.
3. Sum over the integer lattice `k,l ≥ 0`.  At integer `n` every term has
   **finite support**: `T(n+i,·,·)` vanishes for `k > n+3`, and `Ṫ`
   vanishes on continuation cells because the `(n−k)`-factor zero is
   *double* (first derivative of a double zero is zero).  Telescoping
   boundary terms vanish; no continued family is ever invoked.

Byproducts verified: the k- and l-direction first variations vanish
identically (`N₁`-gauge directions), confirming the gauge reading.

## 3. Rung 2 in the n-direction FAILS — structurally `[MEASURED, exact ℚ]`

`eps47_tower2.py`: the twice-differentiated identity
`Σᵢ[cᵢ″Q + 2cᵢ′Q̇ + cᵢQ̈](n) = 0` (with `Q̈ = 2·ΣT(Λ₁²/2 + Λ₂)`,
finite-range) fails for every `n ≤ 15`, with defect `M(n)` a huge integer
sequence.  Diagnosis: second derivatives **resurrect the continuation
cells** — a double zero contributes `2g ≠ 0` to a second derivative — and
the resurrected layer has factorial growth `(k−n−1)!²·T̂ ~ k!·k^{l−2}`:
the gamma-continued double sum *does not exist* beyond first order in the
n-direction.  The defect `M(n)` is not in the degree-≤5 polynomial
`Q(n..n+3)`-module (held-out fits fail) and not in `span{Q,P̂,P}`: it is
the defect of an invalid identity, not a hidden companion.
**The n-direction anchors at order exactly one.**

## 4. Safe and unsafe letter directions `[DERIVED]`

For per-letter parameter directions (deforming `Γ(x_L+1) → Γ(x_L+1+t_L)`):

* **Safe at all jet orders** (never create support beyond `k,l ≤ n`):
  numerator letters `n, n+k, n+l, n+k+l` and denominator letters
  `k, l, k+l` (their Γ's are nonzero/finite on the whole range).
* **Unsafe at jet order ≥ 2**: `n−k, n−l` (each second-order jet revives
  the `k > n` cells with the same factorial divergence).
* Single-letter jets carry Euler-γ terms (`S₁ = p_L ≠ 0`); γ must be
  tracked as a formal symbol (it cancels in any valid identity).

Family-1's `B₅` needs `H^{(4)}_{n−k}, H^{(4)}_{n−l}` data (its `L₄` has
`∓64` on the mk/ml letters), i.e. **order-4 jets in the unsafe
directions**: the *sum-level* tower cannot reach `B₅` as tabulated.
Open question flagged (not resolved here): the `L₄/L₅` null freedom is
4-dimensional — determine whether a null-shifted representative of the
family has mk/ml-order ≤ 1 throughout; if yes, the safe sum-level tower
suffices after all.  (Needs the null basis from `eps17`.)

## 5. The correct home: the integral-level tower `[PROGRAM]`

Mixed jets `∂_{v₁}…∂_{v_j} I(a)` are contour integrals with polygamma
insertions — finite at every order, no support issues.  With the transfer
principle (§1), any identity proved for the jet integrals descends to the
`P`-row.  The proof scheme for the ε⁵ attachment:

1. **Parametric certificate**: a telescoping identity for the integrand
   (equivalently a contiguity/Picard–Fuchs system for `I(a)`) with the
   parameters symbolic along the ≤5-jet of the family-1 directions.  This
   is the single missing computational ingredient (and exactly the tool
   BZ call for at l.424).  Options: (i) parametric creative telescoping
   (Koutschan-class; expensive, one-time); (ii) solve for the certificate
   jet order-by-order from the t⁰ certificate — each order is a *linear*
   solve over ℚ(n,k,l) given the previous orders; (iii) derive from
   `M_{0,8}` Gauss–Manin/KZ data (dinner-party general; hardest, best).
2. Five differentiations along the (null-optimized) family-1 jet
   directions; the transfer principle anchors each rung.
3. The pinned combination's inhomogeneous parts must cancel (finite
   rational-function identity in the certificate data); the remaining
   homogeneous solution is pinned by `n = 0,1,2` initial values —
   yielding `ΣT·B₅ = (33/4)P_n` with **no certificate search**: every
   identity in the chain is a derivative of one proved identity.

## 6. Honest status summary

| item | status |
|---|---|
| transfer principle | proved in BZ (l.729) |
| rung 1, n-direction | proof sketch sound modulo the cited t⁰ certificate; exact ℚ n ≤ 18 |
| rung 2, n-direction | FAILS; divergence mechanism identified; defect characterized negatively |
| safe-direction taxonomy | derived (elementary) |
| B₅ reachability by sum-level tower | blocked as tabulated; null-freedom question OPEN |
| integral-level tower | program; needs the parametric certificate (§5.1) |

The next session's single most valuable step: **§5.1(ii)** — order-by-order
jet-solving of the parametric certificate from the t⁰ certificate, which
first requires obtaining/reconstructing the t⁰ certificate for the double
sum `Q_n` explicitly (an ansatz linear solve over ℚ(n,k,l); bounded and
mechanical), then one differentiation as proof of concept against the
proved rung 1.
