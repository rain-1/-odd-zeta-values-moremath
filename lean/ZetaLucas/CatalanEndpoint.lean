/-
# The Catalan endpoint transform and sharp denominator theorem

This file formalizes the normalized recurrence companion `catalanB` for the "Catalan"
harmonic-jets family (`papers_out/harmonic_jets/main.tex`, Theorem 6.9), its endpoint
binomial transform `catalanT`, the exact transformed recurrence `TREC`, the endpoint
square expansion `TSQ`, the prime-power denominator lemma `RL`, and the resulting sharp
integrality theorem `SHARP`: `Chebyshev.lcmUpto n ^ 2 * catalanB n` is an integer for
every `n`.

**Trust boundary.**  This file formalizes only the *normalized recurrence companion*
`catalanB`, defined by the order-two rational recurrence (REC) below with `B₀ = 0`,
`B₁ = 1`.  It does *not* formalize the identification of `catalanB` with any
harmonic-sum closed form from the Ore certificate machinery elsewhere in the repository;
that connection is left to future work and is not assumed anywhere below.  Every proof
below is closed with no placeholder tactic and no new unproved declaration, and no
theorem quantified over arbitrary `n`/`j`/primes is replaced by finite computation.
-/
import Mathlib

open Finset

namespace ZetaLucas

/-! ## Stage A — the recurrence-defined companion -/

/-- **The normalized Catalan companion**, defined by
`(n+1)² B_{n+1} = (12n²+12n+4) B_n − 32n² B_{n−1}`, `B₀ = 0`, `B₁ = 1`. The leading
coefficient `(n+1)² ≠ 0`, so this determines `B_n ∈ ℚ` uniquely. -/
def catalanB : ℕ → ℚ
  | 0 => 0
  | 1 => 1
  | (n + 2) =>
      ((12 * ((n : ℚ) + 1) ^ 2 + 12 * ((n : ℚ) + 1) + 4) * catalanB (n + 1)
          - 32 * ((n : ℚ) + 1) ^ 2 * catalanB n)
        / ((n : ℚ) + 2) ^ 2

@[simp] theorem catalanB_zero : catalanB 0 = 0 := rfl
@[simp] theorem catalanB_one : catalanB 1 = 1 := rfl

theorem catalanB_rec' (m : ℕ) :
    ((m : ℚ) + 1 + 1) ^ 2 * catalanB (m + 1 + 1)
      = (12 * ((m : ℚ) + 1) ^ 2 + 12 * ((m : ℚ) + 1) + 4) * catalanB (m + 1)
        - 32 * ((m : ℚ) + 1) ^ 2 * catalanB m := by
  have hne : ((m : ℚ) + 2) ^ 2 ≠ 0 := by positivity
  rw [show catalanB (m + 1 + 1)
      = ((12 * ((m : ℚ) + 1) ^ 2 + 12 * ((m : ℚ) + 1) + 4) * catalanB (m + 1)
          - 32 * ((m : ℚ) + 1) ^ 2 * catalanB m)
        / ((m : ℚ) + 2) ^ 2 from rfl]
  field_simp
  ring

theorem catalanB_rec (n : ℕ) (hn : 1 ≤ n) :
    ((n : ℚ) + 1) ^ 2 * catalanB (n + 1)
      = (12 * (n : ℚ) ^ 2 + 12 * (n : ℚ) + 4) * catalanB n - 32 * (n : ℚ) ^ 2 * catalanB (n - 1) := by
  obtain ⟨m, rfl⟩ := Nat.exists_eq_add_of_le hn
  rw [add_comm 1 m]
  have := catalanB_rec' m
  simpa using this

/-- Regression check: the first five values of `catalanB`. -/
theorem catalanB_values :
    catalanB 0 = 0 ∧ catalanB 1 = 1 ∧ catalanB 2 = 7 ∧ catalanB 3 = 404 / 9
      ∧ catalanB 4 = 2603 / 9 := by
  refine ⟨catalanB_zero, catalanB_one, ?_, ?_, ?_⟩
  · show catalanB (0 + 2) = 7
    norm_num [catalanB]
  · show catalanB (1 + 2) = 404 / 9
    norm_num [catalanB]
  · show catalanB (2 + 2) = 2603 / 9
    norm_num [catalanB]

/-- **Recurrence uniqueness.**  Any rational sequence satisfying (REC) from `n ≥ 1` and
agreeing with `catalanB` at `0` and `1` agrees with `catalanB` everywhere. This lets a
future file connect `catalanB` to a harmonic closed form without re-deriving REC. -/
theorem catalanB_unique (f : ℕ → ℚ) (h0 : f 0 = 0) (h1 : f 1 = 1)
    (hrec : ∀ n : ℕ, 1 ≤ n →
      ((n : ℚ) + 1) ^ 2 * f (n + 1)
        = (12 * (n : ℚ) ^ 2 + 12 * (n : ℚ) + 4) * f n - 32 * (n : ℚ) ^ 2 * f (n - 1)) :
    ∀ n, f n = catalanB n := by
  have key : ∀ n : ℕ, f n = catalanB n ∧ f (n + 1) = catalanB (n + 1) := by
    intro n
    induction n with
    | zero => exact ⟨h0, h1⟩
    | succ n ih =>
      refine ⟨ih.2, ?_⟩
      obtain ⟨hn0, hn1⟩ := ih
      have hf := hrec (n + 1) (by omega)
      simp only [Nat.add_sub_cancel] at hf
      have hB := catalanB_rec' n
      have hne : ((n : ℚ) + 1 + 1) ^ 2 ≠ 0 := by positivity
      have heq : ((n : ℚ) + 1 + 1) ^ 2 * f (n + 1 + 1) = ((n : ℚ) + 1 + 1) ^ 2 * catalanB (n + 1 + 1) := by
        rw [hB, ← hn0, ← hn1]
        push_cast at hf ⊢
        linear_combination hf
      exact mul_left_cancel₀ hne heq
  exact fun n => (key n).1

/-! ## Stage B (in progress) — the endpoint binomial transform -/

/-- **The endpoint binomial transform** of `catalanB`. -/
def catalanT (n : ℕ) : ℚ :=
  ∑ k ∈ Finset.range (n + 1), (n.choose k : ℚ) * (-4 : ℚ) ^ (n - k) * catalanB k

@[simp] theorem catalanT_zero : catalanT 0 = 0 := by
  simp [catalanT]

/-- Regression check: the first few values of `catalanT`, computed directly from
`TDEF` and the already-proved values of `catalanB`. These are finite sanity checks only,
not a substitute for the general transformed recurrence `TREC`, which remains open
(see the status log). -/
theorem catalanT_values :
    catalanT 0 = 0 ∧ catalanT 1 = 1 ∧ catalanT 2 = -1 := by
  refine ⟨catalanT_zero, ?_, ?_⟩
  · show catalanT 1 = 1
    simp [catalanT, Finset.sum_range_succ, catalanB]
  · show catalanT 2 = -1
    simp [catalanT, Finset.sum_range_succ, catalanB]
    norm_num [catalanB]

/-- The shifted transform used to expand `catalanT (m+1)` via Pascal's rule:
`V_m = Σ_{j=0}^m C(m,j)(-4)^{m-j} B_{j+1}`. -/
def catalanV (m : ℕ) : ℚ :=
  ∑ j ∈ Finset.range (m + 1), (m.choose j : ℚ) * (-4 : ℚ) ^ (m - j) * catalanB (j + 1)

