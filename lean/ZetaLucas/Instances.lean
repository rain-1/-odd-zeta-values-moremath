/-
**S4 of task P5c — the two instances of Theorem LB.**

(i) the **minimal Apéry form** for `ζ(3)` (`work/LBW_GENERAL.md` §T3, the "γ" line):

        b_n = Σ_k C(n,k)² C(n+k,k)² · (2·H⁽³⁾_n − H⁽³⁾_k)
        p³ · b_{ap+r} ≡ b_a · a_r   (mod p)     for a < p, r < p;

(ii) **Franel** (`w = 2`, the "A" line):

        A(n) = Σ_k C(n,k)³,     B(n) = Σ_k C(n,k)³ · ((1/4)H⁽²⁾_k + (3/4)H_k(H_k − H_{n−k}))
        p² · B_{ap+r} ≡ B_a · A_r   (mod p)     for a < p, r < p, p ≠ 2.

**SCOPE WARNING.**  The Lean theorems are about the *explicit sums displayed above*.
* That `bMin` is the sequence **defined by Apéry's recurrence** `(n+1)³b_{n+1} = P(n)b_n − n³b_{n−1}`
  with `b₀ = 0`, `b₁ = 6` **IS now formalized**, in `ZetaLucas/MinimalForm.lean`
  (`bMin_eq_bApery`); `bApery_lucas` there restates `bMin_lucas` for that sequence.
  What remains *not* formalized is the equivalence with the classical **double-sum** form
  `Σ_k C(n,k)²C(n+k,k)²(H⁽³⁾_n + Σ_{m≤k}(−1)^{m−1}/(2m³C(n,m)C(n+m,m)))`, which is
  **PROVED ON PAPER** in `work/MINIMAL_FORM_PROOF.md` §5 (Step D, CERT-3…CERT-6).
* That `bFranel` is the second solution of the Franel recurrence is **[VERIFIED numerically
  upstream, NOT formalized]**.
The `#eval` blocks at the end pin both normalisations against the literature values.
-/
import ZetaLucas.TheoremLB
import ZetaLucas.Apery

open Finset

set_option linter.unusedSectionVars false

namespace ZetaLucas

/-! ### The trivial character and untwisted harmonic letters -/

/-- The trivial completely multiplicative function `χ ≡ 1`. -/
def triv : ℕ → ℤ := fun _ => 1

theorem triv_mul : ∀ m n : ℕ, triv (m * n) = triv m * triv n := fun _ _ => by simp [triv]

/-- The truncated zeta value `H^{(r)}_y = Σ_{m=1}^{y} 1/m^r`. -/
def Harm (r y : ℕ) : ℚ := K triv r y

/-- An untwisted harmonic letter `H^{(r)}` with argument form `x`. -/
def letterH (r : ℕ) (hr : 0 < r) (x : ℕ → ℕ → ℕ) : Letter where
  chi := triv
  chi_mul := triv_mul
  deg := r
  deg_pos := hr
  arg := x

@[simp] theorem letterH_val (r : ℕ) (hr : 0 < r) (x : ℕ → ℕ → ℕ) (n k : ℕ) :
    (letterH r hr x).val n k = Harm r (x n k) := rfl

@[simp] theorem letterH_arg (r : ℕ) (hr : 0 < r) (x : ℕ → ℕ → ℕ) (n k : ℕ) :
    (letterH r hr x).arg n k = x n k := rfl

@[simp] theorem letterH_chi (r : ℕ) (hr : 0 < r) (x : ℕ → ℕ → ℕ) (m : ℕ) :
    (letterH r hr x).chi m = 1 := rfl

@[simp] theorem letterH_deg (r : ℕ) (hr : 0 < r) (x : ℕ → ℕ → ℕ) :
    (letterH r hr x).deg = r := rfl

/-- `(a·p + r) / p = a` for a digit `r < p`. -/
theorem digit_div {p a r : ℕ} (hp : 0 < p) (hr : r < p) : (a * p + r) / p = a := by
  rw [mul_comm, Nat.mul_add_div hp, Nat.div_eq_of_lt hr, Nat.add_zero]

/-! ## (i) The minimal Apéry form for ζ(3) -/

