---
title: "On the decomposition of motivic multiple zeta values"
authors:
  - "Francis Brown"
arxiv_id: "1102.1310v2"
arxiv_url: "https://arxiv.org/abs/1102.1310"
published: "2011-02-07"
journal_ref: ""
doi: ""
source: "papers/26-brown-2011-decomposition-motivic-mzv/MZVDecomp.tex"
conversion: pandoc-flat
---

# On the decomposition of motivic multiple zeta values

**Francis Brown**

## Abstract

We review motivic aspects of multiple zeta values, and as an application, we give an exact-numerical algorithm to decompose any (motivic) multiple zeta value of given weight into a chosen basis up to that weight.

---
On the decomposition of motivic multiple zeta values

# Introduction

The aim of these notes is to present motivic aspects of multiple zeta values in concrete terms, and give applications which might be of use to physicists. Most introductory texts on multiple zeta values focus exclusively on the relations they satisfy. Here, we take the opposite point of view, and put the emphasis on the coalgebra structure underlying the motivic multiple zeta values. There are two applications:

1.  we show how to use the coalgebra structure to decompose any multiple zeta value numerically into a conjectural basis.

2.  we show how to lift certain identities between multiple zeta values, i.e., real numbers, to their motivic versions.

The first point requires explanation. Since the $\mathbb Q$-vector space of multiple zeta values is finite-dimensional in each weight, standard lattice reduction algorithms give a numerical way to write an arbitrary multiple zeta value of given weight in terms of some chosen spanning set. The point of $(1)$ is that the coalgebra structure enables one to replace this single high-dimensional lattice reduction problem with a sequence of one-dimensional lattice reductions. This is simply the problem of identifying a rational number $\alpha\in \mathbb Q$ which is presented as an element $\alpha \in \mathbb R$ to arbitrarily high accuracy, and can be done using continued fractions. In fact, we expect that there exists a relatively small a priori bound on the denominators of the rational numbers $\alpha$ which can arise, and so this algorithm should be workable in practice.

An application of $(2)$ might be to prove that certain families of relations between multiple zeta values are 'motivic'. The idea behind this was used for the main theorem of [@Br23], where one had to lift a certain relation between actual multiple zeta values to their motivic versions.

The paper is set out as follows. In §2, we review some basic properties of iterated integrals for motivation. In $\S3$ we briefly review the structure of the category of mixed Tate motives over $\mathbb Z$ and state the main properties of motivic multiple zeta values. In $\S4$ we show how to define certain derivation operators $\partial^{\phi}_{2k+1}$, where $k\geq 1$, which act on the space of motivic multiple zeta values. In §5 we describe the decomposition algorithm $(1)$ using these operators, and in §6 we provide a worked example of this algorithm. The reader who is only interested in implementing the algorithm may turn immediately to $\S\S5.1-5.2$, which can be read independently from the rest of the paper.

# Iterated Integrals

We begin with some generalities on iterated integrals, before specializing to the case of iterated integrals on the punctured projective line.

## General iterated integrals.

Let $M$ be a smooth $C^{\infty}$ manifold over $\mathbb R$, and let $k$ be the real or complex numbers. Let $\gamma: [0,1] \rightarrow M$ be a piecewise smooth path on $M$, and let $\omega_1,\ldots, \omega_n$ be smooth $k$-valued 1-forms on $M$. Let us write $$\gamma^*(\omega_i) = f_i(t) dt\ ,$$ for the pull-back of the forms $\omega_i$ to the interval $[0,1$\].

**Definition 1**. Let the iterated integral of $\omega_1,\ldots,\omega_n$ along $\gamma$ be $$\label{defitint} \int_{\gamma} \omega_1\ldots \omega_n = \int_{0\leq t_1\leq \ldots \leq t_n\leq 1} f_1(t_1) dt_1 \ldots f_n(t_n) dt_n\ .$$ More generally, an iterated integral is any $k$-linear combination of such integrals. The empty integral ($n=0$) is defined to be the constant $1$.

The iterated integrals $\int_{\gamma} \omega_1\ldots \omega_n$ do not depend on the choice of parametrization of the path $\gamma$, and satisfy the following basic properties:

*Shuffle product formula*. Given $1$-forms $\omega_1,\ldots, \omega_{r+s}$ one has: $$\int_{\gamma} \omega_1\ldots\omega_r \int_{\gamma} \omega_{r+1}\ldots \omega_{r+s} =\sum_{\sigma \in \Sigma(r,s)}  \int_{\gamma} \omega_{\sigma(1)} \ldots \omega_{\sigma(n)}\ ,$$ where $n=r+s$, and $\Sigma(r,s)$ is the set $(r,s)$-shuffles: $$\Sigma(r,s) = \{\sigma\in \Sigma(n): \sigma(1)<\ldots<\sigma(r) \hbox{ and } \sigma(r+1)<\ldots<\sigma(r+s)\}\ .$$ As a general rule, for any letters $a_1,\ldots, a_{r+s}$, we shall formally write $$\label{shuffdef} a_1\ldots a_r \, \hbox{\rus x} \,a_{r+1}\ldots a_{r+s} = \sum_{\sigma \in \Sigma(r,s)} a_{\sigma(1)} \ldots a_{\sigma(r+s)} \ ,$$ viewed in $\mathbb Z\langle a_1,\ldots, a_{r+s}\rangle$, the free $\mathbb Z$-module spanned by words in the $a$'s.

*Composition of paths*. If $\alpha,\beta:I\rightarrow M$ are two piecewise smooth paths such that $\beta(0)=\alpha(1)$, then let $\alpha\beta$ denote the composed path obtained by traversing first $\alpha$ and then $\beta$. Then $$\int_{\alpha \beta} \omega_1\ldots\omega_n =\sum_{i=0}^n  \int_{\alpha} \omega_1\ldots \omega_i \int_{\beta} \omega_{i+1}\ldots \omega_{n}\ ,$$ where recall that the empty iterated integral ($n=0$) is just the constant $1$.

*Reversal of paths*. If $\gamma^{-1}(t)=\gamma(1-t)$ denotes the reversal of the path $\gamma$, then we have the following reflection formula: $$\int_{\gamma^{-1}} \omega_1\ldots\omega_n = (-1)^n \int_{\gamma} \omega_n\ldots \omega_1\ .$$

*Functoriality*. If $f:M'\rightarrow M$ is a smooth map, and $\gamma:[0,1]\rightarrow M'$ a piecewise smooth path, then we have: $$\int_{\gamma} f^*\omega_1\ldots f^*\omega_n =  \int_{f(\gamma)} \omega_1\ldots \omega_n \ .$$

## The punctured projective line.

Now let us consider the case where $k=\mathbb C$, $S$ is a finite set of points in $\mathbb C$, and $M=\mathbb C\backslash S$. Consider the set of closed one forms $$\label{oneforms} {dz\over z-a_i} \in \Omega^1(M)\ \hbox{ where } a_i \in S \ .$$ Let $a_0,a_{n+1} \in M$ and let $\gamma$ be a path with endpoints $\gamma(0)=a_0, \gamma(1)=a_{n+1}$. Using the notation from [@GG], set: $$\label{Igamma}
I_{\gamma}(a_0;a_1,\ldots, a_n;a_{n+1}) = \int_{\gamma} {dz \over z-a_1} \ldots {dz \over z-a_n}\ .$$ Since the exterior product of any two forms $(\ref{oneforms})$ is zero and each one is closed, one can show that the iterated integrals $(\ref{Igamma})$ only depend on the homotopy class of $\gamma$ relative to its endpoints. When the path $\gamma$ is clear from the context, it can be dropped from the notation.

A variant is to take the limit points $a_0,a_{n+1}$ in the set $S$, in which case only the interior of $\gamma([0,1])$ lies in $M$. When the integral $(\ref{Igamma})$ converges, we can extend the definition to this case and show that the basic properties of §2.1 still hold. Even when it does not converge, $(\ref{Igamma})$ can be defined by a suitable logarithmic regularization procedure (tangential basepoint).

## Multiple zeta values.

From now on, we shall only consider the case where $M = \mathbb C\backslash \{0,1\}$, and thus all $a_i\in \{0,1\}$. There is a canonical path $\gamma: (0,1)\rightarrow M$ where $\gamma(t) =t$, but note that the endpoints of $\gamma$ no longer lie in $M$. Write $$\begin{aligned}
 \label{rhodef} \rho: \mathbb N_+^r  &\longrightarrow& \{0,1\}^\times \\
\rho(n_1,\ldots, n_r) &=& 10^{n_1-1} \ldots 10^{n_r-1} \nonumber
\end{aligned}$$ where $0^k$ denotes a sequence of $k$ zeros, and $\mathbb N_+=\mathbb N\backslash \{0\}$. When $n_r\geq 2$, the following iterated integral and sum converge absolutely, and we have $$\begin{aligned}
  \label{Iconvdef}
  I_{\gamma}(0;\rho(n_1,\ldots, n_r) ;1)   & = &  (-1)^r \sum_{0<k_1<\ldots< k_r} { 1\over k_1^{n_1} \ldots k_r^{n_r}}  \\
& = & (-1)^r \zeta(n_1,\ldots, n_r) \ .   \nonumber
\end{aligned}$$ This is easily verified from a geometric expansion of ${dt\over t-1}$. In this case, the word $\rho(n_1,\ldots, n_r) \in \{0,1\}^\times$ begins in $1$ and ends in $0$, and is called a convergent word in $0,1$ for obvious reasons.

In general, for any sequence $(n_1,\ldots, n_r) \in \mathbb N_+^r$, the quantity $\sum_i n_i$ is called the weight, and $r$ the depth.

## Regularization of MZVs

One can extend the definition of $I_{\gamma}(0;a_1,\ldots, a_n;1)$ with $a_i\in\{0,1\}$ from the set of convergent words to the general case by using the shuffle product formula. We henceforth drop the $\gamma$ from the subscript.

**Lemma 2**. *There is a unique way to define a set of real numbers $I(a_0;a_1,\ldots,a_n;a_{n+1})$ for any $a_i\in \{0,1\}$, such that*

-   *$I(0;a_1,\ldots, a_n;1)$ is given by $(\ref{Iconvdef})$ if $a_1=1$ and $a_n=0$.*

-   *$I(a_0;a_1;a_2)=0$ and $I(a_0;a_1)=1$ for all $a_0,a_1,a_2 \in \{0,1\}$.*

