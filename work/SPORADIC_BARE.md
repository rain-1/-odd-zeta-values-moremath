# SPORADIC_BARE — bare-alphabet harmonic decompositions for the eleven unproved sporadic families

**Author:** mathematician-agent (River's odd-zeta program), 2026-07-26
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, code in `work/sporadic/`
**Labels:** `[PROVED]` · `[VALIDATED]` · `[VERIFIED range]` · `[EXCLUDED with bounds]`
**Reads:** `work/ZETA5_CLOSEDFORM.md`, `work/LBW_GENERAL.md` (authoritative), `work/APERY_DEFECT.md`
**No Wolfram kernel was started.** Everything below is pure-Python exact arithmetic
(numpy int64 mod primes < 2³¹ for the searches; `fractions.Fraction` for every verdict).

---

## 0. HEADLINE

**The new proved count is 4 — unchanged.** The bare alphabet does not rescue any of the
eleven, and the reason is now pinned down precisely rather than left open.

1. **The Lemma-D four (α, ε, s₇, E) admit no tame decomposition, exhaustively.**
   For each family the set of tame letter arguments is *finite and explicitly computable*
   (Lemma T below), so the searches are complete over **all** tame constant-coefficient
   monomial spaces — not merely over the natural Γ-arguments. Every one is
   `[EXCLUDED]` with 106–187 excess equations. **E's verdict is negative**: the programme
   does not get its first proved χ ≠ 1 instance this way.
2. **A genuine new object was found and killed**: Zagier's (d) has a *second, fully tame*
   binomial representation `A(n) = Σ_k 4^{n−2k} C(n,2k) C(2k,k)²` `[VERIFIED n = 0…30]`,
   on whose support **every** Γ-argument lies in `[0,n]`. It supports **no** harmonic
   decomposition at all — 230 columns, rank 230, 90 excess `[EXCLUDED]` — while E's own
   representation at the same `N` is consistent. A sweep of **4.4 M tame templates**
   (≤ 5 binomial factors, support divisor `m ≤ 5`) finds this one representation for E and
   **none whatsoever** for α, ε, s₇.
3. **[PARTLY RETRACTED 2026-07-26 — see the correction box in §2.5 and `work/LEMMAD_CHECK.md`.
   The measurements below stand; the conclusion drawn from them does not: (H2) does not hold
   outright, and the displayed valuation inequality is false for α, ε, E.]**
   **The (H4) obstruction is localised to the vanishing layer alone.**
   `[VERIFIED, 0 violations, p = 5…23, all cells n = ap+r < p²]` — on the *surviving*
   layer `{p ∤ S(n,k)}` the non-tame arguments `2k, 2n−2k, 2k−n` are **already harmless**:
   digit compatibility (H3) holds and `⌊x/p⌋ ≤ p−1` exactly, so every descended letter is
   `p`-integral. On the vanishing layer `⌊x/p⌋` reaches exactly `2p−1`. So (H1),(H2),(H3),
   (H5) hold outright and the *entire* content of a Lemma-D substitute is the single
   inequality `v_p(S) + v_p(p^w w) ≥ 1` on `{p | S}`.
4. **The conjectural seven stay conjectural**, now with stated bounds: 30 searches,
   every complete tame alphabet, up to 520 columns, 55–193 excess equations, all
   `[EXCLUDED]`. New alongside them: **C and δ possess no tame representation whatsoever**
   (support-checked sweep, §3.1), so they could not be proved by Theorem LB even if a
   decomposition were found.
5. **New, and a clean answer to `APERY_DEFECT` §7.1:** the Γ-deformation-with-primitivity
   mechanism produces exactly the *degree-1* weights `Σ_x λ_x H^{(w)}_x`. Probing that
   class over all fifteen families: **γ (Apéry ζ(3)) is the only one for which it is
   consistent.** All fourteen others `[EXCLUDED]`, 44–56 excess. The Γ-derivation is a
   property of Apéry's ζ(3) row, not of the sporadic class.
6. **Two structural facts worth keeping.** (a) Padding a homogeneous weight with a
   *lower*-weight tame part is **vacuous** (proof in §2.3) — so weight-homogeneity is
   forced and the negatives above are complete. (b) The **kernel dimension** of the design
   matrix is a reliable diagnostic: families with a decomposition have large kernels
   (E 37/65, α 19/40), C/F/s₁₈ have small ones, and **B, δ, ζ, η have rank = columns in
   every run** — no ℚ-relation at all between their summand and the harmonic letters.

---

## 1. T1 — the harness, validated before any negative was trusted `[VALIDATED]`

Code: `work/sporadic/core.py` (letters, monomials, modular + exact tables, CRT/rational
reconstruction, exact checker), `fams.py` (all 15 families + `E2` as cell generators),
`fit.py` (design matrices, consistency, exact extraction, greedy minimisation),
`check1.py` (sanity layer 0).

Ansatz, as in `LBW_GENERAL` T3:

```
  B(n) = Σ_cells S(n,k[,l]) · w(n,k[,l]),
  w    = Σ_j c_j ∏_t L_{jt}(x_{jt}),   c_j ∈ ℚ constants,
  L    = H^{(r)}(x) = Σ_{m≤x} 1/m^r          (BARE, not a difference)
       = K_χ^{(r)}(x) = Σ_{m≤x} χ(m)/m^r,
  x    = integer linear forms in (n,k[,l]),   Σ_t r_{jt} = w  (homogeneous, see §2.3).
```

Bracketed families (η, s₁₈) get **two cells per k**, the two binomials of the bracket kept
separate so that their Γ-arguments may differ — a strictly larger ansatz than a single
weight multiplying the bracket.

### 1.1 Sanity layer 0 `[VERIFIED n = 0…14, all 16 families]`

Every summand reproduces `A(n)` from its recurrence **exactly**, and the mod-`q` summand
agrees with the exact summand **cell by cell** (the ordering of cells matters and is
checked, not assumed).

### 1.2 Known decompositions recovered `[VALIDATED, exact ℚ, held out n = 101…108]`

| seq | recovered form | terms | matches |
|---|---|---|---|
| **γ** | `(1/3)H³_n − (1/6)H³_k` | 2 | `LBW` T3 ✔ (⇒ `b_n = Σ C(n,k)²C(n+k,n)²(2H³_n − H³_k)`) |
| **A** (Franel) | `(1/4)H²_k + (3/4)H_k(H_k − H_{n−k})` | 3 | ✔ |
| **s₁₀** | `(1/5)H²_k + (4/5)H_k(H_k − H_{n−k})` | 3 | ✔ |
| **D** | `(1/5)[H²_n + H_k(2H_k − H_n − H_{n−k})]` | 4 | ✔ |
| **E** | `(1/2)K^{(2)}_{2k} + (3/4)H_k(K_{2k}−K_{2n−2k}) − (1/2)H_{2k}(K_{2k}−K_{2n−2k})` | 5 | ✔ verbatim |
| **ε** | 10 terms in `H^{(1,2,3)}` at `{k, n−k, 2k, 2k−n}` | **10** | ✔ (LBW: 10) |
| **s₇** | 8 terms in `H^{(1,2)}` at `{n, k, n−k, 2k}` | **8** | ✔ (LBW: 8) |
| **α** (Domb) | 17 terms at `{k, n−k, 2k, 2n−2k}` | 17 | LBW has **14**; my minimiser is greedy, not optimal |

The independent recovery of ε's 10 and s₇'s 8 (never given explicitly in `LBW`) is the
strongest single validation. Every verdict in this file carries an **excess-equation
guard**: no CONSISTENT/INCONSISTENT verdict is reported below 40 excess equations
(the actual figures are 55–193).

### 1.3 Second-prime recheck of every headline negative `[VERIFIED]`

An INCONSISTENT verdict mod one prime `q` implies inconsistency over ℚ *unless* `q` divides
a denominator of the would-be rational solution. Every headline negative in §2 and §3 —
E (all four tame variants), E2 (tame and full-10), α, ε, s₇, and the strongest run for each
of B, C, δ, ζ, η, s₁₈, F — was therefore recomputed at a **second, unrelated prime**
`q = 1 073 741 717`. **All verdicts and all ranks are identical**, and the positive control
(E's own representation, 65 cols) still comes out CONSISTENT with rank 37. No verdict in
this file rests on a single modulus.

---

## 2. T2 — the Lemma-D four: no tame decomposition `[EXCLUDED, exhaustive]`

### 2.1 Lemma T (the tame alphabet is finite and known) `[PROVED]`

*Let the summation support be `k ∈ [0, n/m]`. Then the integer linear forms
`x = αn + βk` with `0 ≤ x(n,k) ≤ n` on the whole support, for every `n`, are exactly*

> `{ j·k : 1 ≤ j ≤ m }  ∪  { n − j·k : 0 ≤ j ≤ m }`   (`2m+1` forms).

*Proof.* `x` is linear in `k`, so `0 ≤ x ≤ n` on `[0, n/m]` iff it holds at both endpoints.
At `k = 0`: `0 ≤ αn ≤ n` for all `n` forces `α ∈ {0,1}`. If `α = 0`, the endpoint `k = n/m`
gives `0 ≤ βn/m ≤ n`, i.e. `0 ≤ β ≤ m`. If `α = 1`, it gives `0 ≤ n + βn/m ≤ n`, i.e.
`−m ≤ β ≤ 0`. ∎ (For a support `k ∈ [n/2, n]` substitute `i = n−k`; for double sums apply
the argument in each variable.)

**Consequence:** the tame search space of each family is a *finite, completely determined*
list, so the exclusions below are exhaustive over all tame monomial spaces — not merely
over the arguments the summand's Γ-factors happen to supply.

| family | support | complete tame form set |
|---|---|---|
| α (Domb) | `0 ≤ k ≤ n` | `{n, k, n−k}` |
| ε | `n/2 ≤ k ≤ n` | `{n, k, n−k, 2k−n, 2n−2k}` |
| s₇ | `n/2 ≤ k ≤ n` | `{n, k, n−k, 2k−n, 2n−2k}` |
| E | `0 ≤ k ≤ n` | `{n, k, n−k}` |
| E2 (§2.2) | `0 ≤ k ≤ n/2` | `{n, k, 2k, n−k, n−2k}` |

### 2.2 The searches `[EXCLUDED, bounds as stated]`

`N` = number of fitting rows `n = 1…N`; excess = (non-trivial rows) − rank.

| target | alphabet | cols | rank | excess | verdict |
|---|---|---|---|---|---|
| **E** w=2 | tame `{n,k,n−k}` + χ₋₄, **(H5) e = 1** | 12 | 7 | 153 | **INCONSISTENT** |
| **E** | tame + χ₋₄, all monomials (e = 0,1,2) | 27 | 17 | 143 | **INCONSISTENT** |
| **E** | tame + χ₋₄ **and** χ₋₃, χ₈ (wrong conductors, control) | 90 | 54 | 106 | **INCONSISTENT** |
| **E** | tame, pure harmonic (control) | 9 | 6 | 154 | INCONSISTENT (expected) |
| **E2** | complete tame `{n,k,2k,n−2k}` + χ₋₄, e=1 | 20 | 20 | 140 | **INCONSISTENT** |
| **E2** | complete tame 5 forms + χ₋₄, all | 65 | 65 | 95 | **INCONSISTENT** |
| **E2** | **all 10 args, tame or not** + χ₋₄ (`N`=320) | 230 | 230 | 90 | **INCONSISTENT** |
| **E** | control at `N`=320, `{n,k,n−k,2k,2n−2k}` + χ₋₄ | 65 | 37 | 283 | CONSISTENT ✔ |
| **α** w=3 | tame `{n,k,n−k}` = the **entire** tame weight-3 space | 22 | 13 | 187 | **INCONSISTENT** |
| **α** | control `{k,n−k,2k,2n−2k}` (non-tame) | 40 | 19 | 181 | CONSISTENT ✔ |
| **ε** w=3 | complete tame 5 forms = **entire** tame weight-3 space | 65 | 65 | 135 | **INCONSISTENT** |
| **ε** | tame subsets `{k,n−k,2k−n}`, `{n,k,2k−n}` | 22 | 22 | 178 | INCONSISTENT |
| **s₇** w=2 | complete tame 5 forms = **entire** tame weight-2 space | 20 | 20 | 180 | **INCONSISTENT** |

`N = 160` (E), `200` (α, ε, s₇), `320` (E2 control). Held-out exact-ℚ checks on
`n = 161…166 / 201…206` for every CONSISTENT row.

**E2, the second representation of Zagier's (d).** `[VERIFIED exact, n = 0…30]`

> `A_E(n) = Σ_k C(n,k) C(2k,k) C(2n−2k,n−k) = Σ_k 4^{n−2k} C(n,2k) C(2k,k)²`

Its support is `2k ≤ n`, so `n, k, 2k, n−2k` all lie in `[0,n]`: this is the only fully
tame representation of E, and the tame-template sweep (§2.4) shows it is the *only* one up
to refactoring (`4^{n−2k}C(2k,k)C(n−k,k)C(n,k)` is the same summand). It carries **no**
decomposition, tame or not. Two remarks on why: (i) its exponential factor `4^{n−2k}`
forces a `log 2` into any Γ-deformation, whose finite shadow `H_{2x} − H_x` needs the very
arguments `4k, 2n−4k, 2n` that were included and did not help; (ii) its design matrix has
**rank = columns** — no ℚ-relation at all between this summand and the harmonic letters,
in sharp contrast to E's own representation (rank 37 of 65).

### 2.3 Weight-homogeneity is forced — so §2.2 is complete `[PROVED]`

One could try to enlarge the space by *padding*: write `w = w_w + V` with `V` a tame
combination of monomials of weight `v < w` (formally raised to weight `w` by constant
letters `H^{(r)}_c`, `c` fixed). This is **vacuous**. For a tame monomial `M` of weight
`v`, `p^v M ∈ ℤ_(p)`, so `p^w M = p^{w−v}(p^v M) ≡ 0 (mod p)`; Theorem LB's proof then
delivers

    p^w B(n) ≡ χ(p)^e · B_w(a) · A(r) (mod p),   B_w(a) = B(a) − Σ_b S(a,b) V(a,b).

The measured law (`LBW` T2b, re-verified in §4) is `p^w B(n) ≡ χ(p)^e B(a)A(r)`, so
`Σ_b S(a,b)V(a,b) ≡ 0 (mod p)` is required for every `a < p` and every `p ≥ 5`; fixing `a`
and letting `p → ∞` forces `Σ_b S(a,b)V(a,b) = 0` for all `a`. The padding therefore
contributes nothing to `B` and nothing to the congruence. ∎

### 2.4 The tame-representation sweep `[EXCLUDED, 4.4 M templates per family]`

`work/sporadic/hunt.py`. Templates `S = (±1)^k · base^{c(n−jk)} · ∏ C(T_i,B_i)` with all
of `T_i, B_i, T_i−B_i` and the exponent drawn from the complete tame form set of Lemma T,
up to **5 binomial factors**, support divisor `m = 2,3,4,5`, all `(base,c)` with
`base^c = b` (forced, because at `n = 1` the support of any `m ≥ 2` template is `k = 0`
alone and every binomial is 1, so `A(1) = b = base^{c}`); matched against exact `A(n)` for
`n ≤ 25`. Scanned 11 074 / 279 054 / 602 888 / 3 529 500 templates at `m = 2,3,4,5`.

* **E**: exactly one summand, `E2` (in two factorisations).
* **α, ε, s₇**: **no tame representation exists** in this space.

*Caveat, stated honestly:* the sweep assumes the support is `k ∈ [0,n/m]`; a template built
from `m`-tame forms whose binomials do not actually force `k ≤ n/m` (e.g. C's own
`C(n,k)²C(2k,k)`, support `[0,n]`) is a **false positive** and must be re-checked. E2's
tameness was verified directly by measuring all argument ranges on its support
(`n = 30`: `k ∈ [0,15]`, `2k ∈ [0,30]`, `n−2k ∈ [0,30]`). The *negative* results are
unaffected by this caveat.

### 2.5 NEW — the obstruction lives only in the vanishing layer `[VERIFIED, 0 violations]`

`work/sporadic/t2_layers.py`. For each family, its known decomposition's arguments, every
prime `p = 5,7,11,13,17,19,23`, every cell `n = ap+r < p²` (`1 ≤ a < p`), every `k` with
`S(n,k) ≠ 0`, split by `p | S(n,k)`:

| family | args | surviving cells (p=5…23) | (H3) violations | non-`p`-integral letters | max `⌊x/p⌋` surviving | max `⌊x/p⌋` vanishing |
|---|---|---|---|---|---|---|
| γ | `n,k` | 72 … 20 592 | **0** | **0** | `p−1` | `p−1` |
| D | `n,k,n−k` | 72 … 20 592 | **0** | **0** | `p−1` | `p−1` |
| **α** | `k,n−k,2k,2n−2k` | 72 … 20 592 | **0** | **0** | **`p−1`** | **`2p−1`** |
| **ε** | `k,n−k,2k,2k−n` | 30 … 6 006 | **0** | **0** | **`p−1`** | **`2p−1`** |
| **s₇** | `n,k,n−k,2k` | 12 … 2 652 | **0** | **0** | **`p−1`** | **`2p−1`** |
| **E** | `k,2k,2n−2k` | 72 … 20 592 | **0** | **0** | **`p−1`** | **`2p−1`** |

(`2p−1` = 9, 13, 21, 25, 33, 37, 45 at `p` = 5, 7, 11, 13, 17, 19, 23 — measured, not assumed.)

**Why it is automatic on the surviving layer.** `p ∤ C(2k,k)` forces (Kummer) every base-`p`
digit of `k` to be `< p/2`; with `k = bp+s` that gives `2s < p`, hence
`⌊2k/p⌋ = 2b = x(a,b)` and `2b < p`. Likewise `p ∤ C(2n−2k,n−k)` gives `2(r−s) < p` and
`⌊(2n−2k)/p⌋ = 2(a−b) < p`. The wide arguments are therefore *self-taming* exactly where
the Lucas factorisation is alive.

> **Restatement of the gap.** For α, ε, s₇, E hypotheses **(H1), (H2), (H3), (H5) of
> Theorem LB all hold**, and (H4)'s tameness clause is needed for one purpose only: to make
> `p^w w(n,k)` `p`-integral on the **vanishing** layer, where `⌊x/p⌋ ∈ [p, 2p−1]` produces a
> single-layer pole of order ≤ `r` per letter. A Lemma-D substitute is therefore *exactly*
> the statement
>
> **`v_p(S(n,k)) + v_p(p^w w(n,k)) ≥ 1` for every `k` with `p | S(n,k)`,**
>
> and nothing else. `LBW` records that this fails termwise and that the two layers' defects
> cancel; combined with the above, the repair needed is a **single valuation inequality on
> one explicitly described set of cells**, with no digit-compatibility work left to do.

> ## ⚠ CORRECTION (2026-07-26) — the box above is WRONG. See `work/LEMMAD_CHECK.md`.
>
> The displayed inequality is **FALSE** for α, ε and E, and so is its aggregated weakening
> `v_p(Σ_{p|S} S·p^w w) ≥ 1`. `[FALSE with counterexample]`, exact rationals:
> **α, p = 5, n = 20 = 4·5+0, k = 5**: `v_5(S) = 1`, `v_5(p³w) = −2`, sum `= −1 < 1`
> (pole at `2n−2k = 30 ≥ p²`); **ε and E, p = 5, n = 15, k = 15**: sum `= 0 < 1`.
> Measured over all cells `n < p²`, `p = 5…23`: minimum `= −1` (α), `0` (ε, E), uniformly.
> This was already implied by `LBW`'s own `[VERIFIED]` data, which this file cites: a
> termwise bound implies the aggregated one, and `LBW` records the aggregated one failing.
>
> Two further corrections. **(H2) does *not* hold outright**: its clause "the surviving set
> is `{0 ≤ b ≤ a} × Σ_r`" is false for every `a ≥ (p+1)/2` (α, p = 5, a = 3: `b = 0` is
> dropped, `p | C(6,3)`), and the `b`-side hides a second, base-level defect
> `Δ(a) = Σ_{b : p|S(a,b)} S(a,b)w(a,b)`. And **no choice of decomposition repairs any of
> this**: the exact ℚ-kernel of the fit was computed and the resulting `𝔽_p` system is
> inconsistent at every prime (for E the kernel cannot move `Δ(a) mod p` at all).
>
> **The correct target** is the cancellation identity, `[VERIFIED, 0 failures, p = 5…23]`:
> `Σ_{k : p|S(n,k)} S(n,k)·p^w·w(n,k) ≡ χ(p)^e · Δ(a) · A(r) (mod p)`, `n = ap+r`.
> It is a *descent* congruence, not a local valuation bound.
>
> **s₇ is the exception and the real opportunity:** for s₇ the displayed inequality is
> `[TRUE in the tested range]` (`p ∈ {5,11,13,17,19,23,29,31,37,41}`, 0 violations, minimum
> exactly 1), and so is the base-level one, so s₇ — and s₇ alone — is one bounded local
> lemma away from proved. **The count this route can reach is 4 → 5, not 4 → 8**, and it
> does not deliver a χ ≠ 1 instance.

---

## 3. T3 — the conjectural seven: no decomposition found `[EXCLUDED with bounds]`

Complete tame form sets (Lemma T), and the searches run. All 30 runs **INCONSISTENT**;
`N` was chosen in each case so that excess ≥ 55.

| fam | w | χ | complete tame forms | searches (cols / excess), all INCONSISTENT |
|---|---|---|---|---|
| **B** | 2 | χ₋₃ | `{n,k,2k,3k,n−k,n−2k,n−3k}` (7, complete) | tame7 pure 27/193; tame6+χ₋₃ e=1 42/178; tame6+χ₋₃ all 90/130; **tame7+χ₋₃ all 119/60**; +`n+k` 119/101; wide-10 e=1 110/60 |
| **C** | 2 | χ₋₃ | `{n,k,n−k}` (3, complete) | tame3+χ₋₃ e=1 12/188; tame3+χ₋₃ all 27/173; full-6+χ₋₃ 90/114; **conductor-3 args `{n,k,n−k,2k,3k,3n−3k}`+χ₋₃ 90/64**; wide-8 e=1 72/61; all-11-args e=1 132/63 |
| **F** | 2 | χ₋₃ | `{n,k,n−k,l,k−l,n−l,n−k+l}` (7, complete) | tame5+χ₋₃ e=1 30/179; tame5 all 65/153; tame5 pure 20/185; **complete tame7 e=1 56/82**; tame7 pure 35/72; tame7 all (d≤2) 119/104; wide-8 (`2l,2k−2l,n+k`) 152/112 |
| **δ** | 3 | 1 | `{n,k,2k,3k,n−k,n−2k,n−3k}` (7, complete) | tame6 pure 98/102; full7 pure (d≤3) 140/60; +`n+k` 140/60; **tame5+χ₋₃ 330/70**; tame6 (d≤2)+χ₋₃ e=1 78/60 |
| **ζ** | 3 | χ₋₃ | `{n,k,n−k,l,n−l,k−l,k+l−n}` (7, complete) | tame6+χ₋₃ e=1 204/56; tame6 pure 98/102; **complete tame7+χ₋₃ (d≤2) e=1 105/63**; tame7 pure (d≤3) 140/75; tame5+χ₋₃ e=1 130/60; wide-8 (d≤2) e=1 136/66 |
| **η** | 3 | χ₅ | `{n,k,2k,3k,4k,5k,n−k,n−2k,n−3k,n−4k,n−5k}` (11, complete) | tame6+χ₅ e=1 204/69; tame6 pure 98/109; **tame6+χ₅ all 520/87**; **complete tame11+χ₅ (d≤2) e=1 253/60**; tame11 pure (d≤3) 418/60; wide-8 (d≤2) e=1 136/62 |
| **s₁₈** | 2 | χ₋₃ | `{n,k,2k,3k,n−k,n−2k,n−3k}` + bracket form `tb` (8) | tame6+χ₋₃ e=1 42/159; tame6+χ₋₃ all 90/112; tame6 pure 27/174; full-8+χ₋₃ 152/55; wide-10 e=1 110/63; **tame8+χ₋₃ all 152/62** |

Notes on the bounds. Rows marked in bold are the strongest (largest space) for that family.
Where `d ≤ 2` appears, monomials of degree 3 in weight-1 letters were **not** covered — the
column counts at full degree (424–1088) would need `N ≥ 500–1100` rows, which for the two
double sums is beyond a reasonable budget; those gaps are stated, not hidden. For B, C, δ
and s₁₈ the *complete* tame space at *full* degree was reached.

**Structural diagnostic (new).** Rank vs columns is informative:

| family | best rank/cols | reading |
|---|---|---|
| E, α (have forms) | 37/65, 19/40 | large kernel — letters and summand are strongly related |
| C, F, s₁₈, η | 86/90, 100/152, 107/110, 153/156 | small kernel — some relation, target still outside |
| **B, δ, ζ** | **= cols in every run** | **no ℚ-relation at all** between summand and harmonic letters |

B, δ, ζ are therefore the least likely of the seven to yield to any enlargement of this
ansatz; C, F, s₁₈ the most likely. (B and δ are two of the three sequences with **no**
archimedean Apéry limit, `LBW` exception 2.)

### 3.1 Tame-representation sweep for the seven `[EXCLUDED, 4.4 M templates per family]`

Same sweep as §2.4, now with the **support check applied** (each raw hit is re-tested by
measuring every form on the *actual* nonzero support for `n = 6…24`; without this test the
sweep produces false positives, e.g. C's own `C(n,k)²C(2k,k)`, whose forms are `m = 2`-tame
but whose support is `[0,n]`, so `2k` reaches `2n`):

| family | raw hits | genuinely tame | what they are |
|---|---|---|---|
| **B** | 60 | **20** | all 20 are the *same* summand `(−1)^k3^{n−3k}·n!/(k!³(n−3k)!)` refactored; they contribute the arguments `n−k, n−2k`, which are already in B's complete tame set and were searched (119 cols / 60 excess) |
| **C** | 12 | **0** | every hit fails the support test |
| **δ, η, s₁₈** | 0 | **0** | none exists in the template space |
| **F, ζ** | 0 | **0** | but see below — these are *double* sums and the sweep only covers single sums |

**Consequence for the proof route.** Of the seven, only **B, F, ζ** and (partly) **s₁₈, η**
have any tame representation at all: F's native arguments `{n,k,n−k,l,k−l}` are *all* tame,
ζ's are tame except `k+l`, s₁₈'s except `t` and `2n−2k`, η's except `3n` and `t`. **C and δ
have none** — so even if a decomposition were found for C or δ in a wide alphabet,
Theorem LB could not be applied to it without a Lemma-D substitute. That is a sharper
statement than "no decomposition found".

**C, specifically.** `LBW` exception 5 says C admits no decomposition even with χ₋₃-letters
and diagnoses "its conductor-3 letters need arguments not present in `C(n,k)²C(2k,k)`".
Re-examined here with bare twisted letters at explicitly conductor-3 arguments `3k`,
`3n−3k`, `3n` (which the summand indeed does not supply): still **INCONSISTENT**, 90 cols /
64 excess and 132 cols / 63 excess. So supplying the conductor-3 arguments by hand is *not*
sufficient — the obstruction is not merely the missing arguments. C's tame form set is only
`{n,k,n−k}` (its `2k` reaches `2n`), so C could not be proved by Theorem LB even if a form
were found in the wide alphabet.

---

## 4. T4 — congruences, tameness, and the proof status

### 4.1 The congruence `p^w B(ap+r) ≡ χ(p)·B(a)·A(r) (mod p)` `[VERIFIED, 0 failures]`

`work/sporadic/t4.py`, exact ℚ, all `1 ≤ a < p`, `0 ≤ r < p`, `n = ap+r < p²`,
`p = 5, 7, 11, 13, 17, 19` — **2 884 cells per family, 43 260 cells in total, zero
failures**, floor exactly 1 in every cell (i.e. the mod-`p` statement is tight), with two
recorded exceptions that reproduce `LBW`: **D at p = 5 has floor 2**, and **η at p = 5 is
the ramified prime, floor 3** (`χ₅(5) = 0`, the pole never forms).

### 4.2 Tameness verdicts

Every decomposition in hand is **non-tame** except the four already proved:

| decomposition | arguments | tame? | Theorem LB applies? |
|---|---|---|---|
| γ | `n, k` | **yes** | **[PROVED] p ≥ 5** (unchanged) |
| A | `k, n−k` | **yes** | **[PROVED] p ≥ 5** (unchanged) |
| D | `n, k, n−k` | **yes** | **[PROVED] p ≥ 7** (unchanged; p = 5 is the (H4) coefficient clause, denominators 1/5) |
| s₁₀ | `k, n−k` | **yes** | **[PROVED] p ≥ 7** (unchanged) |
| α (17 terms here / 14 in LBW) | `k, n−k, 2k, 2n−2k` | no (`2k → 2n`) | needs Lemma-D substitute; §2.5 localises it |
| ε (10 terms) | `k, n−k, 2k, 2k−n` | no (`2k → 2n`) | ditto |
| s₇ (8 terms) | `n, k, n−k, 2k` | no (`2k → 2n`) | ditto; also excludes p = 7 (denominators 14) |
| E (5 terms) | `k, 2k, 2n−2k` | no | ditto — **and E remains the only χ ≠ 1 instance, still unproved** |

### 4.3 The Γ-derivation probe — γ is alone `[EXCLUDED for 14 of 15]`

`work/sporadic/gamma_probe.py`. `APERY_DEFECT` §7.1's mechanism (deform by
`∏_j Π_j(x)^{c_{j,x}}`, arrange `e_1(c) = … = e_{w−1}(c) = 0` so that `L_1 = … = L_{w−1} = 0`
termwise) yields `[ε^w] = L_w = ((−1)^{w−1}/w) Σ_x e_w(c_x) H^{(w)}_x` — a **degree-1**
weight-`w` bare weight. So the Γ-derivable class is exactly the degree-1 fit, a system with
6–16 columns. Result, `N = 60`, guard 20:

