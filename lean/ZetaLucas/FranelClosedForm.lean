/-
# Harmonic closed forms for the Franel and s₁₀ second solutions

**Targets** (`work/MINIMAL_FORM_PROOF.md` §8.0–8.4; certificates from
`work/minform/certs_stretch.m`, re-verified cellwise in exact arithmetic this session).

* **Franel** (`d = 3`): with `A(n) = Σ_k C(n,k)³` (A000172) and the recurrence
  `(n+1)² u_{n+1} = (7n²+7n+2) u_n + 8n² u_{n−1}`, the second solution (`B₀ = 0, B₁ = 1`) is

      B(n) = Σ_{k=0}^n C(n,k)³ · ( (1/8)(H⁽²⁾_k + H⁽²⁾_{n−k}) + (3/8)(H_k − H_{n−k})² )

  (`franel_closed_form`, `franel_harmonic_closed_form`).

* **s₁₀** (`d = 4`): with `A(n) = Σ_k C(n,k)⁴` and
  `(n+1)³ u_{n+1} = (2n+1)(6n²+6n+2) u_n + n(64n²−4) u_{n−1}`, the second solution is

      B(n) = Σ_{k=0}^n C(n,k)⁴ · ( (1/10)(H⁽²⁾_k + H⁽²⁾_{n−k}) + (2/5)(H_k − H_{n−k})² )

  (`s10_closed_form`, `s10_harmonic_closed_form`).

**Method** — the `MinimalForm.lean` architecture adapted to the symmetric weights: everything
is written at `n = m+1` over the base term `Φ = C(m+2,k)^d / ((m+1)^d(m+2)^d)`; Lemma-0 style
absorption identities (valid for all `k`, no boundary hypotheses) turn each certificate into a
polynomial identity in `ℚ[m,k]`.  The single antidifference is

    Ψ(m,k) = w(m+1,k)·G(m,k) + Z(m,k),
    G = Φ·k^d·(shifted ρ),   Z = C(m+1,k)^d·( N/(m+2−k)^{d+1}·δ + M/(m+2−k)^{d+2} ),

with `δ(n,k) = H_k − H_{n−k}` and `ρ, N, M` the explicit certificates.  The telescoping
identity `star`: the `k`-summand of `(L B)(m+1)` equals `Ψ(m,k+1) − Ψ(m,k)`, holds at **every**
cell `k ≥ 0` (Lean's total division and truncated `ℕ`-subtraction make the boundary cells
`k = m+1, m+2` literally true — verified cellwise in exact arithmetic, `m ≤ 11`, before this
file was written).  The proof splits `k ≤ m` (generic: absorptions + `field_simp` + `ring`)
from the three boundary regimes.  `Finset.sum_range_sub` collapses the sum; the two initial
values close the induction.

The only analytic input is `Harm_succ` (from `MinimalForm.lean`).
-/
import ZetaLucas.MinimalForm

open Finset

namespace ZetaLucas

/-! ## 0. Common: cubes/quartics of the absorption identities, weights -/

/-- `C(n,k)³` as a rational. -/
def c3 (n k : ℕ) : ℚ := ((n.choose k : ℚ)) ^ 3

/-- `C(n,k)⁴` as a rational. -/
def c4 (n k : ℕ) : ℚ := ((n.choose k : ℚ)) ^ 4

theorem c3_eq_zero_of_lt {n k : ℕ} (h : n < k) : c3 n k = 0 := by
  simp [c3, Nat.choose_eq_zero_of_lt h]

theorem c4_eq_zero_of_lt {n k : ℕ} (h : n < k) : c4 n k = 0 := by
  simp [c4, Nat.choose_eq_zero_of_lt h]

/-- Cube of `abs_a`: `C(m+2,k)³(m+2−k)³ = (m+2)³C(m+1,k)³`. -/
theorem cube_a (m k : ℕ) :
    ((m + 2).choose k : ℚ) ^ 3 * ((m : ℚ) + 2 - k) ^ 3
      = ((m : ℚ) + 2) ^ 3 * ((m + 1).choose k : ℚ) ^ 3 := by
  rw [← mul_pow, ← mul_pow, abs_a]

/-- Cube of `abs_b`: `C(m+1,k)³(m+1−k)³ = (m+1)³C(m,k)³`. -/
theorem cube_b (m k : ℕ) :
    ((m + 1).choose k : ℚ) ^ 3 * ((m : ℚ) + 1 - k) ^ 3
      = ((m : ℚ) + 1) ^ 3 * (m.choose k : ℚ) ^ 3 := by
  rw [← mul_pow, ← mul_pow, abs_b]

/-- Cube of `absorb2` at `N = m+2`: `C(m+2,k+1)³(k+1)³ = C(m+2,k)³(m+2−k)³`. -/
theorem cube_c (m k : ℕ) :
    ((m + 2).choose (k + 1) : ℚ) ^ 3 * ((k : ℚ) + 1) ^ 3
      = ((m + 2).choose k : ℚ) ^ 3 * ((m : ℚ) + 2 - k) ^ 3 := by
  have h := absorb2 (m + 2) k
  push_cast at h
  rw [← mul_pow, ← mul_pow, h]

/-- Cube of `absorb2` at `N = m+1`: `C(m+1,k+1)³(k+1)³ = C(m+1,k)³(m+1−k)³`. -/
theorem cube_d (m k : ℕ) :
    ((m + 1).choose (k + 1) : ℚ) ^ 3 * ((k : ℚ) + 1) ^ 3
      = ((m + 1).choose k : ℚ) ^ 3 * ((m : ℚ) + 1 - k) ^ 3 := by
  have h := absorb2 (m + 1) k
  push_cast at h
  rw [← mul_pow, ← mul_pow, h]

/-- Quartic versions, for s₁₀. -/
theorem quart_a (m k : ℕ) :
    ((m + 2).choose k : ℚ) ^ 4 * ((m : ℚ) + 2 - k) ^ 4
      = ((m : ℚ) + 2) ^ 4 * ((m + 1).choose k : ℚ) ^ 4 := by
  rw [← mul_pow, ← mul_pow, abs_a]

theorem quart_b (m k : ℕ) :
    ((m + 1).choose k : ℚ) ^ 4 * ((m : ℚ) + 1 - k) ^ 4
      = ((m : ℚ) + 1) ^ 4 * (m.choose k : ℚ) ^ 4 := by
  rw [← mul_pow, ← mul_pow, abs_b]

theorem quart_c (m k : ℕ) :
    ((m + 2).choose (k + 1) : ℚ) ^ 4 * ((k : ℚ) + 1) ^ 4
      = ((m + 2).choose k : ℚ) ^ 4 * ((m : ℚ) + 2 - k) ^ 4 := by
  have h := absorb2 (m + 2) k
  push_cast at h
  rw [← mul_pow, ← mul_pow, h]

theorem quart_d (m k : ℕ) :
    ((m + 1).choose (k + 1) : ℚ) ^ 4 * ((k : ℚ) + 1) ^ 4
      = ((m + 1).choose k : ℚ) ^ 4 * ((m : ℚ) + 1 - k) ^ 4 := by
  have h := absorb2 (m + 1) k
  push_cast at h
  rw [← mul_pow, ← mul_pow, h]

/-- `H⁽ʳ⁾_1 = 1`. -/
theorem Harm_one (r : ℕ) (hr : 0 < r) : Harm r 1 = 1 := by
  rw [show (1 : ℕ) = 0 + 1 from rfl, Harm_succ, Harm_zero r hr]
  norm_num

/-! ## 1. Franel: definitions -/

/-- The symmetric Franel weight `(1/8)(H⁽²⁾_k + H⁽²⁾_{n−k}) + (3/8)(H_k − H_{n−k})²`
(truncated `ℕ`-subtraction in the argument). -/
def wF (n k : ℕ) : ℚ :=
  (1 / 8) * (Harm 2 k + Harm 2 (n - k)) + (3 / 8) * (Harm 1 k - Harm 1 (n - k)) ^ 2

/-- The asymmetric Franel weight used by `Instances.bFranel`.  Its reflection average is `wF`. -/
def wFOld (n k : ℕ) : ℚ :=
  (1 / 4) * Harm 2 k + (3 / 4) * Harm 1 k * (Harm 1 k - Harm 1 (n - k))

