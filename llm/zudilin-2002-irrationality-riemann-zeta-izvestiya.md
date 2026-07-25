---
title: "zudilin-2002-irrationality-riemann-zeta-izvestiya"
source: "books-and-surveys/zudilin-2002-irrationality-riemann-zeta-izvestiya.pdf"
conversion: pdftotext -layout
note: "extracted text; formulas are flattened and may be lossy — check the PDF for anything load-bearing"
---

Izvestiya: Mathematics 66:3 489–542                               2002
                                                                  c     RAS(DoM) and LMS
Izvestiya RAN : Ser. Mat. 66:3 49–102                  DOI 10.1070/IM2002v066n03ABEH000387

       Irrationality of values of the Riemann zeta function

                                         W. Zudilin

   Abstract. The paper deals with a generalization of Rivoal’s construction, which
   enables one to construct linear approximating forms in 1 and the values of the
   zeta function ζ(s) only at odd points. We prove theorems on the irrationality of the
   number ζ(s) for some odd integers s in a given segment of the set of positive integers.
   Using certain reﬁned arithmetical estimates, we strengthen Rivoal’s original results
   on the linear independence of the ζ(s).

                                        Introduction
   The study of the arithmetical nature of the values of the Riemann zeta function
                                                 ∞
                                                  1
                                        ζ(s) =
                                                 n=1
                                                       ns

at integers s > 1 is one of the most attractive topics of the modern number theory.
In spite of the deceptive simplicity of this problem, the results obtained in this area
in the course of more than two centuries are far from being exhaustive. Euler’s
formula
                                 (2πi)s Bs
                        ζ(s) = −           ,     s = 2, 4, 6, . . .,
                                    2s!
in which the values of the zeta function at even integers are expressed in terms
of π ≈ 3.1415926 and the Bernoulli numbers Bs ∈ Q, which are deﬁned by the
generating function
                               ∞
                  t         t  ts
                      = 1 −  +    Bs ,                 Bs = 0 for odd s ⩾ 3,
               et − 1       2 s=2   s!

undoubtedly marked the ﬁrst progress in this area. In 1882 Lindemann proved
that π is a transcendental number, which implies that ζ(s) is transcendental if s is
even.
   The problem of the irrationality of the values of the zeta function at odd integers
seemed inaccessible until 1978, when Apéry [1] produced a sequence of rational
approximations proving that ζ(3) is irrational.

   This research was supported in part by INTAS and the Russian Foundation for Basic Research
(grant no. IR-97-1904).
   AMS 2000 Mathematics Subject Classiﬁcation. 11J81, 11M06.
490                                         W. Zudilin

Apéry’s Theorem. The number ζ(3) is irrational.
   The history of this discovery and a rigorous mathematical justiﬁcation of Apéry’s
observations can be found in [2]. The phenomenon of Apéry’s sequence was repeat-
edly interpreted from the point of view of various analytical methods of number
theory (see [3]–[8]). New approaches made it possible to strengthen Apéry’s result
quantitatively, that is, to obtain a “good” measure of the irrationality of ζ(3) ([9]
and [10] represent the latest stages of the competition in this area).
   Unfortunately, natural generalizations of Apéry’s construction involve linear
forms containing values of the zeta function at both odd and even integers (the
interest in which faded after the Euler–Lindemann result). This circumstance
makes it impossible to obtain results on the irrationality of ζ(s) for odd s ⩾ 5
by this method. Interesting attempts to approach this problem can be found in the
preprints [11] and [12].
   Finally, in 2000 Rivoal [13] equipped an auxiliary rational function with a sym-
metry and constructed linear forms containing the values of the zeta function only
at odd integers s > 1.
Rivoal’s Theorem. The sequence ζ(3), ζ(5), ζ(7), . . . contains inﬁnitely many
irrational numbers. More precisely, the following estimate holds for the dimen-
sion δ(a) of the spaces generated over Q by 1, ζ(3), ζ(5), . . ., ζ(a − 2), ζ(a) with an
odd integer a:
                               log a          
                      δ(a) ⩾           1 + o(1) ,      a → ∞.
                             1 + log 2
   In this paper we generalize Rivoal’s construction [13] and prove the following
theorems.
Theorem 0.1. Each of the sets

          {ζ(5), ζ(7), ζ(9), ζ(11), ζ(13), ζ(15), ζ(17), ζ(19), ζ(21)},
                                                                                           (0.1)
      {ζ(7), ζ(9), . . . , ζ(35), ζ(37)},        {ζ(9), ζ(11), . . . , ζ(51), ζ(53)}

contains at least one irrational number.1
Theorem 0.2. For every odd integer b ⩾ 1 at least one of the numbers

                      ζ(b + 2), ζ(b + 4), . . . , ζ(8b − 3), ζ(8b − 1)

is irrational.
Theorem 0.3. There are odd integers a1 ⩽ 145 and a2 ⩽ 1971 such that 1, ζ(3),
ζ(a1 ), ζ(a2 ) are linearly independent over Q.
   Theorem 0.3 strengthens the corresponding theorem in [15], where it was estab-
lished that 1, ζ(3), ζ(a) with some odd integer a ⩽ 169 are linearly independent.
   1 When the work on this paper was ﬁnished, I was informed that Rivoal [14] had obtained the

assertion of Theorem 0.1 for the ﬁrst set in (0.1) independently, using another generalization of
the construction in [13].
    Added in proof. I have recently obtained some reﬁnements of Theorem 0.1. In particular, I
have shown [28] that at least one of the four numbers ζ(5), ζ(7), ζ(9), ζ(11) is irrational.
                        Irrationality of values of the zeta function                 491

Theorem 0.4. The following absolute estimate holds for every odd integer a ⩾ 3:

                                                   2   log a
                          δ(a) > 0.395 log a >       ·         .                    (0.2)
                                                   3 1 + log 2

   This paper is organized as follows. In § 1 we describe an analytical construction
of linear forms in the values of the zeta function at odd integers. In §§ 2–4 we
study the asymptotics of linear forms, their coeﬃcients and denominators. Finally,
in § 5 we give complete proofs of the results. The main ingredient in the proofs of
Theorems 0.3 and 0.4 (as well as in [13]) is the following special case of Nesterenko’s
theorem [16].
Criterion for linear independence. Assume that for a given set of real numbers
θ0 , θ1 , . . . , θm , m ⩾ 1, one can ﬁnd a sequence of linear forms

              In = A0,n θ0 + A1,n θ1 + · · · + Am,n θm ,        n = 1, 2, . . . ,

with integer coeﬃcients and numbers α > 0 and β > 0 such that
                                                    
             log |In | = −nα + o(n), log max |Aj,n| ⩽ nβ + o(n)
                                               0⩽j⩽m

as n → ∞. Then
                                                                   α
                      dimQ (Qθ0 + Qθ1 + · · · + Qθm ) ⩾ 1 +          .
                                                                   β

   Let us note that the justiﬁcation of Theorems 0.1–0.4 is based on the saddle-point
method and follows the scheme of proof of Apéry’s theorem in [8]. It should be
noted that some arithmetical results for the values of polylogarithms were obtained
in [17], where the saddle-point method was used. The dissertation [17] served a
link between our empirical observations and the rigorous justiﬁcation in § 2. In § 4
we improve the arithmetical estimates (for the denominators of numerical linear
forms) following [18], [9], [10], which enables us to reﬁne the lower estimate for δ(a)
in Theorems 0.3 and 0.4 for small values of a. Finally, in § 3 we obtain an upper
estimate for the coeﬃcients of linear forms and asymptotics of their growth.
   The main results of this paper were announced in [19].
  I am grateful to Professor Yu. V. Nesterenko for his constant interest and valuable
advice, which have enabled me to improve this paper.

                         § 1. An analytical construction
  In this section we describe an analytical construction that enables us to obtain
“good” linear forms with rational coeﬃcients in the values of the zeta function at
odd integers.
  Let us ﬁx positive integer parameters a, b, r such that 2rb ⩽ a and a + b is even.
For every positive integer n we consider the rational function
                                                             b
                           (t ± (n + 1)) · · · (t ± (n + 2rn))
         R(t) = Rn (t) :=                              a       · (2n)!a−2rb .     (1.1)
                                  t(t ± 1) · · · (t ± n)
492                                       W. Zudilin

Here and below (t ± l) means that the product (sum or set) contains the factors
(summands or elements) t − l and t + l. We assign to the function deﬁned by (1.1)
the sum
                                  ∞
                                           1    db−1 R(t)
                       I = In :=                          .                 (1.2)
                                 t=n+1
                                        (b − 1)! dtb−1

   It is easy to see that the sum in (1.2) is taken only over integers t > n + 2rn.
The series on the right-hand side of (1.2) converges absolutely, since the degrees of
the numerator and the denominator of the rational function (1.1) are equal to 4rbn
and a(2n + 1) ⩾ 4rbn + a ⩾ 4rbn + 2, respectively, whence
                                                   
                          1           db−1 R(t)       1
              R(t) = O 2        and             = O      ,     t → ∞.           (1.3)
                         t              dtb−1         t2

Applying Laplace’s method to the integral representation of the sum in formula (1.2),
we can calculate the quantity
                                           log |In |
                                 κ = lim             > −∞                                    (1.4)
                                       n→∞    n
(the details can be found in § 2 below), following [8] and [17].
Lemma 1.1. For every n = 1, 2, . . . the number deﬁned by formula (1.2) is a linear
form in 1 and the values of the zeta function at odd integers s, b < s < a + b:
                                   
                             I=          Ās ζ(s) − Ā0 .                       (1.5)
                                       s is odd
                                      b<s<a+b

Proof. Decomposing the function (1.1) into a sum of partial fractions
                          n 
                                                           
                                Ak,a           Ak,2    Ak,1
                   R(t) =              +···+         +       ,                               (1.6)
                              (t + k)a       (t + k)2 t + k
                          k=−n

we note that
                                
                                n
                                      Ak,1 = − Res R(t) = 0                                  (1.7)
                                                  t=∞
                               k=−n

by (1.3). Since the function (1.1) is even (odd), that is,

                                     R(−t) = (−1)a R(t),                                     (1.8)

and the decomposition (1.6) is unique, we have

             Ak,j = (−1)a−j A−k,j ,       k = 0, ±1, . . . , ±n,     j = 1, 2, . . . , a.

Hence,
      
      n                       
                              n
             Ak,j = (−1)a−j          Ak,j = 0     if a − j is odd,       j = 2, . . . , a.   (1.9)
      k=−n                    k=−n
                              Irrationality of values of the zeta function                       493

   Substituting (1.6) into (1.2), we obtain that
                 ∞
                       n 
                                 
     b−1                    a+b−2                  Ak,a
(−1)       I=
                t=n+1 k=−n
                            b−1                (t + k)a+b−1
                                                                          
                     a+b−3      Ak,a−1              b      Ak,2        Ak,1
                  +                       +···+                    +            .
                      b−1    (t + k)a+b−2         b − 1 (t + k)b+1   (t + k)b

Simple transformations yield the formula

       I = Āa+b−1 ζ(a + b − 1) + Āa+b−2 ζ(a + b − 2) + · · · + Āb ζ(b) − Ā0 ,             (1.10)

where
                                   n
                              j−1 
         Āj = (−1)    b−1
                                       Ak,j−b+1,              j = b, b + 1, . . . , a + b − 1, (1.11)
                               b−1
                                      k=−n

                            a + b − 2 Ak,a
                         n k+n                         
                                                           b
                                                              
                                                                Ak,2 Ak,1
                                                                          
   Ā0 = (−1)    b−1
                                                 +···+              + b .
                                  b−1     la+b−1         b − 1 lb+1   l
                       k=−n l=1
                                                                          (1.12)

   By (1.7), we have Āb = 0. Hence, the expression on the right-hand side of (1.10)
is well deﬁned even in the case when b = 1. Since a+b is even, formula (1.9) implies
that Āj = 0 if j ⩾ b is even. Hence, formula (1.10) means that I is a linear form
in 1 and the values of the zeta function at odd integers s, b + 1 ⩽ s ⩽ a + b − 1, as
was to be shown.
   The following lemma enables us to calculate the denominators of linear
forms (1.2).
Lemma 1.2 (cf. [20], [13]). Assume that for some polynomial P (t) of degree ⩽ n
the rational function

                                                    P (t)
                             R(t) =                                                           (1.13)
                                      (t + s)(t + s + 1) · · · (t + s + n)

(this representation does not have to be irreducible) satisﬁes the conditions
                            
                  R(t)(t + k) t=−k ∈ Z,      k = s, s + 1, . . . , s + n.    (1.14)

Then                                 
                Dnj dj            
                        R(t)(t + k)       ∈ Z,            k = s, s + 1, . . . , s + n,
                j! dtj                 t=−k

for all non-negative integers j, where Dn is the least common multiple of 1, 2, . . . , n.
Proof. Decomposing the rational function (1.13) into a sum of partial fractions, we
obtain that
                                        Bl
                                       s+n
                               R(t) =           ,
                                           t+l
                                                   l=s
494                                        W. Zudilin

where                          
                Bl = R(t)(t + l) t=−l ∈ Z,             l = s, s + 1, . . . , s + n.
Therefore,
                                   
                                   s+n
                                             t+k         
                                                        s+n
                                                                   k−l
                                                                       
             R(t)(t + k) = Bk +           Bl     = Bk +     Bl 1 +      ,
                                             t+l                   t+l
                                   l=s                        l=s
                                   l=k                       l=k

whence
                                          Bl (k − l)             Bl
        1 dj                           s+n                       s+n
               R(t)(t + k)       = (−1)j                      = −              .
        j! dtj                               (t + l)j+1               (k − l)j
                             t=−k             l=s          t=−k               l=s
                                              l=k                            l=k

This completes the proof of the assertion.
Remark 1.1. Lemma 1.2 was stated by Nesterenko [21]. Nikishin [20] applied it to
the polynomial
                      P (t) = (t + p + 1) · · · (t + p + n)
with p − s ∈ Z and p + n < s or p ⩾ s + n. Rivoal observed [13] that (1.14) holds
for P (t) = n! . In each of these cases Bk , k = s, s + 1, . . . , s + n, are binomial
coeﬃcients, and (1.14) is easily veriﬁed.
   It is easy to see that the rational function (1.1) can be written as a product of
the functions
                                 (t ± (m + 1)) · · · (t ± (m + 2n))
           F (t) = Fn,m (t) :=                               2    ,           n ⩽ m,   (1.15)
                                        t(t ± 1) · · · (t ± n)
                                     (2n)!
           H(t) = Hn (t) :=                                                              (1.16)
                              t(t ± 1) · · · (t ± n)
(see formula (1.22) below).
Lemma 1.3. The following inclusions hold for functions (1.15) and (1.16):
                           
     j
   D2n  dj               
                         2 
             F (t)(t + k)        ∈ Z, k = 0, ±1, . . . , ±n, j = 0, 1, 2, . . .,
    j! dtj                   t=−k                                              (1.17)
                           
      j
   D2n d  j              
           j
              H(t)(t + k)       ∈ Z, k = 0, ±1, . . . , ±n, j = 0, 1, 2, . . .,
     j! dt                   t=−k                                              (1.18)

where D2n is the least common multiple of 1, 2, . . . , 2n.
Proof. The inclusions (1.18) follow from Lemma 1.2 applied to the rational func-
tion (1.16). We prove (1.17) using Lemma 1.2 for the rational functions
                                (t − (m + 1)) · · · (t − (m + 2n))
                       R− (t) =                                    ,
                                       t(t ± 1) · · · (t ± n)
                                                                                         (1.19)
                                (t + (m + 1)) · · · (t + (m + 2n))
                       R+ (t) =
                                       t(t ± 1) · · · (t ± n)
                         Irrationality of values of the zeta function                          495

and the Leibniz rule for the jth derivative of the product R−(t)R+ (t) = F (t). The
assumptions (1.14) hold for each rational function in (1.16) and (1.19), since
                                                                          
                                          (2n)!                      2n
       H(t)(t + k) t=−k = (−1)n+k                       = (−1)n+k           ∈ Z,
                                       (n + k)! (n − k)!               n+k
                                                                        
                                          m + 2n + k                 2n
                  R−(t)(t + k) t=−k =                     · (−1)n+k         ∈ Z,
                                                 2n                    n+k
                                                                        
                                          m + 2n − k                 2n
                  R+ (t)(t + k) t=−k =                    · (−1)n+k         ∈Z
                                                 2n                    n+k
for all k = 0, ±1, . . . , ±n. This completes the proof of the lemma.
   In what follows the denominator den(I) of the linear form I = A0 +
A1 θ1 + · · · + Am θm is deﬁned to be the least rational (not necessarily integer)
D > 0 such that every DA0 , DA1 , . . . , DAm is an integer.
Lemma 1.4. The following inclusions hold for the coeﬃcients of the linear
form (1.5):
                            a+b−1−s
                          D2n       Ās ∈ Z,                       (1.20)
                                                                               a+b−1
where s is zero or an odd integer, b < s < a + b. Therefore, den(In ) divides D2n
and
                                                a+b−1
                     log den(In )         log D2n
                 lim              ⩽ lim               = 2(a + b − 1).          (1.21)
                n→∞       n          n→∞       n
Proof. To determine the coeﬃcients in (1.6), we use the formula
                                   
          1     da−j             
                                 a 
Ak,j =                R(t)(t + k)      ,     k = 0, ±1, . . . , ±n,            j = 1, 2, . . . , a,
       (a − j)! dta−j                    t=−k
and the representation
        R(t) = (Hn (t))a−2rb (Fn,n(t))b (Fn,3n (t))b · · · (F(2r−1)n,n(t))b                (1.22)
