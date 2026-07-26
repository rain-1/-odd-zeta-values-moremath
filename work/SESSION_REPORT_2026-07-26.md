# Session report — 2026-07-26 into 27

**For:** River
**Repo:** `/home/ubuntu/fable-episode-2/zeta-math-2`, all work committed through `575b077`
**Labels used throughout:** `[PROVED]` (a proof exists, on paper) · `[LEAN]` (kernel-verified,
no `sorry`, clean axioms) · `[VERIFIED range]` (exact computation over a stated range, not a
proof) · `[EXCLUDED with bounds]` · `[MEASURED]`

---

## 0. The headline, and the answer to "Lean?"

> **`P̂_n = Σ_{k,l=0}^{n} T(n,k,l)·ŵ₃(n,k,l)` for every `n ≥ 0`.** `[PROVED]`

**It is NOT Lean-verified.** `[PROVED]`, not `[LEAN]`. That distinction is the whole of §2 and
§3 below, and given your standing rule — nothing reported unless kernel-verified — it is the
first thing that should be said about this result.

The proof is a paper proof: a Barnes/Mellin contour derivation plus a literature citation, with
independent verification of every checkable step. It is not a formalisation, and the
formalisation is not close in the way "one `sorry`" makes it sound.

The companion statement for the **top** row, `P_n = Σ T·w₅`, is **open** — neither proved nor
verified-and-nearly-proved. Its gap is now named to within one dimension (§4).

---

## 1. What is proved

### 1.1 The middle row `[PROVED]`

    P̂_n = Σ_{k,l} T(n,k,l)·ŵ₃(n,k,l),
    T(n,k,l) = C(n+k,n)C(n,k)²C(n+l,n)C(n,l)²C(n+k+l,n),
    ŵ₃ = H⁽³⁾_{n+k} − Ψ·H⁽²⁾_{n+k},   Ψ = ½α + β

where `P̂` is the Brown–Zudilin weight-3 companion row, defined by `L_BZ` with
`P̂₀ = 0, P̂₁ = 101/4, P̂₂ = 344923/96`.

**The proof chain, with each link's status:**

| link | statement | status |
|---|---|---|
| A | The Barnes/Mellin derivation of the BZ decomposition, symbolic in `n,k,l` — gamma/reflection reduction, contour choice `c₁=c₂=n+2/3`, complete bivariate partial fractions, uniform universal kernels | `[PROVED]` (Sol) |
| B | Zudilin 2002, *Arithmetic of linear forms involving odd zeta values*, **Lemma 4** supplies the §5 rational coefficient | citation, **verified real** |
| C | `A_kl = C(n+k,n)C(n+k+l,n)C(n,k)²`, `B_kl = A_kl·L_k` | `[PROVED]`, and recomputed symbolically here — **54/54 cells exact** |
| D | the factor-2 normalisation of the descent is uniform in `n` | `[PROVED]` — `outer·A_kl = T(n,k,l)` identically, so the Lemma-4 ζ(3)-coefficient is `2Q_n` against `I″`'s `Q_n`, ratio exactly 2 for all `n` |
| E | §7.3: `Σ T[H⁽³⁾_{k+l} + ¼(L_k+L_l)H⁽²⁾_{k+l}] = Σ T·w3sym` | `[PROVED]` (double zero of `g_l` on `l < j ≤ n`) |
| F | `Σ T·w3sym = Σ T·ŵ₃` | `[PROVED]`, free — `w3sym` is `ŵ₃`'s `k↔l` symmetrisation, the difference is antisymmetric, and `T(n,k,l) = T(n,l,k)` |

**Crucially, no coefficient comparison and no ℚ-linear-independence assumption is used.** That
was the objection that stopped an earlier version of this claim: since ζ(5) irrationality is
open, you cannot match coefficients of `1, ζ(2), ζ(3), ζ(5), ζ(2)ζ(3)` as real numbers. Link D
avoids it — the comparison is between explicitly computed *rationals* inside one derivation.

**Independent verification performed here** (not relayed on trust): the citation was read and
has the claimed shape; C recomputed by symbolic differentiation; the resulting formula matched
the exact ladder at `n = 0…10` in both its asymmetric and symmetric forms; D established from an
exact binomial identity rather than the `n=0` fit Sol originally used.

### 1.2 The ζ(3) two-level digit law `[PROVED]` — earlier the same day

    (a_n, p³b_n) ≡ (a_a, b_a)·u(a,r) (mod p³),   u(a,r) = a_r + 2p·a·U_r + p²a²X_p(r)

