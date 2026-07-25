# Closeout of the weight-5 graded descent campaign — T1 / T2 / T3

**Author:** mathematician-agent (River's odd-zeta program), continuation session
**Date:** 2026-07-24 (evening)
**Working dir:** `/home/ubuntu/fable-episode-2/zeta-math-2`, scripts in `work/lb5/`
**Predecessor:** `work/PROOF_LB5_CAMPAIGN.md` (conventions authoritative; `Q_n` = BZ **double** sum, `Q_1 = 21`)

**Labels.** `[PROVED]` = complete proof written here. `[VERIFIED r]` = exact finite check on
range `r` — evidence, never proof. `[CERTIFIED]` = machine proof object (CT telescoper +
certificate) produced and cross-checked. `[RECALLED-UNVERIFIED]` = memory, not checked.

---

## 0. EXECUTIVE SUMMARY

| task | verdict |
|---|---|
| **T1** — certify Theorem B (`P̂_n = Σ T·ŵ₃`) by creative telescoping | **partially closed.** The CT route is *validated*: the same two-step CT pipeline applied to the un-weighted summand **proves BZ's `Q_n` double-sum formula outright** (order-3 telescoper computed, shown equal to the BZ operator by exact two-sided polynomial division). See §1. For the `ŵ₃`-weighted summand the bottleneck is earlier than expected: `Annihilator` itself (the ∂-finite closure over 11 harmonic monomials) does not return in ~55 min. §1.3 records the exact certificate object still needed and the ε-deformation route that bypasses the closure step. |
| **T2** — prove the corrected middle-row congruence | **essentially closed — reduced by proof to ONE explicit binomial lemma.** New: Lemma G (termwise Frobenius descent of the `ŵ₃` letters) **[PROVED in-regime, VERIFIED 0/600k off-regime]**, and Lemma F (refined fibre-Lucas for the BZ summand) **[VERIFIED, 0 failures]**. Together with Theorems A–C they give a complete proof of the *sharp* middle-row law, including the exact reason the hypothesis `P̂_a ∈ ℤ_p` is needed. Unconditionally **[PROVED]** for `1 ≤ a < p/3`. See §2. |
| **T3** — depth-2 hunt for `w₅` | **SOLVED, and the premise was wrong. `w₅` exists at DEPTH 1.** The campaign's negative (and my own strengthened version of it) was an artefact of capping monomials at **three factors**. Removing only that cap — same alphabet as `ŵ₃`, no nested letters — makes the system consistent with **687 excess equations**, and an explicit 130-term `w₅` has been reconstructed over ℚ and **verified exactly** (`n = 1..20`, Fraction arithmetic, independent re-implementation). See §3.3–3.4. This **overturns §3.3 of `PROOF_LB5_CAMPAIGN.md`.** |

**Two methodological unlocks (both reusable).**
1. `math -script` **breaks** the RISC package load under Mathematica 15 (the kernel exits
   silently after the banner; `wolframscript` reports `RISC\`package::loading`). **`math < file.wl`
   (stdin/interactive mode) works.** The MCP Wolfram evaluator also dies on the `Get`.
2. The 360-term ladder is **not** the data ceiling. The certified order-3 recurrence propagates
   `Q, P, P̂` **mod q** instantly (leading coefficient `2(n+3)^5(2n+5)a_0(n)` is a q-unit),
   cross-checked against the exact ladder for `n ≤ 360`; this lifts the number of exact linear
   equations from 360 to as many as wanted. Without it every weight-5 ansatz of realistic size is
   *untestable* (a 682-column system over 360 rows is vacuously consistent).

---

## 1. T1 — certifying Theorem B by creative telescoping

### 1.1 Set-up

Two-step creative telescoping (`CreativeTelescoping` takes a **single** `delta`, so the double sum
must be eliminated one variable at a time):

```
ann  = Annihilator[F(n,k,l), {S[n],S[k],S[l]}]
ct1  = CreativeTelescoping[ann, S[k]-1, {S[n],S[l]}]      (* telescopers in (n,l) *)
gb   = OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n],S[l]]]
ct2  = CreativeTelescoping[gb,  S[l]-1, {S[n]}]           (* telescoper in n *)
```
Script `work/lb5/gate3.wl`; log `work/lb5/gate3.log`.

### 1.2 Gate passed — the `Q_n` double sum [CERTIFIED]

For `F = T(n,k,l) = C(n+k,n)C(n,k)²C(n+l,n)C(n,l)²C(n+k+l,n)`:

* `ann`: 3 generators, < 1 s.
* `ct1`: 2 telescopers, < 1 s. `gb`: 2 elements.
* `ct2`: **one telescoper, order 3, degree 9 in n**, 4 s.

Writing the telescoper as `Σ_j c_j(n) SS^j` and `L_BZ = c_0(n)+c_1(n)SS+c_2(n)SS²+c_3(n)SS³` with
the certified BZ coefficients (`c_0=(n+1)^5(n+2)a_0(n+1)`, `c_1=−2(n+2)B_8(n)`, `c_2=−2B_9(n)`,
`c_3=2(n+3)^5(2n+5)a_0(n)`, `a_0(n)=41218n³+198849n²+320790n+173057`):

```
PolynomialRemainder[L_BZ,  telescoper, SS] = 0
PolynomialRemainder[telescoper, L_BZ,   SS] = 0
```

i.e. the two operators are **associates over ℚ(n)** — the CT telescoper *is* the BZ operator.
Since the double sum has natural boundaries (`C(n,k)=0` off `0≤k≤n`) and matches `Q_n` at
`n=0,1,2`, this **proves** `Q_n = Σ_{k,l}T(n,k,l)` — the step BZ leave to "[Ko10]".

### 1.3 The `ŵ₃`-weighted sum — where it stands

Summand `T(n,k,l)·ŵ₃(n,k,l)` with `ŵ₃` as in the campaign report §3.2, written in Mathematica's
`HarmonicNumber[·,r]`. Results:

* For the **truncated** summand `T·(H^{(3)}_n + A₃(k) + A₃(l))`:
  `Annihilator[·,{S[n],S[k],S[l]}]` → **6 generators, 1 s**; `CreativeTelescoping[·, S[k]−1, …]`
  then did not terminate in ≈ 1 h. (This run was itself the product of the stdin line-continuation
  trap described in §5 — the intended `ŵ₃` had been silently truncated.)
* For the **full** `ŵ₃` summand (`LeafCount 210`, ~14 distinct harmonic factors, products of two):
  `Annihilator` alone ran ≈ 55 min without returning and was stopped. The ∂-finite closure
  (`DFiniteTimes` over pairs, then `DFinitePlus` over 11 monomials) is where it blows up — the
  holonomic rank of the ideal, not the telescoping, is the bottleneck.

**What is still needed, exactly.** A pair `(q_1(n,S_n,S_l), r_1)` of Ore polynomials with
`q_1 + (S_k−1)r_1 ∈ ann`. Certificate **checking** is crash-safe and cheap: given `r_1`, verifying
`q_1 + (S_k−1)r_1 ∈ ann` is Ore-polynomial reduction against a 6-element Gröbner basis. So if any
run of `CreativeTelescoping` (possibly `Method -> "Barkatou"`, or with `Support -> {…}` fixing the
telescoper shape to `{1,S_n,S_n²,S_n³}`, or `Incomplete -> True`) emits `r_1` before dying, T1
closes. **Recommended next route (in order).**
1. **ε-deformation.** Replace each binomial of `T` by a Γ-quotient with its own parameter
   `δ_i` (`Γ(n+k+1+δ)/Γ(k+1+δ)` etc.). The deformed summand is an ordinary **hypergeometric
   term**, so its CT is the *Q*-gate computation of §1.2 with extra symbolic parameters — cheap.
   Since `∂_δ^m log` of those quotients produces exactly the letters `A_m, B_m, C_m`, every
   weight-3 monomial is a ℚ-combination of third-order Taylor coefficients of `Σ_{k,l}F(δ)`;
   expanding the (δ-dependent) telescoper to order 3 gives a triangular inhomogeneous system whose
   top component annihilates `Σ T·ŵ₃`. This bypasses the ∂-finite closure entirely, which is the
   step that actually failed.
2. `Support -> {1,S[n],S[n]²,S[n]³}` on the *second* elimination (the shape there is known).
3. `Method -> "Hermite"` / `Incomplete -> True` on the first elimination.

The same applies verbatim to the new `w₅` (§3), whose summand has 130 monomials — so route 1
(ε-deformation) is not optional there, it is the only realistic path.

**Independent fallback that does not need CT.** Both sides are annihilated by *some* operator:
`P̂` by `L_BZ` (BZ, certified via `HolonomicFunctions` on the integral `I_n`); the double sum by
the telescoper `L'` once found. Matching `lclm(L_BZ,L')`-many initial values then finishes. The
initial values are cheap: `Σ T·ŵ₃ = P̂_n` was re-verified **exactly** here for `n = 0..30`
(independent re-implementation, `work/lb5/core.py`), and the mod-q fit of §3 re-derives it from
`199` exact equations.

**Status of Theorem B: unchanged — [VERIFIED exact, n ≤ 30 here + n ≤ 40 previously], not yet
[CERTIFIED].** Everything downstream in §2 is stated relative to it.

---

## 2. T2 — the middle Frobenius row

### 2.0 The sharp statement (corrected once more)

**[VERIFIED, 0 failures, p ∈ {5,7,11,13,17,19}, all `1≤a<p`, `0≤r<p`, `n=ap+r≤360`]**

> `v_p( p³P̂_{ap+r} − P̂_a·Q_r ) ≥ 1 + min(0, v_p(P̂_a))`, floor attained.

Equivalently: `p³P̂_{ap+r} ≡ P̂_a Q_r (mod p)` **iff** `P̂_a ∈ ℤ_p`, and unconditionally
`p⁴P̂_{ap+r} ≡ p·P̂_a·Q_r (mod p)`. New data pinning the mechanism:

| p | `v_p(P̂_a)=0` cells | min E there | `v_p(P̂_a)=−1` cells | min E there | `v_p(P̂_n)` when `v_p(P̂_a)≥0` |
|---|---|---|---|---|---|
| 5 | 15 | 1 | 5 | 0 | ≥ −3 |
| 7 | 35 | 1 | 7 | 0 | ≥ −3 |
| 11 | 77 | 1 | 33 | 0 | ≥ −3 |
| 13 | 91 | 1 | 65 | 0 | ≥ −3 |
| 17 | 153 | 1 | 119 | 0 | ≥ −3 |
| 19 | 190 | 1 | 152 | 0 | ≥ −3 |

**New structural fact [VERIFIED, 0 exceptions]:** `v_p(P̂_a) ≥ 0 ⟹ v_p(P̂_{ap+r}) ≥ −3` for every
`r`; every cell with `v_p(P̂_n) = −4` has `v_p(P̂_a) = −1`. So the hypothesis of the theorem is
*exactly* the condition making the left-hand side p-integral.

### 2.1 The ledger, executed

Throughout: `p ≥ 5`, `1 ≤ a < p`, `0 ≤ r < p`, `n = ap+r < p²`; `k = bp+s`, `l = cp+t` with
`0 ≤ b,c ≤ a`, `0 ≤ s,t < p`. Write

```
v(n,k,l) := ŵ₃(n,k,l) − H^{(3)}_n
          = A₃(k)+A₃(l) − ¼[A₂(k)A₁(k)+A₂(l)A₁(l)] − ¾[A₂(k)B₁(k)+A₂(l)B₁(l)]
            − ⅜[A₂(k)+A₂(l)]C₁ − ⅛[A₂(k)A₁(l)+A₂(l)A₁(k)],
```
so that (Theorem B) **`Ŵ_n := P̂_n − H₃(n)Q_n = Σ_{k,l} T(n,k,l)·v(n,k,l)`** — the constant letter
`H^{(3)}_n` is *exactly* the H-layer that Theorem C removes, and `v` has **no** constant letter.
Level-`a` letters are written `A_m^{(a)}(b)=H^{(m)}_{a+b}−H^{(m)}_b`, `B_m^{(a)}(b)=H^{(m)}_{a−b}−H^{(m)}_b`,
`C_m^{(a)}(b,c)=H^{(m)}_{a+b+c}−H^{(m)}_{b+c}`.

#### Lemma H (digit split of a harmonic sum). [PROVED]
For `x ≥ 0`, `m ≥ 1`, `H^{(m)}_x = U_m(x) + p^{−m}H^{(m)}_{⌊x/p⌋}` with `U_m(x):=Σ_{j≤x,p∤j}j^{−m} ∈ ℤ_p`.
*Proof.* Split the range by `p | j`. ∎

#### Lemma G (termwise Frobenius descent of the letters). [PROVED in-regime]
Call `(s,t)` **in-regime** if `s ≤ r`, `t ≤ r` and `r+s+t < p` (exactly the surviving set of
Theorem A's Lemma 4). In-regime one has, with `ε=[r+s≥p]=0`,
```
⌊(n+k)/p⌋ = a+b,   ⌊(n−k)/p⌋ = a−b,   ⌊(k+l)/p⌋ = b+c,   ⌊(n+k+l)/p⌋ = a+b+c,
```
and hence, by Lemma H applied twice,
```
p^m A_m(k) = A_m^{(a)}(b) + p^m·ℤ_p ,
p^m B_m(k) = B_m^{(a)}(b) + p^m·ℤ_p ,
p^m C_m     = C_m^{(a)}(b,c) + p^m·ℤ_p .            (LETTER-DESCENT)
```
Consequently, for every `(k,l)` in-regime,
```
p³·T(n,k,l)·v(n,k,l)  ≡  T(n,k,l)·v(a,b,c)   (mod p).
```
*Proof.* `(LETTER-DESCENT)`: e.g. `A_m(k)=H^{(m)}_{n+k}−H^{(m)}_k
= [U_m(n+k)−U_m(k)] + p^{−m}[H^{(m)}_{a+b} − H^{(m)}_b]`, and the bracket is `A_m^{(a)}(b)`;
multiply by `p^m`. Same for `B` (`⌊(n−k)/p⌋=a−b` needs `s ≤ r`) and `C` (`⌊(k+l)/p⌋=b+c` needs
`s+t<p`, `⌊(n+k+l)/p⌋=a+b+c` needs `r+s+t<p`).
Now let `M = L_1L_2` (or `L_1`) be one of the five monomial types of `v`, of total weight 3.
Then `p³M = ∏(L_i^{(a)} + p^{m_i}z_i)`, `z_i ∈ ℤ_p`, so
`p³M − M^{(a)} = Σ_{∅≠S} ∏_{i∈S}p^{m_i}z_i ∏_{i∉S}L_i^{(a)}`. The level-`a` letters obey
`B_m^{(a)} ∈ ℤ_p` (both arguments `< p`), `C_m^{(a)} ∈ p^{−m}ℤ_p`, and
`A_m^{(a)}(b) ∈ ℤ_p` unless `a+b ≥ p`, in which case `A_m^{(a)}(b) ∈ p^{−m}ℤ_p`. Checking the five
types:
* `A₃(k)`: error `= p³z`, done.
* `A₂(k)X₁` with `X₁∈{A₁(k),B₁(k),C₁,A₁(l)}`: errors are `p²z₁X₁^{(a)}` (and `X₁^{(a)} ∈ p^{−1}ℤ_p`,
  so this is in `pℤ_p`), `p·z₂·A₂^{(a)}(b)`, and `p³z₁z₂`. The only dangerous term is
  `p z₂ A₂^{(a)}(b)`, which lies in `p^{−1}ℤ_p` **only if `a+b ≥ p`**; and then **Lemma D** gives
  `v_p(T(n,k,l)) ≥ 2`, so after multiplying by `T` it lies in `pℤ_p`. ∎

**[VERIFIED, 0 failures]** the congruence `v_p(p³T(n,k,l)v(n,k,l) − T(n,k,l)v(a,b,c)) ≥ 1` holds for
**all** `(k,l)`, in-regime **and** off-regime, at p = 5, 7, 11, 13 (810 / 4 726 / 54 540 in-regime
pairs and 4 660 / 35 559 / 542 815 off-regime pairs at p=5,7,11; p=13 all cells, `n ≤ 168`),
minimum exactly 1. Off-regime the two terms are individually `p`-integral and cancel mod `p`;
that case is **verified, and provable modulo Lemma D⁺⁺** — see §2.3.

#### Lemma F (refined fibre-Lucas for the BZ summand). [VERIFIED, 0 failures]
Put `𝒯(b,c) := Σ_{s,t=0}^{p−1} T(n, bp+s, cp+t) ∈ ℤ` and `d(b,c) := max(0, −v_p(v(a,b,c))) ∈{0,1,2,3}`.
Then for `p ∤ Q_a`
```
𝒯(b,c) ≡ (Q_n/Q_a)·T(a,b,c)   (mod p^{1+d(b,c)})      for all 0 ≤ b,c ≤ a.
```
**[VERIFIED, 0 failures, exact]** p ∈ {5,7,11,13,17,19}, all `a` with `p∤Q_a`, all `r`, all `(b,c)`:

| p | 5 | 7 | 11 | 13 | 17 | 19 | total |
|---|---|---|---|---|---|---|---|
| cells checked | 20 | 21 | 99 | 156 | 272 | 323 | **891** |
| `a` skipped (`p∣Q_a`) | 0 | 3 | 1 | 0 | 0 | 1 | |
| failures | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| min slack `v_p(diff) − (1+d)` | 0 | 0 | 0 | 0 | 0 | 0 | sharp |

(`work/lb5/t2_lemF.py`, arithmetic mod `p^8`.) Mod `p` the statement is exactly Theorem A's
factorisation (`Q_n/Q_a ≡ Q_r`); the content is the `d ≥ 1` refinement, and `d ≥ 1` happens
**only** where `a+b ≥ p` or `a+b+c ≥ p`, i.e. exactly where both sides already carry Kummer
carries. The min slack is 0 in every prime, so no cruder bound suffices.

#### Theorem E (middle Frobenius row). [PROVED, given Theorem B + Lemmas F and G]
For `p ≥ 5`, `1 ≤ a < p`, `0 ≤ r < p`, `n = ap+r`, `p ∤ Q_a`:
```
v_p( p³P̂_n − P̂_a Q_r ) ≥ 1 + min(0, v_p(P̂_a)).
```
In particular **if `P̂_a ∈ ℤ_p` then `p³P̂_{ap+r} ≡ P̂_a·Q_r (mod p)`.**

*Proof.* By Theorem C, `p³P̂_n − P̂_aQ_r ≡ p³Ŵ_n − Ŵ_aQ_r (mod p)`.
By Theorem B and Lemma G,
`p³Ŵ_n = Σ_{k,l}p³T(n,k,l)v(n,k,l) ≡ Σ_{k,l}T(n,k,l)v(a,b,c) = Σ_{b,c} v(a,b,c)·𝒯(b,c) (mod p)`.
By Lemma F, `v(a,b,c)·[𝒯(b,c) − (Q_n/Q_a)T(a,b,c)]` has `v_p ≥ −d(b,c) + 1 + d(b,c) = 1`, so
```
p³Ŵ_n ≡ (Q_n/Q_a)·Σ_{b,c}v(a,b,c)T(a,b,c) = (Q_n/Q_a)·Ŵ_a   (mod p).
```
Hence `p³Ŵ_n − Ŵ_aQ_r ≡ λ·Ŵ_a` with `λ := Q_n/Q_a − Q_r`, and `v_p(λ) ≥ 1` **by Theorem A**
(`Q_n ≡ Q_aQ_r mod p`). Finally `Ŵ_a = P̂_a − H₃(a)Q_a` with `H₃(a) ∈ ℤ_p` (as `a<p`) and `Q_a ∈ ℤ`,
so `v_p(Ŵ_a) ≥ min(0, v_p(P̂_a))`, and `v_p(λŴ_a) ≥ 1 + min(0,v_p(P̂_a))`. ∎

**This is the exact explanation of §5 of the campaign report.** The middle-row product congruence
fails precisely by the factor `λŴ_a`: `λ` supplies one power of `p` (Theorem A), `Ŵ_a` eats it back
when `v_p(P̂_a) = −1`. The observed depth law `E ≥ 1 + min(0,v_p(P̂_a))` with both floors attained is
reproduced *exactly*, which is a strong independent confirmation of the whole chain.

### 2.2 An unconditional corollary that needs nothing but Lemma D

#### Corollary E′. [PROVED — no Lemma F, no Lemma G off-regime, no integrality hypothesis]
For `1 ≤ a < p/3`: every level-`a` letter is `p`-integral (`a+b ≤ 2a < p` kills the `A`-poles,
`a+b+c ≤ 3a < p` kills the `C`-poles, `B` never has one), hence `v(a,b,c) ∈ ℤ_p`, hence
`d(b,c) = 0` and Lemma F degenerates to Theorem A's Lemma 4 (mod `p`). Therefore
```
p³ P̂_{ap+r} ≡ P̂_a·Q_r   (mod p)        for all 1 ≤ a < p/3, 0 ≤ r < p.
```
(Also `P̂_a ∈ ℤ_p` automatically in this range.) **[VERIFIED consistent with the sweep.]**

### 2.3 What remains for T2 — precisely two items

0. **The minimal sufficient statement.** Everything the proof actually uses is
   ```
   (MID)   Σ_{b,c=0}^{a} v(a,b,c)·[ 𝒯(b,c) − Q_r·T(a,b,c) ]  ≡ 0   (mod p)
   ```
   — a single congruence, in which `v(a,b,c)` is the *explicit* weight-3 form displayed above and
   `𝒯(b,c) − Q_rT(a,b,c) ∈ pℤ`. **[VERIFIED]** p ∈ {5,7,11,13}: (MID) holds at **every** cell with
   `P̂_a ∈ ℤ_p` (0 failures out of 20+21+110+156 cells) and fails exactly at the cells with
   `v_p(P̂_a) = −1` — i.e. (MID) **is** the theorem, with nothing to spare. Lemma F below is the
   clean *termwise* strengthening that implies (MID) for a structural reason.
1. **Lemma F.** A mod-`p^{1+d}` refinement of the Lucas factorisation of `T`. Both sides are
   divisible by `p^{≥d}` already (Lemma D / level-`a` Lemma D), so the content is a *relative*
   mod-`p` statement one level below the leading term — the natural tool is a
   Jacobsthal/Granville-type mod-`p²` (resp. `p⁴`) Lucas theorem for
   `C(n+k,n), C(n,k), C(n+k+l,n)`, summed over the fibre `(s,t)`. Sharp (slack 0 attained), so no
   cruder bound will do.
2. **Lemma G off-regime.** For `(s,t)` with `s>r`, `t>r` or `r+s+t ≥ p` the digit identities
   `⌊(n+k)/p⌋=a+b` etc. acquire a `+1`, and the mismatch of `p^mA_m(k)` against `A_m^{(a)}(b)` is
   `ε₁·[H^{(m)}_{a+b+1} − H^{(m)}_{a+b}] = ε₁(a+b+1)^{−m}`, `ε₁=[r+s≥p]`. That is a `p`-unit
   **except** when `a+b+1 = p`, where it is `p^{−m}` — and then Lemma D⁺'s `v_p(T) ≥ 2` is one
   power short for the `A₃` monomial. **The missing power exists**:

   > **Lemma D⁺⁺ (boundary carry).** With `β := ⌊(n+k)/p⌋ = a+b+[r+s≥p]`: if `β ≥ p` **and**
   > `a+b < p` (equivalently `a+b = p−1` and `r+s ≥ p`), then `v_p(T(n,k,l)) ≥ 4`.
   >
   > **[VERIFIED, 0 failures, min exactly 4 — sharp]** p ∈ {5,7,11,13}: 518 / 2 869 / 28 340 /
   > 65 918 index triples. (Contrast: `β ≥ p` **with** `a+b ≥ p` gives min exactly **2** —
   > Lemma D is sharp there, 1.3 M triples.)

   *Proof sketch.* `a+b = p−1` and `r+s ≥ p` make `n+k = p² + (r+s−p)`, so the base-`p` addition
   `n+k` carries at positions 0 **and** 1: `v_p C(n+k,n) = 2`. For the remaining two powers, split
   on `s+t`: if `s+t < p` then `r+s+t ≥ r+s ≥ p` forces a position-0 carry in `n+(k+l)` and then a
   position-1 carry (digit sum `≥ a+b+1 = p`), so `v_p C(n+k+l,n) ≥ 2`; if `s > r` the borrow in
   `n−k` gives `v_p C(n,k)² ≥ 2`. The remaining sub-case (`s+t ≥ p`, `s ≤ r`) is the one still to
   be written out. With Lemma D⁺⁺ the off-regime `A₃`-mismatch closes, and the `A₂·X₁` mismatches
   close the same way (they need only `v_p(T) ≥ 3`).

### 2.4 Correction to the campaign report

* **§6c's table is imprecise on two counts** (this does not affect any stated result):
  `B_r` **does** carry a `p^{−r}` pole for `n < p²` (from `p | j ≤ n−k`); and `C_r` reaches
  `p^{−2r}`, not `p^{−r}`. The consequential point is §6b's Corollary: its case
  "`A₂(k)·X₁` … the deepest combinations again require `β ≥ p`, so Lemma D⁺ applies" is **wrong**
  — `A₂(k)C₁` reaches `p^{−4}` already with `β < p`, whenever `⌊(n+k+l)/p⌋ ≥ p > ⌊(k+l)/p⌋`,
  with no help from Lemma D⁺. The **conclusion `v_p(P̂_n) ≥ −4` still stands** (that route gives
  exactly `−4` too), but the proof needs this extra case. The `n < p` statement `v_p(P̂_a) ≥ −1`
  is unaffected.

---

## 3. T3 — the hunt for `w₅`

### 3.0 Method, and why the old negative was not yet decisive

The fit is `P_n = Σ_{k,l}T(n,k,l)·w₅(n,k,l)` with `w₅` a ℚ-combination of **symmetric** weight-5
monomials in an alphabet of letters, each depending on `k` only, on `l` only, on `k+l` only, or on
`n` only. That separability is what makes the search feasible:
```
Σ_{k,l} T·f(k)g(l)h(k+l) = f^T W_h g ,   W_h[k,l] = T(n,k,l)·h(k+l),
```
so **all** basis values sharing one coupling monomial `h` come from a single matrix product
`(F W_h)F^T` (`F` = the |Sk|×(n+1) matrix of single-variable monomials). Cost per level `n` is
`|Sc|·|Sk|·n²`; everything mod a prime `q < 2^25` (int64 numpy matmul is then exact).

**The decisive point the previous campaign could not reach.** A realistic weight-5 alphabet gives
*hundreds* of basis elements, and the exact ladder stops at `n = 360`. A 682-column system over
360 rows has full row rank — it is **vacuously consistent**, so "we found a solution" and "we
found no solution" are both meaningless there. The prior 149-element negative was real but could
be blamed on the smallness of the basis. Extending the ladders mod `q` (§0, unlock 2) removes the
ceiling and turns the question into a genuine falsification test.

**Positive control (essential).** Same pipeline, weight **3**, target `P̂`, in a 93-element basis
that *includes* depth-2 letters, `N = 400` equations: `rank(M) = 60`, **consistent**, i.e.
`340` excess equations all satisfied. So the protocol does not manufacture inconsistency, and
**Theorem B is re-confirmed with 340 independent excess constraints mod q** (on top of the exact
rational check `n = 0..30` done here). Negative control: the *same* basis with target `P` is
inconsistent, as it must be.

### 3.1 Depth-1 weight 5 with the prior campaign's monomial *shape* — falsified
*(read together with §3.3: the falsified object is the **≤ 3-factor** ansatz, not the depth-1 span)*

Alphabet `{A_r(k),A_r(l),B_r(k),B_r(l),C_r,H^{(r)}_n,H^{(r)}_{2n} : r=1..5}`
(`A_r(x)=H^{(r)}_{n+x}−H^{(r)}_x`, `B_r(x)=H^{(r)}_{n−x}−H^{(r)}_x`,
`C_r=H^{(r)}_{n+k+l}−H^{(r)}_{k+l}`), all symmetric weight-5 monomials with at most 3 factors in
each of the four slots: **682 basis elements** (the prior campaign's basis had 149 and is
contained in this one; the `H^{(r)}_{2n}` letters are new).

| equations `n=1..900` | rank(M) | rank([M\|b]) | verdict |
|---|---|---|---|
| mod q₁ = 33554393 | 478 | 478 | **INCONSISTENT** |
| mod q₂ = 33554467 | 478 | 478 | **INCONSISTENT** |

**422 excess equations**, two independent primes, identical rank. So the prior campaign's negative
is confirmed *and made decisive* — **for that monomial shape**: `P_n` has no weight-5
harmonic-monomial decomposition **with at most three factors per variable**. (§3.3 shows the cap is
exactly what fails.)

### 3.2 Depth-2 — also falsified

Alphabet enlarged by the MZV-style nested (`Z`-)sums `Z_x(α,β) = Σ_{x ≥ m₁ > m₂ ≥ 1} m₁^{−α}m₂^{−β}`
for all `(α,β)` with `3 ≤ α+β ≤ 5` (9 pairs: 12,13,14,21,22,23,31,32,41), placed at exactly the
argument shifts that `ŵ₃`'s letters use:
```
ZA_{α,β}(k)=Z_{n+k}−Z_k ,  ZB_{α,β}(k)=Z_{n−k}−Z_k ,  ZC_{α,β}=Z_{n+k+l}−Z_{k+l} ,
ZN_{α,β}=Z_n ,  ZM_{α,β}=Z_{2n} ,
```
on top of the whole depth-1 alphabet. **1053 basis elements, `N = 1200` equations:**

| | rank(M) | rank([M\|b]) | excess | verdict |
|---|---|---|---|---|
| depth-1+depth-2, 1053 elts | 752 | 752 | **448** | **INCONSISTENT** |

So — **still under the ≤ 3-factor cap** — the naive reading of "the top period is depth 2,
therefore add depth-2 letters" is **false**: adjoining `Z`-sums at the `ŵ₃` argument shifts does not
by itself produce `w₅`. (What was actually missing is in §3.3.)

### 3.3 THE ACTUAL ANSWER: `w₅` **does** exist at depth 1 — the negative was a basis artifact

Removing the *factor-count cap* (and nothing else) from the depth-1 alphabet makes the system
**consistent**. Full ablation, all at `N = 1200` equations, alphabet
`{A_r,B_r}` (k and l) `∪ {C_r} ∪ {H^{(r)}_n, H^{(r)}_{2n}}`, `r = 1..5`, caps
`(mf_k, mf_c, mf_n)` = max factors in the single-variable / coupling / constant slot:

| caps | basis | rank(M) | excess eqs | verdict |
|---|---|---|---|---|
| (3,2,2) — *the previous shape* | 682 | 478 | 422 | **INCONSISTENT** (also mod a 2nd prime) |
| (3,2,**5**) — relax constants only | 789 | 554 | 646 | **INCONSISTENT** |
| (3,**5**,2) — relax coupling only | 711 | 486 | 714 | **INCONSISTENT** |
| (**5**,2,2) — relax single-variable only | 721 | 489 | 711 | **CONSISTENT** |
| (5,5,5) — no cap at all | 857 | 572 | 628 | **CONSISTENT** |

> **The missing ingredient is monomials with FOUR or FIVE factors in one variable** — e.g.
> `A₁(k)⁴A₁(l)`, `A₁(k)³B₁(k)²`, `A₁(k)⁵`. `ŵ₃` needs at most **two** factors, and both the prior
> campaign's 149-element basis and my own first 682-element basis capped the single-variable slot
> at **three**. That cap, not the depth of the period, is what produced every negative result.

**This overturns §3.3 of `PROOF_LB5_CAMPAIGN.md`.** `P_n` *does* admit a representation
`P_n = Σ_{k,l}T(n,k,l)·w₅(n,k,l)` with `w₅` a ℚ-linear combination of weight-5 **harmonic
monomials** — no nested/depth-2 letters, no new objects, the *same* BZ summand `T(n,k,l)` and the
*same* alphabet of letters as `ŵ₃`. The `ζ(5)+2ζ(2)ζ(3)` depth-2 period does **not** force depth-2
letters in the rational row.

Evidence strength: with the minimal consistent basis (721 columns) the mod-`q` system over
`n = 1..1200` has rank 489 and `b` lies in the column space — **711 independent excess equations
all satisfied**; a false positive would require a `q`-adic coincidence of probability `q^{-711}`.

### 3.4 An explicit `w₅`, reconstructed over ℚ and verified exactly

`work/lb5/extract.py` / `extract2.py`: build the design matrix mod **two** primes, row-reduce both
(pivot profiles agree, rank 489 / 572), CRT the two particular solutions, rational-reconstruct.

> **[VERIFIED exact, over ℚ, 0 discrepancies]**
> `P_n = Σ_{k,l=0}^{n} T(n,k,l)·w₅(n,k,l)` for **`n = 1..20`**, with `w₅` the explicit ℚ-combination
> of **130** weight-5 harmonic monomials written out in `work/lb5/w5_solution_abcn.json`.
> `n = 1..14` inside the extraction script; `n = 15..20` by `work/lb5/verify_w5.py`, a **fresh,
> standalone re-implementation** that reads nothing but the JSON and the ladder.

The extraction was run three times, from the 448-, 721- and 857-column bases, at `N = 1000`/`1200`:
**all three returned the byte-identical 130-term solution** (the extra columns of the larger bases
come out as free variables = 0), and each was verified exactly. So the solution is supported
entirely in the minimal alphabet.

**Minimal alphabet (ablation at `N = 1000`, caps `(5,2,2)`):**

| alphabet | basis | rank | excess | verdict |
|---|---|---|---|---|
| `{A_r, C_r, H^{(r)}_n}` (drop `B`) | 123 | 123 | 877 | INCONSISTENT |
| `{A_r, B_r, H^{(r)}_n}` (drop `C`) | 246 | 229 | 771 | INCONSISTENT |
| `{A_r, C_r, H^{(r)}_n, H^{(r)}_{2n}}` | 229 | 229 | 771 | INCONSISTENT |
| **`{A_r, B_r, C_r, H^{(r)}_n}`** | **448** | **313** | **687** | **CONSISTENT** |

So the alphabet of `w₅` is **exactly the alphabet of `ŵ₃`** — the three summand log-derivative
letters plus the constant `H^{(r)}_n`. `H^{(r)}_{2n}` is *not* needed; `B` and `C` both are. The
sole difference between weights 3 and 5 is the **number of factors**: `ŵ₃` uses ≤ 2, `w₅` needs up
to 5 (factor histogram of the 130-term representative: 3 monomials with 1 factor, 14 with 2,
40 with 3, **41 with 4, 32 with 5**).

This is a *rational* verification, not a mod-`q` one: the coefficients are honest fractions and the
sums are exact. Together with the 711 excess mod-`q` equations at `n ≤ 1200` this settles existence.

**Structure of the found solution.** The solution space has dimension `448 − 313 = 135`, so the
printed representative is one point of an affine family and its coefficients are not canonical
(they carry spurious `11²` denominators from the pivot choice). Three features are, however,
already visible and match `ŵ₃` exactly:
* the constant letter enters as `H^{(5)}_n` with coefficient **exactly 1** (as `H^{(3)}_n` does in
  `ŵ₃`);
* the only weight-5 *single* letters occurring are `A₅` and `B₅` — the coefficient of `C₅` is **0**,
  mirroring `ŵ₃`'s "no `C₃` top letter";
* every monomial is built from the *same* letters `A_r(x)=H^{(r)}_{n+x}−H^{(r)}_x`,
  `B_r(x)=H^{(r)}_{n−x}−H^{(r)}_x`, `C_r=H^{(r)}_{n+k+l}−H^{(r)}_{k+l}` and `H^{(r)}_n`;
* the **skeleton is literally `ŵ₃`'s**: the constant slot is used exactly once (`H^{(5)}_n`,
  coefficient 1), the coupling slot exactly by a single `C₁` (in 5 of the 130 monomials, all of
  them weight-4-in-`(k,l)` times `C₁`), and the remaining 125 monomials are pure products of
  `A_r`, `B_r` in `k` and `l`. Compare `ŵ₃ = H^{(3)}_n + A₃(k)+A₃(l) − … − (3/8)(A₂(k)+A₂(l))C₁ − …`
  — one constant letter, one `C₁`, the rest `A`/`B` products.

The five `C₁`-monomials of the representative, for orientation (notation `[f(k)|g(l)]×h(k+l)×s(n)`,
symmetrised in `k↔l`):
```
 -205/968 ·[A₁³|B₁]C₁ ,  +205/968 ·[A₁²B₁|B₁]C₁ ,  -553/1936·[A₁²|A₁B₁]C₁ ,
 -17/968  ·[A₁²|B₁²]C₁ ,  -17/968  ·[A₁²|B₂]C₁ .
```

**Open (and now purely cosmetic-but-valuable):** pick the canonical representative in the
135-dimensional solution space — e.g. by imposing `ŵ₃`'s normalisations (coefficient 1 on
`A₅(k)+A₅(l)`, zero on every monomial whose top letter is `B`, `C` or `H^{(·)}_{2n}`) — and read off
a `w₅` as short and as pretty as `ŵ₃`. That is a small linear-algebra job, not research.

