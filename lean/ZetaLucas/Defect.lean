/-
# The Apéry defect identity `V_n = 0`

**Target** (`work/APERY_DEFECT.md` §3.2, `papers_out/frobenius_matrix/main.tex` Theorem 2.2):

    V_n := Σ_{k=0}^{n} C(n,k)² C(n+k,k)² ( H_{n+k} + H_{n−k} − 2H_k )  =  0    for all n ≥ 0.

The write-up proves this by a residue argument over `ℂ` (reflection formula, cancelling double
poles, sum of residues of an `O(z^{-2})` meromorphic function).  That route is *not* what is
formalized here.  The residue argument can be made completely elementary and purely algebraic,
because the meromorphic function in question is a **rational** function:

    g(z) = Γ(n+z+1)²Γ(z−n)²/Γ(z+1)^4 = [ ∏_{i=1}^{n}(z+i) / ∏_{j=0}^{n}(z−j) ]² = φ(z)² .

`φ = P/Q` has *simple* poles at `z = 0,…,n` with residues `α_k = (−1)^{n−k}C(n,k)C(n+k,k)`, so
`g = φ²` has residue `2 α_m Σ_{k≠m} α_k/(m−k)` at `z = m` — and that double sum is manifestly
antisymmetric, hence sums to `0` over `m`.  Everything reduces to the *finite* identity

    (★)   Σ_{k=0}^{n} β_k / (m − k)  =  β_m ( H_{n+m} + H_{n−m} − 2H_m ),   β_k = (−1)^k C(n,k)C(n+k,k)