for `p ≥ 5`, `n = ap+r`, both rows. Everything reduces to one rational function
`g_r(z) = [∏(z+i)/∏(z−j)]²` with `A_Γ = (sin²πz/π²)g_r`, and the residue theorem applied twice —
once over ℂ giving an identity over ℚ, once over `𝔽_p` where the **carry region is exactly the
complement of the pole divisor**. That is why the vanishing can never be a rational identity.
The rank-(1,1) profile, previously measured at 13 primes, is now a corollary.

Also settled: at `p = 2, 3` the conclusion holds but every mechanism fails; survival is a
resolution artefact (the necessity vectors have rank 0 and 1 against 2 at every `p ≥ 5`).

### 1.3 Other proved items

* **The one-variable boundary certificate.** `Φ` is `k↔l` symmetric, so the two boundary sums
  collapse to one and Gosper closes it: `u(n,j) = Nu/[(j+1)(n+j+1)(n+j+2)(n+j+3)]`, `deg_j Nu = 12`,
  `u` unique, `j³ | Nu` unimposed. Seven checks at `n = 1…14`, both primes. Cleared to
  `ℤ[n,j]`, bidegree ≤ (20,12), **10 monomials**. *Why it was open: the existing code ran Gosper
  on the two halves separately, and only their sum vanishes.*
* **(L1), (L3), (L4), (L5)** — evaluation identities for the combined two-variable object,
  each one line from the product form of `R`. **(L5)**, the anti-diagonal, is the interesting
  one: its poles move with `x`, so it is not obtainable from fixed-pole facts by partial
  fractions. At `n=6, m=2, x=17/6` all 14 summands are nonzero and the sum is exactly 0.
* **Sol's ζ(4) and ζ(3) kernel identities**, by residue-at-infinity and by an explicit
  numerator factor respectively.

---

## 2. What is in Lean

Library `lean/ZetaLucas`, 15 modules, `lake build` clean.

| module | contents | status |
|---|---|---|
| `Reflect.lean` (288 lines) | reflective polynomial-identity checker, sparse `List ((ℕ×ℕ×ℕ)×ℤ)`, `substK`/`substL` | **clean** — axioms `[propext, Quot.sound]`, `eval_congr` axiom-free, **no `native_decide`** |
| `BZQRow.lean` (891 lines) | Q-row certificate, all boundary conditions, denominator positivity | complete **except** `KeyPoly`, carried as an explicit hypothesis |
| `BZStar.lean` (339 lines) | bare-letter shift table, `wstar`, `PStarSum`, three initial values computed from the definitions | complete except `BZRec PStarSum`, quarantined |

**Two `sorry`s, both quarantined and both listed.** The ζ(5) closed forms are **not verified**.

**What the Lean route would deliver, and it is not what §1.1 proves.** The `w★` certificate,
when complete, gives `P̂_n = Σ T·w★` — *not* the compact `ŵ₃` form. The order-0 bridge between
them is `[PROVED]` **impossible** (§4), and any bridge has order ≥ 4. `LEAN_VERIFIED.txt` §9
states this plainly.

**The infrastructure findings, which are reusable:**

* **`ring` is excluded.** Safe to ~6,000 monomials, dead past ~15,000. The Q row's single
  3,798-monomial identity does not fit in 15 GB across nine arrangements.
* **The reflective checker has a wall too**, an order of magnitude further out — flat memory
  only to `|R| ≈ 1800`. The fix is one operation per declaration (the kernel frees its `whnf`
  cache per declaration); confirmed working on the last run, **RSS bounded at 5.13 GB** against
  9.5–12.7 GB still climbing for the monolithic form.
* **Coefficient height is free to compute with** — 63/575/4,159 bits → 82/74/97 s, RSS moving
  20 MB across a 66× range — **but not free to ship**: a 400-monomial table is 12 MB of Lean
  source at 9,884 digits.

---

## 3. What is verified but not proved

* `Σ T·w₅ = P_n`, the **top row**. Verified against every exact ladder value to `n = 360` at two
  primes. No proof.
* `Σ T·B5 = (33/4)P_n` — arrow (B) of the ε route (§4).
* The `w★` order-3 certificate: verified on 218,000 fresh-point identities, lifted to `ℤ[n,k,l]`
  with 0 of 96,813 coefficients unliftable and 889,728 held-out identities matching — **but in a
  gauge that does not satisfy the 16 boundary rows**, so the sum does not yet collapse.

---

## 4. Proved negatives — the most reusable output

* **The order-0 bridge `T(w★ − ŵ₃) = Δ_kR₀ + Δ_lS₀` is impossible.** For a maximal monomial the
  shift matrices are diagonal, so summing forces `d_i·Q_n = 0` with `Q_n ≥ 1`; but `d` has 29
  nonzero maximal components. Any bridge must annihilate `Q`, hence **order ≥ 4**.
