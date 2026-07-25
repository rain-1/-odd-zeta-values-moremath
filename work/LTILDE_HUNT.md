# SECTOR VERDICT for the primitive weight-7 form I′ₙ

**Agent: computational-mathematician. Date 2026-07-24.**
Working scripts: `work/ltilde/{prop,rate,sharp,ext,ctrl,w5,w5b,law12}.py`.
Read-only sources: `/home/ubuntu/fable-episode-2/zeta-math/worthiness/`.

---

## VERDICT: **SECTOR B**, and now with a *no-cancellation* proof shape.

    rho(I') >= rho_B = 0.0939373791041117      (-log rho_B = 2.36512689845)
    kappa   = 7   (exponent-tight; measured, not assumed -- see D)
    gamma_5,7 <= 2.36512689845 / 7 = 0.337875271        [ratio form]
    gamma_5,7 <= (C1 - C0)/(C1 + C2) = 0.705777240      [BZ/gamma.py form]

Sector A is **excluded**, not merely disfavoured. `ONE OF zeta(5), zeta(7) IRRATIONAL`
does **not** follow from this family. The margin is not close: the exponent gap is
`kappa - (-log rho) = 4.635` nats, i.e. a factor **103 per step**.

---

## A. The logical chain (improved: signs replace the cancellation argument)

The campaign's argument (`ZETA7_RESIDUE_I3.md` §3) needed *two* facts: (1) I″ rides B, and
(2) I rides sector A, so that the B-coefficient of I′ = (B-coeff of I) − ζ₂(B-coeff of I″)
is nonzero. Fact (2) is a delicate statement about a *cancellation* being exact.

**It is not needed.** The signs make cancellation impossible:

| step | statement | status |
|---|---|---|
| 1 | L annihilates all 74 exact qₙ | **re-verified**: 70/70 relations exactly 0 |
| 2 | s, P̂ ∈ sol(L) | **new certificate**, see B |
| 3 | ⇒ \|I″ₙ\|^{1/n} → one of {6329.26, 10.6454, 0.0939374, 1.58e−4} | discrete, 4 choices |
| 4 | measured: → 0.0939374 (**sector B**) | see C |
| 5 | I″ₙ < 0 for **all** n = 0…140 | exact rationals, verified |
| 6 | Iₙ > 0 for all n | **rigorous** (all-positive 4-fold series, STATE §1.7) |
| 7 | I′ₙ = Iₙ − ζ₂I″ₙ = Iₙ + ζ₂\|I″ₙ\| ⇒ **\|I′ₙ\| ≥ ζ₂\|I″ₙ\|** | no cancellation possible |
| 8 | ⇒ limsup \|I′ₙ\|^{1/n} ≥ 0.0939374 ≫ 1.58e−4 | **sector A impossible** |

Step 7 is the improvement: I′ₙ is a sum of **two positive quantities**. No conspiracy of
coefficients can make I′ decay faster than I″. The verdict is therefore independent of
anything at all about Iₙ's own decay rate, of den(P₃), of the snap, and of the grid
hypothesis. The *sole* remaining dependency is step 2.

---

## B. Step 2 certified: s, P̂ genuinely satisfy L  (NEW — never done past n=3)

Propagated s, P̂, P, q **exactly in ℚ** (`fractions.Fraction`), index-3 unlocked by the
`c₀(−1)=0` relation. Reproduces `q₃ = 94357501`, `s₃ = 1396906795/3`,
`P̂₃ = 232175579999/972` and the known-false `P₃ = 7536585377621845/22464864`
(den = 2⁵·3⁸·107 — the spurious 107 of GOTCHA G4).

**Arithmetic certificate — the denominator ledger:**

```
    den(s_n)  | d_n^5   for  141/141   n = 0..140
    den(Ph_n) | d_n^5   for  141/141   n = 0..140
```

**Control experiment** (three generic rational initial conditions propagated through the
same L):

| n | log₁₀den(sₙ) | log₁₀den(P̂ₙ) | generic-1 | generic-2 | generic-3 | log₁₀ d_n⁵ |
|---|---|---|---|---|---|---|
| 20 | 14.5 | 37.6 | 63.3 | 64.5 | 64.1 | 41.8 |
| 40 | 29.0 | 74.2 | 116.3 | 117.6 | 117.1 | 78.6 |
| 60 | 47.2 | 122.3 | 180.1 | 181.4 | 180.9 | 124.9 |

`den | d_n^5` holds **61/61** for the true ladder and **4/61** for every generic solution
(the 4 being trivial small-n cases). A degree-19 operator divides by `c₄(n)` at every
step; a generic solution therefore drags in the prime factors of `c₄(n)` for all n and its
denominator overshoots `d_n^5` by ~55 digits at n=60. That the true (s, P̂) stay
`d_n^5`-smooth for 141 consecutive n is an arithmetic coincidence of probability
indistinguishable from zero unless they are genuinely annihilated by L.

**The same test separates P:** `den(P_n) ∤ d_n^7` for **101 of 138** indices n = 3…140; the
excess over `d_n^7` takes only the values `{1, 107, 321 = 3·107}`, and
`den(P_n) | 321·d_n^7` for **141/141**. So the L-propagated P is arithmetically *clean but
wrong*: it obeys a bounded-constant `d_n^7` law, yet the persistent prime 107 (absent from
q, s, P̂, which are strictly `d_n^5`-clean) marks it as a different solution branch.

Note the exclusion of P from sol(L) does **not** rest on the 107. It is forced: the
propagated I′₃ = 43.71, whereas step 7 of section A gives rigorously
`I′₃ = I₃ + ζ₂|I″₃| = I₃ + 3.5675e−5` with `0 < I₃ ≤ 3.0903e−9` (the proved majorant of
`zeta7_p3_upperbound.py`). So `I′₃ = 3.5675e−5` to 4 significant figures **unconditionally
on the snap**, and 43.71 is impossible. P ∉ sol(L), confirming §3.4 — and, as a by-product,
`I′₃` is no longer "conditional on P₃": it is pinned by the ladder plus a rigorous bound.

---

## C. Step 4: the rate of I″ — stability table

I″ₙ = −9qₙζ₅ + 2sₙζ₃ − P̂ₙ evaluated from **exact rationals** at `dps = 4.9n + 100`
(no forward-propagation instability at all, unlike the campaign's 240–300 dps float run).
Statistic: `−log|I″_{n+1}/I″ₙ|`. Model `I″ₙ ~ Cρⁿn^β` ⇒ raw estimator has a `−β/n` bias;
Richardson-1 `2a_{2n}−a_n` kills it, Richardson-2 kills the `1/n²` term.

| n | raw | Rich-1(n,2n) | Rich-2 |
|---|---|---|---|
| 10 | 2.6796806457 | 2.3818974599 | 2.3655899615 |
| 20 | 2.5307890528 | 2.3696668361 | 2.3651904833 |
| 30 | 2.4775676766 | 2.3672005606 | **2.3651463543** |
| 40 | 2.4502279445 | 2.3663095715 | — |
| 50 | 2.4335830363 | 2.3658901534 | — |
| 60 | 2.4223841186 | 2.3656599059 | — |
| 69 | 2.4150358618 | **2.3655314035** | — |

**Target `−log ρ_B = 2.36512689845`.** Raw drifts monotonically down (β<0 prefactor);
Rich-1 reaches 2.36553 at n=69 and is still descending; Rich-2 sits at **2.36515** — five
correct digits. Two disjoint windows (Rich-1 at n=20 and n=69; Rich-2 at n=10 and n=30)
agree.

Crucially this is a **discrete identification, not a continuous fit**: given step 2, the
only admissible answers are `{−8.752939, −2.365127, +2.365127, +8.752939}`. We are within
2·10⁻⁵ of one of them and 4.7 away from the nearest alternative. Sector B.

Also confirmed: I″ₙ < 0 for all 141 indices; ratios climb monotonically
`0.0042, 0.0181, …, 0.0891 (n=65)` → 0.0939374, reproducing the campaign's figures and
extending them from n=29 to n=140.

---

## D. The honest κ — measured, not assumed

The mission asked whether the true denominator budget is below 7. **It is not.** Measured
directly on the **361 exact weight-5 ladder terms** (`falsify_data/ladder_{P,Ph}.json`),
which is the only family where the true P is known:

```
    den(P_n)  | 12 * d_n^5   :  361/361      <- the campaign's sharp-12 law, CONFIRMED to n=360
    den(P_n)  |      d_n^5   :    1/361
    den(P_n)  |  6 * d_n^5   :    1/361      <- 12 is sharp, not 6, not 2
```

| n | log den(Pₙ)/n | log(d_n⁵)/n | ratio |
|---|---|---|---|
| 80 | 4.94330 | 4.96653 | 0.9953 |
| 200 | 5.11650 | 5.15365 | 0.9928 |
| 320 | 5.00779 | 5.03444 | 0.9947 |
| 355 | 4.94456 | 4.97666 | **0.9936 → 1** |

So at weight 5 the constant-term denominator is **exactly `d_n^weight`, tight**, modulo the
bounded constant 12 (which does not move the exponent). The weight-7 descent ladder behaves
identically: `log den(P̂ₙ)/n / (5·log d_n/n) → 0.9856` at n=140, i.e. `κ_desc = 5` tight.

**Therefore κ = 7 for the weight-7 primitive form is the honest budget**, not a placeholder.
There is no `d_n²d_{2n}`-type structure lowering it: the analogue that we *can* measure is
tight at its nominal value. (For reference the slack members are `den(sₙ) ~ d_n^1.95` and
weight-5 `den(P̂ₙ) ~ d_n^3.95` — but the binding constraint on a linear form is its constant
term, and that is tight.)

To pass at sector B one needs `κ < 2.365`, i.e. `den(Pₙ) ≲ d_n^{2.365}`. The shortfall is
`d_n^{4.635} ≈ 103ⁿ`.

---

## E. The weight-5 calibration — this is the *expected* behaviour, not an anomaly

The BZ ζ(5)/M₀,₈ family has the identical dichotomy, and it is settled in the published
literature. Char poly `4λ³−2368λ²−188λ+1`, roots:

```
    lambda_1 = 0.0050037815   (-log = 5.2975614)   <-- SMALL: 0.0050038 < e^-5 = 0.0067379  => WOULD PASS
    lambda_2 = -0.0843843161  (-log = 2.4723737)   <-- MIDDLE: the actual linear-form rate
    lambda_3 = 592.0793805    ( log = 6.3836407)   <-- Q_n growth
```

`gamma.py` (which reproduces BZ's printed values to 8 decimals, re-run and confirmed here)
records **`C0 = log lambda_2 = -2.47237372`** at the symmetric point — the *middle* root.
My independent measurement on the 361 exact terms agrees:

| n | 50 | 100 | 200 | 300 | 340 | target |
|---|---|---|---|---|---|---|
| `−log\|X_{n+1}/Xₙ\|` | 2.5214236 | 2.4971339 | 2.4848135 | 2.4806802 | 2.4797058 | **2.4723737** |

and identically for `Qζ₃−P̂` and for `(Qζ₅−P) ± ζ₂(Qζ₃−P̂)` — every combination rides λ₂.

**So at weight 5 the smallest saddle would have proved ζ(5) irrational, and the primitive
form provably does not ride it.** Weight 7 reproduces this exactly: sector A (1.58e−4)
sits below `e⁻⁷ = 9.119e−4` and would pass; the primitive form rides sector B instead.
The weight-7 sector-B verdict is the *generic* outcome of this construction, not bad luck.

---

## F. γ₅,₇ and what the gap means for the asymmetric-orbit / RV follow-on (STATE §8 item 5)

```
    C1 = log lambda_max = 8.75293868604       (rigorous given L; certified char poly)
    C0 = log rho(I')   <= log rho_B = -2.36512689845
    C2 = kappa = 7      (measured tight, section D)

    gamma_5,7 = (-log rho)/kappa      <= 0.337875271
    gamma_5,7 = (C1-C0)/(C1+C2)       <= 0.705777240
    (sector A would have given 1.250419812 / 1.111276932 -- the theorem-grade event)
```

**Sharpest statement of what the measured gap means for the RV follow-on.** The dimensionless
invariant the Rhin–Viola group moves is `(-C0)/C2`. Measured at weight 5, over the *entire*
known orbit:

```
    symmetric point a=(1,..,1)              : (-C0)/C2 = 2.47237372/5        = 0.494475
    BZ record       a=(8,16,10,15,12,16,18,13): (-C0)/C2 = 31.55296935/49.60574813 = 0.636075
    maximal leverage of the full weight-5 RV group  = factor 1.28636  (+28.6%)
```

Applying the *same relative leverage* to weight 7 from sector B gives
**γ₅,₇ ≈ 0.4346** — still less than half of 1. Reaching γ₅,₇ = 1 requires a factor
**2.9597 (+196%)**, i.e. **≈ 7× the total leverage the Rhin–Viola group delivers at
weight 5**. Equivalently the orbit must find 4.635 nats of exponent, against the 1.03 nats
(`5·(0.636−0.494)` in κ-normalised units) that the group is empirically worth.

**Conclusion for §8 item 5: the asymmetric-orbit optimisation cannot close a sector-B gap.**
It is worth running only if a *different* sector is in play. The productive redirection is
not orbit search on M₀,₁₀ but a construction whose primitive form rides the small saddle —
i.e. attacking the `C0 = log λ₂ (middle) not log λ₁ (small)` phenomenon itself, which is now
established as a *stable structural feature* of cellular families at both weight 5 and
weight 7.

---

## G. Feasibility notes for extending the data

- **Exact ℚ propagation of the ladder through L is cheap and stable**: n=0…140 for all four
  sequences in ~7 min single-core. This supersedes the float sector pipeline entirely (no
  guard-digit problem — the instability was an artefact of propagating in floats).
  It is the right tool for any future ladder question. Numerators reach ~600 digits at
  n=140; n=300 is comfortably reachable (~1 h).
- **I″ₙ evaluation** needs `dps ≈ 4.83n + guard` (the qₙ/I″ₙ dynamic range) — trivial once
  the rationals are exact.
- **What is still not extendable**: Pₙ and I′ₙ for n ≥ 4. The residue/PSLQ route is walled
  (`ZETA7_RESIDUE_I3.md` §2: N ≳ 10⁴⁰ terms for PSLQ-grade I′₃); direct high-precision Iₙ is
  walled by the same N^{−p} convergence. So the **primitive operator L̃ remains unhuntable
  by data-fitting** — there is no P/I′ data to fit, and `salvage_v6_recur.py`'s
  multi-sequence trick needs sequences it cannot be given. STATE §11 item 2 stays open, but
  **it no longer gates the sector question**, which section A settles without it.
- The one cheap thing L̃-adjacent that *is* now known: `den(P_n^{L-prop})/d_n^7 ∈ {107, 321}`
  constant — the false P is a clean L-solution, so any L̃ must differ from L in a way that
  changes the constant-term arithmetic without changing q, s, P̂.

---

## H. Residual dependency, stated honestly

Everything above is unconditional **except** step 2 (s, P̂ ∈ sol(L)), which rests on:
(i) L is the true operator for qₙ — empirically certified on 74 exact terms, **not proved**
(no CT certificate exists, STATE §11 item 1); and (ii) the 141-term `d_n^5` denominator
ledger + control experiment of section B. I regard (ii) as decisive evidence for step 2
*given* (i). If L itself were wrong, the whole char-poly framework (including sector A)
would collapse too — so no route to a sector-A pass runs through doubting L.

I found **no evidence whatsoever** pointing toward sector A, and one new structural argument
(section A step 7) that rules it out given the ladder.
