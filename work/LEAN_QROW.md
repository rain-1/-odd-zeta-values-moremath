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

---

# ADDENDUM 2 — the reflective checker: **provisional cost curve** (measured), and the retired antisymmetry route

## 13. HEADLINE — reflection works, and it is *hours, not days*

**Kernel reduction of sparse-polynomial arithmetic is linear in work and FLAT in memory at
≈ 1.7 GB, independent of problem size.** That is the whole ballgame: `ring`'s wall was
~1 MB of retained proof term per monomial; a reflective proof term is `Eq.refl`, so the memory
axis disappears and only time remains — and time is linear and measurable.

### 13.1 The prototype

```lean
abbrev Mono : Type := Nat × Nat × Nat
abbrev Poly : Type := List (Mono × Int)          -- canonical: lex-sorted, no zero coefficients

def mergeAux : Nat → Poly → Poly → Poly          -- fuel-driven, STRUCTURAL on the fuel
  | 0, _, _ => [] | _+1, [], q => q | _+1, p, [] => p
  | f+1, a :: p, b :: q =>
      if mlt a.1 b.1 then a :: mergeAux f p (b :: q)
      else if mlt b.1 a.1 then b :: mergeAux f (a :: p) q
      else let c := a.2 + b.2
           if c == 0 then mergeAux f p q else (a.1, c) :: mergeAux f p q
def padd (p q : Poly) : Poly := mergeAux (p.length + q.length) p q
def smul (m : Mono) (c : Int) (p : Poly) : Poly := p.map (fun x => (madd m x.1, c * x.2))
def pmul (p q : Poly) : Poly := p.foldr (fun x acc => padd (smul x.1 x.2 q) acc) []
```

Everything is structural recursion (fuel for the merge — `Nat.rec` on a literal is O(1) per
step in the kernel, no unary trap) and `mlt` is built from `Nat.blt`, which is GMP-accelerated.
`padd`/`pmul` preserve the canonical form, so **no `normalise` is needed at all**: the final
check is plain `List` equality, closed by `rfl`, proof term `Eq.refl`.

### 13.2 The curve `[MEASURED]`

Work unit `W := |p|·|q| + |p|·|R|` (monomial products + merge steps). `lake env lean -j1`,
wall clock includes ~3 s of Mathlib import. **`native_decide` was not used and is not needed.**

| case | \|p\| | \|q\| | \|R\| | W | tactic | time | W/s | peak RSS |
|---|---|---|---|---|---|---|---|---|
| A | 20 | 5 | 100 | 2.1·10³ | `rfl` | 3.9 s | — | 1.5 GB |
| B | 100 | 5 | 296 | 3.0·10⁴ | `rfl` | 24.5 s | 1.4·10³ | 1.6 GB |
| C | 400 | 16 | 844 | 3.4·10⁵ | `rfl` | 92 s | 3.7·10³ | 1.7 GB |
| C′ | 400 | 16 | 844 | 3.4·10⁵ | `decide +kernel` | 107 s | 3.2·10³ | 1.7 GB |
| D | 784 | 16 | 1780 | 1.41·10⁶ | `rfl` | 407 s | 3.5·10³ | 1.7 GB |
| D′ | 784 | 16 | 1780 | 1.41·10⁶ | `rfl`, **packed key** | 412 s | 3.4·10³ | 1.7 GB |
| E | 297 | 784 | 3798 | 1.36·10⁶ | `rfl` | **>1140 s**, killed | ≤1.2·10³ | 1.73 GB → **0.34 GB** |

Coefficients throughout are the real certificate's, 58–76 bits.

**Throughput: ≈ 3.5·10³ work units per second for *sparse × dense*, at a flat ~1.7 GB.**

Case E is the exception and it is instructive: it is the only **dense × dense** product
(`|q| = 784` rather than 5–16) and it runs at **≤1.2·10³ W/s, a 3× penalty**, because each
`smul` now builds a 784-monomial list that is then merged into an accumulator of up to 3798.
Its RSS also *fell* to 0.34 GB as the GC reclaimed intermediates — memory is not merely flat,
it is small. **Corollary: never hand the kernel a dense × dense product; chain by sparse
factors.** This is the same ordering discipline `ring` needed, for a different reason.

