# Orchestrator notes — session 2026-07-24 (Fable)

Exact Mathematica computations by the orchestrator (kernel session b2au6FKe).
Everything here is [VERIFIED] on the stated finite ranges — evidence, not proof.

## 0. Context

Prior campaign (../zeta-math, 2026-07-16..20) reduced the sharp-12 denominator
law for the Brown–Zudilin ζ(5) family (p ≥ 5 part) to one gate:

    (DWORK)  p^5 (P_n/Q_n) ≡ P_a/Q_a (mod p),  a = ⌊n/p⌋,

verified there over 272 descents, floor mod p^{2−κ}, κ = ord_p C(2n,n);
proved: the a=1 midpoint band theorem + Q-row Lucas Q_{ap+r} ≡ Q_a Q_r (p).
Open: cubic gate ≡ the P-column of the one-digit Frobenius connection matrix.

## 1. The weight-3 discovery (this session)

For the classical Apéry ζ(3) pair (a_n, b_n):

    p^3 (b_n/a_n) ≡ b_a/a_a  (mod p),   a = ⌊n/p⌋

[VERIFIED p = 7, 11, 13; a = 1, 2; all r; depth v_p(p³b/a − b_a/a_a):
typically 3, boosts to 4, dip to exactly 2 at the reflection center
r = (p−1)/2]. p = 5 exceptional: a_1 = 5 ≡ 0 (5) degenerates the ratio
(ord as low as −1 at (a,r) = (2,1)). Equivalent Lucas-type form (via Gessel
Lucas for a_n):  p^3 b_{ap+r} ≡ b_a · a_r (mod p).

This is the exact weight-3 template of (DWORK). Agent sweep extending this
(all p ≤ 31, n ≤ ~320, iterated digits, exact depth law, integer-normalized
p=5 statement) → work/WARMUP_ZETA3_DWORK.md.

## 2. The weight panel: descent depth scales with weight

Same experiment on lower-weight Apéry-like pairs.

Weight 2 (Apéry ζ(2) pair, recurrence (n+1)²u_{n+1} = (11n²+11n+3)u_n + n²u_{n−1},
A: 1,3,…, B: 0,5,…; B/A → ζ(2), checked to 59 digits):

    v_p(p² B_n/A_n − B_a/A_a):  clean floor 2 at ALL residues EXCEPT the
    center r = (p−1)/2, where the behavior splits by p mod 4:
      p ≡ 1 (4):  BOOST (p=5: 5,8; p=13: 5)
      p ≡ 3 (4):  COLLAPSE TO 0 (p=7, 11) — the naive mod-p statement FAILS
    Quadratic-character (Euler-number?) fingerprint at the center.
    Exceptional digit confirmed: p=7, a=3 fails wholesale since 7² | A₂(3)=147.

Weight 1 (log 2, central Delannoy A: 1,3,13,63,… with companion; B/A → log 2,
59 digits): floor barely 1; center fails at p = 7 (0) and p = 11 (−1);
sporadic dips to 0 elsewhere (p = 13 at r = 2, 10). Exceptional digits again
textbook: (p=7, a=3): 7 | 63; (p=13, a=2): 13 = A(2); (p=3, a=1): 3 | 3.

Conclusions for the program:
(i) the ratio descent is a HIGH-WEIGHT phenomenon — usable slack ≈ w − (small
corrections); at w = 3, 5 the mod-p floor needed by (DWORK) has ≥ 1 digit of
margin; at w = 1, 2 corrections poke through, explaining exactly where danger
lives: center residue r = (p−1)/2, exceptional digits (p | A(a)), and κ.
(ii) any correct general theorem must (a) exclude/renormalize exceptional
digits, (b) handle the center residue separately (its correction has
arithmetic content — quadratic character at w = 2), (c) at odd w ≥ 3 the
center dip loses only 1 digit and the statement survives.

## 1b. CORRECTION (post-sweep, 2026-07-24 later)

