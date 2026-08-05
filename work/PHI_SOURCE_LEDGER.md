# PHI_SOURCE_LEDGER — the companion sources Φ(q) of the fifteen sporadic pairs

**Session 2026-08-05.**  Executes flagship steps 1, 2 and 4 of Sol's proposed
research program (ChatGPT share `6a72ee3d-74dc-83ed-a73a-224ee7e2b707`):
identify the companion source
\[ Φ(q) = \frac{t\,σ^r}{P(t)\,F} \qquad (B = F\,θ_q^{-r}Φ,\ \text{the proved
uniform companion formula}) \]
as an exact modular object for every family, and derive the Apéry limits
from it.  Scripts: `work/z5eps/eps60_phi_source.py`, `eps60b_phi_holdouts.py`,
`eps61_eichler_limits.py`, `eps61b_complex_limits.py` (+ `eps60_results.json`,
`eps60b_results.json`).  All series arithmetic exact (`Fraction`); labels per
program convention.

## 1. Headline

**Twelve of the fifteen sporadic companion sources are pure Eisenstein series
of weight r+1** (weight 3 for the R2 six, weight 4 for the order-3 families)
on the level of the eps51 dictionary — **no cuspidal component anywhere**
`[VERIFIED: exact ℚ, coefficientwise to q^60]`.  The fits were found at
q^26 and survived the held-out extension q^27..q^60 (a 34-coefficient
held-out band, the same discipline as the eps57 prime test).

This is the conceptual explanation of the whole limit column of the
sporadics table: Eisenstein source ⇒ Eichler value = Dirichlet L-value /
zeta value.  It also locates Sol's "reverse factory" precisely: a genuinely
new (elliptic) Apéry limit requires a *cuspidal* source, which the sporadic
class provably-at-q^60 does not contain.

## 2. The identifications `[VERIFIED q^60, zero-tail]`

Notation: σ_χ^{(k)}(m) = Σ_{d|m} χ(m/d) d^k (χ in the *inner* position:
"mode 2"); σ̃_χ^{(k)}(m) = Σ_{d|m} χ(d) d^k ("mode 1"); σ₃ ordinary.
All coefficient laws below give Φ = Σ_{m≥1} c(m) q^m exactly (μ=1: no
rescale needed for any family — Φ is already integral in the canonical
nome).

| fam | r | wt | c(m) | level |
|---|---|---|---|---|
| A | 2 | 3 | σ̃_{χ₋₃}²(m) − σ̃_{χ₋₃}²(m/2) | 6 |
| B | 2 | 3 | σ_{χ₋₃}²(m) − 6σ_{χ₋₃}²(m/2) − 8σ_{χ₋₃}²(m/4) | 36 |
| C | 2 | 3 | σ_{χ₋₃}²(m) − 8σ_{χ₋₃}²(m/2) | 6 |
| D | 2 | 3 | Σ_{d|m}(ψ₁(d) − 2ψ₂(d))d², ψ₁, ψ₂ = Re, Im of the odd char mod 5 (χ(2)=i) | 5 |
| E | 2 | 3 | σ_{χ₋₄}²(m) − 8σ_{χ₋₄}²(m/2) | 8 |
| F | 2 | 3 | σ_{χ₋₃}²(m) − 7σ_{χ₋₃}²(m/2) − 8σ_{χ₋₃}²(m/4) | 12 |
| α | 3 | 4 | σ₃(m) −17σ₃(m/2) −9σ₃(m/3) +16σ₃(m/4) +153σ₃(m/6) −144σ₃(m/12) | 12 |
| γ | 3 | 4 | σ₃(m) −28σ₃(m/2) +63σ₃(m/3) −36σ₃(m/6) | 6 |
| δ | 3 | 4 | σ₃(m) −14σ₃(m/2) −σ₃(m/3) +16σ₃(m/4) +14σ₃(m/6) −16σ₃(m/12) | 12 |
| ε | 3 | 4 | σ₃(m) −21σ₃(m/2) +84σ₃(m/4) −64σ₃(m/8) | 8 |
| ζ | 3 | 4 | **Σ_{d|m} χ₋₃(d)χ₋₃(m/d)d³** (the (χ₋₃,χ₋₃) Eisenstein, coefficient exactly 1) | 9 |
| η | 3 | 4 | σ_{χ₅}³(m) − 14σ_{χ₅}³(m/2) − 16σ_{χ₅}³(m/4) | 20 |

(σ(m/k) := 0 unless k | m.  E4-combination coefficients are ×240 of the
raw fit; the constant terms cancel identically in every family, as they
must — Φ = q + O(q²).)

Notes:
* γ recovers Beukers's classical weight-4 level-6 Eisenstein for Apéry ζ(3);
  D recovers the Γ₁(5) weight-3 picture for ζ(2) — both arrived here from
  the recurrence alone, which is the control confirming the method.
* ζ's source is the single cleanest object in the table: the primitive
  (χ₋₃,χ₋₃)-Eisenstein series of weight 4 on level 9 with coefficient **1**.
* The cusp bases offered (5.4 = η₁⁴η₅⁴, 6.4 = (η₁η₂η₃η₆)², 8.4 = (η₂η₄)⁴,
  9.4 = η₃⁸ and embeddings) were never taken by any fit.
* **Cooper's three (s₇, s₁₀, s₁₈): no fit** at weight 3 or weight 4 with
  levels {7,10,18}·divisors and the natural characters (χ₋₇, mod-5 pair,
  χ₋₃) `[EXCLUDED in this basis; OPEN]` — exactly the three families whose
  t, F were already aperiodic in the canonical nome (eps51).  Their Φ *is*
  integral (μ=1).  The obstruction is the coordinate (Atkin–Lehner
  normalization), not integrality.