-   *(Shuffle product). For all $n=r+s$ and $a_0,\ldots, a_{n+1} \in \{0,1\}$ $$I (a_0;a_1,\ldots, a_r;a_{n+1}) I(a_0;a_{r+1},\ldots, a_{r+s};a_{n+1})  \quad$$ $$\qquad = \sum_{\sigma \in \Sigma(r,s)} I(a_0;a_{\sigma(1)},\ldots, a_{\sigma(r+s)};a_{n+1})\ .$$*

-   *$I(a_0;a_1,\ldots, a_n;a_{n+1}) =0   \hbox{ if } a_0=a_{n+1}  \hbox{ and } n\geq1$.*

-   *$I(a_0;a_1,\ldots, a_n;a_{n+1}) = (-1)^n I(a_{n+1};a_n,\ldots, a_1;a_0)$.*

-   *$I(a_0;a_1,\ldots, a_n;a_{n+1}) =  I(1-a_{n+1};1-a_n,\ldots, 1-a_1;1-a_0)$.*

The second last equation is simply the reversal of paths formula, the last equation is functoriality with respect to the map $t\mapsto 1-t$. The numbers $\zeta(n_1,\ldots, n_r)$ defined for any $n_i\in \mathbb N_+$ by $(-1)^rI(0;\rho(n_1,\ldots, n_r);1)$ are sometimes called shuffle-regularized multiple zeta values.

## Structure of MZV's in low weights

Let $\mathcal{Z}_N$ denote the $\mathbb Q$-vector space spanned by the set of multiple zeta values $\zeta(n_1,\ldots, n_r)$ with $n_r\geq 2$ of total weight $N=n_1+\ldots+n_r$, and let $\mathcal{Z}$ denote the $\mathbb Q$-algebra spanned by all multiple zeta values over $\mathbb Q$. It is the sum of the vector spaces $\mathcal{Z}_N\subset \mathbb R$, and conjecturally a direct sum. By standard lattice reduction methods, one can try to write down a conjectural basis for $\mathcal{Z}$ for weight $\leq N$. Up to weight 10, one experimentally obtains:

             Weight $N$                   1            2            3             4                 5                 6                  7                      8
  --------------------------------- ------------- ------------ ------------ -------------- -------------------- -------------- ---------------------- ---------------------- --
           $\mathcal{Z}_N$           $\emptyset$   $\zeta(2)$   $\zeta(3)$   $\zeta(2)^2$       $\zeta(5)$       $\zeta(3)^2$        $\zeta(7)$            $\zeta(3,5)$
                                                                                            $\zeta(3)\zeta(2)$   $\zeta(2)^3$    $\zeta(5)\zeta(2)$     $\zeta(3)\zeta(5)$
                                                                                                                                $\zeta(3)\zeta(2)^2$   $\zeta(3)^2\zeta(2)$
                                                                                                                                                           $\zeta(2)^4$
   $\dim_{\mathbb Q}\mathcal{Z}_N$        0            1            1             1                 2                 2                  3                      4

             Weight $N$                        9                         10
  --------------------------------- ----------------------- ----------------------------
           $\mathcal{Z}_N$                $\zeta(9)$                $\zeta(3,7)$
                                         $\zeta(3)^3$            $\zeta(3)\zeta(7)$
                                      $\zeta(7)\zeta(2)$            $\zeta(5)^2$
                                     $\zeta(5) \zeta(2)^2$      $\zeta(3,5)\zeta(2)$
                                     $\zeta(3) \zeta(2)^3$   $\zeta(3)\zeta(5)\zeta(2)$
                                                               $\zeta(3)^2\zeta(2)^2$
                                                                    $\zeta(2)^5$
   $\dim_{\mathbb Q}\mathcal{Z}_N$             5                         7

The dimensions at the bottom are conjectural, and it is not even known whether $\zeta(5)$ and $\zeta(3)\zeta(2)$ are linearly independent over $\mathbb Q$.

For example, the table implies that there exists a relation between the two multiple zeta values $\zeta(3)$ and $\zeta(1,2)$ in weight 3, and indeed it was shown by Euler that $\zeta(3)=\zeta(1,2)$. In weight 8 there appears the first multiple zeta value $\zeta(3,5)$ which conjecturally cannot be expressed as a polynomial in the single zetas $\zeta(n)$ with coefficients in $\mathbb Q$. One expects $$\{\zeta(2), \zeta(3),\zeta(5),\zeta(7),\zeta(3,5),\zeta(9),\zeta(3,7)\}$$ to be algebraically independent over $\mathbb Q$.

# Motivic formalism

In what follows, all vector spaces etc are defined over the field $\mathbb Q$.

## The category of mixed Tate motives over $\mathbb Z$

