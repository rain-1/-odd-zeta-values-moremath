# Lean 4 formalization status — task P5 (Lucas congruences)

**Agent:** lean-formalization-agent (River's odd-zeta program)
**Date:** 2026-07-24
**Project:** `/home/ubuntu/fable-episode-2/zeta-math-2/lean/`
**Toolchain:** `leanprover/lean4:v4.33.0-rc1`, Mathlib rev `cd580e54f1a6b46063824e80cec92f64692cbe78`
(the exact pin of `/home/ubuntu/fable-episode-2/zeta-math/zeta5odd/`, reused read-only).

## HEADLINE

| target | status |
|---|---|
| **(1) a-row Lucas** `a_{ap+r} ≡ a_a·a_r (mod p)` (WARMUP_ZETA3_DWORK.md T2) | **FORMALIZED, 0 sorries, axioms clean** |
| **(2) Q-row Lucas** `Q_{ap+r} ≡ Q_a·Q_r (mod p)` (PROOF_LB5_CAMPAIGN.md Theorem A) | **FORMALIZED, 0 sorries, axioms clean** |
| full Lucas product form `x_n ≡ ∏_i x_{n_i}` for both rows | **FORMALIZED** (bonus, not asked) |
| (3) b-row `p³b_{ap+r} ≡ b_a·a_r (mod p)` (T3) | **not formalized**; costed in §S4 below |

Everything below compiles. `lake build` is clean; clean rebuild of the three modules ≈ 36 s (Mathlib already built, not recompiled).

```
'Finset.sum_range_mul'            depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.choose_digits'         depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.choose_digits''        depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.choose_digits_zero'    depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.choose_carry_zero'     depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.A_digits'              depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.apery_lucas'           depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.apery_lucas_digits'    depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.T_digits'              depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.Q_lucas'               depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.Q_lucas_digits'        depends on axioms: [propext, Classical.choice, Quot.sound]
```

No `native_decide`, no `Lean.ofReduceBool`, no `sorryAx`. Only the three standard Mathlib axioms.

---

## S1. Infrastructure + Mathlib inventory

**Setup (≈ 8 min, well inside the 45-min abort budget).** Disk had 111 G free. Rather than
`lake exe cache get`, the new project's `.lake/packages/*` are **symlinks** into the already-built
`zeta5odd/.lake/packages/` (7.1 G of Mathlib `.olean`s). `lake build` recognises the traces and
rebuilds nothing. First build: 57 s (link + elaborate a one-line file). Nothing is written into the
old repo.

### Mathlib inventory (the key finding)

* **Lucas' theorem IS in Mathlib** — `Mathlib/Data/Nat/Choose/Lucas.lean` (Gareth Ma, 2023).
  It did not need to be reproved. The lemma actually used is the **one-step** form:
  ```
  Choose.choose_modEq_choose_mod_mul_choose_div :
      choose n k ≡ choose (n % p) (k % p) * choose (n / p) (k / p)  [ZMOD p]     -- [Fact p.Prime]
  ```
  (plus `..._nat`, the full-digit `lucas_theorem`, and `choose_pow_mul_pow_mul_modEq_choose`).
  The one-step form is *exactly* "Lemma 1 (Lucas step)" of both write-ups, so `ZetaLucas.choose_digits`
  is a 12-line specialization computing `(a*p+r) % p = r`, `(a*p+r)/p = a`.
  Mathlib proves it by the `(1+X)^p ≡ 1+X^p` route the task anticipated
  (`add_pow_eq_mul_pow_add_pow_div_char` in `(ZMod p)[X]`); `add_pow_char` itself does *not* exist
  under that name in this revision.
* **Kummer's theorem IS in Mathlib** — `Mathlib/NumberTheory/Padics/PadicVal/Basic.lean`:
  ```
  padicValNat_choose  (hkn : k ≤ n) (hnb : log p n < b) :
      padicValNat p (n.choose k) = #{i ∈ Finset.Ico 1 b | p ^ i ≤ k % p ^ i + (n - k) % p ^ i}
  padicValNat_choose' (hnb : log p (n + k) < b) :
      padicValNat p ((n + k).choose k) = #{i ∈ Finset.Ico 1 b | p ^ i ≤ k % p ^ i + n % p ^ i}
  sub_one_mul_padicValNat_choose_eq_sub_sum_digits'   -- digit-sum form
  ```
  Not needed for (1) or (2); load-bearing for (3).
* **`padicNorm` / `padicValRat`** (for (3)): `padicNorm.mul`, `padicNorm.div` are **unconditional**
  (no `≠ 0` side conditions), `padicNorm.sum_le'` is zero-safe and needs no `Nonempty`,
  `padicNorm.of_int`, `padicNorm.dvd_iff_norm_le`, `padicNorm.int_lt_one_iff`,
  `padicValRat.mul/.div/.min_le_padicValRat_add/.sum_pos_of_pos`.
* **`Finset` tooling**: `Finset.sum_range_add`, `Finset.sum_subset`, `Finset.sum_mul_sum`,
  `Finset.sum_comm`, `Finset.sum_comm'` (dependent inner range — the exact tool for T3's interchange),
  `Finset.mul_sum`, `Finset.sum_mul`. **Missing**: any "`range (m*n)` → double sum" reindexing lemma;
  written here as `Finset.sum_range_mul` (5 lines, induction on `m`).

---

## S2. Theorem (1) — a-row Lucas  [`ZetaLucas/Apery.lean`, 140 lines / 89 code lines]

```lean
def A (n k : ℕ) : ℕ := (n.choose k) ^ 2 * ((n + k).choose k) ^ 2
def apery (n : ℕ) : ℕ := ∑ k ∈ range (n + 1), A n k

theorem apery_lucas (a r : ℕ) (hr : r < p) :          -- p : ℕ, [Fact p.Prime]
    ((apery (a * p + r) : ℕ) : ZMod p)
      = ((apery a : ℕ) : ZMod p) * ((apery r : ℕ) : ZMod p)

theorem apery_lucas_digits (n : ℕ) :
    ((apery n : ℕ) : ZMod p)
      = ((Nat.digits p n).map (fun d => ((apery d : ℕ) : ZMod p))).prod
```

Uniform in `p` (no `p ≥ 5`), all `a ≥ 0`, matching T2's scope exactly.

### One simplification worth recording

The write-up's Lemma 3 carries an **indicator** `[r+s<p]`. In Lean the indicator is unnecessary and
its removal collapses two of T2's three steps:

```lean
theorem A_digits (a b r s : ℕ) (hr : r < p) (hs : s < p) :
    ((A (a*p+r) (b*p+s) : ℕ) : ZMod p)
      = ((a.choose b ^ 2 * (a+b).choose b ^ 2 : ℕ) : ZMod p) * ((A r s : ℕ) : ZMod p)
```
with `A r s` — *the same summand at the low digits* — on the right. In the carrying regime
`r + s ≥ p` **both** sides vanish mod `p`: the left because
`C(n+k,k) ≡ C(a+b+1,b)·C(r+s−p,s)` and `r < p ⟹ r+s−p < s`; the right because `C(r+s,s) ≡ 0` by the
same carry annihilation. Consequently the write-up's separate step *"every term of `a_r` with
`r+s ≥ p` vanishes mod p"* is **absorbed** into the factorization lemma and never appears again.

### Honest handling of the referee's flagged steps (VERIFY_ZETA3_PROOF.md)

* **Referee item (v)/(2), "the (b,s) region is a product set only after adding vanishing terms".**
  This is the one place where the informal proof waves at a subset relation. In Lean it is
  `apery_eq_sum_range : n + 1 ≤ N → apery n = ∑ k ∈ range N, A n k`, proved by `Finset.sum_subset`
  with the side goal `A n k = 0` for `n < k` (discharged by `Nat.choose_eq_zero_of_lt`). It is
  applied **twice**, and both applications are forced by the type checker:
  - once to extend `range (a*p+r+1) → range ((a+1)*p)` (the full block, so `sum_range_mul` applies);
  - once to extend `range (r+1) → range p` (recovering `a_r` from the low-digit factor).
  There is no residual hand-waving: the completion is an equality of *integers*, not a mod-`p`
  congruence, since `C(r,s) = 0` on the nose.

### Numeric sanity (kernel-checked, in-file)

* `(List.range 6).map apery = [1, 5, 73, 1445, 33001, 819005]` — OEIS A005259, by `decide`.
* `∀ a < 5, ∀ r < 5, apery (5a+r) % 5 = (apery a * apery r) % 5` — by `decide` (includes the
  `p = 5` cells `a_1 = 5 ≡ 0`, `a_3 = 1445 ≡ 0` where the ratio form has poles).
* `#eval` sweep `p ∈ {5,7,11,13}`, `a < 2p` (so multi-digit), `r < p` → prints `true`.

### Measured effort

**89 code lines, ≈ 40 min wall-clock, 4 build iterations.** All four failures were trivial
(`Nat.mul_add_mod` needed `mul_comm`; `Finset.range_subset` in this revision is the
`range n ⊆ s ↔ ∀ x < n, x ∈ s` form; a `congr 1; omega` needed a `(a+b+1)*p = (a+b)*p + p` hint
because `omega` cannot see through the nonlinear product; one `rfl` needed `simp [A]`).
Zero mathematical surprises — the informal T2 proof is faithful.

---

## S3. Theorem (2) — Q-row Lucas  [`ZetaLucas/BrownZudilin.lean`, 221 lines / 150 code lines]

Definition taken from **PROOF_LB5_CAMPAIGN.md §1** (the double sum), *not* the single-sum
`Σ_k C(n,k)²C(n+k,k)` that appears in WARMUP_ZETA3_DWORK.md §T4:

```lean
def T (n k l : ℕ) : ℕ :=
  (n+k).choose n * (n.choose k)^2 * ((n+l).choose n) * (n.choose l)^2 * ((n+k+l).choose n)
def Q (n : ℕ) : ℕ := ∑ k ∈ range (n+1), ∑ l ∈ range (n+1), T n k l

theorem Q_lucas (a r : ℕ) (hr : r < p) :
    ((Q (a * p + r) : ℕ) : ZMod p) = ((Q a : ℕ) : ZMod p) * ((Q r : ℕ) : ZMod p)
theorem Q_lucas_digits (n : ℕ) : ((Q n : ℕ) : ZMod p) = (…product over base-p digits…)
```

**Normalization pinned in-file by `decide`:** `Q 0 = 1 ∧ Q 1 = 21 ∧ Q 2 = 2989`, and
`#eval (List.range 6).map Q = [1, 21, 2989, 714549, 217515501, 76157194521]`.
`Q₁ = 21` agrees with the value the task supplied, confirming the double-sum reading.

### The double-carry lemma, and where the real content sits

`T_digits` is again indicator-free: `T(N,k,l) ≡ T(a,b,c) · T(r,s,t) (mod p)` for all `a,b,c` and all
digits `r,s,t < p`. Six cases; four are "both sides are 0". The non-trivial one is exactly Lemma 3 of
Theorem A:

```lean
  -- surviving regime: s ≤ r, t ≤ r, r+s < p, r+t < p
  have hst : s + t < p := by omega
```

The campaign write-up spends a paragraph on this (`s+t ≥ p ⟹ p ≤ s+t ≤ 2r ⟹ r ≥ p/2`, but
`r+s<p, r+t<p ⟹ s+t ≤ 2(p−1−r) < p`). **In Lean it is one `omega` call** — the deduction is pure
linear arithmetic over ℕ once the four hypotheses are in context. That single fact is what bounds the
carry `ε ∈ {0,1}` and makes `r+s+t−p < r`, killing `C(r+s+t, r)`. Formalization *confirms* the
write-up's claim that this is the step that needed an argument, and simultaneously shows it is
cheap once stated precisely.

The write-up's two boundary remarks (product region after adding vanishing terms; independence of
the `(b,c)` and `(s,t)` regions) become `Q_eq_sum_range` (used twice, as in S2) and
`simp only [← Finset.mul_sum, ← Finset.sum_mul]` after one `Finset.sum_comm` to swap the `s` and `c`
sums. Both are machine-checked.

### Measured effort

**150 code lines, ≈ 20 min wall-clock, 1 build iteration for the mathematics** — `T_digits`,
`Q_lucas`, `Q_eq_sum_range` and `Q_lucas_digits` all compiled on the *first* attempt (7.8 s).
The only iterations were on the numeric sanity checks (see below). This is the **toolkit-reuse
dividend**: S3 was ≈ 2× the code of S2 at ≈ ½ the effort, because `choose_digits`,
`choose_digits_zero`, `choose_carry_zero`, `sum_range_mul` and the extend-by-zeros pattern were
already debugged.

### One practical trap (recorded for future numeric checks)

`Nat.choose` is the unmemoized Pascal recursion. `#eval` is fine (compiled, seconds up to `n ≈ 340`
for `apery`), but `decide` runs it in the **kernel** and blows up: a `decide` sweep of `Q` at
`p = 11, a < 22` (i.e. `n ≤ 241`, binomials near `C(482,241)`) did not terminate in 10 minutes and
had to be killed. Kernel checks for `Q` are kept at `p = 5, a < 3` (6.6 s); `#eval` covers
`p = 5, a < 6` and prints `true`. `Q` grows fast enough (`Q_5 ≈ 7.6·10^10`) that wider kernel sweeps
are not worth the build time.

---

## S4. Cost plan for theorem (3), the b-row  [T3 of WARMUP_ZETA3_DWORK.md]

> **T3.** For every prime `p ≥ 5`, `1 ≤ a < p`, `0 ≤ r < p`:  `p³ · b_{ap+r} ≡ b_a · a_r (mod p)`,
> where `b_n = Σ_k A(n,k)·( H₃(n) + Σ_{m=1}^k (−1)^{m−1}/(2m³C(n,m)C(n+m,m)) ) ∈ ℚ`.

**Nothing of T3 is formalized.** What follows is a concrete plan, priced against measured S2/S3.

### S4.1 Choice of statement — recommendation: `padicNorm`, in ℚ

Three candidates were considered.

* **(A) Cleared-denominator integers** — state `d_a³·(d_n³ b_n) ≡ (d_n³/p³)·(d_a³ b_a)·a_r (mod p)`
  in ℤ. **Reject.** It requires `d_n³ b_n ∈ ℤ` (global integrality at *every* prime), which is
  `[VERIFIED, not PROVED]` in the program's own notes. T3 only needs *local* `p`-integrality, which
  its proof does establish. Option (A) therefore demands strictly more mathematics than T3.
* **(B) `PadicInt` / `Padic` (ℤ_p, ℚ_p)** — statement via `PadicInt.toZMod : ℤ_p →+* ZMod p`.
  Correct, but every rational must be transported along `ℚ → ℚ_p` and one must first *prove*
  membership in ℤ_p before the residue map is even applicable. Extra plumbing on top of the same
  valuation work.
* **(C) `padicNorm` on ℚ — RECOMMENDED.**
  ```lean
  theorem b_row_lucas {p a r : ℕ} [Fact p.Prime] (hp : 5 ≤ p) (ha : 1 ≤ a) (ha' : a < p) (hr : r < p) :
      padicNorm p ((p : ℚ)^3 * b (a*p+r) - b a * (apery r : ℚ)) ≤ (p : ℚ)⁻¹
  -- companions:
  theorem b_p_integral … : padicNorm p ((p : ℚ)^3 * b (a*p+r)) ≤ 1
  theorem b_small_p_integral … : padicNorm p (b a) ≤ 1
  ```
  Why `padicNorm` and **not** `padicValRat`: (i) `padicNorm.mul` and `padicNorm.div` are
  *unconditional* — no `q ≠ 0` side goals, which in a proof full of `(−1)^{m−1}/(2m³C·C)` terms is
  worth a great deal; (ii) `padicNorm.sum_le'` gives the ultrametric bound for a `Finset` sum with no
  `Nonempty` hypothesis and is **zero-safe**, whereas `padicValRat p 0 = 0` by convention breaks the
  naive induction for `padicValRat`; (iii) `padicNorm.dvd_iff_norm_le` / `padicNorm.int_lt_one_iff`
  convert to and from ℤ-divisibility for the integer sub-objects (`a_n`, `T(n,m)`) that S2 already
  handles in `ZMod p`. A ~10-line bridge `(x : ℤ) → padicNorm p x ≤ p⁻¹ ↔ ((x : ZMod p) = 0)` lets
  the S2 results be imported verbatim.

### S4.2 Piece-by-piece cost

Effort is calibrated on measured throughput: S2 ran at **≈ 2.2 code-lines/min** (89 lines / 40 min,
familiar API), S3 at **≈ 7.5 code-lines/min** (150 / 20, full toolkit reuse). T3 introduces three
areas where measured throughput is **zero**: `padicValNat`/Kummer, `padicNorm` on ℚ, and reindexing
`Finset.Icc` (not `range`) into base-`p` blocks. A 2–3× penalty on the S2 rate (≈ **1 line/min**) is
applied to those; S2/S3-like pieces keep the S3 rate.

| # | piece | new lines | effort | risk | notes |
|---|---|---|---|---|---|
| 0 | ℚ-valued defs `H3, c, w, b, W, Tail` | 20 | 0.3 h | low | mechanical |
| 1 | `b_n = H₃(n)a_n + W(n)`; interchange `W = Σ_m c(n,m)T(n,m)` | 25 | 0.5 h | low | **`Finset.sum_comm'` exists** with exactly the needed dependent-range signature; the iff `(k ∈ range(n+1) ∧ m ∈ Icc 1 k) ↔ (m ∈ Icc 1 n ∧ k ∈ Icc m n)` is one `simp; omega`. **Closes referee item 3** (k=0 drops, swap region) rigorously and cheaply. |
| 2 | Kummer digit lemmas K1–K4 | 70 | 1.5 h | **med** | see S4.3 — partially de-risked by a live probe |
| 3 | `padicNorm` glue: sum bound, quotient bound, ℤ↔`ZMod p` bridge | 45 | 1.0 h | low | all four Mathlib lemmas confirmed present |
| 4 | (T-fact), (T-fact0), (Tvanish) | 110 | **3.0 h** | **high** | see S4.4 — the genuinely new combinatorics |
| 5 | H-part: `p³H₃(n) ≡ H₃(a) (mod p³)`, then `·a_n` | 70 | 1.5 h | low | reuses **`apery_lucas` directly**; needs `Finset.sum_nbij'` for `j ↦ jp` |
| 6 | Lemma V (singular layer, `p ∤ m`) | 90 | **2.5 h** | **high** | see S4.5 |
| 7 | `m = jp` layer: `term_j ≡ a_r τ_j`, two cases | 90 | 2.0 h | med | needs a reusable "perturbed quotient" lemma, used 4× |
| 8 | assembly of (H-part)+(W-part) | 30 | 0.5 h | low | |
| | **total** | **≈ 550** | **≈ 12.8 h** | | |

**Estimate: 13 h ± 4 h of focused work ≈ 1.5–2 sessions**, with pieces 4 and 6 carrying essentially
all the schedule risk. If the `Finset.Icc` block reindexing of piece 4 fights back the way
`Finset.range` did *not*, piece 4 alone could double to 6 h and push the total to ≈ 16 h.

### S4.3 Piece 2 detail — Kummer (probed live, partially de-risked)

The favourable structural fact is that **T3's hypothesis `a < p` means `n = ap+r < p²`, so
`Nat.log p n < 2` and Mathlib's carry-counting `Finset` collapses to a singleton.** This was probed
and **compiles**:

```lean
theorem vp_choose_lt_sq {n k : ℕ} (hn : n < p ^ 2) (hk : k ≤ n) :
    padicValNat p (n.choose k) = if p ≤ k % p + (n - k) % p then 1 else 0 := by
  have hlog : Nat.log p n < 2 := by
    rcases Nat.eq_zero_or_pos n with rfl | h
    · simp
    · exact Nat.log_lt_of_lt_pow (by omega) hn
  rw [padicValNat_choose hk hlog, show Finset.Ico 1 2 = {1} from rfl]
  simp only [Finset.filter_singleton, pow_one]
  split <;> simp
```
**12 lines, sorry-free, and now committed to the project** as
`ZetaLucas.padicValNat_choose_lt_sq` in `ZetaLucas/Core.lean` (not used by (1) or (2); recorded so
this estimate is independently checkable). From it:
* **K1** `v_p C(n,m) = [m mod p > r]` for `n = ap+r`, `m ≤ n` — needs `(n − m) % p` in digit form,
  i.e. `= r − m₀` if `m₀ ≤ r`, else `p + r − m₀`. This is the one real friction point: ℕ truncated
  subtraction under `%`. Same technique as `T_digits` (supply `(a−m₁)*p = a*p − m₁*p` hints so
  `omega` treats the products as atoms). **≈ 25 lines.** *This is exactly where referee item 1 lives*
  (`m₀ > r ⟹ m₁ ≤ a−1`, no second borrow) — and here it is not a gap to patch but an automatic
  consequence of `n < p²` bounding the `Ico` to `{1}`.
* **K2** `v_p C(n+m,m) = c₀ + c₁ ≤ 2`: `n+m < 2p²` so `log p (n+m) < 3`, `Ico 1 3 = {1,2}` and the
  two indicators fall out. Use `padicValNat_choose'` (already in the `(n+k).choose k` shape).
  **≈ 25 lines.**
* **K3** `a + b ≥ p ⟹ 1 ≤ v_p C(a+b,b)` (for `a,b < p`) and **K4** `v_p C(n,jp) = 0`,
  `v_p C(n+jp,jp) = [a+j ≥ p]` are `omega` corollaries of K1/K2. **≈ 20 lines.**

### S4.4 Piece 4 detail — why (T-fact) is the expensive one

`T(n,m) := Σ_{k=m}^n A(n,k)` is summed over `Finset.Icc m n`, which is **not** a union of full
base-`p` blocks, so `Finset.sum_range_mul` (the S2/S3 workhorse) does not apply. The proof must:
1. show `Σ_{k ∈ Icc m n} A(n,k) ≡ Σ_{k ∈ Icc ((m₁+1)*p) n} A(n,k) (mod p)` — the discarded terms have
   `⌊k/p⌋ = m₁` and `k ≥ m`, hence low digit `s ≥ m₀ > r`, hence `A ≡ 0` by **`A_digits` from S2**
   (`C(r,s) = 0`);
2. extend the tail to `Icc ((m₁+1)*p) ((a+1)*p − 1)` by the same S2 extend-by-zeros lemma;
3. reindex that range into blocks — needs a **new** `sum_Icc_mul` companion to `sum_range_mul`
   (≈ 15 lines, `Finset.range` shift);
4. factor and read off `T(a,m₁+1) · a_r`.
Step 1 is precisely **referee item 2** (the product-region argument reused inside T-fact without
re-noting the `b = a, s > r` vanishing). In Lean it cannot be skipped — it is step 1, and it is
discharged by the *already proved* `A_digits`, which is the strongest evidence that the referee's
"one more sentence" reading is right and the step is sound.
(Tvanish) `a+j ≥ p ⟹ p² ∣ T(a,j)` is then ≈ 15 lines from **K3** plus the perfect-square shape of
`A` — note this is the ζ(3)-specific factor-of-2 slack that T4(c) warns does *not* survive the
weight-5 port.

### S4.5 Piece 6 detail — Lemma V

Ledger: `v_p(p³ c(n,m) T(n,m)) = 3 − v_p C(n,m) − v_p C(n+m,m) + v_p T(n,m) ≥ 1`, by a three-way
split on `v_p(CC) ∈ {0,1,2}` vs `= 3`. In `padicNorm` terms each branch is
`padicNorm p (p³ · X / (2m³·C·C)) ≤ p⁻¹` with `padicNorm p (1/(2m³)) = 1` (uses `p ≥ 5` for
`p ∤ 2` and `p ∤ m`). The dangerous branch `v_p(CC) = 3` forces `m₀ > r ∧ c₀ ∧ c₁`, whence
`m₁ + 1 ≥ p − a` and **(T-fact) + (Tvanish)** give `p ∣ T(n,m)`. So piece 6 **strictly depends on
piece 4** — they cannot be parallelised, and piece 4 must be finished first.

### S4.6 Scope caveats to carry into the Lean statement

* T3 is **single-digit only** (`1 ≤ a < p`, so `n < p²`). That hypothesis is not cosmetic: it is what
  bounds Kummer to ≤ 2 carries (S4.3) and is used in essentially every piece. The multi-digit master
  form `p³b_n a_q ≡ b_q a_n (mod p³)` and the mod-`p³` boost are `[VERIFIED, not PROVED]` upstream and
  are **not formalizable** until proved on paper.
* `p ≥ 5` is genuinely needed (`p ∤ 2` in `c(n,m)`, and `(−1)^{jp−1} = (−1)^{j−1}` needs `p` odd).
  By contrast (1) and (2) as formalized are uniform in `p` — no `p ≥ 5` hypothesis appears.

### S4.7 Recommended next increment (if a full T3 session is not available)

Do **pieces 2, 3 and 5** (≈ 185 lines, ≈ 3 h, all low-to-medium risk). They yield:
* a reusable **Kummer-in-two-digits** module — the same ledger the weight-5 port needs (T4(c)/(d));
* the `padicNorm` bridge to the existing `ZMod p` results;
* the **H-part of T3 fully proved** (`p³H₃(n)a_n ≡ H₃(a)a_a a_r (mod p)`), which consumes
  `apery_lucas` directly and is the only analytic half of T3 that stands alone.
That converts the riskiest part of the estimate (pieces 4, 6) from "unmeasured" to "measured against
a working `padicNorm` + Kummer toolkit" before committing a full session.

---

## File map

```
/home/ubuntu/fable-episode-2/zeta-math-2/lean/
├── lakefile.toml            (lib ZetaLucas; requires mathlib)
├── lean-toolchain           leanprover/lean4:v4.33.0-rc1
├── lake-manifest.json       mathlib @ cd580e54f1a6b46063824e80cec92f64692cbe78
├── .lake/packages/*         → symlinks into zeta-math/zeta5odd/.lake/packages (read-only reuse)
├── ZetaLucas.lean           root import file
└── ZetaLucas/
    ├── Core.lean           105 L — sum_range_mul, choose_digits(’), choose_digits_zero,
    │                                choose_carry_zero, padicValNat_choose_lt_sq (T3 groundwork)
    ├── Apery.lean          140 L — A, apery, A_digits, apery_lucas, apery_lucas_digits  [THEOREM 1]
    └── BrownZudilin.lean   221 L — T, Q, T_digits, Q_lucas, Q_lucas_digits              [THEOREM 2]
```
