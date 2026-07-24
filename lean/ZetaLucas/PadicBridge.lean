/-
**S1(a) of task P5c** — a minimal API for `p`-integral rationals and for congruences
`mod p` inside the local ring `ℤ_(p) ⊆ ℚ`, plus the bridge to `ZMod p` for integers.

Design note (see `work/LEAN_LUCAS_STATUS.md` §S4.1 for the analysis this implements):
we work with `padicNorm` on `ℚ`, **not** with `PadicInt`/`Padic`.  `padicNorm.mul` and
`padicNorm.div` are unconditional (no `≠ 0` side goals), `padicNorm.sum_lt'` is zero-safe
and needs no `Nonempty`, and no rational ever has to be transported along `ℚ → ℚ_p`.

Three predicates:
* `PInt p q`  : `q ∈ ℤ_(p)`            (`padicNorm p q ≤ 1`)
* `PDvd p q`  : `q ∈ p·ℤ_(p)`          (`padicNorm p q < 1`)
* `PCong p x y` : `x ≡ y (mod p)` in `ℤ_(p)`, i.e. `PDvd p (x - y)`.

`PCong` is an equivalence relation, additive, closed under `Finset.sum`, and multiplicative
*given* `p`-integrality of the surviving factors (`PCong.mul`).  `PCong.of_zmod` imports every
`ZMod p` congruence between integers — in particular all of `ZetaLucas/Core.lean`.
-/
import Mathlib

set_option linter.unusedSectionVars false

open Finset

namespace ZetaLucas

/-- `q : ℚ` is `p`-integral: it lies in the local ring `ℤ_(p) ⊆ ℚ`. -/
def PInt (p : ℕ) (q : ℚ) : Prop := padicNorm p q ≤ 1

/-- `q : ℚ` lies in the maximal ideal `p·ℤ_(p)`; equivalently `q ≡ 0 (mod p)`. -/
def PDvd (p : ℕ) (q : ℚ) : Prop := padicNorm p q < 1

/-- `x ≡ y (mod p)` as an equation in `ℤ_(p)/p ≅ ZMod p`. -/
def PCong (p : ℕ) (x y : ℚ) : Prop := PDvd p (x - y)

variable {p : ℕ} [Fact p.Prime]

/-! ### `PInt` -/

theorem PInt.intCast (z : ℤ) : PInt p (z : ℚ) := padicNorm.of_int z

theorem PInt.natCast (n : ℕ) : PInt p (n : ℚ) := padicNorm.of_nat n

theorem PInt.zero : PInt p 0 := by simp [PInt]

theorem PInt.one : PInt p 1 := by simp [PInt]

theorem PInt.mul {x y : ℚ} (hx : PInt p x) (hy : PInt p y) : PInt p (x * y) := by
  show padicNorm p (x * y) ≤ 1
  rw [padicNorm.mul]
  exact mul_le_one₀ hx (padicNorm.nonneg _) hy

theorem PInt.neg {x : ℚ} (hx : PInt p x) : PInt p (-x) := by
  simpa [PInt, padicNorm.neg] using hx

theorem PInt.add {x y : ℚ} (hx : PInt p x) (hy : PInt p y) : PInt p (x + y) :=
  le_trans padicNorm.nonarchimedean (max_le hx hy)

theorem PInt.sub {x y : ℚ} (hx : PInt p x) (hy : PInt p y) : PInt p (x - y) := by
  rw [sub_eq_add_neg]; exact PInt.add hx (PInt.neg hy)

theorem PInt.pow {x : ℚ} (hx : PInt p x) (n : ℕ) : PInt p (x ^ n) := by
  induction n with
  | zero => simpa using PInt.one (p := p)
  | succ n ih => rw [pow_succ]; exact PInt.mul ih hx

theorem PInt.sum {ι : Type*} {s : Finset ι} {f : ι → ℚ} (h : ∀ i ∈ s, PInt p (f i)) :
    PInt p (∑ i ∈ s, f i) :=
  padicNorm.sum_le' h zero_le_one

/-- Division by a `p`-unit preserves `p`-integrality. -/
theorem PInt.div {x y : ℚ} (hx : PInt p x) (hy : padicNorm p y = 1) : PInt p (x / y) := by
  show padicNorm p (x / y) ≤ 1
  rw [padicNorm.div, hy, div_one]; exact hx

/-- A natural number `0 < m < p` is a `p`-unit. -/
theorem padicNorm_natCast_eq_one {m : ℕ} (h0 : 0 < m) (h : m < p) : padicNorm p (m : ℚ) = 1 :=
  (padicNorm.nat_eq_one_iff m).2 (Nat.not_dvd_of_pos_of_lt h0 h)