The §1 "dip to 2 at the reflection center" is superseded: the full sweep
(work/WARMUP_ZETA3_DWORK.md) shows those cells are exactly ratio-form POLE
cells — the center digit value a_{(p−1)/2} ≡ 0 (mod p) for some primes (e.g.
11 | a_5 = 819005), the same center-vanishing seen at weight 2. On unit cells
the ratio depth floor is a flat 3; the universal integer-normalized law is
p³ b_n a_q ≡ b_q a_n (mod p³), q = ⌊n/p⌋, floor exactly 3, all 5 ≤ p ≤ 31,
n ≤ 320, zero failures. Also v_p(b_n/a_n) = −3v_p(d_n) holds only as ≥.

## 2b. The Lucas/product form is the right universal statement

Ratio-form failures at low weight are ALL explained by p | (Lucas factor):
weight-2 center collapse at p ≡ 3 (4) matches the classical fact that the
ζ(2)-Apéry number at n = (p−1)/2 vanishes mod p for p ≡ 3 (4) [RECALLED-
UNVERIFIED as a citation; the vanishing itself is in our data]; exceptional
digits are p | A(a). The product form

    p^w · b_{ap+r} ≡ b_a · a_r  (mod p)

holds at EVERY previously-failing site [VERIFIED: w=2 p=7,11 all a≤3; w=1
p=7,11,13 all a≤3 incl. 13 = A(2); w=3 p=5 a≤3]. Iterated 2-digit version
p^{2w} b_n ≡ b_{n₂}a_{n₁}a_{n₀} holds at p=5, w=3, n=25..70, min depth 1.
FAILS at p = 2, 3 (min ords −6, 0) — true range p ≥ 5, matching (CB)'s
p ≥ 5 and the sharp-12 primes {2,3}.

## 2c. BZ ζ(5) pair: product form verified up to sign, and it implies (CB)

With the prior campaign's exact ladders (lemma_cb_explore.py; P_n = p_n/binom,
Q_n = q_n/binom, note their q_0 = −1 convention):

