# DIG-3 — the honest scan

**Agent:** DIG-3 (retargeted: the honest scan). **Date:** 2026-07-25.
**Code:** `work/dig/s_*.py` (all mine; DIG-1's `ledger/family/verify/optimize/…` and
DIG-2's `g_*` untouched and not refitted).
**Labels:** `[PROVED]` · `[VERIFIED …]` = exact finite computation, range always stated ·
`[COMP]` = a computed optimum, exhaustive over the stated cone.
All arithmetic exact (`fractions.Fraction`, `int`); wide searches run over `F_q`,
`q = 2^61−1`, with every hit re-verified over ℚ.

---

## HEADLINE

| mission | verdict |
|---|---|
| **M1 ζ₂(7)** | **NO.** Best margin **−5.4548** `[COMP]` — *worse* than DIG-1's −1.4548, because the ledger's `E` is too small at `m ≥ 2` (§2). Two independent walls, both measured. |
| **M2 records** | **NO record.** μ(ζ₂(3)) = 7.17739889912418, μ(ζ₃(3)) = 22.28144795149432, μ(ζ₂(5)) = 20.34265173891448 are each **exactly optimal** over the whole cone `[COMP]`. The group's δ is *identically 0* on the p-adic locus — now measured, not modelled (§4). |
| **M3 hatch** | **SHUT** over a fair sweep `[VERIFIED]`: the coset sum never beats the per-coset minimum by more than **3** (absolute, not per n), and the best fixed ℤ_p-combination gains a **bounded** amount (≤ 28) while the requirement grows like `E·n`. |
| **M4 map** | delivered (§5), in two versions: DIG-1's ledger `E`, and the **corrected, measured** `E`. Headline row: **the p ≥ 5 wall is size, the p = 2 wall is rank, and after the E-correction the nearest miss in the whole family is no longer ζ₂(7) — it is ζ₅(3)/ζ₇(3) at −3.000.** |

Three corrections to the DIG-1 ledger fall out of the scan; all three make the
picture *worse*, none touches a published anchor.

---

## 0. What the ledger did not cover, and why it matters

DIG-1's optimiser `optimize.py` ranges over `r ≤ 3, A ≤ 6, m ∈ {w−3, w−4}, δ ∈ {0,1}`
with `E = A+m+1−δ` and `if m < 0: continue`. The honest scan re-opened four doors:

1. **`m = −1`** (the primitive / Lai–Sprang convention), explicitly skipped. → §1.
2. **`E` at `m ≥ 2`**, never measured (every anchor has `m ≤ 1`). → §2.
3. **the rank axis** — `optimize.py` reports only `rank = 1`, which hides that at
   `p = 2` the *size* constraint is never binding. → §3.
4. **the O(1) "inset" cone** — bounded translations of the bricks, which move no
   asymptotic rate at all and therefore are invisible to the ledger, but move
   every rational coefficient. → §3.

`s_vwp.py` reproduces DIG-1's and DIG-2's anchors before anything else is done
(LSZ's printed `ρ_{0,3} = 768`, `ρ_{1,3} = 73728`, `ρ_{0,0} = 0`, `ρ_{1,0} = −1024`,
`ρ_n = 1, 96, 14944`; all three published μ to every digit).

---

## 1. `m = −1` — the skipped direction, and why it is dead `[VERIFIED]`

The ledger's `α` does not depend on `m`, and `E = A+m+1−δ` is *smallest* at
`m = −1`. Taken at face value this would give, from **the very rational function
LSZ use** (`2^{8n}(2t+n)(t+½)_n^4/(t)_{n+1}^4`, `M = 4`), a rank-1 form in 1 and
ζ₂(3) with `E = 3`, `G = 8log2`, margin **+2.5452** and **μ(ζ₂(3)) ≤ 4.3574** —
a large record. It is false.

**Measured** (`s_meas.py`, exact truncated Volkenborn, `n ≤ 22`):

| family | predicted α | measured `v₂(C^n S_n)/n` |
|---|---|---|
| M=3, m=0 (Beukers R^(B)) | 12 log2 | 11.50 … 11.83 log2 ✓ |
| M=4, m=1 (LSZ) | 16 log2 | 15.17 … 15.72 log2 ✓ |
| M=5, m=0 | 20 log2 | 19.17 … 19.50 log2 ✓ |
| M=6, m=1 | 24 log2 | 23.14 … 23.50 log2 ✓ |
| **M=4, m=−1** | 16 log2 | **8.11 … 8.33 log2** |
| **M=6, m=−1** | 24 log2 | **11.90 … 12.14 log2** |

i.e. **`α = G`, not `2G`: the primitive loses the entire p-adic doubling**, so
`margin = −E < 0` always. Confirmed a second way, with no Volkenborn truncation
at all: `y_n := −ρ₀/ρ_w` converges 2-adically (so the linear-form identity *is*
right) but at exactly half the rate of the `m ≥ 0` controls (135 vs 272 digits
at `n = 18`).

**Why** `[PROVED]`: the smallness of `∫R^{(m)}(t+θ₀)dt` comes from the *product*
`v₂(C^nR(t+½)) = 2Mn + Mn + Mn = 4Mn`, an exponential cancellation between
partial-fraction pieces that are individually of size `2^{−2Mn}`. The primitive
`R̃` is not that product; its pieces `r_{i,k}(t+½+k)^{1−i}/(1−i)` are added
without cancellation, and `v₂(C^nR̃) = O(1)`.

> **Correction 1.** The `m = −1` slice of the family is not a slice of the
> *construction*: `α(m=−1) = G`. DIG-1's ledger should carry `m ≥ 0`.

---

## 2. The denominator `E` is too small at `m ≥ 2` `[VERIFIED, two rules, 0 violations]`

`E = A+m+1−δ` is validated in DIG_LEDGER §2.3 against LSZ (`m=1`), Beukers
(`m=0`), Lai `B_n` and `A_n` (`m=0,1`). **Every anchor has `m ≤ 1`.** Weight 7 at
rank 1 forces `m ≥ 3` (§3). So the ledger extrapolates into unmeasured territory
exactly where the ζ₂(7) question lives.

`s_den.py` factors the exact denominator of `ρ₀` (after the forced normalisation
`C^n = p^{v_p(C)n}`, with the p-part removed since `C^n` pays it) and reads the
exponent off as a function of `ℓ/n`. The profile is a clean two-band step:

```
M=4 VWP, p=2, r=1, n=48
  m=1 : exponent 5 on every prime  l <= n ;  NOTHING above n            E = 5   (ledger 5)
  m=3 : exponent 7 on every prime  l <= n ;  exponent 4 on n < l < 2n   E = 11  (ledger 7)
  m=5 : exponent 9 on every prime  l <= n ;  exponent 6 on n < l < 2n   E = 15  (ledger 9)
```

Since `log lcm{ℓ : n < ℓ < 2n}/n → 1`, the second band costs its exponent
outright. Two rules, both `[VERIFIED with 0 violations]` over
`p ∈ {2,3,5,7}`, `r ∈ {1,2}`, `A ≤ 5`, `m ≤ 4`, `δ ∈ {0,1}`, `n = 30…48`:

> **R1.** The well-poised saving `−δ` is real **only where the symmetry
> `R(−h₀−t) = ±R(t)` actually holds** — at `(p,r) = (2,1)` with every shift ½, and
> at `(2,2)` with the ¼- and ¾-bricks **paired** (Lai's `A_n`). Everywhere else
> (p ≥ 3, and `(2,2)` with all bricks on one coset) the measured exponent on the
> primes `≤ n` is `A+m+1` **exactly** — the `(2t+n)` factor buys nothing.
>
> **R2.** A second band appears on the primes in `(n, 2n)`, of exponent
> **`c = m+1` when `m ≥ A−1`, and `c = 0` otherwise** (single-shift shape).
>
> **`E_true = (A + m + 1 − δ_eff) + c`.**

The band comes from the half-integer sums `T_{k,u} = Σ_{ν<k}(ν+θ₀)^{−u}`, whose
denominators run over the odd numbers up to `2n`; for small `m` they cancel
against the `r_{i,k}`, for `m ≥ A−1` they do not.

**No published result is touched:** all four anchors have `c = 0` and the correct
`δ_eff`, and `s_den.py` re-derives their `E` = 3, 3, 5, 3 exactly. Lai's `B_n` at
`s = 2, 3` (`m = 2, 3`) also has `c = 0` (`m < A−1` there) — so his printed
denominators stand too.

**Can the band be switched off by choosing the shape?** No, at the point that
matters: over the whole inset lattice `[0,2]^4 × [0,2]^4` at the ζ₂(7) rank-1
point (`M=4, m=3, δ=1`), the attainable `(exp_low, exp_high)` pairs are
`(6,6), (7,4), (7,5), (7,6), (7,7), (8,8)` — **minimum `exp_high` = 4, attained at
the symmetric point**, so `E_true = 11` is optimal. `[COMP]`

> **Correction 2.** `E_true(ζ₂(7) rank-1) = 11`, not 7. **The ζ₂(7) margin is
> −5.4548, not −1.4548.** Likewise ζ₂(9): −9.4548; ζ₃(5): −3.8028; ζ₃(7): −8.7042.
>
> **Correction 3.** The `δ = 1` saving is a `p = 2` phenomenon. DIG-1's optimiser
> granted it at every `p`; at `p ≥ 3` every cell that used `δ = 1` is 1 worse.

---

## 3. M1 — ζ₂(7): the two walls

### 3.1 The parity law and why rank-1 caps `A` at 4 `[PROVED, VERIFIED]`

For the VWP family `R = (2t+h₀)^δ ∏_{j≤M}(t+½+e_j)_{h₀−2e_j}/∏_{j≤M}(t+f_j)_{h₀+1−2f_j}`
(any integer insets `e, f`), `R(−h₀−t) = −(−1)^M R(t)`, hence
`r_{i,h₀−k} = −(−1)^{M+i}r_{i,k}` and

> **`ρ_i = 0` whenever `i + M` is even.** `[VERIFIED M = 3…7]`

Together with `ρ₁ = 0` (deg `R ≤ −2`) and `ζ₂(even) = 0` this gives the exact
rank, and the whole family's ledger collapses to two numbers:

> **`margin(M, m) = 2M log2 − (M+m)`,  weights `{m+4, m+6, …, m+M}` (M even),
> `{m+3, m+5, …, m+M}` (M odd), rank = the number of them.**

Rank 1 forces `M ∈ {2,3}` (m even) or `M ∈ {3,4}` (m odd), so **`M ≤ 4`**, and
then weight 7 needs `m = 3` (M=4) or `m = 4` (M=3) — in both cases `m ≥ A−1`, so
Correction 2 bites. **Every rank-1 route to weight 7 at p = 2 must buy the weight
with derivatives, and every such derivative order switches the second denominator
band on.** That is wall #1, and it is structural, not numerical.

### 3.2 Size is not the problem — rank is `[COMP]`

```
  M   m   weights      rank  G        E   margin     mu
  3   0   [3]            1   4.1589   3   +1.1589    7.17740   = Beukers, zeta_2(3)
  4   1   [5]            1   5.5452   5   +0.5452   20.34265   = LSZ, zeta_2(5)
  4   3   [7]            1   5.5452  11   -5.4548      --      <- the rank-1 zeta_2(7) slice
  6   1   [5, 7]         2   8.3178   7   +1.3178   12.62404   <- Lai: one of z2(5), z2(7)
  7   0   [3, 5, 7]      3   9.7041   7   +2.7041    7.17740
  8   1   [5, 7, 9]      3  11.0904   9   +2.0904   10.61098
  9   0   [3, 5, 7, 9]   4  12.4766   9   +3.4766    7.17740
```

`margin = M(2log2 − 1) − m → +∞`. **At `p = 2` there is a positive margin at every
weight; the entire obstruction is that the form carries `⌊(M−1)/2⌋` zeta values.**
If the ζ₂(5)-coefficient of the `M=6, m=1` family could be removed, ζ₂(7) would be
irrational with **μ ≤ 12.62404**. That is the only live route, and §3.3 closes it.

### 3.3 The rank cannot be reduced `[VERIFIED, with a positive control]`

Removing a coefficient requires an operator
`L = Σ_{j,l,d} c_{j,l,d} n^d (n → n+l) (inset-form j)` with **polynomial**
coefficients — anything of size `e^{Gn}` doubles `β` and gives
`α − 2β = −2E < 0` (the classical elimination tax; combining the `M=6` form with
the LSZ form explicitly gives margin `11.09 − 25.86 = −14.78`). So the question is
whether `ker(ρ₃) ⊆ ker(ρ₅)` inside that module. `s_recur.py`, `s_rank.py`, over
`F_q`:

| test | family | kill → keep | forms | L | D | unknowns | dim ker | keep ≠ 0 | control |
|---|---|---|---|---|---|---|---|---|---|
| shifts only | M=6, m=1 | ρ₃ → ρ₅ | 1 | 4 | 10 | 55 | 0 | — | — |
| shifts only, wider | M=6, m=1 | ρ₃ → ρ₅ | 1 | 6 | 12 | 91 | 0 | — | — |
| **inset cone** | M=6, m=1 | ρ₃ → ρ₅ | 4 | 3 | 8 | 144 | **66** | **0** | **66/66** |
| **inset cone, wider** | M=6, m=1 | ρ₃ → ρ₅ | 6 | 4 | 6 | 210 | **120** | **0** | **120/120** |
| **the ζ₂(5) record route** | M=5, m=0 | ρ₂ → ρ₄ | 4 | 3 | 8 | 144 | **77** | **0** | **77/77** |
| **the rank-3 route** | M=7, m=0 | ρ₂,ρ₄ → ρ₆ | 4 | 3 | 8 | 144 | **36** | **0** | **36/36** |
| **the rank-3 route** | M=8, m=1 | ρ₃,ρ₇ → ρ₅ | 4 | 3 | 6 | 112 | **1** | **0** | **1/1** |

The **positive control** evaluates the very same kernel on a coefficient sequence
taken from a *different* family (M = 8, resp. M = 6): every kernel vector gives a
non-zero value there, so the machinery does detect survivors when they exist.

> **Every polynomial-coefficient operator that annihilates the ζ₂(5) coefficient
> annihilates the ζ₂(7) coefficient as well** — and the same in all four families
> tested, including the ζ₂(5)-record route. The coefficients generate the same
> difference module; these forms are irreducible. Wall #2.

### 3.4 The C₁/δ tension at p = 2, measured `[VERIFIED]`

The remaining freedom is the *length* cone (`e_j = ε_j n`, `f_j = φ_j n` — the
Rhin–Viola direction). With `e, f ≥ 0` (forced: negative pole insets put poles on
the wrong side of ℤ_p),

`Σλ = M − 2Σε ≤ M`, `Σν = M − 2Σφ ≤ M`, so `G = (Σλ+Σν)log2 ≤ 2M log2`
**with equality exactly at the symmetric point**, where `C₁ = 0` and `δ_group = 0`.
Measured at `M=6, m=1` (`s_cone.py`, `C₁` de-biased against the symmetric control
at the same `h₀`, `E` measured):

```
  profile (eps ; phi)          sum_lam sum_nu   G        C_1      E    margin
  symmetric                     6.000  6.000   8.3178   +0.0000   7   +1.3178
  one num brick shortened       5.667  6.000   8.0867   -0.6408   9   -0.9133
  two num bricks shortened      5.333  6.000   7.8557   -1.1874  10   -2.1443
  one num + one pole            5.667  5.667   7.8557   -0.0260   7   +0.8557
  stronger asymmetry            5.000  5.667   7.3936   -1.3089   9   -1.6064
```

`G` falls **and** `E` rises. The symmetric point is strictly optimal; the
group direction buys nothing here, and — crucially — `E` is *measured*, so this
already includes whatever Φ_n saving is actually present. **At `p = 2` the
C₁/δ tension is not a near miss: δ is 0 and the cone is strictly downhill.**

### 3.5 M1 verdict

> **No configuration pushes the ζ₂(7) margin positive.**
> **Best margin = −5.4548**, at `p=2, r=1, A=4, m=3, δ=1` (all shifts ½),
> `G = 8log2 = 5.5452`, `α = 2G = 16log2 = 11.0904`, `E_true = 11`,
> `β = G + E = 16.5452`, `margin = α − β = −5.4548`. `[COMP]`
> Ledger printout of the same point: `E_ledger = 7`, `margin = −1.4548`; the
> 4-unit gap is the second prime band of §2, which no shape in the cone removes.

Re-verified at 50 digits (`mpmath`), and `E_true` re-verified at larger `n`:

```
zeta_2(7)  p=2 r=1 A=4 m=3 delta=1
   G      = 5.5451774444795624753          (= 8 log 2)
   alpha  = 11.090354888959124951          (= 16 log 2 = 2G)
   beta   = 16.545177444479562475          (= G + 11)
   margin = -5.4548225555204375247         (ledger would say -1.4548225555204375247)

E_true bands:   n=48 -> (7, 4)    n=60 -> (7, 4)    n=72 -> (7, 4)      E_true = 11
                measured log(denom)/n = 9.72, 10.18, 10.21  (-> 11, from below)
```

---

## 4. M2 — measure records: none `[COMP]`

`μ = α/(α−β) = (G + gain)/(gain − C₁ − E)`. The scan (`s_record.py`) evaluates
this with **`E` and `growth` measured**, so any Φ_n / Rhin–Viola saving that is
actually present is already counted — there is no calibration step anywhere.

* **O(1) insets** (58 / 127 / 288 admissible points at M = 3 / 4 / 5): every
  asymptotic quantity — `Σλ = Σν = M`, `G`, `gain`, `C₁ = 0` — is *identical* to
  the symmetric point, and the measured `E` is identical too. (A promising
  `E: 5 → 3` drop at `M=5` and `n=24` was chased and is a small-`n` artefact:
  at `n = 36, 48, 60` the exponent is back to 5.) **μ unchanged, exactly.**
* **Scaled insets** (the length cone, §3.4): `G` strictly down, `E` up. μ worse.
* **Rank reduction** (which would give μ(ζ₂(5)) ≤ 7.17740 from the `M=5, m=0`
  family, and μ(ζ₂(7)) ≤ 12.62404 from `M=6, m=1`): blocked by §3.3.
* **The group.** DIG-2 `[PROVED]` δ = 0 at the totally symmetric point. The scan
  adds the empirical half: on the whole p-adic locus the *measured* denominator
  never falls below its symmetric value, so `δ_group ≤ 0` throughout. The
  `C₁ = 0` / `δ = 0` disjoint-support wall of DIG_LEDGER §5 is confirmed at
  `p = 2` as well as at `p ≥ 5`.

> **Records stand, and are now known to be exactly optimal over this cone:**
> **μ(ζ₂(3)) ≤ 7.17739889912418**, **μ(ζ₃(3)) ≤ 22.28144795149432**,
> **μ(ζ₂(5)) ≤ 20.34265173891448**. No improvement anywhere. `[COMP]`

Re-verified at 50 digits from `(p, r, A, m, δ)` alone:

```
zeta_2(3)  G = 4.158883083359672   margin = 1.158883083359672   mu = 7.1773988991241796616
zeta_3(3)  G = 3.295836866004329   margin = 0.2958368660043291  mu = 22.28144795149432156
zeta_2(5)  G = 5.545177444479562   margin = 0.5451774444795625  mu = 20.34265173891448181
```

The two would-be records, both closed by §3.3: μ(ζ₂(5)) ≤ **7.17740** from the
`M=5, m=0` family (kernel test 0/77) and μ(ζ₂(7)) ≤ **12.62404** from `M=6, m=1`
(0/66, 0/120).

---

## 5. M3 — the escape hatch: shut `[VERIFIED, range stated]`

`α = min over cosets` is an inequality. `s_coset.py` computes the **actual**
`S_n(j/p^r)` for every coset exactly (the partial fractions are shift-independent,
so one exact computation serves all cosets; `J_u` from the exact truncated
Volkenborn series), then asks two questions.

**(1) The sums the theory needs.** Plain sum and all `φ(p^r)` Teichmüller twists
`Σ_j ω(j)^k S_n(j/p^r)`:

| configuration | `min_j v_p` at the largest n | best twisted sum | gain |
|---|---|---|---|
| p=5, A=2, bricks on 1/5, n=27 | 70 | 71 | **+1** |
| p=5, A=4, bricks on 1/5, n=21 | 109 | 109 | **0** |
| p=5, A=4, spread over 4 cosets, n=21 | 134 | 136 | **+2** |
| p=5, A=4, 2+2 reflection split, n=21 | 109 | 110 | **+1** |
| p=5, A=4, m=1, δ=1, n=21 | 109 | 110 | **+1** |
| p=7, A=3, δ=1, on 1/7, n=18 | 65 | 65 | **0** |
| p=7, A=3, spread, n=18 | 65 | 66 | **+1** |
| p=5, r=2 (20 cosets), n=30 | 139 | 140 | **+1** |

**Gains are 0–3 in absolute terms and do not grow with `n`.** The requirement is
`Ω(n)` (specifically `E·n ≥ 3n`).

**(2) The sharp question.** Normalise `u_n := (S_n(j))_j / p^{min_j v_p}` (so some
coordinate is a unit). A *fixed* `c ∈ ℤ_p^{φ}` gains `Ω(n)` for all `n` iff all
the directions `u_n` lie in one hyperplane to depth `Ω(n)`. That depth is
`H := max_i d_i` of the Smith normal form of the matrix `(u_n)` over ℤ_p
(unit-tested on synthetic data). Measured, once the number of `n`-values exceeds
the number of cosets:

```
  p=5 A=2 on 1/5 : H = 14, 14, 14, 14  at n = 15,18,21,24,27   (min v_p = 40 -> 70)
  p=5 A=4 on 1/5 : H = 26, 26, 26      at n = 15,18,21
  p=5 A=4 spread : H =  0,  0,  0      at n = 15,18,21
  p=5 A=4 2+2    : H = 20, 20, 20      at n = 15,18,21
  p=5 A=4 m=1 d=1: H = 28, 28, 28      at n = 15,18,21
  p=7 A=3 on 1/7 : H = 11, 11, 11      at n = 14,16,18
  p=7 A=3 spread : H = 10, 10, 10      at n = 14,16,18
```

**`H` is constant in `n`** while `min_j v_p(S_n)` grows linearly. So no fixed
ℤ_p-combination of the cosets — twisted, plain or arbitrary — gains more than a
bounded number of digits.

> **M3 verdict: the hatch is SHUT, over the range** `p ∈ {5,7}`, `r ∈ {1,2}`,
> `A ∈ {2,3,4}`, `m ∈ {0,1}`, `δ ∈ {0,1}`, bricks aligned / spread / reflection-split,
> `n ≤ 27` (p=5), `n ≤ 18` (p=7), `n ≤ 30` (p=5, r=2).
> **Gain over the per-coset minimum ≤ 3 absolute; hyperplane depth ≤ 28, constant.**
> Not a proof of impossibility; a fair sweep with a clean negative.
> *(Caveat: the `p=5, r=2` run has 20 cosets and only 9 values of `n`, so its `H`
> is rank-deficient and uninformative; its ω-twist gain is +1.)*

---

## 6. M4 — THE MAP

### 6.1 Rank 1, DIG-1's ledger `E` — independently re-derived `[COMP]`

Exhaustive over `r ≤ 3`, `A ≤ 14`, `0 ≤ m ≤ w+2`, `δ ∈ {0,1}`, all coset spreads
(DIG-1 used `A ≤ 6`, `m ∈ {w−3,w−4}`). **The table is reproduced exactly** — an
independent confirmation of DIG_LEDGER §4.3:

| p \ w | 3 | 5 | 7 | 9 |
|---|---|---|---|---|
| **2** | **+1.1589** (μ 7.18, known) | **+0.5452** (μ 20.34, known) | −1.4548 | −3.4548 |
| **3** | **+0.2958** (μ 22.28, known) | −1.7042 | −3.7042 | −5.7042 |
| **5** | −3.0000 | −2.9882 | −4.9882 | −6.9882 |
| **7** | −3.0000 | −4.0000 | −6.0000 | −8.0000 |
| **11** | −3.0000 | −4.0000 | −6.0000 | −8.0000 |
| **13** | −3.0000 | −4.0000 | −6.0000 | −8.0000 |

### 6.2 Rank 1, **corrected (measured) `E`** — the honest map `[COMP]`

| p | w | ledger margin | `E_led` | **`E_true`** | **TRUE margin** | μ | config |
|---|---|---|---|---|---|---|---|
| 2 | 3 | +1.1589 | 3 | 3 | **+1.1589** | 7.17740 | r=1 A=3 m=0 δ=1 **[published]** |
| 2 | 5 | +0.5452 | 5 | 5 | **+0.5452** | 20.34265 | r=1 A=4 m=1 δ=1 **[published]** |
| 2 | 7 | −1.4548 | 7 | **11** | **−5.4548** | — | r=1 A=4 m=3 δ=1 |
| 2 | 9 | −3.4548 | 9 | 15 | −9.4548 | — | r=1 A=4 m=5 δ=1 |
| 3 | 3 | +0.2958 | 3 | 3 | **+0.2958** | 22.28145 | r=1 A=2 m=0 δ=0 **[published]** |
| 3 | 5 | −1.7042 | 5 | 6 | **−3.8028** | — | r=3 A=4 m=1 δ=0 |
| 3 | 7 | −3.7042 | 7 | 12 | −8.7042 | — | r=1 A=2 m=4 δ=0 |
| 3 | 9 | −5.7042 | 9 | 16 | −12.7042 | — | r=1 A=2 m=6 δ=0 |
| 5 | 3 | −3.0000 | 3 | 3 | **−3.0000** | — | r=1 A=2 m=0 δ=0 |
| 5 | 5 | −2.9882 | 5 | 6 | −3.9882 | — | r=1 A=4 m=1 δ=0 |
| 5 | 7 | −4.9882 | 7 | 12 | −9.9882 | — | r=1 A=4 m=3 δ=0 |
| 5 | 9 | −6.9882 | 9 | 16 | −13.9882 | — | r=1 A=4 m=5 δ=0 |
| 7 | 3 | −3.0000 | 3 | 3 | **−3.0000** | — | r=1 A=2 m=0 δ=0 |
| 7 | 5 | −4.0000 | 4 | 5 | −5.0000 | — | r=1 A=3 m=1 δ=0 |
| 7 | 7 | −6.0000 | 6 | 11 | −11.0000 | — | r=1 A=3 m=3 δ=0 |
| 7 | 9 | −8.0000 | 8 | 15 | −15.0000 | — | r=1 A=3 m=5 δ=0 |
| 11,13 | 3/5/7/9 | −3/−4/−6/−8 | | 3/5/11/15 | −3.0000 / −5.0000 / −11.0000 / −15.0000 | — | as p=7 |

> **THE HEADLINE ROW.** The three published results are exactly the three positive
> cells and they are untouched by every correction. **After the correction the
> nearest miss in the whole family is no longer ζ₂(7): it is ζ₅(3) and ζ₇(3) at
> −3.000** — and those two are the *hardest* cells structurally (§6.4), because
> there the deficit is `−E` exactly, with the p-adic smallness cancelling the
> archimedean growth to the last digit.
> *(Caveat: R2 was verified for the single-shift shape; the multi-coset spreads at
> `p ≥ 5` inherit it by assumption. The p ≥ 5 conclusions do not depend on it —
> those cells are 3 to 15 short either way.)*

### 6.3 The rank axis — where the two walls actually are `[COMP]`

Best margin at rank ≤ R (ledger `E`; R > 1 gives only "one of R values"):

| p | w | rank 1 | rank 2 | rank 3 | rank 4 | min rank for margin > 0 |
|---|---|---|---|---|---|---|
| 2 | 3 | +1.1589 | +3.2383 | +4.3178 | +5.3972 | **1** |
| 2 | 5 | +0.5452 | +2.2383 | +4.3178 | +5.3972 | **1** |
| 2 | 7 | −1.4548 | **+1.3178** | +2.7041 | +4.3972 | **2** |
| 2 | 9 | −3.4548 | −0.6822 | **+2.0904** | +3.4766 | **3** |
| 3 | 3 | +0.2958 | +1.9438 | +2.5917 | +3.2396 | **1** |
| 3 | 5 | −1.7042 | **+0.9438** | +2.5917 | +3.2396 | **2** |
| 3 | 7 | −3.7042 | −1.0562 | **+0.5917** | +2.2396 | **3** |
| 3 | 9 | −5.7042 | −3.0562 | −1.4083 | **+0.2396** | **4** |
| 5 | 3 | −3.0000 | −1.9882 | −1.9882 | −1.9882 | **none ≤ 4** |
| 5 | 5 | −2.9882 | −1.9882 | −1.9882 | −1.9882 | **none ≤ 4** |
| 5 | 7 | −4.9882 | −3.9882 | −3.9882 | −3.9764 | **none ≤ 4** |
| 5 | 9 | −6.9882 | −5.9882 | −4.9764 | −3.9764 | **none ≤ 4** |
| 7 | 3 | −3.0000 | −3.0000 | −3.0000 | −3.0000 | **none ≤ 4** |
| 7 | 5 | −4.0000 | −4.0000 | −3.7298 | −3.7298 | **none ≤ 4** |
| 7 | 7 | −6.0000 | −4.7298 | −3.7298 | −3.7298 | **none ≤ 4** |
| 7 | 9 | −8.0000 | −6.7298 | −5.7298 | −5.7298 | **none ≤ 4** |
| 11, 13 | 3 / 5 / 7 / 9 | −3 / −4 / −6 / −8 | identical at every rank ≤ 4 | | | **none ≤ 4** |

**Read the table as: at `p ∈ {2,3}` the wall is rank; at `p ≥ 5` the wall is size.**
Two different obstructions, and the campaign has been treating them as one.

### 6.4 The structural ceiling `[DERIVED + VERIFIED]`

| p | `p log p/(p−1)²` | verdict at rank 1 |
|---|---|---|
| 2 | 1.386294 | size never binds: `margin = M(2log2−1) − m → +∞` |
| 3 | 0.823959 | `margin ≤ A(0.8240 − 1) − 1 < 0` for every A |
| 5 | 0.502949 | `margin ≤ A(0.5029 − 1) − 1 < 0` |
| 7 | 0.378371 | `margin ≤ A(0.3784 − 1) − 1 < 0` |
| 11 | 0.263768 | `< 0` |
| 13 | 0.231558 | `< 0` |

---

## 7. Non-vanishing

No M1/M2 winner exists, so nothing needs a non-vanishing argument. For the
record, the two objects that *would* have needed one:

* the `M=6, m=1` rank-2 family (margin +1.3178) inherits LSZ's route: the parity
  law gives `ρ_2 = ρ_4 = ρ_6 = 0` identically and the surviving `ρ_3, ρ_5` are
  non-zero at every `n` tested (`n ≤ 60`, exact); a Casoratian argument in the
  style of LSZ Lemma 15b would be the natural proof. It is moot: §3.3 shows the
  form cannot be reduced to rank 1.
* the `m = −1` route is dead on smallness (§1), not on vanishing — though note
  `ρ₀ ≡ 0` identically for `M` odd with `m = −1` and for `M` even with `m` even,
  which is worth recording as a degeneracy of the family.

Per DIG-2 §10, orbit moves rescale the whole form by `κ ≠ 0` and so preserve
non-vanishing; that remains available and unused.

---

## 8. Files

| file | contents |
|---|---|
| `work/dig/s_vwp.py` | the p=2 VWP cone with insets; the **parity law**; LSZ anchors reproduced |
| `work/dig/s_meas.py` | exact measurement of `α` (Volkenborn), growth, `E`; the `m=−1` verdict |
| `work/dig/s_den.py` | the **true `E`**, prime band by prime band; rules R1, R2 |
| `work/dig/s_elim.py` | mod-q partial fractions (validated against exact ℚ); inset lattice |
| `work/dig/s_recur.py`, `s_rank.py` | the **rank-reduction test** + positive control |
| `work/dig/s_cone.py` | the length cone: `G`, `C₁`, `E` measured off-symmetry |
| `work/dig/s_record.py` | M2: the record scan with measured `E` and `C₁` |
| `work/dig/s_coset.py` | M3: exact coset valuations, ω-twists, Smith-form hyperplane depth |
| `work/dig/s_map.py` | M4: the map, ledger `E` and corrected `E` |

## 9. Open items

1. **Prove R2.** `c = m+1` for `m ≥ A−1` is a clean statement about when the odd
   primes in `(n,2n)` cancel in `Σ_{i,k} r_{i,k}(i)_{m+1}T_{k,i+m+1}`. It is a
   Nesterenko/Zudilin-style denominator lemma and looks provable; it would make
   Correction 2 `[PROVED]` rather than `[VERIFIED, 0/…]`, and it sharpens every
   published `d_n`-bound in the `m ≥ 2` range.
2. **Prove the module statement** behind §3.3 (`ker ρ_{w'} ⊆ ker ρ_w` for the
   VWP difference module). This is the exact p-adic analogue of why
   "one of ζ(5),…,ζ(11)" is never sharpened, and it would turn the ζ₂(7)
   obstruction into a theorem.
3. R2 for multi-coset spreads at `p ≥ 5` (assumed, not measured — §6.2 caveat).
4. DIG-2's Gauss-duplication bridge (open item #2 there) is untouched here; §4
   shows it cannot buy a record inside this cone, but it remains the only route
   by which the 1920-element orbit could reach a genuinely p-adic base point.
