# P1e-refold — can `Σ T·ŵ₃` be re-folded to ≤ 4 harmonic symbols?

**Task:** P1e-refold (pure algebra; no standalone Wolfram kernel used, no MCP kernel used).
**Date:** 2026-07-25. **Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`,
artefacts in `work/refold/`.
**Brief:** `PHASE2_CERTS.md` §18.17 ("the refold target, stated exactly"), §18.13
(route 1 = re-fold, route 2 = telescope whole), §5.1/§5.2, §18.2/§18.14 (the letter-count
law), `PHASE2_CANCEL.md` §3 (Lemma Φ₂), `PHASE2_ENDGAME.md` §R1.2 (Lemma Phi).

---

## VERDICT

| question | answer |
|---|---|
| **≤ 4 distinct symbols in the summand?** | **NO — `[EXCLUDED]`.** Not with constant coefficients (min = 9), and not with polynomial coefficients in `(n,k,l)` either: **0 of 171** admissible ≤ 4-symbol letter sets is consistent — four independent sweeps (`dp ≤ 3`, letter degree `≤ 4`, two primes), 150–270 excess equations each. A further **64** of the 235 ≤ 4-symbol sets are killed outright, for *any* `p`-integral coefficients and *any* degree, by a `p`-adic pole argument. A matched control shows degree-2 polynomial coefficients do not lower the minimum by even one symbol. |
| **≤ 4 symbols in `E(w)` (the object §13–§18 actually telescope)?** | **NO — `[EXCLUDED]`.** Minimum = **7** with constant coefficients; **0 of all 235** ≤ 4-symbol letter sets is consistent with polynomial coefficients either. |
| **Is anything gained at all?** | **YES.** A refold `ṽ` exists with **`S = 10` (was 12) and `E = 7` (was 9)**, it is `[VERIFIED exact over ℚ, n = 0…33, 36, 40]`, and — the part the symbol count does not show — **it contains no `C` letter at all**, so the letter module of `T·ṽ` factorises as `M_k ⊗ M_l` with `M_l` of rank 2. `ŵ₃ − ṽ` lies in the **PROVED** kernel (Lemma-Phi species + `k↔l` folding), so certifying `ṽ` certifies **Theorem B itself**, not a cousin of it. |

**Consequence for the Theorem-B certificate route.** §18.13's route 1 (“re-fold to ≤ 4
letters, then telescope whole in the `(3,9)` box”) **cannot be executed as stated**: the
re-folding it needs does not exist. Route 2's blocking step — `Annihilator` of the
undecomposed object — goes from 9 symbols to 7, which by §18.17's own calibration
(9 → OOM at 7.8 GB; 3 → 69 s end-to-end; 0 → 34 s) is an improvement of unknown but
probably insufficient size. What is *new* and not measured by the symbol count is the
`C`-elimination (§4 below), which removes the only letter that moves under **both** `S_k`
and `S_l`. That is the one thing worth a kernel seat here.

---

## 1. The instrument, and its validation

`work/refold/w3full.py` rebuilds the weight-3 fitting system on top of `work/lb5/fit.py`
(the module that produced every earlier fit — `Basis`, `alphabet`, `lad_ext`, `rref`),
with `W = 3`, `maxr = 3` and target ladder `Ph` = `P̂`.

**The space is the *unsymmetrised* (= folded) one**, which is the right space and had not
been used before. Basis monomial

```
    f(k) · g(l) · c(k+l) · s(n) ,    total weight 3,
    f,g ∈ monomials in A_r(x)=H^(r)_{n+x}−H^(r)_x , B_r(x)=H^(r)_{n−x}−H^(r)_x   (r ≤ 3)
    c   ∈ monomials in C_r = H^(r)_{n+k+l}−H^(r)_{k+l}          (r ≤ 3)
    s   ∈ monomials in N_r = H^(r)_n                            (r ≤ 3)
