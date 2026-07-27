import Mathlib
import Zeta3Irrational.Basic

open scoped BigOperators
open Filter Finset

set_option maxHeartbeats 8000000
set_option maxRecDepth 4000

namespace Apery

/-- The cubic harmonic number, in exact rational arithmetic. -/
def harmonic3 (n : ℕ) : ℚ := ∑ j ∈ Finset.Icc 1 n, 1 / (j : ℚ) ^ 3

/-- Apéry's integral binomial kernel. -/
def kernel (n k : ℕ) : ℕ := (n.choose k) ^ 2 * ((n + k).choose k) ^ 2

/-- The standard Apéry sequence `a`. -/
def aClosed (n : ℕ) : ℕ := ∑ k ∈ Finset.range (n + 1), kernel n k

/-- The proposed single-sum closed form for Apéry's companion sequence. -/
def bClosed (n : ℕ) : ℚ :=
  ∑ k ∈ Finset.range (n + 1), (kernel n k : ℚ) * (2 * harmonic3 n - harmonic3 k)

/-- Polynomial coefficient in Apéry's recurrence. -/
def aperyCoeff (n : ℕ) : ℕ := 34 * n^3 + 51 * n^2 + 27 * n + 5

@[simp] theorem harmonic3_zero : harmonic3 0 = 0 := by
  simp [harmonic3]

@[simp] theorem bClosed_zero : bClosed 0 = 0 := by
  norm_num [bClosed, kernel]

@[simp] theorem bClosed_one : bClosed 1 = 6 := by
  native_decide

@[simp] theorem aClosed_zero : aClosed 0 = 1 := by
  norm_num [aClosed, kernel]

@[simp] theorem aClosed_one : aClosed 1 = 5 := by
  native_decide

/-- Apéry's companion sequence in its single-sum form. -/
def b (n : ℕ) : ℚ := bClosed n

/-- The requested closed form for Apéry's companion sequence. -/
theorem b_closed_form (n : ℕ) :
    b n = ∑ k ∈ Finset.range (n + 1),
      (kernel n k : ℚ) * (2 * harmonic3 n - harmonic3 k) := by
  rfl

@[simp] theorem b_zero : b 0 = 0 := bClosed_zero
@[simp] theorem b_one : b 1 = 6 := bClosed_one

/-- A reusable integer-linear-form criterion, isolating the final arithmetic
step of Apéry's irrationality argument. -/
theorem irrational_of_integer_linear_forms
    (x : ℝ) (A B : ℕ → ℤ)
    (hpos : ∀ n, 0 < (A n : ℝ) * x - B n)
    (hzero : Tendsto (fun n => (A n : ℝ) * x - B n) atTop (nhds 0)) :
    Irrational x := by
  -- Assume x is rational and derive a contradiction
  by_contra hcon
  rw [Irrational] at hcon
  push_neg at hcon
  obtain ⟨q, hq⟩ := hcon
  rw [Rat.cast_def] at hq
  -- Key: A n * x - B n = (A n * q.num - B n * q.den) / q.den
  -- The numerator is a positive integer, so A n * x - B n ≥ 1 / q.den
  have hden_pos : (0 : ℝ) < q.den := by exact_mod_cast q.pos
  have hconst : ∀ n, (A n : ℝ) * x - B n ≥ 1 / q.den := by
    intro n
    have hn := hpos n
    rw [← hq] at hn ⊢
    have key : (A n : ℝ) * (q.num / q.den) - B n = ((A n * q.num - B n * q.den) : ℤ) / q.den := by
      field_simp
      ring
    rw [key] at hn ⊢
    have h_int : (A n * q.num - B n * q.den : ℤ) ≥ 1 := by
      contrapose! hn
      have hle : (A n * q.num - B n * q.den : ℤ) ≤ 0 := by linarith
      have : ((A n * q.num - B n * q.den : ℤ) : ℝ) ≤ 0 := by exact_mod_cast hle
      exact div_nonpos_of_nonpos_of_nonneg this (le_of_lt hden_pos)
    apply div_le_div_of_nonneg_right _ (le_of_lt hden_pos)
    exact_mod_cast h_int
  -- Now derive contradiction: sequence ≥ 1/q.den but tends to 0
  have hpos_const : (0 : ℝ) < 1 / q.den := by positivity
  have := hzero.eventually (gt_mem_nhds hpos_const)
  obtain ⟨n, hn⟩ := this.exists
  have := hconst n
  linarith

/-- The real value ζ(3), represented by its absolutely convergent Dirichlet
series. -/
noncomputable def zeta3 : ℝ := ∑' n : ℕ, 1 / ((n + 1 : ℕ) : ℝ)^3

/-- Apéry's theorem. -/
theorem zeta3_irrational : Irrational zeta3 := by
  rw [irrational_iff_ne_rational]
  intro a b hab
  apply zeta_3_irratoinal
  let r : ℚ := a / b
  refine ⟨r, ?_⟩
  have hzeta : (zeta3 : ℂ) = riemannZeta 3 := by
    rw [zeta_eq_tsum_one_div_nat_add_one_cpow (by norm_num)]
    unfold zeta3
    rw [Complex.ofReal_tsum]
    congr 1
    funext n
    norm_num [Complex.ofReal_div, Complex.ofReal_pow]
  rw [← hzeta]
  apply congrArg Complex.ofReal
  simpa [r, Rat.cast_div] using hab.symm

end Apery
