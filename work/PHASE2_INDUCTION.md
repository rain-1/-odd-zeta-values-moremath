# P1d — the digit-scaled induction: base case, level-lifting, and the exact remaining gap

**Author:** mathematician-agent (River's odd-zeta program), task P1d
**Date:** 2026-07-25
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`
**Predecessors (authoritative):** `work/PHASE2_THEOREM.md` (the assembled statement),
`work/PHASE2_FINAL.md` (the `(GAP-5)` closure, `w5_allp.json`, the (DEPTH) certificate),
`work/PHASE2_ENDGAME.md` (Lemma F, Lemma Phi, Lemma B, Lemma D++),
`work/PROOF_LB5_CAMPAIGN.md` (Theorem A, Theorem C, Lemma D), `work/PADIC_SEAM.md` §T3.

**Labels.** `[PROVED]` complete proof written out here or in a named file · `[VERIFIED r]` exact
finite check on range `r`, 0 failures (evidence, never proof) · `[CERT]` machine linear-algebra
certificate re-checked at two primes · `[GAP]` not settled, stated precisely.

---

## 0. HEADLINE

Three things changed. One of them is a hard negative.

1. **The base case is NOT provable the way the brief proposed, and the reason is structural.**
   For `n < p` the harmonic letters of `w₅` *do* reach the arguments `2n` and `n+k+l ≤ 3n`, so
   they *do* have poles at every prime `p ≤ 3n`; the cell-by-cell bound that the depth calculus
   supplies is `ord_p(P_n) ≥ −1`, **exactly one power short**, and the shortfall is **attained**
   at explicit cells (`(n,k,l) = (a,0,a−1)` with `a = (p+1)/2`, at every `p`). Worse: the deficit
   **cannot be removed by any choice of representative** cut out by `p`-independent linear depth
   conditions — the strengthened system `(DEPTH⁺)` (`d₅ ≤ v_p T` instead of `d₅ ≤ 1+min(v_pT,2)`)
   is **INCONSISTENT** with the fitting system (rank jumps from 324 to 342 and the augmented
   system is inconsistent, at both auxiliary primes — §6.1; and it is inconsistent already when
   *only* the three `α+γ+κ = 2` patterns are tightened). So the base case genuinely requires
   an **aggregate cancellation**, and it is not bookkeeping. **`[GAP-BASE]`**, stated exactly in
   §6.1. `[VERIFIED 11 884/11 884: every prime 5 ≤ p ≤ 367, every n < min(p,361), 0 failures]`.

2. **The induction itself is now essentially built, and two of its three new ingredients are
   PROVED.** The correct inductive statement is the scaled one (§4.1); it needs three inputs at
   each digit level, of which
   * **(DEPTH-gen)** — the multi-digit depth bound `d₅(n,k,l) ≤ 5L + 1 + min(v_pT(n,k,l),2)` — is
     **[PROVED]** here (§2), by a *level-lifting* proposition: the 42 single-digit (DEPTH)
     conditions of `PHASE2_FINAL` §2.3 are **level-independent**, i.e. the very same linear
     conditions that give `d₅ ≤ 1+min(vT,2)` at `L = 0` give `d₅ ≤ 5L+1+min(vT,2)` at every `L`.
     No new linear algebra, no new certificate. `[VERIFIED 0/150 955 cells]`
   * **(F-gen)** — Lemma F for **multi-digit** `a`, in the weak form the induction actually needs
     — is **[PROVED]** here (§3), with a proof that is *shorter* than the sharp single-digit one
     and, remarkably, **does not use Lemma Phi at all**, and needs **no `p ∤ Q_a` hypothesis**
     (so the exceptional primes cost nothing). `[VERIFIED 0/111 963 cells]`
   * **(G-gen)** — the letter-descent error — is proved **in-regime** (§4.3) and is **`[GAP]`**
     off-regime (§6.2).

3. **A new theorem falls out on the way**, valid for *all* `n` (not just `n < p²`) and
   unconditional given the two standing inputs of Phase 2 — (T1-top) `[VERIFIED]` and the
   (DEPTH) linear certificate `[CERT]` — which is what the [SKETCHED] node never delivered:
   > **Theorem 5.1 `[PROVED]`.** For every prime `p ≥ 5` and every `n ≥ 1`,
   > `ord_p(P_n) ≥ −5⌊log_p n⌋ − 1`.
   i.e. `d_n⁵ · rad₅(3n) · P_n ∈ ℤ[1/6]`, where `rad₅(3n) = ∏_{5≤p≤3n} p`. The sharp law is
   exactly this **minus one radical**. Before this session nothing at all was proved for `n ≥ p²`.

**Verdict on the P1d node.** The `[SKETCHED]` node does **not** flip to `[PROVED]`. It splits, and
the split is the useful result: the "bookkeeping" half is now genuinely proved and the residue is
**one** clean statement — `(V2)–(V3)` of §6.3 — which is simultaneously the base case *and* the
per-level obstruction, i.e. **the base case and the induction step are the same statement at
different levels.** That is the sharpest formulation of the remaining gap this program has.

**Sweep (as required).** `ord_p(P_n) ≥ κ(n) − 5L(n)` for `p_n = C(2n,n)P_n` (equivalently
`ord_p(P_n) ≥ −5L`): `[VERIFIED 3240/3240]` exact ladders `n ≤ 360`, `p ≤ 31`, 0 failures, and
`[VERIFIED 27 000/27 000]` `n ≤ 3000` via the certified order-3 recurrence, 0 failures, min slack
exactly 0 (§5.3).

---

## 1. Objects, normalisation, and what is quoted

`T(n,k,l) = C(n+k,n)C(n,k)²C(n+l,n)C(n,l)²C(n+k+l,n)`, `Q_n = Σ_{k,l} T(n,k,l) ∈ ℤ`
(`work/PROOF_LB5_CAMPAIGN.md` §1). `H^{(m)}_N = Σ_{i≤N} i^{−m}`, `d_n = lcm(1,…,n)`,
`L = L(n) = ⌊log_p n⌋ = v_p(d_n)`, `κ(n) = v_p C(2n,n)`, `p_n = C(2n,n)·P_n`, so

> `ord_p(p_n) ≥ κ(n) − 5L(n)  ⟺  ord_p(P_n) ≥ −5L(n)`.

Everything below is stated in the `P_n` normalisation.

**(T1-top)** `[VERIFIED]` `P_n = Σ_{k,l} T(n,k,l)·w₅(n,k,l)` with `w₅ = w5_allp`
(`work/lb5/w5_allp.json`, 178 terms, denominators supported on `{2,3}`), a **homogeneous
weight-5** ℚ-combination of monomials in the alphabet

| letter | value at level `n`, cell `(k,l)` | weight |
|---|---|---|
| `A_m(k)` | `H^{(m)}_{n+k} − H^{(m)}_k` | `m` |
| `A_m(l)` | `H^{(m)}_{n+l} − H^{(m)}_l` | `m` |
| `B_m(k)` | `H^{(m)}_{n−k} − H^{(m)}_k` | `m` |
| `B_m(l)` | `H^{(m)}_{n−l} − H^{(m)}_l` | `m` |
| `C_m` | `H^{(m)}_{n+k+l} − H^{(m)}_{k+l}` | `m` |
| `N_m` | `H^{(m)}_n` | `m` |

`1 ≤ m ≤ 5`, caps `(5,2,2)`, 448 basis monomials. Put

```
v₅(n,k,l) := w₅(n,k,l) − H^{(5)}_n ,      W_n := P_n − H^{(5)}_n·Q_n = Σ_{k,l} T(n,k,l) v₅(n,k,l),
d₅(n,k,l) := max(0, −v_p v₅(n,k,l)).
```

**Quoted, proved elsewhere, and used below.**

* **Theorem A** (`campaign` §2) `[PROVED, all a ≥ 0, all p]` `Q_{ap+r} ≡ Q_a Q_r (mod p)`, via
  **Lemma 4**: `T(ap+r, bp+s, cp+t) ≡ [r+s+t<p]·T(a,b,c)·T(r,s,t) (mod p)`. *The proof is
  uniform in `a`; this is the only mod-`p` input we need and it is already multi-digit.*
* **Lemma B** (`endgame` §R1.1) the exact fibre block factorisation. Its proof uses only the
  base-`p` digit bookkeeping of the 15 factorial slots and `m! = p^{m₁}m₁!((p−1)!)^{m₁}m₀!G(m₁,m₀)`;
  **it nowhere uses `a < p`** — see §3.2. `[VERIFIED for general a: §3.2]`
* **the (DEPTH) certificate** (`PHASE2_FINAL` §2.3) `[CERT]` rank(joint) = rank(aug) = 324 at
  `q = 33554393, 33554467`; nullity 124; `w5_allp` is a point of the depth-conditioned family.

---

## 2. (DEPTH-gen): the depth calculus at every digit level `[PROVED]`

This is the technical heart of the induction, and it is where the [SKETCHED] node's "the naive
single-step ratio depth `5−2s` goes negative" (`PADIC_SEAM` §T3.1) is repaired: the correct
multi-digit object is not a ratio at all, it is the *level-graded pole expansion* of `w₅`.

Throughout §2 fix `p ≥ 5` and `n ≥ 1`; put `L = ⌊log_p n⌋`, **`M := L+1`**, **`P := p^M`**, so
`n < P`. Fix a cell `0 ≤ k,l ≤ n`. Write `u := p^{−1}`.

### 2.1 Lemma U (level expansion) `[PROVED]`

> For all `N ≥ 0`, `m ≥ 1`:  `H^{(m)}_N = Σ_{e ≥ 0} u^{em}·Σ_e^{(m)}(N)`, where
> `Σ_e^{(m)}(N) := Σ_{j ≤ ⌊N/p^e⌋, p∤j} j^{−m} ∈ ℤ_p`, and `Σ_e^{(m)}(N) = 0` for `p^e > N`.

*Proof.* Partition `{1,…,N}` by `e = v_p(i)`: `i = p^e j` with `p∤j`, `j ≤ N/p^e`, and
`i^{−m} = p^{−em}j^{−m}`. ∎

Two consequences used constantly:
`Σ_e^{(m)}(N) = Σ_{e−1}^{(m)}(⌊N/p⌋)` for `e ≥ 1`; and `v_p(H^{(m)}_N) ≥ −m⌊log_p N⌋`.

### 2.2 All arguments live in `M+1` levels `[PROVED]`

`n+k, n+l < 2P`; `k+l < 2P`; `n+k+l < 3P`; `n−k, k, l, n < P`. Since `p ≥ 5`, `3P < pP = p^{M+1}`.
Hence **every** letter `X_m` of the alphabet has an expansion

```
X_m = Σ_{e=0}^{M} u^{em}·𝖷_{m,e},        𝖷_{m,e} ∈ ℤ_p,
```
and a weight-5 monomial `∏_i X_{m_i}` (`Σ m_i = 5`) has `u`-order at most `5M`. Consequently

```
v₅(n,k,l) = Σ_{j=0}^{5M} K_j·u^j ,  K_j ∈ ℤ_p ,   so   d₅ ≤ max{ j : K_j ≠ 0 }.     (2.2)
```

### 2.3 The top-level residues, and the pattern `[PROVED]`

Put
```
α := [n+k ≥ P],  γ := [n+l ≥ P],  ε := ⌊(k+l)/P⌋ ∈ {0,1},
κ := [n+k+l ≥ (ε+1)P],  θ := ε+1 ∈ {1,2}   (θ set to 1 when κ = 0).
```

> **Lemma R (top-level residues).** The `e = M` coefficient of a letter is
> `α` for `A_m(k)`, `γ` for `A_m(l)`, `0` for every `B_m` and for `N_m`, and `κ·θ^{−m}` for `C_m`.

*Proof.* `k,l,n,n−k < P` gives `Σ_M(·) = 0` for those arguments. `Σ_M^{(m)}(n+k)` is a sum over
`j ≤ ⌊(n+k)/P⌋ ≤ 1` with `p∤j`, i.e. `= α`. For `C_m`: with `Θ := ⌊(n+k+l)/P⌋ ≤ 2` and
`ε = ⌊(k+l)/P⌋`, every `j ≤ 2 < p`, so the coefficient is `Σ_{j=ε+1}^{Θ} j^{−m}`; and `n < P`
forces `ε ≤ Θ ≤ ε+1`, so `Θ − ε = κ` and the coefficient is `κ·θ^{−m}`. ∎

> **Lemma K (Kummer floor).** `v_p C(n+k,n) ≥ α`, `v_p C(n+l,n) ≥ γ`, `v_p C(n+k+l,n) ≥ κ`; hence
> ```
>            vT := v_p T(n,k,l) ≥ α + γ + κ =: s .                                   (2.3)
> ```

*Proof.* Kummer: `v_p C(n+k,n)` = number of carries in `n+k`. Both `n,k < P = p^M`, so a carry out
of position `M−1` occurs iff `n+k ≥ P`, i.e. iff `α = 1`. Same for `γ`. For `κ`: write
`k+l = εP+ρ`, `0 ≤ ρ < P`; the carry out of position `M−1` in `n+(k+l)` occurs iff `n+ρ ≥ P`, i.e.
iff `n+k+l ≥ (ε+1)P`, i.e. iff `κ = 1`. ∎

> **Lemma C (the census, at EVERY level).** The pattern `π = (α,γ,κ,θ)` takes exactly the seven
> values
> ```
> (0,0,0,1), (0,0,1,1), (1,0,1,1), (0,1,1,1), (1,1,0,1), (1,1,1,1), (1,1,1,2),
> ```
> with `s = α+γ+κ = 0,1,2,2,2,3,3` respectively.

*Proof.* (i) `κ = 0 ⟹ α = γ`. Suppose `α = 1, κ = 0`. If `ε = 0` then `κ = [n+k+l ≥ P] = 0` gives
`n+k+l < P`, contradicting `n+k ≥ P`. So `ε = 1`, i.e. `k+l ≥ P`; then `n+l ≥ k+l ≥ P` (using
`k ≤ n`), so `γ = 1`. Symmetrically `γ = 1, κ = 0 ⟹ α = 1`. So the `κ=0` patterns are `(0,0,0)`
and `(1,1,0)`.
(ii) `θ = 2` (i.e. `ε = 1`, `k+l ≥ P`) forces `n+k ≥ k+l ≥ P` (using `l ≤ n`) and
`n+l ≥ k+l ≥ P`, i.e. `α = γ = 1`.
(iii) with `κ = 1, ε = 0` all four `(α,γ)` occur. Total `2 + 4 + 1 = 7`. ∎

*(This is the same list as `PHASE2_FINAL` §2.2, but the proof is now level-free and does not go
through Lemma D: at `M = 1` it reproves "`a+b ≥ p ⟹ vT ≥ 2`" as a corollary rather than using it.)*

### 2.4 Proposition LIFT — the single-digit depth conditions are level-independent `[PROVED]`

Fix a pattern `π`. For a **letter-multiset** `S` (letters counted with multiplicity) write
`wt(S) = Σ_{X∈S} weight(X)` and

```
Φ_π(S) := Σ_{monomials 𝓜 ⊇ S} c_𝓜 · ∏_{X ∈ 𝓜∖S} ρ(X;π) ,                          (2.4)
```
`c_𝓜` the `w₅`-coefficient of `𝓜` and `ρ(X;π) ∈ {α, γ, κθ^{−m}, 0}` the top-level residue of
Lemma R. These are ℚ-linear functionals of the 448 coefficients, **independent of `p`, `n`, `M`**.

> **Proposition LIFT.** Let `J ≥ 0` and suppose
> ```
>              Φ_π(S) = 0   for every letter-multiset S with wt(S) ≤ 4 − J .        (DEPTH_π(J))
> ```
> Then for **every** `M ≥ 1` and every cell `(n,k,l)` with `⌊log_p n⌋ = M−1` and pattern `π`,
> ```
>              d₅(n,k,l) ≤ 5(M−1) + J = 5L + J .
> ```
> Moreover, at `M = 1` the conditions `(DEPTH_π(J))` are **exactly** the conditions
> "`K_j = 0` identically in the `ℤ_p`-symbols for `j > J`" imposed in `PHASE2_FINAL` §2.3 and
> certified by `work/lb5/solve_depth.py`.

*Proof.* Expand each letter by Lemma U and collect. Writing `j = 5M − δ` and `f_i := M − e_i ≥ 0`
(so `Σ f_i m_i = δ`),

```
K_{5M−δ} = Σ_𝓜 c_𝓜 Σ_{f: Σ f_i m_i = δ, f_i ≤ M}  (∏_{i: f_i ≥ 1} 𝖷_{i,M−f_i})·(∏_{i: f_i = 0} ρ(X_i;π)) .
```

Regard the `𝖷_{i,e}` (`0 ≤ e ≤ M−1`, one indeterminate per (letter, level)) as independent
symbols — this is a *strengthening*, exactly the one already made at `M = 1`. Two contributions
carry the same symbol monomial iff they have the same multiset `{(X_i, M−f_i) : f_i ≥ 1}`; that
multiset determines the dropped multiset `S` and the drop profile `f|_S`. Summing over `𝓜` at
fixed `(S,f|_S)` produces `c(S,f)·Φ_π(S)` where `c(S,f) = ∏_u (q_u!)^{-1}·q!` is the multinomial
count of ways to distribute the `q` copies of a repeated letter among the prescribed levels — a
**nonzero rational independent of `𝓜`** (for a letter occurring `N ≥ q` times in `𝓜`, the count
is `C(N,q)·q!/∏ q_u!`, and the ratio to the `M = 1` count `C(N,q)` is `q!/∏ q_u!`, free of `N`).
Hence

```
K_{5M−δ} = 0 identically in the symbols  ⟺  Φ_π(S) = 0 for every S realisable by some
                                             admissible f with Σ f_i m_i = δ.
```

The minimal `δ` realising a given support `S` is `δ = wt(S)` (all `f_i = 1`), admissible for every
`M ≥ 1`. Therefore

```
{ K_j = 0 for all j > 5(M−1)+J }  ⟸  { Φ_π(S) = 0 for all S with wt(S) ≤ 4−J } ,
```
because `j > 5(M−1)+J ⟺ δ = 5M−j < 5−J ⟺ wt(S) ≤ δ ≤ 4−J`. With (2.2) this gives
`d₅ ≤ 5(M−1)+J`. At `M = 1`, `δ = 5 − (u\text{-order})`, so `u > J ⟺ wt(S) ≤ 4−J`: the two
condition sets coincide, row for row, which is exactly how `depthcond.py` indexes them
(`rows[(pat, u, sym)]`, `sym` = the sorted symbol tuple = `S`). ∎

> **Corollary (DEPTH-gen). `[PROVED]`** With `w₅ = w5_allp` (or any point of the depth-conditioned
> 124-dimensional family), for **every** prime `p ≥ 5`, **every** `n ≥ 1` and **every** cell:
> ```
>     d₅(n,k,l) ≤ 5L + 1 + min(α+γ+κ, 2) ≤ 5L + 1 + min(v_p T(n,k,l), 2) .
> ```
> *(The caps are `J(π) = 1+min(s,2)` for `s ≥ 1`; for `π = (0,0,0,1)` every top residue vanishes,
> so `Φ_π(S) = 0` automatically whenever `𝓜∖S ≠ ∅`, i.e. whenever `wt(S) ≤ 4`, and the corollary
> holds there with `J = 0`.)* The second inequality is Lemma K.

**`[VERIFIED 0 violations / 150 955 cells]`** `p ∈ {5,7,11,13}`, `n ≤ 40/55/45/45` (levels
`L = 0,1,2`), all `(k,l)`; also `v_p T ≥ α+γ+κ` with **0** counterexamples, and the bound is
**sharp** (min slack `0` at every prime, attained already at `L = 0`).

### 2.5 First payoff: an unconditional bound for all `n`

Cell by cell, `v_p(T·v₅) ≥ vT − d₅ ≥ vT − 5L − 1 − min(vT,2) ≥ −5L−1`, and
`v_p(H^{(5)}_n Q_n) ≥ −5L` because `Q_n ∈ ℤ`. Hence **Theorem 5.1** (§5.1).

---

## 3. (F-gen): Lemma F for multi-digit `a` `[PROVED]`

### 3.1 Statement

Let `p ≥ 5`, `a ≥ 1`, `0 ≤ r < p`, `n = ap+r`, and `0 ≤ b,c ≤ a`. Put
`𝒯(b,c) := Σ_{s,t=0}^{p−1} T(n, bp+s, cp+t)`. Let `M_a := ⌊log_p a⌋+1`, `P_a := p^{M_a}` (so
`a < P_a`) and let `α,γ,κ` be the **level-`a`** indicators of §2.3 evaluated at `(a,b,c)`,
`s_a := α+γ+κ`, `vT := v_p T(a,b,c) ≥ s_a` (Lemma K).

> **Lemma F-gen. `[PROVED]`** For every `a ≥ 1` and every `(b,c)`,
> ```
>      v_p( 𝒯(b,c) − Q_r·T(a,b,c) )  ≥  1 + min(s_a, 2)  =: G  (≤ 3).
> ```

Three features distinguish this from the endgame's Lemma F: (i) it holds for **all** `a`, not only
`a < p`; (ii) the comparison constant is `Q_r` itself — **no** `μ = Q_r + p a Ψ_a` correction and
**no** `Λ = Q_n/Q_a`, hence **no `p ∤ Q_a` hypothesis** and no exceptional-prime compensation;
(iii) it is one order weaker than Lemma F (`2+min(vT,2)`), and that single order of slack is what
makes the general-`a` proof short. It is exactly the precision the induction consumes (§4.2).

**`[VERIFIED 0 failures / 111 963 cells]`** `p = 5,7,11,13`, `a ≤ 30/22/15/13` (multi-digit),
all `r`, all `(b,c)`; sharp (min slack `0`).

### 3.2 Ingredient: Lemma B is already general

`endgame` §R1.1 states Lemma B under "`0 ≤ a,r < p`", but the hypothesis `a < p` is never used:
with `k = bp+s`, `l = cp+t`, `0 ≤ s ≤ r`, `0 ≤ t ≤ r`, `e₁=[r+s≥p]`, `e₂=[r+t≥p]`,
`e₃=⌊(r+s+t)/p⌋`, `e₄=[s+t≥p]`, the true base-`p` quotients of the 15 factorial slots are
`(a+b+e₁, a+c+e₂, a+b+c+e₃, a; b,b,b, c,c,c, a−b,a−b, a−c,a−c, b+c+e₄)`, whatever `a` is, and the
substitution `m! = p^{m₁}m₁!((p−1)!)^{m₁}m₀!G(m₁,m₀)` is unconditional. Hence, **exactly**,

```
T(n,k,l) = T(a,b,c)·T(r,s,t)·Π·Ĝ ,
Π = C(a+b+e₁,e₁)·C(a+c+e₂,e₂)·C(a+b+c+e₃,e₃) / C(b+c+e₄,e₄) ,      Ĝ ∈ 1+pℤ_p .   (3.1)
```
`Ĝ ∈ 1+pℤ_p` because each `G(m₁,m₀) = [∏_{i<m₁}B_i/((p−1)!)^{m₁}]·∏_{u≤m₀}(1+m₁p/u) ∈ 1+pℤ_p`
(Lemma W, `p ≥ 5`, the only use of Wolstenholme), for every `m₁ ≥ 0`.
**`[VERIFIED 8 247 294 in-regime cells / 0 failures]`** (`p = 5,7,11`, all `a ≤ 3p+1`, all `r`,
all `0 ≤ b,c ≤ a`, all `s,t ≤ r`; `Ĝ` recomputed as `T(n,k,l)/(T(a,b,c)T(r,s,t)Π)` over ℚ and
tested for `Ĝ − 1 ∈ pℤ_p`) — see §7 `exp8.py`.

The admissible carry patterns are unchanged (they involve only `r,s,t`):
`(e₁,e₂,e₃,e₄) ∈ {(0,0,0,0),(0,0,1,0),(1,0,1,0),(0,1,1,0),(1,1,1,0),(1,1,1,1),(1,1,2,1)}`
(`e₄=1 ⟹ e₁=e₂=1` since `t ≤ r ⟹ r+s ≥ s+t ≥ p`; `e₁=1 ⟹ e₃≥1`; `e₃=2 ⟹ e₄=1`).

### 3.3 Ingredient: two carry inequalities `[PROVED]`

Write `car(x,y,ϵ)` for the number of carries in the base-`p` addition `x+y+ϵ`, `ϵ ∈ {0,1}` the
carry into position 0, and `z(N)` for the number of trailing digits of `N` equal to `p−1`.

> **(C1)** `car(x,y,1) = car(x,y,0) + z(x+y) ≥ car(x,y,0)`.
> *Proof.* `car(x,y,ϵ) = (s(x)+s(y)+ϵ−s(x+y+ϵ))/(p−1)` with `s` the digit sum, and
> `s(N+1) = s(N)+1−(p−1)z(N)`. ∎

> **(C2)** `v_p C(n+k,n) = e₁ + car(a,b,e₁) ≥ v_p C(a+b,a)`, and likewise for `(n+l,n)`;
> `v_p C(n,k) = [s>r] + car(b, a−b−[s>r], [s>r]) ≥ v_p C(a,b) + [s>r]`, likewise for `(n,l)`.
> *Proof.* Split the addition/subtraction at position 0 and apply (C1); for the second, the
> higher-position carries of `k+(n−k)` sum to `a`, and `s(a−b−1)+1 ≥ s(a−b)`. ∎

### 3.4 Proof of Lemma F-gen

**(A) Off-regime terms `s > r` or `t > r`: `v_p T(n,k,l) ≥ G`.**
By `k↔l` symmetry assume `s > r`. If `b = a` then `k > n` and `T = 0`. So `b < a`; the subtraction
`n−k` borrows at position 0, so `v_p C(n,k) ≥ 1` and the **squared** factor gives `v_p T ≥ 2`.
That settles `G ≤ 2`, i.e. `s_a ≤ 1`. If `s_a ≥ 2` then at least two of `α,γ,κ` are 1; `α = γ = 0`
would force `s_a = κ ≤ 1`, so `α = 1` or `γ = 1`, and then (C2) gives
`v_p C(n+k,n) ≥ v_p C(a+b,a) ≥ α` resp. `v_p C(n+l,n) ≥ γ`, i.e. one further power: `v_p T ≥ 3 = G`. ∎

**(B) In-regime terms `s ≤ r`, `t ≤ r`.** Since `Q_r = Σ_{s,t ≤ r} T(r,s,t)` exactly, (3.1) gives

```
Σ_{s,t≤r} T(n,k,l) − Q_r T(a,b,c) = T(a,b,c)·Σ_{s,t≤r} T(r,s,t)·[ΠĜ − 1] ,
```
so it suffices, termwise, that `vT + J + v_p(ΠĜ−1) ≥ G` with `J := v_p T(r,s,t)`. Note
`v_p(ΠĜ−1) ≥ min( v_p(Π−1), v_p(Π)+1 ) ≥ min(v_p(Π), 0)`, and `G = 1+min(s_a,2) ≤ 3`,
`vT ≥ s_a`. Run the seven patterns:

| `(e₁,e₂,e₃,e₄)` | `Π` | `J ≥` | `v_p(ΠĜ−1) ≥` | total ≥ | `≥ G`? |
|---|---|---|---|---|---|
| `(0,0,0,0)` | `1` | `0` | `1` (as `Ĝ−1 ∈ pℤ_p`) | `s_a+1` | ✓ `s_a ≥ min(s_a,2)` |
| `(0,0,1,0)` | `a+b+c+1 ∈ ℤ` | `1` | `0` | `s_a+1` | ✓ |
| `(1,0,1,0)`, `(0,1,1,0)` | `∈ ℤ` | `2` | `0` | `s_a+2` | ✓ |
| `(1,1,1,0)` | `∈ ℤ` | `3` | `0` | `3` | ✓ |
| `(1,1,1,1)` | `(a+b+1)(a+c+1)(a+b+c+1)/(b+c+1)` | `2` | see below | see below | ✓ |
| `(1,1,2,1)` | `(a+b+1)(a+c+1)C(a+b+c+2,2)/(b+c+1)` | `3` | see below | see below | ✓ |

*(the `J` column: `e₁=1 ⟹ C(r+s,r)` carries; `e₂=1 ⟹ C(r+t,r)` carries; if `e₄=0` and `e₃≥1`
then `C(r+s+t,r)` carries at position 0; if `e₄=1` and `e₃=2` then `r+σ ≥ p` with `σ = s+t−p`, so
`C(r+s+t,r)` carries.)*

**The two `e₄ = 1` patterns.** Put `m := v_p(b+c+1)` and `τ := v_p(a)`. Then
`a+b+c+1 = a + (b+c+1)` has `v_p ≥ min(τ,m)`, so `v_p(Π) ≥ min(τ,m) − m` and therefore
`v_p(ΠĜ−1) ≥ min(τ,m) − m` (which is `≤ 0`, so the bound is valid whether or not `v_p(Π) ≥ 0`).

*Case `τ ≥ m`.* Then `v_p(ΠĜ−1) ≥ 0`, and the totals are `vT+2 ≥ 2` resp. `vT+3 ≥ 3`; since
`G ≤ 3` and, for `(1,1,1,1)`, `vT+2 ≥ s_a+2 ≥ min(s_a,2)+1 = G`. ✓

*Case `τ < m` (so `m ≥ 1`).* Then `b+c ≡ −1 (mod p^m)`, i.e. the digits of `b+c` in positions
`0..m−1` are all `p−1`, while `a` has digits `0` in positions `0..τ−1` and `a_τ ≥ 1`. In the
addition `a+(b+c)`: no carry at positions `0..τ−1` (`0+(p−1) = p−1`), a carry at position `τ`
(`a_τ+(p−1) ≥ p`), and a carry at each of `τ+1,…,m−1` (`a_i+(p−1)+1 ≥ p`). Hence

```
E := v_p C(a+b+c,a) ≥ m − τ ,   so   vT ≥ (m−τ) + A + A' + 2D + 2D' ,               (3.2)
```
with `A = v_pC(a+b,a) ≥ α`, `A' = v_pC(a+c,a) ≥ γ`, `D = v_pC(a,b)`, `D' = v_pC(a,c)`.
For `(1,1,1,1)` the total is `≥ vT + 2 + (τ−m) ≥ 2 + A+A'+2D+2D'`. If `s_a ≤ 1` then `G ≤ 2` ✓;
if `s_a ≥ 2` then (as in (A)) `α = 1` or `γ = 1`, so `A+A' ≥ 1` and the total is `≥ 3 = G` ✓.
For `(1,1,2,1)` the total is `≥ vT + 3 + (τ−m) ≥ 3 ≥ G` ✓. ∎

**Remark.** Lemma Phi is not used. The single-digit Lemma F needs it because it aims at relative
precision `p²` (its first-order term must be `(b,c)`-independent); at relative precision `p¹` the
first-order term is simply absorbed, and the whole first-order analysis (Lemmas F1, F2, Phi,
the `Ψ_a` supercongruence) disappears. That is the structural reason the multi-digit statement is
*easier* than the single-digit one.

---

## 4. The induction: statement, ledger, and what it consumes

### 4.1 The inductive statement (verbatim)

> **(IND).** *Let `p ≥ 5`. For `L ≥ 0` let `𝓘(L)` be the assertion*
> ```
>     for every m ≥ 1 with ⌊log_p m⌋ ≤ L :   v_p( W_m ) ≥ −5⌊log_p m⌋ ,
>     where W_m = P_m − H^{(5)}_m·Q_m .
> ```
> *Then `𝓘(0)` is `(BASE)` of §6.1, and for every `L ≥ 1`, `𝓘(L−1) ⟹ 𝓘(L)`. Consequently
> `v_p(P_m) ≥ −5⌊log_p m⌋` for all `m ≥ 1`, i.e. `ord_p(p_m) ≥ κ(m) − 5⌊log_p m⌋`.*

**Why this is the right form, and not the naive one.** The naive per-digit ratio statement
`p⁵ P_n/Q_n ≡ P_a/Q_a (mod p)` fails multi-digit (`ORCHESTRATOR_NOTES` §2d;
`PADIC_SEAM` §T3.1 measures the depth of the single-step ratio as `5−2s`, negative for `s ≥ 3`).
(IND) is scaled: it never divides by `Q`, never renormalises, and its per-level target is an
inequality on `v_p(W)`, not a congruence. The `p^{5s}`-scaled law of `PADIC_SEAM` §T3.1,
`p^{5s}P_{ap^s}Q_{ap^{s−1}} ≡ p^{5(s−1)}P_{ap^{s−1}}Q_{ap^s} (mod p^{3s})`, is the *tower*
shadow of (IND); (IND) is its cell-level cause.

Note `v_p(H^{(5)}_m Q_m) ≥ −5⌊log_p m⌋` always (`Q_m ∈ ℤ`, Lemma U), so `𝓘(L)` is *equivalent* to
`v_p(P_m) ≥ −5⌊log_p m⌋` on the same range.

### 4.2 The step, and the budget ledger

Let `L ≥ 1`, `n` with `⌊log_p n⌋ = L`, `n = ap+r`, `0 ≤ r < p`, `a = ⌊n/p⌋`, `⌊log_p a⌋ = L−1`.
Group the cells of `W_n` by `(b,c) = (⌊k/p⌋, ⌊l/p⌋)`, `0 ≤ b,c ≤ a`, and split

```
p⁵W_n − Q_r W_a  =  (I) + (II),
(II) := Σ_{b,c} v₅(a,b,c)·[ 𝒯(b,c) − Q_r T(a,b,c) ] ,
(I)  := Σ_{k,l} T(n,k,l)·𝓔(n,k,l) ,   𝓔 := p⁵v₅(n,k,l) − v₅(a,⌊k/p⌋,⌊l/p⌋) .
```

If `v_p(I), v_p(II) ≥ −5(L−1)` then, using `𝓘(L−1)` for `v_p(Q_rW_a) ≥ v_p(W_a) ≥ −5(L−1)`,

```
v_p(p⁵W_n) ≥ −5(L−1)   ⟹   v_p(W_n) ≥ −5 − 5(L−1) = −5L ,
```
which is `𝓘(L)`. **Budget ledger for (II), per cell, per digit level:**

| quantity | value | source |
|---|---|---|
| provided: `v_p v₅(a,b,c)` | `≥ −5(L−1) − 1 − min(s_a,2)` | **(DEPTH-gen)**, §2.4 (Prop. LIFT + the (DEPTH) `[CERT]`) |
| provided: `v_p(𝒯 − Q_r T)` | `≥ 1 + min(s_a,2)` | **Lemma F-gen**, §3.4 |
| consumed: target | `≥ −5(L−1)` | (IND) step |
| **slack** | **exactly 0** | both inputs are sharp (min slack 0 in the sweeps) |

So the two new lemmas match to the digit: nothing is wasted and nothing is missing in (II).
Note also what is *not* needed: `Λ = Q_n/Q_a`, the hypothesis `p ∤ Q_a`, the `mod p²`
supercongruence `Q_n ≡ Q_a(Q_r + paΨ_a)`, and Lemma Phi. The exceptional primes
(`v_p(Q_n)` up to 7 at `p = 7`) are irrelevant to (IND).

### 4.3 The descent term (I): in-regime `[PROVED]`, off-regime `[GAP]`

By Lemma U, `p^m H^{(m)}_N = H^{(m)}_{⌊N/p⌋} + p^m Σ_0^{(m)}(N)`. Hence, letter by letter,

```
p^m A_m^{(n)}(k) = A_m^{(a)}(b) + e₁·(a+b+1)^{−m} + p^m σ^A ,   σ^A := Σ_0(n+k) − Σ_0(k) ∈ ℤ_p ,
p^m B_m^{(n)}(k) = B_m^{(a)}(b) − [s>r]·(a−b)^{−m} + p^m σ^B ,
p^m C_m^{(n)}   = C_m^{(a)}(b,c) + [e₃-terms] − [e₄-terms] + p^m σ^C ,
p^m N_m^{(n)}   = N_m^{(a)} + p^m σ^N .
```

**In-regime** (`s ≤ r`, `t ≤ r`, `e₁=e₂=e₃=e₄=0`) all the mismatch terms vanish and
`p^m X^{(n)}_m = X^{(a)}_m + p^m σ^X` exactly. Expanding the product,

```
𝓔 = Σ_{S ≠ ∅} p^{wt(S)}·σ_S·Ψ_S ,   σ_S = ∏_{X∈S} σ^X ∈ ℤ_p ,
Ψ_S := Σ_{𝓜 ⊇ S} c_𝓜 ∏_{X ∈ 𝓜∖S} X^{(a)}   (a level-`a` form of weight 5 − wt(S)).
```
By exactly the argument of Prop. LIFT applied to `Ψ_S` (its `u`-order is `(5−wt S)M_a − δ'` and
its top nonvanishing `δ'` obeys `wt(S)+δ' ≥ 5 − J(π)` because `Φ_π(S ∪ S') = 0` for
`wt(S∪S') ≤ 4−J(π)`),

```
v_p( p^{wt S}σ_S Ψ_S ) ≥ wt(S) − [ (5−wt S)M_a − (5 − J(π) − wt S) ] = 5 − J(π) − (5 − wt S)M_a
```
whenever `wt(S) ≤ 5−J(π)`. (If `wt(S) > 5−J(π)` then `wt(S) ≥ 6−J(π) ≥ 3`, so `wt(S)·M_a ≥ 3 ≥ J(π)`
and the requirement below, `vT ≥ J(π) − wt(S)M_a`, holds trivially.)
Also, in the fully in-regime case (C2) is an equality at every slot, so
`v_p T(n,k,l) = v_p T(a,b,c) = vT`. The requirement `v_p(T·𝓔) ≥ −5(M_a−1)` becomes
`vT ≥ J(π) − wt(S)·M_a`, and with `J(π) = 1+min(s_a,2) ≤ 3`, `wt(S) ≥ 1`, `vT ≥ s_a`:

| `M_a` | `wt(S)` | needed `vT ≥` | have | |
|---|---|---|---|---|
| `1` | `1` | `min(s_a,2)` | `vT ≥ s_a` | ✓ |
| `1` | `2` | `min(s_a,2)−1` | | ✓ |
| `1` | `≥3` | `≤ 0` | | ✓ |
| `≥2` | `≥1` | `≤ 1`, and `=1` only when `J = 3` i.e. `s_a ≥ 2` | `vT ≥ 2` | ✓ |

so **the in-regime descent term costs nothing** — slack `≥ 0` at every cell and every level.

**Off-regime** the mismatch terms `e₁(a+b+1)^{−m}` etc. enter. They are bounded
(`v_p(a+b+1) ≤ M_a` because `a+b+1 ≤ 2a+1 < 2P_a < pP_a`), and their presence *forces carries*
(`e₁ = 1` and `v_p(a+b+1) = λ` give `v_p C(n+k,n) = 1 + car(a,b,1) ≥ 1 + v_pC(a+b,a) + λ` by (C1),
since `z(a+b) ≥ λ`), which is precisely the mechanism of Lemma G off-regime + Lemma D++
(`endgame` §R3) at `a < p`. **Lifting that argument to general `a` is the residual sub-gap
`[GAP-DESC]`, §6.2.** It is a finite carry-bookkeeping problem of exactly the same type as §3.4,
with the same one order of slack available; it is *not* a new mathematical mechanism.

---

## 5. What is now proved, and the sweeps

### 5.1 Theorem 5.1 (unconditional, all `n`) `[PROVED]`

> Assume (T1-top) and the (DEPTH) certificate. For every prime `p ≥ 5` and every `n ≥ 1`,
> ```
>      ord_p(P_n) ≥ −5⌊log_p n⌋ − 1 ,
> ```
> equivalently `d_n⁵·(∏_{5 ≤ p ≤ 3n} p)·P_n ∈ ℤ[1/6]`. (For `p > 3n` all letter arguments are
> `< p`, so `ord_p(P_n) ≥ 0` outright.)

*Proof.* §2.5. ∎

This is strictly stronger than anything previously proved for `n ≥ p²` — the prior tree had
**nothing** there — and it is one radical away from (SHARP-12).

### 5.2 Theorem 5.2 (conditional) `[PROVED modulo (BASE) and (GAP-DESC)]`

> Assume (T1-top), the (DEPTH) certificate, `(BASE)` (§6.1) and `(GAP-DESC)` (§6.2). Then for
> every prime `p ≥ 5` and every `n ≥ 1`, `ord_p(P_n) ≥ −5⌊log_p n⌋`, i.e.
> `ord_p(p_n) ≥ κ(n) − 5⌊log_p n⌋` — **(SHARP-12, `p ≥ 5` part)**.

*Proof.* (IND) of §4.1, whose step is §4.2 with the ledger of that table: (II) is covered by
(DEPTH-gen) + Lemma F-gen with slack exactly 0, (I) in-regime by §4.3 and off-regime by
(GAP-DESC), and `𝓘(0)` is (BASE). ∎

> **UPDATE 2026-07-25.** Both hypotheses have since been discharged: `(BASE)` in
> `work/PHASE2_NUCLEUS.md` (P1h) and `(GAP-DESC)` in `work/PHASE2_GAPDESC.md` (P1i). Theorem 5.2
> is therefore **unconditional given (T1-top) and the (DEPTH) certificate**, i.e. (SHARP-12,
> `p ≥ 5`) now rests on the decomposition certificate alone.

### 5.3 The required sweeps `[VERIFIED, 0 failures]`

| sweep | range | cells | failures | min `ord_p(P_n)+5L` |
|---|---|---|---|---|
| exact ladders | `n ≤ 360`, `p ∈ {5,…,31}` | 3 240 | **0** | **0** (at `p=5, n=1`) |
| same, `(CB)` form `ord_p(p_n) ≥ κ−5L` | `n ≤ 360`, `p ≤ 31` | 3 240 | **0** | — |
| certified order-3 recurrence, exact ℚ | `n ≤ 3000`, `p ∈ {5,…,31}` | 27 000 | **0** | **0** |
| recurrence vs exact ladder cross-check | `n ≤ 360` | 361 | **0 mismatches** | — |
| **(BASE)** `ord_p(P_n) ≥ 0`, `n < p` | every prime `5 ≤ p ≤ 367` | 11 884 | **0** | **0** |
| **(DEPTH-gen)** `d₅ ≤ 5L+1+min(s,2)` | `p ≤ 13`, `L ≤ 2` | 150 955 | **0** | slack min **0** |
| **Lemma K** `v_pT ≥ α+γ+κ` | same | 150 955 | **0** | — |
| **Lemma F-gen** | `p ≤ 13`, `a ≤ 30`, all `r,b,c` | 111 963 | **0** | slack min **0** |
| **Lemma B general `a`** (`Ĝ ∈ 1+pℤ_p`) | `p ≤ 11`, `a ≤ 3p+1`, in-regime | see §7 | **0** | — |

The min slack `0` everywhere is the point: **the depth the ledger provides and the depth the
induction consumes agree exactly, digit by digit.** There is no spare power anywhere in the chain.

---

## 6. The gaps, stated exactly

### 6.1 `[GAP-BASE]` — the base case

> **(BASE).** For every prime `p ≥ 5` and every `n < p`: `ord_p(P_n) ≥ 0`, equivalently
> `v_p(W_n) ≥ 0`.

**Status.** `[VERIFIED 11 884/11 884]` (all primes `5 ≤ p ≤ 367`, all `n < min(p,361)`), min value
exactly `0`. **Not proved.**

**Why the route proposed in the brief does not exist.** The brief suggested: "for `n < p` every
harmonic letter argument is `< p` … so every summand is `p`-integral". This is **false**. In the
178-term `w5_allp` alphabet the letters `A_m(k)`, `A_m(l)` have upper argument `n+k ≤ 2n` and `C_m`
has `n+k+l ≤ 3n`; for `p/3 < n < p` these reach or exceed `p`, and a pole of order `m` appears.
What the depth calculus actually gives at `L = 0` is

```
v_p( T(n,k,l)·v₅(n,k,l) )  ≥  vT − d₅  ≥  vT − 1 − min(vT,2)  ≥  −1 ,
```
and the value `−1` is **attained**, e.g. at `(n,k,l) = ((p+1)/2, 0, (p−1)/2)`
(`p=5: (3,0,2)`, `p=7: (4,0,3)`, `p=11: (6,0,5)`, `p=13: (7,0,6)`, …), where `vT = 2`, `d₅ = 3`,
pattern `(α,γ,κ,θ) = (0,1,1,1)`. `[VERIFIED, p ≤ 19]`

**Why no representative can fix it (a hard negative).** The cell-wise bound would follow from
`d₅ ≤ v_pT`, i.e. from the strengthened depth conditions `(DEPTH⁺)` with caps
`J(π) = α+γ+κ` instead of `1+min(α+γ+κ,2)`. Adjoining those to the fitting system:

| system | caps `J(π)` | condition rows | rank(cond) | rank(joint) | consistent? |
|---|---|---|---|---|---|
| (DEPTH) — `PHASE2_FINAL` | `1+min(s,2)` | 68 | 42 | 324 | **yes** (nullity 124) |
| **(DEPTH⁺)** — all patterns | `s` | **239** | **123** | **342** | **NO** |
| **(DEPTH⁺⁺)** — *only* the three `s = 2` patterns tightened to `J = 2` | `1+min(s,2)`, except `2` on `(0,1,1,1),(1,0,1,1),(1,1,0,1)` | **149** | **81** | **342** | **NO** |

`[CERT — two auxiliary primes q = 33554393, 33554467, N = 600, work in §7]`. The third row is the
sharp localisation: it is **exactly the three `s = 2` patterns — precisely the ones carrying the
`−1` deficit — that cannot be tightened**; the `s ≤ 1` and `s = 3` patterns are already at the
cell-wise optimum for `w5_allp`. So **within the `p`-independent linear framework the deficit is
irreducible**: the base case requires a genuine cancellation between cells, not a better `w₅`. (Consistent with `PHASE2_FINAL` §2.5's "min slack
exactly 0" and with the fact that the same cell-wise bound is *attained* for the middle row,
where `v_p(P̂_a) = −1` really does occur.)

**The cancellation is global.** `[VERIFIED p ≤ 13]` the partial sums `Σ_c T(a,b,c)v₅(a,b,c)` at
fixed `b` still have `v_p = −1`; only the full double sum is integral. So no Lemma-Phi-style
row identity suffices; the identity needed mixes both indices.

### 6.2 `[GAP-DESC]` — the off-regime letter descent at multi-digit `a`

> **(GAP-DESC).** For `a ≥ p`, `n = ap+r`, and cells `(k,l)` with `s > r` or `t > r` or
> `e₁+e₂+e₃+e₄ > 0`, `v_p( T(n,k,l)·𝓔(n,k,l) ) ≥ −5⌊log_p a⌋`, where `𝓔` is the letter-descent
> error of §4.3.

> **UPDATE 2026-07-25 (P1i) — `[PROVED]`, see `work/PHASE2_GAPDESC.md`.** The node is closed for
> **every** `L = ⌊log_p n⌋ ≥ 1` (so the `a < p` case too, and Lemma D++ is not needed for it).
> **The route proposed in the paragraph below is refuted**: the letter-wise mismatch of `A_m(k)`
> has valuation `−mλ` while the Kummer gain of the whole of `T` is only `1+λ`, so at weight 5 the
> trade loses — at `p = 5, n = 19, (k,l) = (6,0)` the letter-wise ledger is short by one power.
> What closes the node is `(DEPTH-gen)` applied at **both** levels (which already annihilates the
> mismatch poles inside `v₅`) together with the Kummer lemma
> `off-regime ⟹ v_pT(n,k,l) ≥ 1 + max(s_n,s_a)` — because off-regime means a carry in base-`p`
> position `0`, the pattern indicators live in position `L ≥ 1`, and Kummer counts both.
> `[VERIFIED 188 353 733 off-regime cells, L = 1,2,3,4, 0 failures, sharp]`

**Status (as of P1d).** Proved for `a < p` (`closeout` §2.1 in-regime, `endgame` §R3 off-regime
via Lemma D++).
In-regime for all `a`: `[PROVED]` §4.3. Off-regime for `a ≥ p`: **not written out**. It is a
carry-bookkeeping lift of `endgame` §R3 with one order of slack available, of exactly the kind
executed in §3.4; the mismatch pole `v_p(a+b+1) = λ` is bounded by `M_a` and is compensated by
`λ` extra Kummer carries in `C(n+k,n)` via (C1). *Assessment: mechanical, ≈ one focused session,
no new mechanism.* This is the weaker of the two gaps.

### 6.3 The unified form of what is missing

Both gaps are the same statement at different levels. Expand `W_n` by the `u`-grading of §2:

```
W_n = Σ_{j} u^j·S_j ,   S_j := Σ_{k,l} T(n,k,l)·K_j(n,k,l) ∈ ℤ_p .
```
Prop. LIFT gives `K_j = 0` for `j > 5L + J(π)`, with `J(π) = 0` for `π = (0,0,0,1)` and
`J(π) = 1+min(s,2)` otherwise. Hence `K_{5L+1} ≠ 0` and `K_{5L+2} ≠ 0` both force `s ≥ 1`
(so `v_pT ≥ 1`), and `K_{5L+3} ≠ 0` forces `s ≥ 2` (so `v_pT ≥ 2`); and `K_j = 0` for `j > 5L+3`.
The target `v_p(W_n) ≥ −5L` is implied by `v_p(S_j) ≥ j − 5L` for every `j`, which is automatic
for `j ≤ 5L` and, for `j = 5L+1`, is `v_p(S_{5L+1}) ≥ 1` — **free**, since every contributing cell
has `v_pT ≥ 1`. So (SHARP-12) `⟸` the two mod-`p` identities

```
(V2)   Σ_{k,l}  T(n,k,l)/p   · K_{5L+2}(n,k,l)  ≡ 0  (mod p)     [cells with v_pT ≥ 1] ,
(V3)   Σ_{k,l}  T(n,k,l)/p²  · K_{5L+3}(n,k,l)  ≡ 0  (mod p)     [cells with v_pT ≥ 2] .
```

`(BASE)` is `(V2)&(V3)` at `L = 0`; the induction step is the assertion that `(V2)&(V3)` at level
`L−1` plus Lemma F-gen implies them at level `L`. **This is the single residual object of Phase 2
on the `p ≥ 5` side**, and it is exactly one power of `p` deep. A natural attack, by analogy with
Lemma Phi (which is the weight-1 shadow of a residue sum), is to seek the weight-2 / weight-3
residue identities on the BZ summand that make `(V2)`, `(V3)` exact; `Ψ_a` of `endgame` §R1.4 is
the first member of that family.

---

## 7. Reproduction

All scripts are exact-arithmetic Python (`fractions.Fraction` / `int`); none touches a Wolfram
kernel or `work/lb5/eps*.wl`.

All are in **`work/p1d/`** (new directory; nothing in `work/lb5/` was modified).

| script `work/p1d/` | what it does | output |
|---|---|---|
| `exp1.py` | `min_{n<p} v_p(P_n)`, `v_p(W_n)` from the exact ladders | `0` at every `p ≤ 47` |
| `basecase.py` | `(BASE)` over every prime `5 ≤ p ≤ 367`, `n < min(p,361)` | 11 884 cells, 0 failures (`basecase.out`) |
| `w5eval.py` | loader + evaluator for any saved `w₅` representative | — |
| `exp2.py` | `min(vT − d₅)` per pole pattern at `L = 0` | `−1`, only in the three `s=2` patterns |
| `exp3.py` | **(DEPTH-gen)** + Lemma K sweep, `L ≤ 2` | 150 955 cells, 0 violations |
| `exp4.py` | deficit across representatives; partial sums over `c` | `−1` for all three reps; row sums still `−1` |
| `exp5.py` | Lemma F verbatim (`2+min(vT,2)`) at multi-digit `a` | 75 053 cells, 0 failures |
| `exp6.py` | cell-wise deficit stratified by `L` | `−1` at `L = 0,1` |
| `exp7.py` | **Lemma F-gen** (`Q_r`, `1+min(s_a,2)`) at multi-digit `a` | 111 963 cells, 0 failures, slack 0 |
| `exp8.py` | **Lemma B** for general `a`: `Ĝ := T(n,k,l)/(T(a,b,c)T(r,s,t)Π) ∈ 1+pℤ_p` | 8 247 294 cells, 0 failures |
| `solve_strong.py strong` | **(DEPTH⁺)** consistency test | 239 rows, rank(cond) 123, rank(joint) 342, **INCONSISTENT**, both primes |
| `solve_strong.py vt2` | **(DEPTH⁺⁺)**: only the three `s = 2` patterns tightened | 149 rows, rank(cond) 81, rank(joint) 342, **INCONSISTENT**, both primes |
| `sweep.py` | the required (S1)/(S1b)/(S2) verification sweeps | 3 240 + 27 000 cells, 0 failures |

`solve_strong.py` reuses `work/lb5/fit.py`, `work/lb5/depthcond.py` unchanged; only the per-pattern
cap dictionary differs from `work/lb5/solve_depth.py`.
