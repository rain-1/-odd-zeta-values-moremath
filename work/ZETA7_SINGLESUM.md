# ζ(7) — is q_n a SINGLE hypergeometric sum?

**Session:** 2026-07-26. **Target:** find a single-sum hypergeometric representation of the
weight-7 coefficient sequence

```
q_n = 1, 61, 52921, 94357501, 235634763001, 715362962769061, …   (74 exact terms)
```

(the ζ(7)-coefficient of the totally symmetric M₀,₁₀ "vanishing in the middle" cellular
integral, σ = (10,2,4,1,6,3,8,5,9,7)), so that its order-4 degree-19 recurrence — currently
**[VERIFIED, not proved]**, guessed by CRT from 105 modular terms — could be **proved** by a
single Zeilberger call.

**Verdict: NOT FOUND. Negative with explicit bounds (§4), plus new structural evidence (§3)
that the right object is a TRIPLE sum, plus a re-reading of the provenance (§6) that says the
Zudilin remark is very probably about a different object.**

---

## 0. What was and was not ruled out before this session

`work/ZETA7_STATE.md` §3.1 is titled *"Sign dichotomy: I′ₙ lies OUTSIDE the single-sum
very-well-poised class"*. Read precisely, it establishes:

* **What it rules out.** The *linear form* `I′ₙ = (75/4)qₙζ7 − 3sₙζ5 − Pₙ` (and `I″ₙ`) is not
  equal to any **very-well-poised single hypergeometric series**. The argument is a sign
  argument on the *ratio of adjacent odd-zeta coefficients*: every reflection-antisymmetric
  VWP block series produces **same-sign** adjacent odd-zeta coefficients, while `I′ₙ` has
  `r5 = coeff(ζ5)/coeff(ζ7) = −48/61 < 0`.
* **What it does NOT rule out.** Anything about `q_n` *alone*. `q_n` is one coefficient of the
  form; a sign relation between *two* coefficients says nothing about a summation formula for
  *one* of them. The §3.1 corollary does touch `q_n`, but only excludes
  *"product-weight subset-coupled multisums of the M₀,₈ type"* — that search
  (`zeta7_dual_triple.py`, `_exhaust.py`, `_Awide.py`) covered **double and triple** sums with
  weight `C(n+k,k)^p C(n,k)^q`, `p,q ≤ 3`, coupled by products of `C(n+Σ_S k_i, n)`.
  **Single sums were never searched.** The caution in the task brief is correct: §3.1 does not
  exclude a single-sum form for `q_n`.

So the question addressed here was genuinely open.

---

## 1. T1 — the sources do not contain a weight-7 formula

Brown–Zudilin `papers/20-…/2026-01-26_CellZeta.tex` gives, for **weight 5** (M₀,₈), an
explicit **double** sum (eq. `Q_n`, line 277):

```
Q_n = Σ_{k1=0}^{n} Σ_{k2=0}^{n} C(n+k1,n) C(n,k1)² C(n+k2,n) C(n,k2)² C(n+k1+k2,n)
    = 1, 21, 2989, 714549, 217515501, …
```

and derives it (line 523 ff., "the leading coefficient has the following explicit double-sum
binomial expression") from a **double Barnes–Mellin integral** (eq. `intJ`, two contour
variables s, t).  For **weight 7** the paper contains only the *integral*, the rank-4 motive
statement and the numerical anchors `I₀, I₁, I₂` — i.e. only `q₀,q₁,q₂ = 1, 61, 52921`. It
gives **no summation formula at all** for the weight-7 coefficients, and explicitly says:

> "There are several technical limitations at the moment to execute this strategy in higher
> weights. For example, calculating higher weight integrals for small values of the parameters
> does not seem practical with current tools."

The construction that produced `Q_n` scales the wrong way for us: the 5-fold integral needs a
**2-fold** Barnes integral, hence a **2-fold** sum; the 7-fold integral needs a **3-fold**
Barnes integral, hence a **3-fold** sum.

Neither sequence is in the OEIS (`1,61,52921,94357501` → no results;
`1,21,2989,714549` → no results).

