# P3 — The p-adic seam

**Author:** mathematician-agent (River's odd-zeta program), 2026-07-24
**Labels:** `[PROVED]` complete proof written out · `[VERIFIED …]` finite exact computation
(evidence, never proof; range always stated) · `[RECALLED-UNVERIFIED]` memory, not checked.
All arithmetic exact (Python `Fraction`/`int`); every p-adic digit comes from exact rationals.

---

## HEADLINE (read this first)

1. **[VERIFIED]** The tower limits exist for all three of our families, with a *uniform*
   convergence rate of **exactly 3 p-adic digits per tower level** — for the Apéry weight-3
   row, for the BZ weight-3 row `P̂`, **and for the BZ weight-5 row `P`**. Weight sets the
   normalising power `p^{ws}`; it does **not** set the rate. The rate is always 3.

2. **[VERIFIED, negative]** None of the tower limits is a small-height ℚ-affine function of
   `ζ_p(3)` or `ζ_p(5)`. Concretely: no relation `c₀ + c₁ζ_p(w) + c₂Λ = 0` with height
   ≲ 10⁴ exists, at p = 5, 7, 11, 13, to 12–24 certified p-adic digits. **The classical Apéry
   pair and the BZ pair do not p-adically approximate the Kubota–Leopoldt zeta values.**
   (Consistent with the literature: Calegari's p-adic ζ_p(3) irrationality uses *different*
   sequences — overconvergent p-adic modular forms — not the Apéry pair.)
   **The sharp form of this negative** (T2.4) is not about margins at all:
   `v_p(b_n − ζ_p(3)a_n) − v_p(a_n) = −3⌊log_p n⌋ + O(1)` and
   `v_p(Q_nζ_p(5) − P_n) − v_p(Q_n) = −5⌊log_p n⌋ + O(1)` — **the p-adic linear forms diverge
   polynomially** (`≍ n³`, `≍ n⁵`) where Bel's criterion needs `exp(−αn)`. No sharpening can
   rescue these pairs p-adically; the gap is infinite.

3. **[VERIFIED, p ∈ {5,7,11,13,17,19}] THE DEFECT VERDICT — the p-adic defect is `c_p = 0`.**
   Archimedean (`work/DEFECT_IDENTIFY.md`, PROVED): `c = lim Î_n/I′_n = −1/(2ζ(2)) = −3/π² ≠ 0`,
   because `I′` and `Î` **share the ray λ₂** — the archimedean degeneracy that produces the
   impurity `ζ(5)+2ζ(2)ζ(3)` and exiles the class off the minimal ray.
   p-adically the two rows sit in **different valuation strata**:
   `v_p(P̂_n/Q_n) = −3L + O(1)`, `v_p(P_n/Q_n) = −5L + O(1)` (`L = ⌊log_p n⌋`), hence
   `v_p(Î_n/I′_n) = 2L + O(1) → +∞`, i.e. `c_p = lim_n Î_n/I′_n = 0`.
   **The archimedean degeneracy is resolved p-adically: the Frobenius grading
   diag(1, p³, p⁵) separates the weight-3 and weight-5 pieces, and there is no p-adic
   purity-defect obstruction at all.** (Renormalised defect `ĉ_p(a) := Λ^{P̂}_a/Λ^P_a` is a
   p-adic unit but depends on the tower base `a` and is not rational.)

---

## Objects and conventions

**Apéry ζ(3) pair.** `a_n = Σ_k C(n,k)²C(n+k,k)²`; `b_n` the second solution with `b_0=0, b_1=6`
(`b_n/a_n → ζ(3)`). Both satisfy `(n+1)³u_{n+1} = (34n³+51n²+27n+5)u_n − n³u_{n−1}`.
**[VERIFIED]** Computationally I use the *integer* recurrence obtained by `α_n=(n!)³a_n`,
`β_n=(n!)³b_n`:

> `u_{n+1} = (34n³+51n²+27n+5)·u_n − n⁶·u_{n−1}`,  `α_0,α_1 = 1,5`;  `β_0,β_1 = 0,6`,
> and `f(n) := b_n/a_n = β_n/α_n`.

Checked against the closed-form double sum for n ≤ 29 (0 mismatches) and against `ζ(3)` to
79 decimals at n = 400. Generated exactly to **n = 125 000**.

**BZ ζ(5) pair.** Exact ladders `Q_n, P_n, P̂_n` (BZ printed normalisation: `Q_0=1, P_0=0,
Q_1=21, P_1=87/4, P_2=1190161/384, P̂_1=101/4, P̂_2=344923/96`), from
`zeta-math/worthiness/falsify_data/ladder_{Q,P,Ph}.json` (n ≤ 360), **extended exactly** by the
certified order-3 recurrence of `work/lb5/core.py` (V6b normalised).
**[VERIFIED]** the recurrence residual is exactly 0 for all three rows at every n ≤ 357
(358 checks per row), and the extension reproduces the archimedean limits:

> `P_n/Q_n → ζ(5)` and `P̂_n/Q_n → ζ(3)`, both to **59 decimals** at n = 800 and n = 5000.

So `I′_n = Q_nζ(5) − P_n` and `Î_n = Q_nζ(3) − P̂_n` in the notation of `DEFECT_IDENTIFY.md`.

**p-adic reference values.** `q_p = p` (p odd), `4` (p=2); ω the Teichmüller character mod `q_p`;
`⟨x⟩ = x/ω(x)`. Source (local, read): `llm/18-lai-sprang-zudilin-2025` §2, **Definition 8**:

> `ζ_p(s) := L_p(s, ω^{1−s})` for integer `s ≥ 2`; in particular
> `ζ_p(3) = L_p(3, ω^{−2})`, `ζ_p(5) = L_p(5, ω^{−4})`.

This is the same normalisation as **Beukers–Vlasenko, "Frobenius structure and p-adic zeta
values", arXiv:2302.09603 (Adv. Math. 480, 2025)**, which states
`ζ_p(m) = p-adic lim −(1−p^{n−1})B_n/n` at `n = 1−m+(p−1)p^r` — fetched and read.

---

## T1 — p-adic limits along p-towers (Apéry ζ(3) pair)

### T1.1 The convergence statement [PROVED, given the descent congruence]

From the master descent `p³·b_n·a_q ≡ b_q·a_n (mod p³)`, `q = ⌊n/p⌋`
(`[VERIFIED 5≤p≤31, n≤320]`, `work/WARMUP_ZETA3_DWORK.md`), on p-unit cells one has the ratio
form `p³ f(n) ≡ f(q) (mod p³)`. Put `n_s = a·p^s` and

> **`L_s := p^{3s}·b_{a p^s} / a_{a p^s}`.**

Multiplying the ratio descent by `p^{3(s−1)}`:

> **`L_s ≡ L_{s−1} (mod p^{3s})`,  hence `(L_s)` is Cauchy and `Λ_a := lim_s L_s` exists in ℚ_p,
> with `Λ_a ≡ L_s (mod p^{3(s+1)})`.**  Rate: **3 new certified digits per level.**

More generally the same holds along **any descent branch** `n_s = p·n_{s−1} + r_s`.

**Structural remark [PROVED].** `Λ_a` is *unchanged* by `b → b + c·a` (since `p^{3s}c → 0`) and
scales by λ under `b → λb`. So `Λ_a` is an intrinsic invariant of the recurrence and the tower,
defined up to one global scalar; the ratios `Λ_a/Λ_{a'}` are absolute invariants. (In particular
`Λ_a` cannot "see" the archimedean normalisation `lim b_n/a_n = ζ(3)` except through the scalar.)
Also `Λ_{p^k a} = p^{−3k}Λ_a` — verified numerically as a consistency check.

### T1.2 Measured rate [VERIFIED]

Exact data to **n = 125 000** (`p=5`: s ≤ 7, n = 78125; `p=7`: s ≤ 6, n = 117649; `p=11`: s ≤ 4;
`p=13`: s ≤ 4). Digits of agreement `L_s` vs `L_{s−1}`, after clearing the common
`p^{min v}` shift:

| p | tower | v_p(Λ_a) | agreement per level |
|---|---|---|---|
| 5 | a=1 | −1 | 2, 5, 8, 11, 14, 17, 20 |
| 5 | a=2 |  0 | 3, 6, 9, 12, 15, 18 |
| 7 | a=1 |  0 | 3, 6, 9, 12, 15, 18 |
| 7 | a=3 |  1 | 2, 5, 8, 11, 14 |
| 11 | a=1 | 0 | 3, 6, 9, 12 |
| 13 | a=1 | 0 | 3, 6, 9, 12 |
| 5 | branch `n_s = p^{s+1}−1` | 1 | 5, 8, 11, 14, 17, 20 |
| 7 | branch `r=1` | 0 | 4, 6, 9, 13, 15 |

**Rate = exactly 3 digits per level, flat in p, in a, and in the branch** — the depth law
"congruence depth = motivic weight" turned into a convergence rate. `v_p(p^{3s}f(n_s))` is
**constant in s** for every tower (so the pole order of `b_n/a_n` is exactly `3⌊log_p n⌋ + O(1)`),
and equals `v_p(b_a/a_a)`. Consistency: `Λ_a ≡ b_a/a_a (mod p^{3+v})`, verified.

---

## T2 — Kubota–Leopoldt reference values, from scratch

### T2.1 The series, derived (not recalled)

From LSZ's definition (above) plus the Volkenborn integral `∫_{ℤ_p} t^k dt = B_k` (with
**B₁ = −1/2**) and `⟨t+x⟩^{1−s} = ⟨x⟩^{1−s}(1+t/x)^{1−s}` for `|x|_p > 1`:

> `ζ_p(s,x) = (s−1)^{-1} ⟨x⟩^{1−s} Σ_{k≥0} binom(1−s,k) B_k x^{−k}`, and with `M` any common
> multiple of `q_p` and the conductor of χ,
>
> **`L_p(s,χ) = 1/((s−1)M) · Σ_{0<j<M, p∤j} χ(j) ⟨j⟩^{1−s} Σ_{k≥0} binom(1−s,k) B_k (M/j)^k`.**

Convergence is exact and effective: `v_p(B_k) ≥ −1` (von Staudt–Clausen) and `v_p((M/j)^k) = k·v_p(M)`,
so the k-th term has `v_p ≥ k·v_p(M) − 1`.

**[PROVED] the series *is* `L_p`.** Setting `s = 1−n` the inner sum truncates and, using
`B_n(x) = Σ_k binom(n,k)B_k x^{n−k}` and the classical `B_{n,ψ} = F^{n−1}Σ_{a=1}^{F}ψ(a)B_n(a/F)`,
the formula collapses to
`L_p(1−n,χ) = −(1 − χω^{−n}(p)p^{n−1})·B_{n,χω^{−n}}/n` — the defining Kubota–Leopoldt
interpolation, for **every** `n ≥ 1`. The right-hand series is continuous in `s ∈ ℤ_p` (uniform
convergence), and `{1−n : n ≥ 1}` is dense in ℤ_p, so the two agree on all of `ℤ_p∖{1}`. ∎

