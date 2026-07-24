/-
**S1(b) of task P5c** — the reusable *two-digit Kummer* module, extending
`ZetaLucas.padicValNat_choose_lt_sq` of `ZetaLucas/Core.lean`.

The favourable structural fact (recorded in `work/LEAN_LUCAS_STATUS.md` §S4.3): a hypothesis
`a < p` puts `n = a·p + r` below `p²`, so Mathlib's Kummer carry-counting `Finset.Ico 1 b`
collapses to the singleton `{1}` — a *single* carry indicator; and `n + m < p³` collapses it to
`{1,2}` — at most two carries.

**This module is NOT used by `ZetaLucas/TheoremLB.lean` or `ZetaLucas/Instances.lean`.**
The `(LB_w^χ)` route of `work/LBW_GENERAL.md` §T4 replaces the entire Kummer ledger of the old
`T3` proof (Lemma V, T-fact, Tvanish) by *tameness*: `p^w·w(n,k)` is `p`-integral outright.
The module is kept because the ledger is what a **non-tame** instance (Domb, ε, s₇, E — the
"Lemma-D upgrade" cases of §T4) will need.
-/
import ZetaLucas.Core

open Finset

set_option linter.unusedSectionVars false

namespace ZetaLucas

variable {p : ℕ} [Fact p.Prime]

/-- `a·p + r < p²` for digits `a, r < p`. -/
theorem lt_sq_of_digits {a r : ℕ} (ha : a < p) (hr : r < p) : a * p + r < p ^ 2 := by
  have h : (a + 1) * p ≤ p * p := Nat.mul_le_mul_right p (by omega)
  have e : (a + 1) * p = a * p + p := by ring
  rw [pow_two]; omega

/-- **K1 — Kummer's theorem in digit form.**  For `n = a·p + r` with `a, r < p` and `m ≤ n`,

    v_p C(n, m) = [ r < m mod p ],

i.e. the valuation is exactly the indicator of a *borrow in the low digit*.  In particular it
is `≤ 1`: two digits admit at most one carry. -/
theorem padicValNat_choose_digits {a r m : ℕ} (ha : a < p) (hr : r < p)
    (hm : m ≤ a * p + r) :
    padicValNat p ((a * p + r).choose m) = if r < m % p then 1 else 0 := by
  have hp0 : 0 < p := (Fact.out (p := p.Prime)).pos
  rw [padicValNat_choose_lt_sq (lt_sq_of_digits ha hr) hm]
  have hmd : m / p * p + m % p = m := Nat.div_add_mod' m p
  have hm0p : m % p < p := Nat.mod_lt _ hp0
  by_cases hc : m % p ≤ r
  · -- no borrow: `⌊m/p⌋ ≤ a` and `(n - m) mod p = r - m mod p`
    have h1 : m / p ≤ a := by
      by_contra hcon
      have h2 : (a + 1) * p ≤ m / p * p := Nat.mul_le_mul_right p (by omega)
      have h3 : (a + 1) * p = a * p + p := by ring
      omega
    have hsub : (a - m / p) * p = a * p - m / p * p := Nat.sub_mul a (m / p) p
    have hle : m / p * p ≤ a * p := Nat.mul_le_mul_right p h1
    have e : a * p + r - m = (a - m / p) * p + (r - m % p) := by omega
    rw [e, mul_comm, Nat.mul_add_mod, Nat.mod_eq_of_lt (by omega : r - m % p < p),
      if_neg (by omega), if_neg (by omega)]
  · -- borrow: `⌊m/p⌋ + 1 ≤ a` and `(n - m) mod p = p + r - m mod p`
    have h1 : m / p + 1 ≤ a := by
      by_contra hcon
      have h2 : a * p ≤ m / p * p := Nat.mul_le_mul_right p (by omega)
      omega
    have hsub : (a - m / p - 1) * p = a * p - m / p * p - p := by
      rw [Nat.sub_mul, Nat.sub_mul, one_mul]
    have hle2 : (m / p + 1) * p ≤ a * p := Nat.mul_le_mul_right p h1
    have h3 : (m / p + 1) * p = m / p * p + p := by ring
    have e : a * p + r - m = (a - m / p - 1) * p + (p + r - m % p) := by omega
    rw [e, mul_comm, Nat.mul_add_mod, Nat.mod_eq_of_lt (by omega : p + r - m % p < p),
      if_pos (by omega), if_pos (by omega)]

/-- In the two-digit range a binomial coefficient carries at most one factor of `p`. -/
theorem padicValNat_choose_le_one {n m : ℕ} (hn : n < p ^ 2) (hm : m ≤ n) :
    padicValNat p (n.choose m) ≤ 1 := by
  rw [padicValNat_choose_lt_sq hn hm]; split <;> omega

/-- **K3 — a low-digit carry forces one factor of `p`.**  For digits `x, y < p` with `x + y ≥ p`,
`p ∣ C(x+y, y)`.  (The `ZMod`-flavoured twin of `ZetaLucas.choose_carry_zero`.) -/
theorem p_dvd_choose_of_carry {x y : ℕ} (hx : x < p) (hy : y < p) (hxy : p ≤ x + y) :
    p ∣ (x + y).choose y := by
  have h := choose_carry_zero (p := p) (x := x + y) (y := y) hxy hy (by omega)
  exact (ZMod.natCast_eq_zero_iff _ _).1 h

/-- **K4 — no carry in `C(n, j·p)`.**  A multiple of `p` never borrows in the low digit, so
`v_p C(a·p + r, j·p) = 0`. -/
theorem padicValNat_choose_mul_p {a r j : ℕ} (ha : a < p) (hr : r < p)
    (hm : j * p ≤ a * p + r) : padicValNat p ((a * p + r).choose (j * p)) = 0 := by
  have hp0 : 0 < p := (Fact.out (p := p.Prime)).pos
  rw [padicValNat_choose_digits ha hr hm, Nat.mul_mod_left, if_neg (by omega)]

/-- **K2 — the three-digit range.**  For `n + m < p³` the Kummer count is the sum of two carry
indicators, so `v_p C(n+m, m) ≤ 2`.  This is the shape needed for the `C(n+m,m)` factor of the
Apéry summand, where `n + m < 2p² < p³`. -/
theorem padicValNat_add_choose_lt_cube {n m : ℕ} (h : n + m < p ^ 3) :
    padicValNat p ((n + m).choose m)
      = (if p ^ 1 ≤ m % p ^ 1 + n % p ^ 1 then 1 else 0)
        + (if p ^ 2 ≤ m % p ^ 2 + n % p ^ 2 then 1 else 0) := by
  have hlog : Nat.log p (n + m) < 3 := by
    rcases Nat.eq_zero_or_pos (n + m) with hz | hpos
    · rw [hz]; simp
    · exact Nat.log_lt_of_lt_pow (by omega) h
  rw [padicValNat_choose' hlog, show Finset.Ico 1 3 = ({1, 2} : Finset ℕ) from rfl]
  rw [Finset.filter_insert, Finset.filter_singleton]
  split_ifs <;> simp_all

/-- `v_p C(n+m, m) ≤ 2` in the three-digit range. -/
theorem padicValNat_add_choose_le_two {n m : ℕ} (h : n + m < p ^ 3) :
    padicValNat p ((n + m).choose m) ≤ 2 := by
  rw [padicValNat_add_choose_lt_cube h]
  split <;> split <;> omega

end ZetaLucas
