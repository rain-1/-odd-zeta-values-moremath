# STUDY MEMO — The Brown Wing of the Odd-Zeta Irrationality Programme

Scope: extraction + synthesis over Brown 2026 (Mellin/transfinite diameter, `llm/21`),
Brown–Zudilin 2022 (cellular ζ(5), `llm/20`), Brown 2014 "dinner parties" (`llm/19`),
Fischler–Rivoal 2013 (Padé/Vasilyev, `llm/24`), Brown 2026 "nonlinear geometry of MZV"
(`llm/32`), skim of Brown–Schnetz 2024 (`llm/31`).

Discipline notes. All in-paper numbering (Theorem/Criterion/Remark/eq) is quoted as it
appears in the source Markdown; garbled formulas were cross-checked against the LaTeX in
`papers/<n>/`. `[RECALLED-UNVERIFIED]` marks anything asserted from background knowledge
rather than the files. "Sibling session" = the readable repo `/home/ubuntu/fable-episode-2/zeta-math`
(its README/SURVEY were consulted for connection points, not re-derived).

The single most important orientation fact, established up front: **the ζ(5) irrationality
seam is not "prove ζ(5) irrational" — every construction here is blocked by the same
parasitic even period ζ(2). The reachable seams are (i) denominators/arithmetic of the
existing forms and (ii) the transfinite-diameter machinery, both of which are partly
finite computations.**

---

## 1. Brown 2026 — Mellin transforms, transfinite diameter, rational approximations (`llm/21`, arXiv 2604.20741)

### 1.1 What the criterion says, exactly

The object is an **algebraic Mellin integral** on a smooth affine `X/ℚ` of dimension `d`
(§2.1, eq. `Isdefn`):
`I(s₁,…,s_r) = ∫_σ f₁^{s₁}…f_r^{s_r} ω`, with `f=(f₁,…,f_r): X → 𝔸^r`, `ω ∈ Ω^d(X)`, `σ` a
relative `d`-chain with `∂σ ⊂ Y(ℂ)`. At integer arguments `I(n)` is a ℚ-linear form in
finitely many periods `ξ₁,…,ξ_m` of `H^d(X,Y)` (Lemma 6). The **anciliary image variety**
`V_f = ` Zariski closure of `f(X) ⊂ 𝔸^r` (Definition 7) is where all the geometry lives.

The construction (Introduction §1.4, formalized §3):
- pick a free ℤ-module `𝓜 = ⊕ ℤ𝔣_i ⊂ 𝒪(V_f)` of rank `N` (the `𝔣_i` are polynomials in
  the `f_j`);
- form the **symmetric period matrix** `Q^σ_N = (∫_σ 𝔣_i 𝔣_j ω)` (Definition 8), whose
  entries are linear forms in the `ξ_i`;
- under positivity hypotheses (P1) `ω ≥ 0` on `σ`, (P2) `𝔣_i` real on `σ`, (P3) `σ`
  Zariski-dense, `Q^σ_N` is **positive-definite** ⇔ the `𝔣_i` are independent (Lemma 9),
  so `det Q^σ_N > 0`.

The load-bearing identity (**Proposition 12**, going back to Heine–Szegő):
`det Q^σ_N = (1/N!) ∫_{σ^N} (det V_𝓜(z))² ω^{⊠N}`, where `V_𝓜(z)=(𝔣_j(z_i))` is a
**generalised Vandermonde matrix**. Hence the determinant is bounded by a Vandermonde sup
(**Corollary 14**): for `N` large, `|det Q^σ_N|^{1/N} < t_𝓜(σ)^{2/N}` where
`t_𝓜(σ) = sup_{z∈σ^N} |det V_𝓜(z)|` (Definition 13).

Feeding this into **Minkowski on linear forms** (Theorem 1 / Theorem 41): after choosing
integer-clearing matrices `D^ℓ, D^r` with `A^σ = D^ℓ Q^σ D^r` integral in the `ξ_i` and
denominator `δ_𝓜 = det|D^ℓ D^r|`, one gets (**Theorem 42**) a nonzero integer linear form
with `0 < |∑ n_i ξ_i| ≤ (t_𝓝(fσ)² δ_N)^{1/N}`. Passing to the limit via the **supremal
transfinite diameter** `Sup_{𝓝,e}(τ) = limsup_n (t_{𝓝_n}(τ))^{1/e_n^𝓝}` (Definition 22;
`e_n` = "exponents", typically the total degree of `det 𝓝_n`) and
`δ_{𝓝,e} = limsup_n δ_{𝓝_n}^{1/e_n^𝓝}` gives the headline:

> **Criterion 4.** `Sup_{𝓝,e}(f(σ))² · δ_{𝓝,e} < 1`  ⟹ (with Criterion 3 hypotheses) `ξ` irrational.

with the pre-limit **Criterion 3** (`t_{𝓜_N}(σ)² δ_{𝓜_N} → 0 ⟹ ξ ∉ ℚ`) and the linear-
independence form **Corollary 43** (`Sup²·δ < 1 ⟹ dim_ℚ⟨ξ₁,…,ξ_r⟩ ≥ 2`). The hypothesis
on the periods (Criterion 3) is: **`m=2, ξ₁=1, ξ₂=ξ`; or `m>2, ξ₁=1` and each `ξ_i ∈ ℚ[ξ]`**.
This hypothesis is exactly the obstruction for ζ(5) — see §1.5.

### 1.2 What finite / numeric data it consumes

Everything reduces to two limits over an explicit sequence of finite matrices:
1. **`t_{𝓜_n}(fσ)` = a sup of a generalised Vandermonde `|det(𝔣_i(z_j))|` over `z ∈ (fσ)^N`**
   — an optimisation over a compact region; bounded above by the transfinite diameter of
   the region `f(σ) ⊂ V_f(ℂ)`.
2. **`δ_{𝓜_n}` = denominator** of `det Q^σ_n` (an lcm-type product coming from pole orders
   along a compactification of `X`).

