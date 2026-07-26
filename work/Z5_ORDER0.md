# Z5_ORDER0 — order-zero certificates for the Barnes kernel identities

**Agent:** order-0 (Claude), 2026-07-26. Code: `work/z5ord0/`.
Everything below is exact (`fractions.Fraction`, ints, or mod-p with
`p1 = 4194301`, `p2 = 4194287`). Finite checks are never called proof.

---

## 0. Headline

| target | status |
|---|---|
| T1 — unwanted ζ(3) | `[PROVED]` by Codex §7.2 — **dropped**, not re-derived here |
| T2 — ζ(2)/compact-weight-3 bridge | `[PROVED, structural]` — **independently verified here, every step, including sensitivity** |
| T3 — rational/compact-weight-5 bridge | **open**. Route-deciding fact established: *the Euler/coupled sums do NOT cancel*. Sharp ranges for `g_l, g_l', q_l` pinned with edge witnesses; `[1]I^{p,q}` DERIVED from §8 |
| order-0 certificates | **no `[EXCLUDED]` verdict issued** — the ζ(4) calibration does not pass, so per discipline 2 nothing is reported as a negative |

Two results are new and independent of everything else in the programme:

1. **The universal rational coefficients `[1] I^{p,q}` are now DERIVED, not fitted**
   (`work/z5ord0/ratpart.py`), directly from §8's finite formula. This discharges
   the caveat on the fitted `r11/r12/r21/r22`.
2. **The Euler-sum content of target 3 survives the `T`-weighted sum** — neither the
   univariate `S_{r,m}` part nor the bivariate `U_{r,m}` part vanishes. Target 3 is
   therefore *not* of the pure rational-product shape that closed T1, T2 and ζ(4).

---

## 1. Target 2 — independent verification of the structural proof `[VERIFIED, all steps]`

Codex's §7.3 proof was checked step by step in `work/z5ord0/t_verify2.py` and
`t_verify2b.py`. The first half of that proof came out of `t_struct.py` in this
directory; the verification below is deliberately arranged so that **every
displayed identity has both sides generically nonzero**, because the naive
end-to-end check compares three quantities that are all `0` and is therefore
vacuous.

### 1.1 The chain

With `x = s+n+1`, `y = t+n+1`,

```
R_n(x,y) = prod_{i=1}^n (x-i)(y-i)(x+y-i) / [prod_{i=0}^n (x+i)^2 (y+i)^2]

g_l(x) = lim_{y->-l}(y+l)^2 R_n = c_l P1(x) P2(x) / prod_{i=0}^n (x+i)^2
P1 = prod_{r=1}^n (x-r),   P2 = prod_{r=1}^n (x-l-r),
c_l = prod_{r=1}^n(-l-r) / prod_{i != l}(i-l)^2   (nonzero)

Q_k(y) = d/dx[(x+k)^2 R_n]|_{x=-k} = g_k(y) Lambda_k(y)
Lambda_k(y) = -sum_{i=1}^n 1/(k+i) + sum_{i=1}^n 1/(y-k-i)
              - 2 sum_{i != k} 1/(i-k)
```

**Zero structure of `g_l` (index ranges checked rigorously — this is where an
off-by-one would hide):**

* `P1(j) = 0` iff `1 <= j <= n`;
* `P2(j) = 0` iff `1 <= j-l <= n`, i.e. `l+1 <= j <= l+n`;
* the denominator `prod_{r=0}^n (j+r)^2 != 0` for every `j >= 1`.

Hence, for `0 <= l <= n`:

```
g_l(j)  = 0   for 1 <= j <= n+l            (union of the two ranges)
g_l'(j) = 0   for l+1 <= j <= n            (intersection: a DOUBLE zero)
```

The intersection is `{1..n} ∩ {l+1..l+n} = {l+1,...,n}`; when `l = 0` the two
products coincide and the numerator is `P1^2`, still a double zero on `1..n`.
There is **no triple zero anywhere** — `g_l''(j) != 0`. That matters for T3 (§3).

### 1.2 Verification table

