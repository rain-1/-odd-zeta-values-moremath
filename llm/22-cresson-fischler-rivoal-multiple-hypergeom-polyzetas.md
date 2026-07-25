---
title: "Séries hypergéométriques multiples et polyzêtas"
authors:
  - "Jacky Cresson"
  - "Stephane Fischler"
  - "Tanguy Rivoal"
arxiv_id: "math/0609743v1"
arxiv_url: "https://arxiv.org/abs/math/0609743"
published: "2006-09-27"
journal_ref: ""
doi: ""
source: "papers/22-cresson-fischler-rivoal-multiple-hypergeom-polyzetas/CFRalgo-HAL.tex"
conversion: pandoc-flat
---

# Séries hypergéométriques multiples et polyzêtas

**Jacky Cresson, Stephane Fischler, Tanguy Rivoal**

## Abstract

We describe a theoretical and effective algorithm which enables us to prove that rather general hypergeometric series and integrals can be decomposed as linear combinations of multiple zeta values, with rational coefficients.

---
We describe a theoretical and effective algorithm which enables us to prove that rather general hypergeometric series and integrals can be decomposed as linear combinations of multiple zeta values, with rational coefficients.

# Introduction

Une généralisation de la fonction zêta de Riemann $\zeta(s)$ est donnée par les séries *polyzêtas*, définies pour tout entier $p\ge 1$ et tout $p$-uplet $\underline{s}=(s_1, s_2, \dots, s_p)$ d'entiers $\ge 1$, avec $s_1\ge 2$, par $$\zeta(s_1, s_2, \ldots, s_p)=
\sum_{k_1> k_2>\cdots > k_p\ge 1}
\frac{1}{k_1^{s_1}k_2^{s_2}\cdots k_p^{s_p}}.$$ Les entiers $p$ et $s_1+s_2+\cdots+s_p$ sont respectivement la profondeur et le poids de $\zeta(s_1, s_2, \ldots, s_p)$. Pour diverses raisons, il est plus simple de considérer que la sommation est faite sur $k_1\ge k_2\ge \cdots\ge k_p \ge 1$ : nous noterons $\overline{\zeta}(s_1, s_2, \ldots, s_p)$ les séries ainsi obtenues. Il est à noter que les deux séries convergent plus généralement pour des exposants complexes vérifiant $\sum _{j=1} ^{r}\Re(s_{j})> r$ pour tout $r\in\{1,\dots,p\}$, ce qui autorise à avoir des exposants entiers négatifs par exemple.

Les polyzêtas interviendront dans cet article par l'intermédiaire des fonctions polylogarithmes multiples, définies par $$\operatorname{Li}_{s_1, s_2 \ldots, s_p}(z_1, z_2,\ldots, z_p)=
\sum_{ k_1> k_2 >\cdots > k_p\ge 1}
\frac{z_1^{k_1}z_2^{k_2}\cdots z_p^{k_p}}{k_1^{s_1}k_2^{s_2}
\cdots k_p^{s_p}}$$ pour $\vert z_1\vert\le 1, \ldots,
\vert z_p\vert \le 1$. On obtiendra en fait les résultats pour les polylogarithmes multiples larges, définis par $$\textup{La}_{s_1, s_2\ldots, s_p}(z_1, z_2\ldots, z_p)=
\sum_{ k_1 \ge k_2\ge \cdots \ge k_p\ge 1}
\frac{z_1^{k_1}z_2^{k_2}\cdots z_p^{k_p}}{k_1^{s_1}k_2^{s_2}
\cdots k_p^{s_p}}.$$ Lorsque $p=1$, les deux variantes coı̈ncident avec les polylogarithmes usuels et si $z_1=z_2=\cdots =z_p=1$ et $s_1 \geq 2$, on a $\operatorname{Li}_{s_1, s_2\ldots, s_p}(1, 1, \ldots, 1)=\zeta(s_1,s_2\ldots, s_p)$ et $\textup{La}_{s_1, s_2\ldots, s_p}(1,1, \ldots, 1)=\overline{\zeta}(s_1,s_2\ldots, s_p).$ Un théorème d'Ulanskiı̆ [@ulanskii] permet de passer linéairement d'un type de série à l'autre ; en vue d'applications diophantiennes, on ne perd donc rien à considérer une variante plutôt qu'une autre.

Remarquons dès à présent que les fonctions polylogarithmes multiples peuvent être définies pour des exposants $s_i$ complexes, à condition de supposer en plus que $\vert z_1\vert <1$ pour des raisons de convergence. En particulier, nous utiliserons ces fonctions avec des $s_j \in \mathbb{Z}$ : par définition, le poids d'une telle fonction est alors $\sum_{j=1}^p \max(s_j,0).$

On voit naturellement apparaı̂tre les polyzêtas lorsque, par exemple, on considère les produits des valeurs de la fonction zêta : on a $\zeta(n)\zeta(m)=\zeta(n+m)+\zeta(n,m)+\zeta(m,n)$, ce qui permet en quelque sorte de linéariser ces produits. En dehors de quelques identités telles que $\zeta(2,1)=\zeta(3)$ (due à Euler), la nature arithmétique de ces séries est aussi peu connue que celle des nombres $\zeta(s)$. Cependant, l'ensemble des nombres $\zeta(\underline s)$ possède une très riche structure algébrique assez bien comprise, au moins conjecturalement (voir [@miw]). Par exemple, on peut s'intéresser aux $\mathbb{Q}$-sous-espaces vectoriels $\mathcal{Z}_p$ de $\mathbb{R}$, engendrés par les $2^{p-2}$ polyzêtas de poids $p\ge 2$ : $\mathcal{Z}_2=\mathbb{Q}\zeta(2)$, $\mathcal{Z}_3=\mathbb{Q}\zeta(3)+\mathbb{Q}\zeta(2,1)$, $\mathcal{Z}_4=\mathbb{Q}\zeta(4)+\mathbb{Q}\zeta(3,1)+
\mathbb{Q}\zeta(2,2)+
\mathbb{Q}\zeta(2,1,1)$, etc. Posons $v_p=\textup{dim}_{\mathbb{Q}}(\mathcal{Z}_p)$. On a alors la

**Conjecture 1**. *$(i)$ Pour tout entier $p\ge 2$, on a $v_p=c_p$, où l'entier $c_p$ est défini par la récurrence de type Fibonacci $c_{p+3}=c_{p+1}+c_{p}$, avec $c_0=1$, $c_1=0$ et $c_2=1$.*

*$(ii)$ Les $\mathbb{Q}$-espaces vectoriels $\mathbb{Q}$ et $\mathcal{Z}_p$ ($p\ge 2)$, sont en somme directe.*

La suite $(v_p)_{p\ge 2}$ devrait donc croı̂tre comme $\alpha^p$ (où $\alpha\approx
1,3247$ est racine du polynôme $X^3-X-1$), ce qui est bien plus petit que $2^{p-2}$. Il y a donc conjecturalement beaucoup de relations linéaires entre les polyzêtas de même poids et aucune en poids différents : dans cette direction, un théorème de Goncharov [@goncharov1] et Terasoma [@terasoma] affirme que l'on a $v_p\le c_p$ pour tout entier $p\ge 2$. Il reste donc à montrer l'inégalité inverse pour montrer (i) mais aucune minoration non triviale de $v_p$ n'est connue à ce jour : si l'on montre facilement que $v_2=v_3=v_4=1$, on est bloqué dès l'égalité $v_5=2$, qui est équivalente à l'irrationalité toujours inconnue de $\zeta(5)/(\zeta(3)\zeta(2))$. Plus généralement, un des intérêts de la conjecture 1 est d'impliquer la suivante.

**Conjecture 2**. *Les nombres $\,\pi, \zeta(3), \zeta(5), \zeta(7), \zeta(9),$ etc, sont algébriquement indépendants sur $\mathbb{Q}$.*

Cette conjecture semble actuellement totalement hors de portée. Un certain nombre de résultats diophantiens ont néanmoins été obtenus en profondeur 1, c'est-à-dire dans le cas de la fonction zêta de Riemann :

-   Le nombre $\zeta(3)$ est irrationnel (Apéry [@ap]) ;

-   La dimension de l'espace vectoriel engendré sur $\mathbb{Q}$ par 1, $\zeta(3)$, $\zeta(5), \ldots, \zeta(A)$ (avec $A$ impair) croı̂t au moins comme $\log(A)$ ([@br; @ri]) ;

-   Au moins un des quatre nombres $\zeta(5), \zeta(7), \zeta(9), \zeta(11)$ est irrationnel (Zudilin [@zud]).

Ces résultats peuvent être obtenus par l'étude de certaines séries de la forme [^1] $$\label{eq:serie simple generale}
\sum_{k=1}^{\infty} \frac{P(k)}{k^A(k+1)^A\cdots (k+n)^A} \,z^{-k}$$ avec $P(X)\in\mathbb{Q}[X]$, $n\ge0$, $A\ge 1$ et $\vert z \vert\ge 1$ (le choix de $1/z$ plutôt que $z$ est purement technique) : nous rappelons sommairement au paragraphe 3.1 comment on utilise ces séries pour les démontrer, en exploitant le fait que, génériquement, elles s'expriment aussi comme combinaisons linéaires des valeurs de zêta aux entiers lorsque $z=1$. Les divers choix de $P$ conduisent à des *séries hypergéométriques généralisées* : voir les ouvrages [@ba; @sl] pour les définitions, qui ne sont pas essentielles ici.

Notre but est de poser les bases d'une généralisation de cette méthode hypergéométrique en profondeur quelconque en considérant *a priori* des séries multiples de la forme $$\label{eq:serie mult generale}
\sum_{k_1\ge \cdots \ge k_p\ge 1}
\frac{P(k_1, \ldots, k_p)}{(k_1)_{n_1+1}^{A_1}
\cdots (k_p)_{n_p+1}^{A_p}}\,z_1^{-k_1}
\cdots z_p^{-k_p},$$ avec $P(X_1,\ldots, X_p)\in\mathbb{Q}[X_1,\ldots, X_p]$, des entiers $A_j\ge 1$ et $n_j\ge 0$ et $\vert z_1\vert\ge 1, \ldots,
\vert z_p\vert \ge 1$, ceci dans l'espoir qu'elles s'expriment comme combinaisons linéaires de polyzêtas intéressants lorsque $z_1= \cdots =z_p=1$. (Pour raccourcir les expressions, on a utilisé le symbole de Pochhammer $(\alpha)_m=\alpha(\alpha+1)\cdots (\alpha+m-1)$.) On pourrait imaginer généraliser encore (eq:serie mult generale) en remplaçant, au dénominateur, chaque facteur $(k_i)_{n_i+1}^{A_i}$ par $(k_i+r_i)_{n_i+1}^{A_i}$. Cela peut être utile (et nos méthodes le permettent) si des bornes explicites apparaissent en fonction des $n_i$, mais pour des résultats qualitatifs c'est inutile car on peut s'y ramener, en remplaçant $n_i$ par $n_i + r_i$ et en multipliant le numérateur par $(k_i)_{r_i} ^{A_i}$.

Les séries de la forme (eq:serie mult generale) apparaissent naturellement dans la littérature. Par exemple, Sorokin [@so1] a déduit l'irrationalité de $\zeta(3)$ d'un résultat que l'on peut écrire ainsi (voir §2.2) : pour tout entier $n\ge 0$, on a $$\label{eq:sorokin1}
n! \sum_{k_1\ge k_2\ge 1}
 \frac{(k_2-n)_n(k_1-k_2+1)_n }{(k_1)_{n+1}^2(k_2)_{n+1}} =
2a_n\zeta(2,1)-b_n,$$ où $a_n$ et $b_n$ sont les célèbres nombres rationnels utilisés par Apéry [@ap] dans sa preuve originelle de l'irrationalité de $\zeta(3)$. La méthode de Sorokin n'utilise pas directement la série (eq:sorokin1) mais consiste à résoudre un subtil problème d'approximation de Padé, qu'il n'est malheureusement pas facile de généraliser à d'autres situations. Nous nous affranchissons de l'approximation de Padé pour espérer profiter, en profondeur supérieure, de la grande souplesse de la méthode hypergéométrique en profondeur 1. Il est intéressant de noter que la série double en (eq:sorokin1) est un exemple de *série hypergéométrique de Kampé de Fériet* (voir [@srivastava p. 27]), comme on le voit après quelques transformations triviales du sommande. Par un léger abus de langage, nous appelons série hypergéométrique multiple une expression de la forme (eq:serie mult generale) bien que, en général, il ne s'agisse seulement que de combinaisons linéaires rationnelles de telles séries.

Un ingrédient, fréquemment utilisé avec des séries simples, consiste à dériver la fraction rationnelle en $k$ dans la série (eq:serie simple generale), avant de sommer ; par exemple, une double dérivation sert à démontrer le résultat de Zudilin [@zud] rappelé après la conjecture 2. Cette astuce, appliquée plusieurs fois, permet de faire disparaı̂tre $\zeta(s)$ de la forme linéaire obtenue, pour de petites valeurs de $s$. On peut imaginer l'utiliser pour des sommes multiples, même si on n'a aucun résultat connu de disparition de polyzêtas dans ce cadre. Il est clair qu'en dérivant une fraction rationnelle de la forme $P(X_1, \ldots, X_p)/\big((X_1)_{n+1}^{A_1} \ldots (X_p)_{n+1}^{A_p} \big)$ par rapport à l'une des variables $X_j$, on obtient une fraction rationnelle de la même forme (avec $A_j$ remplacé par $A_j+1$) : cette remarque montre que l'on ne perd rien à considérer des séries de la forme (eq:serie mult generale).

En profondeur $p\ge2$, l'étude des séries multiples du type de (eq:serie mult generale) se décompose en plusieurs étapes et, malheureusement, la première difficulté se présente dès la première étape, qui est pourtant triviale en profondeur 1. Nous mettons ceci en évidence sur l'exemple de la profondeur 2 au paragraphe 3.2 : la généralisation en profondeur quelconque nécessite la production d'un algorithme récursif (permettant de déduire le cas de la profondeur $p$ du cas de la profondeur $p-1$) que l'on décrit au paragraphe 4.3. Informellement, on obtient alors le résultat suivant.

**Théorème 1**. *Supposons que l'on ait $\vert z_1 \vert >1$ et $\vert z_j \vert \ge  1$ pour tout $j=2,\dots ,p$. Alors, toute série de la forme (eq:serie mult generale) s'écrit comme une combinaison linéaire à coefficients polynômes de Laurent dans $\mathbb{Q}[z_1^{\pm 1}, \ldots, z_p^{\pm 1}]$ en les polylogarithmes multiples $\textup{La}_{s_1, \ldots, s_q}(1/\widehat z_1,\ldots, 1/\widehat z_q)$ où $0\le q\le p$, $\sum_{j=1} ^q \max(s_j,0) \le \sum_{j=1} ^p A_j$ et où les $\widehat z_1,\ldots, \widehat z_q$ sont certains produits des $z_1, \ldots, z_p.$*

**Remarque 1**. *$(1)$ Bien que peu surprenant en apparence, ce résultat est, comme on le verra, loin d'être facile à démontrer. Ici, les entiers $s_1$, ..., $s_q$ peuvent être de signe quelconque et, comme dans toute la suite, on doit entendre un polylogarithme de profondeur $0$ comme étant la fonction identiquement égale à $1$.*

*$(2)$ Certains des $s_j$ peuvent être négatifs ou nuls : cela ne peut être le cas que si l'un des degrés en l'une des variables $X_j$ de la fraction $P(X_1,  \ldots, X_p)/
\big((X_1)_{n_1+1}^{A_1} \cdots (X_p)_{n_p+1}^{A_p}\big)$ est positif, c'est-à-dire lorsque $\textup{deg}_{X_j}(P)\ge A_j(n_j+1)$.*

*$(3)$ On peut raffiner ce théorème : voir le Théorème 6 au paragraphe 5. Il en résulte par exemple que les polynômes de Laurent sont en fait toujours dans $\mathbb{Q}[z_1, z_2^{\pm 1}, \ldots, z_p^{\pm 1}]$.*

Une deuxième difficulté provient du fait que certains polylogarithmes multiples peuvent avoir un ou des exposants $s_j
\le 0$, ce qui nécessite un traitement à part. On obtient le résultat dit de *non-enrichissement* suivant (voir le paragraphe 6): *Lorsque les modules de $z_{1}, \ldots, z_{p}$ sont tous différents de $1$, tout polylogarithme multiple $\textup{La}_{s_1, \ldots, s_p}(\underline z)$, de profondeur $p$ et ayant certains exposants $\le 0$, est une combinaison linéaire en des polylogarithmes multiples d'indices $\ge 1$ (en des produits des $z_j$) de poids $\le \sum_{j=1}^p \max(s_j,0)$, dont les coefficients sont des polynômes à coefficients rationnels en les $\displaystyle\big((1-z_{j_1}\cdots z_{j_m})^{-1}\big)_{1\le j_1< \cdots < j_m\le p,\, m\ge 1}$ et les $(z_j^{\pm 1})_{1\le j\le p}$.*

En combinant ce résultat et le théorème 1 on obtient l'énoncé suivant (qui a été obtenu indépendamment, dans le cas particulier $z_1 = \ldots = z_p$, par Zlobin [@ZlobinZametki2005]) :

**Théorème 2**. *Supposons que pour tout $j=1,\dots ,p$, on ait $\vert z_j \vert > 1$. Alors, toute série de la forme (eq:serie mult generale) s'écrit comme une combinaison linéaire à coefficients polynômes à coefficients rationnels en les $\displaystyle\big((1-z_{j_1}\cdots z_{j_m})^{-1}\big)_{1\le j_1< \cdots < j_m\le p,\, m\ge 1}$ et les $(z_j^{\pm 1})_{1\le j\le p}$ de polylogarithmes multiples $\textup{La}_{s_1, \ldots, s_q}(1/\widehat z_1,\ldots, 1/\widehat z_q)$ où $0\le q\le p$, $s_i \geq 1$ pour $i=1,\dots ,q$, $\sum_{j=1} ^q s_j \le \sum_{j=1} ^p A_j$ et où les $\widehat z_1,\ldots, \widehat z_q$ sont certains produits des $z_1, \ldots, z_p.$*

L'analogue des théorèmes 1 et 2 lorsque $z_1=\dots =z_p =1$ s'énonce comme suit. Une version plus précise (le théorème 9) sera démontrée au paragraphe 7.5; la démonstration nécessite d'utiliser la régularisation des polyzêtas divergents. Ce théorème est celui que nous avons implémenté dans [@algo], ce qui nous a permis d'avoir l'idée du théorème 4 ci-dessous et d'observer d'autres exemples de séries qui font apparaı̂tre seulement certains des polyzêtas attendus [@fialgo].

**Théorème 3**. *Toute série convergente de la forme ((eq:serie mult generale)) s'écrit lorsque $z_1=\dots =z_p =1$ comme une combinaison linéaire à coefficients rationnels en les polyzêtas $\zeta (s_1 ,\dots ,s_q )$ où $0\leq q\leq p$, $s_1 \geq 2$, $s_i \geq 1$ pour $i=1,\dots ,q$ et $\sum_{j=1}^q s_j \leq \sum_{j=1}^p A_j$.*

Notre algorithme donne diverses précisions sur les théorèmes 1, 2 et 3 (dénominateurs des coefficients, degré des polynômes dans le cas des séries les plus simples, dites briques). De plus, il se prête (pour tous $z_1$, ..., $z_p$) à une implémentation informatique que nous avons effectuée [@algo] (lorsque $z_1=\dots =z_p =1$) à l'aide du programme GP/Pari : cela nous a permis de tester de nombreuses séries et d'obtenir des résultats tels que $$\begin{gathered}
\label{eq:exemplehorrible}
\sum_{k_1\ge k_2\ge 1} \frac{5k_2^2-k_1^2-4k_1k_2-3k_1+7k_2}{(k_1)_{3}^4\;(k_2+1)_{4}^3}
\\= -\frac{153060027667}{1289945088} + \frac{832127737}{17915904}\, \zeta(2)
+ \frac{33349589}{2985984} \,\zeta(3) + \frac{10561397}{2985984} \,\zeta(4)
\\
+ \frac{117277}{10368} \,\zeta(5)
+ \frac{1475}{1728} \,\zeta(6) + \frac{757}{432} \,\zeta(7)
+ \frac{6125}{1728} \,\zeta(2,2)
\\
+ \frac{245}{24}\,\zeta(2,3) + \frac{35}{32} \,\zeta(3,2)
+ \frac16 \,\zeta(3,3) + \frac{595}{864}\,\zeta(4,2) + \frac74 \,\zeta(4,3).
\\
\end{gathered}$$ Ce résultat pourrait éventuellement être un peu simplifié en utilisant les relations linéaires connues entre polyzêtas.