/-- Apéry's summand as an integer. -/
def SA (n k : ℕ) : ℤ := (A n k : ℤ)

/-- The letter `H⁽³⁾` at argument `n`. -/
def apLetN : Letter := letterH 3 (by norm_num) (fun n _ => n)
/-- The letter `H⁽³⁾` at argument `k`. -/
def apLetK : Letter := letterH 3 (by norm_num) (fun _ k => k)

/-- Index set, coefficients and monomials of the weight `2H⁽³⁾_n − H⁽³⁾_k`. -/
def apJ : Finset (Fin 2) := Finset.univ
def apC : Fin 2 → ℚ := ![2, -1]
def apMon : Fin 2 → List Letter := ![[apLetN], [apLetK]]

/-- **The minimal closed form for Apéry's `ζ(3)` numerators**
`b_n = Σ_k C(n,k)²C(n+k,k)²(2H⁽³⁾_n − H⁽³⁾_k)`. -/
def bMin (n : ℕ) : ℚ := ∑ k ∈ range (n + 1), (A n k : ℚ) * (2 * Harm 3 n - Harm 3 k)

theorem W_ap (n k : ℕ) : W apJ apC apMon n k = 2 * Harm 3 n - Harm 3 k := by
  simp [W, apJ, apC, apMon, monVal, apLetN, apLetK, Fin.sum_univ_two]
  ring

theorem bMin_eq (n : ℕ) : bMin n = Brow apJ apC apMon SA n := by
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [W_ap]
  simp [SA]

theorem Arow_SA (n : ℕ) : Arow SA n = (apery n : ℤ) := by
  simp [Arow, SA, apery]

theorem apMon_mem {j : Fin 2} {ℓ : Letter} (h : ℓ ∈ apMon j) : ℓ = apLetN ∨ ℓ = apLetK := by
  fin_cases j <;> simp [apMon] at h <;> simp [h]

/-- **Theorem (3) of the odd-zeta program, machine-verified**: the `b`-row Lucas congruence
for the *minimal* Apéry form.

    p³ · b_{a·p + r}  ≡  b_a · a_r   (mod p)          (a < p, r < p, p prime).

Note there is **no `p ≥ 5` hypothesis**: the minimal form's coefficients are the integers
`2, −1`, so the `(H4) coefficient condition` is vacuous.  Compare the informal `T3` of
`work/WARMUP_ZETA3_DWORK.md`, which needs `p ≥ 5` because Apéry's original weight carries
`1/(2m³)`. -/
theorem bMin_lucas {p : ℕ} [Fact p.Prime] {a r : ℕ} (ha : a < p) (hr : r < p) :
    PCong p ((p : ℚ) ^ 3 * bMin (a * p + r)) (bMin a * (apery r : ℚ)) := by
  have hp0 : 0 < p := (Fact.out (p := p.Prime)).pos
  have key := theorem_LB (p := p) (J := apJ) (c := apC) (mon := apMon) (S := SA)
    (w := 3) (χp := 1)
    (H1 := by
      intro a b r s hr hs
      have h := A_digits (p := p) a b r s hr hs
      simp only [SA, Int.cast_natCast]
      exact h)
    (H2 := by
      intro n k h
      simp [SA, A_eq_zero_of_lt h])
    (H3 := by
      intro a b r s hr hs _ _ j hj ℓ hℓ
      rcases apMon_mem hℓ with rfl | rfl
      · simpa [apLetN] using digit_div hp0 hr
      · simpa [apLetK] using digit_div hp0 hs)
    (H4 := by
      intro j hj ℓ hℓ n k hk
      rcases apMon_mem hℓ with rfl | rfl
      · simp [apLetN]
      · simpa [apLetK] using hk)
    (H4c := by
      intro j hj
      fin_cases j
      · show PInt p ((2 : ℚ))
        simpa using PInt.intCast (p := p) 2
      · show PInt p ((-1 : ℚ))
        simpa using PInt.intCast (p := p) (-1))
    (Hw := by intro j hj; fin_cases j <;> simp [apMon, monDeg, apLetN, apLetK])
    (H5 := by intro j hj; fin_cases j <;> simp [apMon, monChi, apLetN, apLetK])
    ha hr
  rw [bMin_eq, bMin_eq, Arow_SA] at *
  simpa using key

