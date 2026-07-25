---
title: "Irrationalité de valeurs de zêta (d'après Apéry, Rivoal, ...)"
authors:
  - "Stéphane Fischler"
arxiv_id: "math/0303066v1"
arxiv_url: "https://arxiv.org/abs/math/0303066"
published: "2003-03-05"
journal_ref: "Séminaire Bourbaki 2002-2003 exposé no. 910 (Nov. 2002); Astérisque 294 (2004), 27-62"
doi: ""
source: "papers/05-fischler-2003-bourbaki-survey/exposearxiv.tex"
conversion: pandoc-flat
---

# Irrationalité de valeurs de zêta (d'après Apéry, Rivoal, ...)

**Stéphane Fischler** — Séminaire Bourbaki 2002-2003 exposé no. 910 (Nov. 2002); Astérisque 294 (2004), 27-62

## Abstract

This survey text deals with irrationality, and linear independence over the rationals, of values at positive odd integers of Riemann zeta function. The first section gives all known proofs (and connections between them) of Apéry's Theorem (1978) : $ζ(3)$ is irrational. The second section is devoted to a variant of the proof, published by Rivoal and Ball-Rivoal, that infinitely many $ζ(2n+1)$ are irrational. The end of this text deals with more quantitative statements.

---
Cet exposé est consacré aux valeurs aux entiers $s \geq 2$ de la fonction zêta de Riemann, définie par $\zeta(s) = \sum_{n=1} ^\infty
n^{-s}$. Quand $s = 2k$ est pair, on sait que $\zeta(2k) \pi^{-2k}$ est un nombre rationnel, lié aux nombres de Bernoulli. Comme $\pi$ est transcendant (voir l'appendice de [@Lang] pour une preuve), $\zeta(2k)$ l'est aussi pour tout $k \geq 1$. La nature arithmétique des $\zeta(2k+1)$ est beaucoup moins bien connue. D'un point de vue conjectural, la situation est simple :

** 1**. *Les nombres $\pi$, $\zeta(3)$, $\zeta(5)$, $\zeta(7)$, ...sont algébriquement indépendants sur $\mathbb{Q}$.*

Cette conjecture est un cas particulier d'une conjecture diophantienne sur les polyzêtas (voir [@MiW] ou [@CartierMZV]). Elle implique que les $\zeta(2k+1)$ sont tous transcendants, donc irrationnels, et linéairement indépendants sur $\mathbb{Q}$.

Très peu de résultats sont connus en direction de la conjecture 1. Le premier d'entre eux a été annoncé par Apéry lors des Journées Arithmétiques de Luminy, en 1978 :

** 2** ([@Apery]). *$\zeta(3)$ est irrationnel.*

Apéry lui-même n'a donné lors de son exposé (voir [@MendesFrance]), et n'a publié [@Apery], qu'une esquisse de sa preuve. Les détails (qui sont loin d'être triviaux) ont été publiés par Van Der Poorten [@VDP] (voir aussi [@CohenGrenoble] et [@Reyssat]), grâce à des contributions de Cohen et Zagier. Par la suite, plusieurs autres démonstrations du théorème d'Apéry sont parues. La première partie de ce texte est consacrée à une synthèse des différents points de vue qu'on peut adopter pour le démontrer.

La grande percée suivante date de 2000 :

** 3** ([@RivoalCRAS], [@BR]). *Le $\mathbb{Q}$-espace vectoriel engendré par $1$, $\zeta(3)$, $\zeta(5)$, $\zeta(7)$, ...est de dimension infinie.*

En conséquence, il existe une infinité de $k$ tels que $\zeta(2k+1)$ soit irrationnel. On peut donner des versions effectives de ce dernier énoncé : Rivoal a démontré [@vingtetun] que parmi les neuf nombres $\zeta(5)$, $\zeta(7)$, ..., $\zeta(21)$, l'un au moins est irrationnel. Ce résultat a été amélioré par Zudilin :

** 4** ([@Zudilinonze], [@Zudilincinqaout]). *L'un au moins des quatre nombres $\zeta(5)$, $\zeta(7)$, $\zeta(9)$, $\zeta(11)$ est irrationnel.*

Malgré ces développements récents, il n'existe aucun entier $s \geq 5$ impair pour lequel on sache si $\zeta(s)$ est rationnel ou non.

Ce texte est divisé en trois parties. La première est une synthèse des méthodes connues pour démontrer l'irrationalité de $\zeta(3)$ ; l'intérêt des différentes approches est qu'elles se généralisent plus ou moins facilement à d'autres situations. La deuxième partie fournit une preuve du théorème 3, et de résultats voisins. La troisième est consacrée à des résultats "quantitatifs" : mesure d'irrationalité de $\zeta(3)$ et théorème 4.

[Remerciements :] Je remercie toutes les personnes qui m'ont aidé dans la préparation de ce texte, notamment F. Amoroso, V. Bosser, N. Brisebarre, P. Cartier, G. Christol, P. Colmez, P. Grinspan, L. Habsieger, M. Huttner, C. Krattenthaler, C. Maclean, F. Martin, Yu. Nesterenko, F. Pellarin, A. Pulita, E. Royer, M. Waldschmidt, D. Zagier et W. Zudilin. Je remercie tout particulièrement T. Rivoal pour les nombreuses discussions très instructives que nous avons eues.

# Irrationalité de $\zeta(3)$

Toutes les preuves connues de l'irrationalité de $\zeta(3)$ ont la même structure. On construit, pour tout $n \geq 0$, des nombres rationnels $u_n$ et $v_n$ ayant les propriétés suivantes :

1.  []{#pointun label="pointun"} La forme linéaire $I_n = u_n \zeta(3) - v_n$ vérifie $$\limsup_{n \to \infty} \vert I_n \vert^{1/n} \leq
    (\sqrt{2}-1)^4 = 0,0294372\ldots$$

2.  []{#pointdeux label="pointdeux"} En notant $d_n$ le p.p.c.m. des entiers compris entre 1 et $n$, les coefficients $u_n$ et $v_n$ vérifient : $$u_n \in \mathbb{Z}\mbox{ et } 2 d_n ^3 v_n \in \mathbb{Z}.$$

3.  []{#pointtrois label="pointtrois"} Pour une infinité d'entiers $n$, on a $I_n \neq 0$.

La conclusion est alors immédiate : si $\zeta(3)$ était un nombre rationnel $p/q$, alors $2q d_n ^3 I_n$ serait un entier pour tout $n$, et tendrait vers zéro quand $n$ tend vers l'infini (car $(\sqrt{2}-1)^4 e^3 < 1$, en utilisant [@Ingham] le théorème des nombres premiers sous la forme $\lim_{n \to
\infty} \frac{\log(d_n)}{n} = 1$) : cela contredit la troisième assertion.

** 5**. *Comme $(\sqrt{2}-1)^4 \cdot 3,23^3 < 1$, le théorème des nombres premiers peut être remplacé par l'assertion plus faible $d_n < 3,23 ^n$ pour $n$ assez grand, qui se démontre en utilisant des arguments élémentaires à la Tchebychev ([@Niven], §8.1 ; [@Ingham], p. 15).*

Dans la suite, on donne plusieurs constructions (§ 1.1 à 1.10) de $u_n$, $v_n$ et $I_n$, à chaque fois notées $u_{i,n}$, $v_{i,n}$ et $I_{i,n}$ (l'indice $i \in \{{\rm R}, {\rm E}, \mathbb{R}, \Sigma,\mathbb{C},{\rm P},
                    {\rm TB},{\rm M} \}$ fait référence à la construction utilisée). En fait, on construit toujours les mêmes formes linéaires : *a posteriori* on s'aperçoit que $u_{i,n}$, $v_{i,n}$ et $I_{i,n}$ ne dépendent pas de $i$. La preuve de cette indépendance est le plus souvent directe. Parfois, on montre simplement que $I_{i,n}= I_{j,n}$ ; les deux autres égalités en découlent en utilisant l'irrationalité de $\zeta(3)$.

Les premières valeurs de $u_n$ et $v_n$ sont : $$\begin{aligned}
(u_n)_{n \geq 0} &=& 1, 5, 73, 1445, 33001, 819005, \ldots \\
(v_n)_{n \geq 0} &=& 0, 6, \frac{351}{4}, \frac{62531}{36},
                \frac{11424695}{288}, \ldots
\end{aligned}$$

Cette partie contient l'esquisse de plusieurs preuves de l'irrationalité de $\zeta(3)$, notamment celles d'Apéry [@Apery] (§1.1 et 1.2), de Beukers [@Beukers] par les intégrales multiples (§1.3) ou [@BeukersBesancon] par les formes modulaires (§1.10), de Prevost [@Prevost] (§1.1 et 1.2), de Nesterenko [@Nesterenko96] (§1.4 et 1.5), de Sorokin [@SorokinApery] (§1.8), et de nombreuses variantes. Certaines preuves sont obtenues en montrant que deux constructions différentes fournissent les mêmes formes linéaires, puis en prouvant le point (pointdeux) à l'aide de l'une et les points (pointun) et (pointtrois) à l'aide de l'autre (par exemple en montrant que $\lim_{n \to \infty} \vert I_n \vert ^{1/n} =
(\sqrt{2}-1)^4$).

La plupart des méthodes connues pour démontrer des résultats d'irrationalité sur les valeurs de $\zeta$ sont liées aux polylogarithmes, définis pour tout entier $k \geq 1$ par : $${\rm Li}_k (z ) = \sum_{n=1} ^\infty \frac{z^n}{n^k},$$ avec $\vert z \vert < 1$ si $k = 1$ et $\vert z \vert \leq 1$ si $k \geq 2$. L'idée est de construire des formes linéaires en polylogarithmes, à coefficients polynomiaux, puis de spécialiser en $z=1$. C'est la méthode employée dans les paragraphes 1.3 à 1.9. Les formes linéaires en polylogarithmes $I_{i,n}(z)$ qu'on utilise ne sont pas toujours les mêmes, mais elles coı̈ncident en $z=1$, pour donner les formes linéaires d'Apéry.

Les polylogarithmes s'insèrent dans la famille des séries hypergéométriques $_{q+1}F_q$ (avec $q \geq 1$), définies par : $$\begin{aligned}
{}_{q+1}F_q
\left(
\begin{array}{cccc}
\alpha_0,&\alpha_1,&\ldots,&\alpha_{q}\\
& \beta_1,&\ldots,&\beta_q\\
\end{array}
\bigg\arrowvert z \right)=\sum_{k=0}^{\infty}
\frac{(\alpha_0)_k(\alpha_1)_k\cdots(\alpha_{q})_k}
{k! \, (\beta_1)_k\cdots(\beta_q)_k} z^k\;,
\label{eq:hyper}
\end{aligned}$$ où le symbole de Pochhammer est $(\alpha)_k=\alpha(\alpha+1)\cdots(\alpha+k-1)$. Dans cet exposé, les $\alpha_j$ et les $\beta_j$ seront des entiers, les $\beta_j$ étant positifs, et $z$ sera un nombre complexe avec $\vert z \vert \leq 1$. On adopte les définitions suivantes ([@AAR], §3.3 et 3.4) :

-   ${}_{q+1}F_q$ est dite *bien équilibrée* si $\alpha_0+1=\alpha_1+\beta_1=\cdots=\alpha_{q}+\beta_q$ ;

-   ${}_{q+1}F_q$ est dite *très bien équilibrée* si elle est bien équilibrée et $\alpha_1=\frac12\alpha_0+1$.

## Récurrence linéaire

** 6**. *Soient $(u_{{\rm R}, n})_{n \geq 0}$ et $(v_{{\rm R}, n})_{n \geq 0}$ les suites définies par la relation de récurrence $$\label{relnrec}
(n+1)^3 y_{n+1} - (34 n^3 + 51 n^2 + 27 n +5) y_n + n^3 y_{n-1} = 0$$ et les conditions initiales $$u_{{\rm R}, 0}= 1 \mbox{ , } u_{{\rm R}, 1}= 5  \mbox{ , } v_{{\rm R}, 0}= 0 \mbox{ , }
v_{{\rm R}, 1}= 6.$$*

Une récurrence immédiate montre que les suites $(u_{{\rm R}, n})$ et $(v_{{\rm R}, n})$ sont croissantes et à termes rationnels, avec $n!^3 u_{{\rm R}, n}\in \mathbb{Z}$ et $n!^3 v_{{\rm R}, n}\in \mathbb{Z}$. En fait on verra qu'on peut remplacer $n!^3$ par $d_n ^3$.

Les propriétés asymptotiques des suites vérifiant la récurrence (relnrec) sont faciles à déterminer (voir par exemple [@Gelfond], Chapitre 5). L'équation caractéristique associée est $X^2 - 34 X + 1$ ; elle a deux racines simples, $(\sqrt{2}+1)^4$ et $(\sqrt{2}-1)^4$. L'espace vectoriel des solutions de (relnrec) est de dimension deux, et admet une base formée de suites $(y_n ^{(0)})_{n \geq 0}$ et $(y_n ^{(1)})_{n \geq 0}$ avec $\lim_{n \rightarrow + \infty} \frac{\log \vert y_n ^{(0)} \vert}{n}
 = \log((\sqrt{2}+1)^4)$ et $\lim_{n \rightarrow + \infty} \frac{\log \vert y_n ^{(1)} \vert}{n}
 = \log((\sqrt{2}-1)^4)$. La suite $(y_n ^{(1)})$ est uniquement déterminée (à proportionnalité près) par son comportement asymptotique  ; toutes les autres solutions de (relnrec) se comportent comme $(y_n ^{(0)})$. Comme $(u_{{\rm R}, n})$ et $(v_{{\rm R}, n})$ sont croissantes, on a : $$\label{asyunvnrec}
\lim_{n \to \infty} u_{{\rm R}, n}^{1/n} =
\lim_{n \to \infty} v_{{\rm R}, n}^{1/n} =
(\sqrt{2}+1)^4 = 33,9705627\ldots$$ Quand on adopte ce point de vue, on a intérêt [@VDP] à considérer $\Delta_n =  \begin{array}{|cc|} v_{{\rm R}, n}& v_{{\rm R}, n-1}\\ u_{{\rm R}, n}& u_{{\rm R}, n-1}
\end{array}$ pour $n \geq 1$. La relation de récurrence montre qu'on a $\Delta_n  = \frac{6}{n^3}$ pour tout $n$, ce qui signifie $\frac{v_{{\rm R}, n}}{u_{{\rm R}, n}} - \frac{v_{{\rm R}, n-1}}{u_{{\rm R}, n-1}} = \frac{6}{n^3 u_{{\rm R}, n}
u_{{\rm R}, n-1}}$. Donc la suite $(\frac{v_{{\rm R}, n}}{u_{{\rm R}, n}})$ est strictement croissante et tend vers une limite finie $\ell$, avec $u_{{\rm R}, n}\ell - v_{{\rm R}, n}= \sum_{k = n+1} ^\infty \frac{6 u_{{\rm R}, n}}{k^3
u_{{\rm R}, k}u_{{\rm R}, k-1}}$. Ceci prouve que

$u_{{\rm R}, n}\ell - v_{{\rm R}, n}$ est une solution de (relnrec) qui tend vers zéro quand $n$ tend vers l'infini : son comportement asymptotique est nécessairement donné par $$\lim_{n \rightarrow +\infty} \frac{\log \vert u_{{\rm R}, n}\ell - v_{{\rm R}, n}\vert}{n}
 = \log((\sqrt{2} - 1)^4).$$

Avec cette définition de $u_{{\rm R}, n}$ et $v_{{\rm R}, n}$, il n'est pas évident de démontrer que $\ell = \zeta(3)$, et de borner par $d_n^3$ les dénominateurs de $u_{{\rm R}, n}$ et $v_{{\rm R}, n}$. Pour ceci, une possibilité est de faire le lien avec le paragraphe 1.2 : c'est la méthode employée dans les premières preuves détaillées de l'irrationalité de $\zeta(3)$, qui sont parues peu après l'exposé d'Apéry ([@Reyssat], [@VDP], [@CohenGrenoble]).

** 7**. *Le raisonnement ci-dessus montre que $\frac{v_{{\rm R}, n}}{u_{{\rm R}, n}}$ est la $n$-ième somme partielle de la série $\zeta(3) = \sum_{k= 1}^{\infty} \frac{6}{k^3
u_{{\rm R}, k}u_{{\rm R}, k-1}}$.*

La définition 6 s'interprète en termes de fractions continues généralisées. En effet, considérons la récurrence linéaire $$\label{relnrecgdy}
Y_{n+1} - (34 n^3 + 51 n^2 + 27 n +5) Y_n + n^6 Y_{n-1} = 0.$$ On passe d'une solution de (relnrec) à une solution de (relnrecgdy), et réciproquement, en posant $Y_n = n!^3 y_n$. Si $U_{{\rm R}, n}$ et $V_{{\rm R}, n}$ sont ainsi associées à $u_{{\rm R}, n}$ et $v_{{\rm R}, n}$, alors $\frac{V_{{\rm R}, n}}{U_{{\rm R}, n}} = \frac{v_{{\rm R}, n}}{u_{{\rm R}, n}}$ est la $n$-ième réduite de la fraction continue généralisée $$\zeta(3)=
 \vcenter{\tabskip 0pt\offinterlineskip\halign{
 \strut##&\hfill\hskip 1pt##\hskip 1pt\hfill&##\cr
 &$6 \,$&\vrule\cr\noalign{\hrule}\vrule&$\, 5$&\cr}}
-
 \vcenter{\tabskip 0pt\offinterlineskip\halign{
 \strut##&\hfill\hskip 1pt##\hskip 1pt\hfill&##\cr
 &$1$&\vrule\cr\noalign{\hrule}\vrule&$117$&\cr}}
-
 \vcenter{\tabskip 0pt\offinterlineskip\halign{
 \strut##&\hfill\hskip 1pt##\hskip 1pt\hfill&##\cr
 &$64$&\vrule\cr\noalign{\hrule}\vrule&$\, 535$&\cr}}
