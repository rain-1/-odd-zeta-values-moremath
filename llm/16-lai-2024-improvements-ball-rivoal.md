---
title: "Small improvements on the Ball-Rivoal theorem and its $p$-adic variant"
authors:
  - "Li Lai"
arxiv_id: "2407.14236v2"
arxiv_url: "https://arxiv.org/abs/2407.14236"
published: "2024-07-19"
journal_ref: ""
doi: ""
source: "papers/16-lai-2024-improvements-ball-rivoal/Small_improvements_on_the_Ball-Rivoal_theorem_and_its__p_-adic_variant.tex"
conversion: pandoc-flat
---

# Small improvements on the Ball-Rivoal theorem and its $p$-adic variant

**Li Lai**

## Abstract

We prove that the dimension of the $\mathbb{Q}$-linear span of $1,ζ(3),ζ(5),\ldots,ζ(s-1)$ is at least $(1.119 \cdot \log s)/(1+\log 2)$ for any sufficiently large even integer $s$. This slightly refines a well-known result of Rivoal (2000) or Ball-Rivoal (2001). Quite unexpectedly, the proof only involves inserting the arithmetic observation of Zudilin (2001) into the original proof of Ball-Rivoal. Although this result is covered by a recent development of Fischler (2021+), our proof has the advantages of being simple and providing explicit non-vanishing small linear forms in $1$ and odd zeta values. Moreover, we establish the $p$-adic variant: for any prime number $p$, the dimension of the $\mathbb{Q}$-linear span of $1,ζ_p(3),ζ_p(5),\ldots,ζ_p(s-1)$ is at least $(1.119 \cdot \log s)/(1+\log 2)$ for any sufficiently large even integer $s$. This is new, it slightly refines a result of Sprang (2020).

---
# Introduction

The arithmetic nature of special values of the Riemann zeta function $\zeta(\cdot)$ has attracted much attention. The values of $\zeta(\cdot)$ at positive even integers are well understood due to Euler, who showed that $\zeta(2k)$ is a non-zero rational multiple of $\pi^{2k}$ for any positive integer $k$. In contrast, the values of $\zeta(\cdot)$ at positive odd integers greater than one (referred to as *odd zeta values* for brevity) are more mysterious. It is conjectured that $\pi$ and all the odd zeta values are algebraically independent over $\mathbb{Q}$. Toward this conjecture, Rivoal in 2000 (or Ball-Rivoal in 2001) made the following breakthrough:

**Theorem 1** (Rivoal [@Riv2000], 2000; Ball-Rivoal [@BR2001], 2001). *We have $$\dim_\mathbb{Q}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta(3),\zeta(5),\ldots,\zeta(s) \right) \geqslant \frac{1-o(1)}{1+\log 2} \cdot \log s,$$ as the odd integer $s \to +\infty$.*

Sprang in 2020 established the $p$-adic version of the Ball-Rivoal theorem. He proved that:

**Theorem 2** (Sprang [@Spr20], 2020). *Let $p$ be any prime number. We have $$\dim_\mathbb{Q}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta_p(3),\zeta_p(5),\ldots,\zeta_p(s) \right) \geqslant \frac{1-o(1)}{2(1+\log 2)} \cdot \log s,$$ as the odd integer $s \to +\infty$.*

Here $\zeta_p(s)$ (for an odd integer $s>1$) is the $p$-adic zeta value. We will recall basic facts about $p$-adic zeta values in Section 7. Note that there is an extra $1/2$ factor in Sprang's theorem comparing to the Ball-Rivoal theorem. Sprang had removed this extra $1/2$ factor in an unpublished work.

The proof of the Ball-Rivoal theorem involves explicit rational functions defined as follows: $$R_n(t) = n!^{s-2r} \cdot \frac{(t-rn)_{rn} \cdot (t+n+1)_{rn}}{(t)_{n+1}^{s}}, \quad n=2,4,6,\ldots,$$ where $r=\lfloor s/\log^2 s\rfloor$ is a positive integer, and $(x)_{k}=x(x+1)(x+2)\cdots(x+k-1)$ denotes the Pochhammer symbol. The quantity $S_n = D_n^{s} \cdot \sum_{\nu=1}^{+\infty} R_n(\nu)$ represents a linear form in $1$ and odd zeta values with integer coefficients, where $D_n$ is the least common multiple of $1,2,\ldots,n$.

Zudilin in 2001 made an observation [@Zud2001] that if we consider different lengths for each Pochhammer symbol appearing in $R_n(t)$, then the coefficients of the resulting linear form have a large common divisor $\Phi_n$. Specifically, Zudilin considered rational functions of the form: $$\begin{aligned}
R_n(t) =&~ (\text{some factor})\cdot(2t+Mn) \\
&\times \frac{\prod_{j=1}^{b}(t-rn)_{(r+\delta_{-j})n} \cdot (t+(M-\delta_{-j})n+1)_{(r+\delta_{-j})n}}{\prod_{j=1}^{s} (t+\delta_jn)_{(M-2\delta_j)n+1}},
\end{aligned}$$ where $s$, $b$, $r$ and $M$ are positive integers satisfying certain parity conditions, and $\delta_{-b}$, $\ldots$, $\delta_{-1}$, $\delta_{1}$, $\ldots$, $\delta_{s}$ are non-negative integers such that $0 \leqslant \delta_{-b} \leqslant \cdots \leqslant \delta_{-1} \leqslant \delta_{1} \leqslant \cdots \leqslant \delta_{s} < M/2$. Then the quantity $S_n = D_{M_1n}^{b}\prod_{j=2}^{s} D_{M_jn} \cdot \sum_{\nu=1}^{+\infty} R_n^{(b-1)}(\nu)$ can be expressed as a linear form in $1$ and odd zeta values with integer coefficients. Here, $D_{M_jn}$ denotes the least common multiple of $1,2,\ldots,M_jn$, and $M_j= \max\{ M-2\delta_1,~M-\delta_j\}$. The coefficients of the linear form have a large common divisor $\Phi_n$. The presence of $\Phi_n$ plays a crucial role in the proof of Zudilin's remarkable theorem [@Zud2001], which states that at least one of $\zeta(5), \zeta(7), \zeta(9), \zeta(11)$ is irrational. It is worth noting that the irrationality of $\zeta(3)$ was proved by Apéry [@Ap1979] in 1979, while the irrationality of $\zeta(5)$ remains an open problem.

For a considerable period, it was expected that Zudilin's $\Phi_n$ factor would have a negligible impact on asymptotic results as $s \to +\infty$. The aim of the current paper is to demonstrate that this previous expectation is inaccurate. In fact, we discover that the $\Phi_n$ factor arising from the denominator of the rational function does have an asymptotic impact. By incorporating Zudilin's $\Phi_n$ factor method into the original proofs of the Ball-Rivoal theorem and Sprang's theorem, we establish the following two results, which serves as the main theorems of the current paper:

**Theorem 1**. *For any sufficiently large even integer $s \geqslant s_0$, we have $$\dim_\mathbb{Q}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta(3),\zeta(5),\ldots,\zeta(s-1) \right) \geqslant \frac{1.009}{1+\log 2}\cdot \log s.$$*

**Theorem 2**. *Let $p$ be any prime number. For any sufficiently large even integer $s \geqslant s_0(p)$, we have $$\dim_\mathbb{Q}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta_p(3),\zeta_p(5),\ldots,\zeta_p(s-1) \right) \geqslant \frac{1.009}{1+\log 2}\cdot \log s.$$*

We remark that the proofs of Theorem 1 and Theorem 2 are programming-free; that is, they avoid the help of computer programming. The $\Phi_n$ factor has the asymptotic estimate $\Phi_n = \exp(\varpi n + o(n))$ as $n \to +\infty$, where $\varpi$ is a computable constant. Usually determining $\varpi$ requires a huge mount of computation. For Theorem 1 and Theorem 2, we use very simple parameters to avoid computer assistance. On the other hand, with the help of computer programming, we can improve the constant $1.009$ to $1.119$ by using complicated parameters. We state the result in the following:

**Claim 3**. *For any sufficiently large even integer $s \geqslant s_0^{\prime}$, we have $$\dim_\mathbb{Q}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta(3),\zeta(5),\ldots,\zeta(s-1) \right) \geqslant \frac{1.119356}{1+\log 2}\cdot \log s.$$ For any prime number $p$, for any sufficiently large even integer $s \geqslant s_0^{\prime}(p)$, we have $$\dim_\mathbb{Q}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta_p(3),\zeta_p(5),\ldots,\zeta_p(s-1) \right) \geqslant \frac{1.119356}{1+\log 2}\cdot \log s.$$*

Note that $1/(1+\log 2) = 0.590\ldots$ and $1.119356/(1+\log 2) = 0.661\ldots$.

Meanwhile, we obtain a by-product result:

**Claim 4**. *We have $$\dim_\mathbb{Q}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta(3),\zeta(5),\ldots,\zeta(75) \right) \geqslant 3.$$*

The proofs of Claim 3 and Claim 4 involve time-consuming calculations (by computer programming). It is not reasonable to require the referee to check the correctness of these time-consuming calculations, since the main idea of this paper has already been conveyed by Theorem 1 and Theorem 2. So we state Claim 3 and Claim 4 as claims rather than theorems. However, we will mention some other simple parameters in Section 13 that improve the constant $1.009$ in Theorem 1 and Theorem 2.

We would like to emphasize that Theorem 1 is subsumed in a result of Fischler, as stated below (but Theorem 2 is new):

**Theorem 3** (Fischler[@{Fis2021+}], 2021+). *For any sufficiently large odd integer $s$, we have $$\dim_\mathbb{Q}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta(3),\zeta(5),\ldots,\zeta(s) \right) \geqslant 0.21 \cdot \sqrt{\frac{s}{\log s}}.$$*

One notable aspect of Fischler's work is the use of non-explicit rational functions. Due to their non-explicity, proving certain non-vanishing property becomes challenging. Fischler overcame this difficulty by employing a generalized version of Shidlovsky's lemma. In contrast, our proof of Theorem 1 relies on explicit rational functions, making it straightforward to establish the required non-vanishing property.

For the $p$-adic case, our proof of Theorem 2 also relies on explicit rational functions. But the corresponding non-vanishing property is not obvious; it is proved in a delicate way.

## Notations

Throughout this paper, the letters $p$ and $q$ always denote prime numbers. As usual, the notations $\mathbb{Z}_p$, $\mathbb{Q}_p$ and $\mathbb{C}_p$ denote the ring of $p$-adic integers, the field of $p$-adic numbers and the completion of an algebraic closure of $\mathbb{Q}_p$, respectively. We use $v_p(x)$ to denote the $p$-adic order of $x$, normalized by $v_p(p)=1$. The $p$-adic norm is defined by $|x|_p = p^{-v_p(x)}$. The notation $|y|$ denotes the Archimedean norm of $y$. The function $\log(\cdot)$ always denotes the natural logarithm (with respect to the base $e = 2.718\ldots$). The function $\log_p(\cdot)$ denotes the $p$-adic logarithm, which is defined by $$\log_p(1+x) := \sum_{k=1}^{+\infty} \frac{(-1)^{k-1}}{k} x^k, \quad |x|_p < 1, ~ x \in \mathbb{C}_p.$$

We use the standard asymptotic notations $O$, $o$, and $\sim$. For two real-valued functions $f(x)$ and $g(x)$, the expressions $f(x)=O(g(x))$, $f(x)=o(g(x))$, and $f(x) \sim g(x)$ mean that $|f(x)| \leqslant Cg(x)$ for some constant $C$, $\lim f(x)/g(x) =0$, and $\lim f(x)/g(x) = 1$, respectively.

For any positive integer $m$, we use $D_m$ to denote the least common multiple of $1,2,\ldots,m$. The Pochhammer symbol $(x)_m$ is defined by $$(x)_m := x(x+1)\cdots(x+m-1),$$ with the convention $(x)_0 := 1$. The Euler totient function is denoted by $\varphi(\cdot)$. The notation $\phi(\cdot)$ is used to denote some other function in this paper.

## An outline of the proof of Theorem 1

In this subsection, we provide a brief outline of the proof of Theorem 1. The reader who is familiar with the works of Ball-Rivoal and Zudilin will quickly recognize that our proof follows by incorporating Zudilin's $\Phi_n$ factor method [@Zud2001] into the original proof of Ball-Rivoal [@BR2001].

Let $s$ be a sufficiently large even integer, and take $r = \lfloor s/\log^2 s \rfloor$. Consider the rational functions: $$\begin{aligned}
    R_n(t) = &\frac{(6n)!^{s/2}(4n)!^{s/2}}{n!^{2r}} \cdot (t+3n) \notag\\
    & \times \frac{(t-rn)_{rn} \cdot (t+6n+1)_{rn}}{ (t)_{6n+1}^{s/2} \cdot (t+n)_{4n+1}^{s/2} }, \quad n=1,2,3\ldots,
\end{aligned}$$

Using similar arguments as in [@BR2001] and [@Zud2004], we have the following list of lemmas:

-   The quantity $S_n = \sum_{\nu=1}^{+\infty} R_n(\nu)$ can be expressed as a linear form in $1$ and odd zeta values with rational coefficients: $$S_n = \rho_0 + \sum_{3 \leqslant i \leqslant s-1 \atop i \text{~odd~}} \rho_i \zeta(i).$$

-   We have $\Phi_n^{-s/2}D_{6n}^s \cdot \rho_i \in \mathbb{Z}$ for all $i=0,3,5,\ldots,s-1$, provided that $n>s^2$. Here $\Phi_n$ is a product of certain primes: $$\Phi_n =  \prod_{\sqrt{6n} < q \leqslant 6n \atop q \text{~prime~}} q^{\phi(n/q)},$$ with the function $$\begin{aligned}
         \phi(x) &= \inf_{y \in \mathbb{R}} \left(  \lfloor6x\rfloor - \lfloor y \rfloor - \lfloor 6x - y \rfloor + \lfloor4x\rfloor - \lfloor y- x \rfloor - \lfloor 5x - y \rfloor \right) \\
         &= \begin{cases}
            1, \quad\text{if~} \{x\} \in \left[\frac{1}{6},\frac{1}{5}\right) \cup \left[\frac{1}{3},\frac{2}{5}\right) \cup \left[\frac{1}{2},\frac{3}{5}\right) \cup \left[\frac{3}{4},\frac{4}{5}\right), \\
            0, \quad\text{otherwise.}
         \end{cases}

    \end{aligned}$$ (As usual, $\{x\}$ denotes the fractional part of $x$.) We remark that $\Phi_n$ is contributed only by the 'denominator type elementrary bricks' of the rational function $R_n(t)$.

-   We have the following bound for the coefficients $\rho_i$ of the linear forms: $$\max_{i=0,3,5,\ldots,s-1} |\rho_i| \leqslant \exp\left( \beta(s)n + o(n) \right), \quad \text{as~} n \to +\infty,$$ where $\beta(s)$ is a constant depending only on $s$, and $$\beta(s) \sim (5\log 2) \cdot s,  \quad\text{as~} s \to +\infty.$$

-   We have the asymptotic estimate for the linear forms: $S_n = \exp\left( -\alpha(s) n + o(n)  \right)$ as $n \to +\infty$, where $\alpha(s)$ is a constant depending only on $s$, and $$\alpha(s) \sim 5 \cdot s\log s, \quad \text{as~} s \to +\infty.$$

-   Let $\psi(x) = \Gamma^{\prime}(x)/\Gamma(x)$ denote the digamma function. We have the asymptotic estimate for the $\Phi_n$ factor: $\Phi_n = \exp\left( \varpi n + o(n) \right)$ as $n \to +\infty$, where $$\begin{aligned}
             \varpi =&~ \psi\left(\frac{1}{5}\right) - \psi\left(\frac{1}{6}\right) + \psi\left(\frac{2}{5}\right) - \psi\left(\frac{1}{3}\right) \\
             &+ \psi\left(\frac{3}{5}\right) - \psi\left(\frac{1}{2}\right) + \psi\left(\frac{4}{5}\right) - \psi\left(\frac{3}{4}\right) \\
               =& 2.157479\ldots.

    \end{aligned}$$

Applying Nesterenko's linear independence criterion to the sequence of linear forms $\{ \Phi_{n}^{-s/2}D_{6n}^s \cdot S_n\}_{n > s^2}$, we obtain $$\begin{aligned}
&\dim_{\mathbb{Q}}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta(3),\zeta(5),\ldots,\zeta(s-1) \right) \\
\geqslant&~ 1 + \frac{\alpha(s) - 6s + \varpi s/2}{\beta(s) + 6s - \varpi s/2} \\
=&~ (C - o(1)) \cdot \log s, \quad \text{as~} s \to +\infty,
\end{aligned}$$ where $$\begin{aligned}
C = \frac{5}{5\log 2 + 6-\varpi/2} = \frac{1.009388\ldots}{1+\log 2}.
\end{aligned}$$ Therefore, we have $\dim_{\mathbb{Q}}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta(3),\zeta(5),\ldots,\zeta(s-1) \right) \geqslant (1.009\cdot \log s)/(1+\log 2)$ for any sufficiently large even integer $s$.

In order to improve the constant $1.009$ further to $1.119$, we will consider more complicated rational functions $R_n(t)$, see (defi_R_n(t))).

## Similarities between the $p$-adic case and the classical case

In this subsection, we briefly discuss the similarities (and differences) between the proofs of Theorem 1 and Theorem 2.

In the classical case, using rational functions to construct linear forms in $1$ and zeta values is based on the observation $$\label{rtol}
\sum_{t=1}^{+\infty} \frac{1}{(t+k)^i} = \zeta(i) - \sum_{\ell=1}^{k} \frac{1}{\ell^i}, \quad(k \in \mathbb{N},~i \in \mathbb{N}_{\geqslant 2}).$$ We have no straightforward $p$-adic analogue for (rtol). Instead, we need an intermediate step by using $p$-adic Hurwitz zeta values. Recall that the classical Hurwitz zeta function is defined by $\zeta(i,x) := \sum_{t = 0}^{+\infty} (t+x)^{-i}$. We have $$\sum_{t=0}^{+\infty} \frac{1}{(t+k+x)^i} = \zeta(i,x) - \sum_{\ell=0}^{k-1} \frac{1}{(\ell+x)^i}, \quad(x \in \mathbb{R}_{>0}).$$ Its $p$-adic analogue is the following evaluation of Volkenborn integral: $$\begin{aligned}
 &~ -\int_{\mathbb{Z}_p} \frac{1}{(1-i)(t+k+x)^{i-1}}\mathrm{d}t \\
 =&~ \omega(x)^{1-i}\zeta_p(i,x) - \sum_{\ell=0}^{k-1} \frac{1}{(\ell+x)^i}, \quad (x \in \mathbb{Q}_{p} \text{~with~} |x|_p \geqslant q_p),
\end{aligned}$$ where $\omega(x)$ is the Teichmüller character and $\zeta_p(i,x)$ is the $p$-adic Hurwitz zeta value.

Note that $$\frac{\mathrm{d}}{\mathrm{d}t}\left( \frac{1}{(1-i)(t+k+x)^{i-1}} \right) = \frac{1}{(t+k+x)^i}.$$ It turns out that, for a rational function $R(t)$ of the form $$R(t) =\sum_{i=1}^{s}\sum_{k=0}^{n} \frac{a_{i,k}}{(t+k)^i}, \quad a_{i,k} \in \mathbb{Q}, ~\deg R \leqslant -2,$$ we have $$\begin{aligned}
\sum_{t=0}^{+\infty} \frac{\mathrm{d}}{\mathrm{d}t}R(t+x) &= \rho_0 + \sum_{i=2}^{s} \rho_i \zeta(i,x), \quad (x \in \mathbb{R}_{>0}), \label{cla}\\
-\int_{\mathbb{Z}_p} R(t+x)\mathrm{d}t &= \rho_0 + \sum_{i=2}^{s} \rho_i \zeta_p(i,x), \quad (x \in \mathbb{Q}_p \text{~with~} |x|_p \geqslant q_p), \label{pad}
\end{aligned}$$ where the coefficients $\rho_0, \rho_i \in \mathbb{Q}$ are exactly the same for both cases.

