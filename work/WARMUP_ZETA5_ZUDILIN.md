# Warmup: Zudilin (2002), "Arithmetic of linear forms involving odd zeta values"

Paper: `llm/04-zudilin-2002-arithmetic-of-linear-forms.md` (math/0206176v2; J. Théorie
Nombres Bordeaux 16:1 (2004), 251–291). LaTeX source: `papers/04-zudilin-2002-arithmetic-of-linear-forms/rvbr.tex`.

Goal of this warmup: reproduce, in exact arithmetic, the Section 8 construction proving
that at least one of ζ(5), ζ(7), ζ(9), ζ(11) is irrational (Theorem 3), and verify the
arithmetic and asymptotic bookkeeping.

Discipline labels: [PROVED] / [VERIFIED n≤N] / [RECALLED-UNVERIFIED]. Finite checks are
evidence, never proof.

All computation in Mathematica (exact rationals) via the Wolfram MCP session; recurrence via a
standalone `math -noprompt` stdin kernel with RISC HolonomicFunctions.

## Status summary

| Task | Result |
|------|--------|
| T1 construction + exact expansion | ✅ exact A₅,A₇,A₉,A₁₁,A₀ for n=1..6; direct-sum anchor agrees 89–95 digits |
| — paper typo | ✅ **found**: (eq:8.7) omits the very-well-poised factor (h₀+2t) (present in eq:8.2); benign |
| T2 denominator lemmas | ✅ Lemma 19 Δ=D₃₅ₙ³D₃₄ₙD₃₃ₙ⁸/Φ clears all coeffs, n=1..6; ν_p bound holds (slack ≥1) |
| T3 asymptotics | ✅ C₀=227.5801964 (exact match); C₂≈226.23 (paper 226.24944, ~4 digits); C₀>C₂ ⇒ irrationality |
| T3 recurrence | ⚠️ method validated on Apéry (order 2, −λ²+34λ−1); actual r=3,q=13 CT crashes the RISC kernel — order not extracted; char-poly roots obtained from saddle points |
| T4 Dwork/Lucas | ✅ verdict NO — ord_p(A₀/A₅) grows (≤−5), no p⁵ descent |

---

## T1. The construction (Section 8, Theorem 3)

### Parameters (read from the paper, lines 1294–1337 of the md / §8 of rvbr.tex)

- `r = 3`, `q = 13` (both odd, q ≥ r+4). Linear form is in `1, ζ(5), ζ(7), ζ(9), ζ(11)`
  (= ζ(r+2), …, ζ(q-2)).
- Directions η = (η₀; η₁,…,η₁₃) = (91; 27,27,27, 29,30,31,32,33,34,35,36,37,38),
  i.e. η₁=η₂=η₃=27 and η_j = 25+j for j=4,…,13.
- `h₀ = 91 n + 2`,  `h_j = η_j·n + 1` for j=1,…,13  (eq:8.13).

### Rational function and linear form

Very-well-poised rational function (eq:8.2):

    R̃(t) = (h₀+2t) · Γ(h₀+t)^r ∏_{j=1}^q Γ(h_j+t)  /  [ Γ(1+t)^r ∏_{j=1}^q Γ(1+h₀−h_j+t) ]

Arithmetic normalization N = ∏_{j=r+1}^q (h₀−2h_j)!  /  ∏_{j=1}^r (h_j−1)!² ; set R(t) = N·R̃(t).
Linear form (eq:8.4/8.6), with r=3:

    F(h) = (1/(r−1)!) Σ_{t=1−h₁}^∞ R^{(r−1)}(t) = (1/2) Σ_{t=1−h₁}^∞ R''(t).

Partial-fraction expansion R(t) = Σ_{j=r+1}^q Σ_{k=h_j}^{h₀−h_j} B_{jk}/(t+k)^{j−r}, with
B_{jk} = coeff of 1/(t+k)^{j−r} (from Apart). Then
    F(h) = Σ_{j=r+1}^q A_{j−1} ζ(j−1) − A₀,
    A_{j−1} = C(j−2, r−1) Σ_k B_{jk},
    A₀ = Σ_j C(j−2,r−1) Σ_k B_{jk} Σ_{l=1}^{k−h₁} 1/l^{j−1}.
