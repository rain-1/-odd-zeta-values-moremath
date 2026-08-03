# Lessons from the General Endpoint-Denominator Theorem

## Purpose

This note records the structural ideas revealed by the general
endpoint-denominator theorem.  It separates statements already proved from
conjectural extensions and gives a concrete program for applying the method to
other harmonic companions and Apéry-like recurrences.

Throughout,

\[
L_n=\operatorname{lcm}(1,2,\ldots,n),\qquad L_0=1.
\]

## 1. The proved theorem

For an integer \(b\), let \(B^{(b)}\) be the normalized rational solution

\[
B^{(b)}_0=0,\qquad B^{(b)}_1=1,
\]

\[
(n+1)^2B^{(b)}_{n+1}
=b(3n^2+3n+1)B^{(b)}_n-2b^2n^2B^{(b)}_{n-1}.
\tag{1}
\]

Define its endpoint binomial transform by

\[
T^{(b)}_n=\sum_{k=0}^n\binom nk(-b)^{n-k}B^{(b)}_k.
\tag{2}
\]

Then

\[
(n+1)^2T^{(b)}_{n+1}-b^2n^2T^{(b)}_{n-1}=(-b)^n,
\tag{3}
\]

and, for \(n\geq1\),

\[
(-1)^{n-1}T^{(b)}_n
=b^{n-1}
\sum_{\substack{0\leq j<n\\n-j\ \mathrm{odd}}}
P_{n,j}^2,
\qquad
P_{n,j}=
\frac{(j+2)(j+4)\cdots(n-1)}
     {(j+1)(j+3)\cdots n}.
\tag{4}
\]

The exact uniform denominator classification is

\[
\boxed{
  L_n^2B^{(b)}_n\in\mathbb Z\text{ for every }n
  \quad\Longleftrightarrow\quad
  4\mid b.}
\tag{5}
\]

The positive direction uses the stronger endpoint fact

\[
L_n2^{n-1}P_{n,j}\in\mathbb Z.
\tag{6}
\]

If \(b=4d\), every contribution to \(L_n^2T^{(b)}_n\) is therefore

\[
d^{n-1}\bigl(L_n2^{n-1}P_{n,j}\bigr)^2\in\mathbb Z.
\]

Binomial inversion transfers this integrality to \(B^{(b)}_n\).  Necessity is
already detected by

\[
B^{(b)}_4=\frac{2603b^3}{576},\qquad
B^{(b)}_8=\frac{6802537507b^7}{180633600}.
\tag{7}
\]

The first value forces \(b\) to be even.  If \(b=2d\) with \(d\) odd, the
second gives

\[
L_8^2B^{(b)}_8=\frac{6802537507d^7}{2}\notin\mathbb Z.
\]

## 2. Endpoint decoupling is a rigid normal form

Consider the more general quadratic recurrence

\[
(n+1)^2u_{n+1}
=\{\alpha n(n+1)+\beta\}u_n-\gamma n^2u_{n-1}.
\tag{8}
\]

Under a binomial shift with nonzero parameter \(h\), its ordinary
generating-function operator becomes

\[
\begin{aligned}
\theta^2
&-z\{(\alpha-3h)(\theta^2+\theta)+(\beta-h)\}\\
&+z^2(\gamma-2\alpha h+3h^2)(\theta+1)^2\\
&+z^3h(\gamma-\alpha h+h^2)(\theta+1)(\theta+2).
\end{aligned}
\tag{9}
\]

The interior \(z\)-term vanishes only if

\[
\alpha=3h,\qquad \beta=h.
\]

Subject to these equations, the \(z^3\)-term vanishes only if

\[
\gamma=2h^2.
\]

Thus (1), with \(h=b\), is exactly the nontrivial endpoint-decoupling locus
inside (8).  The two-step relation (3) is forced by the conjugated operator;
it is not an accidental cancellation special to one sequence.

This suggests treating binomial conjugation as a search for a normal form of a
recurrence, analogous to diagonalizing a linear transformation when the
appropriate basis exists.

## 3. Why the number four appears

Formula (4) separates the recurrence into its two parity chains.  The odd-prime
parts of the denominator of \(P_{n,j}\) are absorbed by \(L_n\).  The remaining
defect is the power of two created by interlacing the even and odd factors.

Because the endpoint quotient is squared, the required correction is

\[
(2^{n-1})^2=4^{n-1}.
\]