| # | statement | range | cells | failures |
|---|---|---|---|---|
| 0 | Barnes translation `R_orig(s,t) == R_xy(x,y)` | `n<=6`, 3 generic rational `(x,y)` | 21 | 0 |
| 1 | closed form of `g_l` as the double-pole residue | `n<=5`, all `l`, 3 generic `x` | 63 | 0 |
| 2 | `sum_k C12(k,l) = sum_k C11(k,l) = 0` | `n<=9`, all `l` | 55 | 0 |
| 3a | `g_l'` partial-fraction form == product form | `n<=9`, all `l`, 4 generic `x` | 220 | 0 |
| 3b | `g_l(j) = 0`, `1<=j<=n+l` | `n<=9` | 385 | 0 |
| 3c | `g_l'(j) = 0`, `l<j<=n` (double zero) | `n<=9` | 165 | 0 |
| S1 | `L_k - L_l = -2 Psi` cellwise | `n<=6` | 140 | 0 |
| S2 | `H^(r)_{n+k}-H^(r)_{k+l} = sum_{j=l+1}^n (k+j)^-r`, `r=2,3` | `n<=8` | 570 | 0 |
| S3a | `sum A (H3_{n+k}+H3_{n+l}) = 2 sum A H3_{n+k}` | `n<=7` | 8 | 0 |
| S3b | `sum (B-C)(H2_{n+k}-H2_{n+l}) = 2 sum B (...)` | `n<=7` | 8 | 0 |
| S3c | `sum (B+C) H2_{k+l} = 2 sum B H2_{k+l}` | `n<=7` | 8 | 0 |
| S4 | `4 sum A w3sym = 4 sum A H3_{n+k} + 2 sum B (H2_{n+k}-H2_{n+l})` | `n<=7` | 8 | 0 |
| S5 | `X1 = Y1`, `X2 = Y2 - 2 sum B H2_{n+l}`, and that last term `= 0` | `n<=7` | 8 | 0 |
| 4 | `Delta_direct == Delta_middle == -2 sum_l sum_{j>l} g_l'(j)` | `n<=8` | 9 | 0 |
| 5 | **target 2 itself**, `-¼ sum T coeff_z2(W_B) == sum T w3sym` | **`n=13..18`** | 6 | 0 |

S3, S4, S5 are the sensitive ones. Sample magnitudes at `n=7`:
`4 sum A w3sym = -202896348993489544115868841/17798901120000`,
`X1 = -153088524901343213815223/8899450560000`, `X2 = +X1` with opposite sign —
both sides genuinely nonzero, so the symmetry steps and the index ranges are
actually being tested.

Row 5 is outside the `n = 0..12` range covered by `work/z5barnes/verify_global.py`,
so it is independent evidence rather than a re-run.

**Verdict: the §7.3 proof of target 2 is correct.** Every ingredient — the
translation, the product form of `g_l`, `sum_k B_kl = 0`, the double-zero index
range, both symmetry reductions, and the `L_k - L_l = -2Psi` substitution — holds
exactly. Target 2 is `[PROVED]` and is dropped.

Also confirmed independently (this was the first half, produced here before the
Codex message arrived, `t_struct.py`):

```
sum_{k,l} T coeff_zeta2(W_B)
   = -4 sum T H^(3)_{k+l}  -  sum T (L_k+L_l) H^(2)_{k+l}
```
because the discarded part is `-2 sum_k sum_{j=1}^{k} Q_k(j)`, and `Q_k(j) = 0`
for `1 <= j <= k` since `g_k(j) = 0` there while `Lambda_k(y)` has poles only at
`y = k+1,...,k+n`. Checked exactly for `n = 0..6`; the `Q_k(j)` vanishing checked
exactly for `n <= 8`.

Also verified independently here: **§7.1's universal coefficient table** (all 16
entries of `[z3],[z2],[z4],[z5],[z2z3]` for the four `I^{p,q}`) against
`universal.py` on `0 <= k,l <= 5` — 0 failures (`w_check.py`).

---

## 2. The alphabet — measured, then DERIVED `[PROVED modulo §8]`

The brief's alphabet warning is confirmed, and sharpened.

### 2.1 What is in the bare span

Measured by exact-ℚ fit over `0 <= k,l <= 7` with held-out check on
`8 <= k <= 10`, `0 <= l <= 10` (`alpha.py`, `t_alpha.py`):

```
[zeta(2)] I^(2,2) = -4 H^(3)_{k+l}          <-- pure bare, one term
```

Consequently **`coeff_zeta2(W_B)` lies entirely in the bare alphabet**, at
degree 3 (not 2). This is why Sol's earlier projection to the *degree-<=2* bare
weight-3 span came back inconsistent: the obstruction was the degree cap, not the
alphabet. Cellwise agreement of the bare formula with `universal.py` verified for
`n <= 4`, all `k,l` (`t_struct.check_cellwise_z2`).

### 2.2 What is not — and the derivation that replaces the fit

The rational coefficients need genuinely new letters. Writing
`S_{r,m}(a) = sum_{t=1}^{a} H^(m)_t / t^r` and
`U_{r,m}(a,b) = sum_{t=1}^{a} H^(m)_{t+b} / t^r`, section 8's finite formula gives
directly, with `A = a+1`, `d = b+1`:

```
[1] Z_m(N)            = -H^(m)_{N-1}
[1] Z_i(A) Z_j(A+d-1) = H^(i)_a H^(j)_{a+b}
[1] S_{r,m}(A,d)      = (-1)^r sum_{j=1}^{m} C(r+m-j-1, m-j) S_{r+m-j, j}(b)
                        + U_{r,m}(a,b)
```

and hence

```
[1] F^{p,q}_{a,b} = (-1)^(p+q-1) sum_{i=0}^{p} C(p,i) i! (p-i+q-1)! [1]S_{i+1,p-i+q}(A,d)
                  + (-1)^(p+q)   sum_{i=0}^{p-1} C(p-1,i)(i+1)!(p+q-2-i)!
                                 H^(i+2)_a H^(p+q-1-i)_{a+b}

[1] I^{p,q}_{k,l} = (-1)^(p+q-2) ( [1]F^{p,q}_{k,l} + [1]F^{q,p}_{l,k} )
                    / ((p-1)!(q-1)!)
```

This is `work/z5ord0/ratpart.py`. **It is a derivation from §8, not a fit**, so
anything built on it inherits §8's `[DERIVED]` status rather than
`[VERIFIED range]`.

**The derivation, in full** (this is the step the coordinator flagged as the one
genuinely open conditional in T3 — it is closed):

*Rational part of `Z`.* §8 defines `Z_1(N) = -H_{N-1}` (purely rational) and
`Z_m(N) = zeta(m) - H^(m)_{N-1}` for `m >= 2`; in both cases
`[1] Z_m(N) = -H^(m)_{N-1}`. For a product,
`Z_i(A) Z_j(A+d-1) = zeta(i)zeta(j) - zeta(i)H^(j) - zeta(j)H^(i) + H^(i)H^(j)`,
and in the reduced basis `{1, z2, z3, z4, z5, z2z3}` none of `zeta(i)zeta(j)`
(`i+j <= 5`, using `z2^2 = 5z4/2`, `z2 z3 = z23`) or `zeta(i)H` is rational.
Hence `[1] Z_i(A)Z_j(A+d-1) = H^(i)_{A-1} H^(j)_{A+d-2} = H^(i)_a H^(j)_{a+b}`.

*Rational part of `S`.* For `m >= 2`, §8 gives
`S_{r,m}(A,d) = zeta(m,r) - sum_{h=1}^{d-1} U_{r,m}(h) - sum_{t=1}^{A-1} t^-r Z_m(t+d)`.
The MZV `zeta(m,r)` contributes nothing rational. §8's partial fractions give
`[1] U_{r,m}(h) = -b_1(h) H_h - sum_{j=2}^{m} b_j(h) H^(j)_h` with
`b_j(h) = (-1)^r C(r+m-j-1, m-j) / h^{r+m-j}`, so with `b = d-1`

```
[1] sum_{h=1}^{d-1} U_{r,m}(h)
   = -(-1)^r sum_{j=1}^{m} C(r+m-j-1,m-j) sum_{h=1}^{b} H^(j)_h / h^{r+m-j}
   = -(-1)^r sum_{j=1}^{m} C(r+m-j-1,m-j) S_{r+m-j, j}(b).
```

And `[1] sum_{t=1}^{A-1} t^-r Z_m(t+d) = -sum_{t=1}^{a} H^(m)_{t+b}/t^r
= -U_{r,m}(a,b)` with `a = A-1`. Combining gives the displayed formula.

For `m = 1`, §8's separate display is
`S_{r,1}(A,d) = -E_r - sum_{h=1}^{d-1}U_{r,1}(h) + sum_{t=1}^{A-1} H_{t+d-1}/t^r`;
`E_r` is a zeta value, `[1]U_{r,1}(h) = -b_1(h)H_h` with `b_1(h) = (-1)^r/h^r`,
and the last sum is `U_{r,1}(a,b)` verbatim — giving the **same** formula, so the
`m = 1` branch needs no special case. That uniformity is what makes the
implementation a one-liner and removes the usual place for an off-by-one.

The only external input is §8 itself (`[DERIVED]` in `Z5CF_BARNES.md`). The
implementation is confirmed against `universal.py` on 468 cells with 0 failures
(table below), spanning both inside and outside the fitted forms' check range.

Collected by hand for the top kernel:

```
[1] I^(2,2) = 6[S_{1,4}(k)+S_{1,4}(l)] + 2[S_{2,3}(k)+S_{2,3}(l)]
            - 6[U_{1,4}(k,l)+U_{1,4}(l,k)]
            - 4[U_{2,3}(k,l)+U_{2,3}(l,k)]
            - 2[U_{3,2}(k,l)+U_{3,2}(l,k)]
            + 2[ (H^(2)_k+H^(2)_l) H^(3)_{k+l} + (H^(3)_k+H^(3)_l) H^(2)_{k+l} ]
```

### 2.3 Cross-check, outside the fit's own range

| form | range | cells | failures |
|---|---|---|---|
| §8-**derived** `[1]I^{p,q}`, all four `(p,q)` | `0 <= k,l <= 8` | 324 | 0 |
| §8-**derived** `[1]I^{p,q}`, all four `(p,q)` | `8 <= k,l < 14` | 144 | 0 |
| Codex **fitted** `r11, r12, r21, r22` | `8 <= k,l < 14` | 144 | 0 |
| hand-collected `[1]I^(2,2)` above | `0 <= k,l <= 8` | 81 | 0 |

The fitted forms are confirmed outside their own check range. They differ
term-by-term from the §8-derived forms (e.g. the fitted `r22` carries
`-2H^(5)_k - 2H^(5)_l` and `+6U_{1,4}` where the derived form carries no `H^(5)`
and `-6U_{1,4}`); the two agree numerically everywhere tested, so they are equal
modulo the standard shuffle relations among `S`, `U` and harmonic products. **The
split into "Euler" and "product" parts is therefore basis-dependent** — which is
why §3 uses the *canonical* §8 split rather than either closed form.

---

## 3. Target 3 — the route-deciding fact `[MEASURED, exact ℚ]`

The coordinator's question was: *do the Euler-sum pieces cancel in the difference
against `w5sym`, or do they survive?*

Section 8's formula splits `[1] F^{p,q}` **canonically** — the `S_{r,m}(A,d)` sums
contribute the entire `S`+`U` content and the `Z*Z` terms contribute pure products
of ordinary harmonic numbers. No fitting is involved in the split. Under that
split (`work/z5ord0/t_euler.py`):

```
kappa * sum_{k,l} T(n,k,l) * (EULER part of coeff_1(W_B))

 n=0   0
 n=1   565/2
 n=2   -8718115/384
 n=3   884973506611/466560
 n=4   -20647767943938451/139345920
 n=5   393760360314208916791/37324800000
 n=6   -5041691897878365758244943/7390310400000
```

and, split further into the univariate and bivariate halves:

| n | `S`-part (univariate Euler) | `U`-part (bivariate coupled) |
|---|---|---|
| 1 | `-328` | `1221/2` |
| 2 | `254901/8` | `-20953363/384` |
| 3 | `-17578939759/5832` | `763762895777/155520` |
| 4 | `63996291296965/248832` | `-18828563690079617/46448640` |
| 5 | `-228465128813892513487/11664000000` | `1874747954197774933249/62208000000` |
| 6 | `31188697680187245223249/23328000000` | `-74611356614808425224851131/36951552000000` |

**ANSWER: they survive.** Neither half vanishes, nor does their sum. Target 3 is
**not** reducible to a pure rational-product identity by discarding the Euler
content, so the shape that closed ζ(4), T1 and T2 does not extend as-is.

Two further structural obstructions to the direct analogue, both established
in §1.1:

* `g_l` has **only double zeros** — `g_l''(j) != 0` for every `j`. A weight-5
  analogue of §7.3 would pair `H^(5)`/`H^(4)` differences against `g_l'''` and
  `g_l''`, and there is no triple zero to kill them.
* `q_l` vanishes on the full range `1 <= j <= n` (see §3.1 — this is *better*
  than what T2 used) but only to **order one**: `q_l'(j) != 0`. So the
  `q`-collapse used for the first half of T2 gives no second-order analogue.

What *does* transfer (verified, `t_target3.py` scaffolding): by `sum_k B_kl = 0`
and `sum_k D_kl = 0`, every additive piece of `[1]I^{1,2}` depending on `l` alone,
and of `[1]I^{1,1}` depending on `k` alone or `l` alone, drops out of the weighted
sum. That is a real but partial simplification; the `U_{r,m}(k,l)` terms, which
couple both indices, are untouched by it.

### 3.1 The three vanishing facts, with SHARP index ranges `[VERIFIED exact ℚ, n = 0..12]`

`work/z5ord0/t_sharp.py`. Each fact is checked *and* a witness is produced just
outside its range, so the boundary is known rather than assumed. `q_l(x)` is the
simple-`y` coefficient `d/dy[(y+l)^2 R_n]|_{y=-l} = g_l(x) Lambda_l(x)`, with
partial fractions `sum_k [C_kl/(x+k)^2 + D_kl/(x+k)]`.