The two "intuitive-example" thresholds (§1.5 of the paper) make the trade explicit: for a
`w`-weight, `r`-parameter rectangular family, Criterion 4 reduces (eq. `intro:generalSupbound`)
to `Sup^{rec}(f σ)·exp(w(2r+1)/(r(r+1))) < 1`, sufficient condition `Sup^{rec}(fσ)·exp(2w/r)<1`.
For `r=1` this is exactly **Zudilin's determinant criterion** `tr(fσ) < exp(-3w/2)` (Remark 2).
The universal constant is `4·Sup^{rec} < 4e^{-2} = 0.5413…`, i.e. the region must be roughly
half the unit square (whose `Sup^{rec}=1/4`). The method **improves as `r` grows** because the
irrationality threshold `exp(-2+1/(w+1))` improves with `r` (taking `r=w`).

### 1.3 What a computer-verified certificate would look like

For a given family and module `𝓝`, a certificate proving Criterion 4 has two independent halves:

- **Analytic half (upper bound on `Sup`):** exhibit an explicit sequence of regions
  `T_min ⊂ φ(τ) ⊂ T_max` (triangles / boxes) whose homogeneous transfinite diameters are
  known in closed form, and chain the reduction lemmas — tensor product **Theorem 20 /
  Theorem 27 / Corollary 30**, direct sum **Proposition 21 / Proposition 31 / Corollary 33**,
  and the hyperbola-region **Propositions 35 & 38**. The atomic known values used are:
  interval `tr([a,b]) = (b-a)/4` (eq. `supinterval`); rectangular box
  `Sup^{rec}([a,b]×[c,d]) = √((b-a)(d-c))/4` (eq. `trecsquarebox`); unit ball
  `tr(B)=1/√(2e)` (Bos); triangle `tr(T) = vol(T)^{1/2}/(e√2)` (eq. `transfinitetriangle`).
  The worked prototype: **Proposition 52**, `(Sup^{rec}_{(1,1)}(τ))² < 0.023` for the ζ(2)
  region, proven by sandwiching between two explicit triangles.
- **Arithmetic half (upper bound on `δ`):** a denominator bound from pole orders. Currently
  done by hand (Lemma 45/46; §9 gives `10/3`, then `115/36 = 3.194…`, then for the 5-param
  family `19/4 = 4.75`). Brown states the *expected* general source: **overconvergent
  `p`-adic de Rham cohomology**, sharpenable by **congruences in algebraic de Rham
  cohomology** (Introduction, and Remark 56 / §8.2.1).

So a machine certificate = (a) a finite chain of transfinite-diameter inequalities with a
numeric slack, plus (b) a proven lcm/`p`-adic denominator bound, with `Sup²·δ` provably `< 1`.

### 1.4 Explicitly computable quantities Brown states without computing; tables extendable by machine

- **The `Q^σ_n` determinant tables for ζ(2)/`M_{0,5}` (§9).** Three tables:
  - two-parameter family `I(n₂,n₁,n₂,n₁,n₂)`, computed to **n=16** (rank 256), Maple;
    columns `t²_n`, `log d_n^{1/e_n}`, `t²_n d_n^{1/e_n}`, threshold `ϑ_n`. At n=16:
    `t²_n = 0.01967`, `t²_n d^{1/e_n} = 0.3476`, `ϑ_n = 1.368`.
  - "two copies" variant `𝓜_n ⊕ u₁𝓜_n`, to **n=9**.
  - full five-parameter family (`𝓜 = 𝒪(M_{0,5}^δ)`), to **n=11** (rank 331), with the
    exponent `e_n = 5n(n+1)(2n+1)/6`.
  These are *directly extendable* by any CAS with exact linear algebra over `ℚ[ζ(2)]`.
  Brown explicitly did **not** optimise the modules: "it might be interesting to consider
  modules whose monomial bases in `r` variables are centered around one or more of the
  Rhin–Viola 'lines'" (§1.6 Plan). **Extending these tables to `M_{0,8}`/ζ(5) is the natural
  seam** (§6.B).
- **The determinant factorisation.** `det Q^σ_n` factors over `ℚ[ζ(2)]` in a structured way:
  Example 51 (n=3, 2-param) factors as degree 4 × degree 6²; Example 54 (5-param, n=1) gives
  `det Q^σ_1 = (1/1024)(8x²−x−20)(16x²−44x+29)²` with `x=ζ(2)`, and the same two factors
  reappear in the 2-param n=2 determinant (eq. `detFactorsf1f2`). Brown: "the precise
  structure is interesting and warrants further investigation." **A clean CAS target: explain
  / prove the factorisation pattern of `det Q^σ_n(ζ(2))`, presumably from the `D₁₀` dihedral
  symmetry** (he notes he did *not* exploit the symmetry, §9 closing remarks).
- **The `p`-adic determinant conjecture (Remark 56).** Because `ζ_p(2)=0`, the `p`-adic
  matrices `Q^p_n` (the `p`-adic realisation of the de Rham matrices `Q^{dR}_n`, §8.2.1)
  have **rational entries**, hence are directly computable. Brown *expects*:
  `δ_n^{1/e_n} ~ ∏_p |det Q^p_n|_p^{1/e_n}`, giving the reformulated criterion
  `limsup_n (|det Q^σ_n|² ∏_p |det Q^p_n|_p)^{1/e_n} < 1`. **This is a finite, testable
  conjecture** — compute `det Q^p_n` for small primes and small `n`, compare its `p`-adic
  valuation to the actual denominator `d_n` in the printed table. Currently *stated without
  computing*.
- **Contiguity / Picard–Fuchs matrices (Appendix, §11).** Explicit `2×2` contiguity matrices
  `M_i(s)` for the ζ(2) family are given; Example 60 computes `I(0,0,1,0,1)=ζ(2)−1` by matrix
  products; Remark 61 gives the all-parameter shift matrix with determinant
  `−(n+1)²(n+2)^{-2}`. These give a fast, exact route to filling `Q^σ_n` without numerical
  integration, and Brown notes they are not exploited in the main text.

### 1.5 Does it apply to the BZ ζ(5) family, and does it change what γ = 0.866 means?

**Short answer: not as literally stated, and it does not change the meaning of γ=0.866 —
but it reframes why 0.866 is a ceiling.**

