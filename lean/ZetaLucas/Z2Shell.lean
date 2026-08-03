/-
# The ζ(2) Apéry shell: `S(n,k) = C(n,k)² C(n+k,k)` and the row `a_n = Σ_k S(n,k)`

**Stage 1** of the formalization of `work/z2cf/note.tex` (`papers_out/binomial_companions`).

This file sets up, for the ζ(2) Apéry summand

    S(n,k) = C(n,k)² C(n+k,k),        a_n = Σ_{k=0}^n S(n,k)   (OEIS A005258),

the "Lemma 0" absorption shell of `MinimalForm.lean`, and proves that `a` is annihilated by
Apéry's ζ(2) operator

    (L u)_n = (n+1)² u_{n+1} − (11n²+11n+3) u_n − n² u_{n−1}                        (`apery2_rec`)

by the Zeilberger certificate of `work/z2cf/note.tex` §3 Step 1,

    G(n,k) = k³ ρ(n,k) C(n+1,k)² C(n+k−1,k) / (n (n+1)²),
    ρ(n,k) = k² + k(1+6n) − 4 − 15n − 11n².

Everything is written at `n = m+1` over the base term

    Φ(m,k) = C(m+2,k)² C(m+k,k) / ((m+1)²(m+2)²),

for which the certificate degenerates to the very clean

    G(m,k) = Φ(m,k) · (m+1) · k³ · ρ(m+1,k),

so that `propB_2` is a single polynomial identity in `ℚ[m,k]`, valid at **every** cell `k ≥ 0`
(no boundary hypothesis, no `0/0`).

The last section records the elementary consequence

    L (H⁽²⁾ · a)_n = a_{n+1} + a_{n−1}                                        (`harm2_apery2_rec`)

which is the first half of the Proposition of `note.tex` §4.
-/
import ZetaLucas.MinimalForm

open Finset

namespace ZetaLucas

/-! ## 0. The summand and the row -/

/-- The ζ(2) Apéry summand `S(n,k) = C(n,k)² C(n+k,k)`. -/
def S2 (n k : ℕ) : ℕ := (n.choose k) ^ 2 * ((n + k).choose k)

/-- The ζ(2) Apéry numbers `a_n = Σ_{k=0}^n C(n,k)² C(n+k,k)` (OEIS A005258). -/
def apery2 (n : ℕ) : ℚ := ∑ k ∈ range (n + 1), (S2 n k : ℚ)

theorem S2_eq_zero_of_lt {n k : ℕ} (h : n < k) : S2 n k = 0 := by
  simp [S2, Nat.choose_eq_zero_of_lt h]

theorem apery2_sum_range {n N : ℕ} (h : n + 1 ≤ N) :
    apery2 n = ∑ k ∈ range N, (S2 n k : ℚ) := by
  refine Finset.sum_subset
    (fun k hk => Finset.mem_range.2 (lt_of_lt_of_le (Finset.mem_range.1 hk) h)) ?_
  intro k _ hk
  simp only [Finset.mem_range, not_lt] at hk
  rw [S2_eq_zero_of_lt (by omega : n < k)]
  simp

theorem S2_cast (n k : ℕ) :
    (S2 n k : ℚ) = (n.choose k : ℚ) ^ 2 * ((n + k).choose k : ℚ) := by
  simp only [S2]
  push_cast
  ring

/-! ## 1. The shell `Φ` and Lemma 0 -/

/-- `Den2 m = (m+1)²(m+2)²`. -/
def Den2 (m : ℕ) : ℚ := ((m : ℚ) + 1) ^ 2 * ((m : ℚ) + 2) ^ 2

theorem Den2_ne (m : ℕ) : Den2 m ≠ 0 := by
  have h : (0 : ℚ) ≤ (m : ℚ) := Nat.cast_nonneg m
  simp only [Den2]
  positivity

/-- The ζ(2) base term `Φ(m,k) = C(m+2,k)² C(m+k,k) / ((m+1)²(m+2)²)`. -/
def Phi2 (m k : ℕ) : ℚ :=
  ((m + 2).choose k : ℚ) ^ 2 * ((m + k).choose k : ℚ) / Den2 m

theorem Phi2_eq_zero_of_lt {m k : ℕ} (h : m + 2 < k) : Phi2 m k = 0 := by
  simp [Phi2, Nat.choose_eq_zero_of_lt h]

/-- Square of `abs_a`: `C(m+2,k)²(m+2−k)² = (m+2)²C(m+1,k)²`. -/
theorem sq_a (m k : ℕ) :
    ((m + 2).choose k : ℚ) ^ 2 * ((m : ℚ) + 2 - k) ^ 2
      = ((m : ℚ) + 2) ^ 2 * ((m + 1).choose k : ℚ) ^ 2 := by
  rw [← mul_pow, ← mul_pow, abs_a]

/-- Square of `abs_b`: `C(m+1,k)²(m+1−k)² = (m+1)²C(m,k)²`. -/
theorem sq_b (m k : ℕ) :
    ((m + 1).choose k : ℚ) ^ 2 * ((m : ℚ) + 1 - k) ^ 2
      = ((m : ℚ) + 1) ^ 2 * (m.choose k : ℚ) ^ 2 := by
  rw [← mul_pow, ← mul_pow, abs_b]

