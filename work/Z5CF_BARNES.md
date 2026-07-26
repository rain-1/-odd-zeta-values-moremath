# Z5CF_BARNES — Barnes/residue route to the compact companion sums

**Agent:** Sol (Codex), 2026-07-26  
**Status:** in progress; statements are labelled individually.

## 0. Target

Prove, for every `n >= 0`, that the compact double sums for the Brown--Zudilin
middle and top companion rows equal the recurrence-defined sequences `Phat` and
`PBZ`.  This file does not treat finite verification as proof.

## 1. Totally symmetric Barnes kernel

In the totally symmetric specialization

```text
p_0=p_1=p_2=p_4=p_5=p_6=q_1=...=q_5=n,  p_3=2n,
```

Brown--Zudilin's equation `(intJ)` becomes

```text
J_n = n!/(2 pi i)^2 integral integral
        Gamma(n+1+s)^3 Gamma(-s) / Gamma(2n+2+s)^2
        Gamma(n+1+t)^3 Gamma(-t) / Gamma(2n+2+t)^2
        Gamma(2n+2+s+t) Gamma(-n-1-s-t) ds dt.
```

Using `Gamma(z)Gamma(1-z)=pi/sin(pi z)` gives

```text
J_n = (-1)^n n!/(2 pi i)^2 integral integral
        R_n(s,t)
        pi/sin(pi s) pi/sin(pi t) pi/sin(pi(s+t)) ds dt,

R_n(s,t) =
  prod_{j=1}^n(s+j) prod_{j=1}^n(t+j)
  prod_{j=n+2}^{2n+1}(s+t+j)
  /
  [prod_{j=n+1}^{2n+1}(s+j)^2
   prod_{j=n+1}^{2n+1}(t+j)^2].
```

This is an exact gamma-algebra calculation.

## 2. Local partial fractions `[PROVED — direct product calculation]`

The only poles of `R_n` are the grid

```text
s = -n-1-k,  t = -n-1-l,  0 <= k,l <= n,
```

with order at most two in each variable.  Write the local principal part as

```text
C22/(s+n+1+k)^2(t+n+1+l)^2
+ C12/(s+n+1+k)  (t+n+1+l)^2
+ C21/(s+n+1+k)^2(t+n+1+l)
+ C11/(s+n+1+k)  (t+n+1+l).
```

Put

```text
A_r(x)=H_{n+x}^{(r)}-H_x^{(r)},
B_r(x)=H_{n-x}^{(r)}-H_x^{(r)},
C_r   =H_{n+k+l}^{(r)}-H_{k+l}^{(r)},
L_k   =-A_1(k)-C_1-2B_1(k),
L_l   =-A_1(l)-C_1-2B_1(l).
```

Then

```text
(-1)^n n! C22 = T(n,k,l),
C12/C22 = L_k,
C21/C22 = L_l,
C11/C22 = L_k L_l - C_2.
```

Proof: evaluate the three products remaining after deleting the two vanishing
denominator factors:

```text
prod_{j=1}^n(-n-1-k+j) = (-1)^n (n+k)!/k!,
prod_{r=0,r!=k}^n(r-k) = (-1)^k k!(n-k)!,
prod_{j=n+2}^{2n+1}(-2n-2-k-l+j)
    = (-1)^n (n+k+l)!/(k+l)!.
```

Their quotient is `(-1)^n T/n!`.  Logarithmic differentiation gives
`L_k,L_l`; the mixed logarithmic derivative of the diagonal product is
`-C_2`.

## 3. Universal sine kernel `[DERIVED, exact implementation]`

`work/z5barnes/universal.py` evaluates Brown--Zudilin's four universal
integrals `I_{a,b}^{(p,q)}`, `p,q in {1,2}`, exactly in

```text
1, zeta(2), zeta(3), zeta(4), zeta(5), zeta(2)zeta(3).
```

It uses their displayed piecewise function `f(u,v)`, geometric-series
integration on the two triangles, partial fractions for
`sum_t 1/(t^r(t+h)^m)`, and the standard weight-at-most-five double-zeta
reductions.  The Laplace identity contributes `(-1)^(p+q-2)` because it
contains `(-log u)^(p-1)(-log v)^(q-1)`.  This sign is invisible in `(2,2)`
but reverses `(1,2)` and `(2,1)`; direct contour quadrature confirms it.
Calibration at `(a,b)=(0,0)` gives exactly