### 13.3 Four findings that change what to build

1. **Memory is constant.** 1.5 GB at W = 2·10³, 1.73 GB at W = 1.4·10⁶. Compare `ring`:
   >15 GB at the same identity. *This is why reflection is the answer.*
2. **Packing the exponent triple into a single `Nat` (`a·4096 + b·64 + c`, one `Nat.blt`
   compare and one `Nat.add` per monomial instead of five and three) buys exactly 0 %**
   — 412 s vs 407 s. The bottleneck is `List`/`Int` whnf overhead, not monomial arithmetic.
   **Do not spend effort on the monomial representation.**
3. **`decide +kernel` is 15 % slower than `rfl` at small sizes — but `rfl` is NOT memory-flat
   at large ones, and `decide +kernel` is. CORRECTED, see §15.4.** At `|R| = 844` both sat at
   1.7 GB; on the real `KeyPoly` the `rfl` route reached **9.5 GB and was still climbing at
   357 s CPU**, because the *elaborator's* `isDefEq` caches every intermediate of the
   computation, whereas the kernel does not. **Use `decide +kernel` for anything at
   certificate scale**; pay the 15 %.
4. **Coefficient bit-length is not a driver in the 58–76-bit range** — case D (60–76 bits) ran
   at the same rate as case C (≈58 bits). GMP `Nat` ops are O(1) here. Untested above ~200 bits.

### 13.4 Projection

`KeyPoly` with the multiplication chained by sparse factors (the same ordering discipline that
`ring` needed):

| piece | W |
|---|---|
| build `Σ_i c_i P_i` (4 × cq·PP + merges) | 5·10⁴ |
| `× (n+1)²(n+2)²`, `× (n+l+2)(n+l+3)`, `× (k+l+1)(k+l+2)`, `× (k+1)³(l+1)³` | 1.4·10⁵ |
| `U₁·A(n,k+1,l)`, `U₂·A`, `U₃·B(n,k,l+1)`, `U₄·B`, chained by the `U` factors | 3.4·10⁵ |
| final merges | 2·10⁴ |
| **total** | **≈ 5.5·10⁵** |

⇒ **`KeyPoly` ≈ 3–5 minutes of kernel time at ~1.7 GB.** The identity `ring` cannot do at all.

**For the 42 `w★` blocks:** taking each block at ~3× the Q row (larger cofactors, extra
denominator factors), W ≈ 1.5·10⁶ per block ⇒ ~7 min each ⇒ **≈ 5 h serial, and the blocks are
independent, so 42 one-block modules on 12 cores land in well under an hour of wall clock, at
1.7 GB per process.** Answer to the coordinator's question: **hours, not days** — and the
memory ceiling that killed `ring` never appears.

### 13.5 What the certificate agent should optimise — revised, and it is not what I said before

Sparse-expanded-over-ℤ remains right. Two refinements now that the cost model is measured:

1. **Minimise Σ of *intermediate* sizes, not the final size.** The cost is
   `Σ_steps (|p|·|q| + |p|·|R|)`, so a dense × dense product is quadratic while a chain of
   sparse multipliers is near-linear. Therefore: **deliver each block as (i) an explicit
   product tree whose factors are small — ideally the linear/quadratic factors as they come
   out of the ansatz denominators — together with (ii) the fully expanded final answer.** The
   kernel then walks the chain. Delivering only the expanded product forces me to reconstruct
   an ordering, and delivering only the factored form forces a dense multiply at the end.
2. **Coefficient height is free below ~10²⁰; monomial count is not.** Do not spend CAS effort
   shrinking coefficients. Do spend it on the common-factor cancellations — e.g. in the Q row
   `(k+1)³(l+1)³` divides *every* term of the cleared identity (3798 → 2037 monomials, a 46 %
   cut, and a 46 % cut in checking time). Expect an analogous factor per block.

### 13.6 The soundness layer — **written, compiled, clean** `lean/ZetaLucas/Reflect.lean`

288 lines, **compiles in 11 s**, `lake build` clean (8676 jobs). Delivered:

