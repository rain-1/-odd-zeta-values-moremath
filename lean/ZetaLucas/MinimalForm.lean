/-
# The harmonic closed form for Apéry's ζ(3) numerators `b_n`

**Target.**  Apéry's second solution `b_n` of the ζ(3) recurrence

    (n+1)³ b_{n+1} = (34n³ + 51n² + 27n + 5) b_n − n³ b_{n−1},        b₀ = 0, b₁ = 6

is here *defined* by that recurrence (`bApery`), and the theorem proved is that it is computed by
the **single explicit sum**

    b_n  =  Σ_{k=0}^{n} C(n,k)² C(n+k,k)² · ( 2 H⁽³⁾_n − H⁽³⁾_k ),     H⁽³⁾_y = Σ_{j=1}^y 1/j³

(`bMin_eq_bApery`).  This is the "minimal form" of `work/MINIMAL_FORM_PROOF.md`; it upgrades
`Instances.bMin_lucas` from a statement about an explicit sum to a statement about the classical
Apéry companion sequence.

**Proof, following `work/MINIMAL_FORM_PROOF.md` §§0–4 (route R1, Theorem 1).**  Everything is
driven by *Lemma 0*, which turns every binomial ratio into a multiplicative absorption identity
valid for **all** `k ≥ 0` (no `0/0`, no boundary case).  Writing `n = m+1 ≥ 1` and

    Φ(m,k) = C(m+2,k)² C(m+k,k)² / ((m+1)²(m+2)²)

one has, as identities in ℚ for all `m, k : ℕ` (`l0a`–`l0d`):

    A(m+1,k) = Φ·(m+2−k)²(m+1+k)²,      A(m+2,k) = Φ·(m+1+k)²(m+2+k)²,
    A(m,k)   = Φ·(m+2−k)²(m+1−k)²,      Φ(m,k+1)(k+1)⁴ = Φ(m,k)(m+2−k)²(m+1+k)².

After Lemma 0 every step is `Φ(m,k)` times a **polynomial identity in ℚ[m,k]**, closed by `ring`:

* `propB`  — CERT-1, Zeilberger's certificate `G = Φ k⁴ T`, `T(n,k) = 4(2n+1)(2k²−3k−4n²−4n)`;
* `propC`  — CERT-2, the Gosper certificate `K = Φ k⁴ U/(n²(n+1)²)`,
             `U(n,k) = −4(k−1)(2n+1)(2n²+2n+1−k)`, which kills the weight correction.

The two certificates combine into a **single telescope**: with

    Ψ(m,k) = (2H⁽³⁾_{m+1} − H⁽³⁾_k)·G(m,k) + K(m,k) + Gd(m,k),      Gd = Φ k T,

the `k`-summand of `(L b)(m+1)` is exactly `Ψ(m,k+1) − Ψ(m,k)` (`star`), so
`Finset.sum_range_sub` collapses the whole sum to `Ψ(m,m+3) − Ψ(m,0) = 0`.  There is no Abel
summation step and no boundary bookkeeping beyond the two evaluations `Ψ(m,0) = Ψ(m,m+3) = 0`.

The only analytic input is `H⁽³⁾_{y+1} − H⁽³⁾_y = 1/(y+1)³` (`Harm_succ`).

**Scope.**  The classical *double-sum* form of `b_n` (van der Poorten's
`Σ_k A(n,k)(H⁽³⁾_n + Σ_{m≤k}(−1)^{m−1}/(2m³C(n,m)C(n+m,m)))`) is **not** formalized here; it is
`MINIMAL_FORM_PROOF.md` §5 (Step D, CERT-3…CERT-6).  What is formalized is the identification of
the minimal sum with the sequence *defined by Apéry's recurrence and initial values*.
-/
import ZetaLucas.Instances

open Finset

namespace ZetaLucas

/-! ## 0. The two absorption identities -/