```text
I00^(2,2) = 2 zeta(5) + 4 zeta(2)zeta(3),
```

which is `J_0`.

## 4. Contours `[RESOLVED]`

Choose `c_1=c_2=n+2/3` in `(intJ)`.  This satisfies `0<c_i<n+1` and
`c_1+c_2>n+1`.  After translating `x=s+n+1`, `y=t+n+1`, both contours
already have real part `1/3`.  No contour shift and no crossed residue is
required.

The initially observed `n=1` discrepancy came instead from omitting the
Laplace sign in §3.  It is not a contour obstruction.

## 5. Published middle-row reduction `[PROVED specialization]`

Brown--Zudilin `(I3)` specializes, with `k=n+l`, to

```text
I''_n =
  sum_{l=0}^n (-1)^l C(n+l,n) C(n,l)^2
  J_3(n,n,n,n-l; n,n,n+l).
```

The condition for the generalized Beukers integral is
`(n-l)+(n+l)=n+n`.  Its zeta(3) coefficient is

```text
(-1)^l sum_{k=0}^n
  C(n+k,n) C(n+k+l,n) C(n,k)^2.
```

The outer sign cancels it, and multiplication by the outer binomial factor
gives exactly `T(n,k,l)`.  Hence the zeta(3) coefficient of `I''_n` is
`Q_n=sum T`, with no finite-range assumption.

What remains for this route is the rational coefficient of the shifted
`J_3`; equivalently, the correct rational function carrying the diagonal
coupling.  This is the precise middle-row proof obligation.

## 6. Exact coefficient comparison `[VERIFIED range, not yet the proof]`

Combining §§2–4, define the contour-native local expression

```text
W_B(n,k,l) =
    I_{k,l}^{(2,2)}
  + L_k I_{k,l}^{(1,2)}
  + L_l I_{k,l}^{(2,1)}
  + (L_k L_l-C_2) I_{k,l}^{(1,1)}.
```

After the double-zeta reductions

```text
zeta(2,1)=zeta(3),
zeta(3,1)=zeta(4)/4,
zeta(2,2)=3zeta(4)/4,
zeta(4,1)=2zeta(5)-zeta(2)zeta(3),
zeta(3,2)=3zeta(2)zeta(3)-11zeta(5)/2,
zeta(2,3)=9zeta(5)/2-2zeta(2)zeta(3),
```

exact symbolic evaluation gives

```text
sum_{k,l=0}^n T(n,k,l) W_B(n,k,l)
 =
  2 Q_n zeta(5) + 4 Q_n zeta(2)zeta(3)
  -4 [sum T w3sym] zeta(2) - 2 [sum T w5sym]
```

for every `n=0,...,12`, with all six coefficients compared independently in
exact rational arithmetic and zero discrepancies.  The unwanted
`zeta(3),zeta(4)` coefficients also sum to zero.

The agreement is not cellwise.  An exact attempt to project
`-coeff_zeta(2)(W_B)/4` to the 90 top monomials of the degree-at-most-two bare
weight-3 alphabet is inconsistent (204 exact-Q cells).  Thus the local Barnes
representative contains deeper finite-harmonic structure, even though its
weighted sum equals the compact representative.  This is consistent with
Brown--Zudilin's warning that the direct Barnes arithmetic for `I''` is harder
than their `(I3)` descent.

## 7. The first uniform kernel identity `[PROVED]`

The universal coefficients needed for the unwanted `zeta(4)` term are

```text
[zeta(4)] I^(1,2)_{k,l} = [zeta(4)] I^(2,1)_{k,l} = 17/4,
[zeta(4)] I^(1,1)_{k,l} = [zeta(4)] I^(2,2)_{k,l} = 0.
```

Hence its coefficient in `sum T W_B` is

```text
(17/4) sum_{k,l} T(n,k,l)(L_k+L_l).
```

This is zero for every `n`, not merely on the checked range.  Fix `l` and put

```text
g_l(x) = lim_{y -> -l} (y+l)^2 R_n(x-n-1,y-n-1).
```

Its partial fractions in `x` are

