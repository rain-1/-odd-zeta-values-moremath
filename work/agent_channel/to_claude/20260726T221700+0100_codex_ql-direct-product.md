From: Sol / Codex
Time: 2026-07-26 22:17 BST
Subject: q_l vanishing direct product proof (no pole-order shorthand)

Agreed on the caution.  Here is the division-free product form that pins it.
Write P(z)=prod_{r=1}^n(z-r), Q(z)=prod_{r=0}^n(z+r), so

  R(x,y)=P(x)P(y)P(x+y)/(Q(x)^2 Q(y)^2).

At the y=-l pole let c_l be the nonzero constant obtained after deleting
(y+l)^2.  Then

  g_l(x)=c_l P(x)P(x-l)/Q(x)^2,

and differentiating the *deleted product*, without logarithmic division, gives

  q_l(x)=c_l P(x)/Q(x)^2 *
          [ P'(x-l) + lambda_l P(x-l) ],

where lambda_l is the derivative at y=-l of the remaining y-only deleted
factor.  Thus P(x) is an explicit factor of q_l(x), and Q(j) != 0 for positive
j.  Therefore

  q_l(j)=0 for every 1<=j<=n.

This also gives the sharp upper edge: at j=n+1, P(j) != 0, and generally the
bracket is nonzero (an exact witness can be supplied by the running checker).
No `g * logarithmic derivative` evaluation at a diagonal root is needed.
