# DELTA_MODULAR_THEOREM — the δ parametrization at theorem grade

**Fork deliverable, 2026-08-04.**  Script: `work/z5eps/eps55_delta_theorem.py`
(exact ℚ series arithmetic throughout, depth `q^139`).  Companion data:
`work/SPORADIC_MODULAR_DICTIONARY.md` (eps51 identification),
`work/MODULAR_COACTION_PROBE.md` Part D (eps52 Eichler companion).

## 0. Statement

Let `A(n)` be the δ-sequence, defined by the Almkvist–Zudilin recurrence
R3(7,3,81,0):

> `(n+1)³u_{n+1} = (2n+1)(7n²+7n+3)u_n − 81n³u_{n−1}`, `A(0)=1`,

equivalently annihilated by `L = θ³ − t(2θ+1)(7θ²+7θ+3) + 81t²(θ+1)³` as a
generating series `y₀(t) = Σ A(n)tⁿ`.  Define the eta quotients (level 12)

> `t(q) = q·∏(1−q^m)⁴(1−q^{4m})⁴(1−q^{6m})¹⁶ / [(1−q^{2m})¹⁶(1−q^{3m})⁴(1−q^{12m})⁴]`
> `F(q) = ∏(1−q^{2m})¹²(1−q^{3m})(1−q^{12m}) / [(1−q^m)³(1−q^{4m})³(1−q^{6m})⁴]`.

**Theorem (modulo hypothesis (H) below).**  `F(q) = y₀(t(q))`; i.e. δ is
modular-parametrized by the weight-2 form `F` over the uniformizer `t` —
the first modular parametrization theorem for a no-limit sporadic family.

## 1. What is proved unconditionally (exact computations, `eps55`)

| step | statement | status |
|---|---|---|
| A | Ligozat conditions for both quotients: `Σδr_δ ≡ 0 (24)`, `Σ(12/δ)r_δ ≡ 0 (24)`; weights (0, 2); character products `6561 = 81²`, `16/9 = (4/3)²` — both rational squares ⇒ trivial characters | **exact integer checks, PASS** |
| B1 | the recurrence nome (Frobenius `y₁ = y₀ log t + g` via dual numbers, `q = t·exp(g/y₀)`, exact series reversion) equals the eta quotient `t(q)` | **exact ℚ to `q^139`** |
| B2 | `y₀(t(q))` equals the eta quotient `F(q)` | **exact ℚ to `q^139`** |
| C1 | among all order-≤3 operators `Σ_{j≤3} C_j(t)θ_t^j` with `deg C_j ≤ 2`, the annihilator space of the eta-side `F` (with `θ_t = (t/θ_q t)·θ_q` computed purely on eta series) is **exactly one-dimensional** (12 unknowns, rank 11, 120 equations) | **exact ℚ** |
| C2/C3 | that one-dimensional space is spanned by **exactly the recurrence operator `L`** (coefficientwise equality after normalization; annihilation checked to `q^139`) | **exact ℚ** |

Step B is a fully independent re-derivation of the eps51 identification with
a 5× deeper margin.  Step C is the load-bearing new content: **the modular
side satisfies the δ recurrence's ODE, uniquely within its degree class.**

## 2. The proof architecture, and hypothesis (H)

The theorem follows from the unconditional steps plus two classical inputs
and one hypothesis:

1. *(citable)* **Ligozat/Newman modularity**: an eta quotient satisfying the
   §1-A conditions is a meromorphic modular form of the stated weight on
   `Γ₀(12)` with the stated (here trivial) character.  [Ligozat 1975; Ono,
   *Web of modularity*, Thm 1.64.]
2. *(citable, classical)* a weight-`k` meromorphic modular form, expressed
   as a function of a degree-one modular function (hauptmodul) `t`,
   satisfies a linear ODE of order `k+1` in `t` with **rational** function
   coefficients, whose singularities are confined to the images of cusps
   and elliptic points.  [Stiller; Zagier, *1-2-3 of Modular Forms*,
   Prop. 21 and §5.4.]
