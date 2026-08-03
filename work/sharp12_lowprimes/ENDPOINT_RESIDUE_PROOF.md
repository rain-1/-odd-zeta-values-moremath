# Proof of the binary and ternary endpoint-residue lemma

This note proves the finite-state lemma isolated in
`ENDPOINT_BREAKTHROUGH.md`.  It is a statement about the compact summand; it
does not by itself prove the still-open global identity expressing `P_n` as
the sum of that compact summand.

## 1. Two elementary digit identities

Let `p` be prime.  For `r >= 1` one has the exact split

\[
H_{pm+d}^{(r)}=p^{-r}H_m^{(r)}+
 \sum_{a=0}^{m-1}\sum_{s=1}^{p-1}(pa+s)^{-r}
 +\sum_{s=1}^{d}(pm+s)^{-r},\qquad0\le d<p.
\tag{1}
\]

In particular, if `M=p^(L+1)` and `0 <= x < 2M`, then

\[
 M^rH_x^{(r)}\equiv [x\ge M]\pmod {p^r\mathbb Z_p}.
\tag{2}
\]

For factorial units put

\[
u_p(a!)=p^{-v_p(a!)}a!\in\mathbb Z_p^\times.
\]

Splitting a factorial into blocks of length `p` gives

\[
u_p((pm+d)!)\equiv(-1)^m u_p(m!)d!\pmod p
\tag{3}
\]

for odd `p`.  For `p=2`, splitting into even and odd factors gives

\[
u_2((2m+d)!)\equiv
u_2(m!)\prod_{j=1}^{m+d}(2j-1)\pmod4.
\tag{4}
\]

Equations (1), (3), and (4) are identities or finite product congruences; no
limit or experimental assertion is involved.

## 2. The harmonic principal part

Write `N=p^L`, `M=pN`, and

\[
e_k=[n+k\ge M],\qquad e_l=[n+l\ge M].
\]

Only `H_(n+k)` and `H_(n+l)` among the arguments in the compact weight can
cross `M`.  If

\[
\begin{aligned}
\alpha&=(H_{n+k}-H_k)-(H_{n+l}-H_l),\\
\beta&=(H_{n-k}-H_k)-(H_{n-l}-H_l),\\
C&=A_2(k)+A_2(l)-\alpha^2-2\alpha\beta,
\end{aligned}
\]

then (2) gives

\[
M\alpha\equiv e_k-e_l,qquad M\beta\equiv0,qquad
M^2C\equiv e_k+e_l-(e_k-e_l)^2\pmod p.
\tag{5}
\]

The weight is

\[
w_5=H_{n+k}^{(5)}+\frac{\alpha-\beta}{2}H_{n+k}^{(4)}
       +\frac C4H_{n+k}^{(3)}.
\tag{6}
\]

At `p=2`, the last quantity in (5) is even for every pair
`(e_k,e_l)`.  Consequently

\[
v_2(w_5)\ge-5L-6.
\tag{7}
\]

At `p=3`, when `e_k=1`, the coefficient of `M^(-5)` in (6) is

\[
1+\frac{1-e_l}{2}
 +\frac{1+e_l-(1-e_l)^2}{4}\equiv0\pmod3.
\]

When `e_k=0`, the same bound follows one order more easily because the three
outer harmonic numbers do not cross `M`.  Thus

\[
v_3(w_5)\ge-5L-4.
\tag{8}
\]

The important point is that the gain in (8) is internal to the connected
combination (6); none of its three displayed terms has that gain separately.

## 3. The two-carry automata

Kummer's theorem applied to the five factors of

\[
T=\binom{n+k}{n}\binom nk^2
  \binom{n+l}{n}\binom nl^2\binom{n+k+l}{n}
\tag{9}
\]

shows that a cell which reaches the new endpoint has `v_p(T)>=2`.  If the
valuation is minimal, the two squared binomials are units and the complete
carry state has the following transition table.  Here a triple is the digit
`(n_i,k_i,l_i)`.

