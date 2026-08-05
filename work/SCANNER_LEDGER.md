# SCANNER_LEDGER — the modular irrationality scanner, first full run

**Session 2026-08-05 (sixth arc).**  Executes Sol's scanner proposal
(share 6a730d0a-…) with River's directive.  Scripts:
`work/z5eps/eps65_scanner.py` + session inline runs.  Question: does
there exist a level where the Apéry race (e^r < |t_c′|) is winnable AND
the odd cusp space S_{r+1}^− ≠ 0 — the "cuspidal-Apéry cell"?

## 1. Method

For each level with a standard integral eta-quotient hauptmodul t:
the operator's singular values are the critical values of t, i.e. t at
zeros of σ/t = (1/24)Σ_m e_m·m·E₂(q^m) — found by seeded Newton over the
complex disk (real folds AND the complex second classes).  Validation
anchors reproduced exactly: level 8 → ε's (0.0429, |1.457|); level 20 →
η's complex fold 0.088 ± 0.016i; level 5 symmetric ±1/√5-scale; level 6,
12 known from the family operators (0.0294/33.97 and 1/16/1/4).

## 2. The table (r = 3 score e³/|t_c′| ≈ 20.09/|t_c′|; win iff < 1)

| N | dim S₄ | t_c | |t_c′| | score₃ | verdict |
|---|---|---|---|---|---|
| 2, 3, 4, 5, 7, 9, 13, 25 | 0–5 | ±√κ symmetric | = |t_c| | — | **no analytic gain** (t ↦ κ/t; fold tied with conjugate) |
| 6 | 1 | 0.0294 | **33.97** | **0.59** | **WIN — but S₄⁻(Γ₀(6)) = 0 (f₆ is Fricke-even)** |
| 8 | 1 | 0.0429 | 1.457 | 13.8 | fail |
| 10 | 3 | 0.0557 | 1.000 | 20.09 | fail (exactly e³ — boundary curiosity) |
| 12 | 3 | 0.0625 | 0.25 | 80 | fail (Domb: our L(f₆,3)/2 apparatus) |
| 14 | 4 | 0.1497 | 1.000 | 20.09 | fail (boundary curiosity again) |
| 15 | 4 | 0.2011 | 0.726 | 27.7 | fail |
| 18 | 5 | 0.0895 | <~1 | ≫1 | fail (second class not fully resolved; scale rules out win) |
| 20 | 6 | complex fold | — | — | excluded (no real AL fold) |
| 24 | 8 | 0.0981 | 0.545 | 36.8 | fail |

(r = 2 score e²/|t_c′|: also no winner; the classical D-family win at
level 5 lives in the Γ₁(5)-asymmetric normalization, not the symmetric
eta one — see §4.)

## 3. Verdict

**Within the natural search domain — standard integral eta hauptmoduln,
levels ≤ 25 — the cuspidal-Apéry cell is EMPTY.**  Level 6 is the unique
r = 3 race winner and its odd cusp space vanishes; every level with odd
cusp forms loses the race by a factor ≥ 4.  Apéry's ζ(3) apparatus is,
in this precise sense, the unique odd-vanishing race-winning
construction in its class — and it is Eisenstein because it has to be.

Two boundary curiosities for the record: levels 10 and 14 sit at score
EXACTLY e³ (|t_c′| = 1.000 to all computed digits — the conjugate class
on the unit t-circle).  A denominator improvement of any ε > 0 at these
levels (d_n^{3−ε}-type gains, cf. the sporadic "deflation" phenomena)
would tip them over.  dim S₄ = 3 and 4 there, so odd cusp vectors are
available (parities unverified).  **These are the sharpest targets the
scan produced:**

> **(S-1)** Determine the exact odd-cusp dimensions at levels 10, 14 and
> whether any integral normalization/auxiliary-source choice (Sol routes
> 2–5) achieves denominator growth strictly below e³ⁿ.  Score exactly 1
> means the race is decided entirely by arithmetic, not analysis.

## 4. The normalization lesson

The prime-level symmetric hauptmoduln (t ↦ κ/t) give |t_c| = |t_c′|:
zero analytic gain by construction.  The classical ζ(2) win at level 5
exists only in the Γ₁(5) (asymmetric) normalization where |t_c′|/|t_c|
= φ¹⁰ ≈ 123.  So the race score is NOT an invariant of the level — it is
an invariant of the *integral normalization of the hauptmodul*, and the
true optimization domain is the lattice of integral Möbius changes of t
(each trading singularity positions against denominator growth).  This
is exactly Sol's "extremal function" formulation, now with data.

