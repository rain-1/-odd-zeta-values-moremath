# Warmup: ζ(3) Apéry pair — a (DWORK) descent congruence

**Author:** mathematician-agent (River's zeta-irrationality program)
**Date:** 2026-07-24
**Discipline labels:** `[PROVED]` = complete proof written out; `[VERIFIED n≤N]` = finite exact check (evidence, never proof); `[RECALLED-UNVERIFIED]` = memory, not checked against a source.

## Objects

Apéry numbers for ζ(3):

- a_n = Σ_{k=0}^n C(n,k)² C(n+k,k)²   (integer; OEIS A005259: 1, 5, 73, 1445, 33001, …)
- b_n = Σ_{k=0}^n C(n,k)² C(n+k,k)² ( H^{(3)}_n + Σ_{m=1}^k (−1)^{m−1} / (2 m³ C(n,m) C(n+m,m)) ),  where H^{(3)}_n = Σ_{m=1}^n 1/m³.

b_n/a_n → ζ(3).

## Working conjecture (Lucas / (DWORK) form)

For p ≥ 7, 0 ≤ r < p, 1 ≤ a < p, with n = ap+r:
- (Lucas, a-row):  a_{ap+r} ≡ a_a · a_r (mod p).
- (Lucas, b-row):  p³ · b_{ap+r} ≡ b_a · a_r (mod p).
- (ratio form):    p³ · (b_n/a_n) ≡ b_a/a_a (mod p).

---

## EXECUTIVE SUMMARY

**Depth law (single-digit, integer-normalized E = v_p(p³ b_n a_a − b_a a_n), min over all cells):**

| p | min E (floor) | E-value tally over single-digit cells (E: count) |
|---|---|---|
| 5 | 3 | 3:18, 4:1, 6:1 |
| 7 | 3 | 3:35, 4:5, 5:1, 6:1 |
| 11 | 3 | 3:104, 4:4, 6:2 |
| 13 | 3 | 3:147, 4:7, 5:1, 6:1 |
| 17 | 3 | 3:260, 4:10, 5:1, 6:1 |
| 19 | 3 | 3:302, 4:35, 5:4, 6:1 |
| 23 | 3 | 3:478, 4:25, 5:2, 6:1 |
| 29 | 3 | 3:774, 4:35, 5:2, 6:1 |
| 31 | 3 | 3:912, 4:16, 5:1, 6:1 |

Floor is a FLAT **3** (independent of κ = v_p C(2n,n)); typical 3; sporadic reflection-symmetric boosts to
4/5/6 at extreme digits (corner (p−1,p−1)→6, edge (p−1,0)→5). Same floor 3 in the multi-digit range.

**Status of statements.**
- **[PROVED]** a-row Lucas a_{ap+r} ≡ a_a a_r (mod p), all a≥0, 0≤r<p, all primes (T2).
- **[PROVED]** b-row Lucas p³ b_{ap+r} ≡ b_a a_r (mod p), all p≥5, 1≤a<p, 0≤r<p (T3, single-digit,
  self-contained; repairs p=5 without dividing by a_a).
- **[VERIFIED, 0 failures, 5≤p≤31, n≤320]** master integer form p³ b_n a_q ≡ b_q a_n (mod p³),
  q=⌊n/p⌋ (single + multi-digit, incl. p=5), depth floor 3. **Proof open** (mod-p³ boost & multi-digit
  induction); Dwork-crystal route indicated.
- **[VERIFIED]** integrality v_p(b_n) ≥ −3 v_p(d_n); exact iterated law v_p(b_n/a_n) = −3 v_p(d_n) is FALSE.
- **p=5 anomaly** fully characterized: ratio form p³ b_n/a_n ≡ b_a/a_a develops a pole exactly when
  a_a ≡ 0 (mod p) (a base-p digit of a hits a zero of a_·: r∈{1,3} for p=5); the integer forms have no pole.

**Literature verdict.** a-row = classical (Gessel 1982; Straub arXiv:2301.12248 → 15 sporadic integer
sequences mod p²). b-row harmonic-weighted descent **not located** in surveyed sources (Straub 2301.12248 and
Apéry-Limits arXiv:2011.03400 both fetched; neither states it); Beukers 1985/1987 prove a DIFFERENT
(endpoint mpʳ−1) supercongruence family. Our T3 is proved from scratch.

**Most important sentence for the weight-5 port:** the elementary ζ(3) proof ports for the integer row Q_n,
but the harmonic row P_n has no order-3/rank-3 analog of Apéry's single-sum b_n = H₃·a_n + W, so the port's
real work is finding the weight-5 harmonic decomposition of P_n (with mixed-weight P̂_n cross-terms) and
redoing the Kummer ledger for the p⁵ pole with the non-square summand — cleanest via a rank-3 Dwork crystal.

---

## Progress log

### T1 results (single-digit range n = ap+r, 1≤a<p, 0≤r<p)

Notation: aa[n]=a_n, bb[n]=b_n exact rationals (memoized, incremental innerSum). Helpers
`vp[x,p]` = v_p(num)−v_p(den); `redp` reduces a p-integral rational mod p.
D(a,r) := v_p( p³ b_n/a_n − b_a/a_a )  (ratio form; a_a,a_n must be p-units).
E(a,r) := v_p( p³ b_n·a_a − b_a·a_n )  (integer-normalized; always defined).
κ(a,r) := v_p C(2n,n).

**[VERIFIED, all primes 5≤p≤31, all n≤320]**
- **a-row Lucas** a_{ap+r} ≡ a_a·a_r (mod p): 0 failures (all p incl. 5; single- AND multi-digit).
- **b-row Lucas (single-digit) p³ b_{ap+r} ≡ b_a·a_r (mod p): 0 failures, INCLUDING p=5.**
  (Both sides genuinely p-integral for n<p²; no spurious matches.)

**[VERIFIED, all primes 7≤p≤31, single-digit unit cells]** Depth (ratio form):
- min D = **3** for every prime; NO cell has D≤2. Typical D=3, rare boosts to 4,5,6.
- Center D(1,(p−1)/2)=3 (pole for p=11 since a_5≡0 mod 11 ⇒ a_16≡0).
- **This REVISES the orchestrator's recalled "floor 2 / dip to 2 at center": the true floor is 3.**
  Direct check p=7,a=1: D(r=0..6)=[3,4,3,3,3,4,3]; r=3 (center) gives 3, not 2.
  My b_n is pinned by b_n/a_n − ζ(3) ≈ −2·10⁻⁶¹, so the normalization is unambiguous.
- Hence the true congruence is the STRONGER **p³ b_n/a_n ≡ b_a/a_a (mod p³)** on unit cells.

**[VERIFIED, all primes 5≤p≤31 INCLUDING p=5, ALL single-digit cells (incl. poles)]**
Integer-normalized floor: **E = v_p(p³ b_n a_a − b_a a_n) ≥ 3, minimum exactly 3.** Zero failures.
  → clean law: **p³ b_{ap+r}·a_a ≡ b_a·a_{ap+r} (mod p³)** for 5≤p, 1≤a<p, 0≤r<p.
  The task's suggested "E ≥ v_p(a_a a_n)+1" is FALSE (E−v_p(a_a a_n) reaches −2 at p=17).
  E-tally per prime: overwhelmingly 3, a handful of 4, one 5 and one 6 per prime.

**The p=5 anomaly, precisely.** a_r ≡ 0 (mod p) occurs for r∈{1,3}(p=5), {5}(p=11), {3,13}(p=17),
{8,10}(p=19), {8,22}(p=31); none for p=7,13,23,29. Reducing the mod-p³ law mod p gives
a_a·(p³ b_n − b_a a_r) ≡ 0 (mod p). When a_a is a p-unit (p≥7, no zero digit) this yields the
reduced b-row p³ b_n ≡ b_a a_r (mod p). When a_a ≡ 0 (mod p) — always for p=5 at a=1,3, and
whenever a base-p digit of a hits a zero of a_· — the factor a_a annihilates the reduction and
the *ratio* form b_a/a_a develops a pole (ord as low as −1). Only the a_a-weighted integer form
p³ b_n a_a ≡ b_a a_n (mod p³) survives, and it does so with zero failures for p=5 too.

### T1 MASTER statement (single + multi-digit, uniform, all primes incl. 5)

**[VERIFIED 5≤p≤31, all n∈[1,320], q:=⌊n/p⌋, zero failures]:**
> p³ · b_n · a_q ≡ b_q · a_n (mod p³),   with v_p(p³ b_n a_q − b_q a_n) ≥ 3 (min exactly 3).

This subsumes everything above: single-digit (q=a<p), multi-digit (q≥p, digit-by-digit descent),
and p=5. On p-unit cells it is equivalent to the ratio descent p³(b_n/a_n) ≡ b_q/a_q (mod p³),
which iterates down the whole base-p expansion. Supporting integrality **[VERIFIED, 0 failures]**:
v_p(b_n) ≥ −3 v_p(d_n) (⇔ d_n³ b_n ∈ ℤ), d_n=lcm(1..n), v_p(d_n)=⌊log_p n⌋.

Corrections to prior/sibling framing:
- The exact "iterated law" v_p(b_n/a_n) = −3 v_p(d_n) is FALSE (equality fails: b_n numerators
  carry sporadic extra p-factors, e.g. 7 | 62531 = numerator(b_3)). It holds only as ≥.
- Depth floor is a FLAT 3, **independent of κ = v_p C(2n,n)** — cells with κ=0,1,2 all floor at 3.
  This contrasts the sibling weight-5 report of "floor 2−κ, typical 3−κ". (Flag for T4.)

### T1 depth fine-structure (boosts above the floor of 3), single-digit

Robust law: E ≥ 3. Boosts (E>3) are sporadic higher cancellations, reflection-symmetric under
(a,r) ↦ (p−1−a, p−1−r), concentrated at extreme digits:
- E=6 at the corner (a,r)=(p−1,p−1)  [i.e. n=p²−1]  (p=11 splits into (10,0),(10,10)).
- E=5 at the edge  (a,r)=(p−1,0)     [n=p(p−1)].
- E=4 on symmetric interior/edge pairs, e.g. p=13: (3,5),(3,7),(9,5),(9,7),(12,2),(12,6),(12,10).
These do not follow a clean κ-law; the provable/robust content is the floor E≥3.

---

## T2 [PROVED]. Lucas congruence for a_n:  a_{ap+r} ≡ a_a · a_r (mod p)

**Theorem.** Let p be prime. For every integer a ≥ 0 and every r with 0 ≤ r < p,
    a_{ap+r} ≡ a_a · a_r  (mod p),
where a_n = Σ_{k=0}^n C(n,k)² C(n+k,k)². Consequently, if n = Σ_i n_i p^i is the base-p
expansion, a_n ≡ ∏_i a_{n_i} (mod p) (full Lucas property).

Write A(n,k) := C(n,k)² C(n+k,k)², so a_n = Σ_{k=0}^n A(n,k).

**Lemma 1 (Lucas step for binomials).** For any integers a,b ≥ 0 and any 0 ≤ r,s < p,
    C(ap+r, bp+s) ≡ C(a,b) · C(r,s)  (mod p).
*Proof.* Base-p digits: ap+r has last digit r and higher digits those of a; bp+s has last digit s
and higher digits those of b. Lucas' theorem gives C(ap+r,bp+s) ≡ C(r,s)·∏_{j≥1}C(a_{j-1},b_{j-1}),
and ∏_{j≥1}C(a_{j-1},b_{j-1}) ≡ C(a,b) (mod p) by Lucas again. ∎

**Lemma 2 (carry annihilation).** Fix a,b ≥ 0, 0 ≤ r,s < p. Set n = ap+r, k = bp+s. Then
    C(n+k, k) ≡ { C(a+b, b) · C(r+s, s)  if r+s < p ;   0  if r+s ≥ p }   (mod p).
*Proof.* n+k = (a+b)p + (r+s). If r+s < p, apply Lemma 1 to (a+b)p+(r+s) and bp+s:
C(n+k,k) ≡ C(a+b,b)C(r+s,s). If r+s ≥ p, then n+k = (a+b+1)p + (r+s−p) with 0 ≤ r+s−p < p, and
Lemma 1 gives C(n+k,k) ≡ C(a+b+1,b)·C(r+s−p, s). But r < p forces r+s−p < s, so C(r+s−p,s) = 0. ∎

**Lemma 3 (summand factorization mod p).** With n=ap+r, k=bp+s as above,
    A(n,k) ≡ [r+s<p] · C(a,b)² C(a+b,b)² · C(r,s)² C(r+s,s)²   (mod p),
where [·] is the indicator. *Proof.* A(n,k)=C(n,k)²C(n+k,k)². By Lemma 1, C(n,k)²≡C(a,b)²C(r,s)².
By Lemma 2, C(n+k,k)² ≡ [r+s<p]·C(a+b,b)²C(r+s,s)². Multiply. ∎
(Numerically confirmed: 200 random (p,a,b,r,s), 0 failures.)

**Proof of Theorem.** Every k ∈ {0,…,n} is written uniquely as k=bp+s with 0≤s<p and 0≤b.
Since k ≤ n = ap+r < (a+1)p we have b ≤ a. Sum Lemma 3 over all k:
    a_n = Σ_{k} A(n,k) ≡ Σ_{b=0}^{a} Σ_{s=0}^{p-1} [r+s<p] C(a,b)²C(a+b,b)² C(r,s)²C(r+s,s)²  (mod p).
The summation region of the surviving terms is the PRODUCT set {0≤b≤a} × {0≤s<p, r+s<p}
(the constraint r+s<p involves only s; the b-range 0..a is independent — and when b=a the term
needs s≤r for k≤n, which is automatic since C(r,s)=0 for s>r). Hence the double sum factors:
    a_n ≡ ( Σ_{b=0}^{a} C(a,b)² C(a+b,b)² ) · ( Σ_{s=0}^{p-1}[r+s<p] C(r,s)² C(r+s,s)² )   (mod p).
The first factor is exactly a_a (the defining identity, an integer equality — no reduction used).
For the second, note a_r = Σ_{s=0}^{r} C(r,s)²C(r+s,s)², and each term with r+s ≥ p vanishes mod p:
there C(r+s,s) = C(1·p+(r+s−p), 0·p+s) ≡ C(1,0)C(r+s−p,s) = 0 (since 0 ≤ r+s−p < s), by Lemma 1.
Also C(r,s)=0 for s>r. Therefore Σ_{s=0}^{p-1}[r+s<p] C(r,s)²C(r+s,s)² ≡ a_r (mod p).
(Numerically confirmed: the deleted r+s≥p terms sum to 0 mod p, 300 random (p,r), 0 failures.)
Combining, a_{ap+r} ≡ a_a · a_r (mod p). The multi-digit product form follows by induction on the
number of base-p digits of a, applying the two-digit statement repeatedly (it holds for ALL a≥0). ∎

This matches the verified sweep (a-row: 0 failures, all p in 5..31, all n≤320, including p=5 —
consistent because the proof nowhere excludes p=5). It is the standard Gessel/McIntosh/Malik–Straub
mechanism specialized to the ζ(3) Apéry summand.

---

## T3 [PROVED, single-digit]. b-row Lucas: p³ b_{ap+r} ≡ b_a · a_r (mod p), p ≥ 5

**Theorem.** For every prime p ≥ 5, every a with 1 ≤ a < p and every r with 0 ≤ r < p,
    p³ · b_{ap+r} ≡ b_a · a_r  (mod p).
(Here both sides are p-integral: n=ap+r<p² ⟹ v_p(b_n) ≥ −3 ⟹ p³ b_n p-integral; a<p ⟹ b_a
p-integral; a_r ∈ ℤ.) **Verified: 0 failures, all p in {5,7,…,31}, all (a,r).**

Write H₃(n)=Σ_{m=1}^n 1/m³ and set
    W(n) := Σ_{k=0}^n A(n,k) · w(n,k),  w(n,k)=Σ_{m=1}^k (−1)^{m−1}/(2 m³ C(n,m) C(n+m,m)),
so that **b_n = H₃(n)·a_n + W(n)** (identity; verified). Then p³ b_n = p³H₃(n)a_n + p³W(n), and the
Theorem splits into two congruences, both proved below:
 (H-part)  p³ H₃(n) a_n ≡ H₃(a) a_a a_r  (mod p);
 (★ W-part) p³ W(n) ≡ a_r W(a)  (mod p).
Granting these: p³ b_n ≡ H₃(a)a_a a_r + a_r W(a) = a_r(H₃(a)a_a + W(a)) = a_r b_a (mod p). ∎

### H-part [PROVED]
For n=ap+r<p², the p-divisible indices in H₃(n) are m=jp, j=1..a, contributing
Σ_{j=1}^a (jp)^{−3} = p^{−3}H₃(a). Writing S=Σ_{m≤n, p∤m} m^{−3} (p-integral),
H₃(n) = S + p^{−3}H₃(a), so p³H₃(n) = p³S + H₃(a) ≡ H₃(a) (mod p³). Hence
p³H₃(n)a_n ≡ H₃(a)a_n (mod p³). Reduce mod p and use a_n≡a_a a_r (T2) and p-integrality of H₃(a):
p³H₃(n)a_n ≡ H₃(a)a_a a_r (mod p). ∎

### W-part (★) [PROVED]
Rewrite W(n)=Σ_{m=1}^n c(n,m) T(n,m), where c(n,m)=(−1)^{m−1}/(2m³C(n,m)C(n+m,m)) and
T(n,m):=Σ_{k=m}^n A(n,k) (an integer). Split the range of m into p∤m and m=jp.

Throughout, for an index x with 0≤x<p² write its digits x=(x₁,x₀), x₀=x mod p. Recall the
mod-p summand rule from T2: A(n,k) ≡ 0 (mod p) unless s:=k mod p satisfies s≤r AND r+s<p, and
for surviving k, A(n,k)≡C(a,b)²C(a+b,b)²C(r,s)²C(r+s,s)² with b=⌊k/p⌋. Two consequences used below:
 (T-fact) If m=(m₁,m₀) with m₀>r then T(n,m) ≡ T(a,m₁+1)·a_r (mod p), where T(a,j):=Σ_{b=j}^a A(a,b).
   [Surviving k=bp+s have s≤r<m₀; for b=m₁ this forces s≥m₀>r — impossible — so only b≥m₁+1 survive;
    the b-sum gives T(a,m₁+1), the s-sum gives a_r.]
 (T-fact0) If m=jp (m₀=0≤r) then T(n,jp) ≡ T(a,j)·a_r (mod p)  [same, now b≥j survives]. (Verified: 0 fails.)
 (Tvanish) T(a,j) ≡ 0 (mod p) whenever a+j≥p, and moreover v_p(T(a,j))≥2:
   every term A(a,b), b≥j, has a+b≥a+j≥p ⟹ Kummer carry ⟹ v_p C(a+b,b)≥1 ⟹ v_p A(a,b)≥2.

**Lemma V (singular layer; termwise) [PROVED].** For p∤m: v_p( p³ c(n,m) T(n,m) ) ≥ 1; hence
Σ_{p∤m} p³ c(n,m)T(n,m) ≡ 0 (mod p). *Proof.* v_p(p³cT) = 3 − v_p C(n,m) − v_p C(n+m,m) + v_p T(n,m)
(as p∤m, v_p(m³)=v_p 2=0). By Kummer, for m≤n<p²: v_p C(n,m)=#borrows(n−m)= [m₀>r] ≤ 1 (the second
borrow would need m₁=a with m₀>r, i.e. m>n). And v_p C(n+m,m)=#carries(n+m)= c₀+c₁ ≤ 2, where
c₀=[r+m₀≥p], c₁=[a+m₁+c₀≥p]. Thus v_p(C(n,m)C(n+m,m)) ≤ 3, with equality **only** when
[m₀>r]=c₀=c₁=1, forcing m₀>r and m₁≥p−1−a. In that (and only that) case (T-fact) applies (m₀>r) and
m₁+1≥p−a, so every b≥m₁+1 has a+b≥p ⟹ A(a,b)≡0 ⟹ T(a,m₁+1)≡0 ⟹ T(n,m)≡0 (mod p), i.e. v_p T(n,m)≥1.
Hence 3−v_p(CC)+v_p T ≥ 1 in every case: (CC)≤2 ⇒ ≥3−2+0=1; (CC)=3 ⇒ ≥3−3+1=1. ∎
(Verified termwise: min v_p over all p∤m equals exactly 1, p=7,11,13.)

