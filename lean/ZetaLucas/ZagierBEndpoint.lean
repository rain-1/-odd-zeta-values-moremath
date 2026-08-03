/-
# The Zagier-B step-three companion (partial formalization)

This file begins the formalization of `papers_out/step_q_endpoint/main.tex`,
Theorem `thm:zagB` ("sharp step-three companion theorem"), the recurrence-defined
companion `zagC` for Zagier's sporadic sequence **B**, its binomial transform `zagS`,
and the target sharp integrality statement

  `(∀ n, L_n^2 * zagC h n ∈ ℤ) ↔ 3 ∣ h`

where `L_n = Nat.lcmUpto n`.

**Trust boundary / status (see `work/harmonic_jets/CLAUDE_ZAGIER_B_STATUS.md` for a
live log).**  This file formalizes:

* the recurrence-defined companion `zagC h`, `(n+1)² C_{n+1} = h(3n²+3n+1) C_n − 3h²n² C_{n−1}`,
  with recurrence-uniqueness (`zagC_unique`);
* the binomial transform `zagS h`;
* the two exact finite witnesses used for the **necessity** half and the
  **optimality-of-exponent-2** claim of the theorem (`zagC_six_eq`, `zagC6_forces_three_dvd`,
  `zagC_two_eq`, `zagC2_not_scaled_integral`).

It does **not** yet formalize: the transformed step-three recurrence `TREC`
(`n² S_n + h³(n−2)(n−1) S_{n−3} = (−h)^{n−1}`), the finite endpoint formula, the
prime-power denominator lemmas, or the full sufficiency direction / iff theorem. Those
are open and are *not* claimed anywhere below — no theorem in this file asserts the
full iff, and no universally-quantified claim is discharged by `decide`/`norm_num` on
finitely many cases. Every declaration below is closed with no `sorry`, `admit`, or new
`axiom`.
-/
import Mathlib
import ZetaLucas.CatalanEndpoint

open Finset

namespace ZetaLucas

/-! ## Stage A — the recurrence-defined companion `zagC` -/

/-- **The Zagier-B companion**, defined for a fixed integer parameter `h` by
`(n+1)² C_{n+1} = h(3n²+3n+1) C_n − 3h²n² C_{n−1}`, `C₀ = 0`, `C₁ = 1`. The leading
coefficient `(n+1)² ≠ 0`, so this determines `C_n ∈ ℚ` uniquely. -/
def zagC (h : ℤ) : ℕ → ℚ
  | 0 => 0
  | 1 => 1
  | (n + 2) =>
      (((h : ℚ)) * (3 * ((n : ℚ) + 1) ^ 2 + 3 * ((n : ℚ) + 1) + 1) * zagC h (n + 1)
          - 3 * (h : ℚ) ^ 2 * ((n : ℚ) + 1) ^ 2 * zagC h n)
        / ((n : ℚ) + 2) ^ 2

@[simp] theorem zagC_zero (h : ℤ) : zagC h 0 = 0 := rfl
@[simp] theorem zagC_one (h : ℤ) : zagC h 1 = 1 := rfl

theorem zagC_rec' (h : ℤ) (m : ℕ) :
    ((m : ℚ) + 1 + 1) ^ 2 * zagC h (m + 1 + 1)
      = (h : ℚ) * (3 * ((m : ℚ) + 1) ^ 2 + 3 * ((m : ℚ) + 1) + 1) * zagC h (m + 1)
        - 3 * (h : ℚ) ^ 2 * ((m : ℚ) + 1) ^ 2 * zagC h m := by
  have hne : ((m : ℚ) + 2) ^ 2 ≠ 0 := by positivity
  rw [show zagC h (m + 1 + 1)
      = (((h : ℚ)) * (3 * ((m : ℚ) + 1) ^ 2 + 3 * ((m : ℚ) + 1) + 1) * zagC h (m + 1)
          - 3 * (h : ℚ) ^ 2 * ((m : ℚ) + 1) ^ 2 * zagC h m)
        / ((m : ℚ) + 2) ^ 2 from rfl]
  field_simp
  ring

theorem zagC_rec (h : ℤ) (n : ℕ) (hn : 1 ≤ n) :
    ((n : ℚ) + 1) ^ 2 * zagC h (n + 1)
      = (h : ℚ) * (3 * (n : ℚ) ^ 2 + 3 * (n : ℚ) + 1) * zagC h n
        - 3 * (h : ℚ) ^ 2 * (n : ℚ) ^ 2 * zagC h (n - 1) := by
  obtain ⟨m, rfl⟩ := Nat.exists_eq_add_of_le hn
  rw [add_comm 1 m]
  have := zagC_rec' h m
  simpa using this

/-- **Recurrence uniqueness.**  Any rational sequence satisfying (REC) from `n ≥ 1` and
agreeing with `zagC h` at `0` and `1` agrees with `zagC h` everywhere. -/
theorem zagC_unique (h : ℤ) (f : ℕ → ℚ) (h0 : f 0 = 0) (h1 : f 1 = 1)
    (hrec : ∀ n : ℕ, 1 ≤ n →
      ((n : ℚ) + 1) ^ 2 * f (n + 1)
        = (h : ℚ) * (3 * (n : ℚ) ^ 2 + 3 * (n : ℚ) + 1) * f n
          - 3 * (h : ℚ) ^ 2 * (n : ℚ) ^ 2 * f (n - 1)) :
    ∀ n, f n = zagC h n := by
  have key : ∀ n : ℕ, f n = zagC h n ∧ f (n + 1) = zagC h (n + 1) := by
    intro n
    induction n with
    | zero => exact ⟨h0, h1⟩
    | succ n ih =>
      refine ⟨ih.2, ?_⟩
      obtain ⟨hn0, hn1⟩ := ih
      have hf := hrec (n + 1) (by omega)
      simp only [Nat.add_sub_cancel] at hf
      have hC := zagC_rec' h n
      have hne : ((n : ℚ) + 1 + 1) ^ 2 ≠ 0 := by positivity
      have heq : ((n : ℚ) + 1 + 1) ^ 2 * f (n + 1 + 1)
          = ((n : ℚ) + 1 + 1) ^ 2 * zagC h (n + 1 + 1) := by
        rw [hC, ← hn0, ← hn1]
        push_cast at hf ⊢
        linear_combination hf
      exact mul_left_cancel₀ hne heq
  exact fun n => (key n).1

/-! ## Stage B — the endpoint binomial transform `zagS` -/

/-- **The endpoint binomial transform** of `zagC h`. -/
def zagS (h : ℤ) (n : ℕ) : ℚ :=
  ∑ k ∈ Finset.range (n + 1), (n.choose k : ℚ) * (-(h : ℚ)) ^ (n - k) * zagC h k

@[simp] theorem zagS_zero (h : ℤ) : zagS h 0 = 0 := by
  simp [zagS]

theorem zagS_one (h : ℤ) : zagS h 1 = 1 := by
  simp [zagS, Finset.sum_range_succ, zagC]

/-! ## Stage B, generic weighted shift tower (Ingredient 1 toward TREC)