## 3. The Apéry limits are Eichler connection values `[VERIFIED numeric]`

At the dominant singularity t_c of P(t) = 1 − at + ct² (R2) resp.
1 − 2at + ct² (R3), the nome map folds (dt/dq = 0 at q_c), so the singular
part of any solution is its odd part in (q − q_c), giving the **connection
formula**

\[ ξ = \lim_n B_n/A_n = \frac{y_B'(q_c)}{y_0'(q_c)}
     = Θ(q_c) + \frac{F(q_c)\,Θ'(q_c)}{F'(q_c)}, \qquad
   Θ = θ_q^{-r}Φ = Σ c(m)m^{-r}q^m . \]

(The lemma "ξ = ratio of q-derivatives at the fold" is a half-page proof
from the local square-root structure; recorded here as provable, used
numerically below.)

With c(m) from §2 (available for ALL m — the point of the identification)
and q_c solved from the exact series (error tracked as |q_c|^N):

| fam | known limit | ξ (computed from Φ alone) − known |
|---|---|---|
| γ | ζ(3)/6 | 6.6e−15 |
| ε | 7ζ(3)/32 | 8.8e−13 |
| α | 7ζ(3)/24 | 8.3e−8 |
| D | ζ(2)/5 | 3.7e−7 |
| ζ | L(χ₋₃,3)/3 | 4.7e−4 * |
| A | ζ(2)/4 | 4.4e−3 * |
| C | L(χ₋₃,2)/2 | 4.4e−3 * |
| E | G/2 | 5.8e−3 * |
| F | 5L(χ₋₃,2)/8 | 3.6e−2 * |

(*) larger q_c: error consistent with the N=26 series truncation |q_c|^26
in q_c and F; the four sharp cases are the strong test.  **All nine limit
families reproduce their limits from the identified Eisenstein source** —
Sol's step 4 (limit = modular-transformation data of the source) holds
numerically across the board.

## 4. The three "no-limit" families have complex Eichler limits `[computed; recognition OPEN]`

B, δ, η are exactly the families whose P(t) has complex-conjugate roots
(disc −27, −128, −16 → CM-adjacent fields ℚ(√−3), ℚ(√−2), ℚ(i)) — this,
not any failure of the theory, is why the classical table says "no limit":
B_n/A_n oscillates.  The connection value at the complex singularity is
still canonical.  At series order N=60 (dps 80):

* ξ_δ = 0.289384069279185217328721946648602157671732873
       − 0.382793539263049809183571589860583184140094533 i  (err ≤ 3e−39)
* ξ_η = 0.427412384177931213153568843953539910126963519
       − 0.221862855742218924237675923183991402052217749 i  (err ≤ 2e−33)
* ξ_B = 0.39151062416206523 − 0.42193463325508115 i  (err ≤ 8e−15;
       |q_c| ≈ 0.58 makes B the hard one)

PSLQ over {1, ζ(3), π³, π³/√2, π³/√5, L(χ₋₈,3), L(χ₋₄,3), L(χ₅,3),
π²log2, ...} and CM-field-twisted variants (√2·Re ξ etc.): **no relation**
(all hits were spurious/degenerate — note L(χ₋₄,3) = π³/32 must be excluded
from any basis).  These are, to current knowledge, new constants: Eichler
values of explicit Eisenstein series at complex multiplication-adjacent
points.  Plausible home: periods of Hecke characters / CM Γ-values
(Chowla–Selberg territory), not Dirichlet L-values.  Sharpest open form:

> **(Φ-1)** Recognize ξ_δ (39 digits above) in closed form.  The source is
> the explicit level-12 weight-4 Eisenstein combination of §2; q_c is the
> nome of the fold over t_c = (7−√−32)/81.

## 5. What this changes structurally

1. **The sporadic class is Eisenstein-sourced.**  Combined with the proved
   Sym²/rectification theorems (modular_anchors paper), the full chain
   recurrence → operator → (t,F) → Φ → limit is now explicit and
   Eisenstein at every link for 12/15 families.  Promotion of §2 from
   [VERIFIED q^60] to [THM] is per-family finite bookkeeping: the (t,F)
   eta identifications (eps51) + Sturm bounds in M_{r+1}(Γ₀(N), χ) — same
   route as the proved ζ identity.  No new mathematics is needed; this is
   the natural next campaign.
2. **Sol's reverse factory has a sharp target.**  New (elliptic-curve)
   Apéry limits require cuspidal Φ.  The construction direction: choose a
   level with S_{r+1} ≠ 0, build B = F θ^{-r}(cusp form), and derive the
   recurrence — the integrality/denominator behaviour of THAT object is
   the discriminating question, and the present ledger says the sporadic
   table will not answer it (they are all Eisenstein).
3. **The "no-limit" column is a CM phenomenon** (complex fold), and it
   produces concrete new constants (§4).
4. Denominator predictions from Bernoulli/Eisenstein constants (Sol step 4
   of the flagship, cf. `DENOMINATOR_HARVEST.md`) can now be attempted
   against the explicit c(m) laws: v_p(den B_n) should be readable from
   the p-parts of c(m)/m^r.  Not attempted this session.

## 6. Honest limits

Identifications are coefficientwise (q^60, zero-tail beyond the found fit)
— not proofs; the modular bookkeeping (weight/level/character of each
divisor-sum combination, Sturm bound) is routine and NOT done here.  The
connection lemma is used at numeric grade; its half-page proof is sketched,
not written.  The limit checks are floating-point with tracked truncation,
not exact.  Cooper's three are excluded only in the stated bases/coordinate.
PSLQ negatives in §4 are bounded by maxcoeff 10^6–10^7 and the listed bases.