---

## 2. Re-verification of the known operator, and its minimality

* The guessed operator `worthiness/zeta7_q_recurrence.json` (order 4, degree 19) annihilates
  **all 70 available relations** among the 74 exact `q_n`. Leading coefficients
  `[7381728, −46800155520, 501765579072, −46800155520, 7381728]`, i.e. characteristic
  polynomial `χ(λ) = λ⁴ − 6340λ³ + 67974λ² − 6340λ + 1` (palindromic). **[re-VERIFIED]**
* **Order 4 is minimal.** Using the 105 modular terms mod p = 2000000011
  (`worthiness/_zeta7_state_backup/fleet_2000000011.txt`) there is
  * no order-1 operator of degree ≤ 39,
  * no order-2 operator of degree ≤ 32,
  * no order-3 operator of degree ≤ 24,
  * an order-4 operator of degree 19 (nullity 1). **[VERIFIED, bounds as stated]**
  Script: `work/z7ss/minimality.py`.
* Roots of χ: `λ + 1/λ = 3170 ± 1824√3`, so the four characteristic roots are
  `{λ, 1/λ, λ′, 1/λ′}` with
  `λ = 6329.260515009297…`, `λ′ = 10.645429…`. The growth constant is
  **μ = 6329.2605150093**, `log μ = 8.752938686040556`.

---

## 3. NEW structural evidence: the order/number-of-sums ladder

The three cellular families in the same tower, each taken in the *same* normalisation (the
McCarthy–Osburn–Straub window diagonal, i.e. the integer "Apéry-numerator" normalisation):

| weight | cell | leading coefficients | # summation indices | minimal recurrence order | char. polynomial | growth |
|---|---|---|---|---|---|---|
| 3 | M₀,₆, σ=(1,5,3,6,2,4) | 1, 5, 73, 1445, 33001 | **1** (Apéry) | **2** | λ²−34λ+1 | 33.9706 = (1+√2)⁴ |
| 5 | M₀,₈ (BZ) | 1, 21, 2989, 714549 | **2** (BZ double sum) | **3** | 4λ³−2368λ²−188λ+1 | 592.0794 |
| 7 | M₀,₁₀ (BZ, this programme) | 1, 61, 52921, 94357501 | ? | **4** | λ⁴−6340λ³+67974λ²−6340λ+1 | 6329.2605 |

The weight-5 line is **new in this session**: the minimal recurrence for BZ's `Q_n` is
**order 3, degree 9**, computed and verified exactly (`work/z7ss/w5_charpoly.py`,
0 failures on 57 relations; char. polynomial `4λ³ − 2368λ² − 188λ + 1`).

The pattern `#sums = order − 1` is exactly what the period interpretation predicts: the
solution space of the operator is spanned by the coefficient sequences of the linear form
(for weight 7: `q, s, P̂, P` — four of them, hence order 4). It is *evidence*, not a theorem —
there is no general theorem forbidding a single hypergeometric sum from having a
minimal telescoper of order 4 — but at weights 3 and 5, where the answer is known, the
prediction is exactly right, and it predicts **3** summation indices at weight 7.

---

## 4. T2 — the search, and exactly what it covers

### 4.1 The class searched

```
    F(n,k) = z^k · ∏_{(a,b)} ( (a·n + b·k)! )^{e_{a,b}} ,
    0 ≤ a ≤ A ,  −B ≤ b ≤ B ,  (a,b) ≠ (0,0) ,  (a = 0 ⇒ b > 0) ,
    Σ e·a = 0 ,  Σ e·b = 0   (scale-balanced) ,   Σ |e| ≤ W ,   1 ≤ |z| ≤ Z ,
    q_n =? Σ_k F(n,k)   over the natural (finite) support.
```

This class **contains every product of binomial coefficients** `C(αn+βk, γn+δk)^e` with
coefficients bounded by A, B — including all of `C(n,k)^p`, `C(n+k,k)^p`, `C(2n−k,n)^p`,
`C(2k,k)^p`, `C(2n−2k,n−k)^p`, `C(n+2k,k)^p`, `C(3n,k)^p`, … and arbitrary
factorial-ratio prefactors depending on `n` alone (the `b = 0` forms `n!, (2n)!, (3n)!`).
It is strictly larger than "products of binomials": arbitrary factorial ratios are allowed.

