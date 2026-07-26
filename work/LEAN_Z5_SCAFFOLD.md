# LEAN_Z5_SCAFFOLD — certificate-independent Lean infrastructure for the compact ζ(5) closed forms

**Author:** lean-agent (River's odd-zeta program), 2026-07-26
**Module:** `lean/ZetaLucas/BZClosedForm.lean` (753 lines, new), wired into `lean/ZetaLucas.lean`
**Toolchain:** Lean `v4.33.0-rc1`, Mathlib `cd580e54`
**Upstream statements:** `work/ZETA5_CLOSEDFORM.md` §0, `work/lb5/core.py`, `work/PROOF_LB5_CAMPAIGN.md` §1

---

## 0. HEADLINE

The whole closed-form theorem is now formalised **except one named hypothesis**.

```
$ lake build
Build completed successfully (8672 jobs).
warning: ZetaLucas/BZClosedForm.lean:660:8: declaration uses `sorry`
```

That is the *only* warning and the *only* `sorry` in the development. Everything else —
the harmonic-letter calculus, the absorption ("Lemma 0") calculus for `T`, the certified
order-3 operator `L_BZ` with its numerical audit, the initial values of both double sums, and
the three-step uniqueness induction — is machine-checked with axioms
`[propext, Classical.choice, Quot.sound]` only.

Two versions of each closed form are proved:

| theorem | hypothesis | axioms |
|---|---|---|
| `PhatSum_eq_Phat_of_rec : BZRec PhatSum → ∀ n, PhatSum n = Phat n` | the reduction, as an argument | **clean** |
| `PSum_eq_PBZ_of_rec : BZRec PSum → ∀ n, PSum n = PBZ n` | the reduction, as an argument | **clean** |
| `PhatSum_eq_Phat : ∀ n, PhatSum n = Phat n` | — | `sorryAx` |
| `PSum_eq_PBZ : ∀ n, PSum n = PBZ n` | — | `sorryAx` |
| `BZ_Phat_closed_form_explicit` (all definitions expanded) | — | `sorryAx` |

When the WZ certificate lands, `bz_creative_telescoping` is discharged and the last three become
clean automatically. **No other line of the file changes.**

---

## 1. THE QUARANTINED LEMMA — exact statement

`lean/ZetaLucas/BZClosedForm.lean`, §5, section `QuarantinedReductionLemma`, line 660:

```lean
def BZRec (Y : ℕ → ℚ) : Prop :=
  ∀ n : ℕ, cc0 n * Y n + cc1 n * Y (n + 1) + cc2 n * Y (n + 2) + cc3 n * Y (n + 3) = 0

theorem bz_creative_telescoping : BZRec PhatSum ∧ BZRec PSum := by
  sorry
```

Fully unfolded, the first conjunct is

```
∀ n : ℕ,
    cc0 n * (∑ k ∈ range (n+1), ∑ l ∈ range (n+1), (T n     k l : ℚ) * w3h n     k l)
  + cc1 n * (∑ k ∈ range (n+2), ∑ l ∈ range (n+2), (T (n+1) k l : ℚ) * w3h (n+1) k l)
  + cc2 n * (∑ k ∈ range (n+3), ∑ l ∈ range (n+3), (T (n+2) k l : ℚ) * w3h (n+2) k l)
  + cc3 n * (∑ k ∈ range (n+4), ∑ l ∈ range (n+4), (T (n+3) k l : ℚ) * w3h (n+3) k l)
  = 0
```

and the second is the same with `w3h → w5`. (`PhatSum_eq_sum_range` / `PSum_eq_sum_range`
let you take **all four** ranges to be `range (n+4)`; see §5.4.)

The lemma is `[VERIFIED exactly over ℚ, n = 0…31]` upstream (`work/z5cf/final_forms.py`).
Its `n = 0` instance is additionally **kernel-checked inside the Lean file** (§3.4 below).

---

## 2. WHAT COMPILES — inventory

### S1. Bare harmonic letters and shifts (§1 of the module)

`Harm` is reused from `Instances.lean`; `Harm_succ` from `MinimalForm.lean` is the only
analytic input.

```lean
def Ad (r n x : ℕ) : ℚ := Harm r (n + x) - Harm r x      -- A_r(x)
def Bd (r n x : ℕ) : ℚ := Harm r (n - x) - Harm r x      -- B_r(x), truncated subtraction
```

| lemma | statement | hypotheses |
|---|---|---|
| `Ad_succ_arg` `@[simp]` | `A_r(x+1) = A_r(x) + 1/(n+x+1)^r − 1/(x+1)^r` | **none** |
| `Ad_succ_n` | `A_r^{(n+1)}(x) = A_r^{(n)}(x) + 1/(n+x+1)^r` | **none** |
| `Bd_succ_arg` | `B_r(x+1) = B_r(x) − 1/(n−x)^r − 1/(x+1)^r` | `0 < r` only |
| `Bd_succ_n` | `B_r^{(n+1)}(x) = B_r^{(n)}(x) + 1/(n+1−x)^r` | `0 < r` only |
| `Harm_zero'`, `Ad_zero`, `Bd_zero` | `H^(r)_0 = 0`, `A_r(0) = B_r(0) = H^(r)_n` | `0 < r` |

**Design point worth knowing.** The `B`-letters use truncated ℕ subtraction, and the correction
terms are written `1 / ((n − x : ℕ) : ℚ)^r` (cast *after* truncation). For `x ≥ n` this is
`1/0^r = 0` and `H^(r)_{n−x} = H^(r)_0 = 0`, so **both shift lemmas hold for every `x` with no
range hypothesis**. A telescoping argument that runs off the end of the summation range (which
this one must — the ranges go to `n+4`) never needs a boundary case.

### S2. Weights, sums, range extension (§2)

```lean
def alph  (n k l : ℕ) : ℚ := Ad 1 n k - Ad 1 n l                      -- α
def bet   (n k l : ℕ) : ℚ := Bd 1 n k - Bd 1 n l                      -- β
def psiBZ (n k l : ℕ) : ℚ := (1/2) * alph n k l + bet n k l           -- Ψ

def w3h (n k l : ℕ) : ℚ := Harm 3 (n+k) - psiBZ n k l * Harm 2 (n+k)

def w5 (n k l : ℕ) : ℚ :=
  Harm 5 (n+k)
    + (1/2) * (alph n k l - bet n k l) * Harm 4 (n+k)
    + ((1/4) * (Ad 2 n k + Ad 2 n l) - (1/2) * alph n k l * psiBZ n k l) * Harm 3 (n+k)

def PhatSum (n : ℕ) : ℚ := ∑ k ∈ range (n+1), ∑ l ∈ range (n+1), (T n k l : ℚ) * w3h n k l
def PSum    (n : ℕ) : ℚ := ∑ k ∈ range (n+1), ∑ l ∈ range (n+1), (T n k l : ℚ) * w5  n k l
```

`T` is **reused** from `BrownZudilin.lean`, not redefined; `T_eq_zero_of_lt_left/right` there
give the range extension.

**Nested sums, not `range (n+1) ×ˢ range (n+1)`** — reasons, all load-bearing downstream:
(i) it matches `ZetaLucas.Q` verbatim, so `Q_eq_sum_range` transports with no reindexing;
(ii) the telescoping input is a *pair* `(ρ, σ)`, one certificate per index, and
`Finset.sum_range_sub` collapses one index at a time — on a product `Finset` each collapse
would need a `Finset.sum_product` first; (iii) `Finset.sum_comm`, used in `Q_lucas`, is stated
for nested sums.

```lean
theorem sum_T_eq_sum_range (w : ℕ → ℕ → ℕ → ℚ) {n N : ℕ} (h : n + 1 ≤ N) :
    ∑ k ∈ range (n+1), ∑ l ∈ range (n+1), (T n k l : ℚ) * w n k l
      = ∑ k ∈ range N, ∑ l ∈ range N, (T n k l : ℚ) * w n k l
theorem PhatSum_eq_sum_range {n N : ℕ} (h : n + 1 ≤ N) : PhatSum n = ∑ k ∈ range N, …
theorem PSum_eq_sum_range    {n N : ℕ} (h : n + 1 ≤ N) : PSum n    = ∑ k ∈ range N, …
```

The `sum_T_eq_sum_range` version is stated for an **arbitrary weight `w`**, so it also serves
any future companion row.

### S2.1 "Lemma 0" for `T` — the absorption calculus (§2.1, **added beyond the brief**)

This is the Brown–Zudilin analogue of `MinimalForm.l0a`–`l0d`, and it is exactly what a WZ
certificate has to be fed through to become a `ring` identity. All are **division-free
identities in ℚ valid for all `n,k,l ≥ 0`** — no range hypothesis, no `0/0`.

```lean
theorem T_symm    (n k l : ℕ) : T n k l = T n l k
theorem T_shift_k (n k l : ℕ) :
    (T n (k+1) l : ℚ) * ((k+1)^3 * (k+l+1)) = (T n k l : ℚ) * ((n+k+1) * (n−k)^2 * (n+k+l+1))
theorem T_shift_l (n k l : ℕ) :
    (T n k (l+1) : ℚ) * ((l+1)^3 * (k+l+1)) = (T n k l : ℚ) * ((n+l+1) * (n−l)^2 * (n+k+l+1))
theorem T_shift_n (n k l : ℕ) :
    (T (n+1) k l : ℚ) * ((n+1−k)^2 * (n+1−l)^2)
      = (T n k l : ℚ) * ((n+1) * (n+k+1) * (n+l+1) * (n+k+l+1))
theorem T_shift_n2 (n k l : ℕ) : …     -- two-step, cascaded grouping
theorem T_shift_n3 (n k l : ℕ) : …     -- three-step, cascaded grouping
```

Supporting: `absorbU (N k) : C(N+1,k+1)·(k+1) = (N+1)·C(N,k)` over ℚ (from
`Nat.add_one_mul_choose_eq`) — the upper-index absorption that `MinimalForm.absorb`/`absorb2`
do not cover; `T_cast`; and `absorb_chain`, a 5-line algebraic helper.

> **Performance note the certificate agent must respect.** `T_shift_n2`/`T_shift_n3` are stated
> in a *cascaded* product grouping `T(n+2)·((C)·(A)) = T(n)·((B)·(D))`. Proving them via
> `linear_combination` on the flattened, fully-expanded form (degree 24 in 3 variables) costs
> **58 s**; via `absorb_chain` in the cascaded grouping it costs **8 s**. Deliver the
> certificate pre-factored, not expanded (§5.6).

The underlying factorial identity, useful for deriving anything else:

```
T(n,k,l) = n! · (n+k)! · (n+l)! · (n+k+l)!
           ────────────────────────────────────────────
           (k!)³ (l!)³ ((n−k)!)² ((n−l)!)² (k+l)!
```

### S3. `L_BZ` and the two companion rows (§3)

Transcribed verbatim from `work/lb5/core.py` (V6b normalised); all four coefficients degree 9.

```lean
def a0P (x : ℚ) : ℚ := 41218*x^3 + 198849*x^2 + 320790*x + 173057
def B8P (x : ℚ) : ℚ := 3874492*x^8 + 59373972*x^7 + 394148190*x^6 + 1481084196*x^5
                     + 3447878810*x^4 + 5095855458*x^3 + 4673546679*x^2
                     + 2433871008*x + 551502039
def B9P (x : ℚ) : ℚ := 48802112*x^9 + 967468896*x^8 + 8488000862*x^7 + 43246197636*x^6
                     + 140983768422*x^5 + 304912330849*x^4 + 437406946975*x^3
                     + 401272692378*x^2 + 213593890911*x + 50257929339

def cc0 (n : ℕ) : ℚ := (n+1)^5 * (n+2) * a0P (n+1)
def cc1 (n : ℕ) : ℚ := -2 * (n+2) * B8P n
def cc2 (n : ℕ) : ℚ := -2 * B9P n
def cc3 (n : ℕ) : ℚ := 2 * (n+3)^5 * (2*n+5) * a0P n

theorem cc3_pos (n : ℕ) : 0 < cc3 n        -- by positivity; the recurrence never degenerates
```

```lean
def Phat : ℕ → ℚ | 0 => 0 | 1 => 101/4 | 2 => 344923/96
  | (n+3) => -(cc0 n * Phat n + cc1 n * Phat (n+1) + cc2 n * Phat (n+2)) / cc3 n
def PBZ  : ℕ → ℚ | 0 => 0 | 1 => 87/4  | 2 => 1190161/384
  | (n+3) => -(cc0 n * PBZ n + cc1 n * PBZ (n+1) + cc2 n * PBZ (n+2)) / cc3 n

theorem Phat_bzrec : BZRec Phat
theorem PBZ_bzrec  : BZRec PBZ
```

`P̂₂ = 344923/96` was not in the brief; it is the exact ladder value
(`falsify_data/ladder_Ph.json`, re-read for this task) and is the third initial condition an
order-3 recurrence needs.

### S3.1 Transcription audit — all kernel-checked `example`s in the file

| check | value |
|---|---|
| `Phat 3` | `3710571371/4320` ✓ |
| `Phat 4` | `602417685937/2304` ✓ |
| `PBZ 3` | `7682021239/10368` ✓ |
| `PBZ 4` | `24943788950905/110592` ✓ |
| **`cc0 0·Q₀ + cc1 0·Q₁ + cc2 0·Q₂ + cc3 0·Q₃ = 0`** | ✓, with `Q₀…Q₃ = 1, 21, 2989, 714549` obtained by `decide` from `ZetaLucas.Q`, i.e. from the **double binomial sum**, not from any recurrence |

The `Q` cross-check is the strongest one: it pins all four degree-9 coefficients against an
object defined independently of the recurrence, in another module.

### S3.2 Initial values of the double sums — computed from the definitions

```lean
theorem PhatSum_zero : PhatSum 0 = 0            theorem PSum_zero : PSum 0 = 0
theorem PhatSum_one  : PhatSum 1 = 101/4        theorem PSum_one  : PSum 1 = 87/4
theorem PhatSum_two  : PhatSum 2 = 344923/96    theorem PSum_two  : PSum 2 = 1190161/384
theorem PhatSum_three : PhatSum 3 = 3710571371/4320
theorem PSum_three    : PSum 3    = 7682021239/10368
```

All six by `norm_num [PhatSum, w3h, psiBZ, alph, bet, Ad, Bd, Harm, K, triv, T,
Finset.sum_range_succ, …]` plus a handful of `Nat.choose` numerals as `rfl` lemmas — the same
recipe as `MinimalForm`'s `bMin 2 = 351/4`.

### S3.3 Weight expansions (§3.3)

Pure `ring` identities that pin the reading of the campaign's letters:

```lean
theorem psiBZ_expand : Ψ = ½H⁽¹⁾_{n+k} − ½H⁽¹⁾_{n+l} + H⁽¹⁾_{n−k} − H⁽¹⁾_{n−l}
                            − (3/2)H⁽¹⁾_k + (3/2)H⁽¹⁾_l
theorem alph_sub_bet_expand : α − β = H⁽¹⁾_{n+k} − H⁽¹⁾_{n+l} − H⁽¹⁾_{n−k} + H⁽¹⁾_{n−l}
theorem Ad2_sum_expand : A₂(k) + A₂(l) = H⁽²⁾_{n+k} − H⁽²⁾_k + H⁽²⁾_{n+l} − H⁽²⁾_l
theorem w3h_expand, w5_expand
```

These confirm the counts of `ZETA5_CLOSEDFORM` §0/§3: `ŵ₃` = 7 monomials in 8 symbols,
`w₅` = 27 monomials in 13 symbols.

### S3.4 The reduction lemma, kernel-checked at `n = 0`

```lean
example : cc0 0 * PhatSum 0 + cc1 0 * PhatSum 1 + cc2 0 * PhatSum 2 + cc3 0 * PhatSum 3 = 0
example : cc0 0 * PSum 0    + cc1 0 * PSum 1    + cc2 0 * PSum 2    + cc3 0 * PSum 3    = 0
```

Both pass. Nothing here touches `Phat`/`PBZ` or the recurrence definition: the four values come
from the double sums and the four coefficients from `L_BZ`. This is `bz_creative_telescoping`
at `n = 0`, verified by the kernel.

### S4. The induction (§4) — `sorry`-free

```lean
theorem eq_of_BZRec {Y Z : ℕ → ℚ} (hY : BZRec Y) (hZ : BZRec Z)
    (h0 : Y 0 = Z 0) (h1 : Y 1 = Z 1) (h2 : Y 2 = Z 2) : ∀ n, Y n = Z n
```

Three-step induction on the triple `(Y n, Y (n+1), Y (n+2))`; the step is
`mul_left_cancel₀ (cc3_ne m)` applied to a single `linear_combination` of the two recurrences.
The two conditional closed forms follow immediately (`PhatSum_eq_Phat_of_rec`,
`PSum_eq_PBZ_of_rec`).

### S6. Explicit form

```lean
theorem BZ_Phat_closed_form_explicit (n : ℕ) :
    ∑ k ∈ range (n+1), ∑ l ∈ range (n+1),
      ((C(n+k,n)·C(n,k)²·C(n+l,n)·C(n,l)²·C(n+k+l,n) : ℕ) : ℚ)
        * ( Σ_{j=1}^{n+k} 1/j³
            − ( ½Σ_{j=1}^{n+k}1/j − ½Σ_{j=1}^{n+l}1/j + Σ_{j=1}^{n−k}1/j − Σ_{j=1}^{n−l}1/j
                − (3/2)Σ_{j=1}^{k}1/j + (3/2)Σ_{j=1}^{l}1/j ) · Σ_{j=1}^{n+k}1/j² )
      = Phat n
```

every definition of the file expanded (`Harm_eq` from `MinimalForm`), in the style of
`apery_b_harmonic_closed_form`.

---

## 3. `#print axioms` — verbatim build output

```
'ZetaLucas.BZCF.Ad_succ_arg'            [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.Ad_succ_n'              [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.Bd_succ_arg'            [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.Bd_succ_n'              [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.sum_T_eq_sum_range'     [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.T_shift_k'              [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.T_shift_l'              [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.T_shift_n'              [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.T_shift_n2'             [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.T_shift_n3'             [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.T_symm'                 [propext, Quot.sound]
'ZetaLucas.BZCF.cc3_pos'                [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.Phat_bzrec'             [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.PBZ_bzrec'              [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.PhatSum_zero/one/two'   [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.PSum_zero/one/two'      [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.w3h_expand'             [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.w5_expand'              [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.eq_of_BZRec'            [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.PhatSum_eq_Phat_of_rec' [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.PSum_eq_PBZ_of_rec'     [propext, Classical.choice, Quot.sound]
--- below the line: the quarantined lemma and its two consequences ---
'ZetaLucas.BZCF.bz_creative_telescoping' [propext, sorryAx, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.PhatSum_eq_Phat'         [propext, sorryAx, Classical.choice, Quot.sound]
'ZetaLucas.BZCF.PSum_eq_PBZ'             [propext, sorryAx, Classical.choice, Quot.sound]
```

`#eval` cross-checks printed by the build:

```
Phat    : [0, 101/4, 344923/96, 3710571371/4320, 602417685937/2304]
PBZ     : [0,  87/4, 1190161/384, 7682021239/10368, 24943788950905/110592]
PhatSum : [0, 101/4, 344923/96, 3710571371/4320]
PSum    : [0,  87/4, 1190161/384, 7682021239/10368]
```

---

## 4. Numerical re-verification done for this task (independent of the Lean side)

* `work/z5cf/final_forms.py` re-run: both closed forms exact for `n = 0…34`; `L_BZ` annihilates
  both for `n = 0…31`. Zero discrepancies.
* `work/lb5/core.py` residuals `rec_residual(Q/P/Ph, n) = 0` for `n = 0…5`, confirming the
  transcribed coefficients against the ladders.
* Ladder values used as initial conditions read directly from
  `/home/ubuntu/fable-episode-2/zeta-math/worthiness/falsify_data/ladder_{Q,P,Ph}.json`.

---

## 5. §S5 — INTERFACE SPEC for the WZ certificate

This is the contract. Everything on the Lean side is already built; the deliverables below are
what is missing, in the shape that makes the Lean proof mechanical.

### 5.1 The operator

`L_BZ = Σ_{i=0}^{3} c_i(n)·N^i`, `N` = shift `n ↦ n+1`, `c_i` as in §S3 above
(Lean: `cc0, cc1, cc2, cc3 : ℕ → ℚ`). `c_3(n) = 2(n+3)⁵(2n+5)a₀(n) > 0` for all `n ≥ 0`
(`cc3_pos`), so there is no degenerate level.

For `w ∈ {ŵ₃, w₅}` define the **operator applied to the summand**

```
E_w(n,k,l) := Σ_{i=0}^{3} c_i(n) · T(n+i,k,l) · w(n+i,k,l)
```

— note `w(n+i,k,l)` means `n` is replaced by `n+i` **inside the letters too**
(`A_r`, `B_r`, and the arguments `n±k`, `n±l`, `n+k`). In Lean this is literally
`w3h (n+i) k l` / `w5 (n+i) k l`.

### 5.2 D1 — the base term Φ (**required** normalisation, not merely recommended)

⚠ **The naive base `T(n,k,l)` does not work here, and the reason is not obvious.**
`T(n,k,l) = 0` for `k > n`, whereas `T(n+i,k,l) ≠ 0` up to `k = n+i`. So
`E_w(n, n+1, l) ≠ 0` in general, while any `R_w` written as `(rational)·T(n,k,l)·(letters)` is
`0` at `k = n+1` unless the rational has a **pole** there. Hence certificates over the base
`T(n,k,l)` necessarily have poles at `k = n+1, n+2, n+3` — which are *interior* points of the
telescoping range `0 ≤ k ≤ n+4`, where `R_w` must be finite for `Σ_{k<N}(R(k+1) − R(k))` to
collapse. (In Lean this bites hard: `1/0 = 0`, so the poles silently evaluate to `0` and the
telescoping identity is simply **false** at `k = n` and `k = n+1`.)

Clearing denominators does not rescue it either: the common denominator
`(n+1−k)²(n+1−l)²…` depends on `k` and `l`, so it cannot be pulled out of the double sum.

Use instead the pole-free base

```
Φ(n,k,l) := T(n+3,k,l)
            ───────────────────────────────────────────────────────────────────────────
            (n+1)(n+2)(n+3)·(n+k+1)(n+k+2)(n+k+3)·(n+l+1)(n+l+2)(n+l+3)
                          ·(n+k+l+1)(n+k+l+2)(n+k+l+3)
```

Every denominator factor is **strictly positive for all `n,k,l ≥ 0`** — Φ has no pole anywhere
in the range — and

```
T(n+i,k,l) = Φ(n,k,l) · P_i(n,k,l),   P_i ∈ ℤ[n,k,l],  deg P_i = 12,   i = 0,1,2,3

P_i = ∏_{j=1}^{i} (n+j)(n+k+j)(n+l+j)(n+k+l+j)
      · [ ∏_{j=i+1}^{3} (n+j−k) ]² · [ ∏_{j=i+1}^{3} (n+j−l) ]²
```

explicitly

```
P_0 = [(n+1−k)(n+2−k)(n+3−k)]² [(n+1−l)(n+2−l)(n+3−l)]²
P_1 = (n+1)(n+k+1)(n+l+1)(n+k+l+1) · [(n+2−k)(n+3−k)]² [(n+2−l)(n+3−l)]²
P_2 = (n+1)(n+2)(n+k+1)(n+k+2)(n+l+1)(n+l+2)(n+k+l+1)(n+k+l+2) · (n+3−k)² (n+3−l)²
P_3 = (n+1)(n+2)(n+3)(n+k+1)(n+k+2)(n+k+3)(n+l+1)(n+l+2)(n+l+3)
        (n+k+l+1)(n+k+l+2)(n+k+l+3)
```

Φ's own steps (the analogue of `MinimalForm.l0d`):

```
Φ(n,k+1,l)·(k+1)³(k+l+1) = Φ(n,k,l)·(n+3−k)²(n+k+1)(n+k+l+1)
Φ(n,k,l+1)·(l+1)³(k+l+1) = Φ(n,k,l)·(n+3−l)²(n+l+1)(n+k+l+1)
```

Also `Φ(n,n+4,l) = Φ(n,k,n+4) = 0` (because `C(n+3,n+4) = 0`), which is what gives the top
boundary for free.

**Lean status.** All six identities are one `field_simp`/`linear_combination` away from the
already-proved `T_shift_k`, `T_shift_l`, `T_shift_n`, `T_shift_n2`, `T_shift_n3`. They are not
in the file because their optimal *grouping* depends on the shape the certificate arrives in
(see the performance note in §S2.1).

### 5.3 D2 — the letter shift table (**already fixed; do not renegotiate**)

Convention throughout: `1/0^r = 0` (Lean ℚ), and `H^(r)_{n−x} := H^(r)_{max(n−x,0)}`.

| symbol | `Δ_n` | `Δ_k` | `Δ_l` | Lean lemma |
|---|---|---|---|---|
| `H^(r)_{n+k}` | `1/(n+k+1)^r` | `1/(n+k+1)^r` | 0 | `Harm_succ` |
| `H^(r)_{n+l}` | `1/(n+l+1)^r` | 0 | `1/(n+l+1)^r` | `Harm_succ` |
| `H^(r)_{n−k}` | `1/(n+1−k)^r` | `−1/(n−k)^r` | 0 | `Bd_succ_n`, `Bd_succ_arg` |
| `H^(r)_{n−l}` | `1/(n+1−l)^r` | 0 | `−1/(n−l)^r` | `Bd_succ_n`, `Bd_succ_arg` |
| `H^(r)_k` | 0 | `1/(k+1)^r` | 0 | `Harm_succ` |
| `H^(r)_l` | 0 | 0 | `1/(l+1)^r` | `Harm_succ` |

The composite letters follow: `Ad r n x` via `Ad_succ_arg` / `Ad_succ_n`, `Bd r n x` via
`Bd_succ_arg` / `Bd_succ_n`. **All four hold unconditionally in `k` and `l`** — no `k ≤ n`
side conditions anywhere.

Weights: `ŵ₃` uses 8 symbols (`H⁽³⁾_{n+k}, H⁽²⁾_{n+k}, H⁽¹⁾_{n+k}, H⁽¹⁾_{n+l}, H⁽¹⁾_{n−k},
H⁽¹⁾_{n−l}, H⁽¹⁾_k, H⁽¹⁾_l`), `w₅` uses 13 (those plus `H⁽⁵⁾_{n+k}, H⁽⁴⁾_{n+k}, H⁽²⁾_{n+l},
H⁽²⁾_k, H⁽²⁾_l`).

### 5.4 D3 — the WZ pair, and the boundary conditions

Let `M_1, …, M_J` be the shift closure of `w`'s monomials under `Δ_n, Δ_k, Δ_l`
(`ZETA5_CLOSEDFORM` §3: **J = 15 for `ŵ₃`, J = 64 for `w₅`**). Deliver rational functions
`ρ_j, σ_j ∈ ℚ(n,k,l)`, `j = 1…J`, such that with

```
R_w(n,k,l) := Φ(n,k,l) · Σ_j ρ_j(n,k,l) · M_j(n,k,l)
S_w(n,k,l) := Φ(n,k,l) · Σ_j σ_j(n,k,l) · M_j(n,k,l)
```

the **single telescoping identity**

```
(★)   E_w(n,k,l)  =  [ R_w(n,k+1,l) − R_w(n,k,l) ]  +  [ S_w(n,k,l+1) − S_w(n,k,l) ]
```

holds as an identity of rational functions in `(n,k,l)` — equivalently, in Lean, for all
`n k l : ℕ`.

**Boundary conditions.** Take `N := n+4`; then `PhatSum_eq_sum_range` (resp. `PSum_…`) puts all
four sums of `BZRec` over `range N × range N`, and

```
Σ_{k<N} Σ_{l<N} E_w  =  Σ_{l<N} [ R_w(n,N,l) − R_w(n,0,l) ]  +  Σ_{k<N} [ S_w(n,k,N) − S_w(n,k,0) ]
```

so it suffices that

* **(B-top)** `R_w(n,N,l) = 0` and `S_w(n,k,N) = 0` for `0 ≤ k,l < N`.
  *Free* if `R_w, S_w` are written over the base `Φ`, since `Φ(n,N,l) = Φ(n,k,N) = 0`, provided
  the `ρ_j, σ_j` are pole-free at `k = N` resp. `l = N`.
* **(B-bot)** `R_w(n,0,l) = 0` and `S_w(n,k,0) = 0` for `0 ≤ k,l < N`.
  Expect this to come from a numerator factor `k³` in every `ρ_j` and `l³` in every `σ_j` — the
  `(k+1)³` in the Φ-step identity is the `MinimalForm` `Gfun = Φ·k⁴·T` pattern one index wider.
  **If it does not, say so explicitly** and supply the two boundary sums in closed form; they
  then have to be shown to cancel, which is extra Lean work not currently scaffolded.

*If the certificate you have does not satisfy (B-bot), the standard fix is to add a Gosper
correction term as in `MinimalForm.propC`/`Kfun`; please do that on the CAS side rather than
leaving it for Lean.*

### 5.5 D4 — what `ring` has to close

After substituting D1 (every `T(n+i,k,l) → Φ·P_i`) and D2 (every letter shift → a rational
function), both sides of (★) are `Φ(n,k,l)` times a `ℚ(n,k,l)`-linear combination of
`M_1, …, M_J`. Cancelling `Φ` and equating coefficients gives **J polynomial identities in
`ℚ[n,k,l]`** (15 for `ŵ₃`, 64 for `w₅`), each of which the Lean proof closes with `ring` (or
`field_simp; ring`). **The deliverable is that list of J identities**, in the form
`LHS_j(n,k,l) = RHS_j(n,k,l)`, together with the common denominator that was cleared.

That is the whole certificate. The Lean proof of `bz_creative_telescoping` is then, per row:

```lean
intro n
rw [PhatSum_eq_sum_range (N := n+4) (by omega), PhatSum_eq_sum_range (N := n+4) (by omega),
    PhatSum_eq_sum_range (N := n+4) (by omega), PhatSum_eq_sum_range (N := n+4) (by omega),
    Finset.mul_sum, Finset.mul_sum, Finset.mul_sum, Finset.mul_sum,
    ← Finset.sum_add_distrib, ← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
rw [Finset.sum_congr rfl fun k _ => Finset.sum_congr rfl fun l _ => star n k l]   -- (★)
rw [Finset.sum_range_sub …, Finset.sum_range_sub …]                              -- twice
simp [R_top, R_bot, S_top, S_bot]                                                -- boundaries
```

mirroring `MinimalForm.bMin_rec` exactly.

### 5.6 D5 — delivery format and size budget

1. **Pre-factored, not expanded.** Give `ρ_j, σ_j` as `numerator / denominator` with both in
   *product* form. Measured: `ring` on a flattened degree-24 3-variable identity in this file
   costs **58 s**; the same content in cascaded product form costs **8 s**. With J = 64 the
   difference is the whole file's viability.
2. **Machine-readable.** JSON or `.m` with integer coefficient lists per monomial, plus a plain
   text rendering. Name the monomial basis `M_1…M_J` explicitly (symbol multiset per index).
3. **Include a numerical residual check** of (★) itself at, say, `n,k,l ≤ 6` in exact ℚ; that is
   the fastest way for the Lean side to catch a transcription slip before elaborating.
4. **State which of `T_shift_k / T_shift_l / T_shift_n / T_shift_n2 / T_shift_n3 / Φ` your
   normalisation uses**, so the Lean side rewrites in the same direction and avoids a `field_simp`
   blow-up.
5. `ŵ₃` first (J = 15). It is the cheap row and it validates the whole pipeline before the
   64-monomial row is attempted. Note `ZETA5_CLOSEDFORM` §3 records that the REFOLD weight `ṽ`
   has closure rank 11, still smaller than this `ŵ₃`'s 15 — if certification of the weight-3
   row is the goal in itself, `ṽ` is the cheaper object; the new `ŵ₃` is here because it is the
   shape that generalises to weight 5.

### 5.7 Alignment with `work/Z5CF_CERT.md` (concurrent computational-agent)

That report landed while this one was being written. The two specs **agree exactly**, which is
worth recording because it means no translation layer is needed:

| `Z5CF_CERT.md` | this file / Lean |
|---|---|
| `(T-n) (n+1−k)²(n+1−l)² T(n+1,k,l) = (n+1)(n+k+1)(n+l+1)(n+k+l+1) T(n,k,l)` | `T_shift_n` — **already proved** |
| `(T-k) (k+1)³(k+l+1) T(n,k+1,l) = (n−k)²(n+k+1)(n+k+l+1) T(n,k,l)` | `T_shift_k` — **already proved** |
| `(T-l)` | `T_shift_l` — **already proved** |
| `(E1) C(n+k+1,n)(k+1) = C(n+k,n)(n+k+1)` | `absorb (n+k) n` (from `MinimalForm`) |
| `(E2) C(n,k+1)(k+1) = C(n,k)(n−k)` | `absorb2 n k` |
| `(E3) C(n+k+1,n+1)(n+1) = C(n+k,n)(n+k+1)` | `absorbU (n+k) n` (new here) |
| `(E4) C(n+1,k)(n+1−k) = C(n,k)(n+1)` | `absorb n k` |
| §3.3 letter shift table (nine base letters) | §5.3 above, identical entry-for-entry |

Same normalisation, same signs, same conventions. Three things that agent should know:

1. **(T-n), (T-k), (T-l) do not need to be re-derived** — they are theorems in
   `ZetaLucas/BZClosedForm.lean` with clean axioms, together with the composed two- and
   three-step forms `T_shift_n2`, `T_shift_n3` that `L_BZ` actually needs.
2. **The `−1/(n−k)^r` pole of §3.3 is already handled and costs nothing.** With truncated ℕ
   subtraction and Lean's `1/0 = 0`, `Bd_succ_arg`/`Bd_succ_n` hold **for every `k`, with no
   `k ≤ n` hypothesis** — the `k = n` term evaluates to `0` on both sides. Please state the
   certificate with the convention `1/(n−k)^r := 0` at `k = n` so the two sides match; nothing
   else about that pole needs to reach Lean.
3. **§5.2 above is the one place where the specs could diverge.** `Z5CF_CERT.md` §3.2 proposes
   "multiply the whole certificate by the product of the denominators → `T(n,k,l) ×` (identity
   in `ℚ[n,k,l][letters]`)". That is fine for the *identity*, but the multiplier depends on `k`
   and `l`, so it cannot be pulled out of the double sum, and the un-cleared certificate then has
   interior poles at `k = n+1, n+2, n+3`. Express `R_w`, `S_w` over `Φ` (= base `T(n+3,k,l)`),
   whose denominators are all strictly positive on the whole range.

