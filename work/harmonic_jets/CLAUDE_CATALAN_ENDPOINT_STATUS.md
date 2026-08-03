# Catalan endpoint / sharp-denominator formalization — progress log

## UPDATE (this session, 2026-08-03): Stage D and Stage E FULLY COMPLETED, real Lean
## code written and compiled. `lean/ZetaLucas/CatalanEndpoint.lean` grew from 1155 to
## ~1580 lines. `lean/ZetaLucas.lean` now imports `ZetaLucas.CatalanEndpoint`. A full
## `lake build` is in progress as this update is written (single serialized instance,
## checked via `ps aux | grep lean` before each invocation) — an earlier attempt at a
## full `lake build` (which rebuilds the *entire* project, not just this file) hit an
## unrelated `Lean exited with code 137` (OOM kill) on `ZetaLucas/BZQRow.lean`, a
## pre-existing file this session did not touch; a clean single-instance retry is
## underway and `CatalanEndpoint` itself has already replayed cleanly (`[8677/8680]
## Replayed ZetaLucas.CatalanEndpoint`, warnings only, no errors) in the run that hit the
## later unrelated OOM. This confirms the new file itself is not the problem.

### Direct answer to "what does the corrected Stage D plan mean / did you find a fix for
### `card_even_odd_diff_le_one_multiples`?"

`card_even_odd_diff_le_one_multiples` was **already fully proved** (no sorry) by a prior
session, sitting unused at the end of the file. This session's job was to consume it: use
it to bound, for every prime power `p^i`, the difference between `endpointDen`'s and
`endpointNum`'s `p`-adic valuations. That assembly (the "corrected Stage D plan" in the
previous log entry) is the part that had **not** been formalized yet at the start of this
session — it is now done. Concretely, this session:

1. Proved a new generic lemma (not previously in the file or, as far as targeted
   searches found, in mathlib under another name):
   ```lean
   theorem factorization_prod_eq_sum_card {p : ℕ} (hp : p.Prime) (s : Finset ℕ)
       (hs : ∀ x ∈ s, x ≠ 0) (b : ℕ) (hb : ∀ x ∈ s, Nat.log p x < b) :
       (∏ x ∈ s, x).factorization p = ∑ i ∈ Finset.Ico 1 b, (s.filter (p ^ i ∣ ·)).card
   ```
   via `Nat.factorization_eq_card_pow_dvd_of_lt` (confirmed present at
   `Mathlib/Data/Nat/Factorization/Basic.lean:432`) applied per-element plus a
   `Finset.sum_comm` swap.
2. Proved `endpointNum_eq_prod_filter` / `endpointDen_eq_prod_filter`: reindexing the
   `Finset.range`-product definitions of `endpointNum`/`endpointDen` into products over
   parity-filters of `Finset.Icc (j+1) n`, exactly per the plan in the previous log entry
   (no double-counting).
3. Proved `den_num_card_bound`: for each `(p,i)`, the count of `p^i`-multiples in the
   `Den`-parity-class of `Icc (j+1) n` exceeds the `Num`-parity-class count by at most 1,
   by case-splitting on the parity of `j` and invoking the correct conjunct of
   `card_even_odd_diff_le_one_multiples (p^i) (j+1) n`.
4. Proved `endpointDen_val_le_odd`: for odd primes `p`,
   `v_p(Den) ≤ v_p(Num) + p.log n`, combining 1–3 with `Finset.sum_le_sum`.
5. Proved `endpointDen_val_le_two`: `v_2(Den) ≤ n - 1`, via `endpointDen n j ∣ n!`
   (`Finset.prod_dvd_prod_of_subset`) and `Nat.sub_one_mul_factorization_factorial`
   (confirmed present, `Mathlib/Data/Nat/Choose/Factorization.lean`) plus a digit-sum
   positivity argument (`Nat.getLast_digit_ne_zero`, `List.single_le_sum`).
6. Assembled **`endpointDen_dvd`** (the `DIV` target), by reducing to
   `Nat.factorization_le_iff_dvd` + `Finsupp.le_def` and case-splitting on `p = 2` vs odd
   prime vs non-prime.
7. Cast to ℚ: **`endpointR_lcm_integral`** (`RL`), by extracting the witness from `DIV`
   and clearing denominators with `field_simp`/`linear_combination`.

All of 1–7 compile with **exit 0**, verified via
`lake env lean ZetaLucas/CatalanEndpoint.lean` (serialized, `ps aux | grep lean` checked
empty beforehand each time).