Une fois cette étape franchie, une troisième difficulté provient de la profusion de polyzêtas qui semblent apparaître spontanément dans des exemples au hasard comme (eq:exemplehorrible). Nous avons donc été conduits à rechercher une classe de polynômes $P(X_1,\ldots, X_p)$ tels que, *a priori*, seulement certains polyzêtas intéressants ont un coefficient non-nul à la sortie de l'algorithme. Par intéressants , nous entendons des polyzêtas qui ne sont pas trivialement des puissances de $\pi$, qui parasitent les applications diophantiennes en les rendant triviales. [^2] Voici quelques exemples de séries qui ne font pas apparaître $\pi$ : $$\begin{gathered}
\sum_{k_1\ge k_2\ge 1} (k_1+1)(k_2+1)\frac{(k_1-k_2-1)_3(k_1+k_2+1)_3(k_1-1)_5(k_2-1)_5}
{(k_1)_3^5\;(k_2)_3^5}
\\
= \frac{27875}{8192}-\frac{2847}{1024}\,\zeta(3) -\frac{15}{32}\,\zeta(5)+\frac{27}{64}\,\zeta(7),
\end{gathered}$$ $$\begin{gathered}
\sum_{k_1\ge k_2\ge 1} \big(k_1+\frac 12\big)\big(k_2+\frac 12\big)\frac{(k_1-k_2-1)_3(k_1+k_2)_3(k_1-1)_4(k_2-1)_4}
{(k_1)_3^7\;(k_2)_3^7}
\\
= -1156 +891\,\zeta(3)+ \frac{189}2 \,\zeta(5) + 78 \big(\zeta(5,3) -\zeta(3,5)\big),
\end{gathered}$$ $$\begin{gathered}
\sum_{k_1\ge k_2\ge 1} \frac{(k_1-k_2)(k_1+k_2+4)(k_1-2)_9(k_2-2)_9}
{(k_1)_5^{4}\;(k_2)_5^{4}}
\\
= -\frac{642739948033}{41278242816}+\frac{10214719}{995328}\,\zeta(3)
+ \frac{57497}{18432}\,\zeta(5),
\end{gathered}$$ $$\begin{gathered}
\sum_{k_1\ge k_2\ge 3\ge 1}\big(k_1+\frac12\big)\big(k_2+ \frac12\big)\big(k_3+\frac12\big)
\\
\times \frac{(k_1-k_2)(k_2-k_3)(k_1-k_3)
(k_1+k_2+1)(k_1+k_3+1)(k_2+k_3+1)}{(k_1)_2^4\;(k_2)_2^4\;(k_3)_2^4}
\\
= -\frac{1}{4} - \zeta(3) + \frac14 \,\zeta(5) + \zeta(3)^2 -\frac14 \,\zeta(7).
\end{gathered}$$ Nous avons proposé dans [@CFRsym] une généralisation en profondeur quelconque, des séries *very-well-poised* [^3] (ou *très bien équilibrées*) introduites en profondeur 1 ; elle explique les quatre exemples ci-dessus. Il s'agit du résultat suivant, qui est démontré sous une forme plus précise dans [@CFRsym].

**Théorème 4**. *Fixons trois entiers $A\ge 2$, $n \ge 0$ et $p \ge 1$, ainsi que $P(X_1, \ldots, X_p) \in\mathbb{Q}[X_1, \ldots, X_p]$ un polynôme tel que : $$P(X_{\sigma(1)}, X_{\sigma(2)},\ldots, X_{\sigma(p)})
= \varepsilon(\sigma) P(X_1, X_2, \ldots, X_p)$$ pour tout $\sigma \in \mathfrak{S}_p$ (où $\varepsilon(\sigma)$ désigne la signature de $\sigma$), et $$\begin{gathered}
\quad P(X_1,\ldots, X_{j-1}, -X_j-n, X_{j+1}, \ldots, X_p )
\\
= (-1)^{A(n+1)+1} P( X_1,\ldots, X_{j-1}, X_j, X_{j+1}, \ldots, X_p )\quad
\end{gathered}$$ pour tout $j \in \{1, \ldots, p\}.$ On suppose que $P$ est de degré au plus $A(n+1)-2$ par rapport à chacune des variables. Alors la série $$\sum_{k_1\ge \cdots \ge k_p\ge 1}
\frac{P(k_1,  \ldots, k_p)}{(k_1)_{n+1}^{A} \cdots (k_p)_{n+1}^{A}}$$ est convergente et c'est un polynôme à coefficients rationnels en les quantités $$\label{eqzetaas}
\sum_{\sigma\in\mathfrak{S}_q} \varepsilon(\sigma) \,\zeta(s_{\sigma(1)}, \ldots, s_{\sigma(q)})$$ avec $q \in  \{1, \ldots, p\}$ et $s_1, \ldots, s_q \geq 3$ impairs.*

La somme (eqzetaas) est appelée *polyzêta antisymétrique* dans [@CFRsym]. Lorsque $q=1$, il s'agit simplement de $\zeta(s_1)$. Pour $q=2$, on obtient $\zeta(s_1, s_2) - \zeta(s_2, s_1)$. L'énoncé plus précis donné dans [@CFRsym] montre notamment que lorsque $p=1$, on obtient une forme linéaire en 1 et les $\zeta(s)$, pour $s$ impair compris entre 3 et $A$. Quand $p=2$, on obtient une forme linéaire en 1, les $\zeta(s)$ pour $s$ impair compris entre 3 et $2A$, et les $\zeta(s, s') - \zeta(s',s)$ pour $s, s'$ impairs tels que $3 \leq s < s' \leq A$. [^4]

Enfin, une dernière difficulté, et non la moindre, consiste à obtenir des résultats diophantiens en direction des conjectures 1 et 2 à l'aide de l'approche combinatoire développée ici. Nous nous contentons ici de démontrer un théorème technique concernant le dénominateur commun aux coefficients rationnels des combinaisons linéaires produites par certaines séries du type de (eq:serie mult generale) : voir le théorème 6 au paragraphe 5.

Nous avons pu faire fonctionner notre implémentation de l'algorithme présenté dans ce texte sur la grappe Médicis. Cela nous a permis de diminuer les temps de calcul nécessaires.

# Liens avec les intégrales hypergéométriques

Dans ce paragraphe, on s'intéresse au lien entre certaines intégrales multiples naturellement liées aux polyzêtas et les séries multiples que nous considérons dans le présent article. À nos yeux, la souplesse combinatoire des séries semble bien adaptée à la construction de formes linéaires en polyzêtas mais l'utilisation d'une intégrale ou d'une série dans ce but est essentiellement une affaire de goût, chacune ayant des avantages et des inconvénients. De plus, nous mentionnons certaines intégrales dont on sait qu'elles s'expriment à l'aide de polyzêtas mais auxquelles nos méthodes ne s'appliquent pas.

## Exemples

Il n'est pas possible de citer l'ensemble des intégrales multiples hypergéométriques qui sont apparues dans la littérature et nous ne mentionnons que les exemples les plus connus.

Posons, pour tous entiers $A\ge 2$ et $n\ge 0$, $$J_{A,n}=\int_{[0,1]^A}\frac{\prod_{j=1}^A x_j^n(1-x_j)^n}
{Q_A(x_1,x_2,\ldots, x_A)^{n+1}}
\,\textup{d}x_1\cdots \textup{d}x_A,$$ où $Q_A(\underline x)=
1-(\cdots (1-(1-x_A)x_{A-1})\cdots)x_1$. Lorsque $A=2$ et $A=3$, on retrouve les célèbres intégrales de Beukers [@be], qui a redémontré le théorème d'Apéry en utilisant le fait que $J_{2,n}
\in \mathbb{Q} +  \mathbb{Q} \zeta(2)$ et $J_{3,n}
\in
\mathbb{Q} +  \mathbb{Q} \zeta(3),$ sous une forme plus précise. En restant en dimension $A=2$ ou $A=3$, ces intégrales ont ensuite été généralisées dans le but d'améliorer les mesures d'irrationalité respectives de $\zeta(2)$ et $\zeta(3)$ : le point d'orgue est la méthode du groupe de Rhin-Viola [@rv1; @rv2], qui ont suivi des travaux de Hata [@hata2; @hata] en particulier. La principale difficulté de cette approche consiste à montrer directement que ces intégrales sont bien des formes linéaires en les valeurs de zêta.

En dimension supérieure, Vasilyev [@vasilyev] a formulé la conjecture suivante, qu'il a prouvée pour $A=4$ et $5$ : *Pour tous entiers $A\ge 2$ et $n\ge 0$, il existe des rationnels $(p_{j,A,n})_{j=0, 2, 3, \ldots, A}$ tels que $$\label{eq:vasint}
J_{A,n}=p_{0,A,n}+\sum_{j \equiv A \,(\textup{mod}\, 2)} p_{j,A,n} \zeta(j).$$* Cette conjecture, dont l'attaque directe est très difficile, a été démontrée par Zudilin [@zucaen paragraphe 8] au moyen d'une identité inattendue entre les intégrales de Vasilyev et certaines séries hypergéométriques très bien équilibrées. Comme on le montre au paragraphe 3.1, il est alors assez facile d'obtenir une forme linéaire en valeurs de zêta à partir d'une série hypergéométrique simple.

Il existe par ailleurs des intégrales d'une forme assez différente et qui ont été étudiées principalement par Sorokin [@sorokin2; @so1]. Dans [@so1], il a obtenu une preuve alternative du théorème d'Apéry en montrant que $$\label{eq:intesorokinzeta3}
S_{3,n}=\int_{[0,1]^3} \frac{x^n(1-x)^ny^n(1-y)^nz^n(1-z)^n}{(1-xy)^{n+1}(1-xyz)^{n+1}}
\, \textup{d}x\textup{d}y \textup{d}z\in
\mathbb{Q} +  \mathbb{Q} \zeta(3),$$ tandis que dans [@sorokin2], il a obtenu une nouvelle preuve de la transcendance de $\pi$ en utilisant l'intégrale $$\label{eq:padepisorokin}
T_{A,n}=\int_{[0,1]^{2A}} \prod_{j=1}^A \frac{(x_jy_j)^{n+(A-j)(n+1)}
(1-x_j)^n(1-y_j)^n}{(1-x_1y_1\cdots x_jy_j)^{n+1}} \, \textup{d}x_j \textup{d}y_j,$$ dont il a montré qu'elle était une forme linéaire rationnelle en 1 et les $\zeta(2,2,\ldots, 2)=\pi^{2j}/(2j+1)!$, pour $j=1, \ldots, A$, lorsque $z=1$. Dans les deux cas, Sorokin parvient à exprimer ses intégrales comme combinaison linéaire de valeurs de polyzêtas en résolvant de manière itérative des problèmes de Padé non triviaux. D'une manière générale, lorsqu'une intégrale provient d'un problème de Padé explicite, il arrive que l'énoncé même du problème permettent d'éliminer *a priori* certains polyzêtas des formes linéaires lorsque l'on spécialise les polylogarithmes multiples en $1$ ou autre valeur intéressante. Ceci confère un grand avantage à cette approche lorsqu'on peut la mettre en œuvre mais elle semble difficile à généraliser. De fait, les travaux ultérieurs cherchent tous à s'affranchir de l'étape Padé.

Le fait particulièrement remarquable que $J_{3,n}=S_{3,n}$ pour tout entier $n\ge 0$ a été généralisé par Fischler [@fi2] et Zlobin [@zlo] indépendamment, qui ont montré entre autres choses que l'on a les identités $$\label{eq:vasi=soro}
J_{A,n}= \int_{[0,1]^A}\prod_{j=1}^{A/2} \frac{x_j^n (1-x_j)^ny_j^n(1-y_j)^n}{(1-x_1y_1\cdots x_jy_j)^{n+1}}
\, \textup{d}x_j \textup{d}y_j$$ pour $A\ge 2$ pair et $$\label{eq:vasi=soro2}
J_{A,n}= \int_{[0,1]^A}\frac{z^n(1-z)^n}{(1-x_1y_1\cdots x_{a} y_{a} z)^{n+1}}
\bigg(\prod_{j=1}^{a} \frac{x_j^n (1-x_j)^ny_j^n(1-y_j)^n}{(1-x_1y_1\cdots x_jy_j)^{n+1}}
\, \textup{d}x_j \textup{d}y_j \bigg)\textup{d}z$$ pour $A\ge 3$ impair avec $a=(A-1)/2$. Il découle de ces travaux l'intuition assez nette que l'on ne perd rien à travailler avec des généralisations de l'une ou l'autre des intégrales $J_{A,n}$ et $S_{A,n}$. Il s'avère que les intégrales de Sorokin $S_{A,n}$ à droite de (eq:vasi=soro) et (eq:vasi=soro2) se développent un peu plus facilement en séries multiples que les intégrales $J_{A,n}$ et qu'elles donnent immédiatement des polyzêtas dans le cas $n=0$. Dans une perspective diophantienne, il est donc naturel de produire des formes linéaires en polyzêtas à partir d'intégrales du type de Sorokin les plus générales possibles ; une telle relation a été démontrée par Zlobin [@zlo]. La proposition 1 (démontrée au paragraphe 2.2 ci-dessous) couplée aux résultats de cet article nous permet de redémontrer une assertion similaire à celle de Zlobin mais nous insistons ici sur le fait que nos résultats (résumés informellement par le théorème 1) nous permettent de traiter des séries multiples plus générales que celles apparaissant dans la proposition 1 ou dans les travaux de Zlobin.

Terminons ce paragraphe en mentionnant un récent article de Zlobin [@zlobin2], où il obtient une nouvelle preuve de la conjecture de Vasilyev en partant de l'intégrale $S_{A,n}$ convenablement développée en série multiple : il s'agit d'un remarquable tour de force.

## Développement en série de certaines intégrales de Sorokin

Le but de ce paragraphe est d'exprimer une intégrale de type Sorokin relativement générale (elle contient du moins tous les cas mentionnés ci-dessus) comme une série multiple. Cette dernière est un cas particulier de celle que nous développons en polylogarithmes multiples et/ou polyzêtas dans la suite de l'article : pour ceux qui aiment travailler à partir d'intégrales, la proposition 1 (voir aussi le lemme 2 de [@ZlobinZametki2005]) est donc la première étape de notre algorithme de construction de formes linéaires en polyzêtas.

**Proposition 1**. *Soient des entiers $D, p\ge 1$ et des entiers positifs $r_1, \ldots, r_p$, $s_1, \ldots, s_p$, $t_1, \ldots, t_p$ et $0=d_0< d_1 < d_2<\cdots <d_p=D$. Pour tout complexe $z$ tel que $\vert z\vert >1$, on a l'identité $$\begin{gathered}
\label{eq:prop:intesoro=seriemult}
\int_{[0,1]^D} \prod_{j=1}^p \frac{
\prod_{\ell=d_{j-1}+1}^{d_j}x_\ell^{r_j}(1-x_\ell)^{s_j}}
{(z-x_1\cdots x_{d_j})^{t_j+1}}\, \textup{d}x_j
\\
= z^{-(t_1+\cdots+ t_p + p-1)} \cdot \prod_{j=1}^{p}\frac{s_j!^{A_j}}{t_j!} \cdot
\sum_{k_1 \ge \cdots \ge k_p\ge 1}  z^{-k_1} \prod_{j=1}^p\frac{(k_j-k_{j+1}+1)_{t_j}}
{(k_j+r_j)_{s_j+1}^{A_j}},
\end{gathered}$$ où $k_{p+1}=1$ et $A_j=d_j-d_{j-1}$ pour $j=1, \ldots, p.$ La série est de profondeur $p$ et de poids $D$.*

**Remarque 2**. *L'équation (eq:prop:intesoro=seriemult) s'étend à $\vert z\vert =1$ lorsque les deux membres ont un sens simultanément.*

*Dans les applications diophantiennes, il est pratique de sommer sur des indices $K_j$ définis par $K_j=k_j+r$, où $r= \min r_j$. En particulier, si tous les $r_j$ sont égaux à $r$, la série s'écrit $$\sum_{K_1 \ge \cdots \ge K_p\ge r+1} z^{-K_1-r} \prod_{j=1}^p\frac{(K_j-K_{j+1}+1)_{t_j}}
{(K_j)_{s_j+1}^{A_j}}$$ avec $K_{p+1}=r+1$. De plus, si $t_p=r$, la présence du symbole de Pochhammer $(K_p-r)_{r}$ implique que sommer sur l'ensemble d'indices $K_1 \ge \cdots \ge K_p\ge r+1$ revient au même que sommer sur $K_1 \ge \cdots \ge K_p\ge 1$.*

*Proof.* Supposer que $\vert z\vert >1$ assure que les diverses décompositions en séries et inversions séries-intégrales ci-dessous sont licites. Le cas d'un point du cercle $\vert z\vert =1$ s'obtient en invoquant des critères de continuité (théorèmes d'Abel, de Lebesgue, etc).

On développe le dénominateur de l'intégrale multiple, notée $I(z)$ dans la suite, au moyen de l'identité (avec $\vert z\vert >1, 0\le x\le 1$) : $$\frac{1}{(z-x)^{t+1}} = \frac{1}{z^t} \sum_{m=0}^{\infty} \binom{m+t}{m}
\bigg(\frac{x}{z}\bigg)^m$$ et on obtient alors $$\begin{gathered}
I(z)
= z^{-(t_1+\cdots+ t_p + p)}
\\\times
\sum_{m_1, \ldots, m_p \ge 0} \prod_{j=1}^p \binom{m_j+t_j}{m_j} z^{-m_j} \int \limits_{[0,1]^D}
\prod_{j=1}^p \bigg((x_1\cdots x_{d_j})^{m_j} \prod_{\ell=d_{j-1}+1}^{d_j}x_\ell^{r_j}(1-x_\ell)^{s_j} \,\textup{d}x_j\bigg).
\end{gathered}$$ Or on vérifie que $$\prod_{j=1}^p \bigg((x_1\cdots x_{d_j})^{m_j} \prod_{\ell=d_{j-1}+1}^{d_j}x_\ell^{r_j}(1-x_\ell)^{s_j}
\bigg) = \prod_{j=1}^p   \bigg(\prod_{\ell=d_{j-1}+1}^{d_j} x_\ell^{r_j+m_j+\cdots + m_p}
(1-x_\ell)^{s_j}\bigg).$$ On peut séparer les variables dans l'intégrale et on obtient alors $D$ intégrales facilement calculables (ce sont des fonctions Beta d'Euler), d'où $$I(z)= z^{-(t_1+\cdots +t_p + p)}
\sum_{m_1, \ldots, m_p \ge 0} \prod_{j=1}^p
\frac{z^{-m_j} \binom{m_j+t_j}{m_j}}{\binom{r_j+s_j+m_j+\cdots +m_p}{s_j}^{A_j}(r_j+s_j+m_j+\cdots +m_p+1)^{A_j}}.$$ On utilise maintenant les deux transformations triviales $\binom{m_j+t_j}{m_j}  = \frac{(m_j+1)_{t_j}}{t_j!}$ et $$\begin{gathered}
\qquad \binom{r_j+s_j+m_j+\cdots +m_p}{s_j}(r_j+s_j+m_j+\cdots +m_p+1)
\\
 = \frac{(r_j+m_j+\cdots +m_p+1)_{s_j+1}}{s_j!}\qquad
\end{gathered}$$ et on pose $k_j=m_j+\cdots +m_p+1$ pour $j=1, \ldots, p$, ainsi que $k_{p+1}=1$. On obtient alors $$I(z)= z^{-(t_1+\cdots+ t_p + p-1)} \cdot \prod_{j=1}^{p}\frac{s_j!^{A_j}}{t_j!}\cdot
\sum_{k_1 \ge  \cdots \ge k_p \ge 1}  z^{-k_1} \prod_{j=1}^p\frac{(k_j-k_{j+1}+1)_{t_j}}
{(k_j+r_j)_{s_j+1}^{A_j}},$$ ce qui termine la preuve. ◻