- **Applicability.** For `M_{0,8}` the periods are `{1, ζ(2), ζ₅ = ζ(5)+2ζ(2)ζ(3)}`, so
  `m=3`. Criterion 3/4 needs each `ξ_i ∈ ℚ[ξ]` with `ξ₁=1`. Here `ξ = ζ₅` but `ζ(2) ∉ ℚ[ζ₅]`
  ([RECALLED-UNVERIFIED] conjecturally algebraically independent). So Criterion 4 does **not**
  certify ζ(5) irrational; at best Corollary 43 gives `dim⟨1,ζ(2),ζ₅⟩ ≥ 2`, already known
  (ζ(2) irrational). This is **exactly the parasitic-ζ(2) obstruction** that BZ hit (§2). Brown
  flags the missing ingredient: "it would be very interesting to generalise the irrationality
  criterion 4 to a **linear independence criterion**, by bounding the numerators in the linear
  forms obtained from Minkowski's theorem. This will be postponed to another day" (§1.6).
- **Meaning of γ=0.866.** γ is the *worthiness* of a **single effective sequence** `I(a·n)`
  (one Rhin–Viola-type line in the 7-dim cone): `γ=(c₁−c₀)/c₁`, a ratio of asymptotic growth
  rates with a group-sharpened denominator. Brown's method is a **different object**: it fills
  `Q^σ` with *many* integrals `I(n)` over a box and lets Minkowski extract a small combination;
  success is governed by `Sup²(fσ)·δ`, which **decouples denominators from asymptotics** — the
  explicit thesis of the Introduction ("a useful strategy is to fill the input matrix `Q^σ`
  with integrals with small denominators, irrespective of whether they individually give good
  approximations"). So γ=0.866 measures the single-line lever; Criterion 4 measures a region.
- **The reframing / connection to the sibling result.** The sibling session measured
  `sup γ = 0.86597135…` over the full 7-dim cone = the BZ published point, i.e. **the group-𝔊
  single-line method is exhausted at 0.866**. This is *precisely consistent* with Brown's
  premise that "the group method, which involves selecting a single line of integrals, ... does
  not fully exploit the whole 5-dimensional [here 7-dim] space of parameters." Brown's
  multi-parameter criterion is the tool designed to exploit the rest of the cone. **So the
  0.866 ceiling and Brown 2026 are two sides of one coin: the seam is whether the full-cone
  Minkowski construction on `M_{0,8}` beats the single-line ceiling — but the parasitic ζ(2)
  still blocks a *new* result until the linear-independence generalisation exists.**

### 1.6 Conjectures / open expectations stated in `llm/21`

- **(Remark 47)** whether the denominator-clearing matrices `D_n` can be designed to exploit
  Rhin–Viola prime cancellation: "I do not know the answer" — yet the ζ(2) experiments show
  "a large degree of 'prime cancellation' of possibly a different nature." Open, and the
  observed cancellation is a computable phenomenon (the printed tables already show the true
  `d_n` far below the crude lcm bound).
- **(Remark 56 / §8.2.1)** the `p`-adic transfinite diameter and the product formula above —
  a conjecture with an explicit finite test.
- **(§8.1 "Beyond positivity")** for `r=1`, `Q^σ_N` is a Hankel matrix and Kronecker's theorem
  controls non-vanishing; for `r>1` these are "multivariable Hankel forms" (cf. Power) — the
  general non-vanishing theory is not worked out.
- **(§5.4)** "there are few results which establish the precise value of the transfinite
  diameter in higher dimensions ... for the rectangular case, very little seems to be known."
  **Computing/bounding the rectangular or homogeneous transfinite diameter of the specific
  regions `f(σ)` from `M_{0,n}` is a genuine, partly-computable analysis problem** and the
  effective bottleneck of the whole method.

---

## 2. Brown–Zudilin 2022 — cellular rational approximations to ζ(5) (`llm/20`, arXiv 2210.03391)

The family is `I(a)` on `M_{0,8}` (eq. `I1`), denoted `⁸π^∨₈` in Brown 2014 Example 7.5. It
decomposes (eq. `deco`) as `I = Q·(2ζ(5)+4ζ(3)ζ(2)) − 4P̂·ζ(2) − 2P`, and "setting ζ(2)=0"
gives `I' = Qζ(5) − P`. **Theorem 1**: an effective sequence `p/q` with
`0 < |ζ(5) − p/q| < 1/q^{0.86}`, worthiness `γ(a) = 0.86597135…` (proof §11, for
`a=(8,16,10,15,12,16,18,13)`). The symmetry group `𝔊 ≅ Σ₇ ≅ W(A₆)`, order `7!=5040`, acts on
28 hyperplanes `h₁,…,h₂₈` (eq. `eq:h`), splitting into orbits `h'` (size 21, `= {s_i+s_j}`)
and `h''` (size 7, `= {s₀−s_i}`) in symmetric coordinates `s₀,…,s₇`.

### 2.1 Every concrete open item (the "what are those other representations?" list)

1. **"But what are those other representations?"** (§12, `(In)conclusive comments`).
   The group `𝔊` is *exhaustive* (§8 shows `Aut_D` gives nothing more), yet the group-derived
   exponents `ν_p` (eq. `nu_p`) are numerically **not always optimal**. BZ expect the missing
   savings to come from **different integral representations, each with its own arithmetic**
   (as in Zudilin 2014 for ζ(2)&ζ(3)). They give one explicit alternative: **eq. `I-b`**,
   identical to `I-a` except for an extra denominator factor `(1−x₂x₃x₄x₅)^{a₁−a₃}`, available
   for every `I(𝔤a)`, `𝔤∈𝔊`. **This is the single most concrete open computational item:
   compute the arithmetic (denominators, prime cancellations) of representation `I-b` (and its
   `𝔊`-orbit), extract the extra ν_p, and test whether γ exceeds 0.866.**
   Sibling-session connection: since `sup γ=0.866` is *already* proven optimal for the printed
   representation, any improvement **must** come from these other representations — so this item
   is both concretely stated and the only route past the ceiling.
2. **Explicit sub-optimality example** (§12). For `a=(15,20,16,14,18,17,16,20)` (γ=0.85163139),
   the group gives `ν_p=3` for primes with `1/19 ≤ {n/p} < 1/18`, but experimentally (n up to
   40) the exponent can be raised to **4**, lifting γ to `0.85665016…`. **A finite, currently-
   unproven computational observation** — extendable/provable by machine.
3. **The `ℓ`-split optimum** (Remark 5, and §11). The choice of the five successive maxima
   `m₁≥…≥m₅` used in the denominator may be non-optimal: possibly `m₁,…,m_ℓ` from the 21-set
   `h'` and `m_{ℓ+1},…,m₅` from the 7-set `h''`, for some `ℓ∈{1,…,5}`. For the Theorem-1 point,
   `ℓ=3` or `4` is consistent; "if the true value of ℓ ... were to differ from 3 and 4, there
   would be a small potential gain." **A finite check.**
4. **Explicit general-parameter Apéry recursion** (Remark 1, Remark 2). A third-order
   Apéry-type recurrence for `I(a·n)` (hence for `Q(a·n),P(a·n),P̂(a·n)` and `I'`) via creative
   telescoping is "a practical (though technically challenging!) task." Done only in the
   totally-symmetric case (the explicit degree-9 recursion in §2). **Concrete CAS goal** —
   sibling session reports the ζ(5) characteristic polynomial `4λ³−2368λ²−188λ+1` confirmed
   three ways.
5. **The middle-weight motive dimensions** (§4). "The dimensions of `M` in middle weights have
   not been rigorously established: to this end, it would be very interesting to have general
   tools to compute the de Rham realisation `M_{dR}` via computer. This would ... provide
   contiguity relations." Only highest/lowest/subleading weights are proven
   (`gr^W₀=ℚ(0)`, `gr^W₁₀=ℚ(−5)`, `gr^W₈=0`). The rank-3 shape
   `gr_W M = ℚ(0)⊕ℚ(−2)⊕ℚ(−5)` is **"computations of periods suggest"** — expected, not proven.
6. **Motivic-ity of `𝔊`** (§4). "It would be very interesting to prove that the entire group
   `𝔊` ... is also motivic."
7. **The symmetry-group pattern** (Remark 4). `W(A₄)=120` [ζ(2)], `W(D₅)=1920` [ζ(3)],
   `W(E₆)=51840` [ζ(4)], and now `Σ₇=W(A₆)=5040` [ζ(5)]. "Precisely how this pattern of
   symmetry groups extends to more general cellular integrals (as we expect) remains a
   mystery." (Note: the ζ(5) group `A₆` *breaks* the `A₄,D₅,E₆→E₇,E₈` progression — itself a
   structural puzzle.) **Computable: determine the symmetry groups of other convergent
   configurations at `M_{0,8}` and higher.**
