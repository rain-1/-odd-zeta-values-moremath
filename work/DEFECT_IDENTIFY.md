# The purity defect identified: c = −1/(2ζ(2)) = −3/π²

Task P2, session 2026-07-24 (agent). Incremental log; headline first.

---

## 0. HEADLINE — [PROVED]

    c  =  −1/(2ζ(2))  =  −3/π²  =  −0.30396355092701331433163838962918291671307632401674…

The "purity defect" of the Brown–Zudilin ζ(5) family is **not a new constant**.
It is the reciprocal period −3/π², and the minimal-ray class it defines is,
up to the factor 4ζ(2), **the cellular integral itself**:

    M_n  :=  Î_n − c·I′_n  =  I_n / (4ζ(2)).

### Proof

Brown–Zudilin (llm/20, eq. (I_n) and again at line 540) prove, for the whole
admissible 8-parameter family:

    I(a·n)  =  2 I′(a·n)  +  4 ζ(2) I″(a·n),
      I′ = Qζ(5) − P,   I″ = Î = Qζ(3) − P̂.

Their Remark 2 / (3-asymp) gives the three asymptotic rays as the roots of the
characteristic polynomial, with

    lim log|I_n|/n  = log|λ₁| = −5.29756…      (λ₁ = 0.00500378…)
    lim log|I′_n|/n = lim log|Î_n|/n = log|λ₂| = −2.47237…   (λ₂ = −0.0843843…)
    lim log|Q_n|/n  = log|λ₃| = +6.38364…      (λ₃ = 592.07938…)

Let V₁ = { solutions u of the order-3 recurrence with limsup log|u_n|/n ≤ log|λ₁| };
dim V₁ = 1 (the minimal ray), and I ∈ V₁ while I′, Î ∉ V₁.

Rewrite BZ's identity as

    I_n  =  4ζ(2) · ( Î_n  +  I′_n /(2ζ(2)) )  ∈ V₁.

So Î + I′/(2ζ(2)) ∈ V₁ already. If also Î − c I′ ∈ V₁, subtracting gives
(c + 1/(2ζ(2))) I′ ∈ V₁; since I′ ∉ V₁ this forces

    c = −1/(2ζ(2)) = −3/π².     ∎

The limit form c = lim Î_n/I′_n follows: Î_n − cI′_n = O(λ₁ⁿ · poly n) while
I′_n ≍ λ₂ⁿ and |λ₁| < |λ₂|.

### Numerical certificate [VERIFIED]

From the exact ladders (falsify_data/ladder_{Q,P,Ph}.json, n ≤ 360), at
mp.dps = 2600, with c* := −3/π² taken exactly:

| n | −log₁₀ \|Î_n/I′_n − c*\| |
|---|---|
| 50 | 61.367 |
| 100 | 122.713 |
| 150 | 184.060 |
| 200 | 245.408 |
| 250 | 306.756 |
| 300 | 368.104 |
| 340 | 417.183 |
| 360 | **441.722** |

Agreement grows linearly at slope **1.22701 digits/n**, and
log₁₀(λ₂/λ₁) = log₁₀(16.8641) = **1.22701** — the convergence rate is exactly
the predicted (λ₁/λ₂)ⁿ. This is not a numerical coincidence at 441 digits; it
is the theorem's own error term.

Third-ray check with c* exact: log|M_n|/n = −5.4161 (n=100), −5.3654 (200),
−5.3462 (300), −5.3393 (360) → log|λ₁| = −5.29756 (from below, standard
n^α correction). And I_n = 4ζ(2)·M_n verified to full working precision
(rel. diff ~1e−2160 at n = 360).

### Why 600-digit PSLQ missed it

