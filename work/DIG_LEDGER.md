# DIG-1 — the parametrized p-adic construction and its exact cost ledger

**Author:** mathematician-agent (River's odd-zeta programme), 2026-07-25
**Labels:** `[PROVED]` = proof written out or read out of a source proof · `[DERIVED]` =
derived here from source lemmas, not separately measured · `[VERIFIED …]` = exact finite
computation (evidence, range always stated) · `[CALIBRATED]` = modelling assumption.
All arithmetic exact (`fractions.Fraction` / `int`); p-adic valuations come from exact
truncated Volkenborn series.
Code: `work/dig/{ledger,family,verify,optimize,freefact,t4_freedom,gate_dig2}.py`.

---

## HEADLINE

1. **T3 GATE: PASS.** One formula, fed only the parameter tuples read off the sources,
   reproduces **all three published p-adic irrationality measures to every printed digit**
   — μ(ζ₂(3)) ≤ 7.177398…, μ(ζ₃(3)) ≤ 22.281447…, μ(ζ₂(5)) ≤ 20.342651… — plus **three
   further independent configurations** (Beukers' second ζ₂(3) form, Lai's two
   one-parameter families, and the structure of Lai–Lupu–Sprang's p ≥ 5 theorem).

2. **The ledger is `α = 2G`, `β = G + E`, `margin = G − E`** at the totally symmetric
   point, with `G = Σ_c (l'_c + 1/(p−1))·log p` (the forced normalisation = the
   archimedean growth) and `E = A + m + 1 − δ` (the d_n budget). Every component is
   derived and separately measured.

3. **The fitted law of `PADIC_SEAM.md` §T4.2 is an artefact and its two deficits are
   wrong.** `margin = (w+3)log p/(p−1) − w` happens to hit the three anchors because
   `(p,r) = (2,2)` and `(3,1)` conspire; it has no first-principles content. The correct
   deficits are **ζ₅(3): −3.000 (not −0.586)** and **ζ₃(5): −1.704 (not −0.606)**, and the
   nearest miss in the whole family is **ζ₂(7): −1.455**.

4. **The real frontier is not size, it is the coset count.** A two-term form in 1 and
   ζ_p(w) exists **iff φ(p^r) = 2**, i.e. `(p,r) ∈ {(2,2),(3,1)}`, plus the exceptional
   point `(2,1)` where LSZ's Lemma 9 makes the single shift ½ *be* the full ζ₂.
   For p ≥ 5, ζ_p(3) is a sum of (p−1)/2 ≥ 2 independent Hurwitz values, and one rational
   function can be p-adically aligned with only one coset at a time. **At p ≥ 5 the best
   rank-1 margin is exactly −E**: the p-adic smallness cancels the archimedean growth to
   the last digit and the whole d_n^E cost goes unpaid. `[VERIFIED numerically at p = 5]`

5. **Beukers already proves the individual Hurwitz values irrational for every p ≥ 3**
   (`ω(a)^{−2}H_p(3,a,p) ∉ ℚ`, Cor. 11.3 — condition (C) holds for every prime power
   F > 2). What is missing at p ≥ 5 is not smallness but **simultaneity**: ζ₅(3) sits in a
   2-dimensional space spanned by two Beukers-irrational numbers, together with
   L₅(3,χ₅) (Beukers Prop. 5.2: `T₅(1/5) = (5³/2)(ζ₅(3) − L₅(3,χ₅))`,
   `T₅(2/5) = (5³/2)(ζ₅(3) + L₅(3,χ₅))`).

6. **DIG-2's crossing does not survive** (§T5). At `α=(25,26,27,28), β=(1,8,48,49)`, p=5:
   `α_p − growth = −28.97` against the requirement `> +48.46`. Even the most generous
   accounting (ideal even coset split, `C₁` ignored) gives `42.25 < 48.46`. The two terms
   the equal-degradation model omits are structural, and one of them is fatal:
   **Bel's p-adic criterion must pay the archimedean coefficient growth `C₁`, which the
   archimedean Rhin–Viola criterion never pays** — and `C₁ = 0` exactly on the degenerate
   locus where DIG-2 proved `δ = 0`.

---

## 0. Sources — fetched, read, and what each was checked for

| source | how obtained | used for |
|---|---|---|
| `llm/18` + `papers/18-*/…tex` (LSZ, arXiv:2505.05005) | local, read in full, formulas cross-checked against the LaTeX | Def. 10/11, Lemmas 5–9, 12, 15–21; the ζ₂(5) anchor |
| `llm/15` (Lai–Sprang, arXiv:2306.10393) | local, read in full | the general machinery: Lemmas 6, 7, 12, 21, 24–34; the coset sum |
| **Beukers, *Irrationality of some p-adic L-values*, arXiv:math/0603277** | **fetched (PDF → text)** | **Thm 11.2 + Prop 11.1 + Prop 5.2 + Appendix — the ζ₂(3) and ζ₃(3) anchors** |
| Calegari, arXiv:math/0408214 | fetched | provenance of the two known ζ_p(3) results |
| **Lai, arXiv:2304.00816 (IJNT 21 (2025) 207)** | **fetched** | the two parametrised families (3.1)/(3.2), and printed rates α = (6s+12)log2, (10s+20)log2 |
| **Lai–Lupu–Sprang, arXiv:2505.23088 (2025)** | **fetched** | the p ≥ 5 construction (Def. 3.1) and Theorem 1.1's constant |
| `work/PADIC_SEAM.md`, `work/padic_seam/padic.py` | local | validated Kubota–Leopoldt implementation (cross-check), the fitted ledger under test |

Two corrections to the corpus notes: (i) LSZ's ζ₂(3)/ζ₃(3) attributions run through
**Beukers Thm 11.2**, whose ledger is fully explicit — it did not have to be reverse-fitted;
(ii) `PADIC_SEAM` T4.2's "same shape α = 2·growth, denominator cost = w" is *correct as a
description of the anchors* but its extrapolation in p is not.

---

## 1. T1 — the parametrized construction

### 1.1 The family (one display)

> **`R_n(t) = C^n · (2t+n)^δ · ∏_{c=1}^{M} (t + θ'_c)_{L_c} / (t)_{n+1}^{A}`**,
> **`S_n(θ₀) = ∫_{ℤ_p} R_n^{(m)}(t + θ₀) dt`**,
> **`S_n = Σ_{θ₀ ∈ Θ} S_n(θ₀)`**

with the free parameter tuple

| parameter | meaning | constraint |
|---|---|---|
| `p` | the prime | — |
| `θ₀ = a/p^r` | integration shift, depth `r = −v_p(θ₀)` | `Θ ∋ θ₀`; see 1.3 |
| `θ'_c`, `c = 1…M` | numerator Pochhammer shifts, depths `l'_c` | fractional; alignment = 1.2 |
| `L_c = λ_c·n` | Pochhammer lengths (**asymmetric allowed** — the Rhin–Viola direction) | `Σλ_c ≤ A` |
| `A` | pole order of `(t)_{n+1}^A` | `deg R = δ + Σ L_c − A(n+1) ≤ −2` |
| `m ≥ 0` | derivative order (`m = −1`: primitive, Lai–Sprang's convention) | — |
| `δ ∈ {0,1}` | the very-well-poised factor | `δ ≤ A − 2` (degree) |
| `C` | normalisation; **forced**, see 2.1 | `C = p^{v_p(C)}` |
| `Θ` | the set of cosets at which the *same* form must be small | 1.3 |

`[VERIFIED]` this family contains, as exact special cases with the printed constants:
LSZ Def. 10 (`p=2, r=1, θ'=½ ×4, A=4, m=1, δ=1, C=2^8`); Lai (3.2) `B_n`
(`p=2, r=2, θ'=¾ ×(s+2), A=s+2, m=s, δ=0, C=2^{3s+6}`); Lai (3.1) `A_n`
(`θ' = ¼^{s+2}·¾^{s+2}, A=2s+4, m=s, δ=1, C=2^{6s+12}`); Beukers' `R^{(B)}`
(`p=2, r=1, θ'=½ ×3, A=3, m=0, δ=1, C=2^6`); Lai–Sprang Def. 16 and Lai–Lupu–Sprang
Def. 3.1 (with free-factorial bricks, §2.5).

### 1.2 What the form is a linear form *in* `[PROVED]`

Partial fractions `R_n(t) = Σ_{i=1}^{A} Σ_{k=0}^{n} r_{i,k}/(t+k)^i`. With
`J_u := ∫_{ℤ_p} dt/(t+θ₀)^u` and `T_{k,u} := Σ_{ν<k}(ν+θ₀)^{−u}` (translation: LSZ Lemma 5):

> `S_n(θ₀) = ρ_0 + Σ_{i=1}^{A} (−1)^m (i)_m ρ_i · J_{i+m}`,  `ρ_i = Σ_k r_{i,k}`,
> `ρ_0 = −(−1)^m Σ_{i,k} r_{i,k} (i)_{m+1} T_{k,i+m+1}`,
> `J_u = u·p^{ru}·ω(a)^{−u}·ζ_p(u+1, θ₀)`.

So `S_n(θ₀)` is a ℤ_p-linear form in **1 and the Hurwitz values `ζ_p(i+m+1, θ₀)`,
`i = 1…A`**. Three killing mechanisms, each with its own parameter dependence:

* **(K1) purity by degree** `[PROVED]`: `ρ_1 = lim_{t→∞} t R_n(t) = 0` when `deg R_n ≤ −2`.
  Kills the weight-`(m+2)` term. *This is the only mechanism that kills an odd weight.*
* **(K2) even vanishing** `[PROVED]`: `ζ_p(2k) = 0`. Available **only for the full ζ_p**,
  i.e. after the twisted coset sum, or at `(p,r) = (2,1)` where LSZ's Lemma 9 makes the
  single shift ½ already the full ζ₂. Hurwitz values at even weight are *not* zero
  (Lai, intro: "the values of ζ₂(·,1/4) at positive even integers are nonzero").
* **(K3) reflection** `[PROVED, and VERIFIED to 43 5-adic digits at p=3]`:
  `ζ_p(s,x) = ζ_p(s,1−x)` (from `B_n(1−x) = (−1)^n B_n(x)` and `ω(−1) = −1`), so cosets
  pair up and only `φ(p^r)/2` classes are independent.

**Rank** (= number of zeta values in the form; only rank 1 yields a measure):

> `rank = #{ i ∈ [2,A] : i + m + 1 odd }` when (K2) applies, else `A − 1`.

`[VERIFIED against the literature]` LSZ `A=4,m=1` → rank 1, weight 5 ✓; `A=6,m=1` → rank 2,
weights {5,7} = Lai's "one of ζ₂(5), ζ₂(7)" ✓; Lai `B_n` → rank `s+1`, weights
`[s+3, 2s+3]` = his Theorem 1.3 ✓.

### 1.3 Which cosets must be covered — the well-definedness condition `[PROVED]`

`ζ_p(i)·D^i = Σ_{1≤j≤D, p∤j} ω(j/D)^{1−i} ζ_p(i, j/D)` (Lai–Sprang Lemma 12, `q_p | D`).
Hence a form in 1 and **ζ_p(w)** (not merely a Hurwitz value) requires either

* `φ(p^r) = 2`, so that a single Hurwitz value *is* ζ_p(w) up to a rational factor —
  this happens **only for `p^r ∈ {3,4}`**, i.e. `(p,r) ∈ {(3,1),(2,2)}`
  (Beukers Prop. 5.2: `T₂(1/4) = 4³ζ₂(3)`, `T₃(1/3) = 3³ζ₃(3)`); or
* the full twisted sum `Θ = {j/p^r : p∤j}` — which also switches on (K2), but then the
  smallness is `min` over the `φ(p^r)` cosets.

At `p ≥ 5` the second route is forced: e.g. `T₅(1/5) = (5³/2)(ζ₅(3) − L₅(3,χ₅))`,
`T₅(2/5) = (5³/2)(ζ₅(3) + L₅(3,χ₅))` — Beukers' machine proves each of these irrational,
but ζ₅(3) is their half-sum.

### 1.4 Non-vanishing `[tracked, parameter-dependent]`

ℚ_p has no positivity, so this is a real constraint and it is *not* uniform over the family:

* **LSZ**: exact Casoratian `ρ_{n,0}ρ_{n+1,3} − ρ_{n+1,0}ρ_{n,3} = 3·2^{16n+18}/(n+1)^5`
  (Lemma 15b). `[VERIFIED exactly, n ≤ 11]` — available only because rank 1 + the
  three-term recursion exist, i.e. only on the very-well-poised slice.
* **Lai** (`A_n`, `B_n`): no Casoratian; non-vanishing is proved only along `n = 2^m − 1`
  by a dominant-term argument (his Lemmas 2.4/2.5, 6.1). Cost: the subsequence.
* **Lai–Sprang / Lai–Lupu–Sprang**: the ℓ(n)-adic criterion (LS Lemma 4) replaces
  non-vanishing by `v_{ℓ(n)}(l_{0,n}) < v_{ℓ(n)}(l_{i,n})` with `ℓ(n) = n+1` prime — this
  *constrains the parameters*: it needs the extra numerator factor
  (`(t+θ_max)_{θ_max n−1}`, resp. LLS's `t^{M_0}`) and `n` in an arithmetic progression.
* **Group moves** (DIG-2 §10) rescale the whole form by `κ ≠ 0` and so preserve
  non-vanishing; the quadratic-transformation bridges do not, and must be re-checked.

---

## 2. T2 — the ledger, exact

All rates are coefficients of `n`. Code: `ledger.py` (formulas), `family.py` (exact
objects), `verify.py` (measurements).

### 2.1 The forced normalisation `G` = the archimedean growth `[DERIVED + VERIFIED]`

`r_{i,k}` carries `∏_c ∏_j (θ'_c − k + j)` (p-denominator `p^{l'_c L_c}`) over
`(k!(n−k)!)^A` (p-denominator `p^{A n/(p−1)}`), so p-integrality of the coefficients forces

> **`v_p(C) = Σ_c l'_c λ_c + A/(p−1)`,  `G := v_p(C)·log p`.**

`[VERIFIED]` this reproduces every published prefactor exactly: `2^{8n}` (LSZ: 4·1+4),
`2^{6n}` (Beukers R^(B): 3+3; Lai B_n at s=0: 2·2+2), `2^{(3s+6)n}`, `2^{(6s+12)n}` (Lai),
`p^{pn}n!^s` (LLS: (p−1)+(p−1+s)/(p−1) = p + s/(p−1)).

**The archimedean coefficient growth equals `G`** when the bricks are *balanced and
co-located* (numerator and pole Pochhammers on the same interval): then the hypergeometric
factor is `e^{o(n)}`. `[PROVED in the sources]` Beukers Prop. 11.1(3) (`|q_n|,|p_n| < e^{εn}`,
radius of convergence 1); LSZ Lemma 20 (char. poly `λ²−2⁹λ+2^{16}`, **double** root `2^8`).
`[VERIFIED]` measured `log max|ρ|/n` → 5.4958…→G=5.5452 (LSZ), 4.15→4.1589 (Lai B₀),
8.21→8.3178 (Lai A₀), 3.276→3.2958 (p=3). *Off that locus the saddle contributes
`C_sad = C₁ > 0` — see §5, where it is decisive.*

### 2.2 The p-adic smallness exponent `α` `[DERIVED + VERIFIED]`

From Sprang's Δ-operator (LSZ Lemma 6/7: `v_p(∫f) ≥ Δ(f) − 1`, `Δ(binom(t+j,n)) ≥ −log_p n`),
applied brick by brick to `R_n^{(m)}(t+θ₀)`:

> **`α = [ v_p(C) + A·r + Σ_c contrib_c(θ₀) ]·log p`**, minimised over `θ₀ ∈ Θ`, where
> `contrib_c = +1/(p−1)` if `θ'_c + θ₀ ∈ ℤ_p` (**aligned**), else `−l''`,
> `l'' = −v_p(θ'_c + θ₀)`.
> Equivalently, with unequal lengths (§5): `α − G = (r + 1/(p−1))·log p·[Σ_d ν_d − Σ_{mis} λ_c]`.

`[VERIFIED — measured `v_p(S_n)` exactly]`

| configuration | predicted α/log p | measured `v_p(S_n)/n` |
|---|---|---|
| LSZ ζ₂(5) | 16 | 16.00 (n=8,16,32) |
| Lai `B_n` s=0 / s=1 | 12 / 18 | 12.06 / 18.25 (n=16) — Lai's printed 12, 18 ✓ |
| Lai `A_n` s=0 / s=1 (mixed alignment) | 20 / 30 | 20.04 / 30.1 (n=24) — Lai's printed 20, 30 ✓ |
| Beukers p=3, weight 3 | 6 | 5.88 → 6 (n=32) |
| p=5, 4 bricks split over 2 cosets | 7.5 | 7.50 (n=12) |
| p=5, 4 bricks all on coset 1/5, *evaluated at 2/5* | 5 = v₅(C) | 5.33 (n=12) → **rate 0** |

The last line is the alignment law made visible: the same form is `p^{−10n}`-small at one
coset and only `p^{−5n}`-small at the other, and `5 = v₅(C)` means the p-adic smallness has
been *exactly* cancelled by the archimedean growth.

**Doubling.** When every copy is aligned and `l'_c = r`: `α = 2G` — LSZ's "totally
symmetric hypergeometric" doubling, here derived rather than observed.

### 2.3 The denominator cost `E` `[DERIVED + VERIFIED]`

> **`E = A + m + 1 − δ`** (times `n`, i.e. `d_n^E`), with a further Φ_n-type saving in some
> families.

The `A + m + 1` is the top pole order of `Σ_i r_{i,k}(i)_{m+1}(ν+θ₀)^{−(i+m+1)}` combined
with `d_n^{A−i} r_{i,k} ∈ ℤ` (Zudilin Lemma 16 / Lai–Sprang Lemmas 26–29); the `−δ` is the
well-poised saving. `[VERIFIED]` measured d_n-multiplicity clearing `ρ_0`: LSZ 5
(= their conjectured (den-con) `d_n^5`, not just their proved `d_n^6`), Lai `B_n` 3, 5
(= 2s+3 ✓), Lai `A_n` 4, 7 (= 3s+4 = A+m+1−δ ✓, one better than his proved `d_n^{3s+5}`),
Beukers p=3 3 ✓. Note `E = w` (the top weight) whenever rank = 1.

### 2.4 The criterion `[PROVED — Bel's Lemma, LSZ Lemma 4]`

Integers `a_n = Φ^{-1}d_n^E ρ_0`, `b_n = Φ^{-1}d_n^E ρ_w`; `|a_n + b_nξ|_p ≤ e^{−αn+o(n)}`,
`max(|a_n|,|b_n|) ≤ e^{βn+o(n)}`, `β = G + E`. Then

> **`margin := α − β = G − E`** (aligned case) **`> 0 ⟹ ξ ∉ ℚ` and `μ(ξ) ≤ α/(α−β) = 2G/(G−E)`.**

Note the asymmetry with the archimedean world, which matters in §5: p-adically the
coefficient *size* enters the irrationality condition; archimedeanly only the denominators do.

### 2.5 The free-factorial direction `[DERIVED + VERIFIED against LLS]`

A numerator brick `n!^S` (Ball–Rivoal/LLS) has `l' = 0`, p-adic contribution `+1/(p−1)`
(`v_p(n!) = n/(p−1)`) and archimedean cost `+log 2` per copy (the binomial saddle
`max_k binom(n,k) = 2^n`), and raises `A` (hence `E`) by one:

> `d(margin)/d(free factorial) = [1/(p−1) + r]·log p − log 2 − 1`.

Feeding LLS's Def. 3.1 (`A = p−1+s`, `p−1` Pochhammer bricks at the shifts `j/p`, `s` free
factorials, primitive so `E = A`) through the ledger gives
`margin(s) = (s+1)·p log p/(p−1) − s(1+log 2) − p + 1`, so a positive margin needs

> `s > [p − 1 − p log p/(p−1)] / [ **p log p/(p−1) − 1 − log 2** ]`

and the bracketed denominator is **exactly the denominator of LLS's constant `c_p`**
(their Theorem 1.1). The numerator differs only in that they replace the crude `log 2` by
the exact `ϖ_p = ψ(1/p) + 2p − 1 + γ + p(log p − Σ_{j≤p} 1/j)`. `[VERIFIED — structure,
the `p/(p−1)` coset factor and the Ball–Rivoal `1 + log 2` all come out of the ledger]`

---

## 3. T3 — VALIDATION (the gate)

`work/dig/ledger.py` — input is **only** `(p, r, shifts, A, m, δ)`; `E`, the regime, the
weights, the rank, `G`, `α`, `β`, `μ` are all derived.

```
zeta_2(3)  Beukers F=4 / Lai B_n s=0   p=2 r=2 A=2 m=0 d=0
   regime S | weights [3] | rank 1 | E = 3 | G = 6log2
   mu <= 7.17739889912418        published 7.177398...      MATCH
zeta_2(3)  Beukers R^(B)             p=2 r=1 A=3 m=0 d=1     (different point, same number)
   regime S2 | weights [3] | rank 1 | E = 3 | G = 6log2
   mu <= 7.17739889912418        published 7.177398...      MATCH
zeta_3(3)  Beukers F=3               p=3 r=1 A=2 m=0 d=0
   regime S | weights [3] | rank 1 | E = 3 | G = 3log3
   mu <= 22.28144795149432       published 22.281447...     MATCH
zeta_2(5)  LSZ 2025                  p=2 r=1 A=4 m=1 d=1
   regime S2 | weights [5] | rank 1 | E = 5 | G = 8log2
   mu <= 20.34265173891448       published 20.342651...     MATCH
```

**T3 VERDICT: PASS.** Beyond the three published measures the same ledger reproduces:
(iv) Beukers' second ζ₂(3) form at a *different* parameter point with the identical
measure — matching LSZ's own remark that the two forms coincide; (v) Lai's `B_n` family,
**both** its smallness rate `(6s+12)log2` and its margin `(3log2−2)s + 6log2−3`, for every
`s`; (vi) Lai's `A_n` smallness rate `(10s+20)log2` for every `s`; (vii) the denominator
of LLS's `c_p`. The only place a source is *sharper than* the ledger is nowhere; the only
place the ledger is sharper than a source is Lai's `A_n` archimedean bound (he prints
`(2+4log2)s + 4 + 8log2`, the ledger gives `(6s+12)log2`, and the exact measurement
8.12→8.21 at n = 8→24 confirms the ledger, converging to 8.3178).

Independent exact re-derivation of the LSZ anchor (`verify.py`): their printed
`ρ_{0,3}=768, ρ_{1,3}=73728, ρ_{0,0}=0, ρ_{1,0}=−1024`, `Σ_k r_{n,1,k} = 0`, the three-term
recursion for both rows (n ≤ 11), the Casoratian `3·2^{16n+18}/(n+1)^5` (n ≤ 11), and
`ρ_{n,3} ∈ ℤ`, `d_n^5ρ_{n,0} ∈ ℤ` (n ≤ 12) — all reproduced from the partial fractions.
Cross-check of the p-adic side against the validated Kubota–Leopoldt code: the reflection
`ζ₃(3,1/3) = ζ₃(3,2/3)` holds to 43 3-adic digits.

---

## 4. T4 — the freedom map

### 4.1 Which parameter moves which component

| direction | `G` (growth) | `α` | `E` | rank | net effect on margin |
|---|---|---|---|---|---|
| `A` (pole order / copies) `+1` | `+(r+1/(p−1))log p` | `+2(r+1/(p−1))log p` | `+1` | `+1` every 2 steps | `+(r+1/(p−1))log p − 1` **but rank grows** |
| `r` (shift depth) `+1` | `+A log p` | `+2A log p` | `0` | `0` | `+A log p` **but φ(p^r) cosets ⇒ regime T** |
| `m` (derivative) `+1` | `0` | `0` | `+1` | `0` (parity flip) | `−1`; raises the weight by 1 |
| `δ` (well-poised) `0→1` | `0` | `0` | `−1` | `0` | `+1` (needs `A ≥ 3`) |
| misalign one copy | `0` | `−(r+1/(p−1))log p` | `0` | `0` | `−(r+1/(p−1))log p` |
| free factorial `n!` `+1` | `+log2 + log p/(p−1)` | `+(2/(p−1)+r)log p` | `+1` | `+½` | `[1/(p−1)+r]log p − log2 − 1` |
| unequal lengths `λ_c` | saddle `C_sad` switches on | linear in `λ` | via `m_j` | — | §5 |

**Where the totally symmetric slice is provably optimal, and where it is merely convenient.**

* **Optimal**: (i) alignment — every copy aligned is the maximum of `Σ_c contrib_c`, so on
  the single-coset regimes the symmetric point maximises `α − G` at fixed `A, r`
  `[PROVED: contrib_c ≤ 1/(p−1) termwise]`; (ii) balance/co-location — it is exactly the
  locus where the hypergeometric saddle vanishes, `C_sad = 0` `[PROVED: Beukers 11.1(3),
  LSZ Lemma 20]`, which is what makes growth `= G`.
* **Merely convenient**: (iii) the *equal exponents* (all `L_c = n`) are not forced —
  unequal lengths are exactly the Rhin–Viola freedom, and they are what DIG-2 needs for
  `δ > 0`; (iv) `δ = 1` and the resulting `E` saving are conveniences of the well-poised
  shape; (v) LSZ's `m = 1, A = 4` is one of two rank-1 routes to weight 5 at `p = 2`
  (`m = 2, A = 3` also works, with a worse margin `6log2 − 5 < 0`).
* **Provably not optimal**: nothing in the symmetric slice fixes `r`; at `p = 2` the depth
  `r = 2` point (Beukers F=4 / Lai `B_n`) and the depth `r = 1` point (Beukers `R^{(B)}`)
  give the identical measure — a genuine 1-parameter degeneracy of the ledger.

### 4.2 The margin function (exported for DIG-3)

```python
# work/dig/ledger.py, work/dig/optimize.py
margin(p, r, shifts, A, m, delta)  =  [ A*r + min_{θ₀∈Θ} Σ_c contrib_c(θ₀) ] * log p  −  E
     E      = A + m + 1 − delta                 # d_n budget
     Θ      = {1/p^r}            if φ(p^r) = 2 or (p,r) = (2,1)     # regime S / S2
            = {j/p^r : p∤j}      otherwise                          # regime T
     rank   = #{i∈[2,A] : i+m+1 odd}  (regimes S2,T)  |  A−1  (regime S)
     weight = the surviving odd index;   rank must be 1 for a measure
# unequal brick lengths (§5):  α − growth = (r+1/(p−1))·log p·[Σν − Σ_mis λ] − C_sad
```

### 4.3 The optimum over the whole parameter space, per `(p, w)`

`optimize.py`, exhaustive over `r ≤ 3, A ≤ 6, m ∈ {w−3,w−4}, δ ∈ {0,1}` and all coset
spreads:

| p | w=3 | w=5 | w=7 | w=9 |
|---|---|---|---|---|
| 2 | **+1.1589** (known) | **+0.5452** (known) | −1.4548 | −3.4548 |
| 3 | **+0.2958** (known) | −1.7042 | −3.7042 | −5.7042 |
| 5 | −3.0000 | −2.9882 | −4.9882 | −6.9882 |
| 7 | −3.0000 | −4.0000 | −6.0000 | −8.0000 |
| 11 | −3.0000 | −4.0000 | −6.0000 | −8.0000 |
| 13 | −3.0000 | −4.0000 | −6.0000 | −8.0000 |

**Sanity anchors and the corrected deficits.** The three known results come out positive
and *only* those three. Against `PADIC_SEAM` §T4.2's extrapolation:

| target | fitted law (PADIC_SEAM) | **first-principles ledger** |
|---|---|---|
| ζ₅(3) | −0.586 | **−3.000** |
| ζ₃(5) | −0.606 | **−1.704** |
| ζ₂(7) | (not tabulated) | **−1.455 ← the nearest miss in the family** |

*Why the fit misled:* `(w+3)log p/(p−1) − w` matches the anchors because at `p=2` the
anchors sit at `r=2, A=2` (and `r=1, A=4`) and at `p=3` at `r=1, A=2`, and
`A(r+1/(p−1))` happens to equal `(w+3)/(p−1)` at exactly those points. The fit has no
`r`, no `A`, and — fatally — no coset count.

### 4.4 The structural statement at p ≥ 5 `[DERIVED, numerically VERIFIED at p=5]`

For `p ≥ 5` every rank-1 configuration is in regime T, some coset has no aligned brick, and

> `A·r + Σ_c contrib_c = A·r − A·r = 0` exactly ⟹ **`α = G`, margin = `−E`.**

i.e. *the p-adic smallness of the twisted sum exactly cancels the archimedean growth of its
coefficients, and the entire `d_n^E` denominator cost is unpaid.* Raising `A` cannot help:
the aligned fraction is at most `1/c_p`, `c_p = φ(q_p)/2`, giving
`margin ≤ A·p log p/(p−1)² − E` with `p log p/(p−1)² < 1` for every `p ≥ 3`
(0.824, 0.503, 0.378, 0.264, … at p = 3,5,7,11) and `E ≥ A`. Raising `r` multiplies the
number of cosets and makes it worse. **Positive margins at p ≥ 5 exist only at rank ≥ 2**,
which is exactly the Lai–Lupu–Sprang "one of ζ_p(3),…,ζ_p(c_p)" regime (§2.5) — never an
individual value, never a measure.

---

## 5. T5 — THE GATE for DIG-2: the crossing does not survive

`work/dig/gate_dig2.py`. Ledger extended to unequal brick lengths (Zudilin llm/04 (2.4)):
numerator bricks `(t+b_j)_{λ_j n}/(λ_j n)!`, pole bricks `(ν_j n−1)!/(t+a_j)_{ν_j n}`,
`λ_j = α_j−β_j`, `ν_j = β_j−α_j`:

> **`α_p − growth = (r + 1/(p−1))·log p·[ Σ_d ν_d − Σ_{mis} λ_c ] − C_sad`**, `C_sad = C₁`.

At DIG-2's crossing point `α=(25,26,27,28), β=(1,8,48,49)`, `p=5`, `r=1`:
`λ = (24,18)`, `ν = (21,21)`, budget 72, `δ = 23.5407`, `C₂ = 48.4593`, `C₁ = 77.2577`.

```
alpha_p - growth  (single Hurwitz coset, all bricks aligned)  =  +7.24
alpha_p - growth  (zeta_5(3): worst coset, best split)        = -28.97
REQUIREMENT                                                   > +48.46
VERDICT: FAIL, shortfall 77.43
most generous accounting (ideal even split, C_1 ignored):  42.25 < 48.46  -> still FAIL
```

Same verdict at the RV optimum (−12.26 vs +29.81) and at the Apéry/Ball direction
(−1.51 vs +3.00). **The equal-degradation model omits two terms:**

1. **`C₁` — and this one is structural.** Bel's p-adic criterion needs
   `α > growth + denominators`; the archimedean Rhin–Viola criterion needs only
   `C₀ > C₂` (`C₁` enters the *measure*, never the irrationality condition). So the p-adic
   side pays the coefficient growth. And `C₁ = 0` **exactly** on the degenerate locus where
   the numerator bricks overlie the poles — Beukers Prop. 11.1(3), LSZ Lemma 20 — which is
   **exactly** where DIG-2 proved `δ = 0` (§6a). `δ > 0` and `C₁ = 0` have disjoint support.
   Measured: `C₁/budget` = 1.175 (symmetric), 0.969 (RV), 1.073 (crossing) — each alone
   exceeds the entire available `δ/budget ≤ 0.44`.
   Moreover `C₁ > C₀ > C₂` at every direction where the archimedean construction works, so
   the p-adic requirement `α_p > C₁ + C₂` is more than twice the archimedean one.
2. **The coset defect.** For ζ_p at `p ≥ 5` a numerator brick aligns with one coset only;
   at the worst coset the aligned length is at most `Σλ/c_p`. Measured defect at the three
   directions: 0.50, 0.357, 0.4286 of `Σν`.

**What would have to be true instead.** The break-even condition is
`(r+1/(p−1))·log p·[Σν − Σ_mis λ] > budget − δ + C₁`. At p=5 the left side is at most
`(1+¼)log5·Σν/2 = 1.006·Σν` while the right side is `≈ 3.0·Σν` at the tested directions —
a factor ≈ 3, not the 16 % relative degradation the equal-degradation model allowed.

**One escape hatch, honestly flagged.** `α = min over cosets` is an *inequality*: the
twisted sum could in principle be more p-adically small than its worst summand through
systematic cancellation between cosets. No construction in the literature does this, and
the ledger has no term for it, but it is the only place in this parameter space where the
p ≥ 5 verdict could be overturned. (Also: DIG-2's caveat (ii) is confirmed — for `p ≥ 3`
the shift lattice must be the full `{ν/p^l}`; that is precisely what forces the min.)

### 5b. The unequal-length ledger, measured `[VERIFIED — this is what makes §5 binding]`

Exact test at `p=5, θ₀=1/5`, numerator bricks `(t+4/5)_n` and `(t+4/5)_{2n}` (lengths
λ = 1, 2), poles `(t)_{n+1}^3`, against the co-located control (lengths 1,1,1):

| | predicted `α/log5` | measured `v₅(S_n)/n` | predicted `G` | measured growth | `C_sad` |
|---|---|---|---|---|---|
| unequal λ = (1,2) | 6.50 | 6.33 – 6.67 (n = 6…15) | 4.4260 | 5.77 – 5.86 | **+1.35** |
| control λ = (1,1,1) | 7.50 | 7.33 – 7.67 | 6.0354 | 5.97 – 6.06 | **≈ 0** |

and the gauge-invariant margin rate closes exactly:
`(r+1/(p−1))·log5·[Σν − Σ_mis λ] − C_sad = 1.25·log5·3 − 1.35 = 4.69`
against the measured `α − growth = 6.50·log5 − 5.77 = 4.69`. **The saddle term `C_sad`
switches on precisely when the bricks stop being co-located** — which is the whole content
of §5, and it is now measured, not assumed.

---

## 6. Reproduction

```
work/dig/ledger.py     the ledger + T3 gate (3 published measures + Lai cross-checks)
work/dig/family.py     exact partial fractions, rho_0/rho_i, Volkenborn J_u, S_n
work/dig/verify.py     exact LSZ regeneration; measured alpha, growth, E; p=3 configuration
work/dig/optimize.py   exhaustive rank-1 optimiser; the (p,w) table; freedom map
work/dig/freefact.py   the free-factorial direction; LLS Theorem 1.1 reproduced
work/dig/t4_freedom.py the alignment law verified numerically at p=5; regime table
work/dig/gate_dig2.py  THE GATE: DIG-2's crossing evaluated
```

## 7. Open items, ranked

1. **Coset cancellation** (§5 escape hatch) — the only route to p ≥ 5 left inside this
   family. Needs: a construction where `v_p(Σ_j S_{j/p}) > min_j v_p(S_{j/p})` by `Θ(n)`.
2. **ζ₂(7) at −1.455** is the nearest miss anywhere in the family; DIG-2's group acts at
   `p = 2` too, where `C₁ = 0` is *also* only at the symmetric point — the same tension,
   but the deficit is 1.455 rather than a factor 3. Worth one calibration run.
3. The `Φ_n`-type savings are family-specific and only partly modelled (`E = A+m+1−δ` is
   the measured multiplicity; Lai's `A_n` additionally has an asymptotic `Φ^{−(s+2)}`).
   A sharper `E` would move every margin by `O(1)`.
4. ~~The unequal-length ledger is only `[DERIVED]`~~ — **CLOSED, now `[VERIFIED]`**, see §5b.
