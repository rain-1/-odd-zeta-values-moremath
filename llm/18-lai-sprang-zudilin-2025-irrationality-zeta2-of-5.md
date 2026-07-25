---
title: "A note on the irrationality of $ζ_2(5)$"
authors:
  - "Li Lai"
  - "Johannes Sprang"
  - "Wadim Zudilin"
arxiv_id: "2505.05005v2"
arxiv_url: "https://arxiv.org/abs/2505.05005"
published: "2025-05-08"
journal_ref: ""
doi: ""
source: "papers/18-lai-sprang-zudilin-2025-irrationality-zeta2-of-5/zeta_2_5__20260527_for_arXiv.tex"
conversion: pandoc-flat
---

# A note on the irrationality of $ζ_2(5)$

**Li Lai, Johannes Sprang, Wadim Zudilin**

## Abstract

In a spirit of Apéry's proof of the irrationality of $ζ(3)$, we construct a sequence $p_n/q_n$ of rational approximations to the $2$-adic zeta value $ζ_2(5)$ which satisfy $0 < |ζ_2(5)-p_n/q_n|_2 < \max\{|p_n|,|q_n|\}^{-1-δ}$ for an explicit constant $δ>0$. This leads to a new proof of the irrationality of $ζ_2(5)$, the result established recently by Calegari, Dimitrov and Tang using a different method. Furthermore, our approximations allow us to obtain an upper bound for the irrationality measure of this $2$-adic quantity; namely, we show that $μ(ζ_2(5)) \le (16\log2)/(8\log2-5) = 20.342\dots$.

---
# Introduction

Apéry's proof [@Ape1979] of the irrationality of $$\zeta(3)=\sum_{k=1}^\infty\frac1{k^3}$$ remains a significant attraction in number theory. One reason for this is that the rational approximations to $\zeta(3)$ used in the proof link with many other mathematics areas --- combinatorics, analysis, algebraic geometry, differential equations, integrable models, mathematical physics --- to name a few. Another reason behind this attractiveness is a recognised difficulty of proving anything beyond $\zeta(3)\notin\mathbb Q$ for the values of Riemann's zeta function and its numerous generalisations that does not follow from known transcendence results for $\pi$ and the logarithms of algebraic numbers. Some partial linear independence results for odd zeta values by Ball and Rivoal [@BR2001; @Riv2000] and by the third author [@Zud2001] consolidated the use of hypergeometric functions in constructing rational approximations to $L$-values, while the recent irrationality advancement [@{CDT2024+}] of Calegari, Dimitrov and Tang sets up promising perspectives for this field. Their proof of $L(2,\chi_{-3})\notin\mathbb Q$ in [@{CDT2024+}], the irrationality for the $L$-value attached to the Dirichlet modulo 3 character, extends existing arithmetic techniques to new horizons; at the same time it builds on essential ingredients of Apéry's proof and its later re-interpretations. The use in [@{CDT2024+}] of novel methodology of the so-called holonomicity criteria leads to further arithmetic advances including the proof of the unbounded denominators conjecture [@CDT2025] and of the irrationality for products of two logarithms; it also allows Calegari, Dimitrov and Tang [@{CDT2020+}; @{CDT2025+}] to demonstrate the irrationality of $\zeta_2(5)$, the $2$-adic analogue of $\zeta(5)$, --- a result whose Archimedean counterpart is non-existent.

Our principal goal in this note is to give a new proof of the irrationality of $\zeta_2(5)$, much in a spirit of Apéry's original proof for $\zeta(3)$, via an explicit construction of rational approximations to the 2-adic zeta value. These approximations allow us to also estimate the quality of general rational approximations to the number, that is, to give an upper bound on the irrationality measure $\mu(\zeta_2(5))$ --- below we carefully define all the objects involved. A remarkable feature of our construction is that our approximations satisfy a three-term Apéry-like recurrence relation $$(n+1)^5\rho_{n+1} - 32(2n+1)(8n^4+16n^3+20n^2+12n+3)\rho_n + 2^{16}n^5\rho_{n-1} = 0
\label{eq:rec}$$ for $n=1,2,\dots$ . Apparently, this recursion did not show up in the literature before; it admits a solution $\{\rho_0,\rho_1,\rho_2,\dots\}=\{1,96,14944,\dots\}$ which is integer-valued --- we give an explicit binomial expression for the latter. Notice that we do not expect the existence of a three-term Apéry-like recursion for the Archimedean zeta value $\zeta(5)$, though four-term recursions of this type are known [@{BZ2022+}].

To summarise, our main result is as follows.

**Theorem 1**. *The $2$-adic zeta value $\zeta_2(5)$ is irrational. Moreover, we have the following upper bound for its irrationality measure: $$\mu(\zeta_2(5)) \leqslant\frac{16\log 2}{8\log 2 - 5} = 20.342651\dotsc.$$*

# Preliminaries

## Irrationality measure

We first recall the definition of irrationality measure for real numbers.

***Definition** 2*. Let $\xi \in \mathbb{R}$. Define the *irrationality measure* of $\xi$ --- denoted by $\mu(\xi)$ --- to be the supremum of the set of real numbers $\mu$ such that $$0< \left| \xi - \frac{A}{B} \right| < \frac{1}{\max\{ |A|, |B| \}^{\mu}}$$ is satisfied by infinitely many pairs $(A,B) \in \mathbb{Z} \times \mathbb{Z}_{>0}$. Note that the supremum can be infinite; in such a case the number $\xi$ is called a Liouville number.

A classical application of the Borel--Cantelli lemma shows that $\mu(\xi) = 2$ for almost all real numbers $\xi$ in the sense of the Lebesgue measure. A deep result of Roth [@Rot1955] states that $\mu(\xi)=2$ for any irrational algebraic real number $\xi$. It is proved by Euler that $\mu(e)=2$. The exact values of $\mu(\pi)$ and $\mu(\zeta(3))$ are also expected to be 2, but we only know that $$\mu(\pi) \leqslant 7.103205\dots$$ from Zeilberger and the third author [@ZZ2020], and $$\mu(\zeta(3)) \leqslant 5.513890\dots$$ from Rhin and Viola [@RV2001].

A similar definition is available for the irrationality measure of a $p$-adic number.

***Definition** 3*. Let $p$ be a prime and $\xi \in \mathbb{Q}_p$. Define the *irrationality measure* of $\xi$ --- again denoted by $\mu(\xi)$ --- to be the supremum of the set of real numbers $\mu$ such that $$0< \left| \xi - \frac{A}{B} \right|_p < \frac{1}{\max\{ |A|, |B| \}^{\mu}}$$ is satisfied by infinitely many pairs $(A,B) \in \mathbb{Z} \times \mathbb{Z}_{>0}$.

Although not explicitly stated in the literature, the upper bounds $$\mu(\zeta_2(3)) \leqslant\frac{12\log 2}{6 \log 2 - 3} = 7.177398\dots$$ and $$\mu(\zeta_3(3)) \leqslant\frac{6\log 3}{3\log 3 -3} = 22.281447\dots$$ can be extracted from Calegari's work [@Cal2005] with the help of a lemma of Bel [@Bel2019] stated below, alternatively, from Beukers' result [@Beu2008 Theorem 11.2].

**Lemma 4** (Bel [@Bel2019 Lemme 3.2]). *Let $p$ be a prime, $\xi \in \mathbb{Q}_p$ and $\alpha, \beta$ two real numbers satisfying $\alpha > \beta > 0$. Suppose that there exist two sequences $(a_n)_{n \geqslant 1} \subset \mathbb{Z}$ and $(b_n)_{n \geqslant 1} \subset \mathbb{Z}$ such that*

-   *$|a_n + b_n \xi|_p \leqslant\exp(-\alpha n +o(n))$ as $n \to \infty$[;]*

-   *$\max\{ |a_n|, |b_n| \} \leqslant\exp(\beta n + o(n))$ as $n \to \infty$[;]*

-   *$a_nb_{n+1} - a_{n+1}b_n \ne 0$ for any $n \in \mathbb{Z}_{>0}$.*

*Then the $p$-adic number $\xi$ is irrational, with the following estimate for its irrationality measure: $$\mu(\xi) \leqslant\frac{\alpha}{\alpha - \beta}.$$*

Bel's lemma is a tool from our arsenal for proving Theorem 1.

## Volkenborn integrals

Let $p$ be a prime number. In this subsection, we will recall the definition of Volkenborn integral [@Vol1972] and its basic properties.

A function $f\colon \mathbb{Z}_p \to \mathbb{Q}_p$ is said to be *Volkenborn integrable* if the sequence $$\frac{1}{p^n} \sum_{k=0}^{p^n-1} f(k)$$ converges $p$-adically as $n \to \infty$. In this case, the value $$\int_{\mathbb{Z}_p} f(t)\,\mathrm{d}t := \lim_{n \to \infty} \frac{1}{p^n} \sum_{k=0}^{p^n-1} f(k) \in \mathbb{Q}_p$$ is called the *Volkenborn integral* of $f$.