The prior exclusions were all *correct*; the basis was simply missing the
inverse period. c has **weight −2**. PSLQ over a ℚ-basis of periods can never
see a reciprocal period: 1/ζ(2) is not in the ℚ-span of {1, ζ(2), ζ(3),
ζ(2)², ζ(5), ζ(2)ζ(3)} nor of the weight-0 ratios tested
{1, ζ₃/ζ₅, ζ₂ζ₃/ζ₅, ζ₂²/ζ₅, ζ₇/(ζ₂ζ₅)}. The one test that would have found
it — `pslq([c*zeta(2), 1])` — was not run.
**Methodological lesson for the program: always adjoin 1/ζ(2) = 6/π² (and
generally π^{−2k}) to any weight-0 PSLQ basis.**

### Interpretation

The defect is exactly the ζ(2)-coefficient in BZ's own decomposition. The
graded picture from ORCHESTRATOR_NOTES §2d is completed:

| ray | eigenvalue | class | period |
|---|---|---|---|
| top (λ₃) | growth 592.08ⁿ | Q_n | ℚ(0) |
| middle (λ₂) | 0.08438ⁿ | I′, Î (span) | ζ(5) and ζ(3) separately |
| minimal (λ₁) | 0.005004ⁿ | I = 2I′ + 4ζ(2)Î | 2ζ(5) + 4ζ(2)ζ(3) |

The class exiled from the minimal ray is exiled *by ζ(2)*. This is the same
object flagged in ORCHESTRATOR_NOTES §2c(iii): BZ's top period is
ζ(5) + 2ζ(2)ζ(3), **depth 2**, and its impurity is what blocks the
weight-5 harmonic-monomial decomposition of P_n. The "rotation" c is the
ζ(2)-twist, nothing more. There is no exotic new period here.

### Consequence for T4 (the cone) — [PROVED, no computation needed]

BZ line 540 states I(a) = 2I′(a) + 4I″(a)ζ(2) for the entire admissible
8-parameter family (under (cond12), (cons1)), and Remark 2 states
|λ₁(a)| < |λ₂(a)| is checkable at each admissible a. The proof above uses
**only** these two facts. Therefore

    c(a) = −1/(2ζ(2)) = −3/π²  for every admissible cone point a.

**c is constant on the cone.** It carries no information about a. No further
cone-point computation is warranted; the T4 budget is better spent on the
connection constants below, which *do* vary with a.

---

## 0b. The right way to say it: c is a Tate class ℚ(1)

    c  =  12 / (2πi)²        [VERIFIED exact: 12/(2πi)² = −3/π²]

because 4ζ(2) = −(2πi)²/6, so c = −1/(2ζ(2)) = 12·(2πi)^{−2}.

This is exactly the shape [BV] Cor. 31 predicts for connection constants of a
Picard–Fuchs operator: **periods with 2πi inverted**. c is a *rational multiple
of a negative Tate twist* — weight −2, depth 0, the most degenerate possible
answer. It carries no motivic information beyond the Tate line. The search for
an exotic period was searching for something that was never there.

---

# T1 — Literature framework verdict

Full extraction in `work/DEFECT_LIT.md` (agent, PDFs fetched). Summary and my
corrections:

## Right papers — three of four candidates confirmed, with one title wrong

| candidate | status |
|---|---|
| Golyshev–Zagier, *Proof of the gamma conjecture for Fano 3-folds of Picard rank one*, Izv. Math. **80** (2016) 24–49 | [VERIFIED] exists; **no arXiv**; author PDF at MPIM. = **[GZ1]** |
| Bloch–Vlasenko, "Motivic Gamma functions" | **TITLE WRONG.** Actual: ***Gamma functions, monodromy and Frobenius constants***, arXiv:**1908.07501**, CNTP 15 (2021) 91–147. = **[BV]** |
| Golyshev, *Deresonating a Tate period*, arXiv:**0908.1458** | [VERIFIED] exists — **but it is about *Apéry* constants (lim bₙ/aₙ = c·L(s₀)), a DIFFERENT invariant.** Do not conflate with Frobenius constants. |
| "anything citing them on Apéry-like operators" | **[GZ2]** Golyshev–Zagier, *Interpolated Apéry numbers, quasiperiods of modular forms, and motivic gamma functions*, PSPM 103.2 (2021) 281–301 — has the largest table. Plus Roy–Vlasenko arXiv:2206.15181 and Kerr arXiv:2008.03618. |

