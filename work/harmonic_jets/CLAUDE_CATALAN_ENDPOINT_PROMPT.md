# Overnight Claude prompt: formalize the Catalan endpoint breakthrough

Copy everything below this line into Claude Code.

---

You are working in:

    /home/ubuntu/fable-episode-2/zeta-math-2

Your task is to formalize, in Lean 4 + mathlib, the newly proved endpoint-transform and
sharp-denominator theorem for the normalized Catalan companion. Work autonomously for
the full session. Do not stop to ask about minor design choices: inspect the repository,
choose robust definitions, compile frequently, and keep going until the strongest honest
theorem below builds.

## Non-negotiable trust rules

- No sorry, admit, axiom, unsafe, fabricated certificates, or replacing a universal
  result by finite computation.
- native_decide/norm_num may check explicit small examples, but may not stand in for any
  theorem quantified over arbitrary n, j, or primes.
- Preserve all existing work. Do not rewrite or delete unrelated zeta(2), Franel,
  Brown--Zudilin, or Lucas files.
- Do not run lake update or change the toolchain/dependencies.
- A smaller fully proved theorem is preferable to a larger statement with a hidden
  assumption. Clearly document every trust boundary.
- Compile after each substantial lemma. End with lake build.

## Read these first

1. papers_out/harmonic_jets/main.tex, especially Theorem 6.9 and its proof, equations
   (43)--(48) near line 813, and Proposition 6.12.
2. work/harmonic_jets/LEAN_CATALAN_HANDOFF.md, especially Section 10 near line 611.
3. work/harmonic_jets/check_catalan_endpoint_transform.py.
4. work/harmonic_jets/verify_catalan_transport_symbolic.py.
5. work/harmonic_jets/verify_general_endpoint.py.
6. lean/ZetaLucas/BZFactor12.lean for the project's convention for rational
   integrality and its existing dlcm.
7. lean/ZetaLucas/Z2Shell.lean and lean/ZetaLucas/Z2Minimal.lean for style:
   recurrence-defined rational companions, exact algebra, and no-placeholder completion.

Run the two endpoint scripts before coding:

~~~bash
python3 work/harmonic_jets/check_catalan_endpoint_transform.py
python3 work/harmonic_jets/verify_catalan_transport_symbolic.py
python3 work/harmonic_jets/verify_general_endpoint.py
~~~

## Mathematical target

The normalized companion is the unique rational sequence B with

\[
B_0=0,\qquad B_1=1,
\]

\[
(n+1)^2B_{n+1}
=(12n^2+12n+4)B_n-32n^2B_{n-1}\qquad(n\ge1). \tag{REC}
\]

Define its endpoint binomial transform

\[
T_n=\sum_{k=0}^n\binom nk(-4)^{n-k}B_k. \tag{TDEF}
\]

The first main identity is

\[
(n+1)^2T_{n+1}-16n^2T_{n-1}=(-4)^n\qquad(n\ge0). \tag{TREC}
\]

At n=0 the term containing T_(n-1) is multiplied by zero. In Lean it is fine to use
truncated natural subtraction here, or state n=0 separately.

For 1 <= n, 0 <= j < n, and odd n-j, put

\[
q=\frac{n-j-1}{2},
\]

\[
R_{n,j}=2^{n-1}
\frac{\prod_{t=0}^{q-1}(j+2+2t)}
     {\prod_{t=0}^{q}(j+1+2t)}\in\mathbb Q. \tag{R}
\]

The empty numerator product is 1. Then

\[
(-1)^{n-1}T_n
=\sum_{\substack{0\le j<n\\n-j\ {\rm odd}}}R_{n,j}^2. \tag{TSQ}
\]

Let L_n=lcm(1,2,...,n), with L_0=1. The arithmetic kernel is

\[
L_nR_{n,j}\in\mathbb Z. \tag{RL}
\]

Consequently L_n^2 T_n is integral. Binomial inversion gives

\[
B_n=\sum_{k=0}^n\binom nk4^{n-k}T_k, \tag{INV}
\]

and therefore the primary target is

\[
\boxed{L_n^2B_n\in\mathbb Z\quad\text{for every }n.} \tag{SHARP}
\]

## Recommended module and definitions

Create lean/ZetaLucas/CatalanEndpoint.lean and add it to lean/ZetaLucas.lean only once
it builds.