Surviving coefficients: A₅, A₇, A₉, A₁₁ (all even-zeta and ζ(3) coefficients vanish exactly).

### DISCREPANCY FOUND (benign typo in the paper) [VERIFIED]

Equation (eq:8.7) — the definition of R(t) — **as literally printed in both the published
LaTeX (`rvbr.tex` lines 2494–2506) and the md** OMITS the very-well-poised factor `(h₀+2t)`
that appears in R̃ (eq:8.2). The factor is required:

- It is the *only* factor that is antisymmetric under t ↦ −t−h₀, so it is what makes the
  symmetry (eq:8.5) `R̃(−t−h₀) = −R̃(t)` hold and thereby forces the EVEN-zeta coefficients
  to vanish (Lemma 19 proof: B_{jk} = (−1)^j B_{j,h₀−k}).
- Numerical test at n=1 (Wolfram): with (h₀+2t) included, ζ(3),ζ(4),ζ(6),ζ(8),ζ(10),ζ(12)
  coefficients are exactly 0 and only ζ(5),ζ(7),ζ(9),ζ(11) survive — as Theorem 3 requires.
  With (h₀+2t) OMITTED (i.e. eq:8.7 read literally), the parities flip: the EVEN zetas
  ζ(4),ζ(6),ζ(8),ζ(10),ζ(12) survive and the odd ones vanish — wrong for Theorem 3.

Conclusion: (eq:8.7) should read R(t) = (h₀+2t)·[the printed product]; equivalently
R = N·R̃ with R̃ from (eq:8.2). All computations below use the correct R WITH the factor.
This is a transcription slip, not a mathematical error — the rest of §8 (8.2, 8.5, 8.6) is
consistent with the factor present.

### n=1..6 verification [VERIFIED n≤6]

For each n I computed the EXACT rational coefficients A₅,A₇,A₉,A₁₁,A₀ by residue extraction
(Series of (t+k)^(q−r)·R(t) at each pole t=−k; Apart silently fails to decompose above
denominator-degree ~250, so residues are the robust route). Independent anchor: direct
high-precision summation of (1/2)Σ_{t≥0} R''(t) (via a log-derivative evaluator, R(t)>0 for
t≥0). Results:

| n | F_n ≈ (sign, magnitude) | direct-sum vs exact expansion |
|---|---|---|
| 1 | +1.16102159982…×10⁻¹⁰⁸ | agree 59 digits |
| 2 | +7.72394914838…×10⁻²¹⁰ | agree 93 digits |
| 3 | −5.54315090308…×10⁻³¹⁰ | agree 95 digits |
| 4 | −4.24829432684…×10⁻⁴⁰⁹ | agree 91 digits |
| 5 | −2.33560524192…×10⁻⁵⁰⁸ | agree 92 digits |
| 6 | −1.32751686524…×10⁻⁶⁰⁷ | agree 89 digits |

All ≫ the required 40-digit anchor. Structure holds for every n: coefficients of
ζ(3),ζ(4),ζ(6),ζ(8),ζ(10),ζ(12) are exactly 0; only ζ(5),ζ(7),ζ(9),ζ(11) and the constant
survive. A₁₁ is an integer for every n=1..6. log₁₀|F_n| ≈ −(98.8 n + 9), consistent with the
paper's C₀=227.58… (since 227.58/ln10 = 98.83).

---

## T2. Arithmetic (denominator) lemmas — Lemma 19