Eqs. (cla) and (pad) suggest that, the $p$-adic analogue of $$\sum_{t=0}^{+\infty} R(t+x)$$ should be $$-\int_{\mathbb{Z}_p} W(t+x)\mathrm{d}t$$ for some suitable primitive function $W(t)$ (that is, $W'(t) = R(t)$).

However, to prove Theorem 1 and Theorem 2, we need use different sequences of rational functions $\{ R_n(t) \}_{n \in \mathbb{N}}$ and $\{ V_n(t) \}_{n \in \mathbb{N}}$ (and their primitive functions $\{ W_n(t)\}_{n \in \mathbb{N}}$, $W^{\prime}_n(t)=V_n(t)$), respectively. Let us briefly explain the reason. Recall that the original rational functions used by Ball-Rivoal [@BR2001] are of the form $$\label{BR-R}
R_n(t) = (\text{some factor}) \cdot \frac{(t-rn)_{rn}(t+n+1)_{rn}}{(t)_{n+1}^s}.$$ The 'left factor' $(t-rn)_{rn}$ is designed to ensure that $\sum_{t=1}^{+\infty} R_n(t)$ is small. The 'right factor' $(t+n+1)_{rn}$ is designed for symmetry to eliminate all even zeta values. In the $p$-adic case, we do not need the symmetry because $\zeta_p(i) = 0$ for any positive even integer $i$. The candidates for the $p$-adic case are $$V_n(t) = (\text{some factor}) \cdot \frac{\prod_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} (t+\nu/p^l)_{n}}{(t)_{n+1}^s},$$ where $l$ is a large positive integer. The role of $l$ is similar to that of $r$ in (BR-R): it makes $$-\int_{\mathbb{Z}_p} W_n(t+x)\mathrm{d}t \quad \left(x = \frac{\nu}{p^l},~1\leqslant \nu \leqslant p^l,~ p \nmid \nu \right)$$ $p$-adically small. We need the 'middle factor' $$\prod_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} \left(t+\frac{\nu}{p^l}\right)_{n}$$ of $V_n(t)$ to control the denominator of the coefficient $\rho_0$ (that is, the coefficient corresponding to $1$ in the resulting linear combination of $1$ and $p$-adic odd zeta values). This observation of 'middle factor' has been used in [@FSZ2019; @LY2020; @{LS2023+}]. However, in order to establish certain non-vanishing property for the $p$-adic case, we need a few technical modifications on $V_n(t)$, see (defi_V_n(t))).

## Structure of the paper

In Section 2, we introduce Nesterenko's linear independence criterion and its $p$-adic variant.

Sections 3--6 are devoted to Theorem 1. In Section 3, we set up parameters and construct linear forms by using explicit rational functions. In Section 4, we prove arithmetic properties of the linear forms. In Section 5, we study the asymptotic behavior of the linear forms. In Section 6, we prove Theorem 1.

Sections 7--12 are devoted to Theorem 2. In Section 7, we recall the definition of $p$-adic zeta values. In Section 8, we set up parameters and construct linear forms by using explicit rational functions. In Section 9, we prove arithmetic properties of the linear forms. In Section 10, we estimate the Archimedean norm of coefficients of the linear forms. In Section 11, we estimate the $p$-adic norm of the linear forms. In Section 12, we prove Theorem 2

Section 13 focuses on the computational aspect of our method. We prove Claim 3 and Claim 4 in this section.

# Linear independence criterion

Two basic criteria for linear independence are Siegel's criterion and Nesterenko's criterion [@Nes1985]. Each criterion has its own advantages. In the non-explicit approach of Fischler [@{Fis2021+}], Siegel's criterion is the only choice. However, in the original setting of Rivoal [@Riv2000] (or Ball-Rivoal [@BR2001]), Nesterenko's criterion is more convenient. In the current paper, we will utilize Nesterenko's criterion and its $p$-adic variant to prove Theorem 1 and Theorem 2, respectively.

**Theorem 5** (Nesterenko's linear independence criterion [@Nes1985], 1985). *Let $\xi_1,\xi_2,\ldots,\xi_s$ be real numbers, with $s \geqslant 1$. Let $\alpha, \beta$ be positive constants. For any $n \in \mathbb{N}$, let $L_n(X_0,X_1,\ldots,X_s) = \sum_{i=0}^{s} l_{n,i}X_i$ be a linear form with integer coefficents, where $l_{n,i} \in \mathbb{Z}$ for $i=0,1,\ldots,s$. Suppose the following conditions hold:*

-   *$|L_n(1,\xi_1,\xi_2,\ldots,\xi_s)| = \exp\left( -\alpha n + o(n)  \right)$, as $n \to +\infty$;*

-   *$\max_{0\leqslant i \leqslant s} |l_{n,i}| \leqslant \exp\left( \beta n + o(n) \right)$, as $n \to +\infty$.*

*Then, we have $$\dim_{\mathbb{Q}}\operatorname{Span}_{\mathbb{Q}}\left( 1,\xi_1,\xi_2,\ldots,\xi_s \right) \geqslant 1 +\frac{\alpha}{\beta}.$$*

In 2010, Fischler and Zudilin [@FZ2010] refined Nesterenko's criterion. We state their result below. The refined version is not necessary for the proof of Theorem 1, but it will be used in Section 13 to prove that $\dim_{\mathbb{Q}}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta(3),\zeta(5),\ldots,\zeta(75) \right) \geqslant 3$.

**Theorem 6** (Fischler-Zudilin [@FZ2010], 2010). *Keep the notations and conditions in Theorem 5. Suppose, in addition, that for each $n \in \mathbb{N}$ and each $i=1,2,\ldots,s$, the integer coefficient $l_{n,i}$ has a positive divisor $d_{n,i}$ such that:*

-   *$d_{n,i}$ divides $d_{n,i+1}$ for any $n \in \mathbb{N}$ and any $i=1,2,\ldots,s-1$;*

-   *$d_{n,j}/d_{n,i}$ divides $d_{n+1,j}/d_{n+1,i}$ for any $n \in \mathbb{N}$ and any $0 \leqslant i < j \leqslant s$, with $d_{n,0}=1$;*

-   *For each $i=1,2,\ldots,s$, we have $d_{n,i}= \exp\left( \gamma_i n + o(n) \right)$ as $n \to +\infty$ for some constant $\gamma_i \geqslant 0$.*

*Let $d = \dim_{\mathbb{Q}}\operatorname{Span}_{\mathbb{Q}}\left( 1,\xi_1,\xi_2,\ldots,\xi_s \right)$. Then, we have $$d \geqslant 1 + \frac{\alpha + \gamma_1 + \gamma_2 + \cdots + \gamma_{d-1}} {\beta}.$$*

In 2012, Nesterenko [@Nes2012] proved a $p$-adic version of his linear independence criterion. We use the following formulation (see [@Spr20 Theorem 1.4]):

**Theorem 7** (Nesterenko's $p$-adic linear independence criterion [@Nes2012], 2012). *Let $p$ be any prime number. Let $\xi_1,\xi_2,\ldots,\xi_s$ be $p$-adic numbers, with $s \geqslant 1$. Let $\alpha_1, \alpha_2, \beta$ be positive real constants. For any $n \in \mathbb{N}$, let $L_n(X_0,X_1,\ldots,X_s) = \sum_{i=0}^{s} l_{n,i}X_i$ be a linear form with integer coefficents, where $l_{n,i} \in \mathbb{Z}$ for $i=0,1,\ldots,s$. Suppose the following conditions hold:*

-   *$\exp\left( -\alpha_1 n + o(n)  \right) \leqslant |L_n(1,\xi_1,\xi_2,\ldots,\xi_s)|_p \leqslant \exp\left( -\alpha_2 n + o(n)  \right)$, as $n \to +\infty$;*

-   *$\max_{0\leqslant i \leqslant s} |l_{n,i}| \leqslant \exp\left( \beta n + o(n) \right)$, as $n \to +\infty$.*

*Then, we have $$\dim_{\mathbb{Q}}\operatorname{Span}_{\mathbb{Q}}\left( 1,\xi_1,\xi_2,\ldots,\xi_s \right) \geqslant \frac{\alpha_1}{\beta+\alpha_1-\alpha_2}.$$*

# Setting of the proof for the classical case

In this section, we will first set up the parameters. Then we will construct a sequence of rational functions $R_n(t)$ and utilize them to produce linear forms in $1$ and odd zeta values.

## Parameters

Fix a positive integer $M$, and fix a finite collection of non-negative integers $\{\delta_j\}_{j=1}^{J}$ such that $$\label{condition_on_deltas}
    0 \leqslant \delta_1 \leqslant \delta_2 \leqslant \cdots \leqslant \delta_J < \frac{M}{2}.$$ Here $J \geqslant 1$ denotes the number of $\delta_j$'s.

Let $s$ be a sufficiently large multiple of $2J$. Take the 'numerator length parameter' $$\label{defi_r}
    r := \left\lfloor \frac{s}{\log^2 s} \right\rfloor$$ to be the same as in the Ball-Rivoal setting [@BR2001].

## Rational functions

Recall that $(x)_k=x(x+1)\cdots(x+k-1)$ denotes the Pochhammer symbol. For any $n \in \mathbb{N}$, we define the following rational function $R_n(t)$:

$$\begin{aligned}
     R_n(t) := &\frac{\prod_{j=1}^{J} ((M-2\delta_j)n)!^{s/J}}{n!^{2r}} \cdot (2t+Mn) \notag\\
    & \times \frac{(t-rn)_{rn} (t+Mn+1)_{rn}}{\prod_{j=1}^{J} (t+\delta_jn)_{(M-2\delta_j)n+1}^{s/J}}. \label{defi_R_n(t)}
\end{aligned}$$ Since $s$ is a multiple of $2J$, this rational function has rational coefficients, i.e., $R_n(t) \in \mathbb{Q}(t)$, and it possesses the following symmetry: $$\label{symmetry}
     R_n(-t-Mn) = - R_n(t).$$ Note that the degree of the rational function $R_n(t)$ is $$\deg R_n  = 1 + 2rn - \frac{s}{J}\sum_{j=1}^{J} \left((M-2\delta_j)n+1\right).$$ Since $r = \lfloor s/\log^2 s \rfloor$ and $s$ is assumed to be sufficiently large, we have $$\label{degleq-2}
     \deg R_n(t) \leqslant -2, \quad\text{for any~}n \in \mathbb{N}.$$ Thus, the rational function $R_n(t)$ has the partial-fraction decomposition of the form $$\label{defi_anik}
    R_n(t) =: \sum_{i=1}^{s}\sum_{k=\delta_1 n}^{(M-\delta_1)n} \frac{a_{n,i,k}}{(t+k)^i},$$ where the coefficients $a_{n,i,k} \in \mathbb{Q}$ ($1 \leqslant i \leqslant s,~\delta_1n \leqslant k \leqslant (M-\delta_1)n$) are uniquely determined by $R_n(t)$.

## Linear forms

We define $$\begin{aligned}
    \rho_{n,i} &:= \sum_{k=\delta_1n}^{(M-\delta_1)n} a_{n,i,k}, \quad i=1,2,3,\ldots,s, \label{defi_rho_i} \\
    \rho_{n,0} &:= -\sum_{i=1}^{s}\sum_{k=\delta_1n}^{(M-\delta_1)n}\sum_{\ell=1}^{k} \frac{a_{n,i,k}}{\ell^i}. \label{defi_rho_0}
\end{aligned}$$ Note that the symmetry of the rational function (see (symmetry)) implies the symmetry of its coefficients in the partial-fraction decomposition; that is $$a_{n,i,k} = (-1)^{i+1} a_{n,i,Mn-k}, \quad (1 \leqslant i \leqslant s,~\delta_1n \leqslant k \leqslant (M-\delta_1)n).$$ Therefore, we have $$\rho_{n,i} = 0 \quad\text{for~} i=2,4,6,\ldots,s.$$ On the other hand, by (degleq-2) and (defi_anik), we have $$\rho_{n,1} = \lim_{t \to +\infty} tR_n(t) = 0.$$

Define $$\label{defi_Sn}
     S_n := \sum_{\nu=1}^{+\infty} R_n(\nu).$$ Using similar arguments as in [@BR2001 Lemme 1], we have the following lemma:

**Lemma 8**. *For any $n \in \mathbb{N}$, we have $$S_n = \rho_{n,0} + \sum_{3 \leqslant i \leqslant s-1 \atop i \text{~odd}} \rho_{n,i} \zeta(i)$$ is a linear form in $1$ and odd zeta values, where the coefficients $\rho_{n,i}$ ($i=3,5,\ldots,s-1$) are defined by (defi_rho_i) and $\rho_{n,0}$ is defined by (defi_rho_0).*

# Arithmetic properties for the classical case

In this section, we will first introduce two types of 'elementrary bricks': the 'denominator type elementrary brick' (see Lemma 9) and the 'numerator type elementrary brick' (see Lemma 10). Our rational functions in (defi_R_n(t))), and many other rational functions in the literature (e.g. [@Riv2000; @Zud2001]), are finite products of these 'elementrary bricks'. Then, we will study the denominators of the coefficients $a_{n,i,k}$ (defined by (defi_anik)) and $\rho_{n,i}$ (defined by (defi_rho_0) and (defi_rho_i)).

Recall that, we denote by $$D_m = \operatorname{lcm}[1,2,3,\ldots,m]$$ the least commom multiple of the numbers $1,2,3\ldots,m$ for any positive integer $m$. We denote by $f^{(\lambda)}(t)$ the $\lambda$-th order derivative of a function $f(t)$ for any non-negative integer $\lambda$. For a prime number $p$, the notation $v_p(x)$ denotes the $p$-adic order of $x$.

**Lemma 9**. *Let $a,b,a_0,b_0$ be integers such that $a_0 \leqslant a \leqslant b \leqslant b_0$ and $b_0 > a_0$. Consider the 'denominator type elementrary brick' $$G(t) = \frac{(b-a)!}{(t+a)_{b-a+1}}.$$ Then, we have $$\label{lem_G_1}
D_{b_0-a_0}^{\lambda} \cdot \frac{1}{\lambda!} \left( G(t)(t+k) \right)^{(\lambda)} \big|_{t=-k} \in \mathbb{Z}$$ for any $k \in [a_0,b_0]\cap \mathbb{Z}$ and any non-negative integer $\lambda$.*

*Moreover, for any prime number $q > \sqrt{b_0-a_0}$, any $k \in [a_0,b_0]\cap \mathbb{Z}$ and any non-negative integer $\lambda$, we have $$\label{lem_G_2}
v_q\left( \left( G(t)(t+k) \right)^{(\lambda)} \big|_{t=-k} \right) \geqslant -\lambda + \left\lfloor \frac{b-a}{q} \right\rfloor - \left\lfloor \frac{k-a}{q} \right\rfloor - \left\lfloor \frac{b-k}{q} \right\rfloor.$$*

*Proof.* See [@Zud2004 Lemmas 16, 18]. We have replaced $b$ and $b_0$ in [@Zud2004 Lemma 16, 18] by $b+1$ and $b_0+1$, respectively. ◻

**Lemma 10**. *Let $a,b,c,m$ be integers with $m > 0$ and $b>0$. Let $$\mu_m(b) := b^{m} \prod_{q \mid b \atop q \text{~prime~}} q^{\lfloor m/(q-1) \rfloor}.$$ Consider the 'numerator type elementrary brick' $$F(t) = \mu_m(b) \cdot \frac{(ct+a/b)_m}{m!}.$$ Then, we have $$D_{m}^{\lambda} \cdot \frac{1}{\lambda!}  F^{(\lambda)}(t)  \big|_{t=-k} \in \mathbb{Z}$$ for any $k \in \mathbb{Z}$ and any non-negative integer $\lambda$.*

Lemma 10 is known in the literature but not stated as above. For example, one can slightly modify the arguments in [@LY2020 Proposition 3.2] to obtain a proof. For the reader's convenience and for the future citation in a subsequent paper, we present a proof below.

*Proof of Lemma 10.* Fix $k \in \mathbb{Z}$. Note that $$F(t-k) =  \frac{\prod_{q \mid b \atop q ~\text{prime}} q^{\lfloor n/(q-1) \rfloor}}{m!} \cdot \prod_{\nu=0}^{m-1} (bct -bck +b\nu + a).$$ Write $$\label{351}
        \prod_{\nu=0}^{m-1} (bct-bck+b\nu + a) =  \sum_{j=0}^{m} C_jt^{j}, \quad C_j \in \mathbb{Z},~ j=0,1,\ldots,m.$$ Then, we have $$\frac{1}{\lambda!}  F^{(\lambda)}(t)  \big|_{t=-k} = \frac{\prod_{q \mid b \atop q ~\text{prime}} q^{\lfloor m/(q-1) \rfloor}}{m!} \cdot C_{\lambda},$$ with the convetion $C_{\lambda} = 0$ for $\lambda > m$.

It remains to show that, for any prime $q_0$, we have $$\label{352}
v_{q_0} \left( D_m^{\lambda}  \frac{\prod_{q \mid b \atop q ~\text{prime}} q^{\lfloor m/(q-1) \rfloor}}{m!} C_{\lambda}\right)  \geqslant 0.$$ Since $C_\lambda \in \mathbb{Z}$ and $v_{q_0}(m!) \leqslant \lfloor  m/(q_0-1)\rfloor$, the inequality (352) holds for any prime $q_0 \mid b$. Now, assume $q_0 \nmid b$. By expanding the left-hand side of (351), we see that $C_\lambda$ can be expressed as a sum of finitely many terms of the form $${(bc)}^{\lambda} \prod_{i=1}^{\lambda+1} U_i,$$ where each $U_i$ is a product of $\ell_i \in \mathbb{Z}_{\geqslant 0}$ consecutive terms in an integer arithmetic progression with common difference $b$ such that $\sum_{i=1}^{\lambda+1} \ell_i = m-\lambda$. Since $q_0 \nmid b$, we have $$v_{q_0}(U_i) \geqslant \sum_{j=1}^{+\infty} \left\lfloor  \frac{\ell_i}{q_0^{j}}\right\rfloor,$$ and hence $$v_{q_0} \left( {(bc)}^{\lambda} \prod_{i=1}^{\lambda+1} U_i \right) \geqslant \sum_{j=1}^{+\infty} \sum_{i=1}^{\lambda+1} \left\lfloor  \frac{\ell_i}{q_0^{j}}\right\rfloor.$$ Noting that $$\sum_{i=1}^{\lambda+1} \left\lfloor  \frac{\ell_i}{q_0^{j}}\right\rfloor \geqslant \sum_{i=1}^{\lambda+1} \frac{\ell_i - (q_0^{j}-1)}{q_0^{j}} = \frac{m+1}{q_0^{j}} - \lambda - 1 > \left\lfloor \frac{m}{q_0^{j}} \right\rfloor - \lambda - 1$$ and the left-hand side above is an integer, we have $$\sum_{i=1}^{\lambda+1} \left\lfloor  \frac{\ell_i}{q_0^{j}}\right\rfloor \geqslant \left\lfloor \frac{m}{q_0^{j}} \right\rfloor - \lambda.$$ Thus, $$\begin{aligned}
v_{q_0} \left( {(bc)}^{\lambda} \prod_{i=1}^{\lambda+1} U_i \right) &\geqslant \sum_{j=1}^{+\infty} \sum_{i=1}^{\lambda+1} \left\lfloor  \frac{\ell_i}{q_0^{j}}\right\rfloor \\
&= \sum_{j=1}^{\lfloor \log m / \log q_0 \rfloor} \sum_{i=1}^{\lambda+1} \left\lfloor  \frac{\ell_i}{q_0^{j}}\right\rfloor \\
&\geqslant \sum_{j=1}^{\lfloor \log m / \log q_0 \rfloor} \left( \left\lfloor \frac{m}{q_0^{j}} \right\rfloor - \lambda \right) \\
&= v_{q_0}(m!) - \lambda v_{q_0}(D_m).
\end{aligned}$$ So $v_{q_0}(C_{\lambda}) \geqslant v_{q_0}(m!) - \lambda v_{q_0}(D_m)$, which proves (352). ◻

Now, we study the arithmetic property of the coefficients $a_{n,i,k}$ defined by (defi_anik). The proof of the following lemma is essentially the same as (part of) the proof of [@Zud2004 Lemma 19], but we would like to present the details here.

**Lemma 11**. *For any integer $n > s^2$, we have $$\Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s-i} \cdot  a_{n,i,k} \in \mathbb{Z}, \quad (1 \leqslant i \leqslant s,~\delta_1n \leqslant k \leqslant (M-\delta_1)n),$$ where the factor $\Phi_n$ is a product of certain primes: $$\label{defi_Phi}
\Phi_n := \prod_{\sqrt{Mn} < q \leqslant (M-2\delta_1)n \atop q \text{~prime}} q^{\phi(n/q)},$$ and the function $\phi(\cdot)$ is defined by $$\label{defi_phi}
\phi(x) := \inf_{y \in \mathbb{R}} \sum_{j=1}^{J}  \left( \lfloor(M-2\delta_j)x\rfloor - \lfloor y-\delta_j x \rfloor - \lfloor (M-\delta_j)x - y \rfloor \right).$$*

