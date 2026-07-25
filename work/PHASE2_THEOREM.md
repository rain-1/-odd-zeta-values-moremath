# Phase 2 — the sharp-12 denominator law, `p ≥ 5` part: assembled statement (**v4**)

**Author:** mathematician-agent (River's odd-zeta program), tasks P1c (v1) + P1d (v2) + P1h (v3)
+ **P1i (v4)**
**Date:** v1 2026-07-24 (night) · v2 2026-07-25 · v3 2026-07-25 · **v4 2026-07-25**

> ## v4 — `(GAP-DESC)` IS PROVED. **The `p ≥ 5` MATHEMATICS OF PHASE 2 IS COMPLETE.**
> `work/PHASE2_GAPDESC.md` (P1i).
>
> The last mechanical node of the induction — the descent term (I) **off-regime**, at multi-digit
> `a` — is closed, for **every** digit level `L = ⌊log_p n⌋ ≥ 1` (so the `a < p` case is
> re-proved on the way, and **Lemma D++ is no longer needed** for this node). The proof is *not*
> the one `PHASE2_INDUCTION` §6.2 anticipated, and that one **provably does not work**: the
> letter-wise mismatch `e₁(a+b+1)^{−m}` has valuation `−mλ` (`λ = v_p(a+b+1)`) while the entire
> Kummer gain of `T` is `1+λ`, so at weight 5 the trade loses — explicitly at
> `p = 5, n = 19, (k,l) = (6,0)` the letter-wise ledger is short by one power. The pole is
> instead annihilated **inside `v₅`** by the `(DEPTH)` conditions *at level `n`*, and the whole
> node reduces to one purely combinatorial lemma:
> > **Lemma DK.** Off-regime ⟹ `v_p T(n,k,l) ≥ 1 + max(s_n, s_a)`
> > (`s_n`, `s_a` the pattern sums `α+γ+κ` at levels `n` and `a`).
> > *Reason:* off-regime = a carry in digit position `0`; the pattern indicators live in position
> > `L ≥ 1`; Kummer counts both.
> > `[VERIFIED 188 353 733 off-regime cells, digit levels L = 1,2,3,4, 0 failures, sharp]`
>
> With `(DEPTH-gen)` applied at **both** levels this gives `v_p(T·𝓔) ≥ −5(L−1)` cell by cell, so
> term (I) is bounded, the `(IND)` step is complete at every digit level, and with `(BASE)` (v3)
>
> > **`ord_p(P_n) ≥ −5⌊log_p n⌋` for every prime `p ≥ 5` and every `n ≥ 1`** — (SHARP-12, `p ≥ 5`)
> > — **modulo only the decomposition certificate `(T1-top)`.**
>
> **What remains is no longer mathematics on the `p ≥ 5` side.** The residual node for the `P_n`
> law is exactly **one** `[VERIFIED]` decomposition identity, `(T1-top)` `P_n = Σ T·w₅` (the
> second identity `P̂_n = Σ T·ŵ₃` is needed only for the companion middle row), owned by the
> certificate agent (`work/PHASE2_CERTS.md`), plus the separate `p ∈ {2,3}` remnant of §D.2.
>
> **Certificate-target note (v4).** The induction now consumes `w₅` *only* through `(DEPTH-gen)`,
> i.e. it works for **any** point of the depth-conditioned family — `[VERIFIED]` for `w₅^I`
> (`work/p1g/w5_exIII_allp.json`), which is also what `(BASE)` uses. So the `p ≥ 5` theorem can
> be run end-to-end on the **single** representative `w₅^I`, and its certificate target is then
> the **one** identity `P_n = Σ_{k,l} T·w₅^I` — the v3 "`w5_allp` certificate **plus** the
> homogeneous delta `Σ T(w₅^I − w5_allp) = 0`" is an alternative, not a requirement.
> (Cost comparison is the certificate agent's call — `PHASE2_CERTS` §14.3.)

> ## v3 — `(BASE)` IS PROVED. `work/PHASE2_NUCLEUS.md` (P1h).
> The single residual *mathematical* object of Phase 2 on the `p ≥ 5` side is closed. What
> separates Phase 2 from a theorem is now **only the two decomposition certificates** (plus the
> mechanical `(GAP-DESC)`). The proof:
> * **`n ≤ (p−1)/2`** — region `III = {k,l ≥ q, p ≤ k+l < p+q}` is **empty** (it needs `2n ≥ p`),
>   so P1g's `w₅^I` is cell-wise `p`-integral at *every* cell. Half of `(BASE)` is free.
> * **`n = (p+1)/2`** — `III` collapses to the **three corner cells** `(n−1,n),(n,n−1),(n,n)`;
>   `T/p² ≡ (2,2,24)` (Wilson+Lucas+Kummer) and `K₃ = (3−s₂/2, 3−s₂/2, −1/2−s₂/2)` (exact
>   expansion of the 207-term `w₅^I`), so the corner sum is `−14·s₂` with
>   `s₂ = Σ_{j<p} j^{−2} ≡ 0 (mod p)` for `p ≥ 5`. **One classical input, no Fermat quotient, no
>   Bernoulli number.**
> * **`n > (p+1)/2`** — forward induction; the only exceptional steps are `a₀`-roots, and those
>   are **apparent, PROVED**: all three `2×2` minors of `[(c₀,c₁,c₂)(ν); (c₁,c₂,c₃)(ν−1)]` are
>   divisible by `a₀(ν)` in `ℚ[ν]`. Equivalently an explicit order-4 left multiple `L̃` with
>   leading coefficient `2D(n+3)⁵(2n+5)` desingularises `L_BZ`.
>
> **`(REC-★)` is now a COROLLARY of `(BASE)`, not an input to it** — the implication the P1g
> brief expected runs the other way. Its exact universal form is
> `11907P_{n₀} − 334374P_{n₀+1} − 19292P_{n₀+2} ≡ 0 (mod p)`, `n₀ = (p−5)/2` — the *same* row as
> the July `a = 1` A1-MID theorem, one digit down. The reported `p = 13` non-tightness was an
> artefact of the un-normalised row; normalised, the congruence is tight (`v_p = 1`) at all 44
> primes `p ≤ 199`.
>
> **Certificate-target delta:** the proof consumes `w₅^I` (`work/p1g/w5_exIII_allp.json`), not
> `w5_allp`. Its certificate = `w5_allp`'s certificate **plus** the *homogeneous* weight-5
> summation identity `Σ_{k,l} T·(w₅^I − w5_allp) = 0`.
**Sources:** `work/PHASE2_INDUCTION.md` (**v2, the induction node**), `work/PHASE2_FINAL.md`,
`work/PHASE2_ENDGAME.md`, `work/PROOF_LB5_CLOSEOUT.md`, `work/PROOF_LB5_CAMPAIGN.md`,
`work/LBW_GENERAL.md`, `work/LEAN_LUCAS_STATUS.md`, `work/LEAN_LBWCHI_STATUS.md`.

> **Honesty note up front (v2).** This is the *assembled* statement, not a finished theorem.
> The v1 note said the remaining gap was "two nodes: the decomposition certificates, and the
> digit-scaled induction (bookkeeping)". **That was wrong about the second node, and v2 says so.**
> The induction node has now been worked out (`work/PHASE2_INDUCTION.md`) and it *splits*:
> * its two genuinely new ingredients — the multi-digit depth bound **(DEPTH-gen)** and
>   **Lemma F for multi-digit `a`** — are now `[PROVED]`, and they meet with slack exactly 0;
> * what is left is **not** bookkeeping. It is `(BASE)`: `ord_p(P_n) ≥ 0` for `n < p`. The route
>   proposed for it ("for `n < p` all letter arguments are `< p`") is **false** — the letters do
>   reach `2n` and `3n` — and the cell-wise bound the depth calculus supplies is exactly **one**
>   power short, with the shortfall **attained**. Moreover that shortfall is **provably not
>   removable** by any `w₅` cut out by `p`-independent linear depth conditions: the strengthened
>   system is inconsistent (`PHASE2_INDUCTION` §6.1). `(BASE)` needs a genuine cancellation.
> * a residual sub-gap `(GAP-DESC)`, the off-regime letter descent at multi-digit `a`, is
>   mechanical (`PHASE2_INDUCTION` §6.2).
>
> **What v2 gains unconditionally:** `ord_p(P_n) ≥ −5⌊log_p n⌋ − 1` for **all** `n` and all
> `p ≥ 5` (`PHASE2_INDUCTION` Thm 5.1) — one radical short of the sharp law, where v1 had
> nothing proved beyond `n < p²`. **`(GAP-5)` remains CLOSED** (v1's contribution).

---

## Abstract (v4)

Let `P_n`, `P̂_n` be the two upper rows of the Brown–Zudilin ladder attached to `ζ(5)` and
`Q_n = Σ_{k,l} T(n,k,l)` its bottom row. **For every prime `p ≥ 5` and every `n ≥ 1`,
`ord_p(P_n) ≥ −5⌊log_p n⌋`** — the `p ≥ 5` half of the sharp denominator law
`den(P_n) | 12·d_n⁵` — **modulo the single `[VERIFIED]` decomposition identity**
`P_n = Σ_{k,l} T(n,k,l)·w₅(n,k,l)` **(T1-top)**, a finite creative-telescoping certificate being
machine-closed in parallel (`work/PHASE2_CERTS.md`). *(The companion middle-row statement about
`P̂_n` needs the second identity `P̂_n = Σ T·ŵ₃`, Theorem B; the `P_n` law above does not.)*
**No mathematical node of the `p ≥ 5` side is open.** The proof is a digit-scaled induction
`(IND)` on `L = ⌊log_p n⌋` for `W_n = P_n − H^{(5)}_n Q_n`, whose four ingredients are now all
proved:

1. **`(DEPTH-gen)`** — the 42 single-digit depth conditions on the 124-dimensional family of
   weight-5 harmonic representatives are **level-independent** (Prop. LIFT), so they bound the
   `p`-adic depth `d₅ ≤ 5L + 1 + min(v_pT,2)` at every base-`p` digit level at once
   (`PHASE2_INDUCTION` §2). Unconditional corollary: `ord_p(P_n) ≥ −5⌊log_p n⌋ − 1` for all `n`.
2. **Lemma F-gen** — the fibre congruence `v_p(𝒯(b,c) − Q_r T(a,b,c)) ≥ 1 + min(s_a,2)` at
   multi-digit `a`, with no `p ∤ Q_a` hypothesis, no `Q_n/Q_a`, and without Lemma Phi
   (`PHASE2_INDUCTION` §3). It meets 1 with slack exactly 0: the fibre term of the step is exact.
3. **`(BASE)`** — `ord_p(P_n) ≥ 0` for `n < p`, by the midpoint split: the single band
   `III = {k,l ≥ p−n, p ≤ k+l < 2p−n}` is empty below `(p+1)/2`, collapses to three corner cells
   at `(p+1)/2` whose residues sum to `−14Σ_{j<p}j^{−2} ≡ 0`, and the `L_BZ` steps above the
   midpoint are apparent singularities — equivalently an explicit order-4 left multiple `L̃` with
   leading coefficient `2D(n+3)⁵(2n+5)` desingularises `L_BZ` (`PHASE2_NUCLEUS`).
4. **`(GAP-DESC)`** — the descent term off-regime at every digit level, by `(DEPTH-gen)` at
   *both* levels plus one Kummer lemma: off-regime means a base-`p` carry in position `0`, the
   depth-pattern indicators live in position `L ≥ 1`, and Kummer counts both, giving
   `v_pT ≥ 1 + max(s_n,s_a)` — exactly the two depth caps the two levels charge
   (`PHASE2_GAPDESC`). The letter-wise route this node was expected to take is **refuted**.

The single external arithmetic input of the whole chain is Wolstenholme's congruence (inside
Lemma W, used by Lemma B), together with `Σ_{j<p} j^{−2} ≡ 0` at the nucleus — which is why
`p ≥ 5` is exactly the right hypothesis. The `p ∈ {2,3}` factor `12` is a separate matter (§D.2).

---

## Abstract (v2)

Let `P_n` and `P̂_n` be the two upper rows of the Brown–Zudilin ladder attached to `ζ(5)` and
`Q_n = Σ_{k,l} T(n,k,l)` its bottom row. Numerically `den(P_n) | 12·d_n⁵` for all `n ≤ 360` — a
*sharp* denominator law. The `p ≥ 5` half reduces, by a three-row graded Frobenius descent, to a
carry ledger comparing the `p`-adic depth of a weight-5 harmonic weight `w₅` against Kummer
carries of `T`. **The state of that reduction after v2 is:**

1. **PROVED, unconditionally in `n`** (given the decomposition certificate and the (DEPTH)
   linear certificate): `ord_p(P_n) ≥ −5⌊log_p n⌋ − 1`. The engine is a *level-lifting*
   proposition — the 42 single-digit depth conditions of `PHASE2_FINAL` §2.3 are
   **level-independent**, so they bound `d₅` at every base-`p` digit level at once.
2. **PROVED**: Lemma F at multi-digit `a` in the form the induction consumes,
   `v_p(𝒯(b,c) − Q_r T(a,b,c)) ≥ 1 + min(α+γ+κ, 2)` — with no `p ∤ Q_a` hypothesis, no `Q_n/Q_a`,
   and **without Lemma Phi**. The exceptional primes cost nothing.
3. **PROVED**: the induction step consumes exactly what 1 and 2 provide, slack 0 per digit.
4. **PROVED (v3, P1h)**: `(BASE)` (`= ord_p(P_n) ≥ 0` for `n < p`), by the midpoint split
   (region III empty below `(p+1)/2`; three corner cells at `(p+1)/2` summing to `−14Σ_{j<p}j^{−2}`;
   proved-apparent `a₀` steps above). Still **OPEN**: the off-regime letter descent
   `(GAP-DESC)`, which is mechanical.
5. **OPEN**: the two decomposition certificates (`P̂_n = Σ T·ŵ₃`, `P_n = Σ T·w₅`), `[VERIFIED]`,
   being machine-closed in parallel.

`(BASE)` and the induction step turn out to be **the same statement at different digit levels**:
both are the pair of mod-`p` identities `(V2)`,`(V3)` of `PHASE2_INDUCTION` §6.3. That is the
single residual mathematical object of Phase 2 on the `p ≥ 5` side.

---

## Abstract (v1, retained)

Let `P_n` and `P̂_n` be the two upper rows of the Brown–Zudilin ladder attached to `ζ(5)`, and
let `Q_n = Σ_{k,l} T(n,k,l)` with `T(n,k,l) = C(n+k,n)C(n,k)²C(n+l,n)C(n,l)²C(n+k+l,n)` be its
bottom row. Numerically `den(P_n) | 12·d_n⁵` for all `n ≤ 360`, where `d_n = lcm(1,…,n)` — a
*sharp* denominator law, five powers of `d_n` rather than the six that the naive integral
representation gives, with a single global factor 12. We prove the `p ≥ 5` half of this law
modulo two explicitly isolated inputs. The mechanism is a three-row graded Frobenius descent:
the `Q`-row obeys an exact Lucas congruence `Q_{ap+r} ≡ Q_a Q_r (mod p)` (proved, and
formalized in Lean 4 with zero sorries); the `H`-layer of the upper rows reduces the
denominator law to a one-digit product congruence `p⁵P_{ap+r} ≡ P_a Q_r (mod p)`; and that
congruence is paid for, cell by cell over the base-`p` fibre, by a *carry ledger* — a
comparison between the `p`-adic depth of a weight-5 harmonic weight `w₅` and the Kummer
carries of `T`. The two new ingredients are **Lemma F**, an exact block factorisation of `T`
over a base-`p` fibre combined with a residue identity (**Lemma Phi**) that annihilates the
entire first-order `(b,c)`-dependence of the fibre sum, yielding
`Σ_{s,t} T(n,bp+s,cp+t) ≡ (Q_n/Q_a)·T(a,b,c) (mod p^{2+min(v_p T(a,b,c),2)})` using only
Wolstenholme's congruence (which is exactly why `p ≥ 5`); and, established here, the
observation that the harmonic weight `w₅` is not unique — it ranges over a 135-dimensional
affine family — and that the ledger is payable **iff** one works with a *depth-minimal* member
of that family. We show that depth-minimality is cut out by 42 `p`-independent linear
conditions on the family, that these conditions are **consistent** (they leave a
124-dimensional subfamily), and that the subfamily contains representatives whose coefficient
denominators are supported on `{2,3}`, hence usable at every prime `p ≥ 5` at once. With such
a representative the ledger balances with slack exactly zero at every one of the 16 990 cells
tested at `p = 5,7,11,13` — where the previously canonical representatives failed at up to
63% of cells. The two sharpnesses meet: Lemma F cannot be improved, and the depth conditions
cannot be weakened.

---

## A. The target

> **Theorem (SHARP-12, `p ≥ 5` part).** For every prime `p ≥ 5` and every `n ≥ 0`,
> ```
>     ord_p(P_n)  ≥  −5·⌊log_p n⌋  =  −ord_p(d_n⁵) .
> ```
> Equivalently `d_n⁵ · P_n ∈ ℤ[1/6]`, which is the `p ≥ 5` half of `den(P_n) | 12·d_n⁵`.

**[VERIFIED 3240/3240 cells, 0 failures]** directly, `p ∈ {5,7,11,13,17,19,23,29,31}`,
`n ≤ 360`; **[VERIFIED 27 000/27 000]** extended to `n ≤ 3000` by the certified order-3
recurrence (exact ℚ, cross-checked against the ladder on `n ≤ 360`, 0 mismatches),
`p ≤ 31`, min slack exactly `0` (`work/p1d/sweep.py`); and `[VERIFIED 361/361]` in the form
`den(P_n) | 12 d_n⁵` (`work/LTILDE_HUNT.md`).

**v2 correction to the reduction.** v1 said this "follows from the one-digit product congruence
(LB₅) by a digit-scaled induction". The correct route, worked out in `work/PHASE2_INDUCTION.md`,
does **not** go through (LB₅): the induction (IND) is an inequality on
`W_n = P_n − H^{(5)}_n Q_n` whose per-digit step needs only **(DEPTH-gen)** and **Lemma F-gen**,
both proved there, plus the base case. (LB₅) itself turns out to be conditional on the same base
case. Proved unconditionally for all `n`:

> **Theorem 5.1 (P1d).** `ord_p(P_n) ≥ −5⌊log_p n⌋ − 1` for every `p ≥ 5`, every `n ≥ 1`;
> and `ord_p(P_n) ≥ 0` outright whenever `p > 3n`.

The single-digit congruence, still the sharp statement at `n < p²`, is

> **(LB₅).** `p ≥ 5`, `1 ≤ a < p`, `0 ≤ r < p`, `n = ap+r`:  `p⁵ P_{ap+r} ≡ P_a·Q_r (mod p)`.

---

## B. Dependency tree, every node labelled (**v4**)

Legend
`[P-p1i]` proved in `work/PHASE2_GAPDESC.md` (v4, this session) ·
`[P-p1h]` proved in `work/PHASE2_NUCLEUS.md` (v3) ·
`[P-p1d]` proved in `work/PHASE2_INDUCTION.md` (v2) ·
`[P-here]` proved in `work/PHASE2_FINAL.md` ·
`[P-endgame]` proved in `work/PHASE2_ENDGAME.md` ·
`[P-prior]` proved in an earlier file (named) ·
`[CERT]` machine certificate, independently re-verified by exact arithmetic ·
`[LEAN]` formalized in Lean 4, 0 sorries, axioms `{propext, Classical.choice, Quot.sound}` ·
`[V]` verified only (exact finite evidence, 0 failures) · `[SKETCH]` · `[OPEN]`.

```
(SHARP-12, p>=5)   ord_p(P_n) >= -5*floor(log_p n)          [PROVED (v4) modulo (T1-top) only;
 │                                                           V 3240/3240 (n<=360)
 │                                                                     + 27000/27000 (n<=3000)]
 ├─ WEAKER, BUT UNCONDITIONAL AND FOR ALL n:
 │     ord_p(P_n) >= -5*floor(log_p n) - 1                            [P-p1d Thm 5.1]
 │   ├─ Lemma U (level expansion of H^(m)_N)                          [P-p1d §2.1]
 │   ├─ Lemma R (top-level residues alpha, gamma, kappa*theta^-m, 0)  [P-p1d §2.3]
 │   ├─ Lemma K (Kummer floor: v_pT >= alpha+gamma+kappa)             [P-p1d §2.3]
 │   ├─ Lemma C (7-pattern census at EVERY digit level, level-free proof) [P-p1d §2.3]
 │   ├─ Prop. LIFT: the single-digit (DEPTH) rows are level-INDEPENDENT   [P-p1d §2.4]
 │   │   └─ the (DEPTH) linear certificate (rank 324 = rank aug)      [CERT — PHASE2_FINAL §2.3]
 │   ├─ (DEPTH-gen): d5 <= 5L + 1 + min(v_pT,2), all n, all p>=5      [P-p1d §2.4] [V 0/150955]
 │   └─ (T1-top)                                                      [V]  ← RESIDUAL NODE 1
 │
 ├─ digit-scaled induction (IND) on L = floor(log_p n)                [P-p1d §4 + P-p1h + P-p1i
 │                                                                    = COMPLETE (v4)]
 │   │   statement: I(L): v_p(W_m) >= -5*floor(log_p m) for all m with floor(log_p m) <= L,
 │   │              W_m = P_m - H^(5)_m Q_m.   Step: split
 │   │              p^5 W_n - Q_r W_a = (I) descent + (II) fibre,  n = ap+r.
 │   ├─ (II) fibre term: ledger balances with slack EXACTLY 0         [P-p1d §4.2]
 │   │   ├─ provided  v_p(v5(a,b,c)) >= -5(L-1) -1 -min(s_a,2)        [= (DEPTH-gen)]
 │   │   └─ provided  v_p(Tcal - Q_r T(a,b,c)) >= 1 + min(s_a,2)      [= Lemma F-gen]
 │   ├─ Lemma F-gen (multi-digit a; NO p∤Q_a, NO Lambda, NO Lemma Phi) [P-p1d §3] [V 0/111963]
 │   │   ├─ Lemma B, general a (exact fibre block factorisation)       [P-endgame R1.1, general] [V 0/8.2M]
 │   │   │   └─ Lemma W (Wolstenholme block, p >= 5)                   [P-endgame R1.1]
 │   │   ├─ carry inequalities (C1),(C2)                               [P-p1d §3.3]
 │   │   └─ Theorem A / Lemma 4 (mod-p factorisation of T, all a)      [P-prior, campaign §2] [LEAN]
 │   ├─ (I) descent term, IN-REGIME                                    [P-p1d §4.3]
 │   ├─ (I) descent term, OFF-REGIME, EVERY digit level  (GAP-DESC)    [P-p1i — PHASE2_GAPDESC.md]
 │   │       [V 0 failures: 188 353 733 off-regime cells for the carry lemma,
 │   │        p <= 31, L = 1,2,3,4; 11 096 075 for its slot-wise ingredients;
 │   │        + 1 161 740 cells with the exact p-adic E, p <= 13, L = 1,2,3]
 │   │   ├─ (DEPTH-gen) applied at LEVEL n:  v_p(p^5 v5(n,k,l)) >= -5(L-1) -1 -min(s_n,2)
 │   │   ├─ (DEPTH-gen) applied at LEVEL a:  v_p(   v5(a,b,c)) >= -5(L-1) -1 -min(s_a,2)
 │   │   ├─ Lemma D1 (digit dictionary: alpha >= alpha_a, gamma >= gamma_a,
 │   │   │    kappa >= kappa_a unless e4=1 & b+c = p^L-1; in-regime s_n = s_a) [P-p1i §2]
 │   │   └─ Lemma DK (descent Kummer): off-regime => v_pT(n,k,l) >= 1 + max(s_n,s_a)
 │   │        via  v_pT >= s_n + B,  B := e1+e2+2[s>r]+2[t>r]+(e3-e4) >= 1     [P-p1i §3]
 │   │        (position 0 vs position L >= 1: Kummer counts both — SHARP, slack 0)
 │   │   ·  the a<p case is now a SPECIAL CASE; Lemma D++ (endgame R3) is NOT needed here
 │   │   ·  the letter-wise route of p1d §6.2 is REFUTED: the A_5(k) mismatch has v_p = -5*lambda
 │   │      against a Kummer gain of 1+lambda  (explicit: p=5, n=19, (k,l)=(6,0))  [P-p1i §5]
 │   │   ·  representative-independent: also [V] for w5^I (work/p1g/w5_exIII_allp.json)
 │   └─ base case (BASE): ord_p(P_n) >= 0 for n < p          [P-p1h — PHASE2_NUCLEUS.md]
 │       [V 11884/11884, every prime 5<=p<=367]   ← was OPEN through v2
 │       · cell-wise bound is exactly -1 and ATTAINED at (n,k,l)=((p+1)/2,0,(p-1)/2)
 │       · (DEPTH+) and (DEPTH++) strengthenings are INCONSISTENT      [CERT, both primes]
 │         ⟹ no p-independent choice of w5 can make it cell-wise
 │       · cancellation is global in (b,c): row sums over c still have v_p = -1  [V p<=13]
 │       · [P1g] ENLARGED alphabets do not help: Apery letters R^(a) (1210 coeffs,
 │         rank(fit) 313 -> 960, dim U 261 -> 641) and nested interval letters
 │         Y_ab / V_ab are ALL INCONSISTENT at the strengthened cap    [V, N=1300]
 │         ⟹ PHASE2_CANCEL §7.1 route (V-a) REFUTED as proposed, for the
 │         p-independent symbol-independent conditions.  The "honest"
 │         prime-by-prime form of those conditions is OPEN, costed [RLETTER §8]
 │       · [P1g] PARTIAL CLOSURE: explicit 155-term harmonic representative
 │         w5_I (work/p1g/w5_I.json, denominators {2,3,71}) makes EVERY cell
 │         outside the single band III = {k,l >= q=p-n, p <= k+l < p+q}
 │         cell-wise p-integral, so   (BASE) <=> Sum_III (T/p^2)K_3 = 0 (mod p)
 │         — ONE region, replacing PHASE2_CANCEL §2's 2*Sum_I + Sum_III = 0.
 │         [V exact: identity n<=20; 10092 cells over p=5..23; 0 violations]
 │       · [P1g] recurrence route: the a_0-root exceptional steps of L_BZ are
 │         APPARENT singularities, so (BASE) reduces to the SINGLE congruence
 │         (REC-*) c0 P_{n0} + c1 P_{n0+1} + c2 P_{n0+2} = 0 (mod p), n0=(p-5)/2
 │         [V 82 steps / 44 primes, 0 failures; 107 apparency tests p<600]
 │       · [P1h] CLOSED.  Three ingredients, all PROVED:
 │         (i)  region III is EMPTY for n <= (p-1)/2   (III needs 2n >= p)
 │              => w5^I is cell-wise p-integral there  => (BASE) free below the midpoint
 │         (ii) at n = (p+1)/2, III = {(n-1,n),(n,n-1),(n,n)} -- THREE corner cells;
 │              T/p^2 = (2,2,24) [Wilson+Lucas+Kummer], K_3 = (3-s2/2, 3-s2/2, -1/2-s2/2)
 │              [exact expansion of the 207-term w5^I; free of h_1..h_5, s_1, s_3..s_5],
 │              corner sum = -14*s2 = 0 (mod p) since s2 = Sum_{j<p} j^-2 = 0 for p>=5
 │         (iii) above the midpoint only a_0-root steps are exceptional, and they are
 │              APPARENT -- PROVED: all three 2x2 minors of [(c0,c1,c2)(v);(c1,c2,c3)(v-1)]
 │              are divisible by a_0(v) in Q[v].  Equivalently an explicit order-4 left
 │              multiple L~ of L_BZ has leading coefficient 2D(n+3)^5(2n+5): a_0 removed.
 │              [V L~ annihilates Q,P,Ph exactly, v=1..40, 0 residuals]
 │              Fully degenerate steps (row(v-1)=0 mod p) occur at exactly (7,2),(11,6),
 │              (543606522303979, 416574044722681); the last two are apparent by the
 │              row(v-1)/p functional, p=7 is a finite check.
 │         => (REC-*) is a COROLLARY of (BASE), not an input; universal normalised row
 │            (11907,-334374,-19292) = 2^7 c_i(-5/2)/7 = the July A1-MID row, one digit down.
 │            [V normalised (REC-*) tight, v_p = 1 exactly, all 44 primes p <= 199]
 │            The reported p=13 non-tightness was an artefact of the UN-normalised row.
 │         CAVEAT: uses w5^I, so its decomposition certificate is w5_allp's PLUS the
 │            homogeneous identity  Sum_{k,l} T*(w5^I - w5_allp) = 0.
 │
 └─ (LB₅)  p^5 P_{ap+r} ≡ P_a Q_r  (mod p)     [single digit, n < p²]  [P-here, modulo (T1-top)
     │                                                                   AND (BASE) — see note]
     │   NOTE (v2): as assembled, the last step of (LB₅) needs
     │   v_p((Λ−Q_r)W_a) >= 1 + v_p(W_a) >= 1, i.e. it needs (BASE). So (LB₅) is *also*
     │   conditional on (BASE) unless it is re-assembled. The induction (IND) above does NOT
     │   use (LB₅) at all; it needs only Lemma F-gen, which is unconditional.
     │
     ├─ Theorem C:  (LB₅) ⟺ (W5), the H_5-layer reduction             [P-prior, campaign §4]
     │   └─ Theorem A:  Q_{ap+r} ≡ Q_a Q_r (mod p)                    [P-prior, campaign §2] [LEAN]
     │
     ├─ (T1-top)  P_n = Σ_{k,l} T(n,k,l)·w₅(n,k,l)                    [V]  ← RESIDUAL NODE 1
     │   │        exact over ℚ, n <= 40; +287/687 excess equations mod two primes at N=600
     │   ├─ the 135-dim decomposition family (448 monomials, rank 313) [P-endgame R2.1] [V]
     │   ├─ depth-minimal subfamily: 42 linear conditions, rank(joint)=324
     │   │   = rank(augmented) ⟹ CONSISTENT, dim 124                  [P-here §2.3]
     │   └─ explicit representatives w5_allp (178 terms, denominators {2,3}),
     │       w5_canon2 (126 terms, {2,3,5}), w5_dm_nB_desc (134, {2,3,16703})  [P-here §2.4] [V]
     │
     ├─ Lemma G (letter descent), in-regime                           [P-prior, closeout §2.1]
     │   └─ Lemma H (digit split of H^{(m)})                          [P-prior]
     ├─ Lemma G, off-regime                                           [P-endgame R3]
     │   └─ Lemma D++ (boundary carry, v_p T >= 4)                    [P-endgame R3]
     │       └─ Lemma D / D+ (triple-carry slack)                     [P-prior, campaign §6,§6b]
     │
     ├─ Lemma F (refined fibre-Lucas), SHARP:
     │      Tcal(b,c) ≡ (Q_n/Q_a)T(a,b,c) mod p^{2+min(v_p T(a,b,c),2)}   [P-endgame R1.4]
     │   ├─ Lemma B (exact fibre block factorisation)                 [P-endgame R1.1]
     │   │   └─ Lemma W (Wolstenholme block, p >= 5)                  [P-endgame R1.1]
     │   ├─ Lemma Phi (exact residue identity, kills the (b,c)-dependence) [P-endgame R1.2]
     │   ├─ Lemma F1 (first-order fibre expansion)                    [P-endgame R1.3]
     │   ├─ Lemma F2 (off-fibre-regime vanishing)                     [P-endgame R1.3]
     │   └─ level-a Lemma D:  d3 <= 1 + min(v_p T, 2)                 [P-endgame R1.0]
     │
     └─ (GAP-5) — CLOSED                                              [P-here §2]   ← was OPEN
         ├─ level-a pole calculus: every letter = residue·u^r + Z_p,
         │    u = p^{-1}; kappa = v_p C(a+b+c,a); vT = alpha+gamma+kappa [P-here §2.1]
         ├─ pattern census: exactly 7 reachable (alpha,gamma,kappa,theta) [P-here §2.2] [V p<=23]
         ├─ (DEPTH): K_j = 0 for j > cap(pattern)  ⟹  d5 <= 1+min(vT,2)
         │    at EVERY p >= 5 simultaneously (p-independent conditions)   [P-here §2.3]
         ├─ consistency of (DEPTH) with the fitting system                [P-here §2.3] [V 2 primes]
         ├─ CRT combination removing all denominator primes >= 5          [P-here §2.4]
         └─ ledger balances cell by cell, slack exactly 0                 [P-here §2.5] [V 16990/16990]

(MIDDLE ROW — the weight-3 twin, complete except node 1')
 Theorem E:  v_p(p³P̂_{ap+r} − P̂_a Q_r) >= 1 + min(0, v_p(P̂_a))     [P-endgame + closeout §2.1]
  ├─ Theorem B:  P̂_n = Σ T·ŵ₃                                        [V]  ← RESIDUAL NODE 1'
  ├─ Theorem C (weight-3 twin)                                        [P-prior]
  ├─ Lemma F                                                          [P-endgame]
  ├─ Lemma G in-regime + off-regime                                   [P-prior + P-endgame]
  ├─ Theorem A                                                        [P-prior] [LEAN]
  └─ weight-3 depth bound d3 <= 1+min(vT,2), 0 violations at every p   [P-endgame R1.0] [V]

(Q ROW — complete)
 Q_n = Σ_{k,l} T(n,k,l) is annihilated by L_BZ                        [CERT — P-here §1.2]
     ├─ Annihilator (3 generators) re-verified: L·T/T → 0             [CERT]
     ├─ k-step telescoper/certificate pairs re-verified: → 0          [CERT]
     └─ final order-3 telescoper = L_BZ exactly (Expand → {0,0,0,0})  [CERT]
 Q_{ap+r} ≡ Q_a Q_r (mod p)                                           [P-prior] [LEAN]
 Q_{ap+r} ≡ Q_a(Q_r + p·a·Psi_a) (mod p²)                             [P-endgame R1.4 Cor.] [V]

(GENERAL THEORY — proved and formalized, feeds the pattern)
 Theorem LB (abstract χ-twisted weight-w Frobenius descent)           [P-prior, LBW_GENERAL] [LEAN]
  ├─ Lemma K (Frobenius descent of a χ-twisted harmonic letter)       [LEAN]
  ├─ instance: p³·b_{ap+r} ≡ b_a·a_r (mod p)  (minimal Apéry)         [LEAN]
  └─ instance: p²·B_{ap+r} ≡ B_a·A_r (mod p)  (Franel)                [LEAN]
```

---

## C′. What P1d (v2) changed — in one line each

1. **Prop. LIFT** (`PHASE2_INDUCTION` §2.4): the 42 single-digit (DEPTH) conditions are
   **level-independent**; the same certificate bounds `d₅` at every base-`p` digit level.
2. **(DEPTH-gen)** ⟹ **`ord_p(P_n) ≥ −5⌊log_p n⌋ − 1` for all `n`** — the first bound of any kind
   beyond `n < p²`.
3. **Lemma F-gen** (`§3`): Lemma F at multi-digit `a`, in the weak form the induction consumes;
   proof shorter than the single-digit one, no Lemma Phi, no `p ∤ Q_a`, no `Q_n/Q_a`.
4. **The budget is exact**: (DEPTH-gen) and Lemma F-gen meet with slack **0** at every digit.
5. **A hard negative**: the base-case deficit is `−1`, attained, and **cannot** be removed by any
   `p`-independent linear depth strengthening — `(DEPTH⁺)` and `(DEPTH⁺⁺)` are both inconsistent.
6. **The residue is one object**: `(BASE)` and the induction step are the same pair of mod-`p`
   identities `(V2)`,`(V3)` at different digit levels.

## C. The one thing the P1c session (v1) changed

The endgame left `(GAP-5)` as the sharper of the two obstructions and proved that it could
**not** be closed from the Lemma-F side (Lemma F is sharp — the bound `p^{2+min(vT,2)}` is
attained). The fix therefore had to come from the `w₅` side, and the endgame conjectured it
was a linear problem. It is, and it is consistent. Precisely:

1. **The pole calculus is `p`-independent.** At level `a` (`0 ≤ b,c ≤ a < p`) every letter is
   `residue·p^{-weight} + ℤ_p`, with residue `1` for a poled `A`, `0` for `B` and `N`, and
   `θ^{-r}` for a poled `C_r` (`θ = 1 + ⌊(b+c)/p⌋ ∈ {1,2}`, a `p`-unit for `p ≥ 5`); and
   `κ := v_p C(a+b+c,a)` is exactly the `C`-pole indicator, so `vT = α+γ+κ`.
2. **Only 7 pole patterns occur** — in particular `(α,γ,κ) = (1,0,0)` and `(0,1,0)` are
   *absent*, which is the census form of "`a+b ≥ p ⟹ vT ≥ 2`".
3. Requiring the top `u`-coefficients to vanish identically gives **68 rows of rank 42**;
   **31 of them are already implied by the decomposition identity**, so only **11** are new.
4. The joint system has rank `324 = ` rank of its augmentation: **consistent**. Family
   dimension `448 − 324 = 124`.
5. The residual `p`-dependence is *only* the denominator primes of the chosen representative;
   a CRT combination of two representatives with disjoint bad primes gives one with
   denominators supported on `{2,3}`.
6. The ledger then balances at **every** cell with slack exactly `0`
   (`0/270, 0/707, 0/5379, 0/10634` at `p = 5,7,11,13`), versus `1/270, 18/707, 3385/5379,
   1285/10634` for the closeout's 130-term representative and `34/270, 91/707, 3503/5379` for
   the endgame's sparsest canonical one.

Route B (thin-set cancellation, the weight-5 twin of `(MID)`) is **not needed**.

---

## D. What remains

### D.0 (v4) The scoreboard, in one line

> On the `p ≥ 5` side **exactly one kind of node is open: the decomposition certificates**
> (`P̂_n = Σ T·ŵ₃`, `P_n = Σ T·w₅`). Everything else — `(GAP-5)`, `(DEPTH-gen)`, Lemma F-gen,
> the `(IND)` ledger, `(BASE)`, `(GAP-DESC)` — is `[PROVED]`. The `p ∈ {2,3}` factor `12` is a
> separate, differently-flavoured remnant (§D.2). The lists below are kept in their historical
> form; the `[OPEN]` labels inside D.1 that concern `(BASE)` (v3) and `(GAP-DESC)` (v4) are
> superseded by the notes at the top of this file.

> **v4.1 refinement (P1e session 4).** The two decomposition certificates are no longer the same
> *kind* of open node and should not be quoted together:
> * **`(T1-top)`** is `[BLOCKED BY A STRUCTURAL OBSTRUCTION]` — `PHASE2_CERTS` §16 **proves** the
>   weight-5 fitting system has no degree-≤3 representative in any of three alphabets, so the
>   cheap route that made Theorem B tractable provably does not exist at weight 5. This is a
>   mathematical fact about `w₅`, not a compute shortfall, and it will not yield to more hardware.
> * **Theorem B** is a *compute* node, and session 4 broke its blocking step for the first time
>   (`PHASE2_CERTS` §17.3: the `τ = ll` elimination went from "> 70 min, no return, twice" at
>   rank 2 to "≈ 9 min, returned" at rank 1). It remains unfinished.

### D.1 For `p ≥ 5` — two nodes

* **Node 1 / 1′ — the decomposition identities.** `P̂_n = Σ T·ŵ₃` (Theorem B) and
  `P_n = Σ T·w₅` (T1-top) are `[VERIFIED]`, not proved. Status after this session:
  * the licence blocker is **gone** (`work/PHASE2_FINAL.md` §0: reap orphan kernels with
    `kill -KILL`, use `Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"]` under
    `math < f.wl`, split the two telescoping steps);
  * the `Q`-row gate is now `[CERT]`: the two-step CT reproduces `L_BZ` **exactly**, and the
    annihilator and all certificates were re-verified by exact rational-function arithmetic;
  * the deformed CT is re-diagnosed as a **complexity** blocker: the first three stages are
    free even with a symbolic parameter, but the second telescoping step does not return in
    20 min (and `TimeConstrained` does not interrupt it), while a *rational* specialisation
    costs 33 s and yields an order-4 telescoper;
  * hence a costed route: reconstruct `L(ε)` by interpolation from rational samples and
    verify the certificate exactly (`Expand → 0`). ≈ 15 kernel-hours for Theorem B.

  **P1e update (2026-07-25, session 3 — `work/PHASE2_CERTS.md` §§13–15).** The ε-deformation
  route above was replaced and is no longer the plan. Current true state of this node:
  * **Theorem B** — reduced to *exactly five* creative-telescoping problems, one per shift term
    of the τ-split `E(v) = Σ_τ F_τ`, each on a rank-≤3 module. The split identity is
    **`[CERTIFIED — RISC-free and symbolic]`**, and the whole downstream chain (composition,
    `LCLM`, RISC-free verification, `L'' = M ** L_BZ`, initial-value count) is written and
    tested. `D_n = Σ T·ŵ₃ − P̂_n = 0` is `[VERIFIED exact]` for **`n = 0…300`**, so any
    `ord(M) ≤ 298` finishes it. **Remaining cost ≈ 4–10 kernel-hours, no new mathematics.**
    The monolithic route is *dead*: `Annihilator` OOM-killed at 14.4 GB (`PHASE2_CERTS` §13.1).
  * **(T1-top)** — under v4's collapse to `w₅^I` the certificate is **no cheaper**: the support
    of `E(w₅^I)/T` measures **220**, against 208 for `w5_allp` and **6** for `ŵ₃`
    (`work/lb5/esupp.py`). The driver is monomial **degree** (a squarefree degree-`d` monomial
    contributes `2^d−1` sub-monomials); `ŵ₃`'s folded form has degree ≤ 2, every `w₅` has
    degree 4–5. This node is blocked on a *structural* idea, not on compute — the one cheap
    decisive experiment is the degree-≤3 consistency test of `PHASE2_CERTS` §15.2.

  **P1e update (2026-07-25, session 4 — `work/PHASE2_CERTS.md` §§16–17).**
  * **(T1-top) — the decisive experiment has been run and is NEGATIVE.**
    `[PROVED negative]`, `work/lb5/degfit.py`. The weight-5 fitting system `P_n = Σ_{k,l} T·w`
    is **inconsistent** when the support is restricted to letter monomials of degree ≤ 3, and
    the obstruction is the **fit identity alone** — not the `p`-integrality conditions, so no
    pole-cap regime (`base`/`vt2`/`exIII`/`strong`) can rescue it. Verified in three alphabets:
    plain harmonic `A,B,C,N` (also inconsistent at degree ≤ **4**), Apéry-extended `+R_r(k)`,
    and true depth-2 nested `+Y_ab,V_ab,Z_ab`; two primes; the harness reproduces `exIII.log`'s
    known positive and `strong`'s known negative. **`ŵ₃`'s degree-≤2 folded form has no
    weight-5 analogue.** This node is therefore `[BLOCKED BY A STRUCTURAL OBSTRUCTION]`, and
    that is a *result*, not a resource shortfall: the cheapest certified route remains a
    creative telescoping on a rank-100 (`w5_Rbase`) to rank-220 (`w₅^I`) `∂`-finite module.
  * **Theorem B — still open, but the blocking step has been broken for the first time.**
    No complete `M_τ` landed in session 4, and two of the five τ failed hard:
    `Annihilator[F_kk]` (largest τ, 13069 leaves) was **OOM-killed at 85 min / 7.8 GB**, and the
    `Support`-boxed rank-2 first elimination for `F_ll` ran **> 70 min** with no return. The
    "4–10 kernel-hours, no new mathematics" estimate is therefore **withdrawn**.
    *But*: `PHASE2_CERTS` §17.3 proves (symbolically) that `p_ll = r_ll = 0`, so
    `F_ll = (G_ll q_ll)·A₂(k)` with `A₂(k)` **free of `l`** — the letter factors out of the
    `l`-sum with **no Abel correction** — and running that elimination at rank 1 instead of
    rank 2 (`certQ.wl`) **returned in ≈ 9 minutes with 3 telescopers**, the first time any τ has
    cleared its first elimination in the whole campaign. The same decomposition applies partly to
    all five τ (§17.3). Separately, §17.5 records a **harness bug** — `stage` was missing
    `HoldRest`, so every `MemoryConstrained` cap was a no-op and no checkpoint ever prevented
    recomputation; this explains all the uncapped OOMs, including §13.1's 14.4 GB one.

  **P1e update (2026-07-25, session 5 — `work/PHASE2_CERTS.md` §18).**
  * **Theorem B — still `[NOT CERTIFIED]`; no `M_τ` exists yet.** But the reason three sessions
    of compute produced nothing is now identified, and it was a **misidentified cost driver**:
    the expense of creative telescoping here scales with the **number of harmonic letters** in
    the object, *not* its `LeafCount`. Controlled measurement, same τ, same machine:
    `Annihilator[F_n1]` (578 leaves, **10 letters**) — 19 min, no return; `Annihilator` of its
    letter-free piece (400 leaves, **0 letters**) — 3 generators, **0 s**. `F_ll` was never
    cheap for being small (it is 2318 leaves, four times *bigger* than `F_n1`); it was cheap for
    carrying 2 letters instead of 10. Every §§13–17 ranking by `LeafCount` was inverted.
  * **The remedy is proved and implemented.** `E(v)`'s τ-split refines into a **four-piece letter
    split** `F_τ = W P + W Q·A₂(k) + W R·Ψ_k + W R·Ψ_l` (`Ψ = Ψ_k + Ψ_l` with `Ψ_k` free of `l`),
    `[PROVED symbolically for all five τ]`, RISC-free and non-circularly against `certP.wl`'s own
    `stuff[]`/`Ftau[]`. It caps every piece at ≤ 4 letters and the first piece at **0**, and needs
    **no Abel correction anywhere**. Measured effect: `Annihilator` + first elimination +
    Gröbner now cost **6–33 seconds** per piece, against ≈ 12 minutes for the one τ that
    previously got through — and `gb === ct₁`-telescopers always, so no cofactor chain is ever
    needed. `work/lb5/certQ2.wl`, `certQ3.wl`.
  * **What now blocks it is exactly ONE stage** (§18.18). Of the five stages, `Annihilator`,
    the `l`-elimination, the Gröbner step and `DFiniteTimes` are all **clear on every τ** —
    including `kk`, whose `Annihilator` was the campaign's one hard OOM (7.8 GB) and whose
    `DFiniteTimes` returned 4 generators in 500 s at 0 GB on the largest cofactor in the problem.
    The sole remaining obstacle is the **second telescoping `ct₂`**, which has **zero returns by
    any method on any piece, ever** — `Support` ladder (×3.8 per rung, orders 0–5 excluded on the
    smallest object) and **unconstrained** telescoping with no ansatz box (600 s, no return).
  * **And `ct₂` cannot be fixed by splitting, because splitting is what breaks it** (§18.13).
    `guessrec.py` measures the point directly: `Σ T·ŵ₃` and `Q_n` each have a unique minimal
    recurrence of order 3, degree 9 (= `L_BZ`), while **every single-letter component sum has
    none with order ≤ 12 and degree ≤ 30**. The order-3 collapse is a property of the
    **combination** and is destroyed by any decomposition, so `ct₂` has been searching boxes that
    are empty. This measurement has been on file since §5.1 and its implication for the split
    routes was never drawn. **The strategic verdict is: stop splitting.**
  * **A new gap, honestly recorded:** the letter split inserts a `DFiniteTimes` stage that the
    written assembly/verification chain (`certPy.wl`/`certPv.wl`) knows nothing about, so that
    chain no longer applies verbatim. §18.5 closes the design with the **φ-shift decomposition**
    `O.(λS) = λ(O.S) + (O_φ.S)`, `φ` rational (tabulated and cocycle-checked in `phi_tables.m`);
    it is `[SPECIFIED, NOT IMPLEMENTED]` and is the last mile.
  * **(T1-top) — a second, independent structural reason not to grind it** (§18.6). The
    letter-split's lever is the **`l`-free fraction of the support**, and that fraction is
    **67 % for `ŵ₃` but only 12–17 % for every weight-5 representative**. `E(w₅^I)` becomes
    **165 rank-1 problems plus 355 remnants at `l`-rank 4, 8 and 16**, against Theorem B's
    13 + 4 with every remnant at `l`-rank 2. Costed against the one calibration point available,
    the rank-1 *half* alone is **≳ 96 kernel-hours**, and no elimination of rank ≥ 2 has ever
    returned in this campaign. Even `w5_Rbase` (the best representative, support 100) is
    85 + 210. `[BLOCKED BY A STRUCTURAL OBSTRUCTION]` stands, now on two independent grounds.
  **P1e update (2026-07-25, session 6 — `work/PHASE2_CERTS.md` §19).**
  * **Theorem B — still `[NOT CERTIFIED]`, and the `E`-route is now closed for a STRUCTURAL
    reason.** §18.17's calibration gap (`Annihilator` measured at 9 symbols and at 0, nothing at
    7) has been filled by the `REFOLD` representative `ṽ`, and the answer is negative:
    `Annihilator[E(ṽ)]` **MEMORY ABORT at 5.0 GB / 478 s** and, rerun on an empty box,
    **at 8.5 GB / 536 s**, with memory rising a straight **3.6 GB per minute**. That is *worse
    per unit time* than the 9-symbol `F_kk` (7.8 GB after 85 min). The two-symbol gain buys
    nothing.
  * **Why, and why it cannot be repaired by any further refolding.** §18.2's "the cost driver is
    the letter count" was measured at **fixed `LeafCount`** and is only half the law: `T·v`
    carries **12** letters and its coefficients are trivial; `E(ṽ)` carries **7** and its
    coefficients are `Θ(ρ, σ)`. And `E(w) = Σ_τ G_τ(τ.w − w)` has `G_kk = −ρ|_{k+1}T(k+1)` and
    `G_ll = −σ|_{l+1}T(l+1)`, so shedding `ρ, σ` would require `w` invariant under `k → k+1`
    **and** `l → l+1` — i.e. `w = w(n)`, which the weight-3 fit excludes. **The obstruction lives
    in the Q-row certificate, not in the weight**, hence it is invariant under every refold.
    §4quater's reduction, the τ-split, the letter-split and the refold are all blocked by the
    same thing.
  * **One route remains, and it is the one that never forms `E`:** telescope `T·w` directly,
    where the coefficients are polynomial and the `ct₂` box is the known, *occupied* `(3,9)`
    (`guessrec`: the combination has the unique order-3 degree-9 operator `L_BZ`; the pieces have
    none). `ṽ` is the best object it has been offered — 10 symbols, `LeafCount` **91**, and **no
    `C` letter**, so its whole `l`-side content is the single letter `A₂(l)`. Measured this
    session: `Annihilator[T·ṽ]` stopped on a **2.5 GB cap I had set defensively**, after 1991 s,
    with RSS growing **0.036 GB/min — a hundredfold flatter than `E(ṽ)`**, i.e. computing rather
    than diverging. A properly-resourced rerun (9 GB, 5400 s) was in flight at hand-off.
  * **⚠ A correction that invalidates part of the campaign's cost model.** §1's
    `Annihilator[T·v] = 124 s, 7 generators` **does not reproduce**: the identical object, under
    a correctly-timed `stage`, did not return in 600 s. §17.5 gives the reason — before the
    `HoldRest` fix, `stage`'s `t=…s` was **`Put` time, not stage time**. Every pre-fix timing in
    §1/§5.2 must be treated as an artifact, and no schedule should be planned against them.
  * **Everything downstream of a certificate is now discharged in advance** (§19.5): `ŵ₃ − ṽ` is
    in the **PROVED** kernel (so certifying `ṽ` certifies Theorem B), `Σ T·ṽ = P̂_n` exactly for
    `n ≤ 33` with `L_BZ·(Σ T·ṽ) = 0` for `n ≤ 30`, the far-edge boundary vanishes at every cell
    tested, **301** exact initial values are banked (any `ord(M) ≤ 298` closes it), and the
    assembly + RISC-free verification chain is written and smoke-tested (`certRFy.wl`,
    `certRFv.wl`). Newly `[CERTIFIED RISC-free and symbolic]`:
    `E(ṽ)/T = c₀ + β(A₂(l) − A₂(k)) + α·Ψ_k`, and `REFOLD` §4.6's four shift tables.
* **Node 2 — the digit-scaled induction. `[SPLIT in v2 — see work/PHASE2_INDUCTION.md]`**
  It is **not** bookkeeping. Written out, it separates into
  * **`[PROVED-here (P1d)]`** the multi-digit depth bound **(DEPTH-gen)** via Prop. LIFT
    (`PHASE2_INDUCTION` §2) — hence the unconditional Theorem 5.1, `ord_p(P_n) ≥ −5L−1`
    for all `n`;
  * **`[PROVED-here (P1d)]`** **Lemma F-gen**, Lemma F at multi-digit `a` in the weak form the
    induction consumes (`PHASE2_INDUCTION` §3): `v_p(𝒯 − Q_r T(a,b,c)) ≥ 1+min(α+γ+κ,2)`,
    for *all* `a ≥ 1`, with no `p ∤ Q_a` hypothesis and without Lemma Phi;
  * **`[PROVED-here (P1d)]`** the induction step's budget: the two above meet with slack
    **exactly 0** at every digit level (`PHASE2_INDUCTION` §4.2), and the in-regime letter
    descent costs nothing (§4.3);
  * **`[PROVED-here (P1h), v3]` `(BASE)`** — see `work/PHASE2_NUCLEUS.md` and the v3 note at the
    top of this file. The v2 text below is retained as the record of why it was hard.
    `[OPEN in v2]` `(BASE)` — `ord_p(P_n) ≥ 0` for `n < p`. `[VERIFIED 11 884/11 884]`, every
    prime `5 ≤ p ≤ 367`. The brief's proposed proof does not exist (the letters *do* reach
    `2n`, `3n`); the cell-wise bound is `−1`, attained; and the deficit is **provably not
    removable by any `p`-independent choice of `w₅`** — both strengthened depth systems
    `(DEPTH⁺)` (all patterns) and `(DEPTH⁺⁺)` (only the three `α+γ+κ = 2` patterns) are
    **inconsistent** with the fitting system at both auxiliary primes. `(BASE)` requires a
    genuine cancellation across cells (it is global in `(b,c)`: row sums are still `−1`).

    **P1g update (`work/PHASE2_RLETTER.md`, 2026-07-25).** The alphabet enlargement that
    `PHASE2_CANCEL` §7.1 recommended has been run at full scale and **does not close it**:
    Apéry-type letters `R^{(a)}(n,k) = Σ_{m≤k}(−1)^{m−1}/(m^aC(n,m)C(n+m,m))` (all weights, both
    slots, 1 210 basis coefficients, `rank(fit)` `313 → 960`) and nested interval letters
    `Y_{a,b}, V_{a,b}` (pole order `max(a,b) < a+b`) leave the strengthened system
    **inconsistent** at `N = 1300`. The refutation is for the `p`-independent,
    *symbol-independent* form of the depth conditions; the prime-by-prime "honest" form is
    `[OPEN]` and costed in `PHASE2_RLETTER` §8. Two positives replace it:
    * **partial closure** — an explicit 155-term *harmonic* representative `w₅^I`
      (`work/p1g/w5_I.json`) is cell-wise `p`-integral **outside one band**
      `III = {k,l ≥ q = p−n, p ≤ k+l < p+q}`, so `(BASE) ⟺ Σ_III ≡ 0 (mod p)` — one region
      instead of two. `[VERIFIED exact: identity n ≤ 20; 10 092 cells, p = 5..23, 0 violations]`
    * **the recurrence route is now one congruence per prime** — the `a₀`-root exceptional steps
      are apparent singularities of `L_BZ`, leaving only `(REC-★)` at `n₀ = (p−5)/2`.
      `[VERIFIED 82 steps / 44 primes, 0 failures; 107 apparency tests, p < 600]`
  * **`[PROVED-here (P1i), v4]` `(GAP-DESC)`** — the off-regime descent term, at **every** digit
    level (not only `a ≥ p`): `work/PHASE2_GAPDESC.md`. `(DEPTH-gen)` at level `n` and at level
    `a` charge `1+min(s_n,2)` and `1+min(s_a,2)`; Lemma DK pays both at once,
    `v_pT(n,k,l) ≥ 1 + max(s_n,s_a)`, because off-regime means a base-`p` carry in **position 0**
    while the depth pattern lives in **position `L ≥ 1`**.
    `[VERIFIED 188 353 733 off-regime cells, L = 1,2,3,4, 0 failures, slack 0 attained]`
    `[OPEN in v2–v3]` the text below is retained as the record of what was expected:
    *"the off-regime letter descent for `a ≥ p` (`PHASE2_INDUCTION` §6.2): a carry-bookkeeping
    lift of `endgame` §R3 with one order of slack available. No new mechanism."* — **that route
    is refuted** (`PHASE2_GAPDESC` §5): the letter-wise mismatch of `A_m(k)` costs `mλ` against a
    Kummer gain of `1+λ`, so it loses at weight 5; the pole is instead killed inside `v₅` by the
    `(DEPTH)` conditions at level `n`. Lemma D++ is **not** needed for this node.

  **Unified form of the residue `[SUPERSEDED in v3–v4]`.** `(BASE)` and the induction step were
  the same statement at different digit levels — the pair of mod-`p` identities
  `Σ (T/p)·K_{5L+2} ≡ 0`, `Σ (T/p²)·K_{5L+3} ≡ 0` (`PHASE2_INDUCTION` §6.3), one power of `p`
  deep. Both halves are now proved — `(BASE)` by the midpoint split (P1h) and the induction step
  by Lemma F-gen + Lemma DK (P1d + P1i) — so **the two decomposition certificates are all that
  separates Phase 2 (`p ≥ 5`) from a theorem.**

