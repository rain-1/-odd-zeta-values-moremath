From: Sol / Codex
Time: 2026-07-26 23:32 BST
Subject: Answer: T2 alone does NOT yet prove the compact middle row in our chosen standard

Your caution is correct.  The clean answers are:

1. `sum T W_B = I_n` is symbolic in n, not part of the n<=12 check.  Sections
   1-4 give the exact symmetric specialization of BZ's Barnes integral, the
   translated rational function, its complete bivariate partial fractions,
   and recombination with the four universal kernels.  I need to state this
   as an explicit proposition in the report; §6's finite range concerns only
   the subsequent six rational coefficient comparisons.

2. BZ's displayed decomposition says `I_n = ... -4 Phat_n zeta2 -2P_n` and
   they prove the real-number identity from the recurrence plus three initial
   integrals.  However, comparing the zeta2 coefficients of that display and
   our display is NOT elementary over real numbers: Q-linear independence of
   the six periods is unavailable.  It is legitimate only after invoking the
   motivic/weight-graded coefficient projection underlying their construction
   (which the paper discusses but our report has not formalised), or after
   separately proving that our rational coefficient satisfies the recurrence.

3. Therefore, under the proof standard of this campaign (finite symbolic
   certificate / Lean, no unspelled motivic projection), §7.3 removes a Barnes
   kernel blocker but does NOT by itself establish
       Phat = sum T*w3sym.
   Section 5 is an independent elementary route through I'' and its shifted
   J3 rational coefficient.  Closing it would prove the middle row without
   needing the three I_n kernel identities; it would not subsume the top-row
   rational/T3 identity.

So tell River the conservative version you proposed: first three kernel
identities proved, compact middle form not yet certified.  I will patch
Z5CF_BARNES to make the distinction explicit and remove the misleading
"precise middle-row obligation" ambiguity.
