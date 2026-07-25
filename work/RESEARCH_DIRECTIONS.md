# Research directions — zeta-math-2, drafted 2026-07-24 (Fable, orchestrator)

Synthesis of: orchestrator experiments (ORCHESTRATOR_NOTES.md), the ζ(3) warmup
(WARMUP_ZETA3_DWORK.md), and the three study memos (STUDY_DWORK_TECH.md,
STUDY_BROWN_WING.md, STUDY_QUANTITATIVE_WING.md). Zudilin-window warmup and
the adversarial verification of the ζ(3) proof pending at draft time.

Evidence classes as in the sibling repo: [FORMAL]/[THM]/[COMP]/[CONJ]/[OPEN].

## The headline discovery of the day

**A second-solution Lucas congruence family, apparently new at every weight:**
for Apéry-like pairs (a_n, b_n) of weight w (b_n/a_n → the constant),

    (LB_w)   p^w · b_{ap+r} ≡ b_a · a_r   (mod p),      p ≥ 5,

with master integer form p^w b_n a_q ≡ b_q a_n (mod p^w), q = ⌊n/p⌋.

Status:
- w = 3 (Apéry ζ(3)): single-digit (LB_3) **[THM — adversarially verified,
  VERIFY_ZETA3_PROOF.md: T2 & T3 CONFIRMED, 0 counterexamples, 3 write-up
  compressions to expand]** — proved elementary, self-contained
  (WARMUP_ZETA3_DWORK.md T3); mod-p³ master form [COMP, floor exactly 3,
  0 failures, p ≤ 31, n ≤ 320].
- w = 1, 2 (log 2 / Delannoy; ζ(2) Apéry): [COMP] at all previously-failing
  sites; ratio-form failures fully explained by p | (Lucas factor).
- w = 5 (Brown–Zudilin cellular (Q_n, P_n), BZ's printed normalization with
  Q_0 = 1, P_0 = 0): **(LB_5) p⁵·P_{ap+r} ≡ P_a·Q_r (mod p)** — [COMP, zero
  failures, all cells n ≤ 45, p = 7..19 incl. exceptional p = 7, uniform
  plus sign; bz_lucas_final.py]. Iterated, it implies the (CB) inequality =
  the last open gate of the sibling campaign's sharp-12 denominator theorem.
  (P2 first move — sign pinning — DONE 2026-07-24.)
- Literature (STUDY_DWORK_TECH.md): second-solution row proved NOWHERE;
  closest object is Beukers–Vlasenko Dwork crystals III **Conjecture 7.5**
  (open, "one of our original motivations"); integral-row congruences are
  classical (Gessel/Straub et al.).

## Ranked programme

**P1. [in progress] Harden (LB_3):** adversarial verification; then the
mod-p³ master form and multi-digit induction. Deliverable: a short standalone
paper ("A Lucas congruence for the second Apéry solution", or similar) —
new theorem about the most-studied sequence in irrationality theory, and the
base case of everything below. Route for mod-p³: H-part is already mod p³;
need (★) mod p³ — Wolstenholme-grade refinements of the T3 ledger.

**P2. The weight-5 port ⇒ close the sibling campaign's Phase 2 [OPEN → THM].**
Target: ε(p)-normalized p⁵ P_{ap+r} ≡ ± P_a Q_r (mod p) for the BZ pair,
p ≥ 5. Obstacles (from T4 assessment): rank-3 filtration (P̂_n cross-terms),
no known Apéry-style single-sum for P_n, asymmetric summand C(n,k)²C(n+k,k)
(half the Kummer slack), κ-dependence. Two routes: (i) find the explicit
harmonic decomposition of P_n (BZ §MZV decomposition + the sibling's Barnes
kernel work) and port the elementary ledger; (ii) rank-3 Dwork-crystal /
ε-deformation route (STUDY_DWORK_TECH.md route (B)). Payoff: completes the
first denominator theorem for M̄₀,₈ cellular periods (sibling results 3–5
become a full [THM]), corrects a published claim, and realises Brown 2026's
"congruences in de Rham cohomology" expectation. First move either way:
resolve the sign convention against BZ's actual integer normalization.

