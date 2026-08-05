# PROGRAM CLOSEOUT — River's odd-zeta program, July 16–27, 2026

**This is the "what is what" document.** One entry per result, with its evidence
label and where it lives. Depth is in the linked ledgers, not here.

Labels (the program's own discipline):
**[LEAN]** kernel-verified, no sorries · **[PROVED]** paper proof exists ·
**[THM]** proved + adversarially refereed · **[VERIFIED n≤N]** exact
computation over a range, *never* treated as proof · **[EXCLUDED]** proved
negative · **[OPEN]** open, with its sharpest known formulation.

## Addendum — August 5, 2026 (Sol's Φ-source program, flagship steps 1–2, 4)

* **All twelve identifiable sporadic companion sources Φ = tσ^r/(PF) are pure
  weight-(r+1) Eisenstein series [VERIFIED q^60, held-out band q^27–60]** —
  explicit divisor-sum coefficient laws per family, no cuspidal component
  anywhere; γ and D recover Beukers's classical ζ(3)/ζ(2) pictures from the
  recurrence alone; ζ's source is the primitive (χ₋₃,χ₋₃) weight-4 level-9
  Eisenstein with coefficient 1.  Cooper's three remain coordinate-obstructed.
* **All nine Apéry limits reproduced from the sources alone** via the fold
  connection formula ξ = Θ(q_c) + FΘ′/F′ (γ to 6.6e−15).  The three
  "no-limit" families are the complex-fold (CM-adjacent) cases; their
  canonical complex Eichler limits are computed to 15–39 digits and are
  apparently **new constants** (PSLQ-negative over natural L-value bases).
  Ledger: `work/PHI_SOURCE_LEDGER.md`; scripts eps60–eps61b.

## Addendum — August 2, 2026

* **Franel and s10 companion closed forms [LEAN].** The symmetric harmonic formulas for the
  canonical recurrence solutions are now proved with explicit all-boundary telescoping
  certificates in `lean/ZetaLucas/FranelClosedForm.lean`. The same file proves that the old
  Franel sum used by `bFranel_lucas` is exactly the recurrence-defined companion and adds the
  missing s10 instance of `theorem_LB`. Consequently both canonical solutions satisfy their
  weight-two Lucas laws (Franel for odd primes; s10 for primes not dividing 10). Proof and
  provenance ledger: `work/FRANEL_S10_LEAN.md`.

The two repositories:

| repo | campaign | contents |
|---|---|---|
| `~/fable-episode-2/zeta-math` | July 16–20 | the Lean "one of ζ(5)…ζ(33)" theorem, sharp-12/Phase-2 congruence campaign, worthiness/ notes |
| `~/fable-episode-2/zeta-math-2` (this repo) | July 24–27 | everything below: 37-paper LLM corpus (`llm/`, `INDEX.md`), session outputs (`work/`), papers (`papers_out/`, root `.tex`), Lean (`lean/ZetaLucas`) |

---

## 1. The flagship theorems

* **"At least one of ζ(5), ζ(7), …, ζ(33) is irrational" [LEAN]** — Zudilin's
  elementary route, formalized end-to-end, zero sorries. (repo 1)
* **The sharp-12 denominator theorem for the BZ ζ(5) family, p ≥ 5** — the
  arXiv:2210.03391 integrality claims are off by exactly 12; the corrected law
  was conjectured, then reduced, then **every mathematical node closed**:
  (A1-MID) band theorem, Q-row Lucas, (GAP-DESC), (BASE)/nucleus — see
  `work/PHASE2_*.md`, paper in `papers_out/sharp12` (45pp). Remaining pieces are
  mechanical certificate runs, recorded in PHASE2_FINAL. (repo 1 → repo 2)
* **Lucas congruence for the SECOND Apéry ζ(3) solution [THM, apparently new]:**
  `p³·b_{ap+r} ≡ b_a·a_r (mod p)`, p ≥ 5 — literature covers the integral row
  only. `work/WARMUP_ZETA3_DWORK.md`, referee pass `VERIFY_ZETA3_PROOF.md`,
  paper `papers_out/lucas2nd` (39pp).
* **The two-level matrix law for ζ(3) [THM]** — the full digit-transition
  matrix `(a_n, p³b_n) ≡ (a_a, b_a)·[[u, p³b_r],[0,u]] (mod p³)` with
  `u = a_r + 2paU_r + p²a²X_p(r)`; mechanism = one rational function + the
  residue theorem over ℂ and over 𝔽_p (the carry region is the complement of
  the pole divisor — the vanishing can never be a rational identity).
  `work/APERY_DEFECT.md`, `work/APERY_GAP.md`, paper `papers_out/frobenius*`.
* **The χ-twisted general Lucas theorem (LB_w^χ) [PROVED]** — the naive law is
  FALSE for 7/15 sporadic pairs; the universal law carries the Dirichlet
  character of the Apéry limit. Theorem LB under (H1)–(H5) + four proved
  instances. `work/LBW_GENERAL.md`; Lean instances in `lean/ZetaLucas`.
* **The compact Brown–Zudilin closed forms** (this repo's last arc):
  - `P̂_n = Σ T·ŵ₃`, ŵ₃ = H³_{n+k} − Ψ·H²_{n+k} **[PROVED]** — Barnes kernel +
    (I3) descent + Zudilin 2002 Lemma 4; no linear-independence input.
  - `P_n = −½ Σ T·[1]W_B` **[PROVED]** — the *subtraction anchor*: once the
    middle row is a theorem, the two evaluations of the real number I_n cancel
    transcendentally and the rational parts must agree. New closed form for
    the top row.
  - `P_n = Σ T·w₅` (3-term compact form) **[OPEN = exactly identity (T3)]**,
    see §4.
  Complete proofs: **`bz_compact_weights_proofs.tex`** (root). Why the weights
  are what they are: `brown_zudilin_laurent_jet_origin.tex` (anti-diagonal
  Laurent jets; the direction that kills the coupled factor).

## 2. The structural discoveries (each changed the program's direction)

* **Bare vs difference alphabets** (`work/ZETA5_CLOSEDFORM.md`): every earlier
  search lived in difference alphabets; Apéry's own minimal weight is bare.
  The compact forms live in the bare alphabet — 27 monomials instead of 178.
* **The ε-deformation exists** (`work/Z5CF_EPSILON.md`): T_ε = T·exp(ΣεᵐL_m)
  with Σ T_ε = Q + ε³tP̂ + ε⁴X + ε⁵(t²/4+8t)P; the compact weights are Bell
  coefficients of one Γ-deformation; C(ε) carries odd zetas only — the
  archimedean face of the Γ_p tower. [VERIFIED exact n≤16, mod-p n≤80]
* **Weight = obstruction, exactly** (`work/APERY_DEFECT.md` (d),(e)): the
  ζ-weight enters as the ε-order of one deformation AND as the p-adic depth
  loss at digit boundaries; closed form, remainder, p-adic scalar and
  Frobenius constants are coefficients of ONE object.
* **The purity defect is a Tate twist [PROVED]**: c = −3/π² = 12/(2πi)²;
  the minimal ray is the unpurified cellular integral (`work/DEFECT_IDENTIFY.md`).
  Primitive κ₅ = (514/87)ζ(5) is PURE (`work/GAMMA_UNIFICATION.md`).
* **The p-adic Apéry limit knows the entire odd ζ_p tower at once**
  (`work/LAMBDA_HUNT.md`); the p-adic/archimedean mirror: archimedean constants
  tame, p-adic constants carry the tower; Transfer Principle [PROVED, new]
  (`work/DIG_GROUP.md`); the naive "one ratio two completions" slogan REFUTED
  (`work/PADIC_SEAM.md`).
* **The middle-root phenomenon (P6)**: at weight 5 a minimal solution fast
  enough for ζ(5)-irrationality EXISTS; cellular forms ride the middle root.
  The sharpest known form of the obstruction. (memory + ORCHESTRATOR_NOTES)

## 3. Proved negatives worth keeping (they are assets)

* "One of ζ(5), ζ(7)" via the symmetric M₀,₁₀ family: **CLOSED NEGATIVE**
  (`work/LTILDE_HUNT.md`).
* Tameness fails structurally at weight 5 (n+k reaches 2n); no tame
  representative at any degree (`work/ZETA5_CLOSEDFORM.md` §4).
* L_BZ is NOT a telescoper of T·ŵ₃; the minimal one has order 7
  (`work/Z5CF_TELESCOPER.md`); the order-7 route is excluded for Lean.
* The order-0 bridge T(w★−ŵ₃) = Δ_kR+Δ_lS is impossible; bridges have order ≥ 4.
* p-adic irrationality is not reachable from these families (DIG ledger:
  best margins ≈ −E; Bel's criterion cost and the δ-support are disjoint).
* **(T3)'s value-grid certificate class is refuted** (this session): no
  cellwise certificate with fixed letter coefficients over the entire
  local/residue calculus — rank saturates ≈ 3500 while the deficit grows with
  rows (`work/Z5T3_BRIDGE.md` §4–4b).

## 4. The open problems, ranked (at close)

1. **(T3)** `Σ T·([1]W_B + 2w₅^sym) = 0` — the ONLY gap between the anchor and
   the compact top row. The campaign is specced: creative telescoping with
   ℚ(n,k,l) coefficients over the U-letter module (rational shift closure
   proved; two-stage 1-variable CT). `work/Z5T3_BRIDGE.md` §4b.
2. **The (DWORK) cubic gate** (repo 1): p⁵(P_n/Q_n) ≡ P_a/Q_a (mod p) — needs
   the P-column of the one-digit Frobenius connection matrix; recurrence +
   Casoratian provably insufficient. `zeta-math/worthiness/PHASE2_ADJUGATE_*`.
3. **The two DIG lemmas + the missing 3 + Theorem B** — `work/OPEN_PROBLEMS.md`
   Tier 1 (the ranked successor ledger; read it first if returning).
4. Lean gaps: `KeyPoly` kernel check (per-declaration split, bounded 5.13 GB);
   `BZRec PStarSum`; the (B-bot) gauge re-lift (task L10, ~1.5h).

## 5. Papers and artifacts

* `papers_out/`: **lucas2nd** (39pp), **sharp12** (45pp), **padiclimits**
  (31pp), **frobenius** + **frobenius_matrix** (26pp), **padicmap** (41pp),
  plus lucas_min, lucas2nd_short, z5partial — all drafted → bibliography-
  verified → hostilely refereed → repaired. Author blocks await River.
  (NB: APERY_GAP §7 lists a sign-typo edit for frobenius_matrix — applied
  status recorded there.)
* Root: `bz_compact_weights_proofs.tex` (+pdf), `brown_zudilin_laurent_jet_origin.tex`.
* Blog essay "The Price of Purity" (claude.ai artifact, id in memory),
  landscape map, method essay (`work/METHOD_ESSAY.md`).
* `harmonic-fun/`: external — the Liu–Zhang ζ(3)-irrationality Lean
  formalization + Aristotle auto-formalization experiments on the Apéry
  closed-form notes (River's exploration; not program output).

## 6. Lean state (`lean/ZetaLucas`, repo 2)

Sorry-free & axiom-clean: `apery_lucas`, `Q_lucas` (+digit forms),
`PadicBridge`, Lemma K, **`theorem_LB`** (the abstract χ-twisted theorem),
instances `bMin_lucas`, `bFranel_lucas`; `Reflect.lean` (288-line reflective
sparse checker — the `ring`-replacement; memory-flat). Quarantined sorries:
`KeyPoly` (BZQRow) and `BZRec PStarSum` (BZStar). Repo-1 Lean: the flagship
theorem. **Standing lesson: `#print axioms` cannot detect a false undischarged
hypothesis** — KeyPoly was false-as-stated and everything downstream was
"clean"; only discharge attempts catch this. House rule: no certificate
reaches the kernel without a faithful outside-Lean re-implementation.

## 7. Method (what made it work — keep these)

Exact arithmetic before any claim; evidence labels on everything; finite
checks are never proof; fetch-before-cite (confabulation at the boundary of
the known is the endemic failure mode); never attack ζ(5) directly — ask what
the machinery also proves; bounded negatives are deliverables; the k↔l
symmetrization pays repeatedly; watch for basis-dependence (Euler/product
splits agree only modulo shuffles); pre-simulate kernel computations in
Python; keep collaboration channels append-only (`work/agent_channel/`, Sol).

## 8. If this is ever picked up again — the three sharpest entry points

1. Run the **T3 creative-telescoping campaign** (`work/Z5T3_BRIDGE.md` §4b) —
   one bounded computation from the compact top row, which would finish
   `bz_compact_weights_proofs.tex` unconditionally.
2. Read `work/OPEN_PROBLEMS.md` (Tier 1) — the DIG lemmas unify the
   archimedean/p-adic mirror.
3. The **middle-root question (P6)**: why do cellular constructions ride the
   middle root while Apéry's rides the minimal one? The answer would say what
   a ζ(5)-proof would even look like.

*Closed 2026-07-27. All work committed on master; git identity pinned local
(rain1). Session reports: `work/SESSION_REPORT_2026-07-26.md` and the ledgers
named above.*
