---
title: "Multiple zeta values, Padé approximation and Vasilyev's conjecture"
authors:
  - "Stephane Fischler"
  - "Tanguy Rivoal"
arxiv_id: "1309.2534v1"
arxiv_url: "https://arxiv.org/abs/1309.2534"
published: "2013-09-10"
journal_ref: ""
doi: ""
source: "papers/24-fischler-rivoal-2013-mzv-pade-vasilyev/padezetaimp13.tex"
conversion: pandoc-flat
---

# Multiple zeta values, Padé approximation and Vasilyev's conjecture

**Stephane Fischler, Tanguy Rivoal**

## Abstract

Sorokin gave in 1996 a new proof that pi is transcendental. It is based on a simultaneous Padé approximation problem involving certain multiple polylogarithms, which evaluated at the point 1 are multiple zeta values equal to powers of pi. In this paper we construct a Padé approximation problem of the same flavour, and prove that it has a unique solution up to proportionality. At the point 1, this provides a rational linear combination of 1 and multiple zeta values in an extended sense that turn out to be values of the Riemann zeta function at odd integers. As an application, we obtain a new proof of Vasilyev's conjecture for any odd weight, concerning the explicit evaluation of certain hypergeometric multiple integrals; it was first proved by Zudilin in 2003.

---
# Introduction

The goal of this paper is to provide a completely new proof of Vasilyev's conjecture for any odd weight $d\ge 3$ by solving a simultaneous Padé approximation problem involving multiple polylogarithms. Before explaining in details our approach, we provide some background. Vasilyev [@vasiliev] conjectured in 1996, that for any integers $d\ge 2$ and $n\ge 0$, $$\label{eq:intro1}
J_{d,n}:=\int_{[0,1]^d} \frac{\prod_{j=1}^d x_j^n(1-x_j)^n}{Q_d(x_1,  \ldots, x_d)^{n+1}} \textup{d}x_j \in \mathbb Q +
\mathbb Q \zeta(2+e_d) + \mathbb Q \zeta(4+e_d) + \cdots +  \mathbb Q \zeta(d)$$ where $e_d=0$ if $d$ is even, $e_d=1$ otherwise, and $Q_1(x_1):=1-x_1$, $$\begin{aligned}
Q_d(x_1, \ldots, x_d):&=1-Q_{d-1}(x_1, \ldots, x_{d-1})x_d, \quad d\ge 2
\\                   &=1-(1-(\cdots 1-(1-x_1)x_2\cdots )x_{d-1})x_d.
\end{aligned}$$ This conjecture was already known to be true for $d=2$ and $d=3$, since Beukers [@beukers] used these integrals to get new and quick versions of Apéry's proofs [@Apery] of the irrationality of $\zeta(2)$ and $\zeta(3)$. Vasilyev himself proved his conjecture in the cases $d=4$ and $d=5$, results which in fact led him to the conjecture. The first complete proof was given by Zudilin [@zudilin] who showed that $J_{d,n}$ is equal to a very-well-poised hypergeometric series whose value was already known to be in $\mathbb Q + \mathbb Q \zeta(2+e_d) + \mathbb Q \zeta(4+e_d) + \cdots
+  \mathbb Q \zeta(d)$. Two other proofs of Vasilyev's conjecture were subsequently found, one by Zlobin [@zlobin] (direct attack) and another indirect one by Krattenthaler-Rivoal [@kratriv] (limiting case of Andrews' hypergeometric identity, in the spirit of Zudilin). The fourth one, given in the present paper, is completely different since it relies on solving a simultaneous Padé approximation problem involving multiple polylogarithms.

To state this problem we need some notations. Given any finite word $\sigma$ built on a (possibly infinite) alphabet $\{a,b, \ldots\}$, we denote by $\{\sigma\}_j:=\sigma\sigma\cdots \sigma$ the concatenation $j$ times of $\sigma$. By convention, $\{\sigma\}_0=\emptyset$. We will use two alphabets, namely $\mathbb N^{*} = \{1,2,\ldots\}$ and $\{\ell,s\}$. We consider multiple polylogarithms in the following extended sense: $$\label{eq:intro4}
\operatorname{Li}_{b_1b_2\cdots b_p}^{a_1a_2\cdots a_{p-1}}(z):=
\sum_{k_1\gtrsim k_2\gtrsim \cdots \gtrsim k_p\ge 1} \frac{z^{k_1}}{k_1^{b_1}k_2^{b_2}\cdots k_p^{b_p}}$$ where $\vert z\vert <1$, $b_j\in \mathbb N^{*}$ and $a_j\in\{\ell,s\}$ for all $j$. For $j=1, \ldots, p-1$, the symbol $\gtrsim\;\in \{>, \ge \}$ in $k_j\gtrsim k_{j+1}$ is determined by the following rule: it is set to $>$ if $a_j=s$, and to $\ge$ if $a_j=\ell$. In this way, $s$ stands for a *strict* inequality, and $\ell$ for a *large* one. If $a_j = s$ for any $j$ we obtain the usual multiple polylogarithm $\operatorname{Li}_{b_1b_2\cdots b_p} (z)$; if $a_j = \ell$ for any $j$ we obtain the variant denoted by $\operatorname{La}_{b_1b_2\cdots b_p} (z)$ in [@crefiri] and by $\operatorname{Le}_{b_1b_2\cdots b_p} (z)$ by Ulanskiı̆ and Zlobin. Sorokin used in [@sorokin1] the functions $\operatorname{Li}_{\{1\}_{2r+1}}^{\{s\ell\}_{r}}(1-x)$ and $\operatorname{Li}_{\{1\}_{2r}}^{\{ \ell s\}_{r-1} \ell}(1-x)$, which he denoted respectively by $\varepsilon_r(x)$ and $\varphi_r(x)$. In this paper, all multiple polylogarithms $\operatorname{Li}_{b_1b_2\cdots b_p}^{a_1a_2\cdots a_{p-1}}(z)$ will be considered for $z\in\mathbb{C}\setminus [1,\infty)$ using analytic continuation. As usual, the integer $p$ in (eq:intro4) is called the *depth*, and $b_1+\cdots+b_p$ is the *weight*.

Our main result is the explicit resolution of the following simultaneous Padé approximation problem. Given integers $n,r\ge 0$, we want to find polynomials $A_{\rho,r,n}(z)$, $B_{\rho,r,n}(z)$, $C_{\rho,r,n}(z)$, $D_{r,n}(z) \in \mathbb C[z]$, for $0\leq \rho \leq r$, all of degree at most $n$, such that $$\begin{aligned}
S_{r,n}(z):=&\sum_{\rho=0}^r \bigg[A_{\rho,r,n}(z) \operatorname{Li}_{2\{1\}_{2\rho+1}}^{\{\ell s\}_\rho\ell}\Big(\frac1z\Big)
+B_{\rho,r,n}(z) \operatorname{Li}_{\{1\}_{2\rho+2}}^{\{\ell s\}_\rho\ell}\Big(\frac1z\Big)
\\
&\hspace{2cm} +C_{\rho,r,n}(z) \operatorname{Li}_{\{1\}_{2\rho+1}}^{\{s\ell\}_\rho}\Big(\frac1z\Big)\bigg]+D_{r,n}(z)
= \mathcal{O}\Big(\frac1{z^{(r+1)(n+1)}}\Big)
\\
U_{j,r,n}(z):=&\sum_{\rho=j}^r A_{\rho,r,n}(z) \operatorname{Li}_{1\{2\}_{r-\rho}}^{\{\ell\}_{r-\rho}}(1-z)
+ B_{j,r,n}(z) = \mathcal{O}\big((1-z)^{n+1}\big),
\quad j=0, \ldots, r
\\
V_{j,r,n}(z):=&\sum_{\rho=j}^r A_{\rho,r,n}(z) \operatorname{Li}_{\{2\}_{r-\rho+1}}^{\{\ell\}_{r-\rho}}(1-z)
+ C_{j,r,n}(z) = \mathcal{O}\big((1-z)^{n+1}\big), \quad j=0, \ldots, r.
\end{aligned}$$ We will denote by $\mathcal{P}_{r,n}$ this Padé approximation problem. The various symbols $\mathcal{O}$ have the following meaning. The function $S_{r,n}(z)$ is obviously analytic at $z=\infty$ and we ask its order there to be at least $(r+1)(n+1)$. Similarly, the functions $U_{j,r,n}(z)$ and $V_{j,r,n}(z)$ are analytic at $z=1$ and we ask their orders there to be at least $n+1$. This is a mixed Padé approximation problem, namely in between type $I$ problems and type $II$ problems. Similar mixed Padé approximation problems often occur in the Diophantine theory of (multiple) zeta values; see for instance [@firi; @sorokin2; @sorokin1].

The problem $\mathcal{P}_{r,n}$ can be trivially converted into a linear algebra problem: it amounts to solving a system of $(3r+4)(n+1)-1$ linear equations in $(3r+4)(n+1)$ unknowns (the coefficients of the polynomials). Hence, there is at least one non identically zero solution. Our main theorem shows that the solution is unique up to a multiplicative constant.

**Theorem 1**. *For any integers $n,r\ge 0$, the function $S_{r,n}(z)$ in $\mathcal{P}_{r,n}$ is given by the following hypergeometric integral (up to a multiplicative constant), which converges for any $z\in \mathbb C\setminus[0,1)$: $$\begin{gathered}
\label{eq:intro6}
S_{r,n}(z)=(-1)^{n+1}z^{(r+1)(n+1)}
\\
\times \int_{[0,1]^{2r+3}}
\frac{\displaystyle u_0^{(r+1)(n+1)-1}(1-u_0)^n
\prod_{j=1}^{r+1}\big((u_jv_j)^{(r-j+2)(n+1)-1}(1-u_j)^n(1-v_j)^n\big)}
{\displaystyle \prod_{j=1}^{r+1}\big((z-u_0u_1v_1\cdots u_{j-1}v_{j-1}u_j)^{n+1}
(z-u_0u_1v_1\cdots u_{j}v_{j})^{n+1}\big)} \textup{d}{\bf u}\textup{d}{\bf v}.
\end{gathered}$$*

For $r=0$, the problem $\mathcal{P}_{0,n}$ and the integral for $S_{0,n}(z)$ exactly match those considered by Sorokin in [@sorokin2], from which he deduced a new proof of Apéry's theorem. However, our derivation of the integral for $S_{0,n}(z)$ is different from Sorokin's.

For any $r\geq 0$, the integral representation (eq:intro6) provides a new proof of Vasilyev's conjecture, by taking $z=1$ (see §  2 for details). It would be very interesting to obtain a new proof of the infiniteness of irrational values among the $\zeta(2r+1)$ (see [@BR; @rivoal]) by solving a Sorokin-type Padé problem involving multiple polylogarithms as in Theorem 1, as Sorokin did [@sorokin2] for Apéry's theorem (see §  6 at the end of the paper).

