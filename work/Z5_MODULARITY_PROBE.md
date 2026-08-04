# Z5_MODULARITY_PROBE — the Brown–Zudilin ζ(5) family has an integral mirror map

**Author:** Fable fork, 2026-08-04.  Script `work/z5eps/eps50_z5_nome.py`
(reuses the eps48 nome instrument; exact `Fraction` arithmetic throughout).
Labels per programme convention.

## 1. The operator and its exponent structure `[PROVED, exact]`

The 4-term certified recurrence `L_BZ` (coefficients `c0..c3`,
`work/lb5/core.py`) gives for `U(t) = Σ Y_n t^n` the operator
`L = Σ_{j=0}^3 t^j P_j(θ)` with `P_j(x) = c_{3−j}(x−(3−j))`, checked
against the exact `Q`-ladder (`Σ_j P_j(N−j)Q_{N−j} = 0`, `N ≤ 28`).

Indicial polynomial at `t = 0`:

> `P0(x) = 2·x⁵·(2x−1)·a0(x−3)` ,  `a0(z) = 41218z³+198849z²+320790z+173057`.

So the ODE has order 9 with local exponents: **0 with multiplicity 5**, one
exponent `1/2`, and the three irrational (one real, two complex) roots of
`a0(x−3)`.  The family is *not* MUM as an order-9 operator; the intrinsic
object is the **5-dimensional unipotent block** at `t = 0` — the
Frobenius-structure signature of a weight-4 variation of Hodge type
`(1,1,1,1,1)`, i.e. Calabi–Yau-fourfold/`Sym⁴`-like, matching the family's
weight-5 period content.  The remaining exponents come from the apparent
inflation of the recurrence-to-ODE conversion (degree-9 coefficients).

## 2. HEADLINE — the mirror map is integral with no rescaling
`[VERIFIED exact ℚ, to q²⁶]`

With `y0 = Q(t) = 1 + 21t + 2989t² + …`, `y1 = y0·log t + g`
(`g` the unique log-partner, existence from `P0(N) ≠ 0` for `N ≥ 1`), and
nome `q = t·exp(g/y0)`:

> **`t(q) ∈ ℤ[[q]]` and `F(q) := y0(t(q)) ∈ ℤ[[q]]`, at scale λ = 1:**
>
> `t(q) = q − 94q² − 591q³ − 454656q⁴ − 104464532q⁵ − 28719179392q⁶ − …`
> `F(q) = 1 + 21q + 1015q² + 140206q³ + 29342713q⁴ + 7466148732q⁵ + …`

Every coefficient through order 26 is an integer; the 2- and 3-adic
denominator profiles are identically zero.  For comparison, generic
recurrences fail this immediately and the sporadic *modular* families pass
it — this is the Golyshev/Mishchenko-style arithmeticity signal, here for a
5-block.  **The ζ(5) cellular family passes the mirror-map integrality test
outright.**

Interpretation (conjectural, stated as such): the BZ family sits in the
Calabi–Yau / mirror-symmetric world — an arithmetic degeneration with an
integral mirror map — rather than the elliptic-modular world of the
weight-2/3 sporadics.  This is consonant with the programme's measured
Frobenius spike `diag(1, p³, p⁵)` (crystalline grading of the same
structure) and gives the "modular-form connection" of the ζ(5) story its
correct home: not an eta-quotient, but a CY-type mirror map whose
arithmetic (integrality, Dwork congruences, unit roots) is the right
replacement toolkit.

## 3. Root integrality `[VERIFIED exact, to t²⁶]`

* `Q(4t)^{1/2} ∈ ℤ[[t]]` — denominators of `Q^{1/2}` are exactly powers of
  2 with `v₂ ≤ 2k`;
* `Q(8t)^{1/4} ∈ ℤ[[t]]` — denominators powers of 2 with `v₂ ≤ 3k`.

All denominators of both root series are pure powers of 2 (no odd primes
to order 26) — a Dwork-type 2-adic phenomenon.  NOTE this is a *series*
statement, not an operator `Sym²`/`Sym⁴` identification; whether the
5-block is `Sym⁴` of an order-2 operator is a separate, operator-level
question, `[OPEN]` (the natural test — existence of rational `p, r` with
`Sym⁴(D²+pD+r)` matching the 5-block after desingularisation — was not
run; the block must first be split off the order-9 operator).

## 4. Identification status `[OPEN]`

`t(q)` and `F(q)` are integral but unidentified: they are not expected to
be eta quotients (wrong weight structure), and no offline table of CY
mirror maps is available in this environment.  Concrete next steps:

1. split the 5-block off the order-9 operator (right factorisation over
   `ℚ(t)`), obtaining the intrinsic order-5 operator; test MUM and compute
   its Yukawa-type invariants / instanton-type numbers from `y2` (the
   log² solution) — their integrality after standard normalisation is the
   next-level signal;
2. compare against the Almkvist–van Enckevort–van Straten–Zudilin tables
   of CY operators (order 5 / `Sym⁴` families) — requires the tables;
3. p-adically: test the Dwork congruence `F(q)/F(q^p) ≡` (unit-root
   ratio) mod p for p = 5, 7 against the programme's crystal data — this
   connects the mirror map directly to the sharp-denominator story.

## 5. Relation to the campaign

