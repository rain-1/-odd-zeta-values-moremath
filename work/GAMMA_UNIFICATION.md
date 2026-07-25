# P2b — The Gamma unification: Frobenius constants of the Brown–Zudilin operator

**Agent, 2026-07-25.** Labels: `[PROVED]` derivation written out · `[VERIFIED n digits]`
high-precision computation with stated precision and coefficient bound ·
`[EXCLUDED]` PSLQ negative with precision + bound · `[OPEN]`.
All scripts in `work/gamma/`. Engine: `frobkappa.py` (mpmath + gmpy2 backend).

---

## 0. HEADLINE

1. **The κ-vector of the BZ order-9 operator, to 434 digits** at its nearest conifold
   `z₃ = 1/λ₃`, normalisation `κ₀ = 1`:

   > `κ₂ = −4ζ(2)`  `κ₃ = (550/87)ζ(3)`  `κ₄ = (365/29)ζ(4)`
   > **`κ₅ = (514/87)ζ(5) − (2200/87)ζ(2)ζ(3)`**

   and in the **primitive (logarithmic) normalisation** `λ = log κ`:

   > `λ₂ = −4ζ(2)`, `λ₃ = (550/87)ζ(3)`, `λ₄ = −(215/29)ζ(4)`,
   > ### **`λ₅ = (514/87)·ζ(5)`  — a pure rational multiple of ζ(5).**

   This **fills the slot that `DEFECT_LIT` §E.4 recorded as open**: "no operator in the
   literature whose first non-trivial Frobenius constant is a rational multiple of ζ(5)".
   For the BZ operator the exponent 0 at `z=0` has multiplicity **5**, so `κ₅` is the
   *first higher* Frobenius constant (BV: "the constants with `k < m(ρ)` are periods of
   the LMHS; there is no reason to expect `(D−ρ)^j L`, `j>0`, to be geometric"), and its
   primitive part is `(514/87)ζ(5)`. The entire ζ(2)ζ(3) impurity of `κ₅` is exactly the
   **decomposable** term `λ₂λ₃` — the impurity is reducible, not primitive.

2. **The conservation law, in falsifiable form.** Let `m` = multiplicity of the local
   exponent 0 at `z=0` (the motivic weight) and `r` = order of the recurrence (= number of
   characteristic rays). Then

   > ### **`r = 1 + ⌊m/2⌋`** — the rays are indexed by the **depth** `d = 0,1,…,⌊m/2⌋`
   > of the period they carry, and depth (purity loss) is **anti-correlated with rate**.

   `[VERIFIED exactly, 4 families]`: Apéry ζ(2) `(m,r)=(2,2)`; Apéry ζ(3) `(3,2)`;
   Brown–Zudilin ζ(5) `(5,3)`; **the prior campaign's ζ(7) family `(7,4)`** — the last is a genuine
   prediction: the law was read off `m = 2,3,5`, then `m` for the ζ(7) operator was
   computed here for the first time (`I(s) = s⁷(s−1)³(2s−5)·(deg 8)`, exact sympy
   factorisation) and `1+⌊7/2⌋ = 4` matches the known order 4.

3. **The archimedean Γ-mirror (T5): all four BZ connection constants identified.**
   `[VERIFIED 260 digits]` — this **corrects** `DEFECT_IDENTIFY`'s "A_Q, A_I′, A_I are not
   algebraic × π^k":

   > `A_Q·A_{I′}·A_I = −π^{5/2} / (12√37)`
   > `A_Q = √u /(8π^{5/2})`, `u = (−700λ₃² + 526604λ₃ − 6199)/(37²·557) ∈ ℚ(λ₃)`,
   > `(A_{I′}π^{−5/2})²`, `(A_I π^{−5/2})²`, `(A_Î π^{−1/2})²` each cubic over ℚ.

   Every one is **(a square root in the S₃ cubic field ℚ(λ₃)) × a half-integer power of π**,
   i.e. a Γ(1/2)-monomial times an algebraic number — and **no `Γ(r/s)` with `s > 2`
   occurs** (`s ∈ {3,4,5,6,8,12,24}` excluded at 240 digits, `|c| ≤ 10⁶`).

4. **Two BV errata settled at 219 digits** (both printed forms verified verbatim from the
   PDF first): `[BV] Ex. 29` `κ₅` should read **`(7/3)ζ(5) − (17/3)ζ(2)ζ(3)`** (printed
   `7/5`); `[BV] Ex. 28` `κ₆` should read **`(87/16)ζ(6) + (5/2)ζ(3)²`** (printed `−`).

---

## 1. T1 — the computational definition, and the exact instrument

### 1.1 Source check (fetch-first)

`bv.pdf`/`bv.txt` (arXiv:1908.07501) is on disk from the prior session; I re-read
Definitions 21–22, Lemma 24 and Examples 28–29 **verbatim** rather than trusting the
prior summary. Quoted from the PDF text:

> **Definition 22.** Assume that `c ≠ 0, ∞` is a special reflection point of `L`. Let `γ`
> be a path from 0 to `c` going through regular points of `L`. Fixing a branch of `t^s`
> along `γ`, we have a collection of Frobenius functions `{φ_{ρ,n}(t)}` defined by the
> analytic continuation of (21) along `γ`. The collection of Frobenius constants
> `{κ_{ρ,n}}` is defined by `(σ_c − 1)φ_{ρ,n}(t) = κ_{ρ,n} δ(t)`.

> **Lemma 24.** … (i) `|φ_{ρ,0}(t)| → ∞` as `t → c⁻`; (ii) all `σ_c`-invariant solutions of
> `(D−ρ)^j L` are analytic at `c`; (iii) `a_n(ρ)` of one sign; (iv) `λ_k := lim a_n^{(k)}(ρ)/(k! a_n(ρ))`
> exists. Then `κ_{ρ,0} ≠ 0` and `κ_{ρ,k}/κ_{ρ,0} = Σ_j (log c)^j/j! · λ_{k−j}`.

Equivalently `κ(ε) = c^ε·Λ(ε)`, `Λ(ε) = lim a_n(ρ+ε)/a_n(ρ)`.

> **[BV] p. 21 (quoted):** "…the Frobenius constants corresponding to actual solutions of
> `L` (with `k < m(ρ)`) are periods of the limiting Hodge structure at `t = 0`. However,
> there is no reason to expect that the operators `(D−ρ)^j L` with `j > 0` are geometric.
> From this point of view, it is surprising that the higher Frobenius constants in the
> above examples are periods."

**This sentence is the structural key for BZ**: with `m(0) = 5`, `κ₀…κ₄` are LMHS periods
and `κ₅` is the first *higher* constant — of weight 5. That is why the BZ operator is the
right place to look for the ζ(5)-analogue of `κ₃ = (17/6)ζ(3)`.

### 1.2 The instrument: κ as a ratio of Stokes constants `[PROVED]`

Lemma 24 as stated converges like `1/n` (the prior session's `frob2.py` reached ~1e−9).
The following recasting is exact-to-all-orders and is what makes 400+ digits cheap.

Write `L = Σ_j z^j q_j(θ)`; the Frobenius recursion is `Σ_{j=0}^{d} q_j(n+s−j)a_{n−j}(s) = 0`,
`a₀ = 1`. Let `A(x) = λ^x x^α F(1/x)`, `F(u) = Σ_k c_k u^k`, `c₀ = 1`, be **the** formal
(Birkhoff) solution of `Σ_j q_j(x−j)A(x−j) = 0` for the dominant characteristic root `λ`.
Because the Frobenius deformation is *literally* `n → n + s`, the deformed sequence has
**the same** formal solution evaluated at `x = n+ε`. Hence with the Stokes constant
`S(ε) := lim_n a_n(ρ+ε)/A(n+ε)`,

    Λ(ε) = (S(ε)/S(0))·λ^ε      and therefore      κ(ε) = S(ε)/S(0).      (★)

The `log c` and `λ^ε` factors cancel identically. Convergence of `a_n(ε)/A(n+ε)` is beyond
all orders: the error is `O((λ₂/λ₁)^n)` plus the asymptotic-series truncation
`≈ M!/(Sn)^M`, `S = log|λ_dom/λ_next|`. This reproduces Golyshev–Zagier's "300 digits from
n = 100" claim exactly (`S = 2log(17+12√2) = 7.05`, `7.05·100/log 10 = 306`).

Implementation of the Birkhoff series (`frobkappa.birkhoff`): with `u = 1/x` and
`Q_j(u) := u^D q_j(1/u − j)` (exact integer polynomials),

    Σ_j λ^{−j} Q_j(u)(1−ju)^{α−k} u^k c_k = 0,
    α = β/γ,   β = Σ_j λ^{−j}Q_j′(0),   γ = Σ_j λ^{−j}Q_j(0)·j,
    c_m = −(1/(γm)) Σ_{k<m} c_k h_{k,m+1−k},   H_k(u) = Σ_j λ^{−j}Q_j(u)(1−ju)^{α−k}.

`α` comes out as an **exact rational** and is a strong self-check (`−1` for Apéry ζ(2),
`−3/2` for Apéry ζ(3), `−5/2` for BZ — i.e. conifold exponents `0, 1/2, 3/2`).

### 1.3 The archimedean/p-adic twinning, stated precisely (and not over-stated)

`LAMBDA_HUNT` found the p-adic tower limits to be **values** of
`G(x) = Γ_p(x)e^{−Γ′_p(0)x} = exp(−Σ_{m≥2} ζ_p(m)x^m/m)` at `x = Ap^k`, while BV's p-adic
Frobenius *structure* constants `α_j` are the **Taylor coefficients** of the same `G` at 0.
The archimedean statement that BV actually make ([BV] Thm 30, Cor. 31) is:

* there is a meromorphic `Γ_{ξ₀}(s)` with `(I(s)/R(e^{−2πis}))·Γ_{ξ₀}(s) = Σ_n κ_{ρ,n}(s−ρ)^n`;
* for `L` Picard–Fuchs the `κ_{ρ,n}` lie in the algebra of periods **with `2πi` inverted**.

So the honest twinning is: *both sides are expansion data of a Γ-type generating function
attached to the operator* — `Γ_p` p-adically, `Γ_{ξ₀}` archimedeanly — and in both cases
the coefficients are (multiple) zeta values, `ζ_p(k)` resp. `ζ(k)`. **What is verified here
and not merely asserted**: (a) the archimedean series `log κ(ε) = Σ λ_j ε^j` has
`λ_j ∈ ℚ·ζ(j)` for `j ≤ 5` on the BZ and Apéry-ζ(3) operators and for `j ≤ 4` on the
Apéry-ζ(2) one (where `λ₅ = ζ(5) − (1/5)ζ(2)ζ(3)` is the first impure coefficient) —
i.e. an initial segment of exactly the shape `exp(−Σ r_m ζ(m)x^m)`, `r_m ∈ ℚ`; (b) the archimedean connection constants are
`Γ(1/2)`-monomials times algebraic numbers (§5). I did **not** find, and do not claim, a
literal identity between the two Γ's.

---

## 2. T2 — validation, then the BZ κ-vector

### 2.1 Instrument validation `[VERIFIED 219 digits]`

`work/gamma/t2_validate.py`, `mp.dps = 220`, `K = 13`, `M = 130`, `n ∈ {300,400}`;
self-agreement across `n` is 208–210 digits.

| control | result |
|---|---|
| Apéry ζ(3): `α` | `−3/2` exact |
| Apéry ζ(3): Stokes `S(0)` | `0.2200437671126430378506897598104866566782…` **= `(1+√2)²/(2^{9/4}π^{3/2})`**, the classical closed form, to all digits shown |
| `κ₂ = −2ζ(2)`, `κ₃ = (17/6)ζ(3)`, `κ₄ = 2ζ(4)` | residuals `1e−219` |
| `κ₆…κ₁₀` vs `[GZ2] (47)` | residuals `1e−219` |
| `λ₂…λ₁₀` vs `[GZ1] §9` (independent packaging) | **all reproduced exactly** (e.g. `λ₆ = −(16/105)ζ(2)³−(1/72)ζ(3)² = −(2/3)ζ(6)−(1/72)ζ(3)²`, `λ₈ = (58/175)ζ(2)⁴ − (11/18)ζ(3)ζ(5) = (29/12)ζ(8) − (11/18)ζ(3)ζ(5)`) |
| Apéry ζ(2) vs `[BV] Ex.28` / `[RV]` Table 2 case D, `κ₂…κ₇` | residuals `1e−219` |

**Erratum 1 [SETTLED].** `[BV]` Ex. 29 prints `κ₅ = (7/5)ζ(5) − (17/3)ζ(2)ζ(3)` (verbatim
from the PDF). Computed: `κ₅ = −8.78522655635014817501029803334929851633233616556963…`;
`(7/3)ζ(5) − (17/3)ζ(2)ζ(3)` agrees to `4.6e−219`, the `(7/5)` form is off by `0.9678`.
**Correct: `κ₅ = (7/3)ζ(5) − (17/3)ζ(2)ζ(3)`**, confirming `[GZ2] (47)`. The prior session's
verdict is confirmed and now certified at 219 digits instead of 15.

**Erratum 2 [SETTLED — previously `[RECALLED-UNVERIFIED]`].** `[BV]` Ex. 28 prints
`κ₆ = (87/16)ζ(6) − (5/2)ζ(3)²`. Computed `κ₆ = 9.14415489562452778198190394025559993842547…`;
the `+` form agrees to `5.3e−220`, the `−` form is off by `7.2247`.
**Correct: `κ₆ = (87/16)ζ(6) + (5/2)ζ(3)²`.**

**New values for the Apéry ζ(2)/Beauville-D operator** (literature stops at `κ₇`):

    κ₈ = (8627/4200)ζ(2)⁴ − (7/2)ζ(2)ζ(3)² + (15/2)ζ(3)ζ(5)
    κ₉ = (29/21)ζ(2)³ζ(3) + (5/3)ζ(3)³ − (19/4)ζ(2)²ζ(5) + (115/16)ζ(2)ζ(7) − (2011/72)ζ(9)
    λ₈ = (336593/105000)ζ(2)⁴ + (2/5)ζ(2)ζ(3)² + (11/2)ζ(3)ζ(5)
    λ₉ = −(14263/5250)ζ(2)³ζ(3) − (2/3)ζ(3)³ − (649/100)ζ(2)²ζ(5) − (39/16)ζ(2)ζ(7) − (2011/72)ζ(9)

`κ₁₀` needs `ζ(3,7)` and `ζ(2)ζ(3,5)`; not attempted (no validated MZV routine — see §7).

### 2.2 The BZ operator: how Def. 22 extends, and how it restricts

`work/gamma/bzop.py` rebuilds `L = A(θ−1) + zB(θ) + z²C(θ+1) + z³D(θ+2)` exactly from BZ's
recurrence and confirms `DEFECT_IDENTIFY`:

    I(s) = q₀(s) = 2 s⁵ (2s−1)(41218s³ − 172113s² + 240582s − 112558)
    char. poly  4λ³ − 2368λ² − 188λ + 1          [both exact, sympy]

**Applicability of Def. 22.**
* *Reflection point:* the conifold exponents are `{0,…,7} ∪ {3/2}` (proved exactly in
  `DEFECT_IDENTIFY`), so `σ_c − 1` has rank-1 image at all three finite singularities —
  **Def. 21's first condition holds.** (The second condition, analyticity of the
  `σ_c`-invariant solutions of `L^∨`, I did not verify; `[OPEN]`.)
* *Nearest singularity, real positive:* `z₃ = 1/λ₃ = 0.0016889627…` — Lemma 24's frame applies.
* *`a_n(0)` of one sign:* `a_n(0) = Q_n = 1, 21, 2989, 714549, …` — verified exactly from the
  Frobenius recursion (this is also the check that my `q_j` are right).
* **Restriction found:** Lemma 24's hypothesis (i), `|φ_{ρ,0}(t)| → ∞` as `t→c⁻`, **fails**
  for BZ (`α = −5/2` ⟹ `Σ Q_n z₃^n ≍ Σ n^{−5/2} < ∞`) — and it *also* fails for the Apéry
  ζ(3) operator (`α = −3/2`), for which BV nevertheless quote the conclusion and for which
  I verify it to 219 digits. **Empirical verdict: hypothesis (i) is sufficient, not
  necessary; the conclusion `κ(ε) = c^ε Λ(ε)` holds at `α = −3/2` and at `α = −5/2`.**
  This is the licence for running the machinery on BZ.
* **The rank-5 block is a feature, not an obstruction.** Def. 22 never requires MUM at `z=0`;
  it requires the reflection point. What `m(0)=5` does is shift *which* `κ_j` is the first
  higher one: `κ₀…κ₄` are LMHS periods, `κ₅` is the first non-geometric one — of weight 5.

### 2.3 The κ-vector `[VERIFIED 434 digits]`

`work/gamma/t3e_high.py`, `mp.dps = 520`, `K = 16`, `M = 260`, `n ∈ {700, 800}`;
self-agreement 434 digits. **Cross-check of the whole pipeline:** the Stokes constant
`S(0) = 0.066676425727156767841653340639345444469628745592456…` reproduces
`DEFECT_IDENTIFY`'s `A_Q` (Neville extrapolation, 158 digits, completely different code) —
every digit agrees.

    kappa_0  = 1
    kappa_1  = 0                       (|κ₁| < 1e−440)
    kappa_2  = −6.5797362673929057458896606665841007568757996048271937509422…
    kappa_3  =  7.5992103073307684709178849290953735048361202389341883331695…
    kappa_4  = 13.6223441484332910311497016978457339487166930155288041829064…
    kappa_5  = −43.874582810463900205738690933659318347119467057796690503173…
    kappa_6  =  34.702212286332465372786749212708512062179423906148420493484…
    kappa_7  =  51.859399033579894576098101769427996696229062468953659401479…
    kappa_8  = −193.48622813404950155339365726175718713033001038335366582809…
    kappa_9  =  328.24744793914070437527259388058406094258869151657638966370…

Identifications (PSLQ, `tol = 1e−380`, `|c| ≤ 10¹⁴`, residuals `1e−440`…`1e−451`; the
weight-`j` basis is `ζ(2)^a ∏ζ(odd)`, checked for internal relations first):

| | `κ_j` | `λ_j = [ε^j] log κ` |
|---|---|---|
| 2 | `−4ζ(2)` | `−4ζ(2)` |
| 3 | `(550/87)ζ(3)` | `(550/87)ζ(3)` |
| 4 | `(146/29)ζ(2)² = (365/29)ζ(4)` | `−(86/29)ζ(2)² = −(215/29)ζ(4)` |
| 5 | `(514/87)ζ(5) − (2200/87)ζ(2)ζ(3)` | **`(514/87)ζ(5)`** |

`κ₅ = λ₅ + λ₂λ₃` exactly: `λ₂λ₃ = (−4ζ(2))(550/87)ζ(3) = −(2200/87)ζ(2)ζ(3)`.

**From `j = 6` on the BZ κ-series stops being weight-homogeneous but stays in the MZV ring**
(this is a positive finding, and the Apéry operators run as controls do *not* do it):

    λ₆ = (38416/249777)ζ(3) + (272/3045)ζ(2)³ − (392/7569)ζ(3)²
    λ₇ = (8835680/8242641)ζ(3) − (38416/83259)ζ(2)² + (784/2523)ζ(2)²ζ(3) − (1070/87)ζ(7)
    λ₈ = (1326081904/272007153)ζ(3) − (8835680/2747547)ζ(2)² + (1319080/249777)ζ(5)
         + (74324/29435)ζ(2)⁴ − (26920/7569)ζ(3)ζ(5)
    λ₉ = (4709901251104/260310845421)ζ(3) − (1326081904/90669051)ζ(2)²
         + (303388400/8242641)ζ(5) − (341600/83259)ζ(2)³ − (1716176/1975509)ζ(3)²
         + (48800/17661)ζ(2)³ζ(3) + (385264/1975509)ζ(3)³ + (26920/2523)ζ(2)²ζ(5) + (590/87)ζ(9)

The mixing pattern is sharp and reproducible:

> **`λ_j` contains exactly the weights `j` and `3, 4, …, j−3`.** Weights `j−1`, `j−2` and
> `0,1,2` never occur. The weight-`(j−3)` coefficient of `λ_j` is `−3 ×` the weight-`(j−4)`
> coefficient of `λ_{j−1}`; all denominators lie in `{3,5,7,11,29}`-smooth numbers, with `29`
> and `87 = 3·29` ubiquitous.

`[EXCLUDED]` at `tol = 1e−380`, `|c| ≤ 10¹⁴`, for `j = 6,…,16`: `κ_j`/`λ_j` in the *graded*
weight-`j` basis. `[EXCLUDED]` at `tol = 1e−195`, `|c| ≤ 10¹²`: the structural hypotheses
(a) `κ = N·G` with `N(s) = I(s)/(I₅s⁵)` the rational indicial factor and `G` graded (BV Thm
30's natural shape) — refuted, because `λ₂…λ₅` carry no rational part while `N` has a
non-zero `s¹` coefficient; (b) `log κ` involving Hurwitz `ζ(k,ρ)` at the other local
exponents at `z=0` (the hypergeometric/Kerr shape); (c) `log(c)`-powers. **The mechanism of
the inhomogeneity is `[OPEN]` and is the sharpest remaining question here.**

---

## 3. T3 — the gamma-deformation test

### 3.1 The shared `⟨ζ(5), ζ(2)ζ(3)⟩` plane, made exact `[VERIFIED 200 digits]`

    174·κ₅(BZ) + 987·κ₅(Apéry ζ3) − 3331·κ₅(Apéry ζ2) = 0

is an **exact** identity (check the two coordinates: `174·514/87 + 987·7/3 − 3331 = 0` and
`174·(−2200/87) + 987·(−17/3) + 3331·3 = 0`). It is *real but cheap*: three vectors in a
2-dimensional space are always dependent. The content is in the individual identifications
above, whose ratios are

    ζ(2)ζ(3) : ζ(5)   =   −2200/514 = −1100/257   (BZ)
                        =   −17/7                 (Apéry ζ3)
                        =   −3                    (Apéry ζ2)
                        =   +2                    (BZ's *top period* 2[ζ(5)+2ζ(2)ζ(3)])

**No Möbius/rational transform carries one operator's Frobenius data to another's**:
`[EXCLUDED]` `pslq([κ_j(BZ), κ_j(A3)])` for `j = 5,…,13` at `tol = 1e−193`, `|c| ≤ 10¹⁴`
(the `j = 2,3,4` hits `κ₂(BZ) = 2κ₂(A3)`, `493κ₃(BZ) = 1100κ₃(A3)`, `58κ₄(BZ) = 365κ₄(A3)`
are forced, since each weight-`j` space is 1-dimensional for `j ≤ 4`). The three operators
are **not** gamma-deformations of one another in any 2-term sense.

**The right statement of the relation is the primitive one.** In every case
`κ₅ = λ₅ + λ₂λ₃`, with `(λ₂, λ₃) = (−4ζ2, (550/87)ζ3)`, `(−2ζ2, (17/6)ζ3)`, `(−(7/5)ζ2, 2ζ3)`
for BZ / Apéry ζ(3) / Apéry ζ(2). `λ₅` is a **pure** rational multiple of `ζ(5)` for the
first two — `(514/87)ζ(5)` and `(7/3)ζ(5)` — and for BZ this is the *first higher*
constant (`j = m = 5`); for the Apéry ζ(2) operator, where `j = 5` is three steps past
`m = 2`, purity has already broken: `λ₅ = ζ(5) − (1/5)ζ(2)ζ(3)`.
**The `⟨ζ(5),ζ(2)ζ(3)⟩` plane is a plane of `(λ₅, λ₂λ₃)`-coordinates, not a plane of new
periods.**

### 3.2 Reciprocal periods

`[EXCLUDED]` `κ_j(BZ) ∈ span{π^{−2k}, k = 0..4}` for `j = 2..8`, `tol = 1e−193`,
`|c| ≤ 10¹⁰`. The DEFECT lesson (adjoin `π^{−2k}`) was applied and is negative *for the
κ's* — the reciprocal period lives in the connection-constant ratio `c`, not in `κ`,
consistent with `[BV] Cor. 31` ("periods with `2πi` inverted") being about the *ratios*.

---

## 4. T4 — the rate–purity conservation law

### 4.1 The exact gap

`work/gamma/t5_conn.py`, from the exact roots of `4λ³ − 2368λ² − 188λ + 1`:

    rate(minimal ray) = −log|λ₁| = 5.297561353009062581089142…
    rate(middle ray)  = −log|λ₂| = 2.472373722746639960549954…
    ### purity cost  Δ = log|λ₂/λ₁| = 2.82518763026242262053918841603…

(`= log 16.86407…`; `Δ/log 10 = 1.2270…` is exactly the digits-per-`n` slope of the
441-digit certificate in `DEFECT_IDENTIFY` §0 — the same number, now to 30 digits.)

### 4.2 The law

> **(RPC) Rate–Purity Conservation.** Let `L` be Apéry-like with `m` = multiplicity of the
> local exponent `0` in the indicial polynomial at `z = 0`, and let `r` be the order of the
> associated recurrence. Then
>
> **(RPC-1)** the characteristic rays are indexed by the **depth** `d = 0,1,…,⌊m/2⌋` of the
> period they carry; hence **`r = 1 + ⌊m/2⌋`**.
>
> **(RPC-2)** depth and rate are **anti-correlated**: `|λ_{(d)}|` is strictly decreasing in
> `d`. The price of purifying from depth `d` to depth `d−1` is
> `Δ_d = log|λ_{(d−1)}/λ_{(d)}| > 0`.
>
> **(RPC-3)** the constant effecting the depth-1 → depth-2 raise is the **middle-ray
> connection ratio** `c = A_Î/A_{I′}`, which is a Tate class `12/(2πi)²` of weight `−2`,
> **constant on the whole admissible cone** (`[PROVED]`, `DEFECT_IDENTIFY` §0/T4). Hence
> **purity is not deformable while `Δ` is** — no motion in the cone converts rate into purity.
>
> **(RPC-4) Frobenius witness.** At the nearest conifold, `κ_m = λ_m + Σ_{a+b=m}λ_aλ_b + (depth ≥ 3)`
> with `λ_m ∈ ℚ·ζ(m)`; the number of depth-`≤2` monomials in `κ_m` is exactly `r − 1`.

### 4.3 Numerical status

| family | `m` (indicial mult. of 0) | `1+⌊m/2⌋` | actual `r` | `κ_m` depth-≤2 monomials | `r−1` |
|---|---|---|---|---|---|
| Apéry ζ(2), `D²−t(11D²+11D+3)−t²(D+1)²` | 2 `[exact]` | 2 | 2 ✓ | `λ₂` → 1 | 1 ✓ |
| Apéry ζ(3), `D³−t(34D³+51D²+27D+5)+t²(D+1)³` | 3 `[exact]` | 2 | 2 ✓ | `λ₃` → 1 | 1 ✓ |
| **Brown–Zudilin ζ(5)** (order 9) | **5** `[exact]` | 3 | **3** ✓ | `λ₅ + λ₂λ₃` → 2 | 2 ✓ |
| **ζ(7) family, prior campaign** (order-4 rec., deg 19) | **7** `[exact]` | 4 | **4** ✓ | `λ₇+λ₂λ₅+λ₃λ₄` → 3 | 3 ✓ |

The ζ(7) row is the **prediction**: the operator was rebuilt from the prior campaign's
certified recurrence (`zeta-math/worthiness/zeta7_q_recurrence.json`, order 4, degree 19,
`q_j(x) = c_{4−j}(x+j−4)`), and its indicial polynomial factors **exactly** as

    I(s) = s⁷ (s−1)³ (2s−5) (3690864s⁸ − 59053824s⁷ + 409061716s⁶ − 1601726448s⁵
                             + 3876913912s⁴ − 5940014784s³ + 5627137052s² − 3014681200s + 699679047)

— `m = 7`, i.e. **the multiplicity of the exponent 0 equals the weight**, matching
`m = 2,3,5` for weights 2,3,5. `1 + ⌊7/2⌋ = 4 = r` ✓.

### 4.4 How to falsify

A fifth Apéry-like family with weight `w` falsifies (RPC-1) if `r ≠ 1 + ⌊w/2⌋`, or (RPC-4)
if the `κ_w` of its nearest conifold has a number of depth-`≤2` monomials different from
`r−1`, or (RPC-3) if its middle-ray connection ratio is a non-Tate period. Concrete open
predictions: a weight-4 family must have `r = 3`; a weight-6 family `r = 4`; a weight-9
family `r = 5` and `κ₉ = λ₉ + λ₂λ₇ + λ₃λ₆ + λ₄λ₅ + (deeper)`.

**Why this is the "rate + purity" law.** The reason ζ(5) is out of reach by the BZ family is
now a *counting* statement: weight 5 admits `⌊5/2⌋ = 2` depths, so the recurrence must have
3 rays; the pure forms `I′, Î` are forced onto the depth-1 ray and the depth-2 combination
`I = 2I′ + 4ζ(2)Î` monopolises the minimal ray. The `4ζ(2)` is `−(2πi)²/6`, and its inverse
`c = 12/(2πi)²` is the cone-constant defect. The rate you would need lives on the ray whose
period is impure **by construction of the depth filtration**, and `Δ = 2.8252…` is the exact
toll. (`ORCHESTRATOR_NOTES` §2c(iii)'s "BZ's top period is depth 2, and its impurity blocks
the weight-5 harmonic-monomial decomposition of `P_n`" is the algebraic shadow of the same
count; the Betti index `2` in `I = 2I′ + …` and and the `24` in the Bernoulli normalisation `4ζ(2) = −(2πi)²/6` are
lattice bookkeeping for the same Tate class.)

---

## 5. T5 — the archimedean Λ-mirror: the connection constants ARE Γ-values

### 5.1 New high-precision values `[VERIFIED 287–322 digits]`

`work/gamma/t5_conn.py`: exact `Fraction` ladders `Q_n, P_n, P̂_n` to `n = 520` from BZ's
recurrence with BZ's own anchors (`Q₃ = 714549` checked), `I′ = Qζ(5)−P`, `Î = Qζ(3)−P̂`,
`I = 2I′+4ζ(2)Î` formed at `mp.dps = 3200` (the cancellation is `(λ₃/|λ₂|)^n = 10^{1999}` at
`n = 520`), then the Birkhoff/Stokes limit on each ray at `mp.dps = 400`, `M = 200`.
All four exponents come out `α = −5/2` automatically.

| constant | value | agreement across `n` | prior (`DEFECT`) |
|---|---|---|---|
| `A_Q`   | `0.0666764257271567678416533406393454444696287455924559300242811…` | 322 dig | 158 dig |
| `A_{I′}`| `−0.751355876474989299509392021708018149940768130341030826253742…` | 288 dig | 148 dig |
| `A_Î`   | `0.228384800223216134984520978825375064420714931582040497484098…` | 288 dig | 148 dig |
| `A_I`   | `4.78381719294327891215233374724085460054978566493764352967709…` | 287 dig | 147 dig |

`A_Î/A_{I′} + 3/π² = 5.7e−381` — the purity defect `c = −3/π²` reconfirmed independently at
**381 digits**.

### 5.2 The identifications `[VERIFIED 260 digits]`

Finder validated first on `Γ(1/3)Γ(2/3) = 2π/√3`, the `Γ(1/6)` duplication, **and** on the
Apéry ζ(3) Stokes constant `S(0) = (1+√2)²/(2^{9/4}π^{3/2})` (relation `[−4,8,−9,−6]` found).
Basis hygiene: `log|z₁|+log|z₂|+log|z₃| = log 4` exactly (the singular cubic is
`z³−188z²−2368z+4`, product of roots `−4`) — including all three is a **degenerate basis**
and produced a spurious zero-on-target hit before I dropped `log|z₃|`.

> **(i) Stokes determinant.**  `A_Q · A_{I′} · A_I = −π^{5/2}/(12√37)`
>   `[VERIFIED, relative difference 1.1e−260]`.  Equivalently `(A_QA_{I′}A_I)² = π⁵/5328`,
>   `5328 = 2⁴·3²·37`.  Corollary (using `c = −3/π²`): `A_Q·A_Î·A_I = √π/(4√37)`,
>   `[VERIFIED independently]`.
>
> **(ii) Each constant separately.**  With `λ₃ = 592.0793805346115628…` the dominant root:
>
>   `64·(A_Q π^{5/2})² = u`, `37u³ − 3219u² − 229u − 1 = 0`, and **explicitly**
>   ### `u = (−700 λ₃² + 526604 λ₃ − 6199)/762533`,  `762533 = 37²·557`
>   `[VERIFIED 261 digits]`, i.e. `A_Q = √u/(8π^{5/2})`.
>
>   `(A_{I′} π^{−5/2})² = t`: `1726272 t³ + 4171824 t² − 8244 t + 1 = 0`
>   `(A_I π^{−5/2})² = t`: `37 t³ + 51504 t² − 58624 t + 4096 = 0`
>   `(A_Î π^{−1/2})² = t`: `2368 t³ + 51504 t² − 916 t + 1 = 0`
>   `[all VERIFIED at tol 1e−230, |c| ≤ 10¹⁶]`.
>
> Internal consistency (a real check, not a restatement): the `A_{I′}` cubic is the `A_Î`
> cubic under `t ↦ t/9`, forced by `A_{I′} = A_Î/c = −(π²/3)A_Î`; and the π-powers
> `(−5/2, +5/2, +5/2, +1/2)` multiply to `π^{5/2}` in (i). `2368` (the `A_Î` cubic's leading
> coefficient) is the middle coefficient of the characteristic polynomial
> `4λ³−2368λ²−188λ+1`; `37` and `557` are the primes of `41218 = 2·37·557`; the singular
> cubic's discriminant is `2⁴·37³·557²` and `disc(37u³−3219u²−229u−1) = 2⁴·37·26357²` —
> **same square class `37`, i.e. the same quadratic resolvent `ℚ(√37)`**, and indeed
> `u ∈ ℚ(λ₃)` explicitly.

**This overturns a recorded negative.** `DEFECT_IDENTIFY` §"What is NOT known" states
"`A_Q, A_{I′}, A_I` are **not** algebraic × π^k" on the strength of `A·π^e`,
`e ∈ {−½,0,½,1,3/2,2,5/2,3}`, minpoly `deg ≤ 12`, `|coef| ≤ 10⁵`. Two gaps: **`e = −5/2`
and `e = −1/2` were never tested** (they are the right exponents for `A_{I′}, A_I, A_Î`),
and for `A_Q` the correct `e = +5/2` *was* tested but the minimal polynomial has
`|coef|` up to `1.3·10⁷`, 130× the bound used. The exclusions were correct as stated and
simply under-ranged.

### 5.3 What the Γ-content actually is

`[EXCLUDED]` `log|A_Q| ∈ ℚ-span{log Γ(k/s)} ∪ {log π, log 2, log 3, log 37, log 557,
log|z₁|, log|z₂|}` for `s ∈ {3,4,5,6,8,12,24}` and combinations, `tol = 1e−240`,
`|c| ≤ 10⁶`. `[EXCLUDED]` `A_Q·π^e ∈ ℚ(λ₃)` (as opposed to its quadratic extension) for
`e ∈ {−3/2,−1/2,0,1/2,3/2}`, `|c| ≤ 10²⁰`.

> **Verdict.** The only Γ-value occurring in the BZ connection constants is **`Γ(1/2) = √π`**.
> The half-integer power is `π^{ρ+1}` with `ρ = 3/2` the conifold exponent — the classical
> transfer factor `1/Γ(−ρ)` (`Γ(−3/2) = 4√π/3`) — and the algebraic part is a square root
> in the `S₃` cubic field `ℚ(λ₃)` of the singular locus. **No `Γ(r/s)` with `s > 2`, no
> cubic-field regulator, no new transcendental.**

This is the exact archimedean counterpart of `LAMBDA_HUNT`'s p-adic verdict: there too, the
answer was `Γ_p` at arguments dictated by the geometry (`p`-power points) times an explicit
algebraic/`ζ_p` factor, and there too `Γ_p(1/2), Γ_p(1/3), Γ_p(1/4)` were shown to be
*algebraic* and hence not the source of anything new. **Both mystery-constant families
terminate at the Gamma function, and on both sides the Γ that matters is the one attached to
the local exponents, not to a root of unity.**

---

## 6. What is new, in one list

* The Stokes-ratio recasting `κ(ε) = S(ε)/S(0)` of BV Lemma 24 — 400+ digits in seconds
  where the direct method gives 9 (`work/gamma/frobkappa.py`).
* `[GZ1] §9`'s `λ`-table reproduced independently through `λ₁₀`; `[BV]` Ex. 28 and Ex. 29
  errata both settled at 219 digits; new `κ₈, κ₉, λ₈, λ₉` for the Apéry ζ(2) operator.
* **The BZ κ-vector**, 434 digits, with `κ₂…κ₅` identified; **`λ₅ = (514/87)ζ(5)`** fills the
  open "first higher Frobenius constant `∈ ℚ·ζ(5)`" slot.
* The observation that the ζ(2)ζ(3) impurity of `κ₅(BZ)` is exactly the decomposable `λ₂λ₃`
  (and, more generally, that `λ_m ∈ ℚ·ζ(m)` at `j = m` for all three operators: `−(7/5)ζ(2)`,
  `(17/6)ζ(3)`, `(514/87)ζ(5)`).
* The inhomogeneity of `λ_j(BZ)` for `j ≥ 6` with the sharp weight pattern `{j} ∪ {3..j−3}`
  and the `−3` recursion between successive off-diagonal coefficients (mechanism `[OPEN]`).
* **`m` = multiplicity of the exponent 0 = the motivic weight** for all four families,
  including the first computation of `m = 7` for the ζ(7) operator of the prior campaign.
* **(RPC): `r = 1 + ⌊m/2⌋`** — rays indexed by depth — verified on 4 families, falsifiable.
* **`A_Q A_{I′} A_I = −π^{5/2}/(12√37)`** and the individual cubics; `A_Q = √u/(8π^{5/2})`
  with `u ∈ ℚ(λ₃)` explicit — overturning the recorded "not algebraic × π^k".
* `A_Î/A_{I′} = −3/π²` reconfirmed to 381 digits by an independent method.

## 7. Open / not done

* **The mechanism of the BZ weight-mixing from `j = 6`.** Refuted: rational-prefactor
  (`κ = N·G`), reparametrisation `s ↦ σ(s)`, Hurwitz-`ζ` at the other exponents,
  `log(c)`-powers. This is the sharpest next question and probably needs `[BV]` Thm 30's
  `R(T)` for a non-cyclic `σ₀` (BV's Cor. 33 assumes a single indicial root).
* **`κ` of the ζ(7) operator.** The `0`/`1` exponent resonance (`I(s) = s⁷(s−1)³…`, so
  `a_n(s)` has a triple pole at `s=0`) needs the resonant Frobenius normalisation. Clearing
  it with `a₀(s) = s³` gives clean `λ₂ = −(292/55)ζ(2)`, `λ₃ = (432/55)ζ(3)` but contaminated
  `λ₄` onward — the base point has slid to the exponent-1 solution. **Do not quote the ζ(7)
  κ's from `work/gamma/z7.out`.** The (RPC) test on ζ(7) rests only on the exact symbolic
  facts `m = 7`, `r = 4`.
* Def. 21's second condition (analyticity of `σ_c`-invariant solutions of `L^∨`) for BZ.
* A validated high-precision MZV routine (needed for `κ₁₀`(Apéry ζ2), `κ₁₁`(Apéry ζ3),
  and any weight-`≥8` BZ identification).
* Individual `A_{I′}`, `A_I` in *explicit* `ℚ(λ₃)` form (only their minimal polynomials are
  pinned down here).

## 8. Files

`work/gamma/frobkappa.py` (engine: eps-series, Birkhoff formal solution, Stokes κ),
`bzop.py` (exact BZ `q_j`), `t2_validate.py` (Apéry controls + errata),
`t2_bz.py`, `t3_pslq.py`, `t3b_lambda.py`, `t3c_ident.py`, `t3d_struct.py` (structure
hypotheses), `t3e_high.py` (434-digit run), `t4_zeta7.py` (ζ(7) operator + indicial
factorisation), `t5_conn.py` (connection constants), `t5b_pslq.py`, `t5c_verify.py`.
Data: `kappas_hi.json`, `kappas.json`, `conn.json`, `bz_kappa.pkl`, `z7_kappa.json`.
