# REFEREE_PAPERS — hostile referee pass on the four drafts (task W6)

**Date:** 2026-07-25 · **Stance:** adversarial; every transcription treated as wrong until
recomputed. All arithmetic below is exact (Python `fractions`/`sympy`/integer). No standalone
kernels were launched. Papers were touched **only** to insert `%% REFEREE` comments; every
`.tex` still compiles, and the rendered page counts are unchanged.

| paper | verdict |
|---|---|
| **P1 `sharp12/sharp12.tex`** (42 pp) | **ISSUES-FOUND** — 1 CRITICAL, 7 MAJOR, 1 MODERATE, 7 MINOR |
| **P2 `lucas2nd/`** (38 pp) | **ISSUES-FOUND** — 0 CRITICAL, 3 MAJOR, 11 MINOR |
| **P3 `padiclimits/`** (29 pp) | **ISSUES-FOUND** — 1 CRITICAL, 4 MAJOR, 4 MINOR |
| **P4 `frobenius/`** (25 pp) | **ISSUES-FOUND** — 2 CRITICAL, 3 MAJOR, 11 MINOR |

---

# 0. THE DEPENDENCY QUESTION — ADJUDICATED

**Question.** Session 5 (`PHASE2_CERTS.md` §18.15, line 2258) states:

> *"Theorem B is **not** certified, so the `p ≥ 5` theorem does **not** yet rest solely on
> `(T1-top)`. It rests on **both**."*

The v4 tree (`PHASE2_THEOREM.md`, lines 29–34 and 103) states the opposite:

> *"modulo only the decomposition certificate `(T1-top)` … (The companion middle-row statement
> about `P̂_n` needs the second identity `P̂_n = Σ T·ŵ₃`, Theorem B; the `P_n` law above does not.)"*

## RULING: the v4 tree is right about ŵ₃. Session 5's sentence is a non-sequitur. But the v4 tree undercounts anyway — for a different reason.

### (a) Nothing in the P_n chain consumes ŵ₃. **Confirmed, three independent ways.**

1. **Citation trace in the paper.** `\ref{thm:B}` and `\wthree` occur at lines 795–855 (the
   statement of Theorem B, §5.2), 1465 (a remark noting only that Lemma Φ lives in *the same
   alphabet*), 2565–2647 (§13, the middle row), 2706–2820 (§14, certification status) and
   2910–2911 (§16 table). **Zero occurrences in §§3–11** — the entire P_n chain (bottom row,
   H-layer, carry lemmas, depth calculus, fibre congruence, induction, off-regime descent,
   nucleus). Line 943's `w_3` is a *different* object (Apéry's weight, §5.4) — see MAJOR-1.
2. **Source logs agree.** `PHASE2_ENDGAME.md` §B's dependency tree (lines 660–697) puts
   Theorem B strictly inside the `(MIDDLE ROW)` subtree, never under `(SHARP-12, p≥5)`.
   `PHASE2_GAPDESC.md` §9 line 426: *"The single remaining obligation for the `P_n` law is the
   decomposition certificate `(T1-top)`; the middle row **additionally** needs Theorem B."*
   `PHASE2_NUCLEUS.md`'s only `P̂` hits (lines 42, 94, 291, 351) are **control experiments**
   (`L̃` annihilates `P̂` too; the `(REC-★)` congruence fails for `P̂`, which is what shows it
   carries content) — not inputs.
3. **The universal midpoint row is not a three-row object.** `(11907, −334374, −19292)` acts on
   `(P_{n₀}, P_{n₀+1}, P_{n₀+2})`, i.e. three consecutive levels of the *same* row. I verified it
   exactly (§P1 below). No `P̂` enters.

**Why session 5 got it wrong.** The sentence's own logic is invalid: Theorem B's *certification
status* has no bearing on whether the P_n chain *consumes* it. In context, §18.15 is the
certificate agent's session ledger ("What remains, complete list"), which correctly enumerates
**that agent's** obligations — the agent owns both identities. The sentence conflates *the
campaign's open obligations* with *Theorem 1.1's logical hypotheses*.

### (b) But "exactly one input" is still wrong, twice over.

**(i) Theorem 1.1 also consumes (DEPTH), which is `[CERT]`, not `[PROVED]`.**
The paper's own text says so everywhere except in Theorem 1.1:

- Thm 1.3 (`thm:baseintro`): *"Assume (T1-top) for the representative w₅^I **and the
  linear-algebra certificate (DEPTH)**."*
- Thm 1.4 / Cor 7.13 (`cor:51`): *"Assume (T1-top) **and (DEPTH)**."*
- Thm 11.1 (`thm:oneband`): *"PROVED given (T1-top) for w₅^I **and the [CERT] linear-algebra
  certificate**."*
- §14 table line 2704: *"(DEPTH) linear system — `[CERT]`"*; line 2705: *"w₅^I cell-wise
  conditions — `[CERT]`"*.
- §16 table line 2894: *"(DEPTH-gen) — `[PROVED] + [CERT]`"* — **inside Theorem 1.1's own subtree**.

Yet Theorem 1.1 reads *"Assume the decomposition identity (T1-top). Then …"*, §16's root row
reads *"PROVED modulo (T1-top)"*, and Remark 14.6 (`rem:flip`) says a (T1-top) certificate would
make Theorems 1.1, 1.3, 1.4 *"unconditional"* — which is false while (DEPTH) is `[CERT]`. The
chain is: Thm 1.1 ← Thm 1.3 (base case) + Cor 10.6 (step) ← Prop 9.3 ← Cor 7.12 (DEPTH-gen)
← Thm 7.8 `[CERT]` (nonemptiness of the depth-conditioned family) **and** the `[CERT]`
membership of w₅^I.

**(ii) The abstract's "exactly one input that is not proved here" is false for the paper as a
whole.** The same abstract paragraph lists *"the weight-3 companion statement for P̂_n"* among
what is proved. Theorem 1.5 is `PROVED modulo Theorem B`, and Theorem B is `[VERIFIED]`. §16's
table gets this right; the abstract does not.

### The statement the paper should make

> The p ≥ 5 headline law for `P_n` rests on **two** inputs that are not proved here — the
> decomposition identity **(T1-top)** `[VERIFIED]` and the depth certificate **(DEPTH)** `[CERT]`.
> It does **not** rest on Theorem B. Theorem B is a third unproved input, needed only for the
> weight-3 companion (Theorem 1.5).

So session 5's *instinct* ("one is an undercount") was right and its *reason* was wrong. This is
the single most consequential correction in this report, because "one open node" is the paper's
headline framing and appears in the abstract, in §1.3, in §14 and in §16.

---

# P1 — `papers_out/sharp12/sharp12.tex`

**Compile:** clean before and after my notes. 0 errors, 0 undefined references, 0 missing
citations, 42 pages (matches "42 pp"). 8 overfull hboxes, max 19.3 pt — cosmetic. 11 `%% REFEREE`
notes inserted; `diff` against the pre-edit file confirms only comment lines and one neutral line
break were added.

## CRITICAL

**C-1. Proposition 5.12 (`prop:apery-a`, line ~936) is FALSE as stated: the left-hand side is
`b_n`, not `a_n`.**

The displayed identity
`a_n = Σ_k C(n,k)²C(n+k,k)²[H⁽³⁾_n + ½(A₁²B₁ + A₁B₁² + A₁B₂)]`
evaluates to Apéry's **numerator** `b_n`, not to the integer sequence `a_n`.

