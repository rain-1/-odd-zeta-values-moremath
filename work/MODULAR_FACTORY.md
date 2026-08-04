# MODULAR_FACTORY — the companion construction run in reverse

**Fork deliverable, 2026-08-04/05.**  Scripts: `work/z5eps/eps55_factory.py`
(pass 1), `eps55b_deep.py` (pass 2); catalogs `eps55_catalog.json`,
`eps55b_pass2.json`; log `eps55.log`.  All arithmetic exact (`int`/`Fraction`)
except the sweep prefilter (mod 4194301, numpy); every classification below
was re-derived exactly at series order 46.  Labels per programme convention.

## 1. The factory

Forward map (validated this session, eps48–52): family → hauptmodul `t(q)` +
weight-w form `F(q)` with `y₀(t) = F(q(t))`.  Reverse map (this memo): pick a
level `N` and a candidate pair from banks of eta products
`t = q·∏(1−q^{mk})^{e_m}` (Σe = 0, Σm·e = 24), `F = ∏(1−q^{mk})^{e_m}`
(Σe = 2w, Σm·e = 0, w ∈ {1,2}), plus Eisenstein members
`(d₂E₂(q^{d₂})−d₁E₂(q^{d₁}))/(d₂−d₁)` and odd-character weight-1 series
`E₁(χ₋₃), E₁(χ₋₄)` at rescalings, plus the `(−q)`-twist
`t̃(q) = −t(−q), F̃ = F(−q)` of every pair (the family-B phenomenon).
Then `a_n := [tⁿ] F(q(t))` (automatically **integral** for integer banks:
reversion and composition of monic integer series), and the pair is a hit iff
`a_n` satisfies a 3-term recurrence with polynomial coefficients of degree
≤ 4 (mod-p nullspace prefilter; exact confirmation).  Hits are fingerprinted
by the scaling+twist invariants `a_k/a₁^k` (quotients by `t → λt` and
`t → −t`), matched against the fifteen (R2/R3 parameter recovery is exact),
and — when new — profiled: companion `B(n)` by the recurrence,
`d_n^w`-denominator class.

## 2. Controls `[VERIFIED exact ℚ, order 46]`

The factory reproduces, from the session's identified `(t, F)` data alone,
the exact recurrences of **all ten identified eta-type families**:

γ→(17,5,1,0), A→(7,2,−8), ζ→(9,3,−27,0), δ→(7,3,81,0), α→(10,4,64,0),
ε→(12,4,16,0), C→(10,3,9), E→(12,4,32), F→(17,6,72), η→(11,5,125,0).

(The Apéry numbers 1, 5, 73, 1445, 33001, … materialize from
`q·(η₁η₆/η₂η₃)¹²` and `(η₂η₃)⁷/(η₁η₆)⁵` with no recurrence input.)
10/10 MATCH — the reverse pipeline is faithful.

## 3. The sweep

Pass 1: caps 12 t-candidates, 24 F-candidates/weight, Σ|e| ≤ 26; pass 2:
24 t, 48 F/weight, Σ|e| ≤ 60 (reaching the region containing the known
large vectors, Σ|e| = 48–60).  Levels {2,…,10, 12, 13, 16, 18, 20, 25};
both twists; ~50,000 pairs total; 91 distinct hit classes.

### 3.1 Rediscovered sporadics (inside the sweep corner)
η (via a level-5 representative), F (6), E (8), **B (via an untwisted
level-9 representative** — an equivalent of the level-36/b(−q) data**)**,
ζ (9) — with their exact (twist-equivalent) parameters.  The other knowns
live outside even the pass-2 corner as bank vectors and are covered by §2.

### 3.2 New 3-term integral hits: all classical degenerates `[PROVED by
recognition, exact]`
Every integer-parameter 3-term hit not among the fifteen is degenerate in
Zagier's sense:

| hit | parameters | identification | degeneracy |
|---|---|---|---|
| level 4 | R2(−16,−4,0) | `a_n = (−1)ⁿ\binom{2n}{n}²` | c = 0 (hypergeometric) |
| level 4 | R3(−16,−8,256,0) | Cauchy square of the above | composite (GF²) |
| level 4 | R3(0,0,64,0) | interleaved `(−1)^m\binom{2m}{m}³` | a=b=0 (2-step) |
| level 8 | R2(0,0,16) | interleaved `(−1)^m\binom{2m}{m}²` | a=b=0 (2-step) |
| level 4 (pass 2) | R2(−32,−12,256) | — | **a²−4c = 0** (double char root) |

plus sparse step-`s` interleavings at levels 16/18 (a₁ = 0 classes) and
~60 hit classes with no integer R2/R3 shape (rational-parameter or
higher-shape objects; catalogued, not pursued).

### 3.3 Headline (a classification-flavored negative)
**Within ~50,000 swept pairs across fifteen genus-zero-type levels, both
twists, weights 1–2, the factory's 3-term integral output is exactly: the
known sporadic zoo + the classical degenerate families.  No sixteenth
sporadic pair exists in the explored corner.**  This is consistent with —
and is the first systematic occupancy scan supporting, by this method —
the expectation that Zagier's six / AZ's six are complete at their weights
for eta-type parametrizations at these levels.  Honest limits: candidate
caps and Σ|e| bounds as stated; generalized-eta (Γ₁-type, needed for
family D), Fricke/Atkin–Lehner hauptmoduls (needed, presumably, for
Cooper's aperiodic three), weight-3 forms (4-term/order-4 territory), and
levels > 25 are **not** covered — these are the four named directions where
a sixteenth pair could still hide.

## 4. What the factory adds beyond the negative

1. **Faithfulness**: the ten control reconstructions are themselves new
   exact statements (recurrence recovered from modular data with no
   recurrence input) — the constructive half of the dictionary.
2. **B at level 9**: the sweep found an untwisted level-9 representative
   equivalent to family B's anomalous level-36/`b(−q)` data — a cleaner
   home for B's parametrization worth recording for the ASD work.
3. **Machinery**: `eps55_factory.py` is a reusable reverse-pipeline
   (banks → recurrence → arithmetic) for any future (level, weight) cell,
   including the four unexplored directions above.

## 5. Recommended next steps (not attempted here)

* Generalized-eta banks (Γ₁(N) data) — would put family D inside the sweep
  and open the `s₇/s₁₀/s₁₈` aperiodic question properly;
* Atkin–Lehner/Fricke hauptmoduls for the `N+` groups;
* weight-3 banks with 4-term shape-matching (Cooper's `Sporadic order-4`
  territory);
* raise level ceiling past 25 with the same caps discipline.