```

**98 columns.** Because `T` is `k↔l` symmetric, `V(w) = V(w^sym)`, so this space has the
same image as the symmetric one but a strictly larger fibre over `P̂` — that extra freedom
is exactly what folding exploits.

```
basis: 98 columns  (k-monomials 18, c-monomials 7, n-monomials 7)
VALIDATION  v (folded)           residual nonzeros = 0 / 240
VALIDATION  w3hat (symmetric)    residual nonzeros = 0 / 240
rank(M) = 35,  nullity = 63,  consistent = True
```

Both known representatives reproduce `P̂_n` at every `n = 1…240` mod `q = 33554393`
(`run1.py`). `rank(V) = 35`, so **`dim ker V = 63`** on this space.

**Symbol counting matches `certP.wl`'s.** A *symbol* is a distinct pair
`(argument, r)` of `HarmonicNumber`; `A_r(k) → {H^(r)_{n+k}, H^(r)_k}`,
`B_r(k) → {H^(r)_{n−k}, H^(r)_k}` (sharing `H^(r)_k`), `C_r → {H^(r)_{n+k+l}, H^(r)_{k+l}}`,
`N_r → {H^(r)_n}`. The harness reports **12** for `v` and **9** for its degree-≥2 part,
reproducing §18.17's measured `12` and `9` exactly, and the nine are the same nine.

> **Why the degree-≥2 part is the right proxy for `E(w)`.** `E(w) = Σ_τ G_τ(τ.w − w)`. For a
> term `c·m` with `m` a single letter and `c` **constant**, `τ.(cm) − cm = c(τ.m − m)` is
> **rational**, so it contributes nothing to `E`'s letter content; for a product,
> `τ.(m₁m₂) − m₁m₂ = m₁δ₂ + m₂δ₁ + δ₁δ₂` with `δ_i` rational, so both letters survive.
> Hence, **for constant coefficients**, `symbols(E(w)) = symbols(degree-≥2 part of w)`.
> Checked against §18.17: `v`'s degree-≥2 part is `−½A₂(k)Ψ`, giving exactly the nine.
>
> ⚠ **The exemption is destroyed by a non-constant coefficient**:
> `τ.(cm) − cm = (τ.c − c)m + (τ.c)(τ.m − m)`, so a degree-1 term with a polynomial
> coefficient *does* put its letter into `E`. Stage 3's `MODE=E` sweep charges for exactly
> this — only the six weight-3 single letters with **constant** coefficient, and the purely
> rational part, are free.

---

## 2. The exhaustive minimum — `[PROVED within the stated space]`

The search is exhaustive, not heuristic. A symbol set `Σ` determines the admissible
columns (those whose letters' symbols all lie in `Σ`); `b ∈ colspace(M_Σ)` is a rank test.
`[M|b]` is first row-compressed to its 35-row RREF — **lossless**, because
`rank(M_{:,S}) = dim π_S(rowspace M)` for every column subset `S`. All 13508 closed symbol
masks with ≤ 9 symbols are enumerated by BFS over letter unions.

```
=== S  whole summand ===                      === E  degree>=2 only ===
  symbols = 0…8 :      0 consistent             symbols = 0…6 :      0 consistent
  symbols = 9   :      2 consistent             symbols = 7   :      4 consistent
```

> **`[EXCLUDED]`** No representative of `Σ T ŵ₃` in this space carries ≤ 8 distinct
> symbols. **Minimum = 9.** No representative has ≤ 6 symbols in its degree-≥2 part.
> **Minimum = 7.**

The two 9-symbol optima are `k↔l` mirrors of one another; the letters are
`{A₁(k), A₂(k), B₁(k), A₁(l), B₁(l), N₃}` — **and no `C` letter**.

**Pareto frontier** (`run4.py`), min `S` for each achievable `E`:

| `E` | min `S` | comment |
|---|---|---|
| 7 | 10 | the `E`-optimum |
| 8 | 9 | the `S`-optimum |
| 9 | 9 | `v` sits at `(S,E) = (12,9)` — dominated in both coordinates |

Exact-ℚ construction and **held-out** validation of both (`run5.py`, `exact.py`): the
design matrix is rebuilt over ℚ from `core.T`/`core.Hs`, fitted on `n = 1…25` and checked
on `n = 26, 28, 30, 33, 36, 40` — **ALL PASS** for both.

---

## 3. Polynomial coefficients do not rescue ≤ 4 — `[EXCLUDED]`

The stage-1/2 space is weight-3-homogeneous with **constant** coefficients. That is a real
restriction: a certificate-side representative may carry coefficients that are rational
functions of `(n,k,l)`, and such coefficients cost **nothing** in symbols. `polyfit.py`
drops both restrictions:

```
    Phat_n = Σ_{k,l} T · Σ_{μ, a+b+c ≤ dp}  λ_{μ,abc} · n^a k^b l^c · μ(n,k,l)
    μ = letter monomial of letter-degree ≤ Dm in the letters allowed by the symbol mask
