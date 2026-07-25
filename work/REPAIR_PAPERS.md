# REPAIR_PAPERS — applying REFEREE_PAPERS to the four drafts (task W7)

**Date:** 2026-07-25 · **Authority:** `work/REFEREE_PAPERS.md` (4 CRITICAL, 17 MAJOR, ~33 MINOR;
22 `%% REFEREE` blocks in the `.tex` files). Every fix verified against the primary source before
the edit; every numerical finding recomputed independently. `%% REFEREE` blocks are deleted only
when their finding is resolved, and replaced by a one-line `%% FIXED` note.

*(Status: in progress — final ledger below.)*

---

## OPS ACKNOWLEDGEMENT (memory)

Both OOM kills of `p3_rate.py` (~07:09, ~40 s apart, both at ~6.4 GB) were **mine**, and both
were the **identical first, unchunked version** of the P3 rate-law sweep: it stored the full
`{n: (U^A_n, U^B_n)}` table for `n ≤ p^6` with a modulus of `p^(k·v_p(N!)+60)` (≈ 4–6 kB per
entry × 2 × 15 625 entries × 15 families). There was **no auto-retry harness**; the second launch
was my own manual relaunch, made before the first kill had been diagnosed. That was the error.

Resolution, already in place before this message arrived:

- The sweep was **rewritten to retain only the requested tower levels** (`n = a·p^s`) instead of
  the whole table — the modulus size is unchanged but peak RSS drops to a few hundred MB. It then
  **completed successfully** at `p = 5` (`s ≤ 6`) and `p = 7` (`s ≤ 5`), and those completed runs
  are the evidence behind the P3 M-4 fix. Nothing is pending and nothing will be relaunched.
- `pgrep` confirms no `p3_rate.py` or other repair-agent Python process is alive.
- All remaining recomputations in this task are small (exact `Fraction` recurrences to
  `n ≤ 2030`, sympy resultants on a cubic, `mpmath` at `dps ≤ 500`); each is launched under
  `ulimit -v 3000000` (3 GB) so that it aborts cleanly rather than being killed.

No finding had to be verified at reduced range: the P3 CRITICAL (Prop 2.5(iv)) needs only
`n ≤ a·p² ≤ 2028` in exact rational arithmetic and never exceeded a few hundred MB — it was
**not** the computation that OOM'd.

---

## 0. Summary

| paper | REFEREE blocks | findings applied | compile |
|---|---|---|---|
| P1 `sharp12` | 11 → 0 | 1 CRITICAL, 7 MAJOR, 1 MODERATE, 7 MINOR | 44 pp, 0 err, 0 undef |
| P2 `lucas2nd` | (none) | 3 MAJOR, 11+ MINOR | 39 pp, 0 err, 0 undef |
| P3 `padiclimits` | 6 → 0 | 1 CRITICAL, 4 MAJOR, 4 MINOR | 31 pp, 0 err, 0 undef |
| P4 `frobenius` | 5 → 0 | 2 CRITICAL, 3 MAJOR, 12 MINOR | 26 pp, 0 err, 0 undef |

All 22 `%% REFEREE` blocks converted to one-line `%% FIXED` notes. **Zero evidence-class
upgrades.** Every class change made in this pass is a downgrade or an added hypothesis:
P1 Thm 14.4 `[PROVED]`→`[CERT]`; P1 Thm 1.1, 1.4, base case gain `(DEPTH)`; P2 seq. D and
Thms 6.19/6.20 qualified; P3 Cor 5.4 demoted to a Finding and Prop 2.5(iv) restricted to
`p`-unit cells with its strengthening deleted; P3 abstract "we prove"→"we exhibit and verify";
P4 Cor 5.2, Obs 5.3/6.2/6.4 split `\PROVED`/`\VER` and given the licensing hypothesis;
P4 Obs 7.5 given an `\EXCL` marker it lacked; P4 (RPC-4) stripped of its tautological half.

## 1. P1 `sharp12` — ledger

