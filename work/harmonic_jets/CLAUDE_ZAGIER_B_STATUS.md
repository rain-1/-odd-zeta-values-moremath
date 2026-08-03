# Zagier-B endpoint companion — status log

File: `lean/ZetaLucas/ZagierBEndpoint.lean`. Added to `lean/ZetaLucas.lean`.

## Commands run
- `python3 work/harmonic_jets/verify_zagier_B_endpoint.py` — passes.
- `lake env lean ZetaLucas/ZagierBEndpoint.lean` — compiled cleanly for the file as it
  stood after Stage A/F (definitions, recurrence, uniqueness, transform, both finite
  witnesses). **Not yet re-checked** against the newly added `genTrC`/`genTrC_succ`/
  `genTrCW1_eq`/`genTrCW2_eq` block (added this round) — a full-project `lake build`
  has been occupying the only serialized Lean process (see below), so per the compile
  hygiene rule no second `lake env lean` has been run concurrently. This is the first
  thing to do once the build frees up.
- `rg -n '\bsorry\b|\badmit\b|^\s*axiom\b' ZetaLucas/ZagierBEndpoint.lean` — no matches
  (checked before this round's additions; the added block also contains no
  sorry/admit/axiom by construction — mechanical generalizations of already-compiled
  CatalanEndpoint.lean lemmas).
- `lake build ZetaLucas` — has been running for 9+ minutes on the pre-existing,
  unrelated `ZetaLucas/BZQRow.lean` (documented as 30+ min); the invocation was wrapped
  in `timeout 590` so it will self-terminate around the 10-minute mark without
  confirming completion. Per the coordinator's instruction this is not urgent/blocking;
  next step is to relaunch it unbounded in the background once the current one exits,
  and continue Lean edits only when no lean process is running (checked via
  `ps aux | grep -i lean` each time, per instructions).

## Compiled theorems (confirmed compiling before this round's additions)
1. `zagC : ℤ → ℕ → ℚ`, `zagC_rec`, `zagC_rec'`, `zagC_unique`.
2. `zagS : ℤ → ℕ → ℚ`, `zagS_zero`, `zagS_one`.
3. `zagC_six_eq`, `lcmUpto_six`, `lcmUpto_six_sq_mul_zagC_six`, `zagC6_forces_three_dvd`
   (**necessity direction**).
4. `zagC_two_eq_at_three`, `lcmUpto_two`, `zagC2_not_scaled_integral` (**optimality
   witness**).

## New this round (added, not yet test-compiled — build was occupied)
- `genTrC (c : ℚ) (a : ℕ → ℚ) (n : ℕ)` — the `c`-parametrized generalization of
  CatalanEndpoint.lean's `genTr` (which hard-codes weight `-4`); `zagS_eq_genTrC`
  identifies `zagS h n = genTrC (-(h:ℚ)) (zagC h) n`.
- `genTrC_succ` — the `c`-parametrized analogue of `genTr_succ`, proved by the same
  peel-and-reindex-forward technique with `-4` replaced by `c` throughout (mechanical
  port, low risk).
- `genTrCW1_eq`, `genTrCW2_eq` — `c`-parametrized analogues of `genTrW1_eq`/`genTrW2_eq`
  (weight-`k` and weight-`k(k-1)` Pascal reductions), same mechanical port.

## Item 2 (TREC) — algebraic scoping this round

Extended the sympy investigation (`work/harmonic_jets/derive_zagB_TREC3.py`) to scope
the "Way B" substitution precisely. Unlike `catalanB_rec` (constant coefficients `12`,
`32`), `zagC_rec`'s coefficients `h(3k²+3k+1)` and `3h²k²` are *quadratic* in `k`.
Checked symbolically that the decompositions
  `3k² + 3k + 1 = 3·k(k−1) + 6k + 1`  and  `k² = k(k−1) + k`
hold exactly, meaning Way B can be built from exactly the same two primitives
CatalanEndpoint.lean needed (weight-`k`, weight-`k(k-1)` Pascal reduction — now ported
above as `genTrCW1_eq`/`genTrCW2_eq`), just applied more times (to both `C` and a
`C`-shifted-by-`(-1)` sequence), rather than needing new degree-2 machinery.