*Proof.* Fix any $i \in \{1,2,\ldots,s\}$ and any $k \in [\delta_1n,~(M-\delta_1)n] \cap \mathbb{Z}$.

By (defi_anik), we have $$\label{a_i_k_determined_by_R_n}
a_{n,i,k} = \frac{1}{(s-i)!} \left( R_n(t)(t+k)^{s} \right)^{(s-i)} \Big|_{t=-k}.$$

Let us define the elementrary bricks: $$\begin{aligned}
    F_0(t) &= 2t+Mn, \\
    F_{-,\tau}(t) &= \frac{(t-(r-\tau)n)_{n}}{n!}, \quad \tau=0,1,2,\ldots,r-1, \\
    F_{+,\tau}(t) &= \frac{(t+(M+\tau)n+1)_{n}}{n!}, \quad \tau=0,1,2,\ldots,r-1, \\
    G_j(t) &=  \frac{((M-2\delta_j)n)!}{(t+\delta_jn)_{(M-2\delta_j)n+1}}, \quad j=1,2,\ldots,J.
\end{aligned}$$ From the definition of the rational function $R_n(t)$ (see (defi_R_n(t)))), we have $$\label{product}
R_n(t)(t+k)^s = F_{0}(t) \cdot \prod_{\tau=0}^{r-1} F_{-,\tau}(t)F_{+,\tau}(t) \cdot \prod_{j=1}^{J} \left(G_j(t)(t+k)\right)^{s/J}.$$ By Lemma 10, for any polynomial $F(t)$ of the form $F_0(t)$, $F_{-,\tau}(t)$, $F_{+,\tau}(t)$, we have $$\label{F_is_good}
D_{n}^{\lambda} \cdot \frac{1}{\lambda!} F^{(\lambda)}(t) \big|_{t=-k} \in \mathbb{Z}$$ for any non-negative integer $\lambda$. By (lem_G_1) of Lemma 9 (with $a_0 = \delta_1n$ and $b_0 = (M-\delta_1)n$), we have $$\label{G_is_good}
D_{(M-2\delta_1)n}^{\lambda} \cdot \frac{1}{\lambda!} \left( G_j(t)(t+k) \right)^{(\lambda)} \big|_{t=-k} \in \mathbb{Z}$$ for any $j=1,2,\ldots,J$ and any non-negative integer $\lambda$. Now, substituting (product) into (a_i_k_determined_by_R_n), applying the Leibniz rule, and using (F_is_good)(G_is_good), we obtain $$\label{arith_anik_1}
D_{(M-2\delta_1)n}^{s-i} \cdot  a_{n,i,k} \in \mathbb{Z}.$$

Moreover, for any prime $q$ such that $\sqrt{Mn} < q \leqslant (M-2\delta_1)n$, taking also (lem_G_2) of Lemma 9 into consideration, and noting that $q>\sqrt{Mn}>s$ (because $n > s^2$), we have $$\begin{aligned}
v_q\left( a_{n,i,k} \right) &= v_q\left( \left( R_n(t)(t+k)^{s} \right)^{(s-i)} \Big|_{t=-k} \right) \notag\\
&\geqslant -(s-i) + \frac{s}{J}\cdot\sum_{j=1}^{J} \left( \left\lfloor \frac{(M-2\delta_j)n}{q}  \right\rfloor - \left\lfloor \frac{k-\delta_jn}{q}  \right\rfloor - \left\lfloor \frac{(M-\delta_j)n - k}{q}  \right\rfloor \right)  \notag\\
&\geqslant -(s-i) + \frac{s}{J}\cdot\phi\left( \frac{n}{q} \right), \label{arith_anik_2}
\end{aligned}$$ where the function $\phi(\cdot)$ is given by (defi_phi). Combining (arith_anik_1) and (arith_anik_2), we obtain the desired conclusion $$\Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s-i} \cdot  a_{n,i,k} \in \mathbb{Z}, \quad (1 \leqslant i \leqslant s,~\delta_1n \leqslant k \leqslant (M-\delta_1)n).$$ ◻

The arithmetic property of $a_{n,i,k}$ propagates to the arithmeric property of $\rho_{n,i}$ (defined by (defi_rho_i) and (defi_rho_0)), as the following lemma shows.

**Lemma 12**. *For any integer $n > s^2$, we have $$\Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s-i} \cdot \rho_{n,i} \in \mathbb{Z}, \quad i=1,2,\ldots,s,$$ and $$\Phi_n^{-s/J} \prod_{j=1}^{J} D_{M_jn}^{s/J} \cdot \rho_{n,0} \in \mathbb{Z},$$ where $$M_j = \max\{ M-2\delta_1,~M-\delta_j \}.$$*

*Proof.* The first assertion follows directly from (defi_rho_i) and Lemma 11.

Now, using (defi_rho_0), we have $$\label{lem4.4_1}
\rho_{n,0} = -\sum_{i=1}^{s}\sum_{k=\delta_1n}^{(M-\delta_1)n} a_{n,i,k} \sum_{\ell=1}^{k} \frac{1}{\ell^i}.$$ Fix any $i \in \{1,2,\ldots,s\}$ and let $$j^{*} = \left\lceil  \frac{iJ}{s} \right\rceil.$$ Note that we have $a_{n,i,k} = 0$ except for $\delta_{j^{*}}n \leqslant k \leqslant (M-\delta_{j^{*}})n$ (by looking at the order of the pole at $t=-k$ in (defi_R_n(t)))). Thus, $$\label{lem4.4_2}
\sum_{k=\delta_1n}^{(M-\delta_1)n} a_{n,i,k} \sum_{\ell=1}^{k} \frac{1}{\ell^i} = \sum_{k=\delta_{j^{*}}n}^{(M-\delta_{j^{*}})n} a_{n,i,k} \sum_{\ell=1}^{k} \frac{1}{\ell^i}.$$ We have obviously $$D_{(M-\delta_{j^{*}})n}^{i} \cdot  \sum_{\ell=1}^{k} \frac{1}{\ell^{i}} \in \mathbb{Z}$$ for any $k \leqslant (M-\delta_{j^{*}})n$. On the other hand, Lemma 11 implies $$\Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s-i} \cdot a_{n,i,k} \in \mathbb{Z}.$$ Noting that $D_{(M-\delta_{j^{*}})n}^{i}  D_{(M-2\delta_1)n}^{s-i}$ is a divisor of $\prod_{j=1}^{J} D_{M_jn}^{s/J}$, we obtain $$\label{lem4.4_3}
\Phi_n^{-s/J} \prod_{j=1}^{J} D_{M_jn}^{s/J} \cdot \sum_{k=\delta_{j^{*}}n}^{(M-\delta_{j^{*}})n} a_{n,i,k} \sum_{\ell=1}^{k} \frac{1}{\ell^i} \in \mathbb{Z}.$$ Combining (lem4.4_1), (lem4.4_2) and (lem4.4_3), we conclude that $$\Phi_n^{-s/J} \prod_{j=1}^{J} D_{M_jn}^{s/J} \cdot \rho_{n,0} \in \mathbb{Z}.$$ ◻

# Asymptotic estimates for the classical case

In this section, we will study the asymptotic behavior of the linear form $S_n$ (defined by (defi_Sn)), the coefficient $\rho_{n,i}$ (defined by (defi_rho_i) and (defi_rho_0)) and the factor $\Phi_n$ (defined by (defi_Phi)) as $n \to +\infty$.

**Lemma 13**. *We have $$\label{S_n_estimate}
S_n = \exp\left( -\alpha(s)n + o(n) \right), \quad \text{as~} n \to +\infty,$$ where $\alpha(s)$ is a constant independent of $n$. Moreover, we have $$\label{alpha}
\alpha(s) \sim \frac{s \log s}{J} \sum_{j=1}^{J} (M-2\delta_j), \quad \text{as~} s \to +\infty.$$*

*Proof.* Consider the Lebesgue integral $$\label{defi_I_n}
I_n = \int_{[0,1]^{s+1}} F(x_0,x_1,\ldots,x_s)^n G(x_0,x_1,\ldots,x_s)~\mathrm{d}x_0\mathrm{d}x_1 \cdots \mathrm{d}x_s,$$ where $$\begin{aligned}
&~ F(x_0,x_1,\ldots,x_s) \notag\\
=&~  \frac{x_0^{r}(1-x_0)^{M}\prod_{j=1}^{J}\prod_{k=1}^{s/J} x_{(j-1)s/J +k}^{r+\delta_j} (1-x_{(j-1)s/J +k})^{M-2\delta_j} }{(1-x_0x_1\cdots x_s)^{2r+M}} \label{F}
\end{aligned}$$ for $(x_0,x_1,\ldots,x_s) \in [0,1]^{s+1} \setminus \{(1,1,\ldots,1)\}$ with $F(1,1,\ldots,1)=0$, and $$G(x_0,x_1,\ldots,x_s) = \frac{1+x_0x_1\cdots x_{s}}{(1-x_0x_1\cdots x_s)^3}$$ for $(x_0,x_1,\ldots,x_s) \in [0,1]^{s+1} \setminus \{(1,1,\ldots,1)\}$ with $G(1,1,\ldots,1)=0$.

We claim that $$\label{S=I}
S_n = \frac{((2r+M)n+2)!}{(Mn)! \cdot n!^{2r}} I_n.$$ In fact, using the expansion $$\begin{aligned}
&\frac{1+x_0x_1\ldots x_s}{(1-x_0x_1\cdots x_s)^{(2r+M)n+3}} \\
=& \frac{1}{((2r+M)n+2)!}\sum_{\nu=1}^{+\infty} (\nu)_{(2r+M)n+1} \cdot ((2r+M)n+2\nu)  \cdot x_0^{\nu-1}x_1^{\nu-1}\cdots x_{s}^{\nu-1}
\end{aligned}$$ and the well-known identity for Euler's Beta function $$\int_{0}^{1} x^{(r+\delta)n+\nu-1}(1-x)^{(M-2\delta)n}~\mathrm{d}x = \frac{((M-2\delta)n)!}{((r+\delta)n+\nu)_{(M-2\delta)n+1}},$$ we deduce from Beppo Levi's lemma and Tonelli's theorem that $$\begin{aligned}
I_n =&~ \frac{(Mn)!}{((2r+M)n+2)!} \\ &\times \sum_{\nu=1}^{+\infty} \frac{(\nu)_{(2r+M)n+1} \cdot ((2r+M)n+2\nu)}{(rn+\nu)_{Mn+1}} \prod_{j=1}^{J} \frac{((M-2\delta_j)n)!^{s/J}}{((r+\delta_j)n+\nu)_{(M-2\delta_j)n+1}^{s/J}} \\
=&~ \frac{(Mn)!\cdot n!^{2r}}{((2r+M)n+2)!} \sum_{\nu=1}^{+\infty} R_n(rn+\nu).
\end{aligned}$$ Then, by (defi_Sn) and the fact that $R_n(\nu)=0$ for $\nu=1,2,3,\ldots,rn$, we conclude that (S=I) is true.

It is easy to see that $G(x_0,x_1,\ldots,x_s)$ is Lebesgue integrable over $[0,1]^{s+1}$. Also, $G(x_0,x_1,\ldots,x_s)$ is positive and continuous over $[0,1]^{s+1} \setminus \{(1,1,\ldots,1)\}$. We claim that $F(x_0,x_1,\ldots,x_s)$ is continuous on $[0,1]^{s+1}$. In fact, the only possible discontinuity of $F(x_0,x_1,\ldots,x_s)$ is at $(1,1,\ldots,1)$. Since $1-x_0x_1\ldots x_s \geqslant 1-x_i$ for every $i=0,1,\ldots,s$ on $[0,1]^{s+1}$, we have $$(1-x_0x_1\cdots x_s)^{s+1} \geqslant \prod_{i=0}^{s} (1-x_i),$$ and hence $$\begin{aligned}
&~F(x_0,x_1,\ldots,x_s) \notag\\
\leqslant&~ x_0^{r}(1-x_0)^{M-\frac{2r+M}{s+1}}\prod_{j=1}^{J}\prod_{k=1}^{s/J} x_{(j-1)s/J +k}^{r+\delta_j} (1-x_{(j-1)s/J +k})^{M-2\delta_j- \frac{2r+M}{s+1}} \label{F2}
\end{aligned}$$ for all $(x_0,x_1,\ldots,x_s) \in [0,1]^{s+1} \setminus \{ (1,1,\ldots,1) \}$. Recall that $r = \lfloor s/\log^2 s \rfloor$ and $s$ is sufficiently large, the above inequality (F2) implies the continuity of $F(x_0,x_1,\ldots,x_s)$ at $(1,1,\ldots,1)$. Thus, by (defi_I_n) we have $$\lim_{n \to +\infty} I_n^{1/n} = \max_{(x_0,x_1,\ldots,x_s) \in [0,1]^{s+1}} F(x_0,x_1,\ldots,x_s).$$ Then, by (S=I) and Stirling's formula, we have $$S_n = \exp\left( -\alpha(s)n + o(n) \right), \quad\text{as~} n \to +\infty,$$ where $$\begin{aligned}
\alpha(s) =&~  M\log M - (2r+M)\log(2r+M) \notag\\
&- \log \max_{(x_0,x_1,\ldots,x_s) \in [0,1]^{s+1}} F(x_0,x_1,\ldots,x_s). \label{defi_alpha}
\end{aligned}$$

Finally, by (defi_alpha) and $r =\lfloor s/\log^2 s \rfloor$, in order to prove the last assertion about the asymptotic behavior of $\alpha(s)$ as $s \to +\infty$, it remains to prove that $$\label{alpha_estimate}
    -\log \max_{(x_0,x_1,\ldots,x_s) \in [0,1]^{s+1}} F(x_0,x_1,\ldots,x_s) \sim \frac{s\log s}{J}\sum_{j=1}^{J} (M-2\delta_j), \quad \text{as~} s\to +\infty.$$ In fact, taking $x_0=x_1=\cdots=x_s = 1-1/r$ in (F), we have (recall $r=\lfloor s/\log^2 s\rfloor$) $$\begin{aligned}
&\log \max_{(x_0,x_1,\ldots,x_s) \in [0,1]^{s+1}} F(x_0,x_1,\ldots,x_s) \notag\\
\geqslant& \left( (s+1)r + \frac{s}{J}\sum_{j=1}^{J} \delta_j \right)\log\left( 1-\frac{1}{r} \right) - \left( M + \frac{s}{J}\sum_{j=1}^{J} (M-2\delta_j) \right) \log r \notag\\
&- (2r+M)\log\left( 1-\left( 1-\frac{1}{r} \right)^{s+1} \right) \notag\\
=&~ -\frac{s\log s}{J}\sum_{j=1}^{J} (M-2\delta_j) - O(s\log\log s), \quad \text{as~} s \to +\infty. \label{F3}
\end{aligned}$$ On the other hand, applying the elementrary inequality $$x^{a}(1-x)^b \leqslant \frac{a^ab^b}{(a+b)^{a+b}} \quad  (a>0, b>0, x \in [0,1])$$ to (F2), we have $$\begin{aligned}
&\log \max_{(x_0,x_1,\ldots,x_s) \in [0,1]^{s+1}} F(x_0,x_1,\ldots,x_s) \notag\\
\leqslant&~ r\log r  + \left( M-\frac{2r+M}{s+1} \right)\log\left( M-\frac{2r+M}{s+1} \right) \notag\\
&-\left( r+M - \frac{2r+M}{s+1} \right)\log\left(  r+M - \frac{2r+M}{s+1} \right) \notag\\ &+\frac{s}{J}\sum_{j=1}^{J}(r+\delta_j)\log(r+\delta_j)   \notag\\
&+ \frac{s}{J}\sum_{j=1}^{J} \left( M-2\delta_j - \frac{2r+M}{s+1} \right) \log\left( M-2\delta_j - \frac{2r+M}{s+1} \right) \notag\\
&- \frac{s}{J}\sum_{j=1}^{J} \left( r+M-\delta_j - \frac{2r+M}{s+1} \right)\log\left(  r+M-\delta_j - \frac{2r+M}{s+1} \right) \notag\\
=&~ \frac{s}{J}\sum_{j=1}^{J} (r+\delta_j)\log r - \frac{s}{J}\sum_{j=1}^{J}\left( r+M-\delta_j \right)\log r + O(s) \notag\\
=&~ -\frac{s\log s}{J}\sum_{j=1}^{J} (M-2\delta_j) + O(s\log\log s), \quad \text{as~} s \to +\infty. \label{F4}
\end{aligned}$$ Combining (F3) and (F4), we obtain that (alpha_estimate) is true. The proof of Lemma 13 is complete. ◻

Recall that $\rho_{n,i}$ ($i=0,1,2,\ldots,s$) are defined by (defi_rho_0) and (defi_rho_i).

**Lemma 14**. *We have $$\label{rho_estimate}
\max_{0 \leqslant i \leqslant s} |\rho_{n,i}| \leqslant \exp\left( \beta(s)n + o(n) \right), \quad \text{as~} n \to +\infty,$$ where $\beta(s)$ is a constant independent of $n$. Moreover, we have $$\label{beta}
\beta(s) \sim \log2 \cdot \frac{s}{J} \sum_{j=1}^{J} (M - 2\delta_j), \quad\text{as~} s \to +\infty.$$*

*Proof.* By (defi_rho_0) and (defi_rho_i), we have $$\label{rho<a}
\max_{0 \leqslant i \leqslant s} |\rho_{n,i}| \leqslant (Mn+1)^{2}s \cdot \max_{i,k} |a_{n,i,k}|,$$ where $\max_{i,k}$ is taken over all $i \in \{ 1,2,\ldots,s \}$ and $k \in [\delta_1n, (M-\delta_1)n] \cap \mathbb{Z}$.

Now fix any pair of $i,k$ in the range above. By (defi_anik) and Cauchy's integral formula, we have $$a_{n,i,k} = \frac{1}{2\pi \sqrt{-1}} \int_{|z+k|=1/10} (z+k)^{i-1}R_n(z)~\mathrm{d}z.$$ Therefore, we have (recall (defi_R_n(t)))) $$\begin{aligned}
|a_{n,i,k}| &\leqslant \max_{|z+k| = 1/10} |R_n(z)| \notag\\
&= \frac{\prod_{j=1}^{J} ((M-2\delta_j)n)!^{s/J}}{n!^{2r}}  \notag\\
&\quad  \times \max_{|z+k| = 1/10} |2z+Mn|  \frac{|(z-rn)_{rn} (z+Mn+1)_{rn}|}{ \prod_{j=1}^{J} |(z+\delta_jn)_{(M-2\delta_j)n+1}|^{s/J}}. \label{|a|<maxR}
\end{aligned}$$ In the following, the complex number $z$ is always on the circle $|z+k|=1/10$. We will use triangle inequality to bound (\|a\|\<maxR) from above.