of the rational function (1.1). The inclusions
               a−j
              D2n  Ak,j ∈ Z,         k = 0, ±1, . . . , ±n,   j = 1, 2, . . ., a,          (1.23)
follow from Lemma 1.3 and the Leibniz rule for the diﬀerentiation of a product.
Inclusions (1.20) follow from (1.11), (1.12) and (1.23). The limiting relation (1.21)
follows from the formula
                                        log Dn
                                   lim         =1                              (1.24)
                                  n→∞      n
(the prime number theorem). This completes the proof of the lemma.
   So we have constructed a sequence of linear forms In , n = 1, 2, . . . . By (1.4),
                                                                            a+b−1
it contains an inﬁnite subsequence of non-zero forms. The forms D2n               In ,
n = 1, 2, . . . , have integer coeﬃcients. Hence, for
                                  κ + 2(a + b − 1) < 0                                     (1.25)
at least one of the numbers ζ(s), where s is an odd integer and b < s < a + b, is
irrational. Moreover, upper estimates for the coeﬃcients of the linear forms (1.10)
in the case when (1.25) holds enable us to obtain a lower estimate for the number
of irrational numbers in the given set of values of the zeta function. This is why our
next step will be to calculate (1.4) and to ﬁnd the asymptotics of the coeﬃcients
of the linear forms (1.10) as n → ∞.
496                                        W. Zudilin

                 § 2. An asymptotic estimate for linear forms
  We shall need some supplementary properties of the function cot z.
Lemma 2.1. The maximum value of the real-valued non-negative function h(y) =
| cot(x + iy)|, y ∈ R, depends only on x (mod πZ) ∈ R.
Proof. If x = πk for some integer k, then z = x is a (unique) pole of the func-
tion cot z on the line Im z = x (see (2.6) below). Therefore, in this case the
absolute maximum of h(y), which is equal to inﬁnity, is attained at y = 0. In what
follows we assume that x ∈   / πZ, whence cos 2x < 1. We have
                                                                             
                    cos(x + iy) 2  (e−y + ey ) cos x + i(e−y − ey ) sin x 2
          h(y)2 =                =                                          
                     sin(x + iy)       (e−y − ey ) cos x + i(e−y + ey ) sin x 
                   e−2y + e2y + 2 cos 2x                   4 cos 2x
                = −2y                       = 1 + −2y
                   e     + e2y − 2 cos 2x           e     + e2y − 2 cos 2x
                          4| cos 2x|
                ⩽1+                  .                                            (2.1)
                        2 − 2 cos 2x
Here we have used the inequality Y + 1/Y ⩾ 2 for Y = e−2y > 0, which becomes an
equality only in the case when Y = 1. The estimate on the right-hand side of (2.1)
depends only on x (mod πZ), which completes the proof of the lemma.
  We deﬁne “diﬀerential iterations” of the cotangent:

                                  (−1)b−1 db−1 cot z
                    cotb z =                         ,       b = 1, 2, . . . .          (2.2)
                                  (b − 1)! dz b−1

Lemma 2.2. For every b = 1, 2, . . .
  (a) the function cotb z is a polynomial in cot z with rational coeﬃcients:

            cotb z = Ub (cot z),         Ub (−y) = (−1)b Ub (y),        deg Ub = b;

  (b) the function sinb z · cotb z is a polynomial in cos z with rational coeﬃcients:

  sinb z · cotb z = Vb (cos z),        Vb (−y) = (−1)b Vb (y),     deg Vb = max{1, b − 2}.
                                                                                        (2.3)
Proof. We proceed by induction. For b = 1 we have cot1 z = cot z and
sin z · cot1 z = cos z, whence U1 (y) = V1 (y) = y.
   (a) According to the diﬀerential equation

                             dy
                                = −(y2 + 1),             y = cot z,
                             dz
and formula (2.2), the following recurrence relation holds for the polynomials Ub (y),
b = 1, 2, . . . :
                               1
                    Ub+1 (y) = (y2 + 1)Ub (y),      b = 2, 3, . . . .
                               b
The induction step from b to b + 1 shows that Ub+1 (−y) = (−1)b+1 Ub+1 (y) and the
degree of Ub+1 is one greater than the degree of Ub .
                           Irrationality of values of the zeta function                497

  (b) Assume that (2.3) holds for some integer b ⩾ 1. Then
                    d                       d
          sin z ·      Vb (cos z) = sin z ·    (sinb z · cotb z)
                    dz                      dz
                                                                          d
                                 = b cos z · sinb z · cotb z + sinb+1 z ·    cotb z
                                                                          dz
                                 = b cos z · Vb (cos z) − b sinb+1 z · cotb+1 z,

whence
                                                         1         d
            sinb+1 z · cotb+1 z = cos z · Vb (cos z) −     sin z ·    Vb (cos z)
                                                         b         dz
                                                         1
                                   = cos z · Vb (cos z) + sin2 z · Vb (cos z)
                                                         b
                                   = Vb+1 (cos z),

where
                                                 1
                             Vb+1 (y) = yVb (y) + (1 − y2 )Vb (y).            (2.4)
                                                 b
   Formula (2.4) and the induction hypothesis imply that Vb+1 (y) is a polynomial
whose degree cannot exceed the degree of Vb (y) more than by one. Besides,
Ub+1 (−y) = (−1)b+1 Ub+1 (y). Since V2 (y) = 1 (by (2.4)), we have deg Vb+1 ⩽ b − 1.
The induction step from b to b+1 and relation (2.4) show that the coeﬃcient of yb−1
in the polynomial Vb+1 (y) is non-zero and equals 2b−1 /b! . Hence, (2.3) holds for
all b = 1, 2, . . . , which completes the proof of the lemma.
Lemma 2.3. For any b = 1, 2, . . . and any integer k the following representation
holds in the neighbourhood of t = k:
                                                   1
                               πb cotb πt =             + O(1),                       (2.5)
                                               (t − k)b
where the function in O(1) is analytic in the neighbourhood of t = k. The function
cotb πt is analytic in the neighbourhood of t ∈ C \ Z
Proof. The second assertion of the lemma follows from formula (2.2) deﬁning the
function cotb z and the decomposition of the cotangent into a sum of partial frac-
tions:
                                      ∞                 
                                 1          1       1
                      π cot πt = +               +                           (2.6)
                                 t m=1 t − m t + m
(see, for example, [22], Ch. X, § 3, formula (3)).
   In the neighbourhood of t = k ∈ Z we have
                                                  ∞                     
                                         1                (2πi)s (t − k)s
           π cot πt = π cot π(t − k) =       · 1+      Bs                  ,          (2.7)
                                        t−k        s=2
                                                                 s!

where Bs , s = 2, 3, . . . , are the Bernoulli numbers (see, for example, [22], Ch. X,
§ 3, formula (2)). Diﬀerentiating identity (2.7) b − 1 times, we obtain representa-
tion (2.5) and the ﬁrst assertion of the lemma, which completes the proof.
498                                         W. Zudilin

Lemma 2.4. The following integral representation holds for the sum in (1.2):
                                             M +i∞
                                 π b−1 i
                            I=                       cotb πt · R(t) dt,                        (2.8)
                                    2       M −i∞

where M ∈ R is an arbitrary constant in the interval n < M < (2r + 1)n.
Proof. Consider the integrand in (2.8) on the contour of the rectangle with vertices
M ± iN , N + 1/2 ± iN (see Fig. 1), where the integer N is suﬃciently large,
N > (2r + 1)n. Since the function R(t) is analytic inside this rectangle and on its
boundary, Cauchy’s theorem and Lemma 2.3 imply that the integral
           M −iN        N+1/2−iN          N+1/2+iN         M +iN     
  πb
                     +              +                  +                  cotb πt · R(t) dt    (2.9)
  2πi       M +iN        M −iN             N+1/2−iN        N+1/2+iN

is equal to the sum of the residues of the integrand at t ∈ Z, M < t ⩽ N . Using (2.5)
and the expansion

                                                    R(b−1)(k)                          
       R(t) = R(k) + R (k) · (t − k) + · · · +               · (t − k)b−1 + O (t − k)b
                                                     (b − 1)!

in the neighbourhood of t = k ∈ Z, M < k ⩽ N , we obtain that the integral (2.9)
is equal to

                                                  R(b−1)(k)   
                                                                  N
                                                                    R(b−1)(k)
               Res π b cotb πt · R(t) =                         =             .               (2.10)
               t=k                                     (b − 1)!      (b − 1)!
      M <k⩽N                                M <k⩽N                  k=n+1

                         Figure 1. The neighbourhood of the point x∗
                         Irrationality of values of the zeta function                       499

Let us note that on the sides [N + 1/2 − iN, N + 1/2 + iN ], [M − iN, N + 1/2 − iN ]
and [N + 1/2 + iN, M + iN ] of the rectangle we have R(t) = O(N −2 ) by (1.3), and
the function cotb πt is bounded. The latter assertion follows from assertion (a) of
Lemma 2.2 and the boundedness of cot πt on the sides under consideration: for the
segment [N + 1/2 − iN, N + 1/2 + iN ] we use Lemma 2.1, while for the other two
segments we use the trivial estimate
                                                  
                             1 + e±2πix · e−2π|y|  1 + e−2π|y|
                            
         | cot π(x + iy)| =                       ⩽            ,  x ∈ R,
                              1 − e±2πix · e−2π|y|  1 − e−2π|y|
for y = ±N . Therefore,
       N+1/2−iN        N+1/2+iN            M +iN     
                   +             +                        cotb πt · R(t) dt = O(N −1 ).
         M −iN           N+1/2−iN          N+1/2+iN

Passing to the limit in (2.9) as N → ∞, we obtain the right-hand side of (2.8). Pass-
ing to the limit in (2.10), we obtain the desired sum (1.2), which completes the proof
of the lemma.
Lemma 2.5. The following relation holds for (1.2) as n → ∞:
                              √
                     (−1)bn (2 πn )a−2rb (2π)b            
              I =I ˜
                                 a−1
                                                1 + O(n−1 ) ,
                               n
where
                                  µ+i∞
                           1
            I˜ = I˜n := −                sinb πnτ · cotb πnτ · enf(τ) · g(τ ) dτ,         (2.11)
                          2πi   µ−i∞

 f(τ ) = b(τ + 2r + 1) log(τ + 2r + 1) + b(−τ + 2r + 1) log(−τ + 2r + 1)
         + (a + b)(τ − 1) log(τ − 1) − (a + b)(τ + 1) log(τ + 1) + (a − 2rb)2 log 2,
                                                                               (2.12)
                              (τ + 2r + 1)b/2 (−τ + 2r + 1)b/2
                     g(τ ) =                                   ,               (2.13)
                                (τ + 1)(a+b)/2 (τ − 1)(a+b)/2
and µ ∈ R is an arbitrary constant in the interval 1 < µ < 2r + 1.
Remark 2.1. To deﬁne the functions f(τ ) and g(τ ) unambiguously, we consider
them in the τ -plane with cuts along the rays (−∞, 1] and [2r + 1, +∞), ﬁxing the
branches of logarithms that take real values on the interval (1, 2r + 1) of the real
axis. This choice of branches is motivated by the following proof.
Proof. Using the formula Γ(z + 1) = zΓ(z), we express the rational function (1.1)
in terms of the gamma function:
                                        b                a
                   Γ(±t + (2r + 1)n + 1)       Γ(t)Γ(1 − t)
   R(t) = (−1)an                                               (2n)!a−2rb , (2.14)
                      Γ(±t + n + 1)           Γ(±t + n + 1)
where, as before, ± stands for two factors in the product. We transform the inte-
grand in (2.8) using formula (2.14) for R(t) and the identity
                                    π
                 Γ(t)Γ(1 − t) =          = (−1)n Γ(−t + n + 1)Γ(t − n).
                                  sin πt
500                                        W. Zudilin

We have

               (−1)bn · sinb πt Γ(±t + (2r + 1)n + 1)b Γ(t − n)a+b
      R(t) =                                                       (2n)!a−2rb .            (2.15)
                     πb                  Γ(t + n + 1)a+b

Substituting this expression into (2.8), we obtain the formula
                   M +i∞
       (−1)bn i
I=                         sinb πt · cotb πt
         2π       M −i∞
             Γ(±t + (2r + 1)n + 1)b Γ(t − n)a+b (2n)!a−2rb
         ×                                                 dt
                           Γ(t + n + 1)a+b
                              M +i∞
       (−1)bn (2n)a−2rb i                                   (−t + (2r + 1)n)b (t + (2r + 1)n)b
  =                                   sinb πt · cotb πt ·
              2π             M −i∞                                     (t + n)a+b
             Γ(±t + (2r + 1)n) Γ(t − n)a+b Γ(2n)a−2rb
                                b
         ×                                            dt,                                  (2.16)
                           Γ(t + n)a+b

where M ∈ R is an arbitrary constant in the interval n < M < (2r + 1)n. We put
M = µn for µ ∈ R in the interval 1 < µ < 2r + 1.
  The asymptotics of the gamma function
                                
                               1                  √            
              log Γ(z) = z −       log z − z + log 2π + O |z|−1          (2.17)
                               2

(see, for example, [23], § 3.10) implies that the following formulae hold on the
contour of integration in (2.16):
                                                 
                                                1
  log Γ(±t + (2r + 1)n) = ±t + (2r + 1)n −          log(±t + (2r + 1)n)
                                                2
                                                        √
                             − (±t + (2r + 1)n) + log 2π + O(n−1 ),
                                      
                                     1                             √
            log Γ(t + n) = t + n −       log(t + n) − (t + n) + log 2π + O(n−1 ),
                                     2
                                      
                                     1                             √
            log Γ(t − n) = t − n −       log(t − n) − (t − n) + log 2π + O(n−1 ),
                                     2
                                   
                                  1                       √
               log Γ(2n) = 2n −       log(2n) − 2n + log 2π + O(n−1 ).
                                  2

The change t = nτ in the integrals in (2.16) yields
                     √                              µ+i∞
            (−1)bn (2 πn )a−2rb (2π)b−1 i
         I=                                                 sinb πnτ · cotb πnτ · enf(τ)
                       na−1                        µ−i∞

                    (τ + 2r + 1)b/2 (−τ + 2r + 1)b/2            
                  ×                                   1 + O(n−1 ) dτ,
                      (τ + 1)(a+b)/2 (τ − 1)(a+b)/2

where f(τ ) is the function deﬁned in (2.12) and µ = M/n ∈ R is an arbitrary
constant in the interval 1 < µ < 2r + 1. This completes the proof of the lemma.
                             Irrationality of values of the zeta function                                 501

   By assertion (b) of Lemma 2.2 the integral in (2.11) can be written as

                 1    
                      b            µ+i∞
         I˜ = −              ck           en(f(τ)−kπiτ) g(τ ) dτ,          ck = c−k ,               (2.18)
                2πi               µ−i∞
                      k=−b

where the sum is taken over those k that have even parity with b, and c−b = cb = 0
if b > 1.
Lemma 2.6. For µ, λ ∈ R, 1 < µ < 2r + 1, and n a positive integer we put
                                            µ+i∞
                                    1
                        Jn,λ =                     en(f(τ)−λπiτ) g(τ ) dτ.                          (2.19)
                                   2πi    µ−i∞

Then
                                            Jn,−λ = Jn,λ,
where the bar stands for complex conjugation.
Proof. Applying Schwarz’ reﬂection principle to the functions f(τ ), g(τ ) analytic
in C \ ((−∞, 1] ∪ [2r + 1, +∞)) and taking real values on the interval (1, 2r + 1)
(see, for example, [24], Ch. III, § 7, Proposition 7.1) and making the change τ → τ̄
in the integral in (2.19), we obtain that
                   µ+i∞                                             µ+i∞
              1                                              1
   Jn,λ =                 en(f(τ̄ )−λπiτ̄) g(τ̄ ) dτ̄ = −                   en(f(τ̄ )−λπiτ̄ ) g(τ̄ ) dτ
             2πi   µ−i∞                                     2πi    µ−i∞
                    µ+i∞
              1
         =                   en( f(τ)+λπiτ ) g(τ ) dτ = Jn,−λ,
             2πi   µ−i∞

as was to be shown.
Corollary 2.1. The integral in (2.11) can be written as
                                               
                                               b
                                  I˜ = −2                 ck Re Jn,k ,                              (2.20)
                                               k=0
                                            k≡b (mod 2)

where ck are some (rational ) constants, c1 = 1 for b = 1 and cb = 0, cb−2 = 0
for b > 1.
Proof. The desired representation (2.20) follows immediately from assertion (b) of
Lemma 2.2, formula (2.18), and Lemma 2.6.
   Now let us calculate the asymptotics of the integrals on the right-hand side
of (2.18) using the saddle-point method. We have to determine the saddle points of
the integrands, that is, the zeros of the derivatives of the functions f(τ ) − kπiτ ,
k = 0, ±1, . . . , ±b, k ≡ b (mod 2). It is easy to verify that the roots of the derivative

        d
           (f(τ ) − kπiτ ) = b log(τ + 2r + 1) − b log(−τ + 2r + 1)
        dτ
                                + (a + b) log(τ − 1) − (a + b) log(τ + 1) − kπi,
                             k = 0, ±1, . . . , ±b,    k ≡ b (mod 2),
502                                    W. Zudilin

are simultaneously the roots of the polynomial

                 (τ + 2r + 1)b (τ − 1)a+b − (τ − 2r − 1)b (τ + 1)a+b ,         (2.21)

