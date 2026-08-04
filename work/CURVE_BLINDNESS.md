# CURVE_BLINDNESS — why polynomial-curve deformations cannot see weight five,
# and what the proof says the missing instrument is

**Author:** Fable, 2026-08-04.  Companion to `BRIDGE_CAMPAIGN_2026-08-03.md`
§5b and `work/z5eps/eps41/42.log`.  This is an understanding document, not a
formalization target.  Labels: the two lemmas are proved here; the finite
statements cite the two-prime scans as computations.

## 0. The phenomenon

Curve atoms `T(n+α(ε), k+β(ε), l+γ(ε))`, with `(α,β,γ)` polynomial in ε,
combined ℚ-linearly and *pinned* (`[ε¹]=[ε²]=0` per ζ-grade,
`[ε³] ∈ ⟨Q,P̂⟩`), always have `[ε⁵]`-row confined to `⟨Q,P̂⟩`: the `P_n`
component is forced to vanish — at curve degrees 1, 2, 3, both primes,
every ζ-grade (eps41/42).  Meanwhile the *formal* family-1 deformation
emits `(33/4)P_n` at ε⁵ — and is exactly the deformation that admits no
meromorphic realization.  Why?

## 1. Lemma A (the coupling / Veronese lemma)

*Setup.*  For a curve atom `v`, each letter `L` has shift series
`s_L(ε) = Σ_{i≥1} d_{i,L} ε^i`, with `d_{i,L}` the letter's linear image of
the curve coefficient `u_i`.  The cell expansion is
`T·exp(Σ_L p_L Σ_{j≥1} c_j (H^{(j)}_{x_L} − ζ-const) s_L(ε)^j)`,
`c_j = (−1)^{j−1}/j`.  A weight-`w` letter monomial appearing at ε-order
`r` collects, per letter factor, a coefficient `[ε^{m_i}] s_L^{j_i}` with
`Σ j_i = w` (the harmonic weight) and `Σ m_i = r` (the ε-order).

**Lemma A.**  *In the top-graded case `w = r`, every factor has `m_i = j_i`
(since always `m_i ≥ j_i`), and `[ε^j] s_L^j = d_{1,L}^j`.  Hence the
top-weight content of `[ε^r]` of a curve atom is a polynomial in the
**first-order direction data alone**, through its pure powers
`d₁^{⊗r}` — the Veronese cone.  All higher curve coefficients
`u₂, u₃, …` feed only harmonic weights `< r` at order `r`.*

Proof: `[ε^m] s^j` with `s = d₁ε + O(ε²)` requires `m ≥ j`, with equality
picking exactly the `(d₁ε)^j` term.  ∎

Consequence: at ε⁵, the only way a curve atom touches weight-5 harmonic
forms — the only forms whose row image can contain `P_n` (the Frobenius
spike `{0,3,5}`: weight-3 forms reach `P̂`, never `P`; see §3(2)) — is
through the fifth powers of its first-order direction.

## 2. The moment-mixture framing

A ℚ-combination of curve atoms is a *mixture of Veronese moment vectors*:
atom `v` contributes `(d_v, d_v^{⊗2}, …, d_v^{⊗5})` (plus u₂,u₃-corrections
in the sub-top weights), and the combination's graded data is the mixture
`μ_m = Σ_v c_v d_v^{⊗m}` (top-graded part).  The pinning conditions are
linear conditions on the *low* moments `μ₁, …, μ₄` — and, crucially,
because the ζ-graded components of each `[ε^r]` involve products
`ζ`-constant × lower rows, the per-grade pinning constrains **many
separate moment aggregates**, not just one per order.

The question "can pinned combinations reach `P` at ε⁵" is then: over the
linear span `M = span{(d, d^{⊗2}, …, d^{⊗5})}`, does the fibre of the
pinning conditions project, at the μ₅ slot, onto forms whose row image
leaves `⟨Q,P̂⟩`?

