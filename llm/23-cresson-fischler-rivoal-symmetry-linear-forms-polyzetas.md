---
title: "Phénomènes de symétrie dans des formes linéaires en polyzêtas"
authors:
  - "Jacky Cresson"
  - "Stephane Fischler"
  - "Tanguy Rivoal"
arxiv_id: "math/0609744v2"
arxiv_url: "https://arxiv.org/abs/math/0609744"
published: "2006-09-27"
journal_ref: ""
doi: ""
source: "papers/23-cresson-fischler-rivoal-symmetry-linear-forms-polyzetas/CFRsym_corrige5.tex"
conversion: pandoc-flat
---

# Phénomènes de symétrie dans des formes linéaires en polyzêtas

**Jacky Cresson, Stephane Fischler, Tanguy Rivoal**

## Abstract

We give two generalizations, in arbitrary depth, of the symmetry phenomenon used by Ball-Rivoal to prove that infinitely many values of Riemann $ζ$ function at odd integers are irrational. These generalizations concern multiple series of hypergeometric type, which can be written as linear forms in some specific multiple zeta values. The proof makes use of the regularization procedure for multiple zeta values with logarithmic divergence.

---
We give two generalizations, in arbitrary depth, of the symmetry phenomenon used by Ball-Rivoal to prove that infinitely many values of Riemann $\zeta$ function at odd integers are irrational. These generalizations concern multiple series of hypergeometric type, which can be written as linear forms in some specific multiple zeta values. The proof makes use of the regularization procedure for multiple zeta values with logarithmic divergence.

# Introduction

Une généralisation de la fonction zêta de Riemann $\zeta(s)$ est donnée par les séries *polyzêtas*, définies pour tout entier $p\ge 1$ et tout $p$-uplet $\underline{s}=(s_1, s_2, \dots, s_p)$ d'entiers $\ge 1$, avec $s_1\ge 2$, par $$\zeta(s_1, s_2, \ldots, s_p)=
\sum_{k_1> k_2>\ldots > k_p\ge 1}
\frac{1}{k_1^{s_1}k_2^{s_2}\ldots k_p^{s_p}}.$$ Les entiers $p$ et $s_1+s_2+\ldots+s_p$ sont respectivement la profondeur et le poids de $\zeta(s_1, s_2, \ldots, s_p)$. On voit naturellement apparaı̂tre les polyzêtas lorsque, par exemple, on considère les produits des valeurs de la fonction zêta : on a $\zeta(n)\zeta(m)=\zeta(n+m)+\zeta(n,m)+\zeta(m,n)$, ce qui permet en quelque sorte de linéariser ces produits. En dehors de quelques identités telles que $\zeta(2,1)=\zeta(3)$ (due à Euler), la nature arithmétique de ces séries est aussi peu connue que celle des nombres $\zeta(s)$. Cependant, l'ensemble des nombres $\zeta(\underline s)$ possède une très riche structure algébrique assez bien comprise, au moins conjecturalement (voir [@MiW]). Par exemple, on peut s'intéresser aux $\mathbb Q$-sous-espaces vectoriels $\mathcal{Z}_p$ de $\mathbb{R}$, engendrés par les $2^{p-2}$ polyzêtas de poids $p\ge 2$ : $\mathcal{Z}_2=\mathbb Q\zeta(2)$, $\mathcal{Z}_3=\mathbb Q\zeta(3)+\mathbb Q\zeta(2,1)$, $\mathcal{Z}_4=\mathbb Q\zeta(4)+\mathbb Q\zeta(3,1)+
\mathbb Q\zeta(2,2)+
\mathbb Q\zeta(2,1,1)$, etc. Posons $v_p=\textup{dim}_{\mathbb Q}(\mathcal{Z}_p)$. On a alors la conjecture suivante, dont le point $(i)$ est dû à Zagier et le point $(ii)$ à Goncharov.

**Conjecture 1**. *$(i)$ Pour tout entier $p\ge 2$, on a $v_p=c_p$, où l'entier $c_p$ est défini par la récurrence linéaire $c_{p+3}=c_{p+1}+c_{p}$, avec $c_0=1$, $c_1=0$ et $c_2=1$.*

*$(ii)$ Les $\mathbb Q$-espaces vectoriels $\mathbb Q$ et $\mathcal{Z}_p$ ($p\ge 2)$, sont en somme directe.*

La suite $(v_p)_{p\ge 2}$ devrait donc croı̂tre comme $\alpha^p$ (où $\alpha\approx
1,3247$ est racine du polynôme $X^3-X-1$), ce qui est bien plus petit que $2^{p-2}$. Il y a donc conjecturalement beaucoup de relations linéaires entre les polyzêtas de même poids et aucune en poids différents : dans cette direction, un théorème de Goncharov [@Goncharov] et Terasoma [@terasoma] affirme que l'on a $v_p\le c_p$ pour tout entier $p\ge 2$. Il reste donc à montrer l'inégalité inverse pour montrer $(i)$, mais aucune minoration non triviale de $v_p$ n'est connue à ce jour : même si les relations classiques donnent $v_2=v_3=v_4=1$, on est bloqué dès l'égalité $v_5=2$, qui est équivalente à l'irrationalité toujours inconnue de $\zeta(5)/(\zeta(3)\zeta(2))$. Plus généralement, un des intérêts de la Conjecture 1 est d'impliquer la suivante.

**Conjecture 2**. *Les nombres $\,\pi, \zeta(3), \zeta(5), \zeta(7), \zeta(9),$ etc, sont algébriquement indépendants sur $\mathbb Q$.*

Cette conjecture semble actuellement totalement hors de portée. Un certain nombre de résultats diophantiens ont néanmoins été obtenus en profondeur 1, c'est-à-dire dans le cas de la fonction zêta de Riemann (voir [@SFBou]) :

-   Le nombre $\zeta(3)$ est irrationnel (Apéry [@Apery]) ;

-   La dimension de l'espace vectoriel engendré sur $\mathbb Q$ par 1, $\zeta(3)$, $\zeta(5), \ldots, \zeta(A)$ (avec $A$ impair) croı̂t au moins comme $\log(A)$ ([@BR; @RivoalCRAS]) ;

-   Au moins un des quatre nombres $\zeta(5), \zeta(7), \zeta(9), \zeta(11)$ est irrationnel (Zudilin [@Zudilinonze]).

Ces résultats peuvent être obtenus par l'étude de certaines séries de la forme $$\label{eq011}
\sum_{k=1}^{\infty} \frac{P(k)}{(k)_{n+1}^A}$$ avec $P(X)\in\mathbb Q[X]$, $n\ge0$, $A\ge 1$ ; on utilise ici le symbole de Pochhammer défini par $(k)_{\alpha} = k(k+1)\ldots (k+\alpha-1)$. Ces séries s'expriment comme combinaisons linéaires sur $\mathbb Q$ de 1 et des valeurs de zêta aux entiers. Le point crucial est que, dans ces combinaisons linéaires, figurent seulement *certaines* valeurs de la fonction zêta : $\zeta(3)$ dans le cas $(i)$, des valeurs $\zeta(s)$ avec $s$ impair dans les cas $(ii)$ et $(iii)$. Ceci provient (dans les deux derniers cas, et aussi dans certaines preuves de $(i)$) d'une propriété de symétrie liée à l'aspect (très) bien équilibré[^1] de la série (eq011) (voir [@BR] ou [@RivoalCRAS]) :

**Théorème 1**. *Soit $P \in \mathbb Q[X]$ de degré au plus $A(n+1)-2$, tel que $$P(-n-X) = (-1)^{A(n+1)+1} P(X).$$ Alors la série (eq011) est une combinaison linéaire, à coefficients rationnels, de 1 et des valeurs $\zeta(s)$ pour $s$ entier impair compris entre 3 et $A$.*

Le but de cet article est de donner deux généralisations, en profondeur quelconque, de ce phénomène de symétrie. Nous espérons que ces généralisations ouvriront la porte à des résultats diophantiens (d'irrationalité ou d'indépendance linéaire) sur les polyzêtas qui interviennent (voir §2.4).

Notre premier résultat (démontré au paragraphe 6) concerne des sommes *découplées*, c'est-à-dire portant sur tous les $p$-uplets $(k_1, \ldots, k_p) \in {\mathbb{N}^*}^p$ :

**Théorème 2**. *Soient $p \geq 1$, $n \geq 0$ et $A \geq 1$ des entiers. Soit $P \in \mathbb Q[X_1, \ldots, X_p]$ un polynôme de degré $\leq A(n+1)-2$ par rapport à chacune des variables, tel que $$\begin{gathered}
\quad P(X_1,\ldots, X_{j-1}, -X_j-n, X_{j+1}, \ldots, X_p )
\\
= (-1)^{A(n+1)+1} P( X_1,\ldots, X_{j-1}, X_j, X_{j+1}, \ldots, X_p )\quad
\end{gathered}$$ pour tout $j \in \{1,\ldots, p\}$. Alors la somme multiple $$\label{eqdecouple}
\sum_{k_1,  \ldots ,  k_p \ge 1}
\frac{P(k_1, \ldots, k_p)}{(k_1)_{n+1}^{A} \ldots (k_p)_{n+1}^{A} }$$ est un polynôme à coefficients rationnels, de degré au plus $p$, en les $\zeta(s)$, pour $s$ entier impair compris entre 3 et $A$.*

Par exemple, lorsque $A=3$ ou $A=4$, cette somme est un polynôme en $\zeta(3)$. Quand on prend $p=1$, on retrouve exactement le théorème 1 (quel que soit $A$).

La preuve du théorème 2 consiste essentiellement (après avoir décomposé la fraction rationnelle en éléments simples) à séparer la somme multiple en un produit de $p$ sommes simples auxquelles on applique le théorème 1. Elle utilise aussi un processus de régularisation, dans une situation simple et élémentaire.

L'inconvénient principal du théorème 2, du point de vue des applications éventuelles, est le fait que la somme sur $k_1$, ..., $k_p$ soit découplée. Cet inconvénient est visible par trois aspects que nous décrivons maintenant.

Tout d'abord, les séries découplées donnent toujours des polynômes en valeurs de $\zeta$ en des entiers, même quand on omet l'hypothèse de symétrie du théorème 2. Cette remarque, qui découle de la preuve du théorème 2 (voir §6), montre que les polyzêtas ne peuvent pas intervenir réellement dans ce cadre.

Ensuite, considérons la série de Ball $$S_n=n!^2 \sum_{k=1}^{\infty} (k + \frac{n}{2}) \frac{(k-n)_{n}(k+n+1)_n}{(k)_{n+1}^4}.$$ Pour tout entier $n$, $S_n$ est une forme linéaire en $1$ et $\zeta(3)$ ; cela se déduit du théorème 1. Elle coı̈ncide exactement avec les formes linéaires qui ont permis à Apéry de démontrer l'irrationalité de $\zeta(3)$ ; sans rentrer dans les détails, indiquons que cette coı̈ncidence n'est pas du tout évidente et qu'elle est la première application de la conjecture des dénominateurs prouvée dans [@KR]. Pour tout entier $p\ge 1$, la série $S_n^p$ est évidemment une série découplée de la forme considérée dans le théorème 2 avec $$\begin{gathered}
P(X_1, \ldots, X_p)
\\
= n!^{2p}  (X_1  + \frac{n}{2})\ldots  (X_p + \frac{n}{2}) (X_1-n)_{n}\ldots (X_p-n)_{n} (X_1+n+1)_n \ldots (X_p+n+1)_n
\end{gathered}$$ et $A = 4$. Ainsi, $S_n^p$ est un polynôme en $\zeta(3)$ de degré (au plus) $p$, dont on pourrait a priori espérer déduire la transcendance de $\zeta(3)$. Pourtant, $S_n^p$ ne contient pas plus d'information diophantienne que $S_n$ et elle ne donne que l'irrationalité de $\zeta(3)$.

Enfin, les sommes multiples qui apparaissent dans les preuves d'irrationalité sont plutôt de la forme $$\label{eq012}
\sum_{k_1 \geq  \ldots \geq   k_p \ge 1}
\frac{P(k_1, \ldots, k_p)}{(k_1)_{n+1}^{A} \ldots (k_p)_{n+1}^{A} },$$ c'est-à-dire que la somme porte sur des variables ordonnées ; c'est à ce genre de séries que s'applique l'algorithme de [@CFRalgo]. Par exemple, lorsque $p=2$, $A=2$ et $$P(X_1, X_2) = n! (X_1-X_2+1)_n (X_2-n)_n(X_2)_{n+1},$$ Sorokin [@SorokinApery] démontre que la somme (eq012) est exactement [^2] la forme linéaire en 1 et $\zeta(3)$ utilisée par Apéry dans sa preuve d'irrationalité. Plus généralement, une conjecture de Vasilyev [@Vasilyev] affirmait qu'une certaine intégrale multiple, égale à la série $$\label{eq:vasilyev}
n!^{p-\varepsilon}\sum_{k_1 \geq  \cdots \geq   k_p \ge 1}
\frac{(k_1-k_2+1)_n \ldots(k_{p-1}-k_p+1)_n (k_p-n)_n }{(k_1)_{n+1}^{2} \ldots (k_{p-1})_{n+1}^{2}(k_p)_{n+1}^{2-\varepsilon} },$$ est une forme linéaire rationnelle en les valeurs de zêta aux entiers $\ge 2$ de la même parité que $\varepsilon\in\{0,1\}$. La formulation intégrale de cette conjecture a été démontrée dans [@Zudilinservice] et une version raffinée dans [@KR] : la méthode consiste à prouver que la série (eq:vasilyev) s'exprime aussi comme une série simple à laquelle le théorème 1 ci-dessus s'applique. Zlobin [@Zlobincoeff] a récemment obtenu une démonstration totalement différente par une étude directe de la série (eq:vasilyev), dans l'esprit des méthodes combinatoires développées dans cet article. On peut alors démontrer des résultats essentiellement de même nature que ceux de [@BR; @RivoalCRAS], ce qui renforce l'intérêt pour des sommes multiples sur des indices ordonnés.

Nous avons démontré dans [@CFRalgo] que toute série convergente de la forme (eq012) s'écrit comme combinaison linéaire de polyzêtas de poids au plus $pA$ et de profondeur au plus $p$ (et ce résultat théorique a été obtenu, indépendamment, par Zlobin [@ZlobinZametki2005]). En outre, nous avons présenté un algorithme, que nous avons implémenté [@CFRweb] en Pari, pour calculer explicitement une telle combinaison linéaire. Ceci nous a permis de découvrir les propriétés de symétrie que nous énonçons maintenant[^3] dans le cas particulier de la profondeur 2 :

