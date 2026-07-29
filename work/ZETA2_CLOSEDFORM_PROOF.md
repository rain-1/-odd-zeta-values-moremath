# ZETA2_CLOSEDFORM_PROOF — the ζ(2) companion: classical form PROVED, minimal form reduced

**Agent:** Claude (Fable) fork, 2026-07-29. **Code + data:** `work/z2cf/`.
**Labels:** `[PROVED]` · `[VERIFIED range]` · `[OPEN]` · `[EXCLUDED]` — finite checks are never proof.

Setting: `S(n,k) = C(n,k)²C(n+k,k)` (the ζ(2)-Apéry summand, A005258 row),
`L u = (n+1)²u_{n+1} − (11n²+11n+3)u_n − n²u_{n−1}`, `B` the second solution
(`B₀ = 0, B₁ = 1`, `B_n/a_n → ζ(2)/5`), `w_min = (1/5)[H⁽²⁾_n + H_k(2H_k − H_{n−k} − H_n)]`
(the LBW_GENERAL T3 fitted weight; target closed form `B_n = Σ_k S·w_min` — §8.5 of
MINIMAL_FORM_PROOF proved the rank-2 template FAILS for it).

## 0. HEADLINE

1. **[PROVED] The classical-form closed form** (new to the program; self-derived, no
   literature input):

   > **`5·B_n = Σ_{k=0}^n S(n,k)·w_cl(n,k)`,**
   > **`w_cl = 2Σ_{m≤n}(−1)^{m−1}/m² + Σ_{m≤k}(−1)^{n+m−1}/(m²C(n,m)C(n+m,m))`**

   — the ζ(2) analog of the van der Poorten/Apéry ζ(3) companion formula. Proof =
   recurrence + initial values; the recurrence by an explicit certificate chain (§2)
   whose final step collapses to `W(n,k) = 3 − 3(n+1)/(n+1−k)` and two one-line
   binomial facts. The ζ(2) **miracle** is `k² + (n+1−k)(n+1+k) = (n+1)²`.

2. **[PROVED] Reduction of the minimal form.** `B_n = Σ S·w_min` for all n **⟺**

   > **(L2)  `L A = −a_{n+1} − a_{n−1}`,  `A_n := Σ_k S(n,k)·H_k(2H_k − H_{n−k} − H_n)`**

   (via `L(H⁽²⁾_n·a_n) = a_{n+1} + a_{n−1}`, an exact two-line computation, plus
   initial values A₀ = 0, A₁ = 2). Given 1., also ⟺ `Σ_k S·(5w_min − w_cl) = 0`.

3. **(L2) remains [OPEN]; three certificate classes [EXCLUDED]:** (i) §8.5's
   decoupled post-Abel Gosper (proved obstruction, prior work); (ii) one-shot
   coupled S-shell certificates, 13/19 letter channels over args {k,n−k,n,n+k},
   3 denominator/degree configs (parent session, rank-saturated, 220–1367 bad rows);
   (iii) same + residue-null gauge library at levels n−1,n,n+1 (8 ρ-families × 3
   levels, μ-deg ≤ 6): rank 1778/1840, **482 bad rows** (`lemma2_sweep.py`).
   Structural diagnosis (parent session): LF of the minimal form is pure S-shell;
   telescopes of S·(rational×harmonic) stay S-shell; the alternating shell
   `U = (−1)^{n+k}C(n,k)` — which is what makes the w_cl proof work — can enter
   only through the weight, and w_min has no tail. **The tail is irremovable at
   certificate level**; (L2) needs either a genuinely new null family or a new
   mechanism (ΠΣ/Sigma-style, or a Beukers-integral evaluation).

## 1. The objects and the miracle `[PROVED]`

`g_m(n) := 1/(m²C(n,m)C(n+m,m)) = ((m−1)!)²(n−m)!/(n+m)!`; `τ(n,k) := Σ_{m=1}^{min(k,n)}
(−1)^{n+m−1}g_m(n)`; `e(n) := Σ_{m≤n}(−1)^{m−1}/m²`; `w_cl = 2e + τ`; `σ := (−1)^n`;
`γ(n,k) := (−1)^k(k!)²(n−k)!/(n+k+1)!`.

