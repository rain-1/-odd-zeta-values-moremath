---
title: "zudilin-2011-arithmetic-hypergeometric-series-survey"
source: "books-and-surveys/zudilin-2011-arithmetic-hypergeometric-series-survey.pdf"
conversion: pdftotext -layout
note: "extracted text; formulas are flattened and may be lossy — check the PDF for anything load-bearing"
---

Russian Math. Surveys 66:2 1–51                               c 2011 RAS(DoM) and LMS
                                                              °
Uspekhi Mat. Nauk 66:2 163–216                   DOI 10.1070/RM2011v066n02ABEH000000

                                 To the blessed memory of Anatolii Alekseevich Karatsuba

                    Arithmetic hypergeometric series

                                       W. Zudilin

       Abstract. The main goal of our survey is to give common characteristics
       of auxiliary hypergeometric functions (and their generalisations), functions
       which occur in number-theoretical problems. Originally designed as a tool
       for solving these problems, the hypergeometric series have become a con-
       necting link between different areas of number theory and mathematics in
       general.
          Bibliography: 183 titles.

       Keywords: hypergeometric series; zeta value; diophantine approxima-
       tion; irrationality measure; modular form; Ramanujan’s mathematics; Cal-
       abi–Yau differential equation; Mahler measure; Wilf–Zeilberger theory;
       algorithm of creative telescoping.

                                       Contents

Introduction                                                                           2
1. Arithmetic of the values of Riemann’s zeta function                                 6
    1.1. Apéry’s theorem                                                              6
    1.2. Hypergeometric series and multiple integrals                                 11
    1.3. Simultaneous approximations to ζ(2) and ζ(3)                                 15
    1.4. q-Analogues of zeta values                                                   18
    1.5. Lower bound for k(3/2)k k and Waring’s problem                               21
2. Calabi–Yau differential equations                                                  22
    2.1. Arithmetic differential equations of order 2 and 3                           22
    2.2. Arithmetic differential equations of order 4 and 5                           24
    2.3. The family of Calabi–Yau quintics                                            26
    2.4. Sp4 modularity                                                               29
    2.5. Ramanujan-type formulae for 1/π 2                                            32
3. Lattice sums and Mahler measures                                                   35
    3.1. Dirichlet L-series and Mahler measures                                       35
    3.2. Quadruple lattice sums                                                       38
Bibliography                                                                          42

   Work is supported by Australian Research Council grant DP110104419.
   AMS 2010 Mathematics Subject Classification. Primary 33C20; Secondary 05A19, 11B65,
11F11, 11J82, 11M06, 11Y60, 14H52, 14J32, 33C75, 33F10, 34M50, 40G99, 65B10, 65Q05.
2                                      W. Zudilin

                                     Introduction
   Arithmetic, known nowadays more usually as number theory, is the heart and
one of the oldest parts of mathematics. Carl Friedrich Gauss, arguably the greatest
mathematician of all the time, called mathematics the ‘Queen of science’ and he
referred to Number Theory as the ‘Queen of mathematics’. Number theory is
famous for having many problems which any school student can understand but
whose solutions require deep methods of modern mathematics. A famous example
is Fermat’s Last Theorem about the insolvability of the equation xn + y n = z n
in positive integers with n > 2, which was not actually proved by Fermat himself
but quite recently by Andrew Wiles. Another example, which remains an open
problem, is the Riemann Hypothesis about the zeros of the function
                                              ∞
                                              X 1
                                    ζ(s) :=              .
                                              n=1
                                                    ns

It is a well-accepted fact that the central problems of number theory are very hard
and as such require methods from many different branches of mathematics; the
development of these methods is highly influential on mathematics in general.
   Among the important tools for solving problems in number theory are the
so-called special functions, whose origin and ultimate importance in mathemati-
cal physics was, for a long time, the main reason for their development. Special
functions usually appear in exactly solvable problems of physical origin [10], but
remarkably they are of definite value in number theory as well. All classical math-
ematical constants [55] such as e, π, values of the logarithms, generalized polylog-
arithmic functions, zeta values ζ(s) at integers s > 1, come as special values of
certain special functions (not necessarily uniquely chosen).
   An important subclass of special functions is the hypergeometric functions [13],
[61], [130] defined by the series
                   µ                       ¯ ¶    ∞
                     a1 , a2 , . . . , am ¯¯     X   (a1 )n (a2 )n · · · (am )n z n
            m Fm−1                           z =                                    , (1)
                          b 2 , . . . , bm ¯            (b2 )n · · · (bm )n     n!
                                                 n=0

