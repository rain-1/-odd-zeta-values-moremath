# APERY_DEFECT — the first-order defect and the weight, on the ζ(3) Apéry case

**Author:** mathematician-agent (River's odd-zeta program), 2026-07-26
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, code in `work/apdef/`
**Labels:** `[PROVED]` · `[VERIFIED range]` · `[EXCLUDED with bounds]`
All arithmetic exact (`fractions.Fraction` / Python ints). No floating point anywhere.

---

## 0. HEADLINE

The ζ(3) defect is **rank 1 at first order AND rank 1 at second order** — where the
Brown–Zudilin rank-3 family is rank 1 then rank **2**. That is the difference, and it
has a mechanism: an exact identity

> **`Σ_{k=0}^n C(n,k)²C(n+k,k)² ( H_{n+k} + H_{n−k} − 2H_k ) = 0`**  `[PROVED, §3]`

kills the only channel that could have made the first-order defect rank 2. At second
order the two extra channels also die, but only **mod p** and only via a cancellation
against the borrow region — verified, not proved (§9). Explicitly

> **`E_p(a,r) := (p³b_{ap+r} − b_a a_r)/p ≡ 2·a·b_a·U_r  (mod p)`**
> **`e_p(a,r) := (a_{ap+r} − a_a a_r)/p ≡ 2·a·a_a·U_r  (mod p)`**
> **`U_r = Σ_s A(r,s)(H_{r+s} − H_{r−s})`** — the same functional for both rows.

`U_r` is `½ ∂a_n/∂n` in the Γ-form: the exact ζ(3) analogue of the Brown–Zudilin
Lemma-Φ functional `Ψ_r`. The two-level law closes, and closes **scalar to depth 3**:

> **`( a_n , p³b_n ) ≡ ( a_a , b_a ) · u(a,r) (mod p³)`,  `n = ap+r`, `a,r < p`**
> **`u(a,r) = a_r + 2p·a·U_r + p²a²·X_p(r) = [ Σ_{s=0}^{p−1} A_Γ(r+ε, s) ]_{ε = pa}`**
> truncated at `ε²`; floor **exactly 3**, all 13 primes `5 ≤ p ≤ 47`.

and the cross term appears at exactly `p³ = p^w`, where it is the low digit's own
weight-3 row:

> **`(a_n, p³b_n) ≡ (a_a, b_a) · [[u(a,r), p³b_r],[0, u(a,r)]]`**

with the `p³` defect splitting as (scalar, rank 2) ⊕ (cross, rank 1); subtracting
`p³a_a b_r` drops the b-row defect from rank 3 to rank 2 and makes its r-side row
space coincide with the a-row's, at every prime. `[VERIFIED, §5]`

**T2 is solved (§7).** `b_n` is a **primitive**, ζ-free third-order coefficient of one
deformed family — with `Π_j(t) = ∏_{i≤t}(1+jε/i)`,

> **`b_n = ½ [ε³] Σ_k A(n,k) ∏_{j=1}^{3} Π_j(n)^{u_j} Π_j(k)^{v_j}`,
>  `u = (6,−6,2)`, `v = (−3,3,−1)`**  `[PROVED; VERIFIED exact, n ≤ 20]`

`[ε¹] = [ε²] = 0` **termwise**, so nothing has to cancel. The symmetry that does it is a
**third finite difference in ε** (`e_1 = e_2 = 0`, `e_3 = 12 : −6 = 2 : −1`), and three
shift points is minimal. Deforming only `A`'s own Γ's provably cannot work
(`b_n ∉ span_ℚ{S_X,S_Y,S_Z}`), and if the Pochhammers are left un-normalised the
coefficient becomes `2(b_n − ζ(3)a_n)` — twice the **Apéry remainder** — with the ζ(3)
coefficient forced to `−1`: the ζ(3) the Γ-series cannot avoid *is* the Apéry limit, and
removing it costs exactly one Γ-constant `= 1 + 2ζ(3)ε³ + O(ε⁴)`.

---

## 1. Instrument validation (`work/apdef/validate.py`)

Before any new computation, the four recorded facts were re-measured from scratch
(ladders from the recurrence `m³u_m = P(m−1)u_{m−1} − (m−1)³u_{m−2}`,
`P(m−1) = 34m³−51m²+27m−5`; `a: 1,5` and `b: 0,6`):

| check | result |
|---|---|
| ladders `=` direct sums `Σ_k A(n,k)` / `Σ_k A(n,k)(2H³_n−H³_k)`, `n ≤ 40` | 0 mismatches |
| Theorem 2 `p³b_{ap+r} ≡ b_a a_r (mod p)`, `p = 5…23`, all `a,r < p` | 0 failures, floor **exactly 1** |
| master form `v_p(p³b_n a_q − b_q a_n) ≥ 3`, `q = ⌊n/p⌋` | floor **exactly 3**, all p |
| `a_{ap+r} − a_a a_r` | floor **exactly 1**, all p |

`b_0..b_5 = 0, 6, 351/4, 62531/36, 11424695/288, 35441662103/36000` (so `b_n ∉ ℤ`;
`v_p(b_n) ≥ −3` for `n < p²`, which is what `p³` normalises).

---

## 2. T1(i) — the ranks `[VERIFIED, 9 primes]`

`work/apdef/t1_rank.py`. Grid `a = 1…p−1` (the `a = 0` row is identically 0 because
`b_0 = 0`), `r = 0…p−1`; rank over `F_p`, no model assumed.

| p | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 |
|---|---|---|---|---|---|---|---|---|---|
| `rank E` (b-row) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| `rank e` (a-row) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

and re-confirmed at `p = 37, 41, 43, 47` in `t1_extend.py` — **13 primes total**.

**Rank exactly 1 at every prime, both rows, and with the *same* r-side vector.**
The r-side is antisymmetric under `r ↦ p−1−r` (so it vanishes at `r = 0`, `r = p−1`
and at the middle `r = (p−1)/2`); the a-side vanishes exactly where `b_a ≡ 0`.

---

## 3. T1(ii) — the factorisation, and the identity behind it

### 3.1 The expansion `[PROVED, p ≥ 5]`

For `0 ≤ s ≤ r < p`, `0 ≤ c ≤ a < p`, `r+s < p`, Wolstenholme (`H_{p−1} ≡ 0 mod p²`,
`H^{(2)}_{p−1} ≡ 0 mod p`) makes the `(ap)!/(p^a a!) ≡ ((p−1)!)^a` factors cancel and

```
  C(ap+r, cp+s)      ≡ C(a,c)C(r,s)     (1 + p[ a H_r − c H_s − (a−c)H_{r−s} ])   mod p²
  C((a+c)p+(r+s),cp+s) ≡ C(a+c,c)C(r+s,s)(1 + p[ (a+c)H_{r+s} − c H_s − a H_r ])  mod p²
```

so with `A = (C(n,k)C(n+k,k))²` the two `a H_r` terms cancel and

> **`A(ap+r, cp+s) ≡ A(a,c) A(r,s) ( 1 + 2p[ a·u(r,s) + c·v(r,s) ] ) (mod p²)`**
> **`u(r,s) = H_{r+s} − H_{r−s} = ½ ∂_n log A`,  `v(r,s) = H_{r+s} + H_{r−s} − 2H_s = ½ ∂_k log A`**

Outside that region (`s > r`, `c > a`, or the carry `r+s ≥ p`) the relevant binomial is
`≡ 0 mod p`, and because `A` is a **square** both `A(ap+r,cp+s)` and `A(r,s)` are
`≡ 0 mod p²`; so those regions do not contribute at first order **at all**, and the
carry correction to `b_a a_r` cancels identically mod `p²`.

Also `H^{(3)}_{ap+r} = p^{-3}H^{(3)}_a + G_{ap+r}` with `G_m = Σ_{j≤m, p∤j} j^{-3}`
`p`-integral, so `p³b_n = Σ_{c,s}A(n,cp+s)(2H³_a − H³_c) + p³·(p-integral)`: **the
weight contributes nothing below order `p³`.** Hence

> `E(a,r) ≡ 2[ a·b_a·U_r + b'_a·V_r ]`,  `e(a,r) ≡ 2[ a·a_a·U_r + a'_a·V_r ]` (mod p)
> `U_r = Σ_s A(r,s)u(r,s)`, `V_r = Σ_s A(r,s)v(r,s)`,
> `a'_a = Σ_c cA(a,c)`, `b'_a = Σ_c cA(a,c)(2H³_a − H³_c)`

a **rank ≤ 2** form. Measured rank is 1, so one channel degenerates. It does:

### 3.2 The identity `V_n = 0` `[PROVED]`

> **`V_n := Σ_{k=0}^{n} C(n,k)²C(n+k,k)² ( H_{n+k} + H_{n−k} − 2H_k ) = 0`  for all `n ≥ 0`.**

`[VERIFIED exact over ℚ, n = 0…60, all zero]` (`t1_ident.py`), and **proved**:

`V_n = ½ Σ_k ∂_k A_Γ(n,k)` where `A_Γ(n,z) = [Γ(n+z+1)/(Γ(z+1)²Γ(n−z+1))]²`.
Reflection `1/Γ(n−z+1) = Γ(z−n)sin(π(z−n))/π` gives
`A_Γ(n,z) = (sin²πz/π²)·g(z)`, `g(z) = Γ(n+z+1)²Γ(z−n)²/Γ(z+1)^4`.
At an integer `z = k`, writing `g = c₂(z−k)^{-2} + c₁(z−k)^{-1} + …`, the two poles cancel:
`∂_z A_Γ|_{z=k} = 2c₂ − 2c₂` over `(z−k)` `+ (2c₁ − c₁) = c₁ = Res_{z=k} g`.
`g`'s only poles are the double poles at `z = 0,1,…,n` (at `z = −1,…,−n` the double pole
of `Γ(z−n)²` is over-cancelled by the 4th-order zero of `Γ(z+1)^{-4}`; for `z ≤ −n−1`
the orders are `2+2−4 = 0`), and `g(z) = O(z^{-2})` at infinity because
`[Γ(z+n+1)/Γ(z+1)]²[Γ(z−n)/Γ(z+1)]² ∼ z^{2n}·z^{−2n−2}`. Sum of all residues of a
meromorphic `O(z^{-2})` function with finitely many poles is 0. ∎

