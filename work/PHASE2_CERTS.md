# Phase-2 certificates — P1e

**Author:** computational agent (River's odd-zeta program), task P1e
**Date:** 2026-07-25
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, artefacts in `work/lb5/`
**Predecessors:** `work/PHASE2_FINAL.md` (§Item 1 playbook), `work/PHASE2_ENDGAME.md` §R4,
`work/PHASE2_THEOREM.md` (assembled statement).

**Mission.** Machine-close the two `[VERIFIED]` decomposition identities

* **(a) Theorem B** `P̂_n = Σ_{k,l} T(n,k,l)·ŵ₃(n,k,l)`
* **(b) (T1-top)** `P_n = Σ_{k,l} T(n,k,l)·w₅(n,k,l)`, `w₅ = w5_allp`

with `T(n,k,l) = C(n+k,n)C(n,k)²C(n+l,n)C(n,l)²C(n+k+l,n)`.

Labels as in `PHASE2_FINAL.md`: `[PROVED]`, `[VERIFIED r]`, `[CERTIFIED]`, `[OPEN]`.

---

## STATUS BOARD

> ### ★ CERTIFICATION STATUS — definitive, 2026-07-25 10:00 (end of P1e session 7)
>
> **Neither identity is `[CERTIFIED]`. Zero telescopers exist. `P1e` has produced no machine
> certificate for Theorem B or for (T1-top), and none of the seven sessions has come closer than
> one `Annihilator` call.**
>
> * **(a) Theorem B** — **`[VERIFIED, NOT CERTIFIED]`**. Four routes, all measured to a named
>   stage. **Three are blocked structurally and must not be reopened**: the `E`-route in every
>   fold (`E`'s coefficients are `Θ(ρ, σ)` for any non-constant `w` — §19.2, measured negative at
>   9 letters *and* at 7), the τ-split (same `ρ, σ`), and the letter-split (`ct₂` on pieces
>   searches a *provably empty* box — §18.13). **One is open and is a resource question, not a
>   mathematical one**: telescope `T·w` directly. `Annihilator[T·ṽ]` — 10 letters, `LeafCount`
>   **91** — **time-aborted at 5402 s having used 5.01 GB of a 9 GB cap**, RSS sawtoothing with
>   four multi-GB releases and a net slope of **0.027 GB/min** (§19.11). It is **the only object
>   in the campaign ever stopped by the clock rather than by memory**, so the honest reading is
>   *stopped by budget, not diverging*. Cost lower bound: **> 90 min**. Everything downstream of
>   that one call is discharged, written and `wlcheck`-clean (§19.5, §19.10). A 20000 s
>   continuation is in flight (§19.11.3).
> * **(b) (T1-top)** — **`[VERIFIED, NOT CERTIFIED]`, and blocked by a `[PROVED negative]`**, §16:
>   the weight-5 fitting system is inconsistent at letter-monomial degree ≤ 3 (and ≤ 4) in three
>   alphabets at two primes, so `ŵ₃`'s degree-≤2 folded form — the single fact that makes
>   Theorem B's route exist at all — **has no weight-5 analogue**. This is mathematics, not
>   compute; §18.6 independently costs the grind at ≳ 96 kernel-hours for the easy half alone.
> * **What would change either verdict.** For (a): one `Annihilator` return. For (b): a new idea
>   about the shape of `w₅` (§14.4's search of `w5_allp + ker(fit)`), not a bigger machine.

| item | status |
|---|---|
| **The "any representative suffices" claim for `w₅`** | **REFUTED as stated — [PROVED negative]**, §1. The 448 basis monomials are *pointwise linearly independent* over ℚ, so the 135-dimensional kernel of the fitting system contains no pointwise-zero element: every kernel element is itself a non-trivial summation identity, of exactly the same difficulty as the target. Certifying one representative does **not** certify another for free. The representative that must be certified is the one used downstream, i.e. `w5_allp`. |
| **Cost model of the CT route** | **RE-DIAGNOSED, §2.** The bottleneck is `CreativeTelescoping`, not the `∂`-finite closure, and its cost is governed by *which variable is eliminated first*, not by the module rank alone. The two-delta call `CreativeTelescoping[ann,{S[k]−1,S[l]−1},…]` is **not implemented** (it returns `$Failed` even for the undeformed `T`, where a telescoper provably exists in the given support). A line-truncation trap — `math < file.wl` **and the Wolfram MCP evaluator** both evaluate input line by line, silently discarding the continuation of any multi-line expression whose first line already parses — is documented there. It bit **twice**, first on the weight definitions and then on the `E(v)` construction, and is the single most likely way to waste a session. `work/lb5/wlcheck.py` now guards against it. |
| **New machinery** | **§3.** Three RISC levers not used in any prior session: `Support ->` (bounded ansatz), OreSys uncoupling (`Method -> Zuercher`), and `Extended -> True` cofactors (lets a two-step certificate be composed into one `(n,k,l)`-level identity). |
| **Verification harness** | **BUILT, §4.** `work/lb5/verifycore.wl` + `certV.wl`: re-derives `T`'s shift ratios from the Γ-product form and rewrites every `HarmonicNumber` by its defining recurrence, then checks certificate identities by `Together → 0`. It loads **no RISC package**; the saved `OrePolynomial`s are read as inert data. |
| **Q-row, single-certificate form** | **[CERTIFIED] — new**, §4bis. `L_BZ·T = Δ_k(ρT) + Δ_l(σT)` with explicit rational `ρ, σ` (`Qrow_rhosigma.m`), checked to exactly `0` twice, the second time in a kernel that never loaded RISC. This is the object every weight-lowering step needs; `PHASE2_FINAL` §1.2 had only the two-step form. |
| **Reduction of Theorem B** | **[PROVED]**, §4quater. Theorem B ⇔ `Σ_{k,l} E(v) = 0`, with `E(v)` explicit and the boundary/telescoping step proved from the pole structure of `ρ, σ` (`ρ(n,0,l) = σ(n,k,0) = 0`; `T`'s double zeros absorb every interior pole). |
| **Structure of `E(v)`** | **[PROVED]**, §4ter. `E(v)/T = c₀ + αA₁(k) + βA₂(k) + γB₁(k) + δC₁ + εA₁(l)` — a hypergeometric term times a **rank-6** factor whose basis elements are *single letters*, against rank 12 / 19 for the direct summands. Saved as `Eletters.m`. |
| **(a) Theorem B** | **STILL NOT closed** after session 3, but the residual obligation is now finite, explicit and checkpointed: **exactly five creative-telescoping problems**, one per τ-piece, each on a rank-≤3 module with coefficients ≤ 13069 leaves (§13.3–13.4). The ∂-finite *closure* step is no longer a blocker (2 s, against an OOM at 14.4 GB for the monolithic form); the *elimination* step is, and **bounding the `Support` does not bound its cost** — only its termination (§13.4). Everything downstream of those five operators is written and `wlcheck`-clean (`certPy.wl` → `certPv.wl` → `certT3f.wl`). Honest remaining budget: **4–10 kernel-hours, no new mathematics.** **Read §§13–14 first, then §§8–12; §§4–6 are two route-revisions out of date.** |
| **(b) (T1-top)** | **NOT closed**, but the evidence is much stronger, §6.1: `Σ T·w5_allp` matches `P_n` at every `n ≤ 360` and satisfies `L_BZ` at 748 consecutive `n` mod two primes, with minimal recurrence exactly `(3, 9)`. Cost of the first weight-lowering step now measured: **≤ 208 letter monomials**, §10. |
| **§8 — the boundary lemma (M2)** | **RESOLVED, and §4quater corrected.** `ρ, σ` have **double** poles; `E(v)` is **not** finite on the box (simple pole at every cell with `k₀ ≥ n₀`); but the box total is exactly `0` — `[VERIFIED exact, n₀ = 1…6]`, `m2bnd.wl`. |
| **§9 — the rank-1 route** | **GAP FOUND AND REPAIRED.** `m·(Δ_kX+Δ_lY)` does not telescope; one Abel summation per branch fixes it and stays rank 1. A certificate built from §5.3 as literally written would be wrong. |
| **§11 — `E(v)` is rank 3** | **`γ = 3α`, `δ = (3/2)α`, `ε = (1/2)α` exactly**, so `E(v)/T = c₀ + βA₂(k) + αΨ` and **only three** telescopers are needed, not six. `α` has a closed form (§11.4). |
| **§13 — the τ-split** | **The route of §§9–11 is superseded, §13.3.** The monolithic rank-3 `Annihilator` was **OOM-killed at 14.4 GB after 50 min** (§13.1): *rank is not the cost, coefficient size is*. Splitting `E(v) = Σ_τ F_τ` over the five shift terms **before** telescoping drops the weights from 132917 leaves to `{84, 86, 66, 12471, 2255}` at unchanged rank ≤ 3, and needs **no Abel correction** (the letters are never factored out, so the §9.1 gap cannot arise). The split is **[CERTIFIED — RISC-free and *symbolic* in `ℚ(n,k,l)[hh…]`]** (`certPv0.wl`), which also gives `Eletters.m` a fourth independent confirmation. A **new** line-reader trap (a line ending in `<|` is a *fatal* syntax error, not a truncation) is documented and `wlcheck.py` extended. |
| **§15 — (b) costed verdict, v4 target** | **`(T1-top)` against `w₅^I` is NO BETTER, §15.1.** Under `PHASE2_THEOREM` v4 the certificate target collapses to the single identity `P_n = Σ T·w₅^I`; measured (`esupp.py`, which reproduces §10's 208 exactly), the support of `E(w₅^I)/T` is **220**, against 208 for `w5_allp` and **6** for `ŵ₃`. §15.2 identifies the true driver: **monomial DEGREE, not weight** — a squarefree degree-`d` monomial contributes `2^d−1` sub-monomials, `ŵ₃`'s folded form has degree ≤ 2, every `w₅` has degree 4–5. The one cheap experiment that can change the cost class is the **degree-≤3 consistency test** of §15.2 (pure Python, `e2.py` machinery); counting says degree ≤ 2 is essentially impossible. The guessed-recurrence route does **not** avoid the cost (§15.3): the operator is already known to be `L_BZ`; the *certificate* is what is missing. |
| **§16 — (b) THE DEGREE-≤3 EXPERIMENT, RUN. `[PROVED negative]`** | **`(T1-top)` is blocked by a STRUCTURAL OBSTRUCTION, not by compute.** §15.2's decisive experiment has been executed (`work/lb5/degfit.py`): the weight-5 fitting system is **inconsistent** restricted to letter monomials of degree ≤ 3 — in the plain harmonic alphabet (where it is inconsistent at degree ≤ **4** too), in the Apéry-extended alphabet `+R_r(k)`, and in the depth-2 nested alphabet `+Y,V,Z`; at two primes; and **the obstruction is the fit identity alone**, so no pole-cap regime can rescue it. The harness reproduces `exIII.log`'s known positive (`rank(fit)=313`, `212` condition rows, `rank(joint)=342`, consistent) and `strong`'s known negative. **`ŵ₃`'s degree-≤2 folded form — the one fact that made Theorem B's route exist — has no weight-5 analogue.** §16.5 lists what must not be re-run. |
| **§17 — (a) Theorem B: the blocking step BROKEN for the first time, and a harness bug found** | Two τ failed hard (`Annihilator[F_kk]` **OOM-killed at 7.8 GB / 85 min**; the boxed rank-2 `ct₁` for `F_ll` **> 75 min, no return, 10.6 GB**), so §13.4's "4–10 kernel-hours" is **withdrawn**. But §17.3 **proves symbolically** that `p_ll = r_ll = 0`, hence `F_ll = (G_ll q_ll)·A₂(k)` with `A₂(k)` free of `l`: the letter factors out of the `l`-sum with **no Abel correction**, and the same elimination run at **rank 1** (`certQ.wl`) **returned in ≈ 9 min with 3 telescopers** — the first τ ever to clear its first elimination. §17.2 measures the cofactors of the untried τ-split **×** letter-split (13 rank-1 problems, nine under 3000 leaves). §17.5 is a **harness bug**: `stage` lacked `HoldRest`, so *every* `MemoryConstrained` cap was a no-op (this, not RISC, is why §13.1's 14.4 GB OOM and both session-4 divergences were uncapped) and *no checkpoint ever prevented recomputation*. One-line fix applied to `certP.wl`/`certP2.wl`, verified. |
| **§18 — (a) THE COST DRIVER WAS MISIDENTIFIED: it is the LETTER COUNT, not `LeafCount`** | Controlled measurement, same τ, same machine: `Annihilator[F_n1]` (**578 leaves, 10 letters**) — 19 min, no return; `Annihilator` of its letter-free piece (**400 leaves, 0 letters**) — 3 generators, **0 s**. `F_ll` was never cheap for being small (2318 leaves, four times *bigger* than `F_n1`) but for carrying 2 letters instead of 10 — so every §§13–17 ranking by `LeafCount` was **inverted**. The remedy is the **four-piece letter split** `F_τ = W P + W Q·A₂(k) + W R·Ψ_k + W R·Ψ_l`, `[PROVED symbolically for all five τ]` RISC-free and non-circularly against `certP.wl`'s own `stuff[]`/`Ftau[]`; it caps every piece at ≤ 4 letters, the first at **0**, and needs **no Abel correction**. Measured: `Annihilator` + `ct₁` + Gröbner now cost **6–33 s per piece** (against ≈ 12 min for the one τ that previously got through), and `gb === ct₁`-telescopers **always**, so no cofactor chain is ever needed. What remains are two named walls (§18.8): the `ct₂` `Support` ladder at **×3.8 per rung**, and `DFiniteTimes` for the two letter-bearing pieces — with a concrete counter-move for each. **Theorem B is `[NOT CERTIFIED]`; zero `M_τ` exist.** New: `certQ2.wl`, `certQ3.wl`, `phi_tables.m`. §18.5 records a **new gap** — the letter split inserts a `DFiniteTimes` stage `certPy`/`certPv` know nothing about — and closes its design with the **φ-shift decomposition**. §18.6 costs `(T1-top)` under the split: its `l`-free fraction is **12–17 %** against `ŵ₃`'s **67 %**, giving **165 rank-1 + 355 remnant problems at `l`-rank up to 16** and **≳ 96 kernel-hours for the easy half alone** — a second, independent reason not to grind it. |
| **§19 — (a) THE `E`-ROUTE IS DEAD, structurally; the cost law has TWO axes** | **§19.** The 7-symbol point of §18.17's calibration was run twice and **does not land**: `Annihilator[E(ṽ)]` **MEMORY ABORT at 5.0 GB / 478 s** and at **8.5 GB / 536 s**, memory rising a straight **3.6 GB per minute**. That is *worse per unit time* than the 9-symbol `F_kk` (7.8 GB after 85 min), so the refold's two-symbol gain buys nothing. §18.2's "the cost driver is the letter count" was measured at **fixed `LeafCount`** and is only half the law — the other half is **coefficient size**: `E(ṽ)` carries only **7** letters and cannot be closed at all, because its coefficients are `Θ(ρ, σ)`, while the direct objects `T·v` / `T·ṽ` carry **12** / **10** letters with *polynomial* coefficients. *(§1's `Annihilator[T·v] = 124 s, 7 generators` is **WITHDRAWN** — a §17.5 `Put`-time artifact that does not reproduce; see §19.4's ⚠ box. Do not quote it.)* And that is **invariant under every refold** — `E(w) = Σ_τ G_τ(τ.w − w)` has `G_kk = −ρ\|_{k+1}T(k+1)`, `G_ll = −σ\|_{l+1}T(l+1)`, so shedding `ρ, σ` would need `w` invariant under `k → k+1` **and** `l → l+1`, i.e. `w = w(n)`, which the fit excludes. **The obstruction lives in the Q-row certificate, not in the weight.** Hence: never form `E`; telescope `T·w` **directly**, where the coefficients are polynomial and the `ct₂` box is the known, *occupied* `(3,9)`. New: `certRF.wl`, `certRFD.wl`, `certRFy.wl`, `certRFv.wl`. Newly `[CERTIFIED RISC-free, symbolic]`: `E(ṽ)/T = c₀ + β(A₂(l) − A₂(k)) + α·Ψ_k` and `REFOLD` §4.6's four shift tables. Everything a certificate will need is discharged in advance (§19.5): the proved-kernel bridge `ŵ₃ − ṽ`, the far-edge boundary, and 301 exact initial values. **§19.11 (session 7) resolves the direct run: `Annihilator[T·ṽ]` — 9 GB cap, 5400 s cap — took the *time* abort at 5402 s with peak RSS 5.01 GB and 3.12 GB at death, RSS sawtoothing (`0.74 → 2.52 ↓2.21 ↑4.32 ↓2.58 ↑4.45 ↓2.84 ↑5.01 ↓3.08`), net 0.027 GB/min. First object in the campaign stopped by the clock rather than by memory; 65 % of its memory budget unused at the abort. `RFD_ann.m` never landed, so nothing downstream ran and the `ORD=kl` waiter self-disarmed at 09:38:42 without taking a seat. Verdict: `T·ṽ` is stopped-by-budget, not diverging; a 20000 s continuation is in flight (§19.11.3).** |
| **§14 — (b) costed verdict (v3 target, superseded)** | **DEFER, §14.** Direct route not feasible on this hardware: `E(w₅)` has rank ≈ 200 against 3, and rank 12 with *trivial* coefficients already failed to yield a telescoper while rank 3 with big ones exhausted 15 GB — floor ≈ 35 kernel-hours with no termination guarantee. The named alternatives are costed in §14.3 (the `w₅^I` route adds an obligation rather than removing one; the "guessed recurrence" route is not independent — the operator is already known, the *certificate* is what is missing). The one step that changes the cost class is §14.4: **search `w5_allp + ker(fit)` for a `p`-integral representative with the §11.1 product structure**, pure Python, no Wolfram seat. |

---

## §0. Why the costed ε-deformation route was replaced

The task specified the `PHASE2_FINAL` §1.3 route: sample the ε-deformed telescoper at rational
ε, interpolate, expand to ε-order 3 (resp. 5), verify exactly. That route was **not executed**,
and deliberately so. Its arithmetic is unattractive — for Theorem B it needs the total-degree-3
part of `L(ε)` in 5 parameters, i.e. 35 homogeneous directions × ~40 samples × 33 s ≈ 13 kernel-
hours, and the weight-5 analogue needs the degree-5 part, i.e. `C(9,4) = 126` directions,
≈ 46 kernel-hours — but the decisive objection is structural: the ε-route reconstructs
`L(ε)` and then has to **evaluate a triangular inhomogeneous system whose right-hand side
involves the weight-1 and weight-2 deformed sums `S_(1), S_(2)`**, which are themselves objects
of unknown complexity. §5.1 measures that complexity for the undeformed analogues and finds it
enormous: none of the five component sums of `ŵ₃` has a recurrence of order ≤ 12 with
coefficients of degree ≤ 30, while their *combination* has order 3, degree 9.

The route taken instead uses the same idea — differentiate a certificate to lower the weight —
but applies it **directly to the certified Q-row certificate** rather than to an interpolated
`L(ε)`. One subtraction takes weight 3 to weight ≤ 2 (§4ter), a second takes it to rank-1
hypergeometric problems (§5.3). No interpolation, no sampling, no ε at all; every object is
exact from the start, so there is nothing whose "being right" the verification could depend on.

Consequently there are **no sample counts or interpolation degrees to report** — the quantities
the task asked for belong to a route that was superseded. What replaced them is in §5.1
(complexity measurements), §4bis (the certified `ρ, σ`) and §4ter (the rank-6 form of `E(v)`).

---

## §1. The `w₅` kernel is not free — the mission's caveat was the right one

The fitting system for `(T1-top)` is `P_n = Σ_{k,l} T(n,k,l) w₅(n,k,l)` over the 448-element
basis of `PHASE2_FINAL` §2 (symmetric monomials of weight 5 in `A₁..A₅, B₁..B₅` at `k`/`l`,
`C₁..C₅` at `k+l`, `N₁..N₅` at `n`). `rank(design) = 313`, hence a 135-dimensional kernel, and
the family of admissible `w₅` is that kernel translated.

If two representatives `w, w'` differ by `z ∈ ker`, then certifying `P_n = Σ T·w` certifies
`P_n = Σ T·w'` **iff** `Σ_{k,l} T·z = 0` is itself certified. That is free only when `z` vanishes
**pointwise**, i.e. when `z(n,k,l) ≡ 0` as a function.

> **[PROVED] The 448 basis monomials are linearly independent as functions on the cells
> `0 ≤ k ≤ l ≤ n`.**
> `work/lb5/ptrank.py`: the cell-level matrix (rows = the 1331 cells of `n = 17,…,22`,
> columns = the 448 basis elements, entry = the value of the symmetrised monomial at that cell)
> has **rank 448** mod `q = 33554393`. Rank can only drop under reduction, so the rank over ℚ
> is 448 as well. ∎

**Consequences.**

1. `ker(design) ∩ {pointwise zero} = 0`. Every one of the 135 kernel directions is a genuine
   *summation* identity `Σ_{k,l} T(n,k,l) z(n,k,l) = 0` valid for all `n` — true, but only
   `[VERIFIED]` (it was read off a finite linear system and confirmed on excess equations),
   never `[CERTIFIED]`.
2. Certifying a kernel element is exactly as hard as certifying a representative: same summand,
   same weight, same machinery. There is no shortcut.
3. Therefore **the representative one certifies must be the representative one uses**. The
   `(GAP-5)` closure of `PHASE2_FINAL` §2 uses `w5_allp` (178 terms, denominators `{2,3}`), so
   `w5_allp` is the object to certify — which is what this task targets. Any report of the form
   "we certified `w5_canon2`, and `w5_allp` follows since they differ by a kernel element" would
   be **unsound**.

This is a correction to the framing in the task brief and to the phrase "the certified kernel of
the fit"; the kernel is not certified, and it cannot be certified more cheaply than the theorem.

---

## §2. Re-measured cost model of creative telescoping on this summand

All timings on the standalone kernel recipe of `PHASE2_FINAL` §0
(`Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"]` under `math < f.wl`).

> **A trap that invalidated part of this table before it was caught -- record it.**
> `math < file.wl` reads standard input **line by line** and evaluates each line as soon as it
> parses — **and so does the Wolfram MCP evaluator**, so the trap is not specific to the
> standalone-kernel recipe. A multi-line assignment whose *first line is already syntactically complete* is
> therefore **silently truncated**, and the continuation lines are evaluated and thrown away:
> ```
> w3hat = HarmonicNumber[n,3] + AA[3,k] + AA[3,l]      <- this alone became w3hat
>         - (1/4)(AA[2,k] AA[1,k] + ...)               <- discarded
> ```
> **Always wrap multi-line expressions in parentheses and assert on the result.** Every script
> here now logs `Length[Cases[w, HarmonicNumber[__], Infinity]]` and aborts if it is wrong.
> This bit **twice**: first on the `w3hat`/`v` weight definitions in the standalone scripts, and
> then again, silently, on the `E(v)` construction inside the MCP evaluator — producing an
> `Eletters.m` that was missing its `ρ` and `σ` terms and on which two kernels ran for twenty
> minutes. It was caught only by evaluating the letter form against an independently built copy
> of `E(v)` at an integer point. **Cross-check every derived object against an independent
> construction at a point where the arithmetic is exact.**
> Rows marked *(truncated)* below were measured before the fix; they describe a smaller weight
> than intended and are kept only because they are still informative about that smaller object.

| object | `Annihilator` | first `CreativeTelescoping` | notes |
|---|---|---|---|
| `T` (undeformed) | 0 s, 3 gens | elim `k`: 0 s | second step 4 s, order 3 = `L_BZ` |
| `T·A₁(k)` | 0 s, 4 gens | elim **`l`**: **81 s**; Gröbner 21 s | second step (elim `k`) > 8 min |
| `T·A₁(k)` | 0 s | elim `k`: > 4 min, no return | |
| `T·C₁` | 0 s, 4 gens | elim `k`: > 4 min (default), > 7 min (`Method->Zuercher`) | coupling letter, worst case |
| `T·(H⁽³⁾_n+A₃(k)+A₃(l))` *(truncated)* | 1 s, 6 gens | elim `k`: > 16 min, no return | rank ≈ 4, still out of reach with the wrong elimination order |
| `T·(H⁽³⁾_n+2A₃(k)−½A₂A₁(k)−(3/2)A₂B₁(k))` *(truncated)* | ~~124 s, 7 gens~~ **WITHDRAWN §19.4** — `Put`-time artifact of the pre-`HoldRest` `stage` (§17.5); re-measured under a correctly-timed `stage`: **TIME ABORT at 600 s** | elim `l` with `Support`: box(1,1) 13 s, (2,2) 12 s, (2,3) 194 s — **no** telescoper in any | `Support` makes each attempt terminate |

> ⚠ **Every timing in this table and in §5.2 passed through the pre-`HoldRest` `stage`, so each
> is `Put` time, not stage time — a lower bound of unknown quality, not a cost.** See §19.4.

**Corrections to the received cost model.**

1. **What matters most is which variable is eliminated first.** Eliminating a variable that the
   harmonic letters do *not* depend on is cheap (the module is block-diagonal in that direction):
   `T·A₁(k)` with `l` eliminated first costs 81 s, against no return in the same budget with
   `k` first. `ŵ₃` has no such direction — every one of its letters involves `k` or `l` —
   which is the core difficulty. The folded weight `v` of §5.2 is the best compromise available:
   only 4 of its 12 closure monomials move under `S_l`, and only by one filtration level.
2. **~~The `∂`-finite closure is cheap relative to telescoping.~~ WITHDRAWN, §19.4.** This rested
   entirely on the "124 s" above; correctly timed, `Annihilator[T·v]` does not return in 600 s,
   and `Annihilator[T·ṽ]` is the object this whole campaign now turns on. The closeout's
   "the `ŵ₃`-weighted `Annihilator` ran 55 min without returning" is not what blocks this route.
3. **`Method -> Zuercher` (OreSys uncoupling) did not help** on the `T·C₁` calibration — it was
   no faster than the default Gröbner-based uncoupling.
4. **The two-delta call is not implemented, rather than failing on this input.**
   `CreativeTelescoping[ann, {S[k]−1,S[l]−1}, {}, Support -> {1,S[n],S[n]²,S[n]³}]` returns
   `$Failed` **for the undeformed `T`**, where `L_BZ` lies in the specified support and is a
   correct telescoper. So that `$Failed` carries no information about the input.
   (`PHASE2_FINAL` §1.1 noted the July log's "`Length ctQ = 0`" was `$Failed` in disguise; this
   pins the reason: the feature is absent.)

---

## §3. Machinery found this session (reusable)

Read off `CreativeTelescoping::usage`, `OreReduce::usage`, `Options[…]` in a live kernel
(`work/lb5/certC.log`, `certD.log`). None of these appear in the prior files.

| lever | what it does | why it matters here |
|---|---|---|
| `Support -> {m₁,…,mᵢ}` | fixes the *support of the telescoper* `q₁`; the `{op₁,…}` argument then becomes superfluous and may be `{}` | converts `CreativeTelescoping`'s unbounded search (which cannot be interrupted — `TimeConstrained` does not bite) into a **finite linear solve that terminates**. Since the target telescoper for both identities is known to be `L_BZ` (order 3), `Support -> {1,S[n],S[n]²,S[n]³}` is the natural constraint for the *second* step. |
| `Method -> Zuercher / AbramovZima / IncompleteZuercher / Gauss` (needs `OreSys.m`, present at `/home/ubuntu/riscergosum/RISC/OreSys.m`) | replaces the Gröbner-basis uncoupling inside Chyzak's algorithm | the default uncoupling (`SolveCoupledSystem`) is the suspected hang |
| `OreGroebnerBasis[…, Extended -> True]` | cofactors transforming the input into the Gröbner basis | |
| `OreReduce[p, gb, Extended -> True]` → `{r, f, {c₁,…}}` with `f·p = r + Σ cⱼ gⱼ` | explicit ideal-membership cofactors | together these let the **two-step** certificate be composed into a single `(n,k,l)`-level identity `L·W + (S_k−1)(X·W) + (S_l−1)(Y·W) = 0`, which is what the independent verifier checks |

Also available and unexplored: `MultiSum.m` (Wegschaider's double-sum algorithm),
`Method -> "Hermite"` (Bostan–Chen–Chyzak–Li–Xin reduction-based telescoping).

---

## §4. The independent verifier (the deliverable-shaped part)

`work/lb5/verifycore.wl` — loads **no RISC package**. It provides

* `tratio[a,b,c]` = `T(n+a,k+b,l+c)/T(n,k,l)` as an explicit rational function, built from
  `T = Γ(n+k+1)Γ(n+l+1)Γ(n+k+l+1)Γ(n+1) / (Γ(k+1)³Γ(n−k+1)²Γ(l+1)³Γ(n−l+1)²Γ(k+l+1))`
  via `grat[x,d] = Γ(x+d)/Γ(x) = ∏(x+i)`;
* `hnorm` — rewrites every `HarmonicNumber[u,r]` occurring in a shifted `ŵ₃` as
  `hh[base,r] + (explicit rational)` using **only** `H^{(r)}_{x+1} = H^{(r)}_x + (x+1)^{−r}`,
  where `base` runs over the nine linear forms `n+k, k, n−k, n+l, l, n−l, n+k+l, k+l, n`;
  the `hh[·,·]` are then independent indeterminates;
* `applyOp[p, ker, extra]` — applies a saved `OrePolynomial`, read as **inert data**
  (`p[[1]]` = list of `{coefficient, exponent vector}`, `p[[2,1]]` = its variables), to a kernel;
* `zeroQ` / `zeroReport` — collect by `hh`-monomials and `Together` each coefficient;
* a hand-rolled Ore algebra (`ope`, `opTimes`, `opZeroQ`, …) implementing
  `S[x]·f(x) = f(x+1)·S[x]`, so that the *operator-level* cofactor identity can be re-checked
  without RISC as well.

`work/lb5/certV.wl` runs, on a certificate package, the checks

* **V-A** (function level) `q_i·W + (S_first−1)(r_i·W) = 0` for every first-step pair;
* **V-B** (operator level) `f·(Q + (S_second−1)·R) = Σ_i w_i·q_i` in `ℚ(n,·)⟨S[n],S[·]⟩`;
* **V-C** telescoper vs `L_BZ` (`Together[coeffs/L_BZ]` constant, `Expand[· − ·] = 0`);
* **V-D** denominators of the certificates, for the boundary/telescoping argument.

An identity that reduces to `0` in `ℚ(n,k,l)[hh…]` is an identity of functions wherever the
harmonic numbers are defined, so V-A/V-B are proofs, not spot checks.

**The harness is validated, and it has already re-certified the Q-row objects RISC-free.**
Run in a kernel that never loaded any RISC package (the MCP evaluator), reading the saved
`OrePolynomial`s as inert data:

| check | statement | result |
|---|---|---|
| Ore algebra | `S[n]·n = (n+1)·S[n]` | `ope[{S[n],S[l]},{{1+n,{1,0}}}]` — correct |
| **V1** | each of the 3 generators of `g0_ann.m` satisfies `L·T ≡ 0` | `{0, 0, 0}` |
| **V2** | each of the 2 `k`-step pairs of `g0_ct1.m`: `tel·T + (S_k−1)(cert·T) ≡ 0` | `{0, 0}` |
| **Q-row single certificate** | `L_BZ·T − Δ_k(ρT) − Δ_l(σT) ≡ 0` | `0` |

`PHASE2_FINAL` §1.2 obtained V1/V2 through RISC's own `ApplyOreOperator` and `FunctionExpand`;
these repeat them with an independent reader and an independently rebuilt shift calculus.

*(Two bugs found and fixed while validating the harness, both worth remembering: an unbalanced
bracket at the end of `applyOp` silently swallowed every later definition in the file, and an
`opShift` written as `c /. Thread[bases -> bases + e]` returns `c` **unchanged** when called
inside a function — `MapThread[Rule, {bv, bv+e}]` works. Both were caught only because the
harness was smoke-tested on objects with known answers; test verifiers on known answers.)*

---

## §4bis. The Q-row certificate in SINGLE-certificate (WZ-pair) form — `[CERTIFIED]` (new)

`PHASE2_FINAL` §1.2 certified the Q-row as a *two-step* object (annihilator + `k`-pairs +
order-3 telescoper `= L_BZ`). Everything downstream needs it in **single-certificate form**, and
`work/lb5/certR.wl` now produces and checks that:

> **[CERTIFIED]** There are explicit rational functions `ρ(n,k,l)`, `σ(n,k,l)` with
> ```
>     L_BZ · T(n,k,l)  =  Δ_k( ρ(n,k,l) T(n,k,l) )  +  Δ_l( σ(n,k,l) T(n,k,l) )
> ```
> as an identity of rational functions. Saved: `work/lb5/Qrow_rhosigma.m`
> (`LeafCount(ρ) = 10553`, `LeafCount(σ) = 1819`).

Extraction (search side): `gb === ct1-telescopers` for the undeformed `T` (so no Gröbner
cofactor chain is needed), `OreReduce[QQ + (S_l−1)·RR, gb, Extended->True]` returns remainder
`0` with multiplier `ff = 1` and two cofactors, and the second-step telescoper `QQ` equals
`L_BZ` **on the nose** (coefficient ratio `{1,1,1,1}` — not merely up to a unit).

Check (proof side): substituting the extracted `ρ, σ` back and reducing
`Σ_j c_j T(n+j,k,l)/T − (ρ|_{k→k+1})T(n,k+1,l)/T + ρ − (σ|_{l→l+1})T(n,k,l+1)/T + σ`
gives **exactly `0`** (`certR.log`: `*** Q-ROW SINGLE-CERTIFICATE CHECK: 0 ***`).

This is the object every weight-lowering step needs, and it is now a machine-checked proof
object rather than a pipeline output.

### §4ter. The weight-lowering identity it buys

For **any** weight `w`, subtracting the `w`-multiple of the Q-row certificate gives, identically,
```
L_BZ·(T w) − Δ_k(ρ T w) − Δ_l(σ T w)  =  E(w),
E(w) = Σ_{j=1}^{3} c_j T(n+j,k,l)[w(n+j,k,l) − w]
       − ρ|_{k→k+1} T(n,k+1,l)[w(n,k+1,l) − w]
       − σ|_{l→l+1} T(n,k,l+1)[w(n,k,l+1) − w] ,
```
and every bracket is a **difference** of `w`, hence of strictly lower weight (a shift changes
each harmonic letter by a rational function). For `w = v` (the folded weight-3 weight of §5.2),
`E(v)` lies in the span of the **single** letters `{1, A₁(k), A₂(k), B₁(k), C₁, A₁(l)}` times
`T` — module rank **6** instead of 12, and every element is a single letter rather than a
product. `LeafCount(E(v)) = 16067` as written, with 166 `HarmonicNumber` occurrences.

> **Reduction. [PROVED, given the boundary step]** Theorem B is equivalent to
> `Σ_{k,l} E(v)(n,k,l) = 0` for all `n ≥ 0`, plus the three initial values `n = 0,1,2`.

**`E(v)` computed, and it is linear in the letters — `[PROVED]`.**
Normalising every `HarmonicNumber` to a base argument (using only
`H⁽ʳ⁾_{x+1} = H⁽ʳ⁾_x + (x+1)^{−r}`) and dividing by `T`:

* exactly **9** distinct harmonic symbols occur — `H_l, H_k, H⁽²⁾_k, H_{k+l}, H_{n−k}, H_{n+l},
  H_{n+k}, H⁽²⁾_{n+k}, H_{n+k+l}` — each to **degree 1**, with **no cross terms**
  (`Coefficient[E/T, H_i]` is free of every `H_j`);
* the coefficients satisfy the four **letter relations**
  `c[H_l]+c[H_{n+l}] = c[H⁽²⁾_k]+c[H⁽²⁾_{n+k}] = c[H_{k+l}]+c[H_{n+k+l}] =
  c[H_k]+c[H_{n+k}]+c[H_{n−k}] = 0`, all four checked to exactly `0`;

hence

> ```
>   E(v) / T  =  c₀ + α·A₁(k) + β·A₂(k) + γ·B₁(k) + δ·C₁ + ε·A₁(l)
> ```
> with `c₀, α, β, γ, δ, ε` explicit rational functions of `(n,k,l)`
> (`LeafCount` 66499, 22317, 44011, 22317, 22317, 22317). Saved: `work/lb5/Eletters.m`
> (and `Ecanon.m` in raw-symbol form).
>
> **Cross-checked**: `T·(letter form) − E(v)` evaluates to exactly `0` at the integer points
> `(n,k,l) = (5,2,3), (6,1,4), (4,3,0)`, where `E(v)` is read from `R_E.m` — built in the *RISC*
> kernel by a different code path from the letter form (built in the MCP kernel). Do this check:
> it is what caught the truncation bug below.

So `E(v)` is a **hypergeometric term times a rank-6 `∂`-finite factor**, against rank 12 for
`T·v` and rank 19 for `T·ŵ₃` — and under `S_l` only two of the six basis elements move (`C₁` and
`A₁(l)`), each by a rational function, so `l` is a cheap elimination direction. This is the
smallest form the problem has been put in, and it is the recommended attack point.

*Computational note:* `Expand`ing `E/T` produces an 11-million-leaf expression; extracting the
coefficients **without** expanding (`Together[Coefficient[…]]` on the unexpanded product) takes
under a second and yields the ~5000-leaf coefficients above. This was the difference between an
intractable and a trivial step.

### §4quater. The boundary step — `[PROVED]`

Passing from the *function* identity to the *sequence* identity needs the telescoped terms to
vanish at the ends of the summation range. All the required facts are now explicit.

| fact | source |
|---|---|
| `ρ(n,0,l) = 0` and `σ(n,k,0) = 0` identically | `Together[ρ /. k->0] = 0`, `Together[σ /. l->0] = 0` |
| `denom(ρ)` factors as `(1+k+l)(k-n-1)(k-n-2)(k-n-3)(l-n-1)(l-n-2)(l-n-3)(1+n)(2+n)(2+l+n)(3+l+n)` | `FactorList` |
| `denom(σ)` factors as `(1+k+l)(l-n-1)(l-n-2)(l-n-3)(1+n)(2+n)(2+l+n)` | `FactorList` |
| `T` has a **double** zero at every integer `k > n` (from `C(n,k)²`), likewise in `l` | definition |
| `v` has at most a **simple** pole at integer `k > n` (only `B₁(k) = H_{n-k} - H_k` is singular there) and is **regular** in `l` for `l > n` (the folded weight has no `B₁(l)`) | inspection of `v` |

Consequently, on the box `0 ≤ k,l ≤ K` with `K ≥ n+3`:

* `T(n+j,k,l) v(n+j,k,l) = 0` for `k > n+j` or `l > n+j` (double zero beats simple pole), so
  `R_{n+j} = Σ_{[0,K]^2} T(n+j) v(n+j)` for `j = 0,1,2,3` — the box may be taken `n`-independent;
* `ρ T v` and `σ T v` are **finite at every integer point of the box** — the only poles of `ρ, σ`
  sit at `k ∈ {n+1,n+2,n+3}` / `l ∈ {n+1,n+2,n+3}`, where `T`'s double zero more than absorbs the
  simple pole of `ρ` and the simple pole of `v`;
* the telescoped sums collapse to `(ρTv)|_{k=K+1} - (ρTv)|_{k=0}` and
  `(σTv)|_{l=K+1} - (σTv)|_{l=0}`, and **all four terms vanish**: at `k = K+1 > n+3` because
  `T = 0` and `ρ` is finite there; at `k = 0` because `ρ(n,0,l) = 0`; symmetrically in `l`.

> **Lemma (reduction). [PROVED]**
> ```
>     L_BZ · ( Σ_{k,l} T(n,k,l) ŵ₃(n,k,l) )  =  Σ_{k,l} E(v)(n,k,l)      for every n ≥ 0.
> ```
> Hence **Theorem B ⇔ `Σ_{k,l} E(v) = 0` for all `n ≥ 0`**, together with the three initial
> values `n = 0,1,2` (already exact). The `ŵ₃ → v` folding is an exact rearrangement of a finite
> sum, using only that `T` is `k↔l` symmetric.

**Honesty note on what was and was not checked here.** The boundary lemma rests on the pole-order
count above, which is exact symbolic information (`Together[ρ /. k->0] = 0`, `FactorList` of the
denominators, the orders of `T`'s zeros and `v`'s poles). An *end-to-end numerical* confirmation
— evaluating `Σ_{k,l≤n+3} E(v)` at a small `n` and seeing `0` — was attempted and **not
completed**: at the cells `k ∈ {n+1,n+2,n+3}` the value of `E(v)` is finite only after a
cancellation between the `v(n+j)` and `−v` parts (both individually infinite, since
`B₁(k) = H_{n−k} − H_k` has a pole there while `T` has a double zero), and Mathematica's `Limit`
did not resolve the resulting `0·∞` on the letter form. The cancellation itself is easy to see
by hand — collecting the `−v` terms gives the factor
`Σ_{j≥1} c_j T(n+j) − ρ|_{k+1}T(n,k+1,l) − σ|_{l+1}T(n,k,l+1) = −c₀T − ρT − σT` by the Q-row
certificate, and `T` has a double zero at `k = n+1` against `ρ`'s simple pole and `v`'s simple
pole — but it has not been machine-checked, and a successor should either do the limit properly
or re-derive `E(v)` in a pole-free normalisation.

Note the shape of this: it does **not** require an order-0 telescoper for `E(v)`. It suffices to
certify *any* operator `L'` annihilating `F_n := Σ_{k,l} E(v)`, and then check `F_n = 0` at
`ord(L')` consecutive values of `n` where the leading coefficient of `L'` does not vanish — which
is a finite exact computation, since `F_n = L_BZ·(Σ T ŵ₃)` and `Σ T ŵ₃ = P̂_n` is known exactly
for `n ≤ 80`, giving `F_n = 0` for `n ≤ 77`.

---

## §5. (a) Theorem B — state

`ŵ₃` is `k↔l` symmetric and `T` is `k↔l` symmetric, so the identity collapses to **five**
distinct double sums:

```
Σ T ŵ₃ = H^{(3)}_n Q_n + 2U₁ − ½U₂ − (3/2)U₃ − ¾U₄ − ¼U₅ ,
U₁ = Σ T A₃(k),  U₂ = Σ T A₂(k)A₁(k),  U₃ = Σ T A₂(k)B₁(k),
U₄ = Σ T A₂(k)C₁, U₅ = Σ T A₂(k)A₁(l).
```

**[VERIFIED exact, `n ≤ 80`, 0 discrepancies]** — `work/lb5/seqdata.py`, values in
`work/lb5/seqdata.json`. (The previous exact range was `n ≤ 40`.)

### 5.1 Sizing — the combination is small, every piece of it is huge

`work/lb5/guessrec.py` computes all six sequences mod `q = 33554393` for `n = 0..500` and
searches for a recurrence `Σ_{j≤r} p_j(n) y_{n+j} = 0`, `deg p_j ≤ d`, over the whole rectangle
`r ≤ 12`, `d ≤ 30` (every `(r,d)` with at least 8 excess equations).

| sequence | minimal `(r, d)` found | nullity |
|---|---|---|
| `Q_n` | **(3, 9)** | 1 |
| `Σ T ŵ₃` | **(3, 9)** | 1 |
| `U₁, U₂, U₃, U₄, U₅` | **none** with `r ≤ 12` and `d ≤ 30` | — |

Two consequences.

1. **Independent modular confirmation of the target.** `Σ_{k,l} T·ŵ₃` satisfies a *unique*
   order-3, degree-9 recurrence — necessarily `L_BZ`, which has exactly that shape — computed
   from 501 values with ~460 excess equations. This is much stronger evidence than the exact
   ladder match alone, and it says the certificate being hunted really does exist and really is
   `L_BZ`.
2. **The decomposition route (Route D) is dead.** No individual `U_i` has a recurrence of order
   `≤ 12` with coefficients of degree `≤ 30`; their minimal operators are therefore very large,
   and an `lclm` of five such is out of reach. Only the *combination* is small. This is a real
   structural fact about these sums, and it explains why per-monomial creative telescoping was
   slow: the telescopers it is being asked to produce are enormous.

### 5.2 Rank reduction by the `k↔l` symmetry

Both `T` and `ŵ₃` are `k↔l` symmetric, so under `Σ_{k,l}` every `l`-letter monomial folds onto
its `k`-mirror:
```
Σ T ŵ₃ = Σ T v,
v = H^{(3)}_n + 2A₃(k) − ½A₂(k)A₁(k) − (3/2)A₂(k)B₁(k) − ¾A₂(k)C₁ − ¼A₂(k)A₁(l).
```
The shift-closure of `T·v` spans **12** monomials against **19** for `T·ŵ₃`, and — decisively —
under `S_l` only four of the twelve move (`C₁, A₁(l), A₂(k)C₁, A₂(k)A₁(l)`), and only by one
filtration level. So for `T·v`, unlike for `T·ŵ₃`, **`l` is a cheap elimination direction**,
which is exactly the property that made `T·A₁(k)` tractable (§2). `Σ T v = P̂_n` still, so the
telescoper is still `L_BZ` and `Support -> {1,S[n],S[n]²,S[n]³}` is still the right constraint
for the second step. `work/lb5/certJ.wl` (unconstrained step 1) and `certK.wl` (Support-bounded
step 1) run this.

**The `P̂` side needs no certificate.** The committed ladder
`zeta-math/worthiness/falsify_data/manifest.json` records
`"recurrence": "normalized order-3 (V6b)"` — i.e. `ladder_Q/P/Ph.json` were *generated by*
`L_BZ` from their initial values, and re-checking confirms `rec_residual = 0` for all three rows
at every `n < 60`. So `L_BZ·P̂ = 0` holds **by construction of the object**, and the finish is
exactly the campaign's: **certify `L_BZ·(Σ T ŵ₃) = 0`, then match `n = 0,1,2`.**

Leading/trailing coefficients of `L_BZ` are `2(n+3)⁵(2n+5)a₀(n)` and `(n+1)⁵(n+2)a₀(n+1)` with
`a₀(x) = 41218x³+198849x²+320790x+173057 > 0` for `x ≥ 0`, so `L_BZ` is non-singular on `n ≥ 0`
and three matching initial values suffice. **[PROVED]**

### 5.3 The chain as it now stands, and the one step that remains

| step | statement | status |
|---|---|---|
| 1 | `L_BZ·T = Δ_k(ρT) + Δ_l(σT)`, `ρ,σ` explicit rational | **[CERTIFIED]** §4bis, checked to `0` twice, once with no RISC loaded |
| 2 | boundary/telescoping over the box `0 ≤ k,l ≤ K`, `K ≥ n+3` | **[PROVED]** §4quater |
| 3 | `Σ T ŵ₃ = Σ T v` (`k↔l` folding) | **[PROVED]** (rearrangement of a finite sum) |
| 4 | `L_BZ·(Σ T ŵ₃) = Σ_{k,l} E(v)`; Theorem B ⇔ `Σ E(v) = 0` | **[PROVED]** §4quater |
| 5 | `E(v)/T = c₀ + αA₁(k) + βA₂(k) + γB₁(k) + δC₁ + εA₁(l)` | **[PROVED]** §4ter — linearity (degree 1, no cross terms) plus four coefficient relations, all checked to `0`; the identity then holds by construction |
| 6 | an operator `L'` with `L'·(Σ E(v)) = 0` | **the remaining step** |
| 7 | `Σ E(v) = 0` for `n ≤ 77`, hence `≡ 0` if `ord(L') ≤ 77` | **[VERIFIED exact]** — `Σ T ŵ₃ = P̂_n` for **`n ≤ 80`** and `L_BZ·P̂ = 0` |

**Step 6 reduces to rank-1 telescoping.** Because every `m` in step 5 is a *single* letter,
`m(n+j) − m` is a rational function, so for any `M = Σ_j M_j(n) S_n^j`
```
M·E = Σ_m [ Σ_j M_j e_m(n+j) T(n+j) ]·m  +  Σ_j M_j T(n+j)[ c₀(n+j) + Σ_m e_m(n+j)(m(n+j)−m) ].
```
The bracket in the first sum telescopes exactly when `M` is a telescoper for the
**hypergeometric** double sum `Σ_{k,l} e_m T` — the *same* rank-1 computation as the Q-row
(4 s). Taking `M = LCLM` over the five letters, the second sum is a hypergeometric term `G`, and
one more rank-1 telescoping gives `N` with `N·(Σ G) = 0`; then `N·M` annihilates `Σ E(v)`.
`work/lb5/certU.wl` runs exactly this. Every creative-telescoping call in it is rank 1, and the
measurements confirm it:

| stage of one letter's rank-1 CT | time | result |
|---|---|---|
| `Annihilator[T·e_m, {S[n],S[k],S[l]}]` | 136 s | **3 generators — rank 1 confirmed** |
| `CreativeTelescoping[ann, S[k]−1, {S[n],S[l]}]` | 412 s | 3 telescopers |
| `OreGroebnerBasis` | 56 s | `gb === ct1-telescopers` → **True** (no cofactor chain needed) |
| `CreativeTelescoping[gb, S[l]−1, {S[n]}]` | running at hand-off | telescoper order not yet known |

Identical timings for `α` and `δ`, run on separate kernels. Budget ≈ 25–45 min per letter, six
letters, two kernels ⇒ ~1.5–2 kernel-hours for the set, then the `LCLM`.

This is why the earlier attempts failed and this one should not: the direct routes asked
`CreativeTelescoping` for telescopers of the *individual* harmonic-weighted sums, which §5.1
shows are enormous (no recurrence of order ≤ 12 and degree ≤ 30 exists for any of them). The
two weight-lowering steps replace all of that by six rank-1 problems and one `LCLM`.

*(CT status: see the run log below and `CERTS_RESUME.md`.)*

---

## §6. (b) (T1-top) — state

The target is **`w5_allp` specifically** (§1): the "certify one representative, get the others
free" shortcut is refuted, so the object to certify is the one the `(GAP-5)` closure uses.

### 6.1 Evidence, substantially strengthened

`work/lb5/w5rec.py` evaluates `Σ_{k,l} T(n,k,l) w5_allp(n,k,l)` directly from the saved
representative (a different code path from the rref that produced it) mod `q = 33554393` and
`q = 33554467`, for `n = 0..750`:

| check | result |
|---|---|
| against the exact ladder `P_n`, every `n ≤ 360` | **0 mismatches**, both primes |
| `L_BZ` residual, `n = 0..747` | **0 at all 748 values**, both primes |
| minimal recurrence of the sequence (search over `r ≤ 12`, `d ≤ 30`) | **(order 3, degree 9), nullity 1** — i.e. exactly `L_BZ` |

The fitting system only imposed equations for `n ≤ 600`, so roughly 147 of these are genuine
excess checks. Previous status was "exact over ℚ for `n ≤ 34`, plus 287/687 excess equations".
This is still `[VERIFIED]`, not `[CERTIFIED]` — but the object being hunted is now pinned:
the certificate must produce `L_BZ` and nothing else.

### 6.2 Route

The §4bis–§4ter machinery applies verbatim with `w₅` in place of `ŵ₃`: fold by `k↔l`, subtract
`w₅` times the certified Q-row certificate, and `E(w₅)` has weight ≤ 4. Iterating the same step
five times reaches weight 0 (the certified Q-row). The one caveat is that at weight ≥ 2 the
brackets `w(shifted) − w` are no longer *single* letters, so the rank-1 shortcut of §5.3 only
becomes available at the last step; the intermediate steps need the general machinery. Detailed
plan in `work/lb5/CERTS_RESUME.md` §5.

Do **not** re-derive `w₅`: `w5_allp.json` is depth-minimal, `p`-integral at every `p ≥ 5`, and
is the representative `PHASE2_FINAL` §2's `(GAP-5)` closure depends on.

---

## §7. Reproduction — files added this session (all in `work/lb5/`)

| file | what it does |
|---|---|
| `wlcheck.py` | **run this on every `.wl` before launching it** — flags multi-line expressions that `math < file` would silently truncate (all current scripts pass) |
| `ptrank.py` | the §1 pointwise-independence computation (cell-level rank of the 448 basis) |
| `seqdata.py`, `seqdata.json` | exact `U₁..U₅`, `Σ T ŵ₃`, and the check against `P̂_n`, `n ≤ 80` |
| `guessrec.py` | minimal-recurrence search (§5.1) |
| `w5rec.py` | the §6.1 forward check of `w5_allp` to `n = 750`, two primes |
| `certA.wl` … `certK.wl` | the direct CT attempts and the cost ladder; logs `cert*.log` |
| `certR.wl`, `certS.wl` | Route R: Q-row single certificate + `E(v)` |
| `certT.wl` | telescoping on `E(v)` in rank-6 letter form (`MODE=box` / `MODE=unc`) |
| `certU.wl` | **the rank-1 route of §5.3** — five hypergeometric telescopers + `LCLM` |
| `Qrow_rhosigma.m` | **the certified `{ρ, σ}`** |
| `Eletters.m` | `{c₀, α, β, γ, δ, ε}` — `E(v)/T` in letter form |
| `Ecanon.m` | `E(v)/T` in raw-harmonic-symbol form |
| `verifycore.wl` | RISC-free exact-arithmetic verification kernel (§4) |
| `certW.wl` | certificate composition (cofactor extraction; RISC used only to *search*) |
| `certV.wl` | the independent verifier (§4) |
| `CERTS_RESUME.md` | precise resume state |

---

## §8. M2 — the boundary lemma, resolved (and corrected)

*(Task P1e continuation, 2026-07-25 02:00. Artefacts: `work/lb5/m2bnd.wl`, `work/lb5/m2bnd.log`.)*

The end-to-end numerical confirmation that §4quater left open is now **done**, and it forced two
corrections to §4quater. Both matter downstream, so they are stated before the result.

### 8.1 Correction 1 — `ρ` and `σ` have DOUBLE poles, not simple ones

§4quater read the denominators off `FactorList[...][[All,1]]`, which prints the distinct factors
and **discards their exponents**. With the exponents:

```
denom(ρ) = (1+k+l) · (k−n−1)²(k−n−2)²(k−n−3)² · (l−n−1)²(l−n−2)²(l−n−3)²
                   · (1+n)²(2+n)² · (2+l+n)(3+l+n)
denom(σ) = (1+k+l) · (l−n−1)²(l−n−2)²(l−n−3)² · (1+n)²(2+n)² · (2+l+n)
```

So the pole of `ρ` at `k = n+1` is of order **2**, against `T`'s double zero and `v`'s simple
pole — the count in §4quater ("double zero beats simple pole, so every interior value is finite")
is off by exactly one order.

### 8.2 Correction 2 — `E(v)` is NOT finite at every integer cell of the box

`m2bnd.wl` evaluates `E(v)` at `n = n₀ + ε`, `k = k₀`, `l = l₀` integers, rewriting every
`HarmonicNumber` by its defining recurrence into `hs[r] = H⁽ʳ⁾_{n₀+ε}` plus an explicit rational
function of `ε`, then expanding `hs[r] = hv[r] + Σ_m dd[r,m] ε^m` with `hv, dd` **free symbols**
(so nothing depends on the numerical value or the Taylor data of `H⁽ʳ⁾`), and Laurent-expanding.
`T` is built as a **polynomial** in `n` via `Pochhammer`, so no `Γ`-cancellation is involved:

```
T(n,k₀,l₀) = (n+1)_{k₀}(n+1)_{l₀}(n+1)_{k₀+l₀}(n−k₀+1)²_{k₀}(n−l₀+1)²_{l₀} / (k₀!³ l₀!³ (k₀+l₀)!)
```

> **[VERIFIED exact, n₀ = 1,…,6]** `E(v)(n,k₀,l₀)` has a **simple pole** in `n` at `n = n₀` for
> **every** cell with `k₀ ≥ n₀` — that is `4(K+1)` of the `(K+1)²` cells of the box `K = n₀+3`
> (20/25, 24/36, 28/49, 32/64, 36/81, 40/100 — exactly `4(K+1)` every time). The pole comes from
> `ρ(n,k₀+1,l₀)·T(n,k₀+1,l₀)·v(n,k₀+1,l₀) ~ ε⁻²·ε²·ε⁻¹`.

Hence **`Σ_{k,l} E(v) = 0` is not a statement about pointwise values of `E(v)`** — at 20–32 cells
per box there is no value to sum. This is the honest reading of the "0·∞" that defeated `Limit`
in the previous session: the limit really does not exist cell-by-cell.

### 8.3 The result — the box sum is exactly 0, and the poles cancel

> **[VERIFIED exact, n₀ = 1,…,6]** With `K = n₀+3` and everything regularised at `n = n₀+ε`:
>
> | n₀ | cells | singular cells | Σ of all ε^{<0} coefficients | ε⁰ total |
> |---|---|---|---|---|
> | 1 | 25 | 20 | **0** | **0** |
> | 2 | 36 | 24 | **0** | **0** |
> | 3 | 49 | 28 | **0** | **0** |
> | 4 | 64 | 32 | **0** | **0** |
> | 5 | 81 | 36 | **0** | **0** |
> | 6 | 100 | 40 | **0** | **0** |
>
> The `ε⁻¹` parts cancel **exactly across the box**, and the `ε⁰` total contains **no `dd[r,m]`**
> (no dependence on the Taylor coefficients of `H⁽ʳ⁾` — the check is an identity in free symbols,
> not a numerical coincidence) and reduces to `0` after `hv[r] → H⁽ʳ⁾_{n₀}`.
> Before that substitution the total is `c · (hv[1] − H_{n₀})` for an explicit integer `c`, i.e.
> it is zero *as a polynomial in the free symbols* once the one true value is supplied.

### 8.4 Why this repairs rather than damages the chain

The cancellation is structural, not accidental: the singular terms enter only through
`Δ_k(ρTv)` and `Δ_l(σTv)`, and a telescoping sum

```
Σ_{k=0}^{K} Δ_k(ρ T v) = (ρTv)|_{k=K+1} − (ρTv)|_{k=0}
```

holds as an identity of **meromorphic** functions: the poles of the interior terms cancel in
**adjacent pairs**, never individually. So the correct statement of the reduction is the
regularised one:

> **Lemma (reduction), corrected form. [PROVED, and now VERIFIED numerically]**
> For every integer `n₀ ≥ 0` and every `K ≥ n₀+3`,
> ```
> L_BZ·(Σ_{k,l} T ŵ₃) |_{n₀}  =  lim_{n→n₀} Σ_{k,l=0}^{K} E(v)(n,k,l) ,
> ```
> the limit existing because the two boundary terms vanish there
> (`ρ(n,0,l) ≡ 0` and `σ(n,k,0) ≡ 0` identically; at `k = K+1 ≥ n₀+4` and `l = K+1` the factors
> `ρ, σ` are regular while `T` has a double zero). **Theorem B ⇔ that limit is 0 for every `n₀`.**

Everything downstream is unaffected **provided the Δ-terms are always kept as telescoping sums
and never split into individual cell values**. Concretely, for step 6 (the operator annihilating
`Σ E(v)`) this means the per-letter certificates must be summed in the same regularised way, and
each of their boundary terms checked at `k,l ∈ {0, K+1}` — not at the interior poles, where the
summand is genuinely infinite. `Σ_box E(v)(n)` is independent of `K` for `K ≥ n₀+3` (the extra
cells have `ρ, σ` regular, `T` doubly zero, `v` simply polar, hence contribute `0` in the limit).


---

## §9. M1 — correction to the rank-1 route of §5.3 / `CERTS_RESUME` §4.0

**The route is sound, but as written it has a gap, and the gap costs one extra telescoping per
branch.** Recording it before any certificate is composed, because a certificate assembled from
the §5.3 formula as literally stated would be **wrong**.

### 9.1 The gap

§5.3 asserts: *"the letter-`m` component of `M·E` telescopes iff `M` is a telescoper for the
hypergeometric double sum `Σ e_m T`."* The first half is false. If
`M·(e_m T) = Δ_k X_m + Δ_l Y_m`, the letter-`m` component of `M·E` is

```
    m(n,k,l) · ( Δ_k X_m + Δ_l Y_m ) ,
```

and `m` **depends on `k` and `l`**, so this is not itself a `Δ_k` of anything: `Σ_{k,l}` of it does
not telescope. (`Σ_k m Δ_k X` telescopes only for `m` independent of `k`.)

### 9.2 The repair — one Abel summation, and it stays inside rank 1

Abel's identity `m Δ_k X = Δ_k(m X) − (Δ_k m)·X|_{k→k+1}` fixes it, and crucially
**`Δ_k m` is a rational function** — precisely because each `m` is a *single* letter, the same
property the route is built on. Writing `X_m = ρ_m e_m T`, `Y_m = σ_m e_m T`, and
`d_m^{(j)} = m(n+j,k,l) − m(n,k,l)` (rational), the correct identity is

```
M·E = Δ_k[ X_{c₀} + Σ_m m X_m ] + Δ_l[ Y_{c₀} + Σ_m m Y_m ] + G ,

G   = − Σ_m (Δ_k m)·X_m|_{k→k+1}  − Σ_m (Δ_l m)·Y_m|_{l→l+1}
      + Σ_j M_j(n) T(n+j,k,l) Σ_m e_m(n+j,k,l) d_m^{(j)} ,
```

valid whenever `M` is a telescoper, **with certificates**, for each of the six hypergeometric
summands `e_m T` and `c₀ T`. `G` is a rational multiple of `T` (every `X_m|_{k+1}` is
`ρ_m(k+1)e_m(k+1)T(n,k+1,l)` and `T(n,k+1,l)/T` is rational), so `G` is **hypergeometric** and a
final rank-1 telescoper `N` with `N·(Σ_{k,l} G) = 0` gives `N·M·F = 0` as intended.

So the plan is unchanged in shape — six rank-1 telescopers, an `LCLM`, one more rank-1 telescoper
— but the input to the last one is `G` **including the Abel corrections**, not merely the
"leftover second line" of §5.3. Omitting them is the error to avoid.

### 9.3 The Abel data (explicit, and cheap)

Each `Δ m` is a two-term rational function, and half of them vanish:

| `m` | `Δ_k m` | `Δ_l m` |
|---|---|---|
| `A₁(k)` | `1/(n+k+1) − 1/(k+1)` | `0` |
| `A₂(k)` | `1/(n+k+1)² − 1/(k+1)²` | `0` |
| `B₁(k)` | `−1/(n−k) − 1/(k+1)` | `0` |
| `C₁` | `1/(n+k+l+1) − 1/(k+l+1)` | `1/(n+k+l+1) − 1/(k+l+1)` |
| `A₁(l)` | `0` | `1/(n+l+1) − 1/(l+1)` |

and the `n`-shift data, `d_m^{(j)} = Σ_{i=1}^{j} δ_m(n+i)` with
`δ_{A₁(k)} = 1/(n+k+1)`, `δ_{A₂(k)} = 1/(n+k+1)²`, `δ_{B₁(k)} = 1/(n+1−k)`,
`δ_{C₁} = 1/(n+k+l+1)`, `δ_{A₁(l)} = 1/(n+l+1)` (each read off
`H⁽ʳ⁾_{x+1} = H⁽ʳ⁾_x + (x+1)^{−r}`).

### 9.4 Two ways to spend the extra telescoping, and which to prefer

* **Combined.** Take `M = LCLM(M_{c₀}, M_α, …, M_ε)` first, form the single `G` above, telescope
  once. One extra CT job, but `G` carries the LCLM cofactors `P_m` (`P_m ** M_m = M`) and is
  correspondingly large.
* **Per letter.** Do the Abel correction with each *individual* `M_m` (small), get
  `g_m = r_m·T`, telescope each to `N_m`, and finish with `LCLM(M_{c₀}, N₁M₁, …, N₅M₅)`.
  Five extra CT jobs, but every intermediate object stays the size of `e_m`, and the five jobs are
  independent, hence parallel across kernels.

The per-letter variant is the safer bet on this hardware: the combined `G` risks being the one
object big enough to make the last CT intractable, and there is no way to bound its cost in
advance. Either way the boundary conditions must be re-checked for the new certificates in the
**regularised** sense of §8.4 — at `k, l ∈ {0, K+1}` only.

### 9.5 Order budget

`F_n = 0` is known exactly for `n ≤ 77` (§4quater), so any `L'` with `L'·F = 0`,
`ord(L') ≤ 297`, and leading coefficient without integer roots in range closes Theorem B
(the exact range is now `n ≤ 300`, §10). `ord(N·M) ≤ ord(N) + Σ_m ord(M_m)` in the worst case,
and by §11 the sum is over **three** telescopers, not six. `seqdata.py NMAX` extends the range
further at `O(N³)`; `N = 300` took about 15 minutes.


### 8.5 Independent confirmation from the letter form — and where the poles are

The `ε`-regularised computation of §8.2 was done entirely from the `{ρ, σ}` side. The **letter**
side agrees, exactly and independently. Factoring the denominators of `Eletters.m`:

| coefficient | denominator factors involving `k − n` | pole of `T·(coef)·(letter)` at that locus |
|---|---|---|
| `c₀` | `(k−n)¹`, `(k−n−1)³`, `(k−n−2)³`, `(k−n−3)³` | simple at `k=n`; simple at `k=n+1,2,3` (order 3 vs `T`'s double zero) |
| `β` (coef. of `A₂(k)`) | `(k−n)¹`, `(k−n−i)³` | same |
| `α, γ, δ, ε` | `(k−n−i)²` only | finite at `k=n`; `γ·B₁(k)` gives a simple pole at `k=n+i` |

so `E(v)/T` has a **simple pole on `k = n`** (carried by `c₀` and `β` alone) and `E(v)` has simple
poles on `k = n+1, n+2, n+3`. That predicts singular cells exactly in the four rows
`k₀ ∈ {n₀, n₀+1, n₀+2, n₀+3}`, i.e. `4(K+1)` cells — **20, 24, 28, 32** for `n₀ = 1,2,3,4`.
Those are precisely the counts §8.3 measured, from a completely different expression for `E(v)`.
Two independent constructions agreeing on the location, order and count of the singularities is
the strongest check available on `Eletters.m`, and it covers the case `k = n` that the three
integer-point checks of §4ter (all with `k < n`) did not reach.

**Practical consequences.**

1. `Σ_{k,l=0}^{n} e_m(n,k,l) T(n,k,l)` is **not** the sequence the rank-1 telescopers annihilate:
   for `m ∈ {c₀, β}` the summand is singular at `k = n`, and for **all** `m` the cells
   `k` or `l ∈ {n+1,n+2,n+3}` contribute a finite non-zero amount (pole order ≤ 2 against `T`'s
   double zero). The correct object throughout is the box `[0,K]²`, `K ≥ n+3`, regularised at
   `n = n₀+ε`. Any numerical cross-check of `M_m` must use that object, not the naive `k,l ≤ n`.
2. Nothing in the certificate *search* is affected — creative telescoping is a formal computation
   on rational functions.

---

## §10. M3 — (b) `w5_allp`: pipeline prepared, and the cost is now a number

P1g (`work/PHASE2_RLETTER.md`) has **not** concluded — its §2.1 pins the obstruction in the
harmonic alphabet to **defect exactly 1** and the `R`-extended runs are still pending, so the
representative may still change. Per the standing rule of §1 (pointwise independence ⇒ no free
transfer between representatives), no `w₅` certificate was launched. What was prepared:

* **`work/lb5/make_w5m.py` → `work/lb5/w5folded.m`.** `w5_allp.json` (178 labelled terms) exported
  as a single parenthesised Wolfram expression in **folded** form: since `T` is `k↔l` symmetric,
  `Σ_{k,l} T·w₅ = Σ_{k,l} T·v₅` with `v₅ = Σ cf·C-part·N-part·(1 if f=g else 2)·f(k)g(l)`
  — the exact analogue of `v` for `ŵ₃` (§5.2). 172 of the 178 terms are asymmetric and get the
  factor 2.
  **[VERIFIED exact]** `Σ_{k,l≤n} T·v₅ = P_n` at `n = 2, 3, 4` (0 discrepancy), computed in a
  kernel that read only `w5folded.m`; `Count[v₅, HarmonicNumber[__], ∞] = 1021`, which is the
  anti-truncation assertion for this object.

* **The cost of the first weight-lowering step, exactly.** `E(w₅)/T` is spanned by the letter
  monomials that are **proper sub-monomials** of the 178 (each shift replaces a letter by
  letter + rational, so a degree-5 monomial contributes all its proper divisors):

  | | `E(v)` (`ŵ₃`) | `E(w₅)` (`w5_allp`) |
  |---|---|---|
  | monomials in the weight itself | 6 | 178 |
  | closure incl. sub-monomials | 7 | 386 |
  | **support of `E(·)/T`** | **6** (naive bound 7; `A₃(k)` cancels) | **≤ 208** |
  | by weight | all weight ≤ 1 | `1·w0 + 16·w1 + 63·w2 + 83·w3 + 45·w4` |

  So the property that makes Theorem B tractable — `E(v)` lands in **single letters**, hence every
  telescoping problem is **rank 1** — **fails at the first step for `w₅`**: only 17 of the ≤ 208
  monomials (the constant and the 16 weight-1 ones) are rank-1-reachable; 191 are not.
  `CERTS_RESUME` §5's "five iterations of the same step reach weight 0" is right in principle, but
  the first four iterations are **not** rank-1 problems, and the measured rank-1 cost
  (136 s + 412 s + 56 s + `ct₂`) is a *lower* bound per monomial. A realistic budget for (b) is
  therefore hundreds of telescoping problems, not six — this is the honest cost statement that
  should govern whether (b) is attempted at all on this hardware.

* **Order budget widened.** `seqdata.py 150` completed (`seqdata150.json`): `Σ T ŵ₃ = P̂_n`
  **exact for `n ≤ 300`** (`seqdata300.json`; the `n ≤ 150` stage is `seqdata150.json`), so
  `F_n = 0` is known for **`n ≤ 297`** (was 77). The step is cheap — `n ≤ 150` took under a minute — so the order of the final operator
  is no longer a binding constraint.

### 8.6 `Eletters.m` re-validated by a third, independent construction

`m2bnd.wl` builds `E(v)` from `{ρ, σ}` and `v` directly, with `T` as a `Pochhammer` polynomial and
every harmonic number normalised by hand — a code path sharing nothing with either the RISC
construction (`R_E.m`) or the MCP construction (`Eletters.m`). At `n₀ = 5`:

> **[VERIFIED exact]** `E(v)(5,k,l) − T(5,k,l)·(c₀+αA₁(k)+βA₂(k)+γB₁(k)+δC₁+εA₁(l))|_{(5,k,l)} = 0`
> at `(k,l) = (0,0), (2,3), (4,1), (1,4), (3,3)`, each cell also confirmed **regular**
> (no negative `ε`-coefficient). The `n₀ = 5` box check itself gives 36 singular cells
> ( `= 4(K+1)`, `K = 8`), all negative `ε`-parts cancelling, total `0`.

Together with §8.5 (agreement on the *location, order and count* of the singularities) this closes
the question of whether `Eletters.m` survived the MCP truncation trap: it did.

---

## §11. M1 — `E(v)` is really RANK 3, not rank 6: four of the six telescopers are the same

**`[PROVED — exact, `Together` of the ratios]`**

```
    γ = 3 α ,      δ = (3/2) α ,      ε = (1/2) α          (exact rational constants)
```

so, writing `Ψ := A₁(k) + 3B₁(k) + (3/2)C₁ + (1/2)A₁(l)`,

> ```
>     E(v) / T  =  c₀  +  β · A₂(k)  +  α · Ψ
> ```

— **three** basis elements, not six. (`LeafCount[Together[β/α]] = 66183` and
`LeafCount[Together[c₀/α]] = 88661`, so `β` and `c₀` are genuinely independent; the equality of the
four `LeafCount`s at 22317 in `Eletters.m` was the visible symptom.)

### 11.1 Why — and it is structural, not a coincidence

Every one of the four terms of `v` that carries a *product* has the **same** left factor `A₂(k)`:

```
v = H⁽³⁾_n + 2A₃(k) − A₂(k)·[ ½A₁(k) + (3/2)B₁(k) + ¾C₁ + ¼A₁(l) ]  =  H⁽³⁾_n + 2A₃(k) − ½A₂(k)Ψ.
```

In each bracket `[w(shift) − w]` of `E(w)`, a product `A₂(k)X` contributes
`A₂(k)·(X^{shift}−X) + (A₂(k)^{shift}−A₂(k))·X^{shift}`. The **second** piece is the only source of
a bare single letter `X`, and its prefactor `(A₂^{shift}−A₂)` does **not depend on `X`**. Hence the
coefficient of `X` in `E(v)/T` is `(that X's coefficient in v) × Λ` with

```
Λ = Σ_{j=1}^{3} c_j (T(n+j)/T)·a_j  −  ρ|_{k→k+1}(T(n,k+1,l)/T)·a′ ,
    a_j = Σ_{i=1}^{j} 1/(n+i+k)² ,   a′ = 1/(n+k+1)² − 1/(k+1)² ,
```

(the `σ` term drops: `A₂(k)` is invariant under `S_l`). With the `v`-coefficients
`−½, −3/2, −¾, −¼` this predicts `α:γ:δ:ε = 2:6:3:1` — exactly the measured `3, 3/2, 1/2`.
So `α = −½Λ`, and `Ψ = −2 ×` (the cofactor of `A₂(k)` in `v`).

### 11.2 Consequences — this is the largest single saving available on this route

1. **Three rank-1 telescoping problems, not six**: `T·c₀`, `T·β`, `T·α`. A telescoper of `e·T` is
   *identically* a telescoper of `(const · e)·T` (the certificates just scale), so
   **`M_γ = M_δ = M_ε = M_α`** — no computation needed for `γ, δ, ε`.
2. **`LCLM` over three operators, not six.** The order bound drops from `Σ_{m=1}^{6} ord(M_m)` to
   `ord(M_{c₀}) + ord(M_β) + ord(M_α)`, halving the order budget of §9.5 (which is now `147`
   anyway).
3. **Two Abel corrections, not five** (§9.3): `Δ_k A₂(k) = 1/(n+k+1)² − 1/(k+1)²`, `Δ_l A₂(k) = 0`,
   and for the composite letter, by linearity,
   `Δ_k Ψ = [1/(n+k+1) − 1/(k+1)] + 3[−1/(n−k) − 1/(k+1)] + (3/2)[1/(n+k+l+1) − 1/(k+l+1)]`,
   `Δ_l Ψ = (3/2)[1/(n+k+l+1) − 1/(k+l+1)] + (1/2)[1/(n+l+1) − 1/(l+1)]`.
   `Ψ` is a *sum* of single letters, so every shift of it is still `Ψ + rational` and the whole
   §9.2 repair applies verbatim with `Ψ` in place of the four separate letters.

### 11.3 Operational note (kernel time lost)

The two kernels launched at 01:30 were given `LABS=alpha,beta,gamma` and `LABS=delta,eps,c0`.
Under the above, **`gamma`, `delta` and `eps` are redundant**, i.e. kernel 2 was working on a
redundant letter (`delta`) and would then do a second redundant one (`eps`) before reaching the
one object nobody else is computing (`c₀`); kernel 1 will do a redundant `gamma` after `beta`.
A reallocation (`kill -KILL 829062`, relaunch on `c0`) was attempted and **blocked by the
permission system**, so both kernels were left to run their original programs. A successor with
kill rights should run exactly `LABS=alpha`, `LABS=beta`, `LABS=c0` — three jobs.

---

## §12. The finish, stated exactly (what "matching initial values" means here)

Let `M = LCLM(M_{c₀}, M_β, M_α)` (order `D`), `N` the rank-1 telescoper of the Abel-corrected
remainder `G` (order `e`), and

```
        L'  = N ** M            (annihilates  F_n = Σ_{k,l} E(v),  order  e + D)
        L'' = L' ** L_BZ        (order  e + D + 3)
```

* `L''` **contains `L_BZ` as a right factor by construction** — that is the whole point of the
  route, not an accident of the `LCLM`. (Whether `M` alone has `L_BZ` as a right factor is a
  separate question; `certY.wl` tests it by `OreReduce[M, {L_BZ}]` and logs the remainder.)
* `L''·R = 0` where `R_n = Σ_{k,l} T ŵ₃`, because `L_BZ·R = F` (§8.4, regularised) and `L'·F = 0`.
* `L''·P̂ = 0`, because `L_BZ·P̂ = 0` holds **by construction of the committed ladder**
  (`zeta-math/worthiness/falsify_data/manifest.json`: `"recurrence": "normalized order-3 (V6b)"`)
  and `L'' = L'·L_BZ`.
* Hence `D_n := R_n − P̂_n` satisfies `L''·D = 0`.

> **Initial values needed: exactly `ord(L'') = e + D + 3` consecutive `n` with `D_n = 0`, plus
> non-vanishing of the leading coefficient of `L''` at every integer `n ≥ 0` in the propagation
> range.** `D_n = 0` is `[VERIFIED exact]` for **`n = 0 … 300`** (`seqdata300.json`), i.e.
> **301 consecutive values**, so any `e + D ≤ 298` closes it.
> With three telescopers instead of six (§11) and `ord(M_m)` expected to be single digits, this is
> not a binding constraint.

The leading coefficient must be checked, not assumed: `L_BZ`'s own leading coefficient
`2(n+3)⁵(2n+5)a₀(n)`, `a₀(x) = 41218x³+198849x²+320790x+173057 > 0` for `x ≥ 0`, is non-vanishing
on `n ≥ 0` **[PROVED]**, but that of `N ** M` is a new object; `certZ.wl` prints it
(`Z_Lfinal.m`) precisely so its integer roots can be listed.

**Verification standard for every certificate in the chain.** Each single-certificate identity
`M_m·(e_m T) = Δ_k(ρ_m e_m T) + Δ_l(σ_m e_m T)` is a rational-function identity and is checked
`Together[…] === 0` by `work/lb5/certVU.wl`, which loads **no RISC package** and reads the saved
`OrePolynomial`s as inert data, rebuilding all shift ratios from the Γ-product form of `T`
(`verifycore.wl`). RISC is used only to *search*.

### 11.4 `α` in closed form — `[PROVED, checked to exactly 0]`

The mechanism of §11.1 is not just an explanation, it is a formula. With
`a_j = Σ_{i=1}^{j} 1/(n+i+k)²` (the `n`-shift of `A₂(k)`) and
`a′ = 1/(n+k+1)² − 1/(k+1)²` (its `k`-shift), and `c_j` the coefficients of `L_BZ`:

> ```
>       Λ  =  Σ_{j=1}^{3} c_j(n) · (T(n+j,k,l)/T) · a_j   −   ρ|_{k→k+1} · (T(n,k+1,l)/T) · a′
>       α  =  −Λ/2
> ```
> **`Together[α + Λ/2] = 0` exactly.** (The `σ` term is absent because `A₂(k)` is `S_l`-invariant.)

Equivalently, as a statement about the summand itself,

```
   T·α  =  −½ [ Σ_{i=1}^{3} (1/(n+i+k)²) Σ_{j=i}^{3} c_j T(n+j,k,l)  −  a′ ρ(n,k+1,l) T(n,k+1,l) ]
```

— a combination of **shifts of `T` with weights that are single simple fractions**, in place of the
22317-leaf `α`. This suggests a cheaper decomposition of the one telescoping problem that is
currently blocking (`T·α`): telescope the four pieces separately (three of them are `T` times
`1/(n+i+k)²` times a polynomial in `n`, i.e. barely harder than the Q-row's 4 s) and take the
`LCLM`, instead of one call on the fully-combined rational function. Not attempted here — no
kernel seat was free — but it is the first thing to try if `certUb.wl`'s `Support` ladder on
`T·α` also proves expensive.

---

# §13. P1e session 3 — the τ-SPLIT, and the death of the monolithic route

**Date:** 2026-07-25, 02:30–onwards. Read this before §§4–12: it supersedes the *route* (not the
mathematics) of §§9 and 11, and records two hard negative measurements.

## 13.1 The monolithic rank-3 attack is MEMORY-infeasible — `[MEASURED, hard failure]`

`certT3.wl` (`MODE=box`) is the direct attack on `E(v)/T = c₀ + β·A₂(k) + α·Ψ` promised by §11.
It was given a free kernel at 02:32. The pre-flight assertions passed —
`Together /@ {γ/α, δ/α, ε/α} = {3, 3/2, 1/2}` and `Ψ` with its 8 `HarmonicNumber`s — and
`LeafCount[T·(c₀+βA₂+αΨ)] = 132917`. It then spent **50 minutes inside `Annihilator`** and was
**OOM-killed at 14.4 GB RSS** (`dmesg`: `Out of memory: Killed process ... total-vm:19423188kB,
anon-rss:14365964kB`), on a 15 GB machine. No output, no checkpoint.

> **The rank is not the cost. The coefficient size is.** `E(v)` has rank 3, but its three
> coefficients carry 66499 / 44011 / 22317 leaves, and RISC's ∂-finite closure blows up on them.
> `Annihilator` on the *rank-12* `T·v` cost 124 s (§2) because *its* coefficients are trivial.
> Any future plan that budgets by module rank alone is mis-budgeted.

The same disease is what stalled `certU`/`certUb`: the per-letter problems are rank **1**, and
still cost 136 s + 412 s + (a `ct₂` that ran 79 minutes without returning, over two sessions).

## 13.2 A NEW variant of the line-truncation trap — a line ending in `<|`

`math < file.wl` does **not** merely truncate here, it *errors and drops the assignment*:

```
Syntax::sntxf: "" cannot be followed by "uW = <|".
```

for the perfectly ordinary

```
tauW = <|
  "n1" -> ..., ... |>;
```

`<` and `|` are also standalone operators, so `x = <|` is a *locally decidable* syntax error
rather than an incomplete expression; the reader gives up, and the following lines then fail in
turn. The symbol `tauW` stays undefined and propagates into the summand as an inert head. Two
kernels were launched on the resulting wrong object and had to be reaped (cost ≈ 4 minutes,
because the assertion below caught it).

* `wlcheck.py` **did not flag this** — its `balanced()` counts only `([{`. It has been extended
  with `assoc_delta()`, which reports **FATAL** for any line ending at a `<|` token. Re-running
  it over the existing scripts found no other instance (`certVU.wl` and `certUb.wl` split an
  association across lines but end the first line on a comma, which continues correctly).
* The general lesson, third time this trap has been paid for: **every derived object must carry
  an assertion that aborts the run.** `certP.wl` now refuses to telescope unless its split check
  returns `{0,0,0,0}` — that is what turned this from a lost session into a lost 4 minutes.

## 13.3 The τ-split — `[CERTIFIED, RISC-free, symbolic]`

The coefficients of `E(v)` are large only because each is a **sum over the five shift terms** of
`E(v)`. Split *before* telescoping. With `v = H⁽³⁾_n + 2A₃(k) − ½A₂(k)Ψ` and `certS.wl`'s own
definition of `E(v)`, write `E(v) = Σ_τ F_τ` over `τ ∈ {n₁, n₂, n₃, kk, ll}`, where

```
F_τ = G_τ · ( p_τ + q_τ·A₂(k) + r_τ·Ψ ) ,

G_{n_j} = c_j T(n+j,k,l) ,   G_{kk} = −ρ(n,k+1,l) T(n,k+1,l) ,
                             G_{ll} = −σ(n,k,l+1) T(n,k,l+1) ,

p_τ = h3_τ + 2a3_τ − ½ dA2_τ dΨ_τ ,     q_τ = −½ dΨ_τ ,     r_τ = −½ dA2_τ ,
```

`dA2_τ = τA₂(k) − A₂(k)`, `dΨ_τ = τΨ − Ψ`, `h3_τ = τH⁽³⁾_n − H⁽³⁾_n`, `a3_τ = τA₃(k) − A₃(k)`
— **every one a short rational function**, because `τ(A₂Ψ) − A₂Ψ = A₂ dΨ + dA2 (Ψ + dΨ)`.

> **`[CERTIFIED — RISC-free, SYMBOLIC in ℚ(n,k,l)[hh…]]`** (`certPv0.wl`, run in a kernel that
> never loaded HolonomicFunctions):
> ```
> Σ_τ F_τ / T  −  ( c₀ + β·A₂(k) + α·Ψ )  =  0        (9 hh-symbols, 11 coefficient classes,
>                                                      0 non-zero)
> ( c₀ + β·A₂(k) + α·Ψ )  −  Ecanon  =  0
> ```
> This is stronger than the four exact integer points `certP.wl` asserts, and it re-derives
> §11's `{γ/α, δ/α, ε/α} = {3, 3/2, 1/2}` on the way. It also gives `Eletters.m` a **fourth**
> independent confirmation (cf. §8.6).

Consistency with §11.4: `α = Σ_τ (G_τ/T) r_τ = −½ Σ_τ (G_τ/T) dA2_τ = −Λ/2`, which §11.4 had
already checked to exactly `0` — so the split is the *mechanism* behind that closed form, applied
to all three coefficients at once instead of only `α`.

**What it buys.** The five weights have `LeafCount` **84, 86, 66, 12471, 2255** — against 132917
for the monolith and 66499 for `c₀` alone. Each `F_τ` is ∂-finite of rank ≤ 3 in the *same* two
letters. Measured (`certP.wl`):

| stage | monolith (`certT3`) | τ-split, `τ = ll` |
|---|---|---|
| summand `LeafCount` | 132917 | 2318 |
| `Annihilator` | **OOM at 14.4 GB after 50 min** | **4 generators in 2 s** |

**No Abel correction is needed** (contrast §9): the letters are never factored out of the
summand — the whole ∂-finite `F_τ` is telescoped — so the §9.1 gap cannot arise. The Abel
machinery of `certZ.wl` is superseded for this route.

**Scripts.** `certP.wl` (per-τ `Annihilator` → `ct₁` → Gröbner → bounded `Support` ladder for
`ct₂`, checkpointed per stage, `MemoryConstrained` per stage), `certPy.wl` (compose each two-step
certificate, `LCLM`, right cofactors, `X̂_τ = P_τ**Ck_τ`), `certPv.wl` / `certPv0.wl` (RISC-free
verification), `certT3f.wl` (`L'' = M ** L_BZ`, leading coefficient, initial-value count).

---

# §14. S4 — costed verdict for (b) `(T1-top)` — **target superseded by §15, cost model still valid**

> **Read §15 first.** `PHASE2_THEOREM.md` **v4** (`(GAP-DESC)` proved, P1i) collapses the
> certificate target for the `P_n` denominator law to the *single* identity `P_n = Σ T·w₅^I`,
> and makes Theorem B a middle-row obligation rather than a headline one. §14 below was written
> against `w5_allp`; its **cost model transfers unchanged** (§15 measures `w₅^I` and finds it no
> better), but its §14.3(i)/§14.4 recommendations are superseded.

*Assessment only; no heavy run was made for (b) this session. The numbers below are the measured
Theorem-B costs of §§2, 13 plus the `w₅` sizing of §10.*

## 14.1 What made Theorem B tractable, stated as a checklist

| enabling property | `ŵ₃` | `w5_allp` |
|---|---|---|
| monomials in the weight (folded) | 6 | 178 |
| support of `E(·)/T` | **6**, all weight ≤ 1 | **≤ 208**: `1·w0 + 16·w1 + 63·w2 + 83·w3 + 45·w4` |
| every product shares one left factor (§11.1) | **yes** — `v = H⁽³⁾ + 2A₃(k) − ½A₂(k)·Ψ` | **no** |
| ⇒ rank of the ∂-finite module to telescope | **3** (and ≤ 3 per τ-piece) | **≈ 200** |
| coefficient size after the τ-split (§13.3) | ≤ 12471 leaves | small — the τ-split *does* transfer |

The τ-split of §13.3 is the one ingredient that carries over unchanged: `E(w₅) = Σ_τ G_τ(τw₅ − w₅)`
holds for **any** weight, and keeps the coefficients small. What does **not** carry over is the
rank. `τw₅ − w₅` spans the proper sub-monomials of the 178, so each `F_τ` has rank ≈ 200 in place
of 3, and rank is what the *closure* step costs.

## 14.2 Direct route on this hardware — **NOT FEASIBLE**

Hard data points, all from this machine (15 GB, ~2 cores per kernel, 2 standalone seats):

* rank 3, coefficients 66499/44011/22317 leaves → `Annihilator` **OOM at 14.4 GB / 50 min** (§13.1);
* rank 12, trivial coefficients → `Annihilator` 124 s, then **no telescoper** in `Support` boxes
  up to `(2,3)`, whose costs were already 13 s / 12 s / **194 s** and climbing steeply (§2);
* rank 1, 22317-leaf coefficient → 136 s + 412 s + 56 s, and a `ct₂` that ran **79 minutes over
  two sessions without returning**.

Rank ≈ 200 with three variables is two orders of magnitude beyond the point at which the closure
already exhausts 15 GB. Iterating the weight-lowering to reach rank 1 needs the analogue of the
§11 collapse at every step; without a common left factor the number of independent CT problems is
of order the number of sub-monomials, i.e. **≥ 200 problems at ≥ 10 min each ⇒ ≥ 35 kernel-hours
as a floor**, with no guarantee that any individual `ct₂` terminates (three did not, this session
and last). **Verdict: do not attempt on this hardware.**

## 14.3 The two named alternatives, costed

**(i) The homogeneous kernel identity via `w₅^I`** (`PHASE2_RLETTER.md`, final paragraph).
`Δ := w₅^I − w5_allp` satisfies `Σ_{k,l} T·Δ = 0`. This does **not** reduce the problem — it
*adds* one: certifying `w₅^I` = certifying `w5_allp` **plus** certifying `Σ T·Δ = 0`, and by §1
the latter is a non-trivial identity of the same weight. Its one genuine advantage is that a
homogeneous target admits an **order-0** certificate: one may look directly for rational `X, Y`
with `T·Δ = Δ_k X + Δ_l Y`, which is a *bounded linear solve* in the letter basis (the
`ptrank.py` / `rfit.py` machinery, mod `p`, no Wolfram kernel) rather than a Gröbner computation.
Cost of the experiment: ≈ 1–2 h of Python. It is a lottery ticket — nothing guarantees an exact
certificate exists — but it is cheap and it is the only proposal here that is affordable today.

**(ii) Guessed recurrence + 301 initial values.** This is **not an independent route.** §6.1
already *has* the operator: the minimal recurrence of `Σ T·w5_allp` is `(order 3, degree 9)`,
nullity 1, i.e. exactly `L_BZ`, with 0 mismatches against `P_n` for every `n ≤ 360` and 0 residual
at all 748 values over two primes. What is missing is the **certificate**, and producing one is
exactly §14.2. (The initial-value half is free: `seqdata.py` extends the exact range at `O(N³)`;
`n ≤ 300` took ~15 min for `ŵ₃`, and `w5_allp` is ~30× more work per cell, so `n ≤ 300` exact for
`w₅` is a few kernel-hours — worth doing only once a certificate is in sight.)

## 14.4 Recommendation — deferral, with a precise and *new* object to look for

Defer (b). The object needed is **not** more compute; it is a better representative:

> **Find `w₅′` in the affine space `w5_allp + ker(fit)` (135-dimensional) that (a) is cell-wise
> `p`-integral for every `p ≥ 5`, and (b) minimises the support of `E(w₅′)/T` — ideally has the
> §11.1 product structure `w₅′ = (harmonic-only part) + A_r(k)·(linear form in letters)`, which
> is what collapses the rank from ≈ 200 to O(1).**

This is legitimate *because* §10 records that `(BASE)` is a statement about the **number** `P_n`:
any exact decomposition with cell-wise integrality proves it, so the downstream `(GAP-5)` closure
does not require `w5_allp` specifically — only a representative with the integrality property.
(The §1 `[PROVED negative]` still stands: it forbids transferring a *certificate* between
representatives for free, not choosing a better representative to certify.)

The search is pure exact linear algebra over the 448-monomial basis — the `ptrank.py` / `e3_solve.py`
machinery already in `work/p1g/` — with an objective function (size of the sub-monomial closure of
the support) that is combinatorial and cheap to evaluate. Estimated 2–4 h of Python, **no Wolfram
seat**, and it is the only step that changes the cost class of (b) rather than grinding at it.
If no such representative exists, that is itself a publishable structural obstruction and should
be recorded as one.

## 13.4 Measured cost of the τ-split, and the verdict on Theorem B this session

All on the 15 GB / 2-standalone-seat box, 2026-07-25 02:32–04:15.

| object | `LeafCount` | `Annihilator` | first `CreativeTelescoping` |
|---|---|---|---|
| monolith `T(c₀+βA₂+αΨ)`, rank 3 | 132917 | **OOM, 14.4 GB, ~50 min** | — |
| `F_ll`, rank 2 | 2318 | **2 s**, 4 generators | elim `k` unbounded: **> 9 min, no return** |
| `F_ll`, rank 2 | 2318 | (checkpoint) | elim `l` unbounded: **> 17 min, 4.3 GB, no return** |
| `F_ll`, rank 2 | 2318 | (checkpoint) | elim `l`, `Support` box 3×3: **> 9 min, no return** |
| `F_kk`, rank 3 | 13069 | **> 37 min, no return** | — |
| `T·e_α`, rank 1 (prev. session) | 22317 | 136 s | 412 s; then `ct₂` **79 min, no return** |

> **The τ-split fixes the `Annihilator` step and does not fix the `CreativeTelescoping` step.**
> The closure went from *impossible* (OOM at rank 3) to **2 seconds**; but the elimination steps
> cost tens of minutes each regardless of which variable is eliminated first, and — the new and
> important negative — **bounding the support does not bound the cost.** `Support -> {…}` bounds
> the *telescoper's* ansatz, but the certificate is still an unknown rational function, so the
> step remains a parametrised Gosper/Abramov problem of full size. `CERTS_RESUME` §1's
> "`Support` turns the step into a finite linear solve that terminates" is true about
> *termination* and **false about cost**; the 13 s / 12 s / 194 s box timings of §2 were on an
> object with trivial coefficients and are not representative.

**Theorem B is therefore NOT `[CERTIFIED]` at the end of this session.** What is new and solid:

* the τ-split identity `E(v) = Σ_τ F_τ`, **[CERTIFIED — RISC-free, symbolic]** (§13.3);
* the closure step is no longer a blocker (2 s vs OOM);
* the residual obligation is reduced to **exactly five creative-telescoping problems**, each on a
  rank-≤3 module with coefficients of ≤ 13069 leaves — a completely explicit, checkpointed,
  restartable task list (`certP.wl` / `certP2.wl`), with the whole downstream chain
  (`certPy.wl` → `certPv.wl` → `certT3f.wl`) written, `wlcheck`-clean and waiting.

**Honest budget for a successor**: 5 τ × (`ct₁` + Gröbner + `ct₂` ladder). On the observed
> 10 min per elimination and 2 seats, that is **4–10 kernel-hours**, and it is the *whole*
remaining cost of Theorem B — there is no further mathematics to discover. The single highest-value
experiment for whoever picks this up is **`CT2V=sn`** and the `CT1A`/`CT1B` box sweep in
`certP2.wl`: if a small box does land a `ct₁`, the rest follows in minutes.

---

# §15. S4 REVISED for `PHASE2_THEOREM.md` v4 — costing `(T1-top)` against `w₅^I`

**Input from the orchestrator (2026-07-25 ~04:30).** `(GAP-DESC)` is proved; no mathematical node
of the `p ≥ 5` side is open. Two accuracy corrections change the target:

1. the `P_n` denominator law needs **only** `(T1-top)`; the `ŵ₃` / Theorem-B certificate is a
   *middle-row* obligation (Theorem E), not the headline;
2. `(BASE)` and `(IND)` are representative-independent and are `[VERIFIED]` for `w₅^I`, so the
   whole `p ≥ 5` theorem runs on `w₅^I` alone and the certificate target is the **single**
   identity `P_n = Σ_{k,l} T·w₅^I` (`work/p1g/w5_exIII_allp.json`, 207 terms). The v3
   "`w5_allp` + homogeneous delta" composition is an alternative, not a requirement.

## 15.1 The 208-monomial obstacle applies to `w₅^I` **equally — in fact slightly worse**

`work/lb5/esupp.py` (new; reproduces §10's `208 = 1·w0+16·w1+63·w2+83·w3+45·w4` for `w5_allp`
exactly, which is its validation):

| representative | terms | monomial **degrees** | support of `E(·)/T` | by weight |
|---|---|---|---|---|
| `ŵ₃` folded (`v`) | 6 | **≤ 2** | **6** | all `≤ w1` |
| `w5_allp` | 178 | 1…5 | 208 | `1,16,63,83,45` |
| **`w₅^I` = `w5_exIII_allp`** | **207** | 1…5 | **220** | `1,17,65,86,51` |
| `w5_I` (155-term, depth-minimal) | 155 | 1…5 | 184 | `1,16,59,74,34` |
| `w5_exIII_b` | 148 | 1…5 | 185 | `1,15,56,70,43` |
| `w5_Rbase` (uses `R₃(l)`) | 70 | **≤ 4** | **100** | `1,15,47,37` |

> **Answer to the question asked: yes, equally.** Switching the target from `w5_allp` to `w₅^I`
> moves the rank of the module that creative telescoping must close from **208 to 220**. Nothing
> about §14.2's verdict changes.

## 15.2 The real structural statement — it is the **degree**, not the weight

Each shift replaces a letter by *letter + rational*, so a monomial of **degree `d`** (number of
letter factors, squarefree) contributes `2^d − 1` proper sub-monomials to `E(·)/T`. Hence

> **support of `E(w)/T` grows exponentially in the maximum monomial DEGREE, and not at all in the
> weight.** `ŵ₃` is weight 3 but its folded form `v = H⁽³⁾_n + 2A₃(k) − ½A₂(k)·Ψ` has degree
> **≤ 2** — *that* is why `E(v)` has support 6 and why §11's rank-3 collapse exists at all.
> Every available `w₅` carries degree-4 and degree-5 monomials (44–53 of them), and a single
> squarefree degree-5 monomial alone already contributes **31** sub-monomials.

This reframes §14.4's proposal into a sharp and *testable* one. It is not "find a representative
with small support" (vague) but:

> **Does the fitting system admit a solution supported only on weight-5 monomials of degree ≤ D?**
> `D = 2` would give support ≈ 15 and put `(T1-top)` in the same cost class as Theorem B;
> `D = 3` gives support ≈ 50 and a ~4× saving, still not enough; `D = 4` is `w5_Rbase`'s 100.

**Counting says `D = 2` is almost certainly impossible in the harmonic alphabet.** Degree-≤2
weight-5 monomials number about `6 + 6·6 + 6·6 = 78` (six weight-`r` letter kinds
`A_r(k), B_r(k), A_r(l), B_r(l), C_r, N_r` per weight, splits `5` and `1+4`, `2+3`), against a
fitting system of rank **313** in the base alphabet. Consistency of the system restricted to 78
columns is a codimension-enormous coincidence. `D = 3` is the only one worth testing.

**Cost of the test: hours of Python, no Wolfram seat** — it is exactly `work/p1g/e2.py`'s
rank-plus-consistency computation with the columns filtered by degree, and it is decisive either
way. If `D = 3` is inconsistent too, the direct route for `(T1-top)` is **closed on this
hardware** and should be recorded as a structural obstruction, not a resource shortfall.

## 15.3 The guessed-recurrence + initial-values route, costed for `Σ T·w₅^I`

This is the orchestrator's fallback, and it is worth stating precisely why it does **not** avoid
the cost:

* **The operator is not the missing object.** §6.1 already establishes, for `Σ T·w5_allp`, that the
  minimal recurrence is `(order 3, degree 9)`, nullity 1, i.e. **exactly `L_BZ`**, with 0 residual
  at 748 consecutive `n` over two primes and 0 mismatches against `P_n` for every `n ≤ 360`. The
  same computation for `w₅^I` is a `w5rec.py` rerun — cheap, and it will say the same thing.
* **What is missing is a *certified* `L` with `L·(Σ T·w₅^I) = 0`**, and producing one is a creative
  telescoping on the rank-220 module — §14.2, unchanged. Guessing does not certify.
* **The initial-value half is genuinely cheap and worth banking now.** If a certified `L` ever
  lands, `L'' = LCLM(L, L_BZ)` annihilates `D_n = Σ T·w₅^I − P_n`, and `ord(L'')+1` exact values
  finish it. For `ŵ₃` we have 301 exact values (`seqdata300.json`); the analogue for `w₅^I` is the
  same `seqdata.py` machinery at `O(N³)` with ~30× the per-cell work (207 terms vs 6). Current
  exact range for `w₅^I` is only `n ≤ 20` (`PHASE2_RLETTER` §13).

> **Recommendation.** (1) Run the degree-`≤3` consistency test of §15.2 — it is the only cheap
> experiment that can change the cost class, and its negative answer is itself a result.
> (2) Independently, extend the exact range for `Σ T·w₅^I` with `seqdata.py`, because it is
> cheap, it is needed by *every* route, and it is the half of the argument that is not blocked.
> (3) Do **not** start a rank-220 creative telescoping on this hardware.

## 15.4 Consequence for Theorem B's priority

Under v4 Theorem B is no longer on the critical path for the `P_n` denominator law — it supports
Theorem E (middle row) and the paper. Its residual cost is now **4–10 kernel-hours with no new
mathematics** (§13.4), against `(T1-top)`'s **blocked-pending-a-structural-idea**. So Theorem B
remains the right thing to finish first on a machine with kernel seats to spare, and `(T1-top)`
should wait for the §15.2 test rather than for compute.

---

# §16. P1e session 4 — M0: the degree-≤3 experiment. **INCONSISTENT.**

`§15.2` proposed the one cheap experiment that could have changed `(T1-top)`'s cost class:

> **Does the weight-5 fitting system admit a solution supported only on letter monomials of
> degree ≤ D?**

It has now been run. **The answer is no, for `D = 2`, `D = 3` and — in the plain harmonic
alphabet — `D = 4`.** The obstruction is *not* the depth conditions: **the fit identity alone is
already inconsistent**, so no choice of pole-cap regime (`base` / `vt2` / `exIII` / `strong`) can
rescue it.

New file: **`work/lb5/degfit.py`** — `e2.py`'s rank-plus-consistency computation with the basis
columns filtered by monomial degree. `degree(element) = |f| + |g| + |h| + |s|` for the basis
element `[f|g]x h x s`, i.e. the same degree that `esupp.py` uses to count the support of
`E(w)/T`. Run as `python3 degfit.py MODE KSPEC CSPEC NSPEC N q DLIST`; `NOCOND=1` skips the
depth-condition block (the fit-alone verdict is `MODE`-independent, so this loses nothing).
Design matrices are cached as `DF_<K>_<C>_<N>_<N>_<q>.npz`.

## 16.1 Validation of the harness

`degfit.py base|exIII AB C N 600 33554393` at `D ≤ 5` (i.e. unrestricted) reproduces the
previously recorded numbers exactly:

* **`rank(fit) = 313`** — §15.2's quoted rank of the base-alphabet fitting system;
* `exIII`: `448` columns, **`212` condition rows, `rank(joint) = 342`, consistent** — identical to
  `work/p1g/exIII.log`, the run that produced `w5_exIII.json = w5_I.json`;
* `strong` at `D ≤ 5` is **inconsistent**, which is exactly why the `exIII` cap regime was
  introduced in the first place.

So the machinery reproduces both a known positive and a known negative.

## 16.2 The measurement

`N = 600` fitting equations, `q = 33554393` (confirmed at `q = 33554467`, §16.3).
`fitINCONS` = the fit identity alone is unsatisfiable; `INCONSISTENT` = fit + depth conditions.

### (a) plain harmonic alphabet `A_r(k), B_r(k), C_r, N_r` — 448 columns

| cap | cols | `rank(fit)` | fit alone | condrows (`exIII`) | `rank(joint)` | verdict |
|---|---|---|---|---|---|---|
| `D ≤ 2` | 44 | 41 | **INCONSISTENT** | 66 | 42 | **INCONSISTENT** |
| `D ≤ 3` | 176 | 151 | **INCONSISTENT** | 163 | 160 | **INCONSISTENT** |
| `D ≤ 4` | 338 | 269 | **INCONSISTENT** | 212 | 292 | **INCONSISTENT** |
| `D ≤ 5` | 448 | 313 | consistent | 212 | 342 | **consistent** |

### (b) Apéry-letter alphabet `+ R_r(k)` (`rfit.KL`) — 1210 columns

| cap | cols | `rank(fit)` | fit alone | verdict |
|---|---|---|---|---|
| `D ≤ 2` | 73 | 69 | **INCONSISTENT** | **INCONSISTENT** |
| `D ≤ 3` | 369 | 329 | **INCONSISTENT** | **INCONSISTENT** |
| `D ≤ 4` | 841 | 600 | consistent — but **vacuously**, `rank = N`, see the caveat below | consistent |

### (c) depth-2 nested alphabet `A,B,Y_ab | C,V_ab | N,Z_ab` — 868 columns

| cap | cols | `rank(fit)` | fit alone | `rank(joint)` | verdict |
|---|---|---|---|---|---|
| `D ≤ 2` | 160 | 139 | **INCONSISTENT** | 146 | **INCONSISTENT** |
| `D ≤ 3` | 488 | 327 | **INCONSISTENT** | 351 | **INCONSISTENT** |
| `D ≤ 4` | 758 | 400 | consistent | 427 | **INCONSISTENT** (depth conditions fail) |
| `D ≤ 5` | 868 | 401 | consistent | 429 | consistent |

> **Caveat that must be read with any positive entry.** The test is only meaningful while
> `rank(fit) < N`; if the restricted columns already span all of `F_q^N` then *every* right-hand
> side is representable and "consistent" says nothing. That is what happens at `ABR`, `D ≤ 4`
> (`rank = 600 = N`) — re-run at `N = 1300` before reading anything into it. Every **negative**
> entry above is immune to this: at `D ≤ 3` the ranks are `151 / 329 / 327` against `N = 600`,
> i.e. the systems are overdetermined by `449 / 271 / 273` independent equations and fail.

### (d) what the known representatives actually look like

Degree histograms of every extracted `w₅` (same `monomial()` as `esupp.py`), for comparison with
the column counts above — the fitted solutions sit exactly where the consistency test says they
must, with the bulk of their mass at degree 4–5:

| representative | terms | degree histogram | terms of degree ≤ 3 |
|---|---|---|---|
| `w₅^I` = `w5_exIII_allp` | 207 | `1:3, 2:19, 3:59, 4:73, 5:53` | 81 |
| `w5_allp` | 178 | `1:2, 2:14, 3:52, 4:66, 5:44` | 68 |
| `w5_I` | 155 | `1:2, 2:14, 3:49, 4:61, 5:29` | 65 |
| `w5_Rbase` | 70 | `1:2, 2:12, 3:34, 4:22` | 48 |
| **`ŵ₃` folded `v`** | **6** | **`1:4, 2:2`** | **6 (all of them)** |

## 16.3 Second prime

Inconsistency mod one prime is already conclusive in the direction that matters (a system
consistent over `ℚ` is consistent mod all but finitely many `q`), but it was re-run at
`q = 33554467` for the two depth-1 alphabets and the verdicts are identical — see
`degfit_base_AB_q2.log`, `degfit_base_ABR_q2.log`.

## 16.4 What this settles

1. **`(T1-top)` cannot be made tractable by choosing a low-degree representative.** The v3 target
   `w5_allp` (support 208), the v4 target `w₅^I` (support **220**) and the best available
   `w5_Rbase` (degree ≤ 4, support 100) are not accidents of a particular extraction order: the
   fitting system *has no degree-≤3 solution at all*, in any of the three alphabets, and the
   plain harmonic alphabet has no degree-≤4 solution either. `ŵ₃`'s degree-≤2 folded form — the
   single structural fact that made Theorem B's route exist — **has no weight-5 analogue.**
2. **The obstruction is arithmetic-free.** It sits in the fit identity `P_n = Σ_{k,l} T·w`, not in
   the `p`-integrality conditions. Enlarging the alphabet with Apéry letters `R_r(k)` (a genuine
   enlargement — it is what makes the degree-≤4 representative `w5_Rbase` exist) or with true
   depth-2 nested letters `Y_ab, V_ab, Z_ab` does not move the `D ≤ 3` verdict.
3. **Adding depth would not have helped even had it worked.** The nested alphabet buys degree by
   spending *depth*: a single `Y_ab(k)` is degree 1 but its `∂`-module is not rank 2 — shifting it
   produces `A_a(k), A_b(k), H^{(a)}_k, H^{(b)}_k` — so the `2^d` support model must be replaced by
   roughly `4^d`. A degree-≤3 nested solution would have had support ≈ 64, not ≈ 8. The
   experiment's *positive* branch was therefore already narrow, which is part of why the negative
   is worth recording rather than reopening.

> **VERDICT — `(T1-top)` is [BLOCKED BY A STRUCTURAL OBSTRUCTION, not by compute].**
> `§15.2`'s own criterion: *"If `D = 3` is inconsistent too, the direct route for `(T1-top)` is
> closed on this hardware and should be recorded as a structural obstruction, not a resource
> shortfall."* That is now the recorded state. The cheapest certified route to `(T1-top)` is a
> creative telescoping on a rank-**100** (`w5_Rbase`) to rank-**220** (`w₅^I`) `∂`-finite module,
> against rank 3 for Theorem B — and Theorem B's rank-3 problem is itself not yet finished
> (§13.4, §17). Nothing short of a new idea about the shape of `w₅` changes this.

## 16.5 What a successor should NOT re-run

* the degree cap at `D ≤ 2, 3` in the alphabets `AB / ABR / ABY` — done, negative, two primes;
* `strong` mode at any degree — inconsistent even unrestricted;
* "find a representative with small support" as an open-ended search — the degree axis is now
  closed; only a **new letter kind** whose `∂`-module is rank 2 and whose weight is 4 or 5 could
  reopen it, and `R_r(k)` (the one such candidate that exists in this codebase) has been tested.

---

# §17. P1e session 4 — M1: Theorem B. Measurements, and the one untried route.

## 17.1 The two session-4 kernel failures, and what they change

Both kernels inherited from session 3 were inside their τ's most expensive stage. Neither
finished; both ended by **diverging in memory**, and in both cases
`MemoryConstrained[·, MEMCAP]` **did not fire** — the same behaviour as the §13.1 monolithic OOM.
**The cause has now been found and it is a bug in our own harness, not a property of RISC — see
§17.5.** Read §17.5 before drawing any conclusion from the timings in this section.

| job | stage | outcome |
|---|---|---|
| `certP.wl TAUS=kk ORD=kl MEMCAP=4e9` | `Annihilator[F_kk]` (13069 leaves) | **OOM-killed at 85 min** (`dmesg`: `oom-kill … task=WolframKernel … anon-rss:7799548kB`). RSS grew monotonically — 1.5 GB (46 min) → 3.7 GB (63 min) → 6.6 GB (74 min) → 8.5 GB (82 min), i.e. ≈ **250 MB/min** with no sign of levelling off. |
| `certP2.wl TAUS=ll,… ORD=lk CT1A=3 CT1B=3 MEMCAP=3.5e9` | `Support`-boxed 3×3 `ct₁` for `F_ll` (rank 2) | **> 67 min, no return, 7.6 GB and climbing.** §13.4 had recorded "> 9 min, no return" for the same box; the extra hour bought nothing. |

> **Consequences, stated plainly.**
> 1. `MEMCAP` was not a control — **because of the §17.5 bug**, not because `MemoryConstrained`
>    is unreliable. With the one-line fix applied it aborts correctly, and these two runs would
>    have returned `$Aborted` at 3–4 GB instead of starving the machine. Note also that
>    **`kill -KILL` is blocked by the permission system on this box** (blocked again this
>    session, as in §7.7), so without a working `MEMCAP` one simply waits ~20 minutes for the
>    OOM killer.
> 2. **`Annihilator[F_kk]` is now a *measured* failure, not an unknown.** It is the single object
>    the τ-split cannot compute, and the τ-split needs all five τ. §8.7's advice ("if `1038875`
>    lands `P_kk_ann.m`, that is the single most expensive object of the whole route and must not
>    be recomputed") should be replaced by: **do not attempt `Annihilator[F_kk]` in this form
>    again** — 7.8 GB was not close to returning.
> 3. The §13.4 budget of **"4–10 kernel-hours, no new mathematics" is not confirmed** and should
>    not be quoted. Two of the five τ have now consumed ~2.4 kernel-hours between them and
>    produced nothing. The honest statement is in §17.4.

## 17.2 The cost table that was missing — τ-split **×** letter-split

`E(v) = Σ_τ F_τ` with `F_τ = G_τ (p_τ + q_τ A₂(k) + r_τ Ψ)`. Two independent splittings have
been tried, each fixing one axis and leaving the other:

* **`certU` (letter-split, §4.0/§11)** — rank 1, but the cofactors `c₀, β, α` have
  **22317 / 44011 / 66499** leaves. Measured: `Annihilator` 136 s, `ct₁` 412 s, `ct₂` **79 min,
  no return**.
* **`certP` (τ-split, §13.3)** — small cofactors, but rank ≤ 3. Measured: §17.1.

The **combination** — split by τ *and* by letter — has never been tried, and every one of its
pieces is a **rational multiple of `T`** (rank 1) with a *small* cofactor. Measured this session
in the MCP kernel (RISC-free, `Together` of the ratio to `T`):

| τ | `LeafCount(G_τ)` | `G_τ p_τ / T` | `G_τ q_τ / T` | `G_τ r_τ / T` |
|---|---|---|---|---|
| `n1` | 84 | 429 | 215 | 121 |
| `n2` | 86 | 4262 | 935 | 151 |
| `n3` | 66 | 15027 | 2810 | 190 |
| `kk` | 12471 | 10905 | 10758 | 10611 |
| `ll` | 2255 | **0** | 1913 | **0** |

**13 non-zero rank-1 problems**, nine of them under 3000 leaves and six under 1000 — against
`certU`'s three problems at 22317–66499 leaves and `certP`'s five rank-3 problems. This is the
cell of the 2×2 table that is small on *both* axes, and it is the route a successor should take.
Its one cost is the §9.2 Abel correction (already implemented in `certZ.wl`), needed wherever a
letter is pulled through a `Δ`.

## 17.3 `τ = ll` needs no Abel correction at all — `[PROVED]`, and it is running

The table's two exact zeros are not a rounding artefact: `certP.wl`'s definitions give
`dA2f["ll"] = 0`, hence `r_ll = −½ dA2_ll = 0` and `p_ll = h3_ll + 2a3_ll − ½ dA2_ll dPsi_ll = 0`
(`h3_ll = a3_ll = 0` as well). Therefore, **exactly**,

```
    F_ll  =  (G_ll q_ll) · A₂(k) ,      G_ll q_ll = (rational, 1913 leaves) × T ,
```

and `A₂(k) = H⁽²⁾_{n+k} − H⁽²⁾_k` **does not depend on `l`**. So

```
    Σ_l F_ll  =  A₂(k) · Σ_l (G_ll q_ll)
```

with no Abel correction of any kind — the §9.1 gap cannot arise, because the letter is not pulled
through a `Δ`, it simply is not a function of the summation variable. The first elimination, the
step that has now failed twice at rank 2 (§13.4 and §17.1), can therefore be run on a **rank-1**
object: the Q-row class of computation.

**Verification of the reduction — RISC-free, MCP kernel, non-circular.** Rebuilding `certP.wl`'s
own `stuff[]` and `Ftau[]` verbatim (with `h3f, a3f, dA2f, dPsif` as certP defines them) and
comparing against `certQ.wl`'s object:

* `Simplify[stuff["ll"] − q_ll·A₂(k)] = 0` — **symbolically zero**, not just at sample points;
* `Ftau["ll"] − (G_ll q_ll)·A₂(k) = 0` at `(n,k,l) = (5,2,3), (6,1,4), (4,3,0), (7,0,2), (9,4,1)`;
* `Cases[G_ll q_ll, HarmonicNumber[__], ∞]` is empty — the object really is letter-free;
* `FreeQ[A₂(k), l]` is `True`.

> ⚠ **`certQ.wl`'s own in-script assertion is CIRCULAR and must be replaced.** It compares
> `GQ·A₂(k)` against a `Fllref` built from the *same* two expressions, so it can only ever return
> `0`. It caught nothing; the check that has actual content is the MCP one above, which rebuilds
> the object from `certP.wl`'s `stuff[]`. Fix the script before reusing it — this is precisely
> the failure mode §13.2 warns about (*"always give a derived object an assertion that aborts the
> run"* — an assertion that cannot fail is not an assertion).

**`work/lb5/certQ.wl`** implements the route (`wlcheck`-clean). Stages `Q1…Q5`, all checkpointed
(`Q_ll_*.m`):

All timings below are **log-header deltas**, not `stage`'s own `t=…` numbers, which are wrong
(§17.5):

| stage | what | measured |
|---|---|---|
| `Q1` | `Annihilator[G_ll q_ll, {S[n],S[k],S[l]}]` | **3 generators, ~1 s** — rank 1 confirmed |
| `Q2` | `CreativeTelescoping[ann, S[l]−1, {S[n],S[k]}]` | **RETURNED in ≈ 9 min**, 3 telescopers, ~2 GB (checkpoint `Q_ll_ct1.m` is 27.8 MB) |
| `Q3` | `OreGroebnerBasis[…, OreAlgebra[S[n],S[k]]]` | **≈ 3 min 20 s**, and **`gb === ct1`-telescopers → True** — so, exactly as for the Q-row, *no Gröbner cofactor chain is needed* |
| `Q4` | `DFiniteTimes[gb, Annihilator[A₂(k),{S[n],S[k]}]]` | annihilator of `A₂(k)H(n,k)`, rank 2 in **two** variables |
| `Q5` | `CreativeTelescoping[…, S[k]−1, {}, Support → …]` | `M_ll` |

> **This is the first time any τ has got past its first elimination in the whole campaign.**
> The comparison is direct and on the *same* τ: rank 2 in three variables, `Support`-boxed —
> **> 67 min, no return, twice**; rank 1 in three variables — **≈ 9 min, returned, 3 telescopers**.
> The lever is the rank, exactly as the τ-split's effect on `Annihilator` was (OOM → 2 s).

The same reduction applies **partially** to the other four τ: `Ψ = A₁(k)+3B₁(k)+(3/2)C₁+(1/2)A₁(l)`
and only `C₁` and `A₁(l)` depend on `l`, so for every τ the pieces
`G_τ p_τ`, `G_τ q_τ A₂(k)`, `G_τ r_τ (A₁(k)+3B₁(k))` all have their letters pull out of the
`l`-sum for free, and only `G_τ r_τ ((3/2)C₁+(1/2)A₁(l))` — a rank-2 remnant — does not.
**Boundary obligations are not discharged by `certQ.wl`**: each of `Q2` and `Q5` introduces its
own telescoped boundary term, to be checked by the §8 pole-order comparison against `T`'s double
zeros. They are listed in `certQ.log` rather than assumed away.

## 17.4 The exact remaining surface of the Phase-2 certification

Everything below the line is done and needs no rerun. This is the complete list of what is not.

**DONE — do not recompute.**

| object | status |
|---|---|
| Q-row single certificate `L_BZ·T = Δ_k(ρT)+Δ_l(σT)` | **[CERTIFIED]**, checked to `0` twice, once RISC-free |
| Theorem B ⇔ `Σ_{k,l} E(v) = 0` | **[PROVED]** |
| the regularised boundary lemma | **[VERIFIED exact, n₀ = 1…6]** (`m2bnd.wl`) |
| `Eletters.m` = `E(v)/T` in letter form | **[PROVED]**, four independent confirmations |
| the rank-3 relations `γ=3α, δ=(3/2)α, ε=(1/2)α`; `α = −Λ/2` | **[PROVED, checked to 0]** |
| the τ-split `E(v) = Σ_τ F_τ` | **[CERTIFIED — RISC-free, symbolic]** (`certPv0.wl`) |
| `p_ll = r_ll = 0`, so `F_ll = (G_ll q_ll)·A₂(k)` with `A₂` free of `l` | **[PROVED, symbolic]** (§17.3) |
| `D_n = Σ T ŵ₃ − P̂_n = 0` for `n = 0…300` | **[VERIFIED exact]** (`seqdata300.json`) — 301 values |
| assembly + verification + initial-value chain (`certPy` → `certPv` → `certT3f`) | written, `wlcheck`-clean, untested only because it has no input yet |
| `(T1-top)` has no degree-≤3 representative in three alphabets | **[PROVED negative]** (§16) |

**NOT DONE — the whole of it.**

1. **The five `M_τ`.** Nothing else stands between the current state and Theorem B. Of the five:
   * `n1, n2, n3` (weights 84 / 86 / 66) — **never attempted**; they are the smallest objects in
     the whole problem and should be tried first;
   * `ll` (weight 2255) — the rank-2 route has failed twice; the **rank-1 route of §17.3 is the
     one to run**;
   * `kk` (weight 12471) — `Annihilator` alone OOMs at 7.8 GB. This is the hard one, and the
     §17.2/§17.3 decomposition is the only proposal on the table for it.
     > ⚠ **OBSOLETE — see §18.14.** The decomposition was run and `kk` is no longer the hard one:
     > its piece `kk:C` (12489 leaves, *0* letters against `F_kk`'s 10) clears `Annihilator` in
     > **34 s at 0 GB**, and `ann + ct₁ + gb` in **69 s**. `Annihilator[F_kk]` is not an obstacle
     > any more. The obstacle moved to `ct₂` for *every* piece — §18.13.
2. **The boundary obligation for each new certificate.** Every `M_τ` produced by a two-step
   telescoping needs its own `k=0` / `l=0` vanishing check and pole-order comparison against
   `T`'s double zeros, exactly as §2 did for the Q-row. `certPv.wl` has the harness; **do not
   skip this** — it is the step that is easiest to assume and hardest to notice missing.
3. **`(T1-top)`** — blocked on a structural idea (§16), not on compute.
4. **The `p ∈ {2,3}` factor 12** — a separate remnant, untouched here (`PHASE2_THEOREM` §D.2).

**Honest cost statement.** The §13.4 figure of "4–10 kernel-hours" is **withdrawn**. What can be
said from measurement: four distinct attacks on the elimination step (unbounded `ct₁`,
`Support`-boxed `ct₁`, unbounded `ct₂`, monolithic `Annihilator`) have each run for 15–85 minutes
without returning, on objects spanning 2255 to 132917 leaves and ranks 1 to 3; and the two that
were allowed to run longest both ended in memory divergence. **The only lever that has ever
changed one of these steps from "no return" into "0 s" is lowering the rank** — the τ-split did it
for `Annihilator` (OOM → 2 s), and §17.3's letter-out reduction does it again for `F_ll`
(rank 2 → rank 1, `Annihilator` 3 generators in 0 s). A successor should therefore spend the
first hour on §17.3's decomposition rather than on more kernel time for the existing scripts.

## 17.5 A HARNESS BUG that invalidates the checkpoint story and disabled every memory cap

`certP.wl`, `certP2.wl` and `certQ.wl` all define

```wolfram
stage[file_, lab_, name_, body_] := Module[{r, t0},
  If[FileExistsQ[DIR <> file],
    r = Get[DIR <> file]; log["  ", lab, " ", name, " : loaded checkpoint"]; r,
    t0 = AbsoluteTime[]; r = MemoryConstrained[body, MEMCAP]; ...]]
```

**`stage` has no hold attribute.** Wolfram evaluates arguments before entering the function, so
`body` — the `Annihilator` or the `CreativeTelescoping` — is **already fully computed by the time
`stage` is called**. Three consequences, all of them things this project has been reasoning about
wrongly:

1. **`MemoryConstrained[body, MEMCAP]` is a no-op.** It wraps a finished value. It cannot abort,
   ever. *This is the entire explanation of "`MemoryConstrained` does not fire"* in §13.1 and
   §17.1 — the 14.4 GB monolithic OOM and both of this session's divergences were uncapped
   because the cap was applied to the answer rather than to the computation.
2. **Checkpoints do not prevent recomputation.** `"… : loaded checkpoint"` is printed *after* the
   expensive stage has been redone and its result discarded. Every restart advertised as cheap in
   §8.7 / §13.4 / `CERTS_RESUME` §8.4 in fact redid all prior stages. (It went unnoticed because
   the only stage anyone ever restarted was `Annihilator[F_ll]`, which costs 2 s.)
3. **The `t=…s` timings printed by `stage` are wrong.** `t0` is set *after* the body has run, so
   the number reported is `Put` time only. `certQ.wl`'s `ct1 #2 t=3s` is not a 3-second
   telescoping — it is a 27.8 MB `Put`; the elimination itself took **≈ 9 minutes** (log header
   `04:59:32` → next header `05:08:36`). Timings taken from `stage` elsewhere in this file and in
   `CERTS_RESUME` should be re-read as lower bounds of `Put` cost, not as stage costs.

**The fix is one line**, and it is applied to `certP.wl` and `certP2.wl`:

```wolfram
SetAttributes[stage, HoldRest];      (* place immediately before the definition *)
```

`HoldRest` holds `lab`, `name` and `body` while leaving `file` evaluated (it is a `StringJoin`
that must evaluate for `FileExistsQ`). `lab`/`name` are strings, so holding them is harmless —
they still print correctly inside `log`. Verified in the MCP kernel: with `HoldRest` the
checkpoint branch **skips the body entirely** and `MemoryConstrained` **aborts** as intended;
without it, neither happens. **`certQ.wl` still needs the same one line** — it was running when
the bug was found and editing a file that `math < file` is reading from stdin is not safe.

> **This also changes the interpretation of the "4–10 kernel-hours" estimate.** The elimination
> steps really do fail to return — that part is measured and stands — but the *restartability*
> that made the five-τ task list look like a bounded grind was never real. Fix `stage` first;
> only then is the checkpointed task list of §8.3 an accurate description of the work.

## 17.6 Kernel state at hand-off (2026-07-25 ~05:30) and the session's ledger

**Kernel-hours consumed this session: ≈ 1.7** (two inherited kernels reaped/abandoned, two new).
Well inside the 5-hour cap — **the binding constraint was never the budget, it was the licence
seat cap of 3 combined with two unreapable runaway kernels** (`kill -KILL` is blocked, §17.1).
`1112624` finally exited at **05:20 after 79 min** on the superseded rank-2 `ll` `ct₁`, freeing
10.8 GB and a seat; `n1, n2, n3` were launched immediately on it. With a working `MEMCAP` (§17.5)
that kernel would have self-aborted at 3.5 GB around 04:10 and the small-weight τ would have had
an extra 70 minutes.

| pid | job | state |
|---|---|---|
| `1038875` | `certP.wl TAUS=kk ORD=kl` | **OOM-killed 04:58**, 85 min inside `Annihilator[F_kk]`. Nothing recovered. |
| `1112624` | `certP2.wl TAUS=ll,n1,n2,n3 ORD=lk CT1A=3 CT1B=3` | **died 05:20 after 79 min** inside the boxed rank-2 `ct₁` for `ll`, having peaked at 10.6 GB. Nothing recovered; it never reached `n1,n2,n3`. Superseded anyway — that τ is now being done at rank 1 by `certQ.wl`. |
| `1205156` | `certQ.wl` (rank-1 `τ = ll`) | **healthy, ~2.9 GB**, `Q1–Q3` complete and checkpointed (`Q_ll_ann1.m`, `Q_ll_ct1.m` 27.8 MB, `Q_ll_gb.m` 4.8 MB), inside `Q4 DFiniteTimes` at hand-off. |
| `1246566` | `certP.wl TAUS=n1,n2,n3 ORD=lk MEMCAP=3e9` — **with the §17.5 `HoldRest` fix** | launched 05:20:44 the moment `1112624` released its seat. On `τ = n1`, **`LeafCount` 578** — the smallest object anywhere in this problem (`F_ll` is 2318, `F_kk` 13069). These three τ had never been attempted before; they are the most likely to land. This is the **first** run in the campaign with a functioning memory cap, so it will report `MEMORY ABORT` rather than starving the box. |
| — | `degfit.py base ABRY CDV NZ` (union alphabet, 2666 cols, fit-only) | design matrix still building at hand-off, badly swap-starved by `1112624`. Not needed for the §16 verdict — `AB`, `ABR` and `ABY/CV/NZ` are all decisive on their own — but it is the widest alphabet and worth finishing on an idle box. |

**Everything `certQ.wl` has produced is on disk**, so with the §17.5 `HoldRest` fix applied a
restart genuinely resumes at `Q4` instead of redoing `Q2`'s nine minutes.

---

# §18. P1e session 5 — the letter-split, and the discovery that **letter count, not leaf count, is the cost**

## 18.1 The four-piece letter split — `[PROVED, symbolic, RISC-free, all five τ]`

§17.3 proved the special case `τ = ll`. The general statement is now proved for **every** τ.
Split `Ψ` into its `l`-free and `l`-dependent halves:

```
    Psi  =  Psik  +  Psil ,
    Psik = A1(k) + 3 B1(k)            <-- FREE of l
    Psil = (3/2) C1 + (1/2) A1(l)     <-- depends on l
```

Then, with `certP.wl`'s own rational data `P_τ = h3+2a3−½ dA2 dPsi`, `Q_τ = −½ dPsi`,
`R_τ = −½ dA2`, every shift term splits into **four** pieces whose sum is `F_τ` exactly:

| piece | summand | `l`-free letter `λ` pulled out | rank of the `l`-elimination |
|---|---|---|---|
| **A** | `W_τ P_τ` | `1` | **1** (letter-free) |
| **B** | `W_τ Q_τ · A₂(k)` | `A₂(k)` | **1** |
| **C** | `W_τ R_τ · Ψ_k` | `Ψ_k` | **1** |
| **D** | `W_τ R_τ · Ψ_l` | `1` | 2 (remnant) |

**Verified in the MCP kernel, RISC-free and non-circularly** — the pieces are compared against
`certP.wl`'s own `stuff[]` and `Ftau[]`, rebuilt verbatim, not against any assertion of ours
(§16's circularity note):

* `Simplify[Ψ − (Ψ_k + Ψ_l)] = 0`;
* `FreeQ[A₂(k), l]` and `FreeQ[Ψ_k, l]` are both `True`;
* `Simplify[stuff[τ] − (P_τ + Q_τ A₂ + R_τ(Ψ_k+Ψ_l))] = 0` **symbolically, for all five τ**;
* `Simplify[F_τ − (W P + W Q A₂ + W R Ψ_k + W R Ψ_l)] = 0` **symbolically, for all five τ**;
* the three cofactors `W_τ P_τ`, `W_τ Q_τ`, `W_τ R_τ` contain **zero** `HarmonicNumber`s;
* `R_τ` is `l`-free for **every** τ (not just `ll`), which is what lets `Ψ_k` come out;
* `Δ_l Ψ_l` and `Δ_k A₂(k)` are both **rational** — so the remnant is genuinely rank 2, and
  each pulled-out letter is rank 2 in its own variable.

Consequently, with **no Abel correction anywhere** (no letter is pulled through a `Δ`; the
letters simply are not functions of `l`):

```
    Sum_l F_tau  =  Sum_l (W P)  +  A2(k) Sum_l (W Q)  +  Psik(n,k) Sum_l (W R)
                                 +  Sum_l (W R Psil)
```

## 18.2 The real cost driver — **the number of harmonic letters**, `[MEASURED]`

This is the session's main structural finding and it corrects the working assumption of §§13–17,
which ranked the objects by `LeafCount`.

| τ | `LeafCount(F_τ)` | **letters in `F_τ`** | `Annihilator[F_τ]` measured |
|---|---|---|---|
| `n1` | **578** | 10 | **> 9 min, no return** (this session, pid 1246566) |
| `ll` | 2318 | **2** | **≈ 2 s** (§17.4) |
| `kk` | 13069 | 10 | **OOM at 7.8 GB / 85 min** (§17.1) |

`F_n1` is the **smallest object in the entire problem by leaf count — a factor of four smaller
than `F_ll`** — and its `Annihilator` is nevertheless orders of magnitude harder. The ordering by
leaf count is not merely imprecise, it is **inverted**. What separates the two is that `F_ll`
carries 2 harmonic letters and `F_n1` carries 10. RISC's closure has to build the tensor product
of the letter module with the hypergeometric part, and that is exponential in the number of
letters and only polynomial in the size of the rational cofactor.

**This retro-explains every failure in the campaign.** `F_ll` (2 letters) is the only τ that ever
got past `Annihilator` cheaply, and it is the only τ that ever got past its first elimination
(§17.3). The four τ that failed — `n1`, `n2`, `n3`, `kk` — are exactly the four with 10 letters.

**Letters per piece under the §18.1 split (MCP-measured):**

| τ | `F_τ` | A | B | C | D |
|---|---|---|---|---|---|
| `n1`,`n2`,`n3`,`kk` | **10** | **0** | 2 | 4 | 4 |
| `ll` | 2 | 0 | 2 | 0 | 0 |

So the split takes every object from 10 letters down to **at most 4**, and piece **A is purely
hypergeometric** (0 letters, rank 1) — the class for which `Annihilator` is a shift-ratio
computation and is essentially free regardless of size. `ll`'s pieces A, C, D are identically
zero, which is §17.3's `p_ll = r_ll = 0` restated.

## 18.3 The rational cofactors — the 13 rank-1 problems, confirmed

`LeafCount` of `W_τ X_τ / T`, re-measured this session (reproduces §17.2 exactly):

| τ | A = `W P/T` | B = `W Q/T` | C, D = `W R/T` |
|---|---|---|---|
| `n1` | 429 | 215 | 121 |
| `n2` | 4262 | 935 | 151 |
| `n3` | 15027 | 2810 | 190 |
| `kk` | 10905 | 10758 | 10611 |
| `ll` | **0** | 1913 | **0** |

**13 non-zero rank-1 problems** (A, B, C for `n1,n2,n3,kk`, plus B for `ll`) and **4 rank-2
remnants** (D for `n1,n2,n3,kk`; `ll` has none). Note `kk`'s cofactors are all ≈ 10 600–10 900
leaves **because of `rho` alone**: `Together[rho]` has a 10 477-leaf numerator over a 71-leaf
denominator, so `rho` does **not** compress and `kk` is intrinsically the expensive τ.

## 18.4 `certQ2.wl` — the generalised script

`work/lb5/certQ2.wl` (`wlcheck`-clean) runs the §18.1 route for any `τ:piece` job list:

```
  R1  ann  = Annihilator[obj, {S[n],S[k],S[l]}]              obj is LETTER-FREE for A,B,C
  R2  ct1  = CreativeTelescoping[ann, S[l]-1, {S[n],S[k]}]   the rank-1 l-elimination
  R3  gb   = OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n],S[k]]]
  R4  annL = DFiniteTimes[gb, Annihilator[lambda,{S[n],S[k]}]]   re-attach the l-free letter
  R5  ct2  = CreativeTelescoping[annL, S[k]-1, {}, Support -> ladder]   -> M_piece
```

It carries the §17.5 `SetAttributes[stage, HoldRest]` fix from birth, checkpoints every stage
(`R_<τ>_<piece>_*.m`), and its assertions are **non-circular**: `chkTau` rebuilds `certP.wl`'s
`stuff[]`/`Ftau[]` and aborts the run unless the symbolic difference is `0` and the cofactors are
letter-free. `JOBS="τ:piece,…"`, `DMAX`, `MEMCAP` from the environment.

## 18.5 The assembly gap, and how to close it — the **φ-shift decomposition**

`certPy.wl` assembles `P_<τ>.m = {ann, ct1, gb, ct2}`: a *two*-step telescoping with no
intermediate product. `certQ2.wl` (and `certQ.wl`) produce `{ann, ct1, gb, annL, ct2}` — there is
a **`DFiniteTimes` stage in the middle**, and `DFiniteTimes` returns generators of `Ann[λS]`
without returning the representation that proves they annihilate. So `certPy`/`certPv` do **not**
apply verbatim to the §18.1 route. This is the one genuinely new gap the letter-split opens, and
it is *not* a boundary-term issue — the boundary obligations are unchanged.

It closes cleanly, because of a fact just verified RISC-free in the MCP kernel:

> **φ-shift lemma `[VERIFIED, symbolic]`.** For `λ ∈ {A₂(k), Ψ_k}` and every shift `0 ≤ a,b ≤ 2`,
> ```
>       S_n^a S_k^b λ  =  λ + φ_λ(a,b;n,k) ,     φ_λ  RATIONAL
> ```
> `FreeQ[φ, HarmonicNumber]` is `True` in all 18 cases; `LeafCount(φ) ≤ 441`. E.g.
> `φ_{Ψk}(0,1) = (3 + 3k + 6n + 2kn + 4n²)/((1+k)(k−n)(1+k+n))`.
> This holds because both letters are *differences of harmonic numbers at shifted arguments*, so
> a shift telescopes to a finite explicit rational sum. It is **not** true of `Ψ_l` — which is
> exactly why `D` is the remnant.

With it, for any Ore operator `O = Σ c_{ab} S_n^a S_k^b` and any `l`-free `λ`,

```
       O . (λ S)  =  λ · (O . S)  +  (O_φ . S) ,        O_φ := Σ c_{ab} φ_λ(a,b) S_n^a S_k^b
```

— an identity between **explicit rational-coefficient operators**, with no closure computation.
Therefore each `DFiniteTimes` generator is verifiable RISC-free by two `OreReduce`s against `gb`:

```
       annL_j . (λ S) = 0     <==>     OreReduce[annL_j, gb] = 0   AND   OreReduce[(annL_j)_φ, gb] = 0
```

and the same identity pushes the `(n,k)`-level certificate back down to `(n,k,l)`, since `λ` is
`l`-free and `gb_i . g = Δ_l(C_i . g)` is what `ct1` returned. The `φ`-correction plays the role
an Abel correction would play, but it is **exact, rational and finite** rather than a boundary
term. `verifycore.wl`'s hh-symbol machinery already treats harmonic numbers as indeterminates,
which is precisely the representation this needs.

> **Status:** `[SPECIFIED, NOT IMPLEMENTED]`. Writing `certQy.wl` / `certQv.wl` on this pattern is
> a bounded scripting job (the mathematics above is complete and checked), but it was **not**
> written this session because at the time no `R_*.m` existed to test it against, and untested
> assembly code is exactly what §13.2 warns about. **It is now the last mile of Theorem B.**

## 18.6 M4 — the honest cost of the `(T1-top)` big grind **under the letter-split**

> ⚠ **The kernel-hour arithmetic in this section was calibrated before the split was measured;
> §18.10 restates it. The conclusion is unchanged, the reason is sharper. Read both.**

The question this session was asked to answer: now that the τ-split **×** letter-split is
understood, how many rank-1 problems does `(T1-top)`'s 220-monomial `E(w₅^I)` become, and how big?

**The answer is that the letter-split does not rescue `(T1-top)`, and the reason is sharp.**

The §18.1 lever is *"a letter monomial that does not depend on `l` pulls out of the `l`-sum, and
the elimination drops to rank 1."* So the lever's reach is exactly the **`l`-free fraction of the
support**. New script `work/lb5/`-adjacent (`lsplit.py`, in the session scratch; it reuses
`esupp.py`'s label parser, and letters in slots `k`/`n` are `l`-free while slots `l`/`c` —
arguments `l, n+l` and `k+l, n+k+l` — are not):

| | `ŵ₃` (`v`, Theorem B) | `w5_allp` | **`w₅^I` (the v4 target)** |
|---|---|---|---|
| support of `E(·)/T` | 6 | 208 | **220** |
| **`l`-free monomials → rank 1** | **4 (67 %)** | 24 (12 %) | **33 (15 %)** |
| `l`-dependent monomials | 2 | 184 | **187** |
| distinct `l`-dependent parts = remnant classes | 2 | 71 | **71** |
| **worst remnant `l`-rank** | **2** | 16 | **16** |

(the remnant `l`-rank of a class is `2^j` for `j` `l`-dependent letter factors, because
`Δ_l(letter)` is rational for each of them — the same fact that makes `D` rank 2 in §18.1.)

Multiplying by the five τ:

> **`(T1-top)` under the τ-split × letter-split = 165 rank-1 problems + 355 remnant problems,
> the remnants at `l`-rank 4, 8 and 16** (25, 24 and 12 classes per τ respectively; only 10
> classes per τ are at `l`-rank 2).
> Against Theorem B's **13 rank-1 problems + 4 remnants, all remnants at `l`-rank 2**.

**Costing it against the one calibration point we have.** The only rank-1 problem in this campaign
to get past its first elimination is `ll:B` (`certQ.wl`): cofactor 1913 leaves, 2 letters, and its
stages measured `ann` ≈ 1 s, `ct₁` ≈ **9 min**, `gb` ≈ 3 min 20 s, `DFiniteTimes` **> 22 min and
still running at the time of writing**, `ct₂` not reached. So **one** rank-1 problem is `≳ 35`
kernel-minutes at 1913 leaves. `(T1-top)`'s cofactors cannot be smaller — they carry the *same*
`G_τ` factor (`rho` alone is an incompressible 10 477-leaf numerator, §18.3) multiplied by the
`dL` rationals of a degree-up-to-5 monomial.

> **Therefore: `(T1-top)`'s rank-1 half alone is `165 × ≳35 min ≳ 96 kernel-hours`, and that is a
> lower bound with optimistic cofactors.** The remaining 355 problems are at `l`-rank 4–16, and
> **no elimination of rank ≥ 2 has ever returned in this campaign** — four distinct attacks at
> rank 2–3 ran 15–85 minutes without returning (§17.4), two of them ending in memory divergence.
> Rank 16 is not a longer version of that; it is a different regime.

**Verdict for the next session's grind-vs-new-idea decision: do not grind.** The letter-split is
worth ~7× on the rank-1 fraction for `ŵ₃` (67 % of a support of 6) and ~1.15× for `w₅^I` (15 % of
a support of 220) — it is a lever sized to Theorem B and not to `(T1-top)`. This is a *second*,
independent structural reason to stop working `(T1-top)` by compute, and it agrees with §16's:
§16 said the degree-≤3 fit is inconsistent, so no cheap representative exists; §18.6 now says that
even with the best decomposition we know, the expensive representative costs ≳ 100 kernel-hours in
its *easy* half. The `(T1-top)` verdict `[BLOCKED BY A STRUCTURAL OBSTRUCTION]` stands, and §16.5's
do-not-rerun list should be extended with **"do not attempt the letter-split grind for `w₅^I`"**.

The one thing that *would* change this is unchanged from §15.2/§14.4: a weight-5 representative
whose **`l`-free fraction** is high — note that is a different and weaker demand than §15.2's
"low degree", and it is the sharper target. `w5_Rbase` (support 100, degree ≤ 4) is the only
representative that has ever moved the support number and is the natural first thing to measure
against this new criterion.

**Measured against every available representative** — the `l`-free criterion, which is the one
that matters for the letter-split, does **not** vary much:

| representative | support | `l`-free (rank 1) | remnant classes | worst `l`-rank | problems (×5 τ) |
|---|---|---|---|---|---|
| `ŵ₃` (`v`) | **6** | **4 (67 %)** | 2 | **2** | 20 rank-1 + 10 remnant *(grouped in practice to 13 + 4)* |
| `w5_Rbase` | 100 | 17 (17 %) | 42 | 8 | 85 + 210 |
| `w5_I` | 184 | 23 (12 %) | 71 | 16 | 115 + 355 |
| `w5_allp` | 208 | 24 (12 %) | 71 | 16 | 120 + 355 |
| **`w₅^I`** (v4 target) | **220** | **33 (15 %)** | **71** | **16** | **165 + 355** |

So `w5_Rbase` — the best representative known, and the only one under degree 5 — is still
**85 rank-1 problems (≳ 50 kernel-hours by the `ll:B` calibration) plus 210 remnants up to
`l`-rank 8**, and it is not `p`-integral for the v4 target anyway. **No available representative
puts `(T1-top)` within an order of magnitude of Theorem B.** The `l`-free fraction sits at 12–17 %
for every weight-5 candidate and at 67 % for `ŵ₃`; that gap, not the raw support count, is the
cleanest single statement of why Theorem B is finishable and `(T1-top)` is not.

**The φ-tables are built and independently checked** (`work/lb5/phi_tables.m`, MCP kernel,
RISC-free, 3 s): `φ_{A₂}(a,b)` and `φ_{Ψk}(a,b)` for `0 ≤ a,b ≤ 5`, every entry rational
(`FreeQ[…, HarmonicNumber]` is `True`), max `LeafCount` 3030. The check that has content is the
**cocycle identity**

```
      phi(a+a', b+b')  ==  phi(a,b) + ( phi(a',b') shifted by n->n+a, k->k+b )
```

which must hold if `S_n^aS_k^b λ = λ + φ(a,b)` is to be consistent with composition of shifts.
It is **exactly `0` in all 81 cases for each of the two letters** — an assertion that could have
failed and did not. `verifycore.wl` already carries the hand-rolled Ore algebra
(`ope/opPlus/opTimes/opShift/toOpe/applyOp`) and the hh-symbol zero test that `certQy`/`certQv`
would use, so the last mile needs no new primitives, only the composition logic of §18.5.

## 18.7 §18.2 validated on the machine, immediately — `[MEASURED]`

The orchestrator reaped the `certP.wl TAUS=n1,n2,n3` kernel (pid 1246566) once §18.2 showed the
leaf-count ranking was inverted, and `certQ2.wl` took the seat at 05:39:41. The very first job is
the cleanest possible test of §18.2, because it is the **same τ** on the **same machine**, differing
only in letter content:

| object | `LeafCount` | letters | `Annihilator` |
|---|---|---|---|
| `F_n1` (whole shift term, `certP.wl`) | 578 | **10** | **19 min, no return** (reaped) |
| `n1:A` = `W_n1 P_n1` (`certQ2.wl`) | 400 | **0** | **3 generators, 0 s** |

The two objects are the same size to within 30 %. The letter count is the entire difference, and
it is the difference between "no return in 19 minutes" and "instant". §18.2 is therefore not an
inference from the `ll`/`kk` contrast alone — it is a controlled measurement.

`certQ2.wl`'s non-circular assertion block also passed on its first live run, exactly as it did in
the MCP kernel: `letters-in-cofactors=0`, `symbolic=0`, `points={0,0,0,0,0}`.

> **Cost the letter-split adds, stated honestly.** Each τ now yields **four** certificates instead
> of one, so there are four `l`-boundary and four `k`-boundary obligations per τ where there was
> one. The obligations *sum* correctly (`Σ_pieces boundary = boundary of F_τ`, since the pieces sum
> to `F_τ`), so the mathematical content is unchanged — but the §17.4 item 2 checklist grows from
> 5 boundary pairs to 19, and none of them are discharged yet. This is bookkeeping, not new
> mathematics, and `certPv.wl` already has the harness for it.

## 18.8 Where the route actually spends its time — the two remaining walls

`certQ2.wl`'s first live job re-partitions the cost completely. The `l`-elimination, which was
*the* wall for three sessions, is now **free**; two later stages are what remain.

**Stage costs for `n1:A` (cofactor 429 leaves, 0 letters), measured:**

| stage | cost |
|---|---|
| `R1` `Annihilator` | 3 generators, **0 s** |
| `R2` `ct₁` (eliminate `l`) | 2 telescopers, **5 s** |
| `R3` `OreGroebnerBasis` | **1 s**, and `gb === ct1`-telescopers → `True` |
| `R4` `DFiniteTimes` | not needed (`λ = 1` for pieces A and D) |
| `R5` `ct₂` `Support` ladder | `d=0…4`: **1, 6, 15, 49, 185 s** — a factor of ≈ **3.8 per rung** |

> **Wall 1 — the `ct₂` `Support` ladder is exponential in the rung.** At 3.8×/rung, `d=5` ≈ 12 min,
> `d=6` ≈ 45 min, `d=7` ≈ 2.9 h. The ladder cannot reach `d ≥ 7` on this hardware, so any piece
> whose minimal telescoper has order ≥ 7 is out of reach *by this method*. Note also that
> `certQ2.wl` does **not** checkpoint `ct₂`, so a long ladder is pure loss on restart, and it
> starves every later job in `JOBS`.

> **Wall 2 — `DFiniteTimes` for the pieces that need it (B and C).** `certQ.wl`'s `Q4`
> (`DFiniteTimes[gb, Annihilator[A₂(k)]]` for `τ = ll`) has now run **> 35 min without returning**
> at a steady ≈ 3.3 GB. Its `gb` is 4.8 MB. This is the *same* object `certQ2.wl` would build for
> `ll:B`, so `ll:B` is blocked behind the same wall, and pieces B and C of every τ go through it.

**`work/lb5/certQ3.wl`** (`wlcheck`-clean, not yet run) is `certQ2.wl` hardened against both:

* `LADDERCAP` (default 2700 s) — abandons a job's ladder and moves to the next job, so one bad
  piece cannot starve the list;
* a **free `ct₂` attempt first** (`CreativeTelescoping[annL, S[k]−1, {S[n]}]`, `TimeConstrained` by
  `FREECAP`, default 600 s) — unconstrained telescoping returns the *minimal* operator directly
  and does not pay the ladder's 3.8×, which on objects this small may simply win;
* a completed job (`R_<τ>_<piece>.m` present) is **skipped**, not recomputed.

### The idea that would remove Wall 2 entirely

`DFiniteTimes` is only needed because `A₂(k)` is treated as a *letter*. But

```
        A2(k)  =  H^(2)_{n+k} - H^(2)_k  =  Sum_{j=1}^{n} 1/(k+j)^2
```

is a **sum of a rational function**. So

```
        Sum_k A2(k) S(n,k)  =  Sum_{j=1}^{n} Sum_k  S(n,k)/(k+j)^2 ,
```

and the inner object carries **no letter at all** — it is `S` times a rational function, of the
same rank as `S`, in the variables `(n,k,j)`. The letter is traded for one extra summation
variable, and `DFiniteTimes` disappears from the pipeline. The cost is that the `j`-range is
`1…n`, so the `n`-telescoping acquires a boundary term at `j = n` — a genuine obligation, but of
exactly the kind §8 already discharges for the Q-row. `Ψ_k = A₁(k) + 3B₁(k)` admits the same
treatment for its `A₁(k)` half; `B₁(k) = H_{n−k} − H_k` is the awkward one.
**This is the single most promising unexplored move and it is cheap to try.**

## 18.9 Measured per-stage costs of the letter-split route

Two kernels, `certQ2.wl` (`JOBS=n1:A,n1:C,n1:B,n1:D,kk:C,kk:B,kk:A,kk:D`) and `certQ3.wl`
(`JOBS=n2:*,n3:*` — disjoint lists, so the two kernels can never write the same checkpoint).
Both passed the non-circular assertion block on their first live run
(`letters-in-cofactors=0`, `symbolic=0`, `points={0,0,0,0,0}`).

| job | cofactor `/T` | letters | `R1` ann | `R2` ct₁ (elim `l`) | `R3` gb | ct₁ checkpoint |
|---|---|---|---|---|---|---|
| `n1:A` | 429 | 0 | **0 s**, 3 gens | **5 s**, 2 telescopers | **1 s** | 143 KB |
| `n2:A` | 4262 | 0 | **6 s**, 3 gens | **22 s**, 2 telescopers | **5 s** | 718 KB |
| *(`ll:B`, `certQ.wl`, for comparison)* | 1913 | 0 | 1 s | **≈ 9 min**, 3 telescopers | 3 min 20 s | **27.8 MB** |

`gb === ct1`-telescopers is `True` in every case, so **no Gröbner cofactor chain is ever needed** —
the same collapse the Q-row enjoyed, now confirmed on three independent objects.

> **The first three stages of the whole route cost seconds.** `n2:A` — a 4262-leaf cofactor,
> larger than `ll:B`'s 1913 — clears `ann + ct₁ + gb` in **33 s total**, against `ll:B`'s ≈ 12 min,
> and its `ct₁` checkpoint is **38× smaller**. So the `l`-elimination's cost is not driven by
> cofactor size either; on this evidence it tracks the number of `ct₁` telescopers returned
> (2 versus 3), i.e. the rank of the surviving `(n,k)`-module.

**What this leaves.** With `R1–R3` free and `R4` avoidable for pieces A and D (`λ = 1`), the entire
remaining cost of Theorem B sits in **two** places, both identified in §18.8: the `ct₂` `Support`
ladder (Wall 1, exponential at ≈ 3.8×/rung) and `DFiniteTimes` for pieces B and C (Wall 2). That
is a much smaller and better-localised remaining surface than any previous session had.

### Coverage note — `τ = ll` is currently unserved

The two live job lists are `certQ2: n1:* + kk:*` and `certQ3: n2:* + n3:*`. **Neither covers
`ll`.** That is deliberate but must not be forgotten: `ll` has only *one* non-zero piece
(`ll:B`, since `p_ll = r_ll = 0` makes A, C and D identically zero), and `ll:B` is precisely
Wall 2 — its `R4` is the very `DFiniteTimes` that `certQ.wl`'s `Q4` failed to return from in
37 min before being reaped. Re-running it in `certQ2/3` form would hit the identical wall on the
identical object, so a seat spent on it now would be wasted.

> **`ll` is therefore blocked on Wall 2 alone**, and the §18.8 `j`-variable idea
> (`A₂(k) = Σ_{j=1}^{n} 1/(k+j)²`, trading the letter for a summation variable and deleting
> `DFiniteTimes` from the pipeline) is the specific thing to try for it. Note the pleasing
> irony: `ll` was the *easiest* τ under the old ranking and is now the *only* one whose single
> piece needs the stage the others can skip.

## 18.10 Recalibration of §18.6 — **read this together with §18.6, it supersedes its arithmetic**

§18.6's figure of "≳ 96 kernel-hours" was calibrated on `ll:B` under the **old** pipeline
(≈ 35 min for one rank-1 problem). The §18.9 measurements supersede that calibration and it
should be restated, because the cost has moved to a different stage:

* `R1–R3` of a rank-1 problem now cost **6–33 s**, not 35 min. The old figure over-charged this.
* But **`ct₂` is charged in full and is the same for every problem**: `n1:A`'s ladder has consumed
  **> 15 min without returning** on the *smallest* piece in the entire problem (429-leaf cofactor,
  0 letters), having ruled out orders 0–4.

So the corrected estimate keeps the same conclusion for a better reason:

> **`(T1-top)`'s 165 rank-1 problems cost `165 × (ct₂)`, and `ct₂` is ≥ 15 min even on the easiest
> object we have** — i.e. **≳ 41 kernel-hours as an absolute floor**, with no upper bound
> established because no `ct₂` has yet returned at all. The 355 remnants at `l`-rank 4–16 are
> additional and are of a class that has never terminated here.

The substance of §18.6 is unchanged — **do not grind `(T1-top)`** — but the *reason* is sharper:
it is not that each problem is individually huge, it is that the letter split moves all of the
cost into `ct₂`, and `ct₂` is charged **per problem** while the split *multiplies* the number of
problems. The split is a large win for Theorem B (5 τ → 19 pieces, each `R1–R3`-free) and a
**net loss** for `(T1-top)` (5 τ → 520 pieces), because the `l`-free fraction that makes pieces
cheap is 67 % there and 12–17 % here. That asymmetry is the whole finding.

## 18.11 `phicore.wl` — the assembly primitive, written and self-tested

`work/lb5/phicore.wl` (`wlcheck`-clean, loads **no** RISC package) implements the §18.5
decomposition: `phiOf[λ,a,b]` (memoised, returns `$Failed` loudly if `φ` is not rational),
`opPhi[O, λ]` on `verifycore.wl`'s hand-rolled `ope[vars, terms]` operators, and
`phiCocycleTest[λ]`. Run in the MCP kernel:

* `phiCocycleTest[A₂(k)]` and `phiCocycleTest[Ψ_k]` are both **`{0}`** (81 cases each);
* the operator identity `O.(λS) = λ(O.S) + (O_φ.S)`, expanded on the basis `SS[a,b] := S(n+a,k+b)`
  for a deliberately awkward test operator (coefficients `(n+1)/(k+2)`, `−3n`, `1/(n−k)`, `k²`
  at shifts `(0,0),(1,0),(1,1),(0,2)`), evaluates to **exactly `0`**;
* `opPhi` correctly drops the `(0,0)` term, since `φ(0,0) = 0`.

> **What this buys, stated precisely.** The identity is a *tautology* once the φ-lemma holds —
> expand both sides on `S(n+a,k+b)`. So **all** the content sits in the φ-table, and the table is
> checked independently by the cocycle identity. This is the one place in the whole campaign where
> the certification is free: verifying a `DFiniteTimes` generator `annL_j` reduces to two ordinary
> Ore reductions against `gb = Ann[S]`,
> `OreReduce[annL_j, gb] == 0` **and** `OreReduce[opPhi[annL_j, λ], gb] == 0`,
> both of which return explicit cofactors and are therefore RISC-free checkable.
> The §18.5 gap is now `[SPECIFIED + PRIMITIVE IMPLEMENTED AND TESTED]`; what remains of it is
> the bookkeeping of `certQy.wl`/`certQv.wl`, not any mathematics.

## 18.12 The split trades elimination cost for **telescoper order** — the tension named

Full ladder for `n1:A`, the **smallest object anywhere in this problem** (429-leaf cofactor, zero
letters, `ann`+`ct₁`+`gb` in 6 s total):

| `d` | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| cost | 1 s | 6 s | 15 s | 49 s | 185 s | **828 s** |
| result | none | none | none | none | none | **none** |

So `ord(M_{n1:A}) ≥ 6`, and the rung cost grows by ×3–4.5, putting `d=6` at ≈ 62 min and `d=7` at
≈ 4.6 h. **The easiest object in the problem does not have an easy telescoper.**

> **This is the structural tension the letter split creates, and it should be stated plainly
> rather than discovered again.** Splitting a sum into pieces makes each piece's *closure and
> elimination* cheap — that is measured and large (§18.9: 12 min → 33 s) — but it makes each
> piece's *telescoper* no easier and generally **harder** than the total's, because the total
> here is `Σ_{k,l}E(v) = 0`, annihilated by everything, while the individual pieces are genuinely
> non-trivial sequences. Splitting into `N` pieces therefore costs `N` telescoper searches at
> orders that do not shrink, and the final `LCLM` has order up to the sum of theirs.
>
> Every route tried in this campaign has now hit `ct₂`: `certU`'s letter-split (79 min, no
> return), `certP`'s τ-split (never reached it), and now the τ×letter split (`d ≤ 5` excluded on
> the smallest piece). The **only** `ct₂` that has ever returned is the Q-row's, on `T` itself.
> **`ct₂` — not the closure, not the first elimination — is the true wall of the whole project**,
> and §§13–17's successive re-diagnoses (rank, then coefficient size, then letter count) were all
> diagnosing the *earlier* stages, which are now demonstrably free.

**What this implies for the next session.** More splitting will not help; it multiplies `ct₂`
searches. The productive directions are the two that attack `ct₂` itself:
* **fewer, not more, pieces** — group the pieces back together wherever they share a cofactor
  (C and D already share `W_τ R_τ`), so that one `ct₂` serves several;
* **do not search for the order at all** — the `Support` ladder pays for every wrong guess.
  Guess-and-certify is legitimate here: the *minimal* recurrence of each piece can be found
  cheaply by rational-arithmetic fitting in Python (`w5rec.py`'s machinery, `O(N³)` at a prime),
  and the resulting order/degree then goes straight into a **single** `Support` box, skipping
  `d = 0…ord−1` entirely. On the ladder above that would have turned 1084 s of failed rungs into
  one call. This is the cheapest available move and it needs no Wolfram seat to decide.

## 18.13 **The evidence that splitting cannot work has been on file since §5.1** — and it predicts every `ct₂` failure since

`work/lb5/guessrec.py` was re-run this session (`guessrec_220.log`, `guessrec_460.log`) and
reproduces §5.1 exactly:

| sequence | minimal `(r, d)` | nullity |
|---|---|---|
| `Q_n = Σ_{k,l} T` | **(3, 9)** | 1 |
| `Σ_{k,l} T·ŵ₃` | **(3, 9)** | 1 |
| `U₁ … U₅` — the five single-letter component sums | **none**, `r ≤ 12`, `d ≤ 30` | — |

§5.1 already drew the right headline — *"the combination is small, every piece of it is huge"* —
but it drew it about the **ε-route**, and then §§9–18 went on to build three successively finer
splits of exactly the objects it had just measured as huge. **The implication was never
transferred, and it is the explanation of the whole `ct₂` wall:**

> A telescoper for a piece is an operator annihilating that piece's double sum. §5.1 measures
> those sums directly and finds **no operator of order ≤ 12 with degree ≤ 30** for any of them,
> while the full combination has order **3**. So `ct₂` is not failing for want of a better
> `Support` box, a better ansatz, or more RAM — **it is searching for operators that are not
> there in the size range being searched.** Every split we can build produces pieces of exactly
> the species §5.1 measured.

The three independent confirmations now on the record, all predicted by this:

* `certU` (pure letter split — its pieces *are* `U₁…U₅`): `ct₂` **79 min, no return** (§17.2);
* `n1:A` (τ × letter split, the **smallest object in the problem**): ladder excludes orders
  `0…5`, costing 1084 s, with `d=6` ≈ 62 min and `d=7` ≈ 4.6 h (§18.12);
* `n2:A`: **unconstrained** `CreativeTelescoping` — no `Support` box at all, so no ansatz
  artefact — `TimeConstrained` at **600 s, no return** (this session). This is the measurement
  that rules out "the ladder was the problem".

> ### The strategic consequence: **stop splitting.**
> Every session since §13 has responded to a failure by splitting more finely, and each split
> *did* deliver exactly what it promised on the stage it targeted — the τ-split took
> `Annihilator` from a 14.4 GB OOM to 2 s, the letter-split took the first elimination from
> ≈ 12 min to 33 s and `Annihilator` to 0 s. Those wins are real and measured. But they move
> cost **into `ct₂`**, and they simultaneously **multiply the number of `ct₂` searches** while
> making each one *harder*, because the order-3 collapse is a property of the **combination**
> and is destroyed by any decomposition. The τ×letter split is the end of that road, not a
> waypoint on it: `R1–R3` are now free, so there is nothing left to split *for*.

**What to do instead — the two routes that do not decompose the combination.**

1. **Telescope the combination, with the letters carried.** This is what OOM'd at 14.4 GB
   (§13.1) — but that was measured *before* §18.2 identified the letter count as the driver, and
   before `HoldRest` made `MEMCAP` real (§17.5). The monolithic object has 10 letters; the
   question never asked is whether the *combination* can be re-expressed with **fewer letters**
   (not fewer terms) — `ŵ₃`'s folded form `v` already did this once, taking degree 5 to degree 2
   (§15.2). A folded form with ≤ 4 letters would put the whole of Theorem B in the class where
   `Annihilator` is instant.
2. **Guess-and-certify the combination's operator, never the pieces'.** `Σ T·ŵ₃` has a *unique*
   order-3 degree-9 recurrence, known from 501 values with ~460 excess equations — it is
   `L_BZ`, and `guessrec` finds it in **0 s**. The missing object was never the operator; it is
   a *certificate*. Certifying `L_BZ·(Σ T ŵ₃) = 0` directly against the combination is a
   **single** `ct₂` in a known, tiny `Support` box (`r = 3`, `d = 9`) — not 19 searches over
   unknown boxes. **This is the one `ct₂` worth spending a seat on, and it has never been run.**

> ⚠ **Caveat on route 2, stated so it is not mis-sold.** "One `ct₂` in a known box" is the
> *second* half of that route. Its *first* half is `Annihilator` of the **undecomposed**
> 10-letter object — precisely the step that OOM-killed at 14.4 GB (§13.1) and again at 7.8 GB
> for `F_kk` (§17.1). So route 2 is **not** currently runnable either; what §18.13 establishes is
> only that its *telescoping* step is small and known, whereas the split routes have `ct₂` steps
> that are large and unknown. **Route 1 (fewer letters in the combination) is therefore the
> enabling move for route 2, not an alternative to it** — the two are one plan:
> *re-fold the combination to ≤ 4 letters, then telescope it whole in the `(3,9)` box.*
> That is the only proposal on the table that is small at **every** stage, and §18.2's letter-count
> law is what says it would work if the re-folding exists. Whether it exists is a question about
> `ŵ₃`, is purely algebraic, needs **no Wolfram seat**, and is the right first task next session.

## 18.14 The letter-count law, confirmed on `kk` — the campaign's cleanest controlled experiment

`certQ3.wl` was launched on `JOBS=kk:C,kk:B,kk:A,kk:D` at 06:03:49. `kk` is the τ that has never
been closed at **any** stage: `Annihilator[F_kk]` was **OOM-killed at 7.8 GB after 85 minutes**
(§17.1), the single measured hard failure of the whole project.

Its letter-split piece `kk:C` is the same τ at **essentially the same size**:

| object | `LeafCount` | **letters** | `Annihilator` |
|---|---|---|---|
| `F_kk` | 13069 | **10** | **OOM-killed, 7.8 GB, 85 min** |
| `kk:C` = `W_kk R_kk` | **12489** | **0** | **3 generators, 34 s, `mem = 0 GB`** |

**A 4 % difference in size; a 10-vs-0 difference in letters; 85 minutes and 7.8 GB versus 34
seconds and no measurable memory.** Nothing else varies — same τ, same `rho`, same machine, same
RISC. This is the cleanest confirmation available that

> **`Annihilator`'s cost here is governed by the number of harmonic letters, and is essentially
> independent of the size of the rational cofactor.**

`certQ3.wl`'s non-circular assertion block also passed on `kk` for the first time
(`letters-in-cofactors=0`, `symbolic=0`, `points={0,0,0,0,0}`), so the §18.1 four-piece split is
now *executed*, not merely proved, on all five τ.

> **What it does and does not buy.** It retires §17.1's headline failure — `Annihilator[F_kk]` is
> no longer the obstacle, and §17.4's "the single object the τ-split cannot compute" is obsolete.
> Every one of the campaign's *closure and elimination* walls has now fallen. But §18.13 is
> unaffected: the cost has moved wholesale into `ct₂`, and `ct₂` is looking for operators that
> the `guessrec` measurement says are not in range. **`kk` is unblocked at `R1–R3` and still
> blocked at `R5`, exactly like every other piece.**

**Full `kk:C` stage record** (the τ that OOM-killed at 7.8 GB / 85 min, now end-to-end through
`R1–R3` in **69 seconds** at `mem = 0 GB`):

| stage | cost | result | checkpoint |
|---|---|---|---|
| `R1` `Annihilator` | **34 s** | 3 generators | `R_kk_C_ann.m`, 584 KB |
| `R2` `ct₁` (eliminate `l`) | **33 s** | 2 telescopers | `R_kk_C_ct1.m`, 1.36 MB |
| `R3` `OreGroebnerBasis` | **2 s** | `gb === ct₁` telescopers → `True` | `R_kk_C_gb.m`, 124 KB |
| `R4` `DFiniteTimes` (`λ = Ψ_k`) | in flight | — | — |

Compare `certQ.wl`'s `ll:B`, a *seven times smaller* cofactor (1913 vs 10611), under the old
pipeline: `ct₁` ≈ 9 min with a **27.8 MB** checkpoint. `kk:C` does it in 33 s with 1.36 MB.
**The updated complete table across all four τ measured this session:**

| job | cofactor `/T` | letters | `R1` | `R2` | `R3` | total |
|---|---|---|---|---|---|---|
| `n1:A` | 429 | 0 | 0 s | 5 s | 1 s | **6 s** |
| `n2:A` | 4262 | 0 | 6 s | 22 s | 5 s | **33 s** |
| `kk:C` | **10611** | 0 | 34 s | 33 s | 2 s | **69 s** |
| *(`ll:B`, old pipeline)* | 1913 | 0 | 1 s | ≈ 9 min | 3 min 20 s | ≈ 12 min |

`R1–R3` scale *gently* with cofactor size (429 → 10611 leaves, a factor 25, costs 6 s → 69 s, a
factor 12) and `gb === ct₁` holds universally. **There is no longer any object in Theorem B that
the closure or the first elimination cannot handle.** The whole of the remaining difficulty is
`R4` (Wall 2, pieces B and C only) and `R5` (`ct₂`, §18.13).

## 18.15 Session ledger and the exact remaining surface

**Theorem B: `[NOT CERTIFIED]`. Zero `M_τ` exist. No `ct₂` returned, for any piece, by any method.**

### Per-τ status

| τ | pieces (non-zero) | `R1–R3` | `R4` `DFiniteTimes` | `R5` `ct₂` |
|---|---|---|---|---|
| `n1` | A, B, C, D | **A done, 6 s** | n/a for A | **orders 0–5 excluded** (1084 s); kernel reaped on §18.13 |
| `n2` | A, B, C, D | **A done, 33 s** | n/a for A | free ct₂ **600 s no return**; ladder `d ≤ 3` excluded, running |
| `n3` | A, B, C, D | not reached | — | — |
| `kk` | A, B, C, D | **C done, 69 s** — retires §17.1's OOM | **C done, 500 s** — retires Wall 2 (§18.18) | in flight |
| `ll` | **B only** (`p_ll = r_ll = 0`) | done, `ann` 2 s | **37 min, no return — and §18.20 shows this is STRUCTURAL**: `ll:B`'s `ct₁` returns **3** telescopers where every other piece returns 2, giving a 4.8 MB `gb` and a rank-6 product. `ll` is the one τ that does not split, so it gets no rank reduction. Needs the §18.8 `j`-variable move. | never reached |

### Kernels this session

| pid | job | outcome |
|---|---|---|
| `1205156` | `certQ.wl` `ll` `Q4` | inherited; reaped at 37 min inside `DFiniteTimes`. `Q1–Q3` harvested. |
| `1246566` | `certP.wl` `n1,n2,n3` | inherited; reaped at 19 min inside `Annihilator[F_n1]` once §18.2 showed the ranking was inverted. |
| `1311963` | `certQ2.wl` `n1:*,kk:*` | reaped at `n1:A` ladder rung `d=6` on the §18.13 verdict. Checkpoints kept. |
| `1332392` | `certQ3.wl` `n2:*,n3:*` | **running** — `LADDERCAP` will retire `n2:A` and survey the rest. |
| `1413357` | `certQ3.wl` `kk:*` | **running** — the §18.14 law test, already to verdict on `R1–R3`. (`1411153` is only the `timeout math` wrapper; map kernels with `pgrep -f WolframKernel`, not with the wrapper pid — the wrapper's RSS is ~5 MB and looks like a dead kernel.) |

Kernel-hours ≈ 2.0. **The binding constraint was never the budget** — it was that three sessions
of it went into `ct₂` searches that §5.1 had already shown could not succeed.

### What is DONE and must not be recomputed

* the four-piece letter split, `[PROVED symbolically, all five τ]`, RISC-free and non-circular;
* the φ-shift lemma and `phi_tables.m`, cocycle-checked; `phicore.wl`, self-tested;
* `R1–R3` for `n1:A`, `n2:A`, `kk:C` — all checkpointed as `R_<τ>_<piece>_{ann,ct1,gb}.m`;
* the `guessrec` re-measurement at `N = 220` and `N = 460`;
* `Annihilator[F_kk]` is **no longer** an obstacle (§18.14) — delete §17.4's claim that it is.

### What remains, complete list

1. **`ct₂` for 19 pieces.** Zero exist. §18.13 says do not pursue this by splitting.
2. **`R4`/Wall 2** for the 8 B/C pieces and `ll:B` — one attempt in flight (`kk:C`).
3. **Assembly** `certQy.wl`/`certQv.wl` — `[SPECIFIED, PRIMITIVE BUILT AND TESTED]` (§18.5, §18.11),
   bookkeeping only.
4. **19 boundary-obligation pairs** (they sum correctly; `certPv.wl` has the harness).
5. `LCLM` + the finish — `D_n = 0` `[VERIFIED exact]` for `n = 0…300`, so any `ord(M) ≤ 298` closes it.

### The dependency, stated exactly

Theorem B is **not** certified, so the `p ≥ 5` theorem does **not** yet rest solely on `(T1-top)`.
It rests on **both**: `(T1-top)` `[VERIFIED, BLOCKED BY A STRUCTURAL OBSTRUCTION — §16 and,
independently, §18.6/§18.10]`, and Theorem B `[VERIFIED numerically to n = 300, NOT CERTIFIED,
blocked at `ct₂`]`. The single highest-value next action is **algebraic and needs no kernel**:
does `ŵ₃`'s combination admit a re-folding to ≤ 4 harmonic letters? §18.2's law, now confirmed
at both extremes (`0 letters / 12489 leaves` = 34 s; `10 letters / 13069 leaves` = 7.8 GB OOM),
says that if it does, the monolithic route becomes cheap at every stage — and §18.13 says the
monolithic route is the only one whose `ct₂` is known to be small.

## 18.16 Files added or changed this session (all in `work/lb5/`)

| file | what |
|---|---|
| `certQ2.wl` | the four-piece letter-split route, `JOBS="τ:piece,…"`; `HoldRest` from birth; non-circular assertion block |
| `certQ3.wl` | `certQ2` **hardened** — free `ct₂` first (`FREECAP`), `LADDERCAP` so one ladder cannot starve the job list, finished jobs skipped. **Prefer this.** (Cosmetic: still writes a `certQ2_<TAG>.log`.) |
| `phicore.wl` | the §18.5 assembly primitive — `phiOf`, `opPhi`, `phiCocycleTest`. No RISC. Self-tested. |
| `phi_tables.m` | `φ_{A₂}(a,b)`, `φ_{Ψk}(a,b)` for `0 ≤ a,b ≤ 5`; all rational; cocycle-checked to `0` |
| `lsplit.py` | **the M4 experiment** — splits `E(w)/T`'s support into `l`-free (rank 1) and `l`-dependent (remnant, `l`-rank `2^j`) classes; reuses `esupp.py`'s label parser |
| `guessrec_220.log`, `guessrec_460.log` | the §18.13 re-measurement: pieces `None`, combination `(3,9,1)` |
| `launch_certQ2.sh`, `launch_certQ3.sh`, `launch_certQ3_kk.sh` | seat-waiters. **Written as files on purpose** — the harness collapses newlines inside `bash -c '…'`, which silently turned an earlier inline waiter into one long `echo` that launched nothing. |
| `R_<τ>_<piece>_{ann,ct1,gb}.m` | checkpoints for `n1:A`, `n2:A`, `kk:C` |

## 18.17 The letter count, stated precisely — **distinct symbols**, and the exact refold target

§18.2's counts are `HarmonicNumber` *instances*. The quantity that governs the closure is the
number of **distinct** harmonic symbols, since that is the rank of the letter module RISC must
tensor with. Re-measured in the MCP kernel:

| τ | **distinct symbols in `F_τ`** | A | B | C | D |
|---|---|---|---|---|---|
| `n1`, `n2`, `n3`, `kk` | **9** | **0** | 2 | 3 | 4 |
| `ll` | **2** | 0 | 2 | 0 | 0 |

The nine are exactly §4ter's nine —
`H_k, H_l, H_{k+l}, H_{n−k}, H_{n+k}, H_{n+l}, H_{n+k+l}, H⁽²⁾_k, H⁽²⁾_{n+k}` — so §18.2's law
and §4ter's structure theorem are measuring the same object from two directions. The pulled-out
letters are `A₂(k) = {H⁽²⁾_k, H⁽²⁾_{n+k}}` (2), `Ψ_k = {H_k, H_{n−k}, H_{n+k}}` (3) and
`Ψ_l = {H_l, H_{k+l}, H_{n+l}, H_{n+k+l}}` (4). The folded weight `v` itself carries **12**
(the nine plus `H⁽³⁾_k, H⁽³⁾_n, H⁽³⁾_{n+k}`).

**Calibration of the law, both endpoints on the same τ and nearly the same size:**

| distinct symbols | object | `LeafCount` | `Annihilator` |
|---|---|---|---|
| **9** | `F_kk` | 13069 | **OOM, 7.8 GB, 85 min** |
| **0** | `kk:C` | 12489 | **34 s, 0 GB** |

> ### The refold target, stated exactly
> **Does `Σ_{k,l} T·ŵ₃` admit a representative whose summand carries ≤ 4 distinct harmonic
> symbols?** (`ŵ₃` folded to `v` carries 12; `E(v)` carries 9.) Four is the level at which the
> letter-split pieces already sit, and those are computable — `kk:C`'s three letters cost 69 s
> end-to-end through `R1–R3`. If such a refold exists, the **monolithic** route becomes cheap at
> every stage, and §18.13 shows the monolithic route is the only one whose `ct₂` is small
> and known (`L_BZ`, order 3, degree 9, found by `guessrec` in 0 s).
> This is purely algebraic, needs **no Wolfram seat**, and is the single highest-value next task.

### In-flight at hand-off (2026-07-25 ~06:10)

Two kernels left running deliberately — both have a **real** `MEMCAP` (the `HoldRest` fix) and
`certQ3.wl`'s `LADDERCAP`, so neither can starve the box or sit on a ladder indefinitely, and
every completed stage is checkpointed:

| kernel | job | state |
|---|---|---|
| `1332392` | `certQ3.wl` `n2:*,n3:*` | `n2:A` `ct₂` ladder, `d ≤ 3` excluded (10, 27, 64, 166 s). `LADDERCAP` retires it ≈ 06:35 and moves to `n2:C`. |
| `1413357` | `certQ3.wl` `kk:*` | `kk:C` `R4 DFiniteTimes` (`λ = Ψ_k`), ~5 min in. |

**Read `kk:C`'s `R4` when it resolves — it decides whether Wall 2 is real.** `ll:B` failed this
stage at 37 min, but its `gb` was **4.8 MB**; `kk:C`'s `gb` is **124 KB**, 39× smaller, because
the old pipeline telescoped a 3-letter object where the new one telescopes a letter-free one. If
`kk:C`'s `R4` returns, Wall 2 was an artefact of the superseded pipeline and pieces B and C are
viable everywhere; if it does not, Wall 2 is intrinsic and the `j`-variable move of §18.8 is
required. Either way §18.13's verdict on `ct₂` is unaffected.

**One waiter is armed on purpose:** `launch_certQ3_ll.sh` fires when `1332392` exits and runs
`JOBS=ll:B,n3:C,n3:B`. `ll:B` is included because §18.18 showed its 37-minute `DFiniteTimes`
failure was the *old* pipeline's 4.8 MB `gb`, not the object — through `certQ3.wl` its `gb` will
be small. It cannot over-subscribe the licence cap: it waits for a seat to free before starting.
`launch_certQ3.sh` and `launch_certQ3_kk.sh` have already fired and are now only parents of their
`math` children.

## 18.18 **Wall 2 is down** — `DFiniteTimes` returns; `ct₂` is now the *only* remaining obstacle

`kk:C`'s `R4` resolved at 06:13:19:

```
   kk:C annL #4  t=500s  (checkpointed)  mem=0GB      R_kk_C_annL.m, 46.5 MB
```

**4 generators in 8 min 20 s at zero measurable memory** — the stage that `certQ.wl`'s `Q4`
(`ll:B`) failed to return from in 37 minutes and that §18.8 named "Wall 2".

The difference is the size of the `gb` handed to `DFiniteTimes`, and it is a **consequence of the
letter split, not a property of `DFiniteTimes`**:

| | `ll:B` (old pipeline) | `kk:C` (letter split) |
|---|---|---|
| cofactor `/T` | 1913 | **10611** (5.5× bigger) |
| `ct₁` checkpoint | **27.8 MB** | 1.36 MB |
| `gb` handed to `DFiniteTimes` | **4.8 MB** | **124 KB** (39× smaller) |
| `R4` | **37 min, no return** | **500 s, 4 generators, 0 GB** |

The old route telescoped an object that still carried letters, so its `gb` was enormous; the new
route telescopes a letter-free object and its `gb` is small, even though its *cofactor* is five
times larger. **So Wall 2 was never intrinsic — it was §18.2's law acting one stage later.**

> ### Consolidated: every stage except `ct₂` is now clear, on every τ
>
> | stage | status |
> |---|---|
> | `R1` `Annihilator` | **clear** — 0–34 s, even on `kk` (was a 7.8 GB OOM) |
> | `R2` `ct₁` (eliminate `l`) | **clear** — 5–33 s (was ≈ 9 min at best) |
> | `R3` `OreGroebnerBasis` | **clear** — 1–5 s, and `gb === ct₁` universally, so no cofactor chain |
> | `R4` `DFiniteTimes` | **clear** — 500 s on the largest cofactor in the problem |
> | **`R5` `ct₂`** | **THE ONLY WALL. Zero returns, by any method, on any piece, ever.** |
>
> This is the sharpest statement the campaign has reached: the entire residual difficulty of
> Theorem B is **one stage**, and §18.13 shows by direct measurement (`guessrec`: pieces have no
> operator with `r ≤ 12, d ≤ 30`; the combination has order 3) that that stage is **searching a
> box that is empty**. The letter split has therefore done everything it can do — it has cleared
> four stages of five — and the fifth cannot be cleared by splitting further, because splitting
> is what puts the operator out of range.

**Corrections this makes to earlier text.** §18.8's "two walls" is superseded: there is one.
`certQ3.wl`'s `j`-variable proposal for Wall 2 (§18.8) is **no longer needed** — do not spend time
on it. `ll:B` should simply be re-run through `certQ3.wl`, where its `gb` will be small.

## 18.19 Final `ct₂` evidence — three pieces, two independent methods each, zero returns

Completed after §18.18. This is the full experimental record behind §18.13's verdict.

| piece | cofactor `/T` | `Support` ladder | unconstrained `ct₂` |
|---|---|---|---|
| `n1:A` | 429 | `d=0…5`: 1, 6, 15, 49, 185, **828 s** — all none | (kernel reaped before) |
| `n2:A` | 4262 | `d=0…5`: 10, 27, 64, 166, 481, **1985 s** — all none; `LADDERCAP` fired at `d=6` | **600 s, none** |
| `kk:C` | 10611 | (not reached) | **421 s, none** |
| `certU` c₀/β/α | 22317–66499 | — | 79 min, no return (§17.2) |

`n2:A` is the decisive one: it was given **both** methods and 3300 s of kernel time, excluded
orders 0–5 by exhaustive ladder, and returned nothing from an unconstrained search with no ansatz
box at all. `kk:C` is the other decisive one: it is the **only piece to clear `R1`–`R4`
completely** (34 + 33 + 2 + 500 s), reaching `ct₂` with everything upstream done — and `ct₂` still
returned nothing.

> **So the wall is `ct₂`, it is not an artefact of the `Support` ansatz, and it is not caused by
> anything upstream.** Combined with `guessrec`'s measurement that the pieces have no operator
> with `r ≤ 12, d ≤ 30` while the combination has order 3, the explanation is complete and the
> conclusion is not provisional: **splitting cannot produce a certificate for Theorem B.**

**The `LADDERCAP` mechanism worked exactly as designed** — it retired `n2:A` at the 2700 s budget
and moved the kernel straight to `n2:C`, whose `Annihilator` returned **3 generators in 0 s**
(§18.2's law again, on a fourth object). Without it that kernel would have spent ~4.6 h on `d=7`.
Any successor running these scripts should use `certQ3.wl`, never `certQ2.wl`.

**Ladder growth, measured on two objects:** ×3.0–4.5 per rung (`n1:A`: 6, 2.5, 3.3, 3.8, 4.5;
`n2:A`: 2.7, 2.4, 2.6, 2.9, 4.1). Extrapolating `n2:A`, `d=6` ≈ 1.6 h and `d=7` ≈ 6 h — so the
ladder is not merely slow, it is unusable beyond `d=6` on any object in this problem.

**Second complete `R1`–`R4` clear, 26 s.** `n2:C` (cofactor 151, `λ = Ψ_k`, 3 letters pulled out)
went `ann` 0 s → `ct₁`/`gb` → `annL` **25 s** and reached `ct₂` in under half a minute. With
`kk:C` (10611, 500 s) this gives the `DFiniteTimes` scaling:

| piece | cofactor `/T` | `R4 DFiniteTimes` |
|---|---|---|
| `n2:C` | 151 | **25 s** |
| `kk:C` | 10611 | **500 s** |

— a factor 70 in cofactor for a factor 20 in time, i.e. **sub-linear**, and both at ≤ 2 GB.
`DFiniteTimes` is comfortably affordable across the whole problem; §18.8's "Wall 2" is fully
retired and its `j`-variable workaround should be deleted from the plan, not deferred.

> **Closing state of Theorem B.** Stages `R1`–`R4` are clear on every τ and every piece tried,
> at seconds-to-minutes cost, including the two objects that previously defined the campaign's
> hard failures (`F_kk`'s 7.8 GB `Annihilator` OOM and `ll:B`'s 37-min `DFiniteTimes`). Pieces
> now reach `ct₂` cheaply and reliably — and `ct₂` returns nothing, on every piece, by every
> method, exactly as `guessrec` predicts it must. **Theorem B is one stage from done and that
> stage is provably empty at the sizes searched. The next move is algebraic, not computational.**

## 18.20 ⚠ **CORRECTION to §18.18** — Wall 2 is driven by the `(n,k)`-module RANK, not by letters

§18.18 attributed `ll:B`'s 37-minute `DFiniteTimes` failure to the old pipeline telescoping "an
object that still carried letters". **That is false and must not be relied on.** `certQ.log`
records `HarmonicNumber count in GQ (must be 0): 0` — `certQ.wl` was *already* running the
letter-free route for `ll:B`, on the identical object `certQ2/3` builds. The real driver is
visible in the `ct₁` output:

| piece | `ct₁` telescopers = rank of surviving `(n,k)`-module | `gb` | `R4 DFiniteTimes` |
|---|---|---|---|
| `n1:A` | **2** | 48 KB | n/a (`λ=1`) |
| `n2:A` | **2** | 184 KB | n/a |
| `n2:C` | **2** | **12.7 KB** | **25 s**, `annL #4` |
| `kk:C` | **2** | 124 KB | **500 s**, `annL #4` |
| **`ll:B`** | **3** | **4.8 MB** | **37 min, no return** |

So the discriminator is `2` versus `3`. A rank-2 module gives a small `gb` and a **rank-4**
product with the rank-2 letter; a rank-3 module gives a 4.8 MB `gb` and a **rank-6** product.
`DFiniteTimes` cost is governed by that product rank.

**Why `ll` is the exception, and it is structural.** `p_ll = r_ll = 0` means three of `ll`'s four
pieces vanish, so `ll:B` **is** the whole of `F_ll` with only the letter removed — it is not split
at all. The other four τ genuinely divide into four pieces, and *that* is what drops their
`(n,k)`-rank from 3 to 2. **The very fact that made `ll` look easiest (§17.3) is what leaves it
with nothing to split.**

**Consequences, stated so no seat is wasted:**

* §18.18's claim that "`ll:B` should simply be re-run through `certQ3.wl`, where its `gb` will be
  small" is **withdrawn**. `certQ3` builds the identical object and will get the identical 3
  telescopers and the identical 4.8 MB `gb`.
* The `ll:B,n3:C,n3:B` job launched at 06:57 (pid 1834107) is therefore expected to **fail at
  `R4`** — but *safely*: unlike `certQ.wl`, `certQ3.wl` has `HoldRest`, so `MemoryConstrained`
  is real and `R4` will `$Aborted` at `MEMCAP` (3 GB) instead of running unbounded. It then
  returns `$Failed` and proceeds to `n3:C`. The run is self-limiting and still yields `n3`.
* **Wall 2 is retired for rank-2 pieces (16 of the 19) and stands for `ll:B`.** §18.18's
  "consolidated: every stage except `ct₂` is clear" is right for those 16 and wrong for `ll`.
* `ll` therefore **does** still need a distinct idea, and §18.8's `j`-variable move
  (`A₂(k) = Σ_{j=1}^n 1/(k+j)²`, trading the letter for a summation variable and deleting
  `DFiniteTimes`) is **reinstated** for `ll:B` specifically — §18.18 was wrong to delete it.

> **Lesson worth keeping.** §18.18 generalised from three rank-2 pieces to "the wall is gone"
> without checking the one object that had actually failed. The `ct₁` telescoper count was in
> every log the whole time. **Read `ct₁ telescopers:` — it predicts `R4` cost better than any
> leaf count.**

## 18.21 §18.20 confirmed — `ll:B` reproduced `certQ.wl`'s `ct₁` **byte-for-byte**

The correction of §18.20 made a falsifiable prediction — that `certQ3.wl` would build the
*identical* object for `ll:B` and get **3** `ct₁` telescopers, not the 2 that every other piece
returns. Result:

```
   ll:B ann #3  t=2s                              (certQ.wl: ~1 s)
   ll:B ct1 #2  t=1021s   ->  ct1 telescopers: 3  (certQ.wl: ~9 min, 3 telescopers)
   R_ll_B_ct1.m  27,850,782 bytes                 (certQ.wl's Q_ll_ct1.m: 27,850,782 bytes)
```

`cmp` reports the two checkpoints **byte-identical**. So the new pipeline and the old one perform
*literally the same computation* on `ll:B` — which is exactly what §18.20 claimed and what
§18.18 denied. The letter split is a no-op on `ll`, because `p_ll = r_ll = 0` leaves it with a
single piece to "split" into.

> **`ll` is confirmed as a genuine structural exception, not a pipeline artefact.**
> `ct₁` returns 3 telescopers → 4.8 MB `gb` → a rank-6 product under `DFiniteTimes` → the 37-minute
> non-return. `certQ3.wl` will now hit that same `R4`, but with `HoldRest` its `MEMCAP` is real,
> so it will `$Aborted` at 3 GB and move on to `n3:C` instead of hanging — the one thing the run
> does buy us beyond this confirmation.

(The `ct₁` took 1021 s here against ≈ 9 min in `certQ.wl`; the difference is host contention —
the second kernel plus the two 6.4 GB `p3_rate.py` OOM events were running concurrently.)

**Methodological note worth keeping.** §18.18 was wrong for a specific and repeatable reason: it
generalised from three objects that happened to share a property (rank 2) to a claim about a
fourth that did not, without re-checking the fourth. The disconfirming evidence — `ct₁
telescopers: 3` and a 4.8 MB `gb` against everyone else's 13–184 KB — was sitting in the logs
before the claim was made. The cheap guard is the one that worked here: **state the prediction
that would distinguish the two explanations, then run it.** That took 17 minutes of a seat that
was going to run anyway and converted a plausible story into a settled fact.

## 18.22 ⚠ A defect in **my own** `LADDERCAP`, found by measurement — and `certQ4.wl`

§18.8 introduced `LADDERCAP` claiming it meant "one bad piece cannot starve the job list". **That
claim is only true if every rung terminates, and it does not hold.** The check is placed at the
*top of each rung's body*:

```wolfram
   Do[Do[supp = Table[S[n]^i, {i, 0, d}];
      If[AbsoluteTime[] - tLad > LADDERCAP, log[...]; Break[]];      (* between rungs only *)
      ct2 = Quiet[Check[MemoryConstrained[CreativeTelescoping[...], MEMCAP], $Failed]];
```

so it bounds how many rungs are **started**, never the time spent **inside** one. The ladder rungs
carry `MemoryConstrained` but — unlike the free attempt — **no `TimeConstrained`**.

**Measured failure.** `kk:C` entered its `d = 0` rung at 06:20:19 and was still inside it at
07:16 — **56 minutes, one rung, no log line, uninterruptible**, at a flat ~2.0 GB so `MEMCAP`
never fires either. Its `LADDERCAP` of 1800 s was due at 06:36 and is simply never consulted.
The run is bounded only by the outer `timeout 11000`, i.e. it will hold a licence seat until
09:06 doing a single rung that §18.13 says cannot succeed.

`n2:A` masked this: its rungs each returned, so `LADDERCAP` fired exactly as designed at `d = 6`
and the kernel moved on to `n2:C`. **A cap that works on the easy case and is vacuous on the hard
one is worse than no cap, because it is believed.**

**`work/lb5/certQ4.wl`** (`wlcheck`-clean, parses to 57 held expressions with 0 holes, not yet
run) is `certQ3.wl` plus a per-rung `TimeConstrained`:

```wolfram
   ct2 = Quiet[Check[TimeConstrained[MemoryConstrained[
           CreativeTelescoping[annL, S[k] - 1, third, Support -> supp], MEMCAP],
           RUNGCAP, $Failed], $Failed]];
```

`RUNGCAP` (env, default 900 s). With it, `LADDERCAP` becomes a real bound: worst case
`LADDERCAP + RUNGCAP`. **Use `certQ4.wl`, not `certQ3.wl`, for any new run.** `certQ3.wl` was not
edited in place because two kernels are reading it from stdin (§17.5's rule).

> **Pattern worth naming, since this is the third instance in the project.** `stage` lacked
> `HoldRest`, so `MemoryConstrained` was a no-op (§17.5). `certQ.wl`'s assertion compared an
> expression against itself, so it could not fail (§17.3). `LADDERCAP` is tested only where it
> cannot bind (here). **Every safety mechanism this project has written has been silently
> inoperative until a measurement caught it — and in each case the mechanism was believed and
> quoted in the docs in the interim.** The guard that works is the one §13.2 already states:
> a control that has never been *observed to fire* is not a control. `RUNGCAP` should be tested
> by giving it a deliberately tiny value on a rung known to exceed it, before it is trusted.

## 18.23 The `RUNGCAP` control test — it fired, it was **invisible**, and fixing that exposed a
## fourth defect: **a timeout was being logged as an exclusion**

Per the principle that a control never observed to fire is not a control, `RUNGCAP` was tested
before being trusted: `n2:A` (checkpoints on disk, so `R1–R3` load in 3 s) with a cap far below
the rung's known cost.

**Round 1 — `RUNGCAP = 3`, and an anomaly.** Rungs `d=1,2` and all three `{S[n]}` rungs reported
`RUNGCAP TIMEOUT (3s) -- rung ABORTED`. But `third={} d=0` reported **`none` at t=3s**. Round 2 at
`RUNGCAP = 1` reproduced it: `{}` `d=0` again said `none`, at t=1s. Two hypotheses — the rung
genuinely completes fast on an idle box (its original 10 s was measured while the host was
swap-thrashing), or the timeout is being **masked**.

**The discriminating measurement.** Same rung, idle box, `RUNGCAP = 120`:

```
   ct2 third={}     d=0  t=16s -> none
   ct2 third={S[n]} d=0  t=14s -> none
```

**True cost is 16 s.** So the `none` at 3 s and at 1 s were *masked timeouts*, not completions.

**Root cause — nesting order.** The rung was written
`Quiet[Check[TimeConstrained[…, RUNGCAP, rungTimedOut], $Failed]]`. When the abort emits any
message, the **outer `Check` intercepts it and returns `$Failed`**, which the logger printed as
`none`. `Check` must be *inside*, guarding only the computation, so `TimeConstrained`'s default
cannot be swallowed:

```wolfram
   ct2 = TimeConstrained[ Quiet[Check[ MemoryConstrained[CreativeTelescoping[...], MEMCAP],
                                      $Failed]],
                          RUNGCAP, rungTimedOut];
```

**Verified after the fix**, same rung (true cost 16 s), cap 3 s — **5 of 5 capped calls now
announce themselves**, including the free attempt:

```
   ct2 FREE          t=3s -> FREECAP TIMEOUT (3s) -- NOT an exclusion
   ct2 third={}  d=0 t=3s -> RUNGCAP TIMEOUT (3s) -- rung ABORTED
   ct2 third={}  d=1 t=3s -> RUNGCAP TIMEOUT (3s) -- rung ABORTED
   ct2 third={S[n]} d=0/d=1 -> RUNGCAP TIMEOUT (3s) -- rung ABORTED
```

### The fourth defect, and why it is the worst of them

`none` and *timeout* are not the same claim. `none` means **no telescoper of order ≤ d exists**;
a timeout means **we stopped looking**. Conflating them lets a successor exclude an order that
was never searched — a *false negative that corrupts the mathematics*, not merely the accounting.
The final line was doing exactly this: it printed `NO telescoper up to d=1` after every rung had
been aborted. `certQ4.wl` now cannot make that claim unearned:

```
   NO telescoper found up to d=1 BUT 4 rung(s) were ABORTED by RUNGCAP/MEMCAP --
   this is NOT an exclusion. Re-run with a larger RUNGCAP before treating any order as ruled out.
```

and, when every rung really did complete, it says so: `(all rungs ran to completion -- a genuine
exclusion)`.

### Audit — **are §18.12/§18.13/§18.19's exclusions genuine?** Yes. `[CHECKED]`

The question this raises about the session's own results was checked rather than assumed:

* **`certQ2.wl` contains no `TimeConstrained` at all**, and `certQ3.wl` has exactly one — on the
  *free* attempt (line 227), never on a ladder rung. So **every ladder rung in this session ran to
  completion.**
* Their times are all distinct and none coincides with a cap: `n1:A` 1, 6, 15, 49, 185, 828 s;
  `n2:A` 10, 27, 64, 166, 481, 1985 s. A masked timeout would have printed the cap value.
* **⇒ The exclusion of orders 0–5 for `n1:A` and `n2:A` is GENUINE and §18.13 stands unchanged.**
* But the three *free* attempts hit their caps exactly — 421 s (`FREECAP` 420), 600 s and 601 s
  (`FREECAP` 600). **Those three are "did not return within the cap", NOT exclusions.** The prose
  of §18.19 says "no return", which is right; its table said "none", which is not. Read that row
  as **timeout**.

Nothing in §18.13's argument depends on the free attempts being exclusions — it needs only that
they *did not return*, which is what was measured. **The conclusion is intact.**

> **Fifth entry in the §18.22 pattern, and the sharpest.** `HoldRest` missing → `MemoryConstrained`
> a no-op. A self-comparing assertion → could not fail. `LADDERCAP` tested only between rungs →
> vacuous. `Check` outside `TimeConstrained` → the cap fired invisibly. And the exclusion line →
> claimed more than was searched. **Every one was caught by a measurement, none by reading the
> code** — including, twice, code written in this session by the person auditing it. The working
> discipline is not "write careful controls"; it is **"make the control announce itself, then run
> the case that must trip it, and check the announcement appears."**

## 18.24 `ll:B` reproduces `certQ.wl` **byte-for-byte at every stage** — §18.20 fully confirmed

| stage | `certQ3.wl` (`R_ll_B_*.m`) | `certQ.wl` (`Q_ll_*.m`) | identical? |
|---|---|---|---|
| `ct₁` | 27,850,782 B, **3 telescopers** | 27,850,782 B, 3 telescopers | **yes (`cmp`)** |
| `gb` | 4,836,451 B, `gb === ct₁` | 4,836,451 B | **yes (`cmp`)** |

Two independent runs, three weeks of pipeline development apart, producing bit-identical output.
`ll` gets **nothing** from the letter split — §18.18's explanation is refuted at every stage and
§18.20's replacement (the discriminator is the `ct₁` rank, 3 for `ll` versus 2 for all others) is
confirmed at every stage. `ll:B` then entered `R4` and is the object that will exercise the last
open prediction: with `HoldRest` making `MEMCAP` real, it should **`$Aborted` at 3 GB** rather
than hang as `certQ.wl` did for 37 minutes. It was at 2.6 GB when this was written.

> **`ll` needs a genuinely different idea, and it is the only τ that does.** The §18.8
> `j`-variable move (`A₂(k) = Σ_{j=1}^n 1/(k+j)²`, trading the letter for a summation variable so
> `DFiniteTimes` leaves the pipeline) is the one proposal on the table, and it is untried.

---

# §19 — P1e session 6: THE REFOLD RUN. The 7-symbol measurement, and the two-axis cost law

`work/REFOLD.md` produced a representative `ṽ` of `Σ T·ŵ₃` carrying `S = 10` distinct harmonic
symbols, `E(ṽ) = 7`, and **no `C` letter**. §18.17 had calibrated `Annihilator` at **9** symbols
(OOM) and at **0** (34 s) and had nothing at 7. This session ran that point, twice, and ran the
`S = 10` **direct** object beside it.

## 19.1 THE MEASUREMENT — `Annihilator[E(ṽ)]`, 7 symbols — `[MEASURED, does not land]`

```
  E(vtilde) distinct symbols : 7   {H_k, H_{n-k}, H_{n+k}, H^(2)_k, H^(2)_l, H^(2)_{n+k}, H^(2)_{n+l}}
  Etil LeafCount 120100     (E/T coefficients:  c0 = 57100,  beta = 24922,  alpha = 38007)

  R1 ann : MEMORY ABORT after 478 s      MEMCAP = 5.0 GB      peak RSS 5.21 GB
  R1 ann : MEMORY ABORT after 536 s      MEMCAP = 8.5 GB      peak RSS 8.38 GB
```

External `free -m` watch at 20 s cadence, second run — the shape is the point:

```
  07:54:46  2.64 GB     07:55:26  4.95 GB     07:56:06  7.29 GB
  07:55:06  3.81 GB     07:55:46  6.09 GB     07:56:26  8.38 GB  -> $Aborted at 536 s
```

**≈ 3.6 GB per minute, linear, with no sign of convergence**, and only **58 seconds** of extra
wall-clock separates the 5 GB abort from the 8.5 GB abort. `MemoryConstrained` fired correctly
both times — the §17.5 `HoldRest` fix is in `certRF.wl` from its first line — so these are clean
**capped** measurements, not OOM kills, and the second is directly commensurable with §18.17's
9-symbol datum (`F_kk`, 7.8 GB).

> ### The number that fills the calibration gap
>
> | distinct symbols | object | `LeafCount` | `Annihilator` |
> |---|---|---|---|
> | 9 | `F_kk` | 13069 | OOM **7.8 GB**, **85 min** |
> | **7** | **`E(ṽ)`** | **120100** | **abort 8.4 GB, 8.9 min** |
> | 0 | `kk:C` | 12489 | **34 s** |
>
> **Seven is not better than nine — it is worse per unit time.** `E(ṽ)` burns through the same
> memory budget **9.5× faster** than `F_kk` did. §18.17's "the cheapest untested thing on the
> board" has been tested, and the answer is negative.

## 19.2 Why — the cost law has TWO axes, and §18.2 measured only one

§18.2's controlled experiment (`F_kk`, 13069 leaves / 9 symbols → OOM, versus `kk:C`, 12489
leaves / 0 symbols → 34 s) held `LeafCount` **fixed** and varied the letters. It is correct, and
it is half the law. Every `Annihilator` measurement of the campaign, in one table:

| object | distinct symbols | `LeafCount` | `Annihilator` |
|---|---|---|---|
| `kk:C`, `n2:C` (letter-split pieces) | **0** | 12489 / small | **34 s** / **0 s** |
| ~~**`T·v`** (folded weight, §5.2 cost model)~~ | **12** | **110** | ~~124 s, 7 generators~~ **WITHDRAWN** (§19.4 ⚠): re-measured, **TIME ABORT at 600 s** |
| `F_n1` (τ-split) | 9 | 578 | 19 min, no return |
| `F_kk` (τ-split) | 9 | 13069 | OOM 7.8 GB, 85 min |
| `E(v)` monolith (`certT3.wl`, §13.1) | 9 | 132917 | OOM 14.4 GB, 50 min |
| **`E(ṽ)`** (this session) | **7** | **120100** | **abort 8.4 GB, 536 s** |
| **`T·ṽ`** (this session) | **10** | **91** | §19.4 |

Read the last row against the second-to-last. `T·ṽ` carries **more** letters than `E(ṽ)` — ten
against seven — and is the only object in the campaign whose `Annihilator` was ever stopped by a
*cap* rather than by its own growth (§19.4), because its coefficients are polynomials in
`(n,k,l)` of trivial size. (The old comparison used `T·v` at "124 s"; that figure is withdrawn —
§19.4's ⚠ box.) `E(ṽ)` carries fewer letters and cannot be closed
at any memory this box can offer, because each of its three coefficients is a five-term sum in
which the `kk` term carries `ρ` (**10553** leaves) and the `ll` term carries `σ` (**1819**).

> **The law, corrected.** `Annihilator` needs the object small on **both** axes, letters *and*
> coefficients. The τ-split fixed the coefficient axis and left the letters. The letter-split
> fixed the letters. The **refold** fixes the letters of `E` — and cannot fix its coefficients,
> **ever**, for a structural reason: `E(w) = Σ_τ G_τ(τ.w − w)` with `G_kk = −ρ|_{k+1}T(k+1)` and
> `G_ll = −σ|_{l+1}T(l+1)`, so the only way to shed `ρ` and `σ` is to have `τ.w − w = 0` for
> `τ = kk` **and** `τ = ll`, i.e. for `w` to be invariant under `k → k+1` and `l → l+1`, i.e.
> for `w` to depend on `n` alone — which the weight-3 fit excludes.

**Consequence, and it is the strategic content of this session.** *Every* representative `w`,
however few letters it carries, yields an `E(w)` whose coefficients are `Θ(ρ, σ)`. So the
`E`-route to Theorem B — §4quater's reduction, the τ-split, the letter-split, and the refold
alike — is blocked at `Annihilator` by an obstruction that lives in the **Q-row certificate**,
not in the weight. **The route with a future is the one that never forms `E` at all:** telescope
`T·w` directly, where the coefficients are polynomial and the `ct₂` box is the known, occupied
`(3,9)`. That is §19.4.

## 19.3 `[CERTIFIED — RISC-free and SYMBOLIC in ℚ(n,k,l)[hh…]]` — the refold `E`-identity

Before any telescoping was attempted, `REFOLD` §4.6's closed form was rebuilt from scratch and
checked in a kernel that never loaded RISC (`verifycore.wl`'s own Γ-shift calculus `tratio` and
harmonic normaliser `hnorm`), **against the raw definition** `Σ_τ W_τ(τ.ṽ − ṽ)` — that is,
against `HarmonicNumber` itself, not against any restatement of the tables:

> `E(ṽ)/T = c₀ + β·( A₂(l) − A₂(k) ) + α·Ψ_k` ,  `Ψ_k = A₁(k) + 3B₁(k)` ,
> `α = Σ_τ (G_τ/T)·½dX_τ` , `β = Σ_τ (G_τ/T)·½dY_τ` ,
> `c₀ = Σ_τ (G_τ/T)·( dh₃_τ + 2da₃_τ + ½dX_τ dY_τ )`
>
> `zeroReport` → **7 hh-symbols, 7 coefficient classes, 0 non-zero.**

This is the weight-3 refold analogue of §13.3's `[CERTIFIED]` τ-split identity, and it is the
one product of this session that is unconditionally reusable. Two further guards ran inside
`certRF.wl` and had to pass before it would telescope anything:

* **the shift tables of `REFOLD` §4.6, symbolically, for all five τ** —
  `Simplify[FunctionExpand[τ.h₃ − h₃ − dh₃_τ]]` and likewise for `da₃, dX, dY`:
  **`{0,0,0,0}` for every one of `n1, n2, n3, kk, ll`.** In particular `dY_ll = 0`, hence
  `p_ll = q_ll = 0` and τ = `ll` contributes to the `Ψ_k` branch **only** — the weight-3
  analogue of §17.3's `p_ll = r_ll = 0`, now landing on the other branch;
* **`ṽ` itself** — 11 `HarmonicNumber` instances, **10 distinct symbols**, `C`-letter-free, and
  `E(ṽ)` exactly **7**: `REFOLD`'s census reproduced independently, in the run that consumes it.

## 19.4 The direct route `T·w` — and a CORRECTION to the §1 cost model that changes its prospects

`certRFD.wl` telescopes the **summand itself**: no `E`, no Q-row, no `E`-boundary lemma, and a
`ct₂` box that is known *and occupied*. Two objects were run.

| object | symbols | `LeafCount` | `Annihilator` | cap that fired |
|---|---|---|---|---|
| `T·ṽ` | 10 | **91** | MEMORY ABORT, 1991 s | `MEMCAP` **2.5 GB** |
| `T·ṽ` rerun, empty box | 10 | 91 | **TIME ABORT, 5402 s** — **peak RSS 5.01 GB against a 9 GB cap** | `ANNCAP` **5400 s** |
| `T·v` (the §5.2 fold, with the `C` letter) | 12 | 110 | TIME ABORT, 600 s | `ANNCAP` **600 s** |

**Neither abort is a verdict — both are caps I set, and both were set low on purpose** (2.5 GB so
`T·ṽ` could not threaten the co-resident `E(ṽ)` run; 600 s because `T·v` was a deliberately tight
probe). What matters is the *shape* of the `T·ṽ` trace, which is the opposite of `E(ṽ)`'s:

```
   T*vtilde   RSS 0.92 GB (07:42)  ->  1.10  ->  1.68  ->  2.10 GB (08:14)
              = 0.036 GB/min over 33 minutes, LINEAR AND FLAT
   E(vtilde)  RSS 2.64 -> 4.00 -> 6.09 -> 8.38 GB in 100 seconds
              = 3.6 GB/min
```

**A factor of 100 in growth rate.** `E(ṽ)` was diverging; `T·ṽ` is computing. `MemoryConstrained`
counts memory *allocated by the evaluation*, not RSS, which is why a 2.5 GB nominal cap fired at
2.1 GB resident — the cap was simply too small for the object, not too small for the box.

> ### ⚠ CORRECTION — §1's `Annihilator[T·v] = 124 s, 7 generators` does not reproduce
>
> This session ran that exact object (13 `HarmonicNumber` instances, **12 distinct symbols**,
> `C` letter present, `LeafCount` 110 — `certP.wl`'s `vw` verbatim) under a **correctly timed**
> `stage`, and it did **not return in 600 s**. §17.5 supplies the explanation: before the
> `HoldRest` fix, `stage`'s `t=…s` was **`Put` time only, not stage time** (that is how
> `certQ.wl`'s "`ct1 t=3s`" turned out to be ≈ 9 minutes). **The 124 s figure is almost
> certainly a `Put`-time artifact**, and with it goes the one measurement that made the direct
> route look cheap. Every timing in §1/§5.2's cost model taken through the pre-fix `stage`
> should be treated the same way — as a lower bound of unknown quality, not a cost.
>
> The consolation is that the *ordering* it induced survives on independent grounds, and the
> two objects are now measured honestly for the first time.

> ### The resourced rerun, and the campaign's first TIME-bound object
>
> Rerun on an empty box at `MEMCAP = 9 GB`, `ANNCAP = 5400 s`: it sailed past the earlier 1991 s
> abort point and ran the **full 90 minutes**, then stopped on the **time** cap with **peak RSS
> 5.01 GB — barely half its memory budget**. The trace is a *sawtooth*, not a ramp:
>
> ```
>   08:26  0.74 GB    08:59  4.32 GB    09:27  2.85 GB    09:38  3.87 GB    09:48  3.10 GB
> ```
>
> — memory is **reclaimed**, repeatedly, which no diverging computation in this campaign has ever
> done. Against `E(ṽ)`'s monotone 3.6 GB/min ramp to abort in 100 seconds, this is a different
> regime entirely.
>
> **`Annihilator[T·ṽ]` is TIME-bound, not memory-bound — the first object in the campaign with
> that diagnosis.** Every previous failure (14.4 GB, 7.8 GB, 8.4 GB) was memory divergence, which
> says *no*. A bounded-memory sawtooth says *not yet*: the question becomes "how long", and that
> is a question this campaign has never before been in a position to ask.

`launch_certRFD_kl.sh` (the `ORD = kl` swap) waited out its 100-minute window without `RFD_ann.m`
appearing and **self-disarmed at 09:38:42**; it never held a seat.

## 19.5 Everything the refold rests on, re-verified this session (no Wolfram seat)

| claim | how | result |
|---|---|---|
| `Σ_{k,l} T·ṽ = P̂_n` | `refold/checkrec.py`, exact ℚ | **ALL PASS, `n = 0…33`** |
| `L_BZ·(Σ T·ṽ) = 0` | same, certified V6b coefficients | **ALL ZERO, `n = 0…30`** |
| `ŵ₃ − ṽ ∈ PROVED kernel` | `refold/keyid.py` | `ŵ₃ − v` **True** (rank 57 → 57) and `v − ṽ` **True** (57 → 57), hence `ŵ₃ − ṽ` **True** |
| the refold identity | `keyid.py`, exact | `Σ T[3A₂(k)C₁ + A₂(k)A₁(l) + 2A₂(l)A₁(k) + 6A₂(l)B₁(k)] = 0`, `n = 0…25`, **ALL ZERO**; it equals `−4(v − ṽ)` |
| far-edge boundary for `T·ṽ` | MCP kernel, `Limit` | `T·ṽ → 0` at **all 15** cells with `k` or `l ∈ {n+1,n+2,n+3}`, `n = 3,4,5`; `ṽ`'s pole there is **simple** (residue `1049291/4233600` at `n=4, l=2, k=5`) against `T`'s **double** zero |
| the `(3,9)` box is occupied | `guessrec.py`, `N = 461` | combination → **`(3, 9)`, nullity 1**, 0 s; pieces `U₁…U₅` → **None** |
| initial values | `seqdata300.json` | **301 consecutive** exact values, `n = 0…300`, zero entries with `ok = False` |

So every side condition a Theorem-B certificate will need is now discharged **in advance**,
including the boundary check CERTS_RESUME §4.0 flags as "easiest to assume and hardest to notice
missing". The only missing object is still the certificate itself.

## 19.6 Status of Theorem B after this session

**Theorem B remains `[VERIFIED, NOT CERTIFIED]`.** No telescoper was produced. What changed is
*which* obstruction it faces, and that is a real change:

| route | status after §19 |
|---|---|
| `E(w)` via the Q-row (§4quater → §13 → §17 → §18 → the refold) | **`[BLOCKED BY A STRUCTURAL OBSTRUCTION]`.** `Annihilator` cannot close `E(w)` for *any* `w`, because `E`'s coefficients are `Θ(ρ, σ)` for every non-constant `w` (§19.2). Measured at 9 symbols (OOM 7.8 GB) and now at 7 (abort 8.4 GB, diverging at 3.6 GB/min). |
| splitting (τ-split, letter-split) | **`[BLOCKED]`, §18.13** — `ct₂` searches a provably empty box. |
| **`T·w` direct, in the known `(3,9)` box** | **the only live route.** Not yet measured to a conclusion: both attempts stopped on caps I set, and `T·ṽ`'s memory trace is flat (0.036 GB/min) where `E(ṽ)`'s diverged (3.6 GB/min). A properly-resourced run is in flight. |

So Theorem B is no longer "one stage from done with four routes open"; it is **one route, one
stage** — `Annihilator[T·w]` — with every downstream obligation already discharged (§19.5) and
the whole assembly + RISC-free verification chain written and smoke-tested (`certRFy.wl`,
`certRFv.wl`). If that annihilator closes, nothing else is in the way: `ct₁` eliminates `l`
against a **single** `l`-side letter `A₂(l)` and no `C` letter, and `ct₂` searches the one box in
this problem that is known to contain its answer.

## 19.7 What this session settles, stated so it is not re-litigated

1. **The 7-symbol point is measured and negative** — twice, at 5.0 GB and 8.5 GB, diverging
   linearly. `REFOLD`'s central hope ("the cheapest untested thing on the board") is closed.
2. **The letter-count law is half a law.** Cost is governed by letters **and** coefficient size;
   §18.2 varied only the first because it held `LeafCount` fixed by construction.
3. **`E` can never be cheap**, for any refold, because `ρ` and `σ` are welded into `G_kk`, `G_ll`.
   This is the first *structural* (rather than empirical) statement about the `E`-route.
4. **The pre-`HoldRest` timings are not costs.** §1's `Annihilator[T·v] = 124 s` does not
   reproduce; §17.5's `Put`-time artifact explains it. Do not plan against those numbers.
5. **`ṽ` is sound and fully instrumented**: `ŵ₃ − ṽ` is in the PROVED kernel, `Σ T·ṽ = P̂_n`
   exactly, the far-edge boundary vanishes, 301 initial values are banked, and the RISC-free
   verifier handles it under every shift it will meet.

## 19.8 Ops record

* **Seat contention is now a real failure mode, and it cost this session ~40 minutes.** The
  waiter `launch_certQ3_ll.sh`, armed in session 5, fired at **06:57:22** and took the seat this
  session's decisive run had been promised, running a piece-`ct₂` job that §18.13/§10.7 prove is
  searching an empty box. **An armed waiter is a claim on a future seat: disarm any waiter whose
  job has been superseded before handing off.** `kill -KILL` is still blocked by the permission
  classifier for the agent that needs it — the only route is to ask the orchestrator, so state
  the pids and the order in the request.
* `wlcheck.py` earned its keep again: it flagged a truncation-risk multi-line assignment in
  `certRFv.wl` (`base = … + … + …`) **before** it ran. That is the fourth distinct object this
  guard has saved.
* Both new run scripts carry `SetAttributes[stage, HoldRest]` from the first line and wrap every
  stage in **both** `TimeConstrained` and `MemoryConstrained`. `MemoryConstrained` is what fired,
  twice, exactly as designed; `TimeConstrained` on `Annihilator` was never reached. The external
  20 s `free -m` watch is what makes the abort *interpretable* — the cap alone tells you it
  stopped, the watch tells you it was diverging linearly and would never have returned.

## 19.9 Files added this session (all `work/lb5/` unless noted)

| file | what |
|---|---|
| `certRF.wl` | the `E(ṽ)` run — assertions (10/7 symbols, §4.6 tables symbolic, 6-point split check) then `R1`–`R4` |
| `certRFD.wl` | the **direct** run — `Annihilator[T·ṽ]`, then `ct₁`/`gb`/`ct₂` in the known `(3,9)` box, with an `M/L_BZ` coefficient-ratio check |
| `certRFy.wl` | composition of the two-step certificate into single-certificate form (no `LCLM`, no cofactors — the object was never split) |
| `certRFv.wl` | **RISC-free** verification: V-A letter form vs raw definition, V-B the certificate, V-C `M = L_BZ`, V-D boundary at `k=0`/`l=0`, V-E denominators |
| `certRF_lk_MEMCAP5G.log`, `certRF_lk_MEMCAP8G5.log` | the two S1 measurements |
| `memwatch_run1.log`, `memwatch_run2.log` | the external memory traces behind them |
| `launch_certRF.sh`, `launch_certRF2.sh`, `launch_certRFD.sh` | the launchers |

## 19.10 In flight at the close of session 6 (2026-07-25 08:24), and the ONE thing to do next

> **Resolved in session 7 — see §19.11.** The run handed off below stopped on its **time** cap
> after 5402 s with **peak RSS 5.01 GB of a 9 GB budget** and a sawtooth trace. It was succeeded
> by a 20000 s continuation. Read §19.11 for the outcome; this section records what was handed
> off and why.

```
  certRFD.wl  ORD=lk  MEMCAP=9000000000  ANNCAP=5400  timeout 11000    started 08:24:16
        -> deadline 09:54:16 ; log certRFD_lk.log ; checkpoint RFD_ann.m ; external
           watch memwatch3.log at 30 s cadence
  launch_certRFD_kl.sh  ARMED -- fires the ORD = kl swap on the second seat the moment
        RFD_ann.m exists, and LOADS that checkpoint rather than recomputing it
        (Annihilator is ORD-independent; only ct1/ct2 differ).
```

**Disarm the waiter if you supersede the run** — §19.8's own lesson. It is a bash loop; ask the
orchestrator for the `kill -KILL`, giving the bash pid first. *(In the event it self-disarmed at
09:38:42 without ever taking a seat — §19.11.2.)*

**If `RFD_ann.m` lands**, nothing further is in the way and every stage is written:

1. `ct₁` eliminates `l`. `ṽ` has **no `C` letter**, so its entire `l`-side content is the single
   letter `A₂(l)` — the structural gain of the refold, and the reason to prefer `ṽ` over `v` here.
2. `gb`, then `ct₂` on `Support -> {1, S_n, S_n², S_n³}` — the **one box in this problem known to
   contain its answer** (`L_BZ`, order 3, degree 9, `guessrec` 0 s from 501 values).
3. `math < certRFy.wl` composes the two-step certificate into
   `M·(T ṽ) = Δ_k(X·T ṽ) + Δ_l(Y·T ṽ)` — no `LCLM`, no right cofactors, because the object was
   never split.
4. `math < certRFv.wl` verifies it RISC-free: V-B the certificate, V-C that `M` **is** `L_BZ`
   coefficientwise, V-D the `k = 0` / `l = 0` boundary pair, V-E the denominators. Exactly one
   boundary pair, not nineteen.
5. The finish needs no new computation: `L_BZ·(Σ T ṽ) = 0` plus `L_BZ·P̂ = 0` plus **301** exact
   values plus `lc(L_BZ) = 2(n+3)⁵(2n+5)a₀(n)` having no integer root `n ≥ 0` `[PROVED]` gives
   `Σ T ṽ = P̂`, and `Σ T ŵ₃ = Σ T ṽ` because `ŵ₃ − ṽ` is in the **PROVED** kernel. **Theorem B.**

**If it does not land**, the position to record is that all four routes are now measured and
blocked at a *named* stage — three structurally — and the next move is algebraic, not
computational: attack the **∂-finite closure** of `T·w` rather than its letter count. `REFOLD`
§5.5's six-dimensional gap in the proved kernel (`dim ker V = 63` against `dim span(proved) = 57`)
is the only place a better representative could still be hiding, and writing down the weight-3
residue identities that `PHASE2_CANCEL` §3 says exist is what would close it.

---

## 19.11 P1e session 7 — THE RESOURCED DIRECT RUN, RESOLVED: `Annihilator[T·ṽ]` is **TIME**-bound, not memory-bound

The run §19.10 handed off (`certRFD.wl`, `ORD = lk`, `MEMCAP = 9 GB`, `ANNCAP = 5400 s`, started
08:24:16) was babysat to resolution. It **did not return**, and *how* it failed is the datum:

```
  D1 ann : TIME ABORT after 5402 s      Sat 25 Jul 2026 09:54:18
           MEMCAP 9 GB      peak RSS 5.01 GB (09:34)      RSS at abort 3.12 GB
```

`certRFD_lk_ANNCAP5400.log`; external `free -m` watch at 30 s, 177 samples,
`memwatch_run4.log` (a second, independent watch at 30 s in `memwatch4.log`).

> ### The RSS trace, which is the whole content of this section
>
> ```
>   08:25  0.74      08:53  2.52      08:59  4.32      09:13  4.45      09:34  5.01
>          ↑ climb          ↓ 2.21           ↓ 2.58           ↓ 2.84           ↓ 3.08 (09:52)
> ```
>
> Local extrema, 0.3 GB hysteresis: `0.74 → 2.52 ↓2.21 ↑4.32 ↓2.58 ↑4.45 ↓2.84 ↑5.01 ↓3.08`.
> End-to-end slope **0.027 GB/min** over 89 minutes. **The trace is a sawtooth, not a ramp:**
> RSS *falls* by 1.7–2.2 GB four separate times. That is real garbage collection between phases
> of a computation, and it is qualitatively unlike anything else in this campaign.

| object | how it died | memory budget used at death |
|---|---|---|
| `E(v)` monolith (§13.1) | OOM-killed, 50 min | **14.4 GB — uncapped, killed the box** |
| `F_kk` (§17.1) | OOM-killed, 85 min | **7.8 GB** |
| `E(ṽ)` (§19.1) | `MemoryConstrained` abort, 478 s / 536 s | **5.21 / 8.38 GB — the cap, twice** |
| **`T·ṽ` (this run)** | **`TimeConstrained` abort, 5402 s** | **5.01 GB peak of 9 GB; 3.12 GB at the abort** |

**`T·ṽ` is the first object in the entire campaign to be stopped by the clock.** Every other
failure in §§13–19 was memory: an OOM kill or a `MemoryConstrained` cap firing. This one had
**44 % of its memory budget unused at its own peak** and **65 % unused at the moment it was
stopped**, and it was still cycling. §19.4's provisional reading ("`T·ṽ` is computing, `E(ṽ)`
was diverging") is now confirmed on the only evidence that could confirm it.

### 19.11.1 What this does and does not license

* **It does not produce a certificate.** `RFD_ann.m` was never written; `ct₁`, `gb`, `ct₂`,
  `certRFy.wl` and `certRFv.wl` were therefore never reached. Nothing downstream ran.
* **It is not an exclusion.** A `TimeConstrained` abort is a statement about `ANNCAP`, not about
  the object — the certQ4 discipline. What is now measured is a **lower bound**:
  `Annihilator[T·ṽ]` costs **more than 90 minutes** at ≤ 5 GB. It is not measured to be
  infinite, and the memory evidence is against divergence.
* **The discriminator asked for in the hand-off has answered "stopped by budget".** Divergence
  would show as monotone RSS growth ending at the cap, as `E(ṽ)` did at 3.6 GB/min. `T·ṽ` grew
  at **0.027 GB/min net**, with four large releases, and hit a *time* wall with memory to spare.

### 19.11.2 The `ORD = kl` swap never fired — and that is correct

`launch_certRFD_kl.sh` was armed to take seat 2 the moment `RFD_ann.m` appeared. It never did,
so at **09:38:42** the waiter logged

```
  RFD_ann.m never appeared; ORD swap not launched at Sat Jul 25 09:38:42 BST 2026
```

to `certRF_launch.trace` and **exited by itself**, taking no seat. This is the §19.8 failure
mode not recurring: the waiter was conditional on the checkpoint, and its horizon
(400 × 15 s ≈ 100 min from 07:58) expired *before* it could collide with anything. No kill was
needed and no seat was stolen.

### 19.11.3 In flight at the close of session 7

```
  launch_certRFD_long.sh   armed 09:38:45 by the orchestrator, FIRED 09:54:25
    certRFD.wl  ORD=lk  MEMCAP=9000000000  ANNCAP=20000  CT1CAP=5400  timeout 24000
    -> ann deadline 15:27:50 ; hard stop 16:34:25 ; kernel pid 2207229
    -> log certRFD_lk.log ; checkpoint RFD_ann.m ; external watch memwatch5.log (30 s)
  preserved from the 5400 s run: certRFD_lk_ANNCAP5400.log , memwatch_run4.log
```

It is guarded: it fires only if the previous log contains `TIME ABORT` and `RFD_ann.m` does not
exist, so it cannot race a success. **Its outcome is trichotomous and all three branches are
informative:**

| branch | reading |
|---|---|
| `ann` returns | the chain of §19.10 fires with nothing in its way — everything downstream is discharged (§19.5), written and `wlcheck`-clean. **Theorem B.** |
| **memory** abort at 9 GB | the first evidence that `T·ṽ` diverges after all. The direct route would then join the other three, and the position becomes fully algebraic. |
| **time** abort at 20000 s | `Annihilator[T·ṽ]` costs **> 5.5 h** at ≤ 9 GB. The direct route stays open but becomes a hardware question, not a mathematics one; the next move is a bigger box, not a cleverer object. |

## 19.12 Theorem B — the definitive status at the close of session 7

**`[VERIFIED, NOT CERTIFIED]`.** No telescoper for Theorem B exists, in any route, at any date in
this campaign. What sessions 6–7 changed is that the *reason* is now different in kind for each
of the four routes, and only one of the four is a resource question:

| route | status | kind of obstruction |
|---|---|---|
| `E(w)` via the Q-row, any fold | **`[BLOCKED]`** | **STRUCTURAL** — `E`'s coefficients are `Θ(ρ, σ)` for every non-constant `w` (§19.2). Measured negative at 9 letters *and* at 7. |
| τ-split | **`[BLOCKED]`** | **STRUCTURAL** — inherits the same `ρ, σ`; `Annihilator[F_kk]` OOM. |
| letter-split | **`[BLOCKED]`** | **STRUCTURAL** — §18.13/§10.7: `ct₂` on pieces searches a *provably empty* box (`guessrec` finds no operator for any single-letter component sum; only the combination has one). |
| **`T·w` direct** | **`[OPEN — stopped by budget]`** | **RESOURCE.** `Annihilator[T·ṽ]` (10 letters, `LeafCount` **91**) time-aborted at 5402 s having used 5.01 GB of 9 GB, RSS sawtoothing. Cost lower bound **> 90 min**; no evidence of divergence. |

**Stated precisely, so it is not overclaimed and not underclaimed:** Theorem B is one
`Annihilator` call away from a machine certificate — the *same* one call it was a session ago —
and that call is now known to be time-expensive rather than memory-explosive. Everything the
certificate consumes is already discharged and re-verified (§19.5): `Σ T·ṽ = P̂` exact to
`n = 33`, `L_BZ·(Σ T·ṽ) = 0` to `n = 30`, `ŵ₃ − ṽ` in the **PROVED** kernel, the far-edge
boundary zero at all 15 tested cells, the `(3,9)` `ct₂` box known *and occupied*, 301 exact
initial values, and a RISC-free verifier that handles `ṽ` under every shift it will meet.

## 19.13 Session 7 ops record

* **The direct-object cost row is filled**, and it is the row the campaign was missing:

  | object | letters | `LeafCount` | `Annihilator` | stopped by |
  |---|---|---|---|---|
  | `T·ṽ` | 10 | **91** | **no return in 5402 s**, peak 5.01 GB of 9 GB | **TIME** |
  | `T·v` | 12 | 110 | no return in 600 s | TIME (tight probe) |
  | `E(ṽ)` | 7 | 120100 | abort 536 s | **MEMORY**, 8.4 GB |

* **A conditional waiter is safe; an unconditional one is not.** `launch_certRFD_kl.sh` and
  `launch_certRFD_long.sh` are both gated on a *file* and a *log string*, so neither could fire
  into a state it was not written for; the former self-disarmed on schedule. Contrast §19.8's
  `launch_certQ3_ll.sh`, which fired on a timer and took a seat.
* **`[WITHDRAWN]` this session**: the "`Annihilator[T·v] = 124 s, 7 generators`" figure has been
  struck at its source (§1's calibration table) and everywhere it was quoted as current (§19.2's
  cost table and prose, the STATUS BOARD row for §19, `CERTS_RESUME` §§2 and 11.2). §19.4's ⚠
  box explains it: `Put` time, not stage time, through the pre-`HoldRest` `stage` (§17.5). A
  blanket warning now sits under §1's table: **every timing there is a lower bound of unknown
  quality, not a cost.**
* **Papers.** `papers_out/sharp12/sharp12.tex` §14.3 (`\label{sec:certsB}`) now carries the
  structural finding — the two-axis cost law, the $7$-letter measurement, and the
  `G_kk = −(ρT)|_{k→k+1}`, `G_ll = −(σT)|_{l→l+1}` argument that no refolding can make `E(w)`
  cheap — followed by the direct route and its discharged side conditions. The closing sentence
  no longer reads "algebraic rather than computational" unqualified, because the direct route is
  a live computation. Recompiled 3× `pdflatex`: **45 pages, 0 errors, 0 undefined references.**
  Remark `rem:flip` (numbered **14.6**, not 14.9) is untouched — Theorem B did not certify, so
  the one-line flip it anticipates was **not** applied.
* **Box state at 10:00, verified by `ps`.** Exactly one compute job runs — the gated
  `launch_certRFD_long.sh` (pid 2180174) → `timeout 24000 math` (2207228) → kernel (**2207229**)
  of §19.11.3 — with **one** external `free -m` watch on it (pid 2209932 → `memwatch5.log`,
  30 s, resolving the live kernel by `pgrep -P 2207228`). The `ORD=kl` waiter self-disarmed at
  09:38:42. **Six** stale `free -m` loops from sessions 6–7 were terminated: five were polling
  pids that had already died (`memwatch.log`, `memwatch2.log`, `memwatch3.log`, `memwatch4.log`)
  and one was a duplicate watch on the live run. *(`memwatch5.log` therefore has a few
  interleaved lines between 09:58:39 and 09:59:39, where the duplicate overlapped; the trace is
  otherwise a clean 30 s series.)* **No orphaned waiter, no orphaned kernel, no duplicate
  watch.** 12.1 GB available, 9.1 GB free.
* **Lesson, added to §11.5's list.** `ps -eo pid,args | grep …` truncates its own output and
  under-reports background loops — the duplicate watch was invisible to it and showed up only
  under `ps -eo pid,ppid,lstart,args`. **Audit the box with `lstart` and match on the loop
  bound, not on the command prefix.**
