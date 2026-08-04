# SPORADIC_MODULAR_DICTIONARY — the fifteen pairs, their parametrizations, and the ASD sweep

**Fork deliverable, 2026-08-04.**  Scripts: `work/z5eps/eps51_dictionary.py`,
`eps51_refine.py` (+ `eps51_results.json`, `eps51_refined.pkl`), reusing the
eps48 nome instrument (read-only).  All arithmetic exact (`Fraction`), series
order `q^26`; identifications are coefficientwise **to `q^25`** with verified
zero tails; the ASD sweep uses `p = 5,7,11,13,17,19,23`.  Labels per
programme convention; nothing below is claimed beyond its label.

Notation: `η_m = q^{m/24}∏(1−q^{mk})`; `t(q)` the nome-inverse hauptmodul,
`F(q) = y₀(t(q))` the parametrizing form; `b_p = [q^p]F`; `A(p)` the p-th
sequence value.  Modular weight of `F` is `Σe_m/2` (1 for the R2 six, 2 for
the rest); the table's congruence weight `w` is modular weight + 1.

## 1. Master table `[VERIFIED: exact ℚ, q^25, zero-tail-checked]`

| # | fam | w | χ | limit | t(q) integral? | t(q) identification | F(q) identification |
|---|---|---|---|---|---|---|---|
| 1 | **A** (Franel) | 2 | 1 | ζ2/4 | yes (μ=1) | `q·η₁³η₆⁹/(η₂³η₃⁹)` (lvl 6) | `η₂η₃⁶/(η₁²η₆³)`, wt 1 |
| 2 | **B** | 2 | χ₋₃ | none | yes | `q·∏(1−q^{mk})^{e}`, e = {1:3, 2:−9, 4:3, 9:−3, 18:9} (lvl 36; NB `Σm·e_m = 132 ∉ 24ℤ`, so as an eta quotient it carries a half-integral q-shift — the sign-twist `b(−q)` phenomenon of the eps49 identification) | `η₂⁹η₃η₁₂/(η₁³η₄³η₆³)`, wt 1 |
| 3 | **C** | 2 | χ₋₃ | L(χ₋₃,2)/2 | yes | `q·η₁⁴η₆⁸/(η₂⁸η₃⁴)` (lvl 6) | `η₂⁶η₃/(η₁³η₆²)`, wt 1 |
| 4 | **D** | 2 | 1 | ζ2/5 | yes | generalized eta, `c_j` ≡ `[5,−5,−5,5,0]` mod 5 (Γ₁(5); the classical ζ(2)-Apéry parametrization) | gen-eta `c_j ≡ [−3,2,2,−3,2]` mod 5, wt 1 |
| 5 | **E** | 2 | χ₋₄ | G/2 | yes | `q·η₁⁴η₄²η₈⁴/η₂¹⁰` (lvl 8) | `η₂¹⁰/(η₁⁴η₄⁴)`, wt 1 |
| 6 | **F** | 2 | χ₋₃ | 5L(χ₋₃,2)/8 | yes | `q·η₁⁵η₃η₄⁵η₆²η₁₂/η₂¹⁴` (lvl 12) | `η₂¹⁵η₃²η₁₂²/(η₁⁶η₄⁶η₆⁵)`, wt 1 |
| 7 | α (Domb) | 3 | 1 | 7ζ3/24 | yes | `q·(η₁η₃η₄η₁₂)⁶/(η₂η₆)¹²` (lvl 12) | `(η₂η₆)¹⁰/(η₁η₃η₄η₁₂)⁴`, wt 2 |
| 8 | γ (Apéry ζ3) | 3 | 1 | ζ3/6 | yes | `q·(η₁η₆/η₂η₃)¹²` (lvl 6; control, matches classical exactly) | `(η₂η₃)⁷/(η₁η₆)⁵`, wt 2 |
| 9 | **δ** | 3 | 1 | none | yes | `q·η₁⁴η₄⁴η₆¹⁶/(η₂¹⁶η₃⁴η₁₂⁴)` (lvl 12) | `η₂¹²η₃η₁₂/(η₁³η₄³η₆⁴)`, wt 2 |
| 10 | ε | 3 | 1 | 7ζ3/32 | yes | `q·(η₁η₈)⁸/(η₂η₄)⁸` (lvl 8) | `(η₂η₄)⁶/(η₁η₈)⁴`, wt 2 |
| 11 | **ζ** | 3 | χ₋₃ | L(χ₋₃,3)/3 | yes | `q·(η₁η₉)⁶/η₃¹²` (lvl 9) | `η₃¹⁰/(η₁η₉)³`, wt 2 (= the Γ₀(9) Eisenstein `(9E₂(q⁹)−E₂(q))/8`, consistent with the eps48/eps49 identification) |
| 12 | **η** | 3 | χ₅ | none | yes | `q·η₁⁶η₄⁶η₁₀¹⁸/(η₂¹⁸η₅⁶η₂₀⁶)` (lvl 20) | `η₂¹⁵η₅η₂₀/(η₁⁵η₄⁵η₁₀³)`, wt 2 |
| 13 | s₇ | 2 | 1 | ζ2/7 | yes | integral, **aperiodic** — not an eta/gen-eta quotient in this coordinate | integral, aperiodic |
| 14 | s₁₀ | 2 | 1 | ζ2/5 | yes | integral, aperiodic | integral, aperiodic |
| 15 | s₁₈ | 2 | χ₋₃ | L(χ₋₃,2)/2 | yes | integral, aperiodic | integral, aperiodic |