**Still open / not yet derived:** the precise "Way A" vs "Way B" auxiliary sum `M_n`
and its two independent expansions that, equated via `linear_combination`, close TREC.
CatalanEndpoint.lean's `catalanM_n := Σ C(n,k)(-4)^{n-k}(k+1)²B_{k+1}` directly produced
a *lag-2* relation (`T_{n+1}` vs `T_{n-1}`) matching its target TREC. The zagB target
TREC has a *lag-3* relation (`S_n` vs `S_{n-3}`) despite `zagC`'s own recurrence being
lag-1 in index (relates `C_{k-1}, C_k, C_{k+1}`), because the generating-function
conjugation in the paper produces a `z³(θ+1)(θ+2)` operator (full cancellation of the
z¹,z² terms), unlike CatalanEndpoint's case which stayed order-2/lag-2 throughout. This
means the direct analogue of `catalanM` (built from `(k+1)²C_{k+1}`, naturally lag-1)
is *not* obviously the right auxiliary object for a lag-3 target, and finding the
correct one is an open research sub-problem, not a mechanical port. Candidates to try
next: (a) iterate the lag-1 `M`-type relation three times and eliminate the
intermediate lag-1/lag-2 objects (`V,W,Y,Z` shift-tower, 4 levels) algebraically; (b) a
directly-lag-3 auxiliary `M'_n := Σ C(n,k)(-h)^{n-k}·g(k)·C_{k+?}` for some cubic-ish
weight `g` chosen to make Way A/Way B match by construction — needs a fresh sympy
search analogous to `derive_zagB_TREC.py`/`TREC2.py` but seeded with a 4-level
shift-tower ansatz instead of the single-relation ansatz already ruled out.

## Priority-item status (of the 7 in the task brief)
1. Definitions/recurrence/uniqueness — **done**.
2. TREC — **partial infrastructure done** (`genTrC`, `genTrC_succ`, `genTrCW1_eq`,
   `genTrCW2_eq`, all mechanical `c`-parametrized ports); the Way-A/Way-B closure
   itself (the actual auxiliary-sum construction and `linear_combination` step) is
   **open**, and is now understood to be a genuine lag-3-vs-lag-1 structural mismatch,
   not just more bookkeeping — see above.
3. Finite endpoint formula — **not started**, depends on item 2.
4. Prime-power denominator lemmas — **not started**, depends on item 3.
5. Necessity via n=6 witness — **done** (`zagC6_forces_three_dvd`).
6. n=2 optimality witness — **done** (`zagC2_not_scaled_integral`); full iff / h=3
   corollary — **not done**, depends on items 2–4.
7. Root import — done; full `lake build` — in progress, not yet confirmed complete
   (blocked only by BZQRow.lean's known long compile time, not by this file).

## BREAKTHROUGH this round: a direct elimination certificate for TREC (supersedes the
## Way-A/Way-B / shift-tower plan above)

`lake env lean ZetaLucas/ZagierBEndpoint.lean` was confirmed clean (only linter
warnings, no errors) for the file including `genTrC`, `genTrC_succ`, `genTrCW1_eq`,
`genTrCW2_eq`. The full `lake build ZetaLucas` was relaunched unbounded in the
background (`nohup ... > /tmp/zagB_full_build.log 2>&1 &`) and is progressing normally
(currently on the pre-existing, unrelated, known-slow `BZQRow.lean`; being watched via
Monitor rather than idle-polled).

While waiting, found — via `work/harmonic_jets/derive_zagB_TREC4.py`/`TREC5.py`/
`TREC6.py` — a **much simpler route to TREC than the Way-A/Way-B auxiliary-sum
construction**: a direct, general-`n` linear elimination certificate, verified
symbolically (treating `C_0,...,C_n` as free symbols, no numeric `h`) for every
`n = 3, ..., 16`:

```
n² S_n + h³(n−2)(n−1) S_{n−3} − (−h)^{n−1}
  = Σ_{k=1}^{n−1} C(n−1,k) (−h)^{n−1−k} · rec_lhs(k)
    + (−1)ⁿ hⁿ · C₀ − (−1)ⁿ h^{n−1} · (C₁ − 1)
```
where `rec_lhs(k) := (k+1)² C_{k+1} − h(3k²+3k+1) C_k + 3h²k² C_{k−1}` is exactly the
residual of `zagC_rec` at index `k` (zero on the true sequence), and `S_n` is the
`zagS`-transform applied to the free symbols `C_0..C_n` (i.e. `Σ C(n,k)(−h)^{n−k}C_k`).

Since `rec_lhs(k) = 0` for all `k ≥ 1` (by `zagC_rec`) and `C_0 = 0`, `C_1 = 1` (by
`zagC_zero`/`zagC_one`), **the entire right-hand side vanishes identically**, so this
single identity — once proved as a *pure finite-algebra fact about binomial
coefficients* (no recurrence used in its proof, exactly analogous in spirit to a
Vandermonde/hockey-stick identity) — immediately gives TREC by direct substitution, no
Way-A/Way-B double-evaluation or 4-level shift tower needed. This is a strictly better
and simpler target than the plan in the previous round's log entry (which is now
superseded, though the `genTrC`/`genTrCW1_eq`/`genTrCW2_eq` infrastructure built for it
may still be reusable inside the proof of the certificate itself, e.g. for the
induction step).