*(Sanity: `n=1`: `F(0) = 1·2(H_1+H_1) = 4`, `F(1) = 4·2(H_2 − 2H_1) = −4`.)*

### 3.3 The first-order law `[VERIFIED, 9 primes, 0 failures]`

`t1_ident.py`, `p = 5,7,11,13,17,19,23,29,31`, all `a ∈ [1,p)`, `r ∈ [0,p)`:

> **`(a_{ap+r} − a_a a_r)/p ≡ 2·a·a_a·U_r`  and  `(p³b_{ap+r} − b_a a_r)/p ≡ 2·a·b_a·U_r` (mod p)**

`U_0..U_8 = 0, 6, 105, 2219, 104825/2, 13276637/10, 70543291/2, 67890874657/70,
766399019471/28`. `U_r = ½ da_n/dn` in the Γ-form — the ζ(3) analogue of the
Brown–Zudilin `Ψ_r`, with the same origin (`∂_n log` of the summand).

**Identification of the shapes asked for.** `E ≡ a·b_a·Ψ_p(r)` holds with
`Ψ_p(r) = 2U_r mod p` — the candidate shape is **confirmed**, with `Ψ` a
*p-independent rational sequence*. `E ≡ a_a·Φ(a,r) + b_a·Ψ(r)` is **excluded** as a
description of the truth: the `a_a` channel would need `Φ` carrying the whole `a`
dependence, whereas the measured a-side factor is exactly `a·b_a` (the b-row) and
`a·a_a` (the a-row) — the two rows share `Ψ` and differ only by their own value at
level `a`. `Ψ` is **not** `a_r`, `b_r`, or divisible by `a_r`: at `p = 5`, `U_r ≢ 0`
exactly where `a_r ≡ 0`.

