# LEAN_APERY_DEFECT — kernel-checking the Apéry defect results

**Agent:** Lean formalization agent (River's odd-zeta program), 2026-07-26
**Module:** `lean/ZetaLucas/Defect.lean` (new), added to `lean/ZetaLucas.lean`
**Toolchain:** Lean `v4.33.0-rc1`, Mathlib `cd580e54`. `lake build` **passes**, whole project.
**Sources checked:** `work/APERY_DEFECT.md` §§3.1–3.3, §4.1; `papers_out/frobenius_matrix/main.tex`.

---

## 0. Headline

* **T1 is done: `V_n = 0` is through the kernel, sorry-free, for all `n`.**
  And the residue proof in the write-up is **not needed** — the function whose residues are
  summed is a *rational* function, so the whole thing is a one-page algebraic argument
  (§1 below). No complex analysis, no `Γ`, no Mathlib gap.
* **T2 second half is done** (the borrow region / squareness step), sorry-free.
* **T2 first half (region-I expansion) is not done**, and the obstruction is named precisely: the
  project has no `mod p^m` p-adic congruence for `m ≥ 2` (`PadicBridge` only has `mod p`).
* **T3 adjudication: the derivation is sound but incomplete as written.** It silently uses one
  lemma that is *not* stated anywhere, and that lemma is load-bearing. I have proved it (§4).
* **Mathlib gap confirmed: no Wolstenholme of any kind.** But the write-up **over-quotes** what
  it needs: the `mod p²` digit expansion uses only the *weak* form `H_{p−1} ≡ 0 (mod p)`, not
  `H_{p−1} ≡ 0 (mod p²)` and not `H^{(2)}_{p−1} ≡ 0 (mod p)`. Weak Wolstenholme is now proved in
  Lean (§3).

Everything below was verified numerically in exact `Fraction` arithmetic *before* being attempted
in Lean, and every headline has `#print axioms` output showing `[propext, Classical.choice,
Quot.sound]` only. No `native_decide` anywhere.

---

## 1. T1 — `V_n = 0` `[PROVED IN LEAN, sorry-free]`

```
theorem ZetaLucas.apery_defect_V_eq_zero (n : ℕ) :
    ∑ k ∈ range (n + 1),
        ((n.choose k : ℚ) ^ 2 * ((n + k).choose k : ℚ) ^ 2)
      * ( Σ_{j=1}^{n+k} 1/j + Σ_{j=1}^{n−k} 1/j − 2 Σ_{j=1}^{k} 1/j ) = 0
```
`#print axioms` → `[propext, Classical.choice, Quot.sound]`.

### The proof that was formalized (not the one in the paper)

The instruction was to prefer an elementary route. **Telescoping in `k` provably fails**, and it
is worth recording why, because it is not a tooling limitation:

> Any antidifference of the shape `Ψ(k) = A(n,k)·(α H_{n+k} + β H_{n−k} + γ H_k + δ)` with
> `α,β,γ,δ ∈ ℚ(n,k)` forces, on the `H_{n+k}` channel, `r(k)α(k+1) − α(k) = 1` with
> `r(k) = A(n,k+1)/A(n,k)`. That is exactly Gosper's equation for `A(n,k)` itself, i.e. it says
> the Apéry summand is Gosper-summable — which it is not (else `a_n` would have a closed form).
> The same equation appears independently on the `H_{n−k}` and `H_k` channels. So the
> `MinimalForm.lean` pattern (`bMin_rec`, a single `Ψ` closed by `Finset.sum_range_sub`) cannot
> be reused here.

What *does* work is to notice that the paper's `g(z) = Γ(n+z+1)²Γ(z−n)²/Γ(z+1)^4` is a rational
function:

```
  Γ(n+z+1)/Γ(z+1) = ∏_{i=1}^{n}(z+i) =: P(z)        (a polynomial, degree n)
  Γ(z−n)/Γ(z+1)   = 1/∏_{j=0}^{n}(z−j) =: 1/Q(z)    (Q has degree n+1)
  ⟹  g = (P/Q)² = φ² ,  deg num 2n, deg den 2n+2 .
```

`φ = P/Q` has **simple** poles at `z = 0,…,n` with residues `α_k = (−1)^{n−k}C(n,k)C(n+k,k)`. So
`g = φ²` has, at `z = m`, residue `2 α_m Σ_{k≠m} α_k/(m−k)`: the double pole of `φ²` contributes
nothing and the cross terms give a **manifestly antisymmetric** double sum. Summing over `m`
gives `0` by the swap `(m,k) ↦ (k,m)` — no contour, no growth estimate, no "sum of residues of an
`O(z^{-2})` function".

Concretely the formalization is two steps.

**(★) The Lagrange step.** For `m ≤ n`, with `β_k = (−1)^k C(n,k)C(n+k,k)`,
```
theorem ZetaLucas.star_identity (n m : ℕ) (hm : m ≤ n) :
    ∑ k ∈ range (n + 1), bb n k / ((m : ℚ) − (k : ℚ)) = bb n m * vv n m
```
(the `k = m` term is `β_m/0 = 0` under Lean's division convention, so no `erase` is needed in the
statement). Proof: Lagrange-interpolate `P(X) = ∏_{i=1}^n (X+i)` at the `n+1` nodes `0,…,n`
(`Polynomial.eq_of_degrees_lt_of_eval_index_eq`), differentiate the resulting polynomial identity
`Σ_k β_k W_k = (−1)^n P` once (`Lagrange.derivative_nodal`), evaluate at `X = m`, and divide by
the nonzero nodal weight `∏_{j≠m}(m−j) = (−1)^{n−m} m!(n−m)!`. The two log-derivatives that
appear are `P'(m)/P(m) = H_{n+m} − H_m` and `W_m'(m)/W_m(m) = H_m − H_{n−m}`; their difference is
exactly `v(n,m)`.

**(antisymmetry) The sum step.** `A(n,m) = β_m²`, so
`V_n = Σ_m β_m Σ_k β_k/(m−k) = Σ_{m,k} β_mβ_k/(m−k) = −V_n` by `Finset.sum_comm`.

Imported machinery: `Mathlib.LinearAlgebra.Lagrange` (`nodal`, `derivative_nodal`,
`eq_of_degrees_lt_of_eval_index_eq`) and `Polynomial.derivative`. Nothing else.

**Numerics.** `V_n = 0` exact over ℚ for `n ≤ 60` (re-run from scratch, 0 nonzero), and (★)
re-verified for all `0 ≤ m ≤ n ≤ 24`, and the underlying polynomial identity at random rationals
for `n ≤ 11`. In-file `#eval` prints `V_0..V_8 = [0,…,0]`.

**Effort:** ≈ 55 min including the search for the elementary route. ≈ 420 lines.

---

## 2. T2 — the digit expansion

### 2a. Second half (borrow region): `[PROVED IN LEAN, sorry-free]`

```
theorem ZetaLucas.borrow_left  {a c r s} (hr : r < p) (hs : s < p)
    (h : ¬ (s ≤ r ∧ c ≤ a ∧ r + s < p)) : p ^ 2 ∣ A (a*p + r) (c*p + s)
theorem ZetaLucas.borrow_right {a c r s} (hr : r < p) (hs : s < p)
    (h : ¬ (s ≤ r ∧ c ≤ a ∧ r + s < p)) : p ^ 2 ∣ A a c * A r s
theorem ZetaLucas.borrow_congr ... :
    (A (a*p+r) (c*p+s) : ZMod (p^2)) = ((A a c * A r s : ℕ) : ZMod (p^2))
```
The squareness step is isolated as
`sq_dvd_A_low : p ∣ C(n,k) → p² ∣ A n k` and `sq_dvd_A_high : p ∣ C(n+k,k) → p² ∣ A n k`,
each a one-liner from `A n k = C(n,k)² C(n+k,k)²`. The three exit cases are:
`s > r` and `c > a` kill the *lower* binomial via `choose_digits`; the carry `r+s ≥ p` kills the
*upper* one via `choose_digits_zero` applied to `(a+c+1)p + (r+s−p)` (the same computation as
`Apery.A_digits`). All three ingredients were already in `Core.lean`.

This is the step the brief flagged as load-bearing, and it **checks out exactly as stated**.
Numerically confirmed for `p ≤ 31`, all `a,c,r,s < p`: 0 failures.

### 2b. First half (region-I expansion): **NOT formalized**, obstruction named

```
A(ap+r, cp+s) ≡ A(a,c)A(r,s)(1 + 2p[a·u(r,s) + c·v(r,s)])  (mod p²)     — verified, not Lean
```
Numerically re-verified from scratch: `p = 5,…,31`, all `a,c,r,s` in region I, 0 failures.

The obstruction is **not** Wolstenholme. It is infrastructural: the project's p-adic bridge
(`PadicBridge.lean`) provides `PInt` (`v_p ≥ 0`), `PDvd` (`v_p ≥ 1`) and `PCong` (congruence
`mod p`) on ℚ — and *nothing graded*. The digit expansion is a `mod p²` statement about
rationals; formalizing it needs a `PDvdPow p m q ↔ v_p(q) ≥ m` layer plus its `mul`/`sum`/
`pow` calculus, and then the factorial decomposition
`(Np+R)! = p^N · N! · U(N,R)`, `U(N,R) ≡ ((p−1)!)^N R! (1 + Np·H_R) (mod p²)`.
Estimated 400–600 lines of new p-adic infrastructure before the expansion itself is reachable.
That is a whole session on its own; I did not start it rather than leave a half-built tower.

### 2c. Wolstenholme: Mathlib gap, and the write-up over-quotes it

Searched Mathlib `cd580e54`: **zero occurrences** of "Wolstenholme", and no statement of
`H_{p−1} ≡ 0` in any modulus. Confirmed gap.

But re-deriving the expansion by hand shows the strong form is never used. The only place
`H_{p−1}` enters is the block product
```
∏_{l=1}^{p−1}(ip+l) ≡ (p−1)! (1 + i·p·H_{p−1})   (mod p²)   [the (ip)² terms die]
```
and for the block to be `≡ (p−1)! (mod p²)` one needs `p·H_{p−1} ≡ 0 (mod p²)`, i.e.
**`H_{p−1} ≡ 0 (mod p)`** — the weak form, which follows from the elementary pairing `l ↔ p−l`
and needs no `H^{(2)}_{p−1}`. So `main.tex` Lemma 2.3's proof sketch ("Wolstenholme's congruences
`H_{p−1} ≡ 0 (mod p²)` and `H^{(2)}_{p−1} ≡ 0 (mod p)` make the factors cancel") **cites more
than it uses**. Not an error, but it points the formalization at a much harder input than
necessary. Recommend weakening the citation in the paper.

Accordingly:
```
theorem ZetaLucas.wolstenholme_weak {p : ℕ} [Fact p.Prime] (hp : 2 < p) :
    PDvd p (Harm 1 (p - 1))
```
is now proved in Lean, sorry-free, via
`2·H_{p−1} = p·Σ_{j<p−1} 1/((j+1)(p−1−j))` (`two_mul_Harm_pred`) and `p`-integrality of the sum.

**Effort (T2):** ≈ 30 min (borrow region + Wolstenholme). ≈ 130 lines.

---

## 3. T3 — adjudication of Corollary 2.4

**Verdict: the derivation is correct, but it is not complete as written. It uses one lemma that
appears nowhere in either document, and that lemma is essential — not cosmetic.**

The corollary is
```
(a_{ap+r} − a_a a_r)/p ≡ 2a·a_a·U_r ,   (p³b_{ap+r} − b_a a_r)/p ≡ 2a·b_a·U_r   (mod p)
U_r = Σ_{s≤r} A(r,s)·u(r,s) ,  V_r = Σ_{s≤r} A(r,s)·v(r,s) = 0 .
```

### What the derivation does supply

* Splitting `k = cp+s` over `c ≤ a`, `s < p` is legitimate: `n = ap+r < p²`.
* Outside region I both sides are `≡ 0 (mod p²)` — §2a, now proved.
* The weight: `H^{(3)}_{ap+r} = p^{−3}H^{(3)}_a + G_{ap+r}` with `G` `p`-integral, so
  `p³b_n ≡ Σ_{c,s} A(n,cp+s)(2H^{(3)}_a − H^{(3)}_c)` mod `p³`, and the coefficients
  `2H^{(3)}_a − H^{(3)}_c` are `p`-integral because `a, c < p`. Fine.
* `V = 0` (T1) kills the `a'_a`/`b'_a` channel. Fine.

### The gap

The digit expansion is available **only** for `r + s < p`. So what the summation actually
produces is the *restricted* functionals
```
Ũ_r = Σ_{s ≤ r, r+s < p} A(r,s)u(r,s) ,   Ṽ_r = Σ_{s ≤ r, r+s < p} A(r,s)v(r,s) ,
```
not `U_r` and `V_r`. Both documents write `U_r`, `V_r` and never mention the restriction. The
identification `Ũ_r ≡ U_r`, `Ṽ_r ≡ V_r (mod p)` is **true but needs proof**, and it is exactly
the same squareness mechanism one level up:

> for `r + s ≥ p` one has `p² ∣ A(r,s)` (the carried binomial `C(r+s,s) ≡ 0 mod p`, squared),
> while `v_p(u(r,s)), v_p(v(r,s)) ≥ −1` (arguments `< 2p`, so at most one `1/p`), hence every
> dropped term has `v_p ≥ 1`.

This is not pedantry. Without it the corollary's `U_r` is not even well defined `p`-adically:
`U_r` is a *`p`-independent rational with `p` in its denominator* for small `r` —
`U_5 = 13276637/10`, `U_7 = 67890874657/70` (`v_5(U_5) = v_7(U_7) = −1`). `U_r` is `p`-integral
**only because `r < p` is assumed**, and *that* is a consequence of the missing lemma, not of
anything stated. A reader who takes `U_r` at face value has no reason to believe
`2a·a_a·U_r (mod p)` is meaningful.

### Closing the gap in Lean `[PROVED, sorry-free]`

```
theorem ZetaLucas.V_restricted_dvd  {r} (hr : r < p) :
    PDvd p (∑ s ∈ (range (r+1)).filter (fun s => r + s < p), (A r s : ℚ) * vv r s)
theorem ZetaLucas.U_restricted_cong {r} (hr : r < p) :
    PCong p (∑ s ∈ (range (r+1)).filter (fun s => r + s < p), (A r s : ℚ) * uu r s)
            (∑ s ∈ range (r+1), (A r s : ℚ) * uu r s)
theorem ZetaLucas.U_pInt {r} (hr : r < p) : PInt p (∑ s ∈ range (r+1), (A r s : ℚ) * uu r s)
```
with the supporting `p_mul_Harm_pInt` (`v_p(H_m) ≥ −1` for `⌊m/p⌋ < p`, from `Letters.K_descent`)
and `carry_dvd_gen`. So the `V`-channel really does die in the form the corollary needs, and
`U_r` really is `p`-integral in the range where the corollary is stated.

### Summary of the adjudication

| item | status |
|---|---|
| region-I expansion (input) | verified numerically, **not proved in Lean**; proof in the write-up is correct but over-cites Wolstenholme |
| borrow region contributes nothing | **proved in Lean** |
| weight contributes nothing below `p³` | correct as written (uses `a,c < p`) |
| `V = 0` kills the second channel | **proved in Lean** (T1) |
| `Ũ_r ≡ U_r`, `Ṽ_r ≡ V_r (mod p)` | **missing from both documents**; now **proved in Lean** |
| conclusion | derivation is complete **once the missing lemma is inserted**; no circularity, no hole |

**Recommendation for the paper:** add one sentence after Lemma 2.3 —
*"Because `A` is a square, the terms with `r+s ≥ p` satisfy `v_p(A(r,s)) ≥ 2` while
`v_p(u), v_p(v) ≥ −1`; hence `U_r`, `V_r` may be summed over the full range `s ≤ r`, and in
particular `U_r` is `p`-integral for `r < p` despite having `p` in its denominator for larger
`r`."*

Independent numerical re-verification of the corollary itself: `p = 5,…,19`, all `a,r < p`, both
rows — **0 failures**; and the `mod p²` two-level law has floor exactly 2 (worst case) over the
same range. Consistent with the report's 9-prime claim.

**Effort (T3):** ≈ 25 min (adjudication + the three Lean lemmas). ≈ 120 lines.

---

## 4. T4 — Γ-deformation origin of `b_n`: assessed, **out of scope**, not started

The statement `b_n = ½ [ε³] Σ_k A(n,k) ∏_j Π_j(n)^{u_j} Π_j(k)^{v_j}` is a coefficient-extraction
identity. Formalizing it needs either `PowerSeries ℚ` with `coeff 3` of a finite product of
`Π_j(t) = ∏_{i≤t}(1 + jε/i)`, or a truncated-polynomial encoding `ℚ[ε]/(ε⁴)`. The mathematical
content — `L₁ = L₂ = 0` termwise from `e₁(u) = e₂(u) = 0` — is a Newton-identity computation in
the exponents, which is easy; the cost is entirely in setting up `log`/`exp` of a formal product
and extracting `B₃ = L₃ + L₁L₂ + L₁³/6`, i.e. a partial-Bell/`exp`-of-series lemma that Mathlib
does not have in usable form for finite products of this shape. Estimate 500+ lines. Correctly
ranked last; not started.

---

## 5. What compiles, with axioms

`lake build` output: `Build completed successfully (8673 jobs)`. `ZetaLucas/Defect.lean` contains
**no `sorry` and no `native_decide`**. (The project's one pre-existing quarantined `sorry` is in
`BZClosedForm.lean` §5, untouched by this work.)

```
'ZetaLucas.Vsum_eq_zero'            [propext, Classical.choice, Quot.sound]
'ZetaLucas.apery_defect_V_eq_zero'  [propext, Classical.choice, Quot.sound]
'ZetaLucas.star_identity'           [propext, Classical.choice, Quot.sound]
'ZetaLucas.key_poly'                [propext, Classical.choice, Quot.sound]
'ZetaLucas.borrow_left'             [propext, Classical.choice, Quot.sound]
'ZetaLucas.borrow_right'            [propext, Classical.choice, Quot.sound]
'ZetaLucas.borrow_congr'            [propext, Classical.choice, Quot.sound]
'ZetaLucas.wolstenholme_weak'       [propext, Classical.choice, Quot.sound]
'ZetaLucas.V_restricted_dvd'        [propext, Classical.choice, Quot.sound]
'ZetaLucas.U_restricted_cong'       [propext, Classical.choice, Quot.sound]
'ZetaLucas.U_pInt'                  [propext, Classical.choice, Quot.sound]
```

In-file sanity `#eval`s (evaluated, not kernel-checked):
* `V_0..V_8 = [0,0,0,0,0,0,0,0,0]`
* `U_0..U_8 = [0, 6, 105, 2219, 104825/2, 13276637/10, 70543291/2, 67890874657/70,
  766399019471/28]` — **exactly** the values printed in `main.tex` §1, computed here from the
  independent Lean definitions. Good cross-check of the paper's numbers.

---

## 6. Findings, ordered by how much they matter

1. **The residue proof of `V_n = 0` is unnecessarily analytic.** `g` is rational; the theorem is
   Lagrange interpolation of `∏_{i=1}^n(X+i)` at `0,…,n`, differentiated, plus an antisymmetry.
   The paper should say so — it turns a `Γ`-function/reflection/growth-estimate argument into
   half a page of algebra valid over any field of characteristic 0, and it is what made T1
   formalizable in under an hour. (`main.tex` Theorem 2.2's proof is *correct*; it is just three
   levels more expensive than needed.)
2. **Corollary 2.4 has a missing lemma** (`Ũ ≡ U`, `Ṽ ≡ V` mod `p`, and hence `p`-integrality of
   `U_r`) — §3. Now proved. Suggested sentence supplied.
3. **Lemma 2.3 over-cites Wolstenholme**: only `H_{p−1} ≡ 0 (mod p)` is used, not the `mod p²`
   form and not `H^{(2)}_{p−1}`. Weak Wolstenholme now proved in Lean.
4. **Mathlib gap: no Wolstenholme at all**, in any form.
5. **Project gap: `PadicBridge` is `mod p` only.** Any `mod p^m` statement (the digit expansion,
   the `mod p³` scalar law, the `mod p⁴` matrix conjecture) is blocked on a graded valuation
   layer that does not exist yet. This is the single highest-leverage next piece of
   infrastructure for this program.
6. **Telescoping genuinely fails for `V_n`** (Gosper obstruction, §1) — recorded so nobody
   spends a session looking for a WZ certificate that cannot exist in that shape.

---

## 7. Files

| file | what |
|---|---|
| `lean/ZetaLucas/Defect.lean` | everything above; §§0–7 of the module mirror this report |
| `lean/ZetaLucas.lean` | `import ZetaLucas.Defect` added |