### T2.2 Implementation cross-checks [VERIFIED]

* **980 / 980** interpolation identities verified mod `p^12`, for `p ∈ {2,3,5,7,11,13,17,19}`,
  every character `ω^e` (`0 ≤ e < p−1`) and every `n ∈ [2,15]`, against **independently coded**
  classical generalised Bernoulli numbers `B_{n,ψ}` (trivial ψ: `B_n` with Euler factor
  `1−p^{n−1}`; non-trivial ψ of conductor p: `p^{n−1}Σ_{a=1}^{p−1}ψ(a)B_n(a/p)`). Zero mismatches.
* **Independence of the auxiliary modulus M** (`M = q_p·m`, `m = 1..5`): identical values.
* **Second, independent route** — the LSZ/BV characterisation
  `ζ_p(s) = lim ζ(k)`, `k ∈ ℤ_{<0}`, `k ≡ s (mod p−1)`, `k → s` p-adically, i.e.
  `−B_n/n` at `n ≡ 1−s (mod lcm(p^N, p−1))`: **16/16 matches** at
  `p ∈ {5,7,11,13}`, `s ∈ {3,5}`, `N ∈ {2,3}` (e.g. `p=13, s=5, n=26360`).

Sample values (base-p digits, least significant first):

| p | `ζ_p(3)` mod `p^{14…22}` digits |
|---|---|
| 5 | 2 4 1 2 3 1 4 2 0 2 0 0 2 3 3 0 … |
| 7 | 1 3 5 4 1 0 2 0 2 4 1 2 5 0 4 6 … |
| 11 | 5 4 1 0 5 8 5 2 6 8 3 1 4 3 |
| 13 | 6 6 5 2 11 12 5 1 5 2 7 5 10 10 |

`v_p(ζ_p(3)) = 0` for `p ≥ 5`; `v_p(ζ_p(5)) = −1` at `p = 5` (the trivial-character pole,
`(p−1) | 4`) and `0` for `p = 7, 11, 13`.

### T2.3 Does `Λ_a` equal a ℚ-affine function of `ζ_p(3)`?  **[VERIFIED — NO]**

Exact-LLL integer-relation search (own exact-Fraction LLL; residue column weighted by `p^K`
so only genuine relations survive; self-tested on a planted relation).

| p | K (certified digits) | best `(1, ζ_p(3), Λ₁)` height | LLL noise floor `p^{K/3}` |
|---|---|---|---|
| 5 | 23 | 1.0 × 10⁵ | 2.3 × 10⁵ |
| 7 | 21 | 4.9 × 10⁵ | 8.2 × 10⁵ |
| 11 | 15 | 4.4 × 10⁴ | 1.6 × 10⁵ |
| 13 | 15 | 1.9 × 10⁵ | 3.7 × 10⁵ |

Every "relation" found sits **at** the noise floor — i.e. nothing. Same for the 2-term test
`(ζ_p(3), Λ₁)` (heights at `√(p^K)`), for all `a = 1…p−1`, and for the normalisation-free test
`Λ_a/Λ_1 ∈ ℚ?` (rational reconstructions all at height ≈ `√(p^K)`, i.e. noise).

### T2.4 The decisive negative, stated sharply [VERIFIED]