```

**Two filters, then the fit.**

*(i) The `p`-adic pole test — coefficient-free and degree-free.* `vp_phat.py`:
`min_{n<p} v_p(P̂_n) = −1` for **every** prime `5 ≤ p ≤ 59`. The pole calculus of
`PHASE2_FINAL` (`A_r` has pole order `r` iff `α`; `C_r` iff `κ`; `B_r`, `N_r` never;
`v_pT = α+γ+κ`) gives, for any `p`-integral coefficients,
`v_p(Σ T w) ≥ min_π ( v_pT(π) − D_L(π) )` over the six reachable `(α,γ,κ)` triples
`(0,0,0) (0,0,1) (1,0,1) (0,1,1) (1,1,0) (1,1,1)` — `(1,0,0)` and `(0,1,0)` are
impossible — with `D_L(π)` the maximum pole weight a monomial of `L` can carry at `π`.
**64 of the 235** ≤ 4-symbol letter sets cannot reach `−1` and are excluded outright — in
particular every set built only from `B` and `N` letters, which are `p`-integral, so a
pole-free alphabet can never produce `P̂`.

*(ii) The fit, on the surviving 171.* A hard guard rejects any system with fewer than 100
excess equations (a system with `rank = #rows` is trivially "consistent" — this bit once
during instrument shakedown and is now impossible to miss).

| sweep | `dp` | `Dm` | `q` | result |
|---|---|---|---|---|
| `s3_S4_D2` | 2 | 3 | 33554393 | **0 / 171 consistent**, 0 undetermined |
| `s3_S4_D2_q2` | 2 | 3 | 33554467 | **0 / 171 consistent**, 0 undetermined |
| `s3_S4_D2_M4` | 2 | **4** | 33554393 | **0 / 171 consistent**, 0 undetermined |
| `s3_S4_D3` | **3** | 3 | 33554393 | **0 / 171 consistent**, 0 undetermined |
| `s3_E4_D2` (`MODE=E`) | 2 | 3 | 33554393 | **0 / 235 consistent**, 0 undetermined |

The last row is the `E`-metric version, run on **all 235** masks (the pole filter is vacuous
there because the free columns already include `A₃(k), A₃(l), C₃`). So ≤ 4 is excluded for
`E(w)` as well as for the summand, and with polynomial coefficients in both cases.

**The control that makes this conclusive — do polynomial coefficients *ever* help?**
`ctrl8.py` runs the same `dp = 2` machinery on **every proper subset** of the 9-symbol
optimum's letter set `{A₁(k), A₂(k), B₁(k), A₁(l), B₁(l), N₃}` and of the proved `E`-optimum's
`{A₁(k), A₂(k), B₁(k), A₂(l)}` — 60 letter sets at 3…8 symbols — and then on the two full
sets as positive controls. Same harness, same degree, **only the letter set varies**:

```
  A1(k),A1(l),A2(k),B1(k),B1(l)   sym=8  cols=560 rows=840  excess=458   inconsistent
  A1(k),A2(k),B1(k),B1(l),N3      sym=8  cols=560 rows=840  excess=368   inconsistent
  A1(k),A1(l),B1(k),B1(l),N3      sym=7  cols=560 rows=840  excess=544   inconsistent
  ... (all 60 subsets, 3–8 symbols, inconsistent) ...
CONTROL positive (must be CONSISTENT):
  A1(k),A1(l),A2(k),B1(k),B1(l),N3   sym= 9 cols=840 rows=1260 excess=699  CONSISTENT
  A1(k),A2(k),A2(l),A3(k),B1(k),N3   sym=10 cols=840 rows=1260 excess=508  CONSISTENT
```

> **Degree-2 polynomial coefficients do not lower the minimum by a single symbol.** The
> constant-coefficient answer (9 / 7) is the answer, and it is a fact about the *letters*,
> not about the coefficient ring.

