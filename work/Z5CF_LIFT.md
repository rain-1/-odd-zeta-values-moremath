# Z5CF_LIFT — `A` lifted to ℤ[n], `a_4` factored, and the honest size of the order-7 certificate

**Agent:** computational-agent (River's odd-zeta program), 2026-07-26
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, code in `work/z5la/`
**Brief:** `work/Z5CF_TELESCOPER.md` §9.1 — lift `A` and the 8 residual cofactor blocks to
`ℤ[n,k,l]`, emit the cleared identities Lean-ready, report the size honestly.
**Labels:** `[PROVED]` · `[VERIFIED range]` · `[MEASURED]` · `[EXCLUDED with bounds]`

---

## 0. HEADLINE — the factorisation of `a_4`

**`A = Σ_{t=0}^{4} a_t(n) S_n^t` is now exact in ℤ[n].** Every `a_t` has degree **58** and
coefficients of **82–85 decimal digits**. All five factor completely over ℚ, and — the point —
they factor through `L_BZ`'s **own** irreducible cubic

```
        a₀(x) = 41218 x³ + 198849 x² + 320790 x + 173057        (Lean: `a0P`)
```

`[PROVED — exact, from the lifted integer coefficients]`

```
  a_0 =    (n+1)²(n+2)²(n+3)³(n+4) · a₀(n+2) a₀(n+3) a₀(n+4) · F_0(n)      deg F_0 = 41
  a_1 = −2 (n+3)²(n+4)             · a₀(n+3) a₀(n+4)          · F_1(n)      deg F_1 = 49
  a_2 = −2 (n+4)                   · a₀(n+1) a₀(n+4)          · F_2(n)      deg F_2 = 51
  a_3 = −2 (n+5)                   · a₀(n+1) a₀(n+2)          · F_3(n)      deg F_3 = 51
  a_4 =  4 (n+5)(n+6)³(n+7)²(2n+13)² · a₀(n+1) a₀(n+2) a₀(n+3) · F_4(n)     deg F_4 = 41
```

with **each `F_t` irreducible over ℚ**. (Internal consistency: the gcds these force —
`deg gcd(a_0,a_t) = 9, 4, 3, 6` — reproduce exactly the measured reduced degrees
`49, 54, 55, 52` of `Z5CF_TELESCOPER` §4.4.)

### The answer to the question that mattered

> **`a_4(n) ≠ 0` for every integer `n ≥ 0`, and it is a five-line Lean proof.**
> `[PROVED]`

* every factor except `F_4` is a product of linear forms and `a₀`-shifts, all strictly
  positive for `n ≥ 0`;
* `F_4` has **exactly one real root `≥ 0`**, at `1.113180042573661259304…`, which is
  **not an integer** — and this needs no root isolation, because

  > `[PROVED]` **`F_4(m+2)` has all 42 coefficients strictly positive**, the smallest being
  > `17 519 109 273 880 859 266 785 645 568` and the largest 61 digits.

  So `F_4(n) > 0` for every real `n ≥ 2`, and `positivity` closes it in one line;
* the two exceptional points are explicit negative integers:

  ```
  a_4(0) = −33581765282109518489684938683276061690088194518588985206006104359585185792000
  a_4(1) = −4035473284898032705358610960797835228948736257597178565234993561609227468800000000
  a_4(2) = +1865870963389461848616416090712608450575357012205388743469751035616491258320938598400000
  ```

**Lean recipe** (this is the deliverable the forward induction of `Z5CF_TELESCOPER` §4.3 needs):

```lean
def F4s (m : ℚ) : ℚ := c₀ + c₁*m + … + c₄₁*m^41            -- all cᵢ > 0, ≤ 61 digits
theorem F4_shift (m : ℚ) : F4 (m + 2) = F4s m := by ring    -- one variable, degree 41
theorem a4_pos  (m : ℕ) : 0 < a4 ((m : ℚ) + 2) := by
  rw [a4, F4_shift]; positivity                            -- everything is a product of
                                                           -- positive linear forms
theorem a4_ne (n : ℕ) : a4 (n : ℚ) ≠ 0 := by
  match n with | 0 | 1 => norm_num [a4] | (m+2) => exact (a4_pos m).ne'
```

`a_4` therefore does **not** have the `cc3 n = 2(n+3)⁵(2n+5)·a0P n` shape — `F_4` is a single
irreducible of degree 41 — but the positivity is nonetheless a one-liner *after the shift
`n ↦ m+2`*, which is what the brief was really asking for. **No desingularisation is needed.**

*(Sign convention: the vector `(a_0,…,a_4)` is the primitive integer one normalised by
`lc(a_0) > 0`. Only `a_4 ≠ 0` matters for the induction; the signs above are stated for that
normalisation.)*

### And the negative, stated loudly

> `[EXCLUDED with bounds]` **The 8 residual cofactor blocks cannot be handed to Lean.** Their
> coefficients are rational functions of `n` of degree `≳ 132/85`; a single cleared block
> identity has `≈ 1.5·10⁶` monomials in `ℤ[n,k,l]` with coefficients of hundreds of bits,
> `≈ 60 MB` each and `≈ 500 MB` for all eight. `ring` will not close any of them, at any
> grouping. This is **not** an artefact of the gauge: repeating the whole sweep with the
> pivot set reversed gives the same exclusion (§4.5).

### And the good surprise

> `[PROVED — exact symbolic]` **7 of the 15 blocks need no `ring` call at all.** They are the
> already-certified Q-row Φ-identity at `n, n+1, …, n+4`, each multiplied by an explicit
> **product of linear forms** `Q_t` and combined with the weights `a_t(n)`. §5.

---

## 1. What was run

| job | what | cost |
|---|---|---|
| `o_asweep.py` | the `a`-direction: `n = 3…419` at `p₁`, `n = 3…199` at 9 more primes, `n = 3…157` at 6 more — order-7 scan `E1` slack 16 | **3120 solves, 0 failures**, 11 workers |
| `o_alift.py` | reduced rational reconstruction per prime, CRT, **LLL simultaneous** rational reconstruction | seconds |
| `o_averify.py` | independent check at fresh `(n,p)` | 33 s |
| `o_afact.py` | factorisation over ℚ, real roots, Pólya/shift positivity | 2 s |
| `o_csweep.py` | the residual cofactor blocks at fixed `(n,p)` — 270 solves forward gauge, 130 reversed | ~35 s each |
| `o_cdeg.py` | degree of the cofactor coefficients in `n` | seconds |
| `o_sym.py`, `o_emit.py` | exact symbolic `S_k,S_l`; the Lean-ready emission | seconds |

Three foreign CPU-bound processes held 3 of the 12 cores throughout; all wall clocks are
under that contention. (A duplicated launch of the first sweep was detected and killed at
17:29; it cost ~25 min of doubled work and no correctness.)

---

## 2. The lift

### 2.1 Degrees `[MEASURED]`

Reduced rational functions `a_t/a_0`, by one nullspace plus a polynomial gcd
(`o_areduce.recon`), from **417 consecutive `n` at `p = 4194301`** and 155–197 samples at 15
further primes:

| | `a_1/a_0` | `a_2/a_0` | `a_3/a_0` | `a_4/a_0` |
|---|---|---|---|---|
| deg num = deg den | 49 | 54 | 55 | 52 |

`lcm` of the four denominators has degree 58 at every prime, so `deg a_t = 58` for all `t`.
The identity that makes this work — and that makes the monic normalisation CRT-consistent —
is `lcm_t (a_0/gcd(a_0,a_t)) = a_0`, valid because the primitive integer vector has
`gcd(a_0,…,a_4) = 1`.

Over-determination: 155–197 samples against `2·56 = 112` unknowns (**1.38–1.76×**), and every
fit is re-checked against *all* samples of its prime.

### 2.2 The arithmetic: why 16 primes, and the LLL step that halved them

The coefficients of `(a_0,…,a_4)/lc(a_0)` have height `≈ 2²⁸⁰`. Balanced two-term rational
reconstruction needs `M > 2H²` — that is `≈ 26` primes of 22 bits. But **all 295 coefficients
share one denominator** `lc(a_0)`, so a lattice of dimension 17 recovers them from
`M ≳ H^{17/16}`. `o_alift.common_den` does this (sympy `DomainMatrix.lll`) and was calibrated
on synthetic data *before* use:

| synthetic height, `M = 2¹³²` | `2⁶⁰` | `2⁸⁰` | `2¹⁰⁰` | `2¹¹⁰` | `2¹¹⁵` | `2¹¹⁸` | `2¹²⁰` | `2¹²⁴` | `2¹²⁸` |
|---|---|---|---|---|---|---|---|---|---|
| true denominator recovered, as top candidate | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |

i.e. it reaches `M^{0.91}` where the balanced method reaches `M^{0.5}`. The real lift then
landed at

```
   16 usable primes  ->  14 in the fit (M = 2^308),  2 RESERVED and never used in the CRT
   LIFTED, and both reserved primes verify.
```

Sizes of the result:

| | `a_0` | `a_1` | `a_2` | `a_3` | `a_4` |
|---|---|---|---|---|---|
| degree | 58 | 58 | 58 | 58 | 58 |
| max `|coef|`, bits | 273 | 279 | 280 | 280 | 270 |
| max `|coef|`, digits | 82 | 84 | 84 | 85 | 82 |

### 2.3 Independent verification `[VERIFIED]`

`o_averify.py` evaluated the exact integer polynomials at **`n ∈ {503, 617, 733, 881}`** — all
beyond the largest `n` ever sampled (419) — at **three primes never used in any fit**
(`4193759, 4193753, 4193743`), and compared with the `a`-direction recomputed from scratch by
the order-7 scan:

```
   12 / 12  MATCH .
```

That is fresh `n` *and* fresh `p`, so it is independent of both the interpolation and the CRT.

---

## 3. The factorisation, in full `[PROVED]`

```
  a₀(x) = 41218x³ + 198849x² + 320790x + 173057                       (irreducible; `a0P`)

  a_0(n) =    (n+1)²(n+2)²(n+3)³(n+4) · a₀(n+2)a₀(n+3)a₀(n+4) · F_0(n),   deg F_0 = 41
  a_1(n) = −2 (n+3)²(n+4)             · a₀(n+3)a₀(n+4)         · F_1(n),   deg F_1 = 49
  a_2(n) = −2 (n+4)                   · a₀(n+1)a₀(n+4)         · F_2(n),   deg F_2 = 51
  a_3(n) = −2 (n+5)                   · a₀(n+1)a₀(n+2)         · F_3(n),   deg F_3 = 51
  a_4(n) =  4 (n+5)(n+6)³(n+7)²(2n+13)² · a₀(n+1)a₀(n+2)a₀(n+3) · F_4(n),  deg F_4 = 41
```

Every `F_t` is **irreducible over ℚ** (sympy `factor_list`, exact). The mod-`p`
irreducible-degree patterns of `a_4`'s squarefree part had already forced a ℚ-factor of degree
`≥ 34` at eight primes — the exact factorisation gives 41, consistent.

`(n+7)` and `(2n+13)` are precisely the factors of `L_BZ`'s own leading coefficient shifted by
four, `c_3(n+4) = 2(n+7)⁵(2n+13)·a₀(n+4)`; and `a₀` reappears at four consecutive shifts across
the five coefficients. The operator `A` is not a generic degree-58 object — it is built out of
`L_BZ`'s arithmetic.

### 3.1 Sign and nonvanishing on ℕ `[PROVED]`

`a_4` is **not** of constant sign on `[0,∞)` — `a_4(0) < 0 < a_4(2)` — so `positivity` cannot be
applied directly, and the brief's `cc3`-style three-liner is genuinely unavailable. What
replaces it:

```
   F_4(m+2)  has all 42 coefficients > 0        [PROVED, exact]
             smallest  17519109273880859266785645568   (the leading one)
             largest   61 digits (202 bits)
   =>  F_4(n) > 0  for every real n >= 2
   F_4(0) = −163297165103558334766985153290812767089243540684800        < 0
   F_4(1) = −597359126028674595220477601913027192865911128064000000     < 0
```

so `a_4(n) > 0` for `n ≥ 2`, `a_4(0), a_4(1) < 0`, and **`a_4(n) ≠ 0` for every `n ≥ 0`**. No
root isolation is used; the shifted-positivity certificate *is* the proof. (For the record,
exact root isolation agrees: `F_4` has exactly one real root `≥ 0`, at `1.1131800425736612593`.)

`[VERIFIED range]` — obtained before the lift and consistent with it: `a_4(n) ≠ 0` and
`a_0(n) ≠ 0` for every integer `n ∈ [0, 10⁷)`, checked simultaneously at nine primes
(`1.8·10⁸` evaluations, zero common zeros).

Certificate files: `work/z5la/a_lift.pkl` (pickle), `work/z5la/a_lift.json` (the five `a_t`,
`F_4`, and the shifted `F_4(m+2)` as integer coefficient lists).

---

## 4. SIZE — the honest answer (Job 4)

### 4.1 The 15 blocks

`M_1 … M_15` = `zla.closure_basis(ŵ₃)`, decreasing degree:

```
  M_1 = u2·xk   M_2 = u2·xl   M_3 = u2·yk   M_4 = u2·yl   M_5 = u2·zk
  M_6 = u2·zl   M_7 = u2      M_8 = u3      M_9 = xk      M_10 = xl
  M_11 = yk     M_12 = yl     M_13 = zk     M_14 = zl     M_15 = 1
```

`xk = H⁽¹⁾_k`, `xl = H⁽¹⁾_l`, `yk = H⁽¹⁾_{n−k}`, `yl = H⁽¹⁾_{n−l}`, `zk = H⁽¹⁾_{n+k}`,
`zl = H⁽¹⁾_{n+l}`, `u2 = H⁽²⁾_{n+k}`, `u3 = H⁽³⁾_{n+k}`;
`ŵ₃ = u3 − (½zk − ½zl + yk − yl − 3/2 xk + 3/2 xl)·u2`, so
`supp(ŵ₃) = {M_1,…,M_6, M_8}`, weights `w = (3/2, −3/2, −1, 1, −1/2, 1/2)` and `w(M_8) = 1`.

| block | route | `deg_n` | bidegree `(k,l)` of the numerator | monomials, cleared | max `|coef|` | `ring`? |
|---|---|---|---|---|---|---|
| `M_1…M_6, M_8` (7) | **Theorem R, `[PROVED]`** | — (product form) | — | *not expanded*: 5 × Q-row lemma (**1294** monomials each, ≤ 73 bits) × a product of ≤ 16 linear forms × `a_t` (58, ≤ 85 digits) | 85 digits | **not needed** |
| `M_7, M_9…M_14` (7) | ansatz `E1` slack 18 | `≳ 132 / 85` (rational) | `(28,28)` | `≈ 1.5·10⁶` | ≥ 280 bits | **NO** |
| `M_15 = ()` | ansatz `Z3` slack 16 | same scale | `(35,35)` | `≈ 1.8·10⁶` | ≥ 280 bits | **NO** |

If one insisted on *expanding* a Theorem-R identity it would have `≈ 8·10⁴` monomials
(tridegree `≈ (123, 21, 29)`) — already beyond `ring`. One must not; §5 shows one need not.

### 4.2 The measurement `[EXCLUDED with bounds]`

`o_csweep.py` solved the seven standalone blocks at **`n = 3…272`, `p = 4194301`** (270 solves;
the coefficient vector has 11 368 entries = 7 blocks × 1624). **One** pivot-column set
throughout, so each coefficient really is a well-defined rational function of `n`.
Reconstructing at the maximal admissible bound `d = 132` (270 samples against 266 unknowns —
an empty nullspace is an *exclusion*, not a failure to find):

| columns probed (random) | reconstructed at `deg ≤ 132` | `deg num` | `deg den` |
|---|---|---|---|
| 20 | **6** | 93 – 132 | 76 – 85 |
| | **14 excluded: no rational function of degree `≤ 132` fits** | — | — |

So the cofactor coefficients are **rational, not polynomial, in `n`**, with numerator degree
`≳ 130` over denominator degree `≈ 80`. (`A`'s coefficients have degree 58; `L_BZ`'s, 9.)
The six that do reconstruct are at only 1.23× over-determination, so read them as a *scale*,
not as exact degrees; the exclusions are exact.

### 4.3 What that costs, in monomials

With `deg_n num = 132`, `deg_n den = 85`, clearing the `n`-denominator gives numerators of
tridegree `(217, 28, 28)`: `218 × 29 × 29 = 183 338` monomials each, over the `(k,l)`
denominator `E1 = (k+1)(l+1)(k+l+1)(k+l+2)∏_{j=1..7}(n+k+j)(n+l+j)`. Clearing a whole block
identity over

```
   D*_i = (k+1)³(l+1)³(k+l+1)²·Dr(n,k,l)·Dr(n,k+1,l)·Ds(n,k,l)·Ds(n,k,l+1)
          · the shift-matrix denominators of §5.2
```

gives `k`- and `l`-degree ≈ 73 and `n`-degree ≈ 273:

| | per residual identity | all 8 |
|---|---|---|
| monomials (dense) | `≈ 74·74·274 ≈ 1.5·10⁶`  (`81·81·274 ≈ 1.8·10⁶` for `()`) | `≈ 1.2·10⁷` |
| coefficient size | `≥ 280` bits (`A`'s own height is already that) | — |
| plain bytes | `≈ 60 MB` | `≈ 500 MB` |

For calibration: `LEAN_Z5_SCAFFOLD` §5.6 measured `ring` at **58 s on a flattened degree-24
three-variable identity**, 8 s cascaded; the Q-row certificate that *is* proved has **1294**
monomials. These are `10³–10⁴ ×` that, and the term ordering alone would exhaust memory during
elaboration.

> **Conclusion, stated as the brief demands:** *every one of the 8 residual identities is too
> large for `ring`.* The order-7 certificate, in this normalisation, is not deliverable to
> Lean. Producing the full ℤ[n,k,l] lift would have cost many hours and produced a ~500 MB
> object of no use to the proof, so **it was deliberately not done** — the measurement was
> done instead.

### 4.4 Why it is that big

The scalar operator `M` for the seven standalone blocks has **rank 1106** against `nc = 1624`
columns, so the cofactor is fixed only up to a **518-dimensional** kernel — the "trivial pairs"
of `Z5CF_LINALG` §4. `fastlin.solve` returns the representative with all non-pivot unknowns
zero. That is a *gauge choice*, and there was every reason to suspect it, not the certificate,
was responsible for degree 132.

### 4.5 It is not the gauge `[MEASURED]`

The entire sweep was repeated with the ansatz monomial order **reversed**, which changes the
pivot set completely and hence the gauge (`o_csweep.ansatzes(rev=True)`, 130 solves,
`n = 3…132`, `p₁`):

```
   reversed gauge, 130 samples:  no relation with max(deg num, deg den) <= 62
                                 on 5 of 5 columns tried  -- same exclusion as the
                                 forward gauge at the same sample count.
```

So the large `n`-degree survives a completely different gauge fixing. It is a property of the
certificate, not of the solver. A *minimal*-degree section would need Beckermann–Labahn
order-basis / Popov-form machinery over `ℚ[n]` on a 518-dimensional module — a real project,
and the one experiment that could still rescue this route (§8).

---

## 5. What IS delivered, exactly (Job 3)

### 5.1 Normalisation — the §5.6(4) statement

* base `Φ_7(n,k,l) = T(n+7,k,l) / ∏_{j=1..7}(n+j)(n+k+j)(n+l+j)(n+k+l+j)`;
  `T(n+i,k,l) = Φ_7·P_i^{(7)}`,
  `P_i^{(7)} = ∏_{j=1..i}(n+j)(n+k+j)(n+l+j)(n+k+l+j)·[∏_{j=i+1..7}(n+j−k)]²[∏_{j=i+1..7}(n+j−l)]²`;
* `ĝ_k = (n+7−k)²(n+k+1)(n+k+l+1)/[(k+1)³(k+l+1)]`, `ĝ_l` the mirror;
* letters `H⁽ʳ⁾_{n+k}, H⁽ʳ⁾_{n+l}, H⁽ʳ⁾_k, H⁽ʳ⁾_l` at base `n`; **`H⁽¹⁾_{n−k}, H⁽¹⁾_{n−l} in the
  MIXED base, i.e. the module letters are `H⁽¹⁾_{n+7−k}` and `H⁽¹⁾_{n+7−l}`.** This is the one
  change from `LEAN_Z5_SCAFFOLD` §5.3, and it is what removes every interior pole;
* uses `T_shift_k`, `T_shift_l`, `T_shift_n`, `T_shift_n2`, `T_shift_n3` and the order-7 `Φ`
  of D1 above. It does **not** use the order-3 `Φ`.

### 5.2 D2 at order 7 — exact shift table `[PROVED — exact symbolic]`

`(S_d)_{ij} ≠ 0` iff `M_i ∣ M_j`; diagonal `1` (unipotent). All off-diagonal entries:

```
S_k :  (M_7 ←M_1)  1/(k+1)               (M_7 ←M_3) −1/(n+7−k)       (M_7 ←M_5)  1/(n+k+1)
       (M_9 ←M_1)  1/(n+k+1)²            (M_10←M_2)  1/(n+k+1)²      (M_11←M_3)  1/(n+k+1)²
       (M_12←M_4)  1/(n+k+1)²            (M_13←M_5)  1/(n+k+1)²      (M_14←M_6)  1/(n+k+1)²
       (M_15←M_1)  1/[(k+1)(n+k+1)²]     (M_15←M_3) −1/[(n+7−k)(n+k+1)²]
       (M_15←M_5)  1/(n+k+1)³            (M_15←M_7)  1/(n+k+1)²      (M_15←M_8)  1/(n+k+1)³
       (M_15←M_9)  1/(k+1)               (M_15←M_11) −1/(n+7−k)      (M_15←M_13) 1/(n+k+1)

S_l :  (M_7 ←M_2)  1/(l+1)               (M_7 ←M_4) −1/(n+7−l)       (M_7 ←M_6)  1/(n+l+1)
       (M_15←M_10) 1/(l+1)               (M_15←M_12) −1/(n+7−l)      (M_15←M_14) 1/(n+l+1)
```

The `(n+7−k)` denominators are **not** poles on the box: they occur only multiplied by `ĝ_k`,
whose numerator carries `(n+7−k)²`.

### 5.3 The 7 Theorem-R blocks — closed form, and no `ring` `[PROVED]`

```
   r_j = w_j · Σ_{t=0}^{4} a_t(n) · r_Q(n+t,k,l) · Q_t(n,k,l)          j ∈ supp(ŵ₃)
   s_j = w_j · Σ_{t=0}^{4} a_t(n) · s_Q(n+t,k,l) · Q_t(n,k,l)

   Q_t(n,k,l) = ∏_{j=1}^{t}(n+j)(n+k+j)(n+l+j)(n+k+l+j) · ∏_{j=t+4}^{7}(n+j−k)²(n+j−l)²
              ( = P_t^{(7)} / P_0^{(3)}(n+t) ,  a POLYNOMIAL for t ≤ 4 )

   Q_0 = ∏_{j=4..7}(n+j−k)²(n+j−l)²
   Q_1 = (n+1)(n+k+1)(n+l+1)(n+k+l+1) · ∏_{j=5..7}(n+j−k)²(n+j−l)²
   Q_2 = ∏_{j=1,2}(n+j)(n+k+j)(n+l+j)(n+k+l+j) · ∏_{j=6,7}(n+j−k)²(n+j−l)²
   Q_3 = ∏_{j=1..3}(n+j)(n+k+j)(n+l+j)(n+k+l+j) · (n+7−k)²(n+7−l)²
   Q_4 = ∏_{j=1..4}(n+j)(n+k+j)(n+l+j)(n+k+l+j)
```

`r_Q, s_Q` are the **already-certified** Q-row Φ-certificate (`work/z5cf/Qrow_phicert.m`:
`r_num` 1294 monomials, tridegree `(25,9,9)`, ≤ 73-bit coefficients).

**The three transport identities**, `[PROVED — exact symbolic, `t = 0…4`, 30 identities, 0
failures]`:

```
   (TR-k)   ĝ_k^{(7)}(n)·Q_t(n,k+1,l)   =  g_k^{(3)}(n+t)·Q_t(n,k,l)
   (TR-l)   ĝ_l^{(7)}(n)·Q_t(n,k,l+1)   =  g_l^{(3)}(n+t)·Q_t(n,k,l)
   (TR-P)   P_u^{(3)}(n+t,k,l)·Q_t(n,k,l) =  P_{t+u}^{(7)}(n,k,l)        u = 0,1,2,3
   g_k^{(3)}(N) = (N+3−k)²(N+k+1)(N+k+l+1)/[(k+1)³(k+l+1)]
```

Both sides of each are **products of linear forms**; each is a one-line `field_simp; ring`.
Multiplying the Q-row identity at `N = n+t` by `Q_t` and applying them gives, for each `t`,

```
   Σ_{u=0}^{3} c_u(n+t)·P_{t+u}^{(7)}(n,k,l)
      = ĝ_k r^{(t)}(n,k+1,l) − r^{(t)} + ĝ_l s^{(t)}(n,k,l+1) − s^{(t)} ,
   r^{(t)} := r_Q(n+t,k,l)·Q_t(n,k,l),   s^{(t)} := s_Q(n+t,k,l)·Q_t(n,k,l),
```

and the seven `supp` block identities are exactly `w_j ×` the `a_t(n)`-weighted sums of these.
The last step needs `V_{t,i} = w_i·Σ_u c_u(n+t)P_{t+u}^{(7)}` for `i ∈ supp` — true because the
shift matrices are unipotent and the `supp` monomials are maximal; `[VERIFIED]` at 3 `(n,p)`,
3150 checks, 0 failures.

`r^{(t)}` is a *polynomial* multiple of `r_Q(n+t,·)`, so it has **no pole anywhere on the box**
— `(B-top)` is free — and `(B-bot)` is free because `r_Q`'s numerator carries `k³`.

### 5.4 Numerical residual check, exact ℚ

`o_emit.residual_check` evaluates the **full** Theorem-R identity — the lifted `a_t(n)`, the
certified `r_Q, s_Q` at `n+t`, the `Q_t`, `ĝ_k, ĝ_l` and the `Σ_u c_u(n+t)P^{(7)}_{t+u}`
right-hand side — at integer `(n,k,l)` in exact ℚ:

```
   n, k, l <= 4 :   125 pole-free points,   0 failures       (o_emit.log)
```

That is an end-to-end check of the lifted `A` against the already-certified Q-row certificate,
in exact rational arithmetic, with no sampling and no prime. (Before the lift landed, the
`t = 0` instance alone was checked the same way at all 64 points of `n,k,l ≤ 3`.)

### 5.5 Delivered files

* `work/z5la/z5cf_order7_partial.json` (228 KB) — operator, base, `M_1…M_15`, the exact shift
  table, `Q_0…Q_4`, `r_Q/s_Q` as integer coefficient lists per monomial, the weights, and an
  explicit note that the 8 residual blocks are **not** delivered and why;
* `work/z5la/a_lift.json` (29 KB) — `a_0…a_4`, `F_4`, and `F_4(m+2)` as integer coefficient
  lists;
* `work/z5la/a_lift.pkl` — the same, pickled.

---

## 6. Verification table

| what | scope | cells | failures |
|---|---|---|---|
| `a`-direction unique (dim 1), all 5 components nonzero | `n = 3…419` at `p₁`; `n = 3…199` at 9 primes; `n = 3…157` at 6 primes | **3120 solves** | **0** |
| degrees of `a_t/a_0` = (49,54,55,52), fit **all** samples of the prime | 417 at `p₁`, 155–197 at 15 more | 5 × 16 | **0** |
| `deg a_t = 58` via `lcm` of the denominators | 16 primes | 80 | **0** |
| rational roots of `a_0, a_4` with multiplicity | `\|u\| ≤ 140`, `v ≤ 12`, 8 primes | 128 | **0 disagreements** |
| `a_4(n) ≠ 0`, `a_0(n) ≠ 0` at every integer `n ∈ [0,10⁷)` | 9 primes simultaneously | `1.8·10⁸` evaluations | **0 common zeros** |
| `common_den` (LLL) calibration | synthetic, `H = 2⁶⁰…2¹³¹`, `M = 2¹³²` | 9 | correct to `M^{0.91}`, fails above — **as designed** |
| **the lift itself: 2 reserved primes, never in the CRT** | 14 fit + 2 reserved | 2 × 295 coefficients | **0** |
| **`A` at fresh `n` AND fresh `p`** | `n ∈ {503,617,733,881}` × `p ∈ {4193759,4193753,4193743}` | 12 | **0 (12/12 MATCH)** |
| factorisation cross-check: `deg gcd(a_0,a_t)` reproduces the measured reduced degrees | `t = 1..4` | 4 | **0** |
| `F_4(m+2)` all coefficients `> 0` | exact | 42 | **0 nonpositive** |
| `V[t,i] = w_i·Σ_u c_u(n+t)P^{(7)}_{t+u}` for `i ∈ supp` | 3 `(n,p)`, 30 points, `t = 0..4`, 7 blocks | 3150 | **0** |
| (TR-k), (TR-l), (TR-P) | `t = 0…4`, exact symbolic in `ℚ(n,k,l)` | 30 | **0** |
| **the full Theorem-R identity with the lifted `a_t`, exactly in ℚ** | integer `n,k,l ≤ 4`, pole-free | 125 | **0** |
| the `t = 0` Theorem-R identity, exactly in ℚ (pre-lift) | integer `n,k,l ≤ 3`, pole-free | 64 | **0** |
| cofactor pivot set constant in `n` | `n = 3…272`, `p₁` | 270 solves | **1 distinct pivot set** |
| cofactor degree, forward gauge | 270 samples, 20 columns | 20 | **14 excluded at `≤132`; 6 at `(93…132, 76…85)`** |
| cofactor degree, **reversed gauge** | 130 samples, 5 columns | 5 | **5 excluded at `≤ 62`** |

Nothing is claimed over `ℚ` or `ℚ(n,k,l)` that was not seen at ≥ 2 primes, and the lift's own
verification uses primes and `n` that no fit ever touched.

---

## 7. Files (`work/z5la/`, new this session)

| file | what |
|---|---|
| `o_asweep.py` | resumable multi-prime `n`-sweep of the `a`-direction (extends `o_areco.sweep`) |
| `o_alift.py` | reduced rational reconstruction per prime, `lcm`-normalised polynomial vector, CRT, and **`common_den`** — LLL simultaneous rational reconstruction with a shared denominator |
| `o_await.py`, `o_atry.py` | retry the lift as primes arrive / exhaustively over LLL parameters |
| `o_averify.py` | independent check of the lifted `A` at fresh `(n,p)` |
| `o_afact.py` | factorisation over ℚ, real roots, shifted-positivity and Pólya exponents |
| `o_csweep.py` | the residual cofactor blocks at fixed `(n,p)`; `rev=True` gives the reversed gauge (extends `o_final.build`) |
| `o_cdeg.py` | degree of the cofactor coefficients as rational functions of `n` |
| `o_sym.py` | exact symbolic `S_k, S_l` and the RHS vector at order 7, mixed base |
| `o_emit.py` | the Lean-ready emission of §5 + the exact-ℚ residual check |
| data | `a_big.pkl`, `a_lift.pkl`, `a_lift.json`, `z5cf_order7_partial.json`, `c_probe.npz`, `c_rev.npz` |
| logs | `o_asweep{,2,3}.log`, `o_await.log`, `o_afact.log`, `o_cprobe{,2}.log`, `o_crev.log`, `o_emit.log` |

`ordm.py`, `o_scan.py`, `o_final.py`, `zla.py`, `solve.py`, `fastlin.py`, `qrow.py`,
`ratrec.py`, `o_areco.py`, `o_areduce.py` are **unmodified**, as instructed.

---

## 8. What remains undone — plainly

1. **The 8 residual cofactor blocks are not lifted, and on this evidence should not be.**
   §4 measures the object at `≈ 500 MB` and shows `ring` cannot take it. Doing the lift anyway
   would have consumed the whole session and produced nothing Lean can use.
2. **The degree-minimising gauge fix was not done.** It is the single experiment that could
   still make the order-7 route Lean-viable: find the minimal-degree section of the
   518-dimensional solution module over `ℚ[n]` (Beckermann–Labahn order basis / Popov form).
   §4.5 shows the naive alternatives (two different pivot orders) do not help, so this needs
   the real algorithm, not another gauge guess.
3. **`w₅` was not touched.**
4. **The `()` block's cofactor was only probed indirectly** — the degree measurement used the
   seven standalone blocks (`do_z=False`) because that solve is 3× cheaper. There is no reason
   to expect `()` to be smaller; it has the larger ansatz.
5. **The sibling agent's lower-order representative, if it lands, makes items 1–2 moot.**
   Nothing in §3 or §5 is wasted if it does: the factorisation of `A` is about `L_BZ`'s
   arithmetic, and the base transport of §5.3 is order-generic.