The factor \(b^{n-1}\) supplies this correction uniformly precisely when
\(4\mid b\).  Hence the modulus four is not an experimental artifact.  It is
the arithmetic signature of a *squared parity chain*.

This separates two roles cleanly:

* \(L_n\) absorbs the ordinary prime denominators;
* divisibility of the recurrence parameter absorbs the residual denominator
  caused by the endpoint step size.

## 4. Global sufficiency versus finite obstruction

There is a useful asymmetry in the proof.

* Sufficiency is global: it uses the complete endpoint expansion and a
  prime-by-prime denominator argument.
* Necessity is local: the indices \(4\) and \(8\) already detect the entire
  obstruction.

This leads to a general research strategy for parameterized recurrences:

1. conjugate the recurrence and prove integrality globally in the transformed
   basis;
2. calculate a modest number of exact initial terms;
3. use their valuations to find sharp necessary congruence conditions on the
   parameters;
4. compare the local obstruction with the global sufficient condition.

When the two coincide, a computational observation becomes an exact
classification.

## 5. Analytic equivalence can conceal arithmetic inequivalence

For \(n\geq1\), the family satisfies the simple dilation identity

\[
B^{(b)}_n=b^{n-1}B^{(1)}_n.
\tag{10}
\]

Consequently the different values of \(b\) do not give essentially new
analytic solutions.  They do, however, give genuinely different integral
structures.  Theorem (5) determines exactly which dilations repair the
uniform denominator defect of the universal rational sequence \(B^{(1)}\).

This is a general warning and opportunity: rescalings that are trivial over
\(\mathbb Q\) can be highly nontrivial over \(\mathbb Z\) or \(\mathbb Z_p\).

## 6. Binomial conjugation as an arithmetic microscope

The original three-term recurrence mixes neighboring indices and conceals its
denominators.  The transformed recurrence (3) splits into independent parity
chains.  Iteration then reveals squares of elementary product quotients.

In this example a single change of basis exposes simultaneously:

* an explicit finite formula;
* positivity after removal of a predictable sign;
* the source of the denominator exponent two;
* the exact parameter obstruction;
* a short route to formal verification.

This supports the broader principle:

> A sharp denominator theorem may become elementary only after the recurrence
> is expressed in the basis adapted to its endpoints.

## 7. A reusable discovery algorithm

The proof suggests the following pipeline for other Apéry-like recurrences.

1. **Operator extraction.** Convert the recurrence, including its initial
   residual, into an inhomogeneous ordinary generating-function equation.
2. **Parameterized conjugation.** Apply a binomial or generalized binomial
   substitution with an undetermined shift parameter.
3. **Locus solving.** Equate unwanted operator coefficients to zero and solve
   the resulting algebraic equations in the recurrence parameters.
4. **Endpoint iteration.** Iterate the decoupled recurrence separately on its
   residue classes.
5. **Product recognition.** Rewrite the resulting products as factorial,
   double-factorial, or multifactorial quotients.
6. **Valuation analysis.** Treat ordinary prime denominators with \(L_n\) and
   isolate the residual primes caused by the step size.
7. **Sharpness search.** Compute exact low-index terms and locate finite
   valuation witnesses for necessity.
8. **Inverse transform.** Transfer integrality, congruences, or positivity back
   to the original companion.

Most stages are amenable to symbolic automation.  The human mathematical work
is concentrated in recognizing the product structure and proving its sharp
valuation bound.

## 8. Connection with harmonic companions

The harmonic formula and the endpoint formula describe the same companion in
two different bases.

* The harmonic basis explains how the companion is produced from a
  hypergeometric shell by differentiation or lifting.
* The endpoint basis explains why the resulting rational numbers have much
  smaller denominators than their individual harmonic summands suggest.

This motivates a stronger working hypothesis:

> Minimal harmonic formulas and sharp denominator theorems are often two
> shadows of the same hidden conjugation.

If correct in broader families, the harmonic alphabet can guide the search for
the companion, while the endpoint normal form can prove its arithmetic
properties.  Neither description alone has to carry the entire proof.

## 9. Extensions and conjectures

The step-size prediction in the original version of this note has now been
proved exactly.  The proposed connection with actual higher-weight harmonic
companions remains conjectural.

### 9.1 Higher harmonic weight

A weight-\(r\) companion may, after the appropriate conjugation, produce
endpoint contributions resembling