Use Nat.lcmUpto from Mathlib.NumberTheory.Chebyshev if convenient. Mathlib already
contains Nat.factorization_lcmUpto, Nat.lcmUpto_ne_zero, Nat.lcmUpto_pos, and
Nat.lcmUpto_dvd_factorial. This is likely more useful for the universal proof than the
project-local dlcm. If you use Nat.lcmUpto, prove once that it has the intended meaning;
only prove equivalence with ZetaLucas.dlcm if a downstream statement needs it.

Suggested public API (rename if Lean conventions suggest better names):

~~~lean
namespace ZetaLucas

def catalanB : ℕ → ℚ := ...

theorem catalanB_zero : catalanB 0 = 0 := ...
theorem catalanB_one : catalanB 1 = 1 := ...
theorem catalanB_rec (n : ℕ) (hn : 1 ≤ n) : ... := ...

def catalanT (n : ℕ) : ℚ :=
  ∑ k ∈ Finset.range (n + 1),
    (n.choose k : ℚ) * (-4 : ℚ) ^ (n-k) * catalanB k

theorem catalanT_rec (n : ℕ) : ... := ...

def endpointQ (n j : ℕ) : ℕ := (n-j-1)/2
def endpointNum (n j : ℕ) : ℕ := ...
def endpointDen (n j : ℕ) : ℕ := ...
def endpointR (n j : ℕ) : ℚ :=
  (2 : ℚ)^(n-1) * endpointNum n j / endpointDen n j

theorem catalanT_square_formula
    (n : ℕ) (hn : 1 ≤ n) : ... := ...

theorem endpointR_lcm_integral
    {n j : ℕ} (hj : j < n) (hodd : Odd (n-j)) :
    ∃ z : ℤ, (Nat.lcmUpto n : ℚ) * endpointR n j = z := ...

theorem catalanT_lcm_sq_integral (n : ℕ) :
    ∃ z : ℤ, (Nat.lcmUpto n : ℚ)^2 * catalanT n = z := ...

theorem catalan_binomial_inversion (n : ℕ) : ... := ...

theorem catalanB_sharp_denominator (n : ℕ) :
    ∃ z : ℤ, (Nat.lcmUpto n : ℚ)^2 * catalanB n = z := ...

end ZetaLucas
~~~

If a reusable predicate such as IsRatInt(x) := exists z : Int, x = z makes closure
under sums and integer multiplication cleaner, introduce it locally with elementary
lemmas.

## Proof architecture

### Stage A — recurrence-defined companion

Define catalanB by primitive recursion at indices 0, 1, and n+2. Prove REC by unfolding.
Also prove the first values

\[
0,\ 1,\ 7,\ 404/9,\ 2603/9
\]

with norm_num; these are regression checks only.

Prove a recurrence uniqueness lemma: two rational sequences satisfying REC from n=1
and agreeing at 0,1 agree everywhere. This will later connect the recurrence-defined
object to the harmonic closed form without importing the giant Ore certificate. State
this trust boundary clearly in the module documentation: this file formalizes the
normalized recurrence companion; equality with the finite harmonic formula is separate.

### Stage B — endpoint recurrence

Prove TREC exactly. Prefer a direct finite-binomial proof in Lean. Useful identities are
Pascal's rule and

\[
(n+1)\binom nk=(n+1-k)\binom{n+1}k,\qquad
k\binom nk=n\binom{n-1}{k-1}.
\]

You may first prove a generic binomial-transform lemma for a sequence satisfying a
three-term polynomial recurrence. Keep all boundary cells explicit; the inhomogeneous
term (-4)^n comes from the exceptional initial residual B_1-4B_0=1 and must not be
silently discarded.

If direct convolution becomes unwieldy, formalize only the required ordinary formal
power-series substitution, not analytic generating functions. Do not assume the
transformed recurrence.

### Stage C — square expansion

First prove the one-step identity from TREC:

\[
T_{n+1}=\frac{16n^2}{(n+1)^2}T_{n-1}
        +\frac{(-4)^n}{(n+1)^2}.
\]

Induct separately on parity, or induct over the admissible forcing indices. The
contribution from forcing index j to T_n is

\[
\frac{(-4)^j}{(j+1)^2}
\prod_{\substack{j+2\le r<n\\r\equiv j\pmod2}}
\frac{16r^2}{(r+1)^2}
=(-1)^jR_{n,j}^2.
\]

All admissible j have parity n-1, yielding TSQ. Define the index set in the way that
minimizes parity coercion pain; parametrization by q is acceptable if equivalence to
the displayed j-sum is proved.