in the unit disc |z| < 1, and analytically continued to the whole C-plane with cut
along the ray [1, +∞). Here
                                  (
                      Γ(a + n)      a(a + 1) · · · (a + n − 1) if n ⩾ 1,
              (a)n =           =
                        Γ(a)        1                          if n = 0,

denotes the Pochhammer symbol (or rising factorial). The m Fm−1 function in (1)
satisfies the linear differential equation
                µ Y m                   Ym           ¶
                                                                d
                 θ     (θ + bj − 1) − z     (θ + aj ) y = 0, θ=z ,          (2)
                   j=2                  j=1
                                                                dz

of order m, which is an example of Picard–Fuchs differential equation [152]. The
theory of hypergeometric functions allows for the unification of many recent achieve-
ments in number theory including, for example, Apéry’s mysterious proof of the
irrationality of ζ(3) [106] and Ramanujan’s rapidly convergent series for π [30].
                            Arithmetic hypergeometric series                          3

   It is not surprising to see that number theory in fact requires only a certain
subclass of hypergeometric functions, the functions which meet several arithmetic
requirements; for example, the parameters of (1) have to be rational or algebraic
numbers. It is these functions which we refer to as arithmetic hypergeometric series.
The idea to formalise such arithmetic conditions was born on the border of physical
String Theory and mathematical Algebraic Geometry. The so-called ‘mirror sym-
metry’ produces a natural duality between certain geometric objects; on one side
of this duality we have Calabi–Yau manifolds whose periods satisfy certain special
Picard–Fuchs differential equations, and the arithmetic data encoded in these equa-
tions (as expected) gives one a way to reconstruct the dual side. The joint paper [6]
of G. Almkvist and this author is one of the first attempts to put the theory of such
Calabi–Yau differential equations on the market of number theory. Further devel-
opment of this subject along with its linking to other problems in number theory
[154], [181], algebraic geometry [4], mathematical physics [73], and other parts of
mathematical science, is of great importance in contemporary mathematics.
   The modest goal of this survey is to demonstrate how the arithmetic hypergeo-
metric series link certain seemingly unrelated to each other research subjects as well
as to explain the underlying arithmetic and analytical techniques. More specifically,
we address the following directions:
   (1) arithmetic properties of the values of Riemann’s zeta function function ζ(s)
        at integers s > 1 and their generalisations;
   (2) arithmetic significance of Calabi–Yau differential equations and generalised
        Ramanujan-type series for π; and
   (3) hypergeometric and special-function evaluations of Mahler measures.
   Section 1 discusses the arithmetic properties of the values of Riemann’s zeta func-
tion. The arithmetic nature of ζ(s) at integers s = 2, 3, 4, . . . (zeta values) is well
understood for even s, thanks to Euler’s evaluation of ζ(2k) yielding ζ(2k)/π 2k ∈ Q
and Lindemann’s 1881 proof of the transcendence of π. For odd s, we have results
only for irrationality (and not transcendence, even though the numbers are all
conjecturally transcendental). After Apéry’s unanticipated 1978 proof of the irra-
tionality of ζ(3), quite recent results of K. Ball and T. Rivoal [15] and of the
author [163], [173] show that there are infinitely many irrational numbers in the set
ζ(3), ζ(5), ζ(7), . . . and much more. For example, we now know that each set

                     ζ(s + 2), ζ(s + 4), . . . , ζ(8s − 3), ζ(8s − 1)

with odd s > 1 contains at least one irrational number, as well as at least one of
the four numbers ζ(5), ζ(7), ζ(9), ζ(11) is irrational. The hypergeometric techniques
used in the proofs allows one to get similar results for the values of other Dirichlet’s
series [119], for q-analogues of zeta values [84], [172] and, more generally, for the
values of many other classical q-series [37], [39], [97].
   It is Section 2 where we give a formal definition of Calabi–Yau differential equa-
tions and overview their monodromy properties. The huge database of such equa-
tions is now tabulated in [3], and one of the problems in the subject is to understand
the relations between different examples of such special equations and their solu-
tions, which are manifestly arithmetic hypergeometric series, by means of algebraic
transformations. An example of such transformations extracted from the recent
4                                                     W. Zudilin

work [5] is as follows. If we define two double hypergeometric series,
                                        ∞
                                        X             µX
                                                       n          µ ¶ 1 2 ¶2
                                                  n                n ( 2 )k
                                                                   k
                              F (z) =         z              (−1)
                                        n=0
                                                                   k k!2
                                                       k=0

and                                                            µ ¶ 1
                                ∞
                                X         1      3    Xn                   3
                                      n ( 4 )n ( 4 )n         k n ( 4 )k ( 4 )k
                    Fb(z) =         z                     (−1)                  ,
                                n=0
                                             n!2                k      k!2
                                                      k=0

then                                              µ                  ¶
                                       1        b    −16z(1 − z)2
                         F (z) = √              F                     .                          (3)
                                   1 − 6z + z 2     (1 − 6z + z 2 )2
   In Section 2 we also discuss generalised Ramanujan formulae for π. Proofs of
the classical Ramanujan formulae for 1/π, such as [111]
                                              ∞
                                              X ( 1 )3n  2             1  4
                                                              (6n + 1) n = ,                     (4)
                                              n=0
                                                        n!3           4   π
                   ∞                                                √
                   X ( 1 )n ( 1 )n ( 5 )n                  (−1)n 640 15
                          2      6      6
                                              (5418n + 263) 3n =        ,                        (5)
                   n=0
                                 n!3                        80     3π

are now uniform thanks to the modular and hypergeometric machinery [30], [16],
[181]. A similar formula, namely,
       ∞
       X ( 1 )n ( 1 )n ( 5 )n
             6     2     6                                                 (−1)n          3
                                (545140134n + 13591409) ·                           =   √        (6)
       n=0
                  n!3                                                    53360 3n+2
                                                                                      2π 10005

due to the Chudnovskys [43], was used by Bellard in December 2009 to compute a
record 2.7 trillion digits of π — on a single workstation. Such series were discovered
by Ramanujan in 1914 but the first complete proofs were obtained only in the 1980s
[30]. However, extensions of these formulae (with five Pochhammer symbols in the
numerator and n!5 in the denominator) were only recently discovered by J. Guillera
[65]–[68] and by G. Almkvist and J. Guillera [2]. There are eleven known formulae of
this kind of which only four are proved rigorously (using hypergeometric algorithms)
while seven, such as
           ∞                                                                         √
          X   ( 12 )n ( 13 )n ( 32 )n ( 16 )n ( 56 )n                    (−1)n ? 128 5
                                                            2
                                   5
                                                      (5418n + 693n + 29) 3n =       2
                                                                                       (7)
          n=0
                               n!                                         80       π

and
                         ∞
                         X (6n)!                                        1 ? 375
                                        (532n2 + 126n + 9)                  =      ,             (8)
                         n=0
                                 n!6                                   106n   4π 2

remain beyond reach of the current methods. It is important to understand the
structure of such formulae and to develop techniques for proving them. The corre-
sponding hypergeometric differential equations are special cases of the Calabi–Yau
differential equations.
                                  Arithmetic hypergeometric series                                     5

   Section 3 deals with special Mahler measures. The (logarithmic) Mahler measure
of a Laurent polynomial

                             P (x1 , . . . , xn ) ∈ C[x±1           ±1
                                                       1 , . . . , xn ]

is defined by
                        Z         Z
             m(P ) :=       ···                log |P (e2πiθ1 , . . . , e2πiθn )| dθ1 · · · dθn .    (9)
                                      [0,1]n

The measure first introduced by Hermite 150 years ago and studied carefully by
Mahler in the 1960s is crucial to understanding the fine structure of the zeros
of integer polynomials and so of transcendence. In 1998 D. W. Boyd — with a
very large amount of computation — conjectured [34] a number of striking and
unexpected relations between the Dirichlet L-series (that is, generalised zeta values)
of elliptic curves and the Mahler measures of polynomials with zero varieties that
correspond to the same elliptic curves.
   The first result in this direction was derived by C. Deninger [47] from the Beilin-
son conjectures; he showed that, up to a rational multiple r,
                                                                               15
                m(1 + x + x−1 + y + y −1 ) = rL0 (E, 0) = r                        L(E, 2),
                                                                              4π 2
where E is an elliptic curve of conductor 15. Numerically [34], the multiple seems
to be equal to 1, and by appealing to the modularity theorem for elliptic curves we
can write the expected equality as

 m(1 + x + x−1 + y + y −1 )
             ∞
     540 X                       (−1)n1 +n2 +n3 +n4
   = 2           ¡                                                 ¢ . (10)
      π n =−∞ (6n1 + 1)2 + 3(6n2 + 1)2 + 5(6n3 + 1)2 + 15(6n4 + 1)2 2
           i
           i=1,2,3,4

K-theory serves as a natural machinery for attacking Boyd’s conjectures [120], [121],
[36], [98], but major progress in this direction is due to combining the approach
with modular-function techniques. This was developed by F. Rodrı́guez-Villegas
and later by M. J. Bertin, D. W. Boyd and others [20], [35], [120]. The requirement
of modularity is however very restrictive. It turns out that the majority of Boyd’s
conjectures can be rephrased as identities for hypergeometric series. This approach
was used by M. Lalı́n and M. D. Rogers [87], [123] to derive several new identities
for the Mahler measures. For example, the hypergeometric evaluation [123]
                                                               ∞ µ
                                                               X    ¶2
                               −1                   −1            2n (1/16)2n+1
                m(1 + x + x            +y+y              )=4                                        (11)
                                                               n=0
                                                                       n         2n + 1

reduces the evaluation (10) to verifying that the quadruple sum is the value of the
hypergeometric series on the right-hand side of (11). Introducing hypergeometric
techniques is a key to a rigorous proof of (10) in [125] and also to some other
longstanding conjectures from Boyd’s list [124].
6                                               W. Zudilin

    The consequence of (10) and (11),
             ∞
       540 X                        (−1)n1 +n2 +n3 +n4
                 ¡                                                    ¢
       π 2 n =−∞ (6n1 + 1)2 + 3(6n2 + 1)2 + 5(6n3 + 1)2 + 15(6n4 + 1)2 2
             i
           i=1,2,3,4
              X∞ µ          ¶2
                       2n        (1/16)2n+1
          =4                                ,                                      (12)
                 n=0
                        n          2n + 1

is a deep analytic result, because it relates a complicated lattice sum to a simple 3 F2
hypergeometric function. Lattice sums have been extensively studied in physics,
where they often arise when calculating electrostatic potentials of crystal lattices
(for instance, see [30], [59], [63] and [159]). It cannot be coincidental that the
evaluation (12) bears a striking resemblance to a famous formula for Catalan’s
constant discovered by Ramanujan [55]:
                          ∞                  ∞ µ     ¶2
                      1 X (−1)n             X     2n (1/4)2n+1
                                         =                        .                (13)
                      π n=0 (2n + 1)2       n=0
                                                   n    2n + 1

Catalan’s constant is one of the simplest arithmetic quantities whose irrationality
is still unproven. This fact that the right-hand sides of (12) and (13) are arithmetic
values of the same hypergeometric function makes us confident in claiming that
many Mahler measure identities can be proved by the arithmetic hypergeometric
techniques. It serves perfectly to illustrate the need for a better understanding of
such sometimes rigorous and sometimes experimental evaluations.
   For many years, Anatolii Alekseevich Karatsuba was expressing his interest in my
arithmetic-hypergeometric research. This was much more than a moral support,
because in 2006–2008 I worked under his leadership in the Division of Number
Theory at the Steklov Institute of Mathematics. His sudden death is a big loss for
number theory and mathematics, but it is at the same time my personal loss of a
teacher and friend. This survey is my tribute to Anatolii Alekseevich.
   My personal enjoyment of arithmetic hypergeometric series and my knowledge on
the subject would be not possible without my colleagues, collaborators and friends.
I use this opportunity to express my gratitude to G. Almkvist, A. Aptekarev,
D. Bertrand, J. Borwein, P. Bundschuh, H. H. Chan, V. Golyshev, S. Fischler,
J. Guillera, M. Huttner, C. Krattenthaler, L. Long, T. Matalo-aho, A. Mellit,
Yu. Nesterenko, Y. Ohno, G. Rhin, T. Rivoal, I. Rochev, M. Rogers, V. Sorokin,
V. Spiridonov, A. Straub, K. Väänänen, W. Van Assche, D. van Straten, C. Viola,
M. Waldschmidt, J. Wan, O. Warnaar, Y. Yang, D. Zagier, and D. Zeilberger.

          1. Arithmetic of the values of Riemann’s zeta function
1.1. Apéry’s theorem. Investigation of sums of the form
                                                     ∞
                                                     X 1
                                           ζ(s) =                                  (14)
                                                     n=1
                                                           ns

for positive integers s goes back to L. Euler [53], [54]. In particular, he proved the
divergence of the series in (14) when s = 1 and its convergence when s > 1, as well
                               Arithmetic hypergeometric series                       7

as his famous formulae
                     X∞
                          1      (2πi)2k B2k
                 2           = −                    for k = 1, 2, 3, . . . .       (15)
                     n=1
                         n2k        (2k)!

The latter relate the values of the series at positive even s to the Archimedean
constant π = 3.14159265 . . . (see [55; § 1.4]) and the Bernoulli numbers Bs ∈ Q,
which can be defined by means of the generating function
                                ∞                   ∞
                   z         z X zs             z X         z 2k
                       = 1 −  +    B s    = 1 −   +   B 2k       .
                ez − 1       2 s=2     s!       2          (2k)!
                                                             k=1

In 1882 F. Lindemann [90] established the transcendence of π, thus, the transcen-
dence of ζ(s) for s even.
   It was only one century after Euler, when B. Riemann [115] considered the series
in (14) as a function of complex variable s. In the domain Re s > 1, the series
represents an analytical function which can be continued to the whole complex
plane to the meromorphic function ζ(s). It is this analytical continuation, as well
as some other important properties of the function ζ(s), which were discovered
by Riemann in his memoir on prime numbers. Riemann’s zeta function and its
generalisations play a fundamental role in analytic number theory [145]. In what
follows we only discuss arithmetic and analytical properties of the Euler sums ζ(s)
in (14) for positive integers s > 1, and their generalisations. For brevity, we will
call the quantities (14) zeta values, and also even and odd zeta values depending
on the parity of positive integer s.
   As noted above, the transcendence (hence the irrationality) of the even zeta
values follow from the classical results of Euler and Lindemann. Similar to (15)
formulae for odd zeta values are not known and, presumably, the number ζ(2k +
1)/π 2k+1 is not rational for any integer k ⩾ 1. The arithmetic nature of odd zeta
values seemed to be impregnable till 1978 when R. Apéry produced a sequence of
rational approximations which showed the irrationality of ζ(3).
   History of this discovery as well as a rigorous mathematical justification of
Apéry’s claims are exposed in [106]. Number ζ(3) is known nowadays as the Apéry
constant (see, for example, [55; § 1.6]). The rational approximations to ζ(3) given
by Apéry have the form vn /un ∈ Q for n = 0, 1, 2, . . . , where the denominators
{un } = {un }n=0,1,... as well as the numerators {vn } = {vn }n=0,1,... satisfy the same
polynomial recursion

             (n + 1)3 un+1 − (2n + 1)(17n2 + 17n + 5)un + n3 un−1 = 0              (16)

with the initial data

                     u0 = 1,   u1 = 5,       and      v0 = 0,      v1 = 6.         (17)

Then
                                         vn
                                      lim   = ζ(3),                                (18)
                                     n→∞ un
8                                      W. Zudilin

nonetheless an important but unexpected (from the recursion (16) point of view)
circumstance is the inclusions
               X n µ ¶2 µ      ¶2
                     n     n+k
         un =                     ∈ Z, Dn3 vn ∈ Z,    n = 0, 1, 2, . . . , (19)
                     k       k
                k=0

where Dn denotes the least common multiple of 1, 2, . . . , n (and D0 = 1 for com-
pleteness). Application of Poincaré’s theorem (see, for example, [62]) to the differ-
ence equation (16) leads one to the limiting relations
                                                   √
                         lim |un ζ(3) − vn |1/n = ( 2 − 1)4 ,                    (20)
                        n→∞
                                                      √
                      lim |un |1/n = lim |vn |1/n = ( 2 + 1)4                    (21)
                      n→∞              n→∞
                                          √              √
in accordance with (18); here numbers ( 2 − 1)4 and ( 2 + 1)4 are roots of the
characteristic polynomial λ2 − 34λ + 1 of the recursion (16). The information
gathered about the properties of the sequences {un } and {vn } demonstrates that
number ζ(3) cannot be rational. Indeed, under assumption that ζ(3) = a/b for
some a, b ∈ Z, the linear forms rn = bDn3 (un ζ(3) − vn ) are integers which are
                                         1/n
nonzero by (20). On the other hand, Dn → e as n → ∞ in accordance with the
prime number theorem (see, for example, [145; Chap. II, § 3]); therefore,
                                     √
                  lim |rn |1/n = e3 ( 2 − 1)4 = 0.59126300 . . . < 1,
                  n→∞

and for all n sufficiently large this estimate contradicts the bound |rn | ⩾ 1 valid
for nonzero integers rn . Furthermore, the additional limiting relations (21) and a
standard argument (see, for example, [75; Lemma 3.1]) allow one to measure the
irrationality of the Apéry constant quantitatively:
                                      √
                                4 log( 2 + 1) + 3
                 µ(ζ(3)) ⩽ 1 +        √           = 13.41782023 . . . .
                                4 log( 2 + 1) − 3

   Here and below, the irrationality exponent µ(α) of a real irrational number α is
the quantity

            µ = µ(α) = inf{c ∈ R : the inequality |α − a/b| ⩽ |b|−c has
                             finitely many solutions in a, b ∈ Z};

when µ(α) < +∞, we say that α is a non-Liouvillian number.
   Apéry original derivation (namely, relations (16)–(21)) were so mysterious that
the interest to Apéry’s theorem remains strong till present time. The phenomenon
of the sequence of Apéry’s rational approximations was reconsidered time and again
from points of view of different methods (see [21], [24], [57], [72], [75], [101], [108],
[113], [132], [134], [135], [144], [154], [155], [160], and [182]). The new approaches
led to strengthening Apéry’s result quantitatively, new estimates for the irrational-
ity exponent of ζ(3) were deduced (the last stages of a competition in this direction
are the works [76] and [113]). We now indicate explicit formulae for the sequence
                                 Arithmetic hypergeometric series                                    9

un ζ(3) − vn that play an important role in our further discussion: Beukers’ repre-
sentation [21]
                          ZZZ n
                              x (1 − x)n y n (1 − y)n z n (1 − z)n
           un ζ(3) − vn =                                          dx dy dz    (22)
                                     (1 − (1 − xy)z)n+1
                              [0,1]3

in the form of multiple real integral, as well as the Gutnik–Nesterenko series [72],
[101]
                                ∞      µ                            ¶2 ¯
                              1 X d (t − 1)(t − 2) · · · (t − n) ¯¯
            un ζ(3) − vn = −                                                   (23)
                              2     dt t(t + 1)(t + 2) · · · (t + n) ¯
                                         ν=1                                            t=ν

and the Ball series [15]
                    ∞ ³                                                           ¯
                   X
                   2      n ´ (t − 1) · · · (t − n) · (t + n + 1) · · · (t + 2n) ¯¯
 un ζ(3) − vn = n!     t+                                                         ¯ . (24)
                   ν=1
                          2                 t4 (t + 1)4 · · · (t + n)4              t=ν

    We remark that on invoking his ‘acceleration convergence’ method, Apéry [12],
[106] also established the irrationality of ζ(2) without use of the formula ζ(2) =
π 2 /6. This time the denominators {u0n } and numerators {vn0 } of his linear approx-
imation forms u0n ζ(2) − vn0 , n = 0, 1, 2, . . . , satisfy the recursion

                  (n + 1)2 un+1 − (11n2 + 11n + 3)un − n2 un−1 = 0                                (25)

with the initial data

                          u00 = 1,       u01 = 3,         v00 = 0,     v10 = 5.                   (26)

Then
                  n µ ¶2 µ
                  X           ¶
                     n    n+k
          u0n =                                ∈ Z,     Dn2 vn0 ∈ Z,       n = 0, 1, 2, . . . ,   (27)
                          k          k
                  k=0

and
                                                          µ√¶5
                                                       5−1
                         lim  |u0n ζ(2) − vn0 |1/n =            < e−2 ,                           (28)
                        n→∞                             2
                                                          µ√      ¶5
                                   1/n             1/n       5+1
                          lim |un |    = lim |vn |     =             .                            (29)
                        n→∞             n→∞                   2

This sequence of approximations results in the estimate
                                      √
                       2       5 log(( 5 + 1)/2) + 2
         µ(ζ(2)) = µ(π ) ⩽ 1 +        √               = 11.85078219 . . .
                               5 log(( 5 + 1)/2) − 2

for the irrationality exponent of π 2 . Apéry’s approximations to ζ(2) can be given
by the double real integral [21]
                                      ZZ n
                0         0        n      x (1 − x)n y n (1 − y)n
               un ζ(2) − vn = (−1)                                dx dy,        (30)
                                                (1 − xy)n+1
                                               [0,1]2
10                                          W. Zudilin

as well as by the hypergeometric series
                                     ∞
                                     X                                     ¯
                                        n! · (t − 1)(t − 2)  · · · (t − n) ¯
              u0n ζ(2) − vn0 = (−1)n                                       ¯         .   (31)
                                       t2 (t + 1)2 (t + 2)2 · · · (t + n)2 ¯
                                      ν=1                                      t=ν

   Apéry theorem is in essence the very first step in approaching the following
problem (which can be undoubtedly called folklore; see, for example, [129; Con-
cluding remarks] for a record): prove that numbers ζ(2k + 1) are irrational for
k = 1, 2, 3, . . . .
   Unfortunately, natural generalisations of Apéry’s construction lead one to linear
forms involving values of the zeta function at both odd and even points. The latter
circumstance prevented to obtain results about the irrationality of ζ(s) for odd
s ⩾ 5. It was only in 2000, when T. Rivoal [116] used a general Ball’s representation
(24) to construct linear forms involving only the odd zeta values; the construction
allowed him to prove the following result.
Theorem 1. Of the numbers

                            ζ(3), ζ(5), ζ(7), ζ(9), ζ(11), . . . ,

infinitely many are irrational. More precisely, the dimension δ(s) of the spaces
which are generated by 1, ζ(3), ζ(5), . . . , ζ(s − 2), ζ(s) over Q, for s odd, satisfies the
estimate
                               log s
                     δ(s) ⩾              (1 + o(1))        as s → ∞.
                             1 + log 2
     Rivoal’s linear approximation forms in [116] are given by
                              ∞ ³              Qrn             Qrn               ¯
                      s+1−2r
                             X      n´           j=1 (t − j) ·  j=1 (t + n + j) ¯¯
      Fn = Fs,r,n = n!           t+                     Qn          s+1          ¯ ,
                             ν=1
                                    2                    j=0 (t + j)               t=ν   (32)
                                        s is odd,

where the auxiliary parameter r < s/2 is of order r ∼ s/ log2 s; in particular, the
series F3,1,n coincides with representation (24) of Apéry’s sequence. Decomposing
the summand, which is a rational function of parameter t, into the sum of partial
fractions and using the ideas from [101] and [103] one can show the arithmetic
inclusions

              2Dns+1 Fn ∈ Zζ(s) + Zζ(s − 2) + · · · + Zζ(5) + Zζ(3) + Z.

Furthermore, the explicit formulae (32) for the linear forms in odd zeta values
allow one to compute the asymptotic behaviour of the forms and their coefficients
as n → ∞. The final step in Rivoal’s proof is application of Nesterenko’s linear
independence criterion [100].
   The fact that the quantities in (32) are Q-linear forms in 1 and zeta values of
the same parity, is related to a special symmetry of the rational summand in (32).
Possible applications of less exotic rational functions are discussed in the works
                                 Arithmetic hypergeometric series                               11

[72], [77], and [117]: the results there are about dimensions of the spaces generated
over Q by the polylogarithmic values
                                                     ∞
                                                     X zn
                                         Lis (z) =
                                                     n=1
                                                           ns

at a rational point z, 0 < |z| ⩽ 1.
   In spite of the fact that the proof of Rivoal’s theorem is indeed a certain gen-
eralization of the construction from the proofs of Apéry’s theorem, Rivoal’s result
provides only a partial solution to the problem of the irrationality of odd zeta val-
ues. For the zeta value ζ(s) which is next irrational after ζ(3), Rivoal’s theorem [15]
only produces the range 5 ⩽ s ⩽ 169. Differentiation of rational summand (like
in representation (23)) allows one to construct Q-linear forms in odd zeta values
which do not involve ζ(3). This leads one [163], [118] to the result that at least one
of the nine odd zeta values ζ(5), ζ(7), . . . , ζ(21) is irrational. Finally, on invoking
the most general form of the construction proposed in Rivoal’s works as well as the
arithmetic method (discussed, for example, in [42], [126], and [75]), which is tra-
ditionally used for sharpening bounds of irrationality measures, we prove in [162],
[173] the following result.
Theorem 2. One of the numbers
                                 ζ(5), ζ(7), ζ(9), and ζ(11)
is irrational.
   We notice that the techniques used in the proof is also successfull in other arith-
metic problems: the paper [119] establishes analogues of Theorems 1 and 2 for the
values of Dirichlet’s beta function
                                               ∞
                                               X     (−1)n
                                     β(s) =
                                               n=0
                                                   (2n + 1)s

at even s ⩾ 2. In the joint paper [58], we give a certain strengthening (and a new
proof) of Nesterenko’s linear independence criterion from [100]; applying the result
we sharpen the ranges of the argument of the zeta function from [15] and [163].
1.2. Hypergeometric series and multiple integrals. Beukers’ proof [21] of
the irrationality of both ζ(2) and ζ(3), which makes use of the integral representa-
tions (30) and (22), is simple and short. This served as main grounds for further
applications of multiple integrals in the quantitative improvements and generalisa-
tions of Apéry’s results (see [50], [75], [76], [112], [113], [140], [141], [142], and [144]).
O. Vasilenko in [140] proposed to consider the following family of s-fold multiple
integrals which generalise the Beukers integrals:
                            Z      Z Qs         n             n
                                          j=1 xj (1 − xj )
                     Js,n = · · ·                               dx1 · · · dxs ,           (33)
                                       Qs (x1 , . . . , xs )n+1
                                [0,1]s

where
           Qs (x1 , . . . , xs ) = 1 − x1 (1 − x2 (1 − · · · (1 − xs−1 (1 − xs )) · · · )).   (34)
12                                             W. Zudilin

The first progress in this direction was the paper [142] of D. Vasil’ev who studied
the integrals J4,n , J5,n and proved that

            4Dn4 J4,n ∈ Zζ(4) + Zζ(2) + Z,              Dn5 J5,n ∈ Zζ(5) + Zζ(3) + Z,           (35)

as well as that the linear forms in (33) tend (reasonably fast) to zero as n → ∞
(unfortunately, not sufficiently fast to conclude on the new irrationality of zeta
values). The inclusions Dn2 J2,n ∈ Zζ(2) + Z and Dn3 J3,n ∈ Zζ(3) + Z established by
Beukers in [21], and (35) gave Vasil’ev grounds to conjecture that

      2s−2 Dns Js,n ∈ Zζ(s) + Zζ(s − 2) + · · · + Zζ(4) + Zζ(2) + Z for s even,
                                                                                                (36)
        Dns Js,n ∈ Zζ(s) + Zζ(s − 2) + · · · + Zζ(5) + Zζ(3) + Z for s odd.

   In spite of validity of this expectation for s = 2, 3, 4, 5, the confidence of the
author of [142] in the truth of (36) for all s was not shared by everybody. The
reason for that was another wrong conjecture, namely, 2s−2 Dns Js,n ∈ Zζ(s) + Z
for s even and Dns Js,n ∈ Zζ(s) + Z for s odd, proposed by Vasil’ev in his previous
work [141]. One of the first steps in answering Vasil’ev’s question in the affirmative
was the following partial (up to an extra multiple 2Dn ) result [166], [171], [173].
Theorem 3. For every integer s ⩾ 2 and n = 0, 1, 2, . . . , the identity

                                               Js,n = Fs,n                                      (37)

is true, where
                                           ³           Qn             Qn                ¯
                                                  n´
                   ∞
                   X
             s−1            (s+1)(t+n+1)                j=1 (t − j) ·  j=1 (t + n + j) ¯¯
 Fs,n = n!             (−1)                    t+             Qn           s+1          ¯ .     (38)
                   ν=1
                                                  2             j=0 (t + j)               t=ν

In particular, the following inclusions take place:

     2s−1 Dns+1 Js,n ∈ Zζ(s) + Zζ(s − 2) + · · · + Zζ(4) + Zζ(2) + Z            for s even,
                                                                                                (39)
       2Dns+1 Js,n ∈ Zζ(s) + Zζ(s − 2) + · · · + Zζ(5) + Zζ(3) + Z            for s odd.

   Note that the series (38) is exactly the same as the series (32) for s odd and
r = 1; therefore, identity (37) means the coincidence of the integral construction of
Q-linear forms in zeta values with the construction from [116].
   Ball’s (24) and Rivoal’s (32) series are well known in the theory of hypergeometric
functions [10], [13], [130]. Formally, a hypergeometric function is defined by the
series (1); the condition

                         Re(a1 + a2 + · · · + am ) < Re(b2 + · · · + bm )                       (40)

ensures convergence of (1) in the domain |z| ⩽ 1 (see, for example, [13; § 2.1]).
An important role in analysis of hypergeometric series is played by summation and
transformation formulae. We give as examples the Pfaff–Saalschütz summation
theorem              µ                     ¯ ¶
                                           ¯
                3 F2
                            −n, a, b       ¯ 1 = (c − a)n (c − b)n           (41)
                      c, 1 + a + b − c − n ¯     (c)n (c − a − b)n
                             Arithmetic hypergeometric series                           13

(here n is a non-negative integer; see, for example, [130; p. 49, equation (2.3.1.3)]),
the limiting case of Dougall’s theorem
               µ                                               ¯ ¶
                a, 1 + 12 a,     b,          c,          d     ¯
          5 F4
                                                               ¯1
                     1
                       a,    1 + a  − b, 1 + a  − c, 1 + a − d ¯
                     2
                 Γ(1 + a − b) Γ(1 + a − c) Γ(1 + a − d) Γ(1 + a − b − c − d)
             =                                                                        (42)
                 Γ(1 + a) Γ(1 + a − b − c) Γ(1 + a − b − d) Γ(1 + a − c − d)

(see [13; § 4.4]), and Whipple’s transformation
              µ                                                            ¯    ¶
                a, 1 + 12 a,     b,         c,           d,          e     ¯
         6 F5
                                                                           ¯ −1
                     1
                     2 a,    1 + a − b, 1 + a − c, 1 + a − d, 1 + a − e ¯
                                                  µ                      ¯ ¶
                Γ(1 + a − d) Γ(1 + a − e)           1 + a − b − c, d, e ¯¯
             =                             · 3 F2                          1          (43)
                Γ(1 + a) Γ(1 + a − d − e)           1 + a − b, 1 + a − c ¯

(see [147] and [13; § 4.4]). Furthermore, the hypergeometric functions possess many
integral representations [13], [130]; we mention here the classical Euler–Pochhammer
integral for the Gaussian function (m = 1)
                µ      ¯ ¶                Z 1
                 a, b ¯¯          Γ(c)
           2 F1          z =                  tb−1 (1 − t)c−b−1 (1 − zt)−a dt    (44)
                  c ¯         Γ(b)Γ(c − b) 0

when Re c > Re b > 0 (see, for example, [130; p. 20, equation (1.6.6)]). Formula (44)
is valid for |z| < 1 and also for any z ∈ C whenever a is a positive integer.
   In his work [148], F. Whipple called hypergeometric series well-poised if their
parameters satisfy the condition

                          a1 + 1 = a2 + b2 = · · · = am + bm ;

known transformations (like (42) and (43)) usually refer to such series. A special
subclass of well-poised hypergeometric series is very-well-poised series, which are
subject to the additional condition

                               a2 = 12 a1 + 1,   b2 = 12 a1 .

A survey on history and applications of (very-) well-poised hypergeometric series
is given in [9]. The series (38) (as well as (32)) are very-well-poised:
                                    µ                                         ¯          ¶
        n!2s+1 (3n + 2)!             3n + 2, 32 n + 2, n + 1, . . . , n + 1 ¯¯       s+1
Fs,n =                   · s+4 Fs+3           3                               ¯ (−1)      .
          (2n + 1)!s+2                        2 n + 1, 2n + 2, . . . , 2n + 2
                                                                                      (45)
Theorem 3 is a consequence of a more general result [166], [171] about representation
of a very-well-poised series as a multiple integral.
   Vasil’ev’s conjecture (36) was fully solved in the work [79] with the help of
Theorem 3. The methods of [79] are based on representation of the sums (45) in
the form of multiple hypergeometric series and heavily exploit ideas of the works
[142] and [171]; however the technical realisation of the ideas required the authors
of [79] large computational work. The series (45) possess different multiple-integral
14                                    W. Zudilin

representations as well, in particular of Sorokin type (the works [133] and [134]
contain number-theoretical applications of such integrals); respective translation
theorems for multiple integrals are established by S. Zlobin [156], [157]. At present,
there are several works where decomposition of special multiple integrals into linear
forms of zeta values and polylogarithms is addressed. This subject already deserves
a separate review; we restrict ourselves here by the references [158] and [174], which
deal with new generalisations of Beukers’ integrals (22) and (30).
   It is worth mentioning here that the hypergeometric techniques of the work [79],
namely, Andrews’ general transformation [8] for terminating very-well-poised series,
allowed K. Krattenthaler and T. Rivoal [80] to give a new proof of the theorem
from [166], [171] (in particular, of Theorem 3). It is surprising that the transforma-
tion, initially designed for q-basic hypergeometric series in connection with applica-
tions to the theory of partitions — generalisations of the famous Rogers–Ramanujan
identities, has found its second birth in arithmetic problems of zeta values. Besides
[79], [80], we should mention the works [81] and [175], as well as solution to a
problem of A. Schmidt discussed in more details below.
   Schmidt observed in [127] that there is a remarkable property of the sequence
of Apéry’s numbers {un }n=0,1,... from (19). Namely, if one defines the numbers
{ck }k=0,1,... successively from the equalities
                           X n µ ¶µ        ¶
                                n n+k
                     un =                    ck ,   n = 0, 1, 2, . . . ,
                                k      k
                         k=0

then these numbers are integral. (The explicit formulae
             µ ¶−1 X n                    µ       ¶
              2n             n−k 2k + 1       2n
       cn =             (−1)                        uk ,      n = 0, 1, 2, . . . ,
               n                 n+k+1 n−k
                       k=0

show that expected inclusions are Dn cn ∈ Z.) Later Schmidt himself [128] and,
independently, V. Strehl [136] derived the following explicit relation:
                   X n µ ¶3      X µn¶2 µ2j ¶
                         n
              cn =            =                 ,     n = 0, 1, 2, . . . , (46)
                   j=0
                          j       j
                                      j      n

experimentally predicted by W. Deuber, W. Thumser, and B. Voigt. In fact, Strehl
used in [136] the corresponding identity
                 Xn µ ¶2 µ       ¶2 X    n µ ¶µ    ¶ k µ ¶3
                       n    n+k             n n+k X k
                                    =
                       k      k             k   k    j=0
                                                          j
                 k=0                    k=0

as a model for demonstrating various proof techniques for binomial identities. A
surprising fact about the sequence (46) is that it was studied already at the end
of the 19th century by J. Franel [60], who showed that it satisfies the polynomial
recursion
                 (n + 1)2 cn+1 − (7n2 + 7n + 2)cn − 8n2 cn−1 = 0.
   Schmidt has noticed in [127] that it is likely that the integrality phenomenon
related to Apéry’s and Franel’s numbers take place in a more general situation.
This expectation was proven in full generality in [176], [177].
                                  Arithmetic hypergeometric series                         15

                                                                                (r)
Theorem 4. For each integer r ⩾ 2, the numerical sequence {ck }k=0,1,... inde-
pendent of parameter n is defined by the equality
         Xn µ ¶r µ       ¶r X   n µ ¶µ          ¶
              n    n+k               n n + k (r)
                             =                    ck , n = 0, 1, 2, . . . . (47)
              k      k               k      k
         k=0                           k=0

                     (r)
Then all numbers ck        are integral.
   But for this case Strehl had only one proof based Using Zeilberger’s algorithm
                                                                    (r)
of creative telescoping, Strehl proved in [136] the integrality of ck when r = 3.
Schmidt’s problem was later stated in the book [64] (Exercise 114 on p. 256) with
                                                                   (r)
an indication that H. Wilf had shown the desired integrality of cn for any r but
only for any n ⩽ 9. The complete proof of Theorem 4 uses a hypergeometric
reformulation from [136] of the problem, as well as Andrews’ transformation of
terminating very-well-poised series [8] mentioned above.
1.3. Simultaneous approximations to ζ(2) and ζ(3). In this section we
present three hypergeometric constructions of simultaneous rational approxima-
tions to ζ(2) and ζ(3). This is to not only demonstrate the hypergeometric series
in action, but also to show how so seemingly unrelated series give rise to the
same numerical approximations. A similar phenomenon, the coincidence of the
Gutnik–Nesterenko series (23) and Ball’s series (24), was already mentioned in § 1.1.
The constructions below depend on an increasing integer parameter n.
   First [167] we take the rational functions
                            Qn                             Qn
                        n!2 j=1 (t − j)        0
                                                       n!2 j=0 (t − j)
             Rn (t) = − Qn             3
                                         ,    Rn (t) = Qn             3
                                                                        ,
                            j=0 (t + j)                    j=0 (t + j)

and consider the corresponding hypergeometric series
                              ∞
                              X           ¯
                      rn =          Rn (t)¯t=ν = qn ζ(3) + pn ζ(2) − sn ,
                              k=1
                              X∞
                                           ¯
                      rn0 =         Rn0 (t)¯t=ν = qn0 ζ(3) + p0n ζ(2) − s0n ,
                              k=1

where
                  qn , qn0 ∈ Z,     Dn pn , Dn p0n ∈ Z,     Dn3 sn , Dn3 s0n ∈ Z.        (48)
The standard eliminating argument leads us to the linear forms
        qn rn0 − qn0 rn = (qn p0n − qn0 pn )ζ(2) − (qn s0n − qn0 sn ) = un ζ(2) − vn ,
        p0n rn − pn rn0 = (qn p0n − qn0 pn )ζ(3) − (p0n sn − pn s0n ) = un ζ(3) − wn ,
where, by (48),
                           Dn un ∈ Z,        Dn3 vn ∈ Z,    Dn4 wn ∈ Z.                  (49)
  The second construction [180] is based on the rational function
                                                                      3
                           en (t) = ((t − 1)(t − 2) · · · (t − n)) .
                           R
                                      n!2 · t(t + 1) · · · (t + n)
16                                               W. Zudilin

Then hypergeometric approximations to the first three polylogarithms are given by
the series
                               ∞
                               X            ¯
                   ren (z) =          en (t)¯
                                   zν R           =u
                                                   en (z) Li1 (z) − sen (z),
                                              t=ν
                               ν=1
                                  ∞              ¯
                                 X      d en (t) ¯
                                          R
                   ren0 (z) = −      zν          ¯     =u
                                                        en (z) Li2 (z) − ven (z),
                                           dt    ¯
                                 ν=1               t=ν
                                 X∞      2e
                                                   ¯
                               1        d  Rn (t)  ¯
                   ren00 (z) =       zν            ¯   =uen (z) Li3 (z) − wen (z),
                               2 ν=1       dt2 ¯t=ν

where
                                        n µ ¶µ
                                        X        ¶3 µ    ¶k
                                           n n+k
                                             n         1
                          u
                          en (z) = (−1)              −                                                 (50)
                                           k   k       z
                                                 k=0

and
                               z1n u
                                   en (z) ∈ Z,         (z1 z2 )n Dn sen (z) ∈ Z,
                                                                                                       (51)
                   (z1 z2 )n Dn D2n ven (z) ∈ Z,           (z1 z2 )n Dn D2n
                                                                         2
                                                                            w
                                                                            en (z) ∈ Z,
z1 and z2 denote the denominators of the numbers 1/z and z/(1 − z), respectively.
   In the limiting case z → 1 we obtain

            ren0 (1) = u
                       en ζ(2) − ven ,       ren00 (1) = u
                                                         en ζ(3) − w
                                                                   en ,            n = 0, 1, . . . ,

where for u
          en = u
               en (1), ven = ven (1), and w
                                          en = w
                                               en (1) from (50), (51) we can write
                                                                     2
                         u
                         en ∈ Z,          Dn D2n ven ∈ Z,        Dn D2n w
                                                                        en ∈ Z.                        (52)

     Finally, we take the rational function

             ee         (t − 1)(t − 2) · · · (t − n) · (2t − 1)(2t − 2) · · · (2t − n)
             R  n (t) =
                                     (t(t + 1)(t + 2) · · · (t + n))2

and consider the following two series:
                             ∞
                          1X                  ¯
                                                       e
                                                       en ζ(2) − e
                                (−1)ν−1 Rn (t)¯t=ν/2 = u         ven ,
                          2 ν=1
                                      ∞         ¯
                                   1 X dRn (t) ¯¯      e          een .
                                 −                   =uen ζ(3) − w
                                   2 ν=1 dt ¯t=ν

The explicit formulae for the approximants allow us to show that
                   n µ ¶2 µ
                   X            ¶µ       ¶
            e         n     n+k   n + 2k
            u
            en =                                             ∈ Z,
                          k           n            n                    for n = 0, 1, 2, . . . .       (53)
                   k=0
                      2 e                     een ∈ Z,
                     D2n ven ∈ Z,         Dn3 w
                                     Arithmetic hypergeometric series                                17

Theorem 5. For n = 0, 1, 2, . . . , the following equalities are true:
  µ      ¶−1                         µ     ¶−1                    µ ¶−1
      2n               e                 2n                        2n
             un = u
                  en = u
                       en ,                    vn = ven = e
                                                          ven ,         wn = w    een , (54)
                                                                             en = w
       n                                 n                          n

that is, the three hypergeometric constructions give the same sequence of simulta-
neous rational approximations to 1, ζ(2) and ζ(3).
  From Theorem 5 and the inclusions (48), (52), (53) one may easily deduce that

            u
            en ∈ Z,      Dn D2n ven ∈ Z,         Dn3 w
                                                     en ∈ Z,      for    n = 0, 1, 2, . . . .      (55)

   Theorem 5 can be shown by means of certain hypergeometric identities. A sim-
pler way (used in [167] and [180]) is based on the algorithm of creative telescoping.
Indeed, the above sequences (54) satisfy the Apéry-type polynomial recurrence rela-
tion

  2(946n2 − 731n + 153)(2n + 1)(n + 1)3 un+1
   − 2(104060n6 + 127710n5 + 12788n4 − 34525n3 − 8482n2 + 3298n + 1071)un
   + 2(3784n5 − 1032n4 − 1925n3 + 853n2 + 328n − 184)nun−1
   − (946n2 + 1161n + 368)n(n − 1)3 un−2 = 0,                     n = 2, 3, . . . ,

of order 3, and the necessary initial data is as follows:

                                   u
                                   e0 = 1, u e1 = 7, ue2 = 163,
                            23           2145                     17                      3135
        ve0 = 0,    ve1 =      ,   ve2 =      ,    w
                                                   e0 = 0, w e1 =    ,            w
                                                                                  e2 =         .
                             2             8                      2                        16
In addition,

                         rn0 |1/n = lim sup |e
                lim sup |e                   rn00 |1/n = |λ1,2 | = 0.067442248 . . . ,
                 n→∞                    n→∞

          lim     un |1/n =
                 |e            lim    vn |1/n =
                                     |e                en |1/n = λ3 = 54.96369509 . . . ,
                                                  lim |w
         n→∞                  n→∞                 n→∞

where λ1,2 = 0.018152450 . . . ± i0.064953409 . . . and λ3 are zeros of the character-
istic polynomial 4λ3 − 220λ2 + 8λ − 1.
   Since log |λ1,2 | = −2.69648361 . . . > −3, from (55) and the above we cannot
conclude about the irrationality of either ζ(2) or ζ(3). However, the use of an
asymmetric rational function

   R(t) = R(a, b; t)
            (2t + b0 )(2t + b0 + 1) · · · (2t + a0 − 1) (t + b1 ) · · · (t + a1 − 1)
          =                                               ·
                              (a0 − b0 )!                           (a1 − b1 )!
                      (b2 − a2 − 1)!               (b3 − a3 − 1)!
              ×                              ·
                 (t + a2 ) · · · (t + b2 − 1) (t + a3 ) · · · (t + b3 − 1)
            (b2 − a2 − 1)! (b3 − a3 − 1)! Γ(2t + a0 ) Γ(t + a1 ) Γ(t + a2 ) Γ(t + a3 )
          =                                   ·                                              ,
                (a0 − b0 )! (a1 − b1 )!         Γ(2t + b0 ) Γ(t + b1 ) Γ(t + b2 ) Γ(t + b3 )
18                                               W. Zudilin

where the integers a and b satisfy

                b1 = 1 < a1 , a2 , a3 < b2 , b3 , b0 < a0 ⩽ 2 max{a1 , a2 , a3 },
                        a0 + a1 + a2 + a3 ⩽ b0 + b1 + b2 + b3 + 2,

lead to the following curious application.
   Taking

                a0 = 10n + 12 , a1 = 6n + 1, a2 = 7n + 1, a3 = 8n + 1,
                   b0 = 6n + 1, b1 = 1, b2 = 13n + 2, b3 = 12n + 2,

for the coefficients of linear forms
                                     ∞
                                     X               ¯
                         rn =              (−1)ν R(t)¯t=ν/2 = un ζ(2) − vn ,
                                 ν=−10n
                                   ∞          ¯
                                  X    dR(t) ¯¯
                         rn0 =                  = un ζ(3) − wn ,
                                 ν=−5n
                                        dt ¯t=ν

we obtain the inclusions

                  Φ−1
                   n un ∈ Z,           D8n D16n Φ−1
                                                 n vn ∈ Z,
                                                                       3
                                                                      D8n Φ−1
                                                                           n wn ∈ Z,

where Φn is a certain product over primes,
                                         log Φn
                                     lim        = 8.48973583 . . . .
                                     n→∞    n
On the other hand,

                           log |rn |           log |rn0 |
                 lim sup             = lim sup            = −17.610428885 . . . .
                  n→∞         n          n→∞      n

Thus, the linear forms rn and rn0 allow one to deduce the irrationality of either ζ(2)
or ζ(3), but not to obtain their simultaneous Q-linear independence with 1 (the
                                              2
common denominator of the coefficients is D8n   D16n Φ−1
                                                       n ).

1.4. q-Analogues of zeta values. It is customary to call q-dependent quanti-
ties, which become ordinary objects as q → 1 (at least formally), q-analogues or
q-etensions. A possible way to q-extend the values of Riemann’s zeta function reads
as follows (here q ∈ C, |q| < 1):
                ∞
                X                       ∞
                                        X                  ∞
                                                           X
                                 n        ν s−1 q ν          q ν ρs (q ν )
     ζq (s) =         σs−1 (n)q =                      =                       ,    s = 1, 2, . . . ,   (56)
                n=1                     ν=1
                                              1 − qν       ν=1
                                                                 (1 − q ν )s
                   P      s−1
where σs−1 (n) =     d|n d    denotes the sum of powers of the divisors, and the
polynomials ρs (x) ∈ Z[x] can be defined recursively by means of the formulae

                                                                          dρs
 ρ1 = 1         and       ρs+1 = (1 + (s − 1)x)ρs + x(1 − x)                       for s = 1, 2, . . . . (57)
                                                                          dx
                              Arithmetic hypergeometric series                            19

Then we have the limiting relations
          lim (1 − q)s ζq (s) = ρs (1) · ζ(s) = (s − 1)! · ζ(s),    s = 2, 3, . . . ;
          q→1
         |q|<1

the equality ρs (1) = (s−1)! follows from (57). The q-zeta values (56) so defined lead
one to a circle of new interesting problems in the theory of diophantine approxima-
tions and transcendental numbers [168], which are extensions of relative problems
for usual zeta values. It is not hard to show [170] that ζq (s) is transcendental as a
function of variable q, and also [109] that the q-zeta values form a set of linearly
independent over C(q) functions.
    For even s ⩾ 2, the series Es (q) = 1 − 2sζq (s)/Bs , where Bs ∈ Q are the
Bernoulli numbers, are known as Eisenstein series. Therefore, the modular origin
(with respect to τ = log    q
                         2πi ; see also § 2.3 below) of the functions E4 , E6 , E8 , . . .
implies the algebraic independence of ζq (2), ζq (4), ζq (6) over Q[q], while all other
even q-zeta values are polynomials in ζq (4) and ζq (6). In this interpretation, the con-
sequence of Nesterenko’s theorem [102], numbers ζq (2), ζq (4), ζq (6) are algebraically
independent over Q for algebraic q, 0 < |q| < 1, is a complete q-extension of Lin-
demann’s theorem [90], ζ(2) = π 2 /6 is transcendental. Not much is known about
the arithmetic nature of odd q-zeta values. P. Erdös [52] showed the irrationality of
ζq (1) (the q-harmonic series) when q = p−1 for p ∈ Z \ {0, ±1}; other proofs of this
fact are given in [27] and [32], while the works [37] and [139] contain the estimate
                                         2π 2
                          µ(ζq (1)) ⩽          = 2.50828476 . . .                       (58)
                                        π2 − 2
for the irrationality exponent of ζq (1) under the same assumptions on q. The
construction of linear approximation forms for ζq (1) in [37] and [139] has several
common features with the construction of Apéry’s approximations (23), (31). This
motivated W. Van Assche to formulate in [139] the problem of constructing linear
approximation forms for ζq (2) and ζq (3), which demonstrate the irrationality of the
numbers when q −1 ∈ Z \ {0, ±1} and which become, as q → 1, Apéry’s sequences
u0n ζ(2) − vn0 and un ζ(3) − vn , respectively (from § 1.1).
    The methods of investigating arithmetic properties of numbers ζ(s), s = 2, 3, . . . ,
successfully extends to q-zeta values. Namely, we mean the hypergeometric con-
struction of linear forms as well as the arithmetic method accomplished by the
group structure approach of G. Rhin and C. Viola [112], [113], [144]. For each
of these constituents we can indicate the required q-extension: for example, the
use of q-basic hypergeometric series, Heine’s classical transformation [61] and the
q-arithmetic method [164] (Table 1 contains corresponding parallels between ordi-
nary and q-arithmetic) allows us in [172] to sharpen the estimate (58) for the
irrationality exponent of the q-harmonic series: µ(ζq (1)) ⩽ 2.46497868 . . . .
    Using a q-analogue of the hypergeometric 3 F2 (1)-series and Hall’s transformation
[61], we not only solve in [165] the problem of Van Asshe for ζq (2) but also optimise
the estimate for the irrationality exponent of the number.
Theorem 6. For each q = 1/p, p ∈ Z \ {0, ±1}, number ζq (2) is irrational whose
irrationality exponent satisfies the inequality
                               µ(ζq (2)) ⩽ 4.07869374 . . . .                           (59)
20                                            W. Zudilin

            ordinary objects                          q-extensions, p = 1/q ∈ Z \ {0, ±1}
                                                                          pn − 1
             numbers n ∈ Z                              q-numbers [n]p =         ∈ Z[p]
                                                                           p−1
                                                      irreducible cyclotomic polynomials
                                                                   l
                                                                   Y
     primes l ∈ {2, 3, 5, 7, . . . } ⊂ Z               Φl (p) =             (p − e2πik/l ) ∈ Z[p]
                                                                    k=1
                                                                  (k,l)=1
                                                          Jackson’s q-gamma function
                                                                Q∞           ν
     Euler’s gamma function Γ(t)                                  ν=1 (1 − q )
                                                     Γq (t) = Q                    (1 − q)1−t
                                                                ∞          t+ν−1 )
                                                                ν=1 (1 − q
         factorial n! = Γ(n + 1)                          q-factorial [n]q ! = Γq (n + 1)
                   Yn
                                                           Yn
             n! =      ν∈Z                                      pν − 1
                                                  [n]p ! =              = pn(n−1)/2 [n]q ! ∈ Z[p]
                    ν=1
                                                           ν=1
                                                                 p −  1
                ¹ º ¹ º                                                 ¹ º
                 n   n                                                   n
      ordl n! =    + 2 + ···                         ordΦl (p) [n]p ! =      , l = 2, 3, 4, . . .
                 l   l                                                   l
 Dn = lcm(1, . . . , n)                                    Dn (p) = lcm([1]p , . . . , [n]p )
         Y                                                          Yn
    =               lblog n/ log lc ∈ Z                           =    Φl (p) ∈ Z[p]
           primes l ⩽ n
                                                                      l=1
      the prime number theorem                                  Mertens’ formula
                log Dn                                            log |Dn (p)|   3
            lim        =1                                     lim    2
                                                                               = 2
           n→∞     n                                         n→∞ n log |p|      π

          Table 1. Comparison of the q-arithmetic with ordinary arithmetic. Here
          b · c is the integral part of a number and abbreviation ‘lcm’ is used for the
          least common multiple

   Quantitative estimates of type (59) for ζq (2) (which show that the number is
the non-Liuovillian for q −1 ∈ Z \ {0, ±1}) were not known before, although as
mentioned earlier the irrationality [49] and even the transcendence of ζq (2) for any
algebraic q satisfying 0 < |q| < 1 follows from Nesterenko’s theorem [102]. A
different interpretation of the rational approximations to ζq (2) in [131] allowed the
authors to simplify the arithmetic part and to sharpen the estimate (59):
                                             10π 2
                            µ(ζq (2)) ⩽              = 3.89363887 . . . .
                                           5π 2 − 24
A particular case of the hypergeometric construction from [165], [131], namely,
                                  X∞ Qn         j
                                                     Qn           j         ¯
                                n     j=1 (1 − q ) ·    j=1 (1 − q T ) n+1 ¯¯
    Un (q)ζq (2) − Vn (q) = (−1)         Qn            n+1+j T )2
                                                                      T     ¯        ,
                                  ν=1      j=0 (1 −  q                        T =q ν

leads to the irrationality of ζq (2) in case of q −1 ∈ Z \ {0, ±1}, while in the limit
q → 1 one obtains the rational approximations of Apéry (31) to ζ(2). In the
                             Arithmetic hypergeometric series                         21

joint paper [84] we indicate a q-analogue of the sequence of the rational approxi-
mations (23), (24); it however does not result in the irrationality of the quantity
ζq (3).
    Application of the q-arithmetic method and the hypergeometric construction
allows one to deduce other quantitative and qualitative results for q-zeta values.
Thus, the work [84] establishes the result on the infiniteness of irrational numbers
in the set of odd q-zeta values (a q-analogue of Rivoal’s theorem) when q −1 ∈
Z \ {0, ±1}; the quantitative results of [84] were slightly improved in the recent
works [58], [78]. A special status is given to the linear independence (under the
same assumptions on q) of ζq (1), ζq (2) and 1 over Q, in both qualitative and
quantitative forms; see the papers [38], [107], [138], [178] on this direction.
    We also notice that one of approaches to the Riemann hypothesis (see [28]) and
to integrality problems occurring in string theory (see [45] and § 2.2 below) exploits
integer-valued factorial quotients and the corresponding generating hypergeometric
series. As shown in [146] (hypothetically in most of the cases), the q-counterpart
of this approach leads to q-polynomials with non-negative coefficients.

1.5. Lower bound for k(3/2)k k and Waring’s problem. We do not aim at
covering all possible applications of hypergeometric constructions in arithmetic.
Our finale in Section 1 is one more problem on the border of diophantine and
analytic number theories. On first sight, it might seem that the problem is not
related to Apéry’s theorem, but the efficient methods of its solutions, a hypergeo-
metric construction and the arithmetic method (used, for example, in the proof of
Theorems 2 and 6), convince of the opposite.
   Let b · c and { · } denote the integer and fractional parts of a number, respectively.
It is known [143] that the inequality {(3/2)k } ⩽ 1 − (3/4)k for k ⩾ 6 implies the
explicit formula g(k) = 2k + b(3/2)k c − 2 for the least integer g = g(k) such that
every positive integer can be expressed as a sum of at most g positive kth powers
(Waring’s problem). K. Mahler [92] used Ridout’s extension of Roth’s theorem to
show that the inequality k(3/2)k k ⩽ C k , where kxk = min({x}, 1 − {x}) is the
distance from x ∈ R to the nearest integer, has finitely many solutions in integers k
for any C < 1. The particular case C = 3/4 gives one the above value of g(k) for all
k ⩾ K, where K is a certain absolute but ineffective constant. This motivates the
question about nontrivial (that is, C > 1/2) and effective (in terms of K) estimate
of the form
                           °µ ¶k °
                           ° 3 °
                           °        °     k
                           ° 2 °>C              for all k ⩾ K.                      (60)

The first progress towards the problem belongs to A. Baker and J. Coates [14]; by
applying effective estimates of linear forms in logarithms in the p-adic case, they
                                                     −64
showed the validity of (60) with C = 2−(1−10 ) . F. Beukers [22] significantly
improved on this result by showing that inequality (60) is valid with C = 2−0.9 =
0.5358 . . . for k ⩾ K = 5000 (although his proof yielded the better choice C =
0.5637 . . . if one did not require an explicit evaluation of the effective bound for K).
Beukers’ proof relied  Pmon ¡explicit
                                 ¢     Padé approximations to a tail of the binomial
                               m
series (1 − z)m =        n=0 n    (−z) n
                                         and was later used by A. Dubickas [48] and
L. Habsieger [74] to derive inequality (60) with C = 0.5769 and 0.5770, respectively.
22                                       W. Zudilin

The latter work also includes the estimate k(3/2)k k > 0.57434k for k ⩾ 5 using
computations from [46] and [85].
   By modifying Beukers’ construction [22], namely, considering Padé approxima-
tions to a tail of the series
                                          X∞ µ     ¶
                                  1           m+n n
                                        =            z ,                     (61)
                             (1 − z)m+1   n=0
                                               m

and evaluating the explicit p-adic order of the binomial coefficients involved, we
prove in [179] the inequality
               °µ ¶k °
               ° 3 °
               °       °        k    −k·0.78512916...
               ° 2 ° > 0.5803 = 2                      for k ⩾ K,

where K is a certain effective constant.
  The construction in [179] allowed us to also establish the estimates
             °µ ¶k °
             ° 4 °
             °       °           k    −k·0.64672207...
             ° 3 ° > 0.4914 = 3                         for k ⩾ K1 ,
             °µ ¶k °                                                                     (62)
             ° 5 °
             °       °           k    −k·0.47839775...
             ° 4 ° > 0.5152 = 4                         for k ⩾ K2 ,

where K1 , K2 are effective constants. The best known result for general sequences
k(1 + 1/N )k k is due to M. Bennett [17]: k(1 + 1/N )k k > 3−k for 4 ⩽ N ⩽ k3k .
Our lower bound for k(4/3)k k complements Bennett’s result [18] on the order of the
additive basis {1, N k , (N + 1)k , (N + 2)k , . . . } for N = 3 (case N = 2 corresponds
to the classical Waring’s problem); to solve this problem one needs the bound
k(4/3)k k > (4/9)k for k ⩾ 6. The question of effectivisation of the estimates (62)
is discussed in [110].

                       2. Calabi–Yau differential equations
2.1. Arithmetic differential equations of order 2 and 3. Certain differen-
tial equations look better than others, at least arithmetically. To illustrate this
principle, consider the differential equation
         ¡ 2                                  ¢                                   d
          θ − z(11θ2 + 11θ + 3) − z 2 (θ + 1)2 y = 0,           where θ = z          .   (63)
                                                                                  dz
What is special about it? First of all, it has a unique analytic solution y0 (z) = f (z)
with f (0) = 1; another solution may be given in the form y1 (z) = f (z)P  log z + g(z)
                                                                              ∞
with g(0) = 0. Secondly, the coefficients in the Taylor expansion f (z) = n=0 An z n
are integral, f (z) ∈ 1+zZ[[z]], which can be hardly seen from the defining recurrence

 (n + 1)2 An+1 − (11n2 + 11n + 3)An − n2 An−1 = 0         for n = 0, 1, . . . ,   A0 = 1 (64)

(cf. (25)), but follows from the explicit expression
                            Xn µ ¶2 µ        ¶
                                 n     n+k
                      An =                    ,      n = 0, 1, . . . ,                   (65)
                                 k        n
                             k=0
                              Arithmetic hypergeometric series                                  23

due to R. Apéry [12]; note that these numbers appear in Apéry’s proof of the irra-
tionality of ζ(2). Thirdly, the expansion q(z) = exp(y1 (z)/y0 (z)) = z exp(g(z)/f (z))
also has integral coefficients, q(z) ∈ zZ[[z]]. This follows from the fact that the
functional inverse z(q),
                                        ∞
                                        Y               n
                               z(q) = q    (1 − q n )5( 5 ) ,                     (66)
                                    n=1
        n
where ( 5 ) denotes the Legendre symbol, lies in qZ[[q]].   The formula in (66), due
to F. Beukers [23], shows that z(q) is a modular function with respect to the con-
gruence subgroup Γ1 (5) of SL2 (Z).
   If the reader is not so much surprised by these integrality properties, then try to
find more such cases, replacing the differential operator in (63) by the more general
one
                D = D(a, b, c) := θ2 − z(aθ2 + aθ + b) + cz 2 (θ + 1)2 .          (67)
To ensure the required integrality one easily gets a, b, c ∈ Z, but for a generic choice
of the parameters already the second feature (y0 (z) = f (z) ∈ 1+zZ[[z]]) fails ‘almost
always’. In fact, this problem was studied by F. Beukers [25] and D. Zagier [154].
The exhaustive experimental search in [154] resulted in 14 (non-degenerate) exam-
ples of the triplets (a, b, c) ∈ Z3 when both this and the third property (the integral-
ity of the corresponding expansion z(q)) happen; the latter follows from modular
interpretations of z(q).

   # in [5]      # in [154]              (a, b, c)           # in [5]            (â, b̂, ĉ)
    (A)            #11                  (16, 4, 0)            (β)             (16, 8, 162 )
    (B)            #14                  (27, 6, 0)             (ι)           (27, 15, 272 )
    (C)            #20                 (64, 12, 0)             (ϑ)           (64, 40, 642 )
    (D)                               (432, 60, 0)             (κ)         (432, 312, 4322 )
     (e)             #19             (32, 12, 162 )                             (32, 8, 0)
     (h)             #25             (54, 21, 272 )                            (54, 12, 0)
     (i)             #26            (128, 52, 642 )                           (128, 24, 0)
     (j)                           (864, 372, 4322 )                         (864, 120, 0)
     (a)           #5, A               (7, 2, −8)              (δ)              (7, 3, 81)
     (b)           #9, D              (11, 3, −1)              (η)            (11, 5, 125)
     (c)           #8, C                (10, 3, 9)             (α)             (10, 4, 64)
     (d)           #10, E              (12, 4, 32)             (²)             (12, 4, 16)
     (f)           #7, B                (9, 3, 27)             (ζ)            (9, 3, −27)
     (g)           #13, F              (17, 6, 72)             (γ)              (17, 5, 1)

           Table 2. Arithmetic differential operators D(a, b, c) and D̂(â, b̂, ĉ)

   A natural extension of the above problem to 3rd order linear differential equa-
tions is prompted by the other Apéry’s sequence used in his proof [12] of the irra-
tionality of ζ(3). One takes the family of differential operators
            D̂ = D̂(â, b̂, ĉ) := θ3 − z(2θ + 1)(âθ2 + âθ + b̂) + ĉz 2 (θ + 1)3       (68)
and looks for the cases when the two solutions f (z) ∈ 1 + zC[[z]] and f (z) log z +
g(z) with g(0) = 0 of the corresponding differential equation satisfy f (z) ∈ Z[[z]]
24                                           W. Zudilin

and exp(g(z)/f (z)) ∈ Z[[z]]. Apart from some degenerate cases, we have found
in [6] again 14 triplets (â, b̂, ĉ) ∈ Z3 meeting the integrality conditions; the second
property holds in all these cases as a modular bonus. Apéry’s example corresponds
to the case (â, b̂, ĉ) = (17, 5, 1). Table 2 lists the corresponding 14 examples of
order 2 and 14 examples of order 3, while the following theorem indicates an explicit
relation between them. The proof of the theorem as well as a geometric motivation
for it can be found in [5; Theorem 1]; there explicit binomial expressions for the
analytic solutions f (z) are given as well.
Theorem 7. Let the triplets (a, b, c) and (â, b̂, ĉ) be related by the formulae
                           â = a,   b̂ = a − 2b    and    ĉ = a2 − 4c.            (69)
For the differential operators D and D b given in (67) and (68), denote by f (z) and
ˆ
f (z) the analytic solutions of Dy = 0 and Dy b = 0, respectively, with f (0) = fˆ(0) =
1. Then                                         µ               ¶
                                     1                 −z
                            2
                       f (z) =                fˆ                 .                 (70)
                                1 − az + cz 2     1 − az + cz 2
2.2. Arithmetic differential equations of order 4 and 5. How can one gener-
alise the above problem of finding ‘arithmetically nice’ linear differential equations
(operators)? An approach we followed in [6], [3], at least up to order 5, was not
specifying the form of the operator, like in (67) and (68), but posing the following:
    (i) the differential equation is of Fuchsian type, that is, all its singular points
        are regular; in addition, the local exponents at z = 0 are zero;
   (ii) the unique analytic solution y0 (z) = f (z) with f (0) = 1 at the origin have
        integral coefficients, f (z) ∈ 1 + zZ[[z]]; and
  (iii) the solution y1 (z) = f (z) log z + g(z) with g(0) = 0 gives rise to the integral
        expansion q(z) := exp(y1 (z)/y0 (z)) ∈ zZ[[z]].
Requirement (i), known as the condition of maximally unipotent monodromy (MUM),
means that the corresponding differential operator written as a polynomial in
variable z with coefficients from C[[θ]] has constant term θm , where m is the
order — degree in θ; the local monodromy around 0 consists of a single Jordan
block of maximal size. Note that (i) guarantees the uniqueness of the above y0 (z)
and y1 (z). Condition (ii) can be usually relaxed to f (Cz) ∈ 1 + zZ[[z]] for some
positive integer C (without the scaling z 7→ Cz, many of the resulting formulae
look ‘more natural’). Property (iii) implies that the functional inverse z(q), the
so-called mirror map, also has integral expansion; furthermore, one consider q as a
new variable, at least in a neighbourhood of the origin.
   In fact, in [6], [3] we posed on 4th order differential equations1
                              y 0000 + P y 000 + Qy 00 + Ry 0 + Sy = 0              (71)
some extra conditions as well:
  (iv) the ‘Calabi–Yau’ or ‘self-duality’ condition
                               1       1            3       1
                               R=P Q − P 3 + Q0 − P P 0 − P 00 ,             (72)
                               2       8            4       2
         which determines the structure of the projective monodromy group; and
     1 Throughout this chapter we use the prime 0 for z-derivatives.
                             Arithmetic hypergeometric series                           25

   (v) the integrality of a related sequence of numbers N0 , N1 , . . . , known as instan-
       ton numbers in the physics literature; these arise as coefficients in the Lam-
       bert q-expansion of the so-called Yukawa coupling
                                         µ         ¶3    µ    Z            ¶
                                      N0     dq             1
                      K = K(q) := 2 q                 exp −     P (z) dz
                                      y0     dz             2
                                   ∞
                                   X   Nd d3 q d
                          = N0 +                 .
                                       1 − qd
                                   d=1

For a long time we have been confident that in all examples these additional con-
ditions (iv), (v) are satisfied automatically when (i)–(iii) hold. However we have
learnt recently from M. Bogner and S. Reiter [29] that the differential operator
    θ4 − 8z(2θ + 1)2 (5θ2 + 5θ + 2) + 192z 2 (2θ + 1)(2θ + 3)(3θ + 2)(3θ + 4)         (73)
satisfies conditions (i)–(iv) while condition (v) seems to fail. Therefore, the Calabi–
Yau equations of order 4 are characterised by all conditions (i)–(v). Furthermore,
the antisymmetric square of any 4th order Calabi–Yau equation is a linear differ-
ential equation of order 5; when it meets conditions (i)–(iii) above (and it is always
the case for all known examples, although this fact can be shown rigorously only
for some instances), we call it a Calabi–Yau equation of order 5.
    Our experimental search [6], [3] resulted in more than 400 examples of such
differential equations. The corresponding differential operators are of Calabi–Yau
type, since some of these examples can be identified with Picard–Fuchs differential
equations for the periods of 1-parameter families of Calabi–Yau manifolds. For an
entry in our table from [3], checking (i) and (iv) is trivial, (ii) usually follows from an
explicit form of the coefficients of f (z) (when it is available), while (iii) can be ver-
ified in certain cases using some of Dwork’s p-adic techniques. Substantial progress
in the latter direction was obtained recently by C. Krattenthaler and T. Rivoal [82],
[83].
    Basic examples of Calabi–Yau differential equations are given by the general
hypergeometric differential equation (2) of order m = 4 (and m = 5) satisfied by
the hypergeometric series (1). The equation (2) has (smallest possible) degree 1
in z and condition (i) forces b2 = · · · = bm = 1 to hold. This motivates count-
ing the Calabi–Yau equations and their analytic solutions as a natural arithmetic
generalisation of hypergeometric equations and series.
    Standard conjectures (see, e.g., [7]) predict that all Calabi–Yau differential oper-
ators in [3] should be of ‘geometric origin’, which means that they correspond (as
subquotients of local systems) to factors of Picard–Fuchs equations satisfied by
period integrals for some family of varieties over the projective line.
    The work [5] contains many explicit algebraic transformations between Calabi–
Yau differential equations and their solutions which can be thought of as higher-
dimensional generalisations of Theorem 7; examples are the transformation (3) from
the introduction and the transformation (98) below. In [5] a simple recipe is given
to diagnose when two Calabi–Yau equations are related by an algebraic transfor-
mation, as well as to write down the corresponding transformation explicitly.
    Another arithmetic feature of Calabi–Yau differential equations, which was first
addressed in [4] in its full generality, is calculation of the corresponding Apéry limits.
26                                          W. Zudilin

This notion originates from Apéry’s work on the irrationality of ζ(2) and ζ(3) which
we review in § 1.1, and is discussed in several papers in relation with 2nd and 3rd
order arithmetic differential equations and their modular parameterizations; the
basic references are [23], [24], [150] and [154]. A way to define the Apéry limit
for a given Calabi–Yau differential operator D is as follows. Consider the analytic
solution y0 (z) = f (z) ∈ 1+zZ[[z]] of the equation Dy = 0 and the (unique) analytic
solution f˜(z) ∈ z + z 2 Q[[z]] of the related inhomogeneous differential equation
Dỹ = z, and write the corresponding expansions
                               ∞
                               X                                  ∞
                                                                  X
                 f (z) = 1 +         un z   n
                                                and f˜(z) = z +         vn z n .
                               n=1                                n=2

Then the Apéry limit Ap(D) is defined by
                                                      vn
                                     Ap(D) := lim        .
                                                  n→∞ un

The notion is motivated by the fact that Apéry’s results (25)–(29) and (16)–(21)
imply
                  ¡           ¢ ζ(2)               ¡          ¢ ζ(3)
              Ap D(11, 3, −1) =            and Ap D̂(17, 5, 1) =
                                     5                              6
(cf. Table 2). It was observed in [4], with many examples proved there and in [150],
that the Apéry limits of Calabi–Yau differential operators happen to be the values
of certain L-series attached to quadratic characters and elliptic curves.
2.3. The family of Calabi–Yau quintics. In this section we review some basic
geometry hidden behind the Calabi–Yau differential equations.
   Let Mz be a family of Calabi–Yau threefolds parameterized by a complex variable
z ∈ P1 (C). Then periods of the unique holomorphic differential 3-form on Mz satisfy
a linear differential equation, called the Picard–Fuchs differential equation of Mz .
When the Hodge number h2,1 is equal to 1, the Picard–Fuchs differential equation
has order 4. One of the most well-known examples is perhaps the family of quintic
threefolds [40]

                  x51 + x52 + x53 + x54 + x55 − z −1/5 x1 x2 x3 x4 x5 = 0                 (74)

in P4 , whose Picard–Fuchs differential equation is
                                                                                   d
           θ4 y − 5z(5θ + 1)(5θ + 2)(5θ + 3)(5θ + 4)y = 0,                 θ=z        .   (75)
                                                                                   dz
This is one of the fourteen families of Calabi–Yau threefolds [3] whose Picard–Fuchs
differential equations are hypergeometric. Before discussing the special features of
this and other examples of very special arithmetic differential equations, let us
address much simpler instances with their classical links to the theory of modular
and hypergeometric functions.
   It is the classical result that the solution
                                          µ1 1 ¯ ¶
                                                ¯
                                           2, 2 ¯ z
                                     2 F1
                                             1 ¯
                                Arithmetic hypergeometric series                              27

of the Picard–Fuchs differential equation
                                         z
                                   θ2 y − (2θ + 1)2 y = 0
                                         4
for the family
                                  Ez : y 2 = x(x − 1)(x − z)
of elliptic curves (that is, of Calabi–Yau onefolds) satisfies
                                      µ1 1 ¯ 4 ¶
                                            ¯ϑ
                                       2, 2 ¯ 2  = ϑ23 ,
                                 2 F1
                                        1 ¯ ϑ43
                P        πiτ (n+1/2)2
                                                          P      πiτ n2
where ϑ2 (τ ) =    n∈Z e               and ϑ3 (τ ) =        n∈Z e       are modular forms
of weight 1/2. In other words, under a suitable setting, z becomes a modular
function and the holomorphic solution of the differential equation at z = 0 becomes
a modular form of weight 1 on the congruence subgroup Γ(2) of SL2 (Z). Likewise,
the solution                          µ1 1 3 ¯            ¶
                                        4 , 2 , 4 ¯¯
                                 3 F2                256z
                                          1, 1 ¯
of the Picard–Fuchs differential equation

                         θ3 y − 4z(4θ + 1)(4θ + 2)(4θ + 3)y = 0                             (76)

for the family
                     Kz : x41 + x42 + x43 + x44 − z −1/4 x1 x2 x3 x4 = 0
of K3 surfaces (that is, of Calabi–Yau twofolds) can be interpreted as a modular
form of weight 2 on Γ0 (2) under a suitable setting. Therefore, one might expect
that the holomorphic solution of (75) at z = 0 can be interpreted as a generalised
modular (or automorphic) form.
     To provide some evidence to the fact that the solutions of (75) and their deriva-
tives form a ‘richer’ algebraic structure, note [94], [104] that, in the classical case,
the modular form or function f (τ ) and its two successive derivatives f 0 (τ ) and
f 00 (τ ) are algebraically independent with q = e2πiτ over the field C(τ ), while all
further derivatives are algebraic over the field C(f (τ ), f 0 (τ ), f 00 (τ )). For example,
the ring of quasi-modular forms C[E2 (τ ), E4 (τ ), E6 (τ )], where

                                                  X∞
                                                       nq n
                                 E2 (τ ) = 1 − 24            ,
                                                  n=1
                                                      1 − qn
                                  ∞
                                  X                                      ∞
                                                                         X
                                    n3 q n                                 n5 q n
              E4 (τ ) = 1 + 240                  ,   E6 (τ ) = 1 − 504                  ,
                                  n=1
                                        1 − qn                           n=1
                                                                               1 − qn

is differentially stable [111], [169]:
               1                      1                      1
      Ė2 =      (E 2 − E4 ),    Ė4 =  (E2 E4 − E6 ), Ė6 = (E2 E6 − E42 ),                (77)
              12 2                    3                      2
                                              1 dE      dE
                                where Ė :=          =q    .
                                             2πi dτ     dq
28                                              W. Zudilin

   The first example of a non-linear differential equation of order 7 for the Yukawa
coupling was given in [89], while in [161] it was shown that no algebraic differential
equation with coefficients from C(q) of smaller order can be given. Note that
the equation from [89] is extremely lengthy, and only recently H. Movasati [99]
has managed to construct a very elegant system of non-linear differential equations
associated to the family of quintic threefolds (74) and its Picard–Fuchs equation (75)
which resembles Ramanujan’s system (77):
            µ                            ¶
          1 6 5           1            1
   Ṫ0 =         T +          T0 T3 − T4 ,
         T5 5 0        3125            5
            µ                                            ¶
          1           6       4                 1
   Ṫ1 =       −125T0 + T0 T1 + 125T0 T4 +          T1 T3 ,
         T5                                   3125
            µ                                                                    ¶
          1             7     1 5         4           2       1        2
   Ṫ2 =       −1875T0 − T0 T1 + 2T0 T2 + 1875T0 T4 + T1 T4 +              T2 T3 ,
         T5                   5                               5       3125
            µ                                                                  ¶
          1             8     1 5         4           3       1        3     2
   Ṫ3 =       −3125T0 − T0 T2 + 3T0 T3 + 3125T0 T4 + T2 T4 +              T ,
         T5                   5                               5       3125 3
            µ                       ¶
          1       4         1
   Ṫ4 =       5T0 T4 +        T3 T4 ,
         T5               625
         T6
   Ṫ5 =    ,
         T5
         µ                                                  ¶      µ               ¶
              72 8       24 4          3 3        2       2     T6     4     2
   Ṫ6 = − T0 −               T T3 − T0 T4 −            T     +     12T0 +       T3 ,
               5       3125 0          5      1953125 3         T5          625

where
                                                          dT
                                              Ṫ := 5q       .
                                                          dq
Namely, he proved in [99] the following result.
Theorem 8. A formal power series solution
                                     ∞
                                     X
                              Tj =         tj,n q n ,       j = 0, 1, . . . , 6,            (78)
                                     n=0

subject to the initial conditions
                              1                                                      1
                     t0,0 =     ,    t0,1 = 24,         t4,0 = 0,    t5,0 = −           ,
                              5                                                    3125
to the above system is unique. Furthermore, the quantity

            (T4 − T05 )2             q            22 q 2                d3 q d
        −                = 5 + 2875     + 609250         + · · · + N d         + ···
              625T53                1−q          1 − q2                1 − qd

is the Yukawa coupling for the family (74), and the functions (78) are algebraically
independent over C (in fact, over C(q, log q) as shown in [161]).
   The argument in both [161] and [99] of showing the algebraic independence of
the functions in question is relating them to the fundamental solution of the linear
                              Arithmetic hypergeometric series                         29

differential equation (75) and using the monodromy structure of the equation. The
latter problem was addressed in several papers on the subject: it is known [26] that
the Zariski closure of the projective monodromy group of (75) but also of other 4th
order differential equations is Sp4 (C) (this is a consequence of (72)); what is a ‘nice’
choice of a basis of solutions with respect to which the monodromy matrices are
in Sp4 (C)? A possible choice of such basis is constructed in [41] for all arithmetic
hypergeometric differential equations. For example, it is shown in [41] that one can
choose the symplectic matrices
                                                           
                          1 1 0 0                     1 0 0 0
                        0 1 0 0                            
                                       and 0 1 0 1                              (79)
                        5 5 1 0                   0 0 1 0
                          0 −5 −1 1                   0 0 0 1
as the monodromy matrices around the singular points z = 0 and z = 1/3125
of (75). Note that the group generated by (79) is contained in the congruence
subgroup                                               
                 
                                     1 ∗ ∗ ∗             
                                                          
                                    0 1 ∗ ∗            
                                     
                   γ ∈ Sp4 (Z) : γ ≡            (mod 5)
                 
                                     0 0 1 0            
                                                          
                                                         
                                      0 0 ∗ 1
of finite index in Sp4 (Z), and it was discovered numerically that similar finite-index
congruence subgroups of Sp4 (Z) contain monodromy groups for the majority of
other Calabi–Yau differential equations. This observation forms grounds for asking
whether one can relate the functions like (78) coming from mirror symmetry to
Siegel modular forms of degree 2 or, more generally, to non-holomorphic modular
forms of degree 2. In the next section we review some partial results in this direction
discussed in [151].
2.4. Sp4 modularity. Consider a Calabi–Yau differential equation of order 4.
Its projective monodromy group Γ ⊂ Sp4 (R) is commensurable with a discrete
subgroup of Sp4 (Z) (of not necessarily finite index), therefore one can gather its
fundamental matrix solution
                                                   
                                 u3 u03 u003 u000
                                                3
                               u2 u02 u002 u000    
                                               2 
                               u1 u1 u1 u1 
                                       0   00   000

                                 u0 u00 u000 u000
                                                0

in such a way that the basis u0 , u1 , u2 , u3 satisfies
                               W (u0 , u2 ) + W (u1 , u3 ) = 0                       (80)
and the monodromy matrices are in Γ. Here the notation W (u0 , u1 ) := u0 u01 − u00 u1
stands for the wronskian. Introduce the functions
       wjl = CzW (uj , ul ) = Cz(uj u0l − u0j ul ),   wjl = −wlj ,   0 ⩽ j, l ⩽ 3,
where C 6= 0 is a certain normalization constant. Thanks to (80) we have a linear
relation w02 + w13 = 0; there is also a quadratic relation
                            w01 w23 + w02 w13 + w03 w12 = 0,
30                                           W. Zudilin

which is tautological in terms of the uj s. The five linearly independent functions

                         w01 ,     w02 = −w13 ,     w03 ,   w12 ,   w23

form a solution to a fifth order linear differential equation (the so-called antisym-
metric square) with the monodromy conjugate to a subgroup commensurable to a
discrete subgroup of O5 (Z) ≃ Sp4 (Z). This establishes the correspondence between
Calabi–Yau differential equations of order 4 and 5.
   If we now define the functions
                         w03                    w02   −w13                    −w12
             τ1 (z) :=       ,      τ2 (z) :=       =      ,    τ3 (z) :=          ,   (81)
                         w01                    w01   w01                      w01
and collect them in the symmetric matrix
                              µ      ¶
                               τ1 τ2                           w23
                         T :=          ,             det T =       ,                   (82)
                               τ2 τ3                           w01

then it is routine to verify that monodromy matrices γ ∈ Γ define the standard
Sp4 -action on T:
                                                        µ      ¶
                                     −1                   A B
          γ : T 7→ (AT + B)(CT + D) = γT       for γ =           ∈ Γ.
                                                          C D

In this record, A, B, C and D are 2×2 components of the 4×4 matrix γ from Sp4 (R).
Note that the differential Galois theory [161] implies the algebraic independence of
the three entries (81) of T = T(z) over C(z).
   The multivalued function τ := τ1 (z) takes values in a certain domain H ⊂ C.
Viewing T as a matrix-valued function of τ , we say that a function f (T(τ )) : H → C
is a Γ-modular form of weight k if
                                                            µ      ¶
                                   k                          A B
            f (γT) = det(CT + D) · f (T)       for all γ =            ∈ Γ.
                                                              C D

This definition is motivated by the facts [151] that the inverse z = z(T(τ )) of the
map τ = τ1 (z) in (81), (82) is a Γ-modular form of weight 0, while the function
w01 viewed as a function of T = T(τ ) is a Γ-modular form of weight 1. Note that
the z-derivatives of the mirror map t(z) = u1 (z)/u0 (z) of the starting 4th order
Calabi–Yau equation and also of the function τ (z), which is the mirror map of the
resulting 5th order Calabi–Yau equation, admit simple formulae

                                 dt   w01          dτ1     u20
                                    =      ,           =                               (83)
                                 dz   Cu20         dz          2
                                                         Cg0 w01

expressing them via the analytic solutions u0 and w01 of the equations. These
relations in turn imply that
                                    Z τ                         Z τ
           τ1 (τ ) = τ, τ2 (τ ) = −     t(τ ) dτ, and τ3 (τ ) =     t(τ )2 dτ, (84)
                                         0                                0

when we view T as a function of τ .
                             Arithmetic hypergeometric series                         31

   An unfortunate thing about the Sp4 -modularity above is the fact that the imag-
inary part of T is indefinite and, thus, is not in the Siegel upper half-space. This
was observed by geometric consideration in [1]; instead, M. Aganagic, V. Bouchard
and A. Klemm [1] define the non-holomorphic embedding
                              µ ¶                                          µ ¶
                     2i         t                                            t
    Z = Z(τ ) = T +     Im T       (t 1) Im T,      where φ = (t 1) Im T        .
                     φ          1                                            1

Then we indeed have Z(τ ) ∈ H2 for all τ , as well as
                                                                   µ     ¶
                                          −1                       A B
          γ : Z 7→ (AZ + B)(CZ + D)            = γZ     for   γ=             ∈ Γ;
                                                                   C D

in addition, the function w = φ · w0 satisfies

                               γ : w 7→ det(CZ + D) · w.                            (85)

   There are at least two recipes to construct non-holomorphic modular forms
w(Z) defined on H2 which satisfy (85) for γ from the full modular group Sp4 (Z):
one can use theta series attached to indefinite quadratic forms [114] or Eisenstein
series [91; Chapter 18]. Below we outline a possible strategy of pulling back suit-
able non-holomorphic forms so constructed to the objects on the one-dimensional
domain of definition, on the example of trivial Yukawa coupling and action of a
finite-index subgroup Γ0 ⊂ PSL2 (Z) on τ = x + iy ∈ H1 (that is, y > 0). This case
corresponds to the equality t = τ of two mirror maps.
   If t = τ , then formulae (84) imply
         µ                   ¶               µ                ¶     µ                 ¶
              τ     − 12 τ 2                     x    − 12 x2     i   y    −xy
T(τ ) =                        , Z(x + iy) =                    +                       ,
           − 12 τ 2 31 τ 3                    − 12 x2 13 x3       2 −xy x2 y + 13 y 3

since φ = − 43 y 3 . We also have

                         1 2 2                           1 4    1
              det Z =      τ |τ |   and    det Im Z =      y =    (Im τ )4 .
                        12                              12     12
A slightly different version of the embedding was discovered independently by
D. Zagier [153]. The related embedding of SL2 (R) into Sp4 (R),
                            2                                       
                µ     ¶      a d + 2abc −3a2 c abd + 12 b2 c 12 b2 d
                  a b       −a2 b        a3      − 12 ab2   − 16 b3 
             ι:         7→ 
                           4acd + 2bc2 −6ac2 ad2 + 2bcd bd2  ,
                                                                     
                  c d
                                6c2 d    −6c3      3cd2        d3

shows that certain arithmetic conditions on Γ0 (for example, b ≡ 0 (mod 6))
maps Γ0 into a subgroup of Sp4 (Z). If we now take an arbitrary Γ0 -modular form
w0 (τ ) of weight 4, then the corresponding function w(x + iy) = − 43 y 3 · w0 (x + iy)
satisfies (85) restricted to the curve
                           ½µ                                          ¶        ¾
                                  x + 2i y        − 12 x2 − 2i xy
       {Z(τ ) : τ ∈ H1 } =                                               : y > 0 ⊂ H2 .
                              − 12 x2 − 2i xy 13 x3 + 2i x2 y + 6i y 3
32                                                                 W. Zudilin

Thus, if one starts with a function w(Z) which obeys the transformation law (85)
it is a¡ technical
            ¢      issue to determine under which conditions the pullback w0 (τ ) =
   3
− 4 w Z(τ ) /(Im τ )3 defined on H1 is holomorphic (or meromorphic) in H1 .
    In the general case of t 6= τ the situation seems to be more delicate because of the
transcendental relation between τ and t. Nevertheless, knowledge of explicit power
series expansions for both τ and t leaves a hope to consider possible pullbacks in
such cases as well.

2.5. Ramanujan-type formulae for 1/π 2 . There is almost no mystery left
about classical Ramanujan’s formulae for 1/π, like (4)–(6) and their numerous
generalisations; the reader is advised to consult the monograph [30] as well as the
recent surveys [16] and [181]. A remarkable thing about the formulae is not only the
obvious appearance of the hypergeometric series on the left-hand side but also the
existence of a purely hypergeometric machinery [51], [65], [67] which enables one to
prove some of these identities. This is the Wilf–Zeilberger (WZ) theory [105], [149]
with the algorithm of creative telescoping as its part. Even this approach does not
cover the whole variety of formulae for 1/π (although algebraic transformations like
we have in Theorem 7 significantly extend its applicability), there are some further
surprising outcomes of the method. J. Guillera [65]–[68] has managed to apply the
WZ theory for proving new generalisations of Ramanujan-type series, namely,

                                         ∞
                                         X ( 1 )5n                                  (−1)n   8
                                                      2
                                                          5
                                                            (20n2 + 8n + 1)            2n
                                                                                          = 2,               (86)
                                         n=0
                                             n!                                      2     π
                            ∞
                            X ( 1 )5n                                               (−1)n  128
                                         2
                                              5
                                                (820n2 + 180n + 13)                   10n
                                                                                          = 2,               (87)
                            n=0
                                n!                                                   2      π
                   ∞
                   X ( 1 )3n ( 1 )n ( 3 )n                                          1   32
                             2            4           4
                                                                  (120n2 + 34n + 3) 4n = 2 ,                 (88)
                  n=0
                                         n!5                                       2    π
                   X∞
                        ( 12 )3n ( 31 )n ( 32 )n      2            33n   48
                                      5
                                                 (74n   + 27n + 3)   3n
                                                                        = 2.                                 (89)
                    n=0
                                  n!                               4     π

Furthermore, this newer pattern of formulae for 1/π 2 suggested Guillera [66] and
Guillera and Almkvist [2] to discover numerically seven additional formulae:

                ∞                                                                                          √
                X ( 1 )n ( 1 )n ( 3 )n ( 1 )n ( 5 )n                                           (−1)n
                                                                                                     ? 256   3
                        2            4            4           6        6
                                                                           (1640n2 + 278n + 15) 10n =          ,
                n=0
                                              n!5                                               2       3π 2

                                                                                                             (90)
                      ∞
                      X ( 1 )n ( 1 )n ( 3 )n ( 1 )n ( 2 )n                     (−1)n ? 48
                                 2            4           4        3       3
                                                                               (252n2 + 63n + 5)
                                                                                     = 2 , (91)
                   n=0
                                           n!5                                  48n    π
                 ∞                                                                        √
                X   ( 21 )n ( 13 )n ( 32 )n ( 61 )n ( 56 )n                    (−1)n ? 128 5
                                                                  2
                                                            (5418n + 693n + 29) 3n =         ,
                n=0
                                     n!5                                        80       π2
                                                                                                             (92)
                                         Arithmetic hypergeometric series                                       33

              ∞
              X ( 1 )n ( 1 )n ( 2 )n ( 1 )n ( 5 )n
                     2       3       3       6     6                2        (−1)n 36n ? 384
                                                         (1930n + 549n + 45)           = 2,
              n=0
                                     n!5                                       212n      π
                                                                                                              (93)
                          ∞
                          X ( 1 )n ( 1 )n ( 2 )n ( 1 )n ( 5 )n                            36n ? 375
                                     2      3     3      6      6
                                                                        (532n2 + 126n + 9) 6n =      ,
                          n=0
                                                  n!5                                     5     4π 2
                                                                                                              (94)
                      ∞                                                                                   √
                      X   ( 21 )n ( 18 )n ( 38 )n ( 58 )n ( 78 )n                      1 ? 56 7
                                               5
                                                                  (1920n2 + 304n + 15) 4n =   2
                                                                                                ,
                      n=0
                                           n!                                         7     π
                                                                                                              (95)
 ∞
 X   ( 12 )3n ( 13 )n ( 23 )n ¡                                        ¢       ? 3
                   5
                               (32 − 216φ)n2 + (18 − 162φ)n + (3 − 30φ) (3φ)3n = 2 , (96)
 n=0
               n!                                                                π

where                                     µ√            ¶5
                                                 5−1
                                 φ=                          = 0.09016994 . . . .
                                                  2
Note that the latter constant appears in the asymptotics of Apéry’s approximations
to ζ(2) (cf. (28) and (29) in § 1.1).
   There exists also the ‘3D’ identity
                         ∞
                         X ( 1 )7n                                1 ? 32
                                 2
                                         (168n3 + 76n2 + 14n + 1) 6n = 3
                         n=0
                                 n!7                             2    π

discovered by B. Gourevich in 2002 (using an integer relations algorithm), and the
most recent news is the formula
       ∞
       X ( 1 )7n ( 1 )n ( 3 )n                                                                 ?   2048
             2
                   9
                    4
                      12n
                         4
                                 (43680n4 + 20632n3 + 4340n2 + 466n + 21) =
      n=0
                 n! 2                                                                               π4

due to J. Cullen [44].
   The works [2], [69], and [151] discuss a relationship of identities (86)–(96) with
the Calabi–Yau differential equations from Section 2.2. A standard example here,
related to Guillera’s formulae (86) and (87), is the hypergeometric series
                            µ1 1 1 1 1 ¯          ¶ X  ∞ µ      ¶5
                               ,   ,  ,  ,  ¯ 10             2n
                F (z) = 5 F4 2 2 2 2 2 ¯¯ 2 z =                    zn,
                                1, 1, 1, 1                    n
                                                      n=0

which satisfies the 5th-order linear differential equation
                    ¡ 5              ¢                                                  d
                     θ − 32z(2θ + 1)5 Y = 0,                             where θ = z       .
                                                                                        dz
If G(z) is another solution of the latter equation of the form F (z) log z + F1 (z) with
F1 (z) ∈ zQ[[z]], then
                                                                        µ        ¶1/2
                                                                     F G
                           Fe(z) = (1 − 2 z)       10    −1/2
                                                                det
                                                                    θF θG
34                                         W. Zudilin

satisfies the 4th-order equation
     ¡ 4                                                           ¢
      θ − 16z(128θ4 + 256θ3 + 304θ2 + 176θ + 39) + 220 z 2 (θ + 1)4 Y = 0,                  (97)

which is entry #204 in the tables [3]. For a quadratic transformation of the new
function Fe(z) one has the following explicit formula [5]:
                        µ          ¶ X ∞ µX
                                          n      µ ¶2 µ        ¶¶2
              1+z e          −z               n−k 2k   2n − 2k
                      F             =       4                      zn,                      (98)
             (1 − z)2     (1 − z)2    n=0
                                                   k    n − k
                                                  k=0

where the right-hand side is the Hadamard square of the series
                        µ1      ¯         ¶       ∞ µ   ¶2
            1                 1 ¯−16z             X  2n    (−1)n z n
                         2,   2 ¯
                 2 F1          ¯              =
         1 − 16z              1 1 − 16z             n    (1 − 16z)n+1
                                                n=0
                                                X∞ µX
                                                    n       µ ¶2 µ           ¶¶
                                                        n−k 2k       2n − 2k
                                              =       4                        zn
                                                n=0
                                                              k       n − k
                                                        k=0

which admits a modular parametrization. Both the 4th-order equation (97) and the
differential equation (of order 4) for the right-hand side in (98) are of Calabi–Yau
type. The underlying Calabi–Yau differential equations are crucial in the numerical
discovery of several formulae for 1/π 2 ; the details can be found in [2].
   A more ‘delicate’ outcome of the WZ-theoretic approach are functional identities
that include the numerical evaluations as specialisations. The anticipated advantage
of functional instances is their ‘easier’ provability because additional functional (for
example, differential) equations can be used. There are several ad hoc methods in
passing from numerics to functions; many of them rest on a tricky application of
the Gosper–Zeilberger algorithm of creative telescoping [105].
   Examples related to Ramanujan’s series (4) and Guillera’s series (86) can be
found in [67]. Consider
        ∞
        X (a + 1 )3n ¡
                  2
                                    ¢ 1
                    3
                      6(n  + a) + 1  · n
        n=0
            (a + 1) n                  4
                           µ                ¶            ∞
                 4a+1        Γ(a + 1)Γ( 12 ) 3   (4a)2 X ( 12 )n (a + 12 )n
             =           ·                     +                                            (99)
               π cos2 πa        Γ(a + 12 )       2a − 1 n=0 (a + 1)n ( 32 − a)n

and, denoting an either side of the latter expression by f (a),

     X∞
         (a + 12 )5n ¡          2
                                                    ¢ (−1)n
                      20(n  + a)  + 8(n  +  a) +  1  ·
     n=0
         (a + 1)5n                                       4n
                          µ                ¶                   ∞
                 2          Γ(a + 1)Γ( 12 ) 2           25 a3 X ( 12 )2n (a + 12 )n
          =             ·                     f (a) +                                  .   (100)
            π cos πa          Γ(a + 12 )               2a − 1 n=0 (a + 1)2n ( 32 − a)n

The specialisation a = 0 of (99) and (100) gives the numerical identities (4) and
(86), respectively.
                                  Arithmetic hypergeometric series                             35

   Another striking arithmetic hidden in Ramanujan’s formulae for 1/π and their
generalisations relies on the so-called supercongruences. It happens that if we
truncate the corresponding hypergeometric series at n = p − 1, we always get
congruences modulo high powers of p, where p > 3 is a prime not dividing the
denominator of the argument. For example,
              p−1 1
              X                                        µ    ¶
                 ( )n ( 1 )n ( 3 )n            (−1)n     −1
                      2      4    4
                                      (20n + 3) 2n ≡ 3       p            (mod p3 ),
              n=0
                            n!3                 2        p
              p−1
              X   ( 12 )3n ( 14 )n ( 43 )n                   1
                                5
                                           (120n2 + 34n + 3) 4n ≡ 3p2     (mod p5 ),
              n=0
                            n!                              2
 p−1 1 7 1
 X  ( )n ( )n ( 3 )n                                                          ?
      2
            9
             4
               12n
                  4
                          (43680n4 + 20632n3 + 4340n2 + 466n + 21) ≡ 21p4              (mod p9 ).
n=0
          n! 2

The known proofs [71], [137], [183] makes use of the Wilf–Zeilberger theory again.
The work [70] discusses the general pattern for all such supercongruences, including
finite analogues for ‘irrational’ Ramanujan-type identities like (96).

                          3. Lattice sums and Mahler measures
3.1. Dirichlet L-series and Mahler measures. For a Laurent polynomial
P (x1 , . . . , xn ), the Mahler measure M (P ) := em(P ) , with m(P ) defined in (9),
is the geometric mean of |P | on the torus

                      Tn = {(x1 , . . . , xn ) ∈ Cn : |x1 | = · · · = |xn | = 1}.

Mahler’s original definition [93] refers to the case n = 1 where one has a different
expression
                                           Xd
                       m(P ) = log |a0 | +     max{0, log |αj |}
                                                  j=1
                                      Qd
for a polynomial P (x) = a0 j=1 (x − αj ), as a consequence of classical Jensen’s
formula. For polynomials P (x) with integer coefficients, clearly m(P ) ⩾ 0, with
m(P ) = 0 only if P is monic (a0 = 1) and has all its zeros inside the unit circle
(hence is a product of a monomial xa and a cyclotomic polynomial, by Kronecker’s
theorem). D. Lehmer [88] asked (already in 1933) whether m(P ) can be arbitrary
small but positive for P (x) ∈ Z[x]; the smallest value he was able to find was

m(x10 + x9 − x7 − x6 − x5 − x4 − x3 + x + 1) = log(1.17628081 . . . ) = 0.16235761 . . . .

This still stands as the smallest positive value of m(P ), in spite of extensive com-
putation by D. Boyd, M. Mossinghoff and others. Although Lehmer’s question is a
completely different story in the study of Mahler measures, it motivated the above
definition of m(P ) to the multi-variable case because of the following limit formula
proven by Boyd in 1981 [33]:

                            m(P (x, xN )) → m(P (x, y)) as N → ∞.
36                                      W. Zudilin

  It was not realised until 1981 that the n-variable Mahler measure could have
some ‘geometric’ roots. Namely, C. Smyth gave an elegant formula [33]
                                   √
                                  3 3
                  m(1 + x + y) =      L(χ−3 , 2) = L0 (χ−3 , −1)         (101)
                                   4π
where
                                ∞
                                X χ−3 (n)            1    1   1
                 L(χ−3 , s) =                 =1−       + s − s + ···
                                n=1
                                      ns             2s  4   5
is the L-function attached to the real odd Dirichlet character modulo 3.
    The proof of Smyth’s formula is worth noting here. Since 1 + x + y is a linear
function of y, Jensen’s formula applied to one of the integrals in (9) shows that
                                       Z 2π                         Z 2π/3
                               1                +    it         1
m(1 + x + y) = m(1 − x + y) =                 log |e − 1| dt =               log |eit − 1| dt
                              2π        0                      2π     0

where log+ x = max{0, log x}. Thus, m(1 + x + y) is given by a special value of the
Clausen integral
                              Z θ                  ∞
                                                   X
                                        it             sin(kθ)
                 Cl2 (θ) = −      log |e − 1| dt =             ,
                               0                          k2
                                                          k=1

and the result follows.
   A similar computation applies to many polynomials P (x, y) = A(x)y + B(x) if
A(x) and B(x) are cyclotomic and if the solutions of |A(x)| = |B(x)| on |x| = 1 are
roots of unity. For example [34],
                                            2
                   m(1 + x + y − xy) =        L(χ−4 , 2) = L0 (χ−4 , −1),
                                            π

where L(χ−4 , 2) = G is Catalan’s constant (cf. (13)),

                                       3 0
                   m(1 + x + x2 + y) =   L (χ−4 , −1),
                                       2
                                       3
                  m(1 + x + y + x2 y) = L0 (χ−3 , −1).
                                       2
   Later V. Maillot and J. Cassaigne [95] derived a general formula for m(a0 +a1 x+
a2 y), for arbitrary complex aj , by means of the Bloch–Wigner dilogarithm
                                  µX
                                   ∞                        ¶
                                     zn
                       D(z) = Im        + log |z| log(1 − z) .
                                 n=1
                                     n2

If |a0 |, |a1 | and |a2 | are the lengths of the sides of a planar triangle opposite the
angles α0 , α1 and α2 , then
                                                                             µ           ¶
                              α0             α1             α2            1    |a1 | iα2
    m(a0 + a1 x + a2 y) =        log |a0 | +    log |a1 | +    log |a2 | + D         e    ;
                               π             π              π             π    |a0 |
                              Arithmetic hypergeometric series                          37

in the alternative case,

                    m(a0 + a1 x + a2 y) = log max{|a0 |, |a1 |, |a2 |}.

Already this result shows a strong connection of Mahler measure evaluation with
K-theory. That is why it is not completely mysterious to expect that more sophisti-
cated polynomials P (x, y) give rise to analogous Mahler measures expressed through
special values of L-functions of elliptic curves. Here the counterpart to

                              d3/2 L(χ−d , 2)
                                              = L0 (χ−d , −1)
                                    4π
is given by
                                       N L(E, 2)
                              bE =               = L0 (E, 0)
                                          4π 2
where N is the conductor of the elliptic curve E and where the latter equality is
only valid if E is a modular curve (that is, a smooth cubic curve over Q that has a
rational point; the Shimura–Taniyama conjecture — the theorem now — says that
all elliptic curves over Q are modular). In other words, there exist polynomials
PE (x, y) for which m(PE )/bE is (presumably) rational. Without explaining deep
K-theoretic reasons for such formulae to exist, we provide some hints on Deninger’s
example (12) mentioned in the introduction.
   Consider
                                               1       1
                           P (x, y) = 1 + x + + y + .
                                               x       y
Let x = eit and treat P (x, y) as a polynomial in y to see that

           |P (x, y)| = |1 + y(1 + 2 cos t) + y 2 | = |(y − y1 (t))(y − y2 (t))|,
                      √
where y1 (t) = −b − b2 − 1 with b = b(t) = 12 + cos t. With the help of Jensen’s
formula,                                Z
                                      1 π
                             m(P ) =         log+ |y1 (t)| dt.
                                      π 0
Since the product of the roots y1 (t) and y2 (t) is 1, we will have |y1 (t)| > 1 > |y2 (t)|
exactly when the roots are real and unequal, that is, when cos t > 12 , so |t| < π3 .
Thus
                                  Z π/3           p
                        m(P ) =         log(b + b2 − 1) dt.
                                       0

This integral can be integrated numerically but, of course, there are various other
ways to represent it, for example,
                              Z 2π Z 2π
                        1
              m(P ) =                      log(1 + 2 cos t + 2 cos s) dt dt
                      (2π)2     0      0
                                µ1         ¯
                                       1 1¯ 1
                                                  ¶        ∞ µ
                                                           X    ¶2
                      1             2, 2, 2¯
                                                              2k (1/16)2k+1
                     = · 3 F2                         =4                      ,
                      4              1, 32 ¯ 16                  k   2k + 1
                                                           k=0
38                                                W. Zudilin

the result we mentioned in (11). In a similar fashion, one can also derive a more
general hypergeometric representation [120], [86], [123]
                                                      µ1 1 1 ¯ 2 ¶
                                           α             , , ¯α
              m(α + x + x + y + y ) = Re 3 F2 2 2 2 ¯¯
                          −1        −1
                                                                             (102)
                                            4            1, 1  16
when α > 0.
   On the other hand, using a cohomological interpretation of m(P (x, y)), Deninger
[47] was able to evaluate this Mahler measure as an Eisenstein–Kronecker series of
the elliptic curve E of conductor 15 given by
                                                    1      1
                                        1+x+          + y + = 0,
                                                    x      y
and then assuming a conjecture of Beilinson, to derive that one should have
                                                15
                               m(P ) = r           2
                                                     L(E, 2) = rL0 (E, 0),
                                              (2π)
where r is a rational number (unspecified in Beilinson’s conjecture). Finally, it was
checked numerically that r = 1.00000000 . . . (up to 200 decimal places), so that
presumably P(10)  holds. The modularity theorem implies that, for the L-function
             ∞
        = k=1 ak k −s attached to an elliptic curve E of conductor N , the function
L(E, s) P
          ∞
f (τ ) = k=1 ak q k , where q = e2πiτ , is a cusp form for the modular group Γ0 (N ).
In Deninger’s case N = 15, so that
                       ∞
                       X                  ∞
                                          Y
            f (τ ) =         ak q k = q         (1 − q m )(1 − q 3m )(1 − q 5m )(1 − q 15m ).
                       k=1                m=1

In view of Euler’s pentagonal number formula
                                          ∞
                                          Y                  X                     2
                       η(τ ) = q 1/24         (1 − q m ) =         (−1)n q (6n+1) /24
                                          m=1                n∈Z

and the hypergeometric evaluation above, the final formula can be stated as (12).
   It is remarkable that, in spite of the origin of formula (12), it does not involve
any Mahler measure: it is a (hypergeometric) single sum evaluation of a quadruple
lattice sum.
3.2. Quadruple lattice sums. Define

     F (a, b, c, d) = (a + b + c + d)2
                       X∞
                                             (−1)n1 +n2 +n3 +n4
                  ×          ¡                                                ¢
                                       2           2            2            2 2
                     nj =−∞ a(6n1 + 1) + b(6n2 + 1) + c(6n3 + 1) + d(6n4 + 1)
                 j=1,2,3,4

where the method of summation is
                                   ∞
                                   X                     M
                                                         X             M
                                                                       X
                                            = lim               ···            ,
                                                M →∞
                                 nj =−∞                n1 =−M         n4 =−M
                                j=1,2,3,4
                                      Arithmetic hypergeometric series                              39

and also set
                                          F (b, c) = F (1, b, c, bc).
   Many cases are known when F (a, b, c, d) can be (sometimes conjecturally) reduced
to a single sum, like                        µ1 1 1¯ ¶
                                   π2           , , ¯1
                        F (3, 5) =     · 3 F2 2 2 3 2 ¯¯
                                   15           1, 2 16
in the case of (12). Another conjectured evaluation, due to Boyd, which is now
settled in [124], is related to a conductor 20 elliptic curve and is equivalent to
                                  µ1 1 1 ¯          ¶             µ2 2 2 ¯         ¶
         25             √
                        3             , 3 , 3 ¯¯ 2     √
                                                       3             , 3 , 3 ¯¯ 2
             F (1, 5) = 2A · 3 F2   3                 + 4B · 3 F2  3                ,
                                      2 4 ¯                          4 5 ¯
        6π 2                          3, 3       27                  3, 3       27

where                             √
                                  3
                                      2Γ( 61 )Γ( 13 )Γ( 12 )              Γ3 ( 32 )
                             A=             √                  and B =              .
                                         8 3π 2                           16π 2
When more general lattice sums are considered, hypergeometric√ functions with
irrational arguments frequently appear. For instance, if φ = (1 + 5)/2, we have
                                         µ1 1 1 ¯ ¶                    µ2 2 2 ¯ ¶
       225                    A             , 3 , 3 ¯¯ 1   3B                   ¯ 1
                                                                        3, 3, 3 ¯
       √     F (1, 5, 5, 5) = √   · 3 F2
                                          3
                                            2 4 ¯        + p    · 3 F2   4 5 ¯      .
     32 5π 2                    φ           3, 3       φ                 3, 3     φ
                              3                            3
                                                             φ2

While it seems likely that equations for F (1, 5, 5, 5) and F (1, 5) = F (1, 1, 5, 5) both
arise as special cases of formulae for F (a, b, c, d), the exact nature of those formulae
remains unclear.
   A standard analytic strategy for proving hypergeometric evaluations is reduc-
tion of the quadruple lattice sum under consideration to a double sum and then
interpreting the double sum as a special value of an elliptic function. For instance,
                                                  ∞
                                                  X
                                             2                 (−1)n+k (2k + 1)
                       F (1, 5, 5, 5) = 16                                            .
                                                                   2 + 15(2k + 1)2 )2
                                                 n=−∞ ((6n + 1)
                                                  k=0

These sorts of transformations follow from well-known q-series results, and are quite
rare. The double sum is a consequence of the following corollary to the Jacobi triple
product:
             ∞
             Y                                    ∞
                                                  X                                     2   2
         2              3n          15n 3
     q             (1 − q )(1 − q       ) =             (−1)n+k (2k + 1)q (15(2k+1) +(6n+1) )/8 .
             n=1                                 n=−∞
                                                  k=0

Notice that this equation gives an example of a lacunary modular form, and only
in such cases the two-dimensional reduction can be achieved. The two-dimensional
lattice sums are then evaluated using Ramanujan’s theories of elliptic functions and
modular equations [11], [19]. Several of these calculations are quite involved.
   The finite amount of elliptic curves whose L-functions are related to four eta
products is given by the following list [96]. Suppose that EN is an elliptic curve of
conductor N , then L(EN , 2) = F (b, c) for the values of N and (b, c) given in Table 3.
40                                          W. Zudilin

                                         N         (b, c)
                                         11       (1, 11)
                                         14        (2, 7)
                                         15        (3, 5)
                                         20        (1, 5)
                                         24        (2, 3)
                                         27        (1, 3)
                                         32        (1, 2)
                                         36        (1, 1)

      Table 3. Correspondence L(EN , 2) = F (b, c) for elliptic curves EN of
      conductor N

Note that case N = 11 does not possess a known hypergeometric evaluation but is
expressed through the Mahler measure,

                   77                ¡
                       F (1, 11) = m   (1 + x)(1 + y)(1 + x + y) + xy),
                  4π 2

