---
title: "Many odd zeta values are irrational"
authors:
  - "Stéphane Fischler"
  - "Johannes Sprang"
  - "Wadim Zudilin"
arxiv_id: "1803.08905v2"
arxiv_url: "https://arxiv.org/abs/1803.08905"
published: "2018-03-23"
journal_ref: "Compositio Math. 155 (2019) 938-952"
doi: "10.1112/S0010437X1900722X"
source: "papers/10-fischler-sprang-zudilin-2018-many-odd-zeta/zeta11w.tex"
conversion: pandoc-flat
---

# Many odd zeta values are irrational

**Stéphane Fischler, Johannes Sprang, Wadim Zudilin** — Compositio Math. 155 (2019) 938-952

## Abstract

Building upon ideas of the second and third authors, we prove that at least $2^{(1-\varepsilon)\frac{\log s}{\log\log s}}$ values of the Riemann zeta function at odd integers between 3 and $s$ are irrational, where $\varepsilon$ is any positive real number and $s$ is large enough in terms of $\varepsilon$. This lower bound is asymptotically larger than any power of $\log s$; it improves on the bound $\frac{1-\varepsilon}{1+\log2}\log s$ that follows from the Ball--Rivoal theorem. The proof is based on construction of several linear forms in odd zeta values with related coefficients.

---
# Introduction {#introduction .unnumbered}

When $s\geq 2$ is an even integer, the value $\zeta(s)$ of the Riemann zeta function is a non-zero rational multiple of $\pi^s$ and, therefore, a transcendental number. On the other hand, no such relation is expected to hold for $\zeta(s)$ when $s\geq 3$ is odd; a folklore conjecture states that the numbers $\pi$, $\zeta(3)$, $\zeta(5)$, $\zeta(7),\ldots$ are algebraically independent over the rationals. This conjecture is predicted by Grothendieck's period conjecture for mixed Tate motives. But both conjectures are far out of reach and we do not even know the transcendence of a single odd zeta value.

It was only in 1978 when Apéry astonished the mathematics community by his proof [@Apery] of the irrationality of $\zeta(3)$ (see [@SFBou] for a survey). The next breakthrough was taken in 2000 by Ball and Rivoal [@BR; @RivoalCRAS] who proved the following:

**Theorem 1** (Ball--Rivoal). *Let $\varepsilon> 0$. Then for any $s\geq 3$ odd and sufficiently large with respect to $\varepsilon$, we have $$\dim_\mathbb{Q}\operatorname{Span}_\mathbb{Q}( 1, \, \zeta(3), \, \zeta(5), \, \zeta(7), \, \ldots , \zeta(s)) \geq \frac{1-\varepsilon}{1+\log 2}\,\log s.$$*

Their corresponding result for small $s$ has been refined several times [@Zudilincentqc; @SFZu], but the question whether $\zeta(5)$ is irrational remains open. The proof of Theorem 1 involves the well-poised hypergeometric series $$\label{eqBR}
n!^{s-2r}\, \sum_{t=1}^\infty \frac{ \prod_{j=0}^{ (2r+1)n} (t-rn+j) }{ \prod_{j=0}^{ n} (t+j)^{s+1}},$$ which happens to be a $\mathbb{Q}$-linear combination of 1 and odd zeta values when $s$ is odd and $n$ is even, and Nesterenko's linear independence criterion [@Nesterenkocritere]. The bound $\frac{1-\varepsilon}{1+\log 2}\log s$ follows from comparison of how small the linear combination is with respect to the size of its coefficients, after multiplying by a common denominator to make them integers. To improve on this bound using the same strategy, one has to find linear combinations that are considerably smaller, with not too large coefficients, --- it comes out to be a rather difficult task. This may be viewed as an informal explanation of why the lower bound in Theorem 1 has never been improved for large values of $s$, whereas the theorem itself has been generalized to several other families of numbers.

Using (with $s=20$) the series $$n!^{s-6}\,  \sum_{k=1}^\infty \left.\Big( \frac{\mathrm{d}}{\mathrm{d}t}\Big)^2 \bigg( \Big(t+\frac{n}{2}\Big) \frac{\prod_{j=0}^{ 3n} (t-n+j)^3 }{ \prod_{j=0}^{ n} (t+j)^{s+3}}\bigg)\right|_{t=k} ,$$ which is a $\mathbb{Q}$-linear combination of 1 and odd zeta values starting from $\zeta(5)$, Rivoal has proved [@vingtetun] that among the numbers $\zeta(5)$, $\zeta(7)$, ..., $\zeta(21)$, at least one is irrational. This result has been improved by the third author [@Zudilinonze]: among the four numbers $\zeta(5)$, $\zeta(7)$, $\zeta(9)$, $\zeta(11)$, at least one is irrational; and he also showed [@Zudilincentqc] that, for any odd $\ell \geq 1$, there is an irrational number among $\zeta(\ell+2)$, $\zeta(\ell+4)$, ..., $\zeta(8\ell-1)$. Proofs of these results do not require use of linear independence criteria: if a sequence of $\mathbb{Z}$-linear combinations of real numbers from a given (fixed) collection tends to 0, and is non-zero infinitely often, then at least one of these numbers is irrational. A drawback of this approach is that it only allows one to prove that *one* number in a family is irrational.

The situation has drastically changed when the third author introduced [@Zudilintrick] a new method (see also [@KrattZ]). He casts (with $s=25$) the rational function in the form $$R(t) =  2^{6n}n!^{s-5}\, \frac{\prod_{j=0}^{6n} (t-n+\frac{j}{2})}{ \prod_{j=0}^{ n} (t+j)^{s+1}}$$ and proves that both series $$\sum_{t=1}^\infty R(t) \quad\mbox{and}\quad \sum_{t=1}^\infty R\Big(t+\frac12\Big)$$ are $\mathbb{Q}$-linear combinations of 1, $\zeta(3)$, $\zeta(5)$, ..., $\zeta(s)$ with *related* coefficients. This allows him to eliminate one odd zeta value, and to prove that *at least two* zeta values among $\zeta(3)$, $\zeta(5)$, ..., $\zeta(25)$ are irrational. In view of Apéry's Theorem, the result means that one number among $\zeta(5)$, ..., $\zeta(25)$ is irrational --- nothing really novel, but the method of proof is new and more elementary than the ones in [@vingtetun] and [@Zudilinonze] as it avoids use of the saddle point method. More importantly, the method allows to prove the irrationality of at least two zeta values in a family without having to produce very small linear forms. The same strategy has been adopted by Rivoal and the third author [@RZnote] to prove that among $\zeta(5)$, $\zeta(7)$, ..., $\zeta(69)$, at least two numbers are irrational.