À titre d'exemples, remarquons que l'intégrale $S_{3,n}$ en (eq:intesorokinzeta3) vaut exactement la série (eq:sorokin1) donnée dans l'introduction tandis que l'intégrale (eq:padepisorokin) s'exprime de la manière suivante, en posant $k_{A+1} = n+1$ : $$T_{A,n}= n!^{A} \sum_{k_1 \ge \cdots \ge k_A\ge 1} \prod_{j=1}^A
\frac{(k_j -k_{j+1}+1)_n}{(k_j+(A-j)(n+1))_{n+1}^2}.$$ Notre algorithme permet ensuite d'exprimer effectivement ces intégrales comme des formes linéaires en polyzêtas. Jusqu'en poids 4, on ne voit apparaître que des valeurs de zêta car tous les polyzêtas de poids $\le 4$ sont des multiples rationnels de 1, $\zeta(2)$, $\zeta(3)$ ou $\zeta(4)$. En revanche, à partir du poids 5, on doit s'attendre à obtenir des polyzêtas linéairement indépendants (du moins, conjecturalement) des valeurs de zêta, comme le montre l'exemple de l'intégrale $$\int_{[0,1]^5} \frac{ \prod_{j=1}^5 x_j^n(1-x_j)^n dx_j}
{ (1-x_1x_2x_3)^{n+1}(1-x_1x_2x_3x_4x_5)^{n+1} }.$$ Pour $n=0$, elle vaut $\zeta(3,2) = -11 \zeta(5) /2 +3 \zeta(2)\zeta(3)$, qui n'est donc probablement pas un multiple rationnel d'une valeur de zêta en un entier. Pour $n=1$, $2$ et $3$, elle est une combinaison linéaire rationnelle en $\zeta(2), \zeta(3), \zeta(4), \zeta(5), \zeta(2,2)$ et $\zeta(3,2)$. Le coefficient de $\zeta(3,2)$ dans ces combinaisons linéaires est non nul ; on peut l'expliciter comme une somme double finie, ce qui pourrait peut-être permettre de démontrer qu'il est non nul pour tout $n \ge 4$, si nécessaire.

## D'autres exemples d'intégrales hypergéométriques

Il existe beaucoup d'autres types d'intégrales hypergéométriques que celles de Vasilyev et Sorokin et dont par des moyens plus ou moins détournés on sait qu'elles s'expriment comme formes linéaires en polyzêtas. Les deux exemples que nous allons aborder sont dus à Zudilin et Goncharov-Manin respectivement.

L'intégrale considérée par Zudilin est la suivante : $$Z_n= \int_{[0,1]^5}
\frac{\prod_{j=1}^5 x_j^n(1-x_j)^n \,\textup{d}x_j}{Q(x_1,x_2,x_3,x_4,x_5)^{n+1}}$$ où $Q(\underline x)=x_1(1-(1-(1-(1-x_2)x_3)x_4)x_5)+ (1-x_1x_2x_3x_4x_5).$ Par un procédé indirect (basé sur des transformations hypergéométriques), il montre que $Z_n$ est égale à une série de nature hypergéométrique très bien équilibrée (avec double une dérivation du sommande) et il en déduit que $Z_n\in\mathbb{Q}+\mathbb{Q}\zeta(4)$.

Les intégrales de Goncharov-Manin [@goncharov2] apparaissent quant à elles comme des périodes de certains motifs de Tate mixte, dont Brown [@brown] a donné la forme explicite suivante: $$\label{eq:gonchmanin}
\int_{[0,1]^A} \frac{\prod_{j=1}^A x_j^{r_j}(1-x_j)^{s_j}\,\textup{d}x_j}
{\prod_{1\le i<j\le A} (1-x_i\cdots x_j)
^{t_{i,j}}}$$ avec des entiers $r_j, s_j, t_{i,j}\ge 0$ tels que l'intégrale converge. Remarquons que (eq:gonchmanin) contient comme cas particulier les intégrales abordées par la proposition 1 (en $z=1$). Par des arguments de nature géométrique, Brown a prouvé une conjecture de Goncharov-Manin qui affirmait que ces intégrales sont toujours de formes linéaires rationnelles en polyzêtas. Sa méthode n'est malheureusement pas constructive, ce qui rend impossible une quelconque utilisation diophantienne de son théorème par les voies classiques.

Ces deux types d'intégrales ont donc le défaut de n'être évaluable que par des procédés très indirects. Pour remédier à cela, on pourrait tenter de les développer en séries multiples à la manière de la proposition 1, puis espérer appliquer une généralisation convenable de notre algorithme. Ceci n'aura rien d'évident ; par exemple, les cas les plus simples de l'intégrale (eq:gonchmanin) peuvent conduire à des séries telles que $$\sum_{m, n\ge 1} \frac{1}{m^{s_1}n^{s_2}(m+n)^{s_3}},$$ dont il n'est même pas clair qu'elles puissent s'exprimer à l'aide de polyzêtas (c'est cependant bien le cas : voir [@moll] pour plus de détails et des références). Étendre notre algorithme nécessitera donc des idées nouvelles.

# Étude de deux situations instructives {#sec:prof 1 et 2}

## Le cas de la profondeur 1

La stratégie [^5] pour démontrer les théorèmes diophantiens concernant les valeurs de la fonction zêta est la suivante. Soient des entiers $n\ge 0$, $A\ge 1$ et $P(X)\in\mathbb{Q}[X]$. Considérons la fraction rationnelle $\displaystyle R(X)= P(X)/(X)_{n+1}^A$ ainsi que la série $$S(z) = \sum_{k=1}^{\infty} R(k) \,z^{-k}.$$ On suppose cette dernière convergente pour $z= 1$, ce qui impose que deg$(P)$ $\le A(n+1)-2$. On commence par développer $R(X)$ en éléments simples : $$R(X) = \sum_{s=1} ^A\sum_{j=0}^n
\frac{C\bigg[\,\begin{matrix} s\\j\end{matrix}\,\bigg]}{(X+j) ^s} \quad
\textup{avec} \quad
C\bigg[\,\begin{matrix} s\\j\end{matrix}\,\bigg]=
\frac{1}{(A-s)!}\bigg(R(X)(X+j)^A\bigg) ^{(A-s)}\bigg\vert_{X=-j}$$ et, en reportant dans $S(z)$, on obtient $$\begin{aligned}
S(z)= \sum_{s=1} ^A\sum_{j=0}^n
C\bigg[\,\begin{matrix} s\\j\end{matrix}\,\bigg] \sum_{k=1}^{\infty}
\frac{z ^{-k}}{(k+j)^s}.
\end{aligned}$$

On remarque alors que, trivialement, $$\label{eq:brique prof 1}
\sum_{k=1}^{\infty} \frac{z ^{-k}}{(k+j)^s} = z^j \,\textup{Li}_s(1/z) -
\sum_{k=1}^{j} \frac{z ^{j-k}}{k^s}$$ et donc qu'il existe des polynômes $Q_{s}(z)$ $\in\mathbb{Q}[z]$, de degré au plus $n$, tels que $$S(z)=Q_{0}(z)+ \sum_{s=1}^A Q_{s}(z)\operatorname{Li}_{s}(1/z).$$ On a bien sûr $\textup{Li}_s(1)=\zeta(s)$ et $\textup{Li}_s(-1)= (2^{1-s}-1)\zeta(s)$ pour tout $s>1$. Pour $s\ge 1$, on a l'expression très simple $$Q_s(z) =\sum_{j=0}^n C\bigg[\,\begin{matrix} s\\j\end{matrix}\,\bigg] z^j.$$

Pour les applications envisagées, il est important de se ramener à des coefficients entiers et on montre que $Q_{1}(1)=0$ et $\textup{d}_n^{A-j} \,Q_{j}(z)\in\mathbb{Z}[z]$ pour tout $j\in\{0, \ldots, A\}$, où $\textup{d}_n=\textup{p.p.c.m.}\{1, 2, \ldots, n\}$. Il existe donc des entiers $q_{j}$ tels que $$\textup{d}_n^{A}S(1) = q_{0} + \sum_{s=2}^{A} q_{s} \,\zeta(s),$$ et une expression similaire pour $S(-1)$.

Tout le problème réside maintenant dans des choix de $A$ et de $P$ tels que l'on puisse appliquer efficacement un critère d'irrationalité ou d'indépendance linéaire : il apparaı̂t rapidement que l'on doit éliminer les nombres $\zeta(s)$ pour $s$ pair, sous peine de n'obtenir que des résultats triviaux. Une manière d'y parvenir est d'imposer que le polynôme $P(X)$ satisfasse à $$\label{eq:symetrie prof 1}
P(-X-n)=-P(X).$$ En effet, par unicité de la décomposition de $R(X)$ en éléments simples, l'équation (eq:symetrie prof 1) se traduit par $C\bigg[\,\begin{matrix} s\\n-j\end{matrix}\,\bigg]
=(-1)^{A(n+1)+s+1}
C\bigg[\,\begin{matrix} s\\j\end{matrix}\,\bigg]$ et donc les coefficients $q_{s}$ sont nuls pour $s$ pair lorsque $A$ est lui-même pair. Par exemple, lorsque $A$ est pair, on peut utiliser les séries $$n!^{A-2r}
\sum_{k=1}^{\infty}
\left(k+\frac{n}{2}\right)\frac{(k-rn)_{rn}(k+n+1)_{rn}}{(k)_{n+1}^A}
=q_{0}+\sum_{{s=3 \atop s \,\textup{impair}}}^A q_{s} \,\zeta(s),$$ qui sont des séries hypergéométriques spéciales, dites *very-well-poised* (voir [@ba; @sl] pour la définition exacte). On se réfèrera à [@br; @fi; @kratriv; @ri; @zud] pour plus de détails sur l'utilisation diophantienne de ce type de série.

## Le cas de la profondeur 2 {#ssec: algo prof 2}

Une fois formalisé le cas de la profondeur 1, il est naturel d'essayer de suivre la même démarche en profondeur supérieure. Le cas de la profondeur $p=2$ est déjà instructif et nous allons le traiter en détails.

Nous expliquons notre approche sur la série suivante $$\label{eq:sorokin2}
S(z_1,z_2)=\sum_{k_1\ge k_2\ge 1}
\frac{P(k_1,k_2)}{(k_1)_{n+1}^2(k_2)_{n+1}^2}
\,z_1^{-k_1}z_2^{-k_2},$$ avec $\textup{deg}_{k_1}(P)\le A(n+1)-2$ et $\textup{deg}_{k_2}(P)\le A(n+1)-2$, ce qui assure que la série converge absolument pour $\vert z_1\vert \ge 1$ et $\vert z_2\vert \ge 1$. On notera que la série introduite en (eq:sorokin1) ne vérifie pas cette condition de degré : les conséquences de cela sont évoquées à la fin de ce paragraphe.

La première étape consiste, comme précédemment, à décomposer en éléments simples la fraction rationnelle qui constitue le sommande de $S(z_1,z_2)$ : $$\frac{P(k_1,k_2)}{(k_1)_{n+1}^2(k_2)_{n+1}^2}
= \sum_{j_1, j_2=0}^n
  \sum_{s_1, s_2=1}^2
\frac{C\bigg[\,\begin{matrix} s_1, s_2\\j_1, j_2\end{matrix}\,\bigg]}{(k_1+j_1)^{s_1}(k_2+j_2)^{s_2}},$$ où les $C\bigg[\,\begin{matrix} s_1, s_2\\j_1, j_2\end{matrix}\,\bigg]$ sont des rationnels explicitables. Il est important de noter que la condition portant sur les degrés de $P$ implique que cette décomposition n'a pas de partie entière. En reportant dans $S(z_1,z_2)$, on obtient ainsi $$S(z_1,z_2)=
\sum_{j_1, j_2=0}^n \, \sum_{s_1, s_2=1}^2
C\bigg[\,\begin{matrix} s_1, s_2\\j_1, j_2\end{matrix}\,\bigg]
\sum_{k_1\ge k_2\ge 1} \frac{z_1^{-k_1}z_2^{-k_2}}
{(k_1+j_1)^{s_1}(k_2+j_2)^{s_2}}.$$

La deuxième étape consiste à exprimer explicitement la série $$\label{eq:brique double elementaire}
\sum_{k_1 =1}^{\infty}
\frac{z_1^{-k_1}}{(k_1+j_1)^{s_1}}\,\sum_{k_2=1}^{k_1} \frac{z_2^{-k_2}}{(k_2+j_2)^{s_2}}$$ comme une combinaison linéaire à coefficients dans $\mathbb{Q}[z_1^{\pm 1}, z_2^{\pm 1}]$ en les polylogarithmes multiples (larges ou stricts). Comme on l'a vu en (eq:brique prof 1), dans le cas d'une seule variable ($p=1$), c'est une étape triviale mais, malheureusement, en deux variables, ce n'est plus le cas. On écrit tout d'abord la somme intérieure sur $k_2$ comme $$\sum_{k_2=1}^{k_1}\frac{z_2^{-k_2}}{(k_2+j_2)^{s_2}}
=\sum_{k_2=j_2+1}^{k_1+j_2}\frac{z_2^{j_2-k_2}}{k_2^{s_2}}
=
\bigg(\sum_{k_2=1}^{k_1+j_1}-\sum_{k_2=1}^{j_2}+\;\varepsilon_{j_1,j_2}
\sum_{k_2=k_1+j_1 \wedge j_2+1}^{k_1+j_1 \vee j_2}\bigg)\frac{z_2^{j_2-k_2}}{k_2^{s_2}}$$ où $j_1 \wedge j_2 = \min(j_1,j_2)$, $j_1\vee j_2 =\max(j_1, j_2)$ et $\varepsilon_{j_1,j_2}=1$ si $j_1<j_2$, $-1$ si $j_1>j_2$, $0$ si $j_1=j_2$. Puis on reporte ces trois sommes dans la somme sur $k_1$. Les deux premières séries se traitent facilement : $$\begin{aligned}
\sum_{k_1=1}^{\infty}\frac{z_1^{-k_1}}{(k_1+j_1)^{s_1}}
\sum_{k_2=1}^{k_1+j_1}\frac{z_2^{j_2-k_2}}{k_2^{s_2}}
 & = & \sum_{k_1=j_1+1}^{\infty}\frac{z_1^{j_1-k_1}}{k_1^{s_1}}
 \sum_{k_2=1}^{k_1}\frac{z_2^{j_2-k_2}}{k_2^{s_2}}\\
 & = & z_1^{j_1}z_2^{j_2}\;\textup{La}_{{s_1},{s_2}}(1/z_1,1/z_2)-
\sum_{k_1=1}^{j_1}\frac{z_1^{j_1-k_1}}{k_1^{s_1}}
\sum_{k_2=1}^{k_1}\frac{z_2^{j_2-k_2}}{k_2^{s_2}}
\end{aligned}$$ et $$\begin{gathered}
\sum_{k_1=1}^{\infty}\frac{z_1^{-k_1}}{(k_1+j_1)^{s_1}}
\sum_{k_2=1}^{j_2}\frac{z_2^{j_2-k_2}}{k_2^{s_2}}
\\
=z_1^{j_1}\bigg(\sum_{k_2=1}^{j_2}
\frac{z_2^{j_2-k_2}}{k_2^{s_2}}\bigg)\textup{La}_{{s_1}}(1/z_1)-
\bigg(\sum_{k_1=1}^{j_1}\frac{z_1^{j_1-k_1}}{k_1^{s_1}}\bigg)
\bigg(\sum_{k_2=1}^{j_2}\frac{z_2^{j_2-k_2}}{k_2^{s_2}}\bigg).\qquad
\end{gathered}$$ La troisième série est un peu plus compliquée : on note que $$\begin{aligned}
\sum_{k_1=1}^{\infty}\frac{z_1^{-k_1}}{(k_1+j_1)^{s_1}}
\sum_{k_2=k_1+j_1 \wedge j_2+1}^{k_1+j_1 \vee j_2}\frac{z_2^{j_2-k_2}}{k_2^{s_2}}
 & = &
\sum_{k_2=j_1 \wedge j_2+1}^{j_1 \vee j_2} z_2^{j_2-k_2}
\sum_{k_1=1}^{\infty}
\frac{(z_1z_2)^{-k_1}}{(k_1+j_1)^{s_1}(k_1+k_2)^{s_2}}
\end{aligned}$$ puis l'on développe en éléments simples la fraction rationnelle $$\frac{1}{(k_1+j_1)^{s_1}(k_1+k_2)^{s_2}}$$ pour conclure que cette série s'écrit comme une combinaison linéaire de $\textup{La}_s(1/z_1z_2)$ avec $1\le s\le s_1 \vee s_2$ et aussi de $\textup{La}_{{s_1}+{s_2}}(1/z_1z_2)$ si $k_2=j_1 \vee j_2=j_1$, avec des coefficients polynomiaux en $z_1^{\pm 1}$ et $z_2^{\pm 1}$. En résumé, lorsque $z_1=z_2=1$, la décomposition de la série (eq:brique double elementaire) fait apparaı̂tre au plus les polyzêtas suivants : $\zeta(s_1, s_2)$, $\zeta(s_1 + s_2)$ et les $\zeta(s)$ pour $1 \le s \le s_1 \vee s_2$. En particulier, il n'y a aucune raison apparente pour que les valeurs de zêta aux entiers pairs n'apparaissent pas.

Enfin, troisième étape, en reportant la décomposition ainsi obtenue dans (eq:sorokin2), on doit identifier les polyzêtas qui apparaissent réellement dans $S(1,1)$, c'est-à-dire ceux affectés d'un coefficient non-nul. Or cette identification n'est pas évidente : la série $S(1,1)$ fait apparaı̂tre *a priori* les polyzêtas $$\zeta(1), \,\zeta(1,1), \,\zeta(2), \,\zeta(2,1), \,\zeta(1,2),
\,\zeta(3), \,\zeta(2,2), \,\zeta(4)$$ (certains sont divergents). Lorsque, par exemple, $P(X_1, X_2)=(X_2-n)_n(X_1-X_2+1)_n$, il est assez difficile de prouver que seuls $\zeta(2)$, $\zeta(2,2)$ et $\zeta(4)$ n'ont pas un coefficient nul.

On doit aussi parfois tenir compte d'un autre phénomène : contrairement à $S(z_1,z_2)$, la décomposition en éléments simples du sommande de la série en (eq:sorokin1) produit une partie entière (puisque le degré en $X_2$ de la fraction $(X_2-n)_n(X_1-X_2+1)_n/(X_1)_{n+1}^2(X_2)_{n+1}$ est positif) qui complique encore cette étape en faisant apparaı̂tre des polylogarithmes multiples exotiques tels que $\textup{La}_{2,-1}(z_1,z_2)$ qu'il faut traiter de façon *ad hoc*. Ce procédé devient quasiment inextricable en trois variables, ce qui explique le formalisme que nous développons au paragraphe 4.

# Démonstration du théorème 1

Nous venons de démontrer le théorème 1 pour $p=1$ (paragraphe 3.1) et $p=2$ (paragraphe [\[ssec:
algo prof 2\]](#ssec:
algo prof 2)). Dans ce paragraphe, on le démontre en toute généralité : la stratégie consiste à se ramener dans un premier temps à un cas plus simple (paragraphe 4.1) que l'on démontre ensuite (théorème 5 au paragraphe 4.3). Nous en obtiendrons des raffinements au paragraphe 5.

## Décomposition des séries multiples en briques {#ssec:serie hyp mult en brique}

[]{#sec:decompositionenbrique label="sec:decompositionenbrique"}

En imitant le cas de la profondeur 1, nous allons transformer la série $$\label{eq:S_p mult generale}
S_P\bigg[\,\begin{matrix}
A_1, \ldots, A_p\\
n_1, \ldots, n_p
\end{matrix}
\,\bigg\vert \,z_1, \ldots, z_p\, \bigg] = \sum_{k_1\ge \cdots \ge
k_p\ge 1} \frac{P(k_1,  \ldots, k_p)}{(k_1)_{n_1+1}^{A_1}
 \cdots (k_p)_{n_p+1}^{A_p}}\,z_1^{-k_1}\cdots z_p^{-k_p}$$ en développant en éléments simples la fraction rationnelle $$R(X_1, \ldots, X_p)= \frac{P(X_1,  \ldots,
X_p)}{(X_1)_{n_1+1}^{A_1}
 \cdots (X_p)_{n_p+1}^{A_p}}.$$ Posons $\hat A_i=\deg_{X_i}(P)- A_i(n_i+1)$ : c'est le degré en $X_i$ de la fraction rationnelle $R$. Notons $J$ l'ensemble des indices $i \in \{1, \ldots, p\}$ tels que $\hat A_i\geq 0$ (c'est-à-dire $\deg_{X_i}(P) \geq A_i(n_i+1)$) : c'est l'ensemble des $i$ pour lesquels $R$ est de degré positif ou nul en $X_i$, c'est-à-dire relativement auxquels une partie entière va apparaı̂tre. Pour $I \subset \{1, \ldots, p\}$, on note $I^{{\rm c}}= \{1, \ldots, p\}\setminus
I$. Alors on a $$\label{eq: decomposition de R}
R(X_1, \ldots, X_p)= \sum_{I \subset J} \sum_{\tiny {\begin{array}{c} (s_i)_{i \in
I^{{\rm c}}} \mbox{ tel que } \\ 1 \leq s_i \leq A_i  \\ \mbox{pour tout } i
\in I^{{\rm c}} \end{array}}} \sum_{\tiny {\begin{array}{c} (j_i)_{i \in I^{{\rm c}}} \mbox{ tel que } \\ 0 \leq
j_i \leq n_i  \\ \mbox{pour tout } i \in I^{{\rm c}} \end{array}}} \sum_{\tiny {\begin{array}{c} (\hat s_i)_{i
\in I} \mbox{ tel que } \\ 0 \leq \hat s_i\leq \hat A_i \\ \mbox{pour tout
} i \in I \end{array}}} C\left[\,{\tiny \begin{matrix} I \\ (s_i) \\ (j_i) \\ (\hat s_i) \end{matrix}} \,\right]\frac{\prod_{i \in I} X_i^{\hat s_i}}{\prod_{i
\in I^{{\rm c}}}(X_i+j_i)^{s_i}}$$ avec $$C\left[\,{\tiny \begin{matrix} I \\ (s_i) \\ (j_i) \\ (\hat s_i) \end{matrix}} \,\right]= \partial\left[\,{\tiny \begin{matrix} I \\ (s_i) \\  (\hat s_i) \end{matrix}} \,\right]\Big(R_I(Y_1, \ldots, Y_p)  \prod_{i \in I^{{\rm c}}} (Y_i+j_i)^{A_i}
\prod_{i \in I} Y_i^{\hat A_i} \Big)_{\left| {\tiny \begin{array}{l} {Y_i = 0
\mbox{ pour } i \in I} \\ {Y_i = -j_i \mbox{ pour } i  \in I^{{\rm c}}} \end{array}}\right.}$$ en notant $\partial\left[\,{\tiny \begin{matrix} I \\ (s_i) \\  (\hat s_i) \end{matrix}} \,\right]$ l'opérateur différentiel suivant $$\partial\left[\,{\tiny \begin{matrix} I \\ (s_i) \\  (\hat s_i) \end{matrix}} \,\right]= \prod_{i \in I^{{\rm c}}} \Big( \frac{1}{(A_i - s_i)!} \Big(
\frac{\partial}{\partial Y_i} \Big)^{A_i-s_i} \Big)
 \prod_{i \in I}
