/-
# The compact closed forms for the Brown–Zudilin ζ(5) companion rows

**Source of the statements.**  `work/ZETA5_CLOSEDFORM.md` §0 (the two forms), `work/lb5/core.py`
(the certified order-3 recurrence `L_BZ`, "V6b normalised"), `work/PROOF_LB5_CAMPAIGN.md` §1
(the difference letters and the normalisation `Q₁ = 21`).

**Target.**  With `T(n,k,l) = C(n+k,n)C(n,k)²C(n+l,n)C(n,l)²C(n+k+l,n)` (already defined in
`ZetaLucas/BrownZudilin.lean`) and the *bare* harmonic letters `H^(r)_x`, put

    A_r(x) = H^(r)_{n+x} − H^(r)_x ,     B_r(x) = H^(r)_{n−x} − H^(r)_x
    α = A₁(k) − A₁(l) ,   β = B₁(k) − B₁(l) ,   Ψ = ½α + β
    ŵ₃ = H⁽³⁾_{n+k} − Ψ·H⁽²⁾_{n+k}
    w₅ = H⁽⁵⁾_{n+k} + ½(α−β)·H⁽⁴⁾_{n+k} + ( ¼(A₂(k)+A₂(l)) − ½·α·Ψ )·H⁽³⁾_{n+k}

Then

    P̂_n = Σ_{k,l=0}^{n} T(n,k,l)·ŵ₃ ,      P_n = Σ_{k,l=0}^{n} T(n,k,l)·w₅ ,

where `P̂` and `P` are the Brown–Zudilin companion rows *defined here by the certified order-3
recurrence* `L_BZ` with the exact initial values `P̂ = 0, 101/4, 344923/96` and
`P = 0, 87/4, 1190161/384`.

**Structure of the file** (it is `ZetaLucas/MinimalForm.lean`, one index wider):

* §1  the bare letters `Ad`, `Bd` and their four one-step shift lemmas — the whole engine;
* §2  the two weights `w3h`, `w5` and the two double sums `PhatSum`, `PSum`, with the
      range-extension lemma mirroring `Q_eq_sum_range`, and **§2.1 "Lemma 0" for `T`** — the
      three division-free absorption identities `T_shift_k`, `T_shift_l`, `T_shift_n` that any
      WZ certificate for this family must be fed through;
* §3  `L_BZ` (`cc0 … cc3`, all of degree 9), the two sequences `Phat`, `PBZ`, and the
      `norm_num` sanity checks against the exact ladders of `work/lb5`;
* §4  the three-step induction: `BZRec Y → BZRec Z → (three initial values) → Y = Z`, and the
      closed-form theorems *conditional on* the creative-telescoping reduction;
* §5  **the single quarantined `sorry`** — the reduction lemma `bz_creative_telescoping`, and
      the unconditional closed-form theorems that follow from it.

Everything outside §5 is `sorry`-free; see the `#print axioms` block at the end.
-/
import ZetaLucas.MinimalForm
import ZetaLucas.BrownZudilin

open Finset

namespace ZetaLucas

namespace BZCF

/-! ## 1.  The bare harmonic letters and their shifts

`Harm r y = H^(r)_y = Σ_{m=1}^{y} 1/m^r` is `ZetaLucas.Harm` (from `Instances.lean`), and the
single analytic input is `Harm_succ : H^(r)_{y+1} = H^(r)_y + 1/(y+1)^r` (from
`MinimalForm.lean`).  Everything below is a consequence of it.

The `B`-letters use **truncated** natural subtraction `n − x`.  This is not a defect: for
`x ≥ n` both `H^(r)_{n−x}` and the correction term `1/(n−x)^r` collapse to `0` (because
`(0 : ℚ)^r = 0` for `r ≥ 1` and `1/0 = 0` in `ℚ`), so the shift lemmas below hold **for all
`x`, with no range hypothesis** — exactly what a telescoping argument that runs off the end of
the summation range needs. -/

/-- `H^(r)_0 = 0` for `r ≥ 1`. -/
theorem Harm_zero' {r : ℕ} (hr : 0 < r) : Harm r 0 = 0 := K_zero triv hr

/-- The *difference letter* `A_r(x) = H^(r)_{n+x} − H^(r)_x`
(`work/PROOF_LB5_CAMPAIGN.md` §1). -/
def Ad (r n x : ℕ) : ℚ := Harm r (n + x) - Harm r x

/-- The *difference letter* `B_r(x) = H^(r)_{n−x} − H^(r)_x`, with truncated subtraction. -/
def Bd (r n x : ℕ) : ℚ := Harm r (n - x) - Harm r x

