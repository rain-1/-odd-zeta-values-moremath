import Mathlib

open scoped BigOperators
open Filter

set_option maxHeartbeats 8000000
set_option maxRecDepth 4000
set_option autoImplicit false

namespace Apery

/-- The binomial kernel in the closed form. -/
def kernel (n k : ℕ) : ℕ := (n.choose k) ^ 2 * ((n + k).choose k) ^ 2

/-- The third harmonic number, regarded as a rational number. -/
def harmonic3 (n : ℕ) : ℚ := ∑ j ∈ Finset.Icc 1 n, (1 : ℚ) / (j : ℚ) ^ 3

/-- Apéry's integer sequence in its short binomial form. -/
def a (n : ℕ) : ℕ := ∑ k ∈ Finset.range (n + 1), kernel n k

/-- Apéry's rational companion in the one-harmonic-sum form. -/
def b (n : ℕ) : ℚ :=
  ∑ k ∈ Finset.range (n + 1),
    (kernel n k : ℚ) * (2 * harmonic3 n - harmonic3 k)

/-- `lcm(1,…,n)`, with the conventional value `d 0 = 1`. -/
def d (n : ℕ) : ℕ := Nat.lcm ((Finset.Icc 1 n).lcm id) 1

lemma harmonic3_zero : harmonic3 0 = 0 := by
  rfl

lemma a_zero : a 0 = 1 := by
  rfl

lemma a_one : a 1 = 5 := by
  rfl

lemma b_zero : b 0 = 0 := by
  simp [b, harmonic3_zero]

lemma b_one : b 1 = 6 := by
  native_decide

/-- Every integer from `1` through `n` divides `d n`. -/
lemma dvd_d (n j : ℕ) (hj₁ : 1 ≤ j) (hjn : j ≤ n) : j ∣ d n := by
  have hmem : j ∈ Finset.Icc 1 n := Finset.mem_Icc.mpr ⟨hj₁, hjn⟩
  exact (Finset.dvd_lcm hmem).trans (Nat.dvd_lcm_left _ 1)

/-- The termwise arithmetic observation behind the denominator bound. -/
lemma scaled_harmonic3_is_integer (n k : ℕ) (hkn : k ≤ n) :
    ∃ z : ℤ, (z : ℚ) = (d n : ℚ) ^ 3 * harmonic3 k := by
  let z : ℕ := ∑ j ∈ Finset.Icc 1 k, (d n / j) ^ 3
  refine ⟨z, ?_⟩
  change ((z : ℕ) : ℚ) = _
  simp only [z, harmonic3, Nat.cast_sum, Nat.cast_pow]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j hj
  have hj₁ : 1 ≤ j := (Finset.mem_Icc.mp hj).1
  have hjk : j ≤ k := (Finset.mem_Icc.mp hj).2
  have hjn : j ≤ n := hjk.trans hkn
  have hdvd : j ∣ d n := dvd_d n j hj₁ hjn
  have hj0q : (j : ℚ) ≠ 0 := by positivity
  rw [Nat.cast_div hdvd hj0q]
  field_simp

/-- The short formula makes the denominator bound termwise. -/
theorem denominator_bound (n : ℕ) :
    ∃ z : ℤ, (z : ℚ) = (d n : ℚ) ^ 3 * b n := by
  unfold b
  rw [mul_comm]
  rw [Finset.sum_mul]
  have key : ∀ i ∈ Finset.range (n + 1), ∃ z : ℤ, (z : ℚ) = (kernel n i : ℚ) * (2 * harmonic3 n - harmonic3 i) * (d n : ℚ) ^ 3 := by
    intro i hi
    have hi' : i ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hi)
    obtain ⟨zn, hzn⟩ := scaled_harmonic3_is_integer n n (le_refl n)
    obtain ⟨zi, hzi⟩ := scaled_harmonic3_is_integer n i hi'
    use (kernel n i) * (2 * zn - zi)
    push_cast
    rw [hzn, hzi]
    ring
  choose! z hz using key
  use ∑ i ∈ Finset.range (n + 1), z i
  push_cast
  rw [Finset.sum_congr rfl hz]

/-- The polynomial coefficient in Apéry's recurrence. -/
def recurrenceCoeff (n : ℕ) : ℚ := 34 * n ^ 3 + 51 * n ^ 2 + 27 * n + 5

/-- The recurrence used as the one external input in the note. -/
def SatisfiesRecurrence (u : ℕ → ℚ) : Prop :=
  ∀ n : ℕ, 1 ≤ n →
    ((n + 1 : ℕ) : ℚ) ^ 3 * u (n + 1) =
      recurrenceCoeff n * u n - (n : ℚ) ^ 3 * u (n - 1)