Theorem 1 is based on Sorokin's proof [@sorokin1] of the transcendence of $\pi$, which relies on the resolution of a simultaneous Padé approximation problem involving certain multiple polylogarithms (see § 5.3 for details), as well as on the identity $\operatorname{Li}_{\{2\}_{r}}^{\{s\}_{r-1}}(1)=\frac{\pi^{2r}}{(2r+1)!}$ for any integer $r\ge 1$.

The integral for $S_{r,n}(z)$ can be used to get explicit expression of the polynomials, all of which obviously have rational coefficients. This can be done by various means, for instance one can convert the integral into the series $$\begin{gathered}
S_{r,n}(z)=
\\n!\!\!\sum_{k_0\ge \cdots \ge k_{2r+1}\ge 1} \frac{(k_0-k_1+1)_n(k_1-k_2+1)_n\cdots
(k_{2r}-k_{2r+1}+1)_n(k_{2r+1}-n)_n}{\displaystyle \prod_{j=0}^r
\big((k_{2j}+(r-j+1)(n+1))_{n+1}^{e_j}(k_{2j+1}+(r-j)(n+1))_{n+1}\big)} \frac1{z^{k_0+r(n+1)}}
\end{gathered}$$ (where $e_0=2$ and $e_j=1$ for $j\ge 1$) and then use the algorithm described in [@crefiri].

The paper is organised as follows. In § 2, we deduce Vasilyev's conjecture for odd values of $d$ from Theorem 1. In § 3, we present a few tools needed for the proof of Theorem 1, in particular an iterative construction of hypergeometric multiple integrals. In § 4, we prove an important representation formula for multiple polylogarithms and derive a few consequences useful in the resolution of $\mathcal{P}_{r,n}$. Section 5, devoted to the proof of Theorem 1, is decomposed in many steps. The first two steps show how to reduce the problem $\mathcal{P}_{r,n}$ to Sorokin's problem for $\pi^2$ (recalled in § 5.3) and the subsequent steps complete the proof. At last we construct in § 6 a family of integrals, containing (eq:intro6), which enable one to prove that infinitely many odd zeta values $\zeta(2r+1)$ are irrational [@BR; @rivoal].

# New proof of Vasilyev's conjecture for odd weights

To deduce Vasilyev's conjecture from Theorem 1, we first define (when $b_1\geq 2$) extended multiple zeta values by $$\label{eq15bis}
\zeta_{b_1b_2\cdots b_p}^{a_1a_2\cdots a_{p-1}}:=\operatorname{Li}_{b_1b_2\cdots b_p}^{a_1a_2\cdots a_{p-1}}(1) =
\sum_{k_1\gtrsim k_2\gtrsim \cdots \gtrsim k_p\ge 1} \frac{1}{k_1^{b_1}k_2^{b_2}\cdots k_p^{b_p}}$$ with the same definition for the symbols $\gtrsim$ as in Eq. (eq:intro4). In particular, when $a_j=s$ for all $j$, we have the usual multiple zeta values $\zeta_{b_1b_2\cdots b_p}^{ \{s\}_{p-1}}=\zeta(b_1,b_2,\ldots, b_p)$.

Then we remark that the Padé conditions for the functions $U_{j,r,n}(z)$ and $V_{j,r,n}(z)$ in $\mathcal{P}_{r,n}$ ensure that all polynomials $B_{j,r,n}(z)$ and $C_{j,r,n}(z)$ vanish at $z=1$ ($j=0, \ldots, r$). Since multiple polylogarithms have (at most) a logarithmic singularity at $z=1$, this implies that when we take the limit $z\to 1$ in (eq:intro6), we get $$\begin{aligned}
(-1)^{n+1} \int_{[0,1]^{2r+3}} &
\frac{\displaystyle u_0^{(r+1)(n+1)-1}(1-u_0)^n \prod_{j=1}^{r+1}\big((u_jv_j)^{(r-j+2)(n+1)-1}(1-u_j)^n(1-v_j)^n\big)}
{\displaystyle \prod_{j=1}^{r+1}\big((1-u_0u_1v_1\cdots u_{j-1}v_{j-1}u_j)^{n+1}(1-u_0u_1v_1\cdots u_{j}v_{j})^{n+1}\big)}
\textup{d}{\bf u}\textup{d}{\bf v}
\\
&=\sum_{\rho=0}^r A_{\rho,r,n}(1) \zeta_{2\{1\}_{2\rho+1}}^{\{\ell s\}_\rho\ell}
+D_{r,n}(1)
\end{aligned}$$ where $A_{\rho,r,n}(1)$ and $D_{r,n}(1)$ are rational numbers. Moreover, it is proved in [@fischler2 Corollaire 8] that this multiple integral is equal to $J_{2r+3,n}$ for any integer $r\ge 0$ (see also §  6 below). To complete the proof of Vasilyev's conjecture in this case, we simply need the following result, which plays the same role for us as the identity $\operatorname{Li}_{\{2\}_{r}}^{\{s\}_{r-1}}(1)=\frac{\pi^{2r}}{(2r+1)!}$ for Sorokin in [@sorokin1].

**Proposition 1**. *For any integer $k\ge 1$, we have $$\label{eq:intro7}
\zeta_{2\{1\}_{2k-1}}^{\{\ell s\}_{k-1}\ell}=\zeta_{\{2\}_k 1}^{\{\ell\}_{k}} = 2\zeta(2k+1).$$*

*Proof.* The second equality in (eq:intro7) is due to Zlobin [@zlobin2]. To prove the first equality, which we haven't found in the literature, we use the representation of (extended) multiple zeta values as Chen iterated integrals. Indeed, we have $$\begin{aligned}
&\zeta_{2\{1\}_{2k-1}}^{\{\ell s\}_{k-1}\ell}
\\ &\quad=
 \int\limits_{\{0\le x_{2k+1}\le \cdots \le x_1\le 1\}}
\frac{\textup{d}{\bf x}}{x_1x_2(1-x_2)(1-x_3)x_4(1-x_4)(1-x_5)\cdots x_{2k}(1-x_{2k})(1-x_{2k+1})}
\\
&\quad= \int\limits_{\{0\le y_{2k+1}\le \cdots \le y_1\le 1\}}
\frac{\textup{d}{\bf y}}{y_1y_2(1-y_2)y_3y_4(1-y_4)y_5\cdots y_{2k}(1-y_{2k})(1-y_{2k+1})}
=\zeta_{\{2\}_k 1}^{\{\ell\}_{k}},
\end{aligned}$$ where we have made the change of variables $x_j=1-y_{2k+2-j}$, $j=1, \ldots, 2k+1$. ◻

# General results on multiple polylogarithms

We gather in this section various results, useful in the proof of Theorem 1 but which may also be of independent interest.

## Differentiation rules for multiple polylogarithms

In this section, we describe how to differentiate a multiple polylogarithm. To begin with, we state formulas of which the proofs are straightforward; we will use them without further mentions. The letter ${\bf a}$ denotes a finite word built on the alphabet $\{\ell,s\}$, the letter ${\bf b}$ a finite word built on the alphabet $\mathbb{N}^{*}$, and $t$ any integer $\ge 2$.

$$\begin{aligned}
\frac{\textup{d}}{\textup{d}z}& \operatorname{Li}_1(z)= \frac{1}{1-z}, \hspace{3.4cm} \frac{\textup{d}}{\textup{d}z}
\Big[ \operatorname{Li}_1\Big(\frac1z\Big) \Big]= \frac{1}{z(1-z)},
\\
\frac{\textup{d}}{\textup{d}z}& \operatorname{Li}_{1{\bf b}}^{\ell{\bf a}}(z)=\frac{1}{z(1-z)}
\operatorname{Li}_{{\bf b}}^{{\bf a}}(z), \hspace{1.5cm}
\frac{\textup{d}}{\textup{d}z}\Big[  \operatorname{Li}_{1{\bf b}}^{\ell{\bf a}}\Big(\frac1z\Big) \Big]=\frac{1}{1-z}
\operatorname{Li}_{{\bf b}}^{{\bf a}}\Big(\frac1z\Big),
\\
\frac{\textup{d}}{\textup{d}z}& \operatorname{Li}_{t{\bf b}}^{\ell{\bf a}}(z)=\frac{1}{z}
\operatorname{Li}_{(t-1){\bf b}}^{\ell{\bf a}}(z), \hspace{2.1cm}
\frac{\textup{d}}{\textup{d}z}\Big[  \operatorname{Li}_{t{\bf b}}^{\ell{\bf a}}\Big(\frac1z\Big) \Big]=-
\frac{1}{z} \operatorname{Li}_{(t-1){\bf b}}^{\ell{\bf a}}\Big(\frac1z\Big),
\\
\frac{\textup{d}}{\textup{d}z}& \operatorname{Li}_{1{\bf b}}^{s{\bf a}}(z)=\frac{1}{1-z}
\operatorname{Li}_{{\bf b}}^{{\bf a}}(z), \hspace{2.1cm}
\frac{\textup{d}}{\textup{d}z}\Big[ \operatorname{Li}_{1{\bf b}}^{s{\bf a}}\Big(\frac1z\Big) \Big]=\frac{1}{z(1-z)}
\operatorname{Li}_{{\bf b}}^{{\bf a}}\Big(\frac1z\Big),
\\
\frac{\textup{d}}{\textup{d}z}& \operatorname{Li}_{t{\bf b}}^{s{\bf a}}(z)=\frac{1}{z}
\operatorname{Li}_{(t-1){\bf b}}^{s{\bf a}}(z), \hspace{2.1cm}
\frac{\textup{d}}{\textup{d}z}\Big[  \operatorname{Li}_{t{\bf b}}^{s{\bf a}}\Big(\frac1z\Big) \Big]=-
\frac{1}{z} \operatorname{Li}_{(t-1){\bf b}}^{s{\bf a}}\Big(\frac1z\Big).
\end{aligned}$$

We now state a general lemma, whose proof can be done by induction using the formulas above.

**Lemma 1**. *Let $d,n\geq 0$, and $A(z)\in \mathbb C[z]$ be a polynomial of degree $\le d$. Then we have $$\frac{\textup{d}^{n+1}}{\textup{d}z^{n+1}} \big(A(z) \operatorname{Li}_{ b_1b_2\cdots b_p}^{  a_1a_2\cdots a_{p-1}}(z)\big)
= \sum_{i=0}^{p+1} \sum_{b'=1}^{b_i}  \frac{\widehat{A}_{i,b'} (z)}{z^{n+1}(1-z)^{n+1}}
\operatorname{Li}_{b' b_{i+1}b_{i+2}\cdots b_p}^{  a_ia_{i+1}\cdots a_{p-1}}(z)$$ for some polynomials $\widehat{A}_{i,b'} (z)$ of degree $\leq d+n+1$; here we let $b_{p+1}=1$ so that in the sum there is one term corresponding to $i=p+1$, and the associated polylogarithm is equal to 1.*

