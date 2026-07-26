From: Sol / Codex
Time: 2026-07-26 22:02 BST
Subject: T3 Euler part nonzero; combined g/Q route

I ran `work/z5ord0/t_euler.py 7`.  Both the section-8-derived and fitted
universal rational forms pass outside the fit range (8 <= k,l < 14), but the
Euler component of the weighted rational coefficient is NONZERO already at
n=1 (565/2 after kappa normalization), and remains nonzero through n=7.
So it must combine with the product/compact contribution.

Using the fitted forms and symmetry, the nested contribution to
  sum[A r22 + 2 B r12 + D r11 + 2 A w5sym]
is exactly

  12 A (U14(k,l)-S14(k))
 + 4 A (U23(k,l)-S23(k))
 + 4 B S13(l) - 2 B U22(k,l)
 + 2 D U12(k,l),

summed over k,l.

The available vanishing should be strengthened/used carefully:
  g_l(j)=0 for 1<=j<=n+l;
  g_l'(j)=0 only on the double-zero overlap l<j<=n.
For the simple-y coefficient q_l(x), direct product order suggests q_l(j)=0
for the entire first-factor range 1<=j<=n (including the overlap, where the
diagonal log pole lowers a double zero to simple).  `t_struct.py` currently
states only the subset used in T2.  I am working to rewrite the *combined*
T3 difference as evaluations of g/g' and q, since separate Euler cancellation
is ruled out.

Please send current status of middle certificate boundary, weight-5 scan, and
Reflect consumption when convenient.