The curve-blindness theorem says tangential deformations cannot see the
weight-5 row; the modular probe now says the weight-5 row lives in an
arithmetic 5-block with an integral mirror map.  Together: the missing
"instrument that can see weight five" should be built from the 5-block's
own coordinates (`q`, `t(q)`, the Frobenius basis `y0..y4`) rather than
from binomial letters — the ζ(5) analogue of what the Γ₀(9) identification
did for the sporadic family ζ.  The natural conjecture, recorded for the
programme:

> **Conjecture (mirror form of the bridge).**  In the `q`-coordinate of
> the 5-block, the companion rows `P̂_n, P_n` are the coefficient
> sequences of explicit `q`-side objects (Eichler-type integrals of the
> block's structure series), and the compact weight identity (BRIDGE) is
> the `t`-coordinate shadow of a `q`-side identity between them.

Falsifier: if the split-off 5-block fails MUM or its Yukawa-type series
fails integrality at every rescaling, the CY reading collapses to a bare
integrality curiosity.

---

# Part 2 — depth probe (eps53): Yukawa integrality, no low-degree splitting, and the calibrated q-side instrument

**Script:** `work/z5eps/eps53_z5_deep.py` (sections dwork/qside/factor).
All exact; series order 32 (factor search: order 64).

## 6. The q-side instrument is calibrated on Apéry ζ(3) `[VERIFIED exact, q³²]`

Running the row-avatar pipeline (nome, then `θ_q³(B/A∘t(q))`) on the γ
(Apéry ζ(3)) control yields an integer series which is **identified
exactly**:

> `θ_q³(B/A)(q) = 6·E^{(1)} − 168·E^{(2)} + 378·E^{(3)} − 216·E^{(6)}`,
> `E^{(d)} = Σ_n σ₃(n) q^{dn}`,

verified coefficientwise to `q³²` — the classical Beukers weight-4
Eisenstein form on `Γ₀(6)`, rediscovered from the recurrence alone.  The
pipeline is therefore trustworthy for q-side row avatars.

## 7. BZ ζ(5): second arithmeticity signal — the Yukawa-type series is integral
`[VERIFIED exact, q³²]`

In the block's q-normal form (`ĝ₁ ≡ 0` verified — the mirror-map
normalization is exact), the Yukawa-type invariant

> `K(q) := θ_q²(ĝ₂/F)(q) = 87·q + 33895·q² + 13385796·q³ + 5474328935·q⁴ + …`

is **integer at scale λ = 1** through `q³²`.  (Note `K₁ = 87 = 4·P₁` — the
P-ladder appears in the block's normal form at the first coefficient.)
Together with the integral mirror map (Part 1) this is the two-signal
CY-arithmeticity pattern.

## 8. Negatives, honestly labelled

* **Naive Dwork fails**: `F(q) ≡ F_{<p}(q)·F(q^p) (mod p)` fails at `q^p`
  for `p = 5, 7`.  The 5-block has three Frobenius slopes
  (`diag(1,p³,p⁵)` in the programme's crystal data); the congruence needs
  its slope-refined form.  `[EXCLUDED in the naive form]`
* **Naive mirror-bridge fails**: `θ_q³(P̂/Q∘t(q))` and
  `θ_q⁵(P/Q∘t(q))` have unboundedly growing denominators — the ζ(3)-style
  Eichler shape does not transfer verbatim; the correct q-side avatars of
  the rows must involve the block's normal-form data (`K(q)` and the
  higher structure series), not bare `θ` powers.  `[EXCLUDED in the naive
  form; the calibrated instrument makes this a sharp negative]`
* **No low-degree splitting**: the order-9 operator admits **no order-5
  right factor of t-degree ≤ 20** annihilating the unipotent block
  (mod-p linear solves, full rank at every degree, series order 64).
  Either the factor has very high apparent-singularity degree or —
  more likely — the global monodromy entangles the block with the
  parasitic exponents and the block is a *local*, not global, direct
  summand.  The block's arithmetic (integral `t(q)`, `F(q)`, `K(q)`)
  is a local statement and stands regardless.  `[EXCLUDED for
  t-degree ≤ 20, one 22-bit prime]`

## 9. Updated reading

The ζ(5) family passes both CY-arithmeticity tests (mirror map, Yukawa)
in its local 5-block, while resisting global factorization and the naive
transfer of the elliptic-modular (ζ(3)) formulas.  The mirror form of the
bridge should therefore be sought in the block's normal-form coordinates:
express the rows through `F, K` and the two remaining structure series
(from `ĝ₃, ĝ₄`), where the ζ(3) control says the correct normalization
will make the avatars integral.  Concrete next computations: the full
normal-form tower `ĝ₃, ĝ₄` and its structure series; the slope-refined
Dwork test against the crystal ladders.

---

**Correction (2026-08-05):** the root-integrality items of §3 are *universal*
for integer series — for any `f ∈ 1 + tℤ[[t]]`, `√(f(4t)) ∈ ℤ[[t]]` and
`f(8t)^{1/4} ∈ ℤ[[t]]` (see `papers_out/half_apery`, Lemma; e.g.
`4^k·binom(1/2,k) = ±2·Catalan_{k−1}`).  They are **not** arithmeticity
evidence and are withdrawn from that list; the integral mirror map (§2) and
the integral Yukawa datum (§7) remain the genuine signals.
