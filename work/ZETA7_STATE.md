# ζ(7) / M₀,₁₀ CAMPAIGN — COMPLETE STATE EXTRACTION

**Purpose.** Everything a new session needs to resume the weight-7 campaign without
re-deriving anything. Target of the new session: the **γ₅,₇ pair-worthiness** number
for the weight-7 M₀,₁₀ cellular family.

**Source repo (READ-ONLY):** `/home/ubuntu/fable-episode-2/zeta-math/`
All paths below are absolute unless prefixed `worthiness/`, which means
`/home/ubuntu/fable-episode-2/zeta-math/worthiness/`.

**Extraction date:** 2026-07-24. Campaign dates: 2026-07-16 → 2026-07-20.

**Reading conventions.** Direct quotes from campaign files are in blockquotes or fenced
blocks and are verbatim. `[INFERRED]` marks my own deduction. `[MISSING]` marks something
the campaign never produced.

---

## ⚡ TL;DR — THE FIVE THINGS THAT MATTER MOST

1. **The recurrence is ALREADY SOLVED.** Order 4, degree 19, exact integer operator,
   CRT-reconstructed and certified against all 74 exact terms. Lives in
   `worthiness/zeta7_q_recurrence.json`. **Do not re-guess it.** (I re-verified it in
   this extraction: 70 annihilation relations, all exactly zero.)
2. **74 exact q_n (n=0…73)** in `worthiness/zeta7_lc_terms.txt`; **105 modular terms
   (n=0…104) at 3 primes** in `worthiness/_zeta7_state_backup/fleet_*.txt`.
   The "~90-term extension in progress" in `README.md` item 8 is **stale** — it completed
   and went past 90.
3. **Characteristic polynomial** `χ(λ) = λ⁴ − 6340λ³ + 67974λ² − 6340λ + 1` (palindromic),
   roots `{6329.2605, 10.6454, 0.0939374, 0.000157996}`, two reciprocal "sectors".
4. **THE BLOCKER for γ₅,₇:** this operator governs the *weight-5 descent ladder*
   (q, s, P̂, I″) — **not** the primitive weight-7 form I′ₙ / Pₙ. Which sector I′ rides is
   the whole game: sector A root 1.58e-4 ⇒ γ-style pass; sector B root 0.0939 ⇒ fail.
   The campaign's best evidence says **sector B** (fail).
5. **den(P₃)** is *conditionally* `2⁵·3⁷ = 69984` (P₃ = 23478462179525/69984) by a
   denominator "snap", verified to 99.75% by rigorous lower bounds — but **not proved**.

---

## 1. DEFINITIONS — regenerating q_n from scratch

### 1.1 The cell and the primal integral

The family is Brown–Zudilin's **totally symmetric ζ(7) cellular integral on M₀,₁₀**, the
"vanishing in the middle" convergent permutation

    σ = (10, 2, 4, 1, 6, 3, 8, 5, 9, 7),    N = 10

Source: BZ `.../bz/2026-01-26_CellZeta.tex`, lines ~1443–1467 (transcribed in
`worthiness/ZETA7_FAMILY.md` §1.1).

Verbatim (`worthiness/ZETA7_BARNES.md`, "Target and anchors"):

```
    I_n = ∫_{0<t1<...<t7<1}  (B/D)^n · dt / D,
    B = t1(t2−t1)(t3−t2)(t4−t3)(t5−t4)(t6−t5)(t7−t6)(1−t7),
    D = (t3−t1) t3 t5 (t5−t2)(t7−t2)(t7−t4)(1−t4)(1−t6).
```

(Equivalently Iₙ = ∫ Bⁿ / Dⁿ⁺¹, over the ordered 7-simplex.)

### 1.2 The two-ladder period decomposition (BZ + campaign refactoring)

Verbatim (`worthiness/ZETA7_FAMILY.md` §1.3, re-confirmed in `ZETA7_DUAL.md` §0 and
`ZETA7_P3_VERIFICATION.md` §4):

```
    I_n  = I′_n + I″_n · ζ(2)
    I′ₙ  = (75/4)·qₙ·ζ7  − 3·sₙ·ζ5  − Pₙ      ∈ span{1, ζ5, ζ7}   (NO ζ3)
    I″ₙ  =    −9·qₙ·ζ5   + 2·sₙ·ζ3  − P̂ₙ      ∈ span{1, ζ3, ζ5}   (NO ζ7)
```

with the BZ-printed anchors

```
    qₙ = 1, 61, 52921          (shared: ζ7-coeff of I′ and ζ5-coeff of I″)
    sₙ = 0, 300, 261153        (shared: ζ5-coeff of I′ and ζ3-coeff of I″)
    Pₙ = 0, 220, 6021219/32
    P̂ₙ = 0, 152, 535857/4
```

BZ's printed exact forms (verbatim, `ZETA7_FAMILY.md` §1.2):

```
    I₀ = 75/4·ζ7                                − 9·ζ5·ζ2
    I₁ = (61·75/4·ζ7 − 300·3·ζ5 − 220)         − (61·9·ζ5 − 300·2·ζ3 + 152)·ζ2
    I₂ = (52921·75/4·ζ7 − 261153·3·ζ5 − 6021219/32)
                                               − (52921·9·ζ5 − 261153·2·ζ3 + 535857/4)·ζ2
```

Numerical anchors: `I₀ = 3.55544884724898403886…`, `I₁ = 3.2070602345247e-5`,
`I₂ = 1.05312589331082e-9` (see GOTCHA G1 below about "1.10e-9"),
`I₃ = 5.6299224184893e-14` (conditional / numerically pinned).
Primitive form values: `I′₀ = 18.91…`, `I′₁ = 0.0645…`, `I′₂ = 0.00116…`,
`I′₃ ≈ 3.56748e-5` (conditional).

Motive: **rank 4**, semisimple pieces `ℚ(0) ⊕ ℚ(−2) ⊕ ℚ(−5) ⊕ ℚ(−7)`. Period basis of the
full Iₙ closes on `{1, ζ(2), ζ(3), ζ(5), ζ(7), ζ(2)ζ(3), ζ(2)ζ(5)}` — **no genuine MZVs
appear** at the totally symmetric point (`ZETA7_FAMILY.md` §1.4).

### 1.3 The McCarthy–Osburn–Straub diagonal construction — AS IMPLEMENTED

This is the **only working route to q_n** and the thing to regenerate from.
Reference: arXiv:1705.05586 (McCarthy–Osburn–Straub, *Sequences, modular forms and
cellular integrals*), §3.2 residue method. Campaign write-up:
`worthiness/ZETA7_BARNES.md` §8.

Verbatim statement of the construction:

```
    A_σ(n) = J_σ(n) = [ (x_1 x_2 ⋯ x_m)^n ] ( ∏_i W_i )^n,
```

> where the W_i are the numerator differences z_j−z_{j+1} written as *window-sums*
> of the σ-gap coordinates x_i (the paper proves A_σ = J_σ via a common recurrence).

**Applied to our cell** (verbatim, `ZETA7_BARNES.md` §8):

> Fixing z_{σ(8)}=1, z_{σ(9)}=0, z_{σ(10)}=∞ and setting x_i = σ-gaps (x_8=1
> homogeniser), the eight numerator differences become the window-sums (variable index
> sets)

```
    W₁={2,3}, W₂={2,3,4,5}, W₃={3,4,5}, W₄={3,4,5,6,7},
    W₅={5,6,7}, W₆={7,8}, W₇={1,…,8}, W₈={1,2,3},

    q_n = A_σ(n) = [ (x_1⋯x_8)^n ] (∏_{i=1}^8 W_i)^n.
```

Here `W_i` denotes the linear form `Σ_{j ∈ W_i} x_j`, and `[…]` is the coefficient of the
**diagonal** monomial `x₁ⁿ⋯x₈ⁿ`. Normalization: **no prefactor** — q₀ = 1 exactly.

Reference implementation (the ground-truth generator):
`worthiness/zeta7_mos_leadcoeff.py` — 8-variable capped DP over the exponent vector,
multinomial distribution of n tokens per window. Windows hardcoded as
`W = [ {2,3}, {2,3,4,5}, {3,4,5}, {3,4,5,6,7}, {5,6,7}, {7,8}, {1,2,3,4,5,6,7,8}, {1,2,3} ]`.

**Faster ground-truth generator:** `worthiness/zeta7_mos_qn2.py` — integer *bucket
elimination* using partial row-sums of the active windows, with the multinomial built by
telescoping (`multinomial(n;a) = ∏_step C(cumsum, a_step)`). Same windows. Used with
CLI args `python3 zeta7_mos_qn2.py 25 26 27 …`.

### 1.4 The low-coupling re-representations (what you actually compute with)

The diagonal value q_n is **representation-independent**: any interval-window set on
{1..8} whose diagonal equals q_n is a valid model. The campaign found **41** such sets
with no full-width coupler (see §4). Two are wired into the production scripts:

```
 W_lc = {1,2}, {1,2,3,4}, {2,3,4,5}, {3,4,5}, {4,5,6}, {4,5,6,7}, {5,6,7,8}, {7,8}
 W_r2 = {1,2}, {1,2,3},   {2,3,4},   {2,3,4,5,6}, {3,4,5,6,7}, {5,6,7}, {6,7,8}, {7,8}
```

