# Z5CF_CERT — certified WZ pair for the NEW compact weight functions

**Agent:** computational-agent (River's odd-zeta program), 2026-07-26
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, artifacts in `work/z5cf/`
**Objects:** the two- and three-term compact weights of `work/ZETA5_CLOSEDFORM.md`
**Labels:** `[PROVED]` · `[VERIFIED range]` · `[MEASURED]` · `[EXCLUDED with bounds]`

---

## 0. HEADLINE

1. **T1, weight 3: `Annihilator[T*ŵ₃]` costs 94 s and < 0.7 GB, 10 generators, rank 15.**
   The previous best direct weight-3 object (`T*ṽ`, 10 symbols) cost **5801 s and 4 GB**.
   That is **62x faster and 6x smaller**, and most of the win is a *method* change, not the
   weight: **never call `Annihilator` on the product.** `T` is hypergeometric (rank 1, 0 s),
   so build `ann = DFiniteTimes[Annihilator[T], Annihilator[w]]` — the harmonic factor is then
   annihilated without a single binomial coefficient in its coefficients. This lever was never
   tried in sessions 1–7 and it applies to every object in the campaign, including `ṽ`.

2. **T1, weight 5: `Annihilator[w₅]` alone TIME-ABORTS at 1800 s, RSS 0.33 → 1.12 GB.**
   Closure 64 was *not* enough — **but the wall is the clock at 1 GB, not memory**, which is
   the opposite signature to every previous weight-5 failure (`F_kk`: OOM at 7.8 GB / 85 min).
   `Annihilator[T*w₅]` is `[NOT MEASURED]`, not `[EXCLUDED]`.

3. **The weight-5 cost law is now pinned, in three measured steps, and it is neither the
   symbol count (§18.2/§18.17) nor the degree nor the module rank.** Every degree-1 piece of
   `w₅` is free **even at 6 distinct symbols** (`Ψ`: rank 7, **1 s**). The degree-2 product
   `α·Ψ` does not return in 1200 s — **and neither does `DFiniteTimes[ann α, ann Ψ]`**, so the
   §2.0 lever does *not* transfer (correction recorded in §2.2c). Bisecting: `α²` and `α·β`
   have **identical input ranks 5 × 5** yet cost **31 s** versus **no return in 900 s**. The
   discriminator is **which letter families the product mixes** — `α` lives in the `n+·` family,
   `β` brings in `n−·`, and only the mixed product fails. **And `ZETA5_CLOSEDFORM` §2.2 already
   proved that no weight-5 representative can avoid that mixing.** So the closure-property route
   is structurally wrong for weight 5, and no rewriting of the weight will rescue it.

4. **T2 did not land at either weight, and two of the three obvious levers are now measured
   shut.** `ct1` is clock-bound (5402 s at 2.0 GB of a 2.8 GB cap). §18.18's diagnosis — shrink
   the basis handed to the next stage — **is excluded here**: `OreGroebnerBasis` over the full
   three-variable algebra ran 2119 s and returned the same 10 generators, same rank 15 and the
   same `LeafCount 5 596 298`, i.e. reduction factor **1.000x** (re-presented but not smaller); `DFiniteTimes` had already
   returned a reduced basis. The single-shot two-delta `CreativeTelescoping` call shape **does
   not exist** in this build (confirmed with messages visible, genuine error). What remains is
   clock, elimination order (`ORD=kl`, in flight) and the linear-algebra route of §7.4.

5. **T3/T4/T5 are done, and validated end-to-end on a certificate that already exists.**
   The whole Lean-ready pipeline — `Φ` base, the four degree-12 `P_i`, the absorption calculus,
   the letter shift table, the regularised singular letter, the four boundary obligations, the
   cleared polynomial identity — was run on the campaign's `[CERTIFIED]` **Q-row** pair in a
   kernel that never loaded RISC. Everything reduces to exactly `0`, the interior poles at
   `k,l = n+1,n+2,n+3` are cancelled **exactly** by `P_0`, `(B-bot)` holds via a `k³` numerator
   factor, and `(B-top)` is free from `Φ(n,n+4,l) = 0`. Delivered as
   **`work/z5cf/Qrow_phicert.m`** in the D1–D5 shape of `LEAN_Z5_SCAFFOLD` §S5.
   **So the gate is now a single RISC elimination, with everything downstream of it already built.**

6. **Independent confirmations worth keeping:** shift-closure **15** and **64** re-measured
   RISC-free (three independent routes agree for `ŵ₃`: predicted 15, `UnderTheStaircase` 15,
   letter-monomial count over the 16 shifts 15); both weights re-checked against the exact
   ladder values inside the RISC kernel *before* any holonomic work (`P̂_n`, `P_n`, `Q_n`,
   `n = 0..3`).

---

## 1. The objects, re-established inside the RISC kernel `[VERIFIED]`

Both weights were re-entered from the closed forms (not from any saved coefficient
vector) and checked **non-circularly** against the exact ladder values before a single
holonomic computation was run:

```
  A_r(x) = H^(r)_{n+x} - H^(r)_x ,     B_r(x) = H^(r)_{n-x} - H^(r)_x
  alpha  = A_1(k) - A_1(l) ,  beta = B_1(k) - B_1(l) ,  Psi = alpha/2 + beta
  S_2    = A_2(k) + A_2(l)
  T(n,k,l) = C(n+k,n) C(n,k)^2 C(n+l,n) C(n,l)^2 C(n+k+l,n)

  w3hat = H^(3)_{n+k} - Psi * H^(2)_{n+k}
  w5    = H^(5)_{n+k} + (1/2)(alpha-beta) H^(4)_{n+k} + (S_2/4 - alpha*Psi/2) H^(3)_{n+k}
```

| check | `w3hat` | `w5` |
|---|---|---|
| `HarmonicNumber` instances | 10 | 23 |
| **distinct symbols** | **8** | **13** |
| `LeafCount[T*w]` | 82 | 162 |
| `Sum_{k,l<=n} T*w`, `n = 0..3` | `0, 101/4, 344923/96, 3710571371/4320` = `Phat_n` | `0, 87/4, 1190161/384, 7682021239/10368` = `P_n` |

`Sum_{k,l<=n} T = 1, 21, 2989, 714549 = Q_n` also re-checked in the same kernel.
The eight / thirteen symbols are exactly

```
  w3hat : H_k, H_l, H_{n-k}, H_{n+k}, H_{n-l}, H_{n+l}, H^(2)_{n+k}, H^(3)_{n+k}
  w5    : the above, minus nothing, plus H^(2)_k, H^(2)_l, H^(2)_{n+l}, H^(4)_{n+k}, H^(5)_{n+k}
```

Note what is **absent**: neither weight contains a `C`-letter (`H_{k+l}`, `H_{n+k+l}`).

---

## 2. T1 — the annihilator measurement `[MEASURED]`

### 2.0 The lever that decided it — **do not call `Annihilator` on the product**

`PHASE2_CERTS` §19 established that the cost of `Annihilator` has two axes: the number of
distinct harmonic symbols *and* the coefficient size. Calling `Annihilator[T*w]` exposes
both at once. But `T` is **hypergeometric** — its annihilator is rank 1, three generators,
`0 s` — so the product can be built by

```
   annT = Annihilator[T,  {S[n],S[k],S[l]}]      (rank 1, 3 generators, 0 s)
   annW = Annihilator[w,  {S[n],S[k],S[l]}]      (the harmonic part ALONE)
   ann  = DFiniteTimes[annT, annW]
```

`annW` never sees a binomial coefficient, so its intermediate coefficients stay small; the
binomials enter only in the last, purely mechanical step. **This is the whole measurement.**

### 2.1 Weight 3 (`w3hat`, 8 symbols, closure 15) `[MEASURED]`

| stage | wall time | generators | rank | peak RSS (external `ps`) |
|---|---|---|---|---|
| `Annihilator[T]` | **0 s** | 3 | 1 | — |
| `Annihilator[w3hat]` | **64 s** | 10 | 15 | < 0.5 GB |
| `DFiniteTimes[annT, annW]` | **30 s** | 10 | **15** | < 0.7 GB |
| **total for `Annihilator[T*w3hat]`** | **94 s** | **10** | **15** | **< 0.7 GB** |

`LeafCount[ann] = 5 596 298`. `UnderTheStaircase` gives rank **15**, which is exactly the
shift-closure `ZETA5_CLOSEDFORM` §3 predicted, and exactly the number of distinct letter
monomials that occur across the 16 shifts `(a,b,c) in {0..3}x{0,1}x{0,1}` (§2.3).

**The comparison that matters.** The best previously-attempted direct weight-3 object was
`T*vtilde` (10 distinct symbols, closure 11, `LeafCount 91`):
`Annihilator` took **5801 s and 4 GB** (`work/lb5/certRFD_lk.log`, 12 generators), and its
`ct1` then memory-aborted at a 9 GB cap. The new weight, at the same `LeafCount` order,
costs **94 s and < 0.7 GB** — a **62x speed-up and a 6x memory reduction**. Most of that is
the `annT (x) annW` factorisation rather than the weight itself, and it is a lever that
applies to `vtilde` too; it was never tried in the earlier sessions.

### 2.2 Weight 5 (`w5`, 13 symbols, closure 64) `[MEASURED — NOT OBTAINED]`

| stage | result |
|---|---|
| `Annihilator[T]` | 3 generators, rank 1, **0 s** |
| `Annihilator[w5]` (harmonic part alone, 13 symbols) | **TIME ABORT at 1800 s**, `MaxMemoryUsed` ≈ 0 GB; external RSS trajectory **0.33 → 1.12 GB over the 1800 s** (≈ 0.026 GB/min, monotone, no sawtooth) |

For comparison, the external RSS trajectory of the weight-3 run over its 94 s annihilator
window was `0.36 → 0.44 → 0.54 → 0.57 → 0.64 GB` (peak **0.64 GB**), and the *failed* weight-3
`ct1` that followed rose to **2.0 GB** and then sat flat there for 80 minutes before the clock
caught it — the classic profile of an expression-swell that is compute-bound, not space-bound.

**This is a clock wall at ~1 GB, not a memory wall** — the first weight-5 object in the
campaign to be stopped that way, and the exact opposite of the `F_kk` signature (OOM at
7.8 GB / 85 min). ⚠ **`Annihilator[T*w5]` is therefore `[NOT MEASURED]`, not `[EXCLUDED]`.**
It was not run to a cap because the strictly easier sub-problem it contains — the harmonic
factor alone, with no binomial coefficients — had already failed to return.

### 2.2b Where the weight-5 clock wall actually is `[MEASURED]` — it is **degree**, not symbol count

Decomposing `w5` into the closure chain of `work/z5cf/z5ann5b.wl`:

```
   w5 = H5[n+k] + (1/2)(alpha-beta)*H4[n+k] + (1/4)*S2*H3[n+k] - (1/2)*alpha*Psi*H3[n+k]
```

| piece | distinct symbols | degree | generators | rank | time |
|---|---|---|---|---|---|
| `H5[n+k]` | 1 | 1 | 3 | 2 | **0 s** |
| `H4[n+k]` | 1 | 1 | 3 | 2 | **0 s** |
| `H3[n+k]` | 1 | 1 | 3 | 2 | **0 s** |
| `alpha - beta` | 6 | 1 | 6 | 5 | **0 s** |
| `S2 = A2(k)+A2(l)` | 4 | 1 | 6 | 5 | **0 s** |
| `alpha` | 4 | 1 | 6 | 5 | **0 s** |
| `Psi = alpha/2 + beta` | 6 | 1 | 6 | 7 | **1 s** |
| **`alpha * Psi`** | **6** | **2** | — | — | **TIME ABORT at 1200 s, ~0 GB** |

Every degree-1 piece is free **even at 6 distinct symbols**; the single degree-2 *product*
`alpha*Psi` — with **no more symbols than `Psi` alone** — does not return in 20 minutes.

> **This sharpens `PHASE2_CERTS` §18.2/§18.17.** The cost driver is not the number of
> distinct harmonic symbols: at fixed 6 symbols, degree 1 costs 1 s and degree 2 costs
> more than 1200 s. What stalls is a **product of two letter-bearing factors**.

### 2.2c ⚠ CORRECTION, and the bisection that locates the wall exactly `[MEASURED]`

An earlier draft of this section claimed the remedy was simply *"build every product with
`DFiniteTimes` instead of `Annihilator`"*. **That is wrong and the measurement refutes it:**

```
   DFiniteTimes[ann alpha, ann Psi]   ->  TIME ABORT after 1200 s, ~0 GB   (13:20:57)
```

exactly like `Annihilator[alpha*Psi]`. `DFiniteTimes` is cheap only when **one factor has
rank 1** — that is why `DFiniteTimes[ann T, ann w3hat]` (rank 1 x rank 15) cost 30 s. The
`annT (x) annW` lever of §2.0 stands, for that reason and no other.

The bisection (`work/z5cf/z5ann5c.wl`, `z5ann5c.log`) then locates the wall precisely:

| product | algebra | rank in | rank out | `LeafCount` out | time |
|---|---|---|---|---|---|
| `alpha * Psi` | **`{S[k]}` only** | 3 x 4 | **9** | 44 922 | **6 s** |
| `alpha * alpha` | `{S[n],S[k],S[l]}` | 5 x 5 | **15** | 513 408 | **31 s** |
| **`alpha * beta`** | `{S[n],S[k],S[l]}` | **5 x 5** | — | — | **TIME ABORT at 900 s, ~0 GB** |
| `alpha * Psi` | `{S[n],S[k],S[l]}` | 5 x 7 | ≤ 35 | — | **> 1200 s** |

### 2.2d The law, third and final version — it is **which letter families the product mixes**

`alpha^2` and `alpha*beta` have **identical input ranks (5 x 5)** and differ by a factor of
**more than 30x** in cost (31 s versus no return in 900 s). So it is not the rank product
either. What separates them is *which alphabets meet*:

```
   alpha = A_1(k) - A_1(l)   uses only the  n+  family :  H_{n+k}, H_k, H_{n+l}, H_l
   beta  = B_1(k) - B_1(l)   brings in the  n-  family :  H_{n-k}, H_{n-l}
```

`alpha * alpha` is a product of a module with **itself** — the result is the symmetric square,
rank 15 rather than 25, and its coefficients stay inside one family. `alpha * beta` mixes the
`n+` and `n-` families, and *that* is what does not close.

> **This lands exactly on the structural note in `ZETA5_CLOSEDFORM` §2.2**, which recorded that
> the weight-5 quadratic *"must mix the `n+.` and `n-.` families, because
> `-alpha*Psi/2 = -alpha^2/4 - alpha*beta/2` genuinely needs both `alpha` and `beta`"* — and
> proved (exact ℚ, 19 columns, 26 excess equations, three sub-alphabets) that **no weight-5
> representative avoids the mixing**. So the very feature that makes the compact weight-5 form
> *exist* is the feature that makes its annihilator expensive. The `alpha*beta` wall is not an
> accident of the representative; it is `[EXCLUDED with bounds]` from being avoidable by any
> choice of weight-5 representative in that search space.
>
> **Consequence: the closure-property route is the wrong tool for weight 5, and no rewriting of
> the weight will fix it.** The three levers left are (i) clock — every wall here is at ~0 GB,
> so a multi-hour run is not obviously hopeless and one is in flight (`z5ann5c.log`, 7200 s on
> `alpha*Psi`); (ii) drop a shift variable — the same product closes in **6 s** in `{S[k]}`
> alone, which is what makes the "eliminate `l` by hand first" reformulation worth designing;
> (iii) **abandon Gröbner engines for linear algebra** — see §7.4, which is now the primary
> recommendation rather than a fallback.

### 2.3 Shift-closure, re-measured independently `[VERIFIED]`

Computed RISC-free, by expanding `W3r[a,b,c]` / `W5r[a,b,c]` (§4) in the `hh` letter basis
over all 16 shifts `(a,b,c) in {0,1,2,3} x {0,1} x {0,1}` and counting distinct monomials:

| weight | distinct letter monomials over the 16 shifts | `ZETA5_CLOSEDFORM` §3 claim | `UnderTheStaircase[ann]` |
|---|---|---|---|
| `w3hat` | **15** | 15 | **15** |
| `w5` | **64** | 64 | — |

Three independent routes to the same number. The 15-element basis for `w3hat` is
```
  1, H_l, H_k, H_{n-k}, H_{n-l}, H_{n+l}, H_{n+k},
  H2_{n+k},  H2_{n+k}*{ H_l, H_k, H_{n-k}, H_{n-l}, H_{n+l}, H_{n+k} },  H3_{n+k}
```
i.e. `1 + 6 + 1 + 6 + 1`. For `w5` exactly 2 of the 64 monomials involve `H2_{n+k}` to
degree 1 and none to higher degree.

### 2.4 T2 — the elimination stages `[MEASURED]`

With the weight-3 annihilator in hand (rank 15), the run went for the telescoper:

| attempt | object | result |
|---|---|---|
| `ct1`, eliminate `l`, on `annS` (`LeafCount` 5 596 298) | rank-15 module | **TIME ABORT at 5402 s**, peak RSS **2.0 GB** — clock-bound, 60 % of the memory cap unused |
| `CreativeTelescoping[ann, {S[k]-1, S[l]-1}, {S[n]}, Support -> ...]` (single-shot two-delta) | same | **rejected in 1 s at every rung `d = 0..5`** — the multi-delta signature does not accept this call shape; a diagnostic re-run with messages visible is in `z5w3b.wl` stage B1 |
| `OreGroebnerBasis[annS, OreAlgebra[S[n],S[k],S[l]]]` (reduce before eliminating) | same | **returned in 2119 s / 2 GB — and changed NOTHING: `LeafCount` 5 596 298 -> 5 596 298, reduction factor exactly `1.000x`, same 10 generators, same rank 15** |
| `CreativeTelescoping[base, {S[k]-1,S[l]-1}, {S[n]}, Support->...]` re-run with messages **visible** | same | **genuine error, not a support miss** — the multi-delta call shape is unavailable in this HolonomicFunctions build |
| `ct1` eliminating `k` (`ORD=kl`) on the same basis, 12000 s clock | same | in flight at hand-off (`z5w3b_kl.log`) |

**So T2 did not land.** The natural diagnosis was §18.18's: the annihilator handed to `ct1`
has `LeafCount 5 596 298` for a module of rank 15 — roughly 370 000 leaves per basis element —
and §18.18 measured that shrinking the basis 39x turned "no return in 37 min" into 500 s.

> ⚠ **That diagnosis is now EXCLUDED for this object, by measurement.** `OreGroebnerBasis` over
> the full three-variable algebra ran to completion in **2119 s** and returned a basis with the
> **same 10 generators, the same rank 15, and the same `LeafCount 5 596 298` to the digit** —
> reduction factor `1.000x`. (The saved files are not byte-identical, so it did re-present the
> terms; it simply achieved no size reduction whatsoever.) `DFiniteTimes` had already handed back a reduced Gröbner basis; the 5.6 M leaves are
> intrinsic to this presentation of the module, not slack that a reduction can remove.
> **So "shrink the basis before eliminating" is not available here**, and the remaining RISC
> levers for weight 3 are clock and elimination order alone.

⚠ **`ct1` is `[NOT MEASURED TO EXHAUSTION]`, not `[EXCLUDED]`.** A time abort at 5402 s with
2 GB of a 2.8 GB cap unused excludes nothing.

---

## 3. T5 — the Lean-ready absorption layer `[PROVED, VERIFIED on a grid incl. degenerate range]`

This is the device that made `work/MINIMAL_FORM_PROOF.md` formalisable in one session:
state every binomial ratio **multiplicatively**, so that no step ever divides and every
identity holds for *all* integer indices, including the degenerate range where both
sides vanish.

### 3.1 Lemma 0 (elementary absorptions) `[PROVED]`

All of the following are instances of `C(N,j+1)(j+1) = C(N,j)(N-j)` and hold for **all**
integers `n, k, l >= 0`:

```
 (E1)  C(n+k+1, n)   (k+1)     = C(n+k, n) (n+k+1)
 (E2)  C(n, k+1)     (k+1)     = C(n, k)   (n-k)
 (E3)  C(n+k+1, n+1) (n+1)     = C(n+k, n) (n+k+1)
 (E4)  C(n+1, k)     (n+1-k)   = C(n, k)   (n+1)
```
`[VERIFIED exactly, n = 0..10, k = 0..14 — 165 cells each, all 0]`

### 3.2 Lemma T (the three shift absorptions for `T`) `[PROVED]`

For all integers `n, k, l >= 0`:

```
 (T-n)  (n+1-k)^2 (n+1-l)^2  T(n+1,k,l) = (n+1)(n+k+1)(n+l+1)(n+k+l+1)  T(n,k,l)
 (T-k)  (k+1)^3 (k+l+1)      T(n,k+1,l) = (n-k)^2 (n+k+1)(n+k+l+1)      T(n,k,l)
 (T-l)  (l+1)^3 (k+l+1)      T(n,k,l+1) = (n-l)^2 (n+l+1)(n+k+l+1)      T(n,k,l)
```

*Proof.* `(T-k)` is `(E1)·(E2)^2·(E1 with k+l for k)`; `(T-l)` is its `k <-> l` mirror;
`(T-n)` is `(E3)·(E4)^2·(E3 with k+l for k)`. ∎

`[VERIFIED exactly on the full grid n = 0..8, k = 0..14, l = 0..14 — 2025 cells per
identity, all 0, and the grid deliberately runs k, l well past n so that the degenerate
range where both sides vanish is covered.]`

### 3.2b The base is `Phi`, **not** `T(n,k,l)` — required, per `LEAN_Z5_SCAFFOLD` §S5.2

An earlier draft of this section proposed normalising on `T(n,k,l)` and clearing
denominators. **That is wrong for the Lean target and the reason is not obvious**: over
the base `T(n,k,l)` the cofactors necessarily have poles at `k = n+1, n+2, n+3`, which are
*interior* points of the telescoping range `0 <= k <= n+4`, and the clearing multiplier
depends on `k` and `l` so it cannot be pulled out of the double sum. In Lean, where
`1/0 = 0`, those poles silently evaluate to `0` and the telescoping identity becomes
**false** rather than erroring. The correct base is

```
  Phi(n,k,l) := T(n+3,k,l) / [ (n+1)(n+2)(n+3) (n+k+1)(n+k+2)(n+k+3)
                               (n+l+1)(n+l+2)(n+l+3) (n+k+l+1)(n+k+l+2)(n+k+l+3) ]
```

every factor of which is strictly positive for `n,k,l >= 0`, so `Phi` has no pole anywhere
in range, and

```
  T(n+i,k,l) = Phi(n,k,l) * P_i(n,k,l),    P_i in Z[n,k,l],  deg P_i = 12,  i = 0,1,2,3
  P_i = prod_{j=1..i} (n+j)(n+k+j)(n+l+j)(n+k+l+j)
        * [ prod_{j=i+1..3} (n+j-k) ]^2 * [ prod_{j=i+1..3} (n+j-l) ]^2
```

with `Phi`'s own two steps
```
  Phi(n,k+1,l) (k+1)^3 (k+l+1) = Phi(n,k,l) (n+3-k)^2 (n+k+1)(n+k+l+1)
  Phi(n,k,l+1) (l+1)^3 (k+l+1) = Phi(n,k,l) (n+3-l)^2 (n+l+1)(n+k+l+1)
```
and `Phi(n,n+4,l) = Phi(n,k,n+4) = 0`. These follow from Lemma T by iteration; they are
`[PROVED]` on the Lean side (`T_shift_k/l/n/n2/n3`, `absorbU`) and were re-derived
independently here — the two derivations agree factor for factor.

**Why this matters.** After substituting `T(n+i,k,l) -> Phi * P_i` and every letter shift
by §3.3, both sides of the certificate are `Phi(n,k,l)` times a `Q(n,k,l)`-linear
combination of the `J` closure monomials (`J = 15` / `64`). Cancelling `Phi` and equating
coefficients gives exactly **`J` polynomial identities in `Q[n,k,l]`**, with no Gamma
function, no limit and no `0/0` anywhere — the shape a Lean agent discharges with `ring`.

### 3.3 The letter layer — the only analytic input `[PROVED]`

Every letter of both weights is a bare `H^(r)_x` with `x` linear in `(n,k,l)`, so the
**only** analytic fact used anywhere below is the defining recurrence

```
  H^(r)_{x+1} = H^(r)_x + 1/(x+1)^r .
```

Its consequences, used verbatim by the RISC-free verifier:

| shift | `H^(r)_{n+k}` | `H^(r)_{n-k}` | `H^(r)_k` | `H^(r)_{n+l}` | `H^(r)_{n-l}` | `H^(r)_l` |
|---|---|---|---|---|---|---|
| `n -> n+1` | `+1/(n+k+1)^r` | `+1/(n-k+1)^r` | `0` | `+1/(n+l+1)^r` | `+1/(n-l+1)^r` | `0` |
| `k -> k+1` | `+1/(n+k+1)^r` | `-1/(n-k)^r` | `+1/(k+1)^r` | `0` | `0` | `0` |
| `l -> l+1` | `0` | `0` | `0` | `+1/(n+l+1)^r` | `-1/(n-l)^r` | `+1/(l+1)^r` |

The single negative entry `-1/(n-k)^r` (and its `l` mirror) is the **only** source of a
pole in the whole problem, and it occurs only at `k = n` / `l = n`. Everything in §5 is
book-keeping around those two entries.

`[VERIFIED under the Lean conventions]` — every row of the table above, restated with
`x -. y := max(x-y,0)` and `1/0^r := 0`, is **exactly 0** over `n = 0..8, k = 0..n+6,
r = 1..5` (495 cells per row, 6 rows = 2970 cells, zero failures), including the negative entry
`Δ_k H^(r)_{n-k} = -1/(n -. k)^r`, which holds unconditionally — no `k <= n` side condition.
So `LEAN_Z5_SCAFFOLD` §5.3's table is confirmed entry-for-entry from this side.

### 3.4 The regularised singular letter — the device that removes the boundary `0 * infinity` `[PROVED]`

The one genuinely delicate point in this family (flagged in `work/lb5/CERTS_RESUME.md` §2
as *"the step easiest to skip"*) is that at an integer `k > n` the factor `T` is `0` while
the letter `H_{n-k}` is `infinity`, so the summand is a literal `0 * infinity` and
`Limit` on the letter form returns `Indeterminate`.

**Both new weights are LINEAR in `beta`**, hence linear in `H_{n-k}` and in `H_{n-l}`
separately, **with no cross term** — for `w3hat` because `Psi = alpha/2 + beta` occurs to
degree 1, for `w5` because `beta` occurs only in `(alpha-beta)/2` and in
`-alpha*Psi/2 = -alpha^2/4 - alpha*beta/2`, both degree 1 in `beta`, and `alpha` contains
no `H_{n-.}` at all. So the whole difficulty is carried by the single composite

```
   Lam(n,k) := C(n,k)^2 * H_{n-k}        (and its k <-> l mirror)
```

> **Lemma R (regularisation).** For every integer `k > n >= 0`,
> `lim_{x -> k} ( Gamma(n+1) / (Gamma(x+1) Gamma(n-x+1)) )^2 * H_{n-x} = 0`.
> Hence `Lam(n,k) = 0` for every integer `k > n`, and `Lam` is finite everywhere.

*Proof.* Put `s = n - x -> -m`, `m >= 1`. `1/Gamma(s+1)^2` has a **double** zero there and
`H_s = psi(s+1) + gamma` a **simple** pole; the product is `-((m-1)!)^2 * epsilon + O(eps^2)`. ∎
`[VERIFIED, exact symbolic Limit, n = 0..5, k = n+1..n+4 — 24 cells, all 0]`

> **Lemma S (division-free shift laws for `Lam`).** For **all** integers `n, k >= 0`:
> ```
>  (Lam-k)  (k+1)^2   Lam(n+0,k+1) = (n-k)^2 Lam(n,k) - (n-k) C(n,k)^2
>  (Lam-n)  (n+1-k)^3 Lam(n+1,k)   = (n+1)^2 (n+1-k) Lam(n,k) + (n+1)^2 C(n,k)^2
> ```
`[VERIFIED exactly, n = 0..10, k = 0..14 — 165 cells each, all 0; the grid deliberately
runs k past n so the degenerate range is covered.]`

*Proof.* `(Lam-k)`: `C(n,k+1)^2 (k+1)^2 = C(n,k)^2 (n-k)^2` (that is `(E2)^2`) combined with
`H_{n-k-1} = H_{n-k} - 1/(n-k)`, then multiplied through by `(n-k)` to clear.
`(Lam-n)`: `C(n+1,k)^2 (n+1-k)^2 = C(n,k)^2 (n+1)^2` (that is `(E4)^2`) with
`H_{n+1-k} = H_{n-k} + 1/(n+1-k)`, times `(n+1-k)`. ∎

**Consequence.** With `Lam` (and its `l` mirror) adopted as a *primitive*, the singular
letter never appears alone, no expression in the entire certificate is ever infinite, and
every shift law is a multiplicative identity in `Z[n,k,l]` valid at **every** integer
point — including the whole overhang `n < k <= n+4` that the telescoping box requires.

---

## 4. T3 — the RISC-free verification kernel `[BUILT, SELF-TESTED]`

`work/z5cf/z5core.wl` extends `work/lb5/verifycore.wl` (which loads **no** RISC package)
with the two shifted kernels

```
  W3r[a,b,c] = T(n+a,k+b,l+c) * w3hat(n+a,k+b,l+c) / T(n,k,l)
  W5r[a,b,c] = T(n+a,k+b,l+c) * w5   (n+a,k+b,l+c) / T(n,k,l)
```

each expressed in `Q(n,k,l)[hh[...]]`, where `hh[base,r]` are the nine base letters
treated as independent indeterminates and every `HarmonicNumber` is reduced to
`hh[base,r] + explicit rational` using **only** the recurrence of §3.3. An expression
that reduces to `0` there is an identity of functions wherever the harmonic numbers are
defined.

**Self-test `[VERIFIED]`** — with `hh[base,r]` re-substituted by the actual harmonic
numbers, `W3r[a,b,c]*T(n,k,l) - T(n+a,k+b,l+c)*w3hat(n+a,k+b,l+c)` is exactly `0` at all
14 combinations of `(n,k,l) in {(7,2,3),(6,0,5)}` and
`(a,b,c) in {(0,0,0),(1,0,0),(3,0,0),(0,1,0),(3,1,0),(0,0,1),(3,0,1)}`; likewise for
`W5r`. This is what licenses using `W3r`/`W5r` as the ground truth for the certificate.

---

## 5. T4 — boundary conditions, and §6 — the Φ pipeline validated end-to-end on the Q-row

### 5.1 The obligation, stated exactly

With `N := n+4` (so that every nonzero term of `P̂_{n+i}`, `i <= 3`, is inside the box) the
telescoped identity summed over `0 <= k,l < N` gives

```
  Sum_{k<N} Sum_{l<N} E_w  =  Sum_{l<N} [ R_w(n,N,l) - R_w(n,0,l) ]
                            + Sum_{k<N} [ S_w(n,k,N) - S_w(n,k,0) ]
```

so four things must be discharged, and they are the *whole* of T4:

| # | obligation | how it is met over the base `Phi` |
|---|---|---|
| **(B-top-k)** | `R_w(n,N,l) = 0` | **free**: `Phi(n,n+4,l) = 0` because `C(n+3,n+4) = 0`, provided the cofactors are pole-free at `k = n+4` |
| **(B-top-l)** | `S_w(n,k,N) = 0` | mirror |
| **(B-bot-k)** | `R_w(n,0,l) = 0` | needs a numerator factor `k^3` in every cofactor |
| **(B-bot-l)** | `S_w(n,k,0) = 0` | mirror |
| **(B-int)** | every cofactor finite at the *interior* points `k,l = n+1,n+2,n+3` | **this is what the `Phi` base is for** — see §5.3 |

### 5.2 Pole orders, settled `[PROVED]`

Both weights are **linear in `beta`** (§3.4), so the summand has at worst a **simple** pole
in `k` at integer `k > n` (from `H_{n-k}`) and at worst a simple pole in `l`; `T` has a
**double** zero at each such point (`C(n,k)^2`). Product: a simple **zero**. With the `Lam`
primitive of §3.4 in place, nothing is ever infinite and nothing is ever `0 * infinity`.

### 5.3 Why the `Phi` base cures the interior poles — the mechanism, `[PROVED]`

```
   R_w / Phi  =  Sum_j rho_j * ( T(n+j,k,l)/T(n,k,l) ) * P_0 * w(n+j,k,l)
              =  P_0 * Sum_j rho_j * Wr[j,0,0]
   P_0 = [(n+1-k)(n+2-k)(n+3-k)]^2 [(n+1-l)(n+2-l)(n+3-l)]^2
```

`P_0` carries **double zeros at exactly the three interior points in `k` and the three in
`l` where a `T`-based cofactor has its poles**. So the transport to the `Phi` base is not a
cosmetic renormalisation: it is precisely the factor that removes (B-int). Measured on the
one certificate in this family that already exists — see §5.4 — the cancellation is exact
and leaves a denominator with **no zero anywhere in range**.

### 5.4 The Q-row (weight 0) certificate, transported and **fully verified** `[PROVED, RISC-free]`

The campaign's `[CERTIFIED]` Q-row pair `work/lb5/Qrow_rhosigma.m`
(`L_BZ.T = Delta_k(rho T) + Delta_l(sigma T)`) was pushed through the entire pipeline of
this report, in a kernel that **never loaded RISC**. This is the end-to-end validation of
every step §3–§5 proposes, on an object whose answer is already known.

| check | result |
|---|---|
| `L_BZ.T - Delta_k(rho T) - Delta_l(sigma T)`, via `verifycore`'s `grat` shift calculus | **exactly 0** (`LeafCount` 10553 / 1819) |
| `T(n+i,k,l) = Phi * P_i`, `i = 0,1,2,3`, as rational functions | **exactly 0**, all four |
| `Phi(n,k+1,l)(k+1)^3(k+l+1) = Phi(n,k,l)(n+3-k)^2(n+k+1)(n+k+l+1)` and the `l` mirror | **exactly 0** |
| transported cofactors `r := rho*P_0`, `s := sigma*P_0` — **denominator factors** | `r`: `(k+l+1)(n+1)^2(n+2)^2(n+l+2)(n+l+3)`; `s`: `(k+l+1)(n+1)^2(n+2)^2(n+l+2)` |
| ⇒ **(B-int)**: any zero of those in `n,k,l >= 0`? | **NONE.** The `(l-n-1)^2 (l-n-2)^2 (l-n-3)^2` poles of `rho` are cancelled **exactly** by `P_0` |
| **(B-bot)** `r(n,0,l) = 0`, `s(n,k,0) = 0` | **both hold** — `rho`'s numerator carries the factor `k^3`, exactly as `LEAN_Z5_SCAFFOLD` §5.4 predicted |
| **(B-top)** `R(n,n+4,l)`, `S(n,k,n+4)` at `n = 0..5`, all `k,l` in range | **all 0** |
| the `Phi`-form telescoping identity `Sum_i c_i P_i = g_k r(n,k+1,l) - r + g_l s(n,k,l+1) - s` | **exactly 0** as a rational-function identity |
| the **cleared polynomial identity** (below), `Expand -> 0` | **exactly 0** |
| **end-to-end**: `Sum_i c_i Sum_{k,l<=n+3} T(n+i,k,l) = ` telescoped boundary, `n = 0..5`, exact ℚ | **0 = 0**, all six |

with `g_k = (n+3-k)^2(n+k+1)(n+k+l+1) / [(k+1)^3(k+l+1)]` and the `l` mirror.

**The cleared polynomial identity** — this is what `ring` closes. Write `r = A/D_r`,
`s = B/D_s` with `A, B` the (already factored) numerators and
`D_r = (k+l+1)(n+1)^2(n+2)^2(n+l+2)(n+l+3)`, `D_s = (k+l+1)(n+1)^2(n+2)^2(n+l+2)`, and
`D* = (k+1)^3(l+1)^3(k+l+1)(k+l+2)(n+1)^2(n+2)^2(n+l+2)(n+l+3)`. Then, in `Z[n,k,l]`:

```
  D* * Sum_{i=0}^{3} c_i(n) P_i(n,k,l)
    =   (l+1)^3 (n+3-k)^2 (n+k+1)(n+k+l+1)          * A(n,k+1,l)
      - (k+1)^3 (l+1)^3 (k+l+2)                     * A(n,k,l)
      + (k+1)^3 (n+3-l)^2 (n+l+1)(n+k+l+1)(n+l+2)   * B(n,k,l+1)
      - (k+1)^3 (l+1)^3 (k+l+2)(n+l+3)              * B(n,k,l)
```

`[PROVED, Expand -> 0]`. Total degrees: LHS `deg_n = 27, deg_k = 11, deg_l = 13`;
`A`: `(25, 9, 9)`; `B`: `(24, 7, 10)`. `LeafCount(A) = 10477`, `LeafCount(B) = 1797`, both
delivered **pre-factored** (`Head = Times`) per `LEAN_Z5_SCAFFOLD` §5.6.1.

### 5.5 ⚠ A SECOND pole source, not covered by `Phi` — **read this before formalising**

`LEAN_Z5_SCAFFOLD` §5.2 identifies one pole source (cofactors over the base `T`) and cures it
with `Phi`. **There is a second, independent one, and it is intrinsic to normalising the
letters.** Measured here, on the LHS of the weight-3 identities:

```
   E_w / Phi  =  P_0 * Sum_{i=0}^{3} c_i * Wr[i,0,0]  =  Sum_{j=1}^{15} b_j(n,k,l) * M_j
```
`[COMPUTED, RISC-free]`. The 15 coefficients `b_j` have denominator factors

```
   2, (n+k+1), (n+k+2), (n+k+3), (k-n-1), (k-n-2), (k-n-3), (n-l+1), (n-l+2), (n-l+3)
```

so **simple poles at `k = n+1, n+2, n+3` and at `l = n+1, n+2, n+3`** — interior points of the
range. `P_0` does **not** cancel them: they do not come from `T`, they come from rewriting
`H^(r)_{n+i-k}` in terms of the base letter `H^(r)_{n-k}` via
`H^(r)_{n+i-k} = H^(r)_{n-k} + Sum_{j=1}^{i} 1/(n+j-k)^r`. The term `1/(n+j-k)^r` is singular at
`k = n+j`, and `P_i` vanishes only at `k = n+i+1..n+3`, i.e. never at the offending point.

**This is not a defect of the certificate — it is a statement about the normalisation.** The
*function* `E_w` is perfectly finite at `k = n+1`: for `i >= 1`, `T(n+i,n+1,l) != 0` and
`w(n+i,n+1,l)` is an ordinary finite value. It is the *decomposition* into "base letters at
`(n,k,l)` plus rational functions" that is singular there, and the singular parts cancel
against the singularity of the base letter `H^(r)_{n-k}` itself.

**Consequence for Lean.** The certificate as a **rational-function identity over `Q(n,k,l)`**
and the certificate as a **Lean statement for all `n k l : ℕ`** are *different statements at
`k, l in {n+1, n+2, n+3}`*, because Lean's conventions (truncated `ℕ` subtraction and
`1/0 = 0`) replace each singular `1/(n+j-k)^r` by `0` and each `H^(r)_{n-k}` by `H^(r)_0 = 0`.
Those conventions are **self-consistent**, and this was *verified* rather than argued:

> **Lemma N (normalisation survives the Lean conventions).** With `x -. y := max(x-y,0)` and
> `1/0^r := 0`, for all `n, k >= 0`, `1 <= i <= 3`, `1 <= r <= 5`:
> ```
>    H^(r)_{(n+i) -. k}  =  H^(r)_{n -. k}  +  Sum_{j=1}^{i} 1 / ((n+j) -. k)^r
> ```
`[VERIFIED exactly, n = 0..6, k = 0..n+5, i = 1..3, r = 1..5 — 945 cells, 0 failures]`

e.g. at `k = n+2, i = 3`: LHS `= H^(r)_1 = 1`; RHS `= 0 + 1/0 + 1/0 + 1/1 = 1`. ✓
So the base-letter normalisation is legitimate in Lean. But Lemma N is **not implied by** the
rational-function identity over `Q(n,k,l)` — over `Q(n,k,l)` the same expression at `k = n+2`
would read `0 + 1/(-1) + 1/0 + 1/1`, which is a different (and singular) object. The two
statements must therefore be checked separately.

> **Obligation added to the hand-off, and it is cheap:** once `(rho, sigma)` exist, verify (★)
> at every integer point with `0 <= k,l <= n+4`, `n <= 6`, **twice** — once over `Q(n,k,l)`
> (the RISC statement) and once under the `ℕ`-truncated / `1/0 = 0` conventions (the Lean
> statement). `z5core.wl` supports both; the second is the one `LEAN_Z5_SCAFFOLD` §5.3 assumes
> and nobody has yet tested. For the **Q-row this obligation is vacuous** (`J = 1`, no letters),
> which is exactly why §5.4 went through cleanly and must not be read as evidence about the
> weight rows.