`genTrC` generalizes `zagS`/CatalanEndpoint.lean's `genTr` to an arbitrary sequence `a`
*and* an arbitrary weight `c` (here `c = -h` will be instantiated), since the
`zagS`-transform's weight `-h` is a parameter, unlike CatalanEndpoint.lean's fixed
weight `-4`. `genTrC_succ` generalizes `genTr_succ`: the proof is the same
peel-and-reindex-forward argument with the literal `-4` replaced by `c` throughout.
This is the mechanical, low-risk first step toward closing `TREC`; the harder
Way-A/Way-B auxiliary-sum closure (four shift levels `V,W,Y,Z`, since `TREC` has a
step-3 lag rather than CatalanEndpoint's step-2 lag) remains open — see the status log.
-/

/-- The endpoint binomial transform of an arbitrary sequence `a` with arbitrary weight
`c`. Specializes to `zagS h n = genTrC (-(h:ℚ)) (zagC h) n`. -/
def genTrC (c : ℚ) (a : ℕ → ℚ) (n : ℕ) : ℚ :=
  ∑ k ∈ Finset.range (n + 1), (n.choose k : ℚ) * c ^ (n - k) * a k

theorem zagS_eq_genTrC (h : ℤ) (n : ℕ) : zagS h n = genTrC (-(h : ℚ)) (zagC h) n := rfl

/-- **Generic weighted Pascal-rule shift.** For any `a : ℕ → ℚ`, `c : ℚ`,
`genTrC c a (m+1) = c · genTrC c a m + genTrC c (a∘succ) m`, with no hypothesis on `a`.
This generalizes CatalanEndpoint.lean's `genTr_succ` (the case `c = -4`). -/
theorem genTrC_succ (c : ℚ) (a : ℕ → ℚ) (m : ℕ) :
    genTrC c a (m + 1) = c * genTrC c a m + genTrC c (fun k => a (k + 1)) m := by
  have hT1 : genTrC c a (m + 1)
      = c ^ (m + 1) * a 0 + ∑ k ∈ Finset.range (m + 1),
          ((m + 1).choose (k + 1) : ℚ) * c ^ (m - k) * a (k + 1) := by
    have h := Finset.sum_range_succ'
      (fun k => ((m + 1).choose k : ℚ) * c ^ (m + 1 - k) * a k) (m + 1)
    simp only [genTrC]
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
      ((m + 1).choose (k + 1) : ℚ) * c ^ (m - k) * a (k + 1)
        = (m.choose k : ℚ) * c ^ (m - k) * a (k + 1)
          + (m.choose (k + 1) : ℚ) * c ^ (m - k) * a (k + 1) := by
    intro k _
    have hp : (m + 1).choose (k + 1) = m.choose k + m.choose (k + 1) := Nat.choose_succ_succ m k
    have hpq : ((m + 1).choose (k + 1) : ℚ) = (m.choose k : ℚ) + (m.choose (k + 1) : ℚ) := by
      exact_mod_cast hp
    rw [hpq]; ring
  rw [Finset.sum_congr rfl hsplit, Finset.sum_add_distrib]
  have hA : ∑ k ∈ Finset.range (m + 1), (m.choose k : ℚ) * c ^ (m - k) * a (k + 1)
      = genTrC c (fun k => a (k + 1)) m := rfl
  have hgenTr : genTrC c a m = c ^ m * a 0
      + ∑ k ∈ Finset.range m, (m.choose (k + 1) : ℚ) * c ^ (m - 1 - k) * a (k + 1) := by
    have h := Finset.sum_range_succ' (fun k => (m.choose k : ℚ) * c ^ (m - k) * a k) m
    simp only [genTrC]
    rw [h]
    simp only [Nat.choose_zero_right, Nat.cast_one, one_mul, Nat.sub_zero]
    rw [add_comm]
    congr 1
    apply Finset.sum_congr rfl
    intro k hk
    simp only [Finset.mem_range] at hk
    have hexp : m - (k + 1) = m - 1 - k := by omega
    rw [hexp]
  have hB : ∑ k ∈ Finset.range (m + 1), (m.choose (k + 1) : ℚ) * c ^ (m - k) * a (k + 1)
      = c * genTrC c a m - c ^ (m + 1) * a 0 := by
    have hpeel : ∑ k ∈ Finset.range (m + 1), (m.choose (k + 1) : ℚ) * c ^ (m - k) * a (k + 1)
        = ∑ k ∈ Finset.range m, (m.choose (k + 1) : ℚ) * c ^ (m - k) * a (k + 1) := by
      rw [Finset.sum_range_succ]
      have hz : (m.choose (m + 1) : ℚ) = 0 := by
        exact_mod_cast Nat.choose_eq_zero_of_lt (by omega)
      rw [hz]; ring
    rw [hpeel]
    have hsum_eq : ∑ k ∈ Finset.range m, (m.choose (k + 1) : ℚ) * c ^ (m - k) * a (k + 1)
        = c * ∑ k ∈ Finset.range m, (m.choose (k + 1) : ℚ) * c ^ (m - 1 - k) * a (k + 1) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro k hk
      simp only [Finset.mem_range] at hk
      have hexp : m - k = (m - 1 - k) + 1 := by omega
      rw [hexp, pow_succ]; ring
    rw [hsum_eq]
    have hrepl : ∑ k ∈ Finset.range m, (m.choose (k + 1) : ℚ) * c ^ (m - 1 - k) * a (k + 1)
        = genTrC c a m - c ^ m * a 0 := by
      rw [hgenTr]; ring
    rw [hrepl]; ring
  rw [hA, hB]
  ring

/-! ## Stage B, weighted Pascal transforms with parametrized weight `c` (toward TREC)

Mechanical `c`-parametrized generalizations of CatalanEndpoint.lean's `genTrW1_eq` /
`genTrW2_eq`, needed for the "Way B" substitution of `zagC_rec` (whose coefficients
`h(3k²+3k+1)` and `3h²k²` are *quadratic* in `k`, unlike `catalanB_rec`'s constant
`12`/`32`).  The additive decompositions `3k²+3k+1 = 3k(k−1)+6k+1` and `k² = k(k−1)+k`
(checked symbolically in `work/harmonic_jets/derive_zagB_TREC3.py`) let Way B reuse
exactly these two primitives (weight `k`, weight `k(k−1)`) rather than needing new
degree-2 machinery. -/

/-- **Weight-`k` Pascal reduction, parametrized weight.**
`Σ_{k≤m+1} C(m+1,k)c^{m+1-k} k a_k = (m+1)·genTrC c (a∘succ) m`. -/
theorem genTrCW1_eq (c : ℚ) (a : ℕ → ℚ) (m : ℕ) :
    ∑ k ∈ Finset.range (m + 1 + 1),
        ((m + 1).choose k : ℚ) * c ^ (m + 1 - k) * (k : ℚ) * a k
      = ((m : ℚ) + 1) * genTrC c (fun k => a (k + 1)) m := by
  have hpeel := Finset.sum_range_succ'
    (fun k => ((m + 1).choose k : ℚ) * c ^ (m + 1 - k) * (k : ℚ) * a k) (m + 1)
  simp only [Nat.cast_zero, mul_zero, zero_mul, add_zero] at hpeel
  rw [hpeel]
  rw [genTrC, Finset.mul_sum]
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
  linear_combination c ^ (m - k) * a (k + 1) * hid

/-- **Weight-`k(k-1)` Pascal reduction, parametrized weight.**
`Σ_{k≤m+2} C(m+2,k)c^{m+2-k} k(k-1) a_k = (m+2)(m+1)·genTrC c (fun k ↦ a (k+2)) m`. -/
theorem genTrCW2_eq (c : ℚ) (a : ℕ → ℚ) (m : ℕ) :
    ∑ k ∈ Finset.range (m + 2 + 1),
        ((m + 2).choose k : ℚ) * c ^ (m + 2 - k) * ((k : ℚ) * ((k : ℚ) - 1)) * a k
      = (((m : ℚ) + 2) * ((m : ℚ) + 1)) * genTrC c (fun k => a (k + 2)) m := by
  have hpeel1 := Finset.sum_range_succ'
    (fun k => ((m + 2).choose k : ℚ) * c ^ (m + 2 - k) * ((k : ℚ) * ((k : ℚ) - 1)) * a k)
    (m + 2)
  simp only [Nat.cast_zero, zero_mul, mul_zero, add_zero] at hpeel1
  push_cast at hpeel1
  rw [hpeel1]
  have hpeel2 := Finset.sum_range_succ'
    (fun k => ((m + 2).choose (k + 1) : ℚ) * c ^ (m + 2 - (k + 1))
        * (((k : ℚ) + 1) * (((k : ℚ) + 1) - 1)) * a (k + 1)) (m + 1)
  simp only [Nat.cast_zero, add_zero, zero_add, mul_zero, zero_mul] at hpeel2
  push_cast at hpeel2
  have hpeel2' : ∑ x ∈ Finset.range (m + 2), ((m + 2).choose (x + 1) : ℚ) * c ^ (m + 1 - x)
        * (((x:ℚ) + 1) * ((x:ℚ) + 1 - 1)) * a (x + 1)
      = ∑ x ∈ Finset.range (m + 1), ((m + 2).choose (x + 1 + 1) : ℚ) * c ^ (m - x)
          * ((((x:ℚ) + 1) + 1) * ((x:ℚ) + 1)) * a (x + 1 + 1) := by
    rw [show (Finset.range (m + 1 + 1)) = Finset.range (m + 2) from rfl] at hpeel2
    rw [hpeel2]
    have hz : ((m + 2).choose 1 : ℚ) * c ^ (m + 1) * (1 * (1 - 1)) * a 1 = 0 := by ring
    rw [hz, add_zero]
    apply Finset.sum_congr rfl
    intro x _
    ring_nf
  rw [show m + 1 + 1 = m + 2 from rfl] at hpeel2'
  rw [hpeel2']
  rw [genTrC, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro k hk
  simp only [Finset.mem_range] at hk
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
  rw [show ((m + 2).choose (k+1+1) : ℚ) * c ^ (m - k) * ((((k:ℚ)+1)+1) * ((k:ℚ)+1)) * a (k + 1 + 1)
      = (((m + 2).choose (k+1+1) : ℚ) * (((k:ℚ)+1+1) * ((k:ℚ)+1))) * c ^ (m - k) * a (k+1+1) from by ring,
    hkey]
  ring

/-! ## Stage B, shifted-index Pascal identities (Q0,Q1,Q2), parametrized weight -/

/-- **Q1, parametrized weight.** `Σ_{j<m+1} C(m+1,j+1)c^{m-j}(j+1) a_j = (m+1)·genTrC c a m`. -/
theorem genTrCQ1_eq (c : ℚ) (a : ℕ → ℚ) (m : ℕ) :
    ∑ j ∈ Finset.range (m + 1), ((m + 1).choose (j + 1) : ℚ) * c ^ (m - j) * ((j:ℚ) + 1) * a j
      = ((m:ℚ) + 1) * genTrC c a m := by
  rw [genTrC, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j hj
  have hid : ((j : ℚ) + 1) * ((m + 1).choose (j + 1) : ℚ) = ((m : ℚ) + 1) * (m.choose j : ℚ) := by
    have h := Nat.add_one_mul_choose_eq m j
    have : ((m + 1) * m.choose j : ℚ) = ((m + 1).choose (j + 1) * (j + 1) : ℚ) := by
      exact_mod_cast h
    push_cast at this
    linarith
  rw [show ((m + 1).choose (j + 1) : ℚ) * c ^ (m - j) * ((j:ℚ) + 1) * a j
      = (((j:ℚ)+1) * ((m + 1).choose (j + 1) : ℚ)) * c ^ (m - j) * a j from by ring, hid]
  ring

/-- **Q2, parametrized weight.** `Σ_{j<m+2} C(m+2,j+1)c^{m+1-j}(j+1)² a_j
= (m+2)(m+1)·genTrC c (a∘succ) m + (m+2)·genTrC c a (m+1)`. -/
theorem genTrCQ2_eq (c : ℚ) (a : ℕ → ℚ) (m : ℕ) :
    ∑ j ∈ Finset.range (m + 2),
        ((m + 2).choose (j + 1) : ℚ) * c ^ (m + 1 - j) * (((j:ℚ) + 1) ^ 2) * a j
      = ((m:ℚ) + 2) * ((m:ℚ) + 1) * genTrC c (fun k => a (k + 1)) m
        + ((m:ℚ) + 2) * genTrC c a (m + 1) := by
  have hpt : ∀ j ∈ Finset.range (m + 2),
      ((m + 2).choose (j + 1) : ℚ) * c ^ (m + 1 - j) * (((j:ℚ) + 1) ^ 2) * a j
        = ((m:ℚ) + 2) * (((m + 1).choose j : ℚ) * c ^ (m + 1 - j) * (j:ℚ) * a j)
          + ((m:ℚ) + 2) * (((m + 1).choose j : ℚ) * c ^ (m + 1 - j) * a j) := by
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
    rw [show ((m + 2).choose (j + 1) : ℚ) * c ^ (m + 1 - j) * (((j:ℚ) + 1) ^ 2) * a j
        = ((((j:ℚ) + 1) ^ 2) * ((m + 2).choose (j + 1) : ℚ)) * c ^ (m + 1 - j) * a j from by ring,
      hsq]
    ring
  rw [Finset.sum_congr rfl hpt, Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum]
  have e1 : ∑ j ∈ Finset.range (m + 2), ((m + 1).choose j : ℚ) * c ^ (m + 1 - j) * (j:ℚ) * a j
      = ((m:ℚ) + 1) * genTrC c (fun k => a (k + 1)) m := genTrCW1_eq c a m
  have e2 : ∑ j ∈ Finset.range (m + 2), ((m + 1).choose j : ℚ) * c ^ (m + 1 - j) * a j
      = genTrC c a (m + 1) := rfl
  rw [e1, e2]
  ring

/-- **Q0, parametrized weight.** `Σ_{j<m+1} C(m+1,j+1)c^{m-j} a_{j+1} = genTrC c a (m+1) - c^{m+1} a 0`. -/
theorem genTrCQ0_eq (c : ℚ) (a : ℕ → ℚ) (m : ℕ) :
    ∑ j ∈ Finset.range (m + 1), ((m + 1).choose (j + 1) : ℚ) * c ^ (m - j) * a (j + 1)
      = genTrC c a (m + 1) - c ^ (m + 1) * a 0 := by
  have h := Finset.sum_range_succ'
    (fun k => ((m + 1).choose k : ℚ) * c ^ (m + 1 - k) * a k) (m + 1)
  simp only [Nat.choose_zero_right, Nat.cast_one, one_mul, Nat.sub_zero] at h
  have hgt : genTrC c a (m + 1) = c ^ (m + 1) * a 0
      + ∑ k ∈ Finset.range (m + 1), ((m + 1).choose (k + 1) : ℚ) * c ^ (m + 1 - (k + 1)) * a (k + 1) := by
    simp only [genTrC]; rw [h]; ring
  have hexp : ∀ k ∈ Finset.range (m + 1),
      ((m + 1).choose (k + 1) : ℚ) * c ^ (m + 1 - (k + 1)) * a (k + 1)
        = ((m + 1).choose (k + 1) : ℚ) * c ^ (m - k) * a (k + 1) := by
    intro k hk
    simp only [Finset.mem_range] at hk
    have : m + 1 - (k + 1) = m - k := by omega
    rw [this]
  rw [Finset.sum_congr rfl hexp] at hgt
  rw [hgt]; ring

/-! ## Stage B, closing TREC via the Way-A/Way-B auxiliary sum `zagM`

`zagM` mirrors CatalanEndpoint.lean's `catalanM`, weighted by the parametrized weight
`c = -h`. **Way A** (`zagM_wayA`) is purely from the Pascal weighted-transform
identities (no use of `zagC_rec`), so it is a mechanical port of `catalanM_wayA`.
**Way B** (`zagM_wayB`) substitutes `zagC_rec'` once; since `zagC_rec`'s coefficients
`h(3k²+3k+1)`, `3h²k²` are *constant in `k`* (just parametrized by `h`, exactly like
CatalanEndpoint's constant `12`,`32`), Way B is also a mechanical port. Equating
Way A and Way B and eliminating the shift-tower objects `zagV`,`zagW`,`zagY` via their
`_succ` relations (using coefficients found by the exact symbolic elimination in
`work/harmonic_jets/derive_zagB_wayAB5.py`) closes **TREC** via `linear_combination`,
exactly as CatalanEndpoint.lean's `catalanT_rec_aux` closed the step-2 analogue. -/

/-- `zagV_n := Σ C(n,k)(-h)^{n-k} C_{k+1}` (shift-1 transform). -/
def zagV (h : ℤ) (n : ℕ) : ℚ := genTrC (-(h:ℚ)) (fun k => zagC h (k + 1)) n

/-- `zagW_n := Σ C(n,k)(-h)^{n-k} C_{k+2}` (shift-2 transform). -/
def zagW (h : ℤ) (n : ℕ) : ℚ := genTrC (-(h:ℚ)) (fun k => zagC h (k + 2)) n

/-- `zagY_n := Σ C(n,k)(-h)^{n-k} C_{k+3}` (shift-3 transform). -/
def zagY (h : ℤ) (n : ℕ) : ℚ := genTrC (-(h:ℚ)) (fun k => zagC h (k + 3)) n

theorem zagS_succ (h : ℤ) (m : ℕ) : zagS h (m + 1) = -(h:ℚ) * zagS h m + zagV h m := by
  have h' := genTrC_succ (-(h:ℚ)) (zagC h) m
  simpa [← zagS_eq_genTrC, zagV] using h'

theorem zagV_succ (h : ℤ) (m : ℕ) : zagV h (m + 1) = -(h:ℚ) * zagV h m + zagW h m := by
  have h' := genTrC_succ (-(h:ℚ)) (fun k => zagC h (k + 1)) m
  simpa [zagV, zagW] using h'

theorem zagW_succ (h : ℤ) (m : ℕ) : zagW h (m + 1) = -(h:ℚ) * zagW h m + zagY h m := by
  have h' := genTrC_succ (-(h:ℚ)) (fun k => zagC h (k + 2)) m
  simpa [zagW, zagY] using h'

/-- `zagM_n := Σ_{k=0}^n C(n,k)(-h)^{n-k}(k+1)² C_{k+1}`. -/
def zagM (h : ℤ) (n : ℕ) : ℚ :=
  ∑ k ∈ Finset.range (n + 1), (n.choose k : ℚ) * (-(h:ℚ)) ^ (n - k) * (((k:ℚ) + 1) ^ 2) * zagC h (k + 1)

/-- **Way A** (no use of `zagC_rec`): purely from the Pascal weighted-transform
identities `genTrCW1_eq`/`genTrCW2_eq` applied to `a := fun k ↦ zagC h (k+1)`. -/
theorem zagM_wayA (h : ℤ) (m : ℕ) :
    zagM h (m + 2)
      = ((m:ℚ) + 2) * ((m:ℚ) + 1) * zagY h m + 3 * (((m:ℚ) + 2) * zagW h (m + 1))
        + zagV h (m + 2) := by
  set c : ℚ := -(h:ℚ)
  have hpt : ∀ k ∈ Finset.range (m + 2 + 1),
      ((m+2).choose k : ℚ) * c ^ (m + 2 - k) * (((k:ℚ) + 1) ^ 2) * zagC h (k + 1)
        = ((m+2).choose k : ℚ) * c ^ (m + 2 - k) * ((k:ℚ) * ((k:ℚ) - 1)) * zagC h (k + 1)
          + 3 * (((m+2).choose k : ℚ) * c ^ (m + 2 - k) * (k:ℚ) * zagC h (k + 1))
          + ((m+2).choose k : ℚ) * c ^ (m + 2 - k) * zagC h (k + 1) := by
    intro k _; ring
  have hsplit : zagM h (m + 2)
      = (∑ k ∈ Finset.range (m + 2 + 1),
            ((m+2).choose k : ℚ) * c ^ (m + 2 - k) * ((k:ℚ) * ((k:ℚ) - 1)) * zagC h (k + 1))
        + 3 * (∑ k ∈ Finset.range (m + 2 + 1),
            ((m+2).choose k : ℚ) * c ^ (m + 2 - k) * (k:ℚ) * zagC h (k + 1))
        + ∑ k ∈ Finset.range (m + 2 + 1),
            ((m+2).choose k : ℚ) * c ^ (m + 2 - k) * zagC h (k + 1) := by
    rw [zagM, Finset.sum_congr rfl hpt]
    rw [Finset.sum_add_distrib, Finset.sum_add_distrib, Finset.mul_sum]
  have hW2 := genTrCW2_eq c (fun k => zagC h (k + 1)) m
  have hW1 := genTrCW1_eq c (fun k => zagC h (k + 1)) (m + 1)
  have hT : ∑ k ∈ Finset.range (m + 2 + 1),
      ((m+2).choose k : ℚ) * c ^ (m + 2 - k) * zagC h (k + 1) = zagV h (m + 2) := rfl
  rw [show (m+1+1+1) = (m+2+1) from rfl] at hW1
  rw [hsplit, hW2, hW1, hT]
  have hY : genTrC c (fun k => zagC h (k + 2 + 1)) m = zagY h m := by
    show genTrC c (fun k => zagC h (k + 2 + 1)) m = genTrC c (fun k => zagC h (k + 3)) m
    norm_num
  have hWm1 : genTrC c (fun k => zagC h (k + 1 + 1)) (m + 1) = zagW h (m + 1) := by
    show genTrC c (fun k => zagC h (k + 1 + 1)) (m + 1) = genTrC c (fun k => zagC h (k + 2)) (m + 1)
    norm_num
  rw [hY, hWm1]
  push_cast
  ring

/-- **Way B** (uses `zagC_rec`): substituting `zagC_rec'` into `zagM`'s `k ≥ 1` terms
(coefficients `A = B = 3h`, `D = h`, `E = 3h²`, all constant in `k`, exactly like
CatalanEndpoint's constant `12`/`32`), and `zagC_one` into its `k = 0` term. -/
theorem zagM_wayB (h : ℤ) (m : ℕ) :
    zagM h (m + 2)
      = (-(h:ℚ)) ^ (m + 2)
        + 3 * (h:ℚ) * (((m:ℚ) + 2) * ((m:ℚ) + 1) * zagW h m)
        + 6 * (h:ℚ) * (((m:ℚ) + 2) * zagV h (m + 1))
        + (h:ℚ) * zagS h (m + 2)
        - 3 * (h:ℚ)^2 * (((m:ℚ) + 2) * ((m:ℚ) + 1) * zagV h m + ((m:ℚ) + 2) * zagS h (m + 1)) := by
  set c : ℚ := -(h:ℚ)
  have hpeel : zagM h (m + 2)
      = c ^ (m + 2) * zagC h 1
        + ∑ k ∈ Finset.range (m + 2), ((m+2).choose (k+1) : ℚ) * c ^ (m + 2 - (k+1))
            * (((k:ℚ) + 1 + 1) ^ 2) * zagC h (k + 1 + 1) := by
    have h' := Finset.sum_range_succ'
      (fun k => ((m+2).choose k : ℚ) * c ^ (m + 2 - k) * (((k:ℚ) + 1) ^ 2) * zagC h (k + 1))
      (m + 2)
    simp only [Nat.cast_zero, Nat.sub_zero, Nat.choose_zero_right, Nat.cast_one, Nat.zero_add] at h'
    rw [zagM]
    rw [h']
    norm_num
    ring
  rw [zagC_one, mul_one] at hpeel
  have hsub : ∀ k ∈ Finset.range (m + 2),
      ((m+2).choose (k+1) : ℚ) * c ^ (m + 2 - (k+1)) * (((k:ℚ) + 1 + 1) ^ 2) * zagC h (k + 1 + 1)
        = ((m+2).choose (k+1) : ℚ) * c ^ (m + 1 - k)
          * ((h:ℚ) * (3 * ((k:ℚ)+1)^2 + 3 * ((k:ℚ)+1) + 1) * zagC h (k+1)
              - 3 * (h:ℚ)^2 * ((k:ℚ)+1)^2 * zagC h k) := by
    intro k hk
    have hrec := zagC_rec' h k
    have hexp : m + 2 - (k + 1) = m + 1 - k := by omega
    rw [hexp]
    have hcert : ((k:ℚ) + 1 + 1) ^ 2 * zagC h (k + 1 + 1)
        = (h:ℚ) * (3 * ((k:ℚ)+1)^2 + 3 * ((k:ℚ)+1) + 1) * zagC h (k+1)
            - 3 * (h:ℚ)^2 * ((k:ℚ)+1)^2 * zagC h k := by
      linear_combination hrec
    rw [show ((m+2).choose (k+1) : ℚ) * c ^ (m + 1 - k) * (((k:ℚ) + 1 + 1) ^ 2) * zagC h (k + 1 + 1)
        = ((m+2).choose (k+1) : ℚ) * c ^ (m + 1 - k) * (((k:ℚ) + 1 + 1) ^ 2 * zagC h (k+1+1))
        from by ring, hcert]
  rw [Finset.sum_congr rfl hsub] at hpeel
  have hexpand : ∀ k ∈ Finset.range (m + 2),
      ((m+2).choose (k+1) : ℚ) * c ^ (m + 1 - k)
          * ((h:ℚ) * (3 * ((k:ℚ)+1)^2 + 3 * ((k:ℚ)+1) + 1) * zagC h (k+1)
              - 3 * (h:ℚ)^2 * ((k:ℚ)+1)^2 * zagC h k)
        = 3 * (h:ℚ) * (((m+2).choose (k+1) : ℚ) * c^(m+1-k) * (((k:ℚ)+1)^2) * zagC h (k+1))
          + 3 * (h:ℚ) * (((m+2).choose (k+1) : ℚ) * c^(m+1-k) * ((k:ℚ)+1) * zagC h (k+1))
          + (h:ℚ) * (((m+2).choose (k+1) : ℚ) * c^(m+1-k) * zagC h (k+1))
          - 3 * (h:ℚ)^2 * (((m+2).choose (k+1) : ℚ) * c^(m+1-k) * (((k:ℚ)+1)^2) * zagC h k) := by
    intro k _; ring
  rw [Finset.sum_congr rfl hexpand] at hpeel
  rw [Finset.sum_sub_distrib, Finset.sum_add_distrib, Finset.sum_add_distrib,
      ← Finset.mul_sum, ← Finset.mul_sum, ← Finset.mul_sum, ← Finset.mul_sum] at hpeel
  have e1 : ∑ k ∈ Finset.range (m + 2),
      ((m+2).choose (k+1) : ℚ) * c^(m+1-k) * (((k:ℚ)+1)^2) * zagC h (k+1)
      = ((m:ℚ)+2) * ((m:ℚ)+1) * zagW h m + ((m:ℚ)+2) * zagV h (m + 1) := by
    have h' := genTrCQ2_eq c (fun k => zagC h (k + 1)) m
    have hWeq : genTrC c (fun k => zagC h (k + 1 + 1)) m = zagW h m := by
      show genTrC c (fun k => zagC h (k + 1 + 1)) m = genTrC c (fun k => zagC h (k + 2)) m
      norm_num
    rw [hWeq] at h'
    have hVeq : genTrC c (fun k => zagC h (k + 1)) (m + 1) = zagV h (m + 1) := rfl
    rw [hVeq] at h'
    exact h'
  have e2 : ∑ k ∈ Finset.range (m + 2),
      ((m+2).choose (k+1) : ℚ) * c^(m+1-k) * ((k:ℚ)+1) * zagC h (k+1)
      = ((m:ℚ)+2) * zagV h (m + 1) := by
    have h' := genTrCQ1_eq c (fun k => zagC h (k + 1)) (m + 1)
    have hVeq : genTrC c (fun k => zagC h (k + 1)) (m + 1) = zagV h (m + 1) := rfl
    rw [hVeq] at h'
    convert h' using 2
    push_cast; ring
  have e3 : ∑ k ∈ Finset.range (m + 2),
      ((m+2).choose (k+1) : ℚ) * c^(m+1-k) * zagC h (k+1)
      = zagS h (m + 2) := by
    have h' := genTrCQ0_eq c (zagC h) (m + 1)
    rw [zagC_zero, mul_zero, sub_zero] at h'
    have hTeq : genTrC c (zagC h) (m + 1 + 1) = zagS h (m + 2) := by
      rw [zagS_eq_genTrC]
    rw [hTeq] at h'
    convert h' using 2
  have e4 : ∑ k ∈ Finset.range (m + 2),
      ((m+2).choose (k+1) : ℚ) * c^(m+1-k) * (((k:ℚ)+1)^2) * zagC h k
      = ((m:ℚ)+2) * ((m:ℚ)+1) * zagV h m + ((m:ℚ)+2) * zagS h (m + 1) := by
    have h' := genTrCQ2_eq c (zagC h) m
    have hVeq : genTrC c (fun k => zagC h (k + 1)) m = zagV h m := rfl
    rw [hVeq] at h'
    have hTeq : genTrC c (zagC h) (m + 1) = zagS h (m + 1) := by rw [zagS_eq_genTrC]
    rw [hTeq] at h'
    exact h'
  rw [e1, e2, e3, e4] at hpeel
  rw [hpeel]
  ring

/-- **TREC, the `m + 3` case.** `(m+3)² S_{m+3} + h³(m+1)(m+2) S_m = (-h)^{m+2}`.
Proved by equating `zagM_wayA`/`zagM_wayB` and eliminating `zagY`, `zagW`, `zagV` via
the shift-tower relations, using coefficients found by the exact symbolic elimination
in `work/harmonic_jets/derive_zagB_wayAB5.py`. -/
theorem zagS_rec_aux (h : ℤ) (m : ℕ) :
    ((m:ℚ) + 3) ^ 2 * zagS h (m + 3) + (h:ℚ)^3 * ((m:ℚ)+1) * ((m:ℚ)+2) * zagS h m
      = (-(h:ℚ)) ^ (m + 2) := by
  have hA := zagM_wayA h m
  have hB := zagM_wayB h m
  have hWs := zagW_succ h m
  have hVs0 := zagV_succ h m
  have hVs1 := zagV_succ h (m + 1)
  have hTs0 := zagS_succ h m
  have hTs1 := zagS_succ h (m + 1)
  have hTs2 := zagS_succ h (m + 2)
  rw [show m + 1 + 1 = m + 2 from rfl] at hVs1 hTs1
  rw [show m + 2 + 1 = m + 3 from rfl] at hTs2
  linear_combination hB - hA
    + (h:ℚ)^2*((m:ℚ)+1)*((m:ℚ)+2) * hTs0 - (h:ℚ)*((m:ℚ)+2)*((m:ℚ)+4) * hTs1
    + ((m:ℚ)+3)^2 * hTs2
    - 2*(h:ℚ)*((m:ℚ)+1)*((m:ℚ)+2) * hVs0 + ((m:ℚ)+2)*((m:ℚ)+4) * hVs1
    + ((m:ℚ)+1)*((m:ℚ)+2) * hWs

/-- **TREC.** `n² S_n + h³(n−2)(n−1) S_{n−3} = (−h)^{n−1}` for all `n ≥ 1`, with
truncated `ℕ` subtraction (the `n < 3` terms containing `S_{n-3}` etc. are handled by
direct computation). This is stated for `n ≥ 1`: at `n = 0` the `ℕ`-truncated
statement is genuinely false (`0 ≠ (-h)^{0-1 truncated to 0} = 1`), matching the fact
that the underlying identity `(-h)^{n-1}` only makes sense for `n ≥ 1`. -/
theorem zagS_rec (h : ℤ) (n : ℕ) (hn : 1 ≤ n) :
    (n:ℚ) ^ 2 * zagS h n + (h:ℚ)^3 * ((n:ℚ) - 2) * ((n:ℚ) - 1) * zagS h (n - 3)
      = (-(h:ℚ)) ^ (n - 1) := by
  match n, hn with
  | 1, _ => norm_num [zagS_one, zagS_zero]
  | 2, _ =>
      have h1 : zagS h 1 = 1 := zagS_one h
      have h2 : zagS h 2 = -(h:ℚ) / 4 := by
        show zagS h 2 = -(h:ℚ) / 4
        have hc2 : zagC h 2 = 7 * (h:ℚ) / 4 := by
          show zagC h 2 = 7 * (h:ℚ) / 4
          norm_num [zagC]
          ring
        simp [zagS, Finset.sum_range_succ, zagC, hc2]
        ring
      norm_num [h1, h2, zagS_zero]
      ring
  | (m + 3), _ =>
      have h' := zagS_rec_aux h m
      have e1 : m + 3 - 3 = m := by omega
      have e2 : m + 3 - 1 = m + 2 := by omega
      rw [e1, e2]
      push_cast
      linear_combination h'

/-! ## Stage C — the finite endpoint formula (item 3)

Mirrors CatalanEndpoint.lean's Stage C (`endpointQ/Num/Den/R`, `catalanSumR`,
`catalanT_square_formula`), adapted from step-2/mod-2 to step-3/mod-3, and *without*
the "square" trick CatalanEndpoint needed (there, `T_n` was a sum of `R_{n,j}²`, an
artifact of CatalanEndpoint's weight `-4` being a perfect square up to sign; here
`S_n` is a sum of `R(n,j)` directly, unsquared, matching the paper's
`(-1)^{n-1}S_n = h^{n-1} Σ R(n,j)`). -/

/-- The "third-length" `r = (n-j-1)/3` appearing in the endpoint formula `R(n,j)`. -/
def zagQ (n j : ℕ) : ℕ := (n - j - 1) / 3

/-- The numerator product `∏_{t=0}^{r-1} (j+2+3t)(j+3+3t)` (empty product `= 1` when
`r = 0`). -/
def zagNum (n j : ℕ) : ℕ :=
  ∏ t ∈ Finset.range (zagQ n j), (j + 2 + 3 * t) * (j + 3 + 3 * t)

/-- The denominator product `∏_{t=0}^{r} (j+1+3t)²`. -/
def zagDen (n j : ℕ) : ℕ :=
  ∏ t ∈ Finset.range (zagQ n j + 1), (j + 1 + 3 * t) ^ 2

theorem zagDen_pos (n j : ℕ) : 0 < zagDen n j := by
  apply Finset.prod_pos; intro t _; positivity

theorem zagDen_ne_zero (n j : ℕ) : zagDen n j ≠ 0 := (zagDen_pos n j).ne'

/-- The endpoint quantity `R(n,j) = Num/Den`. -/
def zagR (n j : ℕ) : ℚ := (zagNum n j : ℚ) / (zagDen n j : ℚ)

/-- At `j = n - 1` (so `r = 0`): `R(n,n-1) = 1/n²`. -/
theorem zagR_top (n : ℕ) (hn : 1 ≤ n) : zagR n (n - 1) = 1 / (n : ℚ) ^ 2 := by
  have hq : zagQ n (n - 1) = 0 := by unfold zagQ; omega
  have hNum : zagNum n (n - 1) = 1 := by unfold zagNum; rw [hq]; simp
  have hDen : zagDen n (n - 1) = n ^ 2 := by
    unfold zagDen; rw [hq]
    have hn' : n - 1 + 1 = n := by omega
    simp [hn']
  unfold zagR
  rw [hNum, hDen]
  push_cast
  ring

/-- Step relation: for `j + 4 ≤ n` with `n - j ≡ 1 (mod 3)`, `Num`/`Den` for `(n,j)` are
obtained from `(n-3,j)` by one extra factor pair `(n-2)(n-1)` (numerator) / `n²`
(denominator). -/
theorem zagNum_step (n j : ℕ) (hj : j + 4 ≤ n) (hmod : n % 3 = (j + 1) % 3) :
    zagNum n j = zagNum (n - 3) j * ((n - 2) * (n - 1)) := by
  have hq : zagQ n j = zagQ (n - 3) j + 1 := by unfold zagQ; omega
  have e1 : j + 2 + 3 * zagQ (n - 3) j = n - 2 := by unfold zagQ; omega
  have e2 : j + 3 + 3 * zagQ (n - 3) j = n - 1 := by unfold zagQ; omega
  unfold zagNum
  rw [hq, Finset.prod_range_succ, e1, e2]

theorem zagDen_step (n j : ℕ) (hj : j + 4 ≤ n) (hmod : n % 3 = (j + 1) % 3) :
    zagDen n j = zagDen (n - 3) j * n ^ 2 := by
  have hq : zagQ n j + 1 = (zagQ (n - 3) j + 1) + 1 := by unfold zagQ; omega
  have e1 : j + 1 + 3 * (zagQ (n - 3) j + 1) = n := by unfold zagQ; omega
  unfold zagDen
  rw [hq, Finset.prod_range_succ, e1]

theorem zagR_step (n j : ℕ) (hj : j + 4 ≤ n) (hmod : n % 3 = (j + 1) % 3) :
    zagR n j = (((n : ℚ) - 2) * ((n : ℚ) - 1) / (n : ℚ) ^ 2) * zagR (n - 3) j := by
  have hNum := zagNum_step n j hj hmod
  have hDen := zagDen_step n j hj hmod
  have hDenpos : (zagDen (n - 3) j : ℚ) ≠ 0 := by exact_mod_cast zagDen_ne_zero (n - 3) j
  have hnQ : (n : ℚ) ≠ 0 := by
    have : 0 < n := by omega
    exact_mod_cast this.ne'
  unfold zagR
  rw [hNum, hDen]
  have hcast2 : ((n:ℚ) - 2 : ℚ) = ((n - 2 : ℕ) : ℚ) := by
    have : (2:ℕ) ≤ n := by omega
    rw [Nat.cast_sub this]; norm_num
  have hcast1 : ((n:ℚ) - 1 : ℚ) = ((n - 1 : ℕ) : ℚ) := by
    have : (1:ℕ) ≤ n := by omega
    rw [Nat.cast_sub this]; norm_num
  rw [hcast2, hcast1]
  push_cast
  field_simp

/-- The endpoint sum `Σ_{0≤j<n, n-j≡1 mod 3} R(n,j)`, as an indicator sum over
`Finset.range n`. -/
def zagSumR (n : ℕ) : ℚ :=
  ∑ j ∈ Finset.range n, if n % 3 = (j + 1) % 3 then zagR n j else 0

/-- Peeling the top index `j = n - 1` (whose indicator is always true) and the two
non-contributing indices `j = n - 2, n - 3` from `zagSumR n`, for `n ≥ 3`. -/
theorem zagSumR_split (n : ℕ) (hn : 3 ≤ n) :
    zagSumR n
      = (∑ j ∈ Finset.range (n - 3), if n % 3 = (j + 1) % 3 then zagR n j else 0)
        + zagR n (n - 1) := by
  obtain ⟨k, rfl⟩ : ∃ k, n = k + 3 := ⟨n - 3, by omega⟩
  have en3 : k + 3 - 3 = k := by omega
  have en1 : k + 3 - 1 = k + 1 + 1 := by omega
  unfold zagSumR
  rw [show k + 3 = k + 1 + 1 + 1 from by omega, Finset.sum_range_succ, Finset.sum_range_succ,
    Finset.sum_range_succ]
  rw [en3, en1]
  -- term j = k  (= n-3): indicator is false
  have hcB : ¬ (k + 1 + 1 + 1) % 3 = (k + 1) % 3 := by omega
  -- term j = k+1  (= n-2): indicator is false
  have hcA : ¬ (k + 1 + 1 + 1) % 3 = (k + 1 + 1) % 3 := by omega
  -- term j = k+2 = k+1+1  (= n-1, the top term): indicator is true
  have hcC : (k + 1 + 1 + 1) % 3 = (k + 1 + 1 + 1) % 3 := rfl
  simp only [hcA, hcB, hcC, if_false, if_true]
  ring

/-- Replacing each term of `zagSumR n`'s "lower" part (indices `j < n - 3`) by the
corresponding `zagSumR (n-3)` term via `zagR_step`. -/
theorem zagSumR_lower_eq (n : ℕ) (hn : 3 ≤ n) :
    (∑ j ∈ Finset.range (n - 3), if n % 3 = (j + 1) % 3 then zagR n j else 0)
      = (((n : ℚ) - 2) * ((n : ℚ) - 1) / (n : ℚ) ^ 2) * zagSumR (n - 3) := by
  unfold zagSumR
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j hj
  rw [Finset.mem_range] at hj
  have hmodeq : n % 3 = (j + 1) % 3 ↔ (n - 3) % 3 = (j + 1) % 3 := by omega
  by_cases hmod : n % 3 = (j + 1) % 3
  · have hmod' : (n - 3) % 3 = (j + 1) % 3 := hmodeq.mp hmod
    simp only [hmod, hmod', if_true]
    have hstep := zagR_step n j (by omega) hmod
    rw [hstep]
  · have hmod' : ¬ (n - 3) % 3 = (j + 1) % 3 := fun h => hmod (hmodeq.mpr h)
    simp [hmod, hmod']

/-- **The endpoint sum's own step relation.** `Σ_{n-j≡1(3)} R(n,j)` at `n` reduces to
the same sum at `n-3`, via `zagSumR_split` (peel the top term) and `zagSumR_lower_eq`
(reduce the rest). -/
theorem zagSumR_step (n : ℕ) (hn : 3 ≤ n) :
    zagSumR n = (((n:ℚ) - 2) * ((n:ℚ) - 1) / (n:ℚ) ^ 2) * zagSumR (n - 3) + 1 / (n:ℚ) ^ 2 := by
  rw [zagSumR_split n hn, zagSumR_lower_eq n hn, zagR_top n (by omega)]

/-- **The finite endpoint formula.** `(-1)^{n-1} S_n = h^{n-1} · Σ_{n-j≡1(3)} R(n,j)`,
proved by induction in steps of three from `TREC` (`zagS_rec`), mirroring
CatalanEndpoint.lean's `catalanT_square_formula`. -/
theorem zagC_two_eq (h : ℤ) : zagC h 2 = 7 * (h : ℚ) / 4 := by
  show zagC h 2 = 7 * (h : ℚ) / 4
  norm_num [zagC]
  ring

theorem zagC_three_eq (h : ℤ) : zagC h 3 = 85 * (h : ℚ) ^ 2 / 36 := by
  show zagC h (1 + 2) = 85 * (h : ℚ) ^ 2 / 36
  norm_num [zagC]
  ring

theorem zagS_two_eq (h : ℤ) : zagS h 2 = -(h : ℚ) / 4 := by
  show zagS h 2 = -(h : ℚ) / 4
  simp [zagS, Finset.sum_range_succ, zagC, zagC_two_eq]
  ring

theorem zagS_three_eq (h : ℤ) : zagS h 3 = (h : ℚ) ^ 2 / 9 := by
  show zagS h 3 = (h : ℚ) ^ 2 / 9
  simp [zagS, Finset.sum_range_succ, zagC, zagC_two_eq, zagC_three_eq]
  ring

theorem zagS_endpoint_formula (h : ℤ) :
    ∀ n : ℕ, 1 ≤ n → (-1 : ℚ) ^ (n - 1) * zagS h n = (h : ℚ) ^ (n - 1) * zagSumR n := by
  have main : ∀ m : ℕ,
      ((-1:ℚ)^(3*m) * zagS h (3*m+1) = (h:ℚ)^(3*m) * zagSumR (3*m+1)) ∧
      ((-1:ℚ)^(3*m+1) * zagS h (3*m+2) = (h:ℚ)^(3*m+1) * zagSumR (3*m+2)) ∧
      ((-1:ℚ)^(3*m+2) * zagS h (3*m+3) = (h:ℚ)^(3*m+2) * zagSumR (3*m+3)) := by
    intro m
    induction m with
    | zero =>
        refine ⟨?_, ?_, ?_⟩
        · -- n = 1
          simp only [Nat.mul_zero, Nat.zero_add, pow_zero, one_mul]
          have hs1 : zagSumR 1 = 1 := by
            unfold zagSumR
            rw [Finset.sum_range_one]
            norm_num
            have h0 : zagR 1 0 = 1 := by
              have h := zagR_top 1 (le_refl 1)
              norm_num at h
              simpa using h
            rw [h0]
          rw [zagS_one, hs1]
        · -- n = 2
          simp only [Nat.mul_zero, Nat.zero_add, pow_one]
          have hs2 : zagSumR 2 = 1 / 4 := by
            unfold zagSumR
            rw [Finset.sum_range_succ, Finset.sum_range_one]
            norm_num
            have h1 : zagR 2 1 = 1 / 4 := by
              have h := zagR_top 2 (by norm_num)
              norm_num at h
              convert h using 2
            rw [h1]
          rw [zagS_two_eq, hs2]
          ring
        · -- n = 3
          simp only [Nat.mul_zero, Nat.zero_add]
          have hs3 : zagSumR 3 = 1 / 9 := by
            unfold zagSumR
            rw [Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_one]
            norm_num
            have h2 : zagR 3 2 = 1 / 9 := by
              have h := zagR_top 3 (by norm_num)
              norm_num at h
              convert h using 2
            rw [h2]
          rw [zagS_three_eq, hs3]
          norm_num
          ring
    | succ m ih =>
        obtain ⟨ih1, ih2, ih3⟩ := ih
        -- Shared step: given the identity at `p` (`prev`), derive it at `p + 3`.
        have step : ∀ p : ℕ, 1 ≤ p →
            (-1:ℚ) ^ (p - 1) * zagS h p = (h:ℚ) ^ (p - 1) * zagSumR p →
            (-1:ℚ) ^ (p + 2) * zagS h (p + 3) = (h:ℚ) ^ (p + 2) * zagSumR (p + 3) := by
          intro p hp ihp
          have hrec := zagS_rec h (p + 3) (by omega)
          have e1 : p + 3 - 3 = p := by omega
          have e2 : p + 3 - 1 = p + 2 := by omega
          rw [e1, e2] at hrec
          have hstep := zagSumR_step (p + 3) (by omega)
          rw [e1] at hstep
          push_cast at hstep
          have hne : ((p:ℚ) + 3) ^ 2 ≠ 0 := by positivity
          -- solve hrec for zagS h (p+3)
          have hSval : zagS h (p + 3)
              = ((-(h:ℚ)) ^ (p + 2) - (h:ℚ)^3 * ((p:ℚ) + 1) * ((p:ℚ) + 2) * zagS h p) / ((p:ℚ) + 3) ^ 2 := by
            push_cast at hrec
            have hc2 : ((p:ℚ) + 3 - 2) = (p:ℚ) + 1 := by ring
            have hc1 : ((p:ℚ) + 3 - 1) = (p:ℚ) + 2 := by ring
            rw [hc2, hc1] at hrec
            field_simp
            linear_combination hrec
          -- solve ihp for zagS h p
          have hsq : (-1:ℚ) ^ (p - 1) * (-1:ℚ) ^ (p - 1) = 1 := by
            rw [← pow_add, ← two_mul, pow_mul]; norm_num
          have hSval1 : zagS h p = (-1:ℚ) ^ (p - 1) * (h:ℚ) ^ (p - 1) * zagSumR p := calc
            zagS h p = (-1:ℚ) ^ (p - 1) * (-1:ℚ) ^ (p - 1) * zagS h p := by rw [hsq]; ring
            _ = (-1:ℚ) ^ (p - 1) * ((-1:ℚ) ^ (p - 1) * zagS h p) := by ring
            _ = (-1:ℚ) ^ (p - 1) * ((h:ℚ) ^ (p - 1) * zagSumR p) := by rw [ihp]
            _ = (-1:ℚ) ^ (p - 1) * (h:ℚ) ^ (p - 1) * zagSumR p := by ring
          have hpm1 : (p:ℚ) + 1 = ((p - 1 : ℕ) : ℚ) + 2 := by
            have : (1:ℕ) ≤ p := hp
            push_cast [Nat.cast_sub this]
            ring
          rw [hSval, hSval1]
          have hpowneg : (-(h:ℚ)) ^ (p + 2) = -1 * (h:ℚ)^3 * (-1:ℚ)^(p-1) * (h:ℚ)^(p-1) := by
            have e3 : p + 2 = 3 + (p - 1) := by omega
            rw [e3, show (-(h:ℚ)) = (-1)*(h:ℚ) from by ring, mul_pow]
            ring
          have hpowLHS : (-1:ℚ) ^ (p + 2) = -1 * (-1:ℚ) ^ (p - 1) := by
            have e3 : p + 2 = 3 + (p - 1) := by omega
            rw [e3, pow_add]; norm_num
          have hpowRHS2 : (h:ℚ) ^ (p + 2) = (h:ℚ)^3 * (h:ℚ) ^ (p - 1) := by
            have e3 : p + 2 = 3 + (p - 1) := by omega
            rw [e3, pow_add]
          rw [hpowneg, hpowLHS, hpowRHS2, hstep]
          field_simp
          have hone : ((-1:ℚ) ^ (p - 1)) ^ 2 = 1 := by
            rw [← pow_mul, mul_comm, pow_mul]; norm_num
          rw [hone]
          ring
        have r1 := step (3 * m + 1) (by omega) ih1
        have r2 := step (3 * m + 2) (by omega) ih2
        have r3 := step (3 * m + 3) (by omega) ih3
        refine ⟨?_, ?_, ?_⟩
        · rw [show 3 * (m + 1) + 1 = 3 * m + 1 + 3 from by ring,
            show 3 * (m + 1) = 3 * m + 1 + 2 from by ring]
          exact r1
        · rw [show 3 * (m + 1) + 2 = 3 * m + 2 + 3 from by ring,
            show 3 * (m + 1) + 1 = 3 * m + 2 + 2 from by ring]
          exact r2
        · rw [show 3 * (m + 1) + 3 = 3 * m + 3 + 3 from by ring,
            show 3 * (m + 1) + 2 = 3 * m + 3 + 2 from by ring]
          exact r3
  intro n hn
  obtain ⟨m, r, hr, rfl⟩ : ∃ m r, r < 3 ∧ n = 3 * m + r + 1 := ⟨(n - 1) / 3, (n - 1) % 3, Nat.mod_lt _ (by norm_num),
    by omega⟩
  interval_cases r
  · have := (main m).1
    simpa using this
  · have := (main m).2.1
    have e1 : 3 * m + 1 + 1 = 3 * m + 2 := by ring
    rw [e1]
    simpa using this
  · have := (main m).2.2
    have e1 : 3 * m + 2 + 1 = 3 * m + 3 := by ring
    rw [e1]
    simpa using this

/-! ## Stage F (early win) — the two finite witnesses -/

/-- **Exact `n = 6` witness.**  Unrolling the recurrence six steps gives
`C₆^{(h)} = −39521 h⁵ / 32400` exactly, as a polynomial identity in `h`. -/
theorem zagC_six_eq (h : ℤ) : zagC h 6 = -39521 * (h : ℚ) ^ 5 / 32400 := by
  show zagC h (4 + 2) = -39521 * (h : ℚ) ^ 5 / 32400
  norm_num [zagC]
  ring

/-- `L₆ = lcm(1,…,6) = 60`. -/
theorem lcmUpto_six : Nat.lcmUpto 6 = 60 := by decide

/-- `L₆² C₆^{(h)} = −39521 h⁵ / 9`. -/
theorem lcmUpto_six_sq_mul_zagC_six (h : ℤ) :
    (Nat.lcmUpto 6 : ℚ) ^ 2 * zagC h 6 = -39521 * (h : ℚ) ^ 5 / 9 := by
  rw [lcmUpto_six, zagC_six_eq]
  norm_num
  ring

/-- **Necessity.**  If `L₆² C₆^{(h)}` is an integer then `3 ∣ h`.  Since `39521` is not
divisible by `3`, integrality at `n = 6` alone forces `3 ∣ h`; this is the necessity
half of the target iff theorem `thm:zagB`. -/
theorem zagC6_forces_three_dvd (h : ℤ) (z : ℤ)
    (hz : (Nat.lcmUpto 6 : ℚ) ^ 2 * zagC h 6 = (z : ℚ)) : (3 : ℤ) ∣ h := by
  rw [lcmUpto_six_sq_mul_zagC_six] at hz
  -- `-39521 h^5 / 9 = z` as rationals ⟹ `-39521 h^5 = 9 z` as integers.
  have hz' : (-(39521 * h ^ 5) : ℤ) = 9 * z := by
    have h9 : (9 : ℚ) ≠ 0 := by norm_num
    have := hz
    field_simp at this
    exact_mod_cast this
  have h3dvd : (3 : ℤ) ∣ 39521 * h ^ 5 := by
    refine ⟨-3 * z, ?_⟩
    linarith [hz']
  have h3prime : Prime (3 : ℤ) := by norm_num
  have h3ndvd39521 : ¬ (3 : ℤ) ∣ 39521 := by decide
  have h3dvdh5 : (3 : ℤ) ∣ h ^ 5 := by
    rcases (h3prime.dvd_mul).1 h3dvd with h1 | h2
    · exact absurd h1 h3ndvd39521
    · exact h2
  exact h3prime.dvd_of_dvd_pow h3dvdh5

/-- **Exact `n = 2` witness at `h = 3`.**  `C₂^{(3)} = 21/4`. -/
theorem zagC_two_eq_at_three : zagC 3 2 = 21 / 4 := by
  show zagC 3 (0 + 2) = 21 / 4
  norm_num [zagC]

/-- `L₂ = 2`. -/
theorem lcmUpto_two : Nat.lcmUpto 2 = 2 := by decide

/-- **Optimality of the exponent `2`.**  At `h = 3`, `L₂ · C₂^{(3)} = 21/2 ∉ ℤ`; hence the
exponent `1` (unlike `2`) does *not* suffice to make the companion integral, showing the
exponent `2` in the main theorem cannot be lowered. -/
theorem zagC2_not_scaled_integral :
    ¬ ∃ z : ℤ, (Nat.lcmUpto 2 : ℚ) * zagC 3 2 = (z : ℚ) := by
  rw [lcmUpto_two, zagC_two_eq_at_three]
  rintro ⟨z, hz⟩
  have : (21 : ℚ) / 2 = (z : ℚ) := by norm_num at hz ⊢; linarith
  have hz' : (21 : ℤ) = 2 * z := by
    have := this
    field_simp at this
    exact_mod_cast this
  omega

/-! ## Stage D — the mod-3 residue-imbalance counting lemma -/

/-- Closed form for the number of elements of `Icc lo hi` congruent to `r` mod `3`,
via the bijection `t ↦ lo' + 3*t` where `lo'` is the least element of `Icc lo hi`'s
ambient range that is `≥ lo` and `≡ r (mod 3)`. -/
theorem card_filter_mod3_eq (lo hi r : ℕ) (hr : r < 3) :
    ((Finset.Icc lo hi).filter (fun i => i % 3 = r)).card =
      if hi < lo + (r + 3 - lo % 3) % 3 then 0
      else (hi - (lo + (r + 3 - lo % 3) % 3)) / 3 + 1 := by
  set lo' := lo + (r + 3 - lo % 3) % 3 with hlo'
  have hlo'r : lo' % 3 = r := by omega
  have hlo'ge : lo ≤ lo' := by omega
  have hlo'lt : lo' < lo + 3 := by omega
  by_cases hc : hi < lo'
  · rw [if_pos hc]
    apply Finset.card_eq_zero.mpr
    ext x
    simp only [Finset.mem_filter, Finset.mem_Icc, Finset.notMem_empty, iff_false]
    rintro ⟨⟨hxlo, hxhi⟩, hxr⟩
    have hxge : lo' ≤ x := by omega
    omega
  · rw [if_neg hc]
    push_neg at hc
    set k := (hi - lo') / 3 + 1 with hk
    have hinj : Set.InjOn (fun t => lo' + 3 * t) (Finset.range k) := by
      intro a _ b _ hab
      simp only at hab
      omega
    have himg := Finset.card_image_of_injOn hinj
    have hfe : (Finset.Icc lo hi).filter (fun i => i % 3 = r)
        = Finset.image (fun t => lo' + 3 * t) (Finset.range k) := by
      ext x
      simp only [Finset.mem_image, Finset.mem_range, Finset.mem_filter, Finset.mem_Icc]
      constructor
      · rintro ⟨⟨h1, h2⟩, h3⟩
        refine ⟨(x - lo') / 3, ?_, ?_⟩
        · rw [hk]; omega
        · omega
      · rintro ⟨t, ht, rfl⟩
        rw [hk] at ht
        refine ⟨⟨by omega, by omega⟩, by omega⟩
    rw [hfe, himg, Finset.card_range]

/-- **The mod-3 residue-imbalance counting lemma.** In any interval `Icc lo hi`, the
count of elements `≡ r1 (mod 3)` and the count of elements `≡ r2 (mod 3)` differ by at
most `1`, for any two residues `r1, r2 < 3`. Direct analogue of
`CatalanEndpoint.lean`'s `card_even_odd_diff_le_one`, proved instead via the closed
form `card_filter_mod3_eq` (rather than a stride-`3` induction), since the closed
forms for two different residues reduce the comparison to a pure arithmetic fact about
floor division that `omega` closes directly. -/
theorem card_mod3_diff_le_one (lo hi r1 r2 : ℕ) (hr1 : r1 < 3) (hr2 : r2 < 3) :
    ((Finset.Icc lo hi).filter (fun i => i % 3 = r1)).card ≤
      ((Finset.Icc lo hi).filter (fun i => i % 3 = r2)).card + 1 := by
  rw [card_filter_mod3_eq lo hi r1 hr1, card_filter_mod3_eq lo hi r2 hr2]
  have e1 : lo + (r1 + 3 - lo % 3) % 3 < lo + 3 := by omega
  have e2 : lo + (r2 + 3 - lo % 3) % 3 < lo + 3 := by omega
  split_ifs <;> omega

/-- Generalization of `card_mod3_diff_le_one` to multiples of `d`, for `d` coprime to
`3`: in any interval `Icc a b`, the counts of multiples of `d` in two residue classes
mod `3` differ by at most `1`. Proved via the bijection `i ↦ i / d` (mirroring
`CatalanEndpoint.lean`'s `card_even_odd_diff_le_one_multiples`, generalized from the
parity-preserving case `d` odd to the mod-3-residue-transforming case `d` coprime to
`3`: `i = d * k` has `i % 3 = r ↔ k % 3 = (r * d) % 3`, since `d % 3 ∈ {1, 2}` is
self-inverse mod `3`). -/
theorem card_mod3_diff_le_one_multiples (d a b r1 r2 : ℕ) (hd3 : ¬ (3 : ℕ) ∣ d)
    (hdpos : 0 < d) (hr1 : r1 < 3) (hr2 : r2 < 3) :
    ((Finset.Icc a b).filter (fun i => d ∣ i ∧ i % 3 = r1)).card ≤
      ((Finset.Icc a b).filter (fun i => d ∣ i ∧ i % 3 = r2)).card + 1 := by
  set lo := (a + d - 1) / d with hlo
  set hi := b / d with hhi
  have hdmod : d % 3 = 1 ∨ d % 3 = 2 := by omega
  have hconv : ∀ x y : ℕ, ((d * x) % 3 = y % 3 ↔ x % 3 = (y * d) % 3) := by
    intro x y
    rw [Nat.mul_mod, Nat.mul_mod y d]
    rcases hdmod with h | h <;> rw [h] <;> omega
  have hcard : ∀ r : ℕ, r < 3 →
      ((Finset.Icc a b).filter (fun i => d ∣ i ∧ i % 3 = r)).card
        = ((Finset.Icc lo hi).filter (fun k => k % 3 = (r * d) % 3)).card := by
    intro r hr
    apply Finset.card_bij (fun i _ => i / d)
    · intro i hi'
      simp only [Finset.mem_filter, Finset.mem_Icc] at hi'
      obtain ⟨⟨ha, hb⟩, hdvd, hmod⟩ := hi'
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
        have := (hconv k r).mp (by rw [Nat.mod_eq_of_lt hr]; exact hmod)
        omega
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
      obtain ⟨⟨hklo, hkhi⟩, hkmod⟩ := hk'
      refine ⟨d * k, ?_, ?_⟩
      · simp only [Finset.mem_filter, Finset.mem_Icc]
        refine ⟨⟨?_, ?_⟩, ⟨k, rfl⟩, ?_⟩
        · rw [hlo, Nat.div_le_iff_le_mul_add_pred hdpos] at hklo
          omega
        · rw [hhi] at hkhi
          rw [Nat.le_div_iff_mul_le hdpos] at hkhi
          rw [mul_comm] at hkhi
          omega
        · have := (hconv k r).mpr hkmod
          omega
      · rw [Nat.mul_div_cancel_left k hdpos]
  rw [hcard r1 hr1, hcard r2 hr2]
  have hr1' : (r1 * d) % 3 < 3 := Nat.mod_lt _ (by norm_num)
  have hr2' : (r2 * d) % 3 < 3 := Nat.mod_lt _ (by norm_num)
  exact card_mod3_diff_le_one lo hi ((r1 * d) % 3) ((r2 * d) % 3) hr1' hr2'

/-! ## Stage D (continued) — `zagNum`/`zagDen` as filtered products over `Icc (j+1) n` -/

/-- The "square root" of `zagDen`: `D = ∏_{t=0}^{r} (j+1+3t)`, so `zagDen = D^2`. -/
def zagDenRoot (n j : ℕ) : ℕ :=
  ∏ t ∈ Finset.range (zagQ n j + 1), (j + 1 + 3 * t)

theorem zagDen_eq_sq (n j : ℕ) : zagDen n j = (zagDenRoot n j) ^ 2 := by
  unfold zagDen zagDenRoot
  rw [← Finset.prod_pow]

/-- `zagNum` splits as a product of the "class-`j+2`" factors and the "class-`j`"
factors. -/
def zagNumB (n j : ℕ) : ℕ := ∏ t ∈ Finset.range (zagQ n j), (j + 2 + 3 * t)

def zagNumC (n j : ℕ) : ℕ := ∏ t ∈ Finset.range (zagQ n j), (j + 3 + 3 * t)

theorem zagNum_eq_mul (n j : ℕ) : zagNum n j = zagNumB n j * zagNumC n j := by
  unfold zagNum zagNumB zagNumC
  rw [← Finset.prod_mul_distrib]

/-- `zagDenRoot` reindexed as the product over the "class-`(j+1)`" filter of
`Icc (j+1) n`. -/
theorem zagDenRoot_eq_prod_filter (n j : ℕ) (hj : j < n) (hmod : n % 3 = (j + 1) % 3) :
    zagDenRoot n j = ∏ i ∈ (Finset.Icc (j + 1) n).filter (fun i => i % 3 = (j + 1) % 3), i := by
  unfold zagDenRoot
  set r := zagQ n j with hr
  have hnr : n = j + 1 + 3 * r := by unfold zagQ at hr; omega
  have hinj : Set.InjOn (fun t => j + 1 + 3 * t) (Finset.range (r + 1) : Finset ℕ) := by
    intro a _ b _ hab; simp only at hab; omega
  have himg := Finset.prod_image (f := (id : ℕ → ℕ)) (g := fun t => j + 1 + 3 * t) hinj
  simp only [id] at himg
  rw [← himg]
  congr 1
  ext i
  simp only [Finset.mem_image, Finset.mem_range, Finset.mem_filter, Finset.mem_Icc]
  constructor
  · rintro ⟨t, ht, rfl⟩
    refine ⟨⟨by omega, by omega⟩, by omega⟩
  · rintro ⟨⟨h1, h2⟩, hpar⟩
    refine ⟨(i - j - 1) / 3, ?_, ?_⟩ <;> omega

/-- `zagNumB` reindexed as the product over the "class-`(j+2)`" filter of
`Icc (j+1) n`. -/
theorem zagNumB_eq_prod_filter (n j : ℕ) (hj : j < n) (hmod : n % 3 = (j + 1) % 3) :
    zagNumB n j = ∏ i ∈ (Finset.Icc (j + 1) n).filter (fun i => i % 3 = (j + 2) % 3), i := by
  unfold zagNumB
  set r := zagQ n j with hr
  have hnr : n = j + 1 + 3 * r := by unfold zagQ at hr; omega
  have hinj : Set.InjOn (fun t => j + 2 + 3 * t) (Finset.range r : Finset ℕ) := by
    intro a _ b _ hab; simp only at hab; omega
  have himg := Finset.prod_image (f := (id : ℕ → ℕ)) (g := fun t => j + 2 + 3 * t) hinj
  simp only [id] at himg
  rw [← himg]
  congr 1
  ext i
  simp only [Finset.mem_image, Finset.mem_range, Finset.mem_filter, Finset.mem_Icc]
  constructor
  · rintro ⟨t, ht, rfl⟩
    refine ⟨⟨by omega, by omega⟩, by omega⟩
  · rintro ⟨⟨h1, h2⟩, hpar⟩
    refine ⟨(i - j - 2) / 3, ?_, ?_⟩ <;> omega

/-- `zagNumC` reindexed as the product over the "class-`j`" filter of `Icc (j+1) n`. -/
theorem zagNumC_eq_prod_filter (n j : ℕ) (hj : j < n) (hmod : n % 3 = (j + 1) % 3) :
    zagNumC n j = ∏ i ∈ (Finset.Icc (j + 1) n).filter (fun i => i % 3 = j % 3), i := by
  unfold zagNumC
  set r := zagQ n j with hr
  have hnr : n = j + 1 + 3 * r := by unfold zagQ at hr; omega
  have hinj : Set.InjOn (fun t => j + 3 + 3 * t) (Finset.range r : Finset ℕ) := by
    intro a _ b _ hab; simp only at hab; omega
  have himg := Finset.prod_image (f := (id : ℕ → ℕ)) (g := fun t => j + 3 + 3 * t) hinj
  simp only [id] at himg
  rw [← himg]
  congr 1
  ext i
  simp only [Finset.mem_image, Finset.mem_range, Finset.mem_filter, Finset.mem_Icc]
  constructor
  · rintro ⟨t, ht, rfl⟩
    refine ⟨⟨by omega, by omega⟩, by omega⟩
  · rintro ⟨⟨h1, h2⟩, hpar⟩
    refine ⟨(i - j - 3) / 3, ?_, ?_⟩ <;> omega

/-! ## Stage D (continued) — the `p ≠ 3` valuation bound -/

/-- The per-`(p,i)` class-count bound: for `p` coprime to `3`, the "class-`(j+1)`"
count of multiples of `p^i` in `Icc (j+1) n` exceeds the "class-`r`" count (for any
`r < 3`) by at most `1`. -/
theorem zag_card_bound (p i n j r : ℕ) (hp3 : ¬ (3 : ℕ) ∣ p) (hr : r < 3) :
    (((Finset.Icc (j + 1) n).filter (fun x => x % 3 = (j + 1) % 3)).filter
        (p ^ i ∣ ·)).card ≤
      (((Finset.Icc (j + 1) n).filter (fun x => x % 3 = r)).filter (p ^ i ∣ ·)).card + 1 := by
  rw [Finset.filter_filter, Finset.filter_filter]
  have e1 : (Finset.Icc (j + 1) n).filter (fun x => x % 3 = (j + 1) % 3 ∧ p ^ i ∣ x)
      = (Finset.Icc (j + 1) n).filter (fun x => p ^ i ∣ x ∧ x % 3 = (j + 1) % 3) := by
    apply Finset.filter_congr; intro x _; exact and_comm
  have e2 : (Finset.Icc (j + 1) n).filter (fun x => x % 3 = r ∧ p ^ i ∣ x)
      = (Finset.Icc (j + 1) n).filter (fun x => p ^ i ∣ x ∧ x % 3 = r) := by
    apply Finset.filter_congr; intro x _; exact and_comm
  rw [e1, e2]
  have hd3 : ¬ (3 : ℕ) ∣ p ^ i := by
    intro hdvd
    have h3p : (3 : ℕ).Prime := by norm_num
    exact hp3 (h3p.dvd_of_dvd_pow hdvd)
  have hdpos : 0 < p ^ i := by
    rcases Nat.eq_zero_or_pos p with hp0 | hp0
    · subst hp0; simp at hp3
    · positivity
  exact card_mod3_diff_le_one_multiples (p ^ i) (j + 1) n ((j + 1) % 3) r hd3 hdpos
    (Nat.mod_lt _ (by norm_num)) hr

/-- **The `p ≠ 3` valuation bound.** For a prime `p ≠ 3`, `zagDenRoot`'s `p`-adic
valuation exceeds each of `zagNumB`'s and `zagNumC`'s by at most `p.log n` — the exact
valuation of `Nat.lcmUpto n` at `p`. Direct analogue of `CatalanEndpoint.lean`'s
`endpointDen_val_le_odd`. -/
theorem zagDenRoot_val_le (p n j : ℕ) (hp : p.Prime) (hp3 : p ≠ 3) (hj : j < n)
    (hmod : n % 3 = (j + 1) % 3) :
    (zagDenRoot n j).factorization p ≤ (zagNumB n j).factorization p + p.log n ∧
    (zagDenRoot n j).factorization p ≤ (zagNumC n j).factorization p + p.log n := by
  have hp3' : ¬ (3 : ℕ) ∣ p := by
    intro hdvd
    have h3p : (3 : ℕ).Prime := by norm_num
    exact hp3 ((Nat.prime_dvd_prime_iff_eq h3p hp).mp hdvd).symm
  rw [zagDenRoot_eq_prod_filter n j hj hmod]
  set b := p.log n + 1 with hb
  have hsD : ∀ x ∈ (Finset.Icc (j + 1) n).filter (fun x => x % 3 = (j + 1) % 3), x ≠ 0 := by
    intro x hx; simp only [Finset.mem_filter, Finset.mem_Icc] at hx; omega
  have hbD : ∀ x ∈ (Finset.Icc (j + 1) n).filter (fun x => x % 3 = (j + 1) % 3),
      Nat.log p x < b := by
    intro x hx
    simp only [Finset.mem_filter, Finset.mem_Icc] at hx
    exact lt_of_le_of_lt (Nat.log_mono_right hx.1.2) (by omega)
  rw [factorization_prod_eq_sum_card hp _ hsD b hbD]
  constructor
  · rw [zagNumB_eq_prod_filter n j hj hmod]
    have hsN : ∀ x ∈ (Finset.Icc (j + 1) n).filter (fun x => x % 3 = (j + 2) % 3),
        x ≠ 0 := by intro x hx; simp only [Finset.mem_filter, Finset.mem_Icc] at hx; omega
    have hbN : ∀ x ∈ (Finset.Icc (j + 1) n).filter (fun x => x % 3 = (j + 2) % 3),
        Nat.log p x < b := by
      intro x hx
      simp only [Finset.mem_filter, Finset.mem_Icc] at hx
      exact lt_of_le_of_lt (Nat.log_mono_right hx.1.2) (by omega)
    rw [factorization_prod_eq_sum_card hp _ hsN b hbN]
    have hpt : ∀ i ∈ Finset.Ico 1 b,
        (((Finset.Icc (j + 1) n).filter (fun x => x % 3 = (j + 1) % 3)).filter
          (p ^ i ∣ ·)).card
          ≤ (((Finset.Icc (j + 1) n).filter (fun x => x % 3 = (j + 2) % 3)).filter
              (p ^ i ∣ ·)).card + 1 :=
      fun i _ => zag_card_bound p i n j ((j + 2) % 3) hp3' (Nat.mod_lt _ (by norm_num))
    calc ∑ i ∈ Finset.Ico 1 b,
          (((Finset.Icc (j + 1) n).filter (fun x => x % 3 = (j + 1) % 3)).filter
            (p ^ i ∣ ·)).card
        ≤ ∑ i ∈ Finset.Ico 1 b,
          ((((Finset.Icc (j + 1) n).filter (fun x => x % 3 = (j + 2) % 3)).filter
            (p ^ i ∣ ·)).card + 1) := Finset.sum_le_sum hpt
      _ = (∑ i ∈ Finset.Ico 1 b,
            (((Finset.Icc (j + 1) n).filter (fun x => x % 3 = (j + 2) % 3)).filter
              (p ^ i ∣ ·)).card)
          + (Finset.Ico 1 b).card := by rw [Finset.sum_add_distrib]; simp
      _ = _ := by rw [Nat.card_Ico]; omega
  · rw [zagNumC_eq_prod_filter n j hj hmod]
    have hsN : ∀ x ∈ (Finset.Icc (j + 1) n).filter (fun x => x % 3 = j % 3), x ≠ 0 := by
      intro x hx; simp only [Finset.mem_filter, Finset.mem_Icc] at hx; omega
    have hbN : ∀ x ∈ (Finset.Icc (j + 1) n).filter (fun x => x % 3 = j % 3),
        Nat.log p x < b := by
      intro x hx
      simp only [Finset.mem_filter, Finset.mem_Icc] at hx
      exact lt_of_le_of_lt (Nat.log_mono_right hx.1.2) (by omega)
    rw [factorization_prod_eq_sum_card hp _ hsN b hbN]
    have hpt : ∀ i ∈ Finset.Ico 1 b,
        (((Finset.Icc (j + 1) n).filter (fun x => x % 3 = (j + 1) % 3)).filter
          (p ^ i ∣ ·)).card
          ≤ (((Finset.Icc (j + 1) n).filter (fun x => x % 3 = j % 3)).filter
              (p ^ i ∣ ·)).card + 1 :=
      fun i _ => zag_card_bound p i n j (j % 3) hp3' (Nat.mod_lt _ (by norm_num))
    calc ∑ i ∈ Finset.Ico 1 b,
          (((Finset.Icc (j + 1) n).filter (fun x => x % 3 = (j + 1) % 3)).filter
            (p ^ i ∣ ·)).card
        ≤ ∑ i ∈ Finset.Ico 1 b,
          ((((Finset.Icc (j + 1) n).filter (fun x => x % 3 = j % 3)).filter
            (p ^ i ∣ ·)).card + 1) := Finset.sum_le_sum hpt
      _ = (∑ i ∈ Finset.Ico 1 b,
            (((Finset.Icc (j + 1) n).filter (fun x => x % 3 = j % 3)).filter
              (p ^ i ∣ ·)).card)
          + (Finset.Ico 1 b).card := by rw [Finset.sum_add_distrib]; simp
      _ = _ := by rw [Nat.card_Ico]; omega

theorem zagNumB_ne_zero (n j : ℕ) : zagNumB n j ≠ 0 := by
  unfold zagNumB; apply Finset.prod_ne_zero_iff.mpr; intro t _; omega

theorem zagNumC_ne_zero (n j : ℕ) : zagNumC n j ≠ 0 := by
  unfold zagNumC; apply Finset.prod_ne_zero_iff.mpr; intro t _; omega

theorem zagDenRoot_ne_zero (n j : ℕ) : zagDenRoot n j ≠ 0 := by
  unfold zagDenRoot; apply Finset.prod_ne_zero_iff.mpr; intro t _; omega

/-- **The `p ≠ 3` combined valuation bound.** `v_p(zagDen) ≤ v_p(zagNum) + 2 v_p(L_n)`
for every prime `p ≠ 3`. -/
theorem zagDen_val_le_ne3 (p n j : ℕ) (hp : p.Prime) (hp3 : p ≠ 3) (hj : j < n)
    (hmod : n % 3 = (j + 1) % 3) :
    (zagDen n j).factorization p ≤ (zagNum n j).factorization p
      + 2 * (Nat.lcmUpto n).factorization p := by
  obtain ⟨hB, hC⟩ := zagDenRoot_val_le p n j hp hp3 hj hmod
  rw [zagDen_eq_sq, zagNum_eq_mul, Nat.factorization_pow,
    Nat.factorization_mul (zagNumB_ne_zero n j) (zagNumC_ne_zero n j),
    Nat.factorization_lcmUpto n hp]
  simp only [Finsupp.smul_apply, Finsupp.add_apply, smul_eq_mul]
  omega

/-! ## Stage D (continued) — the `p = 3` "maximal factor" valuation bound -/

/-- Telescoping identity: `(m-1)! * ∏_{t=0}^{r} (m+t) = (m+r)!`, for `m ≥ 1`. -/
theorem prod_range_add_eq_factorial_div (m r : ℕ) (hm : 1 ≤ m) :
    Nat.factorial (m - 1) * (∏ t ∈ Finset.range (r + 1), (m + t)) = Nat.factorial (m + r) := by
  induction r with
  | zero =>
      obtain ⟨m', rfl⟩ : ∃ m', m = m' + 1 := ⟨m - 1, by omega⟩
      rw [Nat.add_sub_cancel, Finset.prod_range_one, add_zero, Nat.factorial_succ]
      ring
  | succ r ih =>
      rw [Finset.prod_range_succ, ← mul_assoc, ih,
        show m + (r + 1) = (m + r) + 1 from by omega, Nat.factorial_succ]
      ring

/-- **The `p = 3` "maximal factor" valuation bound.** `2 * v_3(zagDenRoot n j) ≤
2 * v_3(L_n) + (n - 1)`, using that when `(j+1) % 3 = 0` (the only nontrivial case,
since otherwise every factor of `zagDenRoot` is coprime to `3`), `zagDenRoot n j =
3^(r+1) * D'` with `D' = m(m+1)⋯(m+r) ∣ (m+r)!` (where `j + 1 = 3m`), so
`v_3(D') ≤ v_3((m+r)!) ≤ (m+r)/2` (Legendre, via `Nat.factorization_factorial_le_div_pred`
at `p = 3`), and `n = 3(m+r)` lets the resulting bound be discharged by `omega`. -/
theorem zagDenRoot_val_le3 (n j : ℕ) (hj : j < n) (hmod : n % 3 = (j + 1) % 3) :
    2 * (zagDenRoot n j).factorization 3 ≤
      2 * (Nat.lcmUpto n).factorization 3 + (n - 1) := by
  by_cases hc : (j + 1) % 3 = 0
  · obtain ⟨m, hm⟩ : ∃ m, j + 1 = 3 * m := ⟨(j + 1) / 3, by omega⟩
    have hm1 : 1 ≤ m := by omega
    set r := zagQ n j with hr
    have hnr : n = j + 1 + 3 * r := by unfold zagQ at hr; omega
    have hn3 : n = 3 * (m + r) := by omega
    have hDeq : zagDenRoot n j
        = 3 ^ (r + 1) * (∏ t ∈ Finset.range (r + 1), (m + t)) := by
      unfold zagDenRoot
      rw [← hr, Finset.prod_congr rfl
        (show ∀ t ∈ Finset.range (r + 1), j + 1 + 3 * t = 3 * (m + t) from
          fun t _ => by omega)]
      rw [Finset.prod_mul_distrib]
      simp
    have hDdvd : (∏ t ∈ Finset.range (r + 1), (m + t)) ∣ Nat.factorial (m + r) := by
      refine ⟨Nat.factorial (m - 1), ?_⟩
      rw [← prod_range_add_eq_factorial_div m r hm1]
      ring
    have hDne : (∏ t ∈ Finset.range (r + 1), (m + t)) ≠ 0 := by
      apply Finset.prod_ne_zero_iff.mpr; intro t _; omega
    have hDfacle : (∏ t ∈ Finset.range (r + 1), (m + t)).factorization 3
        ≤ (Nat.factorial (m + r)).factorization 3 :=
      (Nat.factorization_le_iff_dvd hDne (Nat.factorial_ne_zero _)).mpr hDdvd 3
    have hlegendre : (Nat.factorial (m + r)).factorization 3 ≤ (m + r) / 2 := by
      have := Nat.factorization_factorial_le_div_pred (p := 3) (by norm_num) (m + r)
      simpa using this
    have hfac : (zagDenRoot n j).factorization 3
        = (r + 1) + (∏ t ∈ Finset.range (r + 1), (m + t)).factorization 3 := by
      rw [hDeq, Nat.factorization_mul (by positivity) hDne, Nat.factorization_pow]
      simp [Nat.Prime.factorization_self (p := 3) (by norm_num)]
    have hL3 : 1 ≤ (Nat.lcmUpto n).factorization 3 := by
      rw [Nat.factorization_lcmUpto n (by norm_num)]
      exact Nat.log_pos (by norm_num) (by omega)
    omega
  · have hzero : (zagDenRoot n j).factorization 3 = 0 := by
      apply Nat.factorization_eq_zero_of_not_dvd
      unfold zagDenRoot
      have hp3 : Prime (3 : ℕ) := (by norm_num : Nat.Prime 3).prime
      apply hp3.not_dvd_finsetProd
      intro t _ hdvd
      have hmodeq : (j + 1 + 3 * t) % 3 = (j + 1) % 3 := by omega
      exact hc (by omega)
    omega

/-! ## Stage D (continued) — assembling `zagDen_dvd` (DIV) and `zagR` integrality -/

theorem zagNum_ne_zero (n j : ℕ) : zagNum n j ≠ 0 := by
  unfold zagNum; apply Finset.prod_ne_zero_iff.mpr; intro t _; positivity

/-- **DIV.** The key natural-number denominator divisibility for the Zagier-B
endpoint, given `3 ∣ hnat` (the hypothesis coming from `3 ∣ h` in the ambient integer
parameter). -/
theorem zagDen_dvd (hnat n j : ℕ) (h3 : 3 ∣ hnat) (hj : j < n)
    (hmod : n % 3 = (j + 1) % 3) :
    zagDen n j ∣ (Nat.lcmUpto n) ^ 2 * zagNum n j * hnat ^ (n - 1) := by
  have hDenNe : zagDen n j ≠ 0 := zagDen_ne_zero n j
  have hNumNe : zagNum n j ≠ 0 := zagNum_ne_zero n j
  have hlcmNe : Nat.lcmUpto n ≠ 0 := Nat.lcmUpto_ne_zero n
  by_cases hh : hnat = 0
  · -- if hnat = 0 then n - 1 ≥ 1 forces RHS = 0 only when n ≥ 2; handle n = 1 separately
    subst hh
    rcases Nat.eq_zero_or_pos (n - 1) with hn1 | hn1
    · -- n - 1 = 0, i.e. n ≤ 1; combined with hj : j < n forces n = 1, j = 0
      have hn1' : n = 1 := by omega
      subst hn1'
      have hj0 : j = 0 := by omega
      subst hj0
      have : zagDen 1 0 = 1 := by
        unfold zagDen zagQ; norm_num
      rw [this]
      simp
    · have : (0 : ℕ) ^ (n - 1) = 0 := by
        exact zero_pow (by omega)
      simp [this]
  have hhpowNe : hnat ^ (n - 1) ≠ 0 := pow_ne_zero _ hh
  have hRHSNe : (Nat.lcmUpto n) ^ 2 * zagNum n j * hnat ^ (n - 1) ≠ 0 :=
    mul_ne_zero (mul_ne_zero (pow_ne_zero _ hlcmNe) hNumNe) hhpowNe
  rw [← Nat.factorization_le_iff_dvd hDenNe hRHSNe, Finsupp.le_def]
  intro p
  by_cases hp : p.Prime
  · have hfac : ((Nat.lcmUpto n) ^ 2 * zagNum n j * hnat ^ (n - 1)).factorization p
        = 2 * (Nat.lcmUpto n).factorization p + (zagNum n j).factorization p
          + (n - 1) * hnat.factorization p := by
      rw [Nat.factorization_mul (mul_ne_zero (pow_ne_zero _ hlcmNe) hNumNe) hhpowNe,
        Nat.factorization_mul (pow_ne_zero _ hlcmNe) hNumNe, Nat.factorization_pow,
        Nat.factorization_pow]
      simp
    rw [hfac]
    by_cases hp3 : p = 3
    · subst hp3
      have hb := zagDenRoot_val_le3 n j hj hmod
      have hDeq : (zagDen n j).factorization 3 = 2 * (zagDenRoot n j).factorization 3 := by
        rw [zagDen_eq_sq, Nat.factorization_pow]; simp
      have hh3 : 1 ≤ hnat.factorization 3 :=
        (Nat.Prime.dvd_iff_one_le_factorization (by norm_num) hh).mp h3
      have hNumNn : 0 ≤ (zagNum n j).factorization 3 := Nat.zero_le _
      rw [hDeq]
      have hstep : (n - 1) * hnat.factorization 3 ≥ (n - 1) * 1 := by
        exact Nat.mul_le_mul_left _ hh3
      omega
    · have hp3' : ¬ (3 : ℕ) ∣ p := by
        intro hdvd
        exact hp3 ((Nat.prime_dvd_prime_iff_eq (by norm_num) hp).mp hdvd).symm
      have hbne3 : p ≠ 3 := hp3
      have hb := zagDen_val_le_ne3 p n j hp hbne3 hj hmod
      have hnn : 0 ≤ (n - 1) * hnat.factorization p := Nat.zero_le _
      omega
  · simp [Nat.factorization_eq_zero_of_not_prime _ hp]

/-- **RL.** Casting `DIV` to `ℚ`, for an integer `h` with `3 ∣ h`: `L_n² h^(n-1) R(n,j)`
is always an integer, for `j < n` with `n ≡ j+1 (mod 3)`. -/
theorem zagR_lcm_sq_integral (h : ℤ) (h3 : (3 : ℤ) ∣ h) (n j : ℕ) (hj : j < n)
    (hmod : n % 3 = (j + 1) % 3) :
    ∃ z : ℤ, (Nat.lcmUpto n : ℚ) ^ 2 * (h : ℚ) ^ (n - 1) * zagR n j = z := by
  have h3n : 3 ∣ h.natAbs := by
    have := Int.natAbs_dvd_natAbs.mpr h3
    simpa using this
  obtain ⟨c, hc⟩ := zagDen_dvd h.natAbs n j h3n hj hmod
  have hDenNe : (zagDen n j : ℚ) ≠ 0 := by
    exact_mod_cast zagDen_ne_zero n j
  have hcZ : (zagDen n j : ℤ) ∣ (Nat.lcmUpto n : ℤ) ^ 2 * (zagNum n j : ℤ)
      * (h.natAbs : ℤ) ^ (n - 1) := by
    refine ⟨(c : ℤ), ?_⟩
    exact_mod_cast hc
  have habsPow : (h.natAbs : ℤ) ^ (n - 1) = ((h ^ (n - 1)).natAbs : ℤ) := by
    have := Int.natAbs_pow h (n - 1)
    exact_mod_cast this.symm
  rw [habsPow] at hcZ
  have hDenNeZ : (zagDen n j : ℤ) ≠ 0 := by exact_mod_cast zagDen_ne_zero n j
  have hcZ' : (zagDen n j : ℤ) ∣ (Nat.lcmUpto n : ℤ) ^ 2 * (zagNum n j : ℤ) * (h ^ (n - 1)) := by
    generalize hk : h ^ (n - 1) = k at hcZ ⊢
    rcases Int.natAbs_eq k with heq | heq
    · rwa [← heq] at hcZ
    · have hrw : (Nat.lcmUpto n : ℤ) ^ 2 * (zagNum n j : ℤ) * k
          = -((Nat.lcmUpto n : ℤ) ^ 2 * (zagNum n j : ℤ) * (k.natAbs : ℤ)) := by
        conv_lhs => rw [heq]
        ring
      rw [hrw]
      exact hcZ.neg_right
  obtain ⟨c', hc'⟩ := hcZ'
  refine ⟨c', ?_⟩
  have hc'Q : (Nat.lcmUpto n : ℚ) ^ 2 * (zagNum n j : ℚ) * (h : ℚ) ^ (n - 1)
      = (zagDen n j : ℚ) * (c' : ℚ) := by exact_mod_cast hc'
  unfold zagR
  field_simp
  linear_combination hc'Q

/-! ## Stage E — sharp integrality and the full theorem -/

/-- `(lcmUpto n)^2 * h^(n-1) * zagSumR n` is an integer, given `3 ∣ h` and `1 ≤ n`. -/
theorem zagSumR_lcm_sq_integral (h : ℤ) (h3 : (3 : ℤ) ∣ h) (n : ℕ) :
    ∃ z : ℤ, (Nat.lcmUpto n : ℚ) ^ 2 * (h : ℚ) ^ (n - 1) * zagSumR n = z := by
  unfold zagSumR
  rw [Finset.mul_sum]
  apply ratInt_sum
  intro j hj
  by_cases hcond : n % 3 = (j + 1) % 3
  · rw [if_pos hcond]
    have hjn : j < n := Finset.mem_range.mp hj
    obtain ⟨z, hz⟩ := zagR_lcm_sq_integral h h3 n j hjn hcond
    exact ⟨z, by rw [← hz]⟩
  · rw [if_neg hcond]
    exact ⟨0, by simp⟩

/-- `(lcmUpto n)^2 * zagS h n` is an integer, given `3 ∣ h`. -/
theorem zagS_lcm_sq_integral (h : ℤ) (h3 : (3 : ℤ) ∣ h) (n : ℕ) :
    ∃ z : ℤ, (Nat.lcmUpto n : ℚ) ^ 2 * zagS h n = z := by
  rcases Nat.eq_zero_or_pos n with hn0 | hn1
  · subst hn0; exact ⟨0, by simp⟩
  · obtain ⟨z, hz⟩ := zagSumR_lcm_sq_integral h h3 n
    have hform := zagS_endpoint_formula h n hn1
    have hsq : (-1 : ℚ) ^ (n - 1) * (-1 : ℚ) ^ (n - 1) = 1 := by
      rw [← mul_pow]; norm_num
    have hzS : zagS h n = (-1 : ℚ) ^ (n - 1) * ((h : ℚ) ^ (n - 1) * zagSumR n) := by
      have hkey : (-1 : ℚ) ^ (n - 1) * ((-1 : ℚ) ^ (n - 1) * zagS h n)
          = (-1 : ℚ) ^ (n - 1) * ((h : ℚ) ^ (n - 1) * zagSumR n) := by
        rw [hform]
      rwa [← mul_assoc, hsq, one_mul] at hkey
    refine ⟨(-1) ^ (n - 1) * z, ?_⟩
    rw [hzS]
    have : (Nat.lcmUpto n : ℚ) ^ 2 * ((-1 : ℚ) ^ (n - 1) * ((h : ℚ) ^ (n - 1) * zagSumR n))
        = (-1 : ℚ) ^ (n - 1) * ((Nat.lcmUpto n : ℚ) ^ 2 * (h : ℚ) ^ (n - 1) * zagSumR n) := by
      ring
    rw [this, hz]
    push_cast
    ring

/-- **INV.** Binomial inversion recovering `zagC h` from `zagS h`. -/
theorem zag_binomial_inversion (h : ℤ) (n : ℕ) :
    zagC h n = ∑ k ∈ Finset.range (n + 1), (n.choose k : ℚ) * (h : ℚ) ^ (n - k) * zagS h k :=
  (binom_inv_general (zagC h) (zagS h) (h : ℚ) (fun _ => rfl) n).symm

/-- **SHARP.** For `3 ∣ h`: `(lcmUpto n)^2 * zagC h n` is an integer, for every `n`. -/
theorem zagC_sharp_denominator (h : ℤ) (h3 : (3 : ℤ) ∣ h) (n : ℕ) :
    ∃ z : ℤ, (Nat.lcmUpto n : ℚ) ^ 2 * zagC h n = z := by
  rw [zag_binomial_inversion h n, Finset.mul_sum]
  apply ratInt_sum
  intro k hk
  have hkn : k ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
  obtain ⟨zk, hzk⟩ := zagS_lcm_sq_integral h h3 k
  obtain ⟨m, hm⟩ := lcmUpto_dvd_lcmUpto hkn
  refine ⟨(n.choose k : ℤ) * h ^ (n - k) * m ^ 2 * zk, ?_⟩
  have hlcm : (Nat.lcmUpto n : ℚ) = (Nat.lcmUpto k : ℚ) * (m : ℚ) := by exact_mod_cast hm
  have hrw : (Nat.lcmUpto n : ℚ) ^ 2 * ((n.choose k : ℚ) * (h : ℚ) ^ (n - k) * zagS h k)
      = (n.choose k : ℚ) * (h : ℚ) ^ (n - k) * (m : ℚ) ^ 2
        * ((Nat.lcmUpto k : ℚ) ^ 2 * zagS h k) := by
    rw [hlcm]; ring
  rw [hrw, hzk]
  push_cast
  ring

/-- **The full sharp integrality theorem for the Zagier-B step-three companion.** -/
theorem zagC_sharp_iff (h : ℤ) :
    (∀ n : ℕ, ∃ z : ℤ, (Nat.lcmUpto n : ℚ) ^ 2 * zagC h n = z) ↔ 3 ∣ h := by
  constructor
  · intro hall
    obtain ⟨z, hz⟩ := hall 6
    exact zagC6_forces_three_dvd h z hz
  · intro h3 n
    exact zagC_sharp_denominator h h3 n

/-- **The `h = 3` corollary.** -/
theorem zagC_three_sharp_denominator :
    ∀ n : ℕ, ∃ z : ℤ, (Nat.lcmUpto n : ℚ) ^ 2 * zagC 3 n = z :=
  (zagC_sharp_iff 3).mpr ⟨1, by norm_num⟩

end ZetaLucas