Obviously, we have $$\label{est1}
    \max_{|z+k| = 1/10} |2z+Mn| \leqslant 4Mn.$$ For any $\nu \in \{1,2,\ldots,rn\}$, we have $$|(z-\nu)(z+Mn+\nu)| \leqslant (k+\nu+1)(Mn-k+\nu+1) \leqslant \left( \frac{Mn}{2} + \nu + 1 \right)^2.$$ Therefore, $$\begin{aligned}
&~\max_{|z+k| = 1/10} |(z-rn)_{rn} (z+Mn+1)_{rn}| \notag\\
=&~ \max_{|z+k| = 1/10} \prod_{\nu=1}^{rn} |(z-\nu)(z+Mn+\nu)| \notag\\
\leqslant&~ \prod_{\nu=1}^{rn} \left( \left\lceil\frac{Mn}{2}\right\rceil + \nu + 1 \right)^2 \notag\\
=&~ \frac{\left(\lceil \frac{Mn}{2} \rceil + rn +1\right)!^2}{\left( \lceil\frac{Mn}{2}\rceil + 1 \right)!^2}. \label{est2}
\end{aligned}$$ Now, if $\delta_jn < k < (M-\delta_j)n$, then $$\begin{aligned}
|(z+\delta_jn)_{(M-2\delta_j)n+1}| &\geqslant (k-\delta_jn-1)! \cdot \frac{9}{10} \cdot \frac{1}{10} \cdot \frac{9}{10} \cdot ((M-\delta_j)n-k-1)! \\
&\geqslant \frac{1}{10^3M^2n^2} \cdot (k-\delta_jn)! \cdot ((M-\delta_j)n-k)!,
\end{aligned}$$ and hence $$\frac{((M-2\delta_j)n)!}{|(z+\delta_jn)_{(M-2\delta_j)n+1}|} \leqslant 10^3M^2n^2 \binom{(M-2\delta_j)n}{k-\delta_jn} \leqslant 10^3M^2n^2 \cdot 2^{(M-2\delta_j)n}.$$ If $k \leqslant \delta_j n$, then $$\begin{aligned}
|(z+\delta_jn)_{(M-2\delta_j)n+1}| &\geqslant \frac{1}{10} \cdot \frac{9}{10} \cdot ((M-2\delta_j)n-1)! \\
&\geqslant \frac{1}{10^2Mn} ((M-2\delta_j)n)!,
\end{aligned}$$ and hence $$\frac{((M-2\delta_j)n)!}{|(z+\delta_jn)_{(M-2\delta_j)n+1}|} \leqslant 10^2Mn.$$ Similarly, if $k \geqslant (M-\delta_j)n$, we also have $$\frac{((M-2\delta_j)n)!}{|(z+\delta_jn)_{(M-2\delta_j)n+1}|} \leqslant 10^2Mn.$$ In any case, we always have $$\label{est3}
    \max_{|z+k| = 1/10} \frac{((M-2\delta_j)n)!}{|(z+\delta_jn)_{(M-2\delta_j)n+1}|} \leqslant 10^3M^2n^2 \cdot 2^{(M-2\delta_j)n}.$$ Combining all the equations (rho\<a)--(est3), with the help of Stirling's formula, we have $$\max_{0 \leqslant i \leqslant s} |\rho_{n,i}| \leqslant \exp\left( \beta(s)n + o(n) \right), \quad \text{as~} n \to +\infty,$$ where $$\beta(s) = \left(2r + M \right)\log\left(r+\frac{M}{2} \right) - M\log\frac{M}{2} + \log2 \cdot \frac{s}{J} \sum_{j=1}^{J} (M-2\delta_j).$$ Since $r = \lfloor s/\log^2 s \rfloor$, we have $$\beta(s) \sim \log2 \cdot \frac{s}{J} \sum_{j=1}^{J} (M-2\delta_j), \quad \text{as~} s \to +\infty.$$ ◻

At the end of this section, we estimate the factor $\Phi_n$ (defined by (defi_Phi)). It is well known that the prime number theorem implies $$\label{PNT}
D_m =e^{m+o(m)}, \quad \text{as~} m \to +\infty.$$ The following lemma is also a corollary of the prime number theorem. For details, we refer the reader to [@Zud2002 Lemma 4.4].

**Lemma 15**. *For the factor $\Phi_n$ in (defi_Phi), we have $$\Phi_n = \exp\left( \varpi n + o(n) \right), \quad \text{as~} n \to +\infty,$$ where the constant $$\label{defi_varpi}
 \varpi = \int_{0}^{1} \phi(x)~\mathrm{d}\psi(x) - \int_{0}^{1/(M-2\delta_1)} \phi(x)~\frac{\mathrm{d}x}{x^2}.$$ The function $\psi(x) = \Gamma^{\prime}(x)/\Gamma(x)$ is the digamma function, and the function $\phi(x)$ is defined by (defi_phi).*

# Proof of Theorem 1

In this section, we will first reduce the proof of Theorem 1 to a computational task. Then we will prove Theorem 1 by using some very simple parameters.

**Proposition 16**. *Let $\psi(\cdot)$ be the digamma function. For any collection of non-negative integers $(M,\delta_1,\delta_2,\ldots,\delta_J)$ under the constraints $J \geqslant 1$ and $$0 \leqslant \delta_1 \leqslant \delta_2 \leqslant \cdots \leqslant \delta_J < \frac{M}{2},$$ we define $$\varpi = \int_{0}^{1} \phi(x)~\mathrm{d}\psi(x) - \int_{0}^{1/(M-2\delta_1)} \phi(x)~\frac{\mathrm{d}x}{x^2},$$ where the function $\phi(\cdot)$ is given by $$\phi(x) = \inf_{y \in \mathbb{R}} \sum_{j=1}^{J}  \left( \lfloor(m-2\delta_j)x\rfloor - \lfloor y-\delta_j x \rfloor - \lfloor (m-\delta_j)x - y \rfloor \right).$$*

*Then, we have $$\dim_{\mathbb{Q}}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta(3),\zeta(5),\ldots,\zeta(s-1) \right) \geqslant (C-o(1)) \cdot \log s,$$ as the even integer $s \to +\infty$, where the constant $$\label{defi_C}
C = \frac{\sum_{j=1}^{J} (M-2\delta_j) }{\log2 \cdot \sum_{j=1}^{J}(M-2\delta_j)  - \varpi  + \sum_{j=1}^{J} \max\{ M-2\delta_1,~M-\delta_j \}}.$$*

*Proof.* For any integer $n>s^2$, consider $$\widehat{S}_n := \Phi_n^{-s/J} \prod_{j=1}^{J} D_{M_jn}^{s/J} \cdot S_n,$$ where $M_j = \max\{ M-2\delta_1,~M-\delta_j \}$. By Lemma 8 and Lemma 12, we have that $$\widehat{S}_n = \widehat{\rho}_{n,0} + \sum_{3 \leqslant i \leqslant s-1 \atop i \text{~odd}} \widehat{\rho}_{n,i}\zeta(i)$$ is a linear form in $1$ and odd zeta values with integer coefficients $$\widehat{\rho}_{n,i} := \Phi_n^{-s/J} \prod_{j=1}^{J} D_{M_jn}^{s/J} \cdot \rho_{n,i} \in \mathbb{Z}, \quad i=0,3,5,\ldots,s-1.$$ By Lemma 13, Eq. (PNT) and Lemma 15, we have $$\widehat{S}_n = \exp\left( -\widehat{\alpha}(s)n+o(n) \right),  \quad \text{as~} n\to +\infty,$$ where $$\widehat{\alpha}(s) = \alpha(s) + \frac{s}{J}\varpi - \frac{s}{J}\sum_{j=1}^{J} \max\left\{ M-2\delta_1,~M-\delta_j \right\}.$$ By Lemma 14, Eq. (PNT) and Lemma 15, we have $$\max_{i=0,3,5,\ldots,s-1} |\widehat{\rho}_{n,i}| \leqslant \exp\left( \widehat{\beta}(s)n + o(n) \right), \quad \text{as~} n\to +\infty,$$ where $$\widehat{\beta}(s) = \beta(s) - \frac{s}{J}\varpi + \frac{s}{J}\sum_{j=1}^{J} \max\left\{ M-2\delta_1,~M-\delta_j \right\}.$$

By (alpha) and (beta), we have the following asymptotic estimates for $\widehat{\alpha}(s)$ and $\widehat{\beta}(s)$ as $s \to +\infty$: $$\begin{aligned}
    \widehat{\alpha}(s) &\sim  \frac{s\log s}{J}\sum_{j=1}^{J}(M-2\delta_j),   \label{alphahat}\\
    \widehat{\beta}(s) &\sim  \log 2 \cdot \frac{s}{J}\sum_{j=1}^{J}(M-2\delta_j) - \frac{s}{J}\varpi + \frac{s}{J}\sum_{j=1}^{J} \max\left\{ M-2\delta_1,~M-\delta_j \right\}. \label{betahat}
\end{aligned}$$ Applying Nesterenko's linear independence criterion (Theorem 5) to the sequence of linear forms $\{ \widehat{S}_n \}_{n > s^2}$, and using (alphahat), (betahat), we obtain $$\begin{aligned}
\dim_{\mathbb{Q}}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta(3),\zeta(5),\ldots,\zeta(s-1) \right) &\geqslant 1 +\frac{\widehat{\alpha}(s)}{\widehat{\beta}(s)} \notag \\
&= (C-o(1)) \cdot \log s, \quad \text{as~} s \to +\infty, \label{dim>Clogs}
\end{aligned}$$ where the constant $$C = \frac{\sum_{j=1}^{J} (M-2\delta_j) }{\log2 \cdot \sum_{j=1}^{J}(M-2\delta_j)  - \varpi  + \sum_{j=1}^{J} \max\{ M-2\delta_1,~M-\delta_j \}}.$$

We have restricted that $s \in 2J\mathbb{N}$ in our constructions of rational functions and linear forms. So (dim\>Clogs) is true as $s \in 2J\mathbb{N}$ and $s \to +\infty$. But clearly, if we replaced the condition '$s \in 2J\mathbb{N}$' by '$s \in 2\mathbb{N}$', the conclusion (dim\>Clogs) is still true. The proof of Proposition 16 is complete. ◻

If we take $M=1$, $\delta_1=0$, ($J=1$) in Proposition 16, then $\phi(x) \equiv 0$, $\varpi = 0$, and $C = 1/(1+\log 2)$. Thus, we rediscover the Ball-Rivoal theorem [@BR2001]. The simplest parameters to improve the Ball-Rivoal theorem are: $M=6$, $\delta_1=0$, $\delta_2=1$, ($J=2$). The latter collection of parameters leads to the proof of Theorem 1:

*Proof of Theorem 1.* Take $M=6$, $\delta_1=0$, $\delta_2 = 1$, ($J=2$) in Proposition 16. In this case, the function $\phi(\cdot)$ defined by (defi_phi) is $$\begin{aligned}
\phi(x) &= \inf_{y \in \mathbb{R}} \left(  \lfloor6x\rfloor - \lfloor y \rfloor - \lfloor 6x - y \rfloor + \lfloor4x\rfloor - \lfloor y- x \rfloor - \lfloor 5x - y \rfloor \right).
\end{aligned}$$ Note that the two-variable function $$\phi(x,y) := \lfloor6x\rfloor - \lfloor y \rfloor - \lfloor 6x - y \rfloor + \lfloor4x\rfloor - \lfloor y- x \rfloor - \lfloor 5x - y \rfloor$$ satisfies $\phi(x,y)=\phi(\{x\},\{y\})$. In the $xy$-plane, lines of the form $6x=k$, $y=k$, $6x-y=k$, $4x=k$, $y-x=k$, $5x-y=k$, ($k=0,\pm1,\pm2,\ldots$) cut apart the unit square $[0,1]^2$ into several polygons and $\phi(x,y)$ is constant in the interior of each polygon. Figure 1 indicates the constant value of $\phi(x,y)$ in the interior of each polygon.

<figure id="figure">

<figcaption>the values of <span class="math inline"><em>ϕ</em>(<em>x</em>,<em>y</em>)</span></figcaption>
</figure>

Based on Figure 1, we can express $\phi(x)$ explicitly as follows: $$\begin{aligned}
\phi(x) &= \inf_{y \in \mathbb{R}} \phi(x,y) =\min_{0 \leqslant y < 1} \phi(\{x\},y) \\
&= \begin{cases}
    1, \quad\text{if~} \{x\} \in \left[\frac{1}{6},\frac{1}{5}\right) \cup \left[\frac{1}{3},\frac{2}{5}\right) \cup \left[\frac{1}{2},\frac{3}{5}\right) \cup \left[\frac{3}{4},\frac{4}{5}\right), \\
    0, \quad\text{otherwise.}
\end{cases}
\end{aligned}$$ Therefore, by (defi_varpi) we have $$\begin{aligned}
\varpi =&~ \psi\left(\frac{1}{5}\right) - \psi\left(\frac{1}{6}\right) + \psi\left(\frac{2}{5}\right) - \psi\left(\frac{1}{3}\right) \\
&+ \psi\left(\frac{3}{5}\right) - \psi\left(\frac{1}{2}\right) + \psi\left(\frac{4}{5}\right) - \psi\left(\frac{3}{4}\right) \\
=&~ 2.157479\ldots,
\end{aligned}$$ and hence by (defi_C), $$C = \frac{10}{10\log 2 - \varpi + 12} = \frac{1.009388\ldots}{1+\log 2}.$$ In conclusion, by Proposition 16 we have $$\dim_{\mathbb{Q}}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta(3),\zeta(5),\ldots,\zeta(s-1) \right) \geqslant \frac{1.009}{1+\log 2} \cdot \log s$$ for any sufficiently large even integer $s$. The proof of Theorem 1 is complete. ◻

# Preliminaries for $p$-adic zeta values

From now on, we fix a prime number $p$. In this section we will recall basic facts about Volkenborn integrals, the first Bernoulli functional, $p$-adic Hurwitz zeta functions, and $p$-adic zeta values.

## Overconvergent power series on $\mathbb{Z}_p$

Let $C(\mathbb{Z}_p,\mathbb{Q}_p)$ denote the set of all continuous functions $f: \mathbb{Z}_p \longrightarrow \mathbb{Q}_p$. We define the set $$C^{\dagger}(\mathbb{Z}_p,\mathbb{Q}_p):= \left\{ f \in C(\mathbb{Z}_p,\mathbb{Q}_p) ~\Big|~ f(t) = \sum_{k=0}^{+\infty} a_k t^{k}, a_k \in \mathbb{Q}_p, \limsup_{k \to +\infty} |a_k|_p^{1/k} < 1    \right\}.$$ In other words, $f \in C^{\dagger}(\mathbb{Z}_p,\mathbb{Q}_p)$ if and only if the function $f(t)$ coincides on $\mathbb{Z}_p$ with a power series in $\mathbb{Q}_p\llbracket t \rrbracket$ which has radius of convergence strictly larger than $1$. If $f \in C^{\dagger}(\mathbb{Z}_p,\mathbb{Q}_p)$, we say that $f$ is an *overconvergent power series*.

If $D$ is a set containing $\mathbb{Z}_p$ and $g: D \longrightarrow \mathbb{Q}_p$ is a function such that the restriction function $g|_{\mathbb{Z}_p} \in C^{\dagger}(\mathbb{Z}_p,\mathbb{Q}_p)$, then we slightly abuse the notation to write that $g \in C^{\dagger}(\mathbb{Z}_p,\mathbb{Q}_p)$.

## Volkenborn integrals

A function $f: \mathbb{Z}_p \longrightarrow \mathbb{C}_p$ is said to be *Volkenborn integrable* if the following limit exists in $\mathbb{C}_p$: $$\lim_{N \to +\infty} \frac{1}{p^N}\sum_{k=0}^{p^{N}-1} f(k).$$ For a Volkenborn integrable function $f$, we define its *Volkenborn integral* by $$\int_{\mathbb{Z}_p}f(t) \mathrm{d}t:= \lim_{N \to +\infty} \frac{1}{p^N}\sum_{k=0}^{p^{N}-1} f(k).$$

As usual, we define the Bernoulli numbers $B_k \in \mathbb{Q}$ ($k=0,1,2,\ldots$) by the generating series $$\frac{t}{e^t-1} =: \sum_{k=0}^{+\infty} \frac{B_k}{k!}t^k.$$

**Lemma 17**. *Any overconvergent power series $f(t) = \sum_{k=0}^{+\infty} a_k t^k \in C^{\dagger}(\mathbb{Z}_p,\mathbb{Q}_p)$ is Volkenborn integrable. Moreover, we have $$\int_{\mathbb{Z}_p}f(t) \mathrm{d}t = \sum_{k=0}^{+\infty} a_kB_k.$$*

*Proof.* See [@Rob2000 Proposition, pp. 270], where a stronger result is proved. ◻

The Volkenborn integral has the following behavior under translations:

**Lemma 18**. *Let $k\in \mathbb{N}$ and $f \in C^{\dagger}(\mathbb{Z}_p,\mathbb{Q}_p)$. Then, we have $$\int_{\mathbb{Z}_p} f(t+k)\mathrm{d}t= \int_{\mathbb{Z}_p} f(t)\mathrm{d}t+\sum_{\ell=0}^{k-1}f'(\ell).$$*

*Proof.* See [@Rob2000 Proposition 2, pp. 265]. ◻

## The first Bernoulli functional $\mathcal{L}_1$

The following definition turns out to be useful:

**Definition 19** ([@{LS2023+} Definition 2.6]). *We define the *first Bernoulli functional* $$\mathcal{L}_1: C^{\dagger}(\mathbb{Z}_p,\mathbb{Q}_p) \longrightarrow \mathbb{Q}_p$$ by $$f = \sum_{k=0}^{+\infty} a_k t^{k} \mapsto \mathcal{L}_1(f) := \sum_{k=0}^{+\infty} \frac{a_kB_{k+1}}{k+1}.$$*

Note that the sum $\sum_{k=0}^{+\infty} a_kB_{k+1}/(k+1)$ is convergent in $\mathbb{Q}_p$ since $\limsup_{k \to +\infty} |a_k|_p^{1/k} < 1$ and $|B_{k+1}/(k+1)|_p \leqslant p(k+1)$ (by the von Staudt-Clausen theorem). The main property of $\mathcal{L}_1$ is the following:

**Lemma 20** ([@{LS2023+} Lemma 2.7]). *For any $f\in C^{\dagger}(\mathbb{Z}_p,\mathbb{Q}_p)$ we have the formula $$\mathcal{L}_1(f')=\int_{\mathbb{Z}_p} f(t) \mathrm{d}t - f(0).$$*

*Proof.* We have $f' \in C^{\dagger}(\mathbb{Z}_p,\mathbb{Q}_p)$ because $C^{\dagger}(\mathbb{Z}_p,\mathbb{Q}_p)$ is clearly closed under taking derivative. Suppose that $f(t) = \sum_{k=0}^{+\infty} a_k t^k$. Then, by Definition 19 and Lemma 17, we have $$\mathcal{L}_1(f') = \sum_{k=1}^{+\infty} a_kB_k = \int_{\mathbb{Z}_p} f(t) \mathrm{d}t - f(0).$$ ◻

**Remark 21**. *The first Bernoulli functional $\mathcal{L}_1$ can be viewed as a de-regularization of the first Bernoulli measure $\mu_{1,\alpha}$ over the space of overconvergent power series. See [@{LS2023+} Proposition 2.9]. This justifies the name of $\mathcal{L}_1$.*

## $p$-Adic Hurwitz zeta functions and $p$-adic zeta values

