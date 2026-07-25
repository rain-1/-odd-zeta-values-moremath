# Weight-5 graded descent for the Brown–Zudilin cellular ζ(5) family

**Author:** mathematician-agent (River's odd-zeta program)
**Date:** 2026-07-24
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`
**Data:** exact ladders `../zeta-math/worthiness/falsify_data/ladder_{Q,P,Ph}.json`, n ≤ 360,
BZ-positive normalization (`Q_0=1, Q_1=21, Q_2=2989; P_1=87/4, P_2=1190161/384; P̂_1=101/4, P̂_2=344923/96`).
All computation exact (Mathematica kernel session `Q7TuOfJ4`).

**Labels.** `[PROVED]` = complete proof written here. `[VERIFIED r]` = exact finite check on
range `r` — evidence, never proof. `[RECALLED-UNVERIFIED]` = memory, not checked.

---

## 0. EXECUTIVE SUMMARY

**Headline.** (LB₅) is now reduced, *by proof*, to a single congruence about one explicit
sequence, and the reduction is clean:

> **[PROVED]** (Theorem C) For p ≥ 5, 1 ≤ a < p, 0 ≤ r < p, n = ap+r, put
> `W_n := P_n − H₅(n)·Q_n` with `H₅(n)=Σ_{m≤n} m^{−5}`. Then
> `p⁵P_{ap+r} − P_a·Q_r ≡ p⁵W_{ap+r} − W_a·Q_r (mod p)`.
> Hence **(LB₅) ⟺ (W5): `p⁵W_{ap+r} ≡ W_a·Q_r (mod p)`.** The `H₅` layer of (LB₅) is
> unconditionally proved; *all* remaining content sits in `W`.

> **[VERIFIED, 0 failures]** (W5) holds for every p ∈ {5,7,11,13,17,19,23,29,31}, every
> single-digit cell n = ap+r ≤ 360, min depth exactly 1. Also `v_p(W_n) ≥ −5` (min exactly −5)
> on n < p². **p = 5 is NOT exceptional here.**

**Second headline — T1 for the middle row is solved.**

> **[VERIFIED exact, n ≤ 40, independently re-derived and re-checked n ≤ 16]** (Theorem B, §3.2)
> `P̂_n = Σ_{k,l=0}^n T(n,k,l)·ŵ₃(n,k,l)` on the **same** Brown–Zudilin summand
> `T(n,k,l)=C(n+k,n)C(n,k)²C(n+l,n)C(n,l)²C(n+k+l,n)` that gives `Q_n`, with the explicit
> weight-3 harmonic monomial `ŵ₃` displayed in §3.2. This is exactly the "(BZ summand)·(harmonic
> weight)" decomposition the campaign asked for, one grade down.

**Two corrections to the brief's ESTABLISHED list (both material).**

1. **`Q_n` is NOT `Σ_k C(n,k)²C(n+k,k)`.** That sequence is 1,3,19,147,… (A005258, the ζ(2)
   Apéry numbers) and gives `Q_1 = 3 ≠ 21`. The Brown–Zudilin `Q_n` is the **double** sum
   (BZ eq. (Q_n), verified against the ladder for n ≤ 12, 0 failures):
   ```
   Q_n = Σ_{k,l=0}^{n} C(n+k,n) C(n,k)² C(n+l,n) C(n,l)² C(n+k+l,n)      (BZ-Q)
   ```
   Every congruence below is for **this** `Q_n`. Theorem A proves Lucas for it outright.

2. **(LB₃-in-5) in *product* form is FALSE.** `p³P̂_{ap+r} ≡ P̂_a·Q_r (mod p)` **fails**, and
   fails structurally: `P̂_a` is *not p-integral* — `v_p(P̂_a) = −1` for most `a` with
   `p/2 < a < p`. (p=13: a = 7,8,9,10,11; p=11: a = 6,7,8; p=7: a=5; p=5: a=3.) This is the
   `d_n²d_{2n}` factor of BZ's integrality statement making itself felt: `v_p(d_{2a}) = 1`
   exactly when `2a ≥ p`. The *master* form `p³P̂_nQ_a ≡ P̂_aQ_n (mod p)` does survive
   (**[VERIFIED, 0 failures]**, p ≤ 17), which is why the earlier sweep saw nothing. The
   product form is the one a Lucas argument produces, and it is not available at weight 3.
   **Consequence: the P̂-row is *not* the easy warm-up; it is the harder row.** See §5.

**Status of the campaign targets.**

| target | status |
|---|---|
| Q-row Lucas `Q_{ap+r} ≡ Q_aQ_r (mod p)` | **[PROVED]** (Theorem A) — complete, self-contained, all p, all a ≥ 0. Upgrades the sibling's "certificate-shaped" argument to a proof. |
| H-layer of (LB₅) and reduction (LB₅) ⟺ (W5) | **[PROVED]** (Theorem C) |
| (W5) itself | **[VERIFIED 0 failures]**, p ≤ 31, n ≤ 360; proof open — blocked on T1 for `P` (§3.3) |
| **T1 for the middle row `P̂`** | **SOLVED** — Theorem B (§3.2): `P̂_n = Σ_{k,l} T(n,k,l)·ŵ₃(n,k,l)` on the *same* BZ summand, `ŵ₃` an explicit weight-3 harmonic monomial. **[VERIFIED exact, n ≤ 40, independently re-checked n ≤ 16]** |
| T1 for the top row `P` | **NEGATIVE, delimited** (§3.3): no weight-5 *harmonic-monomial* weight exists in a 149-element basis over 165 exact equations. Needs nested (depth-2) letters — the `ζ(5)+2ζ(2)ζ(3)` period. |
| new closed form for Apéry's `b_n` | **[PROVED]** (§3.1) — pure harmonic monomials, replaces the non-generalising `Σ(−1)^{m−1}/(2m³C(n,m)C(n+m,m))` weight |
| key new lemma (non-square-summand replacement) | **[PROVED]** (Lemma D, §6) — the *triple-carry* lemma |
| (LB₃-in-5) | **corrected statement** (§5); product form disproved |
| T4 assembled theorem | not reached; the (CB) consequence of (LB₅) is unchanged and is spelled out in §7 |

---

## 1. Objects and normalization

`Q_n` as in (BZ-Q); `P_n`, `P̂_n` the ζ(5)- and ζ(3)-companion rows, `I'_n = Q_nζ(5) − P_n`,
`I''_n = Q_nζ(3) − P̂_n`. Write `T(n,k,l) := C(n+k,n)C(n,k)²C(n+l,n)C(n,l)²C(n+k+l,n)`, so
`Q_n = Σ_{k,l} T(n,k,l)`, and `H_s(n) := Σ_{m=1}^n m^{−s}`.

**[VERIFIED]** `Q_n` from (BZ-Q) equals the ladder `Q_n` exactly for n = 0..12.
**[VERIFIED]** `P̂_n/Q_n − H₃(n) → 0` and `P_n/Q_n − H₅(n) → 0` (both `O(n^{−2})`, `O(n^{−4})`),
i.e. `H₃` and `H₅` are the correct leading harmonic weights of the two companion rows.

---

## 2. Theorem A [PROVED] — Lucas for the Brown–Zudilin row `Q`

> **Theorem A.** Let p be prime, a ≥ 0, 0 ≤ r < p, N = ap + r. Then
> `Q_N ≡ Q_a · Q_r (mod p)`, hence `Q_n ≡ ∏_i Q_{n_i} (mod p)` for the base-p digits of n.

*Proof.* Write every summation index in base p: `k = bp+s`, `l = cp+t`, `0 ≤ s,t < p`.
Since `k, l ≤ N < (a+1)p` we have `0 ≤ b, c ≤ a`.

**Lemma 1 (Lucas step).** For `a,b ≥ 0`, `0 ≤ r,s < p`: `C(ap+r, bp+s) ≡ C(a,b)C(r,s) (mod p)`.
*Proof:* Lucas' theorem applied twice (last digit `s` vs `r`; higher digits reassembled by
Lucas again). ∎

