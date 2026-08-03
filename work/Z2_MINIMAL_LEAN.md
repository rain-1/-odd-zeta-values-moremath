# Z2_MINIMAL_LEAN — Lean route to the minimal Apéry ζ(2) companion formula

**Date:** 2026-08-02
**Target:** `work/z2cf/note.tex` Theorem 2 (the "minimal form"),

```text
B_n = (1/5) Σ_{k=0}^n S(n,k) [ H^(2)_n + H_k (2H_k − H_{n−k} − H_n) ],
S(n,k) = C(n,k)² C(n+k,k),
(L u)_n = (n+1)² u_{n+1} − (11n²+11n+3) u_n − n² u_{n−1},   L B = 0, B_0 = 0, B_1 = 1.
```

**Artifacts**

| file | status |
|---|---|
| `lean/ZetaLucas/Z2Shell.lean` | **[LEAN]** compiles, no `sorry`/`axiom`/`unsafe` |
| `lean/ZetaLucas/Z2Minimal.lean` | **[LEAN]** compiles, no `sorry`; scaffolding + descent |
| `lean/ZetaLucas/Z2Cert_{Chi,Gamma,Beta,Alpha}.lean` | **[LEAN]** the four cell-certificate component identities, machine-generated |
| `work/z2cf/emit_all.py`, `work/z2cf/emit_graded.py` | regenerate those four files from `cert.pkl` |

`Z2Shell` and `Z2Minimal` are imported by `lean/ZetaLucas.lean`. The four `Z2Cert_*` files
are **deliberately not** imported by the root: they cost ~50 min of elaboration and nothing
consumes them yet. Build them by name (`lake build ZetaLucas.Z2Cert_Alpha`) and add them to
the root once `star_z2` uses them.

Build times (this machine, `lake build <target>`), and `#print axioms` on every theorem
listed below reports only `propext, Classical.choice, Quot.sound`:

| target | wall |
|---|---|
| `Z2Cert_Gamma` | 16 s |
| `Z2Cert_Chi` | 29 s |
| `Z2Cert_Beta` | 9 min 42 s |
| `Z2Cert_Alpha` | 38 min 31 s |
| `work/z2cf/lean_certificate.py` | exact rerunnable audit of the full stage-2 certificate |
| `work/z2cf/cert_lean.txt` | the emitted `α, β, γ, χ` certificate polynomials |

## 1. What is proved in Lean today

`Z2Shell.lean`:

* the Lemma-0 absorption shell for `S(n,k)`, written at `n = m+1` over
  `Φ(m,k) = C(m+2,k)² C(m+k,k) / ((m+1)²(m+2)²)`;
* `propB_2` — the Zeilberger certificate of `note.tex` §3 Step 1 at **every** cell `k ≥ 0`.
  In this shell the certificate degenerates to `G(m,k) = Φ(m,k)·(m+1)·k³·ρ(m+1,k)`, so
  `propB_2` is one polynomial identity in `ℚ[m,k]` closed by `ring`;
* `apery2_rec` — `a_n = Σ_k S(n,k)` (A005258) is annihilated by `L`;
* `harm2_apery2_rec` — `L(H^(2)·a)_n = a_{n+1} + a_{n−1}`, the first half of the
  Proposition of `note.tex` §4.

`Z2Minimal.lean`: the weight `wz`, the row `Dz`, the shift convention `Lz f m = (L f)_{m+1}`,
the pre-operator `pz0, pz1, pz2`, `pz2_ne_zero`, the descent lemma `defect_vanishes`, and the
initial values `Dz 0 = 0`, `Dz 1 = 5`.

## 2. The obstruction: there is no single telescope

The `MinimalForm.lean` / `FranelClosedForm.lean` architecture — one antidifference
`Ψ = w·G + Z` for the operator itself — **provably cannot work here**.