**Miracle shifts.** For `0 ≤ k ≤ n` (resp. `0 ≤ k ≤ n−1`):

    τ(n+1,k) − τ(n,k) = σ·(2/(n+1))·(γ(n,k)   − 1/(n+1))
    τ(n−1,k) − τ(n,k) = σ·(2/n)    ·(γ(n−1,k) − 1/n)

*Proof.* `(−1)^m[g_m(n+1) + g_m(n)] = 2(n+1)(−1)^m((m−1)!)²(n−m)!/(n+m+1)!`
(one-line factorial computation), and with `P = 2/(n+1)`:
`γ(n,m) − γ(n,m−1) = (−1)^m((m−1)!)²(n−m)!/(n+m+1)!·[m² + (n+1−m)(n+1+m)]
= (n+1)²·(…)` — **the miracle** — so the m-sum telescopes. The backward shift is
the same statement at `n−1`. ∎  `[VERIFIED 0 fails, all cells n ≤ 15]`

**Corollary (rational σ-parts cancel):**
`w_cl(n±1,k) = 2e + τ + σ·(2/(n+1 resp. n))·γ(n resp. n−1, k)`.

## 2. Lemma 1: `L(Σ_k S·w_cl) = 0` for n ≥ 1 `[PROVED]`

Chain (each link machine-verified, `lemma1_final.py`, 0 fails):

* **(SPLIT)** For `0 ≤ k ≤ n−1`:
  `LF_cl(n,k) = LS(n,k)·w_cl(n,k) + U(n,k)·RHSU(n,k)`,
  `U = (−1)^{n+k}C(n,k)`, `RHSU = 2(n+1)²/(n+1−k)² − 2(n−k)/(n+k)`.
  From the miracle + the conversions `S(n+1,k)γ(n,k) = (−1)^kC(n+1,k)/(n+1−k)`,
  `S(n−1,k)γ(n−1,k) = (−1)^kC(n−1,k)/(n+k)` (absorption identities).
* **(CERT)** `LS(n,k) = G_D(n,k+1) − G_D(n,k)` for **all** k ≥ 0, with the shell form
  `G_D = k³·ρ_D·C(n+1,k)²C(n+k−1,k)/(n(n+1)²)`, `ρ_D = k²+k(1+6n)−4−15n−11n²`
  (§8.5's certificate; here re-verified cellwise INCLUDING the continuation cells
  k = n, n+1, and symbolically as one rational identity — sympy cancel = 0).
* **(ABEL)** Sum over k = 0..n+1; boundaries `G_D(n,0) = 0` (k³), `G_D(n,n+2) = 0`
  (C(n+1,k)); `Δτ(n,k) = (−1)^{n+k}g_{k+1}(n)` for k ≤ n−1, else 0; the conversion
  `G_D(n,k+1)·(−1)^{n+k}g_{k+1} = −U(n,k+1)·ρ_D(n,k+1)/((n−k)(n+k+1))·(…)` collapses
  (`S(n,k+1)g_{k+1}(n) = C(n,k+1)/(k+1)²`).
* **(BOUNDARY)** the two cells k = n, n+1 evaluate to `b₁ = 2(n+1)²` and `b₂ = 3`
  exactly (displayed derivations in note.tex; the `3` comes out of
  `−1 + 4 = 3` via `C(2n+2,n+1)(n!)² = (2n+2)!/(n+1)²`).