a result originally conjectured by Boyd and recently shown by F. Brunault [36]
using a K-theoretic argument.
   Finally comes the list of hypergeometric evaluations for the corresponding lattice
sums F (b, c) = L(EN , 2):
                                                 µ4 5                  ¯ ¶
        9              1               1              3 , 3 , 1, 1 ¯¯ 1
            F (1, 1) = log 54 −            4 F3                              ,
       2π 2            9              81                 2, 2, 2 ¯ 2
                                            µ3 3                 ¯       ¶
        16                          1             ,     , 1,  1  ¯ 1
            F (1, 2) = 2 log 2 + 4 F3 2 2                        ¯− ,
        π2                          8             2, 2, 2 ¯ 4
                                  µ1 1 1 ¯ ¶
         8               1                       ¯1
            F (1, 2) = √       F    2, 2, 2 ¯             ,
        π2                 2
                             3  2
                                      1, 2 ¯ 2
                                           3
                                              µ4 5                 ¯     ¶
        81                         1             3  , 3 , 1, 1 ¯¯ 1
            F (1, 3) = log 6 +         4 F3                           − ,
       4π 2                       108               2, 2, 2 ¯ 8
                                     µ1 1 1 ¯                ¶                 µ2 2 2 ¯     ¶
        25             √                  ,    ,       ¯ 2            √          ,  ,  ¯ 2
            F (1, 5) = 2A · 3 F2 3 2 3 4 3 ¯¯                   + 4B · 3 F2 3 4 3 5 3 ¯¯
                        3                                              3
                                                                                             ,
       6π 2                               3, 3            27                     3, 3    27
                                               µ4 5                  ¯    ¶
        40             5             1             3  , 3 , 1, 1 ¯¯ 27
            F (1, 5) = log 2 −           4 F3                                ,
       3π 2            3            16                 2, 2, 2 ¯ 32
                               µ1 1 1 ¯ ¶
         6             1           , , ¯1
            F (2, 3) = 3 F2 2 2 3 2 ¯¯                 ,
        π 2            2           1, 2          4
                                               µ3 3                 ¯ ¶
         24                          1               ,    , 1,  1   ¯1
            F (2, 3) = 3  log 2  −        F       2 2               ¯     ,
        π2                          32
                                        4    3
                                                     2, 2, 2 ¯ 4
                                               µ3 3                  ¯ ¶
        15             1              1            2  , 2 , 1, 1 ¯¯ 8
            F (2, 3) = log 18 − 4 F3                                       ,
        π2             2              9                2, 2, 2 ¯ 9
                                         µ3 3                 ¯        ¶
         9             1                       ,     ,  1,  1 ¯
            F (2, 3) = log 2 + 4 F3 2 2                       ¯ −8 ,
        π2             2                       2, 2, 2 ¯
                                 Arithmetic hypergeometric series                               41

                                µ1 1 1 ¯               ¶               µ2 2 2 ¯           ¶
         14                       3 , 3 , 3 ¯¯ 1                          3 , 3 , 3 ¯¯ 1
            F (2, 7) = A · 3 F2     2 4 ¯−                − B · 3 F2        4 5 ¯−          ,
        π2                          3, 3          27                        3, 3       27
                                            µ4 5              ¯     ¶
        49                        2             ,    , 1,  1  ¯ 27
            F (2, 7) = log 5 −         4 F3
                                               3 3            ¯        ,
       2π 2                     125              2, 2, 2 ¯ 125
                              µ1 1 1 ¯            ¶
        15             1        2 , 2 , 2 ¯¯ 1
            F (3, 5) = 3 F2                         ,
       4π 2            4          1, 32 ¯ 16
                                          µ3 3              ¯     ¶
        45                       2           2 , 2 , 1, 1 ¯¯ 16
            F (3, 5) = log 5 −       4 F3                          ,
       2π 2                     25             2, 2, 2 ¯ 25
                                              µ3 3              ¯     ¶
       165                          1             ,    , 1,   1 ¯ 1
            F (3, 5) = 4 log 2 −         4 F3
                                                 2 2            ¯       ,
       4π 2                        128             2, 2, 2 ¯ 16
                                         µ3 3             ¯       ¶
        75                      2          2 , 2 , 1, 1 ¯¯ 16
            F (3, 5) = log 3 + 4 F3                         −        .
       4π 2                     9            2, 2, 2 ¯ 9