```lean
abbrev Mono := ℕ × ℕ × ℕ            abbrev Poly := List (Mono × ℤ)
def mergeAux : ℕ → Poly → Poly → Poly       def padd, smul, pmul, pneg, psub, ppow
def mval, eval  (into any `CommRing R`)     def pC, pN, pK, pL
theorem eval_mergeAux (n k l : R) : ∀ f p q, p.length + q.length ≤ f →
    eval (mergeAux f p q) n k l = eval p n k l + eval q n k l
theorem eval_padd, eval_smul, eval_pmul, eval_pneg, eval_psub, eval_ppow
theorem eval_congr {p q : Poly} (h : p = q) (n k l : R) : eval p n k l = eval q n k l
```

**`#print axioms`, verbatim:**

```
'ZetaLucas.Reflect.eval_mergeAux' depends on axioms: [propext, Quot.sound]
'ZetaLucas.Reflect.eval_padd'     depends on axioms: [propext, Quot.sound]
'ZetaLucas.Reflect.eval_smul'     depends on axioms: [propext, Quot.sound]
'ZetaLucas.Reflect.eval_pmul'     depends on axioms: [propext, Quot.sound]
'ZetaLucas.Reflect.eval_pneg'     depends on axioms: [propext, Quot.sound]
'ZetaLucas.Reflect.eval_psub'     depends on axioms: [propext, Quot.sound]
'ZetaLucas.Reflect.eval_ppow'     depends on axioms: [propext, Quot.sound]
'ZetaLucas.Reflect.eval_congr'    does not depend on any axioms
```

**Not even `Classical.choice`** — the layer is *cleaner* than the programme's bar, and there is
no `native_decide` anywhere.

**One design decision worth recording.** Proving the merge sound would normally require that
`mlt` be a total order (`¬(a<b) → ¬(b<a) → a = b`), which is a fiddly case split. Instead
`mergeAux` tests `a.1 = b.1` **explicitly** first, and each of the three branches is sound on
its own — the two `mlt` branches emit a correct head *whichever* of `a`, `b` is smaller. So
**`mlt` only has to be some `Bool`**: it makes the output canonical, not correct. Soundness is
then order-free, and the extra `Mono` equality test costs nothing (finding 2 above).

**`.olean` size: 661 KB.** Compare `BZQRow.olean` at **172 MB** — that file's six *degree-14*
`ring` calls alone. Two orders of magnitude, and the reflective one carries the harder theorems.

A worked end-to-end client example is in the file (§6), showing the pattern: `rfl` on the
`Poly` identity, `simp only` along the soundness lemmas, no `ring` call seeing more than a
handful of monomials.

**Still to do:** the client glue for `KeyPoly` itself — bridging `Dstar n k l`, `PP_i`, `U_i`,
`cq_i`, `Amid`, `Bmid` to their `Poly`s and assembling the chain. Two design points are already
fixed by the measurements above:

* the bridges for the **small** polynomials are free — express the `Poly` side as a `pmul`
  chain of two-monomial factor polys and each bridge is `ring` on ≤ 4 monomials;
* the bridges for **`Amid` (1133 monomials) and `Bmid` (239)** must *not* go through `ring`
  (a flat 1133-term sum costs `ring` ~6·10⁵ operations — over budget). Instead **redefine
  `Amid`/`Bmid` in `BZQRow.lean` as `eval AmidP`/`eval BmidP`**, making those bridges `rfl`.
  Nothing else in the development touches their internals (`Rq_bot` needs only the `k³`/`l³`
  factor, which lives in `Anum`/`Bnum`), so this is a safe, local change.

If the soundness layer turns out to be harder than expected I will say so; nothing measured so
far suggests it will be. `native_decide` has not been used anywhere and will not be.

## 14. CORRECTION — the antisymmetric bridge `PhatSum = PStarSum` is **impossible**

Recorded here because it is the obvious cheap route and a reader will ask why it was dropped.