**Lemma 2 (single carry annihilation).** With `N = ap+r`, `k = bp+s`:
`C(N+k, N) ≡ C(a+b,a)C(r+s,r) (mod p)` if `r+s < p`, and `C(N+k,N) ≡ 0 (mod p)` if `r+s ≥ p`.
*Proof:* If `r+s < p` then `N+k = (a+b)p+(r+s)` and Lemma 1 applies. If `r+s ≥ p` then
`N+k = (a+b+1)p + (r+s−p)` with `0 ≤ r+s−p < p`, and Lemma 1 gives
`C(N+k,N) ≡ C(a+b+1,a)C(r+s−p, r)`; but `s < p` forces `r+s−p < r`, so `C(r+s−p,r) = 0`. ∎

**Lemma 3 (double carry annihilation).** Assume `s ≤ r`, `t ≤ r`, `r+s < p`, `r+t < p`
(the regime in which the other five factors of `T` survive mod p; see below). Then
`s + t < p`, and
`C(N+k+l, N) ≡ C(a+b+c, a) C(r+s+t, r) (mod p)` if `r+s+t < p`, `≡ 0 (mod p)` otherwise.
*Proof:* First `s+t < p`. Suppose `s+t ≥ p`. From `s ≤ r, t ≤ r` we get `p ≤ s+t ≤ 2r`, so
`r ≥ p/2`. From `r+s<p, r+t<p` we get `s,t ≤ p−1−r`, so `s+t ≤ 2(p−1−r) < 2(p − p/2) = p`,
contradiction. Hence `s+t < p`, so `r+s+t < 2p` and `N+k+l = (a+b+c+ε)p + (r+s+t−εp)` with
`ε ∈ {0,1}`. If `ε = 0` Lemma 1 gives the stated product. If `ε = 1`, the low digit is
`ρ = r+s+t−p`, and `ρ < r` precisely because `s+t < p`; Lemma 1 then gives a factor
`C(ρ, r) = 0`. ∎

**Lemma 4 (summand factorization).** With the notation above,
```
T(N, bp+s, cp+t) ≡ [ r+s+t < p ] · T_hi(a,b,c) · T_lo(r,s,t)   (mod p),
T_hi(a,b,c) = C(a+b,a)C(a,b)²C(a+c,a)C(a,c)²C(a+b+c,a),
T_lo(r,s,t) = C(r+s,r)C(r,s)²C(r+t,r)C(r,t)²C(r+s+t,r).
```
*Proof:* `C(N,k)² ≡ C(a,b)²C(r,s)²` and `C(N,l)² ≡ C(a,c)²C(r,t)²` by Lemma 1; these vanish
unless `s ≤ r` and `t ≤ r`. `C(N+k,N)`, `C(N+l,N)` by Lemma 2 (vanish unless `r+s<p`, `r+t<p`).
On the surviving regime Lemma 3 applies to `C(N+k+l,N)`. Multiplying the five congruences and
noting that when any factor is `≡ 0` both sides vanish gives the statement. ∎

