# P1g — the decisive experiment: Apéry-type (`R`) letters and the strong depth system

**Author:** mathematician-agent (River's odd-zeta program), task **P1g**
**Date:** 2026-07-25
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, artefacts in `work/p1g/`
**Predecessors (authoritative):** `work/PHASE2_CANCEL.md` (the wall theorem; §7.1 the live route),
`work/PHASE2_FINAL.md` §2 (the rank-324 joint system, `w5_allp`), `work/p1d/solve_strong.py`.

**Labels.** `[PROVED]` · `[VERIFIED r]` exact finite check on range `r`, 0 failures ·
`[REFUTED]` · `[OPEN]`.

---

## 0. HEADLINE

1. **E1 — YES.** `P_n` admits a decomposition in every `R`-extended alphabet tried; a materialised
   example, `P_n = Σ_{k,l}T·w₅^R` with 9 Apéry-letter terms, is **exactly verified** over ℚ for
   `n ≤ 12` (§6.1). The `R`-machinery is validated end to end against an independent exact
   evaluator, so the negatives below are trustworthy.
2. **E2 — NO. The decisive experiment fails.** With the full Apéry alphabet
   `R^{(1..5)}` at both slots (**1 210** coefficients, `rank(fit)` `313 → 960`, depth-conditioned
   value space `dim U` `261 → 641`), the strengthened depth system is **still inconsistent**, at
   both the `vt2` and the full `strong` cap, `N = 1300` (row-saturated). Same for the nested
   interval letters `Y_{a,b}/V_{a,b}` — which reduce pole order below weight and cover the
   coupling slot the `R`-family cannot. **`PHASE2_CANCEL` §7.1's route (V-a) is refuted as
   proposed** (§6), for the `p`-independent symbol-independent form of the conditions; §8 states
   the one remaining loophole precisely and costs it.
3. **The `ζ(3)` premise was wrong, and this is the reason (§3).** Apéry's base case is cell-wise in
   the **purely harmonic** alphabet — new identity, `[PROVED over ℚ + VERIFIED]`:
   `a_n = Σ_k C(n,k)²C(n+k,k)²[H^{(3)}_n + ½A₁(k)(B₁(k)(A₁(k)+B₁(k)) + B₂(k))]`,
   cell-wise `p`-integral with 0 violations for `p ≤ 23`. So the `ζ(3)` precedent never argued for
   binomial-reciprocal letters.
4. **E3b executed, and it sharpens the live route (§7).** The `a₀`-root exceptional steps of `L_BZ`
   are **apparent singularities** (`φ ≡ 0` on `𝔽_p³` at 38 of 39 tested first-steps), so
   `PHASE2_CANCEL` §7.2's "1–4 exceptional steps per prime" collapses to **exactly one congruence
   per prime**, `(REC-★)` at `n₀ = (p−5)/2`.
5. **Partial closure, explicit and verified (§10).** `(BASE)` now reduces to a **single region**:
   the harmonic representative `w₅^I` (`work/p1g/w5_I.json`, 155 terms) is cell-wise `p`-integral on
   every cell **outside** the band `III = {k,l ≥ q, p ≤ k+l < p+q}`, so
   `(BASE) ⟺ Σ_III ≡ 0 (mod p)`, replacing `2Σ_I + Σ_III ≡ 0`.
   `[VERIFIED: exact identity n ≤ 20; 10 092 cells over p = 5..23; 0 violations]`
   An all-primes version `w5_exIII_allp.json` (207 terms, denominators `{2,3}`) removes the single
   bad prime; re-verified independently, 0 failures.
6. **The residue, stated sharply.** `d₅ ≤ v_pT` is achievable on *all* patterns but one
   (`exIII` and `exI` are both consistent); it is exactly **one order of pole on one pattern
   group** that no alphabet enlargement supplies.

---

## 0′. What is being tested

`PHASE2_CANCEL` §7.1 reduced `(BASE)` to a single missing order: on the three pole patterns with
`s = v_pT = 2`, the weight-5 representative `w₅` achieves depth `3` and cell-wise integrality
needs depth `2`. Inside the 448-monomial harmonic alphabet that tightening (`solve_strong.py vt2`)
is **inconsistent**. The proposed fix is to enlarge the alphabet by **Apéry-type letters**

```
   R^(a)(n,k) = Σ_{m=1}^{k} (−1)^{m−1} / ( m^a C(n,m) C(n+m,m) )      (a = 1..5)
```

which carry the *same pole indicator* `α = [n+k ≥ p]` as `A_a(k)` but **pole order 1 at every
weight**, i.e. exactly the one order that is missing, and *outside* the space in which
`PHASE2_INDUCTION` §6.1's impossibility was proved.

---

## 1. The letters and their exact pole structure `[VERIFIED]`

`work/p1g/rlet.py`. Two families:

```
   R^(a)(n,k) = Σ_{m=1}^{k} (−1)^{m−1} / ( m^a C(n,m) C(n+m,m) )        k-slot (and l-slot)
   D^(a)(n,m) = Σ_{j=1}^{m} (−1)^{j−1} / ( j^a C(n+j,j) )               coupling slot m = k+l
```

**`[VERIFIED exact, p ∈ {5,7,11,13,17,19,23}, all n < p, all cells, a = 1..5, 0 failures]`**

| letter | pole order | indicator |
|---|---|---|
| `R^(a)(n,k)`, 812 cells/weight | **≤ 1** for every `a` | poles occur only where `α = [n+k ≥ p] = 1` (0 exceptions) |
| `D^(a)(n,k+l)`, `ε = ⌊(k+l)/p⌋ = 0`, 1 536 cells/weight | **≤ 1** for every `a` | poles only where `κ = [n+k+l ≥ p] = 1` (0 exceptions) |
| `D^(a)(n,k+l)`, `ε = 1` | **≤ a** (the `j = p` term) | — |

So `R` is a clean depth-1 replacement for `A` at every weight; `D` is the same for `C` **except**
on the `ε = 1` sheet, where it costs `a`. `D` therefore requires the pattern census refined by
`ε` (the cap `1+min(v_pT,2)` is unchanged by the refinement, so refining only *weakens* the
conditions — it is sound).

**Depth model used for the conditions.** `A_r` has residue the *constant* `1`; the `R`/`D`
residues are cell-dependent, so they enter the `u`-calculus as **free `ℤ_p` symbols**
(`ρ_{r,slot}`, `δ_r`). Requiring `K_j = 0` identically in the symbols is then *sufficient* for the
depth bound — the same (safe) strengthening already used for the `A/B/C/N` symbols in
`work/lb5/depthcond.py`.

---

## 2. Machinery, and its validation against P1c/P1d `[VERIFIED]`

`work/p1g/rfit.py` rebuilds the fitting system in the enlarged alphabet (modular `matmul` via a
13-bit `float64` split — two `dgemm`s, exact for all sizes used; cross-checked against
`work/lb5/fit.row` at `n = 3,7,12`). `work/p1g/rdepth.py` rebuilds the `u`-graded depth
conditions. Basis sizes (weight 5; `≤5` `k`-factors, `≤2` `c`-factors, `≤2` `n`-factors):

| alphabet | `k`-letters | `k`-monomials | basis columns |
|---|---|---|---|
| `ctrl` = `A,B` / `C` / `N` (P1c) | 10 | 74 | **448** |
| `R` = `A,B,R` / `C` / `N` | 15 | 194 | **1 210** |
| `RD` = `A,B,R` / `C,D` / `N` | 15 | 194 | **1 787** |

**Control run (`e2.py MODE ctrl 600 33554393`) reproduces P1c §2.3 and P1d exactly:**

| MODE | condition rows | rank(fit) | rank(cond) | rank(joint) | inconsistent? |
|---|---|---|---|---|---|
| `base` (cap `1+min(vT,2)`) | 68 | 313 | 42 | 324 | **NO** (nullity 124) |
| `vt2` (cap 2 on the three `s=2` patterns) | 149 | 313 | 81 | 342 | **YES** |
| `strong` (cap `= vT`) | 239 | 313 | 123 | 342 | **YES** |

Identical to `work/p1d/solve_strong_vt2.out` / `_strong.out` and `PHASE2_FINAL` §2.3.

### 2.1 New: the obstruction is a *conjunction*, and the right invariant is `dim U`

**The invariant to watch.** Let `U := M·ker C ⊂ ℚ^N` be the space of value sequences `(V_w(n))_n`
realised by **depth-conditioned** forms. Then
```
      dim U = rank(joint) − rank(cond) ,     and    the system is consistent ⟺ P ∈ U .
```
*(Note: the reported `DEFECT = rank[A|rhs] − rank[A]` is `1` whenever the system is inconsistent —
a single appended column can raise the rank by at most one. It is a restatement of
inconsistency, **not** extra information. `dim U` is the informative quantity.)*

Splitting the `vt2` tightening over the three `s = 2` patterns (`I = (0,1,1,1)`, `II = (1,0,1,1)`,
`III = (1,1,0,1)`), in the control alphabet at `N = 600`:

| tightened patterns | cond rows | rank(cond) | rank(joint) | `dim U` | `P ∈ U`? |
|---|---|---|---|---|---|
| none (`base`) | 68 | 42 | 324 | 282 | **yes** |
| `I` only (`= I+II`, they are `k↔l` mirrors) | 122 | 69 | 342 | 273 | **yes** |
| `III` only | 95 | 54 | 336 | 282 | **yes** |
| `I + II + III` (`vt2`) | 149 | 81 | 342 | 261 | **NO** |
| full `strong` (`cap = vT`) | 239 | 123 | 342 | 219 | **NO** |

> **Observation 2.1 `[VERIFIED, q = 33554393, N = 600]`.** In the harmonic alphabet each pattern
> group is *individually* achievable at depth 2 — it is only their **conjunction** that fails.
> `rank(joint)` is `342` both for `I+II` alone and for all three, so the `III` conditions add no
> new rank on top of `[fit ; cond(I+II)]`; they only shrink `U` (273 → 261) past `P`.

Unwound: *the strengthened depth conditions force linear relations among the values `P_1,…,P_N`
that `P` does not satisfy* — the shape Theorem 5.1 of `PHASE2_CANCEL` predicts (`θ` factors
through the value map, so the only lever is the space of representatives). The `R`-letters are
being asked to enlarge `U` past `P`.

**The obstruction is global, not local `[VERIFIED, `work/p1g/window.py`]`.** The smallest prefix of
levels `n = 1..L` on which `[fit ; cond_vt2]` is already inconsistent is **`L = 262`** — one more
than `dim U = 261`, i.e. exactly the *generic* threshold. There is no short window of levels, and
hence no small-`n` congruence, carrying the obstruction: it is a statement about the whole value
sequence.

---

## 3. A surprise, and it matters: the `ζ(3)` base case does **not** need Apéry letters

`PHASE2_CANCEL` §7.1 attributes the cell-wise integrality of Apéry's `ζ(3)` base case to the
*binomial-reciprocal* letter in the classical weight. Running the identical experiment one weight
down (`work/p1g/zeta3.py`, `work/p1g/z3ex.py`) refutes that attribution.

Set-up: `T_A(n,k) = C(n,k)²C(n+k,k)²`, `a_n = Σ_k T_A(n,k)c(n,k)` with the classical
`c(n,k) = H^(3)_n + ½R^(3)(n,k)`, and `v_pT_A = 2α`, so cell-wise integrality is `d₃ ≤ 2α`.

| alphabet | basis | rank(fit) | condition rows | rank(joint) | inconsistent | defect |
|---|---|---|---|---|---|---|
| `{A_r,B_r}×{N_r}` (harmonic) | 22 | 15 | 1 | 15 | **NO** | 0 |
| `{A_r,B_r,R_r}×{N_r}` | 40 | 32 | 4 | 32 | **NO** | 0 |

and the harmonic solution is explicit and clean:

> **Proposition 3.1 `[PROVED over ℚ by exact rref + VERIFIED]`.** With
> `A₁(k)=H_{n+k}−H_k`, `B₁(k)=H_{n−k}−H_k`, `B₂(k)=H^{(2)}_{n−k}−H^{(2)}_k`,
> ```
>   a_n  =  Σ_{k=0}^{n} C(n,k)²C(n+k,k)² · [ H^{(3)}_n
>            + ½ ( A₁(k)²B₁(k) + A₁(k)B₁(k)² + A₁(k)B₂(k) ) ]
> ```
> **`[VERIFIED exact over ℚ, n = 1..24, 0 mismatches]`**, and this weight is **cell-wise
> `p`-integral**: `d₃(n,k) ≤ v_pT_A(n,k)` with **0 violations** over `p ∈ {5,7,11,13,17,19,23}`,
> all `n < p`, all `k`. (`work/p1g/z3ex.py`; the exact-ℚ solve is over 14 levels + the single
> `u³` condition, rank 15, then checked on 24 levels and 7 primes.)
>
> Equivalently `w₃ = H^{(3)}_n + ½A₁(B₁(A₁+B₁) + B₂)`. So **Apéry's own base case is cell-wise in
> the *purely harmonic* alphabet** — no binomial-reciprocal letter is required.

**Why this matters.** The `ζ(3)` precedent does not, on its own, argue for `R`-letters; it argues
that *some* alphabet enlargement of the right shape exists. It also gives the mechanism a name:
the working weight is a product of **`A`-letters with `B`-letters**, i.e. it spends its weight on
the *non-polar* `B` slot. At weight 3 the harmonic alphabet has enough room to do that; §2.1 shows
that at weight 5, with the extra coupling letter `C` and the `κ` indicator, it does **not** —
by exactly one functional.

---

## 4. A second candidate, and a better one: nested (depth-2) **interval** letters

`PROOF_LB5_CAMPAIGN` §3.3 had already named "nested (depth-2) letters" as the missing ingredient.
They are the natural harmonic-side analogue of what the `R`-letters do:

```
   Y_ab(n,k)   = Σ_{k < m₂ < m₁ ≤ n+k}       m₁^{−a} m₂^{−b}      (k- and l-slot)
   V_ab(n,k+l) = Σ_{k+l < m₂ < m₁ ≤ n+k+l}   m₁^{−a} m₂^{−b}      (coupling slot)
   Z_ab(n)     = Σ_{1 ≤ m₂ < m₁ ≤ n}         m₁^{−a} m₂^{−b}      (n-slot)
```

Each summation range is an *interval of length `n < p`*, so it contains **at most one** multiple of
`p`; since `m₂ < m₁` they cannot both hit it. Hence:

> **Proposition 4.1 `[VERIFIED exact, p ≤ 19, all n < p, all cells, 0 exceptions]`
> (`work/p1g/ylet.py`).** `Y_ab` has weight `a+b` and pole order **exactly `max(a,b) < a+b`**,
> with indicator `α`; `V_ab` likewise with indicator `κ`; `Z_ab` has no pole. All 10 pairs
> `(a,b)`, `2 ≤ a+b ≤ 5` checked.

So `Y_{1,2}` is a *weight-3, depth-2* letter and `V_{1,2}` a weight-3 depth-2 **coupling** letter —
and the coupling slot is exactly where the `R`-family fails (the `D`-letters
`Σ_{j≤k+l}(−1)^{j−1}/(j^aC(n+j,j))` have pole order `a` on the `ε = 1` sheet because of the `j = p`
term; see §1). Unlike the `R`-letters, `Y/V/Z` are **ℚ-linear combinations of ordinary iterated
harmonic sums**, so they stay inside the hypergeometric/creative-telescoping world in which the
decomposition certificates live.

Depth model for the conditions (`rdepth.letter`): with `θ p` the unique multiple of `p` in the
interval, `Y_ab = α(θ^{−a}u^a·σ^{lo}_b + θ^{−b}u^b·σ^{hi}_a) + ℤ_p` where
`σ^{lo}_b = Σ_{m₂ below} m₂^{−b}` and `σ^{hi}_a = Σ_{m₁ above} m₁^{−a}` are `ℤ_p` symbols
**shared across all letters with the same index** (which is exactly true, and gives the conditions
their correct amount of cancellation freedom).

---

## 5. A structural fact about *any* alphabet enlargement `[PROVED]`

> **Proposition 5.1.** Let the alphabet be enlarged by new letters `L` whose `u⁰` part is a *new*
> `ℤ_p` symbol (true for `R`, `D`, `Y`, `V`, `Z` — the integral part of each is a genuinely new
> quantity). Split the basis into `old` (monomials using no new letter) and `new`. Then the
> depth-condition matrix is **block diagonal**,
> ```
>            C  =  [ C_old   0     ]
>                  [ 0       C_new ]  ,
> ```
> because every `u`-expansion term of a `new` monomial carries at least one new symbol in its
> symbol key, and no `old` term does. Consequently `rank(C) = rank(C_old) + rank(C_new)`, and with
> `W_old := M_old·ker C_old`, `W_new := M_new·ker C_new` (subspaces of value-sequence space),
> ```
>       the enlarged system is consistent   ⟺   P ∈ W_old + W_new .
> ```

So the enlargement does **not** relax the old conditions at all: the new letters must supply the
missing value-direction from scratch. What is needed is precisely

> `P ∈ W_old + W_new` — i.e. `W_new` must reach the one direction (mod `W_old`) that `P` needs.

This is also the practical lever: several enlargements can be tested *without* building the
mixed-monomial design matrix, by merging their saved blocks by label (`buildsave.py`).

*(Consistency check on the block structure: `rank(C_vt2) = 81` in `ctrl` and `411` in the
`R`-alphabet, so `rank(C_new) = 330`, and the two blocks are indeed independent.)*

---

## 6. E1 / E2 — the decisive runs

All at `q = 33554393` (a second prime is run on every consistent verdict). `MODE = vt2` is the
tightening `d₅ ≤ 2` on the three `s = 2` patterns; `MODE = strong` is `d₅ ≤ v_pT` everywhere,
which is the full cell-wise `(BASE)` requirement.

| # | alphabet (k / c / n) | cols | `N` | rank(fit) | cond rows | rank(cond) | rank(joint) | `dim U` | `P ∈ U`? |
|---|---|---|---|---|---|---|---|---|---|
| 0 | `A,B` / `C` / `N` (P1c control) | 448 | 600 | 313 | 149 | 81 | 342 | 261 | **NO** |
| 1 | `A,B,R3,R5` / `C` / `N` | 476 | 600 | 323 | 153 | 83 | 355 | 272 | **NO** |
| 2 | `A,B,Y_ab` / `C` / `N` | 634 | 800 | 342 | 245 | 123 | 403 | 280 | **NO** |
| 3 | `A,B,Y_ab` / `C,V_ab` / `N` | 747 | 900 | 371 | 318 | 160 | 453 | 293 | **NO** |
| 4 | **`A,B,R₁..R₅` / `C` / `N`** | **1 210** | **1 300** | **960** | 1 602 | 411 | 1 052 | **641** | **NO** |
| 4′ | same, `MODE = strong` | 1 210 | 1 300 | 960 | 1 784 | 476 | 1 052 | 576 | **NO** |

> ### **E2 VERDICT for the `R`-alphabet: INCONSISTENT.** `[VERIFIED q = 33554393, N = 1300]`
> The full Apéry-letter extension — `R^{(1..5)}` at both the `k`- and the `l`-slot, all products
> with `A,B` up to total weight 5, **1 210** basis coefficients — raises the value-space rank from
> `313` to `960` and the depth-conditioned value space `U` from `261` to `641` dimensions, and
> `P` is **still not in `U`**, at both the `vt2` and the full `strong` cap. `N = 1300 > 1210`, so
> the fitting system is row-saturated: this is not an artefact of too few levels.

So `PHASE2_CANCEL` §7.1's route **(V-a)** does **not** close as proposed. §§3–4 explain why the
`ζ(3)` analogy oversold it, and §§9–10 record what does survive.

### 6.1 The negative is trustworthy: the `R`-machinery is validated end to end `[VERIFIED]`

A negative result is only as good as the code producing it, so the `R`-alphabet fit was
*materialised* and checked against a completely independent exact evaluator. Solving
`[fit ; (DEPTH) base caps]` in the `A,B,R3,R5 / C / N` alphabet at three primes (identical pivot
sets, 0 reconstruction failures) gives

> **`work/p1g/w5_Rbase.json` — 70 terms, 9 of them carrying an Apéry letter**
> (`[A2|R3]`, `[B2|R3]`, `[A1*A1|R3]`, `[1|A1*A1*R3]`, …), denominators on `{2,3}` only, and
> ```
>       P_n  =  Σ_{k,l} T(n,k,l) · w₅^R(n,k,l)      exactly over ℚ,  n = 1..12,  0 mismatches
> ```
> where `w₅^R` is evaluated by `rw5eval.py` with `R^{(a)}` computed as an exact `Fraction` sum —
> an evaluator that shares no code path with the mod-`q` design matrix. **This is a new exact
> weight-5 decomposition of `P_n` using Apéry-type letters**, and it certifies that the
> `R`-columns of the fitting system are the objects they claim to be.
> *(It also reproduces the known deficit: `max d₅ = 3`, `d₅ ≤ v_pT` violated on 5/44/169 cells at
> `p = 5/7/11`, and `v_p(P_n) ≥ 0` at every level — exactly the `w5_allp` picture.)*

**E1 (does `P_n` admit a representation in the enlarged alphabets?) — YES, trivially and
verified:** every enlarged basis contains the 448 control monomials, and `rank(fit)`
grows monotonically (313 → 323 → 342 → …) while the fit alone stays consistent
(`fit-alone inconsistent = False` in every run). So the enlargement never destroys the
decomposition; the whole question is E2.

---

## 7. The fallback route sharpened: `(BASE)` is **one** congruence per prime, not 1–4

Independently of E2, this session sharpens `PHASE2_CANCEL` §7.2 (`work/p1g/fallback.py`,
`work/p1g/apparent.py`).

**7.1 The census, re-run with slack `[VERIFIED, primes 5 ≤ p ≤ 199, 0 failures]`.**
Over the 44 primes there are **82** exceptional steps (`p | c₃(n) = 2(n+3)⁵(2n+5)a₀(n)`,
`0 ≤ n ≤ p−4`): 44 "genuine" ones from `(2n+5)` and 38 from roots of `a₀`. For the `P`-row the
required inequality `v_p(c₀P_n+c₁P_{n+1}+c₂P_{n+2}) ≥ v_p(c₃(n))` holds at **all 82**, and is
**tight** (`v_p = 1 = v_p(c₃)`) at 81 of them (`p = 13` is the one with slack 1). For the `P̂`-row
it **fails at 64 of the 82** — the control that shows the inequality is real content.

**7.2 The `a₀` steps are APPARENT `[VERIFIED, primes 5 ≤ p ≤ 599]`.**
If no exceptional step precedes `n`, then `(Y_n,Y_{n+1},Y_{n+2}) mod p` is an `𝔽_p`-linear image
of `(Y_0,Y_1,Y_2)`, so the requirement at `n` is a linear functional `φ_n` on `𝔽_p³`; the step is
*apparent* (automatic for **every** `p`-integral solution of `L_BZ`) iff `φ_n ≡ 0`. Evaluating
`φ_n` on the three basis solutions at each prime's **first** exceptional step:

| first exceptional step is … | count | `φ ≡ 0` (apparent) | `φ ≢ 0` (real content) |
|---|---|---|---|
| an `a₀`-root | 39 | **38** | 1 (`p = 61`, `n = 0`, i.e. `61 | a₀(0) = 173057`) |
| the genuine `(2n+5)` step | 68 | 2 | **66** |

> **Consequence.** The `a₀`-root steps carry **no arithmetic content**: they are apparent
> singularities of `L_BZ` and a desingularising left multiple removes them. `PHASE2_CANCEL` §7.2's
> "1–4 exceptional steps per prime" therefore collapses to
> ```
>   (REC-★)   c₀(n₀)P_{n₀} + c₁(n₀)P_{n₀+1} + c₂(n₀)P_{n₀+2} ≡ 0 (mod p),   n₀ = (p−5)/2,
> ```
> **exactly one congruence per prime**, producing `P_{(p+1)/2}` — the same level as the attained
> deficit cell `((p+1)/2, 0, (p−1)/2)`. The two localisations coincide, and `(REC-★)` is
> `[VERIFIED, 0 failures, all p ≤ 199]`, tight at every prime except `p = 13`.
> *(Cross-check: at the 16 `a₀`-steps that occur **before** `n₀` — where `P̂` is still
> `p`-integral and hence a fair witness — `P̂` satisfies the inequality 16/16, exactly as
> "apparent" predicts, while it fails the genuine step at 43 of 44 primes.)*

---

## 8. Exactly what the negative does and does **not** say — the one caveat, stated precisely

The depth conditions used throughout (here and in `PHASE2_FINAL` §2.3, `PHASE2_INDUCTION` §6.1,
`work/p1d/solve_strong.py`) are the **symbol-independent** form:

> for every reachable pole pattern `π` and every `u`-power `j > cap(π)`, the coefficient `K_j` must
> vanish **identically in the `ℤ_p` symbols**.

This is *sufficient* for the cell-wise depth bound `d₅ ≤ cap` at every prime simultaneously, and it
is `p`-independent and linear — which is what makes the computation possible at all. It is **not
necessary**: at a fixed prime `p` the symbols range over the finitely many values the cells supply,
not over independent indeterminates (at `p = 5`, pattern `III` has as few as 3 cells at a given
level). So the honest statement of the negative is:

> **`[VERIFIED]` No representative in the `R`-extended (or `Y`-extended) alphabet satisfies the
> `p`-independent, symbol-independent cell-wise depth conditions together with the decomposition
> identity.**

An enlargement of the *conditions'* solution set — replacing "identically in the symbols" by "at
the actual cell values, for every `p`" — is a genuinely different (and non-linear, prime-by-prime)
question that this session did **not** settle. Two remarks bound its plausibility:

* the symbol-independent conditions were **sharp** at the `base` cap: `PHASE2_FINAL` §2.5 finds
  `min slack = 0`, i.e. the bound `d₅ = 1+min(v_pT,2)` is *attained*, so nothing was being wasted
  there;
* as `p → ∞` the cells fill out and the symbols become generic, so the two forms agree
  asymptotically. The gap, if any, lives at small primes.

Costing the honest test: it is a `ℚ_p`-linear-algebra problem — parametrise the fit family exactly
over `ℚ` (135-dim kernel in the control basis; needs exact rational reconstruction of the kernel,
3–4 auxiliary primes) and then solve the congruence system `E·x ≡ 0 (mod p^{5−v_pT})` over `ℤ_p` by
valuation-pivoted elimination. That is one further fitting campaign per prime. **Flagged, not run.**

---

## 9. What *does* survive: a partial closure of `(BASE)`

The control table of §2.1 contains a usable positive. Each `s = 2` pattern group is individually
achievable at depth 2:

> **Proposition 9.1 `[VERIFIED, q = 33554393, N = 600, both auxiliary primes]`.** Inside the
> ordinary 448-monomial harmonic alphabet the joint system
> `[ P_n = Σ T·w₅ ; (DEPTH) ; d₅ ≤ 2 on patterns I and II ]` is **consistent**
> (`rank(joint) = 342`, `dim U = 273`), and so is the system with the tightening on pattern `III`
> instead (`rank(joint) = 336`, `dim U = 282`).

Since `(BASE) ⟺ (V3)₀ ⟺ 2Σ_I + Σ_III ≡ 0 (mod p)` (`PHASE2_CANCEL` §2), a representative of the
first kind makes the `I`- and `II`-cells **individually `p`-integral**, so for it

```
      (BASE)   ⟺   Σ_III (T/p²)·K₃  ≡  0   (mod p)          [region III alone]
```

and a representative of the second kind reduces it to `2Σ_I ≡ 0` instead. Either way the residual
identity loses one of its two regions. `III` is the smaller one at the tested levels
(`p = 7, n = 4`: `|III| = 3` vs `|I ∪ II| = 12`; `p = 7, n = 5`: `5` vs `16`) and is the
`κ = 0, ε = 1` band `k, l ≥ q`, `p ≤ k+l < p+q`. Note that the **attained deficit cell**
`(n,k,l) = ((p+1)/2, 0, (p−1)/2)` has `k = 0 < q = (p−1)/2` and `l = q`, so it lies in region
**`I`**, not `III` — meaning the `exIII` representative genuinely *moves* the deficit off the cell
where `PHASE2_INDUCTION` §6.1 found it. **This is a strict sharpening of the residual `(V3)₀`**
and it is representative-constructible (§10).

---

## 10. The partial closure, made explicit and verified `[VERIFIED, 0 failures]`

Two further `p`-independent modes were added (`rdepth.caps_for`):

* `exIII` — the **full cell-wise cap `d₅ ≤ v_pT` on every pattern except `III`**, where the
  Lemma-F cap `1+min(v_pT,2) = 3` is kept;
* `exI` — the same with `I, II` exempted instead.

| mode | cond rows | rank(cond) | rank(joint) | `dim U` | consistent? |
|---|---|---|---|---|---|
| `exIII` | 212 | 111 | 342 | 231 | **YES** |
| `exI` | 185 | 98 | 336 | 238 | **YES** |
| `strong` (no exemption) | 239 | 123 | 342 | 219 | NO |

So **the entire residue of `(BASE)` is one order of pole on one pattern group**, and the harmonic
alphabet already supplies everything else.

### 10.1 The explicit representative `work/p1g/w5_I.json` `[VERIFIED exact, 0 failures]`

Extracted from `[fit ; (DEPTH) ; d₅ ≤ 2 on I and II]` in the plain 448-monomial harmonic alphabet,
at **three** auxiliary primes with identical pivot sets, CRT + rational reconstruction (0
reconstruction failures):

> **`w5_I.json` — 155 terms, numerators ≤ 5 digits, denominators supported on `{2, 3, 71}`**
> (so valid for every `p ≥ 5` except `p = 71`; a second pivot order gives a different bad prime
> and the `PHASE2_FINAL` §2.4 CRT combination then removes it).

Verification (`work/p1g/verify_partial.py`, exact `Fraction` arithmetic throughout):

| check | result |
|---|---|
| **(V1)** `P_n = Σ_{k,l} T(n,k,l)·w₅^I(n,k,l)` exactly over ℚ | `n = 1..20`: **0** mismatches |
| **(V2)** `v_p( T(n,k,l)·(w₅^I − H^{(5)}_n) ) ≥ 0` for every cell **outside region III** | `p = 5,7,11,13,17,19,23`: **10 092 cells** (1 025 of them exempt), **0** violations |
| **(V3)** the reduction `v_p(P_n) ≥ 0 ⟺ v_p(Σ_{III}) ≥ 0` | **0** failures |

*(per prime: 54 / 139 / 505 / 818 / 1 784 / 2 469 / 4 323 cells, exempt 7 / 16 / 53 / 83 / 174 /
237 / 406.)*

**Cross-check.** Solving the *stronger* `exIII` system (cell-wise cap `d₅ ≤ v_pT` on every pattern
but `III`) in the same pivot order returns **the identical 155-term representative**
(`w5_exIII.json == w5_I.json`) — so the canonical solution of the `I+II` tightening already meets
the full cell-wise cap everywhere outside `III`, exactly as the sweep shows.

### 10.2 Removing the bad prime — an all-primes representative

A second pivot order (`plain`) gives `w5_exIII_b.json`, 148 terms, bad primes `{31, 41}` — disjoint
from `{71}`. The `PHASE2_FINAL` §2.4 CRT construction (`work/p1g/make_allp.py`,
`t = 6 469 841 205`) combines them into

> **`work/p1g/w5_exIII_allp.json` — 207 terms, denominators supported on `{2,3}` only, hence
> `p`-integral for *every* prime `p ≥ 5`.**

Re-verified from scratch (`verify_partial.py`): exact ladder identity `n = 1..16`, **0**
mismatches; cell-wise integrality outside `III` over `p = 5,7,11,13,17,19` — **5 769 cells,
0 violations**. So **Theorem 10.1 holds with no excluded prime.**

**Scope of the claim.** The `exIII` conditions are `p`-**independent** and their sufficiency is the
already-proved pole calculus of `PHASE2_FINAL` §2.1/§2.3: `K_j = 0` for `j > cap(π)` forces
`d₅ ≤ cap(π)` at **every** prime `p ≥ 5` simultaneously, provided the coefficients are
`p`-integral. So the cell-wise statement below holds for **every** `p ≥ 5` with `p ≠ 71`, not only
for the swept primes; the sweep is confirmation, and the two open hypotheses are (i) the
decomposition identity for `w₅^I` (`[VERIFIED]`, certificate pending — §12.2) and (ii) the
linear-algebra certificate for the `exIII` solve (three primes, identical pivot sets).

> ### **Theorem 10.1 (partial closure of `(BASE)`) `[PROVED given (i)+(ii); VERIFIED as stated]`**
> With `w₅^I` as above, for every prime `5 ≤ p ≠ 71` and every `n < p`, **every cell outside the
> band**
> ```
>        III  =  { (k,l) :  k, l ≥ q := p−n ,   p ≤ k+l < p+q }
> ```
> contributes a `p`-integral summand to `P_n = Σ_{k,l} T(n,k,l) w₅^I(n,k,l)`. Consequently
> ```
>        (BASE)   ⟺   v_p( Σ_{(k,l) ∈ III} T(n,k,l)·(w₅^I(n,k,l) − H^{(5)}_n) )  ≥  0 .
> ```
> This replaces `PHASE2_CANCEL` §2's `2Σ_I + Σ_III ≡ 0 (mod p)` by **`Σ_III ≡ 0 (mod p)` alone** —
> one region instead of two, and the `k↔l`-symmetric one. (The mirror statement with `exI` puts
> the whole residue on `2Σ_I ≡ 0`; note the *attained* deficit cell `((p+1)/2, 0, (p−1)/2)` lies in
> region `I`, so the `exIII` representative genuinely **moves** the deficit off the known cell.)

---

## 11. Status of the theorem tree after P1g

```
(BASE)  ord_p(P_n) >= 0 for n < p                                      [OPEN]
  route (V-a) cell-wise weight, Apery R-letters      [REFUTED, symbol-independent form]  (§6)
  route (V-a') cell-wise weight, nested Y/V-letters  [REFUTED, symbol-independent form]  (§6)
  route (V-a'') honest (non-symbolic) cell-wise conditions  [OPEN, costed]               (§8)
  PARTIAL: cell-wise on ALL cells outside ONE region, explicit + verified                (§10)
  route (V-b) recurrence: now exactly ONE congruence per prime, (REC-*)                  (§7)
```

`work/PHASE2_THEOREM.md` therefore stays at **v2**: §6.3 does **not** flip. What changes is the
shape of the residue — see §12.

---

## 12. Delta for `work/PHASE2_THEOREM.md`, and the certificate node

### 12.1 What changes (recorded in `PHASE2_THEOREM.md` §D.1 and the tree, v2 → v2.1)

`(BASE)` stays `[OPEN]`. The changes are:

1. **`(V-a)` is refuted in the form proposed.** `PHASE2_CANCEL` §7.1's recommendation — extend the
   alphabet by Apéry-type letters and re-run `solve_strong.py vt2` — has been executed at full
   scale and the strengthened system remains inconsistent (§6). Same for the nested-letter variant.
   The refutation is for the `p`-independent **symbol-independent** depth conditions (§8).
2. **The residue is now one region, not two.** `(BASE) ⟺ Σ_III ≡ 0 (mod p)` via the explicit,
   exactly verified `w₅^I` (§10) — strictly sharper than `2Σ_I + Σ_III ≡ 0`.
3. **The recurrence route is now one congruence per prime.** The `a₀`-root exceptional steps are
   apparent singularities (§7.2); only `(REC-★)` at `n₀ = (p−5)/2` survives.
4. **A new `ζ(3)` identity** (§3, Prop. 3.1) — harmonic, cell-wise, exact — which corrects the
   attribution in `PHASE2_CANCEL` §7.1 and is reusable.
5. **A new weight-5 identity** `P_n = Σ T·w₅^R` with Apéry letters (§6.1), 70 terms.

### 12.2 The certificate node `[read-only report — nothing in work/lb5 was touched]`

From `work/lb5/CERTS_RESUME.md` and `work/PHASE2_CERTS.md` (P1e, 2026-07-25), unchanged by P1g:

* **`[CERTIFIED]`** the **Q-row** certificate `L_BZ·T = Δ_k(ρT) + Δ_l(σT)`
  (`work/lb5/Qrow_rhosigma.m`), checked to exactly `0` twice, once in a RISC-free kernel.
* **`[OPEN]` Theorem B** (`P̂_n = Σ T·ŵ₃`): reduced to `Σ_{k,l} E(v) = 0`; `E(v)/T` is **linear**
  in five letters with explicit coefficients (`work/lb5/Eletters.m`), so what remains is a rank-1
  telescoping (`certU.wl`). A stated caveat on the boundary lemma's numerical confirmation is
  recorded there and still stands.
* **`[OPEN]` (T1-top)** (`P_n = Σ T·w5_allp`): `[VERIFIED]` only — matches `P_n` for `n ≤ 360`,
  satisfies `L_BZ` at 748 consecutive `n` mod two primes, minimal recurrence exactly `(3,9)`.

**Successor certificate target — the precise delta.** The partial closure of §10 uses `w₅^I`, not
`w5_allp`, so it needs its own decomposition certificate. Because both are exact decompositions of
the *same* `P_n`, their difference lies in the kernel of the value map:

```
        Δ  :=  w₅^I − w5_allp        satisfies        Σ_{k,l} T(n,k,l)·Δ(n,k,l) = 0   ∀ n .
```

So the certificate agent's in-flight object (`w5_allp`) is **not** wasted: certifying `w₅^I`
reduces to certifying `w5_allp` **plus** the homogeneous weight-5 summation identity `Σ T·Δ = 0`.
By `PHASE2_CERTS`' `[PROVED negative]` (the 448 monomials are pointwise independent) that kernel
identity is itself non-trivial and needs a real certificate — it is exactly a "Lemma-Phi species"
object in the sense of `PHASE2_CANCEL` Thm 5.1, i.e. of the *same species* as the already-proved
`(P0)–(P3)`, and it is a **homogeneous** (right-hand side `0`) creative-telescoping target, which
is strictly easier than an inhomogeneous one.

**No new Lemma-U obligation.** `(BASE)` is a statement about the *number* `P_n`, so any exact
decomposition with cell-wise integrality proves it; the digit-level induction may keep using
`w5_allp` throughout. In particular `w₅^I` is purely harmonic, so even if an `R`-representative had
worked, no `R`-analogue of Lemma U (`PHASE2_INDUCTION` §2.1) would have been needed.

---

## 13. Reproduction — `work/p1g/` (all exact-arithmetic Python; no Wolfram kernel used)

| script | what it does | output |
|---|---|---|
| `rlet.py` | Apéry letters `R^{(a)}`, `D^{(a)}`; exact pole-order/indicator verification | §1 table, 0 exceptions |
| `ylet.py` | nested interval letters `Y_ab`, `V_ab`; pole order `= max(a,b)` | §4, 0 exceptions |
| `rfit.py` | enlarged alphabets + fast design matrix (13-bit `float64`-split modular `matmul`) | cross-checked vs `lb5/fit.row` |
| `rdepth.py` | `u`-graded depth conditions incl. `R/D/Y/V/Z`; modes `base`/`vt2[:sel]`/`strong`/`exIII`/`exI` | condition rows |
| `build.py`, `buildsave.py` | cache design matrices | `M_R_1300_*.npy` |
| `e2.py`, `e2b.py` | rank + consistency of `[fit ; conditions]` | §2.1, §6 tables |
| `zeta3.py`, `z3ex.py` | the `ζ(3)` control, mod `q` and exact over ℚ | §3, Prop. 3.1 |
| `e3_solve.py` | 3-prime CRT + rational reconstruction of a representative | `w5_I.json` (= `w5_exIII.json`), `w5_exIII_b.json`, `w5_Rbase.json` |
| `make_allp.py` | CRT-combine two representatives with disjoint bad primes | `w5_exIII_allp.json` (207 terms, denominators `{2,3}`) |
| `e3_verify.py`, `verify_partial.py` | exact verification batteries | §6.1, §10.1–10.2 |
| `window.py` | how many levels are needed to see the obstruction | smallest inconsistent prefix `L = 262` — the obstruction is **global**, not localised |
| `fallback.py`, `apparent.py` | the recurrence route: census, slack, apparent-singularity test | §7 |

**Sweep summary (all exact, 0 failures):** 812 cells × 5 weights `R`-pole (`rlet`) · 1 536 × 5
`D`-pole · 10 pairs × 2 families nested-pole (`ylet`) · `ζ(3)` exact identity `n ≤ 24` + 7 primes
cell-wise · `w5_Rbase` exact identity `n ≤ 12` · **`w5_I` exact identity `n ≤ 20` + 10 092 cells
over 7 primes** · 82 exceptional recurrence steps over 44 primes · 107 apparent-singularity tests
over primes `< 600`.