Let $K$ be either $\mathbb{Q}_p$ or $\mathbb{Z}_p$. A function $f\colon\mathbb{Z}_p \to K$ is said to be *strictly differentiable* on $\mathbb{Z}_p$ --- denoted by $f \in S^{1}(\mathbb{Z}_p,K)$ --- if $$f(x) - f(y) = (x-y) g(x,y)$$ for some continuous function $g(x,y)$ on $\mathbb{Z}_p \times \mathbb{Z}_p$. It is known that every $f \in S^{1}(\mathbb{Z}_p,\mathbb{Q}_p)$ is Volkenborn integrable (see [@Rob2000 p. 264]). For our purposes, we note that if a rational function $f(t) \in \mathbb{Q}_p(t)$ has no pole in $\mathbb{Z}_p$, then $f \in S^{1}(\mathbb{Z}_p,\mathbb{Q}_p)$.

The Volkenborn integral has the following behaviour under translations.

**Lemma 5** ([@Rob2000 Proposition 2, p. 265]). *Let $f \in S^{1}(\mathbb{Z}_p,\mathbb{Q}_p)$. Then, for any $k \in \mathbb{Z}_{>0}$, we have $$\int_{\mathbb{Z}_p} f(t+k)\,\mathrm{d}t = \int_{\mathbb{Z}_p} f(t)\,\mathrm{d}t + \sum_{\ell=0}^{k-1} f'(\ell).$$*

For any positive integer $k$, we denote by $k_{-}$ the non-negative integer obtained by deleting the leading $p$-adic digit of $k$. In other words, if the $p$-adic expansion of $k$ assumes the form $k=a_0+a_1p+\dots+a_{l-1}p^{l-1}+a_{l}p^{l}$ with $a_l \ne 0$, then $$k_{-} = a_0+a_1p+\dots+a_{l-1}p^{l-1}.$$ For estimating the $p$-adic norm of the Volkenborn integral of a function $f \in S^{1}(\mathbb{Z}_p,\mathbb{Q}_p)$, we will use the characteristic $$\triangle(f) := \min\left\{\inf_{k \geqslant 1} v_p\left( \frac{f(k)-f(k_{-})}{k-k_{-}} \right),\, 1+v_p(f(0)) \right\} \in \mathbb{Z} \cup \{+\infty\},$$ where we take the convention that $v_p(0)=+\infty$. This was first introduced by the second author in [@Spr2020] and further developed by the first author in [@Lai2025].

We have the following properties of $\triangle$ viewed as an operator on the space $S^{1}(\mathbb{Z}_p,\mathbb{Q}_p)$.

**Lemma 6** ([@Lai2025 Lemma 2.4]). *Let $f \in S^{1}(\mathbb{Z}_p,\mathbb{Q}_p)$. Then we have $$v_p\left( \int_{\mathbb{Z}_p} f(t)\,\mathrm{d}t \right) \geqslant\triangle(f) - 1.$$*

**Lemma 7**. *The following properties hold for the operator $\triangle$.*

1.  *For any $f,g \in S^{1}(\mathbb{Z}_{p},\mathbb{Q}_{p})$, we have $$\triangle(f + g) \geqslant\min\{ \triangle(f), \triangle(g) \}.$$*

2.  *For any $f \in S^{1}(\mathbb{Z}_{p},\mathbb{Q}_{p})$ and $C \in \mathbb{Q}_p$, we have $$\triangle(C \cdot f) = \triangle(f) + v_p(C).$$*

3.  *If $f,g \in S^{1}(\mathbb{Z}_{p},\mathbb{Z}_{p})$, then $$\triangle(f\cdot g) \geqslant\min\{\triangle(f),\triangle(g)\}.$$*

4.  *If $f(t) = \sum_{j=0}^{\infty} a_jt^{j} \in \mathbb{Z}_{p}\llbracket t \rrbracket$ and $\lim_{j \to \infty} |a_j|_p = 0$, then $$\triangle(f) \geqslant 0.$$*

5.  *For $n,j \in \mathbb{Z}$ with $n>0$ and $$f(t) = \binom{t+j}{n} = \frac{(t+j)(t+j-1)\dotsb(t+j-n+1)}{n!},$$ we have $$\triangle(f) \geqslant-\left\lfloor \frac{\log n}{\log p} \right\rfloor.$$*

*Proof.* For parts (c), (d) and (e), see [@Lai2025 Lemma 2.5]; parts (a) and (b) are clear from definition. ◻

## $p$-adic zeta values

We first recall some basic facts about $p$-adic $L$-functions and $p$-adic zeta values. For a prime number $p$, define $$q_p:=\begin{cases}
        p &\text{if}\; p\ne 2,\\
        4 &\text{if}\; p=2.
    \end{cases}$$ Then $\mathbb{Q}_p^\times \cong p^{\mathbb{Z}} \cdot \mu_{\varphi(q_p)}(\mathbb{Z}_p)\times (1+q_p\mathbb{Z}_p)$ and we write $$\begin{aligned}
    \omega &\colon \mathbb{Q}_p^\times\to p^{\mathbb{Z}} \cdot \mu_{\varphi(q_p)}(\mathbb{Z}_p)\subseteq \mathbb{Q}_p^\times, \\
    \langle \,\cdot\, \rangle &\colon \mathbb{Q}_p^\times\to (1+q_p\mathbb{Z}_p) \subseteq\mathbb{Q}_p^\times
\end{aligned}$$ for the induced projections; $\omega$ is known as the *Teichmüller character*. For $s\in \mathbb{C}_p\setminus \{1\}$ with $|s|_p<q_p p^{-1/(p-1)}$ and $x\in \mathbb{Q}_p$ with $|x|_p\geqslant q_p$, we define the *$p$-adic Hurwitz zeta function* by the Volkenborn integral $$\zeta_p(s,x):=\frac{1}{s-1}\int_{\mathbb{Z}_p} \langle t+x \rangle^{1-s}\,\mathrm{d}t.$$ The *Kubota--Leopoldt $p$-adic $L$-function* associated to a Dirichlet character $\chi$ of conductor $f$ is now defined as follows: Let $M$ be a common multiple of $f$ and $q_p$; then $$L_p(s,\chi):=\frac{\langle M\rangle^{1-s}}{M}\sum_{\substack{j=0\\ p\nmid j}}^{M-1} \chi(j)\zeta_p\bigg( s,\frac{j}{M} \bigg).$$ It is not difficult to check that this definition does not depend on the choice of $M$. For more details, we refer the reader to [@Coh2007 Chap. 11]. Finally, we define $p$-adic zeta values as follows.

***Definition** 8*. For any integer $s \geqslant 2$, the *$p$-adic zeta value* $\zeta_p(s)$ is given by $$\zeta_p(s) := L_p(s,\omega^{1-s}).$$

Notice that the definitions of $\zeta_p(s)$ by Coleman [@Col1984] or Furusho [@Fur2004] differ from ours by the Euler factor $(1-p^{-s})^{-1}$ at $p$. However, for each fixed integer $s\geqslant 2$, this factor is a non-zero rational number, so it does not matter which definition is used for proving irrationality. Let us also note that Beukers in [@Beu2008] refers to $L_p(s,\chi_0)$ corresponding to the principal character $\chi=\chi_0$ as to $\zeta_p(s)$. The name of '$p$-adic zeta' is justified by the following characterisation (see [@Cal2005 Lemma 2.4]): $$\zeta_p(s) = \lim_{\substack{k\to s \;\text{$p$-adically}\\k \in \mathbb{Z}_{<0}, \; k\equiv s \;(\operatorname{mod}p-1)}} \zeta(k) \in \mathbb{Q}_p.$$ In other words, the $p$-adic zeta value $\zeta_p(s)$ is a $p$-adic limit of special values of the Riemann zeta function at negative integers; in particular, we have $\zeta_p(s)=0$ for any even positive integer $s$.

In the special case $p=2$ and $s \in \mathbb{Z}_{\geqslant 2}$, it follows from Definition 8 that $$\begin{aligned}
\zeta_2(s)
&= L_2(s,\omega^{1-s}) \notag\\
&= \frac{1}{4}\left( \omega(1)^{1-s}\zeta_2\left( s,\frac{1}{4}\right) + \omega(3)^{1-s}\zeta_2\left( s,\frac{3}{4}\right) \right) \notag\\
&= \frac{1}{4}\left( \frac{1}{s-1}\int_{\mathbb{Z}_2} \frac{\mathrm{d}t}{\langle t+1/4 \rangle^{s-1}} + \frac{(-1)^{1-s}}{s-1}\int_{\mathbb{Z}_2} \frac{\mathrm{d}t}{\langle t+3/4 \rangle^{s-1}} \right) \notag\\
&= \frac{1}{4(s-1)} \left( \int_{\mathbb{Z}_2} \frac{\mathrm{d}t}{(1+4t)^{s-1}} +  \int_{\mathbb{Z}_2} \frac{\mathrm{d}t}{(3+4t)^{s-1}}  \right) \notag\\
&= \frac{1}{4(s-1)} \bigg( \lim_{N \to \infty}  \frac{1}{2^N} \sum_{k=0}^{2^N -1} \frac{1}{(1+4k)^{s-1}} + \lim_{N \to \infty}  \frac{1}{2^N} \sum_{k=0}^{2^N -1} \frac{1}{(3+4k)^{s-1}}\bigg).
\label{271}
\end{aligned}$$ We can further translate this expression into a Volkenborn integral.

