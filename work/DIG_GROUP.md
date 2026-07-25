# DIG-2 — the Rhin–Viola group half of the p-adic campaign

**Agent:** DIG-2 (group structure & denominator savings).
**Code:** `work/dig/g_*.py` (all mine; DIG-1's files untouched).
**Date:** 2026-07-25.

Everything below is exact rational arithmetic unless explicitly labelled.
Labels: `[PROVED]` = proof given here or cited; `[VERIFIED]` = exact finite
computation, no proof; `[CALIBRATED]` = a modelling step, flagged as such.

---

## 0. Headline

| quantity | value |
|---|---|
| group, weight 3 | `𝔊 = ⟨𝔞₁,𝔞₂,𝔞₃,𝔟,𝔥⟩`, **order 1920 = \|W(D₅)\|** `[VERIFIED]` |
| transfer identity | `Ĩ(h) := F̃(h)/(∏ⱼ(hⱼ−1)!·(1+2h₀−Σhⱼ)!)` is `𝔊`-invariant — **1200/1200 orbit points exact, 0 failures** `[VERIFIED]` |
| pipeline validation | reproduces Rhin–Viola `μ(ζ(3)) ≤ 5.51389062` as **5.51389063** |
| δ at the LSZ/Apéry totally symmetric point | **exactly 0** — orbit size 1 `[PROVED]` ⟹ **the orbit method is fresh money** |
| max δ/budget (unconstrained) | **0.4378** (at a point where the construction itself dies) |
| **the decisive number** | threshold **0.370431**; best attained **0.381408** ⟹ p-adic margin `+0.0110`/budget = **+0.033 absolute, vs the −0.586 ζ₅(3) deficit** `[CALIBRATED]` |

**Bottom line.** The group savings are of the right size and then some: at the
ζ₅(3) configuration the orbit method is worth ≈ **1.0–1.3** against a deficit of
**0.586**. The binding constraint is *not* δ — it is that leaving the totally
symmetric point to buy δ simultaneously costs p-adic smallness. Under the
archimedean-calibrated transfer model the two effects cross, barely, in favour
of the group: `+0.033` where the symmetric point has `−0.586`. Confirming or
refuting that crossing is exactly DIG-1's margin function (§7 gives the rule).

---

## 1. The foundation stone: the Transfer Principle `[PROVED]`

This is the load-bearing new statement, and it dissolves the obstacle that
Lai–Sprang–Zudilin themselves flag as the blocker.

Let `R(t) ∈ ℚ(t)` have poles only at non-positive integers, `deg R ≤ −2`, with
partial fractions `R(t) = Σ_{i,k} r_{i,k}/(t+k)^i`. Set

```
ρ_i    := Σ_k r_{i,k}
ρ_{0,θ}:= −Σ_{i,k} r_{i,k} · Σ_{ν=0}^{k−1} (ν+θ)^{−i}
```

Then **both** of the following hold with *the same rational numbers*:

* **Archimedean** (Hurwitz):
  `Σ_{m≥0} R(m+θ) = ρ_{0,θ} + Σ_{i≥2} ρ_i·ζ(i,θ)`
* **p-adic** (Volkenborn, Lai–Sprang llm/15 Lemma 21):
  `−∫_{ℤ_p} R̃(t+θ) dt = ρ_{0,θ} + Σ_{i≥2} ρ_i·ω(θ)^{1−i}ζ_p(i,θ)`

(`R̃` the primitive of `R`.) The two constructions differ **only** in which
*value* is attached to each `ρ_i`; the coefficient map `R ↦ (ρ_{0,θ}, ρ_2, ρ_3, …)`
is literally the same ℚ-linear functional of the partial-fraction data.

> **Corollary (Transfer Principle).** Every Rhin–Viola / Zudilin transfer
> identity — being an identity *between the rational coefficients* `ρ` at two
> parameter points — is simultaneously an archimedean and a p-adic identity.
> Likewise every denominator/integrality lemma, being a statement about
> rational numbers, holds verbatim at every orbit point.

This is the p-adic analogue of the July campaign's ν_p-sharpening
(`zeta-math/worthiness/CONJECTURE.md`: "legitimate because the underlying
identity `I′(ga) = I′(a)·∏h_i(a)!/∏h_i(ga)!` is exact p-adically"), pushed one
level further: not just *valid in every completion*, but **the p-adic
construction's coefficients ARE the archimedean construction's coefficients.**

**Why this matters.** LSZ (llm/18:413) write: *"It is natural to expect a
hypergeometric-type identity for the Volkenborn integrals…"* and (llm/18:409)
propose the group method as future work. The Transfer Principle says **no new
Volkenborn transformation theory is needed**: the group acts on the rational
function, and the Volkenborn integral is a passive spectator. The corpus survey
(§8) confirms that a Rhin–Viola group has *never* been used p-adically — the
intersection "RV group ∩ p-adic" is empty in 37 papers.

### 1b. δ is insensitive to the p-adic shift `[PROVED]`

Replacing an integer parameter `c·n` by a θ-shifted one `c·n + O(1)` changes
`ord_ℓ` of each factorial by at most `O(1)`, hence changes `ν_ℓ` by `O(1)` for
each prime, hence changes `log Φ_n` by `O(π(m₃n)) = O(n/log n) = o(n)`.
Therefore

> **δ(directions) is the same function in the p-adic and archimedean worlds.**

So δ may be computed entirely with the classical machinery — which is what §3–§6
do.

---

## 2. The group, explicitly `[VERIFIED]`

Realisation (Zudilin, llm/04 Lemma 8): directions `(α,β)` with
`{β₁,β₂} < {α₁..α₄} < {β₃,β₄}` and `Σα = Σβ`; the 4×4 matrix
`c_{jk} = |α_j − β_k|`.

**Generators** (all involutions):

| gen | action on `c` |
|---|---|
| `𝔞_j`, j=1,2,3 | swap rows `j` and `4` |
| `𝔟` | swap columns 3 and 4 |
| `𝔥` | `(c₁₁ c₃₃)(c₁₃ c₃₁)(c₂₂ c₄₄)(c₂₄ c₄₂)` |

`|𝔊| = 1920` — computed by BFS closure, matching Zudilin's C++ count. `𝔊 ≅ W(D₅)`
(the Rhin–Viola group series is `W(A₄)=120` for ζ(2), `W(D₅)=1920` for ζ(3),
`W(E₆)=51840` for ζ(4), `𝔖₇=5040` for the Brown–Zudilin ζ(5) cell integral).

**On the `(a,b)`/`h` side** (`b₁ = 1` normalisation), with
`h₀ = b₃+b₄−b₁−a₁`, `h₁,₂,₃ = 1−b₁+a_{2,3,4}`, `h₄ = b₄−a₁`, `h₅ = b₃−a₁`:

```
𝔞_j : a_j <-> a_4                     (moves h₀ !)
𝔟   : b_3 <-> b_4
𝔥   : (a₁,a₂,a₃,a₄; 1,b₂,b₃,b₄) ↦ (b₃−a₃, a₂, b₃−a₁, a₄;
                                    1, b₂+b₃−a₁−a₃, b₃, b₃+b₄−a₁−a₃)
```

The point that made the first search fail and is worth recording: **`𝔖₅`
permuting `h₁..h₅` acts trivially on the rational function** (it is a product),
so the group is invisible at fixed `h₀`. The non-trivial elements are the row
swaps `𝔞_j`, and **they move `h₀`**. Any search for transfer identities must be
cross-`h₀`.

---

## 3. The transfer identity, verified exactly `[VERIFIED]`

Combining Zudilin's eq. (4.4) with Lemma 9 gives the invariant in `h`-language
(derived here; not stated in this form in llm/04):

```
        H(c)      G̃(a,b)                              F̃(h)
Ĩ  :=  ------  = ----------------------------  = ---------------------------------
        Π(c)      ∏ⱼ(aⱼ−b₁)! · ∏ⱼ(aⱼ−b₂)!        ∏_{j=1}^{5}(hⱼ−1)! · (1+2h₀−Σhⱼ)!
```

with `F̃(h) = Σ_{t≥0} R̃(h;t)`,
`R̃(h;t) = (h₀+2t)·(t+1)_{h₀−1}·∏_{j=1}^{5} 1/(t+hⱼ)_{1+h₀−2hⱼ}`.

`F̃(h) = A·ζ(3) + B` with `A,B ∈ ℚ` computed exactly by partial fractions
(`g_verify.py`).

**Anchor.** At the Ball/Apéry point `h₀=3n+2, hⱼ=n+1`:
`A/(2aₙ) = 1, 1/4, 1/36, 1/576 = 1/n!²` for `n = 1,2,3,4` where
`aₙ = Σ C(n,k)²C(n+k,k)²` — i.e. the machinery reproduces Apéry's numerator
sequence exactly, confirming Ball's `2n!²Σ…` normalisation.

**The test.** `Ĩ(h) = Ĩ(gh)` **coefficient-wise** (both `A/N` and `B/N`),
over the whole orbit:

| direction | orbit `\|𝔊(a,b)\|` | h-valid points | identity holds | fails | distinct κ |
|---|---|---|---|---|---|
| `(1,1,1,1;0,0,2,2)` (symmetric) | **1** | 1 | 1 | 0 | 1 |
| `(2,2,3,3;0,1,4,5)` | 40 | 40 | **40** | **0** | 3 |
| `(3,4,4,5;0,2,7,7)` | 80 | 80 | **80** | **0** | 5 |
| `(4,7,8,11;0,3,13,14)` | 1920 | 1200 | **1200** | **0** | 10 |

(the 720 skipped points are those where a brick degenerates, `1+h₀−2hⱼ < 1` —
a direction-dependent boundary effect, not a failure.)

`κ = N(gh)/N(h) = Π(gc)/Π(c)` is by construction a **ratio of factorials**.
`[PROVED identity]` (it is Bailey's / Whipple's for very-well-poised `₇F₆`, cited
from llm/04 Lemma 7–9); `[VERIFIED]` here at these directions.

### 3b. The identity survives half-integer (p-adic) parameters `[VERIFIED]`

Same test with `h₄,h₅ ∈ ℤ+½` (spectral-vector proportionality, exact 2×2
determinants over every pole-residue class):

| direction | comparable orbit points | proportional | NOT |
|---|---|---|---|
| `(2,2,3,3;0,1,4,5)` | 120 | **120** | **0** |
| `(3,4,4,5;0,2,7,7)` | 180 | **180** | **0** |
| `(4,7,8,11;0,3,13,14)` | 480 | **480** | **0** |

**The mechanism is lattice-robust: it is not an accident of integrality.**

---

## 4. What breaks p-adically — the honest flags

### (F1) Very-well-poisedness forces θ = ½, i.e. p = 2 `[PROVED]`

For `Γ(h_j+t)/Γ(1+h₀−h_j+t)` to be a *rational* function of `t` one needs
`2h_j − h₀ − 1 ∈ ℤ`. With `h₀ ∈ ℤ` this forces `h_j ∈ ½ℤ`. So the only
very-well-poised p-adic shift is `θ = ½`. For `p ≥ 3` (`|θ|_p ≥ q_p` ⟹
`θ = a/p^l`) the shifts must come as the *full* set `{ν/p^l : p∤ν}` — which is
exactly what Lai–Sprang (llm/15 Def. 16) and Lai (llm/16 §7, `V_n(t)`) do, and
it is why those p-adic constructions abandon the `(2t+h₀)` factor.

Sanity check on this: Lai's normalising constant `p^{(l+1/(p−1))Mφ(p^l)n}`
(llm/16:507) collapses at `p=2, l=1, φ=1, M=4` to `2^{8n}` — **exactly LSZ's
`C = 2^{8n}`.** The p=2 case is cheap precisely because `φ(2) = 1`.

### (F2) p-adic admissibility constrains the BASE point only `[PROVED]`

For the Volkenborn integral at shift θ one needs
* (R1) all poles of `R` at integers (else `R(t+θ)` has poles on `ℤ_p`);
* (R2) all numerator bricks at shift `≡ −θ (mod 1)` (else each numerator factor
  costs `−l` instead of gaining `+1/(p−1)`).

**Orbit points need satisfy neither.** They enter only through (i) the exact
rational transfer identity and (ii) their own denominator bound — both pure
ℚ-statements. This is what makes the method work at all, and it is the same
logic as Brown–Zudilin's `ν_p = max_{𝔤} ord_p ∏_F h_i!/∏_F(𝔤h_i)!`.

### (F3) The LSZ *shape* family has NO internal transfer identity `[VERIFIED — negative]`

Parametrise the LSZ shape (numerator bricks at θ, denominator at ℤ, all
centred, i.e. very-well-poised):

```
R(t) = (2t+h₀) ∏_{j=1}^{M}(t+θ+e_j)_{h₀−2e_j} / ∏_{j=1}^{M}(t+f_j)_{h₀+1−2f_j}
```

Exhaustive exact search for proportional pairs (the exact signature of a
transfer identity):

| family | points tested | proportional pairs |
|---|---|---|
| `M=2` (ζ_p(3)), all `h₀ ≤ 9`, cross-`h₀` | 113 | **0** |
| `M=4` (ζ_p(5), LSZ), all `h₀ ≤ 7`, cross-`h₀` | 1629 | **0** |
| `M=4`, fixed `h₀ ≤ 6` | 672 | **0** |

> **You cannot find the group by deforming LSZ inside its own shape class.**
> Its "group" is trivial. This is a real negative and explains why the
> literature has not stumbled on it.

### (F4) …but genuinely p-adic points DO have transfer partners `[VERIFIED — positive]`

Widening to the *full* very-well-poised half-integer family
(`h₀ ∈ ℤ`, `h_j ∈ ½ℤ`, any `q`, reduced modulo brick cancellation), 5507
distinct rational functions, 598 of them *genuinely p-adic* (integer poles **and**
a non-empty half-integer numerator): **13 proportionality classes contain a
genuinely p-adic point together with a distinct partner**, e.g.

```
p-adic  h₀=5, num {5/2,5/2}, den {1²,2⁴,3⁴,4²}   <->  int  h₀=4, den {1⁴,2⁴,3⁴}   κ = 2
p-adic  h₀=6, num {5/2,7/2}, den {2,3⁴,4}        <->  int  h₀=4, den {1³,3³}      κ = 1
p-adic  h₀=7, num {7/2,7/2}, den {1,2,3⁴,4⁴,5,6} <->  int  h₀=5, den {1,2⁴,3⁴,4}  κ = 27/2
p-adic  h₀=6, num {5/2,7/2}, den {1,2³,3⁴,4³,5}  <->  int  h₀=7, num{1,2,5,6},
                                                        den {3⁴,4⁴}               κ = 2⁸
```

**The partners are integer-parameter points** — i.e. members of the classical
archimedean family where the RV group and the whole denominator theory live.
The mechanism is a *quadratic transformation* (Gauss duplication
`(t+½)_n (t+1)_n = 2^{−2n}(2t+1)_{2n}`), the classical bridge between
half-integer and integer very-well-poised parameters.

> **This is the bridge**: a p-adic linear form equals, times an explicit rational
> κ, an integer-family linear form, and the integer family carries the full
> 1920-element orbit. `[VERIFIED at small size; the systematic family version is
> the natural next lemma and is NOT yet proved.]`

---

## 5. The savings function δ `[PROVED formula, VERIFIED implementation]`

```
ν_p   = max_{g∈𝔊} ord_p( Π(c·n) / Π(g c·n) ),   Π(c) = c₂₁!c₃₁!c₄₁!c₁₂!c₃₂!c₄₂!c₃₃!c₄₄!
Φ_n   = ∏_{√(m₀n) < p ≤ m₃n} p^{ν_p}
δ     = lim log Φ_n / n = ∫₀¹ φ(x) dψ(x) − ∫₀^{1/m₃} φ(x) dx/x²
φ(x)  = max_{g∈𝔊} Σ_{i∈F} ( ⌊c_i x⌋ − ⌊(gc)_i x⌋ ),   F the 8-element Π-index set
budget = 2m₁ + m₂,   m₁ = β₄*−α₁*,  m₂ = max{α₁−β₁, α₂−β₂, β₄*−α₃, β₄*−α₄, β₃*−α₁*}
```

**End-to-end validation.** At Rhin–Viola's optimum `(18,17,16,19; 0,7,31,32)`:

```
m₀=19 m₁=16 m₂=18 m₃=16   budget = 50
∫₀¹φ dψ = 24.18768530     ∫₀^{1/16} = 4.00000000
δ = 20.18768530           orbit of distinct F-multisets: 118
C₂ = 29.81231470
μ(ζ(3)) ≤ 5.51389063      <-- published: 5.51389062
```

Eight-digit agreement with the published irrationality measure. The group,
the invariant, the φ-function and the two integrals are therefore all correct.

---

## 6. T3 — the symmetric point, and how much is available

### 6a. The totally symmetric point banks NOTHING `[PROVED]`

Apéry/Ball ⟺ `α = (1,1,1,1)`, `β = (0,0,2,2)`; then **every** `c_{jk} = |α_j−β_k| = 1`.
A group acting by permutations of 16 equal entries has a single orbit point, so

```
ν_p ≡ 0,   Φ_n ≡ 1,   δ = 0 exactly,   stabiliser = all of 𝔊.
```

The same holds for LSZ's ζ₂(5) point (all bricks equal). **Answer to the T3
question: the stabiliser is the *whole group*, the orbit is a point, and LSZ /
Apéry / Calegari / Beukers have banked exactly zero group savings. The orbit
method is fresh money, 100 % of it.**

### 6b. How much money `[VERIFIED]`

Scale-free relative saving `δ/budget`, maximised over integral directions:

| directions (Σ ≤ 30) | δ | budget | δ/budget | δ at a budget-3 config |
|---|---|---|---|---|
| `(4,7,8,11; 0,3,13,14)` | 11.9533 | 29 | **0.41218** | **1.2365** |
| `(2,7,8,9; 0,1,12,13)` | 12.6730 | 32 | 0.39603 | 1.1881 |
| RV optimum | 20.1877 | 50 | 0.40375 | 1.2113 |
| **symmetric** | 0 | 3 | **0** | **0** |

Absolute ceiling found (subject to the construction still working):
`δ/budget = 0.4378` at `(5,7,9,5; 0,2,11,13)`.

> **Raw answer to "is δ big enough for 0.586?":** at a weight-3, budget-3
> configuration the group is worth **δ ≈ 1.21–1.31**, i.e. **2.1× the 0.586
> deficit.** In isolation, yes — comfortably.

Consistency check against the literature: Brown–Zudilin's ζ(5) record point has
`δ = 34.394` against `Σm = 84` → `0.4094`. Rhin–Viola's ζ(3) optimum → `0.4038`.
Both land at ≈ 40 %, and my independent maximisation caps out at ≈ 44 %.
**A Rhin–Viola group removes about 40 % of the denominator, universally.**

---

## 7. The decisive number `[CALIBRATED — read the caveat]`

δ alone is the wrong objective: leaving the symmetric point to buy δ *also*
costs smallness. Archimedean calibration (`g_cal.py`, `C₀ = −f₀(τ₀)` per
llm/04 Lemma 12, anchored to Zudilin's printed `C₀ = 47.15472079`,
`C₁ = 48.46940964`):

| point | C₀/budget | δ/budget | margin/budget = (C₀−budget+δ)/budget |
|---|---|---|---|
| symmetric (Apéry) | 1.175165 | 0 | **0.175165** |
| RV optimum | 0.943094 | 0.403754 | **0.346848** |
| max-δ point `(4,7,8,11;…)` | 0.551327 | 0.412182 | **−0.036** (construction dies!) |
| max-δ that still works | 0.647086 | 0.437758 | 0.084844 |
| **best combined** `(25,26,27,28; 1,8,48,49)` | 1.054454 | 0.326954 | **0.381408** |

### The reduction

The p-adic weight-3 ledger (`work/PADIC_SEAM.md` §T4.2) gives, at the
totally symmetric point with budget 3,
`margin = 6 log 5/4 − 3 = −0.5858`, i.e. `(α_p − growth)/budget = 0.804734`,
against the archimedean `C₀/budget = 1.175165`. Their difference is

```
Δ := 1.175165 − 0.804734 = 0.370431
```

**Equal-degradation model `[CALIBRATED]`:** assume the p-adic smallness ratio
`(α_p − growth)/budget` degrades off the symmetric point by the same amount as
the archimedean `C₀/budget`. Then

```
    p-adic margin / budget  =  (C₀ − budget + δ)/budget  −  0.370431
```

and **ζ₅(3) is reached iff `max (C₀ − budget + δ)/budget > 0.370431`.**

### The answer

Hill-climbing that objective over integral directions (6 independent seeds,
scales up to Σ ≈ 250):

```
CEILING:  0.381408   at  α = (25,26,27,28),  β = (1,8,48,49)
          budget = 72,  δ = 23.54070,  δ/budget = 0.326954,  C₀/budget = 1.054454
          (this direction gives μ(ζ(3)) ≤ 5.5780 — near but not at RV's optimum,
           because RV optimise μ, not margin-per-budget)

threshold = 0.370431      ⟹   p-adic margin/budget = +0.010977
                              absolute margin at budget 3 = +0.0329
                              (the symmetric point has −0.5858)
```

> **THE DECISIVE NUMBER.** The best group saving available near the ζ₅(3)
> configuration takes the margin from **−0.586 to +0.033** — a crossing, by
> about 6 % of the remaining budget. The orbit method removes **106 %** of the
> ζ₅(3) deficit on this calibration.

### Caveat, stated plainly

The crossing is **entirely inside the modelling step**. What is `[VERIFIED]`:
the group, the transfer identities, δ, the archimedean columns, `δ = 0` at the
symmetric point. What is `[CALIBRATED]`: that the p-adic `(α_p − growth)/budget`
falls off-symmetry exactly as the archimedean `C₀/budget` does. Two reasons to
expect the p-adic side to do **better** than this model, i.e. for the crossing
to be safer than `+0.033`:

1. `α_p` is a **Legendre-type valuation sum** — piecewise linear and homogeneous
   in the direction vector. `C₀ = −f₀(τ₀)` is a transcendental saddle value that
   collapses fast off-symmetry (from 1.175 to 0.55 in the table above). A linear
   functional should degrade far less than a saddle value.
2. The p-adic construction gets `ζ_p(even) = 0` and the degree-kill for free
   (`PADIC_SEAM` §T4.1), so it needs fewer parameter constraints than the
   archimedean one and can sit at better shapes.

One reason it could be worse: the p-adic gain `+L/(p−1)` per numerator brick is
the term that shrinks as `p` grows, and it is exactly the term that off-symmetric
shapes attack.

**⇒ Handoff to DIG-1 (§9).**

---

## 8. Literature position `[VERIFIED by corpus sweep]`

A full cross-tabulation of `llm/` (37 papers) for p-adic markers
(`Volkenborn`, `ζ_p`, `ℤ_p`) against group markers (`Rhin`, `permutation
group`, `group of order`) returns **no paper that uses a Rhin–Viola group
p-adically.** The two files that mention both state it as open:

* **llm/18:409 (Lai–Sprang–Zudilin 2025)** — *"our construction … and the earlier
  ones … exploit exclusively the so-called totally symmetric hypergeometric
  approximations… It may certainly be of interest to … investigate more general
  hypergeometric series … amenable to … the arithmetic group method as developed
  in the works of Rhin and Viola."* And llm/18:413: *"It is natural to expect a
  hypergeometric-type identity for the Volkenborn integrals…"*
* **llm/21:567 (Brown 2026)** — *"A referee asked the excellent question of
  whether the matrices `D_n` can be designed to make use of the cancellation of
  primes in the method of Rhin–Viola. I do not know the answer…"*

The nearest existing object is **Lai 2024 (llm/16 §7–8)**, the only genuinely
multi-parameter p-adic Volkenborn family, `V_n(t)` with free `(M; δ₁…δ_J; l; wₙ)`
— but its saving `Φ_n^{−s/J}` is an `inf_y` over floor functions (a
Chudnovsky–Rukhadze–Hata brick saving), **not** a `max_{g∈𝔊}` orbit saving.
The two are independent and compose.

§1's Transfer Principle answers llm/18:413 in the negative-is-positive
direction: the hypergeometric identity for Volkenborn integrals is **not
needed** — the identity is on the rational coefficients, and the Volkenborn
integral never sees it.

---

## 9. Handoff to DIG-1 — the composition rule

The group enters DIG-1's margin function additively and in exactly one place:

```
margin(directions) = α_p(directions) − growth(directions) − budget(directions) + δ(directions)
```

* `δ(directions)` is computed by `work/dig/g_group.py::delta_limit(alpha, beta)`
  (validated to 8 digits against RV's published μ). It is **the same function in
  both completions** (§1b).
* `budget = 2m₁+m₂` from `g_group.py::m_params`.
* At the totally symmetric point `δ = 0` exactly, so DIG-1's current margin is
  unchanged there — the group is a strict addition.
* **The one number DIG-1 must supply:** `(α_p − growth)/budget` at a
  non-symmetric direction. If it exceeds `1 − δ/budget` anywhere, ζ₅(3) follows.
  Concretely, at `α=(25,26,27,28), β=(1,8,48,49)` the requirement is

  ```
  (α_p − growth)/72  >  1 − 0.326954 = 0.673046      i.e.   α_p − growth > 48.46
  ```

  For reference the symmetric-point value of that ratio is `0.804734`, so
  **the group can afford a 16 % relative degradation of the p-adic smallness
  ratio and still win.**

Also worth handing over: `δ/budget` is capped near `0.44`, and the
`(δ/budget, C₀/budget)` Pareto frontier is materially *concave* — pushing δ past
≈ 0.33 costs smallness faster than it gains. **Do not optimise δ alone**; the
max-δ point `(4,7,8,11;0,3,13,14)` has a *negative* archimedean margin.

---

## 10. Non-vanishing (tracked, as instructed)

Orbit moves are by construction multiplication of the whole linear form by a
non-zero rational `κ = Π(gc)/Π(c)`, so:

* the leading term is scaled, never cancelled;
* `S(gh) = 0 ⟺ S(h) = 0` — an orbit move can never create or destroy vanishing;
* Bel's criterion input (llm/18 Lemma 4(iii), the Casoratian
  `ρ_{n,0}ρ_{n+1,3} − ρ_{n+1,0}ρ_{n,3} = 3·2^{16n+18}/(n+1)^5`) is therefore
  scaled by `κ_n κ_{n+1} ≠ 0` and stays non-zero.
* **Caveat for the (F4) bridge:** the quadratic-transformation partners are
  *different* rational functions, not orbit images, so the non-vanishing must be
  re-checked there. At every instance found, `κ ≠ 0` (values `1, 2, 4, 16, 27/2,
  18, 54, 4/27, 4/3, 2⁵, 2⁸`), so no vanishing is introduced. `[VERIFIED at the
  instances computed]`

---

## 11. Files

| file | contents |
|---|---|
| `work/dig/g_forms.py` | exact `(ρ_0, ρ_i)` for the parametrised p-adic family; LSZ anchors (`ρ_{0,3}=768`, `ρ_{1,0}=−1024`, `ρ_{1,3}=73728`, `ρ_n = 1,96,14944`) all reproduced |
| `work/dig/g_group.py` | the group (order 1920), `φ`, `δ`, `m`-parameters; RV validation → `μ ≤ 5.51389063` |
| `work/dig/g_verify.py` | exact transfer-identity verification; Apéry/Ball anchor |
| `work/dig/g_padic.py` | the same on half-integer (p-adic) parameters |
| `work/dig/g_search.py`, `g_search2.py` | negative searches inside the LSZ shape class |
| `work/dig/g_full.py` | exhaustive VWP half-integer proportionality classification |
| `work/dig/g_opt.py`, `g_cal.py`, `g_hill.py` | maximisation of `δ/budget` and of the combined objective |

## 12. Open items, ranked

1. **[the gate]** DIG-1's `(α_p − growth)` at non-symmetric directions. Everything
   hinges on it; §9 gives the exact threshold.
2. **[the bridge lemma]** Promote the (F4) instances to a family identity: prove
   that the θ = ½ very-well-poised family maps by Gauss duplication onto the
   integer family with an explicit factorial `κ`. This is the step that makes the
   1920-orbit available to a genuinely p-adic base point, and it looks like a
   known quadratic transformation waiting to be quoted.
3. **[p ≥ 3]** (F1) says the `(2t+h₀)` factor forces `p = 2`; for `p = 5` the
   shifts must be the full set `{ν/5}`. The group for *that* object (Lai's
   `V_n`) is not identified here. Two routes: (a) the `𝔖₇`/`W(E₆)` groups of the
   higher-weight families; (b) treat `∏_{p∤ν}(t+ν/p^l)_L` via Gauss
   multiplication as a step-`p^l` Pochhammer and look for the induced group.
4. **[free upside]** `μ(ζ₂(5)) < 20.34` and `μ(ζ₂(3)) < 7.177` need *only* items
   1–2 at `p = 2`, where (F1) is not an obstruction at all. That is the
   low-risk publishable target — and it is precisely what LSZ's Final Remarks
   ask for.