**Reduction of the m=jp layer.** By Lemma V, p³W(n) ≡ Σ_{j=1}^a p³ c(n,jp) T(n,jp) (mod p). Put
    term_j := p³ c(n,jp) T(n,jp) = (−1)^{j−1} T(n,jp) / ( 2 j³ C(n,jp) C(n+jp,jp) )
(using p³/(jp)³=j^{−3} and (−1)^{jp−1}=(−1)^{j−1}, p odd). Lucas (T2, Lemma 1) gives, for all j,
    C(n,jp) ≡ C(a,j),   C(n+jp,jp) ≡ C(a+j,j)   (mod p)   [Verified (I),(II): 0 fails].
Let τ_j := (−1)^{j−1} T(a,j) / (2 j³ C(a,j) C(a+j,j)) be the j-th term of W(a) (indeed W(a)=Σ_{j=1}^a τ_j,
the definition of W(a); verified). Two cases (both verified: 0 fails):

• **a+j < p.** Then C(a,j),C(a+j,j) are p-units and C(n,jp)≡C(a,j), C(n+jp,jp)≡C(a+j,j) are units;
  with (T-fact0) T(n,jp)≡T(a,j)a_r we may substitute and invert mod p:
      term_j ≡ (−1)^{j−1} T(a,j) a_r /(2 j³ C(a,j) C(a+j,j)) = a_r τ_j  (mod p).