/-- The compact symmetric weight is the average of the old weight and its reflection. -/
theorem wF_eq_reflection_average {n k : ℕ} (hk : k ≤ n) :
    wF n k = (1 / 2) * (wFOld n k + wFOld n (n - k)) := by
  simp only [wF, wFOld, Nat.sub_sub_self hk]
  ring

/-- The antisymmetric letter `δ(n,k) = H_k − H_{n−k}`. -/
def dlt (n k : ℕ) : ℚ := Harm 1 k - Harm 1 (n - k)

/-- The symmetric-weight Franel second solution. -/
def bFranelSym (n : ℕ) : ℚ := ∑ k ∈ range (n + 1), c3 n k * wF n k

/-- `DenF m = (m+1)³(m+2)³`. -/
def DenF (m : ℕ) : ℚ := ((m : ℚ) + 1) ^ 3 * ((m : ℚ) + 2) ^ 3

theorem DenF_ne (m : ℕ) : DenF m ≠ 0 := by
  have h : (0 : ℚ) ≤ (m : ℚ) := Nat.cast_nonneg m
  simp only [DenF]
  positivity

/-- The Franel base term `Φ_F(m,k) = C(m+2,k)³/((m+1)³(m+2)³)`. -/
def PhiF (m k : ℕ) : ℚ := ((m + 2).choose k : ℚ) ^ 3 / DenF m

/-- The Franel Zeilberger certificate numerator (`rho_F·n` of `certs_stretch.m`). -/
def rhoF (x y : ℚ) : ℚ :=
  -4 + 12 * y - 12 * y ^ 2 + 4 * y ^ 3 - 22 * x + 39 * y * x - 18 * y ^ 2 * x
    - 32 * x ^ 2 + 27 * y * x ^ 2 - 14 * x ^ 3

/-- `G_F(m,k) = Φ_F·k³·(m+1)²·rhoF(m+1,k)`  (equals `k³ ρ_F C(n+1,k)³/(n+1)³` at `n = m+1`). -/
def GF (m k : ℕ) : ℚ := PhiF m k * (k : ℚ) ^ 3 * ((m : ℚ) + 1) ^ 2 * rhoF ((m : ℚ) + 1) (k : ℚ)

/-- The Gosper certificate `N_F` (with its `1/(4n)` prefactor). -/
def NF (x y : ℚ) : ℚ :=
  3 * y ^ 2 * (4 - 16 * y + 24 * y ^ 2 - 16 * y ^ 3 + 4 * y ^ 4 + 26 * x - 68 * y * x
    + 63 * y ^ 2 * x - 20 * y ^ 3 * x + 54 * x ^ 2 - 88 * y * x ^ 2 + 39 * y ^ 2 * x ^ 2
    + 46 * x ^ 3 - 36 * y * x ^ 3 + 14 * x ^ 4) / (4 * x)

/-- The Gosper certificate `M_F` (with its `−1/(2n)` prefactor). -/
def MF (x y : ℚ) : ℚ :=
  -(y * (2 - 10 * y + 20 * y ^ 2 - 20 * y ^ 3 + 10 * y ^ 4 - 2 * y ^ 5 + 15 * x - 50 * y * x
    + 70 * y ^ 2 * x - 45 * y ^ 3 * x + 11 * y ^ 4 * x + 40 * x ^ 2 - 90 * y * x ^ 2
    + 80 * y ^ 2 * x ^ 2 - 25 * y ^ 3 * x ^ 2 + 50 * x ^ 3 - 70 * y * x ^ 3
    + 30 * y ^ 2 * x ^ 3 + 30 * x ^ 4 - 20 * y * x ^ 4 + 7 * x ^ 5)) / (2 * x)

/-- The Gosper part `Z_F(m,k) = C(m+1,k)³( N_F/(m+2−k)⁴·δ(m+1,k) + M_F/(m+2−k)⁵ )`. -/
def ZF (m k : ℕ) : ℚ :=
  c3 (m + 1) k * (NF ((m : ℚ) + 1) (k : ℚ) / ((m : ℚ) + 2 - k) ^ 4 * dlt (m + 1) k
    + MF ((m : ℚ) + 1) (k : ℚ) / ((m : ℚ) + 2 - k) ^ 5)

/-- The single Franel antidifference `Ψ_F = w(m+1,·)·G_F + Z_F`. -/
def PsiF (m k : ℕ) : ℚ := wF (m + 1) k * GF m k + ZF m k

/-! ## 2. Franel: Lemma 0 (shell conversions) -/

theorem l3top (m k : ℕ) :
    c3 (m + 2) k = PhiF m k * (((m : ℚ) + 1) ^ 3 * ((m : ℚ) + 2) ^ 3) := by
  simp only [c3, PhiF, DenF]
  rw [div_mul_eq_mul_div, mul_div_assoc]
  rw [div_self (by have h : (0 : ℚ) ≤ (m : ℚ) := Nat.cast_nonneg m; positivity), mul_one]

theorem l3mid (m k : ℕ) :
    c3 (m + 1) k = PhiF m k * (((m : ℚ) + 1) ^ 3 * ((m : ℚ) + 2 - k) ^ 3) := by
  simp only [c3, PhiF, DenF]
  rw [div_mul_eq_mul_div, eq_div_iff (by simpa [DenF] using DenF_ne m)]
  linear_combination (-((m : ℚ) + 1) ^ 3) * cube_a m k

theorem l3low (m k : ℕ) :
    c3 m k = PhiF m k * (((m : ℚ) + 2 - k) ^ 3 * ((m : ℚ) + 1 - k) ^ 3) := by
  simp only [c3, PhiF, DenF]
  rw [div_mul_eq_mul_div, eq_div_iff (by simpa [DenF] using DenF_ne m)]
  linear_combination (-((m : ℚ) + 1 - k) ^ 3) * cube_a m k
    + (-((m : ℚ) + 2) ^ 3) * cube_b m k

theorem PhiF_succ (m k : ℕ) :
    PhiF m (k + 1) * ((k : ℚ) + 1) ^ 3 = PhiF m k * ((m : ℚ) + 2 - k) ^ 3 := by
  simp only [PhiF]
  rw [div_mul_eq_mul_div, div_mul_eq_mul_div, cube_c]

theorem GF_succ (m k : ℕ) :
    GF m (k + 1)
      = PhiF m k * ((m : ℚ) + 2 - k) ^ 3 * ((m : ℚ) + 1) ^ 2
          * rhoF ((m : ℚ) + 1) ((k : ℚ) + 1) := by
  simp only [GF]
  push_cast
  linear_combination ((m : ℚ) + 1) ^ 2 * rhoF ((m : ℚ) + 1) ((k : ℚ) + 1) * PhiF_succ m k

/-- `C(m+1,k+1)³` in the `Φ_F(m,k)` shell (division by `(k+1)³` is exact). -/
theorem l3mid_succ (m k : ℕ) :
    c3 (m + 1) (k + 1)
      = PhiF m k * (((m : ℚ) + 1) ^ 3 * ((m : ℚ) + 2 - k) ^ 3 * ((m : ℚ) + 1 - k) ^ 3)
          / ((k : ℚ) + 1) ^ 3 := by
  have hk : ((k : ℚ) + 1) ^ 3 ≠ 0 := by positivity
  rw [eq_div_iff hk]
  have h := cube_d m k
  simp only [c3]
  rw [h, ← c3, l3mid]
  ring

/-! ## 3. Franel: the Zeilberger certificate (CERT-1, all `k`) -/

/-- **CERT-1 for Franel**: `L[C(·,k)³] = G_F(m,k+1) − G_F(m,k)` for **all** `m, k ≥ 0`. -/
theorem propB_F (m k : ℕ) :
    ((m : ℚ) + 2) ^ 2 * c3 (m + 2) k
        - (7 * ((m : ℚ) + 1) ^ 2 + 7 * ((m : ℚ) + 1) + 2) * c3 (m + 1) k
        - 8 * ((m : ℚ) + 1) ^ 2 * c3 m k
      = GF m (k + 1) - GF m k := by
  rw [l3top, l3mid, l3low, GF_succ]
  simp only [GF, rhoF]
  ring

/-! ## 4. Franel: the Gosper certificate (CERT-2, `k ≤ m`) -/