Two structural facts now do all the work:

*(a) Polarization is blocked by coupling.*  Over the free symmetric
algebra one can polarize: any degree-5 tensor is a combination of fifth
powers.  But moving `μ₅` by a difference of nearby Veronese points,
`c[(d+δ)^{⊗5} − d^{⊗5}] ≈ 5c·δ⊙d^{⊗4}`, moves `μ₄` by
`4c·δ⊙d^{⊗3}` — the *same order in `cδ`*.  Pure fifth-symmetric motion
with pinned lower moments is not available: for curves, all moments are
powers of the same directions, so `μ₅` cannot be steered independently of
`μ₁…μ₄`.  This is the precise failure of the "polarization escape."

*(b) The pinned μ₅-fibre lands in the degenerate sector.*  Which fifth
powers survive the pinning is a finite linear-algebra computation over the
graded row maps — and that computation **is** the eps41/42 scan: the
pinned fibre's weight-5 row image is `⟨Q,P̂⟩` exactly, at both primes,
through cubic curves.  (The low-order null spaces involved are the known
small ones: `N₁ = ⟨D1,V1⟩` at weight 1 — note `D1 = (∂_k+∂_l)log T` is the
summation-shift *gauge* direction — and the α-line at weight 2.)

**Theorem (curve blindness), with the labels honest:**  Lemma A +
polarization-blocking are proved; given them, the confinement
`[ε⁵]-row ⊆ ⟨Q,P̂⟩` for all pinned curve combinations reduces to the
finite rank statements verified two-prime in eps41/42.  The theorem is
thus: *pinning + power-coupling enslaves the top-weight data to the
low-order null sector, and the null sector's fifth powers are row-blind to
`P`.*

## 3. Why family-1 evades, and consistency checks

1. Family-1's per-letter data table is **not curve-consistent**: e.g. its
   letter `l` has `e₁ = 6` while `e₅ = 528` — not `6⁵`-proportional; its
   order-5 data is an *independent datum*, i.e. family-1 lives in the free
   (polarized) letter algebra, not on the Veronese cone.  That freedom is
   exactly what the realizability obstruction (`δ = ε/120`, ~10¹¹
   multiplicities) measures from the other side: decoupled letter data
   has no polynomial-curve realization.  The two negatives of the campaign
   are one fact seen twice.
2. Consistency with the programme's older data: the resonance spike
   `{0,3,5}` (only `s = 3, 5` carry rows) plus the scans' observation that
   weight-3 forms reach `P̂` at *both* ε³ and ε⁵ but `P` never — `P` is
   top-graded and needs genuine weight-5 forms.
3. Historical confirmation of the polarized prediction: the original
   Z5CF_EPSILON search space *was* the free letter algebra (arbitrary
   `(e₁,…,e₅)` per letter), and it *did* find a `P`-emitter.  Free data
   reaches `P`; curve data cannot.  The boundary between the two is the
   theorem.

## 4. The tool that falls out

The proof names the missing instrument precisely: an object whose
**fifth-order letter data is decoupled from its lower jets**.

* Formally: polarized atoms — the free letter algebra.  Already realized
  (family-1), but with no analytic anchor: that is the bridge's current
  state.
* Analytically: decoupled fifth-order jets of a parametric family are
  **fifth mixed partial derivatives of the period integral**,
  `∂_{v₁}…∂_{v₅} I(a)` — honest contour integrals with log-weighted
  integrands, with no ε¹…ε⁴ content by construction (pinning is free).
  Their span is the full polarized algebra: they can reach `P`-emitting
  forms.  What they lack is an **evaluation anchor**: BZ's decomposition
  `I(a) = Q(2ζ5+4ζ2ζ3) − 4P̂ζ2 − 2P` is an arithmetic statement at
  integer `a`, not an analytic identity in `a`; derivatives need the
  *variation* of the period.
