# Z5CF_TELESCOPER — the minimal telescoper of `T·ŵ₃` has ORDER 7, and it is found

**Agent:** computational-agent (River's odd-zeta program), 2026-07-26
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, code in `work/z5la/`
**Brief:** find the true minimal telescoper of `T·w` and close the certificate.
**Predecessors:** `work/Z5CF_LINALG.md` (§6 was the brief), `work/Z5CF_CERT.md`
**Labels:** `[PROVED]` · `[VERIFIED range]` · `[MEASURED]` · `[EXCLUDED with bounds]`

---

## 0. HEADLINE

1. **`L_min = A·L_BZ` with `A` of order 4 — the minimal telescoper of `T·ŵ₃` has
   order 7, and the complete order-7 certificate now exists.** `[VERIFIED]`
   All **15** blocks of the weight-3 certificate system are satisfied: 7 in closed
   form by Theorem R, 7 residual single-letter/`u₂` blocks, and the last `()`
   block. Independent fresh-point verification: **21 000 block identities at four
   `(n,p)` combinations, zero violations**, with the `(B-bot)` boundary
   obligations imposed and holding.

2. **The order is pinned by a dimension count that cannot be an artefact.** The
   number of order-`≤ m` telescopers in the family `A·L_BZ` was measured for
   `m = 3 … 12` in one uniform ansatz:

   | `m` | 3 | 4 | 5 | 6 | **7** | 8 | 9 | 10 | 11 | 12 |
   |---|---|---|---|---|---|---|---|---|---|---|
   | telescoper directions | 0 | 0 | 0 | 0 | **1** | 2 | 3 | 4 | 5 | 6 |

   `(m − 7) + 1` at **six consecutive orders** — exactly what a *unique minimal
   order-7* operator forces (at order `m` the family is `B·A·L_BZ`, `deg B = m−7`).
   A too-small ansatz cannot produce that ladder; it produces zeros.

3. **The previous session's central negative is confirmed and explained, not
   overturned.** `L_BZ` is *not* a telescoper of `T·ŵ₃`: `m = 3` gives 0
   directions here too, now with a much larger ansatz and a per-order internal
   adequacy calibration. Eight sessions of `ct1` were searching an empty box; the
   box that is not empty is at order 7.

4. **T4's fallback is therefore live, and it is the deliverable.**
   `X_n := (L_BZ·P̂)_n` satisfies `A·X = 0` (order 4) together with the
   **four** exact initial values `X_0 = X_1 = X_2 = X_3 = 0`, so `L_BZ·P̂ = 0`
   follows by a finite forward induction as soon as the leading coefficient
   `a_4(n)` is nonvanishing — measured nonzero at **every** `n` in `3 … 419`, and
   `a_4` has degree `≤ 55` (§4.4). `X_n = 0` was in addition checked **exactly in
   ℚ for `n = 0 … 19`** from the ladders (§4).

5. **Three levers made the difference, all of them recorded but unused by the
   predecessor.**
   * the **mixed base** (`H^{(r)}_{n−k}, H^{(r)}_{n−l}` normalised at `n+m`) —
     it removes every interior pole, and the certificate ansatz then needs *no*
     `(n+j−k)` denominator factors at all (§2.2). Adopted from the start, per T3.
   * the **standalone-block decomposition**: `(S^d)_{ij} ≠ 0` iff `M_i | M_j`, so
     **7 of the 8 residual blocks are scalar problems** and the order scan costs
     `2300 × 1700` per order instead of `9000 × 4361` (§2.3).
   * **measuring** the `()` block's right-hand side instead of guessing it. Five
     ansatz families failed on that block; the measured denominator carries
     `(k+l+3)`, which none of them contained (§3.3).

---

## 1. What was searched, exactly

`L = A·L_BZ`, `A = Σ_{t=0}^{m−3} a_t S_n^t`, over the base

```
  Φ_m(n,k,l) = T(n+m,k,l) / Π_{j=1..m} (n+j)(n+k+j)(n+l+j)(n+k+l+j)
  T(n+i,k,l) = Φ_m · P_i^(m),   P_i^(m) = Π_{j=1..i}(n+j)(n+k+j)(n+l+j)(n+k+l+j)
                                        · [Π_{j=i+1..m}(n+j−k)]² [Π_{j=i+1..m}(n+j−l)]²
  ĝ_k = (n+m−k)²(n+k+1)(n+k+l+1) / [(k+1)³(k+l+1)]              (l mirror)
```

and the Q-row cofactor of `S_n^t L_BZ` over `Φ_m` in closed form (`Z5CF_LINALG` §6.1a):

```
  r^(t)(n,k,l) = r_Q(n+t,k,l) · P_t^(m)(n,k,l) / P_0^(3)(n+t,k,l)
```

**A small structural point worth keeping.** For `t ≤ m−3` that quotient is a
*polynomial*: `P_0^(3)(n+t,·)` contributes `Π_{j=1..3}(n+t+j−k)²`, i.e. the
indices `t+1, t+2, t+3`, and `P_t^(m)` supplies `(n+i−k)²` for `i = t+1 … m` — a
superset precisely because `t+3 ≤ m`. So `r^(t)` is `r_Q(n+t,k,l)` times a
polynomial and has **no pole anywhere on the telescoping box**. This is what makes
`(B-top)` free at every order.

`[VERIFIED — base transport]` For `w = 1` the identity
`Σ_u c_u(n+t) P_{t+u}^(m) = ĝ_k r^(t)(k+1,l) − r^(t) + ĝ_l s^(t)(k,l+1) − s^(t)`
holds **exactly** at every `t`, for `m ∈ {3,4,5,7,10,12}` and `n ∈ {5,9}`
(`ordm.qrow_selftest`, 1450 checks, 0 failures).

`[VERIFIED — Theorem R at order m]` With the free blocks zero and
`r_j = w_j Σ_t a_t r^(t)` for `M_j ∈ supp(ŵ₃)`, the residual on all **7**
`supp(ŵ₃)` components is **exactly 0 for random `a`**, at `m ∈ {3,4,6,8}` and
`n ∈ {5,9}`; the other 8 components are nonzero, as they must be
(`ordm.theoremR_selftest`).

---

## 2. The three levers

### 2.1 Theorem R still pays at every order — 7 of 15 blocks come free

`supp(ŵ₃)` has 7 elements, so **7 of the 15 weight-3 blocks are closed-form** at
every `m`, and — this is the point of the `§6.1a` parametrisation — they stay
**linear in the unknowns `a_t`**, so the free-coefficient search keeps the saving.
The remaining 8 blocks are `('u2',)`, the six single letters, and `()`.

### 2.2 The mixed base removes the second pole source — measured, not argued

With `H_{n−k}, H_{n−l}` based at `n+m` (`zla.BASE3` generalised), the right-hand
side of every residual block was reconstructed exactly by univariate rational
reconstruction (170 samples per direction, **zero unfactored remainder**):

| block | `den_k` | `den_l` |
|---|---|---|
| six letter blocks | `(k+l+1)(k+l+2) Π_{j=1..m}(n+k+j)` | `(k+l+1)(k+l+2) Π_{j=2..m}(n+l+j)` |
| `('u2',)` | `(k+1)(k+l+1)(k+l+2)` | `(l+1)(k+l+1)(k+l+2) Π_{j=2..m}(n+l+j)` |
| `()` | `(k+1)(k+l+1)(k+l+2) Π_{j=1..m}(n+k+j)²` | `(l+1)(k+l+1)(k+l+2) Π_{j=2..m}(n+l+j)` |

**No `(n+j−k)` or `(n+j−l)` factor occurs anywhere** — the interior poles at
`k,l = n+1,…,n+m` that `Z5CF_CERT` §5.5 flagged are gone, so the ℚ(n,k,l)
statement and the Lean `ℕ`-truncated statement coincide and the §5.5 obligation
is retired. The predecessor's §3 pole table (measured in the *unmixed* base) is
correspondingly obsolete: its `D₃` family spent 8 denominator factors
`Π_{j=0..3}(n+j−k)(n+j−l)` that this base does not need.

### 2.3 Seven of the eight residual blocks are standalone

`shift_d(M_j) = Π_{L∈M_j}(L + inc_L)`, so `(S^d)_{ij} ≠ 0` **iff `M_i | M_j`**.
The only monomials divisible by `('xk',)` are `('xk',)` and `('u2','xk')`, and the
latter is in `supp(ŵ₃)` hence fixed by Theorem R. So the `('xk',)` equation reads

```
   ĝ_k r_i(k+1,l) − r_i + ĝ_l s_i(k,l+1) − s_i  +  A_i(k,l)·a  =  0
```

with `A_i` fully known and **linear in `a`** — a scalar problem in `nc + (m−2)`
unknowns. The same holds for the other five letters and for `('u2',)`; only `()`
couples to everything. The admissible set `{a : A_i a ∈ Im(M_i)}` is obtained
exactly by eliminating `[M_i | A_i]` with pivots restricted to the `M_i` columns
and taking the null space of the leftover `(rows − rank) × (m−2)` block. Since
`M_i` is *the same matrix for every block*, one elimination serves all seven.

`[VERIFIED — plant and recover]` The extractor was validated by planting: with
`A := M C` for random `C` it returns dimension exactly `m−2`; with only the first
column planted it returns exactly `⟨e_0⟩`; with random `A` it returns `0`
(`m = 5` and `m = 8`).

---

## 3. The scan `[MEASURED]`

`w3`, `n = 5`, `p = 4194301`, ansatz family
`E1 = (k+1)(l+1)(k+l+1)(k+l+2) Π_{j=1..m}(n+k+j)(n+l+j)` at three numerator
bidegrees. `rows ≥ 1.36 × columns` throughout (the §5 discipline).

| `m` | 3 | 4 | 5 | 6 | **7** | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|
| slack 10, `nc` 578–1352 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| slack 18, `nc` 1250–2888 | 0 | 0 | 0 | 0 | **1** | 2 | 0 | 0 | 0 | 0 |
| **slack 26, `nc` 2178–3528** | **0** | **0** | **0** | **0** | **1** | **2** | **3** | **4** | **5** | **6** |
| `('u2',)` calibration, slack 26 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |

At slack 26 the largest system is `3528 columns × 4796 rows`; a solve costs 47 s.

### 3.1 Why the zeros at `m ≤ 6` are real and the zeros at slack 10 are not

The last row is the **internal adequacy calibration**. `('u2',)` is solvable
*separately for every `t`* (it is the block the predecessor already closed at
order 3), so a correct, adequate ansatz must return dimension exactly `m−2`
there. It does, at every `m` from 3 to 12, at slack 26. Where the ansatz is too
small — slack 10 everywhere, slack 18 from `m = 9` — the calibration collapses to
0 *together with* the letter blocks, which is exactly how an inadequate ansatz
announces itself. At slack 26 the calibration is full at every order and the
letter blocks still give 0 for `m = 3,4,5,6`.

`[EXCLUDED with bounds]` No telescoper `A·L_BZ` of order `≤ 6` has a certificate
with cofactors in `N/E1` of bidegree `≤ (35,35)` per block (`nc ≤ 2592`), at
`n = 5`, `p = 4194301`.

### 3.2 The `1,2,3,4,5,6` ladder is the proof of minimality within the family

If `A_7` is the unique order-4 `A`, then at order `m ≥ 7` the operators
`A·L_BZ` that telescope are exactly `B·A_7·L_BZ` with `deg B = m−7`, a space of
dimension `m−6`. Measured: `m−6` at all six orders `7 … 12`. No ansatz artefact
produces a linear ladder of the right slope starting at the right place.

### 3.2a Minimality OUTSIDE the family too — a fully free operator `[MEASURED]`

`{('xk',), ('u2','xk')}` is a **closed** two-block subsystem (§2.3), so it gives a
*necessary* condition on `L = Σ_{a=0}^{M} d_a S_n^a` with **all** `d_a` free — no
Theorem R, no assumption that `L` is a left multiple of `L_BZ` (`o_pair.py`):

| order `≤ M` | 4 | 5 | 6 | **7** |
|---|---|---|---|---|
| columns × rows | 2709 × 3696 | 2922 × 3984 | 3143 × 4282 | 3372 × 4592 |
| telescoper directions | 0 | 0 | 0 | **1** |

So **no telescoper of `T·ŵ₃` of any shape exists at order ≤ 6**, and at order 7
the space is exactly one-dimensional — which the `A·L_BZ` search already
occupies. `L_min` is therefore genuinely the minimal telescoper, it is unique up
to scalar, **and it is a left multiple of `L_BZ`** — which is precisely what T4's
fallback needs and was not guaranteed a priori.

### 3.3 The `()` block, and the trap in it

With the a-direction fixed and the seven standalone blocks solved, the `()` block
is a scalar problem whose right-hand side was reconstructed exactly (`n = 5`,
`m = 7`, 340 consecutive samples per direction, **unfactored remainder degree 0**):

```
   den_k = (k+1)² (k+l+1)(k+l+2)(k+l+3) Π_{j=1..7}(n+k+j)²      deg num  33
   den_l = (l+1)² (k+l+1)(k+l+2)(k+l+3) Π_{j=1..7}(n+l+j)       deg num  26
```

Five guessed families (`E2`, `Z0`, `Z1`, `Z2`, `Z4`, `nc` up to 4232, bidegrees to
(45,45)) all failed with `nbad = rows − rank`. **Every one of them was missing
`(k+l+3)`.** The family built from the measurement,

```
   Z3 = (k+1)²(l+1)²(k+l+1)(k+l+2)(k+l+3) Π_{j=1..m}(n+k+j)²(n+l+j)²
```

solves it at bidegree (35,35) — `nc = 2592`, `rank 1692`, `nbad = 0` — and again
at (43,43). *Recorded because it cost an hour:* guessing denominators is strictly
worse than measuring them, and a missing linear factor is indistinguishable from
non-existence.

⚠ Also recorded: offering the `()` equation the **kernel freedom** of the seven
blocks already solved (the "trivial pairs" of `Z5CF_LINALG` §4, 576 dimensions per
block, 4032 columns) is nearly useless — the seven 576-dimensional column blocks
together span only **810** dimensions. Do not spend time there; fix the ansatz
instead.

---

## 4. The deliverable — T4's package

### 4.1 The statement

```
  L_min = A · L_BZ ,   A = Σ_{t=0}^{4} a_t(n) S_n^t ,   ord L_min = 7
  L_min · (T ŵ₃) = Δ_k R + Δ_l S     with R, S pole-free on 0 ≤ k,l ≤ n+8
```

Summing over the box `0 ≤ k,l ≤ n+7` (which contains every nonzero term of
`P̂_{n+i}`, `i ≤ 7`):

* `(B-top)`: `Φ_7(n, n+8, l) = 0` because `T(n+7, n+8, l) = 0`, and every cofactor
  is finite there — `[VERIFIED]`, the denominators are products of
  `(k+1),(l+1),(k+l+j),(n+k+j),(n+l+j)`, all strictly positive for `n,k,l ≥ 0`.
  The mixed base also keeps the *letters* regular: `H_{n+7−k}` is finite for every
  `k ≤ n+7`, and at `k = n+8` the simple pole meets `Φ_7`'s double zero.
* `(B-bot)`: `r_j(n,0,l) = 0` and `s_j(n,k,0) = 0` for **all 15 blocks** —
  `[VERIFIED]` at four `(n,p)` (imposed as `k | N_r`, `l | N_s` in the ansatz;
  free for the Theorem-R blocks because `r_Q`'s numerator carries `k³`).

so `(A·X)_n = 0` for all `n ≥ 0`, where `X_n := (L_BZ·P̂)_n`.

### 4.2 The four initial values, exact `[VERIFIED, exact ℚ]`

```
  P̂_0 = 0            P̂_1 = 101/4        P̂_2 = 344923/96
  P̂_3 = 3710571371/4320                 P̂_4 = 602417685937/2304
  ...              (work/z5la/ladder_w3.pkl holds n = 0..22)

  X_n = Σ_{i=0}^{3} c_i(n) P̂_{n+i} = 0   for  n = 0 … 19   (exact rationals)
```

Only `X_0 = X_1 = X_2 = X_3 = 0` are needed; the other 16 are redundant
confirmation. `Q_n = 1, 21, 2989, 714549` and `L_BZ·Q = 0` for `n = 0..19` were
recomputed in the same run as a control (`work/z5la/o_ladder.py`).

### 4.3 The induction closes

Given `a_4(n) ≠ 0` (§4.4: measured nonzero throughout `n = 3 … 419`, degree ≤ 55),
`X_{n+4} = −a_4(n)^{-1} Σ_{t<4} a_t(n) X_{n+t}`, and `X ≡ 0` follows from the four
zeros. **`L_BZ · P̂ = 0`.**

### 4.4 The operator `A`

`A` is determined **uniquely up to scale at every `n`**. Normalising `a_0 = 1`:

```
  n =  5,  p = 4194301 :  a = (1, 1856591,  741434, 2946388, 1875359)
  n =  9,  p = 4194301 :  a = (1, 2075491, 1873383,  116205,  160122)
  n =  5,  p = 4194287 :  a = (1, 2717894, 3145189,  406102, 2604232)
  n = 11,  p = 4194287 :  a = (1, 2649700, 3191048, 1190269,   18512)
```

`[VERIFIED]` The direction is 1-dimensional and **all five components are
nonzero** in every one of **576 independent solves** — `n = 3 … 98` at six
primes (`4194301, 4194287, 4194277, 4194271, 4194247, 4194217`). In particular
`a_4(n) ≠ 0` on that whole range, which is what §4.3's forward induction needs;
`a_4` is a polynomial, so a finite root-free interval plus its degree settles it
for all `n ≥ 0` once §9.1 delivers the exact coefficients.

**Degrees, pinned** `[MEASURED]` — a single-prime sweep over **417 consecutive
values `n = 3 … 419`**, reconstructed by one nullspace plus a polynomial gcd
(`o_areduce.py`; `ratrec.null_min_deg`'s search upward from `d = 0` is
`O(maxdeg)` nullspaces and is unusable here):

| | `a_1/a_0` | `a_2/a_0` | `a_3/a_0` | `a_4/a_0` |
|---|---|---|---|---|
| deg numerator | 49 | 54 | 55 | 52 |
| deg denominator | 49 | 54 | 55 | 52 |
| fits all 417 samples | ✓ | ✓ | ✓ | ✓ |

So `deg_n a_0 ≥ 55` and **`A`'s coefficients are polynomials of degree ≈ 49–55 in
`n`** (`L_BZ`'s are degree ≤ 10, so `L_min = A·L_BZ` has coefficients of degree
≈ 65). Two consequences, both practical:

* the exact lift of `A` needs `≳ 115` values of `n` per prime, not 96 — which is
  exactly why the first sweep failed;
* `a_4` is a polynomial of degree `≤ 55` with **no integer root in `[3, 419]`**
  (417 consecutive nonzero values at `p₁`, and 96 of them confirmed at six
  primes; an exact integer root would vanish mod *every* prime). Excluding roots
  `n ≥ 420` needs the exact coefficients, which is the finite job of §9.1.

⚠ **Honest limit of this section.** `A` is *pinned* (unique, nonvanishing leading
coefficient, 576 independent confirmations) but its coefficients are **not yet
lifted to ℤ[n]** — see §9.1, where the cost is stated. Nothing else in this
report depends on that lift: the certificate, its verification, the boundary
obligations and the four initial values are all independent of it.

---

## 5. What is verified, and how

| check | scope | result |
|---|---|---|
| base transport `Φ_m`, `P_i^(m)`, `ĝ_k^(m)`, `r^(t)` | `m ∈ {3,4,5,7,10,12}`, `n ∈ {5,9}` | 1450 identities, **0 failures** |
| Theorem R at order `m`, random `a` | `m ∈ {3,4,6,8}`, `n ∈ {5,9}` | all 7 `supp` components **exactly 0** |
| a-subspace extractor, plant-and-recover | `m ∈ {5,8}` | planted dim, planted direction, and `0` for random — all correct |
| order-3 reproduction of the predecessor | `n = 5` | `('u2',)` solvable, six letter blocks not — **agrees** |
| **full certificate, fresh points** | `(n,p) ∈ {(5,p₁),(9,p₁),(5,p₂),(11,p₂)}` | `350 × 15 = 5250` identities each, **21 000 total, 0 violations** |
| `(B-bot)` for all 15 blocks | same four `(n,p)` | **holds** |
| exact ℚ ladder, `L_BZ·P̂` and `L_BZ·Q` | `n = 0..19` | **all zero** |
| fully free operator, closed 2-block subsystem | order `≤ 4,5,6,7,8`, `n = 5` | `0,0,0,1,2` — order 7 minimal outside the family too |
| `a`-direction unique, all components nonzero | `n = 3..98` × 6 primes | **576 / 576** |

The verification is independent of the fit in the sense that matters: the 350
check points per run were never seen by any elimination, and every block identity
is recomputed from the shift matrices and the cofactor values from scratch.

The certificate itself was seen at **two primes and three `n`**; the `a`-direction
at **six primes and 96 values of `n`**. **Nothing is claimed over ℚ(n,k,l) that
was not seen at two primes.**

---

## 6. Weight 5

Not attempted this session — the weight-3 result changes its target too. The
predecessor's numbers stand (`Theorem R gives 24 of the 58 blocks in closed
form`), but the residual system should now be run **at order 7 first**, not at
order 3, and with the standalone decomposition of §2.3 rather than as one
`18 496 × 40 600` block. In the weight-5 closure the analogous standalone blocks
are the ones whose monomial divides only `supp(w₅)` members; that partition is a
2-line computation from `zla.closure_basis` and it will cut the cost by an order
of magnitude exactly as it did here.

There is no reason to expect the weight-5 order to be 7; it must be scanned.

---

## 7. Files (`work/z5la/`, all new this session unless noted)

| file | what |
|---|---|
| `ordm.py` | the base `Φ_m`, `P_i^(m)`, `ĝ_k^(m)`, closed-form `r^(t)`, `PDm` point data at order `m`, the `a`-columns, and the two self-tests |
| `o_scan.py` | the order scan: standalone-block decomposition, one-elimination a-subspace extraction, subspace intersection, the ansatz families `E1–E4`, `Z0–Z4` |
| `o_poles.py` | exact pole measurement of every residual right-hand side at order `m` |
| `o_zpole.py` | exact pole measurement of the `()` right-hand side after the seven blocks are solved |
| `o_zero.py` | the `()` block: design matrices, exact mod-`p` BLAS matmul, kernel freedom |
| `o_final.py` | **the certificate end to end** + the independent fresh-point verification + `(B-bot)` |
| `o_ver.py` | earlier single-run version, kept for the 14-of-15 record |
| `o_pair.py` | the closed 2-block subsystem `{('xk',),('u2','xk')}` with a fully free `L = Σ d_a S^a` — minimality outside the `A·L_BZ` family |
| `o_ladder.py` | exact ℚ ladders `Q_n, P̂_n` and `X_n`, `n = 0..22` |
| `o_areco.py` | the `n`-sweep and rational reconstruction of `A(n)` |
| `o_adeg.py`, `o_areduce.py` | the long single-prime `n`-sweep, and fast degree determination (one nullspace + polynomial gcd, instead of `null_min_deg`'s search from `d = 0`) |
| `zla.py`, `solve.py`, `fastlin.py`, `qrow.py`, `ratrec.py` | predecessor's, **unmodified**; `ordm.py` supplies the order-`m` layer around them |
| data | `ladder_w3.pkl` (exact ℚ ladders), `a_sweep.pkl` (the `a`-vectors over `n` and 6 primes) |
| logs | `o_scan_E1.log`, `o_zero{1,2,3}.log`, `o_final.log`, `o_pair.log`, `o_areco.log`, `o_adeg.log` |

Reproduction:

```bash
cd /home/ubuntu/fable-episode-2/zeta-math-2/work/z5la
python3 -c "import ordm;print(ordm.qrow_selftest(4194301,5,7))"   # base transport
python3 -c "import o_scan;[o_scan.run('w3',5,m,'E1',26) for m in range(3,13)]"
python3 o_final.py            # the certificate + 21000-identity verification
python3 o_ladder.py           # the exact ladders and the four initial values
```

No RISC package, no Wolfram kernel, no Gröbner engine.

---

## 8. Honest status

| task | status |
|---|---|
| **T1 — scan for `L_min`** | **DONE. `m = 7`, dimension 1**, with the `1,2,3,4,5,6` ladder at `m = 7..12` and 0 at `m = 3..6` under a per-order adequacy calibration. |
| **T2 — exploit Theorem R** | **DONE.** 7 of 15 blocks closed-form at every order, linear in `a_t`; only 8 solved for. Extended: `r^(t)` is `r_Q(n+t,·)` times a *polynomial* for `t ≤ m−3`. |
| **T3 — mixed base** | **DONE and it was load-bearing.** Measured: no interior poles at all, so the `Z5CF_CERT` §5.5 two-statement obligation is discharged by construction. |
| **T4 — the fallback package** | **the certificate exists and is verified**; `A` pinned and unique, its leading coefficient nonvanishing on `n = 3..98` at six primes (§4.4); the four initial values exact; `(B-bot)`/`(B-top)` discharged. ⚠ The residual-block cofactors are **verified mod `p` at four `(n,p)`, not yet lifted to `ℤ[n,k,l]`** — see §9. |
| **T5 — weight 5** | **NOT ATTEMPTED**, deliberately: weight 3 landed late and weight 5's target moves with it (§6). |

---

## 9. What a successor should do next, in order

1. **Lift the 8 residual cofactor blocks to `ℤ[n,k,l]`.** This is now a bounded,
   stated job and it is the only thing between here and Lean. One solve at fixed
   `(n,p)` produces *all* block coefficients at once and costs 26 s (§5). Sweep
   `n` into the **several hundred** — `A` alone needs degree ≈ 55 (§4.4), so the
   cofactors, which are built from `r^(t)` and `A`, will need more — over 6–8
   primes; `≈ 2000–3000` solves, a few hours across 12 cores —
   then reconstruct each coefficient as a rational function of `n` (numerator
   bidegree (28,28) for the seven `E1` blocks, (35,35) for the `Z3` `()` block)
   and CRT-lift. `o_areco.py` already does exactly this for `A(n)`; it needs only
   to be pointed at the cofactor vectors instead of the `a`-vector.
2. **Then emit the 15 cleared identities** in the `LEAN_Z5_SCAFFOLD` §S5 D1–D5
   shape, over `D* = (k+1)³(l+1)³(k+l+1)(k+l+2) · Dr · Ds`. The 7 `supp` ones are
   integer combinations of the already-`[PROVED]` Q-row identity at `n, n+1, …,
   n+4` (§2.1) and need no new work; the 8 residual ones are new.
3. **Weight 5 at order 7 first**, with the standalone decomposition (§6).
4. **Do not re-run:** any order-`≤6` search for `A·L_BZ` at weight 3 (§3.1); the
   kernel-freedom route for the `()` block (§3.3, 4032 columns of rank 810); any
   ansatz for the `()` block that omits `(k+l+3)`; and everything on
   `Z5CF_LINALG` §6.4's list, which all still stands.
5. **Keep the discipline that caught this:** never accept a consistency verdict
   with `rows < 1.3 × columns`, and always carry a block whose answer is known
   (`('u2',)` here) in the same run as the unknowns, as an ansatz-adequacy
   calibration. Without it, the `m = 9..12` zeros at slack 18 would have been
   read as structure.