> **`[EXCLUDED]` — the pass/fail answer is FAIL.** There is no representative of
> `Σ_{k,l} T·ŵ₃` carrying ≤ 4 distinct harmonic symbols, over the `{A,B,C,N}_{r≤3}`
> alphabet, with coefficients polynomial of degree ≤ 3 in `(n,k,l)` and letter degree ≤ 4.
> The obstruction is the fit identity alone — every failure is
> `rank[A|b] = rank[A] + 1`, with 150–270 excess equations.

**Caveats, stated honestly.** (a) Coefficients with *denominators* are not covered by the
fit sweep (they are covered by the `p`-adic filter only where they stay `p`-integral).
(b) A different alphabet — `R_r(k)` (Apéry), `D_r`, nested `Y/V/Z`, `H^(r)_{2n}` — is not
covered; but those letters are not `HarmonicNumber` symbols at all, so a "≤ 4 symbol"
claim in that alphabet would not be the quantity §18.17 calibrated. (c) The negative is
`[EXCLUDED]` in the sense of an exhaustive finite computation over an explicitly stated
space, not a `[PROVED]` theorem about all conceivable representatives.

---

## 4. What *is* achievable — the refold `ṽ`, and it is PROVED-reachable

### 4.1 The soundness constraint that shapes the answer

Theorem B as consumed downstream is `P̂_n = Σ T·ŵ₃`, and the downstream (Lemma G, the
Lemma-F ledger, the `d₃ ≤ 1+min(v_pT,2)` depth bound) reads `ŵ₃` **cell by cell**.
So certifying `P̂_n = Σ T·w̃` for a different `w̃` does **not** deliver Theorem B unless
`Σ T(ŵ₃ − w̃) = 0` is itself **proved** — the weight-3 transcription of §1's `w₅` caveat.

The **proved** supply of kernel elements is:

* **Lemma Phi** `Σ_k T·Φ = 0`, `Φ = A₁(k)+2B₁(k)+C₁`, for every fixed `l` (`ENDGAME` §R1.2);
* **Lemma Φ₂** `(P1),(P2),(P3)` (`CANCEL` §3) — same, at weight 2;
* both multiplied by any **`k`-free** factor, plus the `k↔l` mirrors — 36 generators;
* the **`k↔l` folding** moves `μ − mirror(μ)` (a rearrangement of a finite sum;
  `PHASE2_CERTS` §5.2 step 3, `[PROVED]`) — 84 generators, span dim 42.

`kernel_proved.py` builds all of them, confirms **every generator is genuinely in `ker V`**
(zero residual against the 240-row design matrix — an independent check of the expansion),
and measures

```
dim span(Lemma-Phi species)                     = 29
dim span(Lemma-Phi species + folding)           = 57
dim ker V                                       = 63          <- codimension 6 gap
```

`ŵ₃ − v` is in the proved span (as it must be — folding); `ŵ₃ − w₉` and `ŵ₃ − w₇` (the
stage-2 optima) are **not**. So the optimisation must be redone **inside the proved affine
set** `ŵ₃ + span(proved)`, which is what `run6.py` does.

### 4.2 The proved-affine optima

```
=== PROVED-AFFINE search ===
  S  whole summand : symbols = 0…9 : 0 reachable ;  symbols = 10 : 4 reachable
  E  degree≥2 only : symbols = 0…6 : 0 reachable ;  symbols =  7 : 2 reachable
```

The proved constraint costs **one** symbol on `S` (10 instead of 9) and **nothing** on `E`.

### 4.3 The representative

`run7.py` builds it exactly over ℚ inside the proved affine set and verifies it:

> ### `ṽ = H^(3)_n + 2A₃(k) + ½·( A₂(l) − A₂(k) )·Ψ_k` ,  `Ψ_k = A₁(k) + 3B₁(k)`

against

> `v  = H^(3)_n + 2A₃(k) − ½·A₂(k)·( Ψ_k + Ψ_l )` , `Ψ_l = (3/2)C₁ + ½A₁(l)`.