---

## 6. MEASURED EFFORT

| stage | wall clock | notes |
|---|---|---|
| reading (`ZETA5_CLOSEDFORM.md`, `MinimalForm.lean`, `BrownZudilin.lean`, `Letters.lean`, `core.py`), locating `L_BZ` | ~12 min | `L_BZ` is in `work/lb5/core.py`, not in any `.md` |
| numerical re-verification (ladders, initial values, recurrence residuals, `final_forms.py`) | ~4 min | |
| S1 letters + shifts | ~8 min | the unconditional `Bd` shift lemmas took one design iteration (truncated-subtraction convention) |
| S2 weights, sums, range extension | ~6 min | first compile: 2 trivial `field_simp`→`ring` errors |
| S2.1 "Lemma 0" for `T` (beyond brief) | ~22 min | incl. finding `Nat.add_one_mul_choose_eq` and the 58 s → 8 s `absorb_chain` refactor |
| S3 `L_BZ`, `Phat`, `PBZ`, all sanity checks | ~14 min | initial values needed `Nat.choose` numerals as `rfl` lemmas |
| S4 induction + quarantine + explicit form | ~10 min | compiled first try |
| S5 spec + this report | ~18 min | |
| **total** | **~95 min** | |

**Build timings (measured, not estimated).**