| finding | action | verification |
|---|---|---|
| **C-1** Prop 5.12 LHS is `b_n` not `a_n` | LHS changed to `b_n`; new Remark says 5.11 and 5.12 are two forms for the *same* sequence, and that `a_n` needs no harmonic weight; §1.3 bullet rewritten; §5.4 heading retitled; Evidence 5.13 gains the `n ≤ 14` check | exact `Fraction`, `n = 0..14`: RHS `= b_n` at **every** n, `= a_n` at **no** n (not even 0). n=2: 351/4 vs 73. `a_n,b_n` regenerated from the order-2 Apéry recurrence, independent of both sum forms |
| **M-1** Thm 1.1 omits (DEPTH) | (DEPTH) added to Thm 1.1's hypotheses, given its own bullet with class `[CERT]`; §16 root rows now "modulo (T1-top) + (DEPTH)"; new `(DEPTH)` row in §16; Remark 14.6 rewritten (a (T1-top) certificate leaves (DEPTH) standing); §5's "the one hypothesis" → "the first of the two" | paper's own Thm 1.3 / Thm 1.4 / Thm 11.1 / §14 / §16 subtree all already carry (DEPTH); no recomputation needed |
| **M-2** abstract "exactly one input" | rewritten: **two** inputs for Thm 1.1, with ranges; the weight-3 companion is now explicitly *modulo Theorem B*, named as a third input **not** used by the `P_n` law. New paragraph in §1.3 states the adjudication (Thm B cited nowhere in §§3–11) | citation trace re-run: `\ref{thm:B}`/`\wthree` absent from §§3–11 |
| **M-3** Ev 1.2 lacks the `c=4` row | display replaced by the full `c ∈ {1,2,3,4,6,12,24}` table; prose now separates the two failure modes | recomputed from `ladder_P.json` **and** independently regenerated from `L_BZ` (0 mismatches, n ≤ 360): `1,1,1,330,1,361,361`; `c=4` fails at 31 values, first `2,6,8,18,20,24,26,54` |
| **M-4** "287 of 687" | rewritten as two complete successes: **all** 287 at `N=600` (600−313) and **all** 687 at `N=1000` (1000−313); Prop 5.4 now names `N=1000` | `PHASE2_ENDGAME` R2.1 and `PROOF_LB5_CLOSEOUT`:421,483 |
| **M-5** Lemma 11.9 | hypothesis `p≥5, 1 ≤ ν ≤ p−4` added; new Remark lists the out-of-range **(29,27)** and replaces the false `p₀`-uniqueness with the correct **two** primes (11 and `p₀`) | sympy: gcd of the three resultants `= 2⁶·3³·7³·11·29³·37²·557³·p₀` (matches print); root-by-root over `2,3,7,11,29,37,557,p₀` → degenerate at `(7,2),(11,6),(29,27),(p₀,·)` and `(2,1),(3,1)`; `Res(a₀(ν),a₀(ν−1)) = −2²·11·37²·557³·p₀`; consecutive roots only at `11` (5,6) and `p₀` |
| **M-6** Thm 14.4 `[PROVED]` | → `[CERT] negative`, in the theorem and in §16; new Remark states what would earn `[PROVED]` (a rational annihilator over ℚ) and that the third alphabet ran at one prime | the paper's own §1.4 definition of `[CERT]`; Thm 7.15 is the same computation, already `[CERT]` |
| **M-7** §15's 28/14/215 | replaced by the single consistent pair from `CONJECTURE.md`'s updated header: **164 cells, 46× / 30×** | `CONJECTURE.md` lines 3–6 vs 54–57 vs 105 |
| **Mo-1** §14.5 snapshot | rewritten to the 06:15 state: five stages named, **four clear on every τ**, `R4 DFiniteTimes` 500 s / 4 generators / 0 GB, `ct₂` the sole wall with zero returns under a `d=0..5` ladder *and* unconstrained search (421 s, 600 s); new paragraph acknowledges §18.13's `guessrec` measurement; the loose "same object before the split" corrected to 12489-leaf *piece* of the 13069-leaf object | `work/lb5/certQ3_kk.stdout` (12489 leaves, ann 34 s, ct₁ 33 s, gb 2 s, annL 500 s, `ct₂ FREE 421s -> none`); `PHASE2_CERTS` §§18.13, 18.18, 18.19 |
| m-1 "two arithmetic inputs" | → "two ... that constrain the prime", with Lucas/Kummer/Wilson named as free; same in the abstract | Lemma 11.4 and §12 do use Wilson |
| m-2 §16 Lean row | split into a mod-`p` `[LEAN]` row and a mod-`p²` "not formalised" row; Evidence 3.7 now states the `b_min` vs `b` gap | `LEAN_LUCAS_STATUS.md`, `LEAN_LBWCHI_STATUS.md`:403 |
| m-3 abstract ranges | exact-over-ℚ `n≤34` / `n≤20` and "modulo two 25-bit primes" now in the abstract | Evidence 14.2 |
| m-4 representative files | Def 5.5 now names `w5_allp.json` (178) and `w5_exIII_allp.json` (207), and warns off the 155-term `w5_exIII/w5_I` | read all four JSONs: 178/{2,3}, 207/{2,3}, 155/{2,3,**71**} |
| m-5 "both sides being p-integral" | statement now asserts only that the **difference** lies in `pZ_p`; new Remark shows that is unconditional and says where the individual integrality actually comes from | `v_p(H^{(m)}_N) ≥ −m⌊log_p N⌋` |
| m-6 (C1),(C2) buried in a proof | promoted to displayed **Lemma 7.6 (carry inequalities)** with its own proof; the three invocation sites now cite it | — |
| m-7 Evidence A.1 | range now `1 ≤ n < min(p,361)` | `Σ min(p,361) = 11955`; `Σ (min(p,361)−1) = 11884` over the 71 primes 5..367 |