-\cdots
-
 \vcenter{\tabskip 0pt\offinterlineskip\halign{
 \strut##&\hfill\hskip 1pt##\hskip 1pt\hfill&##\cr
 &$n^6$&\vrule\cr\noalign{\hrule}\vrule&$\, 34n^3+51n^2+27n+5$&\cr}}
-\cdots.$$ On peut trouver cette formule grâce à un procédé général ([@AperyBNF], [@BatutOlivier], [@Zeilbergerdeconstruction]) qui accélère la convergence d'un développement en fraction continue généralisée. Ce procédé s'applique, en particulier, au développement dont les réduites sont les sommes partielles de la série $\sum_{n=1} ^\infty
\frac{1}{f(n)}$, où $f$ est un polynôme sans zéro parmi les entiers strictement positifs.

En utilisant cette méthode d'accélération de convergence, André-Jeannin a démontré [@AndreJeannin] que la somme des inverses des nombres de Fibonacci est irrationnelle (voir aussi [@BundschuhVaananen] et [@PrevostFibonacci]).

## Formules explicites

** 8**. *Soient $(u_{{\rm E},n})$ et $(v_{{\rm E},n})$ les suites définies par les formules suivantes : $$\begin{aligned}
u_{{\rm E},n}&=& \sum_{k=0} ^n \binom{n}{k}^2 \binom{n+k}{k}^2 \\

v_{{\rm E},n}&=& \sum_{k=0} ^n  \binom{n}{k}^2 \binom{n+k}{k}^2
\left( \sum_{m=1} ^n \frac{1}{m^3} + \sum_{m=1} ^k
\frac{(-1)^{m-1}}{2 m^3 \binom{n}{m} \binom{n+m}{m}} \right)
\end{aligned}$$*

Sous cette forme, il est clair que $u_{{\rm E},n}\in \mathbb{Z}$ et que $\frac{v_{{\rm E},n}}{u_{{\rm E},n}}$ tend vers $\zeta(3)$. Pour démontrer ([@VDP], [@CohenGrenoble], [@Reyssat]) que $2 d_n ^3 v_{{\rm E},n}\in \mathbb{Z}$, il suffit de démontrer que, pour $1 \leq m \leq k \leq n$, $$\label{quotiententier}
\frac{\binom{n+k}{k} d_n ^3}{m^3 \binom{n}{m} \binom{n+m}{m}}
 = \frac{\binom{n+k}{k-m} d_n ^3}{m^3 \binom{n}{m} \binom{k}{m}}$$ est entier. Soit $p$ un nombre premier ; la valuation $p$-adique ${\rm v}_p(n!)$ de $n!$ vaut $\sum_{i=1} ^\alpha
[\frac{n}{p^i}]$ avec $\alpha= [ \frac{\log(n)}{\log(p)}]
 = {\rm v}_p(d_n)$. Pour $1 \leq i \leq {\rm v}_p(m)$ on a $[\frac{n}{p^i}] = [\frac{n-m}{p^i}] + [\frac{m}{p^i}]$ et pour ${\rm v}_p(m) < i \leq {\rm v}_p(d_n)$ on a $[\frac{n}{p^i}] \leq [\frac{n-m}{p^i}] + [\frac{m}{p^i}] +1$. On en déduit ${\rm v}_p(\binom{n}{m}) \leq {\rm v}_p(d_n) - {\rm v}_p(m)$ et ${\rm v}_p(\binom{k}{m}) \leq {\rm v}_p(d_k) - {\rm v}_p(m)$. Il en résulte que $\frac{d_n ^3}{m^3 \binom{n}{m} \binom{k}{m}}$ est un entier, et le quotient (quotiententier) aussi.

Montrons maintenant ([@VDP], [@CohenGrenoble]) que les suites $(u_{{\rm E},n})$ et $(v_{{\rm E},n})$ vérifient la récurrence (relnrec). On pose $\lambda_{n,k}= \binom{n}{k}^2 \binom{n+k}{k}^2$ pour $k,n \in \mathbb{Z}$, et $${\bf A}_{n,k}=4(2n+1)(k(2k+1)-(2n+1)^2) \lambda_{n,k},$$ avec les conventions habituelles (i.e. $\lambda_{n,k}=0$ si $k < 0$ ou $k >n$). On a alors $${\bf A}_{n,k} - {\bf A}_{n,k-1} =
(n+1)^3 \lambda_{n+1,k}- (34 n^3 + 51 n^2 + 27 n +5)
 \lambda_{n,k}  + n^3 \lambda_{n-1,k}.$$ En sommant sur $k$, on obtient que la suite $(u_{{\rm E},n})$ satisfait à la récurrence (relnrec). Pour la suite $(v_{{\rm E},n})$, on peut faire de même en utilisant la suite double $${\bf B}_{n,k} = {\bf A}_{n,k} \left( \sum_{m=1} ^n \frac{1}{m^3} + \sum_{m=1} ^k
\frac{(-1)^{m-1}}{2 m^3 \binom{n}{m} \binom{n+m}{m}} \right) +
\frac{5 (2n+1) k(-1)^{k-1}}{n(n+1)} \binom{n}{k}  \binom{n+k}{k}.$$ Ceci démontre qu'on a $u_{{\rm E},n}= u_{{\rm R}, n}$ et $v_{{\rm E},n}= v_{{\rm R}, n}$ pour tout $n \geq 0$. Compte tenu des résultats démontrés au paragraphe 1.1, on obtient une preuve de l'irrationalité de $\zeta(3)$.

La démonstration donnée ci-dessus que $(u_{{\rm E},n})$ et $(v_{{\rm E},n})$ vérifient la récurrence (relnrec) n'est qu'une simple vérification, à condition d'être capable d'exhiber les suites doubles ${\bf A}_{n,k}$ et ${\bf B}_{n,k}$, ce qui n'a pas été une tâche facile (voir [@VDP], §7). Motivés par ce problème, plusieurs auteurs (notamment Zeilberger) ont ensuite mis au point des algorithmes permettant d'exhiber de telles suites doubles. On a ainsi un moyen automatique de produire des preuves d'identités (voir [@CartierZeilberger], [@Zeilberger], [@AegaleB]). De plus, ces preuves sont immédiatement vérifiables à la main.

Dans les formules ci-dessus, un rôle central est joué par la suite double $c_{n,k} =   \sum_{m=1} ^n \frac{1}{m^3} + \sum_{m=1} ^k
\frac{(-1)^{m-1}}{2 m^3 \binom{n}{m} \binom{n+m}{m}}$ (définie pour $0 \leq k \leq n$). Elle tend vers $\zeta(3)$ quand $n$ tend vers l'infini, uniformément en $k$. On a $c_{n,n} - c_{n-1,n-1} = \frac{5}{2}\frac{(-1)^{n-1}}{n^3 \binom{2n}{n}}$ et $\lim_{n \to \infty} c_{n,n} = \zeta(3)$ donc : $$\label{atrois}
\zeta(3) = \frac{5}{2} \sum_{n=1} ^\infty \frac{(-1)^{n-1}}{n^3
\binom{2n}{n}}.$$ Cette série n'est pas utilisée dans la preuve de l'irrationalité de $\zeta(3)$, mais elle a un intérêt non négligeable puisque les $c_{n,k}$ sont au cœur des formules explicites définissant $u_{{\rm E},n}$ et $v_{{\rm E},n}$. C'est pourquoi plusieurs auteurs ont cherché des généralisations de (atrois) (voir par exemple [@VDP], [@VDPQueens], [@CohenSMF], [@Koecher], [@Leshchiner], [@BorweinBradley], [@AlmkvistGranville]), parmi lesquelles $\zeta(5) = \frac{5}{2} \sum_{n \geq 1} \frac{(-1)^n}{n^3 \binom{2n}{n}}
\left( \sum_{j=1} ^{n-1} \frac{1}{j^2} - \frac{4}{5n^2} \right)$. Mais aucune de ces généralisations n'a permis d'obtenir de nouveau résultat d'irrationalité : la croissance des dénominateurs est trop rapide par rapport à la convergence.

Prévost a montré [@Prevost] comment interpréter les formules explicites données dans ce paragraphe en termes d'approximants de Padé. Posons $\varphi(x) = \sum_{k \geq 1} \frac{1}{(k+x)^3}$, c'est-à-dire $\zeta(3, 1+x)$ où $\zeta$ est la fonction zêta d'Hurwitz (voir [@WhittakerWatson], Chapitre XIII). Pour tout $n \geq 1$, considérons les polynômes suivants : $$\begin{aligned}
P_{n}(x) &=& \sum_{k=0} ^n \binom{n}{k}\binom{n+k}{k}
\binom{x}{k}\binom{x+k}{k} = \, \, {_4 F_3 \left(
\begin{array}{cccc|}
 -n , & -x, & n+1, & x+1 \\
     &  1,  &  1, &  1
\end{array}
\, \,  1 \right)} \\
\mbox{ et } \, \, \, \,
Q_{n}(x) &=& \sum_{k=0} ^n \binom{n}{k}\binom{n+k}{k}
\binom{x}{k}\binom{x+k}{k} \sum_{m=1} ^k
\frac{(-1)^{m-1}}{2 m^3 \binom{x}{m} \binom{x+m}{m}}.
\end{aligned}$$ Alors $P_{n}$ est de degré $2n$, $Q_{n}$ de degré $2n-2$, et on a $P_{n}(x) \varphi(x) - Q_{n}(x) = \textup{O}(x^{-2n-1})$ quand $x$ tend vers l'infini. Cela signifie que $P_{n}$ et $Q_{n}$ sont des approximants de Padé de la fonction $\varphi$. Quand $x$ est un entier $n$, on a $\varphi(n) =
\zeta(3) - \sum_{m=1} ^n \frac{1}{m^3}$ d'où $P_{n}(n) \varphi(n) - Q_{n}(n) = u_{{\rm E},n}\zeta(3) - v_{{\rm E},n}$. On peut en déduire [@Prevost] la majoration $\vert u_{{\rm E},n}\zeta(3) - v_{{\rm E},n}\vert \leq \frac{4 \pi^2}{(2n+1)^2
u_{{\rm E},n}}$. Pour conclure, on a besoin d'une minoration asymptotique de $u_{{\rm E},n}$ comme celle de la formule (asyunvnrec). Il suffit donc de vérifier que $u_{{\rm E},n}$ satisfait à la récurrence (relnrec). On peut utiliser ${\bf A}_{n,k}$ comme ci-dessous ; une autre méthode [@AskeyWilson] est d'utiliser des relations de contiguı̈té entre séries hypergéométriques balancées.

En effet, $u_{{\rm E},n}$ s'écrit ${_4 F_3 \left(
\begin{array}{cccc|}
 -n , & -n,  & n+1, & n+1 \\
     &  1 , &  1 , &  1
\end{array}
\, \,  1 \right)}$. Une série hypergéométrique $_4 F_3 \left(
\begin{array}{cccc|}
 \alpha_0 , & \alpha_1,  & \alpha_2, & \alpha_3 \\
     &  \beta_1 , &  \beta_2 , &  \beta_3
\end{array}
\, \,  z \right)$ est dite ([@Slater], §2.1.1) *balancée* (ou *Saalschützienne*) si $1 + \sum_{i=0} ^3 \alpha_i= \sum_{j=1} ^3 \beta_j$. Si on modifie deux des sept paramètres d'une série balancée, en ajoutant ou en retranchant 1 à chacun des deux, on peut obtenir à nouveau une série balancée. Si c'est le cas, on dit que ces deux séries sont *contiguës*. Il y a $2 \cdot \binom{7}{2} = 42$ séries balancées qui sont contiguës à une série balancée donnée. Quand $\alpha_0$ est un entier négatif (ce qui signifie que la série hypergéométrique est en fait un polynôme), il existe des relations linéaires entre les valeurs en 1 de ces 42 séries, dont les coefficients sont des polynômes en les paramètres $\alpha_0$, ..., $\beta_3$ (voir [@AAR], §3.7). On peut [@AskeyWilson] déduire de ces relations de contiguı̈té que la suite $u_{{\rm E},n}$ vérifie la récurrence (relnrec).

## Intégrale triple réelle

Considérons l'intégrale suivante, qui a été introduite par Beukers [@Beukers] (voir aussi [@BeukersBolyai]) : $$I_{\mathbb{R},n}(z) = \int_0 ^1 \int_0 ^1 \int_0 ^1 \frac{u^n (1-u)^n v^n (1-v)^n w^n
(1-w)^n}{((1-w)z+uvw)^{n+1}} {\rm d}u \, {\rm d}v \, {\rm d}w.$$ Cette intégrale converge pour tout $z \in \mathbb{C}\setminus] - \infty, 0]$. Voici une esquisse de preuve de l'irrationalité de $\zeta(3)$ qui utilise $I_{\mathbb{R},n}(1)$. Les détails se trouvent dans [@Beukers].

Comme le maximum de la fonction $\frac{u (1-u) v (1-v) w (1-w)}{1-w(1-uv)}$ sur le cube unité vaut $(\sqrt{2}-1)^4$, on a : $$\lim_{n \rightarrow +\infty} \frac{\log (I_{\mathbb{R},n}(1)) }{n}
 = \log((\sqrt{2} - 1)^4).$$ Par ailleurs, si on intègre $n$ fois par parties par rapport à $v$, qu'on change $w$ en $\frac{1-w}{1-w(1-uv)}$, et enfin qu'on intègre $n$ fois par parties par rapport à $u$, on obtient : $$I_{\mathbb{R},n}(1) = \int_0 ^1 \int_0 ^1 \int_0 ^1
\frac{P_n(u) P_n(v)}{1-w(1-uv)}
 {\rm d}u \, {\rm d}v \, {\rm d}w,$$ où $P_n(X) = \frac{1}{n!} (X^n (1-X)^n)^{(n)}$ est le $n$-ième polynôme de Legendre. En intégrant par rapport à $w$, il vient $I_{\mathbb{R},n}(1)= \int_0 ^1 \int_0 ^1  \frac{- \log(uv)}{1-uv} P_n(u) P_n(v)
 {\rm d}u \, {\rm d}v$. Or pour tous $k, l \in \{0, \ldots, n\}$ on peut écrire $\int_0 ^1 \int_0 ^1  \frac{- \log(uv)}{1-uv} u^k v^l
 {\rm d}u \, {\rm d}v = 2 a_{k,l} \zeta(3) + b_{k,l}$ avec $a_{k,l} \in \mathbb{Z}$ et $d_n ^3 b_{k,l} \in \mathbb{Z}$. On a donc : $$I_{\mathbb{R},n}(1) = 2 (u_{\mathbb{R},n}\zeta(3) - v_{\mathbb{R},n}) \mbox{ avec } u_{\mathbb{R},n}\in \mathbb{Z}
\mbox{ et } 2 d_n ^3 v_{\mathbb{R},n}\in \mathbb{Z}.$$ Cela termine la preuve de l'irrationalité de $\zeta(3)$.

## Série de type hypergéométrique

Posons $$\label{eqdefr}
R_n(X) = \frac{(X-1)^2 \ldots (X-n)^2}{X^2 (X+1)^2 \ldots (X+n)^2}
 = \frac{(X-n)_n ^2}{(X)_{n+1}^2} = \frac{\Gamma(X)^4}{\Gamma(X-n)^2
 \Gamma(X+n+1)^2},$$ où $\Gamma$ est la fonction Gamma d'Euler, qui vérifie $\Gamma(s+1) = s \Gamma(s)$. En outre, pour $\vert z \vert \geq 1$ on pose : $$\label{eqdefines}
I_{\Sigma,n}(z) = - \sum_{k=1} ^\infty R'_n(k) z^{-k}.$$

En suivant [@BeukersLNM], [@Gutnik83] et [@Nesterenko96] on développe la fraction rationnelle $R_n$ en éléments simples : $$\label{eqdcpelsplesines}
R_n(X) = \sum_{i=0} ^n \left( \frac{\alpha_i}{(X+i)^2} + \frac{\beta_i}{X+i}
\right),$$ avec $\alpha_i =\binom{n}{i}^2  \binom{n+i}{i}^2$ et $\beta_i = 2 (-1)^i  \binom{n}{i} \binom{n+i}{i} \sum_{j \in \{0,
\ldots,n\}, j \neq i}
\frac{(-1)^j   \binom{n}{j} \binom{n+j}{j}}{j-i}$