| what | time |
|---|---|
| `lake env lean ZetaLucas/BZClosedForm.lean` (file alone) | **13.7 s** |
| `lake build` incremental (file changed) | **~21 s** |
| `lake build` clean rebuild of the whole `ZetaLucas` library (11 modules, 8672 jobs) | **1 m 20 s** |

No step came close to the 90-minute isolate-and-move-on threshold.

---

## 7. WHAT A SUCCESSOR SHOULD DO NEXT

1. **Produce the WZ pair** to the spec of §5. `ZETA5_CLOSEDFORM` §7.1 already flags
   `Annihilator`/creative telescoping on `T·w₅` (∂-module rank 64) as the highest-value action;
   §5 above is the precise output format that makes it land in Lean without rework.
2. Discharge `bz_creative_telescoping`. Nothing else in `BZClosedForm.lean` changes; the three
   `sorryAx` entries in §3 become clean.
3. Optional, cheap, and independent: prove Φ and the six identities of §5.2 in Lean *before* the
   certificate arrives — they are pure consequences of the already-proved `T_shift_*`. Deferred
   here only because the optimal grouping depends on the certificate's shape.
4. Optional: transport `Q_lucas` / Theorem LB to `PhatSum`, `PSum`. Note
   `ZETA5_CLOSEDFORM` §4.2: hypothesis (H4)'s **tameness clause fails** for these weights
   (`n+k`, `n+l` reach `2n`) and *cannot* be arranged, so `TheoremLB.lean` does not apply
   off the shelf — that route needs the Lemma-D substitute first.
