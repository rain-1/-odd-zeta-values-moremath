# KZ_ELLIPTIC_REPORT — Project C literature deliverable (verified, ready to execute)

**2026-08-05.  Opus research-agent deliverable, fetch-verified; archived for
the Project C execution session.**  Sources actually read: arXiv:2111.08796
(tex + PDF + published BAMS PDF, diffed), arXiv:2109.12972, 2108.06586,
2011.03400, the Almkvist–van Straten–Zudilin Fields Inst. paper, LMFDB 32.a.

## Headlines

* **Exactly one construction in the literature realizes elliptic L-values as
  Apéry limits**: Koutschan–Zudilin, "Apéry limits for elliptic L-values",
  Bull. Aust. Math. Soc. 106:2 (2022) 273–279 (arXiv:2111.08796).
  Chamberland–Straub, Almkvist–van Straten–Zudilin, and Zudilin's 2021
  preprints contain none (grep-verified; Zudilin 2109.12972's limits are
  Dirichlet L-values).
* Seed: J_n(z) = ∫∫ x^{n−1/2}(1−x)^{n−1/2}y^{n−1/2}(1−y)^n(1−zxy)^{−n−1/2}
  = Γ-quotient · ₃F₂(n+½,n+½,n+½; 2n+1, 2n+3/2 | z).  **Half-integer
  hypergeometric world — the same (2n±1)-structure as Zudilin's Catalan
  recurrence** (this is the key structural fact for our program; see
  CATALAN_CONTROL.md §4).
* Periods: λ(z) = J₀ (Mahler-measure period), ρ₁ = π·₂F₁(½,½;1|z) (imaginary
  period ~ central L-value of a twist), ρ₂ (quasi-period mix).
* Order-3 recurrence for J_n (verbatim in the agent transcript / paper eq.);
  the Apéry-limit pair (A_n, B_n) = 2×2 minors of consecutive (a,b,c)
  coefficient triples satisfies the **exterior-square order-3 recurrence**
  (verbatim in paper), with
  lim B_n/A_n = λ(z)/ρ₁(z).
* **z = 1/2 (k = 2√2): conductor-32 CM curve** (Cremona 32a1 = LMFDB 32.a4,
  newform 32.2.a.a = η(4τ)²η(8τ)²):
  λ(1/2) = 16√2 L(E,2)/π,  ρ₁(1/2) = 4√2 L(E,1);
  B_n/A_n → 4L(E,2)/(πL(E,1)) = 1.7812349412405498670 (agent reproduced to
  19 digits by exact iteration from the printed initial data
  A: 26, 146, 171368/25, …; B: 0, 2494/9, 2743456/225, …).
* **z = 1/16 (k = 1): conductor 15** (15a8, newform 15.2.a.a =
  η₁η₃η₅η₁₅): λ = 30L(E,2)/π; **the paper's ρ₁(1/16) = ½L(E,χ₋₄,1) is
  wrong by a factor 4** — agent verified ρ₁(1/16) = 2L(E,χ₋₄,1) two
  independent ways (twist level 240, ε = +1).  Corrected limit:
  B_n/A_n → 15L(E,2)/(πL(E,χ₋₄,1)) = 1.9785915526594892295.
* Integrality (experimental in the paper): z^n2^{4n}a_n,
  z^n2^{4n}D_{2n}²{b_n,c_n} ∈ ℤ; z^{2n+2}2^{2n}D_{2n}(n+1)(2n+1)²A_n,
  z^{2n+2}2^{2n}D_{2n}²(n+1)(2n+1)²B_n ∈ ℤ (A-claim needs n ≥ 1 — second
  agent-caught erratum).  Weak Apéry limits only; no irrationality.
* For k > 4 a fourth-order family exists but the recurrence is unprinted
  ("does not meet any reasonable aesthetic requirements") — unavailable.

## Project C execution plan (next session)

The full recurrences and initial data are in the agent transcript
(session task aad…/a9a… outputs) and the paper; the z = 1/2 CM case is the
first target.  The program's question, sharpened by Projects B and D:

> The KZ integrands carry the same half-integer indicial structure that
> put Zudilin's Catalan recurrence OUTSIDE the modular-anchor class
> (CATALAN_CONTROL.md).  Prediction: the KZ operator's canonical nome will
> also fail integrality — i.e. the known elliptic Apéry limits are
> hypergeometric-realized, NOT cuspidal-modular-realized; whereas our
> eps62 construction (CUSPIDAL_COMPANION.md) realizes cuspidal L-values
> *inside* the modular class on Apéry's curve.  Testing this cleanly
> separates "which constants" from "which mechanism".  If instead the KZ
> z = 1/2 CM case rectifies modularly (CM might save it — level 32 is in
> our CUSP dictionary as (η₂η₄)⁴'s home at weight 4, and 32.2.a.a is its
> weight-2 sibling), that would be the first bridge between the two worlds.

---

## Project C EXECUTED (same day, third arc continuation) — verdict

`work/z5eps/eps64_kz32.py`, series order 30.  The z = 1/2 (conductor-32
CM) exterior-square recurrence, transcribed from the paper and cross-
checked against the agent's exact table (A₃ = 2033916/5, A₄ =
18919290512/675, B₃ = 380414354/525 — PASS):

* **Universal layer holds**: L(y_B) = (924027/32)·t exactly (pure
  boundary defect); L(y_A) = (243165/16)t + (18888309/2)t² (A is a minor
  sequence, own defect).
* **Modular rectification FAILS, maximally**: the canonical nome has
  denominators 1352, 1.7e13, 1.9e25, … at n = 2,3,4 — no integralizing
  rescale (exhaustive ±2^a3^b5^c, |a|≤10, |b|≤4, |c|≤3).  Indicial
  polynomial factors as
  θ·(θ+1)²·(2θ−1)²·(2θ+1)²·(apparent quartics):
  the half-integer double pairs AND — stronger than the Catalan case —
  exponent 0 is only SIMPLE, so no Frobenius log-partner exists at 0 and
  the canonical coordinate is not even well-founded.

**Sol's distinction is now a verified fact, including in the CM case:**
"the limit is an L-value of a modular form" does NOT imply "the
recurrence is modularly rectifiable."  The hoped-for CM bridge at level
32 does not exist at the level of the canonical coordinate.  The
taxonomy (universal / modular / hypergeometric / bridge?) stands with
the bridge cell still empty — and our eps62 cuspidal companion remains
the only known construction realizing modular-form L-values inside the
modular class.
