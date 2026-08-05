# KZ_ERRATA_NOTE — two errata in Koutschan–Zudilin, "Apéry limits for elliptic L-values" (BAMS 106 (2022) 273–279)

**2026-08-05.  Independently verified per Sol's directive (derivations +
numerical checks, two ways each) before any public communication.  Both
errata are present in arXiv:2111.08796v1 AND the published BAMS text.**

## Erratum 1 (factor 4): ρ₁(1/16) = 2·L(E,χ₋₄,1), not ½·L(E,χ₋₄,1)

Paper's claim (k=1, z=1/16, conductor-15 curve): ρ₁(1/16) = ½L(E,χ₋₄,1).

Verification here (`work/z5eps/` inline, session log):
* ρ₁(z) = π·₂F₁(½,½;1|z) evaluated directly (mpmath, 60 dps):
  ρ₁(1/16) = 3.192484444263567020297938143…
* L(E,χ₋₄,1) computed from the newform 15.2.a.a = η₁η₃η₅η₁₅ (q-expansion
  built exactly from the eta product to n = 4000; a₁…a₁₂ =
  1,−1,−1,−1,1,1,0,3,1,−1,−4,1 ✓), twisted coefficients aₙχ₋₄(n) at level
  240, weight 2, ε = +1, via the completed-L incomplete-Γ formula:
  L(E,χ₋₄,1) = 1.596242222131783510148969072…
* Ratio: ρ₁(1/16)/L(E,χ₋₄,1) = 2.0 with residual |ρ₁ − 2L| < 4×10⁻⁶¹.
  Cross-check by exponentially smoothed Dirichlet series (T = 800):
  1.59502… (agrees to smoothing accuracy).  The paper's ½ gives residual
  2.394 — excluded.
* The same discrepancy was found independently by a separate research
  agent using a different smoothing (T = 100, 200) before this
  verification: three independent evaluations agree.

Corrected limit statement for z = 1/16:
  B_n/A_n → 15·L(E,2)/(π·L(E,χ₋₄,1)) = 1.9785915526594892295…
(The λ(1/16) = 30L(E,2)/π identity checks as printed; only ρ₁ is off.)

## Erratum 2 (range): the A_n-integrality claim needs n ≥ 1

Paper (experimental inclusion): z^{2n+2}2^{2n}D_{2n}(n+1)(2n+1)²A_n ∈ ℤ
"for n = 0,1,2,…".  At n = 0, z = 1/2: the expression equals
(1/4)·1·1·1·1·26 = 13/2 ∉ ℤ.  The claim holds (checked z = 1/2, n = 1…8)
for n ≥ 1.

## Status

Both errata verified to the program's standard; suitable for a polite
communication to the authors.  Drafting/sending an email is a user
decision, not done here.