`W_lc` is the **unique pure bandwidth-4** representation among the 41
(`ZETA7_CT_CERTIFICATE.md` "Representation": *"every other low-coupling rep contains a
size-5 window"*). Its variable incidence: `x4,x5` in 5 windows each (hot center);
`x1,x8` in 2; `x2,x3,x6,x7` in 3.

Scripts:
- `worthiness/zeta7_lc_exact_dp.py` — exact-integer DP, both reps, `validate` mode
  (checks against 13 known q_n) or single-n mode. **The fast exact path.**
- `worthiness/zeta7_lc_modular_dp.py` — modular DP mod p, both reps,
  *within-window incremental token distribution (n² per window, not n⁴)*. **The fast
  modular path.** Usage: `python3 zeta7_lc_modular_dp.py lc 2000000011 95`.

### 1.5 Independent validation of the window construction

Verbatim (`ZETA7_BARNES.md` §9):

> The same window-construction applied to the M₀,₆ cell σ₆=(1,5,3,6,2,4) gives windows
> {1,2,3,4},{3,4},{2,3},{1,2,3} whose diagonal is **exactly the Apéry ζ(3) numbers
> 1, 5, 73, 1445, 33001, 819005**.

This is the "validated twice" of README item 8: (i) reproduces BZ's printed
`q₀,q₁,q₂ = 1, 61, 52921`, and (ii) the *unchanged* construction reproduces the
classical Apéry ζ(3) numbers on M₀,₆.

The **BZ ζ(5) / M₀,₈ analogue** (needed for the γ₅ side of γ₅,₇):
`Q_n = Σ_{k₁,k₂} C(n+k₁,n)C(n,k₁)²·C(n+k₂,n)C(n,k₂)²·C(n+k₁+k₂,n) = 1, 21, 2989, 714549,
217515501, …`; as windows (low-coupling set used for CT):
`{1,2,3},{1,2,3,4},{2,3},{2,3,4,5},{3,4,5,6},{4,5,6}` (max size 4)
(`ZETA7_CT_COUPLING_REPORT.md` §4).

### 1.6 The J-form (for anyone re-attacking I′ₙ analytically)

Two exactly-verified changes of variables reduce the 7-fold simplex integral to a 7-fold
cube integral (verbatim, `ZETA7_BARNES.md` Stages 1–2, both `sympy`-verified `ratio ≡ 1`
for **general symbolic n**):

Stage 1 (simplex → cube, `x_i = t_i / t_{i+1}`, `t_8 := 1`):

```
    I_n = ∫_{[0,1]^7}
          x1^n x2^{2n+1} x3^n x4^{2n+1} x5^n x6^{2n+1} x7^n
          · ∏_{i=1}^7 (1−x_i)^n / (P1 P2 P3 P4 P5 P6)^{n+1}  dx,
    P1 = 1−x1x2,   P2 = 1−x2x3x4,   P3 = 1−x2x3x4x5x6,
    P4 = 1−x4x5x6, P5 = 1−x4x5x6x7, P6 = 1−x6x7.
```

Stage 2 (J-form, leaf collapse `x1=(1−y1)/(1−y1y2), x2=1−y1y2, x7=(1−y7)/(1−y6y7),
x6=1−y6y7`):

```
    I_n = ∫_{[0,1]^7}
          y4^{2n+1} · ∏_{i≠4} y_i^n · ∏_{i=1}^7 (1−y_i)^n / (P2 P3 P4 P5)^{n+1} dy,
    P2 = 1 − y3 y4 (1−y1 y2),
    P3 = 1 − y3 y4 y5 (1−y1 y2)(1−y6 y7),
    P4 = 1 − y4 y5 (1−y6 y7),
    P5 = 1 − y4 y5 (1−y7).
```

Single-centre identity (verbatim, §5f): all four coupled factors share the centre y₄:

```
    P2 = 1 − y₄·L,      P4 = 1 − y₄·R,
    P5 = 1 − y₄·R',     P3 = 1 − y₄·L·R,
    with  L = y₃(1−y₁y₂),  R = y₅(1−y₆y₇),  R' = y₅(1−y₇).
```

Scripts: `zeta7_barnes_stage1.py`, `zeta7_barnes_stage2.py`, `zeta7_barnes_jform.py`,
`zeta7_barnes_stage3.py`, `zeta7_barnes_refl.py`, `zeta7_barnes_jform_mc.py`.

### 1.7 The all-positive 4-fold series for Iₙ (verified; the numeric workhorse)

Verbatim (`ZETA7_BARNES.md` §5f, `zeta7_barnes_num1.py`):

```
    I_n = Σ_{a,b,c,d≥0} C(n+a,a)C(n+b,b)C(n+c,c)C(n+d,d) · G₂(a+b) · H₂(b+c,d)
          · B(n+a+b+1,n+1) · B(2n+2+a+b+c+d,n+1) · B(n+b+c+d+1,n+1),
    G₂(p)=∫∫ y₁^n(1−y₁)^n y₂^n(1−y₂)^n(1−y₁y₂)^p = Σ_k(−1)^k C(p,k)B(n+1+k,n+1)²,
    H₂(q,r)=Σ_j(−1)^j C(q,j)B(n+j+1,n+1)B(n+j+1,n+r+1),  B = Euler Beta.
```

**Every summand is a positive rational** ⇒ any box partial sum is a *rigorous lower
bound* for Iₙ. Reproduces I₀, I₁, I₂ exactly.

New exact structural result at n=0 (verbatim, `ZETA7_RESIDUE_I3.md` §1a):

```
    G2(p) |_{n=0}   = H_{p+1}/(p+1),
    H2(q,r) |_{n=0} = (H_{q+r+1} - H_r)/(q+1),        H_m = sum_{i<=m} 1/i.

    I_0 = sum_{a,b,c,d>=0}  H_{a+b+1}/(a+b+1)^2 · (H_{b+c+d+1}-H_d)/(b+c+1)
                            · 1/((a+b+c+d+2)(b+c+d+1)),
```

i.e. an explicit weight-7 harmonic 4-fold Euler sum. This is the entry point for any
symbolic MZV reduction of I′₃.

---

## 2. DATA INVENTORY

### 2.1 EXACT q_n — 74 terms, n = 0 … 73  ★ THE PRIMARY ASSET

**File:** `/home/ubuntu/fable-episode-2/zeta-math/worthiness/zeta7_lc_terms.txt`
Format: one `q_<n> = <integer>` per line, 74 lines + a 4-line header. q₇₃ has 270 digits.

Header (verbatim):
```
# Exact leading coefficients q_n of the totally-symmetric M_{0,10} zeta(7) cellular integral.
# n=0..30: MOS ground truth (zeta7_mos_qn_values.txt). n=31..73: low-coupling-window DP (rep W_lc),
# cross-validated: (i) W_lc reproduces all 31 ground-truth q_n; (ii) second rep W_r2 agrees exactly
# for the overlap computed (n=31,32,...); (iii) modular DP at 4 primes ~2e9 matches all terms mod p.
```

First terms:
```
q_0 = 1
q_1 = 61
q_2 = 52921
q_3 = 94357501
q_4 = 235634763001
q_5 = 715362962769061
q_6 = 2467090298135229481
q_7 = 9307547697979861686781
q_8 = 37534429062230228638731001
q_9 = 159353643933835371998356995061
```

**Secondary file:** `worthiness/zeta7_mos_qn_values.txt` — q₀…q₃₀ (31 terms), the MOS
ground truth, generated by `zeta7_mos_qn2.py`.

### 2.2 MODULAR q_n — 105 terms, n = 0 … 104, at 3 primes

Directory: `worthiness/_zeta7_state_backup/`

| file | prime | terms | range |
|---|---|---|---|
| `fleet_2000000011.txt` | 2000000011 | 106 lines | n=0…104 (+1 dup) |
| `fleet_2000000033.txt` | 2000000033 | 105 | n=0…104 |
| `fleet_4611686018427388039.txt` | 4611686018427388039 (63-bit) | 105 | n=0…104 |
| `fleet_1999999973.txt` | 1999999973 | 78 | n=0…77 |
| `fleet_1999999943.txt` | 1999999943 | 78 | partial |
| `fleet_2000000063.txt` | 2000000063 | 74 | partial |
| `mlc_p1.txt`, `q4_loc.txt`, `loc33.txt`, `snk33.txt`, `tia33.txt`, `snake_63.txt`, `stage_63.txt`, `tiamat_63.txt`, `local_tail_63.txt` | — | shards | worker outputs merged into the fleet files |

Format: `n=value` per line. `worthiness/zeta7_crt_recon.py` loads `fleet_*.txt` by
globbing and parsing the prime out of the filename.

**Did the "~90-term extension" complete? YES.** `README.md` item 8 (dated 2026-07-18)
still says *"extension to ~90 terms and the recurrence campaign in progress"* — that
sentence is **stale**. `ZETA7_BARNES.md` §10 (2026-07-17) records the finished state:
74 exact + 105 modular terms, and the recurrence resolved. `seq_ext.log` shows the DP
running to n=104 and starting n=105 (n=105 apparently never landed).

### 2.3 The recurrence operator — EXACT, CERTIFIED  ★ THE SECOND PRIMARY ASSET

**File:** `/home/ubuntu/fable-episode-2/zeta-math/worthiness/zeta7_q_recurrence.json`
(byte-equivalent duplicate at `worthiness/_zeta7_state_backup/recurrence.json`).

JSON keys: `order` (=4), `deg` (=19), `Cpoly` (5 lists of 20 integers,
`Cpoly[k][j]` = coefficient of `n^j` in `c_k(n)`), `certified` (=true), `ntested` (=70),
`char_lead` (=`[7381728, -46800155520, 501765579072, -46800155520, 7381728]`).

Operator: `L = Σ_{k=0}^{4} c_k(n) S^k`, each `c_k` a degree-19 integer polynomial,
coefficients up to ~10²¹ (largest observed: 1358592890809078378955).

**I re-verified in this extraction:**
- `Σ_{k=0}^4 c_k(n) q_{n+k} = 0` for **all n = 0…69** (70 relations, all exactly zero)
  against the 74 exact terms.
- `c_0(−1) = 0` exactly (the trailing-coefficient vanishing that enables index-3
  propagation from indices 0,1,2). Full `c_k(−1)` vector:
  `[0, −216940730600, 52220782728840, −31452965849800, 17606837160]`.

Leading (n¹⁹) coefficients: `[c₀,c₁,c₂,c₃,c₄] = 7381728·[1, −6340, 67974, −6340, 1]` —
palindromic.

Characteristic polynomial (verbatim, `ZETA7_BARNES.md` §10.2b):

```
      χ(λ) = λ⁴ − 6340 λ³ + 67974 λ² − 6340 λ + 1     — PALINDROMIC (self-reciprocal)
```

Roots (`ZETA7_IMPLICATIONS_FROM_SOL.txt` §5), in two reciprocal pairs:

```
    6329.2605   <-->  0.000157996        (SECTOR A)
      10.6454   <-->  0.0939374          (SECTOR B)
```

`log λ_max = 8.752938686…`. Factorization over ℚ(√3) (verbatim, Sol):

```
    chi(lambda) = (lambda^2 - (3170 + 1824 sqrt(3)) lambda + 1)
                  (lambda^2 - (3170 - 1824 sqrt(3)) lambda + 1)
```

### 2.4 Companion / P-side data

| quantity | value | status | source |
|---|---|---|---|
| q₃ | 94357501 | **EXACT** (MOS diagonal, 2 independent methods; also recovered by the n=−1 propagation) | `ZETA7_BARNES.md` §8 |
| s₃ | **1396906795/3** | exact *given* that s satisfies L (74-term certified, not a theorem) | `ZETA7_BARNES.md` §10.4 |
| P̂₃ | **232175579999/972** (972 = 2²·3⁵) | same conditionality | `ZETA7_BARNES.md` §10.4 |
| P₃ | **23478462179525/69984**, den = 2⁵·3⁷ | **CONDITIONAL** ("snap"); see §7 | `ZETA7_P3_SNAP.md` |
| I₃ | 5.6299224184893e-14 | numerical, 99.75% verified by rigorous lower bounds | `ZETA7_P3_VERIFICATION.md` |
| I′₃ | ≈ 3.56748e-5 (= 3.5674902958e-5) | conditional on P₃ | `ZETA7_RESIDUE_I3.md` §5a |
| P₄, s₄, P̂₄ | — | **[MISSING]** never computed | — |

**den(P₃) status:** *conditionally* `2⁵·3⁷ = 69984`, i.e. `den(P₃) | d₃⁷ = 2⁷·3⁷` with
ord₃ = 7 tight, ord₂ = 5 (slack 2²), **no 12 = 2²·3 excess**. Depends on two hypotheses
(verbatim, `ZETA7_P3_SNAP.md`): *(i) `den(P₃) | 12·d₃⁷` (snap-grid hypothesis); (ii) the
ladder identification (s₃, P̂₃ exact)*. There is **no proved exact P₃**.

**No P_n data beyond n=3 for the weight-7 family exists anywhere in the repo.**

### 2.5 Weight-5 (M₀,₈ / ζ(5)) companion data — relevant to the γ₅ half of γ₅,₇

- `worthiness/falsify_data/ladder_Q.json`, `ladder_P.json`, `ladder_Ph.json` —
  **exact (Q_n, P_n, P̂_n) for n = 0 … 360**, stored as `[num, den]` string pairs.
  `falsify_data/manifest.json`: `{"hi": 360, "keys": ["Q","P","Ph"], "recurrence":
  "normalized order-3 (V6b)"}`. Generator `worthiness/falsify_data.py`.
- The exact ζ(5) order-3 recurrence, verbatim from `falsify_data.py`:
  ```
    c0(n) = (n+1)^5 (n+2) a0(n+1)
    c1(n) = -2 (n+2) B8(n)          B8 = deg-8 poly
    c2(n) = -2 B9(n)                B9 = deg-9 poly
    c3(n) = 2 (n+3)^5 (2n+5) a0(n)        <- LEADING coefficient
    a0(n) = 41218 n^3 + 198849 n^2 + 320790 n + 173057   (irreducible cubic)
  ```
- ζ(5) characteristic polynomial: `4λ³ − 2368λ² − 188λ + 1` (also written
  `41218·(4λ³−2368λ²−188λ+1)` as the leading-coefficient vector), roots
  `{592.07938, 0.00500378, −0.08438432}`. **Confirmed three independent ways**
  (ore_algebra guess on 70 terms; the modular-nullspace finder; BZ's printed values).
- `worthiness/gamma.py` — the **worthiness exponent implementation for the BZ ζ(5)
  family**, reproducing all the paper's printed γ values to 8 decimals. See §7.3.
- `worthiness/salvage_v6_recur.py`, `salvage_data.py`, `salvage_cache.pkl` — see §5.4.

### 2.6 Numerical / high-precision residue and period values

| quantity | value | precision | file |
|---|---|---|---|
| I₀ | 3.55544884724898403886… | exact closed form (75/4)ζ7 − 9ζ5ζ2 | `ZETA7_BARNES.md` |
| I₁ | 3.2070602345247e-5 | exact closed form | `ZETA7_FAMILY.md` |
| I₂ | 1.05312589331082e-9 | exact closed form | `ZETA7_P3_VERIFICATION.md` |
| I₃ lower bound (exact rational) | S₂₂ = 4.6242e-14 (154-digit numerator) | rigorous | `zeta7_p3_series.py` |
| I₃ lower bound (float, 15-digit-validated) | S₁₆₀ = 5.615790e-14 (99.75%) | rigorous mod float rounding | `zeta7_p3_series_fast.py` |
| I₃ upper bound | **3.0903e-9** (proved separable majorant) | rigorous | `zeta7_p3_upperbound.py` |
| I₃ (claim) | 5.6299224184893e-14 | numerical, extrap 0.04% | `ZETA7_P3_SNAP.md` |
| I″ ratio ladder | 0.0042, 0.0181, 0.0306, 0.0475, 0.0665, 0.0745, 0.0789, 0.0817, 0.0833 (n=29) → 0.0939374 | 240-digit propagation | `ZETA7_RESIDUE_I3.md` §3 |
| exact per-shell partial sums | I0/I1/I2/I3 shells, I3 exact rationals to N=40 (279/292-digit num/den) | exact | `worthiness/zeta7_residue_ckpt/I{0,1,2,3}_shells.json` |

**Precision note:** the sector propagation needs **≥240 guard digits** (300 dps used in
`zeta7_sector_measurement.py`) because forward propagation through L is λ_max-unstable.

### 2.7 Validation anchors ("validated twice" and the dual gate)

1. **MOS gate:** `A_σ(0)=1, A_σ(1)=61, A_σ(2)=52921` — reproduces all three BZ anchors
   including the stringent 52921 (`zeta7_mos_leadcoeff.py`).
2. **Known-answer test:** the same window construction on M₀,₆ σ₆=(1,5,3,6,2,4)
   reproduces the classical Apéry ζ(3) numbers 1, 5, 73, 1445, 33001, 819005.
3. **Dual-representation gate:** `W_lc` and `W_r2` (structurally different, both
   full 8-variable) reproduce identical q_n — *byte identical* on n=31…42; both
   reproduce all 31 MOS ground-truth terms.
4. **Modular cross-check:** the fast modular DP at four primes ≈2·10⁹ reproduces all 74
   exact q_n reduced mod p.
5. **Operator certification:** L annihilates all 74 exact q_n (70 relations, all zero).
6. **n=−1 self-check:** the recurrence at n=−1 recovers q₃ = 94357501 exactly from
   q₀,q₁,q₂; and forward-propagating q from q₀…q₃ via L reproduces all q₄…q₇₃.
7. **Filtration-sign lock:** q₁=61 is forced *twice* (ζ7 coefficient and ζ2ζ5
   coefficient) and s₁=300 twice (ζ5 and ζ2ζ3), consistently
   (`ZETA7_P3_VERIFICATION.md` §4 table).

---

## 3. PROVEN — structural theorems from the campaign

### 3.1 Sign dichotomy: I′ₙ lies OUTSIDE the single-sum very-well-poised class
**Status: [VERIFIED / EXCLUDED]** — `worthiness/ZETA7_DUAL.md` §3.4 and §7.

Statement (verbatim, §3.4):

> Every reflection-antisymmetric block series R(k) (R(−n−k) = −R(k), the structure of ALL
> Zudilin eq.7-type series, for any C) yields **same-sign** odd-zeta coefficients … But
> BZ's I′ₙ and I″ₙ have **opposite-sign** adjacent zetas (§0). A single such series
> therefore *cannot* be I′ₙ or I″ₙ, and a ζ3-kill of two same-sign-ratio companions
> cannot flip r5 negative either.

Conclusion (verbatim, §7.3):

> The BZ eliminated form I′ₙ is a *small* linear form with **opposite-sign** adjacent zeta
> coefficients; every very-well-poised single sum (symmetric or spread) is a *simultaneous
> approximation* whose adjacent odd-zeta coefficients are **same-sign** (the constant term
> carries the cancellation). These are structurally different objects.

Evidence base: 11 284 staircase-asymmetric configs (`zeta7_dual_asym.py`) + 1 248
systematic-VWP configs (`zeta7_dual_vwpsign.py`) + symmetric-block + KR `compute_Zn`,
**all exact-rational; r5 > 0 universally among VWP-clean forms**. The only r5 < 0 configs
carry even zetas (ζ4, ζ6) ⇒ not VWP.

Target invariants that must be matched (verbatim, §0):
```
    I′ₙ:  r5 = coeff(ζ5)/coeff(ζ7),   rc = const/coeff(ζ7)
          n=1:  r5 = −48/61,          rc = −176/915
          n=2:  r5 = −1044612/1323025, rc = −2007073/10584200
    I″ₙ:  r3 = coeff(ζ3)/coeff(ζ5),   rc = const/coeff(ζ5)
          n=1:  r3 = −200/183,        rc = 152/549
          n=2:  r3 = −58034/52921,    rc = 10507/37356
```

**Corollary [EXCLUDED]:** q_n is *not* a product-weight subset-coupled multisum of the
M₀,₈ type. Exhaustive search over all triple sums with weight `C(n+k,k)^p C(n,k)^q`
(p,q≤3) and coupling any product-family of `C(n+Σ_S k_i, n)` over the 7 nonempty
subsets, plus all doubles: **none reproduces 1, 61, 52921** (`ZETA7_DUAL.md` §3.5;
`zeta7_dual_triple.py`, `_exhaust.py`, `_Awide.py`).

### 3.2 Dihedral rigidity: trivial stabilizer, no symmetric orientation
**Status: [VERIFIED]** — `worthiness/ZETA7_BARNES.md` §5b.

The dihedral group of order 20 on the 7 simplex variables, generated by

```
    σ: (t₁,…,t₇) ↦ (1−t₁/t₂, 1−t₁/t₃, …, 1−t₁/t₇, 1−t₁),
    τ: (t₁,…,t₇) ↦ (t₁, t₁/t₇, t₁/t₆, …, t₁/t₂).
```

Both preserve the open simplex; σ¹⁰ = id verified symbolically (`zeta7_barnes_group.py`).

Invariant (verbatim):

> The δ-decagon difference word of π=(10,2,4,1,6,3,8,5,9,7) is [2,2,7,5,7,5,7,4,8,3],
> multiset {2,2,3,4,5,5,7,7,7,8}. Its mod-10 negation [8,8,3,5,3,5,3,6,2,7] has multiset
> {2,3,3,3,5,5,6,7,8,8}. **The multisets differ**, so no dihedral element carries the word
> to its negation or reversed-negation: the **stabiliser of the cell is trivial**, and no
> orientation can be dihedrally symmetric.

Confirmed by an exhaustive **20-orientation leaf scan** (`zeta7_barnes_orient_scan.py`,
run distributed over 4–5 machines): all 20 orientations have 6 coupled factors; tally
**6 with a low leaf (x₁), 6 with a high leaf (x₇), 8 with none — zero with both**. The
two best-balanced profiles (σ⁵, σ⁵τ, sizes [2,2,2,3,3,5]) have **no** leaf at all.

**Consequence:** BZ's M₀,₈ two-sided leaf-collapse does *not* extend; the reduction stalls
at four coupled factors {P2,P3,P4,P5} with the stray `P5 = 1−y₄y₅(1−y₇)`. The
denominator incidence is **2 left / 1 center / 3 right** (asymmetric), vs M₀,₈'s
symmetric 2/0/2.

### 3.3 Merge failure (exact)
**Status: [VERIFIED exact]** — `ZETA7_BARNES.md` §5c, `zeta7_barnes_merge.py`.
Fusing the stray P5 with P4 via `y₆=(1−a)/(1−ab), y₇=1−ab` **strictly increases** the
coupled count 4 → 5 (the Jacobian leaves a net `(1−ab)^{−(n+1)}`). Structural reason:
each of y₄, y₅, y₇ is shared across ≥3 factors, so no leaf-collapse exists.

### 3.4 Two-ladder splitting (the campaign's most important structural finding)
**Status: [FINDING, 74-term certified but not a theorem]** — `ZETA7_BARNES.md` §10.4.

Verbatim:

> - **q, s, P̂ satisfy L.** Propagation gives **s₃ = 1396906795/3** and
>   **P̂₃ = 232175579999/972**, and the companion form **I″ₙ decays correctly** … Both
>   denominators are **2,3-smooth** (3 = 3¹; 972 = 2²·3⁵), the hallmark of genuine
>   d_n-governed clearing.
> - **P (and the weight-7 form I′) do NOT satisfy L.** The known forms decay
>   (I′₀=18.91, I′₁=0.0645, I′₂=1.16×10⁻³) but propagating I′ (or P) through L gives
>   I′₃ = 43.71 — the dominant λ_max mode fails to cancel, i.e. I′ blows up like λ_max^n.
>   The naive-propagated "P₃" carries a spurious prime **107** in its denominator
>   (2⁵·3⁸·107), confirming it is not the true value.
>
> So L is the recurrence of the **weight-5 descent** (q, s, P̂, I″), not of the full
> weight-7 period I′.

### 3.5 Sector verdict (the un-worthiness of the symmetric family at weight 7)
**Status: [ROBUST but conditional on L governing I″]** — `ZETA7_RESIDUE_I3.md` §3.

Two-step cancellation argument, needing **neither** the den-grid hypothesis **nor** an
exact P₃:
- *Fact 1:* I″ rides sector B (0.0939374) — ratios climb monotonically to it under
  240-digit propagation.
- *Fact 2:* I decays strictly faster than sector B (rigorous in magnitude:
  I₂ ≥ 9.45e-10 exact vs 3e-2 sector-B prediction — seven orders below), so I rides
  sector A (1.58e-4).
- *Conclusion (verbatim):* **"Sector-B coefficient of I′ = (B-coeff of I) − ζ₂·(B-coeff
  of I″) = (≈0) − ζ₂·(nonzero) ≠ 0. Therefore I′ₙ ~ −ζ₂ I″ₙ rides SECTOR B (0.0939)."**
- *Verdict (verbatim):* **"the primitive form I′ FAILS the irrationality threshold
  e⁻⁷=9.12e-4 (0.0939 ≫ 9.12e-4, off by two orders). The totally symmetric M₀,₁₀ ζ(7)
  cellular family is un-worthy."**

⚠ This is the **single most consequential result for γ₅,₇** — see §6 and §9-G6.

### 3.6 Ancillary verified results
- **Apéry ζ(3) recurrence re-derived** from cellular windows by iterated creative
  telescoping in **2 s** (verbatim result, `ZETA7_CT_COUPLING_REPORT.md` §3):
  `(n+2)³·q(n+2) − (34n³+153n²+231n+117)·q(n+1) + (n+1)³·q(n) = 0`.
- **BZ ζ(5) char poly `4λ³−2368λ²−188λ+1` confirmed three independent ways.**
- **Two independent CAS fail for the same structural reason** (ore_algebra, Mathematica 15
  built-ins) — non-hypergeometric ₃F₂/Appell couplings; publication-grade difficulty
  evidence (`ZETA7_BARNES.md` §7).

---

## 4. THE CT OBSTRUCTION — what it is, and what it does NOT block

### 4.1 The full-width coupling window

Verbatim (`worthiness/ZETA7_CT_COUPLING_REPORT.md` §5):

> **MOS ζ(7) windows** (cell σ=(10,2,4,1,6,3,8,5,9,7)):
> `{2,3},{2,3,4,5},{3,4,5},{3,4,5,6,7},{5,6,7},{7,8},{1,2,3,4,5,6,7,8},{1,2,3}`.
> The window **W₇ = {1..8}** is a *full-width coupler*: every CT elimination interacts
> with all 8 variables. Result: iterated CT **blew up on the 2nd elimination** regardless
> of order (7.2 GB and climbing at 47 min in one order; hit the 4 GB cap at 215 s in
> another). The 8-variable MOS-window CT is **not feasible** here.

So: the obstruction is *specific to the MOS window representation* being fed to
Koutschan-style **creative telescoping** (holonomic elimination). It is a
**computational-algebra** obstruction, not a mathematical one.

### 4.2 The 41 exact low-coupling re-representations

**Where they are stored:**
`/home/ubuntu/fable-episode-2/zeta-math/worthiness/zeta7_ct_scripts/zeta7_lowcoupling_representations.txt`
— 41 lines, each `HIT [[...],[...],...]` listing 8 interval windows on {1..8}.

**How they were found** (verbatim):

> **Key idea (River's): find a representation that doesn't blow up.** The diagonal value
> q_n is representation-independent; *any* window set whose diagonal equals q_n is a valid
> computable model. A brute-force over interval windows on {1..8} (sizes 2–5, choose 8,
> coverage-filtered) found **41 window sets reproducing q₀…q₃ = 1, 61, 52921, 94357501**
> — and one has **max window size 4, no full-width coupler**:
>
>     W_lc = {1,2},{1,2,3,4},{2,3,4,5},{3,4,5},{4,5,6},{4,5,6,7},{5,6,7,8},{7,8}
>
> Verified: `W_lc` reproduces **all 31 known q_n exactly** (n=0…30).

`W_lc` is line 16 of that file (`[[1,2],[1,2,3,4],[2,3,4,5],[3,4,5],[4,5,6],[4,5,6,7],
[5,6,7,8],[7,8]]`), and is the unique pure bandwidth-4 member. `W_r2` (the dual-gate rep)
is line 1: `[[1,2],[1,2,3],[2,3,4],[2,3,4,5],[3,4,5,6],[3,4,5,6,7],[5,6,7,8],[7,8]]`
— *note*: the version in `zeta7_lc_exact_dp.py`/`zeta7_lc_modular_dp.py` is
`{1,2},{1,2,3},{2,3,4},{2,3,4,5,6},{3,4,5,6,7},{5,6,7},{6,7,8},{7,8}` (line 3 of the
file). **Use the versions in the scripts** — those are the ones actually validated.
Search script named as `search_z7_windows.py` in `ZETA7_CT_COUPLING_REPORT.md` §8;
**that script is not present in the repo** — only its output file survives. [MISSING]

### 4.3 (a) Implication for creative telescoping

`W_lc` **does** clear the elimination that killed MOS. Measured elimination tower for the
diagonal CT (`ZETA7_CT_CERTIFICATE.md`, plus `_zeta7_state_backup/zeta7_ct_lc.log` and
`ct_run/resume.log`):

| step | var | time | #tele ops | outcome |
|---|---|---|---|---|
| 1 | x1 | 25 s | 8 | done |
| 2 | x8 | 931 s | 10 | done (13.7 MB) — **this is where MOS died** |
| 3 | x2 | 10 390 s (2h53m) | 9 | done (20.2 MB) |
| 4 | x6 | **ABORTED after 10 801 s ($TimedOut)** | — | **STOP** |
| 5–8 | x3, x7, x4, x5 | — | — | never reached |

Checkpoints preserved: `worthiness/ct_run/ckpt_after_x2.mx` (1.7 MB, state after elim
x2), `worthiness/ct_run/zeta7_lc_cur.mx` (same), `worthiness/_zeta7_state_backup/
zeta7_lc_cur.mx` (1.1 MB, state after elim x8). Resume script `worthiness/ct_run/
resume.wl`; original `worthiness/zeta7_ct_lc.wl`, `zeta7_ct_lc_resume.wl`.

The **parallel primary route** — period-level discrete CT on the all-positive 6-fold
Barnes sum (`worthiness/ct_run/barnes_ct.wl`, `barnes_ct_long.wl`) — **never completed
even its first elimination**: `barnes_ct.log`: *"elim k ABORTED after 9007s
result=$TimedOut"*; `barnes_long.log`: *"elim k ABORTED after 15687s result=$Failed"*.

**Net: NO CT certificate was ever produced.** The recurrence remains *guessed +
empirically certified*, not proved. Elimination cost grows geometrically (~5–10× per
step at the ζ(5) calibration); the wall is **time**, not RAM.

### 4.4 (b) Implication for plain recurrence GUESSING from terms

**None. The CT obstruction does not affect guessing at all.**

Reasoning (explicit in `ZETA7_CT_COUPLING_REPORT.md` §6–7 and borne out by the outcome):
guessing needs only *term values*, which are representation-independent and are produced
by the **DP**, not by holonomic elimination. The low-coupling rep matters for guessing
only because it makes the DP *fast* (bounded bandwidth ⇒ small state), not because it
removes any obstruction to the linear algebra. The recurrence was in fact found purely by
guessing (modular nullspace + CRT + rational reconstruction) while both CT runs were
still stalled.

Verbatim honest verdict (§7):

> - **ζ(7) recurrence via MOS-window CT: NO** (full-width coupler ⇒ 2nd-elimination blowup).
> - **ζ(7) recurrence via low-coupling DP + guess: LIKELY YES** — every piece is built and
>   validated; the only cost is generating ~90 terms (~30–60 min) and one guess.
> - **ζ(7) recurrence via low-coupling CT: UNCERTAIN** …

The only thing CT would add is upgrading *"annihilates 74 exact terms"* to *"annihilates
q_n for all n"* — i.e. turning a near-certain discovery into a theorem.

---

## 5. RECURRENCE HUNT — FULL STATUS (**RESOLVED**)

### 5.1 Outcome

**The hunt succeeded.** `ZETA7_BARNES.md` §10.2b, verbatim heading:

> ### 10.2b THE RECURRENCE — RESOLVED: **order 4, degree 19** [CONFIRMED]

> Extending the modular DP (memory-gated, one high-n term at a time) to **105 terms** at
> prime 2000000011 and running both the raw modular-nullspace finder and `ore_algebra`:
> - **`ore_algebra` `guess` (auto-minimal) returns order 4, degree 19**, stable whether
>   unconstrained or forced to order 4 or 5. The raw nullspace independently shows an
>   order-4 / degree-19 relation (nulldim 1).
> - (Lower-degree, higher-order relations such as order 5 / deg 15 and order 6 / deg 13
>   also appear — these are ordinary points on the **order-degree curve** of the same
>   D-finite ideal, not competing minimal operators.)

Exact operator reconstruction (verbatim):

> The exact integer operator L = Σ_{k=0}^4 c_k(n) S^k (each c_k a degree-19 integer
> polynomial, coefficients up to ~10²¹) was CRT-reconstructed from three primes (two
> 31-bit, one 63-bit, ~2^125) with a conservative rational-reconstruction pass (61
> coefficients) completed by solving the remaining 39 large coefficients from the 70 exact
> annihilation relations Σc_k(n)q_{n+k}=0. **It annihilates all 74 exact q_n.**

### 5.2 The failed / excluded (order, degree) region — the stalling history

Chronology of what was tried and what it excluded:

| stage | #terms | scripts | outcome |
|---|---|---|---|
| MOS-only | 24 | `guess` (ore_algebra) | *"finds no operator of order ≤6"* |
| MOS ground truth | 31 | scan over (order ≤6, degree) | no recurrence — **31 terms provably insufficient** |
| modular fleet | 93 | `zeta7_recurrence_guess.py` + ore_algebra | **no** recurrence with order ≤4 deg ≤16, nor order 5 deg ≤13, nor order 6 deg ≤11, nor order 3 deg ≤21, nor order 7/8 at tested degrees (nulldim 0 with equation surplus at every tested (order,deg)) |
| modular fleet | **105** | same | **order 4, degree 19, nulldim 1** ✅ |

Verbatim size-bound correction (§10.2):

> So the predecessor's "order ≈4, degree 11–13" estimate is **too small**: the minimal
> operator has (order+1)(degree+1) > 89, i.e. it is one genuine step *larger* than the
> ζ(5) analogue (plausibly order 4, degree ≳17, following the ζ(3)→ζ(5) degree jump 3→9).
> Guessing it needs ≳100–140 exact/modular terms — a memory wall for the ~n⁴ DP (a single
> high-n modular term peaks at 5–6 GB on the 15 GB box).

**Why it stalled before that: not enough terms.** The ansatz was right (P-recursive,
order ~4); the *degree* was underestimated by a factor ~2, and (order+1)(degree+1) = 100
unknowns needs >100 terms. Cost, not method, was the binding constraint.

### 5.3 The guessing pipeline — the exact scripts

- **`worthiness/zeta7_recurrence_guess.py`** ★ the main guesser. Self-contained, stdlib +
  numpy. Pipeline: load `fleet_<prime>.txt` files by glob → build the homogeneous system
  `Σ_k Σ_j c_{k,j} n^j q_{n+k} = 0` mod p → RREF → structure scan over
  `order ∈ 2..8, deg ∈ 1..25` reporting `nulldim` → pick minimal (order,deg) with
  nulldim 1 → nullvector at each usable prime → CRT → **Wang rational reconstruction**
  (`ratrecon`) → clear denominators, remove content → **certify against all exact terms**
  → extract char poly (leading coefficients) and roots → dump `recurrence.json`.
  Requires `len(seq) - order ≥ (order+1)(deg+1) + 2` per prime (surplus check).
- `worthiness/zeta7_crt_recon.py` — the CRT/rational-reconstruction driver (same file
  content as `_zeta7_state_backup/crt_recon.py`).
- `worthiness/_zeta7_state_backup/guess_crt.py`, `guess2.py`, `modw.py`, `modw2.py`,
  `mosw.py`, `qnw.py`, `rescan.py`, `orchestrator.py`, `gen_par.py`, `gen_remote.py`,
  `fleet.sh`, `ptxkill.sh` — the working fleet/orchestration versions.
- Sage variants: `worthiness/_zeta7_state_backup/oreguess.sage`, `guess_gfp.sage`,
  `minop.sage`, `ratrec_op.sage`.

### 5.4 `salvage_v6_recur.py` — the weight-5 template  ★ INVENTORIED

**Path:** `/home/ubuntu/fable-episode-2/zeta-math/worthiness/salvage_v6_recur.py`
(224 lines). Docstring verbatim:

```
V6(a,b): recover the common third-order recurrence for (q_n,p_n,p̃_n) and the
normalized (Q_n,P_n,P̂_n), by exact-fit (route ii).

Method: an order-3 recurrence  Σ_{i=0}^3 c_i(n) X_{n+i} = 0  with c_i polynomials
of degree ≤ D.  Homogeneous linear in the {c_{i,d}}.  We (1) find the minimal D
and the nullspace mod a large prime using ALL THREE sequences simultaneously
(this pins the operator: 3 independent solutions), (2) reconstruct the rational
coefficients by CRT + rational reconstruction over several primes, (3) VERIFY the
reconstructed recurrence annihilates all three exact ladders at every offset.
```

Key design points to reuse for the weight-7 primitive operator:
- **Order is fixed a priori** (3 for ζ(5)); only the polynomial degree D is searched,
  via `find_min_degree(seqs, nlo, nhi, p, Dmax=14)` scanning D = 3…14.
- **Fits all three ladders simultaneously** (`run("normalized (Q,P,P̂)", ["Q","P","Ph"], 6, 40)`)
  — this is exactly the trick to *pin* a single operator when one sequence alone leaves a
  higher-dimensional nullspace. **The ζ(7) campaign never applied this to (P, I′).**
- Primes used: `[2**61-1, (1<<61)-99, 2305843009213693921, 2305843009213693967,
  2305843009213693669]` (five 61-bit primes).
- `rational_reconstruct` = Wang's algorithm with bound `sqrt(m/2)`.
- Data source: `salvage_data.py` (`triple(n)` → dict with keys `q,p,pt,Q,P,Ph`;
  `get_all(0, nhi+4)`); cache in `salvage_cache.pkl`. Also
  `worthiness/salvage_v6_desing.py`, `salvage_v7.py`, `salvage_v8_barnes.py`,
  `salvage_v3_lucas_proof.py`, `salvage_v123.py`; verification report
  `worthiness/PHASE2_SALVAGE_VERIFY.md`.
- Fit window used: n = 6…40 (avoids the degenerate head).

### 5.5 Per-term computational cost of extending q_n  ★ THE FAST PATHS

**Fast EXACT path: `worthiness/zeta7_lc_exact_dp.py`** (rep `lc`), pure stdlib.
Measured (`ZETA7_CT_COUPLING_REPORT.md` §6):

| n | 25 | 30 | 35 | 40 | 45 |
|---|---|---|---|---|---|
| time | 1.7 s | 4.1 s | 8.4 s | 16 s | 27 s |

> Growth ≈ ×1.7–2 per +5 in n.

Observed tail (`_zeta7_state_backup/gen_par.log`): n=80 → 133 s, n=85 → 186 s,
n=87 → 206 s. `gen62.log`: cumulative to n=70 in ~11 min from cold.

**Fast MODULAR path: `worthiness/zeta7_lc_modular_dp.py`** (rep `lc`, p ≈ 2·10⁹),
described in-file as *"within-window incremental token distribution (n^2 per window, not
n^4)"*. Measured (`_zeta7_state_backup/fleet_2000000033.err`):

| n | 60 | 65 | 70 | 73 | 77 |
|---|---|---|---|---|---|
| time | 39.6 s | 63.3 s | 110 s | 145 s | 202 s |

High-n (`seq_ext.log`, one term at a time, memory-gated): n=93 → 4.5 min,
n=98 → 8.4 min, n=104 → 9.4 min, at **10–11.5 GB RSS** on a 15 GB box.
`orchestrator.py` estimates **5.6 GB per high-n job** and gates launches on free RAM.

**Scaling summary [INFERRED from the two tables]:** wall time ≈ ×1.7–2.0 per +5 in n
in the mid range, flattening to roughly ×1.1–1.2 per +1 above n≈90 where memory
paging dominates. **RAM is the binding constraint above n≈95** (5–6 GB/term).

**`zeta7_mos_qn2.py` is NOT the fast path** — it uses the MOS windows including the
full-width `{1..8}` coupler; *"n=30 alone is hours"* (`ZETA7_BARNES.md` §8). Use it only
as ground truth / cross-check.

Parallelism: term generation is **embarrassingly parallel** (each q_n independent). The
campaign used this box + `tiamat` (SSH) + an Oracle box; modular runs give a second
orthogonal axis (one prime per worker).

---

## 6. ASYMPTOTICS / RESIDUE WORK — the numbers

### 6.1 Growth rates from the characteristic polynomial

```
    χ(λ) = λ⁴ − 6340λ³ + 67974λ² − 6340λ + 1
    roots:  6329.2605  ·  10.6454  ·  0.0939374  ·  0.000157996
    SECTOR A = {6329.2605, 0.000157996}      SECTOR B = {10.6454, 0.0939374}
    log λ_max = 8.752938686…      (λ_min = 1/λ_max = 1.58e-4)
```

- **Independent cross-check** (verbatim, §10.2b): *"The exact ratios q_{n+1}/q_n climb
  5648 (n=30) → 6032 (n=72); fitting q_n ~ λ_max^n · n^α gives α ≈ −3.2 and λ_max ≈
  6.31×10³, matching the char-poly λ_max = 6329."*
- **Superseded estimate:** an earlier ratio-only Aitken extrapolation on 24 terms gave
  λ_max ≈ 5.8×10³ (log ≈ 8.67). **Do not use it** — the slow ratio approach is the `n^α`
  prefactor, not a nearby root.
- **Threshold arithmetic** (Sol, verbatim):
  `exp(7)·(1/6329.260515) = 0.1733… < 1`, margin `8.752938686… − 7 = 1.752938686…`;
  whereas `exp(7)·0.093937379 ≫ 1`.

### 6.2 The convergence-rate / precision-wall measurements

Two independent measurements of the all-positive-series truncation error
`err(N) ~ C·N^{−p}`:

| n | `zeta7_barnes_num_accel.py` (§5f) | `zeta7_residue_scaling.py` (`ZETA7_RESIDUE_I3.md` §2) | projected N for 1e-100 |
|---|---|---|---|
| 0 | — | p = 0.655 | ~1e154 |
| 1 | p ≈ 1.16 | p = 1.211 | ~1e80 |
| 2 | p ≈ 1.56 | p = 1.654 | ~1e56 |
| 3 | — | ~2.0 (extrapolated) | ≳1e40 (terms ~N⁴) |

- Wynn's ε-algorithm on 45 partial sums (n=1) improves error only 2.2e-6 → 7e-8,
  **~1.5 digits gained**. Acceleration fails: multi-scale corner singularity.
- Reducing the least-coupled index `a` to a closed 1-D Euler sum
  (`zeta7_residue_n0.py`, `A(b,M)=Σ_{u≥b+1} H_u/(u²(u+M))`) leaves a 3-fold sum that
  **still** converges like N^{−0.65} at n=0.
- Per-tuple residue cost: box-[0,N]⁴ residue-sum costs **~N⁵ exact-rational operations**
  (G2 has a+b+1 terms, H2 has b+c+1 terms).

### 6.3 The rigorous upper bound machinery (`zeta7_p3_upperbound.py`)

Fully separable majorant `M(a,b,c,d) = C₀·f_a f_b f_c f_d ≥ T(a,b,c,d)`, every factor
bound a **proved** inequality (Cauchy–Schwarz log-convexity for G2; monotonicity for H2;
AM–GM for the Betas), 1696-point check with 0 violations, min ratio 137. Result:

```
    RIGOROUS UPPER BOUND:   I₃  ≤  3.0903e-9.
```

The bound is ~55 000× the claimed value — enough to close the snap window
(3.09e-9 < 1.49e-7), not enough to prove I₃.

### 6.4 The sector measurement (`zeta7_residue_sector.py`, `zeta7_sector_measurement.py`)

I″ ratios propagated at 240–300 digits climb monotonically
`0.0042, 0.0181, 0.0306, 0.0475, 0.0665, 0.0745, 0.0789, 0.0817, 0.0833 (n=29) →
0.0939374`. Forward propagation is λ_max-unstable; **≥240 guard digits required**.

I ratios: `9e-6, 3.3e-5, 5.4e-5` climbing toward 1.58e-4 (sector A).
I′ ratios: `0.0034, 0.0180, 0.0306` at n=1,2,3 — matching the I″ ratios exactly.

Archimedean elimination cost measured: `0.0939/1.58e-4 ≈ 594` — *"the archimedean mirror
of the Betti lattice cost"* (`ZETA7_P3_SNAP.md`).

---

## 7. THE ELIMINATION-COST TEST (README item 9: "awaits den(P₃)")

### 7.1 What the test is

The repo's central conjecture (`README.md` items 3–5, `worthiness/CONJECTURE.md`,
`PROOF_MECHANISM.md`) is that **ζ(2)-elimination costs a bounded {2,3}-supported
denominator factor**, measured as exactly `12 = 2²·3` in the BZ ζ(5) / M₀,₈ family, and
mechanistically identified as `24/2` where 24 is the Bernoulli lattice constant of
`ζ(2) = −(2πi)²/24` and 2 is an index-2 refinement of the integral Betti lattice.