Let $\mathcal{MT}(\mathbb Z)$ denote the category of mixed Tate motives over $\mathbb Z$ [@DG]. This is a Tannakian category whose simple objects are the Tate motives $\mathbb Q(n)$, indexed by $n\in \mathbb Z$, and which have weight $-2n$. The structure of $\mathcal{MT}(\mathbb Z)$ is determined by the data: $$\label{extdim}
\mathrm{Ext}_{\mathcal{MT}(\mathbb Z)}^1(\mathbb Q(0),\mathbb Q(n)) \cong \left\{
                           \begin{array}{ll}
                             \mathbb Q\  & \hbox{if } n\geq 3 \hbox{ is odd}\ ,  \\
                             0\   & \hbox{otherwise} \ ,
                           \end{array}
                         \right.$$ and the fact that the $\mathrm{Ext}^2$'s vanish. Thus $\mathcal{MT}(\mathbb Z)$ is equivalent to the category of representations of a group scheme $\mathcal{G}_{\mathcal{MT}}$ over $\mathbb Q$, which is a semi-direct product $$\label{Gexact}
 \mathcal{G}_{\mathcal{MT}} \cong \mathcal{G_U} \rtimes \mathbb{G}_m\ ,$$ where $\mathcal{G_U}$ is the prounipotent algebraic group over $\mathbb Q$ whose Lie algebra is the free Lie algebra with one generator $\sigma_{2n+1}$ in degree $-(2n+1)$. The generators correspond to $(\ref{extdim})$, and the freeness follows from the vanishing of the $\mathrm{Ext}^2$'s. The motivic weight is twice the degree.

*Remark 3*. Henceforth we shall use the word weight to refer to *half* the motivic weight, in keeping with the usual terminology for MZVs.

**Definition 4**. Let $\mathcal{A}^{\mathcal{MT}}$ denote the graded ring of affine functions on $\mathcal{G_U}$ over $\mathbb Q$. It is a commutative graded Hopf algebra whose coproduct we denote by $$\Delta: \mathcal{A}^{\mathcal{MT}}\longrightarrow\mathcal{A}^{\mathcal{MT}}\otimes_{\mathbb Q} \mathcal{A}^{\mathcal{MT}}\ .$$ Define a trivial comodule over $\mathcal{A}^{\mathcal{MT}}$ to be: $$\mathcal{H}^{\mathcal{MT}_+}= \mathcal{A}^{\mathcal{MT}}\otimes_{\mathbb Q} \mathbb Q[f_2]\ ,$$ where $f_2$ is defined to be of degree 2. As a graded vector space, $$\mathcal{H}^{\mathcal{MT}_+}\cong \bigoplus_{k\geq 0} \mathcal{A}^{\mathcal{MT}}[2k] \ ,$$ where $[2k]$ denotes a shift in degree of $+2k$. We also write the coaction: $$\Delta: \mathcal{H}^{\mathcal{MT}_+}\longrightarrow\mathcal{A}^{\mathcal{MT}}\otimes_{\mathbb Q} \mathcal{H}^{\mathcal{MT}_+}\ .$$ It is determined by its restriction to $\mathcal{A}^{\mathcal{MT}}$ and the formula $\Delta(f_2) = 1\otimes f_2$.

The structure of $\mathcal{H}^{\mathcal{MT}_+}$ can be described explicitly as follows. It follows from the remarks above that $\mathcal{A}^{\mathcal{MT}}$ is non-canonically isomorphic to the cofree Hopf algebra on cogenerators $f_{2r+1}$ in degree $2r+1\geq 3$: $$\mathcal{U}'=\mathbb Q\langle f_3,f_5,\ldots \rangle\ .$$ This has a basis consisting of all non-commutative words in the $f_{\mathrm{odd}}$'s. The notation $\mathcal{U}'$ is superfluous but useful since we will need to consider many different isomorphisms $\mathcal{A}^{\mathcal{MT}}\cong \mathcal{U}'$. Again, we denote the coproduct on $\mathcal{U}'$ by $\Delta$, which is given by deconcatenation: $$\begin{aligned}
 \Delta:  \mathcal{U}' &\longrightarrow& \mathcal{U}' \otimes_{\mathbb Q} \mathcal{U}' \\
 \Delta(f_{i_1} \ldots f_{i_r}) & = &  1\otimes f_{i_1}\ldots f_{i_r} + f_{i_1}\ldots f_{i_r}\otimes 1 \nonumber   \\
 && \qquad \quad + \quad \sum_{k=1}^{r-1} f_{i_1}\ldots f_{i_k} \otimes f_{i_{k+1}} \ldots f_{i_r} \nonumber

\end{aligned}$$ The multiplication on $\mathcal{U}'$ is given by the shuffle product $(\ref{shuffdef})$.

By analogy with $\mathcal{H}^{\mathcal{MT}_+}$ let us define a trivial comodule $$\mathcal{U}= \mathbb Q\langle f_3,f_5,\ldots   \rangle \otimes_{\mathbb Q} \mathbb Q[f_2]$$ where $f_2$ is of degree $2$ and commutes with the $f_{\mathrm{odd}}$. The coaction $$\Delta: \mathcal{U}\longrightarrow\mathcal{U}' \otimes_\mathbb Q\mathcal{U}$$ satisfies $\Delta(f_2) = 1\otimes f_2$. The total degree gives a grading $\mathcal{U}_k$ on $\mathcal{U}$ which we call the weight (remark 3). Thus we have a non-canonical isomorphism $$\label{firstpsi}
\psi: \mathcal{H}^{\mathcal{MT}_+}\cong \mathcal{U}$$ of graded algebra-comodules, which induces an isomorphism of the underlying graded Hopf algebras $\mathcal{A}^{\mathcal{MT}}$ and $\mathcal{U}'$, and maps $f_2$ to $f_2$.

**Lemma 5**. *Let $d_k=\dim
\mathcal{U}_k=\dim \mathcal{H}^{\mathcal{MT}_+}_k$. Then $$\label{enumeration}
\sum_{k\geq 1} d_k t^k = {1\over  1-t^2-t^3}\ .$$ In particular, $d_0=1, d_1=0, d_2=1$ and $d_k= d_{k-2}+d_{k-3}$ for $k\geq 3$.*

*Proof.* The Poincaré series of $\mathbb Q\langle f_3,f_5, \ldots \rangle$ is given by $${1\over 1-t^3-t^5-\ldots } = {1-t^2 \over 1-t^2-t^3}$$ Multiplying by the Poincaré series ${1\over 1-t^2}$ for $\mathbb Q[f_2]$ gives $(\ref{enumeration})$. ◻

If we define the depth of $f_{2i+1}$ to be 1 for all $i>0$, and the depth of $f_2$ to be 0, then we obtain a grading on $\mathcal{U}$ which simply counts the number of odd elements $f_{2i+1}$. The *motivic depth* is the associated increasing filtration and can be defined in terms of the coaction $\mathcal{H}^{\mathcal{MT}_+}\rightarrow \mathcal{A}^{\mathcal{MT}}\otimes_{\mathbb Q} \mathcal{H}^{\mathcal{MT}_+}$. One checks that the motivic depth filtration induced on $\mathcal{H}^{\mathcal{MT}_+}$ by $(\ref{firstpsi})$ is well-defined, and independent of the choice of $\psi$. In other words, the filtration is motivic, but the grading is not. This stems from the fact that $\sigma_{2i+1}$ is well-defined only up to addition of commutators of $\sigma_j$ for $j< 2i+1$.

**Example 6**. Compare the structure of $\mathcal{H}^{\mathcal{MT}_+}$ in low weights with the table of multiple zeta values given in §2.5:

              Weight $k$                   1          2       3        4         5                      6                       7                         8                                                9                                                10
  ---------------------------------- ------------- ------- ------- --------- ---------- ---------------------------------- ------------ ------------------------------------- ----------------------------------------------------------- --------------------------------------- --
                                      $\emptyset$   $f_2$   $f_3$   $f_2^2$    $f_5$     $f_3\!\, \hbox{\rus x} \,\! f_3$     $f_7$                   $f_5f_3$                                           $f_9$                                           $f_7f_3$
              Basis for                                                       $f_3f_2$               $f_2^3$                 $f_5f_2$     $f_3\!\, \hbox{\rus x} \,\! f_5$     $f_3\!\, \hbox{\rus x} \,\!f_3\!\, \hbox{\rus x} \,\!f_3$        $f_3\, \hbox{\rus x} \,f_7$
   $\mathcal{H}^{\mathcal{MT}_+}_k$                                                                                         $f_3f_2^2$   $f_3\!\, \hbox{\rus x} \,\!f_3 f_2$                           $f_7 f_2$                                $f_5\, \hbox{\rus x} \,f_5$
                                                                                                                                                       $f_2^4$                                        $f_5f_2^2$                                        $f_5f_3f_2$
                                                                                                                                                                                                      $f_3f_2^3$                            $f_3\!\, \hbox{\rus x} \,\!f_5f_2$
                                                                                                                                                                                                                                           $f_3\!\, \hbox{\rus x} \,\! f_3f_2^2$
                                                                                                                                                                                                                                                          $f_2^5$
                $\dim$                     0          1       1        1         2                      2                       3                         4                                                5                                                 7

The following well-known conjecture is of a transcendental nature.

**Conjecture 1**. The $\mathbb Q$-algebra of MZV's is graded by the weight: $$\mathcal{Z} \cong \bigoplus_{k \geq 0} \mathcal{Z}_k$$ and there is an isomorphism of graded algebras: $$\mathcal{Z} \cong \mathcal{H}^{\mathcal{MT}_+}\ .$$

The first part implies that there should be no relations between multiple zeta values of different weights. The second implies in particular that the multiple zeta values should inherit the coaction of the motivic Hopf algebra $\mathcal{A}^{\mathcal{MT}}$. To see what this coaction should be requires introducing motivic multiple zetas, for which the independence in different weights is automatic.

## Motivic multiple zeta values.

In [@GG], Goncharov showed how to lift the ordinary iterated integrals $I(a_0;\ldots;a_{n+1})$, where $a_i \in \overline{\mathbb Q}$ to periods of mixed Tate motives. In the case where the $a_i \in \{0,1\}$, he showed that these motives are unramified over $\mathbb Z$ (see also [@GM]), and therefore define objects in $\mathcal{A}^{\mathcal{MT}}$. In his version of motivic multiple zeta values, the element corresponding to $\zeta(2)$ is zero.

One can show using the formalism of [@DG] that these can in turn be lifted to elements of $\mathcal{H}^{\mathcal{MT}_+}$ in such a way that the motivic version of $\zeta(2)$ is non-zero. However, the tollation involves making some choices (see [@Br23], §2 for the definitions). In summary:

**Theorem 7**. *[]{#propdefI label="propdefI"} There exists a sub-Hopf algebra $\mathcal{A}\subset \mathcal{A}^{\mathcal{MT}}$ and a graded algebra-comodule $\mathcal{H}$ over $\mathcal{A}$, which satisfies the following properties. It is spanned by elements (called motivic iterated integrals) $$\label{Iframed}
I^{\mathfrak{m}}(a_0;a_1,\ldots, a_n;a_{n+1}) \in \mathcal{H}_{n}$$ where $a_0,\ldots, a_{n+1} \in \{0,1\}$, such that:*

*$I^{\mathfrak{m}}(a_0;a_1,\ldots, a_n;a_{n+1}) =0  \hbox{ if } a_0=a_{n+1}  \hbox{ and } n\geq1$*

*$I^{\mathfrak{m}}(a_0;a_1;a_2)=0$ and $I^{\mathfrak{m}}(a_0;a_1) = 1$ for all $a_0,a_1,a_2 \in \{0,1\}$*

*$I^{\mathfrak{m}}(0;a_1,\ldots, a_n;1) = (-1)^n I^{\mathfrak{m}}(1;a_n,\ldots, a_1;0)$*

*$I^{\mathfrak{m}}(0;a_1,\ldots, a_n;1) =   I^{\mathfrak{m}}(0;1-a_n,\ldots, 1-a_1;1)$*

*Furthermore, for any $a_i,x,y \in \{0,1\}$ the shuffle product formula holds: $$I^{\mathfrak{m}}(x;a_1,\ldots, a_r;y) I^{\mathfrak{m}}(x;a_{r+1},\ldots, a_{r+s};y) = \sum_{\sigma \in \Sigma(r,s)} I^{\mathfrak{m}}(x;a_{\sigma(1)},\ldots, a_{\sigma(r+s)};y)\ .$$ There is a well-defined map (the period) $$\begin{aligned}
 \label{periodmap} per: \mathcal{H}&\rightarrow&  \mathbb R\\
 I^{\mathfrak{m}}(a_0;a_1,\ldots, a_n;a_{n+1}) & \longrightarrow& I(a_0;a_1,\ldots,a_n; a_{n+1}) \nonumber

\end{aligned}$$ which is a ring homomorphism. In particular, all relations satisfied by the $I^{\mathfrak{m}}(a_0;a_1,\ldots, a_n;a_{n+1})$ are also satisfied by the $I(a_0;a_1,\ldots, a_n;a_{n+1})$.*

*Finally, there is a non-canonical isomorphism $$\label{Hotens} \mathcal{H}\cong \mathcal{A}\otimes_{\mathbb Q} \mathbb Q[\zeta^{ \mathfrak{m}}(2)] \ ,$$ where $\zeta^{ \mathfrak{m}}(2)$ denotes the motivic iterated integral $-I^{\mathfrak{m}}(0;1,0;1)$. As a consequence, there is a non-canonical embedding of algebra-comodules $$\label{Hoembed}
\mathcal{H}\hookrightarrow \mathcal{H}^{\mathcal{MT}_+}$$ which maps $\zeta^{ \mathfrak{m}}(2)$ to $f_2$.*

**Definition 8**. Let $n_1,\ldots, n_r\in \mathbb N_+$, where $n_r\geq 2$. Define the *motivic multiple zeta value* to be the element in $\mathcal{H}$ given by: $$\zeta^{ \mathfrak{m}}(n_1,\ldots, n_r) = (-1)^n I^{\mathfrak{m}}(0; \rho(n_1,\ldots, n_r) ;1)\ .$$ Its period is $\zeta(n_1,\ldots, n_r)$.

Note that in our setting the element $\zeta^{ \mathfrak{m}}(2)$ is non-zero.

*Remark 9*. The preceding theorem is rather powerful. For instance, it immediately implies that $$\dim_{\mathbb Q} \mathcal{Z}_k \leq \dim_{\mathbb Q} \mathcal{H}_{k} \leq \dim_{\mathbb Q} \mathcal{H}^{\mathcal{MT}_+}_k= d_k$$ where the numbers $d_k$ are defined by $(\ref{enumeration})$. This theorem was first proved independently by Goncharov (see Deligne-Goncharov [@DG]) and Terasoma [@T]. This upper bound on $\dim_{\mathbb Q} \mathcal{H}_{k}$ comes from $(\ref{Hoembed})$. The main result of [@Br23] is the lower bound $\dim_{\mathbb Q} \mathcal{H}_{k}\geq d_k$, which in turn implies that $(\ref{Hoembed})$ is an isomorphism. We shall not need this fact for the sequel.

The various choices made above will be absorbed into a single morphism of graded algebra-comodules $$\label{firstphi}
\phi: \mathcal{H}\longrightarrow\mathcal{U}$$ which is obtained by composing $(\ref{Hoembed})$ with $(\ref{firstpsi})$. It maps $\zeta^{ \mathfrak{m}}(2)$ to $f_2$, and induces a morphism of Hopf algebras $\phi: \mathcal{A}\rightarrow \mathcal{U}'$.

## Notations

The motivic multiple zeta values can exist on three different levels: the highest being the comodule $\mathcal{H}$; next the Hopf algebra $$\mathcal{A}= \mathcal{H}/ \zeta^{ \mathfrak{m}}(2) \mathcal{H}$$ in which $\zeta^{ \mathfrak{m}}(2)$ is killed; and finally the Lie coalgebra $$\label{lodef}
\mathcal{L}= {\mathcal{A}_{>0} \over \mathcal{A}_{>0} \mathcal{A}_{>0}}\ ,$$ of indecomposable elements of $\mathcal{A}$. We use the notation $\zeta^{ \mathfrak{m}}$ to denote an element in $\mathcal{H}$; $\zeta^{ \mathfrak{a}}$ its image in $\mathcal{A}$; and $\zeta^{ \mathfrak{L}}$ its image in $\mathcal{L}$: $$\begin{array}{ccccc}
 \mathcal{H}_{>0}  & \longrightarrow&   \mathcal{A}_{>0} &  \longrightarrow& \mathcal{L}\\
 \begin{sideways}$\in$\end{sideways}&   &   \begin{sideways}$\in$\end{sideways}&   & \begin{sideways}$\in$\end{sideways}\\
 \zeta^{ \mathfrak{m}}(w) & \mapsto  & \zeta^{ \mathfrak{a}}(w)  & \mapsto & \zeta^{ \mathfrak{L}}(w)
\end{array}$$ Thus the elements $\zeta^{ \mathfrak{a}}(n_1,\ldots, n_r)$ are exactly the motivic multiple zeta values considered by Goncharov in [@GG], and $\zeta^{ \mathfrak{a}}(2)=0$. We use the same superscripts for the motivic iterated integrals, viz. $I^{\mathfrak{m}}$, $I^{\mathfrak{a}}$, $I^{\mathfrak{L}}$.

## Formula for the coaction

Goncharov computed the coproduct $\Delta: \mathcal{A}\rightarrow \mathcal{A}\otimes_{\mathbb Q} \mathcal{A}$ on the elements $I^{\mathfrak{a}}(a_0;\ldots; a_{n+1})$ in [@GG], Theorem 1.2. The coaction on $\mathcal{H}$ is given by the same formula, after interchanging the two right-hand factors (see [@Br23], §2).

**Theorem 10**. *The coaction $$\label{Hcoaction}
 \Delta: \mathcal{H}\longrightarrow\mathcal{A}\otimes_{\mathbb Q} \mathcal{H}\ ,$$ can be computed explicitly as follows. For any $a_0,\ldots, a_{n+1}\in \{0,1\}$, the image of a generator $\Delta\,  I^{\mathfrak{m}}(a_0;a_1,\ldots, a_{n};a_{n+1})$ is given by $$\sum_{i_0<i_1<  \ldots<  i_k<i_{k+1}}
 \!\!\! \Big( \prod_{p=0}^k I^{\mathfrak{a}}(a_{i_p}; a_{i_p+1}, .\, .\,,a_{i_{p+1}-1} ;a_{i_{p+1}}) \Big)\otimes I^{\mathfrak{m}}(a_0;a_{i_1},.\, .\,, a_{i_k}; a_{n+1})  \nonumber$$ where the sum is over indices satisfying $i_0=0$ and $i_{k+1}=n+1$, and all $0\leq k\leq n$. Note that the trivial elements $I^{\mathfrak{a}}(a;b)$ are equal to $1$.*

This formula has an elegant interpretation in terms of cutting off segments of a semicircular polygon, for which we refer to [@GG] for further details.

## Zeta cogenerators.

The following lemma ([@GG], Theorem 6.4) is an easy consequence of theorem (propdefI), theorem 10, and the fact that $\zeta(2n+1) \neq 0$.

**Lemma 11**. *For $n\geq 1$, $\zeta^{ \mathfrak{m}}(2n+1)\in \mathcal{H}$ is non-zero and satisfies $$\Delta\, \zeta^{ \mathfrak{m}}(2n+1) = 1 \otimes \zeta^{ \mathfrak{m}}(2n+1) + \zeta^{ \mathfrak{a}}(2n+1) \otimes 1\ .$$ Furthermore, Euler's relation for even zeta values implies that $$\zeta^{ \mathfrak{m}}(2n) = b_n \zeta^{ \mathfrak{m}}(2)^n$$ where $b_n=(-1)^{n+1}{1\over 2} B_{2n} {(24)^n \over (2n)!}$, and the $B_{2n}$ are Bernoulli numbers.*

We can therefore normalize our choice of map $(\ref{firstphi})$ so that $$\mathcal{H}\overset{\phi}{\longrightarrow} \mathcal{U}$$ maps $\zeta^{ \mathfrak{m}}(2n+1)$ to $f_{2n+1}$. For notational convenience we define $$\label{fndef}
f_{2n} = b_n\, f_2^n   \in \mathcal{U}_{2n}$$ where $b_n$ is defined in the previous lemma. We can therefore write: $$\label{phinormed}
\phi(\zeta^{ \mathfrak{m}}(N))=f_N \quad   \hbox{ for all } \quad  N\geq 2 \ .$$

*Remark 12*. If $\xi \in \mathcal{H}$ is of weight $N$ then $\xi'=\xi+\alpha\, \zeta^{ \mathfrak{m}}(N)$, for any $\alpha \in \mathbb Q$, cannot be distinguished from $\xi$ using the coaction $\Delta$. This is the basic reason why our decomposition algorithm ($\S5$) is not exact.

# The derivations $\partial_{2n+1}$

In order to simplify the formula for the coaction $(\ref{Hcoaction})$, it is convenient to consider an infinitesimal version of it. We first consider the comodule $\mathcal{U}$.

## Truncation operators on $\mathcal{U}$

In order to detect elements in $\mathcal{U}$ we can use a set of derivations as follows. For each $n\geq 1$, define truncation maps $$\begin{aligned}
 \label{truncdef}
\partial_{2n+1}: \mathbb Q\langle f_3,f_5,\ldots \rangle  & \rightarrow & \mathbb Q\langle f_3,f_5,\ldots  \rangle \\
 \partial_{2n+1} (f_{i_1}\ldots f_{i_r}) & =  &\left\{
                           \begin{array}{ll}
                             f_{i_2}\ldots f_{i_r} , & \hbox{if } \quad i_1=2n+1\ ,  \nonumber \\
                             0 , & \hbox{otherwise} \ .
                           \end{array}
                         \right.

\end{aligned}$$ It is easy to verify that $\partial_{2n+1}$ is a derivation for the shuffle product, i.e., $$\partial_{2n+1} (a\, \hbox{\rus x} \,b) = \partial_{2n+1}(a) \, \hbox{\rus x} \,b + a \, \hbox{\rus x} \,\partial_{2n+1}(b) \ ,$$ for any $a,b\in \mathbb Q\langle f_3,f_5,\ldots  \rangle$. The map $\partial_{2n+1}$ decreases the motivic depth by 1, and the weight by $2n+1$. If we set $\partial_{2n+1} (f_2)=0$, then the maps $\partial_{2n+1}$ uniquely extend to derivations: $$\partial_{2n+1} : \mathcal{U}\longrightarrow\mathcal{U}\ .$$

**Definition 13**. Let $\partial_{<N}$ be the sum of $\partial_{2i+1}$ for $1<2i+1<N$: $$\label{deltaN} \partial_{<N} : \mathcal{U}_N \longrightarrow\bigoplus_{1\leq i<\lfloor {N\over 2} \rfloor} \mathcal{U}_{N-2i-1}$$

**Lemma 14**. *The following sequence is exact: $$\label{keronedim}   0 \longrightarrow f_N \mathbb Q\longrightarrow\mathcal{U}_N \overset{\partial_{<N}}{\longrightarrow} \bigoplus_{1\leq i< \lfloor {N\over 2} \rfloor} \mathcal{U}_{N-2i-1} \longrightarrow 0$$*

*Proof.* It is clear that every element $F \in \mathcal{U}_N$ can be uniquely written: $$\label{xiexpand}
F= \sum_{1\leq i < \lfloor  {N\over 2} \rfloor} f_{2i+1} v_{N-2i-1} + c f_N$$ where $c\in \mathbb Q$ and the $v_{j} \in \mathcal{U}_{j}$. The elements $v_{N-2i-1}$ are equal to $\partial_{2i+1} F$ by definition. Every tuple $(v_{N-2i-1})_{1\leq i < \lfloor {N\over 2} \rfloor}$ arises in this way. ◻

Thus by repeatedly applying operators $\partial_{2i+1}$ for $2i+1<N$, we can detect elements in $\mathcal{U}_N$, up to elements in the kernel $f_N \mathbb Q$.

## Hopf algebra interpretation

Recalling that $\mathcal{U}'= \mathcal{U}/f_2$, consider the set of indecomposables: $$L = { \mathcal{U}'_{>0} \over \mathcal{U}'_{>0} \mathcal{U}'_{>0}}\ ,$$ which is the cofree Lie coalgebra on cogenerators $f_3,f_5,\ldots$ in all odd degrees $\geq 3$. Its (weight) graded dual $L^\vee$ is the free Lie algebra on dual generators $f^\vee_3,f^\vee_5,\ldots$ in all negative odd degrees $\leq-3$. In each graded weight $N$ there is a perfect pairing $L_N\otimes_{\mathbb Q}L_N^\vee \rightarrow \mathbb Q$ of finite-dimensional vector spaces. Thus every dual generator defines a map $f^{\vee}_{2n+1}: L \rightarrow \mathbb Q$. Let $\pi: \mathcal{U}'_{>0} \rightarrow L$ denote the quotient map, and for $2n+1\leq N$ consider the map $$\label{Hopfdelta}
\mathcal{U}\overset{\Delta'}{\longrightarrow} \mathcal{U}'_{>0} \otimes_{\mathbb Q} \mathcal{U}\overset{\pi \otimes id}{\longrightarrow} L\otimes_{\mathbb Q} \mathcal{U}\overset{f_{2n+1}^{\vee}\otimes id}{\longrightarrow}  \mathcal{U}$$ where $\Delta' = \Delta - 1 \otimes id$. It follows from the structure of $\mathcal{U}$ that this map is precisely $\partial_{2n+1}$ $(\ref{truncdef})$. Note that $(\ref{Hopfdelta})$, restricted to $\mathcal{U}_N$, factors through: $$\label{factoredDelta} \mathcal{U}_N \longrightarrow\mathcal{U}'_{2n+1}\otimes_{\mathbb Q} \mathcal{U}_{N-2n-1} \overset{\pi\otimes id}{\longrightarrow}  L_{2n+1} \otimes_{\mathbb Q} U_{N-2n-1}$$ where the first map is the $(2n+1,N-2n-1)$-graded part of $\Delta$.

## Derivations on $\mathcal{H}$

The previous constructions can be transferred to the Hopf algebra $\mathcal{H}$. First observe that $\mathcal{H}_{\leq N }\subset \mathcal{H}$ and $\mathcal{U}_{\leq N} \subset \mathcal{U}$ are subcoalgebras. Suppose that we have a linear bijection up to weight $N$: $$\label{weightiso}
\phi: \mathcal{H}_{\leq  N}  \overset{\sim}{\longrightarrow} U_{\leq N}$$ which respects the comodule structures, i.e., $\Delta \phi=\phi \Delta$, and also the multiplication laws, i.e., $\phi(x_1 x_2) = \phi(x_1)\phi(x_2)$ for all $x_1,x_2\in \mathcal{H}$ such that $\deg x_1+\deg x_2 \leq N$. Then every element of $\mathcal{H}_{\leq N}$, and in particular every motivic multiple zeta value of weight less than or equal to $N$, can be identified with a non-commutative polynomial in the generators $f_{i}$.[^1]

Transporting via the map $\phi$ leads to derivations $$\partial^{\phi}_{2n+1} =\phi^{-1} \circ  \partial_{2n+1} \circ \phi$$ for all $2n+1\leq N$. These define derivations on the whole of $\mathcal{H}$, but for the purposes of the present paper we shall only need to consider their restriction $\partial^{\phi}_{2n+1}:\mathcal{H}_{\leq N} \rightarrow \mathcal{H}_{\leq N-2n-1}$ . By analogy with $\partial_{<N}$, we define $$\label{deltaphilessNdefn}
\partial^{\phi}_{<N} = \bigoplus_{1\leq i < \lfloor { N \over 2} \rfloor}  \partial^{\phi}_{2i+1} \ .$$ We shall compute the derivations $\partial^{\phi}_{2i+1}$ in the following way. Let $$\pi : \mathcal{A}_{>0} \rightarrow \mathcal{L}$$ denote the quotient map, where $\mathcal{L}$ is the Lie coalgebra of indecomposables $(\ref{lodef})$. We denote the map $\mathcal{L}_{\leq N} \rightarrow L_{\leq N}$ induced by $(\ref{weightiso})$ by $\phi$ also.

**Definition 15**. For all $2n+1\leq N$, define the *coefficient map* to be $$c^{\phi}_{2n+1}=f_{2n+1}^\vee\circ \phi:\mathcal{L}_{2n+1} \longrightarrow\mathbb Q\ .$$

We shall sometimes extend the coefficient map to $\mathcal{A}_{2n+1}$ and $\mathcal{H}_{2n+1}$, and denote it by $c^{\phi}_{2n+1}$ also. For an element $\xi \in \mathcal{H}_{2n+1}$, the number $c^{\phi}_{2n+1}(\xi)$ is simply the coefficient of $f_{2n+1}$ in the expansion $(\ref{xiexpand})$ of $\phi(\xi)$ as a non-commutative polynomial in the $f$'s.

**Definition 16**. For each odd $r\geq 3$, define $$D_r: \mathcal{H}_{N} \overset{\Delta_{r,N-r}}{\longrightarrow} \mathcal{A}_r \otimes_{\mathbb Q} \mathcal{H}_{N-r} \overset{\pi\otimes id}{\longrightarrow} \mathcal{L}_{r}\otimes_{\mathbb Q} \mathcal{H}_{N-r}$$ to be the weight $(r,N-r)$-graded part of the coaction, followed by projection onto the Lie coalgebra. It follows from theorem 10 that the action of $D_r$ on the element $I^{\mathfrak{m}}(a_0;a_1,\ldots, a_n;a_{n+1})$ is given explicitly by: $$\label{mainformula}
 \sum_{p=0}^{n-r} I^{\mathfrak{L}}(a_{p} ;a_{p+1},.\, .\,, a_{p+r}; a_{p+r+1}) \otimes   I^{\mathfrak{m}}(a_{0}; a_1, .\, .\,, a_{p}, a_{p+r+1}, .\, .\,,  a_n ;a_{n+1}) \ .
 \nonumber$$ Note that this formula is closely related to the Connes-Kreimer coproduct formula for a class of linear graphs with two external legs. By analogy, we call the sequence $(a_p;a_{p+1},\ldots, a_{p+r};a_{p+r+1})$ on the left the *subsequence* and the sequence $(a_{0}; a_1, .\, .\,, a_{p}, a_{p+r+1}, .\, .\,,  a_n ;a_{n+1})$ on the right the *quotient sequence* of our original sequence $(a_0;a_1,\ldots, a_n;a_{n+1})$.

It follows from the above that $$\label{explicitphidelta} \partial^{\phi}_{2n+1} =(c^{\phi}_{2n+1} \otimes id)\circ D_{2n+1}\ .$$ Only the coefficient map depends on the choice of $\phi$.

## Normalization of $\phi$ in depth 1

In order to put the operators $\partial^{\phi}_{2n+1}$ to use we first have to choose an isomorphism $\phi$. We shall always assume that $\phi$ is normalized so that $$\phi(\zeta^{ \mathfrak{m}}(2n+1)) = f_{2n+1}$$ for all $2n+1\leq N$. The coefficient $c^{\phi}_{2n+1} \zeta^{ \mathfrak{m}}(2n+1)$ is therefore 1. By the shuffle relations for motivic iterated integrals, one can check that $$\label{Idepth1shuff}
 I^{\mathfrak{m}}(0; \underbrace{0,\ldots, 0}_a, 1, \underbrace{0,\ldots, 0}_{2n-a};1)  = (-1)^{a} \binom{2n}{a} \zeta^{ \mathfrak{m}}(2n+1)\ .$$ Therefore for any normalized $\phi$ we have $$\label{normphiproj}
c^{\phi}_{2n+1}  \, (I^{\mathfrak{L}}(0; \underbrace{0,\ldots, 0}_a, 1, \underbrace{0,\ldots, 0}_{2n-a};1))  = (-1)^{a} \binom{2n}{a}\ .$$ In the later examples, this equation will be used many times.

**Examples 17**. We compute the operators $D_r$ on some examples.

*i).* Consider the element $\zeta^{ \mathfrak{m}}(2,3) =I^{\mathfrak{m}}(0;10100;1) \in \mathcal{H}_5$. We have $${\small D_3 I^{\mathfrak{m}}(0;10100;1) =   I^{\mathfrak{L}}(1;010;0) \otimes I^{\mathfrak{m}}(0;10;1) +I^{\mathfrak{L}}(0;100;1)\otimes  I^{\mathfrak{m}}(0;10;1) }$$ The reflection relation yields $I^{\mathfrak{m}}(1;010;0) = - I^{\mathfrak{m}}(0;010;1)$ which equals $2I^{\mathfrak{m}}(0;100;1)$ by $(\ref{Idepth1shuff})$, so we conclude that $D_3 \zeta^{ \mathfrak{m}}(2,3) = 3\,  \zeta^{ \mathfrak{L}}(3) \otimes \zeta^{ \mathfrak{m}}(2)$. In particular for any normalized $\phi$, we have $\partial^{\phi}_3 \zeta^{ \mathfrak{m}}(2,3) = 3\, \zeta^{ \mathfrak{m}}(2)\ .$ Thus $\phi(\zeta^{ \mathfrak{m}}(2,3))=3 f_3f_2 + cf_5$ where $c\in \mathbb Q$ remains to be determined.

*ii).* Consider $\zeta^{ \mathfrak{m}}(4,3)=I^{\mathfrak{m}}(0;1000100;1) \in \mathcal{H}_7$. From $(\ref{mainformula})$ , $$\begin{aligned}
D_3 I^{\mathfrak{m}}(0;1000100;1) & =  & I^{\mathfrak{L}}(0;100;1) \otimes I^{\mathfrak{m}}(0;1000;1)    \nonumber \\
 & = & \zeta^{ \mathfrak{L}}(3)
 \otimes \zeta^{ \mathfrak{m}}(4) \nonumber \\
D_5 I^{\mathfrak{m}}(0;1000100;1) & = &   I^{\mathfrak{L}}(1;00010;0)  \otimes  I^{\mathfrak{m}}(0;10;1)+   I^{\mathfrak{L}}(0;00100;1)\otimes  I^{\mathfrak{m}}(0;10;1)  \nonumber   \\
 & =  &  10\,  \zeta^{ \mathfrak{L}}(5) \otimes \zeta^{ \mathfrak{m}}(2)    \nonumber

\end{aligned}$$ Thus, for a normalized $\phi$, $\partial^{\phi}_3 \zeta^{ \mathfrak{m}}(4,3) = \zeta^{ \mathfrak{m}}(4)$ and $\partial^{\phi}_5 \zeta^{ \mathfrak{m}}(4,3) =10\,  \zeta^{ \mathfrak{m}}(2)$. Hence $\phi(\zeta^{ \mathfrak{m}}(4,3))= f_3 f_4+ 10 f_5 f_2 + c f_7$, where $c\in \mathbb Q$ is to be calculated.

These examples can be depicted graphically as follows. The derivations above cut off a segment from the marked semi-circles indicated below. Only the segments which give non-zero contributions are indicated.

<figure id="2gen">
<div class="center">
<p><span id="2gen" label="2gen"></span> (-250,-20)<span><span class="math inline"><em>I</em><sup>𝔪</sup>(0;10100;1)</span></span> (-100,-20)<span><span class="math inline"><em>I</em><sup>𝔪</sup>(0;1000100;1)</span></span></p>
</div>
</figure>

It follows from $(\ref{keronedim})$ that the operators $D_{2r+1}$ yield a lot of explicit information about multiple zeta values and their motivic versions.

As a further illustration, consider the family of elements $$\zeta^{ \mathfrak{m}}(1,3,\ldots, 1,3)=I^{\mathfrak{m}}(0;1100\ldots 1100;1)$$ Any subsequence of odd length $2r+1$ of $1100\ldots 1100$ necessarily begins and ends with the same symbol, and so the corresponding motivic iterated integral vanishes, by **I0**. It follows that for any $\phi$, $\partial^{\phi}_{2r+1} \zeta^{ \mathfrak{m}}(3,1,\ldots, 3,1)=0$ for all $r\geq 1$. Therefore by $(\ref{keronedim})$ the element $\zeta^{ \mathfrak{m}}(1,3,\ldots, 1,3)$ is a rational multiple of $\zeta^{ \mathfrak{m}}(N)$, where $N$ is its weight. On taking the period map we deduce that $$\zeta(\underbrace{1,3,\ldots, 1,3}_n) = \alpha_n \pi^{4n}$$ for some $\alpha_n\in \mathbb Q$. David Broadhurst showed that $\alpha_n = {1 \over (2n+1)(4n+1)!}$.

# A decomposition algorithm

By using the comodule structure of $\mathcal{U}$ and the explicit formula for the operators $D_{2r+1}$, one obtains an 'exact-numerical' algorithm for the decomposition of multiple zeta values into any predefined (algebra) basis.

## Preliminary definitions

Suppose that we wish to decompose multiple zeta values up to some weight $M\geq 2$. We need the following set-up.

**1)**. For $2\leq N\leq M$ let $V_N$ be the $\mathbb Q$-vector space spanned by symbols: $$\label{Alzetagen}
 \zeta^{ \mathfrak{m}}(n_1,\ldots, n_r)$$ where $n_i\geq 1$, $n_r \geq 2$, and $n_1+\ldots + n_r = N$. We call $N$ the weight. We also represent these elements another way using a different set of symbols $$\label{AlImotgen} I^{\mathfrak{m}}(a_0;a_1,\ldots, a_N; a_{N+1})\qquad \hbox{where } a_i\in \{0,1\}\ .$$ Any symbol $(\ref{AlImotgen})$ can be reduced to a linear combination of elements of the form $(\ref{Alzetagen})$ using the following relations:

R0

:   For $n_i\geq 1$, $n_r \geq 2$, and $n_1+\ldots + n_r = N$, we set $$I^{\mathfrak{m}}(0;\underbrace{1,0,\ldots, 0}_{n_1},\ldots, \underbrace{1,0,\ldots, 0}_{n_r} ;1)=  (-1)^r\zeta^{ \mathfrak{m}}(n_1,\ldots, n_r)\in V_N$$

R1

:   $I^{\mathfrak{m}}(a_0;a_1,\ldots,a_N; a_{N+1})=0 \hbox{ if } a_0 =a_{N+1}$ or $a_1=\ldots =a_N$ .

R2

:   For $k,  n_1,\ldots, n_r\geq 1$, $$(-1)^k  I^{\mathfrak{m}}(0;\underbrace{0,\ldots,0}_k, \underbrace{1,0,\ldots, 0}_{n_1},\ldots, \underbrace{1,0,\ldots, 0}_{n_r} ;1)=$$ $$\sum_{i_1+ \ldots +i_r=k} \! \binom{n_1+i_1-1}{i_1}\ldots \binom{n_r+i_r-1}{i_r}
     I^{\mathfrak{m}}(0;\underbrace{1,0,\ldots, 0}_{n_1+i_1},\ldots, \underbrace{1,0,\ldots, 0}_{n_r+i_r} ;1)$$