## 2. P2 `lucas2nd` — ledger

| finding | action | verification |
|---|---|---|
| **MAJOR-1** Sequence D `[PROVED]` | D row daggered; new footnote: `[PROVED]` for the explicit sum `B`, `[VERIFIED]` for the ζ(2)-Apéry second solution, because `(LB)=0` is `\VerifiedR{n≤25}` and Prop 6.22 shows the template cannot supply it. γ, A, s₁₀ explicitly exempted | `sec-minimal.tex:490`; Prop `prop:obstruction` |
| **MAJOR-2** Thms 6.19/6.20 `[PROVED]` with no proof | both relabelled "`[PROVED]` modulo the certificate check described below"; new Remark 6.21 states exactly what is delegated (the Gosper key equations; `N₁₀`,`M₁₀` live only in the certificate file) and cites the §1.2 definition of `[PROVED]` | `sec-intro.tex:206` |
| **MAJOR-3** "E = 5 at the edge" | replaced by `E ∈ {4,5,6}`, with the per-prime list; the p=11 "split" corrected to a *second* E=6 cell | **recomputed exactly** (Apéry recurrence to n=965, `Fraction`): `E(p−1,0) = 4,5,6,5,5,5,5,5,5` at `p=5..31`, `E(p−1,p−1)=6` always; full Table 1 tallies reproduced row for row |
| MINOR Lemma 2.17 range | `0 ≤ a < p` → `1 ≤ a < p` | Lemmas 2.14/2.16 both require `1 ≤ a` |
| MINOR Lemma 2.1 uncited | `\ref{lem:interchange}` cited twice in the proof | — |
| MINOR proof-internals appeal | the needed statement from Lemma 2.16's proof now spelled out in situ | — |
| MINOR `K^{(r)}` missing χ | `K^{(r)}_\chi` in `(eq:LB-letter)` | `LBW_GENERAL.md:271` log typo |
| MINOR `p^w w ∈ Z_(p)` unjustified | one-line reason inserted (Lemma 2.9 valuation + (H4)) | — |
| MINOR reflection symmetry | now stated for the interior boosts only, with the reason the `a=p−1` boosts are outside its range | `(p−1,r) ↦ (0,·)` leaves `1 ≤ a < p` |
| MINOR p=11 "split" | corrected to "duplicated" | tally `6:2` at p=11 |
| MINOR abstract `χ(p)` | → `χ(p)^e` | Thm 4.4 |
| MINOR abstract Apéry-limit definition | `w` redefined as the harmonic weight's total degree; χ/limit attribution restricted to the twelve families that have one | §8.2; three families have no limit |
| MINOR §7.2 outside `p ≥ 5` | now says the **proof**, not the theorem, extends, and says why | Thm 4.4 is stated for `p≥5` |
| MINOR Franel `p≥5`/`p≠2` | cross-reference to §5 added | — |
| MINOR "all six are absorption instances" | corrected: two are absorption, four are the companion `C(N+1,j)(N+1−j)=C(N,j)(N+1)` | companion identity verified for all `N≤13`, `j≤N+1`; hedge restored from `MINIMAL_FORM_PROOF.md:48–51` |
| MINOR `sec-lean.tex:21` | row now names `B_min`, not Theorem 2.18 | `LEAN_LBWCHI_STATUS.md:403` |
| MINOR author placeholder | `\author{AUTHORS TBD (River + collaboration)}` → `\author{}` + comment, as in the companion drafts | it was being typeset |

