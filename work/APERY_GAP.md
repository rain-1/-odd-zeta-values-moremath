# APERY_GAP — the second-order gap is closed

**Author:** mathematician-agent (River's odd-zeta program), 2026-07-26
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, code in `work/apgap/` (reuses `work/apdef/`)
**Labels:** `[PROVED]` · `[VERIFIED range]` · `[CONJECTURAL]`
All arithmetic exact (`fractions.Fraction` / Python ints). No floating point anywhere.
Reference: `work/APERY_DEFECT.md` §9 C2 — the open item this note closes.

---

## 0. HEADLINE

**The gap of `APERY_DEFECT` §9 C2 is closed. The two-level digit law mod `p³` is a
theorem, and so is the `1, 1` part of the C2 rank profile.**

> **THEOREM.** Let `p ≥ 5` be prime and `n = ap + r` with `0 ≤ a, r < p`. Then
> **`( a_n , p³b_n ) ≡ ( a_a , b_a ) · u(a,r)  (mod p³)`**
> **`u(a,r) = a_r + 2p·a·U_r + p²a²·X_p(r) = [ Σ_{s=0}^{p−1} A_Γ(r+ε, s) ]_{ε = pa}`** truncated at `ε²`.

The route that worked is **(c)**, the residue route, and it worked *twice*. Everything
reduces to one rational function

> **`g_r(z) = [ (z+1)(z+2)···(z+r) / ( z(z−1)···(z−r) ) ]²`**,  `A_Γ(r,z) = (sin²πz/π²)·g_r(z)`

and three facts about it:

| fact | statement | gives |
|---|---|---|
| **(i)** | `Σ_s Res_{z=s} g_r = 0` | `V_r = 0` — the *first*-order degeneracy (already `[PROVED]`, §3.2) |
| **(ii)** | `Σ_s Res_{z=s} h_r = 0`, `h_r = 4 g_r(z)·Σ_{i=1}^r 1/(z+i)` | **R1**: `Σ_ac = −2Σ_c²` **over ℚ** |
| **(iii)** | `Σ_{s≤r} FP_s(g_r) + Σ_{t=r+1}^{p−1} g_r(t) ≡ 0 (mod p)` | **R2**: `Σ_c² ≡ −Ξ_p(r)` |

(i) and (ii) are the residue theorem; (iii) is the residue theorem's mod-`p` shadow
(`Σ_{w∈F_p^×} w^{-1} = Σ_{w∈F_p^×} w^{-2} = 0`). **The borrow region is exactly the
complement of the pole set of `g_r` inside `F_p`**: `g_r(r+m) = C(r,m)`, the `ε²` weight
of the digit `s = r+m > r`. That is the whole mechanism — the "cancellation between
region I and the borrow region" is the statement that the finite parts at the poles
`{0,…,r}` and the values at the non-poles `{r+1,…,p−1}` add to zero over `F_p`.

**One correction first.** `APERY_DEFECT` §9, `apdef/channels.py`, and
`papers_out/frobenius_matrix/main.tex` all print the `c²` channel with the wrong sign:

```
  printed :  c²: 2v² − ( H²_{r+s} − 2H²_s + H²_{r−s} )      <- WRONG
  correct :  c²: 2v² − ( H²_{r+s} − 2H²_s − H²_{r−s} )
```

because `[c²]Λ₂ = [c²]( (a+c)²H²_{r+s} − 2c²H²_s − (a−c)²H²_{r−s} ) = H²_{r+s} − 2H²_s − H²_{r−s}`.
With the correct sign the `c²` sums are `0, 13, 905/4, 167965/36, …` (not `0, 11, 607/4, …`)
and the exact rational identity `Σ_ac + 2Σ_c² = 0` appears. The recorded conclusion of
§9 is unaffected — the two channels still fail to vanish over ℚ — but the *typo hid the
identity*, which is the reason the gap looked harder than it is.

---

## 1. The exact digit factorisation `[PROVED]`

Write, for `M, t ≥ 0`,

```
  R(M,t) := Π_{i=1}^{t} (Mp + i) = t! · Π_{i≤t} (1 + Mp/i)
  W(M)   := Π_{j=0}^{M-1} Π_{i=1}^{p-1} (jp + i)
```

so that `(Mp)! = p^M M! W(M)` and hence, **for every `t ≥ 0`** (no `t < p` needed —
`R(M,t)` is just the product of the consecutive integers `Mp+1 … Mp+t`):

> **`(Mp + t)! = p^M M! W(M) R(M,t)`.**  `(1.1)`

**Lemma A (Wolstenholme block).** For `p ≥ 5`, `W(M) ≡ ((p−1)!)^M (mod p³)`.
*Proof.* `Π_{i<p}(jp+i) = (p−1)!·Π_{i<p}(1+jp/i) = (p−1)!(1 + jpH_{p−1} + ½j²p²(H_{p−1}² − H^{(2)}_{p−1}) + …)`.
Wolstenholme gives `H_{p−1} ≡ 0 (p²)` and `H^{(2)}_{p−1} ≡ 0 (p)`, so every correction is
`O(p³)`; multiply the `M` blocks. ∎

**Lemma B (exact factorisation).** For `0 ≤ c ≤ a < p` and `0 ≤ s ≤ r < p`, with no
restriction whatever on `r+s` or `a+c`,

> **`A(ap+r, cp+s) = A(a,c)·A(r,s)· [W(a+c)/(W(c)²W(a−c))]² · 𝓡(a,c;r,s)`**
> **`𝓡 = [ Π_{i≤r+s}(1 + (a+c)p/i) / ( Π_{i≤s}(1 + cp/i)² · Π_{i≤r−s}(1 + (a−c)p/i) ) ]²`**

*Proof.* Apply `(1.1)` to each factorial in
`C(ap+r,cp+s) = C(a,c)·W(a)/(W(c)W(a−c))·R(a,r)/(R(c,s)R(a−c,r−s))` and
`C((a+c)p+r+s, cp+s) = C(a+c,c)·W(a+c)/(W(c)W(a))·R(a+c,r+s)/(R(c,s)R(a,r))`;
`A` is the square of their product, the `R(a,r)` cancels, and
`(r+s)!/(s!²(r−s)!) = C(r,s)C(r+s,s)` so the `t!`-parts assemble to `A(r,s)`. ∎
By Lemma A the `W`-bracket is `1 + O(p³)` and may be dropped mod `p³`.

The `p`-adic expansion of `𝓡` is **not uniform**: the factor at `i = p` is `1 + (a+c)`,
not `1 + O(p)`. That single factor is the entire borrow/carry phenomenon.

### 1.1 The four regions, mod `p³` `[PROVED; VERIFIED 1,087,029 cells]`

Put `u = H_{r+s} − H_{r−s}`, `v = H_{r+s} + H_{r−s} − 2H_s`, `Λ₁ = au + cv`,
`Λ₂ = (a+c)²H^{(2)}_{r+s} − 2c²H^{(2)}_s − (a−c)²H^{(2)}_{r−s}`, and

```
  D(r,s) := A(r,s)/p²   (s ≤ r, r+s ≥ p)         C(r,m) := ( (2r+m)!(m−1)!/((r+m)!)² )²
```

| region | condition | `A(ap+r, cp+s) ≡ … (mod p³)` |
|---|---|---|
| **I** | `s ≤ r`, `r+s < p` | `A(a,c)A(r,s)( 1 + 2pΛ₁ + p²(2Λ₁² − Λ₂) )` |
| **II-a** *(carry)* | `s ≤ r`, `r+s ≥ p` | `p²·A(a,c)·(1+a+c)²·D(r,s)` |
| **II-b** *(borrow)* | `s = r+m`, `m ≥ 1`, `2r+m < p` | `p²·(a−c)²·A(a,c)·C(r,m)` |
| dead | `s > r`, `r+s ≥ p` | `0` (`v_p ≥ 4`); and `A = 0` if `c > a` |

*Proofs.* **I**: `r+s < p` makes every `H_t`, `H^{(2)}_t` in Lemma B `p`-integral, so
`log 𝓡 = 2pΛ₁ − p²Λ₂ + O(p³)`. **II-a**: exactly one multiple of `p` lies in `[1, r+s]`
(namely `p`, since `p ≤ r+s ≤ 2p−2`), so `v_p(A(r,s)) = 2` and `𝓡 = (1+a+c)²(1+O(p))`;
`D(r,s) ≡ ( (r+s−p)! / (s!²(r−s)!) )² (mod p)`. **II-b**: `n−k = (a−c−1)p + (p−m)`, so
`(1.1)` gives `p^{-1}C(ap+r,cp+r+m) ≡ (−1)^{m+1}(a−c)C(a,c)·r!(m−1)!/(r+m)!` using
`(p−m)! ≡ (−1)^m/(m−1)!`, while `C(n+k,k) ≡ C(a+c,c)C(2r+m,r+m)`; squaring and using
`(r!(m−1)!/(r+m)!)²·C(2r+m,r+m)² = C(r,m)` gives the entry. **dead**: two carries. ∎

`t_cellwise.py`, `t_sweep.py cells`: **0 failures in 1,087,029 cells**, `p = 5…31`, every
`(a,c,r,s)`.

Note `C(r,m) ≡ 0 (mod p²)` when `2r+m ≥ p` (one `p` in `(2r+m)!`, none in `(r+m)!`,
`(m−1)!`), so the II-b range may be enlarged to `1 ≤ m ≤ p−1−r` without changing anything
mod `p` — that is the range `Adig` uses.

---

## 2. The assembly, and what the gap really is `[PROVED]`

Let `ω : {0,…,a} → ℤ_(p)` be any `p`-integral weight and `m_j = Σ_c c^j A(a,c)ω(c)`.
Set `T_ω = Σ_{c,s} ω(c) A(ap+r, cp+s)`. Then `T_1 = a_{ap+r}`, and since
`H^{(3)}_{ap+r} = p^{-3}H^{(3)}_a + G_{ap+r}` with `G` `p`-integral,
`T_{2H³_a − H³_c} ≡ p³b_{ap+r} (mod p³)`. So **both rows are the same computation with
different weights.**

Write `S_< = {s ≤ r : r+s < p}`, `S_≥ = {s ≤ r : r+s ≥ p}`, and

```
  Σ_a²(r) = Σ_{s≤r} A(r,s)( 2u² − (H²_{r+s} − H²_{r−s}) )
  Σ_ac(r) = Σ_{s≤r} A(r,s)( 4uv − 2(H²_{r+s} + H²_{r−s}) )
  Σ_c²(r) = Σ_{s≤r} A(r,s)( 2v² − (H²_{r+s} − 2H²_s − H²_{r−s}) )      <- corrected sign
  Δ_r     = Σ_{s∈S_≥} A(r,s)/p²         Ξ_p(r) = Σ_{m=1}^{p−1−r} C(r,m)
```

(all three `Σ`'s are `p`-integral for `p > r`: on `S_≥` the `p^{-2}` of the bracket meets
the `v_p = 2` of `A(r,s)`.)

**Step 1 (first order carries a correction).** On `S_≥`, `u = 1/p + O(1)` and
`v = 1/p + O(1)`, so with `U^<_r = Σ_{S_<}A(r,s)u` and `V^<_r = Σ_{S_<}A(r,s)v`:

> `U^<_r ≡ U_r − pΔ_r`,  `V^<_r ≡ V_r − pΔ_r = −pΔ_r` (mod `p²`),  using **`V_r = 0`** (§3.2).

**Step 2 (the three `Σ`'s lose the same amount).** On `S_≥` the leading `p^{-2}` of the
three channel brackets is `1, 2, 1` respectively, so

> `Σ^<_a² ≡ Σ_a² − Δ`, `Σ^<_ac ≡ Σ_ac − 2Δ`, `Σ^<_c² ≡ Σ_c² − Δ` (mod `p`).

**Step 3 (collect).** Region I contributes `m_0 a_r + 2p[a m_0 U^< + m_1 V^<] + p²[a²m_0Σ^<_a² + a m_1Σ^<_ac + m_2Σ^<_c²]`
minus the `S_≥` part of `m_0 a_r`; region II-a contributes `p²[(a+c)²+2(a+c)]`-weighted `Δ`;
region II-b contributes `p²(a²m_0 − 2am_1 + m_2)Ξ`. The `Δ`-terms cancel **identically**:

```
  −2(a m_0 + m_1)            (Step 1)
  −(a²m_0 + 2a m_1 + m_2)    (Step 2)
  +(a²m_0 + 2a m_1 + m_2 + 2a m_0 + 2m_1)   (region II-a)   =  0
```

> **PROPOSITION 2.1.** For every `p ≥ 5`, `a, r < p`, and every `p`-integral weight `ω`,
> **`( T_ω − m_0(a_r + 2p·a·U_r) ) / p² ≡ a²m_0·Σ_a² + a·m_1·Σ_ac + m_2·Σ_c² + (a²m_0 − 2a·m_1 + m_2)·Ξ_p(r)  (mod p)`**

`[PROVED above; VERIFIED 0 failures, p = 5…31, all (a,r), both weights — t_regions.py, t_sweep.py d2]`

Since `X_p(r) := [ε²]Σ_{s=0}^{p−1}A_Γ(r+ε,s) = Σ_a²(r) + Ξ_p(r)`, the target
`T_ω − m_0(a_r + 2paU_r) ≡ p²·a²·m_0·X_p(r)` is **equivalent** to

> **`a·m_1·( Σ_ac − 2Ξ_p(r) ) + m_2·( Σ_c² + Ξ_p(r) ) ≡ 0 (mod p)`  for all `a`.**  `(*)`

The vectors `( a·m_1(a), m_2(a) )_{a<p}` span `F_p²` at all 13 primes, for both weights
(`t_necessity.py`), so `(*)` is **equivalent** to the pair

> **R1.  `Σ_ac(r) = −2 Σ_c²(r)`  — an identity over ℚ**
> **R2.  `Σ_c²(r) ≡ − Ξ_p(r)  (mod p)`**

*That is the gap, in its sharpest form.* Both are now proved.

---

## 3. The rational function `g_r` `[PROVED]`

**Lemma C (reflection, rational form).** For `r ∈ ℤ_{≥0}`,

> **`A_Γ(r,z) = (sin²πz / π²)·g_r(z)`,  `g_r(z) = [ Π_{i=1}^{r}(z+i) / Π_{j=0}^{r}(z−j) ]²`**

*Proof.* `Γ(r+z+1)/Γ(z+1) = Π_{i≤r}(z+i)`; `Γ(r−z+1) = Π_{l=1}^{r}(l−z)·Γ(1−z)`;
`Γ(z+1)Γ(1−z) = πz/sin πz`. Hence
`Γ(r+z+1)/(Γ(z+1)²Γ(r−z+1)) = (sin πz/π)·(−1)^r Π_i(z+i)/Π_{j=0}^r(z−j)`; square. ∎

So `g_r` is a **rational function** of degree `2r − (2r+2) = −2`, with double poles exactly
at `z = 0,1,…,r` and no others. (This replaces the Γ-asymptotics of §3.2 by an identity.)

**Lemma D (local dictionary).** If `f = α/(z−s)² + β/(z−s) + γ + O(z−s)` at an integer `s`
and `Φ = (sin²πz/π²)f`, then `Φ` is regular at `s` and
`Φ(s) = α`, `Φ'(s) = β`, `½Φ''(s) = γ − (π²/3)α`,
because `sin²πz/π² = (z−s)² − (π²/3)(z−s)⁴ + O((z−s)⁶)`. ∎

Applying Lemma D to `f = g_r` and writing `α_s, β_s, γ_s` for its Laurent data at `z = s`:

| | value | meaning |
|---|---|---|
| `α_s` | `A(r,s)` | the summand |
| `β_s = Res_{z=s} g_r` | `2A(r,s)·v(r,s)` | `Σ_s β_s = 2V_r` |
| `γ_s = FP_{z=s} g_r` | `A(r,s)·( 2v² − (H²_{r+s} − 2H²_s − H²_{r−s}) )` | **`Σ_s γ_s = Σ_c²(r)`** |
| `g_r(r+m)`, `m ≥ 1` | `( (2r+m)!(m−1)!/((r+m)!)² )² = C(r,m)` | **the borrow weight** |

(the `π²/3 = 2ζ(2)` of Lemma D cancels the `ζ(2)` of `∂_k²log A_Γ` exactly, which is why
`γ_s` is the clean `c²`-channel and not a `ζ(2)`-shifted version).
`[VERIFIED exact over ℚ, r ≤ 40, all s — t_residues.py F1,F2,F3]`

`g_r(r+m) = C(r,m)` is immediate from the product form:
`Π_{i≤r}(r+m+i)/Π_{j≤r}(r+m−j) = ((2r+m)!/(r+m)!)/((r+m)!/(m−1)!)`.

### 3.1 R1 `[PROVED]`

**THEOREM R1.** `Σ_ac(r) + 2·Σ_c²(r) = 0` for every `r ≥ 0`.

*Proof.* Expanding the three channels as second derivatives of `A_Γ`,
`Σ_ac + 2Σ_c² = Σ_{s=0}^{r} [ ∂_n∂_k + ∂_k² ] A_Γ (r,s) = Σ_s ∂_k[(∂_n + ∂_k)A_Γ](r,s)`
(the `ζ(2)`-terms of `∂_n∂_k` and `∂_k²` enter with weights `4` and `2·(−2)`, and cancel;
this is exactly why *this* combination, and no other, is `ζ(2)`-free).

Now `A_Γ(n,z) = (sin²π(z−n)/π²)·g_n(z)` with `g_n(z) = Γ(n+z+1)²Γ(z−n)²/Γ(z+1)⁴`, and
**`sin²π(z−n)` is invariant along `(n,z) ↦ (n+t, z+t)`**, so

```
  (∂_n + ∂_z) A_Γ = (sin²π(z−n)/π²) · (∂_n + ∂_z) g_n ,
  (∂_n + ∂_z) log g_n = [2ψ(n+z+1) − 2ψ(z−n)] + [2ψ(n+z+1) + 2ψ(z−n) − 4ψ(z+1)]
                      = 4[ψ(n+z+1) − ψ(z+1)] .
```

**The `ψ(z−n)` cancels** — this is the point. At `n = r ∈ ℤ`,
`ψ(r+z+1) − ψ(z+1) = Σ_{i=1}^{r} 1/(z+i)` is rational, so

> **`h_r(z) := (∂_n + ∂_z)g_n(z)|_{n=r} = 4·g_r(z)·Σ_{i=1}^{r} 1/(z+i)`  is a rational function.**

Its poles: at `z = 0,…,r` of order 2 (the `Σ 1/(z+i)` is regular there); at `z = −i`
(`1 ≤ i ≤ r`) the simple pole meets the double zero of `g_r`, so `h_r` is regular; nowhere
else. And `h_r = O(z^{-2})·O(z^{-1}) = O(z^{-3})`. By Lemma D (applied to `h_r`, order ≤ 2),
`∂_z[(∂_n+∂_z)A_Γ](r,z)|_{z=s} = Res_{z=s} h_r`. A rational function that is `O(z^{-2})` at
infinity has residue sum `0`. Hence `Σ_ac + 2Σ_c² = Σ_{s=0}^{r} Res_{z=s} h_r = 0`. ∎

`[VERIFIED exact over ℚ, r = 0…40, 0 failures: both `Res_s h_r = A(r,s)(ch_ac + 2ch_c²)`
cell-by-cell and the sum — t_residues.py F4; and `Σ_ac + 2Σ_c² = 0` directly, t_reduce.py]`

*Example `r = 1`:* `h_1 = 4(z+1)/(z²(z−1)²)`, residues `+12` at `0` and `−12` at `1`;
and indeed `A(1,0)(ch_ac+2ch_c²) = 1·(−4+16) = 12`, `A(1,1)(…) = 4·(−11/2+5/2) = −12`.

### 3.2 R2 `[PROVED]`

**LEMMA E (mod-`p` finite-part sum).** Let `p ≥ 5`, `0 ≤ r < p`, and let `f ∈ ℚ(z)` have
partial-fraction expansion `f(z) = Σ_{s=0}^{r} [ α_s/(z−s)² + β_s/(z−s) ]` with all
`α_s, β_s ∈ ℤ_(p)` (equivalently: `deg f ≤ −2`, poles only at `0,…,r`, of order ≤ 2, with
`p`-integral principal parts). Let `γ_s = FP_{z=s} f`. Then

> **`Σ_{s=0}^{r} γ_s + Σ_{t=r+1}^{p−1} f(t) ≡ 0 (mod p)`.**

*Proof.* `γ_s = Σ_{s'≠s}[ α_{s'}/(s−s')² + β_{s'}/(s−s') ]` and, for `t ∉ {0,…,r}`,
`f(t) = Σ_{s'}[ α_{s'}/(t−s')² + β_{s'}/(t−s') ]`. Every summand is `p`-integral
(`0 ≤ y, s' ≤ p−1` gives `0 < |y − s'| < p`), so we may interchange:

```
  LHS = Σ_{s'=0}^{r} [ α_{s'} · Σ_{y=0, y≠s'}^{p−1} 1/(y−s')²  +  β_{s'} · Σ_{y≠s'} 1/(y−s') ].
```

For fixed `s'`, `y − s'` runs over a complete set of nonzero residues mod `p`. Hence mod `p`
the inner sums are `Σ_{w∈F_p^×} w^{-2} = Σ_{w=1}^{p−1} w² = (p−1)p(2p−1)/6 ≡ 0` (needs `p ≥ 5`)
and `Σ_{w∈F_p^×} w^{-1} = Σ_{w=1}^{p−1} w ≡ 0` (needs `p ≥ 3`). ∎

**THEOREM R2.** For `p ≥ 5` and `0 ≤ r < p`,  `Σ_c²(r) + Ξ_p(r) ≡ 0 (mod p)`.

*Proof.* Take `f = g_r` in Lemma E. Hypotheses: `deg g_r = −2`; poles exactly the double
poles at `0,…,r` (Lemma C); `α_s = A(r,s) ∈ ℤ`; `β_s = 2A(r,s)v(r,s) ∈ ℤ_(p)` — the only
`p` in a denominator is the `1/p` of `H_{r+s}` when `r+s ≥ p`, and then `v_p(A(r,s)) = 2`.
By the dictionary of §3, `Σ_s γ_s = Σ_c²(r)` and `Σ_{t=r+1}^{p−1} g_r(t) = Σ_{m=1}^{p−1−r} C(r,m) = Ξ_p(r)`. ∎

`[VERIFIED 0 failures, 323 cells: 13 primes 5 ≤ p ≤ 47, every r < p — t_residues.py F5,
and independently on Σ_c² itself, t_reduce.py]`

**Reading.** `{0,…,r}` are the poles of `g_r`; `{r+1,…,p−1}` is the rest of `F_p`; the
first set is region I's digit range and the second is the borrow range. R2 says the
*finite parts on the pole set cancel the values off it, over `F_p`* — the borrow region is
literally the complement of the pole divisor. That is why the vanishing is a mod-`p`
statement and cannot be an identity over ℚ.

---

## 4. THE THEOREM

> **THEOREM 4.1 (two-level digit law mod `p³`).** Let `p ≥ 5` be prime and `n = ap + r`
> with `0 ≤ a, r < p`. Then
>
> **`( a_n , p³b_n ) ≡ ( a_a , b_a ) · u(a,r)  (mod p³)`**
>
> **`u(a,r) = a_r + 2p·a·U_r + p²·a²·X_p(r)`**
>
> **`U_r = Σ_{s=0}^{r} A(r,s)(H_{r+s} − H_{r−s})`**
> **`X_p(r) = Σ_{s=0}^{r} A(r,s)( 2u² − (H^{(2)}_{r+s} − H^{(2)}_{r−s}) ) + Σ_{t=r+1}^{p−1} g_r(t)`**
>
> equivalently `u(a,r) = [ Σ_{s=0}^{p−1} A_Γ(r+ε, s) ]_{ε = pa}` truncated at order `ε²`.

*Proof.* Proposition 2.1 with `ω = 1` and `ω = 2H^{(3)}_a − H^{(3)}_c`; then R1 and R2
turn the residual `a·m_1(Σ_ac − 2Ξ) + m_2(Σ_c² + Ξ)` into `(−2a m_1 + m_2)(Σ_c² + Ξ) ≡ 0`.
The `mod p²` truncation is `APERY_DEFECT` §4.1 (which used `V_r = 0`); the `mod p³`
statement is the new content. ∎

> **COROLLARY 4.2 (C2, orders `p` and `p²`).** The digit defect of the ζ(3) Apéry pair has
> rank **≤ 1** at first order and rank **≤ 1** at second order, both rows, with
> *`a`-side factor exactly `a·(a_a | b_a)` resp. `a²·(a_a | b_a)`* and the **same `r`-side
> vector for both rows** — `(U_r)_r` at first order, `(X_p(r))_r` at second. Rank is
> exactly `1` iff the respective `r`-vector is `≢ 0`, which holds at all 13 primes tested.

`[PROVED]` — this was `[VERIFIED, 13 primes]` in `APERY_DEFECT` §2, §4.2 and C2.

> **COROLLARY 4.3.** `X_p(r) ≡ [ε²] Adig(p,r)` for all `p ≥ 5`, `r < p` (was
> `[VERIFIED, p = 5…23]`, §4.3), and the *restricted* deformation `Σ_{s≤r}` must saturate
> at depth 2: its `[ε²]` is `Σ_a²(r)`, and `Σ_a² ≢ X_p` exactly because `Ξ_p(r) ≢ 0`.

**Still `[CONJECTURAL]`:** only the `mod p⁴` cross-term statement, C1's off-diagonal
`p³b_r`. §5 of `APERY_DEFECT` derives the entry; what is unproved is that the residual
scalar defect at order `p³` is what it is. Theorem 4.1 does not touch it.

---

## 5. Verification record

All exact; `[VERIFIED range]` means 0 failures over the stated range.

| # | statement | range | cells | failures |
|---|---|---|---|---|
| S1 | the four regional formulas for `A(ap+r,cp+s)` mod `p³` | `p = 5…31`, all `(a,c,r,s)` | 1,087,029 | **0** |
| S2 | Proposition 2.1, a-row **and** b-row | `p = 5…31`, all `(a,r)` | 6,690 | **0** |
| F1 | `g_r(r+m) = C(r,m)` | `r ≤ 40`, `m ≤ 11` | 451 | **0** |
| F2 | `FP_s g_r = A(r,s)·ch_c²`, `Σ_s FP_s = Σ_c²` | `r ≤ 40`, all `s` | 861 + 41 | **0** |
| F3 | `Res_s g_r = 2A(r,s)v`, `Σ_s = 2V_r = 0` | `r ≤ 40`, all `s` | 861 + 41 | **0** |
| F4 | `Res_s h_r = A(r,s)(ch_ac + 2ch_c²)`, `Σ_s = 0` (**R1**) | `r ≤ 40`, all `s` | 861 + 41 | **0** |
| R1 | `Σ_ac + 2Σ_c² = 0` over ℚ | `r = 0…40` | 41 | **0** |
| F5/R2 | `Σ_c² + Ξ_p ≡ 0 (mod p)` | 13 primes `5 ≤ p ≤ 47`, all `r` | 323 | **0** |
| C1 | `X_p(r) ≡ [ε²]Adig(p,r)` | 13 primes, all `r` | 323 | **0** |
| C2 | `v_p(a_{ap+r} − a_a·u) ≥ 3`, floor **exactly 3** | 13 primes, all `a≥1, r` | 10,130 | **0** |
| C3 | `v_p(p³b_{ap+r} − b_a·u) ≥ 3`, floor **exactly 3** | 13 primes | 10,130 | **0** |
| C4 | 2nd-order defect: rank **exactly 1**, both rows, same `r`-space, equals `a²(a_a\|b_a)X_p(r)` cell-by-cell | 13 primes | 20,260 | **0** |
| N | `{(a·m₁(a), m₂(a))}` spans `F_p²` (⇒ R1,R2 necessary) | 13 primes, both weights | 26 | rank 2 always |

Primes used: `5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47`.

**Negative bound recorded.** R1 is an identity over ℚ; R2 is **not** — `Σ_c²(r)` is a fixed
nonzero rational (`13, 905/4, 167965/36, …` for `r ≥ 1`) while `Ξ_p(r)` is `p`-dependent, so
no rational identity can replace R2. Equally, no *sub*-sum works: dropping the borrow
region makes `Ξ = 0` and R2 fails at every `p` and every `1 ≤ r ≤ p−1` with `Σ_c²(r) ≢ 0`.

---

## 6. Files (`work/apgap/`)

| file | what |
|---|---|
| `gap_core.py` | channels (corrected `c²` sign), `C(r,m)`, `Ξ_p`, `Δ_r`, weighted moments, `U_r`, `V_r` |
| `t_cellwise.py` | §1.1, the four regional formulas, cell by cell |
| `t_regions.py` | §2, Proposition 2.1 against the measured `D2` |
| `t_reduce.py` | §2, the reduction to R1 and R2 |
| `t_residues.py` | §3, `g_r`, `h_r`, the local dictionary, F1–F5 |
| `t_final.py` | §4, Theorem 4.1 and Corollaries 4.2–4.3, 13 primes |
| `t_sweep.py` | §5, the 0-failure sweeps to `p = 31`, all cells, both rows |
| `t_necessity.py` | §2, the span check making R1,R2 necessary |

---

## 7. What to change in `papers_out/frobenius_matrix/main.tex`

(River edits the paper; this is the list.)

1. **Fix the `c²` channel sign** in §"The remaining gap": `− H^{(2)}_{r−s}`, not `+`.
   The quoted `c²` values `0, 11, 607/4` become `0, 13, 905/4`.
2. **Lemma \ref{lem:exp} generalises**: Lemma B here is exact and needs no
   `r+s < p`, `a+c < p`; state it that way and the mod-`p³` expansion follows by
   isolating the single factor `i = p`.
3. **Theorem \ref{thm:V} gets a shorter proof**: `A_Γ(r,z) = (sin²πz/π²)g_r(z)` with `g_r`
   the explicit *rational* function of Lemma C; the Γ-asymptotics paragraph is unnecessary.
4. **Observation \ref{obs:scalar} and Observation \ref{obs:rank} become theorems**
   (Theorem 4.1, Corollary 4.2 above); §"The remaining gap" is replaced by §3 above.
5. **Conjecture \ref{conj:matrix}** survives only as the `mod p⁴` cross-term statement;
   its diagonal is now proved.

---

## 8. `p = 2` and `p = 3` `[VERIFIED, exhaustive]`

**The conclusion holds. Every step of the proof fails. The conclusion holds only
because at these primes there are not enough digits to detect the failure.**

Tests: `t_small_primes.py`, `t_small_primes2.py`, `t_p23.py`.

### 8.1 The conclusion

Theorem 4.1 has `p²` admissible cells per row (`0 ≤ a, r < p`), so `4` at `p = 2` and
`9` at `p = 3`. Over *every* one of them, both rows:

| `p` | cells (both rows, `a ≥ 1`) | `min v_p(LHS − RHS)` | claimed | verdict |
|---|---|---|---|---|
| 2 | 4 | 4 | ≥ 3 | holds, **with slack** |
| 3 | 12 | 3 | ≥ 3 | holds, **tight** (floor exactly 3, as at `p ≥ 5`) |

The first-order law (`mod p²`) and Lucas (`mod p`) likewise hold at both primes.
So `p = 2, 3` are **not counterexamples**.

The sample cannot be enlarged: allowing `a ≥ p` breaks the law at *every* prime
(`t_small_primes2.py`, `a ≤ 60`: min `v_p` reaches `−10` at `p = 2`, `−5` at `p = 3`,
`−3` at `p = 5, 7`, `0` at `p = 11` — the `b`-row `b_a` stops being `p`-integral). The
single-digit restriction `a < p` is load-bearing at all primes, not just small ones.

### 8.2 The proof, layer by layer

| layer | `p = 2` | `p = 3` | `p = 5, 7` |
|---|---|---|---|
| **Lemma A** `W(M) ≡ ((p−1)!)^M (p³)` | **FAILS** | **FAILS** | holds |
| **Lemma E** `Σ_{F_p^×} w^{−1} ≡ 0` | **FAILS** (`= 1`) | holds | holds |
| **Lemma E** `Σ_{F_p^×} w^{−2} ≡ 0` | **FAILS** (`= 1`) | **FAILS** (`= 2`) | holds |
| **S1** four regional formulas | 0 bad | **4 bad cells** | 0 bad |
| **Prop 2.1** the assembly | 0 bad | **6 bad cells** | 0 bad |
| **R1** `Σ_ac + 2Σ_c² = 0` over ℚ | holds | holds | holds |
| **R2** `Σ_c² + Ξ_p ≡ 0 (p)` | **FAILS, every `r`** | **FAILS, every `r`** | holds |
| **N** rank of `{(a·m₁(a), m₂(a))}` in `F_p²` | **0** | **1** | **2** |
| **Theorem 4.1** | 0 bad | 0 bad | 0 bad |

`R1` is the only survivor, and it is the only `p`-free statement in the list.

**R2's failure, explicitly.** `Σ_c²(r) = 0, 13, 905/4` and `Ξ_p(r)` as below, so

```
  p = 2:  Σ_c² + Ξ ≡ 1, 1        (mod 2)      [wants 0, 0]        Ξ_2 = 1, 0
  p = 3:  Σ_c² + Ξ ≡ 2, 1, 2     (mod 3)      [wants 0, 0, 0]     Ξ_3 = 5/4, 9/4, 0
```

**S1's failure, explicitly.** At `p = 3` the bad cells are exactly
`(a,c,r,s) = (1,1,0,0), (1,1,1,0), (1,1,1,1), (1,1,2,0)` — every one of them has
`a = c = 1`, i.e. `a + c = 2`, so the `W`-bracket of Lemma B is `W(2)/(W(1)²W(0))` and
`W(2) − (2!)² = 40 − 4 = 36`, `v₃ = 2 < 3`. The failures are *precisely* the cells where
the Wolstenholme block is needed and is unavailable.

### 8.3 Why the conclusion survives anyway

Two independent reasons, both of them "too few digits":

1. **The obstruction cannot be probed.** By §2 the theorem is equivalent to
   `a·m₁(Σ_ac − 2Ξ) + m₂(Σ_c² + Ξ) ≡ 0` for all `a`, and `R1, R2` are *necessary* only
   because the vectors `(a·m₁(a), m₂(a))`, `1 ≤ a < p`, span `F_p²`. There are `p − 1`
   such vectors: **one** at `p = 2` and **two** at `p = 3`, and their rank is `0` and `1`
   respectively, against `2` at all 13 primes `≥ 5`. `R2` is false at `p = 2, 3` and the
   theorem does not notice.
2. **The surviving direction is covered by a second failure.** At `p = 3, a = 1` the
   coefficient `(−2a·m₁ + m₂) ≡ 2 ≢ 0` and `Σ_c² + Ξ ≢ 0`, so reason 1 alone does not
   suffice — and indeed Prop 2.1 fails at exactly those cells (`v₃ = 0` for `a = 1`, all
   `r`). The failure of S1/Lemma A and the failure of R2 cancel. On 6 cells that is not a
   phenomenon; it is a coincidence with nowhere to hide.

**Conclusion to record.** `p ∈ {2,3}` are neither counterexamples nor instances: they are
*below the resolution of the statement*. Theorem 4.1 should keep its `p ≥ 5` hypothesis —
not because `2, 3` violate it, but because nothing at `2, 3` is being asserted that has
content. This is a correction to the framing of `FROBENIUS_VIEWPOINT` §7 ("`p ∈ {2,3}` is
exactly where every congruence law fails"): here it is exactly where every *mechanism*
fails, while the law itself is untestable.