---

## 4. The two-level law, mod `p²` and mod `p³`

### 4.1 mod `p²` `[PROVED (given §3.2) and VERIFIED, 9 primes]`

> **`( a_n , p³b_n ) ≡ ( a_a , b_a )·( a_r + 2p·a·U_r ) (mod p²)`,  `n = ap+r`, `a,r<p`**

0 failures at `p = 5…31`; floor **exactly 2** for both rows (`t1_ident.py`).
This is the ζ(3) instance of the Brown–Zudilin split form
`(Q_n, p³Ŵ_n, p⁵W_n) ≡ (Q_a, Ŵ_a, W_a)·(Q_r + p·a·Ψ_r)`, with `Ψ_r → 2U_r`.

### 4.2 T1(iii) — the second-order defect is rank **1**, not 2 `[VERIFIED, 9 primes]`

`t1_order2.py`, `D2 = (X_n − X_a(a_r + 2paU_r))/p² mod p`:

| p | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 |
|---|---|---|---|---|---|---|---|---|---|
| `rank D2` a-row | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| `rank D2` b-row | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

and the two rows have the **same** r-side row space at every prime; re-confirmed at
`p = 37,41,43,47` (`t1_extend.py`), **13 primes total**.
**This is the divergence from the benchmark** (`ZETA5_CLOSEDFORM` §5.3: rank exactly
**2** at second order, all six primes, all three BZ rows). The comparison is
apples-to-apples: same convention, defect of the same first-corrected law, same
`/p²` normalisation.