\Big( \frac{1}{(\hat A_i- \hat s_i)!} \Big( \frac{\partial}{\partial
Y_i} \Big)^{\hat A_i- \hat s_i} \Big),$$ et $R_I(Y_1, \ldots, Y_p)$ la fraction rationnelle obtenue à partir de $R(X_1, \ldots, X_p)$ en posant : $$\left\{
\begin{array}{l}
X_i = \frac{\displaystyle 1}{\displaystyle Y_i} \mbox{ pour } i \in I \\
X_i = Y_i \mbox{ pour } i \in I^{{\rm c}}.
\end{array}
\right.$$

Le cas particulier où il n'y a pas de partie entière correspond à $\hat A_i\leq -1$ pour tout $i \in \{1, \ldots, p\}$, c'est-à-dire $J = \emptyset$. La somme sur $I$ se réduit alors à $I  = \emptyset$, la famille $(\hat s_i)$ est vide et on obtient la décomposition en éléments simples habituelle : $$R(X_1, \ldots, X_p) = \sum_{s_1=1}^{A_1}\cdots \sum_{s_p=1}^{A_p}
\sum_{j_1=0}^{n_1}\cdots \sum_{j_p=0}^{n_p}
C\bigg[\,\begin{matrix} s_1,  \ldots, s_p\\
                        j_1,  \ldots, j_p
\end{matrix} \,\bigg] \frac{1}{(X_1+j_1)^{s_1}\cdots (X_p+j_p)^{s_p} }.$$

Revenons au cas général. En reportant [\[eq: decomposition
de R\]](#eq: decomposition
de R) dans (eq:S_p mult generale), on obtient $$\begin{gathered}
S_P\bigg[\,\begin{matrix}
A_1, \ldots, A_p\\
n_1, \ldots, n_p
\end{matrix}
\,\bigg\vert \,z_1, \ldots, z_p\, \bigg] = \sum_{I \subset J}
\sum_{\tiny {\begin{array}{c} (s_i)_{i \in I^{{\rm c}}} \mbox{ tel que } \\ 1 \leq s_i \leq
A_i  \\ \mbox{pour tout } i \in I^{{\rm c}} \end{array}}} \sum_{\tiny {\begin{array}{c} (j_i)_{i \in I^{{\rm c}}}
\mbox{ tel que } \\ 0 \leq j_i \leq n_i  \\ \mbox{pour tout } i \in
I^{{\rm c}} \end{array}}}
\sum_{\tiny {\begin{array}{c} (\hat s_i)_{i \in I}
\mbox{ tel que } \\ 0 \leq \hat s_i\leq \hat A_i \\ \mbox{pour tout } i \in I \end{array}}}
\\
\cdot C\left[\,{\tiny \begin{matrix} I \\ (s_i) \\ (j_i) \\ (\hat s_i) \end{matrix}} \,\right]\sum_{k_1\ge \cdots \ge k_p\ge 1} \frac{\prod_{i \in I}
k_i^{\hat s_i}}{\prod_{i \in I^{{\rm c}}}(k_i+j_i)^{s_i}} \,z_1^{-k_1}\cdots
z_p^{-k_p}.
\end{gathered}$$ On a donc ramené le problème initial (i.e., l'évaluation de (eq:S_p mult generale)) à celui de la décomposition en polylogarithmes multiples de séries élémentaires de la forme $$\sum_{k_1\ge \cdots \ge k_p\ge 1} \frac{z_1^{-k_1}\cdots
z_p^{-k_p}} {(k_1+j_1)^{s_1}\cdots (k_p+j_p)^{s_p}},$$ où $s_i\in\mathbb{Z}$ et $j_i\in\mathbb{N}$. C'est ce problème que nous allons maintenant résoudre ; cela terminera la preuve du théorème 1.

## Notations

Dans tout ce paragraphe, $N$ désignera un entier $\ge 1$ qui jouera essentiellement le rôle de profondeur, rôle dévolu jusqu'à présent à l'entier $p$. On notera :

-   $\underline{j}_N=(j_i)_{i=1,\ldots N}$ et $\underline{m}_N=(m_i)_{i=1,\ldots N}$ (avec $m_1=0$) des suites d'entiers de $\mathbb{N}$ ;

-   $\underline{s}_N=(s_i)_{i=1,\ldots N}$ une suite d'entiers de $\mathbb{Z}$ ;

-   $\underline{z}_N=(z_i)_{i=1,\ldots N}$ une suite de complexes de modules $\ge 1$ ;

-   $a\wedge b=\min{(a,b)}$ et $a\vee b=\max{(a,b)}$ ;

-   $\varepsilon_{a,b}=1$ si $a<b$, $-1$ si $a>b$, $0$ si $a=b$ et $\varepsilon_{p}=\varepsilon_{j_{p-1},j_p+m_p}$ (pour $p\ge 2$) ;

-   $t_p=j_{p-1}\wedge (j_p+m_p)$ et $T_p=j_{p-1}\vee (j_p+m_p)$ (pour $p\ge 2$).

À toute suite finie $\underline{u}_N=(u_1,\ldots,u_N)$, on associe les trois suites :

-   $\underline{u}_{N}^p=(u_p,\ldots,u_N)$ de longueur $N-p+1$ (pour $1\le p\le N$) ;

-   $_p\underline{u}_{N}=(u_1,\ldots,u_{p-2},u_{p-1}u_p,u_{p+1},\ldots,u_N)$ de longueur $N-1$ (pour $2\le p\le N$) ;

-   $1/\underline{u}_{N}=(1/u_1,\ldots,1/u_N)$ lorsque les $u_i$ sont non-nuls.

On définit les *briques decalées-modulées* par $$\textup{B}_N\Bigg[\,
\begin{matrix}
\underline{s}_N\\
\underline{m}_N\\
\underline{j}_N
\end{matrix}\,
\Bigg\vert \,\underline{z}_N
\,\Bigg]=
\sum_{k_{N-1}+m_N \ge k_N \ge 1\atop
{k_{N-2}+m_{N-1} \ge k_{N-1} \ge 1\atop
{\vdots\atop
{k_1+m_2 \ge k_2\ge 1\atop
k_1\ge 1}}}
}\frac{z_1^{-k_1}\cdots z_N^{-k_N}}
{(k_1+j_1)^{s_1}\cdots(k_N+j_N)^{s_N}}.
\label{eq:3}$$ Les $j_i$ sont les décalages, les $m_i$ les modulations, les $s_i$ les exposants, $N$ la profondeur et on définit son poids comme étant $\sum_{p=1}^N \max(s_p,0)$. Par définition, $m_1=0$ : toutes les briques $\textup{B}^{\prime}$ que nous construirons à l'aide de briques $\textup{B}$ avec $m_1=0$ auront aussi $m^{\prime}_1=0$. Ces séries convergent absolument lorsque $\vert z_1\vert>1$ et $\vert z_j\vert \ge 1$ pour $j=2, \ldots, N$, ce que l'on suppose dorénavant et qui légitime les diverses manipulations que nous effectuerons dessus ; nous montrerons au paragraphe 7 comment obtenir des résultats similaires lorsque tous les $z_i$ valent 1. Un cas particulier important est celui où tous les $m_i$ sont nuls : on parlera de *brique décalée*, ou simplement de *brique*, [^6] et on la notera $$\textup{B}_N\bigg[\,
\begin{matrix}
\underline{s}_N\\
\underline{j}_N
\end{matrix}\,
\bigg\vert \,\underline{z}_N\,
\bigg]=\sum_{k_1 \ge \cdots \ge k_{N}\ge 1}
\frac{z_1^{-k_1}\cdots z_N^{-k_N}}
{(k_1+j_1)^{s_1}\cdots(k_N+j_N)^{s_N}}.
\label{eq:4}$$ Nous avons déjà rencontré ce type de briques dans les cas $N=1$ et $N=2$ au paragraphe 3 et en toute généralité au paragraphe 4.1. Pour obtenir des relations compactes, on définit la brique de profondeur 0 (et vide de paramètres) comme la fonction identiquement égale à 1. La modulation semble *a priori* une notion artificielle et inutile puisqu'on ne s'intéresse réellement qu'aux briques décalées : à l'usage, il n'en est rien car, de façon surprenante, on ne peut apparemment pas produire le théorème 5 ci-dessous sans modulation.

Nous appellerons *terme de profondeur $\le N-1$* toute combinaison linéaire à coefficients dans $\mathbb{Q}[z^{\pm 1}_1,\ldots, z_N^{\pm 1}]$ de briques décalées-modulées de profondeur $\le N-1$ et évaluées en des produits quelconques des variables $z_1, \ldots, z_N$. Le poids d'un terme de profondeur $N-1$ est le plus grand des poids des briques qui le composent.

Pour tout entier $p$ tel que $1\le p\le N+1$, on définit le polynôme de Laurent $$Q_{\underline{s}_{N}^{p},p}(K;\underline{z}_{N}^{p})
=\sum_{K\ge
k_{p}\ge \cdots\ge  k_{N}\ge 1}
\frac{z_{p}^{-k_{p}}\cdots z_{N}^{-k_{N}}}
{\prod_{i=p}^N k_i^{s_i}},
\label{eq:5}$$ (qui vaut $0$ si $K=0$) pour $p\le N$ et $Q_{\underline{s}_{N}^{N+1},N+1}(K;\underline{z}_{N}^{N+1})=1$ pour $p=N+1$. On notera $Q_{\underline{s}_{N}^p,p}(K;\underline{z}_{N}^{p})=Q_{N,p}(K;\underline{z}_{N}^{p})$ lorsqu'il n'y aura pas de risque de confusion sur les exposants en jeu. On a $$Q_{N,p}(K;\underline{z}_{N}^{p})=
\sum_{k_{p}=1}^{K}\frac{z_p^{-k_p}}{k_p^{s_p}}\,
Q_{N,p+1}(k_{p};\underline{z}_{N}^{p+1}).
\label{eq:6}$$

Enfin, pour tout entier $p$ tel que $2\le p\le N$, on définit $$\begin{gathered}
 R_{\underline{s}_{N},p}(K; {}_p\underline{z}_{N})
\\
=
\sum_{k_{p-2}+m_{p-1}\ge k_{p-1}\ge 1\atop{
\vdots\atop
{k_1+m_2\ge k_2\ge 1 \atop
k_1\ge 1}}}
\frac{z_1^{-k_1}\cdots z_{p-2}^{-k_{p-2}}(z_{p-1}z_p)^{-k_{p-1}}}
{\left(\prod_{i=1}^{p-1}(k_i+j_i)^{s_i}\right)
(k_{p-1}+K)^{s_p}} \,Q_{N,p+1}(k_{p-1}+K;\underline{z}_{N}^{p+1}).
\label{eq:7}
\end{gathered}$$ Si $p=2$, on attribue la valeur 1 au produit vide $z_1^{-k_1}\cdots z_{p-2}^{-k_{p-2}}$. On notera $R_{\underline{s}_{N},p}(K;{}_p\underline{z}_{N})=R_{N,p}(K;{}_p\underline{z}_{N})$ lorsqu'il n'y aura pas de risque de confusion et nous montrerons qu'il s'agit d'un terme de profondeur $\le
N-1$.

## L'algorithme de décomposition des briques

Le but de ce paragraphe est de démontrer que *la brique décalée-modulée (eq:3) est la somme de $\left(z_1^{j_1}\cdots z_N^{j_N}\right)\textup{La}_{\underline{s}_N}(1/\underline{z}_N)$ et de termes de profondeur au plus $N-1$*. Cette proposition informelle (qui suffit à démontrer le théorème 1, compte tenu des résultats du paragraphe (sec:decompositionenbrique)) découle du théorème suivant qui est beaucoup plus précis.

**Théorème 5**. *$(i)$ Pour tout entier $N\ge 1$, on a $$\begin{gathered}
\textup{B}_N\Bigg[\,
\begin{matrix}
\underline{s}_N\\
\underline{m}_N\\
\underline{j}_N
\end{matrix}
\,\Bigg\vert\, \underline{z}_N
\,\Bigg]=
\left(z_1^{j_1}\cdots
z_N^{j_N}\right)\textup{La}_{\underline{s}_N}(1/\underline{z}_N)
\\
-\sum_{p=1}^N \left(z_p^{j_p}\cdots
z_N^{j_N}\right)\,Q_{N,p}(j_p; \underline{z}_{N}^{p})\,
\textup{B}_{p-1}\Bigg[\,
\begin{matrix}
\underline{s}_{p-1}\\
\underline{m}_{p-1} \\
\underline{j}_{p-1}
\end{matrix}\,
\Bigg\vert\,\underline{z}_p\,
\Bigg]\\ \qquad+\sum_{p=2}^N \varepsilon_p\,
\left(z_p^{j_p}\cdots z_N^{j_N}\right)
\sum_{k_p=t_p +1}^{T_p}z_p^{-k_p}R_{N,p}(k_p; {}_p\underline{z}_{N}).
\label{eq:8}
\end{gathered}$$*

*$(ii)$ Pour tout entier $p$ tel que $2\le p\le N$ et tout entier $K\ge 0$, la série $R_{N,p}(K;{}_p\underline{z}_{N})$ est un terme de profondeur $\le N-1$, dont le poids est $\le \sum_{p=1}^N\max(s_p,0)$.*

**Remarque 3**. *$(1)$ Si $N=1$, l'expression débutant par $\sum_{p=2}^N\,\varepsilon_p (\cdots)$ n'apparaı̂t pas.*

*$(2)$ Ce théorème fournit un algorithme permettant d'expliciter totalement le résultat informel évoqué au début de ce paragraphe. Nous avons implémenté cet algorithme sous GP-Pari.*

*Démonstration.* La partie (i) repose sur le lemme suivant, que nous démontrons à la toute fin de ce paragraphe.

**Lemme 1**. *$(i)$ Pour tout $N\ge 2$ et tout $p=2,\ldots, N$, on a $$\begin{gathered}
\textup{B}_N\Bigg[\,
\begin{array}{ccccc}
\underline{s}_{N}& & & &\\
\underline{m}_{p}& j_{p}& 0& \cdots&  0 \\
\underline{j}_{p}& 0      & 0& \cdots&  0
\end{array}\,
\Bigg\vert \,\underline{z}_N \,
\Bigg]
= z_p^{j_p}\,\textup{B}_N\Bigg[\,
\begin{array}{ccccc}
\underline{s}_{N}& & & &\\
\underline{m}_{p-1}& j_{p-1}& 0& \cdots &  0 \\
\underline{j}_{p-1}& 0      & 0& \cdots &  0
\end{array}\,
\Bigg\vert \,\underline{z}_N\,
\Bigg]\\
-z_{p}^{j_p}\,Q_{N,p}(j_p; \underline{z}_{N}^{p})\,
\textup{B}_{p-1}\Bigg[\,
\begin{array}{c}
\underline{s}_{p-1}\\
\underline{m}_{p-1} \\
\underline{j}_{p-1}
\end{array}\,
\Bigg\vert \,\underline{z}_p\,
\Bigg]
+\varepsilon_p
\sum_{k_p=t_p +1}^{T_p} z_p^{j_p-k_p}R_{N,p}(k_p;{}_p\underline{z}_{N}).
\end{gathered}$$*

*$(ii)$ Pour tout $N\ge 1$, on a $$\textup{B}_N\Bigg[\,
\begin{array}{ccccc}
\underline{s}_{N}& & & &\\
 0 & j_{1}& 0& \cdots&  0 \\
\underline{j}_{1}& 0      & 0& \cdots&  0
\end{array}\,
\Bigg\vert\,\underline{z}_N\,
\Bigg]=
z_1^{j_1}\,\textup{La}_{\underline{s}_N}(1/\underline{z}_N)-z_1^{j_1}\,Q_{N,1}(j_1;\underline{z}_{N}).$$*

On applique le point (i) de ce lemme avec $p=N$, ce qui donne $$\begin{gathered}
\textup{B}_N\Bigg[\,
\begin{matrix}
\underline{s}_N\\
\underline{m}_N\\
\underline{j}_N
\end{matrix}\,
\Bigg\vert \,\underline{z}_N\,
\Bigg]=-z_N^{j_N} \,Q_{N,N}(j_N;z_N)\,
\textup{B}_{N-1}\Bigg[\,
\begin{matrix}
\underline{s}_{N-1}\\
\underline{m}_{N-1}\\
\underline{j}_{N-1}
\end{matrix}\,
\Bigg\vert \,\underline{z}_{N-1}\,
\Bigg]\\
+z_N^{j_N}
\textup{B}_N\Bigg[\,
\begin{array}{cc}
\underline{s}_{N}& \\
\underline{m}_{N-1}& j_{N-1}\\
\underline{j}_{N-1}& 0
\end{array}\,
\Bigg\vert \,\underline{z}_N\,
\Bigg ]
+\varepsilon_N
\sum_{k_N=t_N +1}^{T_N}z_N^{j_N-k_N}R_{N,N}(k_N; {}_N\underline{z}_{N}).
\end{gathered}$$ On repète ce procédé $N-1$ fois en appliquant le lemme 1, (i), à l'unique brique de profondeur $N$ qui apparaı̂t à chaque itération, jusqu'à obtenir (en plus d'autres termes) la brique $$\textup{B}_N\Bigg[\,
\begin{array}{ccccc}
\underline{s}_{N}&&&&\\
\underline{m}_{1}& j_{1}& 0& \cdots & 0 \\
\underline{j}_{1}& 0& 0&\cdots& 0
\end{array}\,
\Bigg\vert \,\underline{z}_N
\,\Bigg],$$ à laquelle on applique alors le point (ii) du même lemme 1 (puisque $\underline{m}_{1}=m_1=0$). En regroupant les termes, on constate que l'on a démontré le point (i) du théorème 5.

Pour prouver la partie (ii), on a également besoin d'un lemme technique, dont on donnera la démonstration à la fin du paragraphe.

**Lemme 2**. *Soient $e, f \in\mathbb{Z}$ et $i, j\in\mathbb{C}$.*

*$(i)$ Lorsque $i=j$, $$\frac{1}{(X+i)^e(X+j)^f}=\frac{1}{(X+i)^{e+f}}\;.$$*

*$(ii)$ Lorsque $e\le 0$ et $f\ge 1$, $$\frac{1}{(X+i)^e(X+j)^f}=
\sum_{u=0}^{-e}\binom{-e}{u}(i-j)^{-e-u}\frac{1}{(X+j)^{f-u}}\;.$$*

*$(iii)$ Lorsque $e,f\le 0$, $$\frac{1}{(X+i)^e(X+j)^f}=
\sum_{u=0}^{-e}\sum_{v=0}^{-f}\binom{-e}{u}\binom{-f}{v}
i^{-e-u}j^{-f-v}X^{u+v}\;.$$*

*$(iv)$ Lorsque $i\not=j$ et $e,f\ge 1$, $$\frac{1}{(X+i)^e(X+j)^f}=\sum_{u=1}^e
\frac{\binom{e+f-1-u}{f-1}}{(i-j)^{e+f-u}}\frac{(-1)^f}{(X+i)^u}+
\sum_{v=1}^f\frac{\binom{e+f-1-v}{e-1}}{(j-i)^{e+f-v}}
\frac{(-1)^e}{(X+j)^v}.$$*

Nous allons exprimer $R_{N,p}(K;{}_p\underline{z}_{N})$ en termes de briques à l'aide du lemme 2 appliqué à la fraction $$\frac{1}{(k_{p-1}+j_{p-1})^{s_{p-1}}(k_{p-1}+K)^{s_p}}\;$$ qui apparaı̂t dans (eq:7). Cinq cas se présentent naturellement et il n'y en a pas d'autres possibles ; leurs intersections peuvent être non vides mais c'est sans importance ici.

Si $p=N$, resp. $p=2$, les colonnes correspondant à $s_{p+1}, s_{p+2}, \ldots, s_N$, resp. $\underline{s}_{p-2}$, des six briques $\textup{B}_{N-1}$ suivantes n'apparaissent pas.

### Premier cas : $K=j_{p-1}$ {#sssec: 221}

Cela correspond au cas (i) du lemme 2. On a alors $$R_{N,p}(K
;{}_p\underline{z}_{N})
=\textup{B}_{N-1}\Bigg[\,
\begin{array}{cccccc}
\underline{s}_{p-2}&s_{p-1}+s_p&s_{p+1}&s_{p+2}&\cdots&s_N\\
\underline{m}_{p-2}&m_{p-1}&j_{p-1}&0&\cdots&0\\
\underline{j}_{p-2}&j_{p-1}&0&0&\cdots&0
\end{array}\,
\Bigg\vert \, {}_p\underline{z}_{N}
\,\Bigg].$$

### Deuxième cas : $s_{p-1}\le 0$ et $s_p\ge 1$

Cela correspond au cas (ii) du lemme 2. On a alors $$\begin{gathered}
R_{N,p}(K;{}_p\underline{z}_{N})
=\sum_{u=0}^{-s_{p-1}}\binom{-s_{p-1}}{u} (j_{p-1}-K)^{-s_{p-1}-u}\\
\cdot\textup{B}_{N-1}\Bigg[\,
\begin{array}{cccccc}
\underline{s}_{p-2}&s_{p}-u &s_{p+1}&s_{p+2}&\cdots&s_N\\
\underline{m}_{p-2}&m_{p-1}& K&0&\cdots&0\\
\underline{j}_{p-2}& K& 0&0&\cdots&0
\end{array}\,
\Bigg\vert \, {}_p\underline{z}_{N}\,
\Bigg].
\end{gathered}$$

### Troisième cas : $s_{p-1}\ge 1$ et $s_p\le 0$

Cela correspond de nouveau au cas (ii) du lemme 2. On a alors $$\begin{gathered}
R_{N,p}(K;{}_p\underline{z}_{N})
=\sum_{u=0}^{-s_{p}}\binom{-s_{p}}{u}(K-j_{p-1})^{-s_{p}-u}\\
\cdot\textup{B}_{N-1}\Bigg[\,
\begin{array}{cccccc}
\underline{s}_{p-2}&s_{p-1}-u &s_{p+1}&s_{p+2}&\cdots&s_N\\
\underline{m}_{p-2}&m_{p-1}& K&0&\cdots&0\\
\underline{j}_{p-2}& j_{p-1}& 0&0&\cdots&0
\end{array}\,
\Bigg\vert \, {}_p\underline{z}_{N}\,
\Bigg].
\end{gathered}$$

### Quatrième cas : $s_{p-1}\le 0$ et $s_p\le 0$

Cela correspond au cas (iii) du lemme 2. On a alors $$\begin{gathered}
R_{N,p}(K;{}_p\underline{z}_{N})
=\sum_{u=0}^{-s_{p-1}}\sum_{v=0}^{-s_{p}}
\binom{-s_{p-1}}{u}\binom{-s_{p}}{v}
j_{p-1}^{-s_{p-1}-u}K^{-s_{p}-v}\\
\cdot\textup{B}_{N-1}\Bigg[\,
\begin{array}{cccccc}
\underline{s}_{p-2}&-u-v&s_{p+1}&s_{p+2}&\cdots&s_N\\
\underline{m}_{p-2}&m_{p-1}&K&0&\cdots&0\\
\underline{j}_{p-2}&0&0&0&\cdots&0
\end{array}\,
\Bigg\vert \, {}_p\underline{z}_{N}\,
\Bigg].
\end{gathered}$$

### Cinquième cas : $K\neq j_{p-1}$, $s_{p-1}\ge 1$ et $s_p\ge 1$ {#sssec: 225}

Cela correspond au cas (iv) du lemme 2. On a alors

$$\begin{gathered}
R_{N,p}(K;{}_p\underline{z}_{N})\\
= (-1)^{s_{p}}
\sum_{u=1}^{s_{p-1}}
\frac{\binom{s_{p-1}+s_{p}-1-u}{s_{p}-1}}
{(j_{p-1}-K)^{s_{p-1}+s_{p}-u}}
\,\textup{B}_{N-1}\Bigg[
\begin{array}{cccccc}
\underline{s}_{p-2}&u&s_{p+1}&s_{p+2}&\cdots&s_N\\
\underline{m}_{p-2}&m_{p-1}& K& 0&\cdots&0\\
\underline{j}_{p-2}&j_{p-1}& 0&0&\cdots&0
\end{array}\,
\Bigg\vert \, {}_p\underline{z}_{N}\,
\Bigg]
\\
+(-1)^{s_{p-1}}\sum_{v=1}^{s_p}
\frac{\binom{s_{p-1}+s_{p}-1-v}{s_{p-1}-1}}
{(K-j_{p-1})^{s_{p-1}+s_{p}-v}}
\,\textup{B}_{N-1}\Bigg[\,
\begin{array}{cccccc}
\underline{s}_{p-2}&v&s_{p+1}&s_{p+2}&\cdots&s_N\\
\underline{m}_{p-2}&m_{p-1}& K& 0&\cdots&0\\
\underline{j}_{p-2}&K& 0&0&\cdots&0
\end{array}\,
\Bigg\vert \, {}_p\underline{z}_{N}\,
\Bigg].
\end{gathered}$$

Chacun de ces cinq cas montre que $R_{N,p}(K;{}_p\underline{z}_{N})$ est un terme de profondeur $\le N-1$, de poids $\le \sum_{p=1}^N \max(s_p,0)$, ce qui conclut la preuve. ◻

*Démonstration du lemme 1.* Montrons (i). Remarquons tout d'abord que pour toute suite $(u_n)_{n\ge 0}$, on a $$\begin{aligned}
\lefteqn{\sum_{\ell=1}^{k+m}\frac{u_{\ell+j}\,z^{-\ell}}{(\ell+j)^s}
=\sum_{\ell=j+1}^{k+j+m}\frac{u_{\ell}\,z^{j-\ell}}{\ell^s}}\nonumber\\
&=&
\left(-\sum_{\ell=1}^j+
\sum_{\ell=1}^{k+i}+\varepsilon_{i,j+m}
\sum_{\ell=k+i\wedge (j+m)+1}^{k+i\vee
(j+m)}
\right)
\frac{u_{\ell}\,z^{j-\ell}}{\ell^s}\nonumber\\
&=&
\left(-\sum_{\ell=1}^j+
\sum_{\ell=1}^{k+i}
\right)
\frac{u_{\ell}\,z^{j-\ell}}{\ell^s}
+\varepsilon_{i,j+m}
\sum_{\ell=i\wedge (j+m)+1}^{i\vee
(j+m)}\frac{u_{k+\ell}\,z^{j-k-\ell}}{(k+\ell)^s},
\label{eq:suite}
\end{aligned}$$ après quelques manipulations immédiates.

Supposons maintenant $2\le p\le N-1$. On a $$\begin{gathered}
\textup{B}_N\Bigg[\,
\begin{array}{ccccc}
\underline{s}_{N}&&&&\\
\underline{m}_{p}&j_{p}&0&\cdots&0 \\
\underline{j}_{p}& 0& 0&\cdots&0
\end{array}\,
\Bigg\vert \,\underline{z}_N \,
\Bigg]=\\
\sum_{k_{p-2}+m_{p-1} \ge k_{p-1}\ge 1\atop{
\vdots\atop{
k_1+m_2 \ge k_2\ge 1\atop
k_1\ge 1}}} \frac{z_1^{-k_1}\cdots z_p^{-k_{p-1}}}
{\prod_{i=1}^{p-1}(k_i+j_i)^{s_i}}\sum_{k_p=1}^{k_{p-1}+m_p}
\frac{z_p^{-k_p}}{(k_p+j_p)^{s_p}}\,Q_{N,p+1}(k_p+j_p; \underline{z}_{N}^{p+1})\,
\end{gathered}$$ On applique (eq:suite) à la somme $\sum_{k_p=1}^{k_{p-1}+m_p}(\ldots)$ et à la suite $u_{n}=Q_{N,p+1}(n; \underline{x}_{N}^{p+1})$ : grâce à la relation (eq:6) entre $Q_{N,p}$ et $Q_{N,p+1}$, on voit alors que $$\begin{gathered}
\textup{B}_N\Bigg[\,
\begin{array}{ccccc}
\underline{s}_{N}&&&&\\
\underline{m}_{p}&j_{p}&0&\cdots&0 \\
\underline{j}_{p}& 0& 0&\cdots&0
\end{array}\,
\Bigg\vert \,\underline{z}_N\,
\Bigg]
= z_p^{j_p}\,\textup{B}_N\Bigg[\,
\begin{array}{ccccc}
\underline{s}_{N}&&&&\\
\underline{m}_{p-1}&j_{p-1}&0&\cdots&0 \\
\underline{j}_{p-1}& 0& 0&\cdots&0
\end{array}\,
\Bigg\vert \,\underline{z}_N\,
\Bigg]\\
-z_{p}^{j_p}\,Q_{N,p}(j_p ; \underline{z}_{N}^{p})\,
\textup{B}_{p-1}\Bigg[\,
\begin{array}{c}
\underline{s}_{p-1}\\
\underline{m}_{p-1} \\
\underline{j}_{p-1}
\end{array}
\Bigg\vert\,\underline{z}_p\,
\Bigg]
+\varepsilon_p
\sum_{k_p=t_p +1}^{T_p}z_p^{j_p-k_p}R_{N,p}(k_p;{}_p\underline{z}_{N}).
\end{gathered}$$

Pour (ii), on a $$\begin{aligned}
\lefteqn{
\textup{B}_N\Bigg[\,
\begin{array}{ccccc}
\underline{s}_{N}&&&&\\
0  &j_{1}&0&\cdots&0 \\
\underline{j}_{1}& 0& 0&\cdots&0
\end{array}\,
\Bigg\vert \,\underline{z}_N\,
\Bigg]
}\\
&=&\sum_{k_1=1}^{\infty}\frac{z_1^{-k_1}}
{(k_1+j_1)^{s_1}}\,Q_{N,2}(k_1+j_1;\underline{z}_{N}^{2})
=\sum_{k_1=j_1+1}^{\infty}\frac{z_1^{j_1-k_1}}{k_1^{s_1}}\,Q_{N,2}(k_1;
\underline{z}_{N}^{2})\\
&=& z_1^{j_1}\,\textup{B}_N
\Bigg[\,
\begin{array}{ccccc}
\underline{s}_{N}&&&&\\
0&0&0&\cdots&0 \\
0& 0& 0&\cdots&0
\end{array}\,
\Bigg\vert \,\underline{z}_N\,
\Bigg]-\sum_{k_1=1}^{j_1}\frac{z_1^{j_1-k_1}}{k_1^{s_1}}\,
Q_{N,2}(k_1; \underline{z}_{N}^{2})\\
&=& z_1^{j_1}\textup{La}_{\underline{s}_N}(1/\underline{z}_N)-z_1^{j_1}\,Q_{N,1}(j_1;\underline{z}_{N})
\end{aligned}$$ ce qui termine la démonstration du lemme. ◻

*Démonstration du lemme 2.* Les points (i), (ii) et (iii) sont triviaux et on démontre seulement (iv), qui l'est à peine moins. En effet, on a $$\frac{1}{(X+i)^e(X+j)^f} = \sum_{u=1}^e \frac{a_u}{(X+i)^u} +
\sum_{v=1}^f \frac{b_v}{(X+j)^v}$$ avec $$\begin{gathered}
a_u = \frac{1}{(e-u)!} \bigg( \frac{1}{(X+j)^f}\bigg)^{e-u}\bigg\vert_{X=-i}
\\
=
\frac{(-f)(-f-1)\cdots (-f-e+u+1)}{(e-u)!(j-i)^{e+f-u}}=
\binom{e+f-u-1}{f-1}\frac{(-1)^f}{(i-j)^{e+f-u}}
\end{gathered}$$ et la formule similaire attendue pour $b_v.$ ◻

# Précisions sur le Théorème 5 {#sec:raffinement algo}

Le but de ce paragraphe est de préciser la nature des polynômes de Laurent qui apparaissent quand on itère le Théorème 5, sous la condition que tous les exposants $s_i$ sont strictement positifs.

On pose

-   $M_i=\sum_{k=1}^{i} m_k$ avec $M_0=0$ ;

-   $I_N=\max_{i=1, \ldots, N}(T_i+M_{i-1})$ avec $T_i=j_{i-1}\vee (j_i+m_i)$, $j_0=0$ et $I_0=0$ ;

-   $J_{N}=\max_{i=1,\ldots, N}(j_{i})$ et $J_0=0$ ;

-   $K_N=\max_{i=1, \ldots, N}(T_i)$ et $K_0=0$;

-   $\Sigma_N=\sum_{i=1}^N s_{i}$.

$J_N$ est le cas spécial de $I_N$ obtenu lorsque les modulations sont toutes nulles. Rappelons que $\textup{d}_n$ dénote le p.p.c.m. des entiers $1, 2, \ldots, n$. Par convention, $\textup{d}_0=1$. On utilisera le fait trivial que $\textup{d}_n^e \textup{d}_m^f$ divise $\textup{d}_{n\vee m}^{e+f}$.

**Théorème 6**. *Supposons que tous les exposants $s_i$ sont strictement positifs.*

*$(i)$ Les polynômes de Laurent qui interviennent dans la décomposition de la brique décalée-modulée large (eq:3) en polylogarithmes multiples sont dans $$d_{I_{N}}^{-\Sigma_N}\mathbb{Z}
[z_1,z_2^{\pm 1},\ldots,z_N^{\pm 1}]$$ et leur degré en $z_1$ est au plus $K_N$.*

*$(ii)$ Les polynômes de Laurent qui interviennent dans la décomposition de la brique décalée large (eq:4) en polylogarithmes multiples sont dans $$d_{J_{N}}^{-\Sigma_{N}}\mathbb{Z}$$ et leur degré en $z_1$ est au plus $J_N$.*

**Remarque 4**. *$(1)$ Le point $(ii)$ est le seul vraiment utile ; nous ne savons pas le démontrer sans d'abord démontrer $(i$), dont il est un cas particulier.*

*$(2)$ On n'utilisera pas que les $s_i$ sont strictement positifs pour démontrer que les polynômes de Laurent sont des polynômes de degré $\le j_1$ en la variable $z_1$.*

*$(3)$ Concernant le dénominateur, un résultat similaire a probablement lieu dans le cas général mais nous n'avons pas cherché à l'expliciter, faute de perspectives diophantiennes évidentes.*

*Proof.* (i) Nous procédons, en deux temps, par récurrence sur la profondeur $N$ de la brique (eq:3) : le point (ii) en découle en prenant le cas particulier de modulations toutes nulles.

## Preuve de l'assertion sur les dénominateurs

Le cas $N=1$ est immédiat : on a $$\label{eq:B_1 recurrence}
\textup{B}_1\Bigg[\,
\begin{array}{c}
s_{1}\\
0\\
j_{1}
\end{array}\,
\Bigg \vert \,z_1\,
\Bigg]=
z_1^{j_1}\,\textup{La}_{s_1}(z_1)-z_1^{j_1}\,Q_{1,1}(j_1;z_1),$$ où $\displaystyle
Q_{1,1}(j_1;z_1)=\sum_{k_1=1}^{j_1}\frac{z_1^{-k_1}}
{k_1^{s_1}}$ a pour dénominateur $\textup{d}_{j_1}^{s_1}=\textup{d}_{I_1}^{\Sigma_1}$.

Supposons maintenant le Théorème 6 vrai jusqu'à la profondeur $N-1$ et analysons les différents termes de l'équation (eq:8), que nous rappelons : $$\begin{gathered}
\textup{B}_N\Bigg[\,
\begin{array}{c}
\underline{s}_N\\
\underline{m}_N\\
\underline{j}_N
\end{array}\,
\Bigg\vert \,\underline{z}_N\,
\Bigg]=
(z_1^{j_1}\cdots
z_N^{j_N})\,\textup{La}_{\underline{s}_N}(\underline{z}_N)\\
-\sum_{p=1}^N (z_p^{j_p}\cdots
z_N^{j_N}) \,Q_{N,p}(j_p; \underline{z}_{N}^{p})\,\textup{B}_{p-1}
\Bigg[\,
\begin{array}{c}
\underline{s}_{p-1}\\
\underline{m}_{p-1} \\
\underline{j}_{p-1}
\end{array}\,
\Bigg\vert\, \underline{z}_p\,
\Bigg]\\ +\sum_{p=2}^N \varepsilon_p\,(z_p^{j_p}\cdots z_N^{j_N})
\sum_{k_p=t_p +1}^{T_p}z_p^{-k_p}R_{N,p}(k_p; {}_p\underline{z}_{N}).
\end{gathered}$$ Tout d'abord $$Q_{N,p}(j_p;\underline{z}_{N}^p)
=\sum_{j_p\ge k_p\ge \cdots\ge k_N\ge 1}
\frac{z_{p}^{-k_{p}}\cdots z_{N}^{-k_{N}}}
{\prod_{i=p}^N k_i^{s_i}}$$ a pour dénominateur $\textup{d}_{j_p}^{s_p+\cdots+s_N}$. Par hypothèse de récurrence, un dénominateur de la brique $\textup{B}_{p-1}$ est $\textup{d}_{I_{p-1}}^{s_1+\cdots+s_{p-1}}$, même pour $p=1$. Un dénominateur des termes $Q_{N,p}\textup{B}_{p-1}$ est donc $\textup{d}_{j_p}^{s_p+\cdots+s_N}\,\textup{d}_{I_{p-1}}^{s_1+\cdots+s_{p-1}}$, qui divise $\textup{d}_{I_{N}}^{\Sigma_N}$ puisque $j_p\vee
I_{p-1}\le (T_p+M_{p-1})\vee
I_{p-1} = I_p\le  I_N$ pour tout $p\in\{1,\ldots, N\}$.

Il reste à analyser les termes $R_{N,p}(k_p; {}_p\underline{z}_{N})$ : nous allons distinguer deux cas.

### Premier cas : $k_p=j_{p-1}$

On est alors dans la situation du paragraphe 4.3.1: $$R_{N,p}(j_{p-1};{}_p\underline{z}_{N})
=\textup{B}_{N-1}\Bigg[\,
\begin{array}{cccccc}
\underline{s}_{p-2}&s_{p-1}+s_p&s_{p+1}&s_{p+2}&\cdots&s_N\\
\underline{m}_{p-2}&m_{p-1}&j_{p-1}&0&\cdots&0\\
\underline{j}_{p-2}&j_{p-1}&0&0&\cdots&0
\end{array}\,
\Bigg\vert \, {}_p\underline{z}_{N}\,
\Bigg].\label{eq:10}$$ L'hypothèse de récurrence s'applique : un dénominateur de la brique est $$\textup{d}_{I_{p-1}\vee (j_{p-1}\vee (0+j_{p-1})+M_{p} )}^{\Sigma_N} =
\textup{d}_{I_{p-1}\vee (j_{p-1} +M_{p} )}^{\Sigma_N}.$$ Comme $j_{p-1}+M_{p-1}\le T_{p}+M_{p-1}$, ce dénominateur divise $\textup{d}_{I_{p}}^{\Sigma_N}$, qui divise $\textup{d}_{I_{N}}^{\Sigma_N}$.

### Second cas : $k_p\not=j_{p-1}$

On est maintenant dans la situation du paragraphe 4.3.5 : $$\sum_{p=2}^N\varepsilon_p\,(z_p^{j_p}\cdots z_N^{j_N})\sum_{k_p=t_p +1\atop
k_p\not=j_{p-1}}^{T_p}R_{N,p}(k_p;{}_p\underline{z}_{N})
=\sum_{p=2}^N\varepsilon_p\,(z_p^{j_p}\cdots z_N^{j_N})\bigg(\sum_{u=1}^{s_{p-1}}B_{1,p}(u)
+\sum_{v=1}^{s_p}B_{2,p}(v)\bigg)$$ avec $$\begin{gathered}
B_{1,p}(u)=(-1)^{s_{p}}\sum_{k_p=t_p +1\atop k_p\not=j_{p-1}}^{T_p}
\frac{\binom{s_{p-1}+s_{p}-1-v}{s_{p}-1}}{(j_{p-1}-k_p)^{s_{p-1}+s_{p}-u}}\\
\cdot
\textup{B}_{N-1}\Bigg[\,
\begin{array}{cccccc}
\underline{s}_{p-2}&u&s_{p+1}&s_{p+2}&\cdots&s_N\\
\underline{m}_{p-2}&m_{p-1}& k_p& 0&\cdots&0\\
\underline{j}_{p-2}&j_{p-1}& 0&0&\cdots&0
\end{array}\,
\Bigg\vert\, {}_p\underline{z}_{N}
\Bigg]  \label{eq:cpu}
\end{gathered}$$ et $$\begin{gathered}
B_{2,p}(v)=(-1)^{s_{p-1}}\sum_{k_p=t_p
+1\atop
k_p\not=j_{p-1}}^{T_p}
\frac{\binom{s_{p-1}+s_{p}-1-v}{s_{p-1}-1}}
{(k_p-j_{p-1})^{s_{p-1}+s_{p}-v}}\\
\cdot \textup{B}_{N-1}\Bigg[\,
\begin{array}{cccccc}
\underline{s}_{p-2}&v&s_{p+1}&s_{p+2}&\cdots&s_N\\
\underline{m}_{p-2}&m_{p-1}& k_p& 0&\cdots&0\\
\underline{j}_{p-2}&k_p& 0&0&\cdots&0
\end{array}\,
\Bigg\vert\, {}_p\underline{z}_{N}\,
\Bigg].
\label{eq:dpu}
\end{gathered}$$ Nous allons montrer que $\textup{d}_{I_{N}}^{\Sigma_N}$ est un dénominateur convenable pour les termes (eq:cpu) et (eq:dpu), ce qui suffira puisqu'il est indépendant de $p$, $u$ et $v$. Fixons $p$, $u$ et $v$. Par hypothèse de récurrence, les deux briques $\textup{B}_{N-1}$ ont pour dénominateurs respectifs $$D_1 = \textup{d}_{I_{p-1}\vee (k_p+ M_{p-1})}^{u+\Sigma_N-s_p-s_{p-1}}
\quad \textup{et} \quad
D_2 = \textup{d}_{I_{p-2}\vee (j_{p-2}\vee(k_p+m_{p-1})+M_{p-2})\vee
(k_p +M_{p-1})}^{v+\Sigma_N-s_p-s_{p-1}}.$$ Puisque $k_p\le T_p$, on a $I_{p-1}\vee (k_p+M_{p-1})\le I_{p-1}\vee (T_p + M_{p-1}) = I_p$ et donc $D_1$ divise $\textup{d}_{I_p}^{u+\Sigma_N-s_p-s_{p-1}}$. D'autre part, si $j_{p-2}\le k_p+ m_{p-1}$, on a $$j_{p-2}\vee(k_p+m_{p-1})+M_{p-2}\le k_p+m_{p-1}+M_{p-2}\le T_p+M_{p-1}$$ tandis que si $j_{p-2}\ge k_p+ m_{p-1}$, alors $$j_{p-2}\vee(k_p+m_{p-1})+M_{p-2}\le j_{p-2}+M_{p-2}\le T_{p-1}+M_{p-2},$$ d'où $D_2$ divise $\textup{d}_{I_{p-2}\vee (T_{p-1}+M_{p-2})\vee
(T_p +M_{p-1})}^{v+\Sigma_N-s_p-s_{p-1}}= \textup{d}_{I_p}^{v+\Sigma_N-s_p-s_{p-1}}$. On obtient donc des dénominateurs uniformes en $k_p$ pour les briques $\textup{B}_{N-1}$ : $$\textup{d}_{I_{p}}^{u+\Sigma_N-s_p-s_{p-1}}
\quad \textup{et}\quad
\textup{d}_{I_{p}}^{v+\Sigma_N-s_p-s_{p-1}}.$$ Les deux sommes $$\textup{d}_{I_{p}}^{u+\Sigma_N-s_p-s_{p-1}}B_{1,p}(u)=(-1)^{s_p}\sum_{k_p=t_p +1\atop k_p\not=j_{p-1}}^{T_p}
\frac{\binom{s_{p-1}+s_{p}-1-u}{s_{p}-1}}
{(j_{p-1}-k_p)^{s_{p-1}+s_{p}-u}}\,\textup{d}_{I_{p}}^{u+
\Sigma_N-s_p-s_{p-1}}\textup{B}_{N-1}[\cdots]$$ et $$\textup{d}_{I_{p}}^{v+\Sigma_N-s_p-s_{p-1}} B_{2,p}(v)=(-1)^{s_{p-1}}\sum_{k_p=t_p
+1\atop
k_p\not=j_{p-1}}^{T_p}
\frac{\binom{s_{p-1}+s_{p}-1-v}{s_{p-1}-1}}
{(k_p-j_{p-1})^{s_{p-1}+s_{p}-v}}\,
\textup{d}_{I_{p}}^{v+\Sigma_N-s_p-s_{p-1}}
\textup{B}_{N-1}[\cdots]$$ ont donc pour dénominateurs respectifs $\textup{d}_{\vert j_p+m_p-j_{p-1}\vert}^{-u+s_{p-1}+s_p}$ et $\textup{d}_{\vert j_p+m_p-j_{p-1}\vert}^{-v+s_{p-1}+s_p},$ qui divisent trivialement $\textup{d}_{I_{p}}^{-u+s_{p-1}+s_p}$, resp. $\textup{d}_{I_{p}}^{-v+s_{p-1}+s_p}$, car $\vert j_p+m_p-j_{p-1}\vert\le T_p\le I_p$. Ainsi, on peut prendre $$\textup{d}_{I_{p}}^{-u+s_{p-1}+s_p}\,
\textup{d}_{I_{p}}^{u+\Sigma_N-s_p-s_{p-1}}=\textup{d}_{I_{p}}^{\Sigma_N}
\label{eq:den1}$$ et $$\textup{d}_{I_{p}}^{-v+s_{p-1}+s_p}
\,\textup{d}_{I_{p}}^{v+\Sigma_N-s_p-s_{p-1}}
=\textup{d}_{I_{p}}^{\Sigma_N},
\label{eq:den2}$$ comme dénominateur de (eq:cpu) et (eq:dpu), ce qui achève la preuve du Théorème 6 puisque $\textup{d}_{I_p}^{\Sigma_N}$ divise $\textup{d}_{I_N}^{\Sigma_N}$.

## Preuve de l'assertion sur le degré en $z_1$

De nouveau, on raisonne par récurrence sur la profondeur $N\ge 1$. C'est évidemment vrai pour $N=1$ par l'équation (eq:B_1 recurrence). Supposons maintenant l'assertion vraie pour $N-1$ et, comme précédemment, analysons les termes de l'équation (eq:8). Le terme $(z_1^{j_1}\cdots
z_N^{j_N})\,\textup{La}_{\underline{s}_N}(\underline{z}_N)$ est de la forme voulue, avec un degré $j_1\le K_N$. Dans le terme $$\sum_{p=1}^N (z_p^{j_p}\cdots
z_N^{j_N}) \,Q_{N,p}(j_p; \underline{z}_{N}^{p})\,\textup{B}_{p-1}
\Bigg[\,
\begin{array}{c}
\underline{s}_{p-1}\\
\underline{m}_{p-1} \\
\underline{j}_{p-1}
\end{array}\,
\Bigg\vert\, \underline{z}_p\,
\Bigg],$$ si $p\ge 2$, la variable $z_1$ n'apparaı̂t pas dans les polynômes de Laurent $Q_{N,p}(j_p; \underline{z}_{N}^{p})$ et seulement dans la brique $B_{p-1}[\ldots]$ qui est de profondeur $p-1\le N-1$ : l'hypothèse de récurrence s'applique et seules les puissances positives de $z_1$ interviennent bien, jusqu'au plus $z_1^{K_{p-1}}$, donc au plus $z_1^{K_N}$. Si $p=1$, alors $z_1$ intervient dans l'expression $z_1^{j_1}\,Q_{N,1}(j_1; \underline{z}_{N}^{1})\,\textup{B}_{0}[\ldots] = z_1^{j_1}\,Q_{N,1}(j_1; \underline{z}_{N})$, qui est aussi un polynôme en $z_1$ de degré au plus $j_1 \le K_N$. Il reste le dernier terme $$\sum_{p=2}^N \varepsilon_p\,(z_p^{j_p}\cdots z_N^{j_N})
\sum_{k_p=t_p +1}^{T_p}z_p^{-k_p}R_{N,p}(k_p; {}_p\underline{z}_{N})$$ qui ne dépend de $z_1$ que par $R_{N,p}(k_p; {}_p\underline{z}_{N})$. Or les expressions que nous en avons données au paragraphe précédent montrent qu'il s'agit d'une combinaison linéaire de briques de profondeur $\le N-1$ évaluées en ${}_p\underline{z}_{N}$ et dont les coefficients ne dépendent pas des $z_i$. Dans ${}_p\underline{z}_{N}$, la variable $z_1$ apparaı̂t seule si $3 \le p\le N$ : l'hypothèse de récurrence s'applique et on vérifie que le degré en $z_1$ est au plus $K_{p}\le K_N$. Si $p=2$, alors il y a une subtilité car $z_1$ apparaı̂t multiplié par $z_2$ : ce n'est pas gênant, l'hypothèse de récurrence s'applique de nouveau et le degré en $z_1$ est $\le T_2\le
K_N$, ce qui conclut la démonstration. ◻

# Non-enrichissement des $\textup{La}_{s_1,\ldots, s_p}$ à exposants négatifs

L'algorithme de décomposition des briques peut faire apparaître des polylogarithmes larges à exposants négatifs (ou nuls). Par exemple la décomposition de l'intégrale de Sorokin pour $\zeta (3)$ $$\int_{[0,1]^3} \displaystyle\frac{u^n (1-u)^n v^n (1-v)^n w^n (1-w)^n}{(z_1 -uv)^{n+1}
(z_1z_2 -uvw)^{n+1}} \,\textup{d}u \textup{d}v \textup{d}w ,$$ fait intervenir des $\textup{La}_{s_1,s_2} (1/z_1, 1/z_2 )$, avec $s_1=1,2$, $s_2=0, -1, \dots, -n+1$.

Afin de régler ces cas singuliers, on démontre un résultat dit de *non-enrichissement arithmétique*.

**Théorème 7**. *Supposons que, pour tout $j=1, \ldots, p$, on ait $\vert z_j\vert <1$. Alors, tout polylogarithme multiple large $\textup{La}_{s_1,\dots ,s_p} (z_1 ,\dots ,z_p)$ de profondeur $p$ ayant certains exposants $s_j\le 0$ s'exprime comme une combinaison linéaire finie de polylogarithmes multiples larges $\textup{La}_{s'_1,\dots ,s'_q} (z_1^* ,\dots ,z_q^* )$ de profondeur $q \in \{0, \dots, p\}$, avec $s'_j\ge 1$, où les $z_i^*$ sont certains produits des $z_j$. Les coefficients de la combinaison linéaire sont des polynômes à coefficients rationnels en les $\displaystyle\big((1-z_{j_1}\cdots z_{j_m})^{-1}\big)_{1\le j_1< \ldots < j_m\le p, \,m\ge 1}$ et les $\big(z_j^{\pm 1}\big)_{1\le j\le p}$. De plus, on a $\sum_{j=1}^q s'_j\le \sum_{j=1}^p \max(0,s_j)$ pour toutes les suites d'exposants $\underline{s}'$ qui apparaissent.*

**Remarque 5**. *$(1)$ Pour tout $z$ tel que $\vert z\vert <1$, on a $$\textup{La}_{-s} (z) = \left(z\frac{\textup{d}}{ \textup{d}z}\right)^s \left(\frac{1}{1-z}\right) \in (1-z)^{-s-1}\mathbb{Z}[z].$$*

*$(2)$ Ce théorème est de facture informelle mais sa démonstration offre un moyen algorithmique de l'expliciter.*

*$(3)$ Un résultat de ce type est annoncé par Écalle ([@ecalle pp. 419--420]) dans le cas des polyzêtas, sans démonstration.*

## Préliminaires

On suppose dans toute la suite de ce paragraphe que toutes les variables notées $z$ ou $z_j$ sont de modules $<1$. La démonstration utilisera l'identité triviale suivante, valable pour tout entier $K\ge 1$ : $$\sum_{k_1 =1}^{K} \sum_{k_2=1}^{k_1} = \sum_{k_2 =1}^{K}
\bigg( \sum_{k_1=1}^{K} -\sum_{k_1=1}^{k_2 -1} \bigg ).
\label{eq:star}$$ Pour tous entiers $s\ge 0$ et $K\ge 1$, on définit $P_{s} (K,z)=\displaystyle\sum_{k=1}^K k^s z^k,$ qui vérifie : $$\label{eq:pszN}
P_{s} (K,z) =
\bigg(z\frac{\textup{d}}{\textup{d}z}\bigg)^s \left (z \frac{1-z^{K}}{1-z} \right ).$$ On en déduit que l'on a $$\label{eq:pszNzneq1}
P_{s} (K,z)= \sum_{\ell=0}^s \frac{z^Ka_{1, \ell}(s,z)+a_{2,\ell}(s,z)}{(1-z)^{s+1}}
K^\ell$$ où $a_{1, \ell}(s,z)$ et $a_{1, \ell}(s,z)$ sont des polynômes en $z$ de degré au plus $s$ et indépendants de $K$. On notera

Les objets naturels qui vont intervenir sont des *polylogarithmes larges tronqués* : $$\textup{La}^K_{s_1 , \dots , s_p}
(z_1 ,\dots ,z_p )= \displaystyle\sum_{K\geq k_1 \geq \dots \geq
k_p \geq 1} \displaystyle\frac{z_1^{k_1} \dots z_p^{k_p}}{k_1^{s_1}
\dots k_p^{s_p} }.$$ On remarque que l'on a $\textup{La}^K_{s_1} (z_1) =  P_{-s_1}(K,z_1)$ lorsque $s_1\le 0$.

On aura besoin du lemme suivant.

**Lemme 3**. *Soient des entiers $s_1\ge 0$ et $s_2, \ldots ,s_p\in\mathbb{Z}$. Pour tous entiers $K\geq 1$ et $p\geq 2$, on a : $$\begin{gathered}
\textup{La}^K_{-s_1 ,s_2 , \dots , s_p } (z_1 ,\dots ,z_p ) =
P_{s_1}(K,z_1)
\textup{La}^K_{s_2 , \dots , s_p } (z_2 ,\dots ,z_p )
\\
- \sum_{\ell=0}^{s_1} \frac{a_{1,\ell}(s_1, z_1)}{(1-z_1)^{s_1+1}z_1}\sum_{m=0}^\ell
\binom{\ell}{m}
(-1)^{\ell-m} \textup{La}^K_{s_2 -m , s_3, \dots , s_p} (z_1z_2 , z_3, \ldots ,z_p )
\\
- \sum_{\ell=0}^{s_1} \frac{a_{2,\ell}(s_1, z_1)}{(1-z_1)^{s_1+1}}\sum_{m=0}^\ell
\binom{\ell}{m}
(-1)^{\ell-m} \textup{La}^K_{s_2 -m , s_3, \dots , s_p} (z_2 ,\dots ,z_p ).
\end{gathered}$$*

*Proof.* En utilisant (eq:star), on a : $$\begin{aligned}
\textup{La}^K_{-s_1 ,s_2 , \dots , s_p } (z_1 ,\dots ,z_p )
&=&\sum_{k_2 =1}^K \frac{z_2^{k_2}}{k_2^{s_2}}
\bigg( \sum_{k_1 =1}^K k_1^{s_1} z^{k_1} - \displaystyle\sum_{k_1
=1}^{k_2 -1} k_1^{s_1} z^{k_1} \bigg)
\textup{La}^{k_2 }_{s_3  , \dots , s_p } (z_3 ,\dots ,z_p )
\\
&=&
\sum_{k_2 =1}^K {z_2^{k_2} \over k_2^{s_2}} \big(
P_{s_1} (K,z_1) - P_{s_1} (k_2 -1,z_1) \big)
\textup{La}^{k_2}_{s_3 , \dots , s_p } (z_3 ,\dots ,z_p ) .
\end{aligned}$$ Au moyen de (eq:pszNzneq1), on obtient $$\begin{gathered}
\textup{La}^K_{-s_1 ,s_2 , \dots , s_p } (z_1 ,\dots ,z_p )
=P_{s_1}(K,z_1)
\sum_{k_2=1}^K \bigg({z_2^{k_2} \over k_2^{s_2}}
\textup{La}^{k_2}_{s_3 , \dots , s_p} (z_3 ,\dots ,z_p ) \bigg)
\\
-
\sum_{\ell=0}^{s_1}
\frac{1}{(1-z_1)^{s_1+1}}
\sum_{k_2=1}^K (z_1^{k_2-1}a_{1, \ell}(s_1,z_1)+a_{2,\ell}(s_1,z_1))\bigg({z_2^{k_2} \over k_2^{s_2}}
\,(k_2 - 1)^\ell\,
 \textup{La}^{k_2}_{s_3 , \dots , s_p} (z_3 ,\dots ,z_p ) \bigg).
\end{gathered}$$ La première somme vaut exactement $$P_{s_1}(K,z_1)
\textup{La}^K_{s_2 , \dots , s_p} (z_2 ,\dots ,z_p ).$$ La seconde somme faisant intervenir $(k_2 -1)^\ell$ est à peine plus compliquée. En développant le terme $(k_2 -1)^\ell$ par le théorème binomial et en remplaçant directement dans la somme, on obtient en effet : $$\begin{gathered}
- \sum_{\ell=0}^{s_1} \frac{a_{1,\ell}(s_1, z_1)}{(1-z_1)^{s_1+1}z_1}\sum_{m=0}^\ell
\binom{\ell}{m}
(-1)^{\ell-m} \textup{La}^K_{s_2 -m , s_3, \dots , s_p} (z_1z_2 , z_3, \dots ,z_p )
\\
- \sum_{\ell=0}^{s_1} \frac{a_{2,\ell}(s_1, z_1)}{(1-z_1)^{s_1+1}}\sum_{m=0}^\ell
\binom{\ell}{m}
(-1)^{\ell-m} \textup{La}^K_{s_2 -m , s_3,\dots , s_p} (z_2 , z_3, \dots ,z_p ),
\end{gathered}$$ ce qui termine la démonstration. ◻

## Démonstration du théorème 7

On remarque que le lemme 3 exprime un polylogarithme de profondeur $p$ à l'aide de polylogarithmes de profondeur $p-1$, ce qui ouvre la porte à une démonstration du théorème 7 par récurrence

Pour $p=1$, le théorème est vrai, comme le montre la remarque (1) qui suit son énoncé.

On suppose que l'on sait décomposer les polylogarithmes de profondeur $\leq p-1$ (avec $p-1\ge 1$) de la manière prévu par le théorème. Soit maintenant $s_1 ,\dots , s_p$ une suite quelconque d'entiers, avec au moins un $s_j\le 0$ : notons ${q+1}$ le plus petit indice $\ge 1$ tel que $s_{q+1} \le 0$. Pour simplifier, on note $s_{q+1} =-s$ avec $s \ge 0$. On doit distinguer trois cas : $q=0$, $1\le q\le p-2$ et $q=p-1.$

-- Le cas $q=0$. Notons que pour tout entier $t\ge 0$, on a $$\sum_{k=\ell}^{\infty} k^{t} z^{k} =
\left(z\frac{\textup{d}}{ \textup{d}z}\right)^t \left(\frac{z^{\ell}}{1-z}\right) = \frac{z^\ell Q_{t}(\ell,z)}{(1-z)^{t+1}}$$ avec $Q_{t}(\ell,z)\in\mathbb{Z}[\ell,z]$ de degré $s$ en $\ell$ et $z$. On pose donc $Q_t(\ell,z) = \sum_{j=0}^s q_{j,s}(z) \ell^j.$ On a alors $$\begin{aligned}
\textup{La}_{s_1 ,s_2 , \dots , s_p } (z_1 , z_2, \dots ,z_p )
&=&  \sum_{k_2 \ge \cdots \ge k_p\ge 1} \bigg(
\frac{z_2^{k_2}\cdots z_p^{k_p}}{k_2^{s_2}\cdots k_p^{s_p}} \sum_{k_1=k_2}^{\infty} k_1^{s} z_1^{k_1}\bigg)\\
&=&\frac{1}{(1-z_1)^{s+1}} \sum_{k_2 \ge \cdots \ge k_p\ge 1} Q_{s}(k_2, z_1)
\frac{(z_1z_2)^{k_2}z_3^{k_3}\cdots z_p^{k_p}}{k_2^{s_2}k_3^{s_3}\cdots k_p^{s_p}}\\
&=& \frac{1}{(1-z_1)^{s+1}} \sum_{j=0}^s q_{j,s}(z_1) \textup{La}_{s_2 -j, s_3, \dots , s_p } (z_1z_2, z_3 ,\dots ,z_p).
\end{aligned}$$ Comme on n'a finalement que des $\textup{La}$ de profondeur $p-1$, l'hypothèse de récurrence s'applique.

-- Le cas $1\le q\le p-2$. On applique le lemme 3 de telle sorte que $$\begin{aligned}
\lefteqn{\textup{La}_{s_1 ,s_2 , \dots , s_p } (z_1 , z_2, \dots ,z_p ) }\nonumber
\\
&=&
\sum_{k_1\ge \cdots\ge k_q\ge 1}
\frac{z_1^{k_1}\cdots z_q^{k_q}}{k_1^{s_1}\cdots k_q^{s_q}} \,
\textup{La}^{k_q}_{-s, s_{q+2}, \ldots, s_p} (z_{q+1}, z_{q+2}, \ldots, z_p)\nonumber
\\
&=& \sum_{k_1\ge \cdots \ge k_q\ge 1}
\frac{z_1^{k_1}\cdots z_q^{k_q}}{k_1^{s_1}\cdots k_q^{s_q}} P_{s}(k_q,z_{q+1})
\textup{La}^{k_q}_{s_{q+2} , \dots , s_p } (z_{q+2} ,\dots ,z_p )\label{eq:tanguy1}
\\
&& \quad -
\sum_{\ell=0}^{s} \frac{a_{1,\ell} (s ,z_{q+1} )}{(1-z_{q+1})^{s+1}z_{q+1}} \sum_{m=0}^\ell \bigg((-1)^{\ell-m} \binom{\ell}{m}
\nonumber \\
&& \qquad  \qquad\times  \sum_{k_1\ge \cdots \ge k_q\ge 1}
\frac{z_1^{k_1}\cdots z_q^{k_q}}{k_1^{s_1}\cdots k_q^{s_q}} \,
\textup{La}^{k_q}_{s_{q+2} - m , s_{q+3} , \dots , s_p } (z_{q+1}z_{q+2} , z_{q+3} ,\dots ,z_p )\bigg) \label{eq:tanguy22}\\
&& \qquad
-\sum_{\ell=0}^{s} \frac{a_{2,\ell} (s ,z_{q+1} )}{(1-z_{q+1})^{s+1}} \sum_{m=0}^\ell \bigg((-1)^{\ell-m} \binom{\ell}{m}
\nonumber \\
&& \qquad \qquad \times  \sum_{k_1\ge \cdots \ge k_q\ge 1}
\frac{z_1^{k_1}\cdots z_q^{k_q}}{k_1^{s_1}\cdots k_q^{s_q}} \,
\textup{La}^{k_q}_{s_{q+2} - m , s_{q+3} , \dots , s_p } (z_{q+2} , z_{q+3} ,\dots ,z_p )\bigg)
\label{eq:tanguy2}
\end{aligned}$$

Il est facile de traiter les séries (eq:tanguy22) et (eq:tanguy2) puisqu'elles valent respectivment $$\textup{La}_{s_1, \ldots, s_{q}, s_{q+2}-m, s_{q+3}, \ldots, s_p} (z_1, \ldots, z_{q}, z_{q+1}z_{q+2}, \ldots, z_p)$$ et $$\textup{La}_{s_1, \ldots, s_{q}, s_{q+2}-m, s_{q+3}, \ldots, s_p} (z_1, \ldots, z_{q}, z_{q+2}, \ldots, z_p),$$ qui sont de profondeur $p-1$ : on peut donc leur appliquer l'hypothèse de récurrence.

Reste la série sur la ligne (eq:tanguy1) : on utilise de nouveau la forme développée (eq:pszNzneq1) de $P_s(K,z)$ pour en obtenir l'expression alternative $$\begin{gathered}
\sum_{\ell=0}^s \sum_{k_1\ge \cdots \ge k_q\ge 1}
\frac{z_1^{k_1}\cdots z_q^{k_q}}{k_1^{s_1}\cdots k_q^{s_q}}
\frac{z_{q+1}^{k_q} a_{1, \ell}(s,z_{q+1})+a_{2,\ell}(s,z_{q+1})}{k_q^{-\ell}(1-z_{q+1})^{s+1}} \,
\textup{La}^{k_q}_{s_{q+2} , \dots , s_p } (z_{q+2} ,\dots ,z_p )
\\
=\frac{1}{(1-z_{q+1})^{s+1}}\sum_{\ell=0}^s \bigg(a_{1, \ell} (s,z_{q+1}) \textup{La}_{s_1, \ldots, s_{q-1},
s_{q}-\ell, s_{q+2}, \ldots, s_p}(z_1, \ldots, z_{q}z_{q+1}, z_{q+2}, \ldots, z_p)
\\
+ a_{2, \ell} (s,z_{q+1}) \textup{La}_{s_1, \ldots, s_{q-1},
s_{q}-\ell, s_{q+2}, \ldots, s_p}(z_1, \ldots, z_{q}, z_{q+2}, \ldots, z_p) \bigg).
\end{gathered}$$ Comme on a maintenant affaire à une combinaison linéaire de $\textup{La}$ de profondeur $p-1$, l'hypothèse de récurrence s'applique.

-- Le cas $q =p-1$. On a $$\begin{aligned}
\lefteqn{\textup{La}_{s_1 ,s_2 , \dots , s_p } (z_1 , z_2, \dots ,z_p ) }\nonumber
\\
&=&
\sum_{k_1\ge \cdots\ge k_{p-1}\ge 1}
\frac{z_1^{k_1}\cdots z_q^{k_{p-1}}}{k_1^{s_1}\cdots k_{p-1}^{s_{p-1}}} \,
\textup{La}^{k_{p-1}}_{-s} (z_p)\nonumber
\\
&=& \sum_{k_1\ge \cdots \ge k_{p-1}\ge 1}
\frac{z_1^{k_1}\cdots z_q^{k_q}}{k_1^{s_1}\cdots k_q^{s_q}} P_{s}(k_{p-1},z_{p})
\\
&=& \sum_{\ell=0}^s \sum_{k_1\ge \cdots \ge k_{p-1}\ge 1}
\frac{z_1^{k_1}\cdots z_q^{k_q}}{k_1^{s_1}\cdots k_q^{s_q}}
\frac{z_{p}^{k_{p-1}} a_{1, \ell}(s,z_{p})+a_{2,\ell}(s,z_{p})}{ k_q^{-\ell}(1-z_{p})^{s+1}}
\\
&=& \frac{1}{(1-z_{p})^{s+1}} \sum_{\ell=0}^s
\bigg( a_{1, \ell}(s,z_{p})\textup{La}_{s_1, \ldots, s_{p-2}, s_{p-2}-\ell}(z_1, \ldots, z_{p-2}, z_{p-1}z_p)
\\
&& \qquad +
a_{1, \ell}(s,z_{p})\textup{La}_{s_1, \ldots, s_{p-2}, s_{p-2}-\ell}(z_1, \ldots, z_{p-2}, z_{p-1})
\bigg).
\end{aligned}$$ On peut de nouveau appliquer l'hypothèse de récurrence, ce qui termine la preuve du théorème 7.

# Démonstration du théorème 3 {#sec:raffinement en z=1}

Pour démontrer le théorème 3, nous devons régulariser les polyzêtas divergents intervenant dans la décomposition d'une brique. La régularisation qui s'impose ici est la régularisation dite *shuffle* des polyzêtas basée sur l'étude du comportement asymptotique des polylogarithmes lorsque $z$ tend vers $1$.

## Régularisation $\hbox{\xrm sh}$ analytique

Dans [@ra Corollaire 2.5], Racinet caractérise, suivant les travaux de L. Boutet de Monvel, le comportement asymptotique des polylogarithmes lorsque $z$ tend vers $1$.

**Théorème 8**. *Pour tous entiers strictement positifs $s_1
,\dots ,s_p$, la fonction $\textup{Li}_{s_1 ,\dots ,s_p} (z)$ admet, lorsque $z$ tend vers $1$ tel que $\vert z\vert <1$, un développement asymptotique du type $$\textup{Li}_{s_1 ,\dots ,s_p} (z) =Q_{s_1 ,\dots ,s_p} ( \log (1-z) )+o ( (1-z)^{\varepsilon} )$$ avec $Q_{s_1 ,\dots ,s_p} \in \mathbb{C} [t ]$ et $\varepsilon \in
\mathbb{R}^*_+$.*

On note $\zeta^{\hbox{\xrm sh} } (s_1 ,\dots ,s_p )$ la valeur régularisée de $\zeta (s_1 ,\dots ,s_p )$ pour $s_1 =1$ obtenue en posant $\zeta^{\hbox{\xrm sh} } (s_1 ,\dots ,s_p ) =Q(0)$, i.e. le terme constant du polynôme $Q$. Si $s_1 \geq 2$, on a bien sûr $\zeta^{\hbox{\xrm sh} } (s_1 ,\dots ,s_p ) =\zeta (s_1 ,\dots ,s_p )$.

## Aspects effectifs

Notons que l'implémentation effective de l'algorithme de décomposition demande deux choses:

\(i\) Le calcul des $\zeta^{\hbox{\xrm sh} } (s_1 ,\dots ,s_p )$ régularisés en fonction des $\zeta$ classiques.

\(ii\) Le calcul explicite du reste intervenant dans l'estimation asymptotique du théorème 8.

Le calcul des $\zeta^{\hbox{\xrm sh} } (s_1 ,\dots ,s_p )$ dans le cas divergents peut s'effectuer de façon *combinatoire*, beaucoup plus simple que *via* le calcul effectif des développements asymptotiques du théorème 8.

## Régularisation $\hbox{\xrm sh}$ combinatoire

La régularisation $\hbox{\xrm sh}$ que nous venons de définir conserve la symétrie $\hbox{\xrm sh}$ vérifiée par les polyzêtas convergents. Soit $A=\{ \mathbf{0},\mathbf{1} \}$ un alphabet. On note $A_c$ l'ensemble des mots de $A^*$ commencant par $\mathbf{0}$ et se terminant par $\mathbf{1}$. On note $\pi$ le morphisme de $\mathbb{R} \langle A_c \rangle$ dans $\mathbb{R} \langle Y
\rangle$ défini par $\pi (\mathbf{0}^{s-1} \mathbf{1} )=y_s,$ pour tout $s\geq 1$. On note encore $\zeta$ le morphisme défini sur $A_c$ par $\zeta (\mathbf{0}^{s-1} \mathbf{1} )=
\zeta_s$. Le produit de battage ou shuffle sur $A$ se définit par récurrence sur la longueur des mots par $$a\mathbf{b}\hbox{\xrm sh} c\mathbf{d} =a (\mathbf{b}\hbox{\xrm sh} c\mathbf{d}) +c(a\mathbf{b}\hbox{\xrm sh} \mathbf{d}) ,$$ pour tout mot $\mathbf{b},\mathbf{d} \in A^*$, $a,c\in A$.

On démontre en utilisant l'écriture intégrale des polyzêtas la relation de symétrie dite *shuffle* : Pour tout $\mathbf{u} \in A_c$, $\mathbf{v}\in A_c$, on a $$\label{symetrie:shu} \zeta (\mathbf{u} )\zeta (\mathbf{v} )=\zeta
(\mathbf{u} \hbox{\xrm sh} \mathbf{v} )$$ On renvoie par exemple à l'article [@colmez] pour plus de détails.

On note $A_0$ l'ensemble des mots de $A^*$ se terminant par $\mathbf{1}$. On peut donner un sens aux polyzetas sur $A_0$ en utilisant la relation ((symetrie:shu)) en supposant que celle-ci est encore vérifiée pour tout mot de $A_0$, ce qui est le cas de la régularisation $\zeta^{\hbox{\xrm sh} }$ ci-dessus. On note encore $\zeta^{\hbox{\xrm sh} }$ le polyzeta étendu à $A_0$.

Pour tout mot $\underline{s}=s_1 \dots s_r \in A_c$, $r\geq 1$, $s_i \in
A$, on a $\mathbf{1} \hbox{\xrm sh} \mathbf{1}^{i} \underline{s}=(i+1)\mathbf{1}^{i+1} \underline{s}+\mathbf{1}^i s_1 [\mathbf{1} \hbox{\xrm sh} \underline{s}^{>1} ],$ où $\underline{s}^{>1} =s_2 \dots s_r$. En appliquant $\zeta^{\hbox{\xrm sh} }$, on obtient $$\label{recurshuffle} \zeta^{\hbox{\xrm sh} } (\mathbf{1} ) \zeta^{\hbox{\xrm sh} }
(\mathbf{1}^i \underline{s})=(i+1)\zeta^{\hbox{\xrm sh} } (\mathbf{1}^{i+1} \underline{s}) +
\zeta^{\hbox{\xrm sh} } (\mathbf{1}^i s_1 [\mathbf{1}\hbox{\xrm sh} \underline{s}^{>1} ]).$$ Il est donc possible de calculer $\zeta^{\hbox{\xrm sh} } (\mathbf{1}^{i+1}
\underline{s})$ par récurrence sur le nombre de $\mathbf{1}$. Pour cela, il suffit de fixer une valeur à $\zeta^{\hbox{\xrm sh} } (\mathbf{1} )$.

Pour obtenir une régularisation combinatoire qui coincide avec la régularisation analytique définie au paragraphe précédent, on doit poser $\zeta^{\hbox{\xrm sh} } (1) =0$. En effet, un simple calcul donne $\textup{Li}_1 (z)=-\log (1-z)$. La formule ((recurshuffle)) permet alors le calcul explicite et algorithmique des polyzêtas divergents.

## Énoncés

Dans cette partie, et dans toute la suite, on pose pour $j \in \{1, \ldots, p\}$ : $$D_j = \Big( \sum_{i=1} ^j A_i (n_i+1) \Big) - j - 1.$$

**Lemme 4**. *La série $$\sum_{k_1\ge \cdots \ge k_p\ge 1}
\frac{P(k_1,  \ldots, k_p)}{(k_1)_{n_1+1}^{A_1}
 \cdots (k_p)_{n_p+1}^{A_p}}$$ converge si, et seulement si, le polynôme $P(X_1, \ldots, X_p)$ vérifie $$\label{eqCV}
\sum_{i=1}^j \deg_{X_i}P \leq D_j \mbox{ pour tout } j \in \{1,
\ldots, p\}.$$*

**Remarque 6**. *Lorsque $n_1 = \dots = n_p =0$ et $P=1$, ce lemme donne les conditions exactes de convergence des polyzêtas $\zeta(A_1, A_2, \ldots, A_p)$ lorsque les $A_j$ sont dans $\mathbb{Z}.$ Elles correspondent bien aux conditions qui assurent la convergence absolue des polyzêtas pour des exposants *complexes*. Voir [@kratriv2 p. 10] pour une preuve de ces conditions.*

*Proof.* Pour démontrer ce lemme, on va montrer en fait que les conditions (eqCV) équivalent au fait que, pour tout $B
\geq 0$, la série $$\label{eqCVsergal}
\sum_{k_1\ge \cdots \ge k_p\ge 1} \frac{P(k_1,  \ldots, k_p) (\log
k_p)^B}{(k_1)_{n_1+1}^{A_1}
\cdots (k_p)_{n_p+1}^{A_p}}$$ converge. C'est évident pour $p=1$, puisque les conditions (eqCV) se réduisent alors à $\deg_{X_1}P \leq A_1 (n_1+1)-2$. Supposons que ce soit vrai pour $p-1$, et soit $P(X_1, \ldots, X_p)$ ; posons $\delta = \deg_{X_p} P$. Si $\delta \leq A_p (n_p+1)-1$ alors on a $$1 \ll \sum_{k_p = 1}^{k_{p-1}} \frac{k_p ^{\delta}
(\log k_p)^B}{ (k_p)_{n_p+1}^{A_p}} \ll (\log k_{p-1})^{B+\delta}$$ donc la convergence de (eqCVsergal) équivaut à celle de (eqCVsergal) en profondeur $p-1$. Comme justement l'équation correspondant à $j=p$ dans (eqCV) se déduit des autres (puisqu'on a supposé $\deg_{X_p} P \leq A_p (n_p+1)-1$), la preuve est terminée dans ce cas. Supposons maintenant que l'on ait $\delta \geq A_p (n_p+1)$. Alors on a $$k_{p-1}^{\delta - A_p (n_p+1) + 1}   \ll \sum_{k_p = 1}^{k_{p-1}}
\frac{k_p ^{\delta} (\log k_p)^B}{ (k_p)_{n_p+1}^{A_p}}
\ll k_{p-1}^{\delta - A_p (n_p+1) + 1}   (\log k_{p-1})^{B}$$ donc la convergence de (eqCVsergal) avec $P(X_1, \ldots, X_p)$ équivaut à celle de (eqCVsergal) avec un polynôme $\widetilde P(X_1, \ldots, X_{p-1})$ vérifiant $\deg_{X_i}\widetilde P= \deg_{X_i} P$ pour $i \in \{1, \ldots, p-2\}$ et $\deg_{X_{p-1}}\widetilde P= \deg_{X_{p-1}}
P + \deg_{X_p}P - A_p (n_p+1) + 1$. Or justement les conditions (eqCV) pour un tel polynôme $\widetilde P$ équivalent aux conditions (eqCV) pour $P$. Le lemme est donc démontré. ◻