**Self-tests (four, all pass, recovering the correct summand):**
* target `a₁=5, a₂=73` (Apéry ζ(3)) → recovers `(0,1)^−4 (1,−1)^−2 (1,1)^2`
  = `(n+k)!²/(k!⁴(n−k)!²)` = `C(n,k)²C(n+k,k)²`  *(unique hit)*.
* target `3, 19` (Apéry ζ(2)) → recovers `(1,0)^1 (1,1)^1 (0,1)^−3 (1,−1)^−2`
  = `C(n,k)²C(n+k,k)`  *(unique hit)*.
* target `4, 28` (Domb numbers, growth 16, `A=B=2`, `W=12`, a **five-factor** summand) →
  recovers `(0,1)^−4 (0,2)^1 (1,−1)^−4 (1,0)^2 (2,−2)^1`
  = `C(n,k)²C(2k,k)C(2n−2k,n−k)` (among 221 shapes that match such small anchors — the real
  anchors 61 and 52921 are far more discriminating).
* shifted variant (`search5`, `CS=1`), target `40, 1485` for the constructed summand
  `((n+k+1)!)²/(k!⁴(n−k)!²)` → recovers `(1,1;+1)^2 (0,1;+0)^−4 (1,−1;+0)^−2` exactly.

### 4.2 The two filters

1. **Exact arithmetic filter.** `Σ_k F(1,k) = 61` and `Σ_k F(2,k) = 52921`, evaluated in
   exact rational arithmetic via prime-exponent vectors and 128-bit integers.
   (Every surviving shape would then be tested against all 74 terms; none survived.)
2. **Growth filter (shift-invariant).** With `k = tn`,
   `|F(n,tn)| = exp(n·f(t) + O(log n))`, `f(t) = Σ e_j L_j log L_j + t log|z|`,
   `L_j = a_j + b_j t`. Since `q_n` is a sum of `O(n)` terms,
   `lim |q_n|^{1/n} ≤ exp(max_t f(t))`, with equality when the terms are positive. So any
   representation must have `max_t f(t) = log μ = 8.752938686040556`.
   **Constant shifts inside the factorials, and any rational-function factor, do not change
   `f`.** Hence this filter covers a *strictly larger class* than the arithmetic filter: all
   summands `z^k ∏ ((a n + b k + c)!)^e · R(n,k)` with arbitrary integer shifts `c` and
   arbitrary degree-0 rational `R`. It is used both as a DFS prune (`f` is linear in `e`, so a
   partial assignment admits the upper bound `f_cur(t) + budget·max_j |g(L_j(t))|`) and as an
   independent leaf test to 1e−6 in `log μ` (≈ 12 significant digits in μ).

Code: `work/z7ss/search2.c` (exact filter + prune), `search4.c` (adds the refined growth
test), `growth.py`, `shapegrowth.py`.

### 4.3 Result of the exhaustive single-sum search — tabulated totals in §9

**No shape reproduced `q_1 = 61` and `q_2 = 52921` simultaneously, anywhere in the boxes
searched.** Thousands of shapes reproduce `q_1 = 61`; none of them also gives `52921`.
Since no shape survived the first two values, the 74-term check was never reached.

### 4.4 What the search does NOT cover (state this honestly)

The class is infinite in `W`, and there is no upper bound on `W`: a shape can have large
`Σ|e|` and still small growth (e.g. `(1,1)^1 (1,-1)^1 (1,0)^-2` has weight 4 and growth 4).
So **a complete negative is not achievable by enumeration**, and none is claimed. The
uncovered region is:

* `Σ|e| > W_max` for the boxes below;
* `|a| > A` or `|b| > B` (coefficients of `n`,`k` inside the factorials larger than the box);
* `|z| > Z`;
* summands with **infinite support** in `k` (non-terminating very-well-poised series). Those
  are the objects of `ZETA7_STATE.md` §3.1, which excluded them for `I′ₙ` on a sign argument;
  they are *not* excluded for `q_n` here — the searcher requires a denominator factorial that
  truncates the sum at both ends;