• **a+j ≥ p.** Both drop mod p: (i) v_p τ_j = v_p T(a,j) − v_p C(a+j,j) ≥ 2 − 1 = 1 (by (Tvanish) and
  one Kummer carry in C(a+j,j)), so τ_j ≡ 0. (ii) v_p C(n,jp)=[0>r]=0, v_p C(n+jp,jp)=1 (one carry,
  a+j≥p), and v_p T(n,jp) ≥ 2 because every term A(n,k), ⌊k/p⌋=b≥j, has a+b≥a+j≥p ⟹ carry ⟹
  v_p C(n+k,k)≥1 ⟹ v_p A(n,k)≥2; hence v_p(term_j) = −0−1+v_p T(n,jp) ≥ 1, so term_j ≡ 0.

**Assembling.** Summing over j and using W(a)=Σ_j τ_j (with the a+j≥p terms of both sums ≡0):
    p³W(n) ≡ Σ_{j} term_j ≡ Σ_{a+j<p} a_r τ_j ≡ a_r Σ_{a+j<p} τ_j ≡ a_r Σ_{j=1}^a τ_j = a_r W(a)  (mod p).
This proves (★), completing the Theorem. ∎

**Remarks.**
- The proof works verbatim for p=5 (uses only p odd, and j≤a<p ⟹ p∤j). It yields the *reduced* b-row
  p³ b_n ≡ b_a a_r (mod p) even when a_a≡0 (p=5) — because it never divides by a_a; the ratio-form pole
  is an artifact of dividing, not of the congruence.
