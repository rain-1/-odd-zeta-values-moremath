# REFEREE REPORT — Paper E, `papers_out/padicmap`

**Task:** W9, the quality gate for the last paper of the odd-zeta programme.
**Target:** `papers_out/padicmap` (`padicmap.tex` + 9 section files + `app-repro.tex`
+ `refs.tex`), 39 pp.
**Sources of truth:** `work/DIG_GROUP.md`, `work/DIG_LEDGER.md`, `work/DIG_SCAN.md`,
code in `work/dig/`.
**Stance:** every transcription wrong until checked; a false pass is the worst outcome.
**Date:** 2026-07-25.

Everything below was checked by re-running the `work/dig/` code, by reading the source
memos line by line, or by fetching a bibliographic record. Nothing is taken on trust from
the draft. Findings are inserted in the `.tex` files as `%% REFEREE [Rn]` comments and
then repaired in place (§4).

---

## VERDICT

**ISSUES FOUND AND FIXED.** 16 defects, of which **one is substantive and
mathematically false as stated** (R1: Proposition 6.2 is contradicted by the paper's
own Finding 8.1), one is a hypothesis that excludes the paper's own main example
(R2), and one is an internal contradiction between two sections (R4). The rest are
evidence-class, range-label, quotation and reproduction-record defects. All 16 are
repaired; no evidence class was raised; three of them were *lowered*.

The paper's *conclusions* survive intact. Every headline number I re-computed came out
exactly right (§3). The negative results are honestly scoped, the corrected-`E` story is
reproducible, and the disjoint-support finding is correctly stated in the body (it is
only the summary table that over-classes it).

---

## 1. SUBSTANTIVE FINDINGS

### R1 — Proposition 6.2 (`prop:pge5`) is FALSE as stated, and the paper's own Finding 8.1 contradicts it. [FIXED]

Statement as drafted:

> For $p\ge5$, **every** rank-1 configuration of Definition 4.1 is in regime T; some coset
> then has no aligned brick, and at that coset $Ar+\sum_c\mathrm{ctb}_c(\theta_0)=0$ exactly,
> whence $\alpha=G$ and $\mathrm{margin}=-E$.

The proof sketch immediately below it supplies the hypothesis the statement omits:
*"If $\varphi(p^r)>$ the number of distinct brick shifts, some $\theta_0$ has no aligned
brick."* When $A\ge\varphi(p^r)$ and the bricks are spread over all cosets, **every**
coset carries an aligned brick and the conclusion fails.

Verified against `work/dig/ledger.py` at $p=5$, $r=1$, $A=4$, $m=1$, $\epsilon=1$ with the
four bricks on the four cosets $j/5$:

```
contribs at the worst coset 1/5 : (-1, -1, -1, +1/4)
A*r + sum ctb = 4 - 2.75 = 1.25   (not 0)
margin = 1.25*log5 - E = 2.0118 - 5 = -2.9882   (not -E = -5)
```

`-2.9882` is precisely the $(p,w)=(5,5)$ cell of Findings 8.1 and 8.2 in the paper. So
the proposition contradicts the paper's own margin map. (The memo `DIG_LEDGER.md` §4.4
carries the same overstatement, and then immediately gives the correct general bound.)

The correct general statement is already in the paper: Corollary 6.3,
$\mathrm{margin}\le A\cdot p\log p/(p-1)^2-E$.