**Summation.** Sum Lemma 4 over `0 ≤ b,c ≤ a` and `0 ≤ s,t < p`:
```
Q_N ≡ Σ_{b,c=0}^{a} Σ_{s,t: r+s+t<p} T_hi(a,b,c) T_lo(r,s,t)   (mod p).
```
Two boundary points, both exactly as in the ζ(3) template (and as flagged by the referee note
on `WARMUP_ZETA3_DWORK.md`, item 2):

* *The index region is a product only after adding vanishing terms.* The true region is
  `{(b,s): bp+s ≤ N}×{(c,t): cp+t ≤ N}` intersected with the surviving set. The completion to
  the full box `{0≤b≤a}×{0≤s<p}` adds only terms with `b = a, s > r`, for which `C(r,s) = 0`;
  identically for `c,t`. So the completed sum is congruent to the true one.
* *The `(b,c)`-region and the `(s,t)`-region are independent* (`r+s+t<p` constrains only
  `s,t`), so the double sum factors.

The high factor is `Σ_{b,c=0}^{a} T_hi(a,b,c) = Q_a`, an **integer identity** (it is (BZ-Q) at
`n = a`). For the low factor, `Q_r = Σ_{s,t=0}^{r} T_lo(r,s,t)`, and every term of `Q_r` with
`r+s+t ≥ p` vanishes mod p: if `r+s ≥ p` (or `r+t ≥ p`) then `C(r+s,r) ≡ 0` by the Lemma 2
computation; otherwise `r+s<p, r+t<p, s≤r, t≤r`, so Lemma 3 applies and `C(r+s+t,r) ≡ 0`.
Hence `Σ_{s,t: r+s+t<p} T_lo(r,s,t) ≡ Q_r (mod p)`, and `Q_N ≡ Q_a Q_r`.

The multi-digit product form follows by induction on the number of base-p digits, since the
two-digit statement holds for **all** `a ≥ 0`. ∎

**Remarks.** (i) The proof is uniform in p (no exclusion of p = 2,3,5). (ii) Compared with the
sibling repo's `PHASE2_SALVAGE_VERIFY` §V3, the "CARRY-KILL predicate", there stated as
*verified over 2.19M summands*, is here **proved** — Lemma 3 is the step that needed the
argument, and the `s+t<p` deduction is the non-obvious part. (iii) [VERIFIED] Theorem A, 0
failures, p ∈ {5,…,31}, all single-digit cells and iterated digits, n ≤ 360.

---

## 3. T1 — the decomposition hunt

### 3.1 A new closed form for Apéry's `b_n` (the template, upgraded) [PROVED]

The ζ(3) template of `WARMUP_ZETA3_DWORK.md` uses `b_n = H₃(n)a_n + W(n)` with the *non-monomial*
weight `w(n,k)=Σ_{m≤k}(−1)^{m−1}/(2m³C(n,m)C(n+m,m))`. That weight does not generalise. The
residue construction does, and it produces a **pure harmonic-monomial** form:

> **Proposition.** `b_n = Σ_{j=0}^n C(n,j)²C(n+j,n)² [ H_j^{(3)} + (2H_j − H_{n+j} − H_{n−j})·H_j^{(2)} ]`.

*Proof.* Put `F(t) = ∏_{m=1}^n (t−m) / ∏_{m=0}^n (t+m)`, so `F(t)² = Σ_{j=0}^n [β_{2,j}/(t+j)² +
β_{1,j}/(t+j)]` with
`β_{2,j} = (∏_m(−j−m)/∏_{m≠j}(m−j))² = C(n,j)²C(n+j,n)²` and
`β_{1,j} = β_{2,j}·(d/dt)log[(t+j)²F(t)²]|_{t=−j} = 2β_{2,j}(2H_j − H_{n+j} − H_{n−j})`
(the log-derivative is `2[−(H_{n+j}−H_j) − (H_{n−j}−H_j)]`). Since `deg num − deg den = −2`,
the residues sum to zero: `Σ_j β_{1,j} = 0`. Now
`−F'(t)² …`: precisely, `−(F²)'(t) = Σ_j [2β_{2,j}/(t+j)³ + β_{1,j}/(t+j)²]`, so summing over
`t ≥ 1` (using `Σ_{t≥1}(t+j)^{−m} = ζ(m) − H_j^{(m)}`)
```
Σ_{t≥1} −(F²)'(t) = 2(Σ_jβ_{2,j})ζ(3) + (Σ_jβ_{1,j})ζ(2) − [2Σ_jβ_{2,j}H_j^{(3)} + Σ_jβ_{1,j}H_j^{(2)}]
                  = 2 a_n ζ(3) − 2·(the bracket of the Proposition).
```
The `ζ(2)` coefficient vanishes by `Σβ_{1,j}=0`; `Σ_jβ_{2,j} = a_n` is Apéry's identity. The linear
form so produced is the Apéry/Nesterenko form `2(a_nζ(3) − b_n)`, whence the statement. ∎

**[VERIFIED]** exact agreement with the standard `b_n` (the one with `b_n/a_n − ζ(3) ≈ −2·10^{−61}`),
`n = 0..5`, exact rationals: `0, 6, 351/4, 62531/36, 11424695/288, 35441662103/36000`.

