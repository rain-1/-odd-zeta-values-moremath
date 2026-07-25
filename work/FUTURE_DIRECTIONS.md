# Future directions — the exciting ones

Companion to OPEN_PROBLEMS.md. That file is the ranked task ledger; this one
is the ambition, with reasons. Written by Fable at close-out, 2026-07-25.
These are the directions I would race toward, in the order they pull at me.

## 1. The mirror-unification theorem

The p-adic rank wall says: every operator that eliminates the unwanted zeta
value eliminates the wanted one (0/300 with clean controls). The archimedean
window mystery says: "one of ζ(5), ζ(7), ζ(9), ζ(11)" has resisted
sharpening for 25 years. The DIG scan identified the kernel inclusion
ker ρ_{w′} ⊆ ker ρ_w as the exact p-adic analogue of the latter. Prove it
(plus rule R2) and the two become ONE theorem — the first statement in this
subject proved simultaneously about both completions. It would say: the
inability to isolate a single odd zeta value is not an accident of any
construction; it is a property of the elimination module itself. Estimated
character: hard linear algebra over function fields, not transcendence —
i.e., the kind of thing that falls to sustained attack. The single most
important provable statement the program identified.

## 2. The Gamma program: one function sees everything

Every "mystery constant" this program met resolved into the Gamma function's
orbit: archimedean Frobenius constants are values of a Γ-generating series
(Bloch–Vlasenko), and the p-adic Apéry limits are values of
Γ_p(x)e^{−Γ'_p(0)x} at p-power arguments, carrying the entire odd ζ_p tower
in an exponential. The conservation law r = 1 + ⌊m/2⌋ ties the ray structure
to unipotency. The program: make "the motivic Gamma function organizes both
completions" a theorem-level framework — prove the conservation law for the
cellular class; develop the algebra of the Kazandzidis limits (relations
across A, B, across primes, across the 15 families); and ask the question
NOBODY has ever posed because these constants had no names until this week:

    Are the p-adic Apéry limits Λ_a irrational?

That is a fresh irrationality question our own program created — and unlike
ζ(5), the Λ's come with 3-digits-per-level effective approximations built in.
The machinery that failed to reach ζ_p(w) might reach its own byproducts.

## 3. Classify the tax-free points

The purity tax vanishes exactly where Apéry stood: rank 2, no middle ray,
purity free. The wanted poster for the next irrationality proof is now
precise: a family whose minimal-ray class is pure of weight 5 — equivalently
a rank-2 (or ray-aligned) motive with ζ(5) as its only nontrivial period.
Brown's structural analysis suggests cellular geometry cannot supply it; the
purity screen (compute λ_min + PSLQ its period content, hours per family)
means the question is now SEARCHABLE: run it over 𝒞_N's thousands of
configurations, over non-cellular hypergeometric data, over the Bailey/Slater
lists Zudilin pointed at. Either the scan finds a law-breaker (jackpot) or
the empirical law "defect vs motivic invariants" becomes sharp enough to
conjecture the no-go — and no-go conjectures with measured support are how
the true boundary of a field gets drawn.

## 4. The bridge: local O(1) to global e^{δn}

The field's real question, now with its inventory complete: local congruence
structure is worth exactly O(1) per prime (sharp Lemma F, Kazandzidis p³,
the χ-twist — we know the constants), while irrationality needs e^{δn}. The
one framework that converts global growth conditions into arithmetic
conclusions is arithmetic holonomicity (Calegari–Dimitrov–Tang). Nobody has
fed the crystal-level local inventory into that framework. The interface —
what does a CDT-style determinant argument do with a complete Frobenius
descent structure? — is unexplored by anyone, and it is the only direction
on this list that could conceivably touch ζ(5) itself.

## 5. Congruences as geometry: the Hasse–Witt bridge

Every "exceptional digit" (p | a_r) should be a non-ordinary fiber of the
underlying pencil — the weight-2 center-vanishing at p ≡ 3 (mod 4) is CM
supersingularity showing through, and the χ-twist IS the nebentypus. Make
the dictionary exact: congruence tables of sporadic sequences ↔ point counts
and Hasse–Witt loci of their pencils. Cheap to start (a weekend), deep to
finish — it would let one READ geometry off elementary congruence data, and
conversely predict every exceptional structure in the tables from the
pencil. The kind of bridge that makes two communities read each other.

## 6. Verified experimental number theory, at scale

This field turned out to be uniquely suited to full formalization: its
proofs are certificate-shaped (finite witnesses + small uniform identities),
its instruments are validatable, and the week measured a 6× cost collapse
when statements are chosen for tameness. Build the Lean library properly:
Apéry-like pairs, Lucas/Kummer infrastructure, the χ-twisted theorem as API,
telescoping-certificate checking as a tactic. End state: a subject where
"verified" is the default evidence class and referee passes are machine
work. The five silently-inoperative safety controls this campaign found are
the argument that this matters beyond aesthetics.

## 7. The missing 3

The factor 12 = 2²·3 is sharp, attained, and its 3 has NO derivation — the
geometric mechanism provably cannot produce it. Something produces it.
Whatever does (the Bernoulli normalization? a second lattice index? a
2-torsion phenomenon in disguise?) is a piece of integral-motivic structure
nobody has named. Small question, possibly deep answer — the program's
favorite kind.

---

The honest wager across all seven: none promises ζ(5). Items 1–2 promise
theorems; 3–5 promise either discoveries or sharp conjectures; 6 promises
infrastructure that compounds; 7 is a lottery ticket with structural upside.
That portfolio shape — most value in understanding, tail exposure to
miracles — is what this field has always rewarded, one year before each of
its surprises.
