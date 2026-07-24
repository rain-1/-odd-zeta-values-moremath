/-
Theorem (1) of the odd-zeta program's Lean task: the **a-row Lucas congruence** for the
Apéry numbers of ζ(3),

    a_n = Σ_{k=0}^n C(n,k)² C(n+k,k)²      (OEIS A005259)
    a_{a·p+r} ≡ a_a · a_r  (mod p)         for every prime p, every a ≥ 0, every r < p.

Reference proof: `work/WARMUP_ZETA3_DWORK.md`, section T2.
-/
import ZetaLucas.Core

open Finset

namespace ZetaLucas

/-- Apéry's ζ(3) summand `A(n,k) = C(n,k)² · C(n+k,k)²`. -/
def A (n k : ℕ) : ℕ := (n.choose k) ^ 2 * ((n + k).choose k) ^ 2

/-- The Apéry numbers for ζ(3): `a_n = Σ_{k=0}^n C(n,k)² C(n+k,k)²` (OEIS A005259). -/
def apery (n : ℕ) : ℕ := ∑ k ∈ range (n + 1), A n k

/-- The summand vanishes above the diagonal. -/
theorem A_eq_zero_of_lt {n k : ℕ} (h : n < k) : A n k = 0 := by
  simp [A, Nat.choose_eq_zero_of_lt h]

/-- `a_n` may be summed over any range containing `range (n+1)`. -/
theorem apery_eq_sum_range {n N : ℕ} (h : n + 1 ≤ N) :
    apery n = ∑ k ∈ range N, A n k := by
  refine Finset.sum_subset (fun k hk => Finset.mem_range.2
    (lt_of_lt_of_le (Finset.mem_range.1 hk) h)) ?_
  intro k _ hk
  exact A_eq_zero_of_lt (by simpa [Nat.lt_succ_iff, Nat.succ_le_iff] using hk)

variable {p : ℕ} [Fact p.Prime]

/-- **Summand factorization mod p** (Lemma 3 of T2).  With `n = a·p + r` and `k = b·p + s`
(digits `r, s < p`),

    A(n, k) ≡ (C(a,b)² C(a+b,b)²) · A(r, s)   (mod p).

No indicator function is needed: in the carrying regime `r + s ≥ p` *both* sides vanish
mod `p` — the left because `C(n+k, k) ≡ C(a+b+1, b)·C(r+s-p, s)` and `r+s-p < s`, the
right because `C(r+s, s) ≡ 0` by the same carry annihilation. -/
theorem A_digits (a b r s : ℕ) (hr : r < p) (hs : s < p) :
    ((A (a * p + r) (b * p + s) : ℕ) : ZMod p)
      = (((a.choose b) ^ 2 * ((a + b).choose b) ^ 2 : ℕ) : ZMod p) * ((A r s : ℕ) : ZMod p) := by
  have hlow : ((((a * p + r).choose (b * p + s)) : ℕ) : ZMod p)
      = ((a.choose b : ℕ) : ZMod p) * ((r.choose s : ℕ) : ZMod p) :=
    choose_digits a b r s hr hs
  have hsum : a * p + r + (b * p + s) = (a + b) * p + (r + s) := by ring
  rcases lt_or_ge (r + s) p with hc | hc
  · -- No carry: the upper binomial factorizes as `C(a+b, b) · C(r+s, s)`.
    have hhi : ((((a * p + r + (b * p + s)).choose (b * p + s)) : ℕ) : ZMod p)
        = (((a + b).choose b : ℕ) : ZMod p) * (((r + s).choose s : ℕ) : ZMod p) := by
      rw [hsum]; exact choose_digits (a + b) b (r + s) s hc hs
    simp only [A, Nat.cast_mul, Nat.cast_pow] at hlow hhi ⊢
    rw [hlow, hhi]
    ring
  · -- Carry: both sides are `0 (mod p)`.
    have hcs : r + s - p < s := by omega
    have hhi : ((((a * p + r + (b * p + s)).choose (b * p + s)) : ℕ) : ZMod p) = 0 := by
      rw [hsum]
      have hstep : (a + b + 1) * p = (a + b) * p + p := by ring
      have : ((((a + b) * p + (r + s)).choose (b * p + s)) : ℕ)
          = (((a + b + 1) * p + (r + s - p)).choose (b * p + s)) := by
        congr 1; omega
      rw [this, choose_digits (a + b + 1) b (r + s - p) s (by omega) hs,
        Nat.choose_eq_zero_of_lt hcs]
      simp
    have hrs : (((r + s).choose s : ℕ) : ZMod p) = 0 :=
      choose_carry_zero (by omega) hs hcs
    simp only [A, Nat.cast_mul, Nat.cast_pow] at hhi hrs ⊢
    rw [hhi, hrs]
    ring