| consistent | inconsistent (cols / excess) |
|---|---|
| **γ only** (6 cols, rank 6, 54 excess) | A 7/55, B 7/53 (+χ₋₃ 14/46), C 8/52 (+χ₋₃ 16/44), D 6/54, E 8/55 (+χ₋₄ 16/50), F 8/54 (+χ₋₃ 16/48), α 7/55, δ 7/53, ε 7/53, ζ 8/52 (+χ₋₃ 16/44), η 8/52 (+χ₅ 16/44), s₇ 7/53, s₁₀ 6/56, s₁₈ 8/52 (+χ₋₃ 16/44) |

So the Γ-deformation route recovers Apéry's `2H^{(3)}_n − H^{(3)}_k` and **nothing else in
the sporadic class**: for the other fourteen the weight is genuinely of degree ≥ 2, i.e. a
*product* of harmonic letters, which no primitive third-difference Γ-deformation can
produce. This closes the "try the derivation instead of the fit" line as a route to the
eleven, while confirming it is the right explanation of γ.

---

## 5. Fifteen-row status table

`limit`, `w`, `χ` from `LBW_GENERAL` T1. "found?" = bare-alphabet decomposition known
(this work or LBW). "tame?" = all letter arguments in `[0,n]`, i.e. (H4).

| # | family | Apéry limit | w | χ | decomposition found? | terms | tame? | congruence verified? | proof status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **A** (Franel) | ζ(2)/4 | 2 | 1 | yes | 3 | **yes** | ✔ p ≤ 19 | **[PROVED] p ≥ 5** |
| 2 | **B** | none | 2 | χ₋₃ | **no** (119 cols, 60 exc) | — | n/a | ✔ p ≤ 19 | conjectural |
| 3 | **C** | L₋₃(2)/2 | 2 | χ₋₃ | **no** (132 cols, 63 exc) | — | n/a | ✔ p ≤ 19 | conjectural |
| 4 | **D** (Apéry ζ(2)) | ζ(2)/5 | 2 | 1 | yes | 4 | **yes** | ✔ p ≤ 19 (p=5 floor 2) | **[PROVED] p ≥ 7** |
| 5 | **E** (Catalan) | L₋₄(2)/2 = G/2 | 2 | **χ₋₄** | yes (non-tame) | 5 | **NO** `[EXCLUDED]` | ✔ p ≤ 19 | needs Lemma-D |
| 6 | **F** | (5/8)L₋₃(2) | 2 | χ₋₃ | **no** (152 cols, 112 exc) | — | n/a | ✔ p ≤ 19 | conjectural |
| 7 | **α** (Domb) | 7ζ(3)/24 | 3 | 1 | yes (non-tame) | 14 (LBW) / 17 | **NO** `[EXCLUDED]` | ✔ p ≤ 19 | needs Lemma-D |
| 8 | **γ** (Apéry ζ(3)) | ζ(3)/6 | 3 | 1 | yes, **degree 1** | 2 | **yes** | ✔ p ≤ 19 | **[PROVED] p ≥ 5** |
| 9 | **δ** | none | 3 | 1 | **no** (330 cols, 70 exc) | — | n/a | ✔ p ≤ 19 | conjectural |
| 10 | **ε** | 7ζ(3)/32 | 3 | 1 | yes (non-tame) | 10 | **NO** `[EXCLUDED]` | ✔ p ≤ 19 | needs Lemma-D |
| 11 | **ζ** | L₋₃(3)/3 | 3 | χ₋₃ | **no** (204 cols, 56 exc) | — | n/a | ✔ p ≤ 19 | conjectural |
| 12 | **η** | none | 3 | χ₅ | **no** (520 cols, 87 exc) | — | n/a | ✔ p ≤ 19 (p=5 ramified, floor 3) | conjectural |
| 13 | **s₇** | ζ(2)/7 | 2 | 1 | yes (non-tame) | 8 | **NO** `[EXCLUDED]` | ✔ p ≤ 19 | needs Lemma-D (p ≠ 7) |
| 14 | **s₁₀** | ζ(2)/5 | 2 | 1 | yes | 3 | **yes** | ✔ p ≤ 19 | **[PROVED] p ≥ 7** |
| 15 | **s₁₈** | L₋₃(2)/2 | 2 | χ₋₃ | **no** (152 cols, 62 exc) | — | n/a | ✔ p ≤ 19 | conjectural |

