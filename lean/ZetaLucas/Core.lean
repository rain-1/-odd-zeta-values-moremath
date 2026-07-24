/-
Core toolkit for the base-`p` Lucas congruences of the odd-zeta program.

Provides:
* `Finset.sum_range_mul` : reindexing `range (m * n)` as a double sum (the base-`p`
  digit splitting of a summation range);
* `ZetaLucas.choose_digits` : the "Lucas step" `C(a*p+r, b*p+s) ≡ C(a,b) * C(r,s) (mod p)`,
  specialised from Mathlib's `Choose.choose_modEq_choose_mod_mul_choose_div`;
* `ZetaLucas.choose_carry_zero` : carry annihilation, `C(x, y) ≡ 0 (mod p)` when the low
  digits carry (`x = 1*p + (x - p)` with `x - p < y < p`).
-/
import Mathlib

open Finset

namespace Finset

/-- Splitting a range of length `m * n` into `m` blocks of length `n`. -/
theorem sum_range_mul {M : Type*} [AddCommMonoid M] (f : ℕ → M) (m n : ℕ) :
    ∑ k ∈ range (m * n), f k = ∑ i ∈ range m, ∑ j ∈ range n, f (i * n + j) := by
  induction m with
  | zero => simp
  | succ m ih =>
    rw [Nat.succ_mul, Finset.sum_range_add, ih, Finset.sum_range_succ]

end Finset

namespace ZetaLucas

variable {p : ℕ} [Fact p.Prime]

/-- The **Lucas step**: for a prime `p` and digits `r, s < p`,
`C(a*p + r, b*p + s) ≡ C(a,b) * C(r,s) (mod p)`.

This is Mathlib's `Choose.choose_modEq_choose_mod_mul_choose_div` with the base-`p`
division/remainder computed explicitly. -/
theorem choose_digits (a b r s : ℕ) (hr : r < p) (hs : s < p) :
    (((a * p + r).choose (b * p + s) : ℕ) : ZMod p)
      = ((a.choose b : ℕ) : ZMod p) * ((r.choose s : ℕ) : ZMod p) := by
  have key := Choose.choose_modEq_choose_mod_mul_choose_div
    (p := p) (n := a * p + r) (k := b * p + s)
  rw [← ZMod.intCast_eq_intCast_iff] at key
  have hp : 0 < p := (Fact.out (p := p.Prime)).pos
  have h1 : (a * p + r) % p = r := by
    rw [mul_comm, Nat.mul_add_mod, Nat.mod_eq_of_lt hr]
  have h2 : (a * p + r) / p = a := by
    rw [mul_comm, Nat.mul_add_div hp, Nat.div_eq_of_lt hr, Nat.add_zero]
  have h3 : (b * p + s) % p = s := by
    rw [mul_comm, Nat.mul_add_mod, Nat.mod_eq_of_lt hs]
  have h4 : (b * p + s) / p = b := by
    rw [mul_comm, Nat.mul_add_div hp, Nat.div_eq_of_lt hs, Nat.add_zero]
  rw [h1, h2, h3, h4] at key
  push_cast at key
  rw [key]
  ring

/-- The Lucas step in "supply the base-`p` decomposition" form: convenient when the
decomposition of `n` involves a carry (`n = (A+1)*p + (ξ - p)`). -/
theorem choose_digits' {n k A B ξ η : ℕ} (hn : n = A * p + ξ) (hk : k = B * p + η)
    (hξ : ξ < p) (hη : η < p) :
    ((n.choose k : ℕ) : ZMod p)
      = ((A.choose B : ℕ) : ZMod p) * ((ξ.choose η : ℕ) : ZMod p) := by
  subst hn; subst hk; exact choose_digits A B ξ η hξ hη

/-- If the low digit of `n` is strictly below the low digit of `k`, then `C(n,k) ≡ 0 (mod p)`.
This is the mechanism by which a base-`p` carry annihilates a binomial coefficient. -/
theorem choose_digits_zero {n k A B ξ η : ℕ} (hn : n = A * p + ξ) (hk : k = B * p + η)
    (hξ : ξ < p) (hη : η < p) (h : ξ < η) : ((n.choose k : ℕ) : ZMod p) = 0 := by
  rw [choose_digits' hn hk hξ hη, Nat.choose_eq_zero_of_lt h]
  simp

/-- **Carry annihilation.** If `p ≤ x`, `y < p` and `x - p < y`, then
`C(x, y) ≡ 0 (mod p)`: the base-`p` digits of `x` are `(1, x - p)` and those of `y` are
`(0, y)`, so Lucas gives `C(1,0) * C(x - p, y) = 0`. -/
theorem choose_carry_zero {x y : ℕ} (hx : p ≤ x) (hy : y < p)
    (hxy : x - p < y) : ((x.choose y : ℕ) : ZMod p) = 0 := by
  have hlow : x - p < p := by omega
  have hx' : x = 1 * p + (x - p) := by omega
  have hy' : y = 0 * p + y := by omega
  rw [hx', hy', choose_digits 1 0 (x - p) y hlow hy,
    Nat.choose_eq_zero_of_lt hxy]
  simp

/-!
### Groundwork for the b-row (T3)

Not used by `apery_lucas` or `Q_lucas`.  Recorded here because it is the load-bearing
inventory fact for the T3 cost plan in `work/LEAN_LUCAS_STATUS.md` §S4.3: T3's hypothesis
`a < p` puts `n = a*p + r` below `p ^ 2`, and *therefore* Mathlib's Kummer carry-counting
`Finset.Ico 1 b` collapses to the singleton `{1}` — a single carry indicator.
-/

/-- **Kummer's theorem in the two-digit range.**  For `n < p ^ 2` and `k ≤ n`, the `p`-adic
valuation of `C(n,k)` is the single carry indicator `[p ≤ k mod p + (n-k) mod p]`. -/
theorem padicValNat_choose_lt_sq {n k : ℕ} (hn : n < p ^ 2) (hk : k ≤ n) :
    padicValNat p (n.choose k) = if p ≤ k % p + (n - k) % p then 1 else 0 := by
  have hlog : Nat.log p n < 2 := by
    rcases Nat.eq_zero_or_pos n with rfl | h
    · simp
    · exact Nat.log_lt_of_lt_pow (by omega) hn
  rw [padicValNat_choose hk hlog, show Finset.Ico 1 2 = {1} from rfl]
  simp only [Finset.filter_singleton, pow_one]
  split <;> simp

end ZetaLucas