/-- **Theorem (1): the a-row Lucas congruence.**  For every prime `p`, every `a ≥ 0` and
every digit `r < p`,

    a_{a·p + r} ≡ a_a · a_r   (mod p). -/
theorem apery_lucas (a r : ℕ) (hr : r < p) :
    ((apery (a * p + r) : ℕ) : ZMod p)
      = ((apery a : ℕ) : ZMod p) * ((apery r : ℕ) : ZMod p) := by
  have hblock : a * p + r + 1 ≤ (a + 1) * p := by
    have : (a + 1) * p = a * p + p := by ring
    omega
  -- Step 1: extend the summation range to a full block `range ((a+1) * p)`.
  rw [apery_eq_sum_range (n := a * p + r) (N := (a + 1) * p) hblock]
  -- Step 2: split the block into base-`p` digits `k = b·p + s`.
  rw [Finset.sum_range_mul (fun k => A (a * p + r) k) (a + 1) p]
  push_cast
  -- Step 3: factorize each summand mod `p`.
  rw [Finset.sum_congr rfl fun b _ => Finset.sum_congr rfl fun s hs =>
    A_digits a b r s hr (Finset.mem_range.1 hs)]
  -- Step 4: the double sum is a product of two independent sums.
  rw [← Finset.sum_mul_sum]
  congr 1
  · -- The high factor is `a_a`, an exact integer identity (`A a b` unfolds to the summand).
    rw [apery]
    push_cast
    exact Finset.sum_congr rfl fun b _ => by simp [A]
  · -- The low factor is `a_r`: the extra terms `r < s < p` vanish since `C(r,s) = 0`.
    rw [apery_eq_sum_range (n := r) (N := p) hr]
    push_cast
    rfl

/-- **Full Lucas property.**  `a_n ≡ ∏_i a_{n_i} (mod p)`, the product over the base-`p`
digits of `n`.  Immediate induction from `apery_lucas`, which holds for *all* `a ≥ 0`. -/
theorem apery_lucas_digits (n : ℕ) :
    ((apery n : ℕ) : ZMod p)
      = ((Nat.digits p n).map (fun d => ((apery d : ℕ) : ZMod p))).prod := by
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    rcases Nat.eq_zero_or_pos n with rfl | hn
    · simp [apery, A]
    · have hp1 : 1 < p := (Fact.out (p := p.Prime)).one_lt
      rw [Nat.digits_def' hp1 hn]
      simp only [List.map_cons, List.prod_cons]
      rw [← ih (n / p) (Nat.div_lt_self hn hp1)]
      conv_lhs => rw [← Nat.div_add_mod' n p]
      rw [apery_lucas (n / p) (n % p) (Nat.mod_lt _ (by omega))]
      ring

section Sanity

/-- `a_n` reproduces OEIS A005259: `1, 5, 73, 1445, 33001, 819005, …`. -/
example : (List.range 6).map apery = [1, 5, 73, 1445, 33001, 819005] := by decide

/-- Kernel-checked spot-check of `apery_lucas` at `p = 5`. -/
example : ∀ a ∈ List.range 5, ∀ r ∈ List.range 5,
    apery (a * 5 + r) % 5 = (apery a * apery r) % 5 := by decide

-- Wider (evaluated, not kernel-checked) sweep: `p ∈ {5,7,11,13}`, `a < 2p`, `r < p`.
-- Prints `true`.
#eval [5, 7, 11, 13].all fun p =>
  (List.range (2 * p)).all fun a =>
    (List.range p).all fun r => apery (a * p + r) % p = (apery a * apery r) % p

end Sanity

end ZetaLucas
