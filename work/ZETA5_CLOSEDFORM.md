# ZETA5_CLOSEDFORM — compact closed forms for the Brown–Zudilin companion rows

**Author:** mathematician-agent (River's odd-zeta program), 2026-07-26
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, code in `work/z5cf/`
**Labels:** `[PROVED]` · `[VERIFIED range]` · `[EXCLUDED with bounds]`

---

## 0. HEADLINE

Both companion rows of the Brown–Zudilin ζ(5) family have a **two-/three-term** closed
form. The previous best representatives were **19** (weight 3, `ŵ₃`), **6** (the refold
`ṽ`) and **106 / 130 / 178 / 207** monomials (weight 5). The new forms are

> **`P̂_n = Σ_{k,l=0}^{n} T(n,k,l) · ŵ₃`,  `ŵ₃ = H⁽³⁾_{n+k} − Ψ·H⁽²⁾_{n+k}`**
>
> **`P_n = Σ_{k,l=0}^{n} T(n,k,l) · w₅`,**
> **`w₅ = H⁽⁵⁾_{n+k} + ½(α−β)·H⁽⁴⁾_{n+k} + [ ¼(A₂(k)+A₂(l)) − ½ α Ψ ]·H⁽³⁾_{n+k}`**

with the three antisymmetric/symmetric building blocks

```
  A_r(x) = H^(r)_{n+x} − H^(r)_x ,   B_r(x) = H^(r)_{n−x} − H^(r)_x
  α := A₁(k) − A₁(l) ,   β := B₁(k) − B₁(l) ,   Ψ := ½α + β
  T(n,k,l) = C(n+k,n) C(n,k)² C(n+l,n) C(n,l)² C(n+k+l,n)
```

Verification, all from an **independent** re-implementation of the closed formulas
(not from the fitted coefficient vectors):

* `[VERIFIED exact over ℚ, n = 0…34, zero discrepancies]` — `work/z5cf/final_forms.py`,
  `verify_compact.py`, exact `Fraction` arithmetic from `core.T` / `core.Hs`;
* `[VERIFIED against EVERY exact ladder value n = 0…360, at two primes, zero
  discrepancies]` — `work/z5cf/verify_full.py` (722 checks per form);
* `L_BZ·(Σ T·ŵ₃) = L_BZ·(Σ T·w₅) = 0` exactly for `n = 0…31`;
* coefficients obtained by CRT over six primes + rational reconstruction, then
  re-derived by exact-ℚ solve on a prescribed support with held-out levels.

**`w₅` expands to 27 monomials of degree ≤ 3 in 13 symbols** (was 178 monomials,
degree ≤ 5, in the difference alphabet). **`ŵ₃` expands to 7 monomials of degree ≤ 2
in 8 symbols.** Both are exact minimum supports inside their (stated) search spaces.

**The single idea that unlocked it:** every previous campaign searched an alphabet of
*differences* — `A_r(x)`, `B_r(x)`, `C_r`, `N_r`, and the extensions `R_r(k)`,
`Y_ab`, `V_ab`, `Z_ab`. Apéry's own minimal form `b_n = Σ C(n,k)²C(n+k,k)²(2H⁽³⁾_n −
H⁽³⁾_k)` is **not in any such alphabet** — `H⁽³⁾_k` is not a difference. Searching the
**bare** alphabet `H^(r)_x`, `x ∈ {n, k, l, n±k, n±l, k+l, n+k+l}` (the nine symbols
you get by differentiating the five binomials of `T`) is a strictly larger space, and
the weight-5 row lives in its degree-3 part.

---

## 1. Why this does not contradict the recorded negatives

| recorded negative | its space | why the bare search is a different object |
|---|---|---|
| `PHASE2_CERTS` §16: *no degree-≤3 solution in any alphabet*, `D≤3` inconsistent at 271–449 excess equations | (a) `A,B,C,N`; (b) `+R_r(k)`; (c) nested `Y,V,Z` | **all three are difference alphabets.** `H⁽¹⁾_k` alone is in none of them. A bare degree-3 monomial such as `H⁽¹⁾_k H⁽¹⁾_l H⁽³⁾_{n+k}` is not a difference-alphabet degree-3 monomial. |
| `REFOLD.md`: *no ≤4-symbol refold*, 0 of 171/235 masks | `{A,B,C,N}_{r≤3}`, poly coefficients deg ≤3, letter deg ≤4 | same alphabet restriction; `REFOLD` §3 caveat (b) explicitly lists `D_r` / other alphabets as **not covered** |
| `PROOF_LB5_CAMPAIGN` §3.3: 149 symmetric weight-5 monomials, ≤3 factors, inconsistent | difference alphabet | ditto |

Both facts are true simultaneously and were re-measured here:

```
weight 5, degree <= 3, difference alphabet  : INCONSISTENT   (PHASE2_CERTS §16, N=600)
weight 5, degree <= 3, BARE alphabet        : CONSISTENT     165 cols, rank 164,
                                              157 excess equations at q=33554467
                                              and 78–157 excess at q=33554393, N=320
