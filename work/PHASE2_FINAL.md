# Phase-2 final mile — P1c

**Author:** mathematician-agent (River's odd-zeta program), P1c session
**Date:** 2026-07-24 (night)
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, scripts in `work/lb5/`
**Predecessor (authoritative):** `work/PHASE2_ENDGAME.md` (Lemma F, Lemma Phi, Lemma D++,
canonical `w5`, the `(GAP-5)` analysis, R4's licence diagnosis).

**Labels.** `[PROVED]` complete proof. `[VERIFIED r]` exact finite check on range `r`, 0 failures.
`[CERTIFIED]` machine proof object, independently re-checked by exact arithmetic. `[OPEN]`.

---

## STATUS BOARD

| item | status |
|---|---|
| **ITEM 1** — eps-deformation CT certificates | **PARTIAL.** Licence blocker **RESOLVED** (§0). The `Q`-row telescoper is now **[CERTIFIED]**: extracted *and* independently re-verified by exact arithmetic, equal to `L_BZ` on the nose (§1.2). The deformed CT is **re-diagnosed**: the blocker is no longer a licence seat but the *cost of the second telescoping step with a symbolic parameter* (§1.3). A new, costed route (rational specialisation + interpolation + exact certificate check) is opened and measured. Theorem B / (T1-top) remain **[VERIFIED]**, not [CERTIFIED]. |
| **ITEM 2** — close `(GAP-5)` | **CLOSED, route A (depth-minimal `w5`).** The depth conditions are `p`-independent, linear, and **consistent** (rank 324 = rank of the augmented system); the depth-conditioned family has dimension 124. Three explicit representatives verify with **0 failures** on every test, including the decisive cell-by-cell `(GAP-5)` test — **0 / 16 990 cells** at `p = 5,7,11,13`, where the closeout's 130-term representative failed 4 689 and the endgame's sparsest canonical one failed ≥ 3 628. Route B (thin-set cancellation) is not needed. §2. |

---

## §0. The licence blocker — RESOLVED, with the exact recipe

The endgame's R4 diagnosis (seat exhaustion) was correct, and three further facts were needed to
actually get a kernel and keep it:

1. **Seat count.** The two `mathpass` activation keys carry the seat spec `:2,2,8,8`. Empirically
   **three** `WolframKernel` processes may coexist; a fourth is refused with
   `Wolfram 15.0.0 Kernel cannot find a valid password` plus an interactive activation prompt.
   Persistent occupants: the MCP server kernel, plus other agents' kernels.
2. **Orphan kernels are the real hazard.** `timeout T math < f.wl` kills the `math` *shell wrapper*
   at `T`; the `WolframKernel` child **survives**, keeps its seat indefinitely, and **ignores
   `SIGTERM`**. Only `kill -KILL <pid>` frees it. Two seats had been lost this way before this
   session started, which is what made the endgame's retry fail.
   **Always** `ps aux | grep WolframKernel` and reap orphans before launching.
3. **The `Block[{Quit=…}]` workaround of endgame §R4.2 must NOT be used for a standalone kernel,**
   and the local `zeta-math-2/RISC/` copy must not be used either. Together they produce
   ``RISC`package::loading: Unexpected loading error`` → `LinkObject::linkv` → a permanently hung
   kernel that still holds the seat. The recipe that works, unchanged from the July session, is a
   plain
   ```
   Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];      (* v1.7.3, ~1 s *)
   ```
   under `math < file.wl`. (The `Block` trick remains correct advice for the *MCP* kernel only.)
4. **`TimeConstrained` does not interrupt `CreativeTelescoping`.** A 900 s cap was exceeded by
   >20 min with no abort. Budget with an **external** `timeout` and reap the orphan afterwards.

---

## §1. ITEM 1 — the CT certificates

### 1.1 Pipeline and gate

`work/lb5/eps2.wl`. Two-step creative telescoping on the *undeformed* BZ summand
`T(n,k,l) = C(n+k,n)C(n,k)^2 C(n+l,n)C(n,l)^2 C(n+k+l,n)`:

| stage | object | time |
|---|---|---|
| `Annihilator[T,{S[n],S[k],S[l]}]` | 3 generators, orders `(0,0,1),(0,1,0),(1,0,0)` | 0 s |
| `CreativeTelescoping[ann, S[k]-1, {S[n],S[l]}]` | 2 telescoper/certificate pairs | 0 s |
| `OreGroebnerBasis[·, OreAlgebra[S[n],S[l]]]` | 2 elements | 0 s |
| `CreativeTelescoping[gb, S[l]-1, {S[n]}]` | **1 telescoper, order 3** | 3 s |

Saved: `g0_ann.m`, `g0_ct1.m`, `g0_gb.m`, `g0_ct2.m`.
The endgame's claim that the joint call `CreativeTelescoping[ann,{S[k]-1,S[l]-1},{S[n]}]` fails is
confirmed (it returns `$Failed`; the July log's "`Length ctQ = 0`" was `$Failed` in disguise).
**The two-step split is the fix.**

### 1.2 Independent exact verification — `[CERTIFIED]`

`work/lb5/eps4.wl`, stage V. Every check is exact rational-function arithmetic on the *explicit*
binomial expression for `T`, i.e. it does not trust the CT machinery, only re-uses
`ApplyOreOperator` to expand the (fully explicit) operator coefficients.

| check | statement | result |
|---|---|---|
| **V1** | each of the 3 annihilator generators `L` satisfies `L·T ≡ 0` | `Together[(L·T)/T] = 0`, all 3 |
| **V2** | each `k`-step pair: `tel·T + (S_k-1)(cert·T) ≡ 0` | `= 0`, both pairs |
| **V3** | the final order-3 telescoper **is** `L_BZ` | coefficient ratio `{1,1,1,1}`; `Expand[coeffs − L_BZ] = {0,0,0,0}` |

Explicitly, the order-3 telescoper returned by the pipeline has coefficients
```
c0(n) = (n+1)^5 (n+2) a0(n+1),   c1(n) = -2(n+2) B8(n),
c2(n) = -2 B9(n),                c3(n) = 2(n+3)^5 (2n+5) a0(n),
a0(x) = 41218x^3+198849x^2+320790x+173057
```
— *identically* the certified BZ operator. **`Q_n = Σ_{k,l} T(n,k,l)` is annihilated by `L_BZ`:
[CERTIFIED], with the certificate independently re-checked.** (The Q-row node of the dependency
tree is now machine-proved end to end, not merely inherited from the closeout.)

### 1.3 The deformation — re-diagnosed, and a costed route

Deformation as specified in endgame §R4.3 (5 parameters, separating the `k`- and `l`-slots):
```
F(n,k,l;ak,al,bk,bl,g) = GK[ak]·HK[bk]·GL[al]·HL[bl]·CC[g],
GK[x]=Γ(n+k+1+x)/(Γ(n+1)Γ(k+1+x)),  HK[x]=(Γ(n+1)/(Γ(k+1+x)Γ(n-k+1-x)))^2,
CC[x]=Γ(n+k+l+1+x)/(Γ(n+1)Γ(k+l+1+x)),  and GL,HL the l-analogues.
```

**Measured cost** (`work/lb5/eps4.wl` stage R, `eps5.wl`):

| summand | `Annihilator` | CT in `k` | Gröbner | **CT in `l`** | telescoper order |
|---|---|---|---|---|---|
| undeformed `T` | 0 s | 0 s | 0 s | **3 s** | 3 |
| `g = 1/7` (rational) | 0 s | 0 s | 0 s | **33 s** | 4 |
| `ak = 1/7` (rational) | 0 s | 0 s | 0 s | **32 s** | 4 |
| `g = ec` (symbolic) | 0 s | 1 s | 0 s | **> 45 min, no return** (two independent runs: `eps3.wl`, `eps5.wl`) | — |

So: *the first three stages are free even with a symbolic parameter*; the entire cost is the
**second** telescoping step, and it explodes on the transition rational → symbolic. **This is a
complexity blocker, not a licence blocker** — a genuinely different diagnosis from the endgame's.
Note also that the deformation lifts the telescoper order from 3 to 4, exactly as expected (the
deformation breaks the BZ degeneracy), so `L(ε)` is an order-4 operator degenerating to
`L_BZ` (order 3) at `ε = 0`.

**The route this opens (costed, not executed).** Because a *rational* specialisation costs 33 s,
`L(ε)` can be reconstructed by **interpolation** from `O(deg_ε L)` rational samples, and the
resulting operator/certificate pair then **verified exactly** (`Expand → 0`) by the §1.2 method.
The search is then heuristic but the verification is a proof — which is all a certificate needs.
Estimated: ~40 samples ≈ 25 min per parameter direction; total-order-3 mixed derivatives in 5
parameters need 35 homogeneous directions, i.e. **≈ 15 kernel-hours for Theorem B**, and
correspondingly more for the weight-5 identity. That is a *scheduling* problem now, not a
mathematical or licensing one.

**Status of Item 1.** `Q`-row **[CERTIFIED]** (new). Theorem B (`P̂_n = Σ T·ŵ₃`) and (T1-top)
(`P_n = Σ T·w5`) remain **[VERIFIED]** — exact over ℚ for `n ≤ 40`, plus 287/687 (resp. 340)
excess equations mod two primes at `N = 600`.

**Left running at hand-off.** `work/lb5/eps5.wl` (PID may differ; kernel started 23:49, external
`timeout 12000`) is still inside `CreativeTelescoping[gb, S[l]-1, {S[n]}]` for the symbolic
`g = ec` deformation. If `work/lb5/eps5.log` has advanced past `s_g gb`, the symbolic route is
alive after all and `s_g_ct2.m` is on disk; if the log is unchanged and no kernel remains, the
timeout fired — **reap the orphan with `kill -KILL` before launching anything else** (§0.2).

---

## §2. ITEM 2 — `(GAP-5)`: CLOSED via route A (depth-minimal `w5`)

### 2.1 The pole calculus at level `a` — exact, and `p`-independent

Let `p >= 5`, `1 <= a < p`, `0 <= b,c <= a`. All arguments of level-`a` letters are `< 3p`, so
each letter has at most a simple pole in `p` and the residue is *explicit*:

| letter | value | pole |
|---|---|---|
| `A_r(b) = H^(r)_{a+b} − H^(r)_b` | `a+b < 2p`, so `p` is the only possible multiple of `p` in range | `α·p^{-r} + ℤ_p`, `α := [a+b >= p]` |
| `B_r(b) = H^(r)_{a−b} − H^(r)_b` | both arguments `< p` | none, `∈ ℤ_p` |
| `C_r = H^(r)_{a+b+c} − H^(r)_{b+c}` | with `ε := ⌊(b+c)/p⌋ ∈ {0,1}`, the only multiple of `p` in `(b+c, a+b+c]` is `(ε+1)p`, present iff `a+b+c >= (ε+1)p` | `κ·θ^{-r}p^{-r} + ℤ_p`, `θ := ε+1 ∈ {1,2}` |
| `N_r = H^(r)_a` | `a < p` | none |

**[PROVED]** `κ = v_p C(a+b+c, a)`. *(Kummer: writing `b+c = εp+ρ`, the addition `a+(b+c)` carries
at position 0 iff `a+ρ >= p` iff `a+b+c >= (ε+1)p`, and cannot carry at position 1 since
`ε + 1 <= 2 < p`.)* Hence, with `α = v_p C(a+b,a)`, `γ = v_p C(a+c,a)`,
```
vT := v_p T(a,b,c) = α + γ + κ .
```

Consequently, writing `u := p^{-1}`, **every** level-`a` letter is
`(a residue) · u^{weight} + (a ℤ_p-symbol)`, so for any ℚ-combination `w5` of monomials of total
weight 5,
```
v5(a,b,c) := w5(a,b,c) − H^(5)_a = Σ_{j=0}^{5} K_j u^j ,    K_j ∈ ℤ_p ,
```
where `K_j` is a polynomial in the `ℤ_p`-symbols whose coefficients are **ℚ-linear in the 448
`w5`-coefficients** and depend on `(a,b,c,p)` **only through the pole pattern** `(α,γ,κ,θ)`.
Note `θ^{-r}` is a `p`-unit for every `p >= 5`, so the whole calculus is `p`-independent.

### 2.2 The pattern census

**[VERIFIED exhaustive, `p <= 23`, `work/lb5/depthcond.py`]** exactly seven patterns are reachable,
with the following minimum of the Lemma-F budget `1 + min(vT,2)` over their cells:

| `(α,γ,κ,θ)` | `vT` | depth cap `1+min(vT,2)` |
|---|---|---|
| `(0,0,0,1)` | 0 | 1 |
| `(0,0,1,1)` | 1 | 2 |
| `(0,1,1,1)`, `(1,0,1,1)` | 2 | 3 |
| `(1,1,0,1)` | 2 | 3 |
| `(1,1,1,1)`, `(1,1,1,2)` | 3 | 3 |

**The census is complete for EVERY `p >= 5`, not merely the tested range. [PROVED]**

* the cap is **pattern-determined**: `cap = 1 + min(α+γ+κ, 2)`, since `vT = α+γ+κ` (§2.1). So no
  minimisation over cells is involved and no larger prime can lower a cap.
* `(1,0,0,·)` and `(0,1,0,·)` are impossible: `α = 1` means `a+b >= p`, and Observation 2 of
  endgame §R1.0 gives `vT >= 2`, i.e. `γ + κ >= 1`. Symmetrically for `γ`.
* `θ = 2` forces `α = γ = κ = 1`: `θ = 2` means `ε = 1` and (for `θ` to matter) `κ = 1`, i.e.
  `a+b+c >= 2p`. Since `c <= a < p`, `a+b >= 2p − c >= 2p − a > p`, so `α = 1`; symmetrically
  `γ = 1`. ∎
* when `κ = 0` the `C`-residue is `0`, so `θ` is irrelevant and the pattern is `(α,γ,0,·)`.

Hence the seven patterns above are exactly the possible ones, for every prime `p >= 5`, and the
`p <= 23` sweep is a confirmation rather than the source of the list.

### 2.3 The depth conditions (DEPTH) and their consistency — the decisive computation

> **(DEPTH).** For each reachable pattern `π` with cap `J(π)`, and each `j > J(π)`, require
> `K_j = 0` **identically in the `ℤ_p`-symbols**.

These are homogeneous ℚ-linear conditions on the 448 coefficients, and they are *sufficient*:
they force `v5 = Σ_{j <= J} K_j u^j` with `K_j ∈ ℤ_p`, i.e. `d5 <= J(π) <= 1 + min(vT,2)`,
at **every** prime `p >= 5` simultaneously. (Treating the symbols as independent is a
strengthening; it costs nothing, as the next line shows.)

**[VERIFIED exact, two primes `q = 33554393, 33554467`, `work/lb5/solve_depth.py`, `N = 600`]**

| quantity | value |
|---|---|
| raw condition rows | 68 |
| rank of the condition rows alone | 42 |
| rank of the fitting system `P_n = Σ T·w5` alone | **313** (unchanged from the endgame) |
| rank of the **joint** system | **324** |
| rank of the **augmented** joint system `[A | rhs]` | **324** |
| **inconsistent?** | **NO** — at both primes |
| dimension of the depth-conditioned family | **448 − 324 = 124** |

So of the 42 independent depth conditions, **31 are already implied by the decomposition
identity itself**, and only **11 are new**. The family that survives them is a nonempty affine
ℚ-subspace of dimension 124 (down from the endgame's 135).

> **Lemma W5-DEPTH. [PROVED, modulo the linear-algebra certificate above]**
> The decomposition family for `P_n = Σ_{k,l} T(n,k,l) w5(n,k,l)` contains a 124-dimensional
> affine subfamily on which, for **every** prime `p >= 5` and every cell `0 <= b,c <= a < p`,
> ```
> d5(a,b,c) := max(0, −v_p(w5(a,b,c) − H^(5)_a))  <=  1 + min(v_p T(a,b,c), 2) ,
> ```
> provided the chosen representative's coefficients are `p`-integral.

### 2.4 The denominator obstruction, and its removal

The only remaining representative-dependence is the set of primes dividing coefficient
**denominators**: a coefficient with `p` in its denominator inflates `d5` at that one prime and
nowhere else. (This is exactly the artefact the endgame flagged for `p = 11`.) A sweep over 13
pivot orders (`work/lb5/solve_depth2.py`) gives:

| order | terms | denominator primes | bad primes (`>= 5`) |
|---|---|---|---|
| `pref` (endgame preference order) → `w5_canon2.json` | **126** | `{2,3,5}` | `{5}` |
| `top_asc` | 126 | `{2,3,5}` | `{5}` |
| `nB_desc` → `w5_dm_nB_desc.json` | **134** | `{2,3,16703}` | `{16703}` |
| `rand4` → `w5_dm_rand4.json` | 129 | `{2,3,1129}` | `{1129}` |
| `rand2` | 125 | `{2,3,4721}` | `{4721}` |
| `nfac_desc` | 129 | `{2,3,121441}` | `{121441}` |
| `prefrev` | 129 | `{2,3,7,121441,3278837}` | `{7, …}` |

Any two with **disjoint** bad-prime sets already cover all `p >= 5`. Better, they can be
**combined into one**:

> **[PROVED — `work/lb5/make_allp.py`]** If `x1, x2` lie in the depth-conditioned family, `x1` is
> `p`-integral for all `p >= 5` except `P1` (max denominator exponent `e1`) and `x2` except `P2`
> (exponent `e2`), `P1 ≠ P2`, put `d = x2 − x1` and choose an integer `t` with
> `t ≡ 1 (mod P1^{e1+1})`, `t ≡ 0 (mod P2^{e2+1})` (CRT). Then `x = x1 + t·d` lies in the family
> and is `p`-integral for **every** `p >= 5`:
> at `P1`, `x = x2 − (1−t)d` with `v_{P1}((1−t)d) >= (e1+1) − e1 = 1`;
> at `P2`, `x = x1 + t·d` with `v_{P2}(t·d) >= (e2+1) − e2 = 1`;
> at every other `p >= 5`, `x1` and `d` are `p`-integral and `t ∈ ℤ`. ∎

Applied to `w5_canon2` (`P1=5, e1=1`) and `w5_dm_rand4` (`P2=1129, e2=1`), `t = 14021051`:

> **`work/lb5/w5_allp.json` — 178 terms, denominators supported on `{2,3}` only,
> numerators <= 11 digits.**

### 2.5 Verification — `[VERIFIED, 0 failures]`

`work/lb5/verify_depth.py` runs three independent exact tests on a saved representative:
**(V1)** the exact-ℚ ladder identity `P_n = Σ_{k,l} T(n,k,l) w5(n,k,l)`;
**(V2)** the depth sweep `d5 <= 1 + min(vT,2)` over *all* cells;
**(V3)** the decisive cell-by-cell `(GAP-5)` test
`v_p(Tcal(b,c) − (Q_n/Q_a)·T(a,b,c)) >= 1 + d5(b,c)`, computed mod `p^10` from the true fibre
tables.

| representative | (V1) | (V2) `p = 5,7,11,13,17,19,23(,29)` | (V3) `p = 5,7,11,13` |
|---|---|---|---|
| `w5_dm_nB_desc` (134 terms) | `n <= 24`, 0 | max `d5 = 3`, **0** violations, min slack **0** | 270 / 707 / 5379 / 10634 cells, **0** failures |
| `w5_dm_rand4` (129 terms) | `n <= 20`, 0 | max `d5 = 3`, **0** violations, min slack **0** | **0** failures |
| **`w5_allp` (178 terms)** | **`n <= 34`, 0** | max `d5 = 3`, **0** violations, min slack **0**, up to `p = 31` | **0** failures |
| `w5_canon2` (126 terms) | `n <= 26`, 0 | 0 violations for `p >= 7`; 29 at `p=5` (the `5`-denominator artefact) | 0 failures for `p >= 7`; 15/270 at `p=5` |

Compare the endgame's `(GAP-5)` table, i.e. the *same* test run on the previous representatives:

| representative | p=5 | p=7 | p=11 | p=13 |
|---|---|---|---|---|
| 130-term (closeout) | 1/270 | 18/707 | 3385/5379 | 1285/10634 |
| 106-term canonical (endgame R2) | 34/270 | 91/707 | 3503/5379 | — |
| **depth-minimal (this session)** | **0** | **0** | **0** | **0** |

**Sharpness.** `min slack = 0` at every prime: the value `d5 = 1 + min(vT,2)` is *attained*.
So (DEPTH) sits exactly at the edge of what Lemma F supplies — nothing is wasted, and no weaker
condition would do. Lemma F was already known to be sharp (endgame §R1.4); this shows the two
sharpnesses meet exactly.

### 2.6 Canonicity, re-pinned

The endgame found that *sparsest ≠ depth-minimal* and that depth is load-bearing. The correct
canonicalisation order, established here, has **three** criteria, in this order:

1. **depth-minimality** — the 42 independent (DEPTH) conditions of §2.3 (11 of them new);
2. **`p`-integrality for every `p >= 5`** — denominators supported on `{2,3}`, achievable by
   §2.4 and equally load-bearing (a stray `p` in a denominator destroys the bound at that one
   prime — this is what killed both earlier representatives, and it is *not* visible in any
   sparsity or weight statistic);
3. **the endgame's preference order** (fewest factors, fewest `B`, fewest `C`, fewest `N`,
   heaviest letter first, label tie-break) — the rref pivot rule, which is what sparsity buys.

Under 1+3 alone the canonical representative is **`w5_canon2.json` (126 terms, denominators
`{2,3,5}`)** — valid for every `p >= 7`. Under 1+2+3 the explicit witness produced here is
**`w5_allp.json` (178 terms, denominators `{2,3}`)** — valid for every `p >= 5`. Pinning the
*unique* 1+2+3-minimal point requires a lattice reduction inside the 124-dimensional family
(the ℤ[1/6]-points form a coset of a lattice); that is cosmetic and is left open.

### 2.7 Consequence

> **(GAP-5) is CLOSED.** With `w5 = w5_allp` (or `w5_dm_nB_desc` for `p ≠ 16703`, etc.), the
> weight-5 ledger requirement `v_p(Tcal(b,c) − Λ·T(a,b,c)) >= 1 + d5(b,c)` is implied
> **cell by cell** by Lemma F's `p^{2+min(vT,2)}`, because (DEPTH) forces
> `1 + d5 <= 2 + min(vT,2)` everywhere. Route B (thin-set cancellation, the weight-5 twin of
> `(MID)`) is **not needed**.

Route (ii) — "prove Lemma F one order deeper" — remains impossible (Lemma F is sharp); the fix
was on the `w5` side exactly as the endgame predicted, and it is a *linear* fix, exactly as the
endgame predicted.

---

## §3. Reproduction — scripts added this session (all in `work/lb5/`)

| file | what it does |
|---|---|
| `eps2.wl` | two-step CT gate on the undeformed `T`; produces `g0_ann.m`, `g0_ct1.m`, `g0_gb.m`, `g0_ct2.m` |
| `eps4.wl` | **stage V**: independent exact verification of all `g0` certificates (`Expand/Together → 0`) and of `telescoper = L_BZ`; **stage R**: rational-parameter deformation speed probes |
| `eps5.wl` | symbolic-parameter deformation runs (`s_g`, `s_ak`, `s_bk`) — CT in `l` does not return |
| `depthcond.py` | the level-`a` pole calculus: pattern census + the `u`-expansion of every basis monomial; builds the (DEPTH) rows |
| `solve_depth.py` | fit + (DEPTH) joint solve, two primes, CRT + rational reconstruction → `w5_canon2.json` |
| `solve_depth2.py` | pivot-order sweep (13 orders) reporting denominator primes → `w5_dm_*.json` |
| `make_allp.py` | CRT combination of two representatives with disjoint bad primes → `w5_allp.json` |
| `verify_depth.py` | the three-test verifier (V1 ladder / V2 depth sweep / V3 cell-by-cell (GAP-5)) |
| `w5_canon2.json` | depth-minimal, preference-canonical, 126 terms, denominators `{2,3,5}` |
| `w5_dm_nB_desc.json`, `w5_dm_rand4.json`, `w5_dm_rand2.json`, … | depth-minimal, one bad prime each |
| `w5_allp.json` | depth-minimal, denominators `{2,3}`, valid for **all** `p >= 5` |
