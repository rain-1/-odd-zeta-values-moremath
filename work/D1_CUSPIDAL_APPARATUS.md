# D1_CUSPIDAL_APPARATUS — an Apéry-quality apparatus for a cusp-form L-value (D-1 solved)

**Session 2026-08-05 (fourth arc).**  Solves open problem (D-1) of
`CUSPIDAL_COMPANION.md` — and strictly more: the second-kind term is not
merely cancelled between two companions; a *vanishing-source* construction
eliminates it structurally and yields exponentially convergent,
d_n³-integral rational approximations to a cuspidal L-value.
Scripts: session logs + `work/z5eps/eps62*`, constructions rerun exactly;
all claims labeled.

## 1. The negative results that forced the right construction

* **κ-cancellation fails**: κ = Θ_{f,2}(τ_c)/Θ_{Φ,2}(τ_c) =
  1.39173177734068830824… is neither rational nor quadratic
  `[PSLQ-excluded, 40 digits]` — no ℚ-combination of the level-6 cuspidal
  and Eisenstein companions kills the quasiperiod.
* **Diagnosis of slow convergence**: B^f_n − ξ_fA_n grows like
  α^n n^{-7/2} because R = t/√P is singular AT the fold — equivalently
  f(τ_c) ≠ 0.  Apéry-quality error requires the source to VANISH at the
  Fricke point.  Impossible at level 6 (dim S₄ = 1).

## 2. The construction (Domb's curve, level 12)

dim S₄(Γ₀(12)) = 2, spanned by the embeddings f₆(q), f₆(q²) of the
level-6 newform f₆ = (η₁η₂η₃η₆)².  Facts established:

* Family α's fold nome is the level-12 Fricke point:
  q_c = e^{−2π/√12} `[matches to series precision]`.
* **f₆(τ₁₂) = 4·f₆(2τ₁₂) exactly** (`[PSLQ, 35+ digits]`; provable via the
  W₁₂-swap of the embeddings).  Hence the integral vanishing combination
  \[ f^* = f_6(q) - 4f_6(q^2) = q - 6q^2 - 3q^3 + 12q^4 + 6q^5 + \dots
     \in S_4(Γ_0(12)),\qquad f^*(τ_{12}) = 0, \]
  and f* is **Fricke-odd**: f*|W₁₂ = −f*.
* **The source identity**: with P_α = 1−20t+64t² = (1−4t)(1−16t),
  \[ L_α\big(F_α\,θ_q^{-3}f^*\big) \;=\; \frac{t}{\sqrt{1-4t}}, \]
  i.e. f*·√(1−4t) = Φ_α — the vanishing combination extracts the
  CONJUGATE root factor only `[exact rational reconstruction: the
  inhomogeneity coefficients are the central binomials C(2n,n)]`.

## 3. The apparatus `[VERIFIED n≤200 numeric / n≤40 exact]`

Define B*₀ = 0, B*₁ = 1 and
\[ m^3B^*_m = (2m{-}1)(10(m{-}1)^2{+}10(m{-}1){+}4)B^*_{m-1}
   - 64(m{-}1)^3B^*_{m-2} + \binom{2m-2}{m-1}, \]
(the Domb recurrence with central-binomial forcing; B* = 0, 1, 37/4,
818/9, 141587/144, …).  Then with A_n the Domb numbers:

* **d_n³·B*_n ∈ ℤ** (exact, n ≤ 40);
* the error is exponentially small: B*_n/A_n stabilizes at rate ≈ 4^{-n}
  (Δ ≈ 10⁻¹²¹ at n = 200);
* \[ \boxed{\;\lim_{n\to\infty} \frac{B^*_n}{A_n} \;=\; \frac{L(f_6,3)}{2}\;}
  \qquad `[PSLQ: -2ξ^* + L(f_6,3) = 0, \text{ residual } 2\times10^{-61}]` \]
  — **pure critical L-value: no quasiperiod, no πL(f,2), no ζ(3).**

This is, to our knowledge, the first Apéry-style apparatus (integral
d_n³-denominators, exponential convergence, 3-term-plus-forcing
recurrence over ℤ) whose limit is a critical L-value of a cusp form —
manufactured, not found: level chosen for dim S₄ = 2, source chosen in
the Fricke-odd line, vanishing at the fold by construction.

## 4. The mechanism (to prove in the Project A paper)

Two independent effects, both from Fricke-oddness at the fixed point:

1. **Exponential convergence**: f*(τ₁₂) = 0 ⇒ the inhomogeneity
   t·f*/Φ_α is regular at the fold ⇒ the particular solution's
   singularity sits at the conjugate root (radius 1/4 vs 1/16) ⇒ error
   ratio (t_c/t_c')ⁿ = 4^{-n}.
2. **Clean limit**: for an ε = −1 source the fixed-point Eichler
   equation determines precisely the combination the fold connection
   extracts (value + quasi-derivative), leaving period-polynomial data
   only; the parity of the odd period polynomial then selects the single
   critical value L(f,3).  (At ε = +1 — the level-6 experiment — the
   value is contaminated by the second-kind term, exactly as observed.)

Conjecture (D-2): for every genus-zero level N with dim S_{r+1} ≥ 2 and a
rectified sporadic family, the Fricke-odd vanishing combination yields a
d_n^r-integral exponentially-convergent apparatus with limit a rational
multiple of an odd-period critical L-value.  Candidates to test next:
level 8 (ε-family? dim S₄(Γ₀(8)) = 1 — no), level 9 (ζ-family, η₃⁸,
dim 1 — no), level 20 (η-family: dim S₄(Γ₀(20)) ≥ 2 via level-5 and
level-10 oldforms — yes, targets L-values of 5.4.a.a-type forms), and
δ (level 12: same f* on a different curve — immediate).

## 5. Irrationality bookkeeping (honest)

|d_n³(A_nL(f,3)/2 − 2·? B*_n)| ~ e^{3n}·4ⁿ·(subexp) → ∞: the apparatus
does NOT prove irrationality of L(f₆,3) (need error < e^{-3n}·A_n^{-1}-
scale; here the ratio of decay 4ⁿ to d_n³ = e^{3n} loses).  Its value is
structural: cuspidal critical L-values are now inside the
modular-anchor factory with Apéry-quality arithmetic, and the
convergence/denominator tradeoff becomes an optimization problem over
(level, family, source) — the same problem Apéry's ζ(3) wins for the
Eisenstein class.

## 6. Evidence labels

f₆(τ₁₂) = 4f₆(2τ₁₂): numeric PSLQ, proof route via W₁₂ eta
transformations (routine, not written).  Source identity
f*√(1−4t) = Φ_α: exact coefficientwise to q^40 via the central-binomial
reconstruction of R*; Sturm-boundable like the level-6 case (weight 8,
level 12, bound 16).  Limit: 61-digit PSLQ, plus 121-digit stability of
the ratio.  d_n³-integrality: exact to n = 40.  Mechanism §4: observed +
argued, not proved.  Conjecture D-2: two data points (levels 6, 12).

---

## 7. Sol's review (share 6a730c40-…) and the δ control `[same session, executed]`

Sol passed the result on with a six-item theorem package (source identity /
forced recurrence / fold-regularity / Fricke functional equation /
period-parity / denominator theorem — adopted as the Project A paper's
spine for this section) and restated D-2 with full hypotheses:

> For a modular Picard–Fuchs family with a fold fixed by an Atkin–Lehner
> involution, a rational integral source in the (−1)-eigenspace that
> vanishes to the required order at the fold yields a regularized
> companion whose connection value lies in the odd critical-period line.

**δ control (Sol's directed test — same f*, δ's curve):**
* d_n³B^{f*,δ}_n ∈ ℤ still holds (n ≤ 40) — the integrality layer is a
  property of (level, weight, d_n-structure), independent of the curve.
* But δ's fold is complex (q_c ≈ 0.1137 − 0.1970i ≠ the Fricke point),
  f*(q_c^δ) ≈ 0.292 + 0.103i ≠ 0: no regularization; R_δ's coefficients
  oscillate with |ratio| → 9 (both conjugate folds singular).  The
  vanishing-at-THE-FOLD hypothesis is necessary, exactly as the refined
  D-2 states.

**Classification corollary (new):** a rational vanishing source needs
(i) a real fold at an AL fixed point and (ii) dim S_{r+1} ≥ 2.  Among the
nine order-3 sporadics: real folds only at α, γ, ε, ζ (levels 12, 6, 8,
9); cusp dimensions 2, 1, 1, 1.  **α is the unique sporadic family
admitting the D-1 construction.**  The complex-fold families (B, δ, η)
are excluded over ℝ outright — Sol's suggested η test at level 20 is
answered by this clause without computation (η's disc is −16).  Further
instances require non-sporadic rectified families at genus-zero levels
with bigger cusp spaces — the reverse factory's next search domain, now
with a quantitative objective (maximize error-decay base over
denominator-growth base).

---

## 8. Proof notes toward Sol's six-item package `[fifth arc]`

Sol's newest review (share 6a730e52-…) restated D-2 as a mechanism
theorem with three separated layers (integral structure → d_n³;
fold-vanishing → regularization; odd parity → odd critical value),
boxed the reverse-factory search domain, and mandated the six-item proof
sequence.  Progress this session:

**Item 4 (Fricke functional equation) — PROVED (route complete).**
With ε₆ := ε(f₆, W₆) = +1 (from λ₂ = −a₂/2 = 1, λ₃ = −a₃/3 = 1):
\[ (f_6|_4W_{12})(τ) = f_6(-1/(12τ))\,(\sqrt{12}\,τ)^{-4}
   = ε_6\,(\sqrt6\cdot2τ)^4 f_6(2τ)\,(\sqrt{12}τ)^{-4} = 4f_6(2τ). \]
Hence W₁₂ acts on the oldspace span{f₆(q), f₆(q²)} as the involution
f₆(q) ↦ 4f₆(q²), f₆(q²) ↦ ¼f₆(q); eigenvectors f₆ ∓ 4f₆(q²) with
eigenvalues ±1.  **Corollaries, both previously numeric-only:**
(i) c = 4 (the vanishing relation is the eigenvector condition);
(ii) f* is the −1-eigenvector, and since the weight-4 automorphy factor
at the fixed point is (√12τ₁₂)⁴ = 1, f*(τ₁₂) = −f*(τ₁₂) = 0.
Two items of §6's evidence ledger upgrade from [PSLQ] to [PROVED-sketch].

**Item 5 (period parity) — structure verified, constants pending.**
Elementary consequences of ε(f*) = −1, all numerically confirmed:
Λ*(2) = 0 exactly (odd FE kills the even critical value — this IS the
reason no L(f,2) appears); Λ*(1) = −12·Λ*(3) (FE at level 12);
Λ*(3) = L(f₆,3)/(8π³) (embedding scaling; consistent to truncation).
The fold split ξ* = Θ*(τ₁₂) + (2π/√12)Θ*₂(τ₁₂) is verified to 25
digits, F_α|W₁₂ = −12τ²F_α (eta computation, so F′(τ₁₂) = 12τ₁₂F(τ₁₂)),
and the ε = −1 value identity ρ*(τ₁₂) = 0 checks (it is equivalent to
Λ*(1) + 12Λ*(3) = 0).  What remains for the exact ½: the derivative
fixed-point identity's orientation/normalization constants (the hand
computation produced an inconsistent constant; the route — differentiate
the weight-(−2) cocycle at the fixed point, substitute
Θ*′ = 2πiΘ*₂ and F′/F = 12τ₁₂ — is correct, the bookkeeping needs the
careful write-up).  [ROUTE WRITTEN, CONSTANT OPEN]

**Items 1–3, 6:** unchanged status (source identity exact to q^40 +
Sturm-boundable; forced recurrence formal given item 1; fold-regularity
lemma elementary given R* = t/√(1−4t); d_n³ theorem open beyond n≤40).

---

## 9. The irrationality race (Sol's scanner, Route 1 executed; the Φ_γ(τ_c) = 0 discovery)

**Sol's score** (share 6a730d0a-…): δ|β| < 1 with A_n ~ α^n, error ~ β^n,
denominators ≪ δ^n; for our families β = t_c/t_c'-driven: |A_nξ−B_n| ~
|t_c'|^{-n}, δ = e^r.  **Route-1 scan over all fifteen** (larger root
t_c' of P, δ|β| = e^r/|t_c'|):

