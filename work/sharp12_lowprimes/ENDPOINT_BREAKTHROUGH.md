# The low-prime endpoint mechanism behind sharp 12

**Status (3 August 2026).**  The Endpoint Residue Lemma and its implication
to the low-prime sharp denominator bound are now proved; the digit proof is in
`ENDPOINT_RESIDUE_PROOF.md` and has also been checked in exact arithmetic at
every cell through `n = 80`.  The compact double-sum identity used in Part I
remains verified rather than certified.  Part II records the unconditional
Zudilin partial-fraction route.

## 1. Setup

Put

\[
 T(n,k,l)=\binom{n+k}{n}\binom nk^2
          \binom{n+l}{n}\binom nl^2\binom{n+k+l}{n}
\]

and define

\[
\begin{aligned}
 A_r(x)&=H_{n+x}^{(r)}-H_x^{(r)},
 &B_r(x)&=H_{n-x}^{(r)}-H_x^{(r)},\\
 \alpha&=A_1(k)-A_1(l),
 &\beta&=B_1(k)-B_1(l).
\end{aligned}
\]

The compact weight-five summand is

\[
 w_5(n,k,l)=H_{n+k}^{(5)}
 +\frac{\alpha-\beta}{2}H_{n+k}^{(4)}
 +\frac{A_2(k)+A_2(l)-\alpha^2-2\alpha\beta}{4}H_{n+k}^{(3)}.
\tag{1}
\]

Exact computation gives

\[
 P_n=\sum_{k,l=0}^nT(n,k,l)w_5(n,k,l),
\tag{2}
\]

but (2) is not yet a certified identity.  The point of this note is that (1)
exposes the primes 2 and 3 in an unexpectedly small endpoint quotient.

For a prime `p`, write `L=floor(log_p n)` and `N=p^L`.

## 2. Endpoint Residue Lemma

### Binary part

For every `n >= 1` and every `0 <= k,l <= n`,

\[
 v_2(Tw_5)\ge -5L-4.
\]

All cells other than `(k,l)=(N,0),(N,N)` satisfy the stronger bound

\[
 v_2(Tw_5)\ge -5L-2.
\tag{B1}
\]

At the two exceptional endpoints,

\[
\begin{aligned}
2^{5L+4}T(n,N,0)w_5(n,N,0)&\equiv-1\pmod4,\\
2^{5L+4}T(n,N,N)w_5(n,N,N)&\equiv 1\pmod4.
\end{aligned}
\tag{B2}
\]

Thus the two apparent denominator defects cancel by two full powers of 2.

### Ternary part

For every cell,

\[
 v_3(Tw_5)\ge-5L-2.
\]

Every non-deficient cell satisfies

\[
 v_3(Tw_5)\ge-5L-1.
\tag{T1}
\]

There are no deficient cells if the leading ternary digit of `n` is 1.  If

\[
n=2N+r,\qquad 0\le r<N,
\]

then the number of deficient cells is

\[
 \#E_n=3^{1+e_1(r)},
 \qquad
 e_1(r)=\#\{\text{ternary digits of }r\text{ equal to }1\}.
\tag{T2}
\]

Every one of them has the same principal residue

\[
 3^{5L+2}T(n,k,l)w_5(n,k,l)\equiv-1\pmod3.
\tag{T3}
\]

Since `#E_n` is a multiple of 3, the deficient stratum cancels.

### Finite-state proof

The proof uses only the digit split

\[
 H_x^{(m)}=\sum_{\substack{j\le x\\p\nmid j}}j^{-m}
             +p^{-m}H_{\lfloor x/p\rfloor}^{(m)}
\tag{3}
\]

and Kummer's carry formula for every binomial in `T`.  After (3), every
non-integral principal part is determined by the leading digits of `n,k,l`.
At `p=2` the transition has two terminal states, giving (B2).  At `p=3`
the tail-digit transitions have multiplicities

\[
 d=0:1,\qquad d=1:3,\qquad d=2:1.
\]

Starting with three leading states gives

\[
3\prod_{d\text{ a digit of }r}(1,3,1)_d=3^{1+e_1(r)},
\]

and direct substitution of the three leading states in (1) gives the common
residue `-1`.  The full Kummer/harmonic-digit proof, including the binary and
ternary transition tables, is `ENDPOINT_RESIDUE_PROOF.md`.

## 3. Consequence for the compact sum

Assume (2) and the Endpoint Residue Lemma.  By (B1),
`2^(5L+2) T w_5` is 2-integral away from the two endpoints.  By (B2), the
sum of the two endpoint contributions is also 2-integral.  Hence