pour $i \in \{0,\ldots,n\}$ (ces formules s'obtiennent en remarquant que $R_n(X) = (\frac{(X-n)_n}{(X)_{n+1}})^2$ ; voir la démonstration du lemme 21 ci-dessous, ou bien [@Colmez], [@Habsieger] ou [@Zudilinelementary]). En utilisant (eqdcpelsplesines) pour exprimer (eqdefines) il vient : $$\begin{aligned}
I_{\Sigma,n}(z)&=& 2 \sum_{i=0} ^n \alpha_i z^i \sum_{k \geq 1} \frac{z^{-(k+i)}}{(k+i)^3}
+ \sum_{i=0} ^n \beta_i z^i \sum_{k \geq 1} \frac{z^{-(k+i)}}{(k+i)^2}
                    \nonumber \\
&=& 2 A_n(z) {\rm Li}_3(1/z) + B_n (z) {\rm Li}_2(1/z) + C_n(z) \label{dvlptines}
\end{aligned}$$ où les polynômes $A_n$, $B_n$ et $C_n$ sont définis par : $$\begin{aligned}
A_n(z) &=& \sum_{i=0} ^n \alpha_i z^i
= {_4 F_3 \left(
\begin{array}{cccc|}
 -n , & -n,  & n+1, & n+1 \\
     &  1 , &  1 , &  1
\end{array}
\, \,  z \right)}
\\B_n(z) &=& \sum_{i=0} ^n \beta_i z^i
\\C_n(z) &=& - \sum_{t=0} ^{n-1} z^t \sum_{i=t+1} ^n \left( \frac{2 \alpha_i}{(i-t)^3}
+ \frac{\beta_i}{(i-t)^2} \right)
\end{aligned}$$

Il est clair que les polynômes $A_n(z)$, $d_n B_n(z)$ et $d_n^3 C_n(z)$ sont à coefficients entiers.

On a $B_n(1) = 0$ car $R_n$ n'a pas de résidu à l'infini. En posant $u_{\Sigma,n}= A_n(1)$ et $v_{\Sigma,n}= -C_n(1)/2$ il vient : $$\label{NestFourier}
I_{\Sigma,n}(1) =
2 (u_{\Sigma,n}\zeta(3) - v_{\Sigma,n}) \mbox{ avec } u_{\Sigma,n}\in \mathbb{Z}\mbox{ et }
2d_n ^3 v_{\Sigma,n}\in \mathbb{Z}.$$

Pour démontrer l'irrationalité de $\zeta(3)$, il ne reste plus qu'à estimer $I_{\Sigma,n}(1)$. On peut le faire en transformant $I_{\Sigma,n}(1)$ en une intégrale complexe (voir le paragraphe 1.5) ; c'est ainsi que Nesterenko démontre [@Nesterenko96] le théorème d'Apéry.

On peut démontrer, en utilisant [@Zudilinelementary] l'algorithme de "creative telescoping" ([@AegaleB], Chapitre 6), que $I_{\Sigma,n}(1)$, $u_{\Sigma,n}$ et $v_{\Sigma,n}$ satisfont à la relation de récurrence (relnrec). Cela démontre en particulier l'identité $v_{\Sigma,n}=v_{{\rm E},n}$.

## Intégrale complexe

Soit $c$ un réel, avec $0 < c < n+1$. Pour $z \neq 0$, choisissons une détermination de $\arg(z)$ strictement comprise entre $-2\pi$ et $2 \pi$, et considérons l'intégrale suivante, le long de la droite verticale ${\rm Re}(s) = c$ dans $\mathbb{C}$, orientée de bas en haut : $$\begin{aligned}
I_{\mathbb{C},n}(z) &=& \frac{1}{2i\pi} \int_{c-i \infty} ^{c + i \infty}
\left( \frac{\pi}{\sin(\pi s)} \right)^2 R_n(s) z^{-s} {\rm d}s \nonumber \\
&=& \frac{1}{2i\pi} \int_{c-i \infty} ^{c + i \infty}
\frac{\Gamma(n+1-s) ^2 \Gamma(s) ^4}{\Gamma(n+1+s)^2} z^{-s} {\rm d}s,
                        \label{intmeijer}
\end{aligned}$$ cette dernière égalité provenant directement de (eqdefr) et de la formule classique $\frac{\pi}{\sin(\pi s)} = \Gamma(s) \Gamma(1-s)$. La valeur de $I_{\mathbb{C},n}(z)$ ne dépend pas du choix de $c$ d'après le théorème des résidus. L'intégrale (intmeijer) est un exemple de $G$-fonction de Meijer (voir [@Luke], §5.2) :

$$I_{\mathbb{C},n}(z) =
G ^{4,2} _{4,4} \left(
\begin{array}{cccc|}
 -n, & -n ,& n+1, & n+1 \\
   0, & 0,  & 0, &  0
\end{array}
\, \, z \right).$$

La méthode du col (voir par exemple [@Dieudonne], Chapitre IX) permet [@Nesterenko96] d'obtenir une estimation asymptotique très précise : $$I_{\mathbb{C},n}(1)= \frac{\pi ^{3/2} 2^{3/4}}{n^{3/2}} (\sqrt{2}-1)^{4n+2}
(1+\textup{O}(n^{-1})).$$

Quand on déplace le contour d'intégration vers la droite pour faire apparaı̂tre les pôles $n+1$, $n+2$, ..., le théorème des résidus donne ([@Gutnik79], [@Gutnik83]), puisque $(\frac{\pi}{\sin(\pi s)})^2=
\frac{1}{(s-k)^2} + \textup{O}(1)$ quand $s$ tend vers un entier $k$ :

$$\label{eqfunfde}
I_{\mathbb{C},n}(z) =  I_{\Sigma,n}(z) +  \log(z) \sum_{k = 1} ^\infty R_n(k) z^{-k}.$$ En particulier pour $z = 1$ on obtient $I_{\mathbb{C},n}(1) = I_{\Sigma,n}(1)$.

Par ailleurs, Nesterenko a démontré [@NesterenkoCaen] un théorème général qui relie une intégrale multiple réelle à une intégrale complexe ; dans notre cas particulier, ce théorème donne $I_{\mathbb{C},n}(z) = I_{\mathbb{R},n}(z)$.

On peut démontrer [@Nesterenko96] que $I_{\mathbb{C},n}(1)$ vérifie la récurrence (relnrec) en utilisant les relations de contiguı̈té sur les $G$-fonctions de Meijer. C'est en fait une preuve parallèle à celle du paragraphe 1.2, où on utilisait la contiguı̈té entre des $_4 F_3$. En effet ([@Luke], §5.8), ces $_4 F_3$ satisfont aux mêmes équations différentielles que les $G$-fonctions de Meijer correspondantes, donc aux mêmes relations de contiguı̈té.

## Un problème d'approximation de Padé

Considérons [@BeukersLNM] le problème suivant : trouver quatre polynômes $A_n$, $B_n$, $C_n$ et $D_n$, à coefficients rationnels, de degré au plus $n$, tels que :

$$\label{pbpade}
\begin{cases}
F_n(z):=A_n(z){\rm Li}_2(1/z)+B_n(z){\rm Li}_1(1/z)+D_n(z)=\textup{O}(z^{-n-1})
\mbox{ quand } z \to \infty \\
G_n(z):=2A_n(z){\rm Li}_3(1/z)+B_n(z){\rm Li}_2(1/z)+C_n(z)=\textup{O}(z^{-n-1})
 \mbox{ quand } z \to \infty \\
B_n(1) = 0
\end{cases}$$

Une solution à ce problème de Padé est donnée par les polynômes $A_n$, $B_n$ et $C_n$ du paragraphe 1.4 (et un polynôme $D_n$ convenable). On a alors : $$\begin{cases}
F_n(z) = \sum_{k=1} ^\infty R_n(k) z^{-k}
 = \frac{n!^4}{(2n+1)!^2} z^{-n-1}
{_4 F_3} \left(
\begin{array}{cccc|}
 n+1, & n+1, & n+1, & n+1 \\
     &  2n+2,  &  2n+2, &  1
\end{array}
\, \, \,  z^{-1} \right)\\
G_n(z) = I_{\Sigma,n}(z) = - \sum_{k=1} ^\infty R'_n(k) z^{-k}
\end{cases}$$

En effet, la seconde égalité est simplement une réécriture de (eqdefines) et (dvlptines). La première se démontre de manière analogue à (dvlptines), mais sans dériver (eqdcpelsplesines).

L'équation différentielle hypergéométrique sous-jacente aux constructions des paragraphes 1.4 et 1.5 s'écrit $Ly = 0$, en posant

$$L= z(\delta+n +1)^2 (\delta-n)^2 - \delta^4 \mbox{ avec }
\delta= z \frac{{\rm d}}{{\rm d}z}.$$ Elle admet au voisinage de l'infini quatre solutions linéairement indépendantes : $F_n(z)$, $I_{\mathbb{C},n}(z) = G_n(z) + F_n(z) \log(z)$, $A_n(z)$ et $B_n(z) - A_n(z) \log(z)$ (voir [@Luke], §5.1 et 5.8, [@Huttnerlille] et [@Gutnik83]). Ces solutions sont reliées par la monodromie : en prolongeant analytiquement $F_n$ le long d'un lacet qui entoure le point 1 on fait apparaı̂tre $B_n(z) + A_n(z) \log(1/z)$, puis en faisant le tour de l'infini on obtient $A_n(z)$ (voir [@Oesterle] pour la monodromie des polylogarithmes).

Ce point de vue permet de démontrer [@Huttnerlille] que le problème de Padé (pbpade) a une solution unique (à proportionnalité près). En effet, en partant d'une solution $A_n$, $B_n$, $C_n$, $D_n$, on montre que $F_n$ vérifie une équation différentielle linéaire fuchsienne d'ordre 4 qu'on détermine explicitement (en calculant ses exposants, et en utilisant la relation de Fuchs) : on trouve que c'est $Ly = 0$.

Pour démontrer l'unicité de la solution de ce problème de Padé, on peut aussi suivre [@BeukersLNM]. On part d'une solution quelconque, avec des polynômes $A_n$, $B_n$, $C_n$, $D_n$ et des fonctions $F_n$ et $G_n$. On note $\alpha_i$ et $\beta_i$ les coefficients de $A_n$ et $B_n$, et on leur associe la fraction rationnelle $R_n$ définie par (eqdcpelsplesines). On voit alors que $F_n(z) = \sum_{k=1} ^\infty R_n(k) z^{-k}$ et $G_n(z) = - \sum_{k=1} ^\infty R'_n(k) z^{-k}$ , donc les deux premières contraintes de (pbpade) signifient que $R_n$ et sa dérivée s'annulent aux points 1, 2, ..., $n$. En outre, le résidu à l'infini de $R_n$ est alors $B_n(1)=0$ : la fraction rationnelle $R_n$ est nécessairement donnée, à constante multiplicative près, par (eqdefr).

## Polynômes orthogonaux

Considérons ([@BorweinErdelyi], [@AsscheDelhi]) le problème suivant : trouver deux polynômes $\widetilde{A}_n$ et $\widetilde{B}_n$, de degré au plus $n$, tels que : $$\label{pbortho}
\begin{cases}
\int_0 ^1 \left( \widetilde{B}_n(x) - \widetilde{A}_n(x) \log(x) \right) x^k {\rm d}x = 0
\mbox{ pour tout } k \in \{ 0, \ldots, n-1\} \\
\int_0 ^1 \left( \widetilde{B}_n(x)  - \widetilde{A}_n(x)  \log(x) \right) x^k \log(x) {\rm d}x = 0
\mbox{ pour tout } k \in \{ 0, \ldots, n-1\} \\
\widetilde{B}_n(1) = 0
\end{cases}$$ Une solution à ce problème est donnée par les polynômes $\widetilde{A}_n$ et $\widetilde{B}_n$ définis par : $$\label{bnanleg}
\widetilde{B}_n(x) - \widetilde{A}_n(x) \log(x) = \int_x ^1 P_n(\frac{x}{t})
P_n(t) \frac{{\rm d}t}{t},$$ où $P_n$ est le $n$-ième polynôme de Legendre (comme au paragraphe 1.3). En effet, on a alors $\int_0 ^1 \left( \widetilde{B}_n(x) - \widetilde{A}_n(x) \log(x) \right) x^k {\rm d}x =
\left( \int_0 ^1 P_n(u) u^k {\rm d}u \right) ^2$ en posant $u =\frac{x}{t}$. La première condition de (pbortho) en découle immédiatement ; la deuxième s'obtient après dérivation par rapport à $k$.

Comme on a ${\rm Li}_j(1/z) = \frac{(-1)^{j-1}}{(j-1)!} \int_0 ^1 \log^{j-1}(x)
\frac{{\rm d}x}{z-x}$ pour tout entier $j \geq 1$, il vient : $$\label{eqresteavecc}
2 \widetilde{A}_n(z) {\rm Li}_3(1/z) + \widetilde{B}_n(z){\rm Li}_2(1/z) =
- \int_0 ^1  \left(\widetilde{B}_n(z) - \widetilde{A}_n(z) \log(x) \right) \frac{\log(x) \, {\rm d}x}{z-x}.$$ On définit un polynôme $\widetilde{C}_n(z)$ par : $$\widetilde{C}_n(z) =

\int_0 ^1  \frac{\widetilde{B}_n(z) -\widetilde{B}_n(x)}{z-x} \log(x) \, {\rm d}x -
 \int_0 ^1  \frac{\widetilde{A}_n(z) -\widetilde{A}_n(x)}{z-x} \log^2(x) \, {\rm d}x .$$ Grâce à (bnanleg) on peut obtenir des formules explicites pour $\widetilde{A}_n$, $\widetilde{B}_n$ et $\widetilde{C}_n$ ; on trouve les mêmes que pour $A_n$, $B_n$ et $C_n$ respectivement au paragraphe 1.4.

Donc $\widetilde{A}_n$, $d_n \widetilde{B}_n$ et $d_n^3 \widetilde{C}_n$ sont à coefficients entiers. On obtient aussi ([@BorweinErdelyi], Corollaire A.2.3) que tous les zéros de $\widetilde{A}_n(z)$ et de $\frac{\widetilde{B}_n(z)}{z-1}$ sont réels négatifs, et entrelacés. Par ailleurs, on a : $$2 \widetilde{A}_n(z) {\rm Li}_3(1/z) + \widetilde{B}_n(z){\rm Li}_2(1/z) + \widetilde{C}_n(z) =
- \int_0 ^1  \left(\widetilde{B}_n(x) - \widetilde{A}_n(x) \log(x) \right) \frac{\log(x) {\rm d}x}{z-x}.$$ Quand $z=1$, le membre de droite se transforme (en utilisant (bnanleg) et en posant $u=t$, $v = \frac{x}{t}$) en $I_{\mathbb{R},n}(1) = - \int_0 ^1 \int_0 ^1 \frac{\log(uv)}{1-uv}P_n(u)P_n(v) {\rm d}u {\rm d}v$. En appliquant l'estimation asymptotique de $I_{\mathbb{R},n}(1)$ obtenue au paragraphe 1.3, on obtient une démonstration de l'irrationalité de $\zeta(3)$.

En fait un couple $(\widetilde{A}_n, \widetilde{B}_n)$ vérifie (pbortho) si, et seulement si, il existe $C_n$ et $D_n$ tels que $(\widetilde{A}_n, \widetilde{B}_n, C_n, D_n)$ soit une solution du problème de Padé (pbpade). Plus précisément, la première (resp. la deuxième) assertion de (pbpade) équivaut à la première (resp. la deuxième) assertion de (pbortho) (il s'agit d'un fait général : voir par exemple [@NikishinSorokin], Chapitre 4, §3.4). Démontrons-le pour la deuxième. Soient $\Gamma$ un chemin qui entoure le segment $[0,1]$ dans sens direct, et $k \in \{ 0, \ldots, n-1\}$. On a :

$$\frac{1}{2 i \pi} \int_\Gamma z^k \left(
2 \widetilde{A}_n(z) {\rm Li}_3(1/z) + \widetilde{B}_n(z) {\rm Li}_2(1/z) \right) \, {\rm d}z
= - \int_0 ^1 \left( \widetilde{B}_n(x) - \widetilde{A}_n(x) \log(x) \right) x^k \log(x) \, {\rm d}x ,$$

d'après (eqresteavecc), en intervertissant les deux signes d'intégration et en appliquant le théorème des résidus.

Il découle de ceci que le problème (pbortho) a une solution unique (à proportionnalité près), donnée par $\widetilde{A}_n = A_n$ et $\widetilde{B}_n = B_n$.

## D'autres problèmes d'approximation de Padé

Sorokin [@SorokinApery] considère le problème de Padé suivant : pour $n \geq 0$, trouver des polynômes $T_n$, $U_n$, $V_n$, $W_n$ de degré au plus $n$ tels qu'on ait :

$$\begin{cases}
I_{{\rm P},n}(z):=T_n(z){\rm Le}_{2,1}(1/z)+U_n(z){\rm Le}_{1,1}(1/z)+
    V_n(z) {\rm Li}_1(1/z) + W_n(z)=\textup{O}(z^{-n-1}) \\
\hspace{12cm} \mbox{ quand } z \to \infty\\
T_n(z){\rm Li}_2(1-z)+V_n(z)=\textup{O}((1-z)^{n+1}) \mbox{ quand } z \to 1 \\
T_n(z){\rm Li}_1(1-z)+U_n(z)=\textup{O}((1-z)^{n+1}) \mbox{ quand } z \to 1 ,
\end{cases}$$ où pour $s_1, \ldots, s_k \geq 1$ on définit le polylogarithme multiple $${\rm Le}_{s_1,\ldots,s_k}(z) = \sum_{n_1 \geq \ldots \geq n_k \geq 1}
\frac{z^{n_1}}{n_1^{s_1}\ldots n_k^{s_k}},$$ qui vérifie ${\rm Le}_{2,1}(1) = 2 \zeta(3)$ (voir [@MiW]).

Sorokin démontre que ce problème de Padé admet une solution unique, et qu'à proportionnalité près elle vérifie (pour $z \in \mathbb{C}\setminus[0,1[$) : $$I_{{\rm P},n}(z) = z^{n+1}
\int_0 ^1 \int_0 ^1 \int_0 ^1 \frac{u^n (1-u)^n v^n (1-v)^n w^n
(1-w)^n}{(z-uv)^{n+1}(z-uvw)^{n+1}} {\rm d}u \, {\rm d}v \, {\rm d}w.$$ Avec cette normalisation, $T_n$ est à coefficients entiers (donc aussi $d_n U_n$, $d_n ^2 V_n$ et $d_n^3 W_n$), d'où : $$I_{{\rm P},n}(1) = 2 (u_{{\rm P},n}\zeta(3) - v_{{\rm P},n}) \mbox{ avec }
u_{{\rm P},n}\in \mathbb{Z}\mbox{ et } 2 d_n ^3 v_{{\rm P},n}\in \mathbb{Z}.$$ De plus l'expression intégrale donne facilement l'estimation asymptotique de $I_{{\rm P},n}(1)$ ; c'est ainsi que Sorokin démontre l'irrationalité de $\zeta(3)$.

Un théorème général de Zlobin [@Zlobin] montre qu'on a $$I_{{\rm P},n}(z) = \int_0 ^1 \int_0 ^1 \int_0 ^1 \frac{u^n (1-u)^n v^n (1-v)^n w^n
(1-w)^n}{(z-w(1-uv))^{n+1}} {\rm d}u \, {\rm d}v \, {\rm d}w,$$ d'où $I_{{\rm P},n}(1) = I_{\mathbb{R},n}(1)$. On peut obtenir directement ce résultat en appliquant le changement de variables ([@SFCRAS], §2) défini par $U = 1-w$, $V = \frac{(1-u)v}{1-uv}$ et $W = u$ (et qui vérifie $1-W(1-UV) = \frac{(1-u)(1-uvw)}{1-uv}$).