R3

:   $I^{\mathfrak{m}}(0;a_1,\ldots, a_N;1) = (-1)^n I^{\mathfrak{m}}(1;a_N,\ldots, a_1;0)$

R4

:   $I^{\mathfrak{m}}(0;a_1,\ldots, a_N;1) =  I^{\mathfrak{m}}(0;1-a_N,\ldots, 1-a_1;1)$

To see this, take any element of the form $(\ref{AlImotgen})$ and use **R1** and **R3** to ensure that $a_0=0$ and $a_{N+1}=1$. Then use **R2** to rewrite it as a linear combination of elements satisfying $a_1=1$. By **R4** this ensures that $a_N=0$ and finally apply **R2** once more to force $a_1=1$. Conclude using **R0**.

*Remark 18*. Relations **R0** and **R4** actually induce an extra relation (known as duality) on the generators $(\ref{Alzetagen})$. One could take the quotient of $V_N$ modulo this relation if one chooses, but we shall not do this here.

Finally, for any generator of $V_N$, define its period to be the real number $$\label{Alper} per( \zeta^{ \mathfrak{m}}(n_1,\ldots, n_r)  ) =
 \zeta(n_1,\ldots, n_r)\in \mathbb R\ .$$

**2)**. For $2 \leq N\leq M$ define a $\mathbb Q$-vector space $\mathcal{U}_N$ with basis elements $$\label{Alfgen}
 f_{2i_1+1} \ldots f_{2i_r+1} f_2^k$$ where $r,k \geq 0, i_1,\ldots,i_r\geq 1$, and $2(i_1+\ldots+i_r)+r+2k=N$. We also need the multiplication rule $\, \hbox{\rus x} \,: \mathcal{U}_m\times \mathcal{U}_n \rightarrow \mathcal{U}_{m+n}$ defined by $$f_{2i_1+1} \ldots f_{2i_r+1} f_2^k \,\, \hbox{\rus x} \,\, f_{2i_{r+1}+1} \ldots f_{2i_{r+s}+1} f_2^\ell$$ $$\qquad \qquad = \sum_{\sigma \in \Sigma(r,s)}  f_{2i_{\sigma(1)}+1} \ldots f_{2i_{\sigma(r+s)}+1} f_2^{k+\ell}$$ where $\Sigma(r,s)$ is the set of $(r,s)$ shuffles, i.e., permutations $\sigma$ of $1,\ldots, r+s$ such that $\sigma(1)< \ldots < \sigma(r)$ and $\sigma(r+1)< \ldots < \sigma(r+s).$