/-- **Absorption 1**: `C(N+1,k)·(N+1−k) = (N+1)·C(N,k)` over ℚ, for **every** `k ≥ 0`
(both sides vanish when `k > N+1`, so no range hypothesis is needed). -/
theorem absorb (N k : ℕ) :
    ((N + 1).choose k : ℚ) * ((N : ℚ) + 1 - k) = ((N : ℚ) + 1) * (N.choose k : ℚ) := by
  rcases Nat.lt_or_ge (N + 1) k with h | h
  · rw [Nat.choose_eq_zero_of_lt h, Nat.choose_eq_zero_of_lt (by omega : N < k)]
    push_cast
    ring
  · have hnat : (N + 1).choose k * (N + 1 - k) = (N + 1) * N.choose k := by
      rw [← Nat.choose_mul_succ_eq N k]; ring
    have hq := congrArg (fun x : ℕ => (x : ℚ)) hnat
    push_cast [Nat.cast_sub h] at hq
    linear_combination hq

/-- **Absorption 2**: `C(N,k+1)·(k+1) = C(N,k)·(N−k)` over ℚ, for every `k ≥ 0`. -/
theorem absorb2 (N k : ℕ) :
    (N.choose (k + 1) : ℚ) * ((k : ℚ) + 1) = (N.choose k : ℚ) * ((N : ℚ) - k) := by
  rcases Nat.lt_or_ge N k with h | h
  · rw [Nat.choose_eq_zero_of_lt h, Nat.choose_eq_zero_of_lt (by omega : N < k + 1)]
    push_cast
    ring
  · have hq := congrArg (fun x : ℕ => (x : ℚ)) (Nat.choose_succ_right_eq N k)
    push_cast [Nat.cast_sub h] at hq
    linear_combination hq

/-- `C(m+2,k)·(m+2−k) = (m+2)·C(m+1,k)`. -/
theorem abs_a (m k : ℕ) :
    ((m + 2).choose k : ℚ) * ((m : ℚ) + 2 - k) = ((m : ℚ) + 2) * ((m + 1).choose k : ℚ) := by
  have h := absorb (m + 1) k
  rw [show m + 1 + 1 = m + 2 by omega] at h
  push_cast at h
  linear_combination h

/-- `C(m+1,k)·(m+1−k) = (m+1)·C(m,k)`. -/
theorem abs_b (m k : ℕ) :
    ((m + 1).choose k : ℚ) * ((m : ℚ) + 1 - k) = ((m : ℚ) + 1) * (m.choose k : ℚ) := absorb m k

/-- `C(m+k+1,k)·(m+1) = (m+k+1)·C(m+k,k)`. -/
theorem abs_c (m k : ℕ) :
    ((m + k + 1).choose k : ℚ) * ((m : ℚ) + 1)
      = ((m : ℚ) + k + 1) * ((m + k).choose k : ℚ) := by
  have h := absorb (m + k) k
  push_cast at h
  linear_combination h

/-- `C(m+k+2,k)·(m+2) = (m+k+2)·C(m+k+1,k)`. -/
theorem abs_d (m k : ℕ) :
    ((m + k + 2).choose k : ℚ) * ((m : ℚ) + 2)
      = ((m : ℚ) + k + 2) * ((m + k + 1).choose k : ℚ) := by
  have h := absorb (m + k + 1) k
  rw [show m + k + 1 + 1 = m + k + 2 by omega] at h
  push_cast at h
  linear_combination h

/-! ## 1. `Φ` and Lemma 0 -/

/-- `Den m = (m+1)²(m+2)²`, i.e. `n²(n+1)²` for `n = m+1`. -/
def Den (m : ℕ) : ℚ := ((m : ℚ) + 1) ^ 2 * ((m : ℚ) + 2) ^ 2

theorem Den_pos (m : ℕ) : 0 < Den m := by
  have h : (0 : ℚ) ≤ (m : ℚ) := Nat.cast_nonneg m
  simp only [Den]
  positivity

theorem Den_ne (m : ℕ) : Den m ≠ 0 := (Den_pos m).ne'

/-- The **base term** `Φ(n,k) = C(n+1,k)²C(n+k−1,k)²/(n²(n+1)²)` of `MINIMAL_FORM_PROOF.md` §0,
written at `n = m+1` so that no natural subtraction occurs. -/
def Phi (m k : ℕ) : ℚ := (((m + 2).choose k : ℚ) * ((m + k).choose k : ℚ)) ^ 2 / Den m