/-- An integer not divisible by `p` is a `p`-unit. -/
theorem padicNorm_intCast_eq_one {z : ℤ} (h : ¬ (p : ℤ) ∣ z) : padicNorm p (z : ℚ) = 1 :=
  (padicNorm.int_eq_one_iff z).2 h

/-- A rational with `p`-unit denominator is `p`-integral.  This is how the coefficients
`1/4`, `3/4`, `1/5`, … of the harmonic weights are certified. -/
theorem PInt.intCast_div {a b : ℤ} (hb : ¬ (p : ℤ) ∣ b) : PInt p ((a : ℚ) / (b : ℚ)) :=
  PInt.div (PInt.intCast a) (padicNorm_intCast_eq_one hb)

/-! ### `PDvd` -/

theorem PDvd.toPInt {x : ℚ} (h : PDvd p x) : PInt p x := le_of_lt h

theorem PDvd.zero : PDvd p 0 := by simp [PDvd]

theorem PDvd.neg {x : ℚ} (h : PDvd p x) : PDvd p (-x) := by
  simpa [PDvd, padicNorm.neg] using h

theorem PDvd.add {x y : ℚ} (hx : PDvd p x) (hy : PDvd p y) : PDvd p (x + y) :=
  lt_of_le_of_lt padicNorm.nonarchimedean (max_lt hx hy)

/-- Multiplying a `p`-divisible rational by a `p`-integral one stays `p`-divisible. -/
theorem PDvd.mul_left {c x : ℚ} (hc : PInt p c) (hx : PDvd p x) : PDvd p (c * x) := by
  show padicNorm p (c * x) < 1
  rw [padicNorm.mul]
  calc padicNorm p c * padicNorm p x
      ≤ 1 * padicNorm p x := mul_le_mul_of_nonneg_right hc (padicNorm.nonneg _)
    _ = padicNorm p x := one_mul _
    _ < 1 := hx

theorem PDvd.mul_right {x c : ℚ} (hc : PInt p c) (hx : PDvd p x) : PDvd p (x * c) := by
  rw [mul_comm]; exact PDvd.mul_left hc hx

theorem PDvd.sum {ι : Type*} {s : Finset ι} {f : ι → ℚ} (h : ∀ i ∈ s, PDvd p (f i)) :
    PDvd p (∑ i ∈ s, f i) :=
  padicNorm.sum_lt' h zero_lt_one

/-- `p^r · (p-integral)` is `p`-integral. -/
theorem pInt_p_pow_mul {r : ℕ} {x : ℚ} (hx : PInt p x) : PInt p ((p : ℚ) ^ r * x) := by
  refine PInt.mul (PInt.pow ?_ r) hx
  simpa using PInt.natCast (p := p) p

/-- `p^r · (p-integral)` is divisible by `p` as soon as `r ≥ 1`.  This is the workhorse
behind Lemma K: the non-`p`-divisible layer of a harmonic letter is killed by the `p^r` twist. -/
theorem pDvd_p_pow_mul {r : ℕ} (hr : 0 < r) {x : ℚ} (hx : PInt p x) :
    PDvd p ((p : ℚ) ^ r * x) := by
  obtain ⟨r, rfl⟩ : ∃ r', r = r' + 1 := ⟨r - 1, by omega⟩
  have hpn : padicNorm p ((p : ℚ)) = (p : ℚ)⁻¹ :=
    padicNorm.padicNorm_p (Fact.out (p := p.Prime)).one_lt
  have hp1 : (1 : ℚ) < (p : ℚ) := by exact_mod_cast (Fact.out (p := p.Prime)).one_lt
  have hlt : (p : ℚ)⁻¹ < 1 := by rw [inv_lt_one₀ (by linarith)]; exact hp1
  have hrest : PInt p ((p : ℚ) ^ r * x) := pInt_p_pow_mul hx
  have e : (p : ℚ) ^ (r + 1) * x = (p : ℚ) * ((p : ℚ) ^ r * x) := by ring
  show padicNorm p ((p : ℚ) ^ (r + 1) * x) < 1
  rw [e, padicNorm.mul, hpn]
  calc (p : ℚ)⁻¹ * padicNorm p ((p : ℚ) ^ r * x)
      ≤ (p : ℚ)⁻¹ * 1 := mul_le_mul_of_nonneg_left hrest (by positivity)
    _ = (p : ℚ)⁻¹ := mul_one _
    _ < 1 := hlt

/-! ### `PCong` -/

@[refl] theorem PCong.refl (x : ℚ) : PCong p x x := by
  show PDvd p (x - x); simpa [sub_self] using PDvd.zero (p := p)

