/-
**S2/S3 of task P5c — the abstract Theorem LB** of `work/LBW_GENERAL.md` §T4.

    p^w · B(a·p + r)  ≡  χ(p)^e · B(a) · A(r)   (mod p),      a < p,  r < p,

for `A(n) = Σ_k S(n,k)` and `B(n) = Σ_k S(n,k)·w(n,k)` with `w` a `ℚ`-combination of monomials
in harmonic letters (`ZetaLucas/Letters.lean`).

## Statement-design decisions (differences from the informal §T4)

* **(H1) is stated in the "same summand on both sides" form**
  `S(ap+r, bp+s) ≡ S(a,b)·S(r,s) (mod p)`, with no indicator and no case split.  This is the
  `A_digits` insight of `ZetaLucas/Apery.lean`: in the carrying regime *both* sides vanish mod
  `p`, so the dichotomy "either `p ∣ S` or `S` factors" of §T4 is absorbed into a single
  unconditional congruence.  Consequence: **(H2) of §T4 ("the surviving set is a product
  region `{0 ≤ b ≤ a} × Σ_r` with `Σ_{s∈Σ_r} S(r,s) ≡ A(r)`") disappears entirely**, replaced by
  the far weaker and purely integral
  **(H2) `S(n,k) = 0` for `k > n`** — vanishing above the diagonal.  There is no product-region
  argument anywhere in this file; the double sum factors because `Finset.sum_range_mul` splits
  a *full* block `range ((a+1)·p)` and both marginal sums are complete.
* **(H3)** keeps §T4's digit compatibility, with the "surviving set" made explicit as the side
  condition `S(r,s) ≢ 0 (mod p)` (which is where a borrow in an argument like `n − k` is
  excluded).
* **(H4)** tameness is `x(n,k) ≤ n` for `k ≤ n` only; the `k > n` part of the block is handled
  by (H2) *exactly* (both sides are literally `0`), so no valuation bound is needed there.
* **(H5)** χ-homogeneity is stated as `monChi (mon j) p = χp`, i.e. *the product of the letters'
  characters at `p` is the same for every monomial* — strictly more general than §T4's "every
  monomial contains exactly `e ∈ {0,1}` χ-letters", and cheaper to verify (`decide`/`rfl` in
  the untwisted case).  `χp` plays the role of `χ(p)^e`.

The conclusion is stated with the `ZetaLucas/PadicBridge.lean` API: `PCong p x y` means
`padicNorm p (x − y) < 1`, i.e. `x ≡ y (mod p)` in `ℤ_(p)`.
-/
import ZetaLucas.Letters
import ZetaLucas.Core

open Finset

set_option linter.unusedSectionVars false

namespace ZetaLucas

variable {ι : Type*}

/-- The harmonic weight `w(n,k) = Σ_j c_j · ∏_t K^{(r_{jt})}_{χ_t}(x_{jt}(n,k))`. -/
def W (J : Finset ι) (c : ι → ℚ) (mon : ι → List Letter) (n k : ℕ) : ℚ :=
  ∑ j ∈ J, c j * monVal (mon j) n k

/-- The descended weight, with every argument `x` replaced by `⌊x/p⌋`. -/
def WDiv (p : ℕ) (J : Finset ι) (c : ι → ℚ) (mon : ι → List Letter) (n k : ℕ) : ℚ :=
  ∑ j ∈ J, c j * monValDiv p (mon j) n k

/-- The **first solution** `A(n) = Σ_{k≤n} S(n,k)`. -/
def Arow (S : ℕ → ℕ → ℤ) (n : ℕ) : ℤ := ∑ k ∈ range (n + 1), S n k

/-- The **second solution** `B(n) = Σ_{k≤n} S(n,k)·w(n,k)`. -/
def Brow (J : Finset ι) (c : ι → ℚ) (mon : ι → List Letter) (S : ℕ → ℕ → ℤ) (n : ℕ) : ℚ :=
  ∑ k ∈ range (n + 1), (S n k : ℚ) * W J c mon n k

/-! ### Extending the summation range by vanishing terms -/

theorem Arow_eq_sum_range {S : ℕ → ℕ → ℤ} (H2 : ∀ n k : ℕ, n < k → S n k = 0)
    {n N : ℕ} (h : n + 1 ≤ N) : Arow S n = ∑ k ∈ range N, S n k := by
  refine Finset.sum_subset (fun k hk => Finset.mem_range.2
    (lt_of_lt_of_le (Finset.mem_range.1 hk) h)) ?_
  intro k _ hk
  exact H2 n k (by simpa [Nat.lt_succ_iff, Nat.succ_le_iff] using hk)