## Right definition (the computational recipe)

**[BV] Def. 22**, at a **conifold** (not at ∞): deform the Frobenius solution
Φ(s,t) = Σ aₙ(s) t^{n+s}; set φ_{ρ,k} = (1/k!)∂ᵏ_s Φ|_{s=ρ}; continue along a
path 0 → c; then (σ_c − 1)φ_{ρ,n}(t) = κ_{ρ,n}·δ(t), where δ spans the rank-1
image of σ_c − 1. **Normalisation: κ₀ = 1 only. No 2πi, no Γ-factor.**

**[GZ1] (0.3)**, at ∞ of the Borel transform: κⱼ := lim_{z→∞} Ψⱼ(z)/Ψ(z);
these carry Euler γ, and Γ(1+ε)^{−1}·Σκⱼεʲ is the *normalised gamma class*.

**Bridge (agent-verified numerically):** with Λ(ε) = lim Aₙ(ε)/Aₙ(0) from the
ε-deformed recurrence n → n+ε, both equal **κ(ε) = c^ε·Λ(ε)**, c = reciprocal
growth rate. Hypergeometric closed form κ(s) = 1/A(s), A(s) = ∏Γ(s+αⱼ)/∏Γ(s+βⱼ)
([BV] Prop. 26).

## Known values — my prior CONFIRMED, guessed normalisation REFUTED

**[BV] Example 29** for L = D³ − t(34D³+51D²+27D+5) + t²(D+1)³ (the Apéry ζ(3)
operator), path 0 → conifold c = 17 − 12√2:

    κ₀ = 1,  κ₁ = 0,  κ₂ = −π²/3 = −2ζ(2),  κ₃ = (17/6)ζ(3)

So the Apéry ζ(3) Frobenius constant **is** a rational multiple of ζ(3) —
but **(17/6)ζ(3)**, not ζ(3)/(2πi)³. The guessed normalisation was wrong.
Cross-confirmed by Kerr Ex. 9.8 and [GZ2] (47).

### Two errata the agent found in [BV] — and my correction to the agent

The agent reported [BV] Ex. 29's κ₅ = (7/5)ζ(5) − (17/3)ζ(2)ζ(3) as erroneous
with "correct is (7/3)ζ(5)". **That summary is itself garbled.** I checked
numerically at 30 dps against the agent's own value κ₅ = −8.785226558:

    (7/3)ζ(5) − (17/3)ζ(2)ζ(3) = −8.78522655635015   ← MATCHES
    (7/5)ζ(5) − (17/3)ζ(2)ζ(3) = −9.75302579448396
    (7/3)ζ(5)                  = +2.41949809533453

**The erratum is the ζ(5) coefficient only, 7/5 → 7/3. The −(17/3)ζ(2)ζ(3)
term stands.** So κ₅ = (7/3)ζ(5) − (17/3)ζ(2)ζ(3). [VERIFIED by me, 15 digits.]

The second reported erratum ([BV] Ex. 28, κ₆ sign: −(5/2)ζ(3)² should be
+(5/2)ζ(3)²) I did **not** independently check. [RECALLED-UNVERIFIED by me;
agent claims numerical verification.]

### A structural lead this exposes

    κ₅ (Apéry ζ(3) operator) = (7/3)·[ ζ(5) − (17/7)·ζ(2)ζ(3) ]
    BZ top period             =   2  ·[ ζ(5) +  2    ·ζ(2)ζ(3) ]

Both live in the **same 2-dimensional weight-5 depth-2 space
⟨ζ(5), ζ(2)ζ(3)⟩**, differing only in the rational ratio (−17/7 vs +2).
This is the space that ORCHESTRATOR_NOTES §2c(iii) identified as blocking the
weight-5 harmonic-monomial decomposition of P_n. Worth pursuing: is BZ's
ζ(5)+2ζ(2)ζ(3) the κ₅ of *some* operator in the [GZ2] family, i.e. is the
BZ family a gamma-class deformation of a known Fano/CY operator?

### Higher weight (T1 part E)