whose quantity is equal to the degree a + 2b − 1 of this polynomial.
Lemma 2.7. Let a, b, r be positive integers, let a + b be even, a ⩾ 3rb, and let f(τ )
be the function deﬁned by (2.12), where the corresponding branches of the logarithms
in the cut plane C\((−∞, 1]∪[2r+1, +∞)) take real values on the interval (1, 2r+1).
Then the equation
                            f  (τ ) − λπi = 0,   λ ∈ R,                       (2.22)
has
   (a) a pair of real solutions −µ0 ± i0 with µ0 symmetric with respect to the imag-
inary axis for λ = 0, where µ0 ∈ (1, 2r + 1), and + ( −) in ±i0 corresponds to the
upper (lower) bank of the cut (−∞, 1],
   (b) a pair of real solutions −µ1 ± i0 and µ1 ± i0 symmetric with respect to
the imaginary axis for λ = ±b, where µ1 ∈ (2r + 1, +∞), and + ( −) in ±i0
coincides with the sign of λ and corresponds to the upper (lower) banks of the cuts
(−∞, 1], [2r + 1, +∞),
   (c) a real solution ±i0 for λ = ±(a + b), where + ( −) in ±i0 coincides with the
sign of λ and corresponds to the upper (lower) bank of the cut (−∞, 1],
   (d) a solution on the imaginary axis for the real λ such that b < |λ| < a + b,
   (e) a pair of complex solutions symmetric with respect to the imaginary axis for
the real λ such that 0 < |λ| < b.
   All solutions of equation (2.22) corresponding to positive λ are contained in the
half-plane Im τ > 0. All solutions corresponding to negative λ are contained in
the half-plane Im τ < 0. All solutions of equation (2.22) appear in the list (a)–(e).
Proof. Since

                 f  (τ ) = b log(τ + 2r + 1) − b log(−τ + 2r + 1)
                             + (a + b) log(τ − 1) − (a + b) log(τ + 1)         (2.23)

and log z = log |z| + i arg z, −π < arg z < π, for the main branch of the logarithm
with the cut (−∞, 0] in the z-plane, we have

                                   |τ + 2r + 1|b |τ − 1|a+b
               Re f  (τ ) = log                             ,                 (2.24)
                                 | − τ + 2r + 1|b |τ + 1|a+b
               Im f  (τ ) = b arg(τ + 2r + 1) − b arg(−τ + 2r + 1)
                              + (a + b) arg(τ − 1) − (a + b) arg(τ + 1),       (2.25)

and the arguments arg( · ) take the value zero on (1, 2r + 1). Formula (2.25) has
the following geometrical interpretation in the notation of Fig. 2:

      Im f  (τ ) = b(β− + β+ ) + (a + b)(α+ − α− ) = b(π − β) + (a + b)α,     (2.26)
                             Irrationality of values of the zeta function               503

whence Im f  (τ ) > 0 if Im τ > 0 and Im f  (τ ) < 0 if Im τ < 0. By (2.24) and (2.26),
the set of solutions of equation (2.22) for every λ is symmetric with respect
to the imaginary axis, and the symmetry τ → τ̄ maps it onto the set of solu-
tions of equation (2.22) with −λ instead of λ. In what follows we deal with λ > 0
and the upper half-plane. The results thus obtained can b transferred to the case
when λ < 0 by the symmetry with respect to the real axis.

                                              Figure 2

  By (2.23), any solution of equation (2.22) is a root of the polynomial

                (τ + 2r + 1)b (τ − 1)a+b − eλπi (−τ + 2r + 1)b (τ + 1)a+b ,           (2.27)

whose degree is equal to a + 2b − 1 if λ is an integer that has even parity with b
(otherwise, its degree is equal to a + 2b). If λ ≡ b (mod 2), then this polynomial
coincides with (2.21).
   (a), (c). If λ = 0 (or, which is the same, λ = a + b), then the polynomial (2.27)
is an odd function. Therefore, 0 is one of its roots. The corresponding solution
+i0 of equation (2.22) corresponds to λ = a + b, since α = β = π in (2.26)
for τ = 0. Calculating the values of the polynomial at 1, 2r + 1 and using the
fact that this polynomial is odd, we obtain that it has a pair of real roots ±µ0 ,
where µ0 ∈ (1, 2r + 1). We shall show later that µ0 is the unique real root in
(1, 2r + 1), but until then we assume that µ0 is the real root nearest to 2r + 1 of
the polynomial (2.27) with λ = 0 in the above interval. By (2.26), the solutions
−µ0 + i0 and µ0 correspond to λ = 0 in equation (2.22).
   (b) Calculating the values of (2.27) with λ = b at 2r + 1, +∞, we likewise obtain
that this polynomial has a pair of real roots ±µ1 . We assume for the moment that
among the roots in the interval (2r + 1, +∞) the root µ1 ∈ (2r + 1, +∞) is the
nearest to 2r + 1. By (2.26), the solutions −µ1 + i0 and µ1 + i0 correspond to λ = b
in equation (2.22).
   In the case when a ⩾ 3rb there is a better localization of the root µ1 , namely,
µ1 ∈ (2r + 1, 4r + 1). Indeed, the value of the polynomial (2.27) at 4r + 1 is equal
to
                                                                    b       a+b 
                                                                    1        1
        b
(6r + 2) (4r)a+b
                   − (2r) (4r + 2)
                         b           a+b          b
                                           = (2r) (4r)   a+b
                                                                 3+     − 1+           < 0,
                                                                    r        2r
504                                           W. Zudilin

since
                                                         
                         1           3                    1
        (3r + 1) log 1 +      = 4 log > 2 log 2 = log 3 +         if r = 1,
                         2r          2                    r
                                                             
                         1      3r + 1  7                     1
        (3r + 1) log 1 +      >        ⩾ > 2 log 2 > log 3 +      if r ⩾ 2,
                         2r     2r + 1  5                     r

where we have used the elementary inequality
                                                    
                                      1            1    1
                                         < log 1 +     < ,                                (2.28)
                                     n+1           n    n

which holds for all positive integers n, whence
                                                                    
                             1                        1                1
             (a + b) log 1 +      ⩾ (3r + 1)b log 1 +      > b log 3 +     .
                             2r                       2r               r

   (d) By (2.24), we have Re f  (τ ) = 0 on the imaginary axis. As τ ranges over
the ray iy, y > 0, the angles α, β decrease continuously from π to 0. Therefore, the
function Im f  (τ ) = b(π − β) + (a + b)α takes all intermediate values in the interval
(bπ, (a + b)π). In particular, for every real λ, b < λ < a + b, we obtain at least one
solution of equation (2.22) that lies on the imaginary axis.
   (e) We shall now localize the complex solutions of (2.22) corresponding to the
real λ, 0 < |λ| < b.
   Consider the semicircle of radius 2ρ with centre 2r +1, where ρ < r, in the upper
half-plane. For τ = x + iy on this semicircle we have

               | − τ + 2r + 1|2 = 4ρ2 ,          |τ + 2r + 1|2 = 4ρ2 + 4(2r + 1)x,
      |τ − 1|2 = 4ρ2 + 4rx − 4r(r + 1),            |τ + 1|2 = 4ρ2 + 4(r + 1)x − 4r(r + 1).
                                                                                      (2.29)
By (2.24),

                                      (ρ2 + (2r + 1)x)b (ρ2 + rx − r(r + 1))a+b
                2 Re f  (τ ) = log                                             .         (2.30)
                                          ρ2b (ρ2 + (r + 1)x − r(r + 1))a+b

  We denote the function in (2.30) by f˜(x), 2r + 1 − 2ρ < x < 2r + 1 + 2ρ. It is a
monotonically increasing function of x, since

                      b(2r + 1)                (a + b)r                 (a + b)(r + 1)
        f˜ (x) =                     +                        −
                    ρ2 + (2r + 1)x        ρ2 + rx − r(r + 1)       ρ2 + (r + 1)x − r(r + 1)
                   b(2r + 1)                    (a + b)(r(r + 1) − ρ2 )
              =                 +
                ρ2 + (2r + 1)x (ρ2 + rx − r(r + 1))(ρ2 + (r + 1)x − r(r + 1))
                  4b(2r + 1)     16(a + b)(r(r + 1) − ρ2 )
              =                +                           > 0.
                |τ + 2r + 1| 2       |τ − 1|2 |τ + 1|2
                         Irrationality of values of the zeta function                    505

Therefore,

 f˜(2r + 1 − 2ρ) < f˜(x) < f˜(2r + 1 + 2ρ),            x ∈ (2r + 1 − 2ρ, 2r + 1 + 2ρ), (2.31)

and
              Re f  (2r + 1 − 2ρ) < Re f  (τ ) < Re f  (2r + 1 + 2ρ + i0)          (2.32)

on the semicircle under consideration. Consider ρ = (µ1 − 2r − 1)/2, where
µ1 ∈ (2r + 1, +∞) is the real root of the polynomial (2.27) with λ = b.
As mentioned above, 2r + 1 < µ1 < 4r + 1 if a ⩾ 3rb, that is, the assumption
ρ < r holds. By (2.32), we have

                             Re f  (τ ) < Re f  (µ1 + i0) = 0                       (2.33)

for the points of the semicircle. Besides,

                                   lim Re f  (τ ) = +∞.                              (2.34)
                                τ→2r+1

   Consider the rays starting from the point 2r + 1 and contained in the upper half-
plane. By (2.33) and (2.34), each of these contains a point τ belonging to the domain
bounded by the above semicircle and the real axis and such that Re f  (τ ) = 0.
Hence, this domain contains a part of the continuously diﬀerentiable curve

                                          |τ + 2r + 1|b |τ − 1|a+b
                    Re f  (τ ) = log                               = 0.              (2.35)
                                        | − τ + 2r + 1|b |τ + 1|a+b

(See Fig. 3, where this part of the curve is situated, according to (2.31), between
the two semicircles corresponding to ρ = (µ1 − 2r − 1)/2 and ρ = (2r + 1 − µ0 )/2.)
By (2.26), the values of Im f  (τ ) on this curve as it approaches the real axis are equal
to 0 (at µ0 ) and bπ (at µ1 ). Therefore, Im f  (τ ) takes on the curve all intermediate
values between 0 and bπ, that is, the values λπ, where 0 < λ < b. So we have
produced solutions of equation (2.22) for these λ. Every point obtained from these
by reﬂection in the imaginary axis also is a solution.

                                            Figure 3
506                                   W. Zudilin

    We have produced all the solutions of equation (2.22) listed in (a)–(e). To
complete the proof, we have to show that there are no others. Assume the contrary,
that is, assume that for some λ0 ∈ R there is a solution of equation (2.22) that is not
listed in (a)–(e). As mentioned above, this solution is a root of the polynomial (2.27)
with λ = λ0 . We claim that the number of roots of (2.27) listed in (a)–(e) is equal
to its degree, which will contradict our assumption.
    If λ0 is not an integer, then we have a purely imaginary solutions (see (d))
corresponding to λ ≡ λ0 (mod 2), b < |λ| < a + b, and b pairs of complex solutions
(see (e)) corresponding to λ ≡ λ0 (mod 2), |λ| < b. Therefore, the total number of
roots of (2.27) with λ = λ0 listed in (d) and (e) is equal to the degree a + 2b of the
polynomial.
    If λ0 is an integer (even or odd), then a solution of equation (2.22) with λ = λ0
is a root of the polynomial

             (τ + 2r + 1)2b (τ − 1)2(a+b) − (τ − 2r − 1)2b (τ + 1)2(a+b).       (2.36)

For this polynomial we have found two real roots ±µ0 in (a), two real roots ±µ1
in (b), one real root 0 in (c), 2(a − 1) purely imaginary roots in (d) and 4(b − 1)
complex roots in (e). The total number of roots of the polynomial (2.36) listed
in (a)–(e) is equal to its degree 2a + 4b − 1.
   Hence, any solution of equation (2.22) is contained in the list (a)–(e). This
contradiction completes the proof of the lemma.

Remark 2.2. We replaced the original assumption a ⩾ 2rb by the stronger assump-
tion a ⩾ 3rb in Lemma 2.7 only in order to localize the root µ1 . Therefore,
Lemma 2.7 remains valid in the case when a ⩾ 2rb if

                                     µ1 < 4r + 1.                               (2.37)

Corollary 2.2. The set of τ ∈ C for which (2.35) holds is the union of the imagi-
nary axis and a pair of closed curves symmetric with respect to the imaginary axis
(see Fig. 4). These curves divide the complex plane into four parts, in each of which
the sign of Re f  (τ ) is constant.

                                       Figure 4
                         Irrationality of values of the zeta function                507

Corollary 2.3. Any semicircle of radius ρ, 2r + 1 − µ0 < 2ρ < µ1 − 2r − 1, with
centre 2r + 1 lying in the upper half-plane, intersects the curve (2.35) (see Fig. 3)
at precisely one point.

Proof. This assertion follows from inequalities (2.32), since the function Re f  (τ ) is
monotonic on any of these semicircles.

Lemma 2.8. Let a, b, r, n be positive integers, a ⩾ 2rb, let f(τ ), g(τ ) be as deﬁned
in (2.12), (2.13), and let µ, λ ∈ R, 1 < µ < 2r + 1, |λ| ⩽ b. Then the contour of
integration Re τ = µ in the integral

                                µ+i∞
                                       en(f(τ)−λπiτ) g(τ ) dτ                     (2.38)
                               µ−i∞

can be replaced by any other contour L joining inﬁnitely remote points in the
domains Re τ ⩾ µ, Im τ < 0 and Re τ ⩾ µ, Im τ > 0 and intersecting the real
axis at precisely one point τ = µ. In particular, L can go along the upper and (or)
lower bank of the cut [2r + 1, +∞).

Proof. For any real N > µ we join the points of the original contour Re τ = µ and
those of the new contour L by two arcs of radius N with centre at the origin. We
denote the corresponding points of intersection with the contours by M± and L±
(see Fig. 5).

                                          Figure 5
508                                           W. Zudilin

   There are no singular points of the integrand in (2.38) inside the curvilinear
triangles µL+ M+ and µM− L− . The lemma will be proved if we can show that

                en(f(τ)−λπiτ) g(τ ) dτ → 0,                  en(f(τ)−λπiτ) g(τ ) dτ → 0   (2.39)
       L+ M +                                       M − L−

as N → ∞, where L+ M+ and M− L− are arcs of the circle of radius N with centre
at the origin.
   On the arcs L+ M+ and M− L− of the circle τ = N eit we have the inequalities
0 ⩽ t < π/2 and −π/2 < t ⩽ 0, respectively (the value t = 0 is taken on the upper
and lower bank of the cut [2r + 1, +∞)). Using Taylor’s formula, we obtain the
relations
                                                                      
                                                                  e−it
            log(τ + 1) = log(N eit + 1) = log(N eit ) + log 1 +
                                                                   N
                                        −it
                                                     
                                       e           1
                       = log N + it +       +O           ,                        (2.40)
                                        N         N2
                                                     
                                       e−it        1
            log(τ − 1) = log N + it −       +O           ,                        (2.41)
                                        N         N2
                                                                                   
                                it                      it             (2r + 1)e−it
       log(τ + 2r + 1) = log(N e + 2r + 1) = log(N e ) + log 1 +
                                                                            N
                                                −it
                                                               
                                       (2r + 1)e              1
                       = log N + it +                +O          ,                (2.42)
                                            N                N2
      log(−τ + 2r + 1) = ∓πi + log(N eit − (2r + 1))
                                                                        
                                                    (2r + 1)e−it      1
                          = ∓πi + log N + it −                   +O        ,              (2.43)
                                                         N            N2

where − (+) in ∓πi in (2.43) corresponds to the arc L+ M+ ( M− L− ) according
to the choice of branches of the logarithm. The constant in O(1/N 2 ) in formu-
lae (2.40)–(2.43) is absolute, since |e−it | = 1 for real t. Substituting these expan-
sions into (2.12), we obtain the formula

f(τ ) = f(N eit )
                                                                                
  = (log N + it) b(τ + 2r + 1) + b(−τ + 2r + 1) + (a + b)(τ − 1) − (a + b)(τ + 1)
         e−it 
       +        b(2r + 1)(τ + 2r + 1) − b(2r + 1)(−τ + 2r + 1)
          N                                 
         − (a + b)(τ − 1) − (a + b)(τ + 1)
                                                          
                                                      |τ |
       ∓ πi · b(−τ + 2r + 1) + (a − 2rb)2 log 2 + O
                                                      N2
                                                           
                       Ne                                    1
  = −2(a − 2rb) log        + it ± bπi(N e − 2r − 1) + O
                                           it
                                                                ,
                        2                                    N
                             Irrationality of values of the zeta function                             509

where the sign of ±bπ coincides with the sign of t (and sin t). Therefore,
                                                                     
                                        Ne                           1    1
    Re(f(τ ) − λπiτ ) = −2(a − 2rb) log    − (b ∓ λ)πN | sin t| + O     ⩽
                                        2                            N    n

on the arcs L+ M+ and M− L− as N → ∞. (We have used the inequalities a ⩾ 2rb
and |λ| ⩽ b.) Hence, the estimate

                             |en(f(τ)−λπiτ) | = en Re(f(τ)−λπiτ) ⩽ e                              (2.44)

holds for all suﬃciently large N . The following trivial estimate holds for the func-
tion (2.13) on the arcs L+ M+ and M− L− :
                                                                    
                  N b/2 N b/2                   1              1
  |g(τ )| = O                               =O              =O                  as N → ∞,         (2.45)
              N (a+b)/2 N (a+b)/2              Na              N2