\[
 v_2(P_n)\ge-2-5\lfloor\log_2n\rfloor.
\tag{4}
\]

Similarly, (T1) makes `3^(5L+1) T w_5` integral off `E_n`, while
(T2)--(T3) make the sum over `E_n` integral.  Therefore

\[
 v_3(P_n)\ge-1-5\lfloor\log_3n\rfloor.
\tag{5}
\]

Equations (4)--(5) are exactly the low-prime factor
`12 = 2^2 * 3` in the sharp denominator theorem.

This also explains why 3 has no geometric origin in the earlier bicomplex
analysis: it is the cardinality of a ternary endpoint fibre.

## 4. Stronger observed congruences

The recurrence gives, much more strongly,

\[
 2^{2+5L}P_n\equiv-Q_n\pmod4,
 \qquad
 3^{1+5L}P_n\equiv-Q_n\pmod3.
\tag{6}
\]

Because `Q_n` has Lucas digits `(1,0,1)` modulo 3, equality holds in (5)
exactly when every ternary digit of `n` is 0 or 2.  Exact tests also suggest

\[
v_3\!\left(3^{1+5L}P_n\right)
 \ge \#\{\text{ternary digits of }n\text{ equal to }1\}.
\tag{7}
\]

Equations (6)--(7) are not consequences of the residue lemma as presently
stated and remain conjectural.

## 5. Unconditional one-variable route

Zudilin's proved rational functions satisfy

\[
 \widetilde R_n(k)=-k(k+n)R_n(k).
\]

If

\[
 R_n(k)=\sum_{j=0}^n\sum_{s=1}^6\frac{A_{s,j}}{(k+j)^s},
\]

then

\[
 \widetilde A_{s,j}=j(n-j)A_{s,j}+(2j-n)A_{s+1,j}-A_{s+2,j}.
\]

Writing `w` and `wt` for the two zeta(3) coefficients and

\[
C_{s,j}=\widetilde w A_{s,j}-w\widetilde A_{s,j},
\]

one obtains the proved one-dimensional formula

\[
q_n=\sum_jC_{5,j},\qquad
p_n=\sum_{j=0}^n\sum_{s=1}^6 C_{s,j}H_j^{(s)},\qquad
P_n=\frac{(-1)^{n+1}p_n}{\binom{2n}{n}}.
\tag{8}
\]

The purified rational function is odd under `k -> -n-k`, so

\[
C_{s,n-j}=(-1)^{s+1}C_{s,j}.
\tag{9}
\]

It is `O(k^(-4n-3))`; therefore, for `1 <= r < 4n+3`,

\[
\sum_{s\le\min(6,r)}\sum_j
(-1)^{r-s}\binom{r-1}{r-s}j^{r-s}C_{s,j}=0.
\tag{10}
\]

Equations (8)--(10) are unconditional and give the correct target for removing
the remaining dependence on (2): prove the endpoint residue lemma after
quotienting the partial-fraction cells by the zero moments (10).

## 6. Exact audits

Run

```text
python3 work/sharp12_lowprimes/verify_compact_endpoint_residues.py
python3 work/sharp12_lowprimes/verify_zudilin_endpoint.py
```

The first checks every compact cell through `n = 80`.  The second reconstructs
Zudilin's partial fractions and checks reflection, purity, every forced moment,
and the strong low-prime congruence through `n = 20`.

## 7. Exact remaining bridge and failed shortcuts

Let `B_5` be the fifth Bell coefficient of the explicit gamma deformation in
`Z5CF_EPSILON.md` and put

\[
 \Delta_5=B_5-\frac{33}{4}w_5^{\rm sym}.
\]

The bridge (2) reduces to `sum T Delta_5=0`.  A saturated two-prime
calculation shows that `sym(Delta_5)` lies in the full per-fixed-variable
residue kernel.  The constructive residue alphabet presently has rank `419`;
adjoining every admissible elementary-symmetric pole cancellation on the two
simple-zero ranges, the double-zero middle range, and the full numerator
multiset raises the rank but leaves the target one dimension outside.  The
full anti-diagonal Laurent family from `R_n(x,m-x)=0`, enlarged by all natural
affine endpoint weights, also leaves the same residual quotient.

These negatives are useful: the missing certificate is not another ordinary
power-sum, elementary-symmetric, or first anti-diagonal jet.  It must use a
genuinely weighted/nested endpoint jet, or else a recurrence-level creative
telescoping certificate.  Thus the current theorem boundary is exact:

* the endpoint-residue theorem is proved for all `n`;
* its compact-to-recurrence bridge is a single explicit all-`n` identity;
* none of the finite checks is being used as a proof of that identity.