set_option maxRecDepth 8000 in
set_option maxHeartbeats 1600000 in
/-- **CERT-2 for Franel** (the two folded Gosper problems): for `k ≤ m`,

    c₊·C(m+2,k)³(w(m+2,k)−w(m+1,k)) − c₋·C(m,k)³(w(m,k)−w(m+1,k))
      − (w(m+1,k+1)−w(m+1,k))·G_F(m,k+1)  =  Z_F(m,k+1) − Z_F(m,k).  -/
theorem propC_F (m k : ℕ) (hk : k ≤ m) :
    ((m : ℚ) + 2) ^ 2 * c3 (m + 2) k * (wF (m + 2) k - wF (m + 1) k)
        - 8 * ((m : ℚ) + 1) ^ 2 * c3 m k * (wF m k - wF (m + 1) k)
        - (wF (m + 1) (k + 1) - wF (m + 1) k) * GF m (k + 1)
      = ZF m (k + 1) - ZF m k := by
  obtain ⟨j, rfl⟩ := Nat.exists_eq_add_of_le hk
  rw [GF_succ]
  simp only [ZF, wF, dlt]
  rw [l3mid_succ, l3top, l3mid, l3low]
  simp only [show k + j + 2 - k = j + 1 + 1 from by omega,
    show k + j + 1 - k = j + 1 from by omega, show k + j - k = j from by omega,
    show k + j + 1 - (k + 1) = j from by omega]
  simp only [Harm_succ 2 (j + 1), Harm_succ 1 (j + 1),
    Harm_succ 2 j, Harm_succ 1 j, Harm_succ 2 k, Harm_succ 1 k]
  have h1 : ((j : ℚ) + 1) ≠ 0 := by positivity
  have h2 : ((j : ℚ) + 1 + 1) ≠ 0 := by positivity
  have h3 : ((k : ℚ) + 1) ≠ 0 := by positivity
  have h4 : ((k : ℚ) + (j : ℚ) + 1) ≠ 0 := by positivity
  have h5 : ((k : ℚ) + (j : ℚ) + 2) ≠ 0 := by positivity
  simp only [rhoF, NF, MF]
  push_cast
  simp only [show ((k : ℚ) + (j : ℚ) + 2 - (k : ℚ)) = (j : ℚ) + 2 from by ring,
    show ((k : ℚ) + (j : ℚ) + 2 - ((k : ℚ) + 1)) = (j : ℚ) + 1 from by ring]
  have h6 : ((j : ℚ) + 2) ≠ 0 := by positivity
  field_simp
  ring

/-! ## 5. Franel: the telescoping identity at every cell -/

theorem PsiF_zero (m : ℕ) : PsiF m 0 = 0 := by
  simp [PsiF, GF, ZF, NF, MF, c3, dlt]

theorem PhiF_eq_zero_of_lt {m k : ℕ} (h : m + 2 < k) : PhiF m k = 0 := by
  simp [PhiF, Nat.choose_eq_zero_of_lt h]

theorem PsiF_top (m : ℕ) : PsiF m (m + 3) = 0 := by
  have h1 : PhiF m (m + 3) = 0 := PhiF_eq_zero_of_lt (by omega)
  have h2 : c3 (m + 1) (m + 3) = 0 := c3_eq_zero_of_lt (by omega)
  simp [PsiF, GF, ZF, h1, h2]

/-- **The telescoping identity (`star`) for Franel**: for every `m, k ≥ 0`, the `k`-summand of
`(L B)(m+1)` equals `Ψ_F(m,k+1) − Ψ_F(m,k)`.  The three boundary regimes `k = m+1`, `k = m+2`,
`k ≥ m+3` are honest case analyses (truncated subtraction and vanishing binomials make them
true — pre-verified cellwise in exact arithmetic). -/
theorem star_F (m k : ℕ) :
    ((m : ℚ) + 2) ^ 2 * (c3 (m + 2) k * wF (m + 2) k)
        - (7 * ((m : ℚ) + 1) ^ 2 + 7 * ((m : ℚ) + 1) + 2) * (c3 (m + 1) k * wF (m + 1) k)
        - 8 * ((m : ℚ) + 1) ^ 2 * (c3 m k * wF m k)
      = PsiF m (k + 1) - PsiF m k := by
  rcases Nat.lt_or_ge k (m + 1) with hk | hk
  · -- main regime k ≤ m
    have hB := propB_F m k
    have hC := propC_F m k (by omega)
    simp only [PsiF]
    linear_combination wF (m + 1) k * hB + hC
  rcases Nat.eq_or_lt_of_le hk with hk1 | hk1
  · -- k = m+1
    subst hk1
    have e2 : (m + 2).choose (m + 1) = m + 2 := by
      rw [show m + 2 = m + 1 + 1 from rfl, Nat.choose_succ_self_right]
    have e3 : (m + 1).choose (m + 1) = 1 := Nat.choose_self (m + 1)
    have e4 : m.choose (m + 1) = 0 := Nat.choose_eq_zero_of_lt (by omega)
    have e5 : (m + 1).choose (m + 2) = 0 := Nat.choose_eq_zero_of_lt (by omega)
    have e6 : (m + 2).choose (m + 2) = 1 := Nat.choose_self (m + 2)
    have hH2 : Harm 2 (m + 2) = Harm 2 (m + 1) + 1 / ((m : ℚ) + 2) ^ 2 := by
      have h := Harm_succ 2 (m + 1); push_cast at h
      rw [show m + 1 + 1 = m + 2 from rfl] at h
      rw [h]; ring_nf
    have hH1 : Harm 1 (m + 2) = Harm 1 (m + 1) + 1 / ((m : ℚ) + 2) := by
      have h := Harm_succ 1 (m + 1); push_cast at h
      rw [show m + 1 + 1 = m + 2 from rfl] at h
      rw [h]; ring_nf
    have h1 : ((m : ℚ) + 1) ≠ 0 := by positivity
    have h2 : ((m : ℚ) + 2) ≠ 0 := by positivity
    simp only [PsiF, GF, ZF, wF, dlt, PhiF, DenF, c3, e2, e3, e4, e5, e6,
      show m + 2 - (m + 1) = 1 from by omega,
      show m + 1 - (m + 2) = 0 from by omega, show m + 1 - (m + 1) = 0 from by omega]
    rw [hH2, hH1, Harm_one 1 (by norm_num), Harm_one 2 (by norm_num),
      Harm_zero 1 (by norm_num), Harm_zero 2 (by norm_num)]
    simp only [rhoF, NF, MF]
    push_cast
    field_simp
    ring
  · -- k ≥ m+2
    rcases Nat.eq_or_lt_of_le hk1 with hk2 | hk2
    · -- k = m+2
      subst hk2
      have e1 : (m + 1).choose (m + 2) = 0 := Nat.choose_eq_zero_of_lt (by omega)
      have e2 : m.choose (m + 2) = 0 := Nat.choose_eq_zero_of_lt (by omega)
      have e3 : (m + 2).choose (m + 2) = 1 := Nat.choose_self (m + 2)
      have e4 : (m + 2).choose (m + 3) = 0 := Nat.choose_eq_zero_of_lt (by omega)
      have e5 : (m + 1).choose (m + 3) = 0 := Nat.choose_eq_zero_of_lt (by omega)
      simp only [PsiF, GF, ZF, wF, dlt, PhiF, DenF, c3, e1, e2, e3, e4, e5,
        Nat.sub_self, show m + 1 - (m + 2) = 0 from by omega,
        show m + 1 - (m + 3) = 0 from by omega]
      have h1 : ((m : ℚ) + 1) ≠ 0 := by positivity
      have h2 : ((m : ℚ) + 2) ≠ 0 := by positivity
      simp only [rhoF]
      push_cast
      field_simp
      ring
    · -- k ≥ m+3: every term vanishes
      have e1 : (m + 2).choose k = 0 := Nat.choose_eq_zero_of_lt (by omega)
      have e2 : (m + 1).choose k = 0 := Nat.choose_eq_zero_of_lt (by omega)
      have e3 : m.choose k = 0 := Nat.choose_eq_zero_of_lt (by omega)
      have e4 : (m + 2).choose (k + 1) = 0 := Nat.choose_eq_zero_of_lt (by omega)
      have e5 : (m + 1).choose (k + 1) = 0 := Nat.choose_eq_zero_of_lt (by omega)
      simp [PsiF, GF, ZF, PhiF, c3, e1, e2, e3, e4, e5]

/-! ## 6. Franel: recurrence, companion, closed form -/