The **weight-7 elimination-cost test** asks: does the M₀,₁₀ ζ(7)-form show the same
`{2,3}` denominator cost? Operationally: compute the smallest **extra clearing factor K**
such that `K·dₙ⁷·I′ₙ` has integer coefficients, per prime, and check whether a growing
3-part appears.

Measured on the BZ anchors (verbatim table, `ZETA7_FAMILY.md` §5):

| n | K₂ (ord₂) | K₃ (ord₃) | K at p≥5 | total K |
|---|---|---|---|---|
| 0 | +2 | 0 | 0 | 2² |
| 1 | +2 | 0 | 0 | 2² |
| 2 | 0 (slack −2) | 0 | 0 | 1 |

vs M₀,₈ where `K = 2²·3` at the binding cells, the 3-part attained at n=2.
So at n ≤ 2 the weight-7 family shows **no 3-part at all** and only a static,
non-growing `2²` sitting in the de Rham period normalization `75/4 = 3·5²/2²`.

### 7.2 Why n = 3, and what computing it requires

Verbatim (`ZETA7_FAMILY.md` §4, labelled SPECULATION there):

> n = 3 is the smallest n where dₙ = 6 itself acquires a factor 3, so both the "intrinsic
> Bernoulli 3" and the "dₙ-driven 3" first have a place to live simultaneously. The single
> most informative next datum is therefore the exact I′₃.

