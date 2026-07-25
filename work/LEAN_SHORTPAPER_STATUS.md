# Lean 4 formalization status — short-paper targets

**Agent:** lean-formalization-agent (River's odd-zeta program)
**Date:** 2026-07-25
**Project:** `/home/ubuntu/fable-episode-2/zeta-math-2/lean/`
**Toolchain:** `leanprover/lean4:v4.33.0-rc1`, Mathlib rev `cd580e54f1a6b46063824e80cec92f64692cbe78`
**Predecessors:** `work/LEAN_LUCAS_STATUS.md` (P5/P5b), `work/LEAN_LBWCHI_STATUS.md` (P5c).
**Sources followed:** `work/MINIMAL_FORM_PROOF.md` §§0–4 (Target 1); the printed value of
Brown–Zudilin arXiv:2210.03391 (Target 2).

---

## HEADLINE

| target | status |
|---|---|
| **T1** `b_n = Σ_k C(n,k)²C(n+k,k)²(2H⁽³⁾_n − H⁽³⁾_k)` for Apéry's companion `b_n` | **DONE, 0 sorries, axioms clean** |
| **T1′** `b`-row Lucas congruence restated for the classical `b_n` | **DONE, 0 sorries** (free corollary) |
| **T2** Brown–Zudilin factor-12 refutation at `n = 2` | **DONE, 0 sorries, axioms clean** |

`lake build` is clean and was run. **Clean rebuild of all ten `ZetaLucas` modules: 37 s**
(Mathlib prebuilt, not recompiled). `grep -rn "sorry\|native_decide" ZetaLucas/` returns nothing
(the only hit is the English word "admit" inside a comment in `Kummer.lean`).

```
'ZetaLucas.absorb'                        depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.absorb2'                       depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.l0a'                           depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.l0b'                           depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.l0c'                           depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.l0d'                           depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.propB'                         depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.propC'                         depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.star'                          depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.bMin_rec'                      depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.bApery_rec'                    depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.bMin_eq_bApery'                depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.apery_b_harmonic_closed_form'  depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.Harm_eq'                       depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.bApery_lucas'                  depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.dlcm_two'                      does not depend on any axioms
'ZetaLucas.dlcm_two_pow_five'             depends on axioms: [propext]
'ZetaLucas.BZ_d2_pow_five_mul_P2'         depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZ_P2_not_integral'            depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZ_P2_factor_twelve'           depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZ_twelve_minimal'             depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.bMin_lucas'                    depends on axioms: [propext, Classical.choice, Quot.sound]   (unchanged)
```

No `native_decide`, no `Lean.ofReduceBool`, no `sorryAx`.

### File map (new modules in **bold**)

```
/home/ubuntu/fable-episode-2/zeta-math-2/lean/
├── ZetaLucas.lean                    root import file (10 modules)
└── ZetaLucas/
    ├── Core.lean              105 L
    ├── Apery.lean             140 L   A, apery, A_digits, apery_lucas          [P5 THM 1]
    ├── BrownZudilin.lean      221 L   T, Q, T_digits, Q_lucas                  [P5 THM 2]
    ├── PadicBridge.lean       218 L   PInt / PDvd / PCong + ZMod bridge
    ├── Letters.lean           237 L   K, Lemma K, Letter, mon_descent
    ├── TheoremLB.lean         236 L   W, Arow, Brow, theorem_LB
    ├── Instances.lean         276 L   bMin_lucas, bFranel_lucas
    ├── Kummer.lean            110 L   K1–K4 two/three-digit Kummer
    ├── **MinimalForm.lean**   477 L / ~330 code — Lemma 0, CERT-1, CERT-2,
    │                                    bMin_rec, bApery, bMin_eq_bApery       [T1]
    └── **BZFactor12.lean**     87 L / ~45 code — dlcm, BZ_P2_not_integral      [T2]
```

**New code this session: 564 lines / ≈ 375 code lines, 4 build iterations, ≈ 2 h wall clock.**

---

## T1 — the harmonic closed form for `b_n`  [`ZetaLucas/MinimalForm.lean`]

### The statements, verbatim

```lean
/-- Apéry's second solution, DEFINED by his recurrence. -/
def bApery : ℕ → ℚ
  | 0 => 0
  | 1 => 6
  | (n + 2) => (Ppol ((n : ℚ) + 1) * bApery (n + 1) - ((n : ℚ) + 1) ^ 3 * bApery n)
      / ((n : ℚ) + 2) ^ 3
-- Ppol n = 34n³ + 51n² + 27n + 5

theorem bApery_rec (n : ℕ) :
    ((n : ℚ) + 2) ^ 3 * bApery (n + 2)
      = Ppol ((n : ℚ) + 1) * bApery (n + 1) - ((n : ℚ) + 1) ^ 3 * bApery n

/-- MAIN THEOREM (compact form). -/
theorem bMin_eq_bApery (n : ℕ) : bMin n = bApery n
--   where  bMin n = ∑ k ∈ range (n+1), (A n k : ℚ) * (2 * Harm 3 n - Harm 3 k)
--          A n k  = C(n,k)² C(n+k,k)²          (the existing `Apery.lean` definition)

/-- MAIN THEOREM (fully written out; no auxiliary definitions in the statement). -/
theorem apery_b_harmonic_closed_form (n : ℕ) :
    ∑ k ∈ range (n + 1),
        ((n.choose k : ℚ) ^ 2 * (((n + k).choose k : ℚ)) ^ 2)
          * (2 * (∑ j ∈ Finset.Icc 1 n, (1 : ℚ) / (j : ℚ) ^ 3)
              - ∑ j ∈ Finset.Icc 1 k, (1 : ℚ) / (j : ℚ) ^ 3)
      = bApery n

/-- The intermediate result: the explicit sum satisfies Apéry's recurrence. -/
theorem bMin_rec (m : ℕ) :
    ((m : ℚ) + 2) ^ 3 * bMin (m + 2) - Ppol ((m : ℚ) + 1) * bMin (m + 1)
      + ((m : ℚ) + 1) ^ 3 * bMin m = 0

/-- COROLLARY (T1′): the `b`-row Lucas congruence, now about the classical sequence. -/
theorem bApery_lucas {p : ℕ} [Fact p.Prime] {a r : ℕ} (ha : a < p) (hr : r < p) :
    PCong p ((p : ℚ) ^ 3 * bApery (a * p + r)) (bApery a * (apery r : ℚ))
```

`bApery_lucas` is the point of the exercise: `Instances.bMin_lucas` was a theorem about an
explicit harmonic sum; transported along `bMin_eq_bApery` it becomes a theorem about the sequence
defined by Apéry's recurrence, i.e. about a classical object.

### How the proof was organized (and the one structural improvement over the write-up)

The write-up's route R1 needs only **Theorem 1** (`L[B_min] = 0`) once `b_n` is *defined* by the
recurrence — Step D (CERT-3…CERT-6, the classical double sum) is not on the critical path. So the
formalization is §§0–4 of `MINIMAL_FORM_PROOF.md` only.

1. **Two absorption identities over ℚ**, valid for **all** `k ≥ 0` (`absorb`, `absorb2`):
   `C(N+1,k)(N+1−k) = (N+1)C(N,k)` and `C(N,k+1)(k+1) = C(N,k)(N−k)`.
   Both come from Mathlib's `Nat.choose_mul_succ_eq` / `Nat.choose_succ_right_eq`; the `k > N`
   branch is "both sides are 0". *This is where the write-up's claim that Lemma 0 removes every
   boundary subtlety is cashed*: the ℕ-subtraction `N+1−k` is converted to ℚ-subtraction only on
   the branch `k ≤ N+1`, and the other branch never needs it.
2. **Lemma 0(a)–(d)** (`l0a`–`l0d`), with `n = m+1` throughout so no natural subtraction ever
   appears in a statement, and
   `Φ(m,k) = (C(m+2,k)·C(m+k,k))² / ((m+1)²(m+2)²)`.
   Each is `rw [div_mul_eq_mul_div, eq_div_iff …]` followed by one `linear_combination` of two
   squared absorption identities. **10–14 lines each.**
3. **CERT-1 → `propB`, CERT-2 → `propC`.** After Lemma 0 both sides are `Φ(m,k)` times a
   polynomial in `ℚ[m,k]`, and `Φ(m,k)` is an *atom* for `ring` (it is a `def`, never unfolded).
   Both proofs are literally four lines ending in `ring`. `propC` additionally clears the
   `1/Den m` by `div_sub_div_same` + `eq_div_iff (Den_ne m)` — **no `field_simp` is needed
   anywhere in the certificate work.**
4. **THE STRUCTURAL IMPROVEMENT — one telescope instead of Abel summation.** The task brief
   (and the write-up, §3) expected "the telescoping bookkeeping to be the real labour": Abel
   summation of `Σ w(n,k)(G(n,k+1) − G(n,k))`, boundary terms, then a second telescope for
   Proposition C. **None of that is needed.** Setting

   ```lean
   def Wt  (m k : ℕ) : ℚ := 2 * Harm 3 (m + 1) - Harm 3 k
   def Psi (m k : ℕ) : ℚ := Wt m k * Gfun m k + Kfun m k + Gdfun m k
   ```

   the `k`-summand of `(L b_min)(m+1)` is *exactly* `Ψ(m,k+1) − Ψ(m,k)` (`star`), because
   `w(n,k) G(n,k+1) = w(n,k+1) G(n,k+1) + Gd(n,k+1)` (that is Abel's step, but pointwise,
   using `G(n,k+1) = Gd(n,k+1)(k+1)³` and `H⁽³⁾_{k+1} − H⁽³⁾_k = 1/(k+1)³`). So the whole sum
   collapses under a single `Finset.sum_range_sub`, and the only boundary facts are
   `Ψ(m,0) = 0` (factor `k`) and `Ψ(m,m+3) = 0` (factor `C(m+2,k)² = 0` for `k = m+3`),
   both one-line `simp`s. **`bMin_rec` is 11 lines.**
5. **Two-step induction** (`bMin_eq_bApery`): a plain
   `∀ n, bMin n = bApery n ∧ bMin (n+1) = bApery (n+1)` induction; the step is
   `mul_left_cancel₀` against `((n:ℚ)+2)³ ≠ 0` — the "leading coefficient never vanishes"
   remark of the write-up, made explicit. Initial values: `bMin 0 = 0`, `bMin 1 = 6` by `norm_num`.

### Independent numerical confirmation (in the build)

```
#eval (List.range 7).map bApery
  ⟹ [0, 6, 351/4, 62531/36, 11424695/288, 35441662103/36000, 20637706271/800]
#eval (List.range 7).map bMin      ⟹ (identical list)
```
matching `MINIMAL_FORM_PROOF.md` §1 (`B_min(1..3,5) = 6, 351/4, 62531/36, 35441662103/36000`).
Kernel-checked (`norm_num`, not `#eval`): `bApery 2 = 351/4`, `bApery 3 = 62531/36`,
`bMin 2 = 351/4`.

### Measured effort

| piece | code lines | iterations |
|---|---|---|
| `absorb`, `absorb2`, `abs_a`–`abs_d` | 55 | 2 (wrong Mathlib names: `le_or_lt`, `Nat.succ_mul_choose_eq`) |
| `Phi`, `Den`, `A_cast`, `l0a`–`l0d` | 90 | 1 |
| `Ppol/Tpol/Upol/Gfun/Gdfun/Kfun`, `propB`, `propC` | 60 | 1 (`rw [l0a]` needed explicit args — it was matching `A (m+2) k` first) |
| `Harm_succ`, `Wt`, `Psi`, `star_pre`, `star` | 60 | 1 |
| `bMin_sum_range`, `bMin_rec`, `bApery`, `bMin_eq_bApery`, corollaries | 65 | 1 |

**≈ 330 code lines, 4 build iterations, ≈ 1 h 45 m.** Zero mathematical surprises: CERT-1 and
CERT-2 were re-verified symbolically (sympy, `expand → 0`) before any Lean was written, and both
`ring` calls closed on the first attempt. **Every failure in the session was a Mathlib name or a
`rw` unification order — none was mathematical.**

### What is NOT formalized (T1)

* **The classical double-sum form.** `b_n = Σ_k A(n,k)·c(n,k)` with
  `c(n,k) = H⁽³⁾_n + Σ_{m=1}^k (−1)^{m−1}/(2m³C(n,m)C(n+m,m))` (van der Poorten / Apéry's original
  weight) is **not** formalized. That is `MINIMAL_FORM_PROOF.md` §5 (Step D: Lemmas D1–D6,
  CERT-3…CERT-6, `Top(n) = 5(−1)ⁿC(2n+1,n+1)`, and the residual binomial identity (D-BIN)).
  It is `[PROVED]` on paper. The Lean development instead pins `b_n` by the **recurrence +
  initial values**, which is the standard characterization of the second Apéry solution.
* **`b_n/a_n → ζ(3)`.** No analysis, no limits, no irrationality: nothing about the *value*
  `ζ(3)` occurs anywhere in the Lean development.
* Estimated cost of closing Step D on this toolkit: Lemma D1/D2 are two Gosper certificates of the
  same shape as `propC` (the polynomial identities are `m² + (n+m)(n−m) = n²` and
  `m² + (n+1−m)(n+m+1) = (n+1)²`), Lemma D6 is one more telescope, and Lemma D5 needs
  `C(2n+2,n+1) = 2C(2n+1,n+1)`. The genuinely new labour is that `c(n,k)` is a *nested* sum, so
  the `Σ_m` layer needs its own `Finset.sum_range_sub`. Priced at **≈ 4–6 h** against this
  session's measured rate; it is entirely optional for the paper.

---

## T2 — the Brown–Zudilin factor-12 refutation  [`ZetaLucas/BZFactor12.lean`]

### The statements, verbatim

```lean
def dlcm : ℕ → ℕ                              -- d_n = lcm(1,…,n)
  | 0 => 1
  | (n + 1) => Nat.lcm (n + 1) (dlcm n)

theorem dlcm_two : dlcm 2 = 2 := by decide
theorem dlcm_two_pow_five : dlcm 2 ^ 5 = 32 := by decide

def BZ_P2 : ℚ := 1190161 / 384                -- Brown–Zudilin's OWN PRINTED VALUE, quoted

theorem BZ_d2_pow_five_mul_P2 : ((dlcm 2 ^ 5 : ℕ) : ℚ) * BZ_P2 = 1190161 / 12

theorem BZ_P2_not_integral : ¬ ∃ z : ℤ, ((dlcm 2 ^ 5 : ℕ) : ℚ) * BZ_P2 = (z : ℚ)

theorem BZ_P2_factor_twelve : (12 : ℚ) * (((dlcm 2 ^ 5 : ℕ) : ℚ) * BZ_P2) = 1190161

theorem BZ_twelve_minimal (c : ℕ)
    (h : ∃ z : ℤ, (c : ℚ) * (((dlcm 2 ^ 5 : ℕ) : ℚ) * BZ_P2) = (z : ℚ)) : 12 ∣ c
```

`d₂⁵ = 32` is **computed from `Nat.lcm`**, not hard-coded. `BZ_twelve_minimal` (a free extra) says
the defect is *exactly* `12 = 2²·3`: any integer multiplier that repairs integrality is divisible
by 12 (because `1190161 ≡ 1 (mod 12)`, so `1190161` is coprime to 12).

### Honesty of the statement — read this before citing

The file's header says it, and it must be said in the paper too: **the input `P₂ = 1190161/384` is
Brown–Zudilin's own printed number, taken as a hypothesis.** Nothing about their cellular integral,
its period, or the derivation of `P₂` is formalized, verified, or contradicted. The theorem is:
*given that printed value*, the claim `d_n⁵P_n ∈ ℤ` fails at `n = 2`, and fails by exactly a factor
12. If the printed value contains a typo, these theorems say nothing about the corrected value.

**Measured effort: 45 code lines, 1 build iteration (compiled first try), ≈ 20 min.**

---

## What a paper may honestly claim about the Lean coverage

> Two arithmetic cores of this paper are machine-checked in Lean 4 (Mathlib
> `cd580e54`, toolchain `v4.33.0-rc1`; ≈ 2100 lines, no `sorry`, no `native_decide`, and
> `#print axioms` reports only `propext`, `Classical.choice`, `Quot.sound` on every stated
> result). First, **Theorem [closed form]**: for every `n ≥ 0`,
> `Σ_{k=0}^n C(n,k)²C(n+k,k)²(2H⁽³⁾_n − H⁽³⁾_k) = b_n`, where `b_n` is defined in Lean by Apéry's
> order-2 recurrence `(n+1)³b_{n+1} = (34n³+51n²+27n+5)b_n − n³b_{n−1}` with `b₀ = 0`, `b₁ = 6`
> — i.e. the sequence-theoretic characterization of Apéry's second solution, *not* its classical
> double-sum expression, whose equivalence is proved on paper but is not part of the formal
> development. The formal proof is the certificate proof of §[minimal form]: two absorption
> identities, the four instances of Lemma 0, the two rational certificates CERT-1 and CERT-2
> (each closed by `ring` after Lemma 0), and one telescoping sum. Second, **Theorem
> [Lucas for `b`]**: `p³·b_{ap+r} ≡ b_a·a_r (mod p)` for all primes `p` and all `a, r < p`, now
> stated for that same `b_n`. Third, an arithmetic fact about the value `P₂ = 1190161/384`
> *as printed by Brown and Zudilin*: `d₂⁵·P₂ = 1190161/12 ∉ ℤ` while `12·d₂⁵·P₂ ∈ ℤ`, with `12`
> minimal — so the printed value is incompatible with the stated integrality `d_n⁵P_n ∈ ℤ`,
> by exactly a factor `2²·3`. This last item takes the printed number as a hypothesis; the
> cellular-integral construction that produced it is not formalized, and no claim is made about it
> beyond this arithmetic consequence. Nothing about the *value* `ζ(3)` (limits, irrationality,
> `b_n/a_n → ζ(3)`) is formalized anywhere.

### One-line summary for a referee

Formalized: (i) an explicit harmonic sum equals the solution of a named linear recurrence;
(ii) a mod-`p` congruence for that solution; (iii) a rational-arithmetic contradiction with a
printed constant. Not formalized: any analysis, any period/cellular-integral theory, and the
classical double-sum presentation of `b_n`.