theorem bFranelSym_sum_range {n N : ℕ} (h : n + 1 ≤ N) :
    bFranelSym n = ∑ k ∈ range N, c3 n k * wF n k := by
  refine Finset.sum_subset
    (fun k hk => Finset.mem_range.2 (lt_of_lt_of_le (Finset.mem_range.1 hk) h)) ?_
  intro k _ hk
  simp only [Finset.mem_range, not_lt] at hk
  rw [c3_eq_zero_of_lt (by omega : n < k)]
  simp

/-- The symmetric Franel sum is annihilated by the Franel operator. -/
theorem bFranelSym_rec (m : ℕ) :
    ((m : ℚ) + 2) ^ 2 * bFranelSym (m + 2)
        - (7 * ((m : ℚ) + 1) ^ 2 + 7 * ((m : ℚ) + 1) + 2) * bFranelSym (m + 1)
        - 8 * ((m : ℚ) + 1) ^ 2 * bFranelSym m = 0 := by
  rw [bFranelSym_sum_range (n := m + 2) (N := m + 3) (by omega),
    bFranelSym_sum_range (n := m + 1) (N := m + 3) (by omega),
    bFranelSym_sum_range (n := m) (N := m + 3) (by omega),
    Finset.mul_sum, Finset.mul_sum, Finset.mul_sum,
    ← Finset.sum_sub_distrib, ← Finset.sum_sub_distrib]
  rw [Finset.sum_congr rfl (fun k _ => star_F m k)]
  rw [Finset.sum_range_sub (fun k => PsiF m k) (m + 3), PsiF_top, PsiF_zero]
  ring

/-- **The Franel second solution**, defined by the recurrence
`(n+1)² B_{n+1} = (7n²+7n+2) B_n + 8n² B_{n−1}`, `B₀ = 0`, `B₁ = 1`. -/
def franelB : ℕ → ℚ
  | 0 => 0
  | 1 => 1
  | (n + 2) => ((7 * ((n : ℚ) + 1) ^ 2 + 7 * ((n : ℚ) + 1) + 2) * franelB (n + 1)
      + 8 * ((n : ℚ) + 1) ^ 2 * franelB n) / ((n : ℚ) + 2) ^ 2

@[simp] theorem franelB_zero : franelB 0 = 0 := rfl
@[simp] theorem franelB_one : franelB 1 = 1 := rfl

theorem franelB_rec (n : ℕ) :
    ((n : ℚ) + 2) ^ 2 * franelB (n + 2)
      = (7 * ((n : ℚ) + 1) ^ 2 + 7 * ((n : ℚ) + 1) + 2) * franelB (n + 1)
        + 8 * ((n : ℚ) + 1) ^ 2 * franelB n := by
  have hne : ((n : ℚ) + 2) ^ 2 ≠ 0 := by positivity
  rw [show franelB (n + 2)
      = ((7 * ((n : ℚ) + 1) ^ 2 + 7 * ((n : ℚ) + 1) + 2) * franelB (n + 1)
        + 8 * ((n : ℚ) + 1) ^ 2 * franelB n) / ((n : ℚ) + 2) ^ 2 from rfl]
  field_simp

theorem bFranelSym_zero : bFranelSym 0 = 0 := by
  norm_num [bFranelSym, wF, c3, Harm_zero]

theorem bFranelSym_one : bFranelSym 1 = 1 := by
  norm_num [bFranelSym, wF, c3, Finset.sum_range_succ,
    Harm_zero 1 (by norm_num : 0 < 1), Harm_zero 2 (by norm_num : 0 < 2),
    Harm_one 1 (by norm_num : 0 < 1), Harm_one 2 (by norm_num : 0 < 2)]

/-- **Closed form for the Franel second solution** (`MINIMAL_FORM_PROOF.md` §8.2):

    Σ_{k=0}^n C(n,k)³ ((1/8)(H⁽²⁾_k + H⁽²⁾_{n−k}) + (3/8)(H_k − H_{n−k})²)  =  B_n.  -/
theorem franel_closed_form (n : ℕ) : bFranelSym n = franelB n := by
  have key : ∀ n : ℕ, bFranelSym n = franelB n ∧ bFranelSym (n + 1) = franelB (n + 1) := by
    intro n
    induction n with
    | zero => exact ⟨by simp [bFranelSym_zero], by simp [bFranelSym_one]⟩
    | succ n ih =>
      refine ⟨ih.2, ?_⟩
      obtain ⟨h0, h1⟩ := ih
      have hrec := bFranelSym_rec n
      have hB := franelB_rec n
      have hne : ((n : ℚ) + 2) ^ 2 ≠ 0 := by positivity
      have : ((n : ℚ) + 2) ^ 2 * bFranelSym (n + 2) = ((n : ℚ) + 2) ^ 2 * franelB (n + 2) := by
        rw [hB, ← h0, ← h1]
        linear_combination hrec
      exact mul_left_cancel₀ hne this
  exact (key n).1

/-! ## 6a. Identification with the Franel row of `Instances` -/

/-- Rewriting of the original Franel row in terms of `wFOld`. -/
theorem bFranel_eq_old_sum (n : ℕ) :
    bFranel n = ∑ k ∈ range (n + 1), c3 n k * wFOld n k := by
  simp only [bFranel, c3, wFOld, Nat.cast_pow]
  refine Finset.sum_congr rfl fun k _ => ?_
  ring

/-- Reflection invariance of the old Franel sum. -/
theorem bFranel_old_reflect (n : ℕ) :
    (∑ k ∈ range (n + 1), c3 n k * wFOld n (n - k)) = bFranel n := by
  rw [bFranel_eq_old_sum]
  have h := Finset.sum_range_reflect (fun k => c3 n k * wFOld n k) (n + 1)
  rw [show n + 1 - 1 = n by omega] at h
  calc
    (∑ k ∈ range (n + 1), c3 n k * wFOld n (n - k)) =
        ∑ k ∈ range (n + 1), c3 n (n - k) * wFOld n (n - k) := by
          refine Finset.sum_congr rfl fun k hk => ?_
          have hkn : k ≤ n := by simpa using Finset.mem_range.1 hk
          rw [c3, c3, Nat.choose_symm hkn]
    _ = ∑ k ∈ range (n + 1), c3 n k * wFOld n k := h

/-- The symmetric and asymmetric harmonic formulas define exactly the same Franel row. -/
theorem bFranelSym_eq_bFranel (n : ℕ) : bFranelSym n = bFranel n := by
  rw [bFranelSym]
  calc
    (∑ k ∈ range (n + 1), c3 n k * wF n k) =
        ∑ k ∈ range (n + 1),
          c3 n k * ((1 / 2) * (wFOld n k + wFOld n (n - k))) := by
            refine Finset.sum_congr rfl fun k hk => ?_
            rw [wF_eq_reflection_average (by simpa using Finset.mem_range.1 hk)]
    _ = (1 / 2) * (∑ k ∈ range (n + 1), c3 n k * wFOld n k)
          + (1 / 2) * (∑ k ∈ range (n + 1), c3 n k * wFOld n (n - k)) := by
            rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
            refine Finset.sum_congr rfl fun k _ => ?_
            ring
    _ = bFranel n := by
          rw [← bFranel_eq_old_sum, bFranel_old_reflect]
          ring

/-- The row used by the Lucas theorem is the recurrence-defined Franel second solution. -/
theorem bFranel_eq_franelB (n : ℕ) : bFranel n = franelB n := by
  rw [← bFranelSym_eq_bFranel, franel_closed_form]

/-- **Lucas congruence for the recurrence-defined Franel second solution.** -/
theorem franelB_lucas {p : ℕ} [Fact p.Prime] (hp2 : p ≠ 2) {a r : ℕ}
    (ha : a < p) (hr : r < p) :
    PCong p ((p : ℚ) ^ 2 * franelB (a * p + r)) (franelB a * (franel r : ℚ)) := by
  simpa only [← bFranel_eq_franelB] using bFranel_lucas hp2 ha hr