**Delivered:** `work/z5cf/w3_LHS_basis.m` — the 15 named basis monomials
```
  1, H1_l, H1_k, H1_{n-k}, H1_{n-l}, H1_{n+l}, H1_{n+k}, H2_{n+k}, H3_{n+k},
  H2_{n+k} * { H1_l, H1_k, H1_{n-k}, H1_{n-l}, H1_{n+l}, H1_{n+k} }
```
together with the 15 exact coefficients `b_j` (max `LeafCount` 26 871), the per-`j` denominator
factor lists, `P_0`, `P_0..P_3` and `cc`. This is the **left-hand side of the 15 Lean identities
of `LEAN_Z5_SCAFFOLD` §5.5, complete** — it does not depend on how `(rho, sigma)` is found, so
it is usable now.

**Saved: `work/z5cf/Qrow_phicert.m`** — an `Association` with keys `cc`, `P`, `P0`,
`r_num`, `r_den`, `s_num`, `s_den`, `gk`, `gl`, `Dstar`, `polyidentity`, `verified`,
`degrees`, `boundary_terms_n_0_to_5`. This is the weight-0 row of the ζ(5) family in
exactly the D1–D5 shape `LEAN_Z5_SCAFFOLD` §S5 specifies, with `J = 1`, and it is ready to
hand to the Lean agent as the pipeline's calibration row.