## 3. P3 `padiclimits` — ledger

| finding | action | verification |
|---|---|---|
| **C-1** Prop 2.5(iv) false in its own `\VER` range | the `mod p^{w+v_p(Λ_a)}` strengthening **deleted**; the surviving `mod p^w` half now carries the `p`-unit-cell hypothesis explicitly; new Remark 2.6 gives the whole sweep and the Table C.2 one-line refutation; §2.4's "trivial floor" and Finding 6.8 both qualified to the `p`-unit cells | **recomputed from scratch** (exact `Fraction` Apéry recurrence, `s=0,1,2`, 44 cells): all **36** `p`-unit cells satisfy `v ≥ w=3`, distribution `26/7/2/1` at `v=3/4/5/6`; **8** non-unit cells fail (`p=5: a=1,3,6,7,8,9,11`; `p=11: a=5`) — exactly the cells with `v_p(a_a)>0`; the strengthening fails at **4** `p`-unit cells (`(7,3),(13,2),(13,6),(13,10)`, each `v(Λ)=1`, true valuation exactly 3); `v₅(Λ₁−f(1)) = 1` |
| **M-1** abstract "we prove" | → "we exhibit, and verify block by block"; the two things actually proved (`h_p`, `c_p`) now called out as such | Finding 6.6 is `\VER`; `LAMBDA_HUNT.md:185` |
| **M-2** Cor 5.4 `\VER` with no `\PROVED` | demoted `corollary` → `finding`; "at any prime" replaced by the swept range; the wider claim moved to an explicitly-labelled expectation | §1.5's own convention; Findings 5.2/5.5 ranges |
| **M-3** Finding 3.5's two universals | "constant in s for every tower and equals `v_p(b_a/a_a)`" → "eventually constant", "flat in the branch" dropped; new Remark 3.6 gives both counterexamples | **recomputed**: `p=5,a=11` gives `v(L_s) = −4,−2,−2,−2` against `v₅(b₁₁/a₁₁) = −4`; the paper's own Table 3.6 row `4,6,9,13,15` has increments `4,2,3,4,2` |
| **M-4** family F missing | exception set → `{ε, ζ, C, F, s₁₈}`; new Remark describes the deviations as cumulative, not per-level | **independent reimplementation** of the whole sweep from the integer recurrence for `(n!)^k u_n` (so `f=B/A=U^B/U^A`, factorials cancel): at `p=5`, `C = F = s₁₈ = 4,5,7,9,11,13` against a predicted `2,4,6,8,10,12`, `B` and `E` on the nose; at `p=7`, `ε` increments `4,5,2,3,3` |
| MINOR Thm 6.3 `\VER` range | now says `K=12` except `(p²,p)`, which the run truncates to `K=6` | `kaz_p11.txt` `MATCH(all 6)`; `t7_kaz.py:121` |
| MINOR Table 6.7 | new Remark records that the last row is a miss against the script's own finer `v_p=5` prediction at `p=5` | `struct_p5.txt` "discrepancy at v_p = 4 (expect 5)" |
| MINOR Finding 7.1 vs 7.2 | `\VER` range split: `p=5,7,11` for B and (δ), `p=7,11` for (η); the ramified exclusion stated in the finding | `χ₅(5)=0` |
| MINOR §1.3(E) "digits" | → "truncations `⌊A/p^l⌋`"; abstract's missing leading `−1` of (6.3) restored | Thm 6.3 |

## 4. P4 `frobenius` — ledger