Inherited by: the abstract (*"we prove … that for $p\ge5$ the $p$-adic smallness of the
twisted coset sum cancels the archimedean coefficient growth exactly, leaving
$\mathrm{margin}=-E$"*) and §1.3(D). The $\zeta_5(3)$/$\zeta_7(3)$ headline in §8.2 is
**unaffected**: there $A=2<\varphi(p)$, so the hypothesis holds and the deficit really is
$-E=-3$ exactly.

**Repair:** hypothesis restored to the proposition; a remark records the $p=5$, $w=5$
exception with its number; abstract and §1.3(D) qualified.

### R2 — Theorem 1(ii)'s hypothesis excludes $\theta=\tfrac12$ at $p=2$, i.e. every $p=2$ construction in the paper. [FIXED]

The hypothesis $|\theta|_p\ge q_p$ is *faithful to the source* — Lai–Sprang, read verbatim
from `papers/15-…/Revision_Lai-Sprang….tex`:

> "For $x\in\mathbb{Q}_p$ with $|x|_p\geqslant q_p$, there is a unique $p$-adic
> meromorphic function $\zeta_p(s,x)$ …"

But $q_2=4$ and $|1/2|_2=2$, so $\theta=\tfrac12$ at $p=2$ is **not** in the domain — and
$\theta=\tfrac12$ is the integration shift of LSZ's construction, of Beukers'
$R^{(\mathrm B)}$, and of the whole $p=2$ cone of §7. Proposition 4.1 nevertheless says it
"is the case $\theta=\theta_0$ of Theorem 1(ii) after $m$ differentiations", at exactly the
excluded point.

This is not a gap in the mathematics — it is why LSZ prove a separate Lemma 9, which the
paper already quotes correctly in the proof of Theorem 2 (verified verbatim in the source):
$\frac{1}{s-1}\int_{\mathbb Z_2}\mathrm dt/(t+1/2)^{s-1}=2^s\zeta_2(s)$. But the theorem as
stated does not cover its own main application.

**Repair:** proviso added to Theorem 1(ii) and to Proposition 4.1, pointing at LSZ Lemma 9.

### R3 — $\omega$ is undefined at the points where Theorem 1(ii) is applied. [FIXED]

§1.6 defines "$\omega$ the Teichmüller character, $\langle x\rangle=x/\omega(x)$". The
Teichmüller character is a map $\mathbb Z_p^\times\to\mu_{\varphi(q_p)}$; but
$\omega(\theta)^{1-i}$ in (2.4) and $\omega(a)^{-u}$ in (4.1) are applied at
$|\theta|_p>1$. The source *extends* it,

$$\omega(x):=p^{v_p(x)}\,\omega\!\left(x/p^{v_p(x)}\right),\qquad x\in\mathbb Q_p^\times,$$

and that extension is load-bearing: it is what carries the $p^{r(i-1)}$ that reconciles
Theorem 1(ii) with Proposition 4.1's $J_u=u\,p^{ru}\omega(a)^{-u}\zeta_p(u+1,\theta_0)$.
Without it the two displays are inconsistent by a power of $p$.

**Repair:** the extension is now stated in §1.6.

### R4 — §5.2's "no source is sharper than the ledger" is false, and contradicts §5.5(a). [FIXED]

§5.2 closes: *"We note explicitly that there is no case in which a source is sharper than
the ledger."* `work/dig/ledger.py`'s own cross-check block prints, for Lai's $A_n$:

| $s$ | ledger margin | Lai's printed margin |
|---|---|---|
| 0 | 1.5452 | 1.3178 |
| 1 | **1.3178** | **1.4767** |
| 2 | **1.0904** | **1.6355** |
| 3 | **0.8629** | **1.7944** |

From $s=1$ on the source is sharper — for exactly the reason §5.5(a) already gives
("Lai's $A_n$ additionally carries an asymptotic $\Phi^{-(s+2)}$" which the ledger does not
model). So §5.2 and §5.5(a) contradict each other.

The *individual* comparisons §5.2 makes are all correct: the ledger's smallness rate
$(10s+20)\log2$ matches Lai's printed rate, and its archimedean growth $(6s+12)\log2$ is
sharper than Lai's printed $(2+4\log2)s+4+8\log2$ (confirmed by `verify.py`'s measurement
$8.1172\to8.1759\to8.2066$ at $n=8,16,24$, converging to $8.3178$).

**Repair:** the blanket sentence is restricted to the quantities the ledger models
($\alpha$, $G$, $E$), with the $A_n$ margin exception recorded and cross-referenced.

### R5 — Proposition 2.5's proof does not establish $o(n)$. [FIXED, class lowered]