\[
P_{n,j}^{,r}.
\]

If the same parity quotient controls the denominator, one would expect a
uniform parameter threshold involving \(2^r\).  The naive conjectural model is

\[
2^r\mid b,
\]

but this must be tested carefully: mixed harmonic words may introduce cross
terms rather than pure powers, and cancellations can lower the threshold.

### 9.2 Endpoint chains of step \(q\): now proved

For a pure weight-\(w\), step-\(q\) endpoint chain, the residual denominator is
supported exactly on the primes dividing \(q\).  Its sharp modulus is

\[
M(q,w)=\prod_{p\mid q}p^{\left\lceil
 \frac{w}{q}\left(v_p(q)+\frac1{p-1}\right)
\right\rceil}.
\]

Thus the exponent depends not merely on the weight but on the density of the
corresponding multifactorial chain.  For prime step \(q=\ell\), this simplifies
to

\[
M(\ell,w)=\ell^{\lceil w/(\ell-1)\rceil}.
\]

The complete theorem and proof are in
`work/harmonic_jets/SHARP_STEP_Q_ENDPOINT_THEOREM.md`.  The parity-square result
is precisely \((q,w)=(2,2)\), for which \(M(2,2)=4\).

There is now also a natural mixed step-three realization.  The binomial
conjugate of Zagier's sporadic sequence \(\mathbf B\), with recurrence
parameters \((9,3,27)\), has operator

\[
\theta^2+27z^3(\theta+1)(\theta+2).
\]

Its normalized second solution satisfies \(L_n^2B_{\mathbf B}(n)\in\mathbb Z\)
for every \(n\), and the exponent two is optimal.  More generally, the dilation
family \((3h,h,3h^2)\) has this property exactly when \(3\mid h\).  This proves,
for the \(\mathbf B\) row, an integrality statement that had previously been
recorded only computationally in the fifteen-sporadic-pairs paper.

### 9.3 Congruences for second solutions

Once a companion has both a harmonic representation and an endpoint
representation, the two can be combined:

* use the harmonic form for character-resolved Lucas descent;
* use the endpoint form for integrality and valuation control;
* use the recurrence to propagate congruences through exceptional or
  zero-digit cases.

This may be particularly effective for second solutions of sporadic Apéry-like
recurrences, where explicit congruences are much less developed than for the
first solutions.

### 9.4 Automated search for new companions

The operator-locus calculation can be automated over parameterized recurrence
families.  Candidate loci can then be ranked by whether the resulting endpoint
products have recognizable factorial structure.  Harmonic lifting can be run
in the opposite direction to search for compact formulas for the same
solutions.

The most valuable outcome would be a new sequence for which:

1. direct harmonic Gosper searches fail;
2. endpoint conjugation reveals the correct arithmetic normal form;
3. inverse lifting reconstructs a previously unknown minimal harmonic formula;
4. the combined descriptions yield a new sharp denominator theorem or
   supercongruence.

## 10. Immediate next experiments

The following tests would turn the conjectural picture into a focused research
program.

1. Search cubic and quartic polynomial recurrences for binomial conjugations
   that decouple into two or three endpoint chains.
2. Repeat the calculation for known sporadic Apéry-like pairs whose second
   solutions do not yet have compact harmonic formulas.
3. For every successful transform, tabulate the exact valuations of the first
   several terms and guess the sharp parameter modulus.
4. Find a second natural realization with step \(q>3\), or a pure-power
   step-three realization complementing the mixed Zagier-\(\mathbf B\) case.
5. Compare the endpoint products with the harmonic words predicted by the
   connected-lift calculus.
6. Investigate whether endpoint positivity supplies new monotonicity or error
   estimates for ratios of first and second solutions.
7. Formalize the parameterized theorem before generalizing it, so the
   operator-conjugation and valuation components become reusable Lean lemmas.

## 11. Central takeaway

The general endpoint-denominator theorem reveals a three-layer structure:

\[
\text{harmonic lifting}
\quad\longleftrightarrow\quad
\text{recurrence conjugation}
\quad\longleftrightarrow\quad
\text{valuation theory}.
\]

The harmonic description constructs the companion, the conjugated recurrence
finds its natural basis, and the endpoint products make its integrality
visible.  The promising broader idea is that these are not separate tricks but
parts of one method for discovering and proving arithmetic properties of
Apéry-like second solutions.