- **[VERIFIED, not yet PROVED]** (i) the multi-digit extension (a≥p; the master p³ b_n a_q ≡ b_q a_n mod p³
  with q=⌊n/p⌋); (ii) the mod-p³ strengthening on unit cells (depth floor 3). The single-digit proof gives
  the base case for a digit-by-digit induction on the multi-digit statement; the mod-p³ boost would need the
  H-part's mod-p³ congruence (already established) together with a mod-p³ version of (★) (currently only mod p).

### T3 literature verdict [sources fetched, not memory]

- **a-row (T2)** is classical and covered: Gessel, "Some congruences for Apéry numbers," J. Number
  Theory 14 (1982); generalized by Straub, "Gessel–Lucas congruences for sporadic sequences"
  (arXiv:2301.12248, Monatsh. Math. 2023) — *fetched*: proves Lucas mod p and an extension mod p² for
  all 15 sporadic Apéry-LIKE **integer** sequences. Also Malik–Straub. These treat a_n, not the
  harmonic-weighted numerators b_n.
- **b-row (T3)** — the harmonic-weighted numerator descent p³ b_{ap+r} ≡ b_a a_r (mod p) — was **not
  located** in the surveyed literature. Checked and *fetched*: Straub 2301.12248 (integer sequences only);
  "Apéry Limits: Experiments and Proofs" (arXiv:2011.03400) — *fetched*: treats Apéry limits/irrationality
  measures analytically, **no congruence for b_n or b_n/a_n**. Web-search (secondary, not verified against
  source) indicates Beukers, "Some congruences for the Apéry numbers" (1985) and "Another congruence…"
  (1987) prove **endpoint/shift** supercongruences A_{mpʳ−1} ≡ A_{mpʳ⁻¹−1} (mod p^{3r}) and analogues for
  the second solution B(n) — a DIFFERENT congruence family (shift by mpʳ−1, not base-p digit descent).