> Suppose `w − ŵ₃` is `k↔l`-antisymmetric for an admissible `w`; then `sym w = ŵ₃^sym`. The
> order-3 admissible space `W_tel` is **σ-stable** — from `L_BZ·(T·w) = Δ_k R + Δ_l S`,
> swapping `k ↔ l` and using `T(n,k,l) = T(n,l,k)` gives `L_BZ·(T·wᶜ) = Δ_l Rᶜ + Δ_k Sᶜ` — and
> it is linear (`dim W_tel(n) = 37` for `n ≥ 2`, `Z5CF_REP` §3.1), hence closed under
> `sym = ½(1+σ)`. So `w ∈ W_tel` forces `ŵ₃^sym ∈ W_tel`, which `Z5CF_REP` §3.2 excludes at
> four values of `n` and two primes. Contradiction. ∎

**Consequence: every successful representative uses a nonzero *symmetric* element of the
58-dimensional kernel `K`, so the bridge cannot collapse to one `Finset.sum_comm`.**

Actions taken in `lean/ZetaLucas/BZStar.lean`:

* `sum_antisym_zero` **kept** — it is true, one line, and it is the proof that 45 of the 58
  dimensions of `K` are free (`T_symm`).
* `PhatSum_eq_PStarSum_of_antisym` **kept but marked shut** (`⛔ NOT THE ROUTE`), with the
  impossibility argument in the §6 header, so a successor who rediscovers the idea finds it
  already closed rather than re-deriving it.
* **New: `DivCert R₀ S₀`** — a structure carrying exactly the order-zero divergence
  certificate the certificate agent will deliver:
  `T·(w★ − ŵ₃) = Δ_k R₀ + Δ_l S₀` plus `R₀|_{k=0} = R₀|_{k=n+1} = S₀|_{l=0} = S₀|_{l=n+1} = 0`.
* **New: `PhatSum_eq_PStarSum_of_divCert : DivCert R₀ S₀ → ∀ n, PhatSum n = PStarSum n`** —
  proved, clean axioms. Top boundaries at `k,l = n+1`: both sums are over `range (n+1)` and no
  range extension is needed because the certificate is order zero.

So the bridge has a home the moment the order-0 certificate lands, and it is one more customer
for the same checker — with a single copy of `T` instead of four, so **smaller** than any
order-3 block: at the measured rate, seconds.

**None of this is on the critical path.** `PStarSum_eq_Phat_of_rec` reaches `Phat` directly via
`eq_of_BZRec` and the three initial values of §3; it never goes through `PhatSum`.

---

# ADDENDUM 3 — `KeyPoly` closed, and a sign bug the attempt caught

## 15. The Q-row recurrence is now unconditional

`lean/ZetaLucas/BZQRow.lean` no longer carries `KeyPoly` as a hypothesis. The chain is

```lean
theorem key_check : LHSP = RHSP := by rfl          -- kernel; proof term Eq.refl
theorem key_poly  : KeyPoly := fun n k l =>
  (eval_LHSP n k l).trans ((eval_congr key_check n k l).trans (eval_RHSP n k l).symm)
theorem QSum_bzrec : BZRec QSum                    -- no hypothesis
theorem Q_bzrec    : BZRec (fun n => (Q n : ℚ))
theorem Q_rec (n : ℕ) : cc0 n * Q n + cc1 n * Q (n+1) + cc2 n * Q (n+2) + cc3 n * Q (n+3) = 0
theorem QSum_eq_QBZ (n : ℕ) : QSum n = QBZ n
theorem Q_eq_QBZ    (n : ℕ) : (Q n : ℚ) = QBZ n
```

### 15.1 How the glue is built

* **`Amid` and `Bmid` are now *defined* as `eval AmidP` / `eval BmidP`** over their sparse
  tables (1133 and 239 monomials), exactly as §13.6 required: the bridge to the certificate is
  then `rfl` instead of a ~6·10⁵-operation `ring` call. Nothing else in the development touches
  their internals.
* **Two new operations in `Reflect`**, `substK` and `substL`, giving `p(n,k+1,l)` and
  `p(n,k,l+1)`. They are built *out of the operations already proved sound* —
  `(k+1)^b = ppow (padd pK (pC 1)) b` — so the soundness proofs are two short inductions with
  **no binomial-theorem reasoning**. Every WZ certificate in this programme evaluates its
  cofactors at shifted arguments, so these are permanent infrastructure, not Q-row-specific.