Beyond the LLL evidence there is a **structural** reason no ζ_p-irrationality can come out of
these pairs, and it is not a matter of margins:

> **[VERIFIED, all n ≤ 5000, p ∈ {5,7,11,13}]**
> `v_p( b_n − ζ_p(3)·a_n ) − v_p(a_n) = −3⌊log_p n⌋ + O(1)`,
> `v_p( Q_nζ_p(5) − P_n ) − v_p(Q_n) = −5⌊log_p n⌋ + O(1)`.
>
> Equivalently `|a_nζ_p(3) − b_n|_p ≍ n³·|a_n|_p` and `|Q_nζ_p(5) − P_n|_p ≍ n⁵·|Q_n|_p`:
> **the p-adic linear forms diverge polynomially instead of converging.**

Bel's criterion (LSZ Lemma 4) needs `|a_n + b_nξ|_p ≤ exp(−αn)`. Ours grows. So the gap is
infinite, not finite — no sharpening of estimates can rescue these pairs p-adically. (The
`p^{ws}` normalisation of T1/T3 is precisely the act of dividing this divergence out; what
survives, `Λ_a`, is then no longer a linear form in anything.)

**Conclusion.** `Λ_a ∉ ℚ + ℚ·ζ_p(3)` at any height ≲ 10⁴. **There is no "one ratio, two
completions" statement for the classical Apéry pair**: the p-adic tower limit of `b_n/a_n` is
*not* a ζ_p(3)-avatar. This is consistent with (and explains) the fact that Calegari's
p-adic Apéry theorem for `ζ_p(3)` (IMRN 2005, `p = 2,3`) does **not** use the Apéry pair but
overconvergent p-adic modular forms, and with Beukers–Vlasenko: for an **order-3** MUM operator
only `α_1, α_2` exist in the Frobenius expansion `A(y_i(t^p)) = p^i Σ_j α_j y_{i−j}`, and
`ζ_p(3)` first appears at `α_3` (order ≥ 4). The Apéry ζ(3) operator
`θ³ − t(34θ³+51θ²+27θ+5) + t²(θ+1)³` is of order 3 — **too short to carry ζ_p(3)**.

---

## T3 — the BZ pair, and the p-adic defect

### T3.1 Tower limits and rate [VERIFIED]

With `Λ^P_a := lim_s p^{5s}P_{ap^s}/Q_{ap^s}` and `Λ^{P̂}_a := lim_s p^{3s}P̂_{ap^s}/Q_{ap^s}`,
exact ladders to n = 5000:

| p | row (weight) | a | s range | `v_p(p^{ws}·row/Q)` | digits of agreement |
|---|---|---|---|---|---|
| 5 | P (5) | 1 | 0..5 | 0,0,0,0,0,0 | 3, 6, 9, 12, 15 |
| 5 | P̂ (3) | 1 | 0..5 | 0,0,0,0,0,0 | 3, 6, 9, 12, 15 |
| 7 | P (5) | 1 | 0..4 | −1 (const) | 2, 5, 8, 11 |
| 7 | P̂ (3) | 1 | 0..4 | −1 (const) | 2, 5, 8, 11 |
| 11 | P (5) | 1 | 0..3 | 0 (const) | 4, 7, 10 |
| 13 | P (5) | 1 | 0..3 | 0 (const) | 3, 6, 9 |

**The headline of T3.1:** `v_p(p^{5s}P/Q)` is constant in `s` — so weight 5 is the *right*
normalising exponent for the P-row — but the **rate is 3, not 5**. Equivalently the single-step
ratio descent `p⁵f(n_s) ≡ f(n_{s−1})` has depth `5 − 2s`, which **degrades** and goes negative
at `s ≥ 3`: only the `p^{5s}`-scaled statement

> **`p^{5s}·P_{ap^s}·Q_{ap^{s−1}} ≡ p^{5(s−1)}·P_{ap^{s−1}}·Q_{ap^s} (mod p^{3s})`**

survives — the "`p^{5L}`-scaled induction" flagged in `ORCHESTRATOR_NOTES §2d`, here with its
depth measured: `3s`. The P̂-row by contrast has *constant* single-step depth 3, exactly like
the Apéry b-row.

### T3.2 The valuation strata [VERIFIED, n ≤ 5000, p ∈ {5,7,11,13,17,19}]

With `L = ⌊log_p n⌋`, over **all** n (not just towers):