| n | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| `a_n` (true) | 1 | 5 | 73 | 1445 | 33001 | 819005 |
| RHS of Prop 5.12 | 0 | 6 | 351/4 | 62531/36 | 11424695/288 | 35441662103/36000 |
| `b_n` (true) | 0 | 6 | 351/4 | 62531/36 | 11424695/288 | 35441662103/36000 |

Exact `Fraction` check, n = 0…14: **RHS = b_n at every n; RHS = a_n at no n > 0.** It is also
obvious on inspection that a weight-3 harmonic weight cannot produce an integer sequence.

*Root cause:* the source scripts `work/p1g/zeta3.py` (line 4) and `work/p1g/z3ex.py` (`a_exact`)
name the numerator sequence `a_n`. The transcription inherited the local convention.

*Knock-on:* §1.3's "what is new" list (line 342) promises *"a new harmonic closed form for
Apéry's `b_n` **and for `a_n`**"* — the second object does not exist in the paper. Propositions
5.11 and 5.12 are **two closed forms for the same sequence `b_n`**.

*What is correct:* Prop 5.11 is right (verified against the standard `b_n` for n ≤ 8, and its
proof is internally consistent — the residue derivation gives exactly `β_{1,j} = 2β_{2,j}(2H_j −
H_{n+j} − H_{n−j})`). Prop 5.12's *cell-wise integrality* claim is also right: **819 cells,
0 violations** for p ∈ {5,…,23}, all n < p, all k. So the fix is a one-symbol fix in the
statement plus a rewrite of the "what is new" bullet — but as printed the proposition is false.

*Bonus:* the programme's own `LBW_GENERAL.md` §4 records a **third and much simpler** closed form,
`b_n = Σ_k C(n,k)²C(n+k,n)²(2H⁽³⁾_n − H⁽³⁾_k)`, which I also verified exactly for n ≤ 14. It is
the one that is formalised in Lean (as `bMin`). §5.4 does not mention it.

## MAJOR

**M-1. Theorem 1.1's hypothesis list omits (DEPTH).** See §0(b)(i). Also affects §16's root row
and Remark 14.6. *Evidence-class upgrade: a `[CERT]` node discharged in the headline.*

**M-2. The abstract's "exactly one input that is not proved here."** See §0(b)(ii).

**M-3. Evidence 1.2 (`ev:law12`) does not evidence that the factor 3 is needed.**
The display gives counts for `12·d_n⁵` (361/361), `6·d_n⁵` (1/361) and `d_n⁵` (1/361), then
concludes *"neither 6 nor 2 nor 1 suffices"*. But 1, 2, 3 all divide 6, so the "6" row rules them
out for free — **and says nothing about 4**, the only other maximal proper divisor of 12. Since
`den(P_n) | 4·d_n⁵` failing is exactly the assertion that the 3 is real, and §15 makes the source
of the 3 the paper's headline open question, this is the one row that had to be there.

*Referee recomputation (exact, n ≤ 360):*

| c | 1 | 2 | 3 | **4** | 6 | 12 | 24 |
|---|---|---|---|---|---|---|---|
| #{n : den(P_n) \| c·d_n⁵} | 1 | 1 | 1 | **330** | 1 | **361** | 361 |

`c = 4` fails at 31 values (first: n = 2, 6, 8, 18, 20, 24, 26, 54). The claim is TRUE; the
evidence for its most delicate half is missing. (Everything else in Ev. 1.2 verified exactly,
including the four ratios 0.9953 / 0.9928 / 0.9947 / 0.9936 at n = 80/200/320/355.)

**M-4. Evidence 14.2 (`ev:T1`) — "287 of 687 excess equations satisfied … at N = 600" — misreads
the source shorthand and, as printed, asserts that 400 excess checks FAILED.**
That reading would refute (T1-top). The two numbers come from different equation counts:

- `PHASE2_ENDGAME.md` R2.1 (line 452): *"re-confirmed here at `N = 600` over two primes:
  rank(M) = rank([M|b]) = 313, nullity 135, **287 excess equations satisfied at both primes**"*
  — and 600 − 313 = **287**.
- `PROOF_LB5_CLOSEOUT.md` line 421 (ablation at `N = 1000`): basis 448, rank 313, excess **687**,
  CONSISTENT — and 1000 − 313 = **687**.

The logs' `287/687` denotes the pair, not a ratio. Prop 5.4's *"687 independent excess equations
satisfied"* is correct but should name `N = 1000` (the ablation display two lines later says
`N = 1200`, a third value, which compounds the confusion).

**M-5. Lemma 11.9 (`lem:degen`) — "exactly three occurrences" is FALSE; and the parenthetical
about `p₀` is FALSE.**

*(a) A fourth fully degenerate pair exists: (p, ν) = (29, 27).* Exhaustive check over every prime
dividing the stated resultant gcd (7, 11, 29, 37, 557, p₀) and every root of `a₀` mod p:

| p | ν (root of a₀) | V(ν) ≡ 0? | in above-midpoint range [(p−3)/2, p−4]? |
|---|---|---|---|
| 7 | 2 | **yes** | yes ([2,3]) |
| 7 | 6 | no | — |
| 11 | 5 | no | — |
| 11 | 6 | **yes** | yes ([4,7]) |
| **29** | **27** | **yes** | **NO** ([13,25]) |
| 557 | 49 | no | — |
| p₀ | 416574044722681 | **yes** | yes |

At (29, 27): `a₀(27) ≡ 0 (mod 29)`, and `c₁(26) ≡ c₂(26) ≡ c₃(26) ≡ 0 (mod 29)` (for c₃ because
ν+2 = 29). It is **harmless** — ν = 27 lies outside the range the argument uses — but the lemma
as written carries no range hypothesis and is therefore false. Fix: add `1 ≤ ν ≤ p − 4`, or list
(29, 27) and note it is out of range. (Evidence 11.13 is consistent with the restricted reading:
its "2 fully degenerate" for p < 3000 is exactly (7,2) and (11,6).)

*(b) "`p₀` being the unique prime at which `a₀` has two consecutive roots" is false.*
`Res_ν(a₀(ν), a₀(ν−1)) = −2²·11·37²·557³·p₀`, and **p = 11 has the consecutive pair (5, 6)** —
which is precisely the mechanism behind the listed case (11, 6). (37 and 557 divide the resultant
but have no consecutive pair; 37 has no root at all, 557 has the single root 49.)

**M-6. Theorem 14.4 (`thm:degfit`) is labelled `[PROVED] negative` but is a mod-q rank computation
— exactly what §1.4 defines as `[CERT]`, and exactly what Theorem 7.15 (the same kind of
computation) is correctly labelled.**
Inconsistency over `F_q` does not formally imply inconsistency over ℚ: reduction can lower both
`rank(A)` and `rank([A|b])`, and a rational solution can carry q in a denominator. Two primes make
it overwhelming evidence, not a proof. To earn `[PROVED]`, exhibit the rational annihilator
`y` with `yᵀA = 0`, `yᵀb ≠ 0` and check it over ℚ — a finite, exactly-checkable object. Note also
that the third alphabet (`Y, V, Z`) was run at **one** prime only, as the parenthesis concedes.
The paper leans hard on this ("we record this as a mathematical fact about w₅, not a resource
shortfall"), and §16 lists it as "PROVED negative", so the label matters.

**M-7. §15's general-parameter audit mixes three different cell counts.**
The paper: *"Its evidence is ≈215 audited cells: excess at p = 2 is at most +2 (attained **28**
times), at p = 3 at most +1 (attained **14** times)."* In `CONJECTURE.md`:
- header (line 3–6, **updated**, 164 cells): *"excess₂ ≤ +2 attained **46×**, excess₃ ≤ +1
  attained **30×**"*;
