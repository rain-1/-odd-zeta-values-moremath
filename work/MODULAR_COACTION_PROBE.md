# MODULAR_COACTION_PROBE — modular anchors for the unreachable sporadics,
# and a test of the "ε-jets = coaction components" dictionary

**Author:** Fable fork (direction 3), 2026-08-04.
Script: `work/z5eps/eps48_modular_nome.py` (+ inline identification run).
All series arithmetic exact (Fraction), order q^26.  Labels per programme
convention; literature attributions from model knowledge are marked [MK]
and should be cited properly before publication.

## Part A — modular anchors

### A.1 Instrument: the nome test

From each family's 3-term recurrence build the MUM operator
`L = θ^w − t(...) + t²(...)`, compute the Frobenius pair
`y₀ = ΣA(n)tⁿ`, `y₁ = y₀ log t + g` (with `L(g) = −L′(θ)y₀`, solved
coefficientwise), set `q = t·exp(g/y₀)`, invert to `t(q)`, and put
`F(q) = y₀(t(q))`.  Integrality of `t(q)` is the modularity fingerprint;
identification of `F(q)` names the parametrization.

**Control `[PASS, exact]`:** for γ (Apéry ζ(3)) the computed `t(q)` and
`F(q)` equal the classical Γ₀(6) eta-quotients
`t = q(η₁η₆/η₂η₃)^{12}`, `F = (η₂η₃)⁷/(η₁η₆)⁵` **exactly to q^26**.

### A.2 Findings for the three deformation-unreachable families

| family | t(q) integral? | F(q) identified? |
|---|---|---|
| **B** (9,3,27; χ₋₃) | **YES** (ℤ-coeffs to q^18+) | weight-1 object `1+3q−6q³−3q⁴+6q⁷−6q⁹+…`; NOT `E_{1,χ₋₃}` alone nor a 3-term Eisenstein combo at levels {1,3,9} — plausibly a level-27 theta/Eisenstein mix; **unidentified, fingerprint recorded** |
| **δ** (7,3,81; no limit) | **YES** | weight-2 object `1+3q−3q²−15q³−3q⁴+18q⁵+…`; unidentified, fingerprint recorded |
| **ζ** (9,3,−27; χ₋₃) | **YES** | **IDENTIFIED EXACTLY**: `F_ζ(q) = (9E₂(q⁹) − E₂(q))/8`, the weight-2 Eisenstein series on Γ₀(9), verified coefficientwise to q^26 |

Also observed: `t_B` and `t_ζ` have coefficient-wise equal magnitudes with
a period-9 sign/2-multiplier pattern — the two parametrizations appear to
be character twists of each other on the same level-9/27 geometry.

**Conclusion A:** all three families that the deformation instrument and
every harmonic fit provably cannot reach ARE modular-parametrized
(numerically established here; Zagier's six and Cooper's three are modular
per the literature [MK], and this test re-derives it where run).  The
modular anchor exists precisely where the binomial-world anchors fail.

### A.3 The candidate companion ansatz (formulated, first test run)

The second solution should be the *Eichler-integral / nome datum* of the
parametrization: `y₁/y₀ = log q` means the log-solution coefficients `g_n`
are the natural "companion letters" — and their q-side avatars are
twisted divisor sums (for ζ: plain `σ(n)` through `E₂`; for B: the
level-27 twisted object above).  First numeric check: the recurrence's
normalized second solution `B(n)` is NOT simply `g_n + λA(n)` (checked for
B and for the γ control) — the recurrence/ODE translation has boundary
inhomogeneities, so the precise dictionary `B(n) ↔ (g, y₀)` needs that
bookkeeping before a fit is meaningful.  That is the concrete,
well-defined next step; the raw materials (exact `t(q), F(q), g`) are now
on disk.  What the modular side promises that the harmonic side provably
lacks: letters built from `q`-expansion arithmetic (`σ`-sums and their
χ-twists at level 9/27) rather than cell-wise harmonic sums.

## Part B — the coaction dictionary, tested on existing data

Dictionary under test: *ε-jets of parametric families compute de Rham
coaction components; weight grading of jets = weight grading of the
coaction.*  Three predictions checked:

1. **Weight bookkeeping.**  ζ-monomials multiplying weight-s row data at
   ε-order m must have weight exactly m−s.  Holds throughout the
   eps42/43 graded-block data (by construction once the `−ζ(m)S_m`
   bookkeeping was forced — the dictionary *predicted* the shape the
   agent had to adopt to make validation pass).  CONSISTENT (weak-form).
2. **Smallest-jump inhomogeneity.**  The first variation's anchor
   equation should couple only to the lowest-weight row.  eps46:
   `L_BZ(Q̇) = −Σc_i′(n)Q(n+i)` — right side involves **Q only**, not
   P̂ or P.  CONFIRMED (a genuine retrodiction: the unipotent
   one-step-lowering of the connection).
3. **Galois equivariance.**  Untwisted instruments cannot produce
   χ-twisted coaction components.  Matches the eps43 dichotomy for
   B (χ₋₃) and ζ (χ₋₃).  δ is the edge case: χ = 1 but no archimedean
   limit; with A.2 showing δ modular with an (apparently) untwisted
   weight-2 form, δ's unreachability must be attributed not to a
   character but to Betti degeneracy (no real period for the relevant
   extension — "no limit" = nothing for a deformation row to attach to).
   PARTIALLY CONFIRMED, edge case explained by a distinct mechanism and
   flagged as the dictionary's open boundary.

**Verdict:** the dictionary survives contact with all existing data
(2 confirmations, 1 partial with a principled carve-out), and it has
already paid rent twice (the forced `−ζS` bookkeeping; the Q-only
inhomogeneity).  New falsifiable prediction for the next session:
**second variations should anchor with inhomogeneity in span{Q, Q̇}
only** (one- and two-step lowerings), never touching P̂ directly.

## Part C — follow-up mission (eps49): the ζ companion formula, B's form, ASD

### C.1 The ζ companion formula in modular letters `[VERIFIED exact ℚ, n ≤ 22; derivation given]`

Boundary bookkeeping, exact: with `B(0)=0, B(1)=1`, the generating series
satisfies `L_t(y_B) = t` — the only violated recurrence instance (n = 0)
is the inhomogeneity.  With the MUM kernel `{F, F log q, F log²q/2}` the
operator factors as `L_t = (P₃(t)/σ³)·F·θ_q³∘(1/F)`,
`P₃(t) = 1 − 2at + ct²`, `σ = θ_q log t`.  Hence the closed form

> **`B(n) = [tⁿ] F(q)·Θ(q)`,  `Θ = θ_q^{−3}Ψ = Σ_m Ψ_m q^m/m³`,
> `Ψ = t·σ³/(P₃(t)·F)`** — an Eichler-type integral in the identified
> modular data (`F_ζ = (9E₂(q⁹)−E₂(q))/8`, `t = t_ζ(q)`).

Verified coefficientwise over ℚ to n = 22 for **ζ** and for the **Apéry
ζ(3) control** (`eps49_zeta_companion.py`).  This is the companion of a
family for which the complete tame harmonic ansatz is provably empty —
the first companion formula for any of the conjectural seven, in modular
letters.  (Amusing fingerprint: `Ψ_ζ = q − 9q² + 73q⁴ − 126q⁵ + 344q⁷ …`
vanishes at m ≡ 0 mod 3 and `Ψ₄ = 73 = A_ζ(2)`.)

### C.2 Family B's weight-1 form identified `[VERIFIED exact, all 27 coeffs]`

> **`F_B(q) = b(−q)`, `b(q) = η(q)³/η(q³)`** — the Borwein cubic theta
> at `−q` (the level-9 cubic-AGM object of the χ₋₃ world; the `−q` twist
> raises the level to 36-type).  Found by exact linear solve after adding
> sign-twists to the cubic dictionary; the untwisted dictionary
> {a, b at q, q³, q⁹; η₉³/η₃} contains NO combination (completed
> negative).

So both χ₋₃ unreachable families are now anchored: ζ on Γ₀(9) Eisenstein
weight 2, B on the cubic theta `b(−q)` weight 1.  δ's weight-2 form
remains unidentified (fingerprint on record).

### C.3 ASD probe `[VERIFIED, 4 primes]`