**3)**. Suppose that we have some conjectural polynomial basis of (motivic) multiple zeta values $B\subset \bigoplus_{2\leq n \leq M} V_n$ up to weight $M$. We shall assume that $B$ contains the elements $$B^0=\{ \zeta^{ \mathfrak{m}}(2)\} \cup \{\zeta^{ \mathfrak{m}}(3),\zeta^{ \mathfrak{m}}(5), \ldots, \zeta^{ \mathfrak{m}}(2r+1) \}$$ where $r$ is the largest integer such that $2r+1\leq M$. Denote the remaining elements of $B$ by $B'=B \backslash B^0,$ and let $B_n$ denote the set of elements of $B$ of weight $n$. For $2\leq N\leq M$, let $\langle B\rangle_N$ denote the $\mathbb Q$-vector space spanned by monomials in elements of the set $B$ which are of total weight $N$, where the weight is additive with respect to multiplication. Part of the decomposition algorithm is to verify that $B$ is indeed a polynomial basis for the (motivic) multiple zeta values. As a first check, one should have $$\label{Bnormassumption}
\dim_{\mathbb Q} \langle B\rangle_N =d_N  \hbox{ for all } 2\leq N\leq M\ ,$$ where $d_0=1, d_1=0, d_2=1$ and $d_k= d_{k-2}+d_{k-3}$ for $k\geq 3$. The integer $d_N$ is the dimension of the vector space $\mathcal{U}_N$.

## Inductive definition of the algorithm

The algorithm is defined by induction on the weight and has two parts:

1.  For all $n\leq N$, we construct a map $$\phi: B_n \rightarrow \mathcal{U}_n\ ,$$ which assigns a $\mathbb Q$-linear combination of monomials of the form $(\ref{Alfgen})$ to every element of our basis $B$ of weight at most $N$. Using the multiplication law $\, \hbox{\rus x} \,$, extend this map multiplicatively to monomials in the elements of $B$ to give a map $$\rho : \langle B\rangle_n \longrightarrow\mathcal{U}_n$$ for all $n\leq N$. We require that $\rho$ be an isomorphism to continue (otherwise, the present choice $B$ is not a basis).

2.  An algorithm to extend $\phi$ to the whole of $V_n$: $$\label{AlphinVndef}
    \phi: V_n \longrightarrow\mathcal{U}_n$$ for all $n\leq N$. Thus there is an *algorithm* to assign a $\mathbb Q$-linear combination of monomials of the form $(\ref{Alfgen})$ to every element $(\ref{Alzetagen})$, but note that it does not actually need to be computed explicitly on all elements of $V_n$, only on the basis elements $B_n$.

Once $(1)$ and $(2$) have been constructed, they give a way to decompose any element $\xi\in V_N$ as a polynomial in our basis: simply compute $$\rho^{-1} (\phi(\xi)) \in \langle B\rangle_N\ .$$ We now show how to define $(1)$ and $(2)$ by a bootstrapping procedure. Suppose that they have been constructed up to and including weight $N$.[^2]

From $(2)$, we have an algorithm to compute a set of coefficient functions $$\label{Alcoeffns}
c^{\phi}_{2r+1} : V_{2r+1} \longrightarrow\mathbb Q$$ for all $2r+1\leq N$, which to any element $\xi\in V_{2r+1}$ takes the coefficient of the monomial $f_{2r+1}$ in $\phi(\xi)\in \mathcal{U}_{2r+1}$. The induction steps are:

**Step 1**. Define $\phi$ on elements $\xi \in B_{N+1}$ as follows. If $\xi =\zeta^{ \mathfrak{m}}(2n+1)$ then set $\phi(\xi)= f_{2n+1}$. Otherwise, write $\xi$ (or $-\xi$) in the form $$\label{Alxiform}
\xi = I^{\mathfrak{m}}(a_0;a_1,\ldots, a_{N+1}; a_{N+2})$$ where $a_i \in \{0,1\}$, using relation **R0**. Define for all $3\leq 2r+1 \leq N$, $$\label{Alxi2r}
 \xi_{2r+1} = \sum_{p=0}^{N+1-2r} c^{\phi}_{2r+1} \big( I^{\mathfrak{m}}( a_p;a_{p+1},\ldots, a_{p+2r+1}; a_{p+2r+2})\big) \times$$ $$\qquad \qquad   \qquad   \qquad  \qquad   \phi( I^{\mathfrak{m}}( a_0;a_{1},\ldots,a_{p},  a_{p+2r+2},\ldots, a_{N+1}; a_{N+2}))$$ Then $\xi_{2r+1} \in \mathcal{U}_{2r+1}$ ($\xi_{2r+1}$ is denoted $\partial_{2r+1} \xi$ in the examples in §6). The right hand side of the product is computed using the algorithm for $\phi$ in strictly lower weights $(\ref{AlphinVndef})$. Finally, define $$\phi(\xi) = \sum_{3\leq 2r+1 \leq N} f_{2r+1} \xi_{2r+1}\ ,$$ where the product on the right is concatenation. Having computed $\phi$ explicitly on the elements of $B_{N+1}$, compute the map $\rho:\langle B\rangle_{N+1} \rightarrow \mathcal{U}_{N+1}$ by extending $\phi$ by multiplicativity, and check that it is an isomorphism. If not, then the choice of $B$ is not a basis. In the case when $B$ contains linear combinations of terms of the form $( \ref{Alxiform})$, $\phi$ is extended by linearity and computed in exactly the same way.