### Stage E (also newly completed this session)

- `ratInt_sum`: closure of `∃ z:ℤ, x = z` under finite `Finset` sums (simple induction).
- `catalanSumR_lcm_sq_integral`, then **`catalanT_lcm_sq_integral`** (`SHARP for T`):
  `(lcmUpto n)^2 * catalanT n` is an integer, via `TSQ` (`catalanT_square_formula`,
  already in the file) plus `endpointR_lcm_integral` termwise.
- `lcmUpto_dvd_lcmUpto`: `k ≤ n → lcmUpto k ∣ lcmUpto n`, via `Finset.lcm_dvd`/
  `Finset.dvd_lcm` on the `Icc 1 k ⊆ Icc 1 n` containment.
- A **from-scratch general binomial inversion theorem** (mathlib has no ready-made
  version of this shape — checked `Mathlib/Data/Nat/Choose/Sum.lean`, only
  `Int.alternating_sum_range_choose` and friends, not the two-sided scaled inversion
  needed here):
  ```lean
  theorem binom_inv_general (B T : ℕ → ℚ) (c : ℚ)
      (hT : ∀ k, T k = ∑ i ∈ Finset.range (k + 1), (k.choose i : ℚ) * (-c) ^ (k - i) * B i)
      (n : ℕ) :
      ∑ k ∈ Finset.range (n + 1), (n.choose k : ℚ) * c ^ (n - k) * T k = B n
  ```
  proved via: a reusable triangular-double-sum-swap lemma (`sum_range_triangle_swap`,
  using `Finset.sum_Ico_eq_sum_range` and an indicator/filter argument — this was the
  fiddliest part, several iterations to get the `Finset.filter`/`Finset.sum_filter`
  bookkeeping right); a Vandermonde-identity collapse lemma (`inner_sum_collapse`, using
  `Nat.choose_mul {n k s} (hsk : s ≤ k) : n.choose k * k.choose s = n.choose s * (n -
  s).choose (k - s)`, confirmed present at `Mathlib/Data/Nat/Choose/Basic.lean:159`, plus
  the binomial theorem `add_pow (-c) c (n-i)` collapsing to `0^(n-i)`). Specialized this
  to `catalanB`/`catalanT`/`c=4` to get **`catalan_binomial_inversion`** (`INV`).
- **`catalanB_sharp_denominator`** (`SHARP`, the primary target): assembled from `INV`,
  `catalanT_lcm_sq_integral`, `lcmUpto_dvd_lcmUpto`, and `ratInt_sum`, exactly as planned.

All of Stage E also compiles with exit 0 in `lake env lean ZetaLucas/CatalanEndpoint.lean`
(whole-file check, run repeatedly after each addition).

### Current exact status (verify freshness before trusting further)

- `lake env lean ZetaLucas/CatalanEndpoint.lean`: **EXIT 0**, only pre-existing lint
  warnings (unused simp args / no-op push_cast, all predating this session, all in
  Stage A/B code) plus one new lint warning (`hiN` unused variable, harmless).
- `rg -n '\bsorry\b|\badmit\b|^\s*axiom\b' ZetaLucas/CatalanEndpoint.lean` returns exactly
  one line, a mention of the word "sorry" inside a doc comment — **no real placeholders**.
- `lean/ZetaLucas.lean` now has `import ZetaLucas.CatalanEndpoint` appended (root import
  done, per priority-list step 6).
- Full-project `lake build`: **CatalanEndpoint.lean itself confirmed green inside a
  `lake build`; the rest of the pre-existing project did not finish building in this
  session's available time, for reasons unrelated to this work.** Timeline: a first
  attempt (default parallelism) hit `Lean exited with code 137` on the *unrelated,
  pre-existing* `ZetaLucas/BZQRow.lean` (which this session did not modify) — an OOM
  kill from over-parallel compilation. A second, single-instance serialized retry
  (confirmed via `ps aux | grep lean` that only one `lake build` process was running)
  again replayed `CatalanEndpoint` cleanly (`[8677/8680] Replayed
  ZetaLucas.CatalanEndpoint`, warnings only, no errors) and then reached
  `ZetaLucas/BZQRow.lean`, where the single `lean` subprocess ran for 30+ minutes at
  ~98% CPU and ~8.3 GB RSS with its cumulative CPU `TIME` barely advancing over repeated
  checks spaced ~20+ minutes apart (e.g. 32:26 → 32:49 CPU-minutes across a ~20+ minute
  wall-clock gap) — i.e. it is essentially stalled/thrashing, not merely slow, and not
  progressing toward completion in any reasonable time budget. System memory stayed
  healthy throughout (~10 GB available, no swim into swap beyond a small pre-existing
  ~940 MB), so this is not a repeat of the earlier OOM; it looks like a pathological
  elaboration/thrashing case in `BZQRow.lean` itself (a large pre-existing
  Brown–Zudilin file, untouched by this session), independent of `CatalanEndpoint.lean`.
  **Conclusion: this is an environment/pre-existing-file issue, not a correctness issue
  with the Catalan-endpoint work.** The deliverable (`CatalanEndpoint.lean` compiling
  standalone via `lake env lean`, and replaying cleanly as a build target inside `lake
  build` up to and including its own target) is verified independently of whether
  `BZQRow.lean` ever finishes. A future session should investigate `BZQRow.lean`
  separately (it is unrelated to the Catalan endpoint program) before re-attempting a
  full `lake build`.