/-- **Closed form, fully written out.** -/
theorem franel_harmonic_closed_form (n : ℕ) :
    ∑ k ∈ range (n + 1), ((n.choose k : ℚ)) ^ 3
        * ((1 / 8) * ((∑ j ∈ Finset.Icc 1 k, (1 : ℚ) / (j : ℚ) ^ 2)
              + ∑ j ∈ Finset.Icc 1 (n - k), (1 : ℚ) / (j : ℚ) ^ 2)
          + (3 / 8) * ((∑ j ∈ Finset.Icc 1 k, (1 : ℚ) / (j : ℚ))
              - ∑ j ∈ Finset.Icc 1 (n - k), (1 : ℚ) / (j : ℚ)) ^ 2)
      = franelB n := by
  have H1 : ∀ y : ℕ, Harm 1 y = ∑ j ∈ Finset.Icc 1 y, (1 : ℚ) / (j : ℚ) := fun y => by
    rw [Harm_eq 1 y (by norm_num)]
    simp only [pow_one]
  have H2 : ∀ y : ℕ, Harm 2 y = ∑ j ∈ Finset.Icc 1 y, (1 : ℚ) / (j : ℚ) ^ 2 := fun y =>
    Harm_eq 2 y (by norm_num)
  rw [← franel_closed_form, bFranelSym]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [c3, wF, H1 k, H1 (n - k), H2 k, H2 (n - k)]

/-! ## 7. s₁₀ = `Σ_k C(n,k)⁴`: definitions -/

/-- The symmetric s₁₀ weight `(1/10)(H⁽²⁾_k + H⁽²⁾_{n−k}) + (2/5)(H_k − H_{n−k})²`. -/
def w10 (n k : ℕ) : ℚ :=
  (1 / 10) * (Harm 2 k + Harm 2 (n - k)) + (2 / 5) * (Harm 1 k - Harm 1 (n - k)) ^ 2

/-- The symmetric-weight s₁₀ second solution. -/
def bS10Sym (n : ℕ) : ℚ := ∑ k ∈ range (n + 1), c4 n k * w10 n k

/-- `Den10 m = (m+1)⁴(m+2)⁴`. -/
def Den10 (m : ℕ) : ℚ := ((m : ℚ) + 1) ^ 4 * ((m : ℚ) + 2) ^ 4

theorem Den10_ne (m : ℕ) : Den10 m ≠ 0 := by
  have h : (0 : ℚ) ≤ (m : ℚ) := Nat.cast_nonneg m
  simp only [Den10]
  positivity

/-- The s₁₀ base term `Φ₁₀(m,k) = C(m+2,k)⁴/((m+1)⁴(m+2)⁴)`. -/
def Phi10 (m k : ℕ) : ℚ := ((m + 2).choose k : ℚ) ^ 4 / Den10 m

/-- The s₁₀ Zeilberger certificate numerator (`rho_10·n³` of `certs_stretch.m`). -/
def rho10 (x y : ℚ) : ℚ :=
  4 * y - 16 * y ^ 2 + 24 * y ^ 3 - 16 * y ^ 4 + 4 * y ^ 5 - 10 * x + 72 * y * x
    - 172 * y ^ 2 * x + 184 * y ^ 3 * x - 90 * y ^ 4 * x + 16 * y ^ 5 * x - 80 * x ^ 2
    + 368 * y * x ^ 2 - 600 * y ^ 2 * x ^ 2 + 416 * y ^ 3 * x ^ 2 - 104 * y ^ 4 * x ^ 2
    - 255 * x ^ 3 + 796 * y * x ^ 3 - 818 * y ^ 2 * x ^ 3 + 276 * y ^ 3 * x ^ 3
    - 385 * x ^ 4 + 756 * y * x ^ 4 - 374 * y ^ 2 * x ^ 4 - 275 * x ^ 5 + 260 * y * x ^ 5
    - 75 * x ^ 6

/-- `G₁₀(m,k) = Φ₁₀·k⁴·(m+1)·rho10(m+1,k)` (equals `k⁴ ρ₁₀ C(n+1,k)⁴/(n+1)⁴` at `n = m+1`). -/
def G10 (m k : ℕ) : ℚ := Phi10 m k * (k : ℚ) ^ 4 * ((m : ℚ) + 1) * rho10 ((m : ℚ) + 1) (k : ℚ)

/-- The Gosper certificate `N₁₀` (with its `1/(5n³)` prefactor). -/
def N10 (x y : ℚ) : ℚ :=
  4 * y ^ 3 * (-5 * y + 25 * y ^ 2 - 50 * y ^ 3 + 50 * y ^ 4 - 25 * y ^ 5 + 5 * y ^ 6
    + 10 * x - 95 * y * x + 300 * y ^ 2 * x - 450 * y ^ 3 * x + 350 * y ^ 4 * x
    - 135 * y ^ 5 * x + 20 * y ^ 6 * x + 90 * x ^ 2 - 550 * y * x ^ 2 + 1250 * y ^ 2 * x ^ 2
    - 1350 * y ^ 3 * x ^ 2 + 700 * y ^ 4 * x ^ 2 - 140 * y ^ 5 * x ^ 2 + 335 * x ^ 3
    - 1455 * y * x ^ 3 + 2326 * y ^ 2 * x ^ 3 - 1620 * y ^ 3 * x ^ 3 + 415 * y ^ 4 * x ^ 3
    + 640 * x ^ 4 - 1940 * y * x ^ 4 + 1977 * y ^ 2 * x ^ 4 - 670 * y ^ 3 * x ^ 4
    + 660 * x ^ 5 - 1270 * y * x ^ 5 + 626 * y ^ 2 * x ^ 5 + 350 * x ^ 6 - 325 * y * x ^ 6
    + 75 * x ^ 7) / (5 * x ^ 3)

/-- The Gosper certificate `M₁₀` (with its `−1/(2n³)` prefactor). -/
def M10 (x y : ℚ) : ℚ :=
  -(y ^ 2 * (-4 * y + 24 * y ^ 2 - 60 * y ^ 3 + 80 * y ^ 4 - 60 * y ^ 5 + 24 * y ^ 6
    - 4 * y ^ 7 + 6 * x - 76 * y * x + 306 * y ^ 2 * x - 600 * y ^ 3 * x + 650 * y ^ 4 * x
    - 396 * y ^ 5 * x + 126 * y ^ 6 * x - 16 * y ^ 7 * x + 60 * x ^ 2 - 480 * y * x ^ 2
    + 1440 * y ^ 2 * x ^ 2 - 2160 * y ^ 3 * x ^ 2 + 1740 * y ^ 4 * x ^ 2
    - 720 * y ^ 5 * x ^ 2 + 120 * y ^ 6 * x ^ 2 + 255 * x ^ 3 - 1470 * y * x ^ 3
    + 3285 * y ^ 2 * x ^ 3 - 3564 * y ^ 3 * x ^ 3 + 1885 * y ^ 4 * x ^ 3
    - 390 * y ^ 5 * x ^ 3 + 585 * x ^ 4 - 2460 * y * x ^ 4 + 3915 * y ^ 2 * x ^ 4
    - 2748 * y ^ 3 * x ^ 4 + 715 * y ^ 4 * x ^ 4 + 780 * x ^ 5 - 2304 * y * x ^ 5
    + 2349 * y ^ 2 * x ^ 5 - 804 * y ^ 3 * x ^ 5 + 606 * x ^ 6 - 1136 * y * x ^ 6
    + 561 * y ^ 2 * x ^ 6 + 255 * x ^ 7 - 230 * y * x ^ 7 + 45 * x ^ 8)) / (2 * x ^ 3)

/-- The Gosper part `Z₁₀(m,k) = C(m+1,k)⁴( N₁₀/(m+2−k)⁵·δ(m+1,k) + M₁₀/(m+2−k)⁶ )`. -/
def Z10 (m k : ℕ) : ℚ :=
  c4 (m + 1) k * (N10 ((m : ℚ) + 1) (k : ℚ) / ((m : ℚ) + 2 - k) ^ 5 * dlt (m + 1) k
    + M10 ((m : ℚ) + 1) (k : ℚ) / ((m : ℚ) + 2 - k) ^ 6)

/-- The single s₁₀ antidifference `Ψ₁₀ = w(m+1,·)·G₁₀ + Z₁₀`. -/
def Psi10 (m k : ℕ) : ℚ := w10 (m + 1) k * G10 m k + Z10 m k

/-! ## 8. s₁₀: Lemma 0, certificates, telescope -/

theorem l4top (m k : ℕ) :
    c4 (m + 2) k = Phi10 m k * (((m : ℚ) + 1) ^ 4 * ((m : ℚ) + 2) ^ 4) := by
  simp only [c4, Phi10, Den10]
  rw [div_mul_eq_mul_div, mul_div_assoc]
  rw [div_self (by have h : (0 : ℚ) ≤ (m : ℚ) := Nat.cast_nonneg m; positivity), mul_one]

