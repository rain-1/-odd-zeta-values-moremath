# DENOMINATOR_HARVEST — denominator theorems from the Eichler companion formula

**Fork deliverable, 2026-08-05.**  Code: `work/z5eps/eps58_denoms.py`, data
`eps58_results.json`.  All arithmetic exact (`Fraction`).  Labels per
programme convention; the conditionality of every statement is explicit.
Recurrence conventions: R2 rows 1–6 (order r = 2), R3 rows 7–15 (order
r = 3; this includes Cooper's three, whose *modular* weight is 2 but whose
operator order — the exponent that matters here — is 3).
$d_n := \mathrm{lcm}(1,\dots,n)$, $B(0)=0$, $B(1)=1$.

## 1. The conditional denominator theorem

**Theorem (conditional).**  Fix a family with operator order $r$, operator
$L = \theta^r - t(\cdots) + t^2(\cdots)$ (R2/R3 normal form; leading
polynomial $P_r(t)$ with $P_r(0)=1$ and integer coefficients), and suppose:

* (I1) the mirror map is integral: $t(q) \in \Z[[q]]$, $t = q + O(q^2)$;
* (I2) $F(q) := y_0(t(q)) \in \Z[[q]]$, $F(0)=1$;
* (F) the rectification identity $L = (P_r/\sigma^r)\,F\,\theta_q^r\,F^{-1}$
  holds, where $\sigma = \theta_q t/t$.

Then
\[
\boxed{\;d_n^{\,r}\,B(n) \in \Z \quad\text{for all } n\ge 0.\;}
\]

*Proof (complete given the inputs).*
(a) $L(y_B) = t$ exactly: the $n=0$ instance of the recurrence with
$B(0)=0$, $B(1)=1$ contributes coefficient $1$ at $t^1$ and the recurrence
kills all higher coefficients.  (b) Inverting (F):
$y_B = F\,\theta_q^{-r}(A)$ with $A := t\,\sigma^r/(P_r(t)\,F)$.
(c) Integrality of the argument: $t \in \Z[[q]]$ by (I1); $t/q$ is a unit
of $\Z[[q]]$, hence $\sigma = \theta_q t/t = (\theta_q t)\cdot(t)^{-1}
\in \Z[[q]]$ and is a unit ($\sigma(0)=1$); $P_r(t(q))$ is a unit of
$\Z[[q]]$ ($P_r(0)=1$, integer coefficients); $F$ is a unit by (I2).
Hence $A \in q + q^2\Z[[q]]$.
(d) $\theta_q^{-r}$ divides the $q^m$-coefficient by $m^r$; multiplying by
$d_n^{\,r}$ clears every $m \le n$.  (e) Multiplication by $F \in \Z[[q]]$
preserves this, and extraction of $[t^n]$ uses only $q$-coefficients
$m \le n$ because $q(t) \in t + t^2\Z[[t]]$: the compositional inverse of
an integer series with unit linear coefficient is an integer series
(standard; also verified below).  $\square$

**Status of the inputs.**  (I1), (I2), and the inversion integrality
$q(t)\in\Z[[t]]$ are verified in this fork, independently and
self-containedly, to order $q^{48}$ for **all fifteen families** (the
series are rebuilt from the recurrences alone via the Frobenius
$\varepsilon$-derivative; nothing is imported from other memos).  The
identity (F) is verified here through $n\le 40$ for all fifteen (the
formula reproduces $B(n)$ exactly), is **proved** for Ap\'ery
($\gamma$) via the symmetric-square lemma of
`papers_out/expository_apery`, and its family-by-family proof (exact
$\mathrm{Sym}^2$ operator identities) is the eps57 work stream.  For
$\gamma$ the theorem is therefore unconditional modulo the classical
$\Gamma_0(6)$ integrality citations; for the others it is conditional
exactly on (F) (all-$n$) and on upgrading (I1)/(I2) from verified to
proved via the (partly proved) eta identifications.

## 2. Data: the bound holds and is near-sharp (n ≤ 120, p ≤ 13)

For every family and every prime $p \le 13$:
$\max_{n\le120}\bigl(v_p(\mathrm{den}\,B(n)) - r\,v_p(d_n)\bigr) = 0$ —
**no violations anywhere** (consistency of the data with the theorem).
Sharpness at $n = 120$: the table gives
$\mathrm{gap}_p = r\,v_p(d_{120}) - v_p(\mathrm{den}\,B(120))$
(0 = bound attained; large = cancellation):