Exact claim (Lemma 19, read from the file): with D_N = lcm(1,…,N),
m₀ = max{h_r−1, h₀−2h_{r+1}}, m_j = max{m₀, h₀−h₁−h_{r+j}} (j=1,…,q−r), and the cyclotomic
factor Φ = ∏_{√h₀<p≤m_{q−r}} p^{ν_p} with ν_p = min_{h_{r+1}≤k≤h₀−h_{r+1}} ν_{k,p} (ν_{k,p}
the floor-sum in §8), the multiplier Δ := D_{m₁}^r · D_{m₂}⋯D_{m_{q−r}} · Φ^{−1} satisfies
Δ·F(h) ∈ ℤζ(11)+ℤζ(9)+ℤζ(7)+ℤζ(5)+ℤ.

Parameters (computed from h, not hard-coded): m₀ = 33n; m₁ = 35n, m₂ = 34n, m₃=…=m₁₀ = 33n.
This matches the paper's C₂ = r·m₁ + m₂ + … + m_{q−r} = 3·35 + 34 + 8·33 (per unit n). [VERIFIED]

Checks at n=1..6 [VERIFIED n≤6]:

- **Rough multiplier** M_rough = D_{35n}^3·D_{34n}·D_{33n}^8 clears every coefficient
  A₅,A₇,A₉,A₁₁,A₀ to an integer. A₁₁ is already an integer (denominator 1) for every n.
- **Per-coefficient rough bound** D_{m₀}^{q−j−1}·A_j ∈ ℤ holds for j=5,7,9,11 (exponents
  7,5,3,1), all n.
- **Cyclotomic sharpening (Lemma 19 proper)**: Δ = M_rough/Φ is itself an integer and
  Δ·A_j ∈ ℤ for all j and all n=1..6. Φ is substantial: log₁₀Φ ≈ 50.3, 99.1, 180.3, 229.5,
  308.2, 397.9 for n=1..6 (vs log₁₀M_rough ≈ 170, 332, 504, 700, 864, 1056). So Φ removes a
  large, prime-dependent chunk of the denominator (this is exactly the saving that produces
  C₂ < C₀). All ν_p ≥ 0.
- **Refined valuation bound** ord_p A_j ≥ −(q−j−1)+ν_p verified for all j∈{0,5,7,9,11}, all
  primes p∈(√h₀, m_{q−r}], all n=1..6. **Tightness: the bound is never exactly attained —
  observed slack ≥ 1 at every prime** (min slack per coefficient = 1, occasionally 2). So the
  ν_p certificate is safe but not sharp at finite n: the true p-adic denominators are slightly
  smaller than Zudilin's uniform (min over k) certificate. This is expected (A_j = Σ_k B_{jk}
  gains extra cancellation the uniform bound cannot see) and is favorable, not a discrepancy.

---

## T3. Recurrence and asymptotics

### Asymptotic constants (saddle-point / Lemma 20, Proposition 5)

Characteristic polynomial P(τ) = (τ−η₀)^r∏_{j=1}^q(τ−η_j) − τ^r∏_{j=1}^q(τ−η₀+η_j) has
**degree 15** (leading τ^{16} terms cancel). Its 15 roots are the saddle points.

- τ₀ (the root with Im>0, max Re, Re<η₀) = **87.479005418… + 3.328206905…i** — matches the
  paper's printed τ₀ = 87.47900541…+ i·3.32820690… to all printed digits. [VERIFIED]
- **C₀ = −Re f₀(τ₀) = 227.580196412704** = paper's 227.58019641. [VERIFIED — exact match]
  (f₀ from §8; the constant terms −2Ση_j log η_j + Σ(η₀−2η_j)log(η₀−2η_j) = +235.8049 are
  essential.) Im f₀(τ₀)/π = −86.897 ∉ ℤ, as Lemma 20 requires.
- Empirically |F_n| decays with log₁₀|F_n| ≈ −(98.84 n + 9); fitting log|F_n| = −C₀n+…+ over
  exact n=1..6 plus direct-sum n=10,14 gives C₀ ≈ 227.4–227.9 (scatter from the
  Im f₀(τ₀) oscillation e^{n·Re f₀}·|osc|), bracketing the exact 227.5802. [VERIFIED n≤14]