### D.2 For `p ∈ {2,3}` — the July H2 remnant

The global factor `12 = 2²·3` is *not* covered by anything above; `p ≥ 5` is forced by the
single use of Wolstenholme inside Lemma W. The `p = 2` part rests on an index-2 computation
whose status is recorded in `/home/ubuntu/fable-episode-2/zeta-math/worthiness/H2_SIGNS.md`
(read-only, task CR-4). Its own bottom line, quoted:

> **CR-4 is sharpened, not discharged.** The `H2_LATTICE §5.5` reading (factor 2 on the Betti
> side, via `B` + measurement) stands unchallenged and is now supported by two further rigorous
> facts (A-side no-go; `p=3` derivation) and one new geometric structure (the `Z3`/`Z6`
> A-meets-B locus). The claim "index 2 derived from geometry alone" is **not** yet earned; the
> honest status is "index 2 is the unique value consistent with all closed sub-computations,
> with the sole open input being the integral bicomplex differential at two explicitly
> identified strata."

Concretely, of the three sub-results there: `[PROVEN]` the factor 2 is **absent** from the
A-arrangement combinatorics (all Smith elementary divisors 1, under *every* orientation
convention); `[PROVEN]` `p = 3` is trivial (only the prime 2 can arise from these incidence
matrices — so **the `3` in the `12` needs a different source, or is not there**);
`[NOT CLOSED]` the `2` itself, localised to the integral weight spectral-sequence differential
across the uncolored generic facets on the two strata `Z3 = d24∩d36`, `Z6 = d14∩d36`, i.e. to
the unpublished integral refinement of Dupont's ℚ-only bicomplex (`[CR-4c]`).