```

The "depth-2 / purity" reading of the old negative (`ζ(5)+2ζ(2)ζ(3)` is depth 2, so
harmonic *products* cannot span it) was a diagnosis of the **difference** alphabet
only. In the bare alphabet the depth-2 content is carried by the three-fold products
`H⁽¹⁾_x H⁽¹⁾_y H⁽³⁾_{n+k}` — 18 of the 27 monomials.

---

## 2. The search, exactly as run

Design matrix rows `n`, columns = weight-`W` monomials in the nine bare symbols,
entry `Σ_{k,l} T(n,k,l)·monomial mod q`; `k↔l` orbit-reduced (`T` is symmetric).
Code: `work/z5cf/design2.py` (numpy, factorial tables), `bare.py`, `probe.py`,
`t1_alpha.py`, `small_sweep.py`. A hard guard rejects any verdict with fewer than
40 excess equations.

### 2.1 Positive results `[VERIFIED, excess equations as stated]`

| target | alphabet | deg | cols | rank | excess | verdict |
|---|---|---|---|---|---|---|
| `P̂` | all 9 symbols | ≤3 | 143 | 77 | 94 | CONSISTENT |
| `P̂` | `{n,k,l,n+k,n+l}` | ≤2 | 16 | 16 | 155 | CONSISTENT, **unique** |
| `P̂` | `{k,l,n±k,n±l}` | ≤2 | 21 | 20 | 181 | CONSISTENT |
| `P` | `{k,l,n±k,n±l}` | ≤3 | 165 | 164 | 157 | CONSISTENT (q₂), 78 (q₁, N=320) |
| `P` | `{n,k,l,n±k,n±l}` | ≤3 | 254 | 243 | 78 | CONSISTENT |

`{k, l, n+k, n+l, n−k, n−l}` is the **minimal** `k↔l`-closed bare alphabet for weight 5:
the exhaustive sweep of all 63 non-empty orbit-closed sub-alphabets at every degree
`≤ 5` (guard ≥ 40 excess) returns only the two rows above (`work/z5cf/small_w5.log`).

### 2.2 Negatives `[EXCLUDED with bounds]`

| statement | bound |
|---|---|
| no weight-3 form, degree-1 only (all 9 bare symbols, and an 18-symbol extension) | rank(A|b) = rank(A)+1, 155–170 excess |
| no weight-3 form with ≤ 5 monomials in the 9-symbol degree-≤3 bare space (143 cols) | exhaustive, 477 191 prefixes, N = 170 |
| no weight-3 form with ≤ 6 monomials in the 6-symbol degree-≤2 bare space (21 cols) | exhaustive; **minimum = 7** |
| **no weight-5 form in the TAME bare alphabet `{n,k,l,n−k,n−l}`, any degree ≤ 5** | 262 cols, rank 250, 91 excess, N = 340 |
| **no weight-3 form in the TAME bare alphabet, any degree ≤ 3** (= all of weight 3) | 35 cols, rank 33, 168 excess, N = 200 |
| no weight-5 form of degree ≤ 2 in all 9 bare symbols | 96 cols, rank 88, 253 excess, N = 340 |
| no weight-5 form with ≤ 5 monomials in the 6-symbol degree-≤3 bare space (165 cols) | exhaustive, 735 130 prefixes, N = 200 |
| no "quadratic-free" Horner weight-5 form `H⁵+c₁H⁴+c₂H³` with `c₁,c₂` single letters | exact ℚ, 13- and 19-monomial supports, inconsistent |
| no weight-5 form whose `H⁽³⁾_{n+k}` quadratic uses only 4 of the 6 symbols (`{k,l,n+k,n+l}`, `{k,l,n−k,n−l}`, `{n±k,n±l}`) | exact ℚ, 19 cols, 45 equations, 26 excess, each inconsistent |

The last row is the structural reason the 27 terms cannot be shortened much: the
quadratic must mix the `n+·` and `n−·` families, because `−½αΨ = −¼α² − ½αβ`
genuinely needs both `α` and `β`.

---

## 3. Structure — and what it buys the certification route

`PHASE2_CERTS` §15.2's cost law: the support of `E(w)/T` that creative telescoping
must close grows like `2^d` in the maximum monomial **degree**, not in the weight.
Every bare letter `H^(r)_{linear in n,k,l}` has **rational** `n`-, `k`- and
`l`-differences, so the `∂`-module of `T·w` is exactly the set of sub-monomials.

| representative | terms | max degree | symbols | shift-closure (= CT-module rank) |
|---|---|---|---|---|
| `w5_Rbase` | 70 | 4 | — | 100 |
| `w5_allp` | 178 | 5 | — | 208 |
| `w₅^I` (`w5_exIII_allp`) | 207 | 5 | — | 220 |
| **`w₅` (this work)** | **27** | **3** | **13** | **64** |
| `ŵ₃` (original) | 19 | 3 | 17 | 19 |
| `ṽ` (REFOLD) | 6 | 2 | 10 | 11 |
| **`ŵ₃` (this work)** | **7** | **2** | **8** | **15** |

**The weight-5 gain is 3.2–3.4× in CT-module rank** (64 against 208–220), and lands
inside §15.2's own "`D = 3` → support ≈ 50, ~4× saving" cost class — the class the
campaign declared unreachable. At weight 3 the gain is neutral (`ṽ`'s 11 is still the
smallest closure), so **`ṽ` remains the right weight-3 object for certification; the
new weight-3 form is valuable as the *shape* that generalises**, not as a cost win.

### 3.1 The shape, and the ζ(3) precedent

```
   ŵ₃ = H⁽³⁾_{n+k}  −  Ψ · H⁽²⁾_{n+k}
   w₅ = H⁽⁵⁾_{n+k}  +  ½(α−β) · H⁽⁴⁾_{n+k}  +  [ ¼(A₂(k)+A₂(l)) − ½αΨ ] · H⁽³⁾_{n+k}