---

## 6. Files

| file | what |
|---|---|
| `work/z5cf/z5ann.wl` | the annihilator / creative-telescoping driver (self-testing, checkpointed, `TimeConstrained` + `MemoryConstrained` at every stage) |
| `work/z5cf/z5core.wl` | RISC-free kernel functions `W3r`, `W5r`, `applyOpe` (extends `work/lb5/verifycore.wl`) |
| `work/z5cf/z5asm.wl` | certificate composition (RISC used only to *find* cofactors) |
| `work/z5cf/z5ver.wl` | the RISC-free verifier (V-A .. V-E) |
| `work/z5cf/memwatch.sh`, `memwatch.log` | external RSS / free-memory watch |
| `work/z5cf/z5ann5b.wl` | weight 5 by an explicit closure chain — every product via `DFiniteTimes`, never `Annihilator` |
| `work/z5cf/z5ct.wl` | single-shot two-delta creative telescoping, support bounded to the `L_BZ` box |
| `work/z5cf/z5w3b.wl` | second weight-3 attempt: reduce the annihilator first (`B0`), probe the multi-delta signature (`B1`), then `ct1` with `ORD` (`B2`) |
| `work/z5cf/z5phi.wl` | transport a RISC certificate to the pole-free base `Phi`, audit the poles and `(B-bot)`, emit the `J` identities |
| **`work/z5cf/Qrow_phicert.m`** | **the Q-row certificate in the `Phi` base, `[PROVED RISC-free]`, in `LEAN_Z5_SCAFFOLD` §S5 D1–D5 shape** |
| `work/z5cf/z5_w3_lk_annS.m` | the weight-3 annihilator, 10 generators, rank 15 (16.7 MB) |
| `work/z5cf/z5b_*.m` | the weight-5 closure-chain pieces (`H3`,`H4`,`H5`,`alpha`,`Psi`,`alpha-beta`,`S2`) |
| `work/z5cf/z5ann_*.log`, `z5ann5b_*.log`, `z5w3b_*.log`, `z5ct_*.log` | the stage-by-stage timing and memory record |

