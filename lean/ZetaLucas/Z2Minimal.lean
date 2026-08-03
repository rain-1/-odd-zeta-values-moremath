/-
# The minimal harmonic closed form for the Apéry ζ(2) companion

**Target** (`work/z2cf/note.tex`, Theorem 2; `papers_out/binomial_companions/main.tex` §…):
with `S(n,k) = C(n,k)² C(n+k,k)` and `(B_n)` the second solution of Apéry's ζ(2) recurrence,

    B_n = (1/5) Σ_{k=0}^n S(n,k) · [ H⁽²⁾_n + H_k (2H_k − H_{n−k} − H_n) ].

## Shift convention

Apéry's ζ(2) operator is

    (L u)_n = (n+1)² u_{n+1} − (11n²+11n+3) u_n − n² u_{n−1}     (n ≥ 1).

Throughout this file it is used **only** in the shifted form `Lz f m = (L f)_{m+1}`, i.e.

    Lz f m = (m+2)² f(m+2) − P(m+1) f(m+1) − (m+1)² f(m),        P(x) = 11x²+11x+3,

so that `m` ranges over all of `ℕ` and no natural subtraction ever occurs.  Likewise every
`n`-indexed object of the note is written at the base index `m`, with the five rows
`m, m+1, m+2, m+3, m+4` of the summand and the shell `Φ` built on `C(m+5,k)`.

## Why not a single telescope

The architecture of `MinimalForm.lean` (ζ(3)) and `FranelClosedForm.lean` — one antidifference
`Ψ = w·G + Z` for the operator itself — **provably does not exist here**.  Splitting the cell
identity along the letter monomials forces the coefficients of `H_k²`, `H_kH_{n−k}`, `H_kH_n`
and `H⁽²⁾_n` in `Ψ` to be `2χ, −χ, −χ, χ` for the unique `χ` with `Δ_k(Sχ) = L[S(·,k)]`; the
`H_{n−k}` and `H_n` components then both demand a rational solution of

    r(k)·φ(k+1) − φ(k) = ρ(n,k+1)/(k+1),      r(k) = S(n,k+1)/S(n,k),

and Gosper's algorithm certifies that no such rational `φ` exists.  This is the same
obstruction that forces the Ore-elimination route of `note.tex` §4.

## The architecture used instead

A **scalar order-two pre-operator** is applied before telescoping.  With

    Q(x)  = 625x⁴ + 7250x³ + 31245x² + 59264x + 41752,
    p₀(x) = (x+1)(x+2) Q(x),
    p₁(x) = 6875x⁶+100375x⁵+597195x⁴+1849309x³+3136850x²+2758284x+981880,
    p₂(x) = −(x+3)(x+4) Q(x−1),

the combination `p₀(m)·(L·)_{m+1} + p₁(m)·(L·)_{m+2} + p₂(m)·(L·)_{m+3}` applied cellwise to
`S(n,k)w(n,k)` **is** a `k`-difference `Ψ(m,k+1) − Ψ(m,k)` (`star_z2`), with

    Ψ(m,k) = W(m,k)·w(m,k) + S(m,k)·( β H_k + γ (H_{m−k} + H_m) + α ),
    W(m,k) = Σ_{i=0}^2 p_i(m) G(m+i+1,k),

`G` the ζ(2) Zeilberger certificate of `Z2Shell.lean` and `α, β, γ` explicit rational
functions of `(m,k)` with poles only at `k = m+1, …, m+4`.

Summing over `k` gives a **scalar order-two recurrence for the defect** `E_m = (L D)_{m+1}`,
where `D_n = Σ_k S(n,k)w(n,k)`:

    p₀(m) E_m + p₁(m) E_{m+1} + p₂(m) E_{m+2} = 0.

Since `E₀ = E₁ = 0` and the leading coefficient `p₂(m) = −(m+3)(m+4)Q(m−1)` never vanishes on
`m ≥ 0`, induction gives `E ≡ 0`, i.e. `L D = 0`; the two initial values `D₀ = 0`, `D₁ = 5`
then identify `D` with `5B`.  No Ore-algebra bookkeeping is needed: the pre-operator enters
only as three explicit rational coefficients.
-/
import ZetaLucas.Z2Shell

open Finset

namespace ZetaLucas

/-! ## 0. The weight, the row, and the shifted Apéry operator -/

/-- The minimal ζ(2) weight `w(n,k) = H⁽²⁾_n + H_k(2H_k − H_{n−k} − H_n)`
(truncated `ℕ`-subtraction in the argument of the third letter). -/
def wz (n k : ℕ) : ℚ :=
  Harm 2 n + Harm 1 k * (2 * Harm 1 k - Harm 1 (n - k) - Harm 1 n)

/-- The minimal-form row `D_n = Σ_{k=0}^n S(n,k) w(n,k)`; the theorem is `D_n = 5 B_n`. -/
def Dz (n : ℕ) : ℚ := ∑ k ∈ range (n + 1), (S2 n k : ℚ) * wz n k