theorem A_cast (n k : ℕ) : (A n k : ℚ) = (n.choose k : ℚ) ^ 2 * (((n + k).choose k : ℚ)) ^ 2 := by
  simp only [A]
  push_cast
  ring

/-- **Lemma 0(a)**: `A(n,k) = Φ(n,k)(n+1−k)²(n+k)²` at `n = m+1`. -/
theorem l0a (m k : ℕ) :
    (A (m + 1) k : ℚ) = Phi m k * (((m : ℚ) + 2 - k) ^ 2 * ((m : ℚ) + 1 + k) ^ 2) := by
  have e1 : ((m + 2).choose k : ℚ) ^ 2 * ((m : ℚ) + 2 - k) ^ 2
      = ((m : ℚ) + 2) ^ 2 * ((m + 1).choose k : ℚ) ^ 2 := by
    rw [← mul_pow, ← mul_pow, abs_a m k]
  have e2 : ((m + k + 1).choose k : ℚ) ^ 2 * ((m : ℚ) + 1) ^ 2
      = ((m : ℚ) + k + 1) ^ 2 * ((m + k).choose k : ℚ) ^ 2 := by
    rw [← mul_pow, ← mul_pow, abs_c m k]
  simp only [Phi, Den]
  rw [div_mul_eq_mul_div, eq_div_iff (by simpa [Den] using Den_ne m), A_cast,
    show m + 1 + k = m + k + 1 by omega]
  linear_combination (-(((m + k + 1).choose k : ℚ) ^ 2 * ((m : ℚ) + 1) ^ 2)) * e1
    + (((m + 2).choose k : ℚ) ^ 2 * ((m : ℚ) + 2 - k) ^ 2) * e2

/-- **Lemma 0(b)**: `A(n+1,k) = Φ(n,k)(n+k)²(n+k+1)²` at `n = m+1`. -/
theorem l0b (m k : ℕ) :
    (A (m + 2) k : ℚ) = Phi m k * (((m : ℚ) + 1 + k) ^ 2 * ((m : ℚ) + 2 + k) ^ 2) := by
  have f1 : ((m + k + 2).choose k : ℚ) ^ 2 * ((m : ℚ) + 2) ^ 2
      = ((m : ℚ) + k + 2) ^ 2 * ((m + k + 1).choose k : ℚ) ^ 2 := by
    rw [← mul_pow, ← mul_pow, abs_d m k]
  have f2 : ((m + k + 1).choose k : ℚ) ^ 2 * ((m : ℚ) + 1) ^ 2
      = ((m : ℚ) + k + 1) ^ 2 * ((m + k).choose k : ℚ) ^ 2 := by
    rw [← mul_pow, ← mul_pow, abs_c m k]
  simp only [Phi, Den]
  rw [div_mul_eq_mul_div, eq_div_iff (by simpa [Den] using Den_ne m), A_cast,
    show m + 2 + k = m + k + 2 by omega]
  linear_combination (((m + 2).choose k : ℚ) ^ 2 * ((m : ℚ) + 1) ^ 2) * f1
    + (((m + 2).choose k : ℚ) ^ 2 * ((m : ℚ) + k + 2) ^ 2) * f2

/-- **Lemma 0(c)**: `A(n−1,k) = Φ(n,k)(n+1−k)²(n−k)²` at `n = m+1`. -/
theorem l0c (m k : ℕ) :
    (A m k : ℚ) = Phi m k * (((m : ℚ) + 2 - k) ^ 2 * ((m : ℚ) + 1 - k) ^ 2) := by
  have e1 : ((m + 2).choose k : ℚ) ^ 2 * ((m : ℚ) + 2 - k) ^ 2
      = ((m : ℚ) + 2) ^ 2 * ((m + 1).choose k : ℚ) ^ 2 := by
    rw [← mul_pow, ← mul_pow, abs_a m k]
  have e2 : ((m + 1).choose k : ℚ) ^ 2 * ((m : ℚ) + 1 - k) ^ 2
      = ((m : ℚ) + 1) ^ 2 * (m.choose k : ℚ) ^ 2 := by
    rw [← mul_pow, ← mul_pow, abs_b m k]
  simp only [Phi, Den]
  rw [div_mul_eq_mul_div, eq_div_iff (by simpa [Den] using Den_ne m), A_cast]
  linear_combination (-(((m + k).choose k : ℚ) ^ 2 * ((m : ℚ) + 1 - k) ^ 2)) * e1
    + (-(((m + k).choose k : ℚ) ^ 2 * ((m : ℚ) + 2) ^ 2)) * e2