Zero bookkeeping (`0 <= l <= n`): `P1 = prod_{r=1}^n (x-r)` vanishes exactly on
`{1..n}`; `P2 = prod_{r=1}^n (x-l-r)` exactly on `{l+1,...,l+n}`. Because `l <= n`
the union is exactly `{1,...,n+l}` and the intersection exactly `{l+1,...,n}`
(empty at `l = n`). `Lambda_l` has simple poles, each of residue `1`, exactly at
`x = l+1,...,l+n`.

| fact | holds EXACTLY on | fails just outside | cells | failures |
|---|---|---|---|---|
| `q_l == g_l * Lambda_l` (generic `x`) | — | — | 364 | 0 |
| **(V1)** `g_l(j) = 0` | `1 <= j <= n+l` | `g_l(n+l+1) != 0` | 1092 + 91 | 0 |
| **(V2)** `g_l'(j) = 0` | `l < j <= n` (double-zero overlap) | `!= 0` on `1<=j<=l` **and** on `n<j<=n+l` | 364 + 728 | 0 |
| **(V3)** `q_l(j) = 0` | **`1 <= j <= n`** (the whole first-factor range) | `!= 0` on `n < j <= n+l` | 728 + 364 | 0 |

**Sharp-edge witnesses, exact over ℚ** (the last zero, then the first nonzero):

| `(n,l)` | `q_l(n+1)` — edge of (V3) | `g_l(n+l+1)` — edge of (V1) | `g_l'(l)` — lower edge of (V2) | `g_l'(n+1)` — upper edge of (V2) |
|---|---|---|---|---|
| `(6,3)` | `1/185513328` | `1/1635920` | `-1/81648` | `1/185513328` |
| `(7,2)` | `1/35335872000` | `-567/189112352000` | `-1/69120` | `1/35335872000` |
| `(9,5)` | `-7/42966855360000` | `-57967/127157854464000` | `1/720720000` | `-7/42966855360000` |
| `(11,4)` | `1/93311485394190336` | `-77/659186317541376` | `-1/10567065600` | `1/93311485394190336` |

For contrast, at `(6,3)`: `q_l(6) = 0`, `g_l(9) = 0`, `g_l'(4) = g_l'(6) = 0`.
Every edge is nonzero at every `(n,l)` tested, and the systematic sweep over
`n = 0..12`, all `l`, found 0 exceptions in 1183 edge cells. `P(n+1) = n! != 0`
is exactly why (V3) stops at `j = n+1`, as the division-free argument predicts.

**(V3) is confirmed in the stronger form**, and the mechanism is exactly the log
pole: on `1 <= j <= l` the factor `g_l` has a simple zero and `Lambda_l(j)` is
finite; on `l < j <= n` the factor `g_l` has a *double* zero while `Lambda_l` has
a simple pole at `x = l + (j-l)` — the diagonal log pole — so the product still
vanishes, to order one. My earlier statement in §1 (`q_l(j) = 0` only for
`1 <= j <= l`) was correct but **understated**; the true range is the full
`1 <= j <= n`, and that extra leverage is now available to the T3 argument.

**The (V3) zero is exactly order one.** `q_l'(j) != 0` for every `1 <= j <= n`,
checked exactly for `n = 1..8`, all `l`, 0 exceptions in 240 cells; witnesses at
`n=6, l=3`: `q_l'(3) = 8683/205752960`, `q_l'(5) = -1/102910500`. So there is no
second-order `q`-collapse to mirror the `g -> g'` step that closed T2.

One further exact relation falls out of the same bookkeeping and is confirmed by
the witnesses:

```
q_l(j) = g_l'(j)   for  n < j <= n+l
```

because there `g_l` has a simple zero and `Lambda_l` a simple pole of residue 1,
so `lim g_l(x) Lambda_l(x) = g_l'(j)`. Numerically `q_l(7) = g_l'(7) = 1/185513328`
at `n=6, l=3`. This ties the two families together on the one range where both
are nonzero, and may be what lets the `U`-sums be re-expressed.

### 3.2 The combined nested contribution — one term of it is identically zero

Target 3 is `sum_{k,l}[A r22 + 2B r12 + D r11 + 2A w5sym] = 0` (using
`C_kl = B_lk`, `r21(k,l) = r12(l,k)`, `D` symmetric). Reading the Euler/coupled
content off the fitted `r`-forms and folding with the `k<->l` symmetry of `A` and
`D` gives the nested part

