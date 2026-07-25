---
title: "ball-rivoal-2001-inventiones-irrationalite-infinite-zeta"
source: "books-and-surveys/ball-rivoal-2001-inventiones-irrationalite-infinite-zeta.pdf"
conversion: pdftotext -layout
note: "extracted text; formulas are flattened and may be lossy — check the PDF for anything load-bearing"
---

Invent. math. 146, 193–207 (2001)
Digital Object Identifier (DOI) 10.1007/s002220100168

Irrationalité d’une infinité de valeurs
de la fonction zêta aux entiers impairs
Keith Ball1 , Tanguy Rivoal2
1 Department of Mathematics, UCL, Gower Street, London WC1E 6BT, UK
  (e-mail: kmb@math.ucl.ac.uk)
2 Laboratoire SDAD, CNRS FRE 2271, Département de Mathématiques, Université de
  Caen, Campus II, BP 186, 14032 Caen cédex, France
  (e-mail: rivoal@math.unicaen.fr)

Oblatum 5-VI-2000 & 25-V-2001
Published online: 13 August 2001 –  Springer-Verlag 2001

1. Introduction
                                  
Au contraire des nombres ζ(2n)= k≥1 1/k2n = (−1)n−1 22n−1 B2n π 2n /(2n)!
(n ≥ 1), dont la transcendance est une conséquence de celle de π, peu de
résultats sontactuellement connus sur la nature arithmétique des nombres
ζ(2n +1) = k≥1 1/k2n+1 . On peut citer en particulier les résultats suivants.
    • En 1978, Apéry [1] est parvenu à montrer l’irrationalité de ζ(3), mais sa
      démonstration n’a pas pu être généralisée aux nombres ζ(2n + 1) avec
      n ≥2 : voir Van der Poorten [20], Cohen [6] et Reyssat [14] pour des expo-
      sés de la méthode d’Apéry. D’autres démonstrations ont été données de-
      puis par Beukers [2,4,5], Nesterenko [11], Sorokin [19] et Prévost [13].
    • Des mesures d’irrationalité de ζ(3) ont aussi été établies par Apéry [1],
      Dvornicich-Viola [7], Hata [9] et Rhin-Viola [16].
    • En 1979, Gutnik [8] a démontré que, pour tout q ∈ Q, au moins un des
      deux nombres suivants est irrationnel
                         3ζ(3) + qζ(2) ,     ζ(2) + 2q log(2) .
    • En 1981, Beukers [3] a indiqué des résultats similaires à ceux de Gut-
      nik : les deux ensembles qui suivent contiennent au moins un nombre
      irrationnel
                  4                                                
                   π       7π 4 log(2)                7π 6
                       ,               − 15π 2 ,              − ζ(3)
                  ζ(3)        ζ(3)                 3240ζ(3)
                                                                          
         ζ(3)      ζ(3)2    π4                             ζ(3)ζ(5)    π6
               ,         −       , ζ(3)π − 30ζ(5) ,
                                          2
                                                                    −        .
          π2        π2     360                                π2      2268
194                                                                K. Ball, T. Rivoal

Dans cet article, nous démontrons qu’une infinité de valeurs de la fonction
ζ aux entiers impairs sont linéairement indépendantes sur Q. De façon plus
précise, nous prouvons le
Théorème 1 Soit a un entier impair ≥ 3 et notons δ(a) la dimension du
Q −espace vectoriel engendré par 1, ζ(3), ζ(5), . . . , ζ(a). On a alors
                                          1
                                 δ(a) ≥     log(a).
                                          3
De plus, pour tout ε > 0, il existe un entier A(ε) tel que si a > A(ε),
                                       1−ε
                            δ(a) ≥              log(a).
                                     1 + log(2)
Nous montrons également le
Théorème 2 Il existe un entier impair j ≤ 169 tel que 1, ζ(3) et ζ( j) sont
linéairement indépendants sur Q.
Les démonstrations de ces théorèmes sont données au paragraphe 3, après
celles des résultats auxiliaires, énoncés au paragraphe 2.
    Les méthodes de cet article s’inspirent du travail de Nikishin [12] sur
l’approximation simultanée des polylogarithmes Lin (z) en des valeurs ra-
tionnelles. Ces fonctions sont définies par le développement en série entière,
pour z ∈ C , |z| < 1,
                                        +∞
                                               zk
                             Lin (z) =                .
                                        k=0
                                             (k + 1)n
En particulier, Li1 (z) = − log(1 − z)/z diverge au voisinage de 1, alors que
si n ≥ 2, Lin (1) = ζ(n). La démarche de Nikishin le conduit à introduire
des séries de la forme
                      +∞
                               k(k − 1) · · · (k − an − b + 2)
       Nn,a,b (z) =                                                     z −k
                      k=0
                          (k + 1)a (k + 2)a · · · (k + n)a (k + n + 1)b