All these Boyd’s evaluations corresponding to the entries in Table 3 are now rig-
orously established but this is far from exhausting the conjectures in Boyd’s com-
plete list [34], [35]. The ‘lacunary’ sums F (1, 1), F (1, 2) and F (1, 3) are settled
by F. Rodrı́guez-Villegas in [120]; A. Mellit has given a K-theoretic proof of the
formulae for F (2, 7) in [98]; the relations for F (1, 5), F (2, 3) and F (3, 5) are proved
in our joint papers [124], [125] with M. Rogers.
   The methods of [124], [125] are quite elementary in nature. One writes
                             Z 1
                                                          log q
          F (a, b, c, d) = −     η(aτ )η(bτ )η(cτ )η(dτ )       dq,    q = e2πiτ ,
                              0                             q
as                                             Z 1
                            F (a, b, c, d) =         x(q) log y(q) dz(q)
                                                0
where x(q), y(q) and z(q) are modular functions on a congruence subgroup of
SL2 (Z) (and this step can be usually achieved in several ways), and next express x
and y as algebraic functions of z, that is, x(q) = X(z(q)) and y(q) = Y (z(q)). The
substitution reduces F (a, b, c, d) to a complicated integral of elementary functions;
for example,
                                            p                    p3 (2 − p)
                                    Z 1/2    (1 − 2p)(2 − p) log
                               π                                  1 − 2p
               F (2, 3) = −                                2 √              dp.
                               48    0              (1 − p ) p