On dit qu'une fonction $f$, définie sur un ouvert dont le point 1 appartient à l'adhérence, est *à divergence au plus logarithmique* en $z=1$ si elle admet un développement asymptotique de la forme $f(z) = Q( \log(1-z)) + \mathcal{O}((1-z)^\varepsilon)$ pour un certain $\varepsilon> 0$ et un polynôme $Q \in \mathbb C[t]$. La *valeur régularisée* de $f$ en 1 est le coefficient constant de $Q$, c'est-à-dire $Q(0)$. Dans le cas particulier où $f$ est définie et continue en 1, le polynôme $Q$ est constant et cette valeur régularisée est simplement $f(1)$.

**Lemme 5**. *La fonction $$\label{eqfctlog}
\sum_{k_1\ge \cdots \ge k_p\ge 1} \frac{P(k_1,  \ldots,
k_p)}{(k_1)_{n_1+1}^{A_1}
 \cdots (k_p)_{n_p+1}^{A_p}} z^{-k_1}$$ est à divergence au plus logarithmique en $z=1$ si, et seulement si, $$\label{eqdivlog}
\sum_{i=1}^j \deg_{X_i}P \leq D_j + 1 \mbox{ pour tout } j \in
\{1, \ldots, p\}.$$*

La preuve de ce lemme est analogue à celle du lemme 4 ; seule l'initialisation diffère vraiment, puisque la fonction $\sum_{k \geq 1} k^{-1} z^{-k}$ à est divergence au plus logarithmique en $z=1$.

