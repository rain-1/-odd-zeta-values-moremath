# Lean handoff: the Catalan harmonic companion

## 0. Current status and trust boundary

The finite harmonic formula in this note is now **proved**, not merely checked for
small indices.  The present proof has two layers:

1. elementary rational identities give exact scalar recurrences for four auxiliary
   sequences;
2. `ore_algebra` performs exact arithmetic over `ℚ(x)`, constructs annihilators for
   two exponential-generating-function residuals, and proves that they share an
   order-10 right factor.  Finite zero-coefficient propagation then proves the desired
   identity for all indices.

The external computation is reproducible, but a Lean formalization should not treat its
output as an oracle.  The recommended formalization path below turns the certificate into
explicit polynomial identities and a generic coefficient-propagation lemma.

Exact audit commands from the repository root:

```text
python work/harmonic_jets/verify_catalan_scalar.py
/home/ubuntu/.local/opt/harmonic-ore/bin/python \
  work/harmonic_jets/prove_catalan_ore.py
```

The final line of the second command is

```text
SUCCESS: L(E*C-A*D)=1 identically; Catalan formula is proved
```

The polynomial common factor has order 10, degree 29, and SHA-256 fingerprint

```text
5f255471c10932d5a24a7cf4f429729bda8d9f73740aa3a1c37e261e70312fba
```

The files to read first are:

- `work/harmonic_jets/verify_catalan_scalar.py` — transparent symbolic verification of
  the scalar recurrences;
- `work/harmonic_jets/prove_catalan_ore.py` — exact common-factor and propagation proof;
- `papers_out/harmonic_jets/main.tex`, Section 6 — connected lift and parity reduction;
- `lean/ZetaLucas/Letters.lean` and `lean/ZetaLucas/TheoremLB.lean` — existing harmonic
  letters and character-resolved Lucas machinery;
- `lean/ZetaLucas/Z2Shell.lean` and `lean/ZetaLucas/Z2Minimal.lean` — the closest model
  for a recurrence-defined second solution.

## 1. Definitions, with all index conventions fixed

Work over `ℚ` for the recurrence theorem.  Define the real character modulo 4 by

\[
\chi_{-4}(j)=
\begin{cases}
0,&2\mid j,\\
1,&j\equiv1\pmod4,\\
-1,&j\equiv3\pmod4.
\end{cases}
\]

For `q ≥ 1` and `m : ℕ`, define

\[
H_m^{(q)}=\sum_{j=1}^m\frac1{j^q},\qquad
K_m^{(q)}=\sum_{j=1}^m\frac{\chi_{-4}(j)}{j^q}.
\]

Both sums are zero when `m = 0`.  In Lean it is least painful to write them as sums over
`Finset.range m`, using the denominator `j+1`.

Define

\[
S_E(n,k)=
\binom nk\binom{2k}{k}\binom{2(n-k)}{n-k}
\]

for `k ≤ n`, and define it to be zero for `k > n`.  This explicit zero extension is useful
for Lucas and convolution arguments.

The first solution is

\[
A_E(n)=\sum_{k=0}^n S_E(n,k).
\]

Put

\[
\alpha_k=\frac34H_k-\frac12H_{2k}.
\]

The new companion formula is

\[
B_E(n)=\sum_{k=0}^n S_E(n,k)
\left[
\frac12K_{2k}^{(2)}+
\alpha_k\left(K_{2k}^{(1)}-K_{2n-2k}^{(1)}\right)
\right]. \tag{CAT}
\]

The target recurrence is

\[
(n+1)^2u_{n+1}
=(12n^2+12n+4)u_n-32n^2u_{n-1}. \tag{REC}
\]

For the companion, `(REC)` is asserted for `n ≥ 1`, with

\[
B_E(0)=0,\qquad B_E(1)=1.
\]

Initial values useful for regression tests are

\[
B_E(n)=0,1,7,\frac{404}{9},\frac{2603}{9},
\frac{428284}{225},\frac{2884316}{225},\ldots
\]

and

\[
A_E(n)=1,4,20,112,676,\ldots.
\]

## 2. Lean theorem statements

Suggested names and statement shapes (ASCII is used only for readability):