* **Every product is written small-factor-first** and chained by the sparse factors of `D*`,
  `U₁…U₄`, per §13.5.
* **22 linear/quadratic factor `Poly`s** with one-line bridges; `X1P…Y3P`, `PP0P…PP3P` built
  from them by `pmul`, so their bridges are `ring` calls on *atoms*. The two big bridges,
  `eval_LHSP` and `eval_RHSP`, are degree-≤14 `ring` calls with `PP_i`, `cq_i`, `Anum`, `Bnum`
  as atoms — well inside the measured budget.

### 15.2 ⚠ The attempt caught a real sign error in the shipped file

Before running anything in Lean I re-implemented the *exact* `padd`/`pmul`/`ppow`/`substK`
computation in Python and compared `LHSP` with `RHSP` as sorted lists. First run:

```
|LHSP| = 3798   |RHSP| = 4258     LHSP == RHSP : False    differing monomials: 4258
```

Two bugs, both found this way and neither of which any earlier check could have caught:

1. **`AnumP` used `(k+1)³` where `Anum n k l = k³·Acore n k l` uses `k³`.** Only the *shifted*
   numerator `Anum n (k+1) l` carries `(k+1)³`. Fixed by using `pK`/`pL` for the unshifted ones.
2. **`Acore` had a spurious minus sign.** The file shipped
   `Acore := -((n+l+1) * Amid)`, but `Amid` was extracted as `A / (k³(n+l+1))` and *already
   carries the sign of `r_num`*. So the shipped `Anum` was `−A`, which means **`KeyPoly` as
   previously stated was FALSE**. It had never been detected because `KeyPoly` was only ever a
   hypothesis — every theorem downstream was vacuously fine, and the numerical checks of §2
   validated the *certificate*, not the *transcription of `Acore`*.

After both fixes:

```
AnumP == A : True  (1294 = 1294)     BnumP == B : True  (1151 = 1151)
|LHSP| = 3798   |RHSP| = 3798        LHSP == RHSP : True
```

**This is the strongest argument for closing hypotheses rather than carrying them.** A
`sorry`-free conditional theorem with a false hypothesis looks exactly like a correct one in
`#print axioms`. The only thing that distinguishes them is discharging the hypothesis — which
is precisely what the checker now makes affordable. Recommend the same Python-side
pre-simulation for each of the 42 `w★` blocks before any kernel time is spent: it costs
seconds and it found two transcription bugs on the first object attempted.

### 15.3 A note for L6 on `DivCert`

`DivCert.Rbot`/`Sbot` are stated on the **assembled** cofactors `R₀`, `S₀` — single
`ℕ → ℕ → ℕ → ℚ` functions — not blockwise. So the collapse-class grouping at `k = 0`
(`H_k → 0`, `H_{n+k}, H_{n−k} → H_n`, `H_{k+l} → H_l`, `H_{n+k+l} → H_{n+l}`) is already
accommodated: only the *sum over blocks* has to vanish. No change to the structure is needed,
and L6 should not feel obliged to make each block vanish separately.

### 15.4 Kernel cost of `key_check`, and the one optimisation it exposes

The first attempt spent 15 minutes without reaching `key_check` at all: the 1133-entry `AmidP`
list literal blew the default 200 000-heartbeat budget during **elaboration**, and the
cascading errors consumed the rest. `set_option maxHeartbeats 0` fixes it. **Recording this
because it is a trap the 42-block job will hit 26 times**: a multi-thousand-entry `Poly`
literal needs the heartbeat limit lifted *before* any kernel work is attempted, and a failure
there looks exactly like a slow proof.

`key_check : LHSP = RHSP := by rfl` is a **terminating** computation — the merge is
fuel-bounded and every other recursion is structural — so its cost is a duration, not a risk.
One optimisation is already visible and should be made before the 42-block job:

> **`substK`/`substL` are the bottleneck, not the products.** As written they rebuild
> `ppow pN a` and `ppow pL c` *per monomial* — for `AmidP` that is 1133 × (up to 24 + 8)
> single-monomial `pmul`s, each allocating a fresh list. The fix is one line: multiply by the
> monomial `(a, 0, c)` with **`smul`** (a `List.map`) instead of by `ppow pN a * ppow pL c`.
> That replaces ~4·10⁴ full `pmul` calls with ~1·10³ maps and should recover the projection.