theorem PCong.symm {x y : ℚ} (h : PCong p x y) : PCong p y x := by
  have h' := PDvd.neg h
  show PDvd p (y - x)
  rwa [neg_sub] at h'

theorem PCong.trans {x y z : ℚ} (h₁ : PCong p x y) (h₂ : PCong p y z) : PCong p x z := by
  have h := PDvd.add h₁ h₂
  show PDvd p (x - z)
  rwa [sub_add_sub_cancel] at h

theorem PCong.add {x x' y y' : ℚ} (h : PCong p x x') (h' : PCong p y y') :
    PCong p (x + y) (x' + y') := by
  have hh := PDvd.add h h'
  show PDvd p (x + y - (x' + y'))
  rwa [show x + y - (x' + y') = (x - x') + (y - y') by ring]

/-- Transport `p`-integrality along a congruence. -/
theorem PCong.pInt {x y : ℚ} (h : PCong p x y) (hy : PInt p y) : PInt p x := by
  rw [show x = (x - y) + y by ring]
  exact PInt.add (PDvd.toPInt h) hy

/-- `x ≡ 0` is literally `PDvd`. -/
theorem PCong.zero_iff {x : ℚ} : PCong p x 0 ↔ PDvd p x := by
  unfold PCong; rw [sub_zero]

theorem PDvd.toCong {x : ℚ} (h : PDvd p x) : PCong p x 0 := PCong.zero_iff.2 h

/-- Two `p`-divisible rationals are congruent mod `p`.  (Used for the vanishing layer of
Theorem LB, where both sides are `≡ 0`.) -/
theorem PCong.of_dvd_dvd {x y : ℚ} (hx : PDvd p x) (hy : PDvd p y) : PCong p x y := by
  show PDvd p (x - y)
  rw [sub_eq_add_neg]
  exact PDvd.add hx (PDvd.neg hy)

/-- Scaling a congruence by a `p`-integral constant. -/
theorem PCong.const_mul {c x y : ℚ} (hc : PInt p c) (h : PCong p x y) :
    PCong p (c * x) (c * y) := by
  have hh := PDvd.mul_left hc h
  show PDvd p (c * x - c * y)
  rwa [← mul_sub]

/-- **Multiplicativity of congruences.**  Needs `p`-integrality of one factor on each side:
`x·y − x'·y' = x·(y − y') + (x − x')·y'`. -/
theorem PCong.mul {x x' y y' : ℚ} (hx : PInt p x) (hy' : PInt p y')
    (h : PCong p x x') (h' : PCong p y y') : PCong p (x * y) (x' * y') := by
  show PDvd p (x * y - x' * y')
  rw [show x * y - x' * y' = x * (y - y') + (x - x') * y' by ring]
  exact PDvd.add (PDvd.mul_left hx h') (PDvd.mul_right hy' h)

theorem PCong.sum {ι : Type*} {s : Finset ι} {f g : ι → ℚ}
    (h : ∀ i ∈ s, PCong p (f i) (g i)) : PCong p (∑ i ∈ s, f i) (∑ i ∈ s, g i) := by
  show PDvd p (_ - _)
  rw [← Finset.sum_sub_distrib]
  exact PDvd.sum h

/-! ### Bridge to `ZMod p` -/

/-- **The bridge.**  Every congruence of integers in `ZMod p` — in particular every result of
`ZetaLucas/Core.lean`, `Apery.lean`, `BrownZudilin.lean` — becomes a `PCong` in `ℚ`. -/
theorem PCong.of_zmod {z z' : ℤ} (h : (z : ZMod p) = (z' : ZMod p)) :
    PCong p (z : ℚ) (z' : ℚ) := by
  have hmod : z ≡ z' [ZMOD (p : ℤ)] := (ZMod.intCast_eq_intCast_iff z z' p).1 h
  have hd : (p : ℤ) ∣ (z - z') := Int.ModEq.dvd hmod.symm
  show padicNorm p ((z : ℚ) - (z' : ℚ)) < 1
  rw [show ((z : ℚ) - (z' : ℚ)) = ((z - z' : ℤ) : ℚ) by push_cast; ring]
  exact (padicNorm.int_lt_one_iff _).2 hd

/-- A `ZMod p`-vanishing integer is `p`-divisible in `ℚ`. -/
theorem PDvd.of_zmod {z : ℤ} (h : (z : ZMod p) = 0) : PDvd p (z : ℚ) := by
  have hh : PCong p (z : ℚ) 0 := by
    simpa using PCong.of_zmod (p := p) (z := z) (z' := 0) (by simpa using h)
  exact PCong.zero_iff.1 hh

end ZetaLucas