```lean
def chi4 (j : ℕ) : ℤ := ...
def harm (q m : ℕ) : ℚ := ...
def kharm4 (q m : ℕ) : ℚ := ...
def catShell (n k : ℕ) : ℤ := ...
def catA (n : ℕ) : ℤ := ∑ k ∈ Finset.range (n+1), catShell n k
def catAlpha (k : ℕ) : ℚ := 3/4 * harm 1 k - 1/2 * harm 1 (2*k)
def catB (n : ℕ) : ℚ := ... -- formula (CAT)

theorem catA_rec (n : ℕ) :
    (n+1)^2 * catA (n+1)
      = (12*n^2+12*n+4) * catA n - 32*n^2 * catA (n-1) := ...

theorem catB_zero : catB 0 = 0 := ...
theorem catB_one  : catB 1 = 1 := ...

theorem catB_rec (n : ℕ) (hn : 1 ≤ n) :
    ((n+1 : ℚ)^2) * catB (n+1)
      = (12*n^2+12*n+4) * catB n - 32*n^2 * catB (n-1) := ...
```

Avoid Lean's truncated subtraction until the hypothesis `k ≤ n` is in scope.  For
`catShell`, either use an `if h : k ≤ n` branch or use binomial coefficients whose
out-of-range value is already zero, but do not silently identify the two approaches.

## 3. The compact lift (independent theorem, easy formalization)

Let

\[
X_m(t)=\prod_{j=1}^m(1-t/j)^{-1},\qquad
Y_m(t)=\prod_{j=1}^m(1-t/j)^{-\chi_{-4}(j)}.
\]

Define

\[
\begin{aligned}
\mathcal F_E(n,k;u,v)=S_E(n,k)&
\frac{X_k(3u/4)}{X_{2k}(u/2)}
\frac{Y_{2k}(v)}{Y_{2n-2k}(v)}\\
&\times
\frac{Y_{2k}(u+v/2)}{Y_{2k}(u)Y_{2k}(v/2)}.
\end{aligned}
\]

Then the summand in `(CAT)` is exactly

\[
\left.\partial_u\partial_v\mathcal F_E(n,k;u,v)\right|_{u=v=0}.
\]

For Lean, it is not necessary to formalize analytic differentiation.  Introduce a
two-variable second-order jet structure with fields `const`, `du`, `dv`, `duv`, define
multiplication by the product rule, and prove the four logarithmic-jet identities by
finite-product induction.  The relevant values are

\[
(\log\mathcal F_E)_u=\alpha_k,
\quad
(\log\mathcal F_E)_v=K_{2k}^{(1)}-K_{2n-2k}^{(1)},
\quad
(\log\mathcal F_E)_{uv}=\frac12K_{2k}^{(2)}.
\]

This establishes that the formula is generated by the connected lift, but it is not the
recurrence proof.

## 4. Elementary coefficient system underlying the recurrence proof

Define

\[
c_k=\binom{2k}{k},\qquad
a_k=c_k\alpha_k,\qquad
d_k=c_kK_{2k}^{(1)},
\]

\[
e_k=c_k\left(\frac12K_{2k}^{(2)}+\alpha_kK_{2k}^{(1)}\right),
\qquad
p_k=(-1)^kc_k,\qquad s_k=(-1)^ka_k.
\]

The three fundamental increments are

\[
\alpha_{k+1}-\alpha_k=
\frac{k}{2(k+1)(2k+1)}, \tag{I1}
\]

\[
K_{2k+2}^{(1)}-K_{2k}^{(1)}=
\frac{(-1)^k}{2k+1}, \tag{I2}
\]

\[
K_{2k+2}^{(2)}-K_{2k}^{(2)}=
\frac{(-1)^k}{(2k+1)^2}. \tag{I3}
\]

These imply the coupled recurrences

\[
(k+1)c_{k+1}=2(2k+1)c_k, \tag{C1}
\]

\[
(k+1)^2a_{k+1}=2(k+1)(2k+1)a_k+kc_k, \tag{C2}
\]

\[
(k+1)d_{k+1}=2(2k+1)d_k+2p_k, \tag{C3}
\]