since a ⩾ 2rb ⩾ 2. Since the length of each of the arcs L+ M+ and M− L− does not
exceed πN/2, estimates (2.44) and (2.45) imply that every integral in (2.39) is of
order O(1/N ). Hence, the limiting relations (2.39) hold, which completes the proof
of the lemma.
Lemma 2.9. Let a, b, r be positive integers, a ⩾ 2rb, let f(τ ), g(τ ) be the functions
deﬁned in (2.12) and (2.13), and let λ ∈ R, |λ| ⩽ b. Assume, moreover, that (2.37)
and the assumption
                               µ0 + µ20 − 1 ⩾ µ1                                 (2.46)

hold for the real roots µ0 ∈ (1, 2r + 1) and µ1 ∈ (2r + 1, +∞) of (2.36).
   Then the asymptotic behaviour of the integral (2.38) with µ = µ0 as n → ∞
is determined by the single saddle point τ0 (the solution of equation (2.22)) in the
domain Im τ > 0. More precisely, the following asymptotic formula holds:

                   µ0 +i∞
            1
  Jn,λ =                    en(f(τ)−λπiτ) g(τ ) dτ
           2πi    µ0 −i∞
                                                                        
                 −1/2
                   |f  (τ0 )|−1/2 en Re f0 (τ0 ) |g(τ0 )| · e− 2 arg f (τ0 )+i arg g(τ0 )+in Im f0 (τ0 )
                                                                i
        = (2π)
                                     
             × n−1/2 1 + O(n−1 )              as n → ∞,                                            (2.47)

where

        f0 (τ ) = f(τ ) − f  (τ )τ
                 = b(2r + 1) log(τ + 2r + 1) + b(2r + 1) log(−τ + 2r + 1)
                     − (a + b) log(τ + 1) − (a + b) log(τ − 1) + (a − 2rb)2 log 2. (2.48)

Proof. We shall prove the lemma only for λ ⩾ 0. The case when λ < 0 can be
reduced to this case by reﬂection in the real axis.
510                                     W. Zudilin

   According to Lemma 2.8, we replace the contour of integration in (2.38) with
µ = µ0 by a contour consisting of rectilinear rays and segments. Let us note at once
that the derivative of Re f(τ ) on every such rectilinear part τ = τ1 + eiϕ t, t ∈ R, is
given by the formula
                                             
    d                df(τ )        dτ df(τ )
       Re f(τ ) = Re        = Re      ·         = Re f  (τ ) cos ϕ − Im f  (τ ) sin ϕ.
   dt                 dt           dt     dτ
                                                                                     (2.49)
   If λ = 0, then µ0 is the unique maximum point of the function Re f(τ ) on the
line τ = µ0 + it, −∞ < t < +∞, since

                                d
                                   Re f(τ ) = − Im f  (τ )
                                dt
and Im f  (τ ) takes negative values in the domain Im τ < 0 and positive ones in
the domain Im τ > 0. So, in the case when λ = 0, we use the original contour
Re τ = µ0 .
   If λ = b, then we replace the ray going from µ0 to µ0 + i∞ in the contour of
integration in (2.38) with µ = µ0 by a ray going from µ0 to +∞ along the upper
bank of the cut [2r + 1, +∞). The function

                                    Re(f(τ ) − λπiτ )                               (2.50)

increases on the set τ = µ0 + it, −∞ < t ⩽ 0, since

                  d
                     Re(f(τ ) − λπiτ ) = − Im f  (τ ) + λπ ⩾ λπ > 0.               (2.51)
                  dt
On the set τ = t, µ0 ⩽ t < +∞, the function Re(f(τ ) − λπiτ ) = Re f(τ ) has a
unique maximum point at t = µ1 (by Lemma 2.7 and Corollary 2.2).

                                         Figure 6

   It remains to consider the case when λ ∈ (0, b). We replace the ray going
from µ0 to µ0 + i∞ by the segment τ = µ0 + eiϕ t, 0 ⩽ t ⩽ µ20 − 1, passing
through the saddle point τ0 (the unique solution of equation (2.22) in the domain
                            Irrationality of values of the zeta function               511

Re τ > 0) and the ray τ = eiϕ µ20 − 1 + t, µ0 ⩽ t < +∞. By Corollary 2.3, the ray
τ = µ0 +eiϕ t, t > 0, intersects the curve Re f  (τ ) = 0 at a single point (namely, τ0 ),
and 0 < ϕ < π/2. By (2.46), τ0 is an interior point of the above segment (see
Fig. 6). On the ray τ = µ0 + it, t ⩽ 0, the function (2.50) increases by (2.51). On
the ray τ = eiϕ µ20 − 1 + t, t ⩾ µ0 , it decreases, since

                d
                   Re(f(τ ) − λπiτ ) = Re(f  (τ ) − λπi) = Re f  (τ ) < 0
                dt

by Corollary 2.2. Hence, it is suﬃcient to show that τ0 is the unique maximum
point of the function (2.50) on the segment τ = µ0 + eiϕ t, 0 ⩽ t ⩽ t1 , where
t1 = µ20 − 1. Assume that t0 corresponds to the point τ0 = µ0 + eiϕ t0 on the
segment under consideration. By Corollary 2.3,

  Re f  (µ0 + eiϕ t) < 0    for 0 < t < t0 ,Re f  (µ0 + eiϕ t) > 0 for t0 < t ⩽ t1 .
                                                                                 (2.52)
   We claim that the function Im f  (τ ) increases monotonically on the segment
under consideration. Let us use the geometric interpretation (2.26) of the function
Im f  (τ ) once again. As t ⩾ 0 increases on the ray τ = µ0 + eiϕ t, the angle β
decreases monotonically from π to 0, whereas the angle α ﬁrst increases from 0 to
some α0 and then decreases from α0 to 0. We claim that the maximal value α0 is
attained on the ray at t = t1 , which will imply that the function

                               Im f  (τ ) = b(π − β) + (a + b)α

is monotonically increasing on the segment τ = µ0 + eiϕ t, 0 ⩽ t ⩽ t1 .

                                             Figure 7

   The points τ = x + iy of the upper half-plane at which the real segment [−1, 1]
subtends less than a given angle α belong to an arc of the circle of radius 1/ sin α
with centre i cot α (this assertion for an acute angle α is depicted in Fig. 7):

                                    x2 + y2 − 2y cot α = 1,
512                                         W. Zudilin

whence
                                                  x2 + y 2 − 1
                                     α = cot−1                 .
                                                      2y
On the given ray, x = µ0 + t cos ϕ and y = t sin ϕ if t ⩾ 0, whence

               dα    (2x cos ϕ + 2y sin ϕ) · 2y − 2 sin ϕ · (x2 + y2 − 1)
                  =−
               dt                 (x2 + y2 − 1)2 + (2y)2
                                 t − (µ2 − 1)
                                  2
                  = −2 sin ϕ · 2                    .
                              (x + y2 − 1)2 + 4y2

Therefore, the maximal value of α is attained at t = µ20 − 1.
   Since Im f  (τ ) is monotonically increasing on the segment τ = µ0 + eiϕ t, 0 ⩽
t ⩽ t1 , we have

Im f  (µ0 + eiϕ t) < λπ       for 0 ⩽ t < t0 ,      Im f  (µ0 + eiϕ t) > λπ
                                                                   for t0 < t ⩽ t1 .
                                                                             (2.53)
   Combining (2.52), (2.53) and (2.49), we obtain that the function

             d
                Re(f(τ ) − λπiτ ) = Re f  (τ ) cos ϕ − (Im f  (τ ) − λπ) sin ϕ
             dt
on the segment τ = µ0 + eiϕ t, 0 ⩽ t ⩽ t1 , changes sign from plus to minus only
when τ passes through τ0 = µ0 + eiϕ t0 . Hence, τ0 is indeed the unique maximum
point on the segment and on the whole contour of integration consisting of this
segment and two rays.
   To prove the asymptotic formula (2.47), we write down the contribution of the
saddle point τ0 :
                                                                                      
  (2π)1/2 e 2 − 2 arg f (τ0 ) |f  (τ0 )|−1/2 en(f(τ0 )−λπiτ0 ) g(τ0 ) n−1/2 1 + O(n−1 ) (2.54)
           πi   i

(see, for example, [23], § 5.7, formula (5.7.2)). We have

                               b                b         a+b    a+b
                 f  (τ ) =           +               +       −
                          τ + 2r + 1 −τ + 2r + 1 τ − 1 τ + 1
                            (a − 2rb)τ 2 − (2r + 1)(a − 2rb + 2ra)
                         =2                                        = 0
                                   (τ 2 − 1)(τ 2 − (2r + 1)2 )

at those τ for which Re f  (τ ) = 0 (in particular, τ0 ). Using the equality

                        f(τ0 ) − λπiτ0 = f(τ0 ) − f  (τ0 )τ0 = f0 (τ0 )

and separating the modulus and argument in (2.54), we obtain (2.47), which com-
pletes the proof of the lemma.
Corollary 2.4. Let the assumptions of Lemma 2.9 hold. Assume, moreover, that
   1                              π
  − arg f  (τ0 ) + arg g(τ0 ) ≡ (mod πZ)            or   Im f0 (τ0 ) ≡ 0 (mod πZ).   (2.55)
   2                              2
                         Irrationality of values of the zeta function                     513

Then the following limiting relation holds for the integral
                                                 µ0 +i∞
                 1                  1
        Re Jn,λ = (Jn,λ + Jn,−λ) =                        enf(τ) cos(λπnτ )g(τ ) dτ :
                 2                 2πi          µ0 −i∞

           log | Re Jn,λ|
     lim                  = Re f0 (τ0 )
    n→∞           n
                                22(a−2rb)|τ0 + 2r + 1|b(2r+1)| − τ0 + 2r + 1|b(2r+1)
                          = log                                                      .
                                               |τ0 + 1|a+b |τ0 − 1|a+b
                                                                                   (2.56)
Moreover, in the case when
   1
  − arg f  (τ0 ) + arg g(τ0 ) ≡ 0 (mod πZ)      and     Im f0 (τ0 ) ≡ 0 (mod πZ), (2.57)
   2
the integral Jn,λ has the real asymptotics (2.47), which implies that the upper limit
in (2.56) becomes a limit.
Proof. Assumption (2.55) implies that the real part of the coeﬃcient of n−1/2 in
the asymptotic formula (2.47) is non-zero for an inﬁnite sequence of numbers n. It
is on this sequence that the limiting relation (2.56) is attained. If (2.57) holds, then
the principal term of the asymptotics (2.47) is a real number, and (2.56) with lim
instead of lim follows immediately from (2.47).
  We now state our deﬁnitive results concerning
                                    log |In |       log |I˜n |
                           κ = lim            = lim                                     (2.58)
                                n→∞    n       n→∞     n
(see Lemma 2.5). If b = 1 or b = 2, then the results take a simple form, and the
upper limits in (2.58) can be replaced by limits. Our assertions in these cases will
be stated as separate propositions.
Proposition 2.1. Let b = 1, let r be a positive integer, let a > 2r be an odd
integer, and let µ1 ∈ (2r + 1, +∞) be a real root of the polynomial (2.21). Then
               log |In |       22(a−2r)(µ1 + 2r + 1)2r+1 (µ1 − 2r − 1)2r+1
    κ = lim              = log                                             .            (2.59)
           n→∞    n                      (µ1 + 1)a+1 (µ1 − 1)a+1

Proof. In the case when b = 1, τ = µ1 is the unique maximum point of the function
Re f(τ ) on the contour of integration for calculating the asymptotics of the inte-
gral Jn,1 in the proof of Lemma 2.9 (the ray τ = µ0 + it, t ⩽ 0, and the ray τ = t,
t ⩾ µ0 , that goes along the upper bank of the cut [2r + 1, +∞)). This implies, in
particular, that f  (µ1 ) < 0, whence
                             1                π
                            − arg f  (µ1 ) ≡ (mod πZ).
                             2                2
In the case when b = 1 we have for the function (2.13) that
                             π
              arg g(µ1 ) = −      and      Im f0 (µ1 ) = −(2r + 1)π.
                             2
514                                    W. Zudilin

Using Corollary 2.4 with λ = 1 and τ0 = µ1 , we obtain that (2.57) holds and

                              log | Re Jn,1 |
                           lim                = Re f0 (µ1 ).
                          n→∞        n

The formula I˜n = − Re Jn,1 (see Corollary 2.1) and Lemma 2.5 imply that (2.59)
holds.

Proposition 2.2. Let b = 2, let r be a positive integer, assume that a ⩾ 4r is an
even integer, and let µ0 ∈ (1, 2r + 1) be a real root of the polynomial (2.21). Then

          log |In |       22(a−4r)(µ0 + 2r + 1)2(2r+1) (−µ0 + 2r + 1)2(2r+1)
 κ = lim            = log                                                    . (2.60)
      n→∞    n                         (µ0 + 1)a+2 (µ0 − 1)a+2

Proof. If b = 2, then I˜n = −Jn,0 , and τ = µ0 is the unique maximum on the
contour of integration τ = µ0 + it, t ∈ R, for calculating the asymptotics of
the integral Jn,0 in the proof of Lemma 2.9. Therefore, f  (µ0 ) > 0, whence

                            1
                           − arg f  (µ0 ) ≡ 0 (mod πZ).
                            2

It is obvious that
                         arg g(µ1 ) = 0,       Im f0 (µ1 ) = 0.

Corollary 2.4 with λ = 0 and τ0 = µ0 implies that (2.57) holds and

                              log |Jn,0|
                        lim              = Re f0 (µ0 ) = f0 (µ0 ).
                       n→∞        n

Combining this with Lemma 2.5, we obtain (2.60).

Lemma 2.10. Assume that the real root µ1 ∈ (2r+1, +∞) of the polynomial (2.21)
satisﬁes the inequality

                                           br(r + 1) r(r + 1)
                     µ1 ⩽ 2r + 1 + min              ,          .              (2.61)
                                            2(a + b) 3(2r + 1)

Then Re f0 (τ ) regarded as a function of Re τ increases in the domain Re τ > 0,
Im τ ⩾ 0 on curve (2.35).

Proof. As was shown in the proof of Lemma 2.7 (see also Corollary 2.3), on the
smooth curve (2.35) in the domain Re τ > 0, Im τ ⩾ 0 the quantity ρ = |τ −(2r +1)|/2,
τ = x + iy, can be represented as an implicit function of x, µ0 ⩽ x ⩽ µ1 , which is
continuously diﬀerentiable and increases. Using formulae (2.29), (2.30) and diﬀer-
entiating with respect to x, we obtain the following formula on the curve deﬁned
                           Irrationality of values of the zeta function                  515

by formula (2.35):

                                                                            
                    b          b        a+b                   a+b
 2ρρ                        −   +                 −
             ρ2 + (2r + 1)x ρ2 ρ2 + rx − r(r + 1) ρ2 + (r + 1)x − r(r + 1)
                                                                          
                   b(2r + 1)        (a + b)r           (a + b)(r + 1)
            +                  +                 −                           = 0.
                ρ2 + (2r + 1)x ρ2 + rx − r(r + 1) ρ2 + (r + 1)x − r(r + 1)

Simple transformations yield that

                                         
          b(2r + 1)         a+b                    b(2r + 1)ρ2     (a + b)(r(r + 1) − ρ2 )
  2ρρ x                  −                    =                   +                         .
        |τ ± (2r + 1)| 2   |τ ± 1|2               |τ ± (2r + 1)|2          |τ ± 1|2
                                                                                       (2.62)
   Therefore, the function Re f0 (τ ) can be regarded on the curve (2.35) as a function
of x, µ0 ⩽ x ⩽ µ1 . By (2.29), we have

                                            ρ2b(2r+1) (ρ2 + (2r + 1)x)b(2r+1)
  f˜0 (x) := 2 Re f0 (τ ) = log                                                         .
                                  (ρ2 + rx − r(r + 1))a+b (ρ2 + (r + 1)x − r(r + 1))a+b

Combining this with (2.29) and (2.62), we obtain that

                  
                    b(2r + 1)        b(2r + 1)
  f˜0 (x) = 2ρρ              + 2
                        ρ2        ρ + (2r + 1)x
                                                                     
                          a+b                        a+b
               − 2                      − 2
                  ρ + rx − r(r + 1) ρ + (r + 1)x − r(r + 1)
                                                                                    
                    b(2r + 1)2              (a + b)r               (a + b)(r + 1)
             +                     −                       −
                 ρ2 + (2r + 1)x ρ2 + rx − r(r + 1) ρ2 + (r + 1)x − r(r + 1)
                                                                    
                                            b(2r + 1)         a+b
           = 32ρρ (2ρ2 + (2r + 1)x)                      −
                                         |τ ± (2r + 1)|2 |τ ± 1|2
                                                                        
                               b(2r + 1)ρ2       (a + b)(r(r + 1) − ρ2 )
             + 16(2r + 1)                      +
                             |τ ± (2r + 1)|2             |τ ± 1|2
               64ρρ (a + b)r(r + 1) 32(a + b)r(r + 1)x
             +                          −
                       |τ ± 1|2                 |τ ± 1|2
                                                                                
             32(ρ2 + (2r + 1)x)        b(2r + 1)ρ2       (a + b)(r(r + 1) − ρ2 )
           =                                         +
                       x             |τ ± (2r + 1)|2            |τ ± 1|2
               32(a + b)r(r + 1)
             +                     (2ρρ − x).                                     (2.63)
                     |τ ± 1|2
516                                    W. Zudilin

   The function ρ = ρ(x) increases on the curve (2.35). Hence, ρ ⩾ 0. Continuing