@[simp] theorem Ad_zero (r n : ℕ) (hr : 0 < r) : Ad r n 0 = Harm r n := by
  simp [Ad, Harm_zero' hr]

@[simp] theorem Bd_zero (r n : ℕ) (hr : 0 < r) : Bd r n 0 = Harm r n := by
  simp [Bd, Harm_zero' hr]

/-- **Shift 1 (`k`-step of an `A`-letter).**  `A_r(x+1) = A_r(x) + 1/(n+x+1)^r − 1/(x+1)^r`. -/
@[simp] theorem Ad_succ_arg (r n x : ℕ) :
    Ad r n (x + 1) = Ad r n x + 1 / ((n : ℚ) + x + 1) ^ r - 1 / ((x : ℚ) + 1) ^ r := by
  simp only [Ad, show n + (x + 1) = n + x + 1 from rfl, Harm_succ]
  push_cast
  ring

/-- **Shift 2 (`n`-step of an `A`-letter).**  `A_r^{(n+1)}(x) = A_r^{(n)}(x) + 1/(n+x+1)^r`. -/
theorem Ad_succ_n (r n x : ℕ) :
    Ad r (n + 1) x = Ad r n x + 1 / ((n : ℚ) + x + 1) ^ r := by
  simp only [Ad, show n + 1 + x = n + x + 1 by omega, Harm_succ]
  push_cast
  ring

/-- **Shift 3 (`k`-step of a `B`-letter).**  `B_r(x+1) = B_r(x) − 1/(n−x)^r − 1/(x+1)^r`,
valid for **every** `x` (for `x ≥ n` both correction terms are `0`). -/
theorem Bd_succ_arg {r : ℕ} (hr : 0 < r) (n x : ℕ) :
    Bd r n (x + 1) = Bd r n x - 1 / (((n - x : ℕ) : ℚ)) ^ r - 1 / ((x : ℚ) + 1) ^ r := by
  simp only [Bd, Harm_succ]
  rcases lt_or_ge x n with h | h
  · rw [show n - x = n - (x + 1) + 1 by omega]
    rw [Harm_succ]
    push_cast
    ring
  · rw [show n - (x + 1) = 0 by omega, show n - x = 0 by omega]
    simp only [Nat.cast_zero, zero_pow hr.ne', div_zero]
    ring

/-- **Shift 4 (`n`-step of a `B`-letter).**  `B_r^{(n+1)}(x) = B_r^{(n)}(x) + 1/(n+1−x)^r`,
valid for **every** `x`. -/
theorem Bd_succ_n {r : ℕ} (hr : 0 < r) (n x : ℕ) :
    Bd r (n + 1) x = Bd r n x + 1 / (((n + 1 - x : ℕ) : ℚ)) ^ r := by
  simp only [Bd]
  rcases le_or_gt x n with h | h
  · rw [show n + 1 - x = n - x + 1 by omega, Harm_succ]
    push_cast
    ring
  · rw [show n + 1 - x = 0 by omega, show n - x = 0 by omega]
    simp only [Nat.cast_zero, zero_pow hr.ne', div_zero]
    ring

/-! ## 2.  The two weights and the two double sums -/

/-- `α = A₁(k) − A₁(l)`. -/
def alph (n k l : ℕ) : ℚ := Ad 1 n k - Ad 1 n l

/-- `β = B₁(k) − B₁(l)`. -/
def bet (n k l : ℕ) : ℚ := Bd 1 n k - Bd 1 n l

/-- `Ψ = ½α + β`. -/
def psiBZ (n k l : ℕ) : ℚ := (1 / 2) * alph n k l + bet n k l

/-- The weight-3 companion weight `ŵ₃ = H⁽³⁾_{n+k} − Ψ·H⁽²⁾_{n+k}`
(`work/ZETA5_CLOSEDFORM.md` §0; 7 monomials, degree 2, 8 symbols). -/
def w3h (n k l : ℕ) : ℚ := Harm 3 (n + k) - psiBZ n k l * Harm 2 (n + k)

/-- The weight-5 companion weight
`w₅ = H⁽⁵⁾_{n+k} + ½(α−β)H⁽⁴⁾_{n+k} + (¼(A₂(k)+A₂(l)) − ½αΨ)H⁽³⁾_{n+k}`
(`work/ZETA5_CLOSEDFORM.md` §0; 27 monomials, degree 3, 13 symbols). -/
def w5 (n k l : ℕ) : ℚ :=
  Harm 5 (n + k)
    + (1 / 2) * (alph n k l - bet n k l) * Harm 4 (n + k)
    + ((1 / 4) * (Ad 2 n k + Ad 2 n l) - (1 / 2) * alph n k l * psiBZ n k l) * Harm 3 (n + k)

/-- The `P̂`-row double sum `Σ_{k,l=0}^{n} T(n,k,l)·ŵ₃`.

**Why nested `Finset.sum` and not a sum over `range (n+1) ×ˢ range (n+1)`.**  Three reasons,
all of them are things this file (and its successor, the certificate) actually does:
(i) it matches `ZetaLucas.Q` verbatim, so `Q_eq_sum_range` transports without a reindexing step;
(ii) the telescoping input of §5 is a *pair* `(ρ, σ)` of certificates, one per index, and
`Finset.sum_range_sub` collapses one index at a time — on a product `Finset` each collapse would
need `Finset.sum_product` first;
(iii) `Finset.sum_comm` (used in `Q_lucas`) is stated for nested sums. -/
def PhatSum (n : ℕ) : ℚ := ∑ k ∈ range (n + 1), ∑ l ∈ range (n + 1), (T n k l : ℚ) * w3h n k l

/-- The `P`-row double sum `Σ_{k,l=0}^{n} T(n,k,l)·w₅`. -/
def PSum (n : ℕ) : ℚ := ∑ k ∈ range (n + 1), ∑ l ∈ range (n + 1), (T n k l : ℚ) * w5 n k l

/-- **Range extension.**  For *any* weight `w`, the `T`-weighted double sum may be taken over
any square range containing `range (n+1)`: the summand vanishes as soon as `k > n` or `l > n`,
because `T(n,k,l) = 0` there.  This is the ℚ-valued analogue of `Q_eq_sum_range`. -/
theorem sum_T_eq_sum_range (w : ℕ → ℕ → ℕ → ℚ) {n N : ℕ} (h : n + 1 ≤ N) :
    ∑ k ∈ range (n + 1), ∑ l ∈ range (n + 1), (T n k l : ℚ) * w n k l
      = ∑ k ∈ range N, ∑ l ∈ range N, (T n k l : ℚ) * w n k l := by
  have hsub : range (n + 1) ⊆ range N :=
    fun x hx => Finset.mem_range.2 (lt_of_lt_of_le (Finset.mem_range.1 hx) h)
  have inner : ∀ k, ∑ l ∈ range (n + 1), (T n k l : ℚ) * w n k l
      = ∑ l ∈ range N, (T n k l : ℚ) * w n k l := by
    intro k
    refine Finset.sum_subset hsub ?_
    intro l _ hl
    have : T n k l = 0 :=
      T_eq_zero_of_lt_right (by simpa [Nat.lt_succ_iff, Nat.succ_le_iff] using hl)
    simp [this]
  rw [Finset.sum_congr rfl fun k _ => inner k]
  refine Finset.sum_subset hsub ?_
  intro k _ hk
  refine Finset.sum_eq_zero fun l _ => ?_
  have : T n k l = 0 :=
    T_eq_zero_of_lt_left (by simpa [Nat.lt_succ_iff, Nat.succ_le_iff] using hk)
  simp [this]

theorem PhatSum_eq_sum_range {n N : ℕ} (h : n + 1 ≤ N) :
    PhatSum n = ∑ k ∈ range N, ∑ l ∈ range N, (T n k l : ℚ) * w3h n k l :=
  sum_T_eq_sum_range w3h h

theorem PSum_eq_sum_range {n N : ℕ} (h : n + 1 ≤ N) :
    PSum n = ∑ k ∈ range N, ∑ l ∈ range N, (T n k l : ℚ) * w5 n k l :=
  sum_T_eq_sum_range w5 h

/-! ### 2.1  "Lemma 0" for `T` — the three absorption identities

The Brown–Zudilin analogue of `MinimalForm.l0a`–`l0d`.  Every one of them is a
**division-free identity in ℚ valid for all `n, k, l ≥ 0`** — no range hypothesis, no `0/0` —
because outside the summation range both sides vanish.  Together with the harmonic shift lemmas
of §1 they turn any WZ certificate for this family into a polynomial identity in `ℚ[n,k,l]`
closable by `ring`; see §5.

In factorial form
`T(n,k,l) = n!·(n+k)!·(n+l)!·(n+k+l)! / ((k!)³(l!)³((n−k)!)²((n−l)!)²(k+l)!)`,
so the three ratios are

    T(n,k+1,l)/T(n,k,l) = (n+k+1)(n−k)²(n+k+l+1) / ((k+1)³(k+l+1))
    T(n,k,l+1)/T(n,k,l) = (n+l+1)(n−l)²(n+k+l+1) / ((l+1)³(k+l+1))
    T(n+1,k,l)/T(n,k,l) = (n+1)(n+k+1)(n+l+1)(n+k+l+1) / ((n+1−k)²(n+1−l)²)

and these lemmas are exactly those three, cleared of denominators. -/

/-- `C(N+1,k+1)·(k+1) = (N+1)·C(N,k)` over ℚ — the "upper-index" absorption that
`MinimalForm.absorb`/`absorb2` do not cover. -/
theorem absorbU (N k : ℕ) :
    (((N + 1).choose (k + 1) : ℕ) : ℚ) * ((k : ℚ) + 1)
      = ((N : ℚ) + 1) * ((N.choose k : ℕ) : ℚ) := by
  have hq := congrArg (fun x : ℕ => (x : ℚ)) (Nat.add_one_mul_choose_eq N k)
  push_cast at hq
  linear_combination -hq

theorem T_cast (n k l : ℕ) :
    (T n k l : ℚ) = ((n + k).choose n : ℚ) * ((n.choose k : ℚ)) ^ 2 * ((n + l).choose n : ℚ)
      * ((n.choose l : ℚ)) ^ 2 * ((n + k + l).choose n : ℚ) := by
  simp only [T]; push_cast; ring

/-- `T` is symmetric in `k` and `l`. -/
theorem T_symm (n k l : ℕ) : T n k l = T n l k := by
  simp only [T, show n + k + l = n + l + k by omega]; ring

/-- **Lemma 0(k)**: `T(n,k+1,l)·(k+1)³(k+l+1) = T(n,k,l)·(n+k+1)(n−k)²(n+k+l+1)`. -/
theorem T_shift_k (n k l : ℕ) :
    (T n (k + 1) l : ℚ) * (((k : ℚ) + 1) ^ 3 * ((k : ℚ) + (l : ℚ) + 1))
      = (T n k l : ℚ) * (((n : ℚ) + k + 1) * ((n : ℚ) - k) ^ 2 * ((n : ℚ) + k + l + 1)) := by
  have e1 : (((n + k + 1).choose n : ℕ) : ℚ) * ((k : ℚ) + 1)
      = ((n : ℚ) + k + 1) * (((n + k).choose n : ℕ) : ℚ) := by
    have h := absorb (n + k) n
    push_cast at h ⊢
    linear_combination h
  have e2 : ((n.choose (k + 1) : ℕ) : ℚ) * ((k : ℚ) + 1)
      = ((n.choose k : ℕ) : ℚ) * ((n : ℚ) - k) := absorb2 n k
  have e3 : (((n + k + l + 1).choose n : ℕ) : ℚ) * ((k : ℚ) + (l : ℚ) + 1)
      = ((n : ℚ) + k + l + 1) * (((n + k + l).choose n : ℕ) : ℚ) := by
    have h := absorb (n + k + l) n
    push_cast at h ⊢
    linear_combination h
  rw [T_cast, T_cast, show n + (k + 1) = n + k + 1 by omega,
    show n + k + 1 + l = n + k + l + 1 by omega]
  calc (((n + k + 1).choose n : ℕ) : ℚ) * ((n.choose (k + 1) : ℕ) : ℚ) ^ 2
        * (((n + l).choose n : ℕ) : ℚ) * ((n.choose l : ℕ) : ℚ) ^ 2
        * (((n + k + l + 1).choose n : ℕ) : ℚ) * (((k : ℚ) + 1) ^ 3 * ((k : ℚ) + (l : ℚ) + 1))
      = ((((n + k + 1).choose n : ℕ) : ℚ) * ((k : ℚ) + 1))
        * (((n.choose (k + 1) : ℕ) : ℚ) * ((k : ℚ) + 1)) ^ 2
        * (((n + l).choose n : ℕ) : ℚ) * ((n.choose l : ℕ) : ℚ) ^ 2
        * ((((n + k + l + 1).choose n : ℕ) : ℚ) * ((k : ℚ) + (l : ℚ) + 1)) := by ring
    _ = (((n : ℚ) + k + 1) * (((n + k).choose n : ℕ) : ℚ))
        * (((n.choose k : ℕ) : ℚ) * ((n : ℚ) - k)) ^ 2
        * (((n + l).choose n : ℕ) : ℚ) * ((n.choose l : ℕ) : ℚ) ^ 2
        * (((n : ℚ) + k + l + 1) * (((n + k + l).choose n : ℕ) : ℚ)) := by rw [e1, e2, e3]
    _ = _ := by ring

/-- **Lemma 0(l)**: `T(n,k,l+1)·(l+1)³(k+l+1) = T(n,k,l)·(n+l+1)(n−l)²(n+k+l+1)`. -/
theorem T_shift_l (n k l : ℕ) :
    (T n k (l + 1) : ℚ) * (((l : ℚ) + 1) ^ 3 * ((k : ℚ) + (l : ℚ) + 1))
      = (T n k l : ℚ) * (((n : ℚ) + l + 1) * ((n : ℚ) - l) ^ 2 * ((n : ℚ) + k + l + 1)) := by
  have h := T_shift_k n l k
  rw [T_symm n (l + 1) k, T_symm n l k] at h
  linear_combination h

/-- **Lemma 0(n)**: `T(n+1,k,l)·(n+1−k)²(n+1−l)² = T(n,k,l)·(n+1)(n+k+1)(n+l+1)(n+k+l+1)`. -/
theorem T_shift_n (n k l : ℕ) :
    (T (n + 1) k l : ℚ) * (((n : ℚ) + 1 - k) ^ 2 * ((n : ℚ) + 1 - l) ^ 2)
      = (T n k l : ℚ)
        * (((n : ℚ) + 1) * ((n : ℚ) + k + 1) * ((n : ℚ) + l + 1) * ((n : ℚ) + k + l + 1)) := by
  have f1 : (((n + k + 1).choose (n + 1) : ℕ) : ℚ) * ((n : ℚ) + 1)
      = ((n : ℚ) + k + 1) * (((n + k).choose n : ℕ) : ℚ) := by
    have h := absorbU (n + k) n
    push_cast at h ⊢
    linear_combination h
  have f2 : (((n + 1).choose k : ℕ) : ℚ) * ((n : ℚ) + 1 - k)
      = ((n : ℚ) + 1) * ((n.choose k : ℕ) : ℚ) := absorb n k
  have f3 : (((n + l + 1).choose (n + 1) : ℕ) : ℚ) * ((n : ℚ) + 1)
      = ((n : ℚ) + l + 1) * (((n + l).choose n : ℕ) : ℚ) := by
    have h := absorbU (n + l) n
    push_cast at h ⊢
    linear_combination h
  have f4 : (((n + 1).choose l : ℕ) : ℚ) * ((n : ℚ) + 1 - l)
      = ((n : ℚ) + 1) * ((n.choose l : ℕ) : ℚ) := absorb n l
  have f5 : (((n + k + l + 1).choose (n + 1) : ℕ) : ℚ) * ((n : ℚ) + 1)
      = ((n : ℚ) + k + l + 1) * (((n + k + l).choose n : ℕ) : ℚ) := by
    have h := absorbU (n + k + l) n
    push_cast at h ⊢
    linear_combination h
  have hne : ((n : ℚ) + 1) ^ 3 ≠ 0 := by positivity
  refine mul_right_cancel₀ hne ?_
  rw [T_cast, T_cast, show n + 1 + k = n + k + 1 by omega, show n + 1 + l = n + l + 1 by omega,
    show n + k + 1 + l = n + k + l + 1 by omega]
  calc (((n + k + 1).choose (n + 1) : ℕ) : ℚ) * (((n + 1).choose k : ℕ) : ℚ) ^ 2
        * (((n + l + 1).choose (n + 1) : ℕ) : ℚ) * (((n + 1).choose l : ℕ) : ℚ) ^ 2
        * (((n + k + l + 1).choose (n + 1) : ℕ) : ℚ)
        * (((n : ℚ) + 1 - k) ^ 2 * ((n : ℚ) + 1 - l) ^ 2) * ((n : ℚ) + 1) ^ 3
      = ((((n + k + 1).choose (n + 1) : ℕ) : ℚ) * ((n : ℚ) + 1))
        * ((((n + 1).choose k : ℕ) : ℚ) * ((n : ℚ) + 1 - k)) ^ 2
        * ((((n + l + 1).choose (n + 1) : ℕ) : ℚ) * ((n : ℚ) + 1))
        * ((((n + 1).choose l : ℕ) : ℚ) * ((n : ℚ) + 1 - l)) ^ 2
        * ((((n + k + l + 1).choose (n + 1) : ℕ) : ℚ) * ((n : ℚ) + 1)) := by ring
    _ = (((n : ℚ) + k + 1) * (((n + k).choose n : ℕ) : ℚ))
        * (((n : ℚ) + 1) * ((n.choose k : ℕ) : ℚ)) ^ 2
        * (((n : ℚ) + l + 1) * (((n + l).choose n : ℕ) : ℚ))
        * (((n : ℚ) + 1) * ((n.choose l : ℕ) : ℚ)) ^ 2
        * (((n : ℚ) + k + l + 1) * (((n + k + l).choose n : ℕ) : ℚ)) := by rw [f1, f2, f3, f4, f5]
    _ = _ := by ring

/-- Chaining two one-step absorption identities (kept in this cascaded shape on purpose: it
makes the `ring` calls small — the fully expanded form is degree 24 and costs ~50 s). -/
theorem absorb_chain {a b c A B C D : ℚ} (h1 : b * A = a * B) (h2 : c * C = b * D) :
    c * (C * A) = a * (B * D) := by
  calc c * (C * A) = (c * C) * A := by ring
    _ = (b * D) * A := by rw [h2]
    _ = (b * A) * D := by ring
    _ = (a * B) * D := by rw [h1]
    _ = a * (B * D) := by ring

/-- **Lemma 0(n²)** — the two-step `n`-shift, obtained by composing `T_shift_n` with itself.
`L_BZ` is order 3, so the reduction lemma needs `T(n+i,k,l)` for `i = 0,1,2,3` expressed over the
common base `T(n,k,l)`; this and `T_shift_n3` are those two remaining cases. -/
theorem T_shift_n2 (n k l : ℕ) :
    (T (n + 2) k l : ℚ)
        * ((((n : ℚ) + 2 - k) ^ 2 * ((n : ℚ) + 2 - l) ^ 2)
           * (((n : ℚ) + 1 - k) ^ 2 * ((n : ℚ) + 1 - l) ^ 2))
      = (T n k l : ℚ)
        * ((((n : ℚ) + 1) * ((n : ℚ) + k + 1) * ((n : ℚ) + l + 1) * ((n : ℚ) + k + l + 1))
           * (((n : ℚ) + 2) * ((n : ℚ) + k + 2) * ((n : ℚ) + l + 2) * ((n : ℚ) + k + l + 2))) := by
  have h1 := T_shift_n n k l
  have h2 := T_shift_n (n + 1) k l
  rw [show n + 1 + 1 = n + 2 by omega] at h2
  push_cast at h2
  refine absorb_chain h1 ?_
  linear_combination h2

/-- **Lemma 0(n³)** — the three-step `n`-shift. -/
theorem T_shift_n3 (n k l : ℕ) :
    (T (n + 3) k l : ℚ)
        * ((((n : ℚ) + 3 - k) ^ 2 * ((n : ℚ) + 3 - l) ^ 2)
           * ((((n : ℚ) + 2 - k) ^ 2 * ((n : ℚ) + 2 - l) ^ 2)
              * (((n : ℚ) + 1 - k) ^ 2 * ((n : ℚ) + 1 - l) ^ 2)))
      = (T n k l : ℚ)
        * (((((n : ℚ) + 1) * ((n : ℚ) + k + 1) * ((n : ℚ) + l + 1) * ((n : ℚ) + k + l + 1))
            * (((n : ℚ) + 2) * ((n : ℚ) + k + 2) * ((n : ℚ) + l + 2) * ((n : ℚ) + k + l + 2)))
           * (((n : ℚ) + 3) * ((n : ℚ) + k + 3) * ((n : ℚ) + l + 3) * ((n : ℚ) + k + l + 3))) := by
  have h1 := T_shift_n2 n k l
  have h2 := T_shift_n (n + 2) k l
  rw [show n + 2 + 1 = n + 3 by omega] at h2
  push_cast at h2
  refine absorb_chain h1 ?_
  linear_combination h2

/-! ## 3.  `L_BZ`: the certified order-3 recurrence, and the two companion rows

Verbatim from `work/lb5/core.py` (V6b normalised).  All four coefficients have degree 9 in `n`;
`L_BZ` annihilates `Q`, `P̂` and `P` simultaneously
(`work/PHASE2_CERTS.md` §§ "minimal recurrence … (order 3, degree 9), nullity 1"). -/

/-- `a₀(x) = 41218x³ + 198849x² + 320790x + 173057`. -/
def a0P (x : ℚ) : ℚ := 41218 * x ^ 3 + 198849 * x ^ 2 + 320790 * x + 173057

/-- `B₈(x)`, the degree-8 factor of `c₁`. -/
def B8P (x : ℚ) : ℚ :=
  3874492 * x ^ 8 + 59373972 * x ^ 7 + 394148190 * x ^ 6 + 1481084196 * x ^ 5
    + 3447878810 * x ^ 4 + 5095855458 * x ^ 3 + 4673546679 * x ^ 2
    + 2433871008 * x + 551502039

/-- `B₉(x)`, the degree-9 factor of `c₂`. -/
def B9P (x : ℚ) : ℚ :=
  48802112 * x ^ 9 + 967468896 * x ^ 8 + 8488000862 * x ^ 7 + 43246197636 * x ^ 6
    + 140983768422 * x ^ 5 + 304912330849 * x ^ 4 + 437406946975 * x ^ 3
    + 401272692378 * x ^ 2 + 213593890911 * x + 50257929339

/-- `c₀(n) = (n+1)⁵(n+2)·a₀(n+1)`. -/
def cc0 (n : ℕ) : ℚ := ((n : ℚ) + 1) ^ 5 * ((n : ℚ) + 2) * a0P ((n : ℚ) + 1)

/-- `c₁(n) = −2(n+2)·B₈(n)`. -/
def cc1 (n : ℕ) : ℚ := -2 * ((n : ℚ) + 2) * B8P (n : ℚ)

/-- `c₂(n) = −2·B₉(n)`. -/
def cc2 (n : ℕ) : ℚ := -2 * B9P (n : ℚ)

/-- `c₃(n) = 2(n+3)⁵(2n+5)·a₀(n)` — the leading coefficient, positive for all `n ≥ 0`. -/
def cc3 (n : ℕ) : ℚ := 2 * ((n : ℚ) + 3) ^ 5 * (2 * (n : ℚ) + 5) * a0P (n : ℚ)

theorem cc3_pos (n : ℕ) : 0 < cc3 n := by
  have h : (0 : ℚ) ≤ (n : ℚ) := Nat.cast_nonneg n
  simp only [cc3, a0P]
  positivity

theorem cc3_ne (n : ℕ) : cc3 n ≠ 0 := (cc3_pos n).ne'

/-- **`L_BZ`.**  `Y` is annihilated by the certified Brown–Zudilin order-3 operator:

    c₀(n)·Y_n + c₁(n)·Y_{n+1} + c₂(n)·Y_{n+2} + c₃(n)·Y_{n+3} = 0   for all n ≥ 0. -/
def BZRec (Y : ℕ → ℚ) : Prop :=
  ∀ n : ℕ, cc0 n * Y n + cc1 n * Y (n + 1) + cc2 n * Y (n + 2) + cc3 n * Y (n + 3) = 0

/-- **The `P̂` row**, defined by `L_BZ` with `P̂₀ = 0`, `P̂₁ = 101/4`, `P̂₂ = 344923/96`
(exact ladder values, `work/lb5/core.py`). -/
def Phat : ℕ → ℚ
  | 0 => 0
  | 1 => 101 / 4
  | 2 => 344923 / 96
  | (n + 3) => -(cc0 n * Phat n + cc1 n * Phat (n + 1) + cc2 n * Phat (n + 2)) / cc3 n

/-- **The `P` row**, defined by `L_BZ` with `P₀ = 0`, `P₁ = 87/4`, `P₂ = 1190161/384`. -/
def PBZ : ℕ → ℚ
  | 0 => 0
  | 1 => 87 / 4
  | 2 => 1190161 / 384
  | (n + 3) => -(cc0 n * PBZ n + cc1 n * PBZ (n + 1) + cc2 n * PBZ (n + 2)) / cc3 n

@[simp] theorem Phat_zero : Phat 0 = 0 := rfl
@[simp] theorem Phat_one : Phat 1 = 101 / 4 := rfl
@[simp] theorem Phat_two : Phat 2 = 344923 / 96 := rfl
@[simp] theorem PBZ_zero : PBZ 0 = 0 := rfl
@[simp] theorem PBZ_one : PBZ 1 = 87 / 4 := rfl
@[simp] theorem PBZ_two : PBZ 2 = 1190161 / 384 := rfl

theorem Phat_bzrec : BZRec Phat := by
  intro n
  have hne := cc3_ne n
  have h : Phat (n + 3)
      = -(cc0 n * Phat n + cc1 n * Phat (n + 1) + cc2 n * Phat (n + 2)) / cc3 n := rfl
  rw [h]
  field_simp
  ring

theorem PBZ_bzrec : BZRec PBZ := by
  intro n
  have hne := cc3_ne n
  have h : PBZ (n + 3)
      = -(cc0 n * PBZ n + cc1 n * PBZ (n + 1) + cc2 n * PBZ (n + 2)) / cc3 n := rfl
  rw [h]
  field_simp
  ring

/-! ### 3.1  Sanity checks — kernel-verified against the exact ladders

These are the analogue of `MinimalForm.lean`'s `example : bApery 2 = 351/4`: they are the check
that catches a mis-transcribed degree-9 coefficient *before* it poisons the induction.  The
target values are the exact ladder entries of `work/lb5` (`ladder_Q/P/Ph.json`), reproduced in
`work/ZETA5_CLOSEDFORM.md`. -/

section Sanity

set_option maxRecDepth 40000

private theorem ch42 : Nat.choose 4 2 = 6 := rfl
private theorem ch52 : Nat.choose 5 2 = 10 := rfl
private theorem ch62 : Nat.choose 6 2 = 15 := rfl

/-- Kernel-checked: `L_BZ` reproduces `P̂₃ = 3710571371/4320` and `P̂₄ = 602417685937/2304`. -/
example : Phat 3 = 3710571371 / 4320 := by
  norm_num [Phat, cc0, cc1, cc2, cc3, a0P, B8P, B9P]

example : Phat 4 = 602417685937 / 2304 := by
  norm_num [Phat, cc0, cc1, cc2, cc3, a0P, B8P, B9P]

/-- Kernel-checked: `L_BZ` reproduces `P₃ = 7682021239/10368` and `P₄ = 24943788950905/110592`. -/
example : PBZ 3 = 7682021239 / 10368 := by
  norm_num [PBZ, cc0, cc1, cc2, cc3, a0P, B8P, B9P]

example : PBZ 4 = 24943788950905 / 110592 := by
  norm_num [PBZ, cc0, cc1, cc2, cc3, a0P, B8P, B9P]

/-- **The strongest transcription check**: `L_BZ` annihilates the *independently defined*
integer row `Q` of `ZetaLucas/BrownZudilin.lean` at `n = 0`, i.e.

    c₀(0)·Q₀ + c₁(0)·Q₁ + c₂(0)·Q₂ + c₃(0)·Q₃ = 0,   (Q₀,Q₁,Q₂,Q₃) = (1, 21, 2989, 714549).

`Q` is computed here from the double binomial sum, not from any recurrence, so this pins all
four degree-9 coefficients simultaneously. -/
example : cc0 0 * (Q 0 : ℚ) + cc1 0 * (Q 1 : ℚ) + cc2 0 * (Q 2 : ℚ) + cc3 0 * (Q 3 : ℚ) = 0 := by
  have h0 : Q 0 = 1 := by decide
  have h1 : Q 1 = 21 := by decide
  have h2 : Q 2 = 2989 := by decide
  have h3 : Q 3 = 714549 := by decide
  rw [h0, h1, h2, h3]
  norm_num [cc0, cc1, cc2, cc3, a0P, B8P, B9P]

end Sanity

/-! ### 3.2  Initial values of the two double sums

Computed from the definitions (`T`, `Harm`, the bare letters) — no recurrence involved. -/

section InitialValues

set_option maxRecDepth 40000

theorem PhatSum_zero : PhatSum 0 = 0 := by
  norm_num [PhatSum, w3h, psiBZ, alph, bet, Ad, Bd, Harm, K, triv, T, Finset.sum_range_succ]

theorem PhatSum_one : PhatSum 1 = 101 / 4 := by
  norm_num [PhatSum, w3h, psiBZ, alph, bet, Ad, Bd, Harm, K, triv, T, Finset.sum_range_succ]

theorem PhatSum_two : PhatSum 2 = 344923 / 96 := by
  norm_num [PhatSum, w3h, psiBZ, alph, bet, Ad, Bd, Harm, K, triv, T, Finset.sum_range_succ,
    ch42, ch52, ch62]

theorem PSum_zero : PSum 0 = 0 := by
  norm_num [PSum, w5, psiBZ, alph, bet, Ad, Bd, Harm, K, triv, T, Finset.sum_range_succ]

theorem PSum_one : PSum 1 = 87 / 4 := by
  norm_num [PSum, w5, psiBZ, alph, bet, Ad, Bd, Harm, K, triv, T, Finset.sum_range_succ]

theorem PSum_two : PSum 2 = 1190161 / 384 := by
  norm_num [PSum, w5, psiBZ, alph, bet, Ad, Bd, Harm, K, triv, T, Finset.sum_range_succ,
    ch42, ch52, ch62]

private theorem ch43 : Nat.choose 4 3 = 4 := rfl
private theorem ch53 : Nat.choose 5 3 = 10 := rfl
private theorem ch63 : Nat.choose 6 3 = 20 := rfl
private theorem ch73 : Nat.choose 7 3 = 35 := rfl
private theorem ch83 : Nat.choose 8 3 = 56 := rfl
private theorem ch93 : Nat.choose 9 3 = 84 := rfl

/-- The first value **not** used as an initial condition: computed from the double sum alone. -/
theorem PhatSum_three : PhatSum 3 = 3710571371 / 4320 := by
  norm_num [PhatSum, w3h, psiBZ, alph, bet, Ad, Bd, Harm, K, triv, T, Finset.sum_range_succ,
    ch43, ch53, ch63, ch73, ch83, ch93]

theorem PSum_three : PSum 3 = 7682021239 / 10368 := by
  norm_num [PSum, w5, psiBZ, alph, bet, Ad, Bd, Harm, K, triv, T, Finset.sum_range_succ,
    ch43, ch53, ch63, ch73, ch83, ch93]

/-- **Kernel-checked instance of the quarantined reduction lemma at `n = 0`.**  All four values
`PhatSum 0..3` are computed from the double sum `Σ_{k,l} T·ŵ₃`; the four coefficients come from
`L_BZ`.  Nothing here uses `Phat` or the recurrence, so this is an independent confirmation of
`bz_creative_telescoping.1 0`. -/
example : cc0 0 * PhatSum 0 + cc1 0 * PhatSum 1 + cc2 0 * PhatSum 2 + cc3 0 * PhatSum 3 = 0 := by
  rw [PhatSum_zero, PhatSum_one, PhatSum_two, PhatSum_three]
  norm_num [cc0, cc1, cc2, cc3, a0P, B8P, B9P]

/-- The same for the weight-5 row: an independent confirmation of
`bz_creative_telescoping.2 0`. -/
example : cc0 0 * PSum 0 + cc1 0 * PSum 1 + cc2 0 * PSum 2 + cc3 0 * PSum 3 = 0 := by
  rw [PSum_zero, PSum_one, PSum_two, PSum_three]
  norm_num [cc0, cc1, cc2, cc3, a0P, B8P, B9P]

end InitialValues

/-! ### 3.3  The two weights, written out in the bare alphabet

These are pure `ring` identities; they are here because they are the statements a reader (or a
certificate-producing CAS) must match:

    Ψ = ½H⁽¹⁾_{n+k} − ½H⁽¹⁾_{n+l} + H⁽¹⁾_{n−k} − H⁽¹⁾_{n−l} − (3/2)H⁽¹⁾_k + (3/2)H⁽¹⁾_l
    α − β = H⁽¹⁾_{n+k} − H⁽¹⁾_{n+l} − H⁽¹⁾_{n−k} + H⁽¹⁾_{n−l}
    A₂(k) + A₂(l) = H⁽²⁾_{n+k} − H⁽²⁾_k + H⁽²⁾_{n+l} − H⁽²⁾_l

so `ŵ₃` has exactly 7 monomials in 8 symbols, and `w₅` exactly 27 in 13. -/

theorem psiBZ_expand (n k l : ℕ) :
    psiBZ n k l = (1 / 2) * Harm 1 (n + k) - (1 / 2) * Harm 1 (n + l)
      + Harm 1 (n - k) - Harm 1 (n - l) - (3 / 2) * Harm 1 k + (3 / 2) * Harm 1 l := by
  simp only [psiBZ, alph, bet, Ad, Bd]
  ring

theorem alph_sub_bet_expand (n k l : ℕ) :
    alph n k l - bet n k l
      = Harm 1 (n + k) - Harm 1 (n + l) - Harm 1 (n - k) + Harm 1 (n - l) := by
  simp only [alph, bet, Ad, Bd]
  ring

theorem Ad2_sum_expand (n k l : ℕ) :
    Ad 2 n k + Ad 2 n l = Harm 2 (n + k) - Harm 2 k + Harm 2 (n + l) - Harm 2 l := by
  simp only [Ad]
  ring

/-- `ŵ₃` in the eight bare symbols. -/
theorem w3h_expand (n k l : ℕ) :
    w3h n k l = Harm 3 (n + k)
      - ((1 / 2) * Harm 1 (n + k) - (1 / 2) * Harm 1 (n + l) + Harm 1 (n - k) - Harm 1 (n - l)
          - (3 / 2) * Harm 1 k + (3 / 2) * Harm 1 l) * Harm 2 (n + k) := by
  rw [w3h, psiBZ_expand]

/-- `w₅` in Horner form over the tower `H^(r)_{n+k}`, with the two lower coefficients expanded. -/
theorem w5_expand (n k l : ℕ) :
    w5 n k l = Harm 5 (n + k)
      + (1 / 2) * (Harm 1 (n + k) - Harm 1 (n + l) - Harm 1 (n - k) + Harm 1 (n - l))
          * Harm 4 (n + k)
      + ((1 / 4) * (Harm 2 (n + k) - Harm 2 k + Harm 2 (n + l) - Harm 2 l)
          - (1 / 2) * alph n k l * psiBZ n k l) * Harm 3 (n + k) := by
  rw [w5, alph_sub_bet_expand, Ad2_sum_expand]

/-! ## 4.  The three-step induction, and the closed forms *conditional on* `L_BZ`

This section is `sorry`-free.  It reduces the whole closed-form theorem to the single
proposition `BZRec PhatSum` (resp. `BZRec PSum`) — that the double sum is annihilated by
`L_BZ` — which is exactly what a creative-telescoping certificate delivers (§5). -/

/-- **Uniqueness for `L_BZ`.**  Two sequences annihilated by the certified order-3 operator with
the same three initial values are equal.  The leading coefficient `c₃(n) = 2(n+3)⁵(2n+5)a₀(n)`
never vanishes for `n ≥ 0` (`cc3_pos`), so the recurrence propagates without obstruction. -/
theorem eq_of_BZRec {Y Z : ℕ → ℚ} (hY : BZRec Y) (hZ : BZRec Z)
    (h0 : Y 0 = Z 0) (h1 : Y 1 = Z 1) (h2 : Y 2 = Z 2) : ∀ n, Y n = Z n := by
  have key : ∀ n : ℕ, Y n = Z n ∧ Y (n + 1) = Z (n + 1) ∧ Y (n + 2) = Z (n + 2) := by
    intro n
    induction n with
    | zero => exact ⟨h0, h1, h2⟩
    | succ m ih =>
      obtain ⟨a, b, c⟩ := ih
      refine ⟨b, ?_, ?_⟩
      · rw [show m + 1 + 1 = m + 2 by omega]; exact c
      · rw [show m + 1 + 2 = m + 3 by omega]
        have hy := hY m
        have hz := hZ m
        have hstep : cc3 m * Y (m + 3) = cc3 m * Z (m + 3) := by
          linear_combination hy - hz - cc0 m * a - cc1 m * b - cc2 m * c
        exact mul_left_cancel₀ (cc3_ne m) hstep
  exact fun n => (key n).1

/-- **Conditional closed form for the `P̂` row.**  If the `ŵ₃`-double sum is annihilated by
`L_BZ`, then it *is* the Brown–Zudilin `P̂` row. -/
theorem PhatSum_eq_Phat_of_rec (h : BZRec PhatSum) (n : ℕ) : PhatSum n = Phat n :=
  eq_of_BZRec h Phat_bzrec
    (by rw [PhatSum_zero, Phat_zero]) (by rw [PhatSum_one, Phat_one])
    (by rw [PhatSum_two, Phat_two]) n

/-- **Conditional closed form for the `P` row.** -/
theorem PSum_eq_PBZ_of_rec (h : BZRec PSum) (n : ℕ) : PSum n = PBZ n :=
  eq_of_BZRec h PBZ_bzrec
    (by rw [PSum_zero, PBZ_zero]) (by rw [PSum_one, PBZ_one])
    (by rw [PSum_two, PBZ_two]) n

/-! ## 5.  ⚠ THE SINGLE QUARANTINED `sorry` ⚠

**Everything in this file outside this section is complete.**  The one open input is the
creative-telescoping reduction below.  It says exactly this: the two double sums are annihilated
by the certified order-3 Brown–Zudilin operator.

`[VERIFIED numerically, NOT formalized]`  `work/z5cf/final_forms.py` checks
`L_BZ·(Σ T·ŵ₃) = L_BZ·(Σ T·w₅) = 0` **exactly over ℚ for n = 0 … 31**, and
`work/z5cf/verify_full.py` checks the closed forms against every exact ladder value
`n = 0 … 360` at two primes (722 checks per form), with zero discrepancies.

**What discharges it** — see `work/LEAN_Z5_SCAFFOLD.md` §S5 for the full interface spec.  A WZ
pair `(ρ, σ)` with

    Σ_{i=0}^{3} c_i(n)·T(n+i,k,l)·w(n+i,k,l)  =  Δ_k( ρ·T·w )  +  Δ_l( σ·T·w )

together with the boundary vanishing `ρ|_{k=0} = ρ|_{k=n+4} = 0`, `σ|_{l=0} = σ|_{l=n+4} = 0`,
turns `PhatSum_eq_sum_range`/`PSum_eq_sum_range` at `N = n+4` plus two applications of
`Finset.sum_range_sub` into a proof.  The two ingredients that make each step a `ring` identity
are already here: **§2.1** (`T_shift_k`, `T_shift_l`, `T_shift_n`) for the binomial part and
**§1** (`Ad_succ_arg`, `Ad_succ_n`, `Bd_succ_arg`, `Bd_succ_n`, `Harm_succ`) for the harmonic
part.  Nothing else in this file changes. -/

section QuarantinedReductionLemma

/-- ## ⚠ THE ONLY `sorry` IN THIS DEVELOPMENT ⚠

**`bz_creative_telescoping`** — the reduction lemma.  Both Brown–Zudilin companion double sums
are annihilated by the certified order-3 operator `L_BZ`:

    ∀ n,  c₀(n)·Σ_{k,l}T(n,k,l)w(n,k,l) + c₁(n)·Σ_{k,l}T(n+1,k,l)w(n+1,k,l)
        + c₂(n)·Σ_{k,l}T(n+2,k,l)w(n+2,k,l) + c₃(n)·Σ_{k,l}T(n+3,k,l)w(n+3,k,l) = 0

for `w = ŵ₃` and for `w = w₅`.  Verified exactly over ℚ for `n = 0…31`; awaiting the WZ pair. -/
theorem bz_creative_telescoping : BZRec PhatSum ∧ BZRec PSum := by
  sorry

end QuarantinedReductionLemma

/-! ## 6.  The closed forms -/

/-- **MAIN THEOREM (weight 3).**  `P̂_n = Σ_{k,l=0}^{n} T(n,k,l)·(H⁽³⁾_{n+k} − Ψ·H⁽²⁾_{n+k})`,
where `P̂` is the Brown–Zudilin companion row defined by `L_BZ` with `P̂₀ = 0`, `P̂₁ = 101/4`,
`P̂₂ = 344923/96`. -/
theorem PhatSum_eq_Phat (n : ℕ) : PhatSum n = Phat n :=
  PhatSum_eq_Phat_of_rec bz_creative_telescoping.1 n

/-- **MAIN THEOREM (weight 5).**
`P_n = Σ_{k,l=0}^{n} T(n,k,l)·(H⁽⁵⁾_{n+k} + ½(α−β)H⁽⁴⁾_{n+k} + (¼(A₂(k)+A₂(l)) − ½αΨ)H⁽³⁾_{n+k})`,
where `P` is defined by `L_BZ` with `P₀ = 0`, `P₁ = 87/4`, `P₂ = 1190161/384`. -/
theorem PSum_eq_PBZ (n : ℕ) : PSum n = PBZ n :=
  PSum_eq_PBZ_of_rec bz_creative_telescoping.2 n

/-- **MAIN THEOREM (weight 3), fully written out** — every definition of this file expanded,
`H^(r)_y = Σ_{j=1}^{y} 1/jʳ`.  Compare `MinimalForm.apery_b_harmonic_closed_form`. -/
theorem BZ_Phat_closed_form_explicit (n : ℕ) :
    ∑ k ∈ range (n + 1), ∑ l ∈ range (n + 1),
        (((n + k).choose n * (n.choose k) ^ 2 * ((n + l).choose n) * (n.choose l) ^ 2
            * ((n + k + l).choose n) : ℕ) : ℚ)
          * ((∑ j ∈ Finset.Icc 1 (n + k), (1 : ℚ) / (j : ℚ) ^ 3)
              - ((1 / 2) * (∑ j ∈ Finset.Icc 1 (n + k), (1 : ℚ) / (j : ℚ))
                  - (1 / 2) * (∑ j ∈ Finset.Icc 1 (n + l), (1 : ℚ) / (j : ℚ))
                  + (∑ j ∈ Finset.Icc 1 (n - k), (1 : ℚ) / (j : ℚ))
                  - (∑ j ∈ Finset.Icc 1 (n - l), (1 : ℚ) / (j : ℚ))
                  - (3 / 2) * (∑ j ∈ Finset.Icc 1 k, (1 : ℚ) / (j : ℚ))
                  + (3 / 2) * (∑ j ∈ Finset.Icc 1 l, (1 : ℚ) / (j : ℚ)))
                * (∑ j ∈ Finset.Icc 1 (n + k), (1 : ℚ) / (j : ℚ) ^ 2))
      = Phat n := by
  rw [← PhatSum_eq_Phat, PhatSum]
  refine Finset.sum_congr rfl fun k _ => Finset.sum_congr rfl fun l _ => ?_
  rw [w3h_expand]
  simp only [T, Nat.cast_mul, Nat.cast_pow]
  rw [Harm_eq 3 (n + k) (by norm_num), Harm_eq 2 (n + k) (by norm_num),
    Harm_eq 1 (n + k) (by norm_num), Harm_eq 1 (n + l) (by norm_num),
    Harm_eq 1 (n - k) (by norm_num), Harm_eq 1 (n - l) (by norm_num),
    Harm_eq 1 k (by norm_num), Harm_eq 1 l (by norm_num)]
  norm_num

/-! ## 7.  Axiom audit -/

section AxiomAudit

-- Infrastructure: the shift lemmas, the range extension, the recurrence and its sanity, the
-- initial values, the uniqueness induction and the two CONDITIONAL closed forms are all clean
-- (`propext, Classical.choice, Quot.sound` only — no `sorryAx`).
#print axioms Ad_succ_arg
#print axioms Ad_succ_n
#print axioms Bd_succ_arg
#print axioms Bd_succ_n
#print axioms sum_T_eq_sum_range
#print axioms T_shift_k
#print axioms T_shift_l
#print axioms T_shift_n
#print axioms T_shift_n2
#print axioms T_shift_n3
#print axioms T_symm
#print axioms cc3_pos
#print axioms Phat_bzrec
#print axioms PBZ_bzrec
#print axioms PhatSum_zero
#print axioms PhatSum_one
#print axioms PhatSum_two
#print axioms PSum_zero
#print axioms PSum_one
#print axioms PSum_two
#print axioms w3h_expand
#print axioms w5_expand
#print axioms eq_of_BZRec
#print axioms PhatSum_eq_Phat_of_rec
#print axioms PSum_eq_PBZ_of_rec

-- The quarantined lemma and its two consequences depend on `sorryAx`, as flagged.
#print axioms bz_creative_telescoping
#print axioms PhatSum_eq_Phat
#print axioms PSum_eq_PBZ

end AxiomAudit

-- `P̂ = 0, 101/4, 344923/96, 3710571371/4320, 602417685937/2304, …`
-- `P  = 0, 87/4, 1190161/384, 7682021239/10368, 24943788950905/110592, …`
#eval (List.range 5).map Phat
#eval (List.range 5).map PBZ
#eval (List.range 4).map PhatSum
#eval (List.range 4).map PSum

end BZCF

end ZetaLucas