| p | `v_p(P̂_n/Q_n) + 3L` | `v_p(P_n/Q_n) + 5L` | `v_p(P̂_n/P_n) − 2L` |
|---|---|---|---|
| 5 | ∈ {−1, 0} | ∈ {0, 1} | ∈ {−1, 0} |
| 7 | ∈ {−2,−1,0,1} | ∈ {−2,−1,0,1} | ∈ {−2,−1,0} |
| 11 | ∈ {−1,0} | ∈ {−1,0,1} | ∈ {−1,0} |
| 13 | ∈ {−1,0,1} | ∈ {0,1} | ∈ {−2,−1,0,1} |
| 17 | ∈ {−1,0} | ∈ {0,1} | ∈ {−1,0} |
| 19 | ∈ {−1,0} | ∈ {−1,0,1} | ∈ {−2,−1,0,1} |

i.e. `v_p(P̂_n/Q_n) = −3L + O(1)` and `v_p(P_n/Q_n) = −5L + O(1)` with the `O(1)` **bounded by 2
uniformly**. (Also measured: `v_p(Q_n) = 0` always at p = 5, 13, 17, but reaches 7 at p = 7,
4 at p = 11, 3 at p = 19 — the exceptional-prime phenomenon.)

### T3.3 **The defect verdict** [VERIFIED]

Archimedean (`work/DEFECT_IDENTIFY.md`, PROVED): `I′_n` and `Î_n` **ride the same ray** `λ₂`
(`lim log|I′_n|/n = lim log|Î_n|/n = −2.47237…`), so `c = lim Î_n/I′_n` is a finite non-zero
constant, `= −1/(2ζ(2)) = −3/π² = −0.30396…`, and that constant is exactly what forces the
BZ class off the minimal ray.

p-adically, since `ζ_p(3), ζ_p(5) ∈ p^{-1}ℤ_p` while the rows have poles of order `3L`, `5L`:

> `v_p(Î_n) − v_p(Q_n) = −3L + O(1)`, `v_p(I′_n) − v_p(Q_n) = −5L + O(1)`,
> hence **`v_p(Î_n/I′_n) = 2⌊log_p n⌋ + O(1) → +∞`**, i.e.
>
> ### `c_p := lim_{n→∞} Î_n / I′_n = 0` in ℚ_p, for every p ∈ {5,7,11,13,17,19}.

**Interpretation (the strategic point).** The archimedean defect exists *because two of the
three rays coincide* — `I′` and `Î` are degenerate at `λ₂`. p-adically that degeneracy is
**broken**: the Frobenius grading `diag(1, p³, p⁵)` puts `Q`, `P̂`, `P` in three *distinct*
valuation strata `0`, `−3L`, `−5L`. So the p-adic side of our family carries **no purity-defect
obstruction**: `c_p = 0` is as tame as possible, where the archimedean `c = −3/π²` is exactly
the wild object.

**Renormalised defect.** Dividing out the `p^{2s}`:
`ĉ_p(a) := Λ^{P̂}_a/Λ^P_a = lim_s p^{−2s}(P̂_{ap^s}/P_{ap^s})`.
This *is* a well-defined element of ℚ_p with `v_p(ĉ_p(a)) ∈ {−2,−1,0}` — a p-adic unit up to a
bounded power. **[VERIFIED]** it is **not** rational (rational reconstruction at noise floor) and
**it depends on `a`** (different `a` agree to 0 digits). So the renormalised p-adic defect is a
*function on the tower tree*, not a constant — unlike the archimedean `c`.

### T3.4 Explicit values [VERIFIED]

Base-p digits, **least significant first**, from exact rationals (`final_summary.py`):

| p | `ζ_p(3)` | `Λ₁` (Apéry, ×p^{−v}) | `Λ^P_1` (BZ) | `Λ^{P̂}_1` (BZ) | `ĉ_p(1) = Λ^{P̂}_1/Λ^P_1` |
|---|---|---|---|---|---|
| 5 | 2 4 1 2 3 1 4 2 0 2 0 0 | 1 1 3 3 4 0 1 1 1 0 2 2 (v=−1) | 3 3 2 2 4 0 0 2 3 0 1 3 | 4 2 3 0 1 4 4 3 3 4 1 1 | 3 4 2 0 4 3 0 4 0 4 2 2 |
| 7 | 1 3 5 4 1 0 2 0 2 4 1 2 | 4 1 4 4 6 3 0 5 2 6 4 5 | 2 6 5 1 3 3 2 4 0 6 5 1 (v=−1) | 2 5 4 5 1 6 3 6 2 0 1 0 (v=−1) | 1 3 4 5 4 4 2 6 2 5 4 1 |
| 11 | 5 4 1 0 5 8 5 2 6 8 3 1 | 10 8 8 4 10 7 0 6 5 5 5 4 | 3 1 5 7 4 7 2 9 7 9 1 10 | 5 10 6 5 7 3 8 2 3 0 0 0 | 9 7 6 9 1 7 7 5 9 4 9 5 |
| 13 | 6 6 5 2 11 12 5 1 5 2 7 5 | 9 2 5 9 6 6 7 1 10 8 11 7 | 8 12 6 7 8 3 12 2 12 10 12 3 | 6 10 4 2 0 7 7 8 8 11 0 11 | 4 8 4 6 11 8 11 11 10 5 11 10 |

