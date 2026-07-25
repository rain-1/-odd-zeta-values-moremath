# CERTS_RESUME — precise resume state for task P1e

**Date:** 2026-07-25. Read `work/PHASE2_CERTS.md` first (findings), then this file (how to
continue without rediscovery).

---

## 0. Operational facts that cost time to (re)learn

* **Seats.** 3 kernels total; one is permanently the MCP server (`pgrep -a WolframKernel`, the
  one whose command line mentions `PacletSymbol["Wolfram/AgentTools",...]`). So **2 standalone
  kernels**. Standalone kernels ignore `SIGTERM`; `timeout N math < f.wl` kills only the shell
  wrapper. Reap with `kill -KILL <WolframKernel pid>`. Map a kernel to its script by start time
  (`ps -o pid,etime,cmd`) — the wrapper's command line does not name the file (stdin).
* **⚠ THE BIGGEST TIME SINK OF THIS SESSION.** `math < file.wl` reads stdin **line by line** and
  evaluates each line the moment it parses. A multi-line assignment whose *first line is already
  syntactically complete* is **silently truncated**:
  ```
  w3hat = HarmonicNumber[n,3] + AA[3,k] + AA[3,l]        <- w3hat became THIS
          - (1/4)(AA[2,k] AA[1,k] + ...)                 <- evaluated and discarded
  ```
  Wrap every multi-line expression in parentheses **and assert on the result**. All scripts here
  now log `Length[Cases[w, HarmonicNumber[__], Infinity]]` and abort if it is wrong.
  **The Wolfram MCP evaluator behaves the same way** — this bit a second time there, silently
  producing an `Eletters.m` missing its `ρ` and `σ` terms, on which two kernels then ran for
  twenty minutes. It was caught only by evaluating the letter form against an independently
  built copy of `E(v)` at an *integer* point (rational-point numerics are useless here: the
  Binomial form at rational arguments needs `$MaxExtraPrecision` far beyond the default and
  silently returns garbage). **Cross-check every derived object at an exact-arithmetic point.**
* **Load recipe** (unchanged, works): `Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"]`
  under `math < file.wl`. Not the local `zeta-math-2/RISC/` copy; no `Block[{Quit=…}]` trick.
* **The MCP kernel cannot load HolonomicFunctions** (exceeds its wall even at
  `timeConstraint -> 120`). But it **is** perfectly usable as a *third, free* worker for the
  RISC-free verification harness — that is how the Q-row checks in §3 were run. Use it.
* `TimeConstrained` does **not** interrupt `CreativeTelescoping`. The only reliable bound is
  `Support -> {...}`, which turns the step into a finite linear solve that terminates.
* `OreSys.m`, `MultiSum.m`, `Guess.m`, `fastZeil.m` are all in `/home/ubuntu/riscergosum/RISC/`.
  `Method -> Zuercher` (OreSys uncoupling) was tried and did **not** beat the default.

## 1. Cost model — measured this session

| object | `Annihilator` | first CT | verdict |
|---|---|---|---|
| `T` | 0 s | elim k: 0 s | step 2: 4 s, order 3 = `L_BZ` |
| `T·A₁(k)` | 0 s | elim **l**: 81 s (Gröbner 21 s) | cheap: no letter involves `l` |
| `T·A₁(k)` | 0 s | elim k: >4 min no return | |
| `T·C₁` | 0 s | elim k: >4 min (default), >7 min (Zuercher) | coupling letter, worst case |
| `T·(H⁽³⁾+A₃(k)+A₃(l))` | 1 s | elim k: >16 min no return | |
| `T·v` (folded weight, rank 12) | ~~**124 s**, 7 gens~~ — **WITHDRAWN, see §11.6** (`Put`-time artifact; re-measured **TIME ABORT 600 s**) | elim l, `Support` box(1,1) 13 s / (2,2) 12 s / (2,3) 194 s, **no telescoper** | boxes terminate but grow fast |

**Rule:** eliminate first a variable that **no letter depends on**. `ŵ₃` has none; the folded `v`
is the best compromise (only 4 of its 12 closure monomials move under `S_l`, by one level).

`CreativeTelescoping[ann,{S[k]-1,S[l]-1},…]` is **not implemented** — `$Failed` even for the
undeformed `T` with `Support -> {1,S[n],S[n]²,S[n]³}`, which provably contains `L_BZ`. Read
nothing into that `$Failed`.

## 2. What is now [CERTIFIED] — start from here, do not redo

