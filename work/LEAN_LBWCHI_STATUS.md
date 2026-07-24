# Lean 4 formalization status — task P5c (Theorem LB / the general (LB_w^χ) descent)

**Agent:** lean-formalization-agent (River's odd-zeta program)
**Date:** 2026-07-24
**Project:** `/home/ubuntu/fable-episode-2/zeta-math-2/lean/`
**Toolchain:** `leanprover/lean4:v4.33.0-rc1`, Mathlib rev `cd580e54f1a6b46063824e80cec92f64692cbe78`
**Predecessor:** `work/LEAN_LUCAS_STATUS.md` (task P5/P5b), `work/LBW_GENERAL.md` (task P4).

---

## HEADLINE

| target | status |
|---|---|
| **S1(a)** `padicNorm` ↔ `ZMod p` bridge for `p`-integral rationals | **DONE, 0 sorries** |
| **S1(b)** reusable two-digit Kummer module | **DONE, 0 sorries** (not consumed by the theorem — see §S1b) |
| **S2** Lemma K (Frobenius descent of a χ-twisted harmonic letter), Corollary K2 | **DONE, 0 sorries** |
| **S2** statement design of abstract Theorem LB | **DONE** — see §S2 for the three design changes |
| **S3** proof of Theorem LB | **DONE, 0 sorries** |
| **S4(i)** minimal-Apéry instance: `p³·b_{ap+r} ≡ b_a·a_r (mod p)` | **DONE, 0 sorries** |
| **S4(ii)** Franel instance: `p²·B_{ap+r} ≡ B_a·A_r (mod p)` | **DONE, 0 sorries** |
| **S5** `#print axioms`, zero sorries | **DONE** — only `propext, Classical.choice, Quot.sound` |

`lake build` is clean. **Clean rebuild of all eight `ZetaLucas` modules: 34 s** (Mathlib prebuilt,
not recompiled). `grep -rn "sorry\|admit\|native_decide" ZetaLucas/` returns nothing.

```
'ZetaLucas.PCong.of_zmod'                  depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.PCong.mul'                      depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.PCong.sum'                      depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.pDvd_p_pow_mul'                 depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.K_descent'                      depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.K_pInt'                         depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.mon_descent'                    depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.mon_pInt'                       depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.W_descent'                      depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.theorem_LB'                     depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.bMin_lucas'                     depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.bFranel_lucas'                  depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.padicValNat_choose_digits'      depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.padicValNat_add_choose_lt_cube' depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.p_dvd_choose_of_carry'          depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.apery_lucas'                    depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.Q_lucas'                        depends on axioms: [propext, Classical.choice, Quot.sound]
```

### File map (new modules in **bold**)

```
/home/ubuntu/fable-episode-2/zeta-math-2/lean/
├── ZetaLucas.lean                 root import file (8 modules)
└── ZetaLucas/
    ├── Core.lean            105 L / 76 code — sum_range_mul, choose_digits(’),
    │                                          choose_carry_zero, padicValNat_choose_lt_sq
    ├── Apery.lean           140 L /102 code — A, apery, A_digits, apery_lucas      [P5 THM 1]
    ├── BrownZudilin.lean    221 L /168 code — T, Q, T_digits, Q_lucas              [P5 THM 2]
    ├── **PadicBridge.lean** 218 L /139 code — PInt / PDvd / PCong + ZMod bridge    [S1a]
    ├── **Letters.lean**     237 L /168 code — K, Lemma K, Letter, mon_descent      [S2]
    ├── **TheoremLB.lean**   236 L /182 code — W, Arow, Brow, theorem_LB            [S2/S3]
    ├── **Instances.lean**   271 L /185 code — bMin_lucas, bFranel_lucas            [S4]
    └── **Kummer.lean**      110 L / 83 code — K1–K4 two/three-digit Kummer         [S1b]
```

**New code this session: 1072 lines / 757 code lines, 8 build iterations, ≈ 3 h 15 m wall clock.**

---

## The theorems that now exist, verbatim

```lean
-- Letters.lean  — LEMMA K
theorem K_descent {χ : ℕ → ℤ} (hχ : ∀ m n, χ (m * n) = χ m * χ n) {r : ℕ} (hr : 0 < r) (y : ℕ) :
    PCong p ((p : ℚ) ^ r * K χ r y) ((χ p : ℚ) * K χ r (y / p))

-- Letters.lean  — COROLLARY K2
theorem mon_descent {M : List Letter} {n k : ℕ} (h : ∀ ℓ ∈ M, ℓ.arg n k / p < p) :
    PCong p ((p : ℚ) ^ monDeg M * monVal M n k) ((monChi M p : ℚ) * monValDiv p M n k)

-- TheoremLB.lean — THEOREM LB
theorem theorem_LB {J : Finset ι} {c : ι → ℚ} {mon : ι → List Letter}
    {S : ℕ → ℕ → ℤ} {w : ℕ} {χp : ℤ}
    (H1 : ∀ a b r s : ℕ, r < p → s < p →
      ((S (a*p+r) (b*p+s) : ℤ) : ZMod p) = ((S a b : ℤ) : ZMod p) * ((S r s : ℤ) : ZMod p))
    (H2 : ∀ n k : ℕ, n < k → S n k = 0)
    (H3 : ∀ a b r s : ℕ, r < p → s < p → b ≤ a → ((S r s : ℤ) : ZMod p) ≠ 0 →
      ∀ j ∈ J, ∀ ℓ ∈ mon j, ℓ.arg (a*p+r) (b*p+s) / p = ℓ.arg a b)
    (H4 : ∀ j ∈ J, ∀ ℓ ∈ mon j, ∀ n k : ℕ, k ≤ n → ℓ.arg n k ≤ n)
    (H4c : ∀ j ∈ J, PInt p (c j))
    (Hw : ∀ j ∈ J, monDeg (mon j) = w)
    (H5 : ∀ j ∈ J, monChi (mon j) p = χp)
    {a r : ℕ} (ha : a < p) (hr : r < p) :
    PCong p ((p : ℚ) ^ w * Brow J c mon S (a * p + r))
      ((χp : ℚ) * Brow J c mon S a * (Arow S r : ℚ))

-- Instances.lean — S4(i), the b-row for the MINIMAL Apéry form
theorem bMin_lucas {p : ℕ} [Fact p.Prime] {a r : ℕ} (ha : a < p) (hr : r < p) :
    PCong p ((p : ℚ) ^ 3 * bMin (a * p + r)) (bMin a * (apery r : ℚ))
  where  bMin n = ∑ k ∈ range (n+1), (A n k : ℚ) * (2 * Harm 3 n - Harm 3 k)

-- Instances.lean — S4(ii), Franel
theorem bFranel_lucas {p : ℕ} [Fact p.Prime] (hp2 : p ≠ 2) {a r : ℕ} (ha : a < p) (hr : r < p) :
    PCong p ((p : ℚ) ^ 2 * bFranel (a * p + r)) (bFranel a * (franel r : ℚ))
```

`PCong p x y` is defined in `PadicBridge.lean` as `padicNorm p (x - y) < 1`, i.e. `x ≡ y (mod p)`
in `ℤ_(p) ⊆ ℚ`.  (It *implies* `p`-integrality of both sides whenever one side is `p`-integral —
`PCong.pInt` — so the statement is not vacuous.)

---

## S1(a). The `padicNorm` ↔ `ZMod p` bridge  [`PadicBridge.lean`, 139 code lines, ≈ 35 min]

Implements the recommendation of `LEAN_LUCAS_STATUS.md` §S4.1 (option **(C) `padicNorm` on ℚ**).
Three predicates, no new structures, no `PadicInt`:

```lean
def PInt  (p : ℕ) (q : ℚ) : Prop := padicNorm p q ≤ 1     -- q ∈ ℤ_(p)
def PDvd  (p : ℕ) (q : ℚ) : Prop := padicNorm p q < 1     -- q ∈ p·ℤ_(p)
def PCong (p : ℕ) (x y : ℚ) : Prop := PDvd p (x - y)      -- x ≡ y (mod p)
```

API actually consumed downstream (nothing more was proved):
`PInt.{intCast, natCast, zero, one, mul, neg, add, sub, pow, sum, div, intCast_div}`,
`PDvd.{toPInt, zero, neg, add, mul_left, mul_right, sum, of_zmod, toCong}`,
`PCong.{refl, symm, trans, add, pInt, zero_iff, const_mul, mul, sum, of_dvd_dvd, of_zmod}`,
`pInt_p_pow_mul`, `pDvd_p_pow_mul`, `padicNorm_natCast_eq_one`, `padicNorm_intCast_eq_one`.

Three points worth recording.

1. **`PCong.mul` needs `p`-integrality of exactly two of the four operands.**
   `x·y − x'·y' = x·(y − y') + (x − x')·y'`, so `PInt p x` and `PInt p y'` suffice.  Every use
   site in `TheoremLB.lean` has these for free (an integer and a `χ(p)·w(a,b)`).
2. **`padicNorm.sum_lt'` is the right tool** and it is zero-safe (`s = ∅` is handled by the `0 < t`
   argument), which is exactly the failure mode the earlier note predicted for `padicValRat`
   (`padicValRat p 0 = 0` breaks sum induction).  `PCong.sum` is 3 lines.
3. **The bridge is 6 lines**:
   `PCong.of_zmod : (z : ZMod p) = (z' : ZMod p) → PCong p (z:ℚ) (z':ℚ)`, via
   `ZMod.intCast_eq_intCast_iff → Int.ModEq.dvd → padicNorm.int_lt_one_iff`.  It imports
   `A_digits`, `choose_digits` and everything else from `Core.lean`/`Apery.lean` verbatim; this
   is what makes the S4 instances cheap.

`pDvd_p_pow_mul : 0 < r → PInt p x → PDvd p ((p:ℚ)^r * x)` is the single load-bearing valuation
lemma of the whole development — it is what kills the `p ∤ m` layer in Lemma K.

## S1(b). Two-digit Kummer  [`Kummer.lean`, 83 code lines, ≈ 25 min]

**NOT used by `TheoremLB.lean` or `Instances.lean`, and this is the point:** the `(LB_w^χ)` route
replaces the Kummer ledger of the old `T3` proof (Lemma V / T-fact / Tvanish, priced at 5.5 h in
`LEAN_LUCAS_STATUS.md` §S4) by *tameness*.  The module is retained because the ledger is what the
**non-tame** instances (Domb α, ε, s₇, E — the "Lemma-D upgrade" cases of `LBW_GENERAL.md` §T4)
will need.

```lean
theorem padicValNat_choose_digits (ha : a < p) (hr : r < p) (hm : m ≤ a*p+r) :   -- K1
    padicValNat p ((a*p+r).choose m) = if r < m % p then 1 else 0
theorem padicValNat_choose_le_one (hn : n < p^2) (hm : m ≤ n) :
    padicValNat p (n.choose m) ≤ 1
theorem p_dvd_choose_of_carry (hx : x < p) (hy : y < p) (hxy : p ≤ x + y) :      -- K3
    p ∣ (x+y).choose y
theorem padicValNat_choose_mul_p (ha : a < p) (hr : r < p) (hm : j*p ≤ a*p+r) :  -- K4
    padicValNat p ((a*p+r).choose (j*p)) = 0
theorem padicValNat_add_choose_lt_cube (h : n + m < p^3) :                       -- K2
    padicValNat p ((n+m).choose m)
      = (if p^1 ≤ m % p^1 + n % p^1 then 1 else 0) + (if p^2 ≤ m % p^2 + n % p^2 then 1 else 0)
theorem padicValNat_add_choose_le_two (h : n + m < p^3) :
    padicValNat p ((n+m).choose m) ≤ 2
```

**The predicted friction point turned out to be cheap.**  §S4.3 flagged K1 ("ℕ truncated
subtraction under `%`") as *the one real friction point*, ≈ 25 lines.  Measured: **28 lines,
first-try compile.**  The recipe from `T_digits` works verbatim — supply `(a − m₁)*p = a*p − m₁*p`
(`Nat.sub_mul`) and `m₁*p ≤ a*p` (`Nat.mul_le_mul_right`) as hypotheses so `omega` treats the
products as atoms, then everything is linear.  K2 (the `Ico 1 3 = {1,2}` two-carry count) is
**7 lines**, `Finset.filter_insert` + `split_ifs <;> simp_all`, not the 25 predicted.

---

## S2. Statement design — the decisions made

Design was the stated risk concentration, and three changes to the informal §T4 hypotheses were
made.  All three make the theorem *easier to instantiate*, not harder.

### D1. (H1) in "same summand on both sides" form — and (H2) of §T4 **disappears**

§T4 reads:

> **(H1) Lucas/carry dichotomy.** For every k either `p | S(n,k)`, or `S(n,k) ≡ S(a,b)S(r,s)`.
> **(H2) Product region.** The surviving set is `{0 ≤ b ≤ a} × Σ_r` for some `Σ_r ⊆ [0,p)`, and
> `Σ_{s∈Σ_r} S(r,s) ≡ A(r) (mod p)`.

Formalized instead as the single unconditional congruence

```lean
(H1) ∀ a b r s, r < p → s < p → (S (a*p+r) (b*p+s) : ZMod p) = (S a b : ZMod p) * (S r s : ZMod p)
(H2) ∀ n k, n < k → S n k = 0                                      -- vanishing above the diagonal
```

This is the `A_digits` insight of task P5 (`LEAN_LUCAS_STATUS.md` §S2) promoted to a hypothesis:
in the carrying regime *both* sides vanish mod `p`, so the dichotomy is absorbed and the
disjunction never appears.  **Consequence: there is no product-region argument anywhere in the
formalization.**  The double sum factors because `Finset.sum_range_mul` splits a *full* block
`range ((a+1)·p)` and both marginal sums are complete — the extension from `range (n+1)` to the
full block is an equality of integers (H2), not a congruence.  This retires referee item (v)/(2)
of `VERIFY_ZETA3_PROOF.md` for the general theorem, not just for the `a`-row.

The price: (H1) must hold for *all* `a, b`, including the carrying cells.  Verified for both
instances at zero cost (`A_digits` and `choose_digits` are already in that form).

### D2. The "surviving set" of (H3) is made explicit as a side condition on `S(r,s)`

```lean
(H3) ∀ a b r s, r < p → s < p → b ≤ a → (S r s : ZMod p) ≠ 0 →
       ∀ j ∈ J, ∀ ℓ ∈ mon j, ℓ.arg (a*p+r) (b*p+s) / p = ℓ.arg a b
```

`S(r,s) ≢ 0` is precisely what excludes a borrow in an argument like `n − k`: for Franel it gives
`C(r,s) ≠ 0`, hence `s ≤ r`, hence `⌊(n−k)/p⌋ = a − b`.  Stating it this way means the instance
proof *derives* the no-borrow condition instead of having to describe `Σ_r`.

### D3. (H5) χ-homogeneity is stated as a **product of characters**, not a count of χ-letters

§T4: "every monomial of w contains exactly the same number `e ∈ {0,1}` of χ-letters".
Formalized: `∀ j ∈ J, monChi (mon j) p = χp` where `monChi M p = ∏_{ℓ ∈ M} ℓ.chi p`, and the
conclusion carries `χp` (which equals `χ(p)^e` in §T4's situation).  Strictly more general (it
allows mixed conductors as long as the product at `p` is constant), and cheaper to verify — for
the untwisted instances it is `simp`/`rfl`.

### D4. Tameness (H4) is `x(n,k) ≤ n` for `k ≤ n` **only**

The `k > n` part of the block `range ((a+1)p)` is handled by (H2) *exactly* — both sides of the
termwise congruence are literally `0` — so no valuation bound is needed there and (H4) never has
to be checked outside the simplex.  For Apéry the letters are at `{n, k}`; for Franel at
`{k, n−k}`; both are `≤ n` on `k ≤ n` but *not* for `k > n` (`k ≤ n` fails), so this matters.

### D5. The letter system: concrete-minimal, as instructed

```lean
structure Letter where
  chi : ℕ → ℤ ;  chi_mul : ∀ m n, chi (m*n) = chi m * chi n
  deg : ℕ     ;  deg_pos : 0 < deg
  arg : ℕ → ℕ → ℕ
```
A **monomial** is a `List Letter` (so genuine products `H_k·H_{n−k}` are expressible — Franel
needs them); the weight is `W J c mon n k = ∑ j ∈ J, c j * monVal (mon j) n k` over a
`Finset ι`.  Multiplicativity and positivity of the degree are **bundled into the structure**, so
Theorem LB carries no side hypotheses about them and instances build letters with a one-line
`letterH` constructor.  No `DirichletCharacter` is used anywhere, per the brief.

`K χ r y := ∑ m ∈ range (y+1), (χ m : ℚ) / (m:ℚ)^r`.  Using `Finset.range` rather than
`Finset.Icc 1 y` is deliberate: the `m = 0` term is `χ(0)/0^r = 0` in `ℚ` for `r ≥ 1` (this is
why `deg_pos` is bundled), and it makes the `p`-divisible-layer reindexing
`{m ≤ y : p ∣ m} ≅ range (⌊y/p⌋ + 1)` a single `Finset.sum_nbij'` with `m ↦ m/p`, `j ↦ j·p`.
**No `Finset.Icc` reindexing appears in the development** — the piece §S4.4 priced at 3 h and
flagged as the main schedule risk simply does not arise on this route.

**No generalization debt was incurred.**  The abstraction did not fight back (the ≈ 90-min budget
was not reached), so the "single letter list" fallback was not needed: `theorem_LB` is stated for
an arbitrary index type `ι`, arbitrary characters, arbitrary weight `w`, and arbitrary `χp`.

---

## S3. The proof of Theorem LB  [`TheoremLB.lean`, 182 code lines, ≈ 45 min, 3 iterations]

The paper proof really is three lines, and the Lean proof is three blocks.

1. **Lemma K descends each letter.**  `K_descent` (23 lines) splits `range (y+1)` at `p ∣ m` with
   `Finset.sum_filter_add_sum_filter_not`, reindexes the `p`-divisible layer, and observes that
   after multiplication by `p^r` it *equals* `χ(p)·K(⌊y/p⌋)` on the nose (`field_simp; ring`,
   with `j = 0` split off because `0^r = 0`).  The remainder is `p^r·(p-integral)`, killed by
   `pDvd_p_pow_mul`.  `mon_descent` (17 lines) is a `List` induction using `PCong.mul`.
2. **Tameness makes every scaled term `p`-integral, so the carry layer vanishes termwise.**
   `mon_pInt` is `PCong.pInt` applied to `mon_descent`; `pW_pInt` sums it.  In the vanishing
   sublayer `(S r s : ZMod p) = 0`, (H1) gives `(S n k : ZMod p) = 0` and *both* sides are
   `PDvd` — `PCong.of_dvd_dvd` closes it.  No termwise cancellation, no Lemma D.
3. **(H1)+(H2) factor the double sum**, reusing `Finset.sum_range_mul` from `Core.lean` and the
   `Finset.sum_subset` extend-by-zeros pattern from `Apery.lean` (now `Arow_eq_sum_range` /
   `Brow_eq_sum_range`).

Only three build iterations were needed, and all three failures were tactic plumbing, not
mathematics: `Finset.mul_sum`/`Finset.sum_mul` fired on the wrong factor of `χp * (∑) * (∑)`
(fixed by `simp only [mul_sum, sum_mul]; exact Finset.sum_comm`); `simp` left `PCong p 0 0` open;
one `calc` used `≡` notation that does not exist for `PCong`.

---

## S4. The instances

### (i) Minimal Apéry form — a machine-verified `T3`

```lean
def bMin (n : ℕ) : ℚ := ∑ k ∈ range (n+1), (A n k : ℚ) * (2 * Harm 3 n - Harm 3 k)
theorem bMin_lucas [Fact p.Prime] (ha : a < p) (hr : r < p) :
    PCong p ((p:ℚ)^3 * bMin (a*p+r)) (bMin a * (apery r : ℚ))
```

`A n k = C(n,k)²·C(n+k,k)²` and `apery` are the *existing* definitions from `Apery.lean`, so
`(H1)` is `A_digits` composed with `Int.cast_natCast` and `Arow SA r = apery r` is `simp`.
The whole instance is ≈ 35 lines.

**Two sharpenings over the informal `T3` of `WARMUP_ZETA3_DWORK.md`, both consequences of the
minimal form:**

* **No `p ≥ 5` hypothesis.**  The minimal weight's coefficients are the integers `2, −1`, so the
  (H4) coefficient condition is vacuous and the theorem holds for **every** prime, including
  `p = 2, 3`.  `T3` needs `p ≥ 5` only because Apéry's original weight carries `1/(2m³)`.
* **No `1 ≤ a` hypothesis.**  `a = 0` is fine (`bMin 0 = 0`, and `p³·bMin r` is `p`-divisible
  since `bMin r` is `p`-integral for `r < p`).

**SCOPE (stated loudly, as instructed).**  The Lean theorem is about the **explicit sum**
`bMin n = Σ_k C(n,k)²C(n+k,k)²(2H⁽³⁾_n − H⁽³⁾_k)`.  Its equality with the **classical** Apéry
numerator `b_n = Σ_k C(n,k)²C(n+k,k)²(H⁽³⁾_n + Σ_{m≤k}(−1)^{m−1}/(2m³C(n,m)C(n+m,m)))` is
**NOT FORMALIZED HERE**.  (Correction to the task brief, which assumed it was numerical evidence
only: it is in fact `[PROVED]` on paper in `work/MINIMAL_FORM_PROOF.md` §7 — route R1, both halves
closed by six explicit Zeilberger/Gosper certificates CERT-1…CERT-6 verified by exact polynomial
arithmetic.  So the gap between `bMin_lucas` and the literal `T3` statement is a *formalization*
gap, not a mathematical one, and it is a well-scoped one: six rational certificates plus an
induction on the Apéry operator `L`.)  What the formalization *does* provide as independent
evidence is a kernel-independent `#eval` check that `bMin` reproduces the literature values:

```
#eval (List.range 6).map bMin
  ⟹ [0, 6, 351/4, 62531/36, 11424695/288, 35441662103/36000]
```

which is exactly the sequence quoted in `LBW_GENERAL.md` §T3 for the classical `b_n`.

### (ii) Franel

```lean
def bFranel (n : ℕ) : ℚ := ∑ k ∈ range (n+1), ((n.choose k)^3 : ℚ) *
    (1/4 * Harm 2 k + 3/4 * (Harm 1 k * Harm 1 k) - 3/4 * (Harm 1 k * Harm 1 (n-k)))
theorem bFranel_lucas [Fact p.Prime] (hp2 : p ≠ 2) (ha : a < p) (hr : r < p) :
    PCong p ((p:ℚ)^2 * bFranel (a*p+r)) (bFranel a * (franel r : ℚ))
```

This is the first instance to exercise **genuine two-letter monomials** (`H_k·H_k`,
`H_k·H_{n−k}`) and **a non-trivial argument form** (`n − k`, whose digit compatibility needs the
no-borrow condition of D2).  `H1` is `choose_digits` cubed.

**Sharpening:** `LBW_GENERAL.md` §T4 lists Franel as proved for `p ≥ 5`; the Lean proof needs only
`p ≠ 2` (the coefficient denominators are `4`).  Verified: `p = 3` is fine.

Normalisation pinned by `#eval` against the (R2) recurrence
`(n+1)²B_{n+1} = (7n²+7n+2)B_n + 8n²B_{n−1}`, `B(0)=0`, `B(1)=1`:

```
#eval (List.range 6).map franel   ⟹ [1, 2, 10, 56, 346, 2252]      (A000172)
#eval (List.range 5).map bFranel  ⟹ [0, 1, 4, 208/9, 1280/9]        (matches the recurrence)
```

### Independent numeric confirmation of both theorems

`Instances.lean` carries an evaluable form of `PDvd` (`p ∣ num`, `p ∤ den`) and sweeps every cell:

```
#eval [5,7].all fun p => ∀ a < p, ∀ r < p, pDvdCheck p (p^3 * bMin (a*p+r) - bMin a * apery r)  ⟹ true
#eval [5,7].all fun p => ∀ a < p, ∀ r < p, pDvdCheck p (p^2 * bFranel (a*p+r) - bFranel a * franel r) ⟹ true
```

Off-line (not in the build, to keep it under 35 s) the same sweep is `true` for `p = 11, 13`.
Sharpness spot-check: at `p = 5, a = r = 1` the difference is `103188530395/32`, of `5`-valuation
**exactly 1** — the floor is exactly `w`, matching `LBW_GENERAL.md`'s "perfectly flat" finding.

---

## S5. Measured effort vs the estimate

The task brief priced S1 (the "P5b plumbing partial") at **≈ 3 h**.  `LEAN_LUCAS_STATUS.md` §S4
priced the *old* `T3` route at **≈ 13 h ± 4 h**, of which pieces 2+3+5 (Kummer + `padicNorm` glue
+ H-part) were the recommended ≈ 3 h increment.

| stage | estimate | measured | notes |
|---|---|---|---|
| S1(a) `padicNorm`/`ZMod` bridge | 1.0 h (§S4.2 piece 3) | **0.6 h** (139 lines, 2 iterations) | all four Mathlib lemmas were where the inventory said |
| S1(b) two-digit Kummer | 1.5 h (§S4.2 piece 2) | **0.4 h** (83 lines, 1 iteration) | K1 first-try; K2 7 lines not 25 |
| S2 Lemma K + letters + K2 | — (unpriced) | **0.8 h** (168 lines, 2 iterations) | |
| S2 statement design of LB | "risk concentrates here" | **≈ 0.4 h** (inside the S3 figure) | no abort, no specialization needed |
| S3 proof of Theorem LB | — (unpriced) | **0.75 h** (182 lines, 3 iterations) | |
| S4 both instances | — (unpriced) | **0.6 h** (185 lines, 2 iterations) | |
| S5 axioms + status | — | **0.2 h** | |
| **total** | **≈ 3 h for S1 alone** | **≈ 3.25 h for S1–S5** | |

**Throughput: ≈ 3.9 code-lines/min** — between the P5 S2 rate (2.2, unfamiliar API) and the P5 S3
rate (7.5, full toolkit reuse), which is what one would predict for "half new API, half reuse".

**The dominant finding is a schedule fact, not a rate fact.**  `LEAN_LUCAS_STATUS.md` §S4 priced
the `b`-row at 13 h ± 4 h via the `WARMUP_ZETA3` route (Lemma V, T-fact, Tvanish, the
`Finset.Icc` block reindexing, the Kummer ledger — pieces 4 and 6 alone carrying 5.5 h and *all*
the schedule risk).  Via the `LBW_GENERAL` route it cost **≈ 2.2 h** (S2+S3+S4(i)) and produced a
*strictly stronger* result (arbitrary `χ`, arbitrary weight, all primes, `a = 0` allowed, plus a
second sequence for free).  `LBW_GENERAL.md` §T4 Remark 1 claims the new proof "reproves the
WARMUP_ZETA3 T3 theorem in three lines, with no Lemma V, no T-fact, no Kummer ledger" — **this is
now machine-confirmed, and the cost ratio is ≈ 6×.**

---

## What remains (not formalized)

1. **`bMin = b` (minimal vs classical Apéry form).**  `[PROVED on paper —
   work/MINIMAL_FORM_PROOF.md §7 — NOT formalized]`.  This is the single gap between `bMin_lucas`
   and the literal `T3` statement, and it is now purely a formalization task: Lemma 0's six
   binomial conversions, CERT-1…CERT-6 (each an `Expand → 0` polynomial identity, i.e. `ring` in
   Lean), and an induction on the Apéry operator `L` whose leading coefficient `(n+1)³` never
   vanishes.  Independent of everything in this session.
2. **`bFranel` = the second solution of the Franel recurrence.**  Same status.  Formalizing it
   means proving that the explicit sum satisfies `(n+1)²B_{n+1} = (7n²+7n+2)B_n + 8n²B_{n−1}` —
   a creative-telescoping certificate, plausibly the cheapest of the two.
3. **The master form** `v_p(p^w B_n A_q − χ(p) B_q A_n) ≥ w` for all `n` (multi-digit, mod `p^w`
   rather than mod `p`).  `theorem_LB` gives the single-digit mod-`p` statement only; the gap is
   the same one left open on paper (`LBW_GENERAL.md` §T4 Remark 3).  Note `apery_lucas_digits`
   shows the *`a`-row* multi-digit form is a cheap induction — the `b`-row is not, because the
   ratio form has poles.
4. **A twisted instance (`e = 1`).**  Theorem LB's `χp` machinery is proved but never exercised at
   `χp ≠ 1`: per `LBW_GENERAL.md` §T4, the only known twisted sequence (**E**, `χ_{−4}`) is
   **non-tame**, so it needs the Lemma-D upgrade first.  Until then the χ-twist in `theorem_LB` is
   formally correct but untested by an instance.  *A cheap partial test would be to instantiate
   with an artificial tame twisted weight purely to exercise the `monChi` path.*
5. **The non-tame instances** (Domb α, ε, s₇, E).  These need a valuation bound replacing (H4):
   "a Kummer carry in the wide binomial beats the order-1 pole of `H^{(r)}(⌊2k/p⌋)`".
   `Kummer.lean` (S1b) is the toolkit for exactly that and is deliberately kept.
6. **Cooper/Zagier sequences with no known decomposition** (B, C, F, δ, ζ, η, s₁₈) — nothing to
   formalize until a decomposition exists on paper.