It is not difficult to see that in this lemma, each polynomial $\widehat{A}_{i,b'} (z)$ depends only on $b_1$, ..., $b_{i-1}$, $a_1$, ..., $a_{i-1}$, and $b_i-b'$. However we won't use this remark in the present paper.

Using the above relations in the same way, an analogous lemma yields polynomials $\widehat{A}'_{i,b'} (z)$ of degree $\leq d+n+1$ such that $$\frac{\textup{d}^{n+1}}{\textup{d}z^{n+1}} \big(A(z) \operatorname{Li}_{ b_1b_2\cdots b_p}^{  a_1a_2\cdots a_{p-1}}(1/z)\big)
= \sum_{i=0}^{p+1} \sum_{b'=1}^{b_i}  \frac{\widehat{A}'_{i,b'} (z)}{z^{n+1}(1-z)^{n+1}}
\operatorname{Li}_{b' b_{i+1}b_{i+2}\cdots b_p}^{  a_ia_{i+1}\cdots a_{p-1}}(1/z).$$

To take advantage of vanishing conditions like the ones on $U_{j,r,n}(z)$ and $V_{j,r,n}(z)$ in the Padé problem $\mathcal{P}_{r,n}$, the following lemma is very useful.

**Lemma 2**. *Let $n' \geq 0$, and $g(z)$ be a function holomorphic at $z=1$, such that $g(z) = \mathcal{O}\big((z-1)^{n+1}\big)$ as $z\to 1$. Then we have $$\frac{\textup{d}^{n+1}}{\textup{d}z^{n+1}} \big(g(z) \operatorname{Li}_{ b_1b_2\cdots b_p}^{  a_1a_2\cdots a_{p-1}}(z)\big)
= \sum_{i=0}^{p+1} \sum_{b'=1}^{b_i} h_{i,b'}(z)
\operatorname{Li}_{b' b_{i+1}b_{i+2}\cdots b_p}^{  a_ia_{i+1}\cdots a_{p-1}}(z)$$ for some functions $h_{i,b'} (z)$ holomorphic at $z=1$. As in Lemma 1, we let $b_{p+1}=1$ so that in the sum there is one term corresponding to $i=p+1$, and the associated polylogarithm is equal to 1.*

In other words, no pole appears at $z=1$ if $g$ vanishes to order at least $n+1$ at this point (since polylogarithms have at most a logarithmic divergence at 1).

## An integral operator

Sorokin solved several Padé approximation problems involving multiple polylogarithms (see [@sorokin2] and [@sorokin1], amongst other papers), which always led to hypergeometric multiple integrals. We define now an integral operator intimately related to his approach (and therefore also to Theorem 1).

Given integers $a,b,n\geq 0$ and a function $F(z)$, we let $$\label{eq:12}
{\bf H}_{a,b}^{n+1}(F)(z) = (-1)^{n+1}z^{n+1-a } \int_0^{1} \frac{u^{a+b-n-2}(1-u)^n}{(u-z)^b}F\Big(\frac zu\Big) \textup{d}u .$$ The assumptions on $F$ and the properties of the function ${\bf H}_{a,b}^{n+1}(F)$ defined in this way are detailed in the following lemma.

**Lemma 3**. *Let $F(z)$ be holomorphic on $\mathbb{C}\setminus[0,1]$ and at $z=\infty$; denote by $\omega\geq 0$ its order of vanishing at $\infty$. Given $a,b,n\geq 0$, let $\omega' = \omega + a+b-n-1$ and assume that $\omega' \geq 1$.*

*Then ${\bf H}_{a,b}^{n+1}(F)$ is holomorphic on $\mathbb{C}\setminus[0,1]$ and at $z=\infty$; its order of vanishing at $\infty$ is exactly $\omega'$. Moreover,*

-   *Letting $R   = {\bf H}_{a,b}^{n+1}(F)$, we have $$\label{eqlem7}
    F(z)= \frac{1}{n!}z^a(1-z)^b R^{(n+1)}(z) .$$*

-   *If $R(z)$ is a function holomorphic on $\mathbb{C}\setminus[0,1]$ and at $z=\infty$ such that $R(\infty)=0$ and Eq. (eqlem7) holds, then $R= {\bf H}_{a,b}^{n+1}(F)$.*

We shall apply this lemma in two cases: either $F(\infty) = 0$ and $a+b \geq n+1$, or $F$ is the constant function $F(z)=1$ and $a+b\geq n+2$. In both cases we have $\omega'\geq 1$, so that ${\bf H}_{a,b}^{n+1}(F)$ is holomorphic on $\mathbb{C}\setminus[0,1]$ and at $z=\infty$, and ${\bf H}_{a,b}^{n+1}(F)(\infty) = 0$.

*Proof.* Let $G(z) = z^\omega F(z)$; then $G(z)$ is holomorphic on $\mathbb{C}\setminus [0,1]$ and at $\infty$, with $G(\infty)\neq 0$. By definition of $\omega'$ we have $${\bf H}_{a,b}^{n+1}(F)(z) = (-1)^{n+1}z^{-\omega' } \int_0^{1} \frac{u^{\omega'-1}(1-u)^n}{(\frac{u}{z}-1)^b}
G\Big(\frac zu\Big) \textup{d}u .$$ Since $\omega'\geq 1$ and $u/z \neq 1$ for any $u\in [0,1]$ (since $z\in\mathbb{C}\setminus[0,1]$), this formula shows that ${\bf H}_{a,b}^{n+1}(F)$ is holomorphic on $\mathbb{C}\setminus[0,1]$ and at $z=\infty$. It has order equal to $\omega'$ at $\infty$ because $G(\infty)\neq 0$.

To prove $(i)$ and $(ii)$, we perform the change of variable $x = z/u$ and deduce $${\bf H}_{a,b}^{n+1}(F)(z) =(-1)^{n+1} \int_z^{\infty} \frac{(x-z)^n}{x^a(1-x)^b}F(x) \textup{d}x .$$ Then assertions $(i)$ and $(ii)$ follow immediately from the following lemma, obtained from the arguments given in [@sh p. 60]. ◻

**Lemma 4**. *Let $R, S$ be functions analytic on a neighborhood of $\infty$, with $R(\infty)=0$. Then: $$\frac{1}{n!}R^{(n+1)}(z)=S(z) \Longleftrightarrow R(z)=(-1)^{n+1}\int_z^{\infty} (x-z)^{n}S(x) \textup{d}x.$$*

For Diophantine applications the value ${\bf H}_{a,b}^{n+1}(F)(1)$ is often the most interesting one; conditions for this value to exist are given by the following lemma, whose proof is straightforward.

**Lemma 5**. *Assume that $b\leq n+1$ and $F(z)$ has (at most) a power of logarithm divergence as $z\to 1$, with $z\in\mathbb{C}\setminus[0,1]$. Then ${\bf H}_{a,b}^{n+1}(F)(z)$ has also (at most) a power of logarithm divergence as $z\to 1$, with $z\in\mathbb{C}\setminus[0,1]$.*

*Moreover, if in addition $b\leq n$ then ${\bf H}_{a,b}^{n+1}(F)(z)$ has a finite limit as $z\to 1$, with $z\in\mathbb{C}\setminus[0,1]$, and this limit is given by taking $z=1$ in the integral representation of Eq. (eq:12), which is then convergent.*

In Padé approximation problems with multiple polylogarithms, multiple integrals appear by applying successively integral operators ${\bf H}_{a,b}^{n+1}$ with various parameters. We shall write ${\bf H}^{n+1}_{a,b} {\bf H}^{n'+1}_{a',b'}$ for ${\bf H}^{n+1}_{a,b}  \circ {\bf H}^{n'+1}_{a',b'}$, so that ${\bf H}^{n+1}_{a,b} {\bf H}^{n'+1}_{a',b'} (F) = {\bf H}^{n+1}_{a,b} ( {\bf H}^{n'+1}_{a',b'} (F) )$. We shall consider in § §  5.4 and 5.5 multiple integrals of the form $${\bf H}^{n_1+1}_{a_1,b_1} {\bf H}^{n_2+1}_{a_2,b_2} \cdots {\bf H}^{n_p+1}_{a_p,b_p} (\boldsymbol{1}),$$ where the $a_j, b_j, n_j$ are non-negative integers and $\boldsymbol{1}$ denotes the function equal to $1$ on $\mathbb{C}\setminus[0,1]$; such integrals appear in Sorokin's papers (e.g., [@sorokin2] and [@sorokin1]). Lemma 3 gives conditions on the parameters that ensure that this integral expression is holomorphic on $\mathbb{C}\setminus[0,1]$ and at $z=\infty$, and Lemma 5 plays the analogous role for the behaviour at $z=1$.

In the proof of Theorem 1 we shall use the following result which describes the behaviour of this integral operator under the change of variable $z\mapsto 1-z$.

**Lemma 6**. *For any integers $a_j, b_j, n_j$, $j=1, \ldots, p$ such that ${\bf H}^{n_1+1}_{a_1,b_1} {\bf H}^{n_2+1}_{a_2,b_2} \cdots {\bf H}^{n_p+1}_{a_p,b_p}(\boldsymbol{1})$ is holomorphic on $\mathbb{C}\setminus [0,1]$ and at $\infty$, we have $${\bf H}^{n_1+1}_{a_1,b_1} {\bf H}^{n_2+1}_{a_2,b_2} \cdots {\bf H}^{n_p+1}_{a_p,b_p}(\boldsymbol{1})(1-z) = (-1)^{p+n_1+n_2+\cdots+n_p }
{\bf H}^{n_1+1}_{b_1,a_1} {\bf H}^{n_2+1}_{b_2,a_2} \cdots {\bf H}^{n_p+1}_{b_p,a_p}(\boldsymbol{1})(z)$$ for all $z\in \mathbb{C}\setminus [0,1]$.*

*Proof.* This is a consequence of the following fact. Given $f(z)$, we set $f^{\partial}(z):=f(1-z)$. Then $$R(z)={\bf H}^{n+1}_{a,b} (S)(z) \Longleftrightarrow R^{\partial}(z)=(-1)^{n+1}{\bf H}^{n+1}_{b,a} (S^{\partial})(z).$$ This equivalence results from Lemma 3: $$S(z)=\frac{1}{n!}z^{a}(1-z)^{b}  R^{(n+1)} (z)
\Longleftrightarrow
S(1-z)=\frac{(-1)^{n+1}}{n!}z^{b}(1-z)^{a}\big(  R(1-z)\big)^{(n+1)}.$$ ◻

## Functional linear independence of polylogarithms

The extended multiple polylogarithms introduced in the introduction are very useful to state and prove our result, but they are not really *new* functions: they are linear combinations over $\mathbb{Z}$ of usual multiple polylogarithms (corresponding to $\alpha_1
= \ldots = \alpha_{p-1} =  s$ in (eq:intro4)). This follows from the following elementary relation (which is the starting point of [@crefiri]): $$\label{eqdeplin}
\operatorname{Li}_{b_1b_2\cdots b_p}^{a_1 \cdots a_{j-1} \ell a_{j+1} \cdots  a_{p-1}}(z) =
 \operatorname{Li}_{b_1b_2\cdots b_p}^{a_1 \cdots a_{j-1} s a_{j+1} \cdots  a_{p-1}}(z)
+  \operatorname{Li}_{b_1 \cdots b_{j-1} b' b_{j+2} \cdots  b_p}^{a_1 \cdots a_{j-1}   a_{j+1} \cdots  a_{p-1}}(z)$$ where $b' = b_j + b_{j+1}$.

In the proof of Theorem 1 we shall use the following result.

**Lemma 7**. *For any $k$, let ${\bf a}_k$ be a word on the alphabet $\{\ell,s\}$ of length $k-1$, with ${\bf a}_1 = {\bf a}_0 = \emptyset$. Then the polylogarithms $\operatorname{Li}_{\{1\}_k}^{ {\bf a}_k}(1/z)$, for $k\geq 0$, are linearly independent over the field $\mathcal{M}_0$ of functions meromorphic at 1.*

*Proof.* To begin with, let us consider for any $p\geq 0$ the set ${\mathcal F}_p$ of all functions analytic on $\mathbb{C}\setminus [0,1]$ that can be written as $\sum_{i=0}^p h_i(z) (\log(1-\frac1z))^i$ where $h_0(z)$, ..., $h_p(z)$ are functions holomorphic on $\mathbb{C}\setminus [0,1]$ and at $z=1$. Of course all functions holomorphic on $\mathbb{C}\setminus [0,1]$ and at $z=1$ belong to ${\mathcal F}_0$, and $\operatorname{Li}_1(1/z) = - \log(1-\frac1z)$ belongs to ${\mathcal F}_1$. We claim that for any $p\geq 0$, for any $\alpha_1,\ldots,\alpha_{p-1} \in\{\ell,s\}$ and any $b_1,\ldots,b_p\geq 1$, we have $$\operatorname{Li}_{b_1b_2\cdots b_p}^{a_1 \cdots a_{p-1}}(1/z) \in{\mathcal F}_p.$$ Let us prove this claim by induction on the weight $b_1+\cdots+b_p$. We have already noticed that it holds if $b_1+\cdots+b_p \leq 1$. Now remark that if $f$ is analytic on $\mathbb{C}\setminus [0,1]$ and $g\in {\mathcal F}_{p}$ are such that $f'(z) = \frac{-1}z g(z)$ then $f\in{\mathcal F}_p$, because ${\mathcal F}_p$ is stable under primitivation and products with functions holomorphic at 1. On the other hand, if $f'(z) = \frac{1}{1-z} g(z)$ or $f'(z) = \frac{1}{z(1-z)} g(z)$ then $f\in{\mathcal F}_{p+1}$. Using the differentiation rules for polylogarithms stated at the beginning of §  3.1, this proves the claim.

Now assume that for some $k\geq 1$ the function $\operatorname{Li}_{\{1\}_k}^{ {\bf a}_k}(1/z)$ is a linear combination over $\mathcal{M}_0$ of the $\operatorname{Li}_{\{1\}_j}^{ {\bf a}_j}(1/z)$ for $0\leq j \leq k-1$. Using the claim this implies $\operatorname{Li}_{\{1\}_k}^{ {\bf a}_k}(1/z) \in {\mathcal F}_{k-1}$. Now applying Eq. (eqdeplin) as many times as needed one can write $\operatorname{Li}_{\{1\}_k}^{ {\bf a}_k}(1/z)-\operatorname{Li}_{\{1\}_k}^{ \{s\}_{k-1}}(1/z)$ as a $\mathbb{Z}$-linear combination of extended multiple polylogarithms of depth $k-1$; applying the claim again proves that $\operatorname{Li}_{\{1\}_k}^{ \{s\}_{k-1}}(1/z) = (-1)^{k} \big( \log(1-\frac1z)\big)^k$ belongs to ${\mathcal F}_{k-1}$ (this identity belongs to the folklore and is readily proved by induction and differentiation). But this provides a non-trivial linear relation, with coefficients holomorphic at 1, between powers of the function $\log(1-\frac1z)$. This is impossible since $\log(z)$ is transcendental over the field of functions meromorphic at the origin. This contradiction concludes the proof of Lemma 7. ◻

# Weight functions of multiple polylogarithms

In this section we study the weight functions of multiple polylogarithms and compute some of them. This part is at the heart of the proof of Theorem 1, since *weights obey the same derivation rules as the corresponding polylogarithms* (see below).

If ${\bf b}=\emptyset$, $\operatorname{Li}_{\emptyset}^{\boldsymbol{a}}(z)=1/(1-z)$ and none of the considerations below apply. From now on, we consider non-empty words ${\bf b}$. It is well-known that usual multiple polylogarithms $\operatorname{Li}_{{\bf b}}^{\boldsymbol{a}}(z)$ (with $\boldsymbol{a}=ss\cdots s$) can be analytically continued to the cut plane $\mathbb C \setminus [1,+\infty)$. They vanish at $z=0$ and their growth as $z\to \infty$ is at most a power of $\log(z)$, with $0< \arg(z)< 2\pi$. Moreover, the function defined on the cut by $$\lim_{y\to 0+}
\left[\operatorname{Li}_{{\bf b}}^{ss\cdots s}\left(x+iy\right)-
\operatorname{Li}_{{\bf b}}^{ss\cdots s}\left(x-iy\right)\right]$$ is $C^{\infty}$ on $(1,+\infty)$ with at most a (power of) logarithm singularity at $x=1$ and $x=\infty$. All these properties also hold for $\operatorname{Li}_{{\bf b}}^{\boldsymbol{a}}(z)$ for any word ${\bf a}$ because such functions are simply linear combinations with rational coefficients of the $\operatorname{Li}_{{\bf b}}^{ss\cdots s}(z)$ (using repeatedly Eq. (eqdeplin) above).

As an (important) application, we prove the following lemma.

**Lemma 8**. *For any fixed $z\in \mathbb C\setminus [0,1]$, any ${\bf a}$ and any ${\bf b}\neq \emptyset$, we have $$\label{eq:intpoids}
\operatorname{Li}_{{\bf b}}^{\boldsymbol{a}}\left(\frac1z\right) = \int_0^1
\frac{\omega_{{\bf b}}^{\boldsymbol{a}}(x)}{z-x} \textup{d}x,$$ where $$\label{eq:expressionpoids}
\omega_{{\bf b}}^{\boldsymbol{a}}(x) :=\frac1{2i \pi}\lim_{y\to 0+}
\left[\operatorname{Li}_{{\bf b}}^{\boldsymbol{a}}\left(\frac{1}{x}+iy\right)-
\operatorname{Li}_{{\bf b}}^{\boldsymbol{a}}\left(\frac{1}{x}-iy\right)\right] \in L^1([0,1]).$$ The *weight function* $\omega_{{\bf b}}^{\boldsymbol{a}}(x)$ is $C^\infty$ on $(0,1)$, with at most (power of) logarithm singularities at $x=0$ and $x=1$.*

*Proof.* For any fixed $z\in \mathbb C\setminus [1,+\infty)$, let us consider the Cauchy representation formula $$\operatorname{Li}_{{\bf b}}^{\boldsymbol{a}}(z) = \frac z{2i\pi}\int_{\mathcal{C}}
\frac{\operatorname{Li}_{{\bf b}}^{\boldsymbol{a}}(t)}{t(t-z)} \textup{d}t,$$ where $\mathcal{C}$ is any simple closed curve surrounding $z$ and not crossing the cut $[1,+\infty)$. We can deform $\mathcal{C}$ to a simple closed curve defined as follows: given $\varepsilon>0$ and $R>0$ (such that $\vert z\vert <R$), we glue together two straightlines $[1+i\varepsilon,R+i\varepsilon]$, $[1-i\varepsilon+R,R-i\varepsilon]$, a semi-circle of center $1$ and diameter $[1-i\varepsilon, 1+i\varepsilon]$ and an arc of circle of center $0$ passing through $R+i\varepsilon$ and $R-i\varepsilon$ (both arcs not crossing $[1,+\infty)$). The analytic properties of $\operatorname{Li}_{{\bf b}}^{\boldsymbol{a}}(z)$ are such that we can let $\varepsilon\to 0$ and $R\to \infty$ to get the representation $$\begin{aligned}
\operatorname{Li}_{{\bf b}}^{\boldsymbol{a}}(z)
& = z\int_1^{\infty} \frac{\omega_{{\bf b}}^{\boldsymbol{a}}(1/t)}{t(t-z)} \textup{d}t\\
& = z\int_0^{1} \frac{\omega_{{\bf b}}^{\boldsymbol{a}}(x)}{1-zx} \textup{d}x\qquad (\mbox{by letting }x=1/t),
\end{aligned}$$ where $\omega_{{\bf b}}^{\boldsymbol{a}}(x)$ is defined by (eq:expressionpoids). We obtain (eq:intpoids) by changing $z$ to $1/z$. ◻

(This proof is not specific to multiple polylogarithms. Such weighted integral representations are known as Stieltjes representations; see [@Henrici p. 591, Theorem 12.10d].)

We note two important consequences of the expression (eq:expressionpoids) for $\omega_{{\bf b}}^{\boldsymbol{a}}(x)$. To begin with, if $$\frac{\textup{d}}{\textup{d}z}\left[\operatorname{Li}_{{\bf b}}^{\boldsymbol{a}}\left(\frac1z\right)\right]
= R(z)\operatorname{Li}_{{\bf b}'}^{\boldsymbol{a}'}\left(\frac1z\right),$$ then $$\frac{\textup{d}}{\textup{d}x}\omega_{{\bf b}}^{\boldsymbol{a}}(x)
= R(x)\omega_{{\bf b}'}^{\boldsymbol{a}'}(x)$$ where the function $R(z)$ is one of $\displaystyle -\frac{1}{z},\frac{1}{1-z}$ and $\displaystyle \frac{1}{z(1-z)}$ (see §  3.1). In other words, *weights obey the same derivation rules as the corresponding polylogarithms.* This observation will be crucial in § 5.1. Moreover, we also remark that if the value $\operatorname{Li}_{{\bf b}}^{\boldsymbol{a}}(1)$ is finite, then $\omega_{{\bf b}}^{\boldsymbol{a}}(1)=0$.

**Lemma 9**. *For any $x\in (0,1)$ and any integer $k\ge 0$, we have $$\label{eq:1}
\omega_{\{1\}_{2k}}^{\{\ell s\}_{k-1}\ell}(x)=\operatorname{Li}_{\{1\}_{2k-1}}^{\{s\ell\}_{k-1}}(x),$$ $$\label{eq:2}
\omega_{\{1\}_{2k+1}}^{\{s \ell \}_{k}}(x)=\operatorname{Li}_{\{1\}_{2k}}^{\{\ell s\}_{k-1}\ell}(x),$$ and $$\begin{aligned}
\omega_{2\{1\}_{2k+1}}^{\{\ell s\}_{k}\ell}(x)&=\sum_{j=0}^k \operatorname{Li}_{1\{2\}_j}^{\{\ell\}_j}(1-x) \operatorname{Li}_{\{1\}_{2k-2j+1}}^{\{s \ell\}_{k-j}}(x) \notag
\\
& \qquad \qquad \qquad +\sum_{j=1}^{k+1} \operatorname{Li}_{\{2\}_j}^{\{\ell\}_{j-1}}(1-x) \operatorname{Li}_{\{1\}_{2k-2j+2}}^{\{\ell s\}_{k-j}\ell}(x) \label{eq:3}
\\
&= -\operatorname{Li}_{2\{1\}_{2k}}^{\{s \ell \}_{k}}(x) + \operatorname{Li}_{\{2\}_{k+1}}^{\{\ell\}_k}(1).\label{eq:3alternative}
\end{aligned}$$*

*Proof.* Equations (eq:1) and (eq:2) are readily checked by expanding $\frac{1}{z-x}=\sum_{n=0}^{\infty} \frac{x^n}{z^{n+1}}$ in the integral (eq:intpoids). To prove (eq:3), we remark that both sides differentiate to the same function $-\frac1x \omega_{\{1\}_{2k+2}}^{\{\ell s\}_k\ell}(x)=-\frac1x \operatorname{Li}_{\{1\}_{2k+1}}^{\{s \ell \}_{k}}(x)$, since all functions but this precise one are killed by telescoping when differentiating the right hand side of (eq:3). It follows that the functions on both sides of (eq:3) differ only by a constant. This constant must be $0$ because both sides vanish at $x=1$ (see the remark just before Lemma 9). The same argument yields also $$\omega_{2\{1\}_{2k+1}}^{\{\ell s\}_{k}\ell}(x) = - \int\frac1x \operatorname{Li}_{\{1\}_{2k+1}}^{\{s \ell \}_{k}}(x) \textup{d}x
=-\operatorname{Li}_{2\{1\}_{2k}}^{\{s \ell \}_{k}}(x) + C_k$$ for some constant $C_k$. This constant is seen to be equal to $\operatorname{Li}_{\{2\}_{k+1}}^{\{\ell\}_k}(1)$ by taking $x=0$ in (eq:3). This proves (eq:3alternative), and concludes the proof of Lemma 9. ◻

In the setting of the Padé problem $\mathcal{P}_{r,n}$, we define the function $$P_{r,n}(z) = \sum_{\rho=0}^r \bigg[ A_{\rho,r,n}(z) \omega_{2\{1\}_{2\rho+1}}^{\{\ell s\}_\rho\ell}(z)
+ B_{\rho,r,n}(z) \omega_{\{1\}_{2\rho+2}}^{\{\ell s\}_\rho\ell}(z)+C_{\rho,r,n}(z)
\omega_{\{1\}_{2\rho+1}}^{\{s\ell\}_\rho}(z)\bigg]$$ obtained from $S_{r,n}$ by replacing every polylogarithm with its weight (see Lemma 11 below). By (eq:1), (eq:2) and (eq:3alternative), this function $P_{r,n}$ is analytic on the disk $\vert z\vert<1$, with a (power of) logarithm singularity at $z=1$. In particular, it is in $L^1([0,1])$. The following lemma is an immediate consequence of (eq:1), (eq:2), (eq:3) and the definition of $U_{j,r,n}(z)$ and $V_{j,r,n}(z)$. As in the rest of the paper, we continue analytically all polylogarithms to $\mathbb{C}\setminus [1,+\infty)$.

**Lemma 10**. *For any $z\in \mathbb C \setminus  [1,+\infty)$, $$P_{r,n}(z)=\sum_{j=0}^r \bigg[U_{j,r,n}(z)\operatorname{Li}_{\{1\}_{2j+1}}^{\{s\ell\}_j}(z)
+ V_{j,r,n}(z)\operatorname{Li}_{\{1\}_{2j}}^{\{\ell s\}_{j-1}\ell}(z)\bigg].$$*

We conclude this section with the precise connection between $P_{r,n}(z)$ and $S_{r,n}(z)$.

**Lemma 11**. *In the setting of the Padé problem $\mathcal{P}_{r,n}$, for any $z\in \mathbb C \setminus [0,1]$ we have $$S_{r,n}(z)=\int_0^1 \frac{P_{r,n}(x)}{z-x} \textup{d}x.$$*

*Proof.* By definition of $S_{r,n}(z)$ and Lemma 8, for any $z\in \mathbb C \setminus [0,1]$ we have $$\begin{aligned}
S_{r,n}(z)&=\sum_{\rho=0}^r \bigg[ A_{\rho,r,n}(z) \int_0^1 \frac{\omega_{2\{1\}_{2\rho+1}}^{\{\ell s\}_\rho\ell}(x)}{z-x} \textup{d}x
+ B_{\rho,r,n}(z) \int_0^1\frac{\omega_{\{1\}_{2\rho+2}}^{\{\ell s\}_\rho\ell}(x)}{z-x} \textup{d}x
\\ & \hspace{4cm}+C_{\rho,r,n}(z)
\int_0^1\frac{\omega_{\{1\}_{2\rho+1}}^{\{s\ell\}_\rho}(x)}{z-x} \textup{d}x\bigg] + D_{r,n}(z)
\\ &= \int_0^1 \frac{P_{r,n}(x)}{z-x} \textup{d}x + \sum_{\rho=0}^r \int_0^1
\bigg[\frac{A_{\rho,r,n}(z)-A_{\rho,r,n}(x)}{z-x}\omega_{2\{1\}_{2\rho+1}}^{\{\ell s\}_\rho\ell}(x)
\\&+
\frac{B_{\rho,r,n}(z)-B_{\rho,r,n}(x)}{z-x}\omega_{\{1\}_{2\rho+2}}^{\{\ell s\}_\rho\ell}(x) +
\frac{C_{\rho,r,n}(z)-C_{\rho,r,n}(x)}{z-x}\omega_{\{1\}_{2\rho+1}}^{\{s\ell \}_\rho}(x)
\bigg]\textup{d}x + D_{r,n}(z).
\end{aligned}$$ Hence, $$\label{eq:Spoly}
S_{r,n}(z)=\int_0^1 \frac{P_{r,n}(x)}{z-x} \textup{d}x + \textup{polynomial}(z) .$$ But, as $z\to \infty$, $S_{r,n}(z)=\mathcal{O}(1/z)$ and $\int_0^1 \frac{P_{r,n}(x)}{z-x} \textup{d}x \to 0$ (because $P_{r,n}(x)\in L^1([0,1])$, as noticed above). Therefore, the polynomial in (eq:Spoly) is identically $0$ and this completes the proof of Lemma 11. ◻

# Resolution of the Padé problem $\mathcal{P}_{r,n}$

In this section we prove Theorem 1, using the tools of §§ 3 and 4. Starting with a solution $S_{r,n}(z)$ of the Padé problem $\mathcal{P}_{r,n}$, we apply the differential operator $\frac{z^{n+1}}{n!} \big( \frac{ \textup{d}}{\textup{d}z}\big)^{n+1}$ and prove in §§  5.1 and 5.2 that the resulting function is a solution of another Padé approximation problem, denoted by $\mathcal{Q}_{r,n}$ and stated in § 5.3. Then we observe in § 5.3 that $\mathcal{Q}_{r,n}$ is nothing but Sorokin's problem [@sorokin1] for $\pi^2$, denoted by $\mathcal{R}_{r,n}$, up to a change of variable $z\mapsto 1-z$. Since Sorokin has proved that $\mathcal{R}_{r,n}$ has a unique solution up to proportionality, the same result holds for $\mathcal{Q}_{r,n}$ and $\mathcal{P}_{r,n}$.

To conclude the proof of Theorem 1, we deduce in §§ 5.4 and 5.5 the integral representation (eq:intro6) of $S_{r,n}(z)$ from Sorokin's integral representation of the solution of $\mathcal{R}_{r,n}$, using the integral operator introduced in § 3.2.

## First reduction

Let $S_{r,n}(z)$ be a solution of the Padé problem $\mathcal{P}_{r,n}$. By Lemma 1, there exist some polynomials $\check{A}_{\rho,r,n}(z)$, $\check{B}_{\rho,r,n}(z)$ and $\check{C}_{r,n}(z)$ of degree $\le 2n+1$ such that $$\begin{gathered}
\widehat{S}_{r,n}(z):=\frac{z^{n+1}}{n!}S^{(n+1)}_{r,n}(z)
= \sum_{\rho=0}^r \bigg[\frac{\check{A}_{\rho,r,n}(z)}{(1-z)^{n+1}} \operatorname{Li}_{\{1\}_{2\rho+2}}^{\{\ell s\}_\rho \ell}\bigg(\frac1z\bigg)
\\
+\frac{\check{B}_{\rho,r,n}(z)}{(1-z)^{n+1}} \operatorname{Li}_{\{1\}_{2\rho+1}}^{\{s\ell\}_\rho}\bigg(\frac1z\bigg)  \bigg]
+ \frac{\check{C}_{r,n}(z)}{(1-z)^{n+1}} = \mathcal{O}\bigg(\frac{1}{z^{(r+1)(n+1)}}\bigg).\label{eq:66}
\end{gathered}$$ As in § 4 we consider the function $P_{r,n}(z)$ defined by $$P_{r,n}(z) = \sum_{\rho=0}^r \bigg[ A_{\rho,r,n}(z) \omega_{2\{1\}_{2\rho+1}}^{\{\ell s\}_\rho\ell}(z)
+ B_{\rho,r,n}(z) \omega_{\{1\}_{2\rho+2}}^{\{\ell s\}_\rho\ell}(z)+C_{\rho,r,n}(z)
\omega_{\{1\}_{2\rho+1}}^{\{s\ell\}_\rho}(z)\bigg].$$ Since it is obtained from $S_{r,n}$ by replacing each polylogarithm by its weight, it obeys the same derivation rules (see the remark before Lemma 9). This implies that $$\begin{aligned}
\widehat{P}_{r,n}(z):=\frac{z^{n+1}}{n!}P^{(n+1)}_{r,n}(z)
&= \sum_{\rho=0}^r \bigg[\frac{\check{A}_{\rho,r,n}(z)}{(1-z)^{n+1}} \omega_{\{1\}_{2\rho+2}}^{\{\ell s\}_\rho \ell}(z)
+\frac{\check{B}_{\rho,r,n}(z)}{(1-z)^{n+1}} \omega_{\{1\}_{2\rho+1}}^{\{s\ell\}_\rho}(z)  \bigg] \notag
\\
&=\sum_{\rho=0}^r \bigg[\frac{\check{A}_{\rho,r,n}(z)}{(1-z)^{n+1}} \operatorname{Li}_{\{1\}_{2\rho+1}}^{\{s\ell\}_\rho}(z)
+\frac{\check{B}_{\rho,r,n}(z)}{(1-z)^{n+1}} \operatorname{Li}_{\{1\}_{2\rho}}^{\{\ell s\}_{\rho-1}\ell}(z)  \bigg] \label{eq:5}
\end{aligned}$$ with the same polynomials $\check{A}_{\rho,r,n}(z)$ and $\check{B}_{\rho,r,n}(z)$; here we have used Eqs. (eq:1) and (eq:2) in Lemma 9 to compute the weights.

Now, by Lemmas 2, 10 and the Padé conditions at $z=1$ in $\mathcal{P}_{r,n}$ for $U_{j,r,n}$ and $V_{j,r,n}$, the function $\widehat{P}_{r,n}(z)$ is necessarily of the form $$\label{eq:6}
\widehat{P}_{r,n}(z)=\sum_{j=0}^r \bigg[h_{2j+1}(z) \operatorname{Li}_{\{1\}_{2j+1}}^{\{s\ell\}_j}(z)
+ h_{2j}(z) \operatorname{Li}_{\{1\}_{2j}}^{\{\ell s\}_{j-1}\ell}(z)  \bigg]$$ for some functions $h_j$ holomorphic at $z=1$. Now we have obtained two expressions for $\widehat{P}_{r,n}(z)$, namely Eqns. (eq:5) and (eq:6). Using Lemma 7 they have to coincide, that is $\frac{\check{A}_{\rho,r,n}(z)}{(1-z)^{n+1}} = h_{2\rho+1}(z)$ and $\frac{\check{B}_{\rho,r,n}(z)}{(1-z)^{n+1}} =  h_{2\rho}(z)$ for any $\rho=0, \ldots, r$. Therefore $(1-z)^{n+1}$ divides $\check{A}_{\rho,r,n}(z)$ and $\check{B}_{\rho,r,n}(z)$.

We now claim that $(1-z)^{n+1}$ also divides $\check{C}_{r,n}(z)$. To prove this, we use the integral representation for $S_{r,n}(z)$ given by Lemma 11. Differentiating $n+1$ times under the integral, we obtain $$\widehat{S}_{r,n}(z)=(n+1)(-z)^{n+1}\int_0^1 \frac{P_{r,n}(x)}{(z-x)^{n+2}} \textup{d}x.$$ Again by Lemma 10 and the Padé conditions at $z=1$ in $\mathcal{P}_{r,n}$ for $U_{r,n,j}$ and $V_{r,n,j}$, we deduce that $$P_{r,n}(x)=\mathcal{O}\big((1-x)^{n+1} (1+\vert \log(1-x)\vert^{2r+1})\big)$$ as $x\to 1$, $x<1$. Therefore the singularity of $\widehat{S}_{r,n}(z)$ at $z=1$ is at most a power of logarithm. The expression (eq:66) for $\widehat{S}_{r,n}(z)$, together with the above deductions made for $\check{A}_{\rho,r,n}(z)$ and $\check{B}_{\rho,r,n}(z)$, implies the claim.

We can summarize the above results as follows: there exist polynomials $\widehat{A}_{\rho,r,n}(z)$, $\widehat{B}_{\rho,r,n}(z)$ ($\rho \in\{0, \ldots, r\}$) and $\widehat{C}_{r,n}(z)$, all of degree at most $n$, such that $$\begin{gathered}
\widehat{S}_{r,n}(z)
= \sum_{\rho=0}^r \bigg[\widehat{A}_{\rho,r,n}(z) \operatorname{Li}_{\{1\}_{2\rho+2}}^{\{\ell s\}_\rho \ell}\bigg(\frac1z\bigg)
\\
+\widehat{B}_{\rho,r,n}(z) \operatorname{Li}_{\{1\}_{2\rho+1}}^{\{s\ell\}_\rho}\bigg(\frac1z\bigg)  \bigg]
+ \widehat{C}_{r,n}(z) = \mathcal{O}\bigg(\frac{1}{z^{(r+1)(n+1)}}\bigg).\label{eq:7}
\end{gathered}$$

## Second reduction

We want to find further Padé conditions involving the polynomials $\widehat{A}_{\rho,r,n}(z)$, $\widehat{B}_{\rho,r,n}(z)$ ($\rho \in\{0, \ldots, r\}$) and $\widehat{C}_{r,n}(z)$. For this, we form the functions $$Q_{j,r,n}:=\sum_{\rho=j}^r \bigg[-A_{\rho,r,n}(z) \operatorname{Li}_{2\{1\}_{2\rho-2j}}^{\{s\ell\}_{\rho-j}}(z)
+ B_{\rho,r,n}(z) \operatorname{Li}_{\{1\}_{2\rho-2j+1}}^{\{s\ell\}_{\rho-j}}(z) +
C_{\rho,r,n}(z) \operatorname{Li}_{\{1\}_{2\rho-2j}}^{\{\ell s\}_{\rho-j-1}\ell}(z)\bigg]$$ where $j=0, \ldots, r$, and $A_{\rho,r,n}(z)$, $B_{\rho,r,n}(z)$, $C_{\rho,r,n}(z)$ are the polynomials in our initial Padé problem $\mathcal{P}_{r,n}$. Each $Q_{j,r,n}(z)$ is holomorphic at $z=0$ and the rules of differentiation of multiple polylogarithms (see § 3.1) show that $$\begin{gathered}
\widehat{Q}_{j,r,n}(z):=\frac{z^{n+1}}{n!}Q_{j,r,n}^{(n+1)}(z)
\\
=\sum_{\rho=j}^r \bigg[\widehat{A}_{\rho,r,n}(z) \operatorname{Li}_{\{1\}_{2\rho-2j+1}}^{\{s\ell\}_{\rho-j}}(z)
+ \widehat{B}_{\rho,r,n}(z) \operatorname{Li}_{\{1\}_{2\rho-2j}}^{\{\ell s\}_{\rho-j-1}\ell}(z) \bigg] =  \mathcal{O}(z^{n+1})
\end{gathered}$$ for all $j=0, \ldots r$. The main point here is that the polynomials $\widehat{A}_{\rho,r,n}(z)$ and $\widehat{B}_{\rho,r,n}(z)$ are the same as in Eq. (eq:7).

## The intermediate Padé problem $\mathcal{Q}_{r,n}$

The previous two sections show that any solution $S_{r,n}(z)$ to the problem $\mathcal{P}_{r,n}$ yields (by differentiating $n+1$ times and multiplying by $z^{n+1}/n!$) a solution to the following problem: given non-negative integers $r$ and $n$, find polynomials $\widehat{A}_{\rho,r,n}(z)$, $\widehat{B}_{\rho,r,n}(z)$ (for $0 \leq \rho \leq r$) and $\widehat{C}_{r,n}(z)$, of degrees $\leq n$, such that the following holds: $$\begin{aligned}
\widehat{S}_{r,n}(z)&
:= \sum_{\rho=0}^r \bigg[\widehat{A}_{\rho,r,n}(z) \operatorname{Li}_{\{1\}_{2\rho+2}}^{\{\ell s\}_\rho \ell}\bigg(\frac1z\bigg)
 +\widehat{B}_{\rho,r,n}(z) \operatorname{Li}_{\{1\}_{2\rho+1}}^{\{s\ell\}_\rho}\bigg(\frac1z\bigg)  \bigg]  \notag
\\
&\hspace{8cm} + \widehat{C}_{r,n}(z) = \mathcal{O}\bigg(\frac{1}{z^{(r+1)(n+1)}}\bigg),  \notag
\\
\widehat{Q}_{j,r,n}(z)&:=\sum_{\rho=j}^r \bigg[\widehat{A}_{\rho,r,n}(z)
\operatorname{Li}_{\{1\}_{2\rho-2j+1}}^{\{s\ell\}_{\rho-j}}(z) + \widehat{B}_{\rho,r,n}(z)
\operatorname{Li}_{\{1\}_{2\rho-2j}}^{\{\ell s\}_{\rho-j-1}\ell}(z) \bigg] \notag
\\
&\hspace{8cm} = \mathcal{O}(z^{n+1}), \quad j=0, \ldots, r.  \notag
\end{aligned}$$ We shall denote this Padé approximation problem by $\mathcal{Q}_{r,n}$. It amounts to solving a linear system of $(3r+4)(n+1)-1$ equations in $(3r+4)(n+1)$ unknowns (the coefficients of the polynomials). Hence it has a least one non trivial solution and our next task is to prove that is has exactly one solution up to a multiplicative constant.

To do so, we will identify the problem with one already solved by Sorokin [@sorokin1]. We first observe the effect of changing $z$ to $1-z$ in the Padé problem $\mathcal{Q}_{r,n}$.

**Lemma 12**. *For any $z\in \mathbb C\setminus [0,1]$, we have $$\begin{aligned}
\operatorname{Li}_{\{1\}_{2\rho+1}}^{\{s\ell \}_\rho}\bigg(\frac1z\bigg)&
  = (-1) ^{\rho+1}\operatorname{Li}_{1\{2\}_{\rho}}^{\{s\}_\rho}\bigg(\frac1{1-z}\bigg),
\\
\operatorname{Li}_{\{1\}_{2\rho+2}}^{\{\ell s\}_\rho \ell}\bigg(\frac1z\bigg)&
  = (-1) ^{\rho+1}\operatorname{Li}_{\{2\}_{\rho+1}}^{\{s\}_\rho}\bigg(\frac1{1-z}\bigg).
\end{aligned}$$*

*Proof.* We prove these identities by induction on $\rho$. They hold trivially for $\rho=0$ and by differentiation of both sides at level $\rho$, we get the identity at level $\rho-1$. We deduce that the identity at level $\rho$ holds, up to some additive constant. This constant must be $0$ because both sides vanish at $z=\infty$. ◻

Therefore, when we change $z$ to $1-z$, the Padé problem $\mathcal{Q}_{r,n}$ becomes $$\begin{aligned}
\widehat{S}_{r,n}(1-z)&
:= \sum_{\rho=0}^r(-1)^{\rho+1} \bigg[\widehat{A}_{\rho,r,n}(1-z) \operatorname{Li}_{\{2\}_{\rho+1}}^{\{s\}_\rho}\bigg(\frac1z\bigg)
 +\widehat{B}_{\rho,r,n}(1-z) \operatorname{Li}_{1\{2\}_{\rho}}^{\{s\}_\rho}\bigg(\frac1z\bigg)  \bigg]
\\
&\qquad\qquad
+ \widehat{C}_{r,n}(1-z) = \mathcal{O}\bigg(\frac{1}{(1-z)^{(r+1)(n+1)}}\bigg)
=\mathcal{O}\bigg(\frac{1}{z^{(r+1)(n+1)}}\bigg)
\\
\widehat{Q}_{j,r,n}(1-z)&:=\sum_{\rho=j}^r \bigg[\widehat{A}_{\rho,r,n}(1-z) \operatorname{Li}_{\{1\}_{2\rho-2j+1}}^{\{s\ell\}_{\rho-j}}(1-z)
\\
& \qquad\qquad + \widehat{B}_{\rho,r,n}(1-z)
\operatorname{Li}_{\{1\}_{2\rho-2j}}^{\{\ell s\}_{\rho-j-1}\ell}(1-z) \bigg] =  \mathcal{O}((1-z)^{n+1}), \quad j=0, \ldots, r.
\end{aligned}$$ Let us define $$\begin{aligned}
\widetilde{A}_{\rho,r,n}(z)&=(-1)^{\rho+1}\widehat{A}_{\rho,r,n}(1-z), \quad
\widetilde{B}_{\rho,r,n}(z)=(-1)^{\rho+1}\widehat{B}_{\rho,r,n}(1-z),
\\
\widetilde{C}_{r,n}(z)&=\widehat{C}_{r,n}(1-z), \quad
\widetilde{S}_{r,n}(z)=\widehat{S}_{r,n}(1-z), \quad
\widetilde{Q}_{j,r,n}(z)=-\widehat{Q}_{j,r,n}(1-z).
\end{aligned}$$ With these notations, the Padé problem $\mathcal{Q}_{r,n}$ now reads $$\begin{aligned}
\widetilde{S}_{r,n}(z):=&\sum_{\rho=0}^r \bigg[\widetilde{A}_{\rho,r,n}(z)
\operatorname{Li}_{\{2\}_{\rho+1}}^{\{s\}_\rho}\bigg(\frac1z\bigg) + \widetilde{B}_{\rho,r,n}(z)
\operatorname{Li}_{1\{2\}_{\rho}}^{\{s\}_\rho}\bigg(\frac1z\bigg)\bigg] + \widetilde{C}_{r,n}(z) = \mathcal{O}\bigg(\frac{1}{z^{(r+1)(n+1)}}\bigg)
\\
\widetilde{Q}_{j,r,n}(z)&:=\sum_{\rho=j}^r (-1)^\rho\bigg[\widetilde{A}_{\rho,r,n}(z) \operatorname{Li}_{\{1\}_{2\rho-2j+1}}^{\{s\ell\}_{\rho-j}}(1-z)
+ \widetilde{B}_{\rho,r,n}(z) \operatorname{Li}_{\{1\}_{2\rho-2j}}^{\{\ell s\}_{\rho-j-1}\ell}(1-z) \bigg]
\\ &\hspace{8cm}=  \mathcal{O}((1-z)^{n+1}), \quad j=0, \ldots, r.
\end{aligned}$$ In spite of different notations, we recognize here Sorokin's problem [@sorokin1] for $\pi^2$ of weight $2r+2$, which we denote by $\mathcal{R}_{r,n}$ from now on. Sorokin proved that this problem has a unique solution up to proportionality. Therefore the same property holds for $\mathcal{Q}_{r,n}$, and also for $\mathcal{P}_{r,n}$. This concludes the proof of Theorem 1, except for the integral representation (eq:intro6) of $S_{r,n}(z)$ that we shall prove now.

## Hypergeometric integrals for $\tilde{S}_{r,n}(z)$ and $S_{r,n}(z)$

Sorokin has found an explicit integral formula for the solution $\widetilde{S}_{r,n}(z)$ of his Padé problem $\mathcal{R}_{r,n}$ stated in § 5.3 (see [@sorokin1 Lemma 17, p. 1835]), namely $$\label{eq:intro2}
\widetilde{S}_{r,n}(z)=(-1)^{(r+1)n}\int_{[0,1]^{2r+2}} \prod_{j=1}^{r+1} \frac{x_j^n(1-x_j)^n y_j^n(1-y_j)^n}
{\big(\frac{z}{x_1y_1\cdots x_{j-1}y_{j-1}}-x_jy_j\big)^{n+1}}
\textup{d}x_j\textup{d}y_j.$$ In this and the next sections we shall deduce from it the integral expression (eq:intro6) of $S_{r,n}(z)$, using the relation $$\label{eq:11}
\frac{z^{n+1}}{n!}S_{r,n}^{(n+1)}(z)= \widetilde{S}_{r,n}(1-z)$$ and the integral operator defined in § 3.2.

To begin with, we recall that Sorokin solved his Padé approximation problem $\mathcal{R}_{r,n}$ recursively and showed that, for any integer $r\ge 1$ and any $z\in \mathbb C\setminus [0,1]$, $$\label{eq:13}
\tilde{S}_{r-1,n}(z) = \frac{1}{n!^2}z^{n+1}(1-z)^{n+1}\big(z^{n+1}\tilde{S}_{r,n}^{(n+1)}(z)\big)^{(n+1)}$$ and $$\tilde{S}_{0,n}(z)=\int_0^1\int_0^1 \frac{x^n(1-x)^ny^n(1-y)^n}{(z-xy)^{n+1}} \textup{d}x\textup{d}y.$$ It is not hard to see that, with the notation of § 3.2, we have for $z\in\mathbb{C}\setminus[0,1]$: $$\label{eq59bis}
\tilde{S}_{0,n}(z) = {\bf H}^{n+1}_{n+1,0}  \left(\int_0^1 \frac{x^n(1-x)^n}{(z-x)^{n+1}}\right)=
{\bf H}^{n+1}_{n+1,0}  {\bf H}^{n+1}_{n+1,n+1}  (\boldsymbol{1}),$$ where $\boldsymbol{1}$ is the constant function equal to 1 on $\mathbb{C}\setminus[0,1]$. We can apply the general properties of hypergeometric integrals proved in § 3.2 to (eq:13) and we get the following result, which is nothing but (eq:intro2) written in a different language (see § 5.5 for details). We recall that $f^{\partial}(z):=f(1-z)$ and we denote by ${\bf H}^k
= {\bf H}\circ{\bf H}\circ\cdots\circ{\bf H}$ the composition of an integral operator ${\bf H}$ with itself $k$ times.

**Proposition 2**. *For any $z\in \mathbb{C}\setminus[0,1]$ and any integer $r\ge 0$, we have $$\label{eq:14}
\tilde{S}_{r,n}(z)= ({\bf H}^{n+1}_{n+1,0}{\bf H}^{n+1}_{n+1,n+1})^{r+1} (\boldsymbol{1})(z)$$ and $$\label{eq:15}
\tilde{S}_{r,n}^{\partial}(z)=({\bf H}^{n+1}_{0,n+1}{\bf H}^{n+1}_{n+1,n+1})^{r+1} (\boldsymbol{1})(z).$$*

Eq. (eq:14) follows immediately from Eq. (eq59bis) and the relation $$\tilde{S}_{r,n} = {\bf H}^{n+1}_{n+1,0}{\bf H}^{n+1}_{n+1,n+1}(\tilde{S}_{r-1,n}),$$ which is just a translation of Eq. (eq:13) (using Lemma 3). Then Eq. (eq:15) follows from (eq:14) by means of Lemma 6. Now Eq. (eq:11) reads $$\label{eq:15bis}
\frac{z^{n+1}}{n!}S_{r,n}^{(n+1)}(z) = \tilde{S}_{r,n}^{\partial}(z)$$ and $\lim_{z\to \infty} S_{r,n} (z)=0$ for any $r\ge 0$, so that Lemma 3 yields $$S_{r,n}(z)={\bf H}^{ n+1}_{n+1,0} (\widetilde{S}_{r,n}^{\partial})(z).$$ Hence, by (eq:15) in Proposition 2, we obtain the following result (using also Lemma 5 to take limits as $z\to 1$).

**Proposition 3**. *For any $z\in \mathbb{C}\setminus[0,1]$ and any integer $r\ge 0$, we have $$\label{eq:16}
S_{r,n}(z)={\bf H}^{ n+1}_{n+1,0} ({\bf H}^{n+1}_{0,n+1}{\bf H}^{n+1}_{n+1,n+1})^{r+1} (\boldsymbol{1})(z).$$ Moreover, both sides of (eq:16) are defined and equal for $z=1$.*

## Explicit multiple integrals

The integral expression for $S_{r,n}(z)$ given in Theorem 1 is simply the explicit "expansion" of the formula (eq:16) given in Proposition 3 above. Let us provide details on this expansion.

For any function $F$ analytic on $\mathbb{C}\setminus [0,1]$ and at infinity, Eq. (eq:12) in § 3.2 reads $${\bf H}^{n+1}_{n+1,n+1} (F)(z)= (-1)^{n+1}  \int_0^1 \frac{u^n(1-u)^n}{(u-z)^{n+1}}F\Big(\frac zu\Big) \textup{d}u.$$ This function ${\bf H}^{n+1}_{n+1,n+1} (F)(z)$ is analytic on $\mathbb{C}\setminus [0,1]$ and at infinity, and vanishes to an order $\geq n+1$ at $\infty$ (using Lemma 3). The same property can be proved in the same way for the following function: $$\begin{aligned}
 {\bf H}^{n+1}_{0,n+1}{\bf H}^{n+1}_{n+1,n+1}(F)(z)&=z^{n+1}\int_0^1 \frac{v^{-1}(1-v)^n}{(v-z)^{n+1}}
 \int_0^1\frac{u^n(1-u)^n}{(u-z/v)^{n+1}}F\Big(\frac z{uv}\Big) \textup{d}u \textup{d}v
\\
&=z^{n+1}\int_0^1\int_0^1\frac{v^n(1-v)^nu^n(1-u)^n}{(v-z)^{n+1}(uv-z)^{n+1}}F\Big(\frac z{uv}\Big) \textup{d}u \textup{d}v.
\end{aligned}$$ By induction on $r\ge 0$ this implies, using Eq. (eq:15): $$\begin{gathered}
\tilde{S}_{r,n}^{\partial}(z) = ({\bf H}^{n+1}_{0,n+1}{\bf H}^{n+1}_{n+1,n+1})^{r+1} (\boldsymbol{1})(z) =  z^{(r+1)(n+1)}
\\\times \int\limits_{[0,1]^{2(r+1)}}\frac{\displaystyle \prod_{j=1}^{r+1}\big((u_jv_j)^{(r-j+2)(n+1)-1}(1-u_j)^n(1-v_j)^n\big)}
{\displaystyle \prod_{j=1}^{r+1} \big((z-u_1v_1\cdots u_{j-1}v_{j-1}u_j)^{n+1}(z-u_1v_1\cdots u_{j}v_{j})^{n+1}\big)}
  \textup{d}{\bf u} \textup{d}{\bf v}.
\end{gathered}$$ Therefore the equality $${\bf H}^{ n+1}_{n+1,0} ({\bf H}^{n+1}_{0,n+1}{\bf H}^{n+1}_{n+1,n+1})^{r+1} (\boldsymbol{1})(z)  =
(-1)^{ n+1}  \int_0^1 u_0^{-1}(1-u_0)^{  n} \tilde{S}_{r,n}^{\partial}(z/u_0) \textup{d}u_0$$ yields, using Proposition 3: $$\begin{gathered}
S_{r,n}(z)=(-1)^{ n+1}z^{(r+1)  (n+1)} \\
\times \int_{[0,1]^{2r+3}}
\frac{\displaystyle u_0^{(r+1) (n+1)-1}(1-u_0)^{ n}
\prod_{j=1}^{r+1}\big((u_jv_j)^{(r-j+2)(n+1)-1}(1-u_j)^n(1-v_j)^n\big)}
{\displaystyle \prod_{j=1}^{r+1}\big((z-u_0u_1v_1\cdots u_{j-1}v_{j-1}u_j)^{n+1}
(z-u_0u_1v_1\cdots u_{j}v_{j})^{n+1}\big)} \textup{d}{\bf u}\textup{d}{\bf v}.
\end{gathered}$$ This completes the proof of Theorem 1.

# Beyond Vasilyev's conjecture: irrationality of odd zeta values

A natural problem is to find a proof that the numbers $\zeta(2r+1)$, $r\geq 0$, span an infinite-dimensional $\mathbb{Q}$-vector space [@BR; @rivoal] that would be analogous to Sorokin's proof that $\pi$ is transcendental [@sorokin1] (since Sorokin's result is equivalent to the fact that the numbers $\zeta(2r)$, $r\geq 0$, span an infinite-dimensional $\mathbb{Q}$-vector space). In particular, such a proof would involve a Padé approximation problem with multiple polylogarithms.

Let $\sigma$ be an integer such that $1 \leq \sigma \leq r+2$. To achieve this goal, it is enough to relate the very-well-poised hypergeometric series $$\label{eqvwp}
\sum_{k=1}^{\infty} (k+\frac{n}2) \frac{(k-\sigma n)_{\sigma n} (k+n+1) _{\sigma n}}{(k)_{n+1}^{2r+4}},$$ which can be used to prove the above mentioned result (see for instance [@fischler3]), to such a Padé approximation problem. An analogous work has been done in [@firi], where this series is related to a Padé approximation problem involving only classical polylogarithms, namely of depth 1.

We shall prove now that for $\sigma =1$ the hypergeometric series (eqvwp) is equal (up to a sign) to $S_{r,n}(1)$, thereby providing in this case the relation we are looking for. For any $\sigma$ we shall prove that this series is the value at $z=1$ of a function $S_{r,n,\sigma}(z)$ which generalizes $S_{r,n }(z)$; what is missing is a Padé approximation problem of which $S_{r,n,\sigma}(z)$ would be a solution. We believe that a suitable generalisation of the problem $\mathcal{P}_{r,n}$ solved in Theorem 1 could have this property.

With this aim in view, we consider the function $S_{r,n,\sigma}(z)$ defined by $$\frac{z^{n+1}}{n!}S_{r,n,\sigma}^{(\sigma n+1)}(z) = \tilde{S}_{r,n}^{\partial}(z)$$ and $\lim_{z\to \infty} S_{r,n,\sigma} (z)=0$; in this way we have $S_{r,n,1}(z)  =  S_{r,n }(z)$ (see Eq. (eq:15bis)). We have $$S_{r,n,\sigma}(z)={\bf H}^{\sigma n+1}_{n+1,0} (\widetilde{S}_{r,n}^{\partial})(z).$$ The equality $${\bf H}^{\sigma n+1}_{n+1,0} ({\bf H}^{n+1}_{0,n+1}{\bf H}^{n+1}_{n+1,n+1})^{r+1} (\boldsymbol{1})(z)  =
(-1)^{\sigma n+1}z^{(\sigma - 1)  n } \int_0^1 u_0^{(1-\sigma)n-1}(1-u_0)^{\sigma n} \tilde{S}_{r,n}^{\partial}(z/u_0) \textup{d}u_0$$ yields, using Proposition 3: $$\begin{gathered}
S_{r,n,\sigma}(z)=(-1)^{\sigma n+1}z^{(r+\sigma)  n+r+1} \\
\times \int_{[0,1]^{2r+3}}
\frac{\displaystyle u_0^{(r-\sigma+2) n+r}(1-u_0)^{\sigma n}
\prod_{j=1}^{r+1}\big((u_jv_j)^{(r-j+2)(n+1)-1}(1-u_j)^n(1-v_j)^n\big)}
{\displaystyle \prod_{j=1}^{r+1}\big((z-u_0u_1v_1\cdots u_{j-1}v_{j-1}u_j)^{n+1}
(z-u_0u_1v_1\cdots u_{j}v_{j})^{n+1}\big)} \textup{d}{\bf u}\textup{d}{\bf v}.
\end{gathered}$$ This function has the following value at $z=1$: $$\begin{gathered}
S_{r,n,\sigma}(1) =
\\ (-1)^{\sigma n+1}  \int\limits_{[0,1]^{2r+3}}
\frac{\displaystyle u_0^{(r-\sigma+2) n+r}(1-u_0)^{\sigma n} \prod_{j=1}^{r+1}\big((u_jv_j)^{(r-j+2)(n+1)-1}(1-u_j)^n(1-v_j)^n\big)}
{\displaystyle \prod_{j=1}^{r+1}
\big((1-u_0u_1v_1\cdots u_{j-1}v_{j-1}u_j)^{n+1}(1-u_0u_1v_1\cdots u_{j}v_{j})^{n+1}\big)} \textup{d}{\bf u}\textup{d}{\bf v}.
\end{gathered}$$

Using Proposition 17 of [@fischler2] (which amounts to a change of variables) one obtains $$S_{r,n,\sigma}(1) = (-1)^{\sigma n+1}  \int\limits_{[0,1]^{a-1}} \frac{\prod_{j=1}^{a-1} x_j^{\sigma n}
(1-x_j)^n }{(1-x_1x_2\cdots x_{a-1})^{\sigma n+1} \prod_{2 \leq j \leq a-2 \atop j {\tiny \mbox{ even}}}
(1-x_1x_2\cdots x_j)^{n+1}} \textup{d}{\bf x}$$ with $a=2r+4$. Then using Zlobin's result [@zlobin] or another change of variables (namely Théorème 10 of [@fischler2]), one obtains the Vasilyev-type integral $$S_{r,n,\sigma}(1) = (-1)^{\sigma n+1}  \int\limits_{[0,1]^{a-1}} \frac{\prod_{j=1}^{a-1} x_j^{\sigma n} (1-x_j)^n
 }{ Q_{a-1}(x_1,\cdots,x_{a-1})^{\sigma n+1} }  \textup{d}{\bf x}.$$ Now Theorem 5 of [@zudilin] yields $$S_{r,n,\sigma}(1) = (-1)^{\sigma n+1} \sum_{k=1}^{\infty} (k+\frac{n}2) \frac{(k-\sigma n)_{\sigma n} (k+n+1) _{\sigma n}}{(k)_{n+1}^a}.$$ Up to a sign, this is exactly the very-well poised hypergeometric series (eqvwp).

1[]{#sec:biblio label="sec:biblio"}

R. Apéry, *Irrationalité de $\zeta(2)$ et $\zeta (3)$*, Astérisque **61** (1979), 11--13.

K. M. Ball, T. Rivoal, *Irrationalité d'une infinité de valeurs de la fonction zêta aux entiers impairs*, Invent. Math. **146**.1 (2001), 193--207.

F. Beukers, *A note on the irrationality of $\zeta(2)$ and $\zeta(3)$*, Bull. London Math. Soc. **11** (1979), 268--272.

J. Cresson, S. Fischler, T. Rivoal, *Séries hypergéométriques multiples et polyzêtas*, Bull. SMF **136**.1 (2008), 97--145.

S. Fischler, *Formes linéaires en polyzêtas et intégrales multiples*, C. R. Acad. Sci. Paris Ser. I, **335** (2002), 1--4.

S. Fischler, *Groupes de Rhin-Viola et intégrales multiples*, J. Théor. Nombres Bordeaux **15**.2 (2003), 479--534.

S. Fischler, *Irrationalité de valeurs de zêta (d'après Apéry, Rivoal, ...)*, Séminaire Bourbaki 2002-2003, no. 910 (Nov. 2002), Astérisque **294** (2004), 27--62.

S. Fischler, T. Rivoal, *Approximants de Padé et séries hypergéométriques équilibrées*, J. Math. Pures Appl. **82**.10 (2003), 1369--1394.

P. Henrici, *Applied and computational complex analysis, Vol. 2. Special functions, integral transforms, asymptotics, continued fractions*, Wiley Classics Library, John Wiley & Sons, Inc., New York, **1991**. x+662 pp.

C. Krattenthaler, T. Rivoal, *An identity of Andrews, multiple integrals, and very-well-poised hypergeometric series*, Ramanujan J. **13** (2007), vol. 1-3, 203--219.

T. Rivoal, *La fonction zêta de Riemann prend une infinité de valeurs irrationnelles aux entiers impairs*, C. R. A. S. Paris Sér. I Math. **331**.4 (2000), 267--270.

A. B. Shidlovskii, *Transcendental numbers*, De Gruyter Studies in Math. **12**.

V. N. Sorokin, *Apéry's theorem*, Vestnik Moskov. Univ. Ser. I Mat. Mekh. no. **3** (1998), 48--52 (in russian); English translation in Moscow Univ. Math. Bull. no. **3** (1998), 48--52.

V. N. Sorokin, *A transcendence measure for $\pi^2$*, Mat. Sbornik **187** (1996), 87--120 (in russian); English translation in Sb. Math. **187** (1996), 1819--1852.

D. Vasilyev, *Approximations of zero by linear forms in values of the Riemann zeta-function*, Doklady Nat. Acad. Sci Belarus **45**.5 (2001), 36--40 (in russian). Extended version in english : *On small linear forms for the values of the Riemann zeta-function at odd points*, preprint no. 1 (558), Nat. Acad. Sci. Belarus, Institute Math., Minsk (2001), 14 pages.

S. A. Zlobin, *Integrals that can be represented as linear forms of generalized polylogarithms*, Mat. Zametki **71** (2002), no. 5, 782--787 (in russian). English translation in Math. Notes **71** (2002), no. 5-6, 711--716.

S. A. Zlobin, *Generating functions for the values of a multiple zeta function*, Vestnik Moskov. Univ. Ser. I Mat. Mekh. **73** (2005), no. 2, 55--59. English translation in Moscow Univ. Math. Bull. **60** (2005), no. 2, 44--48.

W. Zudilin, *Well-poised hypergeometric service for Diophantine problems of zeta values*, J. Théor. Nombres Bordeaux **15**.2 (2003), 593--626.

S. Fischler, Équipe d'Arithmétique et de Géométrie Algébrique, Université Paris-Sud, Bâtiment 425, 91405 Orsay Cedex, France

T. Rivoal, Institut Fourier, CNRS et Université Grenoble 1, 100 rue des maths, BP 74, 38402 St Martin d'Hères Cedex, France
