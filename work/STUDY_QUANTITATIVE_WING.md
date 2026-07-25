# Study memo — the quantitative wing of odd-zeta irrationality

**Author:** mathematician-agent (River's zeta-irrationality program)
**Date:** 2026-07-24
**Scope:** Primary reads — `llm/13` (Lai–Zhou 2021), `llm/16` (Lai 2024), `llm/17` (Lai 2025), `llm/14` (Fischler 2021). Context — `llm/10` (FSZ 2018), `llm/12` (Lai–Yu 2019).
**Discipline labels:** `[PROVED]` complete proof in paper; `[CLAIM]` asserted, computer-checked, not refereed; `[CONJ]` conjecture; `[VERIFIED]` I re-checked a finite computation; `[RECALLED-UNVERIFIED]` from memory, not in files. Quotes carry in-paper numbering. Equations trusted over prose.

All four primary papers share one machinery: build a rational function `R_n(t)` (a product of Pochhammer "bricks"), read off its partial-fraction coefficients `a_{i,k}`, sum shifted copies `S_{n,θ}=Σ R_n(t+θ)` to get **linear forms in 1 and odd Hurwitz/zeta values**, bound their denominators (with an arithmetic **Φ_n** saving), estimate their size by Stirling/saddle, then feed to a **linear-independence criterion** (Nesterenko) or an **elimination + "small nonzero integer → 0"** contradiction. The differences are which criterion, which elimination trick, and how the bricks are tuned.

---

## Paper 13 — Lai–Zhou, "At least two of ζ(5),ζ(7),…,ζ(35) are irrational" (arXiv 2103.00904)

### Main theorems (verbatim)
- **Theorem 2.** *"At least two of ζ(5),ζ(7),…,ζ(35) are irrational."* `[PROVED]` Improves Rivoal–Zudilin's window 69 → 35.
- **Theorem 1** (quoted, Zudilin). *"At least one of ζ(5),ζ(7),ζ(9),ζ(11) is irrational."*
- **Theorem 11.** *"At least one of β(2),β(4),β(6),β(8),β(10) is irrational"* (Catalan β=L(·,χ₄)); improves Zudilin's 12 → 10. `[PROVED]`

### Construction skeleton
- Rational function `R_n(t)` (eq. `R_n(t)`), even `n`, built from bricks `G_{1/2},G_{1/3},G_{2/3},G_1^-,G_1^+` and `H_j`, with a `(2t+m_2 n)` well-poised symmetry factor giving `R_n(t) = −R_n(−t−m_2 n)`, hence `a_{i,k}=(−1)^{i+1}a_{i,m_2 n−k}` — this kills even zeta values.
- **Elimination = "inserting rational roots"** (θ ∈ 𝒵={1,½,⅓,⅔}), i.e. the Zudilin/Sprang trick used *purely* (not the "twice-derivatives" trick). `Ŝ_{n,b}=Σ_{k=1}^b S_{n,k/b}=b^i·ζ(i)` combos for b∈{1,2,3}; a 3×3 generalized Vandermonde over rows {1,i₁,i₂} lets one eliminate the two hypothetically-irrational values ζ(i₁=3), ζ(i₂∈{5,7,9,11}), leaving a contradiction if a third irrational does not exist.
- **Arithmetic** (Lemma 4/5): `Φ_n^{-1} D_{(m_2−2δ_min)n}^{s+1−i} a_{i,k} ∈ ℤ`, with `Φ_n = ∏_{√(3(2m₁+m₂)n)<p≤(m₂−2δ_min)n} p^{ν₀(n/p)}` and `ν₀(x)=min_y ν(x,y)` a floor-sum.
- **Criterion:** none needed — it is the "sequence of nonzero integers tending to 0" contradiction, driven by `C₁>C₂` (`C₁=lim log Φ_n /n`, `C₂` the size exponent).

### Tunable parameters — hand-chosen vs optimized
- `s=35`; `m₁=209, m₂=243`; δ-staircase δ_j=4 (j≤5), j−1 (6≤j≤11), 2j−12 (12≤j≤32), 4j−76 (33≤j≤36).
- **Explicitly non-optimal / hand-tuned:** *"The above parameters are found by random search and trial-and-error."* Result: `x₀=2.89493833…`, **C₁=16779.9312… > C₂=16779.2826…** — margin ≈ **0.649 out of ~16 780**. `[VERIFIED]` the δ-list is length 36 = s+1, Σδ_j=985 < ((s−2)m₂−8m₁)/2=3173.5, max δ=68 < m₂/2=121.5 (all constraints hold).
- **Remark 8:** *"If one elaborates the method in [RZ20], some first attempts suggest that one cannot obtain a result better than Theorem 2. However, we did not put our effort on figuring it out."*
- **Remark 9:** *"It is possible that the arithmetic behavior of ρ_i and ρ_{0,θ} is even better, by considering certain hypergeometric transformations… the 'denominator conjecture'… It is tremendously difficult to put such things into consideration in this paper."*
- **Remark 10:** the denominator normalization `n!^{8m₁+3m₂}` is non-unique; brick-splitting (`u₁,…,u_I`) leaves Theorem 2 unchanged (−C₁+C₂ invariant).
- **Theorem 11 (Catalan):** *"we are greatly indebted to one of the referees for providing better parameters for Theorem 11"* — parameters (η₀,…,η₁₁)=(94,32,32,32,32,33,34,35,36,37,38,39); r̃_n^{1/n}=e^{118.624566}, (Φ̃_n^{-1}d^{11})^{1/n}=e^{−118.836817} (margin ≈ 0.212).

### What a CA effort can do
- Independently recompute `C₁, C₂, x₀` (the paper used MATLAB `zeta35.m`; C₁ is a finite sum over discontinuities of the 1-periodic piecewise-constant `ν₀`; §"Computational Aspect" gives the exact algorithm and the H×3 matrix `h`). Confirm the 0.649 margin.
- Search for parameters lowering the window 35, or confirm Remark 8's suspicion that ~35 is the wall for the pure-rational-roots method.

---

## Paper 16 — Lai, "Small improvements on the Ball–Rivoal theorem and its p-adic variant" (arXiv 2407.14236)

### Main results (verbatim)
- **Theorem 1.** *"dim_ℚ Span_ℚ(1,ζ(3),ζ(5),…,ζ(s−1)) ≥ (1.009/(1+log2))·log s"* for large even s. `[PROVED]` (programming-free).
- **Theorem 2.** same bound `(1.009/(1+log2))·log s` for the **p-adic** span `1,ζ_p(3),…,ζ_p(s−1)`, any prime p. `[PROVED]`, **new** (refines Sprang 2020, which had a spurious ½).
- **Claim 3.** both classical and p-adic bounds improve to `(1.119356/(1+log2))·log s`. `[CLAIM]` (computer, unrefereed).
- **Claim 4.** *"dim_ℚ Span_ℚ(1,ζ(3),ζ(5),…,ζ(75)) ≥ 3"*, i.e. κ₃ ≤ 75 (was 139, Fischler–Zudilin). `[CLAIM]`.
- Framing: *"it was expected that Zudilin's Φ_n factor would have a negligible impact on asymptotic results as s→∞. The aim of the current paper is to demonstrate that this previous expectation is inaccurate."*

### Construction skeleton
- `R_n(t)= (∏((M−2δ_j)n)!^{s/J}/n!^{2r})·(2t+Mn)·(t−rn)_{rn}(t+Mn+1)_{rn} / ∏(t+δ_j n)_{(M−2δ_j)n+1}^{s/J}`, r=⌊s/log²s⌋ (Ball–Rivoal numerator length). Two brick types: "denominator bricks" `G_j` (Lemma 9) give Φ_n; "numerator bricks" `F` (Lemma 10, the `μ_m(b)=b^m∏p^{⌊m/(p−1)⌋}` normalization) stay integral.
- Φ_n from Lemma 11: `Φ_n=∏_{√(Mn)<q≤(M−2δ₁)n} q^{φ(n/q)}`, `φ(x)=inf_y Σ_j(⌊(M−2δ_j)x⌋−⌊y−δ_jx⌋−⌊(M−δ_j)x−y⌋)`.
- Size: `S_n=exp(−α(s)n+o(n))`, `α(s)∼(s log s/J)Σ(M−2δ_j)`; coeffs `≤exp(β(s)n)`, `β(s)∼log2·(s/J)Σ(M−2δ_j)`; `Φ_n=exp(ϖn+o(n))`.
- **Criterion:** Nesterenko (Theorem 5); dim ≥ 1+α̂/β̂ with `α̂=α+ (s/J)ϖ − (s/J)Σ max{M−2δ₁,M−δ_j}`, `β̂=β − (s/J)ϖ + …`. p-adic case uses Nesterenko's p-adic criterion (Theorem 7) with Volkenborn integrals / first Bernoulli functional 𝓛₁.

### Tunable parameters — hand vs optimized
- **Theorem 1/2 (hand-picked, simple):** M=6, (δ₁,δ₂)=(0,1), J=2 ⇒ ϖ=ψ(1/5)−ψ(1/6)+ψ(2/5)−ψ(1/3)+ψ(3/5)−ψ(1/2)+ψ(4/5)−ψ(3/4)=2.157479…, C=10/(10log2−ϖ+12)=1.009388…/(1+log2). Baseline M=1,δ=0 reproduces Ball–Rivoal.
- Other simple parameters listed: (M=19,δ=(0,1,2)) C=1.036; (M=12,(0,0,1,2)) 1.050; (M=16,(0,0,1,2,3)) 1.063; (M=37,δ=2..11, "Zudilin's ζ(5)..ζ(11)" params) 1.026/1.034.
- **Remark 36:** always take δ₁=0 (shift symmetry ⇒ C=C′≥C).
- **Explicit non-optimality:** *"Since the dependence of ϖ … on the parameters is discrete, it is unlikely to find an optimal constant C."* Claim 3 params: *"After an extensive random search in the range M≤600, δ_j≤200, J≤100, we have found a better C=C′ ≈ 1.119/(1+log2)."* M=433, J=89, δ-table (mostly 0's then odd staircase), ϖ=12557.653439….
- **Claim 4 (razor-thin):** r=2444, M=444, 76 δ's (1,1,1,1,1,2,2,3,3,4,…,124), uses Fischler–Zudilin criterion (Theorem 6) with divisor `d_{n,i}=D_{443n}^3` (γ₁=443·3). Yields `1 + (…)/(…) = 2.006260…` ⇒ dim ≥ 3. Numeric inputs: ϖ̃=42945.452053, α̃=38489.009014, β̃=58209.043057, x₀=0.194387.

### CA opportunities
- **Recompute Claim 4's 2.006260** exactly — the margin above 2 is **0.006**; a δ-table transcription slip or digamma-integral rounding could flip it. Check the Theorem 6 divisibility hypotheses for `d_{n,i}=D_{443n}^3`.
- Re-run the Claim 3 search (M≤600,δ_j≤200,J≤100) to confirm 1.119356 and probe whether a wider net beats it.
- Small-n exact check of Lemmas 11–12 (see Task D).

---

## Paper 17 — Lai, "A note on the number of irrational odd zeta values, II" (arXiv 2501.05321)

### Main theorem (verbatim)
- **Theorem 1.** *"For any sufficiently large positive integer s, #{odd i∈[3,s] | ζ(i)∉ℚ} ≥ 1.284579·√(s/log s)."* `[PROVED]` (proof restricts to even s; count monotone absorbs it). Improves Lai–Yu's 1.192507 by a constant factor. **This is the current record for the irrational-count.**

### Construction skeleton
- Combines **FSZ elimination** (rational zeros θ∈𝒵_B, `𝒵_B` = fractions with φ(den)≤B; `Ψ_B={b:φ(b)≤B}`, `|Ψ_B|∼(ζ(2)ζ(3)/ζ(6))B`) **with Zudilin's Φ_n** (the δ_j staircase, M>1). `R_n(t)` (Definition 3) carries `A_1(B)^n A_2(B)^n` totient-normalization factors, numerator `(t−rMn)_{rMn}(t+Mn+1)_{rMn}∏_{θ∈𝒵_B∖{1}}(t−rMn+θ)_{(2r+1)Mn}`, denominator `∏(t+δ_j n)_{(M−2δ_j)n+1}^{s/J}`.
- Arithmetic (Lemma 9): `Φ_n^{−s/J} D_{(M−2δ₁)n}^{s−i} a_{n,i,k}∈ℤ`, `Φ_n=∏_{√(Mn)<p≤(M−2δ₁)n} p^{ω(n/p)}`, `ω(x)=min_y Σ_j(⌊(M−2δ_j)x⌋−⌊y−δ_jx⌋−⌊(M−δ_j)x−y⌋)`.
- **Elimination (Lemma 15):** generalized Vandermonde `[b^i]_{b∈Ψ_B, i∈{0,1}∪I}` invertible ⇒ eliminate `|Ψ_B|−2` values ⇒ ≥ `|Ψ_B|−1` irrationals if the size condition (`we_need`) `log g(x₀)+s(−ϖ/J+(M−2δ₁))<0` holds.
- **Theorem 16** reduces everything to a finite computation of `ϖ`, `r₀` (a 1-D root of G(r)=0), and closed-form `C₀=√((2ζ(2)ζ(3)/ζ(6))·(1/J)Σ log[((r₀+1)M−δ_j)/(r₀M+δ_j)])`.

### Tunable parameters — hand vs optimized
- **Progression of examples:** M=1,J=1,δ=0 → ϖ=0, r₀=2.263884, C₀=1.192507 (**recovers Lai–Yu**) `[VERIFIED]` r₀=(√(4e²+1)−1)/2=2.263884, C₀=1.192508 reproduced; M=7,J=2,δ=(0,1) → 1.197980; M=57,J=18 → 1.262672; **M=563,J=76,δ-table → ϖ=12694.987927, r₀=1.502726, C₀=1.284579** (Theorem 1).
- **Remark 17:** *"The same δ_j's in Table 1 were used in [Lai2024+]. But the parameter M=563 in this note is different… if we fix J=76 and these δ_j's… and let M vary from 500 to 600, then M=563 gives the best C₀."* — i.e. only a 1-D slice of the parameter space was optimized; J and the δ-pattern are inherited from paper 16, not re-optimized here.

### CA opportunities
- Re-run Theorem 16's evaluation for the M=563 table (verify 1.284579); then a genuine **joint** search over (M, J, δ-staircase) — each evaluation is cheap (piecewise-constant ϖ integral + 1-D root + closed form). Likely pushes the constant slightly above 1.2846.
- The real ceiling is the "denominator conjecture" arithmetic (Lai–Zhou Remark 9), out of reach.

---

## Paper 14 — Fischler, "Linear independence of odd zeta values using Siegel's lemma" (arXiv 2109.10136)

### Main theorems (verbatim)
- **Theorem 1.** *"For any sufficiently large odd integer s: dim_ℚ Span_ℚ(1,ζ(3),ζ(5),…,ζ(s)) ≥ 0.21·√s/√log s."* `[PROVED]` **First asymptotic improvement over Ball–Rivoal's log s for linear independence.**
- Immediately after: *"Here 0.21 is the rounded value of a real number that we did not try to compute exactly."*
- **Theorem 2** (polylogs). for large s and z∈ℚ̄, |z|≤1, z∉{0,1}: `dim_{ℚ(z)} Span(1,Li₁(z),…,Li_s(z)) ≥ (0.26/[ℚ(z):ℚ])·√s/√log s`. `[PROVED]`
- **Remark 5:** for z∉ℝ the constant 0.26 may be replaced by **0.52**.

### Construction skeleton — the conceptual break
- **No explicit hypergeometric series.** Instead `F_n(X)=Σ_{i=1}^a Σ_{j=0}^n c_{i,j}/(X+j)^i` with the integers `c_{i,j}` produced *non-explicitly* by **Siegel's lemma** (Lemma 1, a version mixing equalities and inequalities). Only property used: `F_n(t)=O(t^{−ωn})`.
- Non-explicit ⇒ can't lower-bound the linear form for Nesterenko. Two replacement tools:
  - **Refined Siegel linear-independence criterion (Proposition 1):** needs only that the first column of the coefficient matrix is *not* a combination of the others (i.e. no common zero with x₀≠0), weaker than full-rank; conclusion `dim ≥ ([ℚ_∞:ℝ]/[ℚ:ℚ])(τ+1)`.
  - **Multiplicity estimate / generalized Shidlovsky (Theorem 3, from [SFcaract]):** supplies enough linearly-independent forms via derivations in t and z at z=−1 (using Li_i(−1)=(2^{1−i}−1)ζ(i)).
- Asymptotics (opposite regime from Ball–Rivoal): `log α ∼ −4.55√(s log s)`, `log β ∼ 20.93 log s` (Remark 3) — coefficients far smaller than explicit constructions.

### Tunable parameters — hand vs optimized
- Parameters a,r,κ,ω,Ω,h with n→∞. **§4.6 final choice:** *"we choose r=3.9, κ=10.58, ω=12, Ω=⌊r√(a log a)⌋, and h=0.36 a … all numerical constants are rounded with precision 0.01."* Constraint `(h+1)(κ−2r)+ω>a` and κ>2r.
- Final constant computed as `(2r log r)/(r² log r + 2κ)·1/√(1+h/a) = 0.2174… > 0.21`. `[VERIFIED]` = 0.21746 with those numbers.
- **Non-optimality admitted twice:** Theorem 1's *"real number that we did not try to compute exactly"*; and §4.6 *"the numerical constant 0.21 can be replaced … by a slightly larger real number."*
- **Theorem 2 params:** r=5.3, κ=8.8343, ω=10, Ω=⌊3.3√(a log a)⌋, h=0.3946a; log α₁∼−5.5034√(a log a) ⇒ 0.26.
- **Remark 1 / Remark 2:** the multiplicity estimate is genuinely *weaker* than usual (can't rule out a hidden linear relation `Σ Q_i^{[0]}(z)(λ−log z)^{i−1}/(i−1)! = O((z+1)^{κn})`); the constraint `(h+1)(κ−2r)+ω>a` is *necessary* — if reversed, the approach "cannot even exclude" all Li_i(−1)∈ℚ. This is the structural bottleneck.
- **Remark 4:** an explicit s₀ is effectively computable (but not given).

### CA opportunities
- Compute the exact real constant behind "0.21" and optimize (see Task A). **Important honest finding:** `[VERIFIED]` maximizing the paper's *reduced* ratio `(2r log r)/(r²log r+2κ)/√(1+h/a)` under the binding constraint κ=2r+1/(h/a) gives only **0.21749** (at r≈3.93, κ≈10.66, h/a≈0.358) — i.e. the paper's own parameters are already within 0.00003 of optimal *for that formula*. Real headroom, if any, lives in re-deriving α,β from §4.6 (where ω, Ω enter) rather than in the reduced ratio.

---

## Context — papers 10 and 12

- **FSZ 2018 (paper 10), Theorem 2:** *"among ζ(3),…,ζ(s), at least 2^{(1−ε) log s/log log s} are irrational."* `[PROVED]` Elimination via **divisors of a primorial D** (D=∏_{p≤(1−2ε)log s} p, δ=2^{π(...)} divisors) and the **generalized Vandermonde positivity** (Lemma 4, three proofs: Schur/Fekete/Rolle). **Remark 1:** adding a Ball–Rivoal r-parameter *"does not bring any improvement."* **Remark 2 & §"negligible":** the known Φ_n has, in their setting, no asymptotic effect.
- **Lai–Yu 2019 (paper 12), Theorem 1:** ≥ `(c₀−ε)√(s/log s)` irrationals, `c₀=√(4ζ(2)ζ(3)/ζ(6)·(1−log r₀))=1.192507`, r₀=(√(4e²+1)−1)/2. New ingredient: **inverse-totient design** of the rational zeros (θ with φ(den)≤B). §6 asserts (following FSZ Remark 2) that *"the known types of Φ_n factors have no effect on asymptotics"* and gives an explicit weak version: ≥ (1/10)√(s/log s) for s ≥ 10⁴.

---

# SYNTHESIS

## (a) The current quantitative frontier — records and their units

The four quantities are **not** comparable; each record is measured differently.

| Quantity (unit) | Record | Source | Note |
|---|---|---|---|
| **Irrational-count**, large s: #{irrational odd ζ(i), i≤s} | **≥ 1.284579 √(s/log s)** | **Lai 2025 (17), Thm 1** `[PROVED]` | beats Lai–Yu 1.192507; count only, no independence |
| **Linear-independence dimension**, large s: dim Span(1,ζ(3),…,ζ(s)) | **≥ 0.21 √(s/log s)** (exact const ≈0.2175) | **Fischler 2021 (14), Thm 1** `[PROVED]` | first sub-poly→√ jump; constant admittedly non-optimal |
| Lin-indep dim, **explicit/constructive** & **p-adic** | ≥ (1.119/(1+log2))·log s ≈ 0.661 log s | Lai 2024 (16), Thm 1/2 + Claim 3 | log s only (weaker order) but explicit small forms; **p-adic bound is new** |
| **Window with ≥ 2 irrationals** containing ζ(5) | **ζ(5),…,ζ(35)** | **Lai–Zhou 2021 (13), Thm 2** `[PROVED]` | improves RZ's 69 |
| Window with ≥ 1 irrational containing ζ(5) | ζ(5),ζ(7),ζ(9),ζ(11) | Zudilin 2001 `[RECALLED-UNVERIFIED as not in primary set; quoted as Thm 1 of 13]` | narrowest known |
| **κ₃** = least κ with dim{1,ζ(3),…,ζ(κ)}≥3 | **κ₃ ≤ 75** | Lai 2024 (16), **Claim 4** `[CLAIM]` | improves FZ's 139; unrefereed, margin 2.006 |
| Catalan window, ≥1 irrational | β(2),β(4),…,β(10) | Lai–Zhou 2021 (13), Thm 11 `[PROVED]` | improves Zudilin's 12 |
| Super-polynomial count (historical) | ≥ 2^{(1−ε)log s/log log s} | FSZ 2018 (10) `[PROVED]` | superseded in constant by √(s/log s) results |

Headline reading: **count** frontier = 1.2846√(s/log s) (Lai 2025); **linear-independence** frontier = 0.21√(s/log s) (Fischler 2021, non-explicit); best **explicit/constructive & p-adic** = 0.661 log s (Lai 2024); best **ζ(5)-window with two irrationals** = 35 (Lai–Zhou 2021).

## (b) Ranked concrete tasks (finitely checkable or provable)

1. **Verify Lai 2024 Claim 4 (κ₃ ≤ 75) end-to-end.** *Statement:* recompute ϖ̃, α̃, β̃, x₀ for r=2444, M=444, the 76-entry δ-table, and re-evaluate the Fischler–Zudilin bound `1+(α̃−Σmax+ϖ̃+γ₁)/(β̃+Σmax−ϖ̃)=2.006260…`; check the Theorem 6 divisor hypotheses for d_{n,i}=D_{443n}^3. *Why:* it is the record upper bound on κ₃ and is only a `[CLAIM]` (author says it wasn't reasonable to ask a referee to check). *Feasibility:* high — asymptotic constants are numeric integrals/digamma sums + one polynomial root, no big-integer arithmetic. *Failure mode:* the margin above the integer threshold 2 is **0.006**; any transcription slip in the δ-table or rounding in ϖ̃ flips 3→2, and the Theorem 6 chain-divisibility hypotheses are easy to mis-satisfy.

2. **Verify Lai–Zhou 2021 Theorem 2 (window 35) numerically, then probe the wall.** *Statement:* reimplement the §"Computational Aspect" algorithm (piecewise-constant ν₀ from the H×3 matrix, digamma-measure integral) to confirm C₁=16779.9312 > C₂=16779.2826, x₀=2.8949; then parameter-search to test whether 35 can drop. *Why:* record "two irrationals in a ζ(5)-window." *Feasibility:* high — deterministic finite computation, MATLAB reference `zeta35.m` public. *Failure mode:* margin 0.649/16780 is thin (verification is real value); **lowering** 35 likely blocked — Remark 8 already suspects the method caps here, and real gains need the intractable "denominator conjecture" (Remark 9).

3. **Pin down and re-optimize Fischler's constants 0.21 / 0.26 / 0.52.** *Statement:* compute the exact real number behind "0.21" (≈0.2175) and maximize the true asymptotic constant over (r,κ,ω,Ω/√(a log a),h/a) subject to `(h+1)(κ−2r)+ω>a`, κ>2r — **re-deriving α,β from §4.6**, not just the reduced ratio. Same for Theorem 2's 0.26 and the z∉ℝ value 0.52. *Why:* these are the current linear-independence-record constants and the author explicitly invites the computation. *Feasibility:* high (smooth low-dim optimization). *Failure mode:* **honest ceiling** — `[VERIFIED]` the paper's *reduced* ratio is already within 3×10⁻⁵ of its own constrained optimum (0.21749), so unless the full α,β carry extra freedom in ω,Ω, the gain is cosmetic (0.21 → ~0.2175). Does **not** improve the √(s/log s) order.

4. **Small-n exact validation of the load-bearing arithmetic lemmas.** *Statement:* for small odd s and even n>s² (e.g. s=5, n=26,28,…), compute the partial-fraction `a_{i,k}` in exact rationals for the R_n of papers 13/16/17 and verify (i) `Φ_n^{−s/J}D^{s−i}a_{i,k}∈ℤ`, (ii) the prime-power exponents of Φ_n equal ν₀/ω/φ(n/p), (iii) the ρ_{0,θ}-denominator lemmas (13 Lemma 5, 17 Lemma 11). *Why:* every asymptotic constant rests on these denominator savings; a clean small-n check is strong evidence the load-bearing lemmas are correctly transcribed in the corpus. *Feasibility:* very high — exact CAS arithmetic, minutes. *Failure mode:* evidence, never proof; must respect n>s² (the lemmas' stated range), so keep s tiny to keep n manageable.

5. **Joint parameter search for the count constant (paper 17) beyond 1.2846.** *Statement:* optimize Theorem 16's C₀ jointly over (M, J, δ-staircase), not just the 1-D M-slice of Remark 17 (which inherited J=76 and the δ-pattern from paper 16). *Why:* current count record; each C₀ evaluation is cheap (piecewise ϖ integral + 1-D root r₀ + closed form). *Feasibility:* medium — large discrete space but fast evaluations; use structured δ-staircases. *Failure mode:* discrete dependence ⇒ likely only marginal gain (Lai already random-searched M≤600 in paper 16); the true barrier (denominator conjecture) is untouched.

6. **Produce explicit, effective versions (compute an s₀).** *Statement:* track the o(1)'s to give an explicit s₀ for Fischler Theorem 1's 0.21 bound (Remark 4 says it's computable but omits it), and/or an explicit-constant intermediate for Lai 2025's 1.2846 (cf. Lai–Yu's explicit (1/10)√(s/log s) for s≥10⁴). *Why:* converts asymptotic statements into finitely-checkable ones. *Feasibility:* medium (bookkeeping). *Failure mode:* labor-heavy; the resulting s₀ is likely astronomically large and of limited mathematical interest.

## (c) Internal inconsistencies / suspicious claims (read skeptically)

- **Fischler §4.1 sketch vs §4.6 proof — ω differs.** The sketch (before eq. defining α) writes *"r=3.9, κ=10.58, ω=11.58, Ω sufficiently close to 3.9√(a log a), h=0.36 a"*; the actual proof §4.6 writes *"r=3.9, κ=10.58, ω=12, Ω=⌊r√(a log a)⌋, h=0.36 a."* The value of ω changed (11.58 → 12). **Not a proof error** — the final constant depends on ω only through the constraint `(h+1)(κ−2r)+ω>a` and Ω, and both ω satisfy it — but it is a genuine textual inconsistency in a load-bearing parameter list; anyone re-deriving should use the §4.6 values.

- **The "Φ_n is asymptotically negligible" reversal — easy to misread as a contradiction, but isn't.** FSZ 2018 (Remark 2) and Lai–Yu 2019 (§6) both assert the known Φ_n has *no effect on asymptotics*; Lai 2024 opens by declaring that expectation *"inaccurate"* and gains a constant factor from Φ_n. **These are about different objects:** Lai–Yu's Φ̃_n is the gcd of coefficients over √n-scale primes in the *FSZ/rational-zeros* construction (indeed negligible); Lai 2024's Φ_n comes from the *δ_j-staircase denominator bricks with M>1* — a construction FSZ/Lai–Yu did not use. No contradiction, but a subtle reversal that the prose obscures; verify against the eqs (Φ_n definitions differ in both the prime range and the exponent function).

- **Two razor-thin decisive margins.** Lai–Zhou Thm 2: C₁−C₂ = **0.6486** out of 16 780. Lai 2024 Claim 4: the criterion value **2.006260** clears the integer threshold 2 by **0.006**. Both are the kind of number a single δ-table typo or a coarse digamma-integral quadrature would flip; they are the highest-value verification targets, not asserted errors. (Claim 4 is additionally only a `[CLAIM]`.)

- **Admitted hand-tuning, not errors but caveats on "records."** Lai–Zhou's decisive parameters are *"found by random search and trial-and-error"* (Remark: *"we did not put our effort"* on the wall, Remark 8); Theorem 11's parameters were *referee-supplied*; Lai 2024's 1.119 and Lai 2025's 1.2846 come from *"extensive random search"* / a 1-D M-slice (Remark 17). So every headline constant here is a lower bound from a non-exhaustive search — none is claimed optimal, and all are legitimate targets for a stronger CA search.

- **Minor: Lai 2025 Theorem 1 statement vs proof.** Theorem 1 is stated for *"any sufficiently large positive integer s"* but Theorem 16 / the proof only deliver even s (multiples of 2J); the odd-s case rides on monotonicity of the count. Harmless, but the statement is very slightly ahead of what the proof literally gives.

**No outright mathematical error found in papers 13/14/16/17 in this pass.** `[VERIFIED]` sanity checks that did pass: Fischler ratio 0.21746 with the paper's numbers; r₀=2.263884 and c₀=1.192508 (paper 1.192507); Lai–Zhou δ-list length 36, Σδ=985<3173.5, maxδ=68<121.5; Lai 2025's M=1 reduction reproducing Lai–Yu. The δ-tables of Lai 2024 Claim 4 and Lai 2025 Thm 1, and the two decisive margins, were *not* recomputed and remain the priority checks (Tasks 1–2).