Il existe plusieurs autres problèmes de Padé liés à $\zeta(3)$ ; l'un d'entre eux [@Sorokin94] fait apparaı̂tre l'intégrale suivante : $$\int_0 ^1 \int_0 ^1 \int_0 ^1 \frac{u^n (1-u)^n v^n (1-v)^n w^n
(1-w)^n}{(z(1-u+uv)-uvw)^{n+1}} {\rm d}u \, {\rm d}v \, {\rm d}w.$$ Le changement de variables qui fixe $u$ et $w$ et change $v$ en $\frac{v}{1-u(1-v)}$ transforme cette intégrale en $$\int_0 ^1 \int_0 ^1 \int_0 ^1 \frac{u^n (1-u)^n v^n (1-v)^n w^n
(1-w)^n}{(1-uv)^{n+1}(z-uvw)^{n+1}} {\rm d}u \, {\rm d}v \, {\rm d}w.$$

Ces différents problèmes de Padé fournissent tous les formes linéaires d'Apéry en 1 et $\zeta(3)$, mais ils correspondent à des combinaisons linéaires différentes de polylogarithmes.

## Série hypergéométrique très bien équilibrée

On pose : $$\begin{aligned}
H_n(X) &=& n!^2 (2X+n) \frac{(X-1)\ldots(X-n)(X+n+1)\ldots(X+2n)}{X^4
 (X+1)^4 \ldots (X+n)^4} \\
 &=& n!^2 (2X+n) \frac{(X-n)_n (X+n+1)_n}{(X)_{n+1}^4}
\end{aligned}$$ et $$I_{{\rm TB},n}(z) = \sum_{k =1} ^\infty H_n(k) z^{-k}.$$

La série $I_{{\rm TB},n}(1)$ a été introduite par K. Ball (voir [@survol]) dans le but de répondre à une question de Nesterenko [@Nesterenko96] : trouver une preuve de l'irrationalité de $\zeta(3)$ analogue à celle de Fourier ([@EMS], Chapitre 2, §1.1) pour l'irrationalité de $e$. En effet, on peut estimer $I_{{\rm TB},n}(1)$ de manière élémentaire ([@Zudilinelementary], Lemme 4 ; [@theseTanguy], §5.1 ; voir aussi la seconde démonstration du lemme 3 de [@BR]) : $$\lim_{n \to +\infty} \frac{\log(I_{{\rm TB},n}(1))}{n} = \log((\sqrt{2}-1)^4),$$ ou bien (voir le paragraphe 2.3) déduire cette estimation d'une représentation intégrale de $I_{{\rm TB},n}(z)$ vue comme série hypergéométrique très bien équilibrée : $$I_{{\rm TB},n}(z) = z^{-n-1} \frac{n!^7 (3n+2)!}{(2n+1)!^5} \,
{_{7}F_{6} \left(
\begin{array}{ccccc|}
 3n+2, & \frac{3}{2}n+2, & n+1, & \ldots, & n+1 \\
    & \frac{3}{2}n+1 ,& 2n+2, & \ldots, & 2n+2
\end{array}
\, \, \,  z^{-1} \right)}.$$ De plus, on a $I_{{\rm TB},n}(z) = P_0(z) + \sum_{j=1} ^4 P_j(z)
{\rm Li}_j(1/z)$ avec des polynômes $P_0$, ..., $P_4 \in \mathbb{Q}[z]$ vérifiant $P_j(z) = (-1)^{j+1} z^4 P_j(1/z)$ pour tout $j \in \{1,\ldots,4\}$, $P_1(1)=0$ et $d_n ^{4-j} P_j(z) \in \mathbb{Z}[z]$ pour tout $j \in \{0,\ldots,4\}$ (ceci sera généralisé au paragraphe 2.3). En particulier, on en déduit $$\label{dcpball}
I_{{\rm TB},n}(1) = 2 (u_{{\rm TB},n}\zeta(3) - v_{{\rm TB},n}) \mbox{ avec }
2d_n u_{{\rm TB},n}\in \mathbb{Z}\mbox{ et } 2d_n^4 v_{{\rm TB},n}\in  \mathbb{Z}.$$ Mais ceci ne suffit pas à démontrer l'irrationalité de $\zeta(3)$, car $(\sqrt{2}-1)^4 e ^4 > 1$.

Une identité de Bailey ([@Zudilincinqaout], Proposition 2 ; [@Slater], formule (4.7.1.3)) donne $I_{{\rm TB},n}(1) = I_{\mathbb{C},n}(1)$. Une telle identité ne peut pas avoir lieu pour tout $z$, car ${\rm Li}_4(1/z)$ apparaı̂t dans la décomposition en polylogarithmes de $I_{{\rm TB},n}(z)$ mais pas dans celle de $I_{\mathbb{C},n}(z)$. Par ailleurs Zudilin a démontré une identité générale ([@Zudilinservice], Théorème 5) qui écrit une série hypergéométrique très bien équilibrée sous la forme d'une intégrale généralisant celles introduites par Beukers [@Beukers], Vasilenko [@Vasilenko] et Vasilyev ([@Vasilyevancien], [@Vasilyev]). Dans notre cas particulier, cette identité est $I_{{\rm TB},n}(1) = I_{\mathbb{R},n}(1)$. Enfin, en utilisant les algorithmes

décrits dans [@AegaleB] on peut démontrer que $I_{{\rm TB},n}(1)$ ([@theseTanguy], §5.1 ; [@Zudilinelementary]), ainsi que $u_{{\rm TB},n}$ et $v_{{\rm TB},n}$ [@Krattenthaler], vérifient la relation de récurrence (relnrec). On en déduit $u_{{\rm TB},n}= u_{{\rm E},n}$ et $v_{{\rm TB},n}= v_{{\rm E},n}$, d'où $u_{{\rm TB},n}\in \mathbb{Z}$ et $2d_n^3 v_{{\rm TB},n}\in \mathbb{Z}$ (ce qui est plus précis que (dcpball)).

## Preuve utilisant des formes modulaires

Dans ce paragraphe, on esquisse une preuve due à Beukers [@BeukersBesancon] de l'irrationalité de $\zeta(3)$. Les outils mis en œuvre sont exposés dans [@Serre] (Chapitre VII) et [@Zagier].

Pour $\tau$ dans le demi-plan de Poincaré ${\mathfrak{H}}$, posons $q = e^{2 i \pi
\tau}$ et considérons les séries d'Eisenstein $E_2(\tau) = 1 - 24 \sum_{n \geq 1} \sigma_1(n) q^n$ et $E_4(\tau) = 1 + 240 \sum_{n \geq 1} \sigma_3(n) q^n$. On pose :

$$\begin{aligned}
E(\tau) &=& \frac{1}{24} \left( -5 E_2(\tau) + 2 E_2(2 \tau) - 3 E_2 (3\tau)
+ 30 E_2 (6 \tau) \right) \\
\mbox{et \, \, \, }
F(\tau) &=& \frac{1}{40} \left(E_4(\tau) -28  E_4(2 \tau) + 63 E_4 (3\tau)
-36  E_4 (6 \tau) \right).
\end{aligned}$$ Alors $E(\tau)$, respectivement $F(\tau)$, est une forme modulaire de poids 2, resp. 4, pour $\Gamma_0(6)$. Si $F(\tau) =  \sum_{n \geq 1} f_n q^n$ désigne le développement de Fourier de $F$ à l'infini (où elle s'annule), on pose $f(\tau) =  \sum_{n \geq 1} \frac{f_n}{n^3} q^n$. On a alors $(\frac{{\rm d}}{{\rm d}\tau})^3 f(\tau) = (2 i \pi )^3 F(\tau)$.

Considérons la fonction modulaire pour $\Gamma_0(6)$ donnée par : $$t(\tau) \, = \, \left( \frac{\Delta(6\tau) \Delta(\tau)}{\Delta(2\tau)
\Delta(3\tau)} \right) ^{1/2} \, = \, \, \,
q \! \! \! \! \! \! \prod_{{\tiny \begin{array}{c} n \geq 1 \\ {\rm pgcd}(n,6)=1 \end{array}
}} \! \! \! \! \! \! \! (1-q^n)^{12},$$ avec $\Delta (\tau) = q \prod_{n \geq 1} (1-q^n)^{24}$. Elle n'a ni zéro ni pôle dans ${\mathfrak{H}}$. Au voisinage de $q=0$, $t(\tau) = q - 12 q^2 + 66 q^3 - \ldots$ s'écrit comme une série entière en $q$, à coefficients entiers, avec un rayon de convergence égal à 1. Elle admet une réciproque locale, notée $q(t) \in \mathbb{Z}[[t]]$. Par composition, on peut donc définir des suites $(u_{{\rm M},n})$ et $(v_{{\rm M},n})$ par : $$\begin{aligned}
E(q(t)) &=& \sum_{n \geq 0} u_{{\rm M},n}t^n \in \mathbb{Z}[[t]] \\
\mbox{et }E(q(t))f(q(t))  &=& \sum_{n \geq 0} v_{{\rm M},n}t^n \in \mathbb{Q}[[t]]
\mbox{ avec } v_{{\rm M},0}= 0 \mbox{ et }
d_n ^3 v_{{\rm M},n}\in \mathbb{Z}\mbox{ pour tout } n \geq 1.
\end{aligned}$$ Notons, pour $k \in \mathbb{Z}$, $w_k$ l'opérateur d'Atkin-Lehner

