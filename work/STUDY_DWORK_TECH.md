# Survey: Dwork-congruence technology for the second-solution ratio gate

**Author:** mathematician-agent (River's zeta-irrationality program)
**Date:** 2026-07-24
**Discipline:** every citation carries an arXiv id and a paraphrase of the *fetched* statement. `[RECALLED-UNVERIFIED]` marks anything not fetched. Paywalled/unfindable is flagged, not guessed.

## The two targets

**(A) weight 3, classical Apéry ζ(3).** a_n = Σ C(n,k)²C(n+k,k)² (A005259); b_n the standard companion with b_n/a_n → ζ(3). Target congruence (numerically verified, not proved):
  p³·(b_n/a_n) ≡ b_a/a_a (mod p),  a = ⌊n/p⌋, p ≥ 7 (≈3 p-adic digits; p=5 exceptional via a_1=5).
Equivalently the two "rows": a_{ap+r} ≡ a_a·a_r (mod p) [proved Lucas, integral solution] and p³·b_{ap+r} ≡ b_a·a_r (mod p) [the OPEN second-solution row].

**(B) weight 5, Brown–Zudilin cellular ζ(5).** Integer Q_n (double binomial "sumQ"), companion P_n, Q_nζ(5) − 2P_n ~ cellular integral; both satisfy one order-3 recurrence, char. poly **4λ³ − 2368λ² − 188λ + 1** (confirmed in llm/20 line 102). Target: p⁵·(P_n/Q_n) ≡ P_a/Q_a (mod p), verified 272 descents, 0 failures, floor mod p^{2−κ}, κ = v_p C(2n,n). Q_n satisfies a PROVED Lucas congruence Q_{ap+r} ≡ Q_a·Q_r (mod p). Proving (B) closes a sharp denominator theorem for the BZ family.

**The crux (both targets).** The integral-solution Lucas congruence is well-trodden. The gate is the SECOND solution (log-solution / companion carrying harmonic sums): b_n resp. P_n. We need its Frobenius/Lucas-type congruence and the p^w normalisation (w=3 resp. 5).

---

## Local anchor: Lai–Sprang–Zudilin, ζ₂(5) (arXiv:2505.05005, llm/18)

FETCHED (full local text). This is a *2-adic Apéry-limit* construction, NOT a Dwork ratio-congruence. Technology actually used:
- Volkenborn integral ∫_{Z_p} f dt = lim p^{-n} Σ_{k<p^n} f(k) of a rational function R_n(t); the linear form S_n = ρ_{n,0} + ρ_{n,3}ζ₂(5).
- The **Δ-operator** valuation estimate (Sprang, Duke 2020; Lai, IJNT 2025): Δ(f) := min( inf_k v_p((f(k)−f(k₋))/(k−k₋)), 1+v_p(f(0)) ), with v_p(∫ f) ≥ Δ(f) − 1, and Δ(binom(t+j,n)) ≥ −⌊log n/log p⌋ (Lemma 7e). This is the p-adic-limit engine: it bounds v_p of a Volkenborn integral by a "leading-p-adic-digit-deletion" quantity k₋ — structurally a Dwork/Lucas digit operation.
- Denominators via Andrews transformation + Krattenthaler–Rivoal (Mem. AMS 2007) very-well-poised ₉V₈/₁₃V₁₂ → multiple sums.
- The coefficient recurrence (n+1)⁵ρ_{n+1} − 32(2n+1)(8n⁴+…)ρ_n + 2¹⁶n⁵ρ_{n−1}=0 has char. poly (λ−2⁸)² (double root; a MUM-type degeneration).
Relevance to us: LSZ do NOT prove a ratio congruence p^w(b_n/a_n)≡… ; they bound the *denominator* of the second solution ρ_{n,0} directly (Lemmas 16,18,19) via the Δ-operator and hypergeometric multi-sums. Their key citations for p-adic second-solution arithmetic: Beukers 2008 (Acta Math Sinica, p-adic L-values), Calegari 2005 (IMRN, math/0408214), Sprang 2020 (Duke), Lai 2025 (IJNT). See §5 below.

---

## 1. Beukers–Vlasenko, "Dwork crystals" I / II / III + "Frobenius structure and p-adic zeta values"

### 1b. Dwork crystals II — arXiv:1907.10390 (FETCHED, ar5iv)
- **Class:** constant terms of powers of a Laurent polynomial g(x)^k; periods of the hypersurface f=0; A-hypergeometric periods (coefficients of x^u f^{-k}); the module Ω_f of rational functions with prescribed pole order and its quotient Q_f(μ) by exact forms.
- **Main congruence (Thm 3.2, after Mellit–Vlasenko):** q(t)/q(t^p) ≡ γ_{p^s}(t)/γ_{p^{s-1}}(t^p) (mod p^s), γ_m = Σ_{k<m} b_k t^k truncations of the holomorphic period.
- **Corollary 4.4 (matrix/period form):** γ_m(μ) ≡ Λ_σ · σ(γ_{m/p}(μ)) (mod p^{ord_p(m)}). **Depth = p^{ord_p(m)}** (grows with the p-adic valuation of the level m — this is the source of "mod p^s" for a p^s-descent).
- **Hypothesis:** Hasse–Witt matrix β_p(μ) invertible (**ordinarity / unit-root nonvanishing**).
- **RATIOS / UNIT ROOTS — YES (this is the closest structural technology):** Remark 4.5: lim_{s→∞} γ_{p^s}(t_0)/γ_{p^{s-1}}(t_0) = the **unit root** of the zeta function of f=0. Elliptic-curve model: G_{p^s}(z_0)/G_{p^{s-1}}(z_0) is a p-adic Cauchy sequence → unit root λ ∈ Z_p^×. Theorem 2.3 gives the period-vector relation p_v = Λ_σ σ(p_v) (Cartier/Frobenius eigen-relation). BUT this is the ratio of the SAME holomorphic period across levels (→ unit root), NOT the b_n/a_n second-solution ratio.
- **Apéry / ζ_p:** NOT treated here.

### 1d. Beukers–Vlasenko, "Frobenius structure and p-adic zeta values" — arXiv:2302.09603 (FETCHED, ar5iv). **MOST RELEVANT PAPER FOUND.**
- **Class:** Calabi–Yau-type differential operators of order n with a MUM point; two concrete families — simplicial g=x_1+…+x_n+1/(x_1…x_n) giving L=θ^n−((n+1)t)^{n+1}(θ+1)…(θ+n), and hyperoctahedral g=Σ(x_i+1/x_i).
- **Frobenius structure (the central object):** on the standard MUM solution basis y_i = F_0 (log t)^i/i! + F_1(log t)^{i-1}/(i-1)! + … + F_i, the p-adic Frobenius 𝒜 acts by 𝒜(y_i(t^p)) = p^i Σ_{j=0}^i α_j y_{i-j}(t). **Theorems 1.4 (simplicial, p>n+1) and 1.5 (hyperoctahedral, p>n):** the constants α_1,…,α_{n-1} are explicit expansion coefficients of ratios of Morita's p-adic Γ_p, and **the limits of the Frobenius matrix entries are rational linear combinations of products of ζ_p(k), 1<k<n.** Hypotheses: L irreducible in Q(t)[θ]; n-th Hasse–Witt condition (ordinarity).
- **Quintic (n=4):** α_3 = −8ζ_p(3)/25 (matches Candelas–de la Ossa–van Straten conjecture up to a 5³ change of variable).
- **CRUX bearing:** This proves p-adic zeta values LIVE in the Frobenius matrix entries α_j that couple the second/higher log-solutions y_1,y_2,… to the holomorphic y_0 near a MUM point — precisely the ζ_p content our ratio b_n/a_n is chasing. HOWEVER: (i) they prove a p-adic LIMIT of Frobenius entries, NOT a finite mod-p Lucas/Dwork congruence on coefficients; (ii) they do NOT isolate y_1/y_0 as its own object; (iii) the classical Apéry ζ(3) operator is NOT among their two families (though it is the same CY-type/MUM shape). So: the ζ_p(3)/ζ_p(5) "why" is supplied here; the finite-descent congruence "how" is not.

*(Sub-sections 1a Dwork crystals I and 1c Dwork crystals III are placed after §5 below, where they were finalized — both are FETCHED and complete.)*

## 4. Malik–Straub, Straub, Mellit–Vlasenko, Beukers p-linear schemes (integral-solution Lucas + the one companion precedent)

### 4a. Malik–Straub, "Divisibility properties of sporadic Apéry-like numbers" — arXiv:1508.00297 (FETCHED via agent)
- **Class:** the finite list of *sporadic* Apéry-like sequences (Zagier's search). Includes the classical ζ(3) Apéry numbers A(n)=ΣC(n,k)²C(n+k,n)² and the ζ(2) numbers B(n)=ΣC(n,k)²C(n+k,k).
- **Theorem 3.1:** every sporadic Apéry-like sequence satisfies the full **Lucas congruence mod p**: A(ap+r) ≡ A(a)A(r) (mod p). Proof by McIntosh constant-term method; (η), s₁₈ need finer analysis.
- **Crux — NO.** Only the single integral solution. (B(n) is an independent sporadic solution, not a harmonic companion.)

### 4b. Henningsen–Straub, "Generalized Lucas congruences and linear p-schemes" — arXiv:2111.08641 (FETCHED via agent)
- **Definition (linear p-scheme):** integer states A₀=A, A₁,…,A_m with A_i(pn+k) ≡ Σ_j α_{i,j}^{(k)} A_j(n) (mod p^r). Auxiliary states are genuine integer sequences.
- **Prop 1.3:** A satisfies classical Lucas mod p ⇔ it is a single-state (m=0) linear p-scheme. **Thm 4.1:** multi-state generalized Lucas for constant-term sequences A(n)=ct[P^n Q].
- Proved **mod p**; definition allows p^r. **Crux — NO**, but the multi-state framework is exactly one in which a companion b_n could ride as an extra integer state (not instantiated here).

### 4c. Beukers, "p-Linear schemes for sequences modulo p^r" — arXiv:2211.15240 (FETCHED, verified myself). **THE ONE COMPANION PRECEDENT.**
- **Definition 1.2 (p-linear scheme mod p^r):** a vector a_k=(a_{1,k},…,a_{s,k})^t and integer s×s matrices M_ℓ with **a_{kp+ℓ} ≡ M_ℓ a_k (mod p^r)** for ℓ∈{0,…,p−1}, k≥0. (Lucas = s=1,r=1.)
- **Theorem 1.4 (Gessel 1982), verified verbatim:** companion **A′_k = Σ_{m=0}^k C(k,m)²C(m+k,m)²·(1/(m+1)+…+1/k)** (harmonic-weighted, WEIGHT 1), and
  **A_{kp+ℓ} ≡ A_ℓ A_k + p·A′_ℓ·k·A_k (mod p²).** [index placement of the p-term is per the ar5iv small-model read; the mod-p² depth and the A′ definition are confirmed.]
  Multiplying through by (kp+ℓ) presents {A_k, k·A_k} as a 2-state p-linear scheme.
- Higher-p^r machinery (Thm 3.1 ct[x^u g^k]; Thm 4.1 coeffs of Q/P^ρ; example {2^k,k·2^k} mod p²) is demonstrated on OTHER sequences; the Apéry harmonic companion is **only reached mod p²**, not p³.
- **Crux — YES (partial, and the key precedent).** This is the unique published congruence for a harmonic companion of the Apéry numbers. But: (i) A′ is the WEIGHT-1 harmonic companion (single 1/m harmonic sum), whereas our b_n is the WEIGHT-3 companion (carries H^{(3)}); (ii) depth stops at p². Gessel's statement is essentially the **first parameter-derivative** of the a-Lucas congruence: differentiate A_{kp+ℓ} ≡ A_ℓA_k once in a Pochhammer/ε deformation and the O(p) term produces the weight-1 companion. Our target (A) needs the p³ level ⇔ the **third** ε-derivative (weight 3) — precisely the ε-deformation Beukers/LSZ use elsewhere (cf. llm/18 Lemma 17 ⁹V₈(ε), Lemma 18 d³/dε³ giving the −5 = −(2+3) valuation).

### 4d. Mellit–Vlasenko, "Dwork's congruences for constant terms of powers of a Laurent polynomial" — arXiv:1306.5811 (FETCHED via agent)
- **Class:** b_n = [Λ(x)^n]₀, constant term of powers of Λ ∈ Z_p[x^±].
- **Theorem 1 (hypothesis: Newton polytope of Λ has the origin as its ONLY interior integral point):** with f_s(X)=Σ_{n<p^s} b_n X^n, the Dwork ratio congruence **f_{s+1}(X)f_{s−1}(X^p) ≡ f_s(X)f_s(X^p) (mod p^s)**, i.e. f(X)/f(X^p) ≡ f_s(X)/f_{s−1}(X^p) (mod p^s). Depth **mod p^s**.
- **Crux — NO.** Ratio of truncated g.f.s of ONE (holomorphic) sequence; no second/log solution. This is the engine behind Dwork crystals II §1b.

### 4e. Straub, "Multivariate Apéry numbers and supercongruences of rational functions" — arXiv:1401.0854 (FETCHED via agent)
- **Class:** Taylor coefficients of rational functions; classical Apéry A(n,n,n,n) is the diagonal of 1/((1−x₁−x₂)(1−x₃−x₄)−x₁x₂x₃x₄).
- **Thm 3.2 (Beukers–Dwork-type supercongruence):** ℓ≥2 ⇒ A(p^r n) ≡ A(p^{r−1}n) (mod p^{2r}); and if max λ_j ≤ 2, mod p^{3r} (p≥5). So classical Apéry: **A(p^r m) ≡ A(p^{r−1}m) (mod p^{3r})**, p≥5.
- **Crux — NO.** Integral solution only. (This is the strong "a-row"/holomorphic supercongruence — the well-trodden side.)

**Cluster 4 verdict:** integral rows (a_n, Q_n) fully covered (4a Lucas mod p; 4e supercongruence mod p^{3r}). The ONLY existing second-solution/companion congruence is Gessel via Beukers 4c — weight-1 companion, mod p². Nothing in the literature states the weight-3 (target A) or weight-5 (target B) companion Lucas congruence.

## 2. Delaygue–Rivoal–Roques + mirror-map integrality (the log-ratio Frobenius congruence — closest formal technology)

The mirror map / canonical coordinate **q(z) = z·exp(y₁/y₀) = z·exp(G/F)** is the exponentiated second-solution ratio; y₁ = F·log z + G, y₀ = F. Our b_n/a_n is a truncation of y₁/y₀ = log z + G/F. This cluster is the natural home for "congruences of the ratio", so its exact deliverable matters.

### 2a. Delaygue–Rivoal–Roques, "On Dwork's p-adic formal congruences theorem and hypergeometric mirror maps" — arXiv:1309.5902 (Mem. AMS 246) (FETCHED via agent; Thm 4 from PDF)
- **Class:** univariate generalized hypergeometric operators L_{α,β} = ∏(θ+β_i−1) − z∏(θ+α_i), α,β ∈ ℚ∖ℤ_{≤0}. Holomorphic F_{α,β}=_rF_{s−1}; second solution ω₂ = G+log(z)F; q_{α,β}=z·exp(G/F).
- **Theorem 2 (the engine, fixed p):** a **Frobenius formal congruence for the log-ratio**: G_{⟨t⁽¹⁾α⟩,…}/F(C′z^p) − p·G_{⟨tα⟩,…}/F(C′z) = p·Σ_k R_{k,b}(t) z^k with R_{k,b} in an algebra of ℤ_p-valued functions — generalizing **Dwork's Theorem B**: G_{𝔇p(α),𝔇p(β)}/F(z^p) − p·G_{α,β}/F(z) ∈ p·z·ℤ_p[[z]].
- **Theorem 3 + Cor 2/3:** N-integrality of the mirror map q_{α,β} and of roots exp(S/𝔫).
- **Theorem 4 (abstract Dwork formal congruence, §5, eq 5.1):** for Dwork-tower sequences A_r(n), g_r(n), under divisibility hypotheses, S_r(a,K,s,p,m) := Σ_j [A_r(a+(K−j)p)A_{r+1}(j) − A_{r+1}(K−j)A_r(a+jp)] ∈ p^{s+1} g_{r+s+1}(m) A. **Corollary 1:** Dieudonné–Dwork bridge exp(f)∈1+zℤ_p[[z]] ⇔ f(z^p)−pf(z)∈pzℤ_p[[z]].
- **CRUX — NO Lucas congruence on q's coefficients.** Delivers (i) integrality of the mirror map, (ii) a z↔z^p **Frobenius congruence for the two-solution ratio G/F** (Thm 2 / Thm B) — but it is *consumed by Dieudonné–Dwork to yield integrality*, never stated as a coefficient recursion q_{ap+r}≡… The single power of p in "−p·G/F" matches a **weight-1** log-solution; our targets are weight 3 / 5.

### 2b. Delaygue, "Criterion for the integrality of the Taylor coefficients of mirror maps in several variables" — arXiv:1108.4352 (FETCHED via agent)
- **Class:** multivariate factorial-ratio series F_{e,f}=Σ (∏(e_i·n)!/∏(f_j·n)!)z^n; mirror maps q_{e,f,k}=z_k·exp(G/F).
- **Theorem 1 (integrality dichotomy):** via Landau function Δ_{e,f}(x)=Σ⌊e_i·x⌋−Σ⌊f_j·x⌋; if Δ≥1 on 𝒟 then q∈z_kℤ[[z]]; if Δ=0 somewhere, non-integral. **Theorem 4:** a formal-congruence tool generalizing Dwork/Krattenthaler–Rivoal.
- **CRUX — NO.** Integrality of mirror maps only.

### 2c. "A note on the integrality of mirror maps" — arXiv:2410.04293 (FETCHED via agent)
- **Class:** A-hypergeometric (GKZ) systems, parameter β=0. **Theorem 4.1:** exp G_k(λ) has integral coefficients (mirror-map integrality), via Dieudonné–Dwork + multinomial congruences (Prop 3.1: divisibility by p^{a−b}; Prop 3.2: (pe choose pe_i)−(e choose e_i) divisible by p^{a+1}).
- **CRUX — NO.** Integrality; the mod-p congruences are internal multinomial facts, not Lucas congruences on q.

## 3. Vargas-Montoya — strong Frobenius structures (Lucas only for the holomorphic solution)

### 3a. "Maximal Unipotent Monodromy, congruences à la Lucas and algebraic independence" — arXiv:2103.15192 (FETCHED via agent)
- **Class:** f(z)∈1+zℚ[[z]], D-finite, annihilated by (i) an operator with **strong Frobenius structure** for all p in an infinite set S, and (ii) a Fuchsian MUM operator 𝒟 (regular singular at 0, all exponents 0). p-Lucas ⇔ f|_p(z)=A_p(z)·f|_p(z^p), A_p=Σ_{n<p}(a(n) mod p)z^n.
- **Theorem 1:** for such f, for a.e. p∈S, f|_p(z)=A_p(z)·f|_p(z^{p^{l_p}}) with A_p∈𝔽_p(z) of bounded height; under Λ_p^{l_p}(f|_p)=f|_p, genuine p-Lucas. **Theorem 2:** algebraic independence of f_r=Σ(−1/(2n−1))C(2n,n)^r z^n.
- **CRUX — NO for the ratio.** The Lucas congruence applies **ONLY to the holomorphic power-series solution** f∈1+zℚ[[z]]. Log-solutions and y₁/y₀ are explicitly outside the framework. (Directly answers survey question 3: the strong-Frobenius machinery gives Lucas for the holomorphic solution only.)

### 3b. "p-Integrality of canonical coordinates" — arXiv:2306.03495 (FETCHED via agent). [The paper the task's warning flags.]
- **Class:** order-n≥2 operators L/ℚ(z), **MUM at 0**, with p-integral strong Frobenius structure Φ∈M_n(ℤ_p[[z]]), det Φ≠0, δΦ = A(z)Φ − pΦA(z^p). y₀=𝔣, y₁=𝔣 log z+𝔤; **canonical coordinate q(z)=exp(y₁/y₀)=z·exp(𝔤/𝔣)**.
- **Theorem 1.1:** y₀∈1+zℤ_p[[z]]; and **if |φ_{1,1}(0)|=1 then q(z)=exp(y₁/y₀)∈zℤ_p[[z]]** — p-integrality of the second-solution ratio itself. **Cor 1.1:** irreducible order-4 MUM CY operator ⇒ q∈ℤ[1/N][[z]].
- **CRUX — NO.** Purely p-adic **INTEGRALITY** of the correct object (the second-solution ratio), **no Dwork/Lucas congruence mod p or p^s anywhere**. This is the exact "integrality ≠ congruence" gap: the strong-Frobenius machine controls the ratio's denominators but does not deliver q_{ap+r}≡… .

## 5. p-adic Apéry limits / classical second-solution congruences — DOES TARGET (A) EXIST? (Answer: NO)

### 5a. Chamberland–Straub, "Apéry Limits: Experiments and Proofs" — arXiv:2011.03400 (FETCHED via agent)
- Apéry limit := lim B(n)/A(n), B the companion solution of a common 3-term recurrence, via Casoratian (Lemma 4), Poincaré asymptotics (Thm 6). **NO p-adic content** (no valuations, no ζ_p). Archimedean conjectures only (e.g. Conj 9: ΣC(n,k)^d companion ratio → ζ(2)/(d+1)). Not target (A).

### 5b. Beukers 1985/1987 classical Apéry congruences (PAYWALLED; statements from Osburn–Sahu survey arXiv:0906.3413)
- **1985 (Beukers' conjecture; Gessel r=1, Coster p≥5):** A_{mp^r} ≡ A_{mp^{r−1}} (mod p^{3r}) for A_n=ΣC(n,k)²C(n+k,k)². This is the **first-solution supercongruence** (= our proved a-row, strengthened). **1987 (Ahlgren–Ono):** A_{(p−1)/2} ≡ a(p) (mod p²), a(p) = Fourier coeff. of η(2z)⁴η(4z)⁴ ∈ S₄(Γ₀(8)).
- **Both concern ONLY the first solution A_n.** No companion b_n, nothing → ζ_p(3). Target (A) is NOT here.

### 5c. Beukers, "Irrationality of some p-adic L-values" — arXiv:math/0603277 (= Acta Math. Sinica 2008) (FETCHED via agent)
- Irrationality of ζ_p(2) (p=2), ζ_p(3) (p=2,3). Technology deliberately **elementary**: Padé/continued-fraction convergents to Bernoulli-number Laurent series (Stieltjes), criterion Prop 2.1. **No Frobenius, no Volkenborn, no Dwork.** Approximations are not the classical A_n/companion; no b_n/a_n→ζ_p(3).

### 5d. Calegari, "Irrationality of certain p-adic periods for small p" — arXiv:math/0408214 (FETCHED via agent)
- Thm 3.3 ζ_2(3)∉ℚ; Thm 3.4 ζ_3(3)∉ℚ; Thm 4.2 2-adic Catalan. **ζ_p(5) NOT reached** (exponent θ=0.908<1 fails). Technology = **overconvergent p-adic modular forms + p-adic Eisenstein families** (Thm 2.3; Buzzard continuation); the period is the constant term of a p-adic Eisenstein series. NOT Frobenius/Dwork/holonomy. Builds a "2-adic analogue of Apéry's sequences" but not the classical numbers; no congruence (A).

### 5e. VERDICT on existence of (A): **OPEN.** Neither target (A) nor the p-adic limit b_n/a_n→ζ_p(3) for the classical order-3 Apéry operator is proved or even stated anywhere found. The *phenomenon* is the **Candelas–de la Ossa–van Straten conjecture** (ζ_p(k) in the MUM Frobenius matrix), proved by Beukers–Vlasenko (2302.09603, Adv. Math. 480 (2025)) **only for simplicial/hyperoctahedral CY hypersurface families** — a paper that never mentions Apéry and does not cover the classical operator. (Adjacent 2026 work: Bai–Lee–Pomerleano arXiv:2601.01654, Frobenius structure on CY-3-fold quantum connections, p-adic Gamma class, p>3 — not the target.)

### 1a. Dwork crystals I — arXiv:1903.11155 (IMRN 2021) (FETCHED via agent)
- **Class:** Laurent polynomial f(x)=Σf_u x^u, Newton polytope Δ; module Ω_f, Dwork module W_f=Ω_f/dΩ_f; running objects = expansion coefficients of 1/f = constant terms of powers of g (f=1−tg) = periods of toric hypersurfaces. Central object: **Hasse–Witt matrix** β_m.
- **Theorem 4.3 (+Rmk 4.6):** unit-root decomposition under β_p(μ) invertible (ordinarity): Ω̂_f(μ) ≅ Ω_f^{(1)}(μ) ⊕ F₁(μ), C_p(Ω̂_f) ⊂ Ω_{f^σ}^{(1)} + pF₁^σ.
- **Theorem 5.3 (matrix Dwork congruence):** β_{p^{s+1}}σ(β_{p^s})⁻¹ ≡ β_{p^s}σ(β_{p^{s−1}})⁻¹ (mod p^s); limits Λ_σ (unit-root Frobenius matrix), N_δ (Gauss–Manin). Depth **mod p^s**.
- **CRUX — essentially NO.** The unit root is a ratio lim F_{p^s}/F_{p^{s−1}} of consecutive truncations of the SAME holomorphic period, not the holomorphic-to-log ratio. No p^w-normalized second-period congruence. No ζ/Apéry (example = Legendre elliptic family).

### 1c. Dwork crystals III — arXiv:2105.14841 (IMRN 2023) (FETCHED via agent). **THE SINGLE MOST RELEVANT PAPER for the gate.**
- **Class:** CY family f=1−tg(x), g∈Z[x] with **reflexive** Newton polytope (0 unique interior point). Holomorphic period F(t)=Σ g_n t^n, g_n = **constant term of g(x)^n** (so a_n and Q_n are exactly of this type). Filtration F_k(μ) = "k-th formal derivatives" (coeff a_u divisible by gcd(u_1,…,u_n)^k).
- **Prop 5.11 (leading-solution supercongruences):** a_{p^s m} ≡ Λ σ(a_{p^{s−1}m}) (mod p^{sk}) under the k-th Hasse–Witt condition; k=2 ⇒ mod p^{2s}. **Theorem 1.2:** F(t)/F(t^σ) ≡ F_{mp^s}(t)/F_{mp^{s−1}}(t^σ) (mod p^s).
- **§6:** the ζ(3) **Apéry numbers a_n appear explicitly** as the diagonal of Straub's rational function 1/((1−x₁−x₂)(1−x₃−x₄)−x₁x₂x₃x₄), with Straub's mod p^{3s} supercongruence cited — but this is the holomorphic diagonal, NOT b_n.
- **THE SECOND SOLUTION IS CONSTRUCTED (§9, Prop 9.1):** the order-2 Picard–Fuchs operator θ²y − Bθy − Ay=0 has holomorphic F(t) and **logarithmic second solution F(t)log t + G(t) with G(t) carrying harmonic sums — exactly the b_n structure**. (Hypercubic: F=ΣC(2k,k)^n t^{2k}, G=ΣC(2k,k)^n(Σ_{j=k+1}^{2k}1/j)t^{2k} — WEIGHT-1 harmonic; simplicial similarly.)
- **p^w NORMALIZATION EXPLAINED — Prop 7.7 / eq (22)-(23) / Λ₀:** the Cartier matrix on the rank-2 quotient is Λ=YΛ₀(Y^σ)⁻¹ with **Λ₀ = [[α₀,α₁],[0,pα₀]]**, α₀=1, α₁=log(γ^{p−1}). **The second-solution Frobenius eigenvalue carries exactly ONE extra factor of p per Hodge/F_k step** — this is the structural source of the p^w in our targets (w = number of weight steps: 3 for ζ(3), 5 for ζ(5)).
- **Corollary 7.11 (closest published analog to our target):** mirror map q(t)=t·exp(G/F) ∈ Z_p[[t]], equivalently (Dieudonné–Dwork, Lemma 7.10) **G/F − (1/p)·G(t^σ)/F(t^σ) ∈ Z_p[[t]]** — a congruence on the second-to-first ratio (formal-group log) WITH the 1/p Frobenius twist. But **p-INTEGRALITY only**, not p^w·b_{ap+r} ≡ b_a·a_r (mod p).
- **Theorem 7.3 (excellent Frobenius lift):** for g completely symmetric, a UNIQUE excellent lift σ (q^σ=γ^{p−1}q^p) with C_p(1/f) ≡ (F/F^σ)(1/f^σ) mod **p²F₂^σ** — one power of p deeper than the generic pF₁.
- **Conjecture 7.5 (OPEN — the authors could not prove it, "one of the original motivations"):** the RATIO congruence F/F^σ ≡ F_{mp^s}/F_{mp^{s−1}}(t^σ) holds **mod p^{2s}** (for hyperoctahedral m=2, simplicial m=n+1). No mod-p^{2s} version of the *ratio* congruence is proved.
- **CRUX — YES, this is exactly the gate, and it is OPEN.** BV III supplies (i) the second log-solution G (harmonic sums = b_n species), (ii) the p^w normalization mechanism (Λ₀ eigenvalue = p·unit), (iii) p-integrality of the ratio (Cor 7.11), (iv) the excellent-lift depth-p² mechanism. What it does NOT supply — and explicitly leaves conjectural — is any mod-p^s congruence deepening on the ratio/second solution (Conj 7.5). And its second-solution theory is developed only at **rank-2 (order-2)** for completely-symmetric hypergeometric families; the **sporadic ζ(3) a_n and the order-3 ζ(5) Q_n/P_n are not worked**.

---

## 6. The crux, distilled: what covers the SECOND solution

Reading across all clusters, the second-solution / companion-ratio congruence sits in a well-mapped gap:

| Technology | What it gives on the SECOND solution / ratio | Depth | Gap to our target |
|---|---|---|---|
| Gessel/Beukers p-linear scheme (2211.15240, Thm 1.4) | genuine congruence A_{kp+ℓ} ≡ A_ℓA_k + p·k·A_ℓ′A_k for the **weight-1** harmonic companion A′ | mod p² | wrong weight (need 3,5); depth stops at p² |
| Dwork crystals III (2105.14841): Λ₀, Cor 7.11 | constructs log-solution G (harmonic sums); proves **p-integrality** of q=exp(G/F); p^w from Λ₀ eigenvalue p·unit; excellent lift to mod p² | integrality; leading-ratio mod p^s (Thm 1.2) | the second-solution **congruence** is Conj 7.5 = OPEN; only order-2, completely-symmetric families |
| Delaygue–Rivoal–Roques (1309.5902) Thm 2/Thm B | Frobenius formal congruence G/F(z^p) − p·G/F(z) ∈ pzZ_p[[z]] | formal (z↔z^p) | consumed into integrality; not a coefficient Lucas congruence; weight 1 |
| Vargas-Montoya 2306.03495 (Thm 1.1) | p-integrality of canonical coordinate q=exp(y₁/y₀) | integrality | no congruence at all |
| Vargas-Montoya 2103.15192 (Thm 1) | Lucas — **holomorphic solution only** | mod p | never the log-solution/ratio |
| Frobenius structure & ζ_p (2302.09603) | ζ_p(k) IS the limit of MUM Frobenius entries α_k (weight k) | p-adic limit | limit, not finite-descent congruence; simplicial/hyperoctahedral CY only, not Apéry |

**Consensus:** (i) the integral-solution row is fully covered (Malik–Straub Lucas mod p; Straub/Coster mod p^{3r}; Dwork crystals Prop 5.11 mod p^{sk}); (ii) the SECOND-solution row is nowhere proved as a Lucas/Dwork congruence — the closest is Gessel's mod-p² weight-1 companion and Cor 7.11's integrality, and the honest deepening is exactly BV's OPEN Conjecture 7.5; (iii) the p^w normalization is explained (Λ₀ eigenvalue = p·unit root, one p per weight step; ζ_p(w) is the weight-w Frobenius entry).

---

## VERDICT TABLE

Legend: **Covers** = the theorem, as stated, proves the target (or a strictly stronger statement). **Adaptable** = would prove it after a specified, plausible adaptation. **Blocked** = a stated obstruction prevents it.

| # | Theorem (arXiv) | Target (A) p³(b_n/a_n)≡b_a/a_a mod p | Target (B) p⁵(P_n/Q_n)≡P_a/Q_a mod p |
|---|---|---|---|
| Malik–Straub Lucas (1508.00297 Thm 3.1) | **Blocked**: integral solution only; a-row only (a_{ap+r}≡a_a a_r ✓, but nothing on b) | **Blocked**: gives Q-row Lucas (already proved); silent on P |
| Straub supercong. (1401.0854 Thm 3.2) | **Blocked**: a_{p^r m}≡a_{p^{r−1}m} mod p^{3r}, integral solution only | **Blocked**: integral-solution supercong. only; BZ diagonal not of the covered rational-function shape |
| Mellit–Vlasenko (1306.5811 Thm 1) | **Adaptable(weak)**: gives f/f(X^p)≡f_s/f_{s−1} mod p^s for ct-sequences; adapt = deform Λ→Λ_ε so ct=a_n(ε), b_n=∂_ε^3, extract — but only holomorphic ratio proved | **Adaptable(weak)**: same, needs a Laurent-poly ct-representation of Q_n(ε); Q_n IS a ct (§ llm/20 eq Q_n) but P_n as ∂_ε^5 is unproven |
| Beukers p-linear scheme + Gessel (2211.15240 Thm 1.4) | **Adaptable**: proves the weight-1 companion A′ congruence mod p²; adapt = extend the vector scheme {a_n,…,b_n} to weight-3 & push depth to reach p³·b mod p. Nearest scaffolding | **Adaptable**: same framework; needs weight-5 states + the κ=v_p C(2n,n) correction; order-3 recurrence enlarges the state vector |
| Dwork crystals I (1903.11155 Thm 5.3) | **Blocked**: unit-root ratio of SAME period; no log-solution | **Blocked**: same |
| Dwork crystals III (2105.14841 Cor 7.11, Λ₀, Conj 7.5) | **Adaptable / at the frontier**: constructs G (b_n species), gives p^w from Λ₀, proves integrality of exp(G/F); the target ≈ coefficient-Lucas form of OPEN Conj 7.5 specialized to the sporadic ζ(3) operator. Adapt = prove the mod-p ratio-descent BV leave open, for order-2 sporadic | **Blocked (for now)**: BV's second-solution/excellent-lift theory is rank-2 (order-2) & completely-symmetric only; BZ is order-3, not of that family |
| Delaygue–Rivoal–Roques (1309.5902 Thm 2/4) | **Adaptable(weak)**: Frobenius log-ratio congruence G/F(z^p)−pG/F(z)∈pz Z_p; adapt = keep it as a coefficient congruence instead of exponentiating, iterate weight-3. Hypergeometric only | **Blocked**: hypergeometric L_{α,β} class; BZ pair is not in it |
| Delaygue 1108.4352 / note 2410.04293 | **Blocked**: mirror-map INTEGRALITY only | **Blocked**: same |
| Vargas-Montoya canonical coords (2306.03495 Thm 1.1) | **Blocked**: integrality of exp(y₁/y₀), no congruence | **Blocked**: same (and needs strong Frobenius structure input) |
| Vargas-Montoya MUM Lucas (2103.15192 Thm 1) | **Blocked**: Lucas for holomorphic solution only | **Blocked**: same |
| Frobenius structure & ζ_p (2302.09603 Thm 1.4/1.5) | **Adaptable(conceptual)**: proves ζ_p(k) = MUM Frobenius entry α_k — the "why" of p^w and ζ_p(3); but a p-adic LIMIT, and for simplicial/hyperoctahedral CY, not the order-3 Apéry operator | **Adaptable(conceptual)**: same; ζ_p(5)=α_5 needs order≥6 local, whereas BZ is order-3 → the p⁵ is a global/connection weight, harder |

---

## THE TWO ROUTES

### Route for (A) — ε-deformed Dwork/Gessel descent (weight-3 lift of Gessel's mod-p² companion)
The one published second-solution congruence is Gessel's A_{kp+ℓ} ≡ A_ℓA_k + p·k·A_ℓ′A_k (mod p²) (Beukers 2211.15240 Thm 1.4), where A′ is the **weight-1** harmonic companion — structurally the FIRST ε-derivative of the a-Lucas congruence. Our b_n is the **weight-3** companion, i.e. (up to normalization) the THIRD ε-derivative in a Pochhammer/creative-microscoping deformation a_n(ε) = ct[Λ_ε^n] (exactly the ⁹V₈(ε)/d³ε mechanism of llm/18 Lemmas 17–18, and the F_k filtration of Dwork crystals III where each level costs one power of p). So: (1) write a_n = ct[g(x)^n] (Dwork crystals III §6 gives the reflexive Laurent polynomial) and deform to a_n(ε); (2) apply the Mellit–Vlasenko / Dwork-crystal ratio congruence to the deformed holomorphic family to get a mod-p^s congruence carrying ε; (3) take ∂_ε³|_{ε=0} — the three derivatives land the weight-3 pole and multiply the modulus scaling by p³ (Λ₀ eigenvalue = p·unit per level), yielding p³·b_{ap+r} ≡ b_a·a_r (mod p). This is the coefficient-Lucas realization of Beukers–Vlasenko's OPEN Conjecture 7.5 specialized to the sporadic ζ(3) operator; the p=5 exception (a_1=5) is exactly a Hasse–Witt/ordinarity failure at the excellent lift.

### Route for (B) — multi-state p-linear scheme on the proved Q-Lucas base, weight-5, with the C(2n,n) correction
Q_n has a proved Lucas congruence and an explicit double-binomial constant-term form (llm/20 eq Q_n = Σ C(n+k₁,n)C(n,k₁)²Σ C(n+k₂,n)C(n,k₂)²C(n+k₁+k₂,n)). Build a Beukers/​Henningsen–Straub **vector p-linear scheme mod p^r** (2211.15240 Def 1.2, 2111.08641) whose state vector starts from Q_n and its shifts {Q_n, nQ_n, …} and adjoins the companion states up to the weight-5 harmonic level that assembles P_n; the order-3 recurrence (char. poly 4λ³−2368λ²−188λ+1) fixes the finite number of states. The p⁵ prefactor is five applications of the Λ₀-type one-p-per-weight scaling, and the empirical "floor mod p^{2−κ}, κ=v_p C(2n,n)" is precisely the central-binomial Hasse–Witt correction (p | C(2n,n) ⇔ a carry in base p) that must enter the scheme's matrices. The obstruction beyond (A): BZ is order-3 and NOT a completely-symmetric hypergeometric CY family, so Dwork crystals III's excellent-lift theory does not apply off the shelf; and weight 5 exceeds the order-3 local log-depth (max 2), so the p⁵ is a **connection/global** weight — the scheme must be built by hand from the sumQ representation and the proved Q-Lucas rather than inherited from a local MUM Frobenius structure. This is strictly harder than (A); (A) should be proved first as the template.