* Therefore the concrete mathematical object to develop is the
  **variation of the BZ period in its parameter directions**: the
  inhomogeneous Picard–Fuchs / Frobenius structure of `I(a)` along `v`,
  i.e. what `∂_v I` is as a period-like quantity at integer points.  The
  discrete shadow of this (finite differences across integer `a`) is
  BZ's contiguity algebra — anchored but rational-letter only; the
  infinitesimal version carries the harmonic letters and is exactly where
  second solutions / quasi-periods live.  Note the resonance with the
  sporadics programme: companions **are** second solutions of the
  recurrence; this note says companions are, equally, first variations of
  the period in parameter directions — and the ζ(5) bridge is the
  statement that a specific *fifth* variational jet is anchored to the
  recurrence-defined `P_n`.

**Next mathematical target (the productive avenue):** write down the
first-order variation `∂_v I(a)` of the cellular integral at the
totally-symmetric point for the simplest direction `v`, identify its
evaluation (it should be a linear form in the same zeta values with
coefficients built from `Q', P̂', P'`-type derivative sequences — i.e.
second-solution data of the L_BZ recurrence), and verify against exact
computation.  If first variations anchor, the polarized-atom program has
its induction base, and the bridge becomes a (finite) statement in the
variational calculus of the BZ family rather than a certificate hunt.

## 4b. FIRST APPLICATION — the anchor exists at order one `[VERIFIED exact ℚ, n ≤ 18]`

`work/z5eps/eps46_variation.py` + inline test:

* The k- and l-direction first variations vanish identically
  (`ΣT·Λ₁ = 0`): they are the **gauge** directions (the `N₁` residue
  identities), as §2 predicted.
* The n-direction first variation `Q̇(n) = ΣT·Λ₁^{(n)}`,
  `Λ₁^{(n)} = H_n + H_{n+k} + H_{n+l} − 2H_{n−k} − 2H_{n−l} + H_{n+k+l}`,
  satisfies **exactly the differentiated Brown–Zudilin recurrence**:

  > `L_BZ(Q̇)(n) = − Σ_{i=0}^{3} c_i′(n) · Q(n+i)`,

  with `c_i′` the literal polynomial derivatives of the certified
  coefficients.  Exact over ℚ for n ≤ 18.

* Proof route (identified, not yet written): the Zeilberger/Koutschan
  certificate for `Q` is a *rational-function identity in n*, hence holds
  for the gamma-continued family in continuous `n`; differentiating it in
  `n` yields the displayed identity, with the boundary/range variation
  contributing only at second order (continuation cells vanish doubly).

* **Consequence — the variational tower program for the ε⁵ attachment.**
  The same logic iterates: j-th variations satisfy the j-fold
  differentiated (inhomogeneous) recurrence tower.  Family-1's `B₅` is a
  polynomial in decoupled per-letter jets, i.e. a combination of mixed
  fifth partials of the **8-parameter** BZ family at the symmetric point;
  given a parametric certificate for `Q(a)` (rational identity in all
  parameters — obtainable by parametric creative telescoping, or from
  BZ's contiguity system), five differentiations plus initial values
  would **prove** `ΣT·B₅ = (33/4)P_n` with no polynomial certificate
  search — and with it, sharp-12 by re-running the endpoint analysis on
  the `B₅` weight (completion standard #4 of the bridge prompt).  The Δ₅
  identity (compact ω₅ vs `B₅`) would remain the only unproved piece of
  full (BRIDGE).

## 5. What would falsify this picture

* A pinned curve combination at some degree ≥ 4 reaching `P` (would break
  the moment-coupling argument's finite part — Lemma A itself cannot
  break).
* A weight-3 form whose row equals `P_n` (would break the graded-spike
  input; testable by a Φ₃-row rank computation).
* First variations `∂_v I` failing to be expressible in second-solution
  data (would break the anchoring proposal, leaving blindness true but
  the escape unidentified).