**Step 2**. The algorithm to compute $\phi$ on any generator $\xi \in V_{N+1}$ proceeds as follows. As above, write $\xi$ in the form $(\ref{Alxiform})$, and compute $\xi_{2r+1}$ for $3\leq 2r+1 \leq N$ using the formula $(\ref{Alxi2r})$. As before, let $$u = \sum_{3\leq 2r+1 \leq N} f_{2r+1} \xi_{2r+1}\ .$$ Then $u$ is an element of $\mathcal{U}_{N+1}$, and we can compute $\rho^{-1}( u) \in \langle B\rangle_{N+1}$ as a polynomial in our basis $B$. The general theory tells us that $$Ê\label{cncoeff}
c_{\xi} = {per(\xi - \rho^{-1}( u) ) \over \zeta(N+1)} \in \mathbb R$$ is a rational number. Compute it to as many digits as required in order to identify this rational to a satisfactory degree of certainty. Define $$\phi(\xi) = u + c_{\xi} f_{N+1}\ ,$$ where $f_{2n} = {\zeta(2n)\over \zeta(2)^n} f_2^n$ in the case where $N+1=2n$ is even.

Some worked examples of this algorithm are computed in $\S6$.

## Comments

*i).* In order to decompose an element $\zeta^{ \mathfrak{m}}(n_1,\ldots, n_r)$ of weight $N$ into the basis, one must also decompose all the sub and quotient sequences of $I^{\mathfrak{m}}(0;\rho(n_1,\ldots, n_r);1)$ as they occur in the definition of $D_{2r+1}$. Since such sequences have strictly smaller weight and smaller numbers of $1$'s, the total number of elements to decompose is under control.

*ii).* The computation of the coefficients $(\ref{cncoeff})$ requires an efficient numerical method for computing the multiple zeta values. There are many ways to do this. A simplistic way is to write the path from $0$ to $1$ as the composition of paths from $0$ to ${1\over 2}$ and then from ${1\over 2}$ to $1$, and use the composition of paths formula.

The upshot is that every multiple zeta can be written in terms of multiple polylogarithms evaluated at ${1\over 2}$. Many other methods are also available.

*iii).* This is only an algorithm in the true sense of the word in so far as it is possible to compute the coefficients $c_{\xi}$ $(\ref{cncoeff})$, and this is the only transcendental input. A different realization of the motivic multiple zeta values (say in the $p$-adic setting, or otherwise) might lead to an exact algorithm for the computation of these coefficients too. We hope that one can give a theoretical upper bound for the prime powers which can occur in the denominators $c_{\xi}$ as a function of the weight (and choice of basis).

*iv).* There is in fact no reason to suppose that our basis is an algebra basis, nor that it contains the depth one elements $\zeta^{ \mathfrak{m}}(2n+1)$. For example, in [@Br23] we proved that the Hoffman elements: $$\label{Hoffbasis} \zeta^{ \mathfrak{m}}(n_1,\ldots, n_r)\ ,  \hbox{ where } n_i \in 2, 3$$ are a vector space basis for $\mathcal{H}$. It is obvious that the number of such elements in weight $N$ is given by the integers $d_N$ of $(\ref{enumeration})$. This choice of basis gives a canonical map $$\phi: \mathcal{H}\overset{\sim}{\longrightarrow} \mathcal{U}$$ which respects the coactions, maps $\zeta^{ \mathfrak{m}}(2,\ldots, 2)$ ($n$ two's) to ${(6f_2)^n \over (2n+1)!}$ for all $n\geq 1$, and for all $n=a+b+1$ satisfies $$\begin{aligned}
c^{\phi}_{2n+1} \zeta^{ \mathfrak{m}}(\underbrace{2,\ldots, 2}_a, 3, \underbrace{2,\ldots, 2}_b) & = &2 (-1)^{n} \Big( \binom{2n}{2a+2} - (1-2^{-2n}) \binom{2n}{2b+1}\Big)  \nonumber \\
c^{\phi}_{2n+1} \zeta^{ \mathfrak{m}}(n_1,\ldots, n_r)& = &0 \hbox{ if at least } 2 \,\, n_i\hbox{'s  are equal to } 3 \nonumber
\end{aligned}$$ A slight variant of the previous algorithm allows one to decompose motivic MZV's into this basis also.

*v).* A similar version of this algorithm also works for multiple polylogarithms evaluated at $N^{\mathrm{th}}$ roots of unity, in particular in the case of Euler sums ($N=2$). In some cases an explicit basis for the motivic iterated integrals at roots of unity is known by [@D].

*vi).* Given a relation between motivic multiple zeta values, one can define operators $\partial^{\phi}_{2n+1}$ (for some choice of $\phi$), to obtain more relations of lower weight. Applying the period map gives a relation between real MZVs. Thus a relation between motivic MZVs gives rise to a family of relations between real MZVs.

The converse is also true: the decomposition algorithm allows one to prove an identity between motivic MZVs if one knows sufficiently many relations between real MZVs to determine all the coefficients $(\ref{cncoeff})$ which arise in the algorithm. This was alluded to in point $(2)$ of the introduction. In ([@Br23], §4) this idea was used to lift an identity between real MZV's to the motivic level (it is in fact the definition of the motivic MZV's).

#  Worked example of the decomposition algorithm

We use the following set of motivic multiple zeta values as our independent algebra generators up to weight $10$ (compare the tables in §2.5): $$\label{Appbasis} B=\{\zeta^{ \mathfrak{m}}(2), \zeta^{ \mathfrak{m}}(3) , \zeta^{ \mathfrak{m}}(5), \zeta^{ \mathfrak{m}}(7), \zeta^{ \mathfrak{m}}(3,5), \zeta^{ \mathfrak{m}}(9), \zeta^{ \mathfrak{m}}(3,7)\}\ .$$ We first associate to each element of $B$ an element in $\mathcal{U}$. To economize on notations, we denote $\partial^{\phi_B}_{\cdot}$ by $\partial_{\cdot}$, since there is no confusion.

## Construction of the basis polynomials

The elements $\phi^B(b)\in \mathcal{U}$, for $b\in B$, are defined as follows. Firstly, $$\phi^B(\zeta^{ \mathfrak{m}}(n))= f_n, \hbox{ for } n=2, 3,5,7,9\ ,$$ by $(2)$ of §5. By direct application of definition 16 we have: $$\begin{aligned}
 D_3  \zeta^{ \mathfrak{m}}(3,5)  &=  & I^{\mathfrak{L}}(0;100;1)\otimes I^{\mathfrak{m}}(0;10000;1) + I^{\mathfrak{L}}(1;001;0)\otimes I^{\mathfrak{m}}(0;10000;1)  \nonumber  \\
 D_5  \zeta^{ \mathfrak{m}}(3,5)  &=  & I^{\mathfrak{L}}(1;00100;0)\otimes I^{\mathfrak{m}}(0;100;1) + I^{\mathfrak{L}}(0;10000;1)\otimes I^{\mathfrak{m}}(0;100;1)  \nonumber

\end{aligned}$$ By $(\ref{Idepth1shuff})$, $\partial_3 \, \zeta^{ \mathfrak{m}}(3,5) = 0$, $\partial_5\,  \zeta^{ \mathfrak{m}}(3,5) = -5 \, \zeta^{ \mathfrak{m}}(3)$, and therefore $$\label{App35} \phi^B(\zeta^{ \mathfrak{m}}(3,5)) = -5 f_5 f_3\ ,$$ following the prescription of $(2)$, §5. Similarly, $$\begin{aligned}
 D_3 \zeta^{ \mathfrak{m}}(3,7)  &=  & I^{\mathfrak{L}}(0;100;1)\otimes I^{\mathfrak{m}}(0;1000000;1) + I^{\mathfrak{L}}(1;001;0)\otimes I^{\mathfrak{m}}(0;1000000;1)  \nonumber  \\
 D_5  \zeta^{ \mathfrak{m}}(3,7)  &=  & I^{\mathfrak{L}}(1;00100;0)\otimes I^{\mathfrak{m}}(0;10000;1)   \nonumber   \\
 D_7  \zeta^{ \mathfrak{m}}(3,7)  &=  & I^{\mathfrak{L}}(1;0010000;0)\otimes I^{\mathfrak{m}}(0;100;1)+I^{\mathfrak{L}}(0;1000000;1)\otimes I^{\mathfrak{m}}(0;100;1)   \nonumber

\end{aligned}$$ Thus $\partial_3 \, \zeta^{ \mathfrak{m}}(3,7)= 0$, $\partial_5 \, \zeta^{ \mathfrak{m}}(3,7)=-6 \,\zeta^{ \mathfrak{m}}(5)$, $\partial_7 \, \zeta^{ \mathfrak{m}}(3,7)= -14 \,\zeta^{ \mathfrak{m}}(3)$, *i.e.*, $$\label{App37} \phi^B(\zeta^{ \mathfrak{m}}(3,7)) = -14 f_7f_3 - 6 f_5f_5\ .$$ This computation proves that $B$ is indeed an algebra basis, since the elements in $\phi^B(\langle B\rangle_n)$ for $n\leq 10$ are linearly independent. For example, in weight 10 one checks that we have the following basis for $\mathcal{U}_{10}$: $$f_2^5\ , \ f_3\, \hbox{\rus x} \,f_3f_2^2 \  , \ f_3\, \hbox{\rus x} \,f_5f_2 \ , f_5\, \hbox{\rus x} \,f_5 \ , \ -5 f_5f_3f_2\ , \  f_3 \, \hbox{\rus x} \,f_7 \ ,   -14f_7f_3 -6f_5f_5$$ Therefore any motivic MZV of weight $10$ can be uniquely written $$\begin{aligned}
\xi = a_0 \zeta^{ \mathfrak{m}}(2)^5 +a_1\zeta^{ \mathfrak{m}}(2)^2 \zeta^{ \mathfrak{m}}(3)^2 + a_2 \zeta^{ \mathfrak{m}}(2)\zeta^{ \mathfrak{m}}(3) \zeta^{ \mathfrak{m}}(5) + a_3 \zeta^{ \mathfrak{m}}(5)^2 \nonumber \\
 + a_4 \zeta^{ \mathfrak{m}}(2)\zeta^{ \mathfrak{m}}(3,5) + a_5 \zeta^{ \mathfrak{m}}(3)\zeta^{ \mathfrak{m}}(7) + a_6 \zeta^{ \mathfrak{m}}(3,7)\ , \label{wttenform}

