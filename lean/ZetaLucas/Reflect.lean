/-
# A reflective checker for large polynomial identities in `ℤ[n,k,l]`

**Why this exists.**  `work/LEAN_QROW.md` §4 measures Mathlib's `ring` against the
Brown–Zudilin Q-row certificate: a single identity of 3798 monomials at degrees `(27,11,13)`
exhausts 15 GB in every arrangement tried, because `ring`'s proof term retains every
intermediate monomial (~1 MB per monomial of normal form).  The weight-3 row needs 42 such
identities and the weight-5 row 64, so `ring` is structurally the wrong tool.

**What this is.**  Sparse polynomials as `List ((ℕ × ℕ × ℕ) × ℤ)` in a canonical order, with
`padd`, `smul` and `pmul` written so that **the Lean kernel can reduce them**, and soundness
theorems relating them to evaluation in any commutative ring.  A polynomial identity is then
closed by `rfl` on a `List` — proof term `Eq.refl`, so the memory axis disappears.

`work/LEAN_QROW.md` §13 measures the cost: **≈ 3.5·10³ elementary list steps per second at a
flat ≈ 1.7 GB, independent of problem size.**  The Q-row identity is projected at 3–5 minutes.

**Design points that are measured, not guessed** (`LEAN_QROW.md` §13.3):

* the fuel-driven `mergeAux` is **structural on the fuel**, so the kernel reduces it; `Nat.rec`
  on a literal is O(1) per step, so there is no unary trap;
* `mlt` is built from `Nat.blt`, which the kernel evaluates with GMP;
* packing the exponent triple into a single `ℕ` buys **0 %** — the cost is `List`/`Int` `whnf`
  overhead, not monomial arithmetic — so the readable triple is kept;
* `decide +kernel` is 15 % *slower* than `rfl`;
* `padd` and `pmul` preserve the canonical form, so **no `normalise` is needed**: the final
  check is plain `List` equality.

**`native_decide` is not used here and must never be.**  It would add `ofReduceBool` to
`#print axioms` and void the audited inventory of `work/LEAN_VERIFIED.txt`.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Int.Cast.Lemmas
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace ZetaLucas

namespace Reflect

/-! ## 1.  Representation -/

/-- An exponent triple, for the three variables `n, k, l`. -/
abbrev Mono : Type := ℕ × ℕ × ℕ

/-- A sparse polynomial in `ℤ[n,k,l]`: a list of (exponent triple, coefficient).
The operations below preserve the *canonical form* — strictly increasing in `mlt`, no zero
coefficients — but **soundness does not depend on canonicity**, only on `eval`. -/
abbrev Poly : Type := List (Mono × ℤ)

/-- Lexicographic `<` on exponent triples, via the kernel-accelerated `Nat.blt`. -/
def mlt (a b : Mono) : Bool :=
  if Nat.blt a.1 b.1 then true
  else if Nat.blt b.1 a.1 then false
  else if Nat.blt a.2.1 b.2.1 then true
  else if Nat.blt b.2.1 a.2.1 then false
  else Nat.blt a.2.2 b.2.2

/-- Monomial multiplication: add exponents. -/
def madd (a b : Mono) : Mono := (a.1 + b.1, a.2.1 + b.2.1, a.2.2 + b.2.2)

/-! ## 2.  The operations, all kernel-reducible -/

/-- Merge two polynomials, `fuel`-driven so that the recursion is **structural** and the
kernel can reduce it.  With `fuel ≥ |p| + |q|` this is the usual sorted merge, dropping
monomials whose coefficients cancel. -/
def mergeAux : ℕ → Poly → Poly → Poly
  | 0, _, _ => []
  | _ + 1, [], q => q
  | _ + 1, a :: p, [] => a :: p
  | f + 1, a :: p, b :: q =>
      if a.1 = b.1 then
        (if a.2 + b.2 = 0 then mergeAux f p q else (a.1, a.2 + b.2) :: mergeAux f p q)
      else if mlt a.1 b.1 then a :: mergeAux f p (b :: q)
      else b :: mergeAux f (a :: p) q