/-- **Pascal-rule expansion.** `T_{m+1} = -4 T_m + V_m`. This is a fully elementary
finite-sum identity (Pascal's rule alone); it does not yet use `catalanB`'s own
recurrence, so it is *not* `TREC` — it is the first of several such identities needed
to reach it (see the status log). -/
theorem catalanT_succ (m : ℕ) :
    catalanT (m + 1) = (-4 : ℚ) * catalanT m + catalanV m := by
  -- Step 1: peel the k = 0 term of T(m+1)'s defining sum (it vanishes since
  -- `catalanB 0 = 0`), reindexing the rest as a sum over `k ∈ range (m+1)`.
  have hT1 : catalanT (m + 1)
      = ∑ k ∈ Finset.range (m + 1),
          ((m + 1).choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - k) * catalanB (k + 1) := by
    have h := Finset.sum_range_succ'
      (fun k => ((m + 1).choose k : ℚ) * (-4 : ℚ) ^ (m + 1 - k) * catalanB k) (m + 1)
    simp only [catalanT]
    rw [h]
    simp [catalanB_zero]
  rw [hT1]
  -- Step 2: Pascal's rule splits each summand into an `m`-level and `m+1`-level piece.
  have hsplit : ∀ k ∈ Finset.range (m + 1),
      ((m + 1).choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - k) * catalanB (k + 1)
        = (m.choose k : ℚ) * (-4 : ℚ) ^ (m - k) * catalanB (k + 1)
          + (m.choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - k) * catalanB (k + 1) := by
    intro k _
    have hp : (m + 1).choose (k + 1) = m.choose k + m.choose (k + 1) :=
      Nat.choose_succ_succ m k
    have hpq : ((m + 1).choose (k + 1) : ℚ) = (m.choose k : ℚ) + (m.choose (k + 1) : ℚ) := by
      exact_mod_cast hp
    rw [hpq]; ring
  rw [Finset.sum_congr rfl hsplit, Finset.sum_add_distrib]
  have hV : ∑ k ∈ Finset.range (m + 1),
      (m.choose k : ℚ) * (-4 : ℚ) ^ (m - k) * catalanB (k + 1) = catalanV m := rfl
  have hS : ∑ k ∈ Finset.range (m + 1),
      (m.choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - k) * catalanB (k + 1)
        = (-4 : ℚ) * catalanT m := by
    -- Peel the last (vanishing, since `m.choose (m+1) = 0`) term of the LHS sum.
    have hpeel : ∑ k ∈ Finset.range (m + 1),
        (m.choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - k) * catalanB (k + 1)
          = ∑ k ∈ Finset.range m,
              (m.choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - k) * catalanB (k + 1) := by
      rw [Finset.sum_range_succ]
      have hz : (m.choose (m + 1) : ℚ) = 0 := by
        exact_mod_cast Nat.choose_eq_zero_of_lt (by omega)
      rw [hz]; ring
    rw [hpeel]
    -- Expand `catalanT m` by peeling its own k = 0 term.
    have hT0 : catalanT m
        = ∑ k ∈ Finset.range m,
            (m.choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - (k + 1)) * catalanB (k + 1) := by
      have h := Finset.sum_range_succ'
        (fun k => (m.choose k : ℚ) * (-4 : ℚ) ^ (m - k) * catalanB k) m
      simp only [catalanT]
      rw [h]
      simp [catalanB_zero]
    rw [hT0, Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro k hk
    simp only [Finset.mem_range] at hk
    have hexp : m - k = (m - (k + 1)) + 1 := by omega
    rw [hexp, pow_succ]
    ring
  rw [hV, hS]
  ring

/-! ## Stage B, generic shift tower (Ingredient 1 toward TREC, see status log)

`genTr` generalizes `catalanT`/`catalanV` to an arbitrary sequence `a`, and
`genTr_succ` generalizes `catalanT_succ` to arbitrary `a` (no side condition on `a 0`
needed — the boundary terms cancel identically, as `catalanT_succ`'s proof already
hinted). This one lemma instantiates to all of the shift-tower relations
(`V_n = -4V_{n-1}+W_{n-1}`, `W_{n-1} = -4W_{n-2}+Y_{n-2}`, etc.) used in the TREC
elimination certificate recorded in the status log. -/

/-- The endpoint binomial transform of an arbitrary sequence `a`. -/
def genTr (a : ℕ → ℚ) (n : ℕ) : ℚ :=
  ∑ k ∈ Finset.range (n + 1), (n.choose k : ℚ) * (-4 : ℚ) ^ (n - k) * a k

/-- **Generic Pascal-rule shift.** For any `a : ℕ → ℚ`, `genTr a (m+1) = -4·genTr a m + genTr (a∘succ) m`,
with no hypothesis on `a`. This generalizes `catalanT_succ` (the case `a = catalanB`). -/
theorem genTr_succ (a : ℕ → ℚ) (m : ℕ) :
    genTr a (m + 1) = (-4 : ℚ) * genTr a m + genTr (fun k => a (k + 1)) m := by
  have hT1 : genTr a (m + 1)
      = (-4 : ℚ) ^ (m + 1) * a 0 + ∑ k ∈ Finset.range (m + 1),
          ((m + 1).choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - k) * a (k + 1) := by
    have h := Finset.sum_range_succ'
      (fun k => ((m + 1).choose k : ℚ) * (-4 : ℚ) ^ (m + 1 - k) * a k) (m + 1)
    simp only [genTr]
    rw [h]
    simp only [Nat.choose_zero_right, Nat.cast_one, one_mul, Nat.sub_zero]
    rw [add_comm]
    congr 1
    apply Finset.sum_congr rfl
    intro k hk
    simp only [Finset.mem_range] at hk
    have hexp : m + 1 - (k + 1) = m - k := by omega
    rw [hexp]
  rw [hT1]
  have hsplit : ∀ k ∈ Finset.range (m + 1),
      ((m + 1).choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - k) * a (k + 1)
        = (m.choose k : ℚ) * (-4 : ℚ) ^ (m - k) * a (k + 1)
          + (m.choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - k) * a (k + 1) := by
    intro k _
    have hp : (m + 1).choose (k + 1) = m.choose k + m.choose (k + 1) := Nat.choose_succ_succ m k
    have hpq : ((m + 1).choose (k + 1) : ℚ) = (m.choose k : ℚ) + (m.choose (k + 1) : ℚ) := by
      exact_mod_cast hp
    rw [hpq]; ring
  rw [Finset.sum_congr rfl hsplit, Finset.sum_add_distrib]
  have hA : ∑ k ∈ Finset.range (m + 1), (m.choose k : ℚ) * (-4 : ℚ) ^ (m - k) * a (k + 1)
      = genTr (fun k => a (k + 1)) m := rfl
  have hgenTr : genTr a m = (-4 : ℚ) ^ m * a 0
      + ∑ k ∈ Finset.range m, (m.choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - 1 - k) * a (k + 1) := by
    have h := Finset.sum_range_succ' (fun k => (m.choose k : ℚ) * (-4 : ℚ) ^ (m - k) * a k) m
    simp only [genTr]
    rw [h]
    simp only [Nat.choose_zero_right, Nat.cast_one, one_mul, Nat.sub_zero]
    rw [add_comm]
    congr 1
    apply Finset.sum_congr rfl
    intro k hk
    simp only [Finset.mem_range] at hk
    have hexp : m - (k + 1) = m - 1 - k := by omega
    rw [hexp]
  have hB : ∑ k ∈ Finset.range (m + 1), (m.choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - k) * a (k + 1)
      = (-4 : ℚ) * genTr a m - (-4 : ℚ) ^ (m + 1) * a 0 := by
    have hpeel : ∑ k ∈ Finset.range (m + 1), (m.choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - k) * a (k + 1)
        = ∑ k ∈ Finset.range m, (m.choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - k) * a (k + 1) := by
      rw [Finset.sum_range_succ]
      have hz : (m.choose (m + 1) : ℚ) = 0 := by
        exact_mod_cast Nat.choose_eq_zero_of_lt (by omega)
      rw [hz]; ring
    rw [hpeel]
    have hsum_eq : ∑ k ∈ Finset.range m, (m.choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - k) * a (k + 1)
        = (-4 : ℚ) * ∑ k ∈ Finset.range m,
            (m.choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - 1 - k) * a (k + 1) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro k hk
      simp only [Finset.mem_range] at hk
      have hexp : m - k = (m - 1 - k) + 1 := by omega
      rw [hexp, pow_succ]; ring
    rw [hsum_eq]
    have hrepl : ∑ k ∈ Finset.range m, (m.choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - 1 - k) * a (k + 1)
        = genTr a m - (-4 : ℚ) ^ m * a 0 := by
      rw [hgenTr]; ring
    rw [hrepl]; ring
  rw [hA, hB]
  ring

/-! ## Stage B, generating-function ingredient (in progress)

The following lemma is the "negative binomial coefficient" fact needed to connect
`catalanT`'s finite-sum definition (`TDEF`) to the generating-function statement
`T(z) = (1+4z)⁻¹B(z/(1+4z))` from the paper's proof of Theorem 6.9. It is **not**
`TREC` itself and does not use `catalanB` or `catalanT` at all; it is a standalone,
generic fact about `PowerSeries.invOneSubPow`. Status: newly added, not yet verified
to compile (see the status log for the exact verification command and result). -/

open PowerSeries in
/-- For any `c : ℚ`, the coefficients of `X^k * (1 - cX)^{-(k+1)}` are exactly the
endpoint-transform weights `C(n,k) c^{n-k}` (zero when `n < k`). This is the standard
negative-binomial-series fact underlying the binomial transform's generating function;
it is proved directly from `PowerSeries.invOneSubPow_val_succ_eq_mk_add_choose` and
`PowerSeries.coeff_rescale`, with no appeal to convergence or analysis. -/
theorem coeff_X_pow_mul_rescale_invOneSubPow (c : ℚ) (k n : ℕ) :
    coeff n (X ^ k * rescale c (invOneSubPow ℚ (k + 1)).val)
      = if k ≤ n then (n.choose k : ℚ) * c ^ (n - k) else 0 := by
  rw [coeff_X_pow_mul']
  split_ifs with h
  · rw [coeff_rescale, invOneSubPow_val_succ_eq_mk_add_choose, coeff_mk]
    have hk : k + (n - k) = n := by omega
    rw [hk]
    ring
  · rfl

/-! ## Stage B, chain-rule ingredient (in progress)

The θ = X·d/dX operator and the power-series form of `catalanB_rec`, following the
paper's proof of Theorem 6.9 (equation `\eqref{eq:BOGF}`). This is still purely
algebraic (a restatement of `catalanB_rec'`, no substitution/composition, no analysis
yet). Status: newly added, not yet verified to compile. -/

open PowerSeries in
/-- The operator `θf = X · f'`, purely formal (no analysis). -/
noncomputable def theta (f : ℚ⟦X⟧) : ℚ⟦X⟧ := X * PowerSeries.derivative ℚ f

open PowerSeries in
theorem coeff_theta (f : ℚ⟦X⟧) (n : ℕ) : coeff n (theta f) = (n : ℚ) * coeff n f := by
  unfold theta
  cases n with
  | zero => simp
  | succ m =>
      simp only [coeff_succ_X_mul, coeff_derivative]
      push_cast
      ring

open PowerSeries in
theorem coeff_theta_theta (f : ℚ⟦X⟧) (n : ℕ) :
    coeff n (theta (theta f)) = (n : ℚ) ^ 2 * coeff n f := by
  rw [coeff_theta, coeff_theta]; ring

open PowerSeries in
/-- `catalanB` as a formal power series. -/
noncomputable def catalanBSeries : ℚ⟦X⟧ := PowerSeries.mk catalanB

open PowerSeries in
theorem coeff_catalanBSeries (n : ℕ) : coeff n catalanBSeries = catalanB n := by
  simp [catalanBSeries, coeff_mk]

open PowerSeries in
/-- **The theta-operator equation for `catalanB`.** This is the power-series form of
`(REC)`, including the exceptional initial residual `catalanB 1 - 4 * catalanB 0 = 1`
(the paper's equation `\eqref{eq:BOGF}` with `n ≥ 0`, no truncated subtraction).
Every coefficient of this identity reduces to `catalanB_rec'` (`n ≥ 2`), the boundary
values `catalanB_zero`/`catalanB_one` (`n = 0, 1`), or `0 = 0`; no analysis and no
power-series substitution/composition is used here. -/
theorem catalanB_operator_eq :
    theta (theta catalanBSeries)
      - X * (C (12 : ℚ) * theta (theta catalanBSeries) + C (12 : ℚ) * theta catalanBSeries
              + C (4 : ℚ) * catalanBSeries)
      + X * (X * (C (32 : ℚ) *
          (theta (theta catalanBSeries) + C (2 : ℚ) * theta catalanBSeries + catalanBSeries)))
      = X := by
  apply PowerSeries.ext
  intro n
  rcases n with _ | _ | m
  · -- n = 0
    have hX0 : coeff 0 (X : ℚ⟦X⟧) = 0 := by
      rw [← pow_one (X : ℚ⟦X⟧), coeff_X_pow]; simp
    simp [map_sub, map_add, coeff_C_mul, coeff_theta_theta, coeff_theta,
      coeff_catalanBSeries, coeff_zero_X_mul, catalanB_zero, hX0]
  · -- n = 1
    have hX1 : coeff 1 (X : ℚ⟦X⟧) = 1 := by
      rw [← pow_one (X : ℚ⟦X⟧), coeff_X_pow]; simp
    simp [map_sub, map_add, coeff_C_mul, coeff_theta_theta, coeff_theta,
      coeff_catalanBSeries, coeff_succ_X_mul, coeff_zero_X_mul, catalanB_zero, catalanB_one, hX1]
  · -- n = m + 1 + 1
    have key := catalanB_rec' m
    have hXm : coeff (m + 1 + 1) (X : ℚ⟦X⟧) = 0 := by
      rw [← pow_one (X : ℚ⟦X⟧), coeff_X_pow, if_neg (by omega)]
    simp only [map_sub, map_add, coeff_C_mul, coeff_theta_theta, coeff_theta,
      coeff_catalanBSeries, coeff_succ_X_mul, coeff_zero_X_mul, hXm]
    push_cast
    linear_combination key

/-! ## Stage B, weighted Pascal transforms (toward TREC)

Two reusable lemmas: the endpoint transform of `a` weighted by `k` (resp. `k(k-1)`)
reduces to a plain (unweighted) transform of a shift of `a`, via the identity
`Nat.add_one_mul_choose_eq`. These are the "Ingredient 2"-style facts from the status
log, proved by forward peel-and-reindex (never backward `k-1` subtraction), exactly the
technique already used in `genTr_succ`. -/

/-- **Weight-`k` Pascal reduction.** `Σ_{k≤m+1} C(m+1,k)(-4)^{m+1-k} k a_k = (m+1)·genTr (a∘succ) m`. -/
theorem genTrW1_eq (a : ℕ → ℚ) (m : ℕ) :
    ∑ k ∈ Finset.range (m + 1 + 1),
        ((m + 1).choose k : ℚ) * (-4 : ℚ) ^ (m + 1 - k) * (k : ℚ) * a k
      = ((m : ℚ) + 1) * genTr (fun k => a (k + 1)) m := by
  have hpeel := Finset.sum_range_succ'
    (fun k => ((m + 1).choose k : ℚ) * (-4 : ℚ) ^ (m + 1 - k) * (k : ℚ) * a k) (m + 1)
  simp only [Nat.cast_zero, mul_zero, zero_mul, add_zero] at hpeel
  rw [hpeel]
  rw [genTr, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro k hk
  simp only [Finset.mem_range] at hk
  have hexp : m + 1 - (k + 1) = m - k := by omega
  rw [hexp]
  have hid : ((k : ℚ) + 1) * ((m + 1).choose (k + 1) : ℚ) = ((m : ℚ) + 1) * (m.choose k : ℚ) := by
    have h := Nat.add_one_mul_choose_eq m k
    have : ((m + 1) * m.choose k : ℚ) = ((m + 1).choose (k + 1) * (k + 1) : ℚ) := by
      exact_mod_cast h
    push_cast at this ⊢
    linarith
  push_cast
  linear_combination (-4 : ℚ) ^ (m - k) * a (k + 1) * hid

/-- **Weight-`k(k-1)` Pascal reduction.**
`Σ_{k≤m+2} C(m+2,k)(-4)^{m+2-k} k(k-1) a_k = (m+2)(m+1)·genTr (fun k ↦ a (k+2)) m`. -/
theorem genTrW2_eq (a : ℕ → ℚ) (m : ℕ) :
    ∑ k ∈ Finset.range (m + 2 + 1),
        ((m + 2).choose k : ℚ) * (-4 : ℚ) ^ (m + 2 - k) * ((k : ℚ) * ((k : ℚ) - 1)) * a k
      = (((m : ℚ) + 2) * ((m : ℚ) + 1)) * genTr (fun k => a (k + 2)) m := by
  have hpeel1 := Finset.sum_range_succ'
    (fun k => ((m + 2).choose k : ℚ) * (-4 : ℚ) ^ (m + 2 - k) * ((k : ℚ) * ((k : ℚ) - 1)) * a k)
    (m + 2)
  simp only [Nat.cast_zero, zero_mul, mul_zero, add_zero] at hpeel1
  push_cast at hpeel1
  rw [hpeel1]
  have hpeel2 := Finset.sum_range_succ'
    (fun k => ((m + 2).choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m + 2 - (k + 1))
        * (((k : ℚ) + 1) * (((k : ℚ) + 1) - 1)) * a (k + 1)) (m + 1)
  simp only [Nat.cast_zero, add_zero, zero_add, mul_zero, zero_mul] at hpeel2
  push_cast at hpeel2
  have hpeel2' : ∑ x ∈ Finset.range (m + 2), ((m + 2).choose (x + 1) : ℚ) * (-4 : ℚ) ^ (m + 1 - x)
        * (((x:ℚ) + 1) * ((x:ℚ) + 1 - 1)) * a (x + 1)
      = ∑ x ∈ Finset.range (m + 1), ((m + 2).choose (x + 1 + 1) : ℚ) * (-4 : ℚ) ^ (m - x)
          * ((((x:ℚ) + 1) + 1) * ((x:ℚ) + 1)) * a (x + 1 + 1) := by
    rw [show (Finset.range (m + 1 + 1)) = Finset.range (m + 2) from rfl] at hpeel2
    rw [hpeel2]
    have hz : ((m + 2).choose 1 : ℚ) * (-4 : ℚ) ^ (m + 1) * (1 * (1 - 1)) * a 1 = 0 := by ring
    rw [hz, add_zero]
    apply Finset.sum_congr rfl
    intro x _
    ring_nf
  rw [show m + 1 + 1 = m + 2 from rfl] at hpeel2'
  rw [hpeel2']
  rw [genTr, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro k hk
  simp only [Finset.mem_range] at hk
  -- (k+2)(k+1) * C(m+2,k+2) = (m+2)(m+1) * C(m,k)
  have h1 : ((k : ℚ) + 1 + 1) * ((m + 2).choose (k + 1 + 1) : ℚ)
      = ((m : ℚ) + 2) * ((m + 1).choose (k + 1) : ℚ) := by
    have h := Nat.add_one_mul_choose_eq (m + 1) (k + 1)
    have : ((m + 1 + 1) * (m + 1).choose (k + 1) : ℚ)
        = ((m + 1 + 1).choose (k + 1 + 1) * (k + 1 + 1) : ℚ) := by exact_mod_cast h
    push_cast at this ⊢
    linarith
  have h2 : ((k : ℚ) + 1) * ((m + 1).choose (k + 1) : ℚ)
      = ((m : ℚ) + 1) * (m.choose k : ℚ) := by
    have h := Nat.add_one_mul_choose_eq m k
    have : ((m + 1) * m.choose k : ℚ) = ((m + 1).choose (k + 1) * (k + 1) : ℚ) := by
      exact_mod_cast h
    push_cast at this ⊢
    linarith
  have hkey : ((m + 2).choose (k+1+1) : ℚ) * (((k:ℚ)+1+1) * ((k:ℚ)+1))
      = ((m:ℚ)+2) * ((m:ℚ)+1) * (m.choose k : ℚ) := by
    linear_combination ((k:ℚ)+1) * h1 + ((m:ℚ)+2) * h2
  rw [show ((m + 2).choose (k+1+1) : ℚ) * (-4 : ℚ) ^ (m - k) * ((((k:ℚ)+1)+1) * ((k:ℚ)+1)) * a (k + 1 + 1)
      = (((m + 2).choose (k+1+1) : ℚ) * (((k:ℚ)+1+1) * ((k:ℚ)+1))) * (-4 : ℚ) ^ (m - k) * a (k+1+1) from by ring,
    hkey]
  ring

/-! ## Stage B, shifted-index Pascal identities (Q1, Q2), toward Way B of TREC -/

/-- **Q1.** `Σ_{j<m+1} C(m+1,j+1)(-4)^{m-j}(j+1) a_j = (m+1)·genTr a m`. -/
theorem genTrQ1_eq (a : ℕ → ℚ) (m : ℕ) :
    ∑ j ∈ Finset.range (m + 1), ((m + 1).choose (j + 1) : ℚ) * (-4 : ℚ) ^ (m - j) * ((j:ℚ) + 1) * a j
      = ((m:ℚ) + 1) * genTr a m := by
  rw [genTr, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j hj
  have hid : ((j : ℚ) + 1) * ((m + 1).choose (j + 1) : ℚ) = ((m : ℚ) + 1) * (m.choose j : ℚ) := by
    have h := Nat.add_one_mul_choose_eq m j
    have : ((m + 1) * m.choose j : ℚ) = ((m + 1).choose (j + 1) * (j + 1) : ℚ) := by
      exact_mod_cast h
    push_cast at this
    linarith
  rw [show ((m + 1).choose (j + 1) : ℚ) * (-4 : ℚ) ^ (m - j) * ((j:ℚ) + 1) * a j
      = (((j:ℚ)+1) * ((m + 1).choose (j + 1) : ℚ)) * (-4 : ℚ) ^ (m - j) * a j from by ring, hid]
  ring

/-- **Q2.** `Σ_{j<m+2} C(m+2,j+1)(-4)^{m+1-j}(j+1)² a_j
= (m+2)(m+1)·genTr (a∘succ) m + (m+2)·genTr a (m+1)`. -/
theorem genTrQ2_eq (a : ℕ → ℚ) (m : ℕ) :
    ∑ j ∈ Finset.range (m + 2),
        ((m + 2).choose (j + 1) : ℚ) * (-4 : ℚ) ^ (m + 1 - j) * (((j:ℚ) + 1) ^ 2) * a j
      = ((m:ℚ) + 2) * ((m:ℚ) + 1) * genTr (fun k => a (k + 1)) m
        + ((m:ℚ) + 2) * genTr a (m + 1) := by
  have hpt : ∀ j ∈ Finset.range (m + 2),
      ((m + 2).choose (j + 1) : ℚ) * (-4 : ℚ) ^ (m + 1 - j) * (((j:ℚ) + 1) ^ 2) * a j
        = ((m:ℚ) + 2) * (((m + 1).choose j : ℚ) * (-4 : ℚ) ^ (m + 1 - j) * (j:ℚ) * a j)
          + ((m:ℚ) + 2) * (((m + 1).choose j : ℚ) * (-4 : ℚ) ^ (m + 1 - j) * a j) := by
    intro j _
    have h1 : ((j : ℚ) + 1) * ((m + 2).choose (j + 1) : ℚ) = ((m : ℚ) + 2) * ((m + 1).choose j : ℚ) := by
      have h := Nat.add_one_mul_choose_eq (m + 1) j
      have : ((m + 1 + 1) * (m + 1).choose j : ℚ) = ((m + 1 + 1).choose (j + 1) * (j + 1) : ℚ) := by
        exact_mod_cast h
      push_cast at this
      linarith
    have hsq : (((j:ℚ) + 1) ^ 2) * ((m + 2).choose (j + 1) : ℚ)
        = ((j:ℚ) + 1) * (((m:ℚ)+2) * ((m + 1).choose j : ℚ)) := by
      rw [← h1]; ring
    rw [show ((m + 2).choose (j + 1) : ℚ) * (-4 : ℚ) ^ (m + 1 - j) * (((j:ℚ) + 1) ^ 2) * a j
        = ((((j:ℚ) + 1) ^ 2) * ((m + 2).choose (j + 1) : ℚ)) * (-4 : ℚ) ^ (m + 1 - j) * a j from by ring,
      hsq]
    ring
  rw [Finset.sum_congr rfl hpt, Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum]
  have e1 : ∑ j ∈ Finset.range (m + 2), ((m + 1).choose j : ℚ) * (-4 : ℚ) ^ (m + 1 - j) * (j:ℚ) * a j
      = ((m:ℚ) + 1) * genTr (fun k => a (k + 1)) m := genTrW1_eq a m
  have e2 : ∑ j ∈ Finset.range (m + 2), ((m + 1).choose j : ℚ) * (-4 : ℚ) ^ (m + 1 - j) * a j
      = genTr a (m + 1) := rfl
  rw [e1, e2]
  ring

/-- **Q0.** `Σ_{j<m+1} C(m+1,j+1)(-4)^{m-j} a_{j+1} = genTr a (m+1) - (-4)^{m+1} a 0`. -/
theorem genTrQ0_eq (a : ℕ → ℚ) (m : ℕ) :
    ∑ j ∈ Finset.range (m + 1), ((m + 1).choose (j + 1) : ℚ) * (-4 : ℚ) ^ (m - j) * a (j + 1)
      = genTr a (m + 1) - (-4 : ℚ) ^ (m + 1) * a 0 := by
  have h := Finset.sum_range_succ'
    (fun k => ((m + 1).choose k : ℚ) * (-4 : ℚ) ^ (m + 1 - k) * a k) (m + 1)
  simp only [Nat.choose_zero_right, Nat.cast_one, one_mul, Nat.sub_zero] at h
  have hgt : genTr a (m + 1) = (-4 : ℚ) ^ (m + 1) * a 0
      + ∑ k ∈ Finset.range (m + 1), ((m + 1).choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m + 1 - (k + 1)) * a (k + 1) := by
    simp only [genTr]; rw [h]; ring
  have hexp : ∀ k ∈ Finset.range (m + 1),
      ((m + 1).choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m + 1 - (k + 1)) * a (k + 1)
        = ((m + 1).choose (k + 1) : ℚ) * (-4 : ℚ) ^ (m - k) * a (k + 1) := by
    intro k hk
    simp only [Finset.mem_range] at hk
    have : m + 1 - (k + 1) = m - k := by omega
    rw [this]
  rw [Finset.sum_congr rfl hexp] at hgt
  rw [hgt]; ring

/-! ## Stage B, closing TREC -/

/-- `W_n := Σ C(n,k)(-4)^{n-k} B_{k+2}`. -/
def catalanW (n : ℕ) : ℚ := genTr (fun k => catalanB (k + 2)) n

/-- `Y_n := Σ C(n,k)(-4)^{n-k} B_{k+3}`. -/
def catalanY (n : ℕ) : ℚ := genTr (fun k => catalanB (k + 3)) n

theorem catalanV_eq (n : ℕ) : catalanV n = genTr (fun k => catalanB (k + 1)) n := rfl

theorem catalanV_succ (m : ℕ) : catalanV (m + 1) = -4 * catalanV m + catalanW m := by
  have h := genTr_succ (fun k => catalanB (k + 1)) m
  simpa [catalanV_eq, catalanW] using h

theorem catalanW_succ (m : ℕ) : catalanW (m + 1) = -4 * catalanW m + catalanY m := by
  have h := genTr_succ (fun k => catalanB (k + 2)) m
  simpa [catalanW, catalanY] using h

/-- `M_n := Σ_{k=0}^n C(n,k)(-4)^{n-k}(k+1)² B_{k+1}`. -/
def catalanM (n : ℕ) : ℚ :=
  ∑ k ∈ Finset.range (n + 1), (n.choose k : ℚ) * (-4 : ℚ) ^ (n - k) * (((k:ℚ) + 1) ^ 2) * catalanB (k + 1)

/-- **Way A** (no use of `catalanB_rec`): purely from the Pascal weighted-transform
identities `genTrW1_eq`/`genTrW2_eq` applied to `a := fun k ↦ catalanB (k+1)`. -/
theorem catalanM_wayA (m : ℕ) :
    catalanM (m + 2)
      = ((m:ℚ) + 2) * ((m:ℚ) + 1) * catalanY m + 3 * (((m:ℚ) + 2) * catalanW (m + 1))
        + catalanV (m + 2) := by
  have hpt : ∀ k ∈ Finset.range (m + 2 + 1),
      ((m+2).choose k : ℚ) * (-4 : ℚ) ^ (m + 2 - k) * (((k:ℚ) + 1) ^ 2) * catalanB (k + 1)
        = ((m+2).choose k : ℚ) * (-4 : ℚ) ^ (m + 2 - k) * ((k:ℚ) * ((k:ℚ) - 1)) * catalanB (k + 1)
          + 3 * (((m+2).choose k : ℚ) * (-4 : ℚ) ^ (m + 2 - k) * (k:ℚ) * catalanB (k + 1))
          + ((m+2).choose k : ℚ) * (-4 : ℚ) ^ (m + 2 - k) * catalanB (k + 1) := by
    intro k _; ring
  have hsplit : catalanM (m + 2)
      = (∑ k ∈ Finset.range (m + 2 + 1),
            ((m+2).choose k : ℚ) * (-4 : ℚ) ^ (m + 2 - k) * ((k:ℚ) * ((k:ℚ) - 1)) * catalanB (k + 1))
        + 3 * (∑ k ∈ Finset.range (m + 2 + 1),
            ((m+2).choose k : ℚ) * (-4 : ℚ) ^ (m + 2 - k) * (k:ℚ) * catalanB (k + 1))
        + ∑ k ∈ Finset.range (m + 2 + 1),
            ((m+2).choose k : ℚ) * (-4 : ℚ) ^ (m + 2 - k) * catalanB (k + 1) := by
    rw [catalanM, Finset.sum_congr rfl hpt]
    rw [Finset.sum_add_distrib, Finset.sum_add_distrib, Finset.mul_sum]
  have hW2 := genTrW2_eq (fun k => catalanB (k + 1)) m
  have hW1 := genTrW1_eq (fun k => catalanB (k + 1)) (m + 1)
  have hT : ∑ k ∈ Finset.range (m + 2 + 1),
      ((m+2).choose k : ℚ) * (-4 : ℚ) ^ (m + 2 - k) * catalanB (k + 1) = catalanV (m + 2) := rfl
  rw [show (m+1+1+1) = (m+2+1) from rfl] at hW1
  rw [hsplit, hW2, hW1, hT]
  have hY : genTr (fun k => catalanB (k + 2 + 1)) m = catalanY m := by
    show genTr (fun k => catalanB (k + 2 + 1)) m = genTr (fun k => catalanB (k + 3)) m
    norm_num
  have hWm1 : genTr (fun k => catalanB (k + 1 + 1)) (m + 1) = catalanW (m + 1) := by
    show genTr (fun k => catalanB (k + 1 + 1)) (m + 1) = genTr (fun k => catalanB (k + 2)) (m + 1)
    norm_num
  rw [hY, hWm1]
  push_cast
  ring

/-- **Way B** (uses `catalanB_rec`): substituting `catalanB_rec` into `catalanM`'s
`k ≥ 1` terms, and `catalanB_one` into its `k = 0` term. -/
theorem catalanM_wayB (m : ℕ) :
    catalanM (m + 2)
      = (-4 : ℚ) ^ (m + 2)
        + 12 * (((m:ℚ) + 2) * ((m:ℚ) + 1) * catalanW m) + 24 * (((m:ℚ) + 2) * catalanV (m + 1))
        + 4 * catalanT (m + 2)
        - 32 * (((m:ℚ) + 2) * ((m:ℚ) + 1) * catalanV m + ((m:ℚ) + 2) * catalanT (m + 1)) := by
  have hpeel : catalanM (m + 2)
      = (-4 : ℚ) ^ (m + 2) * catalanB 1
        + ∑ k ∈ Finset.range (m + 2), ((m+2).choose (k+1) : ℚ) * (-4 : ℚ) ^ (m + 2 - (k+1))
            * (((k:ℚ) + 1 + 1) ^ 2) * catalanB (k + 1 + 1) := by
    have h := Finset.sum_range_succ'
      (fun k => ((m+2).choose k : ℚ) * (-4 : ℚ) ^ (m + 2 - k) * (((k:ℚ) + 1) ^ 2) * catalanB (k + 1))
      (m + 2)
    simp only [Nat.cast_zero, Nat.sub_zero, Nat.choose_zero_right, Nat.cast_one, Nat.zero_add] at h
    rw [catalanM]
    rw [h]
    norm_num
    ring
  rw [catalanB_one, mul_one] at hpeel
  have hsub : ∀ k ∈ Finset.range (m + 2),
      ((m+2).choose (k+1) : ℚ) * (-4 : ℚ) ^ (m + 2 - (k+1)) * (((k:ℚ) + 1 + 1) ^ 2) * catalanB (k + 1 + 1)
        = ((m+2).choose (k+1) : ℚ) * (-4 : ℚ) ^ (m + 1 - k)
          * ((12 * ((k:ℚ)+1)^2 + 12*((k:ℚ)+1) + 4) * catalanB (k+1) - 32*((k:ℚ)+1)^2 * catalanB k) := by
    intro k hk
    have hrec := catalanB_rec' k
    have hexp : m + 2 - (k + 1) = m + 1 - k := by omega
    rw [hexp]
    have : ((k:ℚ) + 1 + 1) ^ 2 * catalanB (k + 1 + 1)
        = (12 * ((k:ℚ)+1)^2 + 12*((k:ℚ)+1) + 4) * catalanB (k+1) - 32*((k:ℚ)+1)^2 * catalanB k := by
      linear_combination hrec
    rw [show ((m+2).choose (k+1) : ℚ) * (-4 : ℚ) ^ (m + 1 - k) * (((k:ℚ) + 1 + 1) ^ 2) * catalanB (k + 1 + 1)
        = ((m+2).choose (k+1) : ℚ) * (-4 : ℚ) ^ (m + 1 - k) * (((k:ℚ) + 1 + 1) ^ 2 * catalanB (k+1+1))
        from by ring, this]
  rw [Finset.sum_congr rfl hsub] at hpeel
  have hexpand : ∀ k ∈ Finset.range (m + 2),
      ((m+2).choose (k+1) : ℚ) * (-4 : ℚ) ^ (m + 1 - k)
          * ((12 * ((k:ℚ)+1)^2 + 12*((k:ℚ)+1) + 4) * catalanB (k+1) - 32*((k:ℚ)+1)^2 * catalanB k)
        = 12 * (((m+2).choose (k+1) : ℚ) * (-4:ℚ)^(m+1-k) * (((k:ℚ)+1)^2) * catalanB (k+1))
          + 12 * (((m+2).choose (k+1) : ℚ) * (-4:ℚ)^(m+1-k) * ((k:ℚ)+1) * catalanB (k+1))
          + 4 * (((m+2).choose (k+1) : ℚ) * (-4:ℚ)^(m+1-k) * catalanB (k+1))
          - 32 * (((m+2).choose (k+1) : ℚ) * (-4:ℚ)^(m+1-k) * (((k:ℚ)+1)^2) * catalanB k) := by
    intro k _; ring
  rw [Finset.sum_congr rfl hexpand] at hpeel
  rw [Finset.sum_sub_distrib, Finset.sum_add_distrib, Finset.sum_add_distrib,
      ← Finset.mul_sum, ← Finset.mul_sum, ← Finset.mul_sum, ← Finset.mul_sum] at hpeel
  -- identify the four resulting sums via Q2, Q1, Q0 (applied to `a1 := fun k ↦ catalanB (k+1)`)
  -- and Q2 (applied to `catalanB` itself).
  have e1 : ∑ k ∈ Finset.range (m + 2),
      ((m+2).choose (k+1) : ℚ) * (-4:ℚ)^(m+1-k) * (((k:ℚ)+1)^2) * catalanB (k+1)
      = ((m:ℚ)+2) * ((m:ℚ)+1) * catalanW m + ((m:ℚ)+2) * catalanV (m + 1) := by
    have h := genTrQ2_eq (fun k => catalanB (k + 1)) m
    have hWeq : genTr (fun k => catalanB (k + 1 + 1)) m = catalanW m := by
      show genTr (fun k => catalanB (k + 1 + 1)) m = genTr (fun k => catalanB (k + 2)) m
      norm_num
    rw [hWeq, ← catalanV_eq] at h
    exact h
  have e2 : ∑ k ∈ Finset.range (m + 2),
      ((m+2).choose (k+1) : ℚ) * (-4:ℚ)^(m+1-k) * ((k:ℚ)+1) * catalanB (k+1)
      = ((m:ℚ)+2) * catalanV (m + 1) := by
    have h := genTrQ1_eq (fun k => catalanB (k + 1)) (m + 1)
    rw [← catalanV_eq] at h
    convert h using 2
    push_cast; ring
  have e3 : ∑ k ∈ Finset.range (m + 2),
      ((m+2).choose (k+1) : ℚ) * (-4:ℚ)^(m+1-k) * catalanB (k+1)
      = catalanT (m + 2) := by
    have h := genTrQ0_eq catalanB (m + 1)
    rw [catalanB_zero, mul_zero, sub_zero] at h
    have hTeq : genTr catalanB (m + 1 + 1) = catalanT (m + 2) := rfl
    rw [hTeq] at h
    convert h using 2
  have e4 : ∑ k ∈ Finset.range (m + 2),
      ((m+2).choose (k+1) : ℚ) * (-4:ℚ)^(m+1-k) * (((k:ℚ)+1)^2) * catalanB k
      = ((m:ℚ)+2) * ((m:ℚ)+1) * catalanV m + ((m:ℚ)+2) * catalanT (m + 1) := by
    have h := genTrQ2_eq catalanB m
    rw [← catalanV_eq] at h
    exact h
  rw [e1, e2, e3, e4] at hpeel
  rw [hpeel]
  ring

/-- **TREC, `n ≥ 2` case.** `(m+3)²T_{m+3} - 16(m+2)²T_{m+1} = (-4)^{m+2}`, i.e. `TREC`
at `n = m+2`. Proved by equating `catalanM_wayA`/`catalanM_wayB` and eliminating
`catalanY`, `catalanW`, `catalanV` via the shift-tower relations. -/
theorem catalanT_rec_aux (m : ℕ) :
    ((m:ℚ) + 3) ^ 2 * catalanT (m + 3) - 16 * ((m:ℚ) + 2) ^ 2 * catalanT (m + 1)
      = (-4 : ℚ) ^ (m + 2) := by
  have hA := catalanM_wayA m
  have hB := catalanM_wayB m
  have hWs := catalanW_succ m
  have hVs1 := catalanV_succ m
  have hVs2 := catalanV_succ (m + 1)
  have hTs1 := catalanT_succ (m + 1)
  have hTs2 := catalanT_succ (m + 2)
  rw [show m + 1 + 1 = m + 2 from rfl] at hVs2 hTs1
  rw [show m + 2 + 1 = m + 3 from rfl] at hTs2
  linear_combination hB - hA + ((m:ℚ)+2)*((m:ℚ)+1) * hWs - 8*((m:ℚ)+2)*((m:ℚ)+1) * hVs1
    + ((m:ℚ)+2)*((m:ℚ)+4) * hVs2 - 4*((m:ℚ)+2)*((m:ℚ)+4) * hTs1
    + (1 + ((m:ℚ)+2)*((m:ℚ)+4)) * hTs2

/-- **TREC.** The endpoint binomial transform's recurrence:
`(n+1)²T_{n+1} - 16n²T_{n-1} = (-4)^n` for all `n`, with truncated `ℕ` subtraction (the
`n = 0` term containing `T_{n-1}` is multiplied by `0`). -/
theorem catalanT_rec (n : ℕ) :
    ((n:ℚ) + 1) ^ 2 * catalanT (n + 1) - 16 * (n:ℚ) ^ 2 * catalanT (n - 1) = (-4 : ℚ) ^ n := by
  match n with
  | 0 =>
      have h1 : catalanT 1 = 1 := catalanT_values.2.1
      norm_num [h1]
  | 1 =>
      have h1 : catalanT 1 = 1 := catalanT_values.2.1
      have h2 : catalanT 2 = -1 := catalanT_values.2.2
      norm_num [h1, h2]
  | (m + 2) =>
      have h := catalanT_rec_aux m
      have e1 : m + 2 + 1 = m + 3 := by omega
      have e2 : m + 2 - 1 = m + 1 := by omega
      rw [e1, e2]
      push_cast
      linear_combination h

/-! ## Stage C — the endpoint square expansion -/

/-- The "half-length" `q = (n-j-1)/2` appearing in the endpoint formula `R_{n,j}`. -/
def endpointQ (n j : ℕ) : ℕ := (n - j - 1) / 2

/-- The numerator product `∏_{t=0}^{q-1} (j+2+2t)` (empty product `= 1` when `q = 0`). -/
def endpointNum (n j : ℕ) : ℕ :=
  ∏ t ∈ Finset.range (endpointQ n j), (j + 2 + 2 * t)

/-- The denominator product `∏_{t=0}^{q} (j+1+2t)`. -/
def endpointDen (n j : ℕ) : ℕ :=
  ∏ t ∈ Finset.range (endpointQ n j + 1), (j + 1 + 2 * t)

theorem endpointDen_pos (n j : ℕ) : 0 < endpointDen n j := by
  apply Finset.prod_pos
  intro t _
  omega

theorem endpointDen_ne_zero (n j : ℕ) : endpointDen n j ≠ 0 :=
  (endpointDen_pos n j).ne'

/-- The endpoint quantity `R_{n,j} = 2^{n-1} \cdot Num/Den`. -/
def endpointR (n j : ℕ) : ℚ :=
  (2 : ℚ) ^ (n - 1) * (endpointNum n j : ℚ) / (endpointDen n j : ℚ)

/-- At `j = n - 1` (so `q = 0`): `R_{n,n-1} = 2^{n-1}/n`. -/
theorem endpointR_top (n : ℕ) (hn : 1 ≤ n) :
    endpointR n (n - 1) = (2 : ℚ) ^ (n - 1) / (n : ℚ) := by
  have hq : endpointQ n (n - 1) = 0 := by unfold endpointQ; omega
  have hNum : endpointNum n (n - 1) = 1 := by unfold endpointNum; rw [hq]; simp
  have hDen : endpointDen n (n - 1) = n := by
    unfold endpointDen; rw [hq]
    have hn' : n - 1 + 1 = n := by omega
    simp [hn']
  unfold endpointR
  rw [hNum, hDen]
  simp

/-- Step relation: for `j + 2 ≤ n - 2` (equivalently `j < n - 2` in ℕ) with `n ≥ 3`,
`Num`/`Den` for `(n,j)` are obtained from `(n-2,j)` by one extra factor each, giving
`R_{n,j} = (4(n-1)/n) \cdot R_{n-2,j}`. -/
theorem endpointNum_step (n j : ℕ) (hj : j + 3 ≤ n) (hodd : Odd (n - j)) :
    endpointNum n j = endpointNum (n - 2) j * (n - 1) := by
  have hq : endpointQ n j = endpointQ (n - 2) j + 1 := by
    unfold endpointQ
    rcases hodd with ⟨k, hk⟩
    omega
  unfold endpointNum
  rw [hq, Finset.prod_range_succ]
  congr 1
  unfold endpointQ
  rcases hodd with ⟨k, hk⟩
  omega

theorem endpointDen_step (n j : ℕ) (hj : j + 3 ≤ n) (hodd : Odd (n - j)) :
    endpointDen n j = endpointDen (n - 2) j * n := by
  have hq : endpointQ n j + 1 = (endpointQ (n - 2) j + 1) + 1 := by
    unfold endpointQ
    rcases hodd with ⟨k, hk⟩
    omega
  unfold endpointDen
  rw [hq, Finset.prod_range_succ]
  congr 1
  unfold endpointQ
  rcases hodd with ⟨k, hk⟩
  omega

theorem endpointR_step (n j : ℕ) (hj : j + 3 ≤ n) (hodd : Odd (n - j)) :
    endpointR n j = (4 * ((n : ℚ) - 1) / (n : ℚ)) * endpointR (n - 2) j := by
  have hn3 : 3 ≤ n := by omega
  have hNum := endpointNum_step n j hj hodd
  have hDen := endpointDen_step n j hj hodd
  have hDenpos : (endpointDen (n - 2) j : ℚ) ≠ 0 := by
    exact_mod_cast endpointDen_ne_zero (n - 2) j
  have hnQ : (n : ℚ) ≠ 0 := by
    have : 0 < n := by omega
    exact_mod_cast this.ne'
  unfold endpointR
  rw [hNum, hDen]
  have hpow : (2 : ℚ) ^ (n - 1) = 4 * (2 : ℚ) ^ (n - 2 - 1) := by
    have : n - 1 = (n - 2 - 1) + 2 := by omega
    rw [this, pow_add]
    ring
  rw [hpow]
  push_cast
  have hcast : ((n:ℚ) - 1 : ℚ) = ((n - 1 : ℕ) : ℚ) := by
    have h1n : (1:ℕ) ≤ n := by omega
    rw [Nat.cast_sub h1n]
    norm_num
  rw [← hcast]
  field_simp

/-- The right-hand side of `TSQ`, as an indicator sum over `Finset.range n`. -/
def catalanSumR (n : ℕ) : ℚ :=
  ∑ j ∈ Finset.range n, if Odd (n - j) then (endpointR n j) ^ 2 else 0

/-- Peeling the top index `j = n - 1` (whose indicator is always `1`) and the vanishing
index `j = n - 2` (whose indicator is always `0`) from `catalanSumR n`, for `n ≥ 2`. -/
theorem catalanSumR_succ_succ (n : ℕ) (hn : 2 ≤ n) :
    catalanSumR n
      = (∑ j ∈ Finset.range (n - 2), if Odd (n - j) then (endpointR n j) ^ 2 else 0)
        + (endpointR n (n - 1)) ^ 2 := by
  have hn1 : n - 2 + 1 = n - 1 := by omega
  have hn2 : n - 1 + 1 = n := by omega
  unfold catalanSumR
  rw [← hn2, Finset.sum_range_succ, ← hn1, Finset.sum_range_succ]
  have h1 : Odd (n - (n - 2)) = False := by
    have : n - (n - 2) = 2 := by omega
    simp [this]
  have h2 : Odd (n - (n - 1)) := by
    have : n - (n - 1) = 1 := by omega
    simp [this]
  rw [hn1, hn2]
  simp only [h1, h2, if_true, if_false]
  ring

/-- Replacing each term of `catalanSumR n`'s "lower" part (indices `j < n - 2`) by the
corresponding `catalanSumR (n-2)` term via `endpointR_step`. -/
theorem catalanSumR_lower_eq (n : ℕ) (hn : 2 ≤ n) :
    (∑ j ∈ Finset.range (n - 2), if Odd (n - j) then (endpointR n j) ^ 2 else 0)
      = (16 * ((n : ℚ) - 1) ^ 2 / (n : ℚ) ^ 2) * catalanSumR (n - 2) := by
  unfold catalanSumR
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j hj
  rw [Finset.mem_range] at hj
  have hpar : Odd (n - j) ↔ Odd (n - 2 - j) := by
    rw [Nat.odd_iff, Nat.odd_iff]
    omega
  by_cases hodd : Odd (n - j)
  · have hodd' : Odd (n - 2 - j) := hpar.mp hodd
    simp only [hodd, hodd', if_true]
    have hstep := endpointR_step n j (by omega) hodd
    rw [hstep]
    ring
  · have hodd' : ¬ Odd (n - 2 - j) := fun h => hodd (hpar.mpr h)
    simp [hodd, hodd']

/-- **TSQ.** The endpoint square expansion: `(-1)^{n-1} T_n = Σ_{0≤j<n, n-j odd} R_{n,j}²`,
proved by induction in steps of two from `TREC` (`catalanT_rec`). -/
theorem catalanT_square_formula :
    ∀ n : ℕ, 1 ≤ n → (-1 : ℚ) ^ (n - 1) * catalanT n = catalanSumR n := by
  have main : ∀ n : ℕ,
      ((-1 : ℚ) ^ n * catalanT (n + 1) = catalanSumR (n + 1)) ∧
      ((-1 : ℚ) ^ (n + 1) * catalanT (n + 2) = catalanSumR (n + 2)) := by
    intro n
    induction n with
    | zero =>
        constructor
        · have h1 : catalanT 1 = 1 := catalanT_values.2.1
          have hs1 : catalanSumR 1 = 1 := by
            unfold catalanSumR
            rw [Finset.sum_range_one]
            have e1 : Odd (1 - 0) := by decide
            simp only [e1, if_true]
            have h0 : endpointR 1 0 = 1 := by
              have h := endpointR_top 1 (by norm_num)
              norm_num at h
              exact h
            rw [h0]; norm_num
          rw [h1, hs1]; norm_num
        · have h2 : catalanT 2 = -1 := catalanT_values.2.2
          have hs2 : catalanSumR 2 = 1 := by
            unfold catalanSumR
            rw [Finset.sum_range_succ, Finset.sum_range_one]
            have e0 : Odd (2 - 0) = False := by simp
            have e1 : Odd (2 - 1) := by decide
            simp only [e0, e1, if_true, if_false]
            have h10 : endpointR 2 1 = 1 := by
              have h := endpointR_top 2 (by norm_num)
              norm_num at h
              exact h
            rw [h10]; norm_num
          rw [h2, hs2]; norm_num
    | succ n ih =>
        obtain ⟨ihodd, iheven⟩ := ih
        refine ⟨iheven, ?_⟩
        -- use TREC at index n+2 : (n+3)^2 T(n+3) - 16(n+2)^2 T(n+1) = (-4)^(n+2)
        have htrec := catalanT_rec (n + 2)
        have earg : n + 2 + 1 = n + 3 := by omega
        have earg2 : n + 2 - 1 = n + 1 := by omega
        rw [earg, earg2] at htrec
        push_cast at htrec
        have hpow1 : (-1:ℚ) ^ (n + 2) = (-1) ^ n := by rw [pow_add]; norm_num
        have hpowconv : (-4:ℚ) ^ (n + 2) = (-1) ^ n * 4 ^ (n + 2) := by
          rw [show (-4:ℚ) = (-1) * 4 from by norm_num, mul_pow, hpow1]
        -- Solve for T(n+3)
        have hTn3 : catalanT (n + 3)
            = (16 * ((n:ℚ) + 2) ^ 2 * catalanT (n + 1) + (-1:ℚ) ^ n * 4 ^ (n + 2))
              / ((n:ℚ) + 3) ^ 2 := by
          have hne : ((n:ℚ) + 3) ^ 2 ≠ 0 := by positivity
          rw [← hpowconv]
          field_simp
          linear_combination htrec
        have hsplit := catalanSumR_succ_succ (n + 3) (by omega)
        have hlow := catalanSumR_lower_eq (n + 3) (by omega)
        have hn2 : n + 3 - 2 = n + 1 := by omega
        have hn2' : n + 3 - 1 = n + 2 := by omega
        have hcastn3 : ((n + 3 : ℕ) : ℚ) = (n : ℚ) + 3 := by push_cast; ring
        rw [hn2] at hsplit hlow
        rw [hn2'] at hsplit
        rw [hcastn3] at hlow
        rw [hsplit, hlow, ← ihodd]
        have htop : endpointR (n + 3) (n + 2) ^ 2 = (4:ℚ) ^ (n + 2) / ((n:ℚ) + 3) ^ 2 := by
          have h := endpointR_top (n + 3) (by omega)
          have e : n + 3 - 1 = n + 2 := by omega
          rw [e] at h
          have hcast3 : ((n + 3 : ℕ) : ℚ) = (n : ℚ) + 3 := by push_cast; ring
          rw [hcast3] at h
          rw [h, div_pow]
          congr 1
          rw [show (4:ℚ) = 2 ^ 2 from by norm_num, ← pow_mul, ← pow_mul]
          congr 1
          ring
        rw [htop, hTn3]
        have hne3 : ((n:ℚ) + 3) ^ 2 ≠ 0 := by positivity
        have hnn1 : (-1:ℚ) ^ n * (-1:ℚ) ^ n = 1 := by rw [← mul_pow]; norm_num
        rw [show n + 1 + 1 = n + 2 from rfl]
        field_simp
        linear_combination (4:ℚ) ^ (n + 2) * hnn1
  intro n hn
  match n, hn with
  | (m + 1), _ =>
      have h := (main m).1
      have e : m + 1 - 1 = m := by omega
      rwa [e]

/-! ## Stage D (in progress) — the parity-imbalance combinatorial lemma

This is the smallest fully standalone reusable lemma identified as the starting point
for the crucial denominator divisibility `DIV`/`RL` (see
`work/harmonic_jets/CLAUDE_CATALAN_ENDPOINT_STATUS.md`): in any interval of naturals,
the count of even elements and the count of odd elements differ by at most `1`. It is
proved here in full, with no `sorry`/`admit`/`axiom`. The remaining Stage D work
(specializing to multiples of an odd `d` via the parity-preserving bijection `i ↦ i/d`,
then assembling the per-prime valuation bound and `endpointDen_dvd`) is **not** done in
this file yet; see the status log for the precise blocking gap. -/

/-- In any interval `Icc lo hi` of naturals, the number of even elements and the number
of odd elements differ by at most `1`. Proved by a two-step (stride-2) induction on `hi`
for fixed `lo`: adding two consecutive new top elements (one even, one odd) leaves the
even/odd count difference unchanged, which avoids the parity bookkeeping a naive stride-1
induction would need. -/
theorem card_even_odd_diff_le_one (lo hi : ℕ) :
    ((Finset.Icc lo hi).filter (fun i => Even i)).card ≤
      ((Finset.Icc lo hi).filter (fun i => Odd i)).card + 1 ∧
    ((Finset.Icc lo hi).filter (fun i => Odd i)).card ≤
      ((Finset.Icc lo hi).filter (fun i => Even i)).card + 1 := by
  suffices h : ∀ m : ℕ,
      (((Finset.Icc lo (lo + m)).filter (fun i => Even i)).card ≤
          ((Finset.Icc lo (lo + m)).filter (fun i => Odd i)).card + 1 ∧
        ((Finset.Icc lo (lo + m)).filter (fun i => Odd i)).card ≤
          ((Finset.Icc lo (lo + m)).filter (fun i => Even i)).card + 1) ∧
      (((Finset.Icc lo (lo + m + 1)).filter (fun i => Even i)).card ≤
          ((Finset.Icc lo (lo + m + 1)).filter (fun i => Odd i)).card + 1 ∧
        ((Finset.Icc lo (lo + m + 1)).filter (fun i => Odd i)).card ≤
          ((Finset.Icc lo (lo + m + 1)).filter (fun i => Even i)).card + 1) by
    by_cases hle : lo ≤ hi
    · obtain ⟨m, rfl⟩ := Nat.exists_eq_add_of_le hle
      exact (h m).1
    · have he : Finset.Icc lo hi = ∅ := by apply Finset.Icc_eq_empty; omega
      simp [he]
  intro m
  induction m with
  | zero =>
      refine ⟨?_, ?_⟩
      · have hs : Finset.Icc lo (lo + 0) = {lo} := by simp [Finset.Icc_self]
        rw [hs]
        rcases Nat.even_or_odd lo with hev | hod
        · have hno : ¬ Odd lo := by rw [Nat.odd_iff]; rw [Nat.even_iff] at hev; omega
          simp [Finset.filter_singleton, hev, hno]
        · have hne : ¬ Even lo := by rw [Nat.even_iff]; rw [Nat.odd_iff] at hod; omega
          simp [Finset.filter_singleton, hod, hne]
      · have hs : Finset.Icc lo (lo + 0 + 1) = {lo, lo + 1} := by
          ext x; simp only [Finset.mem_Icc, Finset.mem_insert, Finset.mem_singleton]; omega
        rw [hs]
        have hne : lo ≠ lo + 1 := by omega
        rw [Finset.filter_insert, Finset.filter_insert, Finset.filter_singleton,
          Finset.filter_singleton]
        rcases Nat.even_or_odd lo with hev | hod
        · have hno : ¬ Odd lo := by rw [Nat.odd_iff]; rw [Nat.even_iff] at hev; omega
          have hod1 : Odd (lo + 1) := by rw [Nat.odd_iff]; rw [Nat.even_iff] at hev; omega
          have hne1 : ¬ Even (lo + 1) := by rw [Nat.even_iff]; rw [Nat.odd_iff] at hod1; omega
          simp [hev, hno, hod1, hne1]
        · have hne0 : ¬ Even lo := by rw [Nat.even_iff]; rw [Nat.odd_iff] at hod; omega
          have hev1 : Even (lo + 1) := by rw [Nat.even_iff]; rw [Nat.odd_iff] at hod; omega
          have hno1 : ¬ Odd (lo + 1) := by rw [Nat.odd_iff]; rw [Nat.even_iff] at hev1; omega
          simp [hod, hne0, hev1, hno1]
  | succ m ih =>
      obtain ⟨ihm, ihm1⟩ := ih
      have e0 : lo + (m + 1) = lo + m + 1 := by omega
      refine ⟨by rw [e0]; exact ihm1, ?_⟩
      have e1 : lo + (m + 1) + 1 = lo + m + 2 := by omega
      rw [e1]
      have hins : Finset.Icc lo (lo + m + 2)
          = insert (lo + m + 2) (insert (lo + m + 1) (Finset.Icc lo (lo + m))) := by
        ext x; simp only [Finset.mem_insert, Finset.mem_Icc]; omega
      rw [hins, Finset.filter_insert, Finset.filter_insert, Finset.filter_insert,
        Finset.filter_insert]
      obtain ⟨h1, h2⟩ := ihm
      have hniE1 : (lo + m + 1) ∉ (Finset.Icc lo (lo + m)).filter (fun i => Even i) := by
        simp only [Finset.mem_filter, Finset.mem_Icc]; omega
      have hniO1 : (lo + m + 1) ∉ (Finset.Icc lo (lo + m)).filter (fun i => Odd i) := by
        simp only [Finset.mem_filter, Finset.mem_Icc]; omega
      have hniE2 : (lo + m + 2) ∉ (Finset.Icc lo (lo + m)).filter (fun i => Even i) := by
        simp only [Finset.mem_filter, Finset.mem_Icc]; omega
      have hniO2 : (lo + m + 2) ∉ (Finset.Icc lo (lo + m)).filter (fun i => Odd i) := by
        simp only [Finset.mem_filter, Finset.mem_Icc]; omega
      rcases Nat.even_or_odd (lo + m) with hev | hod
      · -- lo+m even ⇒ lo+m+1 odd, lo+m+2 even
        have hm2 : (lo + m) % 2 = 0 := by rw [← Nat.even_iff]; exact hev
        have hp1 : Odd (lo + m + 1) := by rw [Nat.odd_iff]; omega
        have hp1' : ¬ Even (lo + m + 1) := by rw [Nat.even_iff]; omega
        have hp2 : Even (lo + m + 2) := by rw [Nat.even_iff]; omega
        have hp2' : ¬ Odd (lo + m + 2) := by rw [Nat.odd_iff]; omega
        rw [if_pos hp2, if_neg hp2', if_neg hp1', if_pos hp1]
        rw [Finset.card_insert_of_notMem hniE2, Finset.card_insert_of_notMem hniO1]
        omega
      · -- lo+m odd ⇒ lo+m+1 even, lo+m+2 odd
        have hm2 : (lo + m) % 2 = 1 := by rw [← Nat.odd_iff]; exact hod
        have hp1 : Even (lo + m + 1) := by rw [Nat.even_iff]; omega
        have hp1' : ¬ Odd (lo + m + 1) := by rw [Nat.odd_iff]; omega
        have hp2 : Odd (lo + m + 2) := by rw [Nat.odd_iff]; omega
        have hp2' : ¬ Even (lo + m + 2) := by rw [Nat.even_iff]; omega
        rw [if_neg hp2', if_pos hp2, if_pos hp1, if_neg hp1']
        rw [Finset.card_insert_of_notMem hniE1, Finset.card_insert_of_notMem hniO2]
        omega

/-- Generalization of `card_even_odd_diff_le_one` to multiples of an odd `d`: in any
interval `Icc a b`, the count of multiples of `d` that are even and the count that are
odd differ by at most `1`. Proved via the parity-preserving bijection `i ↦ i / d` (valid
because `d` is odd, so `i` and `i / d` always share parity when `d ∣ i`) between
`{i ∈ Icc a b : d ∣ i}` and the quotient interval `Icc ⌈a/d⌉ ⌊b/d⌋`, reducing directly to
`card_even_odd_diff_le_one`. -/
theorem card_even_odd_diff_le_one_multiples (d a b : ℕ) (hd : Odd d) :
    ((Finset.Icc a b).filter (fun i => d ∣ i ∧ Even i)).card ≤
      ((Finset.Icc a b).filter (fun i => d ∣ i ∧ Odd i)).card + 1 ∧
    ((Finset.Icc a b).filter (fun i => d ∣ i ∧ Odd i)).card ≤
      ((Finset.Icc a b).filter (fun i => d ∣ i ∧ Even i)).card + 1 := by
  have hdpos : 0 < d := hd.pos
  set lo := (a + d - 1) / d with hlo
  set hi := b / d with hhi
  have hcardE : ((Finset.Icc a b).filter (fun i => d ∣ i ∧ Even i)).card
      = ((Finset.Icc lo hi).filter (fun k => Even k)).card := by
    apply Finset.card_bij (fun i _ => i / d)
    · intro i hi'
      simp only [Finset.mem_filter, Finset.mem_Icc] at hi'
      obtain ⟨⟨ha, hb⟩, hdvd, hev⟩ := hi'
      simp only [Finset.mem_filter, Finset.mem_Icc]
      refine ⟨⟨?_, ?_⟩, ?_⟩
      · rw [hlo]
        have h1 : (a + d - 1) / d ≤ (i + d - 1) / d := Nat.div_le_div_right (by omega)
        have h2 : (i + d - 1) / d = i / d := by
          obtain ⟨k, hk⟩ := hdvd
          subst hk
          rw [Nat.mul_div_cancel_left k hdpos]
          have heq : d * k + d - 1 = (d - 1) + d * k := by omega
          rw [heq, Nat.add_mul_div_left (d - 1) k hdpos]
          have hlt : (d - 1) / d = 0 := Nat.div_eq_of_lt (by omega)
          omega
        omega
      · rw [hhi]; exact Nat.div_le_div_right hb
      · obtain ⟨k, hk⟩ := hdvd
        subst hk
        rw [Nat.mul_div_cancel_left k hdpos]
        rw [Nat.even_mul] at hev
        rcases hev with hev | hev
        · exfalso; rw [Nat.even_iff] at hev; rw [Nat.odd_iff] at hd; omega
        · exact hev
    · intro i1 h1 i2 h2 heq
      simp only [Finset.mem_filter, Finset.mem_Icc] at h1 h2
      obtain ⟨⟨_, _⟩, hdvd1, _⟩ := h1
      obtain ⟨⟨_, _⟩, hdvd2, _⟩ := h2
      obtain ⟨k1, hk1⟩ := hdvd1
      obtain ⟨k2, hk2⟩ := hdvd2
      subst hk1; subst hk2
      rw [Nat.mul_div_cancel_left k1 hdpos, Nat.mul_div_cancel_left k2 hdpos] at heq
      rw [heq]
    · intro k hk'
      simp only [Finset.mem_filter, Finset.mem_Icc] at hk'
      obtain ⟨⟨hklo, hkhi⟩, hev⟩ := hk'
      refine ⟨d * k, ?_, ?_⟩
      · simp only [Finset.mem_filter, Finset.mem_Icc]
        refine ⟨⟨?_, ?_⟩, ⟨k, rfl⟩, ?_⟩
        · rw [hlo, Nat.div_le_iff_le_mul_add_pred hdpos] at hklo
          omega
        · rw [hhi] at hkhi
          rw [Nat.le_div_iff_mul_le hdpos] at hkhi
          rw [mul_comm] at hkhi
          omega
        · rw [Nat.even_mul]; right; exact hev
      · rw [Nat.mul_div_cancel_left k hdpos]
  have hcardO : ((Finset.Icc a b).filter (fun i => d ∣ i ∧ Odd i)).card
      = ((Finset.Icc lo hi).filter (fun k => Odd k)).card := by
    apply Finset.card_bij (fun i _ => i / d)
    · intro i hi'
      simp only [Finset.mem_filter, Finset.mem_Icc] at hi'
      obtain ⟨⟨ha, hb⟩, hdvd, hod⟩ := hi'
      simp only [Finset.mem_filter, Finset.mem_Icc]
      refine ⟨⟨?_, ?_⟩, ?_⟩
      · rw [hlo]
        have h1 : (a + d - 1) / d ≤ (i + d - 1) / d := Nat.div_le_div_right (by omega)
        have h2 : (i + d - 1) / d = i / d := by
          obtain ⟨k, hk⟩ := hdvd
          subst hk
          rw [Nat.mul_div_cancel_left k hdpos]
          have heq : d * k + d - 1 = (d - 1) + d * k := by omega
          rw [heq, Nat.add_mul_div_left (d - 1) k hdpos]
          have hlt : (d - 1) / d = 0 := Nat.div_eq_of_lt (by omega)
          omega
        omega
      · rw [hhi]; exact Nat.div_le_div_right hb
      · obtain ⟨k, hk⟩ := hdvd
        subst hk
        rw [Nat.mul_div_cancel_left k hdpos]
        rw [Nat.odd_mul] at hod
        exact hod.2
    · intro i1 h1 i2 h2 heq
      simp only [Finset.mem_filter, Finset.mem_Icc] at h1 h2
      obtain ⟨⟨_, _⟩, hdvd1, _⟩ := h1
      obtain ⟨⟨_, _⟩, hdvd2, _⟩ := h2
      obtain ⟨k1, hk1⟩ := hdvd1
      obtain ⟨k2, hk2⟩ := hdvd2
      subst hk1; subst hk2
      rw [Nat.mul_div_cancel_left k1 hdpos, Nat.mul_div_cancel_left k2 hdpos] at heq
      rw [heq]
    · intro k hk'
      simp only [Finset.mem_filter, Finset.mem_Icc] at hk'
      obtain ⟨⟨hklo, hkhi⟩, hod⟩ := hk'
      refine ⟨d * k, ?_, ?_⟩
      · simp only [Finset.mem_filter, Finset.mem_Icc]
        refine ⟨⟨?_, ?_⟩, ⟨k, rfl⟩, ?_⟩
        · rw [hlo, Nat.div_le_iff_le_mul_add_pred hdpos] at hklo
          omega
        · rw [hhi] at hkhi
          rw [Nat.le_div_iff_mul_le hdpos] at hkhi
          rw [mul_comm] at hkhi
          omega
        · rw [Nat.odd_mul]; exact ⟨hd, hod⟩
      · rw [Nat.mul_div_cancel_left k hdpos]
  rw [hcardE, hcardO]
  exact card_even_odd_diff_le_one lo hi

/-! ## Stage D (continued) — the prime-power valuation assembly, DIV, and RL -/

theorem factorization_prod_eq_sum_card {p : ℕ} (hp : p.Prime) (s : Finset ℕ)
    (hs : ∀ x ∈ s, x ≠ 0) (b : ℕ) (hb : ∀ x ∈ s, Nat.log p x < b) :
    (∏ x ∈ s, x).factorization p = ∑ i ∈ Finset.Ico 1 b, (s.filter (p ^ i ∣ ·)).card := by
  have step1 : ∀ x ∈ s, x.factorization p
      = ((Finset.Ico 1 b).filter (fun i => p ^ i ∣ x)).card := by
    intro x hx
    exact Nat.factorization_eq_card_pow_dvd_of_lt hp (Nat.pos_of_ne_zero (hs x hx))
      (Nat.lt_pow_of_log_lt hp.one_lt (hb x hx))
  calc (∏ x ∈ s, x).factorization p
      = ∑ x ∈ s, x.factorization p := Nat.factorization_prod_apply hs
    _ = ∑ x ∈ s, ((Finset.Ico 1 b).filter (fun i => p ^ i ∣ x)).card :=
        Finset.sum_congr rfl step1
    _ = ∑ x ∈ s, ∑ i ∈ Finset.Ico 1 b, (if p ^ i ∣ x then 1 else 0) := by
        simp_rw [Finset.card_filter]
    _ = ∑ i ∈ Finset.Ico 1 b, ∑ x ∈ s, (if p ^ i ∣ x then 1 else 0) := Finset.sum_comm
    _ = ∑ i ∈ Finset.Ico 1 b, (s.filter (p ^ i ∣ ·)).card := by
        simp_rw [Finset.card_filter]

/-- The `Num` product reindexed as a product over the "opposite-parity-to-`j+1`" filter of
`Icc (j+1) n`. -/
theorem endpointNum_eq_prod_filter (n j : ℕ) (hj : j < n) (hodd : Odd (n - j)) :
    endpointNum n j = ∏ i ∈ (Finset.Icc (j + 1) n).filter (fun i => i % 2 = j % 2), i := by
  unfold endpointNum
  obtain ⟨k, hk⟩ := hodd
  have hQ : endpointQ n j = k := by unfold endpointQ; omega
  rw [hQ]
  have hinj : Set.InjOn (fun t => j + 2 + 2 * t) (Finset.range k : Finset ℕ) := by
    intro a _ b _ hab
    simp only at hab; omega
  have himg := Finset.prod_image (f := (id : ℕ → ℕ)) (g := fun t => j + 2 + 2 * t) hinj
  simp only [id] at himg
  rw [← himg]
  congr 1
  ext i
  simp only [Finset.mem_image, Finset.mem_range, Finset.mem_filter, Finset.mem_Icc]
  constructor
  · rintro ⟨t, ht, rfl⟩
    refine ⟨⟨by omega, by omega⟩, by omega⟩
  · rintro ⟨⟨h1, h2⟩, hpar⟩
    refine ⟨(i - j - 2) / 2, ?_, ?_⟩ <;> omega

/-- The `Den` product reindexed as a product over the "same-parity-as-`j+1`" filter of
`Icc (j+1) n`. -/
theorem endpointDen_eq_prod_filter (n j : ℕ) (hj : j < n) (hodd : Odd (n - j)) :
    endpointDen n j = ∏ i ∈ (Finset.Icc (j + 1) n).filter (fun i => i % 2 = (j + 1) % 2), i := by
  unfold endpointDen
  obtain ⟨k, hk⟩ := hodd
  have hQ : endpointQ n j = k := by unfold endpointQ; omega
  rw [hQ]
  have hinj : Set.InjOn (fun t => j + 1 + 2 * t) (Finset.range (k + 1) : Finset ℕ) := by
    intro a _ b _ hab
    simp only at hab; omega
  have himg := Finset.prod_image (f := (id : ℕ → ℕ)) (g := fun t => j + 1 + 2 * t) hinj
  simp only [id] at himg
  rw [← himg]
  congr 1
  ext i
  simp only [Finset.mem_image, Finset.mem_range, Finset.mem_filter, Finset.mem_Icc]
  constructor
  · rintro ⟨t, ht, rfl⟩
    refine ⟨⟨by omega, by omega⟩, by omega⟩
  · rintro ⟨⟨h1, h2⟩, hpar⟩
    refine ⟨(i - j - 1) / 2, ?_, ?_⟩ <;> omega
/-- The per-`(p,i)` parity-class card bound: the `Den`-parity-class count of multiples of
`p^i` in `Icc (j+1) n` exceeds the `Num`-parity-class count by at most `1`. -/
theorem den_num_card_bound (p i n j : ℕ) (hpodd : Odd p) :
    (((Finset.Icc (j + 1) n).filter (fun x => x % 2 = (j + 1) % 2)).filter
        (p ^ i ∣ ·)).card ≤
    (((Finset.Icc (j + 1) n).filter (fun x => x % 2 = j % 2)).filter (p ^ i ∣ ·)).card + 1 := by
  rw [Finset.filter_filter, Finset.filter_filter]
  have hdodd : Odd (p ^ i) := hpodd.pow
  have hcard := card_even_odd_diff_le_one_multiples (p ^ i) (j + 1) n hdodd
  rcases Nat.even_or_odd j with hje | hjo
  · have e1 : (Finset.Icc (j + 1) n).filter (fun x => x % 2 = (j + 1) % 2 ∧ p ^ i ∣ x)
        = (Finset.Icc (j + 1) n).filter (fun x => p ^ i ∣ x ∧ Odd x) := by
      apply Finset.filter_congr
      intro x _
      have hj1 : (j + 1) % 2 = 1 := by rw [Nat.even_iff] at hje; omega
      rw [hj1, Nat.odd_iff]
      exact ⟨fun h => ⟨h.2, h.1⟩, fun h => ⟨h.2, h.1⟩⟩
    have e2 : (Finset.Icc (j + 1) n).filter (fun x => x % 2 = j % 2 ∧ p ^ i ∣ x)
        = (Finset.Icc (j + 1) n).filter (fun x => p ^ i ∣ x ∧ Even x) := by
      apply Finset.filter_congr
      intro x _
      have hj0 : j % 2 = 0 := Nat.even_iff.mp hje
      rw [hj0, Nat.even_iff]
      exact ⟨fun h => ⟨h.2, h.1⟩, fun h => ⟨h.2, h.1⟩⟩
    rw [e1, e2]
    exact hcard.2
  · have e1 : (Finset.Icc (j + 1) n).filter (fun x => x % 2 = (j + 1) % 2 ∧ p ^ i ∣ x)
        = (Finset.Icc (j + 1) n).filter (fun x => p ^ i ∣ x ∧ Even x) := by
      apply Finset.filter_congr
      intro x _
      have hj0 : (j + 1) % 2 = 0 := by rw [Nat.odd_iff] at hjo; omega
      rw [hj0, Nat.even_iff]
      exact ⟨fun h => ⟨h.2, h.1⟩, fun h => ⟨h.2, h.1⟩⟩
    have e2 : (Finset.Icc (j + 1) n).filter (fun x => x % 2 = j % 2 ∧ p ^ i ∣ x)
        = (Finset.Icc (j + 1) n).filter (fun x => p ^ i ∣ x ∧ Odd x) := by
      apply Finset.filter_congr
      intro x _
      have hj1 : j % 2 = 1 := Nat.odd_iff.mp hjo
      rw [hj1, Nat.odd_iff]
      exact ⟨fun h => ⟨h.2, h.1⟩, fun h => ⟨h.2, h.1⟩⟩
    rw [e1, e2]
    exact hcard.1

/-- For an odd prime `p`, the `p`-adic valuation of `endpointDen n j` exceeds that of
`endpointNum n j` by at most `p.log n` — the exact valuation of `Nat.lcmUpto n` at `p`. -/
theorem endpointDen_val_le_odd (p n j : ℕ) (hp : p.Prime) (hpodd : Odd p)
    (hj : j < n) (hodd : Odd (n - j)) :
    (endpointDen n j).factorization p ≤ (endpointNum n j).factorization p + p.log n := by
  rw [endpointDen_eq_prod_filter n j hj hodd, endpointNum_eq_prod_filter n j hj hodd]
  set b := p.log n + 1 with hb
  have hsD : ∀ x ∈ (Finset.Icc (j + 1) n).filter (fun x => x % 2 = (j + 1) % 2), x ≠ 0 := by
    intro x hx; simp only [Finset.mem_filter, Finset.mem_Icc] at hx; omega
  have hsN : ∀ x ∈ (Finset.Icc (j + 1) n).filter (fun x => x % 2 = j % 2), x ≠ 0 := by
    intro x hx; simp only [Finset.mem_filter, Finset.mem_Icc] at hx; omega
  have hbD : ∀ x ∈ (Finset.Icc (j + 1) n).filter (fun x => x % 2 = (j + 1) % 2),
      Nat.log p x < b := by
    intro x hx
    simp only [Finset.mem_filter, Finset.mem_Icc] at hx
    exact lt_of_le_of_lt (Nat.log_mono_right hx.1.2) (by omega)
  have hbN : ∀ x ∈ (Finset.Icc (j + 1) n).filter (fun x => x % 2 = j % 2),
      Nat.log p x < b := by
    intro x hx
    simp only [Finset.mem_filter, Finset.mem_Icc] at hx
    exact lt_of_le_of_lt (Nat.log_mono_right hx.1.2) (by omega)
  rw [factorization_prod_eq_sum_card hp _ hsD b hbD,
      factorization_prod_eq_sum_card hp _ hsN b hbN]
  have hpt : ∀ i ∈ Finset.Ico 1 b,
      (((Finset.Icc (j + 1) n).filter (fun x => x % 2 = (j + 1) % 2)).filter (p ^ i ∣ ·)).card
        ≤ (((Finset.Icc (j + 1) n).filter (fun x => x % 2 = j % 2)).filter (p ^ i ∣ ·)).card
          + 1 :=
    fun i _ => den_num_card_bound p i n j hpodd
  calc ∑ i ∈ Finset.Ico 1 b,
        (((Finset.Icc (j + 1) n).filter (fun x => x % 2 = (j + 1) % 2)).filter
          (p ^ i ∣ ·)).card
      ≤ ∑ i ∈ Finset.Ico 1 b,
        ((((Finset.Icc (j + 1) n).filter (fun x => x % 2 = j % 2)).filter (p ^ i ∣ ·)).card
          + 1) := Finset.sum_le_sum hpt
    _ = (∑ i ∈ Finset.Ico 1 b,
          (((Finset.Icc (j + 1) n).filter (fun x => x % 2 = j % 2)).filter (p ^ i ∣ ·)).card)
        + (Finset.Ico 1 b).card := by rw [Finset.sum_add_distrib]; simp
    _ = _ := by rw [Nat.card_Ico]; omega

theorem endpointDen_dvd_factorial (n j : ℕ) (hj : j < n) (hodd : Odd (n - j)) :
    endpointDen n j ∣ Nat.factorial n := by
  rw [endpointDen_eq_prod_filter n j hj hodd, ← Finset.prod_Ico_id_eq_factorial n]
  apply Finset.prod_dvd_prod_of_subset
  intro x hx
  simp only [Finset.mem_filter, Finset.mem_Icc] at hx
  simp only [Finset.mem_Ico]
  omega

theorem endpointDen_val_le_two (n j : ℕ) (hj : j < n) (hodd : Odd (n - j)) :
    (endpointDen n j).factorization 2 ≤ n - 1 := by
  have hdvd := endpointDen_dvd_factorial n j hj hodd
  have hnfac : Nat.factorial n ≠ 0 := Nat.factorial_ne_zero n
  have hden : endpointDen n j ≠ 0 := by
    unfold endpointDen
    apply Finset.prod_ne_zero_iff.mpr
    intro t _; omega
  have hle : (endpointDen n j).factorization ≤ (Nat.factorial n).factorization :=
    (Nat.factorization_le_iff_dvd hden hnfac).mpr hdvd
  have hle2 : (endpointDen n j).factorization 2 ≤ (Nat.factorial n).factorization 2 := hle 2
  have hne0 : n ≠ 0 := by omega
  have hdignz : Nat.digits 2 n ≠ [] := Nat.digits_ne_nil_iff_ne_zero.mpr hne0
  have hlast : (Nat.digits 2 n).getLast hdignz ≠ 0 := Nat.getLast_digit_ne_zero 2 hne0
  have hmem : (Nat.digits 2 n).getLast hdignz ∈ Nat.digits 2 n := List.getLast_mem hdignz
  have hsum1 : 1 ≤ (Nat.digits 2 n).sum := by
    have h1 : 1 ≤ (Nat.digits 2 n).getLast hdignz := Nat.one_le_iff_ne_zero.mpr hlast
    exact h1.trans (List.single_le_sum (by intro x _; omega) _ hmem)
  have hval : (2 - 1) * (Nat.factorial n).factorization 2 = n - (Nat.digits 2 n).sum :=
    Nat.sub_one_mul_factorization_factorial (by norm_num)
  norm_num at hval
  omega

/-- **DIV.** The key natural-number denominator divisibility. -/
theorem endpointDen_dvd (n j : ℕ) (hj : j < n) (hodd : Odd (n - j)) :
    endpointDen n j ∣ 2 ^ (n - 1) * Nat.lcmUpto n * endpointNum n j := by
  have hDenNe : endpointDen n j ≠ 0 := by
    unfold endpointDen; apply Finset.prod_ne_zero_iff.mpr; intro t _; omega
  have hNumNe : endpointNum n j ≠ 0 := by
    unfold endpointNum; apply Finset.prod_ne_zero_iff.mpr; intro t _; omega
  have h2powNe : (2 : ℕ) ^ (n - 1) ≠ 0 := by positivity
  have hlcmNe : Nat.lcmUpto n ≠ 0 := Nat.lcmUpto_ne_zero n
  have hRHSNe : (2 : ℕ) ^ (n - 1) * Nat.lcmUpto n * endpointNum n j ≠ 0 :=
    mul_ne_zero (mul_ne_zero h2powNe hlcmNe) hNumNe
  rw [← Nat.factorization_le_iff_dvd hDenNe hRHSNe, Finsupp.le_def]
  intro p
  by_cases hp : p.Prime
  · have hfac : ((2 : ℕ) ^ (n - 1) * Nat.lcmUpto n * endpointNum n j).factorization p
        = (2 ^ (n - 1)).factorization p + (Nat.lcmUpto n).factorization p
          + (endpointNum n j).factorization p := by
      rw [Nat.factorization_mul (mul_ne_zero h2powNe hlcmNe) hNumNe,
          Nat.factorization_mul h2powNe hlcmNe]
      simp
    rw [hfac]
    by_cases hp2 : p = 2
    · subst hp2
      have h1 : ((2 : ℕ) ^ (n - 1)).factorization 2 = n - 1 := by
        rw [Nat.factorization_pow]
        simp [Nat.Prime.factorization_self (p := 2) (by norm_num)]
      have hb := endpointDen_val_le_two n j hj hodd
      omega
    · have hpodd : Odd p := hp.odd_of_ne_two hp2
      have hndvd : ¬ p ∣ (2 : ℕ) := by
        intro hdvd
        exact hp2 ((Nat.prime_dvd_prime_iff_eq hp (by norm_num)).mp hdvd)
      have h1 : ((2 : ℕ) ^ (n - 1)).factorization p = 0 := by
        rw [Nat.factorization_pow]
        simp [Nat.factorization_eq_zero_of_not_dvd hndvd]
      have hb := endpointDen_val_le_odd p n j hp hpodd hj hodd
      rw [Nat.factorization_lcmUpto n hp]
      omega
  · simp [Nat.factorization_eq_zero_of_not_prime _ hp]
/-- **RL.** Casting `DIV` to `ℚ`. -/
theorem endpointR_lcm_integral (n j : ℕ) (hj : j < n) (hodd : Odd (n - j)) :
    ∃ z : ℤ, (Nat.lcmUpto n : ℚ) * endpointR n j = z := by
  obtain ⟨c, hc⟩ := endpointDen_dvd n j hj hodd
  refine ⟨(c : ℤ), ?_⟩
  have hDenNe : (endpointDen n j : ℚ) ≠ 0 := by
    have : endpointDen n j ≠ 0 := by
      unfold endpointDen; apply Finset.prod_ne_zero_iff.mpr; intro t _; omega
    exact_mod_cast this
  have hcQ : (2 : ℚ) ^ (n - 1) * Nat.lcmUpto n * endpointNum n j
      = endpointDen n j * c := by exact_mod_cast hc
  unfold endpointR
  push_cast
  field_simp
  linear_combination hcQ

/-! ## Stage E — sharp integrality -/

/-- Rational numbers of the form `(z : ℚ)` are closed under finite sums indexed by a
`Finset`. -/
theorem ratInt_sum {α : Type*} (s : Finset α) (g : α → ℚ)
    (h : ∀ x ∈ s, ∃ z : ℤ, g x = (z : ℚ)) : ∃ z : ℤ, ∑ x ∈ s, g x = (z : ℚ) := by
  classical
  induction s using Finset.induction with
  | empty => exact ⟨0, by simp⟩
  | insert a s ha ih =>
      obtain ⟨za, hza⟩ := h a (Finset.mem_insert_self a s)
      obtain ⟨zs, hzs⟩ := ih (fun x hx => h x (Finset.mem_insert_of_mem hx))
      exact ⟨za + zs, by rw [Finset.sum_insert ha, hza, hzs]; push_cast; ring⟩

/-- `(lcmUpto n)^2 * catalanSumR n` is an integer. -/
theorem catalanSumR_lcm_sq_integral (n : ℕ) :
    ∃ z : ℤ, (Nat.lcmUpto n : ℚ) ^ 2 * catalanSumR n = z := by
  unfold catalanSumR
  rw [Finset.mul_sum]
  apply ratInt_sum
  intro j hj
  by_cases hodd : Odd (n - j)
  · have hjlt : j < n := Finset.mem_range.mp hj
    obtain ⟨z, hz⟩ := endpointR_lcm_integral n j hjlt hodd
    refine ⟨z ^ 2, ?_⟩
    simp only [hodd, if_true]
    have : (Nat.lcmUpto n : ℚ) ^ 2 * endpointR n j ^ 2
        = ((Nat.lcmUpto n : ℚ) * endpointR n j) ^ 2 := by ring
    rw [this, hz]
    push_cast; ring
  · exact ⟨0, by simp [hodd]⟩

/-- **SHARP for `T`.** `(lcmUpto n)^2 * catalanT n` is an integer. -/
theorem catalanT_lcm_sq_integral (n : ℕ) :
    ∃ z : ℤ, (Nat.lcmUpto n : ℚ) ^ 2 * catalanT n = z := by
  match n with
  | 0 => exact ⟨0, by simp⟩
  | (m + 1) =>
      have htsq := catalanT_square_formula (m + 1) (by omega)
      obtain ⟨z, hz⟩ := catalanSumR_lcm_sq_integral (m + 1)
      refine ⟨(-1) ^ (m + 1 - 1) * z, ?_⟩
      have hsign : ((-1 : ℚ) ^ (m + 1 - 1)) * ((-1 : ℚ) ^ (m + 1 - 1)) = 1 := by
        rw [← mul_pow]; norm_num
      have hTeq : catalanT (m + 1) = (-1 : ℚ) ^ (m + 1 - 1) * catalanSumR (m + 1) := by
        have h2 : (-1 : ℚ) ^ (m + 1 - 1) * ((-1 : ℚ) ^ (m + 1 - 1) * catalanT (m + 1))
            = (-1 : ℚ) ^ (m + 1 - 1) * catalanSumR (m + 1) := by rw [htsq]
        rw [← mul_assoc, hsign, one_mul] at h2
        exact h2
      rw [hTeq]
      push_cast
      rw [show (Nat.lcmUpto (m + 1) : ℚ) ^ 2 * ((-1 : ℚ) ^ m * catalanSumR (m + 1))
          = (-1 : ℚ) ^ m * ((Nat.lcmUpto (m + 1) : ℚ) ^ 2 * catalanSumR (m + 1)) from
          by ring, hz]

/-- `Nat.lcmUpto` is monotone: `lcmUpto k ∣ lcmUpto n` for `k ≤ n`. -/
theorem lcmUpto_dvd_lcmUpto {k n : ℕ} (hkn : k ≤ n) : Nat.lcmUpto k ∣ Nat.lcmUpto n := by
  unfold Nat.lcmUpto
  apply Finset.lcm_dvd
  intro b hb
  simp only [Finset.mem_Icc] at hb
  apply Finset.dvd_lcm
  simp only [Finset.mem_Icc]
  omega

theorem filter_range_le_eq_range (m N : ℕ) (hmN : m ≤ N) :
    (Finset.range (N + 1)).filter (fun i => i ≤ m) = Finset.range (m + 1) := by
  ext i
  simp only [Finset.mem_filter, Finset.mem_range]
  omega

theorem sum_range_succ_eq_sum_ite (m N : ℕ) (hmN : m ≤ N) (g : ℕ → ℚ) :
    ∑ i ∈ Finset.range (m + 1), g i
      = ∑ i ∈ Finset.range (N + 1), (if i ≤ m then g i else 0) := by
  rw [← Finset.sum_filter, filter_range_le_eq_range m N hmN]

theorem filter_range_ge_eq_Ico (i N : ℕ) (hiN : i ≤ N + 1) :
    (Finset.range (N + 1)).filter (fun k => i ≤ k) = Finset.Ico i (N + 1) := by
  ext k
  simp only [Finset.mem_filter, Finset.mem_range, Finset.mem_Ico]
  omega

/-- Swapping a triangular double sum over `Finset.range`. -/
theorem sum_range_triangle_swap (n : ℕ) (f : ℕ → ℕ → ℚ) :
    ∑ k ∈ Finset.range (n + 1), ∑ i ∈ Finset.range (k + 1), f k i
      = ∑ i ∈ Finset.range (n + 1), ∑ k ∈ Finset.Ico i (n + 1), f k i := by
  have h1 : ∀ k ∈ Finset.range (n + 1),
      ∑ i ∈ Finset.range (k + 1), f k i
        = ∑ i ∈ Finset.range (n + 1), (if i ≤ k then f k i else 0) := by
    intro k hk
    have hkn : k ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
    exact sum_range_succ_eq_sum_ite k n hkn (f k)
  rw [Finset.sum_congr rfl h1, Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro i hi
  have hiN : i ≤ n + 1 := by have := Finset.mem_range.mp hi; omega
  rw [← Finset.sum_filter, filter_range_ge_eq_Ico i n hiN]

/-- Vandermonde-style collapse: for `i ≤ n`, `∑_{k=i}^n C(n,k)C(k,i) c^{n-k}(-c)^{k-i}` is
`0` unless `i = n`, in which case it is `1`. Proved via `Nat.choose_mul` (Vandermonde) to
reindex the inner sum into a plain binomial expansion of `((-c) + c) ^ (n - i) = 0`. -/
theorem inner_sum_collapse (n i : ℕ) (hin : i ≤ n) (c : ℚ) :
    ∑ k ∈ Finset.Ico i (n + 1),
        (n.choose k : ℚ) * c ^ (n - k) * ((k.choose i : ℚ) * (-c) ^ (k - i))
      = if i = n then 1 else 0 := by
  have hreindex : ∑ k ∈ Finset.Ico i (n + 1),
        (n.choose k : ℚ) * c ^ (n - k) * ((k.choose i : ℚ) * (-c) ^ (k - i))
      = ∑ j ∈ Finset.range (n - i + 1),
        (n.choose i : ℚ) * ((n - i).choose j : ℚ) * c ^ (n - i - j) * (-c) ^ j := by
    rw [Finset.sum_Ico_eq_sum_range]
    have hlen : n + 1 - i = n - i + 1 := by omega
    rw [hlen]
    apply Finset.sum_congr rfl
    intro j hj
    simp only [Finset.mem_range] at hj
    have hchoose : (n.choose (i + j) : ℚ) * ((i + j).choose i : ℚ)
        = (n.choose i : ℚ) * ((n - i).choose j : ℚ) := by
      have := Nat.choose_mul (n := n) (k := i + j) (s := i) (by omega)
      have heq : i + j - i = j := by omega
      rw [heq] at this
      exact_mod_cast this
    have hnk : n - (i + j) = n - i - j := by omega
    have hkis : i + j - i = j := by omega
    rw [hnk, hkis]
    have : (n.choose (i + j) : ℚ) * c ^ (n - i - j) * (((i + j).choose i : ℚ) * (-c) ^ j)
        = ((n.choose (i + j) : ℚ) * ((i + j).choose i : ℚ)) * c ^ (n - i - j) * (-c) ^ j := by
      ring
    rw [this, hchoose]
  rw [hreindex]
  have hbin0 : ((-c) + c) ^ (n - i)
      = ∑ j ∈ Finset.range (n - i + 1), (-c) ^ j * c ^ (n - i - j) * ((n - i).choose j : ℚ) :=
    add_pow (-c) c (n - i)
  have hbin : ∑ j ∈ Finset.range (n - i + 1),
      (n - i).choose j * c ^ (n - i - j) * (-c) ^ j = (0 : ℚ) ^ (n - i) := by
    have hz : ((-c) + c) = (0 : ℚ) := by ring
    rw [hz] at hbin0
    rw [hbin0]
    apply Finset.sum_congr rfl
    intro j _
    ring
  have hfact : ∑ j ∈ Finset.range (n - i + 1),
        (n.choose i : ℚ) * ((n - i).choose j : ℚ) * c ^ (n - i - j) * (-c) ^ j
      = (n.choose i : ℚ) * ∑ j ∈ Finset.range (n - i + 1),
          ((n - i).choose j : ℚ) * c ^ (n - i - j) * (-c) ^ j := by
    rw [Finset.mul_sum]; apply Finset.sum_congr rfl; intro j _; ring
  rw [hfact]
  by_cases hie : i = n
  · subst hie
    simp
  · have h0pow : (0 : ℚ) ^ (n - i) = 0 := zero_pow (by omega)
    rw [h0pow] at hbin
    rw [hbin, mul_zero]
    simp [hie]

/-- General binomial inversion: if `T k = ∑_{i≤k} C(k,i) (-c)^{k-i} B i` for all `k`, then
`∑_{k≤n} C(n,k) c^{n-k} T k = B n` for all `n`. -/
theorem binom_inv_general (B T : ℕ → ℚ) (c : ℚ)
    (hT : ∀ k, T k = ∑ i ∈ Finset.range (k + 1), (k.choose i : ℚ) * (-c) ^ (k - i) * B i)
    (n : ℕ) :
    ∑ k ∈ Finset.range (n + 1), (n.choose k : ℚ) * c ^ (n - k) * T k = B n := by
  have hexp : ∑ k ∈ Finset.range (n + 1), (n.choose k : ℚ) * c ^ (n - k) * T k
      = ∑ k ∈ Finset.range (n + 1), ∑ i ∈ Finset.range (k + 1),
          (n.choose k : ℚ) * c ^ (n - k) * ((k.choose i : ℚ) * (-c) ^ (k - i) * B i) := by
    apply Finset.sum_congr rfl
    intro k _
    rw [hT k, Finset.mul_sum]
  rw [hexp, sum_range_triangle_swap n
      (fun k i => (n.choose k : ℚ) * c ^ (n - k) * ((k.choose i : ℚ) * (-c) ^ (k - i) * B i))]
  have hswapinner : ∀ i ∈ Finset.range (n + 1),
      ∑ k ∈ Finset.Ico i (n + 1),
          (n.choose k : ℚ) * c ^ (n - k) * ((k.choose i : ℚ) * (-c) ^ (k - i) * B i)
        = (∑ k ∈ Finset.Ico i (n + 1),
            (n.choose k : ℚ) * c ^ (n - k) * ((k.choose i : ℚ) * (-c) ^ (k - i))) * B i := by
    intro i _
    rw [Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro k _
    ring
  rw [Finset.sum_congr rfl hswapinner]
  have hcollapse : ∀ i ∈ Finset.range (n + 1),
      (∑ k ∈ Finset.Ico i (n + 1),
          (n.choose k : ℚ) * c ^ (n - k) * ((k.choose i : ℚ) * (-c) ^ (k - i))) * B i
        = (if i = n then 1 else 0) * B i := by
    intro i hi
    have hin : i ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hi)
    rw [inner_sum_collapse n i hin c]
  rw [Finset.sum_congr rfl hcollapse]
  have hite : ∀ i, (if i = n then (1 : ℚ) else 0) * B i = if i = n then B i else 0 := by
    intro i; by_cases h : i = n <;> simp [h]
  simp_rw [hite]
  rw [Finset.sum_ite_eq' (Finset.range (n + 1)) n B]
  simp

/-- **INV.** Binomial inversion recovering `catalanB` from `catalanT`. -/
theorem catalan_binomial_inversion (n : ℕ) :
    catalanB n = ∑ k ∈ Finset.range (n + 1), (n.choose k : ℚ) * (4 : ℚ) ^ (n - k) * catalanT k :=
  (binom_inv_general catalanB catalanT 4 (fun _ => rfl) n).symm

/-- **SHARP.** The primary target: `(lcmUpto n)^2 * catalanB n` is an integer for every
`n`. -/
theorem catalanB_sharp_denominator (n : ℕ) :
    ∃ z : ℤ, (Nat.lcmUpto n : ℚ) ^ 2 * catalanB n = z := by
  rw [catalan_binomial_inversion n, Finset.mul_sum]
  apply ratInt_sum
  intro k hk
  have hkn : k ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
  obtain ⟨zk, hzk⟩ := catalanT_lcm_sq_integral k
  obtain ⟨m, hm⟩ := lcmUpto_dvd_lcmUpto hkn
  refine ⟨(n.choose k : ℤ) * 4 ^ (n - k) * m ^ 2 * zk, ?_⟩
  have hlcm : (Nat.lcmUpto n : ℚ) = (Nat.lcmUpto k : ℚ) * (m : ℚ) := by exact_mod_cast hm
  have hrw : (Nat.lcmUpto n : ℚ) ^ 2 * ((n.choose k : ℚ) * (4 : ℚ) ^ (n - k) * catalanT k)
      = (n.choose k : ℚ) * (4 : ℚ) ^ (n - k) * (m : ℚ) ^ 2
        * ((Nat.lcmUpto k : ℚ) ^ 2 * catalanT k) := by
    rw [hlcm]; ring
  rw [hrw, hzk]
  push_cast
  ring


end ZetaLucas