The method in [@Zudilintrick] has been generalized by the second author [@Sprang], who introduces another integer parameter $D>1$ and considers the rational function $$\label{eqSprang}
R(t) = D^{6(D-1)n}n!^{s-3D-1}\,\frac{ \prod_{j=0}^{3Dn} (t-n+\frac{j}{D})}{ \prod_{j=0}^{ n} (t+j)^{s+1}}.$$ He proves that for any divisor $d$ of $D$ the series $$\sum_{j=1}^d \sum_{t=1}^\infty R\Big(t+\frac{j}{d}\Big)$$ is a $\mathbb{Q}$-linear combination of 1, $\zeta(3)$, $\zeta(5)$, ..., $\zeta(s)$. The crucial point of this construction is that each $\zeta(i)$ appears in this $\mathbb{Q}$-linear combination with a coefficient that depends on $d$ in a very simple way. This makes it possible to eliminate from the entire collection of these linear combinations as many odd zeta values as the number of divisors of $D$. Finally, taking $D$ equal to a power of 2 and $s$ sufficiently large with respect to $D$, the second author proves that at least $\frac{\log D}{\log 2}$ numbers are irrational among $\zeta(3)$, $\zeta(5)$, ..., $\zeta(s)$. This strategy represents a new proof that $\zeta(i)$ is irrational for infinitely many odd integers $i$.

Building upon the approach in [@Zudilintrick] and [@Sprang] we prove the following result.

**Theorem 2**. *Let $\varepsilon> 0$, and $s\geq 3$ be an odd integer sufficiently large with respect to $\varepsilon$. Then among the numbers $$\zeta(3), \, \zeta(5), \, \zeta(7), \, \ldots , \zeta(s),$$ at least $$2^{(1-\varepsilon)\frac{\log s}{\log \log s}}$$ are irrational.*

In this result, the lower bound is asymptotically greater than $\exp(\sqrt{\log s})$, and than any power of $\log s$; "to put it roughly, \[it is\] much more like a power of $s$ than a power of $\log s$" [@HW Chapter XVIII, §1].

In comparison, Theorem 1 gives only $\frac{1-\varepsilon}{1+ \log 2} \log s$ irrational odd zeta values, but they are linearly independent over the rationals, whereas Theorem 2 ends up only with their irrationality.

Our proof of Theorem 2 follows the above-mentioned strategy of the second and third authors. The main new ingredient, compared to the proof in [@Sprang], is taking $D$ large (about $s^{1-2\varepsilon}$) and equal to the product of the first prime numbers (the so-called primorial) --- such a number has asymptotically the largest possible number of divisors with respect to its size (see [@HW Chapter XVIII, §1]). To perform the required elimination of a prescribed set of odd zeta values, we need to establish that a certain auxiliary matrix is invertible. Whereas the second author's choice of $D$ in [@Sprang] allows him to deal with elementary properties of a Vandermonde matrix, we use at this step a generalization of the corresponding result. We give three different proofs of the latter, based on arguments from combinatorics of partitions, from linear algebra accompanied with a lemma of Fekete, and from analysis using Rolle's theorem.

The structure of this paper is as follows. In §1 we construct linear forms in values of the Hurwitz zeta function. Denominators of the coefficients are studied in §2; and the asymptotics of the linear forms are dealt with in §3. Section 4 is devoted to the proof that an auxiliary matrix is invertible. Finally, we establish Theorem 2 in §5.

# Construction of linear forms

From now on we let $s$, $D$ be positive integers such that $s \geq 3D$; we assume that $s$ is odd. Let $n$ be a positive integer, such that $Dn$ is even. Consider the following rational function: $$R_n(t) = D^{3Dn} \, \, n!^{s+1-3D} \, \, \frac{ \prod_{j=0}^{3Dn} (t-n+\frac{j}{D})}{ \prod_{j=0}^{ n} (t+j)^{s+1}}$$ which, of course, depends also on $s$ and $D$. Notice that the difference of the function from the corresponding one in [@Sprang] is in the factor $D^{3Dn}$ instead of $D^{6(D-1)n}$ (see Eq. (eqSprang)).

Similar rational functions have already been considered, see [@Catalan] for the case $D=2$ and [@Nash; @Nishimoto; @SFcaract] for general $D$. However the "central" factors $t-n+\frac{j}{D}$ with $Dn < j < 2Dn$ are missing, and (as the second author noticed [@Sprang]) they play a central role in the arithmetic estimates (see Lemma 2 below).

***Remark** 1*. Though one can implement an additional parameter $r$ in the definition of the rational function $R_n(t)$, in a way similar to the one for the Ball--Rivoal series (eqBR), we have verified that this does not bring any improvement to the result of Theorem 2.

The rational function $R_n(t)$ has a partial fraction expansion $$\label{eqelsples}
R_n(t) = \sum_{i=1}^s \sum_{k=0}^n \frac{a_{i,k}}{(t+k)^i}.$$ For any $j\in \{1,\ldots,D\}$, take $$r_{n,j} = \sum_{m=1}^\infty R_n\Big(m+\frac{j}{D}\Big).$$

We recall that the Lerch and Hurwitz zeta functions are defined by $$\Phi(z,i,\alpha) = \sum_{n=0}^{\infty}\frac{z^n}{(n+\alpha)^i}
\quad\mbox{and}\quad
\zeta(i,\alpha) = \Phi(1,i,\alpha) = \sum_{n=0}^\infty \frac1{(n+\alpha)^i},$$ where $\alpha>0$ and also $i\geq 2$ for the latter.

The following is precisely [@Sprang Lemma 1.5]; the change of the normalizing factor $D^{3Dn}$ does not affect the statement.

**Lemma 1**. *For each $j\in \{1,\ldots,D\}$, we have $$r_{n,j}
 = \rho_{0,j}+\sum_{\substack{3\leq i \leq s\\i \;\mbox{\scriptsize odd}}} \rho_i \, \zeta\Big(i, \frac{j}{D}\Big),$$ where $$\rho_i = \sum_{k=0}^n a_{i,k} \quad\mbox{for $3\leq i \leq s$, \ $i$ odd},$$ does not depend on $j$, and $$\label{eqdefrhoz}
 \rho_{0,j} = - \sum_{k=0}^n \sum_{\ell=0}^k \sum_{i=1}^s \frac{ a_{i,k}}{(\ell+\frac{j}{D})^i} .$$*