theorem Dz_sum_range {n N : ℕ} (h : n + 1 ≤ N) :
    Dz n = ∑ k ∈ range N, (S2 n k : ℚ) * wz n k := by
  refine Finset.sum_subset
    (fun k hk => Finset.mem_range.2 (lt_of_lt_of_le (Finset.mem_range.1 hk) h)) ?_
  intro k _ hk
  simp only [Finset.mem_range, not_lt] at hk
  rw [S2_eq_zero_of_lt (by omega : n < k)]
  simp

/-- **The shift convention.**  `Lz f m = (L f)_{m+1}`, Apéry's ζ(2) operator applied at index
`m+1`, so that `m` ranges over all of `ℕ`. -/
def Lz (f : ℕ → ℚ) (m : ℕ) : ℚ :=
  ((m : ℚ) + 2) ^ 2 * f (m + 2) - Pz ((m : ℚ) + 1) * f (m + 1) - ((m : ℚ) + 1) ^ 2 * f m

/-! ## 1. The scalar order-two pre-operator -/

/-- `Q(x) = 625x⁴ + 7250x³ + 31245x² + 59264x + 41752`. -/
def Qz (x : ℚ) : ℚ := 625 * x ^ 4 + 7250 * x ^ 3 + 31245 * x ^ 2 + 59264 * x + 41752

/-- `p₀(x) = (x+1)(x+2)Q(x)`. -/
def pz0 (x : ℚ) : ℚ := (x + 1) * (x + 2) * Qz x

/-- `p₁(x) = 6875x⁶+100375x⁵+597195x⁴+1849309x³+3136850x²+2758284x+981880`. -/
def pz1 (x : ℚ) : ℚ :=
  6875 * x ^ 6 + 100375 * x ^ 5 + 597195 * x ^ 4 + 1849309 * x ^ 3
    + 3136850 * x ^ 2 + 2758284 * x + 981880

/-- `p₂(x) = −(x+3)(x+4)Q(x−1)`. -/
def pz2 (x : ℚ) : ℚ := -((x + 3) * (x + 4) * Qz (x - 1))

/-- `Q(m−1) = 625m⁴+4750m³+13245m²+16024m+7108`, manifestly positive for `m ≥ 0`. -/
theorem Qz_sub_one (m : ℕ) :
    Qz ((m : ℚ) - 1)
      = 625 * (m : ℚ) ^ 4 + 4750 * (m : ℚ) ^ 3 + 13245 * (m : ℚ) ^ 2
          + 16024 * (m : ℚ) + 7108 := by
  simp only [Qz]
  ring

/-- **Audit point: the leading coefficient never vanishes on the induction range.** -/
theorem pz2_ne_zero (m : ℕ) : pz2 (m : ℚ) ≠ 0 := by
  have hm : (0 : ℚ) ≤ (m : ℚ) := Nat.cast_nonneg m
  have hQ : 0 < Qz ((m : ℚ) - 1) := by
    rw [Qz_sub_one]
    positivity
  have : 0 < ((m : ℚ) + 3) * ((m : ℚ) + 4) * Qz ((m : ℚ) - 1) := by positivity
  simp only [pz2]
  linarith

/-- **The descent.**  A sequence killed by the scalar order-two operator `(p₀, p₁, p₂)` and
vanishing at `0` and `1` vanishes identically — this is where `pz2_ne_zero` is used. -/
theorem defect_vanishes (E : ℕ → ℚ) (h0 : E 0 = 0) (h1 : E 1 = 0)
    (hrec : ∀ m : ℕ, pz0 (m : ℚ) * E m + pz1 (m : ℚ) * E (m + 1)
      + pz2 (m : ℚ) * E (m + 2) = 0) :
    ∀ m : ℕ, E m = 0 := by
  have key : ∀ m : ℕ, E m = 0 ∧ E (m + 1) = 0 := by
    intro m
    induction m with
    | zero => exact ⟨h0, h1⟩
    | succ m ih =>
      refine ⟨ih.2, ?_⟩
      have h := hrec m
      rw [ih.1, ih.2] at h
      have : pz2 (m : ℚ) * E (m + 2) = 0 := by linarith
      rcases mul_eq_zero.1 this with hc | hc
      · exact absurd hc (pz2_ne_zero m)
      · exact hc
  exact fun m => (key m).1

/-! ## 2. Initial values -/

theorem Dz_zero : Dz 0 = 0 := by
  simp [Dz, wz, S2, Harm_zero]

theorem Dz_one : Dz 1 = 5 := by
  have h1 : Harm 1 1 = 1 := by
    rw [show (1 : ℕ) = 0 + 1 from rfl, Harm_succ, Harm_zero 1 (by norm_num)]
    norm_num
  have h2 : Harm 2 1 = 1 := by
    rw [show (1 : ℕ) = 0 + 1 from rfl, Harm_succ, Harm_zero 2 (by norm_num)]
    norm_num
  norm_num [Dz, wz, S2, Finset.sum_range_succ,
    Harm_zero 1 (by norm_num : 0 < 1), Harm_zero 2 (by norm_num : 0 < 2), h1, h2]

end ZetaLucas