8. **The weight-7 `M_{0,10}` family** (§12). Configuration `(10,2,4,1,6,3,8,5,9,7)`
   ("vanishing in the middle"), a rank-4 motive `ℚ(0)⊕ℚ(−2)⊕ℚ(−5)⊕ℚ(−7)`. `I_n = I'_n + I''_n ζ(2)`
   with `I''_n ∈ ⟨1,ζ(3),ζ(5)⟩` and `I'_n ∈ ⟨1,ζ(5),ζ(7)⟩`; explicit `I₀,I₁,I₂` given
   (`I₀ = (75/4)ζ(7) − 9ζ(5)ζ(2)`). "A similar analysis ... might possibly lead to a result of
   the form 'at least one of ζ(5) and ζ(7) is irrational'." Sibling session already **extended
   this beyond n≤2** (leading coefficients `q₃=94357501`, `q₄=235634763001`, `q₀…q₃₀` archived).
9. **General higher-weight machinery** (§12). "calculating higher weight integrals for small
   values of the parameters does not seem practical with current tools ... A possible way ... is
   to create an entirely new theoretical machinery for the arithmetic and asymptotics ... based
   on the underlying algebraic geometry and contiguity relations." (This is exactly what `llm/21`
   begins to build.)

### 2.2 The integrality / denominator claims — and the sibling's factor-12 correction

- **Totally-symmetric claim** (eq. `dn-totsym`): `Q_n, d_n² d_{2n} P̂_n, d_n⁵ P_n ∈ ℤ`,
  "observed experimentally." `Q_n` is proven integral by the explicit double binomial sum
  (eq. `Q_n`).
- **General claim** (eq. `incl`): `d_{m₁n}d_{m₂n}d_{m₃n}d_{m₄n}d_{m₅n} I'(a·n) ∈ ℤζ(5)+ℤ`, with
  `m₁≥…≥m₅` five successive maxima of the 28-multiset; sharpened by the `𝔊`-cancellation
  factor `Φ_n = ∏_{p>√(m₁n)} p^{ν_p}` (eq. `sharp_incl`).