We follow the strategy of proofs in [@Zudilintrick Lemma 3] and [@Sprang Lemma 1.5]. Let $z$ be a real number such that $0<z<1$. We have $$\begin{aligned}
\sum_{m=1}^\infty R_n\Big(m+\frac{j}{D}\Big) z^m
&= \sum_{m=1}^\infty \sum_{i=1}^s \sum_{k=0}^n \frac{a_{i,k} z^m }{(m+k+\frac{j}{D})^i} \\
&= \sum_{i=1}^s \sum_{k=0}^n a_{i,k} z^{-k} \sum_{m=1}^\infty\frac{ z^{m+k} }{(m+k+\frac{j}{D})^i} \\
&= \sum_{i=1}^s \sum_{k=0}^n a_{i,k} z^{-k} \bigg( \Phi\Big(z, i, \frac{j}{D}\Big) - \sum_{\ell = 0}^k \frac{z^\ell}{(\ell+\frac{j}{D})^i} \bigg).

\end{aligned}$$ Now we let $z$ tend to 1 in the equality we have obtained; the left-hand side tends to $r_{n,j}$. On the right-hand side, the term involving the Lerch function with $i=1$ has coefficient $\sum_{k=0}^n a_{1,k} z^{-k}$. Since $\Phi(z,1,\frac{j}{D})$ has only a logarithmic divergence as $z\to 1$ and $$\sum_{k=0}^n a_{1,k} =\lim_{t\to \infty } t R_n(t) =0,$$ this term tends to 0 as $z\to1$. All other terms have finite limits as $z\to 1$, so that $$r_{n,j} = \rho_{0,j}+\sum_{i=2}^s \rho_i \, \zeta\Big(i, \frac{j}{D}\Big),$$ where $\rho_{0,j}$ is given by Eq. (eqdefrhoz), and $\rho_i = \sum_{k=0}^n a_{i,k}$ for any $i\in \{2,\ldots,s\}$.

To complete the proof, we apply the symmetry phenomenon of [@BR; @RivoalCRAS]. Since $s$ is odd and $Dn$ is even we have $R_n(-n-t) = - R_n(t)$. Now the partial fraction expansion (eqelsples) is unique, so that $a_{i,n-k} = (-1)^{i+1} a_{i,k}$ for any $i$ and $k$. This implies that $\rho_i = 0$ when $i$ is even, and Lemma 1 follows.

# Arithmetic estimates

As usual we let $d_n = \operatorname{lcm}(1,2,\ldots,n)$.

**Lemma 2**. *We have $$\label{arith-I}
d_n^{s+1-i} \rho_i \in\mathbb{Z}\quad\mbox{for}\; i = 3, 5, \ldots, s,$$ and $$\label{arith-II}
d_{n+1}^{s+1} \rho_{0,j} \in\mathbb{Z}\quad\mbox{for any}\; j\in \{1,\ldots,D\}.$$*

For part (arith-I) we use the strategy of the proof of [@SFcaract Lemma 4.5]; note that [@Sprang Lemma 1.3] does not apply in our present situation because of the different normalization of the rational function $R_n(t)$ compared to the one in (eqSprang). To establish (arith-II) we follow the proof of [@Sprang Lemma 1.4]; we use $d_{n+1}$ here instead of $d_n$ to include the case corresponding to $j=D$.

For any $\alpha\in\frac1{D}\mathbb{Z}$ we introduce $$F_\alpha(t) = D^n \, \, \frac{\prod_{j=1}^n (t+\alpha+\frac{j}{D})}{\prod_{j=0}^n( t+j)} = \sum_{k=0}^n \frac{A_{\alpha,k}}{t+k},$$ where $A_{\alpha,k}$ is an integer in view of the explicit formulas $$(-1)^k A_{\alpha,k} = \binom{n}{k} \frac{\prod_{j=1}^n (D( \alpha-k)+j )}{n!} = \begin{cases}
\binom{n}{k} \binom{D( \alpha-k) +n}{n} &\mbox{if}\; \alpha-k\geq 0, \\
0 &\mbox{if}\; \frac{-n}{D} \leq \alpha-k < 0, \\
(-1)^n \binom{n}{k} \binom{D(k- \alpha) -1}{n} &\mbox{if}\; \alpha-k < \frac{-n}{D} .
\end{cases}$$ We also consider $$G(t) = \frac{n!}{\prod_{j=0}^n (t+j)} = \sum_{k=0}^n \frac{ (-1)^k \binom{n}{k} }{t+k},$$ so that $$\label{eqpro}
R_n(t) = (t-n) \, G(t)^{s+1-3D} \, \prod_{\ell = 0 }^{3D-1} F_{-n+\frac{\ell n}{D}}(t).$$ From this expression we compute the partial fraction expansion of $R_n(t)$ using the rules $$\frac{t-n}{t+k} = 1 - \frac{k+n}{t+k}
\quad\mbox{and}\quad
 \frac{1}{(t+k)(t+k')} = \frac{1}{(k'-k)(t+k)}+\frac{1}{(k- k')(t+k')} \quad\mbox{for}\; k\neq k'.$$ A denominator appears each time the second rule is applied, and the denominator is always a divisor of $d_n$ (see [@Colmez] or [@Zudilintrick Lemma 1]). This happens $s+1-i$ times in each term that contributes to $a_{i,k}$ because there are $s+1$ factors in the product (eqpro) (apart from $t-n$). Therefore, $$d_{n}^{s+1-i} a_{i,k} \in \mathbb{Z}\quad\mbox{for any $i$ and $k$},$$ implying (arith-I).