In this subsection, we will recall some basic facts about $p$-adic Hurwitz zeta functions and $p$-adic zeta values.

Set $q_p = p$ if $p > 2$ and $q_2 = 4$. The units $\mathbb{Z}_p^\times$ of the $p$-adic integers decompose canonically $$\mathbb{Z}_p^\times \cong \mu_{\varphi(q_p)}(\mathbb{Z}_p)\times (1+q_p\mathbb{Z}_p).$$ Here, $\mu_{\varphi(q_p)}(\mathbb{Z}_p)$ denotes the group of $\varphi(q_p)$-th roots of unity in $\mathbb{Z}_p$. The canonical projection $$\omega \colon \mathbb{Z}_p^\times \longrightarrow \mu_{\varphi(q_p)}(\mathbb{Z}_p)$$ is called the *Teichmüller character*, which can be extended multiplicatively to a map $$\mathbb{Q}_p^\times \longrightarrow \mathbb{Q}_p^\times,$$ by setting $$\omega(x):=p^{v_p(x)}\omega\left(\frac{x}{p^{v_p(x)}}\right).$$ We define $$\langle x\rangle:=\frac{x}{\omega(x)}$$ for $x\in\mathbb{Q}_p^\times$. Then, both $\omega(x)$ and $\langle x \rangle$ are multiplicative on $\mathbb{Q}_p^\times$. We have $\langle x \rangle \in 1+q_p\mathbb{Z}_p$ for any $x \in \mathbb{Q}_p^\times$.

For any $x \in \mathbb{Q}_p$ with $|x|_p \geqslant q_p$, for any $s \in \mathbb{C}_p \setminus \{ 1 \}$ with $|s|_p < q_pp^{-1/(p-1)}$, we define $$\label{def_Hur}
\zeta_p(s,x) := \frac{1}{s-1} \int_{\mathbb{Z}_p} \langle t+x \rangle^{1-s} \mathrm{d}t.$$ The function $$\zeta_p(\cdot,x) \colon \left\{ s \in \mathbb{C}_p \setminus \{ 1\} ~\mid~  |s|_p < q_pp^{-1/(p-1)}  \right\} \longrightarrow \mathbb{C}_p$$ is called the *$p$-adic Hurwitz zeta function*. It is known that $\zeta_p(\cdot,x)$ is a $p$-adic meromorphic function on $|s|_p < q_pp^{-1/(p-1)}$, see [@Coh2007 Proposition 11.2.8].

Let $\chi$ be a Dirichlet character of conductor $D$. Let $m$ be a common multiple of $D$ and $q_p$. The *Kubota-Leopoldt $p$-adic $L$-function* is defined by $$\label{def_Kub-Leo}
L_p(s,\chi) := \frac{\langle m \rangle^{1-s}}{m} \sum_{1 \leqslant \nu \leqslant m \atop p \nmid \nu} \chi(\nu) \zeta_p\left(s,\frac{\nu}{m} \right)$$ for $s \in \mathbb{C}_p \setminus \{ 1 \}$ with $|s|_p < q_pp^{-1/(p-1)}$. It is known that the right-hand side of (def_Kub-Leo) is independent of $m$, see [@Coh2007 Proposition 11.3.8(1)].

**Definition 22**. *For any integer $s \geqslant 2$, we define the *$p$-adic zeta value* by $$\zeta_p(s) := L_p(s,\omega^{1-s}).$$*

We remark that, $$\zeta_p(s) = \lim_{k \rightarrow s ~p\text{-adically}\atop k \in \mathbb{Z}_{<0},~~ k\equiv s \pmod{p-1}} \zeta(k) \quad \in \mathbb{Q}_p$$ for any integer $s \geqslant 2$ (see [@Cal2005 Lemma 2.4]) and $\zeta_p(s)$ vanishes when $s$ is a positive even integer.

For our purpose, we need the following lemmas.

**Lemma 23**. *Let $i,l$ be integers such that $i \geqslant 2$ and $l \geqslant 2$. Let $\nu$ be an integer such that $p \nmid \nu$. Let $k$ be any non-negative integer. Then, we have $$- \int_{\mathbb{Z}_p} \frac{1}{(1-i)(t+\nu/p^{l}+k)^{i-1}} \mathrm{d}t = \omega\left( \frac{\nu}{p^{l}} \right)^{1-i} \zeta_p\left(i, \frac{\nu}{p^l} \right)  - \sum_{\ell = 0}^{k-1} \frac{1}{(\ell+\nu/p^{l})^{i}}.$$ (When $k=0$, the empty sum $\sum_{\ell=0}^{k-1}$ is understood as $0$.)*

*Proof.* By Lemma 18 and Eq. (def_Hur), we have $$\begin{aligned}
&- \int_{\mathbb{Z}_p} \frac{1}{(1-i)(t+\nu/p^{l}+k)^{i-1}} \mathrm{d}t \\
=  &- \int_{\mathbb{Z}_p} \frac{1}{(1-i)(t+\nu/p^{l})^{i-1}} \mathrm{d}t  - \sum_{\ell = 0}^{k-1} \frac{1}{(\ell+\nu/p^{l})^{i}} \\
= &\omega\left( \frac{\nu}{p^{l}} \right)^{1-i} \zeta_p\left(i, \frac{\nu}{p^l} \right)  - \sum_{\ell = 0}^{k-1} \frac{1}{(\ell+\nu/p^{l})^{i}}.
\end{aligned}$$ ◻

**Lemma 24**. *Let $i,l$ be integers such that $i \geqslant 2$ and $l \geqslant 2$. Then, we have $$p^{li} \cdot \zeta_p(i) = \sum_{1 \leqslant \nu \leqslant p^{l} \atop p \nmid \nu} \omega\left( \frac{\nu}{p^l} \right)^{1-i}
\zeta_p\left( i, \frac{\nu}{p^{l}} \right).$$*

*Proof.* It follows from Definition 22 and Eq. (def_Kub-Leo) (with $m=p^{l}$). ◻

# Setting of the proof for the $p$-adic case

In this section, we will first set up the parameters. Then we will construct a sequence of rational functions $V_n(t)$ and utilize their primitive functions $W_n(t)$ to produce linear forms in $1$ and $p$-adic odd zeta values.

## Parameters

Fix a positive integer $M$, and fix a finite collection of non-negative integers $\{\delta_j\}_{j=1}^{J}$ such that $$\label{condition_on_deltas_p}
    0 \leqslant \delta_1 \leqslant \delta_2 \leqslant \cdots \leqslant \delta_J < \frac{M}{2}.$$ Here $J \geqslant 1$ denotes the number of $\delta_j$'s.

Let $s$ be a sufficiently large multiple of $2J$. Define the 'power parameter' $l$ as $$\label{defi_l}
    l := \left\lfloor  \frac{\log s - 2\log\log s}{\log p} \right\rfloor.$$ We assume that $s$ is sufficiently large so that $l \geqslant 2$. Note that $l$ is defined in such a way that $p^{l}$ is the largest power of $p$ not exceeding $s/\log^2 s$. The role of the parameter $l$ for the $p$-adic case is similar to that of the 'numerator length parameter' $r$ for the classical case.

## Rational functions and their primitive functions

For any $n \in \mathbb{N}$, we define $$\label{defi_L_n}
L_n :=  \left\lfloor  \frac{\log(M\varphi(p^l)n)}{\log p}  \right\rfloor + 2.$$ Let $w_n$ be the unique integer satisfying $$\begin{aligned}
    w_n &\equiv s-1 + \left( -M\varphi(p^l)+ \frac{s}{J}\sum_{j=1}^{J}(M-2\delta_j) \right)n \pmod{(p-1)p^{L_n}}, \label{w_n_prop_cong} \\
    0 &\leqslant w_n < (p-1)p^{L_n}. \notag
\end{aligned}$$ Note that $$\label{w_n_est}
    0 \leqslant w_n  < p^{l+3}Mn.$$ The definitions of $L_n$ and $w_n$ are technical. They are used in Section 11 to prove certain non-vanishing property. (See Lemma 32.)

For any $n \in \mathbb{N}$, we define the following rational function $V_n(t)$: $$\begin{aligned}
    V_n(t) := & p^{(l+1/(p-1))M\varphi(p^{l})n} \cdot \frac{\prod_{j=1}^{J} ((M-2\delta_j)n)!^{s/J}}{n!^{M\varphi(p^{l})}} \cdot \frac{1}{n!^{\lfloor w_n / n\rfloor}(w_n-\lfloor w_n / n\rfloor n)!} \notag \\
    & \times (t-w_n)_{w_n}  \cdot \frac{\prod_{1 \leqslant \nu \leqslant p^{l} \atop p \nmid \nu} (t+\nu/p^{l})_{Mn}}{\prod_{j=1}^{J} (t+\delta_j n)_{(M-2\delta_j)n+1}^{s/J}},  \label{defi_V_n(t)}
\end{aligned}$$

Since $J \mid s$ and $(p-1) \mid \varphi(p^l)$, we have $V_n(t) \in \mathbb{Q}(t)$. Note that the degree of the rational function $V_n(t)$ is $$\begin{aligned}
    \deg V_n &= w_n + M\varphi(p^{l})n -s - \frac{s}{J}\sum_{j=1}^{J} (M-2\delta_j)n \label{degVn}\\
    &\overset{\text{by~} \eqref{w_n_est}\eqref{condition_on_deltas_p}}{<} p^{l+3}Mn + M\varphi(p^{l})n -s - sn \notag\\
    &\overset{\text{by~} \eqref{defi_l}}{<}  \frac{p^3Msn}{\log^2 s} + \frac{Msn}{\log^2 s} - s - sn. \notag
\end{aligned}$$ We assume that $s$ is sufficiently large so that $$\label{degVnleq-2}
\deg V_n  \leqslant -2, \quad\text{for any~} n \in \mathbb{N}.$$ Thus, the rational function $V_n(t)$ has the partial-fraction decomposition of the form $$\label{defi_bnik}
    V_n(t) =: \sum_{i=1}^{s}\sum_{k=\delta_1 n}^{(M-\delta_1)n} \frac{b_{n,i,k}}{(t+k)^i},$$ where the coefficients $b_{n,i,k} \in \mathbb{Q}$ ($1 \leqslant i \leqslant s,~\delta_1n \leqslant k \leqslant (M-\delta_1)n$) are uniquely determined by $V_n(t)$.

For any $n \in \mathbb{N}$, we define the function $W_n(t)$ by $$\label{defi_W_n(t)}
    W_n(t) := \sum_{k=\delta_1 n}^{(M-\delta_1)n} b_{n,1,k} \log_p\left\langle t+k \right\rangle  + \sum_{i=2}^{s} \sum_{k=\delta_1 n}^{(M-\delta_1)n} \frac{b_{n,i,k}}{(1-i)(t+k)^{i-1}}.$$ The function $W_n(t)$ has basic properties stated in the following lemma, which is in fact our motivation for the definition of $W_n(t)$.

**Lemma 25**. *For any $n \in \mathbb{N}$, the function $W_n(t)$ has the following properties.*

1.  *$W_n(t)$ is a primitive function of $V_n(t)$ on $\mathbb{Q}_p \setminus \left( [-(M-\delta_1)n, -\delta_1n] \cap \mathbb{Z} \right)$; that is, $$W_n^{\prime}(t) = V_n(t), \quad t \in \mathbb{Q}_p \setminus \left( [-(M-\delta_1)n, -\delta_1n] \cap \mathbb{Z} \right).$$*

2.  *For any integer $\nu \in [1,p^{l}]$ with $p \nmid \nu$, the restriction of $W_n(t+\nu/p^{l})$ on $\mathbb{Z}_p$ is an overconvergent power series; that is, $$W_n\left( t+\frac{\nu}{p^{l}} \right)  \in C^\dagger(\mathbb{Z}_p,\mathbb{Q}_p).$$*

3.  *For $|t|_p \geqslant 1$, the function $W_n(t/p^{l})$ can be expressed as a $\mathbb{Q}_p$-coefficient convergent power series in $t^{-1}$ with vanishing constant term.*

*Proof.* (1). By (defi_W_n(t))) and (defi_bnik), we have $$W_n^{\prime}(t) = \sum_{k=\delta_1 n}^{(M-\delta_1)n} \frac{b_{n,1,k}}{t+k}  + \sum_{i=2}^{s} \sum_{k=\delta_1 n}^{(M-\delta_1)n} \frac{b_{n,i,k}}{(t+k)^{i}} = V_n(t)$$ for $t \in \mathbb{Q}_p \setminus \left( [-(M-\delta_1)n, -\delta_1n] \cap \mathbb{Z} \right)$.

(2). For $t \in \mathbb{Z}_p$, we have $$\begin{aligned}
\left\langle t+\frac{\nu}{p^{l}} + k  \right\rangle &= \left\langle \frac{\nu}{p^l} + k \right\rangle \langle 1+(\nu+p^{l}k)^{-1} p^{l}t \rangle \\
&= \left\langle \frac{\nu}{p^l} + k \right\rangle ( 1+(\nu+p^{l}k)^{-1} p^{l}t ).
\end{aligned}$$

Thus, by (defi_W_n(t))) we have $$\begin{aligned}
&~ W_n\left(t+\frac{\nu}{p^l}\right) \\
=&~ \underbrace{\sum_{k=\delta_1 n}^{(M-\delta_1)n} b_{n,1,k}\log_p\left\langle \frac{\nu}{p^l} + k \right\rangle}_{\text{constant}}  + \sum_{k=\delta_1 n}^{(M-\delta_1)n} b_{n,1,k}\underbrace{\log_p( 1+(\nu+p^{l}k)^{-1} p^{l}t)}_{\in C^\dagger(\mathbb{Z}_p,\mathbb{Q}_p)}  \\
&+ \sum_{i=2}^{s} \sum_{k=\delta_1 n}^{(M-\delta_1)n}  \frac{b_{n,i,k}}{(1-i)(\nu/p^l + k)^{i-1}} \underbrace{( 1+(\nu+p^{l}k)^{-1} p^{l}t)^{1-i}}_{\in C^\dagger(\mathbb{Z}_p,\mathbb{Q}_p)}.
\end{aligned}$$ Every summand on the right-hand side above is an overconvergent power series. Therefore, $W_n(t+\nu/p^l) \in C^\dagger(\mathbb{Z}_p,\mathbb{Q}_p)$.

(3). For $|t|_p \geqslant 1$, we have $$\left\langle \frac{t}{p^l} + k \right\rangle = \langle t + p^lk \rangle = \langle t \rangle (1+ p^{l}k t^{-1}).$$ Thus, by (defi_W_n(t))) we have $$\begin{aligned}
W_n\left(\frac{t}{p^l}\right) =&~ \left(\sum_{k=\delta_1 n}^{(M-\delta_1)n} b_{n,1,k}\right) \log_p\langle t \rangle + \sum_{k=\delta_1 n}^{(M-\delta_1)n} b_{n,1,k} \log_p(1+ p^{l}k t^{-1}) \\
&+ \sum_{i=2}^{s} \sum_{k=\delta_1 n}^{(M-\delta_1)n} \frac{p^{l(i-1)}b_{n,i,k}}{(1-i)} t^{1-i} (1+p^l k t^{-1})^{1-i}.
\end{aligned}$$ By (defi_bnik) and (degVnleq-2), we have $$\label{sigma_1=0}
\sum_{k=\delta_1 n}^{(M-\delta_1)n} b_{n,1,k} = \lim_{|t|_p \to +\infty} tV_n(t) = 0.$$ Therefore, for $|t|_p \geqslant 1$, $$\begin{aligned}
W_n\left(\frac{t}{p^l}\right) =&~ \sum_{k=\delta_1 n}^{(M-\delta_1)n} b_{n,1,k} \underbrace{\log_p(1+ p^{l}k t^{-1})}_{\in \mathbb{Q}_p\llbracket p^{l}t^{-1}\rrbracket} \\
&+ \sum_{i=2}^{s} \sum_{k=\delta_1 n}^{(M-\delta_1)n} \frac{p^{l(i-1)}b_{n,i,k}}{(1-i)} t^{1-i} \underbrace{(1+p^l k t^{-1})^{1-i}}_{\in \mathbb{Q}_p\llbracket p^{l}t^{-1}\rrbracket}
\end{aligned}$$ is a $\mathbb{Q}_p$-coefficient convergent power series in $t^{-1}$ with vanishing constant term. ◻

## Linear forms

By Lemma 25)(2), for any integer $\nu \in [1,p^l]$ with $p \nmid \nu$, we have $W_n\left( t+\nu/p^{l} \right)  \in C^\dagger(\mathbb{Z}_p,\mathbb{Q}_p)$. Therefore, $W_n\left( t+\nu/p^{l} \right)$ is Volkenborn integrable by Lemma 17.

**Definition 26**. *For any $n \in \mathbb{N}$, for any integer $\nu \in [1,p^l]$ with $p \nmid \nu$, we define $$\label{def_Tntheta}
T_{n,\nu/p^l} :=  -\int_{\mathbb{Z}_p} W_n\left(t+\frac{\nu}{p^l}\right)\mathrm{d}t.$$ Moreover, we define $$\label{def_Tn}
T_n:= \sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} T_{n,\nu/p^l}.$$*

We define the following coefficients: $$\begin{aligned}
    \sigma_{n,i} &:= \sum_{k=\delta_1n}^{(M-\delta_1)n} b_{n,i,k}, \quad i=1,2,3,\ldots,s, \label{defi_sigma_i} \\
    \sigma_{n,0,\nu/p^l} &:= -\sum_{i=1}^{s}\sum_{k=\delta_1n}^{(M-\delta_1)n}\sum_{\ell=0}^{k-1} \frac{b_{n,i,k}}{(\ell+\nu/p^l)^i}, \quad 1 \leqslant \nu \leqslant p^l \text{~with~} p \nmid \nu. \label{defi_sigma_0_theta} \\
    \sigma_{n,0} &:= \sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} \sigma_{n,0,\nu/p^l}. \label{defi_sigma_0}
\end{aligned}$$ (When $k=0$, the empty sum $\sum_{\ell=0}^{k-1}$ in (defi_sigma_0_theta) is understood as $0$.)

It turs out that $T_{n}$ is a linear form in $1$ and $p$-adic odd zeta values.

**Lemma 27**. *For any $n \in \mathbb{N}$, we have $$T_n = \sigma_{n,0} + \sum_{3 \leqslant i \leqslant s-1 \atop i \text{~odd}} \sigma_{n,i} p^{li} \zeta_p(i)$$ is a linear form in $1$ and $p$-adic odd zeta values, where the coefficients $\sigma_{n,i}$ ($i=3,5,\ldots,s-1$) are defined by (defi_sigma_i) and $\sigma_{n,0}$ is defined by (defi_sigma_0).*

*Proof.* For any integer $\nu \in [1,p^l]$ with $p \nmid \nu$, by (def_Tntheta) and (defi_W_n(t))), we have $$\begin{aligned}
    T_{n,\nu/p^l} =  -& \sum_{k=\delta_1 n}^{(M-\delta_1)n} b_{n,1,k} \int_{\mathbb{Z}_p} \log_p\left\langle t+\frac{\nu}{p^l}+k \right\rangle \mathrm{d}t \notag\\
    -& \sum_{i=2}^{s} \sum_{k=\delta_1 n}^{(M-\delta_1)n} b_{n,i,k} \int_{\mathbb{Z}_p}\frac{1}{(1-i)(t+\nu/p^l+k)^{i-1}} \mathrm{d}t. \label{lin_T_n_theta_equation_1}