Computing the test requires exactly one thing: **den(P₃) as a proved exact rational**,
then factoring it and comparing `ord_p den(P₃)` with `ord_p d₃⁷ = ord_p 6⁷`
(the ledger code already exists: `zeta7_p3_endgame.py`, function `ledger(name,val,power)`,
called as `ledger("P", P3, 7)`, `ledger("Phat", Ph3, 7)`, `ledger("s", s3, 5)`).

And **P₃ = (75/4)q₃ζ₇ − 3s₃ζ₅ − I′₃**, so it requires exact `I′₃` (or the primitive
weight-7 operator L̃ that I′ satisfies). q₃ is exact; s₃ is exact-conditional.

Current state (verbatim, `ZETA7_RESIDUE_I3.md` §4):

> at the first 3-adic opportunity (n=3, where d₃=6 first carries a 3) the weight-7
> constant P₃ shows **ord₃ = 7 = tight, no excess and no 12-fingerprint** … **No growing
> Betti cost appears.** (This is the conditional reading; an unconditional statement
> needs the exact residue or a proven denominator bound.)

Also determined (unconditional on the snap, given the ladder): `den(P̂₃) = 2²·3⁵` is
*slack* against `d₃⁵ = 2⁵·3⁵` (excess −3 at 2, 0 at 3); `den(s₃) = 3` deeply slack.