theorem l4mid (m k : ℕ) :
    c4 (m + 1) k = Phi10 m k * (((m : ℚ) + 1) ^ 4 * ((m : ℚ) + 2 - k) ^ 4) := by
  simp only [c4, Phi10, Den10]
  rw [div_mul_eq_mul_div, eq_div_iff (by simpa [Den10] using Den10_ne m)]
  linear_combination (-((m : ℚ) + 1) ^ 4) * quart_a m k

theorem l4low (m k : ℕ) :
    c4 m k = Phi10 m k * (((m : ℚ) + 2 - k) ^ 4 * ((m : ℚ) + 1 - k) ^ 4) := by
  simp only [c4, Phi10, Den10]
  rw [div_mul_eq_mul_div, eq_div_iff (by simpa [Den10] using Den10_ne m)]
  linear_combination (-((m : ℚ) + 1 - k) ^ 4) * quart_a m k
    + (-((m : ℚ) + 2) ^ 4) * quart_b m k

theorem Phi10_succ (m k : ℕ) :
    Phi10 m (k + 1) * ((k : ℚ) + 1) ^ 4 = Phi10 m k * ((m : ℚ) + 2 - k) ^ 4 := by
  simp only [Phi10]
  rw [div_mul_eq_mul_div, div_mul_eq_mul_div, quart_c]

theorem G10_succ (m k : ℕ) :
    G10 m (k + 1)
      = Phi10 m k * ((m : ℚ) + 2 - k) ^ 4 * ((m : ℚ) + 1)
          * rho10 ((m : ℚ) + 1) ((k : ℚ) + 1) := by
  simp only [G10]
  push_cast
  linear_combination ((m : ℚ) + 1) * rho10 ((m : ℚ) + 1) ((k : ℚ) + 1) * Phi10_succ m k

theorem l4mid_succ (m k : ℕ) :
    c4 (m + 1) (k + 1)
      = Phi10 m k * (((m : ℚ) + 1) ^ 4 * ((m : ℚ) + 2 - k) ^ 4 * ((m : ℚ) + 1 - k) ^ 4)
          / ((k : ℚ) + 1) ^ 4 := by
  have hk : ((k : ℚ) + 1) ^ 4 ≠ 0 := by positivity
  rw [eq_div_iff hk]
  have h := quart_d m k
  simp only [c4]
  rw [h, ← c4, l4mid]
  ring

/-- **CERT-1 for s₁₀**: `L[C(·,k)⁴] = G₁₀(m,k+1) − G₁₀(m,k)` for **all** `m, k ≥ 0`. -/
theorem propB_10 (m k : ℕ) :
    ((m : ℚ) + 2) ^ 3 * c4 (m + 2) k
        - (2 * ((m : ℚ) + 1) + 1) * (6 * ((m : ℚ) + 1) ^ 2 + 6 * ((m : ℚ) + 1) + 2)
            * c4 (m + 1) k
        - ((m : ℚ) + 1) * (64 * ((m : ℚ) + 1) ^ 2 - 4) * c4 m k
      = G10 m (k + 1) - G10 m k := by
  rw [l4top, l4mid, l4low, G10_succ]
  simp only [G10, rho10]
  ring

set_option maxRecDepth 8000 in
set_option maxHeartbeats 3200000 in
/-- **CERT-2 for s₁₀** (the two folded Gosper problems), for `k ≤ m`. -/
theorem propC_10 (m k : ℕ) (hk : k ≤ m) :
    ((m : ℚ) + 2) ^ 3 * c4 (m + 2) k * (w10 (m + 2) k - w10 (m + 1) k)
        - ((m : ℚ) + 1) * (64 * ((m : ℚ) + 1) ^ 2 - 4) * c4 m k * (w10 m k - w10 (m + 1) k)
        - (w10 (m + 1) (k + 1) - w10 (m + 1) k) * G10 m (k + 1)
      = Z10 m (k + 1) - Z10 m k := by
  obtain ⟨j, rfl⟩ := Nat.exists_eq_add_of_le hk
  rw [G10_succ]
  simp only [Z10, w10, dlt]
  rw [l4mid_succ, l4top, l4mid, l4low]
  simp only [show k + j + 2 - k = j + 1 + 1 from by omega,
    show k + j + 1 - k = j + 1 from by omega, show k + j - k = j from by omega,
    show k + j + 1 - (k + 1) = j from by omega]
  simp only [Harm_succ 2 (j + 1), Harm_succ 1 (j + 1),
    Harm_succ 2 j, Harm_succ 1 j, Harm_succ 2 k, Harm_succ 1 k]
  have h1 : ((j : ℚ) + 1) ≠ 0 := by positivity
  have h2 : ((j : ℚ) + 1 + 1) ≠ 0 := by positivity
  have h3 : ((k : ℚ) + 1) ≠ 0 := by positivity
  have h4 : ((k : ℚ) + (j : ℚ) + 1) ≠ 0 := by positivity
  have h5 : ((k : ℚ) + (j : ℚ) + 2) ≠ 0 := by positivity
  simp only [rho10, N10, M10]
  push_cast
  simp only [show ((k : ℚ) + (j : ℚ) + 2 - (k : ℚ)) = (j : ℚ) + 2 from by ring,
    show ((k : ℚ) + (j : ℚ) + 2 - ((k : ℚ) + 1)) = (j : ℚ) + 1 from by ring]
  have h6 : ((j : ℚ) + 2) ≠ 0 := by positivity
  field_simp
  ring

theorem Psi10_zero (m : ℕ) : Psi10 m 0 = 0 := by
  simp [Psi10, G10, Z10, N10, M10, c4, dlt]

theorem Phi10_eq_zero_of_lt {m k : ℕ} (h : m + 2 < k) : Phi10 m k = 0 := by
  simp [Phi10, Nat.choose_eq_zero_of_lt h]

theorem Psi10_top (m : ℕ) : Psi10 m (m + 3) = 0 := by
  have h1 : Phi10 m (m + 3) = 0 := Phi10_eq_zero_of_lt (by omega)
  have h2 : c4 (m + 1) (m + 3) = 0 := c4_eq_zero_of_lt (by omega)
  simp [Psi10, G10, Z10, h1, h2]