The proof reads: $O(n/\log n)$ primes in the window, each contributing $O(\log\ell)=O(\log n)$
to $\log\Phi_n$ under an $O(1)$ change of exponent — that product is $O(n)$, **not** $o(n)$,
and $O(n)$ is exactly what must be excluded. The displayed chain
"$O(n)\cdot O(\log n)/\log n\cdot o(1)$" is not a well-formed bound. The memo
(`DIG_GROUP.md` §1b) has the same defect ("changes $\log\Phi_n$ by $O(\pi(m_3n))$" treats
each prime as contributing $O(1)$ rather than $O(\log\ell)$).

The proposition is very probably true — an $O(1)$ shift moves $\lfloor c_in/\ell\rfloor$ only
for the $O(1/\ell)$-density set of primes where a carry occurs, and the perturbed direction
$c+d/n\to c$ with $\Lambda$ continuous off a null set — but that argument is not the one
written.

**Repair:** class lowered `[PROVED]` → `[DERIVED]`; the defective sentence replaced by the
direction-perturbation argument, with the crude $O(n)$ bound stated honestly.

### R6 — the abstract states Theorem 2 without its load-bearing hypothesis. [FIXED]

Abstract: *"We prove that a two-term $p$-adic form in $1$ and $\zeta_p(w)$ exists exactly
when $\varphi(p^r)=2$."* Theorem 2 says "arises from a **single integration shift** if and
only if …", and its own final sentence says that otherwise the full twisted coset sum
produces such a form. Without the qualifier the abstract's claim is false.

### R7 — evidence-class upgrade in the §9.7 summary table. [FIXED, class lowered]