\[
(k+1)p_{k+1}=-2(2k+1)p_k, \tag{C4}
\]

\[
(k+1)^2s_{k+1}=-2(k+1)(2k+1)s_k-kp_k, \tag{C5}
\]

\[
(k+1)^2e_{k+1}
=2(k+1)(2k+1)e_k+p_k+2(k+1)s_k+kd_k. \tag{C6}
\]

`(C6)` is the most useful new simplification.  Expanding its right side from `(I1)`--`(I3)`
and calling `ring` should prove it directly in Lean once nonzero denominators have been
discharged.

## 5. Binomial convolution and residual identity

The formula `(CAT)` is the difference of two binomial convolutions:

\[
B_E(n)=\sum_{k=0}^n\binom nk
\left(e_kc_{n-k}-a_kd_{n-k}\right). \tag{CONV}
\]

Equivalently, for exponential generating functions

\[
C(x)=\sum c_n\frac{x^n}{n!},\quad
A(x)=\sum a_n\frac{x^n}{n!},\quad
D(x)=\sum d_n\frac{x^n}{n!},\quad
E(x)=\sum e_n\frac{x^n}{n!},
\]

we have

\[
\sum B_E(n)\frac{x^n}{n!}=E(x)C(x)-A(x)D(x). \tag{DET}
\]

Let `θ = x D_x` and

\[
\mathscr L=(\theta+1)^2D_x-(12\theta^2+12\theta+4)
+32x(\theta+1). \tag{L}
\]

If `F(x)=Σ f_n x^n/n!`, then the coefficient of `x^n/n!` in `𝓛F` is

\[
(n+1)^2f_{n+1}-(12n^2+12n+4)f_n+32n^2f_{n-1}.
\]

Set

\[
Y_1=\mathscr L(EC),\qquad Y_2=\mathscr L(AD).
\]

The exact certificate proves

\[
Y_1-Y_2=1. \tag{RES}
\]

This is equivalent to `(REC)` for `B_E` at every `n ≥ 1`, with the exceptional constant
coefficient encoding the initial cell.

## 6. Exact Ore certificate, stated as finite algebra

From the exact scalar recurrences for `c,a,d,e`, holonomic closure gives operators
`H1,H2 ∈ ℚ(x)⟨Dx⟩` annihilating `Y1,Y2`, with orders 44 and 29.  After clearing scalar
denominators there is a common right factor `Cop ∈ ℚ[x]⟨Dx⟩` of order 10 and polynomial
degree 29:

\[
H_1=U_1C_{op},\qquad H_2=U_2C_{op},
\qquad \operatorname{ord}(U_1)=34,
\quad \operatorname{ord}(U_2)=19. \tag{F}
\]

Also `Cop(1)=0`.

The proof does not infer `(F)` from data: all three are exact zero-remainder right
divisions over `ℚ(x)`.  A guessed order-11 operator is used only to locate `Cop`.

For a polynomial differential operator

\[
T=\sum_{j,i}t_{j,i}x^iD_x^j,
\]

the coefficient of `x^n` in `Tf` involves `f_{n+j-i}`.  Let

\[
r=\max\{j-i:t_{j,i}\ne0\}.
\]

The coefficient of the forward term `f_{n+r}` is

\[
P_T(n)=\sum_{j-i=r}t_{j,i}(n-i+1)(n-i+2)\cdots(n-i+j). \tag{P}
\]

The three operators `U1,U2,Cop` all have `r=4`.  Their forward coefficients, up to
nonzero rational constants, are:

\[
\begin{aligned}
P_{U_1}(z)={}&(z+1)(z+2)^2(z+3)^2(z+4)^3(z+5)^3
\prod_{j=6}^{9}(z+j)^2\\
&\times\left(z^5+\frac{61}{2}z^4+370z^3+
\frac{4461}{2}z^2+\frac{26709}{4}z+\frac{63465}{8}\right)^3,
\end{aligned}
\]

\[
P_{U_2}(z)=(z+1)(z+2)^2(z+3)^2(z+4)^3(z+5)^3
\prod_{j=6}^{9}(z+j)^2,
\]

\[
P_{C_{op}}(z)=(z+1)(z+2)^2(z+3)^2(z+4)^4(z+5).
\]

