# EPS_DISCOVERY — the curve-atom scanner as a companion-formula discovery instrument

**Session:** 2026-08-04 (Fable + build agent).  Code: `work/z5eps/eps41.py`,
`eps42.py`, `eps43.py` + logs; positives in `eps43_{franel,D}_{eps2,eps3}.pkl`.
Labels follow programme convention; nothing here is claimed beyond its label.

## 1. The instrument

A *curve atom* is a polynomial curve in the summand's argument space,
`(n,k[,l]) + u₁ε + u₂ε² [+ u₃ε³]`; its cell expansion is
`S·exp(Σ_m ε^m Λ_m)` with Λ_m from the validated letter d-maps, and
γ-constants cancel because the `S₁`-forms `Σ_L p_L d_L` vanish identically
(all families; asserted per atom).  ζ-constants enter through graded blocks.
The scanner asks, per ε-order r: does a rational combination of atoms satisfy
the pinning (`[ε¹]=0` per ζ-grade, etc.) with `[ε^r] = b·B(n) + a·A(n)`,
`b ≠ 0`?  Positives are then rationally reconstructed and verified exactly
over ℚ; the standard of claim is *discovery* (conjecture-grade), not proof.

## 2. Validation: the controls rediscover their companions `[VERIFIED exact ℚ, n ≤ 25]`

* **Franel** `S = C(n,k)³` and **D** `S = C(n,k)²C(n+k,n)`: the known
  companions are rediscovered from **linear atoms alone**, minimal support
  (2 atoms), all ζ-graded block identities verified exactly over ℚ for
  `n ≤ 25`, at both primes 4194301/4194247.  The discovered weights differ
  from the published ones by **null weights** (`Σ S·diff = 0`, exact,
  `n ≤ 20`) — i.e. new equivalent representations, same companions.
* Both controls also reach `B(n)` at ε³ via quadratic curves (exact-ℚ
  verified) — reachability at multiple orders.

The discovery loop is therefore validated end-to-end on ground truth.

## 3. The finding: a character-linked reachability dichotomy `[MEASURED, 2 primes; conjecture-grade]`

| family | χ | limit | companion reachable? |
|---|---|---|---|
| Franel | 1 | ζ(2)/4 | **YES** (linear, ε²) |
| D | 1 | ζ(2)/5 | **YES** (linear, ε²) |
| **B** (Zagier f) | χ₋₃ | none | **NO** (lin+quad, ε²&ε³) |
| δ | 1* | none | **NO** (lin+quad, ε²&ε³) |
| ζ (double sum) | χ₋₃ | L(χ₋₃,3)/3 | **NO** (lin+quad, ε²&ε³) |

(*δ carries χ=1 in the fifteen-pair table but has no Apéry limit.)

Exactly the three families for which the sporadics paper *proved* no
harmonic-weight fit exists (rank = columns; `papers_out/sporadics`,
§seven) are also unreachable by the deformation mechanism at linear and
quadratic curve depth — in the rational part and every ζ-graded component,
at both primes, at both ε-orders.  The reachable families are principal
character with real ζ(2)-limits; the unreachable ones have non-principal
character or no archimedean limit.

**Reading (conjectural):** the ε-deformation mechanism generates companions
precisely in the principal-character / convergent sector.  This answers the
paper's open problem **P6** ("deformations as a source of letters") in the
*negative* for exactly the three families it was hoped to help — and
sharpens it: the obstruction is not the fit alphabet (P6's diagnosis) but
appears to be arithmetic (character/limit-linked).  It is also consonant
with the weight-5 finding of `BRIDGE_CAMPAIGN_2026-08-03.md` §5b: there,
too, the deformation sector reaches one row (P̂) and is structurally blind
to the next (P).

## 4. Honest limits of the negatives

Curve depth ≤ 2 (≤ 3 at weight 5), direction boxes `{−2..2}`/`{−1..1}`,
`n ≤ 28`, two 22-bit primes.  Deeper curves, larger boxes, or atoms outside
the diagonal argument space (e.g. Gorodetsky constant-term representations,
which Proposition prop:C already showed are *necessary* for family C) are
not excluded.  The natural next probe for B/δ/ζ is constant-term-kernel
atoms rather than binomial-cell atoms.

## 4b. eps44 — the three fits the sporadics paper never ran, now run `[EXCLUDED, 2 primes]`

The paper stated (l. 981–984) that full-degree coverage for ζ and η over
their complete tame alphabets, and for F at its seven tame arguments, "was
not made" (424–1088 columns).  `eps44.py` ran all three, pure and with
conductor-matched twisted letters (χ₋₃ for F, ζ; χ₅ for η), control-first
(Franel's known weight re-derived exactly, held-out ℚ-verified; the control
also caught an int64 overflow that would have corrupted all verdicts):

| run | cols | rank | excess | verdict |
|---|---|---|---|---|
| F pure / F+χ₋₃ | 35 / 119 | 23 / 75 | 105 / 173 | INCONSISTENT |
| ζ pure / ζ+χ₋₃ | 140 / 770 | 125 / 734 | 123 / 134 | INCONSISTENT |
| η pure / η+χ₅ | 418 / 2530 | 418 / 2530 | 90 / 108 | INCONSISTENT |

Identical ranks and verdicts at both primes.  **The Σ S·𝔴 harmonic ansatz
over complete tame alphabets, twisted letters included, is now exhausted at
full degree for all of the conjectural seven.**  Diagnostic corrections:
ζ *does* have summand–letter ℚ-relations at full degree (15-dim pure /
36-dim twisted kernel) — the old "rank = columns in every run" claim fails
for ζ — but B(n) lies outside the span; η genuinely has rank = columns
even at 2530 columns (the maximally rigid case).  Next ansatz change, per
the programme's own recommendation and Proposition prop:C's necessity
result: Gorodetsky constant-term letters, or rational-function
coefficients.

## 5. What is genuinely new here

1. A validated, reusable **discovery instrument** (scan → reconstruct →
   exact-ℚ verify) that rediscovers known companions from scratch.
2. Two new (equivalent-by-null) representations of the Franel and D
   companions, exact-ℚ verified.
3. A two-prime, two-order, two-depth **reachability dichotomy** aligned
   with character/limit arithmetic — new conjecture-grade structure on the
   fifteen pairs, and a concrete negative resolution direction for P6.