/-- Addition. -/
def padd (p q : Poly) : Poly := mergeAux (p.length + q.length) p q

/-- Multiplication by a single monomial `c·x^m`. -/
def smul (m : Mono) (c : ℤ) (p : Poly) : Poly :=
  p.map (fun x => (madd m x.1, c * x.2))

/-- Multiplication.  `foldr`, so the accumulator is built right-to-left and each step merges a
*sparse* `smul m c q` into it — this is the ordering that keeps the cost near-linear
(`LEAN_QROW.md` §13.5). -/
def pmul (p q : Poly) : Poly := p.foldr (fun x acc => padd (smul x.1 x.2 q) acc) []

/-- Negation. -/
def pneg (p : Poly) : Poly := p.map (fun x => (x.1, -x.2))

/-- Subtraction. -/
def psub (p q : Poly) : Poly := padd p (pneg q)

/-! ## 3.  Evaluation into an arbitrary commutative ring -/

variable {R : Type*} [CommRing R]

/-- The value of a monomial. -/
def mval (m : Mono) (n k l : R) : R := n ^ m.1 * k ^ m.2.1 * l ^ m.2.2

/-- The value of a polynomial. -/
def eval : Poly → R → R → R → R
  | [], _, _, _ => 0
  | x :: p, n, k, l => (x.2 : R) * mval x.1 n k l + eval p n k l

@[simp] theorem eval_nil (n k l : R) : eval ([] : Poly) n k l = 0 := rfl

@[simp] theorem eval_cons (x : Mono × ℤ) (p : Poly) (n k l : R) :
    eval (x :: p) n k l = (x.2 : R) * mval x.1 n k l + eval p n k l := rfl

theorem mval_madd (a b : Mono) (n k l : R) :
    mval (madd a b) n k l = mval a n k l * mval b n k l := by
  simp only [mval, madd, pow_add]
  ring

/-! ## 4.  Soundness -/

/-- The merge is sound whenever the fuel suffices.

Note that soundness holds **branch by branch and needs nothing about `mlt`**: the equality test
`a.1 = b.1` is made explicitly, and both of the remaining branches emit a head that is correct
regardless of which of `a`, `b` is smaller.  `mlt` therefore only has to be *some* `Bool`; it is
what makes the output canonical, not what makes it correct.  That keeps this proof free of any
order reasoning. -/
theorem eval_mergeAux (n k l : R) :
    ∀ (f : ℕ) (p q : Poly), p.length + q.length ≤ f →
      eval (mergeAux f p q) n k l = eval p n k l + eval q n k l := by
  intro f
  induction f with
  | zero =>
    intro p q h
    have hp : p = [] := List.eq_nil_of_length_eq_zero (by omega)
    have hq : q = [] := List.eq_nil_of_length_eq_zero (by omega)
    subst hp; subst hq
    simp [mergeAux]
  | succ f ih =>
    intro p q h
    match p, q with
    | [], q => simp [mergeAux]
    | a :: p, [] => simp [mergeAux]
    | a :: p, b :: q =>
      simp only [List.length_cons] at h
      have hbq : p.length + (b :: q).length ≤ f := by simp only [List.length_cons]; omega
      have hap : (a :: p).length + q.length ≤ f := by simp only [List.length_cons]; omega
      have hpq : p.length + q.length ≤ f := by omega
      rw [mergeAux]
      by_cases hab : a.1 = b.1
      · rw [if_pos hab]
        by_cases h3 : a.2 + b.2 = 0
        · rw [if_pos h3, ih p q hpq]
          have hc : ((a.2 : ℤ) : R) * mval b.1 n k l + ((b.2 : ℤ) : R) * mval b.1 n k l = 0 := by
            rw [← add_mul, ← Int.cast_add, h3, Int.cast_zero, zero_mul]
          simp only [eval_cons, hab]
          rw [show ((a.2 : ℤ) : R) * mval b.1 n k l + eval p n k l
                + (((b.2 : ℤ) : R) * mval b.1 n k l + eval q n k l)
              = (((a.2 : ℤ) : R) * mval b.1 n k l + ((b.2 : ℤ) : R) * mval b.1 n k l)
                + (eval p n k l + eval q n k l) from by ring, hc, zero_add]
        · rw [if_neg h3]
          simp only [eval_cons, ih p q hpq, hab]
          push_cast
          ring
      · rw [if_neg hab]
        by_cases h1 : mlt a.1 b.1
        · rw [if_pos h1]
          simp only [eval_cons, ih p (b :: q) hbq]
          ring
        · rw [if_neg h1]
          simp only [eval_cons, ih (a :: p) q hap]
          ring

