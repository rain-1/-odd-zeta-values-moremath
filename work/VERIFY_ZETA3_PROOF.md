# Hostile referee report — WARMUP_ZETA3_DWORK.md, T2 & T3

**Referee:** verification-agent (hostile stance)
**Date:** 2026-07-24
**Target:** `/home/ubuntu/fable-episode-2/zeta-math-2/work/WARMUP_ZETA3_DWORK.md`, sections
"T2 [PROVED]" and "T3 [PROVED, single-digit]".
**Method:** independent Mathematica implementation of a_n, b_n (NOT copied from the file),
exact rational arithmetic, every lemma re-derived by hand and checked termwise on all cells.

---

## VERDICT

- **T2 (a-row Lucas, a_{ap+r} ≡ a_a·a_r mod p, all a≥0): CONFIRMED.**
- **T3 (b-row Lucas, p³·b_{ap+r} ≡ b_a·a_r mod p, p≥5, 1≤a<p, 0≤r<p, single-digit): CONFIRMED.**

No counterexample found. No logical gap found. Every lemma is correct on its own terms.
Three steps are correct but terse ("one more sentence" issues) — listed at the end. None
affects validity.

Scope note (respected, not a complaint): T3's [PROVED] label is explicitly single-digit
(1≤a<p). The multi-digit / mod-p³ master forms are labeled [VERIFIED, not PROVED] in the
file and were NOT part of this referee pass.

---

## What I independently re-derived and confirmed

### Setup (independent implementation)
- a_n = Σ_k C(n,k)²C(n+k,k)² — reproduces A005259 (1,5,73,1445,33001,819005).
- b_n = Σ_k C(n,k)²C(n+k,k)²(H₃(n)+Σ_{m=1}^k (−1)^{m−1}/(2m³C(n,m)C(n+m,m))).
  Verified b_n/a_n → ζ(3) with the correct ~10^(−3n) convergence, so my b_n is the standard
  companion (normalization unambiguous).

### T2 — every piece checked, 0 failures
| Claim | Range checked | Result |
|---|---|---|
| Theorem a_{ap+r}≡a_a a_r | p∈{5,7,11,13}, a∈0..2p (incl. multi-digit), r∈0..p−1 | 0 fails |
| Lemma 3 factorization A(n,k)≡[r+s<p]C(a,b)²C(a+b,b)²C(r,s)²C(r+s,s)² | p∈{5,7,11,13}, all a≤2p, all b,s | 0 fails |
| First factor Σ_b C(a,b)²C(a+b,b)² = a_a (exact integer identity) | a≤20 | all True |
| Second factor Σ_{s:r+s<p}C(r,s)²C(r+s,s)² ≡ a_r | p≤19, all r | 0 fails |
| Deleted terms of a_r (s≤r, r+s≥p) ≡ 0 mod p | p≤19, all r | 0 fails |
| Product-region extra terms (b=a, s>r, r+s<p) vanish | verified C(r,s)=0 for all such | 0 nonzero |

**The product-region factorization (protocol item v) is legitimate.** The true (b,s) region is
NOT a product set — at b=a the s-range is restricted to s≤r by k≤n. But the extra terms added to
complete the product {0≤b≤a}×{s:r+s<p} all have b=a, s>r, hence C(r,s)=0 and vanish mod p.
Product region ⊇ true region, difference vanishes ⟹ sums equal mod p. Airtight. The Lemma 2
carry-annihilation r+s≥p ⟹ 0 case is correct (C(r+s−p,s)=0 since r<p ⟹ r+s−p<s).
Multi-digit induction: two-digit statement holds for ALL a≥0 (checked to a=2p), so full Lucas
follows. Correct.

### T3 — every lemma and case split checked, 0 failures
| Claim | Range checked | Result |
|---|---|---|
| Theorem p³b_{ap+r}≡b_a a_r | p∈{5,7,11,13,17}, all (a,r); both sides p-integral | 0 fails |
| Identity b_n = H₃(n)a_n + W(n) | n≤10, exact | all True |
| Interchange W(n)=Σ_{m=1}^n c(n,m)T(n,m), T(n,m)=Σ_{k=m}^n A(n,k) | via b_n identity | exact |
| (T-fact) m₀>r ⟹ T(n,m)≡T(a,m₁+1)a_r | p∈{5,7,11}, all (a,r), all m | 0 fails |
| (T-fact0) T(n,jp)≡T(a,j)a_r | p∈{5,7,11}, all (a,r,j) | 0 fails |
| (Tvanish) a+j≥p ⟹ v_p T(a,j)≥2 | p∈{5,7,11}, all (a,j) | 0 fails |
| Kummer v_p C(n,m)=[m₀>r] | p∈{5,7,11,13}, all p∤m | 0 fails |
| Kummer v_p C(n+m,m)=c₀+c₁ | p∈{5,7,11,13}, all p∤m | 0 fails |
| (Lemma V) v_p(p³c(n,m)T(n,m))≥1 for p∤m | p∈{5,7,11,13}, all p∤m | min = exactly 1 |
| Lemma V rescue: v_p(CC)=3 ⟹ m₀>r AND v_p T(n,m)≥1; and v_p(CC)≤3 | p≤19, 14292 CC=3 cases | 0 fails |
| H-part p³H₃(n)≡H₃(a) mod p³ | p∈{5,7,11,13}, all (a,r) | 0 fails |
| H-part reduction p³H₃(n)a_n≡H₃(a)a_a a_r mod p | p≤17, all (a,r) | 0 fails |
| term_j ≡ a_r τ_j mod p | p∈{5,7,11,13}, all (a,r,j) | 0 fails |
| case a+j≥p: v_p τ_j = v_p T(a,j)−v_p C(a+j,j)≥1, τ_j≡0 | p≤17, all such (a,j) | 0 fails |
| case a+j≥p: v_p C(n,jp)=0, v_p C(n+jp,jp)=1, v_p T(n,jp)≥2, term_j≡0 | p≤17 | 0 fails |
| W-part p³W(n)≡a_r W(a) mod p | p∈{5,7,11,13}, all (a,r) | 0 fails |
| W(a)=Σ_{j=1}^a τ_j (exact) | a≤25 | all True |