| fam | r | |t_c'| | e^r/|t_c'| | verdict |
|---|---|---|---|---|
| D (ζ2) | 2 | 11.09 | 0.67 | **WIN — Apéry's ζ(2)** |
| γ (ζ3) | 3 | 33.97 | 0.59 | **WIN — Apéry's ζ(3)** |
| ε | 3 | 1.457 | 13.8 | fail (best of the rest) |
| all others | | ≤ 1 | ≥ 7.4 | fail |

Exactly the two classical Apéry wins, nothing near the boundary — Sol's
expectation confirmed with the exact numbers.

**Structural discovery `[VERIFIED to 1e-122]`:** Φ_γ(τ_c) = 0 — the
classical Apéry ζ(3) source itself vanishes at the fold; it is the
**W₆-odd Eisenstein** direction (any odd weight-4 form vanishes at the
fixed point since the automorphy factor is +1).  So Apéry's miracle is
*the same construction as our D-1 apparatus* — odd source vanishing at
the AL-fixed fold — realized in the Eisenstein class at a level whose
root ratio beats e³.  One mechanism, two classes:

| | odd Eisenstein source | odd cusp source |
|---|---|---|
| level 6 (ratio 34 > e³) | **Apéry's ζ(3) proof** | S₄⁻(Γ₀(6)) = 0 — none exists |
| level 12 (ratio 4 < e³) | (ζ(3)-type, loses race) | our L(f₆,3)/2 apparatus, loses race |

**The precise open problem this leaves (the cuspidal-Apéry question):**

> Find a genus-zero group Γ with a rectified family whose AL-fixed fold
> has conjugate-root ratio |t_c'/t_c|·|t_c| … i.e. |t_c'| > e^r, and
> with S_{r+1}^−(Γ) ≠ 0.  Then the odd-cusp companion would give a
> d_n^r-race-winning apparatus for a cusp-form critical L-value —
> an irrationality proof of a cuspidal period, provided the d_n^r
> integrality (Eisenstein-proved, cuspidally only observed) survives.

Failure modes to respect: cuspidal modular-symbol denominators may be
worse than d_n^r (Sol's warning), and the mixed-source fix at level 6
is impossible (Φ_γ vanishes at the fold, so no Eisenstein subtraction
can force f₆ to vanish there — verified).  Sol's scanner (routes 2–5:
auxiliary-form families, cusp cancellation, pullback acceleration) is
the search instrument; the sporadic table itself is exhausted.
