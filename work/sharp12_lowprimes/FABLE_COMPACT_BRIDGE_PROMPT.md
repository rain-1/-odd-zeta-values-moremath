# Fable handoff: prove the compact Brown--Zudilin weight-five bridge

You are being handed one sharply isolated mathematical proof obligation.  A
finite check, recurrence guess, modular rank computation, or statement that a
certificate ought to exist is **not** completion.  We need an all-`n` proof or
an explicit certificate that can be checked as an exact rational identity.

## 1. The theorem to prove

For `m >= 0` and `r >= 1`, put

\[
H_m^{(r)}=\sum_{j=1}^m\frac1{j^r},\qquad H_0^{(r)}=0.
\]

For `0 <= k,l <= n`, define

\[
T(n,k,l)=\binom{n+k}{n}\binom nk^2
         \binom{n+l}{n}\binom nl^2\binom{n+k+l}{n},
\]

\[
\begin{aligned}
A_r(x)&=H_{n+x}^{(r)}-H_x^{(r)},\\
B_r(x)&=H_{n-x}^{(r)}-H_x^{(r)},\\
\alpha&=A_1(k)-A_1(l),\\
\beta&=B_1(k)-B_1(l),
\end{aligned}
\]

and the asymmetric compact weight

\[
\boxed{
\omega_5(n,k,l)=H_{n+k}^{(5)}
+\frac{\alpha-\beta}{2}H_{n+k}^{(4)}
+\frac{A_2(k)+A_2(l)-\alpha^2-2\alpha\beta}{4}
 H_{n+k}^{(3)}.}
\tag{W5}
\]

Set

\[
S_n=\sum_{k=0}^n\sum_{l=0}^nT(n,k,l)\omega_5(n,k,l).
\tag{S}
\]

Let `P_n` be the Brown--Zudilin top companion in the normalization

\[
P_0=0,\qquad P_1=\frac{87}{4},\qquad
P_2=\frac{1190161}{384},
\]

annihilated by the Brown--Zudilin order-three recurrence `L_BZ`.  Its exact
coefficients are authoritative in `work/lb5/core.py`, functions `c0`--`c3`.

### Required theorem

\[
\boxed{S_n=P_n\qquad\text{for every }n\ge0.}
\tag{BRIDGE}
\]

This is the only missing bridge needed to transfer the already-proved binary
and ternary endpoint-residue theorem from the compact sum to the actual
recurrence-defined companion.

## 2. What immediately follows

The all-`n` endpoint theorem for `S_n` is already proved.  Therefore (BRIDGE)
immediately gives

\[
v_2(P_n)\ge-2-5\lfloor\log_2n\rfloor,
\qquad
v_3(P_n)\ge-1-5\lfloor\log_3n\rfloor.
\]

Equivalently, the low-prime contribution to the sharp denominator is exactly
`2^2 * 3 = 12`.  At `p=2` the proof has two exceptional cells with normalized
residues `-1,+1 mod 4`.  At `p=3` it has

\[
3^{1+e_1(r)}
\]

exceptional cells, all with residue `-1 mod 3`, where `n=2*3^L+r` and `e_1(r)`
counts ternary digits equal to one.  Do not redo this endpoint proof unless you
find an error; the bridge is the bottleneck.

## 3. Acceptable proof routes

### Route A: recurrence plus exact creative telescoping

Prove directly that `S_n` is annihilated by `L_BZ`, including every boundary
term, and check `S_0,S_1,S_2=P_0,P_1,P_2`.  A successful deliverable may be

\[
L_{\rm BZ}(T\omega_5)
=\Delta_k R(n,k,l)+\Delta_l U(n,k,l)
\]

with explicit rational/harmonic certificates `R,U`, or a two-stage
telescoping certificate whose intermediate recurrence is also explicit.

It is permissible to use a left multiple `M=A L_BZ` if:

1. `M S=0` is certified exactly;
2. the additional initial values needed by `M` are proved from (S);
3. exact right division or a recurrence-uniqueness argument removes the extra
   factor and proves `L_BZ S=0`.

A pre-operator is promising: in the zeta(2) problem, a direct telescope did
not exist but an order-two left multiple telescoped cellwise.

### Route B: Barnes/residue identity

Use the bivariate Barnes kernel and prove that its rational coefficient equals
`-2 S_n`.  The local partial fractions are already proved:

\[
(-1)^n n! C_{22}=T,
\quad C_{12}/C_{22}=L_k,
\quad C_{21}/C_{22}=L_l,
\quad C_{11}/C_{22}=L_kL_l-C_2.
\]

The universal sine-kernel evaluation is explicit.  The unwanted zeta(4),
zeta(3), and zeta(2)/weight-three coefficients have already been removed by
uniform residue identities.  The remaining obligation is precisely the
rational/compact-weight-five identity in `work/Z5CF_BARNES.md`.

A particularly attractive proof would express the residual as a finite sum of
Laurent coefficients forced to vanish by

\[
R_n(x,m-x)\equiv0\qquad(1\le m\le n)
\]

or by the numerator zeros of the one-variable functions `g_l,q_l`, with all
ranges and endpoint terms explicit.

### Route C: Zudilin partial fractions

Zudilin's proved one-variable construction gives coefficients `C_{s,j}` with