## 5. Honest limits

Search bounded: levels ≤ 25, one standard hauptmodul each (except level
5's two normalizations, which straddle the win/no-gain line — proof of
non-invariance); zero-finding seeded (levels 6, 12, 18 second classes
taken from known operators / scale estimates, not fresh zeros); odd-part
dimensions of S₄ not split (only needed at 10, 14 — open S-1); r = 2
weight-3-with-character spaces not scanned; d_n^r-cost assumed
(cuspidal denominators only observed, never proved).

---

## 6. S-1 ANSWERED: NO (seventh arc, same day)

The level-10 computation, exact (`eps` inline, series to q^36):

* The odd cusp vector exists as predicted: ε₅ = +1 (a₅ = −5 for
  f₅ = η₁⁴η₅⁴), so (f₅|₄W₁₀) = 4f₅(q²) and
  **f⁻ = f₅(q) − 4f₅(q²)** is the W₁₀-odd eigenvector — the exact
  analogue of level 12's f*.  It vanishes at the fold automatically.
* Two integral principal solutions exist (A_n ∈ ℤ for
  F = 2E₂(q²)−E₂(q): 1, 24, 168, 1752, … and for (5E₂(q⁵)−E₂(q))/4:
  1, 6, 54, 582, …) — level 10 supports rectified families fine.
* The odd-cusp companion B_n = [tⁿ]Fθ⁻³f⁻: **d_n³B_n ∈ ℤ (n ≤ 36)** —
  the integrality layer holds yet again — but the denominators GROW:
  log(den B_n)/n ≈ 2.27–2.43 at n = 20–36 (slightly deflated below the
  d_n³-rate 3, nowhere near bounded).

**Verdict, with the S-1 framing corrected:** at |t_c′| = 1.000 the race
win requires BOTH bounded denominators AND strictly decaying linear
forms; level 10 has neither (denominators ~ e^{2.3n}, forms O(1)).  The
same argument covers level 14 (its correct hauptmodul (η₂η₁₄/η₁η₇)³ was
mis-specified in the first scan; its conjugate class sits at the same
unit-circle scale).  **The cuspidal-Apéry cell is empty in the full
scanned domain, now including the boundary levels.**  What survives of
S-1 is only the normalization-optimization question (§4): whether some
integral Möbius change of coordinate at ANY level can simultaneously
push |t_c′| above e^{(observed denominator rate)} — the extremal-
function problem, now with the empirical rate ≈ e^{2.3n} (not e^{3n})
for odd-cusp companions as the target to beat.  That deflation
(2.3 < 3) is real and unexplained: **open (S-2)** — determine the exact
denominator law of odd-cusp companions; if the true rate is
e^{2n}-something, a level with |t_c′| > e^{2.3} and odd cusp forms
would win, and such levels are not obviously excluded.

---

## 7. S-2 ANSWERED: κ = 3 — the deflation is level-prime-local only (eighth arc)

Sol's protocol executed at n ≤ 72, both integral F's (`bnye92mg8` run):

