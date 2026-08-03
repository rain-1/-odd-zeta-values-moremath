# The Sharp Step-\(q\) Endpoint-Denominator Theorem

**Status:** proved.

**Scope:** a simultaneous generalization of the parity endpoint transform
(step \(2\)) and the squared endpoint quotient (weight \(2\)).

## 1. Statement

Fix integers \(q\geq2\), \(w\geq1\), and \(b\in\mathbb Z\).  Put

\[
L_n=\operatorname{lcm}(1,2,\ldots,n),\qquad L_0=1.
\]

For every prime \(p\mid q\), define

\[
\mu_p(q,w)
=\left\lceil
  \frac{w}{q}\left(v_p(q)+\frac1{p-1}\right)
 \right\rceil
=\left\lceil
  \frac{w\bigl((p-1)v_p(q)+1\bigr)}{q(p-1)}
 \right\rceil,
\tag{1}
\]

and define the **sharp endpoint modulus**

\[
M(q,w)=\prod_{p\mid q}p^{\mu_p(q,w)}.
\tag{2}
\]

Let \(T_m=0\) for \(m\leq0\), and for \(n\geq1\) define \(T_n\in\mathbb Q\) by

\[
n^wT_n
=b^q(n-q+1)^wT_{n-q}+(-b)^{n-1}.
\tag{3}
\]

As usual, the forcing at \(n=1\) is \((-b)^0=1\), including when \(b=0\).

Equivalently, if \(T(z)=\sum_{n\ge0}T_nz^n\) and
\(\theta=z\,d/dz\), then

\[
\bigl\{\theta^w-b^qz^q(\theta+1)^w\bigr\}T(z)
=\frac{z}{1+bz}.
\tag{3a}
\]

This is the step-\(q\) endpoint normal form produced by binomial conjugation.

For \(0\leq j<n\) with \(n-j\equiv1\pmod q\), put

\[
Q_q(n,j)=
\frac{\displaystyle\prod_{t=0}^{r-1}(j+2+tq)}
     {\displaystyle\prod_{t=0}^{r}(j+1+tq)},
\qquad
r=\frac{n-j-1}{q}.
\tag{4}
\]

Empty numerator products are \(1\).

### Theorem (sharp step-\(q\) endpoint denominator)

For every \(n\geq1\),

\[
T_n=b^{n-1}
\sum_{\substack{0\leq j<n\\n-j\equiv1\ (q)}}
(-1)^jQ_q(n,j)^w.
\tag{5}
\]

Moreover, the following conditions are equivalent:

1. \(M(q,w)\mid b\);
2. for every admissible \((n,j)\),
   \[
   L_n^w b^{n-1}Q_q(n,j)^w\in\mathbb Z;
   \tag{6}
   \]
3. for every \(n\geq0\),
   \[
   L_n^wT_n\in\mathbb Z.
   \tag{7}
   \]

Thus (2) is not just a convenient sufficient modulus: it is the exact uniform
denominator threshold for the endpoint sequence.

## 2. Iterating the endpoint recurrence

The forcing at the index \(j+1\) contributes

\[
\frac{(-b)^j}{(j+1)^w}.
\]

If \(n=j+1+rq\), propagation from \(j+1\) to \(n\) multiplies this by

\[
\prod_{t=0}^{r-1}
\frac{b^q(j+2+tq)^w}{(j+1+(t+1)q)^w}.
\]

The total power of \(b\) is \(j+rq=n-1\), and the remaining quotient is
exactly \(Q_q(n,j)^w\).  Summing the contributions proves (5).

## 3. The denominator lemma

The key estimate explains separately what happens at primes outside and inside
the step size.

### Lemma

Let \((n,j)\) be admissible and put \(r=(n-j-1)/q\).

1. If \(p\nmid q\), then
   \[
   v_p(Q_q(n,j))\geq-v_p(L_n).
   \tag{8}
   \]
2. If \(p\mid q\) and \(s=v_p(q)\), then
   \[
   v_p(Q_q(n,j))
   \geq-v_p(L_n)-rs-v_p(r!).
   \tag{9}
   \]

### Proof

