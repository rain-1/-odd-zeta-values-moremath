/-
# The Brown–Zudilin "factor 12" — an arithmetic refutation of the printed integrality claim

**What is assumed, and what is proved.**  Brown and Zudilin (*A cellular integral for ζ(5)*-type
construction, arXiv:2210.03391) print the value

        P₂ = 1190161 / 384                                              (their equation, quoted)

for the second term of their rational sequence `P_n`, and they claim that
`d_n⁵ · P_n ∈ ℤ` for all `n`, where `d_n = lcm(1, 2, …, n)`.

**This file takes their printed value `P₂ = 1190161/384` as a *hypothesis* (a quoted numeral) and
derives a purely arithmetic consequence of it.**  Nothing about cellular integrals, periods, or the
construction that produced the number is formalized, verified, or even mentioned below: the input is
a rational literal, the output is a statement about that literal.  If the printed value is a typo,
these theorems say nothing about the corrected value.

The consequence is that the claim `d_n⁵ P_n ∈ ℤ` **fails at `n = 2`**, and fails by exactly a factor
of `12 = 2²·3`:

* `d₂ = lcm(1,2) = 2`, so `d₂⁵ = 32`;
* `32 · (1190161/384) = 1190161/12 ∉ ℤ`                     (`BZ_P2_not_integral`);
* `12 · 32 · (1190161/384) = 1190161 ∈ ℤ`                   (`BZ_P2_factor_twelve`);
* and `12` is *minimal*: any natural `c` with `c · d₂⁵ · P₂ ∈ ℤ` is divisible by `12`
                                                            (`BZ_twelve_minimal`).

`d₂⁵` is computed from `Nat.lcm`, not hard-coded.
-/
import Mathlib.Data.Rat.Defs
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic

namespace ZetaLucas

/-- `d_n = lcm(1, 2, …, n)`, the usual van der Poorten denominator. -/
def dlcm : ℕ → ℕ
  | 0 => 1
  | (n + 1) => Nat.lcm (n + 1) (dlcm n)

/-- `d₁ = 1`, `d₂ = lcm(1,2) = 2`, `d₃ = 6`, `d₄ = 12` — computed, not assumed. -/
theorem dlcm_one : dlcm 1 = 1 := by decide
theorem dlcm_two : dlcm 2 = 2 := by decide
theorem dlcm_three : dlcm 3 = 6 := by decide
theorem dlcm_four : dlcm 4 = 12 := by decide

/-- `d₂⁵ = 32`, from `Nat.lcm`. -/
theorem dlcm_two_pow_five : dlcm 2 ^ 5 = 32 := by decide

/-- **Brown–Zudilin's own printed value of `P₂`**, quoted verbatim as a rational literal.
This is a *hypothesis of the file*, not a computed or verified quantity. -/
def BZ_P2 : ℚ := 1190161 / 384

/-- `d₂⁵ · P₂ = 1190161/12`, using their printed `P₂`. -/
theorem BZ_d2_pow_five_mul_P2 : ((dlcm 2 ^ 5 : ℕ) : ℚ) * BZ_P2 = 1190161 / 12 := by
  rw [dlcm_two_pow_five, BZ_P2]
  norm_num

/-- **The refutation.**  With Brown–Zudilin's printed `P₂ = 1190161/384`, the quantity
`d₂⁵ · P₂` is *not* an integer — so the claim `d_n⁵ P_n ∈ ℤ` is false at `n = 2`. -/
theorem BZ_P2_not_integral : ¬ ∃ z : ℤ, ((dlcm 2 ^ 5 : ℕ) : ℚ) * BZ_P2 = (z : ℚ) := by
  rintro ⟨z, hz⟩
  rw [BZ_d2_pow_five_mul_P2] at hz
  have h : (1190161 : ℚ) = 12 * (z : ℚ) := by
    field_simp at hz
    linarith
  have h' : (1190161 : ℤ) = 12 * z := by exact_mod_cast h
  omega

/-- **The missing factor is exactly `12 = 2²·3`.**  Multiplying by `12` repairs integrality. -/
theorem BZ_P2_factor_twelve : (12 : ℚ) * (((dlcm 2 ^ 5 : ℕ) : ℚ) * BZ_P2) = 1190161 := by
  rw [BZ_d2_pow_five_mul_P2]
  norm_num

/-- **`12` is minimal**: any natural number `c` for which `c · d₂⁵ · P₂` is an integer is a
multiple of `12`.  (So the defect is exactly `2²·3`, not merely "at least some factor".) -/
theorem BZ_twelve_minimal (c : ℕ)
    (h : ∃ z : ℤ, (c : ℚ) * (((dlcm 2 ^ 5 : ℕ) : ℚ) * BZ_P2) = (z : ℚ)) : 12 ∣ c := by
  obtain ⟨z, hz⟩ := h
  rw [BZ_d2_pow_five_mul_P2] at hz
  have h1 : (c : ℚ) * 1190161 = 12 * (z : ℚ) := by
    field_simp at hz
    linarith
  have h2 : (c : ℤ) * 1190161 = 12 * z := by exact_mod_cast h1
  have h3 : (12 : ℤ) ∣ (c : ℤ) := ⟨z - (c : ℤ) * 99180, by linarith⟩
  exact_mod_cast h3

end ZetaLucas
