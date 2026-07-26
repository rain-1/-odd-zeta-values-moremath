# Z5CF_EPSILON — the ε-deformation of the BZ summand exists, and it is the dressed l-shift

**Author:** mathematician-agent (River's odd-zeta program), 2026-07-26
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, code + data in `work/z5eps/`
**Labels:** `[PROVED]` · `[VERIFIED range]` · `[MEASURED]` · `[EXCLUDED with bounds]`
Exact arithmetic (`Fraction`/ints) for every positive identity; rank/exclusion statements
mod two 31-bit primes `p₁ = 2147483647`, `p₂ = 2147483629` (identical output at both).

---

## 0. HEADLINE

**The one-parameter deformation exists.** With `T_ε := T·exp(Σ_{m=1}^{5} ε^m L_m)` and the
explicit rational `L_m` of §3 (first order: **`L₁ = −2·∂_l log T`**, the shift `l → l−2ε`,
dressed at orders 2–5), the double sum produces all three graded pieces at exactly the
Frobenius orders:

> **`Σ_{k,l} T_ε = Q_n + ε³·t·P̂_n + ε⁴·X_n + ε⁵·(t²/4 + 8t)·P_n + O(ε⁶)`**
> **`[ε¹] = [ε²] = 0` exactly; one modulus `t`; at `t = 1`: `(P̂_n, X_n, (33/4)P_n)`.**
> `[VERIFIED exact over ℚ, n = 0…16, 0 failures; mod p₁,p₂ n = 0…80, 0 failures]`

* **`[ε³]` termwise is the closed form.** At the underlying special point the ε³-Bell
  coefficient's kernel direction is *exactly* `ŵ₃^sym = (X₃+Y₃)/2 − (Ψ/2)(X₂−Y₂)` —
  coefficient for coefficient, not merely modulo nulls (§2.3). The compact weights of
  `ZETA5_CLOSEDFORM` are **Bell-polynomial coefficients of one Γ-deformation**: the
  degree-2/3 product structure (`Ψ·(X₂−Y₂)`, `αΨ·X₃`, …) is `exp`'s `L₁L₂`, `L₁²L₃`, …
  This answers "why the weights are what they are".
* **`[ε⁴] = X_n ∉ span_ℚ{Q, P̂, P}`** — for *every* admissible choice of the order-4
  deformation letters `[EXCLUDED, both primes, incl. exact best-fit residuals n ≤ 16]`.
  So `L_BZ` annihilates the family at orders `0,1,2,3,5` and **not** at order 4. The
  ε-orders that carry rows are exactly `{0,3,5}` = the measured `diag(1,p³,p⁵)` **spike**
  (`ZETA5_CLOSEDFORM` §5.2: only s = 3,5 resonate) — two independent computations now
  point at the same three exponents, with the ε⁴ outsider matching the crystal's missing
  weight-4 piece.
* **The Apéry control shows this is the generic shape, not a defect:** for the *proved*
  weight-3 family of `APERY_DEFECT` §7.1, `[ε⁴]Σ_k A_ε ∉ span_ℚ{a_n, b_n}` for every
  choice of `e₄` (exact rank 4/4, n ≤ 12). **"`L` annihilates the deformation identically
  in ε" is false even in the weight-3 precedent**; the true statement there and here is
  per-order annihilation at the row orders.
* **Un-normalised (keep the `Γ(1+jε)` constants), the family produces BZ's purified
  linear forms with forced ζ-coefficients:**

  > **`[ε³]Σ T̃_ε = −t·(Q_nζ(3) − P̂_n) = −t·I″_n`,  `[ε⁵]Σ T̃_ε = −t₅·(Q_nζ(5) − P_n) = −t₅·I′_n`**

  because the letter-exponent totals obey **`e₂^tot = 0`, `e₃^tot = 3t₃`, `e₄^tot = 0`
  (choice), `e₅^tot = 5t₅` (null-invariant, hence forced)** — the exact analogue of the
  weight-3 "the ζ(3) the Γ-series cannot avoid is the Apéry limit". The Γ-constant is
  `C(ε) = exp(−tζ(3)ε³ − t₅ζ(5)ε⁵ + …)`: **odd zetas only**, the archimedean face of
  `LAMBDA_HUNT`'s `exp(−Σ_{m odd≥3} ζ_p(m)·…)`. The ζ(2)·ζ(3) impurity of `I_n` **never
  appears**: the deformation is even-zeta-blind and lands on the pure rows `I′, I″`
  directly (§5).
* **By-product — a pencil of weight-3 closed forms.** Every point of the line
  `{α₁+α₂+α₃ = 0}` of antisymmetric directions carries a rank-drop kernel; e.g. the
  `α`-letter point gives the new exact identity `[VERIFIED exact, n ≤ 10]`

  > `P̂_n = Σ T·[ 4H³_n − (H³_k+H³_l) − ½(H³_{n+k}+H³_{n+l}) + α·((H²_k−H²_l) − ¼(H²_{n+k}−H²_{n+l})) ]`,
  > `α = A₁(k)−A₁(l)`.  `ŵ₃^sym` is the `Ψ`-point of this pencil.

---

## 1. The space searched

`T = (n+k)!(n+l)!(n+k+l)!·n! / [ (k!)³(l!)³((n−k)!)²((n−l)!)²(k+l)! ]` — nine Γ-letters.
Deformation space = the weight-3 template's, per letter: multiply by Pochhammer ratios
`Π_j(L)^{c_{L,j}}`, `Π_j(x) = ∏_{i≤x}(1+jε/i)`, giving

> `log(T_ε/T) = Σ_m ε^m L_m`,  `L_m = ((−1)^{m−1}/m)·Σ_L e_m(L)·H^{(m)}_L`,
> `e_m(L) = Σ_j c_{L,j} j^m ∈ ℚ` **free per letter per order** (shifts j = 1…5 +
> Vandermonde realise any prescribed `(e₁,…,e₅)`, so this is the complete per-letter space).

Coordinates used: 6 symmetric letter-classes `[n, {k,l}, {n±k,n±l}, k+l, n+k+l]` +
3 antisymmetric pair-differences. Necessary conditions solved order by order (the
"pinning"), demanding `[ε^m]Σ ∈ span_ℚ{Q, P̂, P}` at every order (the `L_BZ` condition).

## 2. The pinning cascade — what each order forces

### 2.1 Order ε¹ `[VERIFIED, 2 primes, n ≤ 34]`
`rank[M1(6 sym)|Q,P̂,P] = 7` ⇒ `[ε¹] ∈ span{rows}` forces `[ε¹] = 0` and `S₁ ∈ N₁`,
`dim N₁ = 2`: `N₁ = ⟨D1, V1⟩` with `D1 = (∂_k+∂_l)log T` (the `V_n = 0`-type residue
identity: `Σ_k ∂_k[T_Γ] = 0` per fixed l via `T_Γ(n,·,l) = (sin²πz/π²)·O(z^{−2})`-rational,
same mechanism as `APERY_GAP` §3 — provable by the same residue theorem, not written out
here) and a second vector `V1 = [2,1,−2,−1,2,0]`. Antisymmetric `A₁` is free (relabelling).

### 2.2 Order ε² — the α-line `[VERIFIED, 2 primes]`
The symmetric quadratics `Σ T·{X², XY, Y²}` all lie in the span of the six weight-2 sums
(no condition on `(a,b)`); the antisymmetric quadrics reduce to exactly **3 conditions**
which factor as `α₂·(Σα) = α₃·(Σα) = 0`, `α₁² = (α₂+α₃)²`, i.e.

> **the admissible antisymmetric directions are exactly the line `α₁+α₂+α₃ = 0`**

(coefficient-sum zero over the three pair-letters; `Ψ ↔ (−3,1,2)` lies on it). On the
line the E2 solution is unique with `(s₂,u₂,v₂) = 0` forced: `[ε²] = 0` exactly.

### 2.3 Order ε³ — the pencil, and `ŵ₃` as a kernel vector `[VERIFIED, 2 primes]`
At every line point the 12-column system `[M3sym | A₁·w₂-columns | rows]` has rank 11:
a **1-dim kernel**, i.e. a pencil of identities `Σ T·(S₃ + A₁A₂) = t₃P̂`. At the Ψ-point
the kernel is *exactly* `(y, β, t₃) = ((X₃+Y₃)/2, −¼(X₂−Y₂)-dir, 1)`, i.e. `ŵ₃^sym`
itself. Two exceptional points (`α`-dir `(1,1)`-combination and `α+β`) have `t₃ = 0`
(null identities). With `S₁ ≠ 0` the inhomogeneous E3 is consistent on the whole
parameter space (the `β`-columns absorb the RHS) — order 3 imposes no further condition.

### 2.4 Orders ε⁴/ε⁵ — the special point
`[ε⁵] ∈ span{rows}` (with the order-4/5 letters `z, γ, w, δ` free) is a strong condition;
the scan over primitive `(a,b,c,d)`, `|a|,|b|,|c| ≤ 5`, `0 ≤ d ≤ 5`, `t ∈ {1,2}` — 12 944
combos — returns **5 hits = exactly 2 families modulo the symmetries** k↔l and ε↔−ε
(§3, §6). `[ε⁴]` fails everywhere (§5).

### 2.5 Negatives along the way `[EXCLUDED with bounds]`
| statement | bound |
|---|---|
| termwise-pure BZ deformation (`[ε¹]=[ε²]=0` termwise, Apéry §7.1 style) | impossible: `[ε³]` would be a degree-1 bare form; `ZETA5_CLOSEDFORM` §2.2's 155–170-excess negative + our `L₁=0` control (unique solution ≡ 0, rank 8/8) |
| k↔l-**symmetric** deformation (6-class space) | ε³-consistency ⇔ `4a³−12a²b+11ab²−5b³ = 0`, **irreducible over ℚ** (no rational root; disc −1712 < 0, one real direction in a cubic field); 26 excess residual rows, 2 primes |
| α off the line `Σα = 0` | dies at ε² (three quadric conditions, complete factorisation, 2 primes) |
| ε-uniform `L_BZ`-annihilation | `[ε⁴] ∉ span{Q,P̂,P}` for every admissible order-4 choice, joint and alone, 2 primes; same failure for the **proved** Apéry family (`[ε⁴] ∉ span{a,b}`, exact, rank 4/4) |

## 3. THE DEFORMATION (family 1, t = 1 member) `[VERIFIED exact ℚ n ≤ 16; mod p₁,p₂ n ≤ 80]`

Per-letter data (class order `[n, {k,l}, {n+k,n+l}, {n−k,n−l}, k+l, n+k+l]`; antisym =
pair differences, k-side minus l-side):

```
  L1 = −2·∂_l log T = −2[ H_{n+l} + H_{n+k+l} + 2H_{n−l} − 3H_l − H_{k+l} ]
  L2 = −4H²_n − 8H²_k + 10H²_l − (17/4)H²_{n+k} − (7/4)H²_{n+l} + 8H²_{n−l}
       + 2H²_{k+l} − 2H²_{n+k+l}
  L3 = 24H³_l − (5/3)H³_{n+l} − (64/3)H³_{n−l} + (8/3)H³_{k+l} − (8/3)H³_{n+k+l}
  L4 = −68(H⁴_k−H⁴_l) + (31/32)(H⁴_{n+k}−H⁴_{n+l}) − 64(H⁴_{n−k}−H⁴_{n−l})
       + 4H⁴_{k+l} − 4H⁴_{n+k+l}
  L5 = (528/5)(H⁵_k+H⁵_l) + (37/40)(H⁵_{n+k}+H⁵_{n+l}) − (512/5)(H⁵_{n−k}+H⁵_{n−l})
       + (32/5)H⁵_{k+l} − (32/5)H⁵_{n+k+l}
```

(`L₄, L₅` are one representative of a 4-dim null freedom; the row outputs are
null-invariant.) Then, with `B_m` the Bell coefficients of `exp`:

> **`Σ_{k,l} T·B₁ = Σ T·B₂ = 0`, `Σ T·B₃ = P̂_n`, `Σ T·B₄ = X_n`, `Σ T·B₅ = (33/4)·P_n`.**

Parity/structure of the letter table (a finding, not an input): `e₁, e₃` are purely
l-sided, `e₄` purely antisymmetric, `e₅` purely symmetric; the letters `k+l, n+k+l`
carry the exact pure-shift values `∓(−2)^m` at all five orders. The `e_m(L)` table is in
`work/z5eps/eps_solution.json`; realisation as `∏_j Π_j(L)^{c_{L,j}}`, `j = 1…5`, is
Vandermonde. **One modulus `t`** (the ε³-kernel scale): `(t₃, t₅) = (t, t²/4 + 8t)`,
verified at `t ∈ {−1,1,2,3,5,10}`; `t` mixes `ŵ₃^sym` into `L₃` (and `−¼(X₂−Y₂)` into
`L₂`), i.e. the ζ(3)-object feeds the ζ(5)-coefficient — `t₅` depends on `t` — while Q
never mixes back.

## 4. The un-normalised family: BZ's I′, I″ with forced ζ's `[VERIFIED via e-totals, exact]`

Keeping the raw `Γ(x+jε)/Γ(x)` (no `Γ(1+jε)`-normalisation) multiplies `Σ T_ε` by
`C(ε) = exp(Σ_m (−1)^m ζ(m) e_m^{tot} ε^m/m)`, `e_m^{tot} = Σ_L e_m(L)` (`e₁^tot = 0`, no γ).
Measured: `e₂^tot = 0` (forced: E2 solution unique), `e₃^tot = 3t = 3t₃`,
`e₄^tot = 0` (choice; representative-dependent), `e₅^tot = 165/4·(t-scaled) = 5t₅`
(**null-invariant: all four E5-null directions have `Σ mult·w = 0`** — the ζ(5)
attachment cannot be removed). Hence `C(ε) = 1 − tζ(3)ε³ − t₅ζ(5)ε⁵ + O(ε⁶)` and

> `Σ T̃_ε = Q_n − ε³·t·I″_n + ε⁴·(X_n) − ε⁵·t₅·I′_n + O(ε⁶)`,

the exact ζ(5)-analogue of `APERY_DEFECT` §7.3(c) (`[ε³] = 2(b_n − ζ(3)a_n)`, ζ-coefficient
forced). Note what does **not** appear: no `ζ(2)Q` at ε², no `ζ(4)Q` at ε⁴ (choosable), no
`ζ(2)ζ(3)` and no `ζ(2)·P̂` at ε⁵ — the deformation produces the **motivically purified**
rows (BZ's "set ζ(2) to zero" is, in ε-language, `e_even^tot = 0`), and the purification
constant `c = −3/π²` never enters. `C(ε)` has the odd-zeta-only shape of the Bloch–Vlasenko
/ `LAMBDA_HUNT` generating series `exp(−Σ_{m odd ≥3} ζ_p(m)·…)` — the archimedean face of
the same object, now attached to the *deformation itself*.

## 5. The ε⁴ coefficient — the outsider that matches the crystal

`X_n = [ε⁴]Σ T_ε`: `0, 95329/64, 1023189029/9216, …` — exact best-fit over `{Q,P̂,P}` on
`n = 0..2` leaves nonzero residuals at 14 of 17 n `[VERIFIED exact]`; with all order-4
letters free the membership system is inconsistent at rank 12/12, both primes, jointly
with ε⁵ and alone. **Interpretation:** the BZ crystal has graded pieces at weights 0, 3, 5
only (`diag(1, p³, p⁵)`, measured as a spike, not a step); a weight-4 row does not exist
(Poincaré duality kills ζ(4)-dual '`ζ(1)`'), and the deformation's ε⁴-coefficient is
accordingly *outside* the L_BZ solution space. The identical phenomenon occurs at weight 3
(Apéry `[ε⁴] ∉ span{a,b}`, exact) where the deformation is nevertheless `[PROVED]` and
load-bearing. Per-order annihilation at the row orders is the correct invariant statement.

## 6. Family 2, and the solution inventory `[MEASURED]`

Scan inventory (primitive tuples, `|a|,|b|,|c| ≤ 5`, `0 ≤ d ≤ 5`, `t ∈ {1,2}`, 12 944
combos; plus `|·| ≤ 3` with `t ∈ {0,±1,2,3}`): nontrivial hits = family 1 at `(−1,0,1,2)`
(all t), its ε↔−ε/k↔l image at `(1,0,1,2)` (`t₅ = −t²/4+8t`), and

> **family 2:** `(a,b,c,d;t) = (−2,−1,0,1;2)` — `S₁ = −2X−Y`, `A₁ = β`-letter direction,
> isolated in `t`; `[ε³] = −32·P̂`, `[ε⁵] = −256·P` (`t₅/t₃ = 8` exactly, = the `t→0`
> limit of family 1's ratio `t/4 + 8`); e-totals again `e₂ = 0, e₃ = 3t₃, e₅ = 5t₅`.
> `[VERIFIED exact ℚ n ≤ 10; identical data at both primes]`

Uniqueness is bounded, not proved: the ε⁵-conditions are polynomial in `(a,b,c,d,t)` and
only heights ≤ 5 were scanned. The complete statements are: `S₁`-space (2-dim) and the
α-line (1-dim) are **exactly** the ε¹/ε²-loci; within them the scan found exactly the two
families above.

## 7. Answers to the programme's step-5 questions

1. **Why the weights are what they are:** `ŵ₃^sym` is the ε³ Bell coefficient
   (`L₃ + L₁L₂ + L₁³/6`) of the dressed l-shift — its degree-2 term is literally `L₁L₂`
   with `L₁`-antisym `∝ Ψ` and `L₂`-antisym `∝ X₂−Y₂`; `w₅`'s degree-3 Horner structure
   is `B₅`'s product terms. The Horner tower in `H^{(r)}_{n+k}` and the two antisymmetric
   letters `α, β` of `ZETA5_CLOSEDFORM` §3.1 are the sym/antisym components of one
   deformation on the `Σα = 0` line.
2. **Why orders 3 and 5:** `[ε¹]` dies on `N₁` (residue identities), `[ε²]` on the α-line;
   weight 4 has no row to land on; 3 and 5 are the first orders where `H^{(3)}`, `H^{(5)}`
   enter the Γ-expansion — the same reason `ζ(3), ζ(5)` are the constants `C(ε)` carries.
3. **Frobenius grading:** the ε-orders `{0,3,5}` coincide with the measured
   `diag(1,p³,p⁵)` spike, including the *absence* at 2 and 4. The two computations are
   independent; the coincidence is now structural, not numerological.
4. **The ζ(2)ζ(3) impurity:** absent. The deformation is even-zeta-free (`e_even^tot = 0`)
   and produces `I′, I″` directly; the impurity of `I_n` and its `12/(2πi)²` purification
   constant belong to the *Betti/cycle* side (which cycle you integrate over), not to the
   deformation side. The ε-route sees the pure de Rham rows only.

## 8. What this buys — and does not buy — the Lean effort

* **Not available:** the "single telescoping certificate at ε⁰ gives all rows" prize.
  It required `L_BZ(Σ T_ε) = 0` identically in ε; that is `[EXCLUDED]` at ε⁴ here **and
  in the proved weight-3 precedent**, so this was never the right target.
* **Available now:** explicit summand-level weights `B₃, B₅` (rational harmonic forms)
  with `Σ T·B₃ = P̂` and `Σ T·B₅ = (33/4)P` — *new representations* of both companion
  rows, plus the pencil of §2.3 (a 1-parameter family of weight-3 representations to
  choose from for certification; only the `Ψ`-point was known before). Whether some
  pencil member has a smaller telescoper than `ŵ₃`'s order 7 is an open, cheap-to-measure
  question — the pencil is exactly the kind of freedom the telescoper scan never had.
* **Conceptually:** the closed forms stop being fitted objects; they are Taylor
  coefficients of `T·exp(−2ε∂_l + …)`. For a Lean formalisation the natural restatement
  of the two unproved sum-identities is: the ε³ and ε⁵ coefficients of one explicit
  deformation identity. The pencil also gives, at each line point, *independent* linear
  relations among the `Σ T·(harmonic monomial)` sums that could shrink the certificate's
  side-condition load.

## 9. Traps, addressed

* **`GAMMA_UNIFICATION`'s "Gamma-deformation hypothesis REFUTED"** concerned the
  archimedean κ-constants' `⟨ζ(5), ζ(2)ζ(3)⟩` coincidence (forced by dimension) — a
  different question entirely; nothing there bears on the summand deformation, and
  nothing here contradicts it. (Curiously the *pure* objects agree: `λ₅ ∈ ℚ·ζ(5)` there,
  even-zeta-free `C(ε)` here.)
* **Trap 2 (naive space fails):** confirmed in force — the symmetric-space route dies on
  an irreducible cubic, the pure-Ψ antisymmetric point dies at ε⁴/ε⁵, and the answer sits
  at a mixed point (`−D1 + 2Ψ` = the l-shift) that only a full search of the 9-letter
  space with both sym and antisym components could find.

## 10. Verification table

| # | statement | method/range | cells | failures |
|---|---|---|---|---|
| V1 | `L₁ = −2∂_l log T` (letter identity) | exact, all cells n ≤ 8 | 285 | 0 |
| V2/V3 | `[ε¹]Σ = [ε²]Σ = 0` | exact ℚ, n ≤ 16; mod p₁,p₂ n ≤ 80 | 17+2·81 | 0 |
| V4 | `[ε³]Σ = P̂_n` (t = 1) | exact ℚ n ≤ 16; mod p₁,p₂ n ≤ 80 | 17+162 | 0 |
| V5 | `[ε⁵]Σ = (33/4)P_n` | exact ℚ n ≤ 16; mod p₁,p₂ n ≤ 80 | 17+162 | 0 |
| V6 | `X_n ∉ span{Q,P̂,P}` | exact best-fit + mod-p rank, 2 primes | 17 | (14/17 nonzero residuals) |
| V7 | e-totals `(0, 3t, 0, 5t₅)`; `Σmult·w` null-invariance | exact + mod-p null basis | — | 0 |
| V8 | `t₅(t) = t²/4+8t` at t = −1,1,2,3,5,10 | mod p₁ all six; t = 1,2,3 also at p₂ | 9 | 0 |
| V9 | family 2: `[ε³] = −32P̂`, `[ε⁵] = −256P` | exact ℚ n ≤ 10; data at 2 primes | 11 | 0 |
| V10 | pencil identity at the α-letter point = P̂ | exact ℚ n ≤ 10 | 11 | 0 |
| V11 | N₁ (rank 7), α-line quadrics (d = 3, same factorisation), pencil rank ≡ 11, sym-space cubic | mod p₁ **and** p₂, n ≤ 30–34 | — | 0 |
| V12 | Apéry control: `[ε⁴] ∉ span{a,b}` ∀e₄ | exact ℚ, n ≤ 12, rank 4/4 | 13 | — |

Finite checks are never proof: the five identity families (V2–V5, V9) are verified, not
proved; their natural proof route is the residue calculus of `APERY_GAP` §3 applied to
`(sin²/π²)·rational` in each variable, which already proves the `N₁`-identities.

## 11. Files (`work/z5eps/`)

| file | what |
|---|---|
| `eps1.py`–`eps3.py` | symmetric-space cascade; the irreducible-cubic exclusion |
| `eps4.py` | tensor sweep (1358 moment accumulators, both primes) |
| `eps5.py`, `eps6.py` | point pipeline (E2–E5 stages; eps6 = corrected columns) |
| `eps7.py`, `eps8.py` | pure-Ψ branch: τ-column test, per-order ε⁵ test |
| `eps9.py` + inline runs | N₁ with rows; the α-line quadrics |
| `eps10.py`, `eps11.py` | joint E4+E5 and E5-only along the line |
| `eps12.py`, `eps13.py` | mixed-branch scans (E3 universality; the ε⁵ hit) |
| `eps14.py`, `eps15.py` | special point: joint test, null structure, data extraction |
| `eps16.py` | **exact-ℚ verification of the family, n ≤ 16** |
| `eps17.py` | hardening: null-invariance, family 2, n ≤ 80 range, letter table |
| `eps_scan5.py`, `eps_scan5.log` | the H = 5 inventory scan (12 944 combos, 5 hits) |
| `eps_solution.json` | machine-readable deformation data (both families, conventions) |

**Next actions someone should take:** (i) prove the five sum-identities by the residue
calculus (the only unformalised step; each is a `(sin²/π²)·rational` residue-sum in one
variable at a time); (ii) measure the telescoper order across the §2.3 pencil — any
member below order 7 immediately cheapens the P̂ certificate; (iii) push the tensor sweep
to ε⁶/ε⁷ to see whether `[ε⁶]` carries `Q`-multiples (ζ(3)²-flavour) as `C(ε)`'s shape
predicts, and whether a second modulus appears.