The correction is moreover **scalar**: `f_b(a)·a_a ≡ f_a(a)·b_a` with ratio exactly
`1` at all nine primes, and the a-side factor is `a²` exactly:
`f(a) = c_p·a²·a_a` (tested against `a^j`, `j = 0..3`; only `j = 2` matches, at every
prime) — `t1_order2b.py`.

### 4.3 The scalar, in closed form `[VERIFIED, 7 primes]`

The `a^j`-at-order-`p^j` pattern says the scalar is a Taylor series in `pa`. It is —
in the Γ-deformation with the **full digit range**. With
`A_Γ(n,k) = [Γ(n+k+1)/(Γ(k+1)²Γ(n−k+1))]²`, `Π(t) = ∏_{i≤t}(1+ε/i)`,
`Π̄(t) = ∏_{i≤t}(1−ε/i)`, the `Γ(1+ε)` factors cancel and everything is rational:

```
  s ≤ r  :  A_Γ(r+ε, s)   = A(r,s) Π(r+s)² / Π(r−s)²
  s = r+m:  A_Γ(r+ε, r+m) = ε² · ( (2r+m)!(m−1)!/((r+m)!)² )² · Π(2r+m)² Π̄(m−1)²
```

The terms with digit `s > r` are present and are **exactly order `ε²`** — they are the
"borrow" region of the p-adic expansion. Define
`Adig(p, r; ε) := Σ_{s=0}^{p−1} A_Γ(r+ε, s)` (**full digit range**, the cut-off is the
only p-dependence). Then `[ε⁰] = a_r`, `[ε¹] = 2U_r`, and

> **`X_p(r) ≡ [ε²] Adig(p,r)  (mod p)` — MATCHES for every `r`, `p = 5…23`**

so the law is

> **`( a_n , p³b_n ) ≡ ( a_a , b_a ) · Adig(p, r; pa)|_{trunc ε²} (mod p³)`, floor exactly 3**

`t1_dscalar.py`, `p = 5,7,11,13,17,19,23`, both rows: floors `1, 2, 3` for truncation
orders `m = 0, 1, 2`, and **`3` for every `m ≥ 3`** — the scalar picture saturates at
depth 3. (The same test with the *restricted* deformation `Σ_{s≤r}` — i.e. without the
borrow terms — saturates at depth **2**: `t1_scalar.py`. The borrow region is exactly
the second-order correction.)

---

## 5. Order `p³`: the cross term, at exactly `p^w` `[VERIFIED, 7 primes]`

`t1_order3.py`, `D3 = (X_n − X_a·u₃)/p³ mod p` with `u₃` the depth-3 scalar of §4.3:

| p | rank `D3` a-row | rank `D3` b-row | rank `D3b − a_a b_r` | same r-space as a-row? |
|---|---|---|---|---|
| all 13 primes `5 ≤ p ≤ 47` | **2** | **3** | **2** | **YES**, all p |