\end{aligned}$$ By Lemma 23, we have $$\label{lin_T_n_theta_equation_2}
    - \int_{\mathbb{Z}_p} \frac{1}{(1-i)(t+\nu/p^{l}+k)^{i-1}} \mathrm{d}t = \omega\left( \frac{\nu}{p^{l}} \right)^{1-i} \zeta_p\left(i, \frac{\nu}{p^l} \right)  - \sum_{\ell = 0}^{k-1} \frac{1}{(\ell+\nu/p^{l})^{i}}.$$ By Lemma 18, we have $$\label{lin_T_n_theta_equation_3}
    -\int_{\mathbb{Z}_p} \log_p\left\langle t+\frac{\nu}{p^l}+k \right\rangle \mathrm{d}t = -\int_{\mathbb{Z}_p} \log_p\left\langle t+\frac{\nu}{p^l} \right\rangle \mathrm{d}t - \sum_{\ell=0}^{k-1} \frac{1}{\ell+\nu/p^l}.$$ Substituting (lin_T_n_theta_equation_2) and (lin_T_n_theta_equation_3) into (lin_T_n_theta_equation_1), we obtain $$\begin{aligned}
T_{n,\nu/p^l} = &-\sigma_{n,1} \int_{\mathbb{Z}_p} \log_p\left\langle t+\frac{\nu}{p^l} \right\rangle \mathrm{d}t \\
&+\sigma_{n,0,\nu/p^l} + \sum_{i=2}^{s} \sigma_{n,i} \omega\left( \frac{\nu}{p^{l}} \right)^{1-i} \zeta_p\left(i, \frac{\nu}{p^l} \right).
\end{aligned}$$ Since $\sigma_{n,1} = 0$ by (sigma_1=0), we have $$\label{lin_T_n_theta_equation_4}
T_{n,\nu/p^l} = \sigma_{n,0,\nu/p^l} + \sum_{i=2}^{s} \sigma_{n,i} \omega\left( \frac{\nu}{p^{l}} \right)^{1-i} \zeta_p\left(i, \frac{\nu}{p^l} \right).$$ Finally, substituting (lin_T_n_theta_equation_4) into (def_Tn) and using Lemma 24, we obtain $$T_n =  \sigma_{n,0} + \sum_{i=2}^{s} \sigma_{n,i} p^{li} \zeta_p(i).$$ Since $\zeta_p(i) =0$ for any positive even integer $i$, we complete the proof of Lemma 27. ◻

# Arithmetic properties for the $p$-adic case

Recall that $D_{m} = \operatorname{lcm}[1,2,3,\ldots,m]$. Similar to Lemma 11, we have the following:

**Lemma 28**. *For any integer $n > s^2$, we have $$\Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s-i} \cdot  b_{n,i,k} \in \mathbb{Z}, \quad (1 \leqslant i \leqslant s,~\delta_1n \leqslant k \leqslant (M-\delta_1)n),$$ where the factor $\Phi_n$ is given by (defi_Phi) and (defi_phi).*

*Proof.* The proof is similar to that of Lemma 11. We indicate the modifications.

Fix any $i \in \{1,2,\ldots,s\}$ and any $k \in [\delta_1n,~(M-\delta_1)n] \cap \mathbb{Z}$.

By (defi_bnik), we have $$b_{n,i,k} = \frac{1}{(s-i)!} \left( V_n(t)(t+k)^{s} \right)^{(s-i)} \Big|_{t=-k}.$$

Define the elementrary bricks: $$\begin{aligned}
F_{1,\tau}(t) &= \frac{(t-w_n +\tau n)_n}{n!}, \quad \tau = 0,1,2,\ldots,\lfloor w_n/n\rfloor - 1, \\
F_{1,\lfloor w_n/n\rfloor}(t) &=  \frac{(t-w_n+\lfloor w_n/n\rfloor n)_{w_n - \lfloor w_n/n\rfloor n}}{(w_n - \lfloor w_n/n\rfloor n)!}, \\
F_{\nu/p^l,\tau}(t) &= p^{ln} \cdot p^{\lfloor n/(p-1)\rfloor} \cdot \frac{(t+\nu/p^l+\tau n)_n}{n!}, \\
&\qquad  1 \leqslant \nu \leqslant p^l \text{~with~} p \nmid \nu, \quad \tau=0,1,2,\ldots,M-1, \\
G_j(t) &=  \frac{((M-2\delta_j)n)!}{(t+\delta_jn)_{(M-2\delta_j)n+1}}, \quad j=1,2,\ldots,J.
\end{aligned}$$ Then by (defi_V_n(t))) we have $$V_n(t)(t+k)^s = A \prod_{\tau=0}^{\lfloor w_n/n\rfloor} F_{1,\tau}(t) \cdot \prod_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu }\prod_{\tau=0}^{M-1} F_{\nu/p^l,\tau}(t) \cdot \prod_{j=1}^{J} \left(G_j(t)(t+k)\right)^{s/J},$$ where $A = p^{M\varphi(p^l)\left\{ n/(p-1) \right\}}$ is a positive integer. By Lemma 10, for any polynomial $F(t)$ of the form $F_{1,\tau}(t)$, $F_{\nu/p^l,\tau}(t)$, we have $$D_{n}^{\lambda} \cdot \frac{1}{\lambda!} F^{(\lambda)}(t) \big|_{t=-k} \in \mathbb{Z}$$ for any non-negative integer $\lambda$. By (lem_G_1) of Lemma 9 (with $a_0 = \delta_1n$ and $b_0 = (M-\delta_1)n$), we have $$D_{(M-2\delta_1)n}^{\lambda} \cdot \frac{1}{\lambda!} \left( G_j(t)(t+k) \right)^{(\lambda)} \big|_{t=-k} \in \mathbb{Z}$$ for any $j=1,2,\ldots,J$ and any non-negative integer $\lambda$.

The rest of the proof of Lemma 28 is literally the same as the rest of the proof of Lemma 11, except that we need to replace $a_{n,i,k}$ by $b_{n,i,k}$. ◻

The arithmetic property of $b_{n,i,k}$ propagates to the arithmeric property of $\sigma_{n,i}$ (defined by (defi_sigma_i) and (defi_sigma_0)), as the following lemma shows.

**Lemma 29**. *For any integer $n > s^2$, we have $$\Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s-i} \cdot \sigma_{n,i} \in \mathbb{Z}, \quad i=1,2,\ldots,s,$$ and $$\Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s} \cdot \sigma_{n,0} \in \mathbb{Z}.$$*

*Proof.* The first assertion follows directly from (defi_sigma_i) and Lemma 28.

To prove the second assertion, by (defi_sigma_0), it suffices to prove that for any integer $\nu \in [1,p^l]$ with $p \nmid \nu$ we have $$\label{arith_sigma0theta}
    \Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s} \cdot \sigma_{n,0,\nu/p^l} \in \mathbb{Z}.$$ We prove (arith_sigma0theta) by contradiction. Suppose that $$\label{not_true}
    \Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s} \cdot \sigma_{n,0,\nu/p^l} \notin \mathbb{Z}.$$ By substituting (defi_sigma_0_theta) into (not_true), we obtain that, there exist integers $k_0$, $\ell_0$ such that $\delta_1 n \leqslant k_0 \leqslant (M-\delta_1)n$, $0 \leqslant \ell_0 < k_0$, and $$\label{not_true_2}
\Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s} \sum_{i=1}^{s} \frac{b_{n,i,k_0}}{(\ell_0+\nu/p^l)^{i}} \notin \mathbb{Z}.$$ Write $\nu^{\prime} = p^l - \nu$. Note that $t+k_0-\ell_0-\nu/p^l$ is a factor of $(t+\nu^{\prime}/p^l)_{Mn}$. Thus, $t+k_0-\ell_0-\nu/p^l$ is a factor of the numerator of $V_n(t)$ (see (defi_V_n(t)))). We have $$\label{V_n(t)_has_root}
    V_n\left(-k_0+\ell_0+\frac{\nu}{p^l} \right) = 0$$ Substituting (defi_bnik) into (V_n(t)\_has_root)_has_root), and using (not_true_2), we obtain $$\begin{aligned}
&~ \Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s} \sum_{i=1}^{s} \frac{b_{n,i,k_0}}{(\ell_0+\nu/p^l)^{i}} \\
=&~ -\Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s} \sum_{i=1}^{s}\sum_{k=\delta_1n \atop k \neq k_0}^{(M-\delta_1)n} \frac{b_{n,i,k}}{(k-k_0+\ell_0+\nu/p^l)^i} \not\in\mathbb{Z}.
\end{aligned}$$ Therefore, there exist a prime $q$, two integers $i_0,i_1 \in \{1,2,\ldots,s\}$, and an integer $k_1 \in \{\delta_1 n,\ldots, (M-\delta_1)n\}$ with $k_1 \neq k_0$ such that $$\begin{aligned}
v_q\left( \Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s} \cdot \frac{b_{n,i_0,k_0}}{(\ell_0+\nu/p^l)^{i_0}}  \right)  &< 0, \\
v_q\left( \Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s} \cdot \frac{b_{n,i_1,k_1}}{(k_1-k_0+\ell_0+\nu/p^l)^{i_1}}  \right) &< 0.
\end{aligned}$$ On the other hand, by Lemma 28, we have $$v_q\left( \Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s-i_0} \cdot b_{n,i_0,k_0} \right) \geqslant 0, \quad v_q\left( \Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s-i_1} \cdot b_{n,i_1,k_1}  \right) \geqslant 0.$$ Therefore, $$v_q\left( \ell_0 + \frac{\nu}{p^l} \right) > v_q(D_{(M-2\delta_1)n}), \quad v_q\left( k_1-k_0+\ell_0+\frac{\nu}{p^l} \right) > v_q(D_{(M-2\delta_1)n}).$$ It follows that $v_q(k_1-k_0) > v_q(D_{(M-2\delta_1)n})$, which is a contradiction because $0<|k_1-k_0| \leqslant (M-2\delta_1)n$. The proof of Lemma 29 is complete. ◻

# Archimedean estimates

In this section we will estimate the Archimedean norm of the coefficients $\sigma_{n,i}$ ($i=0,1,2,\ldots,s$) defined by (defi_sigma_0) and (defi_sigma_i).

**Lemma 30**. *We have $$\label{sigma_estimate}
\max_{0 \leqslant i \leqslant s} |\sigma_{n,i}| \leqslant \exp\left( \beta_p(s)n + o(n) \right), \quad \text{as~} n \to +\infty,$$ where $\beta_p(s)$ is a constant independent of $n$. Moreover, we have $$\label{beta_p}
\beta_p(s) \sim \log2 \cdot \frac{s}{J} \sum_{j=1}^{J} (M - 2\delta_j), \quad\text{as~} s \to +\infty.$$*

*Proof.* By (defi_sigma_i)--(defi_sigma_0), we have $$\label{sigma<b}
\max_{0 \leqslant i \leqslant s} |\sigma_{n,i}| \leqslant (Mn+1)^{2}sp^{l(s+1)} \cdot \max_{i,k} |b_{n,i,k}|,$$ where $\max_{i,k}$ is taken over all $i \in \{ 1,2,\ldots,s \}$ and $k \in [\delta_1n, (M-\delta_1)n] \cap \mathbb{Z}$.

Now fix any pair of $i,k$ in the range above. By (defi_bnik) and Cauchy's integral formula, we have $$b_{n,i,k} = \frac{1}{2\pi \sqrt{-1}} \int_{|z+k|=1/p^{l+1}} (z+k)^{i-1}V_n(z)~\mathrm{d}z.$$ Therefore, we have (recall (defi_V_n(t)))) $$\begin{aligned}
    |b_{n,i,k}| &\leqslant \max_{|z+k| = 1/p^{l+1}} |V_n(z)| \notag\\
    =&~ p^{(l+1/(p-1))M\varphi(p^{l})n} \cdot \frac{\prod_{j=1}^{J} ((M-2\delta_j)n)!^{s/J}}{n!^{M\varphi(p^{l})}} \cdot \frac{1}{n!^{\lfloor w_n / n\rfloor}(w_n-\lfloor w_n / n\rfloor n)!} \notag \\
    & \times \max_{|z+k|=1/p^{l+1}} |(z-w_n)_{w_n}| \frac{\prod_{1 \leqslant \nu \leqslant p^{l} \atop p \nmid \nu} |(z+\nu/p^{l})_{Mn}|}{\prod_{j=1}^{J} |(z+\delta_j n)_{(M-2\delta_j)n+1}|^{s/J}}. \label{|b|<maxV}
\end{aligned}$$ In the following, the complex number $z$ is always on the circle $|z+k|=1/p^{l+1}$. We will use triangle inequality to bound (\|b\|\<maxV) from above.

We have $$\begin{aligned}
&~ \max_{|z+k|=1/p^{l+1}} \frac{|(z-w_n)_{w_n}|}{n!^{\lfloor w_n / n\rfloor}(w_n-\lfloor w_n / n\rfloor n)!} \notag\\
\leqslant&~  \frac{(Mn+2)(Mn+3)\cdots(Mn+w_n+1)}{n!^{\lfloor w_n / n\rfloor}(w_n-\lfloor w_n / n\rfloor n)!} \notag\\
=&~ \frac{(Mn+w_n+1)!}{(Mn+1)!n!^{\lfloor w_n / n\rfloor}(w_n-\lfloor w_n / n\rfloor n)!} \notag\\
\leqslant&~ \left( \underbrace{1+1+\cdots+1}_{\lfloor w_n/n \rfloor + 2} \right)^{Mn+w_n+1} \notag\\
\overset{\text{by~} \eqref{w_n_est}}{\leqslant}&~    (p^{l+3}M+2)^{Mn+p^{l+3}Mn + 1}. \label{p_est1}
\end{aligned}$$ For any integer $\nu \in [1,p^l]$ with $p \nmid \nu$, we have $$\begin{aligned}
\max_{|z+k|=1/p^{l+1}} \frac{|(z+\nu/p^{l})_{Mn}|}{n!^M} &\leqslant \frac{(k+1)!(Mn+1-k)!}{n!^M} \notag\\
&\leqslant \frac{(Mn+2)!}{n!^M} = (Mn+2)(Mn+1) \cdot \frac{(Mn)!}{n!^M} \notag\\
& \leqslant 10M^2n^2 \cdot M^{Mn}. \label{p_est2}
\end{aligned}$$ Similar to the proof of (est3), we have $$\label{p_est3}
    \max_{|z+k| = 1/p^{l+1}} \frac{((M-2\delta_j)n)!}{|(z+\delta_jn)_{(M-2\delta_j)n+1}|} \leqslant p^{3(l+1)}M^2n^2 \cdot 2^{(M-2\delta_j)n}.$$ Combining all the equations (sigma\<b)--(p_est3), we obtain $$\max_{0 \leqslant i \leqslant s} |\sigma_{n,i}| \leqslant \exp\left( \beta_p(s)n + o(n) \right), \quad \text{as~} n \to +\infty,$$ where $$\begin{aligned}
\beta_p(s) =&~ \left( l+\frac{1}{p-1} \right)M\varphi(p^l)\log p + M\varphi(p^l)\log M \\
&+ (p^{l+3}+1)M\log(p^{l+3}M+2) + \log 2 \cdot \frac{s}{J} \sum_{j=1}^{J} (M - 2\delta_j).
\end{aligned}$$

By (defi_l), we have $$\varphi(p^l)<p^l \leqslant \frac{s}{\log^2 s}, \quad l\log p < \log s.$$ Therefore, $$\beta_p(s) \sim \log2 \cdot \frac{s}{J} \sum_{j=1}^{J} (M - 2\delta_j), \quad\text{as~} s \to +\infty.$$ ◻

# $p$-Adic estimates

In this section we will determine the $p$-adic norm of $T_n$ (defined by (def_Tn)).

By Eq. (def_Tntheta), Lemma 20 and Lemma 25)(1)(2), we have $$\label{T_ntheta_L1}
T_{n,\nu/p^l} = - \mathcal{L}_1\left( V_n\left(t+\frac{\nu}{p^l}\right) \right) - W_n\left( \frac{\nu}{p^l} \right)$$ for any integer $\nu \in [1,p^l]$ with $p \nmid \nu$. Substituting (T_ntheta_L1) into (def_Tn), we have $$\label{T_n_L1}
T_n = -\sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu}  \mathcal{L}_1\left( V_n\left(t+\frac{\nu}{p^l}\right) \right) - \sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} W_n\left( \frac{\nu}{p^l} \right).$$

In the rest of this section, we will show that

-   For any sufficiently large $n \in \mathbb{N}$, we can explicitly determine the $p$-adic order of $\sum_{\nu} W_n(\nu/p^l)$.

-   For any sufficiently large $n \in \mathbb{N}$, the $p$-adic order of $\mathcal{L}_1\left( V_n\left(t+\nu/p^l\right) \right)$ is strictly larger than the $p$-adic order of $\sum_{\nu} W_n(\nu/p^l)$.

In this way, we can explicitly determine $|T_n|_p$ for any sufficiently large $n \in \mathbb{N}$.

We need an elementrary lemma:

**Lemma 31**. *For any $m \in \mathbb{Z}$, we have $$v_p\left( \sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} \nu^{m} \right) \geqslant l-1.$$*

*Proof.* For any positive integer $N$, for any integer $\nu \in[1,p^l]$ with $p \nmid \nu$, we have $$\nu^{N\varphi(p^l)+m} \equiv \nu^{m} \pmod{p^{l}\mathbb{Z}_p}.$$ Replacing $m$ by $N\varphi(p^l)+m$ for some sufficiently large positive integer $N$, we may assume without loss of generality that $m > 0$. Then, the conclusion follows by an easy induction on $l$. ◻

Now, we explicitly determine the $p$-adic order of $\sum_{\nu} W_n(\nu/p^l)$.

**Lemma 32**. *For any sufficiently large $n \in \mathbb{N}$, we have $$\begin{aligned}
&~v_p\left( \sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} W_n\left( \frac{\nu}{p^l} \right) \right) \notag\\
=&~ \left( l + \frac{1}{p-1} \right)M\varphi(p^l)n + \frac{s}{J} \sum_{j=1}^{J} v_p(((M-2\delta_j)n)!) \notag\\
&- M\varphi(p^l)v_p\left( n! \right) - \left\lfloor \frac{w_n}{n} \right\rfloor v_p(n!) - v_p\left( \left( w_n -\left\lfloor \frac{w_n}{n} \right\rfloor n \right)! \right) \notag\\
&+ l|\deg V_n|  - v_p(|\deg V_n| - 1) - 1. \label{v_p(sumWn)}
\end{aligned}$$ (The main term on the right-hand side above is $l|\deg V_n|$). In particular, we have $$\label{p_adic_norm_of_sumWn}
 \exp\left( -\alpha_{p,1}(s)n + o(n) \right) \leqslant \left| \sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} W_n\left( \frac{\nu}{p^l} \right) \right|_p \leqslant \exp\left( -\alpha_{p,2}(s)n + o(n) \right)$$ as $n \to +\infty$, where $$\begin{aligned}
    \alpha_{p,1}(s) &= \frac{sl\log p}{J} \sum_{j=1}^{J} (M-2\delta_j) + \frac{s\log p}{(p-1)J}\sum_{j=1}^{J} (M-2\delta_j),  \label{defi_alpha_1}\\
    \alpha_{p,2}(s) &= \alpha_{p,1}(s) - \left( l+\frac{1}{p-1}\right)p^{l+3}M. \label{defi_alpha_2}
\end{aligned}$$*

