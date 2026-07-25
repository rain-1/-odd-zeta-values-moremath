# P4 — the general (LB_w) theorem for the 15 sporadic Apéry-like pairs

**Author:** mathematician-agent (River's odd-zeta program), 2026-07-24
**Labels:** `[PROVED]` complete proof written here; `[VERIFIED r]` exact finite check on range r
(evidence, never proof); `[RECALLED-UNVERIFIED]` memory, not checked against a source.
Scripts: scratchpad `sporadic.py`, `t1b.py`, `t2_final.py`, `t2_diag.py`, `t2_twist.py`,
`t3_fit.py`, `t3_fit2.py`, `t4_proofcheck.py`, `deep.py`.

---

## EXECUTIVE SUMMARY — the headline

The naive law `p^w b_n a_q ≡ b_q a_n (mod p^w)` **is false for 7 of the 15 sporadic pairs**, and the
failure is not noise: it is governed by a **quadratic Dirichlet character χ attached to the
sequence**, and it is repaired by a single sign. The correct universal law is

> **(LB_w^χ)   v_p( p^w · B_n · A_q − χ(p) · B_q · A_n ) ≥ w,   q = ⌊n/p⌋,   p ≥ 5.**

**[VERIFIED, ZERO failures]** all 15 sporadic pairs; 28 primes 5 ≤ p ≤ 103; n ≤ 400 (all p) and
n ≤ 1200 for p = 5,7,11 (up to **5 base-p digits**); exact rational arithmetic. The floor is
**exactly w** in every single (sequence, prime) cell — perfectly flat, no κ-dependence, no
center-residue exception, no exceptional-digit exception.

χ is the character of the sequence's **Apéry limit**: the limit is a rational multiple of
`ζ(w)` (χ trivial) or of `L(χ_D, w)` (χ = χ_D). The correlation is 12/12 on the sequences whose
limit exists. Three sequences (**B, δ, η**) have **no archimedean Apéry limit at all** (their
characteristic roots are a complex-conjugate pair, so `B(n)/A(n)` oscillates forever) — yet the
p-adic descent (LB_w^χ) holds for them flat, with χ = χ_{−3}, trivial, χ_5 respectively. *The
p-adic Apéry limit exists where the archimedean one does not.*

The **mechanism** is a two-line lemma. For any Dirichlet character χ (χ ≡ 1 allowed) and y ≥ 0,

    p^r · K_χ^{(r)}(y)  =  χ(p) · K_χ^{(r)}(⌊y/p⌋)  +  p^r·(p-integral),      K_χ^{(r)}(y) := Σ_{m≤y} χ(m)/m^r,

because the p-divisible indices m = jp contribute χ(jp)(jp)^{−r} = χ(p)p^{−r}χ(j)j^{−r}. **The
factor χ(p) in (LB_w^χ) is exactly the χ(p) coming out of the p-divisible layer of the
harmonic weight.** Sequences whose second solution needs χ-twisted harmonic letters get χ(p);
sequences whose second solution is a pure ζ-harmonic monomial get +1.

Consistency check on that claim (T3): **the χ-twisted sequences provably admit no pure
harmonic-monomial decomposition**, and adding the χ-letters repairs it — verified for E.

---

## T1. The 15 sequences, their second solutions, limits and weights

Source for the sequence tables: **Malik–Straub, arXiv:1508.00297, Tables 1–2** (LaTeX source
fetched and read; Straub arXiv:2301.12248 §1 points there). All 15 binomial sums were
**[VERIFIED]** to reproduce the recurrence solution exactly for n ≤ 11.

Recurrences (u_{−1} = 0, u_0 = 1):

    (R2)  (n+1)² u_{n+1} = (a n² + a n + b) u_n − c n² u_{n−1}                        [Zagier's six]
    (R3)  (n+1)³ u_{n+1} = (2n+1)(a n² + a n + b) u_n − n(c n² + d) u_{n−1}           [AZ six (d=0) + Cooper three]

Second solution **B(n)**: `B(0) = 0`, `B(1) = 1`, recurrence enforced for n ≥ 1 (the n = 0 step is
degenerate — this is exactly Apéry's construction; Chamberland–Straub arXiv:2011.03400 use the
same normalisation, fetched). Scaling B by a p-unit rational does not affect (LB_w^χ), so this
normalisation is canonical for p ≥ 5 up to harmless constants.

| # | label | (a,b,c[,d]) | A(n) | Apéry limit L | w | χ |
|---|---|---|---|---|---|---|
| 1 | **A** (=ASZ (a)) | (7,2,−8) | Σ C(n,k)³ (Franel) | **ζ(2)/4** | 2 | 1 |
| 2 | **B** (=(f)) | (9,3,27) | Σ(−1)^k 3^{n−3k} C(n,3k)(3k)!/k!³ | **none** (complex char. roots) | 2 | χ_{−3} |
| 3 | **C** (=(c)) | (10,3,9) | Σ C(n,k)²C(2k,k) | **L_{−3}(2)/2** | 2 | χ_{−3} |
| 4 | **D** (=(b)) | (11,3,−1) | Σ C(n,k)²C(n+k,n) (Apéry ζ(2)) | **ζ(2)/5** | 2 | 1 |
| 5 | **E** (=(d)) | (12,4,32) | Σ C(n,k)C(2k,k)C(2(n−k),n−k) | **L_{−4}(2)/2 = G/2** (Catalan) | 2 | χ_{−4} |
| 6 | **F** (=(g)) | (17,6,72) | Σ(−1)^k 8^{n−k}C(n,k)Σ_l C(k,l)³ | **(5/8)·L_{−3}(2)** | 2 | χ_{−3} |
| 7 | **(α)** | (10,4,64,0) | Σ C(n,k)²C(2k,k)C(2(n−k),n−k) (Domb) | **7ζ(3)/24** | 3 | 1 |
| 8 | **(γ)** | (17,5,1,0) | Σ C(n,k)²C(n+k,n)² (Apéry ζ(3)) | **ζ(3)/6** | 3 | 1 |
| 9 | **(δ)** | (7,3,81,0) | Σ(−1)^k3^{n−3k}C(n,3k)C(n+k,n)(3k)!/k!³ (AZ) | **none** (complex char. roots) | 3 | 1 |
| 10 | **(ε)** | (12,4,16,0) | Σ C(n,k)²C(2k,n)² | **7ζ(3)/32** | 3 | 1 |
| 11 | **(ζ)** | (9,3,−27,0) | Σ_{k,l} C(n,k)²C(n,l)C(k,l)C(k+l,n) | **L_{−3}(3)/3** | 3 | χ_{−3} |
| 12 | **(η)** | (11,5,125,0) | Σ(−1)^k C(n,k)³[C(4n−5k−1,3n)+C(4n−5k,3n)] | **none** (complex char. roots) | 3 | χ_5 |
| 13 | **s₇** | (13,4,−27,3) | Σ C(n,k)²C(n+k,k)C(2k,n) | **ζ(2)/7** | 2 | 1 |
| 14 | **s₁₀** | (6,2,−64,4) | Σ C(n,k)⁴ | **ζ(2)/5** | 2 | 1 |
| 15 | **s₁₈** | (14,6,192,−12) | Cooper's s₁₈ | **L_{−3}(2)/2** | 2 | χ_{−3} |

**[VERIFIED]** Limits identified by 2-term PSLQ at 400 digits against a 33-constant basis
(ζ(2),ζ(3),ζ(4), L_D(2), L_D(3) for D = −3,−4,−7,−8,−11,−15,−20,−24,5,8,12,13,24, log²2, π²log2,
log³2), matching to 31–401 digits (the weakest, F, converges at rate (8/9)^n; s₁₈ at (3/4)^n).
Known values recovered: ζ(2)/4 for Franel and ζ(2)/5 for ΣC(n,k)⁴ (Cusick, via van der Poorten;
Chamberland–Straub eq. (7.2)); ζ(3)/6 for Apéry (classical). The rest — **7ζ(3)/24 (Domb),
7ζ(3)/32 (ε), L_{−3}(3)/3 (ζ), ζ(2)/7 (s₇), (5/8)L_{−3}(2) (F), L_{−3}(2)/2 (C and s₁₈),
L_{−4}(2)/2 (E)** — are computed here; they are of the shape Zagier and Yang predict
(rational multiples of ζ(2), L_{−3}(2), L_{−4}(2)) and several are presumably in
Almkvist–van Straten–Zudilin's numerical tables **[RECALLED-UNVERIFIED as citations]**.

**The three limit-less sequences (exception #1, a discovery).** For (R2) the characteristic roots
solve λ² − aλ + c = 0; for (R3), λ² − 2aλ + c = 0. Discriminants: **B: −27; δ: −128; η: −16** —
complex-conjugate pairs of equal modulus, so Poincaré–Perron gives no dominant solution and
B(n)/A(n) does **not** converge (numerically: 0 digits of agreement between n = 590 and n = 600,
against 380 for the convergent ones). Every other sporadic sequence has real distinct roots.
Yet all three satisfy (LB_w^χ) with a flat floor. This is the cleanest evidence in the whole
program that the descent is a **statement about Frobenius, not about the archimedean limit**.

**Weights and integrality.** `w` = the minimal exponent with `d_n^w · B(n) ∈ ℤ` (d_n = lcm(1..n)),
computed over n ≤ 600. **[VERIFIED]** w = 2 for all six of Zagier's (R2) sequences **and** for all
three of Cooper's (R3, d ≠ 0) sequences; w = 3 for all six Almkvist–Zudilin (R3, d = 0) sequences.
Sharp in every case (d_n^{w−1}B_n is non-integral for ≥ 596 of the 600 values of n). w always
equals the motivic weight of the Apéry limit. Per-prime integrality
`v_p(B_n) ≥ −w·⌊log_p n⌋` **[VERIFIED, 0 failures, 15 seqs × 16 primes × n ≤ 400]**.

---

## T2. The sweep — and the χ-twist

### T2a. The naive law and where it dies

`v_p(p^w B_n A_q − B_q A_n) ≥ w` (q = ⌊n/p⌋), primes 5..43, n ≤ 300, exact:

| verdict | sequences |
|---|---|
| holds flat, every prime tested | A, D, α, γ, δ, ε, s₇, s₁₀ (8) |
| **fails at p ≡ 2 (mod 3)** | B, C, F, ζ, s₁₈ (5) |
| **fails at p ≡ 3 (mod 4)** | E (1) |
| **fails at p ≡ ±2 (mod 5)** | η (1) |

The failures are total, not marginal: on the failing primes the single-digit floor is **0** (the
difference is a p-unit), and in the multi-digit range the valuation drops to −w·(#digits−1), i.e. as
low as the integrality bound permits. They are *not* explained by exceptional digits (p | A(a)),
by the centre residue, or by κ = v_p C(2n,n): the failing set is exactly the set of primes at which
a quadratic character takes the value −1. Cross-checks that isolate the character (all
**[VERIFIED]**): the passing primes of the χ_{−3} group are mixed mod 4 and mod 5; those of E are
mixed mod 3 and mod 5; those of η (11,19,29,31,41) are mixed mod 3 and mod 4 and are precisely
p ≡ ±1 (mod 5).

### T2b. The repair: one sign

**[VERIFIED, 0 failures]** at every χ(p) = −1 cell, for all 7 twisted sequences, all primes
5 ≤ p ≤ 31 with χ(p) = −1, n < p³ (up to 1500):

    v_p( p^w B_n A_q + B_q A_n ) = w exactly.

So the universal statement is (LB_w^χ) above. Final confirmation runs:

* **[VERIFIED, 0 failures]** 15 sequences × 16 primes {5,…,61} × n ≤ 400: master floor **exactly w**
  in all 240 cells; χ-twisted Lucas form `p^w B_{ap+r} ≡ χ(p)·B_a·A_r (mod p)` holds in all
  single-digit cells (0 failures); integrality `v_p(B_n) ≥ −w⌊log_p n⌋` 0 failures.
* **[VERIFIED, 0 failures]** 15 sequences × primes {5,7,11} with n ≤ 1200 (five base-p digits at
  p = 5) and primes {67,…,103} with n ≤ 400.

### T2c. Ramified primes

For η the prime p = 5 is ramified (χ_5(5) = 0). There (LB_w^χ) reads `p³B_n A_q ≡ 0 (mod p³)`,
which is exactly the statement that **B_n is 5-integral** — and **[VERIFIED, n ≤ 500]** it is:
`min_n v_5(B_n) = 0`, the pole simply does not develop at the ramified prime. Floor exactly 3.
(This is the only ramified prime ≥ 5 among the 15; the χ_{−3} and χ_{−4} sequences ramify only at
3 and 2.)

### T2d. p = 2, 3

Excluded, correctly: with the twisted law and n ≤ 120 the floor drops below w for A (p=2, floor 1),
F (p=2, 1), α (p=2, 2; p=3, 2), γ (p=3, 2), δ (p=3, 1), ε (p=2, 2). The p ≥ 5 boundary matches the
(CB)/sharp-12 boundary of the earlier campaign.

---

## T3. Harmonic decompositions

Method: exact linear fitting (the PROOF_LB5 technique). Ansatz
`B_n = Σ_k S(n,k)·w(n,k)` with `S` the sequence's binomial summand and `w` a ℚ-combination of
weight-w monomials in letters `H^{(r)}_x` (and, when needed, `K_χ^{(r)}_x = Σ_{m≤x} χ(m)/m^r`) at
arguments x that are linear forms in (n,k). Systems solved exactly mod the prime 2⁶¹−1, coefficients
rationally reconstructed, then **validated exactly over ℚ on held-out n**.

**Found (depth 1, all validated exactly on held-out n):**

| seq | w | decomposition `w(n,k)` (summand S as in the T1 table) | held-out |
|---|---|---|---|
| **γ** | 3 | `(1/3)H^{(3)}_n − (1/6)H^{(3)}_k` | n = 60..72 exact |
| **A** | 2 | `(1/4)H^{(2)}_k + (3/4)H_k(H_k − H_{n−k})` | n = 60..72 exact |
| **D** | 2 | `(1/5)[ H^{(2)}_n + H_k(2H_k − H_{n−k} − H_n) ]` | n = 60..72 exact |
| **s₁₀** | 2 | `(1/5)H^{(2)}_k + (4/5)H_k(H_k − H_{n−k})` | n = 60..72 exact |
| **s₇** | 2 | 8 terms in H^{(1,2)} at {k, n−k, n, 2k} | n = 60..72 exact |
| **ε** | 3 | 10 terms in H^{(1,2,3)} at {k, n−k, 2k, 2k−n} | n = 60..72 exact |
| **α** (Domb) | 3 | 14 terms in H^{(1,2,3)} at {k, n−k, 2k, 2n−2k} | n = 60..72 exact |
| **E** | 2 | `(1/2)K^{(2)}_{2k} + (3/4)H_k(K_{2k} − K_{2n−2k}) − (1/2)H_{2k}(K_{2k} − K_{2n−2k})`, K = K_{χ_{−4}} | n = 70..82 exact |

**The γ line is a new and startlingly simple closed form for Apéry's ζ(3) numerators**
(`b_n = 6B_n`):

> **b_n = Σ_{k=0}^n C(n,k)² C(n+k,n)² · ( 2H^{(3)}_n − H^{(3)}_k ).**

**[VERIFIED]** exactly for n = 1..90 (fit), n = 60..72 (held out), and by an **independent direct
re-implementation of the displayed formula**, n = 0..50, all differences exactly 0 — reproducing the
literature values b_n = 0, 6, 351/4, 62531/36, 11424695/288, 35441662103/36000, 20637706271/800.
(The E formula in the last row was likewise re-implemented directly and matches B_n exactly for
n = 0..50: 0, 1, 7, 404/9, ….) It replaces both Apéry's weight
`Σ_{m≤k}(−1)^{m−1}/(2m³C(n,m)C(n+m,m))` and the §3.1 form of PROOF_LB5_CAMPAIGN
`H^{(3)}_j + (2H_j − H_{n+j} − H_{n−j})H^{(2)}_j` (all three are equal; the fitting system has an
11-dimensional kernel, so the harmonic-monomial representation is far from unique — the pivot choice
delivered the shortest one). It is what makes the general proof below three lines long.

Structural note: **A and s₁₀ have literally the same shape** — `(1/(d+1))H^{(2)}_k + (d/(d+1))H_k(H_k − H_{n−k})`
for `A^{(d)}(n) = ΣC(n,k)^d` with d = 3, 4 — which is the natural source of Chamberland–Straub's
Conjecture (their eq. (7.4), limit ζ(2)/(d+1)) and suggests it for every d
**[VERIFIED d = 3,4 only; the d ≥ 5 recurrences have order ≥ 3 and were not tested]**.

**Negative results (exception #2, and it is structural):**

* **C**: no decomposition on the summand `C(n,k)²C(2k,k)` exists in *any* of the bases tried —
  plain harmonic monomials at {n,k,n−k,2k} (14 elts), at {n,k,n−k,2k,n+k,2n−2k,2n,2n−k} (44 elts),
  and with χ_{−3}-letters added (44 and 152 elts, 110 and 220 exact equations). **All inconsistent.**
* **E**: inconsistent in every *pure* harmonic basis tried (up to 44 elements, 8 arguments), and
  **consistent the moment χ_{−4}-letters are allowed**. This is the decisive experiment.
* **δ**: inconsistent in the weight-3 basis at {n,k,3k,n−3k,n+k} (65 elts, 110 equations).
* **B, F, ζ, η, s₁₈**: not attempted (double/alternating sums; ζ needs a genuine 2-index ansatz).

**The dichotomy.** A pure harmonic monomial `∏H^{(r_t)}_{x_t}` can only ever produce values in the
ring generated by ζ(2), ζ(3), … in the limit; it can never produce `L(χ,w)`. So *no* χ-twisted
sequence can have a pure-ζ harmonic decomposition, and the letters must be χ-twisted. This is
confirmed by E and is the reason C's plain fits are inconsistent. C's remaining obstruction is that
its conductor-3 letters need arguments not present in `C(n,k)²C(2k,k)`; the right move is
Gorodetsky's constant-term representation, not a bigger monomial basis. **[open]**

---

## T4. The general theorem

### Lemma K (the Frobenius descent of a harmonic letter) [PROVED]

Let χ be a completely multiplicative arithmetic function (a Dirichlet character; χ ≡ 1 allowed),
r ≥ 1, y ≥ 0, and set `K^{(r)}(y) = Σ_{m=1}^{y} χ(m)/m^r`. Then, as an identity in ℚ,

    p^r · K^{(r)}(y)  =  χ(p) · K^{(r)}(⌊y/p⌋)  +  p^r · T,        T := Σ_{m≤y, p∤m} χ(m)/m^r ∈ ℤ_(p).

*Proof.* Split the sum at p | m. The p-divisible part is Σ_{j≤⌊y/p⌋} χ(jp)(jp)^{−r} =
χ(p)p^{−r} Σ_{j≤⌊y/p⌋} χ(j)j^{−r}. The rest has p-integral terms. ∎

**This single line is the entire source of the χ(p) in (LB_w^χ).**

**Corollary K2.** If `M = ∏_{t=1}^{s} K_{χ_t}^{(r_t)}(x_t)` with Σ_t r_t = w and each
`K_{χ_t}^{(r_t)}(⌊x_t/p⌋) ∈ ℤ_(p)`, then

    p^w · M  ≡  (∏_t χ_t(p)) · ∏_t K_{χ_t}^{(r_t)}(⌊x_t/p⌋)   (mod p).

*Proof.* p^w M = ∏_t (p^{r_t}K_{χ_t}^{(r_t)}(x_t)) = ∏_t (χ_t(p)K_{χ_t}^{(r_t)}(⌊x_t/p⌋) + p^{r_t}T_t);
expand — every cross term carries a factor p and every factor is p-integral. ∎

### Theorem LB (general (LB_w) for the sporadic class) [PROVED]

Let p ≥ 5. Let

* `S(n,k) = ∏_i C(L_i(n,k), M_i(n,k))` with L_i, M_i integer linear forms, `A(n) = Σ_k S(n,k)`;
* `w(n,k) = Σ_j c_j ∏_{t} K_{χ}^{(r_{jt})}(x_{jt})`, a ℚ-combination of monomials of total weight
  `Σ_t r_{jt} = w`, in letters attached to one fixed quadratic character χ and to the trivial
  character, with x_{jt} integer linear forms in (n,k);
* `B(n) = Σ_k S(n,k) w(n,k)`.

Assume, for n = ap + r and k = bp + s with 1 ≤ a < p, 0 ≤ r,s < p:

**(H1) Lucas/carry dichotomy.** For every k either `p | S(n,k)`, or `S(n,k) ≡ S(a,b)S(r,s) (mod p)`.
**(H2) Product region.** The surviving set is `{0 ≤ b ≤ a} × Σ_r` for some `Σ_r ⊆ [0,p)`, and
`Σ_{s∈Σ_r} S(r,s) ≡ A(r) (mod p)`.
**(H3) Digit compatibility.** On the surviving set, `⌊x(n,k)/p⌋ = x(a,b)` for every argument form
x occurring in w.
**(H4) Tameness.** Every argument form satisfies `0 ≤ x(n,k) ≤ n` on the summation range; and
`c_j ∈ ℤ_(p)` for all j.
**(H5) χ-homogeneity.** Every monomial of w contains exactly the same number `e ∈ {0,1}` of
χ-letters (all others being trivial-character letters `H^{(r)}`).

Then for all 1 ≤ a < p, 0 ≤ r < p, with n = ap + r:

> **p^w · B(ap+r)  ≡  χ(p)^e · B(a) · A(r)   (mod p).**

*Proof.* By (H4), every argument satisfies x(n,k) ≤ n < p², hence ⌊x/p⌋ ≤ a < p and every letter
`K^{(r)}(⌊x/p⌋)` is p-integral; likewise `x(a,b) ≤ a < p`, so `w(a,b) ∈ ℤ_(p)` and, by (H4) again,
`p^w w(n,k) ∈ ℤ_(p)` for **every** k. Corollary K2 then gives, for every k,

    p^w w(n,k)  ≡  χ(p)^e · w̃(n,k)   (mod p),      w̃(n,k) := Σ_j c_j ∏_t K^{(r_{jt})}(⌊x_{jt}/p⌋),

and (H3) upgrades `w̃(n,k) = w(a,b)` on the surviving set. Now split

    p^w B(n) = Σ_{k : p | S(n,k)} S(n,k)·p^w w(n,k)  +  Σ_{k surviving} S(n,k)·p^w w(n,k).

The first sum is ≡ 0 (mod p): each `p^w w(n,k)` is p-integral and each S is divisible by p. In the
second, substitute (H1) and the displayed congruence:

    p^w B(n) ≡ χ(p)^e Σ_{b=0}^{a} Σ_{s∈Σ_r} S(a,b) S(r,s) w(a,b)
             = χ(p)^e ( Σ_{b=0}^{a} S(a,b) w(a,b) ) ( Σ_{s∈Σ_r} S(r,s) )
             ≡ χ(p)^e · B(a) · A(r)   (mod p),

using (H2) for both factors. ∎

**Remarks.**
1. With e = 0 and the γ-decomposition this **reproves the WARMUP_ZETA3 T3 theorem
   (`p³b_{ap+r} ≡ b_a a_r`, p ≥ 5) in three lines**, with no Lemma V, no T-fact, no Kummer ledger.
   The entire content of the old two-page proof is absorbed into "use a harmonic-monomial weight".
2. The hypotheses the mechanism really needs, in the language of the task brief: *summand with
   Lucas factorisation and carry annihilation* = (H1)+(H2) (this is exactly Malik–Straub's
   theorem, so it is available for all 15); *harmonic weight of depth 1* = the shape of w;
   *per-carry valuation ≥ 2* is **not** needed — it is replaced by (H4) tameness, which makes
   `p^w w` p-integral outright. Where tameness fails one needs a Lemma-D-style substitute.
3. **The master form** `v_p(p^w B_n A_q − χ(p)B_q A_n) ≥ w` (all n, all q = ⌊n/p⌋, mod p^w rather
   than mod p) is **[VERIFIED flat]** but **not proved here**: the theorem gives the mod-p,
   single-digit statement. The gap is the same one left open at weight 3 in WARMUP_ZETA3.
4. **Corollary (integrality).** Iterating the ratio form over base-p digits gives
   `v_p(B_n) ≥ −w·⌊log_p n⌋`, i.e. `d_n^w B_n ∈ ℤ_(p)` — the coefficient shadow of p-integrality of
   the mirror map (see BV below). **[VERIFIED independently, 0 failures]**.

### Which of the 15 fall inside

**[PROVED] — hypotheses (H1)–(H5) all verified, theorem applies:**

| seq | χ | primes | why (H4) holds |
|---|---|---|---|
| **γ** (Apéry ζ(3)) | 1 | p ≥ 5 | arguments {n, k}; coefficients 1/3, 1/6 |
| **A** (Franel) | 1 | p ≥ 5 | arguments {k, n−k}; coefficients 1/4, 3/4 |
| **D** (Apéry ζ(2)) | 1 | p ≥ 7 | arguments {n, k, n−k}; coefficients 1/5, 2/5 |
| **s₁₀** (ΣC(n,k)⁴) | 1 | p ≥ 7 | arguments {k, n−k}; coefficients 1/5, 4/5 |

(H1)–(H3) for these: for `S = C(n,k)^{α}C(n+k,n)^{β}` the surviving set is `{s ≤ r}` (no borrow in
C(n,k)) intersected with `{r+s < p}` (no carry in C(n+k,n)), a product region; there
`C(n,k) ≡ C(a,b)C(r,s)` and `C(n+k,n) ≡ C(a+b,a)C(r+s,r)` by Lucas, and the deleted `r+s ≥ p`
terms of A(r) vanish mod p — this is verbatim the T2 argument of WARMUP_ZETA3. Digit
compatibility: `⌊k/p⌋ = b`, `⌊(n−k)/p⌋ = a−b` (no borrow), `⌊n/p⌋ = a`. ✔

**[VERIFIED, exact, 0 failures]** of the two proof steps separately (vanishing layer ≡ 0 mod p;
surviving layer ≡ χ(p)B_aA_r mod p), all cells n = ap+r < p²:

* **γ, A, s₁₀: 0 failures at p = 5, 7, 11, 13** (both layers).
* **D: 0 failures at p = 7, 11, 13; 11 failing cells at p = 5** — exactly the coefficient
  condition of (H4) (D's coefficients are 1/5·(1,2,−1,−1)). So D's proof is unconditional for
  p ≥ 7; p = 5 is [VERIFIED] only.
* s₁₀'s coefficients are also 1/5·(1,4,−4) yet it shows no p = 5 defect — the layer valuations
  happen to be one higher there; the proof as written still needs p ≥ 7 for s₁₀.

No other defect of any kind appears in the tame cases: the only obstruction the mechanism ever
meets is the (H4) coefficient condition.

**Need the Lemma-D upgrade** — decomposition known, but **(H4) tameness fails** because arguments
reach 2n (letters at 2k / 2n−2k / 2k−n), so `p^w w(n,k)` acquires a pole in the vanishing layer:

* **α (Domb)**, **ε**, **s₇**, **E**.
  For these the two-layer split is *invalid termwise* — **[VERIFIED]** the vanishing-layer and
  surviving-layer defects occur in exactly equal numbers and cancel, which is why the congruence is
  nonetheless true. What is needed is precisely the analogue of the LB5 campaign's Lemma D: a
  valuation bound showing that a Kummer carry in the wide binomial (`C(2k,k)`, `C(2k,n)`) beats the
  order-1 pole of `H^{(r)}(⌊2k/p⌋)`. (s₇ additionally excludes p = 7: its coefficients have
  denominator 28. **[VERIFIED]** 13 failing cells at p = 7 and none at p = 5,11,13.)
* Notably **E is the only known instance of the twisted theorem (e = 1)**, and it is non-tame.
  Attempts to find a *tame* χ_{−4}-decomposition for E (arguments {n,k,n−k}, and {n,k,n−k,2k})
  were **[VERIFIED inconsistent]** — the wide arguments are essential. So the twisted case of
  Theorem LB is proved as a mechanism but has, at present, no tame instance.

**Remain conjectural** (no harmonic decomposition found; (LB_w^χ) is [VERIFIED] only):
**B, C, F, (δ), (ζ), (η), s₁₈.** Of these, C and δ have *proved-negative* results in the natural
bases (see T3), so they need genuinely new letters — for C the conductor-3 letters, for δ probably
letters attached to the 3-section of the summand.

---

## The relationship to Beukers–Vlasenko, *Dwork crystals III* (arXiv:2105.14841)

Read from the LaTeX source of the paper (fetched). §7 = "Completely symmetric Calabi–Yau
families". Numbering there is by subsection, so §7's numbered items are 7.1 definition
(completely symmetric), 7.2 lemma (hw⁽²⁾), 7.3 theorem (`excellent-example2`), 7.4 remark,
**7.5 conjecture** (`congruence-mod-p2s`). Setting: `f(x) = 1 − t g(x)`, `F(t) = Σ_n f_n t^n` with
`f_n = ` constant term of `g(x)^n` — for the sporadic families these `f_n` are exactly our `A(n)`.
`F_N(t)` is the truncation of F at t^N. `G(t)` is defined by the second solution
`F(t) log t + G(t)` of the (second-order) Picard–Fuchs operator — **its coefficients are our
second solution B(n)**, up to normalisation.

**What BV prove (their eq. (7.6), from BV-II eq. (7)):** for every m, s ≥ 1,

    F(t)/F(t^σ)  ≡  F_{m p^s}(t) / F_{m p^{s−1}}(t^σ)   (mod p^s).

Read off coefficients with the naive lift t^σ = t^p, s = 1: this is the Dwork/Mellit–Vlasenko
congruence whose sporadic specialisation is the **A-row Lucas congruence
`A(ap+r) ≡ A(a)A(r) (mod p)`** — the theorem of Gessel / Malik–Straub / Straub 2301.12248.

**What BV Conjecture 7.5 says:** the same congruence holds **modulo p^{2s}**, for `m = 2` in the
hypercubic and hyper-octahedral families and `m = n+1` in the simplicial families, where σ is the
**excellent Frobenius lift** — the unique lift with `q^σ = γ^{p−1} q^p` for the canonical
(mirror) coordinate `q(t) = t·exp(G(t)/F(t))` (their Definition, and Theorem 7.3: for that lift
the Cartier operator satisfies `𝒞(1/f) ≡ (F(t)/F(t^σ))(1/f^σ) mod p²fil₂`, i.e. the off-diagonal
Frobenius entry λ₁ vanishes identically). BV state they could not prove it for a single g.

**Precise relationship to (LB_w^χ).**

1. **They are the two rows of one 2×2 Frobenius matrix.** BV's crystal `CY(g)(2)` is free of rank 2
   on `1/f, θ(1/f)`; its Frobenius has diagonal `(λ₀, λ₂)` with `λ₀ = F(t)/F(t^σ)` the unit root.
   BV 7.5 is a statement about **λ₀ alone**, sharpened from mod p^s to mod p^{2s}. (LB_w^χ) is the
   statement about the **other** diagonal entry: that Frobenius acts on the second graded piece with
   eigenvalue `χ(p)·p^w`. In coefficient form BV's λ₀-congruence *is* the A-row; ours *is* the
   B-row. **Neither formally implies the other.**
2. **But 7.5's hypothesis is our conclusion's weak form.** Conjecture 7.5 is only stated for the
   *excellent* lift, and the excellent lift exists as a lift of ℤ_p[[t]] precisely because
   `q(t) = t exp(G/F) ∈ ℤ_p[[t]]` — BV's Corollary (p-integrality of the mirror map), which is a
   statement about G, i.e. about B(n). Our Corollary in T4 (`d_n^w B_n ∈ ℤ_(p)`, obtained by
   iterating (LB_w^χ) over base-p digits) is exactly the coefficient-level shadow of that
   integrality, **sharpened**: it does not merely assert p-integrality of the mirror map, it
   pins the depth at exactly w and exhibits the χ(p) eigenvalue. So the implication runs
   **(LB_w^χ) ⟹ (coefficient form of BV's mirror integrality) ⟹ (the excellent lift is defined
   over ℤ_p[[t]])**, which is the standing hypothesis of Conjecture 7.5. In this precise sense
   (LB_w^χ) is *upstream* of 7.5, not equivalent to it.
3. **The χ is invisible in BV's formulation and must be added.** BV work with `λ₀ = F/F^σ` where no
   character can appear (the unit root of the holomorphic period is a unit, and the A-row Lucas
   congruence is untwisted for all 15 — [VERIFIED] here and proved by Malik–Straub). The character
   only surfaces on the **non-unit** eigenvalue. Any crystal-theoretic proof of (LB_w^χ) must
   therefore carry the information that, for 7 of the 15 families, the second Frobenius eigenvalue
   is `χ(p)p^w` and not `p^w` — i.e. the family is the one attached to a CM/quadratic-twisted
   modular parametrisation. **This is a concrete correction to make to any "Dwork crystals ⟹
   Lucas congruences for the second solution" slogan.** [RECALLED-UNVERIFIED that BV or
   Vargas-Montoya state a second-solution version anywhere; I did not find one in the fetched
   source of 2105.14841.]
4. What (LB_w^χ) does **not** give: nothing towards the mod-p^{2s} *doubling* which is the actual
   content of 7.5. Our floor is exactly w and provably not more (equality is attained in every
   cell), so there is no hidden supercongruence in the B-row of the kind 7.5 predicts for the A-row.

---

## Exceptions, restated (these are the discoveries)

1. **The χ-twist.** 7 of the 15 sporadic pairs violate the untwisted descent, at exactly the primes
   where a quadratic character is −1: χ_{−3} for **B, C, F, (ζ), s₁₈**; χ_{−4} for **E**;
   χ_5 for **(η)**. All are repaired by the single factor χ(p), and the repaired law is flat with
   floor exactly w. χ is the character of the Apéry limit (12/12 where the limit exists).
2. **Three sequences have no archimedean Apéry limit at all** — **B, (δ), (η)** — because their
   characteristic roots are complex conjugates of equal modulus. They still satisfy (LB_w^χ)
   flat. The p-adic Apéry limit survives where the archimedean one does not.
3. **Cooper's three (s₇, s₁₀, s₁₈) have weight 2, not 3**, despite living in the (n+1)³ recurrence
   family: the weight tracks `d ≠ 0`, i.e. the Cooper deformation, not the recurrence's shape.
4. **A new, minimal closed form for Apéry's ζ(3) numerators**:
   `b_n = Σ_k C(n,k)²C(n+k,n)²(2H^{(3)}_n − H^{(3)}_k)`.
5. **Sequence C admits no harmonic-monomial decomposition on its own summand**, even with
   χ_{−3}-letters, in bases up to 152 elements with 220 exact equations. Its L_{−3}(2) needs
   conductor-3 arguments the summand does not provide.
6. **The ramified prime is benign**: at p = 5 for (η), χ(5) = 0 and the pole in B_n simply does not
   form (`v_5(B_n) ≥ 0` for all n ≤ 500). The twisted law degenerates to the true statement
   `p^w B_n A_q ≡ 0`.
