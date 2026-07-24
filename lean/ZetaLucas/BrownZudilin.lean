/-
Theorem (2) of the odd-zeta program's Lean task: **Theorem A** of
`work/PROOF_LB5_CAMPAIGN.md` — the Lucas congruence for the Brown–Zudilin row `Q`,

    T(n,k,l) = C(n+k,n) C(n,k)² C(n+l,n) C(n,l)² C(n+k+l,n)
    Q_n      = Σ_{k,l=0}^n T(n,k,l)                      (Q₀ = 1, Q₁ = 21, …)
    Q_{a·p+r} ≡ Q_a · Q_r  (mod p)                       for every prime p, a ≥ 0, r < p.

The new ingredient over the ζ(3) case is the **double-carry annihilation** lemma
(Lemma 3 of Theorem A): the combined low digit `r + s + t` can exceed `p`, and the
key non-obvious step is that on the surviving regime `s ≤ r, t ≤ r, r+s < p, r+t < p`
one automatically has `s + t < p`, so at most one carry occurs and it forces
`r + s + t - p < r`, killing `C(r+s+t, r)`.
-/
import ZetaLucas.Core

open Finset

namespace ZetaLucas

/-- The Brown–Zudilin summand `T(n,k,l) = C(n+k,n) C(n,k)² C(n+l,n) C(n,l)² C(n+k+l,n)`. -/
def T (n k l : ℕ) : ℕ :=
  (n + k).choose n * (n.choose k) ^ 2 * ((n + l).choose n) * (n.choose l) ^ 2 *
    ((n + k + l).choose n)

/-- The Brown–Zudilin row `Q_n = Σ_{k,l=0}^n T(n,k,l)`. -/
def Q (n : ℕ) : ℕ := ∑ k ∈ range (n + 1), ∑ l ∈ range (n + 1), T n k l

theorem T_eq_zero_of_lt_left {n k l : ℕ} (h : n < k) : T n k l = 0 := by
  simp [T, Nat.choose_eq_zero_of_lt h]

theorem T_eq_zero_of_lt_right {n k l : ℕ} (h : n < l) : T n k l = 0 := by
  simp [T, Nat.choose_eq_zero_of_lt h]

/-- `Q_n` may be summed over any square range containing `range (n+1)`. -/
theorem Q_eq_sum_range {n N : ℕ} (h : n + 1 ≤ N) :
    Q n = ∑ k ∈ range N, ∑ l ∈ range N, T n k l := by
  have hsub : range (n + 1) ⊆ range N :=
    fun x hx => Finset.mem_range.2 (lt_of_lt_of_le (Finset.mem_range.1 hx) h)
  have inner : ∀ k, ∑ l ∈ range (n + 1), T n k l = ∑ l ∈ range N, T n k l := by
    intro k
    refine Finset.sum_subset hsub ?_
    intro l _ hl
    exact T_eq_zero_of_lt_right (by simpa [Nat.lt_succ_iff, Nat.succ_le_iff] using hl)
  rw [Q, Finset.sum_congr rfl fun k _ => inner k]
  refine Finset.sum_subset hsub ?_
  intro k _ hk
  refine Finset.sum_eq_zero fun l _ => ?_
  exact T_eq_zero_of_lt_left (by simpa [Nat.lt_succ_iff, Nat.succ_le_iff] using hk)

variable {p : ℕ} [Fact p.Prime]

/-- **Summand factorization mod p** (Lemma 4 of Theorem A).  With `N = a·p + r`,
`k = b·p + s`, `l = c·p + t` and digits `r, s, t < p`,

    T(N, k, l) ≡ T(a, b, c) · T(r, s, t)   (mod p).