**Derivation of the cross term.** `H^{(3)}_m = p^{-3}H^{(3)}_{⌊m/p⌋} + G_m`, and mod `p`
a full block `Σ_{t=1}^{p−1}t^{-3} ≡ 0` (p ≥ 5), so `G_{ap+r} ≡ H^{(3)}_r` and
`G_{cp+s} ≡ H^{(3)}_s`. Therefore the neglected piece of `p³b_n` is
`p³ Σ_k A(n,k)(2G_n − G_k) ≡ p³ · a_a · b_r (mod p⁴)`.
So the low digit acts by the matrix

> **`(a_n, p³b_n) ≡ (a_a, b_a) · [[ u(a,r) , p³ b_r ],[ 0 , u(a,r) ]]`**

The cross entry is the low digit's **own** weight-3 row, scaled by `p³ = p^w`.
**The weight is the order at which the cross term switches on** — the ζ(3) instance of
`ZETA5_CLOSEDFORM` §5.4 ("a cross term can only appear at order `p³`"), here derived
rather than bounded, and with the entry named.

Rank profile, ζ(3) against the benchmark:

| order | ζ(3), a-row | ζ(3), b-row | BZ ζ(5) (all three rows) |
|---|---|---|---|
| `p` | 1 | 1 | 1 |
| `p²` | **1** | **1** | **2** |
| `p³` | 2 | 3 = 2 (scalar) ⊕ 1 (cross) | — |

---

## 6. The two-digit iteration — exactly what is lost `[VERIFIED, p = 5,7,11,13]`

`t1_twodigit.py`. `n = bp² + sp + r`, `N = ⌊n/p⌋ = bp+s`.

| statement | floor, `N < p` | floor, `p ≤ N < p²` |
|---|---|---|
| `p³b_{Np+r} − b_N a_r` | **1** | **−2** |
| `a_{Np+r} − a_N a_r` | **1** | **1** |

**The loss is exactly `3 = w` orders, and it is entirely the weight's.** Cause: for
`N ≥ p` the coefficient `2H^{(3)}_N − H^{(3)}_C` acquires a `p^{-3}` pole, so the `O(p)`
Lucas defect of §3.1 is multiplied by `O(p^{-3})`. The a-row, having no harmonic
weight, does not degrade at all. This is the precise sense in which Theorem 2 being
*mod p* rather than *mod p³* costs information: it pins `b_{ap+r}` only modulo `p^{-2}`,
and re-inserting that at the next digit costs three orders.

**The grading supplies it back, exactly.** With `p^{3m}` for `m` digits:

| statement | floor |
|---|---|
| `p⁶b_{bp²+sp+r} − b_b a_s a_r` | **1** (= the one-digit depth) |
| `a_{bp²+sp+r} − a_b a_s a_r` | **1** |
| `p⁶b_n − b_b(a_s+2pbU_s)(a_r+2pNU_r)` | **2** |
| `a_{Np+r} − a_N·Adig(p,r;pN)` at `m = 0,1,2`, **any** `N < p²` | **1, 2, 3** |

So (i) nothing is irrecoverably lost — the `p^{3m}` grading restores the one-digit
depth exactly; (ii) the first-order defect `U` supplies the next order in the graded
two-digit form as well (floor 1 → 2); and (iii) the a-row scalar law is
**digit-uniform**: `a_{Np+r} ≡ a_N·Adig(p,r;pN)` to depth 3 for every `N < p²`, not
only `N < p`. The b-row law is *not* digit-uniform, and the obstruction is precisely
the `p^{-3}` pole — i.e. the weight.

---

## 7. T2 — the origin of the weight `[SOLVED]`

`b_n` **is** a primitive third-order coefficient of a single deformed hypergeometric
family, exactly, with no ζ-values and nothing to cancel.

### 7.1 The answer

Let `Π_j(t) := ∏_{i=1}^{t}(1 + jε/i) = Γ(t+1+jε)/( t! Γ(1+jε) )` — the
`Γ(1+jε)`-normalised (Pochhammer) ratio. Set

> **`A_ε(n,k) := A(n,k) · ∏_{j=1}^{3} Π_j(n)^{u_j} Π_j(k)^{v_j}`,
>  `u = (6, −6, 2)`,  `v = (−3, 3, −1)`**

Then, with `e_m(c) := Σ_j c_j j^m`,