> **NEW PROVED COUNT: 4** (γ, A, D, s₁₀) — unchanged by the bare alphabet.
>
> **E's verdict, called out separately.** E is the only family with a nontrivial character
> (χ₋₄) and the only known instance of the twisted case `e = 1` of Theorem LB. A tame
> decomposition for it is **`[EXCLUDED]`**, and exhaustively so: (i) E's own representation
> has the complete tame form set `{n,k,n−k}` (Lemma T), and the *entire* tame weight-2 space
> over it — with χ₋₄, with three characters, with and without (H5) — is inconsistent at
> 106–154 excess equations; (ii) the only other tame representation of `A_E` that exists,
> `Σ_k 4^{n−2k}C(n,2k)C(2k,k)²` (new, `[VERIFIED n ≤ 30]`), supports no decomposition at
> all, tame or not (230 cols, rank 230, 90 excess); (iii) a 4.4 M-template sweep finds no
> third tame representation. **The programme does not get its first proved χ ≠ 1 instance
> from the bare alphabet.** What it gets instead is §2.5: for E the only missing ingredient
> is the vanishing-layer valuation inequality, with (H1)–(H3) and (H5) verified.

---

## 6. Files (`work/sporadic/`)

| file | what |
|---|---|
| `core.py` | letters `H^{(r)}`/`K_χ^{(r)}`, monomial enumeration (with (H5) filter), modular + exact partial-sum tables, RREF/consistency, CRT + rational reconstruction, exact checker |
| `fams.py` | all 15 families **plus `E2`** as cell generators (`idx`, `Smod`, `Sexact`, `args`, `tame`); bracketed families split into two cells per `k` |
| `check1.py` | sanity layer 0: `Σ_cells S = A(n)`; `Smod ≡ Sexact (mod q)` cell by cell; measured-vs-declared tame sets |
| `fit.py` | design matrices, `probe` (with the excess guard), exact extraction, greedy support minimisation |
| `validate.py` | T1: recovery of γ, A, s₁₀, D and E's known χ₋₄ form |
| `t2.py`, `t2_layers.py` | T2 tame searches; the surviving/vanishing-layer (H3)/(H4) audit |
| `hunt.py`, `huntchk.py` | the tame-representation sweep (Lemma T template space) and the support filter that removes its false positives |
| `t3.py`, `t3b.py`, `t3c.py`, `t3d.py` | T3, the conjectural seven, in increasing alphabet size |
| `t4.py` | the congruence `p^w B(ap+r) ≡ χ(p)B(a)A(r)`, exact, `p ≤ 19` |
| `gamma_probe.py` | the degree-1 (Γ-derivable) probe over all fifteen |
| `*.log` | every run's output, including the refused-for-insufficient-excess ones and their reruns |