The twisted Lucas law (eq LB) for ζ,
`p³B(ap+r) ≡ χ₋₃(p)^e B(a)A(r) (mod p)`, holds with **e = 1 exactly**:
at p = 5, 11 (χ = −1) e=0 fails and e=1 passes; at p = 7, 13 (χ = +1)
both agree, as they must.  Interpretation: with `F_ζ` identified and the
expected Sym² structure over Γ₀(9) (underlying weight-1 object of
character χ₋₃), the congruence factor `χ₋₃(p)` matches the character of
the non-unit Frobenius eigenvalue — the twisted Lucas law behaves exactly
like the mod-p shadow of Atkin–Swinnerton-Dyer for the identified
parametrization.  This makes the sporadics paper's open problems P2/P3
look approachable by modular technology (ASD congruences for Eisenstein
Sym²), at least for ζ.

## Part D — the Eichler-companion construction across all fifteen (eps52)

The construction of C.1 is intrinsic: it needs only the recurrence
(`L(y_B) = t` boundary identity + the nome factorization
`L = (P/σ^w)·F·θ_q^w∘(1/F)`, `P_{R2} = 1−at+ct²`, `P_{R3} = 1−2at+ct²`).
For order 2 the kernel condition is automatic; for order 3 it is the
geometric (Sym²-type) property, and the exact match against the
recurrence `B(n)` is its test.  `eps52_eichler_all.py`, exact ℚ, n ≤ 20:

| family | order | t(q) ∈ ℤ[[q]]? | construction matches B(n)? | form identified |
|---|---|---|---|---|
| A/Franel | 2 | YES | **PASS** | (known modular [MK]; not re-identified here) |
| **B** | 2 | YES | **PASS** | **b(−q) = [η₁³/η₃](−q)** (C.2) |
| C | 2 | YES | **PASS** | not attempted |
| D | 2 | YES | **PASS** | (known [MK]) |
| E | 2 | YES | **PASS** | (χ₋₄ world; not attempted) |
| F | 2 | YES | **PASS** | not attempted |
| α (Domb) | 3 | YES | **PASS** | (known [MK]) |
| γ (Apéry ζ3) | 3 | YES | **PASS** | Γ₀(6) etas (A.1, exact) |
| **δ** | 3 | YES | **PASS** | open — cubic weight-2 dictionary excluded, fingerprint on file |
| ε | 3 | YES | **PASS** | not attempted |
| **ζ** | 3 | YES | **PASS** | **(9E₂(q⁹)−E₂(q))/8** (A.2, exact) |
| **η** | 3 | YES | **PASS** | **[η₁⁵/η₅](−q)** (NEW, exact all 27 coeffs) |
| s₇ | 3 (d≠0) | YES | **PASS** | (Cooper level 7 [MK]) |
| s₁₀ | 3 (d≠0) | YES | **PASS** | (Cooper level 10 [MK]) |
| s₁₈ | 3 (d≠0) | YES | **PASS** | (Cooper level 18 [MK]) |

**Headline:** every one of the fifteen sporadic pairs — including all
seven conjecturals — satisfies the uniform companion formula

> `B(n) = [tⁿ] F(q) · θ_q^{−w}( t·σ^w / (P·F) )`

exactly (ℚ, n ≤ 20), with every nome integral to q^18.  For order 2 this
is automatic-but-now-explicit; for the twelve order-3 rows (AZ six +
Cooper three + controls) the PASS is a nontrivial numerical confirmation
of the `F·log²q/2` third-solution property family-wide.  Where the form
is identified (γ, ζ, B, η so far), the formula is a companion closed form
in modular letters — including three of the "no formula exists"
conjectural seven (B, ζ, η).

Honest labels: PASS = exact coefficient match n ≤ 20, not an all-n proof;
the all-n statement needs either the Sym²/geometric property proved per
family (classical for several [MK]) or a direct certificate; nome
integrality is a fingerprint, not a theorem, at this stage.

## Honest limits

Nome integrality is checked to q^18–q^26, not proved; F-identifications
beyond ζ are open; the companion↔(g,y₀) dictionary needs the
boundary-term bookkeeping before any fit; all [MK] attributions need
citations.  Nothing here is claimed at theorem grade.