Pour démontrer le théorème 3, on va en fait démontrer le résultat suivant qui est plus fort.

**Théorème 9**. *Si les relations (eqdivlog) sont satisfaites alors la valeur régularisée en 1 de la fonction (eqfctlog) est une combinaison linéaire à coefficients rationnels en les polyzêtas régularisés $\zeta^{\hbox{\xrm sh} } (s_1 ,\dots ,s_q )$ où $0\leq q\leq p$, $s_i \geq 1$ pour $i=1,\dots ,q$, $\sum_{j=1}^q s_j \leq \sum_{j=1}^p A_j$. En outre, on peut calculer *explicitement* une telle combinaison linéaire.*

## Preuve du théorème 9

On démontre le théorème 9 par récurrence sur la profondeur $p$. Quand $p=0$, ce théorème est trivial ; les arguments qui suivent permettent de le démontrer pour $p=1$, mais un raisonnement direct est beaucoup plus facile dans ce cas. Supposons donc que ce théorème soit vrai en toute profondeur strictement inférieure à $p$.

Soit $P(X_1, \ldots, X_p)$ un polynôme tel que les relations (eqdivlog) soient satisfaites. On pose $$R(X_1, \ldots, X_p)= \frac{P(X_1,  \ldots,
X_p)}{(X_1)_{n_1+1}^{A_1}
 \cdots (X_p)_{n_p+1}^{A_p}},$$ et on étudie la fonction $$f(z) = \sum_{k_1\ge \cdots \ge k_p\ge 1} R(k_1,  \ldots, k_p) z^{-k_1}$$ qui est définie pour $|z|  > 1$ et est à divergence au plus logarithmique en $z=1$ grâce au lemme 5. On utilise le développement en éléments simples de $R$, comme au paragraphe 4.1 (dont on reprend les notations). Ceci permet d'écrire, pour $|z| > 1$ : $$\label{eqsomtot}