**Lemma 9**. *For any $s \in \mathbb{Z}_{\geqslant 2}$ we have $$\frac{1}{s-1}\int_{\mathbb{Z}_2} \frac{\mathrm{d}t}{(t+1/2)^{s-1}} = 2^{s} \cdot \zeta_2(s).$$*

*Proof.* We have $$\begin{aligned}
\frac{1}{s-1}\int_{\mathbb{Z}_2} \frac{\mathrm{d}t}{(t+1/2)^{s-1}}
&= \frac{2^{s-1}}{s-1} \int_{\mathbb{Z}_2} \frac{\mathrm{d}t}{(1+2t)^{s-1}} \notag\\
&= \frac{2^{s-1}}{s-1} \lim_{N \to \infty} \frac{1}{2^{N+1}} \sum_{k=0}^{2^{N+1}-1} \frac{1}{(1+2k)^{s-1}} \notag\\
&= \frac{2^{s-1}}{s-1} \lim_{N \to \infty} \frac{1}{2^{N+1}}\bigg( \sum_{k=0}^{2^N-1} \frac{1}{(1+4k)^{s-1}} + \sum_{k=0}^{2^N-1} \frac{1}{(3+4k)^{s-1}} \bigg).
\label{272}
\end{aligned}$$ Comparing (272) with (271), we obtain the result. ◻

# Rational functions and linear forms

In this section, we first introduce a sequence of rational functions. Then we make use of them to construct linear forms in $1$ and $\zeta_2(5)$. Recall that the Pochhammer symbol $(t)_n$ is defined by $(t)_{n}:=t(t+1)\cdots(t+n-1)$ for $n \in \mathbb{Z}_{>0}$ with the convention $(t)_0:= 1$.

***Definition** 10*. For $n \in \mathbb{Z}_{\geqslant 0}$, define the rational function $R_n(t) \in \mathbb{Q}(t)$ by $$R_n(t) :=  2^{8n} \cdot (2t+n) \cdot \frac{(t+1/2)_n^4}{(t)_{n+1}^4}.$$

We mention that similar choices of rational function appear in [@Bel2019; @Lai2025; @{Riv2017+}].

For a rational function $R(t)=P(t)/Q(t)$, where $P$, $Q$ are polynomials, we define the degree of $R(t)$ by $\deg R := \deg P - \deg Q$. Note that for any $n \in \mathbb{Z}_{\geqslant 0}$ we have $$\label{deg_R=-3}
\deg R_n = -3.$$ In particular, our rational function admits a partial-fraction decomposition $$\label{def_rik}
R_n(t) =: \sum_{i=1}^{4}\sum_{k=0}^{n} \frac{r_{n,i,k}}{(t+k)^i},$$ with the coefficients $r_{n,i,k} \in \mathbb{Q}$ uniquely determined by $R_n(t)$.

***Definition** 11*. For $n \in \mathbb{Z}_{\geqslant 0}$, define the following $2$-adic quantity: $$S_n :=  - \int_{\mathbb{Z}_2} R_n'\Big( t+\frac{1}{2} \Big)\,\mathrm{d}t,$$ where $R_n'(t)$ is the derivative function of $R_n(t)$ with respect to $t$.

We claim that $S_n$ is a linear form in $1$ and $\zeta_2(5)$ with rational coefficients.

**Lemma 12**. *For any $n \in \mathbb{Z}_{\geqslant 0}$, we have $$S_n = \rho_{n,0} + \rho_{n,3} \cdot \zeta_2(5),$$ where $$\begin{aligned}
\rho_{n,0} &= -\sum_{i=1}^{4}\sum_{k = 0}^{n}\sum_{\ell=1}^k \frac{i(i+1)r_{n,i,k}}{(\ell-1/2)^{i+2}} \in \mathbb{Q},
\label{def_rho_0}\\
\rho_{n,3} &= 384 \sum_{k=0}^{n} r_{n,3,k} \in \mathbb{Q}.
\label{def_rho_3}
\end{aligned}$$ The convention here and in what follows is that the empty sum [(]when $k=0$[)] is understood as $0$.*

*Proof.* By Definition 11 and Equation (def_rik), we have $$\label{341}
S_n =\sum_{i=1}^{4} \sum_{k=0}^{n} ir_{n,i,k}  \int_{\mathbb{Z}_2} \frac{\mathrm{d}t}{(t+k+1/2)^{i+1}}.$$ By Lemma 5 and Lemma 9, we have $$\begin{aligned}
\int_{\mathbb{Z}_2} \frac{\mathrm{d}t}{(t+k+1/2)^{i+1}}
&= \int_{\mathbb{Z}_2} \frac{\mathrm{d}t}{(t+1/2)^{i+1}} -(i+1)\sum_{\ell=1}^k \frac{1}{(\ell-1/2)^{i+2}} \notag\\
&= (i+1)2^{i+2}\zeta_2(i+2) -(i+1)\sum_{\ell=1}^k \frac{1}{(\ell-1/2)^{i+2}}.
\label{342}
\end{aligned}$$ Substituting (342) into (341), and using $\zeta_2(s)=0$ for even $s$, we obtain $$S_n = \rho_{n,0} + \left(16\sum_{k = 0}^{n} r_{n,1,k}\right) \cdot \zeta_2(3) + \rho_{n,3} \cdot \zeta_2(5).$$ By (def_rik) and (deg_R=-3), we have $$\sum_{k=0}^{n} r_{n,1,k} = \lim_{t \to \infty} tR_n(t) = 0.$$ Therefore, $S_n = \rho_{n,0} + \rho_{n,3} \cdot \zeta_2(5)$, as desired. ◻

***Remark** 13*. Our derivation 'secretly' corresponds to the equality $$\sum_{m=0}^{\infty} R_n''\Big(m+\frac{1}{2}\Big) = \rho_{n,0} + \rho_{n,3} \cdot \left(1 - 2^{-5} \right)\cdot \zeta(5)$$ in the Archimedean case. The coefficients $\rho_{n,0} \in \mathbb{Q}$ and $\rho_{n,3} \in \mathbb{Q}$ in this formula are exactly the same as in Lemma 12, and $\left(1 - 2^{-5} \right)\cdot \zeta(5)$ is the value of the Riemann zeta function at $s=5$ with the Euler factor at $2$ removed. This correspondence to linear forms in classical zeta values explains the motivation behind the artificial minus sign appearing in Definition 11.

# A three-term recursion for $\rho_{n,0}$ and $\rho_{n,3}$

With the help of Zeilberger's algorithm of creative telescoping [@PWZ1997 Chap. 6], we obtain the following recursion for $(R_n(t))_{n \geqslant 0}$.

**Lemma 14**. *For $n \in \mathbb{Z}_{>0}$, let $$\begin{aligned}
T_n(t)
&=\big(8(2n+1)t^4 + 48n(2n+1)t^3 + 2(2n+1)(48n^2-6n-5)t^2
\notag\\ &\quad
+ 2(80n^4 + 16n^3 - 28n^2 - 3n + 3)t
\notag\\ &\quad
+ (48n^5 - 24n^3 + 3n^2 + 4n - 1)\big)
\cdot\frac{2^{8n+4}(t-1/2)_n^4}{(t)_{n+1}^4}.
\label{def_T_n(t)}
\end{aligned}$$ Then $$\begin{gathered}
(n+1)^5 R_{n+1}(t) - 32(2n+1)(8n^4+16n^3+20n^2+12n+3) R_n(t) + 2^{16}n^5 R_{n-1}(t)
\\
= T_n(t+1) - T_n(t).
\label{001}
\end{gathered}$$*

*Proof.* Dividing both sides of (001) by $2^{8(n+1)}(t+1/2)_{n}^4 / (t)_{n+1}^4$ and clearing the denominators in the result, reduce verification of Identity (001) to a linear-algebra check of identity between two polynomials of degree at most 12 in $t$ and at most 14 in $n$. ◻

The telescoping identity for $(R_n(t))_{n \geqslant 0}$ induces the following recursive formulae for both $(\rho_{n,0})_{n \geqslant 0}$ and $(\rho_{n,3})_{n \geqslant 0}$.

**Lemma 15**.

1.  *For each $i \in \{0,3\}$, the sequence $(\rho_{n,i})_{n \geqslant 0}$ satisfies the three-term relation (eq:rec).*