/-- **Lemma 0(d)**: `Φ(n,k+1)(k+1)⁴ = Φ(n,k)(n+1−k)²(n+k)²` at `n = m+1`.  This is the identity
that removes every `0/0` from the certificate calculus. -/
theorem l0d (m k : ℕ) :
    Phi m (k + 1) * ((k : ℚ) + 1) ^ 4
      = Phi m k * (((m : ℚ) + 2 - k) ^ 2 * ((m : ℚ) + 1 + k) ^ 2) := by
  have g1 : ((m + 2).choose (k + 1) : ℚ) ^ 2 * ((k : ℚ) + 1) ^ 2
      = ((m + 2).choose k : ℚ) ^ 2 * ((m : ℚ) + 2 - k) ^ 2 := by
    rw [← mul_pow, ← mul_pow]
    have h := absorb2 (m + 2) k
    push_cast at h
    rw [show ((m + 2).choose k : ℚ) * ((m : ℚ) + 2 - k)
        = ((m + 2).choose k : ℚ) * ((m : ℚ) + 2 - k) from rfl]
    linear_combination (((m + 2).choose (k + 1) : ℚ) * ((k : ℚ) + 1)
      + ((m + 2).choose k : ℚ) * ((m : ℚ) + 2 - k)) * h
  have g2 : ((m + k + 1).choose (k + 1) : ℚ) ^ 2 * ((k : ℚ) + 1) ^ 2
      = ((m : ℚ) + k + 1) ^ 2 * ((m + k).choose k : ℚ) ^ 2 := by
    have h := absorb2 (m + k + 1) k
    push_cast at h
    have h' : ((m + k + 1).choose (k + 1) : ℚ) * ((k : ℚ) + 1)
        = ((m : ℚ) + k + 1) * ((m + k).choose k : ℚ) := by
      rw [h]
      linear_combination abs_c m k
    rw [← mul_pow, ← mul_pow, h']
  have key : (((m + 2).choose (k + 1) : ℚ) * ((m + k + 1).choose (k + 1) : ℚ)) ^ 2
        * ((k : ℚ) + 1) ^ 4
      = (((m + 2).choose k : ℚ) * ((m + k).choose k : ℚ)) ^ 2
        * (((m : ℚ) + 2 - k) ^ 2 * ((m : ℚ) + 1 + k) ^ 2) := by
    linear_combination (((m + k + 1).choose (k + 1) : ℚ) ^ 2 * ((k : ℚ) + 1) ^ 2) * g1
      + (((m + 2).choose k : ℚ) ^ 2 * ((m : ℚ) + 2 - k) ^ 2) * g2
  simp only [Phi]
  rw [show m + (k + 1) = m + k + 1 by omega, div_mul_eq_mul_div, div_mul_eq_mul_div, key]

/-! ## 2. The two certificates -/

/-- Apéry's polynomial `P(n) = 34n³ + 51n² + 27n + 5`. -/
def Ppol (n : ℚ) : ℚ := 34 * n ^ 3 + 51 * n ^ 2 + 27 * n + 5

/-- Zeilberger's certificate polynomial `T(n,k) = 4(2n+1)(2k²−3k−4n²−4n)` (CERT-1). -/
def Tpol (n k : ℚ) : ℚ := 4 * (2 * n + 1) * (2 * k ^ 2 - 3 * k - 4 * n ^ 2 - 4 * n)

/-- Gosper's certificate polynomial `U(n,k) = −4(k−1)(2n+1)(2n²+2n+1−k)` (CERT-2). -/
def Upol (n k : ℚ) : ℚ := -4 * (k - 1) * (2 * n + 1) * (2 * n ^ 2 + 2 * n + 1 - k)

/-- `G(n,k) = Φ(n,k) k⁴ T(n,k)`. -/
def Gfun (m k : ℕ) : ℚ := Phi m k * (k : ℚ) ^ 4 * Tpol ((m : ℚ) + 1) (k : ℚ)

/-- `G(n,k)/k³ = Φ(n,k) k T(n,k)`, defined without division so that `k = 0` is not special. -/
def Gdfun (m k : ℕ) : ℚ := Phi m k * (k : ℚ) * Tpol ((m : ℚ) + 1) (k : ℚ)

/-- `K(n,k) = Φ(n,k) k⁴ U(n,k)/(n²(n+1)²)`. -/
def Kfun (m k : ℕ) : ℚ := Phi m k * (k : ℚ) ^ 4 * Upol ((m : ℚ) + 1) (k : ℚ) / Den m

theorem Gfun_succ (m k : ℕ) :
    Gfun m (k + 1)
      = Phi m k * (((m : ℚ) + 2 - k) ^ 2 * ((m : ℚ) + 1 + k) ^ 2)
        * Tpol ((m : ℚ) + 1) ((k : ℚ) + 1) := by
  simp only [Gfun]
  push_cast
  rw [l0d]

theorem Kfun_succ (m k : ℕ) :
    Kfun m (k + 1)
      = Phi m k * (((m : ℚ) + 2 - k) ^ 2 * ((m : ℚ) + 1 + k) ^ 2)
        * Upol ((m : ℚ) + 1) ((k : ℚ) + 1) / Den m := by
  simp only [Kfun]
  push_cast
  rw [l0d]

theorem Gfun_eq_Gdfun (m k : ℕ) : Gfun m (k + 1) = Gdfun m (k + 1) * ((k : ℚ) + 1) ^ 3 := by
  simp only [Gfun, Gdfun]
  push_cast
  ring

/-- **Proposition B (CERT-1)** of `MINIMAL_FORM_PROOF.md` §2: the Apéry operator applied to the
summand `A` telescopes, `L[A(·,k)] = G(n,k+1) − G(n,k)`, for all `m, k ≥ 0`. -/
theorem propB (m k : ℕ) :
    ((m : ℚ) + 2) ^ 3 * (A (m + 2) k : ℚ) - Ppol ((m : ℚ) + 1) * (A (m + 1) k : ℚ)
        + ((m : ℚ) + 1) ^ 3 * (A m k : ℚ)
      = Gfun m (k + 1) - Gfun m k := by
  rw [l0a m k, l0b m k, l0c m k, Gfun_succ m k]
  simp only [Gfun, Ppol, Tpol]
  ring

/-- **Proposition C (CERT-2)** of `MINIMAL_FORM_PROOF.md` §4: the weight-correction term
`G(n,k)/k³ + 2A(n+1,k) − 2A(n−1,k)` telescopes, `= K(n,k+1) − K(n,k)`. -/
theorem propC (m k : ℕ) :
    Gdfun m k + 2 * (A (m + 2) k : ℚ) - 2 * (A m k : ℚ) = Kfun m (k + 1) - Kfun m k := by
  rw [l0b m k, l0c m k, Kfun_succ m k]
  simp only [Gdfun, Kfun]
  rw [div_sub_div_same, eq_div_iff (Den_ne m)]
  simp only [Den, Tpol, Upol]
  ring

/-! ## 3. The single telescope -/

/-- `H⁽³⁾_{y+1} = H⁽³⁾_y + 1/(y+1)³` — the only analytic input of the whole proof. -/
theorem Harm_succ (r y : ℕ) : Harm r (y + 1) = Harm r y + 1 / ((y : ℚ) + 1) ^ r := by
  simp only [Harm, K, Finset.sum_range_succ, triv]
  push_cast
  ring

theorem Harm_zero (r : ℕ) (hr : 0 < r) : Harm r 0 = 0 := K_zero triv hr

/-- The Apéry weight `w(n,k) = 2H⁽³⁾_n − H⁽³⁾_k` at `n = m+1`. -/
def Wt (m k : ℕ) : ℚ := 2 * Harm 3 (m + 1) - Harm 3 k

/-- The **single antidifference** `Ψ(m,k) = w(m+1,k)G(m,k) + K(m,k) + Gd(m,k)` that telescopes the
whole of `(L b_min)(m+1)`. -/
def Psi (m k : ℕ) : ℚ := Wt m k * Gfun m k + Kfun m k + Gdfun m k

theorem Psi_zero (m : ℕ) : Psi m 0 = 0 := by
  simp [Psi, Gfun, Gdfun, Kfun]

theorem Psi_top (m : ℕ) : Psi m (m + 3) = 0 := by
  have h : Phi m (m + 3) = 0 := by
    simp only [Phi, Nat.choose_eq_zero_of_lt (by omega : m + 2 < m + 3)]
    simp
  simp [Psi, Gfun, Gdfun, Kfun, h]

/-- Splitting off the `n`-dependence of the weight: the `k`-summand of `(L b_min)(m+1)` equals
`w(m+1,k)·L[A(·,k)] + 2A(m+2,k) − 2A(m,k)`.  This is where `H⁽³⁾_{n±1} − H⁽³⁾_n = ±1/(n±1)³` and
the leading coefficients `(n+1)³`, `n³` cancel. -/
theorem star_pre (m k : ℕ) :
    ((m : ℚ) + 2) ^ 3 * ((A (m + 2) k : ℚ) * (2 * Harm 3 (m + 2) - Harm 3 k))
      - Ppol ((m : ℚ) + 1) * ((A (m + 1) k : ℚ) * (2 * Harm 3 (m + 1) - Harm 3 k))
      + ((m : ℚ) + 1) ^ 3 * ((A m k : ℚ) * (2 * Harm 3 m - Harm 3 k))
    = Wt m k * (((m : ℚ) + 2) ^ 3 * (A (m + 2) k : ℚ)
        - Ppol ((m : ℚ) + 1) * (A (m + 1) k : ℚ) + ((m : ℚ) + 1) ^ 3 * (A m k : ℚ))
      + 2 * (A (m + 2) k : ℚ) - 2 * (A m k : ℚ) := by
  have hm1 : ((m : ℚ) + 1) ≠ 0 := by positivity
  have hm2 : ((m : ℚ) + 2) ≠ 0 := by positivity
  have h1 : Harm 3 m = Harm 3 (m + 1) - 1 / ((m : ℚ) + 1) ^ 3 := by
    rw [Harm_succ 3 m]; ring
  have h2 : Harm 3 (m + 2) = Harm 3 (m + 1) + 1 / ((m : ℚ) + 2) ^ 3 := by
    have h := Harm_succ 3 (m + 1)
    rw [show m + 1 + 1 = m + 2 by omega] at h
    push_cast at h
    rw [h, show ((m : ℚ) + 1 + 1) = (m : ℚ) + 2 by ring]
  simp only [Wt]
  rw [h1, h2]
  field_simp
  ring

/-- **The telescoping identity.**  The `k`-summand of `(L b_min)(m+1)` is `Ψ(m,k+1) − Ψ(m,k)`. -/
theorem star (m k : ℕ) :
    ((m : ℚ) + 2) ^ 3 * ((A (m + 2) k : ℚ) * (2 * Harm 3 (m + 2) - Harm 3 k))
      - Ppol ((m : ℚ) + 1) * ((A (m + 1) k : ℚ) * (2 * Harm 3 (m + 1) - Harm 3 k))
      + ((m : ℚ) + 1) ^ 3 * ((A m k : ℚ) * (2 * Harm 3 m - Harm 3 k))
    = Psi m (k + 1) - Psi m k := by
  have hk1 : ((k : ℚ) + 1) ≠ 0 := by positivity
  have hC := propC m k
  have hWG : Wt m k * Gfun m (k + 1)
      = Wt m (k + 1) * Gfun m (k + 1) + Gdfun m (k + 1) := by
    have hk : Harm 3 (k + 1) = Harm 3 k + 1 / ((k : ℚ) + 1) ^ 3 := Harm_succ 3 k
    simp only [Wt]
    rw [hk, Gfun_eq_Gdfun]
    field_simp
    ring
  rw [star_pre, propB]
  simp only [Psi]
  linear_combination hWG + hC

/-! ## 4. `b_min` satisfies Apéry's recurrence -/

theorem bMin_sum_range {n N : ℕ} (h : n + 1 ≤ N) :
    bMin n = ∑ k ∈ range N, (A n k : ℚ) * (2 * Harm 3 n - Harm 3 k) := by
  refine Finset.sum_subset
    (fun k hk => Finset.mem_range.2 (lt_of_lt_of_le (Finset.mem_range.1 hk) h)) ?_
  intro k _ hk
  simp only [Finset.mem_range, not_lt] at hk
  rw [A_eq_zero_of_lt (by omega : n < k)]
  simp

/-- **Theorem 1 of `MINIMAL_FORM_PROOF.md`**: the minimal form is annihilated by the Apéry
operator, `(n+1)³ b_{n+1} − P(n) b_n + n³ b_{n−1} = 0` for all `n = m+1 ≥ 1`. -/
theorem bMin_rec (m : ℕ) :
    ((m : ℚ) + 2) ^ 3 * bMin (m + 2) - Ppol ((m : ℚ) + 1) * bMin (m + 1)
      + ((m : ℚ) + 1) ^ 3 * bMin m = 0 := by
  rw [bMin_sum_range (n := m + 2) (N := m + 3) (by omega),
    bMin_sum_range (n := m + 1) (N := m + 3) (by omega),
    bMin_sum_range (n := m) (N := m + 3) (by omega),
    Finset.mul_sum, Finset.mul_sum, Finset.mul_sum,
    ← Finset.sum_sub_distrib, ← Finset.sum_add_distrib]
  rw [Finset.sum_congr rfl (fun k _ => star m k)]
  rw [Finset.sum_range_sub (fun k => Psi m k) (m + 3), Psi_top, Psi_zero]
  ring

/-! ## 5. Apéry's companion sequence, and the closed form -/

/-- **Apéry's second solution `b_n`**, *defined* by his order-2 recurrence

    (n+1)³ b_{n+1} = (34n³+51n²+27n+5) b_n − n³ b_{n−1},     b₀ = 0,  b₁ = 6.

The leading coefficient never vanishes, so this determines `b_n ∈ ℚ` uniquely. -/
def bApery : ℕ → ℚ
  | 0 => 0
  | 1 => 6
  | (n + 2) => (Ppol ((n : ℚ) + 1) * bApery (n + 1) - ((n : ℚ) + 1) ^ 3 * bApery n)
      / ((n : ℚ) + 2) ^ 3

@[simp] theorem bApery_zero : bApery 0 = 0 := rfl
@[simp] theorem bApery_one : bApery 1 = 6 := rfl

theorem bApery_rec (n : ℕ) :
    ((n : ℚ) + 2) ^ 3 * bApery (n + 2)
      = Ppol ((n : ℚ) + 1) * bApery (n + 1) - ((n : ℚ) + 1) ^ 3 * bApery n := by
  have hne : ((n : ℚ) + 2) ^ 3 ≠ 0 := by positivity
  rw [show bApery (n + 2)
      = (Ppol ((n : ℚ) + 1) * bApery (n + 1) - ((n : ℚ) + 1) ^ 3 * bApery n)
        / ((n : ℚ) + 2) ^ 3 from rfl]
  field_simp

theorem bMin_zero : bMin 0 = 0 := by
  simp [bMin, Harm, K, A, triv]

theorem bMin_one : bMin 1 = 6 := by
  norm_num [bMin, Harm, K, A, triv, Finset.sum_range_succ]

/-- **MAIN THEOREM.**  The minimal harmonic sum computes Apéry's classical companion `b_n`:

    Σ_{k=0}^n C(n,k)² C(n+k,k)² (2 H⁽³⁾_n − H⁽³⁾_k)  =  b_n,

where `b_n` is defined by Apéry's recurrence with `b₀ = 0`, `b₁ = 6`. -/
theorem bMin_eq_bApery (n : ℕ) : bMin n = bApery n := by
  have key : ∀ n : ℕ, bMin n = bApery n ∧ bMin (n + 1) = bApery (n + 1) := by
    intro n
    induction n with
    | zero => exact ⟨by simp [bMin_zero], by simp [bMin_one]⟩
    | succ n ih =>
      refine ⟨ih.2, ?_⟩
      obtain ⟨h0, h1⟩ := ih
      have hrec := bMin_rec n
      have hA := bApery_rec n
      have hne : ((n : ℚ) + 2) ^ 3 ≠ 0 := by positivity
      have : ((n : ℚ) + 2) ^ 3 * bMin (n + 2) = ((n : ℚ) + 2) ^ 3 * bApery (n + 2) := by
        rw [hA, ← h0, ← h1]
        linear_combination hrec
      exact mul_left_cancel₀ hne this
  exact (key n).1

/-- `H⁽ʳ⁾_y = Σ_{j=1}^{y} 1/jʳ` — `Harm` really is the truncated zeta value. -/
theorem Harm_eq (r y : ℕ) (hr : 0 < r) :
    Harm r y = ∑ j ∈ Finset.Icc 1 y, (1 : ℚ) / (j : ℚ) ^ r := by
  induction y with
  | zero => simp [Harm_zero r hr]
  | succ y ih =>
    rw [Harm_succ, ih, Finset.sum_Icc_succ_top (by omega : 1 ≤ y + 1)]
    push_cast
    ring

/-- **MAIN THEOREM, fully written out.**  For every `n ≥ 0`,

    Σ_{k=0}^{n} C(n,k)² C(n+k,k)² · ( 2·Σ_{j=1}^{n} 1/j³ − Σ_{j=1}^{k} 1/j³ )  =  b_n,

`b_n` being Apéry's companion sequence for `ζ(3)` (`b₀ = 0`, `b₁ = 6`,
`(n+1)³b_{n+1} = (34n³+51n²+27n+5)b_n − n³b_{n−1}`). -/
theorem apery_b_harmonic_closed_form (n : ℕ) :
    ∑ k ∈ range (n + 1),
        ((n.choose k : ℚ) ^ 2 * (((n + k).choose k : ℚ)) ^ 2)
          * (2 * (∑ j ∈ Finset.Icc 1 n, (1 : ℚ) / (j : ℚ) ^ 3)
              - ∑ j ∈ Finset.Icc 1 k, (1 : ℚ) / (j : ℚ) ^ 3)
      = bApery n := by
  rw [← bMin_eq_bApery, bMin]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [A_cast, ← Harm_eq 3 n (by norm_num), ← Harm_eq 3 k (by norm_num)]