avec a, b, n entiers ≥ 1, 1 ≤ b ≤ a et z un nombre complexe de module ≥ 1,
z = 1. Ces séries fournissent des approximants de Padé de type I des poly-
logarithmes : spécialisées en z = −1, elles donnent donc des combinaisons
linéaires à coefficients rationnels en les ζ impairs, les ζ pairs et log(2). La
croissance en a des coefficients est néanmoins trop rapide pour obtenir un
résultat arithmétique non trivial dans ce cas.
    Plus récemment, Sorokin [18] a proposé une méthode pour éliminer (en
particulier) les ζ impairs : pour cela, il résout explicitement un problème
d’approximation simultanée de certaines fonctions multizêtas, parvenant
ainsi à donner une nouvelle mesure de transcendance de π. Dans la direc-
tion opposée, en généralisant les intégrales de Beukers [2], Vasilyev [21]
a construit une combinaison linéaire (à coefficients an , bn et cn entiers)
Irrationalité d’une infinité de valeurs de la fonction zêta aux entiers impairs             195

Jn (5) = an ζ(5) + bn ζ(3) + cn tendant vers 0 quand n tend vers +∞ : la
présence de ζ(3) ne permet malheureusement pas la démonstration directe
de l’irrationalité de ζ(5).
    Reyssat [15] a utilisé les approximants de Padé simultanés des puissances
de log(1 − x) pour montrer, avec a/b > 1 rationnel fixé, l’indépendance
linéaire sur Q d’une infinité des nombres logk (a/b) (où k ∈ N), ce qui suffit
pour prouver la transcendance de log(a/b).
    Ce dernier résultat suggère que, plutôt que la recherche, à la manière
d’Apéry, de l’irrationalité de chacune des valeurs de la fonction ζ aux
entiers impairs, il peut être fructueux de les considérer tous ensemble, afin de
prouver leur indépendance linéaire sur Q, ou un résultat dans cette direction.
Pour parvenir à cela, deux autres idées sont nécessaires. La première consiste
à modifier la série de Nikishin de la façon suivante :

                            +∞
                                           qn (k)
                                                             z −k
                            k=0
                                  (k + 1) · · · (k + n + 1)a
                                         a

où qn (k) est un polynôme qui est une fonction paire de k +n/2+1. La parité
de qn assure en effet qu’une fois la fraction rationnelle décomposée en frac-
tions partielles, les polynômes correspondant aux dénominateurs avec une
puissance paire s’annulent pour z = 1 : on obtient ainsi des combinaisons
linéaires à coefficients rationnels uniquement en les ζ impairs. La deuxième
idée est de paramétrer le nombre de zéros entiers de qn par un entier r et
d’ajuster celui-ci de sorte que les coefficients des combinaisons linéaires
aient une croissance moins importante que pour la série de Nikishin, tout
en gardant une décroissance rapide de la combinaison elle-même.
    Pour cela, nous introduisons la série

 Sn,a,r (z)
                     +∞
                       k · · · (k − rn + 1)(k + n + 2) · · · (k + (r + 1)n + 1)
     = n!     a−2r
                                                                                          z −k
                     k=0
                                    (k + 1)a (k + 2)a · · · (k + n + 1)a

où n, r et a sont des entiers vérifiant 1 ≤ r < a/2, n ∈ N. Les conditions
sur a et r assurent que Sn,a,r (z) converge pour tout complexe z de module
≥ 1. Pour simplifier l’exposé des résultats, nous écrirons cette série sous la
forme
                             +∞
                                 (k − rn + 1)rn (k + n + 2)rn −k
             Sn (z) = n!a−2r
                                                                z
                             k=0
                                           (k + 1)an+1

où (α)k est le symbole de Pochammer :

    (α)0 = 1 et            (α)k = α(α + 1) · · · (α + k − 1) si             k = 1, 2, . . .
196                                                                        K. Ball, T. Rivoal

Comme nous l’a suggéré le referee, il est aussi utile de remarquer que Sn (z)
est une fonction hypergéométrique généralisée :

                           Γ(rn + 1)a+1 Γ((2r + 1)n + 2)
  Sn (z) = z −rn−1 n!a−2r
                                 Γ((r + 1)n + 2)a+1
                                                                     
                                rn + 1, . . . , rn + 1, (2r + 1)n + 2
                                                                     z −1 .
                   × a+2 Fa+1
                                  (r + 1)n + 2, . . . , (r + 1)n + 2 
Le paragraphe 2 est consacré à l’étude précise de cette série : le Lemme 1
montre que la série Sn (1) fournit bien des combinaisons linéaires à coeffi-
cients rationnelles en les ζ impairs lorsque n est pair. Le Lemme 2 donne
une expression intégrale similaire à celles de Beukers [2] et de Dvornicich-
Viola [7], §1.3, ce qui permet d’estimer facilement lim |Sn (1)|1/n (Lem-
                                                                    n→+∞
me 3). Nous suivons ensuite Nikishin pour la démonstration des Lemmes 4
et 5, qui concernent les propriétés asymptotiques et arithmétiques des coeffi-
cients des combinaisons linéaires. Enfin, pour montrer que les séries Nn,a,b (z)
fournissent des approximations des polylogarithmes linéairement indépen-
dantes, Nikishin évalue un déterminant : nous évitons cette complication en
appliquant un critère d’indépendance linéaire, dû à Nesterenko [12].

