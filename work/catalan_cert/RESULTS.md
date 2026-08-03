# Catalan companion: certificate proof + twisted Lucas corollary

Date: 2026-08-02.  Everything below is machine-verified exact arithmetic;
scripts in this directory.

## Theorem (was Conjecture `conj:Catalan` in papers_out/harmonic_jets)

With S(n,k) = C(n,k)C(2k,k)C(2n-2k,n-k) and
w(n,k) = ½K2_{2k} + (¾H_k − ½H_{2k})(K1_{2k} − K1_{2n−2k})  (K = χ₋₄-harmonics),
the sum B_E(n) = Σ_k S(n,k)w(n,k) satisfies

    (n+1)² u_{n+1} = (12n²+12n+4) u_n − 32n² u_{n−1}     for all n ≥ 1.

Hence B_E is the normalized second solution (B_E(0)=0, B_E(1)=1) and its
Apéry limit is G/2 (Catalan).  **Observation obs:Catalan is now a theorem.**

## Proof structure (creative telescoping with an order-4 pre-operator)

No single telescope exists: the (−1)^k·H_k sector of the cell identity has no
rational Gosper solution (an exact obstruction, as in the ζ(2) case, which
needed an order-2 pre-operator).  Here the minimal scalar pre-operator has
order 4 and is parity-dependent:

    P = p0(n) + p1(n)E + p2(n)E² + p3(n)E³ + p4(n)E⁴,   E: n → n+1,

with explicit polynomials p_i (two branches, e = (−1)^n = ±1; see
`stage6.py`, degrees ≤ 14).  Then

    Ψ(n,k+1) − Ψ(n,k) = Σ_{i=0}^{4} p_i(n)·C(n+i,k)                    (*)

holds identically, where C(n,k) is the recurrence cell of B_E's summand and

    Ψ(n,k) = S(n,k)·Σ_m c_m(n,k)·M_m

is a finite letter combination: M_m runs over the 10 monomials
{K2a, HkK1a, HkK1b, H2K1a, H2K1b} (weight 2), {σHk, σH2, K1a, K1b, σ} with
σ = (−1)^k, and the c_m are explicit rational functions (10 per parity,
`final_certificate.pkl`).

- (*) was solved by grading the cell in the letter monomials and solving the
  resulting first-order rational recurrences top-down in weight (Abramov
  universal denominators + linear algebra); the pre-operator was found as the
  1-dimensional nullspace of the joint solvability system (exact modular
  linear algebra mod 2¹²⁷−1 at 84 sample n, rational-function reconstruction,
  then symbolic re-derivation and exact symbolic checks: `stage6.py` asserts).
- Boundary: Ψ(n,0) = 0 identically, and the boundary strip k ∈ [n, n+4]
  (where the literal shell vanishes but the shifted cells do not) cancels
  against Ψ(n,n) — proved symbolically in the finite alphabet
  {H_n, H_{2n}, K1_{2n}, K2_{2n}} over Q(n,e) (`strip2.py`: HOLDS, both
  parities).
- Summing (*) over k: the defect g(n) = (n+1)²B_E(n+1) − (12n²+12n+4)B_E(n)
  + 32n²B_E(n−1) satisfies Σ p_i(n) g(n+i) = 0 for n ≥ 1;
  p4(n) = (cleared common denominator) has no zeros at positive integers
  (checked n ≤ 199 + leading-term domination); g(1)=…=g(4)=0 exactly.
  Induction gives g ≡ 0.

Independent verification: the full identity (*) checked in exact rational
arithmetic with real harmonic values on a grid n=4..12 (interior k), summed
identity zero for n=4..12, and the recurrence itself verified exactly for
n ≤ 59.

## Corollary (character-twisted Lucas congruence for the companion)

For odd primes p and single digits 0 < m < p, 0 ≤ r < p/2 (and digit values
p-integral):

    p²·B_E(pm+r)  ≡  p²·A_E(m)·B_E(r) + χ₋₄(p)·B_E(m)·A_E(r)   (mod p).

Equivalently, the pair (A_E, B_E) transforms under n ↦ pn+r by the
lower-triangular twisted Frobenius

    ( A_E )          ( A_E(r)                    0      ) ( A_E(m) )
    ( B_E ) (pm+r) ≡ ( B_E(r)     χ₋₄(p)·p⁻²·A_E(r)     ) ( B_E(m) )   (mod p·p⁻²),

i.e. the weight-2 harmonic weight is a Frobenius degree p⁻² with character
eigenvalue χ₋₄(p) — the exact prediction of the character-resolved Lucas
descent (Section "Character-resolved Lucas descent" of the paper), now
exhibited on an explicit sporadic companion.

Verified exhaustively for p ∈ {5,7,11,13,17,19}, all single-digit (m,r) in
range with p*m+r ≤ 260: zero failures (`RESULTS` scripts in this session; the
first failures occur exactly at m ≥ p, and naive digitwise iteration fails —
consistent with the paper's single-digit-honest statement and the open
divided-power multi-digit direction).

## Files

- `certificate.py`  — letter algebra, cell computation, rational solver (validated
  against literal values; the σ-shift convention bug found and fixed here).
- `preop.py`        — per-shift weight-2 reduction, residual assembly (ORDER=4).
- `scan3.py`        — modular sector-sequential nullspace scan (pre-operator search).
- `fit_mod.py`      — rational-function reconstruction of p_i(n) from samples.
- `stage6.py`       — symbolic completion; writes `final_certificate.pkl`.
- `strip2.py`       — symbolic boundary-strip identity (HOLDS, both parities).
- `verify.py` (+ inline session scripts) — independent exact-arithmetic checks.

## Paper actions suggested

- Upgrade Observation obs:Catalan and Conjecture conj:Catalan to theorems,
  citing the order-4 parity-split pre-operator certificate.
- Add the corollary above as the promised "arithmetic consequence"; it is the
  first explicit Lucas-type congruence for a sporadic second solution.
- The verified range of the closed form can be bumped from n ≤ 30 to n ≤ 80
  (session check), and the recurrence n ≤ 59 independent of the certificate.
