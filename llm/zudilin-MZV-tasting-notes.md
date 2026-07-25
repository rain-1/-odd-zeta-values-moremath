---
title: "zudilin-MZV-tasting-notes"
source: "books-and-surveys/zudilin-MZV-tasting-notes.pdf"
conversion: pdftotext -layout
note: "extracted text; formulas are flattened and may be lossy — check the PDF for anything load-bearing"
---

Multiple zeta values
                              Tasting notes
                         Release: 14 April 2025

                               Wadim Zudilin

  IMAPP, Radboud University, PO Box 9010, 6500 GL Nijmegen,
The Netherlands
  Email address: w.zudilin@math.ru.nl
  URL: http://www.math.ru.nl/~wzudilin/

© Wadim Zudilin (text) 2020–2025
© Victor Zudilin (cover image) 2022
         To the memory of my father Valentin
and of my grandfathers Veniamin and Stanislav

                      I wish I knew you better
                                Contents

Preface                                                              v
Chapter 1. Riemann’s zeta function and its multiple generalisation    1
  1.1. Riemann’s zeta function                                        1
  1.2. Hurwitz’s zeta function                                        3
  1.3. Zeta values                                                    7
  1.4. Analytic continuation of MZF                                  10
Chapter 2. Multiple zeta values                                      15
  2.1. First multiple steps                                          15
  2.2. The partial-fraction method                                   16
  2.3. Calculation of MZVs                                           21
Chapter 3. Algebraic relations of multiple zeta values               26
  3.1. Algebra of multiple zeta values                               26
  3.2. Shuffle algebra of generalised polylogarithms                 28
  3.3. Duality of MZVs                                               32
  3.4. Multiple harmonic sums                                        34
  3.5. Quasi-shuffle products and derivations                        37
Chapter 4. Generating functions and periodic multi-indices           42
  4.1. Hypergeometric function                                       42
  4.2. Broadhurst’s MZV evaluation                                   45
  4.3. Multiple zeta values of fixed weight, length and height       48
  4.4. An identity for alternating Euler sums                        50
Chapter 5. Further relations of MZVs                                 56
  5.1. Ohno’s relations                                              56
  5.2. The Maesaka–Seki–Watanabe formula                             58
  5.3. Ihara–Kaneko derivations                                      60
  5.4. Open questions about MZVs                                     63
Chapter 6. The two-one formula and its relatives                     65
  6.1. The two-one formula                                           65
  6.2. Zagier’s identity                                             70
  6.3. Double zeta values and products of single zeta values         75
  6.4. Hirose–Sato integrals                                         78
Chapter 7. q-Analogues of multiple zeta values                       82
                                    Contents    iv

  7.1.   q-Zeta values                          82
  7.2.   q-Models of MZVs                       84
  7.3.   Multiple q-zeta brackets               89
  7.4.   q-Differentiation of brackets          99
Bibliography                                   103
Index                                          106
                                   Preface

    After doing some odd mathematics choices during my university education
I became a dedicated transcendental number theorist and defended my PhD
thesis mysteriously entitled “On the estimates of the measure of linear inde-
pendence for values of certain analytical functions” in 1995. It was a good
piece of work, with potentials to develop further, but I was looking for real
challenges to taste. Apéry’s proof of the irrationality of ζ(3), its numerous
interpretations and sequels in the literature of the 1980s and 90s lacking any
progress on the irrationality of the other odds — ζ(5), ζ(7), . . . — sounded to
me like a great goal to pursue. I started to systematically dig in publications
on the topic and occasionally crossed with some multiple sums generalising the
values of Riemann’s zeta function

                                          ∞
                                          X 1
                                 ζ(s) =
                                          n=1
                                                ns

at positive integers s > 1. But those multiple findings were all a nice but
side story for me until I got to a lecture of Michel Waldschmidt in April
2000 on Multiple zeta values at the Oberwolfach meeting on Diophantische
Approximationen. There was so much structure in those numerical quantities
that I immediately fell in love with these multiple creatures and saw potentials
in exploring the mechanisms behind them in irrationality and transcendence
applications of ordinary zeta values. I have never managed to do this directly,
and my other inspirations — the talk of Carlo Viola on his joint work [37] with
Georges Rhin at the same Oberwolfach meeting and the later paper [38] of
Tanguy Rivoal which appeared on the arXiv in August 2000 — offered to me
more productive options. But I started a careful study of multiple zeta values
and published my notes [52] as a review of the subject in 2003. Those who
followed [52] can still recognise their influence on the text that follows, though
the latter features many reshapings, improvements and additions through my
personal involvement in this remarkable topic.
    The multiple zeta values keep developing and — quite remarkably — give
life to numerous generalisations and side extensions that now have stories
of their own. I was truly fortunate to be part of the 17th Symposium of
the Mathematical Society of Japan in February 2025 which incorporated the
School on Multiple Zeta Values and Beyond held at Kyushu University and the
Workshop on Modular Forms and Multiple Zeta Values in honour of Masanobu
                                        v
                                    Preface                                   vi

Kaneko at Kindai University. The events gathered — quite impressively —
about 200 participants in total, mainly from Japan where this mathematics
topic can be called national without doubt. During the symposium I learned
from Michel Waldschmidt that his personal involvement in multiple zeta values
had initiated by the late Pierre Cartier, with whom he ran a successful seminar
on zeta values at the Institute of Henri Poincaré from 2000 for several years.
Cartier made a lasting impact on the subject through reporting at different
geographic locations and educating many bright minds; I still have a good
memory of his talk at the 2001 conference in Caen on the occasion of Rivoal’s
PhD defence. One educational fragment of his talk is Exercise 3.14 in this
text.
    An idea behind these notes is to provide a comprehensive but reasonably
elementary introduction to multiple generalisations of Riemann’s zeta function
and to analytic, algebraic, arithmetic, combinatorial methods used in their
study. Great sources for substantial knowledge on the topic of multiple zeta
values are the two monographs [9] and [51] — in no way we compete with these
advanced treatments when it comes to a systematic coverage of the themes.
Further, the dedicated website [17] developed by Michael Hoffman includes
a comprehensive list of references on multiple zeta values. For those who
are already familiar with some aspects of the subject, we use the convention
n1 > · · · > nl > 0 for multiple zeta value summation (same as in [51] and [9]).
    There are several personal motivations to write up these notes. First,
parts of the text below grew from the material for my own lectures for na-
tional master courses in Australia (2011, taught jointly with the late Jonathan
M. Borwein) and in the Netherlands (2019). Second, I have been always trying
to follow methodological advances and collect the simplest proofs available —
though they still have to be nice and reader-friendly. Many earlier proofs
which were mysteriously tricky, are now quite elementary and can be classi-
fied as proofs from the Book. Third, before these notes reach a publisher I
can keep them as a dynamical set of lecture notes rather than a stable book.
Further, I wish to share my personal taste for multiple zeta values via particu-
larly tasteful bites — some results can be seen as somewhat isolated but their
aesthetics is truly appealing for the inclusion. I notice that the exposition is
dry at quite some places and references to the original sources could be greatly
improved — I plan to work on these issues in due course. I definitely welcome
any constructive feedback from those who read the notes.
    There are so many people who influenced me, implicitly or not, to acknowl-
edge. As explained above my initial crash at the topic came from a lecture
of Michel Waldschmidt, who further supported my education on multiple zeta
values through sharing his knowledge and available materials. The papers by
Jonathan Borwein, David Bradley, David Broadhurst, Herbert Gangl, Michael
Hoffman, Kentaro Ihara, Masanobu Kaneko, Yasuo Ohno, Don Zagier and
many others that I followed at the time formed my appreciation to the sub-
ject; I met all these mathematicians in person at later moments of my life
                                     Preface                                    vii

and some of them became my collaborators (not necessarily on multiple zeta
values!) and friends. In the beginning of the 2000s we formed a little circle
in Moscow of those indifferent t o t he a rithmetic q uestions o f z eta values and
polylogarithms — in particular, their multiple generalisations — with Zhenya
Ulanskii, Yuri Nesterenko and Sergey Zlobin; I owe these colleagues of mine
at the time special thanks for an educational and joyful atmosphere of our
seminars where we not only learned but also produced new creative results.
Some related work — partly in parallel — of Stéphane Fischler, Christian Krat-
tenthaler, Tanguy Rivoal, Vladislav Salikhov, Carlo Viola has been another
personal inspiration for years. My interest in multiple zeta values was renewed
in 2007 after a lecture of Yasuo Ohno and from our joint research stay at the
Max-Planck Institute for Mathematics in Bonn; this was a multiply productive
period of my life — thank you, Yasuo! Of course, I am grateful to the Max-
Planck Institute for the unique scientific welcoming a tmosphere t hat l eads to
my multiple visits there. Besides those acknowledged above, I am very thank-
ful to Henrik Bachmann, Benjamin Brindle, Francis Brown, Steven Charl-
ton, Kurusch Ebrahimi-Fard, Hidekazu Furusho, Tatiana Hessami Pilehrood,
Jan-Willem van Ittersum, Ulf Kühn, Dominique Manchon, Kohji Matsumoto,
Maki Nakasuji, Danylo Radchenko, Yoshitaka Sasaki, Nobuo Sato, Shin-ichiro
Seki, Koji Tasaka, Hirofumi Tsumura, James Wan, Shuji Yamamoto, Jian-
qiang Zhao, for being on the multiple zeta value journey, with and without
me.

                                                               Wadim Zudilin
                                                 Nijmegen, Bonn and Newcastle
                                                                 13 April 2025
                                 CHAPTER 1

Riemann’s zeta function and its multiple generalisation

                         1.1. Riemann’s zeta function
   The Riemann zeta function is traditionally defined in the region Re s > 1
by the convergent series
                                     ∞
                                    X    1
                            ζ(s) =          ;                           (1.1)
                                    n=1
                                         ns
this makes it an analytic function in the domain. The function is very special
in number theory, because its analytic properties are ultimately linked to ones
of the prime numbers; this can be seen through Euler’s representation of ζ(s)
as an infinite product over primes:
                                    Y         −1
                                             1
                           ζ(s) =         1− s      .
                                  p prime
                                             p

The first thing one learns in studying the distribution of prime numbers is
that ζ(s) can be analytically continued to a larger domain, and in this story
Riemann’s zeta function is always accompanied by Euler’s gamma function
Γ(z) defined through the product expansion
                                      ∞       
                         1        γz
                                     Y       z −z/k
                              = ze        1+     e                      (1.2)
                        Γ(z)         k=1
                                             k

for its reciprocal. Here
                                        
                     1 1         1
       γ = lim 1 + + + · · · + − log n
            n→∞      2 3         n
         = 0.57721566490153286060651209008240243104215933593992 . . .
is the Euler (or Euler–Mascheroni ) constant. A theorem of Weierstrass guar-
antees that 1/Γ(z) is an entire function with zeros at z = 0, −1, −2, . . . , and
many properties of the gamma function, like the difference equation
                               Γ(z + 1) = zΓ(z),                            (1.3)
the reflection formula
                                    ∞      −1
                                 1Y      z2          π
                  Γ(z)Γ(1 − z) =       1− 2     =                           (1.4)
                                 z k=1   k        sin πz
                                        1
                           1.1. Riemann’s zeta function                                        2

and multiplication formula
             1      2           n − 1
  Γ(z)Γ z +      Γ z+     ···Γ z +          = (2π)(n−1)/2 n−nz+1/2 Γ(nz), (1.5)
             n         n               n
follow straight from the defining product.
   Exercise 1.1. Prove equations (1.3)–(1.5).
   We also take for granted from a complex analysis course the evaluation
                           Z ∞
                                e−t tz−1 dt = Γ(z)                     (1.6)
                                  0
of the Eulerian integral (of the second kind) in the domain Re z > 0.
   Proposition 1.1. The logarithmic derivative ψ(z) = Γ′ (z)/Γ(z) of the
gamma function serves a generating function for the values of Riemann’s zeta
function at positive integers. More specifically,
                                  X∞
                ψ(1 − z) = −γ −       ζ(m + 1)z m for |z| < 1.
                                         m=1

   Proof. It follows from the logarithmic differentiation of (1.2) that
                                   ∞                    
                         1        X      1         1
                −ψ(z) = + γ +          − +
                         z        k=1
                                         k k(1 + z/k)
for z ̸= 0, −1, −2, . . . . Furthermore, from (1.3) we have ψ(1 + z) = 1/z + ψ(z).
Thus,
                                              ∞                   
                             1               X    1            1
            −ψ(1 − z) = − ψ(−z) = γ +                −1 +
                             z               k=1
                                                  k        1 − z/k
                                 ∞     ∞  m           ∞       ∞
                                X   1X z               X
                                                             m
                                                               X     1
                          =γ+                    =γ+       z         m+1
                                                                         ,
                                k=1
                                    k m=1 k            m=1     k=1
                                                                   k
with all the internal series converging in the disk |z| < 1.                                   □
    Exercise 1.2. In this exercise we compute the Eulerian integral of the
first kind                     Z              1
                        B(α, β) =                 xα−1 (1 − x)β−1 dx,
                                          0
where Re α > 0 and Re β > 0.
   (a) Verify the following properties:
                                                                          β
   B(α, β) = B(β, α);                                       B(α, β + 1) =   B(α + 1, β);
                                                                          α
                                                                            β
   B(α, β) = B(α + 1, β) + B(α, β + 1);                     B(α, β + 1) =       B(α, β).
                                                                          α+β
   (b) Show that
                          ZZ                                        ZZ
     Γ(α)Γ(β) = 4 lim                   f (x, y) dx dy = 4 lim                f (x, y) dx dy
                    R→∞        [0,R]2                         R→∞        SR
                               1.2. Hurwitz’s zeta function                         3
                       2   2
where f (x, y) = e−(x +y ) x2α−1 y 2β−1 and SR is the circular sector x2 + y 2 ≤ R,
x ≥ 0, y ≥ 0.
   (c) Pass to the polar coordinates x = r cos θ, y = r sin θ in the integral
                                ZZ
                                       f (x, y) dx dy
                                         SR

and use part (b) to conclude that
                                                    Γ(α)Γ(β)
                                 B(α, β) =                   .
                                                    Γ(α + β)
    Hint. (b) Write
           Z ∞                Z ∞                      Z R
                −t α−1             −x2 2α−1                   2
    Γ(α) =     e t     dt = 2     e x       dx = 2 lim     e−x x2α−1 dx
               0                     0                                R→∞   0

and, similarly, for Γ(β); then show that
         ZZ                        ZZ
                  f (x, y) dx dy −    f (x, y) dx dy → 0 as R → ∞.                 □
              [0,R]2                          SR

    Exercise 1.3. Establish the following evaluation of trigonometric integral:
                                                  1 Γ( m2 )Γ( n2 )
          Z π/2
                                        1
                cosm−1 x sinn−1 x dx = B m2 , n2 =                  .
           0                            2            2 Γ( m+n2
                                                               )
Give closed forms of the integral when m and n are positive integers.
    Exercise 1.4. (a) Show the integral expansion
                                    Z 1
                                         1 − tz−1
                       ψ(z) = −γ +                dt
                                      0    1−t
in the half-plane Re z > 0.
    (b) Prove that, for n = 1, 2, 3, . . . ,
                                                        n−1
                                                        X   1
                                  ψ(n) = −γ +                     .
                                                        k=1
                                                              k

                           1.2. Hurwitz’s zeta function
    In order to analyse the properties of Riemann’s zeta function we turn our
attention to its slightly more general version
                                                   ∞
                                                   X      1
                                 ζ(s, a) =                                      (1.7)
                                                   n=0
                                                       (a + n)s
known as Hurwitz’s zeta function. In this expression we treat a as a real
constant from the interval 0 < a ≤ 1 (though one can allow a to vary over the
real line, and even over the complex plane); again, the series in (1.7) defines
an analytic function of s in the region Re s > 1. Observe that ζ(s, 1) = ζ(s).
                              1.2. Hurwitz’s zeta function                         4

   Proposition 1.2. For Re s > 1,
                                             Z ∞
                                    1              xs−1 e−ax
                         ζ(s, a) =                           dx.
                                   Γ(s)        0   1 − e−x
   Proof. We start with the following consequence of (1.6):
                                  Z ∞
                        −s
                 (a + n) Γ(s) =        xs−1 e−(n+a)x dx.
                                              0

Taking δ > 0, we have in the domain σ = Re s ≥ 1 + δ,
                              N Z ∞
                              X
       Γ(s)ζ(s, a) = lim                  xs−1 e−(n+a)x dx
                       N →∞         0
                              n=0
                              Z ∞                       Z ∞
                                              xs−1 e−(N +1+a)x
                                        xs−1 e−ax
                                                                  
                   = lim                          dx −         dx
                    N →∞   0            1 − e−x
                                            0    1 − e−x
                         Z ∞ s−1 −ax      Z ∞ s−1 −(N +a)x 
                             x e              x e
                   = lim              dx −                  dx .
                    N →∞   0  1 − e−x       0    ex − 1
Since ex ≥ 1+x for x ≥ 0, the absolute value of the second integral is estimated
from above by the quantity
                Z ∞
                     xσ−2 e−(N +a)x dx = (a + N )1−σ Γ(σ − 1),
                   0

which clearly tends to 0 as N → ∞ in view of σ − 1 ≥ δ > 0. This gives the
desired formula for Re s ≥ 1 + δ, hence for Re s > 1.                   □

    For real ρ > 0 (possibly, ρ = ∞), introduce a (Hankel-type) contour D =
D(ρ), which starts at z = ρ, passes once around the origin into the positive
direction (without crossing the half-line z ≥ 0) and ends up at z = ρ. Our
principal interest is in the integral
                       (−z)s−1 e−az               (−z)s−1 e−az
               Z                              Z
                                    dz =  lim                  dz
                D(∞)     1 − e−z         ρ→∞ D(ρ)   1 − e−z
for a fixed s from the half-plane σ = Re s ≥ 1+δ. To avoid the unwanted poles
of the integrand, we further assume that the contours D(ρ) do not contain the
points ±2πin for n = 1, 2, . . . . We specify the branch of (−z)s−1 = e(s−1) log(−z)
by choosing the log(−z) to be real for negative z; then −π ≤ arg(−z) ≤ π
on the contours — this makes the integrand a single-valued function on D(ρ).
Of course, the integrand is not analytic inside D(ρ) but we can still deform it
within C \ [0, ∞) to the contour going along the upper bank of the cut [0, ∞)
from ρ to ε > 0, then making a circle of radius ε around the origin and finally
returning from ε to ρ along the lower bank of the cut. At the beginning we
have arg(−z) = −π, so that (−z)s−1 = e−πi(s−1) z s−1 , and at the end we get
arg(−z) = π, hence (−z)s−1 = eπi(s−1) z s−1 . We set −z = εeiθ on the circle.
                              1.2. Hurwitz’s zeta function                                   5

Therefore,
              (−z)s−1 e−az
       Z
                               dz
         D(ρ)    1 − e−z
                        Z ε s−1 −ax           Z π
               −πi(s−1)       x e                  (εeiθ )s eaε(cos θ+i sin θ)
          =e                        −x
                                       dx + i                                  dθ
                         ρ 1−e                 −π    1 − eε(cos θ+i sin θ)
                            Z ρ s−1 −ax
                    πi(s−1)       x e
                +e                        dx
                              ε   1 − e−x
                          Z ρ s−1 −ax                Z π isθ+aε(cos θ+i sin θ)
                                x e              s−1      εe
          = −2i sin πs               −x
                                         dx + iε                   ε(cos θ+i sin θ)
                                                                                    dθ
                            ε   1−e                   −π 1 − e

for 0 < ε ≤ ρ. As ε → 0 we have εs−1 → 0 and
      Z π isθ+aε(cos θ+i sin θ)       Z π                       Z π
          εe                                    eisθ
                ε(cos θ+i sin θ)
                                 dθ →                      dθ =     ei(s−1)θ dθ,
       −π  1 − e                       −π cos θ +  i sin θ       −π

since the integrand uniformly converges to its limit. We conclude that
                                                  Z ρ s−1 −ax
                     (−z)s−1 e−az
               Z
                                                     x e
                                  dz = −2i sin πs             dx
                D(ρ)   1 − e−z                     0  1 − e−x
implying
                                                  Z ∞
              (−z)s−1 e−az                              xs−1 e−ax
       Z
                           dz = −2i sin πs                        dx
         D(∞)   1 − e−z                             0   1 − e−x
                                                                           ζ(s, a)
                                  = −2i sin πs Γ(s)ζ(s, a) = −2πi
                                                                          Γ(1 − s)
on the basis of Proposition 1.2 and reflection formula (1.4). This brings us to
the following result.
   Proposition 1.3. For Re s > 1,
                                Γ(1 − s)            (−z)s−1 e−az
                                             Z
                    ζ(s, a) = −                                  dz.                     (1.8)
                                  2πi          D(∞)   1 − e−z
    The resulting integral is a single-valued analytic function of s for all s ∈
C. Therefore, the only potential singularities of ζ(s, a) originate from the
singularities of Γ(1 − s), which are the points s = 1, 2, . . . , since the integral
provide the analytic continuation of ζ(s, a) to the entire complex plane with
the exception of these points. At the same time, we already now the analyticity
of ζ(s, a) in the domain Re s > 1 from its defining series expansion (1.7). This
leads us to the following.
    Corollary 1.4. The function ζ(s, a) is analytic in C besides s = 1, where
it has a simple pole with residue 1.
   When a = 1, this implies the analytic properties of ζ(s).
                             1.2. Hurwitz’s zeta function                                 6

    Proof. By the argument above, the point s = 1 is the only candidate for
a singular point. Taking s = 1 in the integral (without the gamma prefactor)
we get the expression
                                         e−az
                                Z
                             1
                                                dz
                            2πi D(∞) 1 − e−z
which is equal to the residue of the integrand at z = 0: this is clearly equal
to 1. Combined with (1.8) this implies
                                        ζ(s, a)
                                   lim          = −1.
                                   s→1 Γ(1 − s)

It remains to recall that Γ(1−s) has a simple pole at s = 1 with residue −1. □
   Exercise 1.5. Show for Re s > 0,
                                   ∞                       Z ∞
                   1−s
                                   X (−1)n−1         1            xs−1
             (1 − 2      )ζ(s) =                  =                     dx.
                                   n=1
                                             ns     Γ(s)    0    ex + 1

   Exercise 1.6. Show for Re s > 1,
                                          Z ∞ s−1 x
               s
                             1       2s    x e
             (2 − 1)ζ(s) = ζ s,     =                dx.
                                2     Γ(s) 0 e2x − 1
   Exercise 1.7. Show for all s ̸= 1,
                            21−s Γ(1 − s)             (−z)s−1
                                                  Z
                  ζ(s) = −                                    dz,
                           2πi (21−s − 1)               z
                                                  D(∞) e + 1

where the contour D(∞) does not contain inside the points ±πi, ±3πi, ±5πi, . . . .
   Proposition 1.5 (Hurwitz). For 0 < a ≤ 1 and σ = Re s < 0,
                              ∞                   ∞          
             2Γ(1 − s)      πs X cos 2πan       πs X sin 2πan
   ζ(s, a) =            sin               + cos                 .                  (1.9)
              (2π)1−s       2 n=1 n1−s          2 n=1 n1−s

   Proof. Consider the integral
                                (−z)s−1 e−az
                             Z
                          1
                       −                     dz,
                         2πi CN 1 − e−z
where N is an odd positive integer, the contour CN is the circle centered at
the origin of radius N π going counter-clockwise from N π to N π. We assume
that arg(−z) = 0 at z = −N π.
   In the domain bounded by the contours CN and D(N π), the function
(−z)s−1 e−az /(1 − e−z ) is analytic and single-valued, except for the poles at
±2πi, ±4πi, . . . , ±(N − 1)πi. Therefore,
                                                                  (N −1)/2
           (−z)s−1 e−az                         (−z)s−1 e−az
        Z                                Z
   1                          1                                     X
                        dz −                                 dz =         (Rn+ + Rn− ),
  2πi   CN   1 − e−z         2πi         D(N π)   1 − e−z
                                                                    n=1
                                  1.3. Zeta values                                 7

where Rn+ and Rn− are the residues of the integrand at 2nπi and −2nπi, respec-
tively. When −z = 2nπe−πi/2 , the residue is equal to (2nπ)s−1 e−πi(s−1)/2 e−2anπi ,
so that
                                             
        +    −           s−1      πs                                    N −1
       Rn + Rn = 2 (2nπ) sin          + 2πan      for n = 1, 2, . . . ,      .
                                   2                                      2
We obtain
                                                (N −1)/2
                     (−z)s−1 e−az      2 sin πs
             Z
        1                                    2
                                                  X cos 2πan
     −                            dz =
       2πi    D(N π)   1 − e−z         (2π)1−s n=1       n1−s
                               (N −1)/2
                      2 cos πs                       (−z)s−1 e−az
                                 X sin 2πan       Z
                            2                   1
                    +                        −                    dz.
                      (2π)1−s n=1       n1−s   2πi CN 1 − e−z

Furthermore, for 0 < a ≤ 1 we can find an absolute bound |e−az /(1−e−z )| < M
for z ∈ CN , independent of N . This means that, for σ = Re s < 0,
                   (−z)s−1 e−az       M π
               Z                         Z
            1
                          −z
                                dz <         |(N π)s eisθ | dθ
          2πi CN 1 − e                2π −π
                                     < M (N π)σ eπ|s| → 0 as N → ∞.
Thus, letting N → ∞ in the above equality we arrive at the desired formula
(1.9). Note the (absolute) convergence of both series when Re s < 0.    □
   Theorem 1.6 (Riemann). The following functional equation is valid for
Riemann’s zeta function:
                                       πs
                     21−s Γ(s)ζ(s) cos    = π s ζ(1 − s).         (1.10)
                                       2
    Proof. Take a = 1 in equation (1.9) and apply the reflection formula
(1.4) of the gamma function. This proves (1.10) in the domain Re s < 0. Since
both sides are analytic in the larger domain C \ {0, 1} (besides the simple
poles at s = 0, 1), the result remains valid there by the theory of analytic
continuation.                                                              □
   Exercise 1.8. Show the function Γ(s/2)π −s/2 ζ(s) does not change under
the involution s ↔ 1 − s.
    It follows from (1.10) that ζ(s) has zeros at negative even integers; these
are called trivial zeros. In his famous 1859 memoir, Riemann suggested that
all other (non-trivial) zeros lie on the critical line Re s = 1/2, which represents
the symmetry of the functional equation.

                                1.3. Zeta values
   One of interesting and still unsolved problems is the problem of determining
polynomial relations over Q for the numbers ζ(s), s = 2, 3, 4, . . . .
                                     1.3. Zeta values                            8

   The first breakthrough in this direction is due to Euler, who showed that
ζ(2k) is always a rational multiple of π 2k , where
            ∞
            X (−1)n
     π=4
            n=0
                  2n + 1
       = 3.14159265358979323846264338327950288419716939937510 . . . .
Although we do not follow Euler’s original method, the derivation is worth
reproducing.
    For a ∈ R, the Bernoulli polynomials Bs (a) ∈ Q[a], where s = 0, 1, 2, . . . ,
are defined by the generating function
                                      ∞
                             zeaz    X          zs
                                   =     Bs (a)    ,                    (1.11)
                            ez − 1   s=0
                                                s!
while the Bernoulli numbers Bs ∈ Q, where s = 0, 1, 2, . . . , are simply given
by Bs = Bs (0). The latter means that the generating function of the Bernoulli
numbers is
                                       ∞
                                z     X       zs
                                    =     B s    .
                             ez − 1   s=0
                                              s!
For example, B0 = 1, B1 = −1/2. The polynomials and numbers satisfy
numerous identities, with several dedicated books devoted to them. As an
example, we have the formulas Bs′ (a) = sBs−1 (a) and
                            N −1
                            X                Bs (N ) − Bs (M )
                                   k s−1 =
                           k=M
                                                     s
for s = 1, 2, . . . , and also the following ones.
   Exercise 1.9. (a) Show that
                        s  
                       X    s
              Bs (a) =         Bk as−k             for s = 0, 1, 2, . . . .
                       k=0
                            k
   (b) Verify that Bs = 0 for odd s ≥ 3.
   (c) Verify that Bs (1) = Bs = Bs (0) for even s ≥ 0.
   Lemma 1.7. For 0 < a ≤ 1 and s = −m a negative integer,
                                                 Bm+1 (a)
                              ζ(−m, a) = −                .
                                                  m+1
   Proof. Recall the integral
                            (−z)s−1 e−az
                     Z
                  1                              ζ(s, a)
                                   −z
                                         dz = −
                 2πi D(∞) 1 − e                 Γ(1 − s)
from Proposition 1.3. If s is a negative integer, s = −m, the expression
                                       (−z)s−1 e−az
                                         1 − e−z
                                    1.3. Zeta values                                 9

is a single-valued function of z, which is analytic in |z| < 2π, z ̸= 0. By
Cauchy’s integral theorem, the integral over D(∞) is equal to the residue of
the integrand at z = 0, that is, to the coefficient of z −s = z m in
                                                         ∞
       (−1)s−1 e−az   (−1)s−1 (−z) e−az       (−1)m−1 X          k        zk
                    =                     =                 (−1)   Bk (a)    .
         1 − e−z          z      e−z − 1          z     k=0
                                                                          k!
It follows that
                        ζ(−m, a)     ζ(s, a)       Bm+1 (a)
                    −            =−              =          ,
                           m!       Γ(1 − s) s=−m (m + 1)!
which implies the result.                                                          □
    When a = 1, we get the following consequence for Riemann’s zeta function
(using also Exercise 1.9).
    Corollary 1.8. For k = 1, 2, . . . , we have ζ(−2k) = 0 and ζ(1 − 2k) =
B2k /(2k).
   Exercise 1.10. Show that ζ(0, a) = 12 − a and ζ(0) = − 12 .
   Corollary 1.9. For k = 1, 2, . . . , we have
                                                  (2π)2k B2k
                             ζ(2k) = (−1)k−1                 .
                                                    2 (2k)!
    Proof. This follows from Corollary 1.8 and the functional equation (1.10)
for s = 2k.                                                                □
   In particular,
                          π2                  π4                     π6
              ζ(2) =         ,   ζ(4) =              ,   ζ(6) =              ,
                         2·3              2 · 32 · 5              33 · 5 · 7
                              π8                         π 10
                    ζ(8) =              ,   ζ(10) =                 ,
                        2 · 33 · 52 · 7             35 · 5 · 7 · 11
                         691π 12                              2π 14
            ζ(12) = 6 3 2                 , ζ(14) = 6 2                  ,
                   3 · 5 · 7 · 11 · 13               3 · 5 · 7 · 11 · 13
and so on.
    Corollary 1.9 gives us the expression for the values of the zeta function at
even integers in terms of π and the (rational) Bernoulli numbers. It implies the
coincidence of the rings Q[ζ(2), ζ(4), ζ(6), ζ(8), . . . ] and Q[π 2 ]. Lindemann’s
theorem from 1882 asserts the transcendence of π, therefore we may conclude
that each of the rings has transcendence degree 1 over the field of rational
numbers.
    Much less is known on the arithmetic nature of the values of the zeta
function at odd integers s = 3, 5, 7, . . . : in 1978, Apéry proved the irrationality
of the number ζ(3) and there are more recent but partial linear independence
results of Rivoal and this lecturer. Rivoal’s theorem settles the infiniteness of
the set of irrational numbers among ζ(3), ζ(5), ζ(7), . . . . Conjecturally, each
of these numbers is transcendental, and a complete answer to the above-stated
                          1.4. Analytic continuation of MZF                                10

question, about polynomial relations over Q for the values of series (1.1) with
s ≥ 2 integer, looks very simple.
    Conjecture 1.10. The numbers
                           π, ζ(3), ζ(5), ζ(7), ζ(9), . . .
are algebraically independent over Q.
    This conjecture may be regarded as a mathematical folklore. It seems to be
unattainable by the present methods. In this course, a certain generalization
of the problem of algebraic independence for the values of the Riemann zeta
function at positive integers (zeta values) is discussed. Namely, we will speak
on the object that is extensively studied during the last decades in connection
with problems of not only number theory but also of combinatorics, algebra,
analysis, algebraic geometry, quantum physics, and many other branches of
mathematics.
    Series (1.1) enables the following multidimensional generalization. For pos-
itive integers s1 , s2 , . . . , sl with s1 > 1, consider the values of the multiple
(l-tuple) zeta function
                                                     X              1
              ζ(s) = ζ(s1 , s2 , . . . , sl ) =                               ; (1.12)
                                                              n n · · · nsl l
                                                               s1 s2
                                                n >n >···>n ≥1 1 2
                                              1    2     l

the corresponding multi-index s = (s1 , s2 , . . . , sl ) will be further regarded as
admissible. The quantities (1.12) are called the multiple zeta values (and ab-
breviated MZVs), or the multiple harmonic series, or the Euler sums. The
sums (1.12) for l = 2 were first investigated by Euler, who obtained a family of
identities connecting double and ordinary zeta values (which we discuss later).
In particular, Euler proved the identity
                                       ζ(2, 1) = ζ(3),                                 (1.13)
which was several times rediscovered after.
    Exercise 1.11. Find your own (elementary) proof of (1.13).

                     1.4. Analytic continuation of MZF
  In this part, we discuss analytic properties of the multiple zeta function
(MZF)
                                 X                1
                    ζ(s) =                  s1 s2         sl          (1.14)
                            n >n >···>n ≥1
                                           n1 n 2  · · · nl
                                   1     2     l

as a function of complex variables s1 , . . . , sl ; the notation σ1 , . . . , σl will be
used for the real parts of s1 , . . . , sl .
    Exercise 1.12. Show that the multiple series in (1.14) converges absolutely
in the domain
         σ1 + · · · + σj = Re(s1 + · · · + sj ) > j      for every j = 1, . . . , l.
                              1.4. Analytic continuation of MZF              11

Conclude from this that the MZV is analytic in each of its variables in the
domain σ1 + · · · + σj > j, where j = 1, . . . , l.
     Hint. Use mathematical induction on l and estimates
                         X 1              1
                                σ
                                  ≤              ,
                         n>M
                              n     (σ − 1)M σ−1
where M ≥ 1 is integral and σ > 1 is real, coming from the integral test (when
the partial sums of a series are compared to Riemann sums).                 □
     Lemma 1.11. For 0 < a ≤ 1 and an integer m ≥ 2,
                         X′ e2πina        Bm (a)
                                    m
                                      =−         ,
                         n∈Z
                             (2πin)         m!
where the dash in summation corresponds to omitting the (problematic) index
n = 0.
     Proof. Comparing Hurwitz’s equation (1.9),
                                     ∞
                 ζ(s, a)      2     X   sin(πs/2 + 2πan)
                         =      1−s
                Γ(1 − s)   (2π)     n=1
                                              n1−s
for s = −m + 1, with the result of Lemma 1.7,
                         Bm (a)      ζ(s, a)
                       −         =                  ,
                           m!       Γ(1 − s) s=−m+1
we find                            ∞
                        Bm (a)    X   sin(−π(m − 1)/2 + 2πan)
                      −        =2                  m
                                                              ,
                         m!       n=1
                                              (2πn)
which is exactly
                      ∞                     ∞
                  k
                      X 2 sin 2πan          X e2πina − e−2πina
           (−1)                         =
                      n=1
                            (2πn)2k+1       n=1
                                                  (2πin)2k+1
                                             ∞              ∞
                                            X     e2πina    X    e−2πina
                                        =                 +
                                            n=1
                                                (2πin)2k+1 n=1 (−2πin)2k+1
or
                      ∞                     ∞
               k
                      X 2 cos 2πan          X e2πina + e−2πina
           (−1)                         =
                      n=1
                            (2πn)2k         n=1
                                                   (2πin)2k
                                             ∞          ∞
                                            X  e2πina   X   e−2πina
                                        =             +
                                          n=1
                                              (2πin)2k n=1 (−2πin)2k