- Evidence section (line 54–57, **103 cells**): *"p = 2: max +2 over all cells (attained **28×**);
  p = 3: max +1 (attained **14×**)"*;
- line 105 (slack-trajectory section): *"~215 cells"*.

The paper pairs the 103-cell attainment counts with the 215-cell total. Quote one consistent pair.

## MODERATE

**Mo-1. §14.5's certification snapshot is one stage behind the current logs — the one-line update
IS needed.**
The paper says the first elimination now returns in seconds *"while the second elimination returns
no telescoper under any support bound so far attempted."* That remains true, and the quoted costs
match the current log **exactly** (`work/lb5/certQ3_kk.stdout`, 06:03–06:20: `obj LeafCount 12489`,
`kk:C ann #3 t=34s`, `kk:C ct1 #2 t=33s`). But `PHASE2_CERTS.md` §18.18 (written 06:15, one minute
after the `.tex`) records that **`R4` `DFiniteTimes` has now also cleared** — `kk:C annL #4 t=500s
mem=0GB`, 4 generators on the largest cofactor in the problem — so **four of the five stages are
clear on every τ and `ct₂` is the sole remaining wall**, with zero returns *by any method,
including unconstrained search with no ansatz box* (`ct₂ FREE t=421s -> none`; and for `n2:A`,
`ct₂ FREE t=600s` plus the whole Support ladder d = 0…4, all `-> none`). That is a materially
sharper and more favourable statement than the one printed.

Two riders: (i) *"for the same object before the split"* is loose — the 12489-leaf `kk:C` is a
*piece* of the 13069-leaf `F_kk` that OOM'd, not the same object; (ii) the paper's *"Theorem B is
a **compute** node, not a structural one"* should acknowledge §18.13, whose direct measurement
(`guessrec`: every single-letter component sum has **no** operator with order ≤ 12 and degree ≤ 30,
while the combination has the unique minimal (3, 9) = L_BZ) means `ct₂` on split pieces has been
searching an empty box — the log's own verdict is *"stop splitting."*

## MINOR

- **m-1.** §16 line 2925: *"the whole chain has exactly two arithmetic inputs"* — Lemma 11.4
  (`lem:Tcorner`) uses **Wilson's theorem** (and Lucas and Kummer), and §12's de-p-adicisation
  remark uses Wilson plus the reflections `H_{p−1−j} ≡ H_j`, `H⁽²⁾_{p−1−j} ≡ −H⁽²⁾_j`. The
  defensible claim is *"exactly two arithmetic inputs that fail at p = 3"* — Wilson holds at every
  prime and so costs nothing. Same wording in the abstract.
- **m-2.** §16 row *"Theorem 1.2 (Lucas, mod p²) — `[PROVED]`, `[LEAN]`"*: the Lean development
  covers only the mod-p statement and its digit-product form (`LEAN_LUCAS_STATUS.md`: `Q_lucas`,
  `Q_lucas_digits`). The mod-p² supercongruence (Cor. 8.7) is **not** formalised. Evidence 3.7
  states this correctly; the summary row does not. Relatedly, Evidence 3.7's *"minimal-Apéry
  (p³b_{ap+r} ≡ b_a a_r)"* — the Lean object is `bMin`, and `bMin = b` is proved on paper
  (`MINIMAL_FORM_PROOF.md` §7), not in Lean (`LEAN_LBWCHI_STATUS.md` line 403).
- **m-3.** The abstract's *"That identity is verified exactly over ℚ, agrees with `P_n` at every
  n ≤ 360"* invites the reading that the ℚ-exact check reaches n = 360. Evidence 14.2: exact over
  ℚ is **n ≤ 34** (`w₅^allp`) / **n ≤ 20** (`w₅^I`); the n ≤ 360 agreement is modulo two 25-bit
  primes. State the ranges in the abstract.
- **m-4.** Definition 5.5's `w₅^I` (207 terms, denominators {2,3}) is the repo's
  `work/p1g/w5_exIII_allp.json`, **not** `work/p1g/w5_I.json` (155 terms, denominators
  **{2, 3, 71}** — i.e. not p-integral at p = 71). Both of the paper's stated numbers are right
  (178 and 207 verified against the files, and `w5_allp` really was produced by `make_allp.py`'s
  CRT), but Appendix A should name the files or a reader will pick up the wrong one.
- **m-5.** Theorem 4.2's *"both sides being p-integral"* is asserted, not shown; p-integrality of
  `p⁵P_n` at n < p² is a consequence of the base case, not free at that point in the exposition.
- **m-6.** (C1) and (C2) are defined inside the *proof body* of Lemma 8.9 (lines 1639–1647) and
  then invoked two sections later at lines 1813 and 1999. They resolve, but they should be a
  displayed lemma.
- **m-7.** Evidence A.1's *"every n < min(p, 361)"* gives 11 955 cells if n = 0 is included; the
  stated **11 884** is the count for `1 ≤ n < min(p,361)`. Write `1 ≤ n`.

## Everything in P1 that I recomputed and found EXACTLY right

This is a long list and it should count in the paper's favour — the arithmetic is, with the
exceptions above, remarkably clean.

- **Normalisation (1.1):** `Q₀,Q₁,Q₂ = 1, 21, 2989`; `P₁ = 87/4`, `P₂ = 1190161/384`;
  `P̂₁ = 101/4`, `P̂₂ = 344923/96` — all match the ladder files. `d₂⁵ = 32`, `384 = 12·32`,
  `gcd(1190161, 384) = 1`.
- **Evidence 1.2** ratios and the 361/1/1 counts (see M-3 for what is missing, not wrong).
- **Evidence A.2 (`ev:sweep`):** 9 primes × 360 = **3240** cells, `min(ord_p P_n + 5L) = 0`
  attained **at p = 5, n = 1** — exactly as printed.
- **Evidence A.1 (`ev:base`):** **11 884** cells over primes 5 ≤ p ≤ 367, 0 failures, minimum
  exactly 0.
- **§15's p ∈ {2,3} law:** `min(v₂(P_n) + 5L₂) = −2` (attained 360×) and
  `min(v₃(P_n) + 5L₃) = −1` (attained 31×), n ≤ 360 — both bounds attained, as claimed.
- **§11 corner arithmetic, in full.** `T/p² ≡ (2, 2, 24) (mod p)` and `v_p(T) = 2` at all three
  corner cells for every prime tested up to 101 (24 mod 5 = 4, mod 7 = 3, mod 11 = 2, mod 13 = 11,
  mod 17 = 7, mod 19 = 5, mod 23 = 1 — all consistent with the single integer 24). The corner sum
  `2(3−s₂/2) + 2(3−s₂/2) + 24(−½−s₂/2) = −14s₂` is correct algebra, and
  `Σ_{j<p} j⁻² ≡ (p−1)p(2p−1)/6 ≡ 0` for p ≥ 5 (and ≡ 2 at p = 3).
- **Evidence 11.8 (`ev:corner`) reproduced independently:** with `w₅^I` = `w5_exIII_allp.json`, at
  **all 32 primes 5 ≤ p ≤ 139**, the three residues `p·T·v₅ mod p` are exactly `(6, 6, −12)` and
  sum to 0 — **0 deviations**. And the Remark's negative control holds: with `w₅^allp`
  (178 terms) the corner combination is non-vanishing at **32 of 32** primes. Lemma 11.5's `K₃`
  values are therefore corroborated end-to-end.
