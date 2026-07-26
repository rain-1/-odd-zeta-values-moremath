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

## 5. Published middle-row reduction `[PROVED — compact middle row]`

Brown--Zudilin `(I3)` specializes, with `k=n+l`, to

```text
I''_n =
  sum_{l=0}^n (-1)^l C(n+l,n) C(n,l)^2
  J_3(n,n,n,n-l; n,n,n+l).
```

The condition for the generalized Beukers integral is
`(n-l)+(n+l)=n+n`.  Its rational coefficient can be evaluated uniformly.
Use the parameter correspondence in Zudilin's Lemma 6, equations `(3.8)` and
`(3.10)`.  For this specialization it gives

```text
a = (n+1, n-l+1, n+1, n+1),
b = (1,   1-l,   2n+2, 2n+2)
```

and the one-variable rational function

```text
R_{n,l}(t) =
 prod_{i=1}^n(t+i) prod_{i=1}^n(t+i-l)
 / prod_{i=n+1}^{2n+1}(t+i)^2.
```

Its poles are `t=-n-1-k`, `0<=k<=n`, of order two.  Write

```text
R_{n,l}(t)
 = sum_k [A_{kl}/(t+n+1+k)^2+B_{kl}/(t+n+1+k)].
```

Deleting the vanishing denominator factor and then logarithmically
differentiating gives

```text
A_{kl}
 = (n+k)!(n+k+l)!/[k!^3(k+l)!(n-k)!^2]
 = C(n+k,n) C(n+k+l,n) C(n,k)^2,

B_{kl}/A_{kl}
 = -(H_{n+k}-H_k)
   -(H_{n+k+l}-H_{k+l})
   -2(H_{n-k}-H_k)
 = L_k.
```

Zudilin's Lemma 4, equation `(2.15)` and the evaluation following it,
therefore gives

```text
J_3(n,n,n,n-l;n,n,n+l)
 = (-1)^l {
     2 [sum_k A_{kl}] zeta(3)
     - sum_k A_{kl}[2H3_{k+l}+L_k H2_{k+l}]
   }.
```

The outer coefficient in the specialized descent is

```text
(-1)^l C(n+l,n) C(n,l)^2,
```

and its product with `A_{kl}` is exactly `T(n,k,l)`.

There is a factor-two normalization worth spelling out.  The residue integral
displayed immediately before Brown--Zudilin `(I3)` is `2I''` in their
normalization

```text
I = 2I' + 4I'' zeta(2),       I''=Q zeta(3)-Phat.
```

The factor is uniform and follows without fitting a constant at any value of
`n`.  Indeed, Lemma 4 gives the `zeta(3)` coefficient

```text
2 sum_{k,l}
  C(n+l,n) C(n,l)^2
  C(n+k,n) C(n+k+l,n) C(n,k)^2
=2 sum_{k,l} T(n,k,l)
=2Q_n.
```

The product in the first line is identically `T`, merely with its six
binomial factors reordered.  On the other hand the `zeta(3)` coefficient of
`I''_n` is `Q_n`.  These are explicit rational coefficients inside the same
descent calculation, so this comparison uses no linear-independence statement
about real zeta values.  The residue descent therefore computes `2I''_n` for
every `n`.  Thus it yields

```text
Phat_n
 = sum_{k,l} T(n,k,l)
     [H3_{k+l} + (1/2)L_k H2_{k+l}]
 = sum_{k,l} T(n,k,l)
     [H3_{k+l} + (1/4)(L_k+L_l)H2_{k+l}].               (M)
```

The second equality is `k<->l` symmetry.  Section 7.3 proves that the right
side of `(M)` is exactly `sum T w3sym`.  Consequently

```text
Phat_n = sum_{k,l=0}^n T(n,k,l) w3sym(n,k,l)
       = sum_{k,l=0}^n T(n,k,l) w3hat(n,k,l)
```

for every `n>=0`; the last equality is symmetrization against `T`.  No
finite-range check, recurrence fit, or linear-independence claim for zeta
values is used.

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

## 7. Three uniform kernel identities `[PROVED]`

### 7.1 The unwanted `zeta(4)` coefficient

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
also reconstructed independently from exact values).

### 7.2 The unwanted `zeta(3)` coefficient

Put, temporarily,

```text
A_{kl}=C22(k,l),  B_{kl}=C12(k,l),
C_{kl}=C21(k,l),  D_{kl}=C11(k,l).
```

The rational function and its partial fractions are symmetric, so

```text
A_{kl}=A_{lk},  C_{kl}=B_{lk},  D_{kl}=D_{lk}.
```