- The master ratio form p³(b_n/a_n) ≡ b_q/a_q (mod p³) is a **Dwork-type / Frobenius descent for the
  p-adic Apéry limit** ζ_p(3)=lim_p b_n/a_n. Machinery that *should* subsume it — Beukers–Vlasenko "Dwork
  crystals" and Vargas-Montoya's "strong Frobenius structure ⇒ Lucas congruences" — is plausible but I did
  **not** verify an explicit statement with matching hypotheses (would need the crystal/Frobenius structure
  for the RANK-2 sub-object carrying b_n, i.e. the second solution, established). **[RECALLED-UNVERIFIED]**
  for that implication; do not cite it as proved.
- **Verdict:** T2 = known (Gessel/Straub). T3 single-digit = **proved here from scratch** (elementary,
  self-contained, no external theorem needed); not found stated in the literature. The multi-digit /
  mod-p³ master form is [VERIFIED] and its proof is open here (Dwork-crystal route is the natural attack).

---

## T4. Port assessment: what a weight-5 proof (Brown–Zudilin cellular pair) additionally needs

**The weight-5 objects** (Brown–Zudilin, arXiv:2210.03391, verified from the paper). Integer row
Q_n = Σ_{k=0}^n C(n,k)² C(n+k,k) (note: single power of C(n+k,k), NOT squared; Q_n = 1,3,19,147,1251,…).
Rational rows P_n (for ζ(5), d_n⁵ P_n ∈ ℤ) and P̂_n (for ζ(3), d_n² d_{2n} P̂_n ∈ ℤ). They satisfy a
common **order-3** (cubic characteristic 4λ³−2368λ²−188λ+1) Apéry-type recurrence, and Q_n P_n P̂_n are
three solutions. The analog descent would be p⁵ P_n Q_q ≡ P_q Q_n (mod p⁵), q=⌊n/p⌋ (floor 5, not 3).