Headlines: **all fifteen nomes are integral at scale μ=1**; **twelve of
fifteen are exactly identified** as (generalized-)eta objects with verified
zero tails, including all four previously "conjectural, no formula, no
modular statement" families that the harmonic/deformation instruments could
not touch — **B (lvl 36), δ (lvl 12), ζ (lvl 9), η (lvl 20)**.  δ and η are
identifications we could not locate in the programme's files; B and ζ agree
with (and eta-sharpen) the eps48/eps49 identifications.  Cooper's three
(s₇, s₁₀, s₁₈) are integral but not eta-type in this coordinate — their
parametrizations presumably need an Atkin–Lehner/other hauptmodul
normalization; recorded honestly as unidentified.

## 2. ASD sweep `[VERIFIED: p = 5..23, exact]`

**Weight-2 families (all nine: α, γ, δ, ε, ζ, η, s₇, s₁₀, s₁₈):**
\[  A(p) \equiv b_p \pmod p \qquad\text{at every tested prime.}  \]
The classical Beukers/ASD congruence holds uniformly — including the three
unidentified Cooper families (whose `F` is known only as a q-series) and the
χ-twisted ζ, η.

**Weight-1 families (the R2 six): a new uniform twisted law.**  The naive
congruence fails, but the defect is exactly structured
`[VERIFIED: 7 primes each]`:
\[
A(p)\;\equiv\;b_p\;-\;b\cdot\chi_N(p)\pmod p
\qquad\text{for } \mathbf A,\mathbf B,\mathbf C,\mathbf E,\mathbf F,
\]
where `b` is the recurrence's constant parameter (2, 3, 3, 4, 6
respectively) and `χ_N` is the quadratic character attached to the
**level** (χ₋₃ for levels 6, 12, 36; χ₋₄ for level 8) — note for Franel
(family χ = 1!) the correction is nonetheless χ₋₃, i.e.\ the level speaks,
not the family character.  For **D** (Γ₁(5), quintic character world) the
defect follows a mod-5 rule: `A(p) − b_p ≡ 2(p mod 5) − 5 (mod p)`
(residues 1,2,3,4 → −3,−1,+1,+3; ≡ 0 at p ≡ 0).  These weight-1 laws
appear to be new; they are conjecture-grade (7 primes) and should be
provable from the weight-1 Eisenstein structure of the identified forms.

## 3. Correlation: what predicts jet-reachability?

Data available (eps43): reachable = {A(Franel), D}; unreachable = {B, δ, ζ}.
Character+limit predicted the split but called δ (χ=1) an edge case.  The
modular table suggests a cleaner discriminant:

* reachable: levels **5, 6** (squarefree);
* unreachable: levels **36, 12, 9** (non-squarefree).

**Discriminating experiment (proposed, not run):** family α (Domb) has
principal character *and* a real limit (character+limit ⇒ reachable) but
level 12, non-squarefree (level criterion ⇒ unreachable).  Running the
eps43 scan on α decides between the hypotheses.  Same for ε (level 8).

## 4. Provable-next targets (ranked)

1. **ζ's ASD congruence + twisted Lucas.**  `F_ζ = η₃¹⁰/(η₁η₉)³` is an
   explicit Eisenstein eta-quotient; `A(p) ≡ b_p` (9 primes-worth of data
   across the sweep) with the χ₋₃ nebentypus matching the twisted Lucas
   law's character.  A classical proof (Eisenstein coefficients =
   twisted divisor sums + Dwork unit root for the level-9 family) looks
   writable, and would be the first proved instance of the sporadics
   paper's (LD)/P2–P3 circle with χ ≠ 1.
2. **δ's parametrization as a theorem.**  Both `t_δ` and `F_δ` are explicit
   level-12 eta quotients; proving `F_δ = y₀(t_δ)` is a finite check
   (both sides satisfy the same order-3 ODE, standard once the quotients'
   modularity/weight is certified) — this would move δ out of
   ``conjectural'' for the first time, and δ is one of the two no-limit
   families.
3. **The weight-1 twisted ASD laws.**  `A(p) ≡ b_p − b·χ_N(p)` across five
   families with identified weight-1 forms: uniform, elementary-looking,
   and directly relevant to family B (the remaining no-formula, no-limit
   R2 case) whose companion hunt can now use the corrected congruence as a
   constraint.

## 5. Honest limits

Series order q^26 (identifications to q^25); ASD to p = 23; no all-n or
all-p claims anywhere; Cooper's three unidentified in this coordinate;
the eta identifications certify the q-expansions match — the statement
"t, F are modular of the stated level/weight" additionally needs the
standard eta-quotient weight/level/character bookkeeping (routine, not
done here); the correlation in §3 rests on two reachable + three
unreachable data points and one proposed discriminating experiment.