All are nonzero for `z ≥ 0`; positivity proves this without root-finding.  The complete
forward coefficient is present starting at `z=30`, `z=15`, and `z=6`, respectively.

Exact coefficient expansion gives:

- the first 34 coefficients of `Cop Y1` are zero;
- the first 19 coefficients of `Cop Y2` are zero;
- the first 10 coefficients of `Y1-Y2-1` are zero.

Now `(F)` and forward induction give `Cop Y1=Cop Y2=0`.  Since `Cop(1)=0`, the series
`Y1-Y2-1` is also a `Cop`-solution; the final 10 initial coefficients and the third
forward recurrence prove `(RES)`.

### Generic Lean lemma needed for this step

Prove once:

```lean
theorem eq_zero_of_polyDiffRec
    (T : PolyDiffOp ℚ)
    (r start : ℕ)
    (hlead : forwardShift T = r)
    (hcoeff : ∀ n, start ≤ n → forwardCoeff T n ≠ 0)
    (hf : T.ActsOn f = 0)
    (hinit : ∀ n < start + r, f n = 0) :
    ∀ n, f n = 0 := ...
```

The proof is strong induction on `n`; isolate the unique `f (n+r)` term and divide by
`forwardCoeff T n`.

### Important certificate-export task

`prove_catalan_ore.py` currently reconstructs the full operators and checks them.  Before
formalizing `(F)`, add a deterministic exporter that prints the coefficient arrays of
`Cop`, `U1`, `U2`, `H1`, and `H2` in a Lean-readable sparse format.  Check the `Cop`
fingerprint above after import.  Do not hand-transcribe these large polynomials.

## 7. Suggested module split

1. `ZetaLucas/CatalanDefs.lean`
   - `chi4`, `kharm4`, `catShell`, `catA`, `catB`;
   - initial values;
   - symmetry of `catShell`.
2. `ZetaLucas/CatalanIncrements.lean`
   - `(I1)`--`(I3)` and `(C1)`--`(C6)`;
   - no Ore algebra, no generating functions.
3. `ZetaLucas/PolyDiffOp.lean`
   - sparse polynomial differential operators;
   - multiplication/composition;
   - action on formal coefficient streams;
   - exact right-factor identity as coefficient equality;
   - the forward-propagation lemma.
4. `ZetaLucas/CatalanCertificateData.lean`
   - generated sparse coefficient arrays and their evaluated operators.
5. `ZetaLucas/CatalanRecurrence.lean`
   - convolution identity `(CONV)`;
   - EGF/product coefficient lemmas;
   - certificate application and `catB_rec`.
6. `ZetaLucas/CatalanLucas.lean` (follow-on)
   - the character-twisted Lucas law stated in Section 9 below.
7. `ZetaLucas/CatalanLimit.lean` (optional analytic follow-on)
   - weighted-average proof of the limit and Casoratian error formula.

Reuse `Rat`/`ℚ` APIs already exercised in `Z2Minimal.lean`.  Keep the certificate layer
purely algebraic; it should require neither real analysis nor `FormalPowerSeries` if
coefficient streams are represented as `ℕ → ℚ`.

## 8. A direct, self-contained evaluation of the limit

The formula makes the value `G/2` accessible without citing a sporadic table.

Normalize the positive shell to a probability measure

\[
\mu_n(k)=\frac{S_E(n,k)}{A_E(n)}.
\]

By shell symmetry, with `ℓ=n-k`, formula `(CAT)` can be rewritten as

\[
\frac{B_E(n)}{A_E(n)}=
\sum_k\mu_n(k)\left[
\frac14\left(K_{2k}^{(2)}+K_{2\ell}^{(2)}\right)
+\frac12(\alpha_k-\alpha_\ell)
       \left(K_{2k}^{(1)}-K_{2\ell}^{(1)}\right)
\right]. \tag{SYM}
\]

On the bulk `n/4 ≤ k ≤ 3n/4`, the alternating-series bounds give

\[
\left|K_{2k}^{(2)}-G\right|\le\frac1{(2k+1)^2},
\]