- **Sibling correction (confirmed against the paper's own printed values).** These are **false
  as printed**: with `P₂ = 1190161/384` and `d₂=2`, `d₂⁵ P₂ = 32·1190161/384 = 1190161/12 ∉ ℤ`.
  The corrected statements require an **exact extra factor 12 = 2²·3** (resp. 2 for the ζ(3)-
  companion `P̂`). The sibling reduced the *sharp* denominator law to a per-prime ceiling
  (`ord_p den(P_n) ≤ ord_p D_ν + [2 if p=2; 1 if p=3; ±1 boundary at p=m₁]`) verified in 200+
  certified cells, and identified the mechanism: `12 = 24/2` where 24 comes from
  `ζ(2)=−(2πi)²/24` (the cost of killing the ζ(2)-column, a multiple of `24γ₁+γ₂`) and the
  factor 2 is a genuine **index-2 refinement of the integral Betti lattice of the `M̄_{0,8}`
  motive**. **This directly instantiates Brown 2026's expectation** that "denominator bounds
  can be significantly improved by exploiting congruences in algebraic de Rham cohomology."
  Named remaining open piece (sibling H1): a two-variable well-poised `2n→n` refinement reduced
  to a **Dwork-descent congruence**.

### 2.3 The geometry section's unproven expectations (§4)

- rank-3 motive shape `gr_W M = ℚ(0)⊕ℚ(−2)⊕ℚ(−5)`: **"computations of periods suggest"**;
- period matrices `periodmatrix1`/`periodmatrix2` rely on `Ext¹(ℚ(−5),ℚ(0))` being
  1-dimensional with period ζ(5) and `Ext¹(ℚ(0),ℚ(−2))` splitting — standard MT-motive facts
  but applied to `M` on the basis of the expected rank;
- middle-weight dimensions unproven (item 5 above);
- the heuristic "three real asymptotics" justification (§5) via the cubic
  `F(x)/(x(p₃−x))` (eq. `Fcubic`) is an analytic-continuation argument, not a cohomology proof.

---

## 3. Brown 2014 — "dinner parties" (`llm/19`, MJCNT 6 (2016))

### 3.1 The structural reason ζ(5) resists

Two nested obstructions, both stated explicitly:

- **The generic haystack** (§1.3). The generic period integral yielding weight-≤5 forms
  (i.e. candidates for `1,ζ(5)`) "depends on 20 independent parameters, which is hopelessly
  large." One needs **vanishing theorems** (requirement (4)): `gr^W_{2k} m(A,B)_{dR}=0 ⟹`
  coefficient of weight-`k` MZVs vanishes. Brown: "I was only able to find a general method to
  force the coefficients of **sub-maximal weight `2ℓ−2`** to vanish" — i.e. only `ζ(ℓ−1)` is
  killed generically. For `M_{0,8}` (`ℓ=5`) that kills `ζ(4)` only. The parasitic `ζ(2)` (and
  `ζ(3)`, and `ζ(2)ζ(3)`) sit in the *middle* of the weight range where no general vanishing
  method exists.
- **Even the clean family still fails to isolate ζ(5)** (Appendix 2, n=8 table). The
  configuration `⁸π₈ = ⁸π_odd` gives linear forms in `1, ζ(3), ζ(5)` **only** (`I_π(0)=2ζ(5)`,
  no ζ(2)!) — yet this is "amply sufficient to prove `dim⟨1,ζ(3),ζ(5)⟩ ≥ 2` but **insufficient
  to prove their linear independence**." So even after killing ζ(2), ζ(3) becomes parasitic.
  To isolate ζ(5) you must kill **both** ζ(2) and ζ(3); BZ's descent-to-ζ(3) handles one and
  "setting ζ(2)=0" the other, and the net is still only `≥2`. **This is the deep reason ζ(5)
  resists: the vanishing machinery kills the top-adjacent weight, never the middle.**

### 3.2 The enumeration of cellular integrals — finite and machine-extendable

The convergent configurations are a variant of the **dinner-table problem** (Poulet 1919):
`σ` is *convergent* iff no `k` elements (`2≤k≤n−2`) are simultaneously consecutive for `δ⁰`
and `σδ⁰`. For `n≤7` this equals the classical dinner-table problem; for `n≥8` it is a
genuinely stronger condition. The counts (Appendix 2):

| `N` | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|
| `𝒞_N` | 0 | 1 | 1 | 5 | 17 | 105 | 771 | 7028 |

**This is a concrete integer sequence, finite for each `N`, directly extendable by machine to
`N=12,13,…`** (the convergence condition is a purely combinatorial predicate on permutations —
footnote 3). It is a genuine compute seam with two payoffs:
- extend `𝒞_N` and identify the analog of the ["odd zeta values only"] configurations at higher
  `N`: `⁸π_odd` gives `1,ζ(3),ζ(5)`; `¹⁰π_odd` gives `1,ζ(3),ζ(5),ζ(7)` (vanishing in weights
  1,2,4,6). A configuration at `N=12` giving `1,ζ(3),ζ(5),ζ(7),ζ(9)` would be the natural next
  Ball–Rivoal-style object.
- the **vanishing phenomena are stated as experimental**: n=9 "By computing all of them in low
  degrees, one observes that all the linear forms vanish in weight 5"; n=10 "They all
  (experimentally) vanish in sub-leading weight." Brown: "It would be interesting to know if it
  is possible to find sequences of higher order with stronger vanishing properties." **These are
  machine-verifiable/refutable and machine-searchable.**

### 3.3 What Brown says is unknown

- **Problem 1** (§8.3): "Find a combinatorial formula for the motivic coaction on the
  `I^𝔪(ω, S_δ)`." (Open, combinatorial.)
- Whether the philosophy (linear inequalities → cohomology vanishing → coefficient vanishing,
  eq. `philosophy`) can be pushed to force *arbitrary* vanishing, "or failing that, to show that
  one cannot construct moduli space motives `m(A,B)` with arbitrary vanishing properties."
- **Example 32** = the BZ family `⁸π^∨₈`: gives an explicit `a₀ + a₂ζ(5)` linear form with huge
  coefficients; "An infinite family of such examples would suffice to prove the irrationality of
  ζ(5)." — the exact hook BZ 2022 picks up.

---

## 4. Fischler–Rivoal 2013 — MZV, Padé approximation, Vasilyev's conjecture (`llm/24`, arXiv 1309.2534)

- **Vasilyev's conjecture** (stated inline as eq. `intro1`, *not* given a "Conjecture N"
  label): for integers `d≥2, n≥0`,
  `J_{d,n} = ∫_{[0,1]^d} ∏ x_j^n(1−x_j)^n / Q_d^{n+1} dx ∈ ℚ + ℚζ(2+e_d) + ℚζ(4+e_d) + … + ℚζ(d)`
  with `e_d = d mod 2` and `Q_d` the nested Vasilyev denominator. I.e. `J_{d,n}` is a rational
  linear form in `1` and (odd `d`) `ζ(3),ζ(5),…,ζ(d)` or (even `d`) `ζ(2),…,ζ(d)`.
- **Status: fully PROVEN, all `d`, all `n`** — before this paper. `d=2,3` Beukers; `d=4,5`
  Vasilyev; **all `d`: Zudilin 2003**; further proofs Zlobin, Krattenthaler–Rivoal. This paper
  is a **fourth proof, for odd `d≥3` only**, via a mixed Padé problem: **Theorem 1** (the Padé
  problem `𝒫_{r,n}` has a unique solution `S_{r,n}(z)` = explicit integral over `[0,1]^{2r+3}`),
  evaluated at `z=1` using the reduction identity **Proposition 1**
  (`ζ^{…}_{2{1}_{2k−1}} = 2ζ(2k+1)`).
- **What remains open: nothing about Vasilyev's conjecture itself** (it is a theorem; no
  residual case-check, no rank/determinant side-condition, **no tables in the paper**). The one
  open item (§6) is a genuine research problem, *not* a finite computation: to prove the
  Ball–Rivoal infinitude of odd-ζ, one needs "**a Padé approximation problem of which
  `S_{r,n,σ}(z)` would be a solution. We believe that a suitable generalisation of the problem
  `𝒫_{r,n}` ... could have this property.**" — a construction to be discovered, not CAS-closable.
