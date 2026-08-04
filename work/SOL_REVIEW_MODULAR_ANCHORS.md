# Sol's hostile referee report on papers_out/modular_anchors (2026-08-05)


This is substantially better than the previous paper. The symmetric-square issue is now stated correctly, and the paper has a real organising idea:

\[
\text{companion}
=
\text{inhomogeneous Frobenius layer in the natural uniformising coordinate}.
\]

However, as a hostile referee, I would still not recommend circulating the present version as a theorem paper. The principal remaining problem is not one hidden gap comparable to the earlier MUM error. It is a systematic mismatch between the strength of the computations and the strength of the prose.

The TeX compiles successfully to a nine-page PDF.

## Overall verdict

There are three different papers mixed together:

1. a computational discovery report about the fifteen sporadic families;
2. a rigorous theorem about companions under an exact operator-factorisation hypothesis;
3. a speculative research programme connecting the Brown–Zudilin \(\zeta(5)\) operator to mirror symmetry, Yukawa couplings, coactions, and arithmetic congruences.

Each could be valuable. Combining them is possible, but the boundaries need to be much sharper. At present, exact finite computations are frequently followed by language such as “is modular-parametrized,” “is mirror-arithmetic,” “provably does not exist,” “the mod-\(p\) shadow of ASD,” and “all fifteen satisfy the bare formula.” Those statements are stronger than the evidence recorded beside them.

The paper’s own evidence labels are careful; the surrounding sentences often are not.

# 1. The symmetric-square repair is correct

Construction 5.1 now says explicitly that
\[
L=\frac{P_3(t)}{\sigma^3}\,F\,\theta_q^3F^{-1}
\]
is strictly stronger than MUM and is equivalent, in the third-order case, to
\[
y_2=\frac{y_1^2}{2y_0}.
\]

That is the right correction.

It also correctly says that a generic MUM operator retains a Yukawa-type coupling in canonical coordinates. This is the conceptual improvement the earlier gap demanded.

But the paper has not yet completed the corresponding mathematical upgrade. It says:

> all fifteen sporadic families satisfy the bare formula — the symmetric-square class

while Theorem 5.2 only reports finite coefficient agreement, and the paper later lists proof of the operator factorisations as an open problem.

The correct present statement is therefore:

> Finite exact computations are consistent with all relevant third-order sporadic operators being symmetric squares and with the resulting Eichler formula producing their companions.

It is not yet:

> all fifteen families satisfy the symmetric-square hypothesis.

For the third-order cases, this can and should be settled immediately by exact rational operator identities. It is a finite symbolic computation, not a long-term research problem.

# 2. The uniform formula has a notation and order problem

The construction alternates among

\[
\theta_q^{-3},
\qquad
\theta_q^{-w},
\qquad
\theta_q^{w+1},
\]

without a precise convention relating \(w\), recurrence order, zeta weight, and modular weight.

Construction 5.1 says:

> weight-\(w\) case: \(\theta_q^{\,w+1}\), adjusted

but then Theorem 5.2 gives
\[
B(n)=[t^n]F\theta_q^{-w}\left(\frac{t\sigma^w}{PF}\right).
\]

For Apéry’s \(\zeta(3)\) recurrence, the required inverse is \(\theta_q^{-3}\). Depending on the paper’s meaning of \(w\),

- zeta weight \(w=3\) gives \(\theta^{-w}\);
- modular weight \(w=2\) gives \(\theta^{-(w+1)}\);
- differential order \(r=3\) gives \(\theta^{-r}\).

The safest formulation is to stop using \(w\) here and use the operator order \(r\):

\[
L=C(t)\,F\,\theta_q^rF^{-1}
\quad\Longrightarrow\quad
y_B
=
F\theta_q^{-r}\!\left(\frac{t}{C(t)F}\right).
\]

Then specialise:

- second-order operators: \(r=2\);
- third-order symmetric-square operators: \(r=3\);
- the five-dimensional block, if rectifiable in an appropriate generalized sense: \(r=5\), but generally with intervening coupling operators.

This would remove a real ambiguity from the central theorem.

# 3. The “exhaustion theorem” is narrower than the paper claims