the chain in (2.63), we obtain that

             32(ρ2 + (2r + 1)x) b(2r + 1)ρ2                    (a + b)(r(r + 1) − ρ2 )
  f˜0 (x) ⩾                                      + 32(2r + 1)
                     x            |τ ± (2r + 1)|2                     |τ ± 1|2
                 32(a + b)r(r + 1)x
               −
                       |τ ± 1|2
             2b(2r + 1) 2(a + b)((2r + 1)ρ2 + r(r + 1)x − r(r + 1)(2r + 1))
           =            −                                                        .
                 x            (ρ2 + rx − r(r + 1))(ρ2 + (r + 1)x − r(r + 1))
Put
                                      br(r + 1) r(r + 1)
                           ε = min             ,         .                        (2.64)
                                      2(a + b) 3(2r + 1)
We have ε ⩾ µ1 − 2r − 1. The localization of the curve (2.35) (see Corollary 2.3)
implies that
                                                           ε
                 2r + 1 − ε ⩽ x ⩽ 2r + 1 + ε,     0<ρ⩽ ,
                                                           2
whence
                 2b(2r + 1) 2(a + b)((2r + 1)ε/4 + r(r + 1))ε
      f˜0 (x) >             −
                 2r + 1 + ε        r(r + 1)(r − ε)(r + 1 − ε)
                                                                     
                                 b            (a + b)(2r + 1 + ε)ε
               > 2(2r + 1)              −
                             2r + 1 + ε 4r(r + 1)(r − ε)(r + 1 − ε)
                             4br(r + 1)(r − ε)(r + 1 − ε) − ε(a + b)(2r + 1 + ε)2
               = 2(2r + 1) ·                                                      .
                                   4r(r + 1)(r − ε)(r + 1 − ε)(2r + 1 + ε)
                                                                                   (2.65)

Combining the inequalities

                                   ε                              br(r + 1)
                        br(r + 1) ⩾ (a + b)                if ε ⩽           ,
                                   2                              2(a + b)
                                                                   r(r + 1)
             8(r − ε)(r + 1 − ε) > (2r + 1 + ε)2           if ε ⩽           ,
                                                                  3(2r + 1)

with (2.64) and (2.65), we obtain that f˜0 (x) > 0. Hence, Re f0 (τ ), regarded as a
function of x = Re τ , increases on the curve (2.35), as was to be shown.
Proposition 2.3. Let a, b, r be positive integers, assume that a + b is even, b ⩾ 3,
a ⩾ 2rb, and assume that (2.61) holds for the real root µ1 ∈ (2r + 1, +∞) of the
polynomial (2.21). Let

                       22(a−2rb)|τ0 + 2r + 1|b(2r+1)| − τ0 + 2r + 1|b(2r+1)
            κ := log                                                        ,
                                      |τ0 + 1|a+b |τ0 − 1|a+b
where τ0 is a complex root of the polynomial (2.21) in the domain Re τ > 0, Im τ > 0
with maximal real part Re τ0 . Assume, moreover, that (2.55) holds. Then
                                          log |In |
                                    lim             = κ.                          (2.66)
                                   n→∞       n
                          Irrationality of values of the zeta function                         517

Proof. The inequality (2.61) implies that µ1 − (2r + 1) < r/3. Hence, (2.37)
and (2.46) hold. By Lemma 2.10, the maximal value of the function Re f0 (τ )
on the roots of polynomial (2.21) is attained at τ = τ0 , for which λ = k = b − 2. By
Corollary 2.4, the asymptotics of the integral (2.20) is determined by the contribu-
tion of Re Jn,b−2, since the contributions of the other quantities are exponentially
smaller in comparison with Re Jn,b−2 , and the coeﬃcient cb−2 in (2.20) is non-zero
by assertion (b) of Lemma 2.2. Therefore,

                          log |I˜n |       log | Re Jn,b−2 |
                      lim            = lim                   = κ.
                      n→∞    n        n→∞         n

Using Lemma 2.5, we obtain the desired relation (2.66).

             § 3. Estimates for the coeﬃcients of linear forms
  Our ﬁrst result will be an upper estimate for the coeﬃcients of linear forms.

Proposition 3.1. Let a, b, r be positive integers, assume that a+b is even, a ⩾ 2rb,
and let the linear forms (1.5) be deﬁned by (1.2) and (1.1). Then the following
estimate holds for the coeﬃcients Ās , s = 0 or s = b + 1, . . . , a + b − 1:

                    log |Ās |
              lim              ⩽ 2b(2r + 1) log(2r + 1) + 2(a − 2rb) log 2,
             n→∞       n                                                                     (3.1)
                     s = 0 or s = b + 1, . . . , a + b − 1 and is odd.

  Moreover, estimate (3.1) is exact in the case when a is even:

                    log |Ās |
              lim              = 2b(2r + 1) log(2r + 1) + 2(a − 2rb) log 2,
             n→∞       n                                                                     (3.2)
                          s = b + 1, . . . , a + b − 1 and is odd.

Proof. Consider decomposition (1.6), where the coeﬃcients can be calculated using
the formulae
                                   
          1     da−j             
                                 a 
Ak,j =                R(t)(t + k)        ,            k = 0, ±1, . . . , ±n,   j = 1, 2, . . . , a.
       (a − j)! dta−j                t=−k

First of all we claim that

                                                   ((2r + 1)n)!2b (2n)!a−2rb
                    max       |Ak,a| = |A0,a | =                             .               (3.3)
              k=0,±1,...,±n                                n!2(a+b)
518                                      W. Zudilin

Since |Ak,a| = |A−k,a| for k = 0, 1, . . . , n, it is suﬃcient to show that |Ak,a| decreases
as k increases from 0 to n. This can be veriﬁed directly:

   |Ak,a|       ((2r + 1)n + k)b           (n − k + 1)a+b
           =                             ·
  |Ak−1,a|   ((2r + 1)n − k + 1)       b     (n + k)a+b
                                                  b          a+b
                ((2r + 1)n + k) · (n − k + 1)           n−k+1
           =                                          ·
                ((2r + 1)n − k + 1) · (n + k)             n+k
                                                             b              a+b
                (2r + 1)n2 − k(k − 1) + n(−2rk + 2r + 1)           n − (k − 1)
           =                                                     ·
                    (2r + 1)n2 − k(k − 1) + n(2rk + 1)                n+k
           < 1,      k = 1, . . . , n.

  We now ﬁx an integer k, |k| ⩽ n, and denote the logarithmic derivative of
R(t)(t + k)a by gk (t):

                                    
                                  (2r+1)n
                                               1             1   n
                    gk (t) = b                    − (a + b)      .
                                              t+l            t+l
                                 l=−(2r+1)n                   l=−n
                                    l=k                       l=k

Then for j = 0, 1, 2, . . . the modulus of the quantity
                                    −(n+1)
           1 dj gk (t)                           (−1)j         
                                                                (2r+1)n
                                                                           (−1)j
                          =b                                + b
           j! dtj t=−k                          (l − k)j+1             (l − k)j+1
                                   l=−(2r+1)n                      l=n+1

                                        
                                        n
                                                   (−1)j
                                   −a
                                                (l − k)j+1
                                        l=−n
                                         l=k

is bounded above by 2(2rb + a)n (we estimate every summand on the right-hand
side by 1). Using Leibniz’ rule for the diﬀerentiation of a product, we obtain that
                                             
            1 dj−1                         
                                          a 
  Ak,a−j =           g k (t) · R(t)(t + k)   
            j! dtj−1                           t=−k
                                                   
            1 j−1
                         1        d j−1−m
                                           gk (t) 
         =                                           · Ak,a−m ,   j = 1, . . . , a − 1,
            j m=0 (j − 1 − m)! dtj−1−m t=−k
                                                                                    (3.4)

whence

                                     1 
                                        j−1
         |Ak,a−j | ⩽ 2(2rb + a)n ·         |Ak,a−m |
                                     j m=0
                  ⩽ 2(2rb + a)n ·        max         |Ak,a−m |,       j = 1, . . . , a − 1.   (3.5)
                                     m=0,1,...,j−1

We obtain the following estimate from (3.5) by induction:
                                        j−1
                 |Ak,a−j | ⩽ 2(2rb + a)n      |Ak,a|,             j = 1, . . . , a.
                         Irrationality of values of the zeta function                        519

By (3.3), we have
                                          a−1 ((2r + 1)n)!2b (2n)!a−2rb
               |Ak,a−j | ⩽ 2(2rb + a)n                                    ,
                                                        n!2(a+b)
                          k = 0, ±1, . . . , ±n, j = 1, . . . , a.

Combining this with (1.11) and (1.12), we obtain that
                                            a−1 ((2r + 1)n)!2b (2n)!a−2rb
      |Ās | ⩽ 2a+b−2 (2n + 1)2 2(2rb + a)n                                 ,
                                                              n!2(a+b)                      (3.6)
                        s = 0 or s = b + 1, . . . , a + b − 1.

We obtain the limiting relations (3.1) from (3.6) using Stirling’s formula (2.17) for
Γ(z) = (z − 1)! with positive integers z → ∞.
   If a is an even integer and j is an even integer such that 0 ⩽ j < a, then
formula (3.4) with k = 0 implies that |A0,a−j | ⩾ |A0,a|. If a is even and s is odd,
b < s < a + b, then the summands on the right-hand side of (1.11) have the same
sign, whence
               |Ās | ⩾ |A0,a|,      s = b + 1, . . . , a + b − 1 and is odd.
So we have obtained both upper and lower estimates for the asymptotics of coef-
ﬁcients of linear forms (1.5) for even a using Stirling’s formula. This proves the
limiting relations (3.2) and completes the proof of the proposition.
   It turns out that the estimate (3.1) holds for odd values of a as well. The results
obtained in § 2 enable us to calculate the asymptotics of the coeﬃcients (1.11) for
odd a. This will occupy the rest of this section.
   For positive integers m the following expansion holds in the neighbourhood of
the point t = 0:
                                     2m    ∞
                               sin πt              (m)
                                          =      dl t2l ,                        (3.7)
                                 π
                                                 l=m
       (m)                                          (m)
where dl , l = m, m + 1, . . . , are real numbers, dm = 1.
Lemma 3.1. Assume that a is an odd integer. Then the following recurrence
relations hold for the coeﬃcients of the linear form (1.5):
                                                    2m
                (2m + b − 1)! (−1)b iM +∞ sin πt
    Ā2m+b = −                                           R(t) dt
                (2m)! (b − 1)! πi     iM −∞       π
                     
                    (a−1)/2
                              (2l)! (2m + b − 1)! (m)                                   a−1
                −                                d Ā2l+b ,         m = 1, 2, . . . ,       ,
                              (2m)! (2l + b − 1)! l                                      2
                    l=m+1                                                                  (3.8)
where M > 0 is an arbitrary real constant.
Proof. If m is a positive integer, then (3.7) implies that the following expansion
holds in the neighbourhood of t = −k ∈ Z:
                       2m                 2m   ∞
                 sin πt         sin π(t + k)            (m)
                            =                   =      dl (t + k)2l .
                   π                 π
                                                          l=m
520                                            W. Zudilin

   Formula (1.6) implies that the following formulae hold in the neighbourhood of
t = −k for the function deﬁned by (1.1):

                                    Ak,a       Ak,a−1         Ak,1
                    R(t) =               a
                                           +        a−1
                                                        +···+      + O(1),
                                  (t + k)    (t + k)          t+k

where k = 0, ±1, . . . , ±n, and R(t) = O(1) in the neighbourhood of t = −k ∈ Z,
|k| > n. Therefore,
                                                
                                 2m          0                              if |k| > n,
                         sin πt                 
              Res                        R(t) =      (m)
                                                  (a−1)/2
             t=−k          π                    
                                                         dl Ak,2l+1             if |k| ⩽ n,
                                                       l=m

for m < a/2 and any integer k. If the closed contour L goes around the points
0, ±1, . . . , ±n anticlockwise, then

                          2m                          
                                                        (a−1)/2
        1          sin πt                                           (2l)! (b − 1)! (m)
                                   R(t) dt = (−1)b−1                              d Ā2l+b
       2πi   L       π                                              (2l + b − 1)! l
                                                         l=m
                                                            (2l)! (b − 1)! (m)
                                                          (a−1)/2                      
                        b−1       (2m)! (b − 1)!
             = (−1)                              Ā2m+b +                      d Ā2l+b ,
                                  (2m + b − 1)!                   (2l + b − 1)! l
                                                              l=m+1                                   (3.9)

                                                              (m)
which follows from (1.11) and the relation dm                       = 1. We deduce from (3.9) the
following recurrence formulae:
                                                           2m
                   (2m + b − 1)! (−1)b              sin πt
      Ā2m+b =                                                      R(t) dt
                   (2m)! (b − 1)! 2πi          L      π
                            
                        (a−1)/2
                                    (2l)! (2m + b − 1)! (m)                                       a−1
                    −                                  d Ā2l+b ,             m = 1, 2, . . . ,       .
                                    (2m)! (2l + b − 1)! l                                          2
                        l=m+1                                                                        (3.10)

                                                   Figure 8
                           Irrationality of values of the zeta function                           521

  Now let the contour of integration L be the rectangle with vertices ±N ± iM ,
where M > 0 is a ﬁxed real constant and N > n is suﬃciently large (see Fig. 8).
As N → ∞, the following estimates hold on the vertical sides of the rectangle:
                                   
                            sin πt  eπM
                                                 R(t) = O(N −2 ).
                            π ⩽ π ,

Therefore, we have
                2m
  1        sin πt
                      R(t) dt
 2πi    L    π
               iM −N         −iM +N         2m
           1                            sin πt
        =               +                          R(t) dt + O(N −1 )                as N → ∞
          2πi iM +N         −iM −N        π
                                                                                          (3.11)

for m = 1, 2, . . ., (a−1)/2, where the constant in O(N −1 ) depends only on M . Since
the integrand in (3.11) is an odd function (see (1.8)) and the contour L is symmetric
with respect to 0, it is suﬃcient to integrate over half the contour and double the
result. Passing to the limit as N → ∞, we obtain the recurrence formulae (3.8)
from (3.10), which completes the proof of the lemma.
   It follows from Lemma 3.1 that the asymptotic behaviour of the coeﬃcients of
the linear form (1.5) is closely connected with the asymptotics of the integrals

                 iM +∞      2m
           1          sin πt
Kn,m =                           Rn (t) dt
           πi iM −∞     π
                                2m+b
          (−1)bn iM +∞ sin πt
        =
            πi    iM −∞       π
              Γ(±t + (2r + 1)n + 1)b Γ(t − n)a+b (2n)!a−2rb                                   a−1
          ×                                                 dt,           m = 1, 2, . . . ,        ,
                            Γ(t + n + 1)a+b                                                     2
                                                                                               (3.12)

as n → ∞, where we have used formula (2.15). As in § 2, we assume that the cuts
(−∞, n] and [(2r + 1)n, +∞) are made in the t-plane.
Lemma 3.2 (compare [23], § 6.5). For any y0 > 0 the asymptotic equality
                       
                      1                  √                        
       log Γ(z) = z −     log z − z + log 2π + O |z|−1 + O e−2π Im z                           (3.13)
                      2

holds in the domain Im z ⩾ y0 .
Proof. The asymptotic relation (2.17) holds in the domain | arg z| < π − ε, but the
identity
                                      π              2πi
                 Γ(z)Γ(−z) = −             = −πiz                            (3.14)
                                  z sin πz    ze    (1 − e2πiz )
522                                       W. Zudilin

enables us to write down asymptotics in the quadrant Im z > 0, Re z < 0 as well.
Making the cut (−∞, 0] in the z-plane and ﬁxing principal values of the argument,
we deduce from (2.17) and (3.14) the following relation in this quadrant:

        log Γ(z) = log(2πi) − log z + πiz − log(1 − e2πiz ) − log Γ(−z)
                                                                  
                                        1
                 = log(2π) + πi z +         − log z − log(1 − e2πiz )
                                        2
                                                                       
                                  1                         √           
                     −     −z −      (log z − πi) + z + log 2π + O |z|−1
                                  2
                          
                         1                   √             
                 = z−        log z − z + log 2π + O |z|−1 + log(1 − e2πiz ). (3.15)
                         2

Observing that |e−2πiz | ⩽ u0 := e−2πy0 < 1 in the domain Im z ⩾ y0 and combin-
ing (3.15) with the relation | ln(1 − u)| ⩽ C|u|, which holds for |u| ⩽ u0 with some
constant C depending only on u0 , we complete the proof of formula (3.13).
Lemma 3.3. Let µ be a positive real constant. Then the relation
                              √
                    (−1)bn (2 πn )a−2rb 2b                           
     Kn,m = K̃n,m ·          2m  a−1
                                            · 1 + O(n−1 ) + O(e−2πnµ )
                           π n
holds for the integrals (3.12) as n → ∞, where

             1     iµ+∞
                                                                                        a−1
  K̃n,m =                 sin2m+b πnτ · enf(τ) g(τ ) dτ,            m = 1, 2, . . . ,       ,   (3.16)
             πi   iµ−∞                                                                   2

and the functions f(τ ), g(τ ) are deﬁned by (2.12) and (2.13) (see also Remark 2.1).
Proof. The proof repeats the proof of Lemma 2.5 except that we replace the asymp-
totics (2.17) by (3.13) (when integrating over the contour Im t = M = µn, µ > 0).
Lemma 3.4. Assume that (2.61) holds for the real root µ1 ∈ (2r + 1, +∞) of the
polynomial (2.21), and assume that

                                             √        log(r2 + r)
                               |η1 | < min       3,                                             (3.17)
                                                           π