* **No successful representative has `w − ŵ₃` purely antisymmetric** — `W_tel` is σ-stable and
  linear, so it would force `ŵ₃^sym ∈ W_tel`, which is excluded.
* **The order-7 route is excluded for Lean.** `A` lifted exactly, `a_4` factors through `L_BZ`'s
  own cubic with a 5-line nonvanishing proof — but the cofactors run to 1.5·10⁶ monomials,
  10³–10⁴× past any consumer.
* **No order-3 representative for the `P` row in the degree-≤3 weight-5 span.** Guarded five
  ways, including the curl gauge that flipped weight 3, and an end-to-end weight-3 control
  through the same code that returns YES.
* **`ŵ₃^sym`, `ṽ`, `ṽ^sym`, `L̃`** all fail at order 3; the ε-pencil is a line in `K` that does
  not meet the admissible set.
* **The Euler/product split is basis-dependent** — the derived and fitted universal forms differ
  term-by-term while agreeing numerically (equal modulo shuffle relations), so "the Euler part
  does not cancel" is a statement about a basis, not the object.

---

## 5. Two methodological findings

### 5.1 `#print axioms` cannot detect a false undischarged hypothesis

`KeyPoly`, carried as a named hypothesis in `BZQRow.lean`, was **false as stated** — a spurious
sign in `Acore`. Every theorem downstream was `sorry`-free with clean axioms, and no automated
check in `LEAN_VERIFIED.txt` could tell that from a correct development: `#print axioms` reports
what a proof *depends on*, not whether its hypotheses are *inhabited*.

It was caught only by attempting to **discharge** the hypothesis. `LEAN_VERIFIED.txt` now opens
with this as a labelled limitation, with the instance as worked example, and a standing rule: no
certificate reaches the kernel until a faithful re-implementation has been run outside Lean and
compared exactly. That rule then caught two transcription bugs on the first object it was
applied to.

### 5.2 The `k↔l` symmetrisation paid three times

Your observation that `T(n,k,l) = T(n,l,k)`, so every antisymmetric weight is annihilated by the
double sum, was the most reused idea of the campaign — in three unrelated places: the free
`Σ T·ŵ₃ = Σ T·w3sym` step (link F above), the σ-stability impossibility argument, and the
collapse of the two boundary sums into one that let Gosper close them.

The mechanism it suggested — that antisymmetric baggage inflates telescoper order — was
**refuted**. The observation itself was load-bearing three times over.

---

## 6. Where to restart

| # | job | state |
|---|---|---|
| L10 | (B-bot) gauge re-lift + the `Nu` solve | **never executed.** All parameters known; step 2 is a one-line solve. ~1.5 h if `class_rows` is vectorised. **The only blocker on the `w★` Lean route.** |
| L8 | `KeyPoly` via the per-declaration split | diagnosed, confirmed bounded at 5.13 GB, needs the run |
| — | **arrow (A)** for the top row | **one dimension short**: 0/1557 generators fail calibration, rank 419 vs `sym(Δ₅) = 420`. **Extract the residual direction before adding families** — at weight 3 the codimension-one residual *itself identified the missing jet* |
| — | **arrow (B)** for the top row | two routes: does `L_BZ` telescope `T·B5`? (cheap probe); or Sol's weighted-sum zero `−(1/2)[1]W_B − (4/33)B5`, which proves both arrows at once. The Laurent span reaches **80 inconsistent rows of 852**; the combined Laurent+jets test was specified but never run |
| L11 | degree-4 affine gate | not run; partial finding — degree-4 denominators are milder, `H1` covers them |

---

## 7. On the collaboration

Sol is a Codex session sharing this repository; the channel is `work/agent_channel/`.

Sol found two real defects in our work by reading it: the impossibility argument that killed a
target I had pushed to two agents, and an over-strong boundary constraint that was faking a
calibration failure. I found the missing link in its middle-row claim — that §7.3 proved a
coefficient comparison inside the Barnes calculation rather than the closed form — and it closed
that with a real citation instead of routing around it.

Each of us retracted a claim the other believed. **The middle row is a theorem rather than a
strong verification because of that.**

One measurement is worth keeping as the emblem: Sol *fitted* the four universal coefficients
(fast); our agent *derived* them (authoritative). They **disagree term-by-term while agreeing
numerically** — equal modulo shuffle relations. Neither result alone says anything; the
difference between them is what revealed that a question both sides had been asking was not
well-posed.