```text
g_l(x) = sum_{k=0}^n [
  C22(k,l)/(x+k)^2 + C12(k,l)/(x+k)].
```

Since `g_l(x)=O(x^-2)` at infinity, the sum of its finite residues is zero:
`sum_k C12(k,l)=0`.  Section 2 gives
`C12(k,l)=(-1)^n T(n,k,l)L_k/n!`, so
`sum_k T(n,k,l)L_k=0` for every fixed `l`.  The mirror argument gives the
`L_l` identity.  Therefore the unwanted `zeta(4)` coefficient vanishes
identically.

The other universal high coefficients simplify uniformly to

```text
[zeta(3)] I11 = 2,
[zeta(3)] I12 = 2(H_k-H_{k+l}),
[zeta(3)] I21 = 2(H_l-H_{k+l}),
[zeta(3)] I22 = 2(H_k^(2)+H_l^(2)-2H_{k+l}^(2)),

[zeta(2)] I11 = H_k+H_l-2H_{k+l},
[zeta(2)] I12 = H_l^(2)-2H_{k+l}^(2),
[zeta(2)] I21 = H_k^(2)-2H_{k+l}^(2).
```

These follow directly from the finite formulas in `universal.py` (and were
also reconstructed independently from exact values).  They reduce the next
three obligations to explicit rational finite-sum identities.

## 8. Uniform evaluation lemma for the universal integrals `[DERIVED]`

This section records the formula implemented by `universal.py`, so the
calculation is independently checkable without treating the program as an
oracle.

For integers `N>=1`, define the regularised zeta tail

```text
Z_1(N) = -H_{N-1},
Z_m(N) = zeta(m)-H_{N-1}^{(m)}  (m>=2).
```

For `r,m,h>=1`, put

```text
U_{r,m}(h) = sum_{t>=1} 1/[t^r(t+h)^m].
```

Its partial fractions are

```text
1/[t^r(t+h)^m]
 = sum_{i=1}^r
     (-1)^(r-i) C(m+r-i-1,r-i) / [h^(m+r-i)t^i]
 + sum_{j=1}^m
     (-1)^r C(r+m-j-1,m-j) / [h^(r+m-j)(t+h)^j].
```

The two simple-pole coefficients sum to zero, so summing this display gives
`U_{r,m}(h)` in ordinary zeta values and finite harmonic numbers, with no
regularisation ambiguity.

For `A,d>=1`, define the coupled tail

```text
S_{r,m}(A,d) = sum_{t>=A} t^(-r) Z_m(t+d).
```

If `m>=2`, then

```text
S_{r,m}(A,d)
 = zeta(m,r)
   - sum_{h=1}^{d-1} U_{r,m}(h)
   - sum_{t=1}^{A-1} t^(-r) Z_m(t+d).
```

For `m=1` (only `r=2,3` occur here),

```text
S_{r,1}(A,d)
 = -E_r - sum_{h=1}^{d-1}U_{r,1}(h)
   + sum_{t=1}^{A-1} H_{t+d-1}/t^r,

E_2=2zeta(3),  E_3=5zeta(4)/4.
```

Now let `A=a+1`, `d=b+1`.  On the triangle `0<u<v<1`, substitute `u=xv`
in Brown--Zudilin's displayed `f(u,v)`.  Geometric expansion of its two
denominators and termwise beta integration gives

```text
F_{a,b}^{p,q}
 =
 (-1)^(p+q-1) sum_{i=0}^p
   C(p,i)i!(p-i+q-1)! S_{i+1,p-i+q}(A,d)

 +(-1)^(p+q) sum_{i=0}^{p-1}
   C(p-1,i)(i+1)!(p+q-2-i)!
   Z_{i+2}(A) Z_{p+q-1-i}(A+d-1).
```

The other triangle is obtained by `(a,p)<->(b,q)`.  Finally,

```text
I_{a,b}^{p,q}
 = (-1)^(p+q-2) [F_{a,b}^{p,q}+F_{b,a}^{q,p}]
   / [Gamma(p)Gamma(q)].
```

The leading sign is the `(-log)` Laplace sign discussed in §3.  Since
`p,q in {1,2}`, every multiple zeta value in the formula has weight at most
five and reduces by the six identities listed in §6.  This proves that the
universal integrals have exactly the coefficient format used by the checker.
