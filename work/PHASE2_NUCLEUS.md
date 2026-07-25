# P1h — the nucleus: `(REC-★)`, and a proof of `(BASE)`

**Author:** mathematician-agent (River's odd-zeta program), task **P1h**
**Date:** 2026-07-25
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, artefacts in `work/p1h/`
**Predecessors:** `work/PHASE2_RLETTER.md` (P1g — `(REC-★)`, the `w₅^I` region reduction),
`work/PHASE2_CANCEL.md` (P1f — the θ wall), `work/PHASE2_THEOREM.md` v2,
July read-only: `../zeta-math/worthiness/PHASE2_A1_MIDPOINT_THEOREM.md`, `PHASE2_MIDPOINT_GATE.md`.

**Labels.** `[PROVED]` complete proof written here · `[VERIFIED r]` exact finite check on range
`r`, 0 failures · `[CERT]` machine certificate · `[OPEN]`.

---

## 0. HEADLINE

1. **`(REC-★)` has a universal normal form.** `n₀ = (p−5)/2` means `n₀ ≡ −5/2 (mod p)`, so the
   three recurrence coefficients reduce to **`p`-independent rational numbers**:
   ```
      (REC-★)   11907·P_{n₀} − 334374·P_{n₀+1} − 19292·P_{n₀+2} ≡ 0  (mod p),   n₀=(p−5)/2 .
   ```
   `(R₀,R₁,R₂) = (11907,−334374,−19292) = 2⁷·c_i(−5/2)/7` is **exactly the July A1-MID row** —
   the base level and its `a=1` lift are governed by the *same* universal row. (§1)
2. **The `p = 13` anomaly is an artefact of the un-normalised row, not arithmetic.** Normalised,
   `(REC-★)` is **tight at every prime**, `v_p = 1` exactly,
   `[VERIFIED 5 ≤ p ≤ 199, 44 primes, 0 failures]`. The one genuine degeneracy is `p = 7`, where
   the content `28 = 2²·7` kills the raw row. (§1.3)
3. **`(BASE)` IS PROVED**, modulo only the two decomposition/depth certificates already on the
   tree. The proof splits the range at the midpoint:
   * `n ≤ (p−1)/2`: **region III is empty** ⟹ `w₅^I` is cell-wise `p`-integral at *every* cell;
   * `n = (p+1)/2`: **region III collapses to three corner cells** `(n−1,n),(n,n−1),(n,n)`, with
     `T/p² ≡ (2,2,24)` and `K₃ ≡ (3 − s₂/2, 3 − s₂/2, −1/2 − s₂/2)`, and the corner sum is
     ```
              2·(3−s₂/2) + 2·(3−s₂/2) + 24·(−1/2−s₂/2)  =  −14·s₂ ,   s₂ := Σ_{j=1}^{p−1} j^{−2} ,
     ```
     which is `≡ 0 (mod p)` for **every `p ≥ 5`** by the classical `Σ_{j<p} j^{−2} ≡ 0`;
   * `n > (p+1)/2`: forward induction, with every `a₀`-root step **proved apparent**.
4. **`(REC-★)` becomes a COROLLARY.** With `v_p(P_{(p+1)/2}) ≥ 0` proved directly, the recurrence
   row at `n₀` yields `(REC-★)`. **The nucleus is dissolved, not cracked.** (§4)
5. **Explicit desingularisation of `L_BZ`.** An order-4 left multiple `L̃` with leading
   coefficient exactly `2·D·(n+3)⁵(2n+5)` — `a₀` **removed**
   (`[VERIFIED]` annihilates `Q`, `P`, `P̂` exactly, `ν = 1..40`, 0 residuals). On the
   desingularised ladder the **only** singular step in `0 ≤ n ≤ p−4` is the midpoint `n₀`, i.e.
   exactly the level the region-III computation supplies. (§3.3)
6. **The single arithmetic input at the nucleus is `Σ_{j<p} j^{−2} ≡ 0 (mod p)`** — the same
   `p ≥ 5` hypothesis that Wolstenholme imposes everywhere else in the program. Neither Fermat
   quotients (`s₁`) nor `s₃` appear: `K₃` is free of `h₁,…,h₅`, `s₁`, `s₃`, `s₄`, `s₅`.

---

## 1. `(REC-★)`, exactly `[PROVED]`

### 1.1 The universal row

`L_BZ`: `c₀(n)Y_n + c₁(n)Y_{n+1} + c₂(n)Y_{n+2} + c₃(n)Y_{n+3} = 0`,
```
  a₀(n) = 41218n³+198849n²+320790n+173057
  c₀(n) = (n+1)⁵(n+2)a₀(n+1),  c₁(n) = −2(n+2)B₈(n),  c₂(n) = −2B₉(n),
  c₃(n) = 2(n+3)⁵(2n+5)a₀(n)
```
(`work/lb5/core.py`). All four `c_i` have degree 9.

> **Proposition 1.1 `[PROVED]`.** `n₀ := (p−5)/2` is the unique `n` with `2n+5 = p`, so
> `n₀ ≡ −5/2 (mod p)`, and since `deg c_i = 9`,
> ```
>     2⁹ c_i(n₀)  ≡  2⁹ c_i(−5/2)  =  28·R_i   (mod p),   (R₀,R₁,R₂,R₃) = (11907,−334374,−19292,0).
> ```
> Equivalently, as an identity in `ℤ[m]` (July `sol_local_regular.py`, re-derived here):
> `128 c_i(m) = 7R_i + (2m+5)H_i(m)`.
> The content `28 = 2²·7` is a `p`-unit for every `p ≥ 5` **except `p = 7`**; at `p = 7` the whole
> row vanishes mod `p` and the recurrence obligation at `n₀` is *vacuous*.

`(R₀,R₁,R₂)` is primitive (`11907 = 3⁵·7²`, `334374 = 2·3·23·2423`, `19292 = 2²·7·13·53`) and is
**identical** to the July A1-MID row for the `a=1` lift `N = p+n₀ = (3p−5)/2`.

### 1.2 Statement

> **`(REC-★)`.** For every prime `p ≥ 5`, with `n₀ = (p−5)/2`,
> ```
>       11907·P_{n₀}  −  334374·P_{n₀+1}  −  19292·P_{n₀+2}   ≡   0   (mod p) .
> ```
> Its role: it is exactly what is needed to make the forward `L_BZ` induction cross the midpoint,
> producing `P_{n₀+3} = P_{(p+1)/2}` — the level of the attained deficit cell
> `((p+1)/2, 0, (p−1)/2)`, and the first level at which region III is non-empty.

### 1.3 Fresh sweep, and the `p = 13` anomaly explained `[VERIFIED 0 failures]`

`work/p1h/r1_sweep.py`, `r1_anom.py`, exact `Fraction` ladders, primes `5 ≤ p ≤ 199`.

| quantity | result |
|---|---|
| `v_p(11907P_{n₀}−334374P_{n₀+1}−19292P_{n₀+2})` | **`= 1` exactly at all 44 primes** |
| same for `Q` | `1` (except `p = 29,131`: `2`) — automatic, `Q ∈ ℤ` solves `L_BZ` |
| same for `P̂` | **`0`** at 42/44 primes — the control: the congruence is real content |
| `v_p(c₃(n₀))` | `1`, except `p = 43` where it is `2` |

> **The `p = 13` anomaly is not arithmetic.** P1g measured the *un-normalised*
> `Σ c_i(n₀)P_{n₀+i}` and found `v_13 = 2` against `v_13(c₃) = 1`, i.e. "slack 1". Writing
> `c_i(n₀) = u·R_i + p·e_i` (`u = 28·2^{−9}`), the raw combination is
> `u·φ_R(P) + p·Σ e_i P_{n₀+i}`; since `v_p(φ_R(P)) = 1` **always**, the raw valuation is `≥ 1`
> always, and jumps to `2` exactly when the *second-order* term `u·(φ_R(P)/p) + Σ e_i P` happens
> to vanish mod `p`. At `p = 13` it does. **In the normalised row `p = 13` is tight like every
> other prime — there is no anomaly.**

### 1.4 The two "double midpoint" primes `[PROVED]`

`v_p(c₃(n₀)) = 1 + v_p(a₀(n₀))` (as `n₀+3 = (p+1)/2 ∈ [1,p−1]` and `2` are units), and
`8·a₀(−5/2) = −241144 = −2³·43·701`, so
```
       p | a₀(n₀)   ⟺   p ∈ {43, 701} ,
```
both with multiplicity 1. There the recurrence route would need `v_p ≥ 2`. **The proof below never
uses the midpoint recurrence step, so `{43,701}` cost nothing.**

---

## 2. The midpoint region collapse — and `(BASE)` for `n ≤ (p+1)/2` `[PROVED]`

`w₅^I` is `PHASE2_RLETTER` §10's representative in the all-primes form
`work/p1g/w5_exIII_allp.json` (207 terms, denominators on `{2,3}`); `v₅ := w₅^I − H^{(5)}_n`; and
```
   Theorem 10.1 (PHASE2_RLETTER):  for every p ≥ 5 and n < p, every cell OUTSIDE
        III = { (k,l) : k,l ≥ q := p−n ,  p ≤ k+l < p+q }
   contributes a p-integral summand to  P_n = Σ_{k,l} T(n,k,l)·w₅^I(n,k,l).
```

### 2.1 Region III is empty below the midpoint `[PROVED]`

> **Lemma 2.1.** If `n ≤ (p−1)/2` then `III = ∅`, hence `v_p(P_n) ≥ 0`.

*Proof.* `III` requires `k+l ≥ p` with `k,l ≤ n`, so `2n ≥ p`; but `2n ≤ p−1`. ∎

So **half of `(BASE)` is free**, and the deficit can first appear only at `n = (p+1)/2` — exactly
where `PHASE2_INDUCTION` §6.1 located the attained deficit cell. The two localisations agree for
a structural reason.

### 2.2 At `n = (p+1)/2`, region III is exactly three corner cells `[PROVED]`

Let `n = (p+1)/2`, `q = p−n = (p−1)/2`, `ñ = 2n−p = 1`.

> **Lemma 2.2.** `III = { (q,q+1), (q+1,q), (q+1,q+1) } = { (n−1,n), (n,n−1), (n,n) }`.

*Proof.* `k,l ≥ q` and `k,l ≤ n = q+1` force `k,l ∈ {q,q+1}`. Then `k+l ∈ {p−1, p, p+1}`;
`k+l ≥ p` excludes `(q,q)`, and `k+l < p+q` holds for the other three (`p+1 < p+(p−1)/2`,
`p ≥ 5`). ∎

`(BASE)` at the critical level is therefore a **three-term** congruence — the smallest object the
program has produced.

### 2.3 The three `T/p²` values `[PROVED]`

Write `ε := (−1)^{(p+1)/2}`, `q = (p−1)/2`; Wilson gives `(q!)² ≡ ε (mod p)`.

> **Lemma 2.3.** At `n = (p+1)/2`, `p ≥ 5`: `v_p(T) = 2` at all three cells and
> ```
>     T(n,n−1,n)/p² ≡ T(n,n,n−1)/p² ≡ 2 ,        T(n,n,n)/p² ≡ 24     (mod p).
> ```

*Proof.* `T(n,k,l) = C(n+k,n)C(n,k)²C(n+l,n)C(n,l)²C(n+k+l,n)`.

*Cell `B = (n,n)`.* `T = C(p+1,n)²·C(3n,n)`. Kummer: `n+n = p+1` in base `p` has exactly one
carry, so `v_pC(p+1,n) = 1`; `n + (p+1)` has none, so `v_pC(3n,n) = 0`; `v_p(T) = 2`. As
`p+1−n = n`, `C(p+1,n)/p = (p+1)(p−1)!/(n!)² ≡ −1/(n!)²`; with `n! = (q+1)q!` and `q+1 ≡ 1/2`,
`(n!)² ≡ ε/4`, so `C(p+1,n)/p ≡ −4ε` and `(C(p+1,n)/p)² ≡ 16`. Lucas on `3n = p + (p+3)/2`,
`n = (p+1)/2` gives `C(3n,n) ≡ C((p+3)/2,(p+1)/2) = (p+3)/2 ≡ 3/2`. Hence `T/p² ≡ 16·(3/2) = 24`.

*Cell `A = (n−1,n) = (q,q+1)`.* `C(n+k,n) = C(p,n)`, `v_p = 1`,
`C(p,n)/p = (p−1)!/(n!q!) ≡ −1/((q+1)(q!)²) ≡ −2ε`; `C(n,k) = C(q+1,q) = q+1 ≡ 1/2`;
`C(n+l,n) = C(p+1,n)`, `/p ≡ −4ε`; `C(n,l) = 1`;
`C(n+k+l,n) = C((3p+1)/2,(p+1)/2) ≡ C(1,0)C((p+1)/2,(p+1)/2) = 1` by Lucas. So `v_p(T) = 2` and
`T/p² ≡ (−2ε)(1/2)²(−4ε) = 2ε² = 2`. ∎

`[VERIFIED]` `work/p1h/r2_corner.py`: `p ∈ {5,…,31}`, `v_p(T) = 2` and `T/p² mod p = 2,2,24` at
every prime, 0 mismatches.

### 2.4 The two `K₃` values — and the cancellation `[PROVED]`

At `n = (p+1)/2` every letter argument is `< 2p`, so each letter contains at most one multiple of
`p` and its `u`-expansion (`u = p^{−1}`) is exact and elementary. With `h_r := H^{(r)}_q (mod p)`,
`s_r := Σ_{j=1}^{p−1} j^{−r} (mod p)`, `(q+1)^{−1} ≡ 2`, `(q+2)^{−1} ≡ 2/3`:

| letter | cell `A = (q,q+1)` | cell `B = (q+1,q+1)` |
|---|---|---|
| `A_r(k)` | `u^r + s_r − h_r` | `u^r + s_r + 1 − h_r − 2^r` |
| `B_r(k)` | `1 − h_r` | `−h_r − 2^r` |
| `A_r(l)` | `u^r + s_r + 1 − h_r − 2^r` | `u^r + s_r + 1 − h_r − 2^r` |
| `B_r(l)` | `−h_r − 2^r` | `−h_r − 2^r` |
| `C_r` (no pole) | `h_r + 2^r` | `h_r + 2^r + (2/3)^r − 1` |
| `N_r` | `h_r + 2^r` | `h_r + 2^r` |

Substituting into the 207 monomials of `w₅^I` and extracting the `u³` coefficient
(`work/p1h/r2_K3.py`, `r3_K3gen.py`; exact `sympy` over `ℚ[h₁..h₅, s₁..s₅]`):

> **Lemma 2.4 `[PROVED — finite exact computation]`.** For every prime `p ≥ 5`,
> ```
>    K₄ = K₅ = 0  at both cells                (the Lemma-F cap  d₅ ≤ 3  is met),
>    K₃(A) = 3 − s₂/2 ,        K₃(B) = −1/2 − s₂/2 .
> ```
> Both are **free of `h₁,…,h₅` and of `s₁,s₃,s₄,s₅`**: the entire harmonic content of the `u³`
> coefficient cancels. (Only letters of weight `≤ 3` can reach `K₃` — the pole part must have
> total weight `3` and the remainder weight `2` — which is why `s₄,s₅` cannot appear and the
> lemma is valid down to `p = 5`.)

> ### **Theorem 2.5 (the nucleus, dissolved) `[PROVED]`**
> For every prime `p ≥ 5`,
> ```
>   Σ_{(k,l)∈III} (T/p²)·K₃  ≡  2(3−s₂/2) + 2(3−s₂/2) + 24(−1/2−s₂/2)  =  −14·s₂  ≡  0  (mod p),
> ```
> because `s₂ = Σ_{j=1}^{p−1} j^{−2} ≡ Σ_{j=1}^{p−1} j² = (p−1)p(2p−1)/6 ≡ 0 (mod p)` for `p ≥ 5`.
> Since `K₀,K₁,K₂ ∈ ℤ_p` and `T/p² ∈ ℤ`, `v_p(Σ_{III} T·v₅) ≥ 0`, hence by Theorem 10.1
> **`v_p(P_{(p+1)/2}) ≥ 0`.**

*The whole nucleus consumes exactly one classical fact,* `Σ_{j<p} j^{−2} ≡ 0`, i.e. the same
`p ≥ 5` hypothesis Wolstenholme imposes elsewhere. No Fermat quotient, no Bernoulli number.

`[VERIFIED, 0 failures]` `work/p1h/r2_check.py`, `r3_e2e.py`: exact `Fraction` arithmetic through
the independent `rw5eval` evaluator; at every prime `5 ≤ p ≤ 139` the three corner residues
`p·T·v₅ mod p` are exactly `(6, 6, −12) mod p` and sum to `0` — **32/32 primes clean**.

**The statement is not vacuous.** The same extraction on `w5_allp` (the non-`exIII`
representative) gives `h₁`-dependent `K₃` and `4K₃(A)+24K₃(B) ≠ 0`. The content of Theorem 2.5
lives precisely in the `exIII` depth conditions — exactly as `PHASE2_CANCEL` Thm 5.1 (the θ wall)
predicts: the value cannot be moved by summand-side identities, only by pinning the
representative. **The wall is respected, and the door it points at is the representative.**

---

## 3. Above the midpoint: the `a₀`-root steps are apparent `[PROVED]`

For `n > (p+1)/2` we use forward induction. To produce level `m ≤ p−1` we use the step
`ν = m−3 ≥ (p−3)/2 > n₀`; on that range `2ν+5 ∈ [p+2, 2p−3]` is odd and `≠ p`, and `ν+3 ≤ p−1`.
**Hence the only possible exceptional steps above the midpoint are roots of `a₀` mod `p`.**
`[VERIFIED]` `work/p1h` sweep over all 428 primes `5 ≤ p < 3000`: **296 267 steps above the
midpoint, 223 exceptional, every one an `a₀`-root, 0 exceptions.**

### 3.1 The proportionality lemma `[PROVED]`

Because `c₀(ν−1) = ν⁵(ν+1)a₀(ν)`, the row at `ν−1` degenerates in the same place as the row at
`ν`. Put `U(ν) := (c₀,c₁,c₂)(ν)` and `V(ν) := (c₁,c₂,c₃)(ν−1)`, both acting on
`(Y_ν,Y_{ν+1},Y_{ν+2})`.

> **Lemma 3.1 (APP) `[PROVED — exact polynomial division]`.** All three `2×2` minors of
> `[U(ν); V(ν)]` are divisible by `a₀(ν)` **in `ℚ[ν]`** (each minor has degree 18; the
> remainders on division by `a₀` are exactly `0`; `work/p1h/r2_apparent.py`).
> Hence, if `p | a₀(ν)`, `ν ≥ 1`, `V(ν) ≢ 0 (mod p)`, and `Y` solves `L_BZ` with
> `Y_{ν−1},…,Y_{ν+2} ∈ ℤ_p`, then `U(ν)·(Y_ν,Y_{ν+1},Y_{ν+2}) ≡ 0 (mod p^{v_p(a₀(ν))})`, so
> `Y_{ν+3} ∈ ℤ_p`.

*Proof.* The row at `ν−1` gives `V(ν)·(Y_ν,Y_{ν+1},Y_{ν+2}) = −ν⁵(ν+1)a₀(ν)Y_{ν−1} ≡ 0
(mod p^v)`, `v := v_p(a₀(ν))`. Each minor is `a₀(ν)·(integer)`, so `≡ 0 (mod p^v)`. Pick `i` with
`V_i` a `p`-unit, set `λ := U_i/V_i ∈ ℤ_p`; then `U_j − λV_j = (U_jV_i − U_iV_j)/V_i ≡ 0
(mod p^v)`, so `U·Y ≡ λ(V·Y) ≡ 0 (mod p^v)`. On this range `v_p(c₃(ν)) = v`. ∎

**This replaces `PHASE2_RLETTER` §7.2's numerical apparency evidence (107 tests) by a proof.**

### 3.2 The fully degenerate steps `[PROVED — explicit finite set]`

`V(ν) ≡ 0` at a root of `a₀` forces `p` to divide all three resultants `Res_ν(a₀, c_i(ν−1))`,
whose gcd is `2⁶·3³·7³·11·29³·37²·557³·543606522303979` (`r2_res.py`). A root-by-root check
(`r2_res2.py`) and the independent `p < 3000` sweep both give **exactly three** occurrences:
```
      (p,ν) = (7,2) ,   (11,6) ,   (p₀, 416574044722681) ,  p₀ := 543606522303979 .
```
`p₀` is the unique prime at which `a₀` has **two consecutive roots** mod `p`, so the whole row at
`ν−1` vanishes mod `p₀`. In all three cases `v_p` of every entry of `row(ν−1)` is `1` (except one
entry at `p = 7`), so `row(ν−1)/p` is a valid `ℤ`-functional with a **unit** `Y_{ν+2}`
coefficient; combined with the regular row at `ν−2` it gives two independent functionals on
`(Y_{ν−2},…,Y_{ν+2})`. `work/p1h/r3_degen.py` computes the ranks over `𝔽_p`:

| `(p,ν)` | `rank[row(ν−2); row(ν−1)/p]` | `+ U(ν)` | verdict |
|---|---|---|---|
| `(11, 6)` | 2 | 2 | **apparent** |
| `(p₀, 416574044722681)` | 2 | 2 | **apparent — `p₀` needs no special treatment** |
| `(7, 2)` | 2 | 3 | not in span → `p = 7` is a **finite check** (levels 5,6; `[VERIFIED]`) |

### 3.3 The desingularised operator `L̃` `[PROVED] [VERIFIED]`

Lemma 3.1 is the shadow of an explicit desingularisation. `a₀` is irreducible over `ℚ`, so
`K := ℚ[ν]/(a₀)` is a field and `U = λV` in `K` with `λ = c₀(ν)/c₁(ν−1)` of degree `≤ 2`:
```
  λ(ν) = ( 392627556035671426586 ν² + 1282015597875460006266 ν + 1052781309790247665282 ) / D ,
  D = 3641620092914355321 = 3·7·11·29·p₀ .
```
Then **every** coefficient of `row(ν) − λ·row(ν−1)` (an order-4 relation on `Y_{ν−1},…,Y_{ν+3}`)
is divisible by `a₀(ν)` in `ℚ[ν]`; dividing through and clearing `D` leaves

> **`L̃`: `d₀Y_{ν−1}+d₁Y_ν+d₂Y_{ν+1}+d₃Y_{ν+2}+d₄Y_{ν+3} = 0`, `d_i ∈ ℤ[ν]`,
> `deg d₀..d₃ = 8`, and `d₄ = 2D·(ν+3)⁵(2ν+5) = 7283240185828710642·(ν+3)⁵(2ν+5)` —
> `a₀` is gone from the leading coefficient.**

`[VERIFIED, 0 residuals]` `L̃` annihilates `Q`, `P` and `P̂` **exactly** over `ℚ` for `ν = 1..40`
(`work/p1h/desing_coeffs.json`). *(Note: `d₁` is not identically zero — the `Y_ν` coefficient
vanishes only modulo `a₀`, and `d₁ = (c₀(ν)−λc₁(ν−1))/a₀(ν)` is a genuine degree-8 polynomial.)*

Consequently: **on the desingularised ladder the only singular step in `0 ≤ n ≤ p−4` is the
midpoint `n₀`** (`2ν+5 ≡ 0`; `ν+3 ≡ 0` gives `ν = p−3`, out of range), for every
`p ∉ {2,3,7,11,29,p₀}` — and those five primes are covered by §3.2. The recurrence half and the
region half of the proof dovetail with no residue: `L̃`'s single singular step is precisely the
single level that Theorem 2.5 supplies.

---

## 4. Assembly, and `(REC-★)` as a corollary

> ### **Theorem 4.1 `(BASE)` `[PROVED, modulo the certificates of §5]`**
> For every prime `p ≥ 5` and every `n < p`, `ord_p(P_n) ≥ 0`.

*Proof.* `n ≤ (p−1)/2`: Lemma 2.1. `n = (p+1)/2`: Theorem 2.5. `n > (p+1)/2`: forward induction
from the four consecutive integral levels below; each step `ν ≥ (p−3)/2` has `p ∤ (ν+3)(2ν+5)`,
so is exceptional only if `p | a₀(ν)`, and then it is apparent by Lemma 3.1 (§3.2 for the three
fully degenerate cases; `p = 7` by the `[VERIFIED]` finite check). ∎

> **Corollary 4.2 `(REC-★)` `[PROVED]`.** With `n₀ = (p−5)/2`,
> `c₀(n₀)P_{n₀}+c₁(n₀)P_{n₀+1}+c₂(n₀)P_{n₀+2} = −c₃(n₀)P_{(p+1)/2}` has `v_p ≥ v_p(c₃(n₀)) ≥ 1`;
> multiplying by `2⁹/28` and using Prop. 1.1 gives
> `11907P_{n₀}−334374P_{n₀+1}−19292P_{n₀+2} ≡ 0 (mod p)` for `p ≠ 7`, and at `p = 7` by the
> `[VERIFIED]` direct check.

**The order of implication is inverted relative to the brief.** `(REC-★)` was expected to be the
*input* to `(BASE)`; it is its *output*. The midpoint singularity of `L_BZ` (`2n+5 ≡ 0`) and the
midpoint appearance of region III (`2n ≥ p`) are the same phenomenon seen from the recurrence
side and the summand side — and it is the summand side that is computable, because there the
object is three cells wide.

---

## 5. What the proof still rests on

| node | status |
|---|---|
| `P_n = Σ_{k,l}T(n,k,l)w₅^I(n,k,l)` (decomposition identity for `w₅^I`) | `[VERIFIED n ≤ 20]`, certificate pending — `PHASE2_RLETTER` §12.2 |
| Theorem 10.1 (`exIII` cell-wise integrality) — the `p`-independent depth certificate | `[CERT, 3 primes, identical pivot sets]` |
| Lemmas 2.1–2.4, Theorem 2.5, Lemma 3.1, `L̃` | `[PROVED here]` |
| `p = 7` at the step `ν = 2` | `[VERIFIED]` (levels 5,6; inside `5 ≤ p ≤ 367`) |

**Certificate-target delta (`PHASE2_RLETTER` §12.2).** The proof consumes `w₅^I`, not `w5_allp`,
so the successor certificate is `w5_allp` **plus** the homogeneous weight-5 summation identity
`Σ_{k,l}T·(w₅^I − w5_allp) = 0`.

---

## 6. Sweep summary (all exact, 0 failures)

* `(REC-★)` normalised: 44 primes `5 ≤ p ≤ 199`, `v_p = 1` exactly at every one.
* corner identity at `n = (p+1)/2`: 32 primes `5 ≤ p ≤ 139`, residues `(6,6,−12) mod p`, sum `0`.
* cell-wise integrality below the midpoint: 1 588 cells over all levels `n < (p+1)/2`, `p ≤ 23`,
  0 violations; plus the top below-midpoint level `n = (p−1)/2` at `p = 29,31,37` (842 cells,
  `|III| = 0` as Lemma 2.1 predicts), 0 violations.
* above-midpoint steps: 296 267 steps over 428 primes `p < 3000`; 223 exceptional, **all**
  `a₀`-roots; 2 fully degenerate, both predicted by the resultant computation.
* `L̃` annihilates `Q, P, P̂` exactly, `ν = 1..40`, 0 residuals.
* `a₀`-minor divisibility, `L̃` construction, `K₃` extraction: exact symbolic, no sampling.

## 7. Reproduction — `work/p1h/`

| script | what it does |
|---|---|
| `r1_normalize.py` | `c_i(−5/2)` → the universal row `(11907,−334374,−19292)` |
| `r1_sweep.py` | `(REC-★)` normalised sweep, `p ≤ 199` |
| `r1_anom.py` | the `p = 13` anomaly: raw vs normalised row |
| `r2_corner.py` | region III at `n = (p+1)/2` = three corner cells; `T/p²`; `Σ_III` |
| `r2_K3.py` | symbolic `u`-expansion at the corner cells → `K₃` |
| `r3_K3gen.py` | same with the Fermat sums `s_r` free → `K₃ = 3−s₂/2, −1/2−s₂/2` |
| `r2_check.py` | exact cross-check + representative dependence (`w5_allp` control) |
| `r2_apparent.py` | Lemma 3.1: the three minors are divisible by `a₀` |
| `r2_res.py`, `r2_res2.py`, `r3_degen.py` | the finite degenerate set and its resolution |
| `r2_desing.py`, `desing_coeffs.json` | the desingularised order-4 operator `L̃` |
| `r3_e2e.py` | end-to-end verification of the assembled proof, prime by prime |