**Théorème 3**. *Soient $n \geq 0$ et $A \geq 1$ des entiers, avec $n$ pair. Soit $P \in \mathbb Q[X_1,   X_2]$ un polynôme en deux variables, de degré $\leq A(n+1)-2$ par rapport à chacune d'elles, tel que $$\label{eqdefadeux}
\left\{
\begin{array}{l}
P(X_1, X_2) = - P(X_2, X_1) \\
P(-n-X_1, X_2 ) = (-1)^{A(n+1)+1} P( X_1, X_2 )\\
P(X_1, -n-X_2 ) = (-1)^{A(n+1)+1} P( X_1, X_2 )
\end{array}
\right.$$ Alors la somme double (eq012) est une combinaison linéaire, à coefficients rationnels :*

-   *de 1,*

-   *de valeurs $\zeta(s)$ avec $s$ entier impair compris au sens large entre 3 et 2A,*

-   *de différences $\zeta(s,s') - \zeta(s',s)$ avec $s$, $s'$ entiers impairs tels que $3 \leq s < s' \leq A$.*

Bien entendu, parmi les conditions (eqdefadeux), la troisième est conséquence des deux premières. En particulier, si $A=4$, ce théorème montre que la série double $$\sum_{k_1 \geq   k_2 \geq 1}
\frac{P(k_1,  k_2)}{(k_1)_{n+1}^{4}  (k_2)_{n+1}^{4} }$$ est une forme linéaire en $1$, $\zeta(3)$, $\zeta(5)$ et $\zeta(7)$ (ce qui était loin d'être évident a priori puisqu'on part d'une série double). Pour $A=3$, on obtient une forme linéaire en $1$, $\zeta(3)$, $\zeta(5)$ ; enfin, pour $A=2$, une forme linéaire en $1$ et $\zeta(3)$.

Il est à noter que dans la série (eq012), les variables $k_1$, ..., $k_p$ sont liées par des inégalités *larges*, comme dans [@CFRalgo] mais à l'inverse de la définition des polyzêtas.

Par exemple, le théorème 3 donne le cas particulier suivant :

**Corollaire 1**. *Soient $n, r, t, \varepsilon\geq 0$ et $A \geq 1$ des entiers, avec $n$ pair, tels que $$\varepsilon\equiv (A+1)(n+1) +1  \bmod 2$$ et $$\varepsilon+ 4 r + 2 t \leq (A-1)(n+1)-4.$$ Alors la série convergente $$\sum_{k_1 \geq k_2 \geq 1}
  \big(k_1 + \frac{n}{2}\big)^{\varepsilon}  \big(k_2 + \frac{n}{2}\big)^{\varepsilon}
 \frac{ (k_1-k_2-r)_{2r+1} (k_1+k_2+n-r)_{2r+1} (k_1-t)_{2t+n+1}
 (k_2-t)_{2t+n+1} }{(k_1)_{n+1}^{A}  \;(k_2)_{n+1}^{A} }$$ est une combinaison linéaire, à coefficients rationnels, de 1, de valeurs $\zeta(s)$ (avec $s$ entier impair tel que $3 \leq s \leq  2A-1$), et de différences $\zeta(s,s') - \zeta(s',s)$ (avec $s$, $s'$ entiers impairs tels que $3 \leq s < s' \leq A$).*

Par exemple, on a $$\begin{gathered}
\sum_{k_1\ge k_2\ge 1} \big(k_1+\frac 12\big)\big(k_2+\frac 12\big)\frac{(k_1-k_2-1)_3(k_1+k_2)_3(k_1-1)_4(k_2-1)_4}
{(k_1)_2^7\;(k_2)_2^7}
\\
= -1156 +891\,\zeta(3)+ \frac{189}2 \,\zeta(5) + 78 \big(\zeta(5,3) -\zeta(3,5)\big).
\end{gathered}$$

Un autre ingrédient, qui est fréquemment utilisé avec des séries simples, consiste à dériver la fraction rationnelle en $k$, avant de sommer ; par exemple, une double dérivation sert à montrer le résultat de Zudilin [@Zudilinonze] rappelé après la conjecture 2. Cette astuce, appliquée plusieurs fois, permet de faire disparaı̂tre $\zeta(s)$ de la forme linéaire obtenue, pour de petites valeurs de $s$. On peut imaginer de l'utiliser pour des sommes multiples, même si on n'a aucun résultat connu de disparition de polyzêtas dans ce cadre (voir cependant [@SFHoffman]). Il est clair qu'en dérivant une fraction rationnelle de la forme $P(X_1, \ldots, X_p)/\big((X_1)_{n+1}^{A} \ldots (X_p)_{n+1}^{A}\big)$ par rapport à l'une des variables $X_i$, on obtient une fraction rationnelle de la même forme (avec $A$ remplacé par $A+1$). En profondeur 2, si un polynôme $P(X_1, X_2)$ vérifie les relations (eqdefadeux), alors le polynôme $Q$ défini par $$\Big( \frac{\partial}{\partial X_1} \Big)^2  \Big(\frac{\partial}{\partial X_2} \Big)^2
\frac{P(X_1, X_2)}{(X_1)_{n+1}^{A}  (X_2)_{n+1}^{A} }
 =   \frac{Q(X_1, X_2)}{(X_1)_{n+1}^{A+2}  (X_2)_{n+1}^{A+2} }$$ les vérifie aussi ; on peut donc lui appliquer aussi le théorème 3. Cette remarque montre qu'on aurait pu ajouter des dérivations dans le corollaire 1. Elle s'applique aussi en profondeur quelconque.

Ce texte est divisé comme suit. Nous donnons au paragraphe 2 l'énoncé général, en profondeur quelconque, que nous obtenons. C'est l'occasion d'introduire la notion de *polyzêtas antisymétriques*, et aussi de comparer notre généralisation des séries (très) bien équilibrées à celles provenant des systèmes de racines.

La preuve utilise deux outils : la régularisation des séries à divergence logarithmique et le développement en éléments simples des fractions rationnelles, qui sont présentés aux paragraphes 3 et 4 respectivement. Ces outils permettent d'énoncer (au paragraphe 4.2) le théorème 6, qui implique notre résultat principal (voir §4.4). Ce théorème est démontré au paragraphe 5, par récurrence sur la profondeur : il s'agit du cœur de la preuve. Le cas des profondeurs 1, 2 et 3 sont détaillés séparément, et servent d'introduction à la démonstration générale.

Enfin, au paragraphe 6, on démontre le théorème 2 énoncé ci-dessus. La preuve suit la même stratégie que celle du résultat principal, mais chaque étape est nettement plus simple à mettre en œuvre.

Les auteurs ont eu l'opportunité d'utiliser la puissance de calcul de la grappe Médicis, ce qui leur a permis de mener plus facilement les expérimentations qui ont conduit aux résultats de cet article. Nous remercions également C. Krattenthaler, M. Schlosser, W. Zudilin et l'arbitre pour leurs nombreuses remarques sur cet article, en particulier pour avoir porté à notre attention le lien entre nos séries et les systèmes de racines. Enfin, le premier auteur remercie l'I.H.É.S. pour l'invitation lors de laquelle il a pu terminer ce travail.

# L'énoncé dans le cas convergent

## Polyzêtas antisymétriques

Pour énoncer notre résultat en profondeur quelconque, nous aurons besoin de la notation suivante. Pour $p \geq 0$ et $s_1, \ldots, s_p \geq 2$ entiers, on pose $$\zeta^{{\rm as}}(s_1, \ldots, s_p) =  \sum_{\sigma\in\mathfrak{S}_p} \varepsilon_{\sigma}
\zeta(s_{\sigma(1)}, \ldots, s_{\sigma(p)}) ,$$ où $\varepsilon_{\sigma}$ désigne la signature de la permutation $\sigma$. On appelle *polyzêta antisymétrique* une telle combinaison linéaire de polyzêtas (même si, pour $p \geq 2$, ce n'est pas en général un polyzêta). Il s'agit de séries convergentes, puisque tous les $s_i$ sont supposés être supérieurs ou égaux à 2 ; on utilisera donc parfois le terme de *polyzêta antisymétrique convergent*. Pour $p=1$, on a $\zeta^{{\rm as}}(s) = \zeta(s)$. La convention naturelle consiste à poser $\zeta^{{\rm as}}(s_1,
\ldots, s_p) = 1$ lorsque $p=0$, puisqu'il existe une unique bijection de l'ensemble vide dans lui-même. Pour $p=2$, on a $\zeta^{{\rm as}}(s_1, s_2) = \zeta(s_1, s_2) - \zeta(s_2, s_1)$ et lorsque $p=3$, on a $$\begin{gathered}
\zeta^{{\rm as}}(s_1, s_2, s_3)
\\
= \zeta(s_1, s_2, s_3) + \zeta(s_2, s_3, s_1) +  \zeta(s_3, s_1, s_2)
- \zeta(s_2, s_1, s_3) - \zeta(s_1, s_3, s_2) -  \zeta(s_3, s_2, s_1).
\end{gathered}$$ Par définition, pour tout $\sigma\in\mathfrak{S}_p$ on a $$\zeta^{{\rm as}}(s_{\sigma(1)}, \ldots, s_{\sigma(p)}) =  \varepsilon_{\sigma} \zeta^{{\rm as}}(s_1, \ldots, s_p),$$ et $\zeta^{{\rm as}}(s_1, \ldots, s_p) = 0$ dès que deux des $s_i$ sont égaux.

Il nous semble raisonnable de penser qu'en général, un poyzêta antisymétrique n'est pas un polynôme en valeurs de la fonction $\zeta$ de Riemann. En revanche, tout polyzêta "symétrique" (défini comme $\zeta^{{\rm as}}(s_1, \ldots, s_p)$ mais en omettant la signature $\varepsilon_{\sigma}$) est un polynôme en les valeurs $\zeta(s)$ (d'après [@Hoffman1992], Theorem 2.2).

## Enoncé du résultat principal

Notons $\mathscr{A}_p$ l'ensemble des polynômes $P(X_1, \ldots, X_p)\in\mathbb Q[X_1, \ldots, X_p]$ tels que : $$\begin{cases}
\mbox{Pour tout } \sigma \in\mathfrak{S}_p \mbox{,  on ait }
\\
\qquad \qquad
P(X_{\sigma(1)}, X_{\sigma(2)},\ldots, X_{\sigma(p)}) = \varepsilon_{\sigma} P(X_1, X_2, \ldots, X_p).
\\
\\
\mbox{Pour tout } j \in \{1,\ldots, p\}\mbox{,  on ait}
\\
\qquad \qquad  P(X_1,\ldots, X_{j-1}, -X_j-n, X_{j+1}, \ldots, X_p )
\\
\qquad \qquad \qquad \qquad = (-1)^{A(n+1)+1} P( X_1,\ldots, X_{j-1}, X_j, X_{j+1}, \ldots, X_p ).
\end{cases}$$ Ces conditions (qui font apparaı̂tre l'action de groupe qui sera utilisée au paragraphe 4.1) sont bien sûr redondantes. Si la première est satisfaite, alors il suffit notamment de vérifier la seconde pour une seule valeur de $j$.

Par exemple, $\mathscr{A}_2$ est exactement l'ensemble des polynômes $P$ vérifiant les conditions (eqdefadeux). Par ailleurs, si $P \in \mathscr{A}_p$ alors $P$ a le même degré par rapport à chacune des variables $X_1,   \ldots, X_p$. Bien entendu la définition de $\mathscr{A}_p$ dépend aussi de la parité de $A(n+1)$, mais on ne reflète pas cette dépendance pour ne pas alourdir la notation.

Nous pouvons maintenant énoncer notre résultat principal.[^4]

**Théorème 4**. *Soient $n \geq 0$ et $A, p \geq 1$ des entiers, avec $n$ pair. Soit $P \in \mathscr{A}_p$ de degré $\leq A(n+1)-2$ par rapport à chacune des variables. Alors la série $$\label{eq021}
\sum_{k_1 \geq  \ldots \geq   k_p \ge 1}
\frac{P(k_1, \ldots, k_p)}{(k_1)_{n+1}^{A} \ldots (k_p)_{n+1}^{A} }$$ est une combinaison linéaire, à coefficients rationnels, de produits de la forme $$\zeta(s_1) \ldots  \zeta(s_{q}) \zeta^{{\rm as}}(s'_{1}, \ldots, s'_{q'})$$ avec $$\label{eqcondithconj1}
\left\{
\begin{array}{l}
q, q' \geq 0   \mbox{ entiers tels que } 2q+q' \leq p, \\
s_1, \ldots, s_q, s'_1, \ldots, s'_{q'} \mbox{ entiers impairs } \geq 3, \\
s_i \leq 2A-1  \mbox{ pour tout } i \in \{1,\ldots, q\}, \\
s'_i \leq A  \mbox{ pour tout } i \in \{1,\ldots, q'\}.
\end{array}
\right.$$*

La dissymétrie entre $s_1, \ldots, s_q$ d'une part, et $s'_1, \ldots, s'_{q'}$ d'autre part, dans la conclusion de cet énoncé sera commentée plus loin (juste après l'énoncé du théorème 6).

Il est important de bien visualiser l'ensemble des produits de polyzêtas qui apparaissent dans ce théorème. Par exemple, lorsque $q'=0$ le polyzêta antisymétrique $\zeta^{{\rm as}}(s'_{1}, \ldots, s'_{q'})$ vaut 1 (conformément à la convention évoquée au paragraphe 2.1), et on obtient un produit de valeurs de $\zeta$ en des entiers impairs. Lorsque $q=q'=0$, ce produit est vide et on obtient 1.

Si $p=1$, le théorème 4 affirme que (eq021) est une combinaison linéaire de $1$ et des $\zeta(s)$ pour $s$ impair tel que $3 \leq s \leq A$ : on retrouve le théorème 1, c'est-à-dire le phénomène de symétrie lié aux séries hypergéométriques (très) bien équilibrées en profondeur $1$.

Si $p=2$, on obtient exactement le théorème 3 énoncé dans l'introduction.

Si $p=3$, ce théorème affirme que la série est une combinaison linéaire, à coefficients rationnels :

-   de produits d'au plus deux valeurs de $\zeta$ en des entiers impairs $\geq 3$,

-   de polyzêtas antisymétriques convergents $\zeta^{{\rm as}}(s_1, s_2)$ avec $s_1, s_2 \geq 3$ impairs,

-   de polyzêtas antisymétriques convergents $\zeta^{{\rm as}}(s_1, s_2, s_3)$ avec $s_1, s_2, s_3 \geq 3$ impairs.

En profondeur $p \geq 4$, des termes tels que $q \geq 1$ et $q' \geq 2$ peuvent apparaı̂tre : il semble que la série obtenue ne soit pas toujours la somme d'un polynôme en valeurs $\zeta(s)$ (avec $s$ impair) et d'une combinaison linéaire de polyzêtas antisymétriques $\zeta^{{\rm as}}
(s_1, \ldots, s_q)$ avec $s_1, \ldots, s_q$ impairs.

À l'inverse, on peut affaiblir la conclusion du théorème 4 en disant que la série est un polynôme (à coefficients rationnels) en les polyzêtas antisymétriques convergents $\zeta^{{\rm as}}(s_1, \ldots, s_q)$ avec $1 \leq q \leq p$ et $s_1, \ldots , s_q \geq 3$ impairs tels que $s_1 +\ldots + s_q \leq pA$.

Lorsque $A \leq 2$, on a forcément $q'=0$ pour tous les produits qui apparaissent, ce qui fournit le corollaire suivant :

**Corollaire 2**. *Sous les hypothèses du théorème 4, si $A \leq 2$ alors la série (eq021) est un polynôme en $\zeta(3)$ à coefficients rationnels.*

Le théorème 4 contient, par exemple, le cas particulier suivant :

**Corollaire 3**. *Soient $n, r, t, \varepsilon\geq 0$ et $A,p \geq 1$ des entiers, avec $n$ pair, tels que $$\varepsilon\equiv (A+1)(n+1) +1  \bmod 2$$ et $$\varepsilon+ (4r+2)p + 2t \leq (A-1)(n+1) + 4r.$$ Alors la série convergente $$\label{eq:seriecorollaire}
\sum_{k_1 \geq \ldots \geq  k_p \geq 1}
\bigg[\prod_{i=1} ^p (k_i + \frac{n}{2})\bigg]^{\varepsilon}
 \frac{ \displaystyle  \bigg[ \prod_{1 \leq i < j \leq p}  (k_i-k_j-r)_{2r+1} (k_i+k_j+n-r)_{2r+1} \bigg]
 \bigg[ \prod_{i=1} ^p (k_i-t)_{2t+n+1}   \bigg]  }{(k_1)_{n+1}^{A} \ldots  (k_p)_{n+1}^{A} }$$ est une combinaison linéaire comme celles du théorème 4.*

Un exemple d'application de ce corollaire est la série suivante (dans laquelle on prend $t=0$ et les symboles de Pochhammer $(k_i)_{n+1}$ se simplifient avec ceux du dénominateur) : $$\begin{gathered}
\label{eq:exempleinteressant}
\sum_{k_1\ge k_2\ge k_3\ge 1}\big(k_1+\frac12\big)\big(k_2+ \frac12\big)\big(k_3+\frac12\big)
\\
\times \frac{(k_1-k_2)(k_2-k_3)(k_1-k_3)
(k_1+k_2+1)(k_1+k_3+1)(k_2+k_3+1)}{(k_1)_2^4\;(k_2)_2^4\;(k_3)_2^4}
\\
= -\frac{1}{4} - \zeta(3) + \frac14 \,\zeta(5) + \zeta(3)^2 -\frac14 \,\zeta(7).
\end{gathered}$$

Dans d'éventuelles applications diophantiennes (voir §2.4), on pourrait prendre $\varepsilon$ égal à 0 ou 1, de telle sorte que sa contribution asymptotique (pour $n$ grand) serait négligeable. Le problème est de bien choisir les paramètres $r$ et $s$ en fonction de $n$, ou encore d'imaginer d'autres polynômes $P$ auxquels on pourrait appliquer le théorème 4.

On pourrait chercher à obtenir un analogue du théorème 4 dans lequel seuls des entiers $s_i$ et $s'_i$ *pairs* apparaı̂traient. Un tel énoncé correspondrait peut-être à des polynômes $P$ invariants sous l'action de ${\mathfrak S}_p$, à des polyzêtas *symétriques* (voir la fin du paragraphe 2.1), ou à des valeurs de polylogarithmes en un point $z  = -1$ (c'est-à-dire à un signe, dépendant de $k_1$, ..., $k_p$, qui multiplierait la fraction rationnelle que l'on somme).

Toujours en vue d'une éventuelle application diophantienne, il serait utile d'avoir un contrôle sur le dénominateur des coefficients qui interviennent dans l'écriture de (eq021) comme combinaison linéaire de polyzêtas. Lorsque $P = n!^{Ap} \widetilde P$ où $\widetilde P$ est un polynôme à coefficients entiers, on peut supposer dans le théorème 4 que $\textup{d}_n ^{Ap}$ est un dénominateur commun des coefficients de la combinaison linéaire (où $\textup{d}_n$ est le ppcm des entiers 1, 2, ..., $n$ ; ceci sera démontré au paragraphe (subsecdenompreuve)). Dans certains autres cas, la présence de symboles de Pochhammer dans la définition de $P$ permet d'obtenir un tel dénominateur, comme c'est le cas habituellement en profondeur 1. Étant donné un polynôme $P$ particulier, il n'est pas difficile de déduire un tel résultat du théorème 6 ci-dessous (il suffit d'adapter le lemme 1 qui figure au paragraphe (subsecdenompreuve)). En outre, il serait intéressant de savoir si une *conjecture des dénominateurs* analogue à celle démontrée dans [@KR] existe.

## Liens avec les séries hypergéométriques issues de systèmes de racines

Lorsque l'on ne précise pas la forme du polynôme $P(X_1,X_2,\ldots, X_p)\in\mathbb{Q}[X_1, X_2, \ldots, X_p]$ au numérateur de (eq012), nos séries multiples peuvent s'exprimer comme combinaisons linéaires à coefficients rationnels de séries hypergéométriques multiples de Lauricella. Lorsque $p=1$, la série (eq:seriecorollaire) considérée au corollaire 3 est une série simple hypergéométrique *very well-poised*.

Il est donc naturel de se demander si, pour $p \ge 2$, la série multiple (eq:seriecorollaire) correspond à l'une ou l'autre des généralisations de *well-poisedness* en dimension supérieure, qui sont liées aux systèmes de racines $C_n$, $D_n$ ou $BC_n$ (voir par exemple [@humphreys] pour les définitions). On peut faire les remarques suivantes. Dans [@schlosser], une série hypergéométrique multiple est dite de type $C_n$ si le facteur $$\label{eq:cn}
\Big(\prod_{1\le i<j\le n} (k_i-k_j+x_i-x_j)(k_i+k_j+x_i+x_j) \Big)
\Big(\prod_{i=1}^n (k_i+x_i)\Big)$$ est présent, la sommation étant sur les $k_1 \ge 0, k_2\ge 0, \ldots, k_n\ge 0$, les $x_j$ étant des paramètres. Elle est dite de type $D_n$ si le facteur $$\label{eq:dn}
\prod_{1\le i<j\le n} (k_i-k_j+x_i-x_j)(k_i+k_j+x_i+x_j)$$ est présent mais pas le facteur $\prod_{i=1}^n (k_i+x_i)$. Le type $C_n$ est donc une des généralisations possibles des séries *very well-poised*, tandis que le type $D_n$ généralise les séries qui sont *well-poised* mais pas *very well-poised*. Cependant, aucune de ces définitions n'impose de propriété de symétrie sur le sommande, alors que dans tous les énoncés obtenus ici les propriétés de symétrie sont cruciales : des exemples (faciles à calculer grâce à [@CFRweb]) permettent facilement de voir qu'on ne peut pas remplacer, dans nos résultats, l'hypothèse de symétrie par une hypothèse de divisibilité par un facteur du type (eq:cn) ou (eq:dn).

Par exemple, dans le corollaire 3 ci-dessus, pour $r=0$, le terme de la série $p$-uple (eq:seriecorollaire) est de type $C_p$ lorsque $\varepsilon=1$ et de type $D_p$ lorsque $\varepsilon=0$, avec $x_i=n/2+1$. La série triple (eq:exempleinteressant) est, quant à elle, de type $C_p$, avec $x_i=3/2$. Cependant, dans ces deux cas, notre sommation porte sur $k_1 \ge k_2\ge \cdots \ge k_p\ge 1$ ce qui, comme on va maintenant le voir, produit une très grosse différence sur la nature des polyzêtas qui apparaissent. En effet, en modifiant la sommation dans (eq:exempleinteressant), on obtient l'évaluation d'une série de type $C_3$ : $$\begin{gathered}
\label{eq:exempleinteressantbis}
\sum_{k_1, k_2, k_3\ge 1}\big(k_1+\frac12\big)\big(k_2+ \frac12\big)\big(k_3+\frac12\big)
\\
\times \frac{(k_1-k_2)(k_2-k_3)(k_1-k_3)
(k_1+k_2+1)(k_1+k_3+1)(k_2+k_3+1)}{(k_1)_2^4\;(k_2)_2^4\;(k_3)_2^4}
= 0
\end{gathered}$$ puisque le sommande est changé en son opposé par l'échange des indices $k_1 \leftrightarrow k_2$. Cette remarque vaut aussi pour la somme de type $D_3$ : $$\sum_{k_1, k_2, k_3\ge 1}
\frac{(k_1-k_2)(k_2-k_3)(k_1-k_3)
(k_1+k_2+1)(k_1+k_3+1)(k_2+k_3+1)}{(k_1)_2^4\;(k_2)_2^4\;(k_3)_2^4}
= 0.$$

Le choix de l'ensemble de sommation des séries est donc crucial afin d'obtenir des résultats non triviaux à partir de séries présentant les symétries $C_n$ et $D_n$. Par ailleurs, on peut remarquer que ces deux symétries ne tiennent finalement que très peu compte de la forme des sommandes des séries telles que (eq:seriecorollaire). Michael Schlosser nous a fait remarquer que ces séries présentent en fait une symétrie proche du type $BC_n$, qui tient compte de la présence de facteurs Pochhammer et dont l'étude est toute récente (voir [@coskun]). Les symétries issues des divers systèmes de racines ont donc un grand intérêt dans l'étude diophantienne des polyzêtas et on peut espérer qu'elles puissent jouer un rôle de plus en plus important à l'avenir.

## Applications diophantiennes éventuelles

Pour tout entier $A \geq 1$, notons ${\mathscr{F}}_A$ le sous-$\mathbb Q$-espace vectoriel de $\mathbb R$ engendré par 1 et les $\zeta(s)$, pour $s$ entier impair tel que $3 \leq s \leq A$. Les minorations suivantes sont essentiellement les seules connues (voir par exemple [@SFBou] pour un survol) : $$\label{eqminodim}
\begin{cases}
\dim {\mathscr{F}}_3 = 2 \quad \mbox{ \cite{Apery}}
\\
\dim {\mathscr{F}}_{145} \geq 3 \quad \mbox{ (\cite{Zudilincentqc}, voir aussi \cite{BR})}
\\
\dim {\mathscr{F}}_A \geq \frac{1 - o(1)}{1 + \log 2} \log A \quad \mbox{ (\cite{BR}, \cite{RivoalCRAS})}.
\end{cases}$$

Pour $A \geq 1$ et $p \geq 1$, notons ${\mathscr{E}}_{A, p}$ le sous-$\mathbb Q$-espace vectoriel de $\mathbb R$ engendré par les produits $\zeta(s_1) \ldots  \zeta(s_{q}) \zeta^{{\rm as}}(s'_{1}, \ldots, s'_{q'})$ satisfaisant aux conditions (eqcondithconj1) énoncées dans le théorème 4. L'intérêt de ce théorème est justement de fournir des séries qui appartiennent à ${\mathscr{E}}_{A, p}$, et qui pourraient permettre de minorer la dimension de cet espace.

Pour $p= 1$ on a simplement ${\mathscr{E}}_{A, 1} = {\mathscr{F}}_A$. Pour $p \geq 2$, l'inclusion ${\mathscr{F}}_{2A-1} \subset {\mathscr{E}}_{A, p}$ permet d'obtenir, à partir de (eqminodim), des minorations de $\dim {\mathscr{E}}_{A, p}$. On peut espérer que le théorème 4 (ou le corollaire 3) conduisent à des minorations plus fines de $\dim {\mathscr{E}}_{A, p}$, qui constitueraient de nouveaux résultats diophantiens. Par exemple, peut-être peut-on obtenir une minoration de la forme $\dim {\mathscr{E}}_{A, p} \geq (c(p)-o_p(1)) \log(A)$, où $o_p(1)$ est une suite qui dépend de $p$ et $A$ et tend vers 0 quand $A$ tend vers l'infini (quelle que soit la valeur, fixée, de $p$), et $c(p)$ est une fonction de $p$ seulement. Ceci serait nouveau à condition qu'on ait $c(p) > \frac{1}{1 + \log 2}$ (ce que l'on peut espérer, notamment si $p$ est grand).

Par ailleurs, si on arrivait à montrer que $\dim {\mathscr{E}}_{2, p} \geq 3$ pour un certain $p$, on obtiendrait que $\zeta(3)$ n'est pas quadratique. Si cette dimension pouvait être arbitrairement grande, cela donnerait la transcendance de $\zeta(3)$. Malheureusement, les contraintes de symétrie imposées au polynôme $P$ dans le théorème 4 semblent trop draconiennes pour qu'on puisse aboutir à un résultat aussi spectaculaire (voir à ce propos [@SFHoffman], où des propriétés de symétrie plus faibles sont démontrées sous des hypothèses moins restrictives). Cependant, l'une des motivations principales de cet article est de montrer que l'algorithme de [@CFRalgo] permet de deviner des propriétés, comme celles démontrées ici, de disparition de polyzêtas. La structure de la preuve du théorème 4 devrait pouvoir être utilisée pour démontrer d'autres résultats analogues, dont les applications diophantiennes pourraient être plus faciles.

# Régularisation des séries divergentes

## Rappels

Dans toute la suite, on note $H_N$ la somme harmonique définie par $$H_N = 1 + \frac12 + \frac13 + \ldots + \frac{1}{N}.$$ La proposition suivante a été démontrée par Racinet (voir le Corollaire 2.1.8 de [@RacinetIHES]), en suivant des travaux de Boutet de Monvel.

**Proposition 1**. *Soient $p \geq 0$ et $s_1, \ldots, s_p \geq 1$. Alors il existe un unique polynôme $Q$ tel que, pour tout $\varepsilon> 0$, on ait quand $N$ tend vers $+\infty$ : $$\sum_{N \geq k_1 > \ldots > k_p \geq 1}
\frac{1}{k_1 ^{s_1} \ldots k_p ^{s_p}} = Q(H_N) + \mathcal{O}_\varepsilon(N^{-1+\varepsilon});$$ on note alors $\zeta _*(s_1,\ldots, s_p)$ le coefficient constant de $Q$, c'est-à-dire sa valeur en 0.*

Cette proposition définit les *valeurs régularisées* $\zeta _*(s_1,\ldots, s_p)$ des séries divergentes $$\sum_{ k_1 > \ldots >  k_p \geq 1}
\frac{1}{k_1 ^{s_1} \ldots k_p ^{s_p}}$$ lorsque $s_1 =1$. Dès que $s_1 \geq 2$, on a simplement $\zeta _*(s_1,\ldots, s_p) = \zeta (s_1,\ldots, s_p)$ et le polynôme $Q$ est constant.

Il s'agit de la régularisation relative au produit nommé *stuffle* (voir [@MiW]), avec la convention $\zeta _*(1) = 0$. Il existe une autre forme de régularisation, liée au produit shuffle, et utilisée dans [@CFRalgo] ; mais nous n'en aurons pas besoin ici.

Les valeurs régularisées $\zeta _*(s_1,\ldots, s_p)$ peuvent se calculer de manière algorithmique ; ce sont des combinaisons linéaires à coefficients rationnels de polyzêtas.

Nous aurons aussi besoin de la définition suivante. On appelle *polyzêta antisymétrique régularisé* la combinaison linéaire suivante de polyzêtas régularisés, pour $p \geq 1$ et $s_1, \ldots, s_p \geq 1$ entiers : $$\zeta _* ^{{\rm as}}(s_1, \ldots, s_p) =  \sum_{\sigma\in\mathfrak{S}_p} \varepsilon_{\sigma} \zeta _*(s_{\sigma(1)}, \ldots, s_{\sigma(p)}) .$$ Lorsque $s_1 \geq 2$, on a $\zeta _* ^{{\rm as}}(s_1, \ldots, s_p) = \zeta^{{\rm as}}(s_1, \ldots, s_p)$ : on retrouve les polyzêtas antisymétriques convergents. Lorsque $p=0$, on pose $\zeta _* ^{{\rm as}}(s_1, \ldots, s_p) = \zeta  (s_1, \ldots, s_p) = 1$.

## Énoncé avec régularisation des divergences

L'une des motivations principales pour considérer des polyzêtas régularisés est qu'ils permettent de rendre la théorie plus complète, et en tout cas plus élégante. Nous en donnons ici une illustration : pour démontrer le théorème 4 (qui concerne seulement des séries convergentes), nous allons utiliser le résultat suivant (dans lequel des divergences logarithmiques sont autorisées, et régularisées).[^5]

**Théorème 5**. *Supposons $n$ pair. Soit $P \in \mathscr{A}_p$ de degré $\leq A(n+1)-1$ par rapport à chacune des variables. Alors il existe un polynôme $Q_P$ tel que, pour tout $\varepsilon> 0$, on ait quand $N$ tend vers $+\infty$ : $$\label{eq1}
 \sum_{N \geq k_1 \geq \ldots \geq k_p \geq 1}
\frac{P(k_1,\ldots,k_p)}{(k_1)_{n+1}^A \ldots (k_p)_{n+1}^A}
= Q_P (H_N) + \mathcal{O}_\varepsilon(N^{-1+\varepsilon}),$$ et tel que $Q_P(0)$ soit une combinaison linéaire, à coefficients rationnels, de produits de la forme $$\label{eq998}
\zeta _*(s_1) \ldots  \zeta _*(s_{q}) \zeta _* ^{{\rm as}}(s'_{1}, \ldots, s'_{q'})$$ avec $$\left\{
\begin{array}{l}
q, q' \geq 0 \mbox{ entiers tels que } 2q+q' \leq p \\
s_1, \ldots, s_q , s'_1, \ldots, s'_{q'} \mbox{ entiers impairs } \geq 1 \\
s_i \leq 2A-1  \mbox{ pour tout } i \in \{1,\ldots, q\}\\
s'_i \leq A  \mbox{ pour tout }  i \in \{1,\ldots, q'\}.
\end{array}
\right.$$*

Comme $\zeta _*(1) = 0$, on peut se restreindre aux produits (eq998) tels que $s_1, \ldots, s_{q} \geq 3$.

Si dans ce théorème on suppose que $P$ est de degré $\leq A(n+1)-2$ par rapport à chacune des variables, alors (eq1) converge quand $N$ tend vers $+\infty$, donc le polynôme $Q_P$ est constant (égal à $Q_P(0)$). Pour déduire le théorème 4 du théorème 5, il suffit donc de démontrer que le produit (eq998) ne peut apparaı̂tre que si $s'_1, \ldots, s'_{q'} \geq 3$. C'est l'objet du paragraphe 4.4; pour y parvenir, on utilise en fait une version plus précise du théorème 5, que nous allons formuler grâce au développement en éléments simples.

# Décomposition en éléments simples

## Notations et actions de groupes

Soit $P(k_1,\ldots,k_p)$ un polynôme de degré $\leq A(n+1)-1$ par rapport à chacune des variables, à coefficients rationnels. La décomposition en éléments simples de la fraction rationnelle $$\label{eq041}
R(k_1,\ldots, k_p) = \frac{P(k_1,\ldots, k_p)}{(k_1)_{n+1}^A \ldots (k_p)_{n+1}^A}$$ s'écrit $$\label{eq2}
R(k_1,\ldots, k_p) = \sum_{\tiny {\begin{array}{c} 0 \leq j_1, \ldots, j_p \leq n \\ 1 \leq s_1, \ldots, s_p \leq A \end{array}}}
\frac{C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]}{(k_1+j_1)^{s_1} \ldots (k_p+j_p)^{s_p}}$$ avec des rationnels $C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]$. L'unicité de ce développement montre que $P$ appartient à $\mathscr{A}_p$ si, et seulement si, on a : $$\label{eq3}
\left\{
\begin{array}{l}
C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]= (-1)^{s_i+1} C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots,  j_{i-1}, n-j_i, j_{i+1}, \ldots, j_p\end{matrix}\,\bigg]\mbox{ pour tout } i \in \{1,\ldots, p\}\\
\\
C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]= \varepsilon_\gamma C\bigg[\,\begin{matrix} s_{\gamma(1)}, \ldots , s_{\gamma(p)} \\ j_{\gamma(1)},\ldots, j_{\gamma(p)} \end{matrix}\,\bigg]\mbox{ pour tout } \gamma \in {\mathfrak S}_p.
\end{array}
\right.$$

Donnons maintenant une interprétation algébrique (en termes de groupes opérant sur des ensembles) de cette situation, qui sera utile dans les preuves.

Pour $\varepsilon\in \mathbb Z/ 2 \mathbb Z$ (où on voit toujours $\mathbb Z/ 2 \mathbb Z$ comme étant le groupe multiplicatif $\{-1, 1\}$) et $j \in \{0,\ldots, n\}$, on pose : $$\left\{
\begin{array}{l}
\varepsilon\cdot j =j \mbox{ si } \varepsilon=1 , \\
\varepsilon\cdot j =n-j \mbox{ si } \varepsilon= -1.
\end{array}
\right.$$ Ceci définit une action de $\mathbb Z/ 2 \mathbb Z$ sur $\{0,\ldots, n\}$. De manière diagonale, on peut alors définir une action de $(\mathbb Z/ 2 \mathbb Z)^p$ sur $\{0,\ldots, n\}^p$ en posant : $$(\varepsilon_1,\ldots, \varepsilon_p) \cdot (j_1,\ldots, j_p) = (\varepsilon_1  \cdot j_1, \ldots,  \varepsilon_p \cdot j_p).$$ En outre, on considère l'action triviale de $(\mathbb Z/ 2 \mathbb Z)^p$ sur $\{1,\ldots, A\}^p$, et on en déduit une action de $(\mathbb Z/ 2 \mathbb Z)^p$ sur $\{0,\ldots, n\}^p \times \{1,\ldots, A\}^p$ définie par : $$(\varepsilon_1,\ldots, \varepsilon_p) \cdot (j_1,\ldots, j_p, s_1,\ldots, s_p) = (\varepsilon_1  \cdot j_1, \ldots,  \varepsilon_p \cdot j_p, s_1,\ldots, s_p).$$ Par ailleurs, le groupe ${\mathfrak S}_p$ agit par permutation des facteurs sur $(\mathbb Z/ 2 \mathbb Z)^p$, sur $\{0,\ldots, n\}^p$ et sur $\{1,\ldots, A\}^p$ (donc agit aussi sur $\{0,\ldots, n\}^p \times \{1,\ldots, A\}^p$). On en déduit une action du produit semi-direct $(\mathbb Z/ 2 \mathbb Z)^p\rtimes{\mathfrak S}_p$ sur $\{0,\ldots, n\}^p \times \{1,\ldots, A\}^p$; et (eq3) signifie que $C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]$ est constant (au signe près) sur chaque orbite (et ce signe est bien déterminé en fonction de la parité des $s_i$).

**Remarque 1**. *Le sous-groupe d'indice 2 de $(\mathbb Z/ 2 \mathbb Z)^p\rtimes{\mathfrak S}_p$ formé par les $(\varepsilon_1,\ldots, \varepsilon_p,
\gamma)$ tel que $\varepsilon_1 \ldots \varepsilon_p = 1$ est d'ordre $2^{p-1} p!$ ; pour $p=5$, c'est exactement le groupe de Rhin-Viola [@RV3] pour $\zeta(3)$. Nous n'avons trouvé aucune explication à cette coı̈ncidence.*

## Énoncé régularisé en termes d'éléments simples

On va déduire les théorèmes 4 et 5 du résultat suivant :

**Théorème 6**. *Supposons $n$ pair. Soient $j_1, \ldots, j_p \in \{0,\ldots, n\}$ et $s_1,\ldots,s_p  \geq 1$. Alors il existe un polynôme $Q_{\underline j, \underline s}$ tel que, pour tout $\varepsilon> 0$, on ait quand $N$ tend vers $+\infty$ : $$\begin{gathered}
\sum_{N \geq k_1 \geq \ldots \geq k_p \geq 1}
 \sum_{\sigma \in {\mathfrak S}_p}
 \sum_{(\varepsilon_1,\ldots,\varepsilon_p)\in (\mathbb Z/ 2 \mathbb Z)^p}
\varepsilon_\sigma  \varepsilon_1^{s_1+1} \ldots \varepsilon_p ^{s_p+1}
\frac{1}{(k_{\sigma(1)} + \varepsilon_1 \cdot j_1)^{s_1} \ldots (k_{\sigma(p)} + \varepsilon_p \cdot j_p)^{s_p}}
\\
= Q_{\underline j, \underline s}(H_N) + \mathcal{O}_\varepsilon(N^{-1+\varepsilon}),
\label{eq4}
\end{gathered}$$ et tel que $Q_{\underline j, \underline s}(0)$ soit une combinaison linéaire, à coefficients rationnels, de produits de la forme $$\label{eq999}
\zeta _*(s'_1) \ldots  \zeta _*(s'_{q'}) \zeta _* ^{{\rm as}}(s''_{1}, \ldots, s''_{q''})$$ avec, pour chaque produit de cette forme : $$\left\{
\begin{array}{l}
q' ,q'' \geq 0   \mbox{ entiers tels que } 2q'+q'' \leq p \\
s'_1, \ldots, s'_{q'}, s''_{1}, \ldots, s''_{q''} \geq 1 \mbox{  impairs } \\
\mbox{il existe } \sigma \in {\mathfrak S}_p\mbox{ tel que : }\\
\quad \quad \bullet \, \, s'_i \leq s_{\sigma(i)} + s_{\sigma(i+q')} \mbox{ pour tout } i \in \{1,\ldots, q'\}\\
\quad \quad \bullet \, \, s''_\ell  = s_{\sigma(\ell+2q')} \mbox{ pour tout } \ell \in \{1,\ldots, q''\}.
\end{array}
\right.$$ De plus, pour la combinaison linéaire construite dans la preuve :*

-   *Les coefficients de la combinaison linéaire peuvent être calculés de manière explicite et ils admettent $\textup{d}_n ^{s_1 + \ldots + s_p}$ pour dénominateur commun.*

-   *Le coefficient du produit (eq999) ne dépend que des $j_{\ell}$ et des $s_\ell$ pour $\ell \in \{ \sigma(2q' + q'' + 1), \ldots, \sigma(p)\}$.*

Dans ce théorème, et dans toute la suite, on identifie le groupe $\mathbb Z/ 2 \mathbb Z$ à $\{-1, 1\}$ : pour $\varepsilon\in \mathbb Z/ 2 \mathbb Z$ et $s$ entier, on a $\varepsilon^s = 1$ si $s$ est pair et $\varepsilon^s = -1$ si $s$ est impair.

Les contraintes sur les produits (eq999) signifient que les polyzêtas $\zeta _*(s'_i)$ de profondeur 1 apparaissent par une sorte de concaténation de deux indices : c'est pourquoi ils peuvent apparaı̂tre jusqu'à $s'_i = 2A - 1$ dans les théorèmes 4 et 5. C'est aussi la raison pour laquelle $q'$ apparaı̂t avec un facteur 2 dans la majoration $2q'+q'' \leq p$. En revanche, les $s''_\ell$ de (eq999) sont directement une sous-famille du $p$-uplet initial $(s_1, \ldots,  s_p)$ (à permutation près). La remarque qui termine l'énoncé du théorème 6 signifie que le coefficient de (eq999) ne dépend ni des $s_\ell$ de cette sous-famille ni de ceux qui contrôlent par concaténation les $s'_i$, mais seulement des autres (s'il y en a ; sinon, c'est que le coefficient ne dépend ni de $s_1, \ldots, s_p$ ni de $j_1, \ldots, j_p$).

Si la profondeur $p$ est inférieure ou égale à 3, les produits (eq999) sont des produits de valeurs de zêta en des entiers impairs, ou bien des polyzêtas antisymétriques de profondeur 2 ou 3. On va maintenant expliciter, à titre d'exemple, le coefficient d'un tel polyzêta antisymétrique $\zeta _* ^{{\rm as}}(s''_{1}, \ldots,
s''_{q''})$ dans la combinaison linéaire (eq4). La preuve de ce résultat sera donnée en même temps que celle du théorème 6, aux paragraphes 5.2 et 5.3.

Si $p=2$, un tel polyzêta ne peut apparaı̂tre (avec un coefficient non nul) que si $s_1$ et $s_2$ sont impairs ; dans ce cas, sa contribution est toujours $4 ( \zeta(s_1, s_2) - \zeta(s_2, s_1))$.

Supposons maintenant que $p=3$. Alors des polyzêtas antisymétriques de profondeur 2 et 3 peuvent apparaı̂tre. En profondeur 3, la seule contribution possible est dans le cas où $s_1$, $s_2$ et $s_3$ sont impairs ; elle vaut $$8 \zeta _* ^{{\rm as}}(s_1, s_2, s_3) = 8 \sum_{\sigma \in \mathfrak{S}_3} \varepsilon_\sigma \zeta _*(s_{\sigma(1)},s_{\sigma(2)}, s_{\sigma(3)}).$$ Explicitons maintenant la contribution des polyzêtas antisymétriques de profondeur 2 (qui correspondent à $q'=0$ et $q'' = 2$). C'est une combinaison linéaire des polyzêtas $\zeta _*(s_{i+1}, s_{i+2}) - \zeta _*(s_{i+2}, s_{i+1})$ pour $i = 1, 2, 3$ (en interprétant les indices modulo 3, par exemple $s_4 = s_1$). Ce polyzêta antisymétrique n'apparaı̂t que si $s_{i+1}$ et $s_{i+2}$ sont impairs. Dans ce cas, son coefficient est $$-4 \Big( \sum_{\ell = 1}^{j_i} \frac{1}{\ell^{s_i}} +  \sum_{\ell = 1}^{n-j_i} \frac{1}{\ell^{s_i}} \Big)$$ si $s_i$ est impair. Si $s_i$ est pair et $j_i \geq n/2$, c'est $$-4 \Big( \sum_{\ell = n-j_i+1}^{j_i} \frac{1}{\ell^{s_i}}  \Big).$$ Enfin, si $s_i$ est pair et $j_i \leq n/2$, c'est $$+4 \Big( \sum_{\ell = j_i+1}^{n-j_i} \frac{1}{\ell^{s_i}}  \Big).$$ Dans chacun de ces trois cas, on voit que ce coefficient ne dépend pas de $s_{i+1}$, $s_{i+2}$, $j_{i+1}$, $j_{i+2}$, mais seulement de $s_{i}$ et de $j_{i}$ (comme énoncé dans le théorème 6).

Pourrait-on utiliser ces expressions explicites (en profondeur 2 ou 3) pour trouver des polynômes $P$ pour lesquels la partie "polyzêtas antisymétriques" de la combinaison linéaire du théorème 4 est nulle ? Pour ces polynômes, cette combinaison linéaire serait donc un polynôme en valeurs de $\zeta$ en des entiers impairs.

## Liens entre les théorèmes 5 et 6

Comme on va le voir, le théorème 6 est une forme plus précise du théorème 5.

Pour déduire le théorème 5 du théorème 6, on procède comme suit (il s'agit de la même stratégie que celle détaillée au paragraphe 4.4 ci-dessous). Étant donné $P \in \mathscr{A}_p$, on utilise le développement en éléments simples du paragraphe 4.1 et on regroupe les termes qui correspondent à une même orbite sous l'action du groupe $(\mathbb Z/ 2 \mathbb Z)^p\rtimes{\mathfrak S}_p$ (voir §4.1). Le fait que $P \in \mathscr{A}_p$ signifie (voir également §4.1) que tous ces termes apparaissent avec le même coefficient, au signe près (et ce signe est donné par la signature). On est donc ramené à évaluer la somme sur chaque orbite, qui est exactement de la forme (eq4): il suffit d'appliquer le théorème 6.

Réciproquement, en mettant au même dénominateur les termes obtenus quand $\sigma$ et $(\varepsilon_1,\ldots,\varepsilon_p)$ varient, on voit que (eq4) est de la forme (eq1) pour un certain polynôme $P  \in \mathscr{A}_p$, de degré $\leq A(n+1)-1$ par rapport à chacune des variables. Ceci prouve que le théorème 5 implique le théorème 6, à condition d'oublier, dans ce dernier, les précisions données en complément.

## Preuve que le théorème 6 implique le théorème 4

Commençons par le point délicat, qui différencie cette preuve de celle du paragraphe 4.3.

Sous les hypothèses du théorème 4, la fraction rationnelle $R$ définie par (eq041) est de degré $\leq -2$ par rapport à chacune de ses variables. Donc $k_1 R(k_1, \ldots, k_p)$ tend vers 0 quand $k_1$ tend vers l'infini, et on obtient en passant à la limite dans (eq2) : $$\sum_{\tiny {\begin{array}{c} 0 \leq j_2, \ldots, j_p \leq  n \\ 1 \leq s_2, \ldots, s_p \leq A  \end{array}}}
\frac{1}{(k_2+j_2)^{s_2} \ldots (k_p+j_p)^{s_p}} \sum_{j_1 = 0} ^n C\bigg[\,\begin{matrix} 1, s_2,  \ldots, s_p\\j_1, j_2, \ldots, j_p\end{matrix}\,\bigg]= 0.$$ Par unicité du développement en éléments simples de la fraction rationnelle nulle, on obtient pour tous $s_2, \ldots, s_p, j_2, \ldots, j_p$ : $$\sum_{j_1 = 0} ^n C\bigg[\,\begin{matrix} 1, s_2,  \ldots, s_p\\j_1, j_2, \ldots, j_p\end{matrix}\,\bigg]= 0.$$ Le même raisonnement, appliqué avec $k_i$ au lieu de $k_1$, montre que pour tout $i \in \{1,\ldots, p\}$ on a : $$\label{eq2pr}
 \sum_{j_i = 0} ^n C\bigg[\,\begin{matrix} s_1, \ldots, s_{i-1}, 1, s_{i+1},  \ldots, s_p\\j_1,  \ldots, j_{i-1}, j_i, j_{i+1}, \ldots,  j_p\end{matrix}\,\bigg]= 0.$$

Une fois ce résultat préliminaire établi, on peut suivre la stratégie résumée au paragraphe 4.3, combinée avec la régularisation des divergences logarithmiques et une étude plus détaillée de l'action du groupe (nécessaire pour utiliser (eq2pr)).

En utilisant le développement en éléments simples (eq2), on voit que la série convergente (eq021) est la limite, quand $N$ tend vers l'infini, de la somme $$\label{eq818}
\sum_{\tiny {\begin{array}{c} 0 \leq j_1, \ldots, j_p \leq  n \\ 1 \leq s_1, \ldots, s_p \leq A  \end{array}}} C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]
\sum_{N \geq k_1 \geq  \ldots \geq   k_p \ge 1}
\frac{1}{(k_1+j_1)^{s_1} \ldots (k_p+j_p)^{s_p}}.$$ Or l'ensemble d'indices $\{0,\ldots, n\}^p \times\{1,\ldots, A\}^p$ est la réunion disjointe des orbites sous l'action du groupe $(\mathbb Z/ 2 \mathbb Z)^p\rtimes{\mathfrak S}_p$ définie au paragraphe 4.1. Etudions la contribution de chaque orbite à cette somme. Fixons $(\underline{j}, \underline{s}) = (j_1, \ldots, j_p, s_1, \ldots, s_p)$, et considérons un point quelconque $(\underline{j'}, \underline{s'}) = (j'_1, \ldots, j'_p, s'_1, \ldots, s'_p)$ de son orbite (notée $\Omega_{\underline{j}, \underline{s}}$). Il existe $\gamma \in {\mathfrak S}_p$ et $(\varepsilon_1, \ldots, \varepsilon_p) \in (\mathbb Z/ 2 \mathbb Z)^p$ tels que $s'_1 = s_{\gamma(1)}$, ..., $s'_p = s_{\gamma(p)}$, $j'_1 = \varepsilon_1 \cdot j_{\gamma(1)}$, ..., $j'_p = \varepsilon_p \cdot j_{\gamma(p)}$. La relation (eq3) donne $$\label{eq820}
C\bigg[\,\begin{matrix} s'_1, \ldots, s'_p\\j'_1, \ldots, j'_p\end{matrix}\,\bigg]= \varepsilon_\gamma  \varepsilon_1^{s_{\gamma(1)}+1} \ldots \varepsilon_p ^{s_{\gamma(p)}+1}  C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg].$$

Comme tout élément $(\underline{j'}, \underline{s'})$ de $\Omega_{\underline{j}, \underline{s}}$ s'écrit ainsi pour exactement $\frac{2^p p!}{{\rm Card}\Omega_{\underline{j}, \underline{s}}}$ éléments $(\varepsilon_1, \ldots, \varepsilon_p, \gamma) \in  (\mathbb Z/ 2 \mathbb Z)^p\rtimes{\mathfrak S}_p$, on voit que la contribution de $\Omega_{\underline{j}, \underline{s}}$ à la somme (eq818) est exactement la somme (eq4), multipliée par $C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]\frac{{\rm Card}\Omega_{\underline{j}, \underline{s}}}{2^p p!}$. D'après le théorème 6, cette contribution s'écrit donc $$\label{eq819}
\frac{{\rm Card}\Omega_{\underline{j}, \underline{s}}}{2^p p!} C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]Q_{\underline{j}, \underline{s}} (H_N) +   \mathcal{O}_\varepsilon(N^{-1+\varepsilon})$$ pour tout $\varepsilon> 0$. Or pour $(\underline{j'}, \underline{s'})  \in \Omega_{\underline{j}, \underline{s}}$, en prenant $(\varepsilon_1, \ldots, \varepsilon_p, \gamma)$ comme ci-dessus, on voit par unicité du polynôme $Q_{\underline{j'}, \underline{s'}}$ que $$Q_{\underline{j'}, \underline{s'}}(X) =  \varepsilon_\gamma  \varepsilon_1^{s_{\gamma(1)}+1} \ldots \varepsilon_p ^{s_{\gamma(p)}+1}    Q_{\underline{j}, \underline{s}} (X).$$ Compte tenu de (eq820), on peut donc écrire (eq819) sous la forme $$\sum_{(\underline{j'}, \underline{s'}) \in \Omega_{\underline{j}, \underline{s}}} \frac{1}{2^p p!} C\bigg[\,\begin{matrix} s'_1, \ldots, s'_p\\j'_1, \ldots, j'_p\end{matrix}\,\bigg]Q_{\underline{j'}, \underline{s'}} (H_N) + \mathcal{O}_\varepsilon(N^{-1+\varepsilon})$$ pour tout $\varepsilon> 0$. Cette écriture de la contribution de $\Omega_{\underline{j}, \underline{s}}$ à (eq818) montre que la somme (eq818) est égale à $$\label{eq817}
 \frac{1}{2^p p!} \sum_{\tiny {\begin{array}{c} 0 \leq j_1, \ldots, j_p \leq  n \\ 1 \leq s_1, \ldots, s_p \leq A  \end{array}}} C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]
 Q_{\underline{j}, \underline{s}} (H_N) + \mathcal{O}_\varepsilon(N^{-1+\varepsilon})$$ pour tout $\varepsilon> 0$. Cette écriture (qui consiste à réécrire (eq818) en moyennant sur chaque orbite, puis en appliquant le théorème 6 à chacune d'elles) est le point crucial qui va permettre maintenant de conclure, en appliquant la relation (eq2pr) démontrée au début du paragraphe.

Comme la somme (eq817) converge vers (eq021) quand $N$ tend vers l'infini, le polynôme $$\label{eq1001}
Q(X) = \frac{1}{2^p p!} \sum_{\tiny {\begin{array}{c} 0 \leq j_1, \ldots, j_p \leq  n \\ 1 \leq s_1, \ldots, s_p \leq A  \end{array}}} C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]
Q_{\underline{j}, \underline{s}} (X)$$ est en fait constant, égal à sa valeur en 0; et cette valeur est exactement la somme (eq021). Donc le théorème 6 montre que (eq021) est une combinaison linéaire, à coefficients rationnels, de produits de la forme $$\label{eq1000}
\zeta _*(s'_1) \ldots  \zeta _*(s'_{q'}) \zeta _* ^{{\rm as}}(s''_{1}, \ldots, s''_{q''})$$ avec, pour chaque produit de cette forme, $q' ,q'' \geq 0$ entiers tels que $2q'+q'' \leq p$, $s'_1, \ldots, s'_{q'}, s''_{1}, \ldots, s''_{q''} \geq 1$ impairs, et $\sigma \in {\mathfrak S}_p$ tel que $s'_i \leq s_{\sigma(i)} + s_{\sigma(i+q')}$ pour tout $i \in \{1,\ldots, q'\}$ et $s''_\ell  = s_{\sigma(\ell+2q')}$ pour tout $\ell \in \{1,\ldots, q''\}$.

Comme $\zeta _*(1) = 0$, on peut supposer que dans un tel produit (eq1000) on a $s'_1, \ldots, s'_{q'} \geq 3$. Si on a aussi $s''_{1}, \ldots, s''_{q''} \geq 3$, alors ce produit fait partie de ceux autorisés dans la conclusion du théorème 4, donc il n'y a rien d'autre à démontrer. Supposons en revanche que $s''_\ell = s_{\sigma(\ell+2q')}=1$ pour un certain $\ell \in \{1,\ldots, q''\}$. D'après les précisions données à la fin du théorème 6, le coefficient du produit (eq1000) dans la décomposition de $Q_{\underline{j}, \underline{s}}(0)$ ne dépend pas de $j_{\sigma(\ell + 2q')}$. D'après (eq1001) et l'égalité (eq2pr) démontrée au début de ce paragraphe (appliquée avec $i = \sigma(\ell+2q')$), ce produit apparaı̂t dans $Q(0)$ avec un coefficient nul, donc ne contribue pas à la somme (eq021).

Ceci termine la preuve du fait que le théorème 6 implique le théorème 4.

Pour démontrer l'assertion sur le dénominateur []{#subsecdenompreuve label="subsecdenompreuve"} des coefficients qui figure à la fin du paragraphe 2.2, il suffit d'appliquer le lemme suivant et de suivre, dans toute la preuve ci-dessus, les dénominateurs des nombres rationnels qui apparaissent.

**Lemme 1**. *Si $P = n!^{Ap} \widetilde P$ où $\widetilde P$ est un polynôme à coefficients entiers, alors $$\textup{d}_n ^{Ap - (s_1+\ldots+s_p)} C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]\in \mathbb Z$$ pour tous $s_1, \ldots, s_p, j_1, \ldots, j_p$.*

Démontrons maintenant ce lemme. Par $\mathbb Z$-linéarité, il suffit de traiter le cas où $P = n!^{Ap} X_1^{r_1} \ldots X_p^{r_p}$ avec $0 \leq r_1, \ldots, r_p \leq A(n+1)-1$. Admettons pour l'instant la propriété suivante en une variable : pour tout $r \in \{0, \ldots, A(n+1)-1\}$ on a $$\label{eqdenomunevar}
\frac{n! ^A k^r}{(k)_{n+1}^A} = \sum_{j=0}^n \sum_{s=1}^A \frac{E_{j,s}^{(r)}}{(k+j)^s}
\mbox{ avec } \textup{d}_n^{A-s} E_{j,s}^{(r)}\in \mathbb Z.$$ Le produit de cette relation, écrite avec $k=k_i$ pour $i \in \{1, \ldots, p\}$, montre que la fraction rationnelle (eq041) peut s'écrire sous la forme (eq2) avec $$\textup{d}_n^{Ap-(s_1+\ldots+s_p)} C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]= \prod_{i=1}^p \textup{d}_n^{A-s_i} E_{j_i,s_i}^{(r_i)}\in \mathbb Z.$$ Ceci termine la preuve du lemme, en admettant la relation (eqdenomunevar).

Démontrons maintenant cette relation. La matrice de passage de la base canonique $(k^r)_{0 \leq r \leq A(n+1)-1}$ à la base formée par les polynômes $(k)_{n+1}^a (k+n+1-\sigma)_{\sigma}$ (pour $0 \leq a \leq A-1$ et $0 \leq \sigma \leq n$) est à coefficients entiers, triangulaire supérieure à diagonale de 1. Donc son inverse l'est aussi ; ceci permet de décomposer le monôme $k^r$ dans la nouvelle base (avec des coefficients entiers). Par $\mathbb Z$-linéarité, on est ramené à décomposer des fractions rationnelles de la forme $\frac{n!^A}{(k)_{n+1}^{A-a-1} (k)_{n+1-\sigma}}$. Pour cela, on utilise la formule suivante : $$\frac{n!  }{(k)_{n+1}} = \sum_{j=0}^n  \frac{H_{n,j}}{k+j} \mbox{ avec } H_{n,j}  \in \mathbb Z.$$ Cette formule (qui est simplement le cas particulier $A=1$, $r=0$ de (eqdenomunevar)) est démontrée par exemple dans le lemme 5 de [@BR]. Il suffit alors de faire le produit cette formule, appliquée $a$ fois sous cette forme et une fois avec $n$ remplacé par $n-\sigma$. Une fois ce produit développé, on utilise (comme dans [@Colmez]) la formule $\frac{1}{(k+j)(k+j')} = \frac{1}{(j'-j)(k+j)} + \frac{1}{(j-j')(k+j')}$ pour $j \neq j'$. Chaque application de cette formule fait apparaı̂tre un dénominateur, qui est un diviseur de $\textup{d}_n$. Après de multiples applications de cette formule, on arrive à une somme de la forme annoncée dans (eqdenomunevar), et le coefficient $E_{j,s}^{(r)}$ est la somme de plusieurs termes qui proviennent tous d'au plus $A-s$ applications de cette formule. Ceci termine la preuve de (eqdenomunevar), donc celle du lemme.

# Démonstration du théorème 6

Dans cette partie, on démontre le théorème 6 par récurrence sur la profondeur. En théorie, l'initialisation (§5.1) et le cœur de la récurrence (§5.4) suffisent ; mais on démontre aussi complètement les cas $p=2$ (§5.2) et $p=3$ (§5.3) pour illustrer et motiver les constructions du paragraphe 5.4.

C'est dans cette partie, et nulle part ailleurs, que l'hypothèse "$n$ est pair" est utilisée (voir la remarque 2 ci-dessous).

## Preuve du théorème 6 en profondeur 1

Quand $p=1$, le théorème 6 concerne des séries de la forme $$\sum_{k=1} ^N \Big(  \frac{1}{(k+j)^s} + \frac{(-1)^{s+1}}{(k+n-j)^s} \Big).$$ Si $s \geq 2$, on voit directement que cette somme vaut $(1+(-1)^{s+1}) \zeta(s) + \rho_{j,s} + \mathcal{O}(\frac{1}{N})$ avec $\textup{d}_n^s \rho_{j,s} \in \mathbb Z$, ce qui démontre le théorème dans ce cas. Sinon, c'est-à-dire si $s=1$, cette somme vaut $2 H_N  +   \rho_{j,s} + \mathcal{O}(\frac{1}{N})$ avec $\textup{d}_n \rho_{j,s} \in \mathbb Z$, ce qui démontre aussi le résultat voulu puisque $\zeta _*(1)=0$.

Le théorème 6 est donc démontré quand $p=1$.

## Preuve du théorème 6 en profondeur 2

Dans ce paragraphe, on suppose $p=2$ et on démontre, par récurrence sur $(j_1,j_2)$, que le théorème 6 est vrai pour tous $s_1, s_2$. L'entier $n$ est fixé dans toute la preuve.

L'initialisation de cette récurrence est le cas où $j_1 = j_2 = \frac{n}{2}$ (puisque $n$ est supposé pair ; voir la remarque 2 ci-dessous). La somme (eq4) est alors nulle si $s_1$ ou $s_2$ est pair ; le résultat du théorème 6 est trivial dans cette situation. On peut donc supposer que $s_1$ et $s_2$ sont impairs. La somme (eq4) vaut alors $4(\tau_{s_1, s_2} - \tau_{s_2, s_1})$, en posant $$\tau_{s_1, s_2} = \sum_{N \geq k_1 \geq k_2 \geq 1} \frac{1}{(k_1 + \frac{n}{2})^{s_1}  (k_2 + \frac{n}{2})^{s_2}}.$$ Or on a $$\begin{aligned}
\tau_{s_1, s_2}
&=&  \sum_{N + \frac{n}{2} \geq \ell_1 \geq \ell_2 \geq  \frac{n}{2} + 1} \frac{1}{\ell_1^{s_1} \ell_2^{s_2}}\\
&=&  \sum_{N + \frac{n}{2} \geq \ell_1 > \ell_2 \geq  1} \frac{1}{\ell_1^{s_1} \ell_2^{s_2}}
+ \sum_{N + \frac{n}{2} \geq \ell  \geq  1} \frac{1}{\ell^{s_1+s_2}}
- \sum_{\ell_2 = 1} ^{n/2}
\frac{1}{\ell_2^{s_2}} \sum_{\ell_1 = \ell_2} ^{N + \frac{n}{2}} \frac{1}{\ell_1^{s_1}}.
\end{aligned}$$ La proposition 1 fournit un polynôme $Q$ tel que, pour tout $\varepsilon> 0$, on ait quand $N$ tend vers l'infini : $$\tau_{s_1, s_2}  = Q(H_N) +  \mathcal{O}_\varepsilon(N^{-1+\varepsilon})$$ avec $$Q(0) = \zeta _*(s_1,s_2) + \zeta(s_1+s_2) - \Big( \sum_{\ell_2 = 1} ^{n/2} \frac{1}{\ell_2 ^{s_2}} \Big)  \zeta _*(s_1) + r ,$$ où $\textup{d}_n ^{s_1+s_2} r \in \mathbb Z$ (ceci provient du fait que $Q(H_{N+n/2}) = Q(H_N) +  \mathcal{O}_\varepsilon(N^{-1+\varepsilon})$). Or $\zeta _*(1) = 0$ et $\zeta _*(s_1) = \zeta(s_1)$ pour $s_1 \geq 2$. d́onné que la somme (eq4) vaut $4(\tau_{s_1, s_2} - \tau_{s_2, s_1})$, cela démontre le théorème 6 quand $s_1$ et $s_2$ sont impairs, avec $j_1 = j_2 = n/2$. Cela termine la preuve de l'initialisation de la récurrence.

**Remarque 2**. *Dans cette initialisation, on a supposé que $n$ est pair. C'est le seul endroit dans cet article (avec les initialisations analogues en profondeurs $3$ et $p \geq 4$ aux paragraphes 5.3 et 5.4) où cette hypothèse est utilisée. Si on voulait démontrer les mêmes résultats lorsque $n$ est impair, il suffirait de démontrer cette initialisation dans ce cas. Bien entendu, on ne pourrait plus prendre $j_1 = j_2 = \frac{n}{2}$, donc les calculs seraient plus compliqués. On pourrait par exemple choisir $j_1 = j_2 =0$.*

La suite de la démonstration consiste à établir le résultat suivant pour tous $j_1  \in \{0,\ldots, n-1\}$ et $j_2 \in \{0,\ldots, n\}$ : $$\label{eqrec2}
\left\{
\begin{array}{l}
\mbox{ le th\'eor\`eme \ref{thconj3}   est vrai pour le couple $(j_1, j_2)$, quels que soient  $s_1$ et $ s_2$}, \\
\quad \quad \mbox{ si, et seulement si, }\\
\mbox{il  est vrai pour le couple $(j_1+1, j_2)$, quels que soient  $s_1$ et $ s_2$}.
\end{array}
\right.$$ En effet, supposons (eqrec2) établie. Comme le théorème est vrai pour le couple $(j_1 = n/2, j_2 = n/2)$, il est vrai pour $(j_1, n/2)$ quel que soit $j_1 \in \{1,\ldots, n\}$ en utilisant (eqrec2). Or quand on échange $j_1$ et $j_2$, ainsi que (simultanément)$s_1$ et $s_2$, la somme (eq4) est changée en son opposé. Donc le théorème est vrai pour $(j_1, j_2)$ et $(s_1, s_2)$ si, et seulement si, il est vrai pour $(j_2, j_1)$ et $(s_2, s_1)$. En particulier, le théorème est donc vrai pour $(n/2, j_2)$ quel que soit $j_2 \in \{1,\ldots, n\}$, et quels que soient $s_1$ et $s_2$. En appliquant à nouveau (eqrec2), on voit que le théorème est vrai pour tout couple $(j_1, j_2) \in \{1,\ldots, n\}^2$.

Pour terminer la preuve du théorème 6 en profondeur 2, il suffit donc d'établir (eqrec2).

Posons $$K_N(j_1, j_2, s_1, s_2) = \sum_{N \geq k_1 \geq k_2 \geq 1}  \frac{1}{(k_1+j_1)^{s_1} (k_2+j_2)^{s_2}}.$$ Alors le théorème 6 concerne la somme $$\label{eq6}
\sum_{\varepsilon_1, \varepsilon_2 \in \mathbb Z/ 2 \mathbb Z} \varepsilon_1 ^{s_1+1}  \varepsilon_2 ^{s_2+1}
\Big( K_N(\varepsilon_1 \cdot j_1, \varepsilon_2 \cdot  j_2, s_1, s_2) -
K_N(\varepsilon_2 \cdot j_2, \varepsilon_1 \cdot  j_1, s_2, s_1)  \Big) .$$ Pour établir (eqrec2), il suffit de démontrer que la différence entre (eq6) pour $(j_1+1, j_2)$ et (eq6) pour $(j_1, j_2)$ est de la forme annoncée dans le théorème 6. Pour évaluer cette différence, on aura besoin des calculs suivants.

D'abord, $$\begin{aligned}
\lefteqn{K_N(j'_1+1 , j'_2, s_1, s_2) - K_N(j'_1, j'_2, s_1, s_2)}\qquad \nonumber \\
&=& \sum_{N \geq k_1 \geq k_2 \geq 1} \frac{1}{(k_2+j'_2)^{s_2}} \Big(  \frac{1}{(k_1+j'_1+1)^{s_1}} -  \frac{1}{(k_1+j'_1)^{s_1}} \Big) \nonumber\\
&=& \sum_{k_2= 1} ^N  \frac{1}{(k_2+j'_2)^{s_2}}  \sum_{k_1 = k_2} ^N
\Big(  \frac{1}{(k_1+j'_1+1)^{s_1}} -  \frac{1}{(k_1+j'_1)^{s_1}} \Big) \nonumber\\
&=& \sum_{k_2= 1} ^N  \frac{1}{(k_2+j'_2)^{s_2}}
\Big(  \frac{1}{(N+j'_1+1)^{s_1}} -  \frac{1}{(k_2+j'_1)^{s_1}} \Big) \nonumber\\
&=& \mathcal{O}(\frac{\log N}{N}) - \sum_{k= 1} ^N  \frac{1}{(k+j'_1)^{s_1} (k+j'_2)^{s_2}}.   \label{eq7}
\end{aligned}$$ On peut en déduire, ou bien démontrer de manière analogue, la relation $$\begin{gathered}
K_N(j'_1-1 , j'_2, s_1, s_2) - K_N(j'_1, j'_2, s_1, s_2)
\\
= \sum_{k_2= 1} ^N  \frac{1}{(k_2+j'_2)^{s_2}}
\Big(  \frac{-1}{(N+j'_1)^{s_1}} +  \frac{1}{(k_2+j'_1-1)^{s_1}} \Big)
\\
= \mathcal{O}(\frac{\log N}{N}) + \sum_{k= 1} ^N  \frac{1}{(k+j'_1-1)^{s_1} (k+j'_2)^{s_2}}.  \label{eq8}
\end{gathered}$$ On aura aussi besoin des relations suivantes, dont la preuve est analogue, et dans lesquelles c'est la deuxième variable que l'on modifie : $$\begin{gathered}
K_N(j'_2, j'_1+1 , s_2, s_1) - K_N(j'_2, j'_1, s_2, s_1)   \\
= \sum_{k= 1} ^N  \frac{1}{(k+j'_1+1)^{s_1} (k+j'_2)^{s_2}}
- \frac{1}{(j'_1+1)^{s_1}} \sum_{k=1}^N \frac{1}{(k+j'_2)^{s_2}}   \label{eq12}
\end{gathered}$$ et $$\begin{gathered}
K_N(j'_2, j'_1-1 , s_2, s_1) - K_N(j'_2, j'_1, s_2, s_1)\\
= - \sum_{k= 1} ^N  \frac{1}{(k+j'_1)^{s_1} (k+j'_2)^{s_2}}
+ \frac{1}{{j'_1}^{s_1}} \sum_{k=1}^N \frac{1}{(k+j'_2)^{s_2}} .   \label{eq13}
\end{gathered}$$

Posons $$\Delta_{\varepsilon_1, \varepsilon_2} (j_1, j_2) =
K_N(\varepsilon_1 \cdot (j_1+1) , \varepsilon_2 \cdot  j_2, s_1, s_2)
- K_N(\varepsilon_1 \cdot j_1, \varepsilon_2 \cdot  j_2, s_1, s_2)$$ et $$\widetilde{\Delta}_{\varepsilon_1, \varepsilon_2} (j_1, j_2) =
K_N(\varepsilon_2 \cdot j_2 , \varepsilon_1 \cdot ( j_1+1), s_2, s_1)
-K_N(\varepsilon_2 \cdot j_2 , \varepsilon_1 \cdot  j_1, s_2, s_1).$$ Avec ces notations, la différence entre (eq6) pour $(j_1+1, j_2)$ et (eq6) pour $(j_1, j_2)$ (que l'on cherche à évaluer) est $$\label{eq11}
\sum_{\varepsilon_1, \varepsilon_2 \in \mathbb Z/ 2 \mathbb Z} \varepsilon_1 ^{s_1+1}  \varepsilon_2 ^{s_2+1}
\Big(  \Delta_{\varepsilon_1, \varepsilon_2} (j_1, j_2)
-  \widetilde{\Delta}_{\varepsilon_1, \varepsilon_2} (j_1, j_2)    \Big) .$$ Or on a : $$\varepsilon_1 \cdot ( j_1+1) =
\left\{
\begin{array}{l}
(\varepsilon_1 \cdot j_1) + 1 \mbox{ si } \varepsilon_1 = +1 \\
(\varepsilon_1 \cdot j_1) - 1 \mbox{ si } \varepsilon_1 = -1.
\end{array}
\right.$$ En utilisant successivement deux fois (eq7), deux fois (eq8), deux fois (eq12) et deux fois (eq13), on voit que (eq11) est la somme des huit termes suivants : $$\begin{aligned}
\Delta_{+1, +1 } (j_1, j_2)
&= - \sum_{k= 1} ^N  \frac{1}{(k+j_1)^{s_1} (k+j_2)^{s_2}}  +  \mathcal{O}(\frac{\log N}{N}) ,
                                                        \label{eq14}\\
(-1)^{s_2+1} \Delta_{+1, -1 } (j_1, j_2)
&= (-1)^{s_2} \sum_{k= 1} ^N  \frac{1}{(k+j_1)^{s_1} (k+n-j_2)^{s_2}}  +  \mathcal{O}(\frac{\log N}{N}) ,
                                                        \label{eq15}\\
(-1)^{s_1+1} \Delta_{-1, +1 } (j_1, j_2)
&= (-1)^{s_1+1} \sum_{k= 1} ^N  \frac{1}{(k+n-j_1-1)^{s_1} (k+j_2)^{s_2}}  +  \mathcal{O}(\frac{\log N}{N}) ,
                                                        \label{eq16}\\
(-1)^{s_1+s_2} \Delta_{-1, -1 } (j_1, j_2)
&= (-1)^{s_1+s_2} \sum_{k= 1} ^N  \frac{1}{(k+n-j_1-1)^{s_1} (k+n-j_2)^{s_2}} \label{eq17}
\\
& \hspace{7.5cm}  +
\mathcal{O}(\frac{\log N}{N}),  \nonumber
\end{aligned}$$ $$- \widetilde{\Delta}_{+1, +1 } (j_1, j_2)
= - \sum_{k= 1} ^N  \frac{1}{(k+j_1+1)^{s_1} (k+j_2)^{s_2}}  +
\frac{1}{(j_1+1)^{s_1}} \sum_{k=1} ^N \frac{1}{(k+j_2)^{s_2}},  \label{eq18}$$ $$\begin{gathered}
(-1)^{s_2} \widetilde{\Delta}_{+1, -1 } (j_1, j_2)
\\
= (-1)^{s_2} \sum_{k= 1} ^N  \frac{1}{(k+j_1+1)^{s_1} (k+n-j_2)^{s_2}}  +
\frac{(-1)^{s_2+1}}{(j_1+1)^{s_1}} \sum_{k=1} ^N \frac{1}{(k+n-j_2)^{s_2}},
\label{eq19}
\end{gathered}$$ $$\begin{gathered}
(-1)^{s_1} \widetilde{\Delta}_{-1, +1 } (j_1, j_2)
\\
= (-1)^{s_1+1} \sum_{k= 1} ^N  \frac{1}{(k+n-j_1)^{s_1} (k+j_2)^{s_2}}  +
\frac{(-1)^{s_1}}{(n-j_1)^{s_1}} \sum_{k=1} ^N \frac{1}{(k+j_2)^{s_2}}, \label{eq20}
\end{gathered}$$ $$\begin{gathered}
(-1)^{s_1+s_2+1} \widetilde{\Delta}_{-1, -1 } (j_1, j_2)
\\
= (-1)^{s_1+s_2} \sum_{k= 1} ^N  \frac{1}{(k+n-j_1)^{s_1} (k+n-j_2)^{s_2}}  +
\frac{(-1)^{s_1+s_2+1}}{(n-j_1)^{s_1}} \sum_{k=1} ^N \frac{1}{(k+n-j_2)^{s_2}}.     \label{eq21}
\end{gathered}$$

On va montrer que la somme de ces huit quantités est bien de la forme voulue, c'est-à-dire s'écrit $Q(H_N) + \mathcal{O}_{\varepsilon} (N^{-1+\varepsilon})$ pour un certain polynôme $Q$ dont la valeur en 0 est une combinaison linéaire des polyzêtas autorisés. Pour cela, on groupe les termes de la manière suivante :

1.  Le premier terme de (eq18) avec (eq17).

2.  Le premier terme de (eq19) avec (eq16).

3.  Le premier terme de (eq20) avec (eq15).

4.  Le premier terme de (eq21) avec (eq14).

5.  Le second terme de (eq18) avec celui de (eq19).

6.  Le second terme de (eq20) avec celui de (eq21).

Pour chacun de ces six groupements, il suffit d'appliquer le théorème 5 en profondeur 1 (c'est-à-dire essentiellement le théorème 1, qui est le phénomène de symétrie habituel : voir §5.1) pour conclure.

Ceci termine la preuve de le théorème 6 en profondeur 2.

## Preuve du théorème 6 en profondeur 3

On procède par récurrence, comme au paragraphe 5.2.

Pour initialiser la récurrence, on considère (puisque $n$ est supposé pair, voir la remarque 2) le cas où $j_1 = j_2 = j_3 = n/2$. Dans ce cas, (eq4) vaut 0 si l'un au moins des $s_i$ est pair. Il ne reste donc à traiter que le cas où les trois $s_i$ sont impairs. Dans ce cas, on a : $$\eqref{eq4} = 8 \sum_{\sigma \in \mathfrak{S}_3} \varepsilon_\sigma \tau_{s_{\sigma(1)},s_{\sigma(2)}, s_{\sigma(3)}}$$ avec $$\tau_{s_1, s_2,s_3} = \sum_{N \geq k_1 \geq k_2 \geq k_3 \geq 1} \frac{1}{(k_1 + \frac{n}{2})^{s_1}  (k_2 + \frac{n}{2})^{s_2}  (k_3 + \frac{n}{2})^{s_3}   }.$$ Or on a $$\begin{aligned}
\tau_{s_1, s_2, s_3}
&=&  \sum_{N + \frac{n}{2} \geq \ell_1 \geq \ell_2  \geq \ell_3 \geq  \frac{n}{2} + 1} \frac{1}{\ell_1^{s_1} \ell_2^{s_2}  \ell_3^{s_3}   }\\
&=&  \sum_{N + \frac{n}{2} \geq \ell_1 \geq \ell_2  \geq \ell_3 \geq   1} \frac{1}{\ell_1^{s_1} \ell_2^{s_2}  \ell_3^{s_3}   } -   \sum_{\ell_3 = 1} ^{n/2}  \frac{1}{\ell_3^{s_3}}
 \sum_{N + \frac{n}{2} \geq \ell_1 \geq \ell_2 \geq  \ell_3} \frac{1}{\ell_1^{s_1} \ell_2^{s_2}}  \\
&=&  \sum_{N + \frac{n}{2} \geq \ell_1 \geq \ell_2  \geq \ell_3 \geq   1} \frac{1}{\ell_1^{s_1} \ell_2^{s_2}  \ell_3^{s_3}   } -  \Big(  \sum_{\ell_3 = 1} ^{n/2}  \frac{1}{\ell_3^{s_3}}   \Big)
 \sum_{N + \frac{n}{2} \geq \ell_1 \geq \ell_2 \geq  1} \frac{1}{\ell_1^{s_1} \ell_2^{s_2}} \\
&& \quad +  \Big( \sum_{\frac{n}{2} \geq \ell_3 > \ell_2 \geq  1} \frac{1}{\ell_3^{s_3} \ell_2^{s_2}} \Big)
 \sum_{\ell_1 = 1} ^{N + n/2}  \frac{1}{\ell_1^{s_1}}
 -   \sum_{ \frac{n}{2} \geq  \ell_3 >  \ell_2 >  \ell_1 \geq  1} \frac{1}{\ell_3^{s_3} \ell_2^{s_2}  \ell_1^{s_1}   }
\end{aligned}$$ donc $\tau_{s_1, s_2, s_3}  = Q(H_N) + \mathcal{O}_\varepsilon(N^{-1+\varepsilon})$ pour un certain polynôme $Q$ tel que (d'après la proposition 1) : $$\begin{aligned}
Q(0) &=& \zeta _*(s_1,s_2,s_3) + \zeta(s_1+s_2, s_3) + \zeta _*(s_1, s_2+s_3) + \zeta(s_1+s_2+s_3)\\
&& - \Big( \sum_{\ell_3 = 1} ^{n/2} \frac{1}{\ell_3^{s_3}} \Big)
\Big( \zeta _*(s_1, s_2) +  \zeta (s_1+s_2) \Big)  + \chi(s_3, s_2) \zeta _*(s_1)
-   \sum_{ \frac{n}{2} \geq  \ell_3 >  \ell_2 >  \ell_1 \geq  1} \frac{1}{\ell_3^{s_3} \ell_2^{s_2}  \ell_1^{s_1} }
\end{aligned}$$ en posant $$\chi(s_3, s_2)  = \sum_{\frac{n}{2} \geq \ell_3 > \ell_2 \geq  1} \frac{1}{\ell_3^{s_3} \ell_2^{s_2}}.$$ Ainsi, on obtient que (eq4) s'écrit sous la forme $Q_1(H_N) + \mathcal{O}_\varepsilon(N^{-1+\varepsilon})$ pour un certain polynôme $Q_1$ tel que $$\begin{gathered}
Q_1(0)
= 8 \sum_{\sigma \in \mathfrak{S}_3} \varepsilon_\sigma \zeta _*(s_{\sigma(1)},s_{\sigma(2)}, s_{\sigma(3)})
 - 8 \Big( \sum_{\ell = 1} ^{n/2} \frac{1}{\ell^{s_3}} \Big) \Big( \zeta _*(s_1, s_2)
 -  \zeta _*(s_2, s_1) \Big)
\\
 + 8 \Big( \sum_{\ell = 1} ^{n/2} \frac{1}{\ell^{s_2}} \Big) \Big( \zeta _*(s_1, s_3)  -  \zeta _*(s_3, s_1) \Big)
 - 8 \Big( \sum_{\ell = 1} ^{n/2} \frac{1}{\ell^{s_1}} \Big) \Big( \zeta _*(s_2, s_3)  -  \zeta _*(s_3, s_2) \Big)
\\
+ 8 \Big( \chi(s_3, s_2) - \chi(s_2, s_3)  \Big)  \zeta _*(s_1)
 - 8 \Big( \chi(s_3, s_1) - \chi(s_1, s_3)  \Big)  \zeta _*(s_2)
\\
- 8 \Big( \chi(s_1, s_2) - \chi(s_2, s_1)  \Big)  \zeta _*(s_3)
- 8  \sum_{\sigma \in \mathfrak{S}_3} \varepsilon_\sigma
 \sum_{ \frac{n}{2} \geq  \ell_3 >  \ell_2 >  \ell_1 \geq  1} \frac{1}{\ell_3^{s_{\sigma(3)}} \ell_2^{s_{\sigma(2)}}  \ell_1^{s_{\sigma(1)}}}.
\end{gathered}$$ Ceci termine l'initialisation de la récurrence.

Démontrons maintenant l'hérédité. Pour raccourcir les notations, on pose $\underline{j}= (j_1, j_2, j_3)$, $\underline{s}= (s_1, s_2, s_3)$ et $\underline{\varepsilon}= (\varepsilon_1, \varepsilon_2, \varepsilon_3)$. La preuve est parallèle à celle dans le cas de la profondeur 2 (§5.2), mais le groupement des termes qui permet de conclure est plus compliqué.

On pose $$K_N(\underline{j}, \underline{s}) = \sum_{N \geq k_1 \geq k_2  \geq k_3  \geq 1}  \frac{1}{(k_1+j_1)^{s_1} (k_2+j_2)^{s_2} (k_3+j_3)^{s_3}}$$ puis, pour $\sigma \in \mathfrak{S}_3$ : $$K_N^\sigma (\underline{j}, \underline{s})  = K_N (j_{\sigma(1)}, j_{\sigma(2)}, j_{\sigma(3)}, s_{\sigma(1)}, s_{\sigma(2)}, s_{\sigma(3)})$$ de telle sorte que $K_N^{{\rm Id}} (\underline{j}, \underline{s}) = K_N  (\underline{j}, \underline{s})$. Puisque $\varepsilon_{\sigma^{-1}} = \varepsilon_{\sigma}$, on a : $$\eqref{eq4} = \sum_{\underline{\varepsilon}\in (\mathbb Z/ 2 \mathbb Z)^3} \underline{\varepsilon}^{\underline{s}+ 1} \sum_{\sigma \in \mathfrak{S}_3} \varepsilon_\sigma
K_N^\sigma (\varepsilon_1 \cdot j_1, \varepsilon_2 \cdot j_2, \varepsilon_3 \cdot j_3, \underline{s})$$ où on note $\underline{\varepsilon}^{\underline{s}+ 1}  = \varepsilon_1 ^{s_1+ 1} \varepsilon_2 ^{s_2+ 1} \varepsilon_3 ^{s_3+ 1} .$ On pose aussi $$\Delta_{\underline{\varepsilon}} ^\sigma (\underline{j}) =
K_N^\sigma (\varepsilon_1 \cdot (j_1+1), \varepsilon_2 \cdot j_2, \varepsilon_3 \cdot j_3, \underline{s})
- K_N^\sigma (\varepsilon_1 \cdot j_1, \varepsilon_2 \cdot j_2, \varepsilon_3 \cdot j_3, \underline{s}).$$ Alors la différence entre (eq4) pour $(j_1+1, j_2, j_3)$ et (eq4) pour $(j_1, j_2, j_3)$ est : $$\label{eq12nv}
\sum_{\underline{\varepsilon}\in (\mathbb Z/ 2 \mathbb Z)^3} \underline{\varepsilon}^{\underline{s}+ 1} \sum_{\sigma \in \mathfrak{S}_3} \varepsilon_\sigma \Delta_{\underline{\varepsilon}} ^\sigma (\underline{j}) .$$ La suite de la preuve est consacrée à (eq12nv) : il s'agit de montrer que cette somme est de la forme voulue, ce qui terminera la récurrence (de manière analogue à (eqrec2) dans le cas de la profondeur 2). Cette somme comprend 48 termes. Dans un premier temps, on fixe $\underline{\varepsilon}\in (\mathbb Z/ 2 \mathbb Z)^3$ et on explicite les 6 termes correspondants. Pour cela, on pose $j'_1 = \varepsilon_1 \cdot j_1$, $j'_2 = \varepsilon_2 \cdot j_2$, $j'_3 = \varepsilon_3 \cdot j_3$. Supposons d'abord que $\varepsilon_1 =  + 1$ ; on a dans ce cas $\varepsilon_1 \cdot (j_1+1) = j'_1 + 1$, et les six termes qui apparaissent correspondent aux formules (eq7) et (eq12) du §5.2.

Commençons par le terme qui provient du 3-cycle (123), qui envoie 1 sur 2, 2 sur 3 et 3 sur 1 : $$\begin{aligned}
\lefteqn{\Delta_{\underline{\varepsilon}} ^{(123)} (\underline{j})}\nonumber \qquad \\
&=& K_N(j'_2 , j'_3, j'_1+1,  s_2, s_3, s_1) - K_N(j'_2 , j'_3, j'_1,  s_2, s_3, s_1) \nonumber \\
&=& \sum_{N \geq k_1 \geq k_2 \geq k_3 \geq 1} \frac{1}{(k_1+j'_2)^{s_2}(k_2+j'_3)^{s_3}} \Big(  \frac{1}{(k_3+j'_1+1)^{s_1}} -  \frac{1}{(k_3+j'_1)^{s_1}} \Big) \nonumber\\
&=& \sum_{N \geq k_1 \geq k_2  \geq 1} \frac{1}{(k_1+j'_2)^{s_2}(k_2+j'_3)^{s_3}} \Big(
\frac{1}{(k_2+j'_1+1)^{s_1}} -  \frac{1}{(j'_1+1)^{s_1}} \Big) \nonumber\\
&=& \sum_{N \geq k \geq \ell  \geq 1} \frac{1}{(\ell+j'_1+1)^{s_1}(k+j'_2)^{s_2}(\ell+j'_3)^{s_3}}  \nonumber\\
&& \hspace{4cm} - \frac{1}{(j'_1+1)^{s_1}}  \sum_{N \geq k \geq \ell  \geq 1} \frac{1}{(k+j'_2)^{s_2}(\ell+j'_3)^{s_3}} .
                                                            \label{eq30}
\end{aligned}$$ Ce terme apparaı̂t dans la somme (eq12nv) avec le coefficient $\underline{\varepsilon}^{\underline{s}+1}$ (sous l'hypothèse que $\varepsilon_1  = +1$), de même que les cinq termes suivants, qui se calculent de manière analogue : $$\begin{aligned}
 \Delta_{\underline{\varepsilon}} ^{{\rm Id}} (\underline{j})
&= -  \sum_{N \geq k \geq \ell  \geq 1} \frac{1}{(k+j'_1)^{s_1}(k+j'_2)^{s_2}(\ell+j'_3)^{s_3}}
+ \mathcal{O}( \frac{\log^2 N}{N})\label{eq34}  \\
- \Delta_{\underline{\varepsilon}} ^{(23)} (\underline{j})
&=  \sum_{N \geq k \geq \ell  \geq 1} \frac{1}{(k+j'_1)^{s_1}(\ell +j'_2)^{s_2}(k+j'_3)^{s_3}}
+ \mathcal{O}( \frac{\log^2 N}{N})  \label{eq33}  \\
- \Delta_{\underline{\varepsilon}} ^{(13)} (\underline{j})
&= -  \sum_{N \geq k \geq \ell  \geq 1} \frac{1}{(\ell+j'_1+1)^{s_1}(\ell+j'_2)^{s_2}(k+j'_3)^{s_3}} \label{eq32} \\
& \qquad \qquad + \frac{1}{(j'_1+1)^{s_1}}  \sum_{N \geq k \geq \ell  \geq 1} \frac{1}{(\ell+j'_2)^{s_2}(k+j'_3)^{s_3}} \nonumber
\end{aligned}$$ $$\begin{aligned}
- \Delta_{\underline{\varepsilon}} ^{(12)} (\underline{j})
&= -  \sum_{N \geq k \geq \ell  \geq 1} \frac{1}{(k+j'_1+1)^{s_1}(k+j'_2)^{s_2}(\ell+j'_3)^{s_3}} \label{eq31} \\
& \qquad \qquad +    \sum_{N \geq k \geq \ell  \geq 1} \frac{1}{(\ell+j'_1)^{s_1}(k+j'_2)^{s_2}(\ell+j'_3)^{s}}\nonumber
\\
\Delta_{\underline{\varepsilon}} ^{(132)} (\underline{j})
&=   \sum_{N \geq k \geq \ell  \geq 1} \frac{1}{(k+j'_1+1)^{s_1}(\ell+j'_2)^{s_2}(k+j'_3)^{s_3}}    \label{eq35} \\
&  \qquad \qquad -    \sum_{N \geq k \geq \ell  \geq 1} \frac{1}{(\ell+j'_1)^{s_1}(\ell+j'_2)^{s_2}(k+j'_3)^{s_3}} .    \nonumber
\end{aligned}$$ Si $\varepsilon_1=-1$, il suffit de prendre l'opposé du membre de droite, et d'y remplacer $j'_1$ par $j'_1-1$, pour que les formules (eq30) à (eq35) soient correctes. Les formules ainsi obtenues sont les analogues de (eq8) et (eq13) (au §5.2). Pour ne pas avoir à distinguer suivant la valeur de $\varepsilon_1$, on aurait pu multiplier le membre de droite par $\varepsilon_1$, et y remplacer $j'_1$ par $j'_1+\frac{\varepsilon_1-1}{2}$. Grâce à ces modifications, les formules (eq30) à (eq35) auraient été valables quel que soit $\varepsilon_1$ ; on utilisera cette convention dans la suite.

Pour exprimer (eq12nv) sous une forme exploitable, on groupe deux par deux les termes obtenus, par les formules (eq30) à (eq35), à partir des 48 termes de la somme (eq12nv). Comme (eq30) et (eq33) ne donnent qu'un terme (à part le terme d'erreur, qu'on omet dans toute la suite des calculs), et que (eq34), (eq32), (eq31) et (eq35) en donnent deux, on écrit ainsi (eq12nv) comme une somme de $8 \times 10 = 80$ termes. On va maintenant expliciter ces 40 groupes de 2 termes.

Soit $\underline{\varepsilon}\in (\mathbb Z/ 2 \mathbb Z)^3$. On pose comme ci-dessus $j'_1 = \varepsilon_1 \cdot j_1$, $j'_2 = \varepsilon_2 \cdot j_2$, $j'_3 = \varepsilon_3 \cdot j_3$. Les 5 groupes qui correspondent à $\underline{\varepsilon}$ sont les suivants :

1.  On regroupe le deuxième terme de (eq30) avec celui de (eq32), ce qui donne $$\label{eq36}
    \varepsilon_1 \underline{\varepsilon}^{\underline{s}+1}  \frac{1}{(j'_1+\frac{\varepsilon_1-1}{2}+1)^{s_1}}  \sum_{N \geq k \geq \ell  \geq 1} \Big( \frac{1}{(\ell+j'_2)^{s_2}(k+j'_3)^{s_3}} - \frac{1}{(k+j'_2)^{s_2}(\ell+j'_3)^{s_3}} \Big).$$

2.  On regroupe le deuxième terme de (eq31) avec le premier terme de (eq33) ; en découplant la sommation sur $k$ et $\ell$, on obtient en omettant le terme d'erreur $$\begin{gathered}
    \varepsilon_1 \underline{\varepsilon}^{\underline{s}+1}
      \sum_{ k=1} ^N   \sum_{ \ell=1} ^N  \frac{1}{(k+j'_1+\frac{\varepsilon_1-1}{2})^{s_1}(\ell+j'_2)^{s_2}(k+j'_3)^{s_3}}
    \\
    + \varepsilon_1 \underline{\varepsilon}^{\underline{s}+1}
      \sum_{ k=1} ^N  \frac{1}{(k+j'_1+\frac{\varepsilon_1-1}{2})^{s_1}(k+j'_2)^{s_2}(k+j'_3)^{s_3}}.  \label{eq37}
    \end{gathered}$$

3.  On regroupe le deuxième terme de (eq35) avec le premier terme de (eq34) ; en découplant la sommation, on obtient (en omettant le terme d'erreur) $$\begin{gathered}
    -\varepsilon_1 \underline{\varepsilon}^{\underline{s}+1}
      \sum_{ k=1} ^N   \sum_{ \ell=1} ^N  \frac{1}{(k+j'_1+\frac{\varepsilon_1-1}{2})^{s_1}(k+j'_2)^{s_2}(\ell+j'_3)^{s_3}}  \label{eq38}\\
    - \varepsilon_1 \underline{\varepsilon}^{\underline{s}+1}
      \sum_{ k=1} ^N  \frac{1}{(k+j'_1+\frac{\varepsilon_1-1}{2})^{s_1}(k+j'_2)^{s_2}(k+j'_3)^{s_3}}.
    \end{gathered}$$

4.  On regroupe le premier terme de (eq31) avec celui de (eq32), d'où : $$\begin{gathered}
    -\varepsilon_1 \underline{\varepsilon}^{\underline{s}+1}
      \sum_{ k=1} ^N   \sum_{ \ell=1} ^N  \frac{1}{(k+j'_1+\frac{\varepsilon_1-1}{2}+1)^{s_1}(k+j'_2)^{s_2}(\ell+j'_3)^{s_3}} \label{eq39} \\
    - \varepsilon_1 \underline{\varepsilon}^{\underline{s}+1}
      \sum_{ k=1} ^N  \frac{1}{(k+j'_1+\frac{\varepsilon_1-1}{2}+1)^{s_1}(k+j'_2)^{s_2}(k+j'_3)^{s_3}},
    \end{gathered}$$ qui se trouve être la même équation que (eq38) mais avec $j'_1$ remplacé par $j'_1+1$ (et sans terme d'erreur à omettre).

5.  On regroupe le premier terme de (eq30) avec celui de (eq35), d'où : $$\begin{gathered}
    \varepsilon_1 \underline{\varepsilon}^{\underline{s}+1}
      \sum_{ k=1} ^N   \sum_{ \ell=1} ^N  \frac{1}{(k+j'_1+\frac{\varepsilon_1-1}{2}+1)^{s_1}(\ell+j'_2)^{s_2}(k+j'_3)^{s_3}}  \label{eq40}\\
    + \varepsilon_1 \underline{\varepsilon}^{\underline{s}+1}
      \sum_{ k=1} ^N  \frac{1}{(k+j'_1+\frac{\varepsilon_1-1}{2}+1)^{s_1}(k+j'_2)^{s_2}(k+j'_3)^{s_3}}
    \end{gathered}$$ qui est la même équation que (eq37) mais avec $j'_1$ remplacé par $j'_1+1$ (et sans terme d'erreur à omettre).

Pour parvenir à la conclusion cherchée, il suffit d'effectuer les groupements suivants, et de constater que chacun d'eux est de la forme voulue :

-   Pour tout $\varepsilon_1 \in \mathbb Z/ 2 \mathbb Z$, on regroupe la somme (eq36) correspondant aux triplets $(\varepsilon_1, 1, 1)$, $(\varepsilon_1, 1, -1)$, $(\varepsilon_1, -1, 1)$ et $(\varepsilon_1, -1, -1)$. La somme de ces quatre termes vaut $$\begin{gathered}
    \frac{\varepsilon_1^{s_1} }{(j'_1+\frac{\varepsilon_1-1}{2}+1)^{s_1}}
    \bigg(\sum_{\varepsilon_2, \varepsilon_3 \in \mathbb Z/ 2 \mathbb Z} \varepsilon_2^{s_2+1} \varepsilon_3^{s_3+1}
    \\
    \cdot \sum_{N \geq k \geq \ell  \geq 1} \Big( \frac{1}{(\ell+\varepsilon_2
    \cdot j_2)^{s_2}(k+\varepsilon_3 \cdot j_3)^{s_3}} - \frac{1}{(k+\varepsilon_2 \cdot j_2)^{s_2}(\ell+\varepsilon_3 \cdot j_3)^{s_3}} \Big)\bigg)
    \end{gathered}$$ Le théorème 6 (démontré en profondeur 2 au §5.2) s'applique à cette somme, et montre qu'elle s'écrit $Q (H_N) + \mathcal{O}_\varepsilon(N^{-1+\varepsilon})$, où $Q(0)$ est une combinaison linéaire (à coefficients dans $\textup{d}_n ^{-(s_2+s_3)} \mathbb Z$) de 1, de valeurs de $\zeta$ en des entiers impairs $s$ compris entre 3 et $s_2+s_3$, et de $\zeta _*(s_3, s_2) - \zeta _*(s_2, s_3)$. En outre ce polyzêta antisymétrique apparaı̂t avec un coefficient nul si $s_2$ ou $s_3$ est pair, et avec un coefficient $4 \varepsilon_1^{s_1} \frac{1}{(j'_1+\frac{\varepsilon_1-1}{2}+1)^{s_1}}$ si $s_2$ et $s_3$ sont impairs. Dans ce dernier cas, en sommant sur $\varepsilon_1 \in \mathbb Z/ 2 \mathbb Z$ on obtient finalement un coefficient $$4 \Big(  \frac{1}{(j_1 +1)^{s_1}} +   \frac{(-1)^{s_1}}{(n-j_1) ^{s_1}}  \Big)$$ qui permet de justifier la remarque qui suit l'énoncé du théorème.

-   Pour tout $(\varepsilon_1, \varepsilon_3)  \in (\mathbb Z/ 2 \mathbb Z)^2$, on regroupe la somme double de (eq37) pour $(\varepsilon_1, 1 , \varepsilon_3)$ avec celle pour $(\varepsilon_1, -1 , \varepsilon_3)$, et avec la somme double de (eq40) relative à $(-\varepsilon_1, 1 , -\varepsilon_3)$ et celle relative à $(-\varepsilon_1,-1, -\varepsilon_3)$. La contribution globale de ces 4 sommes doubles est, en notant génériquement $(\eta_1\varepsilon_1, \eta_2, \eta_1\varepsilon_3)$ les quatre triplets $\underline{\varepsilon}$ qui interviennent : $$\begin{gathered}
    \varepsilon_1^{s_1}  \varepsilon_3^{s_3+1} \bigg(
    \sum_{\eta_1, \eta_2 \in \mathbb Z/ 2 \mathbb Z}
    \eta_1^{s_1+s_3+1} \eta_2 ^{s_2+1} \\
    \cdot
      \sum_{ k=1} ^N   \sum_{ \ell=1} ^N  \frac{1}{(k+\eta_1 \cdot (j'_1+\frac{\varepsilon_1-1}{2}))^{s_1}(\ell+\eta_2 \cdot j_2)^{s_2}(k+\eta_1 \cdot j'_3)^{s_3}}\bigg).
    \end{gathered}$$ Cette somme double se scinde sous la forme suivante : $$\begin{gathered}
     \label{eq41}
    \varepsilon_1^{s_1}  \varepsilon_3^{s_3+1}
    \Big(   \sum_{ k=1} ^N \sum_{\eta_1  \in \mathbb Z/ 2 \mathbb Z}
     \frac{\eta_1^{s_1+s_3+1}  }{(k+\eta_1 \cdot (j'_1+\frac{\varepsilon_1-1}{2}))^{s_1} (k+\eta_1 \cdot j'_3)^{s_3}} \Big)
    \\
    \cdot \Big(    \sum_{ \ell=1} ^N \sum_{\eta_2 \in \mathbb Z/ 2 \mathbb Z}
       \frac{  \eta_2 ^{s_2+1}}{ (\ell+\eta_2 \cdot j_2)^{s_2} } \Big).
    \end{gathered}$$ D'après le théorème 6 (démontrée en profondeur 1), la deuxième somme s'écrit sous la forme $A_1(H_N) + \mathcal{O}_\varepsilon(N^{-1+\varepsilon})$ où $A_1$ est un polynôme tel que $A_1(0)$ soit une combinaison linéaire de 1 et de valeurs de $\zeta$ en des entiers $s$ impairs compris entre 3 et $s_2$, puisque $\zeta _*(1)=0$. En outre $\textup{d}_n^{s_2}$ est un dénominateur commun des coefficients de cette combinaison linéaire. Enfin on a démontré au paragraphe 5.1 que $A_1(0) \in \mathbb Q$ si $s_2$ est pair, et $A_1(0) \in \mathbb Q+ \mathbb Q\zeta(s_2)$ si $s_2$ est impair ; mais cette précision supplémentaire est inutile ici.

    Pour la première somme de (eq41), on applique le théorème 5, démontré en profondeur 1 (voir §§4.1 et 5.1) : cette somme s'écrit sous la forme $A_2(H_N) + \mathcal{O}_\varepsilon(N^{-1+\varepsilon})$ où $A_2$ est un polynôme tel que $A_2(0)$ soit une combinaison linéaire de 1 et de valeurs de $\zeta$ en des entiers $s$ impairs compris entre 3 et $s_1+s_3$. En outre $\textup{d}_n ^{s_1+s_3}$ est un dénominateur commun des coefficients de cette combinaison linéaire.

    Comme la divergence logarithmique de $H_N$ est compensée par le $N^\varepsilon$ du terme d'erreur, on peut faire le produit des deux expressions précédentes et obtenir $$\eqref{eq41}  = \varepsilon_1 \underline{\varepsilon}^{\underline{s}+1}  (A_1A_2)(H_N) + \mathcal{O}_\varepsilon(N^{-1+\varepsilon}).$$ En outre, $A_1A_2(0)$ est une combinaison linéaire de termes de la forme 1, $\zeta(s')$, $\zeta(s'')$ ou $\zeta(s') \zeta(s'')$, avec $s'$, $s''$ impairs et $3 \leq s' \leq s_1+s_3$, $3 \leq s'' \leq s_2$ ; et $\textup{d}_n ^{s_1+s_2+s_3}$ est un dénominateur commun des coefficients.

-   Pour tout $(\varepsilon_1, \varepsilon_2)  \in (\mathbb Z/ 2 \mathbb Z)^2$, on regroupe la somme double de (eq38) pour $(\varepsilon_1,  \varepsilon_2, 1)$ avec celle pour $(\varepsilon_1, \varepsilon_2, -1)$, et avec la somme double de (eq39) relative à $(-\varepsilon_1 , -\varepsilon_2, 1)$ et celle relative à $(-\varepsilon_1, -\varepsilon_2, -1)$. Le même phénomène que précédemment se produit.

-   Pour tout $\underline{\varepsilon}\in (\mathbb Z/ 2 \mathbb Z)^3$, la somme simple de (eq37) et celle de (eq38) (pour cette même valeur de $\underline{\varepsilon}$) sont opposées donc leurs contributions à (eq12nv) s'annulent.

-   De même, la somme simple de (eq39) et celle de (eq40) s'annulent pour tout $\underline{\varepsilon}\in (\mathbb Z/ 2 \mathbb Z)^3$.

## Preuve du théorème 6 en profondeur quelconque

Dans ce paragraphe, on démontre le théorème 6 en profondeur $p \geq 4$ en supposant (par récurrence) qu'il est vrai en profondeurs $p-2$ et $p-1$. En fait cette preuve fonctionne aussi quand $p=2$ et $p=3$ ; on retrouve alors les démonstrations des deux paragraphes précédents, à condition d'être attentif aux conventions quand on somme sur des ensembles vides. Notamment, à la convention habituelle $$\sum_{k \in \emptyset } f(k) = 0$$ on adjoint la convention $$\sum_{k_1 \geq \ldots \geq k_r \geq 1} f(k_1, \ldots, k_r) = 1 \mbox{ pour } r = 0$$ car cette somme porte sur un ensemble vide de variables (par opposition à la précédente, où une variable parcourait un ensemble vide).

L'initialisation de la récurrence se fait de manière tout à fait analogue au cas des profondeurs 2 et 3 : puisque $n$ est supposé pair (voir la remarque 2), il suffit, après avoir posé $$\tau_{s_1,\ldots,s_p} = \sum_{N \geq k_1 \geq \ldots  \geq k_p \geq 1} \frac{1}{(k_1 + \frac{n}{2})^{s_1}  \ldots   (k_p + \frac{n}{2})^{s_p}   },$$ de constater que l'on a $$\tau_{s_1, \ldots,  s_p}
= \sum_{p' = 0} ^p  (-1)^{p'} \Big( \sum_{\frac{n}{2} \geq \ell_p >  \ldots > \ell_{p-p'+1} \geq 1} \frac{1}{\ell_p ^{s_p}  \ldots  \ell_{p-p'+1} ^{s_{p-p'+1}}} \Big)
 \Big( \sum_{N+\frac{n}{2} \geq \ell_1 \geq  \ldots \geq \ell_{p-p'} \geq 1} \frac{1}{\ell_1 ^{s_1}  \ldots  \ell_{p-p'} ^{s_{p-p'}}} \Big).$$

Démontrons maintenant l'hérédité, qui est la partie difficile. On suppose pour cela que le théorème 6 est vrai en profondeurs $p-2$ et $p-1$. On adopte les notations suivantes : $\underline{j}= (j_1, \ldots , j_p)$, $\underline{s}= (s_1, \ldots,  s_p)$, $\underline{\varepsilon}= (\varepsilon_1, \ldots , \varepsilon_p)$, $\underline{\varepsilon}\cdot \underline{j}= (\varepsilon_1 \cdot j_1, \ldots , \varepsilon_p \cdot j_p)$, $\underline{\varepsilon}^{\underline{s}+ 1}  = \varepsilon_1 ^{s_1+ 1} \ldots  \varepsilon_p ^{s_p+ 1}$, $$K_N(\underline{j}, \underline{s}) = \sum_{N \geq k_1 \geq \ldots  \geq k_p  \geq 1}  \frac{1}{(k_1+j_1)^{s_1} \ldots   (k_p+j_p)^{s_p}}$$ et, pour $\sigma \in {\mathfrak S}_p$ : $$K_N^\sigma (\underline{j}, \underline{s})  = K_N (j_{\sigma(1)},\ldots , j_{\sigma(p)}, s_{\sigma(1)}, \ldots , s_{\sigma(p)})$$ de telle sorte que $K_N^{{\rm Id}} (\underline{j}, \underline{s}) = K_N  (\underline{j}, \underline{s})$. Comme $\varepsilon_{\sigma^{-1}} = \varepsilon_{\sigma}$, on a : $$\eqref{eq4} = \sum_{\underline{\varepsilon}\in (\mathbb Z/ 2 \mathbb Z)^p} \underline{\varepsilon}^{\underline{s}+ 1} \sum_{\sigma \in {\mathfrak S}_p} \varepsilon_\sigma
K_N^\sigma (\underline{\varepsilon}\cdot \underline{j}, \underline{s}).$$ On pose aussi $$\Delta_{\underline{\varepsilon}} ^\sigma (\underline{j}) =
K_N^\sigma (\varepsilon_1 \cdot (j_1+1), \varepsilon_2 \cdot j_2, \ldots,  \varepsilon_p \cdot j_p, \underline{s})
- K_N^\sigma (\underline{\varepsilon}\cdot \underline{j}, \underline{s}).$$ Alors la différence entre (eq4) pour $(j_1+1, j_2, \ldots , j_p)$ et (eq4) pour $\underline{j}$ est : $$\label{eq60}
\sum_{\underline{\varepsilon}\in (\mathbb Z/ 2 \mathbb Z)^p} \underline{\varepsilon}^{\underline{s}+ 1} \sum_{\sigma \in {\mathfrak S}_p} \varepsilon_\sigma \Delta_{\underline{\varepsilon}} ^\sigma (\underline{j}) .$$ La suite de la preuve est consacrée à (eq60) : il s'agit de montrer que cette somme est de la forme voulue, ce qui terminera la récurrence (de même qu'en profondeur 2 et 3).

Pour tout $\sigma \in {\mathfrak S}_p$, on pose $t_{\sigma}= \sigma^{-1}(1)$ et $j'_1 = \varepsilon_1 \cdot j_1$, ..., $j'_p = \varepsilon_p \cdot j_p$, de telle sorte que $\underline{j'}= (j'_1,\ldots, j'_p) =\underline{\varepsilon}\cdot \underline{j}$. On pose aussi, par convention, $k_0 = N$ et $k_{p+1} = 1$. Supposons d'abord que $\varepsilon_1 =  + 1$ ; on a dans ce cas $\varepsilon_1 \cdot (j_1+1) = j'_1 + 1$, et : $$\begin{aligned}
\Delta_{\underline{\varepsilon}} ^\sigma (\underline{j})
&=& K_N^\sigma (j'_1+1, j'_2, \ldots,  j'_p, \underline{s}) - K_N^\sigma (\underline{j'}, \underline{s}) \\
&=& \sum_{N \geq k_1 \geq \ldots  \geq k_p  \geq 1} (k_1+j'_{\sigma(1)})^{-s_{\sigma(1)}} \ldots
 (k_{t_{\sigma}}+j'_1+1)^{-s_1} \ldots  (k_p+j'_{\sigma(p)})^{-s_{\sigma(p)}} \\
&& \quad \quad  - \sum_{N \geq k_1 \geq \ldots  \geq k_p  \geq 1} (k_1+j'_{\sigma(1)})^{-s_{\sigma(1)}} \ldots
 (k_{t_{\sigma}}+j'_1)^{-s_1} \ldots  (k_p+j'_{\sigma(p)})^{-s_{\sigma(p)}} \\
&=&  \sum_{N \geq k_1 \geq \ldots \geq \widehat{k_{t_{\sigma}}} \geq \ldots  \geq k_p  \geq 1}
(k_1+j'_{\sigma(1)})^{-s_{\sigma(1)}} \ldots   \widehat{ (k_{t_{\sigma}}+j'_1)^{-s_1} } \ldots  (k_p+j'_{\sigma(p)})^{-s_{\sigma(p)}} \\
&& \quad \quad \times  \sum_{k_{t_{\sigma}} = k_{t_{\sigma}+1}} ^{k_{t_{\sigma}-1}}  (k_{t_{\sigma}}+j'_1+1)^{-s_1}
- (k_{t_{\sigma}}+j'_1)^{-s_1} \\
&=&  \sum_{N \geq k_1 \geq \ldots \geq  \widehat{k_{t_{\sigma}}} \geq \ldots  \geq k_p  \geq 1}
(k_1+j'_{\sigma(1)})^{-s_{\sigma(1)}} \ldots   \widehat{ (k_{t_{\sigma}}+j'_1)^{-s_1} } \ldots  (k_p+j'_{\sigma(p)})^{-s_{\sigma(p)}} \\
&& \quad \quad \times  \Big( \frac{1}{ (k_{t_{\sigma}-1}+j'_1+1)^{s_1}} -  \frac{1}{ (k_{t_{\sigma}+1}+j'_1)^{s_1}} .
\Big)
\end{aligned}$$ Dans ce calcul, comme dans toute la suite, on note avec un chapeau l'omission d'un terme dans une liste. En outre, on utilise les conventions $k_0 = N$ et $k_{p+1} = 1$.

Dans le cas où $\varepsilon_1=-1$, la dernière formule obtenue pour $\Delta_{\underline{\varepsilon}} ^\sigma (\underline{j})$ reste valable, à condition d'en prendre l'opposé et d'y remplacer $j'_1$ par $j'_1-1$. Cela montre qu'on peut écrire, quelle que soit la valeur de $\varepsilon_1$ : $$\label{eq59}
\Delta_{\underline{\varepsilon}} ^\sigma (\underline{j})= S_{\underline{\varepsilon}} ^\sigma (\underline{j})- \widetilde{S}_{\underline{\varepsilon}} ^\sigma (\underline{j})$$ en posant $$\begin{aligned}
\lefteqn{S_{\underline{\varepsilon}} ^\sigma (\underline{j})} \nonumber \\
&=&\varepsilon_1  \sum_{N \geq k_1 \geq \ldots \geq \widehat{k_{t_{\sigma}}} \geq \ldots  \geq k_p  \geq 1}
(k_1+j'_{\sigma(1)})^{-s_{\sigma(1)}} \ldots   \widehat{ (k_{t_{\sigma}}+j'_1)^{-s_1} } \ldots  (k_p+j'_{\sigma(p)})^{-s_{\sigma(p)}}   \label{eq57} \\
&& \quad \quad \quad \quad \times    \frac{1}{ (k_{t_{\sigma}-1}+j'_1+\frac{\varepsilon_1-1}{2}+1)^{s_1}}  \nonumber
\end{aligned}$$ et $$\begin{aligned}
\lefteqn{\widetilde{S}_{\underline{\varepsilon}} ^\sigma (\underline{j})} \nonumber \\
&=& \varepsilon_1  \sum_{N \geq k_1 \geq \ldots \geq \widehat{k_{t_{\sigma}}} \geq \ldots  \geq k_p  \geq 1}
(k_1+j'_{\sigma(1)})^{-s_{\sigma(1)}} \ldots   \widehat{ (k_{t_{\sigma}}+j'_1)^{-s_1} } \ldots  (k_p+j'_{\sigma(p)})^{-s_{\sigma(p)}}   \label{eq58} \\
&& \quad \quad \quad \quad \times    \frac{1}{ (k_{t_{\sigma}+1}+j'_1+\frac{\varepsilon_1-1}{2})^{s_1}}.  \nonumber
\end{aligned}$$ La relation (eq59) va nous permettre de démontrer que (eq60) est de la forme voulue. Dans un premier temps, on isole deux cas particuliers. Le premier concerne les termes de la forme $S_{\underline{\varepsilon}} ^\sigma (\underline{j})$ correspondant à des permutations $\sigma$ telles que $t_{\sigma}= 1$. Pour ces termes, on a d'après (eq57) la majoration $S_{\underline{\varepsilon}} ^\sigma (\underline{j})= \mathcal{O}(\frac{(\log N)^{p-1}}{N})$ puisque $k_0 = N$ ; donc ces termes rentrent dans le terme d'erreur, et on peut les ignorer. Par ailleurs, si on regroupe tous les termes de la forme $\widetilde{S}_{\underline{\varepsilon}} ^\sigma (\underline{j})$ correspondant à des permutations $\sigma$ telles que $t_{\sigma}= p$, on obtient pour contribution globale à (eq60), puisque $k_{p+1}=1$ : $$\begin{aligned}
&& \frac{- 1}{ (j'_1+\frac{\varepsilon_1-1}{2}+ 1)^{s_1}} \sum_{\underline{\varepsilon}\in (\mathbb Z/ 2 \mathbb Z)^p} \underline{\varepsilon}^{\underline{s}+ 1} \varepsilon_1  \sum_{\tiny {\begin{array}{c} \sigma \in {\mathfrak S}_p \\ t_{\sigma}= p \end{array}}} \varepsilon_\sigma   \label{eq62} \\
&&\times \sum_{N \geq k_1 \geq \ldots \geq k_{p-1}  \geq 1}
(k_1+j'_{\sigma(1)})^{-s_{\sigma(1)}} \ldots (k_{p-1}+j'_{\sigma(p-1)})^{-s_{\sigma(p-1)}}.  \nonumber
\end{aligned}$$ En fixant $\varepsilon_1$ dans cette somme, on peut appliquer le théorème 6 en profondeur $p-1$, avec $(\varepsilon_2, \ldots, \varepsilon_p)$, $(j_2, \ldots, j_p)$, et $(s_2, \ldots, s_p)$. Le terme obtenu est multiplié par le rationnel $\frac{- \varepsilon_1 ^{s_1}}{ (j'_1+\frac{\varepsilon_1-1}{2}+ 1)^{s_1}}$, dont $\textup{d}_n^{s_1}$ est un dénominateur ; le résultat est donc de la forme souhaitée. Ce raisonnement généralise celui qui a permis, en profondeur 3, de traiter la somme (eq36).

Pour terminer la preuve, on peut donc ignorer dans (eq60) les termes provenant de ces deux familles de cas particuliers. Cela revient à faire la convention suivante, que nous adoptons dans toute la suite : $$\label{eq61}
\left\{
\begin{array}{l}
S_{\underline{\varepsilon}} ^\sigma (\underline{j})= 0 \mbox{ si } t_{\sigma}= 1 \\
\widetilde{S}_{\underline{\varepsilon}} ^\sigma (\underline{j})= 0 \mbox{ si } t_{\sigma}= p.
\end{array}
\right.$$

On peut maintenant relier les sommes $S_{\underline{\varepsilon}} ^\sigma (\underline{j})$ et $\widetilde{S}_{\underline{\varepsilon}} ^\sigma (\underline{j})$, pour les étudier simultanément. Pour cela, on démontre l'égalité suivante, valable pour tout $\sigma \in {\mathfrak S}_p$ tel que $t_{\sigma}\geq 2$ : $$\label{eq56}
S_{\underline{\varepsilon}} ^\sigma (\underline{j})= \widetilde{S}_{\underline{\varepsilon}} ^{\sigma \circ  (t_{\sigma}-1 \, \, t_{\sigma})} (\underline{j} + (\varepsilon_1, 0, \ldots, 0))$$ avec $\underline{j} + (\varepsilon_1, 0, \ldots, 0)= (j_1+\varepsilon_1, j_2, \ldots, j_p)$. Posons $\widetilde \sigma= \sigma \circ  (t_{\sigma}-1 \, \, t_{\sigma})$ ; on a $\widetilde \sigma(j) = \sigma(j)$ pour $j \not\in \{t_{\sigma}-1, t_{\sigma}\}$, $\widetilde \sigma(t_{\sigma}-1) = 1$ et $\widetilde \sigma(t_{\sigma}) = \sigma(t_{\sigma}-1)$. En particulier, on a $t_{\widetilde \sigma}= t_{\sigma}- 1$. On constate alors qu'en remplaçant $j_1$ par $j_1 + \varepsilon_1$ (ce qui revient à remplacer $j'_1$ par $j'_1+1$) dans la définition (eq58) de $\widetilde{S}_{\underline{\varepsilon}} ^{\widetilde \sigma} (\underline{j})$, on obtient exactement celle (eq57) de $S_{\underline{\varepsilon}} ^\sigma (\underline{j})$, à un changement de notation près sur les indices de sommation. En effet, dans (eq57), l'indice $k_{t_{\sigma}}$ n'apparaı̂t pas dans la somme, alors que $k_{t_{\sigma}- 1}$ apparaı̂t et correspond à deux facteurs. Dans (eq58), c'est $k_{t_{\sigma}-1}$ qui n'apparaı̂t pas, et $k_{t_{\sigma}}$ correspond à deux facteurs, qui sont exactement ceux provenant de $k_{t_{\sigma}-1}$ dans (eq57) (après avoir remplacé $j'_1$ par $j'_1+\varepsilon_1$ dans (eq58)). Enfin les $k_j$ pour $j \not\in \{t_{\sigma}-1, t_{\sigma}\}$ jouent le même rôle dans (eq57) et dans (eq58). Ceci termine la preuve de (eq56).

Compte tenu de (eq59), (eq56) et (eq61), on peut maintenant réécrire (eq60) sous la forme : $$\label{eq63}
-  \sum_{\underline{\varepsilon}\in (\mathbb Z/ 2 \mathbb Z)^p} \underline{\varepsilon}^{\underline{s}+ 1}   \sum_{\tiny {\begin{array}{c} \sigma \in {\mathfrak S}_p \\ t_{\sigma}\leq  p-1 \end{array}}} \varepsilon_\sigma
\Big( \widetilde{S}_{\underline{\varepsilon}} ^\sigma (\underline{j})+ \widetilde{S}_{\underline{\varepsilon}} ^\sigma (\underline{j} + (\varepsilon_1, 0, \ldots, 0))\Big)$$ en omettant (eq62) et le terme d'erreur $\mathcal{O}(\frac{(\log N)^{p-1}}{N})$ rencontrés plus haut (ce qui correspond à la convention (eq61)). Pour conclure la preuve, il suffit donc de démontrer que (eq63) est de la forme voulue.

Pour cela, on définit une application $$\begin{aligned}
\Phi : \{ \sigma \in {\mathfrak S}_p, \, t_{\sigma}\leq p-1 \}
&\rightarrow & \{1,\ldots, p-1\}\times \{2,\ldots, p\}\times {\mathfrak S}_{p-2}\\
\sigma &\mapsto& (t_{\sigma}, \vartheta_{\sigma}, \gamma)
\end{aligned}$$ de la façon suivante. Pour $\sigma \in {\mathfrak S}_p$ tel que $t_{\sigma}\leq p-1$, on pose $$\vartheta_{\sigma}= \sigma(t_{\sigma}+1),$$ et on note $\varphi_{\sigma}: \{1,\ldots, p-2\}\rightarrow \{1,\ldots, p\}\setminus\{ t_{\sigma}, t_{\sigma}+1\}$ et $\psi_{\sigma}: \{1,\ldots, p-2\}\rightarrow \{2,\ldots, p\}\setminus\{ \vartheta_{\sigma}\}$ les bijections strictement croissantes. On pose alors $$\gamma = \psi_{\sigma}^{-1} \circ \sigma \circ \varphi_{\sigma}\in {\mathfrak S}_{p-2}= {\mathfrak S} (\{1,\ldots, p-2\})$$ où on identifie $\sigma$ avec sa restriction $\sigma : \{1,\ldots, p\}\setminus\{ t_{\sigma}, t_{\sigma}+1\} \rightarrow \{2,\ldots, p\}\setminus\{ \vartheta_{\sigma}\}$. Par définition de $t_{\sigma}$ et $\vartheta_{\sigma}$, cette restriction est bijective, donc $\gamma$ aussi. Il est facile de voir que $\Phi$ est une bijection.

Grâce à cette bijection $\Phi$, on va remplacer la somme sur $\sigma$ dans (eq63) par une somme sur $(t_{\sigma}, \vartheta_{\sigma}, \gamma)$. Pour cela on utilise la relation suivante, valable pour tout $\sigma \in {\mathfrak S}_p$ tel que $t_{\sigma}\leq p-1$ : $$\label{eq64}
\varepsilon_\sigma  = (-1)^{\vartheta_{\sigma}} \varepsilon_\gamma.$$ Pour démontrer (eq64), on étudie les couples $(i,j)$ tels que $1 \leq i <  j \leq p$ et $\sigma(i) > \sigma(j)$ ; la signature de $\sigma$ est donnée par la parité du nombre de tels couples. Soit $(i,j)$ un tel couple. Si $\{i,j\} \cap  \{ t_{\sigma}, t_{\sigma}+1\} = \emptyset$, ce couple correspond au couple $(\varphi_{\sigma}^{-1}(i), \varphi_{\sigma}^{-1}(j))$ qui contribue à la signature de $\gamma$. Réciproquement, chaque couple qui intervient dans le calcul de $\varepsilon_\gamma$ est obtenu, une et une seule fois, de cette manière. Comme le cas $\{i,j\} =  \{ t_{\sigma}, t_{\sigma}+1\}$ est exclu puisque $\sigma(t_{\sigma}) =1 < \sigma(t_{\sigma}+1)$, il y a exactement quatre autres possibilités (qui s'excluent mutuellement) pour les couples $(i,j)$ qui contribuent à $\varepsilon_\sigma$ mais pas à $\varepsilon_\gamma$ :

-   Ou bien $i = t_{\sigma}$, mais c'est impossible car $\sigma(t_{\sigma}) = 1 < \sigma(j)$.

-   Ou bien $i = t_{\sigma}+1$ d'où $j \geq t_{\sigma}+  2$ avec $\sigma(j) < \vartheta_{\sigma}$ ; le nombre de tels couples est ${\rm Card}\{ j \geq t_{\sigma}+ 2, \, \sigma(j) < \vartheta_{\sigma}\}$.

-   Ou bien $j = t_{\sigma}$, d'où $i < t_{\sigma}$ et $\sigma(i) > 1$ ; il y a exactement $t_{\sigma}- 1$ tels couples.

-   Ou bien $j = t_{\sigma}+1$ d'où $i < t_{\sigma}$ et $\sigma(i) > \vartheta_{\sigma}$ ; le nombre de tels couples est ${\rm Card}\{ i <   t_{\sigma}, \, \sigma(i) >  \vartheta_{\sigma}\}$.

Pour démontrer (eq64), il suffit donc de prouver la relation suivante : $$\label{eq65}
{\rm Card}\{ j \geq t_{\sigma}+ 2, \, \sigma(j) < \vartheta_{\sigma}\} + {\rm Card}\{ i <   t_{\sigma}, \, \sigma(i) >  \vartheta_{\sigma}\}
+ t_{\sigma}- 1 \equiv \vartheta_{\sigma}\mod 2.$$ Or on a clairement $${\rm Card}\{ j \geq t_{\sigma}+ 2, \, \sigma(j) < \vartheta_{\sigma}\} + {\rm Card}\{ j \geq t_{\sigma}+ 2, \, \sigma(j) >  \vartheta_{\sigma}\}
= {\rm Card}\{ t_{\sigma}+2, \ldots, p \} = p - t_{\sigma}- 1$$ et $${\rm Card}\{ i <   t_{\sigma}, \, \sigma(i) >  \vartheta_{\sigma}\} + {\rm Card}\{ i \geq t_{\sigma}+ 2, \, \sigma(i) >  \vartheta_{\sigma}\}
= {\rm Card}\{ \vartheta_{\sigma}+1, \ldots, p \} = p - \vartheta_{\sigma}.$$ En additionnant ces deux relations on obtient (eq65), ce qui termine la preuve de (eq64).

Grâce à la bijection $\Phi$ et à (eq64), on peut maintenant écrire (eq63) sous la forme suivante : $$\begin{aligned}
\eqref{eq63}
&=& - \sum_{\vartheta= 2} ^p (-1)^\vartheta
 \sum_{\underline{\varepsilon}\in (\mathbb Z/ 2 \mathbb Z)^p} \underline{\varepsilon}^{\underline{s}+ 1}
 \sum_{\gamma \in {\mathfrak S}_{p-2}} \varepsilon_\gamma  \label{eq69} \\
&& \quad \quad \times \sum_{t = 1}^{p-1}  \Big( \widetilde{S}_{\underline{\varepsilon}} ^{\Phi^{-1}(t,\vartheta,\gamma)} (\underline{j})+ \widetilde{S}_{\underline{\varepsilon}} ^{\Phi^{-1}(t,\vartheta,\gamma)} (\underline{j} + (\varepsilon_1, 0, \ldots, 0))\Big) .  \nonumber
\end{aligned}$$ On va maintenant montrer que la somme sur $t$ induit un découplage de l'une des variables. Précisément, fixons $\vartheta\in \{2,\ldots, p\}$, $\underline{\varepsilon}\in (\mathbb Z/ 2 \mathbb Z)^p$ et $\gamma \in {\mathfrak S}_{p-2}$. En posant $\sigma_t= \Phi^{-1}(t,\vartheta,\gamma)$ on a d'après (eq58) : $$\begin{aligned}
\sum_{t=1}^{p-1} \widetilde{S}_{\underline{\varepsilon}} ^{\sigma_t} (\underline{j})
&=& \varepsilon_1  \sum_{t=1}^{p-1}  \sum_{N \geq k_1 \geq \ldots \geq \widehat{k_t} \geq \ldots  \geq k_p  \geq 1}
(k_{t+1}+j'_1+\frac{\varepsilon_1-1}{2})^{-s_1}
\prod_{\tiny {\begin{array}{c} 1 \leq i \leq p  \\ i \neq t \end{array}}}
(k_i+j'_{\sigma_t(i)})^{-s_{\sigma_t(i)}}.
\end{aligned}$$ Notons $\lambda$ la variable $k_{t+1}$, qui apparaı̂t dans deux facteurs. Posons aussi $\ell_i = k_{\varphi_{\sigma_t}(i)}$ pour tout $i \in \{1,\ldots, p-2\}$. On obtient : $$\begin{aligned}
\sum_{t=1}^{p-1} \widetilde{S}_{\underline{\varepsilon}} ^{\sigma_t} (\underline{j})
&=& \varepsilon_1  \sum_{t=1}^{p-1}  \sum_{N \geq \ell_1 \geq \ldots \geq \ell_{t-1} \geq \lambda\geq \ell_t \geq  \ldots  \geq \ell_{p-2}  \geq 1}
(\lambda+j'_1+\frac{\varepsilon_1-1}{2})^{-s_1}  (\lambda+ j'_{\vartheta_{\sigma_t}})^{-s_{\vartheta_{\sigma_t}}}  \\
&& \quad \quad \times
\prod_{i=1} ^{p-2} (\ell_i+j'_{\sigma_t\circ \varphi_{\sigma_t}(i)})^{-s_{\sigma_t\circ \varphi_{\sigma_t}(i)}}.
\end{aligned}$$ La propriété cruciale est alors que le sommande est indépendant de $t$, puisque $\vartheta_{\sigma_t}= \vartheta$ et $\sigma_t\circ  \varphi_{\sigma_t}= \psi_{\sigma_t}\circ \gamma$ par définition ; en outre $\psi_{\sigma_t}$ ne dépend pas de $t$, mais seulement de $\vartheta$ (on note désormais $\psi$ cette fonction). On peut donc découpler la somme en écrivant : $$\sum_{t=1}^{p-1}
\sum_{N \geq \ell_1 \geq \ldots \geq \ell_{t-1} \geq \lambda\geq \ell_t \geq  \ldots  \geq \ell_{p-2}  \geq 1}
=
\sum_{\tiny {\begin{array}{c} N \geq \ell_1 \geq \ldots  \geq \ell_{p-2}  \geq 1 \\ N \geq \lambda\geq 1  \end{array}}}
+  \sum_{i=1}^{p-2}      \sum_{\tiny {\begin{array}{c} N \geq \ell_1 \geq \ldots  \geq \ell_{p-2}  \geq 1 \\ \lambda= \ell_i  \end{array}}}.$$ On obtient ainsi $$\label{eq66}
\sum_{t=1}^{p-1} \widetilde{S}_{\underline{\varepsilon}} ^{\sigma_t} (\underline{j})= {\mathcal A}_{\underline{\varepsilon}} ^{\vartheta, \gamma} (\underline{j})+   \sum_{i=1}^{p-2}      {\mathcal B}_{\underline{\varepsilon}, i} ^{\vartheta, \gamma} (\underline{j})$$ en posant $$\begin{aligned}
{\mathcal A}_{\underline{\varepsilon}} ^{\vartheta, \gamma} (\underline{j})& = &  \varepsilon_1
\Big( \sum_{\lambda= 1}^N (\lambda+j'_1+\frac{\varepsilon_1-1}{2})^{-s_1}  (\lambda+ j'_{\vartheta})^{-s_{\vartheta}}  \Big) \label{eq67} \\
&& \times \Big(    \sum_{N \geq \ell_1 \geq \ldots  \geq \ell_{p-2}  \geq 1}
\prod_{i=1} ^{p-2} (\ell_i+j'_{\psi\circ \gamma (i)})^{-s_{\psi\circ \gamma (i)}} \Big)     \nonumber
\end{aligned}$$ et $$\begin{aligned}
\lefteqn{{\mathcal B}_{\underline{\varepsilon}, i} ^{\vartheta, \gamma} (\underline{j})}  \nonumber
\\&=&   \varepsilon_1   \sum_{N \geq \ell_1 \geq \ldots  \geq \ell_{p-2}  \geq 1}
(\ell_i +j'_1+\frac{\varepsilon_1-1}{2})^{-s_1}  (\ell_i + j'_{\vartheta})^{-s_{\vartheta}}   (\ell_i+j'_{\psi\circ \gamma (i)})^{-s_{\psi\circ \gamma (i)}}   \label{eq68} \\
&& \quad \quad \times   \prod_{\tiny {\begin{array}{c} 1 \leq i' \leq p-2 \\ i' \neq i \end{array}}}      (\ell_{i'}+j'_{\psi\circ \gamma (i')})^{-s_{\psi\circ \gamma (i')}}  .   \nonumber
\end{aligned}$$ Grâce à (eq66), on peut maintenant écrire (eq63) sous la forme suivante (en remplaçant dans (eq69)) : $$\begin{gathered}
\eqref{eq63} = - \sum_{\vartheta= 2} ^p (-1)^\vartheta
 \sum_{\underline{\varepsilon}\in (\mathbb Z/ 2 \mathbb Z)^p} \underline{\varepsilon}^{\underline{s}+ 1}
 \sum_{\gamma \in {\mathfrak S}_{p-2}} \varepsilon_\gamma  \label{eq70} \\
  \times   \Big( {\mathcal A}_{\underline{\varepsilon}} ^{\vartheta, \gamma} (\underline{j})+  {\mathcal A}_{\underline{\varepsilon}} ^{\vartheta, \gamma} (\underline{j} + (\varepsilon_1, 0, \ldots, 0))+    \sum_{i=1}^{p-2}    \Big(  {\mathcal B}_{\underline{\varepsilon}, i} ^{\vartheta, \gamma} (\underline{j})+ {\mathcal B}_{\underline{\varepsilon}, i} ^{\vartheta, \gamma} (\underline{j} + (\varepsilon_1, 0, \ldots, 0))\Big)  \Big).
\end{gathered}$$ Ici, les termes ${\mathcal A}_{\underline{\varepsilon}} ^{\vartheta, \gamma}$ correspondent (en profondeur $p= 3$) aux sommes doubles des équations (eq37) à (eq40) ; les termes ${\mathcal B}_{\underline{\varepsilon}, i} ^{\vartheta, \gamma}$ correspondent aux sommes simples qui les accompagnent. On va maintenant généraliser le groupement de termes utilisé en profondeur 3 : ainsi, on groupe les termes de (eq70) de telle sorte que chaque groupe soit de la forme voulue. Cela terminera la preuve du théorème 6.

La première famille de groupements permet de traiter les termes ${\mathcal A}_{\underline{\varepsilon}} ^{\vartheta, \gamma}$. Soient $\vartheta\in \{2,\ldots, p\}$ et $(\varepsilon_1^0, \varepsilon_\vartheta^0) \in (\mathbb Z/ 2 \mathbb Z)^2$ fixés. On regroupe les $2^{p-1}(p-2)!$ termes suivants : $$\begin{aligned}
&& {\mathcal A}_{\underline{\varepsilon}} ^{\vartheta, \gamma} (\underline{j})\mbox{ pour } \gamma \in {\mathfrak S}_{p-2}\mbox{ et  $\underline{\varepsilon}$ de la forme }
(\varepsilon_1^0, \eta_2, \ldots, \eta_{\vartheta-1}, \varepsilon_\vartheta^0, \eta_{\vartheta+1}, \ldots, \eta_p) \\
&& \quad \quad \quad \mbox{ avec } (\eta_2, \ldots, \eta_{\vartheta-1},  \eta_{\vartheta+1}, \ldots, \eta_p) \in (\mathbb Z/ 2 \mathbb Z)^{p-2}\mbox{ , et} \\
&&{\mathcal A}_{\underline{\varepsilon}} ^{\vartheta, \gamma} (\underline{j} + (\varepsilon_1, 0, \ldots, 0))\mbox{ pour } \gamma \in {\mathfrak S}_{p-2}\mbox{ et  $\underline{\varepsilon}$ de la forme }
(-\varepsilon_1^0, \eta_2, \ldots, \eta_{\vartheta-1}, -\varepsilon_\vartheta^0, \eta_{\vartheta+1}, \ldots, \eta_p) \\
&& \quad \quad \quad \mbox{ avec } (\eta_2, \ldots, \eta_{\vartheta-1},  \eta_{\vartheta+1}, \ldots, \eta_p) \in (\mathbb Z/ 2 \mathbb Z)^{p-2}.
\end{aligned}$$ Pour unifier ces deux cas, on note $\varepsilon_1 = \eta_1 \varepsilon_1^0$ et $\varepsilon_\vartheta= \eta_1 \varepsilon_\vartheta^0$ avec $\eta_1 \in \mathbb Z/ 2 \mathbb Z$. Pour les $2^{p-2}(p-2)!$ termes qui correspondent à $\eta_1 = -1$ (c'est-à-dire ceux de la forme ${\mathcal A}_{\underline{\varepsilon}} ^{\vartheta, \gamma} (\underline{j} + (\varepsilon_1, 0, \ldots, 0))$), il convient de remarquer qu'on a $\varepsilon_1 = - \varepsilon_1^0$ donc $\varepsilon_1 \cdot (j_1+\varepsilon_1) + \frac{\varepsilon_1-1}{2} = (-1) \cdot ((\varepsilon_1^0\cdot j_1) + \frac{\varepsilon_1^0-1}{2})$. Ceci permet de prouver que la contribution globale de ces $2^{p-1}(p-2)!$ termes à (eq70) s'écrit, à un signe près qui dépend de $\vartheta$, $\varepsilon_1^0$ et $\varepsilon_\vartheta^0$ : $$\begin{gathered}
\Big( \sum_{\eta_1 \in \mathbb Z/ 2 \mathbb Z} \eta_1 ^{s_1+s_\vartheta+1} \sum_{\lambda=1}^N
(\lambda+ \eta_1 \cdot ((\varepsilon_1^0\cdot j_1)+  \frac{\varepsilon_1^0-1}{2}))^{-s_1}
(\lambda+ \eta_1 \cdot (\varepsilon_\vartheta^0\cdot j_\vartheta))^{-s_\vartheta} \Big)  \label{eq67bis}
\\
\times \Big( \sum_{(\eta_2, \ldots, \widehat{\eta_{\vartheta}}, \ldots, \eta_p) \in (\mathbb Z/ 2 \mathbb Z)^{p-2}}
\eta_2 ^{s_2+1} \ldots \widehat{\eta_\vartheta^{s_\vartheta+1}} \ldots \eta_p ^{s_p+1}
 \sum_{\gamma \in {\mathfrak S}_{p-2}} \varepsilon_\gamma
\\
 \quad \quad \quad   \quad \quad   \times
  \sum_{N \geq \ell_1 \geq \ldots  \geq \ell_{p-2}  \geq 1}
\prod_{i=1} ^{p-2} (\ell_i+\eta_{\psi\circ \gamma (i)} \cdot j_{\psi\circ \gamma (i)})^{-s_{\psi\circ \gamma (i)}} \Big).
\end{gathered}$$ Pour traiter le deuxième facteur de ce produit, on applique le théorème 6 en profondeur $p-2$, avec $j_2, \ldots, \widehat{j_\vartheta}, \ldots, j_p$ et $s_2, \ldots, \widehat{s_\vartheta}, \ldots, s_p$. Ce facteur s'écrit donc $A_1(H_N) + \mathcal{O}_\varepsilon(N^{-1+\varepsilon})$ où $A_1$ est un polynôme tel que $A_1(0)$ soit une combinaison linéaire de produits de la forme (eq999) avec $\{ i_1 , \ldots , i_{q-q'}  \} \cup \{ j_1 , \ldots , j_{2q'} \} \subset \{2,\ldots, p\}\setminus\{\vartheta\}$. De plus $\textup{d}_n^{s_2 +  \ldots + \widehat{s_\vartheta} + \ldots + s_p}$ est un dénominateur commun des coefficients de cette combinaison linéaire.

Pour le premier facteur de (eq67bis), on applique le théorème 5, démontré en profondeur 1 (voir §§4.1 et 5.1). Cette somme s'écrit donc sous la forme $A_2(H_N) + \mathcal{O}_\varepsilon(N^{-1+\varepsilon})$ où $A_2$ est un polynôme tel que $A_2(0)$ soit une combinaison linéaire de 1 et de valeurs de $\zeta$ en des entiers $s$ impairs compris entre 3 et $s_1+s_\vartheta$. En outre $\textup{d}_n ^{s_1+s_\vartheta}$ est un dénominateur commun des coefficients de cette combinaison linéaire.

Comme la divergence logarithmique de $H_N$ est compensée par le $N^\varepsilon$ du terme d'erreur, on peut faire le produit des deux expressions précédentes et obtenir $$\eqref{eq67bis}  =   (A_1A_2)(H_N) + \mathcal{O}_\varepsilon(N^{-1+\varepsilon}).$$ En outre, $A_1A_2(0)$ est bien de la forme voulue. Ceci termine le traitement des termes de la forme ${\mathcal A}_{\underline{\varepsilon}} ^{\vartheta, \gamma}$ dans (eq70), car ces $2^{p+1}(p-1)!$ termes sont répartis en $4(p-1)$ tels groupes.

On va maintenant traiter les termes ${\mathcal B}_{\underline{\varepsilon}, i} ^{\vartheta, \gamma}$ de (eq70). Pour cela, on les groupe deux par deux de la manière suivante. Soient $\vartheta\in \{2,\ldots, p\}$, $\underline{\varepsilon}\in (\mathbb Z/ 2 \mathbb Z)^p$, $\gamma \in {\mathfrak S}_{p-2}$ et $i \in \{1,\ldots, p-2\}$ fixés. On note $\psi_{\vartheta}$ la bijection strictement croissante de $\{1,\ldots, p-2\}$ dans $\{2,\ldots, p\}\setminus\{\vartheta\}$. Posons $\vartheta' = \psi_{\vartheta}(\gamma(i))$, $\alpha = \psi_{\vartheta'}^{-1}(\vartheta)$ et $\beta = \gamma(i) = \psi_{\vartheta}^{-1}(\vartheta')$. On note $(\alpha \, \, \ldots \, \, \beta)$ le cycle $(\alpha \, \, \alpha+1 \, \,  \ldots \, \, \beta-1 \, \, \beta)$ si $\alpha \leq \beta$, et le cycle $(\alpha \, \, \alpha-1 \, \,  \ldots \, \, \beta+1 \, \, \beta)$ si $\alpha > \beta$. On pose $\gamma' = (\alpha \, \, \ldots \, \, \beta)\circ \gamma$. Avec ces notations, on a $\gamma'(i) = \alpha$ d'où $\{\vartheta, \psi_{\vartheta}(\gamma(i))\} = \{\vartheta' , \psi_{\vartheta'}(\gamma'(i))\}$. En outre, la définition de $\gamma'$ montre que pour tout $i' \in \{1,\ldots, p-2\}\setminus\{i\}$ on a $\psi_{\vartheta}(\gamma(i')) = \psi_{\vartheta'}(\gamma'(i'))$. En reportant dans (eq68) on en déduit : $$\label{eq68bis}
{\mathcal B}_{\underline{\varepsilon}, i} ^{\vartheta, \gamma} (\underline{j})= {\mathcal B}_{\underline{\varepsilon}, i} ^{\vartheta', \gamma'} (\underline{j}).$$ Or on voit facilement que $\varepsilon_{\gamma'} = \varepsilon_{\gamma} (-1)^{\beta - \alpha} =  \varepsilon_{\gamma} (-1)^{\vartheta- \vartheta'  - 1}$, d'où $(-1)^\vartheta\varepsilon_\gamma = - (-1)^{\vartheta'} \varepsilon_{\gamma'}$. Donc les deux membres de l'égalité (eq68bis) apparaissent dans (eq70) avec des signes opposés : leurs contributions se neutralisent. Comme l'application $(\vartheta, \gamma) \mapsto (\vartheta', \gamma')$ ainsi définie est involutive, elle permet de grouper deux par deux tous les termes ${\mathcal B}_{\underline{\varepsilon}, i} ^{\vartheta, \gamma} (\underline{j})$ et ${\mathcal B}_{\underline{\varepsilon}, i} ^{\vartheta, \gamma} (\underline{j} + (\varepsilon_1, 0, \ldots, 0))$ apparaissant dans (eq70). Ceci démontre que leur contribution globale est nulle, et termine la preuve du théorème 6.

# Preuve du théorème découplé

Démontrons maintenant le théorème 2. La stratégie générale est la même que pour le théorème 4, mais elle est beaucoup plus facile à mettre en œuvre.

Soit $P(k_1,\ldots,k_p)$ un polynôme de degré $\leq A(n+1)-2$ par rapport à chacune des variables. Comme au paragraphe 4.1, on considère la fraction rationnelle $$\label{eq641}
R(k_1,\ldots, k_p) = \frac{P(k_1,\ldots, k_p)}{(k_1)_{n+1}^A \ldots (k_p)_{n+1}^A}$$ dont la décomposition en éléments simples s'écrit $$\label{eq662}
R(k_1,\ldots, k_p) = \sum_{\tiny {\begin{array}{c} 0 \leq j_1, \ldots, j_p \leq n \\ 1 \leq s_1, \ldots, s_p \leq A \end{array}}}
\frac{C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]}{(k_1+j_1)^{s_1} \ldots (k_p+j_p)^{s_p}}$$ avec des rationnels $C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]$. L'hypothèse faite sur $P$ dans le théorème 2 s'écrit $$R(k_1, \ldots, k_{\ell-1}, -k_\ell-n, k_{\ell+1}, \ldots, k_p) = - R(k_1, \ldots, k_p)
\mbox{ pour tout } \ell \in \{1,\ldots, p\}.$$ Par unicité du développement en éléments simples, elle implique $$\label{eq287}
C\bigg[\,\begin{matrix} s_1, \ldots, s_{\ell-1}, s_\ell, s_{\ell+1}, \ldots, s_p\\j_1, \ldots,  j_{\ell-1}, n-j_\ell, j_{\ell+1}, \ldots, j_p\end{matrix}\,\bigg]= (-1)^{s_\ell+1} C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]$$ pour tous $j_1, \ldots, j_p, s_1, \ldots, s_p$ et pour tout $\ell \in \{1,\ldots, p\}$.

La série (eqdecouple) est la limite, quand $N$ tend vers l'infini, de la somme $$\label{eq288}
\sum_{k_1 = 1} ^N \ldots \sum_{k_p = 1} ^N R(k_1, \ldots, k_p).$$ Pour tout entier $s \geq 1$, posons $$\zeta_N (s) = \sum_{k=1} ^N \frac{1}{k^s}.$$ Pour $s= 1$ c'est la somme harmonique (notée aussi $H_N$), et pour $s \geq 2$ la suite $(\zeta_N (s))$ tend vers $\zeta(s)$ quand $N$ tend vers l'infini. On a, pour tous $(j_1, \ldots, j_p)$ et $(s_1, \ldots, s_p)$ : $$\sum_{1 \leq k_1, \ldots, k_p \leq N}\prod_{i=1} ^p   \frac{1}{(k_i + j_i)^{s_i}}
= \prod_{i=1} ^p \Big( \zeta_{N+j_i}(s_i) - \sum_{k_i = 1} ^{j_i} \frac{1}{k_i^{s_i}} \Big).$$

Donc la somme (eq288) s'écrit $$\label{eq286}
  \sum_{\tiny {\begin{array}{c} 0 \leq j_1, \ldots, j_p \leq n \\ 1 \leq s_1, \ldots, s_p \leq A \end{array}}}
 C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]\prod_{i=1} ^p \Big( \zeta_{N+j_i}(s_i) - \sum_{k_i = 1} ^{j_i} \frac{1}{k_i^{s_i}} \Big).$$

Notons $E = \{0,\ldots, n\}^p \times\{1,\ldots, A\}^p$ et considérons la relation d'équivalence ${\mathscr{R}}$ sur $E$ définie par : $$\begin{array}{l}
(j_1,\ldots, j_p, s_1, \ldots, s_p) \equiv (j'_1,\ldots, j'_p, s'_1, \ldots, s'_p) \, \bmod \, {\mathscr{R}}\\
\\
\quad \quad \mbox{ si, et seulement si, } \\
\\
    \left\{
    \begin{array}{l}
    s_1 = s'_1, \ldots, s_p = s'_p\\
    j_1 \in \{j'_1, n-j'_1\}, \ldots, j_p \in \{j'_p, n-j'_p\}.
    \end{array}
    \right.
\end{array}$$ On peut scinder la somme (eq286) en somme sur les classes d'équivalence[^6] modulo ${\mathscr{R}}$ (puisque celles-ci forment une partition de $E$). Nous allons démontrer que la somme sur chaque classe est de la forme $Q(H_N) + o(1)$ où $Q$ est un polynôme, $H_N$ la somme harmonique et $o(1)$ une suite qui tend vers 0, avec la propriété que $Q(0)$ est un polynôme à coefficients rationnels, de degré au plus $p$, en les $\zeta(s)$, pour $s$ entier impair compris entre 3 et $A$. Quand $N$ tend vers l'infini, la somme (eq286) converge vers (eqdecouple) donc la contribution globale de ces polynômes $Q(H_N)$ sera un polynôme constant, dont la valeur (en 0) est de la forme annoncée dans le théorème 2. Ceci démontrera donc le théorème 2.

Démontrons maintenant ce fait. Soit $(j_1,\ldots, j_p, s_1, \ldots, s_p) \in E$. Pour simplifier les notations, on suppose (quitte à permuter les indices) que $j_1  =  \ldots = j_a = \frac{n}{2}$ et que $j_{a+1}, \ldots, j_p$ sont différents de $n/2$, avec $a \in \{0,\ldots, p\}$ (par exemple $a=0$ dès que $n$ est impair). Alors la classe d'équivalence de $(j_1,\ldots, j_p, s_1, \ldots, s_p)$ modulo ${\mathscr{R}}$ est formée par les $2^{p-a}$ éléments $(\frac{n}{2},\ldots, \frac{n}{2}, j'_{a+1}, \ldots, j'_p, s_1, \ldots, s_p)$ tels que $j'_{a+1} \in \{j_{a+1}, n-j_{a+1}\}$, ..., $j'_p \in \{j_p, n-j_p\}$. Pour $\varepsilon\in \{-1, 1\}$ et $j \in \{0,\ldots, n\}$ on pose (comme au paragraphe 4.1) : $$\left\{
\begin{array}{l}
\varepsilon\cdot j =j \mbox{ si } \varepsilon= + 1,\\
\varepsilon\cdot j =n-j \mbox{ si } \varepsilon= - 1.
\end{array}
\right.$$ Alors ces $2^{p-a}$ éléments s'écrivent $(\varepsilon_1 \cdot j_1, \ldots, \varepsilon_p \cdot j_p, s_1, \ldots, s_p)$ où $(\varepsilon_1, \ldots, \varepsilon_p)$ décrit $\{1\}^a \times\{-1,1\}^{p-a}$ (c'est-à-dire que $\varepsilon_1, \ldots, \varepsilon_a$ valent toujours 1 et que $\varepsilon_{a+1}, \ldots, \varepsilon_p$ peuvent valoir 1 ou $-1$). La relation (eq287) donne alors, pour tout $(\varepsilon_1, \ldots, \varepsilon_p) \in \{1\}^a \times\{-1,1\}^{p-a}$ : $$C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\ \varepsilon_1 \cdot j_1, \ldots, \varepsilon_p \cdot j_p\end{matrix}\,\bigg]= \varepsilon_{a+1}^{s_{a+1}+1} \ldots  \varepsilon_p^{s_p+1} C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg],$$ donc la somme (eq286) restreinte à la classe d'équivalence de $(j_1,\ldots, j_p, s_1, \ldots, s_p)$ est le produit de $C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]$ par : $$\begin{aligned}
\lefteqn{\sum_{(\varepsilon_1, \ldots, \varepsilon_p) \in \{1\}^a \times\{-1,1\}^{p-a}} \varepsilon_{a+1}^{s_{a+1}+1} \ldots  \varepsilon_p^{s_p+1}
 \prod_{i=1} ^p \Big( \zeta_{N + \varepsilon_i \cdot j_i} (s_i) - \sum_{k_i = 1} ^{\varepsilon_i \cdot j_i} \frac{1}{k_i^{s_i}} \Big)}
\nonumber \\
& = & \Big(   \prod_{i=1} ^a ( \zeta_{N + \frac{n}{2}} (s_i) - \sum_{k_i = 1} ^{n/2} \frac{1}{k_i^{s_i}} ) \Big)
 \sum_{(\varepsilon_{a+1}, \ldots, \varepsilon_p) \in \{-1,1\}^{p-a}}  \prod_{i=a+1} ^p \varepsilon_i^{s_i+1}  ( \zeta_{N + \varepsilon_i \cdot j_i} (s_i) - \sum_{k_i = 1} ^{\varepsilon_i \cdot j_i} \frac{1}{k_i^{s_i}} ) \\
& = & \Big(   \prod_{i=1} ^a ( \zeta_{N + \frac{n}{2}} (s_i) - \sum_{k_i = 1} ^{n/2} \frac{1}{k_i^{s_i}} ) \Big)
\prod_{i=a+1} ^p \sum_{\varepsilon_i \in \{-1,1\}} \Big(  \varepsilon_i^{s_i+1} \zeta_{N + \varepsilon_i \cdot j_i} (s_i) -  \varepsilon_i^{s_i+1} \sum_{k_i = 1} ^{\varepsilon_i \cdot j_i} \frac{1}{k_i^{s_i}} \Big) \\
& = & \Big(   \prod_{i=1} ^a ( \zeta_{N + \frac{n}{2}} (s_i) - \sum_{k_i = 1} ^{n/2} \frac{1}{k_i^{s_i}} ) \Big)
\prod_{i=a+1} ^p \Big( \zeta_{N+j_i}(s_i) +(-1)^{s_i+1}  \zeta_{N+n-j_i} (s_i) \\
&& \hspace{7cm}    -  \sum_{k_i = 1} ^{ j_i} \frac{1}{k_i^{s_i}} - (-1)^{s_i+1}   \sum_{k_i = 1} ^{n- j_i} \frac{1}{k_i^{s_i}}  \Big)\\
& = & \Big(   \prod_{i=1} ^a ( \zeta_{N} (s_i) - \sum_{k_i = 1} ^{n/2} \frac{1}{k_i^{s_i}} + \mathcal{O}(\frac{1}{N}) ) \Big)
\prod_{i=a+1} ^p \Big( (1+(-1)^{s_i+1}) \zeta_N(s_i) + \mathcal{O}(\frac{1}{N})  \\
&& \hspace{7cm}    -  \sum_{k_i = 1} ^{ j_i} \frac{1}{k_i^{s_i}} - (-1)^{s_i+1}   \sum_{k_i = 1} ^{n- j_i} \frac{1}{k_i^{s_i}}  \Big),

\end{aligned}$$ puisque $\zeta_{N+1}(s) = \zeta_N(s) +\mathcal{O}(1/N)$. Ce produit est bien de la forme $Q(H_N) + o(1)$, où $Q$ est un polynôme (à coefficients réels) tel que $$Q(0) =  \Big(   \prod_{i=1} ^a ( \zeta _*(s_i) - \sum_{k_i = 1} ^{n/2} \frac{1}{k_i^{s_i}}) \Big)
\prod_{i=a+1} ^p \Big( (1+(-1)^{s_i+1}) \zeta _*(s_i)   -  \sum_{k_i = 1} ^{ j_i} \frac{1}{k_i^{s_i}} - (-1)^{s_i+1}   \sum_{k_i = 1} ^{n- j_i} \frac{1}{k_i^{s_i}}  \Big)$$ avec $\zeta _*(1) = 0$ et $\zeta _*(s) = \zeta(s)$ pour $s \geq 2$ (comme au paragraphe 3.1).

Si l'un au moins parmi $s_1$, ..., $s_a$ est pair, alors la relation (eq287) montre que le coefficient $C\bigg[\,\begin{matrix} s_1, \ldots, s_p\\j_1, \ldots, j_p\end{matrix}\,\bigg]$ est nul, donc la classe d'équivalence de $(j_1,\ldots, j_p, s_1,
\ldots, s_p)$ ne contribue pas à la somme (eq286). On peut donc supposer que $s_1$, ..., $s_a$ sont tous impairs. Or l'expression ci-dessus de $Q(0)$ ne fait apparaı̂tre, parmi les $\zeta(s_{i})$ avec $i \in \{a+1 , \ldots, p\}$, que ceux tels que $s_i$ soit impair ; en outre ceux parmi $s_1$, ..., $s_p$ qui valent 1 disparaissent car $\zeta _*(1) = 0$. Donc la contribution de la classe d'équivalence de $(j_1,\ldots, j_p, s_1, \ldots, s_p)$ à la somme (eq286) est bien de la forme $Q(H_N)  + o(1)$, où $Q(0)$ est un polynôme à coefficients rationnels, de degré au plus $p$, en les $\zeta(s)$, pour $s$ entier impair compris entre 3 et $A$. Comme remarqué ci-dessus, cela termine la preuve du théorème 2.

10

[R. Apéry] -- "Irrationalité de $\zeta(2)$ et $\zeta(3)$", in *Journées Arithmétiques (Luminy, 1978)*, Astérisque, no. 61, 1979, p. 11--13.

[K. Ball & T. Rivoal] -- " Irrationalité d'une infinité de valeurs de la fonction zêta aux entiers impairs", *Invent. Math.* **146** (2001), no. 1, p. 193--207.

[G. Bhatnagar & M. Schlosser] -- "$C_n$ and $D_n$ very well-poised ${}_{10}\phi_9$ transformations", *Constr. Approx.* **14** (1998), p. 531--567.

[H. Coksun] -- "An Elliptic $BC_n$ Bailey Lemma, Multiple Rogers--Ramanujan Identities and Euler's Pentagonal Number Theorems", à paraı̂tre dans *Trans. AMS*, prépublication disponible sur ArXiv :\
`http://front.math.ucdavis.edu/math.CO/0605653`, 2006.

[P. Colmez] -- "Arithmétique de la fonction zêta", in *Journées mathématiques X-UPS 2002*, éditions de l'école Polytechnique, 2003, http://math.polytechnique.fr/xups/volumes.html, p. 37--164.

[J. Cresson, S. Fischler & T. Rivoal] -- Algorithme disponible sur\
`http://www.math.u-psud.fr/~fischler/algo.html`.

--- , "Séries hypergéométriques multiples et polyzêtas", Bulletin de la Soc. Math. de France, à paraı̂tre.

[S. Fischler] -- "Irrationalité de valeurs de zêta (d'après Apéry, Rivoal, \...)", in *Sém. Bourbaki 2002/03*, Astérisque **294**, 2004, exp. no. 910, p. 27--62.

--- , "Multiple series connected to Hoffman's conjecture on multiple zeta values", prépublication disponible sur ArXiv :\
`http://front.math.ucdavis.edu/math.NT/0609799`, 2006.

[A. Goncharov] -- "Multiple polylogarithms and mixed Tate motives", prépublication disponible sur ArXiv : `http://front.math.ucdavis.edu/math.AG/0103059`, 2001.

[M. Hoffman] -- "Multiple harmonic series", *Pacific J. of Math.* **152** (1992), p. 275--290.

[J. E. Humphreys] -- "Reflection Groups and Coxeter Groups ", Cambrdge studies in advanced mathematics **29**, 1990.

[C. Krattenthaler & T. Rivoal] -- " Hypergéométrie et fonction zêta de Riemann", Memoirs of the AMS **186** (2007), 93 pages.

[G. Racinet] -- "Doubles mélanges des polylogarithmes multiples aux racines de l'unité", *Publ. Math. Inst. Hautes Études Sci.* **95** (2002), p. 185--231.

[G. Rhin & C. Viola] -- "The group structure for $\zeta(3)$", *Acta Arith.* **97** (2001), no. 3, p. 269--293.

[T. Rivoal] -- "La fonction zêta de Riemann prend une infinité de valeurs irrationnelles aux entiers impairs", *C. R. Acad. Sci. Paris, Ser. I* **331** (2000), no. 4, p. 267--270.

[V. Sorokin] -- "Apéry's theorem", *Vestnik Moskov. Univ. Ser. I Mat. Mekh. \[Moscow Univ. Math. Bull.\]* **53** (1998), no. 3, p. 48--53 \[48--52\].

[T. Terasoma] -- "Mixed Tate motives and multiple zeta values", *Invent. Math.* **149** (2002), no. 2, p. 339--369.

[D. Vasilyev] -- "Approximations of zero by linear forms in values of the Riemann zeta-function", *Doklady Nats. Akad. Nauk Belarusi* **45** (2001), no. 5, p. 36--40, en russe ; version étendue en anglais : *On small linear forms for the values of the Riemann zeta-function at odd points*, prépublication no.1 (558), Nat. Acad. Sci. Belarus, Institute Math., Minsk (2001), 14 pages.

[M. Waldschmidt] -- "Valeurs zêta multiples : une introduction", *J. Théor. Nombres Bordeaux* **12** (2000), no. 2, p. 581--595.

[S. Zlobin] -- "Expansion of multiple integrals in linear forms", *Mat. Zametki \[Math. Notes\]* **77** (2005), no. 5, 683--706 \[630--652\].

--- , "Properties of coefficients of certain linear forms in generalized polylogarithms", *Fundamentalnaya i Prikladnaya Matematika \[Fundamental and Applied Mathemetics\]* **11** (2005), no. 6, p. 41--58, Disponible sur ArXiv : `http://front.math.ucdavis.edu/math.NT/0511245`.

[W. Zudilin] -- "One of the numbers $\zeta(5)$, $\zeta(7)$, $\zeta(9)$, $\zeta(11)$ is irrational", *Uspekhi Mat. Nauk \[Russian Math. Surveys\]* **56** (2001), no. 4, p. 149--150 \[774--776\].

--- , "Irrationality of values of the Riemann zeta function", *Izvestiya RAN Ser. Mat. \[Izv. Math.\]* **66** (2002), no. 3, p. 49--102 \[489--542\].

--- , "Well-poised hypergeometric service for diophantine problems of zeta values", *J. Théor. Nombres Bordeaux* **15** (2003), no. 2, p. 593--626.

J. Cresson, Laboratoire de Mathématiques appliquées de Pau, Bâtiment I.P.R.A, Université de Pau et des Pays de l'Adour, avenue de l'Université, BP 1155, 64013 Pau cedex, France.

S. Fischler, Univ. Paris-Sud, Laboratoire de Mathématiques, UMR CNRS 8628, Bâtiment 425, 91405 Orsay cedex, France.

T. Rivoal, Institut Fourier, CNRS UMR 5582, Université Grenoble 1, 100 rue des Maths, BP 74, 38402 Saint-Martin d'Hères cedex, France.

[^1]: Dans cet article, nous utilisons indifféremment les mots *(very) well-poised* ou leur traduction française *(très) bien équilibré*.

[^2]: Quand on applique l'algorithme de [@CFRalgo], on trouve une forme linéaire en 1 et $\zeta(2,1)$ ; il faut alors utiliser la relation $\zeta(2,1) = \zeta(3)$. De plus, Sorokin travaille à l'aide d'une expression intégrale alternative de cette somme.

[^3]: Pour simplifier, nous ne démontrons ici le théorème 3 que dans le cas où $n$ est pair : voir la remarque 2. Cependant, il nous semble raisonnable d'espérer que ce théorème soit vrai aussi quand $n$ est impair.

[^4]: Ce résultat, comme les théorèmes 5 et 6 ci-dessous, ne sera démontré ici que dans le cas où $n$ est pair. Ceci permet de simplifier la preuve (voir la remarque 2) et ne devrait pas être un obstacle à d'éventuelles applications diophantiennes. Cependant, il nous semble raisonnable d'espérer que ces énoncés soient vrais aussi quand $n$ est impair.

[^5]: Plus précisément, nous démontrerons au §5 le théorème 6, qui est une forme plus précise du théorème 5, et nous en déduirons le théorème 4 au paragraphe 4.4.

[^6]: Il s'agit des orbites sous l'action de $(\mathbb Z/ 2 \mathbb Z)^p$ sur $E$ définie au paragraphe 4.1.