for the purely imaginary root η1 ∈ (0, +i∞) of minimal absolute value. Then the
following relation holds for integrals (3.16) as n → ∞:

                                     |g(η1 )|                                     
      |K̃n,(a−1)/2| =                                    en Re f0 (η1 ) 1 + O(n−1 ) ,
                     |f  (η1 )|1/2 2a+b−1/2 π 1/2 n1/2
                                                                                                (3.18)
                                                                            a−1
           |K̃n,m| = |K̃n,(a−1)/2 | · O(e−2πnµ ),         m = 1, 2, . . . ,     − 1,
                                                                             2
where the constant µ is deﬁned by the equality iµ = η1 .
Proof. By Lemma 2.7, λ = a + b − 1 in equation (2.22) corresponds to the root
iµ = η1 of the polynomial (2.21).
                          Irrationality of values of the zeta function                  523

   Using the equality
                       πinτ          2m+b
                       e     − e−πinτ
    sin2m+b πnτ =
                             2i
                         (−1)(a+b)/2 −πi(a+b−1)nτ    
                                                    a+b−1
                  = χm       a+b−1
                                     e            +       hm,l ie−πi(a+b−2l−1)nτ ,
                           2       i
                                                              l=1
                                                    a−1
                                   m = 1, 2, . . .,     ,
                                                     2
where                                              a−1
                                           1 if m =      ,
                               χm =                    2
                                           0 otherwise
and hm,l , m = 1, . . . , (a − 1)/2, l = 1, . . . , a + b − 1 are real coeﬃcients, we write
the integrals (3.16) as

                                               1 
                                                 a+b−1
                        (−1)(a+b)/2
        K̃n,m = −χm                 Jn,a+b−1 +         hm,l Jn,a+b−2l−1 ,
                         2a+b−1 π              π                                      (3.19)
                                                        l=1
                                                  a−1
                                m = 1, 2, . . . ,     ,
                                                   2
where
               iµ+∞
    Jn,k =            en(f(τ)−kπiτ) g(τ ) dτ,      k = 0, ±1, . . . , ±(a + b − 1).   (3.20)
              iµ−∞

   First we shall study the asymptotics of the integral Jn,a+b−1 . The path of inte-
gration passes through the saddle point η1 = iµ. We claim that x = 0 is a maximum
point of the function
                                                        
                     f˜(x) = Re(f(τ ) − (a + b − 1)πiτ )τ=x+iµ .            (3.21)

We have
                                                   
             f˜ (x) = Re(f  (τ ) − (a + b − 1)πi)τ=x+iµ = Re f  (x + iµ).

Hence, the sole candidates for maximum points of (3.21), besides x = 0, are
x = ±x0 , where x0 + iµ is the point of intersection of the ray τ = x + iµ, x > 0,
with the curve Re f  (τ ) = 0 in the domain Re τ > 0 (see Fig. 4) at which Re f  (τ )
changes the sign from + to − (if there is such a point). On the other hand,

              f(τ ) − (a + b − 1)πiτ = f0 (τ ) + f  (τ )τ − (a + b − 1)πiτ

for the function f0 (τ ) deﬁned in (2.48).          By Lemma 2.10 and the inequality
Im f  (x0 + iµ) > 0, we have

        f˜(±x0 ) = f˜(x0 ) = Re f0 (x0 + iµ) − µ Im f  (x0 + iµ) + (a + b − 1)πµ
                < Re f0 (µ1 ) + (a + b − 1)πµ.                                        (3.22)
524                                     W. Zudilin

The inequality
                                                     r(r + 1)
                   2r + 1 < µ1 ⩽ 2r + 1 + 2ε,         ε :=    ,           (3.23)
                                                    6(2r + 1)
which follows from (2.61), enables us to obtain an upper estimate for Re f0 (µ1 ).
We have
Re f0 (µ1 ) < b(2r +1) log((2r +1+ε)ε)−(a+b) log((r +1)r) < −(a−2rb) log(r 2 +r),
since (2r + 1 + ε)ε < r(r + 1) by (3.23). Continuing estimate (3.22) and using
inequality (3.17), we obtain the inequalities
               f˜(±x0 ) < −(a − 2rb) log(r2 + r) + (a + b)πµ
                         ⩽ −(a − 2rb) log(r2 + r) + (a + b) log(r2 + r)
                         = b(2r + 1) log(r2 + r).                                   (3.24)
To obtain a lower estimate for f˜(0), we use the inequalities
                                                         √
              |iµ ± (2r + 1)| > 2r + 1,     |iµ ± 1| ⩽ |i 3 ± 1| = 2.
We have
    f˜(0) = Re f0 (iµ) > 2(a − 2rb) log 2 + 2b(2r + 1) log(2r + 1) − 2(a + b) log 2
                                                
                                              1
                       = 2b(2r + 1) log r +          > b(2r + 1) log(r2 + r).        (3.25)
                                              2
   Comparing (3.24) with (3.25), we obtain that f˜(0) > f(±x     ˜   0 ). Hence, the saddle
point τ = iµ is a maximum point of the function Re(f(τ ) − (a + b − 1)πiτ ) on the
contour Im τ = µ. Therefore, Jn,a+b−1 is equal to the contribution of the saddle
point iµ = η1 :
                         (2π)1/2 g(η1 ) n Re(f(η1 )−(a+b−1)πiη1 )              
          Jn,a+b−1 =                   e                          1 + O(n−1 )
                       |f (η1 )|1/2 n1/2
                         (2π)1/2 g(η1 ) n Re f0 (η1 )             
                    =                  e             1 + O(n−1 ) ,                 (3.26)
                       |f (η1 )| n
                                1/2  1/2

and a similar estimate holds for the integral of the modulus of the integrand:
     iµ+∞
                                            (2π)1/2 |g(η1 )| n Re f0 (η1 )            
           |en(f(τ)−(a+b−1)πiτ) g(τ )| dτ =                   e           1 + O(n−1 ) .
    iµ−∞                                   |f (η1 )| n  1/2 1/2

                                                                                     (3.27)
  For the integrals (3.20) with k < a + b − 1 we use the relation
            |en(f(τ)−kπiτ) g(τ )| = |en(f(τ)−(a+b−1)πiτ) g(τ )| · e−(a+b−1−k)nµ
on the contour Im τ = µ. Combining this with (3.27) and (3.26), we obtain the
inequality
      |Jn,k | ⩽ Ce−(a+b−1−k)nµ|Jn,a+b−1 |,       k = 0, ±1, . . . , ±(a + b − 1),   (3.28)
with some constant C > 0 that does not depend on n or k. (Inequality (3.28)
is obtained by integration along a ﬁnite segment, say [iµ − 1, iµ + 1], since the
contribution of the integral over the remaining inﬁnite part is exponentially small
compared with the contribution of iµ.) Substituting estimates (3.26) and (3.28)
into (3.19), we obtain (3.18), which completes the proof of the lemma.
                        Irrationality of values of the zeta function                525

Proposition 3.2. Let a, b, r be positive integers, let a, b be odd integers, a > 2rb,
assume that the real root µ1 ∈ (2r + 1, +∞) of the polynomial (2.21) is such
that (2.61) holds, and assume that (3.17) holds for the purely imaginary root
η1 ∈ (0, +i∞) of minimal absolute value. Then the following asymptotic formula
holds for the coeﬃcients Ās of the linear form (1.5):

       log |Ās |       22(a−2rb)|η1 + 2r + 1|b(2r+1)| − η1 + 2r + 1|b(2r+1)
    lim           ⩽ log                                                      ,   (3.29)
   n→∞    n                           |η1 + 1|a+b |η1 − 1|a+b

where s = 0 or s = b + 1, . . . , a + b − 1 and is odd. In the case when s = a + b − 1
the upper limit becomes a limit and the inequality becomes an equality.

Proof. The limiting relation

                                   log |Āa+b−1 |
                             lim                  = Re f0 (η1 )
                             n→∞          n

follows from formula (3.8) with m = (a − 1)/2 by Lemmas 3.3 and 3.4. For the
other odd integers s, b < s < a+b−1, estimates (3.29) follow from Lemmas 3.1, 3.3
and 3.4. In the case when s = 0 formula (1.5) implies that
                                                
                             |Ā0 | ⩽ |I| +               |Ās |ζ(s),
                                               s is odd
                                              b<s<a+b

whence
                            log |Ā0 |
                      lim              ⩽ max{Re f0 (τ0 ), Re f0 (η1 )},          (3.30)
                     n→∞       n
where the root τ0 of polynomial (2.21) is deﬁned in Proposition 2.3. Lemma 2.10
implies that Re f0 (τ0 ) < Re f0 (µ1 ). The inequality Re f0 (µ1 ) < Re f0 (η1 ) (even a
stronger one) was proved in Lemma 3.4. Therefore, the maximum on the right-hand
side of (3.30) is equal to Re f0 (η1 ), which completes the proof of the proposition.

Remark 3.1. Estimate (3.29) is but a slight improvement of (3.1), and will not be
used in the proofs of Theorems 0.3 and 0.4. However, it is quite natural (and could
have been foreseen) that the asymptotics of linear forms and their coeﬃcients is
determined by the values of the same function Re f0 (τ ) at diﬀerent roots of the
same polynomial (2.21). (In the case when a is an even integer the asymptotics
of the coeﬃcients of the linear form (1.5) is determined by the root η0 = 0 of
polynomial (2.21); see Proposition 3.1.)

       § 4. Reﬁned estimates for the denominators of linear forms
   The asymptotics of the denominators of linear forms (1.2) (as n → ∞) obtained
in Lemma 1.4, although somewhat coarse, is suﬃcient for the proof of Rivoal’s theo-
rem. We shall reﬁne our results on denominators using the following generalization
of Lemma 1.2.
526                                          W. Zudilin

Lemma 4.1. Assume that for some polynomial P (t), deg P (t) < m(n + 1), the
rational function

                                            P (t)
                     R(t) =                                     m
                             (t + s)(t + s + 1) · · · (t + s + n)

(which may be reducible) satisﬁes the conditions
                                                     
                           Dnj dj                  
                                                   m 
                                      R(t)(t   + k)         ∈ Z,
                            j! dtj                     t=−k                                      (4.1)
                     k = s, s + 1, . . . , s + n, j = 0, 1, . . . , m − 1,

where Dn is the least common multiple of the numbers 1, 2, . . . , n. Then
                                
          Dnj dj              
                              m 
                   R(t)(t + k)        ∈ Z,    k = s, s + 1, . . . , s + n,                      (4.2)
           j! dtj                 t=−k

for all non-negative integers j.
Proof. For the integers j = 0, 1, . . . , m − 1, the inclusions (4.2) follow directly
from (4.1). In what follows we consider only the integers j ⩾ m.
   The rational function R(t) can be decomposed into a sum of partial fractions as
follows:

                   
                   s+n
                              Bl,0      Bl,1             Bl,m−2     Bl,m−1
                                                                           
          R(t) =                   +           + · · · +          +          ,                   (4.3)
                           (t + l)m (t + l)m−1           (t + l)2    t+l
                   l=s

where
                           
       1 dj              
                         m 
Bk,j =        R(t)(t + k)        ,             k = s, s + 1, . . . , s + n,    j = 0, 1, . . . , m − 1.
       j! dtj                t=−k

Since diﬀerentiation is a linear operation and formulae (4.3) and (4.1) hold, it is
suﬃcient to show that
                                                     
                    Dnj−q dj                    1      
                                  (t + k)m                       ∈ Z,
                      j! dt  j             (t + l)m−q                       (4.4)
                                                        t=−k
                    q = 0, 1, . . ., m − 1, k, l = 0, ±1, . . . , ±n.

  Since
                                                            
                       ((t + l) − (l − k))m 
                                                  m
          m    1                                         p m (t + l)
                                                                    m−p
                                                                        (l − k)p
  (t + k)            =                       =       (−1)
          (t + l)m−q        (t + l)m−q           p=0
                                                             p   (t + l)m−q
                       m           
                                   m
                     =     (−1)p       (l − k)p (t + l)q−p ,
                       p=0
                                   p
                         q = 0, 1, . . . , m − 1,   k, l = 0, ±1, . . . , ±n,
                          Irrationality of values of the zeta function                         527

we have for the integers j ⩾ m that
                                          
            1 dj                    1        
                     (t +  k)m               
            j! dtj             (t + l)m−q    
                                              t=−k
                       m           
                                    m   (q −  p)(q − p − 1) · · · (q − p − j + 1)
                  =         (−1)p
                        p=0
                                    p                     j!
                                             
                                               
                    × (l − k)p (t + l)q−p−j 
                                                  t=−k
                               m          
                         1             p+j m (p − q)j
                  =                (−1)                                                       (4.5)
                    (l − k)j−q p=0         p    j!

if l = k and
                                                       
                            1 dj           m      1
                                    (t + k)               =0
                            j! dtj           (t + l)m−q
if l = k. Since
                                                      
                          Dnj−q                       m (p − q)j
                                 ∈ Z     and                        ∈ Z,
                     (l − k)j−q                       p       j!
        q = 0, 1, . . . , m − 1, p = 0, 1, . . . , m, k, l = 0, ±1, . . . , ±n, k = l,

the inclusions (4.4) follow from (4.5), which completes the proof of the lemma.
    The next lemma strengthens the inclusions (1.17). It will be used in our expo-
sition of the general case.
Lemma 4.2. We denote by E = En,m the set of primes dividing each of the numbers

                                       (m + 2n ± k)!
     Bk,0 = F (t)(t + k)2 t=−k =                          ,         k = 0, ±1, . . . , ±n,
                                        (m ± k)! (n ± k)!2

where the function F (t) is deﬁned in (1.15). Let
                                                    
                               Π = Πn,m =                     p.                              (4.6)
                                              √     p∈E
                                                  m+3n<p⩽2n

Then                                    
                    j
                  D2n dj              
                                      2 
           Π−1            F (t)(t + k)        ∈ Z,           k = 0, ±1, . . . , ±n,          (4.7)
                   j! dtj                 t=−k

for all non-negative integers j.
Proof. The fact that Π−1 Bk,0 ∈ Z, k = 0, ±1, . . . , ±n (inclusions (4.7) with j = 0)
follows from the deﬁnition of E and Π. Let us verify inclusions (4.7) with j = 1.
528                                     W. Zudilin

We have                   
         d              
                        2 
  Bk,1 =    F (t)(t + k) 
         dt                 t=−k
               m+2n                       
                                       
                                        n     
                         1       1         1  
       = Bk,0                 +      −2       
                        t+l t−l           t+l 
                 l=m+1                         l=−n          t=−k
                                                l=k
               m+2n                    
                       1   1       
                                    n
                                       1
       = Bk,0             −      −2        ,                          k = 0, ±1, . . . , ±n.
                       l−k l+k        l−k
                 l=m+1                          l=−n                                      (4.8)
                                                 l=k
By Lemma 1.3, we have D2n Bk,1 ∈ Z, k = 0, ±1, . . . , ±n. Therefore,
                       ordp (Π−1 D2n Bk,1 ) = ordp (D2n Bk,1 ) ⩾ 0                       (4.9)
if p is coprime with Π. Now assume that a prime p divides Π, whence
                                ordp Π = 1.                                  (4.10)
        √
For p > m + 3n we have ordp (l±k) ⩽ 1, where (l±k) is any denominator in (4.8).
Therefore,
       m+2n                          
               1    1         n
                                     1
 ordp             −        −2             ⩾ −1,       k = 0, ±1, . . . , ±n. (4.11)
               l−k l+k             l−k
        l=m+1                       l=−n
                                     l=k

We have
                                       ordp D2n ⩾ 1                                    (4.12)
for p ⩽ 2n. Finally,
                         ordp Bk,0 ⩾ 1,      k = 0, ±1, . . . , ±n,                    (4.13)
if p ∈ E.
    Combining estimates (4.10)–(4.13) and taking (4.8) into account in the case
when p divides Π, we obtain that
                                ordp (Π−1 D2n Bk,1 ) ⩾ 0.                              (4.14)
                                  −1
By (4.9) and (4.14), we have Π D2n Bk,1 ∈ Z, k = 0, ±1, . . . , ±n, which proves
that (4.7) holds for j = 1. In the case when j ⩾ 2 it remains to use Lemma 4.1
with m = 2.
   Note that under the assumptions of Lemma 4.2 we have
                                               
                m + 2n k        m k           n k
 ordp Bk,0 =            ±    −     ±     −2     ± ,      k = 0, ±1, . . . , ±n, (4.15)
                   p      p     p p           p p
                   √
for any prime p > m + 3n, since
                              
                          q      q        q
               ordp q! =     + 2 + 3 +··· ,             q = 1, 2, . . . ,       (4.16)
                          p      p       p
where · stands for the integer part of a number. Formula (4.15) enables us to
calculate the asymptotics of the factor (4.6) as n, m → ∞, since
               √                  √                                        
  {p ∈ E : p > m + 3n } = p > m + 3n :            min    {ordp Bk,0 } ⩾ 1 . (4.17)
                                                 k=0,±1,...,±n

  Consider, for example, the simplest version of (1.15) with m = n.
                        Irrationality of values of the zeta function                529

Lemma 4.3.
                                            
             log Πn,n     1      1              5
   1 = lim           =ψ     −ψ     + ψ(1) − ψ     − 1 ≈ 0.4820,                  (4.18)
         n→∞     n        2      3              6
where ψ(x) = Γ (x)/Γ(x) is the logarithmic derivative of the gamma function.
                                             √
Proof. In the case when m = n and p > 2 n, formula (4.15) implies that
                                                                
                                                             n k
                      min       {ordp Bk,0 } =    min ϕ1      ,    ,        (4.19)
                  k=0,±1,...,±n                |k/p|⩽|n/p|   p p
where
              ϕ1 (x, y) = 3x + y + 3x − y − 3 x + y − 3 x − y .                   (4.20)
