# Z5STAR_CERT — the `w★` order-3 certificate: family choice, (B-bot)/(B-top), the lift, the size table

**Agent:** computational-agent (River's odd-zeta programme), 2026-07-26
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, new code and data in `work/z5star/`
**Predecessors:** `work/Z5CF_REP.md` (the order-3 representative `w★`), `work/LEAN_Z5_SCAFFOLD.md` §5
(the interface), `work/LEAN_QROW.md` (the `ring` ceiling and the reflective-checker decision),
`work/Z5CF_TELESCOPER.md`, `work/Z5CF_LIFT.md`
**Labels:** `[PROVED]` · `[VERIFIED range]` · `[MEASURED]` · `[EXCLUDED with bounds]`
**Protected modules were extended, never edited:** nothing under `work/z5rep/`, `work/z5la/`,
`work/z5barnes/`, `work/z5eps/` or `lean/` was modified.

---

## 0. HEADLINE

1. **Keep `w★`.** Four candidate members of the 12-dimensional affine family were built exactly
   over ℚ and all four have the **identical minimal cofactor ansatz** `[MEASURED]`. `w★` wins on
   the remaining criteria (smallest coefficient denominators `{1,2}`, fewest hard blocks, already
   transcribed and kernel-checked in `lean/ZetaLucas/BZStar.lean`). §2.
   The family is **σ-stable** with `dim U = 12 = 3(sym) ⊕ 9(anti)` `[MEASURED, exact ℚ]`, and
   **no member has `w − ŵ₃` purely antisymmetric** `[EXCLUDED, exact ℚ]` — found here
   independently, by an inconsistent linear system *and* by the σ-stability argument. The
   minimum reachable `J` is 40 (against `w★`'s 42) and `N_hard` cannot go below 13. §2.1–2.3.

2. **The certificate is far smaller than the apparatus that found it** `[MEASURED]`. The
   denominator, measured by stripping it one factor at a time, is
   `D = (k+l+1)(n+k+1)(n+k+2)(n+k+3)(n+l+1)(n+l+2)(n+l+3)` and the cofactor numerators have
   bidegree **(12,12)** in `(k,l)` — against the `(32,32)`/`nc = 2178` of `Z5CF_REP` §3's scan.
   Per letter block `nc` goes **1250 → 338** and for the `()` block **1458 → 578**; the joint
   system goes **7290 → 1346 columns**, a 5.4× reduction, and one solve costs seconds rather
   than minutes. §4.

3. **The `n`-lift succeeds and the common denominator is fully explicit** `[MEASURED]`:
   ```
   dn(n) = n (n+1)^4 (n+2)^4 (n+3)^2 (n+4)^2 (n+5)^2 (n+6)^2 (n+7)^2      (degree 19)
   ```
   All **2416** nonzero cofactor coefficients reconstruct as rational functions of `n` from a
   116-point sweep, with 0 failures. §5.

4. **Size table, and it is better than `LEAN_QROW` predicted** `[MEASURED]`. 26 cofactor
   polynomials (13 blocks × `ρ,σ`), each `deg_n ≤ 50`, `deg_k ≤ 12`, `deg_l ≤ 12`, totalling
   **93 073 monomials of `ℤ[n,k,l]`** with **≤ 122-bit** numerators and **≤ 14-bit** denominators.
   The 24-prime lift is **complete — 0 of 96 813 coefficients unliftable**, held-out check
   **0 mismatches in 889 728 identities**. Delivered as
   `work/z5star/CERT_wstar_sparse.json` (7.7 MB). `LEAN_QROW` §9 forecast ~4·10⁵ monomials and
   coefficients well above the `Q` row's 76 bits; the truth is a quarter of the monomials at
   1.6× the height. §6.

   The delivered file is **re-verified from scratch in exact ℚ** by `work/z5star/check6.py`,
   which shares no code with the mod-`p` machinery: **6636 identities at `n,k,l ≤ 6`,
   0 mismatches**. §8.1a.

5. **(B-bot) reduces to one rational single-sum identity, and that identity is verified to hold.**
   The sharp form of (B-bot) is a *collapse-class* condition, not the per-block `k | N_ρ` of the
   brief (§3.1). Of the **17** classes that need a constraint, **16 are simultaneously satisfiable**
   `[VERIFIED, 360 rows, nbad = 0]` and all 29 maximal blocks satisfy (B-bot) for free. The
   remaining one — the **empty monomial** — is infeasible `[EXCLUDED with bounds]`, but once the 16
   are imposed the whole bottom boundary collapses to two **purely rational** single sums whose
   total is
   > `Σ_{l=0}^{n+3} Φ(n,0,l)ρ_()(n,0,l) + Σ_{k=0}^{n+3} Φ(n,k,0)σ_()(n,k,0) = 0`
   > `[VERIFIED, n = 1…13]` — **exactly zero at every `n` tested**.

   So the certificate's boundary contribution genuinely cancels; what is missing is a
   *Lean-checkable one-variable certificate* for that identity. Neither half is Gosper-summable on
   its own `[EXCLUDED with bounds]`, so the two must be certified together — a one-variable WZ
   problem on an explicitly-known rational summand, and the smallest open object in the campaign. §3.

6. ⚠ **The order-0 bridge asked for in the last coordinator message does not exist.**
   `T·(w★ − ŵ₃) = Δ_k R₀ + Δ_l S₀` with vanishing boundaries is **impossible** `[PROVED]`, and
   the same argument forces any bridge operator to annihilate `Q`, hence to have order ≥ 3, hence
   — since `ŵ₃ ∉ W_tel` — **order ≥ 4**. §7.

7. ⚠ **Two messages for `lean/ZetaLucas/BZStar.lean` specifically.**
   * Its §6 says "the bridge will arrive as an **order-zero divergence certificate**
     `T·(w★ − ŵ₃) = Δ_k R₀ + Δ_l S₀`, whose shape is `DivCert`". **`DivCert` can never be
     discharged** — §7 proves no such certificate exists, for any weight whose difference has a
     nonzero maximal component, and gives the replacement (a left multiple of `L_BZ` of order ≥ 4).
   * The certificate's atoms for the two subtracted letters are **`Harm r (n+3−k)` and
     `Harm r (n+3−l)`**, *not* `Harm r (n−k)`, `Harm r (n−l)`. This **mixed base is not
     cosmetic**: it is exactly what makes the interior poles cancel (§2.4), and the bare-at-`n`
     normalisation does **not** cancel them (`P_i` carries `(n+j−k)²` for `j > i`, while
     bare-at-`n` puts the poles at `j ≤ i`). Converting is three applications of
     `Harm_sub_succ_n` per letter and must be done before the componentwise identity is stated.

8. **A bonus that removes an unproved obligation.** The mixed base at `n+3` plus one explicit
   condition on the support — no `H⁽³⁾_{n−k}`, no `H⁽¹⁾_{n−k}H⁽²⁾_{n−k}` (and the `l` mirrors) —
   makes every interior pole at `k = n+1,n+2,n+3` cancel identically. `w★` satisfies it. This is
   exactly "**Lemma N**", which `LEAN_QROW` §6 flagged as *numerically verified but not proved*
   extra Lean work for `ŵ₃`; for `w★` it is not needed at all. §2.4.

---

## 1. What was recovered, and how

`work/z5rep/joint.py` computes the 13-dimensional `λ`-space but saves only one member of it.
`work/z5star/fam.py` re-runs the joint solve at `n = 9, 11, 13` and saves the **whole cumulative
`λ`-space**, then `work/z5star/opt.py` rationalises it.

| quantity | value |
|---|---|
| `λ`-space inside the 17 `ws`-coordinates | **13**, identical at `n = 9, 11, 13` |
| tangent space `U` (the `λ₀ = 0` part), as an exact-ℚ subspace of ℚ¹⁰⁹ | **12** |
| control weight `w = 1` (the `Q` row), full cascade | **closes** — ansatz adequate |
| `Σ_{k,l} T·base = P̂` | `[VERIFIED exact ℚ, n = 0…14, every cell]` |
| every one of the 12 tangent directions in `K` | `[VERIFIED exact ℚ, n = 0…10]` |

Data: `work/z5star/famlam_p4194301.pkl`, `work/z5star/familyQ.pkl` (base + 12 directions, exact ℚ).

---

## 2. JOB 1 — the family member

### 2.1 The family is σ-stable, and that settles the antisymmetry question

`[MEASURED, exact ℚ]` `σ(U) ⊆ U` and `σ(base) − base ∈ U`; so the whole affine family is
`k↔l`-stable, and `U = U^sym ⊕ U^anti` with **dim `U^sym` = 3**, **dim `U^anti` = 9**.

> **`[EXCLUDED, exact ℚ]` No member `w` of the family has `w − ŵ₃` purely antisymmetric.**
> The linear system `Σ λ_i·sym(U_i) = sym(ŵ₃) − sym(base)` is **inconsistent**.

The structural reason (independent of the solve, and it agrees with the coordinator's own
derivation, found here independently): if `w − ŵ₃` were antisymmetric then `sym(w) = ŵ₃^sym`;
the family is σ-stable and affine, so `sym(w) = ½(w + w^σ)` is again in the family, putting
`ŵ₃^sym ∈ W_tel` — which `Z5CF_REP` §3.2 excludes at `n = 9,11,13,17` and two primes. ∎

Consequently **every** successful representative uses a nonzero *symmetric* element of `K`, and
the symmetric defect `d_sym = sym(w) − ŵ₃^sym` ranges over an affine space of dimension **3**
inside the 13-dimensional symmetric part of `K`. It is nonzero for every member.

### 2.2 The candidates, measured head to head

`work/z5star/cands.py`. All four are `[VERIFIED exact ℚ]` representatives of `P̂` (`n = 0…10`)
and all four satisfy (P-int) of §2.4.

| member | support | `J` | hard blocks | letters | coefficient denominators | symmetric | minimal ansatz |
|---|---|---|---|---|---|---|---|
| **`w★`** (base) | **29** | 42 | **13** | 13 | **{1, 2}** | no | `M0`, bidegree **(12,12)** |
| `w_min` | 27 | 40 | 13 | 13 | {1, 2, 4} | no | `M0`, (12,12) |
| `w_sym = sym(w★)` | 42 | 58 | 16 | 17 | {2, 4} | **yes** | `M0`, (12,12) |
| `w_symmin` | 41 | 57 | 16 | 16 | {1, 2, 4} | yes | `M0`, (12,12) |

**The decisive measurement is the last column: the minimal cofactor ansatz is the same for all
four** (probed at `n = 9` with (B-bot) forcing on, `nc = 312`; the delivered unforced ansatz has
`nc = 338` at the same bidegree)**.** Criterion (a) of the revised brief — lowest cofactor degrees — does not distinguish them.
So the choice falls to the tie-breaks:

* `w★` has the **smallest coefficient denominators** (`{1,2}`; the others need `4`), which is
  the direct driver of integer coefficient height after clearing;
* `w★` has **13 hard blocks** against the symmetric members' 16. The σ-equivariance saving a
  symmetric member offers (`σ_j = ρ_{σ(j)}∘swap`, halving the delivered functions — `[PROVED]`:
  if `(R,S)` is a certificate then so is `(σS, σR)`, and the average is σ-equivariant) is real,
  but it buys a factor 2 on the cofactors while costing 16 extra `J`-components and 13 extra
  weight monomials on the left-hand side. With the reflective checker removing `J` as the binding
  constraint, this is close to a wash and does not justify moving;
* `w★` is **already transcribed** in `lean/ZetaLucas/BZStar.lean`, with `PStarSum_zero/one/two`
  computed from the definitions inside the kernel and `#eval PStarSum 3` agreeing with `P̂₃`.
  Switching members would invalidate four kernel-checked transcription points for no measured gain.

> **RECOMMENDATION: keep `w★` exactly as `Z5CF_REP` §4.2 states it and as `BZStar.lean` transcribes
> it.** No family-member change is warranted by any measured quantity.

### 2.3 If block count *were* still the criterion

For the record, since the brief asked for the trade-off explicitly: the minimum `J` reachable over
the family is **40** (`w_min`, support 27), against `w★`'s 42 — a 5 % saving. `N_hard` cannot be
reduced below 13: the coordinates `h1_n*h2_n` and `h1_pkl*h2_n` are **constant and nonzero over
the entire family**, forcing the letters `h1_n, h1_pkl, h2_n` to appear, and every attempt to
remove three of the twelve currently-used `h1/h2` letters turns on three others. Minimum-`J` and
antisymmetric-difference are therefore *both* unreachable at once — the latter is unreachable at all.

### 2.4 (P-int): the interior-pole condition, and why it kills "Lemma N"

**This is new here and it is a hard constraint on any family member.**

`Φ₃`'s `k`-step carries `(n+3−k)²` and `P_i` carries `[Π_{j>i}(n+j−k)]²`. A base letter
`H^(r)_{n+3−k}` contributes a pole `1/(n+j−k)^r`, so the cancellation is exact for `r ≤ 2` and
**fails for total order ≥ 3 in a single `(n+j−k)`**. Hence, in the degree-≤2 weight-3 span,

```
   FORBIDDEN in the support:  H⁽³⁾_{n−k},  H⁽³⁾_{n−l},
                              H⁽¹⁾_{n−k}·H⁽²⁾_{n−k},  H⁽¹⁾_{n−l}·H⁽²⁾_{n−l}.
```

Any weight containing one of those leaves an *uncancelled pole at `k = n+3`* (resp. `l = n+3`) —
an **interior** point of `range (n+4)`, where Lean's `1/0 = 0` makes the componentwise identity
simply false. This is the same failure mode `LEAN_Z5_SCAFFOLD` §5.2 describes for the naive base
`T(n,k,l)`, one level down.

`[VERIFIED]` **`w★` contains none of them**, and neither do any of the four candidates of §2.2.
Mixed products such as `H⁽¹⁾_{n−k}·H⁽²⁾_{n−l}` are safe (the `k`-shift sees only the first factor).

`[MEASURED, with a calibrated control]` `work/z5star/pint.py` evaluates every component of
`E_w/Φ` — a rational function of `(n,k,l)`, so it accepts rational `k` — at
`k = n+j+ε` for `ε = 10⁻¹, 10⁻², 10⁻³`, `j = 1,2,3`, in exact ℚ:

| weight | growth of `max_i |(E_w/Φ)_i|` per 10× closer approach | verdict |
|---|---|---|
| **`w★`** | **1.2** | **finite — no pole at `k = n+1,n+2,n+3`** |
| control `H⁽¹⁾_{n−k}·H⁽²⁾_{n−k}` (a forbidden monomial) | **9.98** | a genuine **simple pole**, exactly as predicted |

The control is the point: the test can see a pole, and `w★` has none.

**Consequence.** `LEAN_QROW` §6 lists, as a *real and unscaffolded* extra obligation for the `ŵ₃`
route, "**Lemma N**": the 15 coefficients `b_j` of `E_{ŵ₃}/Φ` have simple poles at
`k = n+1,n+2,n+3` whose cancellation is legitimate only under Lean's truncation conventions,
"verified numerically on 945 cells, **not proved**". For `w★` in the mixed base at `n+3`, **that
layer does not arise**: every coefficient of `E_{w★}/Φ` and of the shift matrices is pole-free at
those points as a rational function. One unproved obligation is removed, not deferred.

---

## 3. JOB 2 — (B-bot) and (B-top)

### 3.1 (B-bot) is a COLLAPSE-CLASS condition, not a per-block one

(B-bot) is `R_w(n,0,l) = Φ(n,0,l)·Σ_j ρ_j(n,0,l)·M_j(n,0,l) = 0`. At `k = 0` the nine-letter
alphabet **collapses**:

| letter | value at `k = 0` |
|---|---|
| `H^(r)_k` | `H^(r)_0 = 0` — **the whole monomial dies, no constraint** |
| `H^(r)_{n+k}` | `H^(r)_n` — same atom as `H^(r)_n` |
| `H^(r)_{k+l}` | `H^(r)_l` — same atom as `H^(r)_l` |
| `H^(r)_{n+k+l}` | `H^(r)_{n+l}` — same atom as `H^(r)_{n+l}` |
| `H^(r)_{n+3−k}` | `H^(r)_{n+3}` |
| `H^(r)_{n+3−l}` | unchanged |

So distinct basis monomials become the *same* function, and over ℚ(n) with the harmonic values as
independent atoms the sharp condition is

```
   for every collapse class c :   Σ_{j ∈ c} ρ_j(n,0,l) = 0   identically in l,
```

which is **strictly weaker** than the blanket `k | N_{ρ_j}` (`force_k = 1`) that the brief and
`solve.Ansatz` implement. `work/z5star/cert4.py` implements the sharp form as extra linear rows
inside the joint solve. **The distinction is not cosmetic — it is the difference between 16 of the
17 classes being satisfiable and none of them being reachable.**

For `w★` at `n = 9` there are **8 classes in the `k` direction and 9 in the `l` direction** that
need a constraint (`work/z5star/bbotdiag2.py`); the rest either die at the boundary or consist
only of maximal blocks.

### 3.2 What holds `[VERIFIED]`

| obligation | status |
|---|---|
| **(B-top)** `R_w(n,n+4,l) = S_w(n,k,n+4) = 0` | **free** `[PROVED]`. `Φ(n,n+4,l) = 0` because `C(n+3,n+4) = 0`, and every ansatz denominator factor — `(k+l+1)`, `(n+k+j)`, `(n+l+j)` — is **strictly positive** for `n,k,l ≥ 0`, so the `ρ_j` are pole-free there |
| **(B-bot), the 29 maximal blocks** | **free** `[VERIFIED symbolically]`. Their cofactor is `w_j·r_Q`, and `r_Q`'s numerator factors as `−k³(n+l+1)·(…)` while `s_Q`'s vanishes at `l = 0`; this reproduces `Qrow_phicert.m`'s own `"Bbot_r_k0" -> True`, `"Bbot_s_l0" -> True` |
| **(B-bot), the 12 letter blocks** | **holds** `[VERIFIED]`. With the sharp per-block forcing (`work/z5star/cert3.py`) all 12 solve exactly (`nbadL = 0`) and a direct numerical check over 80 random points × 109 blocks finds **0** violations of `ρ_j(n,0,l) = 0` / `σ_j(n,k,0) = 0` |
| **(B-bot), the 16 non-trivial collapse classes** | **each individually FEASIBLE** `[MEASURED]` — one augmented solve per class, `work/z5star/bbotdiag3.py` |
| **(B-bot), the `()` class** | ⚠ **INFEASIBLE** — see §3.3 |

### 3.4 How the 16 (B-bot) rows are imposed — exactly, and for free

The point-sampled version (`work/z5star/gosper.py`) cost ≈ 40 s per `(n,p)`, which would have made
the re-lift a 15-hour job. It is not needed. **At `k = 0` the ansatz numerator collapses:**

```
   ρ_j(n,0,l) = ( Σ_{a,b} c_{ab}·0^a·l^b ) / D(n,0,l) = ( Σ_b c_{0b}·l^b ) / D(n,0,l),
```

so only the `a = 0` row of the `(k,l)` grid survives — **13 of 169** coefficients for a letter
block, **17 of 289** for the `()` block — and since every ansatz block carries the *same*
denominator `D`, a collapse class `c` imposes

```
   Σ_{j ∈ c} c^{(j)}_{0b} = 0      for every power b,
```

an **exact** linear condition with **no sample points at all**. The maximal blocks drop out
identically (`r_Q` has a factor `k³`, `s_Q` an `l³`). That is **195 dense rows** assembled by
numpy indexing in microseconds, and the constrained solve costs **3.6 s per `(n,p)`** — the same
as the unconstrained one, not 40 s.

`[VERIFIED]` at `n = 9, 11`: `nbad0 = 0` with the 195 rows appended; **fresh-point check of all
109 components at 400 unseen points ALL ZERO** (43 600 identities each); and a *direct*
verification that every one of the 16 classes sums to zero at 40 random boundary points —
**0 violations**. At `n = 1,2,3,5,7,9,11,13` the residual `()` boundary sum is **0**
(`work/z5star/bsum2.py`).

### 3.3 The one open obligation, stated exactly

```
   k-dir class 1   members: 1   : INFEASIBLE (24 rows bad)
   l-dir class 1   members: 1   : INFEASIBLE (24 rows bad)
   ALL classes together         : INFEASIBLE (48 bad of 408 (B-bot) rows)
```

`[EXCLUDED with bounds]` `ρ_{()}(n,0,l) = 0` and `σ_{()}(n,k,0) = 0` cannot be imposed, at
`n = 9`, `p = 4194301`, with

* the letter blocks carrying their **full curl gauge**, at letter slack 8, 12, 16 —
  kernel dimension **64, 144, 256** per block, i.e. up to **3072 gauge columns**; and
* the `()` block ranging over the denominators `M0, M2, M4, M5, M6, M7, G0, G1, F1` at slacks
  8–20 (`nc` up to 1458),

rows ≥ 1.3 × columns throughout, and the number of failing rows growing with the ansatz (48, 56,
58 …) rather than shrinking. The empty monomial is a **singleton** collapse class — nothing else
reduces to the constant `1` at `k = 0` — so this constraint cannot be relaxed by grouping.

**Why it is structural, not an ansatz accident.** The only freedom left is the WZ curl
`ρ → ρ + Δ_l τ`, `σ → σ − Δ_k τ`. To reach `ρ_{()}(n,0,l) = 0` one needs
`τ(n,0,l) = −Σ_{l' < l} ρ_{()}(n,0,l')`, i.e. **Gosper-summability of `ρ_{()}(n,0,·)`**, which is
not a rational condition and generically fails. The `Q` row escapes this because its `()` block is
the *whole* certificate and its right-hand side is unpolluted; `w★`'s `()` right-hand side carries
the 12 letter blocks' cofactors.

**What Lean therefore needs, precisely — and it is much smaller than it sounds.** The 360 rows of
the 16 other classes are **simultaneously satisfiable** `[VERIFIED]` — imposing all 360 at once on
the joint system gives `nbad = 0` (`work/z5star/gosper.py`), and only the 48 `()` rows fail out of
408. Impose them. Then every harmonic monomial in `R_w(n,0,l)` is killed, and what survives is

```
   R_w(n,0,l) = Φ(n,0,l)·ρ_{()}(n,0,l) ,      S_w(n,k,0) = Φ(n,k,0)·σ_{()}(n,k,0),
```

**pure rational functions — no harmonic atoms at all**. So with (B-top) free the entire remaining
obligation is the single one-variable identity

```
   Σ_{l=0}^{n+3} Φ(n,0,l)·ρ_{()}(n,0,l)  +  Σ_{k=0}^{n+3} Φ(n,k,0)·σ_{()}(n,k,0)  =  0 .
```

Both summands are explicitly known rational functions, and — the thing that matters —

> `[VERIFIED, n = 1…13, p = 4194301]` **the residual boundary sum is exactly ZERO.**
> `work/z5star/bsum.py`: at each `n`, impose the 360 rows, solve, then evaluate
> `Σ_{l=0}^{n+3} Φ(n,0,l)ρ_{()}(n,0,l) + Σ_{k=0}^{n+3} Φ(n,k,0)σ_{()}(n,k,0)` cell by cell. Zero
> at every `n` tested.

So the certificate is **complete and its boundary contribution genuinely cancels**; what is missing
is not a mathematical fact but a *Lean-checkable certificate for one rational single-sum identity*
in one variable. That is the smallest open object anywhere in this campaign.

`LEAN_Z5_SCAFFOLD` §5.4 anticipates exactly this ("If it does not, say so explicitly and supply the
two boundary sums in closed form"). I am saying so explicitly, and the closed form asked for is a
*rational* single sum, not a harmonic one.

Three routes, in increasing cost:

1. **Gosper each boundary sum separately** — find `u` with
   `g(x)·u(x+1) − u(x) = ρ_{()}(n,0,x)`, `g(x) = (n+3−x)²(n+x+1)²/(x+1)⁴`, and the `k`-mirror.
   `[EXCLUDED with bounds]` **This does not work**: `work/z5star/gosper.py` finds no rational `u`
   with denominator in `{1, (x+1), (x+1)(n+x+1)(n+x+2)(n+x+3), (x+1)³(n+x+j), (x+1)⁴(n+x+j)²}` and
   numerator degree ≤ 40, for either side, at `n = 9`. Neither half telescopes on its own.
2. **Certify the two together** — it is their *sum* that vanishes, so a single certificate for the
   combination suffices, and by (1) that is what is needed. This is a one-variable Zeilberger/WZ
   problem on an explicitly-known rational summand: **the recommended next step**, and cheap.
3. **Absorb the boundary into a modified base.** Replacing `Φ` by `Φ·k` in the `()` component
   alone is not legitimate (it breaks the `k`-step), but a base carrying an explicit
   `(k+l+1)`-type factor may be.

---

## 4. JOB 3a — the minimal ansatz, MEASURED not guessed

`work/z5star/scanmin*.py`. Calibration carried in every run, as the discipline requires:
`ŵ₃`'s `('h2_pk',)` block **must** solve and its `('h1_k',)` block **must not** — both behaved as
the predecessor recorded, in every adequate ansatz.

Stripping the denominator one factor at a time, at `n = 9` and `n = 11` (identical results):

| name | denominator | `deg_k` | first solves at | numerator bidegree | `nc` |
|---|---|---|---|---|---|
| `F1` (`Z5CF_REP`'s) | the generous search family | 16 | slack 16 | (32,32) | 2178 |
| `H3` | `(k+1)³(l+1)³(k+l+1)Π(n+k+j)Π(n+l+j)` | 7 | slack 8 | (15,15) | 480 |
| `J5` | `(k+1)(l+1)(k+l+1)Π(n+k+j)Π(n+l+j)` | 5 | slack 8 | (13,13) | 364 |
| **`M0`** | **`(k+l+1)(n+k+1)(n+k+2)(n+k+3)(n+l+1)(n+l+2)(n+l+3)`** | **4** | **slack 8** | **(12,12)** | **312 / 338** |
| `J1` | `M0` without `(k+l+1)`, with `(k+1)³(l+1)³` | 6 | — | **no solution to slack 16** | |
| `J3` | only two of the three `(n+k+j)` | 6 | — | **no solution to slack 16** | |

Two facts worth recording:

* **The excess is invariant.** *Every* denominator family first solves at exactly `slack 8`, i.e.
  `deg_k(numerator) − deg_k(denominator) = 8` always. That is a property of the `Φ₃`/`L_BZ` setup,
  not of the ansatz — and it is the **same excess the `Q` row has** (`r_num` has `deg_k = 9`,
  `r_den` has `deg_k = 1`). Minimising the denominator therefore minimises the numerator, and `M0`
  is minimal: dropping `(k+l+1)` or any one `(n+k+j)` kills the solution.
* **The full certificate closes at the minimal ansatz** `[VERIFIED]`: letters `M0`/slack 8
  (`nc = 338`, curl kernel 64), `()` block `M0`/slack 12 (`nc = 578`), joint system
  1346 columns × 1857 rows (ratio 1.38); `nbadL = 0`, `nbad0 = 0`, and the **fresh-point
  verification of all 109 components at 400 unseen points is ALL ZERO** (43 600 identities).
  Against `Z5CF_REP` §4.1's 7290 columns × 9685 rows, this is a **5.4× reduction in columns**.

---

## 5. JOB 3b — the lift to ℤ[n,k,l]

`work/z5star/nsweep.py`, `reco.py`, `lcmden.py`, `emit.py`.

**Method.** `fastlin.solve` takes the lexicographically-first independent pivot set, which is the
same for generic `n` and `p`, so every coefficient of the canonical solution is a well-defined
rational function of `n`. Sweep `n`, reconstruct by Cauchy interpolation mod `p`, CRT over several
primes, rational-lift.

> **Which gauge is lifted.** The delivered certificate is in the **(B-bot)-satisfying gauge**:
> the 16 collapse-class conditions of §3.2 are imposed as exact rows inside the joint solve
> (`work/z5star/cert5.py`), so `R_w(n,0,l)` and `S_w(n,k,0)` reduce to the `()` class alone, whose
> boundary sum is zero (§3.3). See §3.4 for how those rows are assembled.

`[VERIFIED]` The certificate closes and passes fresh-point verification at **`n = 1, 2, 3, 4, 5`**
as well as at `n = 9, 11, 13` (`work/z5star/smalln.py`; 200 unseen points × 109 components each,
`nbadL = nbad0 = 0`, no component failures) — small `n` is not a degenerate case here, unlike the
`n = 5` accident `Z5CF_REP` §3 had to discard. At `n = 0` the sampler cannot produce points at all
(the factor `n+0` in its admissibility filter), which is consistent with the next paragraph.

⚠ **`dn(n)` has a factor `n`.** The cofactors therefore have a simple pole at `n = 0`, so the
certificate as delivered proves `BZRec` for **`n ≥ 1`**. This costs nothing in Lean: the `n = 0`
instance is *already kernel-checked* (`LEAN_Z5_SCAFFOLD` §3.4 for `PhatSum`, and `BZStar.lean`'s
`PStarSum_zero/one/two` plus `#eval PStarSum 3` pin `w★` at four points), so the proof is
`intro n; cases n` with the base case by `norm_num`/`decide`. **It must not be overlooked**: the
`ρ_j` evaluate to `1/0 = 0` at `n = 0` and the componentwise identity is false there.

The multi-prime CRT lift (6 primes, `n = 4…153`) and the sparse-ℤ emission are in
`work/z5star/nsweep_6p.pkl` → `lift_Q.pkl` → `work/z5star/CERT_wstar_sparse.json`;
status in §8.

---

## 6. JOB 4 — the size table, and the delivery format

### 6.1 Per-block sizes `[MEASURED]`

Normalisation delivered (see §6.2):
`ρ_j = Nr_j(n,k,l) / ( dn(n)·D(n,k,l) )`, `σ_j = Ns_j(n,k,l) / ( dn(n)·D(n,k,l) )`.

| block | part | `deg_n` | `deg_k` | `deg_l` | live `(k,l)`-monomials | ≤ monomials of `ℤ[n,k,l]` |
|---|---|---|---|---|---|---|
| `()` | `ρ` | 50 | 12 | 10 | 142 | 5 367 |
| `()` | `σ` | 50 | 10 | 12 | 79 | 3 250 |
| `H⁽¹⁾_k` | `ρ` / `σ` | 49 | 12/10 | 10/12 | 131 / 68 | 4 905 / 2 821 |
| `H⁽¹⁾_l` | `ρ` / `σ` | 49 | 12/10 | 10/12 | 131 / 68 | 4 905 / 2 821 |
| `H⁽¹⁾_{n−k}` | `ρ` / `σ` | 49 | 12/10 | 10/12 | 131 / 68 | 4 905 / 2 821 |
| `H⁽¹⁾_n` | `ρ` / `σ` | 49 | 12/10 | 10/12 | 131 / 68 | 4 905 / 2 821 |
| `H⁽¹⁾_{n+k}` | `ρ` / `σ` | 49 | 12/10 | 10/12 | 131 / 68 | 4 905 / 2 821 |
| `H⁽¹⁾_{n+k+l}` | `ρ` / `σ` | 49 | 12/10 | 10/12 | 131 / 68 | 4 905 / 2 821 |
| `H⁽¹⁾_{n+l}` | `ρ` / `σ` | 49 | 12/3 | 10/12 | 131 / 39 | 4 905 / 1 700 |
| `H⁽²⁾_k` | `ρ` / `σ` | 50 | 12/10 | 10/12 | 120 / 57 | 4 584 / 2 438 |
| `H⁽²⁾_l` | `ρ` / `σ` | 50 | 12/10 | 10/12 | 120 / 57 | 4 585 / 2 438 |
| `H⁽²⁾_{n−l}` | `ρ` / `σ` | 50 | 12/3 | 10/12 | 120 / 39 | 4 585 / 1 739 |
| `H⁽²⁾_n` | `ρ` / `σ` | 50 | 12/3 | 10/12 | 120 / 39 | 4 585 / 1 739 |
| `H⁽²⁾_{n+k}` | `ρ` / `σ` | 50 | 12/3 | 10/12 | 120 / 39 | 4 585 / 1 739 |
| **TOTAL (26 polynomials)** | | **≤ 50** | **≤ 12** | **≤ 12** | **2 416** | **≤ 94 595** |

The remaining 29 of the 42 blocks are **maximal**: their cofactor is `w_j·r_Q` (resp. `w_j·s_Q`)
with `w_j ∈ {±1, ±½, +³⁄₂}`, i.e. the **already-certified `Q`-row identity instantiated 29 times**,
not 29 new objects. In Lean each is `linear_combination (w_j) * KeyPoly` against the `BZQRow.lean`
statement — this is the single largest saving the `w★` route gets over the naive count of 42.

Coefficient bit-lengths require the multi-prime lift; see §8.

### 6.2 The interface, restated for `BZStar.lean`

* **Operator:** `L_BZ` itself, `cc0…cc3` of `BZClosedForm.lean`. Nothing new.
* **Base:** `Φ₃` of `LEAN_Z5_SCAFFOLD` §5.2. The normalisation uses the **`T_shift_n3`
  direction** — `T(n+i,k,l) = Φ·P_i` with the `P_i` exactly as §5.2 lists them, and the four
  cofactors in the cascaded parenthesisation `BZQRow.lean` already uses (`PP0 = Y3(Y2 Y1)` etc.).
* **Letters:** the mixed base — `H^(r)_{n−k}` and `H^(r)_{n−l}` are normalised at **`n+3`**, i.e.
  the Lean atoms are `Harm r (n+3-k)` and `Harm r (n+3-l)`. Every other letter is bare. This is a
  change of ℚ(n,k,l)-basis only, and it is what makes §2.4 work.
* **Shift table:** `LEAN_Z5_SCAFFOLD` §5.3 unchanged, and `BZStar.lean` §1's twelve bare-letter
  lemmas (`Harm_sub_succ_n`, `Harm_sub_succ_arg`, `Harm_nk_succ_n/k`, `Harm_nkl_succ_n/k/l`, …)
  are exactly the ones needed. Keep the truncated-ℕ / `1/0 = 0` convention.
* **Denominators, both strictly positive for `n ≥ 1, k,l ≥ 0`:**
  `D(n,k,l) = (k+l+1)(n+k+1)(n+k+2)(n+k+3)(n+l+1)(n+l+2)(n+l+3)`,
  `dn(n) = n(n+1)⁴(n+2)⁴(n+3)²(n+4)²(n+5)²(n+6)²(n+7)²`.
  `positivity` discharges both; `n > 0` comes from the `cases n` of §5.
* **Format:** fully expanded over ℤ, sparse, keyed on exponent triples —
  `[[e_n, e_k, e_l], c]` per block and part, as `work/z5star/CERT_wstar_sparse.json`.
  `LEAN_Z5_SCAFFOLD` §5.6.1 ("pre-factored, never flattened") is **superseded** for this row, per
  `LEAN_QROW` §9.3.

### 6.3 What this predicts for the reflective checker

The checker's cost is roughly linear in total monomials.

**The left-hand side, now measured** `[MEASURED]` (`work/z5star/lhs.py`, cleared per component
and interpolated mod `p`):

| component | clearing exponents | monomials | `(deg_n, deg_k, deg_l)` |
|---|---|---|---|
| `()` | `n³ (n+k+j)² (n+k+l+j) (n+l+j)` | **5 337** | (39,15,12) |
| `H⁽¹⁾_k, H⁽¹⁾_{n−k}, H⁽¹⁾_n, H⁽¹⁾_{n+k+l}, H⁽¹⁾_{n+l}` (×5) | `n² (n+k+j)²` | 2 079 each | (31,12,6) |
| **`H⁽¹⁾_l`, `H⁽¹⁾_{n+k}`** | — | **0 — identically zero** | — |
| `H⁽²⁾_k` | `n (n+k+j)(n+k+l+j)(n+l+j)` | 3 439 | (32,12,12) |
| `H⁽²⁾_l` | `n (n+k+j)(n+k+l+j)` | 2 425 | (29,12,9) |
| `H⁽²⁾_{n−l}, H⁽²⁾_n, H⁽²⁾_{n+k}` (×3) | `n (n+k+l+j)(n+l+j)` | 2 404 each | (29,9,12) |
| the **29 maximal** components | — | **784 each** | (21,6,6) |
| **TOTAL, 42 components** | | **51 544** | |

Two things worth flagging. **The 29 maximal components are 784 monomials at degrees (21,6,6) —
exactly the `Q`-row left-hand side `Σ_i c_i P_i`** (`LEAN_QROW` §2: 784, (21,6,6), 58 bits). They
*are* `w_j ×` that one object, so they carry **no new data**. And **two components vanish
identically** (`H⁽¹⁾_l` and `H⁽¹⁾_{n+k}`: every quotient monomial above them is an `H^(r)_k` or
`H^(r)_l`, whose `n`-increment is zero), so those two block equations are homogeneous.

Genuinely new LHS data: **51 544 − 29×784 = 28 808 monomials**.

The **cleared per-block identities** are larger: each is the cofactor times the
clearing multipliers (`D(n,k+1,l)`, `D(n,k,l+1)`, `gk`, `gl`, `dn`), pushing degrees to roughly
`(60, 25, 25)`. A degree-bound estimate — **not a measured expansion**, and it should be measured
before anyone budgets on it — gives ~4·10⁴ monomials per new block identity, so

```
   13 new block identities × ~4·10^4  ≈  5·10^5 monomials of normal form,
   + 1 Q-row identity (3798, already transcribed in BZQRow.lean) reused 29 times.
```

against `LEAN_QROW` §9's estimate of `~4·10^5` for the whole thing — i.e. **the minimal-ansatz
measurement of §4 has brought the certificate in at roughly the size that report predicted, and
the 29 maximal blocks turn out to be free rather than 29× the Q row.** That is the good news. The
bad news is that this is still ~130× the single `Q`-row identity that killed `ring`, so §6.3
confirms rather than softens `LEAN_QROW`'s verdict: **the reflective checker is not optional.**

### 6.4 Coefficient heights `[MEASURED]` — small, after all

| quantity | value |
|---|---|
| primes used | **24** (`4194301 … 4193957`), modulus ≈ 2⁵²⁸ |
| sweep | `n = 4…153`, **2700 jobs, 0 failures**, 1892 s on 11 cores |
| held-out check of every interpolant | **0 mismatches in 889 728 identities** (8 unseen `n` × 4634 coefficients × 24 primes) |
| degree of the interpolant, agreement across primes | **0 mismatches** |
| **coefficients that failed to lift to ℚ** | **0 of 96 813** |
| max bit-length, ℚ **numerator** | **122** |
| max bit-length, ℚ **denominator** | **14** |
| max bit-length after per-`(k,l)`-column integer clearing | **123**, with column scales ≤ **14** bits |
| total live monomials of `ℤ[n,k,l]` | **93 073** |
| emitted file | `work/z5star/CERT_wstar_sparse.json`, **7.7 MB** |

**This is the good news of the whole report.** `LEAN_QROW` §9 predicted the `w★` certificate would
need "~4·10⁵ monomials of normal form" with coefficients well above the `Q` row's 76 bits. The
measured cofactor data is **93 073 monomials with 122-bit coefficients** — a quarter of the
predicted monomial count and only 1.6× the `Q` row's coefficient height, on a certificate that is
42 blocks rather than one.

⚠ **A methodological warning worth recording.** A 6-prime run (modulus ≈ 2¹³², rational-lift bound
≈ 2⁶⁵) left **30 588** coefficients unliftable *and* returned spurious "successful" lifts for
others, whose per-column lcms ran to **2085 bits** — five hundred times the truth. Every conclusion
drawn from an incomplete rational lift is worthless, and an incomplete lift does not announce
itself. `emit2.py` now writes `unliftable_coefficients` and a `WARNING` field into the JSON for
exactly this reason. **Check that field before transcribing anything.**

**Delivery.** Both forms are in the file, keyed on the same exponent triples: `columns` (integer
lists, one 14-bit scale per `(e_k,e_l)`) and `terms_Q` (one ℚ per monomial). Either is small; a
single integer scale per *block* is not (the lcm of ~5000 denominators has tens of thousands of
digits) and is deliberately not delivered.

**Remaining size lever.** The solution is still the *pivot-canonical* one, not a
minimal one, and there are 64 gauge dimensions per letter block plus the `()` block's own kernel.
`LEAN_QROW` §7.3 proposes minimising `deg(A)+deg(B)` over the gauge; `deg_n = 50` against a `dn` of
degree 19 suggests visible slack. That is now an optimisation, not a necessity.

---

## 7. JOB 5 — the order-0 bridge is IMPOSSIBLE `[PROVED]`

The coordinator asked for a single order-zero divergence certificate
`T(n,k,l)·(w★ − ŵ₃) = Δ_k R₀ + Δ_l S₀` with vanishing boundaries. **It cannot exist.**

**Proof.** Write `d = w★ − ŵ₃ = Σ_j d_j M_j` and `R₀ = T·Σ_j ρ_j M_j`, `S₀ = T·Σ_j σ_j M_j`.
Dividing by `T` and expanding `M_j(n,k+1,l) = Σ_i (S_k)_{ij} M_i(n,k,l)`, the `M_i`-component is

```
   d_i = Σ_j g_k (S_k)_{ij} ρ_j(k+1,l) − ρ_i + Σ_j g_l (S_l)_{ij} σ_j(k,l+1) − σ_i .
```

For a **maximal** monomial `M_i` (nothing in the basis is a strict multiple of it),
`(S_k)_{ij} = (S_l)_{ij} = δ_{ij}`, so the component is a plain scalar WZ equation. Multiply it by
`T(n,k,l)` and sum over `0 ≤ k,l ≤ n`: the right-hand side telescopes to the boundary terms, which
vanish by hypothesis, so `d_i·Σ_{k,l}T(n,k,l) = d_i·Q_n = 0` for every `n`. Since `Q_n ≥ 1`,
`d_i = 0`. But `d` has **29 nonzero maximal components**. ∎

**Corollary (a lower bound on the bridge order).** The same computation applied to a general
bridge operator `M = Σ_t m_t(n)N^t` — assuming, as any *usable* certificate must, that its
boundary terms vanish — shows that for a maximal `M_i` the `n`-shift matrices are unipotent with
`(S_n^t)_{ii} = 1` and no other contribution, so the `M_i`-component is
`Σ_t m_t(n)·T(n+t,k,l)·d_i`; summing over the rectangle forces
`d_i·Σ_t m_t(n)·Q_{n+t} = 0`, i.e. **`M` must annihilate `Q`**. `LEAN_QROW` §2 established by
nullspace search over `Q_0…Q_59` that `Q` has **no** annihilator of order 1 or 2 with polynomial
coefficients of degree ≤ 13, and exactly nullity 1 at (order 3, degree 9), namely `L_BZ`. At
order 3 the bridge would therefore require `d ∈ W_tel`; but `W_tel` is linear, `w★ ∈ W_tel` and
`ŵ₃ ∉ W_tel` (`Z5CF_REP` §3.2), so `d ∉ W_tel`. Hence

> **the minimal bridge order is ≥ 4**, and a bridge is a left-multiple problem
> `A·L_BZ` of order ≥ 4 — the same shape as `Z5CF_TELESCOPER`'s search, run with the fixed weight
> `d = w★ − ŵ₃`. That is a well-posed, bounded scan with the machinery already in `work/z5rep/`
> (`frw.py` with `avec` on the `m = 4` slice), and it is **not done here**.

**This does not block the closed form.** `BZStar.lean`'s `PStarSum_eq_Phat_of_rec` reaches `P̂`
directly through `eq_of_BZRec` and its three kernel-checked initial values; it never goes through
`PhatSum`. The bridge is needed only to also announce the *compact* `ŵ₃` form, exactly as
`LEAN_QROW` §10 says.

---

## 8. Status of the deliverables, and what remains undone

| item | status |
|---|---|
| the 12-dim affine family, exact ℚ | **done** — `work/z5star/familyQ.pkl` |
| family-member decision | **done** — keep `w★`; §2 |
| antisymmetric-difference member | **`[EXCLUDED]`, exact ℚ + structural proof** — §2.1 |
| (P-int) and the removal of "Lemma N" | **done** — §2.4 |
| minimal ansatz, denominator measured | **done** — `M0`, bidegree (12,12)/(16,16); §4 |
| full certificate at the minimal ansatz, fresh-point verified | **done** — 43 600 identities, 0 failures |
| (B-top) | **`[PROVED]` free** |
| (B-bot), maximal + 12 letter blocks + 16 of 17 classes, all 360 rows at once | **done, `[VERIFIED]`** |
| the residual boundary sum is zero | **`[VERIFIED, n = 1…13]`** |
| **a Lean-checkable certificate for that single rational identity** | ⚠ **OPEN** — one-variable WZ, §3.3 route 2 |
| `n`-sweep + rational reconstruction, 1 prime (116 pts) and 6 primes (150 pts) | **done**, 0 failures |
| held-out check of every interpolant | **done** — 0 mismatches in 222 432 identities |
| common `n`-denominator | **done**, fully factored |
| size table (degrees, monomial counts) | **done** — §6.1 |
| 24-prime sweep, `n = 4…153` | **done** — 2700 jobs, **0 failures**, 1892 s on 11 cores |
| **CRT lift → ℚ, sparse JSON emitted** | **done** — `work/z5star/CERT_wstar_sparse.{json,txt}`, 7.7 MB, **0 unliftable of 96 813**; carries both the ℤ-per-`(k,l)`-column form and the ℚ-per-monomial form, plus `unliftable_coefficients` and a `WARNING` field |
| **coefficient bit-lengths** | **done** — ≤ 122-bit ℚ numerators, ≤ 14-bit denominators; §6.4 |
| **exact-ℚ residual check OF THE DELIVERED FILE** | **done** — `work/z5star/check6.py`, no mod-`p` machinery, **6636 identities at `n,k,l ≤ 6`, 0 mismatches** |
| gauge / degree minimisation of the cofactors | **not attempted** — the single biggest remaining size lever |
| the ≥ order-4 bridge to `ŵ₃` | **not attempted**; §7 gives the lower bound and the shape |
| weight 5 | untouched |

Everything claimed as `[MEASURED]` or `[VERIFIED]` above was checked at fresh points never used in
any fit, and the ansatz-adequacy calibration (`ŵ₃`'s `h2_pk` must close, its `h1_k` must not, plus
the `w = 1` control) passed in every run reported.

### 8.1a The independent exact-ℚ check of the delivered file

`work/z5star/check6.py` reads `CERT_wstar_sparse.json` and rebuilds **everything else from its
definition** in exact ℚ — the shift matrices, the base cofactors `P_i`, `g_k`, `g_l`, the operator
coefficients `c_u(n)` and the `Q`-row cofactors — sharing no code with the mod-`p` machinery that
produced the certificate. For every monomial `M_i` of the 42-element closure it checks

```
   Σ_j [ g_k (S_k)_{ij} ρ_j(n,k+1,l) + g_l (S_l)_{ij} σ_j(n,k,l+1) ] − ρ_i − σ_i  =  (E_w/Φ)_i .
```

`[VERIFIED exact ℚ]` **`n,k,l ≤ 6`: 158 cells × 42 components = 6636 identities, 0 mismatches**
(`work/z5star/check6_n6.log`; the `n ≤ 3` run gave 1218 identities, 0 mismatches).

The points `k, l ∈ {n+1, n+2, n+3}` are **skipped by this checker**, not because the identity fails
there but because the individual shift coefficients have *removable* poles there and a naive
rational evaluation is `0/0`. Those are exactly the points (P-int) is about, and they are covered
instead by the limit test of `work/z5star/pint.py` (§2.4), which is calibrated against a
pole-carrying control.

### 8.2 The prime budget — read this before trusting the emitted integers

Rational-function reconstruction **in `n`** happens over `F_p` and depends only on having enough
sample points; it is reliable, and the held-out check confirms it (0 mismatches in 222 432
identities over 6 primes). Reconstruction of the **ℚ coefficients** needs enough primes to exceed
their height, and here the heights are large (§6.4):

| primes | modulus | rational-lift bound | unliftable coefficients |
|---|---|---|---|
| 6 | ≈ 2¹³² | ≈ 2⁶⁵ | **30 588** — far too few, *and* it returned spurious lifts for others |
| **24** | ≈ 2⁵²⁸ | ≈ 2²⁶⁴ | **0 of 96 813** — complete |

**If `emit2.py` prints a nonzero "unliftable" count, the emitted JSON is incomplete and must not
be transcribed.** The fix is purely mechanical — add primes to `nsweep.PRIMES` and re-run — and
each additional prime costs ≈ 140 s of sweep on 11 cores. This is stated explicitly because a
silently-truncated certificate is the worst possible failure mode here.

### 8.1 Reproduction

```bash
cd /home/ubuntu/fable-episode-2/zeta-math-2/work/z5star
python3 fam.py 9,11,13 8 10       # the 13-dim lam-space -> famlam_p4194301.pkl
python3 opt.py                    # rationalise -> familyQ.pkl
python3 job1.py                   # sigma-stability, the antisymmetry exclusion, min-J
python3 job1b.py 6                # the Barnes candidate w_B3: NOT in the span (see below)
python3 cands.py                  # the four candidate members + their minimal ansatz
python3 scanmin2.py 9,11          # the denominator strip-down
python3 scanmin3.py 9             # ... continued: M0 is minimal
python3 job2c.py 9 8 M0 12        # the full certificate with (B-bot) rows
python3 bbotdiag3.py 9 M0 12 8    # which (B-bot) class fails: only the () one
python3 nsweep.py 4:120 1 10      # the n-sweep
python3 reco.py nsweep_1p.pkl 10  # degrees of every cofactor coefficient
python3 lcmden.py                 # the common n-denominator, factored
python3 sizes.py                  # the size table of 6.1
python3 nsweep.py 4:154 0:6 10        # the 6-prime sweep   (nsweep_6p.pkl)
python3 nsweep.py 4:154 6:24 11       # 18 more primes      (nsweep_6_24.pkl)
python3 emit3.py nsweep_6p.pkl nsweep_6_24.pkl   # interpolate + CRT + rational lift
python3 emit2.py                      # -> CERT_wstar_sparse.{json,txt} + the size table
python3 check6.py 4                   # independent exact-Q residual check of the FILE
python3 gosper.py 9                   # the 16 (B-bot) classes; Gosper of the () boundary
python3 bsum.py                       # the residual boundary sum is zero
python3 smalln.py                     # the certificate at n = 1..5
python3 pint.py                       # (P-int), with a pole-carrying control
```

`work/z5star/finish.sh` chains the last stages. Wall clock on 11 cores: the 6-prime sweep 836 s,
the 18-prime sweep ≈ 2500 s, `emit3` ≈ 300 s, `emit2` ≈ 60 s.

### 8.2 The Barnes candidate `w_B3` — tested and negative, independently

The coordinator asked (then retracted) that the contour-canonical symmetric weight `w_B3` of
`work/Z5CF_BARNES.md` be tested. It was tested here **before** the retraction arrived, with an
independent implementation (`work/z5star/job1b.py`, which reads but never writes `work/z5barnes/`),
and the result agrees:

> `[EXCLUDED, exact ℚ]` Fitting `w_B3` over the **full 109-monomial** degree-≤2 bare weight-3 span
> on all 140 cells with `n ≤ 6` is **INCONSISTENT**, with **0** free parameters. `w_B3` is not in
> the span at all, so it is not a candidate member of the family.

Recorded because it is an independent confirmation of the Codex session's own retraction, obtained
against a different basis (109 monomials including the divisibility closure, versus their 90 tops)
and a different cell set.

---

## 9. Do not re-run

* per-block `force_k = force_l = 1` for (B-bot) — it is strictly stronger than (B-bot) and gives a
  reproducible false negative on the `()` block (§3.1);
* the `()` block's (B-bot) in the denominators `M0, M2, M4, M5, M6, M7, G0, G1, F1` at slacks
  8–20 with letter slack 8 (§3.3) — infeasible, and the reason is Gosper-summability, not size;
* any ansatz for this alphabet omitting `(k+l+1)` or any one of `(n+k+1),(n+k+2),(n+k+3)` — no
  solution to slack 16 (§4);
* the search for a family member with `w − ŵ₃` antisymmetric (§2.1), or with `N_hard < 13` (§2.3);
* an order-0, order-1 or order-2 bridge between `w★` and `ŵ₃` (§7).

---

## 10. For the Lean agent, in one place

1. **The weight does not change.** `BZStar.lean`'s `wstar` is right. Keep it, keep
   `PStarSum_zero/one/two`, keep the quarantine shape.
2. **Rewrite the two subtracted letters to the `n+3` normalisation first.** The certificate's
   atoms are `Harm r (n+3−k)`, `Harm r (n+3−l)`. Three `Harm_sub_succ_n` rewrites each. Without
   this the interior poles at `k = n+1,n+2,n+3` do **not** cancel and the componentwise identity is
   false under `1/0 = 0` (§2.4).
3. **`cases n` at the top.** The cofactors carry `1/n`; the certificate proves `BZRec` for `n ≥ 1`
   and `n = 0` is the kernel-checked instance you already have (§5).
4. **29 of the 42 components are `linear_combination (w_j) * KeyPoly`** against `BZQRow.lean` —
   no new data at all. Only 13 blocks carry new cofactors (§6.1).
5. **`DivCert` is unsatisfiable.** Delete the order-0 bridge plan; the minimum is a left multiple
   of `L_BZ` of order ≥ 4 (§7). Nothing on the critical path depends on it.
6. **The last (B-bot) piece is one rational single-sum identity**, verified zero for `n = 1…13`
   (§3.3). It is the right size for a hand-written one-variable WZ certificate and it is the only
   boundary obligation left.
7. **The format is sparse ℤ**, `[[e_n, e_k, e_l], c]`, in `work/z5star/CERT_wstar_sparse.json`
   with a plain-text twin `CERT_wstar_sparse.txt`; `work/z5star/check6.py` re-verifies the
   delivered file from scratch in exact ℚ, using none of the mod-`p` machinery.