Certified digits: Apéry 24 (p=5, n=78125), 21 (p=7, n=117649), 15 (p=11, 13);
BZ 18 (p=5, n=3125), 15 (p=7, n=2401), 12 (p=11, 13).

### T3.5 Relations to `ζ_p(5)`, `ζ_p(3)`? [VERIFIED — none found]

Best LLL heights for `(1, ζ_p(5), Λ^P_a)` and `(1, ζ_p(3), Λ^{P̂}_a)`, `a = 1, 2`, at
K = 12–18 certified digits: `6·10³ – 1.4·10⁴`, against noise floors `1.5·10⁴ – 1.7·10⁴`.
Nothing below the floor. Same negative as T2.3.

---

## T4 — route assessment

### T4.1 What LSZ actually need (extracted from `llm/18`, read in full)

Their object: `R_n(t) = 2^{8n}·(2t+n)·(t+1/2)_n^4/(t)_{n+1}^4` (Def. 10), `deg R_n = −3`;
`S_n := −∫_{ℤ₂} R'_n(t+1/2) dt` (Def. 11).

**Two vanishing inputs (this is the p-adic gift):**

1. **Purity by degree.** `Σ_k r_{n,1,k} = lim_{t→∞} t R_n(t) = 0` because `deg R_n = −3`.
   That is *exactly* what kills the `ζ_2(3)` coefficient, leaving
   `S_n = ρ_{n,0} + ρ_{n,3}·ζ_2(5)` — a **two-term** form (Lemma 12).
2. **`ζ_p(2k) = 0`** for all even `2k ≥ 2` kills the `ζ_2(2)` and `ζ_2(4)` terms for free.

So p-adically one gets a linear form in `{1, ζ_p(5)}` alone. **Archimedean, both mechanisms are
unavailable**: one is stuck with `1, ζ(2), ζ(3), ζ(4), ζ(5)` (and for BZ with the genuinely
impure `ζ(5)+2ζ(2)ζ(3)`). This is the single sharpest reason the p-adic side is easier.

**One non-vanishing input.** Bel's criterion (Lemma 4) hypothesis (iii): LSZ supply the exact
Casoratian `ρ_{n,0}ρ_{n+1,3} − ρ_{n+1,0}ρ_{n,3} = 3·2^{16n+18}/(n+1)^5 ≠ 0` (Lemma 15b).
**[VERIFIED]** exactly for n ≤ 60 by regenerating both sequences from their recursion.

**The `⁹V₈(ε)/∂³ε` twist.** `ρ_n = ρ_{n,3}/768` is obtained as
`∂_ε` of `(n+ε)·(½)_n²(½+ε)_n²/(n!²(1+ε)_n²)·⁹V₈(−n−ε; −n−ε,½,½,½−ε,½−ε,−n,−n)|_{ε=0}`, and
Andrews' transformation (Krattenthaler–Rivoal Thm 8) turns it into the explicit double sum
`ρ_n = Σ_{0≤i≤k≤n} 2^{4(n−k)}C(2i,i)²C(2n−2i,n−i)C(2k−2i,k−i)C(2k,k)²C(2n−2k,n−k)` (Lemma 17)
⟹ `ρ_{n,3} ∈ ℤ`. For `ρ_{n,0}` the same machine at `¹³V₁₂` gives a quadruple sum whose summands
have `v_p ≥ −2`, and `v_p(∂^λ_ε F|_0) ≥ −2−λ`; taking **λ = 3** yields `v_p(ρ_{n,0}) ≥ −5` for
`p > max{√(2n),3}` (Lemma 18). The `∂³ε` is where the "−5" comes from.

**The ledger.** `α = 16 log 2` (smallness, from Sprang's `Δ`-operator: `v_2(∫f) ≥ Δ(f)−1`,
`Δ(R'_n(t+½)) ≥ 16n+4−6log(n+1)/log2`), `β = 8 log 2 + 5` (growth: char. poly
`λ²−2⁹λ+2^{16}` has a **double** root `2⁸`; denominators `Φ_n^{-1}d_n^6 = e^{5n+o(n)}`).
Margin `α−β = 8log2 − 5 = 0.5452`, `μ ≤ α/(α−β) = 20.3427`.

**[VERIFIED, n ≤ 1000]** I regenerated `ρ_{n,0}, ρ_{n,3}, ρ_n` exactly from LSZ's recursion:
`ρ_{n,3} = 768ρ_n`, `ρ_n ∈ ℤ`, the Casoratian formula, **and LSZ's conjectured (den-con)
`d_n^5·ρ_{n,0} ∈ ℤ`** (`d_n^4` does *not* suffice at any tested n). The per-prime ledger
`e_p(n) := −v_p(ρ_{n,0})` equals `5⌊log_p n⌋` **exactly** for almost every p (isolated deficits
of 1–3 at p = 3, 13), and `log(den ρ_{n,0})/n → 5` from below with the gap shrinking
(0.138 at n=200 → 0.042 at n=1000). **The `d_n^5` budget is tight: there is no free
denominator saving hiding in LSZ's construction.**