theorem Brow_eq_sum_range {J : Finset ι} {c : ι → ℚ} {mon : ι → List Letter} {S : ℕ → ℕ → ℤ}
    (H2 : ∀ n k : ℕ, n < k → S n k = 0) {n N : ℕ} (h : n + 1 ≤ N) :
    Brow J c mon S n = ∑ k ∈ range N, (S n k : ℚ) * W J c mon n k := by
  refine Finset.sum_subset (fun k hk => Finset.mem_range.2
    (lt_of_lt_of_le (Finset.mem_range.1 hk) h)) ?_
  intro k _ hk
  have : S n k = 0 := H2 n k (by simpa [Nat.lt_succ_iff, Nat.succ_le_iff] using hk)
  simp [this]

/-! ### Descent of the weight -/

variable {p : ℕ} [Fact p.Prime]

/-- If every argument descends to `x(a,b)` then the descended weight *is* `w(a,b)`. -/
theorem monValDiv_eq_monVal {M : List Letter} {n k a b : ℕ}
    (h : ∀ ℓ ∈ M, ℓ.arg n k / p = ℓ.arg a b) : monValDiv p M n k = monVal M a b := by
  unfold monValDiv monVal
  congr 1
  exact List.map_congr_left fun ℓ hℓ => by
    simp only [Letter.valDiv, Letter.val, h ℓ hℓ]

theorem WDiv_eq_W {J : Finset ι} {c : ι → ℚ} {mon : ι → List Letter} {n k a b : ℕ}
    (h : ∀ j ∈ J, ∀ ℓ ∈ mon j, ℓ.arg n k / p = ℓ.arg a b) :
    WDiv p J c mon n k = W J c mon a b :=
  Finset.sum_congr rfl fun j hj => by rw [monValDiv_eq_monVal (h j hj)]

/-- **Descent of the weight** (Corollary K2, summed over the monomials). -/
theorem W_descent {J : Finset ι} {c : ι → ℚ} {mon : ι → List Letter} {n k w : ℕ} {χp : ℤ}
    (hc : ∀ j ∈ J, PInt p (c j)) (hdeg : ∀ j ∈ J, monDeg (mon j) = w)
    (hchi : ∀ j ∈ J, monChi (mon j) p = χp)
    (harg : ∀ j ∈ J, ∀ ℓ ∈ mon j, ℓ.arg n k / p < p) :
    PCong p ((p : ℚ) ^ w * W J c mon n k) ((χp : ℚ) * WDiv p J c mon n k) := by
  have e1 : (p : ℚ) ^ w * W J c mon n k
      = ∑ j ∈ J, c j * ((p : ℚ) ^ monDeg (mon j) * monVal (mon j) n k) := by
    rw [W, Finset.mul_sum]
    exact Finset.sum_congr rfl fun j hj => by rw [hdeg j hj]; ring
  have e2 : (χp : ℚ) * WDiv p J c mon n k
      = ∑ j ∈ J, c j * ((monChi (mon j) p : ℚ) * monValDiv p (mon j) n k) := by
    rw [WDiv, Finset.mul_sum]
    exact Finset.sum_congr rfl fun j hj => by rw [hchi j hj]; ring
  rw [e1, e2]
  exact PCong.sum fun j hj => PCong.const_mul (hc j hj) (mon_descent (harg j hj))

/-- `p^w · w(n,k)` is `p`-integral — *tameness*. -/
theorem pW_pInt {J : Finset ι} {c : ι → ℚ} {mon : ι → List Letter} {n k w : ℕ}
    (hc : ∀ j ∈ J, PInt p (c j)) (hdeg : ∀ j ∈ J, monDeg (mon j) = w)
    (harg : ∀ j ∈ J, ∀ ℓ ∈ mon j, ℓ.arg n k / p < p) :
    PInt p ((p : ℚ) ^ w * W J c mon n k) := by
  have e1 : (p : ℚ) ^ w * W J c mon n k
      = ∑ j ∈ J, c j * ((p : ℚ) ^ monDeg (mon j) * monVal (mon j) n k) := by
    rw [W, Finset.mul_sum]
    exact Finset.sum_congr rfl fun j hj => by rw [hdeg j hj]; ring
  rw [e1]
  exact PInt.sum fun j hj => PInt.mul (hc j hj) (mon_pInt (harg j hj))