* **(Λ)** What remains is ONE alternating sum identity:
  `Σ_{k=0}^n(−1)^kC(n,k)·W(n,k) = 3(−1)^{n+1}` with
  `W = 2(n+1)²/(n+1−k)² − 2(n−k)/(n+k) + k·ρ_D(n,k)/((n+1−k)²(n+k))`.
  **Collapse [sympy, exact]:** `W(n,k) = 3 − 3(n+1)/(n+1−k)` — the (n+k)-pole and
  the double (n+1−k)-pole cancel identically (the latter is §8.5's boundary
  identity `ρ_D(n,n+1) = −2(n+1)(2n+1)` at work). So (Λ) follows from
  `Σ(−1)^kC(n,k) = 0` (n ≥ 1) and
  `Σ_k(−1)^kC(n,k)/(n+1−k) = (−1)^n/(n+1)` (swap k ↦ n−k, then
  `C(n,k)/(k+1) = C(n+1,k+1)/(n+1)` and the binomial theorem). ∎

**Theorem 1 [PROVED].** `Σ_k S(n,k)w_cl(n,k) = 5B_n` for all n ≥ 0.
*Proof.* Lemma 1 + `(n+1)² ≠ 0` + initial values v₀ = 0, v₁ = 5 (= 5B₁). ∎

## 3. Verification record

| # | statement | method/range | fails |
|---|---|---|---|
| V1 | `Σ S·w_cl = 5B` | exact ℚ, n ≤ 25 | 0 |
| V2 | miracle shifts, both directions | exact, all cells n ≤ 15 | 0 |
| V3 | (SPLIT) | exact, all 0 ≤ k ≤ n−1, n ≤ 13 | 0 |
| V4 | (CERT) cellwise all k ≤ n+2, n ≤ 14 | exact | 0 |
| V5 | (CERT) as one rational identity | sympy cancel | =0 |
| V6 | assembly Lv = Abel + U-sum + Bd; Lv = 0 | exact, n = 2..25 | 0 |
| V7 | (Λ) | exact, n = 2..30 | 0 |
| V8 | b₁ = 2(n+1)², b₂ = 3 | exact n = 2..8 + displayed derivation | 0 |
| V9 | `W = 3 − 3(n+1)/(n+1−k)` | sympy apart, symbolic | exact |
| V10 | (L2) ⟺ closed form; A₀=0, A₁=2 | exact algebra + n ≤ 25 | 0 |
| V11 | (L2) certificate sweeps | 3 classes | EXCLUDED (see §0.3) |

## 4. What would close (L2)

Sharpest formulation: `Σ_k S(n,k)·j(n,k) = 0` with
`S·j := LF_X + S(n+1,k) + S(n−1,k)`, `X = H_k(2H_k − H_{n−k} − H_n)` — pure S-shell,
weight ≤ 2, alphabet {k, n−k, n}. Candidate mechanisms not yet exhausted:
(a) a new proved null family carrying l-free… (here: k-free) content — the moment
ladder for THIS kernel (`R(z) = n!∏(z+i)/∏(z−j)²`, residues at ∞ of `z^m R·ρ` for
m ≥ n−1, which are NONZERO and explicit — the inhomogeneous rows the sweep lacked);
(b) Sigma-style ΠΣ telescoping (Schneider proved the ζ(3) analog mechanically;
Sigma.m is NOT in RISC/ here); (c) evaluating Beukers' double integral
`∫∫ x^n(1−x)^n y^n(1−y)^n/(1−xy)^{n+1}` by partial fractions into the w_min shape
directly (the historical route to such weights). (a) is specced for a next session;
it is exactly the mechanism that closed the weight-5 grids in Z5T3_BRIDGE §4b.

## 5. Files

| file | what |
|---|---|
| `z2cf/lemma1.py` | discovery run: miracle check, split, joint solves |
| `z2cf/lemma1_final.py` | the complete Lemma-1 chain, all verifications |
| `z2cf/lam_symbolic.py` | the W-collapse (sympy apart) |
| `z2cf/lemma2_sweep.py` | (L2) 3-level null sweep [EXCLUDED result] |
| `z2cf/note.tex` | Bourbaki-style note: Theorem 1 with full proof + the reduction |
| `z2cf/z2direct.py` | letter-algebra engine (from parent session) |