/-- Discrete Wronskian calculation for any two solutions of Apéry's recurrence. -/
lemma wronskian_step {u v : ℕ → ℚ}
    (hu : SatisfiesRecurrence u) (hv : SatisfiesRecurrence v)
    (n : ℕ) (hn : 1 ≤ n) :
    v (n + 1) * u n - v n * u (n + 1) =
      ((n : ℚ) / (n + 1 : ℕ)) ^ 3 *
        (v n * u (n - 1) - v (n - 1) * u n) := by
  have hu' := hu n hn
  have hv' := hv n hn
  -- Convert coercions: (↑(n+1) : ℚ) = (↑n + 1 : ℚ)
  have coerc : ((n + 1 : ℕ) : ℚ) = (n : ℚ) + 1 := by norm_cast
  rw [coerc] at hu' hv'
  -- Multiply hu' by v n and hv' by u n, then subtract
  have key : ((n : ℚ) + 1) ^ 3 * (v n * u (n + 1) - u n * v (n + 1)) =
             (n : ℚ) ^ 3 * (u n * v (n - 1) - v n * u (n - 1)) := by
    calc ((n : ℚ) + 1) ^ 3 * (v n * u (n + 1) - u n * v (n + 1))
        = v n * (((n : ℚ) + 1) ^ 3 * u (n + 1)) - u n * (((n : ℚ) + 1) ^ 3 * v (n + 1)) := by ring
      _ = v n * (recurrenceCoeff n * u n - (n : ℚ) ^ 3 * u (n - 1)) -
          u n * (recurrenceCoeff n * v n - (n : ℚ) ^ 3 * v (n - 1)) := by rw [hu', hv']
      _ = (n : ℚ) ^ 3 * (u n * v (n - 1) - v n * u (n - 1)) := by ring
  -- Now rearrange to get the desired form
  have h_nonzero : ((n : ℚ) + 1) ≠ 0 := by positivity
  simp only [coerc]
  field_simp
  linarith [key]