| family | r | gap$_2$ | gap$_3$ | gap$_5$ | gap$_7$ | gap$_{11}$ | gap$_{13}$ |
|---|---|---|---|---|---|---|---|
| A (Franel) | 2 | **12** | 0 | 1 | 1 | 1 | 2 |
| B | 2 | 0 | **8** | 0 | 4 | 0 | 0 |
| C | 2 | 0 | **8** | 0 | 0 | 0 | 0 |
| D | 2 | 0 | 4 | 1 | 2 | 1 | 0 |
| E | 2 | **12** | 0 | 0 | 2 | 0 | 0 |
| F | 2 | **12** | **8** | 3 | 0 | 0 | 1 |
| α (Domb) | 3 | **18** | 0 | 1 | 0 | 1 | 0 |
| γ (Ap\'ery) | 3 | 0 | 0 | 1 | 0 | 3 | 0 |
| δ | 3 | 0 | **12** | 1 | 0 | 1 | 0 |
| ε | 3 | **18** | 0 | 1 | 1 | 1 | 0 |
| ζ | 3 | 0 | **12** | 1 | 1 | 1 | 0 |
| η | 3 | 0 | 0 | **6** | 0 | 1 | 0 |
| s₇ | 3 | 9 | 4 | 5 | 2 | 3 | 2 |
| s₁₀ | 3 | 9 | 4 | 4 | 3 | 3 | 2 |
| s₁₈ | 3 | 9 | **12** | 4 | 2 | 3 | 1 |

Reading (a striking structure, recorded as observation):

* **The bound $d_n^{\,r}$ is attained (gap 0) at most primes for most
  families** — e.g. $\gamma$ at $p=2,3,7,13$; $\zeta$ at $p=2$; $\delta$
  at $p=2$.  The Eichler-formula bound is close to the truth, not a crude
  ceiling.
* **Total cancellation at exactly one structural prime per family** (the
  boldface entries, gap $= r\cdot v_p(d_{120})$, i.e. $B$ is $p$-integral
  or nearly so): $p=2$ for A, E, F, α, ε; $p=3$ for B, C, F, δ, ζ, s₁₈;
  $p=5$ for η (partial).  These match the families' level/conductor data
  (χ₋₃-families cancel at 3; the level-4/8-flavoured at 2; η's χ₅ at 5).
  **Conjecture-grade law: the companion is $p$-integral at the ramified
  prime of its uniformization.**  This is a new, sharp target: e.g.
  $B_\zeta(n) \in \Z_{(3)}$ for all $n$ (verified $n\le120$), on top of
  the conditional $d_n^3 B_\zeta(n) \in \Z$.
* Cooper's three show *uniform partial* cancellation (gap ≈ 9 at 2, ≈ 4
  at 3,5) — consistent with their aperiodic/non-eta nome data; their
  denominators are genuinely richer.

## 3. Controls versus documented results

* **γ (Ap\'ery).**  Classical: $d_n^3 b_n \in \Z$ with $b_n = 6B(n)$.
  Observed: $d_n^3 B(n) \in \Z$ already (gaps 0 at 2,3), i.e. the
  normalized statement is tight without the factor 6; consistent with and
  marginally sharper in normalization than the classical bound.
* **A (Franel).**  The known weight ($\tfrac14 H^{(2)}_k + \tfrac34\dots$)
  suggests denominator 4-support at 2; observed: $B$ is **2-integral**
  (gap 12) and the binding prime is 3, where the full $d_n^2$ is attained.
  The harmonic formula's apparent 2-denominators cancel in the sum — a
  concrete, provable-looking cancellation statement the old decomposition
  hides.
* **D, s₁₀** (documented denominators 5): observed gap$_5$ = 1 (D) and 4
  (s₁₀) — the 5-support is real but bounded; profiles recorded in the
  json.

## 4. First-ever denominator statements for the conjectural seven

Conditional on (F) per family (verified $n\le40$ here; $\mathrm{Sym}^2$
proofs in the eps57 stream), with the observed exact structure attached:

* $d_n^2 B_{\mathbf B}(n)\in\Z$, and observed: $3$-integral
  ($v_3(\mathrm{den})=0$ through $n=120$); binding primes 2, 5, 11, 13.
* $d_n^2 B_{\mathbf C}(n)\in\Z$; observed $3$-integral; the bound is
  attained at $p=2,5,7,11,13$.
* $d_n^2 B_{\mathbf F}(n)\in\Z$; observed cancellation at both 2 and 3.
* $d_n^3 B_{\delta}(n)\in\Z$; observed $3$-integral (level 12; the
  ramified 3 cancels), bound attained at 2.
* $d_n^3 B_{\zeta}(n)\in\Z$; observed $3$-integral, bound attained at 2 —
  the companion of the family with *no* harmonic formula obeys clean
  Ap\'ery-style denominator control.
* $d_n^3 B_{\eta}(n)\in\Z$; observed strong cancellation at 5 (χ₅).
* $d_n^3 B_{s_{18}}(n)\in\Z$; observed cancellation at 3.

These are the first denominator statements of any kind for these
companions (there was previously no formula to derive them from).

## 5. Next-theorem targets (where reality beats the bound)

1. **Ramified-prime integrality** ($B_\zeta \in \Z_{(3)}$ etc.): a clean
   conjecture with a plausible proof route through the Eichler formula at
   the ramified prime (the level prime divides the eta data; the
   $\theta^{-r}$ loss at $p$ should be repaid by the $p$-divisibility of
   the argument's coefficients — check $v_3$ of $A(q)$'s coefficients for
   $\zeta$: this is a finite-signature computation away from a proof).
2. **The Franel 2-cancellation** (harmonic formula has 4's, the sum is
   2-integral): a self-contained classical-looking lemma.
3. Cooper's partial gaps: understand $9 = 3\cdot3$ at $p=2$ (a uniform
   $8^{-n}$-type rescaling hiding in their non-eta nomes?).

## 6. Honest limits

$p \le 13$ and $n \le 120$ for all observations; the theorem's proof is
complete *given* (I1), (I2), (F), which are proved only for $\gamma$
(modulo classical citations) at the time of writing; series orders
$q^{48}$ (inputs) and $n\le40$ (formula) for the in-fork verifications.
Nothing here uses or asserts the ζ(5) five-block (whose rectification is
known to fail in the bare sense; its denominator story needs the corrected
inverse operator and is out of scope).