| finding | action | verification |
|---|---|---|
| **CRITICAL-1** Cor 5.2 unsound `[PROVED]` | statement now opens *"Assume the identifications of Theorem 5.1"*; marker split `\PROVED` (the relations) / `\VER{434 digits}` (the closed forms). Same repair at Obs 5.3, Obs 6.2, Obs 6.4; abstract and Results (3) now carry `\VER{434 digits}` and say the identifications were read off by integer-relation detection | **re-verified at `mp.dps=440`** from `kappas_hi.json`: `κ₅ − κ₂κ₃ − (514/87)ζ(5) = 2.34e−419`, i.e. zero to the archive's floor; `λ₄ + (215/29)ζ(4) = −2.48e−419`. The mathematics is right; only the label was wrong |
| **CRITICAL-2** Obs 5.6 false at `j=8,9` | the moving-diagonal claim replaced by the two **fixed-weight** laws, with the failure of the moving version stated; the repeat in §9 corrected | exact rationals from the paper's own Prop 5.5: fixed weight 3→4 gives `−3` at `j=7,8,9`; 4→5 gives `−3365/294` at `j=8,9`; moving diagonal gives `−3, −3365/294, −3660/4711`. Weight support, absent weights and `{3,5,7,11,29}`-smoothness re-checked and correct as printed |
| **MAJOR-3** (RPC-4) tautology | counting half removed from the conjecture; (RPC-4) keeps only `λ_m ∈ ℚ·ζ(m)`; new Remark 7.x proves the count is `⌊m/2⌋` for *any* log-series; Table 6 caption marks its last two columns as re-expressions; (F2) rewritten to test `λ_w`, with a sentence saying the monomial count can never fire independently | `#{(a,b): 2≤a≤b, a+b=m} = ⌊m/2⌋−1`, checked against all four table rows |
| **MAJOR-4** Γ-exclusion overstated | Obs 7.5 given an `\EXCL` marker naming `s ∈ {3,4,5,6,8,12,24}`; abstract and Results (6) likewise; a sentence points back at the paper's own "an exclusion is a statement about a box" | `GAMMA_UNIFICATION.md:53–54` keeps the restriction |
| **MAJOR-5** dropped `s,P̂ ∈ Sol(L)` | hypothesis restored in the abstract and in Results (7), citing Theorem 8.1 and §9.3 | Thm 8.1 states it; §9.3 declares it unproved |
| MINOR π-powers "multiply to π^{5/2}" | corrected: the **three** determinant powers sum to 5/2, the other triple to 1/2 | `−5/2+5/2+5/2+1/2 = 3` |
| MINOR Trap 2 "not quoted anywhere" | restated: quoted here as the illustration and nowhere else; no result uses them | it quotes two of them three lines above |
| MINOR Table 2 "two exceptions" | one each: Erratum 1 → Apéry ζ(3) row, Erratum 2 → Apéry ζ(2) row | Ex. 29 vs Ex. 28 |
| MINOR vacuous `\VER{…}` | `as tabulated` → `208–434 digits`; `as computed` → `12 digits`; bare `exact` → `exact rational arithmetic, 1074 checks` | §1.4 convention |
| MINOR `\EXCL` polarity | the one negated site restated positively, like the other four; the duplicated "are refuted" dropped | §1.4 convention |
| MINOR Table 5 sign | middle eigenvalue now `(−0.0843843…)^n` | roots of `4λ³−2368λ²−188λ+1` are `592.079…, −0.0843843…, 0.00500378…` |
| MINOR 1.226963 "exactly" | → "the two agree to 4 digits" | `1.22701` vs `1.226963` |
| MINOR `\ldots` on rounded digits | Theorem 5.1 now says "to 48 decimals with the final digit rounded"; `\small` moved out of math mode | `κ₄,κ₅,κ₇,κ₈` round up against `kappas_hi.json`; `κ₂,κ₃,κ₆,κ₉` truncate |
| MINOR residuals not reproducible | `\VER` tag and the precision ledger now say the `10⁻⁴⁴⁰`–`10⁻⁴⁵¹` residuals are in-session and that the 420-digit archive floors any recheck at `≈10⁻⁴¹⁹` | `t3e_high.py:88` `nstr(x,420)`; JSON strings are 422 chars; my recheck lands at `2.3e−419` |
| MINOR uncited `Zu02` | cited at the BZ recurrence (it *is* the third-order Apéry-like recursion for ζ(5)) — no bibliography entry altered | `BIBLIO_VERIFY.md` §4 left intact |
| MINOR leverage rider | `6.84×` now qualified as `γ^ratio`-dependent, with `3.68×` on `γ^worth` | referee's own arithmetic, reproduced |