- **Machine-generable but uncomputed:** the Padé polynomials `A_ρ,B_ρ,C_ρ,D` (all deg ≤ `n`,
  rational, via the given series for `S_{r,n}` + the [crefiri] algorithm); the explicit rational
  Vasilyev linear form `∑_ρ A_ρ(1)·2ζ(2ρ+3) + D(1)` for each odd `d`; the very-well-poised
  series `S_{r,n,σ}(1)`. **No finite open verification exists here — Vasilyev is a closed door
  for a "new result," but the explicit-coefficient generation is a warm-up CAS exercise.**

---

## 5. Brown 2026 — nonlinear geometry of MZV (`llm/32`, arXiv 2604.22735)

**Character: lecture notes/survey; many theorems cited from Brown's other papers. No
irrationality content whatsoever** — the word "irrational" does not appear in the source, and
there is no linear-independence claim about zeta values (target (3): explicitly none). Relevance
to the programme is *conceptual*, via one bridge:

- **The determinantal ("non-linear") integral representation** (eq. `introIasdet`):
  `I = ∫_σ N(x)/det(X)^d dx`, "non-linear precisely when `det(X)` defines an irreducible
  hypersurface." Motivating **Example 1**: `6ζ(3) = ∫ dx₁…dx₅/det(X)²` for an explicit `3×3`
  linear-form matrix `X` (the `W₃` graph Laplacian). **Theorem 16**: `det Λ_G = Ψ_G` (Laplacian
  determinant = graph polynomial). **This is the natural generalisation of the Mellin picture of
  `llm/21`**: there the small forms come from `∏f_i^{n_i}`; here from powers of a single
  irreducible `det(X)`. A Mellin integral is the "linear" (`det X = ∏` of linear forms up to
  monomial) degenerate case. This is the only load-bearing link to the irrationality seams.
- **New objects (for completeness):** canonical forms `ω^n_X = tr((X^{-1}dX)^n)` (odd `n`, closed,
  projectively invariant, bi-invariant Lemma 38); canonical algebra `Ω^•_can = ⋀(⊕ ℚω^{4k+1})`;
  canonical integrals `I_G(ω)` (Definition 39), **always finite** (Theorem 40); they detect graph
  homology (Theorem 42) and evaluate to single-valued MZVs (Theorem 44, Portner). Evaluations:
  `I_{W_g}(ω^{2g-1}) = g C(2g,g) ζ(g)` (Theorem 43); Minkowski volume
  `∫ vol_g = α_g ζ(3)ζ(5)…ζ(g)`, `α_g ∈ ℚ^×` (Theorem 50) — **`α_g` not computed**.
- **Testable conjectures / finite data (all in graph-complex / `GL_n(ℤ)` land, off the
  irrationality axis):** Remark 29 (`Z_g/I_g` MZV-dimension table, weights 2–11, CAS-checkable);
  Table 1 (`dim H_k(GC₂)` to `h_G=11`, "by computer", extendable); **Drinfeld's conjecture**
  (`grt` free on one generator per odd degree ≥3, testable degree-by-degree, after Theorem 31);
  the **zig-zag Hepp-bound dominance** `I^res_G ≤ I^res_{Z_n}` (numerically testable);
  **Question 49** (write an explicit `[ω^5,ω^9]` form on `LM₈^trop` → an irreducible weight-8 MZV
  like `ζ(3,5)`); **Example 55 / Question 54** (the two unknown `g=5` Voronoï cone volumes);
  the undetermined homology degree `k_{m,n}` (Theorem 48, `0<k_{m,n}<2min{m,n}−3`).
- **Note (numbering):** the pandoc conversion transposed the `Ξ_{m,n}` result — cite it as
  **Theorem 48** (inside **Example 47**), `I_{Ξ_{m,n}}(ω^{2m-1}∧ω^{2n-1}) = ζ(m)ζ(n)`, odd `3≤m<n`.

Bottom line for this programme: `llm/32` supplies the *geometric worldview* (periods as
`∫ N/det^d`, odd ζ ↔ `K_{2k+1}(ℤ)` regulators) into which `llm/21`'s Mellin criterion fits, but
contributes **no irrationality statement and no directly-usable new lever**. Its CAS-testable
conjectures belong to graph homology, not Diophantine approximation.

## 5′. Brown–Schnetz 2024 (`llm/31`, skim)

**Largely not relevant to the irrationality programme.** It computes "canonical integrals"
`I_{W_n}(ω^{2n-1})` of graph-Laplacian trace forms and proves them *exact* rational multiples of
single odd zeta values (**Theorem 1**: `I_{W_n} = n·C(2n,n)·ζ(n)` for odd `n≥3`), then uses
non-vanishing to build classes in `GC₂`, `H_*(GL_n(ℤ))`, and tropical moduli. **No** irrationality,
Mellin, transfinite-diameter, `M_{0,n}`, or rational-approximation content ("irrationality",
"Mellin", "transfinite", "M_{0,n}" do not appear). Only cosmetic overlaps: same author, the
recurring `C(2n,n)` and Apéry-type sums (Theorem 62), central-factorial coefficients A036969
(Lemma 64), and an `h_G=7` census (Table 2). Flag only if a self-contained CAS warm-up is wanted;
it does not touch the odd-ζ seams.

---

## 6. SYNTHESIS

### 6.a Map of concretely-stated open problems, ranked by (provable-by-us × mattering)

`P` = tractability for a CAS+proof effort (5 = a weekend, 1 = a career); `M` = advance to the
programme (5 = new Diophantine statement, 1 = cosmetic). Ranked by `P·M`.