**Verdict: the test is [PARTIAL — conditionally answered NEGATIVE].** `TABLE.md` ROW 5
carries the tag `[PARTIAL — awaiting n=3 unlock]`.

### 7.3 Relation to γ₅,₇ — the pair-worthiness setup  [PARTLY INFERRED]

The repo's γ machinery is `worthiness/gamma.py`, written for the **ζ(5)** family.
Docstring verbatim:

```
    gamma(a) = (C1 - C0) / (C1 + C2)
...
  * C0 = lim log|Q_n zeta(5) - P_n| / n = log|lambda_2|,
    C1 = lim log Q_n / n = log|lambda_3|,
    where lambda_1,2,3 are the three saddle-point values attached to the
    cubic factor of the resultant F(x) = Res_y(F1, F2) (Section 4).
  * C2 = (m1+...+m5) - lim log Phi_n / n, where m1>=...>=m5 are the five
    largest entries of the 28-element multiset h(a), and Phi_n is the
    arithmetic (prime factorial) gain from the group G ~ S7 acting on the
    symmetric parameters s1..s7 (Sections 8-10).
```

`gamma(a) > 1 ⇒ ζ(5) irrational`. Record `γ = 0.86597135…` at
`a = (8,16,10,15,12,16,18,13)`; symmetric point `a = (1,…,1)` gives
`C0 = −2.47237372, γ = 0.77795976` (all reproduced to 8 decimals).

