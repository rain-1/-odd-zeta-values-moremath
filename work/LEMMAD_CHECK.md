# LEMMAD_CHECK — is the proposed vanishing-layer inequality true?

**Author:** mathematician-agent (River's odd-zeta program), 2026-07-26
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, code in `work/lemdchk/`
**Reads / corrects:** `work/SPORADIC_BARE.md` §2.5 and §7.1, `work/LBW_GENERAL.md` T4
**Method:** pure-Python exact arithmetic. `fractions.Fraction` for every certificate;
fixed-precision p-adic integers (`work/lemdchk/pad.py`, modulus `p^30`) for the sweeps,
cross-validated against Fractions cell-by-cell. **No Wolfram kernel was started.**

---

## 0. VERDICT

> **The inequality `v_p(S) + v_p(p^w·w) ≥ 1` on `{p | S}` is FALSE.**
> `[FALSE with counterexample]` for **α (Domb), ε, E** at every prime tested.
> `[TRUE in the tested range]` for **s₇** only, and only at `p ≠ 7`.
>
> Its aggregated weakening — `v_p` of the whole vanishing-layer sum `≥ 1` — is **also
> FALSE** for α, ε, E. And **no admissible weight can repair it**: the defect is
> constant on the affine solution space (for E it is literally independent of the choice
> of decomposition; for α and ε the kernel cannot move it to zero at every prime).
>
> The correct target is not a valuation inequality at all. It is the **cancellation
> identity (LD)** of §4: the vanishing layer is not zero, it equals `χ(p)^e·Δ(a)·A(r)`,
> and it is cancelled by an equal and opposite defect that the surviving layer inherits
> from the *base* cell `a`. `[VERIFIED, 0 failures, p = 5…23, all cells n < p²]`
>
> **Consequence for the count:** SPORADIC_BARE's "do it once and go from 4 to 8" is wrong.
> Proving the stated inequality is possible for **s₇ alone**, giving **4 → 5**. For α, ε
> and E the stated inequality is not merely unproved, it is false, and the real target
> (LD) is a *descent* congruence, not a local Kummer estimate.

---

## 1. T1 — what each document actually claims

Notation as in Theorem LB (`LBW_GENERAL` T4). `S(n,k)` = the binomial summand,
`A(n) = Σ_k S(n,k)`, `B(n) = Σ_k S(n,k)·w(n,k)`, `w(n,k) = Σ_j c_j ∏_t K_χ^{(r_{jt})}(x_{jt})`
the harmonic weight, `w` (unadorned, in the exponent `p^w`) the integer weight 2 or 3.
*The source documents overload the letter `w` for both; that collision is itself part of
why the two statements got conflated.* Below, `𝔴(n,k)` denotes the weight **function**.
`n = ap+r`, `k = bp+s`, `1 ≤ a < p`, `0 ≤ r,s < p`, `e ∈ {0,1}` the (H5) χ-degree.

### (SB) — `SPORADIC_BARE.md` §2.5, the restatement box

> "A Lemma-D substitute is therefore *exactly* the statement
> `v_p(S(n,k)) + v_p(p^w w(n,k)) ≥ 1` for every `k` with `p | S(n,k)`, **and nothing else**."

In symbols this is **termwise in `k`**:

```
(SB)   ∀p ≥ 5  ∀ n = ap+r < p²  ∀k with p | S(n,k):
           v_p( S(n,k) )  +  v_p( p^w · 𝔴(n,k) )  ≥  1 .
```

### (LG) — `LBW_GENERAL.md` T4, "Need the Lemma-D upgrade"

> "For these the two-layer split is *invalid termwise* — **[VERIFIED]** the vanishing-layer
> and surviving-layer defects occur in exactly equal numbers and cancel."

The computation behind that `[VERIFIED]` is `work/lbw/t4_proofcheck.py`, and it is
**per-cell aggregated**, one number per cell `(a,r)`, not per `k`:

```
(LG-V)  V(n) := Σ_{k : p | S(n,k)}  S(n,k)·p^w·𝔴(n,k)   ≡  0                      (mod p)
(LG-U)  U(n) := Σ_{k : p∤S(n,k)}   S(n,k)·p^w·𝔴(n,k)   ≡  χ(p)^e·B(a)·A(r)       (mod p)
```

and the recorded result is that **both fail, in the same cells**. "Termwise" in `LBW`
means *"term by term in the two-term split `p^wB = V + U`"* — i.e. layer by layer — **not**
index by index in `k`.

### How they differ, and which is wrong

They are different statements, and **(SB) ⟹ (LG-V)** (a sum of terms each of valuation
≥ 1 has valuation ≥ 1). `LBW` records `(LG-V)` as **failing**. So `LBW`'s own verified data
already refutes `(SB)` — and `SPORADIC_BARE` cites `LBW` as authoritative while asserting
the contrary. **`SPORADIC_BARE` §2.5 is the document that is wrong.** `LBW` is right; its
only fault is the word "termwise", which invites exactly this misreading.

---

## 2. Instrument validation `[VALIDATED]` — done before any verdict was formed

Code: `work/lemdchk/{pad,decs,selfcheck,audit,audit2,audit3,kernel,diag,cert}.py`.

1. **Reproduced a known verified quantity.** Re-ran `work/lbw/t4_proofcheck.py` unchanged.
   It returns `LBW`'s published figures verbatim: **D has 11 failing cells at p = 5** and
   none at 7, 11, 13; **s₇ has 13 failing cells at p = 7** and none at 5, 11, 13; γ, A, s₁₀
   are clean; and for α, ε, s₇, E the vanishing- and surviving-layer failure counts are
   **exactly equal in every cell block**. My independent re-implementation reproduces every
   one of these counts (`audit.py` columns 3 and 4).
2. **The decompositions are re-validated.** Each of the four weights (`decs.py`, taken
   verbatim from `LBW` T3) reproduces `B(n)` **exactly over ℚ** for `n = 40…49`
   (`selfcheck.py` step 1), against `B` generated from the Malik–Straub recurrence.
3. **The p-adic evaluator is validated against exact Fractions.** For `p = 5` and `p = 7`,
   every cell of every family (2 274 + 3 612 evaluations): **0 valuation mismatches**
   between the fixed-precision p-adic value of `p^w·𝔴(n,k)` and the exact rational one.
4. `v_p(S)` is computed by Legendre/Kummer on the binomial factors and cross-checked
   against `v_p` of the exact integer `S(n,k)` in every certificate of §3.2.

---

## 3. T2 — the exact test

### 3.1 The sweep `[FALSE with counterexample]`

All primes `p ∈ {5,7,11,13,17,19,23}`, **all** cells `n = ap+r < p²` (`1 ≤ a < p`,
`0 ≤ r < p`), **all** summation indices `k` with `S(n,k) ≠ 0`, split by `p | S(n,k)`.
`min` = minimum of `v_p(S) + v_p(p^w·𝔴)` over the vanishing layer; `viol` = number of
`(n,k)` with that sum `< 1`; `cells` = number of cells containing at least one violation.
(`work/lemdchk/audit_main.log`.)

| family | p | **termwise min** | viol (n,k) | bad cells | aggregated `v_p(V)` min | bad cells | vanishing-layer terms |
|---|---|---|---|---|---|---|---|
| **α** | 5 | **−1** | 69 | 10/20 | **0** | 10 | 238 |
| **α** | 7 | **−1** | 284 | 21/42 | **0** | 5 | 957 |
| **α** | 11 | **−1** | 1 596 | 54/110 | **0** | 40 | 6 055 |
| **α** | 13 | **−1** | 3 500 | 78/156 | **0** | 65 | 11 922 |
| **α** | 17 | **−1** | 10 323 | 136/272 | **0** | 136 | 35 272 |
| **α** | 19 | **−1** | 16 150 | 171/342 | **0** | 153 | 55 251 |
| **α** | 23 | **−1** | 34 788 | 253/506 | **0** | 231 | 119 317 |
| **ε** | 5…23 | **0** | 18 … 4 914 | 10 … 253 | **0** | 8 … 230 | 130 … 64 075 |
| **E** | 5…23 | **0** | 18 … 15 552 | 10 … 230 | **0** | 8 … 220 | 238 … 119 317 |
| **s₇** | **5** | **1** | **0** | **0** | **1** | **0** | 148 |
| **s₇** | 7 | **0** | 71 | 22 | **0** | 13 | 567 |
| **s₇** | **11,13,17,19,23** | **1** | **0** | **0** | **1** | **0** | 3 503 … 67 429 |

s₇ additionally checked at **p = 29, 31, 37, 41**: `min = 1`, **0 violations**, in
170 696 / 222 915 / 452 862 / 683 278 vanishing-layer terms (`audit_s7_big.log`).

**End-to-end control, in the same runs:** `v_p(p^w B(ap+r) − χ(p)^e B(a) A(r)) = 1` exactly,
**0 failures** in every cell of every family and prime. The theorem's *conclusion* is fine;
it is the *two-layer proof* that does not close.

### 3.2 Counterexample certificates (exact rationals) `[FALSE with counterexample]`

Full data in `work/lemdchk/cert.log`. The minimal ones:

**α (Domb), p = 5, cell n = 20 = 4·5+0, index k = 5 = 1·5+0.**

```
 S(20,5) = C(20,5)²·C(10,5)·C(30,15) = 9 396 127 751 058 800 640 ,  v_5(S) = 1
 arguments:  k = 5 (⌊k/p⌋=1)   n−k = 15 (3)   2k = 10 (2)   2n−2k = 30 (⌊·/p⌋ = 6 ≥ p)
 𝔴(20,5) = 3863945253740937645295558061 / 9113425761793743841651200000 ,  v_5(𝔴) = −5
 v_5(p³·𝔴) = −2       v_5(S) + v_5(p³·𝔴) = 1 + (−2) = −1  <  1        ***FAILS***
```

The term `S(n,k)·p^w·𝔴(n,k)` is not even `p`-integral. The pole is at `2n−2k = 30 ≥ p² = 25`
(not at `2k`), through the monomials `H_k·H_{2n−2k}²` and `H^{(2)}_k·H_{2n−2k}`.

**ε, p = 5, cell n = 15 = 3·5+0, k = 15.** `v_5(S) = 2`, `v_5(p³𝔴) = −2`, sum `= 0 < 1`;
pole at `2k = 30 ≥ 25`, through `H^{(3)}_{2k}` and `H^{(2)}_{2k}H_{2k}`.
**E, p = 5, cell n = 15 = 3·5+0, k = 15.** `v_5(S) = 1`, `v_5(p²𝔴) = −1`, sum `= 0 < 1`;
pole at `2k = 30`, through `K^{(2)}_{χ₋₄,2k}` and `H_{2k}K_{2k}`.
**s₇, p = 7, cell n = 15 = 2·7+1, k = 14.** sum `= 0 < 1` — but here **no argument is wide**
(all `⌊x/p⌋ ≤ 4 < 7`); the whole defect is the (H4) *coefficient* clause, `v_7(1/28) = −1`.
p = 7 is already excluded for s₇ by `LBW`.

### 3.3 Where the failure lives, structurally

`v_p(p^w·𝔴)` is negative exactly when some argument `x` has `⌊x/p⌋ ≥ p`, i.e. `x ≥ p²`:
then `p^r·H^{(r)}(x) = H^{(r)}(⌊x/p⌋) + p^r·(integral)` and `H^{(r)}(⌊x/p⌋)` has
`v_p = −r` (its `⌊x/p⌋ ∈ [p, 2p−1]` range contains exactly one multiple of `p`).
The observed minima are **uniform in `n` and in `p`**:

| family | wide arguments reachable | pole source | `min v_p(p^w𝔴)` (measured) | `min` of the sum |
|---|---|---|---|---|
| α | `2k` or `2n−2k` (never both: `n < p²`) | `H_k·H_{2n−2k}²`, `H^{(2)}_k·H_{2n−2k}` | **−2** | **−1** |
| ε | `2k` | `H^{(3)}_{2k}`, `H^{(2)}_{2k}H_{2k}` (a priori −3; **−2** after the coefficients cancel one order) | **−2** | **0** |
| E | `2k` or `2n−2k` | `K^{(2)}_{χ₋₄,2k}`, `H_{2k}K_{2k}` | **−1** | **0** |
| s₇ | `2k`, only inside **weight-1** letters | `H_k·H_{2k}` | **−1** | **1** (p ≠ 7) |

ε lands at 0 rather than −2 because its summand `C(n,k)²C(2k,n)²` is a **square**, so
`v_p(S) ∈ 2ℤ` and one Kummer carry already buys 2. s₇ survives outright because `2k` occurs
only in weight-1 letters, so the pole is at most order 1 and a single Kummer carry beats it
everywhere — this is exactly the Lemma-D mechanism, and s₇ is the only one of the four in
which it is not out-run by the pole.

---

## 4. T3 — what actually survives, and what the true target is

### 4.1 (a) The aggregated bound — also FALSE `[FALSE with counterexample]`

`v_p(V(n)) = 0` (not `≥ 1`) in 231/506 cells for α at p = 23, 230/506 for ε, 220/506 for E,
and analogously at every prime (§3.1, column 6). Reproduces `LBW`'s counts exactly.
So weakening (SB) from termwise to aggregated buys nothing.

### 4.2 (b) The paired/cancellation statement — TRUE, and it has a closed form `[VERIFIED range]`

The proof of Theorem LB has **two** vanishing-layer requirements, not one. The second is
hidden inside (H2). Splitting the surviving sum as a product needs the `b`-factor
`Σ_{b∈B_a} S(a,b)𝔴(a,b)` to equal `B(a)`, where `B_a = {b : p ∤ S(a,b)}`. Define the
**base-level defect**

```
        Δ(a) := Σ_{b : p | S(a,b)}  S(a,b)·𝔴(a,b)        (1 ≤ a < p)
```

so that `Σ_{b∈B_a} S(a,b)𝔴(a,b) = B(a) − Δ(a)`. Then, `[VERIFIED, 0 failures]`, all cells
`n = ap+r < p²`, `p = 5,7,11,13,17,19,23` (α, ε, E) and `p = 5,11,13,17,19,23,29,31,37`
(s₇):

```
 (LD)   Σ_{k : p | S(n,k)} S(n,k)·p^w·𝔴(n,k)   ≡   χ(p)^e · Δ(a) · A(r)     (mod p)
 (LD′)  Σ_{k : p∤S(n,k)}  S(n,k)·p^w·𝔴(n,k)   ≡   χ(p)^e ·(B(a) − Δ(a))·A(r) (mod p)
```

Counts: 20/20, 42/42, 110/110, 156/156, 272/272, 342/342, 506/506 cells clean, for **both**
lines, for **all four** families (s₇ at p = 7 excepted — 8/42 fail there, the coefficient
clause again). Adding the two lines returns `p^wB(n) ≡ χ(p)^e B(a)A(r)`, so **(LD) is
exactly the missing ingredient**, and nothing else is missing.

**This is the precise content of `LBW`'s "the defects occur in equal numbers and cancel".**
They are equal in number *because* they are the same number, `χ(p)^e·Δ(a)·A(r)`, with
opposite signs. Note that "equal numbers" is not independent evidence: given the (verified)
conclusion `p^wB(n) ≡ χ(p)^eB(a)A(r)`, `V` fails iff `U` fails, automatically. What is
genuine new information is the **closed form** `χ(p)^e·Δ(a)·A(r)`.

Certificates: α p=5 n=20: `V ≡ Δ(4)·A(0) = 37259/54`, matched to `v_5 = 3`.
E p=7 n=28: `Δ(4) = 379/9`, `χ₋₄(7) = −1`, `V ≡ −379/9`, matched to `v_7 = 2`.

A **pole-free** equivalent of `Δ(a) ≡ 0`, useful because everything in it is `p`-integral
(on `B_a` every argument `x(a,b) ≤ p−1`, measured, `kernel.py`):

```
        Δ(a) ≡ 0 (mod p)   ⟺   Σ_{b : p ∤ S(a,b)} S(a,b)·𝔴(a,b) ≡ B(a)  (mod p).
```

`Δ(a) = 0` identically for `a ≤ (p−1)/2` (then every `b ≤ a` survives); the defect exists
only for `a ≥ (p+1)/2`, and there it is nonzero mod p in 11/11 of those `a` for α at p = 23,
10/11 for ε, 10/11 for E, and **0/11 for s₇**.

### 4.3 (c) A bound with a uniform correction — exists, but is useless

The minima of §3.1 are **uniform in `n` and `p`**, so
`v_p(S) + v_p(p^w𝔴) ≥ −1` holds for all four families `[VERIFIED p = 5…23]` (and `≥ 0` for
ε, E, s₇). But the proof needs `≡ 0 (mod p)`, i.e. `≥ 1`; any constant `c > 0` of slack is
as fatal as an infinite one. **No corrected valuation inequality carries the proof.**

### 4.4 Can a *different* decomposition rescue the split? **No.** `[EXCLUDED]`

`𝔴` is far from unique: the fitting system has a large kernel, so the admissible set is
`𝔴₀ + Ker`. `Δ(a) mod p` is linear in `𝔴` and **is** decomposition-dependent in general, so
this had to be checked. `work/lemdchk/kernel.py` computes an **exact ℚ-basis of Ker** (RREF
mod 4 primes → CRT → rational reconstruction) and verifies every basis vector exactly
(`Σ_k S(n,k)κ(n,k) = 0` over ℚ, `n = 1…21`; **0 bad** in every case), then solves the
`𝔽_p`-linear system `Σ_{b∈B_a} S(a,b)𝔴(a,b) ≡ B(a)` for `a = 1…p−1`.

| family | alphabet | cols | dim Ker | p = 5 | 7 | 11 | 13 | 17 | 19 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|
| **α** | `{k,n−k,2k,2n−2k}` | 40 | 21 | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **α** | `+ n` (enlarged) | 65 | 32 | ✓ | ✓ | **✗** | **✗** | **✗** | **✗** | **✗** |
| **ε** | `{k,n−k,2k,2k−n}` | 40 | 2 | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **ε** | `+ n, 2n−2k` | 98 | 7 | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **E** | `{k,n−k,2k,2n−2k}`+χ₋₄, (H5) | 20 | 10 | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **E** | `+ n`, (H5) dropped | 65 | 28 | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **s₇** | `{n,k,n−k,2k}` (+enlarged) | 14 / 27 | 2 | ✓ *(𝔴₀ works)* | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ |

✗ = the `𝔽_p` system is **inconsistent**: no admissible weight makes the vanishing layer die.
For **E the kernel rank is 0 at every prime** — every admissible weight gives the *same*
`Δ(a) mod p`. **`Δ(a) mod p` is an invariant of the family, not an artefact of the fit.**
Confirmed independently by direct perturbation (`diag.py`): at p = 5, all 10 of E's kernel
vectors leave `(Δ(3),Δ(4)) ≡ (3,1) mod 5` unchanged; for α only `κ₁₈, κ₁₉` move it, and only
along `(1,−1)`, never onto `(0,0)`.

*(Scope, stated honestly: this excludes every weight-homogeneous ℚ-combination of bare
letters at the listed argument forms. It does not exclude a wholly different ansatz —
rational-function coefficients, a constant-term representation, or new letters.)*

---

## 5. T4 — corrections to the record, and the honest remaining gap

### 5.1 `SPORADIC_BARE.md` §2.5 — three errors

1. **The restatement box is false.** `v_p(S)+v_p(p^w𝔴) ≥ 1` on `{p|S}` fails for α, ε, E
   (§3.2), and so does its aggregated weakening (§4.1). A correction banner has been
   added to that file pointing here.
2. **"(H1),(H2),(H3),(H5) hold outright" is wrong on (H2).** (H2) as written in
   `LBW` T4 asserts the surviving set is `{0 ≤ b ≤ a} × Σ_r`. The `b`-side is a **proper
   subset** for every `a ≥ (p+1)/2` — e.g. α at p = 5, a = 3: `b = 0` is dropped because
   `p | C(6,3) = 20`. Measured for all four families at p = 5…23. The correct hypothesis is
   `B_a × Σ_r` with `B_a = {b : p ∤ S(a,b)}`, **plus the new clause `Δ(a) ≡ 0 (mod p)`**,
   which is vacuous in the tame case (there `𝔴(a,b) ∈ ℤ_(p)` and `p | S(a,b)`) and is
   precisely what fails for α, ε, E. `[VERIFIED: (H1) 0 failures, (H3) 0 failures,
   product-region structure 0 failures, all four families, p = 5…23.]`
3. **"the repair needed is a single valuation inequality on one explicitly described set
   of cells" is wrong.** The repair needed is (LD), a congruence tying level `n` to level
   `a = ⌊n/p⌋`. It is a **descent** statement, of the same logical type as the theorem it
   is meant to prove, not a local Kummer-vs-pole estimate. That is a materially larger gap.

### 5.2 `LBW_GENERAL.md` — right, but reword one adjective

`LBW`'s claim is correct in substance and its `[VERIFIED]` figures reproduce exactly.
The word "termwise" in "the two-layer split is *invalid termwise*" means *layer by layer*;
read as *index by index* it produced the (SB) error. Recommend: "the two-layer split is
invalid **layer by layer** (each of `V(n)` and `U(n)` is separately ≢ its intended value);
their defects are equal and opposite". `LBW` may also record the closed form `Δ(a)·A(r)`,
which is new here.

### 5.3 The honest gap, 4 → 5 not 4 → 8

| family | (H1) | (H3) | (H2) product | `Δ(a) ≡ 0` | termwise `(V1)` | what is still needed |
|---|---|---|---|---|---|---|
| **s₇** (p ≥ 5, **p ≠ 7**) | ✓ | ✓ | ✓ | **✓** `[p ≤ 37]` | **✓** `[p ≤ 41]` | **prove two valuation inequalities** → **PROVED** |
| **α** | ✓ | ✓ | ✓ | ✗ | ✗ (min −1) | prove **(LD)** — a descent congruence |
| **ε** | ✓ | ✓ | ✓ | ✗ | ✗ (min 0) | prove **(LD)** |
| **E** | ✓ | ✓ | ✓ | ✗ (invariantly) | ✗ (min 0) | prove **(LD)** |

* **s₇ is the one real opportunity.** Everything Theorem LB needs is `[VERIFIED]` for it,
  and the two missing pieces are genuine valuation inequalities of exactly the shape
  SPORADIC_BARE described:

  > **(V1)** `v_p(S(n,k)) + v_p(p²·𝔴(n,k)) ≥ 1` for all `k` with `p | S(n,k)`, `n < p²`
  > **(V2)** `v_p(S(a,b)) + v_p(𝔴(a,b)) ≥ 1` for all `b` with `p | S(a,b)`, `a < p`
  >
  > `[VERIFIED, 0 violations, p ∈ {5,11,13,17,19,23,29,31,37,41}, every cell n < p², every
  > index k — 1 659 068 vanishing-layer terms; minimum exactly 1, i.e. tight]`
  > `[(V2) VERIFIED, 0 violations, p ∈ {5,11,13,17,19,23,29,31,37}]`
  > s₇'s summand is `C(n,k)²C(n+k,k)C(2k,n)`, weight 2, `𝔴` = the 8-term form of `LBW` T3;
  > `p = 7` is excluded by the coefficient denominators 28, and no other weight repairs it
  > (§4.4). The pole is order ≤ 1 because `2k` occurs only in weight-1 letters, so a single
  > Kummer carry in `C(2k,n)` suffices — this is a *bounded, purely local* problem, exactly
  > as SPORADIC_BARE hoped, but for **one** family, not four.
  >
  > **Doing it takes the proved count from 4 to 5** (γ, A, D, s₁₀, s₇). It does **not**
  > deliver a χ ≠ 1 instance: s₇ has χ = 1.

* **α, ε, E need (LD).** For these, no valuation inequality and no re-choice of weight can
  work. E is the sharpest case: `Δ(a) mod p` is independent of the decomposition, so the
  obstruction is intrinsic. Since E is the programme's only χ ≠ 1 instance, **the first
  proved χ ≠ 1 case is further away than SPORADIC_BARE implied**, and is gated on a descent
  congruence rather than a lemma.

### 5.4 What a successor should do

1. **Prove (V1)+(V2) for s₇** (p ≥ 5, p ≠ 7). Bounded, local, Kummer-vs-order-1-pole.
   This is the only one of the four where SPORADIC_BARE's plan works.
2. **Do not attempt** `v_p(S)+v_p(p^w𝔴) ≥ 1` for α, ε or E — false, with the counterexamples
   of §3.2 — nor the aggregated version, nor a re-fit of the weight (§4.4).
3. **For α, ε, E the target is (LD).** Two structural leads from this audit:
   (a) `Δ(a) = 0` identically for `a ≤ (p−1)/2` — the defect is a *large-`a`* phenomenon;
   (b) the per-digit refinement of (LD), `V_b(n) ≡ χ(p)^e S(a,b)𝔴(a,b)A(r)` for each digit
   `b`, is `[VERIFIED, 0 failures]` for **ε and E** (and s₇, p ≠ 7) at p = 5,7,11,13 — so
   for those two families (LD) is provable **one digit at a time**, which is a much more
   tractable statement. It is **false for α** (e.g. 16/30 defect-digits fail at p = 5),
   so α needs the aggregated form. `work/lemdchk/audit3.log`.

---

## 6. Files (`work/lemdchk/`)

| file | what |
|---|---|
| `pad.py` | fixed-precision p-adic integers, Legendre/Kummer valuations, table verifier |
| `decs.py` | the four families' summands and `LBW`'s decompositions |
| `selfcheck.py` | instrument validation (exact `B(n)`; p-adic vs Fraction valuations) |
| `audit.py` | T2: termwise / aggregated / surviving / end-to-end, per family and prime |
| `audit2.py` | (V2), `Δ(a)`, and the cancellation identity (LD)/(LD′) |
| `audit3.py` | (H1), (H2) product structure, and the per-digit refinement of (LD) |
| `kernel.py` | exact ℚ-kernel of the fit; the `𝔽_p` solvability test of §4.4 |
| `diag.py` | direct perturbation confirmation of §4.4 |
| `cert.py` | exact-rational counterexample certificates (§3.2) |
| `*.log` | every run's output |