/-! ## (ii) Franel -/

/-- Franel's summand `C(n,k)³` as an integer. -/
def SF (n k : ℕ) : ℤ := ((n.choose k) ^ 3 : ℕ)

/-- The Franel numbers `A(n) = Σ_k C(n,k)³` (OEIS A000172). -/
def franel (n : ℕ) : ℕ := ∑ k ∈ range (n + 1), (n.choose k) ^ 3

/-- The letters of the Franel weight: `H⁽²⁾` at `k`, `H⁽¹⁾` at `k`, `H⁽¹⁾` at `n − k`. -/
def frLetK2 : Letter := letterH 2 (by norm_num) (fun _ k => k)
def frLetK1 : Letter := letterH 1 (by norm_num) (fun _ k => k)
def frLetNK1 : Letter := letterH 1 (by norm_num) (fun n k => n - k)

def frJ : Finset (Fin 3) := Finset.univ
def frC : Fin 3 → ℚ := ![1 / 4, 3 / 4, -(3 / 4)]
def frMon : Fin 3 → List Letter := ![[frLetK2], [frLetK1, frLetK1], [frLetK1, frLetNK1]]

/-- The Franel second solution
`B(n) = Σ_k C(n,k)³ ((1/4)H⁽²⁾_k + (3/4)H_k(H_k − H_{n−k}))`. -/
def bFranel (n : ℕ) : ℚ :=
  ∑ k ∈ range (n + 1), (((n.choose k) ^ 3 : ℕ) : ℚ) *
    (1 / 4 * Harm 2 k + 3 / 4 * (Harm 1 k * Harm 1 k) - 3 / 4 * (Harm 1 k * Harm 1 (n - k)))

theorem W_fr (n k : ℕ) : W frJ frC frMon n k
    = 1 / 4 * Harm 2 k + 3 / 4 * (Harm 1 k * Harm 1 k) - 3 / 4 * (Harm 1 k * Harm 1 (n - k)) := by
  simp [W, frJ, frC, frMon, monVal, frLetK2, frLetK1, frLetNK1, Fin.sum_univ_three]
  ring

theorem bFranel_eq (n : ℕ) : bFranel n = Brow frJ frC frMon SF n := by
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [W_fr]
  simp [SF]

theorem Arow_SF (n : ℕ) : Arow SF n = (franel n : ℤ) := by
  simp [Arow, SF, franel]

theorem frMon_mem {j : Fin 3} {ℓ : Letter} (h : ℓ ∈ frMon j) :
    ℓ = frLetK2 ∨ ℓ = frLetK1 ∨ ℓ = frLetNK1 := by
  fin_cases j <;> simp [frMon] at h <;> tauto

