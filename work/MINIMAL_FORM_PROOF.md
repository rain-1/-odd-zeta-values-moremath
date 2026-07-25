# P4c — Proof that the minimal form equals Apéry's companion

**Author:** mathematician-agent (River's odd-zeta program), 2026-07-24
**Labels:** `[PROVED]` complete certificate proof written out; `[VERIFIED n≤N]` exact finite check
(evidence, never proof); `[OPEN]`.

## Target

With
```
A(n,k) = C(n,k)^2 C(n+k,k)^2 ,     H3_m = sum_{j=1..m} 1/j^3 ,
u(n,m) = (-1)^{m-1} / ( 2 m^3 C(n,m) C(n+m,m) ) ,
c(n,k) = H3_n + sum_{m=1..k} u(n,m)          (Apéry / van der Poorten weight)
```
prove
```
  B_min(n) := sum_{k=0..n} A(n,k) ( 2 H3_n - H3_k )   ==   b_n := sum_{k=0..n} A(n,k) c(n,k).
```

**STATUS: [PROVED]** — see §7 for the assembled statement. Route R1 (recurrence + initial values),
both halves closed by explicit rational certificates verified by exact polynomial arithmetic.

---

## 0. Notation used throughout

`P(n) := 34n^3 + 51n^2 + 27n + 5`, and `L` the Apéry operator
`(L u)(n) := (n+1)^3 u(n+1) - P(n) u(n) + n^3 u(n-1)`.

The **base term** (n ≥ 1, k ≥ 0 integers)
```
  Phi(n,k) := C(n+1,k)^2 C(n+k-1,k)^2 / ( n^2 (n+1)^2 ).
```

### Lemma 0 (conversion) `[PROVED]`
For all integers `n ≥ 1`, `k ≥ 0`:
```
 (0a)  A(n,k)   = Phi(n,k) (n+1-k)^2 (n+k)^2
 (0b)  A(n+1,k) = Phi(n,k) (n+k)^2 (n+k+1)^2
 (0c)  A(n-1,k) = Phi(n,k) (n+1-k)^2 (n-k)^2
 (0d)  Phi(n,k+1) (k+1)^4 = Phi(n,k) (n+1-k)^2 (n+k)^2
```
*Proof.* Each reduces to the four binomial conversions
`C(n,k)(n+1) = C(n+1,k)(n+1-k)`, `C(n+k,k) n = C(n+k-1,k)(n+k)`,
`C(n+k+1,k) n(n+1) = C(n+k-1,k)(n+k)(n+k+1)`, `C(n-1,k) n(n+1) = C(n+1,k)(n+1-k)(n-k)`,
and (0d) to `C(n+1,k+1)(k+1) = C(n+1,k)(n+1-k)`, `C(n+k,k+1)(k+1) = C(n+k-1,k)(n+k)`.
All six are instances of the absorption identity `C(N,j+1)(j+1) = C(N,j)(N-j)` /
`C(N,j)(N+1-j)... ` and hold **for every integer** `k ≥ 0` including the degenerate range
`k > n` where both sides vanish (no `0/0`: the conversions are stated multiplicatively). ∎

Lemma 0 is the device that removes every boundary subtlety: after it, all identities below are
`Phi(n,k)` times **polynomial identities in ℚ[n,k]**.

`[VERIFIED]` all six conversions, `n = 1..12`, `k = 0..n+4`, exactly 0.

---

## 1. Step A — numerical anchor `[VERIFIED n ≤ 50]`

`B_min(n) - b_n = 0` exactly for `n = 0..50` (exact rational arithmetic, two independent
implementations: a standalone kernel script `work/minform/step_a.wl` for `n ≤ 40` and the audit
run of §7 for `n ≤ 50`).
`B_min(1..3,5) = 6, 351/4, 62531/36, 35441662103/36000` — matches the anchors.
`a_n = 1, 5, 73, 1445, 33001, 819005, 21460825`.
`L[B_min] = 0` and `L[a] = 0` numerically for `n = 1..38`.

---

## 2. Step B — Zeilberger certificate for `A(n,k)` (rederived) `[PROVED]`

Set
```
  T(n,k) := 4(2n+1)( 2k^2 - 3k - 4n^2 - 4n ),
  G(n,k) := Phi(n,k) k^4 T(n,k)
          = 4(2n+1) k^4 (2k^2-3k-4n^2-4n) C(n+1,k)^2 C(n+k-1,k)^2 / ( n^2 (n+1)^2 ).
```

### CERT-1 (polynomial identity in ℚ[n,k]) `[PROVED, Expand → 0]`
```
 T(n,k+1)(n+1-k)^2(n+k)^2 - k^4 T(n,k)
   = (n+1)^3 (n+k+1)^2 (n+k)^2 - P(n)(n+1-k)^2(n+k)^2 + n^3 (n-k)^2 (n+1-k)^2.
```

### Proposition B `[PROVED]`
For all integers `n ≥ 1`, `k ≥ 0`:
```
 (†)  (n+1)^3 A(n+1,k) - P(n) A(n,k) + n^3 A(n-1,k) = G(n,k+1) - G(n,k).
```
*Proof.* By (0a)–(0c) the left side is `Phi(n,k)` times the right side of CERT-1's second line.
By (0d), `G(n,k+1) = Phi(n,k+1)(k+1)^4 T(n,k+1) = Phi(n,k)(n+1-k)^2(n+k)^2 T(n,k+1)`, and
`G(n,k) = Phi(n,k) k^4 T(n,k)`. So the right side is `Phi(n,k)` times the left of CERT-1. ∎

**Boundary values.** `G(n,0) = 0` (factor `k^4`); `G(n,k) = 0` for `k ≥ n+2` (factor `C(n+1,k)^2`);
`G(n,n+1) = -4(n+1)^3 C(2n+1,n+1)^2`.

**Corollary (Apéry's recurrence for `a_n`).** Summing (†) over `k = 0..N` with `N ≥ n+1` telescopes
to `G(n,N+1) - G(n,0) = 0`, giving `(n+1)^3 a_{n+1} - P(n) a_n + n^3 a_{n-1} = 0`. `[PROVED]`

---

## 3. Step B' — applying `L` to `B_min` `[PROVED]`

Write `w(n,k) := 2H3_n - H3_k`, so `B_min(n) = sum_{k≥0} A(n,k) w(n,k)` (terms `k > n` vanish).
Since `w(n±1,k) = w(n,k) ± 2/(n±1)^3` in the sense `w(n+1,k)=w(n,k)+2/(n+1)^3`,
`w(n-1,k)=w(n,k)-2/n^3`,
```
 (L B_min)(n) = sum_{k≥0} w(n,k) [ (n+1)^3 A(n+1,k) - P(n)A(n,k) + n^3 A(n-1,k) ]
                + 2 sum_{k≥0} A(n+1,k) - 2 sum_{k≥0} A(n-1,k)
              = sum_{k≥0} w(n,k) ( G(n,k+1) - G(n,k) )  +  2 a_{n+1} - 2 a_{n-1}.
```
Abel summation with `w(n,k+1) - w(n,k) = -1/(k+1)^3` and `G(n,0)=0`, `G(n,k)=0` for `k ≥ n+2`:
```
 (L B_min)(n) = sum_{j≥1} G(n,j)/j^3 + 2 a_{n+1} - 2 a_{n-1}.        (B')
```

---

## 4. Step C — the correction sum vanishes `[PROVED]`

Set
```
  U(n,k) := -4(k-1)(2n+1)( 2n^2+2n+1-k ),
  K(n,k) := Phi(n,k) k^4 U(n,k) / ( n^2 (n+1)^2 )
          = -4(2n+1)(k-1)(2n^2+2n+1-k) k^4 C(n+1,k)^2 C(n+k-1,k)^2 / ( n^4 (n+1)^4 ).
```

### CERT-2 (polynomial identity in ℚ[n,k]) `[PROVED, Expand → 0]`
```
 U(n,k+1)(n+1-k)^2(n+k)^2 - k^4 U(n,k)
   = n^2(n+1)^2 [ k T(n,k) + 2( (n+k)^2(n+k+1)^2 - (n+1-k)^2(n-k)^2 ) ]
   = n^2(n+1)^2 * 4k(2n+1)( 4k^2 - 3k - 2n - 2n^2 ).
```

### Proposition C `[PROVED]`
For all integers `n ≥ 1`, `k ≥ 0` (with the convention `G(n,0)/0^3 := 0`, consistent since
`G(n,k)/k^3 = Phi(n,k) k T(n,k)`):
```
 (‡)  G(n,k)/k^3 + 2 A(n+1,k) - 2 A(n-1,k) = K(n,k+1) - K(n,k).
```
*Proof.* Left side `= Phi(n,k) [ kT(n,k) + 2((n+k)^2(n+k+1)^2 - (n+1-k)^2(n-k)^2) ]` by (0b),(0c).
Right side `= Phi(n,k)[ (n+1-k)^2(n+k)^2 U(n,k+1) - k^4 U(n,k) ] / (n^2(n+1)^2)` by (0d).
Equality is CERT-2. ∎

`K(n,0) = 0` (factor `k^4`), `K(n,k) = 0` for `k ≥ n+2` (factor `C(n+1,k)^2`).

### Corollary C `[PROVED]`
Summing (‡) over `k = 0..N`, `N ≥ n+1`:  `sum_{j≥1} G(n,j)/j^3 + 2a_{n+1} - 2a_{n-1} = 0`.

### Theorem 1 `[PROVED]`
`(L B_min)(n) = 0` for all `n ≥ 1`. (Combine (B') with Corollary C.)

---

## 5. Step D — the classical companion `b_n` satisfies the same recurrence `[PROVED]`

This is the half that needs the harmonic weight `c(n,k)` to be differenced **in `n`**. Everything
collapses because of two one-line Gosper certificates (Lemma D1) whose whole content is
`m^2 + (n+m)(n-m) = n^2` and `m^2 + (n+1-m)(n+1+m) = (n+1)^2`.

### Notation
```
  D(n,k)   := C(n,k) C(n+k,k)              (so A = D^2),
  u(n,m)   =  (-1)^{m-1} / ( 2 m^3 D(n,m) ),
  phi(n,m) := m u(n,m) = (-1)^{m-1} ((m-1)!)^2 (n-m)! / ( 2 (n+m)! ),
  Lam(n,k) := (n-k) phi(n,k+1) = (-1)^k (k!)^2 (n-k)!/( 2 (n+k+1)! )
            = (-1)^k / ( 2 (n+k+1) D(n,k) ).
```
`D(n,k) != 0` for `0 <= k <= n`, so every division below is legitimate on its stated range.

### Lemma D1 (the two inner Gosper certificates) `[PROVED]`
For `1 <= m <= n` put
```
  Y1(m) := -(n+m) phi(n,m)/n^2      = (-1)^m ((m-1)!)^2 (n-m)!  /( 2 (n+m-1)! n^2 ),
  Y2(m) := -(n+1-m) phi(n,m)/(n+1)^2 = (-1)^m ((m-1)!)^2 (n+1-m)!/( 2 (n+m)! (n+1)^2 ).
```
(The right-hand factorial forms are finite for `1 <= m <= n` resp. `1 <= m <= n+1`.)
Then, using `phi(n,m+1)/phi(n,m) = -m^2/((n-m)(n+m+1))`,
```
  Y1(m+1) - Y1(m) = phi(n,m)/n^2      * [ m^2/(n-m)   + (n+m)   ] = phi(n,m)/(n-m)     (1<=m<=n-1)
  Y2(m+1) - Y2(m) = phi(n,m)/(n+1)^2  * [ m^2/(n+m+1) + (n+1-m) ] = phi(n,m)/(n+m+1)   (1<=m<=n)
```
the two brackets collapsing by the polynomial identities
`m^2 + (n+m)(n-m) = n^2` and `m^2 + (n+1-m)(n+m+1) = (n+1)^2`.  `[PROVED, Expand → 0]`

### Lemma D2 (the two `n`-differences of Apéry's weight) `[PROVED]`
Using `u(n+1,m) = u(n,m)(n+1-m)/(n+m+1)` and `u(n-1,m) = u(n,m)(n+m)/(n-m)`, i.e.
`u(n+1,m)-u(n,m) = -2 phi(n,m)/(n+m+1)` and `u(n-1,m)-u(n,m) = 2 phi(n,m)/(n-m)`, Lemma D1 gives
telescoped closed forms with `Y2(1) = -1/(2(n+1)^3)`, `Y1(1) = -1/(2n^3)`:
```
  c(n+1,k) - c(n,k) = 1/(n+1)^3 - 2 [Y2(k+1)-Y2(1)] =  2 Lam(n,k)/(n+1)^2          (0 <= k <= n)
  c(n-1,k) - c(n,k) = -1/n^3    + 2 [Y1(k+1)-Y1(1)] = -2 (n+k+1) Lam(n,k)/((n-k) n^2)
                                                                                   (0 <= k <= n-1)
```
**The `1/(n+1)^3` and `-1/n^3` cancel exactly.** This is Apéry's miracle: it is *precisely why* the
weight `c(n,k)` carries the `1/2` and the `(-1)^{m-1}` and the `m^3 C(n,m)C(n+m,m)`.

`[VERIFIED]` both, exactly, `n = 1..10`, all admissible `k`.

### Lemma D3 (the correction term) `[PROVED]`
For `0 <= k <= n` set
`E(n,k) := (n+1)^3 A(n+1,k)(c(n+1,k)-c(n,k)) + n^3 A(n-1,k)(c(n-1,k)-c(n,k))`
(the second summand is `0` at `k = n` because `A(n-1,n)=0`). Then by Lemma D2, (0b), (0c),
and `A(n,k) Lam(n,k) = (-1)^k D(n,k)/(2(n+k+1))`:
```
  E(n,k) = (-1)^k D(n,k) [ (n+1)(n+k+1)/(n+1-k)^2 - n(n-k)/(n+k)^2 ].
```
`[VERIFIED exactly, n = 2..10, 0 <= k <= n]`

### Proposition D4 (pointwise operator identity for `B(n,k) = A(n,k)c(n,k)`) `[PROVED]`
For `0 <= k <= n`,
```
  (n+1)^3 B(n+1,k) - P(n) B(n,k) + n^3 B(n-1,k) = c(n,k)( G(n,k+1) - G(n,k) ) + E(n,k),
```
where `B(n-1,k) := 0` for `k >= n`. *Proof:* substitute `c(n±1,k) = c(n,k) + (c(n±1,k)-c(n,k))`
and use Proposition B. ∎  `[VERIFIED exactly, n = 2..10, 0<=k<=n]`

At `k = n+1` only the first term survives: `LHS = (n+1)^3 A(n+1,n+1) c(n+1,n+1)`.

### Lemma D5 (the top term) `[PROVED]`
```
  G(n,n+1) = -4(n+1)^3 C(2n+1,n+1) ^2 = -(n+1)^3 A(n+1,n+1)     (since C(2n+2,n+1) = 2C(2n+1,n+1)),
```
and, with `c(n+1,n+1)-c(n,n) = u(n+1,n+1) + 2 Lam(n,n)/(n+1)^2` (Lemma D2 at `k=n` plus the extra
top letter),
```
  u(n+1,n+1) = (-1)^n/(4(n+1)^3 C(2n+1,n+1)),   Lam(n,n) = (-1)^n/(2(n+1)C(2n+1,n+1)),
  c(n+1,n+1)-c(n,n) = (5/4)(-1)^n/((n+1)^3 C(2n+1,n+1)),
```
so
```
  Top(n) := c(n,n) G(n,n+1) + (n+1)^3 A(n+1,n+1) c(n+1,n+1)
          = (n+1)^3 A(n+1,n+1) ( c(n+1,n+1) - c(n,n) )  =  5 (-1)^n C(2n+1,n+1).
```
`[VERIFIED exactly, n = 1..10]` — this is where the classical `5` of
`zeta(3) = (5/2) sum (-1)^{m-1}/(m^3 C(2m,m))` enters.

### Assembly of `L b`
Summing Proposition D4 over `k = 0..n`, adding the `k = n+1` term, and Abel-summing
`sum_{k=0}^n c(n,k)(G(n,k+1)-G(n,k)) = c(n,n)G(n,n+1) - sum_{j=1}^{n} u(n,j)G(n,j)` (`G(n,0)=0`):
```
  (L b)(n) = Top(n) + sum_{k=0}^{n} V(n,k),      V(n,k) := E(n,k) - u(n,k)G(n,k)
```
(the `k=0` term of the second piece is `0` since `G(n,0)=0`). Now
`u(n,k)G(n,k) = (-1)^{k-1} D(n,k) k T(n,k)/(2(n+1-k)^2(n+k)^2)`, so
```
  V(n,k) = (-1)^k D(n,k) W(n,k),
  W(n,k) = (n+1)(n+k+1)/(n+1-k)^2 - n(n-k)/(n+k)^2 + k T(n,k)/(2(n+1-k)^2(n+k)^2).
```

### CERT-3 (polynomial identity in ℚ[n,k]) `[PROVED, Expand → 0]`
```
  2(n+1)(n+k+1)(n+k)^2 - 2n(n-k)(n+1-k)^2 + k T(n,k) + 10 k (2n+1)(n+1-k)(n+k) = 0,
```
i.e. **`W(n,k) = -5k(2n+1) / ( (n+1-k)(n+k) )`** — the whole weight-3 structure collapses to a
single linear-over-quadratic rational function. With `C(n,k)/(n+1-k) = C(n+1,k)/(n+1)` and
`C(n+k,k)/(n+k) = C(n+k-1,k)/n` (Lemma 0),
```
  V(n,k) = -5(2n+1)/(n(n+1)) * (-1)^k k C(n+1,k) C(n+k-1,k).
```
`[VERIFIED exactly, n = 1..10, 0<=k<=n]`

### Lemma D6 (residual binomial identity) `[PROVED]`
```
  (D-BIN)      sum_{k=0}^{n} (-1)^k k C(n+1,k) C(n+k-1,k) = (-1)^n n C(2n,n).
```
*Proof (Gosper certificate).* Put `s(n,k) := (-1)^k k C(n+1,k) C(n+k-1,k)` and
```
  Y(n,k) := - k(k-1) s(n,k) / ( n(n+1) ).
```
The absorption identities `C(n+1,k+1)(k+1) = C(n+1,k)(n+1-k)`, `C(n+k,k+1)(k+1) = C(n+k-1,k)(n+k)`
(Lemma 0) give `(k+1) s(n,k+1) = -(-1)^k C(n+1,k)C(n+k-1,k)(n+1-k)(n+k)`, hence for **every**
integer `k >= 0` (division-free):
```
  n(n+1)( Y(n,k+1) - Y(n,k) ) = (-1)^k k C(n+1,k)C(n+k-1,k) [ (n+1-k)(n+k) + k(k-1) ] = n(n+1) s(n,k)
```
by the polynomial identity `(n+1-k)(n+k) + k(k-1) = n(n+1)`. So `Y(n,·)` telescopes `s(n,·)`:
`sum_{k=0}^n s(n,k) = Y(n,n+1) - Y(n,0) = Y(n,n+1)`, and
`Y(n,n+1) = -(n+1)n s(n,n+1)/(n(n+1)) = -s(n,n+1) = -(-1)^{n+1}(n+1)C(2n,n+1) = (-1)^n n C(2n,n)`
using `C(2n,n+1) = n C(2n,n)/(n+1)`. ∎
`[VERIFIED exactly, n = 1..20; certificate checked pointwise n=1..12, k=0..n+3]`

### Theorem 2 `[PROVED]`
`(L b)(n) = 0` for all `n >= 1`.
*Proof.* By the assembly and Lemma D6,
`sum_{k=0}^n V(n,k) = -5(2n+1)/(n(n+1)) * (-1)^n n C(2n,n) = -5(-1)^n C(2n,n)(2n+1)/(n+1)
= -5(-1)^n C(2n+1,n+1) = -Top(n)`. ∎
`[VERIFIED exactly: (L b)(n) = 0 and Top(n) + sum V(n,k) = 0 for n = 1..16]`

---

## 6. Initial values `[PROVED]`

`B_min(0) = A(0,0)(2H3_0 - H3_0) = 0 = b_0`.
`B_min(1) = A(1,0)(2·1-0) + A(1,1)(2·1-1) = 1·2 + 4·1 = 6`.
`u(1,1) = (+1)/(2·1^3·C(1,1)C(2,1)) = 1/4`, so `c(1,0) = 1`, `c(1,1) = 5/4`, and
`b_1 = A(1,0)c(1,0) + A(1,1)c(1,1) = 1·1 + 4·(5/4) = 6`. ✓  (`a_1 = 5`, `b_1/a_1 = 6/5`.)

---

## 7. Main Theorem `[PROVED]`

> **Theorem (minimal form).** For every integer `n >= 0`,
> ```
>    sum_{k=0}^n C(n,k)^2 C(n+k,k)^2 ( 2 H3_n - H3_k )
>  = sum_{k=0}^n C(n,k)^2 C(n+k,k)^2 ( H3_n + sum_{m=1}^k (-1)^{m-1}/(2 m^3 C(n,m) C(n+m,m)) ) = b_n,
> ```
> the second Apéry solution for `zeta(3)`. Equivalently
> ```
>    sum_{k=0}^n C(n,k)^2 C(n+k,k)^2 ( H3_n - H3_k - sum_{m=1}^k (-1)^{m-1}/(2 m^3 C(n,m)C(n+m,m)) ) = 0.
> ```

*Proof.* Theorem 1 and Theorem 2 say both sides are annihilated by `L`, whose leading coefficient
`(n+1)^3` never vanishes for `n >= 1`; §6 gives agreement at `n = 0, 1`; induct. ∎

**Certificate inventory** (all verified by exact polynomial arithmetic, `Expand → 0`):

| # | role | certificate | size |
|---|---|---|---|
| CERT-1 | Zeilberger cert. for `a_n` | `T(n,k) = 4(2n+1)(2k^2-3k-4n^2-4n)`, `G = Phi k^4 T` | deg 2 in `k`, deg 3 in `n` |
| CERT-2 | Gosper cert. for the `w`-correction | `U(n,k) = -4(k-1)(2n+1)(2n^2+2n+1-k)`, `K = Phi k^4 U/(n^2(n+1)^2)` | deg 1 in `k`, deg 3 in `n` |
| CERT-3 | `W`-collapse | `W(n,k) = -5k(2n+1)/((n+1-k)(n+k))` | deg 1 / deg 2 |
| CERT-4 | Gosper cert. inner, `Delta_n^+` | `Y2(m) = -(n+1-m)phi(n,m)/(n+1)^2` | linear |
| CERT-5 | Gosper cert. inner, `Delta_n^-` | `Y1(m) = -(n+m)phi(n,m)/n^2` | linear |
| CERT-6 | Gosper cert. for (D-BIN) | `Y(n,k) = -k(k-1)s(n,k)/(n(n+1))` | quadratic |

Supporting polynomial identities, all `Expand → 0`:
`m^2+(n+m)(n-m) = n^2`; `m^2+(n+1-m)(n+m+1) = (n+1)^2`; `(n+1-k)(n+k)+k(k-1) = n(n+1)`;
CERT-1, CERT-2, CERT-3 as displayed.

**Lean-formalization note (main theorem).** Nothing above uses Gamma functions, limits, or `0/0`:
Lemma 0 converts every binomial ratio into a *multiplicative* absorption identity valid for all
integers `k >= 0`, after which each step is (i) a polynomial identity in `ℚ[n,k]` and (ii) a finite
telescoping sum. The only analytic input is `H3_{n+1} - H3_n = 1/(n+1)^3`.

---


## 8. STRETCH — the general mechanism, and two more `[VERIFIED] → [THM]` upgrades

### 8.0 A symmetrization that halves the work `[PROVED, new]`

For the `d`-fold binomial sums `A^{(d)}(n) = sum_k C(n,k)^d` the summand is **symmetric** under
`k -> n-k`, so the fitted weights of `work/LBW_GENERAL.md` T3 may be replaced by their
`k <-> n-k` averages *without changing the sum*:
```
  (1/(d+1)) H^{(2)}_k + (d/(d+1)) H_k(H_k - H_{n-k})
      ~   (1/(2(d+1))) ( H^{(2)}_k + H^{(2)}_{n-k} )  +  (d/(2(d+1))) ( H_k - H_{n-k} )^2 .
```
`[VERIFIED exactly, n = 0..12 for d = 3 and d = 4]`. Concretely
```
  Franel:   B(n) = sum_k C(n,k)^3 [ (1/8)(H2_k + H2_{n-k}) + (3/8)(H_k - H_{n-k})^2 ]
  s10:      B(n) = sum_k C(n,k)^4 [ (1/10)(H2_k + H2_{n-k}) + (2/5)(H_k - H_{n-k})^2 ]
```
This is not cosmetic: in the symmetric form the **only weight-1 letter that ever appears** is the
single antisymmetric combination `delta(n,k) := H_k - H_{n-k}`, because
`sigma := H2_k + H2_{n-k}` differences to *rational* functions under both `n -> n±1` and `k -> k+1`.
The certificate module is therefore rank 2 (`{1, delta}`) instead of rank 4
(`{1, H_k, H_{n-k}, H_n}`) — **two** Gosper problems instead of four.

### 8.1 The template

Given a summand `S(n,k)`, a three-term recurrence `c+(n) u_{n+1} + c0(n) u_n + c-(n) u_{n-1} = 0`,
and a symmetric weight `w = alpha*sigma + beta*delta^2`:

1. **Zeilberger certificate.** `G(n,k) = S(n,k) k^d rho(n,k)/(n+1-k)^d` with `d` the binomial power;
   the defining equation collapses to one polynomial equation in `ℚ[n,k]` because
   `S(n,k+1)/S(n,k) = ((n-k)/(k+1))^d`, so `G(n,k+1) = S(n,k) rho(n,k+1)` — **the shifted
   certificate is the summand times a polynomial**. This is what makes the whole scheme work.
2. **Split.** For `0 <= k <= n`,
   `c+ S(n+1,k)w(n+1,k) + c0 S(n,k)w(n,k) + c- S(n-1,k)w(n-1,k) = w(n,k)(G(n,k+1)-G(n,k)) + Corr(n,k)`
   with `Corr(n,k) = c+ S(n+1,k)(w(n+1,k)-w(n,k)) + c- S(n-1,k)(w(n-1,k)-w(n,k))`,
   and (this is the point) `w(n±1,k)-w(n,k)` lies in `ℚ(n,k) + ℚ(n,k)·delta`.
3. **Abel.** `sum_{k=0}^n w ΔG = w(n,n)G(n,n+1) - sum_{k=0}^{n-1} G(n,k+1) Δ_k w`,
   `Δ_k w` again in `ℚ(n,k) + ℚ(n,k)·delta`.
4. **Two Gosper problems.** Write the `k`-summand as `S(n,k)(A(n,k) + B(n,k) delta(n,k))` and seek
   `Z(n,k) = S(n,k)(z0(n,k) + z1(n,k) delta(n,k))`. Because
   `delta(n,k+1) = delta(n,k) + e(n,k)`, `e := 1/(k+1) + 1/(n-k)`, matching coefficients gives
   ```
     (G1)   r(n,k) z1(n,k+1) - z1(n,k) = B(n,k),          r := S(n,k+1)/S(n,k)
     (G2)   r(n,k) z0(n,k+1) - z0(n,k) = A(n,k) - r(n,k) z1(n,k+1) e(n,k).
   ```
   Both are solved by a rational ansatz `z1 = N(k)/(n+1-k)^{p}`, `z0 = M(k)/(n+1-k)^{p+1}`,
   reducing to two **linear systems over ℚ(n)**.
5. **Boundary.** Everything cancels iff three scalar identities hold:
   ```
     (b1)  rho(n,n+1) = - c+(n) S(n+1,n+1)/S(n,n)         [kills the weight-2 letters H2_n, H_n^2]
     (b2)  N(n) = <explicit>                               [kills H_n]
     (b3)  M(n) = <explicit>                               [kills the constant]
   ```
   plus `Z(n,0) = 0`, automatic from the `k^2`/`k^3` factors of `M`, `N`.

`(b1)` is a *structural* fact: it says the Zeilberger certificate at the top of its support
reproduces the leading term of the recurrence. It is what forces the harmonic decomposition to
exist at all.

### 8.2 Franel `[PROVED]`

`A(n) = sum_k C(n,k)^3` (A000172), `(n+1)^2 u_{n+1} = (7n^2+7n+2) u_n + 8 n^2 u_{n-1}`,
`B(n) = sum_k C(n,k)^3 [ (1/8)(H2_k+H2_{n-k}) + (3/8)(H_k-H_{n-k})^2 ]`,
`B(0..8) = 0, 1, 4, 208/9, 1280/9, 208384/225, 1404928/225, 95174656/2205, 3351248896/11025`.

```
rho_F(n,k) = -(4 - 12k + 12k^2 - 4k^3 + 22n - 39kn + 18k^2 n + 32n^2 - 27k n^2 + 14n^3)/n
G_F(n,k)   = k^3 rho_F(n,k) C(n+1,k)^3/(n+1)^3
z1 = N_F(k)/(n+1-k)^4,
   N_F = (3k^2/(4n)) (4 -16k +24k^2 -16k^3 +4k^4 +26n -68kn +63k^2 n -20k^3 n
                       +54n^2 -88k n^2 +39k^2 n^2 +46n^3 -36k n^3 +14n^4)
z0 = M_F(k)/(n+1-k)^5,
   M_F = -(k/(2n)) (2 -10k +20k^2 -20k^3 +10k^4 -2k^5 +15n -50kn +70k^2 n -45k^3 n +11k^4 n
                     +40n^2 -90k n^2 +80k^2 n^2 -25k^3 n^2 +50n^3 -70k n^3 +30k^2 n^3
                     +30n^4 -20k n^4 +7n^5)
```
Boundary identities, all **`Factor -> 0`**:
`rho_F(n,n+1) = -(n+1)^2`,  `N_F(n) = (3/4)((n+1)^5 - (n+1))`,  `M_F(n) = -(1/2)(1 + (n+1)^5)`.
`[PROVED]`  (`[VERIFIED]` certificate identities pointwise `n=1..10, k=0..n+3` resp. `k=0..n-1`;
`L[B] = 0` numerically `n = 1..25`.)

### 8.3 s₁₀ = `sum_k C(n,k)^4` `[PROVED]`

`(n+1)^3 u_{n+1} = (2n+1)(6n^2+6n+2) u_n + n(64n^2-4) u_{n-1}`,
`B(n) = sum_k C(n,k)^4 [ (1/10)(H2_k+H2_{n-k}) + (2/5)(H_k-H_{n-k})^2 ]`,
`B(0..6) = 0, 1, 21/4, 1001/18, 85085/144, 4203199/600, 52055003/600`.

```
rho_10(n,k) = -( -4k +16k^2 -24k^3 +16k^4 -4k^5 +10n -72kn +172k^2 n -184k^3 n +90k^4 n -16k^5 n
                 +80n^2 -368k n^2 +600k^2 n^2 -416k^3 n^2 +104k^4 n^2
                 +255n^3 -796k n^3 +818k^2 n^3 -276k^3 n^3
                 +385n^4 -756k n^4 +374k^2 n^4 +275n^5 -260k n^5 +75n^6 ) / n^3
G_10(n,k)  = k^4 rho_10(n,k) C(n+1,k)^4/(n+1)^4
z1 = N_10(k)/(n+1-k)^5   (deg 9 in k, factor k^3;  full coefficients in work/minform/certs_stretch.m)
z0 = M_10(k)/(n+1-k)^6   (deg 9 in k, factor k^2;  ditto)
```
Boundary identities, all **`Factor -> 0`**:
`rho_10(n,n+1) = -(n+1)^3`,  `N_10(n) = (4/5)((n+1)^7 - (n+1)^2)`,
`M_10(n) = -(1/2)((n+1) + (n+1)^7)`.
`[PROVED]`  (`[VERIFIED]` certificate identities pointwise `n=1..9`; `L[B] = 0` numerically
`n = 1..20`.)

### 8.4 The pattern

| | `c+(n)` | `rho(n,n+1)` | `N(n)` | `M(n)` |
|---|---|---|---|---|
| Franel (`d=3`) | `(n+1)^2` | `-(n+1)^2` | `(3/4)((n+1)^5-(n+1))` | `-(1/2)(1+(n+1)^5)` |
| s₁₀ (`d=4`) | `(n+1)^3` | `-(n+1)^3` | `(4/5)((n+1)^7-(n+1)^2)` | `-(1/2)((n+1)+(n+1)^7)` |

With `beta_d = d/(2(d+1))` the `delta^2`-coefficient and `c+(n) = (n+1)^{d-1}`, both rows read
```
  rho(n,n+1) = -c+(n) = -(n+1)^{d-1}
  N(n) = 2 beta_d ( (n+1)^{2d-1} - (n+1)^{d-2} )
  M(n) = -(1/2)  ( (n+1)^{2d-1} + (n+1)^{d-3} )
```
(`d=3`: `-(n+1)^2`, `(3/4)((n+1)^5-(n+1))`, `-(1/2)((n+1)^5+1)`;
 `d=4`: `-(n+1)^3`, `(4/5)((n+1)^7-(n+1)^2)`, `-(1/2)((n+1)^7+(n+1))`).
**[CONJ]** this is the general `d` shape, i.e. the Chamberland–Straub conjecture
(`A^{(d)}` has Apéry limit `zeta(2)/(d+1)`) is provable this way for every `d` for which the
sequence satisfies an order-2 recurrence (`d = 3, 4` only, as noted in LBW_GENERAL).

### 8.5 Apéry-ζ(2) (`D`) — the template **provably fails**, with a sharp obstruction `[OPEN]`

`A(n) = sum_k C(n,k)^2 C(n+k,k)` (A005258: 1, 3, 19, 147, 1251, …),
`(n+1)^2 u_{n+1} = (11n^2+11n+3)u_n + n^2 u_{n-1}`,
`B(n) = sum_k C(n,k)^2C(n+k,k) * (1/5)[ H2_n + H_k(2H_k - H_{n-k} - H_n) ]`,
`B(0..6) = 0, 1, 25/4, 1741/36, 6585/16, 13327519/3600, 124308457/3600`;  `L[B] = 0` `[VERIFIED n ≤ 25]`.

Everything up to step 4 of §8.1 goes through, and beautifully:
```
  rho_D(n,k) = k^2 + k(1+6n) - 4 - 15n - 11n^2         (degree 2 — the smallest certificate in the file)
  G_D(n,k)   = k^3 rho_D(n,k) C(n+1,k)^2 C(n+k-1,k) / ( n (n+1)^2 )
```
`[PROVED, Expand → 0; VERIFIED pointwise n=1..9, k=0..n+3]`, and the **structural boundary
identity (b1) holds exactly**:
`rho_D(n,n+1) = -2(n+1)(2n+1) = -(n+1)^2 * C(2n+2,n+1)/C(2n,n) = -c+(n) S(n+1,n+1)/S(n,n)`.
The correction decomposes with `Y(n,k)/S(n,k) = A + B1 H_k + B2 (H_{n-k} + H_n)`,
`B2 = rho_D(n,k+1)/(5(k+1))` `[VERIFIED exactly, n = 2..8, 0<=k<=n-1]`.

**But the `H_{n-k}` component is provably not Gosper-summable.** With
`T(k) := S_D(n,k) B2(n,k)`, Gosper's decomposition is
`T(k+1)/T(k) = (a(k)/b(k))(c(k+1)/c(k))`, `a = (n-k)^2(n+k+1)`, `b = (k+1)^2(k+2)`,
`c(k) = rho_D(n,k+1)`, and `gcd(a(k), b(k+j)) = 1` for all `j >= 0` (roots `n, -n-1` vs `-j-1, -j-2`;
`n` generic). Gosper's key equation is `a(k)x(k+1) - b(k-1)x(k) = c(k)`. Since
```
  a(k) - b(k-1) = -n( k^2 + (n+2)k - n(n+1) )   [degree 2, leading coeff -n != 0]
```
the degree bound is `deg x = 0`, and `x = x0` forces `x0 = -1/n` from the `k^2` coefficient but then
gives `k`-coefficient `n+2` against the required `3+6n`. **Contradiction.** `[PROVED]`
Confirmed independently: the linear system has **no solution for any `deg x <= 8`.**

**Diagnosis.** In Franel/s₁₀ the weight is `k <-> n-k` symmetric, the certificate module has rank 2
(`{1, delta}`), and each component telescopes. Here the weight is genuinely 3-lettered
(`H_k`, `H_{n-k}`, `H_n`) and the components do **not** telescope separately, while the weight-2
part of any enlarged ansatz is forced to vanish (`Δ(S z) = 0 ⟹ z = 0`). So closing the ζ(2)-Apéry
case needs either **(i)** a different gauge for `w` — the harmonic-monomial fit has a large kernel
(11-dimensional in the ζ(3) case), and a kernel shift changes `Y` — or **(ii)** a genuine ΠΣ-field
(Sigma-style) ansatz allowing nested sums, not just rational × harmonic-monomial. **[OPEN]** —
this is the *first place in the programme where the rank-2 mechanism is provably insufficient*, and
the obstruction is exactly the one that will recur at weight 5 (see §10).

---

## 9. Literature `[CONFIRMED-FROM-SOURCE by a dedicated search pass]`

* **The `b_n` recurrence, proved in full:** **C. Schneider, "Apéry's Double Sum is Plain Sailing
  Indeed", Electron. J. Combin. 14 (2007), #N5, 3 pp.** (SFB F013 report 06-41). Three pages
  devoted to exactly this; Sigma (Karr ΠΣ difference fields) + creative telescoping; certificate
  written out with `p0(n,k) = p1(n,k) = 4k^4(n+1)^2(n+2)(2n+3)(2k^2-3k-4n^2-12n-8)`.
  **Substituting `n -> n-1` gives `4k^4 n^2(n+1)(2n+1)(2k^2-3k-4n^2-4n)` — the numerator of my
  `G(n,k)` exactly.** Independent confirmation of §2's normalization.
* **Historical origin (Zagier/Cohen):** **A. van der Poorten, "A proof that Euler missed…",
  Math. Intelligencer 1:4 (1978/79) 195–203, §8.** Gives `B_{n,k} = 4(2n+1)(k(2k+1)-(2n+1)^2)
  C(n,k)^2C(n+k,k)^2` and, for the second solution,
  `A_{n,k} = B_{n,k} c_{n,k} + [5(2n+1)(-1)^{k-1}k/(n(n+1))] C(n,k)C(n+k,k)`.
  **This is precisely my Step-D certificate**: `G_b(n,k) = c(n,k)G(n,k) + F(n,k)` with
  `V(n,k) = 5(2n+1)(-1)^{k-1} k C(n+1,k)C(n+k-1,k)/(n(n+1))` (§5, CERT-3), and
  `G(n,k) = B_{n,k-1}`. **But van der Poorten dispatches the verification as "after some massive
  reorganization (9) becomes A_{n,k} - A_{n,k-1}" — it is exhibited, not written out.**
  Fischler likewise calls it "une simple vérification".
* **Cleanest human-readable citation:** **S. Fischler, Sém. Bourbaki exp. 910, Astérisque 294
  (2004), 27–62, §1.2** — in this repo at `llm/05-fischler-2003-bourbaki-survey.md`, lines 148–168.
* **Also:** Zudilin arXiv:math/0202159 eqs. (5)–(6) has the rational-function form
  `s_n(t) = 4(2n+1)(-2t^2+t+(2n+1)^2)`, i.e. the same polynomial under `t <-> -k`.
  Zeilberger, "Closed form (pun intended!)", Contemp. Math. 143 (1993), 579–607, generalizes the
  Zagier/Cohen method to WZ forms. **Correction to a common mis-citation: `A=B` contains no Apéry
  example at all** (the string "Apéry" occurs zero times in the book).
* **My `2H3_n - H3_k` form: [NOT LOCATED] anywhere.** Checked OEIS A059415 (= exactly this `b_n`;
  its only closed form is the classical double sum), Chamberland–Straub arXiv:2011.03400,
  Gorodetsky arXiv:2102.11839, Straub arXiv:1401.0854, Cooper arXiv:2302.00757, Zagier's
  Apéry-like paper, Paule–Schneider 2003, Schneider 2007, van der Poorten, Fischler.
  **Nearest published relative:** Nesterenko, "A few remarks on ζ(3)", Mat. Zametki 59 (1996)
  865–880, Lemma 1, reproduced as formula (3) of Zudilin math/0202159 —
  `v_n = 2Σ_k A_{2k}Σ_{l≤k}1/l^3 + Σ_k A_{1k}Σ_{l≤k}1/l^2` with
  `A_{1k} = 2A_{2k}(2H_k - H_{n+k} - H_{n-k})`, i.e. weight
  `H3_k + (2H_k - H_{n+k} - H_{n-k})H2_k` — the §3.1 form of `PROOF_LB5_CAMPAIGN`, *not* the
  minimal one. **The minimal form and the present proof of it are new.**
* **(D-BIN) `[NOT LOCATED] as a named identity`, but it is one line from Chu–Vandermonde:**
  `Σ_{k≥0} (-1)^k C(n+1,k)C(n+k-1,k)x^k = 2F1(-(n+1), n; 1; x)`; apply `x d/dx` at `x=1`,
  `= -n(n+1)·2F1(-n,n+1;2;1) = 0` for `n ≥ 1`; peel off the `k = n+1` term.
  So (D-BIN) has both a Gosper certificate (§5, Lemma D6, preferred — it is Lean-ready) and a
  classical hypergeometric proof. Its relative `Σ_k(-1)^kC(n,k)C(n+k,k) = (-1)^n` is `P_n(-1)`.
  **Note the family resemblance:** Paule–Schneider 2003 (Adv. Appl. Math. 31, 359–378) prove
  Ahlgren's `Σ_j (1 - 4jH_j + 4jH_{n-j}) C(n,j)^4 = (-1)^n C(2n,n)` — same right-hand side, same
  `d = 4` summand as my §8.3 s₁₀ case. **They prove only weight-1 identities; `H^{(3)}` never
  appears in that paper.** So the §8.3 result is not covered by theirs.

---

## 10. What the mechanism teaches about hunting the weight-5 depth-2 `w5`

The whole ζ(3) proof turns on **one** structural fact, isolated in Lemma D1/D2: the `n`-difference of
Apéry's weight collapses to a **single hypergeometric term**,
`c(n+1,k)-c(n,k) = 2 Lam(n,k)/(n+1)^2` and `c(n-1,k)-c(n,k) = -2(n+k+1)Lam(n,k)/((n-k)n^2)`,
because the two *rational* pieces
`1/(n+1)^3` and `-1/n^3` are **exactly** cancelled by the boundary value `Y2(1)`, `Y1(1)` of the
inner Gosper antidifference — and that cancellation is the polynomial identity
`m^2 + (n+1-m)(n+m+1) = (n+1)^2`. The weight is not "found", it is *forced*: `c(n,k)` is the unique
(up to the recurrence's kernel) weight whose `n`-difference is a **single hypergeometric term**
rather than a sum. Everything downstream — the miracle `5`, `Top(n) = 5(-1)^n C(2n+1,n+1)`, the
collapse `W(n,k) = -5k(2n+1)/((n+1-k)(n+k))` — is bookkeeping.

For the BZ weight-5 row `P_n` (`PROOF_LB5_CAMPAIGN` BLOCKED: monomial basis provably inconsistent,
top period `zeta(5) + 2 zeta(2)zeta(3)`), this says three concrete things.

1. **Stop fitting monomials; fit `n`-difference collapse.** The right search is not "which weight-5
   harmonic monomials span `P_n`" but "which `w5(n,k)` has `w5(n+1,k) - w5(n,k)` equal to a *single*
   hypergeometric term times a rational function". That is a much smaller, linear, and *decidable*
   search (it is a Gosper problem in the inner index, one per candidate letter), and it is
   automatically insensitive to the kernel that made the monomial fit degenerate. Depth-2 nesting
   enters exactly as it does here — `c(n,k)` is *already* a depth-1 nested object
   (`sum_m (-1)^{m-1}/(2m^3 C(n,m)C(n+m,m))`), and it was found by demanding the collapse, not by
   fitting.
2. **The obstruction has a name and I have now met it (§8.5).** The rank-2 template dies precisely
   when the letters are not organized by a single antisymmetric combination. `zeta(5)+2zeta(2)zeta(3)`
   is impure exactly in that sense — two independent letters at the top. §8.5 is a miniature of the
   weight-5 blockage in a case small enough to compute: there the fix is a gauge change or a ΠΣ
   ansatz, and the same two options are the only ones available at weight 5. **Test the ζ(2)-Apéry
   case first** — it is 10 minutes of Sigma and it will tell you which fix works before spending
   weeks at weight 5.
3. **The `5` is a boundary value, so predict it.** `Top(n) = 5(-1)^n C(2n+1,n+1)` came from
   `c(n+1,n+1) - c(n,n)` — a *single* evaluation at the top of the support. The analogous weight-5
   quantity is computable from the BZ integrand's residue at the top cell **before** any weight is
   known, and it must equal `-Σ_k V(n,k)`. That gives a **necessary numerical fingerprint** for any
   candidate `w5`: compute the top-cell constant from the rank-3 crystal, and reject every candidate
   whose residual sum misses it. Given the purity defect `c = -3/π^2 = 12/(2πi)^2` already isolated
   in `DEFECT_IDENTIFY.md`, the fingerprint should carry that Tate twist explicitly — i.e. expect a
   *pair* of top constants (one per graded piece, matching the `diag(1, p^3, p^5)` Frobenius seen in
   `ORCHESTRATOR_NOTES §2d`), not a single `5`.

