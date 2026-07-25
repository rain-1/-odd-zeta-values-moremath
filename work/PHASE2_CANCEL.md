# P1f — the weight-5 cancellation identity `(V2)/(V3)`: reduction, new identities, and the wall

**Author:** mathematician-agent (River's odd-zeta program), task **P1f**
**Date:** 2026-07-25
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, artefacts in `work/p1f/`
**Target (from `work/PHASE2_INDUCTION.md` §6.3 / `work/PHASE2_THEOREM.md` v2 §6.3):**
`(V2) Σ (T/p)·K_{5L+2} ≡ 0` and `(V3) Σ (T/p²)·K_{5L+3} ≡ 0` (mod `p`), at every digit level `L`.

**Labels.** `[PROVED]` complete proof written out here · `[VERIFIED r]` exact finite check, 0
failures · `[GAP]` not settled, stated precisely.

---

## 0. HEADLINE

**The identity is NOT proved, and this session establishes *why* — with a proof, not a shrug.**

1. **The target simplifies to one statement.** `(V2)` is **vacuous** for `w5_allp`, and `(BASE)`
   is *exactly* the single mod-`p` identity `(V3)₀` (§2). The `(V2)/(V3)` pair at levels `L ≥ 1`
   is a consequence of the already-proved induction step, and is verified graded at `L = 1` (§6).
2. **The toolbox's weight-2 level exists and is now proved.** Three new exact residue identities
   `(P1),(P2),(P3)` — the weight-2 twins of Lemma Phi, obtained from the same `G(x)` by an extra
   rational factor — are derived and verified exactly (§3). They are genuinely new and reusable.
3. **`(V3)₀` is fully de-`p`-adicised** (§4): every ingredient reduces, by Wilson + the two
   reflections + one closed form for `C(p+m,n)/p`, to an *explicit rational function of `(n,q)`
   alone*, `q = p−n`. `(V3)₀` becomes the elementary congruence `F(n,p−n) ≡ 0 (mod p)` for an
   explicit finite double sum `F`. `[VERIFIED]`
4. **THE WALL, and it is a theorem, not an impression (§5).** The cancellation obstruction is a
   linear functional `θ_{p,n}` on weight-5 forms that **factors through the value map
   `w ↦ Σ_{k,l} T·w`**. Hence
   * every identity of "Lemma Phi species" — `Σ_{k,l} T·M = 0` — lies in the kernel of the
     fitting system and **changes no value**: it can never move `θ`. **Route R1 cannot close
     `(BASE)`, in principle.**
   * `θ` is **not** identically zero on the `(DEPTH)`-conditioned space: random depth-conditioned
     `w` give `min_n v_p(Σ T w) = −1` at `p = 5,7,11,13`. `[VERIFIED 3 trials × 4 primes]`
     So the depth calculus, plus *any* amount of summand-side identity work, provably cannot
     prove `(BASE)`. This is the structural reason `(DEPTH⁺)`/`(DEPTH⁺⁺)` are inconsistent.
   * the reflection route **R3** is refuted concretely: the deficit regions have unequal sizes and
     unequal residue multisets, so no involution pairs them (§5.3).
5. **The one route that is not walled** is the one the walls point at: `(BASE)` is a statement
   about the **number** `P_n`, so a proof must import a property of `P_n`. Two such inputs exist
   and are costed in §7: **(V-a)** a *cellwise-integral representation* — the exact analogue of
   Apéry's classical `Σ (−1)^{m−1}/(2m³C(n,m)C(n+m,m))` weight, which is verified here to make
   the `ζ(3)` base case cellwise with slack `0` and **no cancellation at all**; and **(V-b)** the
   certified order-3 recurrence, which reduces `(BASE)` to **1–4 explicitly located exceptional
   steps per prime** (§7.2), the genuine one being at `n = (p−5)/2`, i.e. producing exactly the
   known attained deficit cell `n = (p+1)/2`.
6. **(V-a) is sharply targeted and the mechanism is measured.** Exactly one order is missing, and
   only on the three `s = 2` patterns (§7.1 table). Apéry-type letters
   `R^{(a)}(n,k) = Σ_{m≤k}(−1)^{m−1}/(m^aC(n,m)C(n+m,m))` have **pole order 1 for every weight
   `a = 1..5`**, with pole indicator exactly `α` — the same indicator as `A_a(k)` but one third
   of the depth at weight 3 (Prop. 7.2, `[VERIFIED p ≤ 19]`). That is precisely the missing
   order, and it lives outside the basis in which the impossibility was proved.

---

## 1. The exact `u`-grading (`work/p1f/kgrade.py`) `[VERIFIED]`

Lemma U of `PHASE2_INDUCTION` §2.1 is implemented verbatim: every letter
`X_m = H^{(m)}_{N₁} − H^{(m)}_{N₂}` is expanded as `Σ_{e=0}^{M} u^{em}(Σ_e^{(m)}(N₁)−Σ_e^{(m)}(N₂))`
with `Σ_e^{(m)}(N) = Σ_{j ≤ ⌊N/p^e⌋, p∤j} j^{−m} ∈ ℤ_(p)`, the weight-5 monomials of `w5_allp`
are multiplied out as polynomials in `u = p^{−1}`, and `H^{(5)}_n` is subtracted. Output: the
exact list `[K_0,…,K_{5M}]` of rationals with `v₅ = Σ_j K_j p^{−j}`.

**Checks at `L = 0`** (`work/p1f/t1.py`), `p = 5,7,11,13`, every `n < p`, every `(k,l)` —
**1 516 cells, 0 failures** on each of:

| check | result |
|---|---|
| `Σ_j K_j p^{−j} = v₅(n,k,l)` exactly | **0** mismatches |
| `K_j ∈ ℤ_(p)` for every `j` | **0** violations |
| `K_j = 0` for `j > J(π) = 1+min(s,2)` (`J = 0` at `π=(0,0,0,1)`) | **0** violations |
| `v_p(S_j) ≥ j`, `S_j := Σ_{k,l} T·K_j` — i.e. **`(V2)`,`(V3)` at `L=0`** | **0** failures; sharp (`v_p(S_3)=3` attained at most `n`) |

So `(V2)`,`(V3)` are confirmed at the base level in the exact graded form, not merely through
their consequence `v_p(P_n) ≥ 0`.

---

## 2. `(V2)` is vacuous and `(BASE)` is one identity `[PROVED]`

`work/p1f/kform.py` computes, symbolically in the level-0 letters and *per pole pattern*, the
forms `K_j` for `w5_allp`. Result (independent of `p`, `n`):

| pattern `(α,γ,κ,θ)` | `s` | `K_1` | `K_2` | `K_3` | `K_4,K_5` |
|---|---|---|---|---|---|
| `(0,0,0,1)` | 0 | **0** | **0** | **0** | 0 |
| `(0,0,1,1)` | 1 | 123 mon. | **0** | **0** | 0 |
| `(1,0,1,1)`, `(0,1,1,1)` | 2 | 167 | 60 | **17** | 0 |
| `(1,1,0,1)` | 2 | 166 | 62 | **14** | 0 |
| `(1,1,1,1)`, `(1,1,1,2)` | 3 | 169 | 62 | **18** | 0 |

> **Proposition 2.1 `[PROVED]`.** For `w₅ = w5_allp`, `K_2 = 0` identically on every pattern with
> `s ≤ 1` (this is *stronger* than the cap `J = 1+min(s,2)`, which permits `K_2 ≠ 0` at `s = 1`).
> Hence at `L = 0` every cell with `K_2 ≠ 0` has `v_pT = s ≥ 2`, so `(T/p)K_2 ≡ 0 (mod p)` cell by
> cell: **`(V2)` at `L = 0` is vacuous.**

*(At `L = 0`, `v_pT = α+γ+κ` **exactly**: by Kummer `v_pC(n+k,n) = α`, `v_pC(n+l,n) = γ`,
`v_pC(n,k) = v_pC(n,l) = 0`, `v_pC(n+k+l,n) = κ` — every argument is `< 2p` and `n,k,l < p`.)*

> **Proposition 2.2 `[PROVED]`.** For `p ≥ 5` and `n < p`, `(BASE)` is **equivalent** to
> ```
>   (V3)₀      Σ_{k,l=0}^{n}  ( T(n,k,l) / p² ) · K_3(n,k,l)  ≡  0   (mod p) ,
> ```
> a *full* double sum: `K_3 = 0` off the five patterns with `s ≥ 2`, and on those `v_pT = s ≥ 2`,
> so every summand is `p`-integral; the `s = 3` patterns contribute `0 (mod p)` automatically.

*Proof.* `v_p(W_n) ≥ 0 ⟺ v_p(P_n) ≥ 0` (`n < p` makes `H^{(5)}_nQ_n` integral).
`W_n = Σ_j p^{−j}S_j`. `S_0 ∈ ℤ_p`. `K_1 ≠ 0 ⟹ s ≥ 1 ⟹ v_pT ≥ 1`, so `v_p(S_1) ≥ 1`.
`K_2 ≠ 0 ⟹ s ≥ 2` (Prop. 2.1) `⟹ v_p(S_2) ≥ 2`. `K_4 = K_5 = 0`. Hence
`v_p(W_n) ≥ 0 ⟺ v_p(S_3) ≥ 3`, which is `(V3)₀`. ∎

**Geometry of `(V3)₀`.** Put `q := p−n` and `ñ := n−q = 2n−p` (poles exist iff `q ≤ n`). Then
`α = [k ≥ q]`, `γ = [l ≥ q]`, and the `s = 2` locus is exactly

```
 I   (α,γ,κ) = (0,1,1) :  k < q,  l ≥ q                     (κ = 1 and ε = 0 are automatic)
 II  (1,0,1)           :  k ≥ q,  l < q                      (the k↔l mirror of I)
 III (1,1,0)           :  k,l ≥ q,   p ≤ k+l < p+q           (ε = 1, κ = 0)
```
and `Σ_I = Σ_II`, so **`(V3)₀ ⟺ 2Σ_I + Σ_III ≡ 0 (mod p)`**.

**`[VERIFIED, 0 failures]`** (`work/p1f/t2.py`) the residue density `R(k,l) := p·T·v₅ mod p` is
supported **exactly** on `I ∪ II ∪ III` (patterns `(0,1,1,1),(1,0,1,1),(1,1,0,1)` and no others),
is `k↔l` symmetric, and `Σ_{k,l}R = 0` for **all 66 levels** `n < p`, `p ∈ {5,7,11,13,17,19}`.
Row sums are **not** `0` (`p=7, n=4`: rows `3,1,0,6,4`), confirming `PHASE2_INDUCTION` §6.1's
"the cancellation is global in `(b,c)`".

---

## 3. New: the weight-2 residue identities `[PROVED]` + `[VERIFIED]`

Lemma Phi (`PHASE2_ENDGAME` §R1.2) is the weight-1 member of a family; here is the weight-2 level.

**Set-up.** Fix `n ≥ 0`, `0 ≤ l ≤ n`; level-`n` letters `A_m(k)=H^{(m)}_{n+k}−H^{(m)}_k`,
`B_m(k)=H^{(m)}_{n−k}−H^{(m)}_k`, `C_m=H^{(m)}_{n+k+l}−H^{(m)}_{k+l}`, and
`Φ := A_1(k)+2B_1(k)+C_1`. Let
```
   G(x) := ∏_{i=1}^{n}(x+i) · ∏_{i=1}^{n}(x+l+i)  /  ∏_{j=0}^{n}(x−j)² ,
```
so `deg den − deg num = 2` and `Res_{x=k}G = (T(n,k,l)/K_l)·Φ(k,l)` with `K_l` independent of `k`
(that is Lemma Phi).

> **Lemma Φ₂ `[PROVED]`.** For every `n ≥ 0` and every `0 ≤ l ≤ n`:
> ```
> (P1)  Σ_{k=0}^{n} T(n,k,l)·[ Φ·A_1(k) − A_2(k) ]                 = 0 ,
> (P2)  Σ_{k=0}^{n} T(n,k,l)·[ Φ·C_1     − C_2   ]                 = 0 ,
> (P3)  Σ_{k=0}^{n} T(n,k,l)·[ Φ·B_1(k) − ½(Φ² − A_2(k) − C_2) ]   = 0 .
> ```
> `(P1)+2(P3)+(P2)` is the trivial `Φ²−Φ² = 0`, so exactly two of the three are independent; with
> Lemma Phi `(P0): Σ_k T·Φ = 0` they span a 3-dimensional space of exact `k`-row identities. The
> `k↔l` mirrors hold by symmetry of `T`.

*Proof.* **(P1)** For `1 ≤ i ≤ n` put `G_i := G(x)/(x+i)`. Since `(x+i)` divides the numerator of
`G`, `G_i` has **no** pole at `x = −i`; its only poles are the double poles at `x = 0,…,n`, and
`deg den − deg num = 3 ≥ 2`, so all residues sum to `0`. Writing `(x−k)²G = N/E` with
`(N/E)(k) = T(n,k,l)/K_l` and `(N/E)'(k) = (T/K_l)Φ(k,l)`,
`Res_{x=k}G_i = (T/K_l)[Φ/(k+i) − (k+i)^{−2}]`. Sum over `k`, then over `i = 1..n`, using
`Σ_i (k+i)^{−1} = A_1(k)`, `Σ_i (k+i)^{−2} = A_2(k)`.

**(P2)** identical with `G(x)/(x+l+i)` (again a numerator factor), using
`Σ_i (k+l+i)^{−1} = C_1`, `Σ_i (k+l+i)^{−2} = C_2`.

**(P3)** Take `G_j := G(x)/(x−j)`, `0 ≤ j ≤ n`; now `x=j` is a **triple** pole and
`deg den − deg num = 3`. For `k ≠ j`, `Res_{x=k}G_j = (T_k/K_l)[Φ(k)/(k−j) − (k−j)^{−2}]`. At
`x = j`, with `L := log(N/E)`, `Res = ½(N/E)''(j) = ½(T_j/K_l)[Φ(j)² + L''(j)]`,
```
 L''(j) = −A_2(j) − C_2 + 2( H^{(2)}_j + H^{(2)}_{n−j} ) .
```
Sum over `j = 0..n` and use `Σ_{j≠k}(k−j)^{−1} = −B_1(k)`,
`Σ_{j≠k}(k−j)^{−2} = H^{(2)}_k + H^{(2)}_{n−k}`. The two occurrences of the **non-alphabet**
symbol `H^{(2)}_k+H^{(2)}_{n−k}` cancel exactly (`−1` from the double poles, `+1` from the triple
pole), leaving (P3). ∎

**`[VERIFIED exact over ℚ, 0 failures]`** `work/p1f/t3.py`: all `0 ≤ l ≤ n ≤ 14`, **120/120**
`(n,l)` pairs, each of `(P0),(P1),(P2),(P3)` exactly `0`.

*Remark.* The cancellation of `H^{(2)}_j+H^{(2)}_{n−j}` in (P3) is why a *closed* weight-2
identity exists inside the `{A,B,C,N}` alphabet at all. The same construction with
`G(x)/((x+i)(x+i'))` produces the weight-3 level (the `(V2)` analogue). These answer the question
posed in `PHASE2_INDUCTION` §6.3 ("seek the weight-2/weight-3 residue identities … `Ψ_a` is the
first member of that family"): `Ψ_a` is weight 1, `(P1)–(P3)` weight 2. **But see §5: they cannot
prove `(BASE)`, because they are kernel identities.**

---

## 4. `(V3)₀` de-`p`-adicised `[PROVED]` + `[VERIFIED]`

Let `n < p`, `q = p−n`, `ñ = 2n−p`. Three elementary inputs:

* **Wilson** `(p−1)! ≡ −1`, hence `j!(p−1−j)! ≡ (−1)^{j+1} (mod p)`;
* the **reflections** `H_{p−1−j} ≡ H_j` and `H^{(2)}_{p−1−j} ≡ −H^{(2)}_j (mod p)` (`p ≥ 5`);
* the **carry binomial**: for `0 ≤ m < n < p`,
  ```
        C(p+m, n) / p  ≡  (−1)^{n−m+1} / ( n·C(n−1,m) )      (mod p).            (4.1)
  ```
  *Proof.* `(p+m)! = (p−1)!·p·∏_{i=1}^{m}(p+i) ≡ −p·m! (mod p²)`, then
  `1/(p+m−n)! ≡ (−1)^{n−m}(n−m−1)!` by Wilson-reflection, and `m!(n−m−1)!/n! = 1/(nC(n−1,m))`. ∎

Applying these slot by slot gives, with `l = q+λ` on I and `k = q+κ'`, `l = q+λ'`, `ρ = κ'+λ'−ñ`
on III:

```
 I  :  T/p² ≡ (−1)^k C(n+k,n) C(n,k)² C(n,ñ−λ)² / ( n² C(n−1,λ) C(n−1,k+λ) )
 III:  T/p² ≡ −(−1)^ρ C(n+ρ,n) C(n,ñ−κ')² C(n,ñ−λ')² / ( n² C(n−1,κ') C(n−1,λ') )
```
and every level-0 letter becomes an ordinary harmonic number of an argument `≤ n`:

| on I (`k < q`, `l = q+λ`) | on III (`k = q+κ'`, `l = q+λ'`, `ρ = κ'+λ'−ñ`) |
|---|---|
| `A_1(k) ≡ H_{q−1−k} − H_k` | `A_1(k) ≡ H_{κ'} − H_{q+κ'}` |
| `B_1(k) ≡ H_{q+k−1} − H_k` | `B_1(k) ≡ H_{ñ−κ'} − H_{q+κ'}` |
| `A_1(l) ≡ H_λ − H_{q+λ}` | `A_1(l) ≡ H_{λ'} − H_{q+λ'}` |
| `B_1(l) ≡ H_{ñ−λ} − H_{q+λ}` | `B_1(l) ≡ H_{ñ−λ'} − H_{q+λ'}` |
| `C_1 ≡ H_{k+λ} − H_{k+q+λ}` | `C_1 ≡ H_{q−1−ρ} − H_ρ` |
| `N_1 ≡ H_{q−1}` | `N_1 ≡ H_{q−1}` |

(weight-2 letters identically, with `H^{(2)}` and the sign flip of the `H^{(2)}` reflection).

> **Proposition 4.1 `[PROVED]`.** Define `F(n,q) ∈ ℚ` to be `2Σ_I + Σ_III` computed from the
> right-hand columns above — an explicit finite double sum of rational numbers in which **`p` does
> not occur**. Then for every prime `p ≥ 5` and every `n < p`,
> `(V3)₀ ⟺ F(n, p−n) ≡ 0 (mod p)`.

**`[VERIFIED, 0 failures]`** `work/p1f/t5.py`: `F(n,p−n) ≡ 0 (mod p)` for **all 24** pairs
`(n,q)` with `2 ≤ n ≤ 12`, `q = p−n`, `p = n+q` prime `≥ 5` and `p ∤ den F`. (The single failure
in the raw sweep is `p = 3`, correctly outside the hypothesis.)

**But `F(n,q) ≠ 0` as a rational number** for every tested `(n,q)` — the reduction consumes
Wilson and the reflections, so `(V3)₀` is *genuinely* a mod-`p` congruence, not the specialisation
of a rational identity. This is a sharp negative on the "make it a hypergeometric identity and
telescope it" plan: creative telescoping has nothing to telescope.

---

## 5. THE WALL `[PROVED]`

### 5.1 The obstruction functional factors through the value

Let `𝒟 ⊂ ℚ^{448}` be the space of weight-5 forms satisfying the 42 `(DEPTH)` conditions
(`dim 𝒟 = 406`; `rank(cond) = 42`, recomputed here over ℚ, `work/p1f/t6.py`). For `w ∈ 𝒟` put
`V_w(n) := Σ_{k,l}T(n,k,l)w(n,k,l)`. `(DEPTH)` gives the cell-wise bound `v_p(V_w(n)) ≥ −1`
(`n < p`), and the *entire* content of the cancellation is the linear functional

```
        θ_{p,n} : 𝒟 → 𝔽_p ,        θ_{p,n}(w) := ( p · V_w(n) )  mod p .
```

> **Theorem 5.1 `[PROVED]`.** `θ_{p,n}(w)` depends on `w` only through the single rational number
> `V_w(n)`. Consequently:
> 1. every exact identity `Σ_{k,l}T·M = 0` (Lemma Phi, `(P1)–(P3)`, all their weight-3/4/5
>    products — the whole "Lemma Phi species") lies in `ker(V)` and therefore satisfies
>    `θ_{p,n}(M) = 0` **trivially**, and adding any such `M` to `w₅` changes neither `V` nor `θ`;
> 2. `(V3)₀` for `w₅` is *literally* the assertion `v_p(P_n) ≥ 0` and carries no information
>    beyond it.

*Proof.* Immediate from the definition; `V` is linear and `Σ T M = 0` means `M ∈ ker V`. ∎

### 5.2 …and it is not identically zero on `𝒟`

> **`[VERIFIED, work/p1f/t6.py]`** Three independent random `w ∈ 𝒟` (≈ 420 nonzero coefficients
> each, drawn by rref-completion of the ℚ condition system) give, at `p = 5,7,11,13`,
> ```
>     min_{n<p} v_p( Σ_{k,l} T(n,k,l) w(n,k,l) )  =  −1        (all 12 (trial,prime) pairs)
> ```
> with cell-wise minimum also `−1`. So `θ_{p,n} ≢ 0` on `𝒟`.

**Consequence (the wall).** The `(DEPTH)` calculus *plus arbitrarily much summand-side identity
work* cannot prove `(BASE)`: the property "`v_p(V_w(n)) ≥ 0` for all `p ≥ 5`, `n < p`" is a
`p`-**dependent** linear condition on `w` for each `(p,n)`, is false on a generic point of `𝒟`,
and can only be enforced by conditions that pin the value sequence `V_w` — i.e. by the fitting
system itself. This is the structural explanation of `PHASE2_INDUCTION` §6.1's hard negative
(`(DEPTH⁺)`, `(DEPTH⁺⁺)` inconsistent): those systems were trying to buy, with `p`-independent
linear conditions, something that is not `p`-independent-linear.

### 5.3 Route R3 (reflection) refuted concretely

The attained cell `(n,k,l) = ((p+1)/2, 0, (p−1)/2)` is `(k,λ) = (0,0)` in the `I`-coordinates of
§4, i.e. the *corner* of region I, not a reflection centre. In `(u,v)`-coordinates
(`u = λ`, `v = k+λ` on I; `u = ñ−λ'`, `v = κ'` on III) both regions are width-`q` bands
`0 ≤ v−u ≤ q−1`, and III `=` I `∩ {v ≤ ñ}` — so the index sets **are** related by
`λ' ↦ ñ−λ'`, but the summands are not: the two `T/p²` weights carry
`C(n,v−u)²C(n,ñ−u)²/C(n−1,u)` and `−C(n,ñ−v)²C(n,u)²/C(n−1,ñ−u)` respectively, which no
substitution matches. Numerically:

* `|I ∪ II| ≠ |III|` (`p=7,n=4`: `12` vs `3`; `p=7,n=5`: `16` vs `5`);
* the residue multisets differ (`p=7,n=4`: `{1,2,3,5,1,6}×2` vs `{1,1,4}`).

**No involution pairs the deficit cells.** (And by Theorem 5.1 even a successful pairing would be
a kernel identity and could not have proved `(BASE)`.)

### 5.4 A by-product: the region functionals are massively degenerate

Writing `Λ(ρ,m) := Σ_{cells of ρ}(T/p²)·m (mod p)` for the 27 weight-2 monomials `m` in the
level-0 letters and `ρ ∈ {I,II,III}` (81 coordinates), the 99 vectors `V(199,n)`, `n = 100..198`,
span a space of **rank 21 only** (`work/p1f/t4.py`); the target coefficient vector (the `K_3`
triple) is one of the 60 independent annihilators, and

> **`[VERIFIED, 0 failures]`** `Σ_ρ Σ_m c^ρ_m Λ(ρ,m) = 0` for **all 99** values of `n` at
> `p = 199`, and all 15 at `p = 31`.

This is by far the strongest single verification of `(V3)₀` in the program (`n` up to 198, one
prime, exact `𝔽_p` arithmetic). The degeneracy is explained by §4: mod `p` all level-0 letters
collapse onto ordinary `H_j`, `H^{(2)}_j` with `j ≤ n`.

---

## 6. The graded `(V2)/(V3)` at `L = 1` `[VERIFIED]`

`PHASE2_INDUCTION` §4.2–4.3 already **proves** the induction step (given `(DEPTH-gen)`, Lemma
F-gen, and `(GAP-DESC)` for the off-regime descent at `a ≥ p`), so `(V2)/(V3)` at `L ≥ 1` are
consequences of `(BASE)` + `(GAP-DESC)`, not separate obligations. Verified
independently in the graded form (`work/p1f/t7.py`), `p = 5`, `n = 5..14` (`L = 1`, 700 cells):

| check | result |
|---|---|
| `K_j = 0` for `j > 5L+J(π)` | **0** violations |
| `K_j ∈ ℤ_(p)` | **0** violations |
| `v_p(S_j) ≥ j − 5L` for every `j` (`= (V2)`,`(V3)` at `L=1`) | **0** failures |

---

## 7. The routes that remain, costed

### 7.1 `(V-a)` A cell-wise-integral representation — *the Apéry mechanism* `[RECOMMENDED]`

Apéry's `ζ(3)` base case is not a cancellation at all. With the **classical** weight
`c(n,k) = H^{(3)}_n + Σ_{m=1}^{k}(−1)^{m−1}/(2m³C(n,m)C(n+m,m))` on `T_A = C(n,k)²C(n+k,k)²`:

> **`[VERIFIED, work/p1f]`** for `p = 5,7,11,13,17` and every `n < p`, every `k`:
> `min v_p(T_A·c) = 0` **exactly**, with `max depth(c) = 1` — the single pole
> (`p | C(n+m,m)`, i.e. `n+m ≥ p`) is always paid for by `v_pC(n+k,k)² ≥ 2`.

So for `ζ(3)` the base case is cell-wise, because the weight has **binomial-reciprocal (nested,
depth-2) letters**, not harmonic monomials. `PHASE2_INDUCTION` §6.1's negative is a statement
about the **448 harmonic-monomial basis only** and does *not* exclude a weight-5 `ω` with
Apéry-type letters and `depth(ω) ≤ v_pT` cell-wise. That is precisely the object to look for, and
it would make `(BASE)` immediate and representative-free.

**Exactly how much is needed, and why the Apéry letters supply it.** Compare, at `L = 0`, the
depth `w5_allp` achieves with the depth needed for cell-wise integrality (`d₅ ≤ v_pT = s`):

| `s` | have (`w5_allp`) | need | shortfall |
|---|---|---|---|
| 0 | 0 | 0 | — |
| 1 | 1 (`K_2 = 0`, Prop. 2.1 — better than the cap) | 1 | — |
| **2** | **3** | **2** | **1** |
| 3 | 3 | 3 | — |

So the *only* thing missing is: **kill `K_3` on the three `s = 2` patterns** — precisely the
`(DEPTH⁺⁺)` localisation that `PHASE2_INDUCTION` §6.1 proved impossible inside the harmonic
monomial basis. The mechanism that supplies it:

> **Proposition 7.2 `[VERIFIED, 0 exceptions]`.** Put
> `R^{(a)}(n,k) := Σ_{m=1}^{k} (−1)^{m−1} / ( m^a C(n,m) C(n+m,m) )`, a weight-`a`
> Apéry-type letter. For every `p ≥ 5`, every `n < p`, every `k ≤ n` and every `a = 1,…,5`:
> `R^{(a)}` has **pole order at most 1**, and its pole indicator is **exactly `α = [n+k ≥ p]`** —
> the same indicator as `A_a(k)`, but with pole order `1` instead of `a`.
> `[VERIFIED p ≤ 19, all n < p, all k, a = 1..5]`

That is the whole point: a harmonic monomial of weight 3 in the polar letters costs `u³`, an
Apéry letter of weight 3 costs `u¹`. Replacing the `u³`-carrying part of `w₅` on the `s = 2`
patterns by Apéry letters of the same weight is exactly the one order that is missing, and it is
*outside* the space in which the impossibility was proved.

*Concretely:* extend the fitting alphabet by `R^{(a)}(n,k)`, `R^{(a)}(n,l)` and their
`(k+l)`-analogue (this is exactly the "nested (depth-2) letters — the `ζ(5)+2ζ(2)ζ(3)` period"
that `PROOF_LB5_CAMPAIGN` §3.3 already identified as the missing ingredient), refit `P_n`, and
impose `depth ≤ v_pT` cell-wise, i.e. re-run `solve_strong.py vt2` in the enlarged basis and
check whether it becomes **consistent**. That single linear-algebra run is the decisive
experiment, and it is cheap. Cost: one fitting campaign of the size of `PHASE2_FINAL` §2.

### 7.2 `(V-b)` The certified order-3 recurrence `[COSTED, partial]`

`L_BZ`: `c_0(n)Y_n + c_1(n)Y_{n+1} + c_2(n)Y_{n+2} + c_3(n)Y_{n+3} = 0`, with
`c_3(n) = 2(n+3)^5(2n+5)a_0(n)`, `c_0(n) = (n+1)^5(n+2)a_0(n+1)`,
`a_0(n) = 41218n³+198849n²+320790n+173057`. `P_0 = 0`, `P_1 = 87/4`, `P_2 = 1190161/384` are
`p`-integral for `p ≥ 5`. Forward induction gives `v_p(P_{n+3}) ≥ 0` at every step `n ≤ p−4`
with `v_p(c_3(n)) = 0`, and `1 ≤ n+3 ≤ p−1` kills the `(n+3)^5` factor. Hence:

> **Proposition 7.1 `[PROVED]`.** `(BASE)` for a given `p ≥ 5` follows from
> ```
>    v_p( c_0(n)P_n + c_1(n)P_{n+1} + c_2(n)P_{n+2} )  ≥  v_p(c_3(n))
> ```
> at the finitely many `0 ≤ n ≤ p−4` with `p | (2n+5)·a_0(n)` — i.e. at `n = (p−5)/2` and at the
> roots of `a_0` mod `p` in range.

**`[VERIFIED]`** the census over all primes `5 ≤ p ≤ 199`: **1–4 exceptional steps per prime**
(exactly one from `2n+5`, plus 0–3 from `a_0`; `a_0` has roots in range for 23 of the 44 primes).
At every exceptional step the required inequality holds with `v_p(num) = v_p(c_3) = 1` typically
— and *fails* for `P̂` (`v_p(num_{P̂}) = 0 < 1` at most of them), which is exactly why
`v_p(P̂_a) = −1` occurs. So the inequality is **not** automatic from the recurrence: it is a real
property of the `P`-row, and `Q` shares it (`Q_n ∈ ℤ`).

**What this buys.** The `n = (p−5)/2` step produces `P_{(p+1)/2}` — *precisely* the level at which
`PHASE2_INDUCTION` §6.1 records the attained deficit cell `(n,k,l) = ((p+1)/2, 0, (p−1)/2)`. The
two localisations agree, which is a strong consistency check and pinpoints the single congruence
that has to be proved:
```
   (REC-★)   c_0(n₀)P_{n₀} + c_1(n₀)P_{n₀+1} + c_2(n₀)P_{n₀+2} ≡ 0 (mod p),   n₀ = (p−5)/2 .
```
plus the analogous statement at the `a_0`-roots — for which the standard route is
**desingularisation** of `L_BZ` (`a_0` sits in `c_3(n)` *and* in `c_0(n)` as `a_0(n+1)`, the
signature of an apparent singularity; a left multiple `R·L_BZ` with polynomial content `a_0`
would remove them and leave only `(REC-★)`).

### 7.3 What is definitively closed off

| route | verdict |
|---|---|
| **R1** Lemma-Phi species / residue identities on the summand | **WALLED [PROVED]** — every such identity is in `ker V` (Thm 5.1); it cannot move `θ`. The identities themselves are now proved (§3) and are useful elsewhere (they are exactly the kernel elements the `w₅` family is translated by), but they cannot prove `(BASE)`. |
| **R2** certificate assembly (port of A1-MID) | **WALLED as stated** — the Q/Lucas row and the `Ψ_a` supercongruence are facts about `Q`, and `Q_n ∈ ℤ` makes them `θ`-blind; a certificate assembly can only re-derive kernel identities unless it imports a `P`-row input, which is §7.1/§7.2. |
| **R3** reflection / dihedral involution | **REFUTED [VERIFIED]** — §5.3: unequal region sizes, unequal residue multisets, and the two `T/p²` weights are not related by any substitution. |
| improve the `w₅` representative inside the 448 basis | already `[PROVED]` impossible (`PHASE2_INDUCTION` §6.1); §5 explains *why*. |
| turn `(V3)₀` into a rational identity and telescope | **REFUTED [VERIFIED]** — §4: `F(n,q) ≠ 0` over ℚ; the statement is irreducibly mod `p`. |

---

## 8. Status of `(V2)/(V3)` after P1f

```
(V2)  Σ (T/p)·K_{5L+2} ≡ 0            [PROVED, VACUOUS at L=0 for w5_allp]  (§2, Prop 2.1)
                                       [consequence of the proved induction step for L>=1]
(V3)  Σ (T/p²)·K_{5L+3} ≡ 0           [OPEN at L=0 — this IS (BASE)]        (§2, Prop 2.2)
      · equivalent explicit form  2Σ_I + Σ_III ≡ 0                          (§2)
      · fully de-p-adicised form  F(n,p−n) ≡ 0 (mod p), F explicit, p-free  (§4)
      · VERIFIED: 66 levels p<=19 (t2); 99 levels at p=199 + 15 at p=31 (t4);
        1516 cells graded p<=13 (t1); L=1 at p=5, n<=14 (t7)
      · PROVED unreachable from the w5/depth side                           (§5, Thm 5.1)
      · remaining routes: (V-a) Apéry-type cell-wise weight  [RECOMMENDED]  (§7.1)
                          (V-b) recurrence + desingularisation, 1 congruence (§7.2)
```

`work/PHASE2_THEOREM.md` therefore stays at **v2**: §6.3 does **not** flip to `[PROVED-here]`.
What it gains is that the residual object is now one identity (not two), stated three equivalent
ways, with the two dead routes proved dead and the two live routes costed.

**Decomposition-certificate node (read-only report, nothing touched).** `work/PHASE2_CERTS.md`
(P1e, 2026-07-25) and `work/lb5/CERTS_RESUME.md`:

* `[CERTIFIED] — new`: the **Q-row single certificate** `L_BZ·T = Δ_k(ρT) + Δ_l(σT)` with explicit
  rational `ρ,σ` (`work/lb5/Qrow_rhosigma.m`), checked to exactly `0` twice, the second time in a
  kernel that never loaded RISC.
* `[PROVED negative]`: the "any representative suffices" claim is **refuted** — the 448 basis
  monomials are pointwise independent, so every kernel element is itself a non-trivial summation
  identity. The representative that must be certified is `w5_allp`. *(This is the same fact that
  §5 above turns into the wall: kernel elements are exactly the value-preserving identities.)*
* **(a) Theorem B** (`P̂_n = Σ T·ŵ₃`): **NOT closed** — one step left (an operator annihilating
  `Σ E(v)`, now a rank-1 problem); `certU.wl` was running it.
* **(b) (T1-top)** (`P_n = Σ T·w5_allp`): **NOT closed**; evidence strengthened — matches `P_n`
  for all `n ≤ 360` and satisfies `L_BZ` at 748 consecutive `n` mod two primes, minimal recurrence
  exactly `(3,9)`.

So both residual nodes of `PHASE2_THEOREM` v2 §B remain open, and P1f does not change their state.

---

## 9. Reproduction

All scripts are exact-arithmetic Python (`fractions.Fraction` / `int` / `𝔽_p`); none touches a
Wolfram kernel. All are in **`work/p1f/`** (new directory; nothing outside it was modified).

| script | what it does | output |
|---|---|---|
| `kgrade.py` | exact `u`-graded expansion `v₅ = Σ K_j p^{−j}` at any digit level | module |
| `kform.py` | symbolic `K_j` per pole pattern, as forms in the level-0 letters | table of §2 |
| `t1.py` | `L=0` graded checks (reconstruction, integrality, caps, `(V2)`,`(V3)`) | 1 516 cells, **0** failures (`t1_1113.out`) |
| `t2.py` | residue density `R = p·T·v₅ mod p`; support, symmetry, `ΣR = 0` | 66 levels `p ≤ 19`, **0** failures |
| `t3.py` | the exact weight-2 identities `(P0)–(P3)` over ℚ | 120/120 `(n,l)`, **0** failures |
| `t4.py` | region functionals `Λ(ρ,m)`, target value, rank/nullity | `p=199`: 99/99 zero, **rank 21** (`t4_199.out`) |
| `t5.py` | the `p`-free reduction `F(n,q)`; `F(n,p−n) ≡ 0 (mod p)` | 24/24 primes; `F ≠ 0` over ℚ |
| `t6.py` | **the wall**: random `(DEPTH)`-conditioned `w`, `min_n v_p(Σ T w)` | `−1` in all 12 (trial, prime) pairs |
| `t7.py` | graded `(V2)/(V3)` at `L = 1` | `p=5`, `n ≤ 14`, **0** failures (`t7_p5.out`) |
| `t8.py` | Apéry `ζ(3)` control (cell-wise weight) + pole order of `R^{(a)}` | `min v_p(T_A c) = 0`; `R^{(a)}` pole order `1` for `a = 1..5`, `p ≤ 19` |

**Sweep summary (all exact, 0 failures):** 1 516 graded cells `p ≤ 13` (`t1`) · 66 levels
`p ≤ 19` residue-density (`t2`) · 120 `(n,l)` weight-2 identities over ℚ (`t3`) · 99 levels at
`p = 199` + 15 at `p = 31` (`t4`) · 24 de-`p`-adicised prime cases (`t5`) · 12 wall trials (`t6`)
· 10 levels at `L = 1` (`t7`) · 5 letter weights × 6 primes (`t8`).