The final step is to reduce the elementary integral to Mahler measures. In order to
accomplish this reduction we use properties of hypergeometric functions and elliptic
functions. The machinery from [124], [125] allowed us to obtain different hyperge-
ometric expressions for F (1, 1) and F (1, 3) as well as to deduce a new functional
equation for the Mahler measure
                       ¡                           ¢
                     m (1 + x)(1 + y)(x + y) − αxy ,       α ∈ R.

All this reflects highly non-trivial identities between hypergeometric functions which
do not possess ‘purely hypergeometric’ proofs.
42                                     W. Zudilin

   There are plenty of results and conjectures for n-variable Mahler measures with
n > 2, mostly motivated by K-theoretic considerations. Besides (101), Smyth
established [33] that
                                                 7ζ(3)
                             m(1 + x + y + z) =        ,
                                                  2π 2
and Rodriguez-Villegas further discovered numerically [56] that
                               µ√   ¶5 Z 1
                           ?     15        ¡ 3      3         3     3
                                                                           ¢ log3 q
    m(1 + x + y + z + t) = −                η (3τ )η (5τ ) + η (τ )η (15τ )         dq,
                                2π      0                                      q
                           µ ¶3 Z 1
                         ?   3          2      2      2     2      log4 q
m(1 + x + y + z + t + w) =             η (τ )η (2τ )η (3τ )η (6τ )        dq.
                             π2     0                                 q