---

## 7. What a successor should do next, in order

1. **Re-run every `Annihilator` in the campaign through `DFiniteTimes`.** §2.0/§2.2b: the cost
   driver is the *product*, not the letter count. `Annihilator[T*ṽ]` (5801 s, 4 GB) and
   `Annihilator[F_kk]` (OOM, 7.8 GB, 85 min) were both products of a hypergeometric term with a
   letter-bearing factor, and both were handed to `Annihilator` whole. Cheap to retry; the
   weight-3 measurement here says the factor is ~60x.
2. ~~**Shrink the basis before eliminating.**~~ `[EXCLUDED, MEASURED]` — `OreGroebnerBasis`
   over the full 3-variable algebra costs 2119 s and reduces the `LeafCount` by a factor of
   **1.000** (10 generators in, 10 out; rank 15 in, 15 out). Do not spend time here again.
3. ~~**Fix the multi-delta `CreativeTelescoping` call.**~~ `[EXCLUDED, MEASURED]` — re-run with
   messages visible, it raises a genuine error, so the call shape does not exist in this build.
   The `ct1` -> `OreGroebnerBasis` -> `ct2` -> `OreReduce` assembly (already implemented in
   `z5asm.wl`) is the only route to a pair through RISC.
4. **PRIMARY RECOMMENDATION — the problem is a finite linear solve, not a Gröbner computation.**
   Everything needed is already known and RISC-free: the telescoper (`L_BZ`), the base (`Phi`,
   `P_i`), the monomial basis (`J = 15` / `64`, computed in §2.3), and the two shift matrices
   `A_k, A_l` over `Q(n,k,l)` from the letter table of §3.3. The certificate is then the
   solution of `b = g_k A_k^T r(k+1) - r + g_l A_l^T s(l+1) - s` under a polynomial ansatz for
   `r, s` — `2J(d+1)^2` unknowns over `Q(n)`, solvable modularly. At `J = 15` that is a few
   thousand unknowns; it is a build, but it is bounded and it cannot OOM.