\[
p_n=\sum_{j=0}^n\sum_{s=1}^6C_{s,j}H_j^{(s)},\qquad
P_n=\frac{(-1)^{n+1}p_n}{\binom{2n}{n}}.
\]

They satisfy

\[
C_{s,n-j}=(-1)^{s+1}C_{s,j}
\]

and the exact zero moments

\[
\sum_{s\le\min(6,r)}\sum_j
(-1)^{r-s}\binom{r-1}{r-s}j^{r-s}C_{s,j}=0,
\qquad1\le r<4n+3.
\]

An exact transformation of this one-dimensional formula into (S) proves the
bridge.  Alternatively, an unconditional proof of the two low-prime bounds
directly from these partial fractions also completes the denominator goal,
even if (BRIDGE) remains separate.  If taking this alternative, state clearly
that it proves sharp-12 but not the compact identity.

## 4. The epsilon-defect formulation

There is an explicit gamma deformation whose fifth Bell coefficient is `B_5`.
With

\[
\Delta_5=B_5-\frac{33}{4}\omega_5^{\rm sym},
\]

the desired compact comparison is equivalent to a weight-five residue
identity, provided the deformation-to-`P_n` coefficient is proved rather than
assumed.  Be careful: both

\[
\sum T B_5=\frac{33}{4}P_n
\quad\text{and}\quad
\sum T\Delta_5=0
\]

have extensive exact verification, but verification is not a proof.

What is known structurally:

* `sym(Delta_5)` belongs to the full per-fixed-variable kernel in saturated
  modular computations at two primes;
* hence no genuinely two-variable cancellation appears necessary;
* the current constructive residue generators have symmetric rank `419` and
  miss the target by exactly one dimension;
* adding elementary-symmetric cancellations on every zero range gives valid
  new generators but still leaves the target outside their span;
* enlarging the first anti-diagonal Laurent family by the natural affine
  endpoint weights also fails to close the residual.

The likeliest missing object is therefore a weighted or nested endpoint jet,
not another unweighted power sum or elementary symmetric polynomial.

## 5. Completion standard

Any one of the following is sufficient:

1. an exact telescoping certificate proving `L_BZ S=0`, together with exact
   initial values;
2. a finite Barnes/residue decomposition of the rational coefficient into
   explicitly proved zero functionals;
3. an exact algebraic transformation from Zudilin's proved partial-fraction
   formula to (S);
4. an independent all-`n` proof of the desired `2`- and `3`-adic bounds for
   recurrence-defined `P_n` (this proves sharp-12 but should not be described
   as proving (BRIDGE)).

For a machine certificate, provide both:

* the search output in a stable machine-readable format;
* an independent checker that performs exact arithmetic and verifies the
  certificate without trusting the search package.

The checker must verify shift ratios, the complete rational identity, natural
boundaries, and the required initial values.  No floating point.  Modular
checks may supplement but may not replace the exact checker.

## 6. Do not report these as proofs

The following are evidence only:

* agreement for `n <= N`, however large;
* satisfaction of `L_BZ` for finitely many indices;
* a guessed minimal recurrence;
* equal ranks modulo one or more primes;
* membership in a kernel sampled at finitely many cells;
* the assertion that creative telescoping guarantees some unspecified
  certificate exists.

If a route fails, preserve the exact negative result and identify the missing
dimension or obstruction.  Do not silently replace (BRIDGE) by a nearby
verified statement.

## 7. Authoritative files

Read these first:

* `work/sharp12_lowprimes/ENDPOINT_BREAKTHROUGH.md` -- theorem boundary and
  exact low-prime structure;
* `work/sharp12_lowprimes/ENDPOINT_RESIDUE_PROOF.md` -- completed endpoint
  proof;
* `work/Z5CF_BARNES.md` -- Barnes reduction and the remaining rational bridge;
* `work/Z5CF_EPSILON.md`, especially Section 12 -- Bell defect and residue
  generators;
* `work/Z5_ORDER0.md`, especially (L1)--(L5) -- bivariate zero identities;
* `work/lb5/core.py` -- authoritative `T`, `P`, and `L_BZ` normalization;
* `work/z5eps/eps22.py` -- full-kernel membership formulation;
* `work/z5eps/eps24.py`, `eps25.py`, `eps26.py` -- constructive generator
  searches and the one-dimensional residual;
* `work/sharp12_lowprimes/verify_compact_endpoint_residues.py` -- exact audit
  of the proved endpoint theorem;
* `work/sharp12_lowprimes/verify_zudilin_endpoint.py` -- exact reconstruction
  of Zudilin's partial fractions and zero moments;
* `papers_out/sharp12/sharp12.tex`, Section ``The primes 2 and 3'' -- paper
  statement and consequence.

Related source papers are present locally:

* `papers/20-brown-zudilin-2022-cellular-rational-approx-zeta5/`
* `papers/04-zudilin-2002-arithmetic-of-linear-forms/`

## 8. Desired final report

Lead with exactly one of:

* **PROVED (BRIDGE)**, followed by the certificate/proof and checker;
* **PROVED SHARP-12 BY AN ALTERNATE ROUTE**, while explicitly leaving
  (BRIDGE) open;
* **NOT YET PROVED**, followed by the strongest exact reduction and the next
  concrete certificate problem.

The prize is an unconditional explanation of the factor `12`: the binary
pair cancellation and ternary fibre cancellation are already in hand; only
their attachment to the Brown--Zudilin companion remains.
