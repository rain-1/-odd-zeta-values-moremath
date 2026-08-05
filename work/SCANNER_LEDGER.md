# SCANNER_LEDGER — the modular irrationality scanner, first full run

**Session 2026-08-05 (sixth arc).**  Executes Sol's scanner proposal
(share 6a730d0a-…) with River's directive.  Scripts:
`work/z5eps/eps65_scanner.py` + session inline runs.  Question: does
there exist a level where the Apéry race (e^r < |t_c′|) is winnable AND
the odd cusp space S_{r+1}^− ≠ 0 — the "cuspidal-Apéry cell"?

## 1. Method

For each level with a standard integral eta-quotient hauptmodul t:
the operator's singular values are the critical values of t, i.e. t at
zeros of σ/t = (1/24)Σ_m e_m·m·E₂(q^m) — found by seeded Newton over the
complex disk (real folds AND the complex second classes).  Validation
anchors reproduced exactly: level 8 → ε's (0.0429, |1.457|); level 20 →
η's complex fold 0.088 ± 0.016i; level 5 symmetric ±1/√5-scale; level 6,
12 known from the family operators (0.0294/33.97 and 1/16/1/4).

## 2. The table (r = 3 score e³/|t_c′| ≈ 20.09/|t_c′|; win iff < 1)

| N | dim S₄ | t_c | |t_c′| | score₃ | verdict |
|---|---|---|---|---|---|
| 2, 3, 4, 5, 7, 9, 13, 25 | 0–5 | ±√κ symmetric | = |t_c| | — | **no analytic gain** (t ↦ κ/t; fold tied with conjugate) |
| 6 | 1 | 0.0294 | **33.97** | **0.59** | **WIN — but S₄⁻(Γ₀(6)) = 0 (f₆ is Fricke-even)** |
| 8 | 1 | 0.0429 | 1.457 | 13.8 | fail |
| 10 | 3 | 0.0557 | 1.000 | 20.09 | fail (exactly e³ — boundary curiosity) |
| 12 | 3 | 0.0625 | 0.25 | 80 | fail (Domb: our L(f₆,3)/2 apparatus) |
| 14 | 4 | 0.1497 | 1.000 | 20.09 | fail (boundary curiosity again) |
| 15 | 4 | 0.2011 | 0.726 | 27.7 | fail |
| 18 | 5 | 0.0895 | <~1 | ≫1 | fail (second class not fully resolved; scale rules out win) |
| 20 | 6 | complex fold | — | — | excluded (no real AL fold) |
| 24 | 8 | 0.0981 | 0.545 | 36.8 | fail |

(r = 2 score e²/|t_c′|: also no winner; the classical D-family win at
level 5 lives in the Γ₁(5)-asymmetric normalization, not the symmetric
eta one — see §4.)

## 3. Verdict

**Within the natural search domain — standard integral eta hauptmoduln,
levels ≤ 25 — the cuspidal-Apéry cell is EMPTY.**  Level 6 is the unique
r = 3 race winner and its odd cusp space vanishes; every level with odd
cusp forms loses the race by a factor ≥ 4.  Apéry's ζ(3) apparatus is,
in this precise sense, the unique odd-vanishing race-winning
construction in its class — and it is Eisenstein because it has to be.

Two boundary curiosities for the record: levels 10 and 14 sit at score
EXACTLY e³ (|t_c′| = 1.000 to all computed digits — the conjugate class
on the unit t-circle).  A denominator improvement of any ε > 0 at these
levels (d_n^{3−ε}-type gains, cf. the sporadic "deflation" phenomena)
would tip them over.  dim S₄ = 3 and 4 there, so odd cusp vectors are
available (parities unverified).  **These are the sharpest targets the
scan produced:**

> **(S-1)** Determine the exact odd-cusp dimensions at levels 10, 14 and
> whether any integral normalization/auxiliary-source choice (Sol routes
> 2–5) achieves denominator growth strictly below e³ⁿ.  Score exactly 1
> means the race is decided entirely by arithmetic, not analysis.

## 4. The normalization lesson

The prime-level symmetric hauptmoduln (t ↦ κ/t) give |t_c| = |t_c′|:
zero analytic gain by construction.  The classical ζ(2) win at level 5
exists only in the Γ₁(5) (asymmetric) normalization where |t_c′|/|t_c|
= φ¹⁰ ≈ 123.  So the race score is NOT an invariant of the level — it is
an invariant of the *integral normalization of the hauptmodul*, and the
true optimization domain is the lattice of integral Möbius changes of t
(each trading singularity positions against denominator growth).  This
is exactly Sol's "extremal function" formulation, now with data.

## 5. Honest limits

Search bounded: levels ≤ 25, one standard hauptmodul each (except level
5's two normalizations, which straddle the win/no-gain line — proof of
non-invariance); zero-finding seeded (levels 6, 12, 18 second classes
taken from known operators / scale estimates, not fresh zeros); odd-part
dimensions of S₄ not split (only needed at 10, 14 — open S-1); r = 2
weight-3-with-character spaces not scanned; d_n^r-cost assumed
(cuspidal denominators only observed, never proved).