/-- **Franel instance of Theorem LB.**  `p² · B_{a·p+r} ≡ B_a · A_r (mod p)` for `a, r < p`
and any odd prime `p`.  (`p ≠ 2` is needed only for the coefficient denominators `4`;
`work/LBW_GENERAL.md` states this instance for `p ≥ 5`, which is not necessary.) -/
theorem bFranel_lucas {p : ℕ} [Fact p.Prime] (hp2 : p ≠ 2) {a r : ℕ} (ha : a < p) (hr : r < p) :
    PCong p ((p : ℚ) ^ 2 * bFranel (a * p + r)) (bFranel a * (franel r : ℚ)) := by
  have hpp : p.Prime := Fact.out
  have hp0 : 0 < p := hpp.pos
  have hp4 : ¬ (p : ℤ) ∣ 4 := by
    intro hdvd
    have h4 : p ∣ 4 := by exact_mod_cast hdvd
    have h2 : p ∣ 2 ^ 2 := by rw [show (2 : ℕ) ^ 2 = 4 by norm_num]; exact h4
    exact hp2 ((Nat.prime_dvd_prime_iff_eq hpp Nat.prime_two).1 (hpp.dvd_of_dvd_pow h2))
  have key := theorem_LB (p := p) (J := frJ) (c := frC) (mon := frMon) (S := SF)
    (w := 2) (χp := 1)
    (H1 := by
      intro a b r s hr hs
      have h := choose_digits (p := p) a b r s hr hs
      simp only [SF]
      push_cast
      rw [h]; ring)
    (H2 := by
      intro n k h
      simp [SF, Nat.choose_eq_zero_of_lt h])
    (H3 := by
      intro a b r s hr hs hba hne j hj ℓ hℓ
      -- `S(r,s) ≢ 0` forces `s ≤ r`, i.e. no borrow in `n − k`
      have hsr : s ≤ r := by
        by_contra hcon
        exact hne (by simp [SF, Nat.choose_eq_zero_of_lt (by omega : r < s)])
      rcases frMon_mem hℓ with rfl | rfl | rfl
      · simpa [frLetK2] using digit_div hp0 hs
      · simpa [frLetK1] using digit_div hp0 hs
      · have hbp : b * p ≤ a * p := Nat.mul_le_mul_right p hba
        have hsub : (a - b) * p = a * p - b * p := Nat.sub_mul a b p
        have e : (a * p + r) - (b * p + s) = (a - b) * p + (r - s) := by omega
        simpa [frLetNK1, e] using digit_div hp0 (show r - s < p by omega))
    (H4 := by
      intro j hj ℓ hℓ n k hk
      rcases frMon_mem hℓ with rfl | rfl | rfl
      · simpa [frLetK2] using hk
      · simpa [frLetK1] using hk
      · simp [frLetNK1])
    (H4c := by
      intro j hj
      fin_cases j
      · show PInt p ((1 : ℚ) / 4)
        simpa using PInt.intCast_div (p := p) (a := 1) (b := 4) hp4
      · show PInt p ((3 : ℚ) / 4)
        simpa using PInt.intCast_div (p := p) (a := 3) (b := 4) hp4
      · show PInt p (-((3 : ℚ) / 4))
        exact PInt.neg (by simpa using PInt.intCast_div (p := p) (a := 3) (b := 4) hp4))
    (Hw := by intro j hj; fin_cases j <;> simp [frMon, monDeg, frLetK2, frLetK1, frLetNK1])
    (H5 := by intro j hj; fin_cases j <;> simp [frMon, monChi, frLetK2, frLetK1, frLetNK1])
    ha hr
  rw [bFranel_eq, bFranel_eq, Arow_SF] at *
  simpa using key

/-! ### Numeric normalisation checks (evaluated, not kernel-checked) -/

section Sanity

-- `b_n = 0, 6, 351/4, 62531/36, 11424695/288, …` — the classical Apéry ζ(3) numerators.
#eval (List.range 6).map bMin

-- Franel numbers `1, 2, 10, 56, 346, 2252` (OEIS A000172).
#eval (List.range 6).map franel

-- Franel second solution `0, 1, 4, 208/9, 1280/9` — matches the (R2) recurrence
-- `(n+1)²B_{n+1} = (7n²+7n+2)B_n + 8n²B_{n−1}` with `B(0)=0`, `B(1)=1`.
#eval (List.range 5).map bFranel

/-- `padicNorm p x < 1` ⟺ `p ∣ num x` and `p ∤ den x`; an evaluable form of `PDvd p x`. -/
def pDvdCheck (p : ℕ) (x : ℚ) : Bool := (x.num % (p : ℤ) == 0) && (x.den % p != 0)

-- Independent numeric confirmation of `bMin_lucas` over all cells `a, r < p`.  Prints `true`.
-- (Also verified off-line for `p = 11, 13`.)
#eval [5, 7].all fun p => (List.range p).all fun a => (List.range p).all fun r =>
  pDvdCheck p ((p : ℚ) ^ 3 * bMin (a * p + r) - bMin a * (apery r : ℚ))

-- Independent numeric confirmation of `bFranel_lucas`.  Prints `true`.
#eval [5, 7].all fun p => (List.range p).all fun a => (List.range p).all fun r =>
  pDvdCheck p ((p : ℚ) ^ 2 * bFranel (a * p + r) - bFranel a * (franel r : ℚ))

-- Sharpness: at `p = 5, a = r = 1` the difference is `103188530395/32`, of `5`-valuation
-- exactly `1` — the floor of the master form is exactly `w`, never more.
#eval ((5 : ℚ) ^ 3 * bMin (1 * 5 + 1) - bMin 1 * (apery 1 : ℚ))

end Sanity

end ZetaLucas
