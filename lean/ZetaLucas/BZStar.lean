/-
# `w★`: the order-3 representative of the Brown–Zudilin `P̂` row

**Source of the statement.**  `work/Z5CF_REP.md` §0.  With
`T(n,k,l) = C(n+k,n)C(n,k)²C(n+l,n)C(n,l)²C(n+k+l,n)` and the *bare* harmonic letters
`H^(r)_x = Σ_{m=1}^{x} 1/mʳ` (`ZetaLucas.Harm`), put

    U  =  H_k − ½( H_{n−k} + H_n + H_{n+k+l} − H_{n+l} )
    V  = −½( H_k + H_l − H_{n−k} − H_n + H_{n+k} − H_{n+k+l} )
    w★ =  H⁽³⁾_k + U·( H⁽²⁾_k + H⁽²⁾_n + H⁽²⁾_{n+k} − H⁽²⁾_{n−l} ) + V·( H⁽²⁾_l − H⁽²⁾_k ).

Then `Σ_{k,l=0}^{n} T(n,k,l)·w★(n,k,l) = P̂_n`, and — this is the point of `Z5CF_REP` —
the **order-3** operator `L_BZ` already in `BZClosedForm.lean` is a telescoper of `T·w★`,
which it is *not* of `T·ŵ₃`.  So the whole weight-3 closed form now needs one order-3
certificate (42 blocks) instead of an order-7 one.

**What this file is for.**  Everything the certificate will need, built ahead of it:

* §1  the **bare-letter shift table** — `H^(r)` at each of the eight arguments
  `k, l, n, n−k, n−l, n+k, n+l, n+k+l`, differenced in `k`, in `l` and in `n`.  This is the
  `w★` analogue of `BZClosedForm.lean` §1 (`Ad`, `Bd`), but in the *bare* alphabet, which is
  the alphabet `w★` is stated in.  The truncated-`ℕ`-subtraction convention (`1/0 = 0`,
  `n − x = 0` for `x > n`) is kept, and it is load-bearing: `Harm_sub_succ_arg` and
  `Harm_sub_succ_n` hold **for every `x`, with no `x ≤ n` hypothesis**, because at `x ≥ n`
  both sides collapse to the same thing.  A telescoping argument that runs off the end of
  the summation range (which this one must — the ranges go to `n+4`) never needs a boundary
  case.
* §2  `Ustar`, `Vstar`, `wstar`, `PStarSum`, and the range extension.
* §3  the three initial values `PStarSum 0, 1, 2 = 0, 101/4, 344923/96`, computed from the
  definitions — all `eq_of_BZRec` needs.
* §4  `PStarSum_eq_Phat_of_rec`: `BZRec PStarSum → ∀ n, PStarSum n = Phat n`, `sorry`-free.
* §5  **the quarantined `sorry`** `star_creative_telescoping : BZRec PStarSum`, and the
  unconditional closed form that follows from it.  This is the *only* open input; it is what
  the 42-block certificate of `Z5CF_REP` §4 delivers.
* §6  the bridge `PhatSum = PStarSum`.  The obvious cheap route — "`w★ − ŵ₃` is
  `k↔l`-antisymmetric" — is **impossible**, and the proof of that is recorded in the §6 header
  (`W_tel` is σ-stable and linear, so it would force `ŵ₃^sym ∈ W_tel`, which `Z5CF_REP` §3.2
  excludes).  `sum_antisym_zero` is kept because it is true and explains 45 of the 58
  dimensions of the kernel `K`; `PhatSum_eq_PStarSum_of_antisym` is marked shut.  The bridge
  will arrive as an **order-zero divergence certificate** `T·(w★ − ŵ₃) = Δ_k R₀ + Δ_l S₀`,
  whose shape is `DivCert` and which `PhatSum_eq_PStarSum_of_divCert` consumes.  Note that
  none of this is on the critical path: `PStarSum_eq_Phat_of_rec` reaches `Phat` directly.