It is obvious that the function (4.20) is periodic (with period 1) in each argument:
                    ϕ1 (x, y) = ϕ1 ({x}, {y}),        {x} = x − x .

Therefore, it is suﬃcient to calculate the values of this function inside the unit
square. By the deﬁnition of the integer part of a number, the summands on the
right-hand side of (4.20) change their values only when the point passes through
the lines 3x ± y = const ∈ Z and x ± y = const ∈ Z (see Fig. 9). This enables us to
obtain the values of ϕ1 (x, y) shown in Fig. 10.

        Figure 9. The values of the functions 3x + y, 3x − y and
        −3(x + y + x − y) inside the unit square

         Figure 10. The values of the function ϕ1 (x, y) inside the unit square
530                                      W. Zudilin

    Consider the perpendiculars to the x-axis passing through the points of inter-
section of the lines shown in Fig. 10. We have
                                                                   
                                       1 if {x} ∈ E = 1 , 1 ∪ 5 , 1 ,
                                                     1
   min ϕ1 (x, y) = min ϕ1 ({x}, y) =                       3 2     6        (4.21)
  |y|⩽x            0⩽y⩽1              
                                        0 otherwise.
Formulae (4.17), (4.19) and (4.21) imply that
                                 √            √                   n
                {p ∈ En,n : p > 2 n } = p > 2 n :                     ∈ E1 ,
                                                                  p
whence
                                                                   
                   Πn,n =                p=               p                 p.   (4.22)
                            p:{n/p}∈E         p:{n/p}∈E           2n<p⩽3n
                             √       1              √ 1
                            2 n<p⩽2n             p>2 n

We have the following formula for the denominator of the fraction on the right-hand
side of (4.22):
                                           D3n
                                         p=     .                             (4.23)
                                            D2n
                                   2n<p⩽3n

We can ﬁnd asymptotics of the numerator using following lemma (cf. [25], Theo-
rem 4.3 and § 6, and [26], Lemma 3.2).
Lemma 4.4. The limiting relation
                        1     
                   lim                        log p = ψ(v) − ψ(u)
                  n→∞ n        √
                                  p> Cn
                                {n/p}∈[u,v)

holds for any C > 1 and any interval [u, v) ⊂ (0, 1).
   Using Lemma 4.4 and relations (4.22), (4.23) and (1.24), we obtain the desired
asymptotics (4.18), which completes the proof of Lemma 4.3.
Remark 4.1. Simple as it is, the calculation of (4.21) can be made four times simpler.
It is easy to verify that function (4.20) is not only periodic, but invariant under the
transformations
                                           
                                  1       1
               ϑ1 : (x, y) → x + , y +       ,    ϑ2 : (x, y) → (x, 1 − y)     (4.24)
                                  2       2
(in the last map we use the shift by 1 and the fact that ϕ1 (x, y) is odd with respect
to y). Therefore, it is suﬃcient to ﬁnd the values of the function (4.20) on the
square 0 ⩽ x, y < 12 and then use the transformations ϑ1 , ϑ1 ◦ ϑ2 and ϑ2 to extend
this function to the unit square and so by periodicity to the whole of R2 .
   The next object of our study is the rational function
                                    (t ± (n + 1)) · · · (t ± (n + 2rn))
                 G(t) = Gn (t) :=                              2r     .        (4.25)
                                          t(t ± 1) · · · (t ± n)
Lemma 1.3 and the Leibniz rule for diﬀerentiating a product imply that
                       
   j
 D2n dj              
                    2r 
         G(t)(t + k)         ∈ Z,    k = 0, ±1, . . . , ±n, j = 0, 1, 2, . . . . (4.26)
  j! dtj                 t=−k
                          Irrationality of values of the zeta function                    531

                                                                                    (r)
Lemma 4.5. For every integer r ⩾ 1 there is a sequence of integers Πn = Πn ⩾ 1,
n = 1, 2, . . . , such that
                                        
                   j
                 D2n  dj              
                                     2r 
        Π−1
          n               G(t)(t + k)        ∈ Z, k = 0, ±1, . . . , ±n, (4.27)
                  j! dtj                 t=−k

for all non-negative integers j, and
                (r)      r                               r
           log Πn                 l          l                      1
r = lim            = −2      ψ      +ψ              − (4r + 1)       − 4rγ + 4r,
     n→∞      n                  r        r + 1/2                   l
                         l=1                                    l=1
                                                                           (4.28)
where γ ≈ 0.57712 is Euler’s constant.
Proof. For n ⩽ 2r we put Πn = 1. Then the inclusions (4.27) follow from (4.26).
This ﬁnite part of the sequence has no inﬂuence on the limit (4.28). In what follows
we assume that n > 2r.
  For every prime p we consider the quantity
                                          ((2r + 1)n + k)! ((2r + 1)n − k)!
            νp =       min         ordp                                     .        (4.29)
                   k=0,±1,...,±n              (n + k)!2r+1 (n − k)!2r+1
Put                                             
                               Πn =                          pν p .                  (4.30)
                                          √
                                       p:     (2r+2)n<p⩽2n

  We ﬁx an integer k in the interval |k| ⩽ n and consider the function

                                   Gk (t) := G(t)(t + k)2r .                         (4.31)

We claim that
                                        
                           j
                         D2n dj Gk (t) 
                   Π−1                    ∈ Z,               j = 0, 1, 2, . . . .    (4.32)
                    n
                          j!    dtj t=−k

By Lemma 4.1, it is suﬃcient to prove the inclusions (4.32) for j ⩽ 2r.
  If p is a prime that does not divide Πn , then (4.26) implies that
                                           j                 
                   j   j      
              −1 D2n d Gk (t)                 D2n dj Gk (t) 
      ordp Πn                        = ordp                         ⩾ 0.             (4.33)
                  j!     dtj t=−k              j!    dtj t=−k

   Now assume that p is a prime dividing Πn . We shall prove by induction on
j = 0, 1, . . . , 2r that
                                                  
                                     j  j       
                                −1 D2n d Gk (t) 
                          ordp Πn                     ⩾ 0.             (4.34)
                                    j!    dtj t=−k

For j = 0 relation (4.34) follows from the deﬁnition of Πn , since
                                ((2r + 1)n + k)! ((2r + 1)n − k)!
                   Gk (t)t=−k =                                   .
                                     (n + k)!2r+1 (n − k)!2r+1
532                                           W. Zudilin

We claim that (4.34) holds for j + 1 if it holds for all preceding j. We shall use the
following notation for the logarithmic derivative of the function (4.31):

                             Gk (t)        
                                          (2r+1)n
                                                       1              1
                                                                     n
                  gk (t) =           =                    − (2r + 1)      .
                             Gk (t)                   t+l             t+l
                                         l=−(2r+1)n                l=−n
                                            l=k                    l=k

We have

           1    dj+1 Gk (t)      1     dj             
                            =              gk (t)Gk (t)
        (j + 1)! dtj+1        (j + 1)! dtj
                                      1 
                                           j
                                                  1   dj−m gk (t) 1 dm Gk (t)
                                  =                              ·            . (4.35)
                                    j + 1 m=0 (j − m)! dtj−m       m! dtm

We also have
                                                    1
                                           ordp        = 0,                      (4.36)
                                                  j +1
since p >     (2r + 2)n > 2r + 1 ⩾ j + 1. Further, we have
                                       
                   1   dj−m gk (t) 
       ordp
               (j − m)! dtj−m t=−k
                      (2r+1)n                                          
                                    (−1)j−m             
                                                         n
                                                              (−1)j−m
              = ordp                          − (2r + 1)
                                 (l − k)j−m+1              (l − k)j−m+1
                         l=−(2r+1)n                              l=−n
                            l=k                                  l=k

              ⩾ −(j − m + 1)                                                     (4.37)

for m < j, since p > (2r + 2)n and |l − k| ⩽ (2r + 2)n for all denominators
in (4.37). The inequality

                                         j−m+1
                                   ordp D2n    ⩾ j −m+1                          (4.38)

holds, since p ⩽ 2n. Finally,
                                                     
                                       m
                                      D2n dm Gk (t) 
                             ordp Π−1                    ⩾0                      (4.39)
                                   n
                                      m!    dtm t=−k

by the induction hypothesis. Substituting t = −k into (4.35) and using esti-
mates (4.36)–(4.39), we obtain that relation (4.34) holds for j + 1. This completes
the justiﬁcation of the induction step.
   Combining estimates (4.33) for p  Πn and (4.34) for p | Πn , we obtain that the
inclusions (4.32) and (4.27) hold for j = 0, 1, . . . , 2r. Therefore, they hold for all
non-negative integers j. We claim that the limiting relation (4.28) holds for the Πn ,
n = 1, 2, . . . .
                            Irrationality of values of the zeta function                          533

  By (4.29) and (4.16),
                                                                     
                                                                n k
                                  νp =      min        ϕr        ,                              (4.40)
                                         |k/p|⩽|n/p|            p p
for every integer n > 2r and prime p >            (2r + 2)n, where the function
 ϕr (x, y) = (2r +1)x+y + (2r +1)x −y −(2r +1) x+y −(2r +1) x−y                                 (4.41)
is periodic (with period 1) in each argument. We claim that
                  min ϕr (x, y) = ν   if {x} ∈ Eν ,             ν = 0, 1, . . . , 2r − 1,       (4.42)
                  y∈R
where                                         
                l l+1         1    l 1      l+1
      E2l =       ,       ∪     + , +              ,    l = 0, 1, . . ., r − 1,
               2r 2r + 1      2 2r 2 2r + 1
                                                                            (4.43)
                  l    l      1      l    1    l
   E2l−1 =           ,    ∪     +        , +       ,    l = 1, 2, . . ., r.
               2r + 1 2r      2 2r + 1 2 2r
Taking into account that (4.41) is an odd function, we can easily show that this
function is invariant under the transformations (4.24). Hence, relations (4.42) will
be proved if we prove them in the domain 0 ⩽ x, y < 12 . In this domain
                                                                                 
    min ϕr (x, y) = min ϕr (x, y) = min (2r + 1)x + y + (2r + 1)x − y ,
  0⩽y<1/2                0⩽y⩽x                0⩽y⩽x

since
                                                                0         if 0 ⩽ y ⩽ x < 12 ,
          −(2r + 1) x + y − (2r + 1) x − y =
                                                 2r + 1 if 0 ⩽ x < y < 12 .
   To complete the proof of relations (4.42), it remains to calculate the values of
the function (2r + 1)x + y + (2r + 1)x − y in the domain 0 ⩽ y ⩽ x < 12 (see
Fig. 11) using arguments similar to those used in the proof of Lemma 4.3.

        Figure 11. The values of the function ϕr (x, y) in the domain 0 ⩽ y < x < 12
534                                          W. Zudilin

   By (4.30), (4.40) and (4.42), (4.43), we have
            
           2r−1        
   Πn =                              pν
           ν=1
                  √ p:{n/p}∈Eν
                   (2r+2)n<p⩽2n
           2r−1                         r−1                                                          
                                                                     
                                                                         r        
       =                         p   ν
                                                                   p ·
                                                                    2l
                                                                                              p   2l−1
                                                                                                          .
                   √
             ν=1 p:{n/p}∈Eν                  l=1 2r+1 n<p⩽ 2r n
                                                  l+1         l
                                                                         l=1 2r n<p⩽ 2r+1 n
                                                                             l         l
                 p> (2r+2)n
To obtain the limiting relation (4.28), we use Lemma 4.4, the identity
                                       
                                      1
                      ψ(x) + ψ x +        = −2 log 2 + 2ψ(2x)
                                      2
(see formula (4.47) below with r = 2) and the relation
                       1 
                  lim            log p = β − α,     where α < β,
                 n→∞ n
                             αn<p⩽βn

which follows from the prime number theorem (the asymptotic law of distribution
of primes). We have
          l+1 
       r−1                            
                                       l
                                                 
                                                   1       l+1
                                                                         
                                                                            1     l
                                                                                    
 r =        2l ψ                −ψ          +ψ       +              −ψ       +
                      2r + 1          2r           2 2r + 1                 2 2r
       l=1
                              
                2r 2r + 1
         −          −
                 l       l+1
           r                                                                       
                                l             l               1    l            1       l
       +       (2l − 1) ψ           −ψ               +ψ         +         −ψ      +
                               2r          2r + 1             2 2r              2 2r + 1
          l=1
                                 
                   2r + 1 2r
              −             −
                       l        l
         
         r−1                                   r                                  
                           l+1            l                               l              l
     =2        2l ψ                 −ψ          +2        (2l − 1) ψ          −ψ
                         r + 1/2          r                               r          r + 1/2
         l=1                                         l=1
         r−1                         r                             
                    2r 2r + 1                          2r + 1 2r
       −       2l        −           −      (2l − 1)             −
                     l      l+1                             l         l
          l=1                          l=1
                                                                     
           r
                   l
                                                        r
                                                                    l                          
     =2        ψ        (2l − 1 − 2l) + 4rψ(1) + 2         ψ                 2(l − 1) − (2l − 1)
                   r                                            r + 1/2
           l=1                                          l=1
            r
              1                                 
        −       4rl − 2(l − 1)(2r + 1) + (2l − 1) + 4r
              l
          l=1
           r                                 
                                                    r
                    l            l                     1
      = −2      ψ      +ψ                − (4r + 1)      + 4rψ(1) + 4r.
                    r        r + 1/2                   l
            l=1                                                   l=1

Since ψ(1) = −γ (see, for example, [27], § 1.1, formula (8)), we obtain the desired
result, which completes the proof of the lemma.
                           Irrationality of values of the zeta function                  535

Lemma 4.6. The following estimates hold for the quantity deﬁned by (4.28):

                                                                              1
          − log(r + 1) − 4 < r − 4r + (4r + 1)γ < log(r + 1) +                 + 2.   (4.44)
                                                                              r
In particular,
                      r = 4r(1 − γ) + O(log r)              as r → ∞.                 (4.45)

Proof. Since ψ(x) is monotonically increasing on (0, 1], we have

                          
                          r+1                 
                                                r                     
                                                                        r    
                                   l                       l                 l
                −ψ(1) +         ψ             <   ψ                   <   ψ     .      (4.46)
                                  r+1                   r + 1/2              r
                          l=1                  l=1                      l=1

We can calculate the sums in the upper and lower estimates using the formula

                          
                          r         
                                 l−1
                            ψ x+       = −r log r + rψ(rx)                             (4.47)
                                  r
                          l=1

(see, for example, [27], § 1.1, formula (6)).
   Inequality (2.28) implies that the sequence

                                      1 1         1
                                 1+    + + · · · + − log r
                                      2 3         r
decreases and the sequence

                                    1 1         1
                            1+       + + · · · + − log(r + 1)
                                    2 3         r

increases. Therefore, their common limit γ lies between the elements of these
sequences, that is,
                                 
                                 r
                                   1
                         log r <     − γ < log(r + 1).                 (4.48)
                                   l
                                        l=1

  Substituting estimates (4.46)–(4.48) into (4.28), we obtain that

          r+1                                                   r+1
−4r log       − log(r + 1) < r − 4r + (4r + 1)γ < (2r + 1) log     + log(r + 1).
           r                                                     r

Using inequality (2.28) once again, we complete the proof of estimates (4.44). The
limiting relation (4.45) follows immediately from (4.44). The lemma is proved.
Proposition 4.1. The denominator den(In ) of the linear form (1.5) divides
Π−b  a+b−1                                        (r)
  n D2n    , where the sequence of integers Πn = Πn , n = 1, 2, . . . , is deﬁned
in Lemma 4.5. Hence,

           log den(In )            a+b−1
                              log D2n    − b log Πn
          lim           ⩽ lim                       = 2(a + b − 1) − br .
       n→∞      n        n→∞           n
536                                       W. Zudilin

Proof. We prove this proposition by replacing (1.22) in the proof of Lemma 1.4 by
the representation
                           R(t) = Hn (t)a−2rb Gn (t)b ,
applying Lemmas 1.3 and 4.5 to the functions (1.16) and (4.25), and using the
Leibniz rule for the diﬀerentiation of a product.
   To conclude this section we give some particular values of (4.28) (for r = 1
see (4.18)):

        2 ≈ 2.01561,       3 ≈ 3.64442,      10 ≈ 15.38202,         50 ≈ 82.98948,
   100 ≈ 1.67541 · 100,         1000 ≈ 1.68956 · 1000,    r ≈ 4(1 − γ)r ≈ 1.69114 r.

                 § 5. Proof of the results on linear independence
   The following theorem is based on the results obtained in § 2 and § 4.
Theorem 5.1. Let the assumptions of Proposition 2.3 hold, let b be an odd integer,
and let
                        κ + 2(a + b − 1) − br < 0,
where
                r   
                                               
                                                   r
                     l          l                    1
        r = −2    ψ    +ψ              − (4r + 1)     − 4rγ + 4r.
                     r       r + 1/2                 l
                    l=1                                           l=1

Then at least one of the numbers

                            ζ(b + 2), ζ(b + 4), . . . , ζ(a + b − 1)                     (5.1)

is irrational.
Proof. By Lemma 1.1, for any integer n ⩾ 1 the quantity deﬁned by (1.2) is a
linear form in 1 and the numbers (5.1). Assuming that every number in (5.1)
is rational and denoting their least common denominator by D, we obtain that
Jn = D|In | den(In ) is a positive integer for inﬁnitely many n ⩾ 1. This contradicts
the limiting relation
                                log Jn
                          lim          ⩽ κ + 2(a + b − 1) − br < 0,
                      n→∞         n