SIGN RESOLVED (2026-07-24, later): BZ's paper itself (llm/20, the display
identifying with [Zu02]: Q_n = (−1)^{n+1}q_n/binom, P_n = (−1)^{n+1}p_n/binom,
P̂_n = (−1)^{n+1}p̃_n/binom) supplies the missing (−1)^{n+1}. In BZ's printed
normalization (Q_0 = 1, P_0 = 0, Q_1 = 21, P_1 = 87/4, P_2 = 1190161/384 —
anchors match the paper's printed values exactly):

    (LB_5)   p^5 · P_{ap+r} ≡ P_a · Q_r   (mod p)      [uniform PLUS]

[VERIFIED bz_lucas_final.py: n ≤ 45, p = 7,11,13,17,19, ALL cells, worst
depth 1, ZERO failures, INCLUDING exceptional p = 7]. Perfectly parallel to
the proved weight-3 theorem p³b_{ap+r} ≡ b_a·a_r.

RETRACTED: the earlier "Legendre (r|7) sign pattern" at p=7 was numerology
on degenerate cells — {1,2,4} is just the set of r with 7 | Q_r, where both
signs pass and the best-sign detector picked the deeper one. No sign
function exists; the raw-ladder minus was purely the (−1)^{n+1} conversion
((−1)^{a+r−n} = +1 for odd p makes it uniform).

WHY THIS MATTERS: the product form, iterated, gives ord_p(P_n) ≥ −5L
directly (induction: ord(p⁵P_n − εP_aQ_r) ≥ 1 with P_a p-integral at L=1;
scaled version for L ≥ 2), hence ord_p(p_n) ≥ κ − 5L = (CB), for all p ≥ 5,
WITHOUT q-unit hypotheses or the V5.3 exceptional-prime compensation
argument. It is exactly resume-brief target (D) in intrinsic induction shape,
and the exact analogue of the proved Q-row Lucas theorem. The scripts:
scratchpad bz_lucas_form.py, bz_lucas_sign.py (copy into repo when promoted).

## 2d. The graded-weight discovery (2026-07-24, evening) — the crystal made visible

Using the extracted exact BZ ladders to n = 360 (falsify_data/ladder_*.json,
BZ-positive normalization; P̂_1 = 101/4, P̂_2 = 344923/96):

(i) MASTER DEPTH LAW, rank-2 pairs: v_p(p^w b_n a_q − b_q a_n) ≥ w, q = ⌊n/p⌋,
    FLAT, all p ≥ 5: [VERIFIED 0 failures] w = 1 (Delannoy/log2, n ≤ 300),
    w = 2 (Apéry ζ(2), n ≤ 300, floor exactly 2 for p ≥ 7), w = 3 (floor
    exactly 3, earlier). "Congruence depth = motivic weight."

(ii) WEIGHT 5 IS NOT FLAT — and the deviation is exactly the rank-3 grading:
    - P-row single-digit (q < p): floor exactly 1 for p⁵P_n − P_qQ_r,
      [VERIFIED 0 failures, all p ∈ {7..31}, all cells n ≤ 360] — (LB₅) solid.
    - Multi-digit master form dips negative at exceptional primes — pure
      renormalization (P_q not p-integral for q ≥ p); the correct multi-digit
      statement needs p^{5L}-scaled induction, NOT the naive master form.
    - P̂-row (the ζ(3)-graded piece): master form with w = 3 floors at +1
      (+2 at p = 29, 31); w = 2 and w = 4 go NEGATIVE. [VERIFIED single-digit
      cells, p ∈ {11..31}, n ≤ 360.] The middle piece descends with ITS OWN
      weight 3.

INTERPRETATION: the Frobenius of the M̄₀,₈ cellular motive acts on the graded
pieces ℚ(0), ℚ(−3)̂, ℚ(−5) with eigenvalues 1, p³, p⁵, and the digit-descent
congruences are its elementary shadow — one congruence family per graded
piece. Scripts: depth_law.py, graded_test.py (scratchpad).

CORRECTIONS (2026-07-25, from PROOF_LB5_CAMPAIGN.md — authoritative):
(i) Q_n is BZ's DOUBLE sum (Q₁ = 21), NOT ΣC(n,k)²C(n+k,k) = A005258
    (Q₁ = 3) — the warmup T4's port claim used the wrong sequence. Q-row
    Lucas is now PROVED for the correct Q_n (Theorem A, double-carry
    annihilation lemma), upgrading July's 2.19M-summand certificate.
(ii) The middle row's PRODUCT form p³P̂_{ap+r} ≡ P̂_a·Q_r (mod p) is FALSE in
    general: v_p(P̂_a) = −1 for most a ∈ (p/2, p) (the letter H^{(3)}_{n+k}
    reaches argument 2n). Corrected [VERIFIED 0/1768 fails]: holds iff P̂_a
    is p-integral; unnormalized product congruence needs p⁴. My MASTER-form
    measurement (w = 3 floor 1, Q-weighted both sides) stands — the two
    statements differ exactly by the P̂_a poles. Proved floors:
    v_p(P̂_n) ≥ −4 (n < p²), ≥ −1 (n < p), both attained.
(iii) P_n has NO weight-5 harmonic-MONOMIAL decomposition (149-basis
    inconsistent over 165 exact equations): BZ's top period is
    ζ(5) + 2ζ(2)ζ(3) — DEPTH 2 — so w₅ needs nested letters. The impurity
    that exiles the class to the middle ray is the same object blocking the
    elementary decomposition. Also PROVED: (LB₅) ⟺ (W5) (H₅-layer removed,
    Theorem C), Lemma D/D⁺ (the non-square-summand valuation lemma;
    three-carry version FALSE, 649 counterexamples), and P̂_n's explicit
    weight-3 decomposition on the BZ summand (Theorem B, exact-fit verified,
    CT certification pending).

## 3. Jacobian conjecture verification (unrelated but this session)

Alpöge's tweeted map F = ((1+xy)³z + y²(1+xy)(4+3xy), y + 3x(1+xy)²z +
3xy²(4+3xy), 2x − 3x²y − x³z): det JF ≡ −2 exactly; F(0,0,−1/4) =
F(1,−3/2,13/2) = F(−1,3/2,13/2) = (−1/4,0,0); exact Solve: that fiber has
exactly 3 points and a generic fiber also has 3. Étale, generically 3:1 ⇒
Jacobian conjecture is false. [VERIFIED exact]
