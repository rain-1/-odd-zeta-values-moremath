# Weight-five bridge campaign — session of 2026-08-03 (Fable)

**Task:** `FABLE_COMPACT_BRIDGE_PROMPT.md` — prove `(BRIDGE)  S_n = P_n`.
**Verdict: NOT YET PROVED.**  This file records the strongest exact
reduction obtained (a single explicit 231-monomial identity), four new sharp
negatives, and the recommended next certificate problem.  No finite check is
reported as a proof anywhere below.

## 1. The new exact reduction — the bridge is one explicit identity wide

`work/z5eps/eps31.py` computes, at the eps27 generator level (rank 426), the
echelon residual of `sym(Δ₅)` against the span of all proved one-variable
generators, at two independent 22-bit primes (4194301, 4194247) with matching
pivot patterns, CRT-combines and rationally reconstructs it.  Result
(`work/z5eps/eps31_residual.pkl`):

> an explicit weight-5 form `r` with **231 monomials, exact rational
> coefficients** (degree profile `{(1,1,3):72, (1,1,1,2):58, (1,2,2):60,
> (1,4):22, (2,3):16, (5,):3}`), k↔l symmetric, such that
>
> * `sym(Δ₅) − r` lies in the span of the proved generator alphabet
>   (mod both primes; exact-ℚ lift is mechanical and remains to be written
>   out — the combination is over the calibrated eps24–eps27 alphabet);
> * `ΣΣ_{k,l} T·r = 0` exactly for `n ≤ 5` (and inherits all-`n` truth from
>   `ΣΣT·Δ₅ = 0` *if* that is true — it is the same one-dimensional gap).
>
> **Proving `ΣΣ_{k,l} T(n,k,l)·r(n,k,l) = 0` for all n closes the Δ₅
> bridge** `ΣT·B₅ = (33/4)·ΣT·w₅^sym`.

This is the narrowest formulation of the gap to date: everything else in
`Δ₅` is proved-generator material.

Caveat kept explicit: closing Δ₅ gives `ΣT·B₅ = (33/4)·ΣT·w₅^sym`, which is
**not yet** `(BRIDGE)`; see §4.

## 2. New sharp negatives (all two-sided: calibrated positives, exact ranks)

Throughout, prime 4194301 (22-bit; NB `2147483647` overflows int64 in the
row dot-products — eps26 must be run at the small prime).

1. **eps27** — elementary-symmetric pole-cancellation jets on the two
   *simple-zero endpoint ranges* `A=(0,k]`, `C=(n,n+k]` and their union
   (the families eps26 lacked).  174 generators, all calibrate.  Rank
   424 → 426.  `sym(Δ₅)` still **exactly one** dimension outside.
   With eps26's middle-range and full-multiset elementaries this exhausts
   every unweighted elementary/power-sum pole-cancellation family on the
   Barnes kernel.
2. **eps28** — *z-weighted jets* `Σ_l Res[R_k·z·ρ] = 0` (valid: `R_k ~ z⁻²`,
   `decay(ρ) ≥ 1`; the residues need an extended ring with polynomial
   letters `l`,`k` coupling to a weight-6 harmonic layer; 24 624 extended
   monomials in play).  2030 generators, all calibrate.  Non-saturated
   3200-dim projections, two seeds: rank 1497, with target 1498 —
   **still exactly one dimension outside**.
3. **eps28b** — z²-weighted jets and z-weighted value/derivative towers
   (2429 further calibrated generators, 48 704 extended monomials):
   projection rank 2714, with target 2715 — **still exactly one outside**.
3b. **eps32** — *nested (harmonic-weighted) jets*: blocks
   `Σ_j H_j^{(r)}/(z−j)` (both weight orientations) and
   `Σ_{i∈A/B/C} H_i^{(r)}/(z+i)`, residues carrying nested letters
   `ν_{r,s}`, `μ^{A/B/C}_{r,s}`.  258 generators, 0 calibration failures,
   pure-ring rank 426 → 675 — **still exactly one outside** (two
   projections).  This was the last family class predicted by the prompt
   ("weighted or nested endpoint jet"); both are now implemented and both
   leave the same one-dimensional residual.
3c. **eps33** — saturation stress: `sym(Δ₅) ∈ sym(ker Φ₅)` re-tested at
   `n ≤ 75` (2926 rows): rank of the antisym-restricted system stays
   exactly **1673**, membership **HOLDS**.  So a per-row completion is
   robust; the miss is inside the constructive alphabet, not in the
   membership claim.