which follows from Propositions 2.3 and 4.1.
Proof of Theorem 0.1. We use Theorem 5.1 with suitable a, b and r = 1 for each
set of numbers. Note that µ1 < 3.05 in each of the cases considered below. Hence,
assumption (2.61) holds.
   We prove that at least one of the elements of the ﬁrst set in (0.1) is irra-
tional by putting a = 19 and b = 3 in Theorem 5.1. In this case µ1 ≈ 3.04028,
τ0 ≈ 2.98027 + 0.02985i, and Im f0 (τ0 ) + 3π ≈ 0.09308 ≡ 0 (mod πZ). Combining
the estimate
                     κ + 2(a + b − 1) − br ≈ −0.72567 < 0
with Theorem 5.1, we complete the proof of the assertion for the ﬁrst set in (0.1).
                         Irrationality of values of the zeta function                     537

  For the second we put a = 33 and b = 5. Then

    µ1 ≈ 3.03309,       τ0 ≈ 3.00783 + 0.03046i,            Im f0 (τ0 ) + 9π ≈ 0.14978,
                      κ + 2(a + b − 1) − br ≈ −0.76662 < 0.

  Finally, putting a = 47 and b = 7 for the third, we obtain

    µ1 ≈ 3.03043,       τ0 ≈ 3.01730 + 0.02406i,           Im f0 (τ0 ) + 15π ≈ 0.16232,
                      κ + 2(a + b − 1) − br ≈ −0.82928 < 0.

  The theorem is proved.
Proof of Theorem 0.2. We put a = 7b and r = 1 for every odd integer b ⩾ 3
and denote by τb the root of the corresponding polynomial (2.21) in the domain
Re τ > 0, Im τ > 0 with the maximal possible Re τb . Note that the root of poly-
nomial (2.21) in the interval (3, +∞) coincides with the root of the polynomial

                          (τ + 3)(τ − 1)8 − (τ − 3)(τ + 1)8 ,

which is equal to µ1 ≈ 3.02472. Since (2.61) holds, Lemma 2.10 implies that
Re f0 (τb ) ⩽ Re f0 (µ1 ), whence

                                 22(a−2)(µ1 + 3)3 (µ1 − 3)3
              κ ⩽ bκ0 := b log                              ≈ −15.56497 b.
                                     (µ1 + 1)8 (µ1 − 1)8

Therefore,

             κ + 2(a + b − 1) − br < bκ0 + 16b − b1 ≈ −0.04701 b < 0.

We shall be able to use Theorem 5.1 if we can show that (2.55) holds. It is easy to
verify that

g0 (b) = Im f0 (τb ) + 3(b − 2)π
                                                                  
       = 3b arg(τb − 3) + arg(−τb + 3) − 8b arg(τb − 1) + arg(τb + 1) + 3(b − 2)π
                                                         
       = 2b 3 arg(τb − 3) + 8 arg(τb − 1) − 16 arg(τb + 1) ,

regarded as a function of b ⩾ 3, increases, whence g0 (b) ⩾ g0 (3) ≈ 0.05935 > 0.
The relations

                       b−2
      arg(−τb + 3) ∼       π,      |−τb + 3| ∼ |µ1 − 3|          as b → ∞, b is odd,
                        b

enable us to calculate the limit

                                      lim g0 (b) < π.
                                     b→∞
                                    b is odd
538                                   W. Zudilin

Therefore, Im f0 (τb ) ≡ 0 (mod πZ). An application of Theorem 5.1 completes the
proof.
Proof of Theorem 0.3. By Lemma 1.1 and Proposition 4.1 with b = 1, the I˜n (a, r) =
    a    (r)
In D2n /Πn deﬁned by (1.2) are linear forms in 1, ζ(3), ζ(5), . . . , ζ(a) with integer
coeﬃcients. By Propositions 2.1, 3.1, and 4.1 the α, β in the criterion for linear
independence (see the introduction) are deﬁned by the formulae

                            α(a, r) = −κ(a, r) − 2a + r ,
                                                                                 (5.2)
            β(a, r) = 2(2r + 1) log(2r + 1) + 2(a − 2r) log 2 + 2a − r ,

where κ = κ(a, r) is deﬁned by (2.59). For a = 145, r = 10 and a = 1971, r = 65
we have

                                                        α(145, 10)
         µ1 (145, 10) − 21 ≈ 0.38013 · 10−4 ,        1+            ≈ 2.000397,
                                                        β(145, 10)
                                                       α(1971, 65)
      µ1 (1971, 65) − 131 ≈ 0.22019 · 10−10,        1+             ≈ 3.000103,
                                                       β(1971, 65)

where µ1 (a, r) is the real root of polynomial (2.21) with b = 1 in the interval
(2r + 1, +∞). The criterion for linear independence implies that

                            δ(145) ⩾ 3,         δ(1971) ⩾ 4,                     (5.3)

since the dimension of space is an integer. By Apéry’s theorem, δ(3) = 2. The
assertion of the theorem follows from the estimates obtained.
Lemma 5.1. Assume that the positive integers a, r are such that

                             a > 2(r + 2) log(r + 1) + 1,                        (5.4)

and let µ1 = µ1 (a, r) be a real root of the polynomial

              h(τ ) = (τ + 2r + 1)(τ − 1)a+1 − (τ − 2r − 1)(τ + 1)a+1            (5.5)

in the interval (2r + 1, +∞). Then

                                                                2r + 1
              0 < µ1 − (2r + 1) < 2ε,       where ε :=                  < 1.     (5.6)
                                                               (r + 1)2

Proof. Direct calculations show that

                        h(2r + 1) = 2a+2 (r + 1)ra+1 > 0,                        (5.7)
                                                                      
         h(2r + 1 + 2ε) = 2a+2 (2r + 1 + ε)(r + ε)a+1 − ε(r + 1 + ε)a+1 .        (5.8)

Inequality (5.4) implies that

                            (r + 1 + ε)a−1 > (r + ε)a+1 ,                        (5.9)
                          Irrationality of values of the zeta function            539

since

           (a − 1) log(r + 1 + ε) − (a + 1) log(r + ε)
                                         
                                      1
                = (a − 1) log 1 +           − 2 log(r + ε)
                                    r+ε
                                         
                                      1
                > (a − 1) log 1 +           − 2 log(r + 1)
                                    r+1
                    a−1                     a − 1 − 2(r + 2) log(r + 1)
                >         − 2 log(r + 1) =                              > 0.
                    r+2                                r+2

Besides,

                  (2r + 1)(r + 1 + ε)2
  ε(r + 1 + ε)2 =
                        (r + 1)2
                  (2r + 1)(r + 1 + ε)2   ε(3r2 + 4r + 1 + 2εr + ε)
                >              2
                                       −                           = 2r + 1 + ε.
                        (r + 1)                   (r + 1)2
                                                                            (5.10)

Substituting inequalities (5.9) and (5.10) into (5.8), we obtain that h(2r+1+2ε) < 0.
Combining this inequality with (5.7), we obtain that the interval (2r +1, 2r +1+2ε)
contains at least one root of the polynomial (5.5). Now (5.6) follows from the fact
that µ1 is the unique real root in the interval (2r + 1, +∞) (Lemma 2.7). The
lemma is proved.
Corollary 5.1. Let the assumptions of Lemma 5.1 hold with r > 6. Then the
following estimate holds for κ = κ(a, r) in (2.59):

                κ(a, r) < 2(2r + 1) log(2r + 1) − 2(a + 1)(1 + log r).

Proof. Since h(µ1 ) = 0, we have

                          22(a−2r)(µ1 + 2r + 1)2(2r+1)(µ1 − 1)2(a+1)r
                κ = log                                               .
                                      (µ1 + 1)2(a+1)(r+1)

Combining this with (5.6), we obtain that

κ
  − (a − 2r) log 2
2                                                        
                         2r                             2
   = (2r + 1) log 1 +           − (a + 1)r log 1 +             − (a − 2r) log(µ1 + 1)
                       µ1 + 1                        µ1 − 1
                            
                         r       (a + 1)r
   < (2r + 1) log 1 +          −          − (a − 2r) log(2r + 2)
                       r+1         r+1
                                                        
                                       r
   = (2r + 1) log(2r + 1) − (a + 1)        + log(r + 1) − (a − 2r) log 2
                                     r+1
   < (2r + 1) log(2r + 1) − (a + 1)(1 + log r) − (a − 2r) log 2.
540                                      W. Zudilin

Here we have used the inequality
                                                       
                   2                1                   1        1
       log 1 +           > log 1 +       > 2 log 1 +          >
                µ1 − 1             r+ε               2r + 1     r+1
(see also (2.28) with n = 2r + 1), which holds for r > 6 since
                                           2
                        1               1         r − 4εr − 3r + 1
                  1+        − 1+               =
                      r+ε            2r + 1       (r + ε)(2r + 1)2
                             r − 5r − 7r − 2
                              3      2
                       =                            >0      if r > 6.
                          (r + ε)(r + 1)2 (2r + 1)2
The corollary is proved.
Proof of Theorem 0.4. Since δ(a) is an integer and
 0.395 · log 3 ≈ 0.43395,      0.395 · log 145 ≈ 1.96581,       0.395 · log 1971 ≈ 2.99659,
Apéry’s theorem and estimates (5.3) imply that inequality (0.2) holds for all odd
integers a < e4/0.395, that is, a < 24999. In fact we shall show that the following
estimate holds for odd integers a ⩾ 20737 = 124 + 1, which is stronger than (0.2):
                                                 log a
                                       δ(a) >          ,                              (5.11)
                                                log 12
or, which is the same,
                           δ(12m + 1) > m,         m = 4, 5, 6, . . . .               (5.12)
For every a = 12m + 1 we put
                 2                m     
                 log 12     a       12 + 1
            r=          ·         =         ,                   m = 4, 5, 6, . . .,
                    3     log2 a      3m2
and obtain a lower estimate for δ(a) using the criterion for linear independence,
formulae (5.2), and the inequalities in Lemma 4.6 and Corollary 5.1:
               α(a, r)
δ(a) ⩾ 1 +
               β(a, r)
                               2(a + 1)(1 + log r) + 2(a − 2r) log 2
      >                                                                                 .
          2(2r + 1) log(2r + 1) + 2(a − 2r) log 2 + 2a − 4r(1 − γ) + log(r + 1) + 4 + γ
                                                                                   (5.13)

Now for m = 4, 5, 6, 7 estimate (5.12) follows immediately from (5.13):
                                                   
                             m                   a
           m           a = 12 + 1          r=                 δ(a)
                                                3m2
                  4           20737                 432               > 4.00882
                  5          248833                3317               > 5.15339
                  6          2985985              27648               > 6.35168
                  7         35831809              243753              > 7.58967
                            Irrationality of values of the zeta function                       541

   For the remaining values of m we combine (5.13) with the trivial estimates

                        r      1        2r + 1     2     1         2
                  0<      ⩽       ,            ⩽       + ⩽ 2           ,
                        a    3m2           a     3m2     a    m log 12
                                   12m
                      log r ⩾ log      = m log 12 − 2 log 2 − 2 log m,
                                   4m2
                            log(2r + 1) ⩽ log(a − 1) = m log 12.

We have

                        m log 12 − 2 log m + 1 − log 2 − 1/(3m2 )   m log 12 − 2 log m
δ(a) = δ(12m+1) >                                                 >                    .
                                     1 + log 2 + 2/m                 1 + log 2 + 2/m

Now (5.12) with m ⩾ 8 follows from the fact that the function
                                              
                                             2
 ∆(m) = (m log 12 − 2 log m) − m 1 + log 2 +     = m(log 6 − 1) − 2 log m − 2
                                             m

increases monotonically and takes a positive value, ∆(8) ≈ 0.17519, at m = 8. This
completes the proof of the theorem.
   In fact we have proved estimate (5.11) for odd integers a ⩾ 3 with the exception
of ﬁnitely many values in the range 123 + 1 = 1729 ⩽ a ⩽ 1969.

                                        Bibliography
 [1] R. Apéry, “Irrationalité de ζ(2) et ζ(3)”, Astérisque 61 (1979), 11–13.
 [2] A. van der Poorten, “A proof that Euler missed... Apéry’s proof of the irrationality of ζ(3).
     An informal report”, Math. Intelligencer 1:4 (1978/79), 195–203.
 [3] F. Beukers, “A note on the irrationality of ζ(2) and ζ(3)”, Bull. London Math. Soc. 11
     (1979), 268–272.
 [4] L.A. Gutnik, “The irrationality of certain quantities involving ζ(3)”, Uspekhi Mat. Nauk
     34:3 (1979), 190; English transl., Russian Math. Surveys 34:3 (1979), 200; Acta Arith.
     42:3 (1983), 255–264.
 [5] F. Beukers, “Padé approximations in number theory”, Lecture Notes in Math., vol. 888,
     Springer-Verlag, Berlin 1981, pp. 90–99.
 [6] F. Beukers, “Irrationality proofs using modular forms”, Astérisque 147–148 (1987),
     271–283.
 [7] V. N. Sorokin, “Hermite–Padé approximations of Nikishin systems and the irrationality
     of ζ(3)”, Uspekhi Mat. Nauk 49:2 (1994), 167–168; English transl., Russian Math. Surveys
     49:2 (1994), 176–177.
 [8] Yu. V. Nesterenko, “A few remarks on ζ(3)”, Mat. Zametki 59 (1996), 865–880; English
     transl., Math. Notes 59 (1996), 625–636.
 [9] M. Hata, “A new irrationality measure for ζ(3)”, Acta Arith. 92:1 (2000), 47–57.
[10] G. Rhin and C. Viola, “The group structure for ζ(3)”, Acta Arith. 97:3 (2001), 269–293.
[11] D. V. Vasilyev, “On small linear forms for the values of the Riemann zeta-function at odd
     points”, Preprint no.1 (558), Inst. Math., Nat. Acad. Sci. Belarus, Minsk 2001.
[12] K. Ball, Diophantine approximation of hypergeometric numbers, Manuscript, 2000.
[13] T. Rivoal, “La fonction zêta de Riemann prend une inﬁnité de valeurs irrationnelles aux
     entiers impairs”, C. R. Acad. Sci. Paris Sér. I Math. 331:4 (2000), 267–270; http://
     arXiv.org/abs/math/0008051.
[14] T. Rivoal, Propriétés diophantiennes des valeurs de la fonction zêta de Riemann aux entiers
     impairs, Thèse de Doctorat, Univ. de Caen, Caen 2001.
542                                         W. Zudilin

[15] K. Ball and T. Rivoal, “Irrationalité d’une inﬁnité de valeurs de la fonction zêta aux entiers
     impairs”, Invent. Math. 146:1 (2001), 193–207.
[16] Yu. V. Nesterenko, “On the linear independence of numbers”, Vestnik Moskov. Univ. Ser. 1
     Mat. Mekh. 1985, no. 1, 46–54; English transl., Moscow Univ. Math. Bull. 40:1 (1985),
     69–74.
[17] T. G. Hessami Pilehrood, Arithmetical properties of values of hypergeometric functions,
     Diss. Cand. Phys.-Math. Sci., Mosk. Gos. Univ., Moscow 1999; “Linear independence of
     vectors with polylogarithmic coordinates”, Vestnik Moskov. Univ. Ser. 1 Mat. Mekh. 1999,
     no. 6, 54–56; English transl., Moscow Univ. Math. Bull. 54:6 (1999), 40–42
[18] E. A. Rukhadze, “A lower estimate for rational approximations of ln 2”, Vestnik Moskov.
     Univ. Ser. 1 Mat. Mekh. 1987, no. 6, 25–29; English transl., Moscow Univ. Math. Bull.
     42:6 (1987), 30–35.
[19] V. V. Zudilin, “On the irrationality of the values of the zeta function at odd integer
     points”, Uspekhi Mat. Nauk 56:2 (2001), 215–216; English transl., Russian Math. Surveys
     56 (2001), 423–424.
[20] E. M. Nikishin, “On the irrationality of the values of the functions F (x, s)”, Mat. Sbornik
     109 (1979), 410–417; English transl., Math. USSR-Sb. 37 (1980), 381–388.
[21] Yu. V. Nesterenko, “Diophantine approximations to Riemann’s zeta function”, Report on
     the Workshop on Number Theory (4 October, 2000), Mosk. Gos. Univ., Moscow 2000.
[22] S. Lang, Introduction to modular forms, Grundlehren Math. Wiss., vol. 222, Springer-Verlag,
     Berlin 1976; Russian transl., Mir, Moscow 1979.
[23] N. G. de Bruijn, Asymptotic methods in analysis, North-Holland, Amsterdam 1958; Russian
     transl., Inostr. Lit., Moscow 1961.
[24] M. Yoshida, Hypergeometric function, my love, Aspects of Math., vol. E 32, Vieweg,
     Wiesbaden 1997.
[25] G. V. Chudnovsky, “On the method of Thue–Siegel”, Ann. of Math. (2) 117 (1983),
     325–382.
[26] M. Hata, “Legendre type polynomials and irrationality measures”, J. Reine Angew. Math.
     407:1 (1990), 99–125.
[27] Yu. L. Luke, Mathematical functions and their approximations, Academic Press, New York
     1975; Russian transl., Mir, Moscow 1980.
[28] V. V. Zudilin, “One of the numbers ζ(5), ζ(7), ζ(9), ζ(11) is irrational”, Uspekhi Mat. Nauk
     56:4 (2001), 149–150; English transl., Russian Math. Surveys 56 (2001), 774–776.

Moscow State University,
Moscow 117234, Russia
E-mail address: wadim@ips.ras.ru
                                                                            Received 24/APR/01
                                                       Translated by V. M. MILLIONSHCHIKOV

                                                                              Typeset by AMS-TEX