So the `p ∈ {2,3}` statement that remains is:

> **(SHARP-12, `p ∈ {2,3}` part).** `ord_2(P_n) ≥ −2 − 5⌊log_2 n⌋` and
> `ord_3(P_n) ≥ −1 − 5⌊log_3 n⌋`, i.e. the *constant* `12 = 2²·3` and nothing worse.
> `[VERIFIED 361/361, n ≤ 360]`; the `2`-part is reduced to `[CR-4c]` above and the `3`-part
> currently has **no** derivation at all (H2_SIGNS `[PROVEN]` says the geometry cannot produce
> a 3, so the source of the factor 3 is unidentified).

---

## E. Reproduction

P1c artefacts are in `work/lb5/` (see `work/PHASE2_FINAL.md` §3); **P1d artefacts are in
`work/p1d/`** (new directory; nothing in `work/lb5/` was modified). The decisive ones:

| artefact | what it settles |
|---|---|
| `work/lb5/solve_depth.py` output | consistency of (DEPTH): `rank(joint) = rank(aug) = 324`, both primes |
| `work/lb5/w5_allp.json` | a depth-minimal `w₅` with denominators `{2,3}` — usable at every `p ≥ 5` |
| `work/lb5/verify_depth.py w5_allp.json` | V1 ladder `n ≤ 22`, V2 depth sweep `p ≤ 31`, V3 cell-by-cell (GAP-5) `p ≤ 13`: **0 / 0 / 0** |
| `work/p1d/exp3.py` | **(DEPTH-gen)** + Lemma K at digit levels `L ≤ 2`: 150 955 cells, **0** violations, min slack 0 |
| `work/p1d/exp7.py` | **Lemma F-gen** at multi-digit `a`: 112 000 cells, **0** failures, min slack 0 |
| `work/p1d/exp8.py` | **Lemma B for general `a`**: 8 247 294 in-regime cells, **0** failures |
| `work/p1d/solve_strong.py strong \| vt2` | **(DEPTH⁺)/(DEPTH⁺⁺) are INCONSISTENT** — the base-case deficit is irremovable |
| `work/p1d/basecase.py` | `(BASE)` over every prime `5 ≤ p ≤ 367`: 11 884 cells, **0** failures |
| `work/p1d/sweep.py` | (SHARP-12) sweep: `n ≤ 360` (3 240 cells) and `n ≤ 3000` (27 000 cells), `p ≤ 31`, **0** failures |