| # | Problem (source) | P | M | Note |
|---|---|---|---|---|
| A | **p-adic determinant denominator formula**, `δ_n^{1/e_n} ~ ∏_p|det Q^p_n|_p^{1/e_n}` for ζ(2)/`M_{0,5}` (21-Rem 56) | 5 | 3 | `Q^p_n` rational (ζ_p(2)=0); fully finite; validates the denominator half of Criterion 4 and dovetails with the sibling's index-2 lattice mechanism |
| B | **Weight-7 `M_{0,10}` family** `(10,2,4,1,6,3,8,5,9,7)` → conditional "one of ζ(5),ζ(7) irrational" / a worthiness for the pair (20-§12) | 3 | 5 | sibling already has `Q_n` to `q₃₀`; needs recurrence + asymptotics + denominators; only route to a *new* (conditional) statement |
| C | **Transfinite-diameter table for ζ(5)/`M_{0,8}`**: compute `Sup²·δ, ϑ_n` (extend 21-§9 off `M_{0,5}`) | 3 | 4 | the decisive "does the full-cone Minkowski method beat the single-line 0.866 ceiling" experiment; blocked from a *new* result by parasitic ζ(2) but publishable as measurement |
| D | **Sharp-12 denominator law → Dwork-descent congruence** (20-`incl`; sibling H1) | 3 | 4 | the general denominator theorem for the family; realises 21's "congruences in de Rham cohomology" expectation; one named congruence remains |
| E | **Extend `𝒞_N` enumeration** to `N=12,13`; classify odd-zeta-only & vanishing types (19-App 2) | 4 | 3 | pure combinatorial predicate + HyperInt weight tables; finds the `N=12` `1,ζ(3),ζ(5),ζ(7),ζ(9)` candidate |
| F | **`I-b` and its `𝔊`-orbit**: arithmetic of the alternative representation, extra `ν_p`, test γ>0.866 (20-§12) | 2 | 4 | *the* stated route past 0.866, but BZ warn the gain is "insignificant"; high effort, likely tiny payoff |
| G | **Prove `det Q^σ_n(ζ(2))` factorisation** from `D₁₀` symmetry (21-Ex 51/54/55) | 4 | 2 | clean representation-theory target; "warrants further investigation" |
| H | **General-parameter Apéry recursion** for `I(a·n)` via creative telescoping (20-Rem 1/2) | 3 | 3 | sibling's CT pipeline works; needed input for B, C, F |
| I | **de Rham realisation `M_{dR}` of the ζ(5) motive** by computer → middle-weight dims + contiguity (20-§4) | 2 | 4 | would *rigorise* the rank-3 claim and hand over contiguity matrices (asymptotics+arithmetic for free) |
| J | **Design `D_n` for Rhin–Viola prime cancellation** (21-Rem 47) | 2 | 3 | unify the two denominator-improvement mechanisms; "I do not know the answer" |
| K | **Symmetry-group pattern** `W(A₄),W(D₅),W(E₆),Σ₇` — compute groups of other cellular families (20-Rem 4) | 3 | 2 | "remains a mystery"; ζ(5)'s `A₆` breaks the E-series |
| L | **Combinatorial motivic-coaction formula** (19-Problem 1) | 1 | 3 | structural, hard, open since 2014 |

Non-starters for us (closed or out of scope): Vasilyev's conjecture (`llm/24`, **proven**, no
finite residue); all `llm/32` conjectures (Drinfeld, Hepp/zig-zag, `H_*(GC₂)` — graph-homology,
off-axis); `llm/31` (graph homology, off-axis).

### 6.b Top 3 candidate results a strong CAS+proof effort could realistically deliver

**#1 — The `p`-adic determinant denominator law for ζ(2)/`M_{0,5}` (problem A).**
- *Statement to aim at.* For the two-parameter (and five-parameter) `M_{0,5}` families of `llm/21`
  §9, `lim_n δ_n^{1/e_n} = lim_n (∏_p |det Q^p_n|_p)^{1/e_n}`, where `Q^p_n` is the de Rham matrix
  `Q^{dR}_n` specialised at the crystalline Frobenius (rational entries since `ζ_p(2)=0`). Equivalently,
  the reformulated Criterion 4 `limsup_n(|det Q^σ_n|² ∏_p|det Q^p_n|_p)^{1/e_n} < 1` holds with the
  same numeric value already tabulated (`t²_n d_n^{1/e_n} → ~0.32`).
- *Route.* Fill `Q^{dR}_n` exactly with the contiguity matrices `M_i(s)` of §11 (no numerical
  integration); specialise to `Q^p_n` and compute `ord_p det Q^p_n` for `p ≤ 30`, `n ≤ 20`; compare
  to the printed `d_n` column. Then prove equality from pole-order bounds along the boundary
  divisor `E ⊂ M_{0,5}^δ` (the `p₁,…,p₅` vector of `llm/21` eq. `p1-5vectors`), i.e. that the
  denominator is governed entirely by the `p`-adic valuation of a determinant of periods.