/-- Iterating the Wronskian step gives the exact value `6/n³`. -/
theorem wronskian_exact {u v : ℕ → ℚ}
    (hu : SatisfiesRecurrence u) (hv : SatisfiesRecurrence v)
    (hu0 : u 0 = 1) (hu1 : u 1 = 5)
    (hv0 : v 0 = 0) (hv1 : v 1 = 6) :
    ∀ n : ℕ, 1 ≤ n →
      v n * u (n - 1) - v (n - 1) * u n = 6 / (n : ℚ) ^ 3 := by
  intro n hn
  induction n with
  | zero => omega
  | succ n ih =>
    cases n with
    | zero =>
      simp [hu0, hu1, hv0, hv1]
    | succ n =>
      have hn' : 1 ≤ n + 1 := by omega
      have wronskian_step_result := wronskian_step hu hv (n + 1) hn'
      rw [ih hn'] at wronskian_step_result
      convert wronskian_step_result using 1
      field_simp

/-- The exact increment formula obtained by dividing the Wronskian identity. -/
lemma ratio_increment {u v : ℕ → ℚ} {n : ℕ} (hn : 1 ≤ n)
    (hu_n : u n ≠ 0) (hu_prev : u (n - 1) ≠ 0)
    (hW : v n * u (n - 1) - v (n - 1) * u n = 6 / (n : ℚ) ^ 3) :
    v n / u n - v (n - 1) / u (n - 1) =
      6 / ((n : ℚ) ^ 3 * u n * u (n - 1)) := by
  have hn' : (n : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr (Nat.one_le_iff_ne_zero.mp hn)
  have h1 : v n / u n - v (n - 1) / u (n - 1) = 
            (v n * u (n - 1) - v (n - 1) * u n) / (u n * u (n - 1)) := by
    field_simp [hu_n, hu_prev]
  rw [h1, hW]
  ring

/-- A finite version of the positive-tail identity; this is the telescoping
step before taking the limit. -/
lemma finite_positive_tail {u v : ℕ → ℚ} (n N : ℕ) (hnN : n ≤ N)
    (hinc : ∀ m, 1 ≤ m →
      v m / u m - v (m - 1) / u (m - 1) =
        6 / ((m : ℚ) ^ 3 * u m * u (m - 1))) :
    v N / u N - v n / u n =
      ∑ m ∈ Finset.Icc (n + 1) N,
        6 / ((m : ℚ) ^ 3 * u m * u (m - 1)) := by
  -- Use induction on the difference N - n
  have h : ∀ d, v (n + d) / u (n + d) - v n / u n =
      ∑ m ∈ Finset.Icc (n + 1) (n + d), 6 / ((m : ℚ) ^ 3 * u m * u (m - 1)) := by
    intro d
    induction d with
    | zero => simp
    | succ d ih =>
      have sum_eq : n + (d + 1) = n + d + 1 := by ring
      rw [sum_eq]
      have step : v (n + d + 1) / u (n + d + 1) - v (n + d) / u (n + d) =
          6 / ((n + d + 1 : ℕ) ^ 3 * u (n + d + 1) * u (n + d)) := by
        convert hinc (n + d + 1) (by omega) using 2
      have sum_split : Finset.Icc (n + 1) (n + d + 1) = Finset.Icc (n + 1) (n + d) ∪ {n + d + 1} := by
        ext m
        simp only [Finset.mem_Icc, Finset.mem_union, Finset.mem_singleton]
        omega
      have disjoint : Disjoint (Finset.Icc (n + 1) (n + d)) {n + d + 1} := by
        simp [Finset.disjoint_singleton_right, Finset.mem_Icc]
      rw [sum_split, Finset.sum_union disjoint]
      simp [Finset.sum_singleton]
      have h1 : v (n + d + 1) / u (n + d + 1) - v n / u n =
          (v (n + d + 1) / u (n + d + 1) - v (n + d) / u (n + d)) + (v (n + d) / u (n + d) - v n / u n) := by ring
      rw [h1, step, ih]
      simp [Nat.cast_add]
      ring
  exact h (N - n) |> fun h' => by simp_all [add_tsub_cancel_of_le hnN]

/-- A standard irrationality criterion: positive integer linear forms tending
zero rule out rationality. -/
theorem irrational_of_positive_integer_linear_forms
    (x : ℝ) (P Q : ℕ → ℤ)
    (hpos : ∀ n, 0 < (P n : ℝ) * x - (Q n : ℝ))
    (hzero : Tendsto (fun n => (P n : ℝ) * x - (Q n : ℝ)) atTop (nhds 0)) :
    Irrational x := by
  intro ⟨r, hr⟩
  -- x = r is rational, write r = p / q
  set p := r.num with hp_def
  set q := r.den with hq_def
  have hq_pos : 0 < q := r.pos
  -- x = p / q
  have hx_eq : x = p / q := by rw [← hr, ← Rat.cast_def]
  -- P n * x - Q n = (P n * p - Q n * q) / q
  have hreform : ∀ n, (P n : ℝ) * x - (Q n : ℝ) = ((P n * p - Q n * q : ℤ) : ℝ) / q := by
    intro n
    rw [hx_eq]
    field_simp
    push_cast
    ring
  -- The integer P n * p - Q n * q is positive
  have hhint : ∀ n, 0 < P n * p - Q n * q := by
    intro n
    have h1 := hpos n
    rw [hreform] at h1
    have h2 : (0 : ℝ) < ((P n * p - Q n * q : ℤ) : ℝ) / q := h1
    have hq_pos_r : (0 : ℝ) < q := by exact_mod_cast hq_pos
    rw [lt_div_iff₀ hq_pos_r] at h2
    norm_cast at h2
    simpa using h2
  -- Since P n * p - Q n * q is a positive integer, it's ≥ 1
  have hlower : ∀ n, 1 ≤ (P n * p - Q n * q : ℤ) := fun n => by linarith [hhint n]
  -- Therefore (P n * p - Q n * q) / q ≥ 1/q
  have hge : ∀ n, (1 : ℝ) / q ≤ (P n : ℝ) * x - (Q n : ℝ) := by
    intro n
    rw [hreform]
    have h1 : (1 : ℤ) ≤ P n * p - Q n * q := hlower n
    have hq_pos_r : (0 : ℝ) < q := by exact_mod_cast hq_pos
    exact div_le_div_of_nonneg_right (by norm_cast : (1 : ℝ) ≤ (P n * p - Q n * q : ℤ)) (le_of_lt hq_pos_r)
  -- But hzero says (P n * x - Q n) → 0, contradiction since 1/q > 0
  have hq_pos_r : (0 : ℝ) < q := by exact_mod_cast hq_pos
  have hcontra : Tendsto (fun n => (P n : ℝ) * x - (Q n : ℝ)) atTop (nhds 0) := hzero
  have hbound : ∀ n, (1 : ℝ) / q ≤ (P n : ℝ) * x - (Q n : ℝ) := hge
  have hbound' : (fun _ : ℕ => (1 : ℝ) / q) ≤ᶠ[atTop] fun n => (P n : ℝ) * x - (Q n : ℝ) :=
    eventually_atTop.mpr ⟨0, fun n _ => hbound n⟩
  have hle0 : (1 : ℝ) / q ≤ 0 := le_of_tendsto_of_tendsto tendsto_const_nhds hcontra hbound'
  exact not_lt.mpr hle0 (by positivity)

/-- The final contradiction in the note.  The analytic work supplies
positivity and convergence to zero; the closed formula supplies the integer
`Q n = d_n³ b_n`. -/
theorem apery_irrationality_conclusion
    (x : ℝ)
    (hpos : ∀ n, 0 < (d n : ℝ) ^ 3 * ((a n : ℝ) * x - (b n : ℝ)))
    (hzero : Tendsto
      (fun n => (d n : ℝ) ^ 3 * ((a n : ℝ) * x - (b n : ℝ))) atTop (nhds 0)) :
    Irrational x := by
  choose Q hQ using denominator_bound
  apply irrational_of_positive_integer_linear_forms x
    (fun n => (d n : ℤ) ^ 3 * a n) Q
  · intro n
    have hQr : (Q n : ℝ) = (d n : ℝ) ^ 3 * (b n : ℝ) := by
      exact_mod_cast hQ n
    rw [hQr]
    push_cast
    nlinarith [hpos n]
  · convert hzero using 1
    funext n
    have hQr : (Q n : ℝ) = (d n : ℝ) ^ 3 * (b n : ℝ) := by
      exact_mod_cast hQ n
    rw [hQr]
    push_cast
    ring

end Apery
