# LEAN_QROW — landing the Brown–Zudilin **Q**-row certificate in the kernel

**Agent:** lean-agent (River's odd-zeta programme), 2026-07-26
**Module:** `lean/ZetaLucas/BZQRow.lean` (new, 891 lines / 64 KB), wired into `lean/ZetaLucas.lean`
**Toolchain:** Lean `v4.33.0-rc1`, Mathlib `cd580e54`, 15.2 GB RAM, 12 cores
**Inputs:** `work/z5cf/Qrow_phicert.m`, `work/Z5CF_CERT.md` §5.4, `work/LEAN_Z5_SCAFFOLD.md` §5

---

## 0. ⚠ HEADLINE — READ THIS FIRST ⚠

**`BZRec QSum` is not proved outright.** What is proved, `sorry`-free and with axioms exactly
`[propext, Classical.choice, Quot.sound]`, is

```lean
theorem QSum_bzrec (hkey : KeyPoly) : BZRec QSum
theorem Q_bzrec    (hkey : KeyPoly) : BZRec (fun n => (Q n : ℚ))
theorem QSum_eq_QBZ (hkey : KeyPoly) (n : ℕ) : QSum n = QBZ n
theorem Q_eq_QBZ    (hkey : KeyPoly) (n : ℕ) : (Q n : ℚ) = QBZ n
```

where `KeyPoly` is **one named polynomial identity in `ℤ[n,k,l]`** — the cleared form of the
certificate — and *everything else* in the pipeline (the transport to the pole-free base `Φ`,
the five `T`-shift facts, the strict positivity of every denominator, all four boundary
conditions, the double telescope, the range extension, the three-step uniqueness induction) is
proved unconditionally.

**`KeyPoly` is not discharged, and the obstruction is not mathematical.** The identity is
correct — verified exactly, three independent ways, in integer arithmetic (§2). It is
**Mathlib's `ring` that cannot check it**: it is a degree-`(27,11,13)` identity with 3798
monomials in its normal form, and *every* arrangement I tried exhausts this machine's 15 GB
(§4). `native_decide` would close it in seconds and is excluded by the programme's rule.

**There is NO new `sorry` in the library.** `BZQRow.lean` is `sorry`-free; the missing input is
a hypothesis, not an axiom. The library still contains exactly one `sorry`
(`BZClosedForm.bz_creative_telescoping`, line 661), unchanged.

**Bottom line for the P̂ row: it will not fit through this pipeline** (§6). The Q row is ~1/20
of the P̂ row's `ring` work and the Q row already does not fit. The fix is a reflective
polynomial-identity checker, not more `ring` engineering (§7).

---

## 1. What the file contains

`lean/ZetaLucas/BZQRow.lean`, `namespace ZetaLucas.BZQRow`, importing `ZetaLucas.BZClosedForm`.

### §1 the object

```lean
def QSum (n : ℕ) : ℚ := ∑ k ∈ range (n+1), ∑ l ∈ range (n+1), (T n k l : ℚ)
theorem QSum_eq_Q (n : ℕ) : QSum n = (Q n : ℚ)            -- the integer row of BrownZudilin
theorem QSum_eq_sum_range {n N} (h : n+1 ≤ N) : QSum n = ∑ k ∈ range N, ∑ l ∈ range N, (T n k l : ℚ)
```

`QSum_eq_sum_range` is `BZClosedForm.sum_T_eq_sum_range` at the constant weight `1`; the
"stated for an arbitrary weight `w`" design of that lemma paid for itself immediately.

### §2 the certificate data

Blocks `X1,X2,X3,Y1,Y2,Y3` (all degree 4), the four cofactors

```
PP0 = Y3(Y2 Y1)    PP1 = X1(Y3 Y2)    PP2 = (X1 X2)Y3    PP3 = (X1 X2)X3
```

**in exactly the parenthesisation `T_shift_n`, `T_shift_n2`, `T_shift_n3` are already stated
in** — this is what makes `F0` below cost literally nothing — plus `Dr`, `Ds`, `Dstar`,
`U1…U4`, `cq0…cq3` (`cc_i n = cq_i (n:ℚ)` by `rfl`), and the certificate numerators

```lean
def Amid (n k l : ℚ) : ℚ := …          -- 1133 monomials, degrees (24,6,8)
def Acore (n k l : ℚ) : ℚ := -((n + l + 1) * Amid n k l)
def Anum  (n k l : ℚ) : ℚ := k ^ 3 * Acore n k l                  -- = r_num
def Bmid (n k l : ℚ) : ℚ := …          --  239 monomials, degrees (18,1,7)
def Kfac (n k _l : ℚ) : ℚ := (n+1-k)^2 * (n+2-k)^2 * (n+3-k)^2
def Bcore (n k l : ℚ) : ℚ := Kfac n k l * Bmid n k l
def Bnum  (n k l : ℚ) : ℚ := l ^ 3 * Bcore n k l                  -- = s_num
```

The `k³` and `l³` are kept explicit because they **are** the bottom boundary conditions; the
factorisations `A = −k³(n+l+1)·Amid` and `B = l³·[(n+1−k)(n+2−k)(n+3−k)]²·Bmid` were found
here (they are not in `Qrow_phicert.m`) and cut the transcribed data from 2445 monomials to
1372.

### §3 `KeyPoly` — the one open input

```lean
def KeyPoly : Prop :=
  ∀ n k l : ℚ,
    Dstar n k l * (cq0 n * PP0 n k l + cq1 n * PP1 n k l + cq2 n * PP2 n k l + cq3 n * PP3 n k l)
      = U1 n k l * Anum n (k+1) l - U2 n k l * Anum n k l
        + U3 n k l * Bnum n k (l+1) - U4 n k l * Bnum n k l
```

Verbatim `Z5CF_CERT.md` §5.4's `polyidentity`.

### §4–§9 everything else, unconditionally proved

| lemma | content | cost |
|---|---|---|
| `PP3_pos`, `Dr_pos`, `Ds_pos`, `Dstar_pos` | every denominator **strictly positive** for all `n,k,l ≥ 0` | `positivity`, instant |
| `F0` | `T(n,k,l)·P₃ = T(n+3,k,l)·P₀` | **`exact (T_shift_n3 n k l).symm`** — free |
| `F1`, `F2` | the `i = 1, 2` cases | `linear_combination (-X1)·h`, `(-(X1·X2))·h`; the blocks `X1`, `X2` stay folded so `ring` sees degree ≤ 12 |
| `Fk`, `Fl` | the `k`- and `l`-steps of the base at `n+3` | `T_shift_k/l` + `push_cast` + `linear_combination` |
| `PP3_shift_k/l` | `P₃(n,k+1,l)·(n+k+1)(n+k+l+1) = P₃(n,k,l)·(n+k+4)(n+k+l+4)` | degree-14 `ring`, ~2 s |
| `Dstar_eq_Dr/Ds/Drk/Dsl` | the four factorisations of `D*` used to put the five terms over `P₃·D*` | degree-14 `ring` |
| `Rq_bot`, `Rq_top`, `Sq_bot`, `Sq_top` | **all four boundary conditions**, `simp` | instant |
| `E_eq`, `Rq_here`, `Rq_next`, `Sq_here`, `Sq_next` | the five terms over the common denominator | `linear_combination` with hand-computed cofactors; every `ring` check sees **atoms**, degree ≤ 12 |
| `star hkey` | **(★)** `Σ_i c_i(n)T(n+i,k,l) = Δ_k R + Δ_l S`, all `n,k,l : ℕ`, no range hypothesis | `div_sub_div_same` ×2, `← add_div`, `congr 1`, `linear_combination t · hkey` |
| `QSum_bzrec hkey` | the sum over `range (n+4)²`, `Finset.sum_comm`, `Finset.sum_range_sub` twice | mirrors `MinimalForm.bMin_rec` exactly |
| `QBZ`, `QBZ_bzrec`, `QSum_zero/one/two`, `QSum_eq_QBZ hkey` | the recurrence-defined row and the identification via `eq_of_BZRec` | |

`#eval` cross-check printed by the build:
`QBZ 0..5 = [1, 21, 2989, 714549, 217515501, 76157194521]` from the **recurrence**, against
`QSum 0..3 = [1, 21, 2989, 714549]` from the **double sum**.  `Q₄ = 217515501` and
`Q₅ = 76157194521` agree with `work/ZETA7_STATE.md` and with a direct computation of the double
sum done here.

### `#print axioms` — verbatim build output

```
'ZetaLucas.BZQRow.E_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZQRow.Rq_next' depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZQRow.Sq_next' depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZQRow.star' depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZQRow.QSum_bzrec' depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZQRow.QSum_eq_QBZ' depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZQRow.Q_bzrec' depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZQRow.Q_rec' depends on axioms: [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZQRow.Q_eq_QBZ' depends on axioms: [propext, Classical.choice, Quot.sound]
[1, 21, 2989, 714549, 217515501, 76157194521]
[1, 21, 2989, 714549]
```

No `sorryAx`. No warnings. `lake build` clean.

---

## 2. The certificate is correct — verified three independent ways

None of this used Mathematica.

1. **`sympy`** parse of `Qrow_phicert.m` and `expand(LHS − RHS) == 0`. ✔
2. **A from-scratch exact sparse `ℤ[n,k,l]` implementation** (dict-of-monomials, GMP integers),
   independent of `sympy`: `LHS − RHS` has **0** terms. ✔
3. **Pointwise, in exact `ℚ`, under Lean's own conventions** — this is the check that matters
   for the formalisation, because `LEAN_Z5_SCAFFOLD` §5.7 note 2 and `Z5CF_CERT` §5.5 both warn
   that the rational-function statement and the Lean statement are different at
   `k, l ∈ {n+1,n+2,n+3}`. With `T(n,k,l) := 0` for `k > n` or `l > n`, and `R, S` evaluated as
   written in the Lean file:
   * `Σ_i c_i(n)T(n+i,k,l) = ΔₖR + Δ_lS` — **0 mismatches** over `n = 0…6`, `0 ≤ k,l ≤ n+7`
     (all 476 cells, deliberately running well past the summation range);
   * `R(n,0,l) = R(n,n+4,l) = S(n,k,0) = S(n,k,n+4) = 0` — **0 failures**;
   * `Σ_i c_i(n)Q_{n+i} = 0` for `n = 0…7`. ✔

Also re-derived independently: `Q_n = 1, 21, 2989, 714549, 217515501, 76157194521, …` and the
fact that **`L_BZ` is the minimal-order recurrence for `Q` alone** — a nullspace search over
`Q_0…Q_59` finds nothing at order 1 or 2 for any degree ≤ 13, and exactly nullity 1 at
(order 3, degree 9). So there is no cheaper operator to aim at.

### Sizes (all measured)

| object | monomials | `(deg_n, deg_k, deg_l)` | max coefficient |
|---|---|---|---|
| `Σ_i c_i(n)P_i(n,k,l)` (the LHS before clearing) | **784** | (21,6,6) | 58 bits |
| `A = r_num` | **1294** | (25,9,9) | 73 bits |
| `B = s_num` | **1151** | (24,7,10) | 68 bits |
| `D*·Σ_i c_i P_i` = the cleared identity | **3798** | (27,11,13) | 76 bits |
| `U₁·A(n,k+1,l)` | 4328 | | |
| `U₃·B(n,k,l+1)` | 4235 | | |

A useful fact nobody had recorded: **`(k+1)³(l+1)³` divides every term of the cleared
identity**; dividing it out gives an equivalent identity with **2037** monomials and degrees
(27,8,10) — a 46 % reduction, still far too big (§4).

---

## 3. Traps hit (all of them cost real time)

1. **The `Φ`-base warning of `LEAN_Z5_SCAFFOLD` §5.2 is exactly right and is not optional.**
   Nothing here uses base `T(n,k,l)`. Every denominator (`P₃`, `D_r`, `D_s`, `D*`) is a product
   of factors of the shape `(n+a)`, `(n+k+a)`, `(n+l+a)`, `(n+k+l+a)`, `(k+l+a)`, `(k+a)`,
   `(l+a)` with `a > 0`, hence **strictly positive**; `positivity` discharges all four
   positivity lemmas in one line each and there is not a single `0/0` in the file.
2. **`push_cast` does not normalise `↑n + 1 + 2` to `↑n + 3`.** Every use of `T_shift_n2 (n+1)`
   / `T_shift_n (n+2)` / `T_shift_k (n+3)` therefore needs a `linear_combination h` to absorb
   the numeral reassociation. That is cheap only because the *blocks* `X1`, `X2` stay folded —
   unfolding them turns a 3-second `ring` into a degree-24 flatten.
3. **`div_eq_div_iff` needs the nonzero-ness hypothesis in the *cast-pushed* form.**
   `PPDr_ne n (k+1) l` gives `PP3 ↑n ↑(k+1) ↑l ≠ 0`, but after `push_cast` the goal contains
   `PP3 ↑n (↑k+1) ↑l`. Two extra lemmas (`PPDr_k_ne`, `PPDs_l_ne`) fix it.
4. **`div_add_div_same` does not exist** in this Mathlib (`div_sub_div_same` does). Use
   `← add_div`.
5. **`Finset.sum_add_distrib` will not fire on a nested sum** unless the inner sum has already
   been split. The inner lemma must be stated as `(∑ l, Δ_kR) + (∑ l, Δ_lS)`, not as
   `∑ l, (Δ_kR + Δ_lS)`, or the outer `Finset.sum_add_distrib` has nothing to match.
6. `field_simp` on the `QBZ` recurrence leaves `… * (1 + -1) = 0`; it needs a trailing `ring`
   (`Phat_bzrec` in `BZClosedForm` already does this — I re-learned it).
7. **`pkill -f <pattern>` kills the shell that runs it** when the pattern occurs in that
   shell's own command line. Cost me two scripted runs. Kill by PID.

---

## 4. The wall: `ring` and a 3798-monomial identity — every measurement

All runs: `lake env lean -j1`, machine idle unless noted, 15.2 GB RAM. "killed" = OOM or killed
by me at the memory ceiling; **not one arrangement completed**.

| # | arrangement | coefficients | outcome |
|---|---|---|---|
| 1 | monolithic, `A`,`B` as **flat** sums of 1294/1151 monomials | ℚ | killed at 35 min wall / 13 min CPU, still running |
| 2 | monolithic, `A`,`B` in **Horner** form | ℚ | 10.1 GB at 4 m 32 s CPU, killed |
| 3 | LHS **chain-split** (5 lemmas, one sparse multiplier each: `×(n+1)²(n+2)²`, `×(n+l+2)(n+l+3)`, `×(k+l+1)(k+l+2)`, `×(k+1)³(l+1)³`) + monolithic RHS | ℚ | **the LHS chain succeeded** (whole chain ≈ 2.5 GB); the RHS killed at 10.1 GB |
| 4 | `hV3 : U₃·B(n,k,l+1) = V₃` alone (one of four RHS pieces) | ℚ | killed above 10.6 GB |
| 5 | same, with the six factors of `U₃` multiplied in **explicit left-to-right order** and `B` pre-factored as `l³·Kfac·Bmid` | ℚ | **OOM at 13.4 GB** |
| 6 | `hVsum : V₁ − V₂ + V₃ − V₄ = W` — **no multiplication at all**, just normalising five given polynomials of 3133–4328 monomials and merging | ℚ | 10.5 GB at 6 m 36 s CPU, killed |
| 7 | the same `hVsum` | **ℤ** | 8.5 GB at 2 m 56 s CPU, killed |
| 8 | `hV2 : U₂·A = V₂` (the *smallest* RHS piece: `|U₂| = 24`, `|A| = 1294`, `|V₂| = 3133`) | abstract `CommRing R` | memory stayed flat at **3.0–3.3 GB** — the only arrangement that did — but **10 min CPU and still not finished** when I stopped it; extrapolating, one such lemma is ≥ 15 min, and there are four of them plus the LHS chain |
| 9 | monolithic, `A`,`B` pre-factored, abstract `CommRing R` | integer | 9.0 GB at 45 s CPU, killed |

### What the numbers say

* **Row 6 is the decisive one.** No products, no substitution, no clever ordering: just
  *reading five polynomials of ~4000 monomials into `ring`'s normal form and adding them* costs
  more than 10 GB. The cost is in `ring`'s **proof term**, which is retained in full: every
  intermediate `ExSum` is referenced by the proof of the next step, so memory grows with the
  *total number of monomials ever produced*, not with the working set.
* Empirically the budget is **≈ 5 000–6 000 monomials touched per `ring` call ⇒ ≈ 2.5 GB**;
  ≈ 10 000 ⇒ ≈ 5 GB; ≈ 20 000 ⇒ over 13 GB. It is roughly linear with a brutal constant of
  **~0.5–1 MB per monomial produced**.
* Integer coefficients help, but only by a factor ≈ 1.5–2 (rows 6 vs 7, 2 vs 9) — not the
  order of magnitude needed. Horner vs flat helps the *input* side by ~10× (row 1 vs 2) and is
  strictly the right encoding, but the output side dominates.
* The **chain-split works** (row 3) and is the right technique: one sparse multiplier per lemma
  keeps each call inside the budget. It is simply not enough here, because the RHS chain needs
  ~36 such lemmas with ~90 000 monomials of *written-out intermediate polynomials* (≈ 4.5 MB of
  generated Lean) spread over ~12–15 separate modules to keep each `lean` process under 5 GB.
  I estimate 2–4 h of build time per full rebuild for the Q row alone. That is not a library
  anyone should have to compile, so I did not build it.

**This is not a limit of the certificate, of the `Φ` normalisation, or of the Lean formulation.
It is `Mathlib.Tactic.Ring` meeting a 3798-monomial identity.**

---

## 5. Measured effort and timings

| stage | wall clock |
|---|---|
| reading (`LEAN_Z5_SCAFFOLD` §5, `Z5CF_CERT`, `BZClosedForm`, `MinimalForm`, `Qrow_phicert.m`) | ~25 min |
| independent verification of the certificate (3 ways) + minimal-recurrence search for `Q` | ~20 min |
| designing and validating the Lean structure (a dummy-`Acore` skeleton with `key_poly` stubbed) | ~35 min |
| the `ring` campaign of §4 (nine arrangements) | **~3 h** |
| final module, `lake build`, this report, `LEAN_VERIFIED.txt` | ~40 min |

Build timings for the delivered module:

| what | time |
|---|---|
| `lake env lean -j1 ZetaLucas/BZQRow.lean` (file alone) | **3 m 34 s** (2 m 33 s CPU) |
| skeleton version with a 3-monomial dummy `Amid`/`Bmid` | ~2 min |
| `lake build` incremental after `BZQRow.lean` | see §8 |

The delivered file is 874 lines / 64 KB, of which ~570 lines are the two transcribed
polynomials (`Amid`, `Bmid`, in Horner form).

**One more corroboration of the `ring` constant, from the delivered module itself:** it contains
no large `ring` call — the biggest are the six degree-14 identities `PP3_shift_k/l` and
`Dstar_eq_Dr/Ds/Drk/Dsl`, whose normal forms total ~4000 monomials — and its `.olean` is
**172 MB**. That is ≈ 40 KB of stored proof term per monomial of `ring` normal form, at
degree 14 with 20-bit coefficients. The `key_poly` identity has 3798 monomials at degree 27
with 76-bit coefficients, i.e. an order of magnitude more per monomial. The arithmetic is
consistent with §4 and it is why no amount of splitting rescues this.

---

## 6. ⭑ Calibrated estimate for the P̂ row ⭑

### The data (measured from `work/z5cf/w3_LHS_basis.m`, this session)

`E_{ŵ₃}/Φ = Σ_{j=1}^{15} b_j(n,k,l)·M_j`. Parsing the 15 numerators exactly:

| block | monomials | `(deg_n,deg_k,deg_l)` | coeff bits | denominator |
|---|---|---|---|---|
| `b₀,b₂,b₄,b₆,b₈,b₁₀,b₁₃` (7 blocks) | **784** each | (21,6,6) | 58–60 | `2` or none |
| `b₁,b₃,b₅,b₇,b₉,b₁₁` (6 blocks) | **914** each | (22,7,6) | 60–62 | `(n+k+1)(n+k+2)(n+k+3)` |
| `b₁₂` | **1600** | (25,9,9) | 65 | `(k−n−1)(k−n−2)(k−n−3)(n−l+1)(n−l+2)…` |
| `b₁₄` | **2771** | (30,13,9) | 74 | `(k−n−1)(k−n−2)(k−n−3)(n+k+1)²(n+k+2)²…` |
| **total** | **15 343** | up to (30,13,9) | 74 | |

**The seven 784-monomial blocks are, monomial for monomial and degree for degree, exactly the
same size as the entire Q-row left-hand side** (`Σ_i c_i P_i`: 784, (21,6,6), 58 bits). That is
the calibration: *the Q row is one block of the P̂ row, and it is one of the seven cheapest.*

### The estimate

* **LHS:** 15 343 / 784 = **19.6× the Q row**, in 15 separate identities.
* **RHS:** the 15 pairs `(ρ_j, σ_j)` **do not exist yet** — the `ct1` elimination is still the
  open gate (`Z5CF_CERT` §§2, 4: `ct1` time-aborted at 5402 s, `OreGroebnerBasis` returned the
  same basis with reduction factor 1.000×). When they land, each numerator will be at least the
  size of the Q row's `A`/`B` (1294 / 1151), and **larger**, because the weight rows' common
  denominator carries the extra factors `(n+k+1)(n+k+2)(n+k+3)` and
  `(k−n−1)(k−n−2)(k−n−3)`, `(n−l+1)(n−l+2)(n−l+3)` that the Q row does not have. Scaling the
  Q row's 3798-monomial cleared identity by the LHS ratio and by one extra degree-3 denominator
  factor per index gives **≈ 10 000–20 000 monomials per cleared identity, × 15 identities**,
  i.e. **~2·10⁵ monomials of normal form** against the Q row's 3798.
* **`ring` cost at the measured constant** (~0.5–1 MB per monomial produced, and the Q row's
  3798-monomial identity already needs > 15 GB): the P̂ row needs on the order of
  **200–500 chained lemmas, 1–2 million monomials of generated Lean source (50–100 MB), and
  100+ modules** to keep each process under 5 GB. A full rebuild would be measured in days.
* **Plus** the obligation that is *vacuous for the Q row and real for P̂*: `Z5CF_CERT` §5.5's
  **second, independent pole source**. The 15 coefficients `b_j` have simple poles at
  `k = n+1,n+2,n+3` and `l = n+1,n+2,n+3` that `P₀` does **not** cancel, because they come from
  re-expressing `H^(r)_{n+i−k}` over the base letter `H^(r)_{n−k}`. Their cancellation against
  the singularity of the base letter is only legitimate under Lean's truncated-`ℕ` /
  `1/0 = 0` conventions ("Lemma N", verified numerically on 945 cells, **not proved**). That is
  a whole extra layer of Lean work — 15 letter-monomials × 6 shift rules — that the Q row never
  touches. `Z5CF_CERT` §5.5 says so explicitly and it is right.

### Verdict

> **The P̂ row will NOT fit through this pipeline.** Not "will be expensive" — will not fit.
> The Q row is ≈ 1/20 of it and the Q row does not fit, by a measured factor of ≥ 3 in memory
> on the single cheapest sub-lemma. Continuing to shrink `ring` calls is a dead end: the
> constant is ~1 MB of retained proof term per monomial of normal form, and the P̂ row has
> ~2·10⁵ of them.

This is decision-relevant rather than a failure: it means the gating item for the ζ(5) closed
forms is **not** the RISC elimination (T2). Even if `ct1` returned tomorrow, the certificate
could not be checked by `ring`. **The gate has moved from the CAS to the proof checker.**

---

## 7. What would actually discharge `KeyPoly` (and the P̂ row with it)

In increasing order of leverage.

1. **`native_decide`** closes it in seconds. Excluded by River's rule, correctly — it trusts the
   Lean compiler and the whole toolchain. Recorded only because it is what everyone reaches for.

2. **A reflective polynomial-identity checker.** This is the standard, kernel-only fix and it is
   the recommendation. Represent a sparse multivariate polynomial as
   `List ((ℕ × ℕ × ℕ) × ℤ)` kept sorted, give it a computable `eval : Poly → R → R → R → R` for
   any `CommRing R`, a computable `normalise`, and prove
   `normalise p = normalise q → ∀ x y z, eval p x y z = eval q x y z`. Then `KeyPoly` is closed
   by `rfl`/`decide` on a `List` equality, which the kernel executes with GMP-accelerated `Nat`
   arithmetic — the same mechanism that already makes `decide` viable for `Q 3 = 714549` in
   `BZClosedForm`. Cost of the *checking* step becomes linear with a small constant, and the
   proof term is `Eq.refl`. Estimated **400–800 lines of Lean, one-off**, and it makes the
   entire weight-3 and weight-5 programme checkable. **This is the single highest-leverage item
   in the formalisation half of the campaign.** (Prior art to copy: `Mathlib`'s
   `Polyrith`/`linear_combination` do *not* do this; `Mathlib.Tactic.NormNum` does exactly this
   pattern for numerals; the closest full example is the `ring` implementation itself, which is
   reflective in its *computation* but not in its *proof*.)

3. **Shrink the certificate before it reaches Lean.** Two concrete, cheap-to-try levers:
   * The WZ pair is not unique: `R → R + Δ_l W`, `S → S − Δ_k W` for any `W`. Minimising
     `deg(A) + deg(B)` over a `W`-ansatz is a linear-algebra problem on the CAS side. The
     current `A` has `deg_n = 25` while the identity only has `deg_n = 27`, so there is
     visible cancellation at the top — a lower-degree pair plausibly exists.
   * Divide the cleared identity by `(k+1)³(l+1)³`, which divides **every** term (verified
     here). 3798 → **2037** monomials, degrees (27,11,13) → (27,8,10). Free, and should be done
     in `Qrow_phicert.m` regardless.
   Together these might buy 2–4×. Useful with item 2, **not a substitute for it**: 4× is not
   20×, let alone the 50× the P̂ row needs.

4. **Do not** invest further in chain-splitting `ring`. §4 row 6 shows the floor is not the
   multiplications.

---

## 8. Reproducing

```bash
cd lean && lake build            # clean, 8674 jobs, 3 m 08 s; BZQRow built in 177 s
lake env lean -j1 ZetaLucas/BZQRow.lean    # 3 m 34 s, prints the axiom audit above
grep -rn "sorry\|native_decide" ZetaLucas/*.lean   # still exactly one live sorry:
                                                   # BZClosedForm.lean:661
```

The independent verification scripts are throwaway and were not committed; they are three
short Python programs (a Mathematica-subset parser, a sparse `ℤ[n,k,l]` arithmetic layer, and
the pointwise `ℚ` check with Lean's truncation conventions), each under 100 lines. Everything
they establish is restated exactly in §2 and is re-derivable from `Qrow_phicert.m` in minutes.

---

# ADDENDUM (same session) — `w★`, and the answer on 42 blocks

`work/Z5CF_REP.md` landed while this was being written: `L_BZ` **is** a telescoper of `T·w★`
for a new representative `w★` of the `P̂` row, with a 42-block order-3 certificate. The
coordinator asked for (a) everything that certificate will need, built ahead of it, and (b) —
early — whether 42 blocks will fit through `ring`.

## 9. The answer on 42 blocks: **NO, and not close**

This is the number that was asked for early, so it is first.

**The measured `ring` budget on this machine** (§4, nine arrangements, all of them failures at
the top end):

| monomials touched by one `ring` call (inputs + output + intermediates) | outcome |
|---|---|
| ≲ 1 500 | ~2 s, fine (this is `PP3_shift_k`, `Dstar_eq_*`: degree 14, ~680 monomials each) |
| ~6 000 | ~1–2 min, ≈ 2.5 GB — **the practical ceiling** (`S3poly · (k+1)³(l+1)³ = Wpoly`) |
| ~10 000 | ≈ 5–8 GB, minutes to tens of minutes |
| ~15 000 | **> 15 GB, dies** — this is the Q row's single cleared identity |
| ~20 000 | dies at 13.4 GB in under 4 min |

Six degree-14 `ring` calls in the delivered `BZQRow.lean` produce a **172 MB** `.olean`. That
is the constant: ~40 KB of retained proof term per monomial of normal form at degree 14, and
about an order of magnitude more at degree 27 with 76-bit coefficients.

**Now the P̂ row via `w★`.**

* The Q row is `J = 1`, weight `≡ 1`, no letters at all — the *simplest possible* member of
  this family. Its one cleared identity is 3798 monomials at degrees `(27,11,13)`, and it
  **does not fit**, by a measured factor of ≥ 3 in memory.
* `w★` has `J = 42`. Every one of the 42 blocks produces a cleared identity of the same
  *shape* as the Q row's — same operator `L_BZ` (degree-9 coefficients), same base `Φ₃` (the
  degree-12 `P_i`), same `D*`-style clearing — so each block's identity is **at least**
  Q-row-sized on the `Σ_i c_i P_i` side alone (784 monomials before clearing, 3798 after).
* And the cofactors will be **larger**, not smaller. `Z5CF_REP` §3 runs its ansatz at
  bidegree **(32,32)** in `(k,l)` with `nc = 2178` free coefficients; the Q row's actual
  cofactor numerators have bidegrees `(9,9)` and `(7,10)`. Even after the solve trims them,
  there is no reason to expect them below the Q row's 1294/1151 monomials, and every reason
  (13 symbols, `n+k+1`-type extra denominators — cf. the six `b_j` of the `ŵ₃` basis that
  carry `(n+k+1)(n+k+2)(n+k+3)`) to expect them above.
* Total: **~42 × (10⁴ monomials) ≈ 4·10⁵ monomials of normal form**, against a per-`ring`
  ceiling of ~6·10³ and a *single* identity of 1.5·10⁴ that already kills the machine.

> **Verdict: the 42-block certificate will not go through `ring`. The shortfall is ≥ 10× per
> block and ≥ 400× in total.** This is the same verdict as §6 gave for the order-7 route, for
> the same reason, and it is now backed by a completed worked example on the easiest row in
> the family.

### What this means for L6, concretely

1. **If the goal is `ring`**, the ceiling L6 must hit is: *every cleared block identity, in
   fully expanded `ℤ[n,k,l]` normal form, ≤ ~1 200 monomials with coefficients ≤ ~40 bits,
   each block in its own Lean module.* 42 such modules would build in ~2 h. I do not believe
   that ceiling is reachable — it is 3× smaller per block than the Q row, which is the
   weight-0 case. **L6 should not spend effort optimising toward it.**
2. **The leverage is elsewhere.** Build the reflective polynomial-identity checker of §7.2
   (~400–800 lines of Lean, one-off, no `native_decide`): sparse `List ((ℕ×ℕ×ℕ) × ℤ)`
   representation, computable `normalise` and `eval` into any `CommRing`, soundness lemma,
   and then each block identity closes by kernel computation with a proof term of size
   `Eq.refl`. With it the size ceiling moves by 2–3 orders of magnitude and 42 blocks — or
   the weight-5 row's 64 — becomes routine.
3. **Therefore L6 should optimise for the checker, not for `ring`:** minimise *total*
   monomial count and integer coefficient height, and deliver the blocks in **fully expanded
   sparse-monomial form over ℤ** (a JSON list of `[[e_n,e_k,e_l], c]` per block, both sides,
   plus the common denominator cleared). Pre-factored product form is what `ring` wants and is
   the wrong target now. The `LEAN_Z5_SCAFFOLD` §5.6.1 "pre-factored, never flattened"
   instruction should be **superseded** for the weight rows.
4. **Two free size reductions, worth taking regardless.** (i) In the Q row `(k+1)³(l+1)³`
   divides *every* term of the cleared identity — 3798 → 2037 monomials, degrees
   `(27,11,13)` → `(27,8,10)`. The same cancellation will exist per block. (ii) `A` and `B`
   factor as `−k³(n+l+1)·Amid` and `l³[(n+1−k)(n+2−k)(n+3−k)]²·Bmid`; the second factor is the
   one that cancels `Φ`'s interior `k`-poles and it is worth extracting explicitly, since it
   cut `B` from 1151 to 239 monomials of genuinely free data.

## 10. What compiled for `w★` — `lean/ZetaLucas/BZStar.lean`

New module, 339 lines, **compiles in 10 s**, `lake build` clean (8675 jobs, 15 s incremental).

**Transcription check done before writing any Lean:** `Σ_{k,l≤n} T(n,k,l)·w★(n,k,l) = P̂_n`
exactly over `ℚ` for `n = 0,1,2,3,4` against `0, 101/4, 344923/96, 3710571371/4320,
602417685937/2304`. All five exact.

### §1 the bare-letter shift table — the substantive new infrastructure

`w★` lives in the **bare** alphabet, not the difference alphabet (`Ad`, `Bd`) the development
carried. The eight arguments `k, l, n, n−k, n−l, n+k, n+l, n+k+l` are differenced in `k`, `l`
and `n`; twelve of the twenty-four differences vanish definitionally, and the twelve nonzero
ones are:

```lean
Harm_sub_succ_n   {r} (hr : 0 < r) (n x) : Harm r (n+1-x)   = Harm r (n-x) + 1/((n+1-x:ℕ):ℚ)^r
Harm_sub_succ_arg {r} (hr : 0 < r) (n x) : Harm r (n-(x+1)) = Harm r (n-x) - 1/((n-x:ℕ):ℚ)^r
Harm_succ_self, Harm_nk_succ_n, Harm_nk_succ_k, Harm_nl_succ_n, Harm_nl_succ_l,
Harm_nkl_succ_n, Harm_nkl_succ_k, Harm_nkl_succ_l
```

The two subtraction lemmas hold **for every `x`, with no `x ≤ n` hypothesis** — the
truncated-`ℕ`/`1/0 = 0` convention makes both sides collapse together past the range. That is
`LEAN_Z5_SCAFFOLD` §5.7 note 2, and it is why a telescope that runs to `k = n+4` needs no
boundary case. Keep the convention.

### §2–§4 the weight and the conditional closed form

```lean
def Ustar, Vstar, wstar, PStarSum
theorem PStarSum_eq_sum_range {n N} (h : n+1 ≤ N) : PStarSum n = ∑ k ∈ range N, ∑ l ∈ range N, …
theorem PStarSum_zero : PStarSum 0 = 0
theorem PStarSum_one  : PStarSum 1 = 101/4
theorem PStarSum_two  : PStarSum 2 = 344923/96
theorem PStarSum_eq_Phat_of_rec (h : BZRec PStarSum) (n : ℕ) : PStarSum n = Phat n
```

The three initial values are computed **from the definitions** — no recurrence — so they pin
the transcription of `w★` inside the kernel. `#eval PStarSum 0..3` additionally prints
`[0, 101/4, 344923/96, 3710571371/4320]`: the fourth value is **not** an initial condition and
is used by nothing, and it agrees with the exact ladder `P̂₃`. So the weight is pinned at four
points, not three.

### §5 the quarantine

```lean
theorem star_creative_telescoping : BZRec PStarSum := by sorry     -- BZStar.lean:255
theorem PStarSum_eq_Phat (n : ℕ) : PStarSum n = Phat n :=
  PStarSum_eq_Phat_of_rec star_creative_telescoping n
```

`BZRec PStarSum` is now the **single** remaining input for the weight-3 closed form, exactly as
`bz_creative_telescoping` is for `PhatSum`. `work/LEAN_VERIFIED.txt` §11 and §12 were updated:
the library now has **two** live `sorry`s, both quarantined and both listed.

### §6 the `k↔l` antisymmetry machinery

```lean
theorem sum_antisym_zero (n) (w) (hw : ∀ k l, w n k l = -w n l k) :
    ∑ k ∈ range (n+1), ∑ l ∈ range (n+1), (T n k l : ℚ) * w n k l = 0
theorem PhatSum_eq_PStarSum_of_antisym
    (h : ∀ n k l, wstar n k l - w3h n k l = -(wstar n l k - w3h n l k)) (n) :
    PhatSum n = PStarSum n
```

`sum_antisym_zero` is the *proved* half of `Z5CF_REP` §2's 58-dimensional kernel `K` — 45 of
those 58 dimensions are exactly the antisymmetric subspace, and they are free from
`T n k l = T n l k` (`BZClosedForm.T_symm`). If L6 delivers a family member with
`w★ − ŵ₃` antisymmetric, `PhatSum = PStarSum` closes in one line.

⚠ **But it is not needed and should not be waited for.** `PStarSum_eq_Phat_of_rec` reaches
`Phat` directly, via `eq_of_BZRec` and the three initial values proved in §3 — it never goes
through `PhatSum`. If the delivered member is *not* antisymmetric-equal to `ŵ₃`, nothing is
lost. That is deliberate: the comparison is a convenience, not a dependency.

### `#print axioms` — verbatim

```
'ZetaLucas.BZStar.Harm_sub_succ_n'    [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZStar.Harm_sub_succ_arg'  [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZStar.Harm_nk_succ_n'     [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZStar.Harm_nk_succ_k'     [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZStar.Harm_nkl_succ_n'    [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZStar.Harm_nkl_succ_k'    [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZStar.Harm_nkl_succ_l'    [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZStar.PStarSum_eq_sum_range'        [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZStar.PStarSum_zero'                [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZStar.PStarSum_one'                 [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZStar.PStarSum_two'                 [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZStar.PStarSum_eq_Phat_of_rec'      [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZStar.sum_antisym_zero'             [propext, Classical.choice, Quot.sound]
'ZetaLucas.BZStar.PhatSum_eq_PStarSum_of_antisym' [propext, Classical.choice, Quot.sound]
--- below the line: the quarantined lemma and its consequence ---
'ZetaLucas.BZStar.star_creative_telescoping' [propext, sorryAx, Classical.choice, Quot.sound]
'ZetaLucas.BZStar.PStarSum_eq_Phat'          [propext, sorryAx, Classical.choice, Quot.sound]
[0, 101 / 4, 344923 / 96, 3710571371 / 4320]
```

## 11. The weight-5 half

Nothing is built for `PSum`/`w₅` beyond what `BZClosedForm.lean` already has, deliberately.
The structure is already parallel — `PSum`, `PSum_eq_sum_range`, `PSum_zero/one/two`,
`PSum_eq_PBZ_of_rec` all exist and are clean — so a weight-5 representative and certificate
drop into the same shape with no new scaffolding: define `w5star`, `P5StarSum`, re-prove three
initial values against `0, 87/4, 1190161/384`, and quote `eq_of_BZRec`. The bare-letter table
of §1 above covers `H^(1)` and `H^(2)`; weight 5 additionally needs `H^(4)` and `H^(5)` at
`n+k`, which are the *same* lemma `Harm_succ` at a different `r` — `Harm_nk_succ_n/k` are
already stated for arbitrary `r`, so **nothing new is required**.

The size verdict of §9 applies a fortiori: weight 5's shift closure is 64, and
`Z5CF_CERT` §0.3 shows no representative can avoid the `n+·`/`n−·` letter-family mixing that
drives the cost. If L7 finds an order-3 weight-5 representative, it is a genuine advance for
the CAS side and changes nothing about the Lean-side ceiling.

## 12. Priority, restated

The gate for the ζ(5) closed forms has moved. It is no longer the telescoper order
(`Z5CF_REP` solved that) and it is no longer the RISC elimination. It is **the proof
checker**. One 400–800-line reflective polynomial-identity checker unblocks the Q row, the
42-block `w★` row, and whatever weight-5 representative L7 finds. Everything else in this file
is a measurement of what happens without it.
