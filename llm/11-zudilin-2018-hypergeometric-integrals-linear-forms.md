---
title: "Some hypergeometric integrals for linear forms in zeta values"
authors:
  - "Wadim Zudilin"
arxiv_id: "1804.04129v1"
arxiv_url: "https://arxiv.org/abs/1804.04129"
published: "2018-04-11"
journal_ref: "Bull. Austral. Math. Soc. 98:3 (2018) 372--375"
doi: "10.1017/S0004972718000503"
source: "papers/11-zudilin-2018-hypergeometric-integrals-linear-forms/hyperint03.tex"
conversion: pandoc-flat
---

# Some hypergeometric integrals for linear forms in zeta values

**Wadim Zudilin** — Bull. Austral. Math. Soc. 98:3 (2018) 372--375

## Abstract

We prove integral representations of the approximation forms in zeta values constructed in arXiv:1801.09895 and arXiv:1803.08905.

---
In the exposition below, $s$ and $D$ are positive integers such that $s\ge3D-1$, while the parameter $n$ is assumed to be a positive *even* integer. The notation $$\zeta(s,\alpha) = \sum_{n=0}^\infty \frac1{(n+\alpha)^s}$$ is used for the Hurwitz zeta function, so that $\zeta(s)=\zeta(s,1)$, and $d_n = \operatorname{lcm}(1,2,\dots,n)$.

In [@FSZ18] the following approximations are constructed: for any $j\in\{1,\dots,D\}$, take $$r_{n,j} = \sum_{m=1}^\infty R_n\bigg(m+\frac{j}{D}\bigg),
\qquad\text{where}\quad
R_n(t) = D^{3Dn} n!^{s+1-3D} \, \frac{ \prod_{l=0}^{3Dn} (t-n+l/D)}{ \prod_{l=0}^n (t+l)^{s+1}}.$$ It is shown that [^1] $$\label{forms}
r_{n,j}
=a_{0,j}+\sum_{\substack{2\le i \le s\\i\equiv s\;(\operatorname{mod}2)}}a_i\zeta\bigg(i,\frac{j}{D}\bigg),$$ with $$\begin{gathered}
d_n^{s+1-i}a_i\in\mathbb Z \qquad\text{for}\quad i = 2,3,4,\dots,s, \quad i\equiv s\;(\operatorname{mod}2),
\\
d_{n+1}^{s+1}a_{0,j}\in\mathbb Z \qquad\text{for}\quad j\in \{1,\dots,D\}
\end{gathered}$$ (see [@FSZ18 Lemmas 1 and 2]), and some further information is provided for the asymptotic growth of *positive* quantities $r_{n,j}$ as $n\to\infty$. The approximations are building blocks for linear forms in zeta values $\zeta(i)$ with $i$ of the same parity as $s$, with the help of elementary formula $$\sum_{j=1}^d\zeta\biggl(i,\frac{j\,(D/d)}{D}\biggr)=\sum_{j=1}^d\zeta\biggl(i,\frac jd\biggr)=d^i\zeta(i)$$ valid for any divisor $d$ of $D$.

The principal goal of this note is to establish the following integral representation of the approximations $r_{n,j}$ for $j\in\{1,\dots,D\}$.

**Theorem 1**. *The linear forms (forms) admit the integral representation $$r_{n,j}=\frac{D^{s-1}(3Dn+1)!}{n!^{3D}}\sum_{m=1}^D\xi^{-mj}r_{n,m}^*,$$ where $$r_{n,m}^*
=\xi^m\idotsint\limits_{[0,1]^{s+1}}
\frac{\prod_{i=0}^sx_i^{Dn}(1-x_i^D)^n\,{\mathrm d}x_i}{(1-\xi^mx_0\dotsb x_s)^{3Dn+2}}
=\int_0^{\xi^m}\!\!\idotsint\limits_{[0,1]^s}
\frac{\prod_{i=0}^sx_i^{Dn}(1-x_i^D)^n\,{\mathrm d}x_i}{(1-x_0\dotsb x_s)^{3Dn+2}}$$ and $\xi=\xi_D$ denotes a primitive root of unity of degree $D$.*

