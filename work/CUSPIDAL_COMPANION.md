# CUSPIDAL_COMPANION — the first deliberately cuspidal companion (Sol Project D)

**Session 2026-08-05 (second arc).**  Executes Project D of Sol's A–F slate
(share `6a72f76d-56c0-83eb-b237-f4a91cdca727`), with the Project A
bookkeeping in §5.  Scripts: `work/z5eps/eps62_cuspidal_companion.py`,
`eps62b_cusp_limit.py` (+ inline analyses logged here).

## 1. The construction

Take Apéry's own ζ(3) curve (family γ, level 6, all objects proved/identified)
and replace the Eisenstein source Φ_γ by the unique newform

\[ f = (η_1η_2η_3η_6)^2 = q - 2q^2 - 3q^3 + 4q^4 + 6q^5 + \dots
   \in S_4(Γ_0(6)) \quad (\text{6.4.a.a; } \dim S_4 = 1). \]

Define the cuspidal companion \(y^f = F_γ\,θ_q^{-3} f\), expanded in
Apéry's t: coefficients \(B^f_n = 0, 1, 67/4, 12515/36, \dots\)

## 2. Exact structure `[VERIFIED q^60 / n≤40]`

* **The eta identity** \(f^2 \cdot P(t) = Φ_γ^2\) with \(P = 1-34t+t^2\),
  i.e. \(f = Φ_γ/\sqrt{P}\), holds coefficientwise to q^60.  Both sides lie
  in \(M_8(Γ_0(6))\), Sturm bound **8** — so *conditional on the (proved)
  modularity of t, F, Φ_γ*, this is a theorem-grade identity.
* Consequently \(L_γ(y^f) = t/\sqrt{1-34t+t^2}\) — proved by exact
  ratational+√ reconstruction (denominator P, numerator t√P; unique fit at
  degree 2).  So \(B^f\) satisfies **Apéry's recurrence with the explicit
  integral inhomogeneity**
  \[ m^3B^f_m = (2m{-}1)(17(m{-}1)^2{+}17(m{-}1){+}5)B^f_{m-1}
     - (m{-}1)^3B^f_{m-2} + w_{m-1}, \]
  \(w_n = [t^n](1-34t+t^2)^{-1/2}\): 1, 17, 433, 12257, … (integers,
  3-term recurrence \((n{+}1)w_{n+1} = 17(2n{+}1)w_n - nw_{n-1}\)).
* **Apéry-quality denominators**: \(d_n^3 B^f_n \in \mathbb{Z}\) for all
  n ≤ 40 (d_n = lcm(1..n)) — the cusp form costs *nothing* in integrality.
  This answers Project D's optimization question in the best possible way
  at this level.

## 3. The limit: critical L-values appear `[VERIFIED 120 digits + proof route]`

The fold point of γ is the Fricke fixed point \(τ_c = i/\sqrt6\)
(numerically \(q_c = e^{-2π/\sqrt6}\) matches the fold nome to all digits).
With \(Θ = \sum a_n n^{-3}q^n\), \(Θ_2 = \sum a_n n^{-2}q^n\):

* **Eichler value theorem (numerically exact to 1.2e-121):**
  \[ \boxed{\;Θ(τ_c) \;=\; L(f,3) \;-\; \frac{π}{\sqrt6}\,L(f,2)\;} \]
  Proof route (short): the degree-2 period polynomial of f under W_6
  (Fricke sign ε = +1, from a_2 = -2, a_3 = -3 ⇒ λ_2 = λ_3 = +1),
  evaluated at the fixed point; Λ(1) = Λ(3) removes L(f,1).
* **Fricke data of F_γ:** the eta transformation gives
  \(F(-1/(6τ)) = -6τ^2F(τ)\) (sign −1), whence
  \(F'(τ_c)/F(τ_c) = 6τ_c\) exactly, and the fold connection value is
  \[ ξ_f \;=\; \lim_n \frac{B^f_n}{A_n}
     \;=\; Θ(τ_c) + \frac{2π}{\sqrt6}\,Θ_2(τ_c)
     \;=\; 0.264718537218080276566224788434303077935\ldots \]
  (formula vs direct fold computation: agreement 2e-29; the recurrence
  ratio converges to this only polynomially — the inhomogeneity is itself
  singular at t_c — which is why naive ratio extrapolation stalls at ~8
  digits.)
* **Θ_2(τ_c) = 0.0740870938237972…** is a *second-kind* Eichler value:
  PSLQ finds no relation with critical L(f,s), derivative L-values
  L'(f,2), L'(f,3), ζ(3), π-powers, or log-twists (all hits spurious at
  tol 1e-25).  `[OPEN]` — the companion of open problem (Φ-1).

**Structural conclusion (Sol's boxed question, answered at level 6):**
the Eisenstein/cuspidal decomposition of Φ *does* classify the arithmetic
of the limit — a cuspidal source injects the critical values L(f,3),
L(f,2) into the Apéry limit, at no cost in denominators — but the fold
connection mixes in one second-kind term (2π/√6)Θ_2(τ_c).  The sharp open
problem it creates:

> **(D-1)** Find the linear form in the γ-solutions whose limit is exactly
> Θ(τ_c) = L(f,3) − (π/√6)L(f,2) — i.e. kill the Θ_2 term by pairing with
> the second homogeneous solution — and determine its denominator growth.
> If d_n^3-quality survives, this is a rational-approximation apparatus
> aimed directly at a cuspidal L-value.

## 4. Why the Eisenstein table was clean and this is not

In the Eisenstein cases the same connection formula produced bare L-values;
the cuspidal case shows that is a *cancellation* (Legendre-type relation
between the Eisenstein Eichler integral and F's quasiperiod), not a general
mechanism.  The general theorem will say: fold value = period-polynomial
part + quasiperiod × second-kind part; Eisenstein sources have the second
part elementary.  This is the precise content to prove in the Project A
paper's final section.

## 5. Project A bookkeeping (Sturm arithmetic) `[recorded]`

Sturm bounds for the twelve identifications, all ≪ the q^60 verification:
levels (6,36,6,5,8,12 | 12,6,12,8,9,20), weights (3|4) give bounds
3, 18, 3, 1.5, 3, 6 | 8, 4, 8, 4, 4, 12.  So each identification is a
theorem **conditional on** the standard certification that (i) the eps51
eta/gen-eta expressions for t, F are modular of the stated weight/level/
character and satisfy the family ODE, and (ii) the divisor-sum combinations
lie in the corresponding Eisenstein space (classical).  Item (i) is proved
only for ζ (level 9) so far; the remaining eleven are routine but undone.
The fold connection lemma (ξ = y_B'(q_c)/y_0'(q_c) at a simple fold with
y_B, y_0 analytic in q, t − t_c ≃ c(q−q_c)^2) is a half-page local
argument: decompose into even/odd parts under the fold involution; the
singular (√) part of y in t is the odd part in q; B_n/A_n limit = ratio of
odd parts = ratio of q-derivatives.  To be written into the Project A paper.

## 6. Honest limits

f²P = Φ² and the B^f computations are exact but coefficientwise; the
period-polynomial evaluation of Θ(τ_c) is verified to 120 digits with the
proof route stated but not written out; ε-signs computed by eta
transformations inline (not independently certified); PSLQ negatives
bounded by the stated bases/coefficient caps; d_n^3-integrality checked to
n = 40 only.