f(z) = \sum_{\varpi} C[\varpi] \sum_{k_1\ge \cdots \ge k_p\ge 1}
\frac{\prod_{i \in I} k_i^{\hat s_i}}{\prod_{i \in
I^{{\rm c}}}(k_i+j_i)^{s_i}}z^{-k_1}.$$ Dans cette formule et dans toute la suite, on note $\varpi$ un quadruplet générique $$(I, (s_i)_{i \in I^{{\rm c}}}, (j_i)_{i \in I^{{\rm c}}}, (\hat s_i)_{i \in I} )$$ tel que $1 \leq s_i \leq A_i$ et $0 \leq j_i \leq n_i$ pour tout $i \in I^{{\rm c}}$, et $0 \leq \hat s_i\leq \hat A_i$ pour tout $i \in I$. On pose alors $C[\varpi] = C\left[\,{\tiny \begin{matrix} I \\ (s_i) \\ (j_i) \\ (\hat s_i) \end{matrix}} \,\right]$.

La difficulté est que ce développement en éléments simples fait apparaı̂tre des fonctions de $z$ dont la divergence en 1 n'est pas logarithmique. Par exemple, si $p=2$, $n_1 = 2$, $A_1 =
1$, $P(X_1, X_2) = (X_2)_{n_2+1}^{A_2} X_2$ alors les relations (eqdivlog) sont satisfaites mais dans l'expression (eqsomtot) apparaissent les sommes $$\sum_{k_1 \geq k_2 \geq 1} \frac{k_2}{k_1+j} z^{-k_1}$$ pour $j \in \{0,1,2\}$, qui sont chacune à divergence non logarithmique. Une méthode pour résoudre ce problème serait de généraliser le théorème 9, en autorisant des divergences non logarithmiques (c'est-à-dire des développements asymptotiques avec des termes $\frac{\log^k(z)}{(1-z)^\ell}$). Mais cela nécessiterait une généralisation du théorème 8, et ne présenterait pas d'intérêt pratique. En effet, la présence de pôles en $\frac{1}{1-z}$ nécessite de connaı̂tre aussi le coefficient de $1-z$ dans les développements asymptotiques, car leur produit contribue à la valeur en $z=1$. L'algorithme devrait donc calculer beaucoup de termes des développements asymptotiques, ce qui serait coûteux en temps et en mémoire. C'est pourquoi on procède plutôt comme suit. L'idée importante est celle de la régularisation : quand seules des divergences logarithmiques sont présentes, seul le coefficient constant du polynôme en $\log(1-z)$ intervient dans les calculs, y compris lorsqu'on doit faire des produits.