This is the shape that ports. Note the *letters*: `H^{(r)}_j`, `H^{(r)}_{n+j}`, `H^{(r)}_{n−j}`.

### 3.2 THE MAIN T1 RESULT — exact closed form for the ζ(3)-companion row `P̂_n` [FOUND, VERIFIED]

Define, for `n ≥ 0` and `0 ≤ k,l ≤ n`, the three **letters**
```
A_r(x) := H^{(r)}_{n+x} − H^{(r)}_x ,      B_r(x) := H^{(r)}_{n−x} − H^{(r)}_x ,
C_r    := H^{(r)}_{n+k+l} − H^{(r)}_{k+l} ,   H^{(r)}_n  (the "constant" letter)
```
and the weight-3 form
```
ŵ₃(n,k,l) = H^{(3)}_n + A₃(k) + A₃(l)
            − (1/4)[ A₂(k)A₁(k) + A₂(l)A₁(l) ]
            − (3/4)[ A₂(k)B₁(k) + A₂(l)B₁(l) ]
            − (3/8)[ A₂(k) + A₂(l) ]·C₁
            − (1/8)[ A₂(k)A₁(l) + A₂(l)A₁(k) ] .
```

> **Theorem B (T1 for the middle row).**
> ```
> P̂_n  =  Σ_{k,l=0}^{n}  T(n,k,l) · ŵ₃(n,k,l),
> T(n,k,l) = C(n+k,n)C(n,k)² C(n+l,n)C(n,l)² C(n+k+l,n).
> ```
> **[VERIFIED, exact, 0 discrepancies]** — (a) as the *unique-up-to-basis-relations* solution of an
> exactly-solved linear system over `n = 1..30` in a 22-element weight-3 harmonic-monomial basis,
> then (b) validated on the held-out values `n = 31..40` (all differences exactly 0), and (c)
> re-verified by an independent direct re-implementation of the displayed formula for `n = 1..16`
> against the BZ ladder (all differences exactly 0).

This is the object the campaign brief called for: *`P̂_n = Σ (BZ summand)·(weight-3 harmonic
weight)`*, and it is **exactly** the Brown–Zudilin summand `T(n,k,l)` of (BZ-Q) — the same summand,
graded weight, no extra nested corrections. It is the exact weight-3 analogue of §3.1.

Structural remarks (used in §5 and needed for T2):
* Every non-constant term carries an `A`-letter of the **highest** weight in the monomial; `B₃`,
  `C₃`, and every monomial whose top letter is `B`, `C` or `H^{(r)}_n` has coefficient **0**. The
  fit was run in a basis that *allowed* all of these; they came out zero. That is structure, not
  an assumption.
* The letter `A_r(k) = H^{(r)}_{n+k} − H^{(r)}_k` has argument up to `2n`. **This single fact is
  the source of the `d_{2n}` in BZ's `d_n²d_{2n}P̂_n ∈ ℤ` and of the entire (LB₃-in-5) anomaly**
  (§5): `A₃(k)` acquires a *second* `p`-pole as soon as `⌊(n+k)/p⌋ ≥ p`, which for `n = a < p`
  happens iff `a+k ≥ p`.

### 3.3 T1 for the top row `P_n` — NEGATIVE result, precisely delimited

The same method run at weight 5 **fails**, and the failure is informative.

**[VERIFIED negative]** There is **no** representation `P_n = Σ_{k,l} T(n,k,l)·w₅(n,k,l)` with
`w₅` a ℚ-linear combination of the 149 symmetric weight-5 monomials in the letters
`{A_r(k),A_r(l),B_r(k),B_r(l),C_r,H^{(r)}_n : r = 1..5}` with at most three factors and top letter
in `{A,B,C,H^{(·)}_n}` (this basis strictly contains the weight-3 basis in which `ŵ₃` was found).
The 165 × 149 exact system over `n = 1..165` (computed mod the prime `q = 10⁹+7`) is
**inconsistent**. A first, smaller run (57-element basis modelled directly on the shape of `ŵ₃`,
80 equations) was also inconsistent.

**Interpretation (this is the real obstruction, and it is structural, not computational).** BZ's
period for the top row is `ζ(5) + 2ζ(2)ζ(3)` — a **depth-2** MZV combination — whereas the middle
row's period `ζ(3)` has depth 1. Products of harmonic numbers at the arguments
`k, l, k+l, n±k, n±l, n+k+l` span exactly the *depth-≤1-generated* weights; the weight-5 row should
require genuinely **nested** (depth-2) sums, e.g. `Σ_{i≤k} H^{(2)}_{n+i}/(n+i)`. This is precisely
what Brown–Zudilin call "a difficult technical task" (their Remark on the MZV decomposition) and
what the sibling repo's §V8 recorded as the un-anchorable step. **T1 for `P` is open, and the
next attempt should enlarge the ansatz by nested letters, not by more monomials.**

### 3.4 The (I3) reduction — an exact structural decomposition of `P̂`, recorded