These evaluations are addressed in [122] and also in [31] in relation with short
random walks on the plane.

                                    Bibliography

  [1] M. Aganagic, V. Bouchard, and A. Klemm, “Topological strings and (almost)
      modular forms”, Comm. Math. Phys. 277:3 (2008), 771–819.
  [2] G. Almkvist and J. Guillera, “Ramanujan-like series for 1/π 2 and string theory”,
      Preprint at arXiv: 1009.5202 [math.NT], 2010.
  [3] G. Almkvist, C. van Enckevort, D. van Straten, and W. Zudilin, “Tables of
      Calabi–Yau equations”, Preprint at arXiv: math.AG/0507430, 2005–2010.
  [4] G. Almkvist, D. van Straten, and W. Zudilin, “Apéry limits of differential
      equations of order 4 and 5”, Modular Forms and String Duality, Fields Inst.
      Commun. Ser., vol. 54, Amer. Math. Soc. & Fields Inst., Providence, RI 2008,
      pp. 105–123.
  [5] G. Almkvist, D. van Straten, and W. Zudilin, “Generalizations of Clausen’s
      formula and algebraic transformations of Calabi–Yau differential equations”, Proc.
      Edinburgh Math. Soc. 54:2 (2011), 273–295.
  [6] G. Almkvist and W. Zudilin, “Differential equations, mirror maps and zeta
      values”, Mirror Symmetry V, AMS/IP Studies in Adv. Math., vol. 38, Amer.
      Math. Soc. & International Press, Providence, RI 2006, pp. 481–515.
  [7] Y. André, G-functions and geometry, Aspects Math., vol. E13, Friedr. Vieweg &
      Sohn, Braunschweig 1989.
  [8] G. E. Andrews, “Problems and prospects for basic hypergeometric functions”,
      Theory and application of special functions, Proc. Advanced Sem., Math.
      Res. Center (Univ. Wisconsin, Madison, WI, 1975), Math. Res. Center,
      Univ. Wisconsin, vol. 35 (R. A. Askey, ed.), Academic Press, New York 1975,
      pp. 191–224.
  [9] G. E. Andrews, “The well-poised thread: An organized chronicle of some amazing
      summations and their implications”, Ramanujan J. 1:1 (1997), 7–23.
 [10] G. E. Andrews, R. Askey, and R. Roy, Special functions, Encyclopedia Math.
      Appl., vol. 71, Cambridge Univ. Press, Cambridge 1999.
 [11] G. E. Andrews and B. C. Berndt, Ramanujan’s Lost Notebook. Part I,
      Springer-Verlag, New York 2005; Part II, Springer-Verlag, New York 2009.
 [12] R. Apéry, “Irrationalité de ζ(2) et ζ(3)”, Journées arithmétiques de Luminy
      (Luminy, 1978), Astérisque, vol. 61, 1979, pp. 11–13.
                              Arithmetic hypergeometric series                             43