- ζ(5) appears only as a **higher** Frobenius constant of the order-3 Apéry
  ζ(3) operator (κ₅ above), then ζ(7), ζ(3)ζ(5), ζ(9), ζ(5)², ζ(11), and
  ζ(3,5,3) at κ₁₁ ([GZ2] eq. (47)). [BV] flag these j > 3 constants as
  **not geometric** — "surprising that they are periods".
- [GZ2] §7 conjectures the ε=1 expansion (κ_{1,0} = ζ(3)/6 = Apéry's own
  limit; κ_{1,2} = −(1/18)π²ζ(3) + (11/3)ζ(5); κ_{1,5} ∋ −4ζ(3,5)) equals the
  normalised gamma class of OG(5,10).
- **[UNVERIFIED/OPEN]:** the agent found **no operator in the literature whose
  first non-trivial Frobenius constant is a rational multiple of ζ(5)** — the
  true ζ(5)-analogue of κ₃ = (17/6)ζ(3). That slot appears to be open, and the
  BZ operator is a natural candidate to fill it.
- Lead not read: **Beukers–Vlasenko, *Frobenius structure and p-adic zeta
  values*, arXiv:2302.09603** (Adv. Math. 2025) — p-adic Frobenius matrix at a
  MUM point with entries in the ℚ-span of ζ_p(k). **This is directly relevant
  to the open (DWORK) gate** and should be fetched next.

### Verdict on the framework

Right framework, **wrong instrument for this particular question**. The
BV/GZ κ's are the Taylor coefficients of an ε-deformation at a *conifold*.
Our c is not one of them: it is a ratio of leading asymptotic (Stokes)
constants on two *different* rays. Golyshev's *Apéry constant* is the closer
analogue, and the correct verdict is that **c is the Apéry constant of the
second ray** — and it is Tate.

---

# T2 — The BZ differential operator and its connection constants

## The exact recurrence [VERIFIED exactly on all three ladders]

From BZ (llm/20, the display before "characteristic polynomial"), for n ≥ 2:

    A(n)u_{n+1} + B(n)u_n + C(n)u_{n−1} + D(n)u_{n−2} = 0
    A(n) = 2(2n+1)(41218n³ − 48459n² + 20010n − 2871)(n+1)⁵
    B(n) = −(97604224n⁹ + 178061760n⁸ + 72005308n⁷ − 48634688n⁶ − 39076836n⁵
             + 2622730n⁴ + 7581006n³ + 920112n² − 543402n − 120582)
    C(n) = −2n(3874492n⁸ − 2617900n⁷ − 3144314n⁶ + 2947148n⁵ + 647130n⁴
             − 1182926n³ + 115771n² + 170716n − 44541)
    D(n) = n(41218n³ + 75195n² + 46746n + 9898)(n−1)⁵

Residual is **exactly 0** for u ∈ {Q, P, P̂} at every n = 2..359 (1074 exact
rational checks, `rec_check.py`). Ladder anchors match BZ's printed values
(Q = 1, 21, 2989; P = 0, 87/4, 1190161/384; P̂ = 0, 101/4, 344923/96). Also
holds at n = 1 for Q and P̂ but **not** for P (residual 8479793) — P carries an
inhomogeneity at n = 1.

## The operator [VERIFIED, exact symbolic, sympy]

With θ = z d/dz and Y(z) = Σ uₙzⁿ, the recurrence transports to

    L = A(θ−1) + z·B(θ) + z²·C(θ+1) + z³·D(θ+2)

**order 9 in θ, degree 3 in z.**

**Leading symbol (θ⁹ coefficient):**

    41218·(z³ − 188z² − 2368z + 4)