Independently of Theorem B, BZ's eq. (I3) (paper §"Descent to ζ(3)", LaTeX
`papers/20-.../2026-01-26_CellZeta.tex` lines 690–725) specialises in the totally symmetric case
(`p_j=q_k=n` except `p_3=2n`; put `k = n+j`) to
```
I''_n  =  Σ_{j=0}^{n} (−1)^j C(n+j,n) C(n,j)² · J_3(n,n,n,n−j; n,n,n+j).
```
The RV condition `p_3+q_3 = q_1+q_2` holds (`2n = 2n`), so each `J_3 = α_jζ(3) − β_j`, and BZ's
`A`-formula (quoted from [Zu04]) gives `α_j ∝ Ã_j := Σ_i C(n+i,n)C(n+i+j,n)C(n,i)²` — a **shifted
Apéry sequence** (`Ã_0 = a_n`). Summing the ζ(3)-parts reproduces (BZ-Q) exactly:
`Q_n = Σ_j C(n+j,n)C(n,j)² Ã_j` **[VERIFIED exact, n ≤ 12]**. So the middle row is
`P̂_n = Σ_j C(n+j,n)C(n,j)² β_j`.

Applying §3.1's recipe to `F_j(t) = ∏_{m=1}^n(t−m)·∏_{m=1}^n(t−j−m) / ∏_{m=0}^n(t+m)²`
(whose double-pole coefficients are exactly `c_i = C(n+i,n)C(n+i+j,n)C(n,i)²`, so `Σ_i c_i = Ã_j`,
and whose residues sum to zero) gives the explicit candidate
```
B̃_j = Σ_{i=0}^n c_i [ H_i^{(3)} + λ_i(j) H_i^{(2)} ],
λ_i(j) = ½[ 3H_i + H_{i+j} − H_{n+i} − H_{n+i+j} − 2H_{n−i} ]   (= 2H_i−H_{n+i}−H_{n−i} at j=0 ✓).
```
**[VERIFIED]** `Σ_j C(n+j,n)C(n,j)² B̃_j` reproduces `P̂_n` up to a small, explicitly computable
discrepancy `D_n = P̂_n − Σ_j C(n+j,n)C(n,j)²B̃_j = 1/4, 79/96, 26671/4320, 156557/2304, …`
The discrepancy is a **gauge term**: the rational function `F_j` is not determined by its
double-pole coefficients, and adding any simple-pole part with vanishing residue sum changes `B̃_j`
by `½Σ_i e_i(j)H_i^{(2)}`, `Σ_i e_i(j)=0`, without changing `Ã_j`. The correct `F_j` is the one
carrying the two-variable `(σ+τ)` coupling of the BZ Barnes kernel — i.e. exactly the coupling
that Theorem B's `C₁`-letter encodes. **Theorem B supersedes this route; §3.4 is recorded because
it identifies the pair `(Ã_j, β_j)` as a shifted-Apéry ζ(3) family, which is the right object for
a future inductive proof of the middle-row descent.**

---

## 4. Theorem C [PROVED] — the graded H-layer, and the reduction of (LB₅)

> **Theorem C.** Let `p ≥ 5` be prime, `1 ≤ a < p`, `0 ≤ r < p`, `n = ap+r` (so `n < p²`). Put
> `W_n := P_n − H₅(n)Q_n` and `Ŵ_n := P̂_n − H₃(n)Q_n`. Then
> ```
>   p⁵P_n − P_a Q_r  ≡  p⁵W_n − W_a Q_r   (mod p),
>   p³P̂_n − P̂_a Q_r ≡  p³Ŵ_n − Ŵ_a Q_r   (mod p),
> ```
> both sides being p-integral. Consequently **(LB₅) ⟺ (W5)**: `p⁵W_{ap+r} ≡ W_aQ_r (mod p)`.

*Proof.* For `n = ap+r < p²` the indices `m ≤ n` divisible by `p` are exactly `m = jp`,
`1 ≤ j ≤ ⌊n/p⌋ = a`, and `p ∤ j` since `j ≤ a < p`. Hence
`H₅(n) = S + p^{−5}H₅(a)` with `S := Σ_{m ≤ n, p∤m} m^{−5} ∈ ℤ_p`, so
`p⁵H₅(n) = p⁵S + H₅(a) ≡ H₅(a) (mod p⁵)`.
Since `Q_n ∈ ℤ`, `p⁵H₅(n)Q_n ≡ H₅(a)Q_n (mod p⁵)`, and reducing mod `p` and using Theorem A
(`Q_n ≡ Q_aQ_r`) together with `H₅(a) ∈ ℤ_p` (as `a < p`) gives
`p⁵H₅(n)Q_n ≡ H₅(a)Q_aQ_r (mod p)`. On the other side `P_aQ_r = H₅(a)Q_aQ_r + W_aQ_r`. Subtract.
The weight-3 statement is identical with `5 ↦ 3`. ∎

**Value.** The `H₅`-layer — the whole "`p⁵` pole" of (LB₅) — is now *unconditional*. It needs
nothing but Theorem A and a two-line Kummer/valuation computation, exactly as in the ζ(3) template
(`WARMUP_ZETA3_DWORK.md`, H-part), and it works verbatim at every weight. All of (LB₅)'s difficulty
is transferred to the single congruence (W5) about `W_n`.

**[VERIFIED, 0 failures]** (W5), exhaustively:

| p | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 |
|---|---|---|---|---|---|---|---|---|---|
| `min v_p(p⁵W_n − W_aQ_r)` | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| failures (`< 1`) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `min v_p(W_n)`, `n<p²` | −5 | −5 | −5 | −5 | −5 | −5 | −5 | −5 | −5 |

all single-digit cells `n = ap+r ≤ 360`. **`p = 5` is not exceptional.** The floor is exactly 1
(as for (LB₅) itself), so (W5) is sharp and carries the full content.

---

## 5. (LB₃-in-5): the product form is FALSE — corrected statement