`Ψ_k` is §18.1's own `Ψ_k`, unchanged. **`Σ_{k,l} T·ṽ = P̂_n`, `[VERIFIED exact over ℚ,
n = 0…33, 36, 40, 0 discrepancies]`** (`run7.py`, exact `Fraction` arithmetic from
`core.T`/`core.Hs`, no modular step anywhere).

**The single identity that performs the refold** — `v − ṽ = −½[A₂(k)Ψ_l + A₂(l)Ψ_k]`, i.e.

> `Σ_{k,l} T·[ 3A₂(k)C₁ + A₂(k)A₁(l) + 2A₂(l)A₁(k) + 6A₂(l)B₁(k) ] = 0`
> `[VERIFIED exact, n = 0…25]`, and **in the PROVED span** (Lemma-Phi species + folding)
> — `keyid.py`. It is *not* in the Lemma-Phi species alone; the folding moves are needed.

### 4.4 Census

| object | monomials | distinct symbols `S` | `E` = symbols of degree-≥2 part | shift-closure size | `C` letters |
|---|---|---|---|---|---|
| `ŵ₃` (symmetric) | 11 | 17 | 12 | 19 (§5.2) | yes |
| `v` (§5.2 fold) | 6 | **12** | **9** | 12 (§5.2) | yes |
| **`ṽ` (this work)** | **6** | **10** | **7** | **11** | **none** |

`ṽ`'s ten symbols: `H^(3)_n`; `H^(3)_{n+k}, H^(3)_k`; `H^(2)_{n+k}, H^(2)_k`;
`H^(1)_{n+k}, H^(1)_k, H^(1)_{n−k}`; `H^(2)_{n+l}, H^(2)_l`.
`E(ṽ)`'s seven: the same minus the three `r = 3` ones.

### 4.5 The structural gain the symbol count does not show

`C₁ = H_{n+k+l} − H_{k+l}` is **the only letter in the alphabet that moves under both `S_k`
and `S_l`**. In `ṽ` it is gone, and so is `A₁(l)`. Every letter of `ṽ` is a function of
`(n,k)` alone or of `(n,l)` alone, and the `l`-side letter content is the single letter
`A₂(l)`. Hence

```
    ṽ  =  [ H^(3)_n + 2A₃(k) − ½A₂(k)Ψ_k ]      +   A₂(l) · [ ½ Ψ_k ]
           \___________ l-free ___________/          \_ rank-2 l-factor _/
```

so the letter module of `T·ṽ` is a **tensor product `M_k ⊗ M_l` with `rank M_l = 2`**
(spanned by `1` and `A₂(l)`, and `Δ_l A₂(l)` is rational). Under `S_l` only **3** of the 11
closure monomials move (`A₂(l)`, `A₂(l)A₁(k)`, `A₂(l)B₁(k)`), all by one filtration level,
against 4 of 12 for `v` — and for `v` two of those four (`C₁`, `A₂(k)C₁`) also move under
`S_k`, which is what couples the two eliminations. **`ṽ` decouples them.** This is exactly
the property §5.2 identified as "what made `T·A₁(k)` tractable", now available in both
directions at once, and it is *not* a split in §18.13's sense — the combination is kept
whole and its telescoper is still `L_BZ`.

### 4.6 `E(ṽ)` in closed form — the §4ter analogue, ready to drop into `certP.wl`

`E(w) = Σ_τ G_τ (τ.w − w)` and the weights `G_τ` depend only on `T, ρ, σ, L_BZ` — **not on
the weight `w`** — so §4bis's `[CERTIFIED]` Q-row certificate and `certP.wl`'s `tauW[]` are
reused verbatim. Write `ṽ = h₃ + 2a₃ + ½XY` with

```
    h3 = H^(3)_n ,  a3 = A3(k) ,  X = A2(l) − A2(k) ,  Y = Psi_k = A1(k) + 3 B1(k) .