- **Proposition 11.10 (`prop:univrow`), exact.** `2⁹c_i(−5/2) = (333396, −9362472, −540176, 0) =
  28·(11907, −334374, −19292, 0)`; `128c_i(m) − 7R_i` is divisible by `(2m+5)` with integral
  quotient for all four i; `gcd(11907, 334374, 19292) = 1` with the stated factorisations
  `3⁵·7²`, `2·3·23·2423`, `2²·7·13·53`; `8a₀(−5/2) = −241144 = −2³·43·701`. The row is identical
  to `PHASE2_A1_MIDPOINT_THEOREM.md`'s, as claimed.
- **Lemma 11.7 (`lem:APP`), exact.** `c₀(ν−1) = ν⁵(ν+1)a₀(ν)`; all three 2×2 minors have degree 18
  and remainder **exactly 0** on division by `a₀`.
- **Proposition 11.8 (`prop:Ltilde`), exact.** λ's numerator is
  `392627556035671426586ν² + 1282015597875460006266ν + 1052781309790247665282`;
  `D = 3641620092914355321 = 3·7·11·29·543606522303979`; `2D = 7283240185828710642`;
  all five coefficients of `row(ν) − λ·row(ν−1)` are divisible by `a₀`; `deg d₀…d₃ = 8`;
  `d₄ = 2D(ν+3)⁵(2ν+5)`; `d₁` is genuinely a nonzero degree-8 polynomial. So the singular-step
  analysis (only ν = (p−5)/2 in range, excluded primes {2,3,7,11,29,p₀}) is exactly right.
- **Lemma 11.9's resultant gcd, exact:** `2⁶·3³·7³·11·29³·37²·557³·p₀` (see M-5 for the two
  errors that survive alongside it).
- **Evidence 11.13 (`ev:above`), exact:** **428** primes 5 ≤ p < 3000; **296 267** steps above the
  midpoint; **223** exceptional, every one an `a₀`-root.
- **§8 fibre machinery.** The balanced factorial ratio (8.1) is an identity for all n ≤ 13.
  **Lemma Φ** verified: `Σ_s T(r,s,t)Φ_b = 0` and `Σ_t T(r,s,t)Φ_c = 0`, 0 failures for r ≤ 11.
  Corollary 8.7's `Φ_a` expansion is algebraically identical to Lemma 8.5's, and the
  **mod-p² supercongruence** `Q_{ap+r} ≡ Q_a(Q_r + p·a·Ψ_a)` holds on all **296** cells with
  p ∈ {5,7,11,13}, p ∤ Q_a, n ≤ 360 — **0 failures**.
- **Lemma 12.7 (`lem:Phi2`)**: (P0), (P1), (P2), (P3) each exactly 0 on all **120** pairs
  (n, l) with 0 ≤ l ≤ n ≤ 14.
- **§13 middle row.** Theorem 1.5's bound holds with **0 failures** on every cell at
  p ∈ {5,7,11,13,17,19}. The product-form failure counts are **exactly** as printed:
  **3/5/24/55/84/128** failures among the **5/7/33/65/119/152** cells with `v_p(P̂_a) = −1`, and
  **0** among the cells with `P̂_a ∈ ℤ_p`. Proposition 13.5's bounds are attained:
  `min_{n<p²} v_p(P̂_n) = −4` for p ∈ {5,…,23} and `min_{a<p} v_p(P̂_a) = −1` for p ∈ {5,…,31}.
  The "top row has no such defect" control: **0 exceptions** for `v_p(P_a) ≥ 0` and `v_p(W_a) ≥ 0`.
- **§7 linear algebra, every number.** Theorem 7.8: 68 rows / rank(cond) 42 / rank(fit) 313 /
  rank(joint) 324, nullity 124 — matches `PHASE2_RLETTER` §2's control run exactly, and
  448 − 324 = 124, 324 − 313 = 11, 42 − 11 = 31 are all internally consistent. Theorem 7.15's
  three rows match `base`/`vt2`/`strong` exactly (68/42/324; 239/123/342; 149/81/342).
  Theorem 7.16: 1210 coefficients, rank(fit) 313 → 960, dim U 261 → 641, N = 1300, Λ = 262 = 261+1.
- **§11.1.** Theorem 11.1's `rank(cond) = 111`, `rank(joint) = 342`, consistent — versus 123 / 342,
  inconsistent — matches `PHASE2_RLETTER` line 427 (`exIII`: 212 rows, 111, 342, dim U 231, yes)
  and line 140 (`strong`: 239, 123, 342, 219, NO). Evidence 11.2's **10 092** cells (**1 025**
  exempt) and **5 769** cells match verbatim.
- **§14 degree histograms, recomputed from the JSON files.** `w₅^I`: 1:3, 2:19, 3:59, 4:73, 5:53
  — **sums to 207**. `w₅^allp`: 1:2, 2:14, 3:52, 4:66, 5:44 — **sums to 178**. Perfect internal
  consistency with Definition 5.5.
- **§10 sweep counts and the one count discrepancy the writer resolved.**
  **The writer's resolution toward GAPDESC §8 is CORRECT.** Evidence 10.10's *"fails at 134 964"*
  in-regime cells = GAPDESC §8 row 2's **134 289 + 675**; the in-regime total **13 082 671** =
  row 2's 10 281 175 + 2 801 496; the headline **188 353 733** = 142 820 576 + 45 533 157 and
  **944 levels** = 931 + 13; the sharpness count **41 284** matches row 1. Every one of the eight
  table rows matches GAPDESC §8 row for row, including the correct restriction of the L = 3 row to
  **p ≤ 7** (GAPDESC records p = 11 as still running). The off-regime witness p = 13, n = 153,
  (k, l) = (1, 41) is genuinely off-regime (e₃ = 1) with L = 1 and target 0.
- **§5 fitting-system numbers:** 448 monomials, rank 313, 135-dimensional family (448 − 313);
  the caps ablation (3,2,2)/(3,2,5)/(3,5,2) inconsistent, (5,2,2)/(5,5,5) consistent at N = 1200,
  and the three named missing monomials, all verbatim from `PROOF_LB5_CLOSEOUT` §3.4; the alphabet
  ablation at N = 1000 verbatim from its §3.5 table.
- **§15 quotes vs `H2_SIGNS.md`.** The block quote is **character-for-character** the file's §8
  "Net." paragraph. The three sub-results map correctly onto `[PROVEN]` A-side no-go,
  `[PROVEN]` p = 3 discharge, `[NOT CLOSED]` the integral `d₁`; "uncoloured generic facets" is the
  file's own "uncolored generic facets `C`"; the two strata `Z3 = d24∩d36`, `Z6 = d14∩d36` are
  right. The derived consequence — *the geometric route cannot produce a 3* — is faithful to §5's
  `[PROVEN — derived]`. (One looseness: the file's §8 has five bullets, not "three sub-results".)
  The general-parameter conjecture statement matches `CONJECTURE.md` exactly, including the
  extension of ν_p from `p > √(m₁n)` to every prime, and the n = 2 re-audit flipping both partner
  points to slack. Only the 28/14/215 triple is wrong (M-7).
- **Lucas §3.** Lemmas 3.2–3.5 and the proof of Theorem 1.2 are correct as written; the
  non-obvious `s + t < p` step in Lemma 3.4 checks out. `PROVED, LEAN` is faithful to
  `LEAN_LUCAS_STATUS.md`'s axiom list (`propext`, `Classical.choice`, `Quot.sound`; no
  `native_decide`, no `sorryAx`), modulo m-2's scope point.

---

# P2 — `papers_out/lucas2nd/` (38 pp)

**Verdict: ISSUES-FOUND — 0 CRITICAL, 3 MAJOR, 11 MINOR.** Compile clean: 0 errors, 0 undefined
references, 0 overfull hboxes. No mathematics found wrong; every identity, certificate, tally and
numeric value independently checkable was correct. *(Note: `build.sh` produces **39** pages, not
the 38 quoted in the brief — worth pinning down before anyone cites a page count.)*