Suppose first that \(p\nmid q\).  For a fixed \(p^a\), the denominator of
\(Q_q(n,j)\) contains \(r+1\) terms in one invertible residue progression,
while the numerator contains \(r\) terms in another.  Among any \(r+1\)
consecutive indices, a fixed residue class modulo \(p^a\) occurs at most
\(\lceil(r+1)/p^a\rceil\) times.  Among \(r\) consecutive indices, a fixed
residue class occurs at least \(\lfloor r/p^a\rfloor\) times.  Hence

\[
\#\{p^a\mid\text{denominator factors}\}
-\#\{p^a\mid\text{numerator factors}\}\leq1.
\]

Only powers \(p^a\leq n\) can occur.  Summing over \(a\) proves (8).

Now suppose \(p\mid q\).  Write the denominator factors as

\[
d_t=j+1+tq,\qquad 0\leq t\leq r.
\]

Choose \(t_*\) so that \(v_p(d_{t_*})\) is maximal.  Because
\(d_{t_*}\leq n\),

\[
v_p(d_{t_*})\leq v_p(L_n).
\]

For \(t\ne t_*\), maximality and
\(d_t-d_{t_*}=q(t-t_*)\) give

\[
v_p(d_t)\leq s+v_p(|t-t_*|).
\]

Therefore

\[
\begin{aligned}
v_p\!\left(\prod_{t=0}^r d_t\right)
&\leq v_p(L_n)+rs
  +v_p\bigl(t_*!\,(r-t_*)!\bigr)\\
&\leq v_p(L_n)+rs+v_p(r!),
\end{aligned}
\]

where the last inequality follows because
\(r!/[t_*!\,(r-t_*)!]\) is an integer.  Ignoring the numerator only weakens
the estimate, and proves (9). \(\square\)

## 4. Sufficiency of the sharp modulus

Assume \(M(q,w)\mid b\).  Fix a prime \(p\).

If \(p\nmid q\), (8) immediately gives

\[
v_p\bigl(L_n^wQ_q(n,j)^w\bigr)\geq0.
\]

If \(p\mid q\), write \(s=v_p(q)\) and \(e=v_p(b)\).  By (1),

\[
eq\geq w\left(s+\frac1{p-1}\right).
\tag{10}
\]

Also

\[
n-1=j+rq\geq rq,
\qquad
v_p(r!)\leq\frac{r}{p-1}.
\]

It follows that

\[
e(n-1)\geq erq
\geq wr\left(s+\frac1{p-1}\right)
\geq w\bigl(rs+v_p(r!)\bigr).
\tag{11}
\]

Combining (9) and (11) proves (6).  Formula (5) then proves (7).

## 5. Necessity and the unique lowest-valuation term

Assume \(b\ne0\), and suppose that some prime \(p\mid q\) has

\[
e=v_p(b)<\mu_p(q,w).
\]

Put \(s=v_p(q)\) and examine \(n=qR\).  Its admissible source indices are

\[
j=q\ell-1,\qquad 1\leq\ell\leq R.
\]

For such an index, every numerator factor of \(Q_q(qR,q\ell-1)\) is
congruent to \(1\pmod p\), while its denominator is

\[
q^{R-\ell+1}\frac{R!}{(\ell-1)!}.
\]

Consequently the \(p\)-adic valuation of this contribution to (5) is

\[
e(qR-1)
-w\left((R-\ell+1)s
        +v_p\!\left(\frac{R!}{(\ell-1)!}\right)\right).
\tag{12}
\]

The \(\ell=1\) term is the unique term of least valuation: subtracting its
valuation from (12) gives

\[
w\bigl((\ell-1)s+v_p((\ell-1)!)\bigr)>0
\qquad(\ell>1).
\]

There can therefore be no cancellation of the lowest-valuation term, and

\[
v_p(T_{qR})
=e(qR-1)-w\bigl(Rs+v_p(R!)\bigr).
\tag{13}
\]

After multiplication by \(L_{qR}^w\), divide the right-hand side by \(R\)
and let \(R\to\infty\).  Since

\[
\frac{v_p(R!)}R\longrightarrow\frac1{p-1},
\qquad
\frac{v_p(L_{qR})}R\longrightarrow0,
\]

the limiting normalized valuation is

\[
eq-w\left(s+\frac1{p-1}\right).
\]