```

A **Horner expansion in the single letter tower `H^(r)_{n+k}`**, with coefficients of
weight 0, 1, 2. The weight-3 coefficient `Ψ = ½α + β` reappears inside the weight-5
one as `−½αΨ` — the rows are not independent objects, the ζ(5) row is built on the
ζ(3) row's coefficient.

`MINIMAL_FORM_PROOF` §8.0/§8.5 identified the governing structural question: the
rank-2 template works when the letters are organised by a **single antisymmetric
combination** `δ`, and "dies precisely when the letters are not". Here everything is
built from **exactly two antisymmetric combinations**, `α = A₁(k)−A₁(l)` and
`β = B₁(k)−B₁(l)`, plus one symmetric weight-2 letter `A₂(k)+A₂(l)`. So the BZ family
is a **rank-3** instance of the same mechanism (`{1, α, β}`), not a breakdown of it.
That is the precise sense in which the ζ(2)-Apéry obstruction of §8.5 generalises
rather than blocks.

### 3.2 The collapse criterion of §10, as it actually applied

§10 asked for a weight whose `n`-difference collapses to a single hypergeometric term.
The operative version is stronger and simpler: **every letter of the new forms has a
rational `n`-difference**, because a bare `H^(r)_{x(n,k,l)}` differences to
`1/(x+1)^r`. Apéry's `2H⁽³⁾_n − H⁽³⁾_k` is the degree-1 case of exactly this. The
*fitting* consequence is what did the work — degree-1 bare weights miss `P̂` by exactly
one dimension (rank 6 vs 7) at both weights, and the first degree that closes is 2 for
`P̂` and 3 for `P`.

---

## 4. T3 — the congruences, and tameness

### 4.1 Row congruences, re-measured on the exact ladders `n ≤ 360`

`[VERIFIED, 0 failures, p ∈ {7,11,13,17,19,23}, all cells n = ap+r ≤ 360]`

| statement | floor |
|---|---|
| `Q_{ap+r} − Q_a Q_r` | 1 |
| `p³P̂_{ap+r} − P̂_a Q_r` | 0 in general; **1 exactly when `P̂_a ∈ ℤ_p`** (7/33/65/119/152/85 non-integral cells at p=7/11/13/17/19/23) |
| `p⁵P_{ap+r} − P_a Q_r` | 1 |

This reproduces `PROOF_LB5_CLOSEOUT` §2.0's corrected statement exactly.

### 4.2 Hypotheses of Theorem LB (`LBW_GENERAL`) for the new forms

| hypothesis | verdict |
|---|---|
| (H1) Lucas/carry dichotomy | **holds** — Theorem A's Lemma 4 `[PROVED]` |
| (H2) product region, `Σ_{Σ_r} T_lo = Q_r` | **holds** — Theorem A `[PROVED]` |
| (H3) digit compatibility `⌊x/p⌋ = x(a,b,c)` | **holds, `[VERIFIED 0 violations]` for all nine arguments** over every cell with `p ∤ T(n,k,l)`, `p = 5,7,11,13` (210 / 1122 / 11 556 / 28 392 surviving cells). The surviving set is exactly `{r+s+t < p}`. |
| (H4) coefficient clause `c_j ∈ ℤ_(p)` | **holds for every `p ≥ 3`** — denominators of `ŵ₃` are `{2}`, of `w₅` are `{2,4}` |
| (H4) **tameness clause `0 ≤ x ≤ n`** | **FAILS** — `n+k`, `n+l` reach `2n` |
| (H5) χ-homogeneity | holds trivially (`e = 0`) |

> **So tameness does NOT now hold, and it cannot be arranged.** `[EXCLUDED]` — there
> is no weight-3 (degree ≤ 3 = all of weight 3, 168 excess equations) and no weight-5
> (degree ≤ 5 = all of weight 5, 91 excess equations) representative in the tame bare
> alphabet `{n,k,l,n−k,n−l}`. The non-tameness is forced by the alphabet, not chosen.

### 4.3 The two-layer split, executed `[VERIFIED, exact, p = 5,7,11]`

`work/z5cf/t3_layers.py` splits `p^w Σ_{k,l} T·w` into the vanishing layer `{p | T}`
and the surviving layer, and measures each:

| form | `v_p(p^w · vanishing layer)` (Theorem LB needs ≥ 1) | `v_p(p^w · surviving − Y_a Q_r)` | `v_p(p^w Y_n − Y_a Q_r)` |
|---|---|---|---|
| `ŵ₃ → P̂` | **−1** | −1 | 0 |
| `w₅ → P` | **0** | 0 | **1** |

**The split is invalid termwise, and the two layers' defects cancel exactly** — the
signature `LBW_GENERAL` records for the non-tame family (Domb, ε, s₇, E). So the
elementary proof does **not** now go through; what it needs is precisely the
Lemma-D substitute, and nothing else: (H1),(H2),(H3),(H5) are all in place and the
whole obstruction is localised in the two arguments `n+k`, `n+l`.

The deficit is now **exactly one order** at weight 5 (0 instead of ≥1). The pole that
causes it is the level-`a` letter `H^(r)_{a+b}` with `a+b ≥ p` — i.e. the *same*
indicator `α = [a+b ≥ p]` that `PHASE2_FINAL` §2.1's pole calculus is built from. This
is a sharper localisation of the weight-5 blockage than anything previously recorded.

---

## 5. T3b — the Frobenius matrix congruence

Objects: `Φ_n = [[Q_n,0,0],[P̂_n,Q_n,0],[P_n,X_n,Q_n]]`, `D = diag(1,p³,p⁵)`;
conjugation `Φ̂ := DΦD^{-1}` multiplies entry `(i,j)` by `p^{w_i−w_j}`, `w = (0,3,5)`.
All exact, `n ≤ 360`, `p ∈ {7,11,13,17,19,23}` (`work/z5cf/t3b_*.py`).

### 5.1 The naive product form is dead `[EXCLUDED]`

`Φ̂_{ap+r} ≡ Φ̂_a Φ̂_r (mod p)` fails at **every** prime, and not marginally: the
residual has `v_p = −1` (not even `p`-integral). Reason: for `r < p`,
`v_p(P̂_r) ≥ −1` and `v_p(P_r) ≥ 0`, so `p³P̂_r ≡ p⁵P_r ≡ 0 (mod p)` — the whole
low-digit off-diagonal is annihilated by its own scaling, while the left-hand side
`p³P̂_{ap+r}` retains a genuine pole. Any fixed placement of `p`-powers has this
disease. (`P_0 = P̂_0 = 0`, `Q_0 = 1` kills `B(a)B(r)` independently, as expected.)

### 5.2 What does close — the graded/scalar form `[VERIFIED]`

The sharpness of the grading is a **spike, not a step** — the exponent scan of
`v_p(p^s Y_n Q_q − Y_q Q_n)`, `q = ⌊n/p⌋`, over `s = 0…7`:

```
  Phat: s=0..2 give -8..-2 ; s=3 gives +1 ; s=4..7 fall back to -5..-1
  P   : s=0..4 give -14..-1 ; s=5 gives +2 ; s=6,7 fall back to -9..0