*Proof.* By (defi_V_n(t))), we have $$\begin{aligned}
&~ V_n\left( \frac{t}{p^l} \right) \notag\\
=&~ p^{(l+1/(p-1))M\varphi(p^{l})n} \cdot \frac{\prod_{j=1}^{J} ((M-2\delta_j)n)!^{s/J}}{n!^{M\varphi(p^{l})}} \cdot \frac{1}{n!^{\lfloor w_n / n\rfloor}(w_n-\lfloor w_n / n\rfloor n)!} \notag \\
&\times p^{l|\deg V_n|} \cdot t^{-|\deg V_n|} \notag\\
&\times \prod_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu}\prod_{\tau=0}^{Mn-1} \left( 1+(\nu+p^l\tau)t^{-1} \right) \label{PPP}\\
&\times \frac{\prod_{\tau=1}^{w_n}\left( 1 -\tau p^{l} t^{-1} \right)}{\prod_{j=1}^{J}\prod_{\tau=0}^{(M-2\delta_j)n}\left( 1+(\delta_j n + \tau)p^{l} t^{-1} \right)^{s/J}}. \label{QQQ}
\end{aligned}$$ Note that the product in the line (PPP) is a $\mathbb{Z}_p$-coefficient polynomial in $t^{-1}$ of degree $M\varphi(p^l)n$. The product in the line (QQQ) belongs to $\mathbb{Z}_p\llbracket p^{l}t^{-1} \rrbracket$. Therefore, we can write $V_n(t/p^{l})$ as $$\begin{aligned}
&~ V_n\left( \frac{t}{p^l} \right) \notag\\
=&~ p^{(l+1/(p-1))M\varphi(p^{l})n} \cdot \frac{\prod_{j=1}^{J} ((M-2\delta_j)n)!^{s/J}}{n!^{M\varphi(p^{l})}} \cdot \frac{1}{n!^{\lfloor w_n / n\rfloor}(w_n-\lfloor w_n / n\rfloor n)!} \notag \\
&\times p^{l|\deg V_n|} \cdot t^{-|\deg V_n|} \sum_{k=0}^{+\infty} h_k t^{-k}, \label{V_n(t/p^l)_in_t^-1}
\end{aligned}$$ where the coefficients $h_k \in \mathbb{Z}_p$ ($k=0,1,2,\ldots$) satisfy $$\label{v_p(h_k)}
v_p(h_k) \geqslant l \max\left\{ 0, k - M\varphi(p^l)n \right\}.$$

By Lemma 25)(3), the function $W_n(t/p^l)$ can be expressed as a $\mathbb{Q}_p$-coefficient convergent power series of $t^{-1}$ for $|t|_p \geqslant 1$ with vanishing constant term. Moreover, by Lemma 25)(1), we have $$\label{Wnprime=Vn}
\frac{\mathrm{d}}{\mathrm{d}t} \left( W_n\left( \frac{t}{p^l} \right) \right) = \frac{1}{p^l} V_n\left( \frac{t}{p^l} \right), \quad |t|_p \geqslant 1.$$ Comparing (Wnprime=Vn) to (V_n(t/p\^l)\_in_t\^-1)_in_t^-1), we obtain $$\begin{aligned}
&~\sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} W_n\left( \frac{\nu}{p^l} \right) \\
=&~ p^{(l+1/(p-1))M\varphi(p^{l})n} \cdot \frac{\prod_{j=1}^{J} ((M-2\delta_j)n)!^{s/J}}{n!^{M\varphi(p^{l})}} \cdot \frac{1}{n!^{\lfloor w_n / n\rfloor}(w_n-\lfloor w_n / n\rfloor n)!} \notag\\
&\times p^{l|\deg V_n|} \cdot \frac{1}{p^l} \notag \\
&\times \sum_{k=0}^{+\infty} \frac{h_k}{-|\deg V_n|-k+1} \sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} \nu^{-|\deg V_n|-k+1}.  \label{expression_sumWn}
\end{aligned}$$ In the following, we will prove that for any sufficiently large $n \in \mathbb{N}$ $$\begin{aligned}
\label{claim}
    &~ v_p\left(  \frac{h_k}{-|\deg V_n|-k+1} \sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} \nu^{-|\deg V_n|-k+1}  \right) \notag\\
    >&~ v_p\left(  \frac{h_0}{-|\deg V_n|+1} \sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} \nu^{-|\deg V_n|+1} \right), \quad \text{for any~} k>0.
\end{aligned}$$

Note that $h_0 = 1$. By (degVn) and (w_n_prop_cong), we have $$\label{1-|degVn|}
-|\deg V_n| + 1 \equiv 0 \pmod{(p-1)p^{L_n}}.$$ Since $L_n > l$ by (defi_L_n), we have $\varphi(p^{l}) \mid (-|\deg V_n|+1)$. Thus, $$\sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} \nu^{-|\deg V_n|+1}  \equiv  \sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} 1 \equiv p^{l-1}(p-1) \pmod{p^l\mathbb{Z}_p}.$$ Therefore, $$\label{v_p(0th)}
v_p\left(  \frac{h_0}{-|\deg V_n|+1} \sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} \nu^{-|\deg V_n|+1} \right) = l-1 -v_p\left( |\deg V_n| - 1 \right).$$

For $k>0$, we consider two cases.

Case 1: $v_p(k) < v_p(|\deg V_n| - 1)$. In this case, we have $v_p(-|\deg V_n|-k+1) = v_p(k) < v_p(|\deg V_n| - 1)$. By (v_p(h_k))) and Lemma 31, we have $v_p(h_k) \geqslant 0$ and $$v_p\left( \sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} \nu^{-|\deg V_n|-k+1} \right) \geqslant l-1.$$ In conclusion, (claim) is true for Case 1.

Case 2: $v_p(k) \geqslant v_p(|\deg V_n| - 1)$. In this case, by (1-\|degVn\|) we have $v_p(k) \geqslant L_n$. Then, by $k>0$ and (defi_L_n), we have $$\label{k_is_large}
k \geqslant p^{L_n} > p \cdot M\varphi(p^l)n \geqslant 2 \cdot M\varphi(p^l)n.$$ By (v_p(h_k))), we have $$\label{case2_eq1}
v_p(h_k) \geqslant l \cdot (k - M\varphi(p^l)n) > 2 \cdot \frac{k}{2} = k.$$ Combining (case2_eq1) and Lemma 31, we have $$\begin{aligned}
&~ v_p\left(  \frac{h_k}{-|\deg V_n|-k+1} \sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} \nu^{-|\deg V_n|-k+1}  \right) \\
>&~ k - v_p(|\deg V_n|+k-1) + l - 1.
\end{aligned}$$ In view of (v_p(0th))), to prove (claim), it suffices to prove that $$k + v_p\left( |\deg V_n| - 1 \right) > v_p(|\deg V_n|+k-1).$$ Since $v_p\left( |\deg V_n| - 1 \right) \geqslant L_n >0$, it suffices to prove that $$k > \frac{\log(|\deg V_n|+k-1)}{\log p},$$ or $$p^k > |\deg V_n|+k-1.$$ By (degVn), we have $|\deg V_n|+k-1 < Msn + k$ for sufficiently large $n$. Note that $k > n$ by (k_is_large). If $n$ is large enough, we have $$2^k > Msn + k, \quad \text{for any~} k > n.$$ Therefore, the claimed (claim) is true for any sufficiently large $n$.

By (expression_sumWn), (claim) and (v_p(0th))), we obtain the desired explicit expression of $v_p(\sum_{\nu} W_n(\nu/p^l))$ for any sufficiently large $n \in \mathbb{N}$, as stated in (v_p(sumWn))). Since $v_p(n!) = n/(p-1) + O(\log n)$ and $0 \leqslant w_n < p^{l+3}Mn$ (see (w_n_est)), Eq. (v_p(sumWn))) implies (p_adic_norm_of_sumWn). The proof of Lemma 32 is complete. ◻

Next, we bound from below the $p$-adic order of $\mathcal{L}_1(V_n(t+\nu/p^l))$.

**Lemma 33**. *For any $n\in \mathbb{N}$, for any integer $\nu \in [1,p^l]$ with $p \nmid \nu$, we have $$\begin{aligned}
&~ v_p\left( \mathcal{L}_1\left( V_n\left( t+\frac{\nu}{p^l} \right) \right) \right) \notag\\
\geqslant& ~\left( l + \frac{1}{p-1} \right)M\varphi(p^l)n + \frac{s}{J} \sum_{j=1}^{J} v_p(((M-2\delta_j)n)!) \notag\\
&- M\varphi(p^l)v_p\left( n! \right) - \left\lfloor \frac{w_n}{n} \right\rfloor v_p(n!) - v_p\left( \left( w_n -\left\lfloor \frac{w_n}{n} \right\rfloor n \right)! \right) \notag\\
&+ l|\deg V_n|  +lMn -1-\frac{\log(Mn+1)}{\log p}. \label{v_p(L_1(V_n(shift)))}
\end{aligned}$$*

*Proof.* By (defi_V_n(t))), we have $$\begin{aligned}
&~ V_n\left(t+\frac{\nu}{p^l}\right) \notag\\
=&~ p^{(l+1/(p-1))M\varphi(p^{l})n} \cdot \frac{\prod_{j=1}^{J} ((M-2\delta_j)n)!^{s/J}}{n!^{M\varphi(p^{l})}} \cdot \frac{1}{n!^{\lfloor w_n / n\rfloor}(w_n-\lfloor w_n / n\rfloor n)!} \notag \\
&\times p^{l|\deg V_n|} \cdot p^{lMn} \notag\\
&\times \prod_{\tau=0}^{Mn-1} (t+\tau+1) \cdot  \prod_{1 \leqslant \nu^{\prime} \leqslant p^{l} \atop p \nmid \nu^{\prime},~\nu^{\prime}\neq \nu}\prod_{\tau=0}^{Mn-1} (p^lt+p^{l}\tau+\nu+\nu^{\prime}) \label{PP}\\
&\times
\frac{\prod_{\tau=1}^{w_n}(p^{l}t-p^{l}\tau+\nu)}{\prod_{j=1}^{J}\prod_{\tau=0}^{(M-2\delta_j)n}(p^{l}t+p^{l}\tau+\nu)^{s/J}}. \label{QQ}
\end{aligned}$$ The first product in the line (PP) is a $\mathbb{Z}_p$-coefficient polynomial in $t$ of degree $Mn$. The second product in the line (PP) and the product in the line (QQ) both belong to $\mathbb{Z}_p\llbracket p^{l}t \rrbracket$. Therefore, we can write $V_n(t+\nu/p^l)$ as $$\begin{aligned}
&~ V_n\left(t+\frac{\nu}{p^l}\right) \notag\\
=&~ p^{(l+1/(p-1))M\varphi(p^{l})n} \cdot \frac{\prod_{j=1}^{J} ((M-2\delta_j)n)!^{s/J}}{n!^{M\varphi(p^{l})}} \cdot \frac{1}{n!^{\lfloor w_n / n\rfloor}(w_n-\lfloor w_n / n\rfloor n)!} \notag \\
&\times p^{l|\deg V_n|} \cdot p^{lMn} \cdot \sum_{k=0}^{+\infty} u_kt^{k},  \label{expression_for_Vn(shift)}
\end{aligned}$$ where the coefficients $u_k \in \mathbb{Z}_p$ ($k=0,1,2,\ldots$) satisfy $$\label{v_p(u_k)>}
    v_p(u_k) \geqslant l\max\left\{ 0, k -Mn \right\}.$$

By (expression_for_Vn(shift))) and Definition 19, we have $$\begin{aligned}
&~ \mathcal{L}_1\left( V_n\left(t+\frac{\nu}{p^l}\right) \right) \notag\\
= &~ p^{(l+1/(p-1))M\varphi(p^{l})n} \cdot \frac{\prod_{j=1}^{J} ((M-2\delta_j)n)!^{s/J}}{n!^{M\varphi(p^{l})}} \cdot \frac{1}{n!^{\lfloor w_n / n\rfloor}(w_n-\lfloor w_n / n\rfloor n)!} \notag \\
&\times p^{l|\deg V_n|} \cdot p^{lMn} \cdot \sum_{k=0}^{+\infty} \frac{u_kB_{k+1}}{k+1}. \label{L1Vnshift}
\end{aligned}$$ By (v_p(u_k)\>)>) and the von Staudt-Clausen theorem, we have $$\begin{aligned}
     &~\inf_{k \geqslant 0} v_p\left( \frac{u_kB_{k+1}}{k+1} \right)  \notag\\
    \geqslant&~ \inf_{k \geqslant 0} \left( -1-\frac{\log(k+1)}{\log p} + \max\left\{ 0, k -Mn \right\} \right)  \notag\\
    =& -1-\frac{\log(Mn+1)}{\log p}. \label{inf_vp(L1(u_kt^k))}
\end{aligned}$$ By (L1Vnshift) and (inf_vp(L1(u_kt\^k))))), we obtain (v_p(L_1(V_n(shift))))))). The proof of Lemma 33))) is complete. ◻

Now, we can determine $|T_n|_p$ explicitly for any sufficiently large $n \in \mathbb{N}$.

**Lemma 34**. *We have $$\label{p_adic_norm_Tn}
    \exp\left( -\alpha_{p,1}(s)n + o(n) \right) \leqslant \left| T_n \right|_p \leqslant \exp\left( -\alpha_{p,2}(s)n + o(n) \right), \quad\text{as~} n \to +\infty,$$ where $\alpha_{p,1}(s),\alpha_{p,2}(s)$ are given by (defi_alpha_1) and (defi_alpha_2), respectively. Moreover, we have $$\begin{aligned}
    \alpha_{p,1}(s) &\sim  \frac{s\log s}{J} \sum_{j=1}^{J}(M-2\delta_j), \quad\text{as~} s \to  +\infty, \label{est_alpha_1}\\
    \alpha_{p,1}(s) - \alpha_{p,2}(s) &= O\left(\frac{s}{\log s}\right), \quad\text{as~} s \to  +\infty. \label{est_alpha_2}
\end{aligned}$$*

*Proof.* By Lemma 32 and Lemma 33))), and noting that $$lMn -1 -\frac{\log(Mn+1)}{\log p} > -v_p(|\deg V_n|-1) - 1$$ for any sufficiently large $n \in \mathbb{N}$, we obtain $$\label{yeah}
    v_p\left(  \sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu}  \mathcal{L}_1\left( V_n\left(t+\frac{\nu}{p^l}\right) \right)  \right) > v_p\left( \sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} W_n\left( \frac{\nu}{p^l} \right) \right).$$ Combining (yeah) and (T_n_L1), we have $$|T_n|_p = \left| \sum_{1 \leqslant \nu \leqslant p^l \atop p \nmid \nu} W_n\left( \frac{\nu}{p^l} \right) \right|_p$$ for any sufficiently large $n \in \mathbb{N}$. Then (p_adic_norm_Tn) follows from (p_adic_norm_of_sumWn).

By (defi_l), we have $$\begin{aligned}
    l\log p &= \log s + O(\log\log s), \quad\text{as~} s\to +\infty, \\
    lp^{l} &= O\left( \frac{s}{\log s} \right), \quad\text{as~} s\to +\infty.
\end{aligned}$$ Therefore, the aymptotic estimates for $\alpha_{p,1}(s)$ and $\alpha_{p,1}(s) -\alpha_{p,2}(s)$ follow. ◻

# Proof of Theorem 2

We first reduce the proof of Theorem 2 to a computational problem.

**Proposition 35**. *Let $\psi(\cdot)$ be the digamma function. For any collection of non-negative integers $(M,\delta_1,\delta_2,\ldots,\delta_J)$ under the constraints $J \geqslant 1$ and $$0 \leqslant \delta_1 \leqslant \delta_2 \leqslant \cdots \leqslant \delta_J < \frac{M}{2},$$ we define $$\varpi = \int_{0}^{1} \phi(x)~\mathrm{d}\psi(x) - \int_{0}^{1/(M-2\delta_1)} \phi(x)~\frac{\mathrm{d}x}{x^2},$$ where the function $\phi(\cdot)$ is given by $$\phi(x) = \inf_{y \in \mathbb{R}} \sum_{j=1}^{J}  \left( \lfloor(m-2\delta_j)x\rfloor - \lfloor y-\delta_j x \rfloor - \lfloor (m-\delta_j)x - y \rfloor \right).$$*

*Then, we have $$\dim_{\mathbb{Q}}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta_p(3),\zeta_p(5),\ldots,\zeta_p(s-1) \right) \geqslant (C^{\prime}-o(1)) \cdot \log s,$$ as the even integer $s \to +\infty$, where the constant $$\label{defi_C^prime}
C^{\prime} = \frac{\sum_{j=1}^{J} (M-2\delta_j) }{\log2 \cdot \sum_{j=1}^{J}(M-2\delta_j)  - \varpi  + J \cdot (M-2\delta_1)}.$$*

*Proof.* For any integer $n>s^2$, consider $$\widehat{T}_n := \Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s} \cdot T_n,$$ By Lemma 27 and Lemma 29, we have that $$\widehat{T}_n = \widehat{\sigma}_{n,0} + \sum_{3 \leqslant i \leqslant s-1 \atop i \text{~odd}} \widehat{\sigma}_{n,i}\zeta_p(i)$$ is a linear form in $1$ and odd zeta values with integer coefficients $$\widehat{\sigma}_{n,i} := \Phi_n^{-s/J} D_{(M-2\delta_1)n}^{s} \cdot \sigma_{n,i} \cdot p^{li} \in \mathbb{Z}, \quad i=0,3,5,\ldots,s-1.$$ By Lemma 34, the facts $v_p(\Phi_n)=0$ for $n>p^2$ and $v_p(D_{(M-2\delta_1)n})=O(\log n)$, we have $$\exp\left( -\widehat{\alpha_{p,1}}(s)n+o(n) \right) \leqslant |\widehat{T}_n|_p \leqslant \exp\left( -\widehat{\alpha_{p,2}}(s)n+o(n) \right),  \quad \text{as~} n\to +\infty,$$ where $$\widehat{\alpha_{p,j}}(s) = \alpha_{p,j}(s), \quad j=1,2.$$ By Lemma 30, Eq. (PNT) and Lemma 15, we have $$\max_{i=0,3,5,\ldots,s-1} |\widehat{\sigma}_{n,i}| \leqslant \exp\left( \widehat{\beta_p}(s)n + o(n) \right), \quad \text{as~} n\to +\infty,$$ where $$\widehat{\beta_p}(s) = \beta_p(s) - \frac{s}{J}\varpi + s(M-2\delta_1).$$

By (est_alpha_1), (est_alpha_2) and (beta_p), we have the following asymptotic estimates for $\widehat{\alpha_{p,j}}(s)$ and $\widehat{\beta_p}(s)$ as $s \to +\infty$: $$\begin{aligned}
\widehat{\alpha_{p,1}}(s) &\sim  \frac{s\log s}{J}\sum_{j=1}^{J}(M-2\delta_j),   \label{alphahat_1}\\
\widehat{\alpha_{p,1}}(s) - \widehat{\alpha_{p,2}}(s) &= O\left( \frac{s}{\log s} \right), \label{alphahat_2}\\
\widehat{\beta_p}(s) &\sim  \log 2 \cdot \frac{s}{J}\sum_{j=1}^{J}(M-2\delta_j) - \frac{s}{J}\varpi + s(M-2\delta_1). \label{betahat_p}
\end{aligned}$$ Applying Nesterenko's $p$-adic linear independence criterion (Theorem 7) to the sequence of linear forms $\{ \widehat{T}_n \}_{n > s^2}$, and using (alphahat_1)--(betahat_p), we obtain $$\begin{aligned}
\dim_{\mathbb{Q}}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta_p(3),\zeta_p(5),\ldots,\zeta_p(s-1) \right) &\geqslant \frac{\widehat{\alpha_{p,1}}(s)}{\widehat{\beta_p}(s) + \widehat{\alpha_{p,1}}(s) - \widehat{\alpha_{p,2}}(s) } \notag \\
&= (C^{\prime}-o(1)) \cdot \log s, \quad \text{as~} s \to +\infty, \label{dim>C^primelogs}
\end{aligned}$$ where the constant $$C^{\prime} = \frac{\sum_{j=1}^{J} (M-2\delta_j) }{\log2 \cdot \sum_{j=1}^{J}(M-2\delta_j)  - \varpi  + J\cdot(M-2\delta_1)}.$$

We have restricted that $s \in 2J\mathbb{N}$ in our constructions of rational functions and linear forms. So (dim\>C\^primelogs) is true as $s \in 2J\mathbb{N}$ and $s \to +\infty$. But clearly, if we replaced the condition "$s \in 2J\mathbb{N}$" by "$s \in 2\mathbb{N}$", the conclusion (dim\>C\^primelogs) is still true. ◻