```
  log(A_ε/A) = Σ_{m≥1} ε^m L_m ,   L_m = ((−1)^{m−1}/m)[ e_m(u) H^(m)_n + e_m(v) H^(m)_k ]
  e_1(u) = e_2(u) = 0,  e_3(u) = 12 ;   e_1(v) = e_2(v) = 0,  e_3(v) = −6
  =>  L_1 = L_2 = 0  identically  =>  B_3 = L_3 + L_1L_2 + L_1³/6 = L_3 = 2(2H^(3)_n − H^(3)_k)
```

> **`b_n = ½ · [ε³] Σ_k A_ε(n,k)`**  `[PROVED; VERIFIED exact over ℚ, n = 0…20]`

`t2_final.py` computes `[ε^m] Σ_k A_ε` from scratch (truncated exact series, no use of
the derivation) and gets `(a_n, 0, 0, 2b_n)` for every `n ≤ 20`, e.g.
`n=5: 35441662103/36000 = b_5`. **`[ε¹]` and `[ε²]` vanish termwise**, not by
summation: the coefficient is primitive by construction, not by conspiracy.

### 7.2 The symmetry that kills the weight-1 and decomposable terms

It is a **third finite difference in the deformation parameter**: apply the shift at
the three scaled parameters `ε, 2ε, 3ε` with exponents whose first two power-sum
moments vanish. Given shifts `(1,2,3)` and a target `e_3 = E`, the inverse Vandermonde
forces the exponents up to nothing at all: `(E/2, −E/2, E/6)`. `(u, v)` above are the
`E = 12` and `E = −6` cases, and the ratio `12 : −6` is exactly the `2 : −1` of
`2H^(3)_n − H^(3)_k`. **Two shift points are impossible** (`c₁m₁ + c₂m₂ = 0` and
`c₁m₁² + c₂m₂² = 0` force `m₁ = m₂`), so **three is minimal**. `[PROVED]`

### 7.3 What is obstructed, precisely