Remerciements. Nous remercions le referee, dont les remarques ont permis
de simplifier les démonstrations des Lemmes 2 et 4. Le second auteur tient
par ailleurs à exprimer toute sa gratitude à F. Amoroso pour ses précieux
conseils qui ont permis de grandement améliorer une précédente version,
ainsi qu’à M. Waldschmidt pour sa patiente relecture et son soutien constant.

2. Résultats auxiliaires
                                                 λ
Dans toute la suite, on pose Dλ = λ!1 dtd λ et
                                      (t − rn + 1)rn (t + n + 2)rn
                    Rn (t) = n!a−2r
                                              (t + 1)an+1
de sorte que
                                           +∞
                                           
                                Sn (z) =             Rn (k)z −k .
                                           k=0
Pour l ∈ {1, . . . , a} et j ∈ {0, . . . , n}, on note aussi
                                
                 cl, j,n = Da−l Rn (t)(t + j + 1)a |t=− j−1 ∈ Q ,                        (1)

                    
                    a 
                      n            
                                   j−1
                                          1                         n
      P0,n (z) = −         cl, j,n              z j−k
                                                      et Pl,n (z) =     cl, j,n z j . (2)
                   l=1 j=1         k=0
                                       (k + 1)l
                                                                    j=0

Les Pl,n (z) sont donc des polynômes à coefficients rationnels.
Irrationalité d’une infinité de valeurs de la fonction zêta aux entiers impairs                    197

Lemme 1 On a :
                                                       
                                                       a
                          Sn (1) = P0,n (1) +                Pl,n (1)ζ(l).                           (3)
                                                       l=2

De plus,
                  si (n + 1)a + l est impair, alors Pl,n (1) = 0.                                    (4)
En particulier, si n est pair et a impair ≥ 3, Pl,n (1) = 0 pour tout l ∈
{2, . . . , a} pair et Sn (1) est alors une combinaison linéaire uniquement en
les ζ impairs :
                                               (a−1)/2
                                                 
                  Sn (1) = P0,n (1) +                     P2l+1,n (1)ζ(2l + 1).                      (5)
                                                 l=1

Démonstration
En décomposant Rn (t) en fractions partielles, on obtient :
                                             
                                             a 
                                               n
                                                         cl, j,n
                              Rn (t) =                             .
                                             l=1 j=0
                                                     (t +  j + 1)l

D’où si |z| > 1
                  
                  a 
                    n                 +∞
                                        1         1
      Sn (z) =              cl, j,n         k (k + j + 1)l
                  l=1 j=0             k=0
                                          z

                  
                  a 
                    n                       +∞
                                                            
                                                             j−1
                                               1     1           1    1
              =             cl, j,n z   j
                                                           −
                  l=1 j=0                   k=0
                                                z (k + 1)
                                                 k       l
                                                             k=0
                                                                 z (k + 1)l
                                                                  k

                  
                  a                   
                                      n                   
                                                          a 
                                                            n                 
                                                                              j−1
                                                                                     1
              =         Lil (1/z)           cl, j,n z −
                                                   j
                                                                    cl, j,n                z j−k .
                  l=1                 j=0                 l=1 j=1             k=0
                                                                                  (k + 1)l

On a donc
                                      
                                      a
                        Sn (z) =            Pl,n (z)Lil (1/z) + P0,n (z).                            (6)
                                      l=1

Comme 2r < a,le degré total de la fraction rationnelle Rn (t) est ≤ −2,
donc P1,n (1) = nj=0 Rest=− j (Rn (t)) = 0 et
                                lim (P1,n (z)Li1 (1/z)) = 0 ,
                               z→1
                               |z|>1

ce qui montre (3).
198                                                                         K. Ball, T. Rivoal

      Montrons maintenant (4) et pour cela reformulons (1) sous la forme
                         cl, j,n = (−1)a−l Da−l (Φn, j (x))|x= j
où

  Φn, j (x) = Rn (−x − 1)( j − x)a
                                            (−x − rn)rn (−x + n + 1)rn
                                 = n!a−2r                              ( j − x)a .
                                                    (−x)an+1
On a
                                       (x − (r + 1)n)rn (x + 1)rn
         Φn,n− j (n − x) = n!a−2r                                 (x − j)a .               (7)
                                              (x − n)an+1

En appliquant l’identité (α)l = (−1)l (−α − l + 1)l aux trois symboles de
Pochammer de (7), on obtient
      Φn,n− j (n − x)
                 (−1)rn (−x + n + 1)rn (−1)rn (−x − rn)rn
       = n!a−2r                                           (−1)a ( j − x)a
                            (−1)(n+1)a (−x)an+1
       = (−1)na Φn, j (x).
Donc pour tout k ≥ 0,

                      Φ(k)                       na (k)
                       n,n− j (n − x) = (−1) (−1) Φn, j (x).
                                            k

En particulier avec k = a − l et x = j, on a donc
                             cl,n− j,n = (−1)a−l (−1)an cl, j,n ,
ce qui implique la relation

                             Pl,n (1) = (−1)(n+1)a+l Pl,n (1).
Si (n + 1)a + l est impair, on en déduit que Pl,n (1) = 0.
    Définissons maintenant l’intégrale
                                   a+1 r                    n
                                   l=1 xl (1 − xl )               dx1 dx2 · · · dxa+1
       In (z) =
                  [0,1]a+1    (z − x1 x2 · · · xa+1 )2r+1       (z − x1 x2 · · · xa+1 )2