Theorem 2.1 establishes inconsistency of a particular finite-dimensional ansatz:

- prescribed tame arguments;
- harmonic weight;
- degree at most \(3\);
- specified character-twisted letters;
- specified summand representation.

That is meaningful negative evidence. But the paper repeatedly turns it into:

> no harmonic companion exists;

> the classical letters do not merely happen to fail; their failure is a theorem;

> for the conjectural seven no formula of the classical shape exists.

That conclusion does not follow unless “classical shape” is defined to mean exactly the tested finite vector space.

The computation does not exclude, for example:

- higher polynomial degree in harmonic letters;
- nested harmonic sums;
- additional affine arguments;
- a different hypergeometric representation of the same \(A(n)\);
- telescoping terms that vanish only after summation;
- rational functions of \(n,k,l\) multiplying the letters;
- indefinite-sum or WZ-type extensions outside the chosen basis.

The theorem should say:

> There is no companion in the explicitly defined tame degree-\(\le3\) ansatz.

That is already a useful theorem. “No harmonic companion exists” is much larger.

There is another issue: the result is a two-prime rank computation, not a proof over \(\mathbb Q\), unless the modular witnesses are reconstructed into exact rational certificates.

If a linear system is inconsistent modulo one good prime, then the rational system is indeed inconsistent, provided the modular matrix is exactly the reduction of the rational system and no denominator vanishes modulo that prime. This can be made rigorous. The paper should state the lemma and verify the good-prime condition. At present, the evidence label allows “two-prime computational negative,” but the prose calls it proved without explaining the modular-to-rational implication.

This is fixable.

# 4. Theorem 4.3 makes an invalid inference from finite integrality

The theorem states:

> All three deformation-unreachable families \(\mathbf B,\delta,\zeta\) have integral nome expansions: they are modular-parametrized.

Finite integrality of coefficients does not imply modular parametrisation. Even integrality to all orders would not by itself imply modularity.

Similarly, identifying
\[
F_\zeta(q)
=
\frac18\bigl(9E_2(q^9)-E_2(q)\bigr)
\]
through \(q^{26}\) is strong discovery evidence but not an identity theorem.

There are two distinct upgrades available:

### Exact operator verification

Show that the proposed modular pair \(t(q),F(q)\) satisfies the differential equation exactly. This can often be done by:

- proving the eta quotient or Eisenstein expression is modular;
- deriving a rational relation between \(t\), \(\theta t\), and \(F\);
- substituting into \(L(F)=0\);
- using finite-dimensionality of the relevant modular-form space or a Sturm bound.

Then the identification is proved.

### Careful computational wording

Until that is done, write:

> The first 26 coefficients agree with the modular form … and the first 30 coefficients of the mirror map are integral.

Not:

> the families are modular-parametrized.

The paper itself previously acknowledged that integrality is a fingerprint, not a proof. The theorem currently violates that caution.

# 5. The companion theorem is the strongest part, but needs recasting

The exact observation
\[
L(y_B)=t
\]
from the boundary defect is excellent. It gives a canonical normalization and explains why an inverse differential operator appears.

The clean theorem is:

> Suppose an order-\(r\) operator satisfies the exact identity
> \[
> L=C(t)F\theta_q^rF^{-1},
> \]
> with \(q=t+O(t^2)\), \(F(0)=1\), and suppose the normalized companion generating function satisfies \(L(y_B)=t\). Then
> \[
> y_B
> =
> F\theta_q^{-r}\!\left(\frac{t}{C(t)F}\right).
> \]

This is an actual theorem and its proof is one line.

Then there should be a separate computational proposition:

> For each of the fifteen sporadic pairs, the right-hand side agrees with the normalized companion through \(n\le20\) or \(22\).

And then exact corollaries, one family at a time, after proving the relevant factorisation.

The present Theorem 5.2 is explicitly labelled finite verification, which is honest, but the surrounding language calls it “the uniform companion formula” and says it “yields the second solution for every one” of the fifteen. That sounds all-\(n\).

A reader should not have to inspect the evidence badge to discover that “for every \(n\)” has not been proved.

# 6. “All fifteen are the symmetric-square class” is not literally coherent