**MAJOR**
1. `sec-families.tex:227` — **Sequence D listed as `[PROVED]`** under the heading *"hypotheses
   (H1)–(H5) verified, Theorem 4.4 applies"*, but identifying the object Theorem 4.4 controls with
   D's actual second solution requires `(L B) = 0`, which the **same paper** labels
   `\VerifiedR{n ≤ 25}` at `sec-minimal.tex:490`, and whose §6.6 (Prop. 6.22) proves the paper's
   own template **cannot** establish. Evidence-class upgrade, inherited from `LBW_GENERAL.md:304`.
   γ, A and s₁₀ do not have this problem. **D is the unique defective row.**
2. `sec-minimal.tex:415–441, 443–463` — **Theorems 6.19 (Franel) and 6.20 (s₁₀) marked `[PROVED]`
   with no proof written out.** `[PROVED]` is defined at `sec-intro.tex:206` as *"a complete proof
   is written out here."* Thm 6.19 never states the Gosper equations its certificates solve;
   Thm 6.20's certificates `N₁₀`, `M₁₀` are **not in the paper at all** ("full coefficients in the
   certificate file"). What *is* printed was verified and telescopes correctly.
3. `sec-depth.tex:75` — *"E = 5 at the edge (a,r) = (p−1,0)"* under `\VerifiedR{5 ≤ p ≤ 31}` is
   **false at p = 5 (E = 4) and p = 11 (E = 6)**; neither prime has any cell with E = 5. It
   contradicts the paper's own Table 1 **and** the bullet immediately above it. The correction is
   on file — `VERIFY_ZETA3_PROOF.md:87` records `E(edge) ∈ {4,5,6}` — and was dropped in favour of
   the un-corrected `WARMUP_ZETA3_DWORK.md:125`.

**MINOR (11), abbreviated:** Lemma 2.17 states `0 ≤ a < p` but invokes Lemmas 2.14 and 2.16, both
requiring `1 ≤ a < p` (the a = 0 case is true, unused, and one character from repair); its proof
appeals to *proof internals* of Lemma 2.16 and uses Lemma 2.1 uncited; `sec-general.tex:102` drops
the `χ` subscript on `K^{(r)}` (log typo at `LBW_GENERAL.md:271`); `sec-general.tex:97` asserts
`p^w w(n,k) ∈ ℤ_(p)` without the one-line reason; the reflection-symmetry claim at
`sec-depth.tex:70` fails for every `a = p−1` boost; at p = 11 the E = 6 boost is *duplicated*, not
"split"; the abstract writes `χ(p)` where Thm 4.4 gives `χ(p)^e`; the abstract defines χ and w via
an Apéry limit that (by its own §8.2 and by three of the fifteen sequences) does not always exist;
§7.2 applies Thm 4.4 outside its stated `p ≥ 5`; the Franel `p ≥ 5` / `p ≠ 2` mismatch has no
cross-reference; *"all six are instances of [one] absorption identity"* is wrong for four of the
six (hedge dropped from `MINIMAL_FORM_PROOF.md:48–51`); `sec-lean.tex:21` conflates `B_min` with
`b`; `main.tex:68` still has an author placeholder.

**The specific checks requested:**
- **Lemma 2.17 (editorial addition):** *stands on its own.* No forward references, no circularity;
  it cites only Lemmas 2.9, 2.13, 2.14, 2.16, all strictly earlier and none of which uses it; its
  sole use site is Theorem 2.18. Conclusion confirmed numerically (p ∈ {5,7,11,13}, all a, r:
  0 failures). Its valuation ledger is correct. Only the out-of-scope `a = 0` (MINOR-4 above).
- **Theorems 2.11 / 2.18 / 4.4 / 6.1 vs sources:** **no drift.** 2.11 and 2.18 verbatim against
  `WARMUP_ZETA3_DWORK.md:133–137` and `:179–183`; 4.4 **word-for-word** against
  `LBW_GENERAL.md:241–285` including all five hypotheses; 6.1 verbatim against
  `MINIMAL_FORM_PROOF.md:300–312`.
- **Lemma 2.10 (restructured fibre lemma):** *yields both uses.* It quantifies over `a ≥ 0`
  arbitrary and `0 ≤ β ≤ a+1`. Use 1 (Thm 2.11, β = 0) needs `a` unrestricted — a `a < p` version
  would fail. Use 3 (Cor 2.12(i)) takes **β = m₁+1 up to a+1** — which is exactly why the upper
  limit had to be `a+1`. The product-completion argument is correct (the adjoined terms carry
  `C(r,s)² = 0` and vanish identically).
- **25 vs 28 primes:** *the paper's correction is right and the log is wrong.*
  `LBW_GENERAL.md:19` says *"28 primes 5 ≤ p ≤ 103"*; the true count is **25**
  (π(103) = 27, minus 2 and 3). The paper never prints a count and its decomposition
  `15×16 + 15×9` (`sec-depth.tex:171–172`) gives 25. Fix the log.
- **Three §6 certificate identities, symbolic:** **all three verify to exactly 0** in ℚ[n,k]
  (sympy `expand`): CERT-1 (Lemma 6.3, `sec-minimal.tex:72–75`), CERT-2 (Lemma 6.5, `:120–124`,
  both the identity and the bracket factorisation), CERT-3 (Lemma 6.14, `:272–279`, both the
  identity and `W(n,k) = −5k(2n+1)/((n+1−k)(n+k))`). Plus, as a bonus, the Franel and s₁₀
  Zeilberger certificates, every displayed boundary identity, `B_min(n) = b_n` for n ≤ 30, the
  **14 292** branch count, Table 1's tallies, and the Lean spot value `103188530395/32` — all exact.

---

# P3 — `papers_out/padiclimits/padic-apery-limits.tex` (29 pp)

**Verdict: ISSUES-FOUND — 1 CRITICAL, 4 MAJOR, 4 MINOR.** Compile clean: 29 pages, 0 errors,
0 undefined references, 0 undefined citations, **0 overfull/underfull boxes**. Six `%% REFEREE`
comment blocks inserted (lines 125, 593, 715, 772, 1166, 1242); still compiles clean at 29 pages.

*Numbering note for the brief: the item called "Proposition 2.6(iv)" is **Proposition 2.5(iv)** in
the compiled document (`theorem.2.5` in the `.aux`).*

## CRITICAL

**C-1. Proposition 2.5(iv)'s "honest modulus" is not honest enough — it is FALSE inside its own
stated verification range, and refutable from the paper's own appendix table.**

Line 593:
> `\item $\Lambda_a\equiv f(a)\pmod{p^{w}}$; and \VER{$p=5,7,11,13$; $a\le12$} in fact modulo
> $p^{w+v_p(\Lambda_a)}$.`