4. **t_deep_r** — the sharp closed-subsystem necessary condition for an
   order-zero telescoping certificate `T·r = Δ_k(Tρ) + Δ_l(Tσ)` applied to
   the residual `r` itself: **NOT reachable** at inflation depths 1–3,
   denominator families G1–G3, for three distinct maximal monomials `m0`,
   with zero nullity at the deepest runs (`work/z5ord0/t_deep_r.log`).
   An order-zero certificate for this representative, within the
   `mk-weight ≤ 1` ansatz class, does not exist.

Reading of the pattern: **six** independent mechanism classes (fixed-pole
jets/towers, anti-diagonal family, all elementary-symmetric cancellations,
z- and z²-weighted jets, nested jets, capped order-zero telescoping on the
residual) each miss the target by exactly one dimension.  Since eps33 shows
the per-row membership is genuinely saturated, the missing direction IS
per-row realisable — but apparently not by any local residue functional of
the Barnes kernel in the classes above.  The live hypotheses now:

* deeper nested structure (nested×nested products, shuffle syzygies,
  mixed-orientation nested weights `H_{i−k}`, `H_{n−i}` on the ranges —
  the eps32 alphabet was minimal);
* an *uncapped* telescoping certificate for the residual (mk-weight 2 with
  the explicit `(n−k)^{-2}`-vanishing boundary condition, or an order-2
  pre-operator in one variable — the mechanism that closed ζ(2));
* a transformation from Zudilin's proved one-variable partial fractions
  (Route C), where the recurrence side is already theorems.

## 3. Fixed/It-was-checked

* eps26 rerun at the correct prime reproduces: rank 424, one outside.
* All calibrations 0 failures (1675, 1849, 4459 generator checks).
* `ΣΣT·Δ₅ = 0` exact for n ≤ 5; Δ₅ expansion == direct Bell defect n ≤ 4.

## 4. Attachment audit (what Δ₅-closure would and would not give)

* Brown–Zudilin (CellZeta, §2) **prove**
  `I_n = Q_n(2ζ5+4ζ3ζ2) − 4P̂_n ζ2 − 2P_n` via a Koutschan telescoping
  certificate, and identify `P_n = (−1)^{n+1}p_n/binom(2n,n)` with
  Zudilin's proved one-variable forms.  The recurrence side is safe.
* The universal Barnes integrals have **constant** top-weight coefficients:
  `[ζ5]I^{2,2} = 2`, `[ζ2ζ3]I^{2,2} = ∓4` (sign convention per
  `universal.py`), all others 0, for all `(a,b)` — checked symbolically for
  `a,b ≤ 2` and structurally forced (top-weight parts of the tails don't
  see `(a,b)`).  So in the Barnes display only the **rational** coefficient
  is a nontrivial obligation; with §7 (proved ζ4/ζ3/ζ2 rows) the whole
  chain `ΣT·w₅^sym = P_n` reduces to
  (i) the contour→residue-grid descent `J_n = ΣT·W_B` (documented
  §§1–4 of Z5CF_BARNES; the assembly step should be written out with decay
  estimates before being cited as proved), and
  (ii) the weight-5 rational identity — whose defect `Δ_B = [1]W_B +
  2w₅^sym` lives in a **nested** letter ring (the rational parts of the
  universal integrals contain `Σ_{t≤k} H_{t+l}/t^r`), i.e. the same nested
  extension that eps32 would build.  One build, two targets.
* The ε-route alternative (`ΣT·B₅ = (33/4)P_n` directly) remains
  verification-only; its analytic proof would need the deformed-parameter
  integral representation (Krattenthaler–Rivoal style) and is not started.

## 5. Recommended next actions

1. **eps32 — nested jets.**  Blocks `NQ_r = Σ_j H_j^{(r)}/(z−j)` (and the
   endpoint-nested `Σ_{i∈A∪C} H^{(r)}_i/(z+i)`), extended ring with letters
   `ν_{r,s}`/`μ_{r,s}`, lazy index, same projection tests; targets **both**
   `sym(Δ₅)` and (after building `[1]W_B` in the nested ring) `sym(Δ_B)`.
2. If eps32 closes Δ₅: exact extraction (eps29 pipeline), then the
   full generator-derivation write-up (§12.3-style at weight 5).