Also `R_n=O(x^-2)` as `x -> infinity`.  The coefficient of `x^-1` in its
partial fractions is therefore identically zero as a rational function of
`y`.  Uniqueness of partial fractions in `y` gives, for each fixed `l`,

```text
sum_k B_{kl}=0,       sum_k D_{kl}=0.
```

Consequently, after discarding the `D` sum and using symmetry, the coefficient
of `zeta(3)` (apart from a nonzero common scalar) is

```text
E =
 sum_{k,l} [
   A_{kl}(H2_k+H2_l-2H2_{k+l})
   + B_{kl}(H_k-H_{k+l})
   + C_{kl}(H_l-H_{k+l})]

  = -2 sum_{l=0}^n sum_{j=1}^l sum_{k=0}^n
        [ A_{kl}/(k+j)^2 + B_{kl}/(k+j) ].
```

The last equality uses

```text
H_k-H_{k+l} = -sum_{j=1}^l 1/(k+j),
H2_k-H2_{k+l} = -sum_{j=1}^l 1/(k+j)^2
```

and the `k<->l` symmetry for the second halves of both expressions.  But the
innermost sum is exactly `g_l(j)`, for the rational function in §7.1:

```text
g_l(j)=sum_k [A_{kl}/(j+k)^2+B_{kl}/(j+k)].
```

After the translation used there, `g_l(x)` retains the numerator factor

```text
prod_{r=1}^n (x-r).
```

Its denominator is nonzero at every positive `x=j`, and hence
`g_l(j)=0` for `1 <= j <= l <= n`.  Thus `E=0`, proving that the unwanted
`zeta(3)` coefficient vanishes for every `n`.

### 7.3 The `zeta(2)`/compact-weight-3 bridge

Use the swapped orientation of the same partial fractions:

```text
g_k(y) = sum_l [A_{kl}/(y+l)^2+C_{kl}/(y+l)],
Q_k(y) = sum_l [B_{kl}/(y+l)^2+D_{kl}/(y+l)].
```

Here `Q_k` is the coefficient of the simple pole in `x`; directly from the
product for `R_n`,

```text
g_k(y) = c_k
  prod_{r=1}^n(y-r) prod_{r=1}^n(y-k-r)
  / prod_{r=0}^n(y+r)^2,
```

and `Q_k(y)=g_k(y)Lambda_k(y)` for a logarithmic derivative `Lambda_k`
having no pole at `1 <= y <= k`.  Hence

```text
Q_k(j)=0                 (1 <= j <= k).
```

Using the universal `zeta(2)` coefficients displayed above, symmetry, and

```text
H2_l-H2_{k+l} = -sum_{j=1}^k 1/(l+j)^2,
H_l-H_{k+l}   = -sum_{j=1}^k 1/(l+j),
```

the terms not already equal to
`-4 A_{kl}H3_{k+l}-(B_{kl}+C_{kl})H2_{k+l}` sum to

```text
-2 sum_k sum_{j=1}^k Q_k(j)=0.
```

After undoing the common factor between `A_{kl}` and `T`, this proves

```text
sum T [zeta(2)]W_B
 = -4 sum T H3_{k+l} - sum T(L_k+L_l)H2_{k+l}.            (1)
```

It remains to identify the right side with `-4 sum T w3sym`.  Since
`L_k-L_l=-2Psi`, multiplying the compact symmetric weight by `4A_{kl}` and
using symmetry reduces the difference between the two sides of (1) to

```text
sum_{k,l} [
  4 A_{kl}(H3_{n+k}-H3_{k+l})
  + 2 B_{kl}(H2_{n+k}-H2_{n+l}-H2_{k+l})].
```

For fixed `l`, the term `-2B_{kl}H2_{n+l}` sums to zero because
`sum_k B_{kl}=0`.  Expanding the other two harmonic differences leaves

```text
sum_l sum_{j=l+1}^n sum_k
  [4A_{kl}/(k+j)^3+2B_{kl}/(k+j)^2]
 = -2 sum_l sum_{j=l+1}^n g_l'(j).
```

But

```text
g_l(x)=c_l
  prod_{r=1}^n(x-r) prod_{r=1}^n(x-l-r)
  / prod_{r=0}^n(x+r)^2.
```

For `l<j<=n`, the first numerator product vanishes at `j`, and the second
vanishes because `1<=j-l<=n`; the denominator is nonzero.  Thus `g_l` has a
double zero at `j`, so `g_l'(j)=0`.  Therefore

```text
sum T [zeta(2)]W_B = -4 sum T w3sym
```

for every `n`.

The only remaining all-`n` Barnes kernel identity is now the
rational/compact-weight-5 bridge.

### 7.4 The simple-pole function and its sharp zero range