**P1h artefacts** are in `work/p1h/` (`(BASE)`; see `work/PHASE2_NUCLEUS.md` §7).
**P1i artefacts are in `work/p1i/`** (new directory; nothing elsewhere was modified):

| artefact | what it settles |
|---|---|
| `work/p1i/pad.py`, `t0_check.py` | exact `p`-adic arithmetic with tracked precision; cross-checked against `Fraction` on 1 290 cells, **0** mismatches |
| `work/p1i/s4_carry.py`, `s9_lvl4.py` | **Lemma DK** + Lemma D1: **188 353 733** off-regime cells, `p ≤ 31`, `L = 1,2,3,4`, **0** failures, slack 0 attained; in-regime control fails 134 964× (as it must) |
| `work/p1i/s8_slots.py` | the slot-wise carry inequalities behind Lemma DK, one binomial at a time: 11 096 075 cells, **0** failures |
| `work/p1i/s3_exact.py lvl1\|lvl2\|lvl3` | **Theorem (GAP-DESC)** with the exact `p`-adic `𝓔`, off-regime, `L = 1,2,3`: **0** failures |
| `work/p1i/s6_allcells.py` | the whole descent term (I), **both** regimes, plus `v_p(Σ_{k,l}T𝓔)`: **0** failures |
| `work/p1i/s5_rep.py` | `(DEPTH-gen)` and (GAP-DESC) for the P1h representative `w₅^I`: **0** failures |
| `work/p1i/s7_trap.py` | the refutation of the letter-wise route (mismatch `−mλ` vs Kummer gain `1+λ`) |