```
N = 12 sum A (U_{1,4}(k,l) - S_{1,4}(k))
  +  4 sum A (U_{2,3}(k,l) - S_{2,3}(k))
  +  4 sum B S_{1,3}(l)
  -  2 sum B U_{2,2}(k,l)
  +  2 sum D U_{1,2}(k,l)
```

which reproduces the coordinator's collected expression exactly. Evaluated term
by term (`work/z5ord0/t_nested.py`, exact ℚ):

| n | `12 sA(U14-S14)` | `4 sA(U23-S23)` | `4 sB S13(l)` | `-2 sB U22` | `2 sD U12` | `N` |
|---|---|---|---|---|---|---|
| 1 | `-9` | `-6` | **`0`** | `43` | `-15/2` | `41/2` |
| 2 | `77621/64` | `79861/96` | **`0`** | `-267173/192` | `52001/384` | `302825/384` |
| 3 | `-2995478503/25920` | `-3171068647/38880` | **`0`** | `14197917109/233280` | `-645490043/155520` | `-65512072729/466560` |
| 4 | `73337851755863/7741440` | `26451911537629/3870720` | **`0`** | `-202362368076469/69672960` | `7077425571323/46448640` | `1888857687521209/139345920` |
| 5 | — | — | **`0`** | — | — | `-197880553991455427513/186624000000` |
| 6 | — | — | **`0`** | — | — | `2664401353472324702006689/36951552000000` |

**`4 sum_{k,l} B_kl S_{1,3}(l) = 0` identically**, and for a trivial reason:
`S_{1,3}(l)` depends on `l` alone, so the inner sum is
`sum_l S_{1,3}(l) * (sum_k B_kl) = 0` by §7.1. The combined expression therefore
has **four** surviving terms, not five. More generally: *every additive piece of
`r12` depending on `l` alone, and of `r11` depending on `k` alone or `l` alone,
drops out of the weighted sum.* The `U_{r,m}(k,l)` terms, which couple both
indices, are exactly what survives — and `N != 0`, so they must be balanced
against the product/compact contribution rather than among themselves.

**Recommendation.** The new ingredient target 3 needs is a summation rule for
`sum_{k,l} A_kl U_{r,m}(k,l)` and `sum_{k,l} B_kl U_{r,m}(k,l)`. Abel summation in
`t` turns these into `sum_t (H^(m)_{t+l}/t^r) * (tail sum of A or B over k >= t)`,
and for `B` the tail equals minus the head because `sum_k B_kl = 0`. That is the
natural next handle and is where I would spend the next block of effort.

---

## 4. Order-zero certificates — status, with bounds

### 4.1 Setup

```
T w = Delta_k R + Delta_l S ,  R = T rho , S = T sigma
  <=>  w = gk rho(n,k+1,l) - rho(n,k,l) + gl sigma(n,k,l+1) - sigma(n,k,l)   (*)
  gk = T(n,k+1,l)/T(n,k,l) = (n+k+1)(n-k)^2(n+k+l+1) / [(k+1)^3 (k+l+1)]
```
`rho, sigma` in `Q(n,k,l) (x) <harmonic monomials>`. `sigma := tau(rho)` is WLOG
for every target (all are `k<->l` symmetric; if `(rho,sigma)` works so does
`(tau sigma, tau rho)`, and the average has `sigma = tau rho` and still satisfies
the boundary conditions). Code: `o0core.py`, `joint0.py`.

### 4.2 Boundary conditions — both audited

**Bottom (grouped, NOT blockwise).** At `k = 0` the alphabet collapses:
`h*_k -> 0`, `h*_pk -> h*_n`, `h*_mk -> h*_n`, `h*_kl -> h*_l`, `h*_pkl -> h*_pl`.
So the condition is `sum_{m in class c} rho_m(n,0,l) = 0` per collapse class, not
`rho_m(n,0,l) = 0` per block. Implemented as extra rows in `joint0.System.build`
(`spec_k0`, `groups`), with `force_k = 0`. **Per-block forcing is not merely
stronger — it annihilates almost all of the gauge**: a kernel element
`rho0 = gl v(k,l+1) - v(k,l)` satisfies `rho0(0,l) = 0` only if `v(0,·)` solves a
first-order recurrence, which has no polynomial solution in general. The
`sigma|_{l=0} = 0` mirror is automatic under `sigma = tau(rho)`.
Cross-checked against `work/z5star/cert4.py`, which encodes the same grouping.