theorem eval_padd (p q : Poly) (n k l : R) :
    eval (padd p q) n k l = eval p n k l + eval q n k l :=
  eval_mergeAux n k l _ p q le_rfl

theorem eval_smul (m : Mono) (c : ℤ) (p : Poly) (n k l : R) :
    eval (smul m c p) n k l = (c : R) * mval m n k l * eval p n k l := by
  induction p with
  | nil => simp [smul]
  | cons x p ih =>
    simp only [smul, List.map_cons, eval_cons, ih] at *
    rw [mval_madd]
    push_cast
    ring

theorem eval_pmul (p q : Poly) (n k l : R) :
    eval (pmul p q) n k l = eval p n k l * eval q n k l := by
  induction p with
  | nil => simp [pmul]
  | cons x p ih =>
    simp only [pmul, List.foldr_cons] at *
    rw [eval_padd, eval_smul, ih, eval_cons]
    ring

theorem eval_pneg (p : Poly) (n k l : R) : eval (pneg p) n k l = -eval p n k l := by
  induction p with
  | nil => simp [pneg]
  | cons x p ih =>
    simp only [pneg, List.map_cons, eval_cons] at *
    rw [ih]
    push_cast
    ring

theorem eval_psub (p q : Poly) (n k l : R) :
    eval (psub p q) n k l = eval p n k l - eval q n k l := by
  rw [psub, eval_padd, eval_pneg]
  ring

/-! ## 5.  The client interface

`polys_eq` is the one lemma a client needs: if two `Poly` *expressions* are literally the same
list — a fact the **kernel** establishes by `rfl`, with proof term `Eq.refl` — then their
evaluations agree in every commutative ring. -/

/-- **The reflection principle.**  Equal polynomials evaluate equally. -/
theorem eval_congr {p q : Poly} (h : p = q) (n k l : R) : eval p n k l = eval q n k l := by
  rw [h]

/-! ### 5.1  Building blocks for the client side

A client bridges its own expressions to `Poly`s with these; each bridge is a `ring` call on at
most two monomials, which is free.  Large coefficient tables should **not** be bridged by
`ring` — define them as `eval <table>` in the first place (`LEAN_QROW.md` §13.6). -/

/-- The constant polynomial. -/
def pC (c : ℤ) : Poly := if c = 0 then [] else [((0, 0, 0), c)]

/-- The variable `n`. -/
def pN : Poly := [((1, 0, 0), 1)]
/-- The variable `k`. -/
def pK : Poly := [((0, 1, 0), 1)]
/-- The variable `l`. -/
def pL : Poly := [((0, 0, 1), 1)]

@[simp] theorem eval_pC (c : ℤ) (n k l : R) : eval (pC c) n k l = (c : R) := by
  unfold pC
  split_ifs with h
  · simp [h]
  · simp [mval]

@[simp] theorem eval_pN (n k l : R) : eval pN n k l = n := by simp [pN, mval]
@[simp] theorem eval_pK (n k l : R) : eval pK n k l = k := by simp [pK, mval]
@[simp] theorem eval_pL (n k l : R) : eval pL n k l = l := by simp [pL, mval]

/-- Iterated power, by repeated `pmul` — kept structural so the kernel reduces it. -/
def ppow (p : Poly) : ℕ → Poly
  | 0 => pC 1
  | m + 1 => pmul p (ppow p m)