3. **(H)** `t` is a hauptmodul (degree one) for the group `G` it uniformizes
   — `G ⊇ Γ₀(12)`, plausibly an Atkin–Lehner extension.

Given 1–3: `F` satisfies *some* order-3 rational ODE over `ℚ(t)` with
bounded coefficient degrees; the bound places it inside the `deg ≤ 2`
ansatz of step C1 (four singular fibres: `t = 0, ∞` and the two roots of
`1−14t−81t²`, matching `L`'s exact singular locus); C1's one-dimensionality
forces it to be `L`; hence `F∘` and `y₀` satisfy the same operator with the
same three initial coefficients (checked), so they are equal.

**Why (H) is stated as a hypothesis and not glossed.**  A direct
Ligozat cusp-order computation on `Γ₀(12)` (six cusps, widths included)
gives `t` orders `(−1, −2, +1, …)`-type at the cusps over `d = 1, 2, 12`,
i.e. polar degree `> 1` *on `Γ₀(12)` itself* — so `t` is a hauptmodul only
on a larger group (an Atkin–Lehner quotient identifying the polar cusps)
or the count needs the widths of an intermediate curve.  Determining `G`
exactly (finite: test `t∘w_d = t` for the Atkin–Lehner involutions
`w₃, w₄, w₁₂`, a finite q-expansion check once `w_d`-expansions are set up)
is the **single remaining step** to make the theorem unconditional; the
`1−14t−81t²` singular structure and the C1 uniqueness make any outcome
other than "(H) holds for the correct `G`" essentially impossible, but we
do not claim it.

## 3. Consequences (conditional on the theorem)

* δ's Eichler companion (eps52) `B(n) = [tⁿ]F·θ_q^{−3}(tσ³/(P·F))` becomes
  a **theorem-grade** formula once (H) closes (its only unproved input is
  the parametrization).
* δ's "no archimedean limit" is reinterpreted: the natural limit object is
  the Eichler/L-value datum of a level-12 weight-2 form.  [OPEN to compute.]
* First proved-grade modular statement for any no-limit sporadic family.

## 4. The discriminating experiment (task 2 of this fork; `eps54_domb.py`)

Jet-reachability scan (eps43 protocol: linear + quadratic curve atoms,
per-ζ-graded pinning, targets ε³ and ε², **both primes 4194301/4194247,
identical ranks**):

| family | char | limit | harmonic companion? | level | jet verdict |
|---|---|---|---|---|---|
| α (Domb) | 1 | 7ζ(3)/24 | yes (14 terms) | 12 | **b forced 0 — UNREACHABLE** |
| ε | 1 | 7ζ(3)/32 | yes (10 terms) | 8 | **b forced 0 — UNREACHABLE** |

Both discriminating families are principal-character with real limits *and
possess harmonic companion formulas* — yet the jet mechanism cannot reach
them.  **The character+limit hypothesis for the reachability dichotomy is
refuted; the squarefree-level hypothesis survives** (reachable: Franel
level 6, D level 5 — squarefree; unreachable: ε 8, ζ 9, δ 12, α 12, B 36 —
all non-squarefree).  Corollary worth stating: jet-reachability is
*strictly finer* than harmonic-formula existence — α and ε have formulas
but no jet route to them; the governing invariant is the arithmetic of the
modular level, i.e. of the uniformization, exactly as the modular-anchor
picture predicts.

## 5. Honest limits

* (H) is the one open input to the δ theorem; everything else is exact
  with `q^139` margin or a named citation.
* The eps54 negatives are two-prime modular linear algebra over
  `n ≤ 28`, atom boxes as in eps43; same epistemic grade as the
  eps43 dichotomy rows they extend.
* Nothing here upgrades the eps52 companion formulas' verification ranges.