— exactly the reciprocal of the characteristic polynomial 4λ³−2368λ²−188λ+1.
So the finite nonzero singularities are precisely z_i = 1/λ_i:

    z₃ = 1/λ₃ = 0.00168896271830487…   (nearest to 0; Q's radius of convergence)
    z₂ = 1/λ₂ = −11.850538…
    z₁ = 1/λ₁ = 199.848883…

**Indicial polynomial at z = 0** (the z⁰ part of L):

    2·θ⁵·(2θ − 1)·(41218θ³ − 172113θ² + 240582θ − 112558)

    ⇒ exponents:  θ = 0 with MULTIPLICITY 5;  θ = 1/2;  three roots of an
      irreducible cubic.

**z = 0 is not MUM for the order-9 operator** (that would need multiplicity 9),
but it carries a **rank-5 maximally-unipotent sub-block** — log-depth up to
log⁴z. The multiplicity is **5 = the weight**. This is the ODE-side shadow of
ORCHESTRATOR_NOTES §2d's "congruence depth = motivic weight", and it is why
§2d's remark that "weight 5 exceeds the order-3 local log-depth (max 2)" was
based on the wrong operator: the *recurrence* is order 3, but the *operator*
has a rank-5 unipotent block, exactly enough room for weight 5.

The z³ part of L is (θ+1)⁵(θ+2)(41218θ³ + 322503θ² + 842142θ + 733914) —
the same 5-fold structure at z = ∞.

Cubic field data: disc(z³−188z²−2368z+4) = 251440681552 = 2⁴·37³·557²
(note 41218 = 2·37·557). Not a square ⇒ **Galois group S₃**, field not abelian.

### ODE-side cross-check of the exponent: EXACT [PROVED]

For L (order 9) at a simple root z₀ of the leading symbol, the local exponents
are {0,1,…,7} ∪ {ρ} with ρ = 8 − c₈(z₀)/(z₀·c₉′(z₀)), where c₉, c₈ are the θ⁹,
θ⁸ coefficients. Computing:

    ρ(z) = (−679z³ + 106784z² + 1082176z − 1384) / (74z(−3z² + 376z + 2368))

and ρ(z) = 3/2 ⟺ −692(z³ − 188z² − 2368z + 4) = 0 — i.e. **ρ ≡ 3/2 identically
on the singular locus**, an exact algebraic identity, not a numerical fit.

    All three singularities z₁, z₂, z₃ are conifold points with exponents
    {0,1,2,3,4,5,6,7} ∪ {3/2}.

This independently confirms α = −ρ − 1 = **−5/2** for every ray, matching the
32-digit measurement, and it has a structural payoff:

**exactly one non-integer exponent at each singular point ⇒ σ_c − 1 has rank-1
image ⇒ the BZ operator satisfies the hypothesis of [BV] Def. 22 at all three
singularities.** The BV Frobenius-constant machinery *does* apply here. The
obstruction to running it verbatim is at the *other* end: z = 0 is not MUM for
the order-9 operator, only a rank-5 unipotent block inside it. Adapting [BV]
Def. 22 to a non-maximal unipotent block is the concrete next technical step
if one wants the full κ(ε) series for the BZ operator.

## Asymptotics and connection constants [VERIFIED]

All four sequences obey uₙ ~ A·λⁿ·n^α with

    α = −5/2   for ALL of Q, I′, Î, I    [measured to 32 digits, Richardson]

(not the −3/2 of the order-2 Apéry case; local exponent 3/2 at each conifold).

Method validated on a control: reproduced the classical Apéry constant
aₙ ~ (1+√2)^{4n+2}/(2^{9/4}π^{3/2}n^{3/2}) to 25 digits, ratio = 1.0 exactly.

Ladders extended exactly by the recurrence to n = 1500 (0.7 s in `Fraction`
arithmetic); Neville extrapolation in 1/n over 70 points at mp.dps = 9000:

| constant | value (first 40 digits) | stability |
|---|---|---|
| A_Q | 0.06667642572715676784165334063934544446963 | 158 digits (60pt vs 70pt) |
| A_{I′} | −0.7513558764749892995093920217080181499408 | 148 digits |
| A_Î | 0.2283848002232161349845209788253750644207 | 148 digits |
| A_I | 4.783817192943278912152333747240854600550 | 147 digits |

### The Frobenius/connection-constant statement

At the **first** singularity z₃ = 1/λ₃, with A_P, A_P̂ the same constants for
Σ Pₙzⁿ, Σ P̂ₙzⁿ:

    A_P / A_Q  = ζ(5)     [VERIFIED to 3878 digits]
    A_P̂ / A_Q  = ζ(3)     [VERIFIED to 3878 digits]

At the **second** singularity z₂ = 1/λ₂:

    A_Î / A_{I′} = c = −1/(2ζ(2)) = 12/(2πi)²   [VERIFIED to 1635 digits]

**Honest caveat:** the first two are formally *trivial* — A_P/A_Q = lim Pₙ/Qₙ
= ζ(5) because I′ₙ → 0. They are a (very strong, 3878-digit) consistency check
on the extrapolation machinery, not a new theorem. The content is entirely in
the *third* line, and that content is BZ's decomposition.

### ANSWER TO T2's QUESTION

> "is c (or 1/c, or a Möbius transform of c) a ratio of these constants?"

**Yes, and exactly so:** c = A_Î/A_{I′}, the ratio of the two connection
constants on the middle ray. Its value is 12/(2πi)². The ζ-values ζ(5), ζ(3)
are the ratios at the *first* singularity; c is the ratio at the *second*.
Reading the singularities outward from z = 0, the connection ratios are

    z₃ :  ζ(5), ζ(3)      z₂ :  1/(2ζ(2))      z₁ :  —

The weights descend 5, 3, then **invert** to −2. That inversion is the defect.

## What is NOT known: the individual constants

A_Q, A_{I′}, A_I are **not** algebraic × π^k. [VERIFIED exclusions, 145 digits:]

| target | tested | result |
|---|---|---|
| A·π^e, e ∈ {−½,0,½,1,3/2,2,5/2,3} | minpoly deg ≤ 12, \|coef\| ≤ 10⁵ | none |
| A·π^{3/2} | deg ≤ 3, \|coef\| ≤ 10²⁵ | none |
| A·π^{3/2} | deg ≤ 6, \|coef\| ≤ 10¹⁵ | none |
| A·π^{3/2} | deg ≤ 12, \|coef\| ≤ 10⁸ | none |
| A²·π | deg ≤ 3, \|coef\| ≤ 10¹² | none |
| A_{I′}/A_Q, A_I/A_Q, A_I/A_{I′} | minpoly deg ≤ 12, \|coef\| ≤ 10⁶ | none |
| A_Q·A_{I′}·A_I·π^e, e ∈ {0,1,3/2,3} | rational, \|coef\| ≤ 10²⁰ | none |
| log\|A_Q\| vs {log π, log 2, log 37, log 557, log ζ(3), log ζ(5)} | \|coef\| ≤ 10⁵ | none |
| A_Q ∈ span{1, π^{−3/2}, π^{−1/2}, ζ(2), ζ(3), ζ(5)} | \|coef\| ≤ 10¹² | none |

Contrast with Apéry ζ(3), where the constant **is** (1+√2)²/(2^{9/4}π^{3/2}).
The BZ constants are genuinely harder — consistent with the S₃ cubic field and
the rank-9 operator. **These are the objects that actually vary over the cone.**

---

# T3 — Exclusion table for c (all at mp.dps = 600, maxcoeff 10¹², maxsteps 6·10⁴)

| relation tested | result |
|---|---|
| c rational | **excluded** |
| c ∈ span{1, ζ2, ζ3, ζ5, ζ2ζ3, ζ2²} | **excluded** |
| c ∈ span{1, log 2, Catalan, π, π²} | **excluded** |
| c ∈ span(14-term independent weight-graded basis through weight 8: 1, ζ2, ζ3, ζ2², ζ5, ζ2ζ3, ζ2³, ζ2ζ5, ζ3², ζ7, ζ2²ζ3, ζ2⁴, ζ3ζ5, ζ2ζ3²) | **excluded** |
| c·ζ(3) ∈ same weight-≤8 span | **excluded** |
| c·ζ(5) ∈ span{1, ζ2, ζ3, ζ2², ζ5, ζ2ζ3} | **excluded** |
| c·ζ(5) ∈ same weight-≤8 span | **excluded** |
| **c·ζ(2) rational** | **[−2, −1] ⇒ 2·c·ζ(2) + 1 = 0** |
| **c·π² rational** | **[1, 3] ⇒ c·π² + 3 = 0** |
| **c ∈ span{1, 1/ζ2, 1/ζ3, 1/ζ5}** | **[2, 0, 1, 0, 0] ⇒ 2c + 1/ζ(2) = 0** |

Verification standard met: found at 600 dps; the underlying identity is
independently verified against the exact ladders to **441 digits** at n = 360
with the theoretically-predicted convergence slope, and **proved** in §0.

**Note on a spurious hit.** An earlier run with a *degenerate* weight-≤8 basis
(both ζ8 and ζ2⁴ present) returned [0,…,0,175,0,…,0,−24], i.e.
175ζ(8) = 24ζ(2)⁴ — a relation among the basis vectors with **coefficient 0 on
c**, not a relation for c. Rerun with an independent 14-term basis (verified
independent: pslq returns None on the basis alone) gives the clean exclusion
recorded above. *Always check the basis for internal relations before reading
a PSLQ hit.*

Not tested (superseded — c is identified and proved): Γ(1/3)-periods,
ζ(5,3), the computed Frobenius constants as a basis.

---

# T4 — The cone

**Status: ANSWERED WITHOUT COMPUTATION, and the question is void as posed.**

c(a) = −1/(2ζ(2)) for **every** admissible cone point a, proved in §0 from
BZ's family-wide decomposition (llm/20 line 540) plus |λ₁(a)| < |λ₂(a)|
(BZ Remark 2). c does not vary. There is nothing to measure.

The July machinery (`worthiness/audit.py`, `fast_eval.py`, `gamma.py`) is
therefore **not** needed for c. It *is* needed for the quantities that do vary:

### Recipe for the follow-on (the constants that carry cone information)

For a cone point a with a-vector parameterisation:
1. Get the order-3 recurrence for I(a·n) — BZ themselves flag this as "a
   practical (though technically challenging!) task for existing creative
   telescoping realisations" (llm/20, Remark 2). Koutschan's
   `HolonomicFunctions` is what produced the a = (1,…,1) case. Cost: the
   printed coefficients are degree 9; expect worse off the symmetric point.
2. Cheaper alternative that skips creative telescoping entirely: the three
   λ_i(a) are the roots of F(x)/(x(p₃−x)), the cubic of llm/20 eq. (Fcubic),
   computable directly from a. **No recurrence needed for the singularities.**
3. Generate exact ladders Q(a·n), P(a·n), P̂(a·n) to n ≈ 1500 (0.7 s once the
   recurrence is known — the extension in this session cost under a second).
4. Extrapolate A_Q(a), A_{I′}(a), A_I(a) as in §T2 (Neville in 1/n, 70 points,
   mp.dps ≈ 9000 → ~150 digits). Verify α(a) = −5/2 or find the true exponent.
5. PSLQ the *ratios* A_{I′}(a)/A_Q(a) across cone points; look for a common
   algebraic factor times an a-dependent piece. Test whether the S₃ cubic field
   ℚ(λ(a)) controls them.

Budget estimate: step 1 dominates (creative telescoping, hours to days per
point, and may fail); steps 3–5 are minutes. **If step 1 is the blocker, note
that step 2 already gives the λ_i(a) for free**, so the asymptotic *rates* are
available cone-wide without any recurrence — only the *constants* need it.

---

# Files

- `work/DEFECT_IDENTIFY.md` — this file
- `work/DEFECT_LIT.md` — full T1 literature extraction (agent, PDFs fetched)
- scratchpad: `verify_c.py` (441-digit certificate), `rec_check.py` (exact
  recurrence verification), `ode.py` (symbolic operator), `conn.py`/`conn2.py`
  (connection constants), `ident.py`…`ident4.py` (algebraicity exclusions +
  Apéry control), `t3.py`/`t3b.py` (exclusion table)