As in the ζ(3) case no indicator function is needed: outside the surviving regime
*both* sides vanish mod `p`.  The five factors of `T` are handled by five applications
of the Lucas step; the last one, `C(N+k+l, N)`, is the double-carry case. -/
theorem T_digits (a b c r s t : ℕ) (hr : r < p) (hs : s < p) (ht : t < p) :
    ((T (a * p + r) (b * p + s) (c * p + t) : ℕ) : ZMod p)
      = ((T a b c : ℕ) : ZMod p) * ((T r s t : ℕ) : ZMod p) := by
  -- Linear-arithmetic scaffolding: name the products so that `omega` can treat them as atoms.
  have m1 : (a + b) * p = a * p + b * p := by ring
  have m2 : (a + c) * p = a * p + c * p := by ring
  have m3 : (a + b + c) * p = a * p + b * p + c * p := by ring
  have m4 : (a + b + 1) * p = a * p + b * p + p := by ring
  have m5 : (a + c + 1) * p = a * p + c * p + p := by ring
  have m6 : (a + b + c + 1) * p = a * p + b * p + c * p + p := by ring
  have m7 : (0 : ℕ) * p = 0 := by ring
  -- The two lower binomials always factor.
  have f1 : (((a * p + r).choose (b * p + s) : ℕ) : ZMod p)
      = ((a.choose b : ℕ) : ZMod p) * ((r.choose s : ℕ) : ZMod p) :=
    choose_digits a b r s hr hs
  have f2 : (((a * p + r).choose (c * p + t) : ℕ) : ZMod p)
      = ((a.choose c : ℕ) : ZMod p) * ((r.choose t : ℕ) : ZMod p) :=
    choose_digits a c r t hr ht
  rcases lt_or_ge r s with hsr | hsr
  · -- `s > r`: `C(r,s) = 0` kills both sides.
    have hz : r.choose s = 0 := Nat.choose_eq_zero_of_lt hsr
    simp only [T, Nat.cast_mul, Nat.cast_pow]
    rw [f1, hz]
    simp
  rcases lt_or_ge r t with htr | htr
  · -- `t > r`: symmetric.
    have hz : r.choose t = 0 := Nat.choose_eq_zero_of_lt htr
    simp only [T, Nat.cast_mul, Nat.cast_pow]
    rw [f2, hz]
    simp
  rcases lt_or_ge (r + s) p with hrs | hrs
  case inr =>
    -- `r + s ≥ p`: the carry in `C(N+k, N)` kills the left side, and the same carry in
    -- `C(r+s, r)` kills the right side.
    have hlt : r + s - p < r := by omega
    have hL : ((((a * p + r) + (b * p + s)).choose (a * p + r) : ℕ) : ZMod p) = 0 :=
      choose_digits_zero (A := a + b + 1) (B := a) (ξ := r + s - p) (η := r)
        (by omega) rfl (by omega) hr hlt
    have hR : (((r + s).choose r : ℕ) : ZMod p) = 0 :=
      choose_carry_zero (by omega) hr hlt
    simp only [T, Nat.cast_mul, Nat.cast_pow]
    rw [hL, hR]
    ring
  rcases lt_or_ge (r + t) p with hrt | hrt
  case inr =>
    -- `r + t ≥ p`: symmetric.
    have hlt : r + t - p < r := by omega
    have hL : ((((a * p + r) + (c * p + t)).choose (a * p + r) : ℕ) : ZMod p) = 0 :=
      choose_digits_zero (A := a + c + 1) (B := a) (ξ := r + t - p) (η := r)
        (by omega) rfl (by omega) hr hlt
    have hR : (((r + t).choose r : ℕ) : ZMod p) = 0 :=
      choose_carry_zero (by omega) hr hlt
    simp only [T, Nat.cast_mul, Nat.cast_pow]
    rw [hL, hR]
    ring
  -- Surviving regime: `s ≤ r`, `t ≤ r`, `r + s < p`, `r + t < p`.
  -- **The non-obvious step**: these four force `s + t < p`, so `r+s+t < 2p`, i.e. at most
  -- one carry.  (If `s + t ≥ p` then `p ≤ s + t ≤ 2r`, while `r+s<p` and `r+t<p` give
  -- `s + t ≤ 2(p-1-r) < p`.)
  have hst : s + t < p := by omega
  have f3 : ((((a * p + r) + (b * p + s)).choose (a * p + r) : ℕ) : ZMod p)
      = (((a + b).choose a : ℕ) : ZMod p) * (((r + s).choose r : ℕ) : ZMod p) :=
    choose_digits' (A := a + b) (B := a) (ξ := r + s) (η := r) (by omega) rfl hrs hr
  have f4 : ((((a * p + r) + (c * p + t)).choose (a * p + r) : ℕ) : ZMod p)
      = (((a + c).choose a : ℕ) : ZMod p) * (((r + t).choose r : ℕ) : ZMod p) :=
    choose_digits' (A := a + c) (B := a) (ξ := r + t) (η := r) (by omega) rfl hrt hr
  rcases lt_or_ge (r + s + t) p with hrst | hrst
  · -- No carry anywhere: all five factors factor, and the products match.
    have f5 : ((((a * p + r) + (b * p + s) + (c * p + t)).choose (a * p + r) : ℕ) : ZMod p)
        = (((a + b + c).choose a : ℕ) : ZMod p) * (((r + s + t).choose r : ℕ) : ZMod p) :=
      choose_digits' (A := a + b + c) (B := a) (ξ := r + s + t) (η := r) (by omega) rfl hrst hr
    simp only [T, Nat.cast_mul, Nat.cast_pow]
    rw [f1, f2, f3, f4, f5]
    ring
  · -- **Double-carry annihilation**: `r+s+t ≥ p` but `s+t < p`, so the low digit of
    -- `N+k+l` is `r+s+t-p < r` and `C(N+k+l, N) ≡ 0`; likewise `C(r+s+t, r) ≡ 0`.
    have hlt : r + s + t - p < r := by omega
    have hL : ((((a * p + r) + (b * p + s) + (c * p + t)).choose (a * p + r) : ℕ) : ZMod p) = 0 :=
      choose_digits_zero (A := a + b + c + 1) (B := a) (ξ := r + s + t - p) (η := r)
        (by omega) rfl (by omega) hr hlt
    have hR : (((r + s + t).choose r : ℕ) : ZMod p) = 0 :=
      choose_carry_zero (by omega) hr hlt
    simp only [T, Nat.cast_mul, Nat.cast_pow]
    rw [hL, hR]
    ring