> **Q-row single certificate.** `L_BZ·T = Δ_k(ρT) + Δ_l(σT)`, `ρ, σ` explicit rational functions,
> `work/lb5/Qrow_rhosigma.m` (`LeafCount` 10553 / 1819). Checked to exactly `0`
> **twice**: inside RISC (`certR.log`) and in a kernel that never loaded RISC (MCP evaluator,
> using `verifycore.wl`'s own `grat`-based shift calculus).

Extraction facts worth keeping: for the undeformed `T`, `gb === ct1-telescopers` (no Gröbner
cofactor chain needed), `OreReduce[QQ + (S_l−1)·RR, gb, Extended->True]` gives remainder `0`
with multiplier `ff = 1`, and `QQ = L_BZ` **exactly** (ratio `{1,1,1,1}`).

> **Caveat on the boundary lemma (read this).** Its proof is a pole-order count and is exact,
> but an end-to-end *numerical* confirmation (`Σ_{k,l≤n+3} E(v) = 0` at small `n`) was attempted
> and **not completed**: at `k ∈ {n+1,n+2,n+3}` the value of `E(v)` is finite only after a
> cancellation between the `v(n+j)` and `−v` parts (each individually infinite — `B₁(k)` has a
> pole there, `T` a double zero), and `Limit` on the letter form returns `Indeterminate`. Collect
> the `−v` terms first: their total coefficient is
> `Σ_{j≥1} c_j T(n+j) − ρ|_{k+1}T(n,k+1,l) − σ|_{l+1}T(n,k,l+1) = −(c₀ + ρ + σ)T` by the Q-row
> certificate, which has a simple zero at `k = n+1`. Either do the limit that way, or re-derive
> `E(v)` in a pole-free normalisation, before calling the chain closed.

> **Boundary lemma.** `ρ(n,0,l) = 0`, `σ(n,k,0) = 0`; `denom(ρ)` has factors
> `(1+k+l)(k−n−1)(k−n−2)(k−n−3)(l−n−1)(l−n−2)(l−n−3)(1+n)(2+n)(2+l+n)(3+l+n)` and `denom(σ)` the
> `l`-only analogue. `T` has a *double* zero at every integer `k > n`, `v` at worst a simple pole
> there and none in `l`. Hence on the box `0 ≤ k,l ≤ K`, `K ≥ n+3`, every telescoped boundary
> term vanishes and every interior value is finite. **[PROVED]**

> **Reduction.** `L_BZ·(Σ_{k,l} T ŵ₃) = Σ_{k,l} E(v)` for all `n ≥ 0`, where
> ```
> v   = H⁽³⁾_n + 2A₃(k) − ½A₂(k)A₁(k) − (3/2)A₂(k)B₁(k) − ¾A₂(k)C₁ − ¼A₂(k)A₁(l)
> E(v)= Σ_{j=1}^{3} c_j T(n+j)[v(n+j)−v] − ρ|_{k→k+1}T(n,k+1,l)[v(k+1)−v]
>                                        − σ|_{l→l+1}T(n,k,l+1)[v(l+1)−v]
> ```
> and `Σ T ŵ₃ = Σ T v` by the `k↔l` symmetry of `T` (exact rearrangement of a finite sum).
> **Theorem B ⇔ `Σ_{k,l} E(v) = 0` for all `n`.** **[PROVED]**

> **`E(v)` is LINEAR in the letters, and is now COMPUTED.** After normalising every `HarmonicNumber` to a base
> argument (`certS.wl`'s `hb`), `E(v)` contains exactly **9 distinct harmonic symbols**
> — `H_k, H_l, H_{k+l}, H_{n−k}, H_{n+k}, H_{n+l}, H_{n+k+l}, H⁽²⁾_k, H⁽²⁾_{n+k}` — each to
> **degree 1**. So `E(v) = T·(c₀ + Σ_{i=1}^{9} c_i H_i)` with explicit rational `c_i`, i.e. a
> hypergeometric term times a rank-≈6 `∂`-finite factor (the letters `A₁(k), A₂(k), B₁(k), C₁,
> A₁(l)`), versus rank 12 for `T·v` and 19 for `T·ŵ₃`. There are **no cross terms**, and the four
> letter relations `c[H_l]+c[H_{n+l}] = c[H⁽²⁾_k]+c[H⁽²⁾_{n+k}] = c[H_{k+l}]+c[H_{n+k+l}] =
> c[H_k]+c[H_{n+k}]+c[H_{n−k}] = 0` all hold exactly, so
> ```
>     E(v)/T = c₀ + α·A₁(k) + β·A₂(k) + γ·B₁(k) + δ·C₁ + ε·A₁(l)
> ```
> **Saved: `work/lb5/Eletters.m` = `{c₀, α, β, γ, δ, ε}`**, `LeafCount`
> 66499 / 22317 / 44011 / 22317 / 22317 / 22317; also `Ecanon.m` in raw-symbol form.
> Verified: `T·(letter form) − E(v) = 0` exactly at `(n,k,l) = (5,2,3), (6,1,4), (4,3,0)`,
> against `R_E.m` built independently in the RISC kernel.
> **Computational trap:** `Expand`ing `E/T` gives an **11-million-leaf** expression;
> `Together[Coefficient[…]]` on the *unexpanded* product takes under a second. Never expand it.

## 3. The finish — non-circular, and cheap

`P̂` **is** the `L_BZ`-solution with `P̂₀ = 0, P̂₁ = 101/4, P̂₂ = 344923/96`; `L_BZ` is
non-singular on `n ≥ 0` (leading `2(n+3)⁵(2n+5)a₀(n)`, trailing `(n+1)⁵(n+2)a₀(n+1)`,
`a₀(x) = 41218x³+198849x²+320790x+173057 > 0` for `x ≥ 0`).

`Σ T ŵ₃ = P̂_n` is **exact for `n ≤ 80`** (`seqdata.py 80` / `seqdata.json`), so
`F_n := Σ_{k,l} E(v) = L_BZ·(Σ T ŵ₃)` is **known to be 0 for `n ≤ 77`** — an established fact,
not the thing being proved. Therefore:

> certify **any** operator `L'` with `L'·F = 0`; if `ord(L') ≤ 77` and the leading coefficient of
> `L'` has no integer root in the relevant range, then `F ≡ 0` and Theorem B follows.

In particular an order-0 telescoper (`Support -> {1}`) is *not* required — any `L'` will do.
`seqdata.py NMAX` extends the exact range at `O(N³)` cost if a larger `ord(L')` shows up.

## 4. Where the computation stands, and what to run next

### 4.0 The plan that reduces everything to RANK-1 telescoping — `certU.wl`

This is the key structural observation of the session and the route to finish on.
Write `E(v)/T = c₀ + Σ_m e_m·m` over the five single letters
`m ∈ {A₁(k), A₂(k), B₁(k), C₁, A₁(l)}`. For any operator `M = Σ_j M_j(n) S_n^j`,

```
M·E = Σ_m [ Σ_j M_j e_m(n+j) T(n+j) ]·m
    + Σ_j M_j T(n+j) [ c₀(n+j) + Σ_m e_m(n+j)·d_m^(j) ] ,     d_m^(j) := m(n+j) − m
```

and every `d_m^(j)` is a **rational function**, because each `m` is a *single* letter and a
shift changes a single letter by a rational function. Hence:

* the letter-`m` component of `M·E` telescopes **iff `M` is a telescoper for the
  HYPERGEOMETRIC double sum `Σ_{k,l} e_m(n,k,l) T(n,k,l)`** — a rank-1 problem, i.e. exactly the
  Q-row computation, which costs ~4 s;
* so take `M := LCLM(M_α, M_β, M_γ, M_δ, M_ε)` over the five letters (five rank-1 telescopers);
* the leftover second line is a rational multiple of shifts of `T`, i.e. a **hypergeometric**
  term `G`; a sixth rank-1 telescoping gives `N` with `N·(Σ_{k,l} G) = 0`;
* therefore `M·F = Σ_{k,l} G` and `N·M·F = 0` with `F = Σ_{k,l} E(v)`.

`F_n = 0` is already known exactly for `n ≤ 77` (§3), so if `ord(N·M) ≤ 77` — plausible, since
each `M_m` should have order ≈ 3–8 and the `LCLM` of five such is ≤ ~30 — **Theorem B closes**.
If `ord(N·M) > 77`, extend the exact range further with `seqdata.py NMAX` (cost `O(N³)`; `N = 80` took about four minutes).

The only step that is not obviously cheap is the `LCLM`; if it blows up, note that one does not
need the *minimal* common left multiple — any common left multiple works, e.g. an iterated
`LCLM` of pairs, or simply enlarging the exact range and using the direct sum bound
`ord ≤ Σ_m ord(M_m)`.

**Measured on the CORRECTED coefficients** (`certU_alpha_beta_gamma.log`,
`certU_delta_eps_c0.log`), identically for `α` and `δ`:

| stage | time | result |
|---|---|---|
| `Annihilator[T·e_m, {S[n],S[k],S[l]}]` | **136 s** | **3 generators — rank 1 confirmed** |
| `CreativeTelescoping[ann, S[k]-1, {S[n],S[l]}]` | **412 s** | 3 telescopers |
| `OreGroebnerBasis[ct1, OreAlgebra[S[n],S[l]]]` | **56 s** | `gb === ct1-telescopers` → **True** |
| `CreativeTelescoping[gb, S[l]-1, {S[n]}]` | still running at hand-off (> 15 min) | — |

`gb === ct1` again means **no Gröbner cofactor chain is needed** — `certX.wl` composes the
certificate from the `OreReduce` cofactors alone, exactly as for the Q-row. Budget roughly
25–45 min per letter, six letters, two kernels ⇒ ~1.5–2 kernel-hours for the whole set, then the
`LCLM`.

`certU.wl` now takes `LABS` from the environment, so the six letters can be split across the two
available kernels: `LABS=alpha,beta,gamma math < certU.wl` and `LABS=delta,eps,c0 math < certU.wl`
(logs `certU_alpha_beta_gamma.log`, `certU_delta_eps_c0.log`). The `LCLM` step runs only in a
process that has at least five telescopers, so do the final `LCLM` from the saved `U_Ms_*.m`.

**Boundary, again.** Each rank-1 certificate `M_m·(e_m T) = Δ_k(ρ_m e_m T) + Δ_l(σ_m e_m T)`
needs its own boundary argument before it may be summed. Do exactly what §2 did for the Q-row:
check `Together[ρ_m e_m /. k->0] == 0` and `Together[σ_m e_m /. l->0] == 0`, factor the
denominators, and compare pole orders against `T`'s double zeros at integer `k > n`. `certX.wl`
saves `ρ_m, σ_m` precisely so this is a one-liner per letter. Do **not** skip it — it is the
step that is easiest to assume and hardest to notice missing.

**After `certU`:** run `math < certX.wl`. For each label it composes the two-step certificate
into single-certificate form `M_m·(e_m T) = Δ_k(ρ_m e_m T) + Δ_l(σ_m e_m T)` and prints the
exact check (must be `0`), saving `<label>_rhosigma.m`. Then re-check RISC-free with
`verifycore.wl` (`loadEcanon` gives the `E`-kernel; `applyOp` + `zeroReport` do the rest).


* `work/lb5/certT.wl` — **the run to make**. `MODE=box math < certT.wl` (Support ladder,
  terminates) and `MODE=unc math < certT.wl` (unconstrained step 1). It loads `Eletters.m`,
  builds `T·(c₀+αA₁(k)+βA₂(k)+γB₁(k)+δC₁+εA₁(l))`, takes its annihilator, eliminates `l`
  first (cheap: only `C₁, A₁(l)` move under `S_l`), then `k` with `Support -> {1,…,S[n]^d}`,
  `d = 0,…,10` — `d = 0` would mean `E` is exact, which is the ideal outcome but not required.
  Logs `certT_box.log`, `certT_unc.log`.
* `work/lb5/certS.wl` — earlier version that recomputes the canonical form each run. Builds `E(v)` in canonical form (9 symbols,
  degree 1), checks the canonicalisation against the raw expression, then
  `Annihilator[T·(c₀+Σ c_i H_i)]` and a `Support`-bounded box ladder eliminating `l` first,
  then `S[k]` with `Support -> {1,…,S[n]^d}`, `d = 0..6`. Log: `certS.log`.
* `work/lb5/certR.wl` — the same but feeding the *raw* `E(v)` to `Annihilator`; it was still
  inside that call after 9 minutes, which is why `certS` exists. Keep `certS`.
* If the box ladder exhausts: enlarge `box[A,B]` (each attempt terminates, cost grows steeply —
  13 s, 12 s, 194 s for (1,1),(2,2),(2,3) on the rank-12 object), or try `l`↔`k`, or apply the
  **same weight-lowering trick again**: `E(v)` is linear in the letters, so for each letter `L`
  the bracket `L(shifted) − L` is a *rational function*, and one more application of a
  hypergeometric certificate (for `T·c_i`, rank 1, cheap) reduces to weight 0.

## 5. (b) (T1-top) — what is and is not true

* The target is **`w5_allp` specifically** (178 terms, denominators `{2,3}`). `PHASE2_CERTS.md`
  §1 **proves** the fit kernel contains no pointwise-zero element (the 448 basis monomials have
  cell-matrix rank 448 mod 33554393, hence over ℚ). "Certify one representative, get the others
  free" is **false** — do not use it.
* Evidence upgraded this session (`w5rec.py`): evaluating `Σ_{k,l} T·w5_allp` mod
  `q = 33554393` and `33554467` for `n = 0..750` gives **0 mismatches against the exact ladder
  `P_n` for every `n ≤ 360`** and **`L_BZ` residual 0 at all 748 values**; its minimal recurrence
  is `(order 3, degree 9)` with nullity 1, i.e. exactly `L_BZ`. The fitting system only
  constrained `n ≤ 600`, so ~147 of these are genuine excess checks.
* Route for the certificate: the §2 reduction applies verbatim with `w₅` in place of `ŵ₃` —
  fold by `k↔l`, subtract `w₅·(Q-row certificate)`, and `E(w₅)` has weight ≤ 4. Five iterations
  of the same step reach weight 0 (the certified Q-row). Each step needs the certificate of a
  *hypergeometric* term `T·(rational)`, which is rank 1 and cheap. This is the only route with a
  plausible cost profile; the direct `Annihilator[T·w₅]` closure spans several hundred monomials.

## 5.5 State of the running computation at hand-off

Two standalone kernels were left inside
`CreativeTelescoping[gb, S[l]-1, {S[n]}]` for the letters `α` (kernel 1) and `δ` (kernel 2),
about 15 minutes in, 2.2 GB resident each. If they were reaped when the session ended, just
restart:

```
cd /home/ubuntu/fable-episode-2/zeta-math-2/work/lb5
LABS=alpha,beta,gamma nohup timeout 40000 math < certU.wl > certU1.stdout 2>&1 &
LABS=delta,eps,c0     nohup timeout 40000 math < certU.wl > certU2.stdout 2>&1 &
```
Nothing is lost by restarting — the expensive inputs (`Qrow_rhosigma.m`, `Eletters.m`) are on
disk and the per-letter results are `Put` as soon as each letter finishes (`U_<label>.m`), so a
restart only redoes letters that had not completed. Check `pgrep -a WolframKernel` first and
`kill -KILL` any orphan.

## 6. Files added this session (all in `work/lb5/` unless noted)

| file | what |
|---|---|
| `wlcheck.py` | **run this on every `.wl` before launching it** — flags multi-line expressions that `math < file` would silently truncate (all current scripts pass) |
| `ptrank.py` | cell-level rank of the 448-monomial `w₅` basis → 448 (§1 of the report) |
| `seqdata.py`, `seqdata.json` | exact `U₁..U₅`, `Σ T ŵ₃`, check against `P̂_n`, `n ≤ 80` |
| `guessrec.py` | minimal-recurrence search: `Σ T ŵ₃ → (3,9)`, each `U_i →` none with `r ≤ 12, d ≤ 30` |
| `w5rec.py` | forward check of `w5_allp` to `n = 750`, two primes |
| `verifycore.wl` | **RISC-free** exact verification kernel (shift calculus, harmonic normaliser, inert `OrePolynomial` reader, hand-rolled Ore algebra) |
| `certV.wl` | verifier driver (V-A function level, V-B operator level, V-C vs `L_BZ`, V-D boundary) |
| `certW.wl` | certificate composition via `Extended -> True` cofactors |
| `certR.wl`, `certS.wl` | Route R: the Q-row single certificate and `E(v)` |
| `certT.wl` | telescoping on `E(v)` in rank-6 letter form (`MODE=box` / `MODE=unc`) |
| `certU.wl` | **the rank-1 route (§4.0)** — six hypergeometric telescopers + `LCLM` |
| `certX.wl` | composes each `certU` certificate into single-certificate form and checks it exactly |
| `certA…certK.wl` | earlier attempts + the cost ladder; logs `cert*.log` |
| `Qrow_rhosigma.m` | **the certified `{ρ, σ}`** |
| `Eletters.m` | **`{c₀, α, β, γ, δ, ε}` = `E(v)/T` in letter form** — the object to telescope |
| `Ecanon.m` | `E(v)/T` in raw-harmonic-symbol form |
| `../PHASE2_CERTS.md` | the report |

---

# 7. STATE AT 2026-07-25 02:30 (P1e continuation) — READ THIS BEFORE §4

Full write-up: `work/PHASE2_CERTS.md` §§8–12. The three things that change what you should run:

### 7.1 `E(v)` is RANK 3, and only THREE telescopers are needed (§11)

`γ = 3α`, `δ = (3/2)α`, `ε = (1/2)α` **exactly** (`Together` of the ratios). So

```
    E(v)/T = c₀ + β·A₂(k) + α·Ψ ,   Ψ = A₁(k) + 3B₁(k) + (3/2)C₁ + (1/2)A₁(l)
```

and `M_γ = M_δ = M_ε = M_α`. **Run `LABS=alpha`, `LABS=beta`, `LABS=c0` — nothing else.**
The 01:30 launch (`LABS=alpha,beta,gamma` / `LABS=delta,eps,c0`) spends most of its time on
redundant letters; a reallocation was attempted and blocked by the permission system.
The structural reason: every product term of `v` has the same left factor `A₂(k)`, and only
`(A₂^{shift} − A₂)` produces a bare single letter, with an `X`-independent prefactor.

### 7.2 §4.0's rank-1 argument has a gap — one Abel summation per branch (§9)

`m·(Δ_k X_m + Δ_l Y_m)` does **not** telescope, because `m` depends on `k, l`. Use
`m Δ_k X = Δ_k(mX) − (Δ_k m)X|_{k+1}`; `Δ_k m` is rational, so everything stays rank 1, but the
final hypergeometric `G` must include the Abel terms. `certZ.wl` implements this.

### 7.3 The boundary lemma is confirmed, and §4quater was wrong in two places (§8)

`ρ, σ` have **double** poles at `k−n, l−n ∈ {1,2,3}` (`FactorList[…][[All,1]]` had hidden the
exponents), and `E(v)` therefore has a **simple pole at every cell with `k₀ ≥ n₀`** — it is *not*
finite on the box. `m2bnd.wl` (`n₀ = 1,2,3,4,5`): all negative `ε`-parts cancel across the box and
the `ε⁰` total is exactly `0`, with no dependence on the Taylor data of `H⁽ʳ⁾`. Always keep the
`Δ`-terms as telescoping sums; never split them into cell values.

### 7.4 Files added (all `work/lb5/`)

| file | what |
|---|---|
| `m2bnd.wl` / `m2bnd.log` | the `ε`-regularised boundary check (M2), `n₀ = 1..5` |
| `certY.wl` | harvest the telescopers, `LCLM`, order/degree, `L_BZ` right-factor test |
| `certZ.wl` | **final assembly**: cofactors, Abel-corrected `G`, telescoper `N`, `L' = N**M` |
| `certVU.wl` | RISC-free exact check of each per-letter certificate + boundary data |
| `certUb.wl` | checkpointed certU with `ORD=kl|lk` and a **terminating** `Support` ladder for ct₂ |
| `certT3.wl` | the DIRECT attack on the rank-3 form — try this before the LCLM assembly |
| `make_w5m.py` / `w5folded.m` | folded `w5_allp`, verified `Σ T v₅ = P_n` at `n = 2,3,4` |
| `expel.wl` / `Ecoef.txt` | `e_m` as coefficient tables mod `p` |
| `predrec.py` | **superseded** (wrong summation box) — machinery reusable |
| `seqdata150.json`, `seqdata300.json` | `Σ T ŵ₃ = P̂_n` exact for `n ≤ 300` ⇒ `F_n = 0` for `n ≤ 297` |

### 7.5 What to run next, in order

1. `MODE=box math < certT3.wl` — rank-3 direct route. If it returns a telescoper, §§9–11 are moot.
2. `LABS=alpha DMAX=12 math < certUb.wl`, `LABS=beta …`, `LABS=c0 …` (checkpointed; the
   `Support` ladder terminates, the unconstrained ct₂ cannot be interrupted).
3. `math < certX.wl` → `<lab>_rhosigma.m`; then `Get["certVU.wl"]` in the MCP kernel (RISC-free).
4. `math < certY.wl` (LCLM), then `math < certZ.wl` (Abel + `N` + `L' = N**M`).

### 7.6 `α` has a closed form (PHASE2_CERTS §11.4)

`α = −Λ/2` with `Λ = Σ_{j=1}^{3} c_j (T(n+j)/T) a_j − ρ|_{k→k+1}(T(n,k+1,l)/T) a′`,
`a_j = Σ_{i=1}^{j}1/(n+i+k)²`, `a′ = 1/(n+k+1)² − 1/(k+1)²` (checked to exactly `0`).
So `T·α` is a combination of shifts of `T` weighted by **single simple fractions** — if the
`Support` ladder on `T·α` is slow, telescope those four pieces separately and `LCLM` them.

### 7.7 Kernel state at hand-off

`828900` (`LABS=alpha,beta,gamma`) and `829062` (`LABS=delta,eps,c0`) were both inside the
**unconstrained** `CreativeTelescoping[gb, S[l]-1, {S[n]}]` for `alpha` / `delta` from 01:40:30,
still running at 02:25 (45 min, 2.5 GB each, no output). That call **cannot be interrupted**; the
`Support` ladder in `certUb.wl` is the terminating replacement. `delta` is redundant (§7.1).
`kill -KILL` was attempted at 02:19 and **blocked by the permission system**, so nothing was
reaped. Reap both, then run the three jobs of §7.5.

---

# 8. STATE AT 2026-07-25 ~04:00 (P1e session 3) — READ THIS BEFORE §7

`work/PHASE2_CERTS.md` §§13–14 is the write-up. §7's restart order is **superseded**: do not run
`certT3.wl`, `certUb.wl` or `certZ.wl` — the first is now known to be infeasible, and the other
two are the route the τ-split replaces.

## 8.1 Two hard negatives, do not repeat them

* **`certT3.wl` (monolithic rank-3) is OOM-death.** 50 minutes inside `Annihilator`, killed by the
  kernel OOM-killer at **14.4 GB anon-rss** on a 15 GB box (`dmesg` confirms). *Rank is not the
  cost; coefficient size is* — `E(v)` is rank 3 but its coefficients are 66499 / 44011 / 22317
  leaves. `Annihilator` on the **rank-12** `T·v` costs 124 s because its coefficients are small.
* **The unconstrained last `CreativeTelescoping`** for the letter `α` ran **79 minutes across two
  sessions** without returning and cannot be interrupted. It was `kill -KILL`ed at 03:28 to free
  memory for the priority job. Do not restart it.

## 8.2 A NEW parse trap — a line ending in `<|`

```
tauW = <|                <-  Syntax::sntxf: "" cannot be followed by "uW = <|".
  "n1" -> ... |>;            The assignment is DROPPED; tauW stays an inert Symbol.
```
`<` and `|` are standalone operators, so `x = <|` is a *locally decidable* syntax error rather than
an incomplete expression. Splitting an association after a **comma** (`x = <|"a" -> 1,`) is fine.
`wlcheck.py` now has `assoc_delta()` and reports this as FATAL; re-run it on every `.wl`.
Two kernels ran 4 minutes on the resulting wrong object before the split assertion caught it —
**always give a derived object an assertion that aborts the run.**

## 8.3 The τ-split — the route to finish on

`E(v) = Σ_τ F_τ` over the five shift terms `τ ∈ {n₁, n₂, n₃, kk, ll}` of `certS.wl`'s definition;
each `F_τ = G_τ·(p_τ + q_τ A₂(k) + r_τ Ψ)` is ∂-finite of rank ≤ 3 with a **small** weight
(`LeafCount` 84 / 86 / 66 / 12471 / 2255, against 132917 for the monolith). Formulas in
`PHASE2_CERTS` §13.3; code in `certP.wl`.

> **[CERTIFIED — RISC-free and SYMBOLIC in `ℚ(n,k,l)[hh…]`]**, `certPv0.wl`, one MCP evaluation:
> `Σ_τ F_τ/T − (c₀ + β A₂(k) + α Ψ) = 0` (9 hh-symbols, 11 coefficient classes, 0 non-zero) and
> `(c₀ + β A₂(k) + α Ψ) − Ecanon = 0`. Also re-derives `{γ/α, δ/α, ε/α} = {3, 3/2, 1/2}`.

**No Abel correction** (§9) is needed on this route: the letters are never factored out.

* `certP.wl` — per τ: `Annihilator` → `ct₁` → `OreGroebnerBasis` → bounded `Support` ladder for
  `ct₂`. Checkpointed per stage (`P_<tau>_ann.m`, `P_<tau>_<ORD>_ct1.m`, …) and every stage is
  wrapped in `MemoryConstrained[·, MEMCAP]` (default 4 GB) — **use it, the OOM killer takes the
  biggest process, which is the one you care about.**
* `certP2.wl` — hardened variant with two extra escapes: `CT1A`/`CT1B` bound the **first**
  elimination to `Support -> {S[n]^i S[V2]^j}` (finite linear solve, terminates), and `CT2V=sn`
  passes `{S[n]}` instead of `{}` as the third argument of the last `CreativeTelescoping`
  (if every rung of the ladder reports `none` in ~0 s, that is the bug to suspect).
* `certPy.wl` — composes each two-step certificate, `LCLM`s, computes the right cofactors and
  `X̂_τ = P_τ**Ck_τ`. **Its sign convention depends on `ORD`** and auto-detects it from the
  checkpoint filenames; do not override wrongly.
* `certPv.wl` / `certPv0.wl` — RISC-free verification (V-0 split, V-1 per-τ certificate,
  V-2 boundary at `k=0` / `l=0`, V-3 denominators).
* `certT3f.wl` — `L'' = M ** L_BZ` in verifycore's own one-variable Ore arithmetic, leading
  coefficient, integer roots, initial-value count. Reads `P_cert.m` or `T3_cert.m` (`CERTFILE`).

**Elimination order.** `τ = ll` has `A₂(k)` as its *only* letter, and `A₂(k)` does not depend on
`l` — so by §2's rule (`T·A₁(k)`: elim `l` 81 s, elim `k` >4 min, no return) it must be run
`ORD=lk`. The same argument favours `lk` for the other four (only `Ψ` touches `l`, while `k`
moves both letters).

## 8.4 Exact restart order

```
cd /home/ubuntu/fable-episode-2/zeta-math-2/work/lb5
pgrep -a WolframKernel                       # reap orphans with kill -KILL (SIGTERM is ignored)
python3 wlcheck.py certP.wl certP2.wl certPy.wl certPv.wl   # must all say OK
TAUS=ll,n1,n2,n3 ORD=lk MEMCAP=4000000000 nohup timeout 40000 math < certP.wl > A.stdout 2>&1 &
TAUS=kk          ORD=lk MEMCAP=4000000000 nohup timeout 40000 math < certP.wl > B.stdout 2>&1 &
#  if a ct1 has not returned in ~20 min:  switch that tau to certP2.wl with CT1A=2 CT1B=2
#  if every ct2 rung says "none" in ~0 s: rerun that tau with CT2V=sn
math < certPy.wl        # LCLM + composition  -> P_cert.m
math < certPv.wl        # RISC-FREE verification (the deliverable)
math < certT3f.wl       # L'' = M ** L_BZ, order, leading coefficient, initial-value count
```

## 8.5 The finish, and the number to state

`D_n := Σ_{k,l} T ŵ₃ − P̂_n` satisfies `L''·D = 0` with `L'' = M ** L_BZ`, `ord(L'') = ord(M) + 3`.
`D_n = 0` is `[VERIFIED exact]` for `n = 0 … 300` (`seqdata300.json`, all `ok` true) — **301
consecutive values** — so any `ord(M) ≤ 298` closes Theorem B, provided `lc(L'') = lc(M)(n)·
2(n+D+3)⁵(2n+2D+5)a₀(n+D)` has no integer root `n ≥ 0`; the `L_BZ` factor never vanishes there
`[PROVED]`, so only `lc(M)` must be inspected. `certT3f.wl` prints exactly this.

## 8.6 Cost reality check — read before planning a schedule

`PHASE2_CERTS` §13.4 has the table. The two things that change how you should budget:

1. **The τ-split fixed `Annihilator`, not `CreativeTelescoping`.** Closure: 2 s (was: OOM at
   14.4 GB). Elimination: **> 9–17 min with no return** on the *cheapest* τ, in **both**
   elimination orders.
2. **`Support -> {…}` bounds termination, NOT cost.** It bounds the telescoper's ansatz, but the
   certificate is still an unknown rational function, so the step stays a parametrised
   Gosper/Abramov problem of full size. A `Support` box 3×3 on `F_ll` had not returned after
   19 min. The 13 s / 12 s / 194 s box timings of §2 were on an object with *trivial*
   coefficients and do not transfer.

So: budget **4–10 kernel-hours** for the five τ problems, run them two at a time, and treat any
single elimination that passes ~30 min as a signal to change *something* (order, box, `CT2V`)
rather than to wait.

## 8.7 Kernel state at hand-off (2026-07-25 04:20)

Two standalone kernels were **left running** — everything they finish is `Put` to a checkpoint the
moment it completes, so they can only help:

| pid | job | state at hand-off |
|---|---|---|
| `1038875` | `TAUS=kk ORD=kl` (`certP.wl`) | inside `Annihilator[F_kk]`, **46 min**, 1.5 GB |
| `1112624` | `TAUS=ll,n1,n2,n3 ORD=lk CT1A=3 CT1B=3` (`certP2.wl`) | inside the bounded `ct₁` for `ll`, **19 min**, 2.0 GB |

At 04:35 neither had completed a stage (`kk` `Annihilator` 61 min / 3.3 GB, `ll` bounded `ct₁`
34 min / 2.1 GB). They were **deliberately left running**: both are inside the single most
expensive stage of their τ, both `Put` a checkpoint the instant it completes, and memory is not
tight. If either has landed by the time you read this, that stage is free.

**`MemoryConstrained` is a weaker guard than it looks.** At 04:41 pid `1038875` was at **4.8 GB
RSS** under a nominal `MEMCAP` of 4 GB and had not aborted: `MemoryConstrained` accounts for
memory *allocated by the evaluation*, which is not RSS (baseline, fragmentation and freed-but-
unreturned pages sit outside it). Treat `MEMCAP` as a soft brake, set it to roughly **half** the
headroom you actually have, and keep an external `free -m` watch — the OOM killer takes the
largest process, which is always the job you care about (that is exactly how `certT3.wl` died).

`P_ll_ann.m` is on disk and valid (`Annihilator[F_ll]`, 4 generators, 2 s). If `1038875` lands
`P_kk_ann.m`, that is the single most expensive object of the whole route and must not be
recomputed. **Check `pgrep -a WolframKernel` and `kill -KILL` before launching anything** —
`SIGTERM` is ignored and the licence cap is 3 (the MCP server, pid `140066`, permanently holds one).

## 8.8 What is NOT done, stated exactly

`M_τ` for the five τ. Nothing else. In particular the following are done and need no rerun:
the Q-row certificate; the reduction to `Σ E(v) = 0`; the regularised boundary lemma; `Eletters.m`
(now with a *fourth* independent confirmation); the rank-3 relations; the τ-split identity
(RISC-free, symbolic); and the entire assembly + verification + initial-value chain in code.

## 8.9 (b) `(T1-top)` under `PHASE2_THEOREM` v4 — the number that decides it

`work/lb5/esupp.py` (validated: it reproduces `PHASE2_CERTS` §10's `208` for `w5_allp` exactly).

| representative | terms | max degree | support of `E(·)/T` |
|---|---|---|---|
| `ŵ₃` folded `v` | 6 | **2** | **6** |
| `w5_allp` | 178 | 5 | 208 |
| **`w₅^I` (`w5_exIII_allp`, the v4 target)** | 207 | 5 | **220** |
| `w5_I` | 155 | 5 | 184 |
| `w5_Rbase` (uses `R₃(l)`) | 70 | **4** | **100** |

**The obstacle is the monomial DEGREE, not the weight** — a squarefree degree-`d` monomial
contributes `2^d − 1` proper sub-monomials to `E(·)/T`, and `ŵ₃`'s folded form is degree ≤ 2 while
every `w₅` has degree-4 and degree-5 terms. So the one experiment worth running is
**"is the fitting system consistent when restricted to weight-5 monomials of degree ≤ 3?"** —
pure Python on `work/p1g/e2.py`'s machinery, no Wolfram seat. Degree ≤ 2 (~78 columns against a
rank-313 system) is essentially ruled out by counting. Full memo: `PHASE2_CERTS` §15.

---

# 9. STATE AT 2026-07-25 ~05:30 (P1e session 4) — READ THIS BEFORE §8

`work/PHASE2_CERTS.md` §§16–17 is the write-up. §8's task list is **still the right shape** for
Theorem B, but two of its five τ have now been *measured to fail*, and (b) `(T1-top)` has been
**settled negatively** and should not be worked on further without a new idea.

## 9.1 (b) `(T1-top)` — CLOSED as a compute question. Do not reopen it by search.

`work/lb5/degfit.py` ran §15.2's decisive experiment. **The weight-5 fitting system has no
solution supported on letter monomials of degree ≤ 3** — in the plain harmonic alphabet (none of
degree ≤ **4** either), in the Apéry-extended alphabet `+R_r(k)`, or in the depth-2 nested
alphabet `+Y_ab,V_ab,Z_ab`; two primes; and **the fit identity alone is the obstruction**, so the
depth/pole-cap regime is irrelevant to it. The harness reproduces `exIII.log` exactly
(`rank(fit)=313`, 212 condition rows, `rank(joint)=342`, consistent) and reproduces `strong`'s
known inconsistency, so it is validated on a known positive *and* a known negative.

> `ŵ₃`'s degree-≤2 folded form has **no weight-5 analogue.** `(T1-top)` is
> `[BLOCKED BY A STRUCTURAL OBSTRUCTION]`. See `PHASE2_CERTS` §16.5 for the list of things that
> must **not** be re-run.

## 9.2 (a) Theorem B — what session 4 measured

| job | outcome |
|---|---|
| `Annihilator[F_kk]` (τ-split, 13069 leaves) | **OOM-killed, 7.8 GB, 85 min** (`dmesg` confirms). Do not attempt again in this form. |
| `Support`-boxed 3×3 `ct₁` for `F_ll` (rank 2) | **> 65 min, no return, 6.4 GB and climbing.** |
| `MemoryConstrained[·, MEMCAP]` | **did not fire** — cause found, see the box below. |
| `kill -KILL` | **blocked by the permission system**, again (cf. §7.7). You will be waiting for the OOM killer. |

> ### ⚠ FIX THIS BEFORE RUNNING ANYTHING — `stage` was missing `HoldRest`
> `stage[file_, lab_, name_, body_]` in `certP.wl` / `certP2.wl` / `certQ.wl` had **no hold
> attribute**, so `body` evaluated *before* `stage` was entered. Therefore
> **(i)** `MemoryConstrained[body, MEMCAP]` wrapped an already-computed value and could never
> abort — *that is the whole explanation of every uncapped OOM in this project, including the
> 14.4 GB one in §13.1*; **(ii)** `"loaded checkpoint"` printed only *after* redoing the stage and
> discarding it, so **restarts never saved anything**; **(iii)** the `t=…s` numbers `stage` prints
> are `Put` time only, not stage time (`certQ.wl`'s `ct1 t=3s` was really ≈ 9 min).
> **Fix, one line, immediately before the definition:** `SetAttributes[stage, HoldRest];`
> Applied to `certP.wl` and `certP2.wl` and verified in the MCP kernel (with it, the checkpoint
> branch skips the body and `MemoryConstrained` aborts; without it, neither).
> **`certQ.wl` still needs it** — it was mid-run and `math < file` reads from stdin, so editing
> the file live is unsafe.

**So the §13.4 estimate "4–10 kernel-hours, no new mathematics" is NOT confirmed** — do not quote
it. Two of five τ consumed ~2.4 kernel-hours and produced nothing.

## 9.3 The route that IS new, and the one exact structural win

`PHASE2_CERTS` §17.2 measures the cofactors of the **τ-split × letter-split** — the only cell of
that 2×2 table never tried, and the only one that is small on **both** axes: 13 rank-1 problems
(rational multiples of `T`), nine under 3000 leaves, six under 1000, versus `certU`'s three at
22317–66499 leaves and `certP`'s five at rank 3.

**`τ = ll` is exactly reducible with NO Abel correction** — `[PROVED, symbolic]`:

```
    p_ll = r_ll = 0   ==>   F_ll = (G_ll q_ll) * A2(k) ,
    G_ll q_ll = (rational, 1913 leaves) x T   (letter-free) ,   A2(k) free of l
    ==>  Sum_l F_ll = A2(k) * Sum_l (G_ll q_ll)                 (rank 1, not rank 2)
```

Checked in the MCP kernel by rebuilding `certP.wl`'s own `stuff[]`/`Ftau[]`:
`Simplify[stuff["ll"] − q_ll A2(k)] = 0` **symbolically**, and `Ftau["ll"] − GQ·A2(k) = 0` at five
exact integer points. `work/lb5/certQ.wl` runs it, and **it works** — measured by log-header deltas (not `stage`'s own
broken `t=`):

| stage | measured |
|---|---|
| `Q1` `Annihilator[G_ll q_ll]` | 3 generators, ~1 s — rank 1 confirmed |
| `Q2` `CreativeTelescoping[·, S[l]−1, {S[n],S[k]}]` | **RETURNED in ≈ 9 min**, 3 telescopers (checkpoint 27.8 MB) |
| `Q3` `OreGroebnerBasis` | ≈ 3 min 20 s, and **`gb === ct1`-telescopers → True** (no cofactor chain needed, as for the Q-row) |
| `Q4` `DFiniteTimes[gb, Annihilator[A₂(k)]]` | in flight at hand-off |
| `Q5` `ct₂`, eliminate `k`, `Support` ladder | not reached |

> **This is the first τ in the whole campaign to get past its first elimination.** Same τ, same
> machine: rank 2 → **> 67 min, no return, twice**; rank 1 → **≈ 9 min, returned**.

The same trick applies **partially to all five τ**: `Ψ = A₁(k)+3B₁(k)+(3/2)C₁+(1/2)A₁(l)`, and only
`C₁, A₁(l)` depend on `l`, while `dA2f[τ]` is `l`-free for every τ. So for each τ the `l`-sum splits
into `Σ_l(G p)`, `A₂(k)Σ_l(G q)`, `r_τ(A₁(k)+3B₁(k))Σ_l G` — three **rank-1** problems — plus one
genuinely **rank-2** remnant `r_τ Σ_l G[(3/2)C₁+(1/2)A₁(l)]`. That is the decomposition to build
on, and it needs no Abel correction either (nothing is pulled through a `Δ`; the letters simply do
not depend on `l`).

> ⚠ **`certQ.wl` has a CIRCULAR in-script assertion** (`Fllref` is built from the same two
> expressions as `GQ·A₂(k)`, so it always returns `0`). Replace it with a rebuild of `certP.wl`'s
> `stuff["ll"]` before reusing the script. An assertion that cannot fail is not an assertion.

## 9.4 Exact restart commands

```
cd /home/ubuntu/fable-episode-2/zeta-math-2/work/lb5
pgrep -a WolframKernel            # MCP server is pid-with-PacletSymbol; reap the rest
python3 wlcheck.py certQ.wl certP.wl certP2.wl certPy.wl certPv.wl    # must all say OK

# 1. the rank-1 route for tau = ll  (checkpoints Q_ll_ann1.m / Q_ll_ct1.m / Q_ll_gb.m / ...)
#    FIRST add  SetAttributes[stage, HoldRest];  and replace the circular assertion (see 9.3).
#    Q1..Q3 are already on disk, so with HoldRest in place a restart resumes at Q4.
#    If every Q5 rung reports "none" in ~0 s, that is the certP2.wl CT2V bug: pass {S[n]}
#    instead of {} as the third argument of the last CreativeTelescoping.
DMAX=10 MEMCAP=3000000000 nohup timeout 20000 math < certQ.wl > certQ.stdout 2>&1 &

# 2. the three SMALL-weight tau, never yet attempted (weights 84 / 86 / 66)
TAUS=n1,n2,n3 ORD=lk DMAX=10 MEMCAP=3000000000 nohup timeout 14000 math < certP.wl > certP_n123.stdout 2>&1 &

# 3. do NOT run:  TAUS=kk in any form (Annihilator OOMs at 7.8 GB);
#                 certT3.wl (monolithic, OOM);  certUb.wl / certZ.wl (superseded);
#                 the unconstrained ct2 for the letter alpha (79 min, no return).

# downstream, unchanged and ready:
math < certPy.wl    # LCLM + composition -> P_cert.m
math < certPv.wl    # RISC-FREE verification (the deliverable)
math < certT3f.wl   # L'' = M ** L_BZ, order, leading coefficient, initial-value count
```

**The finish is unchanged and cheap** (§8.5): `D_n = Σ T ŵ₃ − P̂_n = 0` is `[VERIFIED exact]` for
`n = 0…300` (`seqdata300.json`), so **any `ord(M) ≤ 298`** closes Theorem B once the `M_τ` exist.

## 9.5 Files added this session

| file | what |
|---|---|
| `degfit.py` | **the M0 experiment** — degree-capped rank/consistency of `[fit ; depth]`; `NOCOND=1` skips the depth block |
| `degfit_*.log` | the runs: `exIII_AB`, `base_AB`, `base_ABR`, `base_ABYCVNZ`, `base_UNION`, and `_q2` second-prime confirmations |
| `DF_*.npz` | cached design matrices (`M`, `b`) per alphabet/`N`/`q` |
| `certQ.wl` | the rank-1 `τ = ll` route (§9.3); **fix its circular assertion first** |
| `Q_ll_*.m` | its checkpoints (`ann1`, `ct1` 27.8 MB, `gb` 4.8 MB) |

## 9.6 In flight at hand-off — check these before starting anything

```
pgrep -a WolframKernel      # expect: MCP server + up to 2 standalone
```

| pid | job | state |
|---|---|---|
| `1205156` | `certQ.wl` — rank-1 `τ = ll` | `Q1–Q3` done and checkpointed, inside `Q4 DFiniteTimes`, ~2.9 GB, healthy |
| `1246566` | `certP.wl TAUS=n1,n2,n3 ORD=lk MEMCAP=3e9`, **with the `HoldRest` fix** | launched 05:20:44 on `τ = n1` (`LeafCount` **578** — the smallest object in the problem). **Never attempted before this session.** First run ever with a working memory cap, so it will say `MEMORY ABORT` instead of starving the box. |
| — | `degfit.py base ABRY CDV NZ` (union alphabet, fit-only) | design matrix still building; **not needed** — §9.1's verdict rests on three alphabets that are already decisive |

If both kernels are gone when you arrive: `certQ.wl` resumes at `Q4` from disk **once you add
`SetAttributes[stage, HoldRest]`** (without it, it will redo `Q2`'s nine minutes first), and
`certP.wl TAUS=n1,n2,n3` restarts from scratch cheaply — `F_n1` is 578 leaves.

---

# 10. STATE AT 2026-07-25 ~06:00 (P1e session 5) — READ BEFORE §9

`work/PHASE2_CERTS.md` **§18** is the write-up. §9 is still accurate about `(T1-top)` and about
the `HoldRest` bug; what it says about *which objects to run* is superseded by §18.

> ## ⛔ READ §10.7 FIRST — the splitting strategy is disproved
> §§10.1–10.6 below describe the letter-split route accurately and its measured wins are real,
> **but §10.7 shows the route cannot terminate**, and it supersedes the recommendations in
> §10.4 and §10.5. Do not spend a seat on more splitting before reading it.

## 10.1 The one thing to understand first — the cost driver was misidentified for three sessions

**It is the number of harmonic letters in the object, not its `LeafCount`.** Controlled
measurement, same τ, same machine (`PHASE2_CERTS` §18.7):

```
   Annihilator[ F_n1 ]        578 leaves, 10 letters  ->  19 min, NO RETURN
   Annihilator[ n1:A piece ]  400 leaves,  0 letters  ->  3 generators, 0 s
```

`F_ll` was never cheap because it was small (it is 2318 leaves, *four times bigger* than `F_n1`);
it was cheap because it carries 2 letters where the others carry 10. Every ranking in §§13–17
that ordered work by `LeafCount` was ordering it backwards.

## 10.2 The four-piece letter split — `[PROVED symbolically, all five τ]`

`Psi = Psik + Psil`, `Psik = A1(k)+3B1(k)` (`l`-free), `Psil = (3/2)C1+(1/2)A1(l)`. Then

```
   F_tau = W P  +  W Q * A2(k)  +  W R * Psik  +  W R * Psil
             A          B              C              D
   letters:  0          2              4              4        (F_tau itself has 10)
   lambda:   1        A2(k)          Psik            1
```

Pieces A, B, C are **rank 1 in the `l`-elimination** (the object telescoped is letter-free; the
`l`-free letter `λ` is re-attached afterwards by `DFiniteTimes` at the `(n,k)` level). D is the
rank-2 remnant. **No Abel correction anywhere** — no letter is pulled through a `Δ`.
Verified RISC-free in the MCP kernel against `certP.wl`'s own `stuff[]`/`Ftau[]`, symbolically,
for all five τ; `certQ2.wl`/`certQ3.wl` re-assert it at every run and abort if it fails.

## 10.3 Where the cost actually is now — two walls, and `R1–R3` are free

| | measured |
|---|---|
| `R1` `Annihilator` | 0–6 s |
| `R2` `ct₁` (eliminate `l`) | 5–22 s (was ≈ 9 min for `ll:B`) |
| `R3` `OreGroebnerBasis` | 1–5 s, and `gb === ct₁` telescopers **always** — no cofactor chain |
| **`R5` `ct₂` `Support` ladder** | **WALL 1** — `d=0…4` cost 1, 6, 15, 49, 185 s: **×3.8 per rung**, so `d ≥ 7` is unreachable |
| **`R4` `DFiniteTimes`** (pieces B, C only) | **WALL 2** — `certQ.wl`'s `Q4` for `ll:B` ran **37 min, no return**, reaped |

## 10.4 The two moves that would break the walls

1. **Wall 1** — try **unconstrained** `CreativeTelescoping[annL, S[k]-1, {S[n]}]` instead of the
   `Support` ladder. It returns the *minimal* telescoper directly and does not pay the 3.8×.
   `certQ3.wl` does this first, under `TimeConstrained[·, FREECAP]` (default 600 s), and falls
   back to the ladder. **This is the live hypothesis at hand-off.**
2. **Wall 2** — delete `DFiniteTimes` from the pipeline by trading the letter for a summation
   variable: `A2(k) = Sum_{j=1}^{n} 1/(k+j)^2`, so
   `Sum_k A2(k) S(n,k) = Sum_{j=1}^n Sum_k S(n,k)/(k+j)^2` and the inner object carries **no
   letter at all**. Costs one boundary term at `j = n`, of the kind §8 already discharges.
   **Untried, cheap, and the only proposal on the table for `τ = ll`** (whose single non-zero
   piece `ll:B` is pure Wall 2).

## 10.5 Restart commands

```
cd /home/ubuntu/fable-episode-2/zeta-math-2/work/lb5
python3 wlcheck.py certQ2.wl certQ3.wl          # both must say OK
pgrep -af WolframKernel                          # licence cap is 3; MCP holds one

# certQ3.wl is certQ2.wl + (a) free-ct2 first, (b) LADDERCAP so one bad ladder cannot
# starve the job list, (c) finished jobs skipped.  PREFER certQ3.  Checkpoints are
# R_<tau>_<piece>_{ann,ct1,gb,annL}.m and the finished job is R_<tau>_<piece>.m .
# KEEP JOB LISTS DISJOINT ACROSS KERNELS -- two kernels writing one checkpoint file
# would tear it, which is exactly the silent failure mode section 13.2 warns about.
JOBS=kk:C,kk:B,kk:A,kk:D DMAX=10 MEMCAP=3000000000 LADDERCAP=2700 FREECAP=600 \
   nohup timeout 13000 math < certQ3.wl > certQ3_kk.stdout 2>&1 &

# NOTE certQ3.wl still writes its log as certQ2_<TAG>.log (cosmetic: it is a copy).

# do NOT run: certP.wl / certP2.wl on any tau (they telescope the 10-letter F_tau);
#             certQ.wl (its Q4 is Wall 2, and it is the one script never given HoldRest);
#             TAUS=kk in any certP form; certT3.wl; certUb.wl; certZ.wl.
```

## 10.6 What is still missing for Theorem B, exactly

1. **19 `ct₂` telescopers** (4 pieces × 4 τ + 1 for `ll`; `ll:A`, `ll:C`, `ll:D` are identically 0).
   **Zero of them exist at hand-off.**
2. **Wall 2 for the 8 B/C pieces** plus `ll:B`.
3. **Assembly.** `certPy.wl`/`certPv.wl` do **not** apply verbatim — the letter-split inserts a
   `DFiniteTimes` stage they know nothing about. `PHASE2_CERTS` §18.5 specifies the fix completely
   (the **φ-shift decomposition**, `O.(λS) = λ(O.S) + (O_φ.S)`, with `φ` rational and tabulated in
   `phi_tables.m`, cocycle-checked). `[SPECIFIED, NOT IMPLEMENTED]` — this is the last mile.
   Note pieces A and D have `λ = 1`, so for them `certPy`'s existing shape already works.
4. **19 boundary-obligation pairs** instead of 5 (they sum correctly, so it is bookkeeping).
5. `LCLM` over the pieces, then the finish — `D_n = 0` is `[VERIFIED exact]` for `n = 0…300`
   (`seqdata300.json`, 301 values), so **any `ord(M) ≤ 298` closes Theorem B**.

## 10.7 ⛔ **STOP SPLITTING** — measured, and it retires §§10.4–10.6's plan

`guessrec.py` re-run this session at `N=220` and `N=460` (pure Python, no seat), reproducing
`PHASE2_CERTS` §5.1:

```
   Q_n = Sum_{k,l} T                  ->  (r,d) = (3,9), nullity 1   = L_BZ
   Sum_{k,l} T*w3hat  (COMBINATION)   ->  (3,9),        nullity 1    = L_BZ
   U1..U5  (single-letter PIECES)     ->  NONE  with r <= 12, d <= 30
```

**The pieces have no operator in the size range being searched; the combination has order 3.**
`ct₂` has therefore been hunting operators that are not there. Three independent confirmations,
the last of which rules out any ansatz artefact:

* `certU` (its pieces literally *are* `U₁…U₅`) — `ct₂` 79 min, no return;
* `n1:A`, the **smallest object in the problem** — `Support` ladder excluded orders 0–5 at a cost
  of 1084 s, rungs `1, 6, 15, 49, 185, 828 s` (**×3.8 per rung**, so `d=6` ≈ 62 min, `d=7` ≈ 4.6 h);
* `n2:A` — **unconstrained** `CreativeTelescoping`, *no `Support` box at all*, `TimeConstrained`
  at **600 s, no return**.

Each split did deliver what it promised on its target stage (τ-split: `Annihilator` 14.4 GB OOM
→ 2 s; letter-split: first elimination ≈ 12 min → 33 s, `Annihilator` → 0 s — these are real and
measured). But every split moves the cost into `ct₂` while **multiplying the number of `ct₂`
searches**, and the order-3 collapse is a property of the **combination**, destroyed by any
decomposition. With `R1–R3` now free there is nothing left to split *for*.

### The plan that replaces it — one plan, two halves, no seat needed for the first

> **Re-fold `ŵ₃` so the combination carries ≤ 4 harmonic letters, then telescope it *whole* in
> the known `(r,d) = (3,9)` box.**

* **Half 1 (algebra, no Wolfram seat, do this first).** The combination currently carries **10**
  letters. §18.2's law says `Annihilator` is instant at 0 letters and hopeless at 10; the folded
  form `v = H⁽³⁾_n + 2A₃(k) − ½A₂(k)Ψ` already achieved one such collapse (degree 5 → 2, §15.2).
  Ask whether a further re-folding to ≤ 4 letters exists. Purely algebraic.
* **Half 2 (one seat, one `ct₂`).** `Σ T·ŵ₃` has a *unique* order-3 degree-9 recurrence, known
  from 501 values with ~460 excess equations, found by `guessrec` in **0 s**. The operator was
  never the missing object — the **certificate** is. Certifying it against the combination is a
  *single* `ct₂` in a tiny known box, not 19 searches over unknown boxes.
* ⚠ **Half 2's blocker is `Annihilator` on the 10-letter object** (14.4 GB OOM, §13.1), which is
  exactly what Half 1 fixes. They are one plan, in that order — not alternatives.

### What is still worth a seat right now

Only one thing: `JOBS=kk:C,kk:B,kk:A,kk:D` under `certQ3.wl`. `kk` is the sole τ never closed at
**any** stage (`Annihilator[F_kk]` OOM-killed at 7.8 GB). Its letter-split pieces carry ≤ 4
letters against ~10 600-leaf cofactors, so it is a clean test of §18.2's law on the hardest τ —
and `R1–R3` are all it needs to answer. Do **not** expect its `ct₂` to return.

## 10.8 UPDATE 06:13 — **Wall 2 is down. `ct₂` is the only remaining obstacle.**

`kk:C annL #4 t=500s (checkpointed) mem=0GB` — `DFiniteTimes` returned 4 generators in 8 min 20 s
on the **largest cofactor in the problem** (10611 leaves), the stage `certQ.wl`'s `Q4` failed to
return from in 37 min. Cause: the `gb` handed to `DFiniteTimes` is 124 KB in the letter-split
pipeline versus 4.8 MB in the old one, because the new route telescopes a **letter-free** object.
Wall 2 was §18.2's law acting one stage later, not a property of `DFiniteTimes`.

**Consequences for §§10.3–10.6 above:**

* §10.3's table: `R4` is **clear**, not a wall. Every stage `R1`–`R4` is now clear on every τ,
  including `kk`, whose `Annihilator` was the campaign's one hard OOM.
* §10.4 move 2 (the `j`-variable trick to delete `DFiniteTimes`) is **no longer needed**. Drop it.
* `ll` is **not** blocked. Re-run `JOBS=ll:B` through `certQ3.wl` — its `gb` will be small.
* §10.7 is **unaffected and is still the whole point**: `ct₂` has zero returns by any method on
  any piece, and `guessrec` says it is searching an empty box.

> **The state, in one line.** Four of the five stages are free; the fifth is provably searching
> for operators that do not exist at the sizes being searched; and the only way to put the
> operator back in range is to stop splitting and re-fold the *combination* (§10.7).

## 10.9 UPDATE 06:45 — the `ct₂` evidence is now complete; use `certQ3.wl`, never `certQ2.wl`

| piece | ladder | unconstrained `ct₂` |
|---|---|---|
| `n1:A` (429) | `d=0…5`: 1, 6, 15, 49, 185, 828 s — none | — |
| `n2:A` (4262) | `d=0…5`: 10, 27, 64, 166, 481, 1985 s — none; `LADDERCAP` fired at `d=6` | **600 s, none** |
| `kk:C` (10611) | — | **421 s, none** |

`n2:A` got **both** methods and 3300 s and returned nothing. `kk:C` is the only piece to clear
`R1`–`R4` completely (34 + 33 + 2 + 500 s) and reach `ct₂` with everything upstream done — and
`ct₂` still returned nothing. **The wall is `ct₂`, it is not the `Support` ansatz, and nothing
upstream causes it.**

`LADDERCAP` did its job: it retired `n2:A` at budget and moved to `n2:C`, whose `Annihilator`
returned 3 generators in **0 s** (the letter-count law on a fourth object). Without it that
kernel would have spent ~4.6 h on `d=7`. **`certQ2.wl` has no such cap — always run `certQ3.wl`.**

Ladder growth is ×3.0–4.5 per rung on both measured objects, so the ladder is unusable beyond
`d = 6` anywhere in this problem.

## 10.10 ⚠ CORRECTION to §10.8 — Wall 2 falls for **rank-2** pieces only; `ll:B` still stands

§10.8 said Wall 2 was down because the letter-split `gb` is small. **The stated cause was wrong**
(`certQ.wl` was *already* letter-free for `ll:B` — `certQ.log`: `HarmonicNumber count in GQ: 0`).
The real discriminator is the **`ct₁` telescoper count** = rank of the surviving `(n,k)`-module:

```
   n1:A, n2:A, n2:C, kk:C  ->  ct1 telescopers 2  ->  gb 13-184 KB  ->  R4 = 25-500 s
   ll:B                    ->  ct1 telescopers 3  ->  gb 4.8 MB     ->  R4 = 37 min, no return
```

rank 2 gives a rank-4 product with the letter; rank 3 gives rank 6. **`ll` is the exception
because `p_ll = r_ll = 0` makes three of its four pieces vanish, so `ll:B` is not split at all** —
the property that made `ll` look easiest is what leaves it nothing to split.

* **Do NOT re-run `ll:B` expecting a small `gb`.** §10.8's advice is withdrawn.
* The `JOBS=ll:B,n3:C,n3:B` run (pid 1834107, launched 06:57) will fail at `R4` — but *safely*:
  `certQ3.wl` has `HoldRest`, so `MemoryConstrained` is real and `R4` aborts at `MEMCAP` rather
  than hanging, then proceeds to `n3:C`. Self-limiting; still delivers `n3`.
* The `j`-variable move (§10.4 move 2) is **reinstated for `ll:B` specifically** — §10.8 deleted
  it prematurely.
* Everything else in §10.8 stands: Wall 2 is genuinely retired for the 16 rank-2 pieces.

> **`ct₁ telescopers:` in the log predicts `R4` cost better than any leaf count. Read it.**

## 10.11 §10.10 CONFIRMED — `ll:B` reproduced the old `ct₁` byte-for-byte

```
   ll:B ct1 #2  t=1021s  ->  ct1 telescopers: 3
   R_ll_B_ct1.m  27,850,782 bytes  ==  certQ.wl's Q_ll_ct1.m  27,850,782 bytes   (cmp: identical)
```

The new pipeline performs **literally the same computation** on `ll:B` as the old one. The letter
split is a **no-op on `ll`** — `p_ll = r_ll = 0` leaves it one piece to "split" into. `ll` is a
genuine structural exception: 3 telescopers → 4.8 MB `gb` → rank-6 product → the 37-min `R4`
non-return. **Do not re-run `ll:B` in any `certQ*` variant expecting a different result.**
It needs the `j`-variable move (§10.4 move 2) or another idea.

Useful side effect: with `HoldRest`, `certQ3.wl`'s `MEMCAP` is real, so this run's `R4` aborts at
3 GB and proceeds to `n3:C` rather than hanging as `certQ.wl` did.

## 10.12 ⚠ `LADDERCAP` is VACUOUS on long rungs — use `certQ4.wl`

`LADDERCAP` is tested only *between* rungs, so it bounds how many rungs start, not time spent in
one; and the rungs have `MemoryConstrained` but **no `TimeConstrained`**. Measured: `kk:C` sat in
its `d = 0` rung from 06:20 to 07:16+ (**56 min, uninterruptible**) at a flat 2.0 GB, so neither
cap fired; its 1800 s `LADDERCAP` was due at 06:36 and never consulted. Only the outer
`timeout` bounds such a run.

**`certQ4.wl`** = `certQ3.wl` + per-rung `TimeConstrained[..., RUNGCAP]` (env, default 900 s), so
the worst case becomes `LADDERCAP + RUNGCAP`. `wlcheck`-clean, parses clean, **not yet run**.
**Prefer `certQ4.wl` over `certQ3.wl` over `certQ2.wl`.**

> Third silently-inoperative safety mechanism in this project (`HoldRest`/`MemoryConstrained`,
> the self-comparing assertion, now this). **Test `RUNGCAP` with a deliberately tiny value on a
> rung known to exceed it before trusting it** — a control never observed to fire is not a control.

## 10.13 `RUNGCAP` control test — DONE, and it found two more defects. **Use `certQ4.wl`.**

Tested before trusting, per §10.12. `n2:A`, checkpoints on disk, cap far below the rung's cost.

1. **`RUNGCAP` fires** — but as first written it fired **invisibly**: `third={} d=0` printed
   `none` at t=3s and again at t=1s. The discriminating run (`RUNGCAP=120`, idle box) showed the
   rung's **true cost is 16 s**, so those were *masked timeouts*.
2. **Cause: nesting order.** `Quiet[Check[TimeConstrained[...], $Failed]]` lets the outer `Check`
   swallow the timeout when the abort emits a message. `Check` must be **inside**:
   `TimeConstrained[Quiet[Check[MemoryConstrained[...], $Failed]], RUNGCAP, rungTimedOut]`.
   After the fix, **5 of 5 capped calls announce themselves**.
3. **Worse defect found on the way out:** the script printed `NO telescoper up to d=D` even when
   every rung had been aborted. `none` means *no telescoper of that order exists*; a timeout
   means *we stopped looking*. `certQ4.wl` now prints
   `NO telescoper found up to d=D BUT n rung(s) were ABORTED ... this is NOT an exclusion`,
   and otherwise `(all rungs ran to completion -- a genuine exclusion)`.

**AUDIT of this session's own results — `[CHECKED, CLEAN]`.** `certQ2.wl` has **no**
`TimeConstrained`; `certQ3.wl` has exactly one, on the *free* attempt only. So every ladder rung
ran to completion, and their times are all distinct and never equal a cap (`n1:A` 1/6/15/49/185/828 s;
`n2:A` 10/27/64/166/481/1985 s). **The exclusion of orders 0–5 is genuine and §10.7 stands.**
The three *free* attempts, however, hit their caps exactly (421 s, 600 s, 601 s) — read those as
**"did not return", not "excluded"**. §10.7 only ever needed "did not return", so it is unaffected.

> Script preference is now **`certQ4.wl` > `certQ3.wl` > `certQ2.wl`**, and `certQ4.wl` is the
> only one that cannot overstate an exclusion.

---

# 11. STATE AT 2026-07-25 ~08:00 (P1e session 6 — THE REFOLD RUN)

`work/PHASE2_CERTS.md` **§19** is the write-up. §10 is still accurate about `ct₂` on pieces and
about the ops law; what changes is **which object to telescope**, and it changes decisively.

## 11.1 ⛔ The `E`-route is dead, and for a STRUCTURAL reason — do not reopen it

`Annihilator[E(ṽ)]` — 7 distinct symbols, the point §18.17's calibration was missing — was run
**twice**:

```
   MEMCAP 5.0 GB  ->  MEMORY ABORT after 478 s   (peak RSS 5.21 GB)
   MEMCAP 8.5 GB  ->  MEMORY ABORT after 536 s   (peak RSS 8.38 GB)
```

Memory grows **≈ 3.6 GB/min, linearly**, and only 58 s separate the two aborts. Compare `F_kk`
at 9 symbols: 7.8 GB after **85 min**. So **7 symbols is worse per unit time than 9**, and the
refold's two-symbol gain buys nothing.

**Why, and why no refold can ever fix it.** `E(w) = Σ_τ G_τ(τ.w − w)` with
`G_kk = −ρ|_{k+1}T(k+1)` and `G_ll = −σ|_{l+1}T(l+1)`. So **every** `E(w)` carries `ρ` (10553
leaves) and `σ` (1819) in its coefficients, unless `τ.w − w = 0` for both `τ = kk` and `τ = ll`
— i.e. unless `w` depends on `n` alone, which the weight-3 fit excludes. The obstruction lives
in the **Q-row certificate**, not in the weight, so it is invariant under every refold.

> **Do not run:** `Annihilator` on `E(w)` for any `w`, in any fold, at any symbol count.
> `certRF.wl` is kept only as the record of the measurement.

## 11.2 The route that is alive: telescope `T·w` DIRECTLY

The two cost axes are **letters** and **coefficient size**, and the `E`-family is permanently bad
on the second. The `T·w` family is good on both:

| object | symbols | `LeafCount` | `Annihilator` |
|---|---|---|---|
| ~~`T·v` (§5.2 cost model)~~ | 12 | 110 | ~~124 s, 7 gens~~ **WITHDRAWN** (§11.6): **TIME ABORT 600 s** |
| **`T·ṽ`** | **10** | **91** | see §11.6 |
| `E(ṽ)` | 7 | 120100 | **abort 8.4 GB** |

and its `ct₂` box is the one box in this problem that is **known and occupied**: `guessrec` finds
the unique `(3, 9)` operator `L_BZ` for the combination in 0 s from 501 values.

`work/lb5/certRFD.wl` is that run: `Annihilator[T·ṽ]` → `ct₁` (eliminate `l` — `ṽ`'s entire
`l`-side content is the **single** letter `A₂(l)`, rank 2, and there is no `C` letter coupling
`k` to `l`) → `gb` → `ct₂` with `Support -> {1, S_n, S_n², S_n³}`. It needs **no Q-row, no `E`,
and no boundary lemma for `E`** — only §2's pole count, which `ṽ` satisfies with room to spare.

## 11.3 What is discharged in advance — do not redo any of it

* `Σ T·ṽ = P̂_n` exact `n = 0…33`; `L_BZ·(Σ T·ṽ) = 0` exact `n = 0…30` (`refold/checkrec.py`).
* `ŵ₃ − ṽ ∈` the **PROVED** kernel: `ŵ₃ − v` and `v − ṽ` are both in the span (Lemma-Phi species
  + `k↔l` folding), rank 57 → 57 for each (`refold/keyid.py`). **So certifying `ṽ` certifies
  Theorem B.**
* Far-edge boundary: `T·ṽ → 0` at all 15 tested cells with `k` or `l ∈ {n+1,n+2,n+3}`; `ṽ`'s pole
  there is **simple**, `T`'s zero is **double**.
* `E(ṽ)/T = c₀ + β(A₂(l) − A₂(k)) + α·Ψ_k` — `[CERTIFIED RISC-free, SYMBOLIC]`, 7 hh-symbols,
  0 non-zero; and `REFOLD` §4.6's `dh₃/da₃/dX/dY` tables verified symbolically for all five τ.
  (Kept for the record; the `E`-route itself is dead.)
* Initial values: `seqdata300.json`, **301** consecutive exact values, all `ok`. Any `ord(M) ≤ 298`
  closes Theorem B.
* `verifycore.wl`'s `hnorm` handles `ṽ` under every shift `a ≤ 3, b,c ≤ 1` — 10 hh-symbols, no
  failures — so `certRFv.wl` cannot fail late for a normalisation reason.

## 11.4 Downstream, written and smoke-tested, waiting only on a certificate

```
  math < certRFy.wl      # WHICH=D  compose ct1+ct2 into  M.F = Delta_k(X.F) + Delta_l(Y.F)
                         # no LCLM, no right cofactors -- the object was never split
  math < certRFv.wl      # WHICH=D  RISC-FREE verification (V-A..V-E, incl. the k=0 / l=0
                         #          boundary pair, which is the step easiest to skip)
```

## 11.5 Ops — two rules learned the hard way

* **Disarm superseded waiters before handing off.** `launch_certQ3_ll.sh` fired at 06:57:22 and
  took the seat this session's decisive run had been promised, for a piece-`ct₂` job §18.13
  proves is searching an empty box. `kill -KILL` is blocked by the permission classifier for the
  agent that needs it; ask the orchestrator and give it the pids **in kill order** (bash waiter
  first, then the kernel, then the `timeout` wrapper).
* **A memory cap tells you it stopped; only an external watch tells you it was diverging.**
  Run `free -m` at a 20 s cadence alongside every capped stage. The two S1 aborts are
  interpretable *only* because the trace shows a straight 3.6 GB/min line.

## 11.6 The direct route, MEASURED — and a correction that matters more than the measurement

`certRFD.wl` was run on both proved folds. **Read §11.2's table with these numbers substituted.**

| object | symbols | `LeafCount` | `Annihilator` | which cap fired |
|---|---|---|---|---|
| `T·ṽ` | 10 | 91 | **MEMORY ABORT, 1991 s** | `MEMCAP` 2.5 GB (set low to protect a co-resident run) |
| `T·v` | 12 | 110 | **TIME ABORT, 600 s** | `ANNCAP` 600 s (deliberately tight probe) |

**Neither is a verdict.** Both stopped on caps chosen for scheduling reasons, and the memory
traces say opposite things about the two families:

```
   T*vtilde  0.92 -> 1.10 -> 1.68 -> 2.10 GB over 33 min   = 0.036 GB/min   FLAT
   E(vtilde) 2.64 -> 4.00 -> 6.09 -> 8.38 GB over 100 s    = 3.6  GB/min    DIVERGING
```

> ### ⚠ `Annihilator[T·v] = 124 s, 7 gens` (§1 cost model) DOES NOT REPRODUCE
> Same object (12 symbols, 110 leaves, `certP.wl`'s `vw` verbatim), correctly timed `stage`:
> **no return in 600 s.** §17.5 explains it — before the `HoldRest` fix, `stage`'s `t=…s` was
> **`Put` time, not stage time**. **Treat every pre-fix timing in §1/§5.2 as an artifact.** The
> belief that "the direct route is cheap because `Annihilator[T·v]` costs two minutes" was
> resting on that artifact and must not be repeated.

## 11.7 In flight at hand-off (08:24), and the ONE thing to do next

```
  certRFD.wl  ORD=lk  MEMCAP=9000000000  ANNCAP=5400  timeout 11000   started 08:24:16
              -> deadline 09:54:16 ; log certRFD_lk.log ; checkpoint RFD_ann.m
  launch_certRFD_kl.sh  ARMED: fires the ORD=kl swap on seat 2 the moment RFD_ann.m exists
              (it LOADS that checkpoint -- Annihilator is ORD-independent). Disarm it if you
              supersede the run:  ask the orchestrator to kill the bash pid.
```

**If `RFD_ann.m` lands, everything downstream is written and waiting:** `ct₁` eliminates `l`
against the **single** `l`-side letter `A₂(l)` with no `C` letter coupling `k` to `l`; `ct₂`
searches `Support -> {1, S_n, S_n², S_n³}`, the one box in this problem known to contain its
answer; then `certRFy.wl` composes and `certRFv.wl` verifies RISC-free (V-D is the `k=0`/`l=0`
boundary pair — exactly one pair, because the object was never split).

**If it does not land**, the honest position is that *all four* routes to Theorem B are now
measured and blocked at a named stage, three of them structurally, and the remaining move is
algebraic: find a representative whose `T·w` is `∂`-finite-closable, i.e. attack the **closure**
rather than the letters. `ṽ` (10 symbols, 91 leaves, no `C`) is the best object anyone has
offered it, and `REFOLD` §5.5's 6-dimensional gap in the proved kernel (`dim ker V = 63` versus
`dim span(proved) = 57`) is the only known place where a better one could still be hiding.

**UPDATE 08:58 — the cap was the binding constraint, confirmed.** The resourced `certRFD.wl` run
passed the previous abort point (1991 s) **still running**, at 2.21 GB, having grown
`0.74 → 2.21 GB` over 32 minutes (**0.046 GB/min**, flat over multi-minute stretches).
`Annihilator[T·ṽ]` was never diverging — it was stopped by a 2.5 GB scheduling cap. It is the
first object in this campaign stopped by a *cap* rather than by its own growth. **Do not
re-derive this: give it memory, not cleverness.**

---

# 12. STATE AT 2026-07-25 10:00 (P1e session 7 — the resourced direct run, RESOLVED)

`work/PHASE2_CERTS.md` **§§19.11–19.13** is the write-up. §11 is still correct about *what to
run*; this section corrects *what is known about its cost*.

## 12.1 The one number session 6 was missing

```
  Annihilator[T*vtilde]   ORD=lk   MEMCAP = 9 GB   ANNCAP = 5400 s
      -> TIME ABORT after 5402 s        peak RSS 5.01 GB      RSS at abort 3.12 GB
```

`certRFD_lk_ANNCAP5400.log`, external 30 s watch `memwatch_run4.log` (177 samples) and
`memwatch4.log`. **RSS sawtooth**, extrema at 0.3 GB hysteresis:

```
  0.74 (08:25) -> 2.52 -> 2.21 -> 4.32 -> 2.58 -> 4.45 -> 2.84 -> 5.01 (09:34) -> 3.08 (09:52)
  net slope 0.027 GB/min over 89 min ; four releases of 1.7-2.2 GB each
```

> **This is the first object in the whole campaign stopped by the CLOCK and not by MEMORY.**
> `E(v)` OOM-killed at 14.4 GB, `F_kk` OOM-killed at 7.8 GB, `E(ṽ)` capped twice at 5.2/8.4 GB.
> `T·ṽ` peaked at **5.01 GB of a 9 GB budget** and was at **3.12 GB** when the time cap fired.
> §11.6's provisional reading is confirmed: it is **computing**, not diverging.

**Do not re-derive this, and do not read it as an exclusion.** What is measured is a lower
bound — `Annihilator[T·ṽ]` costs **> 90 min** at ≤ 5 GB — plus strong negative evidence for
divergence. Nothing downstream ran: `RFD_ann.m` was never written.

## 12.2 In flight, and how to read its three outcomes

```
  launch_certRFD_long.sh   armed 09:38:45, FIRED 09:54:25   (gated: fires only if the previous
      log says TIME ABORT and RFD_ann.m does not exist -- it cannot race a success)
    certRFD.wl ORD=lk MEMCAP=9e9 ANNCAP=20000 CT1CAP=5400 timeout 24000
      ann deadline 15:27:50 ; hard stop 16:34:25 ; log certRFD_lk.log ; watch memwatch5.log
```

* **returns** → run §11.4's chain; every side condition is discharged (§11.3). **Theorem B.**
* **memory abort at 9 GB** → first evidence `T·ṽ` diverges; the direct route joins the other
  three and the position becomes fully algebraic (§11.7's fallback).
* **time abort at 20000 s** → cost **> 5.5 h** at ≤ 9 GB. Route still open, but it is a hardware
  question: **a bigger box, not a cleverer object.**

## 12.3 Ops

* **The `ORD=kl` waiter behaved.** Gated on `RFD_ann.m`, horizon 400 × 15 s from 07:58; the file
  never appeared, so at **09:38:42** it logged `RFD_ann.m never appeared; ORD swap not launched`
  to `certRF_launch.trace` and exited without taking a seat. **Rule confirmed: gate a waiter on
  a file or a log string, never on a timer** (§19.8's `launch_certQ3_ll.sh` did the latter and
  cost 40 minutes).
* **`[WITHDRAWN]` `Annihilator[T·v] = 124 s, 7 gens`** — struck at source in `PHASE2_CERTS` §1's
  calibration table (with a blanket ⚠ over every timing in it), in §19.2's cost table and prose,
  in the STATUS BOARD, and in this file's §§2 and 11.2. `Put` time, not stage time (§17.5).
* **Box audited and cleaned at 10:00.** Six stale `free -m` loops (sessions 6–7) were killed;
  `memwatch5.log` (pid 2209932) is the only live, correctly-targeted watch, on kernel 2207229.
* **`ps -eo pid,args | grep` truncates and under-reports background loops** — a duplicate watch
  was invisible to it. Audit with `ps -eo pid,ppid,lstart,args` and match on the loop bound.