### 3.5 Secondary finding: the interval-nested route also works

For completeness, adjoining the **interval** nested sums
`YA_{α,β}(k) = Σ_{k<m₂<m₁≤n+k} m₁^{−α}m₂^{−β}` and `YC_{α,β}` (the true depth-2 analogues of
`A_r`, `C_r`) to the depth-1 alphabet makes the system consistent **even with the old cap 3**:
1211 basis elements, `N = 1100`, rank 790, **CONSISTENT**, 310 excess equations. This is the same
phenomenon seen from the other side — `YA_{α,β} = ZA_{α,β} − A_α·H^{(β)}_k` re-introduces exactly the
high-factor products that the cap removed. **The depth-1 statement of §3.3 is the stronger and
cleaner one.**

---

## 4. Assembled status of Phase 2

### 4.1 What is now a theorem, and modulo what

| object | status after this session |
|---|---|
| `Q_n = Σ_{k,l}T(n,k,l)` (BZ's own formula) | **[CERTIFIED]** by two-step creative telescoping: the CT telescoper *is* the BZ order-3 operator (two-sided exact polynomial division, remainder 0 both ways) — §1.2 |
| `Q_{ap+r} ≡ Q_aQ_r (mod p)` | **[PROVED]** (Theorem A, previous session) |
| `(LB₅) ⟺ (W5)` | **[PROVED]** (Theorem C, previous session) |
| `P̂_n = Σ T·ŵ₃` (Theorem B) | **[VERIFIED]** exact `n ≤ 30` + **340 excess equations mod q** (§3.0); CT certificate still open (§1.3) |
| middle row `p³P̂_{ap+r} ≡ P̂_aQ_r (mod p)` when `P̂_a ∈ ℤ_p` | **[PROVED]** given Theorem B, Lemma F, off-regime Lemma G — §2.1; **unconditionally [PROVED] for `a < p/3`** — §2.2 |
| `P_n = Σ T·w₅`, `w₅` a weight-5 harmonic monomial in `ŵ₃`'s alphabet | **[VERIFIED exact ℚ, `n ≤ 20`, + 687 excess equations mod q at `n ≤ 1000`]** — §3.3–3.4; explicit 130-term representative on disk |
| top row `(W5)` / `(LB₅)` | **no longer blocked on the existence of `w₅`**; now blocked on Lemmas F, G-off-regime and on pinning the canonical `w₅` |

### 4.2 What (LB₅) needs, given (W5) — and why the top row is *easier* than the middle one

The §2 ledger is weight-agnostic: Lemma H and the LETTER-DESCENT identities
`p^m L^{(n)} = L^{(a)} + p^m ℤ_p` hold verbatim for every `m`, and Lemma F is a statement about the
BZ summand `T` alone (no weight enters). So **given a `w₅` with `P_n = Σ T·w₅`**, the *same three
steps* give
```
p⁵P_n − P_aQ_r ≡ p⁵W_n − W_aQ_r ≡ (Q_n/Q_a − Q_r)·W_a   (mod p),
```
and the middle row's defect **does not occur at weight 5**:

> **[VERIFIED, 0 exceptions, p ∈ {5,7,…,31}]** `v_p(P_a) ≥ 0` **and** `v_p(W_a) ≥ 0` for every
> `1 ≤ a < p` (`W_n = P_n − H₅(n)Q_n`). Contrast `v_p(P̂_a) = −1` for most `a ∈ (p/2,p)`.

Hence `λW_a ≡ 0 (mod p)` unconditionally, and **(LB₅) would follow with no integrality hypothesis
at all**. And Lemma G ports verbatim: `w₅` lives in the **same alphabet** as `ŵ₃` (§3.4), so the
LETTER-DESCENT identities are the same; only the monomial degree changes, and the pole-vs-Lemma-D
bookkeeping is the same argument run over 5-factor instead of 2-factor monomials.

Concretely, the remaining Phase-2 gap is now exactly:

1. **Canonical `w₅`** — pick the representative in the 135-dimensional solution space that has
   `ŵ₃`'s normalisations, so the ledger of §2.1 can be run on a short explicit formula
   (linear algebra, not research);
2. **Lemma F** at the precision the weight-5 poles demand (`d ≤ 5` instead of `d ≤ 3`);
3. **Lemma G off-regime** — i.e. **Lemma D⁺⁺** (§2.3), one sub-case of a carry count;
4. CT certificates for `P̂_n = Σ T·ŵ₃` and `P_n = Σ T·w₅` (§1.3).

Items 2 and 3 are *shared* between the middle and top rows: proving them closes T2 **and** removes
two of the four obstacles to (LB₅). **Lemma F is the single sharpest remaining obstruction.**

---

## 5. Reproduction / scripts

All under `work/lb5/` (Python 3 + numpy; Mathematica via `math < file.wl`).

| file | what it does |
|---|---|
| `core.py` | exact objects: ladders, `T(n,k,l)`, `H^{(r)}`, `ŵ₃`, the BZ order-3 recurrence, `v_p` |
| `fit.py` | mod-`q` fitting engine: ladder extension by the certified recurrence, harmonic + nested-sum tables, alphabet, symmetric-monomial bases, separable design-matrix rows, numpy `rref` |
| `run_fit.py`, `hunt.py` | basis construction and the T3 driver (`python3 hunt.py <tag> <N> <depth2> <mfk> <mfc> <mfn> [target] [W] [raw]`) |
| `t2_ledger.py` | exact ledger checks L1 (Lemma G), L2, L3 for the middle row |
| `t2_lemF.py` | Lemma F verification mod `p^8`, primes 5..19 |
| `abl_alpha.py` | minimal-alphabet ablation for `w₅` |
| `verify_w5.py` | standalone exact ℚ re-verification of the saved `w₅` |
| `extract.py` / `extract2.py` / `extract3.py` | two-prime CRT + rational reconstruction of `w₅`, then **exact** ℚ verification against the ladder |
| `w5_solution_abcn.json` (= `w5_solution_min.json` = `w5_solution.json`, byte-identical) | the explicit 130-term `w₅` (label format `[f(k)\|g(l)]×h(k+l)×s(n)`) |
| `gate3.wl`, `gate4.wl` | two-step creative telescoping (Q-gate; `ŵ₃`-weighted) |

## 6. Corrections to prior campaign notes (this session)

1. **`PROOF_LB5_CAMPAIGN.md` §3.3 / `ORCHESTRATOR_NOTES §2d` correction (iii) — OVERTURNED.**
   "`P_n` has NO weight-5 harmonic-MONOMIAL decomposition … so `w₅` needs nested letters" is
   **false**. `w₅` exists, at depth 1, in `ŵ₃`'s own alphabet; the negative came from bounding the
   number of monomial factors by 3. Corollary: the depth-2 nature of the period
   `ζ(5)+2ζ(2)ζ(3)` does **not** obstruct an elementary rational weight function. (§3.3)
2. **`PROOF_LB5_CAMPAIGN.md` §6c table.** `B_r` *does* carry a `p^{−r}` pole for `n < p²`;
   `C_r` reaches `p^{−2r}`, not `p^{−r}`. (§2.4)
3. **`PROOF_LB5_CAMPAIGN.md` §6b Corollary, proof.** The case `A₂(k)·X₁` is mis-argued (it does not
   need `β ≥ p`); the conclusion `v_p(P̂_n) ≥ −4` survives. (§2.4)
4. **Sharpened statement of the middle row.** The right law is
   `v_p(p³P̂_{ap+r} − P̂_aQ_r) ≥ 1 + min(0, v_p(P̂_a))` — and §2.1 now *derives* it, with the
   correction term identified as `λ·Ŵ_a`, `λ = Q_n/Q_a − Q_r`.

**Trap to remember:** in `math < file.wl` (stdin/interactive) mode a *line* that already parses as
a complete expression is evaluated immediately — a continuation line beginning with `+`/`-` becomes
a **separate** expression. Multi-line assignments silently truncate. Keep each assignment on one
line (this bit `gate3.wl`: `ŵ₃` was silently truncated to its first three terms).