qui converge a priori pour tout complexe z tel que |z| > 1.
Lemme 2 La série Sn (z) admet la représentation intégrale, pour |z| ≥ 1 :
                                ((2r + 1)n + 1)! (r+1)n+2
                    Sn (z) =                    z         In (z).                          (8)
                                     n!2r+1
Irrationalité d’une infinité de valeurs de la fonction zêta aux entiers impairs              199

Démonstration
La série Sn (z) est une fonction hypergéométrique généralisée dont les para-
mètres sont tels qu’elle peut s’exprimer sous la forme intégrale voulue pour
|z| > 1 (voir par exemple [17], p. 108). Il s’agit de montrer que cette
représentation est encore valide si |z| = 1. Pour cela posons E = {z ∈ C :
|z| ≥ 1} et définissons la fonction
            a+1 r
                 l=1 xl (1−xl )
                                si (x, z) ∈ [0, 1]a+1 × E et (x, z) = (1, 1, . . . , 1);
F(x, z) = (z−x1 ···xa+1 )2r+1
              0                 si (x, z) = (1, 1, . . . , 1).

La fonction F(x, z) est continue sur [0, 1]a+1 × E : en effet, pour x ∈
[0, 1]a+1 , il est clair que pour tout l ∈ {1, . . . , a + 1}, on a 1 − x1 · · · xa+1 ≥
1 − xl , d’où
                                                   
                                                   a+1
                         (1 − x1 · · · xa+1 )a+1
                                                 ≥     (1 − xl ).
                                                                 l=1

Donc pour tout (x, z) ∈ [0, 1]              a+1
                                                     × E tel que (x, z) = (1, 1, . . . , 1),
                                                         a+1 
                                                                                  
                                                                              a−2r
                    |F(x, z)| ≤ F(x, 1) ≤                        xlr (1 − xl ) a+1 .
                                                          l=1

Il en résulte que la fonction F(x, z) est continue sur [0, 1]a+1 × E, puisque
a > 2r.
    Par ailleurs, la fonction G(x, z) = (z − x1 · · · xa+1 )−2 est intégrable sur
[0, 1]a+1 , ce qui résulte de la continuité, pour |t| ≤ 1, de la fonction
                                1       1       1
                                                      dudvdw
                                                                = Li2 (t).
                            0       0       0       (1 − uvwt)2
Notons S̃n (z) le membre de droite de (8) et u(x, z) = F(x, z)n G(x, z). Alors
 • pour tout z ∈ E, |u(x, z)| ≤ u(x, 1) et u(x, 1) est intégrable sur [0, 1]a+1
 • pour tout x ∈ [0, 1]a+1 , x = (1, . . . , 1), la fonction u(x, z) est continue
   sur E.
Donc S̃n (z) est continue sur E. Comme Sn (z) est aussi continue sur E et
Sn (z) = S̃n (z) si |z| > 1, cette dernière égalité est encore vraie sur E, ce
qui termine la démonstration du Lemme 2.
    Considérons le polynôme
                  Q r,a (s) = rsa+2 − (r + 1)sa+1 + (r + 1)s − r .
On remarque que Q r,a (s) = sa+1 (rs − r − 1) + ((r + 1)s − r) < 0 sur
[0, r+1
     r
        ]. De plus
                 
               Q r,a (s) = r(a + 2)sa+1 − (r + 1)(a + 1)sa + r + 1
200                                                                            K. Ball, T. Rivoal

et
                  
                Q r,a (s) = (a + 1)sa−1 (r(a + 2)s − (r + 1)a) .
                                                        