For the 42-block `w★` job this matters: `Z5STAR_CERT.md` §6 reports **26 cofactor polynomials,
≤ 94 595 monomials of `ℤ[n,k,l]` in total, `deg_n ≤ 50`, `deg_k, deg_l ≤ 12`** — that is 38.7×
the Q row's 2445 cofactor monomials, spread over 42 independent identities of roughly Q-row
size each. At the measured 3.5·10³ W/s that is **≈ 1.5–2 h serial, ~10 min wall on 12 cores**
if each block is its own module — *after* the `substK` fix, and it is worth doing that fix
first.

### 15.5 Two corrections from `Z5STAR_CERT.md`, applied to `BZStar.lean`

1. ⛔ **`DivCert` can never be discharged.** `Z5STAR_CERT.md` §7 proves no order-zero divergence
   certificate `T·(w★ − ŵ₃) = Δ_k R₀ + Δ_l S₀` exists for any weight whose difference has a
   nonzero maximal component, and that any bridge *operator* must annihilate `Q` — hence order
   ≥ 3, hence (as `ŵ₃ ∉ W_tel`) **order ≥ 4**. `DivCert` and
   `PhatSum_eq_PStarSum_of_divCert` are kept as markers, labelled `⛔ UNSATISFIABLE`, exactly
   like the antisymmetry route. **Neither is on the critical path**:
   `PStarSum_eq_Phat_of_rec` reaches `Phat` through `eq_of_BZRec` and the three initial values,
   never through `PhatSum` — the `w★` row *is* the `P̂` row because both satisfy `L_BZ` with the
   same three initial values, which is stronger and cheaper than any weight-level bridge.
2. **The certificate's subtracted letters live at base `n+3`**, i.e. `H^(r)_{n+3−k}`,
   `H^(r)_{n+3−l}`, not `H^(r)_{n−k}`, `H^(r)_{n−l}`, and that mixed base is what cancels the
   interior poles. Added to `BZStar.lean` §1.1:

   ```lean
   theorem Harm_sub_succ_n3 {r} (hr : 0 < r) (n x : ℕ) :
       Harm r (n + 3 - x) = Harm r (n - x) + 1/((n+1-x : ℕ) : ℚ)^r + 1/((n+2-x : ℕ) : ℚ)^r
                                            + 1/((n+3-x : ℕ) : ℚ)^r
   ```

   — three applications of `Harm_sub_succ_n`, and like its parent it needs **no `x ≤ n`
   hypothesis**, so the conversion is free at every point of the telescoping range.

---

# ADDENDUM 4 — coefficient height is free; `KeyPoly` needs the same chain-split as `ring`

## 16.1 Height axis `[MEASURED]` — the warning can stay withdrawn

Same product throughout (`|p| = 400`, `|q| = 16`, `|R| = 844`, the §13 case C), coefficients
scaled by `2^b` so that **only** the height changes. `decide +kernel`:

| max coefficient | digits | wall | max RSS |
|---|---|---|---|
| 63 bits | 19 | 82 s | 2.67 GB |
| 575 bits | 174 | **74 s** | 2.68 GB |
| 4 159 bits | 1 252 | 97 s | 2.69 GB |

**Flat to within noise across a 66× range in height, and RSS moves by 20 MB.** GMP does the
arithmetic and the cost is dominated by list-cell traffic, not by the integers. The delivered
`CERT_wstar_sparse.json` at ≤122 bits is comfortably inside the free regime — 1.6× the Q row,
not a change of regime. **L6 should not spend its gauge lever on height.** It should spend it
on (B-bot).

One caveat worth stating: *source size* is not free even when arithmetic is. At 9 884 digits the
same 400-monomial table is a 12 MB Lean file and at 39 476 digits it is 48 MB. Height is free to
*compute with*, not to *ship*.

## 16.2 `KeyPoly` in one kernel evaluation: **12.7 GB, killed** — and the fix