**The failure.** `p³P̂_{ap+r} ≡ P̂_a Q_r (mod p)` fails, and the failures are not sporadic:

| p | cells with `P̂_a ∈ ℤ_p` | failures there | cells with `v_p(P̂_a) = −1` | failures there |
|---|---|---|---|---|
| 5 | 15 | **0** | 5 | 3 |
| 7 | 35 | **0** | 7 | 5 |
| 11 | 77 | **0** | 33 | 24 |
| 13 | 91 | **0** | 65 | 55 |
| 17 | 153 | **0** | 119 | 84 |
| 19 | 190 | **0** | 152 | 128 |
| 23 | 276 | **0** | 230 | 70 |
| 29 | 435 | **0** | 377 | 0 |
| 31 | 496 | **0** | 434 | 0 |

> **[VERIFIED, 0 failures over 1768 cells, p ∈ {5,…,31}]** (LB₃-in-5), corrected:
> **if `v_p(P̂_a) ≥ 0` then `p³P̂_{ap+r} ≡ P̂_a·Q_r (mod p)`.**
> **[VERIFIED, 0 failures]** the master form `p³P̂_nQ_a ≡ P̂_aQ_n (mod p)` holds on *all* cells
> (this is the form quoted in `ORCHESTRATOR_NOTES §2d`; it survives because it is the polar cells'
> weighted version, and it does **not** imply the product form when `p | Q_a` or `P̂_a ∉ ℤ_p`).
> **[VERIFIED]** `v_p(P̂_a) ≥ −1` for all `a < p` and all `p ∈ {5,…,31}`, with equality attained.

**Why — and this is now explained, not observed.** By Theorem B, `P̂_a = Σ_{k,l}T(a,k,l)ŵ₃(a,k,l)`,
and for `a < p` the **only** letter that can be non-`p`-integral is `A_r(k) = H^{(r)}_{a+k} −
H^{(r)}_k`, whose upper argument `a+k` reaches `2a`. So `A₃(k)` contributes a term `p^{−3}` exactly
when `a+k ≥ p`, and nothing else in `ŵ₃` reaches that depth. Hence
```
v_p(P̂_a) ≥ −3 + min{ v_p T(a,k,l) : a+k ≥ p }  ≥  −3 + 2  =  −1
```
**by Lemma D below** — the coefficient of `p^{−3}` is divisible by `p²`. This reproduces the
observed floor `−1` exactly, and it identifies the culprit: the argument `2n` inside the `A`-letter,
i.e. BZ's `d_{2n}`.

**Consequence for the campaign.** The middle row is **not** the easy warm-up. At weight 3 the
graded weight `p³` is *one power short* of clearing the row's own denominator, so the naive
"Frobenius diag(1, p³, p⁵)" product congruence cannot hold verbatim in the middle slot; the correct
middle entry is `p³` **relative to a `p`-integralised `P̂`** (equivalently, the statement must be
made for `d`-normalised `P̂` or restricted to `P̂_a ∈ ℤ_p`). The top row `P` has no such defect
(`v_p(W_n) ≥ −5` with `p⁵` available — exactly matched), which is why (LB₅) and (W5) are clean.

---

## 6. Lemma D [PROVED] — the key new lemma (the non-square-summand replacement)

In the ζ(3) template the summand `A(n,k)=C(n,k)²C(n+k,k)²` is a perfect square, so a **single**
Kummer carry yields `v_p ≥ 2`; that slack closes both the dangerous case of Lemma V and the
`a+j ≥ p` case (`WARMUP_ZETA3_DWORK.md`, T3). The BZ summand
`T(N,k,l) = C(N+k,N)C(N,k)²C(N+l,N)C(N,l)²C(N+k+l,N)` has **three unsquared** binomials, so a
single carry only gives `v_p ≥ 1`. The replacement is that **one digit overflow forces carries in
two different unsquared binomials**:

> **Lemma D (triple-carry slack).** Let `p` be prime, `N = ap+r` with `0 ≤ a, r < p`, and
> `k = bp+s`, `l = cp+t` with `0 ≤ s,t < p` and `0 ≤ b,c ≤ a` (automatic when `k,l ≤ N`).
> **If `a + b ≥ p` then `v_p(T(N,k,l)) ≥ 2`.**

*Proof.* By Kummer, `v_p C(N+k,N)` = number of carries in the base-`p` addition `N + k`. The
position-0 carry is `ε₀ = [r+s ≥ p]`; the position-1 sum is `a + b + ε₀ ≥ a+b ≥ p`, so there is a
carry at position 1. Hence `v_p C(N+k,N) ≥ 1`, with `≥ 2` if `r+s ≥ p`. So assume, else we are done:
1. `r + s < p`;
2. `s ≤ r` and `t ≤ r` — otherwise `s > r` (resp. `t > r`) forces a borrow in `N − k` (resp.
   `N − l`), so `v_p C(N,k) ≥ 1` and the **squared** factor `C(N,k)²` already gives `v_p ≥ 2`;
3. `a + c < p` — otherwise the position-1 argument applied to `C(N+l,N)` gives another power;
4. `r + t < p` — otherwise `C(N+l,N)` has a position-0 carry, giving another power.