**Not yet done:** proving this binomial-coefficient identity in Lean. The natural
approach is induction on `n` (Pascal's rule telescoping, in the same
peel-and-reindex-forward style as `genTrC_succ`/`genTrCW1_eq`), or possibly a direct
`Finset.sum` manipulation collapsing both sides' coefficient of each `C_j` via
`Nat.choose` identities. This is now the single concrete blocker for item 2/TREC.

## Remaining blocker (smallest isolated next step)
Formalize the elimination certificate above as a Lean lemma, e.g.
```
theorem zagS_elimination_cert (h : ℤ) (n : ℕ) (hn : 3 ≤ n) :
    (n:ℚ)^2 * zagS h n + (h:ℚ)^3*((n:ℚ)-2)*((n:ℚ)-1) * zagS h (n-3) - (-(h:ℚ))^(n-1)
      = ∑ k ∈ Finset.Ico 1 n, (n-1).choose k * (-(h:ℚ))^(n-1-k) *
          (((k:ℚ)+1)^2 * zagC h (k+1) - (h:ℚ)*(3*(k:ℚ)^2+3*(k:ℚ)+1) * zagC h k
            + 3*(h:ℚ)^2*(k:ℚ)^2 * zagC h (k-1))
        + (-1:ℚ)^n * (h:ℚ)^n * zagC h 0 - (-1:ℚ)^n * (h:ℚ)^(n-1) * (zagC h 1 - 1)
```
(stated with `zagC h` substituted for the free symbols `C_j`, so it is provable purely
by `Finset.sum` manipulation + `Nat.choose` Pascal identities, without needing
`zagC_rec` at all — the recurrence is only used *after* this lemma, to zero out the sum
and the boundary terms and conclude TREC). Once this compiles, TREC itself
(`n² S_n + h³(n−2)(n−1)S_{n−3} = (−h)^{n−1}`) follows by `rw`/`linarith` using
`zagC_rec`, `zagC_zero`, `zagC_one` to kill the RHS.