**P3. General theorem (LB_w) for a class of pairs [CONJ → THM].** The w = 1,2
data (center quadratic-character structure, exceptional digits) plus the flat
mechanism of the T3 proof suggest: for any "Apéry-like" pair whose summand is
a product of Lucas-factorizable binomial powers with harmonic companion of
weight w, (LB_w) holds for p ≥ 5. Candidate scope: the 15 sporadic sequences
(Straub's list) with their standard companions; Zudilin's window forms (T4 of
the Zudilin warmup, pending). This would be the clean citable theorem — and
resolves the coefficient form of BV Conjecture 7.5 for this class.

**P4. Refereeing-grade verifications with real stakes (quantitative wing):**
(a) Lai 2024 Claim 4 (κ₃ ≤ 75) — unrefereed record, margin 0.006; (b)
Lai–Zhou window 35 — margin 0.649/16780. Either confirms a record or finds
an error; both cheap relative to value. Secondary: joint (M,J,δ) search past
Lai 2025's 1.2846 (marginal expected gain).

**P5. Brown 2026 seams (STUDY_BROWN_WING.md):** (a) the p-adic determinant
denominator law on M₀,₅ (Remark 56) — fully finite, foundational for the
p-adic side; (b) first Sup²·δ measurement for ζ(5)/M̄₀,₈ (measurement only —
the parasitic ζ(2) bars a new theorem); (c) ~~weight-7 γ₅,₇~~ **CLOSED
NEGATIVE 2026-07-24 (work/LTILDE_HUNT.md): sector A excluded by a positivity
argument (I′ₙ = Iₙ + ζ₂|I″ₙ|, sum of positives ⟹ |I′ₙ| ≥ ζ₂|I″ₙ| rides
ρ_B), γ₅,₇ ≤ 0.34 (ratio) / 0.71 (BZ form), κ = 7 measured tight, RV-orbit
leverage (+28.6% at weight 5) is 7× short of the +196% needed — orbit
optimization on M₀,₁₀ not worth running**; (d) extend the convergent-cellular
count 𝒞_N past N = 11 (clean enumerative deliverable).

**P6 (NEW, deep): the middle-root phenomenon.** Calibration finding from the
sector hunt: at weight 5 the BZ operator has λ₁ = 0.0050038 < e⁻⁵ — a
minimal solution decaying FAST ENOUGH TO PROVE ζ(5) IRRATIONAL — but the
actual linear form Qζ₅−P rides the MIDDLE root λ₂ (C₀ = log λ₂, confirmed on
361 exact terms, all sign combinations ±ζ₂ζ₃); weight 7 reproduces this
exactly. Apéry's ζ(3) form rides its minimal root; cellular forms
systematically don't. Conjecture-shaped question: the ζ(2)-elimination is a
Betti-lattice rotation (the July Bernoulli-24/index-2 mechanism) that moves
the class off the minimal ray — understand WHICH constructions ride their
minimal root and what obstructs it. This is Brown's "what are those other
representations?" made quantitative, and it is now the sharpest known
formulation of the whole obstruction. Also: I′₃ pinned unconditionally
(4 s.f.); sharp-12 confirmed 361/361 at n ≤ 360 (and ¬6·d⁵: sharpness).

**Explicitly NOT pursued** (SURVEY.md verdicts stand): direct ζ(5) attacks;
constant-sharpening for its own sake; p-adic analogues as standalone;
arithmetic holonomicity (CDT); Rhin–Viola group search. MZV wing: Vasilyev is
a closed theorem (do not cite as open); llm/32 is off the irrationality axis.

## Why this is the right shape

The SURVEY's central finding was "every search-shaped direction optimizes the
non-binding constraint; the binding constraint is new constructions, which
have no search surface." The (LB_w) family evades that dichotomy: it is not a
search over constructions but a *structural theorem about the constructions
we already have* — exactly the "what does this machinery also prove" framing
the SURVEY prescribes — with a finite-verification surface (congruences),
elementary proof technology that demonstrably works (T3), a named open
conjecture it feeds (BV 7.5), and a concrete campaign it completes (Phase 2).