From 1,2,4: `s + t < p`. [If `s+t ≥ p`, then `p ≤ s+t ≤ 2r` forces `r ≥ p/2`, while `r+s<p`,
`r+t<p` force `s,t ≤ p−1−r` hence `s+t ≤ 2(p−1−r) < p`, a contradiction.]
From 3 and `b ≤ a`: `b + c ≤ a + c < p`.
Therefore `k + l = (b+c)p + (s+t)` is the base-`p` expansion (both digits `< p`), and the
position-1 sum in the addition `N + (k+l)` is `a + (b+c) + [r+s+t ≥ p] ≥ a + b ≥ p`: a carry.
So `v_p C(N+k+l,N) ≥ 1` as well, and `v_p T(N,k,l) ≥ 1 + 1 = 2`. ∎

**[VERIFIED]** 24741 cases (`p ∈ {5,7}`, all `a,r`, all `k,l ≤ N`), **0 failures**.

**Sharpness.** The three-carry strengthening is **false**: `a+b ≥ p` *and* `a+c ≥ p` does **not**
give `v_p ≥ 3` (**649 counterexamples** in the same range). So Lemma D is exactly the available
slack — no more.

**Where it is used.** (i) It is precisely what makes `v_p(P̂_a) ≥ −1` instead of `−3` in §5 —
i.e. it is *already load-bearing* and *already confirmed against independent data*. (ii) It is
the drop-in replacement for the perfect-square step in any port of the T3 W-part argument:
wherever the ζ(3) proof wrote "`a+j ≥ p ⟹ v_p A(a,j) ≥ 2` because `A` is a square", the BZ proof
writes "`a+b ≥ p ⟹ v_p T ≥ 2` by Lemma D".


### 6b. Lemma D⁺ and the first payoff: the exact `p`-adic size of the middle row

> **Lemma D⁺ (refined triple-carry).** With `N = ap+r`, `k = bp+s` as in Lemma D, set
> `β := ⌊(N+k)/p⌋ = a + b + [r+s ≥ p]`. **If `β ≥ p` then `v_p(T(N,k,l)) ≥ 2` for every `l`.**

*Proof.* If `a+b ≥ p` this is Lemma D. Otherwise `β ≥ p` forces `[r+s≥p] = 1` and `a+b = p−1`.
Then the base-`p` addition `N + k` carries at position 0 (`r+s ≥ p`) **and** at position 1
(`a+b+1 = p ≥ p`), so `v_p C(N+k,N) ≥ 2` by Kummer alone. ∎

**[VERIFIED]** 28128 cases (`p ∈ {5,7}`, all `a,r`, all `k,l ≤ N`), **0 failures**.

> **Corollary (integrality of the middle row) [PROVED, conditional on Theorem B].**
> For `n < p²` and `p ≥ 5`, `v_p(P̂_n) ≥ −4`; and for `n < p`, `v_p(P̂_n) ≥ −1`.

*Proof.* By Theorem B, `P̂_n = Σ_{k,l}T(n,k,l)ŵ₃(n,k,l)`. Inspect `ŵ₃`'s letters for `n < p²`,
`k = bp+s` with `b ≤ a`:
* `H^{(3)}_n = (ℤ_p) + p^{−3}H^{(3)}_a`, and `a < p` so `H^{(3)}_a ∈ ℤ_p`: pole order `3`.
* `A₃(k) = H^{(3)}_{n+k} − H^{(3)}_k = (ℤ_p) + p^{−3}(H^{(3)}_β − H^{(3)}_b)` with `β = ⌊(n+k)/p⌋`,
  `b = ⌊k/p⌋ < p`. Since `β ≤ 2a+1 < 2p`, `H^{(3)}_β = (ℤ_p) + p^{−3}[β ≥ p]`. So
  `A₃(k) = p^{−6}[β≥p] + p^{−3}(ℤ_p) + (ℤ_p)`; **only** the indicator term reaches depth 6, and
  by **Lemma D⁺** every `(k,l)` contributing to it has `v_p T ≥ 2`. Pole order `≤ 4` after
  weighting.
* `A₂(k)·X₁` with `X₁ ∈ {A₁,B₁,C₁}`: `A₂` reaches `p^{−4}` (same mechanism, `p^{−2}·p^{−2}`),
  `X₁` reaches `p^{−2}`; the deepest combinations again require `β ≥ p`, so Lemma D⁺ applies.
Taking the minimum gives `−4`. For `n = a < p` the only offending letter is `A₃(k)` with `a+k ≥ p`
(no `p`-divisible `m ≤ a` at all, so `H^{(3)}_a, B_r, C_r` are all `p`-integral), giving
`−3 + 2 = −1`. ∎

**[VERIFIED, both bounds attained]** `min_{n<p²} v_p(P̂_n) = −4` for `p ∈ {5,…,23}` (`= −3` for
`p = 29,31` only because the ladder stops at `n = 360 < p²`); `min_{a<p} v_p(P̂_a) = −1` for every
`p ∈ {5,…,31}`.

**Why this matters.** It is an independent, *quantitative* confirmation that Theorem B is the
right identity — the formula predicts the observed `p`-adic sizes exactly, including the
`−1` floor that broke the product form in §5 — and it shows the machinery (Theorem B + Lemma D⁺)
is already strong enough to prove genuine arithmetic statements about the middle row. It also
pins the correct graded weight for `P̂`: the middle Frobenius slot needs **`p⁴`**, not `p³`, if
one insists on an unnormalised product congruence (`p³` suffices only where `P̂_a ∈ ℤ_p`).

### 6c. The proof of (LB₃-in-5) that is now set up (next step, not done here)

Theorem C splits `p³P̂_n − P̂_aQ_r` into an `H`-part and a `W`-part. With Theorem B the `W`-part
is now an explicit sum, and the ζ(3) template's three moves all have their replacements:

| ζ(3) proof (T3) | Brown–Zudilin replacement |
|---|---|
| `b_n = H₃(n)a_n + W(n)`, `W` a single sum | Theorem B: `P̂_n = Σ T·ŵ₃`, `ŵ₃ = H^{(3)}_n + A₃(k)+A₃(l) + (A₂-terms)` |
| only `p \| m` indices carry the pole | only the letters `H^{(3)}_n`, `A_r(·)`, `C_r` carry poles; `B_r` never does for `n<p²` |
| Kummer borrow/carry ledger | Lemmas 1–4 (§2) give the full mod-`p` factorization of `T` |
| perfect square ⟹ `v_p ≥ 2` per carry | **Lemma D / D⁺** |
| tail-vanishing when `a+j ≥ p` | `β ≥ p` ⟹ `v_p T ≥ 2` (Lemma D⁺), i.e. the tail is killed by the *same* condition that creates the deep pole — the two cancel, which is precisely why the floor is `−1` and not `−3` |

The one genuinely new bookkeeping item is that the pole-creating condition (`β ≥ p`) and the
tail-killing condition are now *the same* condition, so the two must be tracked together rather
than in separate cases as in T3.

---

## 7. Status, and what (LB₅) buys (T4, unchanged part)

**Proved here.** Theorem A (Q-row Lucas, complete proof, all `p`, all `a ≥ 0`); Theorem C (the
graded `H`-layer at weights 3 and 5, and the reduction (LB₅) ⟺ (W5)); Lemma D (the key new
lemma) and its sharpness; the Proposition of §3.1 (new harmonic-monomial closed form for Apéry's
`b_n`).

**Found and verified, not yet proved.** Theorem B — the exact weight-3 closed form for `P̂_n` on
the Brown–Zudilin summand. It is an identity between two explicit expressions and should be
provable by creative telescoping (both sides satisfy the BZ order-3 recurrence in `n`; matching
`n = 0,1,2` then finishes) — *that is the single highest-value next step*, and it is a finite
computation, not a search.

**Open with a precise obstruction.**
* **(W5)** — equivalently (LB₅). Blocked on T1 for the top row: without `w₅` there is no summand
  to run the Kummer ledger on. §3.3 shows the obstruction is the depth-2 (`ζ(5)+2ζ(2)ζ(3)`) nature
  of the top period; the ansatz must be enlarged by *nested* letters.
* **(LB₃-in-5)** — the corrected statement of §5. With Theorem B in hand this is now a concrete
  target: split `ŵ₃ = [H^{(3)}_n + A₃(k) + A₃(l)] + [the A₂-terms]`; the first bracket is the
  "H-part" (Theorem C machinery, but with the `2n`-argument subtlety of §5), the second is the
  "W-part" and needs the Lemma D ledger. **This is the natural next proof to attempt** and it is
  now fully set up.

**What (LB₅) gives (recorded, unchanged).** Iterating the product form with the `p^{5L}`-scaled
induction (not the naive master form — see `ORCHESTRATOR_NOTES §2d`) yields
`ord_p(P_n) ≥ −5L`, `L = ⌊log_p n⌋`, hence `ord_p(p_n) ≥ κ − 5L` = (CB) for all `p ≥ 5`, with
`κ = ord_p C(2n,n)`. The correct induction statement must be scaled: prove
`ord_p( p^{5L}P_n − P_{n_L}·∏_{i<L}Q_{n_i} ) ≥ 1` by induction on the number of digits `L`, with
`P_{n_L}` `p`-integral at the terminal digit — the unscaled master form goes negative at
exceptional primes purely by renormalisation.

**Phase 2 is NOT yet a theorem.** Two of its three graded rows are now theorems in the sense that
matters (row `Q`: Theorem A; the `H`-layer of row `P`: Theorem C), the middle row's statement has
been *corrected* (§5) and its exact decomposition *found* (Theorem B), and the missing valuation
lemma has been *identified and proved* (Lemma D). The remaining gap is exactly one object:
the weight-5 nested harmonic weight `w₅` of `P_n`.

---

## Appendix — corrections to prior campaign notes

1. `ORCHESTRATOR_NOTES §2d` / the brief's ESTABLISHED item 2: `Q_n = Σ_k C(n,k)²C(n+k,k)` is
   **wrong** (that is A005258; `Q_1 = 3 ≠ 21`). Correct: the double sum (BZ-Q). Theorem A is
   proved for the correct `Q_n`.
2. The brief's ESTABLISHED item 3 states (LB₃-in-5) as `v_p(p³P̂_nQ_q − P̂_qQ_n) ≥ 1` — that
   master form is correct, but it does **not** give the product form `p³P̂_{ap+r} ≡ P̂_aQ_r`,
   which is false (§5). Any "Frobenius `diag(1,p³,p⁵)`" statement must use a `p`-integralised
   middle row.
3. `WARMUP_ZETA3_DWORK.md` T4(c) predicted the loss of the perfect-square slack as the main
   obstruction for the port. Confirmed, and resolved: Lemma D.
4. `WARMUP_ZETA3_DWORK.md` T4(b) predicted "no clean Apéry single-sum for `P_n`". Half right:
   there **is** one for `P̂_n` (Theorem B, and on the *same* BZ summand, which is stronger than
   expected); for `P_n` the negative result of §3.3 confirms the prediction, and localises why.
