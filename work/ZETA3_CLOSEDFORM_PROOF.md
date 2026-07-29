# ZETA3_CLOSEDFORM_PROOF — an independent second proof of the b_n closed form

**Agent:** Claude (Fable), 2026-07-29 (post-closeout session).
**Code:** `work/z3cf/` (`z3proof.py`, `z3stage2.py`, certificates as json).
**Labels:** program discipline — `[PROVED]` / `[VERIFIED range]`; finite checks are never proof.

> **⚠ PRIORITY BANNER (added same session, after the fact).** This theorem was
> **already proved** in `work/MINIMAL_FORM_PROOF.md` (P4c, 2026-07-24; six
> certificates, route R1 via comparison with Apéry's classical weight),
> **already formalized** sorry-free in `lean/ZetaLucas/ZetaLucas/MinimalForm.lean`
> (`bMin_eq_bApery`, `apery_b_harmonic_closed_form`; single-telescope proof, no
> Abel step, smaller certificates T, U), and **already written up** in
> `papers_out/lucas_min`. The session below re-derived it independently without
> checking first — kept as (i) an independent verification by a structurally
> different route (direct annihilation, no reference to the classical weight;
> one Zeilberger + one generic-Gosper certificate), and (ii) a record of the
> deficit identity `Σ_{k=0}^n A·ρ = −2C(2n+2,n+1)²` and the boundary value
> `Y(n,n+1) = −2C(2n+2,n+1)²`, which do not appear in the earlier proof.
> **Lesson: grep `work/`, `papers_out/`, and the lean tree before proving.**
> The paper draft that duplicated `lucas_min` is retired to `work/z3cf/`.

## 0. Statement

> **Theorem.** `b_n = Σ_{k=0}^n C(n,k)² C(n+k,k)² · (2H⁽³⁾_n − H⁽³⁾_k)`
> where `b_n` is Apéry's second ζ(3) solution (b₀=0, b₁=6).

Provenance: the weight `2H⁽³⁾_n − H⁽³⁾_k` is the ε³ Bell coefficient `L₃` of the
three-shift Γ-deformation of APERY_DEFECT §7.1 (`u=(6,−6,2)`, `v=(−3,3,−1)`;
`L₁ = L₂ = 0` termwise, `B₃ = L₃ = 2(2H⁽³⁾_n − H⁽³⁾_k)`), rediscovered independently
by exact fitting in LBW_GENERAL T3 (the "γ line"). Until now the sum identity itself
was `[VERIFIED n ≤ 90]` only (the termwise ε-algebra is trivially proved; the value
`½[ε³]Σ A_ε = b_n` was not).

## 1. Proof structure (two-stage CT; the harmonic letter shifts rationally)

Let `A(n,k) = C(n,k)²C(n+k,k)²`, `W(n,k) = 2H⁽³⁾_n − H⁽³⁾_k`, `F = A·W`,
`L = (n+1)³ S_n − (2n+1)(17n²+17n+5) + n³ S_n⁻¹` (Apéry's operator, acting in n).

**Split (exact, from W(n±1,k) = W ± 2/(n+1)³, −2/n³):**

    L F(n,k) = [L A](n,k)·W(n,k) + 2A(n+1,k) − 2A(n−1,k).

**Stage 1 [PROVED].** Zeilberger's classical certificate, here recovered by exact
sampled linear solve + symbolic holdout (0 mismatches on a fresh grid):

    [L A](n,k) = G(n,k+1) − G(n,k),   G = A·R,
    R(n,k) = 4k⁴(2n+1)(2k² − 3k − 4n(n+1)) / ((n+1−k)²(n+k)²).

Pointwise validity: `LA = ΔG` holds at EVERY integer cell 0 ≤ k ≤ n+2, including
the boundary continuation value `G(n,n+1) = C(2n+1,n+1)²·N(n,n+1)/((n+1)²(2n+1)²)`
(N = numerator of R) `[VERIFIED n ≤ 7 all cells, exact]` — no bad cells at all.

**Abel summation** (boundaries vanish: `G(n,0) = 0` since `k⁴ | N`; `G(n,k) = 0`
for k ≥ n+2):

    L c_n = Σ_{k=0}^{n} G(n,k+1)/(k+1)³ + 2(a_{n+1} − a_{n−1}),
    c_n := Σ_k A·W.

**Stage 2 — the remaining identity is purely hypergeometric** (no harmonic letters):
with `ρ(n,k) := N(n,k+1)/(k+1)⁷ + 2[(n+1+k)²/(n+1−k)² − (n−k)²/(n+k)²]`
(the exact rational simplification of `G(n,k+1)/(k+1)³·A(n,k)⁻¹ + 2(A(n±1)/A)`),

    (T)  Σ_{k=0}^{n} A(n,k)·ρ(n,k) = −2·C(2n+2,n+1)²
    [VERIFIED exact, n = 2..13, 0 failures]

(the RHS is the k = n+1 term of `2a_{n+1}` that the k ≤ n range misses).
Given (T): `L c_n = 0` for n ≥ 1; with `c₀ = 0 = b₀`, `c₁ = 6 = b₁` and the same
second-order recurrence, `c_n = b_n` for all n. ∎ (modulo (T))

**Stage 2 [PROVED — Gosper certificate found and verified symbolically].**
sympy `gosper_term` on `t(k) = A·ρ` returned an explicit rational `g(n,k)`
(stored: scratchpad `gosper_g.txt`; denominator of `g·ρ` after cancellation is
`n²(n+1)²(k+n)²(k−n−1)²` — no interior poles on 1 ≤ k ≤ n). Verified as EXACT
RATIONAL IDENTITIES (sympy `cancel`, zero remainder):

    ρ = rA·(gρ)(k+1) − (gρ)(k)          [the antidifference identity]
    (gρ)(k=0) = 0                        [lower boundary]
    lim_{k→n+1} (n+1−k)²·(gρ) = −8(n+1)² [upper boundary, symbolic in n]

Since `A(n,k) → C(2n+1,n+1)²(k−n−1)²/(n+1)²` at k → n+1 and
`C(2n+2,n+1) = 2C(2n+1,n+1)`, telescoping gives exactly
`Σ_{k=0}^n A·ρ = y(n+1) − y(0) = −8·C(2n+1,n+1)² = −2·C(2n+2,n+1)²` — identity (T).

**The theorem is therefore PROVED**: two rational-function certificates
(Zeilberger's classical R for `a_n`, the Gosper g for the correction sum), four
boundary evaluations, and second-order induction from `c₀ = 0, c₁ = 6`.

## 1b. THE LEAN-READY FORM (final; everything cellwise, no continuations)

One binomial shell for both certificates (`C` = binomial, ℚ-valued via cast):

    X(n,k) := C(n+1,k)² · C(n+k−1,k)²          (vanishes for k ≥ n+2 automatically)
    N(n,k) := 4k⁴(2n+1)(2k² − 3k − 4n(n+1))
    M(n,k) := 4k(2n+1)·P(n,k),
    P(n,k) := k⁵ − 2(n²+n+1)k⁴ + (2n²+2n+1)k³ + 2n²(n+1)²k² − 3n²(n+1)²k − 4n³(n+1)³
    G(n,k) := N·X / (n²(n+1)²)                  (n ≥ 1: denominator nonzero)
    Y(n,k) := M·X / (n⁴(n+1)⁴)

The two certificate identities, **valid at EVERY integer cell k ≥ 0, n ≥ 1**
(no boundary exceptions, no rational-function continuations):

    (P1)  (n+1)³A(n+1,k) − (2n+1)(17n²+17n+5)A(n,k) + n³A(n−1,k) = G(n,k+1) − G(n,k)
    (P2)  G(n,k+1)/(k+1)³ + 2A(n+1,k) − 2A(n−1,k) = Y(n,k+1) − Y(n,k)

`[VERIFIED exact, 0 bad cells, n = 1..14, all k = 0..n+3]`, plus the boundary
lemmas `G(n,0) = Y(n,0) = 0` (k | N, k | M), `G = Y = 0` for k ≥ n+2 (shell),
`Y(n,n+1) = −2C(2n+2,n+1)²` (from `M(n,n+1) = −8(2n+1)²n²(n+1)⁴`, symbolic).

Proof skeleton from these: on 0 ≤ k ≤ n+1, X(n,k) > 0 and
`A(n,k)/X = (n+1−k)²(n+k)²/(n²(n+1)²)`, `A(n±1,k)/X` similar,
`X(n,k+1)/X(n,k) = (n+1−k)²(n+k)²/(k+1)⁴` — so (P1),(P2) each reduce to ONE
polynomial identity in ℚ[n,k]; for k ≥ n+2 every term is zero. Then:
Σ(P1)·W + Abel (ΔW = −1/(k+1)³ steps) + Σ(P2) telescoped ⟹ L c_n = 0; two
initial values close the induction. Data: `work/z3cf/` (`sol1.json` = N,
`m2.json` = M expanded, `gosper_g.txt` = raw Gosper term — superseded by M).

## 2. Verification record

| statement | method/range | failures |
|---|---|---|
| c_n = b_n | exact ℚ, n ≤ 30 | 0 |
| stage-1 certificate (rational identity) | sampled solve n≤25 + holdout grid n=26..33 | 0 |
| pointwise LA = ΔG incl. boundary cell k=n+1 | exact, n ≤ 7, all k ≤ n+2 | 0 |
| k⁴ | N and N(n,0)=0 (boundary vanishing) | exact | 0 |
| (T) deficit = −2C(2n+2,n+1)² | exact, n = 2..13 | 0 |

## 3. Why this matters for the program

* The γ closed form was the input that made Theorem LB (LBW_GENERAL T4) a 3-line
  proof of the ζ(3) Lucas congruence; it was fit-backed. This closes it.
* Same template should prove the other three tame decompositions (A/Franel, D,
  s₁₀) — their operators are order 2, their weights depth ≤ 2 with the same
  rational-shift property; the split trick generalizes (H-letters at n and k
  only shift by explicit rationals under S_n, S_k).
* This is the "short elegant formula" route: certificate + 7-term numerator,
  no towers, no grids.