**The weight-7 pair analogue is NOT implemented anywhere in the repo.** [MISSING]
What the campaign *did* state, in Sol's language (`ZETA5_ZETA7_IRRATIONALITY_PROSPECTS_FROM_SOL.txt`,
verbatim), is the equivalent inequality form:

```
(A) Denominator clearing:  D_n I'_n belongs to  Z zeta(7) + Z zeta(5) + Z,
    with D_n^(1/n) -> exp(7)  ... A typical expected form would be
    C d_n^7 I'_n belongs to Z zeta(7) + Z zeta(5) + Z
(B) Nonvanishing and sufficient decay:  0 < |I'_n| for infinitely many n, and
    limsup |I'_n|^(1/n) = rho  with  exp(7) rho < 1.
...
In general, if  D_n^(1/n) -> exp(kappa),  the true condition is  kappa < -log(rho).
```

[INFERRED] mapping to the γ formula: for the pair (ζ5, ζ7) with no coefficient-growth
normalization, `γ₅,₇ > 1 ⇔ −log ρ > κ`, i.e. `C₀ = log ρ` (the primitive linear-form
decay rate, from the characteristic roots of the **primitive** operator L̃) and
`C₂ = κ` (the denominator law exponent, `κ = 7` for the naive `d_n⁷` law, reducible by
Rhin–Viola group gains). With `C₁ = lim log q_n/n = log λ_max = 8.752938686` on the
coefficient side if one uses the full `(C1−C0)/(C1+C2)` shape.