\[
\left|K_{2k}^{(1)}-K_{2\ell}^{(1)}\right|
\le\frac1{2\min(k,\ell)+1},
\]

while `(I1)` bounds `|α_k-α_ℓ|` uniformly on this bulk.  Hence the integrand in `(SYM)`
is `G/2 + O(1/n)` there.  The ratio

\[
\frac{S_E(n,k+1)}{S_E(n,k)}=
\frac{(n-k)^2(2k+1)}{(k+1)^2(2n-2k-1)}
\]

shows that the two outer quarters have exponentially small total mass.  The integrand is
only `O(log(n+1))` globally, so the boundary contribution vanishes.  Therefore

\[
\lim_{n\to\infty}\frac{B_E(n)}{A_E(n)}=\frac G2. \tag{LIMIT}
\]

This is the preferred self-contained proof of the table value.  It uses the new harmonic
formula essentially and avoids modular-form or continued-fraction identification.

## 9. Two striking arithmetic consequences

### 9.1 Exact Casoratian and a positive series for Catalan's constant

For any two solutions `A,B` of `(REC)`, define

\[
W_n=A_nB_{n-1}-A_{n-1}B_n.
\]

The recurrence gives

\[
W_{n+1}=\frac{32n^2}{(n+1)^2}W_n.
\]

For `A_E(0)=1`, `A_E(1)=4`, `B_E(0)=0`, `B_E(1)=1`, this yields

\[
W_n=-\frac{32^{n-1}}{n^2}.
\]

Consequently

\[
\frac{B_E(n)}{A_E(n)}-
\frac{B_E(n-1)}{A_E(n-1)}
=\frac{32^{n-1}}{n^2A_E(n)A_E(n-1)}>0. \tag{ERR1}
\]

Combining `(ERR1)` with `(LIMIT)` gives

\[
\frac G2-\frac{B_E(n)}{A_E(n)}
=\sum_{m=n+1}^{\infty}
\frac{32^{m-1}}{m^2A_E(m)A_E(m-1)}, \tag{ERR2}
\]

and, at `n=0`, the positive series

\[
G=2\sum_{m=1}^{\infty}
\frac{32^{m-1}}{m^2A_E(m)A_E(m-1)}. \tag{GSER}
\]

Thus the harmonic formula supplies explicit rational, monotone lower approximants and an
exact positive error tail.  The associated continued fraction was already implicit in
Zagier's recurrence, so novelty should be claimed for the harmonic numerator formula and
the resulting self-contained derivation, not for the bare continued fraction.

### 9.2 Character-twisted Lucas law for the second solution

The natural full-digit target, for every odd prime `p` and `0 ≤ a,r < p`, is

\[
p^2B_E(ap+r)\equiv
\chi_{-4}(p)B_E(a)A_E(r)\pmod p. \tag{LUC}
\]

This has been checked exactly for every `a,r` and every odd prime `p ≤ 31`.  The paper now
gives two complementary proofs: a termwise proof under the half-digit hypothesis
`2*a+1 < p`, and an unrestricted proof when every first-solution digit `A_E(j)`,
`0 ≤ j < p`, is nonzero modulo `p`.

Why `(LUC)` should hold:

- every monomial in `(CAT)` has total harmonic weight 2;
- every monomial has the same character signature `χ_{-4}`;
- `catShell` has Lucas factorization;
- on a nonzero digit cell, the central binomial factors force
  `2s<p` and `2(r-s)<p`, so the wide arguments `2k` and `2(n-k)` descend without a carry;
- if an outer digit `b` or `a-b` has a doubling carry, the corresponding central binomial
  coefficient makes the outer shell vanish modulo `p`.

Under `2*a+1 < p`, all harmonic arguments are below `p^2`, and the nonzero low-digit
shell forces `2*s<p` and `2*(r-s)<p`.  This gives a direct termwise proof using the
one-letter descent lemma.  The existing abstract theorem in `TheoremLB.lean` is close but
its tameness hypothesis `arg n k ≤ n` excludes `2k`; formalize the short specialized
argument from Theorem 6.9 of the paper.

Without the half-digit hypothesis, a naive termwise proof is false: when `2k ≥ p^2`,
individual carry cells have genuine p-adic poles.  Their sum cancels in every exact test.
The full theorem therefore needs a block-sum carry-cancellation lemma, not merely a looser
tameness bound.