The fifteen sporadic list contains both second-order and third-order recurrences. Symmetric-square terminology applies to third-order operators arising from second-order ones. It does not apply in the same manner to the second-order families.

The paper should divide the list:

- order two: direct projective rectification, typically involving \(\theta_q^2\);
- order three: symmetric-square condition and \(\theta_q^3\);
- higher order: generalized normal form with nontrivial coupling data.

Then the meaningful claim becomes:

> Every tested sporadic operator is in the “barely rectifiable” class appropriate to its order; in order three this is the symmetric-square class.

That would preserve the dichotomy without abusing the term \(\operatorname{Sym}^2\).

# 7. Curve-blindness is not yet a self-contained theorem

Theorem 3.2 refers to:

- “pinned \(\mathbb Q\)-combinations”;
- “curve atoms”;
- degrees \(\le3\);
- “direction boxes as in the companion paper”;
- “every \(\zeta\)-graded component”;
- finite two-prime rank computations.

None of the finite spaces are fully defined in this paper. Therefore the theorem cannot be checked from this paper.

The coupling lemma may be a genuine symbolic theorem. The remaining result is a finite exhaustive computation over a specified search domain. To be publishable as a computational theorem, the paper needs:

1. an exact definition of the atom set;
2. the allowed direction vectors and degree bounds;
3. the pinning constraints;
4. the matrices whose ranks are computed;
5. the modular-to-rational justification;
6. preferably a certificate or hash of the exact matrices.

“Direction boxes as in the companion paper” is not enough for a theorem carrying conceptual weight in this paper.

Also, the abstract says:

> all polynomial-curve deformations provably fail.

The theorem only treats bounded degrees and bounded direction boxes. “All” must be removed unless the coupling lemma genuinely reduces every polynomial curve, with arbitrary direction, to the checked finite span. The text does not presently demonstrate that reduction.

# 8. The ASD claims are interpretations, not established consequences

Proposition 6.1 observes that an experimentally fitted twist agrees with the nebentypus at a few primes. It then states:

> the twisted Lucas law is the mod-\(p\) shadow of the Atkin–Swinnerton-Dyer congruence structure.

That is a plausible interpretation, not a verified mathematical consequence.

To establish it, one needs a theorem connecting:

- the coefficients \(A(n)\) and \(B(n)\);
- the identified modular form;
- the relevant formal group or Frobenius action;
- the stated Lucas-type congruence.

Agreement of a sign at \(p=5,11\), with consistency at \(7,13\), does not prove that mechanism.

The proposition should be renamed something like:

> Nebentypus compatibility of the observed twist.

Then the ASD explanation belongs in a conjecture or remark.

The weight-one law
\[
A(p)\equiv b_p-b\chi_N(p)\pmod p
\]
is interesting, but testing primes only through \(23\) is extremely preliminary. Because the expression was discovered from the same small data, it needs held-out primes before being presented as a robust pattern. It is currently too easy for a simple character-valued correction to interpolate a handful of residues.

# 9. The mirror section contains the largest conceptual overreach

The exact indicial computation showing a fivefold exponent \(0\) is real and useful. It establishes a five-dimensional local generalized eigenspace for local monodromy at \(t=0\).

It does not by itself establish:

- a Calabi–Yau variation;
- a polarized variation of Hodge structure;
- self-duality;
- global nilpotent monodromy of the required type;
- geometric origin;
- a “one floor above elliptic-modular” relationship;
- a Golyshev arithmeticity criterion.

The phrase

> the \((1,1,1,1,1)\) Calabi–Yau-type signature matching weight five

needs definition and probably qualification. A repeated zero exponent is a MUM-like local signature, not a complete Hodge diamond.

Similarly, finite integrality
\[
t(q)\in\mathbb Z[[q]]
\]
through \(q^{26}\), and finite integrality of \(K(q)\) through \(q^{32}\), are evidence of arithmetic structure. They do not establish:

> the family is mirror-arithmetic;

or:

> the family passes the Golyshev-style arithmeticity test outright.

“Mirror-arithmetic” is not a standard property defined in the paper. If it is intended as a new descriptive term, define it explicitly as the conjunction of the finite observations. Otherwise it reads as a theorem of geometric origin.