We now proceed with the second part of Lemma 2, that is, with demonstrating the inclusions (arith-II). Recall from Lemma 1 that $$\label{eqrhoz}
d_{n+1}^{s+1} \rho_{0,j} = - \sum_{k=0}^n \sum_{\ell=0}^k \bigg( \sum_{i=1}^s \frac{d_{n+1}^{s+1} a_{i,k}}{(\ell+\frac{j}{D})^i}\bigg).$$ If $j=D$ then $$d_{n+1}^{s+1-i} a_{i,k} \quad\text{and}\quad \frac{d_{n+1}^i}{(\ell+\frac{j}{D})^i}$$ are integers for any $k$, $\ell$ and $i$, so that $d_{n+1}^{s+1} \rho_{0,j} \in\mathbb{Z}$. From now on, we assume that $1\leq j \leq D-1$ and we prove that for any $k$ and any $\ell$ the internal sum over $i$ in Eq. (eqrhoz) is an integer. With this aim in mind, fix integers $k_0$ and $\ell_0$, with $0\leq \ell_0 \leq k_0 \leq n$, and assume that the corresponding sum is not an integer. Since $1\leq j \leq D-1$ we have $R_n(\ell_0-k_0+\frac{j}{D}) = 0$, so that $$\label{eqentier}
\sum_{i=1}^s \frac{d_{n+1}^{s+1} a_{i,k_0}}{(\ell_0+\frac{j}{D})^i}
= - \sum_{\substack{k=0\\k\neq k_0}}^n \sum_{i=1}^s \frac{d_{n+1}^{s+1} a_{i,k}}{(\ell_0-k_0+k +\frac{j}{D})^i} .$$ This rational number is not an integer: it has negative $p$-adic valuation for at least one prime number $p$. Therefore, on either side of (eqentier) there is at least one term with negative $p$-adic valuation: there exist $i_0,i_1\in\{1,\ldots,s\}$ and $k_1\in \{0,\ldots,n\}$, $k_1\neq k_0$, such that $$v_p\bigg( \frac{d_{n+1}^{s+1} a_{i_0,k_0}}{( \ell_0+\frac{j}{D})^{i_0}} \bigg) < 0 \quad \mbox{and} \quad
v_p\bigg( \frac{d_{n+1}^{s+1} a_{i_1,k_1}}{( \ell_0-k_0+k_1+\frac{j}{D})^{i_1}} \bigg) < 0.$$ Since $d_{n+1}^{s+1-i} a_{i,k}\in\mathbb{Z}$ for any $i$ and $k$, this leads to $$v_p\bigg( \frac{d_{n+1}^{i_0} }{( \ell_0+\frac{j}{D})^{i_0}} \bigg) < 0
\quad \mbox{and} \quad
v_p\bigg( \frac{d_{n+1}^{i_1} }{( \ell_0-k_0+k_1+\frac{j}{D})^{i_1}} \bigg) < 0,$$ implying $$\min\bigg( v_p \Big( \ell_0+\frac{j}{D} \Big) , \, v_p \Big( \ell_0-k_0+k_1+\frac{j}{D} \Big)\bigg)> v_p(d_{n+1}).$$ As $k_0 - k_1 = ( \ell_0+\frac{j}{D} ) - ( \ell_0-k_0+k_1+\frac{j}{D} )$, we deduce that $v_p(k_0 - k_1 ) > v_p(d_{n+1})$, which is impossible in view of the inequality $0 < |k_0 - k_1 | \leq n$. The contradiction completes the proof of Lemma 2.

***Remark** 2*. It is made explicit in [@RZnote], for a particular situation considered there, that the inclusions in Lemma 2 can be sharpened as follows: $$\Phi_n^{-1}d_n^{s+1-i} \rho_i \in\mathbb{Z}\quad\mbox{for}\; i = 3, 5, \ldots, s,$$ and $$\Phi_n^{-1}d_{n+1}^{s+1} \rho_{0,j} \in\mathbb{Z}\quad\mbox{for any}\; j\in \{1,\ldots,D\},$$ where $\Phi_n=\Phi_n(D)$ is a certain product over primes in the range $2\le p\le n$, whose asymptotic behavior $$\phi=\phi(D)=\lim_{n\to\infty}\frac{\log\Phi_n}n$$ can be controlled by means of the prime number theorem. It is possible to show that the quantity $\phi(D)/D$ increases to $\infty$ and at the same time $\phi(D)/(D\log^\varepsilon D)\to0$ as $D\to\infty$, for any choice of $\varepsilon>0$. Later, we choose $D$ such that $D\log D <s$, implying that the arithmetic gain coming from the factors $\Phi_n^{-1}$ is asymptotically negligible as $s\to\infty$.

# Asymptotic estimates of the linear forms

The following lemma is proved along the same lines as [@Sprang Lemma 2.1] (see also [@Zudilintrick Lemma 4] and the second proof of [@BR Lemme 3]). The difference is that here we only assume $\frac{s}{  D\log D}$ to be sufficiently large, whereas in [@Sprang] parameter $D$ is fixed and $s\to\infty$.