défini par $(w_k g)(\tau) = 6^{-k/2} \tau^{-k} g(\frac{-1}{6 \tau})$. Alors $w_2 (E) = -E$ et $w_4(F) = -F$. De cette seconde égalité (et d'un lemme de Hecke : voir [@Weil], §5) découle la relation $w_{-2}(h) = -h$, en posant $h(\tau) =
L(F,3) - f(\tau)$, où $L(F,s)$ est la fonction $L$ de $F$. Il vient alors $w_0 (Eh) = Eh$, c'est-à-dire que la fonction $E(\tau) h(\tau)$ est invariante par la substitution $\tau \mapsto
\frac{-1}{6 \tau}$.

Considérons maintenant les rayons de convergence. La fonction $t(\tau)$ est ramifiée seulement

au-dessus des points $(\sqrt{2}-1)^4$, $(\sqrt{2}+1)^4$ et $\infty$. Au-dessus de $(\sqrt{2}-1)^4$, le seul

point de ramification (modulo $\Gamma_0(6)$) est $\tau = i/\sqrt{6}$ ; il est d'indice deux, et les deux branches en ce point sont échangées par l'involution $\tau \mapsto
\frac{-1}{6 \tau}$. Comme $E(\tau) h(\tau)$ est invariante par cette involution, on peut définir $Eh$ comme une fonction de $t$ au voisinage de $t=  (\sqrt{2}-1)^4$, et en fait sur tout le disque $\vert t \vert
< (\sqrt{2}+1)^4$. Cela signifie que la série $\sum_{n \geq 0} (L(F,3) u_{{\rm M},n}- v_{{\rm M},n}) t^n$ a un rayon de convergence supérieur ou égal à $(\sqrt{2}+1)^4$, c'est-à-dire qu'on a : $$\limsup_{n \to \infty} \frac{\log \vert L(F,3) u_{{\rm M},n}- v_{{\rm M},n}\vert}{n}
\leq \log((\sqrt{2}-1)^4).$$ Ceci conclut la démonstration de l'irrationalité de $L(F,3)$. Or on peut calculer explicitement $L(F,s)$. En effet, quand ${\rm Re}(s) > 4$ on a, pour tout entier $j \geq 1$ : $$L(E_4(j\tau),s) =1+240 \sum_{n \geq 1} \frac{\sigma_3(n)}{(jn)^s}
 = 1+240 \sum_{d,e \geq 1}  \frac{d^3}{(jde)^s}
= 1+240 \zeta(s) \zeta(s-3) j^{-s}.$$ On en déduit immédiatement $L(F,s) = -2 \zeta(s) \zeta(s-3)$, d'où $L(F,3) = \zeta(3)$.

Comme $E(\tau)$ est une forme modulaire de poids 2 et $t(\tau)$ une fonction modulaire, la fonction $E(q(t))$ de la variable $t$ est solution [@ZagierCDF] (voir aussi [@Beukerspideux], p. 58) d'une équation différentielle linéaire ${\mathfrak{D}}y=0$, d'ordre trois. On peut la déterminer explicitement : $${\mathfrak{D}}= (t^4-34t^3+t^2) \frac{{\rm d}^3}{{\rm d}t^3} + (6t^3-153 t^2 + 3t)
\frac{{\rm d}^2}{{\rm d}t^2} + (7t^2 - 112 t +1) \frac{{\rm d}}{{\rm d}t}
+ (t-5).$$ Cette équation différentielle vérifiée par la série génératrice des $u_{{\rm M},n}$ montre qu'ils satisfont à la relation de récurrence (relnrec) : on a donc $u_{{\rm M},n}= u_{{\rm R}, n}$ (voir aussi [@Beukersanother]). En posant $V(t) = E(q(t))f(q(t))$ on montre [@ZagierCDF] que ${\mathfrak{D}}V = 5$, d'où $v_{{\rm M},n}= v_{{\rm R}, n}$.

Une base de solutions de l'équation différentielle ${\mathfrak{D}}y=0$ est donnée par $E(q(t))$, $\tau(t) E(q(t))$ et $\tau^2(t) E(q(t))$ (voir aussi [@BeukersPeters], Corollaire 2). La seule solution qui soit régulière en $0$ est $E(q(t))$ (à proportionnalité près). De plus, la construction de ${\mathfrak{D}}$ montre [@ZagierCDF] que c'est un carré symétrique, ce qui peut se vérifier directement (voir [@DworkAmice]).

** 9**. *Le point de vue adopté dans ce paragraphe est lié "individuellement" à $\zeta(3)$ (qui est vu comme valeur spéciale d'une fonction $L$), par opposition aux méthodes utilisées dans les paragraphes 1.3 à 1.9, où $\zeta(3)$ apparaissait comme la valeur en 1 d'un polylogarithme.*

Cette preuve de l'irrationalité de $\zeta(3)$ s'exprime naturellement en termes des séries génératrices $U(t) = \sum_{n \geq 0} u_n t^n$ et $V(t) = \sum_{n \geq 0} v_n t^n$ des approximations rationnelles de $\zeta(3)$ (voir [@VDPDPP], [@BeukersBesancon] et [@ChudCarbondale], §5 pour d'autres preuves dans le même esprit). L'aspect arithmétique consiste à démontrer que les coefficients de $U(t)$ sont entiers, et que $d_n^3$ est un dénominateur commun aux $n$ premiers coefficients de $V(t)$ : c'est une majoration $p$-adique de ces coefficients, pour toute place finie $p$. L'aspect analytique est une minoration, par $(1+\sqrt{2})^4$, du rayon de convergence (archimédien) de la série entière $\zeta(3)U(t)-V(t)$. En particulier, $U(t)$ et $V(t)$ sont des $G$-fonctions de Siegel. La série $U(t)$ est une solution de l'équation différentielle ${\mathfrak{D}}y=0$ ; la conjecture de Bombieri-Dwork prédit ([@DworkAmice], [@DworkINDAM] ; voir aussi [@Andre] et [@GerottoSullivan]) que ${\mathfrak{D}}$ provient de la géométrie.

Or, pour $t \in {\mathbb P}^1(\mathbb{C}) \setminus\{0, 1, (\sqrt{2} \pm 1)^4, \infty\}$, Beukers et Peters construisent [@BeukersPeters] une surface K3 $X_t$ birationnellement équivalente à la surface projective $S_t$ d'équation affine $1-(1-xy)z-txyz(1-x)(1-y)(1-z)=0$. Ils montrent que si $\omega_t$ est l'unique 2-forme holomorphe sur $X_t$ (à proportionnalité près), et si $\tau_t$ est un certain 2-cycle (constant pour la connexion de Gauss-Manin), alors $U(t)$ est l'intégrale de $\omega_t$ sur $\tau_t$. En particulier ${\mathfrak{D}}y=0$ est l'équation de Picard-Fuchs de cette famille de surfaces : elle provient bien de la géométrie.

## Congruences

De nombreux auteurs ont étudié des propriétés de congruence sur les nombres d'Apéry $u_n$. Par exemple, Chowla, Cowles et Cowles [@ChowlaCC] ont conjecturé $u_p \equiv 5 \mod p^3$ pour tout $p
\geq 5$ premier. Cette conjecture a été démontrée par plusieurs auteurs (voir par exemple [@Gessel], [@Sury], ...). De nombreuses autres congruences ont été prouvées, pour les nombres d'Apéry et certaines de leurs généralisations.

Notons $\sum_{n \geq 1} \gamma_n q^n = q \prod_{n \geq 1} (1-q^{2n})^4 (1-q^{4n})^4$ l'unique forme parabolique normalisée de poids 4 pour $\Gamma_0(8)$. Pour $r \geq 1$, $m \geq 1$ impair et $p$ premier impair, on a la congruence suivante (qui ressemble à celles d'Atkin - Swinnerton-Dyer, voir [@Hazewinkel] §VI.33) : $$u_{\frac12(mp^r-1)} - \gamma_p u_{\frac12(mp^{r-1}-1)} + p^3
u_{\frac12(mp^{r-2}-1)} \equiv 0 \mod p^r$$ avec la convention $u_t = 0$ si $t \notin \mathbb{Z}$. Beukers la démontre [@Beukersanother] en utilisant la construction modulaire du paragraphe 1.10. On en déduit $u_{\frac{p-1}{2}} \equiv\gamma_p \mod p$, congruence dont Beukers a conjecturé [@Beukersanother] qu'elle est vraie modulo $p^2$. Ceci a été prouvé par Ishikawa [@IshikawaKobe] si $p$ ne divise pas $u_{\frac{p-1}{2}}$, puis par Ahlgren et Ono [@AhlgrenOnocongr] dans le cas général. Ahlgren et Ono utilisent des séries hypergéométriques sur ${\mathbb F}_p$ et la modularité de la variété d'équation $x + \frac{1}{x} + y + \frac{1}{y} + z + \frac{1}{z} + w + \frac{1}{w}=0$ (dont la famille de surfaces K3 considérée par Beukers-Peters est un quotient : voir [@PetersStienstra], Théorème 4).

Pour $r,m \geq 1$ et $p \geq 5$ premier, Beukers a démontré [@Beukerscongr], de manière élémentaire, qu'on a $u_{mp^r-1} \equiv u_{mp^{r-1}-1}
\mod p^{3r}$. La même congruence, mais seulement modulo $p^r$, s'interprète en disant que $\int_0 ^T U(t) {\rm d}t$ est (vue comme série formelle en $T$) le logarithme d'une loi de groupe formel sur $\mathbb{Z}$ qui est isomorphe à ${\mathbb G}_m$ sur $\mathbb{Z}$ ([@Beukerscongr] ; voir aussi l'appendice de [@StienstraBeukers] ou [@Hazewinkel], §VI.33).

# Irrationalité d'une infinité de $\zeta(2k +1)$

## Énoncé des résultats

Dans cette partie, on démontre les résultats suivants, dont le premier implique le théorème 3 :

** 10** ([@RivoalCRAS], [@BR]). *Pour $\ell\geq 3$ impair, notons $\delta_\ell$ la dimension du $\mathbb{Q}$-espace vectoriel engendré par 1, $\zeta(3)$, $\zeta(5)$, ..., $\zeta(\ell)$. Pour tout $\varepsilon> 0$ il existe un entier $\ell_0$ tel que pour tout $\ell\geq \ell_0$ impair on ait : $$\delta_\ell\geq \frac{1-\varepsilon}{1+\log(2)} \log(\ell).$$*

** 11**. *Si dans le théorème 10 on remplace $\frac{1-\varepsilon}{1+\log(2)}$ par $\frac{1}{3}$ alors [@BR] on peut prendre $\ell_0 = 3$.*

** 12** ([@BR]). *Il existe un entier impair $\ell$, avec $\ell\leq
169$, tel que 1, $\zeta(3)$ et $\zeta(\ell)$ soient linéairement indépendants sur $\mathbb{Q}$.*

Ce théorème a été amélioré par Zudilin [@Zudilincentqc], qui remplace 169 par 145, grâce à un raffinement du lemme 21 ci-dessous.

Les deux ingrédients essentiels de la démonstration du théorème 10 sont l'absence de $\zeta(2)$, $\zeta(4)$, ..., $\zeta(\ell-1)$ d'une part, et la minoration en $\log(\ell)$ de la dimension d'autre part. Seule cette deuxième idée est utile pour démontrer le théorème suivant.

** 13** ([@theseTanguy]). *Soient $z \in \mathbb{Q}$, $\vert z \vert > 1$, et $\varepsilon> 0$. Il existe un entier $\ell_0$ (qui dépend de $z$ et $\varepsilon$) tel que, pour tout $\ell\geq \ell_0$, la dimension du $\mathbb{Q}$-espace vectoriel engendré par $1, {\rm Li}_1(1/z), {\rm Li}_2(1/z), \ldots, {\rm Li}_\ell(1/z)$ soit minorée par $\frac{1-\varepsilon}{1+\log(2)} \log(\ell)$.*

En conséquence, pour tout nombre rationnel $z$ de valeur absolue supérieure à 1 il existe une infinité d'entiers $j$ tels que ${\rm Li}_j(1/z)$ soit irrationnel. Par ailleurs, quand $z$ est un entier négatif tel que $\vert z \vert > (4\ell)^{\ell(\ell-1)}$, Nikishin a démontré [@Nikishin] que les nombres $1, {\rm Li}_1(1/z), {\rm Li}_2(1/z), \ldots, {\rm Li}_\ell(1/z)$ sont linéairement indépendants sur $\mathbb{Q}$ ; sa méthode a inspiré en partie la construction exposée au paragraphe suivant. Hata a raffiné ([@Hatapolylogs], [@Hatadilog]) le résultat de Nikishin : par exemple $1$, ${\rm Li}_1(1/z)$ et ${\rm Li}_2(1/z)$ sont linéairement indépendants sur $\mathbb{Q}$ pour $z \leq -5$ ou $z \geq 7$.

## Structure de la preuve

Soient $a$ et $r$ deux entiers, avec $a \geq 3$ et $1 \leq r < \frac{a}{2}$. Soit $n \geq 1$. Définissons ${\bf R}_n$ et ${\bf S}_n$ (qui dépendent aussi de $a$ et $r$) par : $$\begin{gathered}
{\bf R}_n(k) = 2n!^{a-2r} (k+\frac{n}{2}) \frac{(k-rn)_{rn}
(k+n+1)_{rn}}{(k)_{n+1}^a} \\
= 2n!^{a-2r} (k+\frac{n}{2}) \frac{(k-1)(k-2)\ldots(k-rn) (k+n+1)
(k+n+2)\ldots (k+(r+1)n)}{k^a (k+1)^a \ldots (k+n)^a}
\end{gathered}$$ et $$\label{eqdefs}
{\bf S}_n(z) = \sum_{k \geq 1} {\bf R}_n(k) z^{-k}.$$ Cette série converge absolument pour tout nombre complexe $z$ tel que $\vert z \vert \geq 1$, car ${\bf R}_n(k)
= \textup{O}(k^{-2})$ quand $k$ tend vers l'infini.

Les propriétés de cette série étudiées au paragraphe 2.3 permettent de démontrer les théorèmes 10 (en prenant $z=1$ et $a$ pair), 12 (avec $z=1$, $a= 169$, $r = 10$ et $n$ impair ; on utilise le théorème d'Apéry) et 13 (avec $z \in \mathbb{Q}$, $z > 1$ ; pour $z < -1$ il suffirait de modifier le lemme 18). Les trois preuves sont parallèles ; on détaille dans ce paragraphe la structure de celle du théorème 10.

On suppose $a$ pair ; on construit des formes linéaires en 1, $\zeta(3)$, $\zeta(5)$, ..., $\zeta(a-1)$ grâce à la proposition suivante :

** 14**. *[]{#proprivoal label="proprivoal"} Supposons $a$ pair. Notons $d_n$ le p.p.c.m des entiers de 1 à $n$. Alors il existe des nombres rationnels $\kappa_0$, $\kappa_3$, $\kappa_5$, ..., $\kappa_{a-1}$ tels que :*

1.  *On a ${\bf S}_n(1) = \kappa_0+ \kappa_3 \, \zeta(3) +
    \kappa_5 \, \zeta(5) + \kappa_7 \, \zeta(7) + \ldots + \kappa_{a-1} \, \zeta(a-1)$.*

2.  *[]{#assertionnest label="assertionnest"} Pour tout $j \in \{0, 3, 5, \ldots, a-1\}$ on a   $\limsup _{n \rightarrow + \infty} \vert \kappa_j \vert ^{1/n} \leq
    2^{a-2r} (2r+1)^{2r+1}$.*

3.  *Pour tout $j \in \{0,3,5,\ldots, a-1\}$, le nombre rationnel $d_n^{a} \kappa_j$ est un entier.*

4.  *Il existe un réel $\psi_{r,a} > 0$ tel que   $\lim_{n \rightarrow + \infty} \vert {\bf S}_n(1)  \vert ^{1/n} = \psi_{r,a}
    \leq \frac{2^{r+1}}{r^{a-2r}}$.*

En fait on conjecture que l'amélioration suivante est possible :

** 15** ([@theseTanguy]). *Dans l'assertion (ameliorable) de la proposition (proprivoal), on peut remplacer $d_n ^a$ par $d_n^{a-1}$.*

** 16**. *En prenant $a=4$ (et $r=1$), on obtient les formes linéaires en 1 et $\zeta(3)$ du paragraphe 1.9, donc la conjecture 15 est vraie quand $a = 4$. Elle est démontrée aussi quand $a=6$ et $r=1$ (voir la fin du paragraphe 2.4). On ne connaı̂t pas de conséquence directe de cette conjecture, mais une version forte de celle-ci pourrait éventuellement permettre de démontrer que parmi $\zeta(5)$, $\zeta(7)$ et $\zeta(9)$, l'un au moins est irrationnel (voir la remarque 27). En tout cas, il serait intéressant d'obtenir une preuve de la conjecture 15 grâce à une interprétation (par exemple géométrique, comme au paragraphe 1.10) de $\kappa_0$, ..., $\kappa_{a-1}$.*

La proposition (proprivoal) fournit des formes linéaires en 1, $\zeta(3)$, ..., $\zeta(a-1)$ (si $a$ est pair). Si cette suite de formes linéaires tend vers 0, sans être nulle à partir d'un certain rang, alors l'un au moins des nombres $\zeta(3)$, ..., $\zeta(a-1)$ est irrationnel. Cette remarque sera utilisée pour démontrer le théorème 4. Ici on veut obtenir les théorèmes 10 à 13, donc on a besoin d'un critère d'indépendance linéaire, qui donne une minoration plus fine de la dimension du $\mathbb{Q}$-espace vectoriel engendré par 1, $\zeta(3)$, ..., $\zeta(a-1)$. On va utiliser à cet effet le théorème 17 ci-dessous.

La meilleure minoration qu'on puisse espérer est donnée par le principe des tiroirs, de la manière suivante. Soient $\alpha$ et $\beta$ des réels, avec $0<\alpha<1$ et $\beta >1$. Soient $\theta_1,\ldots,\theta_s$ des réels qui engendrent un $\mathbb{Q}$-espace vectoriel de dimension au moins $1 - \frac{\log(\alpha)}{\log(\beta)}$. Alors il existe une suite $(\ell_n)$ de formes linéaires en $\theta_1$, ..., $\theta_s$ dont les coefficients entiers $p_{j,n}$ vérifient $\limsup_{n \rightarrow + \infty} \vert p_{j,n} \vert^{1/n}
\leq \beta$ pour tout $j$ et telle que $\limsup_{n \rightarrow + \infty} \vert \ell_n(\theta_1,\ldots,
\theta_s) \vert ^{1/n} \leq \alpha$. Essentiellement, plus la dimension du $\mathbb{Q}$-espace vectoriel engendré est grande, plus les formes linéaires qu'on peut construire sont petites. On cherche une réciproque à cette assertion. Une contrainte supplémentaire est nécessaire : si $\frac{\theta_2}{\theta_1}$ est un nombre de Liouville, on peut construire des formes linéaires extrêmement petites même si la dimension du $\mathbb{Q}$-espace vectoriel engendré est seulement 2. Ce contre-exemple ne tient plus si on demande que les formes linéaires en $\theta_1,\ldots,\theta_s$ ne soient pas trop petites. On a alors la réciproque suivante (pour une preuve, voir [@Nesterenkocritere] ou [@Colmez], §II.1) :

** 17** ([@Nesterenkocritere]). *Soient $\theta_1,\ldots,\theta_s$ des réels. Pour tout $n \geq 1$, soit $\ell _n = p_{1,n} X_1 + \ldots + p_{s,n}
X_s$ une forme linéaire à coefficients entiers. Soient $\alpha$ et $\beta$ des réels, avec $0<\alpha<1$ et $\beta >1$.*

*Supposons qu'on ait $\limsup_{n \to + \infty}
\vert p_{j,n} \vert^{1/n}  \leq  \beta$ pour tout $j$ compris entre 1 et $s$, et $$\lim_{n \to + \infty} \vert \ell_n(\theta_1,\ldots,
\theta_s) \vert^{1/n} = \alpha.$$ Alors le $\mathbb{Q}$-espace vectoriel engendré par $\theta_1,\ldots,\theta_s$ est de dimension au moins $1 - \frac{\log(\alpha)}{\log(\beta)}$.*

Pour déduire le théorème 10 de la proposition (proprivoal) et de ce critère d'indépendance linéaire, il suffit de considérer $d_n ^a {\bf S}_n(1)$, qui est une forme linéaire à coefficients entiers en 1, $\zeta(3)$, $\zeta(5)$, ..., $\zeta(a-1)$. On choisit $a$ suffisamment grand, et $r$ égal à la partie entière de $\frac{a}{(\log(a))^2}$. Alors $r^r$ est négligeable devant $c^a$ (pour toute constante $c$), et on peut prendre $\beta$ essentiellement égal à $(2e)^a = e^{a(1+\log(2))}$ et $\alpha$ essentiellement majoré par $r^{-a}$, qui est de l'ordre de $e^{-a \log(a)}$. Cela démontre le théorème 10.

## Quelques détails sur la preuve

Soit $z$ un nombre complexe de module supérieur ou égal à 1. La série ${\bf S}_n(z)$ peut s'écrire comme une série hypergéométrique très bien équilibrée, de la manière suivante :

$$\begin{gathered}
{\bf S}_n(z) = z^{-rn-1} n!^{a-2r}
\frac{(rn)!((r+1)n+2)_{rn+1}}{(rn+1)_{n+1} ^a} \times \\

{_{a+3}F_{a+2} \left(
\begin{array}{ccccc|}
 (2r+1)n+2, & (r+\frac{1}{2})n+2, & rn+1, & \ldots, & rn+1 \\
    & (r+
\frac{1}{2})n+1 ,& (r+1)n+2, & \ldots, & (r+1)n+2
\end{array}
\, \, \,  z^{-1} \right)}.
\end{gathered}$$

Cette identité provient de simplifications dans les symboles de Pochhammer.

### Représentation intégrale et estimation analytique

On a la représentation intégrale suivante, pour $\vert z \vert \geq 1$ :

$${\bf S}_n(z) =

\frac{((2r+1)n+2)!}{n!^{2r+1}} z^{(r+1)n+1}
\int_{[0,1]^{a+1}} \left( \frac{\prod_{j=1} ^{a+1} t_j ^r (1-t_j)}{(z-
t_1 t_2\ldots t_{a+1})^{2r+1}}\right) ^n \frac{z+t_1\ldots t_{a+1}}{(z-
t_1\ldots t_{a+1})^3} {\rm d}t_1 \ldots {\rm d}t_{a+1}.$$

Cette formule (voir par exemple [@Catalan], Lemme 1) se déduit de l'écriture de ${\bf S}_n(z)$ comme série hypergéométrique : pour $\vert z \vert > 1$ on applique les relations (4.1.2) et (1.5.21) de [@Slater], puis on prolonge à $\vert z \vert = 1$ par continuité (voir la preuve du lemme 2 de [@BR]). On peut aussi obtenir une preuve directe en développant en série le dénominateur de l'intégrande ([@Colmez], [@Habsieger]).

En calculant le maximum sur $[0,1]^{a+1}$ de la fonction dont on intègre la puissance $n$-ième, on déduit de cette représentation intégrale l'estimation analytique suivante :

** 18**. *On suppose $z \in \mathbb{R}$, $z \geq 1$. Le polynôme $$Q_{r,a,z}(s) = r s^{a+2} - (r+1)s^{a+1}+(r+1)zs - rz$$ admet une racine unique $s_0 \in [0,1]$, et elle vérifie $s_0 >
\frac{r}{r+1}$. De plus, si $$\phi_{r,a,z} = z^{-r}  ((r+1)s_0 - r)^r (r+1-rs_0)^{r+1}(1-s_0)^{a-2r},$$ alors $$\lim_{n \to \infty} \vert {\bf S}_n(z) \vert ^{1/n} = \phi_{r,a,z}
\leq \frac{2^{r+1}}{z^r r^{a-2r}}.$$*

Pour démontrer ce lemme, il suffit d'adapter les preuves du lemme 2.2 de [@theseTanguy] et du lemme 3 de [@BR]. On pourrait aussi donner une démonstration élémentaire de ce comportement asymptotique, sans utiliser la représentation intégrale (comme la deuxième preuve du lemme 3 de [@BR]). Enfin, une troisième possibilité serait d'écrire ${\bf S}_n(z)$ comme intégrale complexe et d'appliquer la méthode du col ; mais cette méthode est très difficile à mettre en œuvre quand $r$, $a$ et $z$ sont des paramètres.

** 19**. *Pour démontrer les théorèmes 10 et 13, il suffit de connaı̂tre l'existence de la limite de $\vert {\bf S}_n(z) \vert ^{1/n}$, et sa majoration par $\frac{2^{r+1}}{z^r r^{a-2r}}$. La valeur exacte de $\phi_{r,a,z}$ n'est utile que pour obtenir des estimations numériques précises (par exemple pour le théorème 12).*

### Décomposition en polylogarithmes

Pour démontrer que ${\bf S}_n(z)$ est une combinaison linéaire (à coefficients rationnels) de $1$, ${\rm Li}_1(1/z)$, ..., ${\rm Li}_a(1/z)$ quand $\vert z \vert > 1$, il suffit de décomposer la fraction rationnelle ${\bf R}_n$ en éléments simples, sous la forme suivante : $$\label{dcpelsples}
{\bf R}_n (k) = \sum_{i=0} ^n \sum_{j=1} ^a \frac{c_{i,j}}{(k+i)^j}$$ où les coefficients $c_{i,j}$ sont des rationnels, donnés par $$\label{eqdefcij}
c_{i,j}= \frac{1}{(a-j)!} \left( \frac{{\rm d}}{{\rm d}X} \right) ^{a-j}
({\bf R}_n(X) (X+i)^a) _{\vert X = -i}.$$ On a pour $\vert z \vert > 1$ : $$\begin{aligned}
{\bf S}_n(z) &=&   \sum_{i=0} ^n \sum_{j=1} ^a c_{i,j}
 \sum_{k \geq 1} \frac{z^{-k}}{(k+i)^j} \\
 &=&  \sum_{i=0} ^n \sum_{j=1} ^a c_{i,j}z^i  {\rm Li}_j(1/z) -
  \sum_{i=0} ^n \sum_{j=1} ^a c_{i,j}\sum_{q=1} ^i \frac{z^{i-q}}{q^j},
\end{aligned}$$ d'où $$\label{eqdcppolylogs}
{\bf S}_n(z) = P_0(z) + \sum_{j=1} ^a P_j(z) {\rm Li}_j(1/z)$$ en posant $$\label{eqdefpzero}
P_0(z) = - \sum_{\ell = 0} ^{n-1} \left( \sum_{i=\ell+1} ^n \sum_{j=1} ^a
\frac{c_{i,j}}{(i-\ell)^j} \right) z^\ell$$ et $$\label{eqdefpj}
P_j(z) = \sum_{i=0} ^n c_{i,j}z^i \mbox{ pour } j \in \{1, \ldots,a\}.$$ Bien sûr, les $P_j$ et les $c_{i,j}$ dépendent aussi de $n$, $a$ et $r$.

### Propriété de symétrie

La fonction ${\bf R}_n$ vérifie la propriété de symétrie suivante : $${\bf R}_n(-k-n) = (-1)^{a(n+1)+1} {\bf R}_n(k).$$ Cette symétrie est rendue possible par la présence des deux facteurs de Pochhammer au numérateur de ${\bf R}_n(k)$ : quand $k$ est changé en $-k-n$, ils sont permutés (on applique la formule $(-\alpha)_p = (-1)^p (\alpha- p +1)_p$).

L'unicité du développement en éléments simples montre que $c_{i,j} = (-1)^{j+a(n+1)+1}c_{n-i,j}$ pour tous $i \in \{0,\ldots,n\}$ et $j \in \{1,\ldots,a\}$, ce qui donne pour tout $j  \in \{1,\ldots,a\}$ : $$\label{recipropol}
P_j(z) = (-1)^{j+a(n+1)+1} z^n P_j(1/z).$$ En particulier, si $j+a(n+1)$ est pair alors $P_j(1) = 0$. De plus on a $P_1(1) = 0$, car $P_1(1) = \sum_{i=0} ^n c_{i,1}$ est l'opposé du résidu à l'infini de ${\bf R}_n$ (on peut aussi faire tendre $z$ vers 1 dans (eqdcppolylogs) et constater que le seul terme qui puisse tendre vers l'infini est $P_1(z)
 {\rm Li}_1(1/z)$). Quand $a$ est pair, on obtient donc : $${\bf S}_n(1) = P_0(1) + P_3(1) \zeta(3) +  P_5(1) \zeta(5) +  \ldots
+ P_{a-1}(1) \zeta(a-1).$$ Quand $a$ est impair et $n$ pair, on obtient de même une forme linéaire en 1, $\zeta(2)$, $\zeta(4)$, ..., $\zeta(a-1)$ dont on peut se servir pour montrer qu'une infinité de puissances de $\pi$ sont linéairement indépendantes sur $\mathbb{Q}$, i.e. que $\pi$ est transcendant. On peut aussi en déduire une mesure de transcendance de $\pi$, à la manière de Reyssat [@Reyssatmesure].

Enfin, quand $a$ et $n$ sont impairs, on obtient une forme linéaire en 1, $\zeta(3)$, $\zeta(5)$, ..., $\zeta(a)$ ; c'est ce qu'on utilise pour démontrer le théorème 12.

### Majoration des coefficients de la forme linéaire

** 20**. *Pour tout $j \in \{0,\ldots,a\}$ on a : $$\limsup _{n \rightarrow + \infty} \vert P_j(z) \vert ^{1/n} \leq
2^{a-2r} (2r+1)^{2r+1}\vert z \vert .$$*

: On peut suivre la démonstration du lemme 4 de [@BR] en écrivant la formule de Cauchy sur le cercle $C$ de centre $-i$ et de rayon $1/2$ : $$c_{i,j} = \frac{1}{2 i \pi} \int_{C} {\bf R}_n(t) (t+i)^{j-1} {\rm d}t.$$ On majore ensuite le module de l'intégrande, et le lemme en découle. Une autre preuve, qui conduit à une majoration légèrement moins précise, est donnée dans [@Colmez] et [@Habsieger].

### Estimation arithmétique

Les polynômes $P_0,\ldots,P_a$ sont à coefficients rationnels ; on a besoin d'un dénominateur commun pour leurs coefficients.

** 21**. *Pour tout $j \in \{0,\ldots,a\}$, le polynôme $d_n ^{a-j} P_j(z)$ est à coefficients entiers.*

** 22**. *On peut ([@Zudilincentqc], §4) raffiner ce lemme, ce qui permet de remplacer 169 par 145 dans l'énoncé du théorème 12. Cependant, des exemples montrent qu'on ne peut pas espérer remplacer $d_n ^{a-j}$ par $d_n ^{a-1-j}$. La conjecture 15 signifie que pour $z=1$ on a des compensations particulières qui font chuter le dénominateur.*

:

Posons $F_s (X) = \frac{(X-sn)_n}{(X)_{n+1}}$ et $G_s (X) = \frac{(X+sn+1)_n}{(X)_{n+1}}$ pour tout $s \in \{1,\ldots, r\}$, ainsi que $H(X)   = \frac{n!}{(X)_{n+1}}$ et $I(X) = 2X+n$.

Alors on a $F_s(X) = \sum_{p=0}^{n} \frac{f_{p,s}}{X+p}$ avec $f_{p,s}=(-1)^{n-p} \binom{n}{p} \binom{p+sn}{n} \in \mathbb{Z}$, et de même (avec des notations évidentes) $g_{p,s} \in \mathbb{Z}$ et $h_p \in \mathbb{Z}$ pour tous $p$, $s$. On obtient alors le développement en éléments simples de ${\bf R}_n(X) = \left( \prod_{s=1} ^r F_s (X) \right) \cdot
\left( \prod_{s=1} ^r G_s (X) \right) \cdot H(X)^{a-2r} \cdot I(X)$ en faisant le produit des développements des facteurs. On utilise les formules $\frac{2X+n}{X+p} = 2 + \frac{n-2p}{X+p}$ et $\frac{1}{(X+p)(X+p')} = \frac{1}{(p'- p)(X+p)} + \frac{1}{(p- p')(X+p')}$ pour $p \neq p'$ ; les dénominateurs n'apparaissent que par application de la seconde. Ce calcul montre que $d_n ^{a-j} c_{i,j}$ est entier pour tous $i$, $j$, ce qui achève la preuve (suivant [@Colmez] et [@Habsieger]) du lemme.

## Quelques remarques

Soit $Q_n$ un polynôme à coefficients rationnels, de degré inférieur ou égal à $a(n+1)-1$. On peut toujours considérer ${\bf R}_n(k) = \frac{Q_n(k)}{(k)_{n+1}^a}$ et ${\bf S}_n(z) = \sum_{k \geq 1} {\bf R}_n(k) z^{-k}$, qui converge quand $\vert z \vert > 1$. Une difficulté majeure consiste à bien choisir le polynôme $Q_n$.

Quel que soit ce choix, on peut décomposer ${\bf R}_n$ en éléments simples, définir $P_0$, ..., $P_a$ et obtenir une décomposition de ${\bf S}_n(z)$ en polylogarithmes : toutes les formules du paragraphe 2.3.2 restent valables. Pour obtenir une forme linéaire en valeurs de $\zeta$, il faut[^1] faire tendre $z$ vers 1. Tous les termes de la décomposition en polylogarithmes ont une limite finie, sauf peut-être $P_1(z) {\rm Li}_1(1/z)$. C'est pourquoi on suppose $P_1(1)=0$, ce qui signifie que ${\bf R}_n$ n'a pas de résidu à l'infini, i.e. $\deg(Q_n) \leq a(n+1)-2$ ; alors la série qui définit ${\bf S}_n(z)$ converge absolument dès que $\vert z
\vert \geq 1$.

En outre on souhaite[^2] obtenir une forme linéaire en les $\zeta(2k+1)$ seulement, c'est-à-dire avoir $P_{j}(1)=0$ pour tout $j \geq 2$ pair. Pour assurer cela il est suffisant d'avoir une propriété de symétrie du polynôme $Q_n$, en l'occurrence $Q_n(-k-n) = (-1)^{a(n+1)+1} Q_n(k)$. C'est cette remarque qui constitue le cœur des progrès récents ([@RivoalCRAS], [@BR]). On ne sait pas du tout la généraliser, par exemple pour construire des formes linéaires en $\zeta(s)$ dans lesquelles les $s$ appartenant à une certaine progression arithmétique n'apparaissent pas.

La forme linéaire ${\bf S}_n(1)$ ne sera intéressante que si elle tend suffisamment vite vers 0 quand $n$ tend vers l'infini. Intuitivement, ce sera le cas si les premiers termes de la série qui définit ${\bf S}_n(1)$ sont nuls. C'est pourquoi on cherche un polynôme $Q_n(k)$ qui s'annule aux premiers entiers, en l'occurrence entre 1 et $rn$ ; ceci signifie que $Q_n(k)$ est multiple de $(k-rn)_{rn}$. Il s'agit en fait d'un problème de type Padé : on demande aux polynômes $P_0$, ..., $P_a$ d'être tels que $${\bf S}_n(z) =
P_0(z) + \sum_{j=1} ^a P_j(z) {\rm Li}_j(1/z) = \textup{O}(z^{-rn-1}) \mbox{ quand }
z \to \infty.$$

Parmi tous les polynômes symétriques $Q_n(k)$ multiples de $(k-rn)_{rn}$ (donc nécessairement aussi multiples de $(k+n+1)_{rn}$), on a intérêt à en prendre un de degré minimal, pour que ${\bf S}_n(1)$ soit aussi petit que possible. Si $a(n+1)$ est impair, le polynôme $(k-rn)_{rn}(k+n+1)_{rn}$ a la bonne parité, et on peut considérer $Q_n(k) = n!^{a-2r} (k-rn)_{rn}(k+n+1)_{rn}$ : on obtient la série hypergéométrique bien équilibrée de [@RivoalCRAS] et [@BR]. Si $a(n+1)$ est pair, pour obtenir le bon signe dans la propriété de symétrie de $Q_n$ on est amené à introduire un facteur $k + \frac{n}{2}$, ce qui donne la série très bien équilibrée du paragraphe 2.2. Dans les deux cas, ${\bf S}_n(z)$ est la solution unique d'un problème de Padé (voir [@Huttner03] et [@FischlerRivoal]).

Plus $a$ est grand (en prenant, pour chaque $a$, la valeur optimale de $r$), plus la forme linéaire à coefficients entiers $d_n ^a {\bf S}_n(1)$ est petite (et la présence, ou l'absence, du facteur $k
+ \frac{n}{2}$ a une influence négligeable sur ce comportement). Donc si on cherche des formes linéaires en 1, $\zeta(3)$, $\zeta(5)$, ..., $\zeta(2\ell+1)$, celles obtenues avec la série très bien équilibrée pour $a = 2\ell+2$ seront meilleures que celles obtenues avec la série bien équilibrée pour $a = 2\ell+1$ et $n$ pair. Ceci n'a aucune influence quand $\ell$ tend vers l'infini, mais peut s'avérer crucial si $\ell$ est fixé (comme dans le théorème 4). En outre, si la conjecture 15 (qui n'a aucun équivalent pour des séries seulement bien équilibrées) est vraie alors il suffit de multiplier ${\bf S}_n(1)$ par $d_n ^{a-1}$, ce qui donne une forme linéaire encore plus petite. Pour $a=4$, on retrouve ainsi les formes linéaires d'Apéry en 1 et $\zeta(3)$ (ce qui n'est pas le cas avec la série bien équilibrée quand $a=3$).

** 23**. *Pour démontrer le théorème 10 on pourrait évaluer les formes linéaires en polylogarithmes en $z = -1$ plutôt qu'en $z=1$. Ceci induit peu de changements. Le plus notable est que $\log(2) = -{\rm Li}_1(-1)$ remplace le divergent ${\rm Li}_1(1)$ ; pour $\ell \geq 2$ on a ${\rm Li}_\ell (-1) = -(1-2^{1-\ell})\zeta(\ell)$.*

*Pour $a=3$ et $z=-1$ les formes linéaires construites au paragraphe 2.3 sont [@Krattenthaler] celles utilisées par Apéry ([@Apery], [@VDP]) pour prouver que $\zeta(2)$ est irrationnel. En particulier $d_n^2$ suffit comme dénominateur des coefficients de cette forme linéaire. Plus généralement, la conjecture 15 devrait être valable aussi quand $a$ est impair et $z = -1$.*

Considérons l'opérateur différentiel hypergéométrique suivant, où $\delta= z\frac{{\rm d}}{{\rm d}z}$ : $${\bf L}= \delta^{a+1} (\delta- \frac{n}2 -1) (\delta- (r+1)n - 1) - z
(\delta-n)^{a+1} (\delta-\frac{n}2+1)(\delta+rn+1).$$ L'écriture de ${\bf S}_n(z)$ comme série hypergéométrique très bien équilibrée montre que ${\bf S}_n(z)$ est une solution de l'équation différentielle ${\bf L}y =0$. Par monodromie on voit, grâce à (eqdcppolylogs), que pour tout $b \in \{1, \ldots, a\}$ la fonction $\sum_{j=b} ^a (-1)^{j-1} P_j(z) \frac{\log^{j-b}(z)}{(j-b)!}$ est aussi une solution de ${\bf L}y =0$. En particulier pour $b=a$ on obtient le polynôme $P_a$, qu'on peut écrire comme polynôme hypergéométrique très bien équilibré (avec un petit abus de langage : ici les paramètres inférieurs $-\frac{n}{2}$ et $-(r+1)n$ sont négatifs, mais la série $_{a+3} F_{a+2}$ est quand même bien définie) :

$$\begin{aligned}
P_a(z) &=& (-1)^{rn} n (rn)! ((r+1)n)! n!^{-2r-1} \times\\
 && _{a+3} F_{a+2} \left(
\begin{array}{cccccc|}
 -n , & -\frac{n}{2}+1 ,& rn + 1,  & -n ,& \ldots,  & -n     \\
     &  -\frac{n}{2},  & -(r+1)n ,& 1 , &  \ldots ,& 1
\end{array}
\, \, \, z \right).
\end{aligned}$$ L'aspect bien équilibré de ce polynôme hypergéométrique lui confère (voir [@Andrews] ou [@AAR], §3.5) la propriété de réciprocité (recipropol). En effet, si $y(z)$ est une solution de l'équation différentielle ${\bf L}
y=0$ alors $z^n y(1/z)$ est aussi une solution de cette même équation. Quant aux autres polynômes $P_{a-1}$, ..., $P_1$, ils s'obtiennent par la méthode de Frobenius (voir [@Ince]) et vérifient, eux aussi, (recipropol). Toutes ces considérations valent aussi pour la série bien équilibrée de [@RivoalCRAS] et [@BR], et permettent [@Huttner03] d'écrire celle-ci comme solution unique d'un problème de Padé.

Un autre intérêt des définitions utilisées dans ce texte est que ${\bf S}_n(1)$ possède (pour $a$ pair) plusieurs représentations intégrales assez simples. Tout d'abord, on a ([@Zudilinservice], Théorème 5) l'intégrale suivante, qui généralise $I_{\mathbb{R},n}(1)$ et les intégrales introduites par Vasilenko [@Vasilenko] et Vasilyev ([@Vasilyevancien], [@Vasilyev]) : $$\label{intvasi}
{\bf S}_n(1) = \frac{(rn)!^2}{n!^{2r}} \int_{[0,1]^{a-1}}
\frac{\prod_{j=1} ^{a-1} x_j ^{rn} (1-x_j)^n}{(Q_{a-1}(x_1,\ldots,
x_{a-1}))^{rn+1}} {\rm d}x_1 \ldots {\rm d}x_{a-1},$$ en posant $Q_{a-1}(x_1,\ldots,x_{a-1}) = 1- x_1 (1- x_2 (
 \ldots (1-x_{a-1})\ldots ))$. Vasilyev a démontré [@Vasilyev] que si $a=6$ et $r=1$ alors cette intégrale s'écrit $\kappa'_0+ \kappa'_3 \zeta(3) + \kappa'_5 \zeta(5)$ avec $d_n ^5 \kappa'_0$, $d_n ^5  \kappa'_3$ et $d_n ^5  \kappa'_5$ entiers. Ceci prouve la conjecture 15 dans ce cas. Il n'est pas évident que $\kappa'_0$, $\kappa'_3$ et $\kappa'_5$ soient les $P_0(1)$, $P_3(1)$ et $P_5(1)$ du paragraphe 2.3, mais cela découle de l'indépendance linéaire conjecturale de $1$, $\zeta(3)$ et $\zeta(5)$.

D'autre part, en appliquant à (intvasi) un théorème de Zlobin [@Zlobin] ou le changement de variables qui figure dans [@SFCRAS] (§2) on obtient l'intégrale suivante, qui ressemble à celles utilisées par Sorokin ([@Sorokinpi], [@SorokinApery]) :

$${\bf S}_n(1) = \frac{(rn)!^2}{n!^{2r}} \int_{[0,1]^{a-1}}
\frac{\prod_{j=1} ^{a-1} x_j ^{rn} (1-x_j)^n {\rm d}x_j}{(1-x_1x_2)^{n+1}
(1-x_1x_2x_3x_4)^{n+1} \ldots (1-x_1\ldots x_{a-2})^{n+1}
(1-x_1\ldots x_{a-1})^{rn+1}}.$$

Il serait intéressant d'arriver à démontrer le théorème 10 en utilisant seulement des intégrales multiples comme celle-ci (ou celle de (intvasi)). Le problème est qu'a priori on s'attend à ce qu'une telle intégrale $(a-1)$-uple soit une forme linéaire, à coefficients rationnels, en les polyzêtas de poids au plus $(a-1)$

(voir [@MiW] et [@Zlobin], Théorème 3). Or le théorème 5 de [@Zudilinservice] montre que ces intégrales sont égales à ${\bf S}_n(1)$, donc seuls 1 et les valeurs de $\zeta$ aux entiers impairs apparaissent.

# Résultats quantitatifs

## Exposant d'irrationalité de $\zeta(3)$

On appelle *exposant d'irrationalité* d'un nombre réel irrationnel $\alpha$, et on note $\mu(\alpha)$, la borne inférieure de l'ensemble des réels $\nu$ pour lesquels il n'existe qu'un nombre fini de nombres rationnels $p/q$ tels que $\vert \alpha - \frac{p}{q} \vert < \frac{1}{q^\nu}$. La théorie des fractions continues ([@HW], §11.1), ou le principe des tiroirs de Dirichlet ([@HW], §11.3), montre qu'un exposant d'irrationalité est toujours supérieur ou égal à 2. Si $\alpha$ est algébrique, Liouville a démontré ([@Liouville] ; voir aussi [@HW], §11.7) que $\mu(\alpha)$ est inférieur ou égal au degré de $\alpha$. Ce résultat a été amélioré par Roth en 1955 : on a $\mu(\alpha) = 2$ pour tout nombre algébrique irrationnel $\alpha$ (voir [@EMS], Chapitre 1, § 7). On a aussi $\mu(\alpha) = 2$ pour presque tout réel $\alpha$, au sens de la mesure de Lebesgue ([@HW], §11.11). À l'opposé, un nombre de Liouville est un nombre dont l'exposant d'irrationalité est infini : il est extrêmement bien approché par des nombres rationnels (un exemple de tel nombre est $\sum_{k \geq 1} \frac{1}{10^{k!}}$).

Les formes linéaires d'Apéry montrent que l'exposant d'irrationalité de $\zeta(3)$ est majoré par $13,4179$ (voir [@EMS], Chapitre 2, §5.6) ; en particulier $\zeta(3)$ n'est pas un nombre de Liouville. Ce résultat a été amélioré notamment

par Hata [@Hata] puis Rhin-Viola, qui ont démontré la meilleure majoration de $\mu(\zeta(3))$ connue à ce jour :

** 24** ([@RV3]). *L'exposant d'irrationalité de $\zeta(3)$ est majoré par $5,5139$, c'est-à-dire qu'il n'existe qu'un nombre fini de nombres rationnels $p/q$ tels que $$\vert \zeta(3) - \frac{p}{q} \vert < \frac{1}{q^{5,5139}}.$$*

Pour obtenir ce résultat, Rhin et Viola considèrent les intégrales suivantes : $$\label{intrv}
J_n= \int_0 ^1 \int_0 ^1 \int_0 ^1
\frac{u^{hn}(1-u)^{ln}v^{kn}(1-v)^{sn}w^{jn}(1-w)^{qn}}{(1-w(1-uv))^{(q+h-r)n+1}}
{\rm d}u \, {\rm d}v \, {\rm d}w,$$ où $h, \ldots, s$ sont des paramètres dont on fixe les valeurs de la manière suivante : $h=16$, $j = 17$, $k =19$, $l =15$, $q=11$, $r=9$, $s=13$. Si on prenait tous ces paramètres égaux à un même entier, on obtiendrait les intégrales du paragraphe 1.3, donc la suite des formes linéaires d'Apéry (ou, plus précisément, une suite extraite), conduisant à la même mesure d'irrationalité. L'intérêt réside donc dans le fait de ne pas prendre tous les paramètres égaux ; l'asymptotique obtenue pour $J_n^{1/n}$ est un peu moins bonne, mais on gagne beaucoup sur les dénominateurs par lesquels il faut multiplier $J_n$ pour obtenir une forme linéaire en 1 et $\zeta(3)$ à coefficients entiers. Ce gain provient de l'action sur des intégrales de la forme (intrv) d'un groupe isomorphe au produit semi-direct $H \rtimes{\mathfrak S}_5$, où $H$ est l'hyperplan d'équation $\varepsilon_1+\ldots+\varepsilon_5=0$ dans $(\mathbb{Z}/ 2 \mathbb{Z})^5$. D'autres interprétations de cette action de groupe se trouvent dans [@Zudilincinqaout] et [@SFCaen].

** 25**. *Les majorations de $\mu(\zeta(3))$ mentionnées ci-dessus sont effectives : on peut donner une majoration explicite de la hauteur $\max(\vert p \vert, \vert q \vert)$ des approximations rationnelles $p/q$ "exceptionnellement bonnes". Ceci contraste avec le théorème de Roth, dans lequel on sait seulement majorer le nombre d'exceptions $p/q$, mais pas leur hauteur.*

## Irrationalité d'un nombre parmi $\zeta(5)$, ..., $\zeta(21)$

Soit $a$ un entier pair, avec $a \geq 6$. Dans ce paragraphe, on construit (en suivant [@vingtetun]) des formes linéaires à coefficients rationnels en 1, $\zeta(5)$, $\zeta(7)$, ..., $\zeta(a+1)$. Si, après multiplication par un dénominateur commun des coefficients, elles tendent vers zéro sans être nulles à partir d'un certain rang, alors l'un au moins des nombres $\zeta(5)$, $\zeta(7)$, ..., $\zeta(a+1)$ est irrationnel ; c'est ce qui va se produire avec $a = 20$. On pose : $${\bf \overline{R}}_n(k) = n!^{a-6}
(k+\frac{n}{2}) \frac{(k-n)_n ^3 (k+n+1)_n ^3}{(k)_{n+1} ^a}$$ et $${\bf \overline{S}}_n(z) = \frac12 \sum_{k=1} ^\infty {\bf \overline{R}}_n''(k) z^{-k}.$$ On développe ${\bf \overline{R}}_n$ en éléments simples, ce qui définit des coefficients $\overline{c}_{i,j}$ (les formules (dcpelsples) et (eqdefcij) restant valables). On définit $\overline{P}_1, \ldots, \overline{P}_a$ à partir des $\overline{c}_{i,j}$ par la relation (eqdefpj) ; seul $\overline{P}_0$ est défini par une formule légèrement différente : $$\overline{P}_0(z) = - \sum_{\ell = 0} ^{n-1} \left( \sum_{i=\ell+1} ^n \sum_{j=1} ^a
\frac{j(j+1)\overline{c}_{i,j}}{2(i-\ell)^{j+2}} \right) z^\ell.$$ On obtient la décomposition suivante exactement comme au paragraphe 2.3.2, mais un décalage se produit car on dérive ${\bf \overline{R}}_n$ (voir le paragraphe 1.4) : $${\bf \overline{S}}_n(z) = \overline{P}_0(z) + \sum_{j=1} ^a \frac{j(j+1)}{2} \,
\, \overline{P}_j (z)
{\rm Li}_{j+2} (1/z).$$ Les arguments du paragraphe 2.3.3 restent valables, et montrent (car $a$ est pair) que ${\bf \overline{S}}_n(1)$ est une forme linéaire à coefficients rationnels en 1, $\zeta(5)$, $\zeta(7)$, ..., $\zeta(a+1)$. De plus un dénominateur commun pour ces coefficients est $2 d_n ^{a+2}$ ; on conjecture ([@theseTanguy], §5.1) que $2 d_n ^{a+1}$ convient aussi. La majoration de ces coefficients (qui est effectuée au paragraphe 2.3.4) est inutile ici : elle servait à appliquer le critère de Nesterenko, dont on n'a pas besoin puisqu'on applique seulement la remarque évidente qu'une forme linéaire, à coefficients entiers, en des rationnels fixés ne peut pas être arbitrairement petite sans être nulle.

Le point délicat de la preuve est l'estimation asymptotique de ${\bf \overline{S}}_n(1)$. En effet, on ne connaı̂t pas d'écriture de ${\bf \overline{S}}_n(1)$ comme intégrale multiple réelle. On utilise donc la méthode du col. Posons

$$K_n(u) = \frac{-1}{2i\pi} \int_{c- i \infty} ^{c + i \infty}
{\bf \overline{R}}_n(s) \left(\frac{\pi}{\sin(\pi s)} \right)^3  e^{us} {\rm d}s,$$ où $c$ est un réel avec $0 < c < n+1$, et $u$ un nombre complexe tel que ${\rm Re}(u) \leq 0$ et $\vert {\rm Im}(u) \vert < 3 \pi$. Cette intégrale est à rapprocher de celle notée $I_{\mathbb{C},n}(z)$ au paragraphe 1.5. On peut appliquer le théorème des résidus, pour faire apparaı̂tre les pôles de l'intégrande qui sont situés aux entiers $n+1$, $n+2$, ...Au voisinage d'un tel entier $k$, on a $(\frac{\pi}{\sin(\pi s)})^3 = \frac{(-1)^k}{(s-k)^3} + \frac{(-1)^k
\pi^2}{2(s-k)} + {\small \textup{O}(s-k)}$. On obtient donc (voir [@Hessami] et [@Zudilincentqc] pour des résultats analogues) : $$K_n(u) = \frac{\pi^2 + u^2}{2}
\sum_{k = n+1} ^\infty {\bf \overline{R}}_n(k) (-e^u)^k +
u  \sum_{k = n+1} ^\infty {\bf \overline{R}}_n' (k) (-e^u)^k +
\frac12 \sum_{k = n+1} ^\infty {\bf \overline{R}}_n'' (k) (-e^u)^k .$$ En choisissant $u=i \pi$, le premier terme disparaı̂t, et on obtient ${\bf \overline{S}}_n(1)
= {\rm Re}(K_n(i \pi))$.

La méthode du col donne ([@vingtetun], Lemme 5) deux nombres complexes non nuls $c_0$ et $\alpha$, qu'on peut calculer, tels que $K_n(i \pi) \sim c_0  n^{-8}
e^{\alpha n}$ quand $n$ tend vers l'infini. Comme la partie imaginaire de $\alpha$ n'est pas un multiple entier de $\pi$, il existe une suite strictement croissante $\varphi(n)$ d'entiers tels que l'argument de $c_0 e^{\alpha \varphi(n)}$, vu modulo $2 \pi$, ait une limite autre que $\pm \pi /
2$. On a alors : $$\lim_{n \to \infty} \vert {\bf \overline{S}}_{\varphi(n)}(1) \vert ^{1/\varphi(n)} =
e^{{\rm Re}(\alpha)}.$$ Le choix $a=20$ donne ${\rm Re}(\alpha) = -22,02\ldots$ d'où ${\rm Re}(\alpha) + a + 2 < 0$. Donc la forme linéaire $d_{\varphi(n)} ^{22} {\bf \overline{S}}_{\varphi(n)}(1)$ en 1, $\zeta(5)$, $\zeta(7)$, ..., $\zeta(21)$, à coefficients entiers, tend vers 0 quand $n$ tend vers l'infini et est non nulle pour $n$ assez grand. Cela montre que l'un au moins parmi $\zeta(5)$, $\zeta(7)$, ..., $\zeta(21)$ est irrationnel.

** 26**. *Si on savait démontrer la conjecture mentionnée ci-dessus (i.e. que $2 d_n ^{a+1} \overline{P}_j(1)$ est un entier pour tout $j$), on pourrait ([@theseTanguy], §5.1) appliquer la même méthode avec $a=18$, et démontrer ainsi que l'un au moins des nombres $\zeta(5)$, $\zeta(7)$, ..., $\zeta(19)$, est irrationnel.*

## Irrationalité d'un nombre parmi $\zeta(5)$, $\zeta(7)$, $\zeta(9)$ et $\zeta(11)$

La structure de la preuve est la même que dans le paragraphe précédent. La différence principale vient de dénominateurs nettement plus petits, grâce à une étude fine de leurs valuations $p$-adiques et à l'utilisation d'une fraction rationnelle modifiée : $$\widetilde{{\bf R}}_n(k) = \frac{\prod_{u=1} ^{10} ((13+2u)n)!}{(27n)!^6}(37n+2k)
\frac{(k-27n)_{27n} ^3 (k+37n+1)_{27n} ^3 }{\prod_{u=1} ^{10}
(k+(12-u)n)_{(13+2u)n+1}}.$$ Pour $\vert z \vert \geq 1$ on pose $\widetilde{{\bf S}}_n(z) = \frac12 \sum_{k=1} ^{\infty} \widetilde{{\bf R}}_n'' (k) z^{-k}$. La décomposition en éléments simples $\widetilde{{\bf R}}_n(k) = \sum_{j=1} ^{10} \sum_{i=(j+1)n} ^{(36-j)n}
\frac{\tilde{c}_{i,j}}{(k+i)^{j}}$ définit les $\tilde{c}_{i,j}$ à partir desquels on construit les polynômes $\widetilde{P}_j(z) =  \sum_{i = (j+1)n} ^{(36-j)n} \tilde{c}_{i,j}z^{i}$ pour $j \in \{1, 2, \ldots, 10\}$ et $$\widetilde{P}_0(z) = - \sum_{\ell=0} ^{35n-1} \left( \sum_{j=1} ^{10} \, \,
\sum_{i=\max((j+1)n,\ell+1)} ^{(36-j)n}
\frac{j(j+1)\tilde{c}_{i,j}}{2(i-\ell)^{j+2}} \right) z^\ell.$$ On a alors $\widetilde{{\bf S}}_n(z) = \widetilde{P}_0(z) + \sum_{j=1} ^{10} \frac{j(j+1)}{2}
\widetilde{P}_j(z) {\rm Li}_{j+2} (1/z)$.

Le problème est de majorer de façon très précise le dénominateur des rationnels $\tilde{c}_{i,j}$. En suivant la méthode

utilisée pour démontrer le lemme 21, on obtiendrait $d_{33n}^{10-j} \tilde{c}_{i,j}\in \mathbb{Z}$ pour tous $i$ et $j$. Une étude fine de la valuation $p$-adique des coefficients binomiaux permet d'obtenir un dénominateur nettement plus petit : on trouve un entier $\Phi_n$ "assez grand" tel que $d_{33n}^{10-j} \Phi_n ^{-1} \tilde{c}_{i,j}\in \mathbb{Z}$. On en déduit directement que $2d_{35n} ^3 d_{34n} d_{33n} ^8 \Phi_n^{-1} \widetilde{P}_j(z)$ est à coefficients entiers pour tout $j \in \{ 0, 1, \ldots, 10\}$.

La symétrie $\widetilde{{\bf R}}_n(-37n-k) = - \widetilde{{\bf R}}_n(k)$ donne $z^{37n} \widetilde{P}_j(1/z) = (-1)^{j+1} \widetilde{P}_j(z)$, d'où $\widetilde{P}_j(1)=0$ pour $j = 2, 4, \ldots, 10$. En outre on a $\widetilde{P}_1(1)=0$ car $\widetilde{{\bf R}}_n(k) = \textup{O}(k^{-2})$ quand $k$ tend vers l'infini. Donc $\widetilde{{\bf S}}_n(1)$ est une forme linéaire en 1, $\zeta(5)$, $\zeta(7)$, $\zeta(9)$ et $\zeta(11)$. Pour l'estimer, et démontrer qu'elle est non nulle pour une infinité de $n$, on transforme $\widetilde{{\bf S}}_n(1)$ en une intégrale complexe, à laquelle on applique la méthode du col (voir [@Zudilincentqc], §2). On obtient les comportements asymptotiques suivants quand $n$ tend vers l'infini : $\limsup \vert \widetilde{{\bf S}}_n(1) \vert ^{1/n} \leq e^{-227,58...}$, $\limsup \vert \Phi_n ^{-1} \vert ^{1/n} \leq e^{-176,75...}$ et $(d_{35n} ^3 d_{34n} d_{33n} ^8)
^{1/n} \to e^{403}$. Comme $403 < 227,58 +176,75$ on obtient la conclusion cherchée.

** 27**. *Zudilin conjecture ([@Zudilincinqaout], §9) que des compensations ont lieu quand $z=1$, ce qui permettrait de trouver un dénominateur plus petit pour les $P_j(1)$. Peut-être pourrait-on alors démontrer que parmi $\zeta(5)$, $\zeta(7)$ et $\zeta(9)$ l'un au moins est irrationnel.*

** 28**. *En utilisant des méthodes similaires, on peut démontrer [@Zudilincentqc] que pour tout $\ell \geq 1$ impair l'un au moins des nombres $\zeta(\ell +2)$, $\zeta(\ell+4)$, ..., $\zeta(8 \ell -1)$, est irrationnel.*

AAR

[S. Ahlgren] et [K. Ono] -- *A Gaussian hypergeometric series evaluation and Apéry number congruences*, J. Reine Angew. Math. 518 (2000), 187-212. [G. Almkvist] et [A. Granville] -- *Borwein and Bradley's Apéry-like formulae for $\zeta(4n+3)$*, Experiment. Math. 8.2 (1999), 197-203. [Y. André] -- *$G$-functions and geometry*, Aspects of Math. E13, Vieweg, 1989. [R. André-Jeannin] -- *Irrationalité de la somme des inverses de certaines suites récurrentes*, C. R. Acad. Sci. Paris, Ser. I 308 (1989), 539-541. [G.E. Andrews] -- *The well-poised thread: an organized chronicle of some amazing summations and their implications*, Ramanujan J. 1.1 (1997), 7-23. [G.E. Andrews, R. Askey] et [R. Roy] -- *Special Functions*, The Encyclopedia of Mathematics and its Applications 71 (G.-C. Rota ed.), Cambridge University Press, Cambridge, 1999. [R. Apéry] -- *Irrationalité de $\zeta(2)$ et $\zeta(3)$*, in: Journées Arithmétiques (Luminy, 1978), Astérisque 61 (1979), 11-13. [R. Apéry] -- *Interpolation de fractions continues et irrationalité de certaines constantes*, in: Comité des Travaux Historiques et Scientifiques (CTHS), Bulletin de la Section des Sciences III (Mathématiques), Bibliothèque Nationale, Paris, 1981, 37-53. [R. Askey] et [J.A. Wilson] -- *A recursive relation generalizing those of Apéry*, J. Austral. Math. Soc. 36 (1984), 267-278. [W. Van Assche] -- *Approximation theory and analytic number theory*, in: Special Functions and Differential Equations (Madras, 1997), Allied Publishers, New Delhi, 1998, 336-355.

[K.M. Ball] et [T. Rivoal] -- *Irrationalité d'une infinité de valeurs de la fonction zêta aux entiers impairs*, Invent. Math. 146.1 (2001), 193-207. [C. Batut] et [M. Olivier] -- *Sur l'accélération de la convergence de certaines fractions continues*, Sém. de Théorie des Nombres de Bordeaux 1979-1980, exp. no. 23 (25 p.). [F. Beukers] -- *A note on the irrationality of $\zeta(2)$ and $\zeta(3)$*, Bull. London Math. Soc. 11.3 (1979), 268-272. [F. Beukers] -- *Padé-approximations in number theory*, in: Padé approximation and its applications (Amsterdam, 1980), Lecture Notes in Math. 888, Springer, 1981, 90-99. [F. Beukers] -- *The values of polylogarithms*, in: Topics in classical number theory (Budapest, 1981), Colloq. Math. Soc. János Bolyai 34, 1984, 219-228. [F. Beukers] -- *Irrationality of $\pi^2$, periods of an elliptic curve and $\Gamma_1(5)$*, in: Approximations diophantiennes et nombres transcendants (Luminy, 1982), D. Bertrand et M. Waldschmidt eds., Progress in Math. 31, Birkhäuser, 1983, 47-66.

[F. Beukers] -- *Some congruences for the Apéry numbers*, J. Number Th. 21 (1985), 141-155. [F. Beukers] -- *Irrationality proofs using modular forms*, in: Journées Arithmétiques (Besançon, 1985), Astérisque 147-148 (1987), 271-283. [F. Beukers] -- *Another Congruence for the Apéry Numbers*, J. Number Th. 25 (1987), 201-210.

[F. Beukers] et [C.A.M. Peters] -- *A family of K3 surfaces and $\zeta(3)$*, J. Reine Angew. Math. 351 (1984), 42-54. [J. Borwein] et [D. Bradley] -- *Empirically determined Apéry-like formulae for $\zeta(4n+3)$*, Experiment. Math. 6 (1997), 181-194. [P. Borwein] et [T. Erdélyi] -- *Polynomials and Polynomial inequalities*, Graduate Texts in Math. 161, Springer, 1995. [P. Bundschuh] et [K. Väänänen] -- *Arithmetical investigations of a certain infinite product*, Compositio Math. 91 (1994), 175-199.

[P. Cartier] -- *Démonstration automatique d'identités et fonctions hypergéométriques (d'après Zeilberger)*, Sém. Bourbaki 1991-92, exp. no. 746, Astérisque 206 (1992), 41-91. [P. Cartier] -- *Fonctions polylogarithmes, nombres polyzêtas et groupes pro-unipotents*, Sém. Bourbaki 2000-01, exp. no. 885, à paraı̂tre dans Astérisque. [S. Chowla, J. Cowles] et [M. Cowles] -- *Congruence properties of Apéry numbers*, J. Number Th. 12 (1980), 188-190. [G.V. Chudnovsky] -- *Transcendental numbers*, in: Number theory, Proc. Southern Illinois Conf. (Carbondale, 1979), Lecture Notes in Math. 751, Springer, 45-69. [H. Cohen] -- *Démonstration de l'irrationalité de $\zeta(3)$ (d'après Apéry)*, Sém. de Théorie des Nombres de Grenoble, octobre 1978 (9 p.). [H. Cohen] -- *Généralisation d'une construction de R. Apéry*, Bull. Soc. Math. France 109 (1981), 269-281. [P. Colmez] -- *Arithmétique de la fonction zêta*, Journées X-UPS 2002, à paraı̂tre.

[J. Dieudonné] -- *Calcul infinitésimal*, Collection Méthodes, Hermann, 1968.

[B. Dwork] -- *On Apéry's differential operator*, Groupe d'étude d'analyse ultramétrique 1979-1981, exp. no. 25 (6 p.). [B. Dwork] -- *Arithmetic theory of differential equations*, Symposia Math. 24 (INDAM, Rome, 1979), Academic Press, 1981, 225-243. [B. Dwork, G. Gerotto] et [F.J. Sullivan] -- *An introduction to $G$-functions*, Annals of Math. Studies 133, Princeton Univ. Press, 1994.

[N.I. Fel'dman] et [Yu.V. Nesterenko] -- *Number Theory IV, Transcendental Numbers*, A.N. Parshin et I.R. Shafarevich eds., Encyclopaedia of Mathematical Sciences 44, Springer, 1998. [S. Fischler] -- *Formes linéaires en polyzêtas et intégrales multiples*, C. R. Acad. Sci. Paris, Ser. I 335.1 (2002), 1-4. [S. Fischler] -- *Groupes de Rhin-Viola et intégrales multiples*, Actes des Rencontres Arithmétiques de Caen (juin 2001), soumis au J. Théor. Nombres Bordeaux. [S. Fischler] et [T. Rivoal] -- *Approximants de Padé et séries hypergéométriques équilibrées*, Rapport de recherche 2002-27, LMNO, Université de Caen ; à paraı̂tre au J. Math. Pures Appl.

[A.O. Gel'fond] -- *Calcul des différences finies*, Dunod, 1963. [I. Gessel] -- *Some congruences for Apéry numbers*, J. Number Th. 14 (1982), 362-368. [L.A. Gutnik] -- *The irrationality of certain quantities involving $\zeta(3)$*, Uspekhi Mat. Nauk \[Russian Math. Surveys\] 34.3 (1979), 190 [200]. [L.A. Gutnik] -- *On the irrationality of some quantities containing $\zeta(3)$*, Acta Arith. 42.3 (1983), 255-264 (en russe) ; traduction dans Amer. Math. Soc. Transl. 140 (1988), 45-55.

[L. Habsieger] -- *Introduction to diophantine approximation*, en préparation. [G.H. Hardy] et [E.M. Wright] -- *An introduction to the theory of numbers*, 3ème édition, Oxford Univ. Press, 1954. [M. Hata] -- *On the linear independence of the values of polylogarithmic functions*, J. Math. Pures Appl. 69.2 (1990), 133-173. [M. Hata] -- *Rational approximations to the dilogarithm*, Trans. Amer. Math. Soc. 336.1 (1993), 363-387. [M. Hata] -- *A new irrationality measure for $\zeta(3)$*, Acta Arith. 92.1 (2000), 47-57. [M. Hazewinkel] -- *Formal groups and applications*, Pure and Applied Mathematics 78, Academic Press, 1978. [T.G. Hessami Pilehrood] -- *Linear independence of vectors with polylogarithmic coordinates*, Vestnik Moskov. Univ. Ser. I Mat. Mekh. no. 6 \[Moscow Univ. Math. Bull. 54.6\] (1999), 54-56 \[40-42\].

[M. Huttner] -- *Équations différentielles fuchsiennes. Approximations du dilogarithme, de $\zeta(2)$ et de $\zeta(3)$*, Pub. IRMA Lille 43 (1997). [M. Huttner] -- *Constructible sets of linear differential equations and effective rational approximations of $G$-functions*, Pub. IRMA Lille 59 (2002).

[E.L. Ince] -- *Ordinary differential equations*, Dover Publ., 1926. [A.E. Ingham] -- *The distribution of prime numbers*, Cambridge Univ. Press, 1932. [T. Ishikawa] -- *On Beukers' conjecture*, Kobe J. Math. 6 (1989), 49-52.

[M. Koecher] -- *Letter*, Math. Intelligencer 2 (1980), 62-64.

[C. Krattenthaler] -- Communication personnelle, 28 Octobre 2002.

[S. Lang] -- *Algebra*, 3ème édition, Addison-Wesley, 1993. [D. Leshchiner] -- *Some new identities for $\zeta(k)$*, J. Number Th. 13 (1981), 355-362. [J. Liouville] -- *Sur des classes très étendues de quantités dont la valeur n'est ni algébrique, ni même réductible à des irrationnelles algébriques*, J. Math. Pures Appl. 16 (1851), 133-142. [Y.L. Luke] -- *The special functions and their approximations*, Volume I, Mathematics in Science and Engineering 53, Academic Press, 1969.

[M. Mendès-France] -- *Roger Apéry et l'irrationnel*, La Recherche 97 (1979), 170-172.

[Yu.V. Nesterenko] -- *On the linear independence of numbers*, Vestnik Moskov. Univ. Ser. I Mat. Mekh. no. 1 \[Moscow Univ. Math. Bull. 40.1\] (1985), 46-49 \[69-74\]. [Yu.V. Nesterenko] -- *A few remarks on $\zeta (3)$*, Mat. Zametki \[Math. Notes\] 59.6 (1996), 865-880 \[625-636\].

[Yu.V. Nesterenko] -- *Integral identities and constructions of approximations to zeta-values*, Actes des Rencontres Arithmétiques de Caen (juin 2001), soumis au J. Théor. Nombres Bordeaux. [E.M. Nikishin] -- *On the irrationality of the values of the functions F(x,s)*, Mat. Sbornik 109.3 \[Math. USSR-Sb. 37.3\] (1979), 410-417 \[381-388\]. [E.M. Nikishin] et [V.N. Sorokin] -- *Rational approximations and orthogonality*, Translations of Math. Monographs 92, Amer. Math. Soc., 1991. [I. Niven, H.S. Zuckerman] et [H.L. Montgomery] -- *An introduction to the theory of numbers*, 5ème édition, J. Wiley, 2000.

[J. Oesterlé] -- *Polylogarithmes*, Sém. Bourbaki 1992-93, exp. no. 762, Astérisque 216 (1993), 49-67.

[C. Peters] et [J. Stienstra] -- *A pencil of K3-surfaces related to Apéry's recurrence for $\zeta(3)$ and Fermi surfaces for potential zero*, in: Arithmetics of complex manifolds (Erlangen, 1988), W.P. Barth et H. Lange eds., Lecture Notes in Math. 1399, Springer, 110-127. [M. Petkovšek, H.S. Wilf] et [D. Zeilberger] -- *A=B*, A.K. Peters, 1996. [A. Van Der Poorten] -- *A proof that Euler missed\... Apéry's proof of the irrationality of $\zeta (3)$*, Math. Intelligencer 1.4 (1978/79), 195-203. [A. Van Der Poorten] -- *Some wonderful formulae\... footnotes to Apéry's proof of the irrationality of $\zeta(3)$*, Sém. Delange-Pisot-Poitou, 20e année, 1978-79, no. 29 (7p.). [A. Van Der Poorten] -- *Some wonderful formulas \... an introduction to polylogarithms*, in: Proceedings of the Queen's Number Theory Conference (Kingston, 1979), Queen's Papers in Pure and Applied Mathematics 54, 1980, 269-286. [M. Prevost] -- *A new proof of the irrationality of $\zeta(2)$ and $\zeta(3)$ using Padé approximants*, J. Comp. Appl. Math. 67 (1996), 219-235. [M. Prevost] -- *On the irrationality of $\sum \frac{t^n}{A \alpha^n+B \beta^n}$*, J. Number Th. 73 (1998), 139-161.

[E. Reyssat] -- *Irrationalité de $\zeta(3)$ selon Apéry*, Sém. Delange-Pisot-Poitou, 20e année, 1978-79, no. 6 (6 p.). [E. Reyssat] -- *Mesures de transcendance pour les logarithmes de nombres rationnels*, in: Approximations diophantiennes et nombres transcendants (Luminy, 1982), D. Bertrand et M. Waldschmidt eds., Progress in Math. 31, Birkhäuser, 1983, 235-245.

[G. Rhin] et [C. Viola] -- *The group structure for $\zeta(3)$*, Acta Arith. 97.3 (2001), 269-293. [T. Rivoal] -- *La fonction zêta de Riemann prend une infinité de valeurs irrationnelles aux entiers impairs*, C. R. Acad. Sci. Paris, Sér. I 331.4 (2000), 267-270. [T. Rivoal] -- *Propriétés diophantiennes des valeurs de la fonction zêta de Riemann aux entiers impairs*, thèse de doctorat, Univ. de Caen (2001). Disponible sur `http://theses-EN-ligne.in2p3.fr`. [T. Rivoal] -- *Irrationalité d'au moins un des neuf nombres $\zeta(5)$, $\zeta(7)$, ..., $\zeta(21)$*, Acta Arith. 103.2 (2002), 157-167. [T. Rivoal] -- *Séries hypergéométriques et irrationalité des valeurs de la fonction zêta de Riemann*, Actes des Journées Arithmétiques de Lille (juillet 2001), à paraı̂tre au J. Théor. Nombres Bordeaux. [T. Rivoal] et [W. Zudilin] -- *Diophantine properties of numbers related to Catalan's constant*, Prépublication 315 de l'Institut de Mathématiques de Jussieu (janvier 2002), Univ. Paris 6, soumis.

[J.P. Serre] -- *Cours d'arithmétique*, Presses Univ. de France, 1970. [L.J. Slater] -- *Generalized hypergeometric functions*, Cambridge Univ. Press, 1966. [V.N. Sorokin] -- *Hermite-Padé approximations for Nikishin systems and the irrationality of $\zeta(3)$*, Uspekhi Mat. Nauk \[Russian Math. Surveys\] 49.2 (1994), 167-168 \[176-177\]. [V.N. Sorokin] -- *A transcendence measure for $\pi^2$*, Mat. Sbornik \[Sb. Math.\] 187.12 (1996), 87-120 \[1819-1852\]. [V.N. Sorokin] -- *Apéry's theorem*, Vestnik Moskov. Univ. Ser. I Mat. Mekh. no. 3 \[Moscow Univ. Math. Bull. 53.3\] (1998), 48-53 \[48-52\]. [J. Stienstra] et [F. Beukers] -- *On the Picard-Fuchs equation and the formal Brauer group of certain elliptic K3-surfaces*, Math. Ann. 271 (1985), 269-304. [B. Sury] -- *On a conjecture of Chowla *et al.**, J. Number Th. 72 (1998), 137-139.

[O.N. Vasilenko] -- *Certain formulae for values of the Riemann zeta function at integral points*, in: Number theory and its applications, Proceedings of the science-theoretical conference (Tashkent, 1990), p. 27 (en russe). [D.V. Vasilyev] -- *Some formulas for Riemann zeta-function at integer points*, Vestnik Moskov. Univ. Ser. I Mat. Mekh. no. 1 \[Moscow Univ. Math. Bull. 51.1\] (1996), 81-84 \[41-43\]. [D.V. Vasilyev] -- *On small linear forms for the values of the Riemann zeta-function at odd integers* (en russe), Doklady NAN Belarusi (Reports of the Belarus National Academy of Sciences) 45.5 (2001), 36-40.

[M. Waldschmidt] -- *Valeurs zêta multiples : une introduction*, J. Théor. Nombres Bordeaux 12.2 (2000), 581-595.

[A. Weil] -- *Remarks on Hecke's lemma and its use*, in: Oeuvres scientifiques - Collected Papers III, Springer, 1979, 405-412. [E.T. Whittaker] et [G.N. Watson] -- *A course of modern analysis*, 4ème édition, Cambridge Univ. Press, 1927.

[D. Zagier] -- *Introduction to modular forms*, in: From number theory to physics (Les Houches, 1989), M. Waldschmidt, P. Moussa, J.M. Luck et C. Itzykson eds., Springer, 1992, 238-291. [D. Zagier] -- Cours au Collège de France, mai 2001. [D. Zeilberger] -- *Closed form (pun intended !)*, in: A tribute to Emil Grosswald: Number theory and related analysis, Comtemporary Math. 143 (M. Knopp et M. Sheingorn eds.), Amer. Math. Soc., 1993, 579-607. [D. Zeilberger] -- *Computerized deconstruction*, à paraı̂tre dans Adv. Applied Math. [S.A. Zlobin] -- *Integrals expressible as linear forms in generalized polylogarithms*, Mat. Zametki \[Math. Notes\] 71.5 (2002), 782-787 \[711-716\]. [W. Zudilin] -- *One of the numbers $\zeta(5)$, $\zeta(7)$, $\zeta(9)$, $\zeta(11)$ is irrational*, Uspekhi Mat. Nauk \[Russian Math. Surveys\] 56.4 (2001), 149-150 \[774-776\]. [W. Zudilin] -- *Irrationality of values of the Riemann zeta function*, Izvestiya RAN Ser. Mat. \[Izv. Math.\] 66.3 (2002), 49-102 \[489-542\]. [W. Zudilin] -- *Well-poised hypergeometric service for diophantine problems of zeta values*, Actes des Rencontres Arithmétiques de Caen (juin 2001), soumis au J. Théor. Nombres Bordeaux. [W. Zudilin] -- *Arithmetic of linear forms involving odd zeta values*, preprint, `math.NT/0206176`.

[W. Zudilin] -- *An elementary proof of Apéry's theorem*, preprint, `math.NT/0202159`.

Stéphane Fischler

Département de Mathématiques et Applications

École Normale Supérieure

45, rue d'Ulm

75230 Paris Cedex 05, France

fischler@dma.ens.fr

http://www.dma.ens.fr/$\sim$fischler/

[^1]: Voir cependant la remarque 23.

[^2]: Sauf pour démontrer le théorème 13 ; pour ce dernier, le polynôme $Q_n(k) = (k-rn)_{rn}$ convient aussi. C'est celui qui est utilisé dans le Chapitre 2 de [@theseTanguy].