**Strongest fully-compiled theorem so far, exact signature:**
```lean
theorem catalanB_sharp_denominator (n : ℕ) :
    ∃ z : ℤ, (Nat.lcmUpto n : ℚ) ^ 2 * catalanB n = z
```
This is the file's primary target (`SHARP`), fully proved with no placeholders, confirmed
by direct `lake env lean` on the file.

### Files touched this session

- `lean/ZetaLucas/CatalanEndpoint.lean` — extended (Stage D completion + all of Stage E).
- `lean/ZetaLucas.lean` — added `import ZetaLucas.CatalanEndpoint`.
- `work/harmonic_jets/CLAUDE_CATALAN_ENDPOINT_STATUS.md` — this file.
- Scratch files `lean/ZetaLucas/DScratch.lean`, `lean/ZetaLucas/EScratch.lean`,
  `lean/ZetaLucas/Check.lean` were used to develop/test pieces in isolation and were
  **deleted** after their content was merged into `CatalanEndpoint.lean`; none remain.

### Remaining work

Only the full-project `lake build` confirmation remains (step 6 of the priority list,
partially done: import added, build in progress). No further Lean *content* work is
outstanding for the must-have list (steps 1–6). The optional generalizations (steps 7–10
in the original prompt: parameter `b`, Proposition 6.12, generic binomial inversion
reuse, exponent optimality) have **not** been attempted and are explicitly out of scope
unless requested.

## UPDATE (follow-up session, 2026-08-03): stretch items 7/8/9 (as renumbered in the
## follow-up task — Prop 6.12 transport, generic binomial inversion, exponent
## optimality) investigated. No Lean file changes made; `CatalanEndpoint.lean` and
## `lean/ZetaLucas.lean` are untouched by this session.

**Item 8 (generic binomial inversion): already satisfied, no new work needed.**
`binom_inv_general` (line ~1544 of `ZetaLucas/CatalanEndpoint.lean`) is already a fully
generic, reusable theorem, not specialized to `catalanB`/`catalanT`/`c = 4`:
```lean
theorem binom_inv_general (B T : ℕ → ℚ) (c : ℚ)
    (hT : ∀ k, T k = ∑ i ∈ Finset.range (k + 1), (k.choose i : ℚ) * (-c) ^ (k - i) * B i)
    (n : ℕ) :
    ∑ k ∈ Finset.range (n + 1), (n.choose k : ℚ) * c ^ (n - k) * T k = B n
```
It quantifies over arbitrary `B T : ℕ → ℚ` and arbitrary `c : ℚ`; `catalan_binomial_inversion`
is simply this theorem applied at `B = catalanB`, `T = catalanT`, `c = 4`. Nothing further
to do here.