/-! ## 6. Consequence: the `b`-row Lucas congruence, restated for the classical `b_n` -/

/-- **The `b`-row Lucas congruence for Apéry's classical companion sequence.**

    p³ · b_{a·p+r}  ≡  b_a · a_r    (mod p)           (a < p, r < p, p prime),

where `b_n` is now the sequence *defined by Apéry's recurrence* (`bApery`) and `a_n` is
`Σ_k C(n,k)²C(n+k,k)²` (`apery`).  This is `Instances.bMin_lucas` transported along
`bMin_eq_bApery`; it is the form in which the theorem is about a classical object rather than
about an explicit harmonic sum. -/
theorem bApery_lucas {p : ℕ} [Fact p.Prime] {a r : ℕ} (ha : a < p) (hr : r < p) :
    PCong p ((p : ℚ) ^ 3 * bApery (a * p + r)) (bApery a * (apery r : ℚ)) := by
  rw [← bMin_eq_bApery, ← bMin_eq_bApery]
  exact bMin_lucas ha hr

section Sanity

/-- Kernel-checked: the recurrence reproduces the classical values `b₂ = 351/4`,
`b₃ = 62531/36` (`work/MINIMAL_FORM_PROOF.md` §1). -/
example : bApery 2 = 351 / 4 := by norm_num [bApery, Ppol]
example : bApery 3 = 62531 / 36 := by norm_num [bApery, Ppol]

/-- Kernel-checked: the explicit sum agrees with the recurrence at `n = 2`. -/
example : bMin 2 = 351 / 4 := by
  have h : Nat.choose 4 2 = 6 := rfl
  norm_num [bMin, Harm, K, A, triv, Finset.sum_range_succ, h]

-- `b_n = 0, 6, 351/4, 62531/36, 11424695/288, 35441662103/36000, 20637706271/800, …`
-- (the values quoted in `work/MINIMAL_FORM_PROOF.md` §1 and `work/LBW_GENERAL.md` §T3),
-- computed independently from the recurrence and from the sum.
#eval (List.range 7).map bApery
#eval (List.range 7).map bMin

end Sanity

end ZetaLucas