If we take $M=1$, $\delta_1=0$, ($J=1$) in Proposition 35, then $\phi(x) \equiv 0$, $\varpi = 0$ and $C = 1/(1+\log 2)$. Thus, we rediscover Sprang's theorem [@Spr20]. The simplest parameters to improve Sprang's theorem are: $M=6$, $\delta_1=0$, $\delta_2=1$, ($J=2$). This collection of parameters leads to the proof of Theorem 2.

*Proof of Theorem 2.* Take $M=6$, $\delta_1=0$, $\delta_2=1$, ($J=2$) in Proposition 35. As we have calculated in the proof of Theorem 1 (see Section 6), $\varpi = 2.157479\ldots$. Then, by (defi_C\^prime), we have $$C^{\prime} =  \frac{10}{10\log 2 - \varpi + 12} = \frac{1.009388\ldots}{1+\log 2}.$$ In conclusion, by Proposition 35 we have $$\dim_{\mathbb{Q}}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta_p(3),\zeta_p(5),\ldots,\zeta_p(s-1) \right) \geqslant \frac{1.009}{1+\log 2} \cdot \log s$$ for any sufficiently large even integer $s$. The proof of Theorem 2 is complete. ◻

# Computational explorations

In this section, we will present computational results and prove Claim 3 and Claim 4.

Recall that Proposition 16 and Proposition 35 reduce theoretic problems to computational problems. Since the dependence of $\varpi$ (and hence $C$, $C^{\prime}$) on the parameters is discrete, it is unlikely to find an optimal constant $C$ for Proposition 16 or an optimal constant $C^{\prime}$ for Proposition 35.

The parameters $M=6$, $\delta_1 = 0$, $\delta_2 = 1$, ($J=2$) that we used in the proofs of Theorem 1 and Theorem 2 are very simple. We have discovered some other simple parameters to improve the constant $1.009/(1+\log 2)$ in Theorem 1 and Theorem 2:

-   $M=19$, $(\delta_1,\delta_2,\delta_3)=(0,1,2)$. Then, $\varpi = 9.023331\ldots$, $$C = C^{\prime} = \frac{1.036282\ldots}{1+\log 2}.$$

-   $M=12$, $(\delta_1,\ldots,\delta_4)=(0,0,1,2)$. Then, $\varpi = 9.363813\ldots$, $$C = C^{\prime} = \frac{1.049651\ldots}{1+\log 2}.$$

-   $M=16$, $(\delta_1,\ldots,\delta_5)=(0,0,1,2,3)$. Then, $\varpi=18.818264\ldots$, $$C = C^{\prime} = \frac{1.062948\ldots}{1+\log 2}.$$

-   $M=37$, $(\delta_1,\ldots,\delta_{10})=(2,3,\ldots,11)$. Then, $\varpi = 103.306060\ldots$, $$C=\frac{1.026022\ldots}{1+\log 2}, \quad C^{\prime}= \frac{1.033596\ldots}{1+\log 2}.$$ (The last collection of parameters holds historical significance as it was utilized by Zudilin in [@Zud2001] to prove that at least one of $\zeta(5),\zeta(7),\zeta(9),\zeta(11)$ is irrational.)

**Remark 36**. *If $\delta_1 = 0$, then by (defi_C) and (defi_C\^prime) we have $C=C^{\prime}$.*

*If we replace $(M;\delta_1,\ldots,\delta_J)$ by $$(\widetilde{M};\widetilde{\delta}_1,\widetilde{\delta}_2,\ldots,\widetilde{\delta}_J) = (M-2\delta_1;\delta_1-\delta_1,\delta_2-\delta_1,\ldots,\delta_J-\delta_1),$$ then $\widetilde{\varpi}=\varpi$, and $\widetilde{C}=\widetilde{C^\prime}=C^{\prime} \geqslant C$. Thus, it is always good to take $\delta_1 = 0$.*

After an extensive random search in the range $M \leqslant 600$, $\delta_j \leqslant 200$ $(j=1,2,\ldots,J)$, $J \leqslant 100$, we have found a better $C = C^{\prime}$ to be approximately $1.119/(1+\log 2)$. For an explanation of how to calculate $\varpi$ using a `MATLAB` program, we refer the reader to [@LZ2022 Section 5]. Now, we give the proof of Claim 3.

*Proof of Claim 3.* Take the parameters $M=433$, $J=89$, and $\delta_1,\ldots,\delta_{89}$ in Table 1.

  ------------------- -------------------- ------------------- ------------------- ------------------- ------------------- -------------------
  $\delta_1=0$        $\delta_2=0$         $\delta_3=0$        $\delta_4=0$        $\delta_5=0$        $\delta_6=0$        $\delta_7=0$
  $\delta_8=0$        $\delta_9=0$         $\delta_{10}=0$     $\delta_{11}=0$     $\delta_{12}=0$     $\delta_{13}=0$     $\delta_{14}=0$
  $\delta_{15}=0$     $\delta_{16}=0$      $\delta_{17}=0$     $\delta_{18}=0$     $\delta_{19}=1$     $\delta_{20}=1$     $\delta_{21}=2$
  $\delta_{22}=2$     $\delta_{23}=3$      $\delta_{24}=3$     $\delta_{25}=4$     $\delta_{26}=5$     $\delta_{27}=6$     $\delta_{28}=7$
  $\delta_{29}=8$     $\delta_{30}=9$      $\delta_{31}=10$    $\delta_{32}=11$    $\delta_{33}=12$    $\delta_{34}=13$    $\delta_{35}=14$
  $\delta_{36}=15$    $\delta_{37}=16$     $\delta_{38}=17$    $\delta_{39}=18$    $\delta_{40}=19$    $\delta_{41}=20$    $\delta_{42}=21$
  $\delta_{43}=22$    $\delta_{44}=23$     $\delta_{45}=25$    $\delta_{46}=27$    $\delta_{47}=29$    $\delta_{48}=31$    $\delta_{49}=33$
  $\delta_{50}=35$    $\delta_{51}=37$     $\delta_{52}=39$    $\delta_{53}=41$    $\delta_{54}=43$    $\delta_{55}=45$    $\delta_{56}=47$
  $\delta_{57}=49$    $\delta_{58}=51$     $\delta_{59}=53$    $\delta_{60}=55$    $\delta_{61}=57$    $\delta_{62}=59$    $\delta_{63}=61$
  $\delta_{64}=63$    $\delta_{65}=65$     $\delta_{66}=67$    $\delta_{67}=69$    $\delta_{68}=71$    $\delta_{69}=73$    $\delta_{70}=75$
  $\delta_{71}=77$    $\delta_{72}=79$     $\delta_{73}=81$    $\delta_{74}=83$    $\delta_{75}=85$    $\delta_{76}=87$    $\delta_{77}=89$
  $\delta_{78}=91$    $\delta_{79}=93$     $\delta_{80}=95$    $\delta_{81}=97$    $\delta_{82}=99$    $\delta_{83}=101$   $\delta_{84}=103$
  $\delta_{85}=107$   $\delta_{86}= 111$   $\delta_{87}=115$   $\delta_{88}=119$   $\delta_{89}=123$
  ------------------- -------------------- ------------------- ------------------- ------------------- ------------------- -------------------

  : The choice of $(\delta_1,\ldots,\delta_{89})$

Then, we have $\varpi = 12557.653439\ldots$ and $$C=C^{\prime} = \frac{1.119356\ldots}{1+\log 2}.$$ By Proposition 16 and Proposition 35, we complete the proof of Claim 3. ◻

As a by-product of [@BR2001], Ball and Rivoal proved that $$\dim_{\mathbb{Q}}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta(3),\zeta(5),\ldots,\zeta(169) \right) \geqslant 3.$$ In other words, we have the upper bound $\kappa_3 \leqslant 169$ for the least odd integer $\kappa_3 \geqslant 5$ such that $\dim_{\mathbb{Q}}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta(3),\zeta(5),\ldots,\zeta(\kappa_3) \right) = 3$. Of course, the standard conjecture is $\kappa_3=5$. The upper bound of $\kappa_3$ was improved by Zudilin [@Zud2002] to $145$ and then improved further to $139$ by Fischler and Zudilin [@FZ2010]. Using some complicated parameters, we prove that $\kappa_3 \leqslant 75$.

*A sketch of the proof of Claim 4.* We use the following rational functions: $$\begin{aligned}
    \widetilde{R}_n(t) = &\frac{\prod_{j=1}^{76} ((M-2\delta_j)n)!}{ n!^{2r}} \cdot(2t+Mn)\\
     &\times \frac{(t-rn)_{rn} (t+Mn+1)_{rn}}{\prod_{j=1}^{76}(t+\delta_jn)_{(M - 2\delta_j)n+1}}, \quad n=1,2,3,\ldots,
\end{aligned}$$ where $r = 2444$, $M=444$, and $\delta_1,\ldots,\delta_{76}$ are those in Table 2.

  ----------------- ------------------ ------------------ ------------------ ------------------ ------------------ ------------------- -------------------
  $\delta_1=1$      $\delta_{11}=4$    $\delta_{21}=14$   $\delta_{31}=24$   $\delta_{41}=44$   $\delta_{51}=64$   $\delta_{61}=84$    $\delta_{71}=104$
  $\delta_2=1$      $\delta_{12}=5$    $\delta_{22}=15$   $\delta_{32}=26$   $\delta_{42}=46$   $\delta_{52}=66$   $\delta_{62}=86$    $\delta_{72}=108$
  $\delta_3=1$      $\delta_{13}=6$    $\delta_{23}=16$   $\delta_{33}=28$   $\delta_{43}=48$   $\delta_{53}=68$   $\delta_{63}=88$    $\delta_{73}=112$
  $\delta_4=1$      $\delta_{14}=7$    $\delta_{24}=17$   $\delta_{34}=30$   $\delta_{44}=50$   $\delta_{54}=70$   $\delta_{64}=90$    $\delta_{74}=116$
  $\delta_5=1$      $\delta_{15}=8$    $\delta_{25}=18$   $\delta_{35}=32$   $\delta_{45}=52$   $\delta_{55}=72$   $\delta_{65}=92$    $\delta_{75}=120$
  $\delta_6=2$      $\delta_{16}=9$    $\delta_{26}=19$   $\delta_{36}=34$   $\delta_{46}=54$   $\delta_{56}=74$   $\delta_{66}=94$    $\delta_{76}=124$
  $\delta_7=2$      $\delta_{17}=10$   $\delta_{27}=20$   $\delta_{37}=36$   $\delta_{47}=56$   $\delta_{57}=76$   $\delta_{67}=96$
  $\delta_8=3$      $\delta_{18}=11$   $\delta_{28}=21$   $\delta_{38}=38$   $\delta_{48}=58$   $\delta_{58}=78$   $\delta_{68}=98$
  $\delta_9=3$      $\delta_{19}=12$   $\delta_{29}=22$   $\delta_{39}=40$   $\delta_{49}=60$   $\delta_{59}=80$   $\delta_{69}=100$
  $\delta_{10}=4$   $\delta_{20}=13$   $\delta_{30}=23$   $\delta_{40}=42$   $\delta_{50}=62$   $\delta_{60}=82$   $\delta_{70}=102$
  ----------------- ------------------ ------------------ ------------------ ------------------ ------------------ ------------------- -------------------

  : The choice of $(\delta_1,\ldots,\delta_{76})$

Then $$\widetilde{S}_n := \sum_{\nu=1}^{+\infty} \widetilde{R}_n(\nu) = \widetilde{\rho}_{n,0} + \sum_{3 \leqslant i \leqslant 75 \atop i \text{~odd}} \widetilde{\rho}_{n,i}\zeta(i)$$ is a linear form in $1$, $\zeta(3)$, $\zeta(5)$, $\ldots$, $\zeta(75)$ with rational coefficients. For any $n>76^2$ we have $$\widetilde{\Phi}_n^{-1} \prod_{j=1}^{76} D_{\max\{ (M-2\delta_1)n,~(M-\delta_j)n \}} \cdot \widetilde{\rho}_{n,0} \in \mathbb{Z}$$ and $$\widetilde{\Phi}_n^{-1}D_{(M-2\delta_1)n}^{76-i} \cdot \widetilde{\rho}_{n,i} \in \mathbb{Z}, \quad i=3,5,\ldots,75,$$ where $$\widetilde{\Phi}_{n} = \prod_{\sqrt{(2r+M)n} < q \leqslant (M-2\delta_1)n \atop q \text{~prime}} q^{\widetilde{\phi}(n/q)},$$ with $\widetilde{\phi}(x) = \min_{0 \leqslant y < 1} \widetilde{\phi}(x,y)$ and $$\begin{aligned}
\widetilde{\phi}(x,y) =& \lfloor  rx+y \rfloor + \lfloor  (r+M)x - y \rfloor - \lfloor  y \rfloor - \lfloor  Mx-y \rfloor -2r\lfloor  x \rfloor \\
&+ \sum_{j=1}^{76} \left( \lfloor  (M-2\delta_j)x \rfloor - \lfloor  y-\delta_j x \rfloor - \lfloor  (M-\delta_j)x - y \rfloor \right).
\end{aligned}$$ Note that not only 'denominator type elementrary bricks' but also 'numerator type elementrary bricks' contribute to $\widetilde{\Phi}_n$.

We have the asymptotic estimates as $n \to +\infty$: $$\begin{aligned}
\widetilde{S}_n &= \exp\left( -\widetilde{\alpha} n + o(n) \right), \\
\widetilde{\Phi}_n &= \exp\left( \widetilde{\varpi}n +o(n) \right),
\end{aligned}$$ where $$\begin{aligned}
    \widetilde{\varpi} &= \int_{0}^{1} \widetilde{\phi}(x)~\mathrm{d}\psi(x) - \int_{0}^{1/(M-2\delta_1)} \widetilde{\phi}(x)~\frac{\mathrm{d}x}{x^2} \\
    &= 42945.452053\ldots,
\end{aligned}$$ $$\begin{aligned}
\widetilde{\alpha} =
&- (2r+M)\log\left( 2r+M + x_0 \right) - r\log(r+x_0) \\
&+ (r+M)\log(r+M+x_0) \\
&- \sum_{j=1}^{76} (M-2\delta_j)\log(M-2\delta_j)  \\
&- \sum_{j=1}^{76} (r+\delta_j)\log(r+\delta_j+x_0) \\
&+ \sum_{j=1}^{76} (r+M-\delta_j)\log(r+M-\delta_j+x_0)  \\
&= 38489.009014\ldots,
\end{aligned}$$ and $x_0 = 0.194387\ldots$ is the unique positive real root of the polynomial $$\begin{aligned}
&~(2r+M+X)(r+X)\prod_{j=1}^{76}(r+\delta_j+X) \\
-&~ X(r+M+X)\prod_{j=1}^{76}(r+M-\delta_j+X).
\end{aligned}$$

On the other hand, we have the bound $$\max_{i=0,3,5,\ldots,75} |\widetilde{\rho}_{n,i}| \leqslant \exp\left( \widetilde{\beta}n + o(n) \right), \quad \text{as~} n \to +\infty,$$ where $$\begin{aligned}
\widetilde{\beta} &= (2r+M)\log\frac{2r+M}{2} - M\log\frac{M}{2} + \log 2 \cdot \sum_{j=1}^{76}(M-2\delta_j) \\
&=58209.043057\ldots
\end{aligned}$$

Applying Theorem 6 to the sequence of linear forms $$\left\{\widetilde{\Phi}_n^{-1} \prod_{j=1}^{76} D_{\max\{ (M-2\delta_1)n,~(M-\delta_j)n \}} \cdot \widetilde{S}_n \right\}_{n > 76^2}$$ with the divisor $d_{n,i} = D_{443n}^3$ of $\widetilde{\Phi}_n^{-1} \prod_{j=1}^{76} D_{\max\{ (M-2\delta_1)n,~(M-\delta_j)n \}} \cdot \widetilde{\rho}_{n,2i+1}$, ($i=1,2,3,\ldots,37$), we obtain that ($\gamma_1=443\times 3$) $$\begin{aligned}
&\dim_{\mathbb{Q}}\operatorname{Span}_{\mathbb{Q}}\left( 1,\zeta(3),\zeta(5),\ldots,\zeta(75) \right) \\
\geqslant & 1 + \frac{\widetilde{\alpha} - \sum_{j=1}^{76}\max\{ M-2\delta_1,~M-\delta_j \} + \widetilde{\varpi} + \gamma_1}{\widetilde{\beta} + \sum_{j=1}^{76}\max\{ M-2\delta_1,~M-\delta_j \} - \widetilde{\varpi}} \\
=& 2.006260\ldots,
\end{aligned}$$ which completes the proof of Claim 4. ◻

**Acknowledgements.** I would like to thank Wadim Zudilin, Johannes Sprang, and Tanguy Rivoal for several helpful comments.

99

R. Apéry, *Irrationalité de $\zeta(2)$ et $\zeta(3)$*, in *Journées Arithmétiques (Luminy, 1978)*, Astérisque, vol. 61 (Société Mathématique de France, Paris, 1979), 11--13.

K. Ball, T. Rivoal, *Irrationalité d'une infinité de valeurs de la fonction zêta aux entiers impairs*, Invent. math. 146, 193--207 (2001).

F. Calegari, Irrationality of certain $p$-adic periods for small $p$, *Int. Math. Res. Not.* (2005), no. 20, 1235--1249.

H. Cohen, *Number Theory, Vol. : Analytic and Modern Tools*, Grad. Texts in Math. 240, Springer, New York, 2007.

S. Fischler, *Linear independence of odd zeta values using Siegel's lemma*, arXiv:2109.10136 \[math.NT\], 2021.

S. Fischler, J. Sprang, and W. Zudilin, *Many odd zeta values are irrational*, Compos. Math. 155(5) (2019), 938--952.

S. Fischler and W. Zudilin, *A refinement of Nesterenko's linear independence criterion with applications to zeta values*, Math. Ann. 347 (2010), no. 4, 739--763.

L. Lai and J. Sprang, *Many $p$-adic zeta values are irrational*, to appear in Michigan Math. J., arXiv:2306.10393 \[math.NT\], 2023.

L. Lai and P. Yu, *A note on the number of irrational odd zeta values*, Compos. Math. 156 (2020), no. 8, 1699--1717.

L. Lai and L. Zhou, *At least two of $\zeta(5),\zeta(7),\ldots,\zeta(35)$ are irrational*, Publ. Math. Debrecen 101/3--4 (2022), 353--372.

Y. V. Nesterenko, *On the linear independence of numbers*, Mosc. Univ. Math. Bull. 40, no. 1, 69--74 (1985) traduction de Vest. Mosk. Univ., Ser. , no. 1, 46--54 (1985).

Y. V. Nesterenko, *On a criterion of linear independence of $p$-adic numbers*, Manuscripta Math. 139 (2012), no. 3--4, 405--414.

A. M. Robert, *A course in p-adic analysis*, Graduate Texts in Mathematics 198, Springer-Verlag, New York, 2000.

T. Rivoal, *La fonction zêta de Riemann prend une infinité de valeurs irrationnelles aux entiers impairs*, C. R. Acad. Sci. Paris Sér. I Math. 331 (2000), no. 4, 267--270.

J. Sprang, *Linear independence result for $p$-adic $L$-values*, Duke Math. J. 169 (2020), no. 18, 3439--3476.

W. Zudilin, *One of the numbers $\zeta(5)$, $\zeta(7)$, $\zeta(9)$, $\zeta(11)$ is irrational*, Uspekhi Mat. Nauk \[Russian Math. Surveys\] 56 (2001), 149--150 \[774--776\].

W. Zudilin, *Irrationality of values of the Riemann zeta function*, Izvestiya Ross. Akad. Nauk Ser. Mat. \[Izv. Math.\] 66 (2002), 49--102 \[489--542\].

W. Zudilin, *Arithmetic of linear forms involving odd zeta values*, J. Théor. Nombres Bordeaux 16(1), 251--291 (2004).

L. L., Beijing International Center for Mathematical Research, Peking University, Beijing, China\
*E--mail address*: `lilaimath@gmail.com`