- **C₂ = 226.24944266** (paper). I confirmed it analytically: derived
  lim(logΦ_n/n) = ∫₀¹φ(x)ψ₁(x)dx − ∫₀^{1/33}φ(x)/x²dx (ψ₁ = trigamma, so the paper's "dψ" is
  d(digamma)); with φ(x)=min_y φ₀(x,y) computed directly from the floor-formula (validated to
  equal the exact ν_{k,p} and to reach 9 on Ω₉), the Riemann-sum value is
  **C₂ = 403 − (226.272 − 49.500) = 226.228**, agreeing with 226.24944 to ~4 sig figs (residual
  is step-function discretization under the 1/x² weight). [VERIFIED ~4 digits]

- **Coefficient growth**: C₁ = max_τ Re f₀(τ) = **350.793**. Measured log|A_j(n)|/n rises from
  ~321 (n=1) to ~335 (n=6) for all of A₅,A₇,A₉,A₁₁,A₀ (they share one growth rate), converging
  toward 350.79. [VERIFIED n≤6, consistent]

- **Distinct characteristic magnitudes** (Re f₀ at the 15 saddle points, conjugate-paired):
  **350.79, 340.59, 307.99, 245.55, 131.85, −190.43, −227.58**. F_n is the *minimal* solution
  (e^{−227.58}); the coefficients follow the *maximal* one (e^{+350.79}).

### Recurrence via creative telescoping (RISC HolonomicFunctions)

Tooling note: RISC packages (fastZeil, HolonomicFunctions) **crash the MCP Wolfram kernel**
(anti-tamper layer trips under the WSTP transport). They load fine in a plain
`math -noprompt < script.wl` **stdin** kernel (per prior project notes; thanks River). Keep
exactly one compute kernel alive — a stale kernel causes license-seat segfaults.

Method: F_n = (1/(r−1)!)Σ_t R^{(r−1)}(t) satisfies the **same** n-recurrence as the
non-differentiated sum Σ_t R(n,t), because the Zeilberger telescoper P(n,S_n) commutes with
∂_t (P(n,S_n)R = Δ_t·cert ⟹ P(n,S_n)∂_t^{r−1}R = Δ_t·∂_t^{r−1}cert, which telescopes). So I
creative-telescope the **normalized** summand R(n,t) = N(n)·R̃(n,t) (N = the factorial ratio of
eq:8.6; the normalization balances the recurrence so its characteristic-polynomial roots are the
true growth rates e^{f₀(τ)} rather than degenerate).

**Gate — Apéry ζ(3)** (well-poised sum r=1,q=5, normalized): CreativeTelescoping gives
**order 2**, operator −(n+1)³F_n + (34n³+153n²+231n+117)F_{n+1} − (n+2)³F_{n+2} = 0,
characteristic polynomial **−λ²+34λ−1**, roots **33.9706, 0.0294372 = (1±√2)⁴** — the known
Apéry values. [VERIFIED — method sound]