theorem eval_ppow (p : Poly) (m : ℕ) (n k l : R) :
    eval (ppow p m) n k l = (eval p n k l) ^ m := by
  induction m with
  | zero => simp [ppow]
  | succ m ih => simp only [ppow, eval_pmul, ih, pow_succ]; ring

/-! ### 5.2  The two substitutions `k ↦ k+1` and `l ↦ l+1`

Every WZ certificate in this programme evaluates its cofactors at `(n, k+1, l)` and
`(n, k, l+1)`, so the client needs those shifts at the `Poly` level.  They are built out of
the operations already proved sound — `(k+1)^b` is `ppow (padd pK (pC 1)) b` — so the
soundness proofs are two short inductions and no binomial-theorem reasoning is needed. -/

/-- `substK p` is the polynomial `p(n, k+1, l)`.

The `n^a` and `l^c` parts are applied with **`smul`** — one `List.map` — rather than by
`pmul`-ing `ppow pN a` and `ppow pL c`, which would rebuild those powers once per monomial.
On the Q-row table that is ~4·10⁴ `pmul` calls replaced by ~10³ maps
(`work/LEAN_QROW.md` §15.4). -/
def substK (p : Poly) : Poly :=
  p.foldr (fun x acc =>
    padd (smul (x.1.1, 0, x.1.2.2) x.2 (ppow (padd pK (pC 1)) x.1.2.1)) acc) []

/-- `substL p` is the polynomial `p(n, k, l+1)`; same `smul` optimisation. -/
def substL (p : Poly) : Poly :=
  p.foldr (fun x acc =>
    padd (smul (x.1.1, x.1.2.1, 0) x.2 (ppow (padd pL (pC 1)) x.1.2.2)) acc) []

theorem eval_substK (p : Poly) (n k l : R) :
    eval (substK p) n k l = eval p n (k + 1) l := by
  induction p with
  | nil => simp [substK]
  | cons x p ih =>
    simp only [substK, List.foldr_cons] at *
    rw [eval_padd, ih, eval_smul, eval_ppow, eval_padd, eval_pK, eval_pC, eval_cons]
    simp only [mval]
    push_cast
    ring

theorem eval_substL (p : Poly) (n k l : R) :
    eval (substL p) n k l = eval p n k (l + 1) := by
  induction p with
  | nil => simp [substL]
  | cons x p ih =>
    simp only [substL, List.foldr_cons] at *
    rw [eval_padd, ih, eval_smul, eval_ppow, eval_padd, eval_pL, eval_pC, eval_cons]
    simp only [mval]
    push_cast
    ring

/-! ## 6.  The client pattern, worked

This is the shape every certificate block will take.  Note where the work happens: the
`Poly`-level identity is closed by **`rfl`**, i.e. by kernel computation with proof term
`Eq.refl`; `simp only` then transports it along the soundness lemmas; and no `ring` call ever
sees more than a handful of monomials. -/

example (n k l : ℚ) : (n + k) * (n + k) = n * n + 2 * (n * k) + k * k := by
  have hp : psub (pmul (padd pN pK) (padd pN pK))
      (padd (padd (pmul pN pN) (pmul (pC 2) (pmul pN pK))) (pmul pK pK)) = [] := by rfl
  have h := eval_congr (R := ℚ) hp n k l
  simp only [eval_psub, eval_pmul, eval_padd, eval_pN, eval_pK, eval_pC, eval_nil] at h
  push_cast at h
  linear_combination h

/-! ## 7.  Axiom audit -/

section AxiomAudit

#print axioms eval_mergeAux
#print axioms eval_padd
#print axioms eval_smul
#print axioms eval_pmul
#print axioms eval_pneg
#print axioms eval_psub
#print axioms eval_ppow
#print axioms eval_congr
#print axioms eval_substK
#print axioms eval_substL

end AxiomAudit

end Reflect

end ZetaLucas