**Item 7 (Prop 6.12 general integer-`c` transport recurrence): investigated, not
attempted — genuinely large, correctly out of scope for this session.** Read
`papers_out/harmonic_jets/main.tex` lines 1105–1170, Proposition `prop:bintransport`
("binomial transport and its optimal acceleration", the paper's Prop 6.12 by numbering).
For a sequence `U` and `U^{[c]}_n = Σ_k C(n,k)(-c)^{n-k}U_k`, it states a *4-term, order-3*
recurrence
```
(n+1)²U[c]_{n+1} - (4-c)(3n²+3n+1)U[c]_n + (32-24c+3c²)n²U[c]_{n-1}
  + c(4-c)(8-c)n(n-1)U[c]_{n-2} = (RHS depending on U = A_E or B_E)
```
valid for *both* companions `A_E` and `B_E` of the harmonic pair, with the `c = 4` case
(where the `(4-c)` and `U[c]_{n-2}` terms vanish) reducing exactly to the already-proved
`TREC` (`catalanT_rec`) for `U = B_E = catalanB`.

Two independent reasons this was not attempted:
1. `A_E` (the paper's other companion, needed for the full statement "for `U = A_E` or
   `U = B_E`") is **not defined anywhere in the Lean project** — `catalanB` only plays
   the role of `B_E`. Formalizing the full proposition as stated would require building
   a second companion sequence and its own recurrence from scratch first.
2. Even restricted to the `B_E`/`catalanB` half only, the existing Stage-B machinery
   that proves `TREC` (`genTr`, `genTr_succ`, `genTrW1_eq`, `genTrW2_eq`, `genTrQ0_eq`,
   `genTrQ1_eq`, `genTrQ2_eq`, `catalanM`, `catalanM_wayA`, `catalanM_wayB`,
   `catalanT_rec_aux` — roughly lines 130–710 of the file) all hardcode the transform
   weight as the literal `(-4 : ℚ)`, not a parameter `c`. Re-deriving the order-3,
   4-term recurrence for general integer `c` is not a small edit: it requires
   reparametrizing `genTr` by `c`, redoing every shift-tower identity for the extra
   `U[c]_{n-2}` term (an additional shift `catalanY`-of-`catalanY`-level object beyond
   what Stage B currently tracks), and re-deriving the exact polynomial coefficients
   `(4-c)`, `(32-24c+3c²)`, `c(4-c)(8-c)` symbolically. The paper's own proof takes this
   shortcut via a generating-function substitution
   `U^{[c]}(z) = (1+cz)^{-1}U(z/(1+cz))`, which the top-level task instructions
   explicitly say to avoid formalizing in general (only the minimal needed OGF
   substitution, not full analytic generating-function machinery) — so a from-scratch
   finite-binomial-convolution proof, several hundred lines by the size of the existing
   `c = 4` precedent, would be needed.

Given the explicit guidance that a stretch item should be skipped cleanly rather than
forced when it is genuinely large, and given the trust rule preferring a smaller fully
proved result over a fragile large one, **item 7 was not attempted** this session. The
`c = 4` case is already fully proved (`catalanT_rec`); nothing dishonest or partial was
added in its place. A future session attempting this should scope it explicitly to the
`B_E`/`catalanB` half only (skip `A_E` entirely, since it doesn't exist yet) and budget
for reparametrizing the whole Stage-B shift-tower machinery by `c`.

**Item 9 (exponent optimality / Catalan Lucas congruence): skipped, congruence not
available in the codebase — per explicit instruction not to fabricate it.** Searched
`lean/` and `work/` for any existing formalization of the paper's
`thm:CatalanLucas` ("half-digit twisted Lucas law", `main.tex` lines 1172–1208):
```
p² B_E(ap+r) ≡ χ_{-4}(p) B_E(a) A_E(r)  (mod p)
```
Findings:
- The project *does* have a generic base-`p` Lucas-step toolkit
  (`lean/ZetaLucas/Core.lean`: `ZetaLucas.choose_digits`, `choose_carry_zero`) and several
  *unrelated* sequences' fully proved Lucas congruences built on top of it
  (`ZetaLucas/Apery.lean` — the Apéry `a`-row; `ZetaLucas/BrownZudilin.lean` — the `Q`-row;
  `ZetaLucas/FranelClosedForm.lean` — the Franel/`s₁₀` rows; `ZetaLucas/MinimalForm.lean` —
  the classical `b_n` row).
- None of these is the Catalan/`B_E` congruence, and `grep`/`rg` across `lean/` for any
  mention of `A_E`, `catalanA`, `χ_{-4}`/`chi_{-4}`, or a Catalan-specific Lucas theorem
  returns nothing. The statement exists only in the paper (`main.tex`), not in Lean.
- Per the follow-up task's explicit instruction — "do NOT assume or fabricate this
  congruence... if it doesn't exist, skip item 9 entirely" — **item 9 was skipped**.
  Proving `thm:CatalanLucas` from scratch would additionally require the undefined `A_E`
  companion and the paper's character-sum/monomial-weight machinery (`Lemma monomial`,
  `S_E`, `W`), none of which is in scope here.

### Files touched this follow-up session

None. This was a read-only investigation; no edits were made to `ZetaLucas/CatalanEndpoint.lean`,
`lean/ZetaLucas.lean`, or any other Lean file. Only this status file was updated.