**Lemma 3**. *Assume that $$\label{eqhyp}
\frac{s}{  D\log D} \quad\mbox{is sufficiently large.}$$ Then we have $$\label{eqasyun}
\lim_{n\to\infty} r_{n,j}^{1/n} = g(x_0) <3^{-(s+1)} \quad\mbox{and}\quad \lim_{n\to\infty} \frac{r_{n,j'}}{r_{n,j}} = 1
\quad\mbox{for any}\; j,j'\in\{1,\ldots,D\},$$ where $$g(x) = D^{ 3D } \, \frac{ (x+3)^{3D} (x+1)^{ s+1 }}{ ( x+2)^{2(s+1)}}$$ and $x_0$ is the unique positive root of the polynomial $$(X+3)^D(X+1)^{s+1} - X^D (X+2)^{s+1}.$$*

For $j\in \{1,\ldots,D\}$ and $k\geq 0$, let $$c_{k,j} = R_n\Big( n+k+\frac{j}{D}\Big)
= D^{ 3D n} \, n!^{s+1-3D} \, \frac{ \prod_{\ell=0}^{3Dn} ( k +\frac{j+\ell }{D})}{ \prod_{\ell=0}^{ n} (n+k+\ell+\frac{j}{D})^{s+1}},$$ so that $$r_{n,j} = \sum_{m=1}^\infty R_n\Big(m+\frac{j}{D}\Big) = \sum_{k=0}^\infty c_{k,j}$$ is a sum of positive terms. We have $$\label{eqquok}
\frac{c_{k+1,j}}{c_{k,j}} = \bigg( \prod_{\ell = 1}^D \frac{k+3n+\frac{j+\ell}{D}}{k+\frac{j+\ell-1}{D}}\bigg) \, \bigg( \frac{k+n+\frac{j}{D}}{k+2n+1+ \frac{j}{D}}\bigg)^{s+1}$$ implying that, for any $j$, the quotient $\frac{c_{k+1,j}}{c_{k,j}}$ tends to $f(\kappa)$ as $n\to\infty$ assuming $k\sim \kappa n$ for $\kappa>0$ fixed, where $$f(x) = \Big( \frac{ x+ 3 }{x}\Big) ^D \Big( \frac{ x+ 1 }{x+2}\Big) ^{s+1}.$$ For the logarithmic derivative of this function we have $$\frac{f'(x)}{f(x)} =
\frac{D}{x+3} - \frac{D}{x }+\frac{s+1}{x+ 1 } - \frac{s+1}{x+ 2} =
\frac{ ax^2+bx+c}{x(x+1)(x+2)(x+3)}$$ with $a = s+1-3D > 0$ and $c = -6   D < 0$, hence the derivative $f'(x)$ vanishes exactly at one positive real number $x_1$. This means that the function $f(x)$ decreases on $(0, x_1]$ and increases on $[x_1,+\infty)$. Since $\lim_{x\to 0^+} f(x) = +\infty$ and $\lim_{x\to+\infty} f(x) = 1$, we deduce that there exists a unique positive real number $x_0$ such that $f(x_0 ) = 1$.

Let us now prove (eqasyun). As in [@Bruijn §3.4] we wish to demonstrate that the asymptotic behaviour of $r_{n,j}$ is governed by the terms $c_{k,j}$ with $k$ close to $x_0n$ (see Eq. (eqenca) below). To begin with, notice that $$\begin{aligned}
c_{k,j}
&= D^{-1} \, n!^{s+1-3D} \, \frac{ \prod_{\ell=0}^{3Dn} ( Dk+j+\ell )}{ \prod_{\ell=0}^{ n} (n+k+\ell+\frac{j}{D})^{s+1}}\\
&= D^{-1} \, n!^{s+1-3D} \, \frac{(3Dn+Dk+j)!}{(Dk+j-1)!} \, \frac{\Gamma(n+k+\frac{j}{D})^{s+1}}{\Gamma (2n+k +1+\frac{j}{D})^{s+1}}.
\end{aligned}$$ Denoting by $k_0 (n)$ the integer part of $x_0 n$ and applying the Stirling formula to the factorial and gamma factors we obtain, as $n\to\infty$, $$\begin{aligned}
c_{k_0(n),j}^{1/n}
&\sim
\Big(\frac{n}{e}\Big) ^{s+1-3D} \,  \bigg(\frac{3Dn+Dk_0(n)+j }{e}\bigg) ^{ 3D+Dx_0}
 \, \bigg(\frac{e}{Dk_0(n)+j-1 }\bigg) ^{ Dx_0} \nonumber \\
& \qquad \times
\bigg(\frac{n+k_0(n)+\frac{j}{D} -1 }{e}\bigg) ^{ (s+1)( x_0+1)}
 \, \bigg(\frac{e}{2n+k_0(n) +\frac{j}{D}}\bigg) ^{ (s+1)( x_0+2)} \nonumber \\
 &\sim \frac{((x_0+3)D)^{ (x_0+3)D}}{(x_0D)^{x_0D}}\, \frac{(x_0+1)^{(s+1)(x_0+1)} }{(x_0+2)^{(s+1)( x_0+2)} } \nonumber \\
& = g(x_0) f(x_0)^{x_0} = g(x_0). \label{eqasykz}
\end{aligned}$$

We shall now give details that the asymptotic behavior of $r_{n,j}$ as $n\to\infty$ is determined by the terms $c_{k,j}$ with $k$ close to $x_0n$. Given $D$ and $s$, we take $\varepsilon>0$ sufficiently small to accommodate the condition $$b(\varepsilon) = \max\Big( f(x_0+\varepsilon), \frac1{f(x_0-\varepsilon)}\Big)<1.$$ Then there exists $A(\varepsilon) > x_1$, where $x_1$ is the unique positive root of $f'(x)=0$, such that $f(A(\varepsilon))=b(\varepsilon)$. We have $f(x) \geq \frac1{b(\varepsilon)}$ for any $x\in (0, x_0-\varepsilon]$ and $f(x) \leq b(\varepsilon)$ for any $x\in [ x_0+\varepsilon, A(\varepsilon)]$. For any $k$ such that $(x_0+2\varepsilon)n \leq k\leq (A(\varepsilon)-\varepsilon)n$, Eq. (eqquok) implies that $c_{k,j} \leq b(\varepsilon) c_{k-1,j}$ provided $n$ is large (in terms of $D$, $s$ and $\varepsilon$), so that taking $k_1 = \lfloor (x_0+2\varepsilon)n \rfloor$ and $k_2 = \lfloor (x_0+3\varepsilon)n \rfloor$ we obtain $$\label{eqsommeun}
\sum_{k_2\leq k\leq (A(\varepsilon)-\varepsilon)n} c_{k,j} \leq c_{k_1,j}\sum_{k=k_2}^{+\infty} b(\varepsilon)^{k-k_1}\leq c_{k_1,j}\frac{b(\varepsilon)^{k_2-k_1}}{1-b(\varepsilon)} \leq \varepsilon\, c_{k_1,j}$$ for all $n$ sufficiently large. In the same way, we get the estimate $$\label{eqsommede}
\sum_{1\leq k\leq \lfloor (x_0-3\varepsilon)n \rfloor } c_{k,j} \leq \varepsilon c_{ \lfloor (x_0-2\varepsilon)n \rfloor , j}$$ for all $n$ large (in terms of $D$, $s$ and $\varepsilon$). At last, choosing $\varepsilon$ small we can assume that $A(\varepsilon)$ is sufficiently large (in terms of $D$ and $s$), so that for $k \geq (A(\varepsilon)-\varepsilon)n$ we have $$c_{k,j} \leq (2D)^{3Dn} \bigg( \frac{n!}{k^{n+1}}\bigg)^{ s+1 - 3D}$$ for $n$ large. Using hypothesis (eqhyp) and the Stirling formula, the latter estimate implies $$\begin{aligned}
\sum_{k = \lceil (A(\varepsilon)-\varepsilon)n\rceil} ^{+\infty} c_{k,j}
&\leq (3D)^{3Dn} \frac{n!^{ s+1 - 3D}}{((A(\varepsilon)-\varepsilon)n)^{(s+1-3D)(n+1)-1}} \nonumber\\
&\leq \bigg( \frac{3D}{e (A(\varepsilon)-\varepsilon)}\bigg)^{sn/2}
\leq \Big( \frac12 g(x_0)\Big)^n
\label{eqsommetr}
\end{aligned}$$ provided $n$ is sufficiently large. Combining Eqs. (eqasykz), (eqsommeun), (eqsommede) and (eqsommetr) we obtain $$\label{eqenca}
(1-3\varepsilon) r_{n,j} \leq \sum_{ (x_0-3\varepsilon)n \leq k \leq (x_0+3\varepsilon)n } c_{k,j} \leq r_{n,j}.$$ Now for any $k$ in the range $(x_0-3\varepsilon)n \leq k \leq (x_0+3\varepsilon)n$ it follows from the proof of Eq. (eqasykz) that $$g(x_0)-h(\varepsilon) \leq c_{k,j}^{1/n} \leq g(x_0)+h(\varepsilon)$$ for $n$ large (in terms of $D$, $s$ and $\varepsilon$), where $h$ is a positive function of $\varepsilon$ such that $\lim_{\varepsilon\to0^+} h(\varepsilon) = 0$. This implies $$(g(x_0)-2h(\varepsilon))^n \leq 5\varepsilon n (g(x_0)-h(\varepsilon))^n \leq r_{n,j} \leq \frac{7\varepsilon n}{1-3\varepsilon} (g(x_0)+h(\varepsilon))^n \leq (g(x_0)+2h(\varepsilon))^n$$ for $n$ sufficiently large, and finishes the proof of $\lim_{n\to\infty} r_{n,j}^{1/n} = g(x_0)$ for any $j$.

To establish $$\lim_{n\to\infty} \frac{r_{n,j'}}{r_{n,j}} = 1$$ for any $j,j'\in\{1,\ldots,D\}$, we can assume that $1\leq j \leq D-1$ and $j'=j+1$. For any $k$ we have $$\frac{c_{k,j+1}}{c_{k,j}} =
\frac{k+3D+\frac{j+1}{D}}{k+ \frac{j}{D}} \bigg( \frac{ \Gamma( n+k+\frac{j+1}{D})}{\Gamma( n+k +\frac{j }{D})}
\, \frac{ \Gamma( 2n+k+1+\frac{j }{D})}{\Gamma( 2n+k+1+\frac{j+1}{D})}\bigg)^{s+1}.$$ It follows from the Stirling formula that $\Gamma(x+\frac1{D}) \sim x^{1/D}\Gamma(x)$ as $x\to\infty$, so that for $k = \lfloor x_0 n\rfloor$ we have, as $n\to\infty$, $$\frac{c_{k,j+1}}{c_{k,j}} \sim
\frac{x_0+3}{x_0}\bigg( \frac{(x_0+1)^{1/D}}{(x_0+2)^{1/D}}\bigg)^{s+1} = f(x_0)^{1/D} = 1.$$ More generally, for $k$ in the range $(x_0-3\varepsilon)n \leq k \leq (x_0+3\varepsilon)n$ and $n$ sufficiently large we have $$1-\tilde h(\varepsilon) \leq \frac{c_{k,j+1}}{c_{k,j}} \leq 1-\tilde h(\varepsilon)$$ with $\lim_{\varepsilon\to0^+} \tilde h(\varepsilon) = 0$. Using Eq. (eqenca) this concludes the proof of (eqasyun), except for the upper bound on $g(x_0)$ that we shall verify now.

To estimate $g(x_0)$ from above, we first show that $x_0<a$, where $a = 4\cdot 2^{-\frac{s+1}{D}}$. Observe that $a < \frac12$, since $\frac{s}{D}\geq 3$. For any $x>0$ we have $$\frac{x+1}{x+2} \leq \frac{1}{2} \Big( 1 + \frac{x}{2}\Big)$$ implying $$f(a) \leq \Big( \frac78\Big) ^D  \Big( 1 + \frac{a}{2}\Big)^{s+1}.$$ As $\frac sD$ is large and $\log(\frac78) < -\frac{1}{10}$, we deduce that $$f(a)^{1/(s+1)} \leq \Big( \frac78\Big) ^{\frac{D}{s+1}}
  \Big( 1 + \frac{a}{2}\Big) < \bigg( 1 -  \frac{1}{10} \frac{D}{s+1}\bigg)   \big( 1 +   2^{1-\frac{s+1}{D}}\big) < 1,$$ so that we indeed have $x_0<a<\frac12$. Now this upper bound for $x_0$ implies $$\log g(x_0) \leq 3D\log D + 3D  \log  \Big(\frac72\Big)  + (s+1) \big(  \log(a+1) - 2  \log (a+2)\big).$$ By taking $\frac{s}{D\log D}$ sufficiently large, we may ensure that the first two terms are sufficiently small in comparison with $s$ and that $a$ is sufficiently close to 0, so that $\log g(x_0) < - (s+1) \log 3$.

This completes our proof of Lemma 3.

***Remark** 3*. For $s=77$ and $D=4$ one computes $g(x_0) <  \exp(-78)$. Thus, the suitable linear combinations $$\hat{r}_{n,1}=r_{n,4}, \quad
        \hat{r}_{n,2}=r_{n,2}+r_{n,4} \quad\mbox{and}\quad
        \hat{r}_{n,4}=r_{n,1}+r_{n,2}+r_{n,3}+r_{n,4}$$ of the corresponding linear forms allow us to eliminate three of the odd zeta values on the list $$\{\zeta(3),\zeta(5),\ldots,\zeta(77)\}.$$ In particular, we obtain that two out of $\{\zeta(5),\zeta(7),\ldots,\zeta(77)\}$ are irrational. This result is slightly weaker than the result of Rivoal and the third author [@RZnote], but it drops out as a byproduct of the construction above. The arithmetic gain given by $\Phi_n(4)$ for $\Phi_n(D)$ defined in Remark 2 can be used to slightly reduce the bound of $77$ to $73$, still weaker than the one in [@RZnote].

# A non-vanishing determinant

The following lemma is used to eliminate irrational zeta values in §5 below.

**Lemma 4**. *For $t\geq 1$, let $x_1<\ldots<x_t$ be positive real numbers and $\alpha_1<\ldots<\alpha_t$ non-negative integers. Then the generalized Vandermonde matrix $[x_j^{\alpha_i}]_{1\leq i,j \leq t}$ has positive determinant.*

We remark that, subject to the hypothesis that $x_1,\ldots,x_t$ are real and positive, Lemma 4 is a stronger version of [@LMN Lemme 1] and, therefore, has potential applications to the zero estimates for linear forms in two logarithms.

The above result is quite classical and known to many people. While writing this paper we have found various proofs of rather different nature, three given below. We leave it to the readers to choose their favorite proof.

As pointed out in [@Krattdet §2.1], the generalized Vandermonde determinant in question is closely related to Schur polynomials. Let $\Delta := \det [x_j^{\alpha_{i}}]_{1\leq i,j \leq t}$, and $$V = \det [x_j^{i-1}]_{1\leq i,j \leq t} = \prod_{1\leq i < j \leq t} (x_j-x_i) >0$$ be the Vandermonde determinant of $x_1,\ldots, x_t$. For any $i\in\{1,\ldots,t\}$, we take $\lambda_i = \alpha_{t+1-i}+i - t$, so that $\lambda_1 \geq \ldots \geq \lambda_t \geq 0$; then $\lambda = (\lambda_1,\ldots,\lambda_t)$ is a partition of the integer $\lambda_1+\ldots+\lambda_t$. The associated Schur polynomial $$s_\lambda = s_\lambda (x_1,\ldots, x_t)= \frac{\Delta}{V}$$ possesses the following expression: $$s_\lambda = \sum_\mu K_{\lambda,\mu} m_\mu$$ with the sum over partitions $\mu$ (see, for instance, [@FH Appendix A] or [@Macdonald], and [@Proctor] for a direct proof). Here $m_\mu$ denotes the monomial symmetric polynomial $\sum_\sigma x_1^{\mu_{\sigma(1)}}\ldots  x_t^{\mu_{\sigma(t)}}$, where the sum is over the distinct permutations of $\mu$, while the coefficients $K_{\lambda,\mu}$ are non-negative integers and $K_{\lambda,\lambda}=1$. From this we deduce that $s_\lambda$ is a positive real number, thus $\Delta=s_\lambda V>0$.

Write $A_{J,K}$ for the minor of an $n\times m$-matrix $A$, where $n\le m$, determined by ordered index sets $J$ and $K$. A classical result due to Fekete [@fekete] asserts that if all $(n-1)$-minors $$A_{(1,2,\ldots,n-1),K},\quad K=(k_1,\ldots,k_{n-1}) \quad\text{with}\; 1\leq k_1<\ldots<k_{n-1}\leq m$$ are positive, and all minors of size $n$ with consecutive columns are positive, then all $n$-minors of $A$ are positive. Thus, Lemma 4 follows by induction on $t$ from Fekete's result applied to the matrix $[x_j^k]_{1\leq j \leq t,\, 0\leq k < m}$, using the positivity of the Vandermonde determinant.

By induction on $t$ one proves the following claim: *A non-zero function $$f(x)=\sum_{i=1}^t c_i x^{\alpha_i},$$ with $c_i,\alpha_i\in\mathbb{R}$, has at most $t-1$ positive zeros.* Indeed, if $f$ has $t$ positive zeros then Rolle's theorem provides $t-1$ positive zeros of the derivative $\frac{\mathrm{d}}{\mathrm{d}x} (x^{-\alpha_1} f(x))$. The non-vanishing of the determinant in Lemma 4 is an immediate consequence of this claim. Since the determinant depends continuously on the parameters $\alpha_i$, we deduce the required positivity from the positivity of the Vandermonde determinant.

# Elimination of odd zeta values

Let $0 < \varepsilon< \frac13$, and let $s$ be odd and sufficiently large with respect to $\varepsilon$. We take $D$ to be the product of all primes less than or equal to $(1-2\varepsilon) \log s$ (such a product has asymptotically the largest possible number of divisors with respect to its size, see [@HW Chapter XVIII, §1]). We have $$\log D \, = \sum_{\substack{p \; \mbox{\scriptsize prime}\\ p\leq (1-2\varepsilon) \log s}} \log p \, \leq ( 1-\varepsilon) \log s$$ by the prime number theorem, that is, $D\leq s^{1-\varepsilon}$. Then $D \log D \leq  s^{1-\varepsilon}\log s$: the assumption of Lemma 3 holds.

Notice that $D$ has precisely $\delta = 2^{\pi( (1-2\varepsilon) \log s)}$ divisors, with $$\log \delta = \pi( (1-2\varepsilon) \log s)\, \log 2 \geq (1-3\varepsilon) (\log 2) \,\frac{\log s}{\log \log s}.$$ Assume that the number of irrational odd zeta values between $\zeta(3)$ and $\zeta(s)$ is less than $\delta$. Let $3 = i_1 < i_2 < \ldots < i_{\delta-1}\leq s$ be odd integers such that if $\zeta(i)\not\in\mathbb{Q}$ and $i$ is odd, $3\leq i \leq s$, then $i=i_j$ for some $j$. We set $i_0=1$, and consider the set ${\mathcal D}$ of all divisors of $D$, so that $\operatorname{Card}{\mathcal D}= \delta$. Lemma 4 implies that the matrix $[d^{i_j}]_{d\in{\mathcal D}, 0\leq j \leq \delta-1}$ is invertible. Therefore, there exist integers $w_d \in \mathbb{Z}$, where $d\in{\mathcal D}$, such that $$\label{eqwun}
\sum_{d\in{\mathcal D}}w_d \, d^{i_j} = 0 \quad\mbox{for any}\; j\in\{1,\ldots,\delta-1\}$$ and $$\label{eqwde}
\sum_{d\in{\mathcal D}}w_d \, d^{i_0} = \sum_{d\in{\mathcal D}}w_d \, d \neq 0.$$ With the help of Lemma 1 we construct the linear forms $$r_{n,j} = \rho_{0,j}+\sum_{\substack{3\leq i \leq s\\i \;\mbox{\scriptsize odd}}} \rho_i \, \zeta\Big(i, \frac{j}{D}\Big)$$ for $n \geq 1$ and $1\leq j \leq D$. The crucial point (as in [@Sprang §3]) is that for any $d\in{\mathcal D}$ and any $i\geq 2$, $$\sum_{j=1}^d \zeta\bigg(i, \frac{j \frac{D}{d}}{D}\bigg) = \sum_{j=1}^d \zeta\Big(i, \frac{j}{d}\Big) = \sum_{n=0}^\infty \sum_{j=1}^d \frac{d^i}{(dn+j)^i} = d^i \zeta(i)$$ implying that $$\widehat r_{n,d} = \sum_{j=1}^d r_{n, j\frac{D}{d}}
= \sum_{j=1}^d \rho_{0,j\frac{D}{d}} +\sum_{\substack{3\leq i \leq s\\i \;\mbox{\scriptsize odd}}} \rho_i \, d^i \, \zeta(i),$$ are linear forms in the odd zeta values with asymptotic behavior $$\widehat r_{n,d} = (d+o(1))r_{n,1} \quad\text{as}\; n\to\infty, \quad\mbox{where}\; \lim_{n\to\infty} r_{n,1}^{1/n} = g(x_0) <3^{-(s+1)},$$ by Lemma 3.

We shall use now the integers $w_d$ to eliminate the odd zeta values $\zeta(i_j)$ for $j=1,\dots,\delta-1$, including all irrational ones, as in [@Zudilintrick] and [@Sprang]. For that, consider $$\widetilde r_n = \sum_{d\in{\mathcal D}} w_d \, \widehat r_{n,d}.$$ Eqs. (eqwun) imply that $$\widetilde r_n = \sum_{d\in{\mathcal D}} w_d \sum_{j=1}^d \rho_{0,j\frac{D}{d}} +\sum_{i\in I } \rho_i \bigg( \sum_{d\in{\mathcal D}} w_d \, d^i \bigg) \zeta(i),$$ where $I = \{3,5,7,\ldots,s\}\setminus \{i_1,\ldots,i_{\delta-1}\}$; in particular, no irrational zeta value $\zeta(i)$, where $3\leq i\leq s$, appears in this linear combination. Using Eq. (eqwde) we obtain $$\widetilde r_n = \bigg( \sum_{d\in{\mathcal D}}w_d \, d +o(1) \bigg) r_{n,1}  \quad \mbox{ with }   \quad \sum_{d\in{\mathcal D}}w_d \, d \neq 0,$$ so that $$\lim_{n\to\infty} | \widetilde r_n | ^{1/n} = g(x_0) <3^{-(s+1)}.$$

Now all $\zeta(i)$, $i\in I$, are assumed to be rational. Denoting by $A$ their common denominator, we deduce from Lemma 2 that $A d_{n+1}^{s+1} \widetilde r_n$ is an integer. From the prime number theorem we have $\lim_{n\to\infty} d_{n+1}^{1/n} = e$, hence the sequence of integers satisfies $$0 < \lim_{n\to\infty} | A d_{n+1}^{s+1} \widetilde r_n | ^{1/n} = e^{s+1} g(x_0) < \Big(\frac{e}{3}\Big)^{s+1} < 1.$$ This contradiction concludes the proof of Theorem 2.

## Acknowledgements {#acknowledgements .unnumbered}

We thank Michel Waldschmidt for his advice, Ole Warnaar for his comments on an earlier draft of the paper, and Javier Fresán for educating us about the state of the art in Grothendieck's period conjecture and its consequences.

10

[R. Apéry] -- "Irrationalité de $\zeta(2)$ et $\zeta(3)$", in *Journées Arithmétiques (Luminy, 1978)*, Astérisque, no. 61, 1979, p. 11--13.

[K. Ball & T. Rivoal] -- " Irrationalité d'une infinité de valeurs de la fonction zêta aux entiers impairs", *Invent. Math.* **146** (2001), no. 1, p. 193--207.

[N. G. de Bruijn] -- *Asymptotic methods in analysis*, Dover Publications, 1981.

[P. Colmez] -- "Arithmétique de la fonction zêta", in *Journées mathématiques X-UPS 2002*, éditions de l'école Polytechnique, 2003, p. 37--164.

[M. Fekete & G. Pólya] -- "Über ein Problem von Laguerre", *Rendiconti del Circolo Matematico di Palermo* **34** (1912), p. 89--120.

[S. Fischler] -- "Shidlovsky's multiplicity estimate and irrationality of zeta values", preprint arXiv 1609.09770 \[math.NT\], J. Austral. Math. Soc., to appear.

--- , "Irrationalité de valeurs de zêta (d'après Apéry, Rivoal, \...)", in *Sém. Bourbaki 2002/03*, Astérisque, no. 294, 2004, exp. no. 910, p. 27--62.

[S. Fischler & W. Zudilin] -- "A refinement of Nesterenko's linear independence criterion with applications to zeta values", *Math. Ann.* **347** (2010), p. 739--763.

[W. Fulton & J. Harris] -- *Representation theory: a first course*, Graduate Texts in Math., no. 129, Springer-Verlag, 1991.

[F. Gantmacher & M. Krein] -- *Oscillation matrices and kernels and small vibrations of mechanical systems*, Graduate Texts in Math., AMS Chelsea Publishing, Providence, RI, 2002.

[G. Hardy & E. Wright] -- *An introduction to the theory of numbers*, fifth ed., Oxford Science Publications, 1979.

[C. Krattenthaler] -- "Advanced determinant calculus", *Sém. Lotharingien Combin.* **42** (1999), Article B42q, 67 pp.

[C. Krattenthaler & W. Zudilin] -- " Hypergeometry inspired by irrationality questions", preprint arXiv:1802.08856 \[math.NT\], 2018.

[M. Laurent, M. Mignotte & Y. Nesterenko] -- "Formes linéaires en deux logarithmes et déterminants d'interpolation", *J. Number Th.* **55** (1995), p. 285--321.

[G. Macdonald] -- *Symmetric functions and Hall polynomials*, Oxford Univ. Press, 1979.

[M. H. Nash] -- "Special values of Hurwitz zeta functions and Dirichlet ${L}$-functions", Ph.D. thesis, Univ. of Georgia, Athens, U.S.A., 2004.

[Y. Nesterenko] -- "On the linear independence of numbers", *Vestnik Moskov. Univ. Ser. I Mat. Mekh. \[Moscow Univ. Math. Bull.\]* **40** (1985), no. 1, p. 46--49 \[69--74\].

[M. Nishimoto] -- "On the linear independence of the special values of a Dirichlet series with periodic coefficients", preprint arXiv:1102.3247 \[math.NT\], 2011.

[R. Proctor] -- "Equivalence of the combinatorial and the classical definitions of Schur functions", *J. Combinatorial Th., Series A* **51** (1989), p. 135--137.

[T. Rivoal] -- "La fonction zêta de Riemann prend une infinité de valeurs irrationnelles aux entiers impairs", *C. R. Acad. Sci. Paris, Ser. I* **331** (2000), no. 4, p. 267--270.

--- , "Irrationalité d'au moins un des neuf nombres $\zeta(5)$, $\zeta(7)$, ..., $\zeta(21)$", *Acta Arith.* **103** (2002), no. 2, p. 157--167.

[T. Rivoal & W. Zudilin] -- "Diophantine properties of numbers related to Catalan's constant", *Math. Annalen* **326** (2003), no. 4, p. 705--721.

--- , "A note on odd zeta values", preprint arXiv:1803.03160 \[math.NT\], 2018.

[J. Sprang] -- "Infinitely many odd zeta values are irrational. By elementary means", preprint arXiv:1802.09410 \[math.NT\], 2018.

[W. Zudilin] -- "One of the numbers $\zeta(5)$, $\zeta(7)$, $\zeta(9)$, $\zeta(11)$ is irrational", *Uspekhi Mat. Nauk \[Russian Math. Surveys\]* **56** (2001), no. 4, p. 149--150 \[774--776\].

--- , "Irrationality of values of the Riemann zeta function", *Izvestiya Ross. Akad. Nauk Ser. Mat. \[Izv. Math.\]* **66** (2002), no. 3, p. 49--102 \[489--542\].

--- , "One of the odd zeta values from $\zeta(5)$ to $\zeta(25)$ is irrational. By elementary means", *SIGMA* **14** (2018), no. 028, 8 pages.

Stéphane Fischler, Laboratoire de Mathématiques d'Orsay, Univ. Paris-Sud, CNRS, Université Paris-Saclay, 91405 Orsay, France

Johannes Sprang, Fakultät für Mathematik, Universität Regensburg, 93053 Regensburg, Germany

Wadim Zudilin, Department of Mathematics, IMAPP, Radboud University, PO Box 9010, 6500 GL Nijmegen, Netherlands;\
School of Mathematical and Physical Sciences, The University of Newcastle, Callaghan, NSW 2308, Australia