\end{aligned}$$ where $a_0,\ldots, a_6\in \mathbb Q$. From the action of $\partial_{3}, \partial_5, \partial_7$ computed in $(\ref{App35})$, $(\ref{App37})$, we see that the $a_i$ are given by applying the following operators $$\label{Appwt10operators}
a_1 =  {1\over 2}c^2_2\partial_3^2  \ ,\   a_2= c_2\partial_5\partial_3 \ , a_3 = {1\over 2} \partial_5^2 + {6 \over 14} [\partial_7,\partial_3]$$ $$a_4 = {1\over 5} c_2 [\partial_3,\partial_5] \ , \ a_5 = \partial_7\partial_3 \ , \ a_6 = {1\over 14} [\partial_7,\partial_3]$$ to the element $\phi^B(\xi)$, where $c_2^n$ means taking the coefficient of $f_2^n$.

## Sample decompositions

Let us compute $\zeta^{ \mathfrak{m}}(4,3,3)$ as a polynomial in our basis $B$. From the calculations $(4)$ below, we shall see that its non-trivial sub and quotient sequences are $\zeta^{ \mathfrak{m}}(3,4)$, $\zeta^{ \mathfrak{m}}(4,3)$, $\zeta^{ \mathfrak{m}}(2,3)$. Working backwards, we decompose these elements in increasing order of weight.

1.  *Decomposition of $\zeta^{ \mathfrak{m}}(2,3)$*. By example 17, $\partial_3 \zeta^{ \mathfrak{m}}(2,3) = 3\, \zeta^{ \mathfrak{m}}(2)$. In weight five, $\mathcal{U}_5\cong \mathbb Qf_3f_2  \oplus \mathbb Qf_5$, so it follows that $\zeta^{ \mathfrak{m}}(2,3)$ is of the form $c \,\zeta^{ \mathfrak{m}}(5) + 3\, \zeta^{ \mathfrak{m}}(3)\zeta^{ \mathfrak{m}}(2)$, where $c\in \mathbb Q$. By numerical computation, or some other method, we check that: $$c = {\zeta(2,3) - 3\, \zeta(2)\zeta(3) \over \zeta(5) } \sim -{11\over 2}\ .$$ Thus $\zeta^{ \mathfrak{m}}(2,3) =  -{11\over 2} \zeta^{ \mathfrak{m}}(5)+3 \zeta^{ \mathfrak{m}}(3) \zeta^{ \mathfrak{m}}(2).$

2.  *Decomposition of $\zeta^{ \mathfrak{m}}(4,3)$*. By example 17, we have $\partial_3 \zeta^{ \mathfrak{m}}(4,3) =  \zeta^{ \mathfrak{m}}(4) = {2\over 5} \zeta^{ \mathfrak{m}}(2)^2$, and $\partial_5 \zeta^{ \mathfrak{m}}(4,3) = 10 \zeta^{ \mathfrak{m}}(2)$. In weight 7, $$\mathcal{U}_7 \cong \mathbb Qf_3 f^2_2 \oplus f_5f_2 \oplus \mathbb Qf_7$$ so $\phi^B(\zeta^{ \mathfrak{m}}(4,3))$ is of the form $c f_7 + 10 f_5 f_2 + {2\over 5} f_3 f^2_2$. By numerical computation or otherwise, $$c = {\zeta(4,3) - 10\, \zeta(2)\zeta(5) -{2\over 5} \zeta(3) \zeta(2)^2 \over \zeta(7) } \sim -18\ .$$ Thus $\zeta^{ \mathfrak{m}}(4,3) = -18\, \zeta^{ \mathfrak{m}}(7) + 10 \, \zeta^{ \mathfrak{m}}(5) \zeta^{ \mathfrak{m}}(2) + {2\over 5} \,  \zeta^{ \mathfrak{m}}(3) \zeta^{ \mathfrak{m}}(2)^2.$

3.  *Decomposition of $\zeta^{ \mathfrak{m}}(3,4)$*. We omit the computation, which is similar, and merely state that $\zeta^{ \mathfrak{m}}(3,4)  = 17 \zeta^{ \mathfrak{m}}(7) - 10\,\zeta^{ \mathfrak{m}}(5) \zeta^{ \mathfrak{m}}(2).$ (It also follows immediately from $(2)$ and the so-called stuffle relation $\zeta^{ \mathfrak{m}}(3)\zeta^{ \mathfrak{m}}(4)=\zeta^{ \mathfrak{m}}(3,4)+\zeta^{ \mathfrak{m}}(4,3)+\zeta^{ \mathfrak{m}}(7)$.)

4.  *Decomposition of $\zeta^{ \mathfrak{m}}(4,3,3)$*. By $(\ref{mainformula})$ and lemma 7, $$\begin{aligned}
    D_3 \zeta^{ \mathfrak{m}}(4,3,3) & = & (I^{\mathfrak{L}}(0;100;1) + I^{\mathfrak{L}}(1;001;0) + I^{\mathfrak{L}}(0;100;1)) \otimes I^{\mathfrak{m}}(0;1000100;1)  \nonumber \\
      & = & \zeta^{ \mathfrak{L}}(3) \otimes \zeta^{ \mathfrak{m}}(3,4) \ . \nonumber \\
    D_5 \zeta^{ \mathfrak{m}}(4,3,3) & = & I^{\mathfrak{L}}(1;00010;0)\otimes I^{\mathfrak{m}}(0;10100;1)  +I^{\mathfrak{L}}(0;00100;1)\otimes I^{\mathfrak{m}}(0;10100;1)  \nonumber \\
      & = & 10\, \zeta^{ \mathfrak{L}}(5) \otimes \zeta^{ \mathfrak{m}}(3,2) \ . \nonumber \\
    D_7 \zeta^{ \mathfrak{m}}(4,3,3) & = & (I^{\mathfrak{L}}(1;1000100;0)+ I^{\mathfrak{L}}(1;0001001;0) + I^{\mathfrak{L}}(0;0100100;1)) \otimes I^{\mathfrak{m}}(0;100;1)  \nonumber \\
      & = & (\zeta^{ \mathfrak{L}}(4,3) -\zeta^{ \mathfrak{L}}(3,4) - 3(\zeta^{ \mathfrak{L}}(4,3)+\zeta^{ \mathfrak{L}}(3,4)   )\otimes \zeta^{ \mathfrak{m}}(3) \  ,\nonumber \\
      & = & -32 \, \zeta^{ \mathfrak{L}}(7) \otimes \zeta^{ \mathfrak{m}}(3)  \nonumber

    \end{aligned}$$ Thus we have: $$\begin{aligned}
    \phi^B(\partial_3  \zeta^{ \mathfrak{m}}(4,3,3))  = \phi^B( \zeta^{ \mathfrak{m}}(3,4)) & =  &-18 f_7 + 10 f_5f_2  +{2\over 5}f_3f_2^2 \ . \nonumber \\
    \phi^B( \partial_5 \zeta^{ \mathfrak{m}}(4,3,3))  =  10 \,\phi^B(\zeta^{ \mathfrak{m}}(3,2)) &  = & -55 f_5 + 30  f_3 f_2 \ . \nonumber \\
     \phi^B(\partial_7 \zeta^{ \mathfrak{m}}(4,3,3))  =   -32\, \phi^B(\zeta^{ \mathfrak{m}}(3))&  =  & -32 f_3\ . \nonumber

    \end{aligned}$$ Using the equations ($\ref{Appwt10operators})$ we conclude that $$\zeta^{ \mathfrak{m}}(4,3,3) = a_0\,  \zeta^{ \mathfrak{m}}(2)^5 + {1\over 5} \zeta^{ \mathfrak{m}}(2)^2 \zeta^{ \mathfrak{m}}(3)^2 + 10 \, \zeta^{ \mathfrak{m}}(2) \zeta^{ \mathfrak{m}}(3) \zeta^{ \mathfrak{m}}(5) - {49 \over 2} \zeta^{ \mathfrak{m}}(5)^2$$ $$\qquad \qquad - 18 \, \zeta^{ \mathfrak{m}}(3)\zeta^{ \mathfrak{m}}(7) - 4\,  \zeta^{ \mathfrak{m}}(2) \zeta^{ \mathfrak{m}}(3,5)  +\zeta^{ \mathfrak{m}}(3,7)$$ Finally, by numerical computation, one checks once again that $$\zeta(4,3,3)- \Big[{1\over 5} \zeta(2)^2\zeta(3)^2 + \ldots + \zeta(3,7) \Big]   \sim {271 \over 10} \zeta(10) =  {4336 \over 1925}\zeta(2)^5$$

which gives the coefficient $a_0$ of $\zeta^{ \mathfrak{m}}(2)^5$. In this example the coefficients $a_1,a_2,a_4$ of $(\ref{wttenform})$ are computed exactly; the others are obtained indirectly via the period map and numerical approximation.

# Acknowledgements

Very many thanks to Pierre Cartier for a thorough reading of the text and many detailed corrections and comments. This paper was completed during a stay at the Research Institute for Mathematical Sciences, of Kyoto University, and based on a talk given at the conference: "Development of Galois -Teichmüller Theory and Anabelian Geometry" held there. I would like to thank the organisers heartily for their hospitality.

This work was supported by European Research Council grant no. 257638: 'Periods in algebraic geometry and physics'.

99

**F. Brown**: *Mixed Tate motives over $\mathbb Z$*, preprint (2010).

**J. Blümlein, D.J. Broadhurst, J.A.M. Vermaseren**: *The Multiple Zeta Value Data Mine*, Comput. Phys. Commun. 181, 582-625, (2010).

**P. Deligne**: *Le groupe fondamental unipotent motivique de $\mathbb{G}_m - \mu_N$, pour $N=2,3,4,6$ ou $8$*, Publ. Math. Inst. Hautes Études Sci. 101 (2010).

**P. Deligne, A. Goncharov**: *Groupes fondamentaux motiviques de Tate mixte*, Ann. Sci. École Norm. Sup. (4) 38 no. 1 (2005), 1--56.

**A. B. Goncharov**: *Galois symmetries of fundamental groupoids and noncommutative geometry*, Duke Math. J. Volume 128, Number 2 (2005), 209-284.

**A. B. Goncharov, Y. I. Manin**, *Multiple $\zeta$-motives and moduli spaces $\overline{\mathfrak{M}}_{0,n}$*, Compositio Math. 140 (2004), 1-14.

**H. N. Minh, M. Petitot**, *Lyndon words, polylgoarithms and the Riemann $\zeta$-function*, Discrete Maths, vol 217, 273-292 (2000).

**T. Terasoma**, *Mixed Tate motives and multiple zeta values*, Invent. Math. 149, no. 2, 339-369 (2002).

[^1]: We know by [@Br23] that such a $\phi$ exists for all $N$.

[^2]: For the intial case $N=2$, simply set $\phi(\zeta^{ \mathfrak{m}}(2))=f_2$.