A more defensible title would be:

> Mirror-type local and arithmetic signatures of the \(\zeta(5)\) operator.

That is still notable.

# 10. The Yukawa invariant needs an invariant definition

The quantity
\[
K(q)=\theta^2(\widehat g_2/F)
\]
is called “the Yukawa-type invariant of the block’s exact \(q\)-normal form.”

But the paper does not define:

- the normal-form reduction;
- \(\widehat g_1,\widehat g_2\);
- the allowed gauge transformations;
- why \(K\) is invariant under those choices;
- why \(\widehat g_1\equiv0\) is meaningful rather than normalization;
- how this \(K\) enters the corrected inverse operator.

This is precisely the new datum on which the paper’s conceptual dichotomy depends. It cannot remain a symbol imported from computation logs.

The paper should include the normal form explicitly. Something schematic such as
\[
\theta_q^5
+
K_3(q)\theta_q^3
+
K_2(q)\theta_q^2
+\cdots
\]
would already make the obstruction concrete. Better still, derive the variation-of-parameters operator showing where \(K\) intervenes.

At present the paper says “nontrivial Yukawa datum obstructs the bare formula,” but does not mathematically demonstrate the obstruction.

# 11. The coaction section is currently too speculative

The conjecture that jets are de Rham shadows of motivic coaction components is potentially interesting. The supporting paragraph, however, uses phrases such as:

> has paid rent three times;

> it forced;

> retrodicts;

> assigns the sporadic dichotomy to Galois equivariance;

> reassigned by modular data to Betti degeneracy.

None of those claims is formulated precisely enough to assess.

In particular, no motivic object, coaction map, or comparison morphism is defined. The words “de Rham,” “Betti,” “Galois equivariance,” and “coaction” are carrying conceptual prestige without yet carrying mathematical content.

I would either:

- remove this section from the theorem paper and retain it in a research-programme note; or
- replace it with a precise conjectural diagram naming the objects and maps.

For example:
\[
\Delta I^\mathfrak m
=
\sum_r I_r^{\mathrm{dR}}\otimes I_r^\mathfrak m,
\]
followed by a precise proposed identification between the \(r\)-th jet and a specified \(I_r^{\mathrm{dR}}\).

Without that, it weakens rather than strengthens the paper.

# 12. The “factory” and “zoo occupancy” claims need restraint

A scan of roughly \(5\times10^4\) pairs in a specified bank is a useful computational census. It does not support:

> no sixteenth pair in the explored corner

unless the explored corner is formally defined and the enumeration is exhaustive within it.

The phrase “all \(91\) hit classes exactly confirmed” needs an equivalence relation: equal operators, rational pullbacks, twists, rescalings, or sequence equality?

Likewise:

> supporting the completeness of the Zagier/Almkvist–Zudilin lists at these levels

may be reasonable, but only after the search space is stated mathematically. At present, the search is described through implementation categories rather than a theorem specifying the finite universe.

This result could become a clean computer-assisted classification theorem if the bank is finite and exactly enumerable. It deserves its own proposition with exact hypotheses.

# 13. There are several internal inconsistencies

A few examples:

- Open Problem P2 says “Identify \(\delta\)’s form,” but Theorem 4.3 already gives explicit eta expressions for \(t\) and \(F\), and the ASD section says the identification is nearly a theorem modulo one hypothesis. The open problem should be “complete the proof of \(\delta\)’s modular parametrisation.”

- The introduction says all three deformation-unreachable families have integer nomes and treats this as evidence. Theorem 4.3 then says “they are modular-parametrized.” These should use one consistent evidential status.

- The abstract calls the \(\zeta\) companion “exactly verified.” It is only verified through \(n\le22\), unless an exact operator factorisation has now been completed.

- The abstract says “the complete tame harmonic ansatz … is inconsistent” and then “the classical answer has a boundary, locate the boundary exactly.” A boundary of one chosen finite ansatz is not necessarily the exact boundary of harmonic representations in general.

- Theorem 7.1, item 3, has an empty evidence range:
  \[
  \texttt{\textbackslash VerifiedR\{\}}
  \]
  for the root-integrality statement. The actual computed range must be supplied.