[13] W. N. Bailey, Generalized hypergeometric series, Cambridge Tracts in
     Math., vol. 32, Cambridge Univ. Press, Cambridge 1935; 2nd reprinted ed.,
     Stechert-Hafner, New York–London 1964.
[14] A. Baker and J. Coates, “Fractional parts of powers of rationals”, Math. Proc.
     Cambridge Philos. Soc. 77:2 (1975), 269–279.
[15] K. Ball et T. Rivoal, “Irrationalité d’une infinité de valeurs de la fonction zêta aux
     entiers impairs”, Invent. Math. 146:1 (2001), 193–207.
[16] N. D. Baruah, B. C. Berndt, and H. H. Chan, “Ramanujan’s series for 1/π: a
     survey”, Amer. Math. Monthly 116:7 (2009), 567–587.
[17] M. A. Bennett, “Fractional parts of powers of rational numbers”, Math. Proc.
     Cambridge Philos. Soc. 114:2 (1993), 191–201.
[18] M. A. Bennett, “An ideal Waring problem with restricted summands”, Acta Arith.
     66:2 (1994), 125–132.
[19] B. C. Berndt, Ramanujan’s notebooks. Part I, Springer-Verlag, New York 1985;
     Part II, Springer-Verlag, New York 1989; Part III, Springer-Verlag, New York
     1991; Part IV, Springer-Verlag, New York 1994; Part V, Springer-Verlag, New
     York 1998.
[20] M. J. Bertin, “Mesure de Mahler d’une famille de polynômes”, J. Reine Angew.
     Math. 569 (2004), 175–188.
[21] F. Beukers, “A note on the irrationality of ζ(2) and ζ(3)”, Bull. London Math.
     Soc. 11:3 (1979), 268–272.
[22] F. Beukers, “Fractional parts of powers of rationals”, Math. Proc. Cambridge
     Philos. Soc. 90:1 (1981), 13–20.
[23] F. Beukers, “Irrationality of π 2 , periods of an elliptic curve and Γ1 (5)”,
     Diophantine approximations and transcendental numbers (Luminy, 1982),
     Progr. Math., vol. 31, Birkhäuser, Boston, MA 1983, pp. 47–66.
[24] F. Beukers, “Irrationality proofs using modular forms”, Journées arithmétiques de
     Besançon” (Besançon, 1985), Astérisque, vol. 147-148, 1987, pp. 271–283.
[25] F. Beukers, “On Dwork’s accessory parameter problem”, Math. Z. 241:2 (2002),
     425–444.
[26] F. Beukers and G. Heckman, “Monodromy for the hypergeometric function
     n Fn−1 ”, Invent. Math. 95:2 (1989), 325–354.
[27] J.-P. Bézivin, “Indépendence linéaire des valeurs des solutions transcendantes de
     certaines équations fonctionnelles”, Manuscripta Math. 61:1 (1988), 103–129.
[28] J. W. Bober, “Factorial ratios, hypergeometric series, and a family of step
     functions”, J. London Math. Soc. (2) 79 (2009), 422–444.
[29] M. Bogner, Differentielle Galoisgruppen und Transformationstheorie für
     Calabi–Yau-Operatoren vierter Ordnung, Diploma-Thesis, Institut für Mathematik,
     Johannes Gutenberg-Universität, Mainz 2008.
[30] J. M. Borwein and P. B. Borwein, Pi and the AGM ; A study in analytic number
     theory and computational complexity, Wiley, New York 1987.
[31] J. M. Borwein, A. Straub, J. Wan, and W. Zudilin, “Densities of short uniform
     random walks”, Canad. J. Math. (to appear); Preprint at arXiv: 1103.2995
     [math.CA], 2011.
                                             P 1
[32] P. Borwein, “On the irrationality of       q n +r
                                                       ”, J. Number Theory 37 (1991),
     253–259.
[33] D. W. Boyd, “Speculations concerning the range of Mahler’s measure”, Canad.
     Math. Bull. 24:4 (1981), 453–469.
[34] D. W. Boyd, “Mahler’s measure and special values of L-functions”, Experiment.
     Math. 7:1 (1998), 37–82.
44                                       W. Zudilin

 [35] D. W. Boyd, “Mahler’s measure and invariants of hyperbolic manifolds”, Number
      theory for the millennium, I, A K Peters, Natick, MA 2002, pp. 127–143.
 [36] F. Brunault, “Version explicite du théorème de Beilinson pour la courbe
      modulaire X1 (N )”, C. R. Math. Acad. Sci. Paris 343:8 (2006), 505–510.
 [37] P. Bundschuh and K. Väänänen, “Arithmetical investigations of a certain infinite
      product”, Compositio Math. 91 (1994), 175–199.
 [38] P. Bundschuh and K. Väänänen, “Linear independance of q-analogues of certain
      classical constants”, Result. Math. 47 (2005), 33–44.
 [39] P. Bundschuh and W. Zudilin, “Rational approximations to a q-analogue of π
      and some other q-series”, Diophantine Approximation, Dev. Math., vol. 16,
      Springer-Verlag, Vienna 2008, pp. 123–139.
 [40] P. Candelas, X. C. de la Ossa, P. S. Green, and L. Parkes, “A pair of Calabi–Yau
      manifolds as an exactly soluble superconformal theory”, Nuclear Phys. B 359:1
      (1991), 21–74.
 [41] Y.-H. Chen, Y. Yang, and N. Yui, “Monodromy of Picard–Fuchs differential
      equations for Calabi–Yau threefolds”, with an appendix by C. Erdenberger, J.
      Reine Angew. Math. 616 (2008), 167–203.
 [42] G. V. Chudnovsky, “On the method of Thue–Siegel”, Ann. of Math. (2) 117:2
      (1983), 325–382.
 [43] D. V. Chudnovsky and G. V. Chudnovsky, “Approximations and
      complex multiplication according to Ramanujan”, Ramanujan revisited
      (Urbana-Champaign, IL, 1987), Academic Press, Boston, MA 1988, pp. 375–472.
 [44] J. Cullen, “Pi formula”, Preprint (December 2010).
 [45] E. Delaygue, “Critère pour l’intégralité des coefficients de Taylor des applications
      miroir”, J. Reine Angew. Math. (to appear); Preprint at arXiv: 0912.3776
      [math.NT], 2009.
 [46] F. Delmer and J.-M. Deshouillers, “The computation of g(k) in Waring’s
      problem”, Math. Comp. 54 (1990), 885–893.
 [47] C. Deninger, “Deligne periods of mixed motives, K-theory and the entropy of
      certain Zn -actions”, J. Amer. Math. Soc. 10:2 (1997), 259–281.
 [48] А. К. Дубицкас, “Оценка снизу величины k(3/2)k k”, УМН 45:1 (1990), 153–154;
      English transl., A. K. Dubitskas [A. Dubickas], “A lower bound on the value of
      k(3/2)k k”, Russian Math. Surveys 45:4 (1990), 163–164.
 [49] D. Duverney, “Irrationalité d’un q-analogue de ζ(2)”, C. R. Acad. Sci. Paris Sér. I
      Math. 321:10 (1995), 1287–1289.
 [50] R. Dvornicich and C. Viola, “Some remarks on Beukers’ integrals”, Number theory,
      Vol. II (Budapest, 1987), Colloq. Math. Soc. János Bolyai, vol. 51, North-Holland,
      Amsterdam 1987, pp. 637–657.
 [51] S. B. Ekhad and D. Zeilberger, “A WZ proof of Ramanujan’s formula for π”,
      Geometry, Analysis, and Mechanics (J. M. Rassias, ed.), World Sci. Publ., River
      Edge, NJ 1994, pp. 107–108.
 [52] P. Erdös, “On arithmetical properties of Lambert series”, J. Indiana Math. Soc.
      (N. S.) 12 (1948), 63–66.
 [53] L. Euler, “Variae observationes circa series infinitas”, Comm. Acad. Sci. Imp.
      Petropol. 9 (1737), 160–188; Reprint:, Opera Omnia Ser. I, vol. 14, Teubner,
      Berlin 1925, pp. 216–245.
 [54] L. Euler, “Meditationes circa singulare serierum genus”, Novi Comm. Acad. Sci.
      Petropol. 20 (1775), 140–186; Reprint, Opera Omnia Ser. I, vol. 15, Teubner,
      Berlin 1927, pp. 217–267.
                            Arithmetic hypergeometric series                          45

[55] S. R. Finch, Mathematical constants, Encyclopedia Math. Appl., vol. 94,
     Cambridge University Press, Cambridge 2003.
[56] S. R. Finch, “Modular forms on SL2 (Z)”, Preprint at http://algo.inria.fr/
     csolve/frs.pdf, 2005.
[57] S. Fischler, “Irrationalité de valeurs de zêta [d’après Apéry, Rivoal, ...]”,
     Astérisque 294 (2004), 27–62.
[58] S. Fischler and W. Zudilin, “A refinement of Nesterenko’s linear independence
     criterion with applications to zeta values”, Math. Ann. 347:4 (2010), 739–763.
[59] P. J. Forrester and M. L. Glasser, “Some new lattice sums including an exact result
     for the electrostatic potential within the Na Cl lattice”, J. Phys. A Math. Gen. 15
     (1982), 911–914.
[60] J. Franel, “On a question of Laisant”, L’intermédiaire des mathématiciens,
     vol. 1, Gauthier-Villars, Paris 1894, pp. 45–47; “On a question of J. Franel”,
     L’intermédiaire des mathématiciens, vol. 2, Gauthier-Villars, Paris 1895,
     pp. 33–35.
[61] G. Gasper and M. Rahman, Basic hypergeometric series, 2nd ed., Encyclopedia
     Math. Appl., vol. 96, Cambridge Univ. Press, Cambridge 2004.
[62] А. О. Гельфонд, Исчисление конечных разностей, 3-е изд., Наука, М. 1967;
     English transl., A. O. Gel’fond, Calculus of finite differences, Intern. Monographs
     Adv. Math. Phys., Hindustan Publishing Corp., Delhi 1971.
[63] M. L. Glasser, “Evaluation of lattice sums. IV. A five-dimensional sum”, J. Phys.
     A Math. Gen. 16 (1975), 1237–1238.
[64] R. L. Graham, D. E. Knuth, and O. Patashnik, Concrete mathematics. A
     foundation for computer science, 2nd ed., Addison-Wesley, Reading, MA 1994.
[65] J. Guillera, “Some binomial series obtained by the WZ-method”, Adv. in Appl.
     Math. 29:4 (2002), 599–603.
[66] J. Guillera, “About a new kind of Ramanujan-type series”, Experiment. Math.
     12:4 (2003), 507–510.
[67] J. Guillera, “Hypergeometric identities for 10 extended Ramanujan-type series”,
     Ramanujan J. 15:2 (2008), 219–234.
[68] J. Guillera, “A new Ramanujan-like series for 1/π 2 ”, Preprint at arXiv:
     1003.1915 [math.NT], 2010.
[69] J. Guillera, “A matrix form of Ramanujan-type series fo 1/π”, Gems in
     Experimental Mathematics, Contemp. Math., vol. 517 (T. Amdeberhan,
     L. A. Medina, and V. H. Moll, eds.), Amer. Math. Soc., Providence, RI 2010,
     pp. 189–206.
[70] J. Guillera, “Mosaic supercongruences of Ramanujan type”, Experiment. Math. (to
     appear); Preprint at arXiv: 1007.2290 [math.NT], 2010.
[71] J. Guillera and W. Zudilin, “Divergent” Ramanujan-type supercongruences”, Proc.
     Amer. Math. Soc. (to appear); Preprint at arXiv: 1004.4337 [math.NT], 2010.
[72] Л. А. Гутник, “Об иррациональности некоторых величин, содержащих ζ(3)”,
     УМН 34:3 (1979), 190; Acta Arith. 42:3 (1983), 255–264; English transl.,
     L. A. Gutnik, “On the irrationality of some quantities containing ζ(3)”, Eleven
     papers translated from the Russian, Amer. Math. Soc. Transl. Ser. 2, vol. 140,
     Amer. Math. Soc., Providence, RI 1988, pp. 45–55.
[73] A. J. Guttmann, “Lattice Green functions and Calabi–Yau differential equations”,
     J. Phys. A Math. Theor. 42:23 (2009), 232001, 6 pp.
[74] L. Habsieger, “Explicit lower bounds for k(3/2)k k”, Acta Arith. 106 (2003),
     299–309.
46                                     W. Zudilin

 [75] M. Hata, “Legendre type polynomials and irrationality measures”, J. Reine
      Angew. Math. 407:1 (1990), 99–125.
 [76] M. Hata, “A new irrationality measure for ζ(3)”, Acta Arith. 92:1 (2000), 47–57.
 [77] Т. Г. Хессами Пилеруд, “О линейной независимости векторов с
      полилогарифмическими координатами”, Вестник МГУ. Сер. 1. Матем.,
      мех., 1999, no. 6, 54–56; English transl., T. Hessami Pilehrood, “On the linear
      independence of vectors with polylogarithmic coordinates”, Moscow Univ. Math.
      Bull. 54:6 (1999), 40–42.
 [78] F. Jouhet et E. Mosaki, “Irrationalité aux entiers impairs positifs d’un q-analogue
      de la fonction zêta de Riemann”, Intern. J. Number Theory 6:5 (2010), 959–988.
 [79] C. Krattenthaler et T. Rivoal, Hypergéométrie et fonction zêta de Riemann, Mem.
      Amer. Math. Soc., vol. 186, Amer. Math. Soc., Providence, RI 2007, no. 875.
 [80] C. Krattenthaler and T. Rivoal, “An identity of Andrews, multiple integrals, and
      very-well-poised hypergeometric series”, Ramanujan J. 13 (2007), 203–219.
 [81] C. Krattenthaler and T. Rivoal, “On a linear form for Catalan’s constant”, South
      East Asian J. Math. Sci. 6:2 (2008), 3–15.
 [82] C. Krattenthaler and T. Rivoal, “On the integrality of the Taylor coefficients of
      mirror maps”, Duke Math. J. 151:2 (2010), 175–218; “On the integrality of the
      Taylor coefficients of mirror maps. II”, Commun. Number Theory Phys. 3:3 (2009),
      555–591.
 [83] C. Krattenthaler and T. Rivoal, “Multivariate p-adic formal congruences and
      integrality of Taylor coefficients of mirror maps”, Théories galoisiennes et
      arithmétiques des équations différentielles, Séminaires et Congrès (L. Di Vizio
      and T. Rivoal, eds.), Soc. Math. France, Paris (to appear); Preprint at arXiv:
      0804.3049 [math.NT], 2008.
 [84] C. Krattenthaler, T. Rivoal et W. Zudilin, “Séries hypergéométriques basiques,
      q-analogues des valeurs de la fonction zêta et formes modulaires”, Inst. Jussieu
      Math. J. 5:1 (2006), 53–79.
 [85] J. Kubina and M. Wunderlich, “Extending Waring’s conjecture up to 471600000”,
      Math. Comp. 55 (1990), 815–820.
 [86] N. Kurokawa and H. Ochiai, “Mahler measures via crystalization”, Comment.
      Math. Univ. St. Pauli 54:2 (2005), 121–137.
 [87] M. N. Lalı́n and M. D. Rogers, “Functional equations for Mahler measures of
      genus-one curves”, Algebra Number Theory 1:1 (2007), 87–117.
 [88] D. H. Lehmer, “Factorization of certain cyclotomic functions”, Ann. of Math. (2)
      34:3 (1933), 461–479.
 [89] B. H. Lian and S.-T. Yau, “Differential equations from mirror symmetry”, Surveys
      in differential geometry: differential geometry inspired by string theory, Surv.
      Differ. Geom., vol. 5, Intern. Press, Boston, MA 1999, pp. 510–526.
 [90] F. Lindemann, “ Über die Zahl π”, Math. Ann. 20:2 (1882), 213–225.
 [91] H. Maass, Siegel’s modular forms and Dirichlet series, Lecture Notes in Math.,
      vol. 216, Springer-Verlag, Berlin–New York 1971.
 [92] K. Mahler, “On the fractional parts of powers of real numbers”, Mathematika 4:2
      (1957), 122–124.
 [93] K. Mahler, “An application of Jensen’s formula to polynomials”, Mathematika 7:2
      (1960), 98–100.
 [94] K. Mahler, “On algebraic differential equations satisfied by automorphic
      functions”, J. Austral. Math. Soc. 10 (1969), 445–450.
 [95] V. Maillot, Géométrie d’Arakelov des variétés toriques et fibrés en droites
      intégrables, Mém. Soc. Math. France (N. S.), vol. 80, Soc. Math. France, Paris
      2000.
                             Arithmetic hypergeometric series                          47

 [96] Y. Martin and K. Ono, “Eta-quotients and elliptic curves”, Proc. Amer. Math Soc.
      125:11 (1997), 3169–3176.
 [97] T. Matalo-Aho, K. Väänänen, and W. Zudilin, “New irrationality measures for
      q-logarithms”, Math. Comp. 75:254 (2006), 879–889.
 [98] A. Mellit, “Elliptic dilogarithms and parallel lines”, Preprint, 2009.
 [99] H. Movasati, “Eisenstein type series for Calabi–Yau varieties”, Preprint at arXiv:
      1007.4181 [math.AG], 2010.