**Top (separate audit).** `T(n,n+1,l) = 0` and `T(n,k,n+1) = 0` identically, from
the `C(n,k)^2` factor, so there is no top-boundary equation — only a *regularity*
requirement. The sole pole of `rho(n,k+1,l)` at `k = n` is the `-1/(n-k)^r`
increment of the letters `H^(r)_{n-k}`; `gk` carries `(n-k)^2`, so
`gk * rho(k+1,l) -> 0` provided every monomial of `rho` has `H_{n-k}`-weight
`<= 1`. That is imposed as `mk_cap = 1`.
**This is an ansatz restriction and is flagged as such**: relaxing it requires the
explicit linear condition *"the coefficient of `(n-k)^{-2}` in `rho(k+1,l)`
vanishes"*, which is not implemented. Separately, every denominator family used is
built only from `(k+1),(k+2),(l+1),(l+2),(k+l+1..3),(n+k+1),(n+k+2),(n+l+1),
(n+l+2),(n+k+l+1),(n+1-k),(n+1-l)`, none of which vanishes on `0 <= k,l <= n` or
at the shifted arguments.

### 4.3 Plumbing control `[PASS]`

`t_control.py` plants a random `rho*` in the ansatz, computes
`b = Op(rho*, tau rho*)` at the sample points, and feeds it back:
`n=7, J=43, nc=36, cols=1548, rows=8600, rank=1502, residual = 0`. The shift
matrices, the `tau` pairing, `gk/gl` and the block layout are correct.

### 4.4 TEST A — the constant weight is not an order-zero double difference

Every target `w` has top-degree monomials with nonzero *constant* coefficients
(e.g. `2 h1_pk h1_pl` inside `2 L_k L_l`). If `rho` is confined to the divisor
closure of `supp(w)`, the top-degree blocks are *exactly*

```
c = gk rho(k+1,l) - rho(k,l) + gl sigma(k,l+1) - sigma(k,l),   c in Q
```

i.e. `T` itself must be an order-zero double difference. `t_q0.py`, `n = 6`:

| family | denominator | deg | cols | rows | rank | residual |
|---|---|---|---|---|---|---|
| empty | `1` | 10 | 242 | 544 | 193 | 351 |
| kl1 | `k+l+1` | 10 | 242 | 544 | 193 | 351 |
| E1 | `(k+1)(l+1)(k+l+1)(k+l+2)(n+k+1)(n+l+1)` | 10 | 242 | 544 | 206 | 338 |
| E2 | same, all exponents 2 | 10 | 242 | 544 | 226 | 318 |
| E4 | E1 · `(n-k)(n-l)` | 10 | 242 | 544 | 217 | 327 |
| E5 | `(k+1)^3(l+1)^3(k+l+1)^2(k+l+2)(n+k+1)^2(n+l+1)^2(n+k+l+1)(n-k)^2(n-l)^2` | 10 | 242 | 544 | 241 | 303 |

**Never 0.** This is consistent with an elementary fact: in the `k`-only
direction the same block demands Gosper-summability of `T`, and

```
sum_{k=0}^{n} T(n,k,0) = 1, 5, 73, 1445, ...  = the APERY numbers A_n,
```

which are not a rational function of `n`. So `T` is not Gosper-summable in `k`,
and Test A says the two-variable version fails too.

**Consequence, and it is structural, not a tuning issue:** any order-zero
certificate for these targets *must* inflate `rho` above `deg(w)`, using
trivial-pair gauge blocks
`rho0 = gl v(k,l+1) - v(k,l)`, `sigma0 = -(gk v(k+1,l) - v(k,l))`
whose corrections feed the top blocks a non-constant right-hand side. A denominator
without `(k+1)^3` / `(l+1)^3` carries **no gauge at all** and inflation is a no-op
(measured in `t_control.py`).

### 4.5 The ζ(4) calibration `[does NOT pass]`

`w = L_k + L_l`, the identity proved uniformly in §7.1 — the mandated
known-answer control. Grouped bottom boundary, `force_k = 0`, `mk_cap = 1`,
`n = 7`, `p = 4194301`. `maxdeg = 1` is the uninflated ansatz (must fail, and
does); `maxdeg = 2` is one-step inflation.

| run | blocks | nc | cols | rows | ratio | rank | gauge nullity | residual |
|---|---|---|---|---|---|---|---|---|
| md1/F1/d4 | 9 | 25 | 225 | 675+60 | 3.27 | 225 | 0 | 510 |
| md1/F3/d6 | 9 | 49 | 441 | 1323+80 | 3.18 | 441 | 0 | 962 |
| md1/F4/d6 | 9 | 49 | 441 | 1323+80 | 3.18 | 441 | 0 | 962 |
| md2/F1/d4 | 43 | 25 | 1075 | 3225+168 | 3.16 | 1075 | 0 | 548 |
| md2/F1/d6 | 43 | 49 | 2107 | 6321+224 | 3.11 | 2012 | 95 | 991 |
| md2/F2/d4 | 43 | 25 | 1075 | 3225+168 | 3.16 | 1075 | 0 | 510 |
| **md2/F2/d8** | **43** | **81** | **3483** | **10449+280** | **3.08** | **3253** | **230** | **1595** |