**Numbers already in hand for γ₅,₇:**
- `C₁ = log λ_max = 8.752938686…` (rigorous given L; from the certified char poly).
- `C₀` candidates: `log(0.000157996) = −8.752938686…` (sector A) or
  `log(0.093937379) = −2.36505…` (sector B). **Sector B is the campaign's verdict.**
- `C₂ = 7` naive (`d_n⁷`); required for a pass at sector B: `κ < 2.365…`.
- Threshold: `e⁻⁷ = 9.1188e-4`; sector A passes with margin `e^{1.7529}`; sector B fails
  by two orders.

---

## 8. NEXT STEPS AS THE CAMPAIGN SAW THEM  (verbatim to-do lists)

### 8.1 Sol's "RECOMMENDED NEXT STEPS" — `ZETA5_ZETA7_IRRATIONALITY_PROSPECTS_FROM_SOL.txt` §8

```
1. Finish the creative-telescoping certificate for the discovered q_n
   recurrence.  This secures the descended rank-four structure as a theorem.

2. Compute exact I'_3 by the primal integral, residue decomposition, or the
   primitive holonomic route.  This is the immediate threshold diagnostic.

3. Search directly for the primitive operator annihilating P_n and I'_n rather
   than assuming that the descended operator transfers.

4. Prove or sharply formulate the d_n^7 denominator theorem for the primitive
   form.

5. If the symmetric primitive rate misses exp(-7), optimize asymmetric
   parameter orbits using the full transformation group and compare the
   denominator exponent kappa with the primitive decay exponent.
```

### 8.2 Sol's "Immediate priorities" — `ZETA7_IMPLICATIONS_FROM_SOL.txt`

```
  1. Finish the low-coupling creative-telescoping certificate.
  2. Test factorization and adjoint symmetry over Q(sqrt(3))(n).
  3. Construct the primitive weight-7 operator annihilating P_n and I'_n.
  4. Use it to determine the true P_3 and its denominator.
```

### 8.3 Sol's longer research-direction list — `ZETA7_IMPLICATIONS_FROM_SOL.txt` §7

```
  1. Derive the differential equation for the generating function of q_n and
     study its singularities, monodromy, and possible modular parametrization.

  2. Test whether the rank-four operator decomposes, becomes self-adjoint, or
     is a symmetric/tensor construction after extension to Q(sqrt(3)).

  3. Construct the second recurrence governing the primitive weight-7 form
     I'_n and the rational coefficient P_n.

  4. Compute the true P_3 and obtain the first decisive weight-7 denominator
     ledger at the prime 3.

  5. Compare the two reciprocal quadratic sectors with the motivic weight
     filtration and the weight-7 to weight-5 residue map.

  6. Generalize the low-coupling method to M_{0,12} and a possible zeta(9)
     system, testing whether the order progression continues.
```

### 8.4 The residue agent's "Finish plan for exact P₃" — `ZETA7_RESIDUE_I3.md` §6

```
Two exact routes, both outside a single low-RAM session:
1. **Symbolic left-closure MZV reduction** of the n=0 harmonic 4-fold sum (§1a) and its
   n=3 ₂F₁-blocked analogue → coefficients of {ζ₇,ζ₅ζ₂} and the rational P₃. Needs a
   weight-7 nested-sums/MZV engine (HyperInt-class). Estimate: multi-day; the n=0 closed
   form removes the first obstacle (the blocks were the unknown).
2. **The parallel Barnes-CT run** proving L and, if it yields the weight-7 operator L̃
   (order possibly >4), propagating P₃ — the go/no-go the coordinator flagged. The sector
   verdict above does not wait on it.
```

### 8.5 The Barnes doc's handoff — `ZETA7_BARNES.md` §9

```
**HANDOFF STATE — one live license away from the prize.** With a working kernel,
the path is: run `zeta7_mos_hf_test_apery3.wl` (must return the known order-2 Apéry
ζ(3) recurrence in seconds — final pipeline check), then
`zeta7_mos_holonomic_diag.wl` for the 8-fold recurrence; certify it against the 31
exact q_n; extract the characteristic polynomial (asymptotic rates); then run
`zeta7_mos_recurrence.sage`'s P₃-propagation test (P₀=0, P₁=220, P₂=6021219/32) for
the exact P₃, den(P₃) factored, and the per-prime ledger vs d₃=6 — the first 3-adic
elimination-cost test at weight 7.
```
*(Superseded: the recurrence was found by guessing instead, and the P₃ propagation was
run — see §3.4 — and showed P does **not** satisfy L.)*

### 8.6 Sol's falsification predictions (still live) — `ZETA7_DWORK_FROM_SOL.txt` P7

```
P7. Primitive datum.  Agent B should first reproduce n=0,1,2 exactly, including
all signs in (20).  For n=3, the current falsifiable prediction is

      I_3  = 5.6299224184893...e-14,
      P_3  = 23478462179525/69984,
      I'_3 approximately 3.56748e-5,

and hence sector B for I'.  Any exact residue result differing from that
rational P_3, after normalization is reconciled, falsifies the snap and should
raise the sector-A odds sharply.
```

### 8.7 Sol's honest probability assessment — verbatim

```
    roughly a 10--20 percent chance that this exact totally symmetric family
    proves that zeta(5) or zeta(7) is irrational.
...
  * completing an all-n certificate for the discovered q_n recurrence:
      approximately 85--95 percent;
  * obtaining the true P_3 and additional primitive data:
      approximately 60--75 percent;
  * finding the primitive recurrence for P_n and I'_n:
      approximately 40--60 percent;
  * proving a sharp d_n^7-type denominator theorem:
      approximately 30--50 percent;
  * discovering that the primitive decay is strong enough to beat exp(-7):
      approximately 10--25 percent on present evidence.
```

---

## 9. GOTCHAS — conventions that bit the campaign

**G1. The "1.10e-9" vs "1.05312589331e-9" for I₂.** A loose quote of I₂ propagated
through early campaign notes. The exact filtration chain gives
`I₂ = 1.05312589331082e-9`; the all-positive series confirms it (partial sums reach
1.047839e-9 at N=160 and extrapolate to 1.05386e-9, **never approaching 1.10e-9**).
`ZETA7_P3_VERIFICATION.md` §1 settles it. **Use 1.0531e-9.**

**G2. λ_max ≈ 5.8×10³ is WRONG.** An early Aitken extrapolation of q_{n+1}/q_n on 24
terms. The true value from the certified char poly is **6329.2605**; the ratios approach
it slowly because of the `n^α` prefactor with α ≈ −3.2. Do not use 5.8e3 or log ≈ 8.67.
**Use λ_max = 6329.260515, log λ_max = 8.752938686.**

**G3. "Order ≈4, degree 11–13" is WRONG.** The real answer is **order 4, degree 19**.
A degree underestimate cost the campaign a whole round of failed guessing at 93 terms.
The rule of thumb that worked: `(order+1)(degree+1) = 100` unknowns ⇒ need ≳105 terms.

**G4. The naive-propagated "P₃" with denominator 2⁵·3⁸·107 is a FALSE VALUE.**
It comes from pushing P through L, which P does **not** satisfy. The spurious prime 107
is the tell. The (conditional) correct value is `23478462179525/69984 = 2⁵·3⁷`.

**G5. Do not assume L governs the primitive ladder.** L governs `q, s, P̂, I″` (the
weight-5 descent). It does **not** govern `P` or `I′`. Propagating I′ through L gives
`I′₃ = 43.71` (λ_max mode uncancelled) instead of ~3.57e-5. Sol's warning, verbatim:
*"A telescoper for I is first a theorem about I. It becomes a theorem about the primitive
ladder only after formal coefficient separation, independent ladder certificates, or
certified Ore-module extraction. Order four and rapid decay alone do not cross that
logical gap."*

**G6. The sector-split conjecture is FALSIFIED for the projections.** Early hope: the
primitive form rides sector A (1.58e-4, the passing rate). Verbatim
(`ZETA7_P3_SNAP.md`): *"The filtration (I ≈ 0) LOCKS I′ ≈ −ζ₂I″: **both projections ride
sector B (0.0939)**. The symmetric family CANNOT beat the e⁻⁷ threshold; the sector-split
conjecture (primitive = sector A) is FALSIFIED for the projections — sector A is ridden
by the full 5-word form only."*
Caveat: this is a *robust argument* (§3.5), not a theorem — it depends on L genuinely
governing I″.

**G7. Forward propagation through L is numerically unstable.** λ_max-dominated. Use
**≥240 guard digits** (the scripts use `mp.dps = 300`) to keep the decaying sector-B mode
clean to n ≈ 29.

**G8. MOS windows ≠ low-coupling windows.** `zeta7_ct.wl` (predecessor) silently used the
MOS full-coupler windows (containing `x1+…+x8`), which is exactly the set that blows up
on elimination #2. Verbatim: *"The genuine **low-coupling W_lc CT** (`zeta7_ct_lc.wl`)
had never been run."* Always check which window set a script hardcodes.

