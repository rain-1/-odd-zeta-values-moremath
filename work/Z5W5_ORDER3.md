# Z5W5_ORDER3 — **NO.** At weight 5 the whole degree-≤3 bare representative space is excluded at order 3

**Agent:** computational-agent (River's odd-zeta program), 2026-07-26
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, code and data in `work/z5w5/`
**Brief:** repeat the weight-3 breakthrough of `work/Z5CF_REP.md` one weight up — find a
representative `w` of the `P` row with `Σ_{k,l} T·w = P_n` for which `L_BZ` itself is a
telescoper of `T·w`, and produce the certificate; or exclude one in a stated space.
**Predecessors:** `work/Z5CF_REP.md`, `work/Z5CF_TELESCOPER.md`, `work/ZETA5_CLOSEDFORM.md`,
`work/Z5CF_CERT.md`, `work/Z5CF_EPSILON.md`
**Labels:** `[PROVED]` · `[VERIFIED range]` · `[MEASURED]` · `[EXCLUDED with bounds]`

---

## 0. HEADLINE — **NO**, and the exclusion is sharp

**`L_BZ` is not a telescoper of `T·w` for ANY representative `w` of the `P` row in the
nine-symbol bare weight-5 span of degree ≤ 3** — the exact analogue of the space in which
`w★` was found at weight 3 — with cofactors bounded as in §3.

> `[EXCLUDED with bounds]` Let `V` be the ℚ-span of the weight-5 monomials of degree ≤ 3 in
> the bare alphabet `H^(r)_x`, `r = 1…5`, `x ∈ {n, k, l, n±k, n±l, k+l, n+k+l}`, together with
> its divisibility closure: **`J = 1270`** monomials. Then
>
> ```
>    { w ∈ V : Σ_{k,l} T(n,k,l) w(n,k,l) = P_n }  ∩  W_tel  =  ∅ ,
> ```
>
> where `W_tel` is the set of `w ∈ V` passing the **261 standalone-block** conditions of the
> order-3 certificate system. `dim W_tel = 449`, the image of `W_tel` under the sum map is
> **209**-dimensional (the full sum map has rank **553**), and the `P` row misses it by
> **292 of 501** independent equations at `p₁` and **492 of 701** at `p₂`. On the
> `k↔l`-symmetric subspace — where the restriction is `[PROVED]` WLOG — the same verdict holds
> at `dim W^sym = 254` against 501/701 rows, i.e. at rows/columns ratio **1.97 / 2.76**.

1. **The verdict is a two-family statement.** No single block family excludes; **two pairs do,
   minimally** `[MEASURED]`:

   | minimal excluding pair | blocks | `dim W` | violated equations |
   |---|---|---|---|
   | `H⁽¹⁾H⁽¹⁾` + `H⁽¹⁾H⁽²⁾` | 45 + 81 | 559 | **234** |
   | `H⁽¹⁾H⁽²⁾` + `H⁽¹⁾H⁽³⁾` | 81 + 81 | 604 | **203** |

   Every single family alone, and every other pair, is consistent (`nbad = 0`). The
   obstruction is a genuine *interaction* between the degree-2 blocks, not one bad block.

2. **The result is ansatz-independent, prime-independent and `n`-independent.**
   `dim W_tel = 449` and the per-block codimensions `(5, 6, 8)` are **identical** at three
   ansatz sizes spanning a factor 5.8 in column count (`nc = 968`, `2738`, `5618`; bidegrees
   `(21,21)`, `(36,36)`, `(52,52)`), at `p = 4194301` and `p = 4194287`, and at
   `n = 13, 17, 23` (§4).

3. **The maximal blocks' gauge freedom does not help** `[MEASURED]` — this is the trap that
   produced the false negative at weight 3, and it was checked here. Offering every standalone
   block the *full* curl freedom of all nine of its maximal multiples (`9·nk` extra columns per
   block, `nk = 225`/`625` for `H0`/`H1`), **as an independent freedom per block — a
   relaxation of the true system** — leaves every codimension unchanged and `dim W_tel = 449`
   (§5). The curls do add rank (`+0 / +59 / +205` for the weight-1/2/3 letter families at
   `H0`), they simply add it in directions orthogonal to the obstruction.

4. **The pipeline returns YES on the weight-3 control, run through the identical code.**
   `work/z5w5/w3control.py` reproduces `Z5CF_REP` exactly: sum-map rank **51**, `dim K = 58`,
   170 excess rows; `dim W_tel = 37`; and the affine representative test **passes with 0
   inconsistency rows**, recovering an explicit weight-3 representative (support 33) in
   `W_tel`. So the weight-5 `NO` is not a bug in the test (§6).

5. **`w₅` itself is rejected by only 22 of the 261 blocks.** The compact form of
   `ZETA5_CLOSEDFORM` is *nearly* order-3-admissible; what fails is that no element of the
   717-dimensional space `K5` of alternative representatives repairs those 22 while keeping
   the other 239 blocks closed.

6. **Where the room actually is** `[MEASURED]`, and it is a two-line computation: in the
   degree-≤**4** span (`J = 3325`) the families `H⁽¹⁾H⁽¹⁾` and `H⁽¹⁾H⁽²⁾` **stop being
   standalone** — they acquire the non-maximal multiples `H⁽¹⁾H⁽¹⁾H⁽²⁾` — and those are
   *exactly* the two families of the minimal excluding pairs. The degree-4 enlargement
   therefore relaxes precisely the conditions that do the excluding. That, and higher
   telescoper order, are the two live directions (§8).

---

## 1. What was searched, exactly

```
   T(n,k,l) = C(n+k,n) C(n,k)² C(n+l,n) C(n,l)² C(n+k+l,n)
   L_BZ = Σ_{i=0}^{3} c_i(n) S_n^i ,   c_i = zla.cc(n)   (order 3, the operator in Lean)
   base  Φ(n,k,l) = T(n+3,k,l) / Π_{j=1..3}(n+j)(n+k+j)(n+l+j)(n+k+l+j)
   gk = (n+3−k)²(n+k+1)(n+k+l+1) / [(k+1)³(k+l+1)]                 (l mirror)
   MIXED base: H^(r)_{n−k}, H^(r)_{n−l} normalised at n+3   (Z5CF_TELESCOPER §2.2)
```

**The space.** Bare alphabet `H^(r)_x`, `r = 1…5`, `x` one of the nine arguments obtained by
differentiating `T`'s five binomials. `V` = all weight-5 monomials of **degree ≤ 3** plus the
divisibility closure:

```
   tops   981 = 9 [H⁵] + 81 [H¹H⁴] + 81 [H²H³] + 405 [H¹H¹H³] + 405 [H¹H²H²]
   J     1270 = 1 + 45 [letters] + 414 [degree 2] + 810 [degree 3]
```

Degree ≤ 3 is forced from below: `ZETA5_CLOSEDFORM` §2.2 excludes weight 5 at degree ≤ 2 in
all nine bare symbols (96 orbit-columns, rank 88, 253 excess equations). It is the exact
analogue of weight 3's degree-≤2 space, and `w₅` (27 monomials, closure 64) lies in it.

**Block structure** `[PROVED, `w5span.blocks`]` — `(S^d)_{ij} ≠ 0` iff `M_i | M_j`, so:

| | count | rôle |
|---|---|---|
| maximal (`= tops`) | **981** | closed form by Theorem R: `r_j = w_j r_Q`, `s_j = w_j s_Q` |
| **standalone** degree-2 blocks | **261** | every strict multiple is maximal → scalar problem, **up-set exactly 10** |
| coupled degree-1 blocks `H⁽¹⁾_x, H⁽²⁾_x, H⁽³⁾_x` | 27 | not used here (see §7) |
| coupling `()` block | 1 | not used here |

The 261 standalone blocks split into five families by the weight of the complementary letter:

| family | blocks | complementary letter | codim of the block condition |
|---|---|---|---|
| `H⁽¹⁾H⁽¹⁾` | 45 | `H⁽³⁾_c` | **8** |
| `H⁽¹⁾H⁽²⁾` | 81 | `H⁽²⁾_c` | **6** |
| `H⁽¹⁾H⁽³⁾` | 81 | `H⁽¹⁾_c` | **5** |
| `H⁽²⁾H⁽²⁾` | 45 | `H⁽¹⁾_c` | **5** |
| `H⁽⁴⁾_x` | 9 | `H⁽¹⁾_c` | **5** |

(`H⁽⁴⁾_x` is the one *letter* block that is standalone; `H⁽⁵⁾_x` is maximal.)

**The method is `Z5CF_REP`'s verbatim.** For fixed `L = L_BZ` the certificate system is linear
in the weight as well as in the cofactors, so the standalone block `M` reads

```
   ĝ_k ρ_M(k+1,l) − ρ_M + ĝ_l σ_M(k,l+1) − σ_M  =  A_M(k,l) · w ,
```

`A_M` known and supported on the 10 coordinates of `up(M)`. Since `Msc` is the **same matrix
for every block**, one elimination of `[ Msc | A_{M₁} | … | A_{M₂₆₁} ]` with pivots restricted
to the `Msc` columns serves all of them; the rows past the rank give a condition matrix `Z_M`
of at most 10 independent rows, and

```
   W_tel = { w :  Z_M · w|_{up(M)} = 0  for every standalone block M }.
```

---

## 2. The target row, exact `[VERIFIED exact ℚ]`

`work/z5w5/verify5.py`, independent `Fraction` arithmetic from the binomials and the harmonic
numbers, no fitted vectors:

| check | scope | result |
|---|---|---|
| `w₅` as expanded here (27 bare monomials) `==` `zla.weight_element(FQ,'w5')` (independent encoding via the composite letter `S₂` and the tower `H^(r)_{n+k}`) | all cells `n ≤ 6` | 140 cells, **0 discrepancies** |
| `L_BZ · (Σ_{k,l} T·w₅) = 0` | exact ℚ, `n = 0…11` | **0 failures of 12** |
| controls `L_BZ·Q = 0`, `L_BZ·P̂ = 0` | exact ℚ, same range | **0 failures** |
| `rank_ℚ {Q_n, P̂_n, P_n}` | `n = 0…14` | **3** — `P` is the genuine third row |
| `L_BZ · b₅ = 0` mod `p₁`, `b₅ := (Σ T·w₅)_n` | `n = 0…497` | **0 nonzero of 498** |

```
   P_0 = 0        P_1 = 87/4        P_2 = 1190161/384        P_3 = 7682021239/10368
   P_4 = 24943788950905/110592      P_5 = 81875586674776013003/1036800000
```

(`Σ T·w₅ = P_n` itself is `ZETA5_CLOSEDFORM`'s `[VERIFIED against every exact ladder value
n = 0…360, two primes]`; the row is re-derived here only to make the target of the exclusion
explicit and machine-checkable.)

---

## 3. The denominators were MEASURED, not guessed `[MEASURED]`

`work/z5w5/poles5.py`. For one representative block of each of the five families and **every**
column of its `A`-matrix (i.e. every elementary weight direction `e_j` with `M | M_j`), the
right-hand side was reconstructed exactly as a rational function of `k` (with `l` fixed) and of
`l` (with `k` fixed) — 260 consecutive samples per direction, `n = 9`, `p = 4194301`, degree
budget 60 — and the denominator factored against the candidate linear forms. **Zero
unfactored remainder in every one of the 200 reconstructions.**

```
   k-side :  (k+1)³ (k+l+1)⁴ (k+l+2) · Π_{j=1..3} (n+k+j)² (n+k+l+j)² (n+j−k)
   l-side :  mirror
```

Two things worth recording. (a) The maximum multiplicities are **mild** — degrees `(6,10)`
numerator over `(0,4)` denominator per direction. (b) A factor `(n+j−k)` **does** appear, at
multiplicity 1: the mixed base kills the interior poles only up to `Π(n+j−k)²`, and a weight-3
letter `H⁽³⁾_{n−k}` produces `1/(n+j−k)³`, so at weight 5 one power survives. This is the one
place where the weight-5 pole structure differs from `Z5CF_TELESCOPER` §2.2's weight-3
measurement. (It turned out not to matter: the `H0` family below carries **no** `(n+j−k)` at
all and returns the identical answer.)

**The three ansatz families**, all with `force_k = force_l = 0` (no boundary conditions
imposed — the most permissive setting, which is what an exclusion requires):

| name | denominator | base bidegree | slack | bidegree | `nc` |
|---|---|---|---|---|---|
| `H0` | `(k+1)²(l+1)²(k+l+1)²(k+l+2) Π_{j=1..3}(n+k+j)(n+l+j)(n+k+l+j)` | (11,11) | 10 | (21,21) | **968** |
| `H1` | `(k+1)³(l+1)³(k+l+1)⁴(k+l+2)²(k+l+3)(k+l+4) Π_{j=1..3}(n+k+j)²(n+l+j)²(n+k+l+j)²(n+j−k)(n+j−l)` | (26,26) | 10 | (36,36) | **2738** |
| `H2` | `(k+1)⁴(l+1)⁴(k+l+1)⁵(k+l+2)³(k+l+3)²(k+l+4)(k+l+5) Π_{j=1..4}(n+k+j)³(n+l+j)³ Π_{j=1..3}(n+k+l+j)³ Π_{j=0..4}(n+j−k)(n+j−l)` | (42,42) | 10 | (52,52) | **5618** |

---

## 4. The scan `[MEASURED]`

`work/z5w5/scan5.py`. Rows always `≥ 1.40 · nc` (the §DISCIPLINE ratio; the smallest ratio in
any run reported is **1.47**).

| `n` | 9 | 11 | 13 | 17 | 23 | cumulative |
|---|---|---|---|---|---|---|
| `dim W_tel(n)`, `H1`, `p₁` | 465 | 465 | **449** | **449** | **449** | **449** |
| codim histogram | `{5:216, 8:45}` | same | `{5:135, 6:81, 8:45}` | same | same | — |

`n = 9, 11` are small-`n` accidents (they give *more* freedom, i.e. fewer conditions); from
`n = 13` on the condition is `n`-independent.

### 4.1 The ansatz ladder and the built-in adequacy calibration

The signature of an inadequate ansatz in this formulation is unmistakable and was carried in
every run: if nothing is admissible the block condition has codimension **equal to its up-set
size, 10** (`Z5CF_REP` §3.1's "dim 99 = 109−10"). It never happened — `0 of 261` blocks are
dead in any run.

| ansatz | `nc` | bidegree | `rank(Msc)` | codim histogram at `n = 13` | `dim W_tel` |
|---|---|---|---|---|---|
| `H0` | 968 | (21,21) | 743 | `{5:135, 6:81, 8:45}` | **449** |
| `H1` | 2738 | (36,36) | 2113 | `{5:135, 6:81, 8:45}` | **449** |
| `H2` | 5618 | (52,52) | 4249 | `{5:216, 8:45}` at `n=13`; `{5:135,6:81,8:45}` at `n=17` | **449** (cumulative) |
| `H1`, `p₂ = 4194287` | 2738 | (36,36) | 2113 | `{5:135, 6:81, 8:45}` | **449** |

A factor **5.8** in column count and **2.5** in bidegree changes nothing. The one difference —
`H2` at `n = 13` giving 81 blocks codim 5 instead of 6 — disappears at `n = 17` and does not
survive the intersection over `n`.

### 4.2 The affine representative test

`work/z5w5/affine.py`, `work/z5w5/sum5.py`. The sum map `A5[n, j] = Σ_{k,l=0}^{n} T·M_j` mod
`p` was built for `n = 0…500` at `p₁` and `n = 0…700` at `p₂`. The question is whether some
`w ∈ W_tel` reproduces the `P` row, i.e. `A5 · w = b₅`.

| | `p₁ = 4194301` | `p₂ = 4194287` |
|---|---|---|
| rows of `A5` | 501 | **701** |
| rank of the sum map on `V` | ≥ 501 (row-saturated) | **553** (148 excess rows) |
| `dim K5` | ≤ 769 | **717** |
| `dim W_tel` | 449 | 449 |
| `dim A5(W_tel)` | **209** | **209** |
| `dim (W_tel ∩ K5)` | 240 | 240 |
| **violated equations `nbad`** | **292** of 501 | **492** of 701 |
| verdict | **NO** | **NO** |

The failure is not marginal — it is as large as it can be: *every* one of the `rows − 209` rows
past the rank carries a nonzero residual, at both primes. Note also
`dim K5 = 717 = 573 + 144`: the 573 `k↔l`-antisymmetric directions are in `K5` `[PROVED]` by
`T(n,k,l) = T(n,l,k)` and `[VERIFIED]` here (0 nonzero of 573 × 701), and 144 further
dimensions are genuinely symmetric relations among the `Σ T·(monomial)` sums.

### 4.3 Which blocks do it — the minimal excluding subsets `[MEASURED]`

`work/z5w5/subsets5.py`, all 31 non-empty subsets of the five families, conditions intersected
over `n = 13, 17`:

| subset | blocks | `dim W` | `dim A5(W)` | nbad | verdict |
|---|---|---|---|---|---|
| `(1,1)` | 45 | 910 | 420 | 0 | YES |
| `(1,2)` | 81 | 919 | 406 | 0 | YES |
| `(1,3)` | 81 | 955 | 451 | 0 | YES |
| `(2,2)` | 45 | 1045 | 430 | 0 | YES |
| `(4)` | 9 | 1225 | 501 | 0 | YES |
| **`(1,1) + (1,2)`** | 126 | 559 | 267 | **234** | **NO — minimal** |
| `(1,1) + (1,3)` | 126 | 875 | 407 | 0 | YES |
| `(1,1) + (2,2)` | 90 | 685 | 294 | 0 | YES |
| `(1,1) + (4)` | 54 | 865 | 393 | 0 | YES |
| **`(1,2) + (1,3)`** | 162 | 604 | 298 | **203** | **NO — minimal** |
| `(1,2) + (2,2)` | 126 | 844 | 361 | 0 | YES |
| `(1,2) + (4)` | 90 | 874 | 379 | 0 | YES |
| `(1,3) + (2,2)` | 126 | 730 | 325 | 0 | YES |
| `(1,3) + (4)` | 90 | 910 | 424 | 0 | YES |
| `(2,2) + (4)` | 54 | 1000 | 403 | 0 | YES |
| … | | | | | (all supersets of a NO are NO) |
| **all 261** | 261 | **449** | **209** | **292** | **NO** |

Notably `(1,1) + (1,3) + (2,2) + (4)` — 252 of the 261 blocks — is still **consistent**. The
family `H⁽¹⁾H⁽²⁾` is in every minimal excluder.

### 4.4 The same analysis on the `k↔l`-symmetric subspace — and why it is WLOG

`W_tel`, `K5` and the affine set are all `σ`-stable: `T(n,k,l) = T(n,l,k)`, and the certificate
system is `σ`-equivariant with `ρ ↔ σ` (if `L(Tw) = Δ_kR + Δ_lS` then
`L(Tσw) = Δ_k(σS) + Δ_l(σR)`). So a non-empty intersection contains a symmetric point:
**restricting the search to the symmetric subspace is `[PROVED]` WLOG**, and it halves the
width — `1270` monomials, `697` `σ`-orbits — which is what makes the rows/columns discipline
affordable on every subset verdict. `work/z5w5/subsym5.py`:

| subset | `dim W^sym` | rows/`dim W` | `dim A5(W)` | nbad | verdict |
|---|---|---|---|---|---|
| `(1,1)` | 499 | 1.00 | 420 | 0 | YES |
| `(1,2)` | 511 | 0.98 | 406 | 0 | YES |
| `(1,3)` | 529 | 0.95 | 451 | 0 | YES |
| `(2,2)` | 571 | 0.88 | 430 | 0 | YES |
| `(4)` | 670 | 0.75 | 501 | 0 | YES |
| **`(1,1)+(1,2)`** | 313 | **1.60** | 267 | **234** | **NO — minimal** |
| `(1,1)+(1,3)` | 485 | 1.03 | 407 | 0 | YES |
| `(1,1)+(2,2)` | 373 | 1.34 | 294 | 0 | YES |
| `(1,1)+(4)` | 472 | 1.06 | 393 | 0 | YES |
| **`(1,2)+(1,3)`** | 343 | **1.46** | 298 | **203** | **NO — minimal** |
| `(1,2)+(2,2)` | 493 | 1.02 | 388 | 0 | YES |
| `(1,2)+(4)` | 484 | 1.04 | 379 | 0 | YES |
| `(1,3)+(2,2)` | 403 | 1.24 | 325 | 0 | YES |
| `(1,3)+(4)` | 502 | 1.00 | 424 | 0 | YES |
| `(2,2)+(4)` | 544 | 0.92 | 403 | 0 | YES |
| `(1,1)+(1,3)+(2,2)+(4)` | 332 | **1.51** | 254 | 0 | YES |
| **ALL 261 standalone blocks** | **254** | **1.97** (`p₁`) / **2.76** (`p₂`) | **209** | **292** / **492** | **NO** |

Identical verdicts and identical `nbad` to the full-space table. **The verdict that matters —
all 261 blocks — has `rows / dim W = 1.97`, comfortably above the 1.3 discipline**, as do the
two minimal excluders (1.60, 1.46) and the largest consistent subset
(`(1,1)+(1,3)+(2,2)+(4)`, 252 of the 261 blocks, 1.51). The single-family and some pair
**YES** entries sit at ratio 0.75–1.24 with 501 rows and are recorded as such; they are
*consistency* verdicts, i.e. exactly the kind the discipline says to distrust, and they bear
only on the *minimality* claim, never on the exclusion.

---

## 5. The maximal blocks' gauge freedom — checked, and it does not help `[MEASURED]`

This is the step that turned the weight-3 answer from NO to YES (`Z5CF_REP` §4.1: 5832 gauge
columns of rank 106 were the entire difference), so it was checked before any verdict was
recorded.

Theorem R fixes a maximal block's cofactor pair only up to a **curl**
`(ρ,σ)` with `ĝ_kρ(k+1,l) − ρ + ĝ_lσ(k,l+1) − σ = 0`, i.e. up to `ker(Msc)`. Its contribution
to the equation of a standalone block `M` with `M·L` maximal is
`ĝ_k inc_k(L) ρ(k+1,l) + ĝ_l inc_l(L) σ(k,l+1)` — it depends only on the **letter** `L`, so one
basis `KR = R₁H_r`, `KS = S₁H_s` of the curl images serves every block and the nine letters of
the complementary weight give `9·nk` extra columns per block.

`work/z5w5/gauge5.py` offers exactly that, treating the freedoms as **independent per block**.
A maximal monomial such as `H⁽¹⁾_aH⁽¹⁾_bH⁽³⁾_c` divides three standalone blocks and in truth
must use one curl for all three, so **this is a relaxation of the true system**: the space
computed here *contains* the true admissible space, and a negative here is a negative for the
true system (within the ansatz bound on the curls).

| ansatz | `nk` | gauge cols/block | complementary letter family | `rank[Msc\|G]` vs `rank Msc` | codim histogram | `dim W_tel^gauge` |
|---|---|---|---|---|---|---|
| `H0`, `n=13`, `p₁` | 225 | 2025 | weight 1 (135 blocks) | 743 → 743 (**+0**) | `{5:135}` | |
| | | | weight 2 (81 blocks) | 743 → 802 (**+59**) | `{6:81}` | |
| | | | weight 3 (45 blocks) | 743 → 948 (**+205**) | `{8:45}` | **449** |
| `H1`, `n=13`, `p₁` | 625 | 5625 | weight 1 (135 blocks) | 2113 → 2163 (**+50**) | `{5:135}` | |
| | | | weight 2 (81 blocks) | 2113 → 2213 (**+100**) | `{6:81}` | |
| | | | weight 3 (45 blocks) | 2113 → 2263 (**+150**) | `{8:45}` | **449** |

Rows in the gauge runs: `11 255` against `2738 + 5625 + 10 = 8373` unknowns (ratio **1.34**).

**Every codimension is unchanged, at both ansatz sizes.** The curls do enlarge the image — by
up to 205 dimensions —
but in directions that are orthogonal to the 5/6/8 obstruction directions of each block. The
`H⁽⁴⁾_x` blocks deserve a separate line: the maximal monomials `H⁽¹⁾_cH⁽⁴⁾_x` in their up-sets
divide **no other standalone block**, so for those nine blocks the gauge treatment is not a
relaxation but **exact** — their condition (codim 5) is unconditional on the gauge.

---

## 6. Controls and verification

### 6.1 The weight-3 control — the decisive one `[VERIFIED]`

`work/z5w5/w3control.py` runs the *identical* code path (`w5span` with `W = 3, maxdeg = 2`,
`pd5`, `scan5`, `sum5`, `affine`) on the weight-3 problem, where the answer is known:

| quantity | this pipeline | `Z5CF_REP` |
|---|---|---|
| `J` | 109 | 109 |
| rank of the weight-3 sum map | **51** (170 excess rows) | 51 (170 excess rows) |
| `dim K` | **58** | 58 |
| standalone blocks | 18 | 18 (the letter blocks) |
| per-block codim (`F1`, slack 16, `n = 9`) | **6** (dim 103 of 109) | dim 103 |
| `dim W_tel` | **37** | 37 |
| affine representative test | **YES, nbad = 0** | `ŵ₃ ∈ W_tel + K`, YES |
| recovered representative | support 33, sum-map residual 0 | `w★`, support 29 (same 16-dim family) |
| `L_BZ · P̂ = 0` from the design matrix | 0 nonzero of 218 | — |

Same code, same discipline, known-positive input → positive output. The weight-5 negative is
therefore a property of weight 5, not of the test.

### 6.2 Full verification table

| # | statement | scope | cells | failures |
|---|---|---|---|---|
| V1 | `w₅` (27 bare monomials) `==` `zla`'s independent `w5` | exact ℚ, all cells `n ≤ 6` | 140 | **0** |
| V2 | `L_BZ·(Σ T·w₅) = 0` | exact ℚ, `n = 0…11` | 12 | **0** |
| V3 | controls `L_BZ·Q = 0`, `L_BZ·P̂ = 0` | exact ℚ, `n = 0…11` | 24 | **0** |
| V4 | `rank{Q,P̂,P} = 3` | exact ℚ, `n = 0…14` | 15 rows | rank 3 |
| V5 | `L_BZ·b₅ = 0` (`b₅` = design-matrix row) | mod `p₁` `n = 0…497`, mod `p₂` `n = 0…697` | 1196 | **0** |
| V6 | antisymmetric subspace ⊂ `K5` | 573 directions × (501 + 701) rows | 688 746 | **0** |
| V7 | `dim W_tel = 449`, codims `(5,6,8)` | `n = 13,17,23`, `H0/H1/H2`, `p₁,p₂` | 8 runs | consistent |
| V8 | 0 blocks dead (codim = `\|up\|`) | every run | 261 × 8 | **0 dead** |
| V9 | denominator reconstruction, no unfactored remainder | 5 families × 10 directions × 2 variables | 200 | **0** |
| V10 | maximal-curl gauge leaves codims unchanged | `H0` and `H1`, all three families, `n = 13` | 261 + 261 | **0 changes** |
| V10b | `dim W_tel^gauge = dim W_tel = 449` | `H0`, `H1`, `n = 13`, `p₁` | 2 runs | equal |
| V12b | same verdicts on the symmetric subspace (`dim Sym = 697`) | 21 subsets | 21 | identical `nbad` |
| V14 | degree-≤4 scan, 705 standalone blocks | `n = 13, 17`, `p₁`, `H1` | 1410 | 0 dead, `dim W_tel = 1315` |
| V11 | **affine test fails** | `A5` 501 rows (`p₁`) / 701 rows (`p₂`), `dim W_tel = 449` | 292 / 492 violated | — |
| V12 | minimal excluding pairs | 31 subsets × (`n = 13,17`) | 31 | 2 minimal |
| V13 | weight-3 control passes | `n = 9`, `F1` slack 16, `N = 220` | — | **YES** |
| V15 | **affine test fails on the symmetric subspace too**, ratios 1.97 / 2.76 | `dim W^sym = 254`, 501/701 rows, both primes | 292 / 492 violated | — |
| V16 | `T·w₅` has no order-3 and no order-4 telescoper `A·L_BZ` | `n = 9`, `p₁`, calibration passing | 2 orders | 0 directions |

`p₁ = 4194301`, `p₂ = 4194287`. Nothing is claimed over `ℚ(n,k,l)` that was not seen at two
primes.

---

## 7. Exactly what is, and is not, excluded

**Excluded** `[EXCLUDED with bounds]`:

> There is no `w` in the nine-symbol bare weight-5 span of degree ≤ 3 (`J = 1270`) with
> `Σ_{k,l} T·w = P_n` for which the **261 standalone-block equations** of `L_BZ·(T w) = Δ_k R + Δ_l S`
> are solvable with cofactors `ρ_M, σ_M ∈ N/D`, `D ∈ {H0, H1, H2}` and `deg N ≤ (52,52)`, and
> the maximal blocks' curls likewise bounded — at `n = 13, 17, 23` and `p ∈ {4194301, 4194287}`,
> with the sum-map side carried to 501 rows at `p₁` and **701 rows at `p₂`** (the sum map's
> rank on `V` is **553**, so the row count is 148 past saturation).

**Not excluded** — the four honest gaps, in decreasing order of promise:

1. **Degree-4 weights.** `V` was capped at degree 3, the exact analogue of weight 3's degree-2
   cap and the degree at which `ZETA5_CLOSEDFORM` found `w₅`. In the degree-≤4 span
   (`J = 3325`, tops 2466) the standalone families become
   `{(1,1,2): 405, (1,1,1): 165, (1,3): 81, (2,2): 45, (4): 9}` — and `H⁽¹⁾H⁽¹⁾` and
   `H⁽¹⁾H⁽²⁾`, **the two families of the minimal excluding pairs**, drop out of the standalone
   set entirely (they acquire the non-maximal multiples `H⁽¹⁾H⁽¹⁾H⁽²⁾`, and become *coupled*
   blocks). The enlargement relaxes precisely the conditions that exclude.
   **Measured** `[MEASURED]`, `H1` slack 10, `p₁`, `n = 13` and `n = 17`, 705 standalone
   blocks, up-sets still exactly 10, 0 dead blocks:
   `dim W_tel(deg ≤ 4) = 1315` of `J = 3325`, codim histogram `{5: 540, 6: 165}` — **no
   codim-8 blocks at all**, the `H⁽¹⁾H⁽¹⁾` obstruction is simply not tested any more. The
   affine test there needs a sum-map design matrix at `J = 3325` with `≳ 1.3 × 1315` rows
   (or `≳ 1.3 × 660` on the symmetric subspace), which is the one piece of new work.
   This is the first thing to try.
2. **Higher telescoper order.** Only `L = L_BZ` (order 3) was tested for the free weight.
   `Z5CF_TELESCOPER` found order 7 for `T·ŵ₃`; there is no reason the weight-5 order should be
   3. The free-weight formulation does not extend verbatim to a free operator (the system
   becomes *bilinear* in `(a, w)`), so the practical scan is: fix an `a`-direction, run the
   weight scan, repeat. **For the one representative we have in closed form the order scan was
   started here** (`work/z5w5/ordw5.py`, §7.1).
3. **An extended alphabet.** Nine bare symbols only. Any `H^(r)_{integer-linear}` has rational
   shifts and would be legitimate.
4. **The coupled cascade was never reached** — and did not need to be. The 27 degree-1 blocks
   and the `()` block impose *additional* conditions, so including them can only make the
   answer more negative. They are also where the cost explodes: 261 standalone gauge blocks
   feeding 28 coupled blocks is `261·nk + 28·nc ≈ 1.6·10⁵` columns, out of reach of this
   machine (12 cores, 15 GB) by two orders of magnitude.

### 7.1 By-product: the telescoper order of `T·w₅` itself `[EXCLUDED with bounds]`

`work/z5w5/ordw5.py` runs `Z5CF_TELESCOPER`'s order scan `L = A·L_BZ`,
`A = Σ_{t=0}^{m−3} a_t S_n^t`, on `zla`'s **58-monomial** closure of `w₅`, restricted to the
**26 standalone blocks** of that closure (`o_scan`'s default block list is wrong for `w₅`:
7 letter blocks and `()` are coupled, so they were dropped — the result is therefore a
*necessary* condition on the `a`-direction, exactly as at weight 3). The block `('u4',)` plays
the rôle weight 3's `('u2',)` played: it is solvable separately for every `t`, so an adequate
ansatz must return dimension exactly `m−2` there.

| `m` | 3 | 4 | 5 |
|---|---|---|---|
| `nc` (`H1`, slack 10) | 2738 | 3528 | 4418 |
| rows / columns | 1.37 | 1.37 | 1.36 |
| calibration `('u4',)`, must be `m−2` | **1 ✓** | **2 ✓** | 0 ✗ |
| telescoper directions | **0** | **0** | — (ansatz too small) |

`[EXCLUDED with bounds]` **No `A·L_BZ` of order 3 or 4 is a telescoper of `T·w₅`**, with
cofactors in `N/H1` of bidegree ≤ (41,41), at `n = 9`, `p = 4194301`, under a passing
per-order calibration. At `m ≥ 5` the `H1` ansatz collapses — the calibration says so, and the
zeros there are artefacts, not results. Raising the slack is the obvious continuation.

---

## 8. What a successor should do next, in order

1. **Run the degree-≤4 scan** (`scan5.run(n, 'H1', 10, maxdeg=4)` — the code already takes
   `maxdeg`; `705` standalone blocks, up-sets still exactly 10, so the elimination is
   `npts × (nc + 7050)` and costs about a minute). The only new work is the sum-map design
   matrix at `J = 3325`, which needs the degree-4 monomial group added to `sum5.design`
   (one more `PP` block, grouping by the first three letters) and `N ≳ 1.3·dim W_tel` rows.
   Use the `k↔l`-**symmetric** reduction to halve the width: `W_tel`, `K` and the affine set
   are all `σ`-stable (`T(n,k,l) = T(n,l,k)`), so a non-empty intersection contains a
   symmetric point — searching the symmetric subspace is `[PROVED]` WLOG.
2. **Finish the `T·w₅` order scan** started in §7.1 — `work/z5w5/ordw5.py` already has the
   26-block standalone partition of `w₅`'s own closure and the `('u4',)` calibration; orders 3
   and 4 are excluded with a passing calibration, and orders 5–7 need a larger slack (the
   calibration collapses at `H1` slack 10 from `m = 5` on). One run per order, `≈ 5–10` minutes
   each. This answers "is the weight-5 order 5, 6, 7 or higher?" for the one representative we
   have in closed form, and it is the cheapest remaining measurement.
3. **Do not re-run** anything in §7's excluded statement: the degree-≤3 nine-symbol space at
   order 3 is closed, with three ansatz sizes, two primes, three values of `n`, the
   maximal-curl gauge, and a passing weight-3 control.
4. **Keep the two calibrations that carried this run**: the codim-`=|up|` dead-block detector
   (built into `scan5.run`, printed every time) and the end-to-end weight-3 control
   (`w3control.py`), which is the only thing that distinguishes "the space is empty" from
   "the code is broken".

---

## 9. Files (`work/z5w5/`)

| file | what |
|---|---|
| `w5span.py` | the nine-symbol weight-5 bare alphabet, degree-≤`d` spans, divisibility closure, the maximal/standalone/coupled partition, `σ`, `w₅` and `ŵ₃` as elements |
| `sum5.py` | the sum-map design matrix `A5[n,j] = Σ T·M_j` mod `p` (exact float64 BLAS via an 11-bit split), `K5`, the `P` row `b₅` |
| `pd5.py` | point data at order 3 (`gk, gl, Pm, inc_n/inc_k/inc_l`, `r_Q`, `QR`), the ansatz families `F1/H0/H1/H2`, `scal_mat`, `evalmats`, `Acols_standalone` |
| `poles5.py` | **exact measurement** of every standalone-block right-hand-side denominator, both variables, all five families |
| `scan5.py` | **the free-weight standalone scan** — one elimination for all 261 blocks, per-block conditions, the dead-block adequacy detector |
| `gauge5.py` | the same scan with the **maximal blocks' curl gauge** offered per block |
| `affine.py` | the affine representative test `{w ∈ W_tel : A5 w = b₅}` |
| `subsets5.py` | the 31-subset analysis and the minimal excluding pairs |
| `subsym5.py` | the same on the `k↔l`-symmetric subspace (697 orbits), where the rows/columns discipline is affordable |
| `verify5.py` | exact-ℚ verification of `w₅`, of `L_BZ·(Σ T·w₅) = 0`, and of `rank{Q,P̂,P} = 3` |
| `ordw5.py` | the order scan `A·L_BZ` for the fixed representative `w₅` on its own 58-monomial closure, with the `('u4',)` calibration |
| `w3control.py` | **the end-to-end weight-3 control** |
| data | `A5_p*.npy`, `b5_p*.npy`, `K5_p*.npy`, `w5vec_p*.npy`, `Wcum_*.pkl`, `Wgauge_*.pkl`, `cond_*.pkl` |
| logs | `sum5_*.log`, `scan_H{0,1,2}s10_p{1,2}.log`, `scan_d4.log`, `gauge_H1s10_p1.log`, `subsets_p1.log`, `ordw5_H1s10.log` |

Reproduction:

```bash
cd /home/ubuntu/fable-episode-2/zeta-math-2/work/z5w5
python3 verify5.py 14                       # exact-Q: w5, the P row, L_BZ
python3 poles5.py 9                         # the measured denominators
python3 sum5.py 500 4194301 9               # the sum map, K5, b5   (~10 min)
python3 sum5.py 700 4194287 9               # second prime, rank 553, dim K5 = 717  (~1 h)
python3 w3control.py 4194301 220            # THE CONTROL: weight 3 must return YES
python3 scan5.py 13,17,23 H1 10 4194301 5 3 _m   # dim W_tel = 449
python3 affine.py Wcum_W5_H1_s10_p4194301_m.pkl        # NO, 292 violated equations
python3 affine.py Wcum_W5_H1_s10_p4194287_p2.pkl 4194287  # NO, 492 violated equations
python3 gauge5.py 13 H0 10 4194301 _H0      # the maximal-curl gauge: unchanged
python3 subsets5.py 4194301 H1 10 13,17     # the minimal excluding pairs
python3 subsym5.py  4194301 H1 10 13,17     # the same on the symmetric subspace
python3 scan5.py 13,17 H1 10 4194301 5 4 _d4     # the degree-<=4 span: dim W_tel = 1315
python3 ordw5.py w5 9 H1 10 3,4,5           # order 3 and 4 excluded for w5 itself
```

No RISC package, no Wolfram kernel, no Gröbner engine — everything is linear algebra over
`ℚ(n,k,l)` reduced mod large primes, plus exact `Fraction` arithmetic for every identity.