5. **Do not re-run:** `Annihilator[w₅]` monolithically (1800 s, no return, ~1 GB);
   `Annihilator[alpha*Psi]` (1200 s, no return, ~0 GB) — use `DFiniteTimes` for both;
   the two-delta `CreativeTelescoping` call shape as written in `z5ct.wl` (rejected in 1 s).

---

## 8. Honest status of each task

| task | status |
|---|---|
| **T1** | **DONE for weight 3** (94 s / 0.7 GB / 10 generators / rank 15, plus the 62x comparison). **Weight 5: measured and did not land** — `Annihilator[w₅]` 1800 s TIME abort at 1.07 GB flat; the degree-2 sub-product `α·Ψ` localised as the wall. Neither is an exclusion. |
| **T2** | **NOT OBTAINED.** `ct1` time-aborted at 5402 s / 2.0 GB; two-delta CT call shape rejected; reduction + `ORD=kl` in flight at hand-off. |
| **T3** | **Harness BUILT and SELF-TESTED** (`z5core.wl`, exact 0 at 28 point/shift combinations across both weights), and **exercised to completion on the Q-row**, RISC-free. Awaiting a pair from T2 for the new weights. |
| **T4** | **DONE.** All four boundary obligations stated exactly, pole orders proved (both weights linear in `beta` ⇒ simple pole vs `T`'s double zero), the regularisation lemmas R and S proved and grid-verified, and all four discharged explicitly on the Q-row (`n = 0..5`). |
| **T5-extra** | **Lemma N** and the whole §3.3 letter table `[VERIFIED under Lean's own conventions]` — 945 + 2970 cells, zero failures. This confirms `LEAN_Z5_SCAFFOLD` §5.3 from the CAS side and identifies the one obligation nobody had tested (§5.5). |
| **T5** | **DONE.** Lemma 0 (four elementary absorptions), Lemma T (three multiplicative shift identities for `T`), the `Phi` base with the four degree-12 `P_i` and its two steps, the letter shift table, Lemmas R and S — all `[PROVED]` and grid-verified **including the degenerate range**; the explicit cleared polynomial identity delivered for the Q-row and the general shape (`J` identities in `Q[n,k,l]`, one per closure monomial) fixed for the weight rows. |

---

## 9. Reproduction and kernel hygiene

```bash
D=/home/ubuntu/fable-episode-2/zeta-math-2/work/z5cf
# ALWAYS check the licence seats first -- only TWO standalone kernels may exist, and a third
# fails with "cannot find a valid password" AFTER burning the launch (seen at 09:55 this run).
pgrep -a WolframKernel
nohup $D/memwatch.sh &                                # external RSS / free watch, 20 s

# T1, weight 3 -- the 94 s annihilator (checkpoints z5_w3_lk_ann{T,W,S}.m)
cd $D && WT=3 ORD=lk MEMCAP=2800000000 SPLITCAP=1200 DIRECT=0 TAG=w3_lk math < z5ann.wl
# T1, weight 5 -- closure chain, every product via DFiniteTimes (checkpoints z5b_*.m)
cd $D && TAG=w5_lk MEMCAP=4000000000 PCAP=1200 math < z5ann5b.wl
# T2 retry -- reduce the basis first, then eliminate
cd $D && ORD=kl MEMCAP=5000000000 GBCAP=2400 CT1CAP=12000 math < z5w3b.wl
# T2 -> T3 -> T5, once a pair exists
cd $D && TAG=w3_lk FIRST=l math < z5asm.wl      # RISC: find the cofactors
cd $D && TAG=w3_lk KER=w3   math < z5ver.wl     # NO RISC: verify (V-A..V-E)
cd $D && TAG=w3_lk KER=w3   math < z5phi.wl     # NO RISC: transport to Phi, pole + boundary audit
```

Operational facts that cost time this run and are worth keeping:

* **`math < file.wl`, never `math -script`** (silent line truncation) — held throughout.
* **Every stage needs `SetAttributes[stage, HoldRest]`** or the checkpoint logic evaluates the
  body before looking for the checkpoint. All scripts here have it.
* **A third kernel launch does not queue, it dies** — and it dies *after* the shell has already
  reported the launch, so the failure is only visible in the `.stdout`. Kill and confirm with
  `ps` before launching; `kill` may take several seconds to release the seat (`kill -9` if so).
* **`MaxMemoryUsed` inside the kernel badly understates real RSS** — it read `0 GB` for a stage
  whose external RSS was 1.12 GB. Always run the external `free -m` / `ps` watch; the in-kernel
  number alone would have mislabelled two clock walls as "free".

---

## 10. In flight at hand-off (2026-07-26 13:40)

Two standalone kernels left running **deliberately**, both with a real `TimeConstrained` +
`MemoryConstrained` cap and per-stage checkpoints, so neither can starve the box or sit
indefinitely, and every completed stage is on disk:

| pid | job | state | cap expires |
|---|---|---|---|
| `337252` | `z5w3b.wl` `ORD=kl` — weight-3 `ct1` **eliminating `k`** on the (measurably irreducible) rank-15 basis | `B0` and `B1` resolved (both negative, §2.4); `B2` running since 13:38:04 | 12000 s ≈ 16:58 |
| `364321` | `z5ann5c.wl` — `DFiniteTimes[ann alpha, ann Psi]` on a long clock, the honest "diverging or merely slow?" test for the weight-5 wall | running since 13:37:55 at ~1.1 GB | 7200 s ≈ 15:38 |

Read `z5w3b_kl.log` and `z5ann5c.log` first on resuming. Checkpoints already on disk that must
**not** be recomputed: `z5_w3_lk_ann{T,W,S}.m` (the 94 s weight-3 annihilator),
`z5_w3_gb3.m` (its 2119 s Gröbner reduction — identical to the input),
`z5b_{H3,H4,H5,Al,Be,Ps,AB,S2}.m`, `z5c_AlAl.m` (`alpha^2`, 31 s),
`z5c_{Al,Ps,AP}_k.m` (the one-variable probes).

**If `364321` returns**, `z5ann5d.wl` assembles the weight-5 annihilator from it and the
already-checkpointed pieces, and asserts `rank = 64` against the independently computed
shift closure. **If it does not**, §7.4 is the route: the module is explicitly known, so the
annihilator, the telescoper and the certificate are all kernels of finite matrices over
`Q(n,k,l)`, and none of those computations can stall the way a Gröbner engine does.