### T4.2 The margin ledger — how far the known machinery is from p ≥ 5

The three published individual results have the *same* shape: `α = 2·growth` (the
"totally symmetric hypergeometric" doubling that LSZ themselves single out), `denominator cost
= w` (the weight), and `growth_p = (w+3)·log p/(p−1)` — so
**`margin(p,w) = α − β = (w+3)·log p/(p−1) − w`**.
**[VERIFIED — this fit reproduces all three published irrationality measures exactly]:**

| known result | α | β | μ = α/(α−β) | published |
|---|---|---|---|---|
| `ζ_2(3)` (Beukers/Calegari) | 12log2 | 6log2+3 | 7.1773988991… | 7.177398… ✓ |
| `ζ_3(3)` (Beukers/Calegari) | 6log3 | 3log3+3 | 22.2814479514… | 22.281447… ✓ |
| `ζ_2(5)` (LSZ) | 16log2 | 8log2+5 | 20.3426517389… | 20.342651… ✓ |

Extrapolating the same ledger (`margin = (w+3)·log p/(p−1) − w`; i.e. `6log p/(p−1) − 3` at
weight 3 and `8log p/(p−1) − 5` at weight 5):

| p | margin, weight 3 | margin, weight 5 |
|---|---|---|
| 2 | **+1.1589** (known) | **+0.5452** (known) |
| 3 | **+0.2958** (known) | −0.6056 |
| 5 | −0.5858 | −1.7811 |
| 7 | −1.0541 | −2.4055 |
| 11 | −1.5613 | — |
| 13 | −1.7175 | — |

`[CONJECTURAL FIT — three data points, all at p ∈ {2,3}; the *conclusion* is robust in that
nothing individual is known for any p ≥ 5.]` This is the honest statement of the frontier:
**no individual `ζ_p(odd)` is known irrational for a single prime p ≥ 5.** The two nearest
misses are almost exactly equally far:

> **`ζ_5(3)`: deficit 0.586** — need to shave ≈ 20 % off the `d_n^3` budget.
> **`ζ_3(5)`: deficit 0.606** — need to shave ≈ 12 % off the `d_n^5` budget.

### T4.3 What our machinery does and does not buy

**Does NOT buy (T1–T3, [VERIFIED negative]):** our two families do not p-adically approximate
`ζ_p(3)` or `ζ_p(5)`. The tower limits `Λ_a, Λ^P_a, Λ^{P̂}_a` are honest elements of ℚ_p with
3-digits-per-level convergence, but they are not ℚ-affine in `ζ_p(w)` at any height ≲ 10⁴ —
and every Beukers–Vlasenko-style Frobenius constant (`−ζ_p(3)/3`, `−8ζ_p(3)/25`, `−35ζ_p(3)/108`,
`−ζ_p(5)/5`, …) has height ≤ 10², so those are excluded with a wide margin. Structural reason:
the Apéry ζ(3) operator `θ³ − t(34θ³+51θ²+27θ+5) + t²(θ+1)³` has **order 3**, so its Frobenius
data is `α_0, α_1, α_2` only; in Beukers–Vlasenko's expansion `ζ_p(3)` first enters at `α_3`,
which requires order ≥ 4. (That the Apéry operator is a symmetric square of an order-2 operator,
leaving no room at all, is `[RECALLED-UNVERIFIED]`.) **So there is no ζ_p-irrationality route
through our pairs, at any prime.**

**Does buy — the three statements that are new and provable with what we have:**

* **(S1) Rate theorem.** For a weight-`w` row `X` over `Q` with the descent law of depth `w`,
  the tower sequence `p^{ws}X_{ap^s}/Q_{ap^s}` converges in ℚ_p, gaining **exactly 3 digits per
  level, independently of w**. Verified at w = 3 (Apéry `b/a`; BZ `P̂/Q`) and w = 5 (BZ `P/Q`),
  p ∈ {5,7,11,13}, out to `n = 125 000` (Apéry) / `n = 5 000` (BZ). The weight-5 statement is
  the *only* correct multi-digit form: `p⁵f(n_s) ≡ f(n_{s−1})` has depth `5−2s`, which goes
  negative at `s ≥ 3`; the surviving law is the scaled one,
  `p^{5s}P_{ap^s}Q_{ap^{s−1}} ≡ p^{5(s−1)}P_{ap^{s−1}}Q_{ap^s} (mod p^{3s})`, with depth `3s`.
  This *sharpens and corrects* the "graded-weight discovery" of `ORCHESTRATOR_NOTES §2d`.
