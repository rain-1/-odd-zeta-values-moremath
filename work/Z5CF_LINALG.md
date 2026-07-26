# Z5CF_LINALG — the WZ certificate as a finite matrix kernel: framework, one PROVED
# closed-form reduction, and a measured obstruction at order 3

**Agent:** computational-agent (River's odd-zeta program), 2026-07-26
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, code in `work/z5la/`
**Brief:** obtain the weight-5 (and weight-3) certificate by LINEAR ALGEBRA over the
explicitly known module basis, abandoning Gröbner engines entirely.
**Labels:** `[PROVED]` · `[VERIFIED range]` · `[MEASURED]` · `[EXCLUDED with bounds]`

---

## 0. HEADLINE

1. **The linear-algebra route was built, validated three independent ways, and it
   runs.** `Z5CF_CERT` §7.4 is correct that the certificate is the kernel of a finite
   matrix over ℚ(n,k,l); the whole pipeline is now in `work/z5la/`, entirely
   RISC-free, with a blocked mod-p BLAS solver that does a 3630-column system in
   14 s (the same solve took 221 s with a naive mod-p Gauss–Jordan).

2. **NEW STRUCTURAL THEOREM, and it is the most useful thing here.** The
   top-degree cofactors of the certificate are **forced and available in closed
   form** from the already-`[CERTIFIED]` Q-row pair, with no search at all:

   > **Theorem R (leading reduction).** Let `(r_Q, s_Q)` be the Q-row Φ-certificate,
   > `Σ_i c_i P_i = ĝ_k r_Q(n,k+1,l) − r_Q + ĝ_l s_Q(n,k,l+1) − s_Q`.
   > Write the weight `w = Σ_j w_j M_j` with **constant** `w_j` over the closure
   > basis. Then for **every** monomial `M_j ∈ supp(w)`
   > ```
   >        r_j = w_j · r_Q ,      s_j = w_j · s_Q
   > ```
   > satisfies the `M_j`-component of the certificate system **exactly**.

   *Proof.* Leibniz on `Δ_k(ρ_Q T w)` plus unipotence of the letter shifts (every
   letter shifts to itself + a rational function, so `w(k+1) − w` has strictly
   smaller module degree), plus the Q-row identity. ∎
   `[VERIFIED: residual exactly 0 at 760 sample points, all 7 supp(ŵ₃) components;
   and at 300 points for all 24 supp(w₅) components, at n = 5 and n = 9, two primes.]`

   This closes **7 of the 15** weight-3 blocks and **24 of the 58** weight-5 blocks
   in closed form, and it hands the Lean agent explicit ℤ[n,k,l] identities today
   (§5). The `('u2',)` block closes too, by linear algebra — **8 of 15 at weight 3**.

3. **The weight-5 module is 58, not 64.** `H⁽²⁾_{n+k} − H⁽²⁾_k + H⁽²⁾_{n+l} − H⁽²⁾_l`
   is closed under all three shifts, so it is a legitimate *single* letter; keeping
   the four `H⁽²⁾` letters separate (as the previous session did) inflates the
   closure from 58 to 64. `[VERIFIED, downward-closure computation, §1.2]`

4. **⚠ THE CENTRAL NEGATIVE, and it changes the campaign's target.**
   With the leading cofactors fixed by Theorem R (or left free, or replaced by the
   `k↔l` mirror, or by any element of a 900-dimensional ansatz), the **remaining
   seven weight-3 components — the six single-letter blocks and the constant block —
   have no rational solution**. Measured over **5 denominator families × numerator
   bidegrees up to (32,31) (up to 2047 unknowns per block) × 2600 sample points ×
   n ∈ {3,5,7,11} × 2 primes**: in every single run
   `#violated rows = #rows − rank`, i.e. the right-hand side sits in **generic
   position** relative to the image — there is no partial convergence at all.

   The full 15-block joint system is inconsistent as well, and a **free-coefficient
   telescoper search finds 0 telescoper directions at every order ≤ 8**, on a control
   (the Q-row) where the same test correctly finds exactly **1** order-3 direction.

   > **The natural reading is that `L_BZ · (T·ŵ₃)` is NOT `(Δ_k, Δ_l)`-exact —
   > `L_BZ` annihilates `P̂_n` but is not a telescoper of `T·ŵ₃`.** That is fully
   > consistent with everything sessions 1–8 measured: `ct1` never returned because
   > the order-3 object it was asked to certify does not exist. `[MEASURED,
   > EXCLUDED with bounds — not a proof of non-existence]`

5. **Consequence and the corrected target (§6).** If `L_min = A·L_BZ` is the minimal
   telescoper of order `m > 3`, then `L_min` *does* have a certificate, and
   `L_BZ·P̂ = 0` follows from `L_min·P̂ = 0` by a **finite** argument:
   `X_n := (L_BZ·P̂)_n` satisfies `A·X = 0`, and `X_0 = … = X_{m−4} = 0` are exact
   rational checks. So the campaign should stop asking for an order-3 certificate and
   ask the free-coefficient linear algebra for `m`. The framework does exactly that;
   the cost is given in §6.

6. **Housekeeping measurement.** The in-flight `ct1` with `ORD=kl` (the one lever
   `Z5CF_CERT` §2.4 left open) **MEMORY-ABORTED after 1683 s at 6 GB**
   (`work/z5cf/z5w3b_kl.log`, 14:06). With that, every Gröbner lever listed in
   `Z5CF_CERT` §7 is measured shut. Both standalone kernels were then stopped.

---

## 1. The framework

### 1.1 The equation, exactly

Base `Φ(n,k,l) = T(n+3,k,l) / ∏_{j=1..3}(n+j)(n+k+j)(n+l+j)(n+k+l+j)`,
`T(n+i,k,l) = Φ·P_i`, `deg P_i = 12`, all as in `Z5CF_CERT` §3.2b. Put

```
  ĝ_k = (n+3−k)²(n+k+1)(n+k+l+1) / [(k+1)³(k+l+1)]        ĝ_l = k↔l mirror
  E_w/Φ = Σ_{i=0}^{3} c_i(n) P_i(n,k,l) w(n+i,k,l)  =  Σ_j b_j M_j
```

Writing `R = Φ·Σ_j r_j M_j`, `S = Φ·Σ_j s_j M_j`, the identity
`E_w = Δ_k R + Δ_l S` is **exactly** the ℚ(n,k,l)-linear system

```
   b_i  =  Σ_j [ ĝ_k (S^k)_{ij} r_j(n,k+1,l) + ĝ_l (S^l)_{ij} s_j(n,k,l+1) ]
           − r_i(n,k,l) − s_i(n,k,l)                              (i = 1..J)   (★)
```

with `(S^d)_{ij}` the matrix of the letter shift, `shift_d(M_j) = Σ_i (S^d)_{ij} M_i`.

`[VERIFIED — formulation self-test]` With *arbitrary* rational `r_j, s_j`, the
right-hand side of (★) times `Φ`, evaluated with genuine `HarmonicNumber`s, equals
`Δ_k(Φ·Σ r_j M_j) + Δ_l(Φ·Σ s_j M_j)` **exactly**, at 4 points, for **both** weights
(`J = 15` and `J = 58`). This is the check that licenses everything below.

### 1.2 The module, and why the shifts are unipotent

Every letter is a bare `H^{(r)}_x` with `x` linear in `(n,k,l)`, so it shifts to
*itself plus a rational function*. Hence the closure basis is simply the **downward
closure of `supp(w)` under divisibility**, and every shift matrix is `I + N` with `N`
strictly lowering the number of letter factors.

| weight | letters | `|supp(w)|` | closure `J` | blocks by degree |
|---|---|---|---|---|
| `ŵ₃` | 8 | 7 | **15** | 6 (deg 2), 8 (deg 1), 1 (deg 0) |
| `w₅` | 10 (with the composite `S₂`) | 24 | **58** | 18 (deg 3), 29 (deg 2), 10 (deg 1), 1 (deg 0) |

15 reproduces `Z5CF_CERT` §2.3 exactly. **58 < 64**: `S₂ = A₂(k)+A₂(l)` shifts to
`S₂ + rational` under all of `n,k,l`, so the four separate `H⁽²⁾` letters are never
needed; that removes 6 basis monomials. The weights themselves were re-entered from
the closed forms and re-checked against the exact ladders
`P̂_n = 0, 101/4, 344923/96, 3710571371/4320, 602417685937/2304` and
`P_n = 0, 87/4, 1190161/384, 7682021239/10368, 24943788950905/110592`
(`n = 0..4`) `[VERIFIED]`, and `Σ_i c_i(n)·P̂_{n+i} = Σ_i c_i(n)·P_{n+i} = 0`
exactly for `n = 0..7` `[VERIFIED]`.

### 1.3 Solver

`work/z5la/fastlin.py`: right-looking **blocked** Gaussian elimination over `F_p`
using float64 BLAS (`nb = 64`, `p < 2²²`, so every dgemm accumulation
`nb·(p−1)² ≈ 1.1·10¹⁵ < 2⁵³` is exact). Measured **2.3 s at N = 2000**, i.e. `~16×`
faster than the naive mod-`p` Gauss–Jordan on the real 3630-column system
(221 s → 14 s). Rank-revealing with columns scanned left to right, so the pivot-column
set is the lexicographically first independent set — the same for generic `n` and `p`,
which is what makes the canonical (free-unknowns = 0) solution a well-defined
rational function of `n`.

`[VERIFIED — plant-and-recover]` A certificate with random bidegree-(3,3)
polynomial cofactors was planted in all 15 weight-3 blocks; the joint solver
recovered it at ansatz degrees 3, 4 and 5 with **13 500 rows** and residual
**0**. So the machinery finds a certificate when one exists.

---

## 2. Theorem R — the leading reduction `[PROVED, VERIFIED]`

Using the certified Q-row identity `L_BZ·T = Δ_k(ρ_Q T) + Δ_l(σ_Q T)`, Leibniz gives

```
  E_w = Δ_k(ρ_Q T w) + Δ_l(σ_Q T w) + G ,
  G/Φ = Σ_a c_a P_a[w(n+a) − w]
        − ĝ_k r_Q(n,k+1,l)[w(n,k+1,l) − w]
        − ĝ_l s_Q(n,k,l+1)[w(n,k,l+1) − w]
```

and **each bracket has strictly smaller module degree**, because the letter shifts
are unipotent. Therefore the components of (★) indexed by `supp(w)` are solved
exactly by `r_j = w_j r_Q`, `s_j = w_j s_Q` — the top-degree part of the certificate
requires no search whatsoever.

| check | result |
|---|---|
| weight 3, all 7 `supp(ŵ₃)` components, 760 random points mod `p` | residual **0** |
| weight 5, all 24 `supp(w₅)` components, 300 points, `n = 5` and `n = 9` | residual **0** |
| the other 8 / 34 components with the free blocks set to 0 | residual `≠ 0` (as expected — they carry `G`) |

Concretely for `ŵ₃ = u₃ − Ψ u₂`, `Ψ = ½z_k − ½z_l + y_k − y_l − 3/2 x_k + 3/2 x_l`
(`x=H_·`, `y=H_{n−·}`, `z=H_{n+·}`, `u_r = H^{(r)}_{n+k}`):

```
   r_{u3}      = r_Q                 s_{u3}      = s_Q
   r_{u2·z_k}  = −½ r_Q              r_{u2·z_l}  = +½ r_Q
   r_{u2·y_k}  = −1  r_Q             r_{u2·y_l}  = +1  r_Q
   r_{u2·x_k}  = +3/2 r_Q            r_{u2·x_l}  = −3/2 r_Q      (and s likewise)
```

**In addition**, the `('u2',)` block is solvable by the linear algebra (residual 0
with `nc = 544`, denominator
`(k+l+1)∏_{j=1..3}(n+k+j)(n+l+j)∏_{j=0..3}(n+j−k)(n+j−l)`, bidegree (20,20)),
at `n ∈ {3,5,7,11}` and both primes. **So 8 of the 15 weight-3 blocks are settled.**

---

## 3. The measured obstruction `[MEASURED, EXCLUDED with bounds]`

With the leading blocks fixed by Theorem R, each remaining component becomes a
**standalone scalar WZ problem** `f_i = ĝ_k r(k+1,l) − r + ĝ_l s(k,l+1) − s` with a
completely known right-hand side. Its pole structure was measured exactly by
univariate rational reconstruction (130 samples, full factorisation, zero
unfactored remainder):

| component | `den_k(f)` | `den_l(f)` | growth |
|---|---|---|---|
| six letter blocks `(x_k),(x_l),(y_k),(y_l),(z_k),(z_l)` | `(n+k+1)(n+k+2)(n+k+3)(k+l+1)(k+l+2)` | `(n+l+2)(n+l+3)(k+l+1)(k+l+2)` | `k⁶, l⁶` |
| `('u2',)` | `(k+1)(n−k)(n+1−k)(n+2−k)(n+3−k)(k+l+1)(k+l+2)` | mirror + `(n+l+2)(n+l+3)` | `k⁶, l⁶` |
| `()` | `(k+1)(n+k+1)²(n+k+2)²(n+k+3)²(n−k)(n+1−k)(n+2−k)(n+3−k)(k+l+1)(k+l+2)` | `(n+l+2)(n+l+3)(n+1−l)(n+2−l)(n+3−l)(k+l+1)(k+l+2)` | `k⁵, l⁶` |

All of these are **pole-free on the telescoping box** `0 ≤ k,l ≤ n+4`. Nevertheless:

| ansatz for `(r,s)` | unknowns per block | rows | verdict |
|---|---|---|---|
| `D₁ = (k+l+1)(n+k+1)(n+k+2)(n+l+2)`, bidegree (9,8)…(27,26) | 161 … **1457** | 2600 | inconsistent, `nbad = rows − rank` |
| `D₂ = D₁·(n+k+3)(n+l+3)`, bidegree (10,9)…(28,27) | 199 … **1567** | 2600 | idem |
| `D₃ = D₂·∏_{j=0..3}(n+j−k)(n+j−l)`, bidegree (14,13)…(32,31) | 391 … **2047** | 2600 | idem |
| `D₄ = D₂·(k+l+2)(n+k+l+1)(n+k+l+2)`, bidegree (13,12)…(31,30) | 337 … **1921** | 2600 | idem |
| `D₅ = [(k+l+1)(n+k+1)(n+k+2)(n+k+3)(n+l+2)(n+l+3)]²`, bidegree (14,12)…(32,30) | 362 … **1982** | 2600 | idem |

`nbad = rows − rank` **in every one of the 25 runs**: the right-hand side is in
generic position relative to the image at every ansatz size, so this is *not* an
"almost solvable, needs more degree" situation. Independently varied and unchanged:

* `n ∈ {3, 5, 7, 11}` and `p ∈ {4194301, 4194287}` — **identical rank and identical
  `nbad` in all 8 combinations**, so the obstruction is not an unlucky specialisation;
* boundary constraint on/off — dropping `k | N_r`, `l | N_s` and re-running at
  `nc = 882` (bidegree (24,24) over `D₃`) still gives `nbad = 843 = 1500 − 657`;
* leading cofactors from Theorem R, **or** from their `k↔l` mirror
  (`ρ'(n,k,l) = σ_Q(n,l,k)`, also a valid Q-row certificate), **or** left free and
  solved jointly with the letter block (2-block system, up to 1368 columns) —
  all inconsistent, all with `nbad = rows − rank`.

**Full joint systems** (all `J` blocks free simultaneously — the coordinate-free test):

| ansatz | columns | rows | result |
|---|---|---|---|
| polynomial, bidegree 9 | 3000 | 3900 | INCONSISTENT (rank 2531) |
| polynomial, bidegree 10 | 3630 | 6000 | INCONSISTENT (rank 2978) |
| polynomial, bidegree 12 | 5070 | 6000 | INCONSISTENT (rank 3962) |
| `(k+l+1)∏_{j=1..3}(n+k+j)(n+l+j)`, bidegree (12,12) | 4680 | 6000 | INCONSISTENT (rank 3760) |
| `(k+l+1)∏_{j=1..3}(n+k+j)(n+l+j)`, bidegree (18,18) | **10 260** | **11 400** | INCONSISTENT (rank 7390); free-`d` order ≤ 3: **0** directions |

> ⚠ A caution recorded because it cost this session an hour: the bidegree-10 system
> at **3000 rows** *is* consistent, and the same system at **6000 rows** is not.
> Under-sampling a polynomial identity manufactures false consistency. Every verdict
> above uses `rows ≥ 1.3 × columns`, and every *negative* verdict is rigorous
> regardless (a functional solution would satisfy every sampled row).

### 3.1 The free-coefficient telescoper search, with a control

Replacing `c_i(n)` by unknowns `d_0..d_m` turns (★) into the *creative telescoping*
problem itself, still pure linear algebra: the number of order-`≤m` telescopers whose
certificate lies in the ansatz is `(m+1) − [rank(M|W) − rank(M)]`.

| object | ansatz | order ≤ 3 | ≤ 4 | ≤ 5 | ≤ 6 | ≤ 8 |
|---|---|---|---|---|---|---|
| **Q-row control** (`J = 1`, `L_BZ` is `[CERTIFIED]` here) | `(k+l+1)`, bidegree 12, 400 rows | **1** | 1 | — | — | — |
| weight 3 | polynomial bidegree 10, 3900 rows | 0 | 0 | 0 | 0 | 0 |
| weight 3 | `(k+l+1)∏(n+k+j)(n+l+j)`, bidegree 12, 6000 rows | 0 | 0 | 0 | 0 | — |
| weight 3, 2-block subsystem | bidegree 21 and 25, `nc` up to 924, 2800 rows | 0 | 0 | 0 | 0 | 0 |

The control finds **exactly the one** order-3 telescoper that is known to exist, and
nothing spurious. On the weight-3 object the same test finds nothing at any order up
to 8 within the ansätze reached.

---

## 4. Why the naive triangular cascade does not work (recorded so nobody retries it)

Unipotence makes (★) block-triangular by monomial degree, which *looks* like `J`
independent scalar problems solvable top-down. **It is not**, and the reason is
sharp: the certificate is unique only up to a *trivial pair*
`(δ,ε) = (ĝ_l h(l+1) − h, −(ĝ_k h(k+1) − h))`, and changing a high-degree block by a
trivial pair changes the *lower* blocks' right-hand sides by something that is **not**
in the image of the same operator. A cascade that picks an arbitrary representative
at each level therefore poisons every level below it. Measured: the six weight-3
degree-2 blocks each solve in isolation with a bidegree-8 *polynomial* ansatz
(`nc = 144`), and every degree-1 block then fails.

Theorem R is exactly the statement of **which** representative is the right one at the
top. It is the fix for the top level — and it is not enough to make the rest close.

---

## 5. What can be handed to Lean today

For each `M_j ∈ supp(w)` the `M_j`-component of the certificate identity is
`w_j ×` the Q-row identity, so it is already in the D1–D5 shape of
`LEAN_Z5_SCAFFOLD` §S5, with the *same* `A`, `B`, `D*` as `work/z5cf/Qrow_phicert.m`.
With `A`, `B` the pre-factored numerators of `r_Q, s_Q` and

```
  D* = (k+1)³(l+1)³(k+l+1)(k+l+2)(n+1)²(n+2)²(n+l+2)(n+l+3)
```

the cleared identity in **ℤ[n,k,l]**, one for each `M_j ∈ supp(w)`, is

```
  (2 w_j) · D* · Σ_{i=0}^{3} c_i(n) P_i(n,k,l)
    =  (2 w_j) · [   (l+1)³(n+3−k)²(n+k+1)(n+k+l+1)        · A(n,k+1,l)
                   − (k+1)³(l+1)³(k+l+2)                   · A(n,k,l)
                   + (k+1)³(n+3−l)²(n+l+1)(n+k+l+1)(n+l+2) · B(n,k,l+1)
                   − (k+1)³(l+1)³(k+l+2)(n+l+3)            · B(n,k,l) ]
```

with `2w_j ∈ ℤ` equal to `2` for `M_j = H⁽³⁾_{n+k}` and to `−1, +1, −2, +2, +3, −3`
for `M_j = H⁽²⁾_{n+k}·{H_{n+k}, H_{n+l}, H_{n−k}, H_{n−l}, H_k, H_l}` respectively
(weight 3); the 24 weight-5 constants are the coefficients of `w₅`, all in `½ℤ`
(denominators `{2,4}`), so `4w_j ∈ ℤ` suffices there. Each is discharged by `ring`
from the single already-`[PROVED]` Q-row polynomial identity by multiplying by an
integer — no new work.

**Both obligations of `Z5CF_CERT` §5.5 are vacuous for these components**, for the
same reason they were vacuous for the Q-row: the identity is an integer multiple of
the `J = 1` Q-row identity, which carries no letters, so the ℚ(n,k,l) statement and
the ℕ-truncated / `1/0 = 0` Lean statement coincide. They will *not* be vacuous for
the residual blocks, and the two checks must be run on those when they exist.

**Also recorded, and useful independently of all the above:** normalising the letters
at a **mixed base** — `H^{(r)}_{n+3−k}, H^{(r)}_{n+3−l}` instead of `H^{(r)}_{n−k},
H^{(r)}_{n−l}`, everything else at base `n` — **removes `Z5CF_CERT` §5.5's second
pole source entirely**. `P_a`'s double zeros `∏_{j=a+1}^{3}(n+j−k)²` exactly cancel
the poles `1/(n+j−k)^r` that the normalisation introduces. `[MEASURED]` the
right-hand-side coefficients then have denominators only `(n+k+j)`, `(n+l+j)`,
`j = 1,2,3`, whose zeros are at `k,l = −n−j`, **outside** the range — so the
interior poles at `k,l = n+1,n+2,n+3` that §5.5 flagged, and with them the whole
"two different statements" problem, simply disappear. Any successor formalisation
should use the mixed base.

---

## 6. What a successor should do next, in order

1. **Stop asking for an order-3 certificate; ask for `m`.** Run the free-coefficient
   search of §3.1 on the full weight-3 system with the leading blocks *fixed by
   Theorem R* (which removes 7 of 15 unknown blocks and all of the top-degree
   freedom) and the residual 8 blocks at denominator `D₃` and bidegree ≈ (20,20)
   (`nc = 544`): **columns `8·544 + (m+1) = 4361`, rows `15·600 = 9000`, one solve
   ≈ 90 s** at `p < 2²²` with `fastlin`. Scan `m = 4..12`. This is a *bounded*
   computation with a stated size, and it decides the question.
1a. **How to parametrise the order-`m` search so that Theorem R still applies.**
   The telescoper ideal of `T` itself is generated by `L_BZ` (that is what
   `Qrow_phicert.m` certifies), so any telescoper of `T·w` that is also one of `T`
   has the form `A·L_BZ`, `A = Σ_{t=0}^{m−3} a_t S_n^t`. Then
   `(S_n^t L_BZ)·T = Δ_k(ρ_Q(n+t,k,l) T(n+t,k,l)) + Δ_l(σ_Q(n+t,k,l) T(n+t,k,l))`,
   so the Q-row cofactor for `S_n^t L_BZ` over the base `Φ` is, in closed form,
   ```
      r^{(t)}(n,k,l) = r_Q(n+t,k,l) · P_t(n,k,l) / P_0(n+t,k,l)
   ```
   and Theorem R gives the top-degree blocks as `r_j = w_j · Σ_t a_t r^{(t)}`,
   **linear in the unknowns `a_t`** — so the free-coefficient search keeps all of
   Theorem R's savings. ⚠ One base change is required: `P_j = T(n+j,k,l)/Φ(n,k,l)`
   is polynomial only for `j ≤ 3`, so for order `m` re-base on
   `Φ_m = T(n+m,k,l)/∏_{j=1..m}(n+j)(n+k+j)(n+l+j)(n+k+l+j)`; `ĝ_k` then reads
   `(n+m−k)²(n+k+1)(n+k+l+1)/[(k+1)³(k+l+1)]` and everything else is unchanged
   (`zla.gk_val` / `zla.Pi` take the `3` from a single place).

2. **If `m` is found**, the certificate for `L_min` follows from the same solve, and
   `L_BZ·P̂ = 0` follows from `L_min·P̂ = 0` by the finite argument of §0.5
   (`A·X = 0` plus `m−3` exact initial values) — which is *easier* to formalise than a
   certificate, not harder.
3. **Weight 5 costs no more than weight 3 in the leading part.** Theorem R already
   gives 24 of the 58 blocks; the residual 34 blocks at `nc ≈ 544` are
   `34·544 = 18 496` columns, `58·700 = 40 600` rows — ≈ 2.8·10¹³ flops, ~8 h on one
   core with `fastlin`, i.e. ~45 min across the 12 cores if split by `(n,p)`.
   Bounded, and it cannot OOM: peak memory is one `rows × cols` float64 array.
4. **Do not re-run:** the scalar cascade (§4 — measured poisoned); any Gröbner lever
   (`ct1` `ORD=lk` time-abort 5402 s; `ct1` `ORD=kl` **memory-abort 1683 s at 6 GB**,
   new this session; `OreGroebnerBasis` reduction factor 1.000×; the two-delta
   `CreativeTelescoping` call shape); any ansatz for the six weight-3 letter blocks
   or the constant block at order 3 up to the bounds of §3.
5. **Under-sampling guard.** Never accept a consistency verdict with
   `rows < 1.3 × columns`; §3's caution is a real trap that produced a false positive.

---

## 7. Files (`work/z5la/`)

| file | what |
|---|---|
| `zla.py` | letters, module algebra, closure basis, weights, `P_i`, `c_i`, `ĝ_k/ĝ_l`, mixed-base normalisation |
| `solve.py` | ansatz class, `PointData` (per-`(n,p)` numeric data: `b`, `S^k−I`, `S^l−I`, `ĝ`), naive mod-`p` RREF |
| `fastlin.py` | **blocked mod-`p` BLAS elimination** — the enabling piece (16× on the real systems) |
| `joint.py`, `jfix.py`, `sub2.py` | the full joint system; joint with blocks fixed (Theorem R); the 2-block necessary subsystem |
| `qrow.py` | fast mod-`p` evaluation of the certified Q-row Φ-certificate (`work/z5cf/Qrow_phicert.m`) |
| `ratrec.py`, `recon.py` | univariate rational reconstruction (pole detection), CRT + rational lifting |
| `cascade.py` | adaptive scalar cascade with automatic ansatz design from measured poles — kept as the record of §4 |
| `t_fix*.py, t_scal.py, t_sweep.py, t_nrob.py, t_full.py, t_last.py, t_w5.py, freed.py` | the experiments of §2–§3, with their `.log` files |

Reproduction:

```bash
cd /home/ubuntu/fable-episode-2/zeta-math-2/work/z5la
python3 t_w5.py       # Theorem R at weight 5: 24 of 58 blocks, residual 0
python3 t_sweep.py    # the scalar obstruction sweep of section 3
python3 t_nrob.py     # its robustness over n and p
python3 freed.py q0   # the free-coefficient control: exactly 1 order-3 direction
python3 t_full.py     # the full-system verdict
```

No RISC package is loaded anywhere; no Wolfram kernel is used at all.

---

## 8. Honest status

| task | status |
|---|---|
| **framework** | **DONE and validated** — formulation self-test exact at both weights; plant-and-recover at 13 500 rows; Q-row control. |
| **weight-3 certificate** | **PARTIAL. 8 of 15 blocks settled** — 7 in closed form by Theorem R (`r_j = w_j r_Q`), 1 (`H⁽²⁾_{n+k}`) by linear algebra. The remaining 7 have **no rational solution within the bounds of §3**. |
| **weight-5 certificate** | **PARTIAL. 24 of 58 blocks settled in closed form** by Theorem R, verified at two `n` and two primes. The residual 34 blocks were not attempted at order 3 because the weight-3 evidence says the target is wrong. |
| **is `L_BZ` a telescoper?** | **Evidence says NO for both weight rows**, `[EXCLUDED with bounds]` at every ansatz reached, robust over `n`, `p`, boundary conditions, and the choice of leading representative — but this is a measured negative, not a proof. |
| **matrix sizes** | stated throughout: weight-3 full system `4680–5070 columns × 6000 rows`; the decisive residual system of §6.1 is `4361 × 9000`; weight-5 residual `18 496 × 40 600`. |
| **the two §5.5 checks** | **vacuous for every component delivered** (each is an integer multiple of the letter-free Q-row identity); and the **mixed-base normalisation removes the second pole source altogether**, which retires the problem for successors. |