**Provenance and independent check.**  `w★` is transcribed from `Z5CF_REP.md` §0 and was
re-verified before transcription: `Σ_{k,l≤n} T(n,k,l)·w★(n,k,l) = P̂_n` exactly over `ℚ` for
`n = 0,1,2,3,4` against `0, 101/4, 344923/96, 3710571371/4320, 602417685937/2304`.  The first
three of those are re-proved *inside Lean* in §3.
-/
import ZetaLucas.BZClosedForm

open Finset

namespace ZetaLucas

namespace BZStar

open BZCF

/-! ## 1.  The bare-letter shift table

`Harm r y = H^(r)_y` and `Harm_succ : H^(r)_{y+1} = H^(r)_y + 1/(y+1)ʳ` are the only analytic
input, exactly as in `MinimalForm` and `BZClosedForm` §1.

The eight arguments occurring in `w★` are `k, l, n, n−k, n−l, n+k, n+l, n+k+l`.  Twelve of the
twenty-four differences are `0` and hold **definitionally** (e.g. `H^(r)_k` does not move when
`n ↦ n+1`), so only the twelve nonzero ones are stated. -/

section Letters

variable (r n k l : ℕ)

/-! ### 1.1  The two subtraction letters — no range hypothesis anywhere -/

/-- `H^(r)_{(n+1)−x} = H^(r)_{n−x} + 1/((n+1−x))ʳ`, for **every** `x`.
For `x > n` both correction terms vanish (`1/0ʳ = 0`) and both sides are `H^(r)_0`. -/
theorem Harm_sub_succ_n {r : ℕ} (hr : 0 < r) (n x : ℕ) :
    Harm r (n + 1 - x) = Harm r (n - x) + 1 / (((n + 1 - x : ℕ) : ℚ)) ^ r := by
  rcases le_or_gt x n with h | h
  · rw [show n + 1 - x = n - x + 1 by omega, Harm_succ]
    push_cast [Nat.cast_sub h]
    ring
  · rw [show n + 1 - x = 0 by omega, show n - x = 0 by omega]
    simp only [Nat.cast_zero, zero_pow hr.ne', div_zero]
    ring

/-- `H^(r)_{n−(x+1)} = H^(r)_{n−x} − 1/(n−x)ʳ`, for **every** `x`. -/
theorem Harm_sub_succ_arg {r : ℕ} (hr : 0 < r) (n x : ℕ) :
    Harm r (n - (x + 1)) = Harm r (n - x) - 1 / (((n - x : ℕ) : ℚ)) ^ r := by
  rcases lt_or_ge x n with h | h
  · rw [show n - x = n - (x + 1) + 1 by omega, Harm_succ]
    push_cast
    ring
  · rw [show n - (x + 1) = 0 by omega, show n - x = 0 by omega]
    simp only [Nat.cast_zero, zero_pow hr.ne', div_zero]
    ring

/-! ### 1.2  The additive letters -/

/-- `Δ_k H^(r)_k`  (and `= Δ_n H^(r)_n`, `= Δ_l H^(r)_l` after renaming). -/
theorem Harm_succ_self : Harm r (k + 1) = Harm r k + 1 / ((k : ℚ) + 1) ^ r := Harm_succ r k

/-- `Δ_n H^(r)_{n+k}`. -/
theorem Harm_nk_succ_n : Harm r (n + 1 + k) = Harm r (n + k) + 1 / ((n : ℚ) + k + 1) ^ r := by
  rw [show n + 1 + k = n + k + 1 by omega, Harm_succ]
  push_cast
  ring

/-- `Δ_k H^(r)_{n+k}`. -/
theorem Harm_nk_succ_k : Harm r (n + (k + 1)) = Harm r (n + k) + 1 / ((n : ℚ) + k + 1) ^ r := by
  rw [show n + (k + 1) = n + k + 1 by omega, Harm_succ]
  push_cast
  ring

/-- `Δ_n H^(r)_{n+l}`. -/
theorem Harm_nl_succ_n : Harm r (n + 1 + l) = Harm r (n + l) + 1 / ((n : ℚ) + l + 1) ^ r :=
  Harm_nk_succ_n r n l

/-- `Δ_l H^(r)_{n+l}`. -/
theorem Harm_nl_succ_l : Harm r (n + (l + 1)) = Harm r (n + l) + 1 / ((n : ℚ) + l + 1) ^ r :=
  Harm_nk_succ_k r n l

/-- `Δ_n H^(r)_{n+k+l}`. -/
theorem Harm_nkl_succ_n :
    Harm r (n + 1 + k + l) = Harm r (n + k + l) + 1 / ((n : ℚ) + k + l + 1) ^ r := by
  rw [show n + 1 + k + l = n + k + l + 1 by omega, Harm_succ]
  push_cast
  ring

/-- `Δ_k H^(r)_{n+k+l}`. -/
theorem Harm_nkl_succ_k :
    Harm r (n + (k + 1) + l) = Harm r (n + k + l) + 1 / ((n : ℚ) + k + l + 1) ^ r := by
  rw [show n + (k + 1) + l = n + k + l + 1 by omega, Harm_succ]
  push_cast
  ring

/-- `Δ_l H^(r)_{n+k+l}`. -/
theorem Harm_nkl_succ_l :
    Harm r (n + k + (l + 1)) = Harm r (n + k + l) + 1 / ((n : ℚ) + k + l + 1) ^ r := by
  rw [show n + k + (l + 1) = n + k + l + 1 by omega, Harm_succ]
  push_cast
  ring

/-! ### 1.3  The twelve vanishing differences

These are `rfl` — the argument simply does not mention the shifted variable — and are recorded
so that a certificate script can quote a lemma name for every cell of the table. -/

theorem Harm_k_shift_n : Harm r k = Harm r k := rfl
theorem Harm_k_shift_l : Harm r k = Harm r k := rfl
theorem Harm_l_shift_n : Harm r l = Harm r l := rfl
theorem Harm_l_shift_k : Harm r l = Harm r l := rfl
theorem Harm_n_shift_k : Harm r n = Harm r n := rfl
theorem Harm_n_shift_l : Harm r n = Harm r n := rfl
theorem Harm_nk_shift_l : Harm r (n + k) = Harm r (n + k) := rfl
theorem Harm_nl_shift_k : Harm r (n + l) = Harm r (n + l) := rfl
theorem Harm_nsubk_shift_l : Harm r (n - k) = Harm r (n - k) := rfl
theorem Harm_nsubl_shift_k : Harm r (n - l) = Harm r (n - l) := rfl

end Letters

/-! ## 2.  `w★` and its double sum -/

/-- `U = H_k − ½(H_{n−k} + H_n + H_{n+k+l} − H_{n+l})`  (`Z5CF_REP.md` §0). -/
def Ustar (n k l : ℕ) : ℚ :=
  Harm 1 k - (1 / 2) * (Harm 1 (n - k) + Harm 1 n + Harm 1 (n + k + l) - Harm 1 (n + l))

/-- `V = −½(H_k + H_l − H_{n−k} − H_n + H_{n+k} − H_{n+k+l})`  (`Z5CF_REP.md` §0). -/
def Vstar (n k l : ℕ) : ℚ :=
  -(1 / 2) * (Harm 1 k + Harm 1 l - Harm 1 (n - k) - Harm 1 n + Harm 1 (n + k)
    - Harm 1 (n + k + l))

/-- **`w★`** `= H⁽³⁾_k + U·(H⁽²⁾_k + H⁽²⁾_n + H⁽²⁾_{n+k} − H⁽²⁾_{n−l}) + V·(H⁽²⁾_l − H⁽²⁾_k)`.
29 monomials in 13 symbols; shift closure `J = 42` (`Z5CF_REP.md` §0.6). -/
def wstar (n k l : ℕ) : ℚ :=
  Harm 3 k
    + Ustar n k l * (Harm 2 k + Harm 2 n + Harm 2 (n + k) - Harm 2 (n - l))
    + Vstar n k l * (Harm 2 l - Harm 2 k)

/-- The `w★` double sum, `Σ_{k,l=0}^{n} T(n,k,l)·w★(n,k,l)`. -/
def PStarSum (n : ℕ) : ℚ := ∑ k ∈ range (n + 1), ∑ l ∈ range (n + 1), (T n k l : ℚ) * wstar n k l

/-- Range extension, from `BZClosedForm.sum_T_eq_sum_range` at the weight `w★`. -/
theorem PStarSum_eq_sum_range {n N : ℕ} (h : n + 1 ≤ N) :
    PStarSum n = ∑ k ∈ range N, ∑ l ∈ range N, (T n k l : ℚ) * wstar n k l :=
  sum_T_eq_sum_range wstar h

/-! ## 3.  The three initial values, computed from the definitions

These are what `eq_of_BZRec` needs, and they are the check that catches a mis-transcribed
letter in `w★` before it poisons anything.  Target values: the exact ladder entries
`P̂ = 0, 101/4, 344923/96` (`work/lb5`, quoted in `BZClosedForm.lean` §3). -/

section InitialValues

set_option maxRecDepth 40000

private theorem ch42 : Nat.choose 4 2 = 6 := rfl
private theorem ch52 : Nat.choose 5 2 = 10 := rfl
private theorem ch62 : Nat.choose 6 2 = 15 := rfl

theorem PStarSum_zero : PStarSum 0 = 0 := by
  norm_num [PStarSum, wstar, Ustar, Vstar, Harm, K, triv, T, Finset.sum_range_succ]

theorem PStarSum_one : PStarSum 1 = 101 / 4 := by
  norm_num [PStarSum, wstar, Ustar, Vstar, Harm, K, triv, T, Finset.sum_range_succ]

theorem PStarSum_two : PStarSum 2 = 344923 / 96 := by
  norm_num [PStarSum, wstar, Ustar, Vstar, Harm, K, triv, T, Finset.sum_range_succ,
    ch42, ch52, ch62]

end InitialValues

/-! ## 4.  The closed form, *conditional* on the reduction — `sorry`-free -/

/-- **Conditional closed form.**  If the `w★` double sum is annihilated by `L_BZ`, then it *is*
the Brown–Zudilin `P̂` row.  Uses `BZClosedForm.eq_of_BZRec`, whose only input is
`cc3_pos`. -/
theorem PStarSum_eq_Phat_of_rec (h : BZRec PStarSum) (n : ℕ) : PStarSum n = Phat n :=
  eq_of_BZRec h Phat_bzrec
    (by rw [PStarSum_zero, Phat_zero]) (by rw [PStarSum_one, Phat_one])
    (by rw [PStarSum_two, Phat_two]) n

/-! ## 5.  ⚠ THE QUARANTINED `sorry` ⚠

**Everything in this file outside this section is complete.**  The one open input is the
creative-telescoping reduction for `w★`.

`[VERIFIED numerically, NOT formalized]`  `work/Z5CF_REP.md` §0 checks
`Σ_{k,l≤n} T·w★ = P̂_n` exactly over `ℚ` for `n = 0…20` (every cell) and
`L_BZ·(Σ T·w★) = 0` exactly over `ℚ` for `n = 0…17`; the 42-block order-3 certificate is
verified at 218 000 fresh-point identities over two primes with zero violations.  What is
missing is only its **lift from `mod p` at fixed numeric `n` to `ℤ[n,k,l]`**
(`Z5CF_REP.md` §6.1) and the transcription of the resulting 42 cleared identities.

**What discharges it.**  Exactly the shape of `LEAN_Z5_SCAFFOLD` §5.5: a WZ pair `(ρ_j, σ_j)`,
`j = 1…42`, over the pole-free base `Φ₃ = T(n+3,·,·)/P₃`, with the boundary vanishing
`ρ|_{k=0} = ρ|_{k=n+4} = 0`, `σ|_{l=0} = σ|_{l=n+4} = 0`.  §1 above supplies every letter
shift it needs; `BZClosedForm` §2.1 supplies `T_shift_k`, `T_shift_l`, `T_shift_n`,
`T_shift_n2`, `T_shift_n3`; and `ZetaLucas.BZQRow` supplies the worked template
(`F0`–`F2`, `Fk`, `Fl`, the positivity of every denominator, `star`, and the double
telescope) on the `J = 1` row.

⚠ **Read `work/LEAN_QROW.md` §4 before transcribing anything.**  The Q row's *single* cleared
identity (3798 monomials, degrees `(27,11,13)`) **cannot be checked by Mathlib's `ring`** on a
15 GB machine, in any arrangement tried.  42 blocks of comparable size will not fit either;
the fix is a reflective polynomial-identity checker (`LEAN_QROW.md` §7), not more `ring`
engineering. -/

section QuarantinedReduction

/-- ## ⚠ QUARANTINED `sorry` ⚠  — the `w★` reduction lemma.

    ∀ n, c₀(n)·Σ T·w★|_n + c₁(n)·Σ T·w★|_{n+1} + c₂(n)·Σ T·w★|_{n+2} + c₃(n)·Σ T·w★|_{n+3} = 0

Verified exactly over `ℚ` for `n = 0…17` (`work/Z5CF_REP.md` §0); awaiting the ℤ[n,k,l] lift of
the 42-block certificate. -/
theorem star_creative_telescoping : BZRec PStarSum := by
  sorry

end QuarantinedReduction

/-- **The weight-3 closed form via `w★`** — depends on the quarantined lemma. -/
theorem PStarSum_eq_Phat (n : ℕ) : PStarSum n = Phat n :=
  PStarSum_eq_Phat_of_rec star_creative_telescoping n

/-! ## 6.  The bridge `PhatSum = PStarSum`

`T(n,k,l) = T(n,l,k)` (`BZClosedForm.T_symm`), so a `k↔l`-antisymmetric weight is annihilated
by the double sum.  `Z5CF_REP.md` §2 measures the kernel `K` of the sum map as 58-dimensional,
of which **45 dimensions are exactly this antisymmetric subspace** and are proved, not
measured.

⚠ **The obvious cheap bridge — "`w★ − ŵ₃` is antisymmetric" — is IMPOSSIBLE, not merely
unknown.**  Recorded here because a reader will otherwise ask why it was not taken.

> Suppose `w − ŵ₃` is antisymmetric for some admissible `w`; then `sym w = sym ŵ₃ = ŵ₃^sym`.
> The order-3 admissible space `W_tel` is **σ-stable**: if `L_BZ·(T·w) = Δ_k R + Δ_l S` then
> swapping `k ↔ l` and using `T(n,k,l) = T(n,l,k)` gives `L_BZ·(T·wᶜ) = Δ_l Rᶜ + Δ_k Sᶜ`, so
> `wᶜ ∈ W_tel`.  `W_tel` is also linear (`dim W_tel(n) = 37` for `n ≥ 2`, `Z5CF_REP` §3.1),
> hence closed under `sym = ½(1 + σ)`.  So `w ∈ W_tel` would force `ŵ₃^sym ∈ W_tel`.  But
> `Z5CF_REP` §3.2 **excludes** `ŵ₃^sym` at four values of `n` and two primes under a
> calibrated ansatz.  Contradiction. ∎

**Consequence: every successful representative uses a nonzero *symmetric* element of `K`, so
`PhatSum = PStarSum` cannot collapse to one `Finset.sum_comm`.**  `sum_antisym_zero` below is
kept — it is true, cheap and genuinely used to explain 45 of the 58 dimensions of `K` — but
`PhatSum_eq_PStarSum_of_antisym` is **not the route** and is marked so.

The bridge will instead arrive as an **order-zero divergence certificate**
`T·(w★ − ŵ₃) = Δ_k R₀ + Δ_l S₀` with both boundary conditions; `DivCert` below is exactly its
shape, and `PhatSum_eq_PStarSum_of_divCert` consumes it.  One copy of `T` instead of four, so
it should be *smaller* than any order-3 block. -/

/-- A `k↔l`-antisymmetric weight is annihilated by the `T`-weighted double sum. -/
theorem sum_antisym_zero (n : ℕ) (w : ℕ → ℕ → ℕ → ℚ) (hw : ∀ k l, w n k l = -w n l k) :
    ∑ k ∈ range (n + 1), ∑ l ∈ range (n + 1), (T n k l : ℚ) * w n k l = 0 := by
  have hswap : ∀ k l : ℕ, (T n l k : ℚ) * w n l k = -((T n k l : ℚ) * w n k l) := by
    intro k l
    rw [T_symm n l k, hw l k]
    ring
  have h1 : ∑ k ∈ range (n + 1), ∑ l ∈ range (n + 1), (T n k l : ℚ) * w n k l
      = ∑ k ∈ range (n + 1), ∑ l ∈ range (n + 1), (T n l k : ℚ) * w n l k := Finset.sum_comm
  rw [Finset.sum_congr rfl fun k _ => Finset.sum_congr rfl fun l _ => hswap k l] at h1
  simp only [Finset.sum_neg_distrib] at h1
  linarith

/-- ⛔ **NOT THE ROUTE — the hypothesis is unsatisfiable.**  See the impossibility argument in
the section header: `W_tel` is σ-stable and linear, so an antisymmetric `w★ − ŵ₃` would force
`ŵ₃^sym ∈ W_tel`, which `Z5CF_REP` §3.2 excludes.  The statement is retained only because it is
true and one line, and because a successor who rediscovers the idea should find it here already
marked shut.  **Use `PhatSum_eq_PStarSum_of_divCert` instead.** -/
theorem PhatSum_eq_PStarSum_of_antisym
    (h : ∀ n k l : ℕ, wstar n k l - w3h n k l = -(wstar n l k - w3h n l k)) (n : ℕ) :
    PhatSum n = PStarSum n := by
  have hz := sum_antisym_zero n (fun n k l => wstar n k l - w3h n k l) (fun k l => h n k l)
  have e : ∀ k l : ℕ, (T n k l : ℚ) * (wstar n k l - w3h n k l)
      = (T n k l : ℚ) * wstar n k l - (T n k l : ℚ) * w3h n k l := fun k l => mul_sub _ _ _
  rw [Finset.sum_congr rfl fun k _ => Finset.sum_congr rfl fun l _ => e k l] at hz
  simp only [Finset.sum_sub_distrib] at hz
  simp only [PhatSum, PStarSum]
  linarith

/-- **The order-zero divergence certificate for `w★ − ŵ₃`**, in the shape the certificate agent
will deliver it (sparse, expanded over `ℤ`).  `R₀`, `S₀` are the two cofactors; the summand
carries a *single* copy of `T`, so this object is smaller than any order-3 block.

The top boundaries are taken at `k = n+1` and `l = n+1`: `PhatSum` and `PStarSum` are both
summed over `range (n+1)`, and no range extension is needed because the certificate is
order zero. -/
structure DivCert (R0 S0 : ℕ → ℕ → ℕ → ℚ) : Prop where
  /-- `T·(w★ − ŵ₃) = Δ_k R₀ + Δ_l S₀`, for all `n,k,l`. -/
  div : ∀ n k l : ℕ, (T n k l : ℚ) * (wstar n k l - w3h n k l)
          = (R0 n (k + 1) l - R0 n k l) + (S0 n k (l + 1) - S0 n k l)
  /-- `R₀|_{k=0} = 0`. -/
  Rbot : ∀ n l : ℕ, R0 n 0 l = 0
  /-- `R₀|_{k=n+1} = 0`. -/
  Rtop : ∀ n l : ℕ, R0 n (n + 1) l = 0
  /-- `S₀|_{l=0} = 0`. -/
  Sbot : ∀ n k : ℕ, S0 n k 0 = 0
  /-- `S₀|_{l=n+1} = 0`. -/
  Stop : ∀ n k : ℕ, S0 n k (n + 1) = 0

/-- **The bridge to the published compact form.**  An order-zero divergence certificate for
`w★ − ŵ₃` collapses, over the square `0 ≤ k,l ≤ n`, to `PhatSum = PStarSum` — so the `w★` row
*is* the `ŵ₃` row and `BZClosedForm.PhatSum_eq_Phat` follows without
`bz_creative_telescoping`. -/
theorem PhatSum_eq_PStarSum_of_divCert {R0 S0 : ℕ → ℕ → ℕ → ℚ} (h : DivCert R0 S0) (n : ℕ) :
    PhatSum n = PStarSum n := by
  have hz : ∑ k ∈ range (n + 1), ∑ l ∈ range (n + 1),
      (T n k l : ℚ) * (wstar n k l - w3h n k l) = 0 := by
    have inner : ∀ k : ℕ, ∑ l ∈ range (n + 1), (T n k l : ℚ) * (wstar n k l - w3h n k l)
        = (∑ l ∈ range (n + 1), (R0 n (k + 1) l - R0 n k l))
          + (∑ l ∈ range (n + 1), (S0 n k (l + 1) - S0 n k l)) := by
      intro k
      rw [← Finset.sum_add_distrib]
      exact Finset.sum_congr rfl fun l _ => h.div n k l
    rw [Finset.sum_congr rfl fun k _ => inner k, Finset.sum_add_distrib]
    have hR : ∑ k ∈ range (n + 1), ∑ l ∈ range (n + 1), (R0 n (k + 1) l - R0 n k l) = 0 := by
      rw [Finset.sum_comm]
      refine Finset.sum_eq_zero fun l _ => ?_
      rw [Finset.sum_range_sub (fun k => R0 n k l) (n + 1), h.Rtop, h.Rbot, sub_zero]
    have hS : ∑ k ∈ range (n + 1), ∑ l ∈ range (n + 1), (S0 n k (l + 1) - S0 n k l) = 0 := by
      refine Finset.sum_eq_zero fun k _ => ?_
      rw [Finset.sum_range_sub (fun l => S0 n k l) (n + 1), h.Stop, h.Sbot, sub_zero]
    rw [hR, hS, add_zero]
  have e : ∀ k l : ℕ, (T n k l : ℚ) * (wstar n k l - w3h n k l)
      = (T n k l : ℚ) * wstar n k l - (T n k l : ℚ) * w3h n k l := fun k l => mul_sub _ _ _
  rw [Finset.sum_congr rfl fun k _ => Finset.sum_congr rfl fun l _ => e k l] at hz
  simp only [Finset.sum_sub_distrib] at hz
  simp only [PhatSum, PStarSum]
  linarith

/-! ## 7.  Axiom audit -/

section AxiomAudit

-- The bare-letter shift table, the weight, the initial values and the conditional closed form
-- are clean: `[propext, Classical.choice, Quot.sound]` only.
#print axioms Harm_sub_succ_n
#print axioms Harm_sub_succ_arg
#print axioms Harm_nk_succ_n
#print axioms Harm_nk_succ_k
#print axioms Harm_nkl_succ_n
#print axioms Harm_nkl_succ_k
#print axioms Harm_nkl_succ_l
#print axioms PStarSum_eq_sum_range
#print axioms PStarSum_zero
#print axioms PStarSum_one
#print axioms PStarSum_two
#print axioms PStarSum_eq_Phat_of_rec
#print axioms sum_antisym_zero
#print axioms PhatSum_eq_PStarSum_of_antisym
#print axioms PhatSum_eq_PStarSum_of_divCert

-- Below the line: the quarantined lemma and its consequence.
#print axioms star_creative_telescoping
#print axioms PStarSum_eq_Phat

end AxiomAudit

-- `Σ T·w★ = 0, 101/4, 344923/96, 3710571371/4320 = P̂_n`, computed from the definitions.
#eval (List.range 4).map PStarSum

end BZStar

end ZetaLucas