The weight-5 calculation also needs the coefficient of the simple pole in the
second variable.  Put

```text
P(z)=prod_{r=1}^n(z-r),       Q(z)=prod_{r=0}^n(z+r).
```

For fixed `0 <= l <= n`, delete the factor `(y+l)^2` from

```text
R_n(x,y)=P(x)P(y)P(x+y)/[Q(x)^2Q(y)^2]
```

and differentiate the resulting product at `y=-l`.  If `q_l(x)` denotes this
simple-pole coefficient, the product rule (without any logarithmic division)
gives

```text
q_l(x)=c_l P(x)/Q(x)^2 [P'(x-l)+lambda_l P(x-l)],
```

where `c_l != 0` and `lambda_l` is finite: after deleting `(y+l)^2`,
all remaining denominator factors are nonzero at `y=-l`, while
`P(-l)=prod_{r=1}^n(-l-r) != 0`.  Consequently

```text
q_l(j)=0                    (1 <= j <= n).                 (2)
```

This avoids the more delicate shorthand `q_l=g_l Lambda_l` at a diagonal
zero.  The derivative in `y` never touches the explicit factor `P(x)`, so that
factor survives syntactically.  Since `Q(j) != 0` for positive `j`, (2) follows
immediately.  The upper range is sharp: the factor `P(j)` no longer vanishes at
`j=n+1`.

In partial fractions,

```text
q_l(x)=sum_k [C_{kl}/(x+k)^2+D_{kl}/(x+k)].
```

Thus (2), together with the sharp ranges for `g_l` and `g_l'` in §§7.2–7.3,
is available for the remaining combined weight-5 reduction.

### 7.5 Barnes coefficients and the epsilon jets are the same local object

The residue and epsilon-deformation descriptions have an exact dictionary.
For the local double-pole coefficient `A=C22` of §2,

```text
C12/C22 = L_k = -partial_k log T,
C21/C22 = L_l = -partial_l log T,
C11/C22 = L_k L_l-C_2.
```

Here the derivatives mean logarithmic derivatives of the gamma continuation,
evaluated at the integer lattice point.  In the deformation normalisation of
`Z5CF_EPSILON`, its first logarithmic jet is

```text
L_1^epsilon = 2 L_l^Barnes.
```

Thus the Barnes local table is the two-variable logarithmic 2-jet of the same
gamma product whose higher Bell coefficients produce the compact weights.
This also explains a limitation of §§7.1–7.4: fixed-pole evaluations see the
value and first derivative jets, but not every quadratic or cubic expression
in `L_l`.

The missing identities are supplied by *pole-raising jets*.  If `R_k(z)` is a
one-variable residue function and `rho(z)` has a pole at the same lattice
points, the global residue theorem applied to `R_k(z)rho(z)` extracts the
second and third logarithmic jets of `R_k`.  The useful choices include

```text
rho(z) = (sum_j 1/(z-j))^2,
rho(z) = (sum_j 1/(z-j)) (sum_{i=0}^n 1/(z+i)).
```

Off-lattice residues vanish by the same numerator-`P` mechanism used in
§§7.2–7.4.  One must not use arbitrary products of pole sums: when a shared
double pole meets only a simple zero of `R_k`, an extra residue remains.  Each
jet family therefore requires the same direct product/zero-order check as the
fixed-pole identities.

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

More explicitly, no divergent series is being assigned a value here.  Sum the
partial-fraction identity only for `1 <= t <= M`.  Its two simple-pole terms are

```text
a_1 H_M + b_1(H_{M+h}-H_h),       a_1+b_1=0.
```

This equals `b_1(H_{M+h}-H_M-H_h)` and tends to `-b_1 H_h`; all terms of order
at least two converge ordinarily.  Thus the displayed formula for `U` is the
limit of a sequence of finite rational identities.  The notation
`Z_1(N) = -H_{N-1}` is only shorthand for the finite part that remains after this
cancellation.

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

For the same reason, the `m=1` occurrence in `S_{r,1}` is also an ordinary
limit: use

```text
H_{t+d-1}=H_t+sum_{h=1}^{d-1} 1/(t+h)
```

at a finite upper cutoff, then pass to the limit.  Here `r` is `2` or `3`, so
`sum H_t/t^r` and every shifted-product sum converge absolutely.  The
geometric expansions used on each open triangle are dominated after inserting
the logarithmic factors occurring for `p,q in {1,2}`; equivalently, one may
integrate first over `[delta,1-delta]^2` away from the diagonal and then let
`delta -> 0`.  The two triangle formulas have matching integrable boundary
limits.  This supplies the cutoff justification behind `universal.py`; it does
not by itself discharge the remaining all-`n` rational/weight-5 bridge from
§7.