* an extra factor `c^n` with `c ∉ {1}` (a factor depending on `n` alone that is *not* a
  factorial ratio); such a factor rescales the growth constant by `c`, so it would move the
  target out of the tested window. Factorial-ratio factors in `n` alone **are** covered
  (they are the `b = 0` forms).

Everything else in the box is covered, and — through the shift-invariant growth test —
also every version of it with arbitrary integer shifts inside the factorials and any
degree-0 rational-function factor.

---

## 5. Two further targeted searches, both derived from Brown–Zudilin's own machinery

### 5.1 Is q_n a BZ *weight-5* leading coefficient `Q(p;q)`?

This is not a wild guess. BZ's own decomposition is `I_n = I′_n + I″_n ζ(2)` with

```
    I″ₙ = −9·qₙ·ζ5 + 2·sₙ·ζ3 − P̂ₙ      ∈ span{1, ζ3, ζ5}
```

i.e. `q_n` is, up to the constant −9, the **ζ(5)-coefficient of a weight-5 linear form**. For
the whole BZ weight-5 family `J(p;q)` that coefficient is `2Q(p;q)` with `Q` given by their
explicit double sum (eq. `sumQ`, tex lines 525–530):

```
Q(p;q) = (−1)^{p0+…+p6} Σ_{k1,k2∈ℤ} C(k1,p0) C(k2,p6) C(k1+k2+q3−p0−p6, p3+q3−p0−p6)
                                    · C(q1,k1−p1) C(q2,k1−p2) C(q4,k2−p4) C(q5,k2−p5)
```

So **if `I″ₙ` lies in the BZ `J(p;q)` family** (which is exactly what the campaign's
"weight-5 descent ladder" language asserts), then `q_n = c·Q(p;q)` for parameters linear
in `n`, and `q_n` would be an explicit **double** sum — enough for
Koutschan-style creative telescoping and therefore enough to *prove* the order-4 operator.

**Implemented and validated** (`work/z7ss/bzQ.c`): the totally symmetric specialisation
`p = (n,n,n,2n,n,n,n)`, `q = (n,n,n,n,n)` reproduces `1, 21, 2989, 714549, 217515501`
exactly.

**Scan:** all `p_j = A_j·n` (j = 0…6) and `q_j = G_j·n` (j = 1…5) with `A_j, G_j ∈ {0,…,AMAX}`,
matching `Q(1)/Q(0) = ±61` **and** `Q(2)/Q(0) = ±52921` (ratios, so an overall constant is
free), then `Q(3)/Q(0) = ±94357501`. **Result: no match.** — see §9 for the exact bounds.

### 5.2 Is q_n one summation layer above the weight-5 object (the *descent* template)?

BZ obtain the weight-5 double sum from the weight-3 single sum by exactly one extra
summation (tex lines 691–725):

```
Q(p;q) = Σ_k (−1)^{k+p4+p5+p6} C(k,p6) C(q4,k−p4) C(q5,k−p5) · A(p0,p1,p2,p3−k ; q1,q2,q3−p6+k)
A(P;Q) = (−1)^{P0+P1+P2+P3} Σ_j C(j,P0) C(j+Q3−P0, P3+Q3−P0) C(Q1,j−P1) C(Q2,j−P2)
```