## 5. Disputes

1. **P4 CRITICAL-1, on the *scope* of the relabelling.** The referee lists the abstract and
   Results (3) as having "no evidence marker at all" and treats that as the same defect as
   Cor 5.2's. I applied the fix, but I record a partial dissent: an abstract that states a
   result without a marker is a different failure from a *numbered corollary* that states a
   `[VERIFIED]` result under a `[PROVED]` marker. The first is a stylistic omission; only the
   second actively asserts a false evidence class. I fixed both, but the corollary is the one
   that mattered.
2. **P3 M-2, on the remedy.** The referee offered "demote to a Finding **or** add `\PROVED`
   with a proof". Adding a proof is not available (the content is a non-existence claim over a
   search box), so I demoted. Note this makes `cor:noroute` a `finding` whose label still reads
   `cor:` — I kept the label to avoid breaking the `.aux`; the printed environment is correct.
3. **P1 C-1 "Bonus" (LBW_GENERAL's third closed form) — deliberately NOT applied.** The referee
   notes that `b_n = Σ_k C(n,k)²C(n+k,n)²(2H⁽³⁾_n − H⁽³⁾_k)` is shorter than both printed forms
   and is the one formalised in Lean, and that §5.4 does not mention it. I verified it exactly
   (`n ≤ 14`, and it is `= b_n` at every n). But adding a third proposition is new content, not
   a repair, and the rules for this pass forbid opportunistic additions. Flagged for the author.
4. **P3, on the "0 overfull/underfull boxes" baseline.** The referee recorded 0 boxes for
   `padiclimits`; the current build has **3 underfull hboxes, all in `thebibliography`**
   (Kerr, Malik–Straub, Roy–Vlasenko), at lines far below any edit of mine. They come from the
   bibliography pass, which I was instructed not to undo. Cosmetic; not touched.
5. **P2 page count.** The referee's note stands: `build.sh` produces **39** pages, not 38.
   Confirmed again after the repairs.

## 6. Mini re-check (each CRITICAL re-verified from scratch, after the edits)

Written fresh, reusing nothing from the diagnostic runs:

- **P1 Prop 5.12** — `a_n`,`b_n` regenerated from the order-2 Apéry recurrence (not from any sum
  form); the displayed RHS equals `b_n` at every `n = 0..14` and `a_n` at **no** n. ✔
- **P1 Evidence 1.2 / Lemma 11.9** — divisor counts `1,1,1,330,1,361,361`; `c=4` fails 31×,
  first `2,6,8,18,20,24,26,54`. Degenerate pairs `(7,2),(11,6),(29,27),(p₀,·)`, of which only
  `(29,27)` violates `1 ≤ ν ≤ p−4`. `Res(a₀(ν),a₀(ν−1)) = −2²·11·37²·557³·p₀`; consecutive roots
  at `11` and `p₀` only. ✔
- **P3 Prop 2.5(iv)** — 36 `p`-unit cells all satisfy `v ≥ 3` (distribution `26/7/2/1`); 8
  non-unit cells fail; the deleted strengthening fails at 4 `p`-unit cells. ✔
  *(This re-check corrected one number I had written into the paper: the deepest failure is
  `v = −4` at `p=5, a=11`, not at `a=6` (which is `−1`). The paper now lists all eight
  valuations explicitly.)*
- **P4 Cor 5.2** — `κ₅ − κ₂κ₃ − (514/87)ζ(5) = 2.34e−419` at `dps 440`. ✔
- **P4 Obs 5.6** — fixed-weight ratios exactly `−3` (j=7,8,9) and `−3365/294` (j=8,9); moving
  diagonal `−3, −3365/294, −3660/4711`. ✔

## 7. Compile status (3× pdflatex each, after all edits)

| paper | pages | errors | undefined refs/cites | overfull |
|---|---|---|---|---|
| `sharp12/sharp12.tex` | 44 (was 42) | 0 | 0 | 9 (cosmetic) |
| `lucas2nd/main.tex` (`build.sh`) | 39 | 0 | 0 | 1 (pre-existing table) |
| `padiclimits/padic-apery-limits.tex` | 31 (was 29) | 0 | 0 | 0 overfull, 3 underfull (bibliography) |
| `frobenius/frobenius.tex` | 26 (was 25) | 0 | 0 | 0 |