**What ports directly (my ζ(3) proof, reused verbatim):**
1. *Integer-row Lucas* Q_{ap+r} ≡ Q_a Q_r (mod p). **Verified: 0 failures, all p in 5..31.** Same T2
   mechanism (Lucas step + carry annihilation + product-region factorization). The single power of
   C(n+k,k) is harmless here: one factor ≡0 still kills the term.
2. *The H-part idea*: the top harmonic layer of P_n contributes the p^{−5} pole from indices m=jp, giving
   a clean "p⁵·(top harmonic) ≡ (a-part harmonic) (mod p⁵)" reduction (weight-5 harmonic sum in place of H₃).
3. *The singular-layer philosophy*: only m ≡ 0 (mod p) indices carry the pole mod p.

**What needs genuinely new work (concrete obstructions my ζ(3) proof would hit):**

(a) **Rank 3, not rank 2 — the essential new ingredient.** ζ(3)'s recurrence is order 2: the descent is a
   statement about the RATIO of the two solutions (a single Apéry limit ζ(3)). Weight 5 is order 3: a
   3-dimensional solution space with an *intermediate* weight-3 sub-object P̂_n coupling the ζ(3) and ζ(5)
   limits. The descent must be proved for the full rank-3 local system; the middle row P̂_n (with its own
   d_n² d_{2n} normalization) will appear in the P_n descent as a cross-term with no ζ(3) analog. There is
   no getting around handling the whole 3-term filtration 0 → (ζ(5)) → M → (ζ(3)) → 0 at once.