depending on whether m = 2k + 1 is odd or m = 2k is even.                    □
     Lemma 1.12. For 0 < a ≤ 1 and any integer m ≥ 2,
                                        4m!
                            |Bm (a)| <       .
                                       (2π)m
                            1.4. Analytic continuation of MZF                   12

   Proof. It follows from Lemma 1.12 that
                                X′     1     2m! ζ(m)
                  |Bm (a)| ≤ m!          m
                                           =          .
                                n∈Z
                                    (2πn)     (2π)m

It remains to apply the trivial estimate ζ(m) ≤ ζ(2) = π 2 /6 < 2.              □
   For the statement and application of the following classical result, it will be
convenient to introduce the periodic Bernoulli polynomials given by B    em (a) =
Bm ({a}), where { · } denotes the fractional part of a real number. By Lem-
ma 1.12 (and Exercise 1.9) we get the estimate
                                        4m!
                        |B
                         em (a)| <             for m = 2, 3, . . . ,       (1.15)
                                       (2π)m
now valid for all real a.
   Exercise 1.13. Verify the validity of (1.15) for m = 0, 1.
   We will also implement the (standard) notation
                       (
           Γ(s + m)      s(s + 1) · · · (s + m − 1) if m = 1, 2, . . . ,
   (s)m =            =                                                     (1.16)
              Γ(s)       1                          if m = 0,
for the Pochhammer symbol, though it makes sense for any (not necessarily
integer or nonnegative) m. For example, (s)−1 = Γ(s − 1)/Γ(s) = 1/(s − 1).
    Proposition 1.13 (Euler–Maclaurin summation). Let f (x) be a (complex-
valued ) C ∞ function on the real interval [1, ∞). Then for any positive integers
N and m, m even,
  N          Z N                                  m
 X                           1                  X   Bk (k−1)
                                                              (N ) − f (k−1) (1)
                                                                                
     f (n) =      f (x) dx + f (1) + f (N ) +           f
 n=1           1             2                   k=2
                                                     k!
                      Z N
                   1       em (x)f (m) (x) dx.
                −          B
                  m! 1
   Notice that the sum over k in the formula only involves k even, because
Bk = 0 for odd k ≥ 2.
   Lemma 1.14. Given s ∈ C with Re s > 1, for integers M ≥ 1 and m ≥ 2,
m even, we have
                       m
                                       (s)m ∞ B
             X 1                            Z
                      X   Bk (s)k−1               em (x)
                  s
                    =          s+k−1
                                     −              s+m
                                                         dx.
             n>M
                 n    k=0
                          k! M          m!    M   x

   Proof. Apply Proposition 1.13 with f (x) = 1/xs twice: when N → ∞
and when N = M . Taking the difference of the results we arrive at
   X 1         ∞            M
               X 1          X 1
           =            −
  n>M
      ns       n=1
                   ns       n=1
                                  ns
                                 1.4. Analytic continuation of MZF                            13
                 Z ∞                      m
                             1           X    Bk (k−1)
            =     f (x) dx − f (M ) −            f     (M )
               M             2           k=2
                                              k!
                      Z ∞
                   1       em (x)f (m) (x) dx
                −          B
                  m! M
                                        m
                                                          (s)m ∞ B
                                                               Z
                    1           1       X   Bk (s)k−1            em (x)
            =               −       −                   −               dx,
              (s − 1)M s−1 2M s k=2 k! M s+k−1              m! M xs+m

which can be written in the desired form because B0 = 1 and B1 = −1/2. □
   Exercise 1.14. Use Lemma 1.14 (with M = 1, say) and the estimates of
Lemma 1.12 to show that Riemann’s zeta function can be analytically contin-
ued to the half-plane Re s > −L for any real L > 0.
    Introduce the following discrete subset of Cl :
               Σl = s ∈ Cl : s1 ∈ {1}, s1 + s2 ∈ {1, 2} ∪ 2Z≤0 ,
                    

                                       s1 + · · · + sj ∈ Z≤j for j = 3, . . . , l .
The following general result provides the analytic continuation of the MZV
ζ(s) to a meromorphic function on Cl with (at most) simple poles given by Σl .
   Theorem 1.15. Assume l ≥ 2. Then for any s = (s1 , . . . , sl ) ∈ Cl \ Σl
and an even m > l + |σ1 | + · · · + |σl |, we have
                           m
                           X Bk
                 ζ(s) =                 (s1 )k−1 · ζ(s1 + s2 + k − 1, s3 , . . . , sl )
                           k=0
                                  k!
                                                           Z ∞ e
                              (s1 )m X            1            Bm (x)
                            −                  s2       sl            dx.                 (1.17)
                               m! n >···>n ≥1 n2 · · · nl n2 xs1 +m
                                             2       l

    Proof. The absolute convergence of the second series in the formula (1.17)
follows from the estimate
      Z ∞ e                    Z ∞
           Bm (x)         4m!      dx                   4m!
             s+m
                  dx ≤      2m      σ+m
                                        =                               ,
       M   x            (2π)    M x        (2π) (m − 1 + σ)M m−1+σ
                                                2m

where σ = Re s, implying
                                                 Z ∞ e
                 X            1                      Bm (x)
                                                             dx
            n >···>n ≥1
                        n2 n3 · · · nsl l
                         s2 s3
                                                  n2 x
                                                       s1 +m
             2         l

                             4m!                     X          1
                 ≤                                                               .
                                                       m−1+σ
                     (2π)2m (m − 1 + σ1 ) n >···>n ≥1 n2
                                                    2
                                                            1 +σ
                                                                  n3 · · · nσl l
                                                                2 σ3
                                                            l

For the latter sum we use
                 1                |σ |+|σ | |σ |    |σ |   |σ |+|σ |+|σ |+···+|σl |
                               ≤ n2 1 2 n3 3 · · · nl l ≤ n2 1 2 3
                n3 · · · nσl l
          σ1 +σ2 σ3
         n2
                         1.4. Analytic continuation of MZF                         14

and the fact that the number of integers n3 , . . . , nl satisfying n2 > n3 > · · · >
nl ≥ 1 is bounded above by nl−2   2   (because each nj satisfies 1 ≤ nj < n2 ), so
that
           X                  1                 X n|σ1 |+|σ2 |+|σ3 |+···+|σl | nl−2
                                                     2                          2
                     m−1+σ1 +σ2 σ3         σl ≤                  m−1
                   n
        n >···>n ≥1 2
         2
                                n3  · · · nl   2n ≥1
                                                               n 2
                l

converges when m > l + |σ1 | + · · · + |σl |.
   Now, to get the formula (1.17) we apply Lemma 1.14 with s = s1 , n = n1
and M = n2 , and then perform the summation over n2 > n3 > · · · > nl ≥ 1.
   It remains to carefully control the (potential) poles by induction on l. □
   Exercise 1.15. Show that the potential poles of ζ(s) at s ∈ Σl are at
most simple.
   Hint. Notice that the second (multiple) sum in (1.17) is analytic, so that
the only source for poles comes from
                  m
                 X   Bk
                        (s1 )k−1 · ζ(s1 + s2 + k − 1, s3 , . . . , sl ).
                 k=0
                     k!
Use mathematical induction on l and the fact that ζ(s) (when l = 1) has one
simple pole at s = 1.                                                    □
                                        CHAPTER 2

                              Multiple zeta values

                              2.1. First multiple steps
    The quantities
                                                            X                 1
               ζ(s) = ζ(s1 , s2 , . . . , sl ) =                                       ;    (2.1)
                                                                   ns1 ns2 · · · nsl l
                                                   n1 >n2 >···>n ≥1 1 2
                                                                l

for the admissible tuples of integers (all s1 , . . . , sl are positive and s1 > 1) were
introduced in the 1990s by Hoffman and, independently, by Zagier (with the
opposite order of summation on the right-hand side of (2.1)). Those very first
papers produced some Q-linear and Q-polynomial relations as well as indi-
cated a series of conjectures (that has been partly resolved since then) on the
structure of algebraic relations for the family (2.1). Hoffman also introduced
the alternative version
                                                          X                1
             ζ ⋆ (s) = ζ ⋆ (s1 , s2 , . . . , sl ) =                  s1 s2         sl (2.2)
                                                     n ≥n ≥···≥n ≥1
                                                                    n 1 n2  · · · n l
                                                        1   2       l

of generalised Euler sums, with non-strict inequalities in summation; these are
known by the name multiple zeta star values.
   Exercise 2.1. For any admissible index s = (s1 , s2 , . . . , sl ), show the
(dual) relations
                     X                          X
       (a) ζ ⋆ (s) =   ζ(p) and      (b) ζ(s) =     (−1)σ(p) ζ ⋆ (p),
                          p                                               p

where p runs through all indices of the form (s1 ◦ s2 ◦ · · · ◦ sl ) with ‘◦’ being
either the symbol ‘,’ or the sign ‘+’, and the exponent σ(p) denotes the number
of signs ‘+’ in p. (The total number of such indices p is 2l−1 .)
    Hint. This is a purely combinatorial statement; use the inclusion-exclusion
principle for part (b).                                                       □
   Although all relations of series (2.2) may be translated, with the help of
Exercise 2.1, into relations for series (2.1) and vice versa, several identities
possess a more compact form by means of (2.2); for example,
        ζ ⋆ ({2}k , 1) = ζ ⋆ (2, . . . , 2, 1) = 2ζ(2k + 1),            k = 1, 2, . . . .   (2.3)
                              | {z }
                              k times

Observe that the particular instance k = 1 of (2.3) is equivalent to Euler’s
identity ζ(2, 1) = ζ(3).
                                                   15
                                             2.2. The partial-fraction method                                   16

    To each quantity (2.1) (or (2.2)), assign two characteristics: the weight
(or degree) |s| = s1 + s2 + · · · + sl and the length (or depth) ℓ(s) = l. We
shall witness in the course that all relations known so far for the MZVs (2.1)
and (2.2) are weight-preserving.

                                     2.2. The partial-fraction method
    This elementary analytic method is a powerful source of identities for mul-
tiple zeta values.
     Theorem 2.1 (Hoffman’s relations). For any admissible multi-index s =
(s1 , s2 , . . . , sl ), the identity
                      l
                      X
                               ζ(s1 , . . . , sk−1 , sk + 1, sk+1 , . . . , sl )
                      k=1
                                    k −2
                                 l sX
                                 X
                           =                     ζ(s1 , . . . , sk−1 , sk − j, j + 1, sk+1 , . . . , sl )    (2.4)
                                k=1 j=0
                                sk ≥2

holds.
   Proof. For any k = 1, 2, . . . , l, we have
           X                    1                     X                  1
                                             +                          sk+1
                       n
    nk >nk+1 >···>nl ≥1 k
                         sk +1 sk+1       sl
                              nk+1 · · · nl
                                                                     sk
                                                                    n mnk+1 · · · nsl l
                                               nk >m>nk+1 >···>nl ≥1 k
                   X                       1
        =                                sk+1
          n ≥m>n
                                n mnk+1 · · · nsl l
                       >···>n ≥1 k
                                  sk
              k                k+1           l
                                                  nk
                        X                         X                   1
         =                                        sk+1             ,
             nk >nk+1 >···>nl ≥1 m=nk+1 +1
                                           mnskk nk+1  · · · nsl l

hence
     ζ(s1 , . . . , sk−1 , sk + 1, sk+1 , . . . , sl ) + ζ(s1 , . . . , sk−1 , sk , 1, sk+1 , . . . , sl )
                          X                                1
        =                                              sk +1 sk+1
            n1 >···>nk >nk+1 >···>nl ≥1 1
                                         n · · · nk nk+1 · · · nsl l
                                            s1

                                X                                     1
                +                                               sk       sk+1
                    n >···>n >m>n     >···>n ≥1 1
                                                        s1
                                                      n · · · nk mnk+1        · · · nsl l
                           1             k        k+1        l
                                                           nk
                                  X                        X                        1
         =                                                            sk+1
              n1 >···>nk >nk+1 >···>nl ≥1 m=nk+1 +1
                                                    mns11 · · · nskk nk+1  · · · nsl l
                                         nk
                        X      1        X    1
         =                s1 s2     sl
                         n n · · · nl m=n +1 m
           n >n >···>n ≥1 1 2
                  1    2             l                               k+1
                                           2.2. The partial-fraction method                                          17

and
  X l
                                                                                                              
         ζ(s1 , . . . , sk−1 , sk + 1, sk+1 , . . . , sl ) + ζ(s1 , . . . , sk−1 , sk , 1, sk+1 , . . . , sl )
  k=1
                                             n1
                   X           1            X   1
     =                   s1 s2          sl
                        n n · · · nl m=1 m
       n1 >n2 >···>nl ≥1 1 2
                                             ∞          
             X                 1            X     1   1
     =                                              −      .                                               (2.5)
                        ns1 ns2 · · · nsl l m=1 m n1 + m
       n >n >···>n ≥1 1 2
           1       2           l

From now on, to each collection n1 > n2 > · · · > nl ≥ 1 we will associate
the set of parameters m1 , m2 , . . . , ml ≥ 1 such that nk = mk + · · · + ml for
k = 1, 2, . . . , l; alternatively, mk = nk − nk+1 for k = 1, . . . , l − 1 and ml = nl .
    Now notice the following partial-fraction decomposition (where both sides
are viewed as functions of m for n ̸= 0 fixed):
                                                   s−1
                                       1       1   X       1
                                           s
                                             = s −                 ;                                       (2.6)
                                   m(n + m)   n m j=0 n (n + m)s−j
                                                       j+1

for the proof, it is sufficient to sum a geometric progression on the right-hand
side. For n = n1 and s = s1 this implies
                              sX  1 −2
          1    1         1                      1                1
          s1      −              =        j+1             +             .
         n1 m n + m1                j=0
                                                    s
                                         n1 (n1 + m) 1 −j   m(n1 + m)s1

Going on in equality (2.5) we find that
  l
  X                                                                                                              
         ζ(s1 , . . . , sk−1 , sk + 1, sk+1 , . . . , sl ) + ζ(s1 , . . . , sk−1 , sk , 1, sk+1 , . . . , sl )
  k=1
          1 −2
         sX                X               X      1
     =
          j=0 n1 >n2 >···>nl ≥1 m≥1
                                    (n1 + m)s1 −j nj+1   s2
                                                    1 n2 · · · nl
                                                                 sl

                    X           X              1
            +
              n >n >···>n ≥1 m≥1
                                    m(n1 + m)s1 ns22 · · · nsl l
                       1   2           l

          1 −2
         sX
     =             ζ(s1 − j, j + 1, s2 , . . . , sl )
          j=0
                           X               X     1
               +
                   n >···>n ≥1 m,m ≥1
                                      m(n2 + m + m1 )s1 ns22 · · · nsl l
                       2           l       1

          1 −2
         sX                                                       X                        1
     =             ζ(s1 − j, j + 1, s2 , . . . , sl ) +                                               ,    (2.7)
          j=0
                                                                              ns1 m1 ns22 · · · nsl l
                                                          n0 >n1 >n2 >···>n ≥1 0
                                                                            l

where in the latter tuple sum we interchanged m ↔ m1 and set n0 = n1 + m.
Using now identity (2.6) with m = mk−1 , n = nk = nk−1 − mk−1 and s = sk ,
                                       2.2. The partial-fraction method                                            18

we deduce that
                                                  k −1
                                                 sX
                   1               1                           1
                     sk =                  s
                                               +        j+1
               mk−1 nk    mk−1 (nk + mk−1 )  k
                                                  j=0
                                                       nk (nk−1 + mk )sk −j
                                     k −1
                                    sX
                                              1                 1
                               =         sk −j j+1 + sk                        for k = 2, . . . , l,
                                    j=0
                                        nk−1 nk
                                                    nk−1 mk−1

therefore
                       X                                    1
                                               sk−1            sk+1
                                ns1 ns2 · · · nk−2
               n0 >n1 >···>nl ≥1 0 1
                                                    mk−1 nskk nk+1  · · · nsl l
                        k −1
                       sX              X                                    1
                  =                                        sk−1 sk −j j+1 sk+1
                                            ns1 ns2 · · · nk−2
                       j=0 n0 >n1 >···>nl ≥1 0 1
                                                               nk−1 nk nk+1 · · · nsl l
                                       X                                    1
                         +                                     sk−1 sk        sk+1
                                                ns1 ns2 · · · nk−2
                               n0 >n1 >···>nl ≥1 0 1
                                                                   nk−1 mk−1 nk+1  · · · nsl l
                        k −1
                       sX
                  =            ζ(s1 , . . . , sk−1 , sk − j, j + 1, sk+1 , . . . , sl )
                       j=0
                                       X                                   1
                         +                                     sk−1 sk      sk+1             ,              (2.8)
                                                ns1 ns2 · · · nk−2
                               n0 >n1 >···>nl ≥1 0 1
                                                                   nk−1 mk nk+1  · · · nsl l

where again we swap the role of mk−1 and mk . Applying consequently identi-
ties (2.8) for k = 2, . . . , l for the second multiple sum on the right-hand side
of equality (2.7), we obtain
l
X                                                                                                              
       ζ(s1 , . . . , sk−1 , sk + 1, sk+1 , . . . , sl ) + ζ(s1 , . . . , sk−1 , sk , 1, sk+1 , . . . , sl )
k=1
        1 −2
       sX
   =           ζ(s1 − j, j + 1, s2 , . . . , sl )
        j=0
                  k −1
               l sX
               X
          +                ζ(s1 , . . . , sk−1 , sk − j, j + 1, sk+1 , . . . , sl )
               k=2 j=0
                       X                       1
          +
                               ns1 ns2 · · · nsl−1
               n0 >n1 >···>n ≥1 0 1
                                                k
                                                   ml
                                l

          k −2
       l sX
       X
   =                 ζ(s1 , . . . , sk−1 , sk − j, j + 1, sk+1 , . . . , sl )
        k=1 j=0
               l
               X                                                                  X                    1
          +          ζ(s1 , . . . , sk−1 , 1, sk , sk+1 , . . . , sl ) +
               k=2
                                                                                            ns1 ns2 · · · nsl−1
                                                                           n0 >n1 >···>nl ≥1 0 1
                                                                                                             k
                                                                                                                nl
                                     2.2. The partial-fraction method                     19

            k −2
         l sX
         X
     =               ζ(s1 , . . . , sk−1 , sk − j, j + 1, sk+1 , . . . , sl )
         k=1 j=0
               l
               X
           +         ζ(s1 , . . . , sk , 1, sk+1 , . . . , sl ).                       (2.9)
               k=1

Reducing both sides by the latter sum over k, we finally arrive at the desired
identity (2.4).                                                             □
     If l = 1, the statement of Theorem 2.1 can be written in the following form.
     Theorem 2.2 (Euler). For any integer s ≥ 3, the identity
                                            s−1
                                            X
                                                  ζ(j, s − j) = ζ(s)                  (2.10)
                                            j=2

takes place.
   Note also that, in the case s = 3, identity (2.10) becomes nothing else but
Euler’s relation (1.13).
   As a simple companion to Theorem 2.2 we have the following.
     Theorem 2.3 (Weighted analogue of Euler’s theorem [33]). For any s ≥ 3,
                                    s−1
                                    X
                                           2j ζ(j, s − j) = (s + 1)ζ(s).              (2.11)
                                     j=2

     Proof. We follow the proof from [44]. Write the left-hand side of (2.11)
as
     s−1       ∞                 s−1 X ∞                      ∞
                                                          s−1 X
     X
           j
               X      1          X              2j        X         2j
         2                     =                        +
     j=2   m,n=1
                 (n + m)j ns−j   j=2 m,n=1
                                           (n + m)j ns−j j=2 n=1 (2n)j ns−j
                                                         m̸=n
                                                  ∞             s−1
                                                  X  1 X (2n)j
                                             =                       + (s − 2)ζ(s).
                                               m,n=1
                                                     ns j=2 (n + m)j
                                                  m̸=n

The geometric summation in j reduces the remaning sum to
                ∞ 
                             2s
                                                        
               X                                 4
                                         −               .
              m,n=1
                    (n2 − m2 )(n + m)s−2 (n2 − m2 )ns−2
                       m̸=n

The first summand has antisymmetry in the variables m, n and hence vanishes
when summed. For the second one we use the partial-fraction decomposition
to obtain
         ∞                 ∞                 
        X      1       1 X       1        1
             2 − n2
                    =                −
        m=1
            m         2n m=1
                               m − n    m+n
           m̸=n                            m̸=n
                            2.2. The partial-fraction method                               20

                            n−1     ∞                     
                         1 X        X          1         1
                     =           +                 −
                        2n m=1 m=n+1         m−n m+n
                            X n−1       2n−1      ∞            
                         1         1     X 1 X          1      1
                     =       −        −         +          −
                        2n     k=1
                                   m k=n+1 k k=1 k k + 2n
                            X n−1       2n−1      2n   
                         1         1     X 1 X        1
                     =       −        −         +
                        2n     k=1
                                   m    k=n+1
                                              k   k=1
                                                      k
                                     
                         1     1    1       3
                     =     ·     +      = 2,
                        2n     n 2n        4n
and the result follows.                                                                    □
   Exercise 2.2. (a) Show that
                         X ∞     2
                      2        1
                  ζ(2) =             = ζ(4) + 2ζ(2, 2).
                           n=1
                               n2
   (b) Verify that ζ(2, 2) = 43 ζ(4).
   (c) Conclude that ζ(2)2 = 52 ζ(4); in particular, the formula ζ(2) = π 2 /6
implies ζ(4) = π 4 /90.
   Hint. (b) Use Theorems 2.2 and 2.3 for s = 4.                                           □
   Exercise 2.3. For s ≥ 4 even, show that
                              s−1
                              X                      1
                                  (−1)j ζ(j, s − j) = ζ(s).
                              j=2
                                                     2
   Exercise 2.4 (Euler). For s ≥ 3, show that
                                      s−2
                                      X
                  2ζ(s − 1, 1) +             ζ(j)ζ(s − j) = (s − 1)ζ(s).
                                       j=2

In other words, ζ(s − 1, 1) can be always expressed in terms of single zeta
values.
   In [21], Hoffman and Ohno proved the following result also by means of
the partial-fraction method. A somewhat simpler proof was given by Ohno
[30] (see also the later publication [31] by Ohno and Wakabayashi).
     Theorem 2.4 (Cyclic sum theorem). For any admissible multi-index s =
(s1 , s2 , . . . , sl ), the identity
            l
            X
                  ζ(sk + 1, sk+1 , . . . , sl , s1 , . . . , sk−1 )
            k=1
                       k −2
                    l sX
                    X
               =                ζ(sk − j, sk+1 , . . . , sl , s1 , . . . , sk−1 , j + 1)
                   k=1 j=0
                   sk ≥2
                                       2.3. Calculation of MZVs                                    21

holds.
    One of the consequences of the cyclic sum theorem is independence of the
sum of all multiple zeta values of fixed length and fixed weight on the length;
this statement, as well as Theorem 2.1, generalises Euler’s theorem.
   Theorem 2.5 (Sum theorem). For any integers s > 1 and l ≥ 1, the
identity
                    X
                            ζ(s1 , s2 , . . . , sl ) = ζ(s)
                            s1 >1,s2 ≥1,...,sl ≥1
                             s1 +s2 +···+sl =s

holds.
   We prove this theorem in Section 4.3. In fact, Theorems 2.1 and 2.5 are
particular instances of Ohno’s relations (Theorem 5.1), which we discuss in
Chapter 5.

                                2.3. Calculation of MZVs
    There are several ways of computing the MZVs efficiently based on their
different representations. Notice that the original series (2.1) defining ζ(s) is
somewhat inefficient, because the convergence is very slow (already for l = 1).
The method we discuss below was designed by R. Crandall; later on in the
course we shall witness a completely different strategy (see Proposition 3.8).
    First observe the equality
            Z ∞                       Z ∞
         1        s−1 −xn         1                               1
                 x e      dx = s           (nx)s−1 e−nx d(nx) = s          (2.12)
       Γ(s) 0                  n Γ(s) 0                           n
valid for Re s > 0; this follows from (1.6).
   Lemma 2.6. For admissible indices s = (s1 , . . . , sl ) ∈ Zl>0 ,
                       Z     Z     l
              X                   Y                                  duj
    ζ(s) =               ···          (uj − uj−1 )sj −1 e−uj mj            ,                   (2.13)
           m ,...,m ≥1            j=1
                                                                   Γ(s j )
              1    l        ul >ul−1 >···>u1 >u0

where we set u0 = 0.
   Proof. It follows from (2.12) that
                              Z     Z Yl
                     X                     s −1         dxj
         ζ(s) =                 ···       xj j e−xj nj
                  n >···>n ≥1         j=1
                                                       Γ(sj )
                        1          l     x1 ,...,xl >0
                                        Z             l
                                                    Z Y
                             X                             s −1 −xj (mj +···+ml )    dxj
                  =                          ···          xj j   e                         .
                       m1 ,...,ml ≥1 x ,...,x >0 j=1
                                                                                    Γ(sj )
                                         1      l
                                       Pk
Change the variables uk = j=1 xj and use the fact that the Jacobian of this
transformation is the identity.                                          □
                                             2.3. Calculation of MZVs                                              22

    For a fixed real parameter u > 0, consider the subdomains of the integration
domain
               T = {(u1 , . . . , ul ) : ul > ul−1 > · · · > u1 > 0} ∈ Rl>0
in (2.13) given as follows:
   Tk = Tk (u) = {(u1 , . . . , ul ) : ul > · · · > uk+1 > u > uk > · · · > u0 } ∈ Rl>0
for k = 0, 1, . . . , l − 1, and
    Tl = Tl (u) = {(u1 , . . . , ul ) : u > ul > · · · > u1 > u0 } ∈ Rl>0 .
Clearly, the domain T is the disjoint union of the l+1 subdomains T0 , T1 , . . . , Tl .
   Denote
         f (s; u) = fl (s1 , . . . , sl ; u)
                                          Z      Z                    l
                        X                                            Y                              duj
                  =                          ···                         (uj − uj−1 )sj −1 e−uj mj
                               m1 ,...,ml ≥1 u >u                    j=1
                                                                                                   Γ(sj )
                                             l      l−1 >···>u1 >u

(it differs from the one in (2.13) by reducing the integration domain to ul >
ul−1 > · · · > u1 > u, so that f (s; 0) = ζ(s)) and
   g(s; q; u) = gl (s1 , . . . , sl ; q; u)
                                        Z       Z                            l
                    X                                                       Y                              duj
              =                             ···                       uql       (uj − uj−1 )sj −1 e−uj mj
                         m1 ,...,ml ≥1 u>u >u                               j=1
                                                                                                          Γ(sj )
                                             l      l−1 >···>u1 >u0

(the integration domain is now bounded with an extra twist of the integrand
by uql implemented, for q = 0, 1, 2, . . . ). These definitions immediately imply
     X Z          Z Yl
                                                   duj
              ···       (uj − uj−1 )sj −1 e−uj mj        = fl (s1 , . . . , sl ; u), (2.14)
  m ,...,m ≥1       j=1
                                                  Γ(sj )
    1      l          T0 (u)
                  Z        Z Yl
        X                                                   duj
                       ···       (uj − uj−1 )sj −1 e−uj mj        = gl (s1 , . . . , sl ; 0; u). (2.15)
  m1 ,...,ml ≥1              j=1
                                                           Γ(sj )
                      Tl (u)

    Exercise 2.5. It follows from the definition of g(s; q; u) that
                                      g(s; 0; ∞) = lim g(s; 0; u) = ζ(s)
                                                           u→∞
for all admissible multi-indices s. Compute
                                           g(s; q; ∞) = lim g(s; q; u)
                                                                u→∞
for q = 1, 2, . . . .
    Hint. Compute the q-th power of
                  ul = (ul − ul−1 ) + (ul−1 − ul−2 ) + · · · + (u2 − u1 ) + u1
using the multinomial theorem (or apply repeatedly the binomial theorem).
                                                                       □
                                            2.3. Calculation of MZVs                                             23

   Lemma 2.7. For k = 1, . . . , l − 1,
     X Z          Z Yl
                                                   duj
              ···       (uj − uj−1 )sj −1 e−uj mj
  m ,...,m ≥1       j=1
                                                  Γ(sj )
    1     l        Tk (u)
               sk+1 −1
                X (−1)q
           =            gk (s1 , . . . , sk ; q; u)fl−k (sk+1 − q, sk+2 , . . . , sl ; u). (2.16)
                q=0
                    q!

    Proof. We use the binomial expansion
                                        sk+1 −1
    1                 sk+1 −1      1     X       (sk+1 − 1)!     sk+1 −q−1
          (uk+1 − uk )        =                                 uk+1       (−uk )q
 Γ(sk+1 )                       Γ(sk+1 ) q=0 q! (sk+1 − q − 1)!
                                              sk+1 −1k+1 −q−1
                                          X (−1)q usk+1
                                        =                     uqk
                                          q=0
                                              q! Γ(sk+1 − q)
and integrate over the groups of variables u1 , . . . , uk and uk+1 , . . . , ul separately.
                                                                                          □
    Combining equalities (2.14)–(2.16) we arrive at the following result.
    Proposition 2.8. In the above notation,
 ζ(s) = gl (s1 , . . . , sl ; 0; u) + fl (s1 , . . . , sl ; u)
                        X−1 (−1)q
                   l−1 sk+1
                   X
               +                              gk (s1 , . . . , sk ; q; u)fl−k (sk+1 − q, sk+2 , . . . , sl ; u).
                   k=1      q=0
                                       q!

    The expression found shows that, for any positive u, every MZV can be
written as a finite sum of products of the functions f (s; u) and g(s; q; u). Our
next step is to find efficient algorithms for computing these functions, at least
for some u > 0.
    Proposition 2.9. For s1 , . . . , sl positive integers and u > 0 real,
                                                 s −1
                                               ∂ 1 e−ut
                                          
                     1          X                                    1
      f (s; u) =                           −                    · s2          .
                 (s1 − 1)! n >n >···>n ≥1     ∂t        t t=n1 n2 · · · nsl l
                                        1     2         l

    The series for f (s; u) is rapidly convergent, as a geometric series with rate
e−u , especially for large u.
   Proof. Take nj = mj + · · · + ml for j = 1, . . . , l and nl+1 = 0, so that
                          Z     Z     l
                 X                  Y                                       duj
   f (s; u) =               ···         (uj − uj−1 )sj −1 e−uj (nj −nj+1 )
              n >···>n ≥1           j=1
                                                                           Γ(sj )
                    1        l    ul >ul−1 >···>u1 >u
                                        Z           Z       l
                        X                                   Y                                          duj
               =                              ···                 (uj − uj−1 )sj −1 e−(uj −uj−1 )nj          .
                   n1 >···>nl ≥1 u >u                       j=1
                                                                                                      Γ(sj )
                                   l    l−1 >···>u1 >u
                                          2.3. Calculation of MZVs                                        24

Now notice that the summand is obtained from applying the differential oper-
ator                     s1 −1          s2 −1          sl −1
                       ∂                ∂                ∂
                    −              −              ··· −
                      ∂n1             ∂n2               ∂nl
to
         Z      Z      l
                      Y                    duj
            ···           e−(uj −uj−1 )nj
                      j=1
                                          Γ(sj )
      ul >ul−1 >···>u1 >u
                                              l                                      l
                                                                        e−un1 Y
                      Z           Z           Y
                                                   −xj nj    dxj                            1
            =               ···                   e                =                              .
                                                            Γ(sj )   n1 n2 · · · nl j=1 (sj − 1)!
                 x1 >u, x2 >0, ..., xl >0 j=1

This implies the desired form of f (s; u).                                                                □
   To study g(s; q; u), we first observe that, when u < 2π, we can use
                                  ∞
                                  X
                                              −uj mj       e−uj        1
                                          e            =          =
                                  mj =1
                                                         1 − e−uj   euj − 1

within the range 0 < uj < u for j = 1, . . . , l, so that we can write
                                     l
                                         (uj − uj−1 )sj −1 duj
                    Z      Z        Y
                                  q
   g(s; q; u) =        ···       ul
                                    j=1
                                                euj − 1     Γ(sj )
                   u>ul >ul−1 >···>u1 >u0

                                   uql
                     Z u                 Z ul
                         dul                   dul−1 (ul − ul−1 )sl −1
                 =                                                     ···
                                 ul
                    0 Γ(sl ) e − 1 0          Γ(sl−1 )    eul−1 − 1
                               du2 (u3 − u2 )s3 −1 u2 du1 (u2 − u1 )s2 −1 us11 −1
                        Z u3                           Z
                     ×                                                            .
                          0   Γ(s2 )      eu2 − 1       0  Γ(s1 )       eu1 − 1
   Recall that
                                                      ∞
                                                  z   X  Bk k
                                                z
                                                    =       z .                                       (2.17)
                                               e − 1 k=0 k!
Change variables uj = vj uj+1 for j = 1, . . . , l − 1 and ul = vl u in the resulting
integral for g(s; q; u). We get
            du1 (u2 − u1 )s2 −1 us11 −1
     Z u2

       0   Γ(s1 )          eu1 − 1
           Z 1
                u2 dv1                                       X Bk
         =                (u2 − u2 v1 )s2 −1 (u2 v1 )s1 −2             1
                                                                         (u2 v1 )k1
             0 Γ(s1 )                                        k1 ≥0
                                                                    k1 !
           X Bk                                  Z  1
                                           1
         =           1
                       uk21 +s1 +s2 −2 ·              v1k1 +s1 −2 (1 − v1 )s2 −1 dv1
           k ≥0
                 k 1 !                   Γ(s 1 )  0
             1
            X Bk                                    Γ(s2 ) Γ(k1 + s1 − 1)
        =               1
                            uk21 +s1 +s2 −2 ·                                ,
            k1 ≥0
                    k1 !                          Γ(s1 ) Γ(k1 + s1 + s2 − 1)
                                    2.3. Calculation of MZVs                            25

where the Euler integral of the first kind was used (see Exercise 1.2); then
           du2 (u3 − u2 )s3 −1 uk21 +s1 +s2 −2
    Z u3

      0   Γ(s2 )             eu2 − 1
          X Bk                                   Γ(s3 ) Γ(k1 + k2 + s1 + s2 − 2)
        =          2
                     uk31 +k2 +s1 +s2 +s3 −3 ·                                      ,
          k ≥0
                k2 !                           Γ(s2 ) Γ(k1 + k2 + s1 + s2 + s3 − 2)
            2

and so on. The final result reads
                                      l
                    1       X Y          Bkj Kl +Sl +q−l Γ(Kl + Sl + q − l)
     g(s; q; u) =                             ·u
                  Γ(s1 ) k ,...,k ≥0 j=1 kj !           Γ(Kl + Sl + q + 1 − l)
                            1       l

                          l−1
                          Y    Γ(Kj + Sj − j)
                      ×                        ,
                          j=1
                              Γ(Kj + Sj+1 − j)
where Kj = k1 + · · · + kj and Sj = s1 + · · · + sj for j = 1, . . . , l.
    Proposition 2.10. For 0 < u < 2π,
                                     l                        l−1
                   1       X Y          Bkj    uKl +Sl +q−l   Y   Γ(Kj + Sj − j)
  g(s; q; u) =                              ·               ·                     .
                 Γ(s1 ) k ,...,k ≥0 j=1 kj ! Kl + Sl + q − l j=1 Γ(Kj + Sj+1 − j)
                        1       l

   Because the series in (2.17) converges in the disk |z| < 2π, the sum we
deduce for g(s; q; u) converges absolutely at the geometric rate u/(2π).
    Exercise 2.6. To compute the multiple sums for f (s; u) in Proposition 2.9
and for g(s; q; u) in Proposition 2.10 with a given accuracy ε, one needs
(roughly) to sum the first expression over n1 ≤ N and the second one over
k1 + · · · + kl ≤ K, where
                           − log ε               log ε
                     N∼            and K ∼               .
                              u              log(u/(2π))
What is an (approximate) optimal value u for both sums? This can be used
for computing the multiple zeta value ζ(s) numerically on the basis of Propo-
sition 2.8.
   Exercise 2.7. Implement a code for computing ζ(s) and ζ(s, t), single and
double zeta values, where s ≥ 2 and t ≥ 1 are integers. Choose a reasonable
accuracy for your numerical calculation, for example, 10−10 .
                                       CHAPTER 3

          Algebraic relations of multiple zeta values

    In this part, we expose the standard algebraic setup of the MZVs. It
is expected that all known algebraic relations (that is, numerical identities)
over Q for the quantities (2.1) are produced by the so-called double shuffle
relations which we describe below.

                      3.1. Algebra of multiple zeta values
    It is useful to represent ζ as a linear map of a certain polynomial algebra
into the field of real numbers. Consider coding of multi-indices s by words (i.e.,
by monomials in non-commutative variables) over the alphabet X = {x0 , x1 }
by the rule
                        s 7→ xs = xs01 −1 x1 xs02 −1 x1 · · · xs0l −1 x1 .
Set
                                    ζ(xs ) = ζ(s)                            (3.1)
for all admissible (starting with x0 and ending on x1 ) words; then the weight
(or degree) |xs | = |s| coincides with the total degree of the monomial xs , while
the length ℓ(xs ) = ℓ(s) expresses the degree with respect to the variable x1 .
    Let Q⟨X⟩ = Q⟨x0 , x1 ⟩ be the graded by degree Q-algebra (where the degree
of each variable x0 and x1 is agreed to be 1) of polynomials in the two non-
commutative variables; we identify the algebra Q⟨X⟩ with the graded Q-vector
space H spanned over monomials in the variables x0 and x1 . Define as well the
graded Q-vector spaces H1 = Q1⊕Hx1 and H0 = Q1⊕x0 Hx1 , where 1 denotes
the unit (the empty word of weight 0 and length 0) of the algebra Q⟨X⟩.
Then H1 may be regarded as the subalgebra of Q⟨X⟩ generated by the words
ys = xs−1               0
        0 x1 , while H is the Q-vector space spanned over all admissible words.
Now, we may view the function ζ as the Q-linear map ζ : H0 → R defined by
the relations ζ(1) = 1 and (3.1).
                                   
    Define the multiplications (the shuffle product) on H and ∗ (the harmonic
or stuffle product) on H1 by the rules
                  1    w = w  1 = w,            1∗w =w∗1=w                  (3.2)
for any word w, and
              xj u    x v = x (u  x v) + x (x u  v),
                        k      j         k        k   j                       (3.3)
                yj u ∗ yk v = yj (u ∗ yk v) + yk (yj u ∗ v) + yj+k (u ∗ v)    (3.4)
for any words u, v, any letters xj , xk , and any generators yj , yk of the subalge-
bra H1 , respectively, distributing then rules (3.2)–(3.4) on the whole algebra H
                                             26
                           3.1. Algebra of multiple zeta values                       27

and the whole subalgebra H1 by linearity. Sometimes it becomes useful to
spread the stuffle product on the whole algebra H, formally adding the rule
                                xj0 ∗ w = w ∗ xj0 = wxj0                           (3.5)
for any word w and integer j ≥ 1, to rule (3.4).
      Exercise 3.1. Compute x0 x1            x x and x x ∗ x x .
                                               0 1         0 1       0 1

   Exercise 3.2. Use the inductive argument to prove commutativity and
associativity of each of the multiplications.
                                                       
    The corresponding algebras H = (H, ), H1∗ = (H1 , ∗) (and also H∗ =
(H, ∗)) are examples of so-called Hopf algebras.
    The following two statements motivate consideration of the introduced mul-
tiplications  and ∗.
    Theorem 3.1. The map ζ is a homomorphism of the shuffle algebra H0 =
      
(H0 , ) into R, that is,
                 ζ(w1    w ) = ζ(w )ζ(w ) for all w , w ∈ H .
                            2           1      2                 1    2
                                                                               0
                                                                                   (3.6)
   Theorem 3.2. The map ζ is a homomorphism of the stuffle algebra H0∗ =
  0
(H , ∗) into R, that is,
                 ζ(w1 ∗ w2 ) = ζ(w1 )ζ(w2 ) for all            w1 , w2 ∈ H0 .      (3.7)
    Later we give detailed proofs of the two theorems using the differential-
difference origin of the multiplications           
                                          and ∗ in suitable functional models
of the algebras H and H0∗ .
    One more family of identities is given by the following statement, which
is equivalent to Hoffman’s relations in Theorem 2.1; we will discuss later its
different proof.
      Theorem 3.3. The map ζ satisfies the relations
                    ζ(x1 w − x ∗ w) = 0 for all w ∈ H
                                    1
                                                                           0
                                                                                   (3.8)
(in particular, the polynomials x  w − x ∗ w belong to H ).
                                        1              1
                                                                           0

    All (rigorously and experimentally) known identities for the multiple zeta
values (are expected to) ‘follow’ from identities (3.6)–(3.8) — the double shuffle
relations. This makes the following conjecture looking truthful.
   Conjecture 3.4. All linear relations over Q of multiple zeta values are
generated by identities (3.6)–(3.8); equivalently,
                    ker ζ = {u     v − u ∗ v : u ∈ H , v ∈ H }.
                                                           1           0

   In particular, the conjecture implies that all relations of MZVs over Q are
homogeneous in weight.
    Exercise 3.3. Using Theorems 3.1–3.3 show that:
  (i) every MZV of weight 4 is a rational multiple of ζ(4);
 (ii) every MZV of weight 5 is in the Q-linear span of ζ(5) and ζ(2)ζ(3);
                  3.2. Shuffle algebra of generalised polylogarithms                                28

(iii) every MZV of weight 6 is in the Q-linear span of ζ(6) and ζ(3)2 ;
(iv) every MZV of weight 7 is in the Q-linear span of ζ(7), ζ(2)ζ(5) and
      ζ(2)2 ζ(3).
In other words, any MZV of weight up to 7 can be expressed algebraically
through the (single) zeta values ζ(s).
    Exercise 3.4. (a) Using the stuffle product show that
                            n
                            X                                        n
                                                                     X
                  n                        i              n−i
ζ(2m + 1)ζ({2} ) =                ζ({2} , 2m + 1, {2}           )+         ζ({2}i−1 , 2m + 3, {2}n−i )
                            i=0                                      i=1

    for integers m, n ≥ 1.
(b) Deduce from part (a) that
           n
           X                                                n
                                                            X
                (−1)m−1 ζ(2m + 1)ζ({2}n−m ) =                        ζ({2}i−1 , 3, {2}n−i )
           m=1                                               i=1

    for n = 1, 2, . . . .

            3.2. Shuffle algebra of generalised polylogarithms
   In order to prove shuffle relations (3.6) for multiple zeta values, let us define
the generalised polylogarithms
                              X              z n1
               Lis (z) =                                   , |z| < 1,          (3.9)
                                       ns1 ns2 · · · nsl l
                         n >n >···>n ≥1 1 2
                                  1    2       l

for any collection of positive integers s1 , s2 , . . . , sl . By definition,
         Lis (1) = ζ(s),              s ∈ Zl ,     s1 ≥ 2, s2 ≥ 1, . . . , sl ≥ 1.             (3.10)
Taking, as before for multiple zeta values,
                              Lixs (z) = Lis (z),          Li1 (z) = 1,                        (3.11)
let us extend action of the map Li : w 7→ Liw (z) by linearity on the graded
algebra H1 (not H, since multi-indices are coded by words in H1 ).
    Lemma 3.5. Let w ∈ H1 be an arbitrary non-empty word and xj the first
letter in its record (that is, w = xj u for some word u ∈ H1 ). Then
                            d Liw (z) = d Lixj u (z) = ωj (z) Liu (z),                         (3.12)
where                                      
                                             dz
                                           
                                                                if xj = x0 ,
                        ωj (z) = ωxj (z) =   z                                                 (3.13)
                                              dz
                                           
                                                                if xj = x1 .
                                             1−z
                   3.2. Shuffle algebra of generalised polylogarithms                              29

    Proof. Assuming w = xj u = xs for some multi-index s, we have
                                           X             z n1
            d Liw (z) = d Lis (z) = d
                                                    ns1 ns2 · · · nsl l
                                      n >n >···>n ≥1 1 2
                                                   1       2           l
                                                                   n1 −1
                                       X                       z
                             =                                            dz.
                                                  ns1 −1 ns22 · · · nsl l
                                 n1 >n2 >···>nl ≥1 1

Therefore, in the case s1 > 1 (corresponding to the letter xj = x0 ), we obtain
                               1      X                 z n1
                d Lix0 u (z) =                                           dz
                               z n >n >···>n ≥1 ns11 −1 ns22 · · · nsl l
                                  1  2                 l

                                  1
                                 = Lis1 −1,s2 ,...,sl (z) dz = ω0 (z) Liu (z)
                                  z
and, in the case s1 = 1 (corresponding to the letter xj = x1 ), we get
                                                                                       ∞
                      X            z n1 −1                X                1          X
d Lix1 u (z) =                    s2         sl dz =                 s2          sl          z n1 −1 dz
                                n
               n1 >n2 >···>nl ≥1 2
                                     · · · n l                     n
                                                      n2 >···>nl ≥1 2
                                                                         · · · n l n1 =n2 +1
                                            n2
                  1        X              z                   1
             =                         s2        sl dz =          Lis2 ,...,sl (z) dz = ω1 (z) Liu (z),
               1 − z n >···>n ≥1 n2 · · · nl              1−z
                         2       l

and the result follows.                                                                            □

    Lemma 3.5 motivates another definition of the generalised polylogarithms,
now defined for all elements of the algebra H. As before, it is sufficient to give
it for words w ∈ H only, distributing then over all algebra by linearity; set
Li1 (z) = 1 and
                  k
                  log z
                 
                                      if w = xk0 for some k ≥ 1,
        Liw (z) = Z k!z                                                     (3.14)
                        ωj (z) Liu (z) if w = xj u contains letter x1 .
                 
                 
                 
                         0

Evidently, Lemma 3.5 remains true for this extended version (3.14) of the
polylogarithms (the fact yields coincidence of the newly-defined polylogarithms
with the ‘old’ ones (3.11) for words w in H1 ).
    Exercise 3.5. (a) Compute Lix1 x0 (z).
    (b) Show that
            lim z −1/2 Liw (z) = 0 if the word w ∈ H contains letter x1 .
           z→0+

    Hint. (a) It is standard to use
                                                 d δ
                                      log z =       (z )     .
                                                 dδ      δ=0
                 3.2. Shuffle algebra of generalised polylogarithms                       30

We get
                    Z z                    Z z               Z z
                                               log z dz   d       zδ
        Lix1 x0 (z) =     ω1 (z) Lix0 (z) =             =               dz
                       0                     0   1−z      dδ 0 1 − z       δ=0
                         Z zX  ∞                        ∞   n+δ
                       d                            d  X  z
                    =             z n−1+δ dz     =
                      dδ 0 n=1               δ=0   dδ n=1 n + δ δ=0
                       ∞ 
                           (log z) z n z n
                      X                      
                    =                   − 2 = (log z) Li1 (z) − Li2 (z).
                      n=1
                                n         n
   (b) Use the fact that if f (z) is continuous on (0, 1) and z −1/2 f (z) → 0 as
z → 0+ , then                          Z        z
                                F (z) =             f (z) dz
                                            0
is also continuous on (0, 1) and satisfies z −1/2 F (z) → 0 as z → 0+ . Of course,
this fact should be also established (by using traditional analysis techniques).
                                                                                □
    Lemma 3.6. The map w 7→ Liw (z) is a homomorphism of the algebra H
into C((0, 1); R).
   Proof. We have to verify the equalities
                Liw1 w2 (z) = Liw1 (z) Liw2 (z) for all w1 , w2 ∈ H;                 (3.15)
it is sufficient to do this job for words w1 , w2 ∈ H. We will prove equality (3.15)
by induction on the quantity |w1 | + |w2 |. If w1 = 1 or w2 = 1, relation (3.15)
becomes tautological by (3.2). Otherwise, w1 = xj u and w2 = xk v, hence by
Lemma 3.5 and the inductive hypothesis we have
                                                      
         d Liw1 (z) Liw2 (z) = d Lixj u (z) Lixk v (z)
                            = d Lixj u (z) · Lixk v (z) + Lixj u (z) · d Lixk v (z)
                            = ωj (z) Liu (z) Lixk v (z) + ωk (z) Lixj u (z) Liv (z)
                            = ωj (z) Liuxk v (z) + ωk (z) Lixj uv (z)
                            = d Lixj (uxk v) (z) + Lixk (xj uv) (z)
                                                                     

                            = d Lixj uxk v (z)
                            = d Liw1 w2 (z).
Thus,
                       Liw1 (z) Liw2 (z) = Liw1 w2 (z) + C,               (3.16)
                    +
and letting z → 0 if at least one of the words w1 , w2 contains letter x1 , or
substituting z = 1 if the records of w1 , w2 consist of letter x0 only, gives the
relation C = 0. Therefore, equality (3.16) becomes the required relation (3.15),
and the lemma follows.                                                         □
    Proof of Theorem 3.1. Theorem 3.1 follows from Lemma 3.6 and re-
lations (3.10).                                                   □
                   3.2. Shuffle algebra of generalised polylogarithms                    31

    Exercise 3.6. Show that
                                              Li1 (z)k   (− log(1 − z))k
                   Li{1}k (z) = Lixk1 (z) =            =
                                                 k!            k!
for k = 1, 2, . . . .
    Explicit computation of the monodromy group for the system of differential
equations (3.12) allows to Minh, Petitot and van der Hoeven to prove that the
homomorphism w 7→ Liw (z) of the shuffle algebra H over C is injective,
that is, all C-algebraic relations for generalised polylogarithms are originated
from shuffle relations (3.15) only; in particular, generalised polylogarithms are
linearly independent over C. A much simpler proof of the linear independence
of functions (3.9), as a consequence of elegant identities for the functions, is
due to Ulanskiı̆ [42].
    Exercise 3.7. Verify that the dilogarithm function Li2 satisfies the identity
                                                                       
                               x              y                    xy
    Li2 (x) + Li2 (y) = Li2         + Li2            − Li2
                              1−y           1−x              (1 − x)(1 − y)
                          − log(1 − x) log(1 − y).
    Exercise 3.8. (a) Demonstrate that for n = 1, 2, . . . ,
            X n                                    
         d
            x     (−1) Lin (x) + (1 − x) Li1 (x) − x = (−1)n Lin (x).
                      j
        dx    j=2

(b) For n = 1, 2, . . . , show that the function
                               Xn
                      fn (x) =     Lin (x) + (1 − x) Li1 (x) − nx
                                j=2

     satisfies
                        ∂n
                                  fn (x1 · · · xn ) = log(1 − x1 · · · xn ).
                    ∂x1 · · · ∂xn
(c) Given k ∈ Z≥0 and n ∈ Z>0 , prove that there is a linear form fn,k (x) in
    single polylogarithms (1 − x) Li1 (x), Li2 (x), . . . , Lim (x), . . . and powers of
    the logarithm logj x, where j = 1, 2, . . . , such that
              ∂n
                        fn,k (x1 · · · xn ) = (x1 · · · xn )k−1 log(1 − x1 · · · xn ).
          ∂x1 · · · ∂xn
    Hint. (b) Show that, more generally,
                   ∂n
                             fn (tx1 · · · xn ) = t log(1 − tx1 · · · xn )
               ∂x1 · · · ∂xn
by induction on n.                                                                       □
   Exercise 3.9 (‘Landen’ connection formula [35, 42]). Prove that
                                                                                   
                                                l
                                                   X                             −z
  Lis (z) = Lixs1 −1 x1 ···xsl −1 x1 (z) = (−1)              Liw1 x1 ···wl xl        .
               0            0
                                                  w1 ,...,wl                    1−z
                                               |wj |=sj −1 for j=1,...,l
                                  3.3. Duality of MZVs                                 32

      Note that z 7→ −z/(1 − z) is an involution.

                              3.3. Duality of MZVs
   By Lemma 3.5, the following integral representation is valid for the word
w = xε1 xε2 · · · xεk ∈ H1 :
                         Z z             Z z1                 Z zk−1
               Liw (z) =       ωε1 (z1 )      ωε2 (z2 ) · · ·        ωεk (zk )
                             0             0                   0
                                Z        Z
                       =            ···          ωε1 (z1 )ωε2 (z2 ) · · · ωεk (zk ) (3.17)
                        z>z1 >z2 >···>zk−1 >zk >0

if 0 < z < 1. When xε1 ̸= x1 , i.e., w ∈ H0 , the integral in (3.17) converges in the
region 0 < z ≤ 1, hence, in accordance with (3.10), we reduce representation
for the multiple zeta values
                                Z       Z
                      ζ(w) =        ···   ωε1 (z1 ) · · · ωεk (zk )            (3.18)
                                1>z1 >···>zk >0

in a form of Chen’s iterated integrals.
    There is a simple mnemonic way to write down the integral representa-
tion (3.18):
                                              Z 1
                      ζ(xε1 xε2 · · · xεk ) =     xε1 xε2 · · · xεk , (3.19)
                                                    0
where (with a definite ambiguity!) x0 and x1 denote the corresponding differ-
ential forms ω0 (z) and ω1 (z).
    Denote by τ the anti-automorphism of the algebra H = Q⟨x0 , x1 ⟩, inter-
changing x0 and x1 ; for example, τ (x20 x1 x0 x1 ) = x0 x1 x0 x21 . Clearly, τ is an
involution preserving weight. It can be easily seen that τ is also the automor-
phism of the subalgebra H0 .
    The following result is an immediate application of the integral represen-
tation (3.18).
      Theorem 3.7 (Duality theorem). For any word w ∈ H0 , the relation
                                      ζ(w) = ζ(τ w)
holds.
  Proof. To prove the theorem, it is sufficient to do the change of variable
z1′
  = 1 − zk , z2′ = 1 − zk−1 , . . . , zk′ = 1 − z1 , and apply relations ω0 (z) =
−ω1 (1 − z) followed from (3.13).                                               □
   As the simplest consequence of Theorem 3.7, notice (again) identity (1.13),
which follows for the word w = x20 x1 , as well as the general identity
                      ζ(n + 2) = ζ(2, {1}n )            n = 1, 2, . . . ,          (3.20)
for the words w = xn+1
                   0   x1 . Recall our convention (see (2.3)) about {s}n to
denote the n-repetition of multi-index s.
                                      3.3. Duality of MZVs                                   33

     Exercise 3.10. Show that
                    ζ({2, 1}n ) = ζ({3}n ),                     n = 1, 2, . . . .        (3.21)
For n = 1, this is again Euler’s (1.13).
  The integral representation (3.17) leads to a recipe for computing the
MZVs. For this write as in (3.18),
                             Z      Z
                 ζ(w) =         ···    ωε1 (z1 ) · · · ωεk (zk )
                               z0 >z1 >···>zk >zk+1

where for simplicity we set z0 = 1 and zk+1 = 0. Now we take an arbitrary
z in the interval 0 < z < 1 and split the integration domain into the disjoint
union of k + 1 subdomains like it was done in Section 2.3:
                      Xk        Z      Z
              ζ(w) =               ···         ωε1 (z1 ) · · · ωεk (zk )
                       j=0 z >···>z >z>z
                              0         j           j+1 >···>zk+1

                       k
                       X       Z            Z
                   =                  ···        ωε1 (z1 ) · · · ωεj (zj )
                       j=0 z >···>z >z
                              0         j
                                  Z          Z
                         ×             ···           ωεj+1 (zj+1 ) · · · ωεk (zk )
                             z>zj+1 >···>zk+1
                       k
                       X           Z            Z
                   =                    ···            ω1−εj (zj′ ) · · · ω1−ε1 (z1′ )
                       j=0
                             1−z>zj′ >···>z1′ >0
                                  Z          Z
                         ×             ···           ωεj+1 (zj+1 ) · · · ωεk (zk )
                             z>zj+1 >···>zk+1
                       k
                       X
                   =         Liτ (xε1 ···xεj ) (1 − z) Lixεj+1 ···xεk (z).
                       j=0

Finally, making the choice z = 1/2 leads to the following formula.
   Proposition 3.8. For the multiple zeta value ζ(w) with w = xε1 · · · xεk ∈
 0
H , we have
                             X         1 1
                     ζ(w) =      Liτ u     Liv    ,
                            w=uv
                                        2      2
where the sum runs over all possible ways of writing the word w as uv.
    The efficiency of this formula follows from the fact that the series repre-
sentation of any polylogarithm Liw (z) converges at the geometric rate z; the
convergence of the series at z = 1/2 is fast. At the same time, the computa-
tional scheme implied by Proposition 3.8 is much simpler than the one coming
from Proposition 2.8.
                                 3.4. Multiple harmonic sums                                   34

    Exercise 3.11. (a) Give the formula for ζ(s), where s > 1 is an integer,
in terms of polylogarithms evaluated at z = 1/2.
    (b) Implement it for computing the zeta values for a given accuracy.
    Hint. (a) Make use of Exercise 3.6.                                                        □
    The iterated integral representations of MZVs and generalised polyloga-
rithms motivate considering a slightly general than (2.1) version of MZVs,
namely, the alternating (or ‘alternative’) Euler sums
                                                          X         σ1n1 σ2n2 · · · σlnl
             ζ(s1 , . . . , sl ; σ1 , . . . , σl ) =                                      , (3.22)
                                                     n >n >···>n ≥1
                                                                    ns11 ns22 · · · nsl l
                                                  1    2       l

where σj ∈ {±1} are ‘signs’ and sj , as before, are positive integers. It is
customary to shortcut the notation by combining strings of exponents and signs
and replacing sj by sj in the multi-index string if and only if the corresponding
σj = −1. For example, ζ(1) = ζ(1; −1) = Li1 (−1) = − log 2 and ζ(2, 1) =
ζ(2, 1; −1, 1).
    Exercise 3.12. Show that
                                                       (− log 2)n
            (a) ζ(1, {1}n−1 ) = Li{1}n (−1) =                     ,      n = 1, 2, . . . ;
                                                           n!
                           ζ(3)
            (b) ζ(2, 1) =       .
                            8
    In Section 4.4 we will see that the standard algebraic setup for the alter-
nating Euler sums is an extension of the non-commutative algebra Q⟨x0 , x1 ⟩ to
Q⟨x0 , x1 , x1 ⟩, and generalization of the integral in (3.19) by allowing the three
differential forms
                                     dz                      dz
                      x0 7→ ω0 (z) =     , x1 7→ ω1 (z) =
                                      z                     1−z
                                                                              (3.23)
                                                    −dz
                             and x1 7→ ω 1 (z) =         .
                                                   1+z

                            3.4. Multiple harmonic sums
   Another way to cast multiple zeta values ζ(s) is through the limiting case,
as N → ∞, of the multiple harmonic sums (MHSs)
                                                         X                  1
    ζ<N (s) = H(s; N ) = H(s1 , . . . , sl ; N ) =                    s1 s2         sl ,
                                                   N >n >n >···>n ≥1
                                                                     n1 n 2  · · · nl
                                                               1   2       l
                                                                                (3.24)
where N = 1, 2, . . . ; we also set H( ; N ) = 1 for the empty index s. Given N ,
notice that these are finite sums, therefore well defined for any s1 , . . . , sl ∈ R.
This allows us, in our algebraic setting, to assign the MHS H(xs ; N ) = H(s; N )
to any word
                xs = xs01 −1 x1 xs02 −1 x1 · · · xs0l −1 x1 = ys1 ys2 · · · ysl ∈ H1 .
                                 3.4. Multiple harmonic sums                                      35

Then we extend the map H( · ; N ) : w 7→ H(w; N ) defined on words w ∈ H1
by linearity on the graded algebra H1 . Notice that

                                                 N −1
                                                 X    1
                     H(s1 , . . . , sl ; N ) =        s1 H(s2 , . . . , sl ; n1 );            (3.25)
                                                     n
                                                 n =1 1
                                                  1

this iteration shares some analogy with integrating the polylogarithms using
the differential equations in (3.12).
    Fix N ∈ Z>0 . An easy calculation shows that

   H(s1 ; N )H(s2 ; N ) = H(s1 , s2 ; N ) + H(s2 , s1 ; N ) + H(s1 + s2 ; N )                 (3.26)

but also motivates the fact that the product of any two MHSs (of weights k
and m) can be always represented as a Z-linear combination of MHSs (all of
weight k + m). More specifically, the following result takes place.

   Lemma 3.9. For any N ∈ Z>0 and words w1 , w2 ∈ H1 , we have

                         H(w1 ; N )H(w2 ; N ) = H(w1 ∗ w2 ; N ).

Here the stuffle product is defined by the rules (3.2), (3.4).

     Proof. Recall the connection between a multi-index s = (s1 , . . . , sl ) and
the word w ∈ H1 : it is assigned to w = ys1 · · · ysl . We prove the required
identity by induction on the sum of lengths of the multi-indices corresponding
to w1 and w2 . Write w1 = yj u and w2 = yk v for u = ys1 · · · ysl and v =
yr1 · · · yri . Then

       H(w1 ; N )H(w2 ; N )
                 X                        1                   X                      1
        =                                                                     r         r
                                 nj ns1 · · · nsl l N >m0 >m1 >···>mi ≥1 mk0 m11 · · · mi i
             N >n0 >n1 >···>nl ≥1 0 1

(we split the sum into three, according to whether n0 > m0 , n0 < m0 or
n0 = m 0 )

              X 1
         =             H(s1 , . . . , sl ; n0 )H(k, r1 , . . . , ri ; n0 )
                   nj
             n0 <N 0
                  X 1
               +            H(j, s1 , . . . , sl ; m0 )H(r1 , . . . , ri ; m0 )
                 m0 <N
                        mk0
                  X 1
               +        j+k
                             H(s1 , . . . , sl ; n0 )H(r1 , . . . , ri ; n0 )
                 n0 <N
                       n0
                                    3.4. Multiple harmonic sums                                   36

(we apply the inductive hypothesis to the internal products)
              N −1                       N −1
              X    1                     X     1
           =        j H(u ∗ yk v; n0 ) +         k
                                                   H(yj u ∗ v; m0 )
             n0 =1
                   n0                    m0 =1
                                               m 0
                     N −1
                     X       1
                +          j+k
                                 H(u ∗ v; n0 )
                    n0 =1 n0
           = H(yj (u ∗ yk v); N ) + H(yk (yj u ∗ v); N ) + H(yj+k (u ∗ v); N ),
where the property (3.25) was implemented at the final step. The result con-
verts into H(w1 ∗ w2 ; N ) according to the definition in (3.4).          □
    Lemma 3.9 means that the map
                                 w 7→ {H(w; N ) : N = 1, 2, . . . }
into the Q-linear space of (rational-valued) sequences is a homomorphism of
the stuffle algebra H1∗ .
    Exercise 3.13. Show that
                                      ∞
                       z             X
                           Lis (z) =      H(s; N )z N .
                     1−z             N =1
In other words, the left-hand side is the generating function of the sequence
{H(s; N ) : N = 1, 2, . . . }.
    We will have another opportunity to witness the multiple harmonic sum
(3.24) as a refinement of multiple zeta value ζ(s) in Section 5.2.
    Proof of Theorem 3.2. This follows immediately from considering the
limiting case of Lemma 3.9 as N → ∞.                                 □
    Several other proofs Theorem 3.2 are known. For example, one can in-
vent a functional model (viewing H(w; N ) as functions of N , not necessarily
integral!) satisfying the shuffle relations in a way similar to our treatment of
generalised polylogarithms in Section 3.2. Another proof exploits Hoffman’s
homomorphism ϕ : H1 → Q[[t1 , t2 , . . . ]], where Q[[t1 , t2 , . . . ]] is the Q-algebra
of formal power series in the countable set of (commuting) variables t1 , t2 , . . . .
Namely, the Q-linear map ϕ is defined by setting ϕ(1) = 1 and
                          X
  ϕ(ys1 ys2 · · · ysl ) =          tsn11 tsn22 · · · tsnll , s ∈ Zl , s1 ≥ 1, . . . , sl ≥ 1.
                            n1 >n2 >···>nl ≥1

The image of the homomorphism (actually, the monomorphism) ϕ is the alge-
bra QSym of quasi-symmetric functions. A formal power series (of bounded
degree) in t1 , t2 , . . . is called here a quasi-symmetric function if the coefficients
of tsn11 tsn22 · · · tsnll and tsn1′ tsn2′ · · · tsnl′ are the same whenever n1 > n2 > · · · > nl and
                                   1     2           l
n′1 > n′2 > · · · > n′l . By the above means, the homomorphism in Theorem 3.2
is defined as restriction of the homomorphism ϕ on H0 by setting tn = 1/n for
n = 1, 2, . . . .
                           3.5. Quasi-shuffle products and derivations                            37

    Exercise 3.14 (Cartier). (a) For an admissible multi-index s, prove the
integral representation
                     l−1
                           t1 t2 · · · ts1 +···+sj             dt1 dt2 · · · dt|s|
            Z     Z Y
    ζ(s) = · · ·                                         ·                                   , (3.27)
                     j=1
                         1 −  t1 t2  · · · ts 1 +···+s j
                                                           1 − t1 t2 · · · ts 1 +s2 +···+s l
                [0,1]|s|

where l = ℓ(s).
   (b) Using part (a) show that
        ζ(s1 )ζ(s2 ) = ζ(s1 + s2 ) + ζ(s1 , s2 ) + ζ(s2 , s1 ) for s1 ≥ 2, s2 ≥ 2,
which corresponds to the stuffle product of words ys1 and ys2 (see (3.26)).
    Hint. (a) Integrate termwise the series
                                   ∞                          ∞
                              1    X                     t    X
                                 =    tn       and          =    tn .
                            1 − t n=0                  1 − t n=1
    (b) Substitute u = t1 · · · ts1 , v = ts1 +1 · · · ts1 +s2 into the (elementary!) iden-
tity
                1             1          u               v
                         =       +               +
          (1 − u)(1 − v)   1 − uv (1 − u)(1 − uv) (1 − v)(1 − uv)
and integrate over the hypercube [0, 1]s1 +s2 using (3.27).                                       □
   The approach in Exercise 3.14 (b) can be extended to demonstrate Theo-
rem 3.2 in its generality.

                  3.5. Quasi-shuffle products and derivations
    The following construction, due to Hoffman, allows one to consider each of
the algebras H and H1∗ as a particular case of some general algebraic structure.
    Consider the non-commutative, graded by degree, polynomial algebra A =
K⟨A⟩ over the field K ⊂ C; here A denotes a locally finite set of generators
(that is, the set of generators of fixed positive degree is finite). As usual,
elements of the set A are said to be letters and monomials in these letters are
words. To any word w, assign its length (the number of letters in the record)
ℓ(w) and its weight (the sum of degrees of the letters) |w|. The unique word
of length 0 and weight 0 is the empty word, which is denoted by 1; this word
is the unit of the algebra A. The neutral (zero) element of the algebra A is
denoted by 0.
    Now, define the product ◦, additively distributing it over the whole alge-
bra A, by the following rules:
                                      1◦w =w◦1=w                                             (3.28)
for any word w, and
                aj u ◦ ak v = aj (u ◦ ak v) + ak (aj u ◦ v) + [aj , ak ](u ◦ v)              (3.29)
                      3.5. Quasi-shuffle products and derivations                        38

for any words u, v and letters aj , ak ∈ A, where the functional

                                     [ · , · ] : Ā × Ā → Ā                        (3.30)

(Ā = A ∪ {0}) satisfies the properties
   (S0) [a, 0] = 0 for any a ∈ Ā;
   (S1) [[aj , ak ], al ] = [aj , [ak , al ]] for any aj , ak , al ∈ Ā;
   (S2) either [aj , ak ] = 0 or |[ak , aj ]| = |aj | + |ak | for any aj , ak ∈ A.
Then A◦ = (A, ◦) becomes an associative graded K-algebra and, if the addi-
tional property
   (S3) [aj , ak ] = [ak , aj ] for any aj , ak ∈ Ā
holds, then it is the commutative K-algebra (the result of Hoffman).
    If [aj , ak ] = 0 for all letters aj , ak ∈ A, then (A, ◦) is the standard shuffle
algebra; in particular case A = {x0 , x1 }, we obtain the shuffle algebra A◦ = H
of the multiple zeta values (or of the polylogarithms). The stuffle algebra H1∗
corresponds to the choice of the generators A = {yj }∞      j=1 and the functional

                 [yj , yk ] = yj+k        for integers j ≥ 1 and k ≥ 1.

   Exercise 3.15. On the algebra A with the given functional (3.30), define
the dual product ◦¯ by the rules

                                      1¯◦w = w¯◦1 = w,
                 uaj ◦¯vak = (u¯◦vak )aj + (uaj ◦¯v)ak + (u¯◦v)[aj , ak ]

in place of (3.28) and (3.29), respectively. Then A¯◦ = (A, ◦¯) is a graded
K-algebra as well (commutative, if property (S3) holds).
   Show that the algebras A◦ and A¯◦ coincide.

   Hint. Use induction on ℓ(w1 ) + ℓ(w2 ) to demonstrate that

                                      w1 ◦ w2 = w1 ◦¯w2

for all words w1 , w2 ∈ K⟨A⟩. Note that property (S3) is not required in this
derivation!                                                                □

   Lemma 3.10. For any letter a ∈ A and any words u, v ∈ A, the following
identity holds:
                          a ◦ uv − (a ◦ u)v = u(a ◦ v − av).                         (3.31)

    Proof. We will prove the statement by induction on the number of letters
in the word u. If the word u is empty, then identity (3.31) is evident. Other-
wise, write the word u as u = a1 u1 , where a1 ∈ A and the word u1 consists of
less number of letters, hence the identity

                        a ◦ u1 v − (a ◦ u1 )v = u1 (a ◦ v − av)
                    3.5. Quasi-shuffle products and derivations                    39

holds. Then
        a ◦ uv − (a ◦ u)v = a ◦ a1 u1 v − (a ◦ a1 u1 )v
                           = aa1 u1 v + a1 (a ◦ u1 v) + [a, a1 ]u1 v
                                − (aa1 u1 + a1 (a ◦ u1 ) + [a, a1 ]u1 )v
                           = a1 (a ◦ u1 v − (a ◦ u1 )v) = a1 u1 (a ◦ v − av)
                           = u(a ◦ v − av),
which is the desired result.                                                       □
    By a derivation of the (graded non-commutative polynomial) algebra A =
K⟨A⟩ we mean a linear map δ : A → A (of the graded K-vector spaces) that
satisfies the Leibniz rule
                    δ(uv) = δ(u)v + uδ(v) for all u, v ∈ A.                    (3.32)
     Exercise 3.16. Verify that the commutator of two derivations [δ1 , δ2 ] =
δ1 δ2 − δ2 δ1 is a derivation.
    Therefore, the set of all derivations of the algebra A forms the Lie algebra
Der(A) (naturally graded by degree).
    It can be easily seen that, for defining a derivation δ ∈ Der(A), it is suffi-
cient to give its image on the generators A and distribute then over the whole
algebra by linearity and in accordance with rule (3.32).
    The next assertion gives examples of derivations of A, when the algebra
possesses an additive multiplication ◦ with the properties (3.28) and (3.29).
   Theorem 3.11. For any letter a ∈ A, the map
                               δa : w 7→ aw − a ◦ w                            (3.33)
is a derivation.
    Proof. Linearity of the map δa is clear. By Lemma 3.10, for any words
u, v ∈ A we have
            δa (uv) = auv − a ◦ uv = auv − (a ◦ u)v − u(a ◦ v − av)
                   = (δa u)v + u(δa v),
thus (3.33) is actually a derivation.                                              □
   Theorem 3.11 implies that the maps δ : H → H and δ∗ : H1 → H1 , defined
by the formulae
   δ : w 7→ x1 w − x1    w, δ : w 7→ y w − y ∗ w = x w − x ∗ w,
                                 ∗           1       1         1       1       (3.34)
are derivations; thanks to rule (3.5), the map δ∗ is a derivation on the whole
algebra H. We mention the action of derivations (3.34), obtained in accordance
with (3.2)–(3.5), on the generators of the algebra:
      δ x0 = −x0 x1 , δ x1 = −x21 ,     δ∗ x0 = 0, δ∗ x1 = −x21 − x0 x1 .    (3.35)
                                                                           0
   For any derivation δ of the algebra H (or of the subalgebra H ), define the
dual derivation δ = τ δτ , where τ is the anti-automorphism of the algebra H
                           3.5. Quasi-shuffle products and derivations                                          40

(and H0 ) in Section 3.2. A derivation δ is said to be symmetric if δ = δ, and
anti-symmetric if δ = −δ. Since τ x0 = x1 , an (anti-)symmetric derivation δ is
uniquely determined by its value on one of the generators x0 or x1 , while an
arbitrary derivation requires its values on both generators.
    Define now the derivation D of the algebra H by setting Dx0 = 0, Dx1 =
x0 x1 (that is, Dys = ys+1 for the generators ys of the algebra H1 ) and write
the statement of Theorem 2.1 (Hoffman’s relations) in the following form.
   Theorem 3.12 (Derivation theorem). For any word w ∈ H0 , the identity
                                                ζ(Dw) = ζ(Dw)                                               (3.36)
holds.
   Proof. Expressing a word w ∈ H0 as w = ys1 ys2 · · · ysl (with s1 > 1), note
that the left-hand side of equality (2.4) corresponds to the element
    Dw = D(ys1 ys2 · · · ysl )
             = ys1 +1 ys2 · · · ysl + ys1 ys2 +1 ys3 · · · ysl + · · · + ys1 · · · ysl−1 ysl +1             (3.37)
of the algebra H0 . On the other hand,
                                 s     −1
 Dw = τ D x0 xs1l −1 x0 x1l−1               · · · x0 xs12 −1 x0 xs11 −1
                                                                          

                  k −2
               l sX
                                                 s    −1                          s     −1
               X
         =τ               x0 xs1l −1 · · · x0 x1k+1 x0 xj1 x0 xs1k −j−1 x0 x1k−1             · · · x0 xs11 −1
               k=1 j=0
               sk ≥2
                k −2
             l sX
                                            s    −1                           s   −1
             X
         =              xs01 −1 x1 · · · x0k−1 x1 xs0k −j−1 x1 xj0 x1 x0k+1 x1 · · · xs0l −1 x1 (3.38)
             k=1 j=0
             sk ≥2

that corresponds to the right-hand side in (2.4). Applying now the map ζ to
both sides of obtained equalities (3.37) and (3.38), by Theorem 2.1 we deduce
the required identity (3.36).                                              □
   Note that the condition w ∈ H0 in Theorem 3.12 cannot be weakened;
equality (3.36) is false for the word w = x1 :
                                ζ(Dx1 ) = ζ(x0 x1 ) ̸= 0 = ζ(Dx1 ).
   Proof of Theorem 3.3. Comparing action (3.35) of derivations (3.34)
with those of D, D on the generators of the algebra H,
                  Dx0 = 0,           Dx1 = x0 x1 ,            Dx0 = x0 x1 ,           Dx1 = 0,
we see that δ∗ − δ = D − D. Therefore application of Theorem 3.12 to the
word w ∈ H0 leads to the required equality:
     
ζ(x1 w − x1 ∗ w) = ζ (δ∗ − δ )w = ζ (D − D)w = ζ(Dw) − ζ(Dw) = 0.
                                                

This completes the proof.                                                                                       □
                         3.5. Quasi-shuffle products and derivations                               41

   Another proof of Theorem 3.3, based on the shuffle and stuffle relations for
the so-called coloured polylogarithms
                                                               X         z1n1 z2n2 · · · zlnl
     Lis (z) = Lis1 ,s2 ,...,sl (z1 , z2 , . . . , zl ) =                  s1 s2           sl , (3.39)
                                                          n >n >···>n ≥1
                                                                         n 1  n 2  · · · n l
                                                      1   2      l

was given by Waldschmidt. (As it is easily seen, specialising z2 = · · · =
zl = 1 functions (3.39) become generalised polylogarithms (3.9).) We do not
discuss properties of the functional model (3.39) here, except for the cases
when z1 , . . . , zl ∈ {±1} (see Sections 3.3 and 4.4).
    Exercise 3.17. (a) Show that
                                                  
                              x(1 − y)            x
         Li1,1 (x, y) = Li2 −            − Li2 −       − Li2 (xy).
                               1−x               1−x
    (b) Use part (a) to compute the integral
                               log 1+x   log 1−x
                          Z 1                   
                                    2         2    dx
                                       −
                            0   1−x       1+x      x
in terms of the values of logarithm and dilogarithm.
    Hints. (a) Use appropriate differentiation.
    (b) Expand the integrand into a power series.                                                  □
                                    CHAPTER 4

      Generating functions and periodic multi-indices

    Another application of differential equations for generalised polylogarithms,
deduced in Lemma 3.5, is the generating-function method.
    Let us first remark that, for an admissible multi-index s = (s1 , . . . , sl ), the
corresponding set of periodic polylogarithms
          Li{s}n (z),   where {s}n = ( s, s, . . . , s ) for n = 0, 1, 2, . . . ,
                                       | {z }
                                                n times

possesses the generating function
                                          ∞
                                          X
                            Ls (z, t) =         Li{s}n (z)tn|s| ,
                                          n=0

which satisfies an ordinary differential equation with respect to the variable z.
For instance, if ℓ(s) = 1 that is s = (s), the corresponding differential equation,
by Lemma 3.5, has the form
                                      s−1      
                              d        d          s
                      (1 − z)        z         − t Ls (z, t) = 0,
                              dz       dz
and its solution may be written explicitly by means of generalised hypergeo-
metric series.

                        4.1. Hypergeometric function
    In order to show any reasonable result for MZVs using generating functions,
we have to familiarise ourselves with the Euler–Gauss hypergeometric function
(or hypergeometric series)
                                         
                                  a, b
          F (a, b; c; z) = 2 F1         z
                                   c
                            ∞
                           X    (a)n (b)n n
                         =                z
                           n=0
                                 n!(c)n
                              a·b      a(a + 1) · b(b + 1) 2
                        =1+       z+                        z
                              1·c         1 · 2 · c(c + 1)
                              a(a + 1)(a + 2) · b(b + 1)(b + 2) 3
                            +                                  z + ··· ,
                                  1 · 2 · 3 · c(c + 1)(c + 2)
                                            42
                            4.1. Hypergeometric function                            43

where                             (
                     Γ(a + n)      1                          if n = 0,
              (a)n =          =
                       Γ(a)        a(a + 1) · · · (a + n − 1) if n ≥ 1,
denotes the Pochhammer symbol (1.16).
   The convergence of the series can be determined by the ratio test. If we
denote
                                      (a)n (b)n
                                 an =
                                       n!(c)n
the nth coefficient of the hypergeometric series F (a, b; c; z), then
                    an+1   (a + n)(b + n)
                         =                → 1 as n → ∞,
                     an    (1 + n)(c + n)
hence the series converges in the unit disc, |z| < 1. In several cases, depending
on the parameters a, b, c, the series may converge on the boundary of the disc,
for example, at z = 1. We will examine the latter situation.
    Because of the relation
        (1 + n)(c + n) · an+1 = (a + n)(b + n) · an      for n = 0, 1, 2, . . . ,
we have
                                               X∞
     d      d                           d       d          (a)n (b)n n
z z    +a z    + b F (a, b; c; z) = z z    +a z    +b               z
    dz      dz                          dz      dz     n=0
                                                            n!(c)n
        ∞                                      ∞
        X (a)n (a + n) · (b)n (b + n)          X (a)n+1 (b)n+1
   =z                                   zn =                     z n+1
        n=0
                      n!(c)n                   n=0
                                                     n!(c)n
       ∞                       ∞
       X   (a)n (b)n           X (a)n (b)n · n(c + n)
   =                    zn =                            zn
    n=1
        (n − 1)!(c) n−1      n=0
                                         n!(c)n
                        X ∞
        d       d                (a)n (b)n n
   = z       z     +c−1                    z
       dz      dz            n=0
                                  n!(c)n
                        
        d       d
   = z       z     + c − 1 F (a, b; c; z).
       dz      dz
    Lemma 4.1. The hypergeometric function F (a, b; c; z) satisfies the differ-
ential equation
                                                  
                d       d             d      d
           z z     +a z    +b − z          z     + c − 1 y = 0;
                dz      dz           dz      dz
in equivalent form,
                        d2 y                      dy
                 z(1 − z)  2
                             + (c − (a + b + 1)z) − aby = 0.
                        dz                        dz
   Lemma 4.2 (Pochhammer’s integral). If Re c > Re b > 0 and |z| < 1, then
                                    Z 1
                           Γ(c)
      F (a, b; c; z) =                  xb−1 (1 − x)c−b−1 (1 − zx)−a dx.
                       Γ(b)Γ(c − b) 0
                            4.1. Hypergeometric function                    44

    Note that for a = 0 the integral on the right-hand side reduces to Euler’s
integral of the first kind B(b, c − b).
   Proof. The conditions Re b > 0 and Re(c − b) > 0 ensure convergence of
the integral
                             Z 1
             I(a, b; c; z) =     xb−1 (1 − x)c−b−1 (1 − zx)−a dx.
                                  0
Furthermore, for |z| < 1,
                                              ∞
                                              X (a)n
                            (1 − zx)−a =                  z n xn .
                                              n=0
                                                     n!
Therefore,
                                   ∞
                                Z 1X
                                     (a)n z n b+n−1
              I(a, b; c; z) =                x      (1 − x)c−b−1 dx
                               0 n=0    n!
                               ∞
                              X (a)n z n Z 1
                            =                xb+n−1 (1 − x)c−b−1 dx
                              n=0
                                   n!      0
                                ∞
                                X (a)n z n Γ(b + n)Γ(c − b)
                            =
                                n=0
                                      n!            Γ(c + n)
                                Γ(b)Γ(c − b)
                            =                F (a, b; c; z),
                                    Γ(c)
and the result follows.                                                     □
   As a corollary of this result and Abel’s theorem on power series, we deduce
   Lemma 4.3 (Gauss’ summation formula). If Re c > Re(a + b), then
                                             Γ(c)Γ(c − a − b)
                          F (a, b; c; 1) =                    .
                                             Γ(c − a)Γ(c − b)
    Proof. The result follows, whenever Re c > Re b > 0 and Re(c−a−b) > 0,
by taking the limit z → 1 in Lemma 4.2 and using the beta integral evaluation
of the resulted definite integral:
                                            Z 1
                                   Γ(c)
              F (a, b; c; 1) =                  xb−1 (1 − x)c−b−a−1 dx
                               Γ(b)Γ(c − b) 0
                                   Γ(c)       Γ(b)Γ(c − a − b)
                             =              ·                  .
                               Γ(b)Γ(c − b)       Γ(c − a)
To get rid of restriction Re c > Re b > 0, note that the formula is valid for
Re(c − a − b) > 0 and use the theory of analytic continuation.              □
   Remark. When a is a negative integer −m, the theorem becomes
            m  
           X   m (b)n                             (c − b)m
                        (−1)n = F (−m, b; c; 1) =          ,
           n=0
               n   (c)n                             (c)m
                            4.2. Broadhurst’s MZV evaluation                               45

the result known as the Chu–Vandermonde summation. With the help of the
latter formula one can show the following binomial evaluation:
                         m                    
                        X    p       q        p+q
                                          =          .
                        n=0
                            n m−n              m

    Exercise 4.1. (a) Show that
                                               Γ(1 + b − a)Γ(1 + 21 b)
                  F (a, b; 1 + b − a; −1) =                            .
                                               Γ(1 + b)Γ(1 + 12 b − a)
    (b) Give a gamma-function evaluation of the hypergeometric series
                                         1
                            F a, 1 − a; c; .
                                          2

                      4.2. Broadhurst’s MZV evaluation
    It is now a good time to go back to the MZV story.
   Lemma 4.4. The following equality holds:
 L3,1 (z, t) = F 12 (1 + i)t, − 12 (1 + i)t; 1; z · F 21 (1 − i)t, − 21 (1 − i)t; 1; z , (4.1)
                                                                                     

                                                                             √
where F (a, b; c; z) denotes the hypergeometric function and i = −1.
    Proof. Routine verification (with a help of Lemma 3.5 for the left-hand
side) shows that both sides of the required equality are annihilated by action
of the differential operator
                                       2      2
                                     d        d
                             (1 − z)        z       − t4 ;
                                     dz       dz
in addition, the first terms in z-expansions of both sides in (4.1) coincide:
                        t4 2 t4 3 t8 + 44t4 4
                        1+z + z +           z + ··· .
                        8     18       1536
Thus the statement of the lemma follows.                                                   □
    Exercise 4.2. Fill in the missing details.
    The following result was conjectured by Zagier in his pioneering talk at the
European Congress of Mathematics in 1994. The proof was given some years
later in joint work of Borwein, Bradley, Broadhurst and Lisoněk.
    Theorem 4.5. For any integer n ≥ 1, the identity
                                                   2π 4n
                                 ζ({3, 1}n ) =                                          (4.2)
                                                 (4n + 2)!
holds.
                              4.2. Broadhurst’s MZV evaluation                         46

    Proof. By Lemma 4.3 (Gauss’ summation formula),
                                                 1           sin πa
                      F (a, −a; 1; 1) =                    =        ,               (4.3)
                                          Γ(1 − a)Γ(1 + a)     πa
substituting z = 1 into equality (4.1) yields
  ∞
  X
                n   4n                   sin 21 (1 + i)πt sin 21 (1 − i)πt
        ζ({3, 1} )t      = L3,1 (1, t) = 1               · 1
  n=0                                      2
                                             (1 + i)πt      2
                                                              (1 − i)πt
                             1
                         = 2 2 · e(1+i)πt/2 − e−(1+i)πt/2 e(1−i)πt/2 − e−(1−i)πt/2
                                                                                  
                           2π t
                             1
                         = 2 2 · eπt + e−πt − eiπt − e−iπt
                                                                 
                           2π t
                                    ∞
                             1 X                                     (πt)m
                         = 22          (1 + (−1)m − im − (−i)m )
                           2π t m=0                                    m!
                             ∞
                             X 2π 4n t4n
                         =                   .
                             n=0
                                 (4n + 2)!
Comparison of the coefficients in the same powers of t gives the desired identity.
                                                                                □
    Identity (4.2) is not the unique example of application of generating func-
tions. We present more identities of Borwein, Bradley and Broadhurst, similar
to (4.2), for which the above method is also effective:
                            2n+1                             2n+1
            n     2(2π)2n 1                   n      4(2π)4n 1
      ζ({2} ) =                      , ζ({4} ) =                      ,
                 (2n + 1)! 2                        (4n + 2)! 2
                                         6(2π)6n
                            ζ({6}n ) =            ,
                                       (6n + 3)!
                                          4n+2             4n+2       (4.4)
                      8(2π)8n
                               
               n                       1                  1
         ζ({8} ) =               1+ √            + 1− √             ,
                     (8n + 4)!          2                  2
                                         √ 10n+5           √ 10n+5 
                 10(2π)10n
                                 
            n                       1+ 5                1− 5
     ζ({10} ) =                1+                   +                   ,
                 (10n + 5)!            2                   2
where n = 1, 2, . . . . Identities
           ζ(m + 2, {1}n ) = ζ(n + 2, {1}m ),       where m, n = 0, 1, 2, . . . ,
may be derived by the generating-function method (as well as by straightfor-
ward application of Theorem 3.7). The fact that both sides of this equality are
expressed as polynomials in single zeta values ζ(s) with rational coefficients is
the subject of Exercise 4.6.
    Exercise 4.3. Prove (some) identities in (4.4).
   A different proof of the first identity in (4.4) is discussed in Exercise 4.6
below.
                           4.2. Broadhurst’s MZV evaluation                                47

   Exercise 4.4. Show that
                                                  1
                              ζ({3, 1}n ) =            ζ({2}2n ).
                                                2n + 1
   The family of identities
      ζ({2}n+3 ) + 2ζ({2}n , 3, 3) = ζ(2, 1, {2}n , 3),             n = 1, 2, . . . ,   (4.5)
conjectured by Hoffman, stayed a conjecture for almost 20 years. It was finally
proved by M. Hirose and N. Sato in [15].
   An example of other-type generating functions relates to generalization of
Apéry’s identity
                                     ∞
                                  5 X (−1)k−1
                           ζ(3) =               ;
                                  2 k=1 k 3 2k
                                             k
namely, the following expansions are valid:
     ∞                        ∞
     X
                     2n
                              X             1
           ζ(2n + 3)t     =
     n=0                      k=1
                                    k 3 (1 − t2 /k 2 )
                             ∞                               k−1
                                (−1)k−1 1                           t2
                                                             Y       
                            X                       2
                          =                   +                   1− 2 ,
                                   3 2k           −  2 /k 2
                                        
                            k=1
                                 k    k
                                            2   1   t         l=1
                                                                     l
     ∞                        ∞                                                         (4.6)
     X
                     4n
                              X       1
           ζ(4n + 3)t     =
     n=0                    k=1
                                k (1 − t4 /k 4 )
                                 3

                               ∞                       k−1
                            5 X (−1)k−1        1       Y 1 + 4t4 /l4
                          =                                           .
                            2 k=1 k 3 2k   1 − t4 /k 4 l=1 1 − t4 /l4
                                         
                                       k

Their proofs as well as proofs of several other identities is based on transforma-
tion and summation formulae of generalised hypergeometric functions, similar
to application of formula (4.3) in deducing Theorem 4.5.
    Identities (4.6) can be used in fast computation of the Riemann zeta func-
tion at odd integers. To see that note that they both come as special cases
(s = 0 and t = 0) of the bivariate generating function identity
           ∞ X ∞                                      ∞
         X          n+m                      2n 4m
                                                      X           k
                            ζ(2n + 4m + 3)s t =
          n=0 m=0
                       n                               k=1
                                                            k − s k 2 − t4
                                                             4    2

                  ∞                           k−1
               1 X (−1)k−1      5k 2 − s2     Y (m2 − s2 )2 + 4t4
             =                                                    ,
               2 k=1 k 2k   k 4 − s2 k 2 − t4 m=1 m4 − s2 m2 − t4
                          
                        k

which was conjectured by Cohen and proved independently by Bradley and
Rivoal. Recently, applying the so-called Markov–WZ algorithm, the Hessami
Pilehroods gave a different identity
     ∞                         ∞
                            1 X (−1)n−1 r(n) n−1      2   2 2     4
                                            Q
               k                              m=1 ((m − s ) + 4t )
    X
          4 − s2 k 2 − t4
                          =           2n
                                             2n                      , (4.7)
        k                   2
                                            Q        4 − s2 m2 − t4 )
    k=1                       n=1
                                    n  n      m=n  (m
           4.3. Multiple zeta values of fixed weight, length and height              48

where
             r(n) = 205n6 − 160n5 + (32 − 62s2 )n4 + 40s2 n3
                       + (s4 − 8s2 − 25t4 )n2 + 10t4 n + t4 (s2 − 2).
Formula (4.7) generates (Apéry-like) series for all ζ(2n + 4m + 3), n, m ≥ 0,
convergent at the geometric rate with ratio 2−10 . For example, if s = t = 0
one gets the Amdeberhan–Zeilberger series for ζ(3),
                               ∞
                         1 X (−1)n−1 (205n2 − 160n + 32)
                  ζ(3) =                    5           .
                         2 n=1         n5 2n         n

   Exercise 4.5. Using (4.7), find fast converging series for ζ(5) and ζ(7).

     4.3. Multiple zeta values of fixed weight, length and height
   In this section we discuss a different application of generating functions
and the theory of hypergeometric series.
   We will need the formula
                                            ∞
                                               ζ(k)xk
                                          X          
                    Γ(1 − x) = exp γx +                 .               (4.8)
                                           k=2
                                                  k
This follows from Proposition 1.1.
    Define the height m = m(s) of a multi-index s = (s1 , . . . , sl ) to be the
number of components satisfying sj > 1; for an admissible s we have s1 > 1,
so that m(s) ≥ 1. Denote the set of admissible multi-indices of fixed weight
w = |s|, length l = ℓ(s) and height m = m(s) by I(w, l, m), and set
                               ∞
                               X                                X
               Φ(x, y, z) =             xw−l−m y l−m z 2m−2                ζ(s)
                              w,l,m=0                         s∈I(w,l,m)

to be a (formal) power series with real coefficients.
   Theorem 4.6. The generating function Φ(x, y, z) is given by
                                       X∞                   
                         1                   ζ(k)
         Φ(x, y, z) =            1 − exp          Sk (x, y, z) ,                  (4.9)
                      xy − z 2           k=2
                                              k

where the homogeneous polynomials Sk (x, y, z) of degree k are defined through
the formula
                                                              p
                                                    x +  y ±      (x + y)2 − 4z 2
  Sk (x, y, z) = xk + y k − αk − β k with {α, β} =                                ,
                                                                   2
                                                                             (4.10)
or alternatively by the identity
                    ∞
                                                 xy − z 2
                                                             
                   X   Sk (x, y, z)
                                    = log 1 −                   .            (4.11)
                   k=2
                            k                 (1 − x)(1 −  y)
            4.3. Multiple zeta values of fixed weight, length and height                       49
                                              P
In particular, all of the coefficients   s∈I(w,l,m) ζ(s) of Φ(x, y, z) can be ex-
pressed as polynomials in single zeta values ζ(2), ζ(3), . . . with rational coeffi-
cients.

   Proof. If one defines, more generally,
                                ∞
                                X                                 X
             Φ(x, y, z; t) =             xw−l−m y l−m z 2m−2                Lis (t),
                               w,l,m=0                         s∈I(w,l,m)
                                ∞
                                X                              X
             Φ(x,
             e y, z; t) =                xw−l−m y l−m z 2m                Lis (t),
                               w,l,m=0                         ˜
                                                             s∈I(w,l,m)

       ˜ l, m) is the set of all multi-indices s including those with s1 = 1.
where I(w,
Using the differential equations of the generalised polylogarithms, Lemma 3.5,
we find out that
        dΦ  x   1 e                               d e               y e
           = Φ + (Φ − 1 − z 2 Φ),                    (Φ − z 2 Φ) =     Φ.               (4.12)
        dt  t   yt                                dt               1−t

One can eliminate Φ   e from this system and write a homogeneous linear 2nd
order differential equation for Y = 1 − (xy − z 2 )Φ:

                 d2 Y                            xy − z 2
                                       
                           1−x       y    dY
                       +         −           +            Y = 0.      (4.13)
                  dt2        t     1 − t dt      t(1 − t)

This equation is recognised as a hypergeometric differential equation (see
Lemma 4.1) whose unqiue holomorphic solution at t = 0 starting Y (t) =
1 + O(t) is given by the hypergeometric function F (α − x, β − x; 1 − x; t),
where α + β = x + y and αβ = z 2 . Specialising to t = 1 and using Gauss’
summation formula (Lemma 4.3) arrive at

                                                                          Γ(1 − x)Γ(1 − y)
  1 − (xy − z 2 )Φ(x, y, z; 1) = F (α − x, β − x; 1 − x; 1) =                              .
                                                                          Γ(1 − α)Γ(1 − β)

The rest follows from the power series expansion (4.8).                                        □

   Particular specialisations of Theorem 4.6 lead one to numerous beautiful
identities of MZVs, in particular, to a simple proof of the sum formula.

    Proof of Theorem 2.5. Letting z 2 → xy in (4.9) we obtain the gener-
ating function
                                   ∞
                        √          X                          X
                Φ(x, y, xy) =             xw−l−1 y l−1                     ζ(s)
                                    w,l                  s∈I(w,l,m)m any
                    4.4. An identity for alternating Euler sums                    50

of multiple zeta values of weight w and length l on the left-hand side. At the
same time, the right-hand side simplifies to
                ∞                    ∞            k  k
               X          1         X    1 X x 1 y 2
                                  =
               n=1
                   (n − x)(n − y) n=1 n2 k ,k ≥0 n         n
                                             1 2
                                      X
                                  =        ζ(k1 + k2 + 2)xk1 y k2 ,
                                         k1 ,k2 ≥0
                                                  √
so that the coefficient of xw−l−1 y l−1 in Φ(x, y, xy) is equal to ζ(w) as required.
                                                                                  □
   Exercise 4.6 ([32]). (a) Using Theorem 4.6 prove that
                                     π 2n
                     ζ({2}n ) =                  for n = 0, 1, . . . .
                                  (2n + 1)!
(b) Show that, for each m, n = 0, 1, 2, . . . , the multiple zeta values ζ(m + 2,
    {1}n ) = ζ(n + 2, {1}m ) are polynomials in single zeta values with rational
    coefficients.
   Hint. Use specialisation x = y = 0 in (a) and z = 0 in (b).                     □

               4.4. An identity for alternating Euler sums
   In this part we discuss a family of relations for the alternating Euler
sums (3.22) formally introduced in Section 3.3.
   Theorem 4.7 (Zhao). The following equalities are true:
                                 1
                 ζ({2, 1}n ) =      ζ({3}n ),        where n = 1, 2, . . . .   (4.14)
                                 8n
    The family of identities (4.14) was conjectured by Borwein, Bradley and
Broadhurst in [5] (see (3.22) for the definition of alternating Euler sums); it
generalises Exercises 3.10 and 3.12 (b) and looks similar to that in Theorem 4.5.
It was proven more than a decade later by Zhao [49] using the (finite) double
shuffle relations and distribution relation for the alternating Euler sums, so
that it was quite from the proof given in Section 4.2. A proof by generating
functions is still wanted. Here we adopt Zhao’s only-known proof of (4.14).
    We have essentially settled standard setup for the (alternating) Euler sums
at the end of Section 3.3. The non-commutative algebra H = Q⟨x0 , x1 ⟩ is
extended to the algebra H b = Q⟨x0 , x1 , x1 ⟩, and its subalgebra
                      b 0 = Q1 ⊕ x0 Hx
                      H             b 1 ⊕ x0 Hx
                                             b 1 ⊕ x1 Hx
                                                      b 1

of admissible words is generated by words not beginning with x1 and not
ending with x0 . Furthermore, H    b 0 is generated by the words ys = xs−1 x1 and
                                                                          0
       s−1
y s = x0 x1 , where s = 1, 2, . . . , with the only restriction that the words over
this newer alphabet cannot begin with y1 .
                        4.4. An identity for alternating Euler sums                                    51

    By assigning the three differential forms
                                   dz                    dz
                   x0 7→ ω0 (z) =     , x1 7→ ω1 (z) =       ,
                                    z                   1−z
                                                −dz
                           and x1 7→ ω 1 (z) =
                                               1+z
(cf. (3.23)) to the three letters, for a word w ∈ H b 0 we define the evaluation
zeta map by                               Z                 1
                                            ζ(w) =              w                                  (4.15)
                                                        0
(with the convention used in (3.19)). Then, of course, ζ(s) = ζ(ys1 · · · ysl ) if the
multi-index s = (s1 , . . . , sl ) does not involve bars (so that the corresponding
word does not contain letter x1 ). For example,
                                    ({3}n ) 7→ y3n = (x20 x1 )n .
If however the multi-index s involves bars, then the rule of assigning the word
is as follows. Going for s1 to sl , as soon as we see the first signed entry si we
change every yk after ysi (inclusive) to y k until the next signed entry sj occur.
We then leave all the yk after ysj (again inclusive) until we see the next signed
entry when we start toggling again, and so on. In other words, we can think
of the bars as of switches between y and y.
    Exercise 4.7. Write the word which corresponds to the multi-index
                                          (1, 2, 1, 2, 3, 4, 5).
   Exercise 4.8. Prove the following correspondence:
                                                (
       n          2     2 ⌊n/2⌋      2 2{n/2}    (x0 x21 x0 x21 )k (x0 x21 ) if n = 2k + 1,
({2, 1} ) 7→ (x0 x1 x0 x1 )     (x0 x1 )      =
                                                 (x0 x21 x0 x21 )k           if n = 2k,
                                                      = (y 2 y 1 y2 y1 )⌊n/2⌋ (y 2 y 1 )2{n/2} .
   The shuffle and stuffle products in (3.2)–(3.4) are extended to the alge-
    b 0 as well. In fact, the shuffle product uses the old rules, now allowing
bra H
one extra letter x1 for either xj or xk in (3.3). As for the stuffle product, to
complement rule (3.4) we use
 yj u ∗ yk v = yj γyj (γyj u ∗ yk v) + yk γyk (yj u ∗ γyk v) + [yj , yk ]γ[yj ,yk ] (γyj u ∗ γyk v),
where γyj w = w for yj = x0j−1 x1 and γyj w = γw = w is the word with all yi
and y i toggled, while
              [yj , yk ] = [y j , y k ] = yj+k    and [yj , y k ] = [y j , yk ] = y j+k .
Then
                         ζ(w1    w ) = ζ(w ∗ w ) = ζ(w )ζ(w ).
                                      2           1      2            1       2                    (4.16)
    Exercise 4.9. (a) Prove the (finite) double shuffle relations (4.18).
                               b 0 for all w ∈ H
(b) Verify that x1 w − x1 ∗ w ∈ H               b 0 and ζ(x1 w − x1 ∗ w) = 0.      
                           4.4. An identity for alternating Euler sums                                  52

    Zhao’s proof of (4.14) follows from the three lemmas displayed below.
Though the results of Lemmas 4.8 and 4.9 represent a pure combinatorial
structure, they are merely computational. In their statements we take u =
x0 (x1 x1 + x1 x1 ) = y2 y 1 + y 2 y1 to be a particular word of weight 3.

     Lemma 4.8. For n = 0, 1, 2, . . . ,

      n
      X                                          n
                                                 X
 n           n−i           i−1
u +          u     ∗ y1u         (y2 + y 2 ) −         y 1 un−i ∗ ui−1 (y2 + y 2 ) = (−1)n (y3 + y 3 )n .
       i=1                                       i=1
                                                                                                    (4.17)

    Proof. Trivially, the statement is valid for n = 0.
    Note that the words 1, y2 + y 2 and any power of u are invariant under the
toggling operator γ : w 7→ w. This simplifies application of the stuffle rules
when these words and their products are involved. For v1 , v2 ∈ {1, y2 + y 2 },
integers k ≥ 0 and m ≥ 1 we have

       y 1 uk v1 ∗ um v2 = y 1 uk v1 ∗ (y2 y 1 + y 2 y1 )um−1 v2
                            = y 1 (uk v1 ∗ um v2 )
                                 + y2 (y 1 uk v1 ∗ y 1 um−1 v2 ) + y 2 (y 1 uk v1 ∗ y 1 um−1 v2 )
                                 + y3 (uk v1 ∗ y 1 um−1 v2 ) + y 3 (uk v1 ∗ y 1 um−1 v2 )
                            = y 1 (uk v1 ∗ um v2 ) + (1 + γ) y2 (y 1 uk v1 ∗ y 1 um−1 v2 )
                                                                                          

                              + (1 + γ) y3 (uk v1 ∗ y 1 um−1 v2 )
                                                                 

but also

       y 1 uk v1 ∗ (y2 + y 2 ) = y 1 (uk v1 ∗ (y2 + y 2 ))
                                      + y2 y 1 uk v1 + y 2 y1 uk v1 + (y3 + y 3 )uk v1
                                   = y 1 (uk v1 ∗ (y2 + y 2 )) + uk+1 v1 + (y3 + y 3 )uk v1 .
                               4.4. An identity for alternating Euler sums                                                                      53

Therefore, denoting the left-hand side of (4.17) by wn we obtain, by telescop-
ing,
                   X n                         Xn                    
             n            n−i   i−1                 n−i   i−1
     wn = u + y 1       u ∗ u (y2 + y 2 ) −        u ∗ u (y2 + y 2 )
                                     i=1                                                   i=1
                           Xn−1
                 + (1 + γ) y2     y 1 un−i−1 ∗ y 1 ui−1 (y2 + y 2 )
                                                  i=1
                               n
                               X                                                      
                                              n−i                    i−1
                           −          y1u               ∗ y1u              (y2 + y 2 )
                               i=2
                           Xn−1
                 + (1 + γ) y3     y 1 un−i−1 ∗ ui−1 (y2 + y 2 )
                                                  i=1
                               n
                               X                                                 
                                       n−i                      i−1
                           −          u            ∗ y1u              (y2 + y 2 )
                               i=2
                 − un + (y3 + y 3 )un−1
                                                                 

               = −(1 + γ)(y3 wn−1 ),

and the result follows from the inductive hypothesis wn−1 = (−1)n−1 (y3 +y 3 )n−1 .
                                                                               □

   Lemma 4.9. For n = 0, 1, 2, . . . ,
                n                                                                     n
                                  x u x (x + x ) −                                                       u x (x + x )
                X                                                                     X
           n               n−i                    i−1
      u +              u                  1             0        1          1              x1 un−i                i−1
                                                                                                                        0    1      1
                 i=1                                 i=1
                       n     2     2 ⌊n/2⌋      2 2{n/2}
                 = (−2) (x0 x1 x0 x1 )     (x0 x1 )      .                                                                                  (4.18)

    Proof. Our strategy is similar to that for the proof of Lemma 4.8 but we
deal exclusively with the shuffle in this part. Again, equality (4.18) is trivially
true for n = 0.
    Let wn denote the left-hand side of (4.18). Notice that the shuffle rules
allow to swap the role of any two letters, in particular, of x1 and x1 ; this
means that our target equality (4.18) is equivalent to

                                 wn = (−2)n (x0 x21 x0 x21 )⌊n/2⌋ (x0 x21 )2{n/2} .

Take {v1 , v2 } = {1, x0 (x1 + x1 )} and recall that u = x0 u′ , where u′ = x1 x1 +
x1 x1 . Then for non-negative integers k ≥ 1 and m ≥ 1 we get

x1 uk v1    u v = x (u v  u v ) + x (x u v  (x x + x x )u v )
                 m
                       2         1
                                      k
                                              1
                                                            m
                                                                 2           0     1
                                                                                       k
                                                                                           1         1 1               1 1
                                                                                                                              m−1
                                                                                                                                        2

                 = x (u v  u v ) + x x (x u v  x u
                                 1
                                      k
                                              1          v) m
                                                                 2           0 1       1
                                                                                           k
                                                                                               1         1
                                                                                                                 m−1
                                                                                                                        2

                   + x x (x u v  x u0 1 v ) + x x (u v  u u
                                                   1
                                                        k
                                                            1 v)        1
                                                                                m−1
                                                                                       2           0 1
                                                                                                             k
                                                                                                                 1
                                                                                                                            ′ m−1
                                                                                                                                    2
                              4.4. An identity for alternating Euler sums                                                                                  54

                         = x1 (uk v1  u v ) + x x (x u v  x u v )
                                                          m
                                                                  2             0 1           1
                                                                                                   k
                                                                                                       1       1
                                                                                                                   m−1
                                                                                                                             2

                              + x x x (x u v  u
                                    0 1 1           v ) + x x x (u v  x u
                                                      1
                                                              k
                                                                   1        v)  m−1
                                                                                              2            0 1 1
                                                                                                                     k
                                                                                                                         1           1
                                                                                                                                             m−1
                                                                                                                                                   2

                              + 2x x (u v  x u
                                          2
                                        0 1
                                                  k
                                                   v ) + x x x (u u v  u u
                                                          1             1
                                                                                m−1
                                                                              v ),        2            0 1 0
                                                                                                                   ′ k−1
                                                                                                                                 1
                                                                                                                                             ′ m−1
                                                                                                                                                       2

with the formula remaining valid for m = 0, v2 = 1 (in which case all the terms
containing um−1 have to be dropped) and for k = 0, v1 = 1 (in which case the
last term containing uk−1 has to be dropped). In addition, with v = x0 (x1 +x1 )
we have
    x1 u k    v = x (u  v) + x (x + x )x u + x x (u  (x + x ))
                          1
                                k
                                                          0        1            1     1
                                                                                              k
                                                                                                        0 1
                                                                                                               k
                                                                                                                             1           1

                 = x (u  v) + x (x + x )x u + x x (x + x )u
                          1
                                k
                                                          0        1            1     1
                                                                                              k
                                                                                                        0 1    1         1
                                                                                                                                 k

                   + x x x (u u    (x + x ))
                               0 1 0
                                              ′ k−1
                                                                            1         1

                 = x (u  v) + u
                          1
                                k
                                   + 2x x u + x x x (u u    (x + x ))
                                                          k+1                     2 k
                                                                                0 1                    0 1 0
                                                                                                                   ′ k−1
                                                                                                                                         1         1

for k ≥ 1 and

   x1 v    u = x (v  u ) + x x (x v  x u )
               m
                          1
                                         m
                                                              0 1       1                 1
                                                                                                  m−1

                + x x (x v  x u
                               0 1  ) + x x (v  u u
                                         1             )  1
                                                                  m−1
                                                                                      0 1
                                                                                                            ′ m−1

              = x (v  u ) + x x (x v  x u
                          1
                                         m
                                                )             0 1       1                 1
                                                                                                  m−1

                + x x x (x v  u
                               0 1 1) + x x x (v  x u
                                              1          )        m−1
                                                                                      0 1 1                    1
                                                                                                                   m−1

                + 2x x (v  x u   2
                                0 1) + x x x ((x + x )  u u
                                                      1
                                                               m−1
                                                                                     0 1 0              1      1
                                                                                                                             ′ m−1
                                                                                                                                         )
for m ≥ 1. Substituting these findings into the left-hand side of (4.18) we
obtain, for n ≥ 1,
                           n                                                     n
                                              x u v−                                                      u v
                           X                                                     X
                    n                   n−i                       i−1
          wn = u +                  u                     1                               x1 un−i              i−1

                              i=1                                                   i=1
                  n−1
                                                                  u                                                     x u
                  X
              =           x0 x1 x1 (x1 ui−1 v                           n−i−1
                                                                                      ) + x0 x1 x1 (ui−1 v                       1
                                                                                                                                       n−i−1
                                                                                                                                               )
                   i=1
               + 2x0 x21 (ui−1 v x1 un−i−1 )
                                            
                                              
                n
                                                                                                                   x u v)
                X
              −    x0 x1 x1 (x1 un−i ui−2 v) + x0 x1 x1 (un−i                                                            1
                                                                                                                                 i−2

                   i=2
                   + 2x0 x21 (un−i             x u v) − 2x x u
                                                          1
                                                                  i−2                           2 n−1
                                                                                              0 1

              = −2x0 x21 wn−1 .
Thus, the desired formula follows from the inductive hypothesis for wn−1 (hence
for wn−1 ).                                                                  □
   Lemma 4.10. For n = 0, 1, 2, . . . ,
                            n       1             1
            ζ x20 (x1 + x1 )     = n ζ (x20 x1 )n = n ζ({3}n ).
                                                 
                                     4             4
                      4.4. An identity for alternating Euler sums                     55

   Proof. Observe that
          dz     1 d(z 2 )          dz       −dz     2z dz       d(z 2 )
               =            and           +        =         =           .
           z     2 z2              1−z 1+z           1 − z2     1 − z2
Performing the change   of variables z 2 7→ z in the iteratedintegral (4.15) for
                n
    2
ζ x0 (x1 + x1 )    we obtain the integral for 2−2n ζ (x20 x1 )n .               □
    Proof of Theorem 4.7. The statement of Lemma 4.8 can be alterna-
tively written as
             Xn                           n
                                          X
        n         n−i    i−1
       u +       u ∗ x1 u x0 (x1 + x1 ) −   x1 un−i ∗ ui−1 x0 (x1 + x1 )
              i=1                               i=1
                      n                 n
                          x20 (x1 + x1 ) ;
                                        
             = (−1)
in other words, its left-hand side coincides with that in Lemma 4.9 except that
every shuffle product in the latter is replaced by the stuffle product in the
former. Application of the double shuffle relations (Exercise 4.9) then implies
that                        n 
            ζ x20 (x1 + x1 )     = 2n ζ (x0 x21 x0 x21 )⌊n/2⌋ (x0 x21 )2{n/2} ;
                                                                             

it remains to use Lemma 4.10 to arrive at (4.14).                               □
    The result of Lemma 4.10 is in fact a particular instance of the distribution
relation of multiple polylogarithms (3.39): for any d ∈ Z>0 and s = (s1 , . . . , sl ),
                    X
                         Lis (z1 , . . . , zl ) = dl−|s| Lis (a1 , . . . , al ).
                     zjd =aj
                    j=1,...,l

When d = 2 and a1 = · · · = al = 1, we have
                 l      X       (1 + (−1)n1 ) · · · (1 + (−1)nl )
 ζ x20 (x1 + x1 ) =                          3          3
                                                                    = 2−2l ({3}l ).
                      n >···>n >0
                                           n 1  · · · n l
                                1   l

Zhao notices that this relation does not follow from the (finite) double shuffle
relations, which are involved in the other part of his proof in [49].
     Exercise 4.10. Check that indeed x20 (x1 +x1 ) = y3 +y 3 cannot be reduced
to 41 x20 x1 = 41 y3 in H
                        b using the finite double shuffle relations.

   Hint. You can list, for example, all linear relations in H
                                                            b of weight 3.            □
                                             CHAPTER 5

                                Further relations of MZVs

                                         5.1. Ohno’s relations
    The following result contains Theorems 2.1, 2.5 and 3.7 as particular cases
(corresponding implications are given by Ohno).
    Theorem 5.1 (Ohno’s relations [29]). Let a word w ∈ H0 and its dual
w′ = τ w ∈ H0 have the following records in terms of the generators of the
algebra H1 :
                 w = ys1 ys2 · · · ysl , w′ = ys′1 ys′2 · · · ys′k .
Then, for any integer m ≥ 0, the identity
      X                                                           X
              ζ(ys1 +i1 ys2 +i2 · · · ysl +il ) =                                 ζ(ys′1 +i1 ys′2 +i2 · · · ys′k +ik )
     i1 ,i2 ,...,il ≥0                                        i1 ,i2 ,...,ik ≥0
  i1 +i2 +···+il =m                                        i1 +i2 +···+ik =m

holds.
     The proof of this theorem was given by Ohno in 1999. It used manipulations
with multiple integral representations of (generating functions of) the sums
involved in the identity. Different proofs were given later by Bradley [7] (he
proved a q-version of Theorem 5.1 — see Theorem 7.2), Okuda and Ueno [35],
and Ulanskii [43]. Here we follow a very simple and elementary proof given
by Seki and Yamamoto [39] using the method of connected sums.
     We continue to use recording of multi-indices as words over the alphabets
x0 , x1 and ys = xs−1     0 x1 , where s = 1, 2, . . . ; all the notations are as in Sec-
tion 3.1. To a (formal) variable t and two multi-indices s = (s1 , . . . , sl ) and
r = (r1 , . . . , rk ), not necessarily admissible if both non-empty, we assign the
‘connected’ sum
                  x0 x1 · · · x0sl −1 x1
               s1 −1                                                             
                                                       s            s1 , . . . , s l
           Z r1 −1                          t =Z         t =Z                        t
                  x0 x1 · · · xr0k −1 x1               r            r1 , . . . , rk
                          X                                    1
                 =                  C(n1 , m1 ; t) s1 −1
                      n1 >···>nl >0
                                                  n1 (n1 − t) · · · nsl l −1 (nl − t)
                         m1 >···>mk >0
                                                                         1
                                            ×                                           ,                         (5.1)
                                                mr11 −1 (m1 − t) · · · mrkk −1 (mk − t)
where the connector C(n, m) is defined by
                                   (1 − t)n (1 − t)m   Γ(n + 1 − t)Γ(m + 1 − t)
              C(n, m; t) =                           =
                                      (1 − t)n+m       Γ(1 − t)Γ(n + m + 1 − t)
                                                      56
                                    5.1. Ohno’s relations                         57

(we refer to the Pochhammer symbol (1.16)) and C(n, ∅; t) = C(∅, m; t) = 1
(this is the case when one of multi-indices s and r is not present, so that
the corresponding sum in (5.1) degenerates to a sum over single group of
variables). Without the connector in (5.1), the right-hand side would be simply
the product of two multiple sums (the product ζ(s)ζ(r) when t = 0 provided
both s and r are admissible). The symmetry
                                               
                               s             r
                           Z       t =Z          t                         (5.2)
                               r             s
is clear from the definition, and we also have
                     x01 x1 · · · xs0l −1 x1
                    s −1                                          
                                                            s
                 Z                             t =Z                t
                                1                          −
                           X                          1
                    =                                                          (5.3)
                                    n
                       n1 >···>nl >0 1
                                      s1 −1
                                            (n1 − t) · · · nsl l −1 (nl − t)
in the case when the second multi-index is absent.
   Exercise 5.1. Assume that t is real, t < 1. Prove that the multiple sum
indeed converges if both s and r have length at least 1.
   The main rationale behind the definition (5.1) is the following property of
the connected sums.
    Lemma 5.2 (Transporting relations). If s1 > 1 then
                                                              
                    s1 , . . . , s l        s1 − 1, . . . , sl
                Z                    t =Z                       t ;            (5.4)
                   r1 , . . . , r k          1, r1 , . . . , rk
if s1 = 1 then
                                                                 
                       1, s2 , . . . , sl         s2 , . . . , s l
                     Z                    t =Z                     t .         (5.5)
                        r1 , . . . , r k        r1 + 1, . . . , rk
Equivalently (and uniformly),
                                             
                            xε u          u
                        Z        t =Z          t                               (5.6)
                             v          x1−ε v
for xε ∈ {x0 , x1 } and two words u, v over the alphabet {x0 , x1 }.
   Proof. Clearly, property (5.4) follows from (5.5) and the symmetry (5.2).
To prove (5.5), observe that
          1               (1 − t)n−1 (1 − t)m
             C(n, m; t) =
         n−t                  (1 − t)n+m
                                                                 
                          1 (1 − t)n−1 (1 − t)m (1 − t)n (1 − t)m
                        =                       −
                          m      (1 − t)n+m−1         (1 − t)n+m
                          1                             
                        =    C(n − 1, m; t) − C(n, m; t) ,
                          m
                     5.2. The Maesaka–Seki–Watanabe formula                                58

hence
                             ∞
                             X  C(n1 , m1 ; t)   C(n2 , m1 ; t)
                                               =
                        n =n +1
                                  n1 − t             m
                         1     2

by telescoping, where n2 = 0 if l = 1.                                                     □
    Exercise 5.2. Using properties (5.2), (5.3) and (5.6) give another proof
of Euler’s identity (1.13).
   Proof of Theorem 5.1. The properties of the Seki–Yamamoto connected
sums (5.1) imply
                                                                                   
      X                             1                            w                1
                  s1 −1                    sl −1            =Z      t = ··· = Z      t
                n 1     (n 1 −  t) · · · n l     (n l −  t)       1              τ w
  n1 >···>nl >0
              X                               1
      =                    ′
                         s1 −1                     s′ −1
                                                                .
         n1 >···>nk >0 n1      (n1 − t) · · · nkk (nk − t)
It remains to expand both sides in powers of t using
                                                   ∞
                         1              1        X     ti
                                =              =
                   ns−1 (n − t)   ns (1 − t/n)    i=0
                                                      ns+i
and compare the coefficients of tm .                                                       □
   It is straightforward that case m = 0 in Theorem 5.1 is the duality theorem
(Theorem 3.7).
    Exercise 5.3. (a) Show that the choice m = 1 in Theorem 5.1 corre-
    sponds to Hoffman’s relations (Theorem 2.1).
(b) Show that, if multi-index s in Theorem 5.1 is one-component (that is,
    s = (s)), then the theorem reduces to the sum theorem (Theorem 2.5).
   Exercise 5.4 ([35]). Deduce Theorem 5.1 from the Landen connection
formula in Exercise 3.9.
               5.2. The Maesaka–Seki–Watanabe formula
    As another illustration of the power of the method of connected sums used
in the previous section, we prove a refinement of the link between the multiple
zeta values defined via the the sum (2.1) and their representation (3.18) as
iterated integrals. For the former we use the multiple harmonic sums
                                                    X                1
           ζ<N (s) = ζ<N (s1 , . . . , sl ) =
                                                               n n · · · nsl l
                                                                s1 s2
                                              N >n >n >···>n ≥1 1 2
                                                      1   2      l

from Section 3.4, while for the latter we introduce a new type of multiple sum
                                             l
             ♭
                                   X         Y                       1
            ζ<N (s) =                                                                   (5.7)
                                             j=1
                                                   nj1 nj2 · · · nj,sj −1 (N − njsj )
                        N >n11 ≥···≥n1s1
                          >n21 ≥···≥n2s2
                             .........
                         >nl1 ≥···≥nlsl >0
                          5.2. The Maesaka–Seki–Watanabe formula                                              59

inspired by the representation (3.18). Indeed, we have n1 = N1 · n/N 1
                                                                          and N 1−n =
 1       1
N
    · 1−n/N  , and this allows us to recognise the sum in (5.7) as an N -regular
Riemann sum for the integral (3.18). For example,
   ♭               1            X                            1
  ζ<N  (2, 1, 3) = 6                         n1
                  N N >n ≥n >n >n ≥n ≥n >0 N (1 − N ) · (1 − nN3 ) · nN4 nN5 (1 − nN6 )
                                                    n2
                               1    2    3     4   5   6

which is a regular Riemann sum that approximates the iterated integral
    Z
                                 dz1 dz2    dz3     dz4 dz5 dz6
                                          ·       ·               = ζ(2, 1, 3);
     1>z1 >z2 >z3 >z4 >z5 >z6 >0 z1 1 − z2 1 − z3    z4 z5 1 − z6
thus, we obtain
                                        ♭
                                   lim ζ<N (2, 1, 3) = ζ(2, 1, 3).
                                   N →∞

    Exercise 5.5. Verify that
                                                  ♭
                                             lim ζ<N (s) = ζ(s)
                                         N →∞

for all admissible s.
    Quite amazingly, as shown by Maesaka, Seki and Watanabe in [28], the
limiting equality
                           ♭
                      lim ζ<N (s) = ζ(s) = lim ζ<N (s)
                             N →∞                               N →∞
for admissible s has the following natural refinement.
    Theorem 5.3. For any index s (not necessarily admissible) and any inte-
ger N > 0, we have
                                      ♭
                           ζ<N (s) = ζ<N (s).                         (5.8)
   Proof. It is convenient to introduce the compact notation ΣN (s) for the
summation indices
                   n = (n11 , . . . , n1s1 , n21 , . . . , n2s2 , . . . , nl1 , . . . , nlsl )
in (5.7). The choice of connected sums is
  ZN (s | r) = ZN (s1 , . . . , sl | r1 , . . . , rk )
                            l                                                                     k
                X           Y                      1                                             Y    1
      =                                                                · CN (nlsl − 1, m1 ) ·          ri ,
                           j=1
                                   nj1 · · · nj,sj −1 (N − njsj )                                i=1
                                                                                                     m i
             n∈ΣN (s)
          N >m1 >···>mk >0

where the connector CN (n, m) is given by
                           n
                             
                           m         n(n − 1) · · · (n − m + 1)
             CN (n, m) = N −1 =                                    .
                           m
                                   (N − 1)(N   −   2) · · · (N − m)
The transport identity
                                    ZN (s, t | r) = ZN (s | t, r)                                      (5.9)
                                5.3. Ihara–Kaneko derivations                                    60

then implies that
          ♭
         ζ<N (s) = ZN (s1 , . . . , sl | ∅) = ZN (s1 , . . . , sl−1 | sl ) = · · ·
                  = ZN (s1 | s2 , . . . , sl ) = ZN (∅ | s1 , s2 , . . . , sl ) = ζ<N (s),
which is precisely the identity in (5.8).
    The remaining check of (5.9) follows from application once of the telescop-
ing identity
                  N −1                                      N −1
 CN (n − 1, m)    X    CN (n − 1, a − 1) − CN (N − 1, a)    X    CN (n, a)
               =                                         =
    N −n         a=m+1
                                     N −n                  a=m+1
                                                                    n

and then t times of the identity
          n                     n
          X CN (b, m)           X CN (b, m) − CN (b − 1, m)                CN (n, m)
                            =                                          =             .           □
          b=1
                     b          b=1
                                                    m                          m

    Finally notice that Hirose, Matsusaka and Seki [14] generalise the formula
from Theorem 5.3 to the case of multiple polylogarithms; some further varia-
tions on the theme are discussed by Yamamoto in [46].

                          5.3. Ihara–Kaneko derivations
    Theorem 3.12 has a natural generalization. For any n ≥ 1, define the anti-
symmetric derivation ∂n ∈ Der(H) by the rule ∂n x0 = x0 (x0 + x1 )n−1 x1 ; as
mentioned in the proof of Theorem 3.3, we have ∂1 = D − D = δ∗ − δ . The
following result is valid.
   Theorem 5.4. For any n ≥ 1 and any word w ∈ H0 , the identity
                                          ζ(∂n w) = 0                                        (5.10)
holds.
    In what follows, we describe a scheme of the proof of the theorem given
by Kaneko and Ihara [23] (see also [24]); a different proof was provided by
Hoffman and Ohno [21].
    For each integer n ≥ 1 define the derivation Dn ∈ Der(H) setting Dn x0 = 0
and Dn x1 = xn0 x1 . It may be easily justified that the derivations D1 , D2 , . . .
pairwise commute; this holds for the dual derivations D1 , D2 , . . . as well. Con-
sider a completion of H, namely the algebra H   b = Q⟨⟨x0 , x1 ⟩⟩ of formal power
series in non-commutative variables x0 , x1 over the field Q. Action of the
anti-automorphism τ and of derivations δ ∈ Der(H) is naturally extended to
the whole algebra H.b For simplicity, the record w ∈ ker ζ will mean that all
homogeneous components of the element w ∈ H     b belongs to ker ζ. The maps
                                   ∞                       ∞
                                   X Dn                    X Dn
                             D=               ,      D=
                                    n=1
                                          n                 n=1
                                                                  n
                                  5.3. Ihara–Kaneko derivations                                 61

are derivations of the algebra H,
                               b and the standard relation of a derivation and
homomorphism implies that the maps
                           σ = exp(D),               σ = τ στ = exp(D)
are automorphisms of the algebra H.
                                  b By the above means, Ohno’s relations
(Theorem 5.1) may be re-stated as follows.
   Theorem 5.5. For any word w ∈ H0 , the inclusion
                                             (σ − σ)w ∈ ker ζ                               (5.11)
holds.
   Proof. Since Dx0 = 0 and
                       x20 x30
                                     
          Dx1 = x0 +      +    + · · · x1 = (− log(1 − x0 ))x1 ,
                       2    3
we may conclude that Dn x0 = 0 and Dn x1 = (− log(1−x0 ))n x1 , hence σx0 = x0
and
       ∞
      X   1
σx1 =        (− log(1 − x0 ))n x1 = (1 − x0 )−1 x1 = (1 + x0 + x20 + x30 + · · · )x1 .
      n=0
          n!
Therefore, for the word w = ys1 ys2 · · · ysl ∈ H0 , we have
         σw = σ(xs01 −1 x1 xs02 −1 x1 · · · x0sl −1 x1 )
              = xs01 −1 (1 + x0 + x20 + · · · )x1 xs02 −1 (1 + x0 + x20 + · · · )x1 · · ·
                 · · · x0sl −1 (1 + x0 + x20 + · · · )x1
                ∞
                X           X
              =                      xs01 −1+e1 x1 xs02 −1+e2 x1 · · · x0sl −1+el x1 ;
                 n=0     e1 ,e2 ,...,el ≥0
                       e1 +e2 +···+el =n

thus σw − στ w ∈ ker ζ by Theorem 5.1. Applying now Theorem 3.7 (with
m = n), we arrive at the desired inclusion (5.11).                 □
   Recalling ∂1 , ∂2 , . . . , consider the derivation
                                        ∞
                                       X   ∂n
                                  ∂=          ∈ Der(H).
                                                      b
                                       n=1
                                            n
   Lemma 5.6. The following equality holds:
                                             exp(∂) = σ · σ −1 .                            (5.12)
    Proof. First of all, let us note pairwise commutativity of the operators ∂n ,
n = 1, 2, . . . . Indeed, since ∂n (x0 + x1 ) = 0 for any n ≥ 1, it is sufficient to
verify the equality ∂n ∂m x0 = ∂m ∂n x0 for n, m ≥ 1. Taking in mind that
∂n (x0 + x1 )k = 0 for any n ≥ 1 and k ≥ 0, we obtain the desired property:
∂n ∂m x0 = ∂n (x0 (x0 + x1 )m−1 x1 )
         = x0 (x0 + x1 )n−1 x1 (x0 + x1 )m−1 x1 − x0 (x0 + x1 )m−1 x0 (x0 + x1 )n−1 x1
                             5.3. Ihara–Kaneko derivations                                       62

         = x0 (x0 + x1 )n−1 (x0 + x1 − x0 )(x0 + x1 )m−1 x1
             − x0 (x0 + x1 )m−1 (x0 + x1 − x1 )(x0 + x1 )n−1 x1
         = −x0 (x0 + x1 )n−1 x0 (x0 + x1 )m−1 x1
              + x0 (x0 + x1 )m−1 x1 (x0 + x1 )n−1 x1
         = ∂ m ∂ n x0 .

   Consider the family φ(t), t ∈ R, of automorphisms of the algebra H           bR =
                                          ′
R⟨⟨x0 , x1 ⟩⟩, defined on the generators x0 = x0 + x1 and x1 by the rules
                                                                          −1
                                                       1 − (1 − x′0 )t
                                                  
                ′      ′                    ′ t
       φ(t) : x0 7→ x0 , φ(t) : x1 7→ (1 − x0 ) x1 1 −                 x1     ,
                                                            x′0
where t ∈ R. Routine verification shows that
                                          d
  φ(t1 )φ(t2 ) = φ(t1 + t2 ), φ(0) = id,    φ(t)     = ∂,                    φ(1) = σ · σ −1 ;
                                         dt      t=0

hence φ(t) = exp(t∂) and substitution t = 1 leads to the required result (5.12).
                                                                              □
   Proof of Theorem 5.4. Now let us show how Theorem 5.4 follows from
Theorem 5.5 and Lemma 5.6. First we have
                                                        ∞
                                                       X   ((σ − σ)σ −1 )n−1 −1
 ∂ = log(σ · σ −1 ) = log(1 − (σ − σ)σ −1 ) = −(σ − σ)                      σ
                                                       n=1
                                                                  n

and secondly
                                                                       ∞
                                 −1
                                                                       X ∂ n−1
           σ − σ = (1 − σ · σ )σ = (1 − exp(∂))σ = −∂                                σ,
                                                                       n=1
                                                                                n!

hence ∂H0 = (σ − σ)H0 , and Theorem 5.5 yields the required identities (5.10).
                                                                            □
   Does there exist a simpler way of proving relations (5.10)? Explicit com-
putations show that ∂1 = δ∗ − δ ,
                  ∂2 = [δ∗ , δ ∗ ],
                       1                      1             1
                  ∂3 = [δ∗ , [∂1 , δ ∗ ]] − [δ∗ , ∂2 ] − [δ ∗ , ∂2 ],
                       2                      2             2
                       1                          1
                  ∂4 = [δ∗ , [∂1 , [∂1 , δ ∗ ]]] − [δ ∗ , [δ∗ , [∂1 , δ ∗ ]]]
                       6                          6
                              1                   1               1
                         + [∂1 , [∂2 , δ ∗ ]] + [∂3 , δ∗ ] + [∂3 , δ ∗ ]
                              6                   3               3
and, in addition, δ∗ + δ ∗ = δ + δ  ; therefore cases n = 1, 2, 3, 4 in Theo-
rem 5.4 are served by induction (with Theorem 3.12 as inductive base). This
circumstance motivates the following hypothesis.
                         5.4. Open questions about MZVs                         63

     Conjecture 5.7. For any n ≥ 1, the above-defined anti-symmetric deriva-
tion ∂n is contained in the Lie subalgebra of Der(H) generated by the derivations
δ∗ , δ ∗ , δ , and δ  .

                      5.4. Open questions about MZVs
    In addition to Conjectures 1.10, 3.4 and 5.7 given earlier, we mention a
series of other important conjectures concerning the structure of the subspace
ker ζ ⊂ H. Denote by Zk the Q-vector space in R spanned by multiple zeta
values of weight k; in particular, Z0 = Q and Z1 = {0}. Then the Q-subspace
Z ∈ R spanned by all multiple zeta values is the subalgebra of R over Q graded
by weight.
   Conjecture 5.8. As a Q-algebra, the algebra Z is the direct sum of the
subspaces Zk , where k = 0, 1, 2, . . . .
   It can be easily seen that relations (3.6)–(3.8) for multiple zeta values are
homogeneous in weight, hence Conjecture 5.8 follows from Conjecture 3.4.
   Denoting by dk the dimension of the Q-space Zk , k = 0, 1, 2, . . . , note that
d0 = 1, d1 = 0, d2 = 1 (since ζ(2) ̸= 0), d3 = 1 (since ζ(3) = ζ(2, 1) ̸= 0)
and d4 = 1 (since Z4 = Qπ 4 by Exercise 3.3 (i)). For k ≥ 5, above-deduced
identities allow to compute the upper bounds; for instance, d5 ≤ 2, d6 ≤ 2,
d7 ≤ 3 (see Exercise 3.3), and so on.
   Conjecture 5.9. For k ≥ 3, the recurrence relations
                                dk = dk−2 + dk−3                           (5.13)
hold; equivalently,
                            ∞
                            X                     1
                                   dk tk =               .
                             k=0
                                             1 − t2 − t3
    It is now shown dimQ Zk ≤ dk for all k, where the sequence dk is defined
by the recursion (5.13) (and d0 = d2 = 1, d1 = 0). There are several proofs
of this result, due to Terasoma [41], to Deligne and Goncharov [10], and to
F. Brown [8]; all are algebraic and use motivic interpretations of the multiple
zeta values.
    Even if Conjectures 5.8 and 5.9 are confirmed, the question of choosing
a transcendence basis of the algebra Z and (or) a rational basis of the Q-
spaces Zk , k = 0, 1, 2, . . . , is still open. Concerning this problem, we find
the next conjecture of Hoffman rather natural (compare, for example, with
Exercise 3.4 (b)).
    Conjecture 5.10 (Hoffman’s basis). For any k = 0, 1, 2, . . . , a basis of
the Q-spaces Zk is given by the set of numbers
                
                  ζ(s) : |s| = k, sj ∈ {2, 3}, j = 1, . . . , ℓ(s) .    (5.14)
   A serious argument for Conjecture 5.10 to be valid, is not only experimental
confirmation for k ≤ 16 (under the hypothesis of Conjecture 3.4) but also
                            5.4. Open questions about MZVs                                64

agreement of the dimension of the Q-space spanned by the numbers (5.14)
with the dimension dk of the spaces Zk in Conjecture 5.9.
    Exercise 5.6. For given k = 0, 1, 2, . . . , show that the number of MZVs
in (5.14) is equal to dk . Here dk is the same sequence defined earlier in (5.13).
    Although proving Conjectures 5.8–5.10 in the form given is hopeless at the
present time, the ‘true’ MZVs in R are the images under a Q-linear map of cer-
tain motivic MZVs which are defined purely algebraically. The Terasoma [41]
and Deligne–Goncharov [10] bound dimQ Zk ≤ dk , as well as Conjecture 5.8
about disjointness of the subspaces Zk , are shown to be true for the motivic
MZVs. Terasoma and Goncharov established the bound by showing that all
MZVs are periods of so-called mixed Tate motives that are unramified over Z.
Another well-known conjecture in the area states the converse, that is, that all
periods of mixed Tate motives over Z can be expressed as linear combinations
(over Q[(2πi)±1 ]) of MZVs. Equivalently, this says that the dimension of the
space of motivic MZVs of weight k is exactly dk .
    Brown [8] proved the latter conjecture and also the fact that the motivic
MZVs from Hoffman’s conjectural basis in Conjecture 5.10 form a basis of the
corresponding Zk . Brown’s proof requires quite specific properties of certain
coefficients occurring in the relations over Q of some special MZVs; namely,
that the MZVs
                    ξ(m, n) = ζ({2}m , 3, {2}n ) for n, m ≥ 0,
which are part of Hoffman’s basis, are Q-linear combinations of products
π 2µ ζ(2ν + 1) with µ + ν = m + n + 1. A very explicit version of such a
formula was given by Zagier [48]; we discuss this remarkable identity of MZVs
in Section 6.2.
     Our final exercise in this part relates counting of the number of MZVs to
partitions.
    Exercise 5.7. (a) How many different MZVs of given weight k exists?
                               1/k
    (b) Compute the limit of dk as k → ∞ for the sequence dk constructed
in Conjecture 5.9.
    (c) Any polynomial in single zeta values,
         (π 2 )s0 ζ(3)s1 ζ(5)s2 · · · ζ(2l + 1)sl ,   s0 , s1 , s2 , . . . , sl ∈ Z≥0 ,
belongs to the linear space Zk of MZVs of weight
                      k = 2s0 + 3s1 + 5s2 + · · · + (2l + 1)sl .
Assuming Conjecture 1.10, all these polynomials are linearly independent over Q.
Denote by ck the total number of such polynomials of given weight k. Compute
ck for small values of k (namely, for k ≤ 12) and show that ck < dk for k ≥ 8.
(In other words, the algebra of MZVs cannot be fully generated by single zeta
values.)
    (d) For the sequence ck from part (c), find a general analytic formula and
                        1/k
compute the limit of ck as k → ∞.
                                   CHAPTER 6

              The two-one formula and its relatives

                            6.1. The two-one formula
    In the introductory section the following alternative version of the multiple
zeta values with non-strict inequalities was mentioned (see (2.2)):
                                                          X              1
             ζ ⋆ (s) = ζ ⋆ (s1 , s2 , . . . , sl ) =                               .
                                                                   n n · · · nsl l
                                                                    s1 s2
                                                     n ≥n ≥···≥n ≥1 1 2
                                               1   2     l

Exercise 2.2 gives a simple recipe to pass from one model to the other.
    Relation (2.3) is an example of simple relations for the multiple zeta star
values; its companion is
                                                         ∞
                  ⋆     k            1−2k
                                                         X (−1)n−1
                 ζ ({2} ) = 2(1 − 2         )ζ(2k) = 2               .
                                                         n=1
                                                               n2k

(This expression can be compared with the one for ζ({2}k ) given in (4.4) and
reproduced in (6.11) below.)
    The starting goal of our joint project with Ohno (in 2006) was not just
finding a general form of the two families of identities for the MZSVs but
searching for alternatives of Hoffman’s basis (5.14) in terms of multiple zeta
star values. Note the one can replace that basis with its dual (the order is
swapped and each 3 is replaced with 2, 1)
    
      ζ(s) : |s| = k, sj ∈ {2, 1}, j = 1, . . . , ℓ(s), no 1s next to each other .
                                                                                 (6.1)
Another choice of the basis
                   ⋆
                    ζ (s) : |s| = k, sj ∈ {2, 3}, j = 1, . . . , ℓ(s) .
was also proposed at the time in [22], and later confirmed by Glanois [11]; the
equivalence of the two Hoffman’s basis conjecture was also discussed by Zagier
and Brown. Essentially, the original question was whether one could replace
(conjecturally) the MZVs in the ‘dual’ Hoffman’s basis (6.1) with MZSVs. We
found that this is not the case already in weight 12 by showing that ζ ⋆ ({2, 1}4 )
is a rational multiple of π 12 , hence of ζ ⋆ ({2}6 ). However, on this way we suc-
ceeded in generalising (2.3), conjecturally. Some particular cases of our conjec-
ture — dubbed as the ‘two-one formula’ — were established by ourselves, and
it was finally proved in full generality by Zhao in 2013. One of lucky accidents
of our proofs was a discovery of the weighted version (2.11) of Euler’s original
formula (2.10) (the sum formula of depth 2 in the modern terminology).
                                          65
                                  6.1. The two-one formula                            66

      Theorem 6.1 (Two-one formula). For k = 0, 1, 2, . . . , denote µ2k+1 =
({2}k , 1). Then for any admissible index s = (s1 , s2 , . . . , sl ) with odd entries
s1 , . . . , sl , the following identities are valid:
                                                         X
                        ζ ⋆ (µs1 , µs2 , . . . , µsl ) =   (−1)σ(p) 2l−σ(p) ζ ⋆ (p) (6.2)
                                                  p
                                                 X
                                             =        2l−σ(p) ζ(p),                (6.3)
                                                  p

where, as in Exercise 2.1, p runs through all indices of the form (s1 ◦ s2 ◦
· · · ◦ sl ) with ‘◦’ being either the symbol ‘,’ or the sign ‘+’, and the exponent
σ(p) denotes the number of signs ‘+’ in p.
    Surprisingly enough, the pattern in (6.2), (6.3) is similar to that in Exer-
cise 2.1. One particular instance corresponding to l = 2,
        ζ ⋆ ({2}s1 , 1, {2}s2 , 1) = 2ζ(2s1 + 2s2 + 2) + 4ζ(2s1 + 1, 2s2 + 1),
was shown to be true in our original work with Ohno (by an elaborate de-
scending inductive argument given in eight lemmas!). It implies the equality
    ζ ⋆ ({2}s1 , 1, {2}s2 , 1) + ζ ⋆ ({2}s2 , 1, {2}s1 , 1)
          = 4ζ(2s1 + 2s2 + 2) + 4ζ(2s1 + 1, 2s2 + 1) + 4ζ(2s2 + 1, 2s1 + 1)
          = 4ζ(2s1 + 1)ζ(2s2 + 1) = ζ ⋆ ({2}s1 , 1)ζ ⋆ ({2}s2 , 1)
when s1 , s2 ≥ 1, which does not seem to be generalisable further to cases l > 2.
A related formula
                   ζ ⋆ ({2, {1}m−1 }n , 1) = (m + 1)ζ((m + 1)n + 1)
for any positive integers m, n was given two different proofs are given by Zlobin
and Ohno–Wakabayashi. If m = 1 it is nothing but formula (2.3), while
if m ≥ 2 then its left-hand side equals ζ ⋆ ({µ3 , {µ1 }m−2 }n , µ1 ), so that the
two-one formula implies the closed-form evaluation of the corresponding right-
hand side in (6.2) (equivalently, in (6.3)) by means of the single zeta value
(m + 1)ζ((m + 1)n + 1), where the integers m ≥ 2 and n ≥ 1 are arbitrary.
    Exercise 6.1. Show the equality of the right-hand sides in (6.2) and (6.3).
    Hint. Use Exercise 2.1.                                                           □
    On the right-hand side of (6.2) and (6.3) we have MZSVs and MZVs of
length at most l, while the left-hand side involves a single zeta star attached
to an index with entries 2 and 1 only (and the number of 1’s is equal to l);
the latter circumstance was the reason of dubbing the formula as the two-
one formula. The formula does not seem to be a specialization of identities for
polylogarithms (3.9) but, after Zhao’s proof, is linked to the multiple harmonic
sums (3.24), their star counterparts
                                                         X                1
        H ⋆ (s; N ) = H ⋆ (s1 , . . . , sl ; N ) =                                  ,
                                                                    n n · · · nsl l
                                                                     s1 s2
                                                   N ≥n ≥n ≥···≥n ≥1 1 2
                                                        1     2   l
                                       6.1. The two-one formula                                         67

but also to a different type
                           X                      N !2                 1
        H(s;
         b N) =
                                                                  s1 s2       sl ,
                         N ≥n >n >···>n ≥1
                                           (N − n1 )! (N + n1 )! n1 n2 · · · nl
                               1   2        l

where N = 0, 1, 2, . . . and H(
                             e ; N ) = H(
                                       b ; N ) = 1 for the empty index s. As
seen earlier
                  lim H(s; N ) = ζ(s) and                  lim H ⋆ (s; N ) = ζ ⋆ (s)
                 n→∞                                      n→∞

when s1 > 1.
    Exercise 6.2. Show that for admissible multi-indices s, we have
                          lim H(s;
                                b N ) = ζ(s).
                                        n→∞

   Hint. The limit relation is equivalent to showing that, for k ≥ 2 and any
multi-index s = (s1 , . . . , sl ),
                  N
                                               N !2
                                                         
                 X      H(s; m − 1)
             lim                     1−                      = 0.       (6.4)
            N →∞
                 m=1
                                mk      (N − m)! (N + m)!
(Notice that the expression in the parentheses is always positive.) Try first to
prove (6.4) in the toughest possible case k = 2, s1 = · · · √
                                                            = sl = 1. One√
                                                                         possible
strategy is to split the sum into two, according to m ≤ N and m > N ; use
an estimate for the expression in the parentheses for the first sum and some
trivial estimates for the second one.                                          □
  With the above notation in mind Theorem 6.1 is the limiting case, as
N → ∞, of the following result.
    Theorem 6.2. For any N ∈ N,
                                                                     X
H ⋆ ({2}s1 , 1, {2}s2 , 1, . . . , {2}sl , 1; N ) = 2                                      2σ̄(p) H(p;
                                                                                                  b    N ),
                                                        p=(2s1 +1)◦(2s2 +1)◦···◦(2sl +1)
                                                                         (6.5)
where ◦ is either comma or plus and σ̄(p) denotes the exact number of commas.
     Proof. For aesthetic reasons we will write HN⋆ (s) and H b N (s) for H ⋆ (s; N )
and H(s;
      b N ), respectively. The proof of (6.5) is by induction on N + l. As
H1⋆ (s) = 1 for any s and Hb 1 (s) = 1/2 if l = 1 and 0 otherwise, the equality in
(6.5) is trivially true when N = 1 and l ≥ 0 is arbitrary.
     Furthermore, assume that N > 1 and use the definition to write
                 HN⋆ ({2}s1 , 1, {2}s2 , 1, . . . , {2}sl , 1)
                        s1
                       X        1
                    =         2s 1 −2k
                                       HN⋆ −1 ({2}k , 1, {2}s2 , 1, . . . , {2}sl , 1)
                       k=0
                           n
                                   1
                           +              HN⋆ ({2}s2 , 1, . . . , {2}sl , 1).
                               N 2s1 +1
                                          6.1. The two-one formula                                               68

Applying the induction statement to the newer multiple harmonic sums we
obtain

                  HN⋆ ({2}s1 , 1, {2}s2 , 1, . . . , {2}sl , 1)
                                s1
                          2 X                           X
                     = 2s1          N 2k                                           2σ̄(p) H
                                                                                          b N −1 (p)
                        N      k=0                p=(2k+1)◦(2s2 +1)◦···◦(2sl +1)
                                     2                   X
                             +                                          2σ̄(p) H
                                                                               b N (p).                     (6.6)
                                  N 2s1 +1
                                              p=(2s2 +1)◦···◦(2sl +1)

   Using then the geometric sum
                              s1    2k
                              X    N                     1 N 2s1 +2 − n2s 1
                                                                            1 +2

                                                    =
                              k=0
                                         n1             n2s
                                                         1
                                                            1
                                                              (N − n1 )(N + n1 )

we deduce that
        s1
        X
              N 2k H
                   b N −1 (p1 + 2k, p2 , . . . , pr )
        k=0
                                   X               N !2                    1
          = N 2s1                                                  p1 +2s1 p2
                          N >n >n >···>n ≥1
                              1     2
                                            (N − n1 )! (N + n1 )! n1
                                              r
                                                                          n2 · · · npr r
                           1             X           N !2                  1
                     −                                               p1 −2 p2
                          N N >n >n >···>n ≥1 (N − n1 )! (N + n1 )! n1 n2 · · · npr r
                             2
                                    1     2         r

                                   X               N !2                    1
          = N 2s1                                                  p1 +2s1 p2
                          N ≥n >n >···>n ≥1
                              1     2
                                            (N − n1 )! (N + n1 )! n1
                                              r
                                                                          n2 · · · npr r
                           1             X           N !2                  1
                     −                                               p1 −2 p2
                          N N ≥n >n >···>n ≥1 (N − n1 )! (N + n1 )! n1 n2 · · · npr r
                             2
                                    1     2         r

                                                                  1 b
          = N 2s1 H
                  b N (p1 + 2s1 , p2 , . . . , pr ) −                HN (p1 − 2, p2 , . . . , pr ).
                                                                  N2

Therefore, the equality in (6.6) can be written as
                                                                           X
 HN⋆ ({2}s1 , 1, {2}s2 , 1, . . . , {2}sl , 1) − 2                                              2σ̄(p) H
                                                                                                       b N (p)
                                                             p=(2s1 +1)◦(2s2 +1)◦···◦(2sl +1)
              2                   X
    =                                               2σ̄(p) H
                                                           b N (p)
        N 2s1 +1
                      p=(2s2 +1)◦···◦(2sl +1)
                      2                       X
          −                                                    2σ̄(p) H
                                                                      b N (p)
                  N 2s1 +2
                             p=(−1)◦(2s2 +1)◦···◦(2sl +1)
                                       6.1. The two-one formula                                              69

(we expand the first ◦ in p = (−1) ◦ (2s2 + 1) ◦ · · · ◦ (2sl + 1))
           2                  X
    =                                        2σ̄(p) H
                                                    b N (p)
        N 2s1 +1
                   p=(2s2 +1)◦···◦(2sl +1)
                   2               X
          −                                        2σ̄(p) H
                                                          b N (p)
               N 2s1 +2
                           p=(2s2 )◦···◦(2sl +1)
                           N
                   4       X      N !2                                       X
          −                                   m                                               2σ̄(p) Hm−1 (p).
               N 2s1 +2 m=1 (N − m)! (N + m)!
                                                                    p=(2s2 +1)◦···◦(2sl +1)
                                                                                                          (6.7)
   Finally, the other identity
              N
              X         N !2
          2                         m Hm−1 (p1 , p2 , . . . , pr )
              m=1
                  (N − m)! (N + m)!
                       N                       m−1
                       X         N !2          X Hn −1 (p2 , . . . , pr )
                                                    1
               =2                            m
                       m=1
                           (N − m)! (N + m)!   n =1
                                                        np11
                                                               1

                   N                                         N
                   X    Hn1 −1 (p2 , . . . , pr )            X     N !2
               =                                  · 2                          m
                   n =1
                                np11                  m=n +1
                                                             (N − m)! (N + m)!
                       1                                       1

(the internal sum is summed by Exercise 6.3 below)
                   N
                   X Hn −1 (p2 , . . . , pr )
                               1                             (N − n1 ) N !2
               =                                      ·
                   n1 =1
                                     np11                 (N − n1 )! (N + n1 )!
                  b N (p1 , p2 , . . . , pr ) − H
               = NH                             b N (p1 − 1, p2 , . . . , pr )

simplifies the right-hand side of (6.7) to zero.                                                             □
   Exercise 6.3. For integers N > 0 and n ≥ 0, show
                           N
                               m N      N Nn−1
                                              
                          X
                                   m
                       2        N +m
                                      = N +n .
                                      m=n+1          m                n

   Hint. Use a telescoping argument: verify that
   2m N                                              (N + m) N
                                                               
       m                                                      m
    N +m
         = G(N, m + 1) − G(N, m), where G(N, m) = −    N +m
                                                              ,
      m                                                                                            m

and sum both sides of the identity over m from n + 1 to N .                                                  □
   Finally, we point out that using the integral representation of MZSVs,
                                                dt1 · · · dts1 +···+sl
                      Z     Z
               ⋆
              ζ (s) = · · ·                  Ql
                             [0,1]s1 +···+sl  i=1 (1 − t1 · · · ts1 +···+si )
                                       6.2. Zagier’s identity                                  70

(compare with (3.27)) valid for any admissible multi-index s = (s1 , . . . , sl ), we
can write the right-hand side of (6.2) as follows:
                                Ql−1
                                      (1 + t1 · · · ts1 +···+si )
        Z     Z
      2 ···                     Qli=1                               dt1 · · · dts1 +···+sl . (6.8)
                [0,1]s1 +···+sl  i=1  (1 − t1 · · · ts 1 +···+s i
                                                                  )
The change of variable uj = t1 · · · tj for j = 1, . . . , s1 +· · ·+sl gives the integral
         Z      Z      Y           Y i −1 duj (1 + us +···+s ) dus +···+s 
                       l−1  s1 +···+s
                                                               1         i         1        i
    2       ···                                    ·
                       i=1 j=s +···+s      +1
                                               uj      (1   − u s 1 +···+s i
                                                                             )us 1 +···+s i
      1>u1 >···>us1 +···+sl >0          1     i−1

                      Y l −1
                  s1 +···+s
                                    duj   dus1 +···+sl
            ×                           ·              ,                                    (6.9)
                j=s1 +···+sl−1   +1
                                    uj 1 − us1 +···+sl

where the empty sum s1 + · · · + si−1 for i = 1 is interpreted as 0. Therefore,
any of the two integrals in (6.8), (6.9) may replace the right-hand sides of (6.2)
or (6.3).

                                    6.2. Zagier’s identity
    Zagier’s formula shows that the multiple zeta values
                        ξ(m, n) = ζ({2}m , 3, {2}n ) for m, n ≥ 0,                        (6.10)
which are part of Hoffman’s basis in Conjecture 5.10, are Q-linear combinations
of products π 2µ ζ(2ν + 1) with µ + ν = m + n + 1.
    Before giving the formula for the numbers ξ(m, n), we first recall the much
easier formula from the family (4.4) (see Exercise 4.6(a)),
                                                   π 2n
                         ξ(n) = ζ({2}n ) =                      for n ≥ 0,                (6.11)
                                                (2n + 1)!
for the simplest of the Hoffman basis elements.
    Theorem 6.3 (Zagier). For all integers m, n ≥ 0, we have
                  m+n+1                                    
                   X
                           r−1          1       2r           2r
      ξ(m, n) = 2      (−1)       1 − 2r              −
                   r=1
                                       2     2m  + 1      2n + 2
                          × ξ(m + n − r + 1)ζ(2r + 1),                                    (6.12)
where the value of ξ(m+n−r +1) is given by (6.11). Conversely, each product
ξ(µ)ζ(k − 2µ) of odd weight k is a rational combination of numbers ξ(m, n)
with m + n = (k − 3)/2.
   Zagier’s original proof [48] is skillfully designed and worth studying on its
own. Other proofs can be found in [12, 26, 27] (see also [13]). Here we follow
an elementary proof given by L. Lai, C. Lupu and D. Orr in [25].
                                6.2. Zagier’s identity                              71

    Lemma 6.4. For nonnegative integers m and k the integral
                                2 π/2 (2z)2m
                                   Z
                         Im,k =               cos2k z dz
                                π 0    (2m)!
is evaluated as follows:
                                 2k
                                    
                                  k
                                      X            1
                         Im,k = 2k             2        2
                                                          ,
                                2 k >···>k >k k1 · · · km
                                         1       m

where the empty sum (when m = 0) is understood as 1.
    Proof. For m > 0 and k > 0, start with integration by parts
       2 π/2 (2z)2m
         Z
Im,k =                  cos2k−1 z d(sin z)
       π 0      (2m)!
         Z π/2 
                 (2z)2m                                  2(2z)2m−1
                                                                                     
       2                               2k−2        2                     2k−1
     =                     (2k − 1) cos     z sin z −                 cos     z sin z dz
       π 0        (2m)!                                   (2m − 1)!
                                     4 π/2 (2z)2m−1
                                       Z
     = (2k − 1)(Im,k−1 − Im,k ) +                          cos2k−1 z d(cos z)
                                    π 0       (2m − 1)!
implying
                                        Z π/2
                 2k − 1              2          (2z)2m−1
         Im,k =           Im,k−1 +                          cos2k−1 z d(cos z).
                    2k              πk 0       (2m − 1)!
Then
  2 π/2 (2z)2m−1
    Z
                      cos2k−1 z d(cos z)
  π 0     (2m − 1)!
          2 π/2 (2z)2m−1                                       2(2z)2m−2
            Z                                                                    
                                              2k−1                            2k
       =                        (2k − 1) cos        z sin z −              cos z dz
          π 0        (2m − 1)!                                 (2m − 2)!
                       2 π/2 (2z)2m−1
                          Z
       = −(2k − 1) ·                       cos2k−1 z d(cos z) − 2Im−1,k
                       π 0      (2m − 1)!
implying
               2 π/2 (2z)2m−1
                  Z
                                                               1
                                    cos2k−1 z d(cos z) = − Im−1,k .
               π 0       (2m − 1)!                             k
Thus
                                 2k − 1              1
                        Im,k =           Im,k−1 − 2 Im−1,k ,
                                   2k                k
which can be conveniently written as
                      22k          22k−2           22k Im−1,k
                       2k
                            Im,k =  2k−2
                                          Im,k−1 −  2k
                                                              ,
                                                         k2
                                                     
                        k           k−1             k

and the same recursion Sm,k = Sm,k−1 − Sm−1,k /k 2 is satisfied by the sums
                                   X          1
                        Sm,k =             2       2
                                          k · · · km
                               k >···>k >k 1
                                     1       m
                                  6.2. Zagier’s identity                               72

for m, k > 0. Therefore, the formula stated follows by induction on m + k with
the help of identities
                                                     2k
                                                        
                               2 π/2
                                 Z
                                         2k           k
                       I0,k =         cos z dz = 2k
                               π 0                  2
(see Exercise 1.3) and
                         Z π/2
                2m+1                            π 2m        X            1
        Im,0 =                   z 2m dz =             =             2        2
               π(2m)!     0                   (2m + 1)! k >···>k >0 k1 · · · km
                                                                 1      m

(see (6.11)).                                                                          □

   We also need the following special case of the hypergeometric function (see
Section 4.1).
   Exercise 6.4 ([40, eq. (1.5.7)]). The following identity is valid:
                      F 12 a, − 21 a; 21 ; sin2 z = cos az.
                                                 

   Comparing the coefficients of the expansion of the identity in powers of a
(and reverting the sides) we deduce the following formula.
   Lemma 6.5. For positive integers n,
                           ∞
                 z 2n   1 X (2 sin z)2k      X                           1
                      = 2n                                                         .
                       2 k=1 k 2 2k                                l2 · · · ln−1
                                                                             2
                                    
                (2n)!             k     k>l >···>l               ≥1 1
                                                   1       n−1

   For the next evaluation we introduce generalised Clausen’s functions
                       ∞
                         X sin nθ
                                    = Im Lis (eiθ ) for s even,
                       
                       
                               ns
                       
                       
                         n=1
              Cls (θ) = X ∞
                             cos nθ
                                    = Re Lis (eiθ ) for s odd.
                       
                       
                       
                       
                               n s
                         n=1

They satisfy differential equations
                   d Cls (θ)
                             = (−1)s Cls−1 (θ) for s = 2, 3, . . . .
                      dθ
   Exercise 6.5. (a) Give a closed form expression for Cl1 (θ) and show that
                                 d Cl1 (θ)    1   θ
                                           = − cot .
                                    dθ        2   2
(b) (Clausen) Prove that
                                         Z θ
                                                           t
                          Cl2 (θ) = −          log 2 sin     dt.
                                          0                2
                                  6.2. Zagier’s identity                                73

   Lemma 6.6 ([36, Theorem 2.1]). For a nonnegative integer n and real x,
       Z πx                      n                   
             n                n
                                X
                                        ⌊(k−1)/2⌋    n Clk+1 (2πx)
            z cot z dz = (πx)       (−1)          k!
        0                       k=0
                                                     k   (2πx)k
                                       (−1)n/2 n!
                                + δ⌊n/2⌋,n/2      ζ(n + 1),                         (6.13)
                                          2n
where δk,m stands for Kronecker’s delta.
   Proof. Denote the function on the right-hand side of (6.13) by g(x). Then
              n−1                    
 ′          n
              X
                       ⌊(k−1)/2⌋      n          Clk+1 (2πx)
g (x) = (πx)      (−1)           k!      (n − k)
              k=0
                                      k           x(2πx)k
                  n
                                        n (−1)k+1 2π Clk (2πx)
                X                      
              n           ⌊(k−1)/2⌋
        + (πx)      (−1)            k!                   k
                                                               + (πx)n π cot(πx)
                k=1
                                        k         (2πx)
      = π n+1 xn cot(πx)
and this clearly coincides with the derivative of the left-hand side in (6.13). In
addition,
                              Cln+1 (0)                (−1)n/2 n!
      g(0) = (−1)⌊(n−1)/2⌋ n!            + δ ⌊n/2⌋,n/2            ζ(n + 1) = 0.    □
                                 2n                        2n
   Lemma 6.7. For a nonnegative integer n,
Z π/2               π n         ⌊n/2⌋                                           
       n
                                    X
                                               k        2r               n ζ(2r + 1)
      z cot z dz =          log 2+       (−1) (2r)!(2 −1+δr,⌊n/2⌋ )                   .
 0                   2              r=1
                                                                        2r    (2π)2r
In particular, for a polynomial P (z) ∈ C[z] of degree d > 0 with P (0) = 0 we
have
 Z π/2                                 ⌊d/2⌋
                          π          X (−1)r                 
                                                   (2r) π       1
       P (z) cot z dz = P      log 2 +           P         1 − 2r ζ(2r + 1)
  0                        2            r=1
                                             22r        2      2
                                               ⌊d/2⌋
                                               X (−1)r
                                          +                  P (2r) (0)ζ(2r + 1).
                                               r=1
                                                       22r
    Proof. For the first identity, substitute x = π/2 in (6.13) and use Cl1 (π) =
− log 2, Cl2r+1 (π) = −(1 − 2−2r )ζ(2r + 1) and Cl2r (π) = 0 for r = 1, 2, . . . . For
the second identity, we only need to verify it for P (z) = z n where n = 1, 2, . . . ,
but this is precisely the first one.                                                □
   Exercise 6.6 (open problem). Give a direct proof of the formulae in
Lemma 6.7.
   Proof of Theorem 6.3. The proof compares two evaluations of the very
same integral
                        Z 1
            ˆ         2     (2 arccos x)2m+1 (2 arcsin x)2n+2 dx
            ξ(m, n) =                                            . (6.14)
                      π 0       (2m + 1)!        (2n + 2)!    x
                                  6.2. Zagier’s identity                                    74

   First use the identity of Lemma 6.5 for n shifted by 1 and z = arcsin x to
write
              ∞           Z 1
                               (2 arccos x)2m+1
                                                           
 ˆ         2X 1                                      2k dx
                                                              X              1
ξ(m, n) =            2k
                                                (2x)                     2
                                                                                     .
                                                        x k>l >···>l ≥1 l1 · · · ln2
                        
           π k=1 k k
                   2
                            0      (2m + 1)!
                                                                        1      n

Now observe that
    Z 1                            Z π/2
        (2 arccos x)2m+1 2k−1             (2z)2m+1
                        x     dx =                   cos2k−1 z sin z dz
     0      (2m + 1)!               0    (2m + 1)!
                                         Z π/2
                                      1         (2z)2m+1
                                 =−                       d(cos2k z)
                                     2k 0      (2m + 1)!
                                   1 π/2 (2z)2m
                                     Z
                                                                  π
                                 =                  cos2k z dz =     Im,k
                                   k 0      (2m)!                 2k
in the notation of Lemma 6.4, hence
             ∞
 ˆ
             X 1          X           1          X              1
 ξ(m, n) =         3              2         2               2         2
                                                                        = ζ({2}m , 3, {2}n ).
             k=1
                 k              k
                     k >···>k >k 1
                                    · · · k               l
                                           m k>l >···>l ≥1 1  · · · ln
                      1      m                  1      n

    On the other hand, taking z = arcsin x in the integral (6.14) and using
arcsin x + arccos x = π/2 for 0 ≤ x ≤ 1, we find out that
                    Z π/2
        ˆ         2       (π − 2z)2m+1 (2z)2n+2
       ξ(m, n) =                                 cot z dz
                  π 0       (2m + 1)! (2n + 2)!
                                      Z π/2 
                       22m+2n+4               π    2m+1
               =                                −z        z 2n+2 cot z dz.
                  π(2m + 1)! (2n + 2)! 0      2
For the polynomial P (z) = (π/2 − z)2m+1 z 2n+2 we get P (π/2) = 0 and
                                               
               (2r) π                2n + 2       π 2m+2n+3−2r
                    
             P          = −(2r)!                               ,
                      2           2r − 2m − 1 2
                                            
                 (2r)             2m + 1        π 2m+2n+3−2r
               P (0) = (2r)!
                                2r − 2n − 2 2
for r = 1, . . . , m + n + 1. Therefore, Lemma 6.7 implies
                                  m+n+1                                     
 ˆ                      2          X
                                              r−1           2n + 2            1
 ξ(m, n) =                               (−1) (2r)!                      1 − 2r
             (2m + 1)! (2n + 2)! r=1                     2r − 2m − 1         2
                                                    
                                            2m + 1
                                     −                  π 2m+2n+2−2r ζ(2r + 1),
                                          2r − 2n − 2
which after a simple manipulation with the factorials and the use of (6.11)
gives precisely the right-hand side of (6.12).                           □
    Exercise 6.7. Prove the second statement of the theorem (that is, the
invertibility of matrix Mk in (6.15)) by computing the 2-adic valuation of the
entries of the matrix.
            6.3. Double zeta values and products of single zeta values        75

    Remark. The second part of Theorem 6.3 (Exercise 6.7 above) gives rise
to several other open questions [48].
    The coefficients in the expressions for the products ξ(µ)ζ(k − 2µ) as linear
combinations of the numbers ξ(m, n) do not seem to be given by any simple
formula. For example, the inverse of the 5 × 5 matrix
                             3 − 15  189
                                         − 255   4603
                                                       
                                  2   16    16    256
                           0 − 15   315
                                         − 1753  9585 
                          
                                  2   8     16    64    
                                    157    889  10689
                                                        
                          0 0
                                     16
                                         − 16     128 
                                                        
                           0 2 −30 1985        − 11535
                                                       
                                           16       64 
                            −2 12 −30 56 − 17925   256

expressing the vector {ξ(m, n) : m + n = 4} in terms of the vector {ζ(2m +
3)ξ(n) : m + n = 4} is
                                                                    
               11072595 19354609 23488575 22114173 15331307
             59984880 122931470 160083660 147349978 89977320 
       1    
            246001728 508012288 669540272 613537008 369002592 ,
                                                                     
   2555171 494939520 1022542528 1349936640 1236102000 742409280
                                                                     
              300405248 620662272 819546624 750355968 450607872
in which no simple pattern can be discerned and in which even the denominator
(prime 2555171) cannot be recognised. This shows that the Hoffman basis,
although it works over Q, is very far from giving a basis over Z of Z-linear
span of MZVs, and suggests the question of finding better basis elements.
   The following question is supported by numerical data for m + n ≤ 30, but
remains open.
    Exercise 6.8 (open problem). Denote Mk the matrix from (6.12) express-
ing the vector {ξ(m, n) : m + n = k} in terms of the vector {ζ(2m + 3)ξ(n) :
m + n = k}, that is,
                                                  
               µ          1     2µ + 2         2µ + 2
 Mk = 2(−1)        1 − 2µ+2              −                            . (6.15)
                       2        2m + 1      2k − 2m + 2       0≤m,µ≤k

Show that all the entries of the inverse matrix Mk−1 are strictly positive.

     6.3. Double zeta values and products of single zeta values
    In this section we fix an odd number k = 2l + 1 ≥ 3 and discuss the rela-
tionship between the double zeta values ζ(m, n), the zeta products ζ(m)ζ(n),
and our latest heroes ξ(µ, ν), all of weight m + n = 2(µ + ν) + 3 = k.
    It was already found by Euler (explicitly for k up to 13) that all double
zeta values of odd weight are rational linear combinations of products of single
zeta values.
            6.3. Double zeta values and products of single zeta values          76

   Theorem 6.8. The double zeta value ζ(m, n) (with m ≥ 2 and n ≥ 1) of
weight m + n = k = 2l + 1 is given in terms of the products ζ(2s)ζ(k − 2s),
s = 0, 1, . . . , l − 1, by
                         l−1                                             
                       n
                         X      k − 2s − 1    k − 2s − 1                n
  ζ(m, n) = (−1)                           +              − δm,2s + (−1) δs,0
                         s=0
                                  m−1           n−1
                         × ζ(2s)ζ(k − 2s).                                  (6.16)
    Proof. The harmonic and shuffle products in the case of single zeta values
result in
     ζ(r)ζ(s) = ζ(r, s) + ζ(s, r) + ζ(k), where r + s = k, r, s ≥ 2,        (6.17)
                k−1                   
                X       m−1          m−1
     ζ(r)ζ(s) =                   +         ζ(m, k − m),                    (6.18)
                m=2
                         r−1          s−1
                          where r + s = k, r, s ≥ 2,
In both cases we can suppose without loss of generality that r ≤ s, since both
sides of the equations are symmetric in r and s. This will give us only 2(l − 1)
equations for the 2l − 1 unknowns ζ(m, k − m), 2 ≤ m ≤ k − 1. However, both
(6.17) and (6.18) remain true if we fix any value T (that is, any regularization)
for the divergent zeta value ζ(1) (here 0 or Euler’s constant γ would be natural
choices but we can also simply take T to be an indeterminate) and use one of
them to define the divergent double zeta value ζ(1, k − 1), so that this gives
2l−1 equations in 2l−1 unknowns. To solve them, we introduce the generating
functions
              X                                         X
  P (x, y) =      ζ(r)ζ(s)xr−1 y s−1 and Q(x, y) =            ζ(m, n)xm−1 y n−1 ,
             r,s≥1                                        m,n≥1
            r+s=k                                         m+n=k

with the convention ζ(1) = T and ζ(1, k − 1) = ζ(k − 1)T − ζ(k) − ζ(k − 1, 1).
Then the (double shuffle) relations (6.17) and (6.18) translate into equations
                                                  xk−1 − y k−1
                P (x, y) = Q(x, y) + Q(y, x) + ζ(k)
                                                     x−y
                        = Q(x, x + y) + Q(y, x + y).
Using Q(−x, −y) = −Q(x, y) (for k odd), allows us to solve for Q:
              Q(x, y) = R(x, y) + R(x − y, −y) + R(x − y, x),
                                                         xk−1 − y k−1
                                                                     
                         1
        where R(x, y) =      P (x, y) + P (−x, y) − ζ(k)                .
                         2                                  x−y
This is equivalent (because of ζ(0) = − 21 ) to (6.16).                         □
   Either of the double shuffle relations (6.17) and (6.18) permits us to express
the single zeta products ζ(2r)ζ(k − 2r) in terms of all double zeta values of
weight k, but we would like to do this using
            6.3. Double zeta values and products of single zeta values         77

    (a) only the ‘odd-even’ values ζ(k − 2r, 2r), where we also include ζ(k) to
         have the right number of quantities, or
    (b) only the ‘even-odd’ double zeta values ζ(k − 2r − 1, 2r + 1).
This turns out to be possible only in case (a), as we now show.
   Since in case (a) we have taken ζ(k) as one of the basis elements, we can
omit it from the basis and work modulo ζ(k) in the right-hand side of (6.16),
which simplifies to
                l−1                     
                X      2l − 2s      2l − 2s
ζ(k − 2r, 2r) ≡                 +              ζ(2s)ζ(k − 2s), 1 ≤ r ≤ l − 1,
                s=1
                       2l − 2r      2r − 1
                                                                         (6.19)
where the congruence is modulo Qζ(k).
   Theorem 6.9. For odd k = 2l + 1 ≥ 3, the products ζ(2s)ζ(k − 2s),
1 ≤ s ≤ l − 1, are expressible in terms of double zeta values ζ(k − 2r, 2r),
1 ≤ r ≤ l − 1.
    Proof. Let Nk be the (l − 1) × (l − 1) matrix whose (r, s)-entry is the
sum of binomials in (6.19). It is sufficient to show that the determinant of the
matrix is non-zero.
    Any binomial coefficient m
                                 
                               n
                                   with m even and n odd is even, because in
this case                                      
                               m        m m−1
                                    =              .
                               n        n n−1
Thus, the matrix Nk is congruent modulo 2 to a unipotent triangular matrix
and hence has odd determinant.                                                □
    Remark. The immediate consequence of Theorems 6.3 and 6.9 is the fol-
lowing result: For each odd k = 2l + 1 ≥ 3, the l numbers ζ(k) and ζ(k − 2r,
2r), 1 ≤ r ≤ l − 1, span the same space over Q as the l numbers
       {ξ(m, n) : m + n = l − 1}     or   {π 2r ζ(k − 2r) : 0 ≤ r ≤ l − 1}.
   Zagier made several experimental observations about the matrix Nk which
we give here as open problems.
    Exercise 6.9 (open problem). For k = 2l + 1 ≥ 3 and the matrix N = Nk
defined above, show the following:
     (a) det N = (−1)l 1 · 3 · 5 · · · (2l − 1); and
     (b) the entries of the inverse matrix N −1 are explicitly given by either of
         the two expressions
                      k−2s                            
      −1        −2 X k − 2r − 1                n + 2s − 2
  (N )s,r =                                                Bn
              2s − 1 n=0 k − 2s − n                n
                      k−2s                            
                 2 X           2r − 1          n + 2s − 2
            =                                              Bn , 1 ≤ s, r ≤ l − 1,
              2s − 1 n=0 k − 2s − n                n
        where Bn denotes the nth Bernoulli number (see Section 1.3).
                                       6.4. Hirose–Sato integrals                                        78

                                6.4. Hirose–Sato integrals
    One can cast the two-one formula (6.3) in the form
                                                           X          2#{n1 ,n2 ,...,nl }
    ζ ⋆ ({2}k1 , 1, {2}k2 , 1, . . . , {2}kl , 1) =                                              ,
                                                                n2k1 +1 n2k
                                               n1 ≥n2 ≥···≥nl ≥1 1       2
                                                                           2 +1
                                                                                 · · · n2kl
                                                                                            l +1

                                                                                               (6.20)
where k1 ≥ 1, k2 , . . . , kl ≥ 0 and #{n1 , n2 , . . . , nl } counts distinct elements in
{n1 , n2 , . . . , nl }. In fact, Zhao gives in [50] a general formula expressing any
multiple zeta star value ζ ⋆ (s) in terms of the zeta-star looking sums
                                           X                                       2#{n1 ,...,nl }
  ζ # (s) = ζ # (s1 , . . . , sl ) =               (−1)n1 (s1 −1)+···+nl (sl −1)                    . (6.21)
                                       n1 ≥···≥nl ≥1
                                                                                   ns11 · · · nsl l

More precisely, he show that there is a bijection σ on the set of admissible
indices such that
                                  ζ ⋆ (s) = ζ # (σs) for all s.                                     (6.22)
For the particular shape s = ({2}k1 , 1, {2}k2 , 1, . . . , {2}kl , 1) of an admissible
index one gets σs = (2k1 + 1, 2k2 + 1, . . . , 2kl + 1) implying the two-one for-
mula (6.20). The general description of the bijection σ in [50] is somewhat
sophisticated and requires introducing a lot of additional notation. In order to
gain a clear vision of σ we follow the generalisation of Zhao’s formula (6.22)
given by Hirose and Sato in [16].
    Given holomorphic 1-forms ϕ1 , . . . , ϕk on an open connected domain V ⊂
P and a path γ : [0, 1] → P1 such that γ(0, 1) ⊂ V , define
  1

                                           Z     Z
             Iγ (x; ϕ1 , . . . , ϕk ; y) =   ···   ϕ(γ(z1 )) · · · ϕ(γ(zk )),
                                              1>z1 >···>zk >0

where x = γ(1) and y = γ(0). We omit γ if it happens to be a straight line
connecting x with y. For z ∈ C, set
                                                         dt
                                             ez (t) =       .
                                                        t−z
In these settings,
                                                     1 −1       s     −1       l −1
     ζ ⋆ (s1 , . . . , sl ) = (−1)s1 +···+sl I(1; es−1               l−1
                                                          e1 · · · e−1   e1 es−1    (e1 − e−1 ); ∞).

To produce an integral expression for ζ # (s), we assign the sequence ε0 , ε1 , . . . , εl ∈
{±1} to the admissible index s = (s1 , . . . , sl ) by the rule
                  ε0 = 1 and εj = (−1)sj −1 εj−1                    for j = 1, . . . , l.
Then
                                                            s   −1
ζ # (s) = (−1)s1 +···+sl I(1; es01 −1 (2eε1 −e0 ) · · · e0l−1 (2eεl−1 −e0 )es0l −1 (2eεl −2e0 ); ∞).
                                 6.4. Hirose–Sato integrals                                   79

Let us first see how the two-one formula looks like, on a particular example
ζ ⋆ (2, 2, 1, 2, 1) = ζ # (5, 3):
                 I(1; e−1 e1 e−1 e1 e1 e−1 e1 (e1 − e−1 ); ∞)
                     = I(1; e0 e0 e0 e0 (2e1 − e0 ) e0 e0 (2e1 − 2e0 ); ∞).               (6.23)
In order to present the correspondence between the two expressions in a more
transparent form, introduce auxiliary differential 1-forms
        f1,−1 = f−1,1 = e0 ,        f1,1 = 2e1 − e0      and f−1,−1 = 2e−1 − e0 .
In this notation, the right-hand side of (6.23) can be stated as
             I(1; f1,−1 f−1,1 f1,−1 f−1,1 f1,1 f1,−1 f−1,1 (f1,1 − f1,−1 ); ∞),
where the rule we choose to switch between f1,−1 and f−1,1 (which both cor-
respond to the same e0 ) is to force alternation of 1 and −1 in all consecutive
indices, and we always start from f1,−1 . We are now ready to witness an
explicit form of Zhao’s idenity (6.22).
    Theorem 6.10 (Zhao’s relations). For any ε1 , . . . , εk , εk+1 ∈ {±1} with
ε1 ̸= 1, we have
        I(1; eε1 eε2 · · · eεk−1 (eεk − eεk+1 ); ∞)
            = I(1; f1,ε1 fε1 ,ε2 · · · fεk−2 ,εk−1 (fεk−1 ,εk − fεk−1 ,εk+1 ); ∞).        (6.24)
    Though Theorem 6.10 sounds general enough, its form suggests existence
of an even more general result. Suppose that we can find some differential
forms fˆz,w for any z, w ∈ C such that
  (i) fˆz,w = fz,w for z, w ∈ {±1}, and
 (ii) the identity
            I(1; ez1 ez2 · · · ezk−1 (ezk − ezk+1 ); ∞)
               = I(1; fˆ1,z fˆz ,z · · · fˆz ,z (fˆz
                            1   1   2      k−2   k−1    k−1 ,zk
                                                                  − fˆzk−1 ,zk+1 ); ∞).
     holds for any z1 , z2 , . . . , zk , zk+1 ∈ C with z1 ̸= 1 (to ensure the conver-
     gence of either side!).
The naive choice fˆz,w = 2e(z+w)/2 − e0 clearly meets condition (i) but it fails
to satisfy (ii).
    Exercise 6.10. Prove that the differential 1-form
                              √              √                du
           fˆz,w (u) = 2d log( u2 − 2zu + 1 − u2 − 2wu + 1) −
                                                               u
satisfy both (i) and (ii) above.
    With the differential form from Exercise 6.10 in mind, after the change of
variable t = (u + u−1 )/2, we can now give a general identity which implies
Theorem 6.10.
                                     6.4. Hirose–Sato integrals                                      80

   Theorem 6.11 (Hirose–Sato [16]). For k ≥ 0 and z0 , z1 , . . . , zk , zk+1 ∈ C
with z0 ̸= z1 and zk ̸= zk+1 , we have
        Iγ (z0 ; ez1 ez2 · · · ezk−1 (ezk − ezk+1 ); ∞)
            = Iγ (z0 ; gz0 ,z1 gz1 ,z2 · · · gzk−2 ,zk−1 (gzk−1 ,zk − gzk−1 ,zk+1 ); ∞),         (6.25)
where
                                           dt
                          gz,w (t) = p
                                      (t − z)(t − w)
and γ is a fixed path from z0 to ∞ avoding the singularities of the integrand.
    Sketch of proof. Denoting fk (z0 , z1 , . . . , zk , zk+1 ) either side of (6.25),
one routinely verifies that
                                    ∂                           1
                                        f1 (z0 , z1 , z2 ) =
                                  ∂z1                        z1 − z0
and
            ∂                                              1
               fk (z0 , z1 , . . . , zk , zk+1 ) =               fk−1 (z0 , z1 , . . . , zk ).
           ∂zk                                        zk − zk−1
Integrating we determine the constant by setting zk = zk+1 , in which case both
sides vanish.                                                                                  □
   The argument can be generalised even further by introducing, for complex
α with Re α > 0, the differential 1-forms
                          α                 dt
                        gz,w (t) =                    .
                                   (t − z) (t − w)1−α
                                          α

   Theorem 6.12 (Hirose–Sato [16]). For k ≥ 0 and z0 , z1 , . . . , zk , zk+1 ∈ C
with z0 ̸= z1 and zk ̸= zk+1 , the integral
                Iγ (z0 ; gzα0 ,z1 gzα1 ,z2 · · · gzαk−2 ,zk−1 (gzαk−1 ,zk − gzαk−1 ,zk+1 ); ∞)   (6.26)
does not depend on α.
    In particular, the choice α = 1 corresponds to the left-hand side of (6.25),
while α = 21 is for the right-hand side of (6.25). Thus, Theorem 6.11 follows
from Theorem 6.12.
    The most general form of the Hirose–Sato theorem is the following Selberg-
integral-type identity.
    Theorem 6.13 (Hirose–Sato [16]). Take
                                  α,β                       dt
                                 gz,w (t) =                                .
                                                (t − z)α (t − w)1−β
For k ≥ 0 and collections of complex (k + 2)-tuples z0 , . . . , zk+1 , α0 , . . . , αk+1
and β0 , . . . , βk+1 satisfying
   z0 ̸= z1 , zk ̸= zk+1 , Re α0 > 0, Re β0 > 0, Re αk+1 < 1, Re βk+1 < 1,
                α0 − β0 = α1 − β1 = · · · = αk − βk = αk+1 − βk+1 ,
                                         6.4. Hirose–Sato integrals                                                       81

the following identity is valid :
                                      α ,α                                                         β ,β
   Iγ (z0 ; gzα00,z,α11 gzα11,z,α22 · · · gzkk,zk+1
                                                 k+1
                                                     ; zk+1 )   Iγ (z0 ; gzβ00,z,β11 gzβ11,z,β22 · · · gzkk,zk+1
                                                                                                              k+1
                                                                                                                  ; zk+1 )
                              α0 ,αk+1                        =                            β0 ,βk+1
                                                                                                                           .
              Iγ (z0 ; gz0 ,zk+1 ; zk+1 )                                 Iγ (z0 ; gz0 ,zk+1 ; zk+1 )
                                                                                                                       (6.27)
   Choosing α0 = · · · = αk+1 = α → 0 and β0 = · · · = βk+1 = 21 in Theo-
rem 6.13 we recover Zagier’s formula from Section 6.2.
                                 CHAPTER 7

               q-Analogues of multiple zeta values

                             7.1. q-Zeta values
    The classical idea of introducing an additional parameter in an expression
or formula we wish to deal with, is quite fruitful in many situations. This
may significantly simplify a proof of the corresponding identity or lead to
a more general identity which have several other useful specializations of the
parameter introduced. We have already witnessed a usefulness of this approach
on examples of functional models of generalised polylogarithms in Section 3.2
and of multiple harmonic sums in Section 3.4. These were used for proving
the shuffle and stuffle relations of MZVs, respectively. Because the functional
versions satisfy only ‘half’ of relations of MZVs, we can hardly use either of
them as a parametric version of the latter numbers.
    There is a different way of introducing a parameter. The story usually
refers to the parameter q (from ‘quantum’, whatever it means) and often has a
different flavour. The basic idea is simply replacing a number n (not necessarily
an integer!) by the function [n] = [n]q = (1 − q n )/(1 − q); this is, of course,
nothing else but a polynomial for positive n ∈ Z. The actual motivation of
the replacement has clear analytical grounds:

                                  lim [n]q = n,
                                  q→1
                                 0<q<1

so that the (sometimes formal) limit as q → 1 produces back the original
quantities. Note however that this is only a part of the recipe, as multiplying
the ‘q-number’ [n]q by any power of q makes exactly the same job as q → 1.
Getting the right exponents of q is an art.

   Exercise 7.1. For integers m ≥ n ≥ 0, define the q-binomial coefficients
           
         m       m           [m]!
             =        =             , where [n]! = [1] [2] · · · [n].
          n      n q [n]! [m − n]!

Show that all are polynomials in q with integer nonnegative coeffcients. These
are also known by the name Gaussian (binomial) polynomials in the literature.

   Hint. Show first the q-analogue
                                        
                        m      n m−1    m−1
                            =q        +
                        n          n     n−1
                                         82
                                            7.1. q-Zeta values                                              83

of Pascal identities, or the q-binomial theorem
                        m               m             
                                             n(n+1)/2 m
                       Y               X
                                 k
                           (1 + q z) =     q            zn.                                                 □
                       k=1             n=0
                                                      n
    Before going into details of q-generalization of multiple zeta values, let us
examine the zeta values — MZVs of length 1. For this purpose, we introduce
an ‘arithmetically motivated’ q-model of ζ(s), namely,
                              ∞                        ∞
                              X
                                                  n
                                                       X ns−1 q n
                  ζ̃q (s) =         σs−1 (n)q =                         ,    s = 1, 2, . . . ,           (7.1)
                              n=1                       n=1
                                                               1 − qn
where σs−1 (n) = d|n ds−1 denotes the sum of powers of the divisors. Here
                    P
are the first few instances:
               ∞                       ∞                           ∞
              X     qn                X      qn                   X   q n (1 + q n )
    ζ̃q (1) =           n
                          , ζ̃q (2) =            n )2
                                                      , ζ̃q (3) =              n )3
                                                                                     ,
              n=1
                  1 − q               n=1
                                          (1 − q                  n=1
                                                                       (1  − q
               ∞                                                  ∞
               X q n (1 + 4q n + q 2n )                           X q n (1 + 11q n + 11q 2n + q 3n )
   ζ̃q (4) =                                  ,       ζ̃q (5) =
               n=1
                          (1 − q n )4                             n=1
                                                                                   (1 − q n )5
and, in general,
                                      ∞
                                      X q n ρk (q n )
                          ζ̃q (k) =                        ,      k = 1, 2, 3, . . . ,
                                      n=1
                                            (1 − q n )k
where the polynomials ρk (x) ∈ Z[x] are determined recursively by the formulae
       ρ1 = 1,        ρk+1 = (1 + (k − 1)x)ρk + x(1 − x)ρ′k                      for k = 1, 2, . . . .
The latter imply ρk+1 (1) = k! that results in the limiting relations
                     lim (1 − q)s ζ̃q (s) = (s − 1)! · ζ(s),                s = 2, 3, . . . .
                   q→1
                  0<q<1

    If s ≥ 2 is even, then the series Es (q) = 1−2sζq (s)/Bs , where the Bernoulli
numbers Bs ∈ Q are defined in Section 1.3, are known as the Eisenstein se-
ries. In particular, they are examples of (quasi-)modular forms whose struc-
tural properties are well studied. This circumstance allows one to prove the
coincidence of the rings
    Q[q, ζ̃q (2), ζ̃q (4), ζ̃q (6), ζ̃q (8), ζ̃q (10), . . . ] and Q[q, ζ̃q (2), ζ̃q (4), ζ̃q (6)];
the fact can be viewed as a q-analogue of the coincidence of the numerical rings
               Q[ζ(2), ζ(4), ζ(6), ζ(8), ζ(10), . . . ] and Q[ζ(2)] = Q[π 2 ]
which we established in Corollary 1.9. Even more, the ring Q[q, ζ̃q (2), ζ̃q (4), ζ̃q (6)]
is differentially stable because of Ramanujan’s system of differential equations
           1                       1                     1
   δE2 = (E22 − E4 ), δE4 = (E2 E4 − E6 ), δE6 = (E2 E6 − E42 ), (7.2)
          12                       3                     2
                          d
where, as before, δ = q dq .
                                     7.2. q-Models of MZVs                                     84

      Exercise 7.2 (Bailey [4, 54]). Show that
                                 X              q n1
                     ζ̃q (3) =                n1 )2 (1 − q n2 )
                                                                .
                               n ≥n ≥1
                                       (1 − q
                                      1   2

    Multiplying both sides of this identity by (1 − q)3 and letting q → 1, again
recover Euler’s identity (1.13).

                                7.2. q-Models of MZVs
     The main requirement from a q-model of MZVs (or MZSVs) is a better
understanding of the structure of linear and algebraic relations between the
corresponding numbers. An important advantage of the q-model is that prov-
ing the absence of such relations and guessing their existence are usually a
much easier task: for example, the linear independence of any version of q-
MZVs (and much more) is known, while just the irrationality of odd single
zeta values seems to be hard. On the other hand, showing that some relations
hold is normally easier for numbers than for functions. The main problem here
is finding an appropriate q-analogue which is often dictated by already existing
proofs of the corresponding original identities.
     An unfortunate thing about MZVs is that there is no uniform q-generaliza-
tion of the multiple zeta (star) values. Having however several q-analogues in
mind and a simple way to pass from one q-model to another gives one a very
natural parallel between the numbers and their q-analogues.
     There are very good reasons to believe that the most perfect q-extension
of MZVs is given by
                                          X         q n1 (s1 −1)+n2 (s2 −1)+···+nl (sl −1)
        ζq (s1 , s2 , . . . , sl ) =                              s1 [n ]s2 · · · [n ]sl
                                                                                           , (7.3)
                                     n >n >···>n ≥1
                                                          [n  1 ]      2            l
                                 1    2       l

where conditions on the multi-index s = (s1 , . . . , sl ) are exactly the same as
for the MZVs (2.1) (that is, the multi-index is admissible). The corresponding
q-analogues of the values of Riemann’s zeta function are in this case as follows:
                                       X q n(s−1)
                              ζq (s) =         s
                                                  .
                                       n≥1
                                           [n]

The q-model (7.3) inherits many relations available for MZVs ζ(s). There is
a version of stuffle relations, which is based on the identity from the following
exercise.
      Exercise 7.3. (a) Show that
                 q n(s−1) q m(r−1)              q n(s+r−2) q n(s+r−1)
                                      = (1 − q)           +           .
                   [n]sq    [m]rq m=n           [n]s+r−1
                                                    q        [n]s+r
                                                                q

    (b) One may also interpret ζq as a linear evaluation map on the Q-algebra
  0
H generated by admissible words over the alphabet {y1 , y2 , . . . } (as in Sec-
tion 3.1). Use part (a) to define the harmonic (stuffle) product ∗q on the
                                 7.2. q-Models of MZVs                           85

algebra H1 in such a way that
                ζq (w1 ∗q w2 ) = ζq (w1 )ζq (w2 ) for words w1 , w2 ∈ H0 .
    There is however no reasonably nice version of shuffle relations. The follow-
ing result of Okuda and Takeyama [34], which includes numerous implications,
is a convincing argument to count the q-MZVs (7.3) appropriate enough. Re-
call that the height m = m(s) of a multi-index s = (s1 , . . . , sl ) is the number
of components satisfying sj > 1, so that m(s) ≥ 1 for an admissible indices
s. Denote the set of admissible multi-indices of fixed weight w = |s|, length
l = ℓ(s) and height m = m(s) by I(w, l, m), and set
                             ∞
                             X                        X
              Φq (x, y, z) =    xw−l−m y l−m z 2m−2           ζq (s).
                              w,l,m=0                     s∈I(w,l,m)

   Theorem 7.1. The generating function Φq is given by
                             ∞
       2
                            Y   ([n]q − αq n )([n]q − βq n )
 1 + (z − xy)Φq (x, y, z) =
                            n=1
                                ([n]q − xq n )([n]q − yq n )
                                   ∞                          k
                                      xk + y k − α k − β k X
                                X                                             
                                                                        k−j
                          = exp                                  (q − 1) ζq (j) ,
                                  k=2
                                                k            j=2
                                                                             (7.4)
where α and β are determined by
                   α + β = x + y + (q − 1)(z 2 − xy),        αβ = z 2 .
In particular, the sum of the multiple q-zeta values of fixed weight, length and
height is a polynomial in q and single q-zeta values.
   The limiting case q → 1 is Theorem 4.6 of Ohno and Zagier given in
Section 4.3.
   Corollary 1. We have the generating function identity
    X∞
       xs+1 y r+1 ζq (s + 2, {1}r )
     s,r=0
                    ∞                                   k
                       xk + y k − (x + y + (1 − q)xy)k X
                  X                                                     
                                                                  k−j
             = exp                                         (q − 1) ζq (j) .
                   k=2
                                      k                j=2

In particular, because of the symmetry in x and y,
                          ζq (s + 2, {1}r ) = ζq (r + 2, {1}s ).
   Proof. The identity follows by taking z = 0 in (7.4).                         □
    Corollary 2 (Sum theorem). The sum of all admissible multiple q-zeta
values of fixed weight w and fixed length is equal to ζq (w),
                               X
                                       ζq (s) = ζq (w).
                              s:|s|=w, ℓ(s)=l
                                             7.2. q-Models of MZVs                                         86

    Proof. This derivation is more subtle. Taking the limit as z 2 → xy
in (7.4) gives
                                    ∞
                   √                X             qr
       Φq (x, y, xy) =
                                  r=1
                                      ([r]q − xq r )([r]q − yq r )
                                   ∞                  −1              −1
                                       qr        xq r              yq r
                                  X         
                                =             1−            1−
                                  r=1
                                      [r]2q      [r]q              [r]q
                                    ∞
                                    X                                       X
                                =           xm y n ζq (m + n + 2) =                 xw−l−1 y l−1 ζq (w).
                                    m,n=0                                   w>l≥1

On the other hand, it follows directly from definition that
                                                ∞
                            √      X                                        X
                   Φq (x, y, xy) =   xw−l−1 y l−1                                      ζq (s).
                                               w,l=0                s:|s|=w, ℓ(s)=l
                                                                              √
It remains to compare the coefficients in the two representations of Φq (x, y, xy).
                                                                                □
    Exercise 7.4. For an indeterminate t, show
                                      l                    ∞
                        X     q n1 Y            1         X            q ln
                                                     nj
                                                        =         l ([n] − tq n )
                                                                                  .
                 n >···>n ≥1
                             [n 1 ]q j=1
                                         [nj ]q − tq      n=1
                                                              [n] q     q
                  1         l

    Hint. This is equivalent to the sum theorem in Corollary 2.                                            □

    The q-model (7.3) also fits the q-version of Theorem 5.1.
    Theorem 7.2 (q-analogue of Ohno’s relations [7, 39]). Given a non-
negative integer m, for an admissible index s = (s1 , . . . , sl ) and its dual
s′ = (s′1 , . . . , s′k ) (in the sense of Section 3.3), we have the identity
           X                                              X
                        ζq (s1 + i1 , . . . , sl + il ) =   ζq (s′1 + i1 , . . . , s′k + ik ).
        i1 ,...,il ≥0                                       i1 ,...,ik ≥0
      i1 +···+il =m                                       i1 +···+ik =m

    Exercise 7.5. Prove Theorem 7.2.
    Hint. Replace the Seki–Yamamoto ‘connected’ sums (5.1) by their q-an-
alogues using the rules
                                          1               q n(s−1)
                                                 7→
                                    ns−1 (n − t)    [n]s−1         n
                                                       q ([n]q − tq )

and
                                                         Qn             j
                                                                             Qm             j
                                                    nm    j=1 ([j]q − tq ) ·  j=1 ([j]q − tq )
       C(n, m; t) 7→ Cq (n, m; t) = q                             Qn+m             j
                                                                                               .           □
                                                                    j=1 ([j]q − tq )
                                       7.2. q-Models of MZVs                                          87

    In spite of the above naturalness of the q-MZVs (7.3), there exist other
variations, and we indicate more in what follows. The main difficulty of all
these q-models occurs when we look for a reasonable q-generalization of the
shuffle product from Theorem 3.1, the product originated from the differential
equations for the multiple polylogarithms (3.9). Lemma 3.5 tells us that
                                           1
                                         
                d                         Lis1 −1,s2 ,...,sl (z) if s1 ≥ 2,
                                         
                   Lis1 ,s2 ,...,sl (z) = z 1                                (7.5)
               dz                        
                                               Lis2 ,...,sl (z) if s1 = 1,
                                           1−z
and this comes from the fundamental theorem of calculus,
                   d               d                         d
                     f (z)g(z) =      f (z) · g(z) + f (z) · g(z).                  (7.6)
                  dz               dz                        dz
The differential equations (7.5) give rise to an integral representation of the
polylogarithms (3.9) (hence, of the multiple zeta values), where the participat-
ing differential forms dz/z and dz/(1−z) are assigned as two non-commutative
letters, so that the integrals themselves are interpreted as words on these let-
ters.
    The q-analogue of (7.6) reads as
               
  Dq f (z)g(z) = Dq f (z) · g(z) + f (z) · Dq g(z) − (1 − q)z · Dq f (z) · Dq g(z), (7.7)
where
                                                    f (z) − f (qz)
                                      Dq f (z) =                   .
                                                       (1 − q)z
Defining a q-analogue of the multiple polylogarithms (3.9) as
                                            X                z n1
                   Lis1 ,...,sl (z; q) =                   s1 · · · [n ]sl
                                                                           ,                       (7.8)
                                         n >···>n ≥1
                                                     [n1 ]            l
                                                1       l

from (7.7) we deduce the following analogue of (7.5):
                                          1
                                        
                                         Lis1 −1,s2 ,...,sl (z; q) if s1 ≥ 2,
                                        
            Dq Lis1 ,s2 ,...,sl (z; q) = z 1
                                        
                                              Lis2 ,...,sl (z; q) if s1 = 1.
                                          1−z
This q-model of the multiple polylogarithms, together with classical formulae
in the theory of basic hypergeometric series (which we ‘touch’ below), were
used in the derivation of Theorem 7.1 by Okuda and Takeyama [34]. This
is a reason to believe that the q-multiple polylogarithms (7.8) are ‘motivated’
q-analogues of (3.9), and that their values at z = q,
   zq (s1 , s2 , . . . , sl ) = (1 − q)−|s| Lis1 ,s2 ,...,sl (q; q)
                                     X                              q n1
                              =                                                                ,   (7.9)
                                n >n >···>n ≥1
                                               (1 − q n1 )s1 (1 − q n2 )s2 · · · (1 − q nl )sl
                              1   2       l
                                7.2. q-Models of MZVs                                   88

are reasonable q-analogues of multiple zeta values. Note the normalization
factor (1 − q)−|s| in the latter specialization; it makes many formulae for q-
MZVs ‘cleaner’ and could be also used for the q-model (7.3).
    Although the rule (7.7) might be interpreted as a shuffle product of a suit-
able functional q-model of the multiple polylogarithms and the corresponding
q-MZVs, these models are different from and even ‘incompatible’ with already
given models. For example, the q-analogue of the formula

                                Li1 (z)r = r! Li{1}r (z)

(cf. Exercise 3.12 (a)) in terms of (7.8) involve certain undesired ‘parasites’: if
r = 2, from
                               1                           1               z
  Dq Li1 (z; q) Li1 (z; q) =       Li1 (z; q) + Li1 (z; q)     − (1 − q)
                               1−z                         1−z           (1 − z)2
we have
                                                        ∞
                         2
                                                        X (n − 1)z n
                Li1 (z; q) = 2 Li1,1 (z; q) − (1 − q)                  ,
                                                        n=1
                                                              [n]

where the latter series cannot be expressed by means of (7.8).
   A related problem is a q-generalization of Euler’s decomposition formula
            r−1                      s−1      
            X     s−1+i                X    r−1+i
 ζ(r)ζ(s) =              ζ(s+i, r −i)+             ζ(r +i, s−i) (7.10)
            i=0
                    i                  i=0
                                              i

(which follows from the double shuffle relations (6.17), (6.18)), since the known
proofs make use (explicitly or not) of the shuffle relations. It seems that a way
to overcome this difficulty is to extend the algebra of q-MZVs differentially,
that is, to consider a differential algebra of q-MZVs and all their δ-derivatives
                                  d
of arbitrary order, where δ = q dq  . Although it is hard to justify this claim, let
us see how the problem may be fixed on the example of a q-analogue of (7.10)
when r = s = 2,
                             ζ(2)2 = 2ζ(2, 2) + 4ζ(3, 1),                       (7.11)
by means of (7.9). As Bradley shows, even this particular case involves some-
thing, which is not expressible by means of q-MZVs (7.3).
    We start with the partial-fraction identity
        1         1                                                     1+x
                 = f (x, y) + f (y, x) ,        where f (x, y) =                    ,
  (1 − x)(1 − y)  2                                                 (1 − x)(1 − xy)
and differentiate both sides with respect to x and y,
∂f (x, y)            2               4               4          1 + xy
          =                   +               −               −        .
 ∂x ∂y      (1 − x) (1 − xy) (1 − x)(1 − xy) (1 − x)(1 − xy) (1 − xy)3
                   2        2               3               2
                                    7.3. Multiple q-zeta brackets                                             89

Multiplying the result by xy, substituting x = q n and y = q m , and using
            ∞                                        ∞
            X xy(1 + xy)                            X           q l (1 + q l )
                                                  =     (l − 1)
           n,m=1
                   (1 − xy)3        x=q n , y=q m   l=1
                                                                (1 − q l )3
                   ∞                   ∞
                   X       ql         X   q l (1 + q l )
              =δ               l )2
                                    −               l )3
                                                         = δzq (2) − 2zq (3) + zq (2),
                    l=1
                        (1 − q        l=1
                                          (1   −  q
we finally arrive at
        zq (2)2 + δzq (2) = 2zq (2, 2) + 4zq (3, 1) − 4zq (2, 1) + 2zq (3) − zq (2),
which is the desired q-analogue of (7.11).
    One can also use Ramanujan’s system of differential equations (7.2) to get
rid of the term δzq (2). Namely, using
                         δzq (2) = zq (2) − 5zq (3) + 5zq (4) − 2zq (2)2
we obtain
      zq (2)2 = −2zq (2, 2) − 4zq (3, 1) + 4zq (2, 1) + 5zq (4) − 7zq (3) + 2zq (2),
which is also a q-analogue of (7.11). But for a general q-analogue of (7.10) we
do expect terms involving δzq (s) and δzq (t), hence working in the δ-differential
algebra generated by the multiple q-zeta values (7.9). Is there a nice form of
double shuffle relations in this differential algebra?

                               7.3. Multiple q-zeta brackets
    Apart from standard q-model of the multiple zeta values (7.3) and (7.9)
discussed above, there is a somewhat different version introduced recently by
Bachmann (partly in collaboration with Kühn):
                                    1                 X
    [s1 , . . . , sl ] =                                      ds1 −1 · · · dsl l −1 q n1 d1 +···+nl dl
                         (s1 − 1)! · · · (sl − 1)! n >···>n >0 1
                                                       1         l
                                                       d1 ,...,dl >0
                                  1
                   =
                       (s1 − 1)! · · · (sl − 1)!
                            X
                       ×             ds11 −1 · · · dsl l −1 q (m1 +···+ml )d1 +(m2 +···+ml )d2 +···+ml dl .
                          m1 ,...,ml >0
                          d1 ,...,dl >0
                                                                                                       (7.12)
The series are generating functions of multiple divisor sums, called (mono-)
brackets, with the Q-algebra spanned by them denoted by MD. These clearly
include the single q-zeta values (7.1) from Section 7.1. Note that the q-series
(7.12) can be alternatively written
                                     1                 X           ρ̂s1 (q n1 ) · · · ρ̂sl (q nl )
     [s1 , . . . , sl ] =                                                                          ,
                          (s1 − 1)! · · · (sl − 1)! n >···>n >0 (1 − q n1 )s1 · · · (1 − q nl )sl
                                                           1         l
                                  7.3. Multiple q-zeta brackets                                            90

where ρ̂s (x) = xρs (x) are (essentially) the polynomials from Section 7.1:
                                               s−1        ∞
                       ρ̂s (x)                d       x    X
                               =           x             =     ds−1 xd .
                      (1 − x)s               dx      1−x   d=1

Since ρ̂s (1) = ρs (1) = (s − 1)! , we have

                      lim (1 − q)s1 +···+sl [s1 , . . . , sl ] = ζ(s1 , . . . , sl ).                  (7.13)
                     q→1−

   In addition to (7.12), Bachmann introduced a more general model of the
brackets
                            
            s1 , . . . , s l                     1
                               =
             r1 , . . . , rl     r1 ! (s1 − 1)! · · · rl ! (sl − 1)!
                                        X
                                 ×              nr11 ds11 −1 · · · nrl l dsl l −1 q n1 d1 +···+nl dl
                                    n1 >···>nl >0
                                     d1 ,...,dl >0
                                                 1
                             =
                                 r1 ! (s1 − 1)! · · · rl ! (sl − 1)!
                                        X       nr11 ρ̂s1 (q n1 ) · · · nrl l ρ̂sl (q nl )
                                 ×                                                         ,           (7.14)
                                   n >···>n >0
                                                (1 − q n1 )s1 · · · (1 − q nl )sl
                                      1        l

which he called bi-brackets, in order to describe, in a natural way, the dou-
ble shuffle relations of these q-analogues of MZVs. Note that the stuffle (or
harmonic) product for both models (7.12) and (7.14) in Bachmann’s work
comes from the standard rearrangement of the multiple sums obtained from
the term-by-term multiplication of two series. The other shuffle product is
then interpreted for the model (7.14) only, as a dual product to the stuffle one
via a partition duality. Bachmann further conjectures that the Q-algebra BD
spanned by the bi-brackets (7.14) coincides with the Q-algebra MD.
    The goal of this section is to make an algebraic setup for Bachmann’s
double stuffle relations as well as to demonstrate that those relations indeed
reduce to the corresponding stuffle and shuffle relations in the limit as q → 1− .
We also briefly address the reduction of the bi-brackets to the mono-brackets.
    The following result allows one to control the asymptotic behaviour of the
bi-brackets not only as q → 1− but also as q approaches radially a root of
unity.

   Exercise 7.6. As q = 1 − ε → 1− ,

           1      ρ̂s (q n )     1
                               = s s (1 − ε)Fs−1 (ε) + λ̂s · εs − λ̂s + O(ε)
                                                               
        (s − 1)! (1 − q ) n  s  nε
                                   7.3. Multiple q-zeta brackets                              91

where the polynomials Fk (ε) ∈ Q[ε] of degree max{0, k − 1} are generated by
            ∞
            X                       1
                  Fk (ε)xk =
            k=0
                            1 − (1 − e−εx )/ε
                                                                
                                        1         2     1 2
                           =1+x+ − ε+1 x +                ε − ε + 1 x3
                                        2               6
                                                          
                                     1 3      7 2 3
                              + − ε + ε − ε + 1 x4
                                    24       12     2
                                                              
                                   1 4 1 3 5 2
                              +       ε − ε + ε − 2ε + 1 x5 + · · ·
                                  120       4     4
and
                    ∞                             ∞
                    X
                               s    xex      1   X    B2k 2k
                         λ̂s x = −      x
                                          =1+ x+           x
                     s=0
                                   1−e       2   k=1
                                                     (2k)!
is the (modified) generating function of the Bernoulli numbers.

    By moving the constant term λ̂s to the right-hand side, we get
          1 ρ̂1 (q n )
                                     
                         1     −1   1
            +           = · ε −         + O(ε),
          2 1 − qn       n          2
             ρ̂2 (q n )
                                              
        1                 1     −2    −1    1
          +             = 2 · ε −ε +             + O(ε),
       12 (1 − q n )2    n                 12
             ρ̂3 (q n )
                                                 
                          1     −3   3 −2 1 −1
                        = 3· ε − ε + ε              + O(ε),
            (1 − q n )3  n           2       2
             ρ̂4 (q n )
                                                               
       1                  1     −4     −3    7 −2 1 −1       1
    −     +             = 4 · ε − 2ε + ε − ε −                    + O(ε),
      720 (1 − q n )4    n                   6      6       720
and so on.
    Proposition 7.3. Assume that s1 > r1 +1 and sj ≥ rj +1 for j = 2, . . . , l.
Then
                   
   s1 , . . . , s l     ζ(s1 − r1 , s2 − r2 , . . . , sl − rl )         1
                      ∼                                                               as q → 1− ,
   r1 , . . . , r l              r1 ! r2 ! · · · rl !           (1 − q)s1 +s2 +···+sl
where ζ(s1 , . . . , sl ) denotes the standard MZV.
   Another way to tackle the asymptotic behaviour of the (bi-)brackets is
based on the Mellin transform
                                    Z ∞
                       φ(t) 7→ φ(s)
                               e =      φ(t)ts−1 dt
                                                     0

which maps
                                                            Γ(s)
                      q n1 d1 +···+nl dl q=e−t 7→                             .
                                                    (n1 d1 + · · · + nl dl )s
                               7.3. Multiple q-zeta brackets                               92

Note that the bijective correspondence between the bi-brackets and the zeta
functions
                       Γ(s)                      X        nr11 ds11 −1 · · · nrl l dsl l −1
          r1 ! (s1 − 1)! · · · rl ! (sl − 1)! n >···>n >0 (n1 d1 + · · · + nl dl )s
                                                 1         l
                                                 d1 ,...,dl >0

can be potentially used for determining the linear relations of the former. A
simple illustration is the linear independence of the length 1 bi-brackets.
   Theorem 7.4. The bi-brackets sr11 , where 0 ≤ r1 < s1 ≤ n, s1 + r1 ≤
                                       

n, are linearly independent over Q. Therefore, the dimension dBD   n  of the Q-
space spanned by all bi-brackets of weight at most n is bounded from below by
⌊(n + 1)2 /4⌋ ≥ n(n + 2)/4.
    Proof. Indeed, the functions
            Γ(s)      X nr1 ds1 −1                             ζ(s − s1 + 1)ζ(s − r1 )
                                       1   1
                                               s
                                                 = Γ(s)                                ,
            r1 ! (s1 − 1)! n ,d >0 (n1 d1 )                         (s1 − 1)! r1 !
                           1   1

                        where 0 ≤ r1 < s1 ≤ n, s1 + r1 ≤ n,
are linearly independent over Q (because of their disjoint sets of poles
                                                                       s1at
                                                                           s = s1
and s = r1 + 1, respectively); thus the corresponding bi-brackets r1 are Q-
linearly independent as well.                                                   □
    A similar (though more involved) analysis can be applied to describe the
Mellin transform of the length 2 bi-brackets; note that it is more easily done
for another q-model we introduce below.
    Consider now the alphabet Z = {zs,r : s, r = 1, 2, . . . } on the double-
indexed letters zs,r of the pre-defined weight s + r − 1. On QZ define the
product
                                   
                        r1 + r2 − 2
  zs1 ,r1 ⋄ zs2 ,r2 =                   zs1 +s2 ,r1 +r2 −1
                           r1 − 1
                            s1                            
                                   s2 −1 s1 + s2 − j − 1
                           X
                        +      (−1)                         λs1 +s2 −j zj,r1 +r2 −1
                           j=1
                                                  s 1 −  j
                            s2                                                    
                                   s1 −1 s1 + s2 − j − 1
                           X
                        +      (−1)                         λs1 +s2 −j zj,r1 +r2 −1 , (7.15)
                           j=1
                                                  s 2 −  j
where
                        ∞                       ∞
                        X
                                   s   x       X   Bs s
                             λs x = −    x
                                           =1+        x
                         s=0
                                      1−e      s=1
                                                   s!
is the generating function of Bernoulli numbers. Note that λ̂s = λs for s ≥ 2,
while λ̂1 = 12 = −λ1 in the notation of Exercise 7.6.
    Exercise 7.7. Show that the the product ⋄ is (associative and) commu-
tative.
                                     7.3. Multiple q-zeta brackets                           93

   With the help of (7.15) define the stuffle product on the Q-algebra Q⟨Z⟩
                    
recursively by 1 w = w 1 = w and     
                aw          bv = a(w       bv) + b(aw      v) + (a ⋄ b)(w      v),   (7.16)
for arbitrary w, v ∈ Q⟨Z⟩ and a, b ∈ Z.
   Proposition 7.5. The evaluation map
                                                                       
                                                      s1 , . . . , s l
               [ · ] : zs1 ,r1 · · · zsl ,rl 7→                                          (7.17)
                                                  r1 − 1, . . . , rl − 1
                                                      
extended to Q⟨Z⟩ by linearity satisfies [w v] = [w] · [v], so that it is a homo-
                                                
morphism of the Q-algebra (Q⟨Z⟩, ) onto (BD, · ), the latter hence being a
Q-algebra as well.
   Proof. The proof is based on the identity
             nr1 −1 ρ̂s1 (q n )                  nr2 −1 ρ̂s2 (q n )
                                          ·
     (s1 − 1)! (r1 − 1)! (1 − q n )s1 (s2 − 1)! (r2 − 1)! (1 − q n )s2
                                  nr1 +r2 −2              ρ̂s1 +s2 (q n )
                                             
            r1 + r2 − 2
        =
               r1 − 1          (r1 + r2 − 2)! (s1 + s2 − 1)! (1 − q n )s1 +s2
                 s1
                                                                          ρ̂j (q n )
                                                 
                            s2 −1 s1 + s2 − j − 1
                X
            +       (−1)                            λs1 +s2 −j
                j=1
                                         s1 − j                  (j − 1)! (1 − q n )j
                 s2
                                                                          ρ̂j (q n )
                                                                                    
                            s1 −1 s1 + s2 − j − 1
                X
            +       (−1)                            λs1 +s2 −j                         .     □
                j=1
                                         s2 − j                  (j − 1)! (1 − q n )j

   Modulo the highest weight, the commutative product (7.15) on Z assumes
the form                                       
                                     r1 + r2 − 2
                zs1 ,r1 ⋄ zs2 ,r2 ≡               zs1 +s2 ,r1 +r2 −1 ,
                                        r1 − 1
so that the stuffle product (7.16) reads
        zs1 ,r1 w                                                         
                        zs2 ,r2 v ≡ zs1 ,r1 (w zs2 ,r2 v) + zs2 ,r2 (zs1 ,r1 w v)
                                                        
                                             r1 + r2 − 2                   
                                      +                    zs1 +s2 ,r1 +r2 −1 (w v)      (7.18)
                                                r1 − 1
for arbitrary w, v ∈ Q⟨Z⟩ and zs1 ,r1 , zs2 ,r2 ∈ Z. If we set zs = zs,1 and further
restrict the product to the subalgebra Q⟨Z ′ ⟩, where Z ′ = {zs : s = 1, 2, . . . },
then Proposition 7.3 results in the following statement.
   Theorem 7.6. For admissible words w = zs1 · · · zsl and v = zs′1 · · · zs′m of
weight |w| = s1 + · · · + sl and |v| = s′1 + · · · + s′m , respectively,
                        [w      v] ∼ (1 − q)−|w|−|v| ζ(w ∗ v)     as q → 1− ,
where ∗ denotes the standard stuffle (harmonic) product of MZVs on Q⟨Z ′ ⟩.
                                     7.3. Multiple q-zeta brackets                                                  94

    Since [w] ∼ (1 − q)−|w| ζ(w), [v] ∼ (1 − q)−|v| ζ(v) as q → 1− and [w v] =                             
[w] · [v], Theorem 7.6 asserts that the stuffle product (7.16) of the algebra MD
reduces to the stuffle product of the algebra of MZVs in the limit as q → 1− .
    To analyse the duality of bi-brackets, we introduce the following alternative
extension of the mono-brackets (7.12), called multiple q-zeta brackets:
                                                
        s1 , . . . , s l          s1 , . . . , s l
    Z                      = Zq
        r1 , . . . , rl           r1 , . . . , r l
                  X
       =c                   mr11 −1 ds11 −1 · · · mrl l −1 dlsl −1 q (m1 +···+ml )d1 +(m2 +···+ml )d2 +···+ml dl
            m1 ,...,ml >0
            d1 ,...,dl >0
                  X  mr11 −1 ρ̂s1 (q m1 +···+ml )mr22 −1 ρ̂s2 (q m2 +···+ml ) · · · mrl l −1 ρ̂sl (q ml )
      =c
         m ,...,m >0
                           (1 − q m1 +···+ml )s1 (1 − q m2 +···+ml )s2 · · · (1 − q ml )sl
              1      l
                                                                                                             (7.19)

where
                                                      1
                            c=                                                 .
                                 (r1 − 1)! (s1 − 1)! · · · (rl − 1)! (sl − 1)!
Then
                                                                                                       
        s1       s                                                   s1 , . . . , s l        s1 , . . . , s l
              =Z 1                   and        [s1 , . . . , sl ] =                    =Z                      .
      r1 − 1     r1                                                   0, . . . , 0            1, . . . , 1

     By applying iteratively the binomial theorem in the forms
                                           r +r −1 
        (m + n)r1 −1 nr2 −1    1X 2
                                                                   mr1 +r2 −j−1     nj−1
                                                              
                                                        j−1
                             =
         (r1 − 1)! (r2 − 1)!    j=1
                                                        r2 − 1 (r1 + r2 − j − 1)! (j − 1)!

and
                                          r
                            (n − m)r−1 X               ni−1    mr−i
                                       =     (−1)r+i
                              (r − 1)!   i=1
                                                     (i − 1)! (r − i)!

we see that the Q-algebras spanned by either (7.14) or (7.19) coincide. More
precisely, the following formulae link the two versions of brackets.

     Exercise 7.8. Show that
                                             
              s1 ,        s2 , . . . , sl
            r1 − 1, r2 − 1, . . . , rl − 1
               r1 +r 2 −1           j2 +r3 −1           jl−1X  +rl −1         
                  X         j2 − 1       X         j3 − 1                   jl − 1
            =                                              ···
                 j2 =1
                            r2 − 1      j3 =1
                                                   r3 − 1         jl =1
                                                                           rl − 1
                                                                                
                              s1 ,            s2 ,      ...,      sl−1 ,      sl
              ×Z
                       r1 + r2 − j2 , j2 + r3 − j3 , . . . , jl−1 + rl − jl , jl
                                 7.3. Multiple q-zeta brackets                                95

and
                     X   r1 X  r2        rl−1
    s1 , . . . , s l                       X
Z                      =             ···        (−1)r1 +···+rl−1 −i1 −···−il−1
    r1 , . . . , rl
                         i1 =1 i2 =1     il−1 =1
                                                                                      
            r1 − i1 + i2 − 1                 rl−2 − il−2 + il−1 − 1 rl−1 − il−1 + rl − 1
    ×                                 ···
                     r1 − i1                       rl−2 − il−2                 rl−1 − il−1
                                                                                            
               s1 ,             s2 ,          ...,           sl−1 ,                    sl
    ×                                                                                          .
           i1 − 1, r1 − i1 + i2 − 1, . . . , rl−2 − il−2 + il−1 − 1, rl−1 − il−1 + rl − 1
  Exercise 7.8 allows us to construct an isomorphism φ of the two Q-algebras
Q⟨Z⟩ with two evaluation maps [ · ] and Z[ · ],
                                                                       
                                                       s1 , . . . , s l
                       Z[zs1 ,r1 · · · zsl ,rl ] = Z                      ,
                                                       r1 , . . . , r l
such that
                   [w] = Z[φw]        and       Z[w] = [φ−1 w].
Note however that the isomorphism breaks the simplicity of defining the stuffle
product . 
    Another algebraic setup can be used for the Q-algebra Q⟨Z⟩ with evalua-
tion Z. We can recast it as the familiar Q-subalgebra H0 = Q1 ⊕ x0 Hx1 of the
Q-algebra H = Q⟨x0 , x1 ⟩ by setting Z[1] = 1 and
                                                                  
                          s1 r1      sl rl        s1 , . . . , s l
                      Z[x0 x1 · · · x0 x1 ] = Z                      .
                                                  r1 , . . . , r l
The length (or depth) is defined as the number of appearances of the subword
x0 x1 , while the weight is the number of letters x0 or x1 minus the length.
    Proposition 7.7 (Duality). We have
                                                                      
                     s1 , s2 , . . . , sl         rl , rl−1 , . . . , r1
                  Z                          =Z                           .
                      r1 , r2 , . . . , rl        sl , sl−1 , . . . , s1
    Proof. This follows from the rearrangement of the summation indices:
                                l
                                X          l
                                           X            l
                                                        X           l
                                                                    X
                                      di         mj =         d′i         m′j
                                i=1        j=i          i=1         j=i

where d′i = ml+1−i and m′j = dl+1−j .                                                         □
    If τ denotes the familiar anti-automorphism of the algebra H (and of its
subalgebra H0 ), interchanging x0 and x1 , then, clearly, τ is an involution pre-
serving both the weight and length. The duality can be then stated as
                              Z[τ w] = Z[w]         for any w ∈ H0 .                     (7.20)
We also extend τ to Q⟨Z⟩ by linearity.
   The duality in Proposition 7.7 transfered to the bi-bracket setting (7.14),
namely φ−1 τ φ, is exactly the partition duality given by Bachmann.
                                    7.3. Multiple q-zeta brackets                                                  96

     We can now introduce the product which is dual to the stuffle one. Namely,
it is the duality composed with the stuffle product and, again, with the duality:
         w       v = φ−1 τ φ(φ−1 τ φw              φ−1 τ φv) for w, v ∈ Q⟨Z⟩.                              (7.21)
It follows then from Propositions 7.5 and 7.7 that
    Proposition 7.8. The evaluation map (7.17) on Q⟨Z⟩ satisfies [w v] =                                  
[w] · [v], so that it is also a homomorphism of the Q-algebra (Q⟨Z⟩, ) onto                                
(BD, · ).
   Proof. We have
        [w      v] = [φ−1 τ φ(φ−1 τ φw              φ−1 τ φv)]
                    = Z[τ φ(φ−1 τ φw            φ−1 τ φv)] = Z[φ(φ−1 τ φw                 φ−1 τ φv)]
                    = [φ−1 τ φw           φ−1 τ φv] = [φ−1 τ φw] · [φ−1 τ φv]
                    = Z[τ φw] · Z[τ φv] = Z[φw] · Z[φv] = [w] · [v].                                               □
    Note that (7.18) is also equivalent to the expansion from the right (this is
established in Exercise 3.15):
       wzs1 ,r1      vzs2 ,r2 ≡ (w                                           
                                          vzs2 ,r2 )zs1 ,r1 + (wzs1 ,r1 v)zs2 ,r2
                                                          
                                           r1 + r2 − 2               
                                       +                     (w v)zs1 +s2 ,r1 +r2 −1 .                       (7.22)
                                              r1 − 1
    The next statement addresses the structure of the dual stuffle product
(7.21) for the words over the sub-alphabet Z ′ = {zs = zs,1 : s = 1, 2, . . . } ⊂ Z.
Note that the words from Q⟨Z ′ ⟩ can be also presented as the words from
Q⟨x0 , x0 x1 ⟩ necessarily ending with x0 x1 .
   Proposition 7.9. Modulo the highest weight and length,
                               aw      bv ≡ a(w          bv) + b(aw         v)                            (7.23)
for arbitrary words w, v ∈ Q1 ⊕ Q⟨x0 , x0 x1 ⟩x0 x1 and a, b ∈ {x0 , x0 x1 }.
   Proof. First note that restricting (7.22) further modulo the highest length
implies
         wzs1 ,r1        vzs2 ,r2 ≡ (w        vzs2 ,r2 )zs1 ,r1 + (wzs1 ,r1        v)zs2 ,r2 ,
and that we also have
       wzs1 ,r1 +1       vzs2 ,r2 ≡ (wzs1 ,r1        vzs2 ,r2 )x1 + (wzs1 ,r1 +1         v)zs2 ,r2 ,
    wzs1 ,r1 +1      vzs2 ,r2 +1 ≡ (wzs1 ,r1         vzs2 ,r2 +1 )x1 + (wzs1 ,r1 +1            vzs2 ,r2 )x1 .
The relations already show that
                             wa′      vb′ ≡ (w         vb′ )a′ + (wa′       v)b′                          (7.24)
for arbitrary words w, v ∈ Q + Q⟨Z⟩ and a′ , b′ ∈ Z ∪ {x1 }, where
                  zs1 ,r1 · · · zsl−1 ,rl−1 zsl ,rl x1 = zs1 ,r1 · · · zsl−1 ,rl−1 zsl ,rl +1 .
                                     7.3. Multiple q-zeta brackets                                        97

   Secondly note that the isomorphism φ (based on Exercise 7.8) acts trivially
on the words from Q⟨Z ′ ⟩. Therefore, applying τ φ to both sides of (7.21) and
extracting the homogeneous part of the result corresponding to the highest
weight and length we arrive at
                       τ (w       v) ≡ τ w      τv    for all w, v ∈ Q⟨Z ′ ⟩.
Denoting                                    (
                                             x1             if a = x0 ,
                                   a = τa =
                                             x0 x 1         if a = x0 x1 ,
and using (7.24) we find out that
τ (aw       bv) ≡ τ (aw)         τ (bv) ≡ (τ w)a     (τ v)b
                 ≡ (τ w     (τ v)b)a + ((τ w)a           τ v)b
                 ≡ (τ w       τ (bv))a + (τ (aw)         τ v)b ≡ (τ (w        bv))a + (τ (aw        v))b
                 ≡ τ (a(w         bv) + b(aw      v)),
which implies the desired result.                                                                         □
   Theorem 7.10. For admissible words w = zs1 · · · zsl and v = zs′1 · · · zs′m of
weight |w| = s1 + · · · + sl and |v| = s′1 + · · · + s′m , respectively,
                  [w      v] ∼ (1 − q)−|w|−|v| ζ(w          v)       as    q → 1− ,
where    denotes the standard shuffle product of MZVs on Q⟨Z ⟩.                         ′

    Proof. Because both φ and τ respect the weight, Proposition 7.9 shows
that the only terms that can potentially interfere with the asymptotic be-
haviour as q → 1− correspond to the same weight but lower length. However,
according to (7.21) and (7.22), the ‘shorter’ terms do not belong to Q⟨Z ′ ⟩,
that is, they are linear combinations of the monomials zq1 ,r1 · · · zqn ,rn with
r1 + · · · + rn = l + m > n, hence rj ≥ 2 for at least one j. The latter
circumstance and Proposition 7.3 then imply
                               lim (1 − q)|w|+|v| [zq1 ,r1 · · · zqn ,rn ] = 0.                           □
                            q→1−

   Theorem 7.10 asserts that the dual stuffle product (7.21) restricted from
BD to the subalgebra MD reduces to the shuffle product of the algebra of
MZVs in the limit as q → 1− . More is true: using (7.18) and Proposition 7.9
we obtain
   Theorem 7.11. For two words w = zs1 · · · zsl and v = zs′1 · · · zs′m , not
necessarily admissible,
        [w      v−w      v] ∼ (1 − q)−|w|−|v| ζ(w ∗ v − w           v)           as       q → 1− ,
whenever the MZV on the right-hand side makes sense.
   In other words, the q-zeta model of bi-brackets provides us with a (far
reaching) regularisation of the MZVs: the former includes the extended double
shuffle relations as the limiting q → 1− case.
                                 7.3. Multiple q-zeta brackets                                 98

    Conjecture 7.12 (Bachmann). The resulting double stuffle (that is, stuffle
and dual stuffle) relations exhaust all the relations between the bi-brackets.
Equivalently (and simpler), the stuffle relations and the duality exhaust all the
relations between the bi-brackets.
    We would like to point out that the duality τ we introduced in this sec-
tion is similar to the duality of MZVs from Section 3.3. However the two
dualities are not related: the limiting q → 1− process squeezes the appear-
ances of x0 preceding x1 in the words xs01 x1 xs02 x1 · · · xs0l x1 , so that they be-
come x0s1 −1 x1 xs02 −1 x1 · · · xs0l −1 x1 . Furthermore, the duality of MZVs respects
the shuffle product: the dual shuffle product coincides with the shuffle product
itself. On the other hand, the dual stuffle product of MZVs is very different
from the stuffle (and shuffle) products. It may be an interesting problem to
understand the double stuffle relations of the algebra of MZVs.
    Finally, we present some observations towards another conjecture of Bach-
mann about the coincidence of the Q-algebras of bi- and mono-brackets.
    Conjecture 7.13 (Bachmann). MD = BD.
    Based on the representation of the elements from BD as the polynomials
from Q⟨x0 , x1 ⟩ (see also the above comment about duality τ ), we can loosely
interpret this conjecture for the algebra of MZVs as follows: all MZVs lie in
the Q-span of
                   ζ(s1 , s2 , . . . , sl ) = ζ(xs01 −1 x1 xs02 −1 x1 · · · xs0l −1 x1 )
with all sj to be at least 2 (so that there is no appearance of xr1 with r ≥ 2).
The latter statement is already known to be true: Brown proves that one can
span the Q-algebra of MZVs by the set with all sj ∈ {2, 3}.
    In what follows we analyse the relations for the model (7.19), because it
makes simpler keeping track of the duality relation. We point out from the
very beginning that the linear relations given below are all experimentally
found (with the check of 500 terms in the corresponding q-expansions) but we
believe that it is possible to establish them rigorously using the double stuffle
relations given above.
    The first presence of the q-zeta brackets that are not reduced  to ones from
MD by the duality relation happens in weight 3. It is Z 2 and we find out
                                                            2
that
                                                    2,1 
                         Z 22 = 12 Z 21 + Z 31 − Z 1,1
                                         
                                                          .
There are 34 totally q-zeta brackets of weight up to 4,
     ∗  1 ∗  2            ∗  
 Z      , Z 1 , Z 1 = Z 12 , Z 22 , Z 31 = Z 13 , Z 32 = Z 23 , Z 41 = Z 14 ,
                                                                                     
     ∗  2,1                                                     1,2   2,1 ∗  1,2 ∗
  Z 1,1
                          1,1   1,2        1,1   2,1 
     1,1 , Z 1,1 = Z 1,2 , Z 1,1 = Z 2,1 , Z 2,1 = Z 1,2 , Z 1,2 , Z 2,1 ,

                  Z 2,2
                                1,1   3,1        1,1   1,3        1,1 
                     1,1 = Z 2,2 , Z 1,1 = Z 1,3 , Z 1,1 = Z 3,1 ,
                     
  1,1,1 ∗  2,1,1                                                         1,1,1   1,1,1,1 ∗
           , Z 1,1,1 = Z 1,1,1
                                    1,2,1        1,1,1   1,1,2 
Z 1,1,1                     1,1,2 , Z 1,1,1 = Z 1,2,1 , Z 1,1,1 = Z 2,1,1 , Z 1,1,1,1 ,
                          
                                7.4. q-Differentiation of brackets                                   99

where the asterisk marks the self-dual ones. Only 21 of those listed are not
dual-equivalent, and only five of the latter are not reduced                   to the q-zeta
                                                                                          3  brack-
ets from MD; besides the already mentioned Z 2 these are Z 2 , Z 2,12
                                                                                                  
  2,1           1,2                                                                            2,1 ,
Z 1,2 and Z 2,1 . We find out that

         Z 32 = 41 Z 21 + 32 Z 41 − 2Z 2,2
                                         
                                                1,1 ,

        Z 2,1 = Z 1,1 + 2 Z 1,1 − Z 1,1 + Z 1,3
          2,1        2,1  1  1,2         2,2                   2,1,1       1,2,1 
                                                            1,1 − Z 1,1,1 − Z 1,1,1 ,
                                                            

        Z 2,1
                             2,1  1  1,2         2,2      3,1        1,3       1,2,1 
           1,2 = − 2 Z 1,1 − 2 Z 1,1 + 2Z 1,1 + Z 1,1 − Z 1,1 + Z 1,1,1 ,
                        1
          

        Z 1,2
                           2,1      2,2      2,1,1 
           2,1 = −Z 1,1 + 2Z 1,1 + Z 1,1,1 ,
          

and there is one more relation in this weight between the q-zeta brackets from
MD:
                                            2,2 
                 1
                   Z 21 − Z 31 + Z 41 − 2Z 1,1     + 2Z 3,1
                                                  
                 3                                      1,1 = 0.

The computation implies that the dimension dBD   4  of the Q-space spanned by
all multiple q-zeta brackets of weight not more than 4 is equal to the dimension
dMD
 4   of the Q-space spanned by all such brackets from MD and that both are
equal to 15. A similar analysis demonstrates that
                       dBD
                        5  = dMD
                              5  = 28 and dBD
                                           6  = dMD
                                                 6  = 51,
and it seems less realistic to compute and verify that dBD
                                                        n  = dMD
                                                              n  for n ≥ 7
though Conjecture 7.13 supports
                          ∞
                          X               ?         1 − x2 + x4
                                dMD
                                 n  xn =                                .
                          n=0
                                              (1 − x)2 (1 − 2x2 − 2x3 )

We can compare this with the count cMD n   and cBD
                                                n  of total number of mono-
and bi-brackets of weight ≤ n, respectively:
      ∞                                       ∞                               ∞
      X                     1                 X                   1−x        X
             cMD
              n  xn =                and             cBD n
                                                      n x =                =     F2n xn ,
       n=0
                         1 − 2x               n=0
                                                               1 − 3x + x2   n=0

where Fn denotes the Fibonacci sequence.
    In addition, we would like to point out one more expectation for the algebra
of (both mono- and bi-) brackets, which is not shared by other q-models of
MZVs: all linear (hence algebraic) relations between them over C(q) seem to
be always liftable to relations over Q.
    Exercise 7.9 (Open problem). Show that a collection of (bi-)brackets is
linearly dependent over C(q) if and only if it is linearly dependent over Q.

                          7.4. q-Differentiation of brackets
    Lemma 7.14 ([2, Theorem 3.1]). The generating series
                                    X
             T (x1 , . . . , xl ) =   [s1 , . . . , sl ]xs11 −1 · · · xsl l −1
                                         s1 ,...,sl >0
                                         7.4. q-Differentiation of brackets                                            100

of brackets of length l can be written as
                                                                            l
                                                                   X        Y edj xj q d1 +···+dj
                            T (x1 , . . . , xl ) =                                                  .
                                                              d ,...,d >0 j=1
                                                                              1 − q d1 +···+dj
                                                               1      l

    Proof. Indeed,
                                       X               (d1 x1 )s1 −1 · · · (dl xl )sl −1 n1 d1 +···+nl dl
                                                         X
      T (x1 , . . . , xl ) =                                                            q
                               s ,...,s >0 n >···>n >0
                                                        (s 1 −  1)! · · · (s l −   1)!
                                   1       l        1          l
                                                    d1 ,...,dl >0
                                         X
                           =                            ed1 x1 +···+dl xl q n1 d1 +···+nl dl
                               n1 >···>nl >0
                                d1 ,...,dl >0
                                        X
                           =                         ed1 x1 +···+dl xl q (m1 +···+ml )d1 +(m2 +···+ml )d2 +···+ml dl
                               d1 ,...,dl >0
                               m1 ,...,ml >0

                                       X           l
                                                   Y                X
                           =                              edj xj           q mj (d1 +···+dj ) .                             □
                               d1 ,...,dl >0 j=1                   mj >0

   Theorem 7.15 ([2, Theorem 1.7]). The Q-algebra MD is closed under the
                 d
derivative δ = q dq .

    Proof. We start from observing that
                            d 
                              q           dq d
                         δ          =
                            1 − qd     (1 − q d )2
implying
                                                                                                  l
                             X
                                                d1 x1 +···+dl xl     q d1         q d1 +···+dl X d1 + · · · + dj
δT (x1 , . . . , xl ) =                    e                                ···
                          d1 ,...,dl >0
                                                                   1 − q d1     1 − q d1 +···+dl j=1 1 − q d1 +···+dl
                                                                                       l
                      ∂ X              d1 x1 +···+dl xl   q d1         q d1 +···+dl X e(d1 +···+dj )x
                    =                e                           ···                                           .
                      ∂x d ,...,d >0                    1 − q d1     1 − q d1 +···+dl j=1 1 − q d1 +···+dl x=0
                                   1        l

    The product of two generating series
                                           X                                        qd      q d1           q d1 +···+dl
  T (x)T (x1 , . . . , xl ) =                            edx+d1 x1 +···+dl xl                      · · ·
                                       d,d1 ,...,dl >0
                                                                                  1 − q d 1 − q d1       1 − q d1 +···+dl

can be viewed as shuffling of single and l-tuple sums. We split the sum over d
into the sums
         X                  X                                 qd      q d1           q d1 +···+dl
Σj =                                   edx+d1 x1 +···+dl xl                  · · ·
      d ,...,d >0 d +···+d <d<d +···+d
                                                            1 − q d 1 − q d1       1 − q d1 +···+dl
         1    l     1          j            1           j+1
                                            7.4. q-Differentiation of brackets                                                      101
                                                                                    P                        P
for j = 0, 1, . . . , l, where the internal sums are 0<d<d1 and d>d1 +···+dl for
j = 0 and j = l, respectively, and the sums
              X           X                              qd      q d1           q d1 +···+dl
     Σ′j =                        edx+d1 x1 +···+dl xl                  · · ·
           d ,...,d >0 d=d +···+d
                                                       1 − q d 1 − q d1       1 − q d1 +···+dl
                      1     l           1       j

                          X                              q d1           q d1 +···+dl e(d1 +···+dj )x q d1 +···+dl
           =                       ed1 x1 +···+dl xl            · · ·
                 d1 ,...,dl >0
                                                       1 − q d1       1 − q d1 +···+dl   1 − q d1 +···+dl

for j = 1, . . . , l. Writing d = d1 + · · · + dj + dˆ and dj+1 = dˆ+ dˆj+1 , we see that
         Σj = T (x + x1 , . . . , x + xj+1 , xj+1 , . . . , xl ) for j = 0, 1, . . . , d − 1
and Σl = T (x + x1 , . . . , x + xl , x). For the second group of sums we use
q d = 1 − (1 − q d ) to write them as
                  X                            q d1           q d1 +···+dl    e(d1 +···+dj )x
         Σ′j =             ed1 x1 +···+dl xl          · · ·
               d ,...,d >0
                                             1 − q d1       1 − q d1 +···+dl 1 − q d1 +···+dl
                            1      l

                                − T (x + x1 , . . . , x + xj , xj+1 , . . . , xl )
for j = 1, . . . , l. It follows then that
                                                                       l
    X
                     d1 x1 +···+dl xl     q d1         q d1 +···+dl X e(d1 +···+dj )x
                 e                               ···
 d1 ,...,dl >0
                                        1 − q d1     1 − q d1 +···+dl j=1 1 − q d1 +···+dl
                                             l
                                             X
  = T (x)T (x1 , . . . , xl ) +                     T (x + x1 , . . . , x + xj , xj+1 , . . . , xl )
                                              j=1
                 l
                 X
          −               T (x + x1 , . . . , x + xj , xj , xj+1 , . . . , xl ) − T (x + x1 , . . . , x + xl , x).
                 j=1

Using T (x) = [1] + [2]x + · · · , differentiating both side of the identity and
substituting x = 0 we obtain
                                                                       j
                                                                     l X
                                                                     X   ∂T (x1 , . . . , xl )
     δT (x1 , . . . , xl ) = [2]T (x1 , . . . , xl ) +
                                                                     j=1 k=1
                                                                                          ∂xk
                                                l X     j
                                                X   ∂T (z1 , . . . , zl+1 )
                                            −
                                                j=1 k=1
                                                                      ∂zk               (z1 ,...,zl+1 )=(x1 ,...,xj ,xj ,...,xl )
                                                l+1
                                                X   ∂T (z1 , . . . , zl+1 )
                                            −                                                                   .
                                                k=1
                                                           ∂z   k           (z 1 ,...,z l+1 )=(x 1 ,...,x l ,0)

It remains to take into account that the coefficients in the (multi-variable)
Taylor expansion of any order partial derivative of T (x1 , . . . , xl ) are integer
multiples of mono-brackets.                                                       □
   Now we turn our attention to bi-brackets (7.14). A straightforward com-
putation implies the following result.
                                7.4. q-Differentiation of brackets                                102

   Lemma 7.16. We have
                           Xl                                                            
          s1 , . . . , s l                    s1 , . . . , sj−1 , sj + 1, sj+1 , . . . , sl
      δ                     =   sj (rj + 1)                                                   .
          r1 , . . . , r l                    r1 , . . . , rj−1 , rj + 1, rj+1 , . . . , rl
                                j=1

 As a corollary of Lemma 7.16 and Theorem 7.15 we deduce the following.
 Theorem 7.17. Any bi-bracket rs of length 1 is an element of Q-algebra
                                
MD.
   Proof. Since
                                                         
                                s+1      X
                                               r s nd   r+1
                                      =       ndq =           ,
                                 r      n,d>0
                                                         s

we assume without loss of generality that the entries of our bi-bracket rs
                                                                                   
under consideration satisfy s > r. Then a repeated application of Lemma 7.16
implies
                                                                          
      s         1        s−1                        1                    r s−r
          =          δ         = ··· =                                 δ         ,
      r     (s − 1)r r − 1             (s − 1)(s − 2) · · · (s − r) r!      0
and the result follows from noticing that the mono-bracket s−r
                                                                  
                                                                    0
                                                                        = [s − r] and
all its δ-derivatives are in MD by Theorem 7.15.                                    □
                                   Bibliography

 [1] H. Bachmann, Multiple Eisenstein series and q-analogues of multiple zeta values,
     in Periods in Quantum Field Theory and Arithmetic (RTMZV 2014, Madrid, Spain),
     J. I. Burgos Gil, K. Ebrahimi-Fard and H. Gangl (eds.), Springer Proc. Math. Stat. 314
     (Springer, 2020), 173–235.
 [2] H. Bachmann and U. Kühn, The algebra of generating functions for multiple divisor
     sums and applications to multiple zeta values, Ramanujan J. 40 (2016), no. 3, 605–648.
 [3] H. Bachmann and U. Kühn, A dimension conjecture for q-analogues of multiple zeta
     values, in Periods in Quantum Field Theory and Arithmetic (RTMZV 2014, Madrid,
     Spain), J. I. Burgos Gil, K. Ebrahimi-Fard and H. Gangl (eds.), Springer Proc. Math.
     Stat. 314 (Springer, 2020), 237–258.
 [4] W. N. Bailey, An algebraic identity, J. London Math. Soc. 11 (1936), 156–160.
 [5] J. M. Borwein, D. M. Bradley and D. J. Broadhurst, Evaluations of k-fold Eu-
     ler/Zagier sums: a compendium of results for arbitrary k, Electron. J. Combin. 4 (1997),
     no. 2, #R5.
 [6] J. M. Borwein, D. M. Bradley, D. J. Broadhurst and P. Lisoněk, Special values
     of multiple polylogarithms, Trans. Amer. Math. Soc. 353 (2001), no. 3, 907–941.
 [7] D. M. Bradley, Multiple q-zeta values, J. Algebra 283 (2005), no. 2, 752–798.
 [8] F. Brown, Mixed Tate motives over Z, Ann. of Math. (2) 175 (2012), 949–976.
 [9] J. I. Burgos Gil, J. Fresán, with contributions by U. Kühn, Multiple zeta values:
     from numbers to motives, Clay Mathematics Proceedings (in press).
[10] P. Deligne and A. B. Goncharov, Groupes fondamentaux motiviques de Tate mixte,
     Ann. Sci. École Norm. Sup. (4) 38 (2005), no. 1, 1–56.
[11] C. Glanois, Motivic unipotent fundamental groupoid of Gm \ µN for N = 2, 3, 4, 6, 8
     and Galois descents, J. Number Theory 160 (2016), 334–384.
[12] Kh. Hessami Pilehrood and T. Hessami Pilehrood, An alternative proof of a
     theorem of Zagier, J. Math. Anal. Appl. 449 (2017), no. 1, 168–175.
[13] Kh. Hessami Pilehrood and T. Hessami Pilehrood, Generating functions for
     multiple zeta star values, J. Théorie Nombres Bordeaux 31 (2019), no. 2, 343–360.
[14] M. Hirose, T. Matsusaka and S. Seki, A discretization of the iterated integral
     expression of the multiple polylogarithm, Preprint arXiv:2404.15210 [math.NT].
[15] M. Hirose and N. Sato, Hoffman’s conjectural identity, Intern. J. Number Theory
     15 (2019), no. 1, 167–171.
[16] M. Hirose and N. Sato, A new proof of the two-one formula, in progress (2020).
[17] M. E. Hoffman, Multiple zeta values, Michael Hoffman’s homepage; also a compre-
     hensive list of references on MZVs and related stuff.
[18] M. E. Hoffman, Multiple harmonic series, Pacific J. Math. 152 (1992), no. 2, 275–290.
[19] M. E. Hoffman, The algebra of multiple harmonic series, J. Algebra 194 (1997), no.
     2, 477–495.
[20] M. E. Hoffman, Quasi-shuffle products, J. Algebraic Combin. 11 (2000), no. 1, 49–68.
[21] M. E. Hoffman and Y. Ohno, Relations of multiple zeta values and their algebraic
     expression, J. Algebra 262 (2003), no. 2, 332–347.

                                            103
                                      Bibliography                                     104

[22] K. Ihara, J. Kajikawa, Y. Ohno and J. Okuda, Multiple zeta values vs. multiple
     zeta-star values, J. Algebra 332 (2011), 187–208.
[23] K. Ihara and M. Kaneko, Derivation relations and regularized double shuffle relations
     of multiple zeta values, Preprint (2000).
[24] K. Ihara, M. Kaneko and D. Zagier, Derivation and double shuffle relations for
     multiple zeta values, Compos. Math. 142 (2006), no. 2, 307–338.
[25] L. Lai, C. Lupu and D. Orr, Elementary proofs of Zagier’s formula for multiple zeta
     values and its odd variant, Preprint arXiv:2201.09262 [math.NT].
[26] T. Lee-Peng, Alternating double Euler sums, hypergeometric identities and a theorem
     of Zagier, J. Math. Anal. Appl. 462 (2018), 777–800.
[27] Z-H. Li, Another proof of Zagier’s evaluation formula of the multiple zeta values
     ζ(2, . . . , 2, 3, 2, . . . , 2), Math. Res. Lett. 20 (2013), 947–950.
[28] T. Maesaka, S. Seki and T. Watanabe, Deriving two dualities simultaneously
     from a family of identities for multiple harmonic sums. arXiv:2402.05730 Preprint
     arXiv:2402.05730 [math.NT].
[29] Y. Ohno, A generalization of the duality and sum formulas on the multiple zeta values,
     J. Number Theory 74 (1999), no. 1, 39–43.
[30] Y. Ohno, A proof of the cyclic sum conjecture for multiple zeta values, Preprint MPIM
     2000 (21).
[31] Y. Ohno and N. Wakabayashi, Cyclic sum of multiple zeta values, Acta Arith. 123
     (2006), no. 3, 289–295.
[32] Y. Ohno and D. Zagier, Multiple zeta values of fixed weight, depth, and height,
     Indag. Math. (N.S.) 12 (2001), no. 4, 483–487.
[33] Y. Ohno and W. Zudilin, Zeta stars, Commun. Number Theory Phys. 2 (2008), no. 2,
     325–347.
[34] J. Okuda and Y. Takeyama, On relations for the multiple q-zeta values, Ramanujan
     J. 14 (2007), no. 3, 379–387.
[35] J. Okuda and K. Ueno, Relations for multiple zeta values and Mellin transforms of
     multiple polylogarithms, Publ. Res. Inst. Math. Sci. 40 (2004), no. 2, 537–564.
[36] D. Orr, Generalized rational zeta series for ζ(2n) and ζ(2n + 1), Integral Transforms
     Spec. Funct. 28 (2017), no. 12, 966–987.
[37] G. Rhin and C. Viola, The group structure for ζ(3), Acta Arith. 97 (2001), no. 3,
     269–293.
[38] T. Rivoal, La fonction zêta de Riemann prend une infinité de valeurs irrationnelles
     aux entiers impairs, C. R. Acad. Sci. Paris Sér. I Math. 331 (2000), no. 4, 267–270.
[39] S. Seki and S. Yamamoto, A new proof of the duality of multiple zeta values and its
     generalizations, Intern. J. Number Theory 15 (2019), no. 6, 1261–1265.
[40] L. J. Slater, Generalized hypergeometric functions (Cambridge University Press,
     Cambridge, 1966).
[41] T. Terasoma, Mixed Tate motives and multiple zeta values, Invent. Math. 149 (2002),
     no. 2, 339–369.
[42] E. A. Ulanskii, Identities for generalized polylogarithms, Mat. Zametki 73 (2003),
     no. 4, 613–624; English transl., Math. Notes 73 (2003), 571–581.
[43] E. Ulanskii, A new proof of the theorem on Ohno relations for MZVs, Moscow J.
     Combin. Number Theory 7 (2017), no. 1, 79–88.
[44] J. Wan, Some notes on weighted sum formulae for double zeta values, in Number theory
     and related fields, Springer Proc. Math. Stat. 43 (Springer, New York, 2013), 361–379.
[45] S. Yamamoto, Interpolation of multiple zeta and zeta-star values, J. Algebra 385
     (2013), 102–114.
[46] S. Yamamoto, Some remarks on Maesaka–Seki–Watanabe’s formula for the multiple
     harmonic sums, Preprint arXiv:2403.03498 [math.NT].
                                           Bibliography                                           105

[47] D. Zagier, Values of zeta functions and their applications, in First European Congress
     of Mathematics, Vol. II (Paris, 1992), Progress in Math. 120 (Birkhäuser, Basel, 1994),
     497–512.
[48] D. Zagier, Evaluation of the multiple zeta values ζ(2, . . . , 2, 3, 2, . . . , 2), Ann. of Math.
     (2) 175 (2012), 977–1000.
[49] J. Zhao, On a conjecture of Borwein, Bradley and Broadhurst, J. Reine Angew. Math.
     639 (2010), 223–233.
[50] J. Zhao, Identity families of multiple harmonic sums and multiple zeta star values, J.
     Math. Soc. Japan 68 (2016), no. 4, 1669–1694.
[51] J. Zhao, Multiple zeta functions, multiple polylogarithms and their special values, Series
     on Number Theory and its Applications 12 (World Sci. Publ., Hackensack, NJ, 2016).
[52] W. Zudilin, Algebraic relations for multiple zeta values, Russian Math. Surveys 58
     (2003), no. 1, 1–29.
[53] W. Zudilin, Multiple q-zeta brackets, Mathematics 3 (2015), no. 1, 119–130.
[54] W. Zudilin, Hypergeometric heritage of W. N. Bailey, Not. Intern. Congress Chinese
     Mathematicians 7 (2019), no. 2, 32–46.
[55] W. Zudilin, On a family of polynomials related to ζ(2, 1) = ζ(3), in Periods in Quan-
     tum Field Theory and Arithmetic (RTMZV 2014, Madrid, Spain), J. I. Burgos Gil,
     K. Ebrahimi-Fard and H. Gangl (eds.), Springer Proc. Math. Stat. 314 (Springer,
     2020), 621–630.
                                    Index

Bailey, W.N., 84
Borwein, J.M., 50
Bradley, D.M., 50, 56
Broadhurst, D.J., 50
Brown, F., 64, 65

Cartier, P., 37

Deligne, P., 64

Glanois, C., 65
Goncharov, A.B., 64

Hirose, M., 47, 60, 78
Hoffman, M.E., 15, 16, 20, 60, 63

Ihara, K., 60

Kaneko, M., 60

Maesaka, T., 59
Matsusaka, T., 60

Ohno, Y., 19, 20, 48, 56, 60, 65
Okuda, J., 31, 56, 58, 85

Sato, N., 47, 78
Seki, S., 56, 59, 60

Takeyama, Y., 85
Terasoma, T., 64

Ueno, K., 31, 56, 58
Ulanskii, E.A., 31, 56

Wakabayashi, N., 20
Wan, J.G., 19
Watanabe, T., 59

Yamamoto, S., 56, 60

Zagier, D., 15, 48, 64, 65
Zhao, J., 50, 65, 78

                                     106