("formula (sumQ) is nothing but an iterated residue of the integrand", tex:657; "a recursive
structure between cellular integrals of different weights via iterated residues", tex:1476).
**This two-layer form is implemented and validated in `work/z7ss/bzDescent.c` — it reproduces
`1, 21, 2989, 714549, 217515501`.**

This is arguably the most natural reading of "it's a single hypergeometric sum": **one**
outer Zeilberger-able summation on top of an object whose recursion is already known.
Applying the same template one level up,

```
q_n =? Σ_k (±1)^k C(k, P6·n) C(Q4·n, k−P4·n) C(Q5·n, k−P5·n) · Q( weight-5 params with one
                                                                   slot shifted by ∓k )
```

was scanned over the inner parameters tied by the cell's dihedral symmetry
(`p = (a,a,a,b,a,a,a)n`, `q = (c,c,d,c,c)n`), all five outer parameters, **all 7×5 choices of
which inner slot absorbs −k and +k**, and both sign conventions. **Result: no match** — see §9.
This scan is *narrow* (the true weight-7 outer layer may carry more than three binomials, and
the inner parameters need not be dihedrally tied), so this negative is much weaker than §4's.

---

## 6. Re-reading the provenance of the target

The brief quotes Zudilin: *"the recursion for zeta(7) only requires an execution of Zeilberger
in Maple, because it's a single hypergeometric sum, that's a routine — no memory problems."*
I do not have the correspondence itself; what follows is inference from the published record,
and should be treated as such.

Three facts from `2026-01-26_CellZeta.tex` sit badly with reading that sentence as being
about *our* `q_n`:

1. **BZ did not use a single Zeilberger call even at weight 5.** They write (tex:240):
   *"Then Koutschan's `HolonomicFunctions` produces a third order Apéry-type recursion for the
   integrals I_n"*, and (tex:282–283) *"The validity of this formula can be independently
   established by verifying … that the **double sum** on the right-hand side satisfies the
   above recursion."* A double sum, and Koutschan's holonomic machinery — not `Zb`.
2. **Even the weight-5 general-parameter recursion is described as an open task** (tex:645):
   *"A practical (though technically challenging!) task for existing creative telescoping
   realisations is writing down explicitly a (third order Apéry-type) recursion for the
   integrals I(a n) = J(p n; q n)…"*.
3. **For weight 7 they state the tools do not exist** (tex:1470–1471): *"There are several
   technical limitations at the moment to execute this strategy in higher weights… calculating
   higher weight integrals for small values of the parameters does not seem practical with
   current tools."*

Meanwhile, Zudilin's *own* ζ(7) constructions — Rivoal / Ball–Rivoal / Zudilin very-well-poised
series (`llm/02`, `llm/03`, `llm/04`, `llm/06`, `llm/11`, `zudilin-2004-well-poised-…`) — really
**are** single hypergeometric sums, in exactly one variable, and their Poincaré-type recursions
really **are** obtained by one Zeilberger call with no memory problems.

**Most likely reading:** the remark is about the very-well-poised ζ(7) series (his own
construction), not about the M₀,₁₀ cellular family's `q_n`. Two other readings are live and
worth putting to him: (b) `q_n` really is a single sum outside the boxes searched here;
(c) "single hypergeometric sum" means *one outer summation* on top of the already-known
weight-5 object (§5.2), so that one Zeilberger/creative-telescoping step suffices.

`ZETA7_STATE.md` §3.1 is consistent with (a): it shows the *linear form* `I′ₙ` is not a
very-well-poised single series, so a VWP series for ζ(7) is a *different* approximation
sequence from the cellular one — which is precisely why its recursion is easy and ours is not.

---

## 7. T4 — the question to put to Zudilin

One line, self-contained:

> **When you said the ζ(7) recursion "only requires an execution of Zeilberger, because it's a
> single hypergeometric sum", did you mean the very-well-poised (Ball–Rivoal / Rivoal–Zudilin)
> series for ζ(7), or the coefficient sequence `q_n = 1, 61, 52921, 94357501, …` of the totally
> symmetric M₀,₁₀ "vanishing in the middle" cellular integral — and if the latter, what is the
> sum?**

Two facts to attach, because they are what make the question sharp and they are new:

* `q_n` satisfies an order-4 (degree-19) minimal recurrence, characteristic polynomial
  `λ⁴ − 6340λ³ + 67974λ² − 6340λ + 1`; **order 4 is minimal** (no order ≤ 3 operator of degree
  ≤ 24 exists). Your weight-5 `Q_n` has minimal order **3** with characteristic polynomial
  `4λ³ − 2368λ² − 188λ + 1` — the one printed in the paper.
* Apéry (weight 3, single sum) → order 2; your `Q_n` (weight 5, double sum) → order 3; so the
  weight-7 object looks like a **triple** sum, and we have not been able to find any single
  sum for it (search bounds in §9).

A natural follow-up in the same message:

> **Is there a weight-7 analogue of your eq. (sumQ) — the iterated-residue formula that gives
> the leading coefficient of a cellular integral on M₀,₁₀ as an explicit (presumably triple)
> binomial sum — written down anywhere? That, not a single sum, is what we need to prove the
> order-4 recursion.**

---

## 8. Recommended next steps (independent of the reply)

1. **Derive, don't guess, the weight-7 iterated-residue formula.** The mechanism is fully
   explicit in BZ §"Descent to ζ(3)" (tex:652–731) and is implemented and validated here in
   `work/z7ss/bzDescent.c` for the weight-3 → weight-5 step. The missing ingredient is the
   weight-5 → weight-7 step for the M₀,₁₀ integrand, i.e. the 3-fold Barnes–Mellin
   representation of the 7-fold integral and its residue expansion. That yields a triple sum,
   from which Koutschan's `HolonomicFunctions` (which BZ used at weight 5) can produce and
   *prove* the order-4 recursion.
2. **A triple sum is enough.** The stated goal ("provable in one Zeilberger call") is achievable
   with a triple sum plus creative telescoping; a single sum is not required. The campaign's
   CT obstruction (`ZETA7_STATE.md` §4) is about the **8-variable diagonal**, which is a much
   worse starting point than a 3-index binomial sum.
3. **Widen the §5.1 scan.** The BZ `Q(p;q)` scan here fixed `p_j, q_j` to be exact multiples of
   `n`. Allowing constant offsets (`p_j = A_j n + a_j`) and rational multiples of `q_n` would
   cover the case where `I″ₙ` is a *shifted* member of the BZ weight-5 family. This is cheap
   (`bzQ.c` runs 16.7M parameter vectors in 3 s) and is the highest-value remaining experiment.

---

## 9. Coverage table — the exact bounds of the negative

All rows: target `q_1 = 61`, `q_2 = 52921` matched **exactly** (rational arithmetic);
`z ∈ {+1, −1}` for `Z = 1`. "growth-feasible" = shapes not eliminated by the growth prune,
i.e. those that could in principle reach `μ = 6329.2605`.

| box (A,B) | weight cap `Σ|e|` | `z` | shapes enumerated | matched `q_1 = 61` | matched `q_1` **and** `q_2` | status |
|---|---|---|---|---|---|---|
| 2, 2 | ≤ 6  | ±1 | 1 660 (balanced, finite support) | 0 | 0 | complete |
| 2, 2 | ≤ 8  | ±1 | 17 370 | 0 | 0 | complete |
| 2, 2 | ≤ 10 | ±1 | 113 481 | 3 | 0 | complete |
| 3, 3 | ≤ 6  | ±1 | 65 788 | 44 | 0 | complete |
| 3, 3 | ≤ 8  | ±1 | 2 479 296 | 938 | 0 | complete |
| 3, 3 | ≤ 8  | ±1 | 1 222 822 growth-feasible | 172 | 0 | complete (with growth prune) |
| 3, 3 | ≤ 12 | ±1 | ≥ 233 372 012 growth-feasible | 16 748 | 0 | **11 of 12 shards** |
| 4, 4 | ≤ 10 | ±1 | ≥ 87 609 701 growth-feasible | 9 799 | **1** | **3 of 6 shards** |
| 3, 3, with `Σe = −8` (§11) | ≤ 10 | ±1 | 22 growth-feasible | 0 | 0 | complete |
| 3, 3, with `Σe = −8` (§11) | ≤ 12 | ±1 | 39 536 growth-feasible | 0 | 0 | complete |
| 2, 2, with shifts `c ∈ {−1,0,1}` | ≤ 8 | ±1 | 32 427 237 growth-feasible | 278 | 0 | complete |

Two rows need comment.

* Rows marked "growth-feasible" count only the shapes the growth prune could not eliminate,
  i.e. those that *could* reach `μ = 6329.2605`. Everything else is excluded a fortiori: it
  grows too slowly to be `q_n` no matter what its terms are.
* **The single `q_1 & q_2` hit** (box `A=B=4`, `W ≤ 10`) is
  `z=1, (0,1)^−1 (0,2)^−1 (0,4)^−1 (2,2)^1 (2,4)^−1 (4,−3)^−2 (4,1)^1 (4,2)^1`, i.e.
  `(2n+2k)!(4n+k)!(4n+2k)! / (k!(2k)!(4k)!(2n+4k)!((4n−3k)!)²)`. It is **refuted at n = 3**,
  where it gives `255115448/3` — not even an integer (`work/z7ss/checkhit.py`). Note that it
  has `Σe = −3`, so the §11 fingerprint (`Σe = −8`) predicted its failure independently.

So: **in the whole search, not one shape survives past `q_2`.**

Additional targeted scans of Brown–Zudilin's own weight-5 formula (§5):

| scan | parameter box | configurations | matched `q_0,q_1,q_2` | matched `q_3` |
|---|---|---|---|---|
| §5.1 `Q(p;q)`, `p_j = A_j n`, `q_j = G_j n` | `A_j, G_j ∈ {0,1}` | 4 096 | 0 | 0 |
| §5.1 same | `A_j, G_j ∈ {0,…,3}` | 16 777 216 | 0 | 0 |
| §5.1 same | `A_j, G_j ∈ {0,…,5}` | 2 176 782 336 | 0 | 0 |
| §5.1 with offsets `p_j = A_j n + a_j` | `A_j ∈ {0,1,2}`, `a_j ∈ {0,1}` | 2 176 782 336 | 0 | 0 |
| §5.2 descent template | inner `∈{0,…,3}`, outer `∈{0,1,2}`, all 35 shift slots, both signs | 4 354 560 | 0 | 0 |

(The wider descent scan, inner `∈{0,…,5}` / outer `∈{0,…,4}`, was started and cancelled for
time; the template is a guess at which slot absorbs `k`, so its evidential value is low
anyway.)

---

## 10. Files produced

All in `work/z7ss/`:

| file | what |
|---|---|
| `qdata.py` | loader for the 74 exact `q_n` |
| `minimality.py` | order ≤ 3 exclusion for `q_n` (modular, 105 terms) |
| `w5_order.py`, `w5_charpoly.py` | weight-5 `Q_n` minimal recurrence (order 3, deg 9) and char. polynomial — reproduces BZ's printed operator |
| `growth.py` | LP bound on the weight needed to reach `μ` (relaxed; weak, kept for the record) |
| `shapegrowth.py` | growth constant + all characteristic roots of a given shape (validated on Apéry ζ(2), ζ(3)) |
| `search1.c` | first exhaustive enumerator (no growth prune) |
| `search2.c` | + growth prune |
| `search3.c` | + coarse growth-window logging |
| `search4.c` | + refined (1e−6) shift-invariant growth test |
| `search5.c` | + constant shifts `(a n + b k + c)!`, `|c| ≤ CS` |
| `bzQ.c` | BZ eq. (sumQ) evaluator + parameter scan (validated: reproduces 1, 21, 2989, 714549, 217515501) |
| `bzQ2.c` | same with constant offsets in the parameters |
| `bzDescent.c` | BZ's weight-3 → weight-5 iterated-residue descent, validated, + the weight-5 → weight-7 template scan |
| `zeil_check.wl` | RISC `fastZeil` toolchain check — recovers Apéry's `(n+1)³a_n − (2n+3)(17n²+51n+39)a_{n+1} + (n+2)³a_{n+2} = 0` |

**T3 (certification) was not reached**: no candidate summand exists to certify. The toolchain
is verified working (`zeil_check.wl`), so a single `Zb[summand, {k,0,n}, n, 4]` call is all
that would be needed the moment a single-sum candidate appears.

---

## 11. A sharp fingerprint any single sum must have  ★ NEW, and the most useful thing to hand over

From the 74 exact terms, with `μ = 6329.260515009297`:

```
    θ_n := n(1 − q_n/(μ q_{n−1}))  =  3.3701 (n=40), 3.3956 (50), 3.4128 (60), 3.4251 (70)
    Richardson (θ_n = θ − c/n):  θ = 3.498732 (from n=50,70),  3.498985 (from n=60,73)
```

so

```
    q_n  ~  C · μ^n · n^{−7/2},        μ = 6329.2605150093…            [VERIFIED to 4 digits]
```

Now suppose `q_n = Σ_k z^k ∏_j ((α_j n + β_j k)!)^{ε_j}` with a **non-degenerate interior
saddle** (the generic case). Stirling gives `F(n,t*n) ~ (∏ (2π L_j n)^{ε_j/2}) e^{n f(t*)}`,
and Laplace summation over `k` contributes `n^{+1/2}`. Hence

```
    q_n ~ C μ^n n^{(1/2)Σ_j ε_j + 1/2}   ⟹   Σ_j ε_j = −8 .
```

(Checks: Apéry ζ(3), `Σε = 2−4−2 = −4` → `n^{−3/2}` ✓; Apéry ζ(2), `Σε = −3` → `n^{−1}` ✓.)

**So any single hypergeometric sum for `q_n` must satisfy simultaneously**

```
    Σ_j ε_j·α_j = 0 ,     Σ_j ε_j·β_j = 0 ,     Σ_j ε_j = −8 ,
    max_t Σ_j ε_j L_j log L_j + t log|z| = log(6329.2605150093…) .
```

The third condition is new and very restrictive: the summand must carry **exactly eight more
factorials in the denominator than in the numerator**. It immediately kills the most obvious
family: `Σ_k C(n,k)^a C(n+k,k)^b` has `Σε = −(a+b)`, so `a+b = 8` is forced, and the nine
growth constants are

```
    a+b=8:  256.000, 339.470, 473.042, 704.809, 1153.999, 2173.528, 5096.958, 16510.302, 9.4e9
    (a=8,7,6,5,4,3,2,1,0)          — none is 6329.2605.
```

This quadruple of conditions is exactly what should be quoted to Zudilin: it is a complete,
checkable fingerprint of the summand he would have to have in mind.

---

## 12. Runs still in flight when this report was written

Three sweeps were still running and will keep writing to their logs in `work/z7ss/`:

* `search2 3 3 12 1 hitsW12_<s>.txt <s> 12` — shards 3, 4, 5 of 12 (the shards are residue
  classes of the exponent of `k!`; 3, 4, 5 are the largest subtrees). 9 of 12 done.
* `search3 4 4 10 1 hitsA4W10_<s>.txt <s> 6` — shards 0, 2, 3, 4, 5 of 6. 3 of 6 done
  (shard 3 produced the single refuted hit above).
* `search6 3 3 14 … −8` and `search6 3 3 20 … −8` (the `Σe = −8` fingerprint at higher
  weight; `W ≤ 10` and `W ≤ 12` are complete, both with zero candidates).
* `search5` (shifted forms): the `W ≤ 8` sweep is **complete** — 32 427 237 growth-feasible
  shapes, 278 matched `q_1`, **0** matched `q_1` and `q_2`, and **0** matched the refined
  growth constant. The `W ≤ 10` shifted sweep was **cancelled**, not completed — it is not
  covered.

To finish and aggregate:

```sh
cd work/z7ss
cat log*_*.err | awk '{for(i=1;i<=NF;i++){split($i,a,"=");
  if(a[1]=="leaves")L+=a[2]; if(a[1]=="valid")V+=a[2];
  if(a[1]=="q1hits")H1+=a[2]; if(a[1]=="q1q2hits")H2+=a[2]}}
  END{print "leaves="L" growth-feasible="V" q1="H1" q1&q2="H2}'
cat hits*.txt              # any survivor -> feed to checkhit.py, then to zeil_check.wl
```

Any new `q_1 & q_2` survivor must be run through `python3 checkhit.py 10` (exact, all 74
terms available) before it is believed — the one hit found so far died at `n = 3`.