Write the cell identity relative to the shell and split it along the letter monomials
`{1, H_k, H_{n−k}, H_n, H^(2)_n, H_k², H_kH_{n−k}, H_kH_n}`. Every other monomial is excluded
because its coefficient satisfies a homogeneous equation `r·c(k+1) = c(k)` with
`r = S(n,k+1)/S(n,k)`, which has no nonzero rational solution. The same uniqueness forces the
coefficients of `H_k², H_kH_{n−k}, H_kH_n, H^(2)_n` in `Ψ` to be exactly `2χ, −χ, −χ, χ`,
where `χ` is the Zeilberger antidifference cofactor. The `H_{n−k}` and `H_n` components then
*both* reduce to the requirement that

```text
r(k) φ(k+1) − φ(k) = ρ(n,k+1)/(k+1)
```

have a rational solution `φ`. Gosper's algorithm certifies that it does not
(`CHECK 0` in `lean_certificate.py`). This is exactly the obstruction that forces the
Ore-elimination route of `note.tex` §4.

## 3. The route used instead: a scalar order-two pre-operator

Let

```text
Q(x)  = 625x⁴ + 7250x³ + 31245x² + 59264x + 41752
p₀(x) = (x+1)(x+2) Q(x)
p₁(x) = 6875x⁶ + 100375x⁵ + 597195x⁴ + 1849309x³ + 3136850x² + 2758284x + 981880
p₂(x) = −(x+3)(x+4) Q(x−1)
```

Then the combination `p₀(m)·(L·)_{m+1} + p₁(m)·(L·)_{m+2} + p₂(m)·(L·)_{m+3}`, applied
cellwise to `S(n,k)w(n,k)`, **is** a `k`-difference:

```text
Ψ(m,k) = W(m,k)·w(m,k) + S(m,k)·( β H_k + γ (H_{m−k} + H_m) + α ),
W(m,k) = Σ_{i=0}^{2} p_i(m) G(m+i+1,k).
```

`α, β, γ` are explicit rational functions of `(m,k)` with poles only at `k = m+1,…,m+4`:

| | denominator | numerator degree in `k` / `m` | terms |
|---|---|---|---|
| `χ` | `∏_{t=1}^{4}(k−m−t)²` | 9 / 13 | 77 |
| `γ` | `∏_{t=1}^{3}(k−m−t)²` | 7 / 11 | 57 |
| `β` | `∏_{t=1}^{4}(k−m−t)³` | 13 / 17 | 150 |
| `α` | `(m+1)(m+2)(m+3)(k−m−4)²∏_{t=1}^{3}(k−m−t)³` | 12 / 19 | 174 |

The pre-operator is **minimal**: an order-0 pre-operator (i.e. `L` itself) and an order-1
pre-operator both give an empty solution space under a generous denominator/degree ansatz;
at order 2 the solution space is one-dimensional, so `(p₀,p₁,p₂)` is unique up to scale.

Summing the cell identity over `k` gives a **scalar order-two recurrence for the defect**
`E_m := (L D)_{m+1}`, where `D_n = Σ_k S(n,k)w(n,k)`:

```text
p₀(m) E_m + p₁(m) E_{m+1} + p₂(m) E_{m+2} = 0.
```

`E₀ = E₁ = 0` by direct evaluation, and `p₂(m) = −(m+3)(m+4)Q(m−1)` with
`Q(m−1) = 625m⁴+4750m³+13245m²+16024m+7108 > 0`, so the leading coefficient never vanishes
on the induction range (`pz2_ne_zero`, proved by `positivity`). Hence `E ≡ 0`, i.e. `L D = 0`;
with `D₀ = 0` and `D₁ = 5` this gives `D = 5B`.

No Ore algebra, no generic parameters, no order-three operator: the pre-operator enters the
Lean file only as three explicit polynomial coefficients.

## 4. The boundary cells

Under Lean's conventions (truncated `ℕ`-subtraction, `C(n,k) = 0` for `k > n`, total division
`x/0 = 0`) the cell identity is **not** literally true at `k = n, …, n+4`: there `S(n,k)`
vanishes while `β, γ, α` have poles, and in the analytic object those poles cancel against the
poles of `H_{n−k}`. This is verified cell by cell — the identity holds exactly on
`k ≤ n−1` and fails at exactly the five cells `k = n,…,n+4`.

The remedy is Abel summation with an explicit boundary block, as in `note.tex` §3 Step 3:
telescope only over `k = 0,…,n−1` and add the five top cells of the summand explicitly. The
required closure