Notons ${\mathscr{E}}_0$ l'ensemble des quadruplets $\varpi= (I, (s_i)_{i
\in I^{{\rm c}}}, (j_i)_{i \in I^{{\rm c}}}, (\hat s_i)_{i \in I} )$ tels que la fonction $$\label{equnebriq}
 \sum_{k_1\ge \cdots \ge k_p\ge 1} \frac{\prod_{i \in I} k_i^{\hat s_i}}{\prod_{i \in I^{{\rm c}}}(k_i+j_i)^{s_i}}z^{-k_1}$$ soit à divergence au plus logarithmique en $z=1$, et ${\mathscr{E}}_1$ son complémentaire. Dans la somme (eqsomtot), chaque élément $\varpi\in {\mathscr{E}}_0$ donne lieu à un développement asymptotique de la forme $Q_{\varpi}(\log(1-z)) + \mathcal{O}((1-z)^\varepsilon)$ avec $\varepsilon> 0$ (qu'on peut choisir indépendant de $\varpi$) et $Q_{\varpi} \in \mathbb C[t]$. En regroupant d'autre part les contributions de tous les éléments $\varpi\in {\mathscr{E}}_1$, on a donc : $$\label{eq1235}
 \sum_{\varpi\in {\mathscr{E}}_1} C[\varpi] \sum_{k_1\ge \cdots \ge k_p\ge 1}
\frac{\prod_{i \in I} k_i^{\hat s_i}}{\prod_{i \in I^{{\rm c}}}
(k_i+j_i)^{s_i}}z^{-k_1} = f(z) -  \sum_{\varpi\in {\mathscr{E}}_0} Q_{\varpi}(\log(1-z)) + \mathcal{O}((1-z)^\varepsilon).$$ Comme $f(z)$ est à divergence au plus logarithmique, on voit que le membre de gauche aussi ; on va maintenant transformer ce membre de gauche en une somme du type (eqfctlog) en profondeur $p-1$. Soit $\varpi\in {\mathscr{E}}_1$, avec $\varpi= (I,
(s_i)_{i \in I^{{\rm c}}}, (j_i)_{i \in I^{{\rm c}}}, (\hat s_i)_{i \in I} )$. L'hypothèse (eqdivlog) (avec $j=1$) montre que l'ensemble $J$ défini au paragraphe 4.1 est inclus dans $\{2, \ldots, p \}$, donc $I$ aussi. En outre, $I$ est non vide (sinon on aurait $\varpi\in {\mathscr{E}}_0$ d'après le lemme 5). Donc il existe $t \in \{2, \ldots, p\}$ tel que $t \in I$. En notant $B_s$ le $s$-ième polynôme de Bernoulli (qui est à coefficients rationnels), on a [^7] : $$\label{eq1237}
\sum_{k_t = k_{t+1} } ^{k_{t-1}} k_t^{\hat s_t} = B_{\hat s_t}
(k_{t-1}+1) - B_{\hat s_t}(k_{t+1}).$$ Cette relation permet d'écrire, en posant $\ell_1 = k_1$, ..., $\ell_{t-1} = k_{t-1}$, $\ell_t = k_{t+1}$, $\ell_{p-1} =
k_p$ : $$\begin{gathered}
\sum_{k_1\ge \cdots \ge k_p\ge 1} \frac{\prod_{i \in I} k_i^{\hat s_i}}{\prod_{i \in I^{{\rm c}}}(k_i+j_i)^{s_i}}z^{-k_1}\\
=\sum_{\ell_1\ge \cdots \ge \ell_{p-1} \ge 1} \frac{
\displaystyle{\prod_{\tiny {\begin{array}{c} i \in I \\ i \leq t-1 \end{array}}} \ell_i^{\hat s_i}
\prod_{\tiny {\begin{array}{c} i \in I \\ i \geq t+1 \end{array}}} \ell_{i-1}^{\hat s_i} } }{
\displaystyle{\prod_{\tiny {\begin{array}{c} i \in I^{{\rm c}} \\ i \leq
t-1 \end{array}}}(\ell_i+j_i)^{s_i} \prod_{\tiny {\begin{array}{c} i \in I^{{\rm c}} \\ i \geq
t+1 \end{array}}}(\ell_{i-1}+j_i)^{s_i}}
 } \times \Big(  B_{\hat s_t} (\ell_{t-1}+1) - B_{\hat s_t}(\ell_t) \Big)  z^{-\ell_1} .

\end{gathered}$$ Cette somme est de la forme $$\sum_{\ell_1\ge \cdots \ge \ell_{p-1} \ge 1} R_{\varpi} (\ell_1, \ldots, \ell_{p-1}) z^{-\ell_1}$$ pour une certaine fraction rationnelle $R_{\varpi}$ (qui dépend aussi du choix, arbitraire et fixé, de $t$). Le membre de gauche de (eq1235) s'écrit donc $$\label{eq1236}
\sum_{\ell_1\ge \cdots \ge \ell_{p-1} \ge 1} \widetilde R(\ell_1,
\ldots, \ell_{p-1}) z^{-\ell_1},$$ où l'on a posé $$\widetilde R(\ell_1, \ldots, \ell_{p-1}) =  \sum_{\varpi\in {\mathscr{E}}_1} C[\varpi]  R_{\varpi} (\ell_1, \ldots, \ell_{p-1}).$$ La relation (eq1235) et le lemme 5 montrent que cette fraction rationnelle $\widetilde R(\ell_1, \ldots,
\ell_{p-1})$ satisfait aux hypothèses du théorème 9, en profondeur $p-1$. Par hypothèse de récurrence, on peut donc écrire (eq1236) sous la forme $\widetilde Q(\log(1-z)) + \mathcal{O}((1-z)^\varepsilon)$, où $\widetilde Q(0)$ est une combinaison linéaire explicite à coefficients rationnels en les polyzêtas régularisés $\zeta^{\hbox{\xrm sh} } (s_1 ,\dots ,s_q
)$ où $1\leq q\leq p-1$, $\sum_{j=1}^q s_j \leq \sum_{j=1}^p A_j$. Compte tenu de (eq1235), il suffit maintenant de calculer $Q_{\varpi}(0)$ pour $\varpi\in {\mathscr{E}}_0$, et la preuve du théorème 9 sera terminée.

Pour cela, on décompose la somme (equnebriq). Tout d'abord, si $I$ est non vide alors on applique la relation (eq1237) comme ci-dessus, et on est ramené à une profondeur strictement inférieure. On peut donc supposer que $I$ est vide. Il suffit alors de suivre la preuve du théorème 1 (voir le paragraphe 4) avec $z_1 = z$, $z_2 =
\ldots = z_p = 1$, puis d'appliquer le théorème 9 en profondeur $\leq p-1$. Ceci termine la preuve du théorème 9.

1 S. Akiyama, S. Egami et Y. Tanigawa, *Analytic continuation of multiple zeta-functions and their values at non-positive integers*, Acta Arith. **98** (2001), 107--116.

S. Akiyama et Y. Tanigawa, *Multiple zeta values at non-positive integers*, The Ramanujan Journal, vol. 5, no.4 (2001) 327-351.

R. Apéry, *Irrationalité de $\zeta(2)$ et $\zeta(3)$*, Astérisque **61** (1979), 11--13.

W. N. Bailey, *Generalized hypergeometric series*, Cambridge University Press, Cambridge, 1935.

K. Ball et T. Rivoal, *Irrationalité d'une infinité de valeurs de la fonction zêta aux entiers impairs*, Invent. Math. **146**.1 (2001), 193--207.

F. Beukers, *A note on the irrationality of $\zeta(2)$ and $\zeta(3)$*, Bull. London Math. Soc. **11** (1979), 268--272.

F. C.S. Brown, *Périodes des espaces des modules $\overline{\mathscr M}\sb {0,n}$ et multizêtas*, C. R. Acad. Sci. Paris, Ser. I **336** (2006).

P. Cartier, *Fonctions polylogarithmes, nombres polyzêtas et groupes pro-unipotents*, Séminaire Bourbaki, Vol. 2000/2001, Astérisque **282** (2002), exposé No. 885, 137--173.

P. Colmez, *Arithmétique de la fonction zêta*, Éd. École Polytechnique, 2003.

J. Cresson, *Calcul Moulien*, Prépublication de l'I.H.E.S. 06/22 (2006), 93 pages.

J. Cresson, S. Fischler et T. Rivoal, *Phénomènes de symétrie dans des formes linéaires en polyzêtas*, Prépublication de l'I.H.E.S. M/06/37, Juin 2006.

J. Cresson, S. Fischler et T. Rivoal, Code en GP-Pari de l'implémentation de l'algorithme décrit dans *Séries hypergéométriques multiples et polyzêtas*, disponible sur

`http://www.math.u-psud.fr/~fischler/algo.html`

J. Écalle, *ARI/GARI, la dimorphie et l'arithmétique des multizêtas: un premier bilan*, J. Théor. Nombres Bordeaux **15** (2003), 411--478.

O. Espinosa et V. H. Moll, *The evaluation of Tornheim double sums. I.*, J. Number Theory **116** (2006), , 200--229.

S. Fischler, *Groupes de Rhin-Viola et intégrales multiples*, J. Théor. Nombres Bordeaux **15** (2003), , 479--534.

S. Fischler, *Irrationalité de valeurs de zêta (d'après Apéry, Rivoal, \...)*, Séminaire Bourbaki, Vol. 2002/2003, Astérisque **294** (2004), exposé No. 910, 27--62.

S. Fischler, *Multiple series connected to Hoffman's conjecture on multiple zeta values*, en préparation.

S. Fischler et T. Rivoal, *Approximants de Padé et séries hypergéométriques équilibrées*, J. Math. Pures Appl. **82**.10 (2003), 1369--1394.

A. B. Goncharov, *Multiple polylogarithms and mixed Tate motives*, 2001, prépublication disponible l'ArXiv : `http://front.math.ucdavis.edu/math.AG/0103059`

A. B. Goncharov et Yu. I. Manin, *Multiple $\zeta$-motives and moduli spaces $\overline{\mathscr M}\sb {0,n}$*, Compos. Math. **140** (2004), , 1--14.

M. Hata, *A note on Beukers' integral*, J. Austral. Math. Soc. Ser. A **58** (1995), , 143--153.

M. Hata, *A new irrationality measure for $\zeta(3)$*, Acta Arith. **92** (2000), , 47--57.

C. Krattenthaler et T. Rivoal, *Hypergéométrie et fonction zêta de Riemann*, à paraı̂tre aux Memoirs of the AMS (2006), 93 pages.

C. Krattenthaler et T. Rivoal, *An identity of Andrews, multiple integrals, and very-well-poised hypergeometric series*, à paraı̂tre au Ramanujan J. (2006), 16 pages.

L. Lewin, *Polylogarithms and associated functions*, North-Holland Publishing Co., New York-Amsterdam, 1981.

Yu. V. Nesterenko, *A few remarks on $\zeta(3)$* (en russe), Mat. Zametki **59**.6 (1996), 865--880; traduction en anglais dans Math. Notes **59**.6 (1996), 625--636.

Hoang Ngoc Minh, M. Petitot et J. Van Der Hoeven, *Shuffle algebra and polylogarithms*, Discrete Math. **225** (2000), 217--230.

G. Racinet, *Série génératrices non-commutatives de polyzêtas et associateurs de Drinfeld*, Thèse de doctorat, Université d'Amiens, 2000.

G. Racinet, *Doubles mélanges des polylogarithmes multiples aux racines de l'unité*, Publ. Math. Inst. Hautes Études Sci., **95** (2002), 185--231.

C. Reutenauer, *Free lie algebras*, London Math. Soc. Monographs, new series 7, 1993.

G. Rhin et C. Viola, *On a permutation group related to $\zeta(2)$*, Acta Arith. **77** (1996), 23--56.

G. Rhin et C. Viola, *The group structure for $\zeta(3)$*, Acta Arith. **97**.3 (2001), 269--293.

T. Rivoal, *La fonction zêta de Riemann prend une infinité de valeurs irrationnelles aux entiers impairs*, C. R. Acad. Sci. Paris, Série I Math. **331**.4 (2000), 267--270.

L. J. Slater, *Generalized hypergeometric functions*, Cambridge University Press, Cambridge, 1966.

V. N. Sorokin, *On the measure of transcendency of the number $\pi\sp 2$*, en russe, Mat. Sb. **187** (1996), , 87--120 ; traduction en anglais dans Sb. Math. **187** (1996), , 1819--1852.

V. N. Sorokin, *Apéry's theorem*, Vestnik Moskov. Univ. Ser. I Mat. Mekh. no. 3 (1998), 48--52; traduction en anglais dans Moscow Univ. Math. Bull. no. 3 (1998), 48--52.

V. N. Sorokin, *On the linear independence of values of generalized polylogarithms*, en russe, Mat. Sb. **192** (2001), , 139--154 ; traduction en anglais dans Sb. Math. **192** (2001), -8, 1225--1239.

H. M. Srivastava et P. W. Karlsson, *Multiple Gaussian hypergeometric series*, Ellis Horwood Series: Mathematics and its Applications, New York, 1985.

T. Terasoma, *Mixed Tate motives and multiple zeta values*, Invent. Math. **149**.2 (2002), 339--369.

E. A. Ulanskiı̆, *Identities for generalized polylogarithms* (en russe), Mat. Zametki **73**.4 (2003), 613--624 ; traduction en anglais dans Math. Notes **73** (2003), no. 3-4, 571--581.

D. V. Vasilyev, *Approximations of zero by linear forms in values of the Riemann zeta-function*, Doklady Nat. Acad. Sci Belarus **45**.5 (2001), 36--40 (en russe). Version étendue en anglais : *On small linear forms for the values of the Riemann zeta-function at odd points*, prépublication no.1 (558), Nat. Acad. Sci. Belarus, Institute Math., Minsk (2001), 14 pages.

M. Waldschmidt, *Valeurs zêtas multiples. Une introduction*, J. Théor. Nombres Bordeaux **12** (2000), 581--595.

M. Waldschmidt, *Twisted Hoffman algebras*, Report 12/2003, Colloque Elementare und analytische Zahlentheorie, Oberwolfach, 2003.

D. Zagier, *Values of zeta functions and their applications*, First European Congress of Mathematics, Vol. II (Paris, 1992), 497--512, Progr. Math., 120, BirkhÃ'user, Basel, 1994

S. Zlobin, *Integrals that can presented as linear forms in generalized polylogarithms* (en russe), Mat. Zametki **71**.5 (2002), 782--787 ; traduction en anglais dans Math. Notes 71 (2002), no. 5-6, 711--716.

S. Zlobin, *Properties of coefficients of certain linear forms in generalized polylogarithms*, *Fundamentalnaya i Prikladnaya Matematika \[Fundamental and Applied Mathemetics\]* **11** (2005), no. 6, p. 41--58, Disponible sur ArXiv : `http://front.math.ucdavis.edu/math.NT/0511245`.

S. Zlobin, *Expansion of multiple integrals in linear forms*, Mat. Zametki **77**.5 (2005), 683--706 ; traduction en anglais dans Math. Notes 77 (2005), no. 5, 630--652.

W. Zudilin, *Well-poised hypergeometric service for Diophantine problems of zeta values*, J. Théor. Nombres Bordeaux **15** (2003), , 593--626.

W. Zudilin, *Arithmetic of linear forms involving odd zeta values*, J. Théor. Nombres Bordeaux **16** (2004), 251--291.

J. Cresson, Laboratoire de Mathématiques appliquées de Pau, Bâtiment I.P.R.A, Université de Pau et des Pays de l'Adour, avenue de l'Université, BP 1155, 64013 Pau cedex, France.

S. Fischler, Équipe d'Arithmétique et de Géométrie Algébrique, Université Paris-Sud, Bâtiment 425, 91405 Orsay Cedex, France.

T. Rivoal, Institut Fourier, CNRS UMR 5582, Université Grenoble 1, 100 rue des Maths, BP 74, 38402 Saint-Martin d'Hères cedex, France.

[^1]: du moins, dans le cas de (i) et (ii) ; le point (iii) nécessite une idée *a priori* différente (série dérivée) mais on peut l'intégrer dans le cadre fourni par (eq:serie simple generale). Voir un peu plus loin dans cette Introduction pour plus de détails.

[^2]: Par exemple, la minoration de la dimension de l'espace des nombres $\zeta(2n+1)$ devient sans intérêt lorsque l'on rajoute les nombres $\zeta(2n)$ : la transcendance de $\pi$ implique leur indépendance linéaire sur $\mathbb{Q}$ et donc une minoration de dimension de l'ordre de $A/2$ au lieu de $\log(A).$

[^3]: Voir le paragraphe 3.1 pour l'origine de cette dénomination.

[^4]: Les trois premiers exemples numériques précédant le théorème 4 suggèrent que, pour $p=2$, on a parfois des zêtas simples jusqu'à $2A-3$ et des zêtas doubles avec $3\le s<s'\le A-2$ seulement. Nous n'avons pas cherché à savoir sous quelles conditions cela est vrai.

[^5]: C'est essentiellement la seule dont on dispose : toutes les autres approches connues produisent les mêmes formes linéaires (voir [@fi]).

[^6]: Dans un contexte voisin, Zudilin [@zud] a introduit une notion de *brique*, reprise et généralisée dans [@kratriv]. Ces briques n'ont rien à voir avec les nôtres ; elles sont suffisamment différentes pour ne pas les confondre si on est amené à manipuler les deux types de briques simultanément.

[^7]: On peut noter que l'on utilise les mêmes idées que celles du paragraphe 6 sur le non-enrichissement des $\textup{La}$ à exposants négatifs. En particulier, (eq1237) est l'analogue de (eq:pszNzneq1) lorsque tous les $z_j$ valent 1.