### Stage D — the crucial denominator lemma

Prove the stronger natural divisibility statement, avoiding rational normalization:

\[
\operatorname{endpointDen}(n,j)
\mid 2^{n-1}L_n\operatorname{endpointNum}(n,j). \tag{DIV}
\]

Then RL follows by casting.

The paper's proof is prime-by-prime. For every odd prime p and each power p^a <= n,
the multiples of p^a in [j+1,n] are p^a times a consecutive interval. Since p^a is
odd, it preserves parity. In a consecutive interval, one parity class exceeds the
other by at most one. Therefore the denominator progression has at most one extra
factor of p at each prime-power level. Mathlib gives exactly the lcm valuation:

~~~lean
Nat.factorization_lcmUpto (n) hp :
  (Nat.lcmUpto n).factorization p = p.log n
~~~

For p=2, the denominator progression is either odd or its valuation is bounded by
v_2(n!) <= n-1; the prefactor 2^(n-1) absorbs it. Relevant libraries/lemmas include:

    Mathlib.Data.Nat.Factorization.Basic
    Mathlib.NumberTheory.Chebyshev
    Mathlib.NumberTheory.Padics.PadicVal.Basic
    Nat.factorization_prod_apply
    Nat.factorization_le_iff_dvd
    padicValNat_factorial_lt_of_ne_zero

Do not overcommit to padicValNat if Nat.factorization makes product and lcm divisibility
cleaner. Isolate “parity imbalance in a consecutive interval is at most one” as a
reusable lemma before bringing in primes.

### Stage E — sharp integrality

From RL and TSQ, prove integrality of L_n^2 T_n using closure of rational integers under
squares and finite sums. Prove binomial inversion INV with a standard signed-binomial
identity. Since L_k divides L_n for k <= n, every term in INV is integral after
multiplication by L_n^2; conclude SHARP.

Prove Nat.lcmUpto k divides Nat.lcmUpto n for k <= n once as a helper, using the
Finset.Icc definition or factorization.

## Priority order

Must-have, in this order:

1. Clean definitions, companion recurrence, initial values, recurrence uniqueness.
2. Exact endpoint recurrence TREC.
3. Exact square formula TSQ.
4. Prime-power denominator lemma RL/DIV.
5. Final theorem SHARP.
6. Root import and full lake build.

Only after all six compile:

7. Generalize the endpoint theorem to an integer parameter b divisible by 4:
   \[
   (n+1)^2B_{n+1}=b(3n^2+3n+1)B_n-2b^2n^2B_{n-1}.
   \]
   The shift by b gives
   \[
   (n+1)^2T_{n+1}-b^2n^2T_{n-1}=(-b)^n.
   \]
   The same proof gives the exact classification
   \[
   (\forall n,\ L_n^2B_n\in\mathbb Z)\quad\Longleftrightarrow\quad4\mid b.
   \]
   Necessity is witnessed at n=4 for odd b and at n=8 for b congruent to 2 modulo 4.
   Do not attempt this generalization before the b=4 theorem builds.
8. Formalize the general integer-c transport recurrence from Proposition 6.12.
9. Formalize binomial inversion as a generic reusable theorem if the first proof was
   specialized.
10. Formalize exponent optimality at primes only if the Catalan Lucas congruence is
   already available. Do not assume that congruence.

Do not spend overnight time formalizing the real-analytic finite-part identity for G,
the asymptotic convergence factor, or the large harmonic/Ore certificate until the
algebraic sharp-denominator theorem is complete.

## Verification and overnight reporting

Keep a concise progress log at:

    work/harmonic_jets/CLAUDE_CATALAN_ENDPOINT_STATUS.md

Update it only with facts: theorem names that compile, exact remaining blockers, and
commands run. Do not call a theorem complete if its proof contains a placeholder.

Before finishing, run:

~~~bash
cd /home/ubuntu/fable-episode-2/zeta-math-2/lean
lake env lean ZetaLucas/CatalanEndpoint.lean
lake build
rg -n '\bsorry\b|\badmit\b|^\s*axiom\b' ZetaLucas/CatalanEndpoint.lean
~~~

The ripgrep result must contain no proof placeholders.

In the final status report include:

- all created/modified files;
- the strongest fully compiled theorem and its exact Lean signature;
- which stages A--E are complete;
- build/test output;
- any remaining blocker with the smallest isolated lemma that would unblock it.

Start now by reading the specified files and running the endpoint certificates.

---