[100] Ю. В. Нестеренко, “О линейной независимости чисел”, Вестник МГУ. Сер. 1.
      Матем., мех., 1985, no. 1, 46–54; English transl., Yu. V. Nesterenko, “Linear
      independence of numbers”, Moscow Univ. Math. Bull. 40:1 (1985), 69–74.
[101] Ю. В. Нестеренко, “Некоторые замечания о ζ(3)”, Матем. заметки 59:6
      (1996), 865–880; English transl., Yu. V. Nesterenko, “Some remarks on ζ(3)”,
      Math. Notes 59:6 (1996), 625–636.
[102] Ю. В. Нестеренко, “Модулярные функции и вопросы трансцендентности,”,
      Матем. сб. 187:9 (1996), 65–96; English transl., Yu. V. Nesterenko, “Modular
      functions and transcendence questions”, Sb. Math. 187:9 (1996), 1319–1348.
[103] Е. М. Никишин, “Об иррациональности значений функций F (x, s)”, Матем.
      сб. 109:3 (1979), 410–417; English transl., E. M. Nikishin, “Irrationality of values
      of functions F (x, s)”, Math. USSR Sb. 37:3 (1979), 381–388.
[104] K. Nishioka, “A conjecture of Mahler on automorphic functions”, Arch. Math. 53:1
      (1989), 46–51.
[105] M. Petkovšek, H. S. Wilf, and D. Zeilberger, A = B, A K Peters, Wellesley 1996.
[106] A. van der Poorten, “A proof that Euler missed... Apéry’s proof of the
      irrationality of ζ(3)”, Math. Intelligencer 1:4 (1978/79), 195–203.
[107] K. Postelmans and W. Van Assche, “Irrationality of ζq (1) and ζq (2)”, J. Number
      Theory 126 (2007), 119–154.
[108] M. Prévost, “A new proof of the irrationality of ζ(3) using Padé approximants”, J.
      Comput. Appl. Math. 67 (1996), 219–235.
[109] Ю. А. Пупырев, “О линейной и алгебраической независимости q-дзета-
      значений”, Матем. заметки 78:4 (2005), 608–613; English transl.,
      Yu. A. Pupyrev, “Linear and algebraic independence of q-zeta values”, Math.
      Notes 78:4 (2005), 563–568.
[110] Ю. А. Пупырев, “Эффективизация нижней оценки для k(4/3)k k”, Матем.
      заметки 85:6 (2009), 927–935; English transl., Yu. A. Pupyrev, “Effectivization
      of a lower bound for k(4/3)k k”, Math. Notes 85:6 (2009), 877–885.
[111] S. Ramanujan, “Modular equations and approximations to π”, Quart. J. Math.
      Oxford Ser. (2) 45 (1914), 350–372; Reprinted:, G. H. Hardy, P. V. Sechu Aiyar,
      and B. M. Wilson (eds.), Collected papers of Srinivasa Ramanujan, Cambridge
      University Press & Chelsea Publ., New York 1962, pp. 23–39.
[112] G. Rhin and C. Viola, “On a permutation group related to ζ(2)”, Acta Arith. 77:1
      (1996), 23–56.
[113] G. Rhin and C. Viola, “The group structure for ζ(3)”, Acta Arith. 97:3 (2001),
      269–293.
[114] O. Richter, “On transformation laws for theta functions”, Rocky Mountain J.
      Math. 34:4 (2004), 1473–1481.
[115] B. Riemann, “Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse”,
      Monatsberichte der Berliner Akademie, 1859; Reprint, Gesammelte Werke,
      Teubner, Leipzig 1892.
[116] T. Rivoal, “La fonction zêta de Riemann prend une infinité de valeurs
      irrationnelles aux entiers impairs”, C. R. Acad. Sci. Paris Sér. I Math. 331:4
      (2000), 267–270.
48                                      W. Zudilin

[117] T. Rivoal, Propriétés diophantiennes des valeurs de la fonction zêta de Riemann
      aux entiers impairs, Thèse de Doctorat, Univ. de Caen, Caen 2001.
[118] T. Rivoal, “Irrationalité d’au moins un des neuf nombres ζ(5), ζ(7), . . . , ζ(21)”,
      Acta Arith. 103 (2002), 157–167.
[119] T. Rivoal and W. Zudilin, “Diophantine properties of numbers related to
      Catalan’s constant”, Math. Ann. 326:4 (2003), 705–721.
[120] F. Rodrı́guez-Villegas, “Modular Mahler measures I”, Topics in number theory
      (University Park, PA, 1997), Math. Appl., vol. 467, Kluwer Acad. Publ.,
      Dordrecht 1999, pp. 17–48.
[121] F. Rodrı́guez-Villegas, “Identities between Mahler measures”, Number theory for
      the millennium, III, A K Peters, Natick, MA 2002, pp. 223–229.
[122] F. Rodrı́guez-Villegas, R. Toledano, and J. D. Vaaler, “Estimates for Mahler’s
      measure of a linear form”, Proc. Edinburgh Math. Soc. 47:2 (2004), 473–494.
[123] M. D. Rogers, “Hypergeometric formulas for lattice sums and Mahler measures”,
      Intern. Math. Res. Not. (to appear).
[124] M. D. Rogers and W. Zudilin, “From L-series of elliptic curves to Mahler
      measures”, Preprint at arXiv: 1012.3036 [math.NT], 2010.
[125] M. D. Rogers and W. Zudilin, “On the Mahler measure of 1 + X + 1/X + Y + 1/Y ”,
      Preprint at arXiv: 1102.1153 [math.NT], 2011.
[126] Е. А. Рухадзе, “Оценка снизу приближения ln 2 рациональными числами”,
      Вестник МГУ. Сер. 1. Матем., мех., 1987, no. 6, 25–29; English transl.,
      E. A. Rukhadze, “Lower estimate for rational approximations of ln 2”, Moscow
      Univ. Math. Bull. 42:6 (1987), 30–35.
[127] A. L. Schmidt, “Generalized q-Legendre polynomials”, J. Comput. Appl. Math.
      49:1-3 (1993), 243–249.
[128] A. L. Schmidt, “Legendre transforms and Apéry’s sequences”, J. Austral. Math.
      Soc. Ser. A 58:3 (1995), 358–375.
[129] А. Б. Шидловский, Трансцендентные числа, Наука, М. 1987; English transl.,
      A. B. Shidlovskii, Transcendental numbers, de Gruyter Stud. Math., vol. 12,
      Walter de Gruyter & Co., Berlin 1989.
[130] L. J. Slater, Generalized hypergeometric functions, Cambridge Univ. Press,
      Cambridge 1966.
[131] C. Smet and W. Van Assche, “Irrationality proof of a q-extension of ζ(2) using
      little q-Jacobi polynomials”, Acta Arith. 138:2 (2009), 165–178.
[132] В. Н. Сорокин, “Аппроксимации Эрмита–Паде для систем Никишина
      и иррациональность ζ(3)”, УМН 49:2 (1994), 167–168; English transl.,
      V. N. Sorokin, “Hermite–Padé approximations for Nikishin systems and the
      irrationality of ζ(3)”, Russian Math. Surveys 49:2 (1994), 176–177.
[133] В. Н. Сорокин, “О мере трансцендентности числа π 2 ”, Матем. сб. 187:12
      (1996), 87–120; English transl., V. N. Sorokin, “A transcendence measure for π 2 ”,
      Sb. Math. 187:12 (1996), 1819–1852.
[134] В. Н. Сорокин, “Теорема Апери”, Вестник МГУ. Сер. 1. Матем., мех., 1998,
      no. 3, 48–53; English transl., V. N. Sorokin, “On Apéry’s theorem”, Moscow Univ.
      Math. Bull. 53:3 (1998), 48–52.
[135] В. Н. Сорокин, “Циклические графы и теорема Апери”, УМН 57:3 (2002),
      99–134; English transl., V. N. Sorokin, “Cyclic graphs and Apéry’s theorem”,
      Russian Math. Surveys 57:3 (2002), 535–571.
[136] V. Strehl, “Binomial identities — combinatorial and algorithmic aspects,”, Discrete
      Math. 136:1-3 (1994), 309–346.
                              Arithmetic hypergeometric series                             49

[137] Z.-W. Sun, “Supercongruences and Euler sums”, Preprint at arXiv: 1001.4453
      [math.NT], 2010.
[138] Y. Tachiya, “Irrationality of certain Lambert series”, Tokyo J. Math. 27:1 (2004),
      75–85.
[139] W. Van Assche, “Little q-Legendre polynomials and irrationality of certain
      Lambert series”, Ramanujan J. 5 (2001), 295–310.
[140] О. Н. Василенко, “Некоторые формулы для значения дзета-функции Римана
      в целых точках”, Теория чисел и ее приложения (Ташкент, 26–28 сентября
      1990 г.), Тезисы докладов Республиканской научно-теоретической
      конференции, Ташкентский гос. пед. институт, Ташкент 1990, с. 27;
      English transl., O. N. Vasilenko, “Certain formulae for values of the Riemann
      zeta-function at integral points”, Number theory and its applications (Tashkent,
      26–28 September 1990), Proceedings of the science-theoretical conference,
      Tashkent State Pedagogical Inst., Tashkent 1990, pp. 27.
[141] Д. В. Васильев, “Некоторые формулы для дзета-функции в целых точках”,
      Вестник МГУ. Сер. 1. Матем., мех., 1996, no. 1, 81–84; English transl.,
      D. V. Vasil’ev, “Some formulas for the Riemann zeta function at integer points”,
      Moscow Univ. Math. Bull. 51:1 (1996), 41–43.
[142] D. V. Vasilyev, On small linear forms for the values of the Riemann zeta-function
      at odd points, Preprint № 1 (558), Nat. Acad. Sci. Belarus, Institute Math., Minsk
      2001.
[143] R. C. Vaughan, The Hardy–Littlewood method, 2nd ed., Cambridge Tracts in
      Math., vol. 125, Cambridge Univ. Press, Cambridge 1997.
[144] C. Viola, “Birational transformations and values of the Riemann zeta-function”, J.
      Théor. Nombres Bordeaux 15:2 (2003), 561–592.
[145] С. М. Воронин, А. А. Карацуба, Дзета-функция Римана, Физматлит, М. 1994;
      English transl., A. A. Karatsuba and S. M. Voronin, The Riemann zeta-function,
      de Gruyter Exp. Math., vol. 5, Walter de Gruyter & Co., Berlin 1992.
[146] S. O. Warnaar and W. Zudilin, “A q-rious positivity”, Aequat. Math. 81:1-2 (2011),
      177–183.
[147] F. J. W. Whipple, “A group of generalized hypergeometric series: relations between
      120 allied series of the type F [a, b, c; d, e]”, Proc. London Math. Soc. (2) 23 (1925),
      104–114.
[148] F. J. W. Whipple, “On well-poised series, generalized hypergeometric series having
      parameters in pairs, each pair with the same sum”, Proc. London Math. Soc. (2)
      24 (1926), 247–263.
[149] H. S. Wilf and D. Zeilberger, “An algorithmic proof theory for hypergeometric
      (ordinary and “q”) multisum/integral identities”, Invent. Math. 108:3 (1992),
      575–633.
[150] Y. Yang, “Apéry limits and special values of L-functions”, J. Math. Anal. Appl.
      343:1 (2008), 492–513.
[151] Y. Yang and W. Zudilin, “An Sp4 modularity of Picard–Fuchs differential
      equations for Calabi–Yau threefolds”, with an appendix by V. Pasol, Gems
      in Experimental Mathematics, Contemp. Math., vol. 517 (T. Amdeberhan,
      L. A. Medina, and V. H. Moll, eds.), Amer. Math. Soc., Providence, RI 2010,
      pp. 381–413.
[152] M. Yoshida, Fuchsian differential equations. With special emphasis on the
      Gauss–Schwarz theory, Aspects Math., vol. E11, Friedr. Vieweg & Sohn,
      Braunschweig 1987.
[153] D. Zagier, “The non-holomorphic embedding of H into H2 ”, Unpublished note,
      2008.
50                                     W. Zudilin

[154] D. Zagier, “Integral solutions of Apéry-like recurrence equations”, Groups and
      Symmetries: From Neolithic Scots to John McKay, CRM Proc. Lecture Notes,
      vol. 47, Amer. Math. Soc., Providence, RI 2009, pp. 349–366.
[155] D. Zeilberger, “Computerized deconstruction”, Adv. Appl. Math. 31 (2003),
      532–543.
[156] С. А. Злобин, “Интегралы, представляемые в виде линейных форм от
      обобщенных полилогарифмов”, Матем. заметки 71:5 (2002), 782–787;
      English transl., S. A. Zlobin, “Integrals expressible as linear forms in generalized
      polylogarithms”, Math. Notes 71:5 (2002), 711–716.
[157] С. А. Злобин, “О некоторых интегральных тождествах”, УМН 57:3 (2002),
      153–154; English transl., S. A. Zlobin, “On some integral identities”, Russian
      Math. Surveys 57:3 (2002), 617–618.
[158] С. А. Злобин, “Интегралы Рина”, Матем. заметки 81:2 (2007), 226–239;
      English transl., S. A. Zlobin, “Rhin integrals”, Math. Notes 81:2 (2007), 201–212.
[159] I. J. Zucker, “Madelung constants and lattice sums for hexagonal crystals”, J.
      Phys. A Math. Gen. 24:4 (1991), 873–879.
[160] В. В. Зудилин, “Разностные уравнения и мера иррациональности чисел”,
      Аналитическая теория чисел и приложения, Труды МИАН, 218, 1997,
      с. 165–178; English transl., W. Zudilin, “Difference equations and the irrationality
      measure of numbers”, Proc. Steklov Inst. Math. 218 (1997), 160–174.
[161] W. Zudilin, “Number theory casting a look at the mirror”, Preprint at arXiv:
      math.NT/0008237, 2000.
[162] В. В. Зудилин, “Одно из чисел ζ(5), ζ(7), ζ(9), ζ(11) иррационально”, УМН
      56:4 (2001), 149–150; English transl., W. Zudilin, “One of the numbers ζ(5), ζ(7),
      ζ(9), ζ(11) is irrational”, Russian Math. Surveys 56:4 (2001), 774–776.
[163] В. В. Зудилин, “Об иррациональности значений дзета-функции Римана”,
      Изв. РАН. Серия матем. 66:3 (2002), 49–102; English transl., W. Zudilin,
      “Irrationality of values of the Riemann zeta function”, Izv. Math. 66:3 (2002),
      489–542.
[164] W. Zudilin, “Remarks on irrationality of q-harmonic series”, Manuscripta Math.
      107:4 (2002), 463–477.
[165] В. В. Зудилин, “О мере иррациональности q-аналога ζ(2)”, Матем. сб. 193:8
      (2002), 49–70; English transl., W. Zudilin, “On the irrationality measure for a
      q-analogue of ζ(2)”, Sb. Math. 193:8 (2002), 1151–1172.
[166] В. В. Зудилин, “Совершенно уравновешенные гипергеометрические ряды и
      кратные интегралы”, УМН 57:4 (2002), 177–178; English transl., W. Zudilin,
      “Very well-poised hypergeometric series and multiple integrals”, Russian Math.
      Surveys 57:4 (2002), 824–826.
[167] В. В. Зудилин, “О рекурсии третьего порядка типа Апери для ζ(5)”, Матем.
      заметки 72:5 (2002), 796–800; English transl., W. Zudilin, “A third-order
      Apéry-like recursion for ζ(5)”, Math. Notes 72:5 (2002), 733–737.
[168] В. В. Зудилин, “О диофантовых задачах для q-дзета-значений”, Матем.
      заметки 72:6 (2002), 936–940; English transl., W. Zudilin, “Diophantine
      problems for q-zeta values”, Math. Notes 72:6 (2002), 858–862.
[169] W. Zudilin, “The hypergeometric equation and Ramanujan functions”, Ramanujan
      J. 7:4 (2003), 435–447.
[170] В. В. Зудилин, “О функциональной трансцендентности q-дзета-значений”,
      Матем. заметки 73:4 (2003), 629–630; English transl., W. Zudilin, “On the
      functional transcendence of q-zeta values”, Math. Notes 73:4 (2003), 588–589.
[171] W. Zudilin, “Well-poised hypergeometric service for diophantine problems of zeta
      values”, J. Théor. Nombres Bordeaux 15:2 (2003), 593–626.
                              Arithmetic hypergeometric series                           51

[172] W. Zudilin, “Heine’s basic transform and a permutation group for q-harmonic
      series”, Acta Arith. 111:2 (2004), 153–164.
[173] W. Zudilin, “Arithmetic of linear forms involving odd zeta values”, J. Théor.
      Nombres Bordeaux 16:1 (2004), 251–291.
[174] W. Zudilin, “Well-poised hypergeometric transformations of Euler-type multiple
      integrals”, J. London Math. Soc. 70:1 (2004), 215–230.
[175] В. В. Зудилин, “О биномиальных суммах, связанных с рациональными
      приближениями к ζ(4)”, Матем. заметки 75:4 (2004), 637–640; English
      transl., W. Zudilin, “Binomial sums related to rational approximations to ζ(4)”,
      Math. Notes 75:4 (2004), 594–597.
[176] W. Zudilin, “On a combinatorial problem of Asmus Schmidt”, Electron. J.
      Combin. 11:1 (2004), #R22, 8 pages.
[177] В. В. Зудилин, “Об обратном преобразовании Лежандра одного семейства
      последовательностей”, Матем. заметки 76:2 (2004), 300–303; English transl.,
      W. Zudilin, “The inverse Legendre transform of a certain family of sequences”,
      Math. Notes 76:2 (2004), 276–279.
[178] W. Zudilin, “Approximations to q-logarithms and q-dilogarithms, with
      applications to q-zeta values”, Труды по теории чисел, Зап. научн. сем.
      ПОМИ, 322, 2005, с. 107–124; Reprinted:, J. Math. Sci. (N. Y.) 137:2 (2006),
      4673–4683.
[179] W. Zudilin, “A new lower bound for k(3/2)k k”, J. Théor. Nombres Bordeaux 19:1
      (2007), 313–325.
[180] W. Zudilin, “Approximations to -, di- and tri-logarithms”, J. Comput. Appl. Math.
      202:2 (2007), 450–459.
[181] W. Zudilin, “Ramanujan-type formulae for 1/π: A second wind?”, Modular Forms
      and String Duality, Fields Inst. Commun. Ser., vol. 54, Amer. Math. Soc. & Fields
      Inst., Providence, RI 2008, pp. 179–188.
[182] W. Zudilin, “Apéry’s theorem. Thirty years after”, Intern. J. Math. Computer Sci.
      4:1 (2009), 9–19.
[183] W. Zudilin, “Ramanujan-type supercongruences”, J. Number Theory 129:8 (2009),
      1848–1857.

W. Zudilin                                                                Received 18/FEB/11
School of Mathematical and Physical Sciences,                    Translated by THE AUTHOR
University of Newcastle, Callaghan, Australia
E-mail: wadim.zudilin@newcastle.edu.au