**Zudilin ζ(5)–ζ(11)** (r=3, q=13): the explicit recurrence could NOT be extracted — in this
environment HolonomicFunctions `CreativeTelescoping` **crashes the kernel** (segfault, not a
clean memory cap) for every case beyond the simplest. Systematic probe (Annihilator always
succeeds, #2 first-order operators; CT then dies):

| case | r | q | pole order | CreativeTelescoping |
|------|---|---|-----------|---------------------|
| Apéry ζ(3) | 1 | 5 | 1 | ✅ order 2, −λ²+34λ−1 |
| ζ(5)…(r=1,q=13) | 1 | 13 | ≤12 | ✖ kernel crash |
| minimal r=3 | 3 | 7 | ≤4 | ✖ kernel crash |
| Zudilin actual | 3 | 13 | ≤10 | ✖ kernel crash (also the η₀=91 Annihilator OOM-crashes) |

So it is the **r≥3 / high-order-pole** structure (Γ^r cube + poles of order up to q−r) that
defeats the package here, independent of parameter size (the tiny all-η=1 proxies crash too).
The order was therefore not obtained by CT.

**Characteristic polynomial (rigorous, from saddle points — this is the asymptotic content):**
the recurrence's characteristic roots are ρ_i = e^{f₀(τ_i)} at the 15 zeros τ_i of
P(τ) = (τ−η₀)³∏(τ−η_j) − τ³∏(τ−η₀+η_j) (degree 15). Their distinct magnitudes are
|ρ| = e^{Re f₀} ∈ {e^{350.79}, e^{340.59}, e^{307.99}, e^{245.55}, e^{131.85}, e^{−190.43},
e^{−227.58}}. F_n is the minimal solution (e^{−227.58 n} = e^{−C₀ n}); its coefficients follow
the maximal one (e^{+350.79 n} = e^{C₁ n}). NB: for Apéry the analogous P has degree 5 but the
minimal recurrence order is only 2, so here the minimal order is ≤ 15 and plausibly much
smaller — but I could not pin it exactly given the CT crash.

### Irrationality bookkeeping [VERIFIED]

The cleared form Δ_n·F_n = Δ_n A₅ζ(5)+Δ_nA₇ζ(7)+Δ_nA₉ζ(9)+Δ_nA₁₁ζ(11) − Δ_nA₀ has integer
coefficients (T2). Its size ≍ e^{(C₂−C₀)n}. Since
**C₀ − C₂ = 227.5802 − 226.2494 = 1.331 > 0** (my numbers: 227.5802 − 226.228 = 1.353 > 0),
Δ_n F_n → 0 while being a nonzero integer combination of 1,ζ(5),ζ(7),ζ(9),ζ(11); hence not all
of ζ(5),ζ(7),ζ(9),ζ(11) can be rational ⇒ **at least one is irrational (Theorem 3)**.
Note: at the *finite* n I can reach, logΔ_n/n (≈275→242 for n=1→14) has not yet fallen below
C₀ — the D_N/N and Φ_n/n convergence is logarithmically slow, so the inequality is genuinely
an n→∞ statement, as in the paper. The analytic constants above are the rigorous inputs.

---

## T4. Dwork/Lucas-type descent (exploratory) — VERDICT: does NOT hold in the stated form

Computed exact A₅(n), A₀(n) for n=1..12. Let ρ(n) = A₀(n)/A₅(n). p-adic valuations
ord_p(A₀/A₅):

```
p=7 : n=1..12 ord = -5,-11,-11,-9,-10,-10,-10,-10,-11,-15,-15,-17
p=11: n=1..12 ord = -5, -5, -6,-10,-10,-10,-10,-10, -9,-10,-10,-10
p=13: n=1..12 ord = -5, -5, -6, -5,-10,-12,-10,-10,-10,-10,-10,-10
```

- The conjectured p⁵·ρ(n) ≡ ρ(⌊n/p⌋) (mod p) **cannot hold**: ord_p(ρ) ≤ −5 with strict growth
  in n, so neither p⁵·ρ(n) nor ρ(⌊n/p⌋) is a p-adic integer (e.g. p=7,n=9: ord(p⁵ρ(n))=−6,
  ord(ρ(1))=−5 — different, so no mod-p comparison exists). Explicit check for all valid
  (n,⌊n/p⌋) pairs: fails on valuation grounds.
- Structure hint: ord_p(ρ(n)) equals exactly −5 at the smallest n (n<p−ish) and steps to −10,
  −15,… as n grows past multiples of ~ (p−1), i.e. ≈ −5·(number of "digits/levels"). So there
  is a digit-graded valuation pattern, but not the simple one-step p⁵ descent.
- A₅(n) alone has ord_p of both signs (e.g. p=7: 1,−1,1,−5,−3,−6,−5,0,1,−1,−5,0) — no clean
  Lucas pattern in this range.

Verdict: no Dwork/Lucas descent of the conjectured shape; the A₀/A₅ valuations grow linearly,
which is itself the (unsurprising) obstruction.

