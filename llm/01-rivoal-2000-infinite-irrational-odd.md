---
title: "La fonction Zeta de Riemann prend une infinite de valeurs irrationnelles aux entiers impairs"
authors:
  - "Tanguy Rivoal"
arxiv_id: "math/0008051v1"
arxiv_url: "https://arxiv.org/abs/math/0008051"
published: "2000-08-07"
journal_ref: ""
doi: "10.1016/S0764-4442(00)01624-4"
source: "papers/01-rivoal-2000-infinite-irrational-odd/Notecras.tex"
conversion: pandoc-repaired
---

# La fonction Zeta de Riemann prend une infinite de valeurs irrationnelles aux entiers impairs

**Tanguy Rivoal**

## Abstract

We provide a lower bound for the dimension of the vector space spanned by 1 and by the values of the Riemann Zeta function at the first odd integers. As a consequence, the Zeta function takes infinitely many irrational values at odd integers.

---
Théorie des Nombres/*Theory of Numbers*

**La fonction Zêta de Riemann prend une infinité\
de valeurs irrationnelles aux entiers impairs.**

Tanguy Rivoal

**Résumé -** Nous montrons que la dimension de l'espace vectoriel engendré sur les rationnels par 1 et les n premières valeurs de la fonction Zêta de Riemann aux entiers impairs croı̂t au moins comme un multiple de log(n). Il en résulte l'irrationalité d'une infinité de valeurs de la fonction Zêta aux entiers impairs.

**There are infinitely many irrational values of\
the Riemann Zeta function at odd integers.**

**Abstract -** We provide a lower bound for the dimension of the vector space spanned over the rationals by 1 and by the values of the Riemann Zeta function at the first n odd integers. We prove that this dimension increases at least like a constant times log(n). As a consequence, the Zeta function takes infinitely many irrational values at odd integers.\

Hormis l'irrationalité de $\zeta(3)$, démontrée par R. Apéry [1], peu de résultats sont connus sur la nature arithmétique des nombres $\zeta(2n+1)=\sum_{k\ge 1}1/k^{2n+1}$ ($n$ entier $\ge 1$). Dans cette note, nous esquissons la démonstration du théorème suivant, dont découle l'irrationalité d'une infinité de $\zeta(2n+1)$ :

**THÉORÈME 1**. *Pour tout $\varepsilon>0$, il existe un entier $N(\varepsilon)$ tel que si $n>N(\varepsilon)$,*

$$\text{dim}_{{\fam\msbfam\relax Q}}\left({\fam\msbfam\relax Q}\,+{\fam\msbfam\relax Q}\;\zeta(3)
+\cdots+{\fam\msbfam\relax Q}\;\zeta(2n-1)+{\fam\msbfam\relax Q}\;\zeta(2n+1)\right)\geq
\frac{(1-\varepsilon)}{1+\log(2)}\log(n).$$ La démonstration s'inspire du travail de Nikishin [7] sur les approximants de Padé de type I des fonctions polylogarithmes $L_n(z)=\sum_{k\ge 0}z^k/(k+1)^n$ (pour $z\in{\fam\msbfam\relax C}\;$, $|z|<1$). De façon plus précise, ayant fixé des entiers $a$ et $b$ tels que $1\le b\le a$, il détermine, pour $|z|>1$, des polynômes $Q_{i,n}(z)$ de degré $\le n$ si $i=1,\ldots,\, b$ et de degré $\le n-1$ si $i=0,\, b+1,\ldots,\, a$, tels que l'ordre en $z=\infty$ de la fonction $$N_{n,a,b}(z)=Q_{0,n}(z)+\displaystyle\sum_{i=1}^a Q_{i,n}(z)L_i(1/z)$$ soit au moins $an+b-1$ . En particulier, il obtient la formule explicite $$N_{n,a,b}(z)=\sum_{k=0}^{+\infty}
\frac{k(k-1)\cdots(k-an-b+2)}{(k+1)^a(k+2)^a\cdots(k+n)^a(k+n+1)^b}z^{-k}$$ ce qui lui permet de montrer que si $p/q\in{\fam\msbfam\relax Q}$ est tel que $|q|>|p|^a(4a)^{a(a-1)}$, alors les nombres $1$, $L_1(p/q),\ldots,L_a(p/q)$ sont linéairement indépendants sur ${\fam\msbfam\relax Q}$. Malheureusement les approximations de Nikishin, spécialisées en $z=-1$ et $b=a$, permettent seulement de montrer qu'il y a au moins un irrationnel parmi les nombres $\log(2)$, $\zeta(2)$, $\zeta(3),\ldots,\zeta(a)$ (ce qui résulte a priori de la transcendance de $\log(2)$, par exemple).\
Pour améliorer ce résultat, on pourrait modifier la série $N_{n,a,a}(z)$ en introduisant un paramètre $r$ conduisant à de meilleures estimations sur la croissance des coefficients de la combinaison linéaire des valeurs de la fonction Zêta. Un choix convenable de $r$ montrerait alors que la dimension $D(a)$ de l'espace vectoriel engendré sur ${\fam\msbfam\relax Q}$ par $1,\zeta(2),
\zeta(3),\ldots,\zeta(a)$ est au moins $c_0 \log(a)$ (où $c_0$ est une constante effective). Cependant la formule d'Euler $\zeta(2n)=2^{2n-1}B_n\pi^{2n}/(2n)!$ et la transcendance de $\pi$ impliquent que $D(a)\ge a/2$ : pour obtenir le Théorème 1, il s'agit donc d'éliminer les nombres $\zeta(2n)$. Dans le cas de $\zeta(2),
\zeta(3)$ et $\zeta(4)$, K. Ball [1] a construit la série $$B_n=n!^2\sum_{k=1}^{+\infty}
\left(k+\frac{n}{2}\right)
\frac{(k-1)\cdots(k-n)(k+n+1)\cdots(k+2n)}{k^4(k+1)^4\cdots (k+n)^4}$$ dont la forme particulière permet en effet d'éliminer $\zeta(2)$ et $\zeta(4)$. Dans un message à l'auteur, K. Ball indiquait que sa formule était \<\< facilement généralisable à $\zeta(5)$ et ainsi de suite \>\> [2]. Nous généraliserons ici les séries de Nikishin et Ball en considérant la série (convergente pour $|z|\ge 1$) $$\begin{aligned}
S_n(z)&=&\sum_{k=0}^{+\infty} n!^{a-2r}
\frac{(k-rn+1)_{rn}(k+n+2)_{rn}}{(k+1)_{n+1}^a}z^{-k}
=\sum_{k=0}^{+\infty}R_{n}(k)z^{-k}
\end{aligned}$$ où $n$, $r$ et $a$ sont des entiers vérifiant $1\leq r< a/2$, $n\in{\fam\msbfam\relax N}\,$ et où $(\alpha)_k$ est le symbole de Pochammer : $(\alpha)_0=1$ et $(\alpha)_k=\alpha(\alpha+1)\cdots(\alpha+k-1)$ si $k=1, 2,\ldots$.\
Ces séries, spécialisées en $z=1$, donneront des combinaisons linéaires à coefficients rationnels des Zêta impairs. Moyennant un bon choix de $r$, ces combinaisons auront une décroissance rapide vers $0$ et leurs coefficients auront des dénominateurs et une croissance bien contrôlés. Le Théorème 1 découlera alors du résultat suivant, dû à Y. Nesterenko [6] :\
Considérons $N$ réels $\theta_1,\theta_2,\ldots,\theta_N$ ($N\geq 2$) et supposons qu'il existe $N$ suites d'entiers $(p_{i,n})_{n\geq 0}$ tels que :

-   $\log\left|\sum_{i=1}^N p_{i,n}\theta_i\right|=
    n\log(\alpha)+o(n)$ avec $0<\alpha<1$ ;

-   $\forall i=1,\ldots,N$, $\log|p_{i,n}|\leq n\log(\beta)+o(n)$ avec $\beta>1$.

Dans ces conditions, $\text{dim}_{{\fam\msbfam\relax Q}}({\fam\msbfam\relax Q}\;\theta_1+{\fam\msbfam\relax Q}\;
\theta_2+\cdots+{\fam\msbfam\relax Q}\;\theta_N)\geq 1-\log(\alpha)/\log(\beta)$.\
Je tiens à remercier vivement le professeur K. Ball : sans les fructueux échanges que nous avons eus autour de sa série, cet article n'aurait pu voir le jour. Je tiens également à exprimer toute ma gratitude aux professeurs F. Amoroso et M. Waldschmidt pour leurs précieux conseils et leur soutien constant.\

Pour $i=1,\ldots,a$, $j=0,\ldots,n$, définissons les nombres rationnels $c_{i,j,n}=D_{a-i}\left(R_{n}(t)(t+j+1)^a\right)_{\vert t=-j-1}\;$ où $D_{\lambda}=\frac{1}{\lambda!}d^{\lambda}/dt^{\lambda}$ et les polynômes\
$P_{0,n}(z)=-
\displaystyle\sum_{i=1}^a
\displaystyle\sum_{j=1}^n c_{i,j,n}
\displaystyle\sum_{k=0}^{j-1}\frac{1}{(k+1)^i} z^{j-k}$ et $P_{i,n}(z)=\displaystyle\sum_{j=0}^n c_{i,j,n} z^j \quad(i=1,\ldots,a)$.\

**LEMME 1**. *Si $n$ est pair et $a$ impair $\geq 3$, alors $$S_n(1)=P_{0,n}(1)+\sum_{i=1}^{(a-1)/2} P_{2i+1,n}(1)\zeta(2i+1).$$*

*Preuve.* - En décomposant $R_{n}(t)$ en fractions partielles, on a $$R_{n}(t)= \displaystyle\sum_{i=1}^a\displaystyle\sum_{j=0}^n
\displaystyle\frac{c_{i,j,n}}{(t+j+1)^i}.$$ D'où si $|z|>1$, $$S_{n}(z)=P_{0,n}(z)+\displaystyle\sum_{i=1}^a P_{i,n}(z)L_i(1/z).$$ La convergence de la série $S_{n}(1)$ implique que $\displaystyle \lim_{{z\to 1\atop |z|>1}}(P_{1,n}(z)L_1(1/z))=0$. On peut écrire $c_{i,j,n}=(-1)^{a-i}D_{a-i}(\Phi_{n,j}(x))_{\vert x=j}$ où $\Phi_{n,j}(x)=R_{n}(-x-1)(j-x)^a$ : en appliquant l'identité $(\alpha)_l
=(-1)^l(-\alpha-l+1)_l$, on montre que $$\Phi_{n,n-j}(n-x)=(-1)^{na}\Phi_{n,j}(x).$$ Donc pour tout $k\geq 0$, $\Phi_{n,n-j}^{(k)}(n-x)=(-1)^k(-1)^{na}\Phi_{n,j}^{(k)}(x)$ : en particulier avec $k=a-i$ et $x=j$, on a $c_{i,n-j,n}=(-1)^{a-i}(-1)^{an}
c_{i,j,n}$, d'où $$P_{i,n}(1)=(-1)^{(n+1)a+i}P_{i,n}(1).$$ Si $n$ est pair et $a$ impair, on en déduit que pour tout $i$ pair, $P_{i,n}(1)=0$.\
Le Lemme suivant donne une expression intégrale similaire à celles de Beukers [4] (voir aussi [5], §1.3).

**LEMME 2**. *La série $S_{n}(z)$ admet la représentation intégrale, pour $|z|\ge 1$ : $$\begin{aligned}
S_{n}(z)=\frac{((2r+1)n+1)!}{n!^{2r+1}z^{-(r+1)n-2}}
\int_{[0,1]^{a+1}}\left(\frac{\prod_{i=1}^{a+1}x_i^{r}(1-x_i)}
{(z-x_1x_2\cdots x_{a+1})^{2r+1}}\right)^n
\frac{dx_1dx_2\cdots dx_{a+1}}{(z-x_1x_2\cdots x_{a+1})^2}.
\end{aligned}$$*

*Preuve.* - Si $|z|>1$, cette égalité s'obtient en développant en série entière le dénominateur de la fraction sous le signe intégral, l'interversion des signes somme et intégral étant alors justifiée. En utilisant un argument de continuité, on montre que l'égalité reste valable si $|z|=1$.\
Cette représentation intégrale permet alors d'estimer la décroissance des nombres $S_n(1)$ :

**LEMME 3**. *La limite $s_{r,a}=\displaystyle \lim_{n\to+\infty}\left
\vert S_{n}(1)\right\vert^{1/n}$ existe et vérifie $$\begin{aligned}
s_{r,a}\le
(2r+1)^{2r+1}\frac{(ra+r)^{ra+r}(a-2r)^{a-2r}}{(ra+a-r)^{ra+a-r}}.
\end{aligned}$$*

Pour estimer la croissance des nombres $P_{i,n}(1)$, il suffit de majorer convenablement les coefficients $c_{l,j,n}$ au moyen de la formule de Cauchy $$c_{l,j,n}=\frac{1}{2i\pi}\int_{\vert z+j+1\vert =1/2}R_n(z)(z+j+1)^{l-1}dz$$ où $\vert z+j+1\vert =1/2$ désigne le cercle de centre $-j-1$ et de rayon $1/2$. On obtient alors le

**LEMME 4**. *Pour tout $i=0,\ldots,a$, on a $\displaystyle\limsup_{n\to+\infty}\left\vert P_{i,n}(1)\right\vert^{1/n}
\leq 2^{a-2r}(2r+1)^{2r+1}.$*

Enfin, pour construire des combinaisons linéaires à coefficients entiers, il reste à déterminer les dénominateurs des nombres $P_{i,n}(1)$, ce qui résulte du

**LEMME 5**. *On pose $d_n=\text{ppcm}(1,2,\ldots,n)$. Alors pour $i=0,\ldots,a$, $d_n^{a-i}P_{i,n}(1)\in{\fam\msbfam\relax Z}$.*

*Preuve.* - Il s'agit d'évaluer le dénominateur commun des coefficients $c_{i,j,n}$. Pour cela, fixons $n$ et $j$ et décomposons le numérateur de $R_{n}(t)$ en $2r$ produits de $n$ facteurs consécutifs : on a $R_n(t)(t+j+1)^a=F_{1}(t)\cdots F_{r}(t) G_{1}(t)\cdots G_{r}(t)
H(t)^{a-2r}$ où $$F_{l}(t)=\displaystyle\frac{(t-nl+1)_n}{(t+1)_{n+1}}(t+j+1)\,,\;
G_{l}(t)=\displaystyle\frac{(t+nl+2)_n}{(t+1)_{n+1}}(t+j+1)\,,\;
H(t)=\displaystyle\frac{n!(t+j+1)}{(t+1)_{n+1}}.$$ En décomposant $F_{l}(t)$, $G_{l}(t)$ et $H(t)$ en fractions partielles, on montre que pour tout entier $\lambda\geq 0$, $d_n^{\lambda}(D_{\lambda}F_l)_{\vert t=-j-1}$, $d_n^{\lambda}(D_{\lambda}G_l)_{\vert t=-j-1}$ et $d_n^{\lambda}(D_{\lambda}H_l)_{\vert t=-j-1}$ sont des entiers. Grâce à la formule de Leibniz, on en déduit que $d_n^{a-i}c_{i,j,n}\in{\fam\msbfam\relax Z}$ et donc $d_n^{a-i}P_{i,n}(1)\in{\fam\msbfam\relax Z}$ pour $i=0,\ldots,a$ et pour tout $n\in{\fam\msbfam\relax N}$.\
Soit $a$ un entier impair $\geq 3$ : notons $\delta(a)$ la dimension de l'espace vectoriel engendré sur ${\fam\msbfam\relax Q}\;$ par $1$ et les $\zeta(j)$ pour $3\leq j\leq a$ et $j$ impair.\
D'après le Théorème des Nombres Premiers, $d_n=e^{n+o(n)}$. Définissons pour tout entier $n\geq 0$ : $\ell_{n}=d_{2n}^{a}S_{2n}(1)$, $p_{0,n}=d_{2n}^aP_{0,2n}(1)$ et $p_{i,n}=d_{2n}^aP_{2i+1,2n}(1)$ ($i=1,\ldots,(a-1)/2$). Le Lemme 5 implique que $p_{i,n}\in{\fam\msbfam\relax Z}$ pour tout $i=0,\ldots,(a-1)/2$ et d'après le Lemme 1, $$\ell_n=p_{0,n}+\displaystyle\sum_{i=1}^{(a-1)/2}p_{i,n}\zeta(2i+1).$$ On peut appliquer le critère de Nesterenko avec $N=(a+1)/2$, $\beta=(e^a2^{a-2r}(2r+1)^{2r+1})^2$ (Lemme 4) et $\alpha=(e^as_{r,a})^2$ (Lemme 3) : pour tout entier $r$ tel que $1\leq r <a/2$, on en déduit alors $\delta(a)\geq f(a,r)/g(a,r)$ où $$\begin{aligned}
f(a,r)&=& (a-2r)\log(2)+(ra+a-r)\log(ra+a-r)\\
&& -(ra+r)\log(ra+r)-(a-2r)\log(a-2r)
\end{aligned}$$ et $$g(a,r)=a+(a-2r)\log(2)+(2r+1)\log(2r+1).$$ Effectuons maintenant un développement limité pour $a,r\to+\infty$ des fonctions $f(a,r)$ et $g(a,r)$ : $$f(a,r)=a\log(r)+O(a)+O(r\log(r))\, \text{ et }\,
g(a,r)=(1+\log(2))a+O(r\log(r)).$$ On choisit $r=r(a)$ comme l'entier $<a/2$ le plus proche de $a(\log(a))^{-2}$ : on a alors $a\log(r)= a\log(a)(1+o(1))$ et $r\log(r)=o(a)$. D'où $$\delta(a)\geq \frac{f(a,r)}{g(a,r)}=
\frac{a\log(a)(1+o(1))+O(a)}{(1+\log(2))a+o(a)}=\frac{\log(a)}{1+\log(2)}
(1+o(1))\,,$$ ce qui prouve le Théorème 1.\

**Références**

$[1]$ R. Apéry, *Irrationalité de $\zeta(2)$ et $\zeta(3)$*, Astérisque **61**, 11-13 (1979).\
$[2]$ K. Ball, Communication personnelle du 17 décembre 1999.\
$[3]$ K. Ball, Communication personnelle du 4 janvier 2000.\
$[4]$ F. Beukers, *A note on the irrationality of $\zeta(2)$ and $\zeta(3)$*, Bull. London. Math. Soc. **11**, no. 33, 268-272 (1978).\
$[5]$ R. Dvornicich et C. Viola, *Some remarks on Beukers' integrals*, Number theory, Vol. II (Budapest, 1987), 637--657, Colloq. Math. Soc. János Bolyai, 51, North-Holland, Amsterdam, 1990.\
$[6]$ Y.V. Nesterenko, *On the linear independence of numbers*, Mosc. Univ. Math. Bull. **40**, no. 1, 69-74 (1985) traduction de Vest. Mosk. Univ., Ser. I, no. 1, 46-54 (1985).\
$[7]$ E.M. Nikishin, *On the irrationality of the values of the functions $F(x,s)$*, Mat. Sbornik **37**, no. 3, 381-388 (1979).\
