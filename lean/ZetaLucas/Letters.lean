/-
**S2 of task P5c** — the harmonic-letter calculus and **Lemma K**, the Frobenius descent of a
twisted harmonic letter (`work/LBW_GENERAL.md` §T4).

For a completely multiplicative `χ : ℕ → ℤ` (a Dirichlet character; `χ ≡ 1` allowed — we
deliberately do *not* use Mathlib's `DirichletCharacter`, which would force a modulus and a
`ZMod`-valued target) and `r ≥ 1` set

    K χ r y = Σ_{m = 1}^{y} χ(m) / m^r     (as a rational).

**Lemma K.**   `p^r · K χ r y  ≡  χ(p) · K χ r ⌊y/p⌋   (mod p)`.

The `p`-divisible layer `m = jp` contributes `χ(p)p^{-r}χ(j)j^{-r}` and reproduces the right-hand
side *exactly*; the layer `p ∤ m` is `p`-integral and is annihilated by the `p^r` twist.
This single line is the entire source of the `χ(p)` in `(LB_w^χ)`.

A **letter** is a triple `(χ, r, x)` with `x : ℕ → ℕ → ℕ` the argument form; a **monomial** is a
`List Letter`, and `monDeg` / `monChi` are its total weight and its character value at `p`.
`mon_descent` is Corollary K2: `p^{monDeg M} · M(n,k) ≡ monChi M p · M(⌊·/p⌋)`.
-/
import ZetaLucas.PadicBridge

open Finset

set_option linter.unusedSectionVars false

namespace ZetaLucas

/-- The truncated `χ`-twisted zeta value `K^{(r)}_χ(y) = Σ_{m=1}^{y} χ(m)/m^r`.

The sum is written over `range (y+1)`; the `m = 0` term is `χ(0)/0^r = 0` whenever `r ≥ 1`
(division by zero is zero in `ℚ`), so no `Finset.Icc` bookkeeping is ever needed. -/
def K (χ : ℕ → ℤ) (r y : ℕ) : ℚ := ∑ m ∈ range (y + 1), (χ m : ℚ) / (m : ℚ) ^ r