```

Only `s = 3` and `s = 5` resonate — an assumption-free confirmation of
`diag(1, p³, p⁵)` from the data alone.

**The form that closes** is `D Φ_n D^{-1} ≡ Φ_a · (Q_r·I) (mod p)`, i.e. the low digit
acts by a **scalar**. In the `W`-normalisation (`Ŵ_n = P̂_n − H₃(n)Q_n`,
`W_n = P_n − H₅(n)Q_n`) it sharpens to

> **`( Q_n , p³Ŵ_n , p⁵W_n ) ≡ ( Q_a , Ŵ_a , W_a ) · u(a,r)`,  `u(a,r) := Q_r + p·a·Ψ_r`**

with `Ψ_r = Σ_{s,t≤r} T(r,s,t)·(H_{r+s}+H_{r+t}+H_{r+s+t}+H_r−2H_{r−s}−2H_{r−t})` the
Lemma-Phi functional. Measured floors `[VERIFIED, 0 failures, p ∈ {7,…,23}]`:

| graded piece | floor |
|---|---|
| `Q` (weight 0) | **2** |
| `Ŵ` (weight 3) | **1** |
| `W` (weight 5) | **2** |

### 5.3 The defect is exactly rank 1 — new `[VERIFIED, 6 primes]`

The first-order defect, as a matrix on the digit grid `(a,r)`, has **rank exactly 1**
at every prime, for all three rows:

```
  (Q_n − Q_a Q_r)/p          rank 1   (f(a) ∝ a·Q_a  — matches the PROVED mod-p² law)
  p³P̂_n − P̂_a Q_r            rank 1
  (p⁵P_n − P_a Q_r)/p        rank 1