/-- **Lemma 0(mid)**: `S(m+1,k) = Φ(m,k)·(m+2−k)²(m+k+1)(m+1)`. -/
theorem s2_mid (m k : ℕ) :
    (S2 (m + 1) k : ℚ)
      = Phi2 m k * (((m : ℚ) + 2 - k) ^ 2 * ((m : ℚ) + k + 1) * ((m : ℚ) + 1)) := by
  simp only [Phi2, Den2]
  rw [div_mul_eq_mul_div, eq_div_iff (by simpa [Den2] using Den2_ne m), S2_cast,
    show m + 1 + k = m + k + 1 by omega]
  linear_combination
    (-(((m + k + 1).choose k : ℚ) * ((m : ℚ) + 1) ^ 2)) * sq_a m k
    + (((m + 2).choose k : ℚ) ^ 2 * ((m : ℚ) + 2 - k) ^ 2 * ((m : ℚ) + 1)) * abs_c m k

/-- **Lemma 0(top)**: `S(m+2,k) = Φ(m,k)·(m+k+1)(m+k+2)(m+1)(m+2)`. -/
theorem s2_top (m k : ℕ) :
    (S2 (m + 2) k : ℚ)
      = Phi2 m k * (((m : ℚ) + k + 1) * ((m : ℚ) + k + 2) * ((m : ℚ) + 1) * ((m : ℚ) + 2)) := by
  simp only [Phi2, Den2]
  rw [div_mul_eq_mul_div, eq_div_iff (by simpa [Den2] using Den2_ne m), S2_cast,
    show m + 2 + k = m + k + 2 by omega]
  linear_combination
    (((m + 2).choose k : ℚ) ^ 2 * ((m : ℚ) + 1) ^ 2 * ((m : ℚ) + 2)) * abs_d m k
    + (((m + 2).choose k : ℚ) ^ 2 * ((m : ℚ) + 1) * ((m : ℚ) + 2) * ((m : ℚ) + k + 2))
        * abs_c m k

/-- **Lemma 0(low)**: `S(m,k) = Φ(m,k)·(m+2−k)²(m+1−k)²`. -/
theorem s2_low (m k : ℕ) :
    (S2 m k : ℚ) = Phi2 m k * (((m : ℚ) + 2 - k) ^ 2 * ((m : ℚ) + 1 - k) ^ 2) := by
  simp only [Phi2, Den2]
  rw [div_mul_eq_mul_div, eq_div_iff (by simpa [Den2] using Den2_ne m), S2_cast]
  linear_combination
    (-(((m + k).choose k : ℚ) * ((m : ℚ) + 1 - k) ^ 2)) * sq_a m k
    + (-(((m + k).choose k : ℚ) * ((m : ℚ) + 2) ^ 2)) * sq_b m k

/-- **Lemma 0(shift)**: `Φ(m,k+1)(k+1)³ = Φ(m,k)(m+2−k)²(m+k+1)`.  This is the identity that
removes every `0/0` from the certificate calculus. -/
theorem Phi2_succ (m k : ℕ) :
    Phi2 m (k + 1) * ((k : ℚ) + 1) ^ 3
      = Phi2 m k * (((m : ℚ) + 2 - k) ^ 2 * ((m : ℚ) + k + 1)) := by
  have g1 : ((m + 2).choose (k + 1) : ℚ) ^ 2 * ((k : ℚ) + 1) ^ 2
      = ((m + 2).choose k : ℚ) ^ 2 * ((m : ℚ) + 2 - k) ^ 2 := by
    have h := absorb2 (m + 2) k
    push_cast at h
    rw [← mul_pow, ← mul_pow, h]
  have g2 : ((m + k + 1).choose (k + 1) : ℚ) * ((k : ℚ) + 1)
      = ((m : ℚ) + k + 1) * ((m + k).choose k : ℚ) := by
    have h := absorb2 (m + k + 1) k
    push_cast at h
    rw [h]
    linear_combination abs_c m k
  simp only [Phi2]
  rw [show m + (k + 1) = m + k + 1 by omega, div_mul_eq_mul_div, div_mul_eq_mul_div]
  congr 1
  linear_combination
    (((m + k + 1).choose (k + 1) : ℚ) * ((k : ℚ) + 1)) * g1
    + (((m + 2).choose k : ℚ) ^ 2 * ((m : ℚ) + 2 - k) ^ 2) * g2

/-! ## 2. The Zeilberger certificate and the recurrence for `a` -/

/-- Apéry's ζ(2) polynomial `P(n) = 11n² + 11n + 3`. -/
def Pz (n : ℚ) : ℚ := 11 * n ^ 2 + 11 * n + 3

/-- The Zeilberger certificate polynomial `ρ(n,k) = k² + k(1+6n) − 4 − 15n − 11n²`
(`note.tex` §3). -/
def rhoz (x y : ℚ) : ℚ := y ^ 2 + y * (1 + 6 * x) - 4 - 15 * x - 11 * x ^ 2