- “Theorem” and “Proposition” environments are used for purely finite experiments. That can be legitimate, but then the title or first sentence should say “computer-assisted finite verification” and state the exact certificate.

# What I think is genuinely strong

The paper has several important and potentially publishable ideas.

First, the boundary-defect equation
\[
L(y_B)=t
\]
is conceptually clean and useful.

Second, once exact factorisation is available, the companion formula
\[
y_B
=
F\theta_q^{-r}
\left(\frac{t}{C(t)F}\right)
\]
is elegant. It replaces an ad hoc search for harmonic weights with canonical inversion in the uniformising coordinate.

Third, the discovery that the third-order sporadic operators may uniformly lie in the symmetric-square class is structurally significant. Proving the finite operator identities for the relevant families should be a priority.

Fourth, the contrast between the sporadic order-two/order-three cases and the \(\zeta(5)\) five-block looks real. The five-block appears not to admit the same bare normal form, and isolating the residual coupling series is exactly the correct next step.

Fifth, the modular identifications may well be correct. Most appear amenable to exact proof using standard modular-form methods rather than long coefficient checks.

# Recommended reorganisation

I would restructure the paper around one proved theorem and three tiers of evidence.

## Core theorem

State and prove the abstract companion inversion theorem for an exact rectified operator:
\[
L=C(t)F\theta_q^rF^{-1}.
\]

## Exact sporadic results

For each family where feasible:

- prove the modular parametrisation exactly;
- prove the differential-operator identity exactly;
- deduce the companion formula for all \(n\).

Even doing this first for Apéry and \(\zeta\) would create a rigorous paper.

## Computer-assisted finite results

State precisely:

- the tested ansatz spaces;
- the rank certificates;
- the coefficient ranges;
- the search universes;
- the modular-to-rational lemmas.

## Conjectural mirror programme

Place the five-block, Yukawa, coaction, and mirror bridge in a clearly labelled final section. Avoid presenting local signatures as established geometry.

# Priority corrections

Before another review, I would require these five changes:

1. Replace every unconditional modular-identification sentence based only on coefficient agreement with a finite-verification statement, or prove it by Sturm/operator methods.

2. Replace “no harmonic companion exists” with the exact bounded ansatz excluded.

3. Rewrite the companion theorem using operator order \(r\), not an ambiguous weight \(w\).

4. Prove the symmetric-square identities for the third-order sporadic operators and move them out of the “empirically confirmed” category.

5. Downgrade the mirror, ASD, and coaction interpretations to conjectures unless the missing structural maps are supplied.

The paper now contains a strong mathematical spine. The principal danger is that it attempts to convert an unusually rich collection of computational discoveries into a completed theory too quickly. A narrower paper proving the exact modular-anchor theorem for one or two new families would presently be much stronger than a broad paper claiming the entire sporadic and \(\zeta(5)\) landscape.


---

# Point-by-point response (revision of 2026-08-05)

**STANDING NOTE (do not remove):** this response file is the ledger of
evidential statuses settled during review. Future revisions of
`papers_out/modular_anchors` MUST NOT re-upgrade any statement below
(e.g. finite agreement → identity, finite integrality → modularity,
box-bounded exclusion → universal exclusion) without adding a new dated
entry here recording the proof that licenses the upgrade.

**§1 (Sym² must be proved, not asserted).** DONE, and upgraded beyond the
request: all six third-order sporadic operators are now PROVED symmetric
squares by exact residual-zero identities in ℚ(t) (`eps57_sym2_all.py`),
with the uniform closed form D̃ = θ² − t(2aθ² + aθ + b/2) + ct²(θ+½)².
Combined with the order-2 Frobenius lemma and the boundary-defect/
uniqueness lemmas, the uniform companion formula is now an ALL-n THEOREM
for all fifteen families (paper Thm 3.4). The former finite verification
is demoted to an implementation check.

**§2 (w/r ambiguity).** DONE: operator order r used exclusively;
dictionary in §1.2.