```

and the **second**-order defect has **rank exactly 2** at every prime, for all three.
So the low digit acts by a scalar to second order and only splits into two channels at
the third — the first place where a genuine unipotent cross term could live.

### 5.4 Verdict on the cross entry `(3,2)` `[precise negative]`

Because the low-digit matrix is **scalar** mod `p²`, the `(3,1)` entry of `Φ_aΛ_r`
never sees `X_a`: the cross entry is neither constrained by, nor constrains, the other
entries. Any weight-2 row `X` obeying its own congruence `p²X_n ≡ X_a Q_r` completes
the matrix, and no choice is preferred. **The graded Frobenius congruence closes, and
it closes *split*: mod `p²` the extension carries no cross term.** A cross term can
only appear at order `p³`, where the defect first has rank 2.

### 5.5 Reconciliation with `PADIC_SEAM` §T3 `[VERIFIED, no contradiction]`

* multi-digit, `n = ap^s + …`: `v_p( p^{ws} Y_n − Y_a ∏Q_{r_i} ) ≥ 1` for `Y = P`,
  `w = 5`, `s = 1,2`, all six primes (floor exactly 1); `≥ 0` for `P̂`, `w = 3`.
* `PADIC_SEAM` §T3's form `p^{5s}P_{ap^s}Q_{ap^{s−1}} − p^{5(s−1)}P_{ap^{s−1}}Q_{ap^s}`
  measures floor **3** at `s = 1` and **6** at `s = 2` — exactly the recorded depth `3s`.
* The unrestricted ratio form `p⁵P_nQ_q − P_qQ_n` with multi-digit `q` degrades to
  `−2 … +2` (the `P_q ∉ ℤ_p` renormalisation), which is why the single-digit
  restriction in §5.2 is the right statement.

**New:** restricted to single-digit `q = ⌊n/p⌋ < p`, the ratio form has floor
**exactly 2 at weight 5** and **exactly 1 at weight 3**, uniformly over all six primes.
The two graded pieces have *different* ratio depths — the weight-5 row is the deeper
one, contrary to what the weight ordering would suggest.

---

## 6. Files (`work/z5cf/`)

| file | what |
|---|---|
| `bare.py`, `design2.py` | the bare-symbol alphabet, monomial enumeration, `k↔l` orbits, fast mod-`q` design matrices, modular RREF |
| `probe.py`, `t1_alpha.py`, `small_sweep.py` | consistency probes and the exhaustive 63-alphabet sweeps (with the excess-equation guard) |
| `minsupp.py` | minimum-support search (random projection + prefix elimination + hash matching, hits verified on the full system) |
| `extractCRT.py`, `fixsupp.py`, `extract3.py` | exact-ℚ extraction (CRT + rational reconstruction; prescribed support) with held-out verification |
| `verify_compact.py`, `final_forms.py` | **independent** exact verification of the closed forms + `L_BZ` residuals |
| `analyze.py`, `h3test.py` | size metrics, shift-closure, (H3)/(H4) tests |
| `t3_layers.py` | the two-layer split, executed |
| `t3b_frob.py`, `t3b2_defect.py`, `t3b3_ident.py`, `t3b4_scalar.py`, `t3b5_cross.py` | T3b: matrix congruence, defect ranks, rank-1 identification, scalar form, cross term, multi-digit |
| `w3_bare.json`, `w5_bare.json` | the fitted representatives, machine-readable |

---

## 7. What a successor should do next

1. **Run `Annihilator` / creative telescoping on `T·w₅`.** Its `∂`-module has rank
   **64**, against 208–220 for every previously offered weight-5 object. §15.2's cost
   model says this is the first weight-5 candidate in the tractable class. This is the
   single highest-value next action.
2. **Close the tameness gap with a Lemma-D substitute** for the two arguments `n+k`,
   `n+l`. Everything else in Theorem LB is verified; the deficit at weight 5 is
   exactly one order, and the pole indicator is the familiar `α = [a+b ≥ p]`.
3. **Identify the rank-2 second-order defect** (§5.3). It is the only place a
   Frobenius cross term can live, and it is cheap exact arithmetic on loaded data.
4. Do **not** re-run: the tame-alphabet searches (excluded at both weights with 91–168
   excess equations); degree-≤2 weight-5 in all nine bare symbols; the ≤5-monomial
   weight-3 search in the 143-column space; the naive matrix product form.