*Proof.* As the rational function $R_n(t)$ has zeros at $t=m-(D-j)/D$ for $m=1,\dots,n$ and $j\in\{1,\dots,D\}$, we can write $$\begin{aligned}
r_{n,j}
&= \sum_{m=n}^\infty R_n\bigg(m+\frac{j}{D}\bigg)
= D^{3Dn} n!^{s+1-3D}\sum_{k=0}^\infty
\frac{ \prod_{l=0}^{3Dn} (k+(l+j)/D)}{ \prod_{l=0}^n (k+n+l+j/D)^{s+1}}
\nonumber \displaybreak[2]\\
&=\frac{n!^{s+1-3D}\prod_{l=0}^{3Dn} (l+j)}{D\prod_{l=0}^n (n+l+j/D)^{s+1}}
\nonumber \\ &\quad\times
{}_{s+D+1}F_{s+D}\biggl(\begin{matrix} \{3n+\frac{j+l}D:l=1,\dots,D\}, \, \{n+\frac jD\}^{s+1} \\[2.5pt]
\{1+\frac{j-l}D:l=1,\dots,D,\,j\ne l\}, \, \{2n+1+\frac jD\}^{s+1} \end{matrix}\biggm|1\biggr)
\nonumber \displaybreak[2]\\
&=\frac{(3Dn+j)!}{D\,n!^{3D}(j-1)!}
\idotsint\limits_{[0,1]^{s+1}}f_j(t_0\dotsb t_s)
\prod_{i=0}^st_i^{n+j/D-1}(1-t_i)^n\,{\mathrm d}t_i,
\label{forms2}
\end{aligned}$$ where $$\begin{aligned}
f_j(t)
&={}_DF_{D-1}\biggl(\begin{matrix} \{3n+\frac{j+l}D:l=1,\dots,D\} \\
\{1+\frac{j-l}D:l=1,\dots,D,\,j\ne l\} \end{matrix} \biggm| t \biggr)
\\
&=\sum_{k=0}^\infty\frac{\prod_{l=1}^D(3n+\frac{j+l}D)_k}{\prod_{l=1}^D(1+\frac{j-l}D)_k}\,t^k
=\sum_{k=0}^\infty\frac{(3Dn+j+1)_{Dk}}{(j)_{Dk}}\,t^k
\qquad\text{for}\quad j\in\{1,\dots,D\}.
\end{aligned}$$ Using $$\sum_{l=0}^\infty\frac{(a)_l}{l!}\,x^l=\frac1{(1-x)^a}$$ observe that $$\begin{aligned}
\frac{(3Dn+2)_{j-1}}{(j-1)!}\,x^{j-1}f_j(x^D)
&=\sum_{k=0}^\infty\frac{(3Dn+2)_{Dk+j-1}}{(Dk+j-1)!}\,x^{Dk+j-1}
\\
&=\sum_{\substack{l=0\\l\equiv j-1\;(\operatorname{mod}D)}}^\infty\frac{(3Dn+2)_l}{l!}\,x^l
=\frac1D\sum_{m=1}^D\frac{\xi^{-m(j-1)}}{(1-\xi^mx)^{3Dn+2}}.
\end{aligned}$$ Taking $t_i=x_i^D$ for $i=0,1,\dots,s$ in the integrals (forms2) we thus obtain $$\begin{aligned}
r_{n,j}
&=\frac{D^{s-1}(3Dn+1)!}{n!^{3D}}
\sum_{m=1}^D\xi^{-m(j-1)}\idotsint\limits_{[0,1]^{s+1}}
\frac{\prod_{i=0}^sx_i^{Dn}(1-x_i^D)^n\,{\mathrm d}x_i}{(1-\xi^mx_0\dotsb x_s)^{3Dn+2}}
\end{aligned}$$ for each $j\in\{1,\dots,D\}$. ◻

Taking $D=2$ and $s\ge5$ odd, we obtain the linear forms $$\begin{aligned}
7r_{n,2}-r_{n,1}
&=\frac{2^s(6n+1)!}{n!^6}\idotsint\limits_{[0,1]^{s+1}}
\biggl(\frac3{(1-x_0x_1\dotsb x_s)^{6n+2}}
\\[-10.5pt] &\qquad\qquad\qquad\qquad\qquad\qquad
-\frac4{(1+x_0x_1\dotsb x_s)^{6n+2}}\biggr)
\prod_{i=0}^sx_i^{2n}(1-x_i^2)^n\,{\mathrm d}x_i
\\
&=\frac{2^s(6n+1)!}{n!^6}\idotsint\limits_{\gamma\times[0,1]^s}
\frac{\prod_{i=0}^sx_i^{2n}(1-x_i^2)^n\,{\mathrm d}x_i}{(1-x_0x_1\dotsb x_s)^{6n+2}}
\end{aligned}$$ in $\mathbb Q+\mathbb Q\zeta(5)+\dots+\mathbb Q\zeta(s)$ considered previously in [@Zu18]. Here the path $\gamma\subset\mathbb R$ for integrating with respect to $x_0$ is given by $\gamma=3[0,1]+4[0,-1]$, and the parity assumption on $n$ can be dropped.

## Acknowledgements {#acknowledgements .unnumbered}

The note was produced during the trimester on *Periods in Number Theory, Algebraic Geometry and Physics* at the Hausdorff Research Institute for Mathematics (Bonn, Germany). I thank Clément Dupont for his encouragement to write the integrals for the hypergeometric approximations used in [@FSZ18; @Zu18].

9

[S. Fischler], [J. Sprang] and [W. Zudilin], Many odd zeta values are irrational, *Preprint* `arXiv: 1803.08905 [math.NT]` (2018).

[W. Zudilin], One of the odd zeta values from $\zeta(5)$ to $\zeta(25)$ is irrational. By elementary means, *SIGMA* **14** (2018), no. 028, 8 pages; *Preprint* `arXiv: 1801.09895 [math.NT]` (2018).

[^1]: Choosing $n$ even implies $3Dn+1+(s+1)(n+1)\equiv s\;(\operatorname{mod}2)$, hence $R_n(-n-t)=(-1)^sR_n(t)$. This reflects on the parity in summation in (forms) --- consideration in [@FSZ18] is restricted to the case of $s$ odd.