Denominators: `F1 = (k+1)^3(l+1)^3(k+l+1)`;
`F2 = F1·(k+l+1)(k+l+2)`;
`F3 = F2·(n+k+1)(n+l+1)(n+k+l+1)`;
`F4 = (k+1)^3(k+2)(l+1)^3(l+2)(k+l+1)^2(k+l+2)^2(n+k+1)^2(n+l+1)^2(n+k+l+1)(n+1-k)(n+1-l)`.
All rows/cols ratios are `>= 3.0` raw, `>= 1.5` after discounting the `tau`
redundancy — above the `1.3` floor of discipline 3.

**The calibration does not pass, therefore no `[EXCLUDED]` verdict is issued for
any target.** What has been established is narrower and should be read as exactly
that:

* `[EXCLUDED with bounds]` — an order-zero certificate confined to the divisor
  closure of `supp(w)` (no inflation) does not exist, for **any** weight with a
  nonzero constant top coefficient. Bound: Test A above, plus the Apéry-number
  argument, which is uniform in the ansatz and therefore not a size question.
* **Open** — one-step inflation (`maxdeg = deg(w)+1`) up to numerator bidegree
  `(8,8)`, 43 blocks, 230-dimensional gauge, five denominator families. Not
  reached: two-step inflation, and numerator bidegree beyond `(10,10)`. Memory
  (15 GB shared with three concurrent agents) is the binding constraint on the
  joint solve; `maxdeg = 3` for this weight is `J = 147` blocks and needs
  ~1.5 GB at `nc = 36`.

### 4.6 The cheap way to settle it (built, not yet run to depth)

`work/z5ord0/t_deep.py` implements the sharp necessary condition. For a fixed
top-degree monomial `m0` of `w`, the equations indexed by
`{ mu : mu contains m0 }` form a **closed** sub-system of the full joint system
(the coefficient of `mu` only ever involves `rho_nu` for `nu ⊇ mu ⊇ m0`), with
right-hand side `c` at `m0` and `0` above it, and **no boundary condition touches
it** — so dropping the boundary only relaxes. Inconsistency there implies
inconsistency of the whole system, at any inflation depth, and it costs
`(#blocks above m0) x npts` rows instead of `J x npts`. At depth 3 over the
8 weight-1 letters that is 165 blocks rather than the full basis, and it isolates
exactly the obstruction Test A exposes. This is the recommended next run.

---

## 5. Deliverables that do not apply

No certificate was found, so there is nothing to lift to `ℤ[n,k,l]`; the
sparse-`List ((exponent triple) x ℤ)` emission, monomial counts and coefficient
bit-lengths are moot. Target 2 needs no certificate at all — its proof is
structural and formalises without a reflective polynomial checker, which is the
outcome the programme wanted.

## 6. Files

```
work/z5ord0/
  o0core.py      letters, increments, k=0 collapse, module algebra, gk/gl, ansatz
  joint0.py      joint order-0 solver, grouped bottom boundary, mk_cap top audit
  weights.py     L_k, L_l, the target weight elements, compact w3sym/w5sym
  evalq.py       exact rational evaluation of module elements and T-weighted sums
  alpha.py       H, S_{r,m}, U_{r,m} and the exact-Q alphabet fitter
  ratpart.py     [1] I^{p,q} DERIVED from section 8   <-- key artefact
  w_check.py     section-7 coefficient table check; target sums
  t_q0.py        TEST A (constant weight)
  t_control.py   plumbing control + gauge (kernel) dimension measurement
  t_cal.py       the zeta(4) calibration sweep         (logs cal2_n7.log, cal3_n7.log)
  t_deep.py      closed sub-system above one top monomial, unlimited depth
  t_alpha.py     alphabet measurement
  t_struct.py    first-half structural reduction of target 2 (fed section 7.3)
  t_verify2.py   step-by-step verification of the target-2 proof
  t_verify2b.py  the SENSITIVE (both-sides-nonzero) verification
  t_euler.py     cross-check of derived vs fitted forms; the Euler-survival test
  t_target3.py   target-3 triage scaffolding
  t_sharp.py     SHARP index ranges for g_l, g_l', q_l + edge witnesses
  t_nested.py    the combined nested (Euler/coupled) contribution, term by term
```