There is, however, a clean full-digit theorem away from zero digits.  First prove

\[
A_E(p-1)\equiv(-1)^{(p-1)/2}=\chi_{-4}(p)\pmod p. \tag{LAST}
\]

In the shell sum for `A_E(p-1)`, the two central binomial coefficients force
`k=(p-1)/2`; that one shell is `(-1)^((p-1)/2)` modulo `p`.

Now assume `A_E(j) ≠ 0 (mod p)` for every `0 ≤ j < p`.  Lucas factorization makes every
`A_E(m)` with `m<p^2` a `p`-unit.  The finite Casoratian sum is

\[
\frac{B_E(N)}{A_E(N)}=
\sum_{m=1}^{N}\frac{32^{m-1}}{m^2A_E(m)A_E(m-1)}. \tag{VAR}
\]

For `N=ap+r`, multiply `(VAR)` by `p^2` and reduce modulo `p`.  Only `m=jp` survives.
Lucas and Fermat give

\[
\frac{p^2B_E(ap+r)}{A_E(ap+r)}
\equiv\frac1{A_E(p-1)}
\sum_{j=1}^a\frac{32^{j-1}}{j^2A_E(j)A_E(j-1)}
=\frac{B_E(a)}{A_E(a)A_E(p-1)}.
\]

Use `A_E(ap+r) ≡ A_E(a)A_E(r)` and `(LAST)` to obtain `(LUC)` with no restriction on
`a,r`.  This argument is particularly Lean-friendly once the Casoratian identity and
first-solution Lucas theorem are available: it is a finite localization calculation,
not a carry analysis.

## 10. Sharp denominator theorem (now proved)

Let `L_m = lcm(1,2,...,m)`.  Formula `(CAT)` immediately gives the coarse but explicit
bound

\[
4L_{2n}^2B_E(n)\in\mathbb Z. \tag{DEN}
\]

The much sharper statement is now a theorem:

\[
L_n^2B_E(n)\in\mathbb Z. \tag{SHARP-DEN}
\]

The proof is independent of the large Ore certificate once `(REC)` and the two initial
values are available.  Define

\[
T_n=\sum_{k=0}^n\binom nk(-4)^{n-k}B_E(k). \tag{TDEF}
\]

Ordinary generating-function substitution, or direct binomial algebra, gives

\[
(n+1)^2T_{n+1}-16n^2T_{n-1}=(-4)^n,\qquad T_{-1}=T_0=0. \tag{TREC}
\]

Iterating on the two parity classes gives

\[
(-1)^{n-1}T_n=
\sum_{\substack{0\le j<n\\n-j\ {\rm odd}}}R_{n,j}^2, \tag{TSQ}
\]

\[
R_{n,j}=2^{n-1}
\frac{(j+2)(j+4)\cdots(n-1)}
     {(j+1)(j+3)\cdots n}. \tag{R}
\]

The key elementary lemma is

\[
L_nR_{n,j}\in\mathbb Z. \tag{RL}
\]

For an odd prime `p`, write the negative valuation of the ratio in `(R)` as a sum over
prime powers `p^a`.  Multiples of `p^a` in `[j+1,n]` are `p^a` times a consecutive
interval.  Since `p^a` is odd, it preserves parity, and the denominator parity class
outnumbers the numerator parity class by at most one.  Hence

\[
-v_p(R_{n,j})\le \#\{a:p^a\le n\}=v_p(L_n).
\]

For `p=2`, the denominator progression is either odd or has valuation at most
`v₂(n!) ≤ n-1`, which is absorbed by the factor `2^(n-1)`.  This proves `(RL)`,
and `(TSQ)` gives `L_n^2 T_n ∈ ℤ`.  Finally, binomial inversion is

\[
B_E(n)=\sum_{k=0}^n\binom nk4^{n-k}T_k.
\]

Since `L_k ∣ L_n`, `(SHARP-DEN)` follows termwise in the inverted sum.

This is a particularly attractive Lean target: it needs only finite sums, valuations,
parity counts, and binomial inversion.  Suggested statements:

```lean
def catT (n : ℕ) : ℚ :=
  ∑ k ∈ Finset.range (n+1), (n.choose k : ℚ) * (-4)^(n-k) * catB k

theorem catT_rec (n : ℕ) :
    ((n+1 : ℚ)^2) * catT (n+1) - 16*n^2 * catT (n-1) = (-4)^n := ...

def endpointRoot (n j : ℕ) : ℚ := ...

theorem endpointRoot_lcm_integral
    (hjn : j < n) (hpar : Odd (n-j)) :
    IsInt ((Nat.lcmRange n : ℚ) * endpointRoot n j) := ...

theorem catB_sharp_denominator (n : ℕ) :
    IsInt ((Nat.lcmRange n : ℚ)^2 * catB n) := ...
```

The exact audit is `work/harmonic_jets/check_catalan_endpoint_transform.py`.  It checks
`(TREC)`, `(TSQ)`, and every termwise assertion `(RL)` through `n=300`; the
independent recurrence audit still checks `(SHARP-DEN)` through `n=500`.

For every prime `p≥5`, the proved half-digit Lucas law with `a=1,r=0` gives
`p^2 B_E(p) ≡ χ₋₄(p) (mod p)`.  Thus `v_p(B_E(p))=-2`, so the exponent 2 in
`(SHARP-DEN)` is genuinely optimal.

### 10.1 Parameterized endpoint classification

The paper now proves a stronger reusable theorem. For an integer parameter \(b\), let
\(B^{(b)}\) be the normalized companion

\[
(n+1)^2B^{(b)}_{n+1}
=b(3n^2+3n+1)B^{(b)}_n-2b^2n^2B^{(b)}_{n-1}.
\]

Its binomial transform by \((-b)\) satisfies

\[
(n+1)^2T^{(b)}_{n+1}-b^2n^2T^{(b)}_{n-1}=(-b)^n.
\]

The same finite parity expansion proves the exact classification

\[
\left(\forall n,\ L_n^2B^{(b)}_n\in\mathbb Z\right)
\quad\Longleftrightarrow\quad 4\mid b.
\]

For sufficiency, write \(b=4d\); each endpoint contribution is
\(d^{n-1}(L_n2^{n-1}P_{n,j})^2\). Necessity is already witnessed by

\[
B^{(b)}_4=\frac{2603b^3}{576},\qquad
B^{(b)}_8=\frac{6802537507b^7}{180633600}.
\]

Thus a generic Lean theorem parameterized by \(b:\mathbb Z\) and \(4\mid b\) is the
natural follow-on after the Catalan specialization. The symbolic and exact audit is
`work/harmonic_jets/verify_general_endpoint.py`.

## 11. What is proved, proposed, and already known

| Claim | Status |
|---|---|
| Harmonic formula `(CAT)` satisfies `(REC)` | proved by exact Ore certificate |
| Compact connected lift | proved elementarily |
| `B_E/A_E → G/2` from the harmonic formula | proved by shell concentration in the paper |
| Casoratian identities `(ERR1)`--`(ERR2)` | elementary consequence of recurrence and limit |
| Positive series `(GSER)` | consequence of the preceding two |
| Coarse denominator bound `(DEN)` | proved termwise |
| Sharp denominator `(SHARP-DEN)` | proved by endpoint transform and parity valuation |
| Twisted Lucas law `(LUC)`, `2*a+1<p` | proved termwise in the paper |
| Full-digit law when all first-solution digits are `p`-units | proved from `(VAR)` and `(LAST)` |
| Full-digit twisted Lucas law at zero-digit primes | exact audit for every odd prime `p≤31`; zero--pole cancellation open |
| Irrationality of `G` | open; not implied here |
| Continued fraction for `G/2` | already known from Zagier's recurrence |

The highest-value Lean milestone is `catB_rec`.  Once that is available, the sharp
denominator theorem is the cleanest next formal milestone; it avoids analysis and the
large Ore layer.  After that come the proved half-digit Lucas law, the self-contained
analytic proof of `(LIMIT)`, and the exact error formula.  Mathematically, the remaining
high-value target is the unrestricted second-digit carry cancellation.