\[
\begin{array}{c|c|c}
p&\text{leading digit(s)}&\text{allowed lower digits}\\ \hline
2&(1,1,0),(1,1,1)&(0,0,0),(1,0,0)\\[2pt]
3&(2,1,0),(2,1,2),(2,2,0),(2,2,1)&
 (0,0,0),(1,0,0),(1,0,1),(1,1,0),(2,0,0).
\end{array}
\tag{10}
\]

For clarity, the lower row means: if `n_i=0` or `2`, then
`(k_i,l_i)=(0,0)`; if `n_i=1`, then

\[
(k_i,l_i)\in\{(0,0),(0,1),(1,0)\}.
\tag{11}
\]

This table is a finite proof, not an induction hypothesis.  To obtain it,
first impose that `binom(n,k)` and `binom(n,l)` have no carries (their
valuations occur twice), then enumerate the incoming and outgoing carry bits
in the remaining three additions.  For `p=2` the next possible shell
valuation after `2` is `4`; a valuation `3` is excluded by the same table.
For `p=3`, valuation `3` may occur but is already sufficient with (8).

It follows immediately from (10) that the binary minimal cells are

\[
(k,l)=(N,0),(N,N).
\tag{12}
\]

For `p=3` minimal-shell cells exist only if the leading digit of `n` is `2`.
Writing `n=2N+r`, their number before the final harmonic test is

\[
4\cdot3^{e_1(r)},qquad
e_1(r)=\#\{\text{digits of }r\text{ equal to }1\}.
\tag{13}
\]

## 4. Unit transitions

Substitute (1), (3), and (4) into (6) and (9), remove the valuations in
(7)--(8), and reduce the remaining units.  All dependence on higher digits
cancels.  The complete transition table is

\[
\begin{array}{c|c|c}
p&\text{tail digit}&\text{multiplier of the normalised cell}\\ \hline
2&(0,0,0),(1,0,0)&1\pmod4\\
3&(0,0,0),(1,0,0),(1,0,1),(1,1,0),(2,0,0)&1\pmod3.
\end{array}
\tag{14}
\]

For reproducibility, one line of the calculation is illustrative.  In the
ternary case (3) replaces every factorial unit at the next digit by
`(-1)^m u_3(m!)d!`; the signs occur twice in each squared binomial and the
remaining three signs cancel against the sign from the connected harmonic
coefficient in (6).  The three possibilities in (11) leave respectively the
unit products `1,1,1`.  The binary calculation uses (4); the odd products from
the five binomials cancel in pairs, leaving multiplier `1 mod 4` for both
possible digits of `n`.

At the leading digit, direct substitution gives

\[
\begin{array}{c|c|c}
p&(k_L,l_L)&\text{normalised value}\\ \hline
2&(1,0)&-1\pmod4\\
2&(1,1)& 1\pmod4\\ \hline
3&(1,0),(1,2),(2,0)&-1\pmod3\\
3&(2,1)&0\pmod3.
\end{array}
\tag{15}
\]

In the last line `0` means that the weight gains one additional ternary
order.  Combining (14) and (15), the ternary deficient stratum therefore has

\[
\#E_n=3\cdot3^{e_1(r)}=3^{1+e_1(r)},
\tag{16}
\]

and every member has residue `-1 mod 3`.

## 5. Conclusion

All cells outside (12) satisfy

\[
v_2(Tw_5)\ge-5L-2.
\]

The two cells in (12) have valuation `-5L-4` and, by (15), opposite residues
modulo `4`; their sum has valuation at least `-5L-2`.  Hence

\[
2^{2+5L}\sum_{k,l}T(n,k,l)w_5(n,k,l)\in\mathbb Z_2.
\tag{17}
\]

At `p=3`, all cells outside `E_n` satisfy

\[
v_3(Tw_5)\ge-5L-1.
\]

Every member of `E_n` has valuation `-5L-2`, common residue `-1`, and the
cardinality (16), which is divisible by `3`.  Therefore

\[
3^{1+5L}\sum_{k,l}T(n,k,l)w_5(n,k,l)\in\mathbb Z_3.
\tag{18}
\]

This proves the Endpoint Residue Lemma for every `n`.