**§3 (exhaustion overclaim + modular-to-rational).** DONE: the ansatz is
fully defined in-paper (Def 5.1, with the three tame argument sets);
the theorem states exactly that space; the scope remark lists what is NOT
excluded; the modular-to-rational transfer lemma is stated and proved
(Lemma 1.1); "no harmonic companion exists" does not appear.

**§4 (integrality ≠ parametrization).** DONE: Theorem 4.3 dissolved into
(i) Prop 4.1 — the ζ identification PROVED via Ligozat + Sturm bound 2 +
agreement to q⁴⁰; (ii) a discovery-grade Verification 4.3 with the
explicit caveat sentence; (iii) δ's status cited precisely
(proved modulo the Atkin–Lehner degree-one hypothesis).

**§5 (recast companion theorem).** DONE exactly as prescribed: abstract
one-line-proof inversion theorem (Thm 2.4) + rectification hypotheses
proved separately (§3) + all-n corollary + demoted verification.

**§6 (Sym² incoherent across orders).** DONE: split by operator order
(Lemma 3.1 for r=2 incl. Cooper d≠0 rows; Thm 3.2 for r=3).

**§7 (curve-blindness not self-contained).** DONE: atoms, d-maps, pinning,
boxes defined in-paper (Def 5.4). Upgraded per the coordinator's addendum:
the coupling lemma's reduction is degree-independent, and a NEW exact
computation (Veronese saturation, Lemma 5.6: box directions have full rank
6/10/15/21 in Sym^{2..5}(ℚ³)) makes the top-grade clause unconditional
over ALL polynomial curves and directions; the sub-top clauses are stated
as box-certified. The abstract's "all polynomial-curve deformations" now
refers only to the proved top-grade clause.

**§8 (ASD interpretation; weight-1 law preliminary).** DONE: renamed
nebentypus compatibility; ASD mechanism moved to Conjecture 6.3. The
weight-1 law was subjected to sixteen genuinely held-out primes
(29..97) per family (`eps57_heldout.py`): ALL PASS, all six families.
Status upgraded from "fitted on 7 primes" to "fitted on 7, survives 16
held-out" — still finite verification, labeled as such.

**§9 (mirror overreach).** DONE: section renamed "mirror-type signatures";
"mirror-arithmetic" and "passes the Golyshev test outright" removed;
local block stated as exact indicial computation; integrality as
verification with ranges. ADDITIONAL correction beyond the report: the
root-integrality items are withdrawn entirely — they are universal for
integer series (papers_out/half_apery, Lemma) and carry no arithmetic
information; correction also appended to Z5_MODULARITY_PROBE.md.

**§10 (K needs definition).** DONE: Definition 7.4 gives the normal form
θ⁵ + K₃θ³ + ..., the ĝ-tails, where K intervenes, and states honestly that
gauge-invariance and the ĝ₃, ĝ₄ tower are OPEN — K's current status is an
exactly computed series in a fixed scripted normalisation.

**§11 (coaction too speculative).** DONE: reduced to one precise
conjectural display (Δ I^m = Σ I_r^dR ⊗ I_r^m with the jet
identification) plus a two-sentence record of its one retrodiction and
one falsifiable prediction. All rent-paying prose removed.

**§12 (census restraint).** DONE: search universe and equivalence
relation defined (Def 5.7); result stated as a Census environment scoped
to that universe; the four uncovered directions named.

**§13 (internal inconsistencies).** All six fixed: P2 reworded; abstract
ranges honest; nome integrality consistently discovery-grade; boundary
wording removed; empty VerifiedR filled (then withdrawn per the
half-apery correction); finite experiments use Census/Computer-assisted
finite verification environments.

**New results added during revision** (all labeled): the six Sym²
identities [PROVED]; the ζ form identity [PROVED]; the first ζ
annihilation law [PROVED, order-2 WZ certificate, eps45]; Veronese
saturation [PROVED]; held-out primes [VERIFIED]; root-integrality
withdrawal [correction].

**Disagreements with the referee:** none of substance. One scope note:
the referee's suggested reformulation "no companion in the explicitly
defined tame degree-≤3 ansatz" was adopted verbatim; we additionally kept
the observation (now Prop 4.2, proved) that part of the ansatz failure is
explained by alphabet degeneracy, which the report did not request but
does not conflict with.
