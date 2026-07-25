---
title: "zudilin-2004-well-poised-hypergeometric-service"
source: "books-and-surveys/zudilin-2004-well-poised-hypergeometric-service.pdf"
conversion: pdftotext -layout
note: "extracted text; formulas are flattened and may be lossy — check the PDF for anything load-bearing"
---

WELL-POISED HYPERGEOMETRIC SERVICE
      FOR DIOPHANTINE PROBLEMS OF ZETA VALUES

                                         WADIM ZUDILIN

        Abstract. It is explained how the classical concept of well-poised hyperge-
        ometric series and integrals becomes crucial in studing arithmetic properties
        of the values of Riemann’s zeta function. By these well-poised means we
        obtain: (1) a permutation group for linear forms in 1 and ζ(4) = π 4 /90
        yielding a conditional upper bound for the irrationality measure of ζ(4);
        (2) a second-order Apéry-like recursion for ζ(4) and some low-order recur-
        sions for linear forms in odd zeta values; (3) a rich permutation group for
        a family of certain Euler-type multiple integrals that generalize so-called
        Beukers’ integrals for ζ(2) and ζ(3).
        2000 Mathematics Subject Classification. Primary 11J82, 33C20; Secondary
        11B37, 11M06.
        Key words and phrases. Zeta value, irrationality measure, well-poised hy-
        pergeometric series, permutation group, Apéry-like difference equation, con-
        tinued fraction.

                                    1. Introduction
  In this work, we deal with the values of Riemann’s zeta function (zeta values)
                                                   ∞
                                                   X 1
                                         ζ(s) :=
                                                   n=1
                                                         ns

at integral points s = 2, 3, 4, . . . . Lindemann’s proof of the transcendence of π
as well as Euler’s formula for even zeta values, summarized by the inclusions
ζ(2n) ∈ Qπ 2n for n = 1, 2, . . . , yield the irrationality (and transcendence) of
ζ(2), ζ(4), ζ(6), . . . . The story for odd zeta values is not so complete, we know
only that:
      • ζ(3) is irrational (R. Apéry [Ap], 1978);
      • infinitely many of the numbers ζ(3), ζ(5), ζ(7), . . . are irrational (T. Ri-
        voal [Ri1], [BR], 2000);
      • at least one of the four numbers ζ(5), ζ(7), ζ(9), ζ(11) is irrational1 (this
        author [Zu3], [Zu4], 2001).

  Date: 21 March 2002; LATEX-revision: 4 March 2003.
  1The first record of this type, at least one of the nine numbers ζ(5), ζ(7), . . . , ζ(21) is
irrational, is due to T. Rivoal [Ri2].
2                                        W. ZUDILIN

The last two results are due to a certain well-poised hypergeometric2 construc-
tion, and a similar approach can be put forward for proving Apéry’s theorem
(see [Ri3] and [Zu5] for details).
   After remarkable Apéry’s proof [Ap] of the irrationality of both ζ(2) and
ζ(3), there have appeared several other explanations of why it is so; we are
not able to indicate here the complete list of such publications and mention
the most known approaches:
        • orthogonal polynomials [Be1], [Hat] and Padé-type approximations
          [Be2], [So1], [So3];
        • multiple Euler-type integrals [Be1], [Hat], [RV2];
        • hypergeometric-type series [Gu], [Ne1];
        • modular interpretation [Be3].
G. Rhin and C. Viola have developed a new group-structure arithmetic method
to obtain nice estimates for irrationality measures of ζ(2) and ζ(3) (see [RV1],
[RV2], [Vi]). The permutation groups in [RV1], [RV2] for multiple integrals can
be translated into certain hypergeometric series and integrals, and this trans-
lation [Zu4] leads one to classical permutation groups (due to F. J. W. Whipple
and W. N. Bailey) for very-well-poised hypergeometric series.
   The aim of this paper is to demonstrate potentials of the well-poised hy-
pergeometric service (series and integrals) in solving quite different problems
concerning zeta values. Here we concentrate on the following features:
        • hypergeometric permutation groups for ζ(4) (Sections 3–5) and for lin-
          ear forms in odd/even zeta values (Section 8);
        • a conditional estimate for the irrationality measure of ζ(4) via the
          group-structure arithmetic method (Section 6);
        • an Apéry-like difference equation and a continued fraction for ζ(4) (Sec-
          tion 2) and similar difference equations for linear forms in odd zeta
          values (Section 7);
        • Euler-type multiple integrals represented very-well-poised hypergeo-
          metric series and, as a consequence, linear forms in odd/even zeta
          values (Section 8).
All these features can be considered as a part of the general hypergeometric
construction proposed recently by Yu. Nesterenko [Ne2], [Ne3].
   Hypergeometric sums and integrals of Sections 3–6 are prompted by Bailey’s
integral transform (Proposition 2 below), and it is a pity that the permutation
group for ζ(4) (containing 51840 elements!) leads to an estimate for the irra-
tionality measure of ζ(4) under a certain (denominator) conjecture only. We
indicate this conjecture (supported by our numerical calculations) in Section 6.
The particular case of the construction is presented in Section 2; this case can
be regarded as a toy-model of that follows, and its main advantage is a certain
nice recursion satisfied by linear forms in 1 and ζ(4).
    2
    We refer the reader to [Ba], Section 2.5, or to formula (69) for a formal definition, to [An]
for a nice historical exposition, and to Sections 2–8 below for number-theoretic applications.
           WELL-POISED HYPERGEOMETRIC SERVICE FOR ZETA VALUES                            3

   Section 7 is devoted to difference equations for higher zeta values; such
recursions make possible to predict a true arithmetic (i.e., denominators) of
linear forms in zeta values.
   The subject of Section 8 is motivated by multiple integrals
                     xn1 (1 − x1 )n xn2 (1 − x2 )n · · · xnk (1 − xk )n
        Z     Z
Jk,n := · · ·                                                             dx1 dx2 · · · dxk
                 (1 − (1 − (· · · (1 − (1 − xk )xk−1 ) · · · )x2 )x1 )n+1
          [0,1]k

that were conjecturally Q-linear forms in odd/even zeta values depending on
parity of k (see [VaD]). D. Vasilyev [VaD] required several clever but cumber-
some tricks to prove the conjecture for k = 4 and k = 5. However, one can
see no obvious generalization of Vasilyev’s scheme and, in [Zu4], we have made
another conjecture, yielding the old one, about the coincidence of the multiple
integrals with some very-well-poised hypergeometric series. We now prove the
conjecture of [Zu4] in more general settings and explain how this result leads
to a permutation group for a family of multiple integrals.
Acknowledgements. I am grateful to F. Amoroso and F. Pellarin for their
kind invitation to contribute to this volume of Actes des 12èmes rencontres
arithmétiques de Caen (June 29–30, 2001). I am kindly thankful to T. Rivoal
for his comments and useful discussions on the subject and to G. Rhin for
pointing out the reference [Co], where the recurrence for ζ(4) was first dis-
covered by means of Apéry’s original method. Special gratitude is due to
E. Mamchits for his valuable help in computing the group G of Section 5 for
linear forms in 1, ζ(4).

                       2. Difference equation for ζ(4)
  In his proof of the irrationality of ζ(3), Apéry consider the sequences un and
vn of rationals satisfying the difference equation
(1)          (n + 1)3 un+1 − (2n + 1)(17n2 + 17n + 5)un + n3 un = 0,
                      u0 = 1, u1 = 5,      v0 = 0, v1 = 6.
A priori, the recursion (1) implies the obvious inclusions n!3 un , n!3 vn ∈ Z, but
a miracle happens and one can check (at least experimentally) the inclusions
                                 un ∈ Z,     Dn3 vn ∈ Z
for each n = 1, 2, . . . ; here and later, by Dn we denote the least common
multiple of the numbers 1, 2, . . . , n (and D0 = 1 for completeness), thanks to
the prime number theorem
                                         log Dn
(2)                                lim          = 1.
                                  n→∞       n
The sequence
                          un ζ(3) − vn ,      n = 0, 1, 2, . . . ,
is also a solution of the difference equation (1), and it exponentially tends to 0
as n → ∞ (even after multiplying it by Dn3 ). A similar approach has been
4                                    W. ZUDILIN

used for proving the irrationality of ζ(2) (see [Ap], [Po]), and several other
Apéry-like difference equations have been discovered later (see, e.g., [Be4]).
Surprisingly, a second-order recursion exists for ζ(4) and we are now able to
present and prove it by hypergeometric means.
Remark. During preparation of this article, we have known that the difference
equation for ζ(4), in slightly different normalization, had been stated indepen-
dently by V. Sorokin [So4] by means of certain explicit Padé-type approxima-
tions. Later we have learned that the same but again differently normalized
recursion had been already known [Co] in 1981 thanks to H. Cohen and G. Rhin
(and Apéry’s original ‘accélération de la convergence’ method). We underline
that our approach presented below differs from that of [Co] and [So4]. We also
mention that no second-order recursion for ζ(5) and/or higher zeta values is
known.
    Consider the difference equation
(3)          (n + 1)5 un+1 − b(n)un − 3n3 (3n − 1)(3n + 1)un−1 = 0,
where
              b(n) = 3(2n + 1)(3n2 + 3n + 1)(15n2 + 15n + 4)
(4)
                   = 270n5 + 675n4 + 702n3 + 378n2 + 105n + 12,
with the initial data
(5)                 u0 = 1,   u1 = 12,      v0 = 0,   v1 = 13
for its two independent solutions un and vn .
Theorem 1. For each n = 0, 1, 2, . . . , the numbers un and vn are positive
rationals satisfying the inclusions
(6)                       6Dn un ∈ Z,       6Dn5 vn ∈ Z,
and there holds the limit relation
                                   vn   π4
(7)                            lim    =    = ζ(4).
                              n→∞ un    90
   Application of Poincaré’s theorem then yields the asymptotic relations
               log un          log vn               √
          lim          = lim          = 3 log(3 + 2 3 ) = 5.59879212 . . .
         n→∞      n       n→∞     n
and (see [Zu1], Proposition 2)
                log |un ζ(4) − vn |               √
           lim                      = 3 log |3 − 2 3 | = −2.30295525 . . . ,
         n→∞             n
since the√characteristic √polynomial   λ2 − 270λ − 27 of the equation (3) has zeros
135 ± 78 3 = (3 ± 2 3 )3 . Thus, we can consider vn /un as convergents of a
continued fraction for ζ(4) and making the equivalent transform of the fraction
([JT], Theorems 2.2 and 2.6) we obtain
                WELL-POISED HYPERGEOMETRIC SERVICE FOR ZETA VALUES                                       5

Theorem 2. There holds the following continued-fraction expansion:
          13    17 · 2 · 3 · 4 27 · 5 · 6 · 7       n7 (3n − 1)(3n)(3n + 1)
ζ(4) =        +               +               +···+                         +··· ,
         b(0)       b(1)           b(2)                       b(n)
where the polynomial b(n) is defined in (4).
   Unfortunately, the linear forms
                                    6Dn5 (un ζ(4) − vn ) ∈ Zζ(4) + Z
do not tend to 0 as n → ∞.3
  A motivation of a hypergeometric construction considered below leans on
the two series
          ∞                           2
         X    d (t − 1) · · · (t − n)
(8)    −                                  ∈ Qζ(3) + Q, n = 0, 1, 2, . . .
         t=1
             dt t(t + 1) · · · (t + n)