Because \(e<\lceil w(s+1/(p-1))/q\rceil\), this number is strictly negative.
Thus \(L_{qR}^wT_{qR}\) fails to be integral for all sufficiently large
members of some tail.  This proves that (7) forces every divisibility condition
in (2).

The case \(b=0\) is harmless: \(M(q,w)\mid0\), and (3) gives \(T_1=1\) and
\(T_n=0\) for \(n\ne1\).

We have proved the equivalence of (1)--(3) in the theorem.

## 6. Binomial transport back to companion sequences

Define

\[
B_n=\sum_{k=0}^n\binom nk b^{n-k}T_k.
\tag{14}
\]

Binomial inversion gives

\[
T_n=\sum_{k=0}^n\binom nk(-b)^{n-k}B_k.
\tag{15}
\]

Since \(L_k\mid L_n\) for \(k\leq n\), (14) and (15) imply

\[
\left(\forall n,\ L_n^wB_n\in\mathbb Z\right)
\quad\Longleftrightarrow\quad
\left(\forall n,\ L_n^wT_n\in\mathbb Z\right).
\]

Hence the same exact classification holds in the original binomial basis:

\[
\boxed{
\forall n,\ L_n^wB_n\in\mathbb Z
\quad\Longleftrightarrow\quad
M(q,w)\mid b.}
\tag{16}
\]

At the generating-function level the two bases are related by

\[
B(z)=\frac1{1-bz}T\!\left(\frac{z}{1-bz}\right),
\qquad
T(z)=\frac1{1+bz}B\!\left(\frac{z}{1+bz}\right).
\]

For \((q,w)=(2,2)\), formula (1) gives \(M(2,2)=4\), recovering the general
Catalan endpoint-denominator theorem.

## 7. Unexpected special cases

If \(q=\ell\) is prime, then

\[
\mu_\ell(\ell,w)=\left\lceil\frac{w}{\ell-1}\right\rceil,
\qquad
M(\ell,w)=\ell^{\lceil w/(\ell-1)\rceil}.
\tag{17}
\]

Thus the naive sufficient guess \(q^w\mid b\) is usually far from sharp.  For
example,

\[
M(3,2)=3,\qquad M(5,4)=5,
\]

not \(9\) and \(625\), respectively.  The parity case is exceptional because
\(p-1=1\):

\[
M(2,w)=2^w.
\]

Some initial rows \(M(q,1),\ldots,M(q,8)\) are

| \(q\) | sharp moduli for \(w=1,\ldots,8\) |
|---:|:---|
| 2 | \(2,4,8,16,32,64,128,256\) |
| 3 | \(3,3,9,9,27,27,81,81\) |
| 4 | \(2,4,8,8,16,32,64,64\) |
| 5 | \(5,5,5,5,25,25,25,25\) |
| 6 | \(6,6,6,12,36,36,72,72\) |

The formula captures a balance between three quantities:

* the endpoint weight \(w\);
* the built-in divisibility \(v_p(q)\) of every step;
* the average factorial contribution \(1/(p-1)\).

This is precisely the valuation structure that was invisible in the original
three-term recurrence.

## 8. Reproducibility

The independent exact audit is
`work/harmonic_jets/verify_step_q_endpoint.py`.  It checks:

* the modulus table above;
* recurrence (3) against finite formula (5) through \(n=80\) for
  \(2\leq q\leq10\), \(1\leq w\leq6\), and positive and negative parameters;
* every termwise integrality assertion for \(q\leq12\), \(w\leq8\),
  \(n<180\);
* deficient-prime sharpness witnesses for \(q\leq14\), \(w\leq9\).

Run it from the repository root with

```bash
python3 work/harmonic_jets/verify_step_q_endpoint.py
```

## 9. Interpretation

The theorem confirms and sharpens the methodology suggested by the parity
case.  A step-\(q\) endpoint chain does concentrate the residual denominator on
the primes dividing \(q\), but the exponent is not simply the harmonic weight.
It is the optimal density

\[
\frac{w}{q}\left(v_p(q)+\frac1{p-1}\right)
\]

rounded upward.  The first term is the fixed \(p\)-divisibility of the step;
the second is the asymptotic valuation density of a factorial.  The unique
lowest-valuation endpoint at \(n=qR\) shows that this density bound cannot be
improved by cancellation.