**Lemma V is the load-bearing step and it is sound.** The valuation
v_p(p³cT)=3−v_p(CC)+v_p T with v_p(CC)≤3. The only dangerous case v_p(CC)=3 forces
[m₀>r]=c₀=c₁=1 (I confirmed this on all 14292 occurrences, and v_p(CC) never exceeds 3),
which puts us in the m₀>r regime where (T-fact) gives T(n,m)≡T(a,m₁+1)a_r, and m₁+1≥p−a makes
every surviving b satisfy a+b≥p ⟹ A(a,b)≡0 ⟹ T(a,m₁+1)≡0 ⟹ v_p T(n,m)≥1. Rescue holds
termwise. The perfect-square summand (v_p A ≥ 2 per single Kummer carry) is exactly the slack
that closes both Lemma V's dangerous case and the a+j≥p case (v_p T(n,jp)≥2). This matches the
file's own caveat (T4c) that the weight-5 port loses this factor of 2.

**Boundaries probed (protocol item i):** r=0, r=p−1, a=1, a=p−1, and all internal
m=n, m=jp with j=a, s=0, k=0 are covered by the exhaustive sweeps above (all pass). The
b=a boundary inside T-fact/T-fact0 is handled by the same C(r,s)=0 vanishing as T2 (verified).
The k=0 term of W drops out (empty inner sum). Reflection-symmetric depth boosts
E(corner (p−1,p−1))=6, E(edge (p−1,0))∈{4,5,6} reproduced.

**p=5 is not special (protocol/file claim confirmed).** For p=5, a_a≡0 mod 5 at a∈{1,3}
(a_1=5, a_3=1445). T3 in integer form p³b_n≡b_a a_r mod p passes at ALL these pole cells
(a∈{1,3}, all r) with 0 failures — because the proof never divides by a_a. The ratio-form pole
is a division artifact, exactly as the file states.

---

## Under-justified (correct, but each needs one more sentence to be referee-proof)

1. **Lemma V, "v_p C(n,m) ≤ 1".** The write-up justifies the single-borrow bound with
   "the second borrow would need m₁=a with m₀>r, i.e. m>n". Correct, but it silently uses the
   step: for m≤n with m₀>r, necessarily m₁≤a−1 (else m=m₁p+m₀ = ap+m₀ > ap+r = n). Spelling out
   "m₀>r ⟹ m₁≤a−1 ⟹ a−m₁−1≥0, no second borrow" would close it.

2. **Product-region factorization reused inside (T-fact)/(T-fact0).** The write-up proves the
   product-set argument carefully for T2, then in the bracketed T-fact/T-fact0 justifications
   ("the b-sum gives T(a,m₁+1), the s-sum gives a_r" / "same, now b≥j survives") reuses it
   without re-noting that at the top boundary b=a the extra s>r terms vanish by C(r,s)=0 — i.e.
   that the (b,s) region is again only a product set *after* adding vanishing terms. It is the
   identical mechanism as T2 and is correct, but one sentence importing the T2 argument into the
   T-fact context would make it self-contained.

3. **The interchange defining T(n,m).** W(n)=Σ_k A(n,k)Σ_{m=1}^k c(n,m) = Σ_m c(n,m)Σ_{k=m}^n A(n,k)
   is asserted directly. Correct (the k=0 term has an empty inner sum and drops; the swap is over
   1≤m≤k≤n). A half-sentence noting the k=0 vanishing and the swap region would satisfy a referee.

None of these three is a gap in the logic; each is a compression. The mathematics is complete.

---

## Bottom line
Both proofs survive a hostile pass. T2 = CONFIRMED, T3 (single-digit) = CONFIRMED, at the
stated scope. Independent exact-arithmetic verification: 0 failures across every theorem,
lemma, case split, Kummer count, and boundary, for p up to 17–19. The three flagged steps are
terse but correct.