(Gutnik’s form of Apéry’s sequence [Gu], [Ne1]), and
                ∞
            2
                X                (t − 1) · · · (t − n) · (t + n + 1) · · · (t + 2n)
       n!             (2t + n)                                                      ∈ Qζ(3) + Q,
(9)             t=1
                                               (t(t + 1) · · · (t + n))4
                                                n = 0, 1, 2, . . .
(Ball’s sequence), and on the coincidence of these series proved by T. Rivoal
[Ri2], [Ri3] with a help of the difference equation (1). These arguments make
possible to give a new ‘elementary’ proof of the irrationality of ζ(3) (see [Zu5]
for details).
   Consider the rational function
                                                                                   2
                     n           (t − 1) · · · (t − n) · (t + n + 1) · · · (t + 2n)
(10) Rn (t) := (−1) (2t + n)
                                               (t(t + 1) · · · (t + n))2
and the corresponding series
                                                       ∞
                                                       X
(11)                                       Fn := −           Rn0 (t).
                                                       t=1

In some sense, the series (11) is a mixed generalization of both (8) and (9).
Lemma 1. There holds the equality
(12)                    Fn = Un ζ(5) + Un0 ζ(4) + Un00 ζ(3) + Un000 ζ(2) − Vn ,
where Un , Dn Un0 , Dn2 Un00 , Dn3 Un000 , Dn5 Vn ∈ Z.
Proof. The polynomials
(13)
               (t − 1) · · · (t − n)                                        (t + n + 1) · · · (t + 2n)
  Pn(1) (t) :=                                   and         Pn(2) (t) :=
                        n!                                                            n!
   3For a simple explanation why ζ(4) is irrational, see [Han].
6                                       W. ZUDILIN

are integral-valued and, as it is well known,
           Dnj dj Pn (t)
(14)                       ∈Z             for k ∈ Z and j = 0, 1, 2, . . . ,
           j!     dtj t=−k

where Pn (t) is any of the polynomials (13).
  The rational function
                                                   n!
(15)                          Qn (t) :=
                                          t(t + 1) · · · (t + n)