/-- **Theorem (2) = Theorem A: the Q-row Lucas congruence.**  For every prime `p`,
every `a ≥ 0` and every digit `r < p`,

    Q_{a·p + r} ≡ Q_a · Q_r   (mod p). -/
theorem Q_lucas (a r : ℕ) (hr : r < p) :
    ((Q (a * p + r) : ℕ) : ZMod p) = ((Q a : ℕ) : ZMod p) * ((Q r : ℕ) : ZMod p) := by
  have hblock : a * p + r + 1 ≤ (a + 1) * p := by
    have : (a + 1) * p = a * p + p := by ring
    omega
  -- Step 1: extend both summation ranges to a full block `range ((a+1) * p)`.
  rw [Q_eq_sum_range (n := a * p + r) (N := (a + 1) * p) hblock]
  -- Step 2: split both blocks into base-`p` digits.
  rw [Finset.sum_range_mul (fun k => ∑ l ∈ range ((a + 1) * p), T (a * p + r) k l) (a + 1) p]
  rw [Finset.sum_congr rfl fun b _ => Finset.sum_congr rfl fun s _ =>
    Finset.sum_range_mul (fun l => T (a * p + r) (b * p + s) l) (a + 1) p]
  push_cast
  -- Step 3: factorize each summand mod `p`.
  rw [Finset.sum_congr rfl fun b _ => Finset.sum_congr rfl fun s hs =>
    Finset.sum_congr rfl fun c _ => Finset.sum_congr rfl fun t ht =>
      T_digits a b c r s t hr (Finset.mem_range.1 hs) (Finset.mem_range.1 ht)]
  -- Step 4: swap the `s` and `c` sums so the (b,c)-region and the (s,t)-region separate.
  rw [Finset.sum_congr rfl fun b _ =>
    Finset.sum_comm (s := range p) (t := range (a + 1))
      (f := fun s c => ∑ t ∈ range p, ((T a b c : ℕ) : ZMod p) * ((T r s t : ℕ) : ZMod p))]
  -- Step 5: the quadruple sum is a product of two independent double sums.
  simp only [← Finset.mul_sum, ← Finset.sum_mul]
  congr 1
  · -- The high factor is `Q_a`, an exact integer identity.
    rw [Q]
    push_cast
    rfl
  · -- The low factor is `Q_r`: the extra terms with `s > r` or `t > r` vanish
    -- since `C(r,s) = 0` resp. `C(r,t) = 0`.
    rw [Q_eq_sum_range (n := r) (N := p) hr]
    push_cast
    rfl

/-- **Full Lucas property** for the Brown–Zudilin row: `Q_n ≡ ∏_i Q_{n_i} (mod p)`. -/
theorem Q_lucas_digits (n : ℕ) :
    ((Q n : ℕ) : ZMod p) = ((Nat.digits p n).map (fun d => ((Q d : ℕ) : ZMod p))).prod := by
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    rcases Nat.eq_zero_or_pos n with rfl | hn
    · simp [Q, T]
    · have hp1 : 1 < p := (Fact.out (p := p.Prime)).one_lt
      rw [Nat.digits_def' hp1 hn]
      simp only [List.map_cons, List.prod_cons]
      rw [← ih (n / p) (Nat.div_lt_self hn hp1)]
      conv_lhs => rw [← Nat.div_add_mod' n p]
      rw [Q_lucas (n / p) (n % p) (Nat.mod_lt _ (by omega))]
      ring

section Sanity

/-- Kernel-checked: `Q₀ = 1`, `Q₁ = 21`, `Q₂ = 2989`.  In particular `Q₁ = 21` pins the
double-sum normalization of `work/PROOF_LB5_CAMPAIGN.md` §1 (as opposed to the single-sum
`Σ_k C(n,k)²C(n+k,k)`, which would give `3`). -/
example : Q 0 = 1 ∧ Q 1 = 21 ∧ Q 2 = 2989 := by decide

-- Kernel-checked spot-check of `Q_lucas` at `p = 5` (including the multi-digit cell `a = 2`).
set_option maxRecDepth 4000 in
example : ∀ a ∈ List.range 3, ∀ r ∈ List.range 5,
    Q (a * 5 + r) % 5 = (Q a * Q r) % 5 := by decide

end Sanity

-- First few values of `Q`: `[1, 21, 2989, 714549, 217515501, 76157194521]`.
#eval (List.range 6).map Q

-- Evaluated (not kernel-checked) sweep of `Q_lucas` at `p = 5`, `a < 6`, `r < 5`.
-- Prints `true`.
#eval (List.range 6).all fun a =>
  (List.range 5).all fun r => Q (a * 5 + r) % 5 = (Q a * Q r) % 5

end ZetaLucas