/-- The certificate `G(m,k) = Φ(m,k)·(m+1)·k³·ρ(m+1,k)`. -/
def Gz (m k : ℕ) : ℚ := Phi2 m k * ((m : ℚ) + 1) * (k : ℚ) ^ 3 * rhoz ((m : ℚ) + 1) (k : ℚ)

theorem Gz_succ (m k : ℕ) :
    Gz m (k + 1)
      = Phi2 m k * (((m : ℚ) + 2 - k) ^ 2 * ((m : ℚ) + k + 1)) * ((m : ℚ) + 1)
          * rhoz ((m : ℚ) + 1) ((k : ℚ) + 1) := by
  simp only [Gz]
  push_cast
  linear_combination
    (((m : ℚ) + 1) * rhoz ((m : ℚ) + 1) ((k : ℚ) + 1)) * Phi2_succ m k

@[simp] theorem Gz_zero (m : ℕ) : Gz m 0 = 0 := by simp [Gz]

theorem Gz_top (m : ℕ) : Gz m (m + 3) = 0 := by
  simp [Gz, Phi2_eq_zero_of_lt (by omega : m + 2 < m + 3)]

/-- **CERT-1 for ζ(2)** (`note.tex` §3, Step 1): the Apéry ζ(2) operator applied to the summand
telescopes, `L[S(·,k)] = G(m,k+1) − G(m,k)`, at **every** cell `m, k ≥ 0`. -/
theorem propB_2 (m k : ℕ) :
    ((m : ℚ) + 2) ^ 2 * (S2 (m + 2) k : ℚ) - Pz ((m : ℚ) + 1) * (S2 (m + 1) k : ℚ)
        - ((m : ℚ) + 1) ^ 2 * (S2 m k : ℚ)
      = Gz m (k + 1) - Gz m k := by
  rw [s2_top, s2_mid, s2_low, Gz_succ]
  simp only [Gz, Pz, rhoz]
  ring

/-- **`a` is annihilated by the ζ(2) Apéry operator**:
`(n+1)² a_{n+1} = (11n²+11n+3) a_n + n² a_{n−1}` for every `n = m+1 ≥ 1`. -/
theorem apery2_rec (m : ℕ) :
    ((m : ℚ) + 2) ^ 2 * apery2 (m + 2) - Pz ((m : ℚ) + 1) * apery2 (m + 1)
      - ((m : ℚ) + 1) ^ 2 * apery2 m = 0 := by
  rw [apery2_sum_range (n := m + 2) (N := m + 3) (by omega),
    apery2_sum_range (n := m + 1) (N := m + 3) (by omega),
    apery2_sum_range (n := m) (N := m + 3) (by omega),
    Finset.mul_sum, Finset.mul_sum, Finset.mul_sum,
    ← Finset.sum_sub_distrib, ← Finset.sum_sub_distrib]
  rw [Finset.sum_congr rfl (fun k _ => propB_2 m k)]
  rw [Finset.sum_range_sub (fun k => Gz m k) (m + 3), Gz_top, Gz_zero]
  ring

/-! ## 3. The weight `H⁽²⁾_n` -/

/-- **First half of the Proposition of `note.tex` §4**:

    L (H⁽²⁾ · a)_n = a_{n+1} + a_{n−1}.

The shifts of `H⁽²⁾` produce exactly `1/(n+1)²` and `−1/n²` against the leading coefficients. -/
theorem harm2_apery2_rec (m : ℕ) :
    ((m : ℚ) + 2) ^ 2 * (Harm 2 (m + 2) * apery2 (m + 2))
        - Pz ((m : ℚ) + 1) * (Harm 2 (m + 1) * apery2 (m + 1))
        - ((m : ℚ) + 1) ^ 2 * (Harm 2 m * apery2 m)
      = apery2 (m + 2) + apery2 m := by
  have h1 : Harm 2 m = Harm 2 (m + 1) - 1 / ((m : ℚ) + 1) ^ 2 := by
    rw [Harm_succ 2 m]; ring
  have h2 : Harm 2 (m + 2) = Harm 2 (m + 1) + 1 / ((m : ℚ) + 2) ^ 2 := by
    have h := Harm_succ 2 (m + 1)
    rw [show m + 1 + 1 = m + 2 by omega] at h
    push_cast at h
    rw [h, show ((m : ℚ) + 1 + 1) = (m : ℚ) + 2 by ring]
  have e1 : ((m : ℚ) + 1) ^ 2 * (1 / ((m : ℚ) + 1) ^ 2) = 1 := by
    field_simp
  have e2 : ((m : ℚ) + 2) ^ 2 * (1 / ((m : ℚ) + 2) ^ 2) = 1 := by
    field_simp
  have hrec := apery2_rec m
  rw [h1, h2]
  linear_combination Harm 2 (m + 1) * hrec + apery2 (m + 2) * e2 + apery2 m * e1

section Sanity

-- `a_n = 1, 3, 19, 147, 1251, 11253, …`  (A005258)
#eval (List.range 6).map apery2

end Sanity

end ZetaLucas