```text
Ψ(n,n) − Ψ(n,0) + Σ_{k=n}^{n+4} (summand)(n,k) = 0,        Ψ(n,0) = 0,
```

is verified in exact arithmetic for `n ≤ 10` (`CHECK boundary closure`) and is a finite
identity in `C(2n,n)`, `H_n` and rational functions of `n`.

## 5. What remains

1. ~~Prove the four scalar component identities.~~ **Done** — `Z2Cert_{Chi,Gamma,Beta,Alpha}`.
   Assemble them into the generic cell identity `star_z2` for `k ≤ n−1`: expand the summand
   and `Ψ` in the `Φ` shell, push the letter shifts through `Harm_succ`
   (`H_{m+j} = H_m + Σ_{t≤j} 1/(m+t)`, `H_{m+j−k} = H_{m−k} + Σ_{t≤j} 1/(m+t−k)`,
   `H_{m−(k+1)} = H_{m−k} − 1/(m−k)`; all valid under `k ≤ m−1`), and match letter monomial
   by letter monomial against the four component lemmas. Do **not** finish with a single
   `field_simp`/`ring` over the assembled expression — see the tactic notes below, which
   apply verbatim to the assembly step.

   **Measured tactic guidance (do not skip).** The obvious formulation
   — state the component as an identity of rational expressions and call `field_simp; ring` —
   **does not work**: on the *smallest* component (`γ`) it ran 5 min of elaboration and still
   left the goal unsolved. `field_simp` cross-multiplies without cancelling the large common
   factor shared by the three terms. (Reported RSS for these builds is ~7 GB but is dominated
   by shared `Mathlib` olean mappings; anonymous usage stays near 3 GB, so the obstacle is
   time and term size, not memory.)

   What does work is **minimal clearing done in advance**, plus **grading in `y`**. Both are
   load-bearing; see `Z2Cert_*.lean`, which are machine-generated.

   *Minimal clearing.* For `γ`, multiplying `r·γ(k+1) − γ(k) = r·χ(k+1)/(k+1)` through by the
   common denominator and dividing the three resulting terms by their gcd

   ```text
   (x+1)(x−y)⁴(y+1)³(x−y+1)⁴(x−y+2)⁴(x−y+3)²(x+y+1)
   ```

   leaves a three-term polynomial identity of total degree 12 with 76 / 50 / 70 monomials,
   which plain `ring` closes in 71 s. State each component in that pre-cleared form, as a
   lemma in two free rationals `x, y` — no casts.

   *`y`-grading.* Minimal clearing alone is not enough at the top end: as one monolithic
   bivariate `ring`, `β` (5 terms, 974 monomials, degree 20) takes **53 min**, and `α`
   (7 terms, 1571 monomials, degree 22) is worse. Regrouping the identity as a polynomial in
   `y` whose every coefficient is a sum of univariate polynomials in `x` that cancels, and
   discharging each coefficient with its own univariate `ring`, brings `β` down to
   **9 min 42 s**. Each coefficient lemma is individually near-instant; the residual cost is
   elaborating the ~25 KB statement, so do not merge the four components into one file.

   Note `maxHeartbeats` is **per declaration**, not per tactic: fifteen individually-cheap
   `ring` calls in one theorem still exhaust the default budget. These files set
   `maxHeartbeats 0`.

   A change of variables `z = x − y` (the natural one, since all poles are at `x − y + t`)
   was tried and gives **no** sparsity gain — 975 vs 974 monomials for `β`, 1726 vs 1571 for
   `α`. Do not spend time on it again.
2. Prove the five-cell boundary closure of §4.
3. Conclude `Dz_op_rec`, then `Lz Dz ≡ 0` via `defect_vanishes`, then `Dz n = 5 * bz2 n`.
4. `#print axioms` audit on the headline theorem.

## 6. Scope

The theorem statement itself is verified in exact arithmetic for `n ≤ 11`
(`CHECK minimal formula`). The classical double-sum form (`note.tex` Theorem 1) is a separate
target and is **not** covered here; its `note.tex` §3 proof is elementary and would follow the
`FranelClosedForm.lean` pattern with an Abel step.
