# Z5CF_REP — **YES.** The telescoper order is a property of the REPRESENTATIVE, and an order-3 one exists

**Agent:** computational-agent (River's odd-zeta program), 2026-07-26
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, code and data in `work/z5rep/`
**Brief:** find a representative `w` of the `P̂` row whose summand `T·w` has a low-order
telescoper, or exclude one in a stated search space.
**Predecessors:** `work/Z5CF_TELESCOPER.md` (order 7 for `T·ŵ₃`), `work/Z5CF_CERT.md`,
`work/Z5CF_LINALG.md`, `work/ZETA5_CLOSEDFORM.md`, `work/REFOLD.md`, `work/PHASE2_NUCLEUS.md`
**Labels:** `[PROVED]` · `[VERIFIED range]` · `[MEASURED]` · `[EXCLUDED with bounds]`

---

## 0. HEADLINE — **YES**

**`L_BZ` itself — order 3, the operator already in Lean — IS a telescoper of `T·w★` for a
new representative `w★` of the `P̂` row.** The complete order-3 certificate exists and has
been verified at fresh points; the entire order-7 apparatus of `Z5CF_TELESCOPER` (the
order-4 factor `A` with degree 49–55 coefficients, the extra forward induction, the
unfactored leading coefficient `a₄(n)`) is **not needed and should be discarded**.

> ### `w★ = H⁽³⁾_k + U·( H⁽²⁾_k + H⁽²⁾_n + H⁽²⁾_{n+k} − H⁽²⁾_{n−l} ) + V·( H⁽²⁾_l − H⁽²⁾_k )`
>
> ```
>   U =   H_k − ½( H_{n−k} + H_n + H_{n+k+l} − H_{n+l} )
>   V = − ½( H_k + H_l − H_{n−k} − H_n + H_{n+k} − H_{n+k+l} )
> ```
>
> **`Σ_{k,l=0}^{n} T(n,k,l)·w★(n,k,l) = P̂_n`** `[VERIFIED exact ℚ, n = 0…20, every cell,
> 0 discrepancies]` and `L_BZ·(Σ T·w★) = 0` `[VERIFIED exact ℚ, n = 0…17]`.

1. **The certificate.** With the pole-free base `Φ₃` of `LEAN_Z5_SCAFFOLD` §5.2, all **42**
   blocks of the shift-closure system for `T·w★` are solved by rational cofactors
   `ρ_j, σ_j`, i.e. `L_BZ·(T w★) = Δ_k R + Δ_l S`. `[VERIFIED]` — five independent
   fresh-point runs, `(n,p) ∈ {(9,p₁),(11,p₁),(13,p₁),(9,p₂),(11,p₂)}`, **400 points ×
   109 components = 43 600 identities each, 218 000 total, zero violations** (§4.3). The
   admissible set is a **13-dimensional** space that is *identical* at `n = 9, 11, 13, 17`.

2. **What actually blocked the predecessor was the representative, not the row.**
   `ŵ₃`'s six single-letter blocks are unsolvable at order 3 — the predecessor's central
   negative, reproduced here exactly as an ansatz calibration (§3.1). Replacing `ŵ₃` by
   another representative of the *same* row removes them completely: there is a
   **16-dimensional** family of representatives for which all 18 letter blocks close, and a
   12-dimensional affine subfamily for which the coupling `()` block closes too.

3. **`P̂` has a 58-dimensional kernel of representatives** in the degree-≤2 bare weight-3
   span (109 monomials, 9 symbols): `dim K = 58`, rank of the sum-map `51`, measured with
   170 excess rows at two primes (§2). **45 of those 58 dimensions are the `k↔l`
   antisymmetric subspace** and are `[PROVED]` in `K` by `T(n,k,l) = T(n,l,k)`; the other 13
   are genuinely symmetric relations.

4. **Symmetrisation alone is NOT the mechanism** `[MEASURED]`. `ŵ₃^sym` fails at order 3 in
   **exactly the same six letter blocks** as `ŵ₃`, at `n = 9, 11, 13, 17`. So does `ṽ`, and
   so does `ṽ^sym`. The antisymmetric-baggage hypothesis is refuted as a *fix*, although its
   premise is correct and useful: the antisymmetric part is in `K`, which is part of why the
   representative family is large. A symmetric member of the successful family does exist —
   it is simply not the symmetrisation of `ŵ₃` (§3.4).

5. **`ṽ` (REFOLD, closure rank 11) does not help at order 3** `[EXCLUDED, bounds in §3.2]`,
   and **`L̃` (the desingularised order-4 left multiple, `PHASE2_NUCLEUS` §3.3) buys
   nothing**: its admissible weight space is *identical* to `L_BZ`'s, dimension 37, at
   `n = 9, 11, 13` (§3.3). Step 3 of the brief is answered: `L̃` is not a telescoper of
   `T·ŵ₃` nor of `T·ṽ`.

6. **The cost trade for Lean.** `w★` has 29 monomials, 13 symbols, **shift closure `J = 42`**
   (against `J = 15` for `ŵ₃`). So the Lean file gets **42 `ring`-closable identities at
   order 3** instead of 15 at order 7 — and loses the order-7 route's three genuinely hard
   obligations: `A`'s degree-55 coefficients, the second forward induction, and proving
   `a₄(n) ≠ 0` for a degree-≤55 polynomial with no known factorisation. `L_BZ`'s own leading
   coefficient `c₃(n) = 2(n+3)⁵(2n+5)a₀(n)` is already proved positive in Lean in three
   lines (§5).

⚠ **The one thing not yet delivered** is the lift of the 42 cofactor pairs from
`mod p, fixed numeric n` to `ℚ(n,k,l)` and then `ℤ[n,k,l]`. That is a bounded, stated,
mechanical job (§6.1) — the same job `o_areco.py` already performs for `A(n)`, but now
against cofactor vectors of *far* smaller degree, and with no `a₄`-style obstruction behind
it. Everything in §0.1–§0.6 is independent of it.

---

## 1. The framing that made the difference

The predecessor asked *"what is the minimal telescoper of `T·ŵ₃`?"* and answered 7, correctly.
The right question is one level up. Write `V` for the ℚ-span of a shift-closed set of
harmonic monomials and

```
   K  :=  { w ∈ V  :  Σ_{k,l} T(n,k,l) w(n,k,l) = 0  for every n }.
```

Every element of `ŵ₃ + K` is a representative of the same row `P̂`, and telescoper order is a
property of the *summand*, so it varies over that coset. The key computational point is that
for a **fixed** operator `L` the certificate system is **linear in `w` as well as in the
cofactors** — so one can solve for the *weight and the certificate simultaneously* instead of
scanning weights one at a time. That single change turns an unbounded search into one
elimination.

Concretely, with `L = L_BZ` (order 3) and the base `Φ₃`, the block-`M` equation is

```
   ĝ_k ρ_M(k+1,l) − ρ_M + ĝ_l σ_M(k,l+1) − σ_M  =  A_M(k,l) · w ,
```

`A_M` known and **linear in the weight-coefficient vector `w`**. The admissible set is
`{ w : A_M w ∈ Im(Msc) }` — exactly `o_scan.asubspaces`'s shape with `w` in place of `a`, so
one elimination of `[Msc | A_{M₁} | … | A_{M₁₈}]` serves all blocks. The predecessor's
standalone-block decomposition is reused verbatim.

### 1.1 The search space, stated exactly

Bare alphabet `H^(r)_x`, `r = 1,2,3`, `x ∈ {n, k, l, n+k, n+l, n−k, n−l, k+l, n+k+l}`
(the nine arguments you get by differentiating `T`'s five binomials — `ZETA5_CLOSEDFORM` §0).

```
   V  =  span of all weight-3 monomials of DEGREE ≤ 2, plus their divisibility closure
      =  { () } ∪ { H⁽¹⁾_x } ∪ { H⁽²⁾_x } ∪ { H⁽³⁾_x } ∪ { H⁽¹⁾_x H⁽²⁾_y }
      =  1 + 9 + 9 + 9 + 81  =  109 monomials.
```

`ŵ₃` (7 monomials), `ṽ` (15), `ŵ₃^sym` (14), `ṽ^sym` (29) all lie in `V`. Degree-3 monomials
`H⁽¹⁾H⁽¹⁾H⁽¹⁾` are **excluded** (they would take `J` to 319 and break the
"every strict multiple of a letter is maximal" property that makes the scan cheap). That is
the one stated restriction on the search space; `w★` did not need them.

---

## 2. `K`, measured `[MEASURED, two primes, 170 excess rows]`

`work/z5rep/sumrows.py`: rows `n = 0…220`, columns the 109 monomials, entry
`Σ_{k,l} T(n,k,l)·M_j(n,k,l)` mod `p`.

| quantity | value |
|---|---|
| rank of the sum-map `V → (sequences)` | **51** |
| `dim K` | **58** |
| `P̂` in the image | **yes** |
| `Σ T·ŵ₃ − P̂`, `Σ T·ṽ − P̂` over `n = 0…220` | 0 nonzero rows |
| `Σ T·ŵ₃^sym − P̂`, `Σ T·ṽ^sym − P̂` | 0 nonzero rows |
| `Σ T·ŵ₃^anti` | 0 nonzero rows (221 of 221) |

Identical at `p = 4194301` and `p = 4194287`.

**Structure of `K`** `[PROVED for the 45, MEASURED for the 13]`. `T(n,k,l) = T(n,l,k)`, so
every `k↔l`-antisymmetric weight is in `K`; that subspace has dimension **45** in `V`
(3 + 3 + 3 antisymmetric letters, 36 antisymmetric `H⁽¹⁾_x H⁽²⁾_y`). The remaining
**13** dimensions of `K` are symmetric relations and do require the linear solve — the
`REFOLD` "key identity" `Σ T·[3A₂(k)C₁ + A₂(k)A₁(l) + 2A₂(l)A₁(k) + 6A₂(l)B₁(k)] = 0` is one
of them. This confirms and sharpens the coordinator's §1: the antisymmetric half is free, the
symmetric half is not.

> **Note for `ZETA5_CLOSEDFORM` §0** (flagged, not edited — another agent may be in that file):
> "exact minimum support inside the stated search space" is only well posed **modulo `K`**.
> With `dim K = 58` in a 109-dimensional space, two representatives of the same row have
> incomparable supports; `ŵ₃`'s 7 monomials and `w★`'s 29 describe the *same* `P̂`. The
> minimality claim should be qualified as "minimum support among weights, not among
> representatives of the row".

---

## 3. The scan `[MEASURED]`

`work/z5rep/frw.py`, `scanN.py`. Ansatz family
`F1 = (k+1)²(l+1)² · Π_{j=1..m+2}(k+l+j) · Π_{j=1..m}(n+k+j)²(n+l+j)²(n+k+l+j)`
— chosen to *contain* every denominator any letter of the nine-symbol alphabet can produce,
including the `(k+l+3)` that cost the predecessor an hour (`Z5CF_TELESCOPER` §3.3) and the
`(n+k+l+j)` that its `E1` family did not have. Base degrees `(16,16)`, slack 16 →
bidegree `(32,32)`, `nc = 2178`, rows `3107` (**ratio 1.36**, the §5 discipline).

| `n` | 5 | 9 | 11 | 13 | 17 |
|---|---|---|---|---|---|
| `dim W_tel(n)` (18 letter blocks, `L = L_BZ`) | 58 | **37** | **37** | **37** | **37** |
| cumulative `∩` | — | 37 | 37 | 37 | 37 |
| `ŵ₃ ∈ W_tel + K` | YES | **YES** | **YES** | **YES** | **YES** |

`n = 5` is degenerate (small-`n` accident) and is not used. From `n = 9` on the condition is
**`n`-independent**: `dim(W_tel ∩ K) = 16`, so the affine family
`(ŵ₃ + K) ∩ W_tel` is **16-dimensional and non-empty** — every one of its members passes all
18 letter-block conditions at every `n` tested. Identical numbers at `p = 4194287`.

### 3.1 Per-order adequacy calibration — it caught two too-small ansätze

Two run-internal calibrations, both with answers known from the predecessor:

* **`('u2',) = H⁽²⁾_{n+k}` must admit `ŵ₃`** (the one block `Z5CF_CERT` closed at order 3);
* **the six single-letter blocks must reject `ŵ₃`** (the predecessor's central negative).

| slack | `nc` | `h2_pk` admits `ŵ₃`? | `h1_k` admits `ŵ₃`? | `dim W_tel(5)` | verdict |
|---|---|---|---|---|---|
| 4 | 882 | **no** | no | 10 | **ansatz too small — discarded** |
| 10 | 1458 | YES | no | 58 | adequate |
| 16 | 2178 | YES | no | 58 | adequate, stable |

At slack 4 every block returned `dim 99 = 109 − 10`, i.e. *nothing* was admissible — the
signature of an inadequate ansatz, and it would have read as a clean negative. Also carried:
the **control weight `w = 1`** (the Q row), whose full cascade including the `()` block must
close; it did in every run reported below (`family.py`, `joint.py`).

### 3.2 `ṽ`, `ŵ₃^sym`, `ṽ^sym` at order 3 `[EXCLUDED with bounds]`

Step 1 of the brief. `Σ_{k,l} T·ṽ = P̂_n` is confirmed first — `[VERIFIED exact ℚ, n = 0…20,
0 discrepancies]`, `work/z5rep/vt_exact.py`, and `L_BZ·(Σ T·ṽ) = 0` for `n = 0…17`.

Then, at `n = 9, 11, 13, 17`, `p = 4194301`, slack 16 (calibration passing):

| block | `ŵ₃` | `ŵ₃^sym` | `ŵ₃^anti` | `ṽ` | `ṽ^sym` |
|---|---|---|---|---|---|
| `H⁽¹⁾_k` | ✗ | ✗ | ✗ | ✗ | ✗ |
| `H⁽¹⁾_l` | ✗ | ✗ | ✗ | ✓ | ✗ |
| `H⁽¹⁾_{n+k}` | ✗ | ✗ | ✗ | ✗ | ✗ |
| `H⁽¹⁾_{n+l}` | ✗ | ✗ | ✗ | ✓ | ✗ |
| `H⁽¹⁾_{n−k}` | ✗ | ✗ | ✗ | ✗ | ✗ |
| `H⁽¹⁾_{n−l}` | ✗ | ✗ | ✗ | ✓ | ✗ |
| `H⁽²⁾_{n+k}` | ✓ (calib.) | ✓ | ✓ | ✗ | ✓ |
| `H⁽²⁾_k`, `H⁽²⁾_l`, `H⁽²⁾_{n+l}` | ✓ | ✓ | ✓ | ✗ | ✓ |
| **verdict at order 3** | **NO** | **NO** | **NO** | **NO** | **NO** |

`[EXCLUDED]` None of the four named representatives has `L_BZ` as a telescoper, with cofactors
in `N/F1` of bidegree ≤ (32,32) per block (`nc ≤ 2178`), at four values of `n` and two primes.
`ṽ`'s smaller closure rank (11 against 15) buys nothing: it *changes* which letter blocks
fail, it does not remove them.

### 3.3 `L̃`, the desingularised order-4 operator `[MEASURED]`

Step 3 of the brief, and it is cheap because `L̃` is a *left multiple*:
`[VERIFIED, ν = 3,5,8,11, exact ℚ]` `L̃ = const·( a₀·L_BZ|_{ν−1} + a₁·L_BZ|_ν )` with
`(a₀,a₁) ∝ (−λ(ν), 1)`, `λ` as in `PHASE2_NUCLEUS` §3.3 — so `L̃ = A·L_BZ` with `A` of
order 1, and it sits inside the `m = 4` slice of the predecessor's own family
(`work/z5rep/ltilde.py`).

Running the free-weight scan with the `a`-direction **fixed to `L̃`'s**, at `n = 9, 11, 13`:

```
   dim W_tel(L̃, n) = 37   at every n   —  IDENTICAL to L_BZ's,
   ŵ₃ ∉ W_tel(L̃),  ŵ₃^sym ∉,  ṽ ∉,  ṽ^sym ∉,   ŵ₃ ∈ W_tel(L̃) + K.
```

**`L̃` admits exactly the same weights as `L_BZ` and no more.** It is not a telescoper of
`T·ŵ₃` or of `T·ṽ`, and going to order 4 through `L̃` gains nothing. (Consistent with
`Z5CF_TELESCOPER` §3's `m = 4` zero, and now with a much larger ansatz and a fixed direction.)

### 3.3a The `Z5CF_EPSILON` pencil is a LINE inside the space searched here `[MEASURED]`

The ε-deformation report exhibits a pencil of weight-3 closed forms for `P̂` along
`{α₁+α₂+α₃ = 0}`, with `ŵ₃^sym` at the `Ψ`-point and the explicit `α`-letter point

```
   P̂_n = Σ T·[ 4H⁽³⁾_n − (H⁽³⁾_k+H⁽³⁾_l) − ½(H⁽³⁾_{n+k}+H⁽³⁾_{n+l})
                + α·( (H⁽²⁾_k−H⁽²⁾_l) − ¼(H⁽²⁾_{n+k}−H⁽²⁾_{n+l}) ) ],   α = A₁(k)−A₁(l).
```

Re-checked here against the independent design matrix of §2:

| check | result |
|---|---|
| the pencil member lies in the span `V` of §1.1 (21 monomials) | **yes** |
| `Σ T·(pencil member) − P̂`, `n = 0…220`, `p₁` | **0 nonzero rows** — it is a representative |
| `(pencil member) − ŵ₃^sym` lies in `K` | **yes** |
| pencil member ∈ `W_tel` (all 18 letter blocks close at order 3) | **no** |

So **the whole pencil is a 1-parameter line inside the 58-dimensional `K` characterised in
§2**, and the search reported here is not "scan the pencil" but "scan the entire
representative space", of which the pencil is a line. The line does not meet `W_tel`; the
space does. This is the reason the free-weight formulation of §1 was worth building: a
one-parameter family would have been scanned and found empty.

*(No conflict with `Z5CF_EPSILON`'s "the `k↔l`-symmetric weight space is excluded by an
irreducible cubic": that statement is about the symmetric locus of the **ε-deformation**
cascade, a different object from the symmetric **representatives** of `P̂`. Symmetric
representatives certainly exist — `ŵ₃^sym` is one, `[VERIFIED]` here at `n = 0…220` — and
§3.4 records that the successful family contains a symmetric member.)*

### 3.4 On the symmetrisation hypothesis

`W_tel` **is** stable under `k↔l` (as it must be: `T` is symmetric and the whole system is
`σ`-equivariant with `ρ ↔ σ`), and the 16-dimensional admissible family **does contain a
symmetric member** `[MEASURED]`. But `ŵ₃^sym` is not in it, and neither is `ṽ^sym`. So:
*symmetry is compatible with order 3 but is not what causes it* — the working representatives
differ from `ŵ₃` by symmetric elements of `K`, not only by the antisymmetric part.

---

## 4. The certificate `[VERIFIED]`

### 4.1 The gauge freedom, and why it was the last obstacle

Solving the blocks in decreasing degree and taking the *canonical* solution in each letter
block throws away `dim ker(Msc)` directions per block — trivial pairs (`curls`)
`ĝ_kρ(k+1,l) − ρ + ĝ_lσ(k,l+1) − σ = 0` which still solve that block but **change the `()`
block's right-hand side**. In the canonical gauge the `()` block closes at every individual
`n` but for an `n`-*dependent* member of the family (`family.py`: 7-dimensional `λ`-space at
each of `n = 9, 11, 13`, pairwise intersections 6-dimensional and inside `λ₀ = 0`) — a clean
false negative. The same behaviour at slack 22 as at slack 16, so it is not an ansatz effect.

Offering those `18 × 324 = 5832` gauge directions to the `()` block (`joint.py`: one
elimination of `[Msc₀ | G]`, `7290` columns × `9685` rows, ratio 1.33) changes the answer:

| `n` | 9 | 11 | 13 | 17 |
|---|---|---|---|---|
| `λ`-directions of 17 | 13 | 13 | 13 | 13 |
| cumulative `∩` | **13** | **13** | **13** | **13** |
| contains `λ₀ ≠ 0` (i.e. an actual representative) | **YES** | **YES** | **YES** | **YES** |

The intersection does not drop — the condition is `n`-independent. *(Recorded because it is
the trap: `rank[Msc₀|G] = 1164` against `rank Msc₀ = 1058`, so the 5832 gauge columns add only
**106** dimensions — exactly the "nearly useless" the predecessor measured at §3.3 — and yet
those 106 are the entire difference between NO and YES.)*

### 4.2 The representative

The canonical member of the family, rationally reconstructed from `p = 4194301`
(denominators `{1,2}`, `work/z5rep/rationalise.py`) and then re-derived independently in
closed form (`work/z5rep/wstar.py`, which checks it monomial-by-monomial against the fit):

```
   U  =  H_k − ½( H_{n−k} + H_n + H_{n+k+l} − H_{n+l} )
   V  = −½( H_k + H_l − H_{n−k} − H_n + H_{n+k} − H_{n+k+l} )

   w★ =  H⁽³⁾_k  +  U·( H⁽²⁾_k + H⁽²⁾_n + H⁽²⁾_{n+k} − H⁽²⁾_{n−l} )  +  V·( H⁽²⁾_l − H⁽²⁾_k )
```

29 monomials, 13 symbols, **shift closure `J = 42`**. Note `H⁽³⁾_k` — the Apéry `ζ(3)` letter,
which `ZETA5_CLOSEDFORM` §0 identified as the thing every *difference*-alphabet search misses.
`w★` is one member of a **12-dimensional affine family**; no attempt was made to minimise its
support or its closure (§6.2).

### 4.3 Verification table

| what | scope | cells | failures |
|---|---|---|---|
| `Σ T·ṽ = P̂` exact ℚ | `n = 0…20`, every `(k,l)` | 1771 cells | **0** |
| `Σ T·ŵ₃ = P̂` exact ℚ | `n = 0…20` | 1771 | **0** |
| `L_BZ·(Σ T·ṽ) = 0` exact ℚ | `n = 0…17` | 18 | **0** |
| **`Σ T·w★ = P̂` exact ℚ** | `n = 0…20`, every `(k,l)` | **1771** | **0** |
| **`L_BZ·(Σ T·w★) = 0` exact ℚ** | `n = 0…17` | 18 | **0** |
| `w★` closed form == fitted vector | all 109 coefficients | 109 | **0** |
| `dim K = 58`, rank 51 | `n = 0…220`, `p ∈ {4194301, 4194287}` | 442 rows | consistent |
| `Σ T·ŵ₃^anti = 0` | `n = 0…220` | 221 | **0** |
| letter blocks `W_tel(n) = 37` | `n = 9,11,13,17` × 2 primes | — | stable |
| ansatz calibration (`h2_pk` ✓ / `h1_k` ✗ for `ŵ₃`) | every run | — | as predecessor |
| control weight `w = 1`, full cascade incl. `()` | every run | — | closes |
| **full certificate, all 42 blocks, FRESH points** | `(9, p₁)` | 400 × 109 = **43 600** | **0** |
| **same** | `(11, p₁)` | **43 600** | **0** |
| **same** | `(13, p₁)` | **43 600** | **0** |
| **same** | `(9, p₂)` | **43 600** | **0** |
| **same** | `(11, p₂)` | **43 600** | **0** |
| **total** | 5 runs, 2 primes, 3 values of `n` | **218 000** | **0** |

`p₁ = 4194301`, `p₂ = 4194287`. The 400 verification points were never seen by any
elimination, and every component is recomputed from the shift matrices and cofactor values
from scratch. Nothing is claimed over `ℚ(n,k,l)` that was not seen at two primes.

*(The residual verification is done over the full 109-monomial basis; the 67 components
outside `w★`'s own 42-element closure are identically zero on both sides, which is itself a
consistency check on the bookkeeping.)*

---

## 5. What changes in `lean/ZetaLucas/BZClosedForm.lean`

1. **The `sorry` at line 660 stays exactly where it is and keeps its statement shape.** It is
   `bz_creative_telescoping` for the `P̂` row, `L_BZ` order 3 — the operator already in the
   file. Nothing about `cc0…cc3` changes; `cc3 n = 2(n+3)⁵(2n+5)·a0P n > 0` remains the whole
   non-degeneracy argument, three lines.
2. **The weight changes.** `w3h n k l` must be redefined as `w★` (§4.2) — 13 symbols, all
   already in the §5.3 shift table plus `H⁽²⁾_n, H⁽²⁾_k, H⁽²⁾_l, H⁽¹⁾_n, H⁽¹⁾_{k+l},
   H⁽¹⁾_{n+k+l}`, each with the same `Harm_succ` / `Bd_succ_*` lemmas and **no `k ≤ n` side
   conditions**. The Lean statement of Theorem B should continue to be stated for `ŵ₃`; the
   two agree because `w★ − ŵ₃ ∈ K`, which needs its own (short) Lean lemma — see §6.3.
3. **`J` goes from 15 to 42** identities closable by `ring`, and the base is `Φ₃`
   (`T_shift_n3` direction) exactly as §5.2 already specifies. No `(n+j−k)` denominators are
   needed anywhere.
4. **Deleted:** everything the order-7 route would have required — the order-4 operator `A`,
   its degree 49–55 coefficients, the second forward induction on `X_n = (L_BZ·P̂)_n`, the
   four extra initial values, and the `a₄(n) ≠ 0` obligation.

`work/z5rep/CERT_w3star.json` holds the weight, the 42-element monomial basis with explicit
symbol multisets, the normalisation used, and the verification record, in the
`LEAN_Z5_SCAFFOLD` §5.6 machine-readable shape.

---

## 6. Honest status, and the remaining job

### 6.1 What is NOT delivered `[the bounded remainder]`

The 42 cofactor pairs `ρ_j, σ_j` are currently **solutions mod `p` at fixed numeric `n`**, not
elements of `ℚ(n,k,l)`. To meet `LEAN_Z5_SCAFFOLD` §5.4–§5.6 in full still requires:

1. an `n`-sweep (several hundred `n`, 6–8 primes) + rational reconstruction + CRT — the job
   `work/z5la/o_areco.py` already performs for `A(n)`, pointed at the cofactor vectors
   instead. **Far cheaper than the order-7 version**: `A`'s coefficients forced degree ≈ 55
   and hence `≳ 115` values of `n` per prime; here there is no `A` at all, the operator is
   `L_BZ` itself, and the cofactors are built only from `r_Q` and `w★`;
2. **(B-bot)**: `ρ_j(n,0,l) = 0`, `σ_j(n,k,0) = 0` was *not* imposed (`force_k = force_l = 0`
   throughout). It must be re-imposed as `k | N_ρ`, `l | N_σ` in the ansatz and the solve
   repeated — the predecessor did exactly this at order 7 and it cost nothing there;
3. **(B-top)** is free by the same argument as `Z5CF_TELESCOPER` §4.1: `Φ₃(n, n+4, l) = 0` and
   the `F1` denominators are products of `(k+1),(l+1),(k+l+j),(n+k+j),(n+l+j),(n+k+l+j)`, all
   strictly positive for `n,k,l ≥ 0`;
4. the exact-ℚ residual spot check at `n,k,l ≤ 6` of §5.6(3), which needs (1) first.

### 6.2 What was not attempted

* **Minimising `w★`.** It is the canonical (pivot-order) member of a 12-dimensional affine
  family. A member with smaller support, or fewer symbols, or a smaller closure than 42 may
  well exist, and every monomial removed is one fewer Lean identity. This is a cheap,
  well-posed follow-up: minimise support/closure over a 12-dimensional affine space with the
  machinery already in `work/z5rep/`.
* **Weight 5.** The same free-weight method applies verbatim to the `P` row and is now the
  obvious next target; `Z5CF_TELESCOPER` §6's advice to "scan weight 5 at order 7 first"
  should be replaced by "run the free-weight scan at order 3 first".
* **Degree-3 monomials** `H⁽¹⁾H⁽¹⁾H⁽¹⁾` in the weight span (§1.1), and the gauge freedom of
  the 90 *maximal* blocks (Theorem R's particular solution was used there). Both are
  restrictions that could only *enlarge* the admissible family — they cannot invalidate the
  YES.

### 6.3 The soundness chain, stated

```
   Σ_{k,l} T·w★ = P̂        [VERIFIED exact ℚ, n = 0…20]  — and it is an identity in K,
                             so a Lean proof needs  Σ T·(w★ − ŵ₃) = 0 , which is
                             45 antisymmetric generators (free, by k↔l relabelling —
                             one `Finset.sum_comm`) plus at most 13 symmetric ones.
   L_BZ·(T w★) = Δ_k R + Δ_l S   [VERIFIED mod p, 218 000 fresh identities, 2 primes, n=9,11,13]
   (B-top), (B-bot)               [(B-top) VERIFIED; (B-bot) TO BE RE-IMPOSED, §6.1]
   ⟹  L_BZ · P̂ = 0.
```

`w★ − ŵ₃` decomposes over `K`'s measured basis; if the symmetric part of that decomposition
is nonzero, those generators must be proved in Lean too. **Check this before committing** —
if `w★` can be moved inside the family so that `w★ − ŵ₃` is *purely antisymmetric*, the whole
step is one `Finset.sum_comm`. That is the single highest-value item on §6.2's minimisation
list.

---

## 7. Files (`work/z5rep/`)

| file | what |
|---|---|
| `bare.py` | the nine-symbol bare alphabet, weight-3 spans, divisibility closure, up-sets, `σ`-symmetrisation, `ŵ₃`/`ṽ` as elements |
| `sumrows.py` | the sum-map design matrix, `K`, the `P̂` row |
| `frw.py` | **the free-weight scan** — point data over the extended alphabet, the `A_L` columns, the admissible-weight extraction |
| `scanN.py`, `run_frw.py`, `multi.py` | drivers; intersection of `W_tel(n)` over `n`; comparison with `K` |
| `cert.py` | the full cascade for a given weight + fresh-point verification of all `J` components |
| `family.py` | the `()` block over the whole representative family (canonical gauge) |
| `joint.py` | **the joint solve with the letter blocks' trivial-pair gauge freedom** — this is what turned the NO into a YES |
| `verify_full.py` | the definitive end-to-end build + fresh-point verification |
| `extract.py`, `tight.py` | candidate extraction; minimal-ansatz measurement |
| `ltilde.py`, `ltest.py` | `L̃` in the `A·L_BZ` family, verified; the `L̃` scan |
| `rationalise.py`, `wstar.py` | rational reconstruction; **the closed form of `w★` and its exact ℚ verification** |
| `vt_exact.py` | exact ℚ verification of `ṽ`, `ŵ₃` against `ladder_w3.pkl` |
| `CERT_w3star.json`, `wjoint_p4194301_Q.json` | the deliverables, machine-readable |
| logs | `scanN_m3_s16.log`, `scanN_p2.log`, `ltest_s16.log`, `family_multi.log`, `family_s22.log`, `joint_multi.log`, `vfull_p1.log`, `vfull_p2.log` |

Reproduction:

```bash
cd /home/ubuntu/fable-episode-2/zeta-math-2/work/z5rep
python3 vt_exact.py 20                       # v-tilde and w3hat are representatives (exact Q)
python3 sumrows.py 220 2                     # K:  dim 58, rank 51
python3 scanN.py 9,11,13,17 3 F1 16          # W_tel = 37, w3hat in W_tel + K
python3 ltest.py 9,11,13 F1 16               # L-tilde: identical admissible set
python3 joint.py 9,11,13,17 8 10             # the 13-dim lam-space, lam_0 != 0 at every n
python3 wstar.py 20                          # w* closed form, exact Q
python3 verify_full.py wjoint_p4194301.npy 9,11 8 10          # 43600 fresh identities each
python3 verify_full.py wjoint_p4194301.npy 9    8 10 4194287  # second prime
```

No RISC package, no Wolfram kernel, no Gröbner engine. Everything is linear algebra over
`ℚ(n,k,l)` reduced mod large primes.

---

## 8. Do not re-run

* any order-`≤6` search for `A·L_BZ` at weight 3 **with the weight fixed to `ŵ₃`**
  (`Z5CF_TELESCOPER` §3.1 — still correct, and now beside the point);
* `ṽ`, `ŵ₃^sym`, `ṽ^sym` at order 3 (§3.2, excluded with bounds);
* `L̃` as a telescoper of `T·ŵ₃` or `T·ṽ` (§3.3, excluded — same admissible set as `L_BZ`);
* the `()` block in the **canonical gauge** (§4.1 — it gives a reproducible false negative);
* any ansatz for this alphabet omitting `(k+l+3)` or `(n+k+l+j)`.