---

## 7. What a successor should do next

1. **[CORRECTED 2026-07-26, `work/LEMMAD_CHECK.md`.]** ~~Prove the vanishing-layer
   inequality of §2.5 for one of α, ε, s₇, E … takes the proved count from 4 to 8.~~
   The inequality is **false** for α, ε, E. **Prove it for s₇** (`p ≥ 5`, `p ≠ 7`), where it
   is `[VERIFIED, 0 violations, p ≤ 41]` together with its base-level companion
   `v_p(S(a,b)) + v_p(w(a,b)) ≥ 1`; that is a bounded, purely local Kummer-vs-order-1-pole
   problem and it takes the proved count from **4 to 5** (χ = 1, so no χ ≠ 1 instance).
   For α, ε, E the target is instead the descent congruence (LD) of `LEMMAD_CHECK` §4.2.
2. **Do not re-run**: any tame search for α, ε, s₇, E (excluded, and complete by Lemma T);
   the E2 representation (dead, 230 cols); the degree-1/Γ-derivation class (γ only);
   B, C, δ, s₁₈ at full degree in their complete tame spaces (excluded).
3. **The open gaps in §3, stated precisely**: full-degree (degree-3 in weight-1 letters)
   coverage for **ζ** and **η** in their complete tame spaces, and for **F** at 7 tame
   arguments — 424–1088 columns, needing `N ≈ 500–1150` rows. Only these three, and only at
   degree 3.
4. **For the conjectural seven, change the ansatz, not the alphabet.** The rank diagnostic
   (§3) says B, δ, ζ have *no* ℚ-relation between summand and harmonic letters, so no
   enlargement of a `Σ_k S·w` fit will succeed. The two candidates worth trying are
   (a) Gorodetsky-style constant-term representations (already `LBW`'s recommendation for
   C, and now known to be necessary rather than optional — supplying the conductor-3
   arguments by hand does not repair C), and (b) rational-function coefficients `c_j(n,k)`,
   which would require replacing (H4)'s coefficient clause by
   `c_j(n,k) ≡ c_j(a,b) (mod p)` on the surviving set — note that the obvious candidates
   `1/(2k+1)`, `1/(n+1)` **fail** that test, so this needs a genuinely new idea.