3. If eps32 also misses by one: treat that as evidence for the second
   hypothesis in §2 and attack the residual `r` with an *uncapped*
   telescoping ansatz (mk-weight 2 with the explicit `(n−k)^{-2}`
   vanishing condition — the flagged unimplemented boundary case in
   `Z5_ORDER0` §4.2), or with a second-order (pre-operator) telescoper in
   one variable, the mechanism that worked for ζ(2).

## 5b. The ε-analytic route (opened 2026-08-04)

Strategy: avoid polynomial certificates entirely by expressing the companion
rows as ε-Taylor coefficients of honest meromorphic deformations of the BZ
integral, where the analytic side is classical contour analysis.

* **New sharp negative:** the tabulated family-1 deformation is NOT
  realizable as a gamma product with reasonable shifts.  The integer-moment
  lattice conditions (e.g. `Σc_j(j⁴−j²) ≡ 0 mod 12`) force the shift scale
  `δ = ε/N` with `120 | N`, and the minimal integer multiplicities are
  ~10¹¹ (`work/z5eps/eps40_gate.py` + inline solver).  So the family's
  letters `k, l, n±k, n±l` are essentially non-meromorphic data; only the
  `k+l / n+k+l` letters are clean (single `−2ε` shift — the undressed
  l-shift).  Any analytic proof must therefore change representative.
* **Correct formulation:** work with *argument-shift atoms*
  `T(n+αε, k+βε, l+γε)`, `(α,β,γ)` small integers.  Each atom is
  automatically meromorphic and equals BZ's parametric integrand at
  ε-shifted parameters, so BZ/Zudilin continuous-parameter machinery
  applies directly.  Linear combinations of atoms span a richer space of
  ε-coefficient rows than single exp-dressed families.  The decisive
  question (eps41, running): does some ℚ-combination of atoms satisfy the
  pinning `[ε¹]=[ε²]=0`, `[ε³] ∈ ⟨Q,P̂⟩`, `[ε⁵] = b·P + ⟨Q,P̂⟩` with
  `b ≠ 0`?  If yes, the bridge becomes: (i) finite algebra (the atom
  combination's Bell rows — machine-checkable), plus (ii) one classical
  analytic theorem about `I(a+εv)` expansions — no certificates.
  If `b` is forced to 0, that is a structural obstruction worth recording.

* **RESULT (eps41/eps42, agent-run, both primes 4194301/4194247): the
  obstruction is real and total.**  For directional atoms (linear curves,
  124), quadratic curves (3374) and cubic curves (5102), under the pinning
  `[ε¹]=[ε²]=0`, `[ε³] ∈ ⟨Q,P̂⟩` (with or without an `[ε⁴]` span
  condition), the ε⁵ row of every pinned combination is **confined to
  `span{Q, P̂}` — the `P`-component is forced to 0 in the rational part
  and in every ζ-graded component** (for linear atoms the ε⁵ row vanishes
  entirely; quadratic/cubic atoms can reach `P̂` and ζ(3)-graded `Q` at ε⁵
  but never `P`), while the ε³ P̂-coefficient remains free.  Ranks/dims identical at both
  primes (`work/z5eps/eps41.log`, `eps42.log`; validation of the Bell/ζ
  bookkeeping against independent mpmath Cauchy-Taylor expansion to 30
  digits).  **Conclusion:** Taylor deformations of the T-cell along
  polynomial curves in `(n,k,l)` see the ζ(3)-row and are structurally
  blind to the ζ(5)-row; the only known ε⁵→P-emitting deformation
  (family 1) is exactly the one that is not meromorphically realizable
  (the δ=ε/120, ~10¹¹-multiplicity obstruction above).  The two negatives
  are two faces of one fact: the weight-5 companion is not reachable from
  the analytic deformation sector of the diagonal kernel — a new,
  prime-independent structural boundary for the program.  Any analytic
  route must therefore change the *kernel* (non-diagonal parameter curves
  in the full 8-parameter BZ family, or boundary/telescoping sources),
  not just the deformation.

## 6. Files added this session

| file | what |
|---|---|
| `work/z5eps/eps27.py` | endpoint-range elementary jets (rank 426) |
| `work/z5eps/eps28.py` (+`eps28_wf.pkl`) | z-weighted jets, extended ring, projection tests |
| `work/z5eps/eps28b.py` | z² jets + z-weighted towers |
| `work/z5eps/eps29.py` | exact-extraction pipeline (ready; unused until a span closes) |
| `work/z5eps/eps31.py` (+`eps31_residual.pkl`) | **the 231-monomial residual identity** |
| `work/z5ord0/t_deep_r.py` | order-zero necessary condition on the residual |