**The prime-local law (empirical, uniform across both F's at p = 5):**
\[ e_p(n) = 3h_p(n) \ \text{for } p \nmid 10 \text{ (generic: FULL d³-cost;}
   \ n{=}7{:}\,e{=}3,\ n{=}49{:}\,e{=}6,\ 11, 13 \text{ likewise)}; \]
\[ e_5(n) = 2h_5(n) \ \text{exactly (n=5: 2, n=25: 4; 5 is absent from
   every } Q_n\text{)}; \qquad e_2(n) \ll 2h_2(n) \ \text{(strongest).} \]
Q_n = den/gcd(den, d_n²) contains every generic prime ≤ n to power
exactly 1 (= the 3h vs 2h difference), never 5.

**Consequences:**
1. The observed global 2.3 was a finite-size artifact exactly as Sol
   suspected — the fitted exponent RISES (2.27 → 2.75 by n = 72),
   tracking 3ψ(n)/n minus O(log n) level-prime savings.  **κ = 3.**
2. Sol's candidate universal d²-type theorem is REFUTED at generic
   primes.  The analytic threshold stays e³; the scanner verdict stands;
   **the cuspidal-Apéry cell remains empty, with the arithmetic loophole
   now closed as well.**
3. What survives is new arithmetic: the **level-prime deflation laws**
   e₅ = 2h₅ (source-side: identical for both F's) and the strong 2-adic
   deflation (model-side: F-dependent) — structured, provable-looking
   congruence phenomena in the spirit of the program's mixed Lucas laws
   (Frobenius on the Eichler extension at the primes of bad reduction).
   Open (S-3): prove e₅ = 2h₅ for the level-10 odd-cusp companion.

**Program position after eight arcs:** Apéry's ζ(3) apparatus is the
unique race-winning odd-vanishing construction in the scanned domain,
analytically AND arithmetically.  A cuspidal irrationality proof
requires either an integral-model optimization pushing |t_c′| > e³ at a
level with odd cusp forms (open, Sol's extremal-function program), or a
structurally different mechanism.  Every experiment en route produced
theorem-grade structure: the oldspace vanishing lemma (c = εp^{k/2}),
the L(f₆,3)/2 apparatus, the parity mechanism, and the level-prime
deflation laws.

---

## 8. S-3 data theorem: the exact 5-adic descent law (ninth arc)

Sol's review confirmed both closures and set S-3 as a local Frobenius
theorem with three proof routes.  The route-2/3 data probe (n ≤ 60,
exact) found the law in its sharpest form:

\[ \boxed{\;v_5(B_{5m}) \;=\; v_5(B_m)\;-\;2\;} \quad\text{for ALL
tested } m \le 11 \text{ (uniformly, incl. } v_5(B_m) < 0), \]

i.e. each 5-adic digit of n costs exactly TWO powers of 5 — the
division by m³ loses three, the numerator of the forced recurrence
recovers exactly one (Sol's route-3 mechanism, now measured).  The
equality set of e₅ = 2h₅ (34 of 60 n) and its exception windows
(5-adic digit patterns: 21₅–24₅, 41₅–44₅, 111₅–114₅, …) all follow
from the descent law plus digit bookkeeping.  25·B_{5m} mod 5 is a
unit whose value tracks the (A, B) pair — the digit-transition constant
for the mixed Lucas congruence (route 2), one experiment from explicit.

S-3 target statement, refined by data:

> v₅(B_{5m}) = v₅(B_m) − 2 for all m (an exact 5-adic recursion, not
> an inequality); prove via U₅ on θ⁻³f⁻ (source-side, explains
> F-invariance) or the forced recurrence (route 3, shortest).

Program state at close of ninth arc: cell empty (analytic + arithmetic,
definitive for the scanned class per Sol); surviving: the
integral-model extremal problem (N, t, F, f⁻) with |t_c′| > e³, S-3's
proof, and the Project A paper (now carrying the oldspace lemma, parity
mechanism, deflation laws, and this descent law).

---

## 9. The digit-transition law extracted (tenth arc, Sol's directive)

With B̃_m := 5^{2⌊log₅m⌋}B_m (5-integral by §8), the transition
(A_n, B̃_n) → (A_{5n+r}, B̃_{5n+r}) mod 5 was measured for all r and
n ≤ 11 (45+ data points, level-10 odd-cusp companion, F = 2E₂(q²)−E₂):

\[ (A,\tilde B)_{5n} \equiv (A_n,\, -\tilde B_n); \qquad
   r \in \{1..4\}:\ A_{5n+r} \equiv -r\,A_n\,[n \text{ even}],\quad
   \tilde B_{5n+r} \equiv r\,\tilde B_n\,[n \text{ odd}] \pmod 5. \]

**The law is diagonal with a parity character** — a mod-10 automaton
(base-5 digits × the mod-2 part of the level), not five constant
matrices: the level's factor 2 twists the Frobenius at 5.  Every
"exception window" of §8 is a state where a unit is killed (e.g.
n = 11 = 21₅: r=1 from even n=2 kills B̃'s unit — matching the observed
e₅ deficiency exactly).  Sol's prediction that the windows are the
automaton is confirmed; the extension entry (the η₅ Sol expects in the
lower-triangular slot) is invisible mod 5 at this normalization —
[OPEN, next depth: the same measurement mod 25].  All [VERIFIED n≤60];
proof route unchanged (forced recurrence for the descent; U₅ for
source-invariance).

---

## 10. Sol's connection-kernel program (X-1) and the Fricke-forced branch obstruction (eleventh arc)

Sol (share 6a733361-…) closed the remaining gcd loophole THEMSELVES by
direct computation on our Domb apparatus (no exponential common divisor
of d_n³A_n and d_n³B*_n: the gcd rate decays 0.57 → 0.12 by n = 150;
effective denominator cost → e^{2.8+}, i.e. κ = 3 stands), and proposed
the next-generation scanner: rank by Δ = log(decay) − κ; search for
(1) higher-order/multi-point vanishing at ALL dominant singularities,
(2) multi-companion rational combinations, (3) positive-density
character-dependent deflation (the only kind that changes κ),
(4) integral-coordinate optimization of 𝒥 = log|t_c'/t_c| − κ(t),
(5) integral pullbacks.  Boxed:

> **X-1: find a nonzero rational integral source in ker 𝒞_{1/4} within
> a larger Fricke-odd source space** (weakly holomorphic, poles confined
> to the t = ∞ cusp; or higher-level oldspaces), with the critical-
> period functional nonvanishing.

**Obstruction sketch (this session, to be made rigorous next):** on the
Domb curve X-1 is EMPTY.  Every meromorphic Fricke-odd weight-4 source
is f*·g(u) with g rational in the Fricke-EVEN hauptmodul u (odd/odd =
even; the odd line is 1-dimensional over the even function field).  The
conjugate singularity t' = 1/4 is itself an AL fixed point, so
u − u(1/4) ~ (t − 1/4)²: g contributes only integer powers of
(t − 1/4)² and can never cancel the half-integer branch of
R = t·g/√(1−4t).  Killing the branch forces g ∝ √(1−4t)·(rational),
i.e. the source into the Eisenstein line Φ_α·(rational) — which kills
the cuspidal functional.  **The branch is Fricke-forced: on any family
whose BOTH singular values are AL-elliptic points (all our winners and
near-winners: levels 5, 6, 12), source-side cancellation at the
conjugate singularity is impossible without killing the L-value.**

**The escape this identifies (next campaign's charter):** families whose
conjugate singularity is a CUSP value of t (not an elliptic point).
There, vanishing conditions at the bad cusp are LINEAR conditions on
q-expansions in a weakly-holomorphic space of unbounded dimension —
higher-order cancellation is available, and the error can be pushed to
the next singularity.  The scanner's next target list: rectified
families with (real AL fold) × (conjugate singularity at a cusp) ×
(odd cusp forms ≠ 0).  [OPEN X-2; nothing scanned yet.]

---

## 11. X-1 EXECUTED: empty, now by exact computation (twelfth arc)

Script `work/z5eps/eps66_x1.py` (+ `eps66.log`), all series exact to
q^96.  The eleventh-arc obstruction sketch is upgraded to a computed
theorem on the Domb curve — with one geometric correction.

**The corrected geometry.**  t_alpha is W₁₂-INVARIANT (measured: max
residual 1.5e-28 over 4 points of the imaginary axis): t is a hauptmodul
of the FRICKE QUOTIENT X₀(12)/W₁₂, not of X₀(12).  The sketch's "even
hauptmodul u" is t itself.  The covers are generated by
s := √(1−4t) and s₂ := √(1−16t); s = Φ_α/f* is an exact ratio of two
Γ₀(12)-forms, hence an honest function on X₀(12), vanishing simply over
t = 1/4 — so t − 1/4 = −s²/4 has a DOUBLE zero in the upstairs
coordinate.  [The sketch's u−u(1/4) ~ (t−1/4)² becomes this identity.]
f* and Φ_α are both W₁₂-odd (measured to 1e-28; f* also proved, §8 of
D1 ledger).

**The computed apparatus.**
* Source identity: I_{f*} := L_α(F θ⁻³f*) = t·ΣC(2m,m)tᵐ = t/√(1−4t),
  exact to q^96.  I_Φ = t exactly, Φ := f*·√(1−4t).
* **Φ_α is PURE EISENSTEIN, explicitly:**
  Φ = (1/240)E₄(q) − (17/240)E₄(q²) − (3/80)E₄(q³) + (1/15)E₄(q⁴)
    + (51/80)E₄(q⁶) − (3/5)E₄(q¹²),  residual zero to q^96.
* The connection map S ↦ I_S is POINTWISE multiplication by t/Φ
  (Q(t)-linear), so S = (I_S/t)·Φ inverts it.

**The branch table (exact, all at coefficient degree 2).**  Every
weight-4 source decomposes w·I_S = a + b·s + c·s₂ + d·s·s₂ with
polynomial coefficients; b or d ≠ 0 ⇔ irremovable branch at t' = 1/4
(4⁻ⁿ error floor); c or d ≠ 0 ⇔ singular at the fold (functional
destroyed).  Results:
* f₆(q):  a = c = 0, b = t(16t−1), d = −t  — branch at BOTH points;
* f₆(q²): a = c = 0, b = t(1−16t), d = −t  — likewise;
* f*:     (4t−1)I = t·s, i.e. pure s  — branch at 1/4 only (the
  L(f₆,3)/2 apparatus, error 4⁻ⁿ, as measured in D-1);
* all five E₄-differences: b ≠ 0 AND c ≠ 0 — worse;
* f₆(q⁴) (level-24 oldspace probe): NOT in Q(t)[s,s₂] up to deg 14 —
  higher-level oldspaces leave the level-12 AL tower entirely (their
  branch analysis belongs to a different curve: X-2's domain).

**Local exponents** of L_α at t = 1/4 AND t = 1/16: {0, 1/2, 1}
(computed indicial polynomials).  Hence any s-content in I_S forces
particular-solution branch terms (t−1/4)^{m+3/2} with NO resonance:
coefficient decay exactly 4⁻ⁿ·poly — higher-order vanishing at 1/4
improves only the polynomial factor, never the rate.  ker 𝒞_{1/4}
(= sources whose companion beats 4⁻ⁿ) within fold-regular sources is
exactly {b = c = d = 0} = {I_S rational} = **Φ_α·Q(t): the Eisenstein
line** (pointwise inversion; poles-at-t=∞ refines Q(t) to Q[t]).

**The critical-period functional vanishes on the kernel** [PSLQ,
error < 1e-60, n ≤ 300 recurrence]:
* control f*: ξ = L(f₆,3)/2 reconfirmed (relation (2,0,0,−1));
* Domb principal Φ: ξ = 7ζ(3)/24 reconfirmed;
* kernel element Φ·t (I = t²): ξ = (7ζ(3)−6)/384 — pure Eisenstein
  class, L(f₆,3)-coefficient EXACTLY 0 in the 4-term PSLQ.

**Verdict: X-1 is EMPTY on the Domb curve** — every fold-regular source
killing the conjugate-singularity branch lies on the Eisenstein line
Φ_α·Q[t], where the cuspidal functional vanishes identically.  The
branch is Fricke-forced exactly as sketched, with the mechanism now
exact: s ∈ Q(X₀(12)) vanishes at the AL-elliptic point over t' = 1/4,
so cuspidal sources (odd line f*·Q(t,s₂)-side) always carry odd
s-powers in I.  Evidence labels: series identities exact to q^96;
parities/invariance numeric 1e-28; ξ-classes PSLQ 60 digits; the
"no other escape" clause rests on the (Z/2)² field structure
Q(X₀(12)) = Q(t, s, s₂-side), verified generator-by-generator at deg 2
but not abstractly proved.  [X-1 CLOSED; X-2 (conjugate singularity at
a cusp) is the surviving charter, unchanged.]

---

## 12. X-2 STEP 1 EXECUTED: the cells exist — and a NEW obstruction (thirteenth arc)

Sol's X-2 algorithm (share 6a733a57) step 1 executed exactly:
`work/z5eps/eps67_x2_scan.py` (grid pass) + `eps68_x2_exact.py`
(exact AL-fixed-point enumeration by matrices, PSLQ algebraic
identification, PARI dimensions/AL matrices), logs `eps67/68.log`.
New instrument: cusp VALUES of t computed for every level
(multiplier-tracked eta reduction), separating cusp obstructions
(killable: linear conditions in weakly-holo spaces) from elliptic
obstructions (X-1's Fricke-forced branch, unkillable).

**Method validation:** level 6 reproduces Apéry exactly (fold and
barrier = roots of 1−34t+t², the γ operator's own P). Level 10's
"boundary curiosity" RESOLVED: the unit-circle conjugate class is
t' = 1 EXACTLY and ELLIPTIC — the sixth-arc boundary score of
precisely e³ is an algebraic identity, and the obstruction is
Fricke-forced: level 10 closed for good.  (Its true W₁₀ pair is
9∓4√5 with a critical value at t=1 in between.)

**THE X-2 CELLS EXIST.**  In the standard eta normalizations,
exactly two levels have (AL fold) < (cusp obstruction) < (elliptic
barrier) with the barrier beating a race threshold:

| N | fold | cusp obstruction | elliptic barrier | score₃ | score₂ | S₄⁻ | S₃(N,χ) |
|---|---|---|---|---|---|---|---|
| 12 | 7−4√3 (t²−14t+1) | t = −1 (cusps 1/2, 1/6) | 7+4√3 = 13.93 | 1.44 NEAR-MISS | **0.53 WIN** | 1 (f*) | dim 1 (χ₋₃), dim 2 (χ₋₄) |
| 18 | 5−2√6 (t²−10t+1) | t = e^{±iπ/3} (4 cusps) | 5+2√6 = 9.90 | 2.03 | **0.75 WIN** | 2 | dim 2 (χ₋₃) |

Levels 5, 6, 8, 9, 14, 15, 16, 20, 21, 24: no cell (elliptic barrier
first, or barrier below both thresholds).  Level 16 checked
separately: barrier (1+√2)/2, no intermediate cusp value.

**The new obstruction (odd-weight AL irrationality).**  The r=2 wins
need a weight-3 source with character vanishing at the AL fold over ℚ.
Exact AL matrices (PARI): on S₃(12,χ₋₄): W₁₂ = [1,−4;−1/2,−1] with
M² = 3·Id — eigenvalues ±√3; on S₃(18,χ₋₃): W₁₈² = 6·Id (±√6), and
every partial AL likewise irrational (±i√2, ±√3).  Measured fold
values: f₁/f₀(τ₁₂) = −2(√3−1) exactly — the vanishing combination
lives in ℚ(√3), not ℚ.  The D-1 oldspace escape is closed here:
S₃ = 0 at every proper level below 12 and 18 (all-new spaces, no
rational AL-swap pairs).  The dim-1 space S₃(12,χ₋₃) has pseudo-
eigenvalue i and does NOT vanish at the fold (0.1500, tautological
fixed-point identity).  **Odd weight makes AL pseudo-eigenvalues
±√Q ∉ ℚ: rational fold-vanishing fails in both cells.**  This is
structurally new — X-1's obstruction was character-theoretic
(branch ⇔ cuspidal projection); this one is Galois-theoretic.

**What survives (for Sol):**
1. **The ℚ(√Q)-descent question:** the vanishing combination exists
   over ℚ(√3) (level 12) / ℚ(√6) (level 18); both Galois-conjugate
   apparatuses exist simultaneously.  Does a trace/norm construction
   (companion pair over the real quadratic field, d_n²-integrality in
   O_K) yield ℚ-irrationality of the CM L-value?  Nothing in the X-1
   obstruction forbids it.
2. **The r=3 near-miss at level 12:** the SAME f* on the t₁₂ =
   (η₁η₁₂/η₃η₄)⁴ family (weight-4, trivial character: AL rational,
   fold-vanishing works!) has barrier 13.93: score 20.09/13.93 = 1.44.
   Needs denominator exponent κ < ln 13.93 = 2.634 to win; measured
   asymptotic κ = 3 (§7) — loses by exactly the generic-prime cost.
   Sol's step 6 on this apparatus would quantify the margin; any
   mechanism shaving 0.37 off κ (character-dependent deflation, the
   only kind that changes κ, §10) flips it.
3. Whether the cusp obstruction at t = −1 vanishes automatically for
   cusp-form sources (Eichler integrals regular at cusps) — if yes,
   steps 2–4 of the algorithm are free at level 12 and the whole
   question is (1)/(2)'s arithmetic.  [UNTESTED]

Evidence labels: obstruction values exact-algebraic [PSLQ 30 digits +
matrix enumeration]; AL matrices exact [PARI]; fold values numeric
40 digits; cusp values numeric, cross-checked at two offsets; the
t₁₂-family apparatus itself NOT yet constructed (no step-6 data).
[X-2 STEP 1 CLOSED: cells found at 12, 18 (r=2); blocked by the
odd-weight AL obstruction pending Sol's review of (1)–(3).]

---

## 13. X-2A/X-2B EXECUTED: the parity law, the norm route dead, the cusp-limited L(f₆,3)/2 apparatus (fourteenth arc)

Sol's dual directive (share 6a734412: X-2A restriction-of-scalars norm
criterion ρρ^σ > e^{2κ}; X-2B character-density denominator scan)
executed: `work/z5eps/eps69_x2a.py`, `eps70_x2b.py` + inline runs
(`eps69/70/70b/70c.log`).  All series exact to q^420 (PARI); numerics
420–440 digits.

**Preliminary (new exact facts).**  On the t₁₂ = (η₁η₁₂/η₃η₄)⁴ family:
R = f₁/f₀ at the fold = 2−2√3 EXACTLY [PSLQ 45 digits]; at the
conjugate AL point R' = 2+2√3 = σ(R) [43 digits] — Sol's Galois
prediction verified.  Hence the ℚ-rational weakly-holomorphic source
v = (t−3)f₀ − 2f₁ (pole order 1 at the t=∞ cusps) vanishes at BOTH
AL-elliptic points (rational fold conditions are Galois-forced at the
conjugate).

**The parity law (the arc's discovery, measured three ways).**  Branch
regularity of I at an AL-elliptic point is NOT a vanishing condition —
it is a LOCAL PARITY condition: every factor of I = P·F·S/σ³ carries a
definite parity under the local involution (t even, σ odd), and the
branch dies iff parity(F)·parity(S) matches.  Local parity = global
AL-eigencomponent; in odd weight the eigencomponents are irrational
(±√Q pseudo-eigenvalues, §12) — for the SOURCE and for F alike:
* rational v (vanishing at both AL points!): fold-stuck,
  |Λ_n| ~ 13.93ⁿ·n^{-5/2} — value-vanishing regularizes nothing;
* K-eigenvector s = f₀+((1+√3)/4)f₁, BOTH embeddings (Sol's table):
  fold-stuck identically (ρ_id ≈ ρ^σ ≈ 1; the weight-1 F = θ₃² is
  itself parity-impure, so no source choice can help);
* r=3 with parity-matched F: see below — fold branch KILLED.
**X-2A verdict: the norm criterion fails as measured
(ρ_id·ρ^σ ≈ 1 ≪ e⁴ = 54.6), and the parity law explains why the
odd-weight cells cannot be regularized by any ℚ- or K-rational source
with a rational F.**  [Escape not yet excluded: a parity-pure K-valued
F-pair (F, F^σ) realizing Sol's asymmetric table ρ_id = 13.93, ρ^σ = 1
— product 13.93 < 54.6 still fails the κ=2 norm criterion, so the
route is dead unless κ_norm < 1.32.]

**The r=3 apparatus WORKS when parity is matched (even weight —
rational).**  F_odd = 12E₂(q¹²)−E₂(q) (weight 2, W₁₂-odd), source f*:
* fold branch DEAD: |Λ_n| local base → 1.00 from above — the error is
  CUSP-LIMITED at t = −1: |Λ_n| ~ n^{-c}, exactly the predicted
  step-2/3 geometry (Sol's Q3 answered: the cusp obstruction is real —
  a period defect survives the vanishing source);
* ξ = L(f₆,3)/2 EXACTLY (30+ digits) — same functional as the Domb
  apparatus on a different curve: pipeline validation and a second
  member of the D-2 family;
* d_n³·B_n ∈ ℤ (n ≤ 414) — the integrality layer holds on the third
  curve in a row;
* **X-2B answered: NO character-split deflation.**  e_p(n) = 3h_p(n)
  for 36/37 primes with χ₁₂(p) = +1 AND 40/41 with χ₁₂(p) = −1
  (deflation only at level primes, as in §7).  κ → 3; Sol's needed
  density-0.366 saving is absent.  The r=3 near-miss stays a miss.

**Program state.**  What survives of X-2 at level 12:
kill the t = −1 cusp period defect (finitely many linear period
conditions, Sol's steps 3–4) → |Λ_n| ~ 13.93^{-n}, the strongest
cuspidal apparatus yet (beats Domb's 4^{-n}) — but the race still
needs κ < 2.634 vs measured κ → 3.  Both X-2 routes now reduce to the
same single question that closed every previous arc: **a denominator
mechanism below e³ for cuspidal companions.**  The geometric program
(X-1, X-2 steps 1–5) is complete; the obstruction ledger is:
interior branch (X-1, character-theoretic) — parity/Galois (odd
weight, this arc) — denominator exponent (arithmetic, open).
Evidence labels: R-values PSLQ 43–45 digits; parities/bases measured
420 digits, 420 exact coefficients; e_p exact factorization at n=414;
no proofs.