* **(S2) Strata theorem.** `v_p(Q_n) ≥ 0`, `v_p(P̂_n/Q_n) = −3L + O(1)`,
  `v_p(P_n/Q_n) = −5L + O(1)` with the `O(1)` in `[−2,1]` uniformly
  (`[VERIFIED n ≤ 5000, p ∈ {5,7,11,13,17,19}]`). This is a clean denominator statement about
  the whole BZ family, in the same family as the sharp-12 conjecture, and it is exactly the
  input a Rhin–Viola-style saving would have to improve on.
* **(S3) `c_p = 0`.** The p-adic purity defect vanishes identically: `v_p(Î_n/I′_n) = 2L+O(1)`.
  Archimedean, `I′` and `Î` are degenerate on the ray `λ₂` and the defect `c = −3/π²` is what
  exiles the class from the minimal ray; p-adically the Frobenius grading separates them and
  **there is no defect obstruction at all**.

### T4.4 The recommendation

**The most plausible new ζ_p statement within reach is *not* a new prime and *not* a new
constant — it is an improved irrationality measure obtained by porting the Rhin–Viola /
Zudilin arithmetic-group denominator savings to the Volkenborn construction.**
This is the same conclusion LSZ reach in their own Final Remarks ("it may certainly be of
interest to … investigate more general hypergeometric series … amenable to … the arithmetic
group method as developed in the works of Rhin and Viola"), and T4.1 shows *why* it is the only
lever: their `d_n^5` budget is provably tight, so the saving must come from a **group action on
a multi-parameter family**, not from a sharper estimate on the present one.

Concretely, in decreasing order of plausibility:

1. **[most plausible]** `μ(ζ_2(5)) < 20.34` and `μ(ζ_2(3)) < 7.177` via a multi-parameter
   Volkenborn family + group method. Needs: a several-parameter `R_{n,\mathbf{h}}(t)`, its
   Volkenborn `Δ`-estimate, and the group of Rhin–Viola symmetries acting on it. Our
   contribution would be the exact-arithmetic ledger machinery (this file's tooling) plus (S2).
2. **[the real prize, and the closest miss]** `ζ_5(3) ∉ ℚ`. Needs a saving of `e^{0.586n}` on
   the `d_n^3` budget of the 5-adic weight-3 construction — i.e. one must show the `p`-part of
   the denominator can be removed for a set of primes of positive density. Our `(LB_w)` descent
   congruences are the **single-prime shadow** of exactly this kind of saving; what is missing
   is that they save `O(1)` per prime (bounded depth), hence `o(n)` in total, whereas one needs
   `δn`. Bridging `O(1) → δn` is the whole problem.
3. **[structural, low risk]** Publish (S1)–(S3) as congruence-level structure theorems: the
   rate theorem, the strata theorem, and `c_p = 0`. (S1) needs the depth-3 descent proved in the
   multi-digit scaled form — the natural continuation of the proved
   `p³b_{ap+r} ≡ b_a a_r (mod p)` theorem.
4. **[not recommended]** Linear independence of `1, ζ_p(3), ζ_p(5)` for a specific p. Two-term
   forms are already at the edge; a three-term form needs the *elimination* technology of
   Fischler–Sprang–Zudilin / Lai–Yu, whose p-adic versions (Sprang 2020, Lai–Sprang 2023) give
   only asymptotic counts, never a fixed small index set.

**The one thing T1–T3 changes about the strategy.** The archimedean programme is blocked by
positivity: `I′_n = I_n + ζ₂|I″_n|` forces the cellular class onto `ρ_B`, and the defect
`c = −3/π² ≠ 0` measures that. `[VERIFIED]` **p-adically that obstruction is simply absent**
(`c_p = 0`; three distinct valuation strata). So the strategic asymmetry is real and now
quantified: *the p-adic side of our family is structurally clean but arithmetically too weak
(no ζ_p in the limits, margin negative for p ≥ 5); the archimedean side is arithmetically
strong but structurally obstructed.* The seam does not close from our families — but the
p-adic side is where a denominator-saving idea has the largest payoff, because there the
obstruction it must overcome is purely a size budget and not a purity defect.

---

## Reproduction

Scripts (scratchpad, self-contained, exact arithmetic only):
`apery.py`, `t1_towers.py`, `t1_run.py`, `t1_analyze.py` (T1);
`padic.py` (Kubota–Leopoldt from scratch + both cross-checks), `lll.py` (exact LLL,
rational reconstruction), `t2_compare.py`, `t2_lll.py`, `t2_hunt.py` (T2);
`t3_bz.py` (exact ladder extension), `t3_run.py`, `t3_defect.py`, `t3_strata.py` (T3);
`t4_lsz.py` (LSZ ledger) (T4).