The `[VERIFIED]` half is a faithful transcription of the source's own false claim
(`LAMBDA_HUNT.md:114` *"the trivial floor is 3, because `Λ_a ≡ f(a) (mod p^{3+v})` holds for
free"*; `PADIC_SEAM.md:122` same). The `[PROVED]` `mod p^w` half is the writer's own addition and
holds only under Theorem 2.4's **p-unit-cell** hypothesis, which the adjacent `\VER` range
silently overrides.

Independent recomputation (own integer recurrence mod p^K), **44 cells**, p ∈ {5,7,11,13}, a ≤ 12,
p ∤ a:

| claim | failures |
|---|---|
| `v_p(Λ_a − f(a)) ≥ w` (the **[PROVED]** half) | **8/44** — p=5: a = 1,3,6,7,8,9,11; p=11: a = 5 |
| `v_p(Λ_a − f(a)) ≥ w + v_p(Λ_a)` (the **[VERIFIED]** half) | **8/44** — p=5: a = 1,3,11; p=7: a = 3; p=11: a = 5; p=13: a = 2,6,10 |

Two distinct mechanisms: the first group has `v_p(a_a) > 0` (Thm 2.4's hypothesis fails); but
**p = 7, a = 3 and p = 13, a = 2, 6, 10 *are* p-unit cells** — there `v_p(Λ) = 1`, the claim
demands `p⁴`, and the true difference-valuation is exactly 3.

*It is refutable without any computation at all, from Table C.2 of the paper itself:* at p = 5 the
table prints `Λ₁ = 5⁻¹(1 1 3 3 4 …)`, while `f(1) = b₁/a₁ = 6/5 = 5⁻¹(1 1 0 0 0 …)`. First
discrepancy at digit 2 ⇒ `v₅(Λ₁ − f(1)) = 1`, which is neither ≥ w = 3 nor ≥ w + v = 2. The
source's own raw log agrees: `work/lambda/logs/t1_p5.log` records `a=1 relagree L:[2, 5, 8, …]` —
first-level agreement **2** relative digits, not 3.

*Knock-on:* §2.4's *"the trivial floor: any ansatz expressing Λ_a through f(a) reproduces w digits
for free"* and Finding 6.8's *"each at exactly the trivial floor of w = 3 digits handed over for
free by Proposition 2.5(iv)"* are not universal.

## MAJOR

**M-1. The abstract's only "we prove" is attached to the one thing that is not proved.**
Line 125: *"We prove `Λ_a = h_p(a) + (blocks)/Ã_a`."* In the body this assembly is **Finding 6.6**,
tagged `\VER{p = 5,7,11,13, block by block}`, and `LAMBDA_HUNT.md:185` labels it
`[VERIFIED order by order]`, never `[PROVED]`. Only `h_p` (Thm 6.1) and `c_p` (Thm 6.3) are proved.

**M-2. Corollary 5.4 carries `\VER` and no `\PROVED`** — the only theorem-class environment in the
paper with that property, in direct violation of its own §1.5 (*"statements labelled theorem,
proposition, lemma, corollary are [proved]"*). Its content — *"There is no route to the
irrationality of any ζ_p(2k+1) … at any prime"* — is also quantified far beyond the evidence
(p ∈ {5,7,11,13}, heights ≲ 10⁴, n ≤ 5000). `PADIC_SEAM.md:398` makes the same unquantified
assertion, but a numbered Corollary is a much stronger speech act than a bolded log sentence.

**M-3. Finding 3.5's universal quantifier was added on transcription, and is false.**
*"`v_p(p^{3s}f(n_s))` is constant in s for **every** tower and equals `v_p(b_a/a_a)`"* — recomputed
at **p = 5, a = 11**: `v_p(L_s) = −4, −2, −2, −2, −2` while `v_p(b₁₁/a₁₁) = −4`. The source's own
logs already show it (`hunt_p5.txt`: *"a=11 v(L)=-2"*; `t1_p5.log`: *"a=11 … relagree
L:[0, 2, 5, …]"* — the leading 0 is the valuation jump). `PADIC_SEAM` T1.2, whence the sentence,
tested only a = 1,2 (p=5), a = 1,3 (p=7), a = 1 (p=11,13). In the same sentence *"flat … in the
descent branch"* is contradicted by **Table 3.6 two lines below**: row "7, branch r = 1" reads
4, 6, 9, 13, 15 → increments 4, **2**, 3, 4, **2**.

**M-4. The rate-law exceptions list is incomplete: family F is missing.**
Finding 3.3 (line 715) lists *"(ε), (ζ), C, s₁₈"*, faithfully transcribing `LAMBDA_HUNT.md:291`.
Recomputed sweep (15 families × p ∈ {5,7,11}, N = 20 000, a = 1, with the χ(p)^s twist):

```
p=5   C   cumulative 4, 5, 7, 9, 11, 13   (predicted 2,4,6,8,10,12)
p=5   F   cumulative 4, 5, 7, 9, 11, 13   <-- IDENTICAL to C, NOT LISTED
p=5   s18 cumulative 4, 5, 7, 9, 11, 13
p=5   B   cumulative 2, 4, 6, 8, 10, 12   (on the nose)
```

**F deviates at p = 5 in exactly the same way and by exactly the same amount as C and s₁₈.**
Either all three are listed or none. The recomputed exceptional set is **{ε, ζ, C, F, s₁₈}**. The
omission is inherited from the source, not a transcription slip. Sub-point: *"**upward**
deviations"* is true only cumulatively — at p = 5 the level-2 increment for C, F, s₁₈ is **1**
(below the predicted 2), and at p = 7 the ε increments are 4, 5, **2**, 3, 3. Everything else in
the sweep reproduces `min(3, r(χ,w))` exactly.

## MINOR

- Theorem 6.3's `\VER{12 pairs × p ∈ {5,7,11} at K = 12 digits, all digits matching}` overstates
  one cell per prime: `t7_kaz.py:121` drops K to 6 when `a·p⁵ ≥ 4e6`, and `kaz_p11.txt` shows
  `c_p(121,11) … MATCH(all 6)`. (The *claim* is true — I checked (p²,p) to 15/12/10 digits — but
  the printed range is not what the logged run did.)
- Table 6.7 (`tab:blocks`): the raw log `work/lambda/logs/struct_p5.txt` prints *"discrepancy at
  v_p = 4 (**expect 5**)"* for the last row, i.e. a **miss** against the script's own prediction;
  `LAMBDA_HUNT.md:203` relaxed the prediction to "≥ 4" and the paper inherits the relaxed column
  together with *"Every predicted block is confirmed"*.
- Finding 7.1's `\VER{p = 5,7,11}` asserts p-adic tower limits for B, (δ), (η) at p = 5, while
  Finding 7.2 says (η) degenerates entirely at p = 5 (χ₅(5) = 0). Internal tension.
- §1.3(E) calls `T` *"a finite Γ_p-product over the base-p **digits**"* — it is a product over the
  base-p **truncations** `⌊A/p^l⌋`; and the abstract drops the leading `−1` of (6.3).

## Cleared

**The χ(p)^k tree law (the first of the writer's two corrections) is CORRECT and the correction
was necessary.** `PADIC_SEAM.md:100` has only the untwisted `Λ_{p^k a} = p^{−3k}Λ_a`; the
χ-twisted definition is `LAMBDA_HUNT.md:54`. The writer generalised, correctly. Numerics at
**p = 5**, family **C** (w = 2, χ₋₃(5) = −1, so the factor is not vacuous):

```
Lambda_5           = 5^-2 * (3 1 3 1 4 0 0 2 3 0 …)
chi(5)*5^-2*Lambda_1 = 5^-2 * (3 1 3 1 4 0 0 2 3 0 …)   -> 70/70 digits MATCH
5^-2*Lambda_1 (no chi)                                   -> 0 digits, DIFFER
```

Control at trivial χ (Apéry γ, p = 5): `Λ₅ = 5⁻³Λ₁`, 69/69 digits — reproduces
`PADIC_SEAM:100`. The proof's `χ(p)⁻ᵏ = χ(p)ᵏ` step (quadratic or trivial character at an
unramified prime) is right, and the χ(p) = 0 case is exactly Finding 7.2's ramified degeneration.

**Theorem 6.3 (the closed form) is CLEAN — character-for-character against `LAMBDA_HUNT.md:29`
and `work/lambda/t7_kaz.py`.** Leading `−`, `p^{v_p C(A,B)}`, `T(A,B)`, the
`Γ_p(A+1)/(Γ_p(B+1)Γ_p(D+1))` ratio, and
`Z = −Σ_{m≥3 odd} ζ_p(m)(Aᵐ−Bᵐ−Dᵐ)pᵐ/(m(1−pᵐ))` all identical; the paper *adds* the explicit
`T(A,B)` product (matching `t7_kaz.py:89–92`) and the correct side-condition `= 1 when A < p`.
Re-derived from scratch with an independent Kubota–Leopoldt series, an independent Γ_p and an
independent direct binomial limit — nothing imported from `work/`: **36 (pair, prime) cells,
zero mismatches**, to 15 digits (p=5), 12 (p=7), 10 (p=11), including carry cases, `p | A`, and
`v_p(c_p) = 1`; ζ_p(3) digits reproduce Table C.1 exactly at all four primes; Corollary 6.4
reproduces the logged `c_p(2,1)` digits exactly; Remark 6.5's "4–5 correct digits" is exact
(4 at p=5, 5 at p=7,11,13). Where the source is self-inconsistent (`LAMBDA_HUNT.md:347` "2 primes"
vs `:175` "3 primes"), **the writer picked the correct one.**

**All fourteen data tables** (`tab:constants`, `ingredients`, `zetadigits`, `precision`,
`aperyrate`, `bzrate`, `strata`, `lll1`, `lll2`, `ansatz`, `familyrates`, `blocks`, `ledger`,
`margins`) are character-for-character matches of `PADIC_SEAM` T1.2/T2.2/T2.3/T3.1/T3.2/T3.4/T4.2
and `LAMBDA_HUNT` T1–T4. Additional independent confirmations: Λ₁ digits at all four primes;
`(LB₃)` for the Apéry pair over 9 primes 5 ≤ p ≤ 31, n ≤ 320, floor exactly 3; the Casoratian
`a_{n+1}b_n − a_n b_{n+1} = −6/(n+1)³` exact for n ≤ 59; `v_p(ζ_p(3)) = 0`, `v_p(ζ_p(5)) = −1` at
p = 5 else 0; the §7 discriminants (B: −27, δ: −128, η: −16) and the real-distinct-roots claim for
all fifteen. Table 3.1's harmonic rates and Finding 3.4 (Kazandzidis, exactly 3 digits/level)
verified exactly, and every χ(p) in Table 3.2 independently correct.

---

# P4 — `papers_out/frobenius/frobenius.tex` (25 pp)

**Verdict: ISSUES-FOUND — 2 CRITICAL, 3 MAJOR, 11 MINOR.** Compile clean: 25 pages, 0 errors,
0 undefined references, 0 undefined citations. Five `%% REFEREE` comments inserted; output
identical.

**CRITICAL**
1. **The `[VERIFIED] → [PROVED]` upgrade of Corollary 5.2 is UNSOUND.**
   - *Original evidence class:* `GAMMA_UNIFICATION.md` §2.3 is headed
     ``### 2.3 The κ-vector `[VERIFIED 434 digits]` `` and line 224 records the provenance as
     **PSLQ** (`tol = 1e−380`, `|c| ≤ 10¹⁴`). `λ₅ = (514/87)ζ(5)` sits in the λ column, i.e. it was
     itself read off by integer-relation detection. **There is no derivation anywhere in the log.**
   - *The licensing hypothesis is NOT stated.* The phrase *"given the identifications"* **does not
     occur anywhere in the paper.** The licence exists only as the parenthetical `(from Theorem
     5.1.)` glued to the `\PROVED` marker and a sentence inside the proof. The corollary's
     statement is unconditional and **boxed**.
   - *The proof's algebra is correct* (`λ₄ = κ₄ − κ₂²/2`, `λ₅ = κ₅ − κ₂κ₃` from the log-expansion;
     the substitution closes), **but its inputs are `[VERIFIED]`** — Theorem 5.1 is
     `\VER{434 digits}`, and it in turn runs under Observation 4.4, an *empirical licence* that the
     paper itself shows BV Lemma 24's hypothesis (i) fails. A `[PROVED]` conclusion from
     `[VERIFIED]` premises directly violates the paper's own §1.4 (line 297:
     *"Numerical agreement is never presented as proof."*).
   - *Same defect at four more sites:* Obs. 5.3 (824), Obs. 6.2 (918, upgraded from the log's
     `[VERIFIED 200 digits]`), Obs. 6.4 (945), and — worst — the **abstract** (92–96) and
     **Results (3)** (246–252, *"whence λ₅ = 514/87 ζ(5) exactly"*) state the closed forms with
     **no evidence marker at all**.
   - *Independent re-verification (mp.dps = 500, from `work/gamma/kappas_hi.json`):* the identity
     **is true** — `λ₅ − (514/87)ζ(5) = 2.34e−419`, at the archive's precision floor. **The
     mathematics is right; the label is wrong.** (Side finding: the paper's quoted residuals of
     `10⁻⁴⁴⁰`–`10⁻⁴⁵¹` are **not reproducible from the archived data** — `t3e_high.py:88` writes
     the JSON at `nstr(x, 420)`, capping any recheck at ~1e−419.)
   - *Minimal fix:* `\PROVED (the relation λ₅ = κ₅ − κ₂κ₃); \VER{434 digits} (the closed forms)`,
     and open the statement with *"Assume the identifications of Theorem 5.1."*
2. **Observation 5.6 (line 880) is FALSE and marked `\VER{j ≤ 9}`.** The claimed
   *"weight-(j−3) coefficient of λ_j = −3 × weight-(j−4) coefficient of λ_{j−1}"* is refuted by
   **Proposition 5.5 printed immediately above it**: exact ratios are −3 at j = 7 but
   **−3365/294 at j = 8** and **−3660/4711 at j = 9**. The true pattern is at *fixed* weights 3→4
   (exactly −3 for j = 7,8,9), not on the moving top off-diagonal. Inherited from
   `GAMMA_UNIFICATION.md:250` and **repeated at line 1654**. (The rest of Obs. 5.6 — weight support,
   absences, {3,5,7,11,29}-smoothness of all 14 denominators — is correct.)

**MAJOR**
3. **(RPC-4) is a tautology** (line 1147, Table 6, (F2) at 1226). For *any* log-series the
   depth-≤2 part of `[ε^m]exp(Σ λ_j ε^j)` has exactly `1 + #{(a,b): 2 ≤ a ≤ b, a+b = m} = ⌊m/2⌋`
   monomials — always. So "(RPC-4)" **is** (RPC-1). Table 6's last two columns are its first two
   re-expressed, falsification route **(F2) cannot fire unless (F1) fires**, and the weight-9
   "concrete open prediction" is a formal identity.
4. **Γ-exclusion overstated** — abstract (100), Results (269) and Obs. 7.5 (1353, which carries
   **no evidence marker**) say *"all Γ(r/s), s > 2, excluded"*; only `s ∈ {3,4,5,6,8,12,24}` was
   searched, and the log keeps the restriction.
5. **Abstract (103–105) and Results (7) drop Theorem 8.1's standing hypothesis** `s, P̂ ∈ Sol(L)`,
   which Thm 8.1 states scrupulously and §9.3 declares **not proved**.

**The specific checks requested:**
- **Corrected leverage arithmetic (0.6773 vs 4.6349): the PAPER IS RIGHT; the LOG was wrong.**
  The two numbers are **not competitors** — they are the two sides of one comparison, both correct
  and both in the paper: **nats needed** `= κ − (−C₀) = 7 − 2.36512689845 = 4.63487`, **nats
  bought** `= (−C₀)(1.286364711 − 1) = 0.677289`, ratio **6.843**, which is forced (it equals
  195.968 % / 28.636 % identically). The number that was *replaced* is the source log's:
  `LTILDE_HUNT.md:211–213` says *"1.03 nats (`5·(0.636−0.494)`)"*, and **1.03 is wrong under every
  reading**, including its own — the parenthetical formula gives 0.708, the κ = 7 additive reading
  gives 0.9912, the multiplicative reading actually used gives 0.6773. The paper silently
  corrected it. *(MINOR rider: "6.84 ≈ seven times" is normalisation-dependent — on the paper's
  other measure `γ^worth` it is 3.68×. The conclusion survives either way.)*
- **The errata vs `GAMMA_UNIFICATION.md`: faithful, and if anything under-stated.** Erratum 1
  (Obs. 3.2 vs log lines 159–163) and Erratum 2 (Obs. 3.3 vs 165–168) match **character for
  character**, and both were re-verified independently at dps 250 (`(7/3)` form: residual 0;
  the printed `(7/5)` form off by 0.9678. `+` form: residual −1.4e−250; the printed `−` form off
  by 7.2247). The paper **narrows** scope rather than widening it ("the erratum concerns the
  coefficient of ζ(5) only") and softens the log's rhetoric to *"it is evidence and not proof."*
  No overstatement. (One slip: Table 2 says *"the **two** exceptions"* on the Apéry-ζ(2) row; only
  one belongs there.)

**MINOR (11), abbreviated:** line 1314 *"the four π-powers −5/2, +5/2, +5/2, +1/2 multiply to
π^{5/2}"* is false (= π³); Trap 2 says the weight-7 κ-values are *"not quoted anywhere in this
paper"* three lines after quoting two of them; Table 2's "two exceptions"; four `\VER{…}` markers
violate the paper's own `\VER{d digits}` convention; `\EXCL` polarity is inconsistent between
lines 877/925/1276/1284 and 905; Table 5 prints the middle eigenvalue without its minus sign;
line 1073 calls 1.226963 *"exactly"* the 441-digit certificate's slope of 1.22701 (they agree to
4 digits); `\ldots` is appended to **rounded** final digits in Theorem 5.1 and Table 9; the
`10⁻⁴⁴⁰`–`10⁻⁴⁵¹` residuals are not reproducible from the archive; uncited bibitem `Zu02`;
`\small` invalid in math mode at line 750.

**Where P4 is above reproach:** all 8 printed κ digit strings match `kappas_hi.json` to the last
digit; all 4 connection constants match `conn.json`; every closed form verified numerically at
dps 250; Propositions 4.1 and 4.2 verified **symbolically** from `bzop.py` (including
`Disc = 2⁴·37³·557²` and `41218 = 2·37·557`); Theorems 7.3/7.4 verified from `conn.json`
(`A_Q A_{I'} A_I` vs `−π^{5/2}/(12√37)`, relative difference 1.10e−260 against the paper's
1.1e−260); Table 1's truncation model reproduced; and the paper **silently fixed two log errors**
(`16.86407 → 16.86411`, `1.22701 → 1.226963`).

---

# GLOBAL PATTERNS ACROSS THE FOUR DRAFTS

1. **Evidence-class drift is the dominant failure mode, and it is systematic.** Every one of the
   four papers has at least one `[VERIFIED]`/`[CERT]` presented as proved: P1's Theorem 1.1
   hypothesis list and Theorem 14.4; P2's sequence D and Theorems 6.19/6.20; P3's abstract "we
   prove" and Corollary 5.4; P4's Corollary 5.2 and its four companions. In almost every case the
   *mathematics* survives and it is the *label* that fails. All four papers define a scrupulous
   evidence convention in §1 and then violate it — which is worse than not having one, because a
   reader who trusts the convention is misled precisely where the paper is weakest.
2. **Abstracts are consistently one notch stronger than bodies.** P1's "exactly one input";
   P2's `χ(p)` for `χ(p)^e` and its Apéry-limit definition; P3's single "we prove", attached to the
   one assembly that is `[VERIFIED]` only; P4's unmarked closed forms and dropped
   `s, P̂ ∈ Sol(L)`. In every case the body or the summary table is correct. The abstract is
   written last and audited least — audit it separately and last.
3. **Universal quantifiers get added on transcription.** P3's Finding 3.5 ("for **every** tower",
   from a source that tested five cells, refuted at p = 5, a = 11), P3's Corollary 5.4 ("at **any**
   prime", from four), P4's Γ-exclusion ("**all** Γ(r/s)", from seven values of s), P1's Lemma 11.9
   ("**exactly three** occurrences", when there are four). This is the second-largest class after
   evidence drift and the easiest to grep for: every `every`/`any`/`all`/`exactly n` in a
   transcribed statement should be checked against the range the source actually swept.
4. **Two errors are naming conventions inherited from throwaway scripts.** P1's Prop 5.12
   (`zeta3.py` calls `b_n` "a_n") and P2's `sec-general.tex:102` (`K^{(r)}` missing its `χ`). Both
   are one-symbol fixes and both are, as printed, false statements. A grep of every paper symbol
   against the script that produced it would be worth the hour.
5. **Three papers inherited a false claim verbatim from a log that had already contradicted
   itself elsewhere.** P3's Prop 2.5(iv) is refutable from the paper's *own appendix table* and
   from the source's *own raw log*; P2's E = 5 edge claim is contradicted by the paper's own
   Table 1 and by a correction sitting in `VERIFY_ZETA3_PROOF.md`; P4's Obs. 5.6 is refuted by the
   proposition printed immediately above it. The common failure is that logs were read
   section-by-section rather than cross-checked against their own tables. Conversely, where a log
   was simply *wrong* and self-consistent, the writers usually caught it (P4's 1.03 nats, silently
   and correctly fixed; P2's 28 primes; P3 picking the right one of two contradictory ranges). **On
   balance the papers are more reliable than the logs they came from** — the residual errors are
   concentrated where a log contradicts itself and the writer read only one side.
6. **The arithmetic is excellent.** Across roughly 60 independent recomputations in P1 alone —
   sweep counts to the cell, resultants to 38 digits, degree histograms, the entire midpoint-row
   and desingularisation apparatus — I found **one** wrong number (Prop 5.12's left-hand side) and
   **one** wrong enumeration (Lemma 11.9). Across all four papers, essentially every certificate,
   digit string, tally and closed form that could be recomputed was exactly right. The defects are
   overwhelmingly in *what the sentences claim about* the numbers, not in the numbers.

## Recommended order of repair before circulation

1. **P1 Prop 5.12** (one symbol) and **P1 §1.3's "and for a_n"** — a false displayed identity.
2. **P3 Prop 2.5(iv)** — false over its own range; restore Thm 2.4's p-unit hypothesis to the
   `[PROVED]` half and replace the `[VERIFIED]` half with what the sweep actually shows.
3. **P4 Cor 5.2** (+ Obs. 5.3/6.2/6.4, abstract, Results) — relabel, and state the hypothesis
   inside the corollary.
4. **P4 Obs. 5.6** — false at j = 8, 9 on the paper's own data; replace with the fixed-weight law.
5. **P1's dependency framing** — abstract, Thm 1.1, §16 root row, Remark 14.6: two inputs, not one,
   and not the two session 5 named.
6. **P1 ev:T1's "287 of 687"** — as printed it reads as 400 failed checks.
7. Everything else is MAJOR-or-below and can be fixed in one editing pass.