- *Failure mode.* The relation may be `~` (leading-order) not `=`: boundary-prime fluctuations
  (the sibling's `±1` at `p=m₁` in the sharp-12 law) could break equality at each finite `n`, leaving
  only the asymptotic. Still a theorem, just weaker. Second risk: the "de Rham matrix" `Q^{dR}_n`
  needs the middle-weight cohomology to be understood — for `M_{0,5}` it is (rank 2), so this risk is
  low here (but it is exactly problem I for `M_{0,8}`).

**#2 — First honest transfinite-diameter measurement for the ζ(5)/`M_{0,8}` family (problem C, needs H).**
- *Statement to aim at.* A proven upper bound `Sup²_{𝓝}(f(σ_{0,8})) < c` via the tensor/direct-sum
  reduction chain (21-Thm 20/27, Prop 21/31, Cor 33) applied to the `M_{0,8}` region, together with
  a computed table of `t²_n, d_n^{1/e_n}, ϑ_n` for the BZ integrals to as high `n` as HyperInt allows;
  hence the first numeric value of `Sup²·δ` for a weight-5 family and a quantified comparison to the
  single-line worthiness ceiling 0.866.
- *Route.* Reuse the sibling's exact-integral pipeline (HyperInt / Barnes / creative telescoping) to
  fill `Q^σ_n` with `I(n)` on `M_{0,8}`; get `t_n = (det Q^σ_n)^{1/e_n}` and the denominator `d_n`;
  bound `Sup` by sandwiching `f(σ_{0,8})` between explicit polytopes as in Prop 52. Problem H (general
  recursion) accelerates filling the matrix.
- *Failure mode.* (i) It **cannot** yield a new irrationality result — `m=3` with parasitic ζ(2),
  Criterion 4 gives only `dim≥2` (known); the deliverable is a *measurement*, honestly framed. (ii) The
  higher-dimensional transfinite diameter is largely unknown (21-§5.4), so expect *bounds*, not values.
  (iii) Weight-5 HyperInt at useful `n` is expensive; the table may stall at small `n`, making the
  `Sup·δ` limit extrapolated rather than tight.

**#3 — A conditional Diophantine statement from the weight-7 `M_{0,10}` family (problem B, needs H).**
- *Statement to aim at.* An effective sequence with a *proven* worthiness `γ_{5,7}` for the pair
  `(ζ(5),ζ(7))`, and — if `γ_{5,7}>1` after any available denominator sharpening — the conclusion
  "at least one of ζ(5), ζ(7) is irrational" (BZ's own stated hope). Failing `γ>1`, a sharp
  worthiness number is still a result (the analog of BZ Theorem 1 one weight up).
- *Route.* From the sibling's `Q_n` (to `q₃₀`): (a) creative-telescoping recurrence (order 3–4) →
  characteristic polynomial → the four asymptotics `λ₁..λ₄`; (b) denominator from pole orders; (c)
  worthiness `γ = (c₁−c₀)/c₁`. The `I_n = I'_n + I''_n ζ(2)` split (BZ §12) isolates `I'_n ∈ ⟨1,ζ(5),ζ(7)⟩`.
- *Failure mode.* (i) The cell is **dihedrally rigid** (sibling: trivial stabiliser) — so, unlike ζ(5),
  there is **no Rhin–Viola group to sharpen denominators**; the worthiness is likely `<1` and the
  statement stays conditional-at-best. (ii) The rank-4 motive carries *two* parasitic even-weight
  contaminations, so even `γ>1` may only give `dim≥2` among three unknowns, not a clean dichotomy.
  (iii) The subleading-asymptotic "set ζ(2)=0" step needs the motivic justification, unproven here.

*Lower-risk fallbacks if the above stall:* problem G (det factorisation — a clean, self-contained
theorem) and problem A's purely-numerical half (a certified table, no proof) are near-certain
deliverables; problem E (enumeration extension) is a guaranteed finite result of independent interest.

### 6.c Skeptical notes — asserted-without-proof, repeated as fact

1. **The BZ rank-3 motive `gr_W M = ℚ(0)⊕ℚ(−2)⊕ℚ(−5)` is not proven.** BZ §4: "Computations of
   periods **suggest**" the rank-3 shape, and "The dimensions of `M` in middle weights **have not been
   rigorously established**." Only top/bottom/subleading weights are proven (`gr^W₈=0`). The clean
   "single period `ζ(5)+2ζ(3)ζ(2)`" narrative and the period matrices `periodmatrix1/2` lean on the
   unproven middle-weight structure. Treat the rank-3 picture as a well-supported conjecture (problem I).
2. **The printed integrality claims are literally false.** `dn-totsym` (`d_n⁵P_n ∈ ℤ`) and `incl`,
   "observed experimentally," are wrong by an exact factor **12 = 2²·3** — checkable against BZ's *own*
   printed `P₂ = 1190161/384` (`d₂⁵P₂ = 1190161/12 ∉ ℤ`). A downstream reader who repeats the
   integrality statement inherits the error. (Sibling result, verified against the paper.)
3. **The Weyl-group pattern is folklore, not theorem.** `W(A₄)=120, W(D₅)=1920, W(E₆)=51840`, then
   `Σ₇=W(A₆)=5040` for ζ(5): BZ Remark 4 itself calls the extension "a mystery," and the ζ(5) group
   `A₆` **breaks** the `A₄,D₅,E₆(→E₇,E₈)` extrapolation one might have guessed. "Rhin–Viola groups are
   Weyl groups, systematically" is an over-reading.
4. **"The method improves as dimension increases" is demonstrated only where it cannot matter.** Brown
   (21) proves the principle on ζ(2), where he states there is "(intentionally!) no possible new
   irrationality result." The multi-parameter *gain over the single-line group method* is
   **experimental/expected**; the thresholds behave well numerically but "It is not clear what to expect
   of the limit of the thresholds `ϑ_n`" (21-§9). The narrative should not be read as an established
   asymptotic advantage for higher-weight ζ.
5. **"Setting ζ(2)=0" is a priori meaningless.** BZ say so outright ("A priori this operation does not
   make sense"); it is justified only via motivic MZVs / cohomology — and the motivic-ity of the whole
   group `𝔊` is *itself* an open expectation (BZ §4: "It would be very interesting to prove that the
   entire group `𝔊` ... is also motivic"). The descent-to-ζ(3) and the parasitic-elimination rest on
   this scaffolding.
6. **Worthiness 0.86 is a comparison, not a bound, and does not touch irrationality.** BZ Theorem 1's
   "best possible when compared to any other known constructions" is comparative; `γ=0.866<1` proves
   nothing about ζ(5). The sibling's `sup γ = 0.86597135` (published point optimal) is `[COMP]` — a
   convincing hill-climb over 31,710 points + basin-hopping, **not a proof** that 0.866 is the true
   cone supremum; and it pertains to the *single-line* worthiness, orthogonal to Brown's `Sup²·δ`.
7. **Higher-dimensional transfinite diameters are mostly unknown.** 21-§5.4: "there are few results
   which establish the precise value of the transfinite diameter in higher dimensions ... for the
   rectangular case, very little seems to be known." The method's improvement story rests on *upper
   bounds* for `Sup`, sandwiched between polytopes — not exact values. Any claim of a sharp `Sup·δ` for
   `M_{0,n}` is currently out of reach analytically.
8. **Reverse caution — do not repeat Vasilyev as open.** Vasilyev's conjecture (`llm/24`, eq. `intro1`)
   is a **theorem for all `d`** (Zudilin 2003; three further proofs). It is sometimes cited as a deep
   open problem; it is not. There is no finite residue to close and no new result to be had there.

---

*End of memo. Primary sources: `/home/ubuntu/fable-episode-2/zeta-math-2/llm/{19,20,21,24,31,32}-*.md`
(LaTeX cross-checks under the matching `papers/<n>/`). Sibling connections:
`/home/ubuntu/fable-episode-2/zeta-math/README.md`, `worthiness/{RESULTS,CONJECTURE,PROOF_MECHANISM}.md`.*