(the `k = m` term is `β_m/0 = 0` by Lean's division convention), which is the Lagrange
interpolation formula for `P(X) = ∏_{i=1}^n (X+i)` at the nodes `0,1,…,n`, differentiated once
and evaluated at a node.  So the only imported machinery is `Lagrange.nodal` and
`Polynomial.derivative`; no analysis of any kind occurs.

Summing (★) against `β_m` and using `β_m² = A(n,m)` gives `V_n = Σ_{m,k} β_mβ_k/(m−k) = 0`.
-/
import ZetaLucas.MinimalForm
import Mathlib.LinearAlgebra.Lagrange

open Finset Polynomial

namespace ZetaLucas

/-! ## 0. The sequences -/

/-- `c(n,k) = C(n,k)·C(n+k,k)`, the square root of the Apéry summand `A(n,k)`. -/
def cc (n k : ℕ) : ℚ := (n.choose k : ℚ) * ((n + k).choose k : ℚ)

/-- The **signed** square root `β_k = (−1)^k c(n,k)` — the residue of `φ` at `z = k`, up to the
global sign `(−1)^n`. -/
def bb (n k : ℕ) : ℚ := (-1) ^ k * cc n k

theorem bb_sq (n k : ℕ) : bb n k ^ 2 = (A n k : ℚ) := by
  have h : ((-1 : ℚ) ^ k) ^ 2 = 1 := by
    rw [← pow_mul, mul_comm, pow_mul]; norm_num
  simp only [bb, cc, A_cast, mul_pow, h, one_mul]

/-- `v(n,k) = H_{n+k} + H_{n−k} − 2H_k = ½ ∂_k log A(n,k)`. -/
def vv (n k : ℕ) : ℚ := Harm 1 (n + k) + Harm 1 (n - k) - 2 * Harm 1 k

/-- `V_n = Σ_{k=0}^n A(n,k) v(n,k)`. -/
def Vsum (n : ℕ) : ℚ := ∑ k ∈ range (n + 1), (A n k : ℚ) * vv n k

/-! ## 1. Elementary harmonic and factorial evaluations -/

/-- `H_m = Σ_{j<m} 1/(j+1)`. -/
theorem Harm_one_eq (m : ℕ) : Harm 1 m = ∑ j ∈ range m, (1 : ℚ) / ((j : ℚ) + 1) := by
  induction m with
  | zero => simp [Harm_zero 1 (by norm_num)]
  | succ m ih => rw [Harm_succ, ih, Finset.sum_range_succ]; simp

theorem prod_range_add_one (m : ℕ) : ∏ j ∈ range m, ((j : ℚ) + 1) = (m.factorial : ℚ) := by
  induction m with
  | zero => simp
  | succ m ih => rw [Finset.prod_range_succ, ih, Nat.factorial_succ]; push_cast; ring

/-! ### The lower half `j < m` -/

theorem prod_lower (m : ℕ) :
    ∏ j ∈ range m, ((m : ℚ) - (j : ℚ)) = (m.factorial : ℚ) := by
  rw [← prod_range_add_one m, ← Finset.prod_range_reflect (fun j => (m : ℚ) - (j : ℚ)) m]
  refine Finset.prod_congr rfl fun j hj => ?_
  have hj' : j < m := Finset.mem_range.1 hj
  have : ((m - 1 - j : ℕ) : ℚ) = (m : ℚ) - 1 - (j : ℚ) := by
    have : (1 : ℕ) + j ≤ m := by omega
    push_cast [Nat.cast_sub (by omega : j ≤ m - 1), Nat.cast_sub (by omega : 1 ≤ m)]
    ring
  rw [this]; ring

theorem sum_lower (m : ℕ) :
    ∑ j ∈ range m, (1 : ℚ) / ((m : ℚ) - (j : ℚ)) = Harm 1 m := by
  rw [Harm_one_eq, ← Finset.sum_range_reflect (fun j => (1 : ℚ) / ((m : ℚ) - (j : ℚ))) m]
  refine Finset.sum_congr rfl fun j hj => ?_
  have hj' : j < m := Finset.mem_range.1 hj
  have : ((m - 1 - j : ℕ) : ℚ) = (m : ℚ) - 1 - (j : ℚ) := by
    push_cast [Nat.cast_sub (by omega : j ≤ m - 1), Nat.cast_sub (by omega : 1 ≤ m)]
    ring
  rw [this]; ring_nf

/-! ### The upper half `m < j ≤ n` -/

theorem prod_upper (n m : ℕ) (hm : m ≤ n) :
    ∏ j ∈ Ico (m + 1) (n + 1), ((m : ℚ) - (j : ℚ))
      = (-1) ^ (n - m) * ((n - m).factorial : ℚ) := by
  rw [Finset.prod_Ico_eq_prod_range]
  have hcard : n + 1 - (m + 1) = n - m := by omega
  rw [hcard]
  have : ∀ i ∈ range (n - m), ((m : ℚ) - ((m + 1 + i : ℕ) : ℚ)) = (-1) * ((i : ℚ) + 1) := by
    intro i _; push_cast; ring
  rw [Finset.prod_congr rfl this, Finset.prod_mul_distrib, Finset.prod_const,
    Finset.card_range, prod_range_add_one]

theorem sum_upper (n m : ℕ) (hm : m ≤ n) :
    ∑ j ∈ Ico (m + 1) (n + 1), (1 : ℚ) / ((m : ℚ) - (j : ℚ)) = -Harm 1 (n - m) := by
  rw [Finset.sum_Ico_eq_sum_range]
  have hcard : n + 1 - (m + 1) = n - m := by omega
  rw [hcard, Harm_one_eq]
  rw [← Finset.sum_neg_distrib]
  refine Finset.sum_congr rfl fun i _ => ?_
  have : ((m + 1 + i : ℕ) : ℚ) = (m : ℚ) + 1 + (i : ℚ) := by push_cast; ring
  rw [this]
  rw [show (m : ℚ) - ((m : ℚ) + 1 + (i : ℚ)) = -((i : ℚ) + 1) by ring]
  rw [div_neg]

/-! ### The split of `(range (n+1)).erase m` -/

theorem erase_split (n m : ℕ) (hm : m ≤ n) :
    (range (n + 1)).erase m = range m ∪ Ico (m + 1) (n + 1) := by
  ext j
  simp only [Finset.mem_erase, Finset.mem_range, Finset.mem_union, Finset.mem_Ico]
  omega

theorem erase_disj (n m : ℕ) : Disjoint (range m) (Ico (m + 1) (n + 1)) := by
  rw [Finset.disjoint_left]
  intro j hj hj'
  simp only [Finset.mem_range] at hj
  simp only [Finset.mem_Ico] at hj'
  omega

/-- `∏_{j ≤ n, j ≠ m} (m − j) = (−1)^{n−m} m! (n−m)!` — the nodal weight at `m`. -/
theorem prod_erase (n m : ℕ) (hm : m ≤ n) :
    ∏ j ∈ (range (n + 1)).erase m, ((m : ℚ) - (j : ℚ))
      = (-1) ^ (n - m) * (m.factorial : ℚ) * ((n - m).factorial : ℚ) := by
  rw [erase_split n m hm, Finset.prod_union (erase_disj n m), prod_lower, prod_upper n m hm]
  ring

/-- `Σ_{j ≤ n, j ≠ m} 1/(m − j) = H_m − H_{n−m}`. -/
theorem sum_erase (n m : ℕ) (hm : m ≤ n) :
    ∑ j ∈ (range (n + 1)).erase m, (1 : ℚ) / ((m : ℚ) - (j : ℚ))
      = Harm 1 m - Harm 1 (n - m) := by
  rw [erase_split n m hm, Finset.sum_union (erase_disj n m), sum_lower, sum_upper n m hm]
  ring

theorem prod_erase_ne_zero (n m : ℕ) (hm : m ≤ n) :
    ∏ j ∈ (range (n + 1)).erase m, ((m : ℚ) - (j : ℚ)) ≠ 0 := by
  rw [prod_erase n m hm]
  have h1 : ((m.factorial : ℚ)) ≠ 0 := Nat.cast_ne_zero.2 (Nat.factorial_ne_zero m)
  have h2 : (((n - m).factorial : ℚ)) ≠ 0 := Nat.cast_ne_zero.2 (Nat.factorial_ne_zero _)
  have h3 : ((-1 : ℚ)) ^ (n - m) ≠ 0 := pow_ne_zero _ (by norm_num)
  exact mul_ne_zero (mul_ne_zero h3 h1) h2

/-! ### The `P`-side products -/

theorem prod_P (n m : ℕ) :
    (m.factorial : ℚ) * ∏ i ∈ Icc 1 n, ((m : ℚ) + (i : ℚ)) = ((n + m).factorial : ℚ) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [show Icc 1 (n + 1) = insert (n + 1) (Icc 1 n) by
      ext j; simp only [Finset.mem_Icc, Finset.mem_insert]; omega,
      Finset.prod_insert (by simp)]
    rw [show n + 1 + m = (n + m) + 1 by omega, Nat.factorial_succ]
    push_cast

    linear_combination ((m : ℚ) + (n : ℚ) + 1) * ih

theorem sum_P (n m : ℕ) :
    ∑ i ∈ Icc 1 n, (1 : ℚ) / ((m : ℚ) + (i : ℚ)) = Harm 1 (n + m) - Harm 1 m := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [show Icc 1 (n + 1) = insert (n + 1) (Icc 1 n) by
      ext j; simp only [Finset.mem_Icc, Finset.mem_insert]; omega,
      Finset.sum_insert (by simp), ih, show n + 1 + m = (n + m) + 1 by omega, Harm_succ]
    push_cast
    ring

/-! ## 2. The two polynomials, and Lagrange interpolation -/

/-- `W_k(X) = ∏_{j ≤ n, j ≠ k} (X − j)`. -/
noncomputable def Wpoly (n k : ℕ) : ℚ[X] :=
  Lagrange.nodal ((range (n + 1)).erase k) (fun j : ℕ => (j : ℚ))

/-- `P(X) = ∏_{i=1}^{n} (X + i)`. -/
noncomputable def Ppoly (n : ℕ) : ℚ[X] :=
  Lagrange.nodal (Icc 1 n) (fun i : ℕ => -(i : ℚ))

theorem Wpoly_eval (n k : ℕ) (x : ℚ) :
    (Wpoly n k).eval x = ∏ j ∈ (range (n + 1)).erase k, (x - (j : ℚ)) := by
  simp [Wpoly, Lagrange.eval_nodal]

theorem Ppoly_eval (n : ℕ) (x : ℚ) :
    (Ppoly n).eval x = ∏ i ∈ Icc 1 n, (x + (i : ℚ)) := by
  simp only [Ppoly, Lagrange.eval_nodal, sub_neg_eq_add]

theorem Wpoly_degree (n k : ℕ) (hk : k ∈ range (n + 1)) : (Wpoly n k).degree ≤ (n : WithBot ℕ) := by
  rw [Wpoly, Lagrange.degree_nodal, Finset.card_erase_of_mem hk, Finset.card_range]
  simp

theorem Ppoly_degree (n : ℕ) : (Ppoly n).degree ≤ (n : WithBot ℕ) := by
  rw [Ppoly, Lagrange.degree_nodal, Nat.card_Icc]
  simp

/-- **The node identity.**  `β_m · ∏_{j≠m}(m−j) = (−1)^n ∏_{i=1}^n (m+i)`. -/
theorem node_id (n m : ℕ) (hm : m ≤ n) :
    bb n m * ∏ j ∈ (range (n + 1)).erase m, ((m : ℚ) - (j : ℚ))
      = (-1) ^ n * ∏ i ∈ Icc 1 n, ((m : ℚ) + (i : ℚ)) := by
  have hfac : ((m.factorial : ℚ)) ≠ 0 := Nat.cast_ne_zero.2 (Nat.factorial_ne_zero m)
  -- the underlying natural-number factorial identity
  have hnat : n.choose m * ((n + m).choose m) * (m.factorial * (n - m).factorial * m.factorial)
      = (n + m).factorial := by
    have h1 : n.choose m * m.factorial * (n - m).factorial = n.factorial :=
      Nat.choose_mul_factorial_mul_factorial hm
    have h2 : (n + m).choose m * m.factorial * (n + m - m).factorial = (n + m).factorial :=
      Nat.choose_mul_factorial_mul_factorial (by omega)
    rw [show n + m - m = n by omega] at h2
    calc n.choose m * ((n + m).choose m) * (m.factorial * (n - m).factorial * m.factorial)
        = (n.choose m * m.factorial * (n - m).factorial)
          * ((n + m).choose m * m.factorial) := by ring
      _ = n.factorial * ((n + m).choose m * m.factorial) := by rw [h1]
      _ = (n + m).choose m * m.factorial * n.factorial := by ring
      _ = (n + m).factorial := h2
  have hnatQ : (n.choose m : ℚ) * ((n + m).choose m : ℚ)
      * ((m.factorial : ℚ) * ((n - m).factorial : ℚ) * (m.factorial : ℚ))
      = ((n + m).factorial : ℚ) := by exact_mod_cast congrArg (fun t : ℕ => (t : ℚ)) hnat
  -- multiply both sides by `m!`
  refine mul_left_cancel₀ hfac ?_
  rw [prod_erase n m hm]
  have hP : (m.factorial : ℚ) * ((-1) ^ n * ∏ i ∈ Icc 1 n, ((m : ℚ) + (i : ℚ)))
      = (-1) ^ n * ((n + m).factorial : ℚ) := by
    rw [← prod_P n m]; ring
  rw [hP]
  have hsign : ((-1 : ℚ)) ^ m * (-1) ^ (n - m) = (-1) ^ n := by
    rw [← pow_add, show m + (n - m) = n by omega]
  simp only [bb, cc]
  calc (m.factorial : ℚ) * ((-1) ^ m * ((n.choose m : ℚ) * ((n + m).choose m : ℚ))
        * ((-1) ^ (n - m) * (m.factorial : ℚ) * ((n - m).factorial : ℚ)))
      = ((-1 : ℚ)) ^ m * (-1) ^ (n - m) * ((n.choose m : ℚ) * ((n + m).choose m : ℚ)
        * ((m.factorial : ℚ) * ((n - m).factorial : ℚ) * (m.factorial : ℚ))) := by ring
    _ = (-1) ^ n * ((n + m).factorial : ℚ) := by rw [hsign, hnatQ]

/-- **Lagrange interpolation of `P` at the nodes `0,…,n`.** -/
theorem key_poly (n : ℕ) :
    ∑ k ∈ range (n + 1), C (bb n k) * Wpoly n k = C ((-1 : ℚ) ^ n) * Ppoly n := by
  have hinj : Set.InjOn (fun j : ℕ => (j : ℚ)) (range (n + 1)) :=
    fun a _ b _ h => Nat.cast_injective h
  have hcard : (range (n + 1)).card = n + 1 := Finset.card_range _
  have hlt : (n : WithBot ℕ) < ((n + 1 : ℕ) : WithBot ℕ) := by
    exact_mod_cast Nat.lt_succ_self n
  refine eq_of_degrees_lt_of_eval_index_eq (range (n + 1)) hinj ?_ ?_ ?_
  · refine lt_of_le_of_lt (Polynomial.degree_sum_le _ _) ?_
    rw [hcard]
    refine lt_of_le_of_lt (Finset.sup_le fun k hk => ?_) hlt
    exact le_trans (Polynomial.degree_mul_le _ _)
      (by simpa using add_le_add (Polynomial.degree_C_le) (Wpoly_degree n k hk))
  · rw [hcard]
    refine lt_of_le_of_lt ?_ hlt
    exact le_trans (Polynomial.degree_mul_le _ _)
      (by
        simpa using add_le_add
          (Polynomial.degree_C_le (R := ℚ) (a := ((-1 : ℚ) ^ n))) (Ppoly_degree n))
  · intro m hm
    have hmn : m ≤ n := by
      have := Finset.mem_range.1 hm; omega
    rw [Polynomial.eval_finsetSum, Polynomial.eval_mul, Polynomial.eval_C, Ppoly_eval]
    rw [Finset.sum_eq_single m]
    · rw [Polynomial.eval_mul, Polynomial.eval_C, Wpoly_eval]
      exact node_id n m hmn
    · intro k hk hkm
      rw [Polynomial.eval_mul, Polynomial.eval_C, Wpoly_eval]
      have : ∏ j ∈ (range (n + 1)).erase k, ((m : ℚ) - (j : ℚ)) = 0 :=
        Finset.prod_eq_zero (Finset.mem_erase.2 ⟨Ne.symm hkm, hm⟩) (by ring)
      rw [this, mul_zero]
    · intro h; exact absurd hm h

/-! ## 3. Differentiating the interpolation formula -/

/-- The derivative of `W_k` at a node `m ≠ k`. -/
theorem dW_eval_ne (n k m : ℕ) (hk : k ∈ range (n + 1)) (hm : m ∈ range (n + 1)) (hkm : k ≠ m) :
    (derivative (Wpoly n k)).eval (m : ℚ)
      = (∏ j ∈ (range (n + 1)).erase m, ((m : ℚ) - (j : ℚ))) / ((m : ℚ) - (k : ℚ)) := by
  classical
  rw [Wpoly, Lagrange.derivative_nodal, Polynomial.eval_finsetSum]
  rw [Finset.sum_eq_single m]
  · rw [Lagrange.eval_nodal]
    have hset : (((range (n + 1)).erase k).erase m) = (((range (n + 1)).erase m).erase k) := by
      ext j; simp only [Finset.mem_erase]; tauto
    rw [hset]
    have hkmem : k ∈ (range (n + 1)).erase m := Finset.mem_erase.2 ⟨hkm, hk⟩
    have hne : ((m : ℚ) - (k : ℚ)) ≠ 0 := by
      have : (m : ℚ) ≠ (k : ℚ) := fun h => hkm (by exact_mod_cast h.symm)
      exact sub_ne_zero_of_ne (Ne.symm (Ne.symm this))
    field_simp
    rw [Finset.prod_erase_mul _ _ hkmem]
  · intro i hi hine
    rw [Lagrange.eval_nodal]
    refine Finset.prod_eq_zero ?_ (by ring)
    exact Finset.mem_erase.2 ⟨Ne.symm hine, Finset.mem_erase.2 ⟨Ne.symm hkm, hm⟩⟩
  · intro h
    exact absurd (Finset.mem_erase.2 ⟨Ne.symm hkm, hm⟩) h

/-- The derivative of `W_m` at its own missing node `m`. -/
theorem dW_eval_self (n m : ℕ) (hm : m ≤ n) :
    (derivative (Wpoly n m)).eval (m : ℚ)
      = (∏ j ∈ (range (n + 1)).erase m, ((m : ℚ) - (j : ℚ))) * (Harm 1 m - Harm 1 (n - m)) := by
  classical
  rw [Wpoly, Lagrange.derivative_nodal, Polynomial.eval_finsetSum, ← sum_erase n m hm,
    Finset.mul_sum]
  refine Finset.sum_congr rfl fun i hi => ?_
  rw [Lagrange.eval_nodal]
  have him : i ≠ m := (Finset.mem_erase.1 hi).1
  have hne : ((m : ℚ) - (i : ℚ)) ≠ 0 := by
    have : (m : ℚ) ≠ (i : ℚ) := fun h => him (by exact_mod_cast h.symm)
    exact sub_ne_zero_of_ne this
  field_simp
  rw [Finset.prod_erase_mul _ _ hi]

/-- The derivative of `P` at `m`. -/
theorem dP_eval (n m : ℕ) :
    (derivative (Ppoly n)).eval (m : ℚ)
      = (∏ i ∈ Icc 1 n, ((m : ℚ) + (i : ℚ))) * (Harm 1 (n + m) - Harm 1 m) := by
  classical
  rw [Ppoly, Lagrange.derivative_nodal, Polynomial.eval_finsetSum, ← sum_P n m, Finset.mul_sum]
  refine Finset.sum_congr rfl fun i hi => ?_
  rw [Lagrange.eval_nodal]
  have hi1 : 1 ≤ i := (Finset.mem_Icc.1 hi).1
  have hne : ((m : ℚ) + (i : ℚ)) ≠ 0 := by
    have : (0 : ℚ) < (i : ℚ) := by exact_mod_cast hi1
    have : (0 : ℚ) ≤ (m : ℚ) := Nat.cast_nonneg m
    positivity
  simp only [sub_neg_eq_add]
  field_simp
  rw [Finset.prod_erase_mul _ _ hi]

/-! ## 4. The identity (★) and `V_n = 0` -/

/-- **(★)** — the differentiated interpolation formula at the node `m`:

    Σ_{k=0}^{n} β_k / (m − k)  =  β_m ( H_{n+m} + H_{n−m} − 2H_m ) .

(The `k = m` term of the left-hand side is `β_m/0 = 0`.) -/
theorem star_identity (n m : ℕ) (hm : m ≤ n) :
    ∑ k ∈ range (n + 1), bb n k / ((m : ℚ) - (k : ℚ)) = bb n m * vv n m := by
  classical
  have hmr : m ∈ range (n + 1) := Finset.mem_range.2 (by omega)
  set E : ℚ := ∏ j ∈ (range (n + 1)).erase m, ((m : ℚ) - (j : ℚ)) with hE
  have hEne : E ≠ 0 := prod_erase_ne_zero n m hm
  -- differentiate the interpolation identity and evaluate at `m`
  have hd := congrArg (fun q : ℚ[X] => (derivative q).eval (m : ℚ)) (key_poly n)
  simp only [derivative_sum, derivative_C_mul, Polynomial.eval_finsetSum, Polynomial.eval_mul,
    Polynomial.eval_C] at hd
  rw [dP_eval n m] at hd
  -- split off the `k = m` term on the left
  rw [← Finset.add_sum_erase _ _ hmr, dW_eval_self n m hm] at hd
  have hleft : ∑ k ∈ (range (n + 1)).erase m, bb n k * (derivative (Wpoly n k)).eval (m : ℚ)
      = E * ∑ k ∈ (range (n + 1)).erase m, bb n k / ((m : ℚ) - (k : ℚ)) := by
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun k hk => ?_
    obtain ⟨hkm, hkr⟩ := Finset.mem_erase.1 hk
    rw [dW_eval_ne n k m hkr hmr hkm]
    ring
  rw [hleft] at hd
  -- `(−1)^n · P(m) = β_m · E`
  have hnode : ((-1 : ℚ)) ^ n * ∏ i ∈ Icc 1 n, ((m : ℚ) + (i : ℚ)) = bb n m * E := by
    rw [hE, node_id n m hm]
  have hd2 : bb n m * (E * (Harm 1 m - Harm 1 (n - m)))
      + E * ∑ k ∈ (range (n + 1)).erase m, bb n k / ((m : ℚ) - (k : ℚ))
      = bb n m * E * (Harm 1 (n + m) - Harm 1 m) := by
    rw [hd, ← hnode]; ring
  -- solve for the sum
  have hsum : ∑ k ∈ (range (n + 1)).erase m, bb n k / ((m : ℚ) - (k : ℚ)) = bb n m * vv n m := by
    refine mul_left_cancel₀ hEne ?_
    simp only [vv]
    linear_combination hd2
  -- put the (vanishing) `k = m` term back
  rw [← Finset.add_sum_erase _ _ hmr, hsum, sub_self, div_zero, zero_add]

/-- **Theorem `V_n = 0`.**  The `v`-channel of the Apéry digit defect degenerates identically. -/
theorem Vsum_eq_zero (n : ℕ) : Vsum n = 0 := by
  classical
  set s : Finset ℕ := range (n + 1) with hs
  set f : ℕ → ℕ → ℚ := fun m k => bb n m * bb n k / ((m : ℚ) - (k : ℚ)) with hf
  have hanti : ∀ m k, f k m = -f m k := by
    intro m k
    simp only [hf]
    rw [show (k : ℚ) - (m : ℚ) = -((m : ℚ) - (k : ℚ)) by ring, div_neg, mul_comm (bb n k)]
  have hexp : Vsum n = ∑ m ∈ s, ∑ k ∈ s, f m k := by
    rw [Vsum, hs]
    refine Finset.sum_congr rfl fun m hm => ?_
    have hmn : m ≤ n := by have := Finset.mem_range.1 hm; omega
    rw [← bb_sq n m, pow_two, mul_assoc, ← star_identity n m hmn, Finset.mul_sum]
    refine Finset.sum_congr rfl fun k _ => ?_
    simp only [hf]
    ring
  have hswap : ∑ m ∈ s, ∑ k ∈ s, f m k = -∑ m ∈ s, ∑ k ∈ s, f m k := by
    conv_lhs => rw [Finset.sum_comm]
    rw [← Finset.sum_neg_distrib]
    refine Finset.sum_congr rfl fun m _ => ?_
    rw [← Finset.sum_neg_distrib]
    exact Finset.sum_congr rfl fun k _ => hanti m k
  rw [hexp]
  linarith [hswap]

/-- **`V_n = 0`, fully written out.**  For every `n ≥ 0`,

    Σ_{k=0}^{n} C(n,k)² C(n+k,k)² ( Σ_{j=1}^{n+k} 1/j + Σ_{j=1}^{n−k} 1/j − 2 Σ_{j=1}^{k} 1/j ) = 0.
-/
theorem apery_defect_V_eq_zero (n : ℕ) :
    ∑ k ∈ range (n + 1),
        ((n.choose k : ℚ) ^ 2 * (((n + k).choose k : ℚ)) ^ 2)
          * ((∑ j ∈ Finset.Icc 1 (n + k), (1 : ℚ) / (j : ℚ))
              + (∑ j ∈ Finset.Icc 1 (n - k), (1 : ℚ) / (j : ℚ))
              - 2 * ∑ j ∈ Finset.Icc 1 k, (1 : ℚ) / (j : ℚ))
      = 0 := by
  rw [← Vsum_eq_zero n, Vsum]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [A_cast, vv]
  simp only [Harm_eq 1 _ (by norm_num), pow_one]

/-! ## 5. The borrow region: `A` is a square, so it contributes nothing at first order

This is the second half of the digit expansion (`work/APERY_DEFECT.md` §3.1, paper Lemma 2.3):
*outside* the region `s ≤ r`, `c ≤ a`, `r+s < p` the relevant binomial coefficient is `≡ 0 mod p`,
and because `A(n,k) = (C(n,k)·C(n+k,k))²` is a **square**, both `A(ap+r, cp+s)` and `A(a,c)A(r,s)`
are then `≡ 0 mod p²`.  So the borrow region cannot contribute to a first-order (`mod p²`)
congruence at all.  The step is load-bearing: at second order the same region does contribute,
and its contribution is exactly what kills the two `c`-channels (report §9). -/

section Borrow

variable {p : ℕ} [Fact p.Prime]

/-- Squareness, low factor: `p ∣ C(n,k) ⟹ p² ∣ A(n,k)`. -/
theorem sq_dvd_A_low {n k : ℕ} (h : ((n.choose k : ℕ) : ZMod p) = 0) : p ^ 2 ∣ A n k := by
  rw [ZMod.natCast_eq_zero_iff] at h
  simpa only [A] using Dvd.dvd.mul_right (pow_dvd_pow_of_dvd h 2) (((n + k).choose k) ^ 2)

/-- Squareness, high factor: `p ∣ C(n+k,k) ⟹ p² ∣ A(n,k)`. -/
theorem sq_dvd_A_high {n k : ℕ} (h : (((n + k).choose k : ℕ) : ZMod p) = 0) : p ^ 2 ∣ A n k := by
  rw [ZMod.natCast_eq_zero_iff] at h
  simpa only [A] using Dvd.dvd.mul_left (pow_dvd_pow_of_dvd h 2) ((n.choose k) ^ 2)

/-- **Borrow region, left-hand side.**  Outside `s ≤ r ∧ c ≤ a ∧ r+s < p` one has
`p² ∣ A(ap+r, cp+s)`. -/
theorem borrow_left {a c r s : ℕ} (hr : r < p) (hs : s < p)
    (h : ¬ (s ≤ r ∧ c ≤ a ∧ r + s < p)) : p ^ 2 ∣ A (a * p + r) (c * p + s) := by
  by_cases hsr : s ≤ r
  · by_cases hca : c ≤ a
    · -- the carry `r + s ≥ p`: the *upper* binomial dies
      have hcarry : p ≤ r + s := by omega
      have hexp : (a + c + 1) * p = a * p + c * p + p := by ring
      refine sq_dvd_A_high (choose_digits_zero (A := a + c + 1) (B := c)
        (ξ := r + s - p) (η := s) (by omega) rfl (by omega) hs (by omega))
    · -- `c > a`: the *lower* binomial dies through `C(a,c) = 0`
      refine sq_dvd_A_low ?_
      have hd := choose_digits (p := p) a c r s hr hs
      rw [Nat.choose_eq_zero_of_lt (by omega : a < c)] at hd
      simpa using hd
  · -- `s > r`: the lower binomial dies through `C(r,s) = 0`
    exact sq_dvd_A_low (choose_digits_zero rfl rfl hr hs (by omega))

/-- **Borrow region, right-hand side.**  Outside `s ≤ r ∧ c ≤ a ∧ r+s < p` one has
`p² ∣ A(a,c)·A(r,s)`. -/
theorem borrow_right {a c r s : ℕ} (hr : r < p) (hs : s < p)
    (h : ¬ (s ≤ r ∧ c ≤ a ∧ r + s < p)) : p ^ 2 ∣ A a c * A r s := by
  by_cases hsr : s ≤ r
  · by_cases hca : c ≤ a
    · have hcarry : p ≤ r + s := by omega
      exact Dvd.dvd.mul_left
        (sq_dvd_A_high (n := r) (k := s) (choose_carry_zero hcarry hs (by omega))) (A a c)
    · have hz : A a c = 0 := by
        simp [A, Nat.choose_eq_zero_of_lt (by omega : a < c)]
      simp [hz]
  · have hz : A r s = 0 := by
      simp [A, Nat.choose_eq_zero_of_lt (by omega : r < s)]
    simp [hz]

/-- **The borrow region contributes nothing at first order.**  Outside the region
`s ≤ r ∧ c ≤ a ∧ r+s < p` the two sides of the digit expansion agree modulo `p²`, both being
`≡ 0`.  (Inside the region the expansion carries the correction `1 + 2p[a·u + c·v]`; that half is
*not* formalized here — see the module note.) -/
theorem borrow_congr {a c r s : ℕ} (hr : r < p) (hs : s < p)
    (h : ¬ (s ≤ r ∧ c ≤ a ∧ r + s < p)) :
    ((A (a * p + r) (c * p + s) : ℕ) : ZMod (p ^ 2))
      = ((A a c * A r s : ℕ) : ZMod (p ^ 2)) := by
  rw [(ZMod.natCast_eq_zero_iff _ _).2 (borrow_left hr hs h),
    (ZMod.natCast_eq_zero_iff _ _).2 (borrow_right hr hs h)]

end Borrow

/-! ## 6. Weak Wolstenholme

`H_{p−1} ≡ 0 (mod p)` for every odd prime.  Mathlib has **no** Wolstenholme congruence of any
kind (checked: no occurrence of the name, and no `H_{p-1}` statement).  The strong form
`H_{p−1} ≡ 0 (mod p²)` (and its companion `H^{(2)}_{p−1} ≡ 0 (mod p)`) is what the write-up
quotes, but the `mod p²` digit expansion only ever uses `p·H_{p−1} ≡ 0 (mod p²)`, i.e. the
**weak** form proved here by the elementary pairing `l ↔ p−l`. -/

theorem two_mul_Harm_pred (p : ℕ) (hp : 2 ≤ p) :
    2 * Harm 1 (p - 1)
      = (p : ℚ) * ∑ j ∈ range (p - 1),
          (1 : ℚ) / (((j + 1 : ℕ) : ℚ) * ((p - 1 - j : ℕ) : ℚ)) := by
  have h1 : Harm 1 (p - 1) = ∑ j ∈ range (p - 1), (1 : ℚ) / ((j : ℚ) + 1) := Harm_one_eq _
  have h2 : Harm 1 (p - 1) = ∑ j ∈ range (p - 1), (1 : ℚ) / ((p : ℚ) - 1 - (j : ℚ)) := by
    rw [h1, ← Finset.sum_range_reflect (fun j => (1 : ℚ) / ((j : ℚ) + 1)) (p - 1)]
    refine Finset.sum_congr rfl fun j hj => ?_
    have hj' : j < p - 1 := Finset.mem_range.1 hj
    have hcast : ((p - 1 - 1 - j : ℕ) : ℚ) = (p : ℚ) - 2 - (j : ℚ) := by
      have hnat : p - 1 - 1 - j + (j + 2) = p := by omega
      have := congrArg (fun t : ℕ => (t : ℚ)) hnat
      push_cast at this
      linarith
    rw [hcast]
    ring_nf
  rw [two_mul]
  nth_rewrite 1 [h1]
  nth_rewrite 1 [h2]
  rw [← Finset.sum_add_distrib, Finset.mul_sum]
  refine Finset.sum_congr rfl fun j hj => ?_
  have hj' : j < p - 1 := Finset.mem_range.1 hj
  have hx : ((j + 1 : ℕ) : ℚ) = (j : ℚ) + 1 := by push_cast; ring
  have hy : ((p - 1 - j : ℕ) : ℚ) = (p : ℚ) - 1 - (j : ℚ) := by
    have hnat : p - 1 - j + (j + 1) = p := by omega
    have := congrArg (fun t : ℕ => (t : ℚ)) hnat
    push_cast at this
    linarith
  rw [hx, hy]
  have hxne : ((j : ℚ) + 1) ≠ 0 := by positivity
  have hyne : ((p : ℚ) - 1 - (j : ℚ)) ≠ 0 := by
    have : (j : ℚ) + 1 ≤ (p : ℚ) - 1 := by
      have : (j : ℚ) + 2 ≤ (p : ℚ) := by exact_mod_cast (by omega : j + 2 ≤ p)
      linarith
    intro hc
    have : (0 : ℚ) < (j : ℚ) + 1 := by positivity
    linarith
  field_simp
  ring

/-- **Weak Wolstenholme.**  `H_{p−1} ≡ 0 (mod p)` for every prime `p > 2`.  Proof: pairing
`l ↔ p−l` gives `2H_{p−1} = p·Σ_{j<p−1} 1/((j+1)(p−1−j))`, whose sum is `p`-integral. -/
theorem wolstenholme_weak {p : ℕ} [Fact p.Prime] (hp : 2 < p) : PDvd p (Harm 1 (p - 1)) := by
  have hPI : PInt p (∑ j ∈ range (p - 1),
      (1 : ℚ) / (((j + 1 : ℕ) : ℚ) * ((p - 1 - j : ℕ) : ℚ))) := by
    refine PInt.sum fun j hj => ?_
    have hj' : j < p - 1 := Finset.mem_range.1 hj
    refine PInt.div PInt.one ?_
    rw [padicNorm.mul, (padicNorm.nat_eq_one_iff (j + 1)).2 (Nat.not_dvd_of_pos_of_lt
        (by omega) (by omega)),
      (padicNorm.nat_eq_one_iff (p - 1 - j)).2 (Nat.not_dvd_of_pos_of_lt (by omega) (by omega)),
      one_mul]
  have hdvd : PDvd p (2 * Harm 1 (p - 1)) := by
    rw [two_mul_Harm_pred p (by omega)]
    simpa using pDvd_p_pow_mul (p := p) (r := 1) one_pos hPI
  have hn2 : padicNorm p (2 : ℚ) = 1 := by
    have h : ¬ p ∣ 2 := Nat.not_dvd_of_pos_of_lt (by norm_num) hp
    simpa using (padicNorm.nat_eq_one_iff (p := p) 2).2 h
  show padicNorm p (Harm 1 (p - 1)) < 1
  have h := hdvd
  rw [show PDvd p (2 * Harm 1 (p - 1)) = (padicNorm p (2 * Harm 1 (p - 1)) < 1) from rfl,
    padicNorm.mul, hn2, one_mul] at h
  exact h

/-! ## 7. The form of `U_r`, `V_r` that the first-order law actually uses

The digit expansion is only available in the region `r+s < p`, so the corollary
(`work/APERY_DEFECT.md` §3.3, paper Corollary 2.4) really produces the *restricted* functionals
`Σ_{s ≤ r, r+s < p}`, whereas `U_r`, `V_r` are defined as `Σ_{s ≤ r}`.  The write-up silently
identifies the two.  The identification is correct, and for the same reason as the borrow lemma:
when `r+s ≥ p` one has `p² ∣ A(r,s)` (squareness) while `v_p(u), v_p(v) ≥ −1`, so each carry term
has `v_p ≥ 1`.  This also shows `U_r` is `p`-integral for `r < p` — which is *not* automatic:
`U_5 = 13276637/10` and `U_7 = 67890874657/70` do have `p` in the denominator for `p = 5, 7`. -/

section Tail

variable {p : ℕ} [Fact p.Prime]

/-- `u(r,s) = H_{r+s} − H_{r−s} = ½ ∂_n log A`. -/
def uu (n k : ℕ) : ℚ := Harm 1 (n + k) - Harm 1 (n - k)

/-- `p·H_m` is `p`-integral as soon as `⌊m/p⌋ < p`. -/
theorem p_mul_Harm_pInt {m : ℕ} (hm : m / p < p) : PInt p ((p : ℚ) * Harm 1 m) := by
  have h := K_descent (p := p) triv_mul (r := 1) one_pos m
  rw [pow_one] at h
  exact PCong.pInt h (PInt.mul (PInt.intCast _) (K_pInt one_pos hm))

omit [Fact p.Prime] in
theorem small_div_lt {x : ℕ} (hx : x < p * p) : x / p < p := Nat.div_lt_of_lt_mul hx

/-- `p·u(r,s)` is `p`-integral for digits `r, s < p`. -/
theorem p_mul_uu_pInt {r s : ℕ} (hr : r < p) (hs : s < p) : PInt p ((p : ℚ) * uu r s) := by
  have hp2 : 2 ≤ p := (Fact.out (p := p.Prime)).two_le
  have h1 : (r + s) / p < p := small_div_lt (by nlinarith)
  have h2 : (r - s) / p < p := small_div_lt (by nlinarith [Nat.sub_le r s])
  have : (p : ℚ) * uu r s = (p : ℚ) * Harm 1 (r + s) - (p : ℚ) * Harm 1 (r - s) := by
    simp only [uu]; ring
  rw [this]
  exact PInt.sub (p_mul_Harm_pInt h1) (p_mul_Harm_pInt h2)

/-- `p·v(r,s)` is `p`-integral for digits `r, s < p`. -/
theorem p_mul_vv_pInt {r s : ℕ} (hr : r < p) (hs : s < p) : PInt p ((p : ℚ) * vv r s) := by
  have hp2 : 2 ≤ p := (Fact.out (p := p.Prime)).two_le
  have h1 : (r + s) / p < p := small_div_lt (by nlinarith)
  have h2 : (r - s) / p < p := small_div_lt (by nlinarith [Nat.sub_le r s])
  have h3 : s / p < p := small_div_lt (by nlinarith)
  have : (p : ℚ) * vv r s
      = (p : ℚ) * Harm 1 (r + s) + (p : ℚ) * Harm 1 (r - s) - 2 * ((p : ℚ) * Harm 1 s) := by
    simp only [vv]; ring
  rw [this]
  exact PInt.sub (PInt.add (p_mul_Harm_pInt h1) (p_mul_Harm_pInt h2))
    (PInt.mul (by simpa using PInt.natCast (p := p) 2) (p_mul_Harm_pInt h3))

/-- **A carry term of `U_r` or `V_r` vanishes mod `p`.**  If `r + s ≥ p` then `p² ∣ A(r,s)`
(squareness) while `v_p` of the harmonic weight is `≥ −1`, so the product has `v_p ≥ 1`. -/
theorem carry_dvd_gen {r s : ℕ} (hr : r < p) (hs : s < p) (hc : p ≤ r + s)
    {w : ℚ} (hw : PInt p ((p : ℚ) * w)) : PDvd p ((A r s : ℚ) * w) := by
  obtain ⟨M, hM⟩ : p ^ 2 ∣ A r s :=
    sq_dvd_A_high (n := r) (k := s) (choose_carry_zero hc hs (by omega))
  have hcast : (A r s : ℚ) * w = (p : ℚ) ^ 1 * ((M : ℚ) * ((p : ℚ) * w)) := by
    rw [show (A r s : ℚ) = ((p ^ 2 * M : ℕ) : ℚ) by exact_mod_cast congrArg (fun t : ℕ => (t : ℚ)) hM]
    push_cast
    ring
  rw [hcast]
  exact pDvd_p_pow_mul one_pos (PInt.mul (PInt.natCast _) hw)

theorem carry_dvd_vv {r s : ℕ} (hr : r < p) (hs : s < p) (hc : p ≤ r + s) :
    PDvd p ((A r s : ℚ) * vv r s) := carry_dvd_gen hr hs hc (p_mul_vv_pInt hr hs)

theorem carry_dvd_uu {r s : ℕ} (hr : r < p) (hs : s < p) (hc : p ≤ r + s) :
    PDvd p ((A r s : ℚ) * uu r s) := carry_dvd_gen hr hs hc (p_mul_uu_pInt hr hs)

/-- **The restricted `V`-channel is `≡ 0 (mod p)`.**  This is the statement the first-order law
actually needs: `V_r = 0` exactly (Theorem `Vsum_eq_zero`), and the terms dropped by the digit
expansion's range restriction are themselves `≡ 0 (mod p)`. -/
theorem V_restricted_dvd {r : ℕ} (hr : r < p) :
    PDvd p (∑ s ∈ (range (r + 1)).filter (fun s => r + s < p), (A r s : ℚ) * vv r s) := by
  classical
  have hsplit := Finset.sum_filter_add_sum_filter_not (range (r + 1))
    (fun s => r + s < p) (fun s => (A r s : ℚ) * vv r s)
  have hfull : ∑ s ∈ range (r + 1), (A r s : ℚ) * vv r s = 0 := Vsum_eq_zero r
  have htail : PDvd p (∑ s ∈ (range (r + 1)).filter (fun s => ¬ r + s < p),
      (A r s : ℚ) * vv r s) := by
    refine PDvd.sum fun s hs => ?_
    simp only [Finset.mem_filter, Finset.mem_range, not_lt] at hs
    exact carry_dvd_vv hr (by omega) hs.2
  have : ∑ s ∈ (range (r + 1)).filter (fun s => r + s < p), (A r s : ℚ) * vv r s
      = -∑ s ∈ (range (r + 1)).filter (fun s => ¬ r + s < p), (A r s : ℚ) * vv r s := by
    rw [hfull] at hsplit; linarith [hsplit]
  rw [this]
  exact PDvd.neg htail

/-- **The restricted `U`-channel agrees with `U_r` mod `p`** — and, as a corollary, `U_r` is
`p`-integral for `r < p`. -/
theorem U_restricted_cong {r : ℕ} (hr : r < p) :
    PCong p (∑ s ∈ (range (r + 1)).filter (fun s => r + s < p), (A r s : ℚ) * uu r s)
      (∑ s ∈ range (r + 1), (A r s : ℚ) * uu r s) := by
  classical
  have hsplit := Finset.sum_filter_add_sum_filter_not (range (r + 1))
    (fun s => r + s < p) (fun s => (A r s : ℚ) * uu r s)
  have htail : PDvd p (∑ s ∈ (range (r + 1)).filter (fun s => ¬ r + s < p),
      (A r s : ℚ) * uu r s) := by
    refine PDvd.sum fun s hs => ?_
    simp only [Finset.mem_filter, Finset.mem_range, not_lt] at hs
    exact carry_dvd_uu hr (by omega) hs.2
  show PDvd p _
  have hdiff : (∑ s ∈ (range (r + 1)).filter (fun s => r + s < p), (A r s : ℚ) * uu r s)
      - ∑ s ∈ range (r + 1), (A r s : ℚ) * uu r s
      = -∑ s ∈ (range (r + 1)).filter (fun s => ¬ r + s < p), (A r s : ℚ) * uu r s := by
    linarith [hsplit]
  rw [hdiff]
  exact PDvd.neg htail

/-- `U_r` is `p`-integral whenever `r < p`. -/
theorem U_pInt {r : ℕ} (hr : r < p) : PInt p (∑ s ∈ range (r + 1), (A r s : ℚ) * uu r s) := by
  classical
  have hsplit := Finset.sum_filter_add_sum_filter_not (range (r + 1))
    (fun s => r + s < p) (fun s => (A r s : ℚ) * uu r s)
  have h1 : PInt p (∑ s ∈ (range (r + 1)).filter (fun s => r + s < p), (A r s : ℚ) * uu r s) := by
    refine PInt.sum fun s hs => ?_
    simp only [Finset.mem_filter, Finset.mem_range] at hs
    refine PInt.mul (PInt.natCast _) ?_
    refine PInt.sub ?_ ?_
    · exact PCong.pInt (PCong.refl _) (by
        have := K_pInt (p := p) (χ := triv) (r := 1) (y := r + s) one_pos hs.2
        simpa [Harm] using this)
    · have hle : r - s ≤ r := Nat.sub_le r s
      have := K_pInt (p := p) (χ := triv) (r := 1) (y := r - s) one_pos (by omega)
      simpa [Harm] using this
  have h2 : PInt p (∑ s ∈ (range (r + 1)).filter (fun s => ¬ r + s < p), (A r s : ℚ) * uu r s) := by
    refine PInt.sum fun s hs => ?_
    simp only [Finset.mem_filter, Finset.mem_range, not_lt] at hs
    exact PDvd.toPInt (carry_dvd_uu hr (by omega) hs.2)
  rw [← hsplit]
  exact PInt.add h1 h2

end Tail

section Sanity

-- `V_n = 0` for `n = 0,…,8`, computed from the definition.
#eval (List.range 9).map Vsum

-- `U_0,…,U_8 = 0, 6, 105, 2219, 104825/2, 13276637/10, 70543291/2, 67890874657/70,
-- 766399019471/28` (paper §1); note the primes `5, 7` in the denominators — `U_r` is `p`-integral
-- only because `r < p` is assumed.
#eval (List.range 9).map (fun r => ∑ s ∈ Finset.range (r + 1), (A r s : ℚ) * uu r s)

end Sanity

end ZetaLucas