2.  *For any $n \in \mathbb{Z}_{\geqslant 0}$, we have the 'determinant' formula $$\rho_{n,0}\rho_{n+1,3} - \rho_{n+1,0}\rho_{n,3} = \frac{3 \cdot2^{16n+18}}{(n+1)^5} \ne 0.$$*

*Proof.* We first prove part (a). By (def_T_n(t))), the function $T_n(t)$ is a rational function in $t$ with $\deg T_n = 0$, hence its partial-fraction decomposition assumes the form $$T_n(t) =: c_{n} + \sum_{i=1}^{4}\sum_{k=0}^n \frac{a_{n,i,k}}{(t+k)^i}$$ for some $c_n \in \mathbb{Q}$ and $a_{n,i,k} \in \mathbb{Q}$.

By Equations (001), (def_rik) and the uniqueness of partial-fraction decomposition, we obtain for $n \in \mathbb{Z}_{>0}$, any $k \in \{0,1,\dots,n+1\}$ and $i \in\{1,2,3,4\}$ that $$(n+1)^5 r_{n+1,i,k} - 32(2n+1)(8n^4+16n^3+20n^2+12n+3) r_{n,i,k} + 2^{16}n^5 r_{n-1,i,k} = a_{n,i,k-1} - a_{n,i,k},
\label{421}$$ where all the coefficients outside the eligible range vanish: $a_{n,i,-1} = a_{n,i,n+1} =0$ and $r_{n,i,n+1} =r_{n-1,i,n} =r_{n-1,i,n+1} = 0$. Taking $i=3$ in (421), summing (421) over $k \in \{0,1,\dots,n+1\}$ and using (def_rho_3), we obtain $$\label{rec_for_rho_3}
(n+1)^5\rho_{n+1,3} - 32(2n+1)(8n^4+16n^3+20n^2+12n+3)\rho_{n,3} + 2^{16}n^5\rho_{n-1,3} = 0.$$ In a different direction, using Definition 11, Equation (001), Lemma 5 and Equation (def_T_n(t))), we have $$\begin{aligned}
&
(n+1)^5 S_{n+1} - 32(2n+1)(8n^4+16n^3+20n^2+12n+3) S_n + 2^{16}n^5 S_{n-1}
\notag\\
&\; =-\int_{\mathbb{Z}_2} \Big( (n+1)^5 R_{n+1}'\Big(t +\frac{1}{2} \Big) - 32(2n+1)(8n^4+16n^3+20n^2+12n+3) R_n'\Big(t +\frac{1}{2} \Big)
\notag\\ &\;\quad
+ 2^{16}n^5 R_{n-1}'\Big(t +\frac{1}{2} \Big)  \Big) \,\mathrm{d}t \notag\\
&\; = -\int_{\mathbb{Z}_2} \Big( T_n'\Big(t +\frac{3}{2} \Big) - T_n'\Big(t +\frac{1}{2} \Big) \Big) \,\mathrm{d}t
= -T_n''\Big( \frac{1}{2} \Big)
= 0.
\label{rec_for_S_n}
\end{aligned}$$ By Lemma 12, we have $\rho_{n,0} = S_n - \rho_{n,3}\cdot\zeta_2(5)$. Therefore, Equations (rec_for_rho_3) and (rec_for_S_n) imply that the sequence $(\rho_{n,0})_{n \geqslant 0}$ satisfies the recursion (eq:rec) as well. This completes the proof of part (a).

Now we prove part (b). For $n=0$, the determinant formula is checked by a straightforward computation: since $\rho_{0,0}=0$, $\rho_{0,3}=768$, $\rho_{1,0}=-1024$, $\rho_{1,3}=73728$, we deduce that $$\rho_{0,0}\rho_{1,3} - \rho_{1,0}\rho_{0,3} = 3 \cdot 2^{18}.$$ For $n\geqslant 1$ it follows inductively by using the recursions from part (a) that $$\rho_{n,0}\rho_{n+1,3} - \rho_{n+1,0}\rho_{n,3}
=2^{16} \frac{n^5}{(n+1)^5}(\rho_{n-1,0}\rho_{n,3} - \rho_{n,0}\rho_{n-1,3}).
\qedhere$$ ◻

# Arithmetic properties

In this section, we will investigate the arithmetic properties of the coefficients $\rho_{n,i}$ of linear forms $S_n = \rho_{n,0} + \rho_{n,3} \cdot \zeta_2(5)$ as defined in Lemma 12.

In what follows, $d_n$ stands for the least common multiple of $1,2,\dots,n$ where $n \in \mathbb{Z}_{>0}$.

Note that building blocks of the rational function $R_n(t)$ are rational functions $2t+n$, $$F(t) = 2^{2n} \cdot \frac{(t+1/2)_n}{n!}
\quad\text{and}\quad
G(t) = \frac{n!}{(t)_{n+1}}.$$ Applying a somewhat standard argument based on their properties (see [@Lai2025+b Lemma 4.2] and [@Zud2004 Lemma 16]), we have $d_n^{4-i} \cdot r_{n,i,k} \in \mathbb{Z}$ for any $n \in \mathbb{Z}_{>0}$, $1 \leqslant i \leqslant 4$ and $0 \leqslant k \leqslant n$. Then, adapting the strategy of the proof of [@FSZ2019 Lemma 2] (as in [@Lai2025 Lemma 4.6]), it is elementary to establish the following inclusions.

**Lemma 16**. *For $n \in \mathbb{Z}_{>0}$, $$d_{n} \cdot \rho_{n,3} \in \mathbb{Z}
\quad\text{and}\quad
d_{n}^6 \cdot \rho_{n,0} \in \mathbb{Z}.$$*

The result of the lemma is weaker than the expectation $$\rho_{n,3} \in \mathbb{Z}
\quad\text{and}\quad
d_{n}^5 \cdot \rho_{n,0} \in \mathbb{Z}
\quad\text{for all}\; n\in\mathbb Z_{>0},
\label{den-con}$$ based on a numerical check for $n\leqslant 5000$ (using the recurrence equation (eq:rec)) and on a 'usual' behaviour of the coefficients of related linear forms in (Archimedean) zeta values. Such expectations are dubbed 'denominator conjectures' in this context, and many of them were systematically established by Krattenthaler and Rivoal in [@KR2007]. Modifying their methodology, while still making use of the famous Andrews transformation [@And1975] of terminating very-well-poised hypergeometric series into a multiple hypergeometric sum (as $q\to1$), we demonstrate below that indeed $\rho_{n,3} \in \mathbb{Z}$ for $n\in\mathbb Z_{>0}$ and a slightly weaker version of the companion inclusions in (den-con). The latter weakness does not affect the asymptotic behaviour of the denominators of $\rho_{n,0}$ as $n\to\infty$, so that our arithmetic findings are as good as required when it comes to their application for Theorem 1.

**Lemma 17**. *The solution $(\rho_n)_{n\geqslant 0}$ of the difference equation (eq:rec) with the initial conditions $\rho_0=1$, $\rho_1=96$ is given by the binomial double sum $$\rho_n=\sum_{0\leqslant i\leqslant k\leqslant n}2^{4(n-k)}{\binom{2i}i}^2\binom{2n-2i}{n-i}\binom{2k-2i}{k-i}{\binom{2k}k}^2\binom{2n-2k}{n-k}.$$ Furthermore, for the coefficients $\rho_{n,3}$ given in (def_rho_3) we have $\rho_{n,3}=768\rho_n\in\mathbb Z$ for $n\in\mathbb Z_{\geqslant 0}$.*

*Proof.* Though one can easily verify that the double sum indeed satisfies the recursion (eq:rec) with the help of multi-sum algorithms of creative telescoping, we give a human proof below, which also indicates how we arrived at the explicit expression for $\rho_n$.

We define our sequence $(\rho_n)_{n\geqslant 0}$ via the formula $$\rho_n:=\frac12\sum_{k=0}^nr_{n,3,k}=\frac12\sum_{k\in\mathbb Z}r_{n,3,k},$$ where the coefficients $r_{n,3,k}$ in the partial-fraction decomposition (def_rik) are given by $$r_{n,3,k}=\frac{\mathrm{d}}{\mathrm{d}t}\big(R_n(t)(t+k)^4\big)\Big|_{t=-k} \quad\text{for}\; k=0,1,\dots,n.$$ The inspection of this formula for $n=0$ and $1$ reveals that $\rho_0=1$ and $\rho_1=96$, while the recursion (eq:rec) for the sequence follows from $\rho_n=\rho_{n,3}/768$ (as shown in Lemma 12) and Lemma 15. Now consider the $\varepsilon$-deformation $$R_n(t;\varepsilon)=2^{8n}(2t+n+\varepsilon)\,\frac{(t+1/2)_n^2(t+\varepsilon+1/2)_n^2}{(t)_{n+1}^2(t+\varepsilon)_{n+1}^2}$$ of the function $R_n(t)$ with the motive that $$\frac{\mathrm{d}}{\mathrm{d}t}\big(R_n(t)(t+k)^4\big)
=2\frac{\partial}{\partial\varepsilon}\big(R_n(t;\varepsilon)(t+k)^2(t+\varepsilon+k)^2\big)\bigg|_{\varepsilon=0},$$ so that $$\begin{aligned}
\rho_n
&=\frac12\sum_{k=0}^n\frac{\mathrm{d}}{\mathrm{d}t}\big(R_n(t)(t+k)^4\big)\bigg|_{t=-k}
\\
&=\sum_{k=0}^n\frac{\partial}{\partial\varepsilon}\big(R_n(t;\varepsilon)(t+k)^2(t+\varepsilon+k)^2\big)\bigg|_{\varepsilon=0,\;t=-k}
\\
&=\sum_{k=0}^n\frac{\partial}{\partial\varepsilon}\big(R_n(t-k;\varepsilon)t^2(t+\varepsilon)^2\big)\bigg|_{\varepsilon=0,\;t=0}
\\
&=2^{8n}\frac{\partial}{\partial\varepsilon}\bigg(\sum_{k=0}^n
(n+\varepsilon-2k)\,\frac{(1/2-k)_n^2(\varepsilon+1/2-k)_n^2}{k!^2(n-k)!^2(1-\varepsilon)_k^2(1+\varepsilon)_{n-k}^2}
\bigg)\bigg|_{\varepsilon=0}
\\
&=2^{8n}\frac{\partial}{\partial\varepsilon}\bigg((n+\varepsilon)\frac{(\frac12)_n^2(\frac12+\varepsilon)_n^2}{n!^2(1+\varepsilon)_n^2}

\cdot
{}_9V_8(-n-\varepsilon; \, -n-\varepsilon, \, \tfrac12, \, \tfrac12, \, \tfrac12-\varepsilon, \, \tfrac12-\varepsilon, \, -n, \, -n)\bigg)\bigg|_{\varepsilon=0},
\end{aligned}$$ where the notation $$\label{eq:def-very-well-poised}
{}_{m+2}V_{m+1}(a_0;a_1,\dots,a_m)
=\sum_{k=0}^\infty\frac{(a_0+2k)\prod_{j=0}^m(a_j)_k}{a_0\,k!\prod_{j=1}^m(1+a_0-a_j)_k}$$ is used for the very-well-poised hypergeometric series evaluated at $1$.

Taking $m=2$ and $a=-n-\varepsilon$, $b_1=\frac12$, $c_1=-n-\varepsilon$, $b_2=\frac12-\varepsilon$, $c_2=-n$, $b_3=\frac12$, $c_3=\frac12-\varepsilon$ in [@KR2007 Théorème 8] we obtain the following double sum expression: $$\begin{aligned}
&
(n+\varepsilon)\frac{(\frac12)_n^2(\frac12+\varepsilon)_n^2}{n!^2(1+\varepsilon)_n^2}
\cdot{}_9V_8(-n-\varepsilon; \, -n-\varepsilon, \, \tfrac12, \, \tfrac12, \, \tfrac12-\varepsilon, \, \tfrac12-\varepsilon, \, -n, \, -n)

\\ &\quad
=(n+\varepsilon)\frac{(\frac12)_n^2(\frac12+\varepsilon)_n^2}{n!^2(1+\varepsilon)_n^2}
\cdot\frac{(-\varepsilon)\cdot(1-n-\varepsilon)_{n-1}(-n)_n}{(\frac12-n-\varepsilon)_n(\frac12-n)_n}
\\ &\quad\quad
\times
\sum_{0\leqslant i\leqslant k\leqslant n}\frac{(\frac12)_i(\frac12-\varepsilon)_i(-n)_i}{i!^2(\frac12-n-\varepsilon)_i}
\cdot
\frac{(\frac12)_{k-i}(\frac12)_k(\frac12-\varepsilon)_k(-n)_k}{(k-i)!k!(1-\varepsilon)_k(\frac12-n)_k}
\displaybreak[2]\\ &\quad
=\varepsilon\cdot\frac{(\frac12)_n^4}{n!^2(\frac12-n)_n^2}
\sum_{0\leqslant i\leqslant k\leqslant n}\frac{(\frac12)_i^2(-n)_i}{i!^2(\frac12-n)_i}
\cdot
\frac{(\frac12)_{k-i}(\frac12)_k^2(-n)_k}{(k-i)!k!^2(\frac12-n)_k}
+O(\varepsilon^2)
\displaybreak[2]\\ &\quad
=\varepsilon\sum_{0\leqslant i\leqslant k\leqslant n}\frac{(\frac12)_i^2(\frac12)_{n-i}}{i!^2(n-i)!}
\cdot
\frac{(\frac12)_{k-i}(\frac12)_k^2(\frac12)_{n-k}}{(k-i)!k!^2(n-k)!}
+O(\varepsilon^2)
\quad\text{as}\; \varepsilon\to0.
\end{aligned}$$ This implies that $$\rho_n=2^{8n}\sum_{0\leqslant i\leqslant k\leqslant n}\frac{(\frac12)_i^2(\frac12)_{n-i}}{i!^2(n-i)!}
\cdot
\frac{(\frac12)_{k-i}(\frac12)_k^2(\frac12)_{n-k}}{(k-i)!k!^2(n-k)!};$$ finally, one uses $(\frac12)_i/i!=2^{-2i}\binom{2i}{i}$ multiple times to arrive at the formula for $\rho_n$ claimed. ◻

We now focus on the sequence $(\rho_{n,0})_{n\geqslant 0}$ defined in (def_rho_0) and write it as $$\rho_{n,0} = -\sum_{\ell=1}^n \bigg(\sum_{k=\ell}^{n} \sum_{i=1}^{4} \frac{i(i+1)r_{n,i,k}}{(\ell-\frac12)^{i+2}} \bigg).
\label{def_rho_0-new}$$

**Lemma 18**. *For any prime $p>\max\{\sqrt{2n},3\}$, we have $$v_p(\rho_{n,0}) \geqslant-5.$$*

*Proof.* Since $$\begin{aligned}
\frac12\sum_{i=1}^{4} \frac{i(i+1)r_{n,i,k}}{(\ell-\frac12)^{i+2}}
&=-\frac{1}{3!} \, \frac{\mathrm{d}^3}{\mathrm{d}t^3} \bigg( R_n(t)(t+k)^4 \cdot \frac{1}{(t+k-\ell+\frac12)^3} \bigg)\bigg|_{t=-k} \\
&=-\frac{1}{3!} \, \frac{\mathrm{d}^3}{\mathrm{d}\varepsilon^3} \bigg( R_n(-k+\varepsilon)\varepsilon^4 \cdot \frac{1}{(\varepsilon-\ell+\frac12)^3} \bigg)\bigg|_{\varepsilon=0}
\displaybreak[2]\\
&=\frac{1}{3!} \, \frac{\mathrm{d}^3}{\mathrm{d}\varepsilon^3} \bigg( 2^{8n} (n-2k+2\varepsilon)(\ell-\tfrac12-\varepsilon)
\\ &\qquad\qquad\times
\frac{(\ell+\frac12-\varepsilon)_{k-\ell}^4 (\frac12-\varepsilon)_{\ell-1}^4 (\frac12+\varepsilon)_{n-k}^4}{(1-\varepsilon)_k^4(1+\varepsilon)_{n-k}^4} \bigg)\bigg|_{\varepsilon=0},
\end{aligned}$$ we obtain $$\sum_{k=\ell}^{n} \sum_{i=1}^{4} \frac{i(i+1)r_{n,i,k}}{(\ell-\frac12)^{i+2}}
=\frac13\,\frac{\mathrm{d}^3}{\mathrm{d}\varepsilon^3}T_{n,\ell}(\varepsilon)\bigg|_{\varepsilon=0},$$ where $$T_{n,\ell}(\varepsilon):=2^{8n}(\ell-\tfrac12-\varepsilon) (\tfrac12-\varepsilon)_{\ell-1}^4 \sum_{k=\ell}^n (n-2k+2\varepsilon) \frac{(\ell+\frac12-\varepsilon)_{k-\ell}^4  (\frac12+\varepsilon)_{n-k}^4}{(1-\varepsilon)_k^4(1+\varepsilon)_{n-k}^4}.$$ Using the argument in the proof of [@KR2007 Chap. 9, Corollaire 1] we recognise the sum as a limiting case of very-well-poised hypergeometric series, $$\begin{aligned}
T_{n,\ell}(\varepsilon)
&= 2^{8n}(\ell-\tfrac12-\varepsilon) (\tfrac12-\varepsilon)_{\ell-1}^4 (n-2\ell+2\varepsilon) \frac{(\frac12+\varepsilon)_{n-\ell}^4}{(1-\varepsilon)_{\ell}^4 (1+\varepsilon)_{n-\ell}^4}
\\ &\quad
\times \lim_{\delta \to 0} {}_{13}V_{12}(a; \, b_1, \, c_1, \, \dots, \, b_5, \, c_5(\delta), \, -N),
\end{aligned}$$ where we use the notation ${}_{13}V_{12}(\dots)$ for the very-well-poised hypergeometric series introduced in (eq:def-very-well-poised) with the parameters $$\begin{gathered}
    N = n-\ell, \quad
    a = -n+2\ell -2\varepsilon, \quad
    b_1=\cdots=b_4 = -n+\ell-\varepsilon, \\
    c_1=\cdots=c_4 = \ell+\tfrac{1}{2}-\varepsilon, \quad
    b_5 = 1, \quad
    c_5(\delta) = \ell+1-2\varepsilon- \delta.
\end{gathered}$$ Note that the limit $\delta \to 0$ assures that the resulting sum is finite. Applying the Andrews transformation [@KR2007 Théorème 8] leads to the quadruple-sum expression $$\begin{aligned}
T_{n,\ell}(\varepsilon) =\sum_{0 \leqslant i_1 \leqslant\dots \leqslant i_4 \leqslant n-\ell} F_{i_1,i_2,i_3,i_4}(\varepsilon),
\end{aligned}$$ where $$\begin{aligned}
F_{i_1,i_2,i_3,i_4}(\varepsilon)
&=2^{2n}  \frac{(\frac12-\varepsilon)_{\ell+i_1}(\frac12+\varepsilon)_{n-\ell-i_1}}{(1-\varepsilon)_{\ell+i_1}(1+\varepsilon)_{n-\ell-i_1}} \\ &\quad
\times2^{2n} \frac{(\ell+\frac12-\varepsilon)_{i_2}(\frac12-\varepsilon)_{\ell-1}(\frac12+\varepsilon)_{n-\ell-i_2}}{(1-\varepsilon)_{\ell+i_2}(1+\varepsilon)_{n-\ell-i_2}} \\ &\quad
\times2^{2n} \frac{(\ell+\frac12-\varepsilon)_{i_3}(\frac12-\varepsilon)_{\ell-1}(\frac12+\varepsilon)_{n-\ell-i_3}}{(1-\varepsilon)_{\ell+i_3}(1+\varepsilon)_{n-\ell-i_3}} \\ &\quad
\times (-n+\ell-1)\binom{2i_1}{i_1} \binom{2i_2-2i_1}{i_2-i_1}\binom{2i_3-2i_2}{i_3-i_2}\binom{2i_4-2i_3}{i_4-i_3}
\\ &\quad
\times \frac{\ell-2\varepsilon}{i_4+1} \cdot \frac{(\ell+1-2\varepsilon)_{i_4}}{(\ell+1-\varepsilon)_{i_4}}
\cdot 2^{2\ell} \frac{(\frac12-\varepsilon)_{\ell-1}}{(1-\varepsilon)_{\ell}}
\\ &\quad
\times 2^{2n-2\ell-2i_4} \frac{(\frac12+\varepsilon)_{n-\ell-i_4}}{(1+\varepsilon)_{n-\ell-i_4}}
\cdot\frac{(n-\ell+1-i_4)_{i_4}}{(n-\ell+1-i_4+\varepsilon)_{i_4}}.
\end{aligned}$$

We now fix a prime $p>\max\{\sqrt{2n},3\}$. Using the formula $2^{2i} \left(\frac{1}{2}\right)_i/i!=\binom{2i}{i}$ repeatedly, observe that $$\begin{aligned}
F_{i_1,i_2,i_3,i_4}(\varepsilon) |_{\varepsilon= 0}
&=-\frac{16}{(2\ell-1)^2} \, \frac{n-\ell+1}{i_4+1}
\binom{2(\ell+i_1)}{\ell+i_1}\binom{2(n-\ell-i_1)}{n-\ell-i_1}
\\ &\quad
\times \binom{2(\ell+i_2)}{\ell+i_2}\binom{2(n-\ell-i_2)}{n-\ell-i_2}
\binom{2(\ell+i_3)}{\ell+i_3}\binom{2(n-\ell-i_3)}{n-\ell-i_3}
\\ &\quad
\times \binom{2i_1}{i_1}\binom{2(i_2-i_1)}{i_2-i_1}\binom{2(i_3-i_2)}{i_3-i_2} \binom{2(i_4-i_3)}{i_4-i_3}
\\ &\quad
\times \binom{2(\ell-1)}{\ell-1}\binom{2(n-\ell-i_4)}{n-\ell-i_4}.
\end{aligned}$$ Keep in mind that $p>\sqrt{2n}$ implies, for $\ell,i_4\leqslant n$, the estimates $v_p(2\ell -1)\leqslant 1$ and $v_p(i_4+1)\leqslant 1$, so that for trivial reasons we always have $$v_p\big(  F_{i_1,i_2,i_3,i_4}(\varepsilon) |_{\varepsilon= 0} \big) \geqslant-3.$$

We claim that, for any $i_1,\dots,i_4$ such that $0 \leqslant i_1 \leqslant\dots \leqslant i_4 \leqslant n-\ell$, we have the stronger statement $$\label{claim}
v_p\big(  F_{i_1,i_2,i_3,i_4}(\varepsilon) |_{\varepsilon= 0} \big) \geqslant-2.$$ If $p \nmid (2\ell-1)$ or $p \nmid (i_4+1)$, then (claim) clearly holds; therefore, in the sequel we assume that $$p \mid (2\ell-1) \quad\text{and}\quad  p \mid (i_4+1).$$

Note that for any non-negative integer $m  \leqslant n$, we have $$p \mid \binom{2m}{m} \iff (m \bmod p) \geqslant\frac{p+1}{2},$$ where $(m \bmod p)$ is the least non-negative residue of $m$ modulo $p$.

If $(i_1 \bmod p) \geqslant\frac{p+1}{2}$, then we have $p \mid \binom{2i_1}{i_1}$, hence Claim (claim) is true. If $(i_1 \bmod p) \leqslant\frac{p-3}{2}$, then $p \mid \binom{2(\ell+i_1)}{\ell+i_1}$, validating Claim (claim) again. In the remaining situation, we have $$\begin{aligned}
i_1 \equiv \frac{p-1}{2} \;(\operatorname{mod}p), \quad
\ell \equiv \frac{p+1}{2} \;(\operatorname{mod}p) \quad\text{and}\quad
i_4 \equiv p-1 \;(\operatorname{mod}p).
\end{aligned}$$ Now, if $(n \bmod p) > \frac{p-1}{2}$, then $p \mid \binom{2(n-\ell-i_1)}{n-\ell-i_1}$, so that Claim (claim) is true. If $(n \bmod p) = \frac{p-1}{2}$, then $p \mid (n-\ell+1)$, again validating the claim. Finally, if $(n \bmod p) < \frac{p-1}{2}$, then $p \mid \binom{2(n-\ell-i_4)}{n-\ell-i_4}$, so that Claim (claim) holds true. This completes the verification of (claim).

Using the induction argument as in [@Zud2004 Lemma 17], we deduce from (claim) that $$v_p\bigg( \frac{\mathrm{d}^{\lambda}}{\mathrm{d}\varepsilon^{\lambda}} F_{i_1,i_2,i_3,i_4}(\varepsilon) \bigg|_{\varepsilon= 0} \bigg) \geqslant-2-\lambda \quad \text{for all}\; \lambda \in \mathbb{Z}_{\geqslant 0}.$$ Taking $\lambda = 3$ we conclude that the $p$-adic order of $$\sum_{k=\ell}^{n}\sum_{i=1}^{4}\frac{i(i+1)r_{n,i,k}}{(\ell -\frac{1}{2})^{i+2}}
=\frac13\sum_{0 \leqslant i_1 \leqslant\dots \leqslant i_4 \leqslant n-\ell} \frac{\mathrm{d}^3}{\mathrm{d}\varepsilon^3}F_{i_1,i_2,i_3,i_4}(\varepsilon)\bigg|_{\varepsilon= 0}$$ is at least $-5$ for any $\ell\in\{1,2,\dots,n\}$. Finally, application of Equation (def_rho_0-new) completes the proof for the $p$-adic order of $\rho_{n,0}$. ◻

**Lemma 19**. *For any $n \in \mathbb{Z}_{>0}$, we have $$\Phi_n^{-1} d_n^6 \cdot \rho_{n,0} \in \mathbb{Z},$$ where $\Phi_n$ denotes the following product over primes: $$\Phi_n = \prod_{\max\{\sqrt{2n},3\}<p \leqslant n} p.$$*

*Proof.* This follows from Lemmas 16 and 18. ◻

Finally, notice consequences of the prime number theorem: $$d_n = e^{n + o(n)} \quad\text{and}\quad
\Phi_n = e^{n + o(n)} \quad\text{as}\; n \to \infty.
\label{eq:PNT}$$ This makes the loss in Lemma 19 vs the expectation (den-con) asymptotically negligible.

# Asymptotic estimates

**Lemma 20**. *We have $$\max\{ |\rho_{n,0}|, |\rho_{n,3}| \} \leqslant 2^{8n+o(n)} \quad \text{as}\; n \to \infty.$$*

*Proof.* By Lemma 15 both sequences of the coefficients satisfy the same difference equation (eq:rec) whose characteristic polynomial $\lambda^2-2^9\lambda+2^{16}$ has double zero $\lambda=2^8$. By the classical Poincaré theorem we conclude that $\limsup_{n\to\infty}|\rho_{n,i}|^{1/n}\leqslant 2^8$ for both $i=0,3$; this implies the desired claim. ◻

**Lemma 21**. *We have $$|S_n|_2 \leqslant 2^{-16n+o(n)} \quad\text{as}\; n \to \infty.$$*

*Proof.* From Definition 10) we have $$R_n\Big( t+\frac{1}{2} \Big) = 2^{12n+4} \cdot g(t) \cdot \prod_{j=1}^{n} \left( t+j \right)^4,
\quad\text{where}\;
g(t) = \frac{2t+n+1}{\prod_{j=0}^{n} \left( 2t+2j+1 \right)^4}.$$ By the Leibniz rule we deduce $$\begin{aligned}
R_n'\Big( t+\frac{1}{2} \Big)
&= 2^{12n+4}  \cdot g'(t) \cdot \prod_{j=1}^{n} ( t+j)^4 \\
&\quad
+ 2^{12n+4}  \cdot g(t) \cdot 4 \cdot \sum_{j=1}^{n} (t+j)^3 \prod_{\substack{1 \leqslant k \leqslant n\\ k \ne j}} (t+k)^4 \\
&=2^{12n+4} n!^4 \cdot g'(t) \cdot \binom{t+n}{n}^4 \\
&\quad
+ 2^{12n+6} n!^3 \cdot g(t) \cdot \binom{t+n}{n}^3 \sum_{j=1}^{n} (j-1)! (n-j)! \binom{t+j-1}{j-1} \binom{t+n}{n-j}.
\end{aligned}$$ By part (d) of Lemma 7, we have $\triangle(g) \geqslant 0$ and $\triangle(g') \geqslant 0$. By part (e), $$\begin{gathered}
\triangle\left( \binom{t+n}{n} \right) \geqslant-\frac{\log n}{\log 2}, \\
\triangle\left( \binom{t+j-1}{j-1} \right) \geqslant-\frac{\log n}{\log 2} \quad\text{and}\quad
\triangle\left( \binom{t+n}{n-j} \right) \geqslant-\frac{\log n}{\log 2}
\end{gathered}$$ for $j \in \{1,2,\dots,n\}$. Therefore, by part (c) of the lemma we obtain $$\begin{aligned}
\triangle\bigg( g'(t) \cdot \binom{t+n}{n}^4 \bigg) &\geqslant-\frac{\log n}{\log 2}, \\
\triangle\bigg( g(t) \cdot \binom{t+n}{n}^3\binom{t+j-1}{j-1} \binom{t+n}{n-j}  \bigg) &\geqslant-\frac{\log n}{\log 2}
\end{aligned}$$ for $j \in \{1,2,\dots,n\}$. Now notice that $$\begin{aligned}
v_2(n!) \geqslant n - \frac{\log (n+1)}{\log 2} \quad\text{and}\quad
v_2((j-1)!(n-j)!) \geqslant n - 1 - \frac{2 \log (n+1)}{\log 2}
\end{aligned}$$ for such $j$. Thus, by parts (a), (b) of Lemma 7 we obtain $$\triangle\Big( R_n'\Big( t+\frac{1}{2} \Big) \Big) \geqslant 16n + 4 - \frac{6\log(n+1)}{\log 2}.$$ Finally, by Definition 11 and Lemma 6, we have $$v_2(S_n) \geqslant\triangle\Big( R_n'\Big( t+\frac{1}{2} \Big) \Big) - 1
\geqslant 16n + 3  -\frac{6\log(n+1)}{\log 2},$$ which implies the asymptotics claimed. ◻

# Proof of the main theorem

*Proof of Theorem [1].* For any $n \in \mathbb{Z}_{>0}$, define $$\widehat{S}_n := \Phi_n^{-1}d_n^6 \cdot S_n.$$ By Lemma 12, Lemma 16 and Lemma 19 we have $$\widehat{S}_n = a_n + b_n \zeta_2(5),
\quad\text{where}\;\;
a_n = \Phi_n^{-1}d_n^6 \cdot \rho_{n,0} \in \mathbb{Z}, \;
b_n = \Phi_n^{-1}d_n^6 \cdot \rho_{n,3} \in \mathbb{Z}.$$ Furthermore, by Lemma 15 (b), $$a_n b_{n+1} - a_{n+1}b_n \neq 0 \quad \text{for all}\; n \in \mathbb{Z}_{>0}.$$ Note that $v_2(\Phi_n^{-1}d_n^6) = O(\log n)$ as $n \to \infty$. By Lemma 21, we obtain $$|\widehat{S}_n|_2 \leqslant\exp(-\alpha n + o(n)) \quad\text{as}\; n \to \infty,$$ where $\alpha = 16\log 2$. By Lemma 20 and Equations (eq:PNT), we have $$\max\{ |a_n|, |b_n| \} \leqslant\exp(\beta n + o(n)) \quad \text{as}\; n \to \infty,$$ where $\beta = 8\log 2 + 5$. Since $\alpha > \beta >0$, we conclude that $\zeta_2(5)$ is irrational. Finally, from Lemma 4 we deduce the estimate $$\mu(\zeta_2(5)) \leqslant\frac{\alpha}{\alpha-\beta} = \frac{16\log 2}{8\log 2 - 5} = 20.342651\dots$$ for the irrationality measure. ◻

# Final remarks

The existing provable instances of 'denominator conjectures' concerning the denominators of coefficients of certain linear forms in zeta values, suggest that expectation (den-con) can be achieved in a transparent way, that is, via a different representation of linear forms from Lemma 12 for which one can deduce the inclusions in (den-con) 'straight away', without separate manipulations for the coefficients $\rho_{n,0}$ and $\rho_{n,3}$ only. Such a different representation is expected to be a multiple hypergeometric sum, at least a double sum as Lemma 17 hints at. It may still be a cumbersome task to make such a transparency simple --- one can foretaste the potentials from a related treatment of linear forms in $1$ and $\zeta(4)$ in [@MZ2020 Sect. 3].

Our proof of the irrationality of $\zeta_2(5)$ alone can be lightened through avoiding the use of Lemma 18 (and of Lemma 17). Already from Lemma 16 and Lemma 15 (a) one finds out that $\Psi_n\rho_{n,i}\in\mathbb Z$ for $n\in\mathbb Z_{>0}$ and $i\in\{0,3\}$, where $\Psi_n=\gcd(d_n^6,n!^5)$ behaves asymptotically as $\exp(5.5n+o(n))$ as $n\to\infty$. Since $8\log 2 + 5.5 < 16\log 2$, the conclusion $\zeta_2(5)\notin\mathbb Q$ still holds but the corresponding estimate for $\mu(\zeta_2(5))$ is not worth a mention.

Speaking about the irrationality measure for $\zeta_2(5)$ and also for the related $p$-adic zeta values $\zeta_2(3),\zeta_3(3)$, our construction in this note and the earlier ones in [@Beu2008; @Cal2005; @Lai2025] exploit exclusively the so-called totally symmetric hypergeometric approximations (or their equivalents). It may certainly be of interest to take a step further and investigate more general hypergeometric series leading to rational approximations that depend not only on $n\in\mathbb Z_{\geqslant 0}$ but on multiple integer parameters. Such generalisations are amenable to additional arithmetic manipulations, for example, to the use of the arithmetic group method as developed in the works of Rhin and Viola [@RV2001]; see further examples in [@{BZ2022+}; @MZ2020].

In a different direction, the recursion (eq:rec) is ultimately linked with the theory of Calabi--Yau differential operators [@AZ2006; @vSt2018] and --- potentially --- with geometry of Calabi--Yau three- and fourfolds. Algebraic varieties whose periods are associated with irrationality proofs are known to be particularly 'minimalistic' (for example, in the sense of level or conductor) --- one can find recent examples of such connection in [@vSt2021].

Finally, it seems evident that the Volkenborn integral of a rational function is a hypergeometric object deserving investigation on its own, especially from the point of view of summation and transformation formulae. At the moment, manipulations with linear forms in the values of $p$-adic zeta functions are performed hypergeometrically at the level of their coefficients, as the forms themselves are not compatible with their Archimedean 'traditional-hypergeometric' companions --- our Remark 13 illustrates well this discrepancy. On the other hand, one can show that the two integrals $$\begin{aligned}
{2}
S_n^{(\mathrm{L})}
&:= -\int_{\mathbb{Z}_2} R_n^{(\mathrm{L})}(t+\tfrac{1}{4}) \,\mathrm{d}t
=\rho_{n,0}^{(\mathrm{L})} + \rho_{n,2}^{(\mathrm{L})} \zeta_2(3),
&\quad\text{where}\;
R_n^{(\mathrm{L})}(t) &:= 2^{6n} \frac{(t+3/4)_n^2}{(t)_{n+1}^2}
\\ \intertext{(the special case $s=0$ of \cite[Theorem 1.5]{Lai2025}), and}
S_n^{(\mathrm{B})}
&:= -\int_{\mathbb{Z}_2} R_n^{(\mathrm{B})}(t+\tfrac{1}{2}) \,\mathrm{d}t
=\rho_{n,0}^{(\mathrm{B})} + \rho_{n,2}^{(\mathrm{B})} \zeta_2(3),
&\quad\text{where}\;
R_n^{(\mathrm{B})}(t) &:= 2^{6n} (2t+n) \frac{(t+1/2)_n^3}{(t)_{n+1}^3},
\end{aligned}$$ correspond to the *same* linear forms in $1$ and $\zeta_2(3)$. (These linear forms also coincide essentially with those constructed in [@Cal2005] and [@Beu2008] by other means.) It is natural to expect a hypergeometric-type identity for the Volkenborn integrals behind the coincidence $S_n^{(\mathrm{L})}=S_n^{(\mathrm{B})}$.

***Acknowledgements** 1*. We are indebted to the anonymous referee for their enthusiastic report on this note and creative feedback.

vietnamese The first author thanks Di\~m My for inspiring him at H\` Chí Minh City. He is supported by Research Foundation for Scholars of Xiamen University X2450218.

The second author gratefully acknowledges the support through the DFG funded Collaborative Research Center SFB 1085 'Higher Invariants'. The third author thanks the Institut des Hautes Études Scientifiques (Bures-sur-Yvette, France) and the Max-Planck Institute for Mathematics (Bonn, Germany) for hospitality and support during his stays in March 2025 and April--June 2025, respectively; his work on this project was fully performed during these stays.

99

G. Almkvist and W. Zudilin, *Differential equations, mirror maps and zeta values*, in: Mirror Symmetry V, N. Yui, S.-T. Yau and J. D. Lewis (eds.), AMS/IP Stud. Adv. Math. **38** (International Press & Amer. Math. Soc., Providence, R.I., 2006), 481--515.

G. E. Andrews, *Problems and prospects for basic hypergeometric functions*, Theory and application of special functions, R. A. Askey (ed.), Math. Res. Center, Univ. Wisconsin, Publ. No. 35 (Academic Press, New York, 1975), 191--224.

R. Apéry, *Irrationalité de $\zeta(2)$ et $\zeta(3)$*, in: Journées Arithmétiques (Luminy, 1978), Astérisque **61** (Soc. Math. France, Paris, 1979), 11--13.

K. Ball et T. Rivoal, *Irrationalité d'une infinité de valeurs de la fonction zêta aux entiers impairs*, Invent. Math. **146** (2001), 193--207.

P. Bel, *Irrationalité des valeurs de $\zeta_p(4,x)$*, J. Théor. Nombres Bordeaux **31** (2019), no. 1, 81--99.

F. Beukers, *Irrationality of some $p$-adic $L$-values*, Acta Math. Sin. (Engl. Ser.) **24** (2008), no. 4, 663--686.

F. Brown and W. Zudilin, *On cellular rational approximations to $\zeta(5)$*, Preprint [`arXiv:2210.03391v3 [math.NT]`](https://arxiv.org/abs/2210.03391v3) (2026), 32 pages.

F. Calegari, *Irrationality of certain $p$-adic periods for small $p$*, Int. Math. Res. Not. (2005), no. 20, 1235--1249.

F. Calegari, V. Dimitrov and Y. Tang, *$p$-adic Eisenstein series, arithmetic holonomicity criteria, and irrationality of the $2$-adic period $\zeta_2(5)$*, <https://people.maths.ox.ac.uk/newton/lnts/VDimitrov-LNT.pdf> (2020).

F. Calegari, V. Dimitrov and Y. Tang, *The linear independence of $1$, $\zeta(2)$, and $L(2,\chi_{-3})$*, Preprint [`arXiv:2408.15403v2 [math.NT]`](https://arxiv.org/abs/2408.15403v2) (2024), 218 pages.

F. Calegari, V. Dimitrov and Y. Tang, *The unbounded denominators conjecture*, J. Amer. Math. Soc. **38** (2025), no. 3, 627--702.

F. Calegari, V. Dimitrov and Y. Tang,

*Arithmetic holonomy bounds and effective Diophantine approximation*, Preprint [`arXiv:2510.04156v1 [math.NT]`](https://arxiv.org/abs/2510.04156v1) (2025), 20 pages.

H. Cohen, *Number Theory, Vol. 2: Analytic and Modern Tools*, Grad. Texts in Math. **240** (Springer, New York, 2007).

R. F. Coleman, *Dilogarithms, regulators and $p$-adic $L$-functions*, Invent. Math. **69** (1982), no. 2, 171--208.

S. Fischler, J. Sprang and W. Zudilin, *Many odd zeta values are irrational*, Compos. Math. **155** (2019), no. 5, 938--952.

H. Furusho, *$p$-adic multiple zeta values I: $p$-adic multiple polylogarithms and the $p$-adic KZ equation*, Invent. Math. **155** (2004), no. 2, 253--286.

C. Krattenthaler and T. Rivoal, *Hypergéométrie et fonction zêta de Riemann*, Mem. Amer. Math. Soc. **186** (2007), no. 875, x + 87 pp.

L. Lai, *On the irrationality of certain $2$-adic zeta values*, Int. J. Number Theory **21** (2025), no. 1, 207--235.

L. Lai, *Small improvements on the Ball--Rivoal theorem and its $p$-adic variant*, Preprint [`arXiv:2407.14236v2 [math.NT]`](https://arxiv.org/abs/2407.14236v2) (2025), 51 pages.

R. Marcovecchio and W. Zudilin, *Hypergeometric rational approximations to $\zeta(4)$*, Proc. Edinburgh Math. Soc. **63** (2020), no. 2, 374--397.

M. Petkovšek, H. S. Wilf and D. Zeilberger, *$A = B$* (A. K. Peters, Ltd., Wellesley, M.A., 1997).

G. Rhin and C. Viola, *The group structure for $\zeta(3)$*, Acta Arith. **97** (2001), no. 3, 269--293.

T. Rivoal, *La fonction zêta de Riemann prend une infinité de valeurs irrationnelles aux entiers impairs*, C. R. Acad. Sci. Paris Sér. I Math. **331** (2000), no. 4, 267--270.

T. Rivoal, *Padé type approximants of Hurwitz zeta functions $\zeta(4,x)$*, Preprint <https://hal.science/hal-01584731v2> (2018), 11 pages.

A. M. Robert, *A course in $p$-adic analysis*, Graduate Texts in Mathematics **198** (Springer-Verlag, New York, 2000).

K. F. Roth, *Rational approximations to algebraic numbers*, Mathematika **2** (1955), 1--20; corrigendum, 168.

J. Sprang, *Linear independence result for $p$-adic $L$-values*, Duke Math. J. **169** (2020), no. 18, 3439--3476.

D. van Straten, *Calabi--Yau operators*, in: Uniformization, Riemann--Hilbert correspondence, Calabi--Yau manifolds & Picard--Fuchs equations, Adv. Lect. Math. **42** (International Press, Somerville, MA, 2018), 401--451.

D. van Straten, *Rank four Calabi--Yau motives of low conductor*, in: Moduli spaces and modular forms (Oberwolfach Report, MFO, 2021), 335--344.

A. Volkenborn, *Ein $p$-adisches Integral und seine Anwendungen, I*, Manuscripta Math. **7** (1972), 341--373.

D. Zeilberger and W. Zudilin, *The irrationality measure of $\pi$ is at most $7.103205334137\dots$ *, Mosc. J. Combin. Number Theory **9** (2020), no. 4, 407--419.

W. Zudilin, *One of the numbers $\zeta(5)$, $\zeta(7)$, $\zeta(9)$, $\zeta(11)$ is irrational*, Uspekhi Mat. Nauk \[Russian Math. Surveys\] **56** (2001), no. 4, 149--150 \[774--776\].

W. Zudilin, *Arithmetic of linear forms involving odd zeta values*, J. Théor. Nombres Bordeaux **16** (2004), no. 1, 251--291.

L. L.: School of Mathematical Sciences, Xiamen University, Fujian, China\
*E-mail address*: [`lilaimath@gmail.com`](mailto:lilaimath@gmail.com)

J. S.: Department of Mathematics, University of Duisburg-Essen, Essen, Germany\
*E-mail address*: [`johannes.sprang@uni-due.de`](mailto:johannes.sprang@uni-due.de)

W. Z.: IMAPP, Radboud University Nijmegen, The Netherlands &\
Max-Planck Institute for Mathematics, Bonn, Germany\
*E-mail address*: [`w.zudilin@math.ru.nl`](mailto:w.zudilin@math.ru.nl)