/-- **The telescoping identity (`star`) for s₁₀**, at every cell `k ≥ 0`. -/
theorem star_10 (m k : ℕ) :
    ((m : ℚ) + 2) ^ 3 * (c4 (m + 2) k * w10 (m + 2) k)
        - (2 * ((m : ℚ) + 1) + 1) * (6 * ((m : ℚ) + 1) ^ 2 + 6 * ((m : ℚ) + 1) + 2)
            * (c4 (m + 1) k * w10 (m + 1) k)
        - ((m : ℚ) + 1) * (64 * ((m : ℚ) + 1) ^ 2 - 4) * (c4 m k * w10 m k)
      = Psi10 m (k + 1) - Psi10 m k := by
  rcases Nat.lt_or_ge k (m + 1) with hk | hk
  · have hB := propB_10 m k
    have hC := propC_10 m k (by omega)
    simp only [Psi10]
    linear_combination w10 (m + 1) k * hB + hC
  rcases Nat.eq_or_lt_of_le hk with hk1 | hk1
  · subst hk1
    have e2 : (m + 2).choose (m + 1) = m + 2 := by
      rw [show m + 2 = m + 1 + 1 from rfl, Nat.choose_succ_self_right]
    have e3 : (m + 1).choose (m + 1) = 1 := Nat.choose_self (m + 1)
    have e4 : m.choose (m + 1) = 0 := Nat.choose_eq_zero_of_lt (by omega)
    have e5 : (m + 1).choose (m + 2) = 0 := Nat.choose_eq_zero_of_lt (by omega)
    have e6 : (m + 2).choose (m + 2) = 1 := Nat.choose_self (m + 2)
    have hH2 : Harm 2 (m + 2) = Harm 2 (m + 1) + 1 / ((m : ℚ) + 2) ^ 2 := by
      have h := Harm_succ 2 (m + 1); push_cast at h
      rw [show m + 1 + 1 = m + 2 from rfl] at h
      rw [h]; ring_nf
    have hH1 : Harm 1 (m + 2) = Harm 1 (m + 1) + 1 / ((m : ℚ) + 2) := by
      have h := Harm_succ 1 (m + 1); push_cast at h
      rw [show m + 1 + 1 = m + 2 from rfl] at h
      rw [h]; ring_nf
    have h1 : ((m : ℚ) + 1) ≠ 0 := by positivity
    have h2 : ((m : ℚ) + 2) ≠ 0 := by positivity
    simp only [Psi10, G10, Z10, w10, dlt, Phi10, Den10, c4, e2, e3, e4, e5, e6,
      show m + 2 - (m + 1) = 1 from by omega,
      show m + 1 - (m + 2) = 0 from by omega, show m + 1 - (m + 1) = 0 from by omega]
    rw [hH2, hH1, Harm_one 1 (by norm_num), Harm_one 2 (by norm_num),
      Harm_zero 1 (by norm_num), Harm_zero 2 (by norm_num)]
    simp only [rho10, N10, M10]
    push_cast
    field_simp
    ring
  · rcases Nat.eq_or_lt_of_le hk1 with hk2 | hk2
    · subst hk2
      have e1 : (m + 1).choose (m + 2) = 0 := Nat.choose_eq_zero_of_lt (by omega)
      have e2 : m.choose (m + 2) = 0 := Nat.choose_eq_zero_of_lt (by omega)
      have e3 : (m + 2).choose (m + 2) = 1 := Nat.choose_self (m + 2)
      have e4 : (m + 2).choose (m + 3) = 0 := Nat.choose_eq_zero_of_lt (by omega)
      have e5 : (m + 1).choose (m + 3) = 0 := Nat.choose_eq_zero_of_lt (by omega)
      simp only [Psi10, G10, Z10, w10, dlt, Phi10, Den10, c4, e1, e2, e3, e4, e5,
        Nat.sub_self, show m + 1 - (m + 2) = 0 from by omega,
        show m + 1 - (m + 3) = 0 from by omega]
      have h1 : ((m : ℚ) + 1) ≠ 0 := by positivity
      have h2 : ((m : ℚ) + 2) ≠ 0 := by positivity
      simp only [rho10]
      push_cast
      field_simp
      ring
    · have e1 : (m + 2).choose k = 0 := Nat.choose_eq_zero_of_lt (by omega)
      have e2 : (m + 1).choose k = 0 := Nat.choose_eq_zero_of_lt (by omega)
      have e3 : m.choose k = 0 := Nat.choose_eq_zero_of_lt (by omega)
      have e4 : (m + 2).choose (k + 1) = 0 := Nat.choose_eq_zero_of_lt (by omega)
      have e5 : (m + 1).choose (k + 1) = 0 := Nat.choose_eq_zero_of_lt (by omega)
      simp [Psi10, G10, Z10, Phi10, c4, e1, e2, e3, e4, e5]

/-! ## 9. s₁₀: recurrence, companion, closed form -/

theorem bS10Sym_sum_range {n N : ℕ} (h : n + 1 ≤ N) :
    bS10Sym n = ∑ k ∈ range N, c4 n k * w10 n k := by
  refine Finset.sum_subset
    (fun k hk => Finset.mem_range.2 (lt_of_lt_of_le (Finset.mem_range.1 hk) h)) ?_
  intro k _ hk
  simp only [Finset.mem_range, not_lt] at hk
  rw [c4_eq_zero_of_lt (by omega : n < k)]
  simp

theorem bS10Sym_rec (m : ℕ) :
    ((m : ℚ) + 2) ^ 3 * bS10Sym (m + 2)
        - (2 * ((m : ℚ) + 1) + 1) * (6 * ((m : ℚ) + 1) ^ 2 + 6 * ((m : ℚ) + 1) + 2)
            * bS10Sym (m + 1)
        - ((m : ℚ) + 1) * (64 * ((m : ℚ) + 1) ^ 2 - 4) * bS10Sym m = 0 := by
  rw [bS10Sym_sum_range (n := m + 2) (N := m + 3) (by omega),
    bS10Sym_sum_range (n := m + 1) (N := m + 3) (by omega),
    bS10Sym_sum_range (n := m) (N := m + 3) (by omega),
    Finset.mul_sum, Finset.mul_sum, Finset.mul_sum,
    ← Finset.sum_sub_distrib, ← Finset.sum_sub_distrib]
  rw [Finset.sum_congr rfl (fun k _ => star_10 m k)]
  rw [Finset.sum_range_sub (fun k => Psi10 m k) (m + 3), Psi10_top, Psi10_zero]
  ring

/-- **The s₁₀ second solution**, defined by
`(n+1)³ B_{n+1} = (2n+1)(6n²+6n+2) B_n + n(64n²−4) B_{n−1}`, `B₀ = 0`, `B₁ = 1`. -/
def s10B : ℕ → ℚ
  | 0 => 0
  | 1 => 1
  | (n + 2) => ((2 * ((n : ℚ) + 1) + 1) * (6 * ((n : ℚ) + 1) ^ 2 + 6 * ((n : ℚ) + 1) + 2)
        * s10B (n + 1)
      + ((n : ℚ) + 1) * (64 * ((n : ℚ) + 1) ^ 2 - 4) * s10B n) / ((n : ℚ) + 2) ^ 3

@[simp] theorem s10B_zero : s10B 0 = 0 := rfl
@[simp] theorem s10B_one : s10B 1 = 1 := rfl

theorem s10B_rec (n : ℕ) :
    ((n : ℚ) + 2) ^ 3 * s10B (n + 2)
      = (2 * ((n : ℚ) + 1) + 1) * (6 * ((n : ℚ) + 1) ^ 2 + 6 * ((n : ℚ) + 1) + 2)
          * s10B (n + 1)
        + ((n : ℚ) + 1) * (64 * ((n : ℚ) + 1) ^ 2 - 4) * s10B n := by
  have hne : ((n : ℚ) + 2) ^ 3 ≠ 0 := by positivity
  rw [show s10B (n + 2)
      = ((2 * ((n : ℚ) + 1) + 1) * (6 * ((n : ℚ) + 1) ^ 2 + 6 * ((n : ℚ) + 1) + 2)
          * s10B (n + 1)
        + ((n : ℚ) + 1) * (64 * ((n : ℚ) + 1) ^ 2 - 4) * s10B n) / ((n : ℚ) + 2) ^ 3 from rfl]
  field_simp

theorem bS10Sym_zero : bS10Sym 0 = 0 := by
  norm_num [bS10Sym, w10, c4, Harm_zero]

theorem bS10Sym_one : bS10Sym 1 = 1 := by
  norm_num [bS10Sym, w10, c4, Finset.sum_range_succ,
    Harm_zero 1 (by norm_num : 0 < 1), Harm_zero 2 (by norm_num : 0 < 2),
    Harm_one 1 (by norm_num : 0 < 1), Harm_one 2 (by norm_num : 0 < 2)]

/-- **Closed form for the s₁₀ second solution** (`MINIMAL_FORM_PROOF.md` §8.3). -/
theorem s10_closed_form (n : ℕ) : bS10Sym n = s10B n := by
  have key : ∀ n : ℕ, bS10Sym n = s10B n ∧ bS10Sym (n + 1) = s10B (n + 1) := by
    intro n
    induction n with
    | zero => exact ⟨by simp [bS10Sym_zero], by simp [bS10Sym_one]⟩
    | succ n ih =>
      refine ⟨ih.2, ?_⟩
      obtain ⟨h0, h1⟩ := ih
      have hrec := bS10Sym_rec n
      have hB := s10B_rec n
      have hne : ((n : ℚ) + 2) ^ 3 ≠ 0 := by positivity
      have : ((n : ℚ) + 2) ^ 3 * bS10Sym (n + 2) = ((n : ℚ) + 2) ^ 3 * s10B (n + 2) := by
        rw [hB, ← h0, ← h1]
        linear_combination hrec
      exact mul_left_cancel₀ hne this
  exact (key n).1

/-! ## 9a. Lucas congruence for the recurrence-defined s₁₀ solution -/

/-- The quartic binomial summand as an integer. -/
def S10 (n k : ℕ) : ℤ := ((n.choose k) ^ 4 : ℕ)

/-- The primary s₁₀ row `A(n) = Σ_k C(n,k)⁴`. -/
def s10A (n : ℕ) : ℕ := ∑ k ∈ range (n + 1), (n.choose k) ^ 4