```

Since `dX_τ := τ.X − X` and `dY_τ := τ.Y − Y` are **rational**,
`τ.(XY) − XY = X·dY + Y·dX + dX·dY`, hence

> **`E(ṽ)/T = c₀ + β·( A₂(l) − A₂(k) ) + α·Ψ_k`  — rank 3, exactly as §4ter/§11,**
> `α = Σ_τ (G_τ/T)·½dX_τ`, `β = Σ_τ (G_τ/T)·½dY_τ`,
> `c₀ = Σ_τ (G_τ/T)·( dh₃_τ + 2da₃_τ + ½dX_τ dY_τ )`.

The rational data, in `certP.wl`'s own idiom (`sumi[e,j] = Σ_{i=1}^{j} e`):

| τ | `dh3` | `da3` | `dX` | `dY` |
|---|---|---|---|---|
| `n_j` (j=1,2,3) | `sumi[1/(n+i)³, j]` | `sumi[1/(n+i+k)³, j]` | `sumi[1/(n+i+l)² − 1/(n+i+k)², j]` | `sumi[1/(n+i+k) + 3/(n+i−k), j]` |
| `kk` | `0` | `1/(n+k+1)³ − 1/(k+1)³` | `−[1/(n+k+1)² − 1/(k+1)²]` | `[1/(n+k+1) − 1/(k+1)] − 3[1/(n−k) + 1/(k+1)]` |
| `ll` | `0` | `0` | `1/(n+l+1)² − 1/(l+1)²` | **`0`** |

Two structural facts fall out for free:

* **`dY_ll = 0`**, so for `τ = ll` the whole `Ψ_k` branch vanishes — the weight-3 analogue
  of §17.3's `p_ll = r_ll = 0`, and it now happens for the *l*-shift of the **only**
  `l`-carrying letter;
* `Ψ_k` is `l`-free and `X` is a **difference of a pure-`l` and a pure-`k` letter**, so the
  §18.1 four-piece split, if it is ever wanted again, degenerates to **three** pieces
  (`W P`, `W Q·X`, `W R·Ψ_k`) with letter counts `0 / 4 / 3` instead of `0 / 2 / 4 / 4`.

**Independent check (`checkrec.py`, exact ℚ):** `Σ_{k,l} T·ṽ = P̂_n` for `n = 0…33`, and
`L_BZ·(Σ T·ṽ) = 0` for `n = 0…30`, using `core.rec_residual`'s certified V6b coefficients —
so `ṽ` demonstrably lives in the known `(3,9)` box.

---

## 5. What this means for the Theorem-B certificate

1. **Route 1 of §18.13 is closed.** "Re-fold the combination to ≤ 4 letters" is not
   possible; §18.15's "single highest-value next action" has been executed and returns a
   negative. This is the weight-3 analogue of §16's `(T1-top)` negative and should be
   recorded the same way.
2. **Route 2 is cheaper than it was, by an unquantified amount.** Two objects, both
   improved:

   | object `Annihilator` must close | for `v` | for `ṽ` |
   |---|---|---|
   | `T·w` (direct: `Annihilator` then `ct` on `S_k−1, S_l−1` in `Support → {1,S_n,S_n²,S_n³}`) | 12 symbols | **10** |
   | `E(w)` (via the `[CERTIFIED]` Q-row, §4bis + §4ter) | 9 symbols — **OOM 14.4 GB**, §13.1 | **7** |

   §18.17's calibration has data at 9 (OOM), 3 (69 s) and 0 (34 s) but none at 7, so the
   honest statement is: **untested, and the cheapest untested thing on the board.**
   The cheapest single experiment is `Annihilator[E(ṽ), {S[n],S[k],S[l]}]` with §4.6's
   rational data dropped into `certP.wl` (a 20-line edit: replace `A2k`/`Psi`/`vw` and the
   four `dA2f`/`dPsif`/`h3f`/`a3f` tables) and `MEMCAP` real (§17.5). If it returns, the
   `ct₂` is the *single* known `(3,9)` box.
3. **Soundness is intact.** `ŵ₃ − ṽ` is in the proved kernel, so a certificate for `ṽ`
   *is* a certificate for Theorem B. No new uncertified obligation is created. (This is
   the one place where the naive "any representative will do" would have been unsound, and
   it is why the optimisation was rerun inside the proved affine set at a cost of one
   symbol.)
4. **`ṽ` also passes the weight-3 depth calculus — but do not substitute it downstream
   without redoing Lemma G.** Theorem B's *statement* is unchanged (it is still about
   `ŵ₃`), so nothing downstream needs `ṽ`. Still, it is worth recording that `ṽ` is not
   disqualified: `PHASE2_ENDGAME` §35–60 **Observation 1** ("every monomial contains an
   `A₂` or `A₃` letter") **holds** for `ṽ − H^(3)_n` (its `A₂` merely sometimes sits on the
   `l` slot, which the `(D-TRIGGER)` argument tolerates — it needs `α = 1` *or* `γ = 1`),
   and `depth_vt.py` confirms numerically over **29 061 cells** (`p = 5…31`, all `n < p`,
   all `0 ≤ k,l ≤ n`): `max d₃ = 3` and **0 violations** of `d₃ ≤ 1 + min(v_pT, 2)` — the
   same figures as the control `v = ŵ₃ − H^(3)_n`. What would still need redoing is Lemma
   G's five-monomial-type case analysis and the Lemma-D++ off-regime budgets, which are
   written against `ŵ₃`'s specific monomials. **So: certify `ṽ`, state Theorem B for `ŵ₃`.**
5. **A 6-dimensional gap in the proved kernel is now visible and is worth closing.**
   `dim ker V = 63`, `dim span(proved) = 57`. `PHASE2_CANCEL` §3's remark says the
   weight-3 residue identities exist (the `G(x)/((x+i)(x+i'))` construction, the `(V2)`
   analogue) but they have never been written down. Writing them would very likely close
   the 6 and, since the unconstrained optimum `w₉` sits at **distance exactly 1** from the
   proved span (rank `57 → 58`), might buy the last symbol (`S = 10 → 9`).

---

## 6. Files (`work/refold/`)

| file | what |
|---|---|
| `w3full.py` | the unsymmetrised weight-3 basis (98 columns), design matrix, symbol census, exact linear algebra. Built on `work/lb5/fit.py`. |
| `run1.py` | instrument validation (`v` and `ŵ₃` → residual 0) + exhaustive whole-summand symbol minimisation |
| `run2.py` | the same for the degree-≥2 (`E`) metric |
| `run4.py` | Pareto frontier `min S` vs `E` |
| `exact.py` | exact-ℚ design matrix, solver, held-out validator |
| `run5.py` | exact construction + held-out check of the unconstrained optima `w₉`, `w₇` |
| `polyfit.py` | polynomial-coefficient design matrices (`n^a k^b l^c · μ`), 13-bit float split matmul |
| `run3.py` | the ≤ 4-symbol sweep: `p`-adic pole filter + fit, with the excess-equation guard |
| `valpoly.py` | polyfit controls (two positives, one negative, second prime) |
| `vp_phat.py` | `min_{n<p} v_p(P̂_n) = −1`, `p = 5…59` |
| `kernel_proved.py` | the proved kernel (Lemma Phi, Lemma Φ₂, folding), its dimension, membership tests |
| `run6.py` | symbol minimisation **inside the proved affine set** |
| `run7.py` | exact construction + exact verification of `ṽ`; writes `wtilde3_proved.json` |
| `keyid.py` | the single refold identity, exact + proved-span membership |
| `checkrec.py` | independent exact check that `Σ T·ṽ = P̂` and `L_BZ·(Σ T·ṽ) = 0` |
| `depth_vt.py` | the weight-3 depth bound `d₃ ≤ 1+min(v_pT,2)` for `ṽ`, 29 061 cells, 0 violations |
| `wtilde3.json`, `wtilde3_proved.json` | the representatives, machine-readable |
| `s3_*.log`, `ctrl8_D2.log`, `stage3_*.json`, `search_*.json` | the sweep logs and per-mask verdicts (`stage3_S_S4_D2.json` holds the first `dp=2` sweep, whose console output went to the task log) |

**Reproduce:** `python3 run1.py 240 33554393 9`, then `run2.py`, `run4.py`, `run5.py`,
`kernel_proved.py`, `run6.py`, `run7.py`. Total ≈ 20 min, pure Python + numpy.
The ≤ 4 sweeps: `SMAX=4 DP=2 DM=3 python3 run3.py` (≈ 4 min each).

---

## 7. What a successor should NOT re-run

* the ≤ 4-symbol search in the `{A,B,C,N}_{r≤3}` alphabet, in any of the four sweeps above
  — it is exhaustive and negative at two primes;
* the constant-coefficient minimisation — 9 (summand) / 7 (`E`) are exact minima, and
  10 / 7 inside the proved affine set;
* looking for a pole-free (`B`,`N`-only) representative — `v_p(P̂_n) = −1` forbids it.

**The one thing to run next:** `Annihilator[T·ṽ, {S[n],S[k],S[l]}]` under a real memory
cap. It is the only untested point on §18.17's calibration curve that matters, and `ṽ` is
the smallest object that has ever been offered to it.