| route | outcome |
|---|---|
| `by rfl` | 9.5 GB at 357 s CPU, still climbing, killed. The *elaborator's* `isDefEq` caches every intermediate. |
| `by decide +kernel` (+ `Dstar_group` to keep the one degree-14 `ring` out of `eval_LHSP`) | **12.7 GB at 229 s CPU, still climbing, killed.** |

So §13.3 finding 1 — "memory is constant" — **holds only up to about `|R| ≈ 1 800`**. Measured
scaling of the *computation's* memory (RSS minus the ~1.5 GB Mathlib baseline):

```
|R| =  844  ->  1.2 GB          |R| = 1780  ->  ~1.5 GB       |R| = 3798 (+ substK over 1133)  ->  >11 GB
```

The kernel's `whnf` cache grows with the total number of cells produced *inside a single
declaration*, and is released only when the declaration closes. **This is the same wall as
`ring`'s, an order of magnitude further out.** `ring` died at ~4·10³ monomials of normal form;
the checker dies at ~4·10³ monomials *plus* a 1133-monomial `substK`, i.e. after roughly 10×
the work — but it does die.

**The fix is the fix that already worked twice: one operation per declaration.** Emit the
intermediate `Poly`s explicitly and chain

```lean
theorem s1 : pmul G1P SP  = S1P := by decide +kernel     -- |R| =  980
theorem s2 : pmul G2P S1P = S2P := by decide +kernel     -- |R| = 1323
theorem s3 : pmul G3P S2P = S3P := by decide +kernel     -- |R| = 2037
theorem s4 : pmul G4P S3P = WP  := by decide +kernel     -- |R| = 3798
…
theorem key_check : LHSP = RHSP := by rw [s1, s2, s3, s4, …]
```

Each declaration's cache is freed when it closes, so peak memory is that of the *largest single
step*, not of the whole computation. At the measured 1.4 MB per produced monomial that is
≈ 5 GB for the 3798-monomial step and under 3 GB for every other — it fits, and every step is
independently checkable by the Python pre-simulation. Cost: ~9 k monomials of extra emitted
text for the LHS chain and ~17 k for the RHS, exactly as §4 row 3 described for `ring`.

**This is bounded, mechanical work that I did not have time to finish.** Nothing about it is
uncertain: the identity is confirmed (`LHSP == RHSP`, 3798 = 3798), the checker is proved sound,
and the only change is where the declaration boundaries go.

## 16.3 State of the tree

`lake build` clean, 8676 jobs, 7 m 27 s. `BZQRow.lean` is back in its **conditional** form —
`QSum_bzrec (hkey : KeyPoly) : BZRec QSum` — with **the `Acore` sign bug fixed**, so `KeyPoly`
as now stated is *true* and simply undischarged, which is the honest state. The generated glue
(22 factor `Poly`s, `X1P…PP3P`, `cq0P…cq3P`, `AmidP`, `BmidP`, `LHSP`, `RHSP`, the bridges) is
reproducible from §15.1 and the certificate; regenerating it is minutes, and the chain-split
above is the only new thing needed.

## 16.4 For the 42 blocks

* **29 of 42 are free** once `KeyPoly` closes (`linear_combination (w_j) * KeyPoly`), so the
  real work is **13 blocks**.
* Sizes are final and inside the model: 93 073 monomials, `deg_n ≤ 50`, `deg_k, deg_l ≤ 12`,
  ≤122-bit numerators.
* **Hold the `star_creative_telescoping` discharge** until the (B-bot)-satisfying re-lift lands.
  The delivered gauge satisfies (★) and (B-top) but not the 16 collapse-class rows, so the
  rectangle sum does not collapse and `BZRec PStarSum` does not follow. Building the glue
  against the current file is not wasted — a gauge change moves coefficients, not structure.
* Atoms are `Harm r (n+3−k)` / `Harm r (n+3−l)`; `BZStar.Harm_sub_succ_n3` is the conversion and
  needs no `x ≤ n` hypothesis. (P-int) retires "Lemma N".
* `dn(n)` carries a factor `n`, so the certificate covers `n ≥ 1`; `n = 0` is already
  kernel-checked in `BZClosedForm` §3.1. The induction base is in hand.