@[simp] theorem K_zero (χ : ℕ → ℤ) {r : ℕ} (hr : 0 < r) : K χ r 0 = 0 := by
  simp [K, zero_pow hr.ne']

variable {p : ℕ} [Fact p.Prime]

theorem padicNorm_pow (q : ℚ) (n : ℕ) : padicNorm p (q ^ n) = padicNorm p q ^ n := by
  induction n with
  | zero => simp
  | succ n ih => rw [pow_succ, padicNorm.mul, ih, pow_succ]

/-- A term `χ(m)/m^r` with `p ∤ m` is `p`-integral. -/
theorem K_term_pInt {χ : ℕ → ℤ} {r m : ℕ} (hm : ¬ p ∣ m) :
    PInt p ((χ m : ℚ) / (m : ℚ) ^ r) := by
  refine PInt.div (PInt.intCast _) ?_
  rw [padicNorm_pow, (padicNorm.nat_eq_one_iff m).2 hm, one_pow]

/-- **`K` is `p`-integral in the digit range.**  All denominators `m ≤ y < p` are `p`-units. -/
theorem K_pInt {χ : ℕ → ℤ} {r y : ℕ} (hr : 0 < r) (hy : y < p) : PInt p (K χ r y) := by
  refine PInt.sum fun m hm => ?_
  have hmy : m ≤ y := Nat.lt_succ_iff.1 (Finset.mem_range.1 hm)
  rcases Nat.eq_zero_or_pos m with rfl | hm0
  · simp [zero_pow hr.ne', PInt.zero]
  · exact K_term_pInt (Nat.not_dvd_of_pos_of_lt hm0 (by omega))

/-- Reindexing the `p`-divisible layer of `range (y+1)` as `{j·p : j ≤ ⌊y/p⌋}`. -/
theorem sum_filter_dvd (f : ℕ → ℚ) (hp : 0 < p) (y : ℕ) :
    ∑ m ∈ (range (y + 1)).filter (fun m => p ∣ m), f m
      = ∑ j ∈ range (y / p + 1), f (j * p) := by
  classical
  refine Finset.sum_nbij' (fun m => m / p) (fun j => j * p) ?_ ?_ ?_ ?_ ?_
  · intro m hm
    simp only [Finset.mem_filter, Finset.mem_range] at hm ⊢
    exact Nat.lt_succ_of_le (Nat.div_le_div_right (Nat.lt_succ_iff.1 hm.1))
  · intro j hj
    simp only [Finset.mem_range, Finset.mem_filter] at hj ⊢
    refine ⟨?_, dvd_mul_left p j⟩
    have h1 : j ≤ y / p := Nat.lt_succ_iff.1 hj
    have h2 : j * p ≤ y / p * p := Nat.mul_le_mul_right p h1
    have h3 : y / p * p ≤ y := Nat.div_mul_le_self y p
    omega
  · intro m hm
    simp only [Finset.mem_filter] at hm
    exact Nat.div_mul_cancel hm.2
  · intro j _
    exact Nat.mul_div_cancel j hp
  · intro m hm
    simp only [Finset.mem_filter] at hm
    rw [Nat.div_mul_cancel hm.2]

/-- **Lemma K — the Frobenius descent of a harmonic letter.**

    p^r · K χ r y  ≡  χ(p) · K χ r ⌊y/p⌋   (mod p).

`χ` is only required to be multiplicative; no modulus, no primitivity, no `DirichletCharacter`. -/
theorem K_descent {χ : ℕ → ℤ} (hχ : ∀ m n, χ (m * n) = χ m * χ n) {r : ℕ} (hr : 0 < r) (y : ℕ) :
    PCong p ((p : ℚ) ^ r * K χ r y) ((χ p : ℚ) * K χ r (y / p)) := by
  classical
  have hp0 : 0 < p := (Fact.out (p := p.Prime)).pos
  have hpQ : (p : ℚ) ≠ 0 := Nat.cast_ne_zero.2 hp0.ne'
  set f : ℕ → ℚ := fun m => (χ m : ℚ) / (m : ℚ) ^ r with hfdef
  -- Split `K` at `p ∣ m`.
  have hsplit : K χ r y
      = (∑ m ∈ (range (y + 1)).filter (fun m => p ∣ m), f m)
        + (∑ m ∈ (range (y + 1)).filter (fun m => ¬ p ∣ m), f m) :=
    (Finset.sum_filter_add_sum_filter_not _ _ _).symm
  -- The `p`-divisible layer reproduces `χ(p)·K(⌊y/p⌋)` exactly, after the `p^r` twist.
  have hkey : (p : ℚ) ^ r * (∑ m ∈ (range (y + 1)).filter (fun m => p ∣ m), f m)
      = (χ p : ℚ) * K χ r (y / p) := by
    rw [sum_filter_dvd f hp0 y, K, Finset.mul_sum, Finset.mul_sum]
    refine Finset.sum_congr rfl fun j _ => ?_
    rcases Nat.eq_zero_or_pos j with rfl | hj0
    · simp [hfdef, zero_pow hr.ne']
    · have hjQ : (j : ℚ) ≠ 0 := Nat.cast_ne_zero.2 hj0.ne'
      simp only [hfdef, hχ j p]
      push_cast
      field_simp
      ring
  -- The remaining layer is `p`-integral, hence killed by `p^r`.
  have hrest : PInt p (∑ m ∈ (range (y + 1)).filter (fun m => ¬ p ∣ m), f m) := by
    refine PInt.sum fun m hm => ?_
    simp only [Finset.mem_filter] at hm
    exact K_term_pInt hm.2
  show PDvd p _
  have hdiff : (p : ℚ) ^ r * K χ r y - (χ p : ℚ) * K χ r (y / p)
      = (p : ℚ) ^ r * (∑ m ∈ (range (y + 1)).filter (fun m => ¬ p ∣ m), f m) := by
    rw [hsplit, mul_add, hkey]; ring
  rw [hdiff]
  exact pDvd_p_pow_mul hr hrest

/-! ### Letters and monomials -/

/-- A **harmonic letter**: a completely multiplicative `χ`, a weight `deg ≥ 1`, and an argument
form `arg : ℕ → ℕ → ℕ` (a linear form in `(n,k)` in every application).  The multiplicativity
proof and `deg > 0` are bundled so that the statement of Theorem LB carries no side hypotheses
about them. -/
structure Letter where
  /-- The character (completely multiplicative arithmetic function; `χ ≡ 1` is allowed). -/
  chi : ℕ → ℤ
  /-- Complete multiplicativity. -/
  chi_mul : ∀ m n, chi (m * n) = chi m * chi n
  /-- The weight `r` of the letter `K^{(r)}`. -/
  deg : ℕ
  /-- Weights are positive. -/
  deg_pos : 0 < deg
  /-- The argument form `x(n,k)`. -/
  arg : ℕ → ℕ → ℕ

namespace Letter

/-- The value `K^{(r)}_χ(x(n,k))` of a letter. -/
def val (ℓ : Letter) (n k : ℕ) : ℚ := K ℓ.chi ℓ.deg (ℓ.arg n k)

/-- The descended value `K^{(r)}_χ(⌊x(n,k)/p⌋)` of a letter. -/
def valDiv (ℓ : Letter) (p n k : ℕ) : ℚ := K ℓ.chi ℓ.deg (ℓ.arg n k / p)

end Letter

/-- The value of a monomial (a list of letters) at `(n,k)`. -/
def monVal (M : List Letter) (n k : ℕ) : ℚ := (M.map (fun ℓ => ℓ.val n k)).prod

/-- The descended value of a monomial at `(n,k)`. -/
def monValDiv (p : ℕ) (M : List Letter) (n k : ℕ) : ℚ :=
  (M.map (fun ℓ => ℓ.valDiv p n k)).prod

/-- The total weight `Σ_t r_t` of a monomial. -/
def monDeg (M : List Letter) : ℕ := (M.map Letter.deg).sum

/-- The character value `∏_t χ_t(p)` of a monomial — the source of the `χ(p)^e` twist. -/
def monChi (M : List Letter) (p : ℕ) : ℤ := (M.map (fun ℓ => ℓ.chi p)).prod

@[simp] theorem monVal_nil (n k : ℕ) : monVal [] n k = 1 := rfl
@[simp] theorem monValDiv_nil (p n k : ℕ) : monValDiv p [] n k = 1 := rfl
@[simp] theorem monDeg_nil : monDeg [] = 0 := rfl
@[simp] theorem monChi_nil (p : ℕ) : monChi [] p = 1 := rfl

@[simp] theorem monVal_cons (ℓ : Letter) (M : List Letter) (n k : ℕ) :
    monVal (ℓ :: M) n k = ℓ.val n k * monVal M n k := rfl
@[simp] theorem monValDiv_cons (ℓ : Letter) (M : List Letter) (p n k : ℕ) :
    monValDiv p (ℓ :: M) n k = ℓ.valDiv p n k * monValDiv p M n k := rfl
@[simp] theorem monDeg_cons (ℓ : Letter) (M : List Letter) :
    monDeg (ℓ :: M) = ℓ.deg + monDeg M := rfl
@[simp] theorem monChi_cons (ℓ : Letter) (M : List Letter) (p : ℕ) :
    monChi (ℓ :: M) p = ℓ.chi p * monChi M p := rfl

/-- A descended monomial value is `p`-integral once every descended argument is `< p`. -/
theorem monValDiv_pInt {M : List Letter} {n k : ℕ}
    (h : ∀ ℓ ∈ M, ℓ.arg n k / p < p) : PInt p (monValDiv p M n k) := by
  induction M with
  | nil => simpa using PInt.one (p := p)
  | cons ℓ M ih =>
    rw [monValDiv_cons]
    exact PInt.mul (K_pInt ℓ.deg_pos (h ℓ (by simp)))
      (ih fun ℓ' hℓ' => h ℓ' (by simp [hℓ']))

/-- `p^{deg ℓ} · (value of a letter)` is `p`-integral. -/
theorem letter_pInt {ℓ : Letter} {n k : ℕ} (h : ℓ.arg n k / p < p) :
    PInt p ((p : ℚ) ^ ℓ.deg * ℓ.val n k) :=
  PCong.pInt (K_descent ℓ.chi_mul ℓ.deg_pos _)
    (PInt.mul (PInt.intCast _) (K_pInt ℓ.deg_pos h))

/-- **Corollary K2 — descent of a monomial.**

    p^{Σ r_t} · ∏_t K^{(r_t)}_{χ_t}(x_t(n,k))
      ≡ (∏_t χ_t(p)) · ∏_t K^{(r_t)}_{χ_t}(⌊x_t(n,k)/p⌋)   (mod p).

Every cross term in the expansion carries a factor `p`, and every factor is `p`-integral. -/
theorem mon_descent {M : List Letter} {n k : ℕ}
    (h : ∀ ℓ ∈ M, ℓ.arg n k / p < p) :
    PCong p ((p : ℚ) ^ monDeg M * monVal M n k)
      ((monChi M p : ℚ) * monValDiv p M n k) := by
  induction M with
  | nil => simp; exact PCong.refl 1
  | cons ℓ M ih =>
    have hℓ : ℓ.arg n k / p < p := h ℓ (by simp)
    have hM : ∀ ℓ' ∈ M, ℓ'.arg n k / p < p := fun ℓ' hℓ' => h ℓ' (by simp [hℓ'])
    have e1 : (p : ℚ) ^ monDeg (ℓ :: M) * monVal (ℓ :: M) n k
        = ((p : ℚ) ^ ℓ.deg * ℓ.val n k) * ((p : ℚ) ^ monDeg M * monVal M n k) := by
      rw [monDeg_cons, monVal_cons, pow_add]; ring
    have e2 : ((monChi (ℓ :: M) p : ℚ)) * monValDiv p (ℓ :: M) n k
        = ((ℓ.chi p : ℚ) * ℓ.valDiv p n k) * ((monChi M p : ℚ) * monValDiv p M n k) := by
      rw [monChi_cons, monValDiv_cons]; push_cast; ring
    rw [e1, e2]
    exact PCong.mul (letter_pInt hℓ)
      (PInt.mul (PInt.intCast _) (monValDiv_pInt hM))
      (K_descent ℓ.chi_mul ℓ.deg_pos _) (ih hM)

/-- `p^{monDeg M} · (monomial value)` is `p`-integral — the *tameness* consequence that makes
the vanishing layer of Theorem LB die termwise. -/
theorem mon_pInt {M : List Letter} {n k : ℕ} (h : ∀ ℓ ∈ M, ℓ.arg n k / p < p) :
    PInt p ((p : ℚ) ^ monDeg M * monVal M n k) :=
  PCong.pInt (mon_descent h) (PInt.mul (PInt.intCast _) (monValDiv_pInt h))

/-- The `p`-integral monomial value at small arguments. -/
theorem monVal_pInt {M : List Letter} {n k : ℕ} (h : ∀ ℓ ∈ M, ℓ.arg n k < p) :
    PInt p (monVal M n k) := by
  induction M with
  | nil => simpa using PInt.one (p := p)
  | cons ℓ M ih =>
    rw [monVal_cons]
    exact PInt.mul (K_pInt ℓ.deg_pos (h ℓ (by simp)))
      (ih fun ℓ' hℓ' => h ℓ' (by simp [hℓ']))

end ZetaLucas