D’où Q r,a (0) = r + 1 > 0, Q r,a (1) = 2r − a < 0 et Q r,a  (s) < 0 sur [0, 1].
On en déduit que Q r,a a une seule racine s0 dans [0, 1[ et que s0 ∈ ] r+1
                                                                         r
                                                                            , 1[.
Lemme 3 On a
                                lim |Sn (1)|1/n = ϕr,a                                       (9)
                              n→+∞

où
             ϕr,a = ((r + 1)s0 − r)r (r + 1 − rs0 )r+1 (1 − s0 )a−2r .
De plus, on a l’encadrement
                                                       2r+1
                                   0 < ϕr,a ≤                 .
                                                       r a−2r
Nous allons donner une première démonstration en utilisant le Lemme 2,
puis une seconde démonstration en utilisant directement la série.

Première démonstration
En vertu de la formule de Stirling,
                                     
                      ((2r + 1)n + 1)! 1/n
                lim                        = (2r + 1)2r+1 .
              n→+∞          n!2r+1

L’expression intégrale (8) et le Lemme 2 impliquent que lim |Sn (1)|1/n
                                                        n→+∞
existe et vaut
                                                              a+1 r
                                                              l=1 xl (1 − xl )
     ϕr,a = (2r + 1)2r+1            max                                                > 0.
                           (x1 ,... ,xa+1 )∈[0,1]a+1     (1 − x1 x2 · · · xa+1 )2r+1

Posons
                                                            a+1 r
                                                            l=1 xl (1 − xl )
             F(x) = F(x1 , . . . , xa+1 ) =
                                                       (1 − x1 x2 · · · xa+1 )2r+1
et f(x) = log(F(x)) : les extrema de F doivent vérifier pour tout l ∈
{1, . . . , a + 1}
                                                                 
          ∂f        1        xl                x1 x2 · · · xa+1
              (x) =     r−        + (2r + 1)                        = 0.
          ∂xl       xl     1 − xl            1 − x1 x2 · · · xa+1
Le maximum de F est donc atteint sur la diagonale x1 = x2 = · · · = xa+1
et on a                                r(a+1)            
                                       s       (1 − s)a+1
          ϕr,a = (2r + 1)2r+1
                               max                          .
                              s∈[0,1]    (1 − sa+1 )2r+1
Irrationalité d’une infinité de valeurs de la fonction zêta aux entiers impairs     201

On vérifie que ce maximum est atteint pour s = s0 , racine dans ]0, 1[ du
polynôme Q r,a . De la relation rs0a+2 − (r + 1)s0a+1 + (r + 1)s0 − r = 0, on
déduit que
                                     (r + 1)s0 − r
                            s0a+1 =
                                      r + 1 − rs0
d’où
                                  sr(a+1) (1 − s0 )a+1
               ϕr,a = (2r + 1)2r+1 0
                                    (1 − s0a+1 )2r+1

                    = ((r + 1)s0 − r)r (r + 1 − rs0 )r+1 (1 − s0 )a−2r

                         (2r + 1)r+1    (2r + 2)r+1   2r+1
                    ≤                ≤              ≤
                        (r + 1)a−r+1   (r + 1)a−r+1   r a−2r
                            r
en utilisant l’encadrement r+1 < s0 < 1.

Seconde démonstration
Ecrivons Rn (k) = (k + 1)−a R̃n (k) où
                                        (k − rn + 1)rn (k + n + 2)rn
                    R̃n (k) = n!a−2r                                 .
                                                 (k + 2)an
Puisque R̃n (k) = 0 pour 0 ≤ k ≤ rn − 1 et que r < a/2, on voit facilement
qu’il existe c = c(a, r) > 0 tel que
                              max R̃n (k) = max R̃n (k).
                               k≥0              rn≤k≤cn
                                              
Notons Mn ce maximum : comme                         (k + 1)−a < 1 et R̃n (k) ≥ 0, on a
                                              k≥rn

                                  1
                                      Mn ≤ Sn (1) ≤ Mn .
                                (cn)a
                                        1/n
Il suffit donc de montrer que Mn converge vers ϕr,a . La formule de Stirling
montre que pour rn ≤ k ≤ cn
                                  kk(a+1) (k + (r + 1)n)k+(r+1)n n n(a−2r)
               R̃n (k) = ρn (k)
                                      (k + n)(k+n)(a+1)(k − rn)k−rn
où ρn (k)1/n tend vers 1. Posons
                                       x x(a+1)(x + r + 1)x+r+1
                         F̃(x) =                                 .
                                     (x + 1)(x+1)(a+1)(x − r)x−r
Alors                                   
                                        k
               max F̃(x) = lim max F̃      = lim Mn1/n .
               x∈[r,c]    n→+∞ rn≤k≤cn  n   n→+∞
202                                                                    K. Ball, T. Rivoal

De plus, on peut choisir c de telle sorte que max F̃(x) =                   max F̃(x).
                                                         x∈[r,c]           x∈[r,+∞[
Donc
                            lim |Sn (1)|1/n = max F̃(x).
                           n→+∞                   x∈[r,+∞[

Un calcul montre que max F̃(x) = F̃(x0 ) où x0 = s0 /(1 − s0 ), et que
                             x∈[r,+∞[
F̃(x0 ) = ϕr,a .
    Notons enfin que la majoration ϕr,a ≤ 2r+1 /r a−2r découle immédiate-
ment de l’inégalité k + (r + 1)n < 21+1/r k pour k > rn. En effet, pour
k > rn on a
                                             a−2r n  2r+1 n
                 (a−2r)n k (2
                          rn 1+1/r rn
                                  k)     r+1 n
    R̃n (k) < n                       = 2                 < a−2r .
                              kan              k              r

Lemme 4 Pour tout l ∈ {0, . . . , a},
                               1/n
             lim sup  Pl,n (1) ≤ 2a−2r (2r + 1)2r+1 .                               (10)
                        n→+∞

Démonstration
Si l ∈ {1, . . . , a}, il suffit de majorer les coefficients cl, j,n puisque Pl,n (1) =
  n
    j=0 cl, j,n . Pour cela on utilise la formule de Cauchy :

                             1
                cl, j,n =                        Rn (z)(z + j + 1)l−1 dz
                            2iπ   |z+ j+1|=1/2

où |z + j + 1| = 1/2 désigne le cercle de centre − j − 1 et de rayon 1/2.
Sur ce cercle, on a
                            |(z − rn + 1)rn | ≤ ( j + 2)rn ,
                          |(z + n + 2)rn | ≤ (n − j + 2)rn ,
                   et |(z + 1)n+1 | ≥ 2−3 ( j − 1)!(n − j − 1)! .
On a alors
                            (rn + j + 1)!              ((r + 1)n − j + 1)!
         |cl, j,n | ≤                             ·
                        ( j + 1)!( j!(n − j)!) (n − j + 1)!( j!(n − j)!)r
                                              r
                                       a−2r
                                 n!
                         ·                      · ( j(n − j))a 8a ,
                             j!(n − j)!

                  ≤ (2r + 1)(2r+1)n+2 2(a−2r)n (2n 2 )a
en remarquant que les coefficients multinômiaux
                 (rn + j + 1)!                      ((r + 1)n − j + 1)!
                                         et
             ( j + 1)!( j!(n − j)!)r             (n − j + 1)!( j!(n − j)!)r
Irrationalité d’une infinité de valeurs de la fonction zêta aux entiers impairs             203

sont majorés respectivement par (2r + 1)rn+ j+1 et (2r + 1)(r+1)n− j+1 . On a
donc                               1/n
                  lim sup  Pl,n (1) ≤ 2a−2r (2r + 1)2r+1 .
                       n→+∞
Il nous reste à majorer P0,n (1), dont on a déterminé l’expression (2)
                                        
                                        a 
                                          n                    
                                                               j−1
                                                                      1
                       P0,n (1) = −                  cl, j,n                .
                                        l=1 j=1                k=0
                                                                   (k + 1)l

Comme
                         
                         j−1
                                 1       
                                         j−1
                                              1
                                       ≤         ≤ j ≤n
                          k=0
                              (k + 1)l
                                         k=0
                                             k+1
on a bien là aussi
                                       1/n
                      lim sup  P0,n (1) ≤ 2a−2r (2r + 1)2r+1 .
                      n→+∞

Lemme 5 On pose dn = ppcm(1, 2, . . . , n). Alors pour l ∈ {0, . . . , a}
                                    dna−l Pl,n (z) ∈ Z [z].                                  (11)

Démonstration
L’évaluation du dénominateur des coefficients cl, j,n repose sur une réécriture
de Rn (t). Fixons les entiers n et j. On décompose alors le numérateur de
Rn (t) en 2r produits de n facteurs consécutifs :
                                       
                                       r                        
                                                                r
           Rn (t)(t + j + 1) =  a
                                              Fl (t) ×                G l (t) × H(t)a−2r
                                        l=1                     l=1

où pour l ∈ {1, . . . , r},
           (t − nl + 1)n                                              (t + nl + 2)n
Fl (t) =                 (t + j + 1) ,                G l (t) =                     (t + j + 1) ,
             (t + 1)n+1                                                 (t + 1)n+1
                                     n!
                             H(t) =         (t + j + 1).
                                (t + 1)n+1
Décomposons Fl (t), G l (t) et H(t) en fractions partielles :
                         
                         n
                           ( j − p) f p,l                              
                                                                       n
                                                                         ( j − p)g p,l
         Fl (t) = 1 +                           , G l (t) = 1 +                          ,
                         p=0
                             t+ p+1                                     p=0
                                                                            t+ p+1
                         p= j                                           p= j

                                              
                                              n
                                                ( j − p)h p
                                    H(t) =
                                              p=0
                                                     t+ p+1
                                              p= j
204                                                                       K. Ball, T. Rivoal

où
               (− p − nl)n
     f p,l =
               
               n
                 (− p + h)
               h=0
               p= p
                                                             
                 (−1)n ((l − 1)n + p + 1)n       n− p nl + p   n
               =                           = (−1)                 ∈ Z,
                     (−1) p!(n − p)!
                           p                             n     p

               (− p + nl + 1)n
     g p,l =
                n
                    (− p + h)
                h=0
                p= p
                                                                
                   (−1) p ((l + 1)n − p)!           n(l + 1) − p n
                 =                        = (−1) p                    ∈Z
                    (nl − p)! p!(n − p)!                  n         p
et                                                         
                           n!          (−1) p n!         p n
               hp = n              =             = (−1)        ∈ Z.
                                     p!(n − p)!            p
                        (− p + h)
                       h=0
                       p= p
On a alors pour tout entier λ ≥ 0 :
                                                  n
                                                            ( j − p) f p,l
                  (Dλ Fl (t))|t=− j−1 = δ0,λ +        (−1)λ                ,
                                                  p=0
                                                            ( p −  j)λ+1

                                                  p= j

                                               n
                                                         ( j − p)g p,l
                 (Dλ G l (t))|t=− j−1 = δ0,λ +     (−1)λ               ,
                                               p=0
                                                         ( p − j)λ+1
                                                  p= j

                                         
                                         n
                                                         ( j − p)h p
                  (Dλ H(t))|t=− j−1 =           (−1)λ
                                         p=0
                                                         ( p − j)λ+1
                                         p= j

avec δ0,λ = 1 si λ = 0, δ0,λ = 0 si λ > 0. On a donc montré que
          dnλ (Dλ Fl )|t=− j−1 ,   dnλ (Dλ G l )|t=− j−1     et dnλ (Dλ H )|t=− j−1
sont des entiers pour tout λ ∈ N. Grâce à la formule de Leibniz
 Da−l (R(t)(t + j + 1)a ) =
  
      (Dµ1 F1 ) · · · (Dµr Fr )(Dµr+1 G 1 ) · · · (Dµ2r G r )(Dµ2r+1 H ) · · · (Dµa H )
      µ

(où la somme est sur tous les multi-indices µ ∈ N a tels que µ1 + · · · + µa =
a − l), on en déduit alors que dna−l cl, j,n ∈ Z et donc que dna−l Pl,n (z) ∈ Z [z].
Irrationalité d’une infinité de valeurs de la fonction zêta aux entiers impairs        205

3. Irrationalité d’une infinité de ζ impairs

Nous appliquons le critère suivant pour démontrer la Proposition 1 ci-
dessous. Les Théorèmes 1 et 2 sont des conséquences de cette Proposition.

Critère d’indépendance linéaire de Nesterenko
Considérons N réels θ1 , θ2 , . . . , θ N (N ≥ 2) et supposons qu’il existe N
suites ( pl,n )n≥0 tels que :
(i)  ∀l ∈ {1, . . . , N}, pl,n ∈ Z ;
                   N
(ii) α1n+o(n) ≤ |      pl,n θl | ≤ α2n+o(n) avec 0 < α1 ≤ α2 < 1 ;
                     l=1
(iii) ∀l ∈ {1, . . . , N}, | pl,n | ≤ β n+o(n) avec β > 1.
Dans ces conditions,
                                                            log(β) − log(α1 )
      dimQ (Q θ1 + Q θ2 + · · · + Q θ N ) ≥                                         .
                                                       log(β) − log(α1 ) + log(α2 )

Proposition 1 Soit a un entier impair ≥ 3. Pour tout entier r tel que
1 ≤ r < a/2, on a la minoration
                   (a − 2r) log(2) + (2r + 1) log(2r + 1) − log(ϕr,a )
         δ(a) ≥                                                                         (12)
                      a + (a − 2r) log(2) + (2r + 1) log(2r + 1)
où
               ϕr,a = ((r + 1)s0 − r)r (r + 1 − rs0 )r+1 (1 − s0 )a−2r
et s0 est l’unique racine dans ]0, 1[ du polynôme Q(s) = rsa+2 −(r +1)sa+1
+ (r + 1)s − r. En particulier
                                       log(r) + a+1
                                                a−r
                                                    log(2)
                       δ(a) ≥                                          .                (13)
                                 1 + log(2) + 2r+1
                                              a+1
                                                   log(r + 1)

Démonstration
Notons tout d’abord que d’après le Théorème des nombres premiers,
                                       dn = en+o(n) .                                   (14)
Définissons pour tout entier n ≥ 0, n = d2n
                                           a
                                              S2n (1),
 p0,n = d2n
         a
            P0,2n (1) et pl,n = d2n
                                 a
                                    P2l+1,2n (1) pour l ∈ {1, . . . , (a − 1)/2} .
(5) montre que n est une combinaison linéaire en les ζ impairs :
                                           (a−1)/2
                                            
                           n = p0,n +               pl,n ζ(2l + 1).                    (15)
                                             l=1
206                                                              K. Ball, T. Rivoal

(11) montre que pour tout l ∈ {0, . . . , (a − 1)/2} et pour tout n ≥ 0,
pl,n ∈ Z . (9) et (14) montrent que
               log |n | = 2n log(κ) + o(n) avec      κ = ea ϕr,a .
Enfin, (10) et (14) impliquent que pour tout l ∈ {0, . . . , (a − 1)/2} :
        log | pl,n | ≤ 2n log(τ) + o(n) avec    τ = ea 2a−2r (2r + 1)2r+1 .
On peut donc appliquer le critère de Nesterenko avec N = (a + 1)/2,
α1 = α2 = κ 2 et β = τ 2 :
            log(τ) − log(κ)
  δ(a) ≥
                log(τ)
                       (a − 2r) log(2) + (2r + 1) log(2r + 1) − log(ϕr,a )
                    =                                                      .
                          a + (a − 2r) log(2) + (2r + 1) log(2r + 1)
En utilisant la majoration ϕr,a ≤ 2r+1 /r a−2r donnée au Lemme 3 et l’enca-
drement 2r ≤ 2r + 1 ≤ 2(r + 1), on obtient l’inégalité (13).

Démonstration du Théorème 2
On choisit a = 169 et r = 10 dans la Proposition 1 : un calcul par ordinateur
montre que
             s0 ≈ 0, 90909093       et   log(ϕ10,169) ≈ −505, 73453
d’où δ(169) > 2, 001. Il existe donc deux entiers impairs j et k tels que
3 ≤ j, k ≤ 169 et 1, ζ( j) et ζ(k) sont linéairement indépendants sur Q.
L’irrationalité de ζ(3) nous permet de supposer k = 3, ce qui prouve le
Théorème 2.

Démonstration du Théorème 1
Supposons a impair. Nous allons distinguer plusieurs cas :
• 3 ≤ a ≤ 167 < e6 : le Théorème d’Apéry donne δ(3) ≥ 2, d’où
  δ(a) ≥ 2 ≥ 13 log(a).
• 169 ≤ a ≤ 8.103 − 1 < e9 : le Théorème 2 donne δ(169) ≥ 3 d’où
  δ(a) ≥ 3 ≥ 13 log(a).
• 8.103 + 1 ≤ a ≤ 105 − 1 < e12 : la Proposition 1 (avec r = 200) donne
  δ(8.103 + 1) > 3 d’où δ(a) ≥ 4 ≥ 13 log(a).
• 105 + 1 ≤ a ≤ 106 − 1 < e15 : la Proposition 1 (avec r = 600) donne
  δ(105 + 1) > 4 d’où δ(a) ≥ 5 ≥ 13 log(a).
• a ≥ 106 + 1 : on choisit r = [a3/5 + 1] < a/2 dans la proposition 1. On
  obtient
                                      3
                            δ(a) ≥        log(a)
                                    5c(a)
      où c(a) = 1+log(2)+ 2aa+1+3 log(a3/5 +1) est décroissante et c(106 +1)
                              3/5

      < 9/5. Donc là aussi δ(a) ≥ 13 log(a).
Irrationalité d’une infinité de valeurs de la fonction zêta aux entiers impairs         207

Montrons maintenant la deuxième partie : on choisit pour cela r = r(a)
comme l’entier < a/2 le plus proche de a(log(a))−2 . On a alors
                          a−r
                log(r) +       log(2) = (1 + o(1)) log(a)
                         a+1
et
                        2r + 1
          1 + log(2) +         log(r + 1) = 1 + log(2) + o(1).
                         a+1
D’où
                               (1 + o(1)) log(a)
                        δ(a) ≥                   ,
                               1 + log(2) + o(1)
ce qui prouve le Théorème 1.

Références
 1. R. Apéry, Irrationalité de ζ(2) et ζ(3), Astérisque 61, 11–13 (1979)
 2. F. Beukers, A note on the irrationality of ζ(2) and ζ(3), Bull. London. Math. Soc. 11,
    no. 33, 268–272 (1978)
 3. F. Beukers, The values of Polylogarithms, “Topics in classical number theory”, 219–
    228, Colloq. Math. Soc. János Bolyai, Budapest (1981)
 4. F. Beukers, Padé approximations in Number Theory dans “Padé approximation and its
    applications”, Amsterdam 1980, LNM 888, 90–99, Springer (1981)
 5. F. Beukers, Irrationality proofs using modular forms, Journées arithmétiques de Be-
    sançon (Besançon, 1985). Astérisque No. 147–148 (1987)
 6. H. Cohen, Démonstration de l’irrationalité de ζ(3) (d’après Apéry), Séminaire de
    Théorie des Nombres de Grenoble, VI.1–VI.9 (1978)
 7. R. Dvornicich, C. Viola, Some remarks on Beukers’ integrals, dans Number Theory,
    Vol. II, 637–657, Budapest (1987). Colloq. Math. Soc. János Bolyai, 51, Budapest
 8. L.A. Gutnik, The irrationality of certain quantities involving ζ(3), Russ. Math. Surv.
    34, no. 3, 200 (1979). En russe dans Acta Arith. 42, no. 3, 255–264 (1983)
 9. M. Hata, A new irrationality measure for ζ(3), Acta. Arith. 92, no. 1, 47–57
10. Y.V. Nesterenko, On the linear independence of numbers, Mosc. Univ. Math. Bull. 40,
    no. 1, 69–74 (1985) traduction de Vest. Mosk. Univ., Ser. I, no. 1, 46–54 (1985)
11. Y.V. Nesterenko, A few remarks on ζ(3), Math. Notes 59, no. 6, 625–636 (1996)
12. E.M. Nikishin, On the irrationality of the values of the functions F(x, s), Mat. Sbornik
    37, no. 3, 381–388 (1979)
13. M. Prévost, A new proof of the irrationality of ζ(3) using Padé approximants, J. Comput.
    Appl. Math. 67, 219–235 (1996)
14. E. Reyssat, Irrationalité de ζ(3), selon Apéry, Séminaire Delange-Pisot-Poitou, 20ème
    année (1978–1979), exposé no. 6, 6pp
15. E. Reyssat, Mesures de transcendance pour les logarithmes de nombres rationnels,
    “Approximations diophantiennes et nombres transcendants”, Luminy 1982, 235–245,
    Progress in Mathematics, Birkhäuser (1983)
16. G. Rhin, C. Viola, The group structure for ζ(3), Acta Arith. 97, 269–293 (2001)
17. L.J. Slater, Generalized Hypergeometric Functions, Cambridge University Press (1966)
18. V.N. Sorokin, A transcendence measure for π 2 , Mat. Sbornik 187, no. 12, 1819–1852
    (1996)
19. V.N. Sorokin, Apéry’s Theorem, Mosc. Univ. Math. Bull. 53, no. 3, 48–52 (1998)
20. A. Van der Poorten, A proof that Euler missed... Apéry’s proof of the irrationality of
    ζ(3), Math. Intellig. 1, 195–203 (1979)
21. D.V. Vasilyev, On small linear forms for the values of the Riemann zeta function at odd
    integers, soumis à Dokl. Nat. Acad. Sci. of Belarus
