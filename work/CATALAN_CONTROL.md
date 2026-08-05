# CATALAN_CONTROL — Project B: the Catalan control experiment (Sol A–F slate)

**Session 2026-08-05 (third arc).**  Executes Sol's Project B.  Literature
input from an Opus research agent (fetch-verified against arXiv
math/0201024 v3 and math/0210423; initial data independently recomputed
here).  Script: `work/z5eps/eps63_catalan.py` (+ `eps63_seqs.pkl`,
`eps63_nome.pkl`).

## 1. Input (verified)

Zudilin's Catalan recurrence (EJC 2003):
\[ (2n{+}1)^2(2n{+}2)^2p(n)\,u_{n+1} - q(n)\,u_n - (2n{-}1)^2(2n)^2p(n{+}1)\,u_{n-1}=0, \]
p = 20n²−8n+1, q = 3520n⁶+5632n⁵+2064n⁴−384n³−156n²+16n+7;
u: 1, 7/4, 649/64, …; v: 0, 13/8, 10699/1152, …; v_n/u_n → G (exactly G,
no π² or log 2 admixture).  Characteristic polynomial λ²−11λ−1 — the same
φ⁵-growth as Apéry's ζ(2).  Denominators: 2^{4n+o(n)}u_n ∈ ℤ,
2^{4n+o(n)}D_{2n−1}²v_n ∈ ℤ (v uses lcm to 2n−1, the "doubled" range).
Agent's initial-value table reproduced exactly by direct recursion here.

## 2. What holds

* **The boundary-defect structure is universal**: with the raw operator
  L = P₀(θ) + tP₁(θ) + t²P₂(θ) (P₀ = a(θ−1) etc.),
  \[ L(y_u) = 0, \qquad L(y_v) = \tfrac{13}{2}\,t \]
  exactly `[VERIFIED q^40]`.  The normalized companion (L(y_B) = t) is
  B = (2/13)v.  Sol's inhomogeneous-normalization formalism applies
  verbatim even here.

## 3. What fails — the boundary of the mechanism `[EXCLUDED, bounded]`

* **Arithmetic half.**  The canonical nome q = t·exp(g/y₀) gives
  t(q) = q − (15/2)q² + (9569/192)q³ − … with denominator profile
  2, 192, 960, 10321920, … — and **no rational rescale μ integralizes it**:
  exhaustive scan over μ = ±2^a3^b5^c, |a| ≤ 8, |b| ≤ 3, |c| ≤ 2.  The
  direct source Φ = θ_q²(y_B/F) has denominators growing superexponentially.
  This is not the sporadic (μ-rescale) pattern; there is no integral mirror
  map in this coordinate.
* **Analytic half.**  The fold connection value at the dominant singularity
  t_c = (√125−11)/2 (q_c ≈ 0.17267) is 0.17298…, while the true normalized
  limit is (2/13)G = 0.14092… — a mismatch of 3.2×10⁻², far above the
  series truncation (≲10⁻⁶).  The fold lemma's hypothesis fails: the raw
  operator has order six with indicial roots {0,0,½,½,·,·} at t = 0, the
  recurrence's 2-dimensional solution block is not a differential
  subsystem in t, and y₀(q) is not analytic at the fold.

## 4. Verdict and what it teaches

Sol's outcome 3, with the diagnosis sharpened: **Zudilin's Catalan
recurrence lies genuinely outside the modular-anchor mechanism** — not
"modular after a bad rescaling" but structurally hypergeometric (the
well-poised ₆F₅ / Rhin–Viola permutation-group world of the sources), with
the ½-indicial pairs as the visible fingerprint.  Answers to Sol's control
question:

> *Does the companion source depend chiefly on the constant, or on the
> geometric realization producing it?*

**The realization.**  The same constant G is reached two ways in this
program: family **E** (sporadic, level 8) reaches G/2 with a pure
weight-3 χ₋₄-Eisenstein source and an integral mirror map; Zudilin's
recurrence reaches G hypergeometrically with no modular structure in the
canonical coordinate.  Denominator and congruence phenomena of the E-family
are therefore properties of the modular realization, not of Catalan's
constant.

Sharpest open form:

> **(B-1)** Is there a change of variable (t = s², an Atkin–Lehner-type
> re-coordinate, or a quadratic pullback absorbing the ½-exponents — the
> D_{2n−1} denominators hint at variable doubling) after which Zudilin's
> Catalan operator acquires an integral mirror map?  A positive answer
> would re-absorb it into the modular class at a doubled level; a proved
> negative would make the hypergeometric/modular boundary exact.

## 5. Honest limits

The μ-scan is bounded as stated; the fold mismatch is numeric (≈6 correct
digits, limited by F's convergence at q_c ≈ 0.72×radius); the ½-indicial
claim is read off P₀ = (2θ−1)²(2θ)²p(θ−1) exactly.  Zudilin's second
Catalan recursion (math/0210423 §2) was not run — same construction class,
expected same verdict, unverified.  Project C's literature report is in
`work/KZ_ELLIPTIC_REPORT.md` — notably, the Koutschan–Zudilin elliptic
recurrences carry the SAME half-integer hypergeometric structure
(x^{n−1/2} integrands, (2n±1)-coefficients) as the Catalan recurrence
excluded here, supporting the view that the known non-sporadic L-value
recurrences are hypergeometric-realized, outside the modular-anchor class.