**Update — a genuinely stated `C : ℕ → ℚ`-generic version, and a promising (but
unfinished) induction route.** The certificate should be stated for an *arbitrary*
sequence `C : ℕ → ℚ` (not `zagC h` specifically), exactly as it was verified in sympy —
this is important because it lets an inductive proof invoke itself at the *shifted*
sequence `C' := fun k => C (k+1)` for free (universal quantification over `C` in the
induction hypothesis), rather than needing hand-built named shift-tower objects
(`V,W,Y,Z`) as CatalanEndpoint.lean did. Concretely, worked out by hand (not yet in
Lean): writing `S_n(C) := genTrC (-h) C n` and using `genTrC_succ` to expand
`S_{n+1}(C) = c·S_n(C) + S_n(C')` and `S_{n-2}(C) = c·S_{n-3}(C) + S_{n-3}(C')` (where
`c = -h`), the target identity at `n+1` decomposes into: `c ·` [the identity at `n` for
`C`] `+` [the identity at `n` for `C'`] `+` correction terms `(2n+1)·S_n(C) +
2h³(n−1)·S_{n−3}(C) + (2n+1)·S_n(C') + 2h³(n−1)·S_{n−3}(C')` coming from the coefficient
mismatch `(n+1)² − n² = 2n+1` and `h³(n−1)n − h³(n−2)(n−1) = 2h³(n−1)`. This only needs
**one** extra shift level (`C'`), not four — a materially smaller proof burden than
first estimated. **Not yet closed:** matching these correction terms against the
*RHS* sum's own Pascal-shift behavior (`(n choose k) = (n−1 choose k) + (n−1 choose
k−1)` applied to the `Finset.Ico 1 n` sum, relating `RHS(n+1,C)` to `RHS(n,C)` and
`RHS(n,C')`) requires a further Finset-reindexing lemma that has not yet been derived
or attempted in Lean. This is the smallest concrete next step: derive that Pascal-shift
identity for the RHS sum (by hand/sympy first, as with the certificate itself), then
assemble the full induction. Given remaining effort in this round, this was scoped but
not attempted in Lean — no unproved theorem was added to the file (per the trust
rules, nothing that doesn't compile is committed).

**Correction (this round): the "one extra shift level" hypothesis above did NOT
verify.** Tested computationally (`work/harmonic_jets/derive_zagB_TREC7.py` through
`TREC10.py`): the candidate identity
`RHS(n+1,C) = c·RHS(n,C) + RHS(n,C') + (2n+1)S_n(C) + 2h³(n−1)S_{n−3}(C) + (2n+1)S_n(C') + 2h³(n−1)S_{n−3}(C')`
(with `C' = C∘succ`, `c=-h`) leaves a nonzero residual for every `n` tested (4..9),
confirmed by direct symbolic expansion. A follow-up linear search (`TREC9.py`,
`TREC10.py`) allowing the residual to be an arbitrary-degree-2-in-`h` combination of
`S_n(C), S_{n-3}(C), S_n(C'), S_{n-3}(C'), S_n(C''), S_{n-3}(C'')` (`C'' = C∘succ∘succ`,
a *second* extra shift level) plus boundary corrections up to `C_2` **also found no
solution** for `n+1 = 4,...,8`. So the RHS sum's own Pascal-shift recursion is *not*
capturable by a bounded 1- or 2-level shift-tower correction with low-degree-in-`h`
coefficients; the earlier optimism was premature. This is consistent with (not
contradicting) the original assessment that this construction is comparable in scale
to CatalanEndpoint.lean's ~500-line `catalanT_rec` closure, likely larger due to the
lag-3 structure. **Item 2 (TREC) remains open** and is now the accurately-scoped
hardest remaining blocker; no further shortcut was found this round. The verified
elimination certificate itself (n=3..16, `TREC4`–`TREC6` scripts) remains valid and is
still the best available target statement — it is a true fact, just not yet proved in
Lean via any route tried so far (direct induction with 0, 1, or 2 shift levels).

## TREC CLOSED (later this round) — via the Way-A/Way-B `zagM` auxiliary sum

Reverted to the CatalanEndpoint `catalanT_rec`-style Way-A/Way-B strategy, as the
coordinator suggested, and it worked directly. Key realization: `zagC_rec`'s
coefficients `h(3k²+3k+1)` and `3h²k²`, while they *look* more complex than
`catalanB_rec`'s `12k²+12k+4`/`32k²`, are in fact **constant in `k`** exactly like
CatalanEndpoint's — they're just parametrized by `h` (`A=B=3h, D=h, E=3h²` vs.
CatalanEndpoint's `A=B=12, D=4, E=32`). This means `zagM`'s Way A and Way B expansions
are *mechanical* ports of `catalanM_wayA`/`catalanM_wayB`. What differs is the
**eliminated relation**: general symbolic elimination (`work/harmonic_jets/
derive_zagB_wayAB.py` through `wayAB5.py`) of the shift-tower unknowns
(`zagV,zagW,zagY` via their `_succ` relations) from Way A `=` Way B, for general
coefficients `A,B,D,E,c`, gives an **exact formula for the resulting `T`-relation**:
```
T_{m+3}·(m+3)² + T_m·(-Ac² - Ec - c³)(m²+3m+2)/(coefficients bundle) = c^{m+2}   [general form]
```
and substituting `A=3h,B=3h,D=h,E=3h²,c=-h` makes the `T_{m+1}` and `T_{m+2}`
coefficients **vanish identically**, leaving exactly
`(m+3)² T_{m+3} + h³(m+1)(m+2) T_m = (-h)^{m+2}` — i.e. TREC's lag-3 shape emerges
automatically from this substitution (`derive_zagB_wayAB.py`, verified by direct
symbolic substitution, and cross-checked against CatalanEndpoint's own lag-2 result by
re-substituting `A=12,B=12,D=4,E=32,c=-4` into the *same* general formula, which
reproduces exactly CatalanEndpoint's `catalanT_rec` shape as a sanity check). The exact
`linear_combination` multipliers for the elimination were extracted symbolically
(`derive_zagB_wayAB5.py`, via `sp.diff` of the fully-substituted-and-expanded
Way-A-minus-Way-B expression with respect to each succ-relation "residual").

**Compiled in Lean** (`ZetaLucas/ZagierBEndpoint.lean`, confirmed via
`lake env lean`, no errors, only pre-existing/new linter warnings, no
sorry/admit/axiom):
- `genTrCQ1_eq`, `genTrCQ2_eq`, `genTrCQ0_eq` — `c`-parametrized ports of
  CatalanEndpoint's `genTrQ1_eq`/`genTrQ2_eq`/`genTrQ0_eq`.
- `zagV`, `zagW`, `zagY` (shift-1/2/3 transforms), `zagS_succ`, `zagV_succ`,
  `zagW_succ` (their Pascal-shift relations).
- `zagM` (the Way-A/Way-B auxiliary sum), `zagM_wayA`, `zagM_wayB`.
- **`zagS_rec_aux`**: `(m+3)² S_{m+3} + h³(m+1)(m+2) S_m = (-h)^{m+2}`, closed via
  `linear_combination hB - hA + h²(m+1)(m+2)·hTs0 - h(m+2)(m+4)·hTs1 + (m+3)²·hTs2
  - 2h(m+1)(m+2)·hVs0 + (m+2)(m+4)·hVs1 + (m+1)(m+2)·hWs`.
- **`zagS_rec` (TREC itself)**:
  `theorem zagS_rec (h : ℤ) (n : ℕ) (hn : 1 ≤ n) : (n:ℚ)^2 * zagS h n + (h:ℚ)^3*((n:ℚ)-2)*((n:ℚ)-1) * zagS h (n-3) = (-(h:ℚ))^(n-1)`
  — proved for `n=1,2` by direct computation (a bug was caught and fixed here: an
  earlier hand-computed value `zagS h 2 = -2h` was wrong, the correct value is
  `zagS h 2 = -h/4`, found via `zagC h 2 = 7h/4` from `zagC_rec`) and for `n = m+3` via
  `zagS_rec_aux`. **Note the statement requires `1 ≤ n`**: at `n=0` the `ℕ`-truncated
  identity is genuinely false (`0² S_0 + ... = 0 ≠ 1 = (-h)^{0-1 truncated}`), since the
  underlying identity's `(-h)^{n-1}` only makes sense for `n ≥ 1`; this matches the
  paper's implicit restriction and does not weaken the theorem for its intended use
  (the endpoint formula/integrality argument only ever invokes TREC at `n ≥ 3`).

**Item 2 (TREC) is now COMPLETE.** Proceeding to item 3 (finite endpoint formula).

## Item 3 (finite endpoint formula) COMPLETE

Adapted CatalanEndpoint.lean's Stage C (`endpointQ/Num/Den/R`, `catalanSumR`,
`catalanT_square_formula`) from step-2/mod-2 to step-3/mod-3. Key simplification versus
CatalanEndpoint: our `R(n,j)` sums *unsquared* (the paper's own
`(-1)^{n-1}S_n = h^{n-1} Σ R(n,j)`, no square), since CatalanEndpoint's square was an
artifact of its weight `-4` being a perfect square — not needed here.

**Compiled** (`ZetaLucas/ZagierBEndpoint.lean`, confirmed via `lake env lean`, no
errors, no sorry/admit/axiom):
- `zagQ`, `zagNum`, `zagDen`, `zagR` — the endpoint quantities; `zagR_top` (top term
  `R(n,n-1)=1/n²`); `zagNum_step`/`zagDen_step`/`zagR_step` (the step-3 recursion
  `R(n,j) = (n-2)(n-1)/n² · R(n-3,j)` for `n-j≡1 mod 3`, `j+4≤n`).
- `zagSumR` (the indicator sum `Σ_{n-j≡1(3)} R(n,j)`), `zagSumR_split` (peel the top
  term `j=n-1`, discarding the two always-false residues `j=n-2,n-3` in one
  three-way `Finset.sum_range_succ` peel — done via `obtain ⟨k,rfl⟩ : n=k+3` first to
  avoid a subtraction-rewrite bug that corrupted the goal on the first attempt),
  `zagSumR_lower_eq`, `zagSumR_step` (combining both: `zagSumR n = (n-2)(n-1)/n² ·
  zagSumR(n-3) + 1/n²`).
- `zagC_two_eq`, `zagC_three_eq`, `zagS_two_eq`, `zagS_three_eq` — exact base-case
  values (`zagC h 2 = 7h/4`, `zagC h 3 = 85h²/36`, `zagS h 2 = -h/4`,
  `zagS h 3 = h²/9`).
- **`zagS_endpoint_formula`**:
  ```
  theorem zagS_endpoint_formula (h : ℤ) :
      ∀ n : ℕ, 1 ≤ n → (-1 : ℚ) ^ (n - 1) * zagS h n = (h : ℚ) ^ (n - 1) * zagSumR n
  ```
  Proved by a triple-conjunction induction (three residues mod 3, mirroring
  `catalanT_square_formula`'s double-conjunction for mod 2), with a shared `step`
  helper lemma (`∀ p ≥ 1, [identity at p] → [identity at p+3]`) applied three times
  in the inductive case with the three different base points `3m+1,3m+2,3m+3`, then a
  final dispatcher decomposing arbitrary `n≥1` via `n = 3*(n-1)/3 + (n-1)%3 + 1` and
  `interval_cases` on the residue. One genuine bug caught and fixed en route: a naive
  `rw [← e]`-chain to peel three terms from a `Finset.range n` sum corrupted the goal
  by rewriting `n` inside already-produced subterms; fixed by `obtain ⟨k, rfl⟩ : n = k
  + 3` first (avoiding subtraction entirely) before peeling.

**Item 3 is now COMPLETE.** Proceeding to item 4 (prime-power denominator lemmas).

## Re-verification session (this round)

- Re-checked `ps aux | grep -i lean`: a `lake build ZetaLucas` (PID 1099391, child lean PID
  1099509) was already running, started at the top of this round, compiling the
  pre-existing unrelated `ZetaLucas/BZQRow.lean` (known 30+ min compile). No second
  `lake env lean` was started concurrently, per the compile-hygiene rule.
- `tail /tmp/zagB_final_build.log`: only linter warnings (unused simp args at lines
  577/737/742) for `ZetaLucas/ZagierBEndpoint.lean` — **confirms the file as it stands
  (939 lines, through item 3) compiles cleanly**, no errors.
- `rg -n '\bsorry\b|\badmit\b|^\s*axiom\b' ZetaLucas/ZagierBEndpoint.lean`: only the
  doc-comment sentence *mentioning* `sorry`/`admit`/`axiom` (line 28, describing the
  trust boundary) — no actual placeholders in the file. Confirmed clean.
- Read CatalanEndpoint.lean's Stage D (`card_even_odd_diff_le_one` through
  `endpointR_lcm_integral`, lines 939–1388, ~450 lines) in full to plan the mod-3 port.
  Key structural notes for whoever continues item 4:
  - CatalanEndpoint's actual DIV bound is **not** the two-sided "≥ −2v_p(L_n)" counting
    argument sketched in the original task brief; it's simpler in structure: `endpointDen
    n j ∣ 2^(n-1) * Nat.lcmUpto n * endpointNum n j`. The odd-prime case uses a tight
    parity-imbalance bound (`card_even_odd_diff_le_one_multiples`, generalizing "evens vs
    odds differ by ≤1 in any interval" to "multiples of `p^i` that are even vs odd differ
    by ≤1", via the parity-preserving bijection `i ↦ i/p^i` since `p^i` is odd). The `p=2`
    case is handled separately and *crudely* (`endpointDen_val_le_two`, just bounds
    `v_2(Den) ≤ n-1` via `Den ∣ n!` and Legendre's formula), with the resulting slack
    `2^(n-1)` factor evidently absorbed elsewhere (by the weight `(-4)^{n-k}` structure)
    rather than needing a matching tight bound at 2.
  - For zagB (mod 3, weight `h`), the direct analogue would replace "even/odd" with the
    three residue classes mod 3, and the roles are: `zagDen` lives on the class `j+1 mod
    3` (squared), `zagNum` splits across the *other two* classes `j+2 mod 3` and `j mod
    3` (one factor each, paired). The odd-prime-style tight bound generalizes to primes
    `p ≠ 3` (any `p` coprime to 3, both even and odd primes — no odd/even split needed
    here since we're already working mod 3 not mod 2), via a 3-class imbalance lemma
    (classes differ pairwise by ≤ 1, or a combined bound that the doubled target class
    exceeds the sum of the other two by ≤ 2) analogous to
    `card_even_odd_diff_le_one_multiples`. The prime `p = 3` case needs its own dedicated
    argument (the brief's "maximal factor" valuation lemma, `v_3(D) ≤ v_3(L_n) + r +
    v_3(r!)`) — this does **not** have a direct analogue in CatalanEndpoint (whose `p=2`
    case was handled by the crude `∣ n!` bound with an absorbed slack factor, not by a
    forced-tight argument), so it is genuinely new work, not a port.
  - **Assessment given the scale**: CatalanEndpoint's Stage D + Stage E together are
    ~650 lines (939–1607) of dense `Finset`/`Nat.factorization` manipulation, itself the
    product of a comparably long prior session. A faithful mod-3 port plus the new `p=3`
    argument is realistically **not completable in a single short session** — it needs
    many compile-fix iterations (per-lemma `lake env lean` cycles), consistent with the
    task brief's own framing ("comparable in size to CatalanEndpoint's own Stage D...
    keep iterating across many compile-fix cycles").
- **No new Lean code was added this round** (per the trust rules: nothing that doesn't
  compile is committed, and a large multi-lemma port attempted under a tight budget and
  submitted without full verification would risk exactly the "fabricated
  certificate"/unverified-claim failure mode the rules forbid). Item 4 remains **not
  started** in the `.lean` file itself, but is now scoped in detail above (residue-class
  roles identified, `p≠3` vs `p=3` case split confirmed to mirror the brief, CatalanEndpoint's
  actual (not idealized) proof shape identified as the concrete template for `p≠3`).

## Priority-item status (updated)
1–3: done (see above). 4: **scoped, not started** (see this round's notes — smallest
next step is the mod-3 3-class imbalance counting lemma, direct analogue of
`card_even_odd_diff_le_one_multiples` at lines 1046–1153 of CatalanEndpoint.lean, adapted
from 2 classes to 3). 5–6 (necessity, n=2 optimality): done. 7 (root import, full
`lake build`): import done; full build was mid-flight on unrelated `BZQRow.lean` at the
end of this round, not yet confirmed to finish (not blocked by this file — its own
compile is clean).

## Item 4 — MAJOR PROGRESS (real, compiled code this round)

Added `import ZetaLucas.CatalanEndpoint` to `ZagierBEndpoint.lean` (reuses
`factorization_prod_eq_sum_card`; CatalanEndpoint.olean was already built). All of the
following are confirmed compiling via repeated `lake env lean ZetaLucas/ZagierBEndpoint.lean`
(exit 0, only pre-existing-style linter warnings, no errors), with a final
`rg 'sorry|admit|axiom'` check showing no placeholders:

- `card_filter_mod3_eq`, `card_mod3_diff_le_one` — closed-form count of `{i ∈ Icc lo hi :
  i%3=r}` via an image-bijection (not induction), giving the mod-3 pairwise-imbalance
  bound directly from `omega` on the two closed forms. (Different proof strategy than
  CatalanEndpoint's stride-2 induction, same end result, for 3 classes instead of 2.)
- `card_mod3_diff_le_one_multiples` — the multiples-of-`d` generalization (`d` coprime to
  `3`), via the bijection `i ↦ i/d`, using the fact every nonzero residue mod 3 is its own
  inverse (`d%3 ∈ {1,2}` self-inverse) to compute the transformed residue.
- `zagDenRoot`, `zagNumB`, `zagNumC` (unsquared root / split factors of `zagDen`/`zagNum`)
  and their `_eq_prod_filter` reindexings into filtered products over `Icc (j+1) n`
  (direct analogues of `endpointNum/Den_eq_prod_filter`).
- `zag_card_bound`, `zagDenRoot_val_le` — the **`p ≠ 3` valuation bound**:
  `v_p(zagDenRoot) ≤ v_p(zagNumB) + p.log n` and same for `zagNumC`.
- `zagDen_val_le_ne3` — the **combined `p ≠ 3` bound**: `v_p(zagDen) ≤ v_p(zagNum) +
  2 v_p(L_n)`.
- `prod_range_add_eq_factorial_div` — telescoping identity `(m-1)! · ∏_{t=0}^r(m+t) =
  (m+r)!`.
- `zagDenRoot_val_le3` — the **`p = 3` bound**: `2 v_3(zagDenRoot) ≤ 2 v_3(L_n) + (n-1)`.
  Proved by a *simpler* route than the brief's `v_3(r!)`-refined estimate: when
  `(j+1)%3=0`, `zagDenRoot = 3^(r+1) · D'` with `D' ∣ (m+r)!` (`j+1=3m`), and
  `Nat.factorization_factorial_le_div_pred` (`v_3((m+r)!) ≤ (m+r)/2`) together with
  `n = 3(m+r)` and `v_3(L_n) ≥ 1` (since `n ≥ 3`) closes the whole numeric chain by
  `omega` — no `v_3(r!)` term needed at all, the crude factorial bound is already enough.
- **`zagDen_dvd`** (**DIV**, the item-4 headline result):
  ```
  theorem zagDen_dvd (hnat n j : ℕ) (h3 : 3 ∣ hnat) (hj : j < n)
      (hmod : n % 3 = (j + 1) % 3) :
      zagDen n j ∣ (Nat.lcmUpto n) ^ 2 * zagNum n j * hnat ^ (n - 1)
  ```
  proved by combining the `p ≠ 3` and `p = 3` bounds per-prime via
  `Nat.factorization_le_iff_dvd`, exactly mirroring `endpointDen_dvd`'s structure (with
  `2^(n-1)` replaced by `hnat^(n-1)` using `3 ∣ hnat` for the `p=3` slack instead of a
  fixed base-2 slack).

**Item 4's core denominator bound (DIV) is now COMPLETE and compiled with no sorry/admit/
axiom.**

## ITEM 4 FULLY COMPLETE — full iff theorem and h=3 corollary compiled (same round)

Continuing directly from DIV, the rest of the assembly was completed and verified via
repeated `lake env lean ZetaLucas/ZagierBEndpoint.lean` (final state: exit 0, only
linter warnings, confirmed by a final `rg 'sorry|admit|axiom'` showing no placeholders):

- **`zagR_lcm_sq_integral`** (RL): casts `zagDen_dvd` to ℚ, handling the sign of `h`
  via `Int.natAbs_eq`/`Int.natAbs_pow` (since `zagDen_dvd` is stated for `h.natAbs`, not
  `h` itself, to stay in `ℕ`-factorization land).
- **`zagSumR_lcm_sq_integral`**: termwise sum via `ratInt_sum` (reused from
  CatalanEndpoint.lean) over `Finset.range n`, dispatching on the same mod-3 indicator
  `zagSumR` already sums over.
- **`zagS_lcm_sq_integral`**: transfers integrality from `zagSumR` to `zagS` via
  `zagS_endpoint_formula` and `(-1)^(n-1) * (-1)^(n-1) = 1`.
- **`zag_binomial_inversion`**: `zagC h n = Σ (n.choose k) h^(n-k) zagS h k`, by directly
  reusing `binom_inv_general` from CatalanEndpoint.lean (its hypothesis `T k = Σ
  (k.choose i)(-c)^(k-i) B i` matches `zagS`'s definition exactly with `c := (h:ℚ)`, no
  adaptation needed).
- **`zagC_sharp_denominator`**: transfers integrality from `zagS` to `zagC` via the
  inversion formula, `lcmUpto_dvd_lcmUpto` (reused from CatalanEndpoint.lean), and
  `ratInt_sum` again — direct structural copy of `catalanB_sharp_denominator`.
- **`zagC_sharp_iff`** — **the full target theorem**:
  ```
  theorem zagC_sharp_iff (h : ℤ) :
      (∀ n : ℕ, ∃ z : ℤ, (Nat.lcmUpto n : ℚ) ^ 2 * zagC h n = z) ↔ 3 ∣ h
  ```
  (`←` from `zagC_sharp_denominator`; `→` from the already-proved `zagC6_forces_three_dvd`
  necessity witness, instantiated at `n = 6`).
- **`zagC_three_sharp_denominator`** — the `h = 3` corollary:
  ```
  theorem zagC_three_sharp_denominator :
      ∀ n : ℕ, ∃ z : ℤ, (Nat.lcmUpto n : ℚ) ^ 2 * zagC 3 n = z
  ```

**All 7 priority items are now COMPLETE.** `zagC2_not_scaled_integral` (n=2 optimality
witness, already proved in an earlier round) stands as the standalone
optimality-of-exponent-2 result alongside the iff theorem.

Full file (`ZetaLucas/ZagierBEndpoint.lean`, now 1532 lines) confirmed via
`lake env lean ZetaLucas/ZagierBEndpoint.lean`: exit 0, zero errors, only pre-existing-
style linter warnings (unused simp args, deprecated `push_neg`), and a final
`rg -n '\bsorry\b|\badmit\b|^\s*axiom\b'` shows no real placeholders (only the doc-comment
sentence at line 28 that describes the trust boundary in prose).

**Not independently re-verified this round:** a full-project `lake build` (the
pre-existing, unrelated `ZetaLucas/BZQRow.lean` was still mid-compile at the end of the
round, ~40 CPU-minutes in, not blocking `ZagierBEndpoint.lean`'s own compile per the
per-file `lake env lean` check, which is authoritative for this file's correctness).
Whoever continues should let that build finish and re-confirm project-wide integrity,
though `ZagierBEndpoint.lean` itself is already fully verified standalone.