def s10LetK2 : Letter := letterH 2 (by norm_num) (fun _ k => k)
def s10LetNK2 : Letter := letterH 2 (by norm_num) (fun n k => n - k)
def s10LetK1 : Letter := letterH 1 (by norm_num) (fun _ k => k)
def s10LetNK1 : Letter := letterH 1 (by norm_num) (fun n k => n - k)

def s10J : Finset (Fin 5) := Finset.univ
def s10C : Fin 5 → ℚ := ![1 / 10, 1 / 10, 4 / 10, 4 / 10, -(8 / 10)]
def s10Mon : Fin 5 → List Letter :=
  ![[s10LetK2], [s10LetNK2], [s10LetK1, s10LetK1],
    [s10LetNK1, s10LetNK1], [s10LetK1, s10LetNK1]]

theorem W_s10 (n k : ℕ) : W s10J s10C s10Mon n k = w10 n k := by
  simp [W, s10J, s10C, s10Mon, monVal, s10LetK2, s10LetNK2, s10LetK1,
    s10LetNK1, w10, Fin.sum_univ_five]
  ring

theorem bS10Sym_eq_Brow (n : ℕ) : bS10Sym n = Brow s10J s10C s10Mon S10 n := by
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [W_s10]
  simp [c4, S10]

theorem Arow_S10 (n : ℕ) : Arow S10 n = (s10A n : ℤ) := by
  simp [Arow, S10, s10A]

theorem s10Mon_mem {j : Fin 5} {ℓ : Letter} (h : ℓ ∈ s10Mon j) :
    ℓ = s10LetK2 ∨ ℓ = s10LetNK2 ∨ ℓ = s10LetK1 ∨ ℓ = s10LetNK1 := by
  fin_cases j <;> simp [s10Mon] at h <;> tauto

/-- **s₁₀ instance of Theorem LB.**  For every prime not dividing `10`,
`p² B_{ap+r} ≡ B_a A_r (mod p)` for the symmetric harmonic sum. -/
theorem bS10Sym_lucas {p : ℕ} [Fact p.Prime] (hp10 : ¬ (p : ℤ) ∣ 10)
    {a r : ℕ} (ha : a < p) (hr : r < p) :
    PCong p ((p : ℚ) ^ 2 * bS10Sym (a * p + r)) (bS10Sym a * (s10A r : ℚ)) := by
  have hpp : p.Prime := Fact.out
  have hp0 : 0 < p := hpp.pos
  have key := theorem_LB (p := p) (J := s10J) (c := s10C) (mon := s10Mon) (S := S10)
    (w := 2) (χp := 1)
    (H1 := by
      intro a b r s hr hs
      have h := choose_digits (p := p) a b r s hr hs
      simp only [S10]
      push_cast
      rw [h]
      ring)
    (H2 := by
      intro n k h
      simp [S10, Nat.choose_eq_zero_of_lt h])
    (H3 := by
      intro a b r s hr hs hba hne j hj ℓ hℓ
      have hsr : s ≤ r := by
        by_contra hcon
        exact hne (by simp [S10, Nat.choose_eq_zero_of_lt (by omega : r < s)])
      rcases s10Mon_mem hℓ with rfl | rfl | rfl | rfl
      · simpa [s10LetK2] using digit_div hp0 hs
      · have hbp : b * p ≤ a * p := Nat.mul_le_mul_right p hba
        have hsub : (a - b) * p = a * p - b * p := Nat.sub_mul a b p
        have e : (a * p + r) - (b * p + s) = (a - b) * p + (r - s) := by omega
        simpa [s10LetNK2, e] using digit_div hp0 (show r - s < p by omega)
      · simpa [s10LetK1] using digit_div hp0 hs
      · have hbp : b * p ≤ a * p := Nat.mul_le_mul_right p hba
        have hsub : (a - b) * p = a * p - b * p := Nat.sub_mul a b p
        have e : (a * p + r) - (b * p + s) = (a - b) * p + (r - s) := by omega
        simpa [s10LetNK1, e] using digit_div hp0 (show r - s < p by omega))
    (H4 := by
      intro j hj ℓ hℓ n k hk
      rcases s10Mon_mem hℓ with rfl | rfl | rfl | rfl
      · simpa [s10LetK2] using hk
      · simp [s10LetNK2]
      · simpa [s10LetK1] using hk
      · simp [s10LetNK1])
    (H4c := by
      intro j hj
      fin_cases j
      · simpa [s10C] using PInt.intCast_div (p := p) (a := 1) (b := 10) hp10
      · simpa [s10C] using PInt.intCast_div (p := p) (a := 1) (b := 10) hp10
      · simpa [s10C] using PInt.intCast_div (p := p) (a := 4) (b := 10) hp10
      · simpa [s10C] using PInt.intCast_div (p := p) (a := 4) (b := 10) hp10
      · exact PInt.neg (by
          simpa [s10C] using PInt.intCast_div (p := p) (a := 8) (b := 10) hp10))
    (Hw := by
      intro j hj
      fin_cases j <;>
        simp [s10Mon, monDeg, s10LetK2, s10LetNK2, s10LetK1, s10LetNK1])
    (H5 := by
      intro j hj
      fin_cases j <;>
        simp [s10Mon, monChi, s10LetK2, s10LetNK2, s10LetK1, s10LetNK1])
    ha hr
  rw [← bS10Sym_eq_Brow, ← bS10Sym_eq_Brow, Arow_S10] at key
  simpa using key

/-- **Lucas congruence for the recurrence-defined s₁₀ second solution.** -/
theorem s10B_lucas {p : ℕ} [Fact p.Prime] (hp10 : ¬ (p : ℤ) ∣ 10)
    {a r : ℕ} (ha : a < p) (hr : r < p) :
    PCong p ((p : ℚ) ^ 2 * s10B (a * p + r)) (s10B a * (s10A r : ℚ)) := by
  simpa only [← s10_closed_form] using bS10Sym_lucas hp10 ha hr

/-- **Closed form, fully written out.** -/
theorem s10_harmonic_closed_form (n : ℕ) :
    ∑ k ∈ range (n + 1), ((n.choose k : ℚ)) ^ 4
        * ((1 / 10) * ((∑ j ∈ Finset.Icc 1 k, (1 : ℚ) / (j : ℚ) ^ 2)
              + ∑ j ∈ Finset.Icc 1 (n - k), (1 : ℚ) / (j : ℚ) ^ 2)
          + (2 / 5) * ((∑ j ∈ Finset.Icc 1 k, (1 : ℚ) / (j : ℚ))
              - ∑ j ∈ Finset.Icc 1 (n - k), (1 : ℚ) / (j : ℚ)) ^ 2)
      = s10B n := by
  have H1 : ∀ y : ℕ, Harm 1 y = ∑ j ∈ Finset.Icc 1 y, (1 : ℚ) / (j : ℚ) := fun y => by
    rw [Harm_eq 1 y (by norm_num)]
    simp only [pow_one]
  have H2 : ∀ y : ℕ, Harm 2 y = ∑ j ∈ Finset.Icc 1 y, (1 : ℚ) / (j : ℚ) ^ 2 := fun y =>
    Harm_eq 2 y (by norm_num)
  rw [← s10_closed_form, bS10Sym]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [c4, w10, H1 k, H1 (n - k), H2 k, H2 (n - k)]

section Sanity

-- Franel second solution `0, 1, 4, 208/9, 1280/9, 208384/225` and
-- s₁₀ second solution `0, 1, 21/4, 1001/18, 85085/144` — the values of
-- `MINIMAL_FORM_PROOF.md` §8.2/§8.3, from the recurrence and from the sum.
#eval (List.range 6).map franelB
#eval (List.range 6).map bFranelSym
#eval (List.range 5).map s10B
#eval (List.range 5).map bS10Sym

/-- Kernel-checked: the sum agrees with the recurrence at `n = 3` (Franel). -/
example : bFranelSym 3 = 208 / 9 := by
  norm_num [bFranelSym, wF, c3, Finset.sum_range_succ, Harm_succ, Harm_zero,
    Nat.choose]

end Sanity

/-! Kernel audit for the two closed forms and the Franel synthesis. -/
#print axioms franel_harmonic_closed_form
#print axioms s10_harmonic_closed_form
#print axioms bFranelSym_eq_bFranel
#print axioms bFranel_eq_franelB
#print axioms franelB_lucas
#print axioms s10B_lucas

end ZetaLucas