has also ‘nice’ arithmetic properties. Namely,

                                      (−1)k nk ∈ Z if k = 0, 1, . . . , n,
                                    (         
(16)     ak := Qn (t)(t + k) t=−k =
                                      0            for other k ∈ Z,

that allow to write the following partial-fraction expansion:
                                             n
                                            X     al
                                   Qn (t) =            .
                                            l=0
                                                t +  l

Hence, for j = 1, 2, . . . we obtain
                                              n
          Dnj dj                      Dnj dj X
                                                            
                                                       l−k
                 Qn (t)(t + k) t=−k =            al 1 −
          j! dtj                      j! dtj l=0        t + l t=−k
(17)                                                            n
                                                                X       1
                                                    j−1
                                           = (−1)         Dnj               j
                                                                              ∈ Z.
                                                                l=0
                                                                    (l −  k)
                                                                l6=k

Therefore the inclusions (14), (16), (17) and the Leibniz rule for differentiating
a product imply that the numbers
(18)
           (n)       1    d4−j                    4
                                                    
    Ajk = Ajk :=                 R n (t)(t +  k)      t=−k
                 (4 − j)! dt4−j
            1     d4−j       n               (1)          (2)                      4
                                                                                     
       =                (−1)   (2t +  n) · P n   (t)  · P n   (t) · (Qn (t)(t + k))    t=−k
         (4 − j)! dt4−j
satisfy the inclusions
                    (n)
(19)      Dn4−j · Ajk ∈ Z         for k = 0, 1, . . . , n and j = 1, 2, 3, 4.

Now, writing down the partial-fraction expansion of the rational function (10),
                                          4 X
                                            n             (n)
                                          X        Ajk
(20)                           Rn (t) =                j
                                                         ,
                                        j=1 k=0
                                                (t + k)
            WELL-POISED HYPERGEOMETRIC SERVICE FOR ZETA VALUES                                               7

we obtain that the quantity
                          ∞ X n
                            4 X                   4 X  n X ∞
                          X           jAjk       X             jAjk
                  Fn =                         =
                       t=1 j=1 k=0
                                   (t + k)j+1    j=1 k=0 l=k+1
                                                               lj+1
                        4    n      X ∞      k 
                       X     X              X       1
                     =     j    Ajk       −
                       j=1 k=0        l=1   l=1
                                                  lj+1

has the desired form (12) with
               n
               X                        n
                                        X                           n
                                                                    X                          n
                                                                                               X
                       (n)                     (n)                            (n)                     (n)
(21) Un = 4           A4k ,   Un0 = 3         A3k ,    Un00 = 2              A2k ,   Un000 =         A1k ,
                k=0                     k=0                         k=0                        k=0
                                     4         n            k
                                     X         X      (n)
                                                            X      1
(22)                          Vn =         j         Ajk                 .
                                     j=1       k=0          l=1
                                                                  lj+1

Finally, using the inclusions (19) and
                       k
                      X      1
            Dnj+1 ·         j+1
                                ∈Z       for k = 0, 1, . . . , n,             j = 1, 2, 3, 4,
                      l=1
                          l

we deduce that Un , Dn Un0 , Dn2 Un00 , Dn3 Un000 , Dn5 Vn ∈ Z as required.                                 

  Now, with a help of Zeilberger’s algorithm of creative telescoping ([PWZ],
Chapter 6) we get the rational function (certificate) Sn (t) := sn (t)Rn (t), where
(23)
                     1
sn (t) :=
       (2t + n)(t + 2n − 1)2 (t + 2n)2
   × −(122n2 + 115n + 29)(t + 2(5n − 1))t7
       − (4796n4 + 2336n3 − 859n2 − 459n + 16)t6
       − 2(4333n5 − 43n4 − 2645n3 − 734n2 + 86n + 7)t5
       − (3965n6 − 13782n5 − 14109n4 − 2207n3 + 878n2 + 142n + 7)t4
       + 2(5906n7 + 17354n6 + 10901n5 + 329n4 − 1340n3 − 289n2 − 15n + 2)t3
       + (22774n8 + 42602n7 + 20740n6 − 2935n5 − 4922n4 − 1162n3
         + 13n2 + 44n + 4)t2
       + 2n(8249n8 + 13764n7 + 5775n6 − 2178n5 − 2468n4 − 568n3
         + 94n2 + 64n + 8)t
       + n2 (4549n8 + 7531n7 + 2923n6 − 1975n5 − 2056n4 − 424n3
         + 196n2 + 112n + 16)
                              

satisfying the following property.
8                                        W. ZUDILIN

Lemma 2. For each n = 1, 2, . . . , there holds the identity
(24)
(n + 1)5 Rn+1 (t) − b(n)Rn (t) − 3n3 (3n − 1)(3n + 1)Rn−1 (t) = Sn (t + 1) − Sn (t),
where the polynomial b(n) is given in (4).
Proof. Divide both sides of (24) by Rn (t) and verify the identity
                 (2t + n + 1)(t − n − 1)2 (t + 2n + 1)2 (t + 2n + 2)2
     − (n + 1)5 ·
                                (2t + n)(t + n + 1)6
            − 3(2n + 1)(15n2 + 15n + 4)(3n2 + 3n + 1)
                    3                            (2t + n − 1)(t + n)6
            + 3n (3n − 1)(3n + 1) ·
                                        (2t + n)(t − n)2 (t + 2n − 1)2 (t + 2n)2
                     (2t + n + 2)t6 (t + 2n + 1)2
      = sn (t + 1)                                 − sn (t),
                    (2t + n)(t − n)2 (t + n + 1)6
where sn (t) is given in (23).                                                                
Lemma 3. The quantity (11) satisfies the difference equation (3) for n =
1, 2, . . . .
Proof. Since Rn (t) = O(t−3 ) and Sn0 (t) = O(t−2 ) as t → ∞ for n ≥ 1, differen-
tiating identity (24) and summing the result over t = 1, 2, . . . we arrive at the
equality
          (n + 1)5 Fn+1 − b(n)Fn − 3n3 (3n − 1)(3n + 1)Fn−1 = Sn0 (1).
It remains to note that, for n ≥ 1, both functions Rn (t) and Sn (t) = sn (t)Rn (t)
have second-order zero at t = 1. Thus Sn0 (1) = 0 for n = 1, 2, . . . and we obtain
the desired recurrence (3) for the quantity (11).                                
Lemma 4. The coefficients Un , Un0 , Un00 , Un000 , Vn in the representation (12) sat-
isfy the difference equation (3) for n = 1, 2, . . . .
Proof. Write the partial-fraction expansion (20) in the form
                                         4 +∞           (n)
                                         X X      Ajk
                             Rn (t) =                 j
                                                        ,
                                      j=1 k=−∞
                                               (t + k)
where the formulae (18) remain valid for all k ∈ Z and j = 1, 2, 3, 4. Multiply
both sides of (24) by (t + k)4 , take (4 − j)th derivative of the result, substitute
t = −k and sum over all k ∈ Z; this procedure yields that, for each j = 1, 2, 3, 4,
the numbers (21) written as
         +∞
         X                        +∞
                                  X                         +∞
                                                            X                        +∞
                                                                                     X
                 (n)                      (n)                       (n)                      (n)
Un = 4          A4k ,   Un0 = 3          A3k ,   Un00 = 2          A2k ,   Un000 =          A1k
         k=−∞                     k=−∞                      k=−∞                     k=−∞

satisfy the difference equation (3). Finally, the sequence
                  Vn = Un ζ(5) + Un0 ζ(4) + Un00 ζ(3) + Un000 ζ(2) − Fn
also satisfies the recursion (3).                                                             
          WELL-POISED HYPERGEOMETRIC SERVICE FOR ZETA VALUES                         9

  Since
             2                 4       4      12      12      13      13
  R0 (t) =      ,   R1 (t) = − 4 +           + 3 +           − 2 +          ,
             t3               t    (t + 1) 4   t   (t + 1) 3   t   (t + 1)2
in accordance with (21), (22) we obtain
                       U00 = 6,     U0 = U000 = U0000 = V0 = 0,
                    U10 = 72,     V1 = 78,       U1 = U100 = U1000 = 0,
hence as a consequence of Lemma 4 we arrive at the following result.
Lemma 5. There holds the equality
                                  Fn = Un0 ζ(4) − Vn ,
where Dn Un0 ∈ Z and Dn5 Vn ∈ Z.
   The sequences un := Un0 /6 and vn := Vn /6 satisfy the difference equation (3)
and initial conditions (5); the fact |Fn | → 0 as n → ∞, which yields the
limit relation (7), will be proved in Section 4. This completes our proof of
Theorem 1.
 The conclusion (6) of Theorem 1 is far from being precise; in fact, (experi-
mentally) there hold the inclusions
                                un ∈ Z,          Dn4 vn ∈ Z,
and, moreover, there exists the sequence of positive integers Φn , n = 0, 1, 2, . . . ,
such that
                        Φ−1
                          n un ∈ Z,      Φ−1   4
                                           n Dn vn ∈ Z.

This sequence can be determined as follows: if νp is the order of prime p in
(3n)!/n!3 , then
                                  Y
                            Φn :=     pbνp /2c ;
                                             p

here and below bxc and {x} := x − bxc denote respectively
                                                       √    the integral and
fractional parts of a real number x. For primes p > 3n we obtain the explicit
(simple) formula
                                   (
                                    1 if {n/p} ∈ [ 23 , 1),
                         bνp /2c =
                                    0 otherwise,
hence
                     log Φn            2
                lim         = ψ(1) − ψ     = 0.74101875 . . . ,
               n→∞      n               3
where ψ(x) := Γ0 (x)/Γ(x). Thus, we obtain that the linear forms
                                                    ?
(25)                    Φ−1 4
                         n Dn (un ζ(4) − vn ) ∈ Zζ(4) + Z

do not tend to 0 as n → ∞.
10                                      W. ZUDILIN

              3. Well-poised hypergeometric construction
     Consider the set of eight positive integral parameters
                         h = (h0 , h−1 ; h1 , h2 , h3 , h4 , h5 , h6 ),
(26)          where h−1 = 2 + 3h0 − (h1 + h2 + h3 + h4 + h5 + h6 ),
satisfying the conditions
                                   1
(27)             h0 − h−1 < hj < h0 ,                 j = 1, 2, 3, 4, 5, 6,
                                   2
and assign to h the rational function
                                                                    Q6
                                                                          j=−1 Γ(hj + t)
          R(t) = R(h; t) := (−1)h0 γ(h) · (h0 + 2t) · Q6
                                                                 j=−1 Γ(1 + h0 − hj + t)

                          = (−1)h0 · (h0 + 2t)
                                                            Γ(h1 + t)
                                × Γ(1 + h0 − h1 − h2 )
                                                       Γ(1 + h0 − h2 + t)
                                                            Γ(h5 + t)
                             × Γ(1 + h0 − h1 − h5 )
                                                       Γ(1 + h0 − h1 + t)
                                                            Γ(h2 + t)
                             × Γ(1 + h0 − h2 − h4 )
                                                       Γ(1 + h0 − h4 + t)
(28)                                                        Γ(h6 + t)
                             × Γ(1 + h0 − h3 − h6 )
                                                       Γ(1 + h0 − h3 + t)
                                 1 Γ(h3 + t)
                             ×
                               Γ(h3 ) Γ(1 + t)
                                       1                   Γ(h4 + t)
                             ×
                               Γ(h−1 − h0 + h4 ) Γ(1 + h0 − h−1 + t)
                                 1         Γ(h0 + t)
                             ×
                               Γ(h5 ) Γ(1 + h0 − h5 + t)
                                       1                 Γ(h−1 + t)
                             ×                                           .
                               Γ(h−1 − h0 + h6 ) Γ(1 + h0 − h6 + t)
In the last representation we pick out the rational functions
                    Γ(a + t)              (b − a − 1)!
           Γ(b − a)          =                                        if a < b,
                    Γ(b + t)   (t + a)(t + a + 1) · · · (t + b − 1)
            1       Γ(a + t)   (t + b)(t + b + 1) · · · (t + a − 1)
                             =                                        if a ≥ b,
      Γ(1 + a − b) Γ(b + t)                 (a − b)!
of the form (15), (13), having some nice arithmetic properties ([Zu4], Sec-
tion 7).
   It is easy to verify that, due to (26), for the rational function (28) the
difference of numerator and denominator degrees is equal to 3, hence
(29)                       R(t) = O(t−3 )           as t → ∞.
           WELL-POISED HYPERGEOMETRIC SERVICE FOR ZETA VALUES                                         11

  The series
                                                      ∞
                                                      X d
                                        F (h) := −             R(h; t)
(30)                                                  t=t
                                                          dt
                                                         0

           with any t0 ∈ Z,             1 − min {hj } ≤ t0 ≤ 1 − max{0, h0 − h−1 },
                                             1≤j≤6

produces a linear form in 1 and ζ(4).

Lemma 6. The quantity F (h) is a linear form in 1 and ζ(4) with rational
coefficients.

Proof. Order the parameters h1 , . . . , h6 as h∗1 ≤ · · · ≤ h∗6 and consider the
partial-fraction expansion of the rational function (28):

                                             4 0 h −h∗
                                             X  Xj+2            Ajk
(31)                                R(t) =                            ,
                                             j=1 k=h∗j+2
                                                             (t + k)j

where
                                  1         d4−j              4
                                                                
                        Ajk =                      R(t)(t + k)    t=−k
                                                                       ∈Q
(32)                          (4 − j)! dt4−j
                      for k = h∗j+2 , . . . , h0 − h∗j+2 and j = 1, 2, 3, 4.

Then we obtain
                   4 0         h −h∗                  4   0   h −h∗     ∞    k−h1          ∗
                 X X  Xj+2                 jAjk      X     Xj+2       X     X        1
   F (h) =                                         =            jA jk      −
                t=1−h∗1 j=1 k=h∗j+2
                                        (t + k)j+1   j=1 k=h∗          l=1    l=1
                                                                                    lj+1
                                                                   j+2

                4
                X
           =          Aj ζ(j + 1) − A0 ,
                j=1

with
                h0 −h∗j+2                                         4 0    h −h∗          k−h∗1
                  X                                               X  Xj+2               X 1
       Aj = j               Ajk ,   j = 1, 2, 3, 4,        A0 =                  jAjk         j+1
                                                                                                  ,
                k=h∗j+2                                           j=1 k=h∗j+2           l=1
                                                                                            l

and the well-poised origin of the series (30) (namely, the property R(−t−h0 ) =
−R(t), hence Ajk = (−1)j−1 Aj,h0 −k by (32), cf. [Zu4], Section 8, with r = 2
and q = 6) yields A2 = A4 = 0, while the residue sum theorem accompanied
with (29) implies A1 = 0 (cf. [Ne1], Lemma 1).                                

Remark. The question of denominators of the rational numbers A3 and A0 that
appear as the coefficients in F (h) can be solved by application of Nesterenko’s
denominator theorem [Ne3] (announced by Yu. Nesterenko in his Caen’s talk).
12                                        W. ZUDILIN

Namely, consider the set
N := {h3 − 1, h−1 − h0 + h4 − 1, h5 − 1, h−1 − h0 + h6 − 1, h0 − 2h1 , h0 − 2h2 ,
      h0 − h1 − h2 , h0 − h1 − h3 , h0 − h1 − h4 , h0 − h1 − h6 , h0 − h2 − h3 ,
      h0 − h2 − h5 , h0 − h2 − h6 , h0 − h3 − h5 , h0 − h4 − h5 , h0 − h4 − h6 ,
          h0 − h∗1 − h∗3 , h0 − h∗1 − h∗3 , h0 − h∗1 − h∗4 , h0 − h∗1 − h∗5 , h0 − h∗1 − h∗6 },
then,
(33)                   Dm1 Dm2 Dm3 Dm4 Dm5 · F (h) ∈ Zζ(4) + Z,
where m1 ≥ · · · ≥ m5 are the five successive maxima of the set N .
  Unfortunately, we have not succeeded in using the inclusion (33) for arith-
metic applications; actually, our experimental calculations show that the stron-
ger inclusion for the linear forms F (h), indicated at the beginning of Section 6,
holds.
  Using standard arguments, the property (29) and the fact that R(t) has
second-order zeros at integers t = 1 − h∗1 , . . . , − max{0, h0 − h−1 }, one deduces
the following hypergeometric-integral representation of the series (30).
Lemma 7 (cf. [Ne1], Lemma 2). There holds the equality
(34)
                   Z t1 +i∞              2
              1                      π
     F (h) =            R(h; t)              dt
             2πi t1 −i∞            sin πt
            (−1)h−1 γ(h) t1 +i∞ Γ(h0 + t) Γ(1 + 12 h0 + t) Γ(h−1 + t) Γ(h1 + t)
                         Z
          =
                πi         t1 −i∞            Γ( 12 h0 + t) Γ(1 + h0 − h1 + t)
                Γ(h2 + t) · · · Γ(h6 + t) · Γ(h−1 − h0 − t) Γ(−t)
              ×                                                      dt,
                    Γ(1 + h0 − h2 + t) · · · Γ(1 + h0 − h6 + t)
with any t1 ∈ R, 1 − h∗1 < t1 < − max{0, h0 − h−1 }.
  The series (30) as well as the corresponding hypergeometric integral (34) are
known in the theory of hypergeometric functions and integrals as very-well-
poised objects, i.e., one can split their top and bottom parameters in pairs
such that
 h0 + 1 = (1 + 21 h0 ) + 12 h0 = h−1 + (1 + h0 − h−1 ) = · · · = h6 + (1 + h0 − h6 )
and the second parameter has the special form 1 + 12 h0 .
Remark. As it is easily seen, the sequence Fn of Section 2 corresponds (after
a suitable shift of the summation parameter t) to the choice
(35)      h0 = h−1 = 3n + 2,            h1 = h2 = h3 = h4 = h5 = h6 = n + 1
of the parameters h. Hence the equalities Un = Un00 = Un000 = 0 in the represen-
tation (12) can be deduced from Lemma 6.
          WELL-POISED HYPERGEOMETRIC SERVICE FOR ZETA VALUES                                            13

                                      4. Asymptotics
  We take the new set of positive parameters
(36)                               η = (η0 , η−1 ; η1 , . . . , η6 )
satisfying the conditions
                 6
                 X                                1
(37)     4η0 =          ηj ,       η0 − η−1 < ηj < η0 ,                j = 1, 2, 3, 4, 5, 6,
                 j=−1
                                                  2
and for each n = 0, 1, 2, . . . relate them with the old parameters by the formu-
lae
(38)   h0 = η0 n + 2,          h−1 = η−1 n + 2,            hj = ηj n + 1,        j = 1, 2, . . . , 6.
Then Lemma 6 yields that the quantities Fn = Fn,η := F (h) are linear forms
in 1 and ζ(4) with rational coefficients, say
                 Fn = Fn,η = un ζ(4) − vn ,                   n = 0, 1, 2, . . . ,
and the goal of this section is to determine the asymptotic behaviour of these
linear forms as well as their coefficients un and vn as n → ∞.
   To the set (36) assign the polynomial
                               6
                               Y                  6
                                                  Y
(39)                               (τ − ηj ) −           (τ − η0 + ηj )
                           j=−1                   j=−1

and the function
           6
           X
f0 (τ ) :=   ηj log(ηj − τ )
         j=−1
                                                          6
                                                          X
           − (η0 − η−1 ) log(τ − η0 + η−1 ) −                    (η0 − ηj ) log(η0 − ηj − τ )
                                                           j=1

           + (η0 − η1 − η2 ) log(η0 − η1 − η2 ) + (η0 − η1 − η5 ) log(η0 − η1 − η5 )
           + (η0 − η2 − η4 ) log(η0 − η2 − η4 ) + (η0 − η3 − η6 ) log(η0 − η3 − η6 )
           − η3 log η3 − (η−1 − η0 + η4 ) log(η−1 − η0 + η4 )
           − η5 log η5 − (η−1 − η0 + η6 ) log(η−1 − η0 + η6 )
defined in the cut τ -plane C \ (−∞, max{0, η0 − η−1 }] ∪ [η1∗ , +∞), where η1∗ ≤
η2∗ ≤ · · · ≤ η6∗ denotes the ordered version of the set η1 , η2 , . . . , η6 .
   The first condition in (37) implies that (39) is a fifth-degree polynomial;
moreover, the symmetry under substitution τ 7→ η0 − τ and the second condi-
tion in (37) yield that this polynomial has zeros
                             η0 η0             η0
                                ,   ± s0 , and     ± is1 ,
                              2 2               2
                      η0
                          − s0 ∈ max{0, η0 − η−1 }, η1∗ , s1 ∈ (0, +∞).
                                                       
             where
                       2
14                                       W. ZUDILIN

The last four zeros can be easily determined by solving a certain biquadratic
(in terms of η0 /2 − τ ) equation. Set
                           η0                     η0
(40)                τ0 :=     − s0     and  τ1 :=    + is1 .
                           2                      2
Proposition 1. The following limit relations hold:
                           log |Fn |
(41)         C0 := − lim              = −f0 (τ0 ),
                      n→∞      n
                            log |un |             log |vn |
(42)         C1 := lim sup            = lim sup             = Re f0 (τ1 ).
                     n→∞       n          n→∞        n
Proof. The proof is based on application of the saddle-point method to the
integral representation of Lemma 7 for the quantities Fn and a similar integral
representation (see formula (48) below) for the coefficients un ; the fact that
both limits in (42) are equal follows immediately from the limit relation
                          vn       un ζ(4) − Fn
                      lim    = lim              = ζ(4) 6= 0
                      n→∞ un   n→∞      un
since −C0 < 0 < C1 under the conditions (37).
   Without loss of generality, we will restrict ourselves to the ‘most symmetric’
case (35), i.e.,
(43)               η0 = η−1 = 3           and      η1 = · · · = η6 = 1,
that corresponds to the linear forms in 1, ζ(4) constructed in Section 2.
   In the case (43), the zeros (40) of the corresponding polynomial (39) are as
follows:
                                     r      √
             3             π    3       3     3
        τ0 = − 31/4 cos       = −         +      = 0.22877012 . . . ,
             2            12    2       4    2
                                     r       √
             3             π     3      3      3
        τ1 = + i31/4 sin      = +         −      = 1.5 + i0.34062501 . . . .
             2             12    2      4     2
     By Lemma 7,
                   Z t1 +i∞
           (−1)n                              Γ(3n + 2 + t)2 Γ(n + 1 + t)6 Γ(−t)2
      Fn =                    (3n + 2 + 2t)                                       dt
            2πi   t1 −i∞                               Γ(2n + 2 + t)6
               n Z t1 +i∞
          (−1)                (3n + 2 + 2t)(3n + 1 + t)2 (3n + t)2 (n + t)6
        =
           2πi      t1 −i∞              (2n + 1 + t)6 (2n + t)6
                                    Γ(3n + t)2 Γ(n + t)6 Γ(−t)2
                                ×                               dt,
                                           Γ(2n + t)6
with any t1 ∈ R, −n < t1 < 0. Using the asymptotic formula
                                                √
                              
                             1
                                 log z − z + log 2π + O |z|−1
                                                              
             log Γ(z) = z −
                             2
           WELL-POISED HYPERGEOMETRIC SERVICE FOR ZETA VALUES                                   15

for z ∈ C with Re z = const > 0, taking t1 = −nτ0 and changing variables
t = −nτ , after necessary transformations we obtain

             2π(−1)n τ0 +i∞ (3 − 2τ )(3 − τ )3 (1 − τ )3 nf (τ )
                      Z
                                                                         −1
                                                                             
(44) Fn =                                               e        1 + O(n    )  dτ
                in2    τ0 −i∞        τ (2 − τ )9

as n → ∞, where

f (τ ) := 2(3 − τ ) log(3 − τ ) + 6(1 − τ ) log(1 − τ ) + 2τ log τ − 6(2 − τ ) log(2 − τ ).

Since
                                                         τ 2 (2 − τ )6
(45)                                 f 0 (τ ) = log
                                                      (3 − τ )2 (1 − τ )6

and τ0 is a zero of the polynomial (39) (which is (τ − 3)2 (τ − 1)6 − τ 2 (τ − 2)6 in
the restricted case), we conclude that f 0 (τ0 ) = 0 and τ0 is the unique maximum
of the function Re f (τ ) on the contour. Thus the integral (44) is determined
by the contribution of the saddle-point τ0 (see [Br], Section 5.7):

     (−1)n (2π)3/2 (3 − 2τ0 )(3 − τ0 )3 (1 − τ0 )3 00        −1/2 nf (τ0 )       −1
                                                                                     
Fn =              ·                               ·|f (τ 0 )|    ·e        1+O(n    )  ,
         n5/2              τ0 (2 − τ0 )9

hence
            log |Fn |
         lim          = f (τ0 ) = f (τ0 ) − τ0 f 0 (τ0 ) =: f0 (τ0 )
        n→∞    n
                            (3 − τ0 )6 (1 − τ0 )6               √
(46)                  = log                          =   3 log(2   3 − 3) =: −C0 .
                                 (2 − τ0 )12

This proves the limit relation (41).
  In the neighbourhood of t = −k, where k = n + 1, . . . , 2n + 1, the function
R(t) has the expansion

                               A4k        A3k        A2k      A1k
               R(t) =              4
                                     +        3
                                                +        2
                                                           +      + O(1)
                            (t + k)    (t + k)    (t + k)    t+k

by (31). On the other hand,
                           2                         2
                   sin πt                sin π(t + k)
                                                             = (t + k)2 + O (t + k)4
                                                                                        
                                 =
                     π                        π

about t = −k for k ∈ Z. Therefore,
                                     2        (
                                                 A3k            if k = n + 1, . . . , 2n + 1,
                     
                            sin πt
         Rest=−k                          R(t) =
                              π                  0              for other k ∈ Z,
16                                 W. ZUDILIN

and if L is a closed clockwise contour surrounding points t = −n−1, . . . , −2n−
1, then
                         2n+1              I           2
                 1       X              1        sin πt
                   un =       A3k = −                      R(t) dt
                 3      k=n+1
                                       2πi   L     π
                                            4
                           (−1)n
                                 I 
(47)                                 sin πt
                      =−                       (3n + 2 + 2t)
                            2πi L       π
                             Γ(3n + 2 + t)2 Γ(n + 1 + t)6 Γ(−t)2
                           ×                                       dt.
                                       Γ(2n + 2 + t)6
Taking the rectangle with vertices ±it2 ± N , for some fixed real t2 > 0 and
any N > 2n + 1, as the contour L and using the estimates
                sin πt   eπt2
                       ≤      ,     R(t) = O(N −3 ) as N → ∞
                   t      π
on the lateral sides of the rectangle, from (47) we deduce that
                   Z it2 +N Z −it2 −N            4
           3(−1)n                            sin πt
   un = −                     +
             2πi      it2 −N     −it2 +N       π
                             Γ(3n + 2 + t)2 Γ(n + 1 + t)6 Γ(−t)2
           × (3n + 2 + 2t)                            6
                                                                 dt + O(N −2 ),
                                        Γ(2n + 2 + t)
where the constant in O(N −2 ) depends on t2 only. Tending N → ∞ and
making the substitution t 7→ −t − h0 = −t − (3n + 2) in the first integral, we
obtain
                                               4
                      3(−1)n −it2 −∞ sin πt
                              Z        
              un = −                              (3n + 2 + 2t)
                         πi    −it2 +∞     π
(48)
                         Γ(3n + 2 + t)2 Γ(n + 1 + t)6 Γ(−t)2
                      ×                                      dt
                                    Γ(2n + 2 + t)6
(cf. [Zu2], Lemma 3.1). Finally, take t2 = −ns1 = −n Im τ1 , change the
variable t = −nτ and apply the asymptotic formula
                                        √
                      
                     1
                         log z − z + log 2π + O |z|−1 + O(e−2π| Im z| )
                                                     
      log Γ(z) = z −
                     2
                       for z ∈ C, | Im z| ≥ y0 > 0

(see [Br], Section 6.5, and [Zu2], Lemma 3.2), to get from (48) the expansion
         12π(−1)n is1 +∞ (3 − 2τ )(3 − τ )3 (1 − τ )3 nf (τ )
                    Z
   un =                                               e
             in2     is1 −∞         τ (2 − τ )9
                                             4
                                     sin πnτ
                                                 1 + O(n−1 ) + O(e−2πns1 ) dτ.
                                                                          
                                ×
                                         π
           WELL-POISED HYPERGEOMETRIC SERVICE FOR ZETA VALUES                             17

Since
                4
                         e−4πinτ    e−4πinτ
  
      sin πnτ
                     −        4
                                 =        4
                                              · | − 4e2πinτ + 6e4πinτ − 4e6πinτ + e8πinτ |
         π                (2π)       (2π)
                                       −2πns1     e−4πinτ
                                 < 15e         ·
                                                   (2π)4

for τ ∈ C with Im τ = s1 > 0, we obtain
                              Z is1 +∞
               3(−1)n                    (3 − 2τ )(3 − τ )3 (1 − τ )3 n(f (τ )−4πiτ )
          un =                                                       e
               4π 3 in2        is1 −∞            τ (2 − τ )9
(49)
                                               × 1 + O(n−1 ) + O(e−2πns1 ) dτ.
                                                                                  

By (45) and the definition of the point τ1 (that is the zero of the polyno-
mial (39)), hence f 0 (τ1 ) − 4πiτ1 = 0, we conclude that τ = τ1 is the unique
maximum of the function Re(f (τ ) − 4πiτ ) on the line Im τ = s1 . Therefore,
the saddle-point method says that the asymptotics of the integral in (49) is
determined by the contribution of the point τ = τ1 that yields the desired limit
relation

                     log |un |
         lim sup               = Re f (τ1 ) = Re(f (τ1 ) − τ1 f 0 (τ1 )) =: Re f0 (τ1 )
          n→∞           n
                                     |3 − τ1 |6 |1 − τ1 |6            √
                               = log                       = 3 log(2     3 + 3) =: C1 .
                                          |2 − τ1 |12

The proof of Proposition 1 is complete.                                                   

Remark. The limit relation (46) yields that |Fn | → 0 as n → ∞, and this is the
fact that we have promised to prove for Theorem 1 (see the paragraph after
Lemma 5). To be honest, the fact, that the asymptotics of the linear     √ forms
and their coefficients in the case (35) is determined by the zeros (3 ± 2 3 )3 of
a quadratic polynomial with integral coefficients, gave us the idea to look for
a second-order difference equation.

                              5. Group structure for ζ(4)
  This section can be viewed as a continuation of the story in [Zu4], Sections
4–6, where we explain the Rhin–Viola group structures for ζ(2) and ζ(3) by
means of classical hypergeometric identities.
18                                      W. ZUDILIN

Proposition 2 (Bailey’s integral transform [Ba], Section 6.8, formula (1)).
There holds the identity
(50)
            Γ(a + t) Γ(1 + 12 a + t) Γ(b + t) Γ(c + t) Γ(d + t) Γ(e + t)
     Z i∞
 1
2πi −i∞ Γ( 12 a + t) Γ(1 + a − c + t) Γ(1 + a − d + t) Γ(1 + a − e + t)
         Γ(f + t) Γ(g + t) Γ(h + t) Γ(b − a − t) Γ(−t)
   ×                                                        dt
      Γ(1 + a − f + t) Γ(1 + a − g + t) Γ(1 + a − h + t)
         Γ(c) Γ(d) Γ(e) Γ(f + b − a) Γ(g + b − a) Γ(h + b − a)
  =
     Γ(k + c − a) Γ(k + d − a) Γ(k + e − a) Γ(1 + a − g − h)
                                ×Γ(1 + a − f − h) Γ(1 + a − f − g)
                 Γ(k + t) Γ(1 + 12 k + t) Γ(b + t) Γ(k + c − a + t) Γ(k + d − a + t)
           Z i∞
        1
    ×
       2πi −i∞ Γ( 12 k + t) Γ(1 + a − c + t) Γ(1 + a − d + t) Γ(1 + a − e + t)
          Γ(k + e − a + t) Γ(f + t) Γ(g + t) Γ(h + t) Γ(b − k − t) Γ(−t)
       ×                                                                  dt,
               Γ(1 + k − f + t) Γ(1 + k − g + t) Γ(1 + k − h + t)
where k = 1 + 2a − c − d − e, and the parameters are connected by the relation
                         2 + 3a = b + c + d + e + f + g + h.
     By Lemma 7 the transform (50) rearranges the parameters h as follows:
(51)
b = b123 : h 7→ (1 + 2h0 − h1 − h2 − h3 , h−1 ; 1 + h0 − h2 − h3 , 1 + h0 − h1 − h3 ,
                  1 + h0 − h1 − h2 , h4 , h5 , h6 ).
     Consider the set of 27 complementary parameters e,
          ejk = h0 − hj − hk ,    1 ≤ j < k ≤ 6,          e0k = hk − 1,      1 ≤ k ≤ 6,
(52)
        e0k = h−1 − h0 + hk − 1 = 1 + 2h0 − (h1 + · · · + h6 ) + hk ,             1 ≤ k ≤ 6,
and set
                                     H(e) := F (h).
Then Bailey’s transform can be written as follows:
                      Γ(e01 + 1) Γ(e02 + 1) Γ(e12 + 1) Γ(e05 + 1)
(53)         H(e) =                                               H(be),
                      Γ(e23 + 1) Γ(e13 + 1) Γ(e03 + 1) Γ(e46 + 1)
where b from (51) is the following second-order permutation of the parame-
ters (52):
(54)          b = (e01 e23 )(e02 e13 )(e03 e12 )(e04 e56 )(e05 e46 )(e06 e45 ).
We can also write the transform (53) in the form
             H(e)     H(be)
(55)                =         ,        where Π1 (e) := e01 ! e02 ! e12 ! e05 ! .
             Π1 (e)   Π1 (be)
          WELL-POISED HYPERGEOMETRIC SERVICE FOR ZETA VALUES                                    19

  Further, the h-trivial group (i.e., the group of permutations of the parame-
ters h1 , h2 , . . . , h6 ) is generated by second-order permutations of hk , 1 ≤ k ≤ 5,
and h6 . The action of these five permutations on the set (52) is as follows:
         h1 = (h1 h6 ) = (e01 e06 )(e01 e06 )(e12 e26 )(e13 e36 )(e14 e46 )(e15 e56 ),
         h2 = (h2 h6 ) = (e02 e06 )(e02 e06 )(e12 e16 )(e23 e36 )(e24 e46 )(e25 e56 ),
(56)     h3 = (h3 h6 ) = (e03 e06 )(e03 e06 )(e13 e16 )(e23 e26 )(e34 e46 )(e35 e56 ),
         h4 = (h4 h6 ) = (e04 e06 )(e04 e06 )(e14 e16 )(e24 e26 )(e34 e36 )(e45 e56 ),
         h5 = (h5 h6 ) = (e05 e06 )(e05 e06 )(e15 e16 )(e25 e26 )(e35 e36 )(e45 e46 ),
and the quantity
                 Γ(e03 + 1) Γ(e04 + 1) Γ(e05 + 1) Γ(e06 + 1)
(57)                                                         · H(e)
                 Γ(e12 + 1) Γ(e15 + 1) Γ(e24 + 1) Γ(e36 + 1)
(due to the definition (28)) is stable under the action of (56). Setting
(58)     E = E(e) := {e01 , e02 , e04 , e06 , e01 , e02 , e03 , e05 , e12 , e15 , e24 , e36 }
and combining the above stability results we arrive at the following fact.
Lemma 8. The quantity
                         H(e)                                      Y
                              ,          where Π(e) :=                     ejk !,
                         Π(e)                                     ejk ∈E

is stable under the action of the group
                                 G := hb, h1 , h2 , h3 , h4 , h5 i.
Moreover, the quantities h−1 and
                                                    X
                                       Σ(e) :=              ejk
                                                   ejk ∈E

are also G-stable.
Proof. Routine calculations show the stability of H(e)/Π(e) under the action
of b, h1 , h2 , h3 , h4 , h5 with a help of (55) and (57). Hence H(e)/Π(e) is stable
under the action of the e-permutation group generated by these six permuta-
tions (54), (56).
   The stability of h−1 under the action of (56) is obvious, and b does not
change the parameter h−1 by (51). Finally,
           Σ(e) = 12h0 − 4(h1 + h2 + h3 + h4 + h5 + h6 ) = 4h−1 − 8
that yields the stability of Σ(e) under the action of G. The proof is complete.
                                                                             
  With the help of a C++ program we have discovered that the group G consists
of 51840 elements, hence the left factor G/S6 includes 51840/6! = 72 left
cosets; here S6 is identified with the h-trivial group hh1 , h2 , h3 , h4 , h5 i. It is
20                                           W. ZUDILIN

interesting to mention that the group G0 acting trivially on the set (58) consists
of just 4 elements: g0 = id,
              g1 = (h3 h1 h2 h5 b h1 h4 h5 b h1 )3
                 = (e01 e02 )(e02 e01 )(e03 e06 )(e04 e05 )(e05 e04 )(e06 e03 )
                         (e13 e26 )(e14 e25 )(e15 e24 )(e16 e23 )(e34 e56 )(e35 e46 ),
              g2 = (h1 h2 h4 h2 b h3 h5 h1 h2 )3
                 = (e01 e24 )(e02 e03 )(e03 e46 )(e04 e05 )(e05 e26 )(e06 e01 )
                    (e02 e15 )(e04 e13 )(e06 e35 )(e12 e36 )(e14 e56 )(e25 e34 ),
              g3 = h1 h2 b h3 h1 h5 h2 h3 b = g1 g2
                 = (e01 e15 )(e02 e06 )(e03 e35 )(e05 e13 )(e01 e03 )(e02 e24 )
                         (e04 e26 )(e06 e46 )(e12 e36 )(e14 e34 )(e16 e23 )(e25 e56 ).
Remark. In the most symmetric case (35) all complementary parameters (52)
are equal to n that means that any permutation from G does not change the
quantity F (h). This fact explains why do we dub this case as ‘most symmetric’.

                           6. Denominators of linear forms
   As we have mentioned in Remark to Lemma 6, ‘trivial’ arithmetic (33)
of the linear forms H(e) = F (h) does not lead us to a qualitative result
for ζ(4). We are able to estimate the irrationality measure of ζ(4) under the
following condition, which we have checked numerically for several values of h
satisfying (26) and (27).
Denominator Conjecture. There holds the inclusion4
                    Dm1 Dm2 Dm3 Dm4 · Φ−1 (e) · H(e) ∈ Zζ(4) + Z,
where m1 ≥ m2 ≥ m3 ≥ m4 are the four successive maxima of the set e in (52)
and                                  Y
                         Φ(e) :=          p νp
                                     √
                                                  p>   h−1

with
           $                    % $                   %
            1 1 X ejk      1 X ejk     1 h−1 − 2     1 X ejk
     νp :=               −           =             −           .
            2 4 e ∈E p     8 e ∈E p    2    p        8 e ∈E p
                    jk                  jk                                       jk

   If this conjecture is true, then taking any element g ∈ G and writing con-
clusion of Lemma 8 as
                                                               Π(e)Φ(ge)
     Dm1 Dm2 Dm3 Dm4 H(e) = Dm1 Dm2 Dm3 Dm4 Φ−1 (ge)H(ge) ·
                                                                 Π(ge)
     4In the most symmetric case (35) this conjecture reduces to the conjecture (25) of Sec-
tion 2.
          WELL-POISED HYPERGEOMETRIC SERVICE FOR ZETA VALUES                                            21
                                                     p
we deduce that, for any prime p >                          h−1 ,
                                        Π(e)Φ(ge)
        ordp Dm1 Dm2 Dm3 Dm4 H(e) ≥ ordp
                                           Π(ge)
(59)
                                        $                  %
                    
                X ejk      X e0jk
                                   
                                         1 h−1 − 2
                                                   
                                                       1 X e0jk
             =            −           +              −          ,
               e ∈E
                      p     0
                                  p      2    p        8 0  p
                     jk                    ejk ∈gE                                         ejk ∈gE

where gE = E(ge) and ordp (uζ(4) − v) := min{ordp u, ordp v} for rational
numbers u, v. Finally, setting
                                      Y
                               Λ(e) =   pλp
                                      √
                                                           p>   h−1

with
                                                               $                  0 %!
                 X  ejk                  X  e0jk            1 h−1 − 2
                                                                          
                                                                              1 X  ejk
  λp := max                           −                      +              −            ,
         g∈G                   p                     p          2    p        8 0   p
                 ejk ∈E                   e0jk ∈gE                                        ejk ∈gE

from (59) we obtain the inclusion
(60)                 Dm1 Dm2 Dm3 Dm4 · Λ−1 (e) · H(e) ∈ Zζ(4) + Z.
  Now, to each n = 0, 1, 2, . . . assign the parameters h in accordance with (38)
and set
        ejk = η0 − ηj − ηk ,               1 ≤ j < k ≤ 6,                   e0k = ηk ,   1 ≤ k ≤ 6,
        e0k = η−1 − η0 + ηk = 2η0 − (η1 + · · · + η6 ) + ηk ,                            1 ≤ k ≤ 6,
so that the set of complementary parameters e · n corresponds to the set h.
Then, in the above notation, we can write the inclusion (60) as
               Dm1 n Dm2 n Dm3 n Dm4 n · Λ−1 (en) · H(en) ∈ Zζ(4) + Z.
The asymptotic behaviour of the linear forms H(en) ∈ Qζ(4) + Q and their
coefficients as n → ∞ is determined by Proposition 1; in addition,
                log(Dm1 n Dm2 n Dm3 n Dm4 n )
               lim                            = m1 + m2 + m3 + m4
           n→∞               n
by the consequence (2) of the prime number theorem, while the Chudnovsky–
Rukhadze–Hata arithmetic lemma (see, e.g., [Zu2], Lemma 4.4) yields
                                         Z 1
                           log Λ(en)
                       lim             =      λ(x) dψ(x),
                      n→∞       n          0

where
                     X                                                                           
                                                X                          1           1 X 0
   λ(x) := max                     bejk xc −              be0jk xc +         bη−1 xc −     bejk xc
               g∈G                                                         2           8 0
                          ejk ∈E               e0jk ∈gE                                  ejk ∈gE

is a 1-periodic function.
22                                       W. ZUDILIN

  Recalling the notation of Proposition 1 and combining its results with say-
ing above, as in [RV2], the proof of Theorem 5.1, we arrive at the following
statement.
Proposition 3. Under the denominator conjecture, let
                             C0 = −f0 (τ0 ),
                                         C1 = Re f0 (τ1 ),
                                              Z 1
                     C2 = m1 + m2 + m3 + m4 −     λ(x) dψ(x).
                                                           0

If C0 > C2 , then the irrationality exponent of ζ(4) satisfies the estimate
                                                    C0 + C1
                                    µ(ζ(4)) ≤               .
                                                    C0 − C2
   Recall that the irrationality exponent µ = µ(α) of a real irrational number α
is the least possible exponent such that for any ε > 0 the inequality
                                               p    1
                                       α−        ≤ µ+ε
                                               q  q
has only finitely many solutions in integers p, q with q > 0.
  With a help of Proposition 3 we are able to state the following conditional
result.
Theorem 3. The irrationality exponent of ζ(4) satisfies the estimate
(61)                             µ(ζ(4)) ≤ 25.38983113 . . .
provided that the denominator conjecture holds.
Proof. Taking η = (68, 57; 22, 23, 24, 25, 26, 27) we obtain
         τ0 = 11.83684636 . . . ,              C0 = −f0 (τ0 ) = 37.85606933 . . . ,
         τ1 = 34 + i6.34312459 . . . ,         C1 = Re f0 (τ1 ) = 104.96178579 . . . ,
and
                                               Z 1
           C2 = m1 + m2 + m3 + m4 −                  λ(x) dψ(x)
                                                0
               = 27 + 26 + 25 + 24 − 69.76893283 . . . = 32.23106716 . . . .
Thus, application of Proposition 3 yields the desired estimate (61).                     
     The estimate (61) can be compared with the ‘best known’ estimate
                                µ(ζ(4)) ≤ 204.94259587 . . . ,
which follows from the general result of Yu. Aleksentsev [Al] on approximations
of π by algebraic numbers.5
     5In fact, the result of [Al] is proved for approximations of π by algebraic numbers of
sufficiently large degree.
          WELL-POISED HYPERGEOMETRIC SERVICE FOR ZETA VALUES                                     23

          7. Further difference equations for zeta values
  A natural very-well-poised generalization of Ball’s sequence (9),
                           ∞
                     k−1
                           X                (t − 1) · · · (t − n) · (t + n + 1) · · · (t + 2n)
(62)    Fk,n := n!               (2t + n)
                           t=1
                                                    tk+1 (t + 1)k+1 · · · (t + n)k+1

                                     × (−1)(k−1)(t+n+1)
                  (
                   Qζ(k) + Qζ(k − 2) + · · · + Qζ(2) + Q                     for k ≥ 2 even,
             ∈
                   Qζ(k) + Qζ(k − 2) + · · · + Qζ(3) + Q                     for k ≥ 2 odd,
where n = 1, 2, . . . , gives rise for searching difference equations satisfied by
both linear forms Fk,n and their rational coefficients. Applying Zeilberger’s
algorithm of creative telescoping in the manner of Section 2 we deduce the
following result for the linear forms
(63)                             F5,n = un ζ(5) + wn ζ(3) − vn .
Theorem 4. The numbers un , wn , vn in the representation (63) are positive
rationals satisfying the third-order difference equation
                  (n + 1)(n + 2)5 b0 (n)un+2 − b1 (n)un+1 − b2 (n)un
(64)
                       + 2(2n + 1)n5 b0 (n + 1)un−1 = 0,
        u0 = 2,      w0 = 0, v0 = 0,       u1 = 18, w1 = 66,                    v1 = 98,
                                         6125         74463
                       u2 = 938, w2 =         , v2 =        ,
                                           2             16
where
b0 (n) = 41218n3 + 48459n2 + 20010n + 2871,
b1 (n) = 2(n + 1)(3874492n8 + 33613836n7 + 123666762n6 + 250134420n5
        + 301587620n4 + 220011738n3 + 94372815n2 + 21917736n + 2131500),
b2 (n) = 2(48802112n9 + 350188128n8 + 1080631646n7 + 1882848690n6
        + 2045758212n5 + 1442754107n4 + 663248761n3 + 192486369n2
        + 32136756n + 2360484).
   The characteristic polynomial λ3 − 188λ2 − 2368λ + 4 of the difference equa-
tion (64) determines the asymptotic behaviour of the linear forms (63) and
their coefficients as n → ∞.
   A similar (but quite cumbersome) fourth-order recursion with characteristic
polynomial λ4 − 828λ3 − 132246λ2 + 260604λ − 27 has been discovered by us
for the linear forms F7,n and their coefficients. These recursions allow us to
verify the inclusions
   Dn5 F5,n ∈ Zζ(5) + Zζ(3) + Z,                  Dn7 F7,n ∈ Zζ(7) + Zζ(5) + Zζ(3) + Z
24                                             W. ZUDILIN

up to n = 1000, although we are able to prove that
(65)          e −1
        Dnk+1 Φ n Fk,n ∈ Zζ(k) + Zζ(k − 2) + · · · + Zζ(3) + Z for k odd,
where
(66)
                  Y                         log Φ
                                                en            2 1
     Φ
     e n :=                    p,       lim        = ψ(1) − ψ    − = 0.24101875 . . . ,
                 p<n
                                        n→∞    n               3  2
              {n/p}∈[ 32 ,1)

using our arithmetic results [Zu2], Lemmas 4.2–4.4.
  Another story deals with the quantities
            ∞                                                                     3 
         1 X d2
                            
                               (t − 1) · · · (t − n) · (t + n + 1) · · · (t + 2n)
   Fn :=
   e                 (2t + n)
         2 t=1 dt2                           (t(t + 1) · · · (t + n))2
         =u         en ζ(5) − ven ,
          en ζ(7) + w
where u
      en , w
           en , ven are positive rationals. We have discovered a (quite cumber-
some) fourth-order difference equation satisfied by uen , w
                                                          en , ven ; its characteristic
polynomial is
         λ4 + 9264λ3 − 12116166λ2 − 752300λ − 19683                   (19683 = 39 ).
As we have proved in [Zu2], Proposition 4.1, the following inclusions hold:
                         e −3 · Fen ∈ Zζ(7) + Zζ(5) + Z,
                    D8 · Φ          n     n

where Φe n is given in (66), while our calculations up to n = 1000 with a help
of the recursion mentioned above show that
                            e −2 · Fen ∈ Zζ(7) + Zζ(5) + Z.
                       D7 · Φ       n     n
     What is a trick that makes arithmetic as it is?
                       8. Multiple-integral representation
                    of very-well-poised hypergeometric series
  In [Zu4], Section 9, we conjecture, for integer k ≥ 2, the coincidence of the
very-well-poised hypergeometric series (62) and the multiple integral
                   Z n
                       x1 (1 − x1 )n xn2 (1 − x2 )n · · · xnk (1 − xk )n
              Z
(67) Jk,n := · · ·                                                       dx1 dx2 · · · dxk ,
                                Qk (x1 , x2 , . . . , xk )n+1
                       [0,1]k

where Q0 := 1 and
      Qk = Qk (x1 , x2 , . . . , xk ) := 1 − (1 − (· · · (1 − (1 − xk )xk−1 ) · · · )x2 )x1
(68)
         = 1 − x1 Qk−1 (x2 , . . . , xk ) = Qk−1 (x1 , . . . , xk−1 ) + (−1)k x1 x2 · · · xk
for k ≥ 1. The integrals J2,n and J3,n have been studied by F. Beukers [Be1] in
the connection with Apéry’s proof of the irrationality of ζ(2) and ζ(3). In [Zu4],
we prove the coincidence of F3,n and J3,n with the help of Bailey’s identity
([Ba], Section 6.3, formula (2)) and Nesterenko’s integral theorem ([Ne2], The-
orem 2), and use similar arguments for showing that F2,n = J2,n . For general
           WELL-POISED HYPERGEOMETRIC SERVICE FOR ZETA VALUES                             25

integer k ≥ 2, the integrals (67) are introduced by O. Vasilenko [VaO] who
states several results for Jk,0 . The cases k = 4, 5 and an arbitrary integer n
in (67) are developed by D. Vasilyev [VaD]; in particular, he conjectures the
inclusions

           Dnk Jk,n ∈ Zζ(k) + Zζ(k − 2) + · · · + Zζ(3) + Z for k odd

(cf. (65)), and proves them if k = 5.
   There is a regular way to obtain difference equations for the quantities (67);
it is a part of the general WZ-theory developed by H. Wilf and D. Zeil-
berger [WZ]. However, difference equations for J4,n and J5,n by these means
are out of calculative abilities of our computer, so we cannot use a ‘routine
matter’ to verify the identity Fk,n = Jk,n even when k = 4, 5.
   The aim of this section is to deduce the desired coincidence of (62) and (67)
from a general analytic result on a multiple-integral representation of very-
well-poised hypergeometric series.6
   Consider two objects: very-well-poised hypergeometric series
(69)
                                         Γ(1 + h0 ) kj=1 Γ(hj )
                                                      Q
 Fk (h) = Fk (h0 ; h1 , . . . , hk ) := Qk
                                             j=1 Γ(1 + h0 − hj )
                               h0 , 1 + 12 h0 ,
                                                                                         
                                                    h1 ,      ...,        hk
            × k+2Fk+1                 1                                           (−1)k+1
                                      2
                                        h0 ,    1 + h0 − h1 , . . . , 1 + h0 − hk
            ∞                        Qk
                                        j=0 Γ(hj + µ)
          X
        =      (h0 + 2µ) Qk                                   (−1)(k+1)µ ,
           µ=0                    j=0 Γ(1 + h0 − hj + µ)

and multiple integrals
                                            
                        a0 , a1 , . . . , ak
         Jk (a, b) = Jk
                             b1 , . . . , bk
(70)                        Z Qk           aj −1
                                   j=1 xj        (1 − xj )bj −aj −1
                     Z
                   := · · ·                                         dx1 dx2 · · · dxk .
                                    Qk (x1 , x2 , . . . , xk )a0
                         [0,1]k

Theorem 5. For each k ≥ 1, there holds the identity
      Qk+1
        j=1 Γ(1 + h0 − hj − hj+1 )
                                     · Fk+2 (h0 ; h1 , . . . , hk+2 )
             Γ(h1 ) Γ(hk+2 )
(71)                                                                    
                  h1 ,     h2 ,          h3 ,       ...,          hk+1
           = Jk                                                            ,
                       1 + h0 − h3 , 1 + h0 − h4 , . . . , 1 + h0 − hk+2

  6As it is mentioned by G. E. Andrews in [An], Section 16, “an entire survey paper could
be written just on integrals connected with well-poised series”. The following theorem would
extend this survey a little bit.
26                                  W. ZUDILIN

provided that
                                             k+2
                                        2    X
(72)                      1 + Re h0 >      ·     Re hj ,
                                      k + 1 j=1
(73)       Re(1 + h0 − hj+1 ) > Re hj > 0          for j = 2, . . . , k + 1,
(74)                        h1 , hk+2 6= 0, −1, −2, . . . .
Remark. Condition (72) is required for the absolute convergence of the se-
ries (69) in the unit circle (and, in particular, at the point (−1)k+1 ), while con-
dition (73) ensures the convergence of the corresponding multiple integral (70).
The restriction (74) can be removed by the theory of analytic continuation if
we write Γ(hj + µ)/Γ(hj ) for j = 1, k + 2 as Pochhammer’s symbol (hj )µ when
summing in (69).
  In the case of integral parameters h, the quantities (69) are known to be
Q-linear forms in even/odd zeta values depending on parity of k ≥ 4 (see
[Zu4], Section 9). Therefore, if positive integral parameters a and b satisfy the
additional condition
(75)                  b1 + a2 = b2 + a3 = · · · = bk−1 + ak ,
then the quantities (70) are Q-linear forms in even/odd zeta values. Special-
ization aj = n + 1 and bj = 2n + 2 gives one the desired coincidence of (62)
and (67). The choice aj = rn + 1 and bj = (r + 1)n + 2 in (70) (or, equiv-
alently, h0 = (2r + 1)n + 2 and hj = rn + 1 for j = 1, . . . , k + 2 in (69))
with the integer r ≥ 1 depending on a given odd integer k presents almost the
same linear forms in odd zeta values as considered by T. Rivoal in [Ri1] for
proving his remarkable result on infiniteness of irrational numbers in the set
ζ(3), ζ(5), ζ(7), . . . .
   In addition, we have to mention, under hypothesis (75), the obvious stability
of the quantity
  Fk+2 (h0 ; h1 , . . . , hk+2 )                   Jk (a, b)
        Qk+2                     = Qk+1          Qk+1
          j=1 Γ(hj )                j=2 Γ(hj ) ·  j=1 Γ(1 + h0 − hj − hj+1 )
                                                      Jk (a, b)
                         = Qk                                        Qk
                              j=1 Γ(aj ) · Γ(b1 + a2 − a0 − a1 ) ·     j=1 Γ(bj − aj )

under the action of the (h-trivial) group Gk of order (k + 2)! containing all
permutations of the parameters h1 , . . . , hk+2 . This fact can be applied for
number-theoretic applications as in [RV1], [RV2] and Sections 5, 6 above. In
the cases k = 2 and k = 3 the change of variables (xk−1 , xk ) 7→ (1−xk , 1−xk−1 )
in (70) produces an additional transformation b of both (70) and (69); for k ≥ 4
this transformation is not yet available since condition (75) is broken. The
groups hG2 , bi and hG3 , bi of orders 120 and 1920 respectively are known: see
[Ba], Sections 3.6 and 7.5, for a hypergeometric-series origin and [RV1], [RV2]
for a multiple-integral explanation. G. Rhin and C. Viola make a use of these
groups to discover nice estimates for the irrationality measures of ζ(2) and ζ(3).
          WELL-POISED HYPERGEOMETRIC SERVICE FOR ZETA VALUES                         27

Finally, we want to note that the group Gk can be easily interpretated as the
permutation group of the parameters
  e0l = hl − 1,    1 ≤ l ≤ k + 2,       ejl = h0 − hj − hl ,    1 ≤ j < l ≤ k + 2,
as in Section 5 (see [Zu4], Section 9, for details).
Lemma 9. Theorem 5 is true if k = 1.
Proof. Thanks to a limiting case of Dougall’s theorem,
                                   Γ(h1 ) Γ(h2 ) Γ(h3 ) Γ(1 + h0 − h1 − h2 − h3 )
(76)     F3 (h0 ; h1 , h2 , h3 ) =
                                   Γ(1 + h0 − h1 − h2 ) Γ(1 + h0 − h1 − h3 )
                                                           ×Γ(1 + h0 − h2 − h3 )
(see, e.g., [Ba], Section 4.4, formula (1)), provided that 1 + Re h0 > Re(h1 +
h2 + h3 ) and hj is not a non-positive integer for j = 1, 2, 3. On the other hand,
the integral on the right of (71) has Euler type, that is
                                    Z 1 h2 −1
                                                (1 − x)h0 −h2 −h3
                
                  h1 ,     h2            x
             J1                     =                             dx
                       1 + h0 − h3     0        (1 − x)h1
                                      Γ(h2 ) Γ(1 + h0 − h1 − h2 − h3 )
                                    =                                  ,
                                            Γ(1 + h0 − h1 − h3 )
provided that 1 + Re h0 > Re(h1 + h2 + h3 ) and Re h2 > 0. Therefore, mul-
tiplying equality (76) by the required product of gamma-functions we deduce
identity (71) if k = 1.                                                         
Remark. If we arrange about J0 (a0 ) to be 1, the claim of Theorem 5 remains
valid if k = 0 thanks to another consequence of Dougall’s theorem ([Ba],
Section 4.4, formula (3)).
Lemma 10 ([Ne2], Section 3.2). Let a0 , a, b ∈ C and t0 ∈ R be numbers
satisfying the conditions
         Re a0 > t0 > 0,     Re a > t0 > 0,     and    Re b > Re a0 + Re a.
Then for any non-zero z ∈ C \ (1, +∞) the following identity holds:
        Z 1 a−1
            x (1 − x)b−a−1
                             dx
          0    (1 − zx)a0
(77)                          Z −t0 +i∞
                Γ(b − a) 1              Γ(a0 + t) Γ(a + t) Γ(−t)
             =          ·                                        (−z)t dt,
                 Γ(a0 )   2πi −t0 −i∞           Γ(b + t)
where (−z)t = |z|t eit arg(−z) , −π < arg(−z) < π for z ∈ C \ [0, +∞) and
arg(−z) = ±π for z ∈ (0, 1]. The integral on the right-hand side of (77)
converges absolutely. In addition, if |z| ≤ 1, both integrals in (77) can be
identified with the absolutely convergent Gauss hypergeometric series
                                               ∞
      Γ(a) Γ(b − a)          a0 , a     Γ(b − a) X Γ(a0 + ν) Γ(a + ν) ν
                     · 2F1          z =                               z .
           Γ(b)                   b      Γ(a0 ) ν=0    ν! Γ(b + ν)
  Set εk = 0 for k even and εk = 1 or −1 for k odd.
28                                          W. ZUDILIN

Lemma 11. For each integer k ≥ 2, there holds the relation
                                       
            a0 , a1 , . . . , ak−1 , ak
       Jk
                 b1 , . . . , bk−1 , bk
                                      Z −t0 +i∞
              Γ(bk − ak ) 1                       Γ(a0 + t) Γ(ak + t) Γ(−t)
          =                     ·
                  Γ(a0 )          2πi −t0 −i∞                Γ(bk + t)
                                                                        
                      εk πit            a0 + t, a1 + t, . . . , ak−1 + t
                 ×e           · Jk−1                                       dt,
                                                b1 + t, . . . , bk−1 + t

provided that Re a0 > t0 > 0, Re ak > t0 > 0, Re bk > Re a0 + Re ak , and the
integral on the left converges.

Proof. We start with mentioning that the first recursion in (68) and inductive
arguments yield the inequality
(78)
  0 < Qk (x1 , x2 , . . . , xk ) < 1 for (x1 , x2 , . . . , xk ) ∈ (0, 1)k and k ≥ 1.

By the second recursion in (68), Qk = Qk−1 · (1 − zxk ) for k ≥ 2, where

                                         (−1)k+1 x1 · · · xk−1
                                    z=                             .
                                         Qk−1 (x1 , . . . , xk−1 )

For each (x1 , . . . , xk−1 ) ∈ (0, 1)k−1 , the number z is real with the property
z < 0 for k even and 0 < z < 1 for k odd, since in the last case we have
                   x1 · · · xk−1                             x1 · · · xk−1
       z=                                    =                                           <1
            Qk−1 (x1 , . . . , xk−2 , xk−1 )   Qk−2 (x1 , . . . , xk−2 ) + x1 · · · xk−1

by (78). Therefore, splitting the integral (70) over [0, 1]k = [0, 1]k−1 × [0, 1]
and applying Lemma 10 to the integral

                                     xakk −1 (1 − xk )bk −ak −1
                               Z 1
                                                                dxk
                                0          (1 − zxk )a0

we arrive at the desired relation.                                                            

Proof of Theorem 5. The case k = 1 is considered in Lemma 9. Therefore we
will assume that k ≥ 2, identity (71) holds for k − 1, and, in addition, that
                                    k+1
                                 2 X
(79)                  1 + Re h0 > ·     Re hj ,                Re hk+2 < 1.
                                 k j=1

The restrictions (79) can be easily removed from the final result by the theory
of analytic continuation.
          WELL-POISED HYPERGEOMETRIC SERVICE FOR ZETA VALUES                                  29

  By the inductive hypothesis, for t ∈ C with Re t < 0, we deduce that
                                                                                      
                  h1 + t,       h2 + t,          h3 + t,      ...,         hk + t
       Jk−1
                            1 + h0 − h3 + t, 1 + h0 − h4 + t, . . . , 1 + h0 − hk+1 + t
                    Qk
                      j=1 Γ(1 + h0 − hj − hj+1 )
              =                                      · Fk+1 (h0 + 2t; h1 + t, . . . , hk+1 + t)
                         Γ(h1 + t) Γ(hk+1 + t)
(80)                Qk                                       Z −s0 +i∞
                      j=1 Γ(1 + h0 − hj − hj+1 )        1
              =                                      ·        (h0 + 2t + 2s)
                      Γ(h1 + t) Γ(hk+1 + t)            2πi
                                                      −s0 −i∞

                     Γ(h0 + 2t + s) k+1
                                    Q
                                      j=1 Γ(hj + t + s) Γ(−s) εk−1 πis
                   ×       Qk+1                                e       ds,
                             j=1 Γ(1 + h0 − hj + t + s)

where the real number s0 > 0 satisfies the conditions

Re(h0 +2t) > s0 ,           Re(1+ 12 h0 +t) > s0 ,     Re(hj +t) > s0      for j = 1, . . . , k+1,

and the absolute convergence of the last Barnes-type integral follows from [Ne2],
Lemma 3. Shifting the variable t + s 7→ s in (80) (with a help of the equality
eεk πit · eεk−1 πis = eεk−1 πi(t+s) · eε1 πit ), applying Lemma 11, and interchanging
double integration (thanks to the absolute convergence of the integrals) we
conclude that
                                                                                      
               h1 ,      h2 ,           h3 ,       ...,       hk ,          hk+1
          Jk
                    1 + h0 − h3 , 1 + h0 − h4 , . . . , 1 + h0 − hk+1 , 1 + h0 − hk+2
                    Qk+1
                       j=1 Γ(1 + h0 − hj − hj+1 )
                 =
                                 Γ(h1 )
(81)                       Z −s1 +i∞                    Qk+1
                        1                                 j=1 Γ(hj + s)
                    ×                 (h0 + 2s) Qk+1                         eεk−1 πis
                      2πi −s1 −i∞                    j=1 Γ(1 + h0 − hj + s)
                           Z −t0 +i∞
                        1              Γ(−s + t) Γ(h0 + s + t) Γ(−t) ε1 πit
                    ×                                                    e     dt ds,
                      2πi −t0 −i∞             Γ(1 + h0 − hk+2 + t)

where s1 = s0 + t0 . Since Re hk+2 < 1 and hk+2 6= 0, −1, −2, . . . , the last
Barnes-type integral has the following closed form by Lemma 10:
                    Z −t0 +i∞
               1              Γ(−s + t) Γ(h0 + s + t) Γ(−t) ±πit
                                                            e     dt
              2πi    −t0 −i∞     Γ(1 + h0 − hk+2 + t)
                                        Z 1 h0 +s−1
                             Γ(−s)          x       (1 − x)−hk+2 −s
                     =                                              dx
                        Γ(1 − hk+2 − s) 0         (1 − x)−s
                             Γ(−s)        Γ(h0 + s) Γ(1 − hk+2 )
                     =                  ·
                        Γ(1 − hk+2 − s) Γ(1 + h0 − hk+2 + s)
30                                       W. ZUDILIN

                     Γ(h0 + s) Γ(hk+2 + s) Γ(−s) sin π(hk+2 + s)
                  =                               ·
                    Γ(hk+2 ) Γ(1 + h0 − hk+2 + s)     sin πhk+2
                     Γ(h0 + s) Γ(hk+2 + s) Γ(−s)
                  =
                    Γ(hk+2 ) Γ(1 + h0 − hk+2 + s)
                                                                    
                         πis 1 − i cot πhk+2    −πis 1 + i cot πhk+2
                    × e ·                    +e     ·                  .
                                    2                       2
Substituting this final expression in (81) we obtain
                                                                                
          h1 ,      h2 ,          h3 ,      ...,         hk ,          hk+1
     Jk
               1 + h0 − h3 , 1 + h0 − h4 , . . . , 1 + h0 − hk+1 , 1 + h0 − hk+2
           Qk+1
               j=1 Γ(1 + h0 − hj − hj+1 )
        =
                    Γ(h1 ) Γ(hk+2 )
                 1 − i cot πhk+2 −s1 +i∞
                                 Z
           ×                                 (h0 + 2s)
                         4πi        −s1 −i∞
                       Qk+2
                          j=0 Γ(hj + s) Γ(−s)
                  × Qk+2                           e(εk−1 +1)πis ds
                         j=1 Γ(1 + h0 − hj + s)

                1 + i cot πhk+2 −s1 +i∞
                                 Z
            +                               (h0 + 2s)
                      4πi          −s1 −i∞
                       Qk+2
                          j=0 Γ(hj + s) Γ(−s)
                                                                    
                  × Qk+2                           e(εk−1 −1)πis ds .
                         j=1 Γ(1 + h0 − hj + s)

If k is even, we take εk−1 = −1 in the first integral and εk−1 = 1 in the second
one. Therefore the both integrals are equal to
Z −s1 +i∞           Qk+2
                      j=0 Γ(hj + s) Γ(−s)
          (h0 +2s) Qk+2                    eεk πis ds = 2πi·Fk+2 (h0 ; h1 , . . . , hk+2 )
  −s1 −i∞           j=1 Γ(1 + h0 − hj + s)

that gives the desired identity (71). The proof of Theorem 5 is complete.              

  Another family of multiple integrals
                      Z Qk        aj −1
                            j=1 xj      (1 − xj )bj −aj −1
                 Z
(82)    S(z) := · · ·     Qm                                 ci
                                                                dx1 dx2 · · · dxk ,
                             i=1 (1 −  zx 1 x 2 · · · x r i
                                                            )
                       [0,1]k

                                1 ≤ r1 < r2 < · · · < rm = k,
is known due to works of V. Sorokin [So2], [So3]. Recently, S. Zlobin [Zl1],
[Zl2] has proved (in more general settings) that the integrals (70) can be re-
duced to the form (82) with z = 1. Therefore, Theorem 5 gives one a way
to reduce the integrals S(1) to the very-well-poised hypergeometric series (69)
under certain conditions on the parameters aj , bj , ci , and ri in (82). In addi-
tion, Zlobin [Zl1] shows that, for integral parameters in (82) satisfying natural
            WELL-POISED HYPERGEOMETRIC SERVICE FOR ZETA VALUES                             31

restrictions of convergence, the integral S(z) is a Q[z −1 ]-linear combination of
modified multiple polylogarithms
            X               z n1
                        s1 s2          sl with sj ≥ 1, sj ∈ Z, j = 1, . . . , l,
       n ≥n ≥···≥n ≥1
                      n 1 n 2  · · · n l
        1   2      l

where 0 ≤ s1 + s2 + · · · + sl ≤ k and 0 ≤ l ≤ m.
   Following a spirit of this section, we would like to finish the paper with the
following
Problem. Find a multiple integral over [0, 1]5 that represents the series (30)
(or, equivalently, the integral (34)) of Section 3.

                                      References
[Al]    Yu. M. Aleksentsev, On the measure of approximation for the number π by alge-
        braic numbers, Mat. Zametki [Math. Notes] 66:4 (1999), 483–493.
[An]    G. E. Andrews, The well-poised thread: An organized chronicle of some amazing
        summations and their implications, The Ramanujan J. 1:1 (1997), 7–23.
[Ap]    R. Apéry, Irrationalité de ζ(2) et ζ(3), Astérisque 61 (1979), 11–13.
[Ba]    W. N. Bailey, Generalized hypergeometric series, Cambridge Math. Tracts 32
        (Cambridge Univ. Press, Cambridge, 1935); 2nd reprinted edition (Stechert-Hafner,
        New York–London, 1964).
[BR]    K. Ball, T. Rivoal, Irrationalité d’une infinité de valeurs de la fonction zêta aux
        entiers impairs, Invent. Math. 146:1 (2001), 193–207.
[Be1]   F. Beukers, A note on the irrationality of ζ(2) and ζ(3), Bull. London Math. Soc.
        11:3 (1979), 268–272.
[Be2]   F. Beukers, Padé approximations in number theory, Lecture Notes in Math. 888
        (Springer-Verlag, Berlin, 1981), 90–99.
[Be3]   F. Beukers, Irrationality proofs using modular forms, Astérisque 147–148 (1987),
        271–283.
[Be4]   F. Beukers, On Dwork’s accessory parameter problem, Math. Z. 241:2 (2002),
        425–444.
[Br]    N. G. de Bruijn, Asymptotic methods in analysis (North-Holland Publ., Amster-
        dam, 1958).
[Co]    H. Cohen, Accélération de la convergence de certaines récurrences linéaires,
        Séminaire de Théorie des nombres de Bordeaux (Année 1980–81), exposé 16, 2 pages.
[Gu]    L. A. Gutnik, On the irrationality of certain quantities involving ζ(3), Uspekhi Mat.
        Nauk [Russian Math. Surveys] 34:3 (1979), 190; Acta Arith. 42:3 (1983), 255–264.
[Han]   J. Hancl, A simple proof of the irrationality of π 4 , Amer. Math. Monthly 93 (1986),
        374–375.
[Hat]   M. Hata, Legendre type polynomials and irrationality measures, J. Reine Angew.
        Math. 407:1 (1990), 99–125.
[JT]    W. B. Jones, W. J. Thron, Continued fractions. Analytic theory and applications,
        Encyclopaedia Math. Appl. Section: Analysis 11 (Addison-Wesley, London, 1980).
[Ne1]   Yu. V. Nesterenko, A few remarks on ζ(3), Mat. Zametki [Math. Notes] 59:6
        (1996), 865–880.
[Ne2]   Yu. V. Nesterenko, Integral identities and constructions of approximations to zeta
        values, Actes des 12èmes rencontres arithmétiques de Caen (June 29–30, 2001), J.
        Théor. Nombres Bordeaux, this issue (2003).
[Ne3]   Yu. V. Nesterenko, Arithmetic properties of values of the Riemann zeta function
        and generalized hypergeometric functions, in preparation (2002).
32                                       W. ZUDILIN

[PWZ] M. Petkovšek, H. S. Wilf, D. Zeilberger, A = B (A. K. Peters, Ltd., Wellesley,
      MA, 1997).
[Po]  A. van der Poorten, A proof that Euler missed... Apéry’s proof of the irrationality
      of ζ(3), An informal report, Math. Intelligencer 1:4 (1978/79), 195–203.
[RV1] G. Rhin, C. Viola, On a permutation group related to ζ(2), Acta Arith. 77:1
      (1996), 23–56.
[RV2] G. Rhin, C. Viola, The group structure for ζ(3), Acta Arith. 97:3 (2001), 269–293.
[Ri1] T. Rivoal, La fonction zêta de Riemann prend une infinité de valeurs irrationnelles
      aux entiers impairs, C. R. Acad. Sci. Paris Sér. I Math. 331:4 (2000), 267–270.
[Ri2] T. Rivoal, Propriétés diophantiennes des valeurs de la fonction zêta de Riemann
      aux entiers impairs, Thèse de Doctorat (Univ. de Caen, Caen, 2001).
[Ri3] T. Rivoal, Séries hypergéométriques et irrationalité des valeurs de la fonction zêta,
      Journées arithmétiques (Lille, July, 2001), J. Théor. Nombres Bordeaux, to appear
      (2003).
[So1] V. N. Sorokin, Hermite–Padé approximations for Nikishin’s systems and irrational-
      ity of ζ(3), Uspekhi Mat. Nauk [Russian Math. Surveys] 49:2 (1994), 167–168.
[So2] V. N. Sorokin, A transcendence measure of π 2 , Mat. Sb. [Russian Acad. Sci. Sb.
      Math.] 187:12 (1996), 87–120.
[So3] V. N. Sorokin, Apéry’s theorem, Vestnik Moskov. Univ. Ser. I Mat. Mekh. [Moscow
      Univ. Math. Bull.] 53:3 (1998), 48–52.
[So4] V. N. Sorokin, One algorithm for fast calculation of π 4 , Preprint (Russian Acad-
      emy of Sciences, M. V. Keldysh Institute for Applied Mathematics, Moscow, 2002),
      59 pages; http://www.wis.kuleuven.ac.be/applied/intas/Art5.pdf.
[VaO] O. N. Vasilenko, Certain formulae for values of the Riemann zeta-function at inte-
      gral points, Number theory and its applications, Proceedings of the science-theoretic
      conference (Tashkent, September 26–28, 1990), 27 (Russian).
[VaD] D. V. Vasilyev, On small linear forms for the values of the Riemann zeta-function
      at odd points, Preprint no. 1 (558) (Nat. Acad. Sci. Belarus, Institute Math., Minsk,
      2001).
[Vi]  C. Viola, Birational transformations and values of the Riemann zeta-function,
      Actes des 12èmes rencontres arithmétiques de Caen (June 29–30, 2001), J. Théor.
      Nombres Bordeaux, this issue (2003).
[WZ] H. S. Wilf, D. Zeilberger, An algorithmic proof theory for hypergeometric (or-
      dinary and “q”) multisum/integral identities, Invent. Math. 108:3 (1992), 575–633.
[Zl1] S. A. Zlobin, Integrals expressible as linear forms in generalized polylogarithms,
      Mat. Zametki [Math. Notes] 71:5 (2002), 782–787.
[Zl2] S. A. Zlobin, On some integral identities, Uspekhi Mat. Nauk [Russian Math. Sur-
      veys] 57:3 (2002), 153–154.
[Zu1] W. Zudilin, Difference equations and the irrationality measure of numbers, Collec-
      tion of papers: Analytic number theory and applications, Trudy Mat. Inst. Steklov
      [Proc. Steklov Inst. Math.] 218 (1997), 165–178.
[Zu2] W. Zudilin, Irrationality of values of Riemann’s zeta function, Izv. Ross. Akad.
      Nauk Ser. Mat. [Russian Acad. Sci. Izv. Math.] 66:3 (2002), 49–102.
[Zu3] W. V. Zudilin, One of the numbers ζ(5), ζ(7), ζ(9), ζ(11) is irrational, Uspekhi Mat.
      Nauk [Russian Math. Surveys] 56:4 (2001), 149–150.
[Zu4] W. Zudilin, Arithmetic of linear forms involving odd zeta values, J. Théor. Nombres
      Bordeaux, submitted for publication (2002).
[Zu5] W. Zudilin, An elementary proof of Apéry’s theorem, E-print math.NT/0202159
      (February 2002).
      WELL-POISED HYPERGEOMETRIC SERVICE FOR ZETA VALUES   33

Department of Mechanics and Mathematics
Moscow Lomonosov State University
Vorobiovy Gory, GSP-2
119992 Moscow
Russia
URL: http://wain.mi.ras.ru/index.html
E-mail address: wadim@ips.ras.ru