(b) **No clean Apéry single-sum for P_n.** My whole T3 rested on the explicit formula b_n = H₃(n)a_n + W(n)
   with W a *single* alternating harmonic sum over the SAME summand A(n,k). Brown–Zudilin give P_n via
   cellular/residue integrals and the recurrence, not an Apéry-style closed sum; the analogous
   decomposition of P_n into (weight-5 harmonic weight)·(summand) + (nested double sum) must first be
   *found* — likely involving weight-(2,3) nested harmonic sums, matching the mixed d_n² d_{2n} denominator.

(c) **Asymmetric summand breaks the valuation bookkeeping.** ζ(3)'s A(n,k) = C(n,k)²C(n+k,k)² is a perfect
   square, so a single Kummer carry gives v_p ≥ 2 — the exact slack that closed Case B of Lemma V (needed
   v_p T(n,jp) ≥ 2). Q_n's summand C(n,k)²C(n+k,k) gives only v_p ≥ 1 per carry. To feed a p⁵ pole the
   valuation ledger must be redone with the correct (weighted) carry counts, and the "tail-vanishing"
   lemma (T-vanish) re-derived; the comfortable factor-of-2 is gone.

(d) **Deeper pole = more layers.** Assembling p^{−1},…,p^{−5} singular layers (vs p^{−1},…,p^{−3}) means
   more Kummer-carry cases and, for n < p² still ≤2 digits but with carries up to 5 deep in the products —
   the case analysis in Lemma V roughly squares in size.

(e) **κ-dependence returns.** My ζ(3) depth floor is a FLAT 3, independent of κ = v_p C(2n,n). The sibling
   weight-5 campaign reports a κ-DEPENDENT law (floor 2−κ, typical 3−κ). This is structural: the weight-5
   normalization carries a central-binomial C(2n,n) denominator (via d_n² d_{2n} P̂_n) absent at weight 3.
   Any weight-5 depth statement must be phrased relative to κ from the start; the clean flat floor is a
   ζ(3)-specific luxury.

**The single most important sentence for the port:** *Everything elementary in the ζ(3) proof survives for
the integer row Q_n, but the harmonic (P_n) descent has no order-3, rank-3 analog of Apéry's single-sum
b_n = H₃·a_n + W — so the port's real content is (i) discovering the correct weight-5 harmonic
decomposition of P_n (with its P̂_n/mixed-weight cross-terms) and (ii) redoing the Kummer-valuation ledger
for the p⁵ pole with the asymmetric, non-square summand — most cleanly via a rank-3 Dwork/Frobenius crystal
rather than the hand combinatorics that sufficed at weight 3.*


