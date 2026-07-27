# Z5T3_BRIDGE — the subtraction anchor and the direct weight-5 bridge

**Agent:** Claude (Fable), 2026-07-27, continuing from the 2026-07-26/27 session close.
**Code + data:** `work/z5t3/`.  Paper draft: `bz_compact_weights_proofs.tex` (repo root).
**Labels:** `[PROVED]` · `[VERIFIED range]` · `[MEASURED]` — finite checks are never proof.

## 0. HEADLINE

1. **The top-row anchor is closed — arrow (B) is PROVED, and B5 is not needed for it.**
   The missing identification of the Barnes rational part with `PBZ` follows by a
   *subtraction argument* with NO linear-independence input:

   > `Sigma T·W_B = I_n` (Sol's §§1–4, symbolic) evaluates by the five PROVED upper
   > coefficient identities to
   > `2Q z5 + 4Q z2z3 + 0·z4 + 0·z3 − 4(Sigma T w3sym)·z2 + Sigma T·[1]W_B`.
   > BZ's own display (I_n), proved by recursion + initial values, is
   > `2Q z5 + 4Q z2z3 − 4 P̂ z2 − 2P`.  The middle row (PROVED 2026-07-26) says
   > `P̂ = Sigma T w3sym`.  Subtracting the two evaluations of the same real number
   > kills every transcendental term exactly, leaving
   >
   > **`P_n = −(1/2) Σ_{k,l} T(n,k,l) · [1]W_B(k,l)`  [PROVED]**

   `[1]W_B = r22 + L_k r12 + L_l r21 + (L_kL_l − C2) r11` — the explicit rational
   parts (bare + S/U Euler sums) of the four universal integrals (z5ord0/t_euler.py,
   verified against universal.py on 8 ≤ k,l < 14 in exact arithmetic).
   The two missing z5-level constants are trivial: `[z5]I22 = 2`, `[z2z3]I22 = 4`,
   and only I22 carries them (weight bound p+q+1) ⟹ coefficients `2Q, 4Q` by `Q = ΣT`.
   Also extracted: **`[z2]I22 = −4·H3_{k+l}`** (exact fit, rank-27 system, 49 cells —
   to be re-derived from the §8 master formula for the paper).
   Numeric validation of every link incl. the anchor: `work/z5t3/anchor_check.py`,
   n ≤ 3, coefficient-wise, 8/8 PASS per n.

2. **Consequence: the ONLY remaining gap for `P_n = Σ T·w5` is the finite identity**

   > **(T3)  `Σ T·([1]W_B + 2·w5sym) = 0`**

   — no integrals, no zeta values, no recurrence certificate needed.  Everything else
   in both compact closed forms is now proved (paper draft has full proofs).

3. **T3 status: the 3-component density system went from INCONSISTENT to CONSISTENT
   once two new proved families were added** `[MEASURED]`:
   * live1 (Sol's Laurent span + eps24/25 jets): n≤9 consistent (overfit), n≤11
     INCONSISTENT (163 bad rows), n≤12: 554 bad. The "combined Laurent+jets" shot
     as specified fails — bounded negative.
   * live2 (+ weighted value towers TX with j-weights, + inverse-power weights):
     n≤12: 313 bad (progress, still inconsistent).
   * **live3 (+ k-side letter multipliers on sub-weight towers, + n-coupled weight
     args {n±j, n±l, n+j+l}): n≤14 3-component system CONSISTENT — 0 bad rows with
     1134 dependent rows.**  Holdout not yet stable (canonical solution not pinned
     while rank 2583 < 5633 columns); pushing N.
   * All 5633 columns calibrated null (`Σ T·[a + L_k b + (L_kL_l−C2) d] = 0`,
     n = 3..5 exact-mod-p, plus live1 --check crosschecks vs Sol's Fraction code).

## 1. The two key structural findings for T3

* **The missing generator family was the *weighted value towers*:**
  `0 = Σ_{j∈range} φ(j)·(R_k ρ)(−j)` for ρ a monomial in the lattice blocks Q_r.
  Since ρ has no poles at −j, this vanishes termwise on ALL of (0, n+k], and the
  partial-fraction expansion of R_k·ρ (order ≤ 2 + wt(ρ) at the lattice) turns it
  into the null form `u(l) = Σ_s (−1)^s c_s(l)·Σ_{j∈range} φ(j)/(j+l)^s`, s ≤ 5.
  These produce exactly the high-power crossed sums `Σ_j φ(j)/(j+l)^{3,4}` that the
  U-letters of `[1]W_B` unnest into (`U_{r,m}(a,b) = H^r_a H^m_{a+b} −
  Σ_{j≤a} H^r_{j−1}/(b+j)^m`).  Fixed-pole evaluation facts stop at power 3
  (g double zeros) and can never reach (l+j)^4 — that was the wall.
  Sub-weight towers must be multiplied by k-side letters (args n, k, n±k) to fill
  weight 5 — eps24 did this for its jets, the towers needed it too.
* **The 3-component (a,b,d) density split is optional and can be folded:**
  B_kl = A_kl·L_k, D_kl = A_kl(L_kL_l−C2) with bare L's, so one folded density row
  per cell (`f = a + L_k b + (L_kL_l−C2) d`) suffices for T3.  (The k-free nested
  b-content of the target (e.g. `4S(l,1,3)` in 2r12) obstructs *some* 3-component
  mechanisms but folding dissolves it; empirically the 3-component system closed
  anyway once TX2/EXTW2 were added.)

## 2. Protocol (unchanged from eps25 discipline)

Solve on n ≤ N, hold out N+1; two primes (4194301, second 4194287 — both < 2^22 as
fastlin needs); exact reconstruction (CRT/ratrec) of a stabilized solution;
verify exact on held-out n; then convert to a certificate: every surviving column
family carries a one-line proof (pointwise zero / residue theorem / Laurent
coefficient of an identically-zero function), and the cellwise identity
target = Σ x_i·col_i is finite and exact.  For the *uniform-in-n* statement the
certificate must be re-expressed as an identity in the extended letter ring
(bare letters + S/U/crossed range-sum symbols) — the weight-3 precedent is
Z5CF_EPSILON §12.3 (20-term integer combination, coefficient-wise exact).

## 3. Files

| file | what |
|---|---|
| `z5t3/anchor_check.py` | the anchor validation (8 identities per n, exact, sympy zeta basis) |
| `z5t3/live1.py` | Sol-span + EPS jets; fast mod-p reimplementation, `--check` (vs Fraction code), `--null` |
| `z5t3/live2.py` | + TX weighted towers (j-weights), inverse-power weights, folded assembly |
| `z5t3/live3.py` | + k-side multipliers on sub-weight towers (TX2/TD), n-coupled weight args (EXTW2); primary runs |
| `z5t3/residual25.py` | eps25 bare-ring residual direction (452-entry support, decoded: H⁵ and products at k+l, n+k+l args — recorded for arrow (A), now optional) |
| `z5t3/diag1.py` | bad-row locator for cached systems |
| `live1_p1.log, live1_n11/12.log, live2_n12.log, live3_n14.log` | the measured ladder above |

## 4. Final measured ladder for T3 (this session) — ALL BOUNDED NEGATIVES

| system | families | verdict |
|---|---|---|
| 3-comp n≤9 | Sol Laurent span + eps jets (live1) | consistent (overfit) |
| 3-comp n≤11 / n≤12 | same | **INCONSISTENT: 163 / 554 bad** — the "combined Laurent+jets" shot fails |
| 3-comp n≤12 | + TX weighted towers, inverse weights (live2) | 313 bad |
| 3-comp n≤14 | + k-side fills TX2/TD, n-coupled weights (live3) | consistent, 1134 deprows (overfit at depth:) |
| 3-comp n≤17 | same | **INCONSISTENT: 2323/6324** |
| folded n≤20 | same 5633 columns | **INCONSISTENT: 514/3310, rank 2778** |
| folded n≤20, coeffs in ℚ(n) deg ≤ 2 | ×3 columns | row-limited (rank 3290/3310), INCONCLUSIVE — needs n≈26+ build |
| folded n≤20 + XY 2-var jets | +22 columns | **rank unchanged (2778), nbad 514** — XY jets are per-fiber-reducible (measured: every fiber sum already 0) |

**XY jets** (`z5t3/xyjets.py`): Σ_{k,l}Res_yRes_x[R·ρ(x)σ(y)] with lattice-pole
raising both sides, computed from the 2-variable local germ
(α_m(k)-, β_m(l)-, γ_m(k+l)-jet series, coupling only through (x'+y')^m).
All 22 weight-5 members are exact nulls (verified) but add no rank: the
iterated-residue class with lattice raising collapses into the per-fiber span.

**Formal obstruction identified**: the folded target contains l-free nested
monomials (−6S_{1,4}(k) −2S_{2,3}(k) −2H⁵_k −2H²_kH³_k + w5sym's k-side tower),
and NO per-fiber or iterated-residue null functional carries l-free monomial
content.  So a *formal* cellwise certificate over these families is impossible;
the value-wise 514-row deficit is the numeric shadow.  The only mechanisms that
can carry l-free content:
1. **marginal nulls** `v(n,k)+v(n,l)` with `Σ_k v·S_k(n) = 0`, S_k(n) = Σ_l T —
   their residue calculus comes from the moment ladder
   `Σ_l Res_{y=-l}[y^m R(x,y)] = −[explicit rational in x]`
   (e.g. m=1: Σ_l[g_l(x) − l·q_l(x)] = −P(x)/Q(x)²) — NOT built this session;
2. coefficients rational in n (needs a properly-determined system, n≈26+).

## 4b. THE MOMENT TOWERS (continuation session, same day) — **the deficit closes**

The identified mechanism (1) implemented as `z5t3/momtow.py` — **inhomogeneous
moment towers**: for ρ a Q-block monomial, keep the residue at infinity:

> `Σ_{l=0}^n Res_{z=l}[z^m R_k(z)ρ(z)] = [z^{−m−1}](R_kρ)|_∞ = e(n,k)` (explicit
> power-sum data; sanity-verified exactly mod p at (n,k,ρ,m) samples).

Locally `Res_{z=l}[z^m R_kρ] = γ_kT·Σ_i C(m,i) l^{m−i} [w^{1−i}](E·ρser)` — the
densities carry **polynomial l-weights** (weight-0 letters) and the lower jet
coefficients `[w^{≤0}]`, exactly the content no homogeneous null functional has.
Each fact is inhomogeneous; the explicit costs get their own constraint rows
(`Σ_j y_j·Σ_k φ_j(n,k)e_j(n,k) = 0` per n), so any solution still proves
`Σ T·(target) = 0`.

**Effect: folded n≤20 nbad 514 → 0** (708 MT columns, 4 ρ's × m ∈ {1,2,3} ×
59 k-side letter fills; rank 2778 → 3310 = full cell rank).  BUT the
properly-determined deep test (full n≤26 build, 6225 rows vs 6341 columns,
solve n≤25) is **INCONSISTENT: rank saturates at 3504, nbad = 2707** —
the n≤20 closure was again row-limited.  The moment towers are real content
(+726 rank over the previous 2778 plateau) but the deficit now grows linearly
with rows.

**CONCLUSION — the hypothesis class is refuted, not a family**: across every
calculus implemented (fixed-pole/derivative evaluations with arbitrary letter
weights, bands, jets to order 5, weighted value/derivative towers with k-side
fills, two-variable iterated-residue jets, inhomogeneous moment towers with
cost rows), rank saturates ≈ 3500 on these grids while the target needs the
full row space.  **No cellwise certificate with FIXED letter coefficients over
the local/residue calculus expresses T3.**  Consistent with the formal l-free
obstruction (§4).

**PIVOT (the mapped next campaign): the Δ-certificate / creative-telescoping
class** — coefficients rational in (n,k,l), the class every proved identity of
this kind actually lives in:
> find R, S with  `T·([1]W_B + 2w5sym) = Δ_k R + Δ_l S`,
or two-stage 1-variable CT: stage 1 = l-telescoper for the fiber sums
`V(n,k) = Σ_l T·defect` (fiberprobe.py has exact values; V has no per-fiber
vanishing, no k↔n−k symmetry, partial sums unstructured — genuine content);
stage 2 = k-telescoper for `Σ_k V = 0`.  KEY feasibility fact (verified):
**the U-letters have rational l-shift closure over the bare alphabet**
(`U_{r,m}(k,l+1) − U_{r,m}(k,l) = Σ_{t≤k} 1/(t^r (t+l+1)^m)` partial-fractions
into rationals × bare H-differences), so the defect's l-shift module is
finite-rank over ℚ(n,k,l) and the Z5CF_LINALG doctrine applies (telescoper =
kernel of a finite matrix over ℚ(n,k,l); fastZeil/Wolfram verified working in
this repo).  This is a bounded multi-hour campaign, not attempted tonight.

## 5. Open at the time of writing

* T3 open.  Next session: build the marginal-null family from the moment ladder
  (§4.1), then the ℚ(n)-augmented folded system at n≤26 with pruned columns.
* Second prime + exact reconstruction only after a stabilized hit.
* Paper: `bz_compact_weights_proofs.tex` — Theorems 1 (middle, complete proof),
  2a (anchor, complete proof), 2b (compact top row, conditional on exactly T3),
  §8 = the honest ledger above.  [z2]I22 and [z4]I12 now DERIVED by hand from
  the master formula in the paper (not fit-backed).
* Arrow (A) (`Σ T·B5 = (33/4)Σ T·w5`) is now OPTIONAL for the closed forms; the
  eps25 residual direction is recorded in `z5t3/residual25.log` for the ε-story.