The row *"$\delta_{\mathfrak G}>0$ and $C_1=0$ have disjoint support — `[PROVED]` +
`[VERIFIED measured]`"* is an upgrade. `DIG_LEDGER.md` §5 never classes it `[PROVED]`. What
is proved is (a) $C_1=0$ on the balanced co-located locus (Prop. 4.7, "proved in the
sources": Beukers 11.1(3), LSZ Lemma 20) and (b) $\delta_{\mathfrak G}=0$ at the totally
symmetric point (Prop. 3.6 — a *single point*, plus LSZ's). The inclusion
$\{C_1=0\}\subseteq\{\delta_{\mathfrak G}=0\}$ is verified on the cone of §7.6, not proved.

**Repair:** `[DERIVED]` + `[VERIFIED measured]`. (The body, §9.3, states it in an untagged
box and is fine.)

### R8 — "$C_1>C_0>C_2$ at every direction where the archimedean construction works" is false at the symmetric direction. [FIXED]

`gate_dig2.py` gives $C_1=3.525494$ at the Apéry/Ball direction; the calibration table of
§9.2 gives $C_0/\mathrm{budget}=1.175165$ at the same direction, i.e. $C_0=3.525495$. They
are equal — as they must be, both being $4\log(1+\sqrt2)$ at the Apéry point. The strict
inequality holds at the other two measured directions (RV optimum $48.4694>47.1547>29.8123$;
crossing $77.2577>75.92>48.4593$).

**Repair:** "$C_1\ge C_0>C_2$ at the directions measured, with equality at the symmetric
point".

### R16 — `find:LLS` mis-identifies which term of $c_p$ is replaced. [FIXED]

Fetched from arXiv:2505.23088 (HTML), Theorem 1.1:

```
c_p = p + (p - 1 - varpi_p) / ( (p/(p-1)) log p - 1 - log 2 )
varpi_p = psi(1/p) + 2p - 1 + gamma + p( log p - sum_{j=1..p} 1/j )
```

The paper's break-even condition is
$s>\bigl[p-1-\tfrac{p\log p}{p-1}\bigr]\big/\bigl[\tfrac{p\log p}{p-1}-1-\log2\bigr]$.

* The **denominators agree exactly**, including the $\log 2$ — this is the paper's real
  claim and it is **correct**, a genuinely strong test.
* The paper then says "Their numerator differs only in replacing the crude $\log2$ by an
  exact quantity $\varpi_p$". Wrong term: the $\log2$ is in the *denominator* of both and
  is *identical*; what $\varpi_p$ replaces is the ledger's $p\log p/(p-1)$ in the numerator.
* $\varpi_p$'s printed closed form matches the source **verbatim**.

---

## 2. RANGE, LABEL AND QUOTATION DEFECTS

### R9 — Finding 5.9's `[VERIFIED]` range is not reproducible as printed. [FIXED]

Claimed: $p\in\{2,3,5,7\}$, $r\in\{1,2\}$, $A\le5$, $m\le4$, $\epsilon\in\{0,1\}$,
$n=30,\dots,48$; **0 violations**.

Committed `s_den.py` evaluates 15 hand-listed configurations at the single value $n=48$ and
contains **no $p=7$ case at all**. I re-ran rules (R1) and (R2) over the claimed range at
$n\in\{30,36,42,48\}$: **1120 configurations, 1084 non-degenerate, 1 violation** —

```
(p,r,A,m,eps) = (5,2,5,2,1) at n=30 : measured (7,0), predicted (8,0)
```

a small-$n$ artefact of the modal-exponent estimator: at $n=30$ the exponents are
$\{7\!:\!7,\ 11\!:\!7,\ 13\!:\!7,\ 17\!:\!8,\ 19\!:\!8,\ 23\!:\!7,\ 29\!:\!8\}$ — the plateau
has not formed and the mode picks 7; at $n=32,34,36,42,48$ the same configuration reads 8.
Everything else in the range reproduces with 0 violations, **including all of $p=7$**, which
I supplied.

**Repair:** the range now reads $n=32,\dots,48$, with the $n=30$ exception recorded.

### R10 — Finding 3.9 (F3), third row, mislabelled. [FIXED]

"$M=4$, fixed $h_0\le6$ — 672 points". `g_search.py`'s fixed-$h_0$ blocks are
$h_0=3,4,5,6$ with $15/127/127/672$ points (941 in total); **672 is the $h_0=6$ block
alone**. The other two rows reproduce exactly: `g_search2.py 2 9` → 113 points, 0
proportional pairs, 0 cross-$h_0$; `g_search2.py 4 7` → 1629 points, 0, 0.

**Repair:** relabelled "fixed $h_0=6$" — which also keeps the §9.7 total $113+1629+672=2414$
correct.

### R11 — Finding 3.6's `[VERIFIED]` range understates the search. [FIXED]

`g_opt.py` prints "directions with sum $\le34$: 9556 admissible shapes" and returns the
tabulated $0.412182$, $\delta=11.953292$, budget $29$, budget-3 saving $1.236547$; the tag
says $\sum\alpha\le30$.

### R12 — (3.2) is not Zudilin's Lemma 8. [FIXED]

Zudilin's Lemma 8 (read verbatim from `llm/04`) defines
$c_{jk}=a_j-b_k$ if $a_j\ge b_k$ and $c_{jk}=b_k-a_j-\mathbf1$ if $a_j<b_k$; the paper writes
$c_{jk}=|\alpha_j-\beta_k|$. Under (3.1) the two differ by exactly $1$ in the entries
$c_{33},c_{44}$ — both of which sit in $\Pi(c)$. The difference is an $O(1)$ shift of
factorial arguments and therefore does not move $\delta_{\mathfrak G}$ (Prop. 2.5) — which is
why the pipeline still returns $5.51389063$ against the published $5.51389062$ — but the
attribution should say so rather than silently simplify.

### R13 — the Brown quotation is truncated mid-sentence without an ellipsis. [FIXED]

Source (`papers/21-…/NewDetCritReSubmit.tex:1473`, and `llm/21` Remark 47):

> "…I do not know the answer to this question**, but the numerical experiments to be
> discussed later clearly demonstrate a large degree of `prime cancellation' of possibly a
> different nature.** It would be very interesting to investigate this further."

The draft ends the quotation at "question." — comma silently promoted to full stop, and the
qualifying clause dropped. The dropped clause is material to §9.4(A), which reads Brown's
remark as an open invitation.

### R14 — two printed negatives a reproducer will meet are not in App. A.3. [FIXED]

App. A.3 exists precisely so "a reproducer will meet them". Two more:

1. `g_verify.py` block **[C]** prints a large `[BROKEN]` banner — the $\theta$-shifted
   family is proportional only $10/40$ ($\theta=\tfrac12,\tfrac15,\tfrac25,\tfrac13$) and
   $5/80$ at the wider direction. This is **not** a failure of Findings 3.7/3.8: it is the
   same negative as Finding 3.9 (F3) — shifting the numerator bricks by $\theta$ leaves the
   very-well-poised family, and that shape class has no internal transfer identity. The
   positive half-integer test is `g_padic.py`, which returns $120/120$, $180/180$,
   $480/480$.
2. `verify.py` prints a "predicted $E$" for Lai's $A_n$ of $3$ ($s=0$) and $5$ ($s=1$)
   against measured $4$ and $7$. The measured values are the right ones and are what the
   paper uses ($E=A+m+1-\epsilon=3s+4$, §5.3); the script's *predicted* column is what is
   wrong.

### R15 — §7.3(i) overstates at $n=24$. [FIXED]

"the symmetric point $e=f=0$ is the best point of the cone at every $n$ tested" — for the
$M=5$ block at $n=24$, `s_record.py` reports `BEST over the cone: mu=3.77371516 at
e=(0,0,2,2,2) f=(0,0,2,2,2)` with $E=3$. That is the $E:5\to3$ artefact recorded two
sentences later; the claim needs the proviso, not the retrospective caveat.

---

## 3. WHAT I RE-COMPUTED, AND WHAT CAME OUT RIGHT

All from `work/dig/`, this session, exact arithmetic unless noted.

**Headline numbers (the five requested, and more):**

| quantity | paper | recomputed | ✓ |
|---|---|---|---|
| RV pipeline $\mu(\zeta(3))$ | $\le5.51389063$ | `g_group.py` → 5.51389063 | ✓ |
| its ingredients | $m_0..m_3=19,16,18,16$; budget 50; $\int\Lambda\,d\psi=24.18768530$; $\int_0^{1/16}=4$; $\delta=20.18768530$; $C_2=29.81231470$; orbit 118 | all reproduced digit for digit | ✓ |
| margin map, corrected $E$ | Finding 8.2, 17 rows | `s_map.py` MAP 5 — **every row**, incl. the compressed $p=11,13$ row ($E_{\rm true}=3/5/11/15$, margin $-3/-5/-11/-15$) | ✓ |
| nearest miss | $\zeta_5(3),\zeta_7(3)$ at exactly $-3.000$ | $A=2$, $m=0$, $\epsilon=0$, $E=3$, regime T, margin $=-E=-3$ exactly | ✓ |
| parity law | $\rho_i=0$ iff $i+M$ even | `s_vwp.py`: $M=3..7$ → zeros $[1,3],[1,2,4],[1,3,5],[1,2,4,6],[1,3,5,7]$ | ✓ |
| $\mathrm{margin}(M,m)=2M\log2-(M+m)$ | at $(6,1)$: $+1.3178$; at $(4,3)$: $-1.4548$ | `s_vwp.py` A3 both exact | ✓ |
| exclusion tolerances | F3: 0 pairs, exact rational, zero tolerance | determinant test `r0i*rzj-r0j*rzi==0` over `Fraction`; 113/1629/672 points, 0 hits | ✓ |
| rank wall | $66{+}120{+}77{+}36{+}1=300$, keep$\ne0$ **0**, controls $300/300$ | `s_rank.log`, `s_recur.log` — every cell, and the timings 163/575/126/198/118 s in App. A.1 | ✓ |

**Also re-checked and exact:** all three published measures from the tuple alone
(`ledger.py`, every printed digit, plus the 50-digit re-verification block);
Finding 5.10's $E$-band table at $n=48$ (5/0, 7/4, 9/6) and Finding 7.11's
$(7,4)$ at $n=48,60,72$ with rates $9.72,10.18,10.21$; the whole of Finding 7.13
(length cone, 5 rows, $C_1$ and $E$); the whole of Finding 7.16 (hatch, 8 rows of gains
$0..{+}2$ and 7 hyperplane depths $14,26,0,20,28,11,10$, max 28); Finding 9.3
(crossing: $-28.97$ vs $>+48.46$, shortfall $77.43$, generous $42.25<48.46$; RV $-12.26$
vs $+29.81$; symmetric $-1.51$ vs $+3.00$; $C_1/\mathrm{bud}=1.1752/0.9694/1.0730$; coset
defect $0.50/0.357/0.4286$); Finding 3.6 rows 1–3; the $43$ 3-adic digits of
$\zeta_3(3,1/3)=\zeta_3(3,2/3)$ (`verify.py`); the 58/127/288 = 473 inset points.

**Statements checked verbatim against their sources (all correct):**
Zudilin Lemma 7 = eq. (4.4) invariant and the $h$-variables; Lemma 9 = $H(c)/\Pi(c)$ stable
with $\Pi(c)=c_{21}!c_{31}!c_{41}!c_{12}!c_{32}!c_{42}!c_{33}!c_{44}!$; Lemma 12 = the
saddle $C_0=-f_0(\tau_0)$; Lemma 16 = the denominator lemma; the RV optimum
$(18,17,16,19;0,7,31,32)$ and the printed $C_0=47.15472079\dots$, $C_1=48.46940964\dots$,
$\mu(\zeta(3))\le5.51389062\dots$ (Zudilin eq. (5.11)–(5.12)).
Lai–Sprang Lemma 4 (ℓ(n)-adic criterion), Lemma 12 (coset sum — **verbatim identical** to
(1.4)), Definition 16, Lemma 21 (the Volkenborn linear form, including $\rho_{0,\theta}$),
Lemmas 26–29 — the arXiv numbering the paper cites is the right one.
LSZ Lemma 4 = Bel Lemme 3.2, Lemma 5 = translation, Lemmas 6–7 = $\triangle$, **Lemma 9 =
the $\theta=\tfrac12$ identity**, Def. 10/11, Remark 13 (quoted correctly, including
$(1-2^{-5})\zeta(5)$), Lemma 15(b) = $3\cdot2^{16n+18}/(n+1)^5$, Lemma 16 = $d_n\rho_{n,3}$,
$d_n^6\rho_{n,0}$ with the (den-con) expectation $\rho_{n,3}\in\mathbb Z$,
$d_n^5\rho_{n,0}\in\mathbb Z$, Lemma 20 = $\lambda^2-2^9\lambda+2^{16}$ with double root
$2^8$. **Both LSZ Final-remarks quotations are verbatim.** Brown–Zudilin
$\lim\log\Phi_n/n=34.39425186\dots$ against $m=\{18,17,17,16,16\}$, $\sum m=84$.

**Scope discipline (Theorem 3), the §1.4 promise:** every optimality sentence in §1.3(E),
§1.4, Theorem 3 and its follow-on sentence, §7.3, §7.5, §7.7, §8.1–8.3 and §9.7 carries its
family/cone qualifier. **One exception**, now fixed: the abstract's "$\delta_{\mathfrak G}$
… is never positive anywhere on the $p$-adic locus", where §7.3(iv) carries
`[VERIFIED: the cone of §7.6]`.

**App. A.3 artefacts:** both are correctly stated *as artefacts*, and nothing load-bearing
cites them. `s_record.py` does print `-> NEW RECORD` with $\mu=6.817240$ and $17.135417$,
its `BEST over the cone` line does return $e=f=0$ for $M=3$ and $M=4$, and it does raise
`ValueError: could not convert string to float: '-- (rank 2: weights {3,5})'` with the
third scan printed and the fourth not run — exactly as described. Theorem 3 rests on the
`BEST over the cone` line and on the 50-digit asymptotic re-verification, not on the
`NEW RECORD` line. Two further printed negatives were missing (R14).

---

## 4. REPAIR LEDGER

Evidence classes moved **down** only. Each edit carries a `%% REFEREE [Rn]` comment.

| # | file | change |
|---|---|---|
| R1 | `sec-classification.tex` | hypothesis restored to Prop. `prop:pge5`; new Remark with the $p=5,w=5$ exception |
| R1 | `padicmap.tex`, `sec-intro.tex` | abstract and §1.3(D) qualified |
| R1 | `sec-map.tex` | headline box notes the hypothesis holds at those cells |
| R2 | `sec-transfer.tex`, `sec-ledger.tex` | proviso on Thm 1(ii) and Prop. 4.1, via LSZ Lemma 9 |
| R3 | `sec-intro.tex` | §1.6 states the extension of $\omega$ to $\mathbb Q_p^\times$ |
| R4 | `sec-validation.tex` | blanket claim restricted; $A_n$ exception recorded |
| R5 | `sec-transfer.tex` | `[PROVED]`→`[DERIVED]`; proof corrected |
| R6 | `padicmap.tex` | "from a single integration shift" restored |
| R7 | `sec-discussion.tex` | `[PROVED]`→`[DERIVED]` in the summary table |
| R8 | `sec-discussion.tex` | $C_1\ge C_0>C_2$, equality at the symmetric point |
| R9 | `sec-validation.tex` | range $n=32,\dots,48$; $n=30$ exception recorded |
| R10 | `sec-group.tex` | "fixed $h_0=6$" |
| R11 | `sec-group.tex` | $\sum\alpha\le34$, 9556 shapes |
| R12 | `sec-group.tex` | Zudilin's $c_{jk}$ convention noted |
| R13 | `sec-intro.tex` | Brown quotation restored in full |
| R14 | `app-repro.tex` | two further printed negatives recorded |
| R15 | `sec-scan.tex` | $n=24$ proviso |
| R16 | `sec-ledger.tex` | the replaced term corrected |
| bib | `refs.tex` | `UNVERIFIED-LLS2025` → `LLS2025`, completed (below) |

---

## 5. BIBLIOGRAPHY

### 5.1 `UNVERIFIED-LLS2025` — COMPLETED, and it has since been published

Fetched: arXiv abstract page, arXiv API (Atom), arXiv HTML full text, Crossref
(`api.crossref.org/works/10.1007/s40687-025-00559-x`).

> L. Lai, C. Lupu and J. Sprang, *On the irrationality of certain $p$-adic zeta values*,
> Res. Math. Sci. **12** (2025), no. 4, Paper No. 77; arXiv:2505.23088.

* Title: **"On the irrationality of certain $p$-adic zeta values"** (arXiv API + Crossref
  agree verbatim).
* Authors and initials: **Li Lai, Cezar Lupu, Johannes Sprang** → `L. Lai, C. Lupu and
  J. Sprang`. Surnames in the draft were right; the initials are now confirmed, not guessed.
* Submitted 29 May 2025; comments "24 pages, 1 table".
* Journal reference **added**: Research in the Mathematical Sciences 12 (2025), no. 4,
  article no. 77, published 4 Oct 2025, DOI 10.1007/s40687-025-00559-x (Crossref).

**The six citing sentences, checked against the fetched text:**

| locus | claim | verdict |
|---|---|---|
| Finding 4.2 | the family contains their Def. 3.1 once free factorials are allowed | ✓ Def. 3.1 is $R_n(t)=p^{pn}n!^s\,t^{M_0}\prod_{j=1}^{p-1}(t+j/p)_n/(t)_{n+1}^{p-1+s}$ |
| Finding 4.6 | prefactor $p^{pn}n!^s$ from $(p-1)+(p-1+s)/(p-1)=p+s/(p-1)$ | ✓ exact — the arithmetic and the prefactor both check |
| §4.5 | "the factor $t^{M_0}$ of [LLS]" | ✓ $t^{M_0}$, $M_0=p^{2+N_0}s-1$, $N_0=v_p(p-1+s)$, is in Def. 3.1 |
| Finding 4.12 | $A=p-1+s$, $p-1$ bricks at $j/p$, $s$ free factorials | ✓ |
| Finding 4.12, §5.2(iv) | the bracket is **exactly** the denominator of $c_p$ in Thm 1.1 | ✓ both are $\frac{p\log p}{p-1}-1-\log2$ |
| Finding 4.12 | "their numerator differs only in replacing the crude $\log2$ by $\varpi_p$" | ✗ **R16** — the $\log2$ is in the denominator of both and is identical; $\varpi_p$ replaces $p\log p/(p-1)$. $\varpi_p$'s printed closed form is verbatim correct. |
| Cor. 6.3 | "the 'one of $\zeta_p(3),\dots,\zeta_p(c_p)$' regime" | ✓ Thm 1.1: "there exists an odd integer $i$ in $[3,c_p]$ such that $\zeta_p(i)$ is irrational" |

### 5.2 Five spot-checks — all five clean, no invented fields

| entry | fetched record | verdict |
|---|---|---|
| `Bel2019` | NUMDAM `JTNB_2019__31_1_81_0`, DOI 10.5802/jtnb.1069: Pierre Bel, *Irrationalité des valeurs de $\zeta_p(4,x)$*, JTNB **31** (2019), no. 1, 81–99 | **exact**, incl. issue and pages |
| `RhinViola` | matwbn PDF fetched: "ACTA ARITHMETICA LXXVII.1 (1996) — On a permutation group related to $\zeta(2)$ — Georges Rhin (Metz) and Carlo Viola (Pisa)", pages read off as 23–56. Second part confirmed by LSZ's own bibliography in the repo (`\bibitem{RV2001} … Acta Arith. 97 (2001), no. 3, 269–293`) and Zudilin's reference list | **exact**, both parts |
| `Beukers2008` | arXiv API for math/0603277: title *Irrationality of some $p$-adic $L$-values*, F. Beukers; Acta Math. Sin. (Engl. Ser.) **24** (2008), no. 4, 663–686 confirmed by search | **exact** |
| `KubotaLeopoldt1964` | De Gruyter / EUDML: *Eine $p$-adische Theorie der Zetawerte. Teil I: Einführung der $p$-adischen Dirichletschen $L$-Funktionen*, J. reine angew. Math. **214/215** (1964), 328–339, DOI 10.1515/crll.1964.214-215.328 | **exact** (long title, both volume numbers, pages) |
| `FSZ2019` | arXiv API journal-ref for 1803.08905: "Compositio Math. 155 (2019) 938-952", DOI 10.1112/S0010437X1900722X | **exact — the volume error found in `padiclimits` and `frobenius` (154/2018) is NOT present here** |

**Bonus, checked in passing and correct:** `Zudilin2004` (J. Théor. Nombres Bordeaux 16:1
(2004), 251–291 — arXiv journal-ref verbatim); `Brown2026` (arXiv:2604.20741 resolves to
F. Brown, *Mellin transforms, transfinite diameter and rational approximations of
integrals*); `Apery1979` and `BallRivoal2001` (against LSZ's own bibliography in the repo).
No entry was invented, and no field was added that I did not read off a fetched record.

---

## 6. RESIDUAL RISK, STATED PLAINLY

1. **Rule (R2) for multi-coset spreads at $p\ge5$ is assumed, not measured.** The paper says
   so twice (Remark 8.4, Open Lemma 9.1) and correctly notes the $p\ge5$ conclusions do not
   depend on it. Unchanged by this review.
2. **`s_den.py` as committed does not sweep the range Finding 5.9 claims.** I supplied the
   sweep (1120 configurations) and it holds with the single $n=30$ exception now recorded;
   but the *script* should be extended before anyone else tries to reproduce the tag.
3. **Proposition 2.5** now carries `[DERIVED]` with a corrected sketch. A referee who wants
   $\delta_{\mathfrak G}$ computed archimedeanly with a proof rather than a sketch will ask
   for the density argument in full. Nothing downstream depends on it (the conclusion is
   negative in the direction the proposition would help).
4. **The `[COMP]` claims are optimality over $\mathcal C$**, and the paper says so at every
   occurrence. That discipline is real and I could not break it.

---

## 7. COMPILE

`bash build.sh` — three `pdflatex` passes, `-halt-on-error`.

| | passes | undefined refs/citations | `LaTeX Warning` | overfull | pages |
|---|---|---|---|---|---|
| before repair | 3/3 clean | none | 0 | 8 | 39 |
| after repair | 3/3 clean | none | 0 | 8 | 41 |

All new labels resolve (`rem:halfexcl` 2.3, `rem:pge5sharp` 6.2, `rem:R1R2exc`,
`eq:omegaext` 1.2); the renamed key `LLS2025` resolves at all six citation sites; the
repaired abstract, the Brown quotation, the two corrected table labels, the completed
bibliography entry and Remark 6.2 were all read back out of the rendered PDF.
