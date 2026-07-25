# P1i — `(GAP-DESC)`: the descent term (I) off-regime, at every digit level `[PROVED]`

**Author:** mathematician-agent (River's odd-zeta program), task **P1i**
**Date:** 2026-07-25
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, artefacts in `work/p1i/`
**Predecessors (authoritative):** `work/PHASE2_INDUCTION.md` (the `(IND)` framework, `(DEPTH-gen)`,
Lemma F-gen, the budget ledger, and the statement of `(GAP-DESC)` in §6.2),
`work/PHASE2_NUCLEUS.md` (P1h — `(BASE)`), `work/PHASE2_ENDGAME.md` (§R3 Lemma D++,
the `a < p` off-regime route), `work/PHASE2_THEOREM.md` v3.

**Labels.** `[PROVED]` complete proof written out here · `[VERIFIED r]` exact finite check on
range `r`, 0 failures (evidence, never proof) · `[CERT]` machine certificate · `[OPEN]`.

---

## 0. HEADLINE

1. **`(GAP-DESC)` IS PROVED** — and not only for `a ≥ p`. The proof is uniform in the digit level:
   it holds for **every** `L = ⌊log_p n⌋ ≥ 1`, i.e. it re-proves the `a < p` case as well, and it
   does so **without Lemma D++, without Lemma G, without Lemma B, Lemma F, Lemma Phi, the carry
   inequalities (C1),(C2), and without Wolstenholme**. Its only inputs are **`(DEPTH-gen)`
   applied at *both* levels** and **Kummer's theorem**.

2. **The route the brief and `PHASE2_INDUCTION` §6.2 anticipated does not exist**, and this is a
   hard negative, not a stylistic remark. §6.2 proposed: *"the mismatch pole `v_p(a+b+1) = λ` is
   bounded by `M_a` and is compensated by `λ` extra Kummer carries in `C(n+k,n)` via (C1)."* At
   weight 5 that trade is **losing by a factor of 5**: the letter-wise descent mismatch of
   `A_m(k)` is `e₁(a+b+1)^{−m}`, of valuation `−mλ`, while the *entire* Kummer gain of `T` in that
   slot is `1+λ`. Explicitly, at `p = 5`, `n = 19`, `(k,l) = (6,0)` (so `a = 3, b = 1`,
   `a+b+1 = p`, `e₁ = 1`): `v_pT = 4`, the `A₅(k)` term of the letter-wise expansion has
   `v_p = 4 − 5 = −1`, and the target is `0`. **`[VERIFIED, §5]`** The pole is not there in the
   assembled `𝓔`: it is annihilated *inside* `v₅` by the `(DEPTH)` conditions at level `n`.
   The correct instrument is therefore `(DEPTH-gen)` at level `n` — not a letter-wise ledger.

3. **The whole node collapses to one purely combinatorial statement**, proved in §3:

   > **Lemma DK (descent Kummer).** For `p ≥ 5`, `L = ⌊log_p n⌋ ≥ 1`, `a = ⌊n/p⌋`, and every
   > **off-regime** cell, `v_p T(n,k,l) ≥ 1 + max(s_n, s_a)`, where `s_n`, `s_a` are the pattern
   > sums `α+γ+κ` of `PHASE2_INDUCTION` §2.3 at level `n` (with `P = p^{L+1}`) and at level `a`
   > (with `P_a = p^L`).

   `[VERIFIED 188 353 733 / 188 353 733 off-regime cells, digit levels L = 1,2,3,4, 0 failures,
   slack 0 attained]`
   The mechanism is one line: *off-regime means a carry in base-`p` position `0`, the pattern
   indicators live in position `L ≥ 1`, and Kummer counts both.*

4. **Consequently the induction step of `(IND)` is complete at every digit level**, and — with
   `(BASE)` `[P1h]` — **the `p ≥ 5` mathematics of Phase 2 is finished**: for the `P_n` law what
   is left is the *single* decomposition certificate `(T1-top)` `P_n = Σ T·w₅` (the second one,
   `P̂_n = Σ T·ŵ₃`, is needed only for the companion middle row), owned by the certificate agent
   (`work/PHASE2_CERTS.md`, read-only from here). Since the argument below is
   representative-independent (§6), the `w₅` target may be taken to be the *single* identity for
   `w₅^I` — the representative `(BASE)` already uses — instead of `w5_allp` plus the homogeneous
   delta of `PHASE2_NUCLEUS` §5.

5. **Sweeps (all exact, 0 failures).**

| sweep | range | cells | failures |
|---|---|---|---|
| **Lemma DK** and its ingredients `(DK1),(DK2)`, Lemma D1 | 944 levels, `p ≤ 31`, `L = 1,2,3,4` | **188 353 733** off-regime | **0** |
| the same criterion, in-regime (**control**: it must and does FAIL there) | same | 13 082 671 in-regime | 134 964 failures — *by design* |
| the **slot-wise** inequalities behind `(DK2)`, + the exact carry identities | `p ≤ 31`, `L = 1,2,3` | **11 096 075** | **0** |
| **`(GAP-DESC)` itself**, exact `p`-adic `𝓔` | `p ≤ 13`, `L = 1,2,3` | 1 640 083 off-regime | **0** (min slack **0** at `L=1`) |
| whole term (I), **both** regimes + the aggregate `v_p(Σ T𝓔)` | `p ≤ 13`, `L = 2,3` | 15 553 in + 345 334 off | **0** |
| `(DEPTH-gen)` + `(GAP-DESC)` for the **`w₅^I`** representative of P1h | `p ≤ 13`, `L ≤ 2` | 15 228 + 43 213 | **0** |

---

## 1. Setup, and exactly what is quoted

Fix a prime `p ≥ 5` and `n ≥ p`; put

```
L := ⌊log_p n⌋ ≥ 1 ,  M := L+1 ,  P := p^M      (so n < P),
a := ⌊n/p⌋ ,  r := n − ap ∈ [0,p)               (so p^{L−1} ≤ a < p^L =: P_a, ⌊log_p a⌋ = L−1).
```

For a cell `0 ≤ k,l ≤ n` write `b := ⌊k/p⌋ ≤ a`, `s := k − bp`, `c := ⌊l/p⌋ ≤ a`, `t := l − cp`,
and the four base-`p` carry indicators of `PHASE2_INDUCTION` §3.2

```
e₁ := [r+s ≥ p],   e₂ := [r+t ≥ p],   e₃ := ⌊(r+s+t)/p⌋ ∈ {0,1,2},   e₄ := [s+t ≥ p],
ζ  := e₃ − e₄ .
```

> **IN-REGIME** := `s ≤ r`, `t ≤ r` and `e₁ = e₂ = e₃ = e₄ = 0`; **OFF-REGIME** := everything else.

`(α,γ,κ,θ)` is the level-`n` pattern of `PHASE2_INDUCTION` §2.3 computed with `P = p^{L+1}`, and
`(α_a,γ_a,κ_a,θ_a)` the level-`a` pattern computed with `P_a = p^L`; `s_n := α+γ+κ`,
`s_a := α_a+γ_a+κ_a`. Finally, with `v₅ := w₅ − H^{(5)}_n` as in `PHASE2_INDUCTION` §1,

```
𝓔(n,k,l) := p⁵·v₅(n,k,l) − v₅(a, b, c) ,        (I) = Σ_{k,l} T(n,k,l)·𝓔(n,k,l) .
```

> **`(GAP-DESC)`** (the node, verbatim from `PHASE2_INDUCTION` §6.2, with the range widened from
> `a ≥ p` to all `a ≥ 1`). *For every off-regime cell,*
> ```
>            v_p( T(n,k,l)·𝓔(n,k,l) )  ≥  −5(L−1) .
> ```

**Quoted, proved elsewhere, used below.**

* **`(DEPTH-gen)`** `[PROVED — PHASE2_INDUCTION §2.4, Prop. LIFT + the (DEPTH) `[CERT]`]`. For
  every prime `p ≥ 5`, every `m ≥ 1` and every cell `(x,y)` of level `m`,
  ```
        d₅(m,x,y) := max(0, −v_p v₅(m,x,y))  ≤  5⌊log_p m⌋ + 1 + min(s, 2) ,
  ```
  `s` the pattern sum at level `m`. *(The refined cap `J(π) = 0` at the trivial pattern is
  available but **not** used here.)*
* **Kummer's theorem** `v_p C(x+y,x) = #{carries in the base-`p` addition x+y}`.

Nothing else. In particular the proof below uses **neither** the in-regime machinery of §4.3
(`Ψ_S`, the `Φ_π` functionals) **nor** any of the Lemma-F apparatus.

---

## 2. The digit dictionary `[PROVED]`

> **Lemma D1.** With the notation of §1:
> 1. `⌊(n+k)/p⌋ = a+b+e₁`, `⌊(n+l)/p⌋ = a+c+e₂`, `⌊(n+k+l)/p⌋ = a+b+c+e₃`,
>    `⌊(k+l)/p⌋ = b+c+e₄`, `⌊(n−k)/p⌋ = a−b−[s>r]`, `⌊n/p⌋ = a`.
> 2. `0 ≤ ζ = e₃−e₄ ≤ 1`, and `ζ = 1` iff the addition `n+(k+l)` carries out of position `0`.
> 3. `α = [a+b+e₁ ≥ P_a] ≥ α_a` and `γ = [a+c+e₂ ≥ P_a] ≥ γ_a`.
> 4. `ε := ⌊(k+l)/P⌋ = ⌊(b+c+e₄)/P_a⌋ = ε_a + e₄·[b+c = P_a−1]`, and
>    `κ = [a+b+c+e₃ ≥ (ε+1)P_a]`.
> 5. `κ ≥ κ_a` **unless** `e₄ = 1` and `b+c = P_a−1`; hence in all cases
>    ```
>              s_n  ≥  s_a − [e₄ = 1] .
>    ```
> 6. In-regime, `s_n = s_a` (and, by §4.3, `v_p T(n,k,l) = v_p T(a,b,c)`).

*Proof.* 1. is the definition of the four indicators (`n = ap+r`, `k = bp+s`, `l = cp+t`, and
`n−k = (a−b−[s>r])p + ((r−s) mod p)`).

2. `e₄ ≤ e₃` because `r+s+t ≥ s+t`, and `e₃ ≤ e₄+1` because `r < p`. The digit of `k+l` in
position `0` is `s+t−e₄p`, so the addition `n+(k+l)` carries out of position `0` iff
`r+s+t−e₄p ≥ p` iff `e₃ ≥ e₄+1`.

3. `n+k ≥ P = p·P_a` iff `⌊(n+k)/p⌋ ≥ P_a` iff `a+b+e₁ ≥ P_a`, and `a+b+e₁ ≥ a+b`.

4. `b+c ≤ 2a ≤ 2P_a − 2`, so `1 ≤ b+c+1 ≤ 2P_a−1` contains exactly one multiple of `P_a`, namely
`P_a` itself; hence `⌊(b+c+1)/P_a⌋ − ⌊(b+c)/P_a⌋ = [b+c = P_a−1]`. The formula for `κ` is
`n+k+l ≥ (ε+1)P ⟺ ⌊(n+k+l)/p⌋ ≥ (ε+1)P_a`.

5. If `ε = ε_a`, then `κ = [a+b+c+e₃ ≥ (ε_a+1)P_a] ≥ [a+b+c ≥ (ε_a+1)P_a] = κ_a`. Otherwise `ε`
exceeds `ε_a`, which by 4. forces `e₄ = 1` and `b+c = P_a−1`; and always `κ ≥ κ_a − 1` because
both are `0/1`. Adding 3. gives the display.

6. In-regime all four `e_i` vanish, so 3. and 4. give `α = α_a`, `γ = γ_a`, `ε = ε_a`, `κ = κ_a`. ∎

*(Remark. Item 5 is sharp: `e₄ = 1` with `b+c = P_a−1` really does drop `κ` from `1` to `0`.
Explicitly `p = 5`, `n = 101`, `(k,l) = (63,63)`: `L = 2`, `a = 20`, `r = 1`, `b = c = 12`,
`s = t = 3`, `b+c = 24 = P_a−1`, `(e₃,e₄) = (1,1)`, level-`a` pattern `(1,1,1,1)` with `s_a = 3`,
level-`n` pattern `(1,1,0,1)` with `s_n = 2`. There `B = 4` and `v_pT = 10 ≥ 1+max(s_n,s_a) = 4`.
`[VERIFIED]` `work/p1i/s4_carry.py` meets the exceptional configuration 20 798 times in the sweep
range and Lemma DK survives every one of them.)*

---

## 3. Lemma DK — the descent Kummer lemma `[PROVED]`

Define the **bottom-carry count**

```
B := e₁ + e₂ + 2[s>r] + 2[t>r] + ζ .
```

> **Lemma DK.** Let `p ≥ 5`, `n ≥ p`, `L = ⌊log_p n⌋ ≥ 1`, and let `(k,l)` be **off-regime**. Then
> ```
>   (DK1)   B ≥ 1 ;   and if  e₄ = 1  then  B ≥ 2 ;
>   (DK2)   v_p T(n,k,l)  ≥  s_n + B ;
>   (DK3)   v_p T(n,k,l)  ≥  1 + max(s_n, s_a) .
> ```

*Proof.*

**(DK1).** Three exhaustive cases.
* `s > r` or `t > r`: then `B ≥ 2` outright, from the term `2[s>r]` resp. `2[t>r]`.
* `s ≤ r`, `t ≤ r`, `e₄ = 1`: then `r+s ≥ s+t ≥ p` and `r+t ≥ s+t ≥ p`, so `e₁ = e₂ = 1` and
  again `B ≥ 2`.
* `s ≤ r`, `t ≤ r`, `e₄ = 0`: then `ζ = e₃`, and off-regime forces `e₁+e₂+e₃ ≥ 1`; each of the
  three summands contributes `1` to `B` (for `e₃` through `ζ = e₃`), so `B ≥ 1`.

So `B ≥ 1` always, and — since `e₄ = 1` occurs only in the first two cases — `e₄ = 1 ⟹ B ≥ 2`.

**(DK2).** Write `T = C(n+k,n)·C(n,k)²·C(n+l,n)·C(n,l)²·C(n+k+l,n)` and let
`V₁,…,V₅` be the `v_p` of the five binomials, so `v_pT = V₁+V₂+2V₃+2V₄+V₅`. By Kummer each `V_i`
is a count of carries in one addition. In each addition we locate the **bottom** carry (out of
base-`p` position `0`) and, where the level-`n` pattern demands one, the **top** carry (out of
position `M−1 = L`); the two positions are distinct precisely because `L ≥ 1`, i.e. because we
are in the multi-digit regime — this is the one and only place the hypothesis is used.

* `V₁` counts the carries of `n+k`. Position `0`: carries iff `r+s ≥ p`, i.e. iff `e₁ = 1`.
  Position `L`: since `n,k < P = p^{L+1}`, it carries iff `n+k ≥ P`, i.e. iff `α = 1`
  (`PHASE2_INDUCTION` Lemma K). Hence `V₁ ≥ α + e₁`. Likewise `V₂ ≥ γ + e₂`.
* `V₃` counts the carries of `k + (n−k)`. In position `0` the digits are `s` and `(r−s) mod p`,
  summing to `r + p·[s>r]`, so it carries iff `s > r`. Hence `V₃ ≥ [s>r]`, and likewise
  `V₄ ≥ [t>r]`.
* `V₅` counts the carries of `n + (k+l)`. Position `0`: carries iff `ζ = 1` (Lemma D1.2).
  Position `L`: writing `k+l = εP+ρ`, `0 ≤ ρ < P`, the low `M` digits of the addition sum to
  `n+ρ`, so it carries out of position `M−1 = L` iff `n+ρ ≥ P`, i.e. iff `κ = 1`
  (`PHASE2_INDUCTION` Lemma K). Hence `V₅ ≥ κ + ζ`.

Summing with the multiplicities `(1,1,2,2,1)`:
`v_pT ≥ (α+γ+κ) + (e₁+e₂+2[s>r]+2[t>r]+ζ) = s_n + B`.

**(DK3).** By (DK2) and (DK1), `v_pT ≥ s_n + B ≥ s_n + 1`. For the level-`a` half, Lemma D1.5
gives `s_n ≥ s_a − [e₄=1]`, and (DK1) gives `B ≥ 1 + [e₄=1]`; hence
`v_pT ≥ s_n + B ≥ (s_a − [e₄=1]) + (1 + [e₄=1]) = s_a + 1`. ∎

**`[VERIFIED 188 353 733 / 188 353 733, 0 failures]`** (`work/p1i/s4_carry.py`: 931 levels over
`p ∈ {5,7,11,13,17,19,23,29,31}`, digit levels `L = 1,2,3`, 142 820 576 off-regime cells;
`work/p1i/s9_lvl4.py`: 13 further levels at `L = 4` (and `L = 3`), `p ∈ {5,7,11}`, `n` up to
3 124, 45 533 157 off-regime cells; **all** cells `0 ≤ k,l ≤ n` in each level): `(DK1)`,
`(DK2)`, `(DK3)`, Lemma D1.2 and Lemma D1.5 hold at every off-regime cell, with **0** violations.
The criterion that Theorem 4.1 consumes, `v_pT ≥ max(J(π_n),J(π_a))`, has slack **0** at 41 284
of them, so the lemma is **sharp**. The five slot-wise inequalities used in the proof of `(DK2)`
were checked separately, one binomial at a time, on 11 096 075 cells with **0** violations
(`work/p1i/s8_slots.py`), together with the two exact carry identities
`V₁ = v_pC(a+b,a) + e₁(1+v_p(a+b+1))` and `V₃ = v_pC(a,b) + [s>r](1+v_p(a−b))` quoted in §5.

**Control `[VERIFIED]`.** In-regime, `B = 0` and `s_n = s_a` at **every** one of the 13 082 671
in-regime cells of the sweep (0 exceptions, as Lemma D1.6 predicts) and the criterion
`v_pT ≥ max(J(π_n),J(π_a))` **fails** at 134 964 of them.
So off-regime is not a convenience of the proof: it is exactly the hypothesis that buys the
extra power of `p`. *(This is the structural reason the induction step must be split into two
regimes at all, and why §4.3's `Ψ_S`-expansion is unavoidable in-regime.)*

---

## 4. `(GAP-DESC)` `[PROVED]`

> ### **Theorem 4.1 `(GAP-DESC)`.**
> Let `p ≥ 5`, `n ≥ p`, `L = ⌊log_p n⌋ ≥ 1`, `a = ⌊n/p⌋`, and let `(k,l)`, `0 ≤ k,l ≤ n`, be an
> **off-regime** cell, `b = ⌊k/p⌋`, `c = ⌊l/p⌋`. Then, with `𝓔 = p⁵v₅(n,k,l) − v₅(a,b,c)`,
> ```
>            v_p( T(n,k,l)·𝓔(n,k,l) )  ≥  −5(L−1) .
> ```

*Proof.* `(DEPTH-gen)` at level `n` (`⌊log_p n⌋ = L`, pattern sum `s_n`) gives
`v_p v₅(n,k,l) ≥ −5L − 1 − min(s_n,2)`, hence

```
v_p( p⁵ v₅(n,k,l) )  ≥  5 − 5L − 1 − min(s_n,2)  =  −5(L−1) − 1 − min(s_n,2) .
```

`(DEPTH-gen)` at level `a` (`⌊log_p a⌋ = L−1`, pattern sum `s_a`) gives

```
v_p( v₅(a,b,c) )  ≥  −5(L−1) − 1 − min(s_a,2) .
```

Therefore

```
v_p(𝓔)  ≥  −5(L−1) − 1 − max( min(s_n,2), min(s_a,2) )  ≥  −5(L−1) − 1 − max(s_n, s_a) ,
```

while Lemma DK gives `v_p T(n,k,l) ≥ 1 + max(s_n,s_a)`. Adding the two displays proves the
theorem. ∎

> ### **Corollary 4.2 (the descent term (I)) `[PROVED]`.**
> For every `p ≥ 5` and every `n` with `L = ⌊log_p n⌋ ≥ 1`,
> ```
>            v_p( (I) )  =  v_p( Σ_{k,l} T(n,k,l)·𝓔(n,k,l) )  ≥  −5(L−1) ,
> ```
> cell by cell: off-regime by Theorem 4.1, in-regime by `PHASE2_INDUCTION` §4.3 `[PROVED]`.

> ### **Corollary 4.3 (the `(IND)` step) `[PROVED]`.**
> `𝓘(L−1) ⟹ 𝓘(L)` for every `L ≥ 1`: in `PHASE2_INDUCTION` §4.2 the term (II) is bounded by
> `(DEPTH-gen)` + Lemma F-gen (slack exactly 0) and the term (I) by Corollary 4.2. Hence, with
> `(BASE)` = `𝓘(0)` `[PROVED, PHASE2_NUCLEUS.md]`,
> ```
>       ord_p(P_n) ≥ −5⌊log_p n⌋   for every prime p ≥ 5 and every n ≥ 1,
> ```
> i.e. **(SHARP-12, `p ≥ 5` part)** — modulo only the decomposition certificate `(T1-top)`.

**Sharpness.** The proof's slack at a cell is `v_pT − 1 − max(min(s_n,2),min(s_a,2)) ≥ 0`, and the
*true* quantity `v_p(T𝓔) + 5(L−1)` attains `0` (e.g. `p = 13, n = 153, (k,l) = (1,41)`:
`v_pT = 3`, `v_p𝓔 = −3`, target `0`). So Theorem 4.1 cannot be weakened, and the ledger of §7 is
exact.

---

## 5. The trap: why the letter-wise route of §6.2 fails `[VERIFIED]`

`PHASE2_INDUCTION` §6.2 assessed `(GAP-DESC)` as *"a carry-bookkeeping lift of `endgame` §R3 with
one order of slack available, of exactly the kind executed in §3.4"*, the mechanism being: the
descent of a letter produces a mismatch term, and the mismatch **forces carries**, e.g.

```
p^m A_m^{(n)}(k) = A_m^{(a)}(b) + e₁·(a+b+1)^{−m} + p^m σ^A ,
v_p C(n+k,n) = v_p C(a+b,a) + e₁(1+λ₁) ,   λ₁ := v_p(a+b+1)                        (5.1)
```

*(both identities are correct — the second follows from (C1) with `z(a+b) = λ₁`, and is
`[VERIFIED]` in `work/p1i/s7_trap.py`)*. **But the trade is losing at weight 5.** Expanding
`𝓔` letter-wise, `𝓔 = Σ_{S ≠ ∅} (∏_{X∈S} D_X)·Ψ_S` with `D_X` the per-letter mismatch, the
single term `S = {A₅(k)}` contributes

```
c · (a+b+1)^{−5} ,   v_p = −5λ₁ ,   c := the w₅-coefficient of the symmetrised A₅(k)+A₅(l)
                                    monomial  =  3830046703/48 ≠ 0 in w5_allp (a p-unit),
```

against a total Kummer gain of only `1+λ₁` in the whole of `T`. Cell-wise (`work/p1i/s7_trap.py`;
the last column is the *true* value, computed with the exact `p`-adic evaluator):

| `p` | `n` | `(k,l)` | `a,b` | `λ₁` | `v_pT` | letter-wise `S={A₅(k)}` term `v_pT − 5λ₁` | target `−5(L−1)` | true `v_p(T𝓔)` | |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 19 | (6,0) | 3,1 | 1 | 4 | **−1** | 0 | **1** | **letter-wise FAILS** |
| 5 | 19 | (6,19) | 3,1 | 1 | 4 | **−1** | 0 | **1** | **letter-wise FAILS** |
| 5 | 99 | (26,30) | 19,5 | 2 | 8 | −2 | −5 | 0 | (survives, but by 3 not by design) |
| 7 | 244 | (100,50) | 34,14 | 2 | 8 | −2 | −5 | 0 | (idem) |

so at `p = 5, n = 19, (k,l) = (6,0)` the letter-wise ledger is short by exactly one power — and
no refinement of the carry bookkeeping can repair it, because (5.1) is an **equality**. (This is
the weight-5 shadow of the fact that `endgame` §R3 could afford the trade only up to weight 3:
Lemma D++ supplies `v_pT ≥ 4`, which covers `A₃` but not `A₅`.)

**What actually happens.** The pole is not present in `𝓔` at all: `p⁵v₅(n,k,l)` has
`v_p ≥ −5(L−1) − 1 − min(s_n,2) ≥ −5(L−1) − 3`, because the `(DEPTH)` conditions annihilate the
top `u`-coefficients of `v₅` **at level `n`** — the mismatch poles of the individual letters
cancel among themselves inside `v₅`. Hence the correct instrument for the off-regime descent is
`(DEPTH-gen)` at level `n`, and the only thing left to check is that `T` pays for the *two*
depth caps, which is Lemma DK.

**Consequence for the tree.** `Lemma D++` (`endgame` §R3) is **no longer needed** for the descent
term at any digit level; the `a < p` case of `(GAP-DESC)` is now a special case of Theorem 4.1.
(D++ remains what it was inside the `(LB₅)` assembly, which `(IND)` does not use.)

---

## 6. Scope, and what the proof does *not* need

* **Uniform in the level.** Theorem 4.1 holds for every `L ≥ 1`; nothing in §§2–4 distinguishes
  `a < p` from `a ≥ p`. The hypothesis `L ≥ 1` enters exactly once — in `(DK2)`, to know that
  digit positions `0` and `L` are distinct. At `L = 0` there is no descent to make.
* **No `p ∤ Q_a`, no `Λ = Q_n/Q_a`, no supercongruence, no Lemma Phi** — as with Lemma F-gen, the
  exceptional primes cost nothing.
* **No Wolstenholme.** `p ≥ 5` is inherited only from `(DEPTH-gen)` (through the representative)
  and from the surrounding theorem; the arguments of §§2–4 are valid for every prime.
* **Representative-independence.** The proof consumes `w₅` only through `(DEPTH-gen)`, i.e. it
  works verbatim for **any** point of the 124-dimensional depth-conditioned family — in
  particular for **`w₅^I`** (`work/p1g/w5_exIII_allp.json`), the representative that
  `PHASE2_NUCLEUS` §2 uses for `(BASE)`. `[VERIFIED]`: `w₅^I` satisfies `(DEPTH-gen)` (0
  violations in 15 228 cells, including the refined trivial-pattern cap `J = 0`) and Theorem 4.1
  holds for it (0 failures in 43 213 off-regime cells, 18 levels, `p ≤ 13`) —
  `work/p1i/s5_rep.py`. **So the whole of `(IND)` *and* `(BASE)` can be run with one and the same
  representative `w₅^I`**, in which case the weight-5 certificate obligation is the **single**
  identity `P_n = Σ_{k,l} T·w₅^I` rather than `w5_allp`'s identity *plus* the homogeneous delta
  `Σ T(w₅^I − w5_allp) = 0` of `PHASE2_NUCLEUS` §5. (Which of the two is cheaper to certify is
  the certificate agent's call — `PHASE2_CERTS` §1 shows the two are genuinely different
  obligations, §14.3 costs them.)

---

## 7. The budget ledger, completed

Per cell, per digit level (`L ≥ 1`, `n = ap+r`), for the **descent** term (I), off-regime:

| quantity | value | source |
|---|---|---|
| provided: `v_p(p⁵v₅(n,k,l))` | `≥ −5(L−1) − 1 − min(s_n,2)` | **(DEPTH-gen)** at level `n` |
| provided: `v_p(v₅(a,b,c))` | `≥ −5(L−1) − 1 − min(s_a,2)` | **(DEPTH-gen)** at level `a` |
| provided: `v_p T(n,k,l)` | `≥ 1 + max(s_n,s_a)` | **Lemma DK** (§3) |
| consumed: target | `≥ −5(L−1)` | `(IND)` step, term (I) |
| **slack** | **≥ 0, and `0` is attained** | §4 |

Together with `PHASE2_INDUCTION` §4.2 (term (II): `(DEPTH-gen)` + Lemma F-gen, slack exactly 0)
and §4.3 (term (I) in-regime, slack ≥ 0), **every line of the induction step is now closed, and
no line has spare depth.**

---

## 8. Sweeps `[all exact arithmetic, 0 failures]`

All `p`-adic arithmetic is exact: valuations are computed with tracked precision
(`work/p1i/pad.py`), and the evaluator is cross-checked against exact `fractions.Fraction`
evaluation of the 178-term `w5_allp` on 1 290 cells with **0** mismatches of valuation *or* unit
(`work/p1i/t0_check.py`).

| # | sweep | range | cells | failures | min slack |
|---|---|---|---|---|---|
| 1 | **Lemma DK** `(DK1),(DK2),(DK3)` + Lemma D1.2, D1.5 | 931 levels, `p ∈ {5,7,11,13,17,19,23,29,31}`, `L = 1,2,3` | **142 820 576** off-regime | **0** | **0** attained (41 284 cells) |
| 1b | the same, at digit level **`L = 4`** (and `L = 3` controls) | 13 levels, `p ∈ {5,7,11}`, `n` up to 3124 | **45 533 157** off-regime | **0** | 1 |
| 2 | control: the same criterion **in-regime** | rows 1+1b | 10 281 175 + 2 801 496 | **134 289 + 675 failures — by design** | — |
| 3 | control: `B = 0` and `s_n = s_a` in-regime (Lemma D1.6) | rows 1+1b | 13 082 671 | **0** | — |
| 4 | **slot-wise** `V₁ ≥ α+e₁`, `V₃ ≥ [s>r]`, `V₅ ≥ κ+ζ`, and the exact identities `V₁ = v_pC(a+b,a)+e₁(1+λ₁)`, `V₃ = v_pC(a,b)+[s>r](1+μ₁)` | `p ≤ 31`, `L = 1,2,3` | **11 096 075** | **0** | — |
| 5 | **Theorem 4.1**, exact `p`-adic `𝓔` | `p ∈ {5,7,11,13}`, `L = 1`, 86 levels | 174 527 | **0** | **0** (attained) |
| 6 | **Theorem 4.1**, exact `p`-adic `𝓔` | `p ∈ {5,7,11,13}`, `L = 2`, 35 levels | 530 900 | **0** | 2 |
| 7 | **Theorem 4.1**, exact `p`-adic `𝓔` | `p ∈ {5,7}`, `L = 3`, 16 levels (`p = 11` still running) | 934 656 | **0** | 3 |
| 8 | whole term (I), **both** regimes, + the aggregate `v_p(Σ_{k,l} T𝓔)` | `p ≤ 13`, `L = 2,3`, 20 levels | 15 553 in + 345 334 off | **0** | in 2 / off 2 |
| 9 | `(DEPTH-gen)` (incl. the refined `J = 0` cap) **and** Theorem 4.1 for **`w₅^I`** | `p ≤ 13`, `L ≤ 2` | 15 228 + 43 213 | **0** | 0 / 1 |
| 10 | the letter-wise route **fails** (the trap of §5) | 4 exhibited cells | — | *short by 1 power* | — |
| 11 | evaluator cross-check `pad.py` vs exact `Fraction` | `p = 5,7,11`, `n ≤ 13` | 1 290 | **0** | — |

Rows 1 + 1b are the decisive ones: together they are the whole content of `(GAP-DESC)` beyond
`(DEPTH-gen)`, checked on **every** cell of 944 different levels — **188 353 733 off-regime
cells, digit levels `L = 1,2,3,4`, 0 failures** — with **no** sampling inside a level. Rows 5–8 test the
assembled statement itself with the exact `p`-adic `𝓔`, i.e. they also re-test `(DEPTH-gen)`,
Prop. LIFT and the `(DEPTH)` certificate along the way. In row 1 the slack of the criterion
`v_pT ≥ max(J(π_n),J(π_a))` is `0` at 41 284 cells (all of them with `max(s_n,s_a) ≥ 1`, where
the coarse cap `1+max(min(s_n,2),min(s_a,2))` used in §4 coincides with it), so **neither
Lemma DK nor Theorem 4.1 can be weakened.**

---

## 8bis. Sweeps still running at the time of writing

`work/p1i/s3_lvl3.out` (level-3 exact `𝓔`; the remaining `p = 7,11` levels, up to `n = 1342`) was
still running when this file was written — every level it had completed reported **0 failures**;
its final lines are the record. It is not load-bearing: rows 1, 1b of §8 cover the criterion on
188.4 M cells and rows 5–8 cover the assembled statement on ~1.6 M cells.

`work/p1i/s1_crude.py` / `s2_crude_big.py` were the first (coarser) scans of the same criterion,
written before Lemma DK was found; `s1` ran clean (272 282 off-regime cells) and `s2` was **superseded and
stopped** — `s4_carry.py` + `s9_lvl4.py` check strictly more, on strictly more cells.

---

## 9. What this leaves, and one cheap follow-on

* **`p ≥ 5` side:** nothing mathematical. The single remaining obligation for the `P_n` law is the
  decomposition certificate `(T1-top)`; the middle row additionally needs Theorem B. Both are the
  certificate agent's (`work/PHASE2_CERTS.md`).
* **`p ∈ {2,3}`:** untouched by this node — the factor `12` remains the July H2 remnant
  (`PHASE2_THEOREM` §D.2).
* **Cheap follow-on, if formalisation is wanted.** Lemma D1 and Lemma DK are pure base-`p`
  combinatorics over `ℕ` — no harmonic numbers, no representative, no analysis. They are the
  most formalisation-ready statements the program has produced since Theorem A (already
  `[LEAN]`), and would make the induction step's Kummer half machine-checked. `(DEPTH-gen)`
  would remain the analytic input.

---

## 10. Reproduction — `work/p1i/`

| script | what it does | output |
|---|---|---|
| `kummer.py` | carries, `v_pT`, patterns, `J(π)` | — |
| `pad.py` | exact `p`-adic arithmetic (valuation + unit, tracked precision) and a `w₅` evaluator | — |
| `t0_check.py` | cross-check of `pad.py` against exact `Fraction` evaluation | 1 290 cells, 0 mismatches |
| `s1_crude.py` | first (coarser) scan of the criterion `v_pT ≥ max(J(π_n),J(π_a))` | 272 282 off-regime cells, 0 failures |
| `s2_crude_big.py` | the same, wider — **superseded** by `s4`+`s9`, stopped | — |
| `s4_carry.py` | **Lemma DK** and its ingredients, + the in-regime controls (`L ≤ 3`) | `s4_carry.out` |
| `s9_lvl4.py` | the same at digit level `L = 4`, `n` up to 3 124 | `s9_lvl4.out` |
| `s8_slots.py` | the slot-wise inequalities behind `(DK2)` + the exact carry identities | `s8_slots.out` |
| `s3_exact.py lvl1\|lvl2\|lvl3\|lvl4` | **Theorem 4.1** with exact `𝓔`, off-regime | `s3_lvl*.out` |
| `s6_allcells.py` | whole term (I), both regimes, + `v_p(Σ_{k,l} T𝓔)` | `s6_all.out` |
| `s5_rep.py <w5.json>` | `(DEPTH-gen)` + Theorem 4.1 for another representative (`w₅^I`) | `s5_exIII.out` |
| `s7_trap.py` | the letter-wise route: mismatch pole `−mλ` vs Kummer gain `1+λ` | `s7_trap.out` |

Nothing in `work/lb5/`, `work/p1d/`, `work/p1g/`, `work/p1h/` was modified; `work/PHASE2_CERTS.md`
was read only.