/-- `w(a,b)` is `p`-integral for digit-sized arguments. -/
theorem W_pInt {J : Finset ι} {c : ι → ℚ} {mon : ι → List Letter} {n k : ℕ}
    (hc : ∀ j ∈ J, PInt p (c j)) (harg : ∀ j ∈ J, ∀ ℓ ∈ mon j, ℓ.arg n k < p) :
    PInt p (W J c mon n k) :=
  PInt.sum fun j hj => PInt.mul (hc j hj) (monVal_pInt (harg j hj))

/-! ### Theorem LB -/

/-- **Theorem LB** (`work/LBW_GENERAL.md` §T4).

For a summand `S` with the base-`p` digit dichotomy (H1) that vanishes above the diagonal (H2),
and a tame (H4) `χ`-homogeneous (H5) harmonic weight of uniform total degree `w`, compatible
with the digits (H3):

    p^w · B(a·p + r)  ≡  χp · B(a) · A(r)   (mod p)      for all a < p, r < p,

where `χp` is the common value of `∏_t χ_t(p)` over the monomials of the weight. -/
theorem theorem_LB {J : Finset ι} {c : ι → ℚ} {mon : ι → List Letter}
    {S : ℕ → ℕ → ℤ} {w : ℕ} {χp : ℤ}
    (H1 : ∀ a b r s : ℕ, r < p → s < p →
      ((S (a * p + r) (b * p + s) : ℤ) : ZMod p)
        = ((S a b : ℤ) : ZMod p) * ((S r s : ℤ) : ZMod p))
    (H2 : ∀ n k : ℕ, n < k → S n k = 0)
    (H3 : ∀ a b r s : ℕ, r < p → s < p → b ≤ a → ((S r s : ℤ) : ZMod p) ≠ 0 →
      ∀ j ∈ J, ∀ ℓ ∈ mon j, ℓ.arg (a * p + r) (b * p + s) / p = ℓ.arg a b)
    (H4 : ∀ j ∈ J, ∀ ℓ ∈ mon j, ∀ n k : ℕ, k ≤ n → ℓ.arg n k ≤ n)
    (H4c : ∀ j ∈ J, PInt p (c j))
    (Hw : ∀ j ∈ J, monDeg (mon j) = w)
    (H5 : ∀ j ∈ J, monChi (mon j) p = χp)
    {a r : ℕ} (ha : a < p) (hr : r < p) :
    PCong p ((p : ℚ) ^ w * Brow J c mon S (a * p + r))
      ((χp : ℚ) * Brow J c mon S a * (Arow S r : ℚ)) := by
  have hp0 : 0 < p := (Fact.out (p := p.Prime)).pos
  set n := a * p + r with hn
  -- `n < p²`, and `⌊n/p⌋ = a`.
  have hnp : n / p = a := by
    rw [hn, mul_comm, Nat.mul_add_div hp0, Nat.div_eq_of_lt hr, Nat.add_zero]
  have hblock : n + 1 ≤ (a + 1) * p := by
    have : (a + 1) * p = a * p + p := by ring
    omega
  -- ### Left-hand side as a double sum over base-`p` digits.
  have hLHS : (p : ℚ) ^ w * Brow J c mon S n
      = ∑ b ∈ range (a + 1), ∑ s ∈ range p,
          (p : ℚ) ^ w * ((S n (b * p + s) : ℚ) * W J c mon n (b * p + s)) := by
    rw [Brow_eq_sum_range H2 hblock, Finset.mul_sum,
      Finset.sum_range_mul (fun k => (p : ℚ) ^ w * ((S n k : ℚ) * W J c mon n k)) (a + 1) p]
  -- ### Right-hand side as the same double sum.
  have hAr : (Arow S r : ℚ) = ∑ s ∈ range p, (S r s : ℚ) := by
    rw [Arow_eq_sum_range H2 (show r + 1 ≤ p by omega)]; push_cast; ring
  have hRHS : (χp : ℚ) * Brow J c mon S a * (Arow S r : ℚ)
      = ∑ b ∈ range (a + 1), ∑ s ∈ range p,
          (χp : ℚ) * ((S a b : ℚ) * W J c mon a b) * (S r s : ℚ) := by
    rw [hAr, Brow]
    simp only [Finset.mul_sum, Finset.sum_mul]
    exact Finset.sum_comm
  rw [hLHS, hRHS]
  -- ### Termwise congruence.
  refine PCong.sum fun b hb => PCong.sum fun s hs => ?_
  have hba : b ≤ a := Nat.lt_succ_iff.1 (Finset.mem_range.1 hb)
  have hsp : s < p := Finset.mem_range.1 hs
  set k := b * p + s with hk
  -- arguments at `(a,b)` are digit-sized
  have hargab : ∀ j ∈ J, ∀ ℓ ∈ mon j, ℓ.arg a b < p := fun j hj ℓ hℓ =>
    lt_of_le_of_lt (H4 j hj ℓ hℓ a b hba) ha
  have hWab : PInt p (W J c mon a b) := W_pInt H4c hargab
  rcases le_or_gt k n with hkn | hkn
  · -- **Main layer** `k ≤ n`: tameness applies.
    have hargnk : ∀ j ∈ J, ∀ ℓ ∈ mon j, ℓ.arg n k / p < p := by
      intro j hj ℓ hℓ
      have h1 : ℓ.arg n k ≤ n := H4 j hj ℓ hℓ n k hkn
      calc ℓ.arg n k / p ≤ n / p := Nat.div_le_div_right h1
        _ = a := hnp
        _ < p := ha
    by_cases hs0 : ((S r s : ℤ) : ZMod p) = 0
    · -- vanishing sublayer: both sides are `≡ 0`
      have hSnk : ((S n k : ℤ) : ZMod p) = 0 := by
        rw [hn, hk, H1 a b r s hr hsp, hs0, mul_zero]
      refine PCong.of_dvd_dvd ?_ ?_
      · rw [show (p : ℚ) ^ w * ((S n k : ℚ) * W J c mon n k)
            = (S n k : ℚ) * ((p : ℚ) ^ w * W J c mon n k) by ring]
        exact PDvd.mul_right (pW_pInt H4c Hw hargnk) (PDvd.of_zmod hSnk)
      · exact PDvd.mul_left
          (PInt.mul (PInt.intCast _) (PInt.mul (PInt.intCast _) hWab)) (PDvd.of_zmod hs0)
    · -- surviving sublayer: (H3) upgrades the descended weight to `w(a,b)`
      have hargeq : ∀ j ∈ J, ∀ ℓ ∈ mon j, ℓ.arg n k / p = ℓ.arg a b :=
        H3 a b r s hr hsp hba hs0
      have hWd : PCong p ((p : ℚ) ^ w * W J c mon n k) ((χp : ℚ) * W J c mon a b) := by
        have := W_descent (p := p) (J := J) (c := c) (mon := mon) (n := n) (k := k)
          (w := w) (χp := χp) H4c Hw H5 hargnk
        rwa [WDiv_eq_W hargeq] at this
      have hSc : PCong p (S n k : ℚ) ((S a b : ℚ) * (S r s : ℚ)) := by
        have h := PCong.of_zmod (p := p) (z := S n k) (z' := S a b * S r s) (by
          push_cast
          rw [hn, hk]
          exact H1 a b r s hr hsp)
        rwa [show (((S a b * S r s : ℤ)) : ℚ) = (S a b : ℚ) * (S r s : ℚ) by push_cast; ring] at h
      have hprod := PCong.mul (p := p) (PInt.intCast (S n k))
        (PInt.mul (PInt.intCast χp) hWab) hSc hWd
      rw [show (p : ℚ) ^ w * ((S n k : ℚ) * W J c mon n k)
            = (S n k : ℚ) * ((p : ℚ) ^ w * W J c mon n k) from by ring,
        show (χp : ℚ) * ((S a b : ℚ) * W J c mon a b) * (S r s : ℚ)
            = ((S a b : ℚ) * (S r s : ℚ)) * ((χp : ℚ) * W J c mon a b) from by ring]
      exact hprod
  · -- **Trivial layer** `k > n`: both sides vanish *exactly* (no valuation argument).
    have hbp : b * p ≤ a * p := Nat.mul_le_mul_right p hba
    have hrs : r < s := by omega
    have h1 : S n k = 0 := H2 n k hkn
    have h2 : S r s = 0 := H2 r s hrs
    rw [h1, h2]
    simp only [Int.cast_zero, zero_mul, mul_zero]
    exact PCong.refl 0

end ZetaLucas
