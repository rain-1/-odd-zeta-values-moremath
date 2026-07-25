---
title: "Linear independence of odd zeta values using Siegel's lemma"
authors:
  - "Stéphane Fischler"
arxiv_id: "2109.10136v3"
arxiv_url: "https://arxiv.org/abs/2109.10136"
published: "2021-09-21"
journal_ref: ""
doi: ""
source: "papers/14-fischler-2021-siegel-lemma-linear-independence/siegel_arxiv_v3.tex"
conversion: pandoc-flat
---

# Linear independence of odd zeta values using Siegel's lemma

**Stéphane Fischler**

## Abstract

We prove that among 1 and the odd zeta values $ζ(3)$, $ζ(5)$, \ldots, $ζ(s)$, at least $ 0.21 \sqrt{s}/\sqrt{\log s}$ are linearly independent over the rationals, for any sufficiently large odd integer $s$. This is the first asymptotic improvement on the lower bound, logarithmic in $s$, obtained by Ball-Rivoal in 2001. The proof is based on Siegel's lemma to construct non-explicit linear forms in values at odd integers of the Riemann zeta function, instead of using explicit well-poised hypergeometric series. A new refinement of Siegel's linear independence criterion is applied, together with a multiplicity estimate (namely a generalization of Shidlovsky's lemma). The result is also adapted to deal with values of the first $s$ polylogarithms at a fixed algebraic point in the unit disk, improving bounds of Rivoal and Marcovecchio.

---
Math. Subject Classification: 11J72 (Primary), 11M06 (Secondary).

# Introduction

It is well known that $\zeta(s) = \sum_{n=1}^\infty n^{-s}$ is equal, when $s\geq 2$ is an even integer, to $c_s \pi^{ s}$ for some $c_s \in\mathbb{Q}^\ast$. Since $\pi$ is transcendental, so is $\zeta(s)$ in this case. No such formula is known, or even conjectured to exist, when $s\geq 3$ is odd. Eventhough $\pi$, $\zeta(3)$, $\zeta(5)$, ...are conjectured to be algebraically independent over $\mathbb{Q}$, very few results are known in this direction.

The first one is due to Apéry [@Apery]: $\zeta(3)$ is irrational. Then the next breakthrough is the following result of Ball-Rivoal [@BR; @RivoalCRAS]: $$\label{eqBR}
\dim_\mathbb{Q}{\rm Span}_\mathbb{Q}(1, \zeta(3), \zeta(5), \ldots, \zeta(s)) \geq \frac{1-\varepsilon}{1+\log 2}\log s$$ for any $\varepsilon>0$, provided that $s$ is an odd integer large enough in terms of $\varepsilon$. This result has been made effective, and refined, by several authors -- but only for small values of $s$, and there is still no odd $s\geq 5$ for which $\zeta(s)$ is known to be irrational. For large values of $s$, the following result is the first improvement[^2] on the lower bound (eqBR).

**Theorem 1**. *For any sufficiently large odd integer $s$ we have: $$\dim_{\mathbb{Q}} {\rm Span}_{\mathbb{Q}} (1,\zeta(3),\zeta(5),\ldots,\zeta(s)) \geq 0.21 \frac{\sqrt{s}}{\sqrt{ \log s}} .$$*

Here $0.21$ is the rounded value of a real number that we did not try to compute exactly.

As a corollary, there are at least $0.21 \frac{\sqrt{s}}{\sqrt{ \log s}}$ irrational numbers among $\zeta(3)$, $\zeta(5)$, ..., $\zeta(s)$. This weaker result was proved recently by Lai and Yu [@LaiYu] with a better numerical constant, namely[^3] $1.19\ldots$ instead of $0.21$, by following the approach of [@Zudilintrick] and [@Sprang], developed in [@FSZ]. This strategy provides only a lower bound on the number of irrational odd zeta values, but nothing like (eqBR) or Theorem 1 about linear independence. This makes an important difference: no linear independence criterion is needed, so that the proof is much more elementary.

The proof of Theorem 1 extends to values of polylogarithms ${\rm Li}_s(z) = \sum_{n=1}^\infty \frac{z^n}{n^s}$; recall that ${\rm Li}_1(z) = -\log(1-z)$. From now on, we fix an embedding of $\overline{\mathbb{Q}}$ in $\mathbb{C}$. Given a positive integer $s$, and $z\in\overline{\mathbb{Q}}^\ast$ such that $|z|$ is small enough (in terms of $s$ and the degree and height of $z$), the values $1$, ${\rm Li}_1(z)$, ..., ${\rm Li}_s(z)$ are known to be $\mathbb{Q}(z)$-linearly independent (see [@Nikishin; @Hatapolylogs] for the case $z\in\mathbb{Q}$, and [@Chudseul; @Chuddeux; @Andre] for the general case). If $z\in\overline{\mathbb{Q}}^\ast$ is fixed with $|z|<1$, this is conjecturally true for any $s$ but the only known result is the following one (due to Rivoal [@Rivoalpolylogs] for $z\in\mathbb{R}$, to Marcovecchio [@Marcovecchio] in the general case): for any non-zero $z\in\overline{\mathbb{Q}}$ such that $|z|<1$ we have $$\dim_{\mathbb{Q}(z)} {\rm Span}_{\mathbb{Q}(z)} (1,{\rm Li}_1(z),\ldots,{\rm Li}_s(z))\geq \frac{1 -\varepsilon}{(1+\log 2)[\mathbb{Q}(z):\mathbb{Q}]} \log s$$ provided $s\in\mathbb{N}=\{0,1,2,\ldots\}$ is sufficiently large in terms of $\varepsilon>0$. We refer also to [@gfndio2] for algebraic points $z$ outside the unit disk.

In this paper we improve this lower bound as follows.

**Theorem 2**. *Let $s$ be a sufficiently large integer. Then for any $z\in\overline{\mathbb{Q}}$ such that $|z|\leq1$ and $z\not\in\{0,1\}$ we have: $$\dim_{\mathbb{Q}(z)} {\rm Span}_{\mathbb{Q}(z)} (1,{\rm Li}_1(z),{\rm Li}_2(z),\ldots,{\rm Li}_s(z))\geq \frac{0.26}{[\mathbb{Q}(z):\mathbb{Q}]} \frac{\sqrt{s}}{\sqrt{ \log s}} .$$*

Of course this result holds trivially at $z=1$ (after removing ${\rm Li}_1(z)$ from the family), since even powers of $\pi$ are linearly independent over $\mathbb{Q}$.

Most proofs of irrationality (or linear independence) of odd zeta values start with a rational function $$F_n(X) = \sum_{i=1}^a \sum_{j=0}^n \frac{c_{i,j}}{(X+j)^i} \in\mathbb{Q}(X)$$ where $c_{i,j}\in\mathbb{Z}$. For instance Ball-Rivoal's proof of (eqBR) is based on the following function (where $n$ is even and $s$ is odd), which is related to a well-poised hypergeometric series: $$F_n(X) = d_n^s n!^{s-2r} \frac{ (X-rn)_{rn} (X+n+1)_{rn}}{(X)_{n+1}^s},$$ where $(x)_\alpha = x(x+1)\ldots (x+\alpha-1)$ is Pochhammer's symbol, $d_n = {\rm lcm}(1,2,\ldots, n)$, and $r = \lfloor \frac{s}{(\log s)^2}\rfloor$. The point is to obtain a linear combination of $1$ and odd zeta values, namely $$\label{eqflintro}
\sum_{t=1}^\infty F_n(t) = \varrho_{0,n} + \varrho_{3,n}\zeta(3) + \varrho_{5,n}\zeta(5) \ldots+ \varrho_{s,n}\zeta(s)$$ with $\varrho_{i,n} \in\mathbb{Z}$, such that $| \varrho_{i,n}| \leq \beta^{n(1+o(1))}$ as $n\to\infty$ and the absolute value of (eqflintro) is less than $\alpha^{n(1+o(1))}$. Applying a linear independence criterion yields a lower bound $1-\frac{\log \alpha}{\log\beta}$ on the dimension of the $\mathbb{Q}$-vector space spanned by $1$, $\zeta(3)$, $\zeta(5)$, ..., $\zeta(s)$.

In the literature, this strategy has always been applied to an explicit rational function $F_n(X)$ with explicit integers $c_{i,j}$. This has allowed Ball-Rivoal to bound from below the absolue value of (eqflintro), and apply Nesterenko's linear independence criterion [@Nesterenkocritere].

On the contrary, to prove Theorem 1 we apply Siegel's lemma and obtain in this way the existence of integers $c_{i,j}$, not all zero, satisfying suitable assumptions. These integers are therefore *not explicit*. This allows us to get completely different asymptotic values of the parameters as $s\to\infty$. Whereas $\log\alpha\sim -s\log s$ and $\log\beta\sim (1+\log 2)s$ in Ball-Rivoal's proof, we obtain $\log\alpha\sim - 4.55 \sqrt{s \log s}$ and $\log\beta\sim 20.93 \log s$. In particular the coefficients $c_{i,j}$ are much smaller than in explicit constructions.

Using non-explicit integers $c_{i,j}$ makes it impossible to use Nesterenko's linear independence criterion. We use Siegel's criterion instead, by considering for each $n$ a family of linear forms instead of just (eqflintro). This extrapolation procedure is performed using derivation with respect to both $t$ and $z$ (see parameters $p$ and $k$ in §4.1). Then a multiplicity estimate (namely a generalization [@SFcaract] of Shidlovsky's lemma) is used to provide sufficiently many linearly independent linear forms. Since $z=1$ is a singularity of the underlying differential system, we work at the point $z=-1$ by taking profit of the classical relation ${\rm Li}_i(-1) = (2^{1-i}-1)\zeta(i)$ for $i\geq 2$. In such a setting, for each $n$ multiplicity estimates usually give $p$ linearly independent linear forms in $p$ numbers. However, in our situation it is not always possible to obtain this: the conclusion of our multiplicity estimate is weaker, but sufficient because we use a refinement of Siegel's linear independence criterion.

The structure of this paper is as follows. Section 2 contains the tools we need: a version of Siegel's lemma combining equalities and inequalities, a refined version of Siegel's linear independence criterion, and a generalization of Shidlovsky's lemma. In §3 we apply Siegel's lemma to construct the integers $c_{i,j}$, or in other words the rational function $F_n(X)$, that will allow us to prove Theorems 1 and 2 in §4.

# Diophantine tools

We gather in this section the auxiliary Diophantine tools we shall use in the proof of Theorems 1 and 2, namely Siegel's lemma, a refined version of Siegel's linear independence criterion, and a multiplicity estimate which generalizes Shidlovsky's lemma.

## Siegel's lemma

We shall apply the following version of Siegel's lemma. The difference with respect to usual statements (see for instance [@SchmidtLNM Chapter 1, Lemmas 1, 4D or 9A]) is that linear inequalities (namely (eqlemLS2) below) appear: there are not only linear equations with integer coefficients.

**Lemma 1**. *Let $N>M\geq M_0\geq 0$ be integers, and $\lambda_{i,m}\in\mathbb{Z}$ for $1\leq i \leq N$ and $1\leq m \leq M$. For each $1\leq m\leq M$, let $H_m\geq 1$ be a real number such that $\sqrt{\sum_{i=1}^N \lambda_{i,m} ^2}\leq H_m$. For each $m$ such that $M_0< m\leq M$, let $G_m\geq 1$ be a real number. Define $$X = \sqrt N \Big( H_1\ldots H_{M_0}G_{M_0+1}\ldots G_M\Big)^{\frac1{N-M_0}}.$$ Then there exists $(x_1,\ldots,x_N)\in\mathbb{Z}^N\setminus\{(0,\ldots,0)\}$ such that $$\label{eqlemLS1}
 \sum_{i=1}^N \lambda_{i,m} x_i =0 \mbox{ for any } m\in\{1,\ldots,M_0\},$$ $$\label{eqlemLS2}
\Big| \sum_{i=1}^N \lambda_{i,m} x_i \Big| \leq \frac{H_m X}{G_m} \mbox{ for any } m\in\{M_0+1,\ldots,M\},$$ and $$\label{eqlemLS3}
 \sqrt{\sum_{i=1}^N x_i^2}\, \, \leq \, X.$$*

Inequality (eqlemLS2) means that the upper bound deduced from (eqlemLS3) using Cauchy-Schwarz inequality is improved by a multiplicative factor $1/G_m$.

In applying Lemma 1 we shall use the following consequence of (eqlemLS3): $$|x_i| \leq X \mbox{ for any } i\in\{1,\ldots,N\}.$$

of Lemma 1: Let $F$ denote the set of all $x = (x_1,\ldots,x_N)\in\mathbb{R}^N$ such that (eqlemLS1) holds: this is a Euclidean space of dimension $D\geq N-M_0$, with norm given by $\Vert x\Vert = \sqrt{\sum_{i=1}^N x_i^2}$. It is rational, i.e. given by linear equations (eqlemLS1) with integer coefficients $\lambda_{i,m}$; this is equivalent to the existence of a basis of $F$ consisting in elements of $\mathbb{Q}^N$. Then $\Lambda = F \cap \mathbb{Z}^N$ is a lattice in $F$, that is a discrete $\mathbb{Z}$-module of rank $D$; we refer to [@SchmidtLNM Chapter 1] for all notions of geometry of numbers used in this proof. We point out that geometry of numbers is considered, in [@SchmidtLNM] and in most references, in the Euclidean space $\mathbb{R}^D$. Since we need to work in $F$, which is Euclidean with the scalar product induced from the canonical one on $\mathbb{R}^N$, we fix a linear isometric isomorphism $F\to \mathbb{R}^D$ and use it to carry all definitions and properties.

The determinant of $\Lambda$, denoted by $\det \Lambda$, is the absolute value of the determinant of any $\mathbb{Z}$-basis of $\Lambda$ with respect to an orthonormal basis of $F$ (because such an orthonormal basis is mapped to the canonical basis of $\mathbb{R}^D$ by the above-mentioned isometric isomorphism). It is equal to the volume of the fundamental parallelepiped of $\Lambda$ (see [@SchmidtLNM Chapter 1, §2]).

The *height* of $F$, denoted by $H(F)$, is by definition $\det \Lambda$ (see [@SchmidtLNM Chapter 1, §4] or [@SchmidtAnnals]). Now let $F^\perp$ denote the orthogonal complement of $F$ in $\mathbb{R}^N$, and consider the vector $u_m=(\lambda_{1,m}, \ldots, \lambda_{N,m})\in\mathbb{Z}^N$ for any $m\in\{1,\ldots,M_0\}$. The definition (eqlemLS1) of $F$ implies $F^\perp = {\rm Span}(u_1,\ldots,u_{M_0})$. Reindexing $u_1$, ..., $u_{M_0}$ if necessary, we may assume that $u_1$, ..., $u_{N-D}$ are linearly independent, so that $F^\perp = {\rm Span}(u_1,\ldots,u_{N-D})$. Denoting by $U$ the square matrix of size $N-D$ of which the columns are the coordinates of $u_1$, ..., $u_{N-D}$ in an orthonormal basis of $F^\perp$, since $F^\perp\cap \mathbb{Z}^N$ contains the $\mathbb{Z}$-module spanned by $u_1$, ..., $u_{N-D}$ we have $$H(F^\perp) = \det( F^\perp\cap \mathbb{Z}^N)\leq | \det U | \leq \prod_{m=1}^{N-D} \Vert u_m\Vert \leq \prod_{m=1}^{N-D} H_m$$ using Hadamard's inequality (as in [@SchmidtLNM Chapter 1, §4, p. 11]). Since $H(F)=H(F^\perp)$ (see [@SchmidtLNM Lemma 4C]) and $H_m\geq 1$ for any $m$, we have $$\label{eqref1}
\det \Lambda = H(F) \leq \prod_{m=1}^{M_0} H_m.$$

Now let us denote by ${\mathcal{C}}$ the set of all $x = (x_1,\ldots,x_N)\in F$ such that Eqns. (eqlemLS2) and (eqlemLS3) hold. We claim that $$\label{eqref2}
{\rm vol}\, {\mathcal{C}}\geq \frac{(2X/\sqrt D)^D}{\prod_{m=M_0+1}^{M} G_m}$$ where ${\rm vol}\, {\mathcal{C}}$ is the volume of ${\mathcal{C}}$ inside the Euclidean space $F$. Admitting this lower bound for now, and comparing it with Eq. (eqref1) and the definition of $X$, we obtain $${\rm vol}\, {\mathcal{C}}\geq 2^D \prod_{m=1}^{M_0} H_m\geq 2^D\det \Lambda$$ since $N-M_0\leq D \leq N$ and $H_m, G_m\geq 1$ for any $m$. Now ${\mathcal{C}}$ is a symmetric compact convex body, so Minkowski's first theorem asserts the existence of a non-zero $x\in{\mathcal{C}}\cap\Lambda={\mathcal{C}}\cap\mathbb{Z}^N$. This concludes the proof of Lemma 1, except for the claim (eqref2) that we shall prove now.

To prove Eq. (eqref2) we consider $u_m= (\lambda_{1,m}, \ldots, \lambda_{N,m})$ for any $m\in\{M_0+1,\ldots,M \}$, and notice that ${\mathcal{C}}$ contains all $x\in F$ such that $$\Vert x \Vert \leq X \mbox{ and }|\langle u_m, x \rangle | \leq \frac{ \Vert u_m \Vert \, X}{G_m}\mbox{ for any } m\in\{M_0+1,\ldots,M \}$$ since $\Vert u_m \Vert \leq H_m$. Now all indices $m\in\{M_0+1,\ldots,M \}$ play symmetric roles so we may assume that $G_{M_0+1}\geq \ldots\geq G_M\geq 1$. There exists an orthonormal basis $(e_1,\ldots,e_D)$ of $F$ such that $u_{M_0+i}\in {\rm Span}(e_1,\ldots,e_i)$ for any $1\leq i \leq M-M_0$. We shall prove that ${\mathcal{C}}$ contains the set ${\mathcal{C}}'$ of all points $x=\alpha_1e_1+\ldots+\alpha_De_D$ such that $$|\alpha_i| \leq \frac{ X}{G_{M_0+i} \sqrt{D}} \quad \mbox{ if } 1\leq i \leq M-M_0, \quad \mbox{ and } \quad |\alpha_i| \leq \frac{ X}{\sqrt{D}} \quad \mbox{ if } M-M_0+1\leq i \leq D.$$ Indeed any such $x$ satisfies $\Vert x \Vert \leq \sqrt D \max_{1\leq i \leq D} |\alpha_i| \leq X$. Moreover, for $M_0+1\leq m \leq M$ we have, since $u_{m}\in {\rm Span}(e_1,\ldots,e_{m-M_0})$: $$ | \langle u_m, x \rangle | =  | \langle u_m, \sum_{i=1}^{m-M_0} \alpha_i e_i \rangle | \leq \Vert u_m \Vert \cdot \Vert \sum_{i=1}^{m-M_0} \alpha_i e_i \Vert \leq \Vert u_m \Vert \sqrt{m-M_0} \frac{ X}{G_m\sqrt{D}} \leq \frac{ \Vert u_m \Vert \, X}{ G_m}.$$ Thus ${\mathcal{C}}' \subset {\mathcal{C}}$, and Eq. (eqref2) follows. This concludes the proof of Lemma 1.

## A refinement of Siegel's linear independence criterion

The proof of Theorems 1 and 2 relies on the following refinement of Siegel's linear independence criterion (for usual versions, see for instance [@EMS p. 81--82 and 215--216], [@Matala-Aho §3], [@Marcovecchio Proposition 4.1], [@SFcaract Proposition 4.6] or [@gfndio2 Theorem 4]).

Let $\mathbb{K}$ be a number field embedded in $\mathbb{C}$, and ${\mathcal O}_{\mathbb{K}}$ be its ring of integers. Let $\mathbb{K}_\infty=\mathbb{R}$ if $\mathbb{K}\subset\mathbb{R}$, and $\mathbb{K}_\infty=\mathbb{C}$ otherwise. The house of $\xi\in\mathbb{K}$, denoted by $\mathord{
 \mathpalette\@house{\xi}
 }$, is the maximum modulus of the conjugates of $\xi$.

**Proposition 1**. *Let $\theta_0,\ldots,\theta_p$ be elements of $\mathbb{K}_\infty$, with $\theta_0\neq 0$. Let $\tau>0$, and $(Q_n)$ be a sequence of real numbers with limit $+\infty$. Let $\mathcal{N}$ be an infinite subset of $\mathbb{N}$, and for any $n\in\mathcal{N}$ let $[\ell_{i,j}^{(n)}]_{0\leq i \leq I_n, 0\leq j \leq p}$ be a matrix with coefficients in ${\mathcal O}_{\mathbb{K}}$ such that:*

-   *As $n\to\infty$ with $n\in\mathcal{N}$, $$\max_{  i,j  }
     \mathord{
     \mathpalette\@house{ \ell_{i,j}^{(n)} }
     }
     \leq Q_n^{1+o(1)}\quad
    \mbox{ and } \quad
    \max_{0\leq i\leq I_n } | \ell_{i,0}^{(n)} \theta_0 + \ldots + \ell_{i,p}^{(n)} \theta_p | \leq Q_n^{-\tau + o(1)}.$$*

-   *For any $n\in\mathcal{N}$ sufficiently large, for any $x_0,\ldots,x_p\in\mathbb{K}$, if $$\forall i\in\{0,\ldots,I_n\} \quad\quad   \ell_{i,0}^{(n)} x_0 + \ldots + \ell_{i,p}^{(n)} x_p = 0$$ then $x_0=0$.*

*Then we have $$\dim_\mathbb{K}{\rm Span}_\mathbb{K}(\theta_0,\ldots,\theta_p)\geq \frac{ [\mathbb{K}_\infty : \mathbb{R}]}{ [\mathbb{K}:\mathbb{Q}]} \cdot ( \tau+1) .$$*

Usually, in Siegel's linear independence criterion the conclusion of assumption $(ii)$ is $x_0=\ldots=x_p=0$. It turns out that $x_0=0$ is sufficient (since we assume $\theta_0\neq 0$). In terms of the matrix $[\ell_{i,j}^{(n)}]_{0\leq i \leq I_n, 0\leq j \leq p}$, we assume that the first column (corresponding to $j=0$) is not a linear combination of other columns. This is weaker than the usual assumption, namely that the $p+1$ columns are linearly independent. In particular, Proposition 1 may apply in settings where the number of linear forms, namely $I_n+1$, is less than $p+1$.

Another way of stating this is that we assume that the $I_n+1$ linear forms we have (for a given $n$) have no common zero $x=(x_0,\ldots,x_p)$ such that $x_0\neq 0$. The usual assumption is that they have no common zero at all in $\mathbb{K}^{p+1}\setminus\{0\}$.

In the proof of Theorem 1 we apply Proposition 1 with $\mathbb{K}=\mathbb{Q}$, $Q_n = \beta^n$, and $\tau = -\frac{\log \alpha}{\log\beta}$ (so that $Q_n^{-\tau} = \alpha^n$), where $\alpha$ and $\beta$ will be defined in §4.6. The setting is similar for Theorem 2, with $\mathbb{K}=\mathbb{Q}(z)$ (see §4.7).

*Proof of Proposition 1.* Let $d=\dim_\mathbb{K}{\rm Span}_\mathbb{K}(\theta_0,\ldots,\theta_p)$. There exists a matrix $\Lambda=[\lambda_{i,j}]_{1\leq i \leq p+1-d, 0\leq j \leq p}\in M_{p+1-d,p+1}({\mathcal O}_{\mathbb{K}})$ of rank $p+1-d$ such that for any $1\leq i \leq p+1-d$, we have $\sum_{j=0}^{p} \lambda_{i,j}\theta_j=0$. For any $n\in \mathcal{N}$ we let $L^{(n)}=[\ell_{i,j}^{(n)}]_{0\leq i \leq I_n, 0\leq j\leq p}\in M_{I+1,p+1}({\mathcal O}_{\mathbb{K}})$ and consider the matrix $M^{(n)}=\left[\begin{array}{c} \Lambda \\  L^{(n)}\end{array}\right]\in M_{p+I_n+2-d, p+1}({\mathcal O}_{\mathbb{K}})$. Since ${\rm rk}M^{(n)}$ takes only finitely many values, there exists $r\leq p+1$ such that ${\rm rk}M^{(n)} = r$ for infinitely many $n\in\mathcal{N}$. Discarding other elements of $\mathcal{N}$, we may assume that ${\rm rk}M^{(n)} = r$ for any $n\in\mathcal{N}$.

For any $n\in\mathcal{N}$ there exists ${\mathcal{C}}_n\subset\{0,\ldots,p\}$ of cardinality $r$ such that the columns of $M^{(n)}$ with index $j\in {\mathcal{C}}_n$ are linearly independent; then all other columns of $M^{(n)}$ are $\mathbb{K}$-linear combinations of these $r$ columns. If $0\not\in{\mathcal{C}}_n$ then there exist $x_1^{(n)}, \ldots,
x_p^{(n)}\in\mathbb{K}$ such that for any $0\leq i \leq I_n$, $\ell_{i,0}^{(n)} = \sum_{j=1}^p x_j^{(n)}\ell_{i,j}^{(n)}$. This contradicts hypothesis $(ii)$ if $n$ is large enough, so that $0\in{\mathcal{C}}_n$ (discarding finitely many integers $n$ if necessary). Since ${\mathcal{C}}_n$ takes only finitely many values, as above we may assume that there exists ${\mathcal{C}}\subset\{0,\ldots,p\}$ of cardinality $r$, with $0\in{\mathcal{C}}$, such that ${\mathcal{C}}_n={\mathcal{C}}$ for any $n\in\mathcal{N}$. Since $\theta_1,\ldots,\theta_p$ play symmetric roles, we assume for simplicity that ${\mathcal{C}}= \{0,\ldots, r-1\}$.

We denote by $C_0^{(n)},\ldots, C_p^{(n)}$ the columns of $M^{(n)}$. Since ${\mathcal{C}}_n = \{0,\ldots, r-1\}$, for any $j\in \{r,\ldots,p\}$ there exist $\kappa_{j,0}^{(n)}, \ldots, \kappa_{j,r-1}^{(n)}\in\mathbb{K}$ such that $C_j^{(n)} = \kappa_{j,0}^{(n)} C_0^{(n)} + \ldots+  \kappa_{j,r-1}^{(n)} C_{r-1}^{(n)}$. This implies $\kappa_{j,0}^{(n)} \ell_{i,0}^{(n)} + \ldots+  \kappa_{j,r-1}^{(n)}  \ell_{i,r-1}^{(n)} -  \ell_{i,j}^{(n)}=0$ for any $0\leq i \leq I_n$, so that $\kappa_{j,0}^{(n)}=0$ using assumption $(ii)$. We deduce that for any $0\leq i \leq I_n$: $$\sum_{j=0}^p  \ell_{i,j}^{(n)}\theta_j= \sum_{j=0}^{r-1}  \ell_{i,j}^{(n)}\theta_j +  \sum_{j=r}^{p}\Big( \sum_{t=1}^{r-1}   \kappa_{j,t}^{(n)}  \ell_{i,t}^{(n)} \Big)  \theta_j  =  \sum_{s=0}^{r-1} \Theta_s^{(n)}  \ell_{i,s}^{(n)}$$ where $$\Theta_s^{(n)} = \theta_s +  \sum_{j=r}^{p}    \kappa_{j,s}^{(n)}  \theta_j  \quad \mbox{ for any $0\leq s \leq r-1$,}$$ and in particular $\Theta_0^{(n)} = \theta_0$ since $\kappa_{j,0}^{(n)}=0$ for any $j$. In the same way, we have $0 = \sum_{j=0}^p \lambda_{i,j}\theta_j =  \sum_{s=0}^{r-1} \Theta_s^{(n)}  \lambda_{i,s}$ for any $1\leq i \leq p+1-d$. Therefore the linear combination of columns $\sum_{s=0}^{r-1} \Theta_s^{(n)}  C_s^{(n)}$ consists in $p+1-d$ coefficients equal to $0$, and then $I_n+1$ coefficients bounded by $Q_n^{-\tau + o(1)}$.

Denote by $M_1^{(n)}=\left[\begin{array}{c} \Lambda_1 \\  L_1^{(n)}\end{array}\right]\in M_{p+I_n+2-d, r}({\mathcal O}_{\mathbb{K}})$ the matrix obtained by keeping only the first $r$ columns of $M^{(n)}=\left[\begin{array}{c} \Lambda \\  L^{(n)}\end{array}\right]$, so that $\Lambda_1$ and $L_1^{(n)}$ are obtained in the same way from $\Lambda$ and $L ^{(n)}$ respectively. Then ${\rm rk}M_1^{(n)} = r$ since ${\mathcal{C}}_n  = \{0,\ldots, r-1\}$, and ${\rm rk}\Lambda_1  = {\rm rk}\Lambda  = p+1-d$ because the columns of $\Lambda_1$ span the same vector space as those of $\Lambda$; in particular, $r\geq p+1-d$.

Therefore $M_1^{(n)}=\left[\begin{array}{c} \Lambda_1 \\  L_1^{(n)}\end{array}\right]$ has rank $r$ equal to its number of columns, and its first $p+1-d$ rows are linearly independent: we may choose $r-(p+1-d)$ rows among those of $L_1^{(n)}$ that make up, together with $\Lambda_1$, an invertible matrix. Up to renumbering the linear forms, we may assume that the first $r-(p+1-d)$ rows have this property. Then we denote by $L_2^{(n)}=[\ell_{i,j}^{(n)}]_{0\leq i \leq  r-p+d-2, 0\leq j\leq r-1}\in M_{r-p+d-1,r}({\mathcal O}_{\mathbb{K}})$ the matrix obtained from $L_1^{(n)}$ by keeping only these rows, and we let $M_2^{(n)}=\left[\begin{array}{c} \Lambda_1 \\  L_2^{(n)}\end{array}\right]\in M_{r}({\mathcal O}_{\mathbb{K}})\cap {\rm GL}_r(\mathbb{K})$.

As in the usual proof of Siegel's criterion, we may now consider the non-zero determinant $\Delta^{(n)}\in {\mathcal O}_{\mathbb{K}}$ of $M_2^{(n)}$. Recall that $\mathbb{K}$ is embedded in $\mathbb{C}$, and that $\sum_{s=0}^{r-1} \Theta_s^{(n)}  C_s^{(n)}$ consists in $p+1-d$ coefficients equal to $0$, and then $I_n+1$ coefficients bounded by $Q_n^{-\tau + o(1)}$, where $C_0^{(n)},\ldots, C_{r-1}^{(n)}$ are the columns of $M_1^{(n)}$. Keeping only the first $r$ coefficients of these columns, we obtain the corresponding columns of $M_2^{(n)}$. Then $\Delta^{(n)}$ is equal to the determinant of the matrix obtained from $M_2^{(n)}$ by replacing the first column with this linear combination divided by $\Theta_0^{(n)} = \theta_0$ (which is non-zero by assumption, and independent of $n$). Since only the last $r-p+d-1$ rows of $M_2^{(n)}$ depend on $n$, and these are the only rows where non-zero coefficients may appear in the new first column, we obtain by expanding the determinant with respect to this column: $$|\Delta^{(n)}| \leq  Q_n^{-\tau + o(1)} \Big(Q_n^{1+o(1)}\Big)^{r-p-2+d} =  Q_n^{-\tau +r-p-2+d+ o(1)} \leq  Q_n^{-\tau  -1+d+ o(1)}$$ using assumption $(i)$ and the upper bound $r\leq p+1$.

Let $\delta=[\mathbb{K}:\mathbb{Q}]$ and denote by $\sigma_1={\rm Id}$, $\sigma_2$, ..., $\sigma_\delta$ the embeddings $\mathbb{K}\to\mathbb{C}$. If $\mathbb{K}_\infty=\mathbb{R}$, we bound $|\sigma_k(\Delta^{(n)})| = |\det \sigma_k(M_2^{(n)})|$ trivially by $Q_n^{r-p-1+d+o(1)}\leq Q_n^{d+o(1)}$ for any $2\leq k \leq \delta$, so that $\prod_{k=1}^\delta  \sigma_k(\Delta^{(n)})  \in\mathbb{Z}\setminus\{0\}$ satisfies $$1 \leq \Big| \prod_{k=1}^\delta \sigma_k(\Delta^{(n)}) \Big| \leq Q_n^{-\tau  -1+d+d(\delta-1) +o(1)} = Q_n^{-\tau  -1+d \delta + o(1)}$$ and therefore $d \delta \geq \tau+1$. If $\mathbb{K}_\infty=\mathbb{C}$ then we may assume $\sigma_2$ to be complex conjugation so that $|\sigma_2(\Delta^{(n)})| =  |\sigma_1(\Delta^{(n)})|$. We bound $|\sigma_k(\Delta^{(n)})|$ as above for $3\leq k \leq \delta$, and deduce $2( -\tau  -1+d) + (\delta-2)d\geq 0$, that is $d \delta \geq 2(\tau+1)$. ◻

## Multiplicity estimate

Let us state now the generalisation of Shidlovsky's lemma we shall use, namely [@SFcaract Theorem 3.1]. It is based on Fuchs' global relation on exponents, following the approach initiated by Chudnovsky [@ChudShid; @ChudShidDeux] in the Fuchsian case and generalized by Bertrand-Beukers [@BB] and Bertand [@DBShid] using differential Galois theory.

We consider a positive integer $N$ and a matrix $A \in M_N(\mathbb{C}(z))$. We let $S_0,\ldots,S_{N-1}\in\mathbb{C}[X]$ with $\deg S_i \leq m$ for any $i$. With each solution $Y =  \ ^t (y_0,\ldots,y_{N-1})$ of the differential system $Y'=AY$ is associated a remainder $R(Y)$ defined by $$R(Y)(z) = \sum_{i=0}^{N-1} S_i(z) y_i(z).$$ Let $\Sigma$ be a finite subset of $\mathbb{P}^1(\mathbb{C}) = \mathbb{C}\cup\{\infty\}$, with $\infty\in\Sigma$. For each $\sigma\in\Sigma$, let $(Y_j)_{j\in J_\sigma}$ be a family of solutions of $Y'=AY$ such that:

-   For any $j\in J_\sigma$, the function $R(Y_j)$ belongs to the Nilsson class at $\sigma$, i.e. can be written as a $\mathbb{C}$-linear combination of functions of the form $h(z)(z-\sigma)^a(\log(z-\sigma))^b$ with $a\in\mathbb{C}$, $b\in\mathbb{N}$, and $h$ holomorphic at $\sigma$; here $z-\sigma$ should be understood as $1/z$ if $\sigma=\infty$.

-   The functions $R(Y_j)$, for $j\in J_\sigma$, are linearly independent over $\mathbb{C}$ (as functions on a small open disk centered at $\sigma$).

**Theorem 3**. *Let $\mu$ denote the order of a non-zero differential operator $L \in \mathbb{C}(z)[\frac{{\rm d}}{{\rm d}z}]$ such that $L(R(Y_j))= 0$ for any $\sigma\in\Sigma$ and any $j\in J_\sigma$. Then $$\sum_{\sigma\in\Sigma}\sum_{j\in J_{\sigma}} {\rm ord}_\sigma(R(Y_j)) \leq (m+1) (\mu - {\rm Card}\,J_\infty) + c_1$$ where $c_1$ is a constant that depends only on $A$ and $\Sigma$.*

In this result we denote by ${\rm ord}_\sigma$ the order of vanishing at $\sigma$ (recall that logarithmic factors may appear, but they have no influence on the order of vanishing; for instance, ${\rm ord}_0(z^e(\log z)^i)$ is the real part of $e$, for $e\in\mathbb{C}$ and $i\in\mathbb{N}$).

# A non-explicit rational function

In this section we construct the rational function $F_n(X)$ that will be used in §4 to prove Theorems 1 and 2. The output of this construction is stated as Theorem 4 in §3.1. Its proof, based on Siegel's lemma, is given in §3.5. It relies on a result of [@FR], which relates asymptotic estimates of $F_n(X)$ at infinity to values at 1 of some functions $P_{k,1}(z)$ related to a differential system arising from polylogarithms. In §3.2 we define these functions $P_{k,1}(z)$, explain the setting and state as Proposition 2 a technical result used in the proof of Theorem 4. We prove Proposition 2 in §3.4, after dealing with a lemma of analytic number theory in §3.3.

## Output of the construction

In this section we apply Siegel's lemma (namely Lemma 1 stated in §2.1) to construct integers $c_{i,j}\in\mathbb{Z}$, for $1\leq i \leq a$ and $0\leq j \leq n$, such that the rational function $$\label{eqfncij}
F_n(X) = \sum_{i=1}^a \sum_{j=0}^n \frac{c_{i,j}}{(X+j)^i} \in\mathbb{Q}(X)$$ has interesting properties. We denote by $$F_n(t) = \sum_{d=1}^\infty \frac{{\mathfrak A}_d}{t^d}$$ the expansion of $F_n(t)$ as $|t|\to\infty$.

**Theorem 4**. *Let $a\in\mathbb{N}$ and $\omega,\Omega,r\in\mathbb{Q}$ be such that $a>\Omega\geq \omega\geq 1$ and $r\geq 1$. Then for any $n\geq 0$ such that $rn, \omega n , \Omega n\in\mathbb{N}$ there exist integers $c_{i,j}\in\mathbb{Z}$ for $1\leq i \leq a$ and $0\leq j \leq n$, not all zero, with the following properties:*

-   *As $|t| \to\infty$, we have $F_n(t) = O(|t|^{-\omega n})$.*

-   *As $n\to \infty$, we have $|c_{i,j}| \leq \chi^{n(1+o(1))}$ for any $i$, $j$, with $$\label{eqdefchi}
    \chi = \exp\Big(\frac{ \omega\log 2 + 3\omega^2 + \omega^2 \log (a+1) +\frac12 \Omega^2 \log r }{a-\omega}\Big).$$*

-   *For any $d < \Omega n$ we have $|{\mathfrak A}_d |\leq r^{d-\Omega n} n^d d^a \chi^{n(1+o(1))}$.*

*Moreover in $(ii)$ and $(iii)$ the sequences denoted by $o(1)$ do not depend on $i$, $j$, $d$, and tend to 0 as $n\to\infty$.*

The upper bound $(iii)$ is interesting only when $\omega n \leq d < \Omega n$, since part $(i)$ means ${\mathfrak A}_d = 0$ for any $d< \omega n$. We also point out that, even if it is not explicit in the notation, the integers $c_{i,j}$ depend on $a,\omega,\Omega, r, n$.

This section is devoted to the proof of Theorem 4; this proof will be completed in §3.5.

A rather easy construction of integers $c_{i,j}$ satisfying properties $(i)$ and $(iii)$ of Theorem 4 would be to apply Lemma 1, translating $(i)$ as ${\mathfrak A}_d =0$ for any $d<\omega n$. However the explicit expression of ${\mathfrak A}_d$ (see Eq. (eqdefad) in §3.5) shows that for $d$ close to $\omega n$, the equation ${\mathfrak A}_d =0$ is of the form $\sum_{i,j} \lambda_{i,j}c_{i,j}=0$ with integers $\lambda_{i,j}$ such that $| \lambda_{i,j}|\leq n^{\omega n(1+o(1))}$. Applying Lemma 1 with such a huge bound would not give as $n\to\infty$ a geometric bound on $|c_{i,j}|$ in $(ii)$, and therefore it would not seem possible to derive any Diophantine application. Instead, to prove Theorem 4 we translate assertion $(i)$ as $P_{k,1}(1)=0$ for any $k<\omega n$ (see §3.5). We shall define these functions $P_{k,1}(z)$ now.

## Setting of the proof

Let $a\geq 1$ and $n\geq 0$. In this section we start with arbitrary real numbers $c_{i,j}$, for $1\leq i \leq a$ and $0\leq j \leq n$, which may either be fixed or considered as unknowns. We point out that the result of §§3.2 to 3.4, namely Proposition 2 below, will be used 3 times in this paper: in §3.5 to prove Theorem 4, in §4.3 to prove Lemma 5, and in §4.7 for Theorem 2.

We let $P_i(z) = \sum_{j=0}^n c_{i,j}z^j$ for $1\leq i \leq a$, and $P_0(z)=0$. We define $P_{k,i}(z)$ for $0\leq i \leq a$ and $k\geq 1$ as follows: $P_{1,i}(z) = P_i(z)$ for any $i$, and for $k\geq 2$: $$\label{eqrecpkijtechnique}
\left\{ \begin{array}{l}
P_{k,i}(z) = P'_{k-1,i}(z) - \frac1{z} P_{k-1,i+1}(z) \mbox{ for } 1\leq i \leq a \\
P_{k,0}(z) = P'_{k-1,0}(z) + \frac{\alpha_1z + \alpha_0}{z(1-z)} P_{k-1,1}(z)
\end{array}\right.$$ where $P_{k-1,a+1}$ is taken to be the zero function; the motivation for this definition will be given in §§3.5 and 4.1 (see Eqns. (eqpkdef) and (eqdefqpk)). Here $(\alpha_0,\alpha_1)\in\mathbb{Z}^2$ is fixed; we shall take $(\alpha_0,\alpha_1)=(1,1)$ in the proof of Theorem 1, and $(\alpha_0,\alpha_1)=(1,0)$ for Theorem 2. It is not difficult (as in [@SFcaract proof of Proposition 4.4]) to prove that $z^{k-1} P_{k,i}(z)$ is a polynomial of degree at most $n$ for $1\leq i \leq a$, and that $z^{k-1} (1-z)^{k-1} P_{k,0}(z)$ is a polynomial of degree at most $n+k-1$; this follows also from the proof of Proposition 2 below. We define the coefficients $p_{k,i,j}$ by $$\label{eqdefpkij}
\left\{ \begin{array}{l}
 z^{k-1} P_{k,i}(z) = \sum_{j=0}^n p_{k,i,j} z^j \mbox{ if } i\geq 1,\\
z^{k-1} (1-z)^{k-1} P_{k,0}(z)= \sum_{j=0}^{n+k-1} p_{k,0,j} z^j.
\end{array}\right.$$ It is clear that each coefficient $p_{k,i,j}$ is a $\mathbb{Q}$-linear combination of the (fixed or unknown) coefficients $c_{i',j'}$ we have started with to define $P_0$, ..., $P_a$. In other words, there exist rational numbers $\vartheta_{k,i,j,i',j'}$ such that for any $k$, $i$, $j$: $$\label{eqch0}
p_{k,i,j} = \sum_{i'=1}^a\sum_{j'=0}^n \vartheta_{k,i,j,i',j'}c_{i',j'}.$$ The point of the next result, which is the main step in the proof of Theorem 4, is to provide a common denominator (depending only on $k$) and an upper bound on these coefficients $\vartheta_{k,i,j,i',j'}$.

**Proposition 2**. *For any $k\geq 1$ there exists a positive integer $\delta_k =\delta_k (a,n, \alpha_0,\alpha_1)$, which depends only on $k$, $a$, $n$, $\alpha_0$, $\alpha_1$, such that:*

-   *We have $\delta_k \leq (e^3(a+1))^{ \max(n,k) }$ provided $n$ is large enough in terms of $a$.*

-   *For any $i$, $j$, $i'$, $j'$ we have $\frac{\delta_k}{(k-1)!} \vartheta_{k,i,j,i',j'}\in \mathbb{Z}$.*

-   *For any $i$, $j$, $i'$, $j'$ we have $$\Big| \frac{\delta_k}{(k-1)!} \vartheta_{k,i,j,i',j'}\Big| \leq
    \left\{
    \begin{array}{l}
    k^a 2^n \delta_k \mbox{ if } 1\leq i \leq a,\\
    \max(| \alpha_0| ,| \alpha_1| )\, k^{a+1} 8^{\max(n,k)}\delta_k \mbox{ if } i=0.
    \end{array}
    \right.$$*

The first observation is that we have geometric bounds as $n\to\infty$ (with $k<\omega n$): this solves the problem raised at the end of §3.1. Another crucial remark is the dependence with respect to $a$ of the upper bound in $(i)$: it is polynomial in $a$, whereas a direct approach would lead to an exponential bound, thereby ruining the Diophantine application we have in mind. Indeed we recall (see the end of the introduction, or §4.6 for details) that we plan to construct a linear combination of odd zeta values, with coefficients bounded by $\beta^{n(1+o(1))}$ as $n\to\infty$, where $\beta$ is a polynomial in $a$. To achieve this, the bound in $(i)$ has to be polynomial in $a$. This property comes from Lemma 2 below.

In the proof of Theorem 4 we shall not use the case $i=0$ of parts $(ii)$ and $(iii)$, but they will be used in the proof of Lemma 5 in §4.3.

## A lemma from analytic number theory

A crucial step in the proof of Proposition 2 is the use of the following lemma, which is of independent interest.

**Lemma 2**. *Let $a, N \geq 1$. Denote by $\Delta_{a,N}$ the least common multiple of all products $N_1\ldots N_{\alpha}$ where $\alpha\leq a$ and $N_1$, ..., $N_\alpha$ are pairwise distinct integers between $-N$ and $N$ such that $\max N_i - \min N_i \leq N$. Then as $N\to\infty$ (while $a$ is fixed) we have: $$\label{eqlemarithgene}
 \Delta_{a,N} = \exp \Big( N ( \sum_{j=1}^a \frac1j+o(1))\Big)
 \leq \Big(( a+1) e^{\gamma+o(1)}\Big)^{ N}$$ where $\gamma$ is Euler's constant.*

The naive version of this lemma would be to use the upper bound $\Delta_{a,N} \leq d_N^a$, where $d_N = {\rm lcm}(1,2,\ldots,N)$, leading to $\Delta_{a,N} \leq e^{aN(1+o(1))}$. The dependence in $a$ is much better in Lemma 2 because we use the assumption that $N_1$, ..., $N_\alpha$ are pairwise distinct.

In the proof we shall use the function $\psi$ defined by $\psi(x) = \sum_{p^e \leq x} \log p$, where the sum is over prime numbers $p$ and positive integers $e$ such that $p^e \leq x$. The least common multiple of $1$, $2$, ..., $N$ is then $\exp(\psi(N))$. We recall (see for instance [@HW Chapter XXII, Theorem 434]) that the prime number theorem yields $\psi(N) = N(1+o(1))$.

of Lemma 2: For any prime power $p^e$ we let $f_{a,N}(p^e) = \min( a, \lfloor \frac{N}{p^e} \rfloor)$ and we consider $$\Delta = \prod_{p ^e \leq N} p^{ f_{a,N}(p^e) }$$ where the product is taken over all pairs $(p,e)$ such that $p$ is a prime number, $e\geq 1$, and $p^e\leq N$. Our goal is to prove that $\Delta_{a,N} =\Delta$. To begin with, we compute for any prime $p\leq N$ the $p$-adic valuation of $\Delta$ as follows: $$\label{eqvpDel}
v_p(\Delta)= \sum_{e=1}^{\lfloor \frac{\log N}{\log p} \rfloor } f_{a,N}(p^e) =a \Big\lfloor \frac{\log (N/a) }{\log p} \Big\rfloor + \sum_{e = \lfloor \frac{\log (N/a)}{\log p} \rfloor +1 }^{\lfloor \frac{\log N}{\log p} \rfloor }\Big\lfloor \frac{N}{p^e} \Big\rfloor .$$ Now let us prove that $\Delta_{a,N}$ divides $\Delta$. Let $p$ be a prime number; we shall prove that $v_p ( N_1\ldots N_{\alpha} ) \leq v_p( \Delta)$ for any non-zero pairwise distinct integers $N_1$, ..., $N_\alpha$ between $-N$ and $N$, with $\alpha\leq a$ and $\max N_i - \min N_i \leq N$. Since $|N_i| \leq N$ for each $i$, we have $$\label{eqvppro}
v_p ( N_1\ldots N_{\alpha} ) = \sum_{i=1}^\alpha v_p(N_i) =\sum_{e =1}^{ \lfloor \frac{\log N }{\log p} \rfloor } {\rm Card}\,{\mathcal{S}}_{p,e}$$ where ${\mathcal{S}}_{p,e}=\{i\in\{1,\ldots,\alpha\}, \, v_p(N_i)\geq e\}$. Obviously we have ${\rm Card}\,{\mathcal{S}}_{p,e}\leq \alpha\leq a$, and $${\rm Card}\,{\mathcal{S}}_{p,e}\leq \Big\lfloor \frac{\max_i N_i - \min_i N_i }{ p^e} \Big\rfloor +1\leq \Big\lfloor\frac{N }{ p^e}\Big\rfloor +1.$$ Moreover if ${\rm Card}\,{\mathcal{S}}_{p,e}= \lfloor\frac{N }{ p^e}\rfloor +1$ then $\min_i N_i = up^e$ and $\max_i N_i = vp^e$ with $u,v\in\mathbb{Z}$ such that $v-u = \lfloor\frac{N }{ p^e}\rfloor$. If $u\geq 1$ then $v\geq 1 + \lfloor\frac{N }{ p^e}\rfloor > N/p^e$ so that $vp^e> N$, which is impossible. The same contradiction holds if $v\leq -1$ because in this case $-u \geq 1 + \lfloor\frac{N }{ p^e}\rfloor > N/p^e$. Therefore we have $u\leq 0 \leq v$; since all $N_i$ are non-zero, we obtain ${\rm Card}\,{\mathcal{S}}_{p,e}\leq \lfloor\frac{N }{ p^e}\rfloor$ and finally ${\rm Card}\,{\mathcal{S}}_{p,e}\leq f_{a,N}(p^e)$. Combining Eqns. (eqvppro) and (eqvpDel) concludes the proof that $\Delta_{a,N}$ divides $\Delta$.

Let us prove now[^4] that $\Delta$ divides $\Delta_{a,N}$. Let $p$ be a prime number; we shall construct pairwise distinct integers $N_i$ between 1 and $N$ such that $v_p ( N_1\ldots N_a ) =v_p(\Delta)$. We write $e = \lfloor \frac{\log (N/a) }{\log p} \rfloor +1$, so that $p^{e-1}\leq N/a < p^e$, and $k = \lfloor\frac{N }{ p^e}\rfloor$. If $\lfloor \frac{\log N }{\log p} \rfloor = \lfloor \frac{\log (N/a) }{\log p} \rfloor$ the sum in Eq. (eqvpDel) is empty, so that letting $N_i = i p^{e-1}$ for $1\leq i \leq a$ we have $v_p ( N_1\ldots N_a ) = a(e-1)=v_p(\Delta)$ since assuming $\lfloor \frac{\log N }{\log p} \rfloor = \lfloor \frac{\log (N/a) }{\log p} \rfloor$ implies $a<p$ so that $v_p(i)=0$ for any $1\leq i \leq a$. Assume now, on the contrary, that $\lfloor \frac{\log N }{\log p} \rfloor \geq e$. Then we have $p ^e\leq N$ and $k\geq 1$; we let $N_i = i p^e$ for $1\leq i \leq k$, and we pick up $N_{k+1}$, ..., $N_a$ among the $\lfloor\frac{N }{ p^{e-1}}\rfloor - \lfloor\frac{N }{ p^e}\rfloor \geq a-k$ integers between $p^{e-1}$ and $N$ with $p$-adic valuation equal to $e-1$. Then for any $i\in\{1,\ldots,a\}$ we have $e-1\leq v_p(N_i)\leq \lfloor\frac{\log N }{\log p }\rfloor$, and for any $e'\in\{e, \ldots, \lfloor\frac{\log N }{\log p }\rfloor \}$ the number of indices $i$ such that $v_p(N_i)\geq e'$ is equal to $\lfloor\frac{N }{ p^{e'}}\rfloor$. Therefore we have $$v_p ( N_1\ldots N_a ) = a(e-1) + \sum_{e'=e}^{\lfloor\frac{\log N }{\log p }\rfloor} \Big\lfloor\frac{N }{ p^{e'}}\Big\rfloor =v_p(\Delta)$$ using Eq. (eqvpDel). Finally, for any prime $p$ we have found pairwise distinct integers $N_i$ between 1 and $N$ such that $v_p(\Delta) = v_p ( N_1\ldots N_a )$. Therefore $\Delta$ divides $\Delta_{a,N}$, and equality holds: $\Delta = \Delta_{a,N}$.

To conclude the proof of Lemma 2, we use this explicit expression of $\Delta$ to compute it asymptotically. In what follows we denote by $o(1)$ any quantity that tends to 0 as $N\to\infty$, with $a$ fixed. Since $\psi(N) = N(1+o(1))$ as recalled before the proof, we have $$\begin{aligned}
\log \Delta
&=& \sum_{p^e\leq N} f_{a,N}(p^e) \log p\\
&=& \sum_{p^e\leq N/a} a \log p + \sum_{k=1}^{a-1} \sum_{\frac{N}{k+1} < p^e\leq \frac{N}{k} } k \log p \\
&=& a \psi(N/a) + \sum_{k=1}^{a-1} k \Big( \psi(N/k) - \psi(N/(k+1))\Big)\\
&=& a \psi(N/a) + \sum_{k=1}^{a-1} k \psi(N/k) - \sum_{k=2}^{a } (k-1) \psi(N/ k ) \\
&=& a \psi(N/a) + \psi(N) - (a-1) \psi(N/a) + \sum_{k=2}^{a-1} \psi(N/k) \\
&=& \sum_{k=1}^a \psi(N/k) = N\Big( \sum_{k=1}^a 1/k+o(1)\Big).
\end{aligned}$$ At last, $\sum_{k=1}^a \frac1{k} - \log (a+1)$ is non-decreasing with respect to $a$, and tends to $\gamma$ as $a\to\infty$, so that $\sum_{k=1}^a 1/k \leq \gamma + \log (a+1)$ for any $a$. This concludes the proof of Lemma 2.

## Proof of Proposition 2

In this section we prove Proposition 2 by computing explicitly the coefficients $\vartheta_{k,i,j,i',j'}$. We shall use the following lemma, proved in [@Farhibinomial] using Kummer's theorem on $p$-adic valuations of binomial coefficients.

**Lemma 3**. *Let $N$ be a positive integer. The least common multiple of the binomial coefficients $\binom{N}{i}$, $0\leq i \leq N$, is equal to $\frac{d_{N+1}}{N+1}$ where $d_{N+1} = {\rm lcm}(1,2,\ldots,N+1)$.*

We shall use also the following notation. Given integers $0\leq \ell < k$, we denote by $H_{\ell,k}$ the set of all $\underline{h}= (h_0,\ldots,h_\ell)\in (\mathbb{N}^\ast)^{\ell+1}$ such that $h_0+\ldots+h_\ell=k$; we let $H_{\ell,k}=\emptyset$ if $\ell\geq k$ or $\ell<0$. In particular we have $H_{0,k} = \{ (k)\}$.

For $\underline{h}\in H_{\ell,k}$ and $T\in\mathbb{Z}$, we let $$\kappa(T,k,\underline{h}) = \frac{T(T-1)\ldots (T-k+2)}{\prod_{i=0}^{\ell-1} (T+1-\sum_{j=0}^i h_j)}$$ where empty products are taken equal to 1; notice that all factors in the denominator appear also in the numerator, so that $\kappa(T,k,\underline{h})\in\mathbb{Z}$. Here and below we agree that if $T = \sum_{j=0}^{i_0} h_j-1$ for some $i_0 \in \{0,\ldots,\ell-1\}$ (which is then unique), then the zero factor $T+1- \sum_{j=0}^{i_0} h_j$ has to be omitted from both products, in the numerator and in the denominator. In precise terms, we then have $T+2\leq k$ and $$\kappa(T,k,\underline{h}) = (-1)^{k-T}
\frac{T! (k-T-2)!}{ \prod_{0\leq i \leq \ell-1 \atop i\neq i_0} (T+1- \sum_{j=0}^{i} h_j) }.$$

The proof of Proposition 2 falls into 4 steps.

: Computation of $\vartheta_{k,i,j,i',j'}$ for $i\geq 1$.

The goal of this step is to prove by induction on $k\geq 1$ that for any $1\leq I \leq a$ and any $0\leq T \leq n$ we have $$\label{eqch1}
\vartheta_{k,i,T,I,T}= (-1)^{I-i} \sum_{\underline{h}\in H_{I-i,k}} \kappa(T,k,\underline{h})\quad\quad \mbox{ if } \max(1,I-k+1)\leq i \leq I$$ and $\vartheta_{k,i,j,I,T}= 0$ otherwise (with $i\geq 1$), namely $$\label{eqch2}
\vartheta_{k,i,j,I,T}= 0\quad \quad \mbox{ if ($i\geq 1$ and $j\neq T$) or ($i\geq I+1$) or ($1\leq i \leq I-k$).}$$ The value of $\vartheta_{k,0,j,i',j'}$, namely with $i=0$, will be computed in Step 2 below.

An equivalent form of Eqns. (eqch1) and (eqch2) is the following: for any $1\leq i \leq a$ and any $k\geq 1$, we have $$\label{eqch3}
P_{k,i}(z) = \sum_{t=1-k}^{n+1-k} z^t \Big( \sum_{I=i}^{\min(a,i+k-1)} c_{I,t+k-1} (-1)^{I-i} \sum_{\underline{h}\in H_{I-i,k}} \kappa(t+k-1,k,\underline{h}) \Big).$$ We shall now prove Eq. (eqch3) by induction on $k\geq 1$.

For $k=1$, Eq. (eqch3) holds trivially; indeed it reads $P_{1,i}(z) = \sum_{t=0}^{n} c_{i,t}z^t$ since $H_{0,1}=\{(1)\}$ and $\kappa(t,1,(1))=1$. Let us assume that Eq. (eqch3) holds for $k-1$, with $k\geq 2$. We recall that $$P_{k,i}(z) = P'_{k-1,i}(z) - \frac1{z} P_{k-1,i+1}(z) \mbox{ for } 1\leq i \leq a$$ with $P_{k-1,a+1}(z)=0$. Using Eq. (eqch3) twice (since it reduces to $0=0$ if $i=a+1$) we obtain: $$\begin{aligned}
P_{k,i}(z)
&=&
\sum_{t=2-k}^{n+2-k} tz^{t-1} \Big( \sum_{I=i}^{\min(a,i+k-2)} c_{I,t+k-2} (-1)^{I-i} \sum_{\underline{h}\in H_{I-i,k-1}} \kappa(t+k-2,k-1,\underline{h}) \Big)\\
&&
- z^{t-1} \Big( \sum_{I=i+1}^{\min(a,i+k-1)} c_{I,t+k-2} (-1)^{I-i-1} \sum_{\underline{h}\in H_{I-i-1,k-1}} \kappa(t+k-2,k-1,\underline{h}) \Big).
\end{aligned}$$ Letting $t'=t-1$ yields $$\begin{aligned}
P_{k,i}(z)
&=&
\sum_{t'=1-k}^{n+1-k} z^{t' } \sum_{I=i}^{\min(a,i+k-1)} c_{I,t'+k-1} (-1)^{I-i} \\
&&
\Big( (t'+1) \sum_{\underline{h}\in H_{I-i,k-1}} \kappa(t'+k-1,k-1,\underline{h})
+ \sum_{\underline{h}\in H_{I-i-1,k-1}} \kappa(t'+k-1,k-1,\underline{h}) \Big);
\end{aligned}$$ here zero terms have been added (namely $I= i+k-1$ in the first sum, if $i+k-1\leq a$, and $I=i$ in the second term; notice that $H_{k-1,k-1}=H_{-1,k-1}=\emptyset$). To conclude it is enough to check that for any $t$, $I$ such that $1-k\leq t\leq n+1-k$ and $i\leq I \leq \min(a,i+k-1)$ we have $$(t+1) \sum_{\underline{h}' \in H_{I-i,k-1}} \kappa(t +k-1,k-1,\underline{h}' ) +
 \sum_{\underline{h}'' \in H_{I-i-1,k-1}} \kappa(t +k-1,k-1,\underline{h}'' ) \label{eqch4}$$ $$= \sum_{\underline{h}\in H_{I-i,k}} \kappa(t +k-1,k ,\underline{h}).$$ Indeed let $\underline{h}= (h_0,\ldots, h_{I-i})\in H_{I-i,k}$, so that $h_0 + \ldots + h_{I-i} = k$. If $h_{I-i} \geq 2$ then $$\kappa(t +k-1,k,\underline{h}) = \frac{(t+k-1)(t+k-2)\ldots (t+1)}{\prod_{\lambda=0}^{I-i-1}(t+k-\sum_{j=0}^\lambda h_j)}
= (t+1)\, \kappa(t +k-1,k-1,\underline{h}' )$$ where $\underline{h}' = (h_0,\ldots, h_{I-i-1},h_{I-i} -1 ) \in H_{I-i,k-1}$. On the other hand, if $h_{I-i}=1$ then for $\lambda= I-i-1$ we have $t+k-\sum_{j=0}^\lambda h_j = t+1$ so that $$\kappa(t +k-1,k,\underline{h}) = \frac{(t+k-1)(t+k-2)\ldots (t+2)}{\prod_{\lambda=0}^{I-i-2}(t+k-\sum_{j=0}^\lambda h_j)}
= \kappa(t +k-1,k-1,\underline{h}'' )$$ where $\underline{h}'' = (h_0,\ldots, h_{I-i-1} ) \in H_{I-i-1,k-1}$. This concludes the proof of Eq. (eqch4), and by induction that of Eq. (eqch3).

: Computation of $\vartheta_{k,i,j,i',j'}$ for $i=0$.

In this step we shall prove that for any $k\geq 1$, any $0\leq j \leq n+k-1$, any $1\leq I \leq a$ and any $0\leq T \leq n$ we have $$\label{eqch8}
\vartheta_{k,0,j,I,T} \, \, \, \, = \, \, \, \, \sum_{\varepsilon= 0}^{ 1 } \, \, \alpha_\varepsilon\, \, \, \,
\sum_{s'=1-k}^{-1} \, \, \, \, \sum_{t'=-s'-k+\varepsilon}^{n-s'-k+\varepsilon} \, \, \, \, (-1)^{j-t'-k+1}$$ $$\cdot \binom{s'+k-1}{j-t'-k+1} \, \, \sum_{\alpha=-1-s'}^{k-2} \, \, (t'+1)_{s'+\alpha+1} \, \, (s'+\alpha+2)_{-s'-1} \, \, \vartheta_{k-\alpha-1,1,t'+s'-\varepsilon+k,I,T}$$ where the coefficients $\vartheta_{k-\alpha-1,1,t'+s'-\varepsilon+k,I,T}$ have been computed in Step 1, and $\alpha_\varepsilon$ comes from Eq. (eqrecpkijtechnique). In Eq. (eqch8) and throughout this paper, all binomial coefficients $\binom{r}{s}$ are considered to be zero if $s<0$ or $s>r$.

With this aim in mind we define functions $\psi_{k,\varepsilon}(z)$ for $k\geq 1$ and $\varepsilon\in\{0,1\}$ by letting $\psi_{1,\varepsilon}(z)=0$ and $$\label{eqch7}
\psi_{k,\varepsilon}(z) = \psi_{k-1,\varepsilon} ' (z) + z^{\varepsilon-1}(1-z)^{-1} P_{k-1,1}(z)$$ for any $k\geq 2$. Indeed the recurrence relation $$P_{k,0}(z) = P'_{k-1,0}(z) + \frac{\alpha_1z + \alpha_0}{z(1-z)} P_{k-1,1}(z)$$ with $P_{1,0}(z) = 0$ yields immediately, by induction: $$\label{eqch9}
P_{k,0}(z) = \sum_{\varepsilon=0}^1 \alpha_\varepsilon\psi_{k ,\varepsilon} (z) \mbox{ for any } k\geq 1.$$ Let us fix $\varepsilon\in\{0,1\}$. Then Eq. (eqch7) implies, by induction, $$\psi_{k,\varepsilon}(z) = \sum_{\alpha=0}^{k-2} \Big(\frac{d}{dz}\Big)^{\alpha} \Big( z^{\varepsilon-1}(1-z)^{-1} P_{k-\alpha-1,1}(z)\Big)$$ for any $k\geq 1$. Recall that $$P_{k-\alpha-1,1}(z) = \sum_{t=\alpha+2-k}^{n+\alpha+2-k} p_{k-\alpha-1,1,t+k-\alpha-2}z^t,$$ so that Leibniz' formula yields $$\psi_{k,\varepsilon}(z) = \sum_{\alpha=0}^{k-2} \sum_{t=\alpha+2-k}^{n+\alpha+2-k} p_{k-\alpha-1,1,t+k-\alpha-2}
\sum_{\beta=0}^\alpha \binom{\alpha}{\beta}
(t+\varepsilon-\beta)_\beta z^{t+\varepsilon-\beta-1} (\alpha-\beta)! (1-z)^{-1-\alpha+\beta}.$$ Letting $t'=t+\varepsilon-\beta-1$ and $s'=-1-\alpha+\beta$ we obtain $$\psi_{k,\varepsilon}(z) = \sum_{s' = 1-k}^{-1} \sum_{t' = -s' -k+\varepsilon}^{n-s'-k+\varepsilon} z^{t'}(1-z)^{s'}
\sum_{\alpha=-1-s' }^{k-2} p_{k-\alpha-1,1,t'+s' + k-\varepsilon}
(t'+1)_{s'+\alpha+1} (s'+\alpha+2)_{-s'-1} .$$ For $1-k\leq s'\leq -1$ and $-s' -k+\varepsilon\leq t' \leq n-s'-k+\varepsilon$ we write now $$\begin{aligned}
z^{t'} (1-z)^{s'}
&=& (1-z)^{1-k} \sum_{\sigma=0} ^{s'+k-1} (-1)^\sigma z^{\sigma+t'} \binom{s'+k-1}{\sigma}\\
&=&(1-z)^{1-k} \sum_{j=0} ^{n+k-1} (-1)^{j-t'-k+1} z^{ j+1-k } \binom{s'+k-1}{j-t'-k+1}
\end{aligned}$$ by letting $j = t'+\sigma+k-1$; notice that the values taken by $j$ form actually a subset of $\{0,\ldots,n+k-1\}$, but additional terms are zero because of the above-mentioned convention on binomial coefficients. Substituting this formula into the expression for $\psi_{k,\varepsilon}(z)$ and interchanging summations, we obtain $$\begin{aligned}
&& \psi_{k,\varepsilon}(z) =
 (1-z)^{1-k} \sum_{j=0}^{n+k-1} z^{j+1-k}
\sum_{s' = 1-k}^{-1} \sum_{t' = -s' -k+\varepsilon}^{n-s'-k+\varepsilon}
(-1)^{j-t'-k+1} \\
&&
\cdot \binom{s'+k-1}{j-t'-k+1} \sum_{\alpha=-1-s' }^{k-2} p_{k-\alpha-1,1,t'+s' + k-\varepsilon}
(t'+1)_{s'+\alpha+1} (s'+\alpha+2)_{-s'-1} .
\end{aligned}$$ Using Eqns. (eqch0) and (eqch9) this concludes the proof of Eq. (eqch8).

: Denominators.

In this step we prove that assertion $(ii)$ of Proposition 2 holds with $$\delta_k = d_k^2 \Delta_{a,\max(k,n)}$$ where $\Delta_{a,\max(k,n)}$ is defined in Lemma 2. Since $\gamma\leq 1$, the upper bound $(i)$ on $\delta_k$ in Proposition 2 follows immediately from Lemma 2 and the prime number theorem (namely, $d_k = \exp(k(1+o(1)))$).

Let us start with the case $i\geq 1$. We shall prove that $$\label{eqch11}
\frac{d_k \Delta_{a,\max(k,n)}}{(k-1)!} \kappa(T,k,\underline{h}) \in\mathbb{Z}$$ for any $k\geq 1$, $1\leq I \leq a$, $0\leq T \leq n$, $\max(1,I-k+1)\leq i \leq I$ and any $\underline{h}= (h_0,\ldots,h_{I-i})\in (\mathbb{N}^\ast)^{I-i+1}$ such that $h_0+\ldots+h_{I-i}=k$. Using Eq. (eqch3) proved in Step 1 and Eq. (eqch0), this is enough to prove assertion $(ii)$ of Proposition 2 for $i\geq 1$ (even in a stronger form, namely with $d_k \Delta_{a,\max(k,n)}$ instead of $\delta_k$) .

To prove (eqch11), we recall that $$\label{eqch10}
\kappa(T,k,\underline{h}) = \frac{T(T-1)\ldots (T-k+2)}{\prod_{\lambda=0}^{I-i-1} (T+1-\sum_{j=0}^\lambda h_j)}.$$ If $T-k+2> 0$ then $$\frac{d_k \Delta_{a,\max(k,n)}}{(k-1)!} \kappa(T,k,\underline{h}) = d_k \binom{T}{k-1} \frac{ \Delta_{a,\max(k,n)}}{\prod_{\lambda=0}^{I-i-1} (T+1-\sum_{j=0}^\lambda h_j)}\in\mathbb{Z}$$ using Lemma 2, since the $T+1-\sum_{j=0}^\lambda h_j$ are $I-i\leq a-1$ pairwise distinct integers between $0$ and $T\leq n\leq \max(k,n)$.

If $T-k+2\leq 0$ then a factor vanishes in the numerator of Eq. (eqch10). In proving Eq. (eqch11) we may assume that a factor vanishes in the denominator too, namely $T+1-\sum_{j=0}^{\lambda_0} h_j$, and in this case these factors have to be omitted in Eq. (eqch10); we then have $$\begin{aligned}
&&\frac{d_k \Delta_{a,\max(k,n)}}{(k-1)!} \kappa(T,k,\underline{h}) \\
&=& (-1)^{T-k+2} \frac{d_k}{(k-1){ \left( \begin{array}{c} k-2 \\ T \end{array} \right)}} \frac{ \Delta_{a,\max(k,n)}}{ \prod_{0 \leq\lambda\leq I-i-1\atop \lambda \neq \lambda_0 } (T+1-\sum_{j=0}^\lambda h_j)}\in\mathbb{Z}
\end{aligned}$$ using Lemmas 2 and 3, since the $T+1-\sum_{j=0}^\lambda h_j$ with $\lambda \neq \lambda_0$ are $I-i-1\leq a-2$ pairwise distinct integers between $T-k+2\geq -k+2$ and $T\leq n$, with distance at most $k-2$ from one another.

This concludes the proof of assertion $(ii)$ of Proposition 2 for $i\geq 1$; let us study the case $i=0$ now. Using Eq. (eqch8) (see Step 2) it is enough to prove that $$\frac{d_k^2 \Delta_{a,\max(k,n)}}{(k-1)!} \, \, \, \,
(t'+1)_{s'+\alpha+1} \, \, (s'+\alpha+2)_{-s'-1} \, \, \, \,
 \vartheta_{k-\alpha-1,1,t'+s'-\varepsilon+k,I,T}\, \, \, \,
\in\, \, \mathbb{Z}$$ for any $k\geq 1$, $0\leq \varepsilon\leq 1$, $1-k\leq s' \leq -1$, $-s'-k+\varepsilon\leq t' \leq n-s'-k+\varepsilon$, $-1-s'\leq \alpha\leq k-2$, $1\leq I \leq a$ and $0\leq T\leq n$. Now we have proved in the first part of Step 3 that for $i\geq 1$, assertion $(ii)$ of Proposition 2 holds with $d_k \Delta_{a,\max(k,n)}$ instead of $\delta_k$, so that $$\frac{d_k \Delta_{a,\max(k,n)}}{(k-1-\alpha)!} \vartheta_{k-\alpha-1,1,t'+s'-\varepsilon+k,I,T} \in\mathbb{Z}.$$ Since we have $$d_k \frac{ (k-1-\alpha)!}{ (k-1)!} (t'+1)_{s'+\alpha+1} (s'+\alpha+2)_{-s'-1}
 = \frac{ d_k }{{ \left( \begin{array}{c} k-1 \\ \alpha \end{array} \right)}} { \left( \begin{array}{c}  s'+\alpha+1+t' \\ t' \end{array} \right)}\in\mathbb{Z}$$ using Lemma 3, this concludes the proof of assertion $(ii)$ of Proposition 2.

: Absolute values.

To conclude the proof of Proposition 2, let us prove part $(iii)$. To bound $| \frac{\delta_k}{(k-1)!} \vartheta_{k,i,j,I,T}|$ from above, we begin with the case where $i\geq 1$ and use Eqns. (eqch1) and (eqch2) proved in Step 1. Whenever $1\leq I \leq a$ and $0\leq T \leq n$ we have ${\rm Card}\,H_{I-i,k}\leq k^{I-i}\leq k^a$ and, for any $\underline{h}\in H_{I-i,k}$: $$\Big| \frac{ \kappa(T,k,\underline{h}) }{(k-1)!} \Big| \leq \binom T {k-1}\leq 2^T\leq 2^n \mbox{ if } T\geq k-1,$$ whereas $$\Big| \frac{ \kappa(T,k,\underline{h}) }{(k-1)!} \Big| \leq \frac{1}{ (k-1) \binom {k-2}T }\leq 1 \mbox{ if } T\leq k-2.$$ Therefore we obtain $$\label{eqmajonvnvun}
 \Big| \frac{\delta_k}{(k-1)!} \vartheta_{k,i,j,I,T}\Big| \leq k^a 2^n \delta_k \mbox{ if } i \geq 1.$$

Let us deal now with the case $i=0$, using Eq. (eqch8) proved in Step 2. In this sum there are at most $2k(k-1)$ values of the triple $(\varepsilon, s',\alpha)$. For each value, the sum over $t'$ of $\binom{s'+k-1}{j-t'-k+1}$ is bounded by $2^{ s'+k-1}\leq 2^{k-1}$, and we have $$\Big| (t'+1)_{s'+\alpha+1} (s'+\alpha+2)_{-s'-1} \Big| =
\left\{
\begin{array}{l}
\alpha! \, \binom{t'+s'+\alpha+1}{t'}\leq \alpha! \, 2^n\mbox{ if } t'\geq 0, \\
\\
0 \mbox{ if } t'<0\leq t'+s'+\alpha+1, \\
\\
 \alpha! \, \binom{-t'-1}{ s'+\alpha+1} \leq \alpha! \, 2^{-t'}\leq \alpha ! \, 2^k \mbox{ if } t'+s'+\alpha+1<0.
\end{array}
\right.$$ Using Eq. (eqmajonvnvun) with $k-\alpha-1$ instead of $k$ we deduce that $$\begin{aligned}
\Big| (t'+1)_{s'+\alpha+1} (s'+\alpha+2)_{-s'-1} \frac{1}{(k-1)!} \vartheta_{k-\alpha-1,1,t'+s'-\varepsilon+k,I,T}\Big|
&\leq& \frac{ \alpha! \, (k-\alpha-2)! \, k^a\, 2^{n+\max(n,k)}}{(k-1)!} \\
& \leq & \frac{k^a\,  2^{n+\max(n,k)}}{k-1}
\end{aligned}$$ since $\binom{k-2}{\alpha}\geq 1$. Therefore Eq. (eqch8) yields $$\Big| \frac{\delta_k}{(k-1)!} \vartheta_{k,0,j,I,T}\Big| \leq \max( |\alpha_0|, |\alpha_1|)\ k^{a+1} \ 2^{n+k+\max(n,k)} \ \delta_k.$$ This concludes the proof of Proposition 2.

## Application of Siegel's lemma

In this section we use Proposition 2 to conclude the proof of Theorem 4. The notation is the one of §§3.1 and 3.2; the coefficients $c_{i,j}$ are related to the function $F_n(X)$ we are trying to construct by Eq. (eqfncij).

The asymptotic expansion of $F_n(t)$ at infinity reads $$\label{eqfnasy}
F_n(t) = \sum_{d=1}^\infty \frac{{\mathfrak A}_d}{t^d} \mbox{ for any $t$ such that $|t|>n$,}$$ where the coefficients ${\mathfrak A}_d$ are given explicitly (see [@FR Eq. (17)]) by $$\label{eqdefad}
{\mathfrak A}_d = (-1)^d \sum_{i=1}^{\min(a,d)} \sum_{j=0}^n (-1)^i \binom{d-1}{i-1} j^{d-i} c_{i,j}\mbox{ for any } d\geq 1.$$ The important point here is that we have also [@FR Proposition 2] $$\label{eqrnasy}
R_n(z) = \sum_{d=1}^\infty {\mathfrak A}_d (-1)^{d-1} \frac{(\log z)^{d-1}}{(d-1)!} \mbox{ for any $z\in\mathbb{C}$ such that $|z-1|<1$}$$ where $$\label{eqdefrn}
R_n(z) = \sum_{i=1}^a P_i(z) (-1)^{i-1} \frac{(\log z)^{i-1}}{(i-1)!}.$$ As in §3.2 we consider the rational functions $P_{k,i}(z)$ defined by $P_{1,i}(z) = P_i(z)$ and, for any $k\geq 2$, $$\label{eqpkdef}
 P_{k,i}(z) = P'_{k-1,i}(z) - \frac1{z} P_{k-1,i+1}(z) \mbox{ for } 1\leq i \leq a \\$$ where $P_{k-1,a+1}$ is understood as 0; however we are not interested in $P_{k,0}(z)$ here. Since the derivative of $(-1)^{i-1} \frac{(\log z)^{i-1}}{(i-1)!}$ is $\frac{-1}{z} (-1)^{i-2} \frac{(\log z)^{i-2}}{(i-2)!}$ if $i\geq 2$, and $0$ if $i=1$, we have $$R_n^{(k-1)}(z) = \sum_{i=1}^a P_{k,i}(z) (-1)^{i-1} \frac{(\log z)^{i-1}}{(i-1)!} \mbox{ for any } k\geq 1$$ and in particular $$\label{eqrnderiv}
R_n^{(k-1)}(1) = P_{k,1}(1).$$

Using Eqns. (eqfnasy), (eqrnasy) and (eqrnderiv) we see that the following assertions are equivalent:

-   As $|t|\to\infty$, $F_n(t) = O(|t|^{-\omega n})$.

-   For any $d\in\{1,\ldots,\omega n-1\}$, ${\mathfrak A}_d = 0$.

-   As $z\to 1$, $R_n(z) = O((z-1)^{\omega n -1})$.

-   For any $k\in \{1,\ldots,\omega n-1\}$, $R_n^{(k-1)}(1) = 0$.

-   For any $k\in \{1,\ldots,\omega n-1\}$, $P_{k,1}(1) = 0$.

Using the notation of §3.2, the last assertion reads $\sum_{j=0}^n p_{k,1,j} =0$, or equivalently $$\label{eqsyslin}
 \frac{\delta_k}{(k-1)!} \sum_{i'=1}^a\sum_{j'=0}^n \Big( \sum_{j=0}^n \vartheta_{k,1,j,i',j'} \Big) c_{i',j'} = 0 \mbox{ for any } k\in \{1,\ldots,\omega n-1\}$$ using the integer $\delta_k$ (which depends also on $a$ and $n$) provided by Proposition 2. This result asserts that (eqsyslin) is a linear system of $M_0 = \omega n-1$ equations in $N=a(n+1)$ unknowns $c_{i',j'}$, with integer coefficients bounded by $$\label{eqet2}
\Big| \frac{\delta_k}{(k-1)!} \sum_{j=0}^n \vartheta_{k,1,j,i',j'} \Big| \leq (n+1) k^a 2^n \delta_k \leq \Big( 2(a+1)^{ \omega}e^{3\omega}\Big)^{ n (1+o(1))}$$ as $n\to\infty$, since $k\leq \omega n -1$ and $\omega\geq 1$. To be consistent with the notation of Lemma 1, we let $H_k =\sqrt{N}(n+1)k^a 2^n \delta_k$ for $1\leq k\leq M_0=\omega n -1$.

In applying Lemma 1, for any $k\in\{\omega n, \ldots, \Omega n-1\}$ we consider ${\mathfrak A}_k$ given by Eq. (eqdefad) as a linear combination of the unknowns $c_{i',j'}$, with integer coefficients bounded in absolute value by $k^an^k$. We take $M = \Omega n-1$ and for each $k$ such that $M_0=\omega n -1 <k \leq M$ we let $G_k = \sqrt N r^{\Omega n-k}$ and $H_k = \sqrt{N}k^an^k$. Then Lemma 1 applies, and with its notation we have $$X \leq \sqrt N \, \, \Big[ N^{(\Omega n-1)/2} \, \, \Big(2 (a+1)^{ \omega}e^{3\omega}\Big)^{(\omega n -1)n (1+o(1))} \, \, \prod_{k=\omega n}^{\Omega n -1} r^{\Omega n-k} \Big]^{\frac1{N-M_0}}$$ using Eq. (eqet2), so that $$\begin{aligned}
\log X
&\leq& \frac{ n (1+o(1))}{a-\omega} \Big( \omega\log 2 + 3\omega^2 + \omega^2 \log (a+1) +\frac1{n^2} \sum_{k=\omega n}^{\Omega n -1} (\Omega n-k) \log r\Big)\\
&\leq& \frac{ n (1+o(1))}{a-\omega} \Big( \omega\log 2 + 3\omega^2 + \omega^2 \log (a+1) +\frac12 \Omega^2 \log r\Big).
\end{aligned}$$ This concludes the proof of Theorem 4.

# Main part of the proof

In this section we prove Theorem 1 stated in the introduction; we explain in §4.7 how to modify this proof and deduce Theorem 2. We explain the notation and sketch the proof in §4.1. We obtain an expansion in polylogarithms in §4.2. Then we study the resulting linear forms: their coefficients (§4.3) and their asymptotic behavior (§4.4). We apply a multiplicity estimate in §4.5, and conclude the proof in §4.6.

## Setting, notation and sketch of the proof

Let $a, r , \omega, \Omega\geq 1$ and $n\geq 2$, with $a,n\in\mathbb{Z}$, $r,\omega, \Omega\in\mathbb{Q}$, and $1\leq \omega\leq \Omega< a$; we assume $rn$, $\omega n$ and $\Omega n$ to be integers. We shall use also another parameter $h\in \mathbb{Z}$, with $0\leq h \leq a$, to bound the order $p$ of derivation with respect to $t$. In our application, $a$, $r$, $\omega$, $\Omega$, $h$ will be fixed and $n$ will tend to $\infty$. We refer to the end of this section (and to §4.6) for the choice of parameters.

Using Siegel's lemma we have constructed in Theorem 4 (see §3.1) integers $c_{i,j}\in\mathbb{Z}$, for $1\leq i \leq a$ and $0\leq j \leq n$, such that $$F_n(X) = \sum_{i=1}^a \sum_{j=0}^n \frac{c_{i,j}}{(X+j)^i} \in\mathbb{Q}(X)$$ satisfies $F_n(t) = O(|t|^{-\omega n})$ as $\vert t \vert \to\infty$, with $|c_{i,j}| \leq \chi^{n(1+o(1))}$ as $n\to \infty$, where $$\label{eqchi41}
\chi = \exp\Big(\frac{ \omega\log 2 + 3\omega^2 + \omega^2 \log (a+1) +\frac12 \Omega^2 \log r }{a-\omega}\Big).$$ We have also $$\label{eqmajofrakad}
|{\mathfrak A}_d |\leq r^{d-\Omega n} n^d d^a \chi^{n(1+o(1))}$$ for any $d < \Omega n$, where ${\mathfrak A}_d$ is defined by $$\label{eqfnad4}
 F_n(t) = \sum_{d=1}^\infty \frac{{\mathfrak A}_d}{t^d} \, \, \mbox{ if $|t|>n$;}$$ notice that the upper bound (eqmajofrakad) is interesting only when $\omega n \leq d < \Omega n$ since ${\mathfrak A}_d = 0$ for any $d< \omega n$.

For any $p\geq0$, the $p$-th derivative of $F_n$ is $$F_n^{(p)}(X) = \sum_{i=1}^a \sum_{j=0}^n \frac{c_{i,j}(-1)^p (i)_p}{(X+j)^{i+p}}$$ where $(i)_p=i(i+1)\ldots (i+p-1)$. As mentioned at the beginning of this section, we fix an additional parameter $h\geq 0$ with $h\leq a$. For any $z\in\mathbb{C}$ such that $\vert z \vert = 1$ and any $p\in\{0,\ldots,h\}$ we consider $$S_{n,p}(z)
 = z^{rn} \sum_{t=rn+1}^\infty \Big( F_n^{(p)}(t) z^{-t} - F_n^{(p)}(-t) z^{ t} \Big)$$ which is convergent since $F_n^{(p)}(t) = O(|t|^{-\omega n})$ as $\vert t \vert \to\infty$, with $\omega n \geq 2$. The point here is that even zeta values should not appear in the linear combination we are trying to construct. A symmetry phenomenon (related to well-poised hypergeometric series) is used in general to obtain this property. However we have to consider derivatives of $S_{n,p}(z)$ to apply the multiplicity estimate, and this property is not transfered to derivatives. We overcome this difficulty as in [@SFcaract], by considering the functions ${\rm Li}_i(1/z)-(-1)^i {\rm Li}_i(z)$ instead of just ${\rm Li}_i(1/z)$. This leads to the definition above of $S_{n,p}(z)$, instead of simply $z^{rn} \sum_{t=rn+1}^\infty F_n^{(p)}(t) z^{-t}$.

We let also $$\label{eq44bis}
P_i(z) = \sum_{j=0}^n c_{i,j}z^j \mbox{ for } 1\leq i \leq a$$ and we shall prove in Lemma 4 that, if $z\neq 1$, $$\label{eq410}
S_{n,p}(z)
 = V_p(z) + \sum_{i=1}^a z^{rn} P_i(z) (-1)^p (i)_p \Big( {\rm Li}_{i+p}(1/z) - (-1)^{i+p} {\rm Li}_{i+p}(z) \Big)$$ for some polynomial $V_p\in\mathbb{Q}[X]$ of degree at most $2rn$. For $k\geq 1$ we shall consider the $(k-1)$-th derivative $S_{n,p}^{(k-1)}(z)$ of $S_{n,p}(z)$. Since the coefficients of the polynomial $V_p$ have large denominators (that would ruin our Diophantine application), we shall be interested only in integers $k$ such that $k-1\geq 2rn+1>\deg V_p$, so that $V_p^{(k-1)}=0$.

For $0\leq p \leq h$ and $1 \leq i \leq a$ we let $$\label{eqdefqp}
Q^{[p]}_{i+p}(z) = z^{rn} P_i(z) (-1)^p (i)_p$$ and also $Q^{[p]}_i(z)=0$ for $i \in \{1,\ldots,p\} \cup \{a+p+1,\ldots,a+h\}$. Then Eq. (eq410) reads $$\label{eqdevsnp}
S_{n,p}(z)=V_p(z)+\sum_{i=1}^{a+h} Q^{[p]}_i(z) \Big( {\rm Li}_i(1/z) - (-1)^{i} {\rm Li}_{i}(z)\Big).$$ Now let $Q^{[p]}_{1,0}(z) = 0$, $Q^{[p]}_{1,i}(z) = Q^{[p]}_i(z)$ for any $i\in\{1,\ldots,a+h\}$, and for $k\geq 2$: $$\label{eqdefqpk}
\left\{ \begin{array}{l}
 Q^{[p]}_{k,i}(z) = { Q^{[p]_{'}} _{k-1,i}}(z) - \frac1{z} Q^{[p]}_{k-1,i+1}(z) \mbox{ for } 1\leq i \leq a+h\\
 Q^{[p]}_{k,0}(z) = { Q^{[p]_{'}} _{k-1,0}}(z) + \frac{z+1}{z(1-z)} Q^{[p]}_{k-1,1}(z)
\end{array}\right.$$ where $Q^{[p]}_{k-1,a+h+1}$ is taken to be the zero function. In particular we have $Q^{[p]}_{k,i}(z)=0$ for any $i\in \{a+p+1,\ldots,a+h\}$, but not (in general) for $0\leq i \leq p$. Since the derivative of ${\rm Li}_i(1/z) - (-1)^{i} {\rm Li}_{i}(z)$ is $\frac{z+1}{z(1-z)}$ for $i=1$, and $- \frac1{z} \Big( {\rm Li}_{i-1}(1/z) - (-1)^{i-1} {\rm Li}_{i-1}(z)\Big)$ for $i\geq 2$, we have $$\label{eq33nv}
S_{n,p}^{(k-1)}(z)= Q^{[p]}_{k,0}(z) + \sum_{i=1}^{a+h} Q^{[p]}_{k,i}(z) \Big( {\rm Li}_i(1/z) - (-1)^{i} {\rm Li}_{i}(z)\Big) \mbox{ for any } k\geq 2rn+2$$ since $\deg V_p \leq 2rn$; when $1 \leq k \leq 2rn+1$ an additional term $V_p^{(k-1)}(z)$ appears on the right hand side. The point is that we have now many linear forms for each value of $n$, as $k$ and $p$ vary. This is necessary to apply the multiplicity estimate, and then Siegel's linear independence criterion.

For any $k\geq 2rn+2$ we let $$\label{eqdeflikn}
\ell_{p,k,i}^{(n)}= (-2)^{k-1} \frac{\delta_k}{(k-1)!} Q^{[p]}_{k,i} (-1) \mbox{ for } 0\leq i \leq a+h$$ where $\delta_k= \delta_k (a+h,(r+1)n, 1,1)$ is given by Proposition 2 in §3.2 with $a$ replaced by $a+h$ and $n$ by $(r+1)n$; then Eq. (eq33nv) yields $$\label{eqFL}
 (-2)^{k-1} \frac{\delta_k}{(k-1)!}
S_{n,p}^{(k-1)}(-1) = \ell_{p,k,0}^{(n)}+ \sum_{i=1}^{a+h} \ell_{p,k,i}^{(n)}( 1- (-1)^{i}) {\rm Li}_i(-1) .$$ These are the linear forms we are interested in, with $0\leq p \leq h$ and $2rn+2 \leq k\leq \kappa n$ (where $\kappa\in\mathbb{Q}$ is a fixed parameter such that $2r<\kappa< \omega$). We shall prove in Lemma 5 that their coefficients are not too large integers, namely $\ell_{p,k,i}^{(n)}\in\mathbb{Z}$ and $$| \ell_{p,k,i}^{(n)}| \leq \beta^{n(1+o(1))} \mbox{ with }
 \beta = \chi \Big( e^3 (2a+1) \Big)^\kappa\cdot 4^{\kappa+r+1}.$$ Then in Lemma 6 we shall prove that these linear forms are small : $$\Big| \ell_{p,k,0}^{(n)}+ \sum_{i=1}^{a+h} \ell_{p,k,i}^{(n)}\Big( 1 - (-1)^i\Big) {\rm Li}_i(-1) \Big| \leq \alpha^{n(1+o(1))} \mbox{ with }
\alpha = \chi r^{-\Omega}( 2e^4(2a+1))^{\kappa} .$$ Assume that $(h+1)(\kappa-2r)+\omega>a$, and that $n$ is sufficiently large. Then using the generalization of Shidlovsky's lemma stated in §2.3 we prove in §4.5 that there are sufficiently many linearly independent linear forms among them; this allows us in §4.6 to apply Siegel's linear independence criterion (recalled in §2.2) and deduce that $$\dim_\mathbb{Q}{\rm Span}_\mathbb{Q}(\{1\}\cup \{ (1-(-1)^i) {\rm Li}_i(-1), \, 1\leq i \leq a+h\}) \geq 1 - \frac{\log \alpha}{\log \beta } .$$ Choosing appropriate parameters (namely $r =3.9$, $\kappa= 10.58$, $\omega= 11.58$, $\Omega\in\mathbb{Q}$ sufficiently close to $3.9 \sqrt{a \log a}$, and $h =0.36\ a$) enables one to conclude the proof of Theorem 1 (see §4.6 for details); recall that $(1-(-1)^i){\rm Li}_i(-1)$ vanishes when $i$ is even, and is equal to $2(2^{1-i}-1)\zeta(i)$ when $i\geq 3$ is odd.

## Expansion in polylogarithms

**Lemma 4**. *For any $p\in\{0,\ldots,h\}$ there exists a polynomial $V_p\in\mathbb{Q}[X]$ of degree at most $2rn$ such that, for any $z\in\mathbb{C}$ with $\vert z\vert =1$ and $z \neq 1$, $$S_{n,p}(z)
 = V_p(z) + \sum_{i=1}^a z^{rn} P_i(z) (-1)^p (i)_p \Big( {\rm Li}_{i+p}(1/z) - (-1)^{i+p} {\rm Li}_{i+p}(z) \Big).$$*

of Lemma 4: To begin with, we let $$\label{eqdefsninf}
 S_{n,p}^{[\infty]}(z)
 = z^{rn} \sum_{t=rn+1}^\infty F_n^{(p)}(t) z^{-t}$$ for $z\in \mathbb{C}$, $|z|\geq1$, $z\neq 1$. We have $$\begin{aligned}
 S_{n,p}^{[\infty]}(z)
&=& \sum_{t=rn+1}^\infty \sum_{i=1}^a \sum_{j=0}^n \frac{c_{i,j}(-1)^p (i)_p}{(t+j)^{i+p}} z^{rn-t} \\
&=& \sum_{i=1}^a \sum_{j=0}^n c_{i,j}(-1)^p (i)_p \sum_{\ell =rn+1+j}^\infty \frac{z^{rn-\ell+j}}{ \ell^{i+p}} \\
&& \quad \quad \quad \mbox{since this series is convergent (because $|z|\geq1$ and $z\neq 1$)} \\
&=& \sum_{i=1}^a \sum_{j=0}^n c_{i,j}(-1)^p (i)_p \Big( z^{rn+j} {\rm Li}_{i+p}(1/z) - \sum_{\ell =1}^{rn+j} \frac{z^{rn-\ell+j}}{ \ell^{i+p}}\Big)
\end{aligned}$$ so that $$S_{n,p}^{[\infty]}(z) = V_p^{[\infty]}(z) + \sum_{i=1}^a z^{rn} P_i(z) (-1)^p (i)_p {\rm Li}_{i+p}(1/z)$$ where (as defined above) $$P_i(z) = \sum_{j=0}^n c_{i,j}z^j \mbox{ for } 1\leq i \leq a$$ and $$\label{eqdefVzero}
V_p^{[\infty]}(z) = - \sum_{i=1}^a \sum_{j=0}^n c_{i,j}(-1)^p (i)_p \sum_{t=0}^{rn+j-1} \frac{z^{t}}{(rn+j-t)^{i+p}} \in\mathbb{Q}[z].$$ Observe that the polynomials $P_i$ have degree at most $n$, and do not depend on $p$, whereas $V_p^{[\infty]}$ depends on $p$ and has degree at most $(r+1)n-1$.

On the other hand we consider, for $z\in \mathbb{C}$ with $|z|\leq1$ and $z\neq 1$, $$\begin{aligned}
S_{n,p}^{[0]}(z)
&=& z^{rn} \sum_{t=rn+1}^\infty F_n^{(p)}(-t) z^{t}
\\
&=& \sum_{t=rn+1}^\infty \sum_{i=1}^a \sum_{j=0}^n \frac{c_{i,j}(-1)^p (i)_p}{(-t+j)^{i+p}} z^{rn+t} \\
&=& \sum_{i=1}^a \sum_{j=0}^n c_{i,j}(-1)^p (i)_p (-1)^{i+p} \sum_{\ell =rn+1-j}^\infty \frac{z^{rn+\ell+j}}{ \ell^{i+p}}\nonumber \\
&=& \sum_{i=1}^a \sum_{j=0}^n c_{i,j}(-1)^p (i)_p (-1)^{i+p} \Big( z^{rn+j} {\rm Li}_{i+p}(z) - \sum_{\ell =1}^{rn-j} \frac{z^{rn+\ell+j}}{ \ell^{i+p}}\Big)\nonumber
\end{aligned}$$ so that $$S_{n,p}^{[0]}(z) = V_p^{[0]}(z) + \sum_{i=1}^a z^{rn} P_i(z) (-1)^p (i)_p (-1)^{i+p} {\rm Li}_{i+p}(z)$$ with the same polynomials $P_i$, and $$\label{eqdefVinf}
V_p^{[0]}(z) = - \sum_{i=1}^a \sum_{j=0}^n c_{i,j}(-1)^i (i)_p \sum_{t=rn+j+1}^{2rn} \frac{z^{t}}{(t-rn -j)^{i+p}} \in\mathbb{Q}[z].$$ Observe that $V_p^{[0]}$ has degree at most $2rn$ and is a multiple of $z^{rn+1}$. Since $S_{n,p}(z) = S_{n,p}^{[\infty]}(z) - S_{n,p}^{[0]}(z)$, we let $V_p(z) = V_p^{[\infty]}(z) - V_p^{[0]}(z)$; this concludes the proof of Lemma 4.

## Coefficients of the linear forms

For any algebraic number $\xi$, we denote by $\mathord{
 \mathpalette\@house{\xi}
 }$ its house, i.e. the maximum modulus of its Galois conjugates. To prepare for the proof of Theorem 2 (see §4.7) we shall estimate the coefficients of the linear forms in a slightly more general setting than what is needed in the proof of Theorem 1.

Let $z_0\in\overline{\mathbb{Q}}$ be such that $|z_0| \geq 1$ and $z_0\neq 1$; denote by $q\in\mathbb{N}^\ast$ a denominator of $z_0$, i.e. such that $qz_0 \in {\mathcal O}_{\mathbb{Q}(z_0)}$ where ${\mathcal O}_{\mathbb{Q}(z_0)}$ is the ring of integers of $\mathbb{Q}(z_0)$. For any $k\geq 1$ we let $$\label{eqdefl43}
\ell_{p,k,i}^{(n)}(z_0) = q^{(r+1)n+k-1} z_0^{k-1}(1-z_0)^{k-1} \frac{\delta_k}{(k-1)!} Q^{[p]}_{k,i} (z_0) \mbox{ for } 0\leq i \leq a+h$$ where $\delta_k=\delta_k (a+h,(r+1)n,1,1)$ is given by Proposition 2 in §3.2, and the rational functions $Q^{[p]}_{k,i} (z)$ are defined by Eq. (eqdefqpk). The special case needed in the proof of Theorem 1 is $z_0=-1$, $q=1$; then $\mathbb{Q}(z_0) = \mathbb{Q}$ and ${\mathcal O}_{\mathbb{Q}(z_0)}= \mathbb{Z}$, and $\ell_{p,k,i}^{(n)}(z_0) = \ell_{p,k,i}^{(n)}$ (see Eq. (eqdeflikn)).

**Lemma 5**. *We have $\ell_{p,k,i}^{(n)}(z_0) \in{\mathcal O}_{\mathbb{Q}(z_0)}$ for any $p\in\{0,\ldots,h\}$, any $i\in\{0,\ldots,a+h\}$ and any $k\geq 1$. Moreover, provided $k\leq\kappa n$ with a fixed $\kappa\geq r+1$ (independent from $n$), we have as $n\to\infty$: $$\mathord{
 \mathpalette\@house{\ell_{p,k,i}^{(n)}(z_0)}
 }
 \leq \beta^{n(1+o(1))} \mbox{ with } \beta = \chi \Big( 8 e^3 (2a+1) \Big)^\kappa\cdot \Big( q\max(1,
 \mathord{
 \mathpalette\@house{z_0}
 }
 ,
 \mathord{
 \mathpalette\@house{ 1-z_0}
 }
 ) \Big)^{\kappa+r+1}$$ where $\chi$ is defined by Eq. (eqchi41).*

of Lemma 5: We fix $p$ and apply the results of §3.2. With respect to the notation of that section, $P_i(z)$ is replaced with $Q^{[p]}_i(z)$, $a$ with $a+h$ and $n$ with $(r+1)n$; recall that $\deg Q^{[p]}_i\leq (r+1)n$ for any $i\in\{1,\ldots,a+h\}$ (see Eq. (eqdefqp) and the line following it). We take $\alpha_0=\alpha_1= 1$ in the notation of §3.2, so that Eqns. (eqrecpkijtechnique) and (eqdefqpk) are consistent. We write $$\left\{ \begin{array}{l}
 z^{k-1} Q^{[p]}_{k,i}(z) = \sum_{j=0}^{(r+1)n} q_{k,i,j} z^j \mbox{ if } i\geq 1,\\
z^{k-1} (1-z)^{k-1} Q^{[p]}_{k,0}(z)= \sum_{j=0}^{(r+1)n+k-1} q_{k,0,j} z^j.
\end{array}\right.$$ Then Eq. (eqdefl43) reads $$\label{eq792}
 \ell_{p,k,i}^{(n)}(z_0) =
q^{k-1} (1-z_0)^{k-1} \sum_{j=0}^{(r+1)n} \frac{\delta_k}{(k-1)!} q_{k,i,j} q^{(r+1)n} z_0^j \mbox{ for } 1\leq i \leq a+h,$$ and $$\label{eq793}
\ell_{p,k,0}^{(n)}(z_0) = \sum_{j=0}^{(r+1)n+k-1} \frac{\delta_k}{(k-1)!} q_{k,0,j} q^{(r+1)n+k-1} z_0^j.$$ To be consistent with the notation of §3.2 we write also $Q^{[p]}_i(z)= \sum_{j=0}^{(r+1)n} c'_{i,j} z^j$ for $1\leq i \leq a+h$. Combining Eq. (eqch0) with part $(ii)$ of Proposition 2, we deduce that $\frac{\delta_k}{(k-1)!} q_{k,i,j} \in\mathbb{Z}$ for any $k$, $i$, $j$, since $c'_{i',j'} \in\mathbb{Z}$ for any $i'$, $j'$. Moreover, part $(iii)$ of Proposition 2 and Eq. (eqch0) yield $$\Big| \frac{\delta_k}{(k-1)!} q_{k,i,j} \Big| \leq k^{a+h+1} \, \, 8^{\max(k, (r+1)n)} \, \,\delta_k \, \, (a+h) \, \,((r+1)n+1) \, \,\max_{i',j'} |c'_{i',j'}|$$ for any $k$, $i$, $j$, with $\delta_k \leq ( e^3 (a+h+1) )^{\max(k, (r+1)n)}$ according to part $(i)$ -- recall that Proposition 2 is applied with $a+h$ and $(r+1)n$ instead of $a$ and $n$, respectively. Since $a+h\leq 2a$, we deduce that $$\Big| \frac{\delta_k}{(k-1)!} q_{k,i,j} \Big| \leq 2 \, \,k^{2a+1} \, \, (8 e^3 (2a+1) )^{\max(k, (r+1)n)} \, \,a((r+1)n+1) \, \,\max_{i',j'} |c'_{i',j'}|.$$ Using Eqns. (eq792) and (eq793) we obtain $\ell_{p,k,i}^{(n)}(z_0) \in {\mathcal O}_{\mathbb{Q}(z_0)}$ for any $i \in \{0,\ldots,2a\}$, any $k\geq 1$ and any $p\in\{0,\ldots,h\}$, and $$\begin{aligned}
 \vert \ell_{p,k,i}^{(n)}(z_0) \vert &\leq &
2 \, \, k^{2a+1} \, \,( 8 e^3 (2a+1) )^{\max(k, (r+1)n)} \, \,a((r+1)n+k)^2 \, \,\max_{i',j'} |c'_{i',j'}| \\
 &&\quad \cdot \,
q^{(r+1)n+k-1} \, \, \max(1,
 \mathord{
 \mathpalette\@house{ z_0}
 }
^{(r+1)n}) \, \,\max( 1,
 \mathord{
 \mathpalette\@house{ 1-z_0}
 }
 ^{k-1} ,
 \mathord{
 \mathpalette\@house{z_0}
 }
^{k-1} ) .
\end{aligned}$$ Now Eq. (eqdefqp) and Theorem 4 yield $\max_{i',j'} |c'_{i',j'}| \leq (a)_a \chi^{n(1+o(1))}$ since $h\leq a$. Using the assumption $k\leq \kappa n$ with $\kappa\geq r+1$, this concludes the proof of Lemma 5.

## Asymptotic estimate of the linear forms

Let $z_0\in\overline{\mathbb{Q}}$ be such that $|z_0| = 1$; in this section $z_0$ could be equal to 1. We shall take $z_0=-1$ in the proof of Theorem 1, and adapt the proof of Lemma 6 below in §4.7 to prove Theorem 2. Recall that $\delta_k=\delta_k (a+h,(r+1)n, \alpha_0,\alpha_1)\in\mathbb{N}^\ast$ has been defined in Proposition 2 (in which $a$ should be replaced with $a+h$ and $n$ by $(r+1)n$), and $\chi$ in Theorem 4.

**Lemma 6**. *Assume that $r\geq 2$, $0 \leq p \leq h$, and $2rn+2\leq k \leq \kappa n$, with $\kappa< \omega$. Then we have $$\Big| \frac{\delta_k}{(k-1)!} S_{n,p}^{(k-1)}(z_0)\Big| \leq \alpha_0^{n(1+o(1))} \mbox{ with }
\alpha_0 = \chi r^{-\Omega}( e^4(2a+1))^{\kappa} .$$*

of Lemma 6: Recall that $S_{n,p}(z)=S_{n,p}^{[\infty]}(z)- S_{n,p}^{[0]}(z)$ with the notation introduced in the proof of Lemma 4. Taking the $p$-th derivative of Eq. (eqfnad4) (see §4.1) yields $F_n^{(p)}(t)=\sum_{d=1}^{\infty} \frac{{\mathfrak A}_d (-1)^p (d)_p}{t^{d+p}}$ for $|t|>n$. By definition of $S_{n,p}^{[\infty]}(z)$ (see Eq. (eqdefsninf) in §4.2) we obtain $$\label{eq1235}
S_{n,p}^{[\infty]}(z) = \sum_{t=rn+1}^\infty \sum_{d=1}^\infty \frac{{\mathfrak A}_d (-1)^p (d)_p}{t^{d+p}} z^{rn-t} \mbox{ for } |z| \geq 1, \, z\neq 1.$$ Now Theorem 4 asserts that $F_n(t)=O(|t|^{-\omega n})$ as $|t|\to\infty$, so that ${\mathfrak A}_d=0$ for any $d\in\{1,\ldots,\omega n -1\}$: the sum on $d$ in Eq. (eq1235) starts only at $d=\omega n$. Therefore we have for any $k\geq1$: $$\frac{\delta_k}{(k-1)!} S_{n,p}^{[\infty] (k-1) }(z) = (-1)^{k-1} \delta_k \sum_{t=rn+1}^\infty \sum_{d= \omega n}^\infty \frac{{\mathfrak A}_d (-1)^p (d)_p}{t^{d+p}} \binom{t-rn+k-2}{k-1} z^{rn-t-k+1}.$$ Since $\vert z \vert \geq 1$ and $t^p \geq 1$ we obtain $$\Big| \frac{\delta_k}{(k-1)!} S_{n,p}^{[\infty] (k-1) }(z)\Big| \leq \delta_k \sum_{t=rn+1}^\infty \binom{t-rn+k-2}{k-1}
 \Big( \frac{n}{t }\Big)^{\omega n}
\sum_{d= \omega n}^\infty \frac{ | {\mathfrak A}_d | (d)_p }{t^{d-\omega n}}n^{-\omega n}.$$ We bound $| {\mathfrak A}_d |$ trivially (using Eq. (eqdefad) and assertion $(ii)$ of Theorem 4) for $d\geq \Omega n$, and we use assertion $(iii)$ of Theorem 4 for $d$ such that $\omega n \leq d < \Omega n$. Therefore we have $$\label{eq12357}
\Big| \frac{\delta_k}{(k-1)!} S_{n,p}^{[\infty] (k-1) }(z)\Big| \leq \delta_k \chi^{n(1+o(1))} \sum_{t=rn+1}^\infty \binom{t-rn+k-2}{k-1}
 \Big( \frac{n}{t }\Big)^{\omega n}
\sum_{d= \omega n}^\infty u_{t,d}$$ where the sequence $o(1)$ does not depend on $k$, nor on $p$, and tends to 0 as $n\to\infty$; we define $u_{t,d}$ by $$u_{t,d} = (d)_p d^a (n/t)^{d-\omega n} \mbox{ for } d \geq \Omega n$$ and $$u_{t,d} = r^{d-\Omega n} (d)_p d^a (n/t)^{d-\omega n} \mbox{ for } \omega n \leq d < \Omega n.$$ Let us bound the term $\sum_{d= \omega n}^\infty u_{t,d}$ in Eq. (eq12357). For any $d \geq \Omega n$ we have $u_{t,d+1}/u_{t, d} \leq (1+\frac{p}{d}) \cdot (1+\frac1{d})^a \cdot \frac1r \leq\frac3{2r}$ for any $t\geq rn+1$, provided $n$ is large enough (using the assumption that $\Omega>0$). Since $r\geq 2$ we obtain $$\label{eq319ter}
\sum_{d= \Omega n}^\infty u_{t,d} \leq u_{t,\Omega n} \sum_{d= \Omega n}^\infty \Big(\frac34\Big) ^{d-\Omega n} \leq 4 r^{(\omega-\Omega) n}(\Omega n)_p (\Omega n)^a$$ for any $t\geq rn+1$. On the other hand, for $\omega n \leq d < \Omega n$ we have $$u_{t,d} = r^{(\omega-\Omega) n} (d)_p d^a (rn/t)^{d-\omega n} \leq r^{(\omega-\Omega) n} ( \Omega n)_p ( \Omega n)^a .$$ Combining this upper bound with Eq. (eq319ter) yields $$\sum_{d= \omega n}^\infty u_{t,d} \leq (4 + (\Omega-\omega)n) r^{(\omega-\Omega) n} (\Omega n)_p (\Omega n)^a \leq r^{(\omega-\Omega) n} \chi^{o(n)};$$ here and below, the sequences $o(\cdots)$ may depend on $p$ (but not on $k$). Using Eq. (eq12357) we obtain $$\label{eq319bis}
 \Big| \frac{\delta_k}{(k-1)!} S_{n,p}^{[\infty] (k-1) }(z)\Big| \leq r^{-\Omega n} \delta_k \chi^{n(1+o(1))} \sum_{t=rn+1}^\infty \binom{t-rn+k-2}{k-1} \Big( \frac{rn}{t }\Big)^{\omega n} .$$ We let $\sigma = \frac{k-1}{rn}$ so that $\sigma > 1$. Let $t>rn$; then we have $t-rn+k-2 \leq t + (\sigma-1)rn < \sigma t$ so that $$\binom{t-rn+k-2}{k-1} \Big( \frac{rn}{t }\Big)^{\omega n-2} \leq \frac{(\sigma t)^{k-1}}{(k-1)!} \Big( \frac{rn}{t }\Big)^{\omega n-2} \leq
 \frac{\sigma ^{k-1} (rn) ^{k-1} }{(k-1) ^{k-1} e^{-k+1}} \Big( \frac{rn}{t }\Big)^{\omega n-k-1} \leq e^{k-1}$$ since $\frac{rn}{t }\leq 1$ and $k+1\leq \kappa n +1 \leq \omega n$; recall that $(k-1)!\geq (\frac{k-1}{e})^{k-1}$, and $\sigma r n = k-1$ by definition of $\sigma$. This proves that $$\label{eqmajolemasytemp}
 \sum_{t=rn+1}^\infty \binom{t-rn+k-2}{k-1} \Big( \frac{rn}{t }\Big)^{\omega n } \leq r^2 n^2 e^{k-1} \pi^2/6.$$ Using Eq. (eq319bis), Theorem 4 and assertion $(i)$ of Proposition 2 (where $a$ is replaced with $a+h\leq 2a$ and $n$ with $(r+1)n$), we obtain $$\Big| \frac{\delta_k}{(k-1)!} S_{n,p}^{[\infty] (k-1) }(z)\Big| \leq \alpha_0^{n(1+o(1))} .$$

We now turn to $S_{n,p}^{[0](k-1) }(z)$ (recall that $S_{n,p}(z) = S_{n,p}^{[\infty]}(z) - S_{n,p}^{[0]}(z)$). As for $S_{n,p}^{[\infty]}$ above, we have $$S_{n,p}^{[0]}(z) = \sum_{t=rn+1}^\infty \sum_{d=\omega n }^\infty \frac{{\mathfrak A}_d (-1)^p (d)_p}{(-t)^{d+p}} z^{rn+t} \mbox{ for } |z| \leq 1, \, z\neq 1,$$ so that, for any $k\geq 2rn+2$, $$\frac{\delta_k}{(k-1)!} S_{n,p}^{[0](k-1) }(z) = \delta_k \sum_{t=k-1-rn}^\infty \sum_{d= \omega n}^\infty \frac{{\mathfrak A}_d (-1)^d (d)_p}{t^{d+p}} \binom{rn+t}{k-1} z^{rn+t-k+1}.$$ We have $$\Big| \frac{\delta_k}{(k-1)!} S_{n,p}^{[0](k-1) }(z) \Big| \leq \delta_k \chi^{n(1+o(1))} \sum_{t=k-1-rn}^\infty \binom{rn+t}{k-1}
 \Big( \frac{n}{t }\Big)^{\omega n}
\sum_{d= \omega n}^\infty u_{t,d}$$ with the same $u_{t,d}$ as above, so that $$\label{eq319bisdeux}
 \Big| \frac{\delta_k}{(k-1)!} S_{n,p}^{[0](k-1) }(z) \Big| \leq r^{-\Omega n } \delta_k \chi^{n(1+o(1))} \sum_{t=k-1-rn}^\infty \binom{rn+t}{k-1} \Big( \frac{rn}{t }\Big)^{\omega n} .$$ Now we have $t+rn\leq t-rn+k-2$ for any $t$, so that $\binom{rn+t}{k-1} \leq \binom{t-rn+k-2}{k-1}$: we obtain the same upper bound as in Eq. (eq319bis), and deduce in the same way $$\Big| \frac{\delta_k}{(k-1)!} S_{n,p}^{[0](k-1) }(z) \Big| \leq \alpha_0^{n(1+o(1))} .$$ Since $S_{n,p}^{(k-1)}(z ) = S_{n,p}^{[\infty] (k-1) }(z) - S_{n,p}^{[0](k-1) }(z)$, taking $z=z_0$ this concludes the proof of Lemma 6.

## Multiplicity estimate

In this section we apply the multiplicity estimate stated in §2.3 to prove Proposition 3 below, which makes it possible to apply the refinement of Siegel's linear independence criterion proved in §2.2.

To state Proposition 3, recall that $P_i(z) = \sum_{j=0}^n c_{i,j}z^j$ for $1\leq i \leq a$. Since the integers $c_{i,j}$ are not all zero, we may consider $$b = \max\{ i\in\{1,\ldots,a\}, \, \exists j \in\{0,\ldots,n\}, \, c_{i,j}\neq 0\}.$$ Then we have $1\leq b \leq a$, $P_b\neq 0$, and $P_{b+1}= \ldots = P_a=0$. Eqns. (eqdefqp), (eqdefqpk) and (eqdeflikn) show that $Q^{[p]}_i(z)$, $Q^{[p]}_{k,i}(z)$ and $\ell_{p,k,i}^{(n)}$ all vanish when $b+p+1\leq i \leq a+h$: Eq. (eqFL) becomes a linear form in 1 and the numbers $(1-(-1)^i) {\rm Li}_{i}(-1)$ for $1 \leq i \leq b+h$, namely $$\label{eqformeslinlemz}
 (-2)^{k-1} \frac{\delta_k}{(k-1)!}
S_{n,p}^{(k-1)}(-1) = \ell_{p,k,0}^{(n)}+ \sum_{i=1}^{b+h} \ell_{p,k,i}^{(n)}( 1- (-1)^{i}) {\rm Li}_i(-1)$$ with $2rn+2 \leq k\leq \kappa n$ and $0\leq p \leq h$. To sum up, for a given $n$ we have (small) linear forms, indexed by $k$ and $p$, in $b+h+1$ numbers.

Usually, the conclusion of a zero estimate in this setting would be that there exist $b+h+1$ linearly independent linear forms among them. However this is *false* in general in our setting (see Remark 1 below): there may be non-trivial linear relations between the coefficients $\ell_{p,k,i}^{(n)}$, $0\leq i \leq b+h$, valid for any $k$ and any $p$. The crucial point is that such a relation cannot involve $\ell_{p,k,0}^{(n)}$, as the following result shows. This is sufficient to apply the refinement of Siegel's linear independence criterion proved in §2.2.

**Proposition 3**. *Assume that $(h+1)(\kappa-2r)+\omega> a$, and that $n$ is sufficiently large. Let $x_0, \ldots, x_{b+h}\in\overline{\mathbb{Q}}$ be such that $$\sum_{i=0}^{b+h}  \ell_{p,k,i}^{(n)}x_i =0 \mbox{ for any } k \in \{2rn+2,\ldots,\kappa n\}\mbox{ and any } p \in \{0,\ldots,h\}.$$ Then $x_0=0$.*

**Remark 1**. *Since our linear forms are constructed using Siegel's lemma, it seems extremely difficult to exclude the case where, for some $\lambda\in\mathbb{C}$, we would have $$\label{eqdrame}
\sum_{i=1}^b  Q^{[0]}_i(z) \frac{  (\lambda-\log z)^{i-1}}{(i-1)!} = O((z+1)^{\kappa n})$$ as $z\to -1$. Indeed, if $\lambda-\log (-1)\in\mathbb{Z}$, where we fix a determination of $\log z$ around $z=-1$, this amounts to $\kappa n$ linear equations in the coefficients $c_{i,j}$; recall that these $a(n+1)$ coefficients have been constructed in §3.5 by solving $\omega n -1$ linear equations, and $\omega n -1 + \kappa n$ is still much smaller that $a(n+1)$ with the parameters we shall choose in §4.6.*

*In case Eq. (eqdrame) holds, we deduce using Eq. (eqdefqp) that for any $p\in\{0,\ldots,h\}$, $$\begin{aligned}
\sum_{i=p+1}^{p+b}  Q^{[p]}_i(z) \frac{  (\lambda-\log z)^{i-1}}{(i-1)!}
&=& \sum_{i=p+1}^{p+b}  Q^{[0]}_{i-p}(z) (-1)^p (i-p)_p \frac{  (\lambda-\log z)^{i-1}}{(i-p)_p(i-p-1)!}    \label{eqfctdrame}  \\
&=& (-1)^p  (\lambda-\log z)^p \sum_{j=1}^b  Q^{[0]}_j(z) \frac{  (\lambda-\log z)^{j-1}}{(j-1)!}  \nonumber  \\
&=& O((z+1)^{\kappa n})  \mbox{ as $z \to -1$.}  \nonumber
\end{aligned}$$ Recall that the $Q^{[p]}_{k,i}(z)$ were defined in Eq. (eqdefqpk) to compute derivatives of linear forms in the functions 1 and ${\rm Li}_{i}(1/z )- (-1)^i {\rm Li}_{i}( z )$, $1 \leq i \leq b+h$. Now the functions $\frac{  (\lambda-\log z)^{i-1}}{(i-1)!}$ satisfy the same rules of differentiation so that $\sum_{i=p+1}^{p+b}  Q^{[p]}_{k,i}(z)  \frac{  (\lambda-\log z)^{i-1}}{(i-1)!}$ is the $(k-1)$-th derivative of the function (eqfctdrame): it vanishes at $z=-1$ for any $k \in \{2rn+2,\ldots,\kappa n\}$ and any $p \in \{0,\ldots,h\}$. Using Eq. (eqdeflikn) we obtain a non-trivial linear relation, valid for any $k$ and any $p$, between the coefficients $\ell_{p,k,i}^{(n)}$ of our linear forms: under the assumptions of Proposition 3, it would be false to claim that $x_0=\ldots=x_{b+h}=0$.*

**Remark 2**. *Let us comment on the assumption $(h+1)(\kappa-2r)+\omega> a$. To explain how necessary it is, we claim that if $(h+1)(\kappa-2r)+\omega< a$ then our approach cannot even exclude the case where $(1-(-1)^i) {\rm Li}_{i}(-1) \in\mathbb{Q}$ for any $1 \leq i \leq a+h$. The point is that the coefficients $c_{i,j}$ are provided by Siegel's lemma: they are not explicit, and the only property we can reasonably use in a multiplicity estimate is that $F_n(t)=O(t^{-\omega n})$ as $|t|\to \infty$ (see Theorem 4). This amounts to $\omega n +O(1)$ linear equations in the unknowns $c_{i,j}$, where $O(1)$ denotes a term that is bounded uniformly with respect to $n$. Assuming that $(1-(-1)^i) {\rm Li}_{i}(-1) \in\mathbb{Q}$ for any $1 \leq i \leq a+h$, we claim that all linear forms (eqformeslinlemz) may vanish, for any $2rn+2 \leq k\leq \kappa n$ and any $0\leq p \leq h$. Indeed this would mean that the integers $c_{i,j}$ are solution of a linear system of $(h+1)(\kappa-2r)n+\omega n +O(1)$ linear equations with rational coefficients (see Eqns. (eqdeflikn), (eqdefqp) and (eq44bis)). If $(h+1)(\kappa-2r)+\omega< a$ and $n$ is sufficiently large, this system has fewer equations that the number of unknowns $c_{i,j}$ (namely, $a(n+1)$): there is a family of integers $c_{i,j}$, not all zero, that satisfy these equations. We see no reasonable way to prove that Theorem 4 does not provide this family; and if it does, all linear forms we are interested in vanish. Therefore we cannot hope to reach any contradiction if $(h+1)(\kappa-2r)+\omega< a$.*

In this section we prove Proposition 3. To get ready for §4.7 (where the proof of Theorem 1 is adapted to prove Theorem 2), we consider any $z_0\in\overline{\mathbb{Q}}\setminus \{0,1\}$, not only the special case $z_0=-1$ used to prove Theorem 1. In this general setting, the coefficients $\ell_{p,k,i}^{(n)}$ are defined by Eq. (eqdefl43).

Let $x_0, \ldots, x_{b+h}\in\overline{\mathbb{Q}}$ be as in Proposition 3. By contradiction we assume $x_0\neq 0$, and even $x_0=1$ (dividing all $x_i$ by $x_0$ if necessary). Using Eq. (eqdefl43) we obtain $$\label{eqannulQx}
\sum_{i=0}^{b+h} Q^{[p]}_{k,i}(z_0) x_i =0 \mbox{ for any } k \in \{2rn+2,\ldots,\kappa n\}\mbox{ and any } p \in \{0,\ldots,h\}.$$ Throughout the proof of Proposition 3 we fix a small open disk centered at $z_0$, contained in $\mathbb{C}\setminus\{0,1\}$; all functions of $z$ we consider will be holomorphic on this disk.

We denote by $Y'=A_0 Y$ with $A_0\in M_{b+h+1}(\mathbb{Q}(z))$ the differential system satisfied by the vector $Y(z)= \ ^t (y_0(z),\ldots,y_{b+h}(z))$ given by $y_0(z)=1$ and $y_i(z)= {\rm Li}_{i}(1/z )- (-1)^i {\rm Li}_{i}( z )$ for $1 \leq i \leq b+h$. Since $z_0\not\in \{0,1\}$, the point $z_0$ is not a singularity of this system: there exists a solution $\ ^t (g_0(z),\ldots,g_{b+h}(z))$ of this system consisting in functions holomorphic around $z_0$ such that $g_i(z_0)=x_i$ for any $0\leq i \leq b+h$. We have $$g'_0(z)=0, \quad g'_1(z)=\frac{z+1}{z(1-z)} g_0(z), \quad \mbox{ and  } g'_i(z)=\frac{-1}{z} g_{i-1}(z) \mbox{ for  } 2\leq i \leq b+h.$$ We consider, for any $p\in \{0,\ldots,h\}$, the function $$\label{eqdefff}
f_p(z) = T_p(z) + \sum_{i=0}^{b+h} Q^{[p]}_{i}(z ) g_i(z)$$ where $T_p(z)\in\overline{\mathbb{Q}}[z]_{\leq 2rn }$ is chosen so that $f_p(z) = O((z-z_0)^{2rn+1})$ as $z\to z_0$ (namely, $- T_p(z)$ is the Taylor approximation polynomial of degree at most $2rn$ of $\sum_{i=0}^{b+h} Q^{[p]}_{i}(z ) g_i(z)$ around $z_0$).

Vanishing of $f_p(z)$ with order at least $\kappa n$ at $z_0$.

We claim that for any $p\in\{0,\ldots,h\}$ we have $$\label{eqannulff}
f_p(z) = O((z-z_0)^{ \kappa n})\mbox{ as } z\to z_0.$$ Indeed the definition of $Q^{[p]}_{k,i}(z)$ in Eq. (eqdefqpk), intended to compute derivatives of linear forms in the functions 1 and ${\rm Li}_{i}(1/z )- (-1)^i {\rm Li}_{i}( z )$, $1 \leq i \leq b+h$ (see Eq. (eqdevsnp)), can also be used for linear forms in $g_0(z)$, ..., $g_{b+h}(z)$ because they satisfy the same rules of differentiation (i.e., $\ ^t (g_0(z),\ldots,g_{b+h}(z))$ is a solution of $Y'=A_0 Y$). Therefore we have $$f_p ^{(k-1)}(z) = T_p ^{(k-1)}(z)+ \sum_{i=0}^{b+h} Q^{[p]}_{k,i}(z ) g_i(z) \mbox{ for any } k \geq 1.$$ For any $k\in \{2rn+2,\ldots,\kappa n\}$, Eq. (eqannulQx) yields $f_p ^{(k-1)}(z_0)=0$ since $g_i(z_0)=x_i$ and $\deg T_p\leq 2rn$. This concludes the proof of Eq. (eqannulff).

Defining new polynomials and functions.

The strategy of the proof of Proposition 3 is to apply Shidlovsky's lemma. The problem for now is that the functions $f_p$ are not suitable for this: the polynomials $Q^{[p]}_{i}(z )$ in Eq. (eqdefff) should be independent from $p$. Their dependence in $p$ is rather weak (see Eq. (eqdefqp)), and we shall overcome this difficulty now (see Eqns. (eqcclhh) and (eqsysdiff)).

We consider the functions $\varrho_q(z)$ defined by: $$\label{eqdefhh}
\varrho_q(z) = \sum_{p=0}^q {q \choose p }(-\log z)^{q-p} f_p(z) \mbox{ for } q \in\{0,\ldots,h\};$$ here and throughout §4.5, $\log z$ can be seen formally. We define also $y_{0,q},\ldots, y_{b+h,q}$ for $q\in\{0,\ldots,h\}$ by: $$\label{eqdefyq}
\left\{
\begin{array}{rcl}
y_{i,q}(z) &=&
0 \mbox{ for } 0\leq i \leq h-q-1 \\ \\
y_{i,q}(z) &=&
\frac{q!}{(i+q-h)!} (-\log z)^{i+q-h} \mbox{ for } h-q \leq i \leq h \\ \\
y_{i,q}(z) &=&
 \sum_{p=0}^q {q \choose p }(-\log z)^{q-p} (-1)^p (i-h)_p g_{i-h+p}(z) \mbox{ for } h+1 \leq i \leq b+h
 \end{array}
 \right.$$ and the following polynomials $S_0,\ldots,S_{b+h}\in\overline{\mathbb{Q}}[z]_{\leq 2rn}$: $$\label{eqdefSS}
\left\{
\begin{array}{rcl}
S_i(z) &=&
\frac{1}{(h-i)!} T_{h-i}(z) \mbox{ for } 0\leq i \leq h \\ \\
S_i(z) &=&
z^{rn} P_{i-h} (z) \mbox{ for } h+1 \leq i \leq b+h.
 \end{array}
 \right.$$ Then we have for any $q\in\{0,\ldots,h\}$:

$$\begin{aligned}
\varrho_q(z)
&=& \sum_{p=0}^q {q \choose p }(-\log z)^{q-p} \Big( T_p(z) +\sum_{i=p+1}^{p+b} Q^{[p]}_i(z)g_i(z)\Big) \\
&&\quad \mbox{using Eqns.~\eqref{eqdefff} and~\eqref{eqdefhh}, since $Q^{[p]}_i(z)=0$ if $i\leq p$ or $i\geq b+p+1$} \\
&=& \sum_{p=0}^q {q \choose p }(-\log z)^{q-p} T_p(z) + \sum_{p=0}^q {q \choose p }(-\log z)^{q-p} \sum_{i=1}^b z^{rn} P_i(z)
 (-1)^p (i)_p g_{i+p}(z) \\
 &&\quad \mbox{using Eq.~\eqref{eqdefqp}} \\
&=& \sum_{i=h-q}^h \frac{1}{(h-i)!} T_{h-i}(z) \frac{q!}{(i+q-h)!} (-\log z)^{i+q-h} \\
 &&\quad \quad + \sum_{i=h+1}^{b+h} z^{rn} P_{i-h}(z) \sum_{p=0}^q {q \choose p }(-\log z)^{q-p} (-1)^p (i-h)_p g_{i-h+p}(z)

\end{aligned}$$ so that $$\label{eqcclhh}
\varrho_q(z) = \sum_{i=0}^{b+h} S_i(z) y_{i,q}(z)$$ by definition of $S_i(z)$ and $y_{i,q}(z)$. The point in writing $\varrho_q(z)$ in this way is that the polynomials $S_i(z)$ are independent from $p$ (or $q$).

A differential system independent from $p$ (or $q$).

The construction in Step 2 has an important feature: the vectors $Y_q =  \ ^t ( y_{0,q},\ldots, y_{b+h,q})$ are solutions of the same differential system, independent from $q$. This is what we shall prove now.

In precise terms, we claim that for any $q\in\{0,\ldots,h\}$ we have: $$\label{eqsysdiff}
\left\{
\begin{array}{rcl}
y_{i,q}'(z) &=&
- \frac1z y_{i-1,q}(z) \mbox{ for } 1 \leq i \leq b+h\mbox{ such that } i \neq h+1 \\
y_{h+1,q}'(z) &=&
\frac{z+1}{z(1-z)} y_{h,q} (z) \\
y_{0,q}'(z) &=&
0.
 \end{array}
 \right.$$ We shall check this property now by considering successively various ranges for $i$. If $i=0$, we have $y_{0,q}(z) =0$ if $q\leq h-1$ and $y_{0,h}(z) =h!$. If $1 \leq i \leq h-q-1$ we have $y_{i,q}(z) = y_{i-1,q}(z) = 0$. If $i=h-q$ then $y_{i,q}(z) =q!$ and $y_{i-1,q}(z) = 0$. In the case where $h-q+1\leq i\leq h$, the derivative of $y_{i,q}(z) = \frac{q!}{(i+q-h)!} (-\log z)^{i+q-h}$ is equal to $- \frac1z \frac{q!}{(i+q-h-1)!} (-\log z)^{i+q-h-1} =
- \frac1z y_{i-1,q} (z)$. When $i=h+1$ the derivative of $y_{i,q}(z)$ can be computed as follows: $$\begin{aligned}
y_{h+1,q}'(z)
&=&
\sum_{p=0}^q {q \choose p }(-1)^p p! \Big( - \frac1z (q-p) (-\log z)^{q-p-1} g_{p+1}(z) + (-\log z)^{q-p} g_{p+1}'(z) \Big)\\
&=&
- \frac1z \Big( \sum_{p=0}^{q-1} \frac{q!}{(q-p-1)!} (-1)^p (-\log z)^{q-p-1} g_{p+1}(z) \\
&&
\quad
+ \sum_{p=1}^q \frac{q!}{(q-p)!} (-1)^p (-\log z)^{q-p} g_{p}(z) \Big)+ (-\log z)^{q} \cdot \frac{z+1}{z(1-z)} g_0(z) \\
&&
\quad \quad \mbox{since $g_{p+1}'(z) = - \frac1z g_{p}(z) $ for $p\geq 1$, and $g_{1}'(z) = \frac{z+1}{z(1-z)} g_0(z) $}\\
&=&  \frac{z+1}{z(1-z)} y_{h,q}(z)

\end{aligned}$$ since the two sums inside the bracket are opposite of each other, and $g_0$ is the constant function equal to $x_0=1$. At last, for $h+2\leq i \leq b+h$ we have a similar computation: $$\begin{aligned}
y_{i,q}'(z)
&=&
- \frac1z \Big( \sum_{p=0}^{q-1} \frac{q!}{(q-p-1)!} (-1)^p \frac{(i-h)_p}{p!} (-\log z)^{q-p-1} g_{i-h+p}(z) \\
 &&\quad \quad + \sum_{p=0}^q \frac{q!}{(q-p)!} (-1)^p \frac{(i-h)_p}{p!} (-\log z)^{q-p} g_{i-h+p-1}(z) \Big) \\
&=&
- \frac1z \sum_{p=0}^{q} \frac{q!}{(q-p)!} (-1)^p (-\log z)^{q-p} g_{i-h+p-1}(z) \Big( - \frac{(i-h)_{p-1}}{(p-1)!} + \frac{(i-h)_p}{p!} \Big)

\end{aligned}$$ where $\frac{(i-h)_{p-1}}{(p-1)!}$ should be understood as 0 for $p=0$. Now $- \frac{(i-h)_{p-1}}{(p-1)!} + \frac{(i-h)_p}{p!} = \frac{(i-h-1)_{p}}{p!}$ for any $p\geq 0$, so that $y_{i,q}'(z) = - \frac1z y_{i-1,q} (z)$. This concludes the proof of the claim.

Linear independence of the functions $\varrho_0$, ..., $\varrho_h$.

Recall that $\varrho_q$ has been defined in Step 1 by Eq. (eqdefhh), for $q\in\{0,\ldots,h\}$. Let us prove that these functions are linearly independent over $\mathbb{C}$. Let $\lambda_0$, ..., $\lambda_h\in\mathbb{C}$ be such that $\sum_{q=0}^h \lambda_q \varrho_q(z)=0$. Then Eq. (eqcclhh) yields $$\label{equab}
 \sum_{i=0}^{b+h} S_i(z) \sum_{q=0}^h \lambda_q y_{i,q}(z)=0.$$ Now let $y_i(z)=\sum_{q=0}^h \lambda_q y_{i,q}(z)$ for $0\leq i \leq b+h$. Then Eqns. (eqsysdiff) yield $y_0'(z)=0$, $y_{h+1}'(z)= \frac{z+1}{z(1-z)}y_h(z)$, and $y_i'(z)=-\frac1z y_{i-1}(z)$ for any $i \in\{1,\ldots,b+h\}\setminus\{h+1\}$.

Assume that $\lambda_0$, ..., $\lambda_h$ are not all zero. Let $q_0$ be the maximal index $q\in\{0,\ldots,h\}$ such that $\lambda_q\neq0$. Then Eqns. (eqdefyq) yield $y_{h-q_0}(z)= \sum_{q=0}^{q_0} \lambda_q y_{h-q_0,q}(z) = \lambda_{q_0} q_0!\neq 0$ and $y_i(z)=0$ for $0\leq i \leq h-q_0-1$. We write $i_0 = h-q_0$, so that $y_{i_0}(z)= \lambda_{q_0} q_0!\neq 0$ and $y_i(z)=0$ for $i<i_0$.

We shall prove by decreasing induction on $\alpha\in\{i_0,\ldots,b+h\}$ that there exist polynomials $U_{\alpha,i_0}$, ..., $U_{\alpha,\alpha}$ such that $$\label{eqrecdes}
U_{\alpha,\alpha} \mbox{ is not the zero polynomial and } \sum_{i=i_0}^{\alpha} U_{\alpha,i}(z) y_{i}(z)=0 \mbox{ for any } z\in D,$$ where $D$ is the open disk we have chosen around $z_0$. This is true for $\alpha=b+h$ by definition of $i_0$, upon letting $U_{b+h,i}(z)=S_i(z)$: recall that $S_{b+h}(z)=z^{rn}P_b(z)$ is not the zero polynomial (by definition of $b$ at the beginning of §4.5), and that (equab) holds. Assume that (eqrecdes) holds for some $\alpha\in \{i_0+1,\ldots,b+h\}$ and denote by $d$ the degree of $U_{\alpha,\alpha}$. Then the $(d+1)$-th derivative of the zero function can be written as $$z^{d+1} (1-z)^{d+1} \Big( \sum_{i=i_0}^{\alpha} U_{\alpha,i}(z) y_{i}(z) \Big)^{(d+1)} = \sum_{i=i_0}^{\alpha-1} U_{\alpha-1,i}(z) y_{i}(z)$$ for some polynomials $U_{\alpha-1,i}$, using the expression of $y_i'(z)$ in terms of $y_{i-1}(z)$ deduced above from Eqns. (eqsysdiff); notice that $y_\alpha(z)$ does not appear anymore since $U_{\alpha,\alpha} ^{(d+1)}=0$. To prove that $U_{\alpha-1,\alpha-1}\neq 0$, we first assume that $\alpha\neq h+1$. By induction on $t\geq 0$ we have $$\Big( U_{\alpha,\alpha}(z) y_\alpha(z)\Big)^{(t)} = U_{\alpha,\alpha}^{(t)}(z) y_\alpha(z) + \sum_{j=0}^{t-1} \Big( \frac{-1}{z} U_{\alpha,\alpha}^{(j)}(z) \Big) ^{(t-1-j)} y_{\alpha-1}(z) + V_t(z)$$ where $z^{t} (1-z)^{t} V_t(z)$ is a $\overline{\mathbb{Q}}[z]$-linear combination of $y_{i_0}(z)$, ..., $y_{\alpha-2}(z)$. Therefore we have $$U_{\alpha-1,\alpha-1}(z) = z^{d+1} (1-z)^{d+1} \Big(U_{\alpha,\alpha-1}^{(d+1)}(z) + \sum_{j=0}^{d} \Big( \frac{-1}{z} U_{\alpha,\alpha}^{(j)}(z) \Big) ^{(d-j)} \Big).$$ This is not the zero polynomial because in the expansion of $z^{-(d+1)} (1-z)^{-(d+1)} U_{\alpha-1,\alpha-1}(z)$ as a linear combination of $z^n$, $n\in\mathbb{Z}$, the coefficient of $z^{-1}$ (namely, the residue) is $- U_{\alpha,\alpha}^{(d)}\neq 0$. In the case where $\alpha= h+1$ we have $y_\alpha'(z)=\frac{z+1}{z(1-z)}y_{\alpha-1}(z)$ so that the same formulas hold with $\frac{z+1}{z(1-z)}$ instead of $\frac{-1}{z}$; we conclude in the same way, by writing $z^{-(d+1)} (1-z)^{-(d+1)} U_{\alpha-1,\alpha-1}(z) = \sum_{n=n_0}^{+\infty} a_n z^n$ for some $n_0\leq -1$, with $a_{-1}\neq 0$. In both cases this concludes the inductive proof of (eqrecdes) for all $\alpha\in \{i_0,\ldots,b+h\}$.

Now for $\alpha=i_0$ we obtain $U_{i_0,i_0}(z) y_{i_0}(z)=0$ for any $z\in D$, where $U_{i_0,i_0}$ is not the zero polynomial and $y_{i_0}(z)=\lambda_{q_0} q_0!\neq 0$. This contradiction concludes the proof of the claim.

Defining linearly independent functions $\widetilde \varrho_1$, ..., $\widetilde \varrho_b$.

Consider, for $\beta\in \{1,\ldots,b\}$, the functions $\widetilde y_{i,\beta}$ defined by $$\label{eqdefyyti}
\left\{\begin{array}{l}
\widetilde y_{i,\beta}(z) = 0 \mbox{ for } 0\leq i \leq h+\beta-1\\
\widetilde y_{i,\beta}(z) = \frac{(-\log z)^{ i-h-\beta }}{ ( i-h-\beta )!} \mbox{ for } h+\beta \leq i \leq b+h
\end{array}\right.$$ They satisfy the differential system (eqsysdiff); we define $$\label{eqdefhhti}
\widetilde \varrho_\beta(z) = \sum_{i=0}^{b+h} S_i(z) \widetilde y_{i,\beta}(z) = \sum_{i=h+\beta}^{b+h} z^{rn} P_{i-h}(z) \frac{(-\log z)^{ i-h-\beta }}{ ( i-h-\beta )!}= \sum_{i= \beta}^{b} z^{rn} P_{i }(z) \frac{(-\log z)^{ i -\beta }}{ ( i -\beta )!}.$$ Let us prove that the functions $\widetilde \varrho_1$, ..., $\widetilde \varrho_b$ are linearly independent over $\mathbb{C}$. Let $\lambda_1$, ..., $\lambda_b$ be complex numbers, not all zero, such that $\sum_{\beta=1}^b \lambda_\beta \widetilde \varrho_\beta(z) =0$. Denote by $\beta_0$ the least index $\beta$ such that $\lambda_\beta\neq 0$. Then we have the following $\mathbb{C}[z]$-linear relation between powers of $\log z$: $$\sum_{\beta=\beta_0}^b \sum_{i=\beta}^b \lambda_\beta z^{rn} P_{i }(z) \frac{(-\log z)^{ i -\beta }}{ ( i -\beta )!} =0.$$ Since $\log z$ is transcendental over $\mathbb{C}[z]$, the coefficient of $( \log z)^{ b -\beta_0 }$ has to be zero: $\lambda_{\beta_0}P_b(z)=0$. Since $\lambda_{\beta_0}\neq 0$ and $P_b$ is not the zero polynomial (by definition of $b$, see the beginning of §4.5), this is a contradiction. This concludes the proof that $\widetilde \varrho_1$, ..., $\widetilde \varrho_b$ are linearly independent over $\mathbb{C}$.

Application of Shidlovsky's lemma.

Let us apply the general version of Shidlovsky's lemma stated as Theorem 3 in §2.3. We let $N= b+h+1$ and consider the matrix $A\in M_N(\mathbb{Q}(z))$ that corresponds to the differential system (eqsysdiff). The polynomials $S_0,\ldots,S_{b+h}$ are defined by Eq. (eqdefSS); we have $\deg S_i \leq m$ with $m=2rn$ (recall that $r\geq 1$, $\deg T_p\leq 2rn$ and $\deg P_i\leq n$). We let $\Sigma = \{0,1,\infty,z_0\}$; recall that $z_0\not\in\{0,1\}$. Let us start with the vanishing conditions at $z_0$.

Eq. (eqcclhh) reads $R(Y_q)(z)=\varrho_q(z)$ for any $q\in\{0,\ldots,h\}$, where $Y_q =  \ ^t (y_{0,q}(z),\ldots,y_{b+h,q}(z))$ is a solution of $Y'=AY$. The functions $y_{i,q}(z)$ are analytic at $z_0$ (since $z_0\not\in\{0,1\}$), and the remainders $R(Y_q)(z)=\varrho_q(z)$, for $q\in J_{z_0}=\{0,\ldots,h\}$, are linearly independent over $\mathbb{C}$ (as proved in Step 4). Moreover we have proved in Step 1 that $f_p(z) = O((z-z_0)^{\kappa n})$ as $z\to z_0$, so that $R(Y_q)(z)= O((z-z_0)^{\kappa n})$ for any $q$ using Eq. (eqdefhh). Therefore we have $$\label{eqshidzz}
 \sum_{j\in J_{z_0} } {\rm ord}_{z_0}(R(Y_j)) \geq (h+1) \kappa n.$$

Let us consider now the points 0 and $\infty$. We let $J_0=J_\infty=\{1,\ldots,b\}$, and for $\beta$ in this set we let $\widetilde Y_\beta =  \ ^t (\widetilde y_{0,\beta}(z),\ldots,\widetilde y_{b+h,\beta}(z))$ where the functions $\widetilde y_{i,\beta}(z)$ have been defined in Step 5. Then $R(\widetilde Y_\beta)(z)= \widetilde \varrho_\beta(z)$ is given by Eq. (eqdefhhti); as proved in Step 5, the functions $R(\widetilde Y_1)$, ..., $R(\widetilde Y_b)$ are $\mathbb{C}$-linearly independent. Recall from Eq. (eqdefSS) that $S_i(z)=O(z^{rn})$ as $z\to 0$, and $\deg S_i\leq (r+1)n$, for any $i\in\{h+1,\ldots,b+h\}$. Therefore Eqns. (eqdefyyti) and (eqdefhhti) yield $\widetilde \varrho_\beta(z) =O(z^{rn}(\log z)^{b-1})$ as $z\to 0$, and $\widetilde \varrho_\beta(z) =O((1/z)^{-(r+1)n}(\log (1/z))^{b-1})$ as $z\to \infty$, so that $$\label{eqshidzi}
\sum_{\sigma\in\{0,\infty\}} \sum_{\beta\in J_{\sigma} } {\rm ord}_{\sigma}(R(\widetilde Y_\beta)) \geq brn - b(r+1)n = -bn;$$ recall that logarithmic factors have no influence on the order of vanishing, e.g. ${\rm ord}_0(z^e(\log z)^i)= \mbox{Re}(e)$ for $e\in\mathbb{C}$ and $i\in\mathbb{N}$.

At last, we let $J_1=\{1\}$ and notice that $R(\widetilde Y_1)(z)= \widetilde \varrho_1(z)$ defined by Eq. (eqdefhhti) is equal to $z^{rn} R_n(z)$, where $R_n(z)$ is defined in Eq. (eqdefrn) (recall that $P_{b+1}(z)=\ldots=P_a(z)=0$). The proof of Theorem 4 (namely $(iii)$ in §3.5) shows that $R_n(z) = O((z-1)^{\omega n-1})$ as $z\to 1$; therefore we have $$\label{eqshidun}
 {\rm ord}_{1}(R(Y_1)) \geq \omega n-1$$ where $R(Y_1)$ is not the zero function (see Step 5).

Combining Eqns. (eqshidzz), (eqshidzi) and (eqshidun), Theorem 3 yields $$\Big( (h+1)\kappa-b+\omega\Big) n - 1 \leq (2rn+1) (\mu-b) + c_1$$ where $c_1$ depends only on $a$, $h$, $z_0$ (but can be made independent of $b$ and $n$ since $b\leq a$), and $\mu$ is the minimal order of a non-zero differential operator $L$ such that $L(R(Y))= 0$ for any solution $Y$ of the differential system $Y'=AY$. Now for any such $Y$, the row matrix $\ ^t (R(Y)\, R(Y)' \ldots R(Y)^{(N)})$ can be written as $\ ^t Y M$ where $M\in M_{N,N+1}(\overline{\mathbb{Q}}(z))$ is independent of $Y$: the first column of $M$ is given by the $S_i$, and the following ones by rational functions $S_{k,i}$ (see [@SFcaract §3.2, Step 1]). There is a non-trivial $\overline{\mathbb{Q}}(z)$-linear relation between the columns of $M$; it provides a differential operator $L$ of order at most $N$ such that $L(R(Y))= 0$ for any solution $Y$, so that $\mu\leq b+h+1$. Since $n$ is assumed to be sufficiently large (in terms of $b$, $h$, $\omega$, $r$, $z_0$ and $\kappa$, and also therefore in terms of $c_1$), we obtain $(h+1)(\kappa-2r)+\omega\leq b$. Since $b \leq a$, $\omega>0$ and $(h+1)(\kappa-2r)+\omega> a$, this is a contradiction.

## End of the proof

Let $a$ be a positive integer. In Theorem 1 the numerical constant $0.21$ can be replaced (as the proof will show) by a slightly larger real number. Therefore in the proof we may assume that $a$ is a multiple of 25. Then we choose $r =3.9$, $\kappa= 10.58$, $\omega= 12$, $\Omega= \lfloor r \sqrt{a \log a}\rfloor$, and $h =0.36\ a\in\mathbb{N}$, so that $(h+1)(\kappa-2r)+\omega> a$ and $\Omega> \omega$. Here and below all numerical constants are rounded with precision 0.01.

We consider $z_0 = -1$ and choose $q=1$, so that $qz_0 \in \mathbb{Z}$. We denote by $\mathcal{N}_a$ the set of all sufficiently large multiples of 50: for any $n\in\mathcal{N}_a$ we have $rn , \kappa n , \omega n,\Omega n\in \mathbb{N}$. For any $n\in\mathcal{N}_a$ we consider the integers $c_{i,j}$ provided by Theorem 4, and define $b$ as in the beginning of §4.5, namely $$b = \max\{ i\in\{1,\ldots,a\}, \, \exists j \in\{0,\ldots,n\}, \, c_{i,j}\neq 0\}.$$ This integer $b$ depends on $n$, but it can take only $a$ values. Therefore there exists an infinite subset $\mathcal{N}_a'\subset\mathcal{N}_a$ such that all $n\in\mathcal{N}_a'$ correspond to the same $b$. From now on, we consider only integers $n\in\mathcal{N}_a'$.

Let $k\in\{2rn+2,\ldots,\kappa n\}$ and $p \in\{ 0 ,\ldots,h\}$. Lemma 5 yields $\ell_{p,k,i}^{(n)}\in \mathbb{Z}$ for any $i$, and $$|  \ell_{p,k,i}^{(n)}|  \leq \beta^{n(1+o(1))} \mbox{ with } \beta =
 \chi \Big( 8 e^3(2a+1)\Big)^\kappa\cdot 2^{\kappa+r+1}$$ where $\chi$ is defined by Eq. (eqdefchi) in Theorem 4, namely $$\chi = \exp\Big(\frac{ \omega\log 2 + 3\omega^2 + \omega^2 \log (a+1) +\frac12 \Omega^2 \log r }{a-\omega}\Big).$$ Now we have (using Eq. (eqFL) and the definition of $b$, see the beginning of §4.5) $$\ell_{p,k,0}^{(n)}+ \sum_{i=1}^{b+h} \ell_{p,k,i}^{(n)}\Big( 1 - (-1)^i\Big) {\rm Li}_i(-1) = (-2)^{k-1} \frac{\delta_{k}}{(k-1)!}
S_{n,p}^{(k-1)}(-1).$$ Since $k \leq\kappa n$, we may apply Lemma 6 and deduce that $$\Big| \ell_{p,k,0}^{(n)}+ \sum_{i=1}^{b+h} \ell_{p,k,i}^{(n)}\Big( 1 - (-1)^i\Big) {\rm Li}_i(-1) \Big| \leq \alpha^{n(1+o(1))} \mbox{ with }
\alpha =
2^\kappa\alpha_0 = \chi r^{-\Omega}( 2e^4(2a+1))^{\kappa} .$$ Using Proposition 3, the refined version of Siegel's linear independence criterion (stated and proved in §2.2) applies to these linear forms for $n\in \mathcal{N}_a'$, with coefficients $\ell_{p,k,i}^{(n)}$, $\theta_0=1$, $Q_n = \beta^n$ and $\tau = -\frac{\log \alpha}{\log\beta}$ (so that $Q_n^{-\tau} = \alpha^n$). We obtain $$\label{eqaveclogd}
\dim_\mathbb{Q}{\rm Span}_\mathbb{Q}( \{1, \log 2\}\cup\{\zeta(i), \, 3\leq i \leq a+h, \, i \mbox{ odd}\}) \geq 1 - \frac{\log \alpha}{\log \beta } .$$ Now recall that $a>0$ is a multiple of $25$, $r =3.9$, $\kappa= 10.58$, $\omega= 12$, $\Omega=\lfloor r \sqrt{a \log a}\rfloor$, and $h =0.36\ a$. As $a\to\infty$ the formulas above yield $$\log\chi\sim \frac{ \Omega^2 \log r}{2a} \sim \frac{r^2\log r}2 \log a ,$$ $$\log\beta\sim \log \chi + \kappa\log a \sim \Big( \frac{r^2\log r}2 +\kappa\Big) \log a ,$$ $$\log\alpha\sim - \Omega\log r \sim - r\log r \cdot \sqrt{a \log a}$$ so that $$\begin{aligned}
- \frac{\log \alpha}{\log \beta}
&\sim& \frac{ 2 r \log r}{r^2 \log r + 2 \kappa} \sqrt{\frac{a}{\log a}} \\
&\sim& \frac{ 2 r \log r}{r^2 \log r + 2 \kappa}\cdot \frac1{\sqrt{1+h/a}} \cdot \sqrt{\frac{a+h}{\log (a+h)}}.
\end{aligned}$$ Now recall that $r=3.9$, $\kappa=10.58$ and $h=0.36 a$, so that $$\frac{ 2 r \log r}{r^2 \log r + 2 \kappa}\cdot \frac1{\sqrt{1+h/a}} = 0.2174\ldots > 0.21.$$ If $a$ is large enough we obtain $$- \frac{\log \alpha}{\log \beta} \geq 0.21 \cdot \sqrt{\frac{a+h}{\log (a+h)}}.$$ We take $s = a+h$ and apply Eq. (eqaveclogd). The additional 1 in the right hand side accounts for the number $\log 2$ in the left hand side, that we want to get rid of. This concludes the proof of Theorem 1.

**Remark 3**. *It follows from the computations above that, as $s = a+h$ tends to $\infty$, $$\log\alpha\sim - 4.55 \sqrt{s \log s} \quad \mbox{ and } \quad \log\beta\sim 20.93 \log s.$$*

**Remark 4**. *The proof allows one to compute effectively an integer $s_0$ such that the conclusion of Theorem 1 holds for any $s\geq s_0$.*

## The case of polylogarithms: proof of Theorem 2

To prove Theorem 2, we follow the proof of Theorem 1 except that we consider $S_{n,p}^{[\infty]}(z)$ (defined in Eq. (eqdefsninf)) instead of $S_{n,p}(z)$. Therefore Eq. (eq33nv) becomes $$\label{eq33polylogsnv}
 S_{n,p}^{[\infty] (k-1) }= Q^{[p]}_{k,0}(z) + \sum_{i=1}^{a+h} Q^{[p]}_{k,i}(z) {\rm Li}_i(1/z) \mbox{ for any } k\geq (r+1)n+1.$$ The point here is that (with the notation of the proof of Lemma 4 in §4.2) we have $\deg V_p^{[\infty]}\leq (r+1)n-1$ and $\deg V_p^{[0]}\leq 2rn$. In the proof of Theorem 1 we had to restrict to integers $k\geq 2rn+2$ so that $( V_p^{[\infty]}- V_p^{[0]}) ^{(k-1)}=0$, whereas to prove Theorem 2 assuming $k\geq (r+1)n+1$ is enough to ensure that $V_p^{[\infty] (k-1)}=0$.

Let $z_0\in\overline{\mathbb{Q}}$ be such that $|z_0| \geq 1$ and $z_0\neq 1$; let $q\in\mathbb{N}^\ast$ be a denominator of $z_0$, i.e. such that $qz_0 \in {\mathcal O}_{\mathbb{Q}(z_0)}$ where ${\mathcal O}_{\mathbb{Q}(z_0)}$ is the ring of integers of $\mathbb{Q}(z_0)$. For any $k\geq (r+1)n+1$ we let $$\ell_{p,k,i}^{(n)}(z_0) = q^{(r+1)n+k-1} z_0^{k-1}(1-z_0)^{k-1} \frac{\delta_k}{(k-1)!} Q^{[p]}_{k,i} (z_0) \mbox{ for } 0\leq i \leq a+h$$ where $\delta_k=\delta_k (a+h,(r+1)n, 1,0)$ is given by Proposition 2 in §3.2 with $a$ replaced by $a+h$ and $n$ by $(r+1)n$; in the setting of §3.2 we take $\alpha_0= 1$ and $\alpha_1= 0$ in the recurrence relation (eqrecpkijtechnique), to fit the differential system satisfied by the functions 1 and ${\rm Li}_i(1/z)$. Then following the proof of Lemma 5 (with only one difference: for $i=0$, due to the value of $(\alpha_0,\alpha_1)$) yields $\ell_{p,k,i}^{(n)}(z_0)\in{\mathcal O}_{\mathbb{Q}(z_0)}$ and $$\mathord{
 \mathpalette\@house{\ell_{p,k,i}^{(n)}(z_0)}
 }
 \leq \beta_1^{n(1+o(1))} \mbox{ with } \beta_1 = \chi \Big( 8e^3 (2a+1) \Big)^\kappa\cdot \Big( q\max(1,
 \mathord{
 \mathpalette\@house{z_0}
 }
 ,
 \mathord{
 \mathpalette\@house{ 1-z_0}
 }
 ) \Big)^{\kappa+r+1}$$ provided $k \leq \kappa n$ and $\kappa\geq r+1$. Moreover Eq. (eq33polylogsnv) yields $$q^{(r+1)n+k-1} z_0^{k-1}(1-z_0)^{k-1} \frac{\delta_k}{(k-1)!} S_{n,p}^{[\infty] (k-1) }(z_0) = \ell_{p,k,0}^{(n)}(z_0) + \sum_{i=1}^{a+h} \ell_{p,k,i}^{(n)}(z_0) {\rm Li}_i(1/z_0)$$ for any $k\geq (r+1)n+1$. Following the proof of Lemma 6 we deduce that $$\Big| q^{(r+1)n+k-1} z_0^{k-1}(1-z_0)^{k-1} \frac{\delta_k}{(k-1)!} S_{n,p}^{[\infty] (k-1) }(z_0) \Big| \leq \alpha_1^{n(1+o(1))}$$ with $$\alpha_1 = \chi r^{-\Omega} q^{r+1} ( e^4(2a+1)q | z_0(1-z_0)| )^{\kappa} .$$ Then we adapt Proposition 3, assuming that $(h+1)(\kappa- r-1)+\omega> a$ and considering integers $k$ such that $(r+1)n+1\leq k \leq \kappa n$. This enables us to apply Proposition 1 and deduce that $$\dim_{\mathbb{Q}(z_0)} {\rm Span}_{\mathbb{Q}(z_0)} (\{1\}\cup \{ {\rm Li}_i(1/z_0), \, 1\leq i \leq a+h\}) \geq \frac1{[ \mathbb{Q}(z_0):\mathbb{Q}]} \Big( 1 - \frac{\log \alpha_1}{\log \beta_1 } \Big).$$ Our choice of parameters is the same as in §4.6, except for numerical constants. The only difference is that the assumptions $\kappa> 2 r$ and $(h+1)(\kappa-2 r)+\omega> a$ in §4.6 are weakened here to $\kappa> r+1$ and $(h+1)(\kappa- r-1)+\omega> a$. We choose $r =5.3$, $\kappa= 8.8343$, $\omega= 10$, $\Omega= \lfloor 3.3 \sqrt{a \log a}\rfloor$, and $h =0.3946\ a\in\mathbb{N}$ (assuming that $10^4$ divides $a$), so that $(h+1)(\kappa-r-1)+\omega> a$. As in §4.6 we have, as $a\to\infty$: $$\log\chi\sim 9.0807 \log a, \quad
 \log\beta_1\sim 17.915 \log a , \quad
\log\alpha_1\sim - 5.5034 \sqrt{a \log a}$$ so that $$- \frac{\log \alpha_1}{\log \beta_1} \geq 0.26 \sqrt{\frac{a+h}{\log (a+h)}}$$ provided $a$ is large enough. This concludes the proof of Theorem 2.

**Remark 5**. *If $z\not\in\mathbb{R}$ then we have $[\mathbb{K}_\infty:\mathbb{R}]=2$ in the notation of Proposition 1, so that the constant $0.26$ may be replaced with $0.52$ in Theorem 2.*

10

[Y. André] -- *$G$-functions and geometry*, Aspects of Math., no. E13, Vieweg, 1989.

[R. Apéry] -- "Irrationalité de $\zeta(2)$ et $\zeta(3)$", in *Journées Arithmétiques (Luminy, 1978)*, Astérisque, no. 61, 1979, p. 11--13.

[K. Ball & T. Rivoal] -- " Irrationalité d'une infinité de valeurs de la fonction zêta aux entiers impairs", *Invent. Math.* **146** (2001), no. 1, p. 193--207.

[D. Bertrand] -- "Le théorème de Siegel-Shidlovsky revisité", in *Number theory, Analysis and Geometry: in memory of Serge Lang* (D. Goldfeld *et al.*, éd.), Springer, 2012, p. 51--67.

[D. Bertrand & F. Beukers] -- " Équations différentielles linéaires et majorations de multiplicités", *Ann. Sci. École Norm. Sup. (4)* **18** (1985), no. 1, p. 181--192.

[D. Chudnovsky & G. Chudnovsky] -- " Rational approximations to solutions of linear differential equations", *Proceedings of the National Academy of Sciences of the United States of America* **80** (1983), p. 5158--5162.

--- , "Applications of Padé approximations to Diophantine inequalities in values of $G$-functions", in *Number theory (New York, 1983/84)*, Lecture Notes in Math., vol. 1135, Springer, 1985, p. 9--51.

[G. Chudnovsky] -- "Rational and Padé approximations to solutions of linear differential equations and the monodromy theory", in *Complex Analysis, Microlocal Calculus and Relativistic Quantum Theory (Les Houches, 1979)*, Lecture Notes in Physics, no. 126, Springer, 1979, p. 136--169.

--- , "On applications of Diophantine approximations", *Proceedings of the National Academy of Sciences of the United States of America* **81** (1984), no. 22, p. 7261--7265.

[B. Farhi] -- "An identity involving least common multiple of binomial coefficients and its application", *Amer. Math. Monthly* **116** (2009), p. 836--839.

[N. Fel'dman & Y. Nesterenko] -- *Number theory IV, transcendental numbers*, Encyclopaedia of Mathematical Sciences, no. 44, Springer, 1998, A.N. Parshin and I.R. Shafarevich, eds.

[S. Fischler] -- "Shidlovsky's multiplicity estimate and irrationality of zeta values", *J. Austral. Math. Soc.* **105** (2018), no. 2, p. 145--172.

[S. Fischler & T. Rivoal] -- "Approximants de Padé et séries hypergéométriques équilibrées", *J. Math. Pures Appl.* **82** (2003), no. 10, p. 1369--1394.

--- , "Linear independence of values of ${G}$-functions, II. Outside the disk of convergence", *Ann. Math. Québec* **45** (2021), no. 1, p. 53--93.

[S. Fischler, J. Sprang & W. Zudilin] -- " Many odd zeta values are irrational", *Compositio Mathematica* **155** (2019), no. 5, p. 938--952.

[G. Hardy & E. Wright] -- "An introduction to the theory of numbers", 4th ed., Oxford Univ. Press, 1975.

[M. Hata] -- "On the linear independence of the values of polylogarithmic functions", *J. Math. Pures Appl.* **69** (1990), no. 2, p. 133--173.

[L. Lai & P. Yu] -- "A note on the number of irrational odd zeta values", *Compositio Math.* **156** (2020), no. 8, p. 1699--1717.

[L. Lai] -- "Small improvements on the Ball-Rivoal theorem and its $p$-adic variant", preprint arXiv:2407.14236\[math.NT\], 2024.

--- , "A note on the number of irrational odd zeta values, II", preprint arXiv:2501.05321\[math.NT\], 2025.

[R. Marcovecchio] -- "Linear independence of linear forms in polylogarithms", *Annali Scuola Norm. Sup. Pisa* **V** (2006), no. 1, p. 1--11.

[T. Matala-aho] -- "On Diophantine approximations of the solutions of $q$-functional equations", *Proc. Roy. Soc. Edinburgh Sect. A* **132** (2002), p. 639--659.

[Y. Nesterenko] -- "On the linear independence of numbers", *Vestnik Moskov. Univ. Ser. I Mat. Mekh. \[Moscow Univ. Math. Bull.\]* **40** (1985), no. 1, p. 46--49 \[69--74\].

[E. Nikishin] -- "On the irrationality of the values of the functions $F(x,s)$", *Mat. Sbornik \[Math. USSR-Sb.\]* **109 [37]** (1979), no. 3, p. 410--417 \[381--388\].

[T. Rivoal] -- "La fonction zêta de Riemann prend une infinité de valeurs irrationnelles aux entiers impairs", *C. R. Acad. Sci. Paris, Ser. I* **331** (2000), no. 4, p. 267--270.

--- , "Indépendance linéaire des valeurs des polylogarithmes", *J. Théor. Nombres Bordeaux* **15** (2003), no. 2, p. 551--559.

[W. Schmidt] -- "Diophantine approximations and Diophantine equations", Lecture Notes in Math. 1467, Springer, 1991.

--- , "On heights of algebraic subspaces and Diophantine approximations", *Annals of Math.* **85** (1967), p. 430--472.

[A. B. Shidlovsky] -- *Transcendental numbers*, de Gruyter Studies in Math., no. 12, de Gruyter, Berlin, 1989.

[J. Sprang] -- "Infinitely many odd zeta values are irrational. By elementary means", preprint arXiv:1802.09410 \[math.NT\], 2018.

[W. Zudilin] -- "One of the odd zeta values from $\zeta(5)$ to $\zeta(25)$ is irrational. By elementary means", *SIGMA* **14** (2018), no. 028, 8 pages.

[^1]: Université Paris-Saclay, CNRS, Laboratoire de mathématiques d'Orsay, 91405 Orsay, France

[^2]: After this paper was written, Lai [@Lai2024] refined the constant $\frac{1 }{1+\log 2}=0.59\ldots$ in Eq. (eqBR) to $0.66\ldots$

[^3]: This constant $1.19\ldots$ has also be refined by Lai [@Lai2025] to $1.28\ldots$

[^4]: For the application we have in mind, an upper bound on $\Delta_{a,N}$ is enough. We provide its exact asymptotics for the sake of completeness.