**G9. `W_r2` has two published variants.** Line 1 of
`zeta7_lowcoupling_representations.txt` is `{1,2},{1,2,3},{2,3,4},{2,3,4,5},{3,4,5,6},
{3,4,5,6,7},{5,6,7,8},{7,8}`; the scripts use line 3's
`{1,2},{1,2,3},{2,3,4},{2,3,4,5,6},{3,4,5,6,7},{5,6,7},{6,7,8},{7,8}`. **Trust the
scripts** (`zeta7_lc_exact_dp.py`, `zeta7_lc_modular_dp.py`) — those were validated.

**G10. Mathematica / HolonomicFunctions environment traps** (`ZETA7_CT_COUPLING_REPORT.md`
§1), all four hit in one session:
  1. The MCP `WolframLanguageEvaluator` (WSTP transport) **crashes** loading
     `HolonomicFunctions.m` — its anti-tamper layer trips. Use a plain
     `wolfram -noprompt` **stdin** kernel.
  2. `$VersionNumber` is Locked — cannot be `Block`-spoofed.
  3. **License-seat exhaustion**: stray kernels cause spurious "No valid password found".
     Keep exactly one compute kernel alive.
  4. A **stale 404-HTML stub** named `HolonomicFunctions.m` in the working dir shadowed
     the real package via `.` on `$Path`. **Always `Get` by absolute path**:
     `Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"]`.
  Also: monolithic `Takayama` never finishes (>22 min on the 4-variable Apéry case);
  **iterated `CreativeTelescoping`, one variable at a time, is the method** (Apéry in 2 s).
  The `math` symlink segfaults — use `wolfram -noprompt` via stdin.

**G11. Elimination order matters.** For the diagonal CT the campaign used
`x1, x8, x2, x6, x3, x7, x4, x5` — *"low-incidence boundary first, hot center last"*
(x4, x5 are in 5 windows each).

**G12. The 2² in the ζ(7) form is de Rham, not a Betti cost.** It sits in the period
normalization `I′₀ = (75/4)ζ(7)`, `75/4 = 3·5²/2²`, present already at n=0 — a *period
feature, not an n-growth elimination cost*. Do not read it as the `12 = 2²·3` fingerprint.

**G13. `README.md` item 8 is stale.** It says *"q₀…q₃₀ archived (extension to ~90 terms
and the recurrence campaign in progress)"*. Actual state: 74 exact + 105 modular terms,
recurrence resolved and certified. `TABLE.md` ROW 5 is also tagged
`[PARTIAL — awaiting n=3 unlock]` and pre-dates §10.

**G14. Direct MC / quadrature of the primal integral is useless.** Corner singularity
1/P: plain Monte-Carlo on the cube form gives `15 ± 12` (and 3.99 vs 3.555 in another
run); the J-form MC gives `3.86 ± 0.27` with finite variance. **The exact symbolic
identity is the gate, not the numerics.**

**G15. Recovered-from-crash coefficients.** The `_zeta7_state_backup/` directory is the
salvaged state of a crashed session; `worthiness/zeta7_q_recurrence.json` and
`_zeta7_state_backup/recurrence.json` are **byte-equivalent** (I diffed them), and
`zeta7_crt_recon.py` == `_zeta7_state_backup/crt_recon.py`, `zeta7_p3_endgame.py` ==
`endgame.py`, `zeta7_recurrence_guess.py` == `guess2.py`. So nothing is garbled — but
`zeta7_p3_endgame.py` loads `recurrence.json` **relative to its own directory**, so it
must be run from `_zeta7_state_backup/` or have the path fixed.

---

## 10. FILE INDEX (quick reference)

### Documents (`worthiness/`)
| file | size | what |
|---|---|---|
| `ZETA7_BARNES.md` | 59 k | **the main record** — Stages 1–3, obstruction §5, dihedral scan §5b, numeric wall §5f, CT campaign §5g, Mathematica §7, MOS side door §8, HF endgame §9, **the recurrence §10** |
| `ZETA7_FAMILY.md` | 15 k | extraction from BZ, ladder skeleton, feasibility routes (a)–(d), the n≤2 denominator audit |
| `ZETA7_DUAL.md` | 14 k | the VWP series route and its **exclusion** (sign dichotomy) |
| `ZETA7_SERIES_NOTES.md` | 3 k | short summary of the above |
| `ZETA7_CT_COUPLING_REPORT.md` | 10 k | **the CT obstruction + the 41 reps + Plan A** |
| `ZETA7_CT_CERTIFICATE.md` | 5 k | the CT certificate attempt; elimination towers (never finished) |
| `ZETA7_P3_SNAP.md` | 5 k | the P₃ denominator snap |
| `ZETA7_P3_VERIFICATION.md` | 8 k | independent verification of the snap |
| `ZETA7_RESIDUE_I3.md` | 13 k | residue pipeline, scaling, **the sector verdict** |
| `ZETA5_ZETA7_IRRATIONALITY_PROSPECTS_FROM_SOL.txt` | 9 k | ★ **the pair-irrationality target, thresholds, probabilities** |
| `ZETA7_IMPLICATIONS_FROM_SOL.txt` | 9 k | Sol on the recurrence's meaning; ℚ(√3) splitting |
| `ZETA7_DWORK_FROM_SOL.txt` | 26 k | Sol's Dwork memo + falsification predictions P1–P8 |
| `TABLE.md` | 14 k | 5-family comparison table; **ROW 5 = ζ(7)** |
| `CONJECTURE.md`, `PROOF_MECHANISM.md` | | the sharp-12 denominator law and its mechanism (weight-5) |

### Data
| file | what |
|---|---|
| `worthiness/zeta7_lc_terms.txt` | **74 exact q_n, n=0…73** |
| `worthiness/zeta7_mos_qn_values.txt` | 31 exact q_n (MOS ground truth) |
| `worthiness/zeta7_q_recurrence.json` | **the certified order-4 degree-19 operator** |
| `worthiness/_zeta7_state_backup/fleet_*.txt` | modular q_n, up to n=104 at 3 primes |
| `worthiness/zeta7_ct_scripts/zeta7_lowcoupling_representations.txt` | **the 41 low-coupling reps** |
| `worthiness/zeta7_residue_ckpt/I{0,1,2,3}_shells.json` | exact per-shell partial sums (rigorous lower bounds) |
| `worthiness/falsify_data/ladder_{Q,P,Ph}.json` | **exact weight-5 (M₀,₈) ladders to n=360** |
| `worthiness/ct_run/ckpt_after_x2.mx`, `_zeta7_state_backup/zeta7_lc_cur.mx` | CT elimination checkpoints |
| `/home/ubuntu/fable-episode-2/zeta-math/zeta7_qn_certificate.nb` | Mathematica notebook (21 k) |

### Scripts by function (`worthiness/`)
- **Generate q_n:** `zeta7_lc_exact_dp.py` ★, `zeta7_lc_modular_dp.py` ★,
  `zeta7_mos_leadcoeff.py`, `zeta7_mos_qn.py`, `zeta7_mos_qn2.py`
- **Guess the recurrence:** `zeta7_recurrence_guess.py` ★, `zeta7_crt_recon.py`,
  `salvage_v6_recur.py` ★ (weight-5 template, multi-sequence fit)
- **P₃ / endgame:** `zeta7_p3_endgame.py`, `zeta7_mos_recurrence.sage`,
  `zeta7_p3_series.py`, `zeta7_p3_series_fast.py`, `zeta7_p3_upperbound.py`
- **Residue / asymptotics:** `zeta7_residue_pipeline.py`, `_hiprec.py`, `_n0.py`,
  `_scaling.py`, `_sector.py`, `_ckpt_gen.py`, `zeta7_sector_measurement.py`
- **Barnes / J-form:** `zeta7_barnes_stage{1,2,3}.py`, `_jform.py`, `_jform_mc.py`,
  `_refl.py`, `_group.py`, `_orient_scan.py`, `_merge.py`, `_series_n0.py`,
  `_num1.py`, `_num_accel.py`
- **VWP series exclusion:** `zeta7_dual_*.py` (16 scripts)
- **Creative telescoping (WL):** `zeta7_ct_lc.wl`, `zeta7_ct_lc_resume.wl`,
  `zeta7_mos_holonomic_diag.wl`, `zeta7_mos_hf_test_apery3.wl`,
  `ct_run/barnes_ct.wl`, `ct_run/barnes_ct_long.wl`, `ct_run/resume.wl`,
  `zeta7_ct_certify.py`, `ct_run/compare_op.py`
- **γ / worthiness (weight-5):** `gamma.py` ★, `search.py`, `audit.py`, `fast_eval.py`

---

## 11. WHAT IS MISSING / NEVER DONE  (say this out loud, don't guess)

1. **No CT certificate.** Neither the diagonal route (stopped at elim #4 of 8) nor the
   Barnes route (never finished elim #1) completed. The order-4/degree-19 operator is
   *empirically certified on 74 terms*, not proved.
2. **No primitive weight-7 operator L̃** annihilating P_n / I′_n. Never searched for
   directly — and `salvage_v6_recur.py`'s multi-sequence simultaneous-fit trick was
   **never applied** to (P, I′). This is the biggest untried idea in the repo.
3. **No exact P₃.** Only the conditional snap.
4. **No P_n, s_n, P̂_n data beyond n = 3** for the weight-7 family.
5. **No γ₅,₇ implementation.** `gamma.py` is weight-5-only; the weight-7 pair analogue
   (C₀, C₂ for the mixed form) does not exist in code.
6. **No `search_z7_windows.py`** — the script that found the 41 reps is gone; only its
   output survives.
7. **q_n beyond n = 104** — `seq_ext.log` shows n=105 started, never recorded.
8. **The ℚ(√3) factorization of the full Ore operator** — only the char poly was
   factored; the operator itself was never tested for factorization/adjoint symmetry.