**(a) The suggested family cannot work.** `A(n,k) = [Γ(n+k+1)/(Γ(k+1)²Γ(n−k+1))]²`
has exactly three Γ-letters `n+k, k, n−k`; deforming *those* (i.e. "shift each of the
four binomial factors by its own ε-parameter") can only produce
`H^(3)_{n+k}, H^(3)_k, H^(3)_{n−k}` at weight 3 — never `H^(3)_n`. And

> `b_n ∉ span_ℚ{ S_X, S_Y, S_Z }`,  `S_L(n) := Σ_k A(n,k) H^(3)_{L}`
> `[EXCLUDED]` — `S_X, S_Y, S_Z, S_N` are ℚ-**independent** (rank 4 of 4 on
> `n = 0…15`, 11 excess equations), and `b_n = 2S_N − S_Y` uniquely. `t2_exclude.py`

So an `n`-only factor is **mandatory**, and the representation `2S_N − S_Y` — hence the
weight `3` and the coefficient `2` — is an invariant of `b_n`, not a choice.

**(b) Purity of the one-parameter members.** Within the single-shift family
`(α,β,γ)` on `(n+k, k, n−k)`, requiring `e_1 = e_2 = e_3 = 0` (no Euler γ, no ζ(2), no
ζ(3)) has the **unique** solution `(1,0,1)` — the shift `n → n+ε` — with
`L_3 = (2/3)(H^(3)_{n+k} − H^(3)_{n−k})`. `[PROVED, t2_deform.py §STEP 2]`
That is exactly the deformation that drives T1's p-adic scalar law (§4.3). The other
distinguished member is the shift `k → k+ε`, `(1,1,−1)`, whose **first-order coefficient
of the sum vanishes — by the identity `V_n = 0` of §3.2.** The same identity governs
both targets.

**(c) Where the ζ(3) lives, and the Bloch–Vlasenko link.** If the Pochhammers are left
un-normalised — plain `Γ(n+1+jε)/Γ(n+1)` — the `Γ(1+jε)` factors survive and

> `[ε³] Σ_k A_ε(n,k) = 2( b_n − ζ(3)·a_n )`,  i.e. **twice the Apéry remainder**
> `[PROVED; L_1 = L_2 = 0 and L_3 = 2(2H³_n − H³_k) − 2ζ(3) verified for all n ≤ 12]`

and the ζ(3) coefficient is forced to be **exactly `−1` relative to `b_n`**, for every
scaling and every choice of `(n,k)`-dependent letters — again by the ℚ-independence in
(a): the ζ(3) coefficient of `L_3` is `−⅓Σ_L e_3(L)`, and `Σ_L e_3(L) = 0` together with
`Σ_L e_3(L)H^{(3)}_L = t(2H^{(3)}_n − H^{(3)}_k)` is inconsistent over any set of
`(n,k)`-dependent letters. `[EXCLUDED]`

**So the ζ(3) that the un-normalised Γ-deformation cannot avoid is the Apéry limit
itself**, and removing it costs exactly one constant Γ-factor,
`∏_j Γ(1+jε)^{-v_j} = 1 + 2ζ(3)ε³ + O(ε⁴)`. That factor is literally a value of the
Γ-generating series `exp(−Σ_{m≥2} ζ(m)x^m/m)` of `FROBENIUS_VIEWPOINT` §8 — the same
series whose Taylor coefficients are the Bloch–Vlasenko structure constants behind
`κ₃ = (17/6)ζ(3)` for this operator (`GAMMA_UNIFICATION` §2.1). The ζ(3) impurity of
the deformation and the ζ(3) in `κ₃` are the same object in the same series; only the
normalisation (n-side vs Frobenius z-side) differs, which is why the rational
prefactors differ. A brute sweep over 65 letters `αn+βk+δ` confirms that the *only*
way to reach coefficient-sum zero is a constant letter, i.e. a Γ-constant
(`t2_exclude.py`: `{n:2, k:−1, const 1:−9, const 2:+8}`, and `−9H^{(3)}_1 + 8H^{(3)}_2 = 0`).

### 7.4 One framework, both targets

The `Π_j` machinery of §7.1 is the same object as `Adig(p,r;ε)` of §4.3: the p-adic
scalar `u(a,r)` is the `n`-shift member evaluated at `ε = pa` with the k-sum cut at the
digit bound `p−1`, and the T2 answer is the third-difference member of the same family.
`U_r` is its `[ε¹]`, `X_p(r)` its `[ε²]`, and `b_n` its `[ε³]`. The weight `3` enters
as: the order of the finite difference needed to make the coefficient primitive
= the ε-order at which `H^{(3)}` appears = the `p`-power in the congruence = the order
at which the Frobenius cross term switches on (§5).

---

## 8. Files

| file | what |
|---|---|
| `core.py` | ladders (recurrence + direct sums), `A(n,k)`, `H^{(r)}`, `v_p`, mod-`p^k`, `F_p` rank/rref |
| `validate.py` | §1, instrument validation against the four recorded facts |
| `t1_rank.py` | §2, first-order defect ranks, 9 primes |
| `t1_ident.py` | §3, the identity `V=0`, `U_r`, the first-order law, the mod-`p²` law |
| `series.py` | the `n`-shift Γ-deformation, restricted `k`-range (`Σ_{s≤r}`) |
| `dseries.py` | `Adig(p,r;ε)` — Γ-deformation over the **full digit range**, exact rational |
| `t1_order2.py`, `t1_order2b.py`, `t1_X.py` | §4.2, second-order rank, scalarity, `a²`, and `X_p` |
| `t1_scalar.py`, `t1_dscalar.py` | §4.3, depth of the restricted vs full-digit-range scalar |
| `t1_order3.py` | §5, third-order split and the cross term |
| `t1_twodigit.py` | §6, the two-digit accounting |
| `t1_extend.py` | all five §2–§5 claims re-run at 13 primes, `5 ≤ p ≤ 47` |
| `t2_deform.py` | §7.3(b), the purity classification; the un-normalised construction |
| `t2_exclude.py` | §7.3(a)(c), the ℚ-independence and the 65-letter sweep |
| `t2_final.py` | §7.1, the primitive deformation, verified exactly `n ≤ 20` |
| `channels.py` | §9, the three `(a,c)`-channels; `ac`/`c²` are not rational identities |

---

## 9. Two precise conjectures, with their verification ranges

**C1 (two-level matrix law).** For every prime `p ≥ 5` and `n = ap+r` with `a, r < p`,

> `( a_n , p³b_n ) ≡ ( a_a , b_a ) · [[ u(a,r) , p³ b_r ],[ 0 , u(a,r) ]] (mod p⁴)`
> `u(a,r) = a_r + 2p·a·U_r + p²a²·X_p(r)`,
> `U_r = [ε¹]`, `X_p(r) = [ε²]` of `Σ_{s=0}^{p−1} A_Γ(r+ε, s)`

The `mod p³` truncation (drop the cross entry, keep `u`) is **`[PROVED]` at order `p`
and `p²`** (§3.1–§4.1) and `[VERIFIED, floor exactly 3, 13 primes 5 ≤ p ≤ 47]` at order
`p²a²`. The cross entry at `p³` is `[VERIFIED, 13 primes]` in the sharp form
"rank drops 3 → 2 and the r-space becomes the a-row's"; the full `mod p⁴` statement is
`[CONJECTURAL]` — the residual scalar defect at `p³` has rank 2 and is not yet named.

**C2 (rank profile).** The digit defect of the ζ(3) Apéry pair has rank profile
`1, 1, (2 | 3)` at orders `p, p², p³`, against `1, 2` for the Brown–Zudilin rank-3
ζ(5) family. `[VERIFIED, 13 primes 5 ≤ p ≤ 47 for ζ(3); 6 primes for BZ]`
Mechanism for the first `1`: the identity `V_n = 0` `[PROVED]`. Mechanism for the
second `1`: writing `A(ap+r,cp+s) ≡ A(a,c)A(r,s)·exp(2pΛ₁ − p²Λ₂)` with
`Λ₁ = a·u + c·v` and `Λ₂ = (a+c)²H^{(2)}_{r+s} − 2c²H^{(2)}_s − (a−c)²H^{(2)}_{r−s}`,
the `p²` bracket `2Λ₁² − Λ₂` has three channels

```
  a²:  2u² − (H²_{r+s} − H²_{r−s})           <- survives, and equals [eps^2] of the
                                                restricted (s<=r) deformation
  ac:  4uv − 2(H²_{r+s} + H²_{r−s})          <- must die
  c²:  2v² − (H²_{r+s} − 2H²_s + H²_{r−s})   <- must die
```

and the measured a-side factor `a²` says the last two die **mod p**. They are **not**
identities: `Σ_s A(r,s)·(ac-channel) = 0, −26, −905/2, −167965/18, …` and the `c²` sums
are `0, 11, 607/4, …`, nonzero over ℚ for `1 ≤ r ≤ 30`. So the vanishing is a genuine
mod-`p` cancellation **between region I and the borrow region `s > r`** — the same
borrow terms that supply `X_p(r) − c_2(r)`. `[VERIFIED, 13 primes]`, **not proved:
this is the one remaining gap between C2 and a theorem, and the sharpest open item
here.**

> **UPDATE 2026-07-26 — CLOSED. See `work/APERY_GAP.md`.** Two corrections/results:
> (a) the `c²` channel above has a **sign typo** (`+H²_{r−s}` should be `−H²_{r−s}`,
> since `[c²]Λ₂ = H²_{r+s} − 2H²_s − H²_{r−s}`); with the correct sign the `c²` sums are
> `0, 13, 905/4, …` and `Σ_ac + 2Σ_c² = 0` **identically over ℚ** `[PROVED]`;
> (b) with `g_r(z) = [(z+1)···(z+r)/(z(z−1)···(z−r))]²`, so that `A_Γ(r,z) = (sin²πz/π²)g_r(z)`,
> the borrow weight is `C(r,m) = g_r(r+m)` and `Σ_c² = Σ_{s≤r} FP_{z=s} g_r`, whence
> `Σ_c² + Ξ_p(r) ≡ 0 (mod p)` `[PROVED]` because `Σ_{w∈F_p^×} w^{-1} = Σ_{w∈F_p^×} w^{-2} = 0`.
> Consequently the `mod p³` law of C1 and the `1, 1` of C2's rank profile are **theorems**.
> Only C1's `mod p⁴` cross entry remains `[CONJECTURAL]`. (Note the contrast with the first order, where the borrow region contributes
nothing at all because `A` is a square — §3.1. At second order it contributes, and its
contribution is exactly what kills the two `c`-channels.)
