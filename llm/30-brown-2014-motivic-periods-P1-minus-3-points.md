---
title: "Motivic periods and the projective line minus three points"
authors:
  - "Francis Brown"
arxiv_id: "1407.5165v1"
arxiv_url: "https://arxiv.org/abs/1407.5165"
published: "2014-07-19"
journal_ref: ""
doi: ""
source: "papers/30-brown-2014-motivic-periods-P1-minus-3-points/MotivicPeriodsandP1minus3pointsv3.tex"
conversion: pandoc-flat
---

# Motivic periods and the projective line minus three points

**Francis Brown**

## Abstract

This is a review of the theory of the motivic fundamental group of the projective line minus three points, and its relation to multiple zeta values.

---
Primary 11M32; Secondary 14C15.

Belyi's theorem, multiple zeta values, mixed Tate motives, modular forms.

# Introduction

The role of the projective line minus three points $X=\mathbb{P}^1 \backslash \{0,1,\infty\}$ in relation to Galois theory can be traced back to Belyi's theorem [@Belyi] (1979):

**Theorem 1**. *Every smooth projective algebraic curve defined over $\overline{\mathbb{Q}}$ can be realised as a ramified cover of $\mathbb{P}^1$, whose ramification locus is contained in $\{0,1,\infty\}$.*

Belyi deduced that the absolute Galois group of $\mathbb{Q}$ acts faithfully on the profinite completion of the fundamental group of $X$, i.e., the map $$\label{introGQaction}
\mathrm{Gal}(\overline{\mathbb{Q}} /\mathbb{Q}) \rightarrow  \mathrm{Aut}(\widehat{\pi}_1(X(\mathbb{C}), b))$$ where $b \in X(\mathbb{Q})$, is injective. In his famous proposal '*Esquisse d'un programme*' in 1984 [@Esquisse], Grothendieck suggested studying the absolute Galois group of $\mathbb{Q}$ via its action on completions of fundamental groups of moduli spaces of curves $\mathcal{M}_{g,n}$ of genus $g$ with $n$ ordered marked points ($X$ being isomorphic to $\mathcal{M}_{0,4}$) and their interrelations. A few years later, at approximately the same time, these ideas were developed in somewhat different directions in three enormously influential papers due to Drinfeld, Ihara, and Deligne [@Drinfeld; @Ihara; @DeP1]. Ihara's 1990 ICM talk gives a detailed account of the subject at that time [@IharaICM]. However, the problem of determining the image of the map $(\ref{introGQaction})$ remains completely open to this day.

In this talk I will mainly consider the pro-unipotent completion of the fundamental group of $X$, which seems to be a more tractable object than its profinite version, and closely follow the point of view of Deligne, and Ihara (see [@IharaICM], §5).

## Unipotent completion

Deligne showed [@DeP1] that the pro-unipotent completion of $\pi_1(X)$ carries many extra structures corresponding to the realisations of an (at the time) hypothetical category of mixed Tate motives over the integers. Since then, the motivic framework has now been completely established due to the work of a large number of different authors including Beilinson, Bloch, Borel, Levine, Hanamura, and Voevodsky. The definitive reference is [@DG], §§1-2.

1.  There exists an abstract Tannakian category $\mathcal{MT}(\mathbb{Z})$ of mixed Tate motives unramified over $\mathbb{Z}$. It is a $\mathbb{Q}$-linear subcategory of the category $\mathcal{MT}(\mathbb{Q})$ of mixed Tate motives over $\mathbb{Q}$ obtained by restricting certain Ext groups. It is equivalent to the category of representations of an affine group scheme $G^{dR}$ which is defined over $\mathbb{Q}$ and is a semi-direct product $$G^{dR} \cong U^{dR} \rtimes \mathbb{G}_m\ .$$ The subgroup $U^{dR}$ is pro-unipotent, and its graded Lie algebra (for the action of $\mathbb{G}_m$) is isomorphic to the free graded Lie algebra with one generator $$\sigma_3, \sigma_5, \sigma_7, \ldots$$ in every odd negative degree $\leq -3$. The essential reason for this is that the algebraic $K$-theory of the integers $K_{2n-1}(\mathbb{Z})$ has rank 1 for $n =3,5,7,\ldots$, and rank 0 otherwise, as shown by Borel [@Bo1; @Bo2]. Note that the elements $\sigma_{2n+1}$ are only well-defined modulo commutators.

2.  The pro-unipotent completion $\pi^{un}_1(X,\overset{\rightarrow}{1}\!_0, -\overset{\rightarrow}{1}\!_1)$ is the Betti realisation of an object, called the motivic fundamental groupoid (denoted by $\pi_1^{mot}$), whose affine ring is a limit of objects in the category $\mathcal{MT}(\mathbb{Z})$.

The majority of these notes will go into explaining 2 and some of the ideas behind the following motivic analogue of Belyi's injectivity theorem $(\ref{introGQaction})$:

**Theorem 2**. *$G^{dR}$ acts faithfully on the de Rham realisation of $\pi^{mot}_1(X, \overset{\rightarrow}{1}\!_0, -\overset{\rightarrow}{1}\!_1)$.*

This theorem has an $\ell$-adic version which can be translated into classical Galois theory ([@IharaICM], §5.2), and relates to some questions in the literature cited above. Unlike Belyi's theorem, which is geometric, the proof of theorem 2 is arithmetic and combinatorial. The main ideas came from the theory of multiple zeta values.

## Multiple zeta values

Let $n_1,\ldots, n_r$ be integers $\geq 1$ such that $n_r\geq 2$. Multiple zeta values are defined by the convergent nested sums $$\zeta(n_1,\ldots, n_r) = \sum_{1\leq k_1 < \ldots < k_r} {1 \over k_1^{n_1} \ldots k_r^{n_r}}  \quad \in \mathbb{R}\  .$$ The quantity $N=n_1+\ldots+ n_r$ is known as the weight, and $r$ the depth. Multiple zeta values were first studied by Euler (at least in the case $r=2$) and were rediscovered independently in mathematics by Zagier and Ecalle, and in perturbative quantum field theory by Broadhurst and Kreimer. They satisfy a vast array of algebraic relations which are not completely understood at the time of writing.

The relationship between these numbers and the fundamental group comes via the theory of iterated integrals, which are implicit in the work of Picard and were rediscovered by Chen and Dyson. In general, let $M$ be a differentiable manifold and let $\omega_1, \ldots, \omega_n$ be smooth 1-forms on $M$. Consider a smooth path $\gamma: (0,1) \rightarrow M$. The iterated integral of $\omega_1,\ldots, \omega_n$ along $\gamma$ is defined (when it converges) by $$\int_{\gamma} \omega_1 \ldots \omega_n = \int_{0< t_1 < \ldots < t_n < 1} \gamma^*(\omega_1)(t_1) \ldots  \gamma^*(\omega_n)(t_n)\ .$$ Kontsevich observed that when $M=X(\mathbb{C})$ and $\gamma(t)=t$ is simply the inclusion $(0,1) \subset X(\mathbb{R})$, one has the following integral representation $$\label{MZVasitint}
\zeta(n_1,\ldots, n_r) = \int_{\gamma} \omega_1 \underbrace{\omega_0 \ldots \omega_0}_{n_1-1}  \omega_1  \underbrace{\omega_0 \ldots \omega_0}_{n_2-1}   \ldots\omega_1  \underbrace{\omega_0 \ldots \omega_0}_{n_r-1}$$ where $\omega_0 = {dt \over t}$ and $\omega_1 = {dt \over 1-t}$. I will explain in §2.1 that this formula allows one to interpret multiple zeta values as periods of the pro-unipotent fundamental groupoid of $X$. The action of the motivic Galois group $G^{dR}$ on the (de Rham version of) the latter should translate, via Grothendieck's period conjecture, into an action on multiple zeta values themselves. Thus one expects multiple zeta values to be a basic example in a Galois theory of transcendental numbers ([@An], §23.5); the action of the Galois group should preserve all their algebraic relations.

Of course, Grothendieck's period conjecture is not currently known, so there is no well-defined group action on multiple zeta values. This can be circumvented using motivic multiple zeta values. The action of $G^{dR}$ on the de Rham fundamental group of $X$ can then be studied via its action on these objects.

## Motivic periods

Let $T$ be a neutral Tannakian category over $\mathbb{Q}$ with two fiber functors $\omega_B , \omega_{dR} : T \rightarrow \mathrm{Vec}_{\mathbb{Q}}$. Define the ring of motivic periods to be the affine ring of functions on the scheme of tensor isomorphisms from $\omega_{dR}$ to $\omega_B$ $$\mathcal{P}_T^{\mathfrak{m}} = \mathcal{O}( \mathrm{\underline{Isom}}_T(\omega_{dR}, \omega_B)) \ .$$ Every motivic period can be constructed from an object $M \in T$, and a pair of elements $w \in \omega_{dR}(M),  \sigma \in \omega_{B}(M)^{\vee}$. Its matrix coefficient is the function $$\phi \mapsto   \langle \phi(w), \sigma \rangle \quad : \quad  \mathrm{\underline{Isom}}_T(\omega_{dR}, \omega_B)  \rightarrow  \mathbb{A}^1_{\mathbb{Q}}$$ where $\mathbb{A}^1_{\mathbb{Q}}$ is the affine line over $\mathbb{Q}$, and defines an element denoted $[M, w, \sigma]^{\mathfrak{m}} \in \mathcal{P}_T^{\mathfrak{m}}$. It is straightforward to write down linear relations between these symbols as well as a formula for the product of two such symbols. If, furthermore, there is an element $\mathrm{comp}_{B, dR} \in \mathrm{\underline{Isom}}_T(\omega_{dR}, \omega_B)(\mathbb{C})$ we can pair with it to get a map $$\label{permap}
\mathrm{per}: \mathcal{P}_T^{\mathfrak{m}} \longrightarrow \mathbb{C}$$ called the period homomorphism. The ring $\mathcal{P}_T^{\mathfrak{m}}$ admits a left action of the group $G^{dR} = \mathrm{\underline{Isom}}_T(\omega_{dR}, \omega_{dR})$, or equivalently, a left coaction $$\label{Gdrcoact}
\mathcal{P}_T^{\mathfrak{m}} \longrightarrow \mathcal{O}(G^{dR}) \otimes_{\mathbb{Q}} \mathcal{P}_T^{\mathfrak{m}}\ .$$

**Example 3**. *Let $T$ be any category of mixed Tate motives over a number field. It contains the Lefschetz motive $\mathbb{L}=\mathbb{Q}(-1)$, which is the motive $H^1(\mathbb{P}^1\backslash \{0,\infty\})$. Its de Rham cohomology is the $\mathbb{Q}$-vector space spanned by the class $[{dz \over z}]$ and its Betti homology is spanned by a small positive loop $\gamma_0$ around $0$. The Lefschetz motivic period is $$\mathbb{L}^{\mathfrak{m}} =[ \mathbb{L},[ \textstyle {dz \over z}] ,  [\gamma_0]]   \quad \in \quad  \mathcal{P}^{\mathfrak{m}}_T\    .$$ Its period is $\mathrm{per}(\mathbb{L}^{\mathfrak{m}}) = 2 \pi i$. It transforms, under the rational points of the de Rham Galois group of $T$, by $\mathbb{L}^{\mathfrak{m}} \mapsto \lambda \mathbb{L}^{\mathfrak{m}}$, for any $\lambda \in \mathbb{Q}^\times$.*

This construction can be applied to any pair of fiber functors to obtain different notions of motivic periods. Indeed, the elements of $\mathcal{O}(G^{dR})$ can be viewed as 'de Rham' motivic periods, or matrix coefficients of the form $[M, w,v]^{dR}$, where $w\in \omega_{dR}(M)$ and $v\in \omega_{dR}(M)^{\vee}$ (called framings). Whenever the fiber functors carry extra structures (such as 'complex conjugation' on $\omega_B$ or a 'weight' grading on $\omega_{dR}$), then the ring of motivic periods inherits similar structures.

### Motivic MZV's

Let $T= \mathcal{MT}(\mathbb{Z})$. The Betti and de Rham realisations provide functors $\omega_B, \omega_{dR}$, and integration defines a canonical element $\mathrm{comp}_{B,dR} \in \mathrm{\underline{Isom}}_T(\omega_{dR}, \omega_B)(\mathbb{C})$. Since the de Rham functor $\omega_{dR}$ is graded by the weight, the ring of motivic periods $\mathcal{P}^{\mathfrak{m}}_{\mathcal{MT}(\mathbb{Z})}$ is also graded.[^2] It contains graded subrings $$\mathcal{P}^{\mathfrak{m},+}_{\mathcal{MT}(\mathbb{Z}),\mathbb{R}} \  \subset \  \mathcal{P}^{\mathfrak{m},+}_{\mathcal{MT}(\mathbb{Z})} \  \subset  \  \mathcal{P}^{\mathfrak{m}}_{\mathcal{MT}(\mathbb{Z})}$$ of geometric periods (periods of motives whose weights are $\geq 0$), denoted by a superscript $+$, and those which are also invariant under complex conjugation (denoted by a subscript $\mathbb{R}$, since their periods lie in $\mathbb{R}$ as opposed to $\mathbb{C}$).

Next, one has to show that the integral $(\ref{MZVasitint})$ defines a period of an object $M$ in $\mathcal{MT}(\mathbb{Z})$ (this can be done in several ways: [@GM], [@Terasoma], [@DG])). This defines a matrix coefficient $[M, w, \sigma]^{\mathfrak{m}}$, where $w$ encodes the integrand, and $\sigma$ the domain of integration, which we call a motivic multiple zeta value (§2.2) $$\zeta^{\mathfrak{m}}(n_1,\ldots, n_r) \in \mathcal{P}^{\mathfrak{m}}_{\mathcal{MT}(\mathbb{Z})}\ .$$ Its weight is $n_1+\ldots +n_r$ and its period is $(\ref{MZVasitint})$. Most (but not all) of the known algebraic relations between multiple zeta values are also known to hold for their motivic versions. Motivic multiple zeta values generate a graded subalgebra $$\label{Hdef}
 \mathcal{H}\quad  \subset \quad  \mathcal{P}^{\mathfrak{m},+}_{\mathcal{MT}(\mathbb{Z}),\mathbb{R}}\  .$$ The description $\S\ref{sectIntroUnip}$, (1) of $U^{dR}$ enables one to compute the dimensions of the motivic periods of $\mathcal{MT}(\mathbb{Z})$ in each degree by a simple counting argument: $$\label{dNdef}
\hbox{if} \quad d_N:= \dim_{\mathbb{Q}} \big( \mathcal{P}^{\mathfrak{m},+}_{\mathcal{MT}(\mathbb{Z}),\mathbb{R}}\big)_N   \quad \hbox{ then } \quad \sum_{N\geq 0} d_N  t^N= { 1 \over 1-t^2 -t^3}  \  .$$ This implies a theorem proved independently by Goncharov and Terasoma [@DG],[@Terasoma].

**Theorem 4**. *The $\mathbb{Q}$-vector space spanned by multiple zeta values of weight $N$ has dimension at most $d_N$, where the integers $d_N$ are defined in $(\ref{dNdef})$.*

So far, this does not use the action of the motivic Galois group, only a bound on the size of the motivic periods of $\mathcal{MT}(\mathbb{Z})$. The role of $\mathbb{P}^1\backslash \{0,1,\infty\}$ is that the automorphism group of its fundamental groupoid yields a formula for the coaction $(\ref{Gdrcoact})$ on the motivic multiple zeta values (§2.5). The main theorem uses this coaction in an essential way, and is inspired by a conjecture of M. Hoffman [@Hoff].

**Theorem 5**. *The following set of motivic MZV's are linearly independent: $$\label{HoffmotMZVs}
 \{ \zeta^{\mathfrak{m}}(n_1,\ldots, n_r)  \quad \hbox{ for } \quad  n_i = \{2,3\}\}\ .$$*

From the enumeration $(\ref{dNdef})$ of the dimensions, we deduce that $\mathcal{H}=  \mathcal{P}^{\mathfrak{m},+}_{\mathcal{MT}(\mathbb{Z}),\mathbb{R}}$, and that $(\ref{HoffmotMZVs})$ is a basis for $\mathcal{H}$. From this, one immediately sees that $U^{dR}$ acts faithfully on $\mathcal{H}$, and theorem $\ref{thmfaithfulactionofGdr}$ follows easily. As a bonus we obtain that $U^{dR}$ has canonical generators $\sigma_{2n+1}$ (defined in §3.1), and, furthermore, by applying the period map we obtain the

**Corollary 6**. *Every multiple zeta value of weight $N$ is a $\mathbb{Q}$-linear combination of $\zeta(n_1,\ldots, n_r)$, where $n_i \in \{2,3\}$ and $n_1+\ldots+n_r=N$.*

The point of motivic periods is that they give a mechanism for obtaining information on the action of $G^{dR}$, via the period map, from arithmetic relations between real numbers. For theorem $\ref{thmHoffMZVLi}$, the required arithmetic information comes from a formula for $\zeta(2,\ldots, 2, 3,2, \ldots, 2)$ proved by Zagier [@Zagier] using analytic techniques.

## Transcendence of motivic periods

With hindsight, theorem 5 has less to do with mixed Tate motives, or indeed $\mathbb{P}^1\backslash \{0,1,\infty\}$, than one might think. Define a category $H$ whose objects are given by the following data:

1.  A finite-dimensional $\mathbb{Q}$-vector space $M_B$ equipped with an increasing filtration called the weight, which is denoted by $W$.

2.  A finite-dimensional $\mathbb{Q}$-vector space $M_{dR}$ equipped with an increasing filtration $W$ and a decreasing filtration $F$ (the Hodge filtration).

3.  An isomorphism $\mathrm{comp}_{B,dR} : M_{dR} \otimes \mathbb{C}\overset{\sim}{\rightarrow} M_{B}\otimes \mathbb{C}$ which respects the weight filtrations. The vector space $M_B$, equipped with $W$ and the filtration $F$ on $M_B\otimes \mathbb{C}$ induced by $\mathrm{comp}_{B,dR}$ is a $\mathbb{Q}$-mixed Hodge structure.

The category $H$ is Tannakian ([@DeP1], 1.10), with two fiber functors, so it has a ring of motivic periods $\mathcal{P}_{H}^{\mathfrak{m}}$. Furthermore, the Betti and de Rham realisations define a functor $M  \mapsto     (M_{B}, M_{dR}, \mathrm{comp}_{B,dR}) :\mathcal{MT}(\mathbb{Z}) \rightarrow H$, and hence a homomorphism $$\begin{aligned}
 \label{PeMTZtoH}
  \mathcal{P}_{\mathcal{MT}(\mathbb{Z})}^{\mathfrak{m}}   &  \longrightarrow  \mathcal{P}_{H}^{\mathfrak{m}}\ .
\end{aligned}$$ This map is known to be injective, but we do not need this fact. The main theorem 5 is equivalent to saying that the images $\zeta^H(n_1,\ldots, n_r) \in  \mathcal{P}_{H}^{\mathfrak{m}}$ of $(\ref{HoffmotMZVs})$ for $n_i\in \{2,3\}$ are linearly independent. In this way, we could have dispensed with motives altogether and worked with objects in $\mathcal{P}_{H}^{\mathfrak{m}}$, which are elementary.[^3] This leads to the following philosophy for a theory of transcendence of motivic periods in $H$ (or another suitable category of mixed Hodge structures). It differs from standard approaches which emphasise finding relations between periods [@KoZa].

-   Write down arithmetically interesting elements in, say $\mathcal{P}_{H}^{\mathfrak{m}}$, which come from geometry (i.e., which are periods in the sense of [@KoZa]).

-   Compute the coaction $(\ref{Gdrcoact})$ on these motivic periods, and use it to prove algebraic independence theorems.

Indeed, there is no reason to restrict oneself to mixed Tate objects, as the category $H$ does not rely on any conjectural properties of mixed motives. The role of $\mathbb{P}^1\backslash \{0,1,\infty\}$ was to give an integral representation for the numbers $(\ref{MZVasitint})$ and provide a formula for the coaction.

### Multiple modular values

Therefore, in the final part of this talk I want to propose changing the underlying geometry altogether, and replace a punctured projective line with (an orbifold) $M=\Gamma \backslash \!\!\backslash \mathbb{H}$, where $\mathbb{H}$ is the upper half plane, and $\Gamma \leq \mathrm{SL}_2(\mathbb{Z})$ is a subgroup of finite index. Because of Belyi's theorem 1, every smooth connected projective algebraic curve over a number field is isomorphic to an $\overline{\Gamma \backslash \mathbb{H}}$. Therefore the (pure) motivic periods obtained in this way are extremely rich[^4]. It is reasonable to hope that the action of the Tannaka group on the *mixed* motivic periods of $M$ should be correspondingly rich and should generate a large class of new periods suitable for applications in arithmetic and theoretical physics. Many of these periods can be obtained as regularised iterated integrals on $M=\Gamma \backslash \mathbb{H}$ (building on those considered by Manin in [@Ma1; @Ma2]), and the philosophy of §1.4 concerning their Galois action can be carried out by computing a suitable automorphism group of non-abelian group cocyles. There still remains a considerable amount of work to put this general programme in its proper motivic context and extract all the arithmetic consequences.

## Contents

In §2, I review the motivic fundamental group of $X$ from its Betti and de Rham view points, define motivic multiple zeta values, and derive their Galois action from first principles. The only novelty is a direct derivation of the infinitesimal coaction from Ihara's formula. In §3, I state some consequences of theorem 5. In §4 I explain some results of Deligne concerning the motivic fundamental group of the projective line minus $N^\mathrm{th}$ roots of unity, and in §5 discuss the depth filtration on motivic multiple zeta values and its conjectural connection with modular forms. In §6 I mention some new results on multiple modular values for $\mathrm{SL}_2(\mathbb{Z})$, which forms a bridge between multiple zeta values and modular forms.

For reasons of space, it was unfortunately not possible to review the large recent body of work relating to associators, double shuffle equations ([@An] §25, [@Fu], [@Racinet]) and applications to knot theory, the Kashiwara-Vergne problem, and related topics such as deformation quantization; let alone the vast range of applications of multiple zeta values to high-energy physics and string theory. Furthermore, there has been recent progress in $p$-adic aspects of multiple zeta values, notably by H. Furusho and G. Yamashita, and work of M. Kim on integral points and the unit equation, which is also beyond the scope of these notes.

Many technical aspects of mixed Tate motives have also been omitted. See [@DG], §1-2 for the definitive reference.

# The motivic fundamental group of $\mathbb{P}^1 \backslash \{0,1,\infty\}$

Let $X= \mathbb{P}^1 \backslash \{0,1,\infty\}$, and for now let $x,y  \in X(\mathbb{C})$. The motivic fundamental groupoid of $X$ (or rather, its Hodge realisation) consists of the following data:

1.  (Betti). A collection of schemes $\pi_1^B(X,x,y)$ which are defined over $\mathbb{Q}$, and which are equipped with the structure of a groupoid: $$\pi_1^B(X,x,y) \times \pi_1^B(X,y,z) \longrightarrow \pi_1^B(X,x,z)$$ for any $x,y,z \in X(\mathbb{C})$. There is a natural homomorphism $$\label{pitop2piB}
     \pi^{top}_1(X,x,y) \longrightarrow \pi_1^B(X,x,y)(\mathbb{Q})$$ where the fundamental groupoid on the left is given by homotopy classes of paths relative to their endpoints. The previous map is Zariski dense.

2.  (de Rham). An affine group scheme[^5] over $\mathbb{Q}$ denoted by $\pi_1^{dR}(X)$.

3.  (Comparison). A canonical isomorphism of schemes over $\mathbb{C}$ $$\label{comparisonIsom3}
    \mathrm{comp}_{B,dR}:  \pi_1^{B}(X,x,y)\times_{\mathbb{Q}} \mathbb{C}\overset{\sim}{\longrightarrow} \pi_1^{dR}(X)\times_{\mathbb{Q}} \mathbb{C}\ .$$

These structures are described below. Deligne has explained ([@DeP1], §15) how to replace ordinary base points with tangential base points in various settings. Denote such a tangent vector by $${\overset{\rightarrow}{v}\!}_x = \hbox{the tangent vector } v \in T_{x}(\mathbb{P}^1(\mathbb{C}))  \hbox{ at the point } x\ .$$ Identifying $T_{x}(\mathbb{P}^1(\mathbb{C}))$ with $\mathbb{C}$, one obtains natural tangent vectors $\overset{\rightarrow}{1}\!_0$ and $-\overset{\rightarrow}{1}\!_1$ at the points $0$ and $1$ respectively, and a canonical path, or 'droit chemin' $$\mathrm{dch}\in   \pi^{top}_1(X,\overset{\rightarrow}{1}\!_0,-\overset{\rightarrow}{1}\!_1)$$ given by the straight line which travels from $0$ to $1$ in $\mathbb{R}$ with unit speed.

The reason for taking the above tangential base points is to ensure that the corresponding motive (theorem 7) has good reduction modulo all primes $p$: in the setting of $\mathbb{P}^1\backslash \{0,1,\infty\}$ there are no ordinary base points with this property.

The following theorem states that the structures $1-3$ are motivic.

**Theorem 7**. *There is an ind-object (direct limit of objects) $$\label{pi1motivic}
\mathcal{O}( \pi_1^{mot} ( X, \overset{\rightarrow}{1}\!_0, -\overset{\rightarrow}{1}\!_1 )) \in \mathrm{Ind}\,  (\mathcal{MT}(\mathbb{Z}))$$ whose Betti and de Rham realisations are the affine rings $\mathcal{O}(\pi_1^B(X,\overset{\rightarrow}{1}\!_0, -\overset{\rightarrow}{1}\!_1))$, and $\mathcal{O}(\pi_1^{dR}(X))$, respectively.*

*Proof.* (Sketch) The essential idea is due to Beilinson ([@GoMTM], theorem 4.1) and Wojtkowiak [@Wo]. Suppose, for simplicity, that $M$ is a connected manifold and $x,y \in M$ are distinct points. Consider the submanifolds in $M\times \ldots \times M$ ($n$ factors): $$N_i = M^{i-1} \times \Delta \times M^{n-i-1}  \qquad \hbox{ for } i=1, \ldots, n-1$$ where $\Delta$ is the diagonal $M \subset M\times M$. Set $N_0 = \{x\} \times M^{n-1}$ and $N_{n} =  M^{n-1} \times \{y\}$, and let $N\subset M^n$ be the union of the $N_i$, for $i=0,\ldots, n$. Then $$\label{HkMnN}
 H_k (M^{n}, N) = \begin{cases} \mathbb{Q}[ \pi_1^{top}(M,x,y)] / I^{n+1} \quad   \hbox{ if } k = n  \\  0 \qquad  \qquad \qquad \qquad \qquad \hbox{ if } k< n \end{cases}$$ where the first line is the $n^\mathrm{th}$ unipotent truncation of the fundamental torsor of paths from $x$ to $y$ ($I$ is the image of the augmentation ideal in $\mathbb{Q}[ \pi_1^{top}(M,x)]$; see below). In the case when $M=\mathbb{P}^1 \backslash \{0,1,\infty\}$, the left-hand side of $(\ref{HkMnN})$ defines a mixed Tate motive. The case when $x=y$, or when $x$ or $y$ are tangential base points, is more delicate [@DG], §3. ◻

The Betti and de Rham realisations can be described concretely as follows.

1.  (Betti). The Betti fundamental groupoid is defined to be the pro-unipotent completion of the ordinary topological fundamental groupoid. For simplicity, take $x=y \in X(\mathbb{C})$. Then there is an exact sequence $$0 \longrightarrow I \longrightarrow \mathbb{Q}[\pi_1^{top}(X(\mathbb{C}), x) ] \longrightarrow \mathbb{Q}\longrightarrow 0$$ where the third map sends the homotopy class of any path $\gamma$ to $1$ (thus $I$ is the augmentation ideal). Then one has (Malčev, Quillen) $$\mathcal{O}( \pi_1^B(X,x) ) = \lim_{N \rightarrow \infty} \Big( \mathbb{Q}[ \pi_1^{top}(X,x)] / I^{N+1}\Big)^{\vee}$$ The case when $x\neq y$ is defined in a similar way, since $\mathbb{Q}[\pi_1^{top}(X(\mathbb{C}), x,y) ]$ is a rank one module over $\mathbb{Q}[\pi_1^{top}(X(\mathbb{C}), x) ]$.

2.  (de Rham). When $X = \mathbb{P}^1\backslash \{0,1,\infty\}$, one verifies that $$\mathcal{O}(\pi_1^{dR}(X)) \cong \bigoplus_{n \geq 0} H^1_{dR}(X)^{\otimes n}$$ which is isomorphic to the tensor coalgebra on the two-dimensional graded $\mathbb{Q}$-vector space $H^1_{dR}(X)\cong \mathbb{Q}(-1) \oplus \mathbb{Q}(-1)$. We can take as basis the elements $$[\omega_{i_1} | \ldots | \omega_{i_n}]  \quad \hbox{ where } \omega_{i_k} \in  \textstyle{\{ {dt \over t}, {dt \over 1-t}\}}$$ where the bar notation denotes a tensor product $\omega_{i_1}\otimes \ldots \otimes \omega_{i_n}$. It is a Hopf algebra for the shuffle product and deconcatenation coproduct and is graded in degrees $\geq 0$ by the degree which assigns ${dt \over t}$ and ${dt \over 1-t}$ degree $1$.

Denoting $\overset{\rightarrow}{1}\!_0$ and $-\overset{\rightarrow}{1}\!_1$ by $0$ and $1$ respectively, one can write, for $x, y \in \{0,1\}$ $${}_x\Pi^{\bullet}_y = \mathrm{Spec}( \mathcal{O}(\pi_1^{\bullet}(X,x,y))   \qquad \hbox{ where } \quad \bullet \in  \{B, dR, \mathrm{mot}\}\ .$$ It is convenient to write ${}_x\Pi_y$ instead of ${}_x\Pi^{dR}_y$. It does not depend on $x$ or $y$, but admits an action of the motivic Galois group $G^{dR}$ which is sensitive to $x$ and $y$. If $R$ is any commutative unitary $\mathbb{Q}$-algebra, $${}_x\Pi_y (R)  \cong \{ S \in R\langle\langle x_0, x_1 \rangle \rangle^{\times}  : \Delta S= S \otimes S \}$$ is isomorphic to the group of invertible formal power series in two non-commuting variables $x_0, x_1$, which are group-like for the completed coproduct $\Delta$ defined by $\Delta(x_i) = x_i \otimes 1 + 1 \otimes x_i$. The group law is given by concatenation of series.

## Periods

The periods of the motivic fundamental groupoid of $\mathbb{P}^1\backslash \{0,1,\infty\}$ are the coefficients of the comparison isomorphism $\mathrm{comp}_{B,dR}$ $(\ref{comparisonIsom3})$ with respect to the $\mathbb{Q}$-structures on the Betti and de Rham sides. Let $${}_01_1^B \quad   \in \quad  \pi_1^B(X,\overset{\rightarrow}{1}\!_0, -\overset{\rightarrow}{1}\!_1) (\mathbb{Q})   \quad \subset  \quad \mathcal{O}( \pi_1^B(X,{\small \overset{\rightarrow}{1}\!_0 , -\overset{\rightarrow}{1}\!_1}) ) ^{\vee}$$ denote the image of $\mathrm{dch}$ under the natural map $(\ref{pitop2piB})$. It should be viewed as a linear form on the affine ring of the Betti $\pi_1$. For all $\omega_{i_k} \in \{ {dt \over t}, {dt \over 1-t} \}$, $$\label{genitint}
\langle \mathrm{comp}_{B,dR}([\omega_{i_1}| \ldots | \omega_{i_n}]),  {}_01_1^B \rangle = \int_{\mathrm{dch}} \omega_{i_1} \ldots   \omega_{i_n}$$ The right-hand side is the iterated integral from $0$ to $1$, *regularised* with respect to the tangent vectors $1$ and $-1$ respectively, of the one-forms $\omega_{i_k}$. No regularisation is necessary in the case when $\omega_{i_1} = {dt \over 1-t}$ and $\omega_{i_n} = {dt \over t}$, and in this case the right-hand side reduces to the formula $(\ref{MZVasitint})$. In general, one can easily show:

**Lemma 8**. *The integrals $(\ref{genitint})$ are $\mathbb{Z}$-linear combinations of MZV's of weight $n$.*

The *Drinfeld associator* is the de Rham image of $\mathrm{dch}$ $$\mathcal{Z}=  \mathrm{comp}_{B, dR}({}_01_1^B) \in {}_0 \Pi_{1}(\mathbb{C})$$ Explicitly, it is the non-commutative generating series of the integrals $(\ref{genitint})$ $$\begin{aligned}
 \mathcal{Z} &= \sum_{i_k \in \{0,1\} }  x_{i_1} \ldots x_{i_n}   \int_{\mathrm{dch}} \omega_{i_1} \ldots   \omega_{i_n}  \\
 & = 1 + \zeta(2) [x_1, x_0]+ \zeta(3) ([x_0,[x_0,x_1]] + [x_1,[x_1,x_0]]  ) +\cdots
\end{aligned}$$ It is an exponential of a Lie series.

## Motivic multiple zeta values

By the previous paragraph, the affine ring of the de Rham fundamental group is the graded Hopf algebra $$\mathcal{O}({}_x \Pi_y) \cong \mathbb{Q}\langle e_0, e_1 \rangle$$ independently of $x,y \in \{0,1\}$. Its product is the shuffle product, and its coproduct is deconcatenation. Its basis elements can be indexed by words in $\{0,1\}$. By a general fact about shuffle algebras, the antipode is the map $w \mapsto w^*$ where $$(a_1\ldots a_n)^* = (-1)^n a_n \ldots a_1$$ is signed reversal of words. Thus any word $w$ in $\{0,1\}$ defines a de Rham element in $\mathcal{O}({}_x \Pi_y)$. The augmentation map $\mathbb{Q}\langle e_0,e_1\rangle \rightarrow \mathbb{Q}$ corresponds to the unit element in the de Rham fundamental group and defines a linear form ${}_x1^{dR}_y \in  \mathcal{O}({}_x \Pi_y)^{\vee}$.

Define Betti linear forms ${}_x1_y^B \in \mathcal{O}( {}_x \Pi^B_y)^{\vee}$ to be the images of the paths $$\mathrm{dch}\hbox{ if } x=0, y=1 \quad ; \quad
   \mathrm{dch}^{-1}    \hbox{ if }  y=1, x=0  \quad ; \quad
   c_x   \hbox{ if } x=y \ ,$$ where $\mathrm{dch}$ is the straight path from $0$ to $1$, $\mathrm{dch}^{-1}$ is the reversed path from $1$ to $0$, and $c_x$ is the constant (trivial) path based at $x$.

Out of this data we can construct the following motivic periods.

**Definition 9**. Let $x,y\in \{0,1\}$ and let $w$ be any word in $\{0,1\}$. Let $$I^{\mathfrak{m}}(x;w;y)  = [  \mathcal{O}({}_x\Pi_y^{\mathrm{mot}}),  w,  {}_x1_y^B]^{\mathfrak{m}}  \qquad \in \quad \mathcal{P}^{\mathfrak{m},+}_{\mathcal{MT}(\mathbb{Z}), \mathbb{R}}$$

We call the elements $I^{\mathfrak{m}}$ motivic iterated integrals. The 'de Rham' motivic period is the matrix coefficient $[ \mathcal{O}({}_x\Pi_y^{\mathrm{mot}}),  w,  {}_x1_y^{dR}]$ on $\mathcal{MT}(\mathbb{Z})$ with respect to the fiber functors $\omega_{dR}, \omega_{dR}$. It defines a function on $G^{dR}$. Its restriction to the prounipotent group $U^{dR}$ defines an element $I^{\mathfrak{u}}(x;w;y) \in \mathcal{O}(U^{dR})$. The latter are equivalent to objects defined by Goncharov (which he also called motivic iterated integrals).

**Definition 1**. *Define motivic (resp. unipotent) multiple zeta values by $$\zeta^{\bullet} (n_1,\ldots, n_r) = I^{\bullet} (0; 1 0^{n_1-1}  \cdots 1 0^{n_r-1} ; 1) \  ,  \quad \bullet = \mathfrak{m}, \mathfrak{u}\\  \nonumber$$*

It is important to note that $\zeta^{\mathfrak{m}}(2)$ is non-zero, whereas $\zeta^{\mathfrak{u}}(2)=0$.[^6] We immediately deduce from the definitions that $$\begin{aligned}
 \begin{split}  \label{Iwproperties}
(i). & \quad I^{\mathfrak{m}} (x;w;x)   = \delta_{w, \emptyset}  \qquad \hbox{ for } x  \in \{0,1\}   \\
(ii). & \quad I^{\mathfrak{m}} (x;w;y)  = I^{\mathfrak{m}}(y;w^*;x)     \end{split}
\end{aligned}$$ The first property holds because the constant path is trivial, the second follows from the antipode formula and because $\mathrm{dch}\circ \mathrm{dch}^{-1}$, or $\mathrm{dch}^{-1} \circ \mathrm{dch}$, is homotopic to a constant path. Finally, replacing multiple zeta values with their motivic versions, we can define a motivic version of the Drinfeld associator $$\label{motivicDrinfeld}
\mathcal{Z}^{\mathfrak{m}} = \sum_{i_1,\ldots, i_n \in \{0,1\}} x_{i_1}\ldots x_{i_n} I^{\mathfrak{m}}(0; i_1, \ldots,  i_n;1)  \ .$$ It satisfies the associator equations defined by Drinfeld [@Drinfeld], on replacing $2 \pi i$ by $\mathbb{L}^{\mathfrak{m}}$ (using the fact that $\zeta^{\mathfrak{m}}(2) = {-(\mathbb{L}^{\mathfrak{m}})^2 \over 24}$), and the double shuffle equations of [@Racinet].

## Action of the motivic Galois group

The category $\mathcal{MT}(\mathbb{Z})$ is a Tannakian category with respect to the de Rham fiber functor. Therefore the motivic Galois group acts on the affine ring $\mathcal{O}({}_0 \Pi_{1})$ of the de Rham realisation of the motivic fundamental torsor of path $(\ref{pi1motivic})$. A slight generalisation of theorem 7 shows that $G^{dR}$ acts on the de Rham fundamental schemes $${}_x \Pi_y \qquad \hbox{ for all } x, y \in \{0,1\}$$ and furthermore, is compatible with the following structures:

-   (Groupoid structure). The multiplication maps $${}_x \Pi_y \times {}_y \Pi_z \longrightarrow   {}_x \Pi_z$$ for all $x,y,z \in \{0,1\}$.

-   (Inertia). The action of $U^{dR}$ fixes the elements $$\exp(x_0) \hbox{ in } {}_0 \Pi_0(\mathbb{Q}) \qquad \hbox{ and } \qquad  \exp(x_1) \hbox{ in } {}_1 \Pi_1(\mathbb{Q})$$

The groupoid structure is depicted in figure 1.

<figure>
<div class="center">
<p>(-93,-3)<span><span class="math inline">0</span></span> (-66,22)<span><span class="math inline"><sub>0</sub><em>Π</em><sub>1</sub></span></span> (-27,-3)<span><span class="math inline">1</span></span> (-66,-8)<span><span class="math inline"><sub>1</sub><em>Π</em><sub>0</sub></span></span> (-132,7)<span><span class="math inline"><sub>0</sub><em>Π</em><sub>0</sub></span></span> (2,7)<span><span class="math inline"><sub>1</sub><em>Π</em><sub>1</sub></span></span></p>
</div>
<figcaption>The groupoid <span class="math inline"><sub><em>x</em></sub><em>Π</em><sub><em>y</em></sub></span> for <span class="math inline"><em>x</em>, <em>y</em> ∈ {0, 1}</span>. The diagram only represents the groupoid structure; the paths shown do not accurately depict the tangential base points.</figcaption>
</figure>

The local monodromy map $\pi_1^{top}(\mathbb{G}_m, \overset{\rightarrow}{1}\!_0) \rightarrow  \pi_1^{top}(X, \overset{\rightarrow}{1}\!_0)$ (where we write $\mathbb{G}_m$ for $\mathbb{P}^1\backslash \{0,\infty\}$), corresponding to monodromy around $0$, has a motivic analogue which gives rise to the inertial condition. Its de Rham realisation is the map $$\pi_1^{dR}(\mathbb{G}_m, \overset{\rightarrow}{1}\!_0)  \rightarrow   \pi_1^{dR}(X, \overset{\rightarrow}{1}\!_0)=  {}_0 \Pi_{0}$$ and is respected by $G^{dR}$. One shows that $U^{dR}$ acts trivially on $\pi_1^{dR}(\mathbb{G}_m, \overset{\rightarrow}{1}\!_0)$, and furthermore that the element $\exp(x_0) \in {}_0 \Pi_0(\mathbb{Q})$ is in the image of the previous map. This gives the first inertial condition.

**Remark 10**. It is astonishing that one obtains much useful information at all from such symmetry considerations. Nonetheless, it is enough to show the faithfulness of the action of $G^{dR}$ (below). There are further structures respected by $G^{dR}$, such as compatibilities with automorphisms of $\mathbb{P}^1 \backslash \{0,1,\infty\}$. They are not required.

## Ihara action

Let $\mathcal{A}$ denote the group of automorphisms of the groupoid ${}_x \Pi_{y}$ for $x,y\in \{0,1\}$ which respects the structures $1,2$ described in §2.3.

**Proposition 11**. *The scheme ${}_0 \Pi_{1}$ is an $\mathcal{A}$-torsor. In particular, the action of $\mathcal{A}$ on $1 \in {}_0 \Pi_{1}$ defines an isomorphism of schemes $$\label{Auactson1}
a \mapsto a(1) : \mathcal{A}\longrightarrow  {}_0 \Pi_{1}\ .$$ The action of $\mathcal{A}$ on ${}_0 \Pi_{1}$ defines, via this isomorphism, a new group law $$\circ: {}_0 \Pi_{1}\times {}_0 \Pi_{1}\rightarrow {}_0 \Pi_{1}\ .$$ It is given explicitly on formal power series by Ihara's formula $$\begin{aligned}
  \label{Iharaaction}
A(x_0,x_1) \circ G(x_0,x_1) & = G(x_0, A x_1 A^{-1}) A
\end{aligned}$$*

*Proof.* For the basic geometric idea, see [@IharaICM], §2.3. Let $\mathfrak{a}\in \mathcal{A}$, and write $a_{xy}(\xi)$ for the action of $\mathfrak{a}$ on $\xi\in {}_x \Pi_y$. Write $a = a_{01} (1)$. Since ${}_0 \Pi_0$ is a group, $\mathfrak{a}$ acts trivially on its identity element, and so $a_{00}(1)=1$. Via the map ${}_0 \Pi_{1} \times {}_1 \Pi_{0}  \rightarrow {}_0 \Pi_{0}$ we have $a_{01}(1) a_{10}(1) = a_{00}(1)$ and hence $a_{10}(1) = a^{-1}$. The inertial conditions give $$\label{Autinert} a_{00} (\exp(x_0)) = \exp(x_0) \quad \hbox{ and }  \quad a_{11} (\exp(x_1))= \exp(x_1)$$ Now the composition of paths ${}_1 \Pi_{0} \times {}_0 \Pi_{0} \times {}_0 \Pi_{1} \rightarrow {}_1 \Pi_{1}$ gives rise to an equation $1. \exp(x_1). 1 = \exp(x_1)$. Applying $\mathfrak{a}$ to this gives by the second equation in $(\ref{Autinert})$ $$\label{Aooonexpx1}
a_{00}( \exp(x_1)) = a \exp(x_1) a^{-1}  = \exp( a x_1 a^{-1})$$ which completely determines the action of $\mathcal{A}$ on ${}_0 \Pi_0$. Via the map ${}_0 \Pi_{0} \times {}_0 \Pi_{1}  \rightarrow {}_0 \Pi_{1}$ we have the equation $g. 1 = g$, and hence $$\label{a01froma00}
a_{01}(g)  = a_{00}(g) . a \ .$$ Formula $(\ref{Iharaaction})$ follows from $(\ref{Autinert})$, $(\ref{Aooonexpx1})$, $(\ref{a01froma00})$. One easily checks that $a$ uniquely determines $\mathfrak{a}$, and so $(\ref{Auactson1})$ is an isomorphism (see also [@DG], 5.9.) ◻

The groupoid and inertia structures are preserved by $U^{dR}$, giving a morphism $$\label{UtoAu}
 \rho: U^{dR} \longrightarrow \mathcal{A}\overset{(\ref{Auactson1})}{\cong} {}_0 \Pi_{1}$$ such that the following diagram commutes $$\begin{aligned}
  \label{udrcommutativediagram}
 U^{dR}  \times {}_0 \Pi_{1}&    \longrightarrow {}_0 \Pi_{1}\\
  { {}_{\rho\times \mathrm{id}}} \downarrow \qquad   &  \ \quad \quad \downarrow_{\mathrm{id}}  \nonumber \\
  {}_0 \Pi_{1}\times {}_0 \Pi_{1}& \overset{\circ}{\longrightarrow} {}_0 \Pi_{1}\nonumber
\end{aligned}$$

In principle this describes the action of the motivic Galois group on ${}_0 \Pi_{1}$. Note, however, that the map $(\ref{UtoAu})$ is mysterious and very little is known about it.

## Dual formula

The coaction on motivic iterated integrals is dual to Ihara's formula. Dualising $(\ref{udrcommutativediagram})$, we have $$\Delta: \mathcal{O}({}_0 \Pi_{1}) \longrightarrow \mathcal{O}(U^{dR}) \otimes \mathcal{O}({}_0 \Pi_{1})$$ It is equivalent, but more convenient, to consider the infinitesimal coaction $$D \ : \  \mathcal{O}({}_0 \Pi_{1}) \longrightarrow   \mathcal{L}  \otimes \mathcal{O}({}_0 \Pi_{1})   \qquad \big( D(x) = \Delta(x) - 1\otimes x  \mod  \mathcal{O}(U^{dR})_{>0} ^2 \big)$$ where $\mathcal{L} =  \mathcal{O}(U^{dR})_{>0}/\big(\mathcal{O}(U^{dR})_{>0} \big)^2$ is the Lie coalgebra of indecomposables in $\mathcal{O}(U^{dR})$. The following formula is an infinitesimal variant of a formula due to Goncharov [@GG], relating to slightly different objects. In order to fill a gap in the literature, I will sketch how it follows almost immediately from Ihara's formula.

**Proposition 12**. *Let $a_0,\ldots, a_{n+1}\in \{0,1\}$. The coaction $D$ is given by $$\begin{aligned}
\label{mainformula}
 D ( I^{\mathfrak{m}}(a_0;a_1,\ldots, a_n; a_{n+1}) )  = & \sum_{0\leq p<q \leq n} \big[  I^{\mathfrak{u}} (a_{p} ;a_{p+1},\ldots, a_{q}; a_{q+1}) \big] \\
  & \otimes   I^{\mathfrak{m}}(a_{0}; a_1, \ldots, a_{p}, a_{q+1}, \ldots ,  a_n ;a_{n+1}) \nonumber  \ .

\end{aligned}$$ where the square brackets on the left denote the map $[\,\,]: \mathcal{O}(U^{dR})_{>0} \rightarrow \mathcal{L}$.*

*Proof.* Denote the action of $\mathrm{Lie}\, \mathcal{A}$ on $\mathrm{Lie}\, {}_0 \Pi_0$ by $\circ_0$. By $(\ref{Auactson1})$, $\mathrm{Lie}\, \mathcal{A}\cong \mathrm{Lie}\, {}_0 \Pi_{1}$ is the set of primitive elements in its (completed) universal enveloping algebra which we denote simply by $\mathcal{U} ({}_0 \Pi_{1})$. By $(\ref{Autinert})$ and $(\ref{Aooonexpx1})$ we have $a \circ_0 x_0 = 0$ and $a \circ_0 x_1 = a x_1 - x_1 a$. The antipode on $\mathcal{U} ({}_0 \Pi_{1})$ is given by the signed reversal $*$. Since $a \in   \mathcal{U} ({}_0 \Pi_{1})$ is primitive, $a=-a^*$ and also $$a \circ_0 x_0 = 0 \qquad \hbox{ and } \qquad  a \circ_0 x_1 = a x_1  + x_1 a^*\ .$$ This extends to an action on $\mathcal{U} ( {}_0 \Pi_0)$ via $a\circ_0 w_1w_2 = (a \circ_0 w_1)w_2+ w_1(a \circ_0 w_2)$. Now consider the action $a \circ_0 \cdot$ on the following words. All terms are omitted except those terms where $a$ or $a^*$ is inserted in-between the two bold letters: $$\begin{aligned}
a \, \circ_0 \,w_1  \mathbf{ x_0 x_0} w_2  & = \cdots \  + \  0  \ +  \ \cdots \nonumber \\
a \,\circ_0 \,w_1  \mathbf{ x_0 x_1} w_2  & = \cdots \ +\  w_1 \mathbf{ x_0  a x_1 } w_2 \ + \ \cdots \nonumber \\
a\, \circ_0\, w_1  \mathbf{ x_1 x_0} w_2  & = \cdots  \ + \  w_1 \mathbf{ x_1 a^* x_0 } w_2   \ + \ \cdots \nonumber \\
a \,\circ_0\, w_1  \mathbf{ x_1 x_1} w_2  & =  \cdots  \ + \ \underbrace{  w_1 \mathbf{ x_1 a x_1  }  w_2 + w_1 \mathbf{ x_1 a^* x_1  }  w_2 }_{0}  \ + \ \cdots \nonumber
\end{aligned}$$ These four equations are dual to all but the first and last terms in $(\ref{mainformula})$, using the fact that $I^{\mathfrak{u}}(x;w;x)=0$ for $x=0,1$ (first and fourth lines), and the fact that $I^{\mathfrak{u}}(1;w^*;0) = I^{\mathfrak{u}}(0;w;1)$ (third line). A straightforward modification of the above argument taking into account the initial and final terms (using $(\ref{a01froma00})$) shows that the action $\circ_1$ of $\mathrm{Lie}\, \mathcal{A}$ on ${}_0 \Pi_{1}$ is dual to the full expression $(\ref{mainformula})$. ◻

Armed with this formula, we immediately deduce that for all $n\geq 2$, $$\begin{aligned}
 \label{zetamprimitives}
D\,  \zeta^{\mathfrak{m}}(n) & =   [\zeta^{\mathfrak{u}}(n)] \otimes 1
\end{aligned}$$ where we recall that $\zeta^{\mathfrak{u}}(2n)=0$. One easily shows that $\zeta^{\mathfrak{u}}(2n+1) \neq 0$ for $n\geq 1$. See also [@HaMa]. Denote the map $w \mapsto [I^{\mathfrak{u}}(0;w;1)]: \mathcal{O}({}_0 \Pi_{1})_{>0} \rightarrow \mathcal{L}$ simply by $\xi \mapsto [\xi^{\mathfrak{u}}]$. From the structure $\S\ref{sectIntroUnip},1$ of $G^{dR}$ we have the following converse to $(\ref{zetamprimitives})$ ([@BMTZ], §3.2).

**Theorem 13**. *An element $\xi \in \mathcal{O}({}_0 \Pi_{1})$ of weight $n \geq 2$ satisfies $D\xi=[\xi^{\mathfrak{u}}]\otimes 1$ if and only if $\xi \in \mathbb{Q}\, \zeta^{\mathfrak{m}}(n)$.*

This theorem, combined with $(\ref{mainformula})$, provides a powerful method for proving identities between motivic multiple zeta values. Applications are given in [@BrDec].

# The main theorem and consequences

Theorem $\ref{thmHoffMZVLi}$ is a result about linear independence. There is an analogous statement for algebraic independence of motivic multiple zeta values.

**Definition 2**. *Let $X$ be an alphabet (a set) and let $X^{\times}$ denote the free associative monoid generated by $X$. Suppose that $X$ has a total ordering $<$, and extend it to $X^{\times}$ lexicographically. An element $w\in X^{\times}$ is said to be a Lyndon word if $$w <u \quad  \hbox{ whenever } \quad  w = u v \quad  \hbox{ and }  \quad u, v \neq \emptyset\ .$$*

For an ordered set $X$, let $\mathrm{Lyn(X)}$ denote the set of Lyndon words in $X$.

**Theorem 14**. *Let $X_{3,2} = \{2,3\}$ with the ordering $3<2$. The set of elements $$\label{zetamHofflyndon} \zeta^{\mathfrak{m}}(w)\quad \hbox{ where } w \in \mathrm{Lyn}(X_{3,2}^{\times})$$ are algebraically independent over $\mathbb{Q}$, and generate the algebra $\mathcal{H}$ of motivic multiple zeta values.*

Theorem $\ref{thmAlgInd}$ implies that every motivic multiple zeta value is equal to a unique polynomial with rational coefficients in the elements $(\ref{zetamHofflyndon})$. It is often convenient to modify this generating family by replacing $\zeta^{\mathfrak{m}}(3,2,\ldots, 2)$ (a three followed by $n-1$ two's) with $\zeta^{\mathfrak{m}}(2n+1)$ (by theorem 18). Taking the period yields the

**Corollary 1**. *Every multiple zeta value is a polynomial, with coefficients in $\mathbb{Q}$, in $$\label{ZHL} \zeta(w)\quad \hbox{ where } w \in \mathrm{Lyn}(X_{3,2}^{\times}) \ .$$*

**Corollary 2**. *The category $\mathcal{MT}(\mathbb{Z})$ is generated by $\pi^{mot}_1(\mathbb{P}^1\backslash \{0,1,\infty\},\overset{\rightarrow}{1}\!_0,-\overset{\rightarrow}{1}\!_1)$ in the following sense. Every mixed Tate motive over $\mathbb{Z}$ is isomorphic, up to a Tate twist, to a direct sum of copies of sub-quotients of $$\mathcal{O}(\pi^{mot}_1(\mathbb{P}^1\backslash \{0,1,\infty\}, \overset{\rightarrow}{1}\!_0, -\overset{\rightarrow}{1}\!_1))\ .$$*

**Corollary 3**. *The periods of mixed Tate motives over $\mathbb{Z}$ are polynomials with rational coefficients of $(2\pi i)^{-1}$ and $(\ref{ZHL})$.*

More precisely [@DLetter], if $M \in \mathcal{MT}(\mathbb{Z})$ has non-negative weights (i.e. $W_{-1}M=0$), then the periods of $M$ are polynomials in $(\ref{ZHL})$ and $2 \pi i$.

## Canonical generators

Recall that the unipotent zeta values $\zeta^{\mathfrak{u}}$ are elements of $\mathcal{O}(U^{dR})$. As a consequence of theorem 14:

**Corollary 4**. *For every $n\geq 1$ there is a canonical element $\sigma_{2n+1}\in \mathrm{Lie} \, U^{dR}(\mathbb{Q})$ which is uniquely defined by $\langle \exp(\sigma_{2n+1}), \zeta^{\mathfrak{u}}(2m+1) \rangle= \delta_{m,n}$, and $$\begin{aligned}
\langle \exp(\sigma_{2n+1}), \zeta^{\mathfrak{u}}(w) \rangle &  = 0 \qquad \hbox{ for all } w\in \mathrm{Lyn}(X_{3,2}) \hbox{ such that  } \deg_3 w>1 \  .\nonumber
\end{aligned}$$*

The elements $\sigma_{2n+1}$ can be taken as generators in §1.1 (1). It is perhaps surprising that one can define canonical elements of the motivic Galois group at all. These should perhaps be taken with a pinch of salt, since there may be other natural generators for the algebra of motivic multiple zeta values.

**Corollary 5**. *There is a unique homomorphism $\tau: \mathcal{H}\rightarrow \mathbb{Q}$ (see $(\ref{Hdef})$) such that: $$\langle \tau, \zeta^{\mathfrak{m}}(2) \rangle  = - \textstyle{1 \over 24}$$ and $\langle \tau, \zeta^{\mathfrak{m}}(w) \rangle   = 0$ for all $w\in \mathrm{Lyn}(X_{3,2})$ such that $w \neq 2$.*

Applying this map to the motivic Drinfeld associator defines a canonical (but not explicit!) rational associator: $$\tau (\mathcal{Z}^{\mathfrak{m}}) \in  {}_0 \Pi_{1}(\mathbb{Q}) = \mathbb{Q}\langle \langle  x_0, x_1 \rangle \rangle$$

By acting on the canonical rational associator with elements $\sigma_{2n+1}$, one deduces that there exists a huge space of rational associators (which forms a torsor over $G^{dR}(\mathbb{Q})$). Such associators have several applications (see, for example [@Fu]).

## Transcendence conjectures

**Conjecture 15**. *A variant of Grothendieck's period conjecture states that $$\mathrm{per}: \mathcal{P}_{\mathcal{MT}(\mathbb{Z})}^{\mathfrak{m}} \longrightarrow \mathbb{C}$$ is injective. In particular, its restriction to $\mathcal{H}$ is injective also.*

The last statement, together with theorem $\ref{thmHoffMZVLi}$, is equivalent to

**Conjecture 16**. *(Hoffman) The elements $\zeta(n_1,\ldots, n_r)$ for $n_i \in \{2,3\}$ are a basis for the $\mathbb{Q}$-vector space spanned by multiple zeta values.*

This in turn implies a conjecture due to Zagier, stating that the dimension of the $\mathbb{Q}$-vector space of multiple zeta values of weight $N$ is equal to $d_N$ $(\ref{dNdef}),$ and furthermore that the ring of multiple zeta values is graded by the weight. Specialising further, we obtain the following folklore

**Conjecture 17**. *The numbers $\pi, \zeta(3),\zeta(5), \zeta(7), \ldots$ are algebraically independent.*

## Idea of proof of theorem $\ref{thmHoffMZVLi}$

The proof of linear independence is by induction on the number of $3$'s. In the case where there are no 3's, one can easily show by adapting an argument due to Euler that $$\zeta(\underbrace{2,\ldots, 2}_n) = {\pi^{2n}  \over (2n+1)!}\  .$$ The next interesting case is where there is one 3.

**Theorem 18**. *(Zagier [@Zagier]). Let $a,b\geq 0$. Then $$\zeta( \underbrace{2,\ldots 2}_a,3, \underbrace{2,\ldots, 2}_{b})=  2\,\sum_{r=1}^{a+b+1}(-1)^r (A^r_{a,b}-B^r_{a,b})\, \zeta(2r+1)\, \zeta(\underbrace{2,\ldots, 2}_{a+b+1-r})\,$$ where, for any $a,b,r\in \mathbb{N}$, $A^r_{a,b} =  \binom{2r}{2a+2}$, and $B^r_{a,b} =\bigl(1-2^{-2r}\bigr)\binom{2r}{2b+1}$.*

Zagier's proof of this theorem involves an ingenious mixture of analytic techniques. The next step in the proof of theorem $\ref{thmHoffMZVLi}$ is to lift Zagier's theorem to the level of motivic multiple zeta values by checking its compatibility with the coaction $(\ref{mainformula})$ and using theorem 13. Since then, the proof of theorem 18 was simplified by Li [@Li], and Terasoma [@TerasomaBZ] has verified that it can be deduced from associator equations. Since the associator equations are known to hold between motivic multiple zeta values, it follows that, in principle, this part of the proof can now be deduced directly by elementary methods (i.e., without using theorem 13).

From the motivic version of theorem 18, one can compute the action of the abelianization of $U^{dR}$ on the vector space built out of the elements $\zeta^{\mathfrak{m}}(n_1,\ldots, n_r)$, with $n_i =2,3$, graded by the number of $3$'s. This action can be expressed by certain matrices constructed out of the combinatorial formula $(\ref{mainformula})$, whose entries are linear combinations of the coefficients $A^r_{a,b}$ and $B^r_{a,b}$ of theorem 18. The key point is that these matrices have non-zero determinant $2$-adically, and are hence invertible. At its heart, this uses the fact that the $B^r_{a,b}$ terms in theorem 18 dominate with respect to the $2$-adic norm due to the factor $2^{-2r}$.

# Roots of unity

There are a handful of exceptional cases when one knows how to generate certain categories of mixed Tate motives over cyclotomic fields and write down their periods. These results are due to Deligne [@DeRoots], inspired by numerical computations due to Broadhurst in 1997 relating to computations of Feynman integrals.

Let $N\geq 2$ and let $\mu_N$ be the group of $N^{\mathrm{th}}$ roots of unity, and consider $$\label{P1minusmuN}
\mathbb{P}^1 \backslash \{0,\mu_N, \infty\}$$ Fix a primitive $N^{\mathrm{th}}$ root $\zeta_N$. One can consider the corresponding motivic fundamental groupoid (with respect to suitable tangential base points) and ask whether it generates the category $\mathcal{MT}(\mathcal{O}_N[\textstyle{1 \over N}])$, where $\mathcal{O}_N$ is the ring of integers in the field $\mathbb{Q}(\zeta_N)$. Goncharov has shown that for many primes $N$, and in particular, for $N=5$, this is false: already in weight two, there are motivic periods of this category which cannot be expressed as motivic iterated integrals on $\mathbb{P}^1 \backslash \{0,\mu_N, \infty\}$.

In certain exceptional cases, Deligne has proven a stronger statement:

**Theorem 19**. *For $N=2,3,4,6$ (resp. $N=8$) the motivic fundamental group $$\pi_1^{mot}( \mathbb{P}^1\backslash \{0,1,\infty\}, \overset{\rightarrow}{1}\!_0, \zeta_N) \qquad \big(\hbox{resp. }  \pi_1^{mot}( \mathbb{P}^1\backslash \{0,\pm 1,\infty\}, \overset{\rightarrow}{1}\!_0, \zeta_8) \big)$$ generates the categories $\mathcal{MT}(\mathcal{O}_N[\textstyle{1 \over N}])$ for $N =2,3,4, 8$, and $\mathcal{MT}(\mathcal{O}_N)$ for $N = 6$.*

Iterated integrals on $(\ref{P1minusmuN})$ can be expressed in terms of cyclotomic multiple zeta values[^7] which are defined for $(n_r, \varepsilon_r) \neq (1,1)$ by the sum $$\zeta(n_1,\ldots, n_r ; \varepsilon_1, \ldots, \varepsilon_r) = \sum_{0< k_1 < k_2 <\ldots <k_r} {\varepsilon_1^{k_1} \ldots \varepsilon_r^{k_r}
\over k_1^{n_1} \ldots k_r^{n_r}}$$ where $\varepsilon_{1},\ldots, \varepsilon_{r}$ are roots of unity. The weight is defined as the sum of the indices $n_1+
\ldots +n_r$ and the depth is the increasing filtration defined by the integer $r$. It is customary to use the notation $$\zeta(n_1,\ldots, n_{r-1},   n_r \zeta_N) = \zeta(n_1,\ldots, n_r ; \underbrace{1,\ldots , 1}_{r-1} , \zeta_N)\ .$$ One can define motivic versions relative to the canonical fiber functor $\omega$ ([@DG], §1.1) playing the role of what was previously the de Rham fiber functor (the two are related by $\omega_{dR} = \omega\otimes \mathbb{Q}(\zeta_N)$), and the Betti realisation functor which corresponds to the embedding $\mathbb{Q}(\zeta_N) \subset \mathbb{C}$. Denote these motivic periods by a superscript $\mathfrak{m}$. Recall that $\mathbb{L}^{\mathfrak{m}}$ is the motivic Lefschetz period of example 3, whose period is $2 \pi i$. Let $X_{odd} = \{1,3,5,\ldots \}$ with the ordering $1>3>5 \ldots$. Rephrased in the language of motivic periods, Deligne's results for $N=2,3,4$ yield:

1.  ($N=2$; algebra generators). The following set of motivic periods: $$\{ \mathbb{L}^{\mathfrak{m}} \} \cup \{ \zeta^{\mathfrak{m}}(n_1,\ldots,  n_{r-1}, - n_{r})\hbox{ where } (n_r,\ldots, n_1) \in \mathrm{Lyn}(X_{odd})\}$$ are algebraically independent over $\mathbb{Q}$. The monomials in these quantities form a basis for the ring of geometric motivic periods[^8] of $\mathcal{MT}(\mathbb{Z}[{1 \over 2}])$.

2.  ($N=3, 4$; linear basis). The set of motivic periods $$\zeta^{\mathfrak{m}}(n_1,\ldots, n_{r-1},   n_r \zeta_N) (\mathbb{L}^{\mathfrak{m}})^p \qquad \hbox{ where } n_i \geq 1, p\geq 0$$ are linearly independent over $\mathbb{Q}$. They form a basis for the space of geometric motivic periods of $\mathcal{MT}(\mathcal{O}_N  [ \textstyle{1 \over N}])$, for $N=3,4$ respectively.

By applying the period map, each case gives a statement about cyclotomic multiple zeta values. In the case $N=2$, the underlying field is still $\mathbb{Q}$, and it follows from $(i)$ that every multiple zeta value at $2^{\mathrm{nd}}$ roots of unity (sometimes called an Euler sum) is a polynomial with rational coefficients in $$(2 \pi i)^2  \quad \hbox{ and } \quad \zeta(n_1,\ldots,n_{r-1},  -n_{r})  \qquad  \hbox{ where } \quad (n_1,\ldots, n_r) \in \mathrm{Lyn}(X_{odd})\ .$$ This decomposition respects the weight and depth, where the depth of $(2 \pi i)^n$ is $1$. Thus an Euler sum of weight $N$ and depth $r$ can be expressed as a polynomial in the above elements, of total weight $N$ and total depth $\leq r$.

# Depth

The results of the previous section for $N=2,3,4,6,8$ crucially use the fact that the depth filtration is dual to the lower central series of the corresponding motivic Galois group. A fundamental difference with the case $N=1$ is that this fact is false for $\mathbb{P}^1 \backslash \{0,1,\infty\}$, due to a defect closely related to modular forms.

Recall that ${}_0 \Pi_{1}$ is a group for the Ihara action $\circ$. Let $\mathrm{Lie } ({}_0 \Pi_{1})$ denote its Lie algebra. Its bracket is denoted by $\{\  , \  \}$. Denote the images of the canonical generators §3.1 by $\sigma_{2n+1} \in \mathrm{Lie } ({}_0 \Pi_{1})(\mathbb{Q})$, for $n\geq 1$. They are elements of the free graded Lie algebra on two generators $x_0, x_1$, and we have, for example $$\sigma_3 = [x_0,[x_0,x_1]] +  [x_1,[x_1,x_0]]$$ The higher $\sigma_{2n+1}$ are of the form $\sigma_{2n+1} = \mathrm{ad}(x_0)^{2n} (x_1)$ plus terms of degree $\geq 2$ in $x_1$, but are not known explicitly except for small $n$. By theorem 2, the $\sigma_{2n+1}$ freely generate a graded Lie subalgebra of $\mathrm{Lie } ({}_0 \Pi_{1})(\mathbb{Q})$ which we denote by $\mathfrak{g}$. The depth filtration $\mathcal{D}$ on $\mathfrak{g}$ is the decreasing filtration given by the degree in the letter $x_1$. In 1993, Ihara and Takao observed that $$\label{IharaTakao}
\{\sigma_3, \sigma_9\} - 3  \{\sigma_5, \sigma_7\}  = {691 \over 144} \,   e_\Delta$$ where $e_\Delta$ is an element with integer coefficients of depth $\geq 4$ (degree $\geq 4$ in $x_1$), and the coefficient $691$ on the right-hand side is the numerator of the Bernoulli number $B_{12}$. The element $e_\Delta$ is sparse:[^9] indeed, computations in the early days gave the impression that the right-hand side is zero, although we now know that the $\sigma_{2n+1}$ generate a free Lie algebra.

Relations such as $(\ref{IharaTakao})$ show that the structure of $\mathfrak{g}$ is related to arithmetic, but more importantly show that the associated depth-graded Lie algebra $\mathrm{gr}_{\mathcal{D}}\,  \mathfrak{g}$ is not free, since the left-hand side of $(\ref{IharaTakao})$ vanishes in $\mathrm{gr}^2_{\mathcal{D}}\,  \mathfrak{g}$. The depth filtration on $\mathfrak{g}$ corresponds, dually, to the depth filtration on motivic multiple zeta values, and $(\ref{IharaTakao})$ implies that motivic multiple zeta values of depth $\leq 2$ are insufficient to span the space of all (real geometric) motivic periods of $\mathcal{MT}(\mathbb{Z})$ in weight 12 (one needs to include elements of depth $\geq 4$ such as $\zeta^{\mathfrak{m}}(2,2,2,3,3)$ in a basis). By counting dimensions, this can be interpreted as a relation, viz: $$\label{exoticrel}
 28 \, \zeta^{\mathfrak{m}}(3,9)+  150 \, \zeta^{\mathfrak{m}}(5,7) + 168  \, \zeta^{\mathfrak{m}}(7,5) = {5197\over 691} \zeta^{\mathfrak{m}}(12)  \ Ê.$$ The corresponding relation for multiple zeta values was found in [@GKZ] and generalised to an infinite family corresponding to cuspidal cohomology classes of $\mathrm{SL}_2(\mathbb{Z})$. In particular, the family of motivic multiple zeta values $$\zeta^{\mathfrak{m}}(2n_1+1,\ldots, 2n_r+1) \zeta^{\mathfrak{m}}(2k)$$ cannot be a basis for $\mathcal{H}$, although it has the right dimensions in each weight $(\ref{dNdef})$. The Hoffman basis $(\ref{HoffmotMZVs})$ gets around such pathologies, since, for example, its elements in weight 12 have depths between four and six.

In 1997, Broadhurst and Kreimer made exhaustive numerical computations on the depth filtration of multiple zeta values, which led them to the following conjecture, translated into the language of motivic multiple zeta values.

**Conjecture 20**. *(Motivic version of the Broadhurst-Kreimer conjecture) Let $\mathcal{D}$ denote the increasing filtration on $\mathcal{H}$ induced by the depth. Then $$\label{BKconj}
\sum_{N, d\geq 0} \dim_{\mathbb{Q}}\,  (gr^{\mathcal{D}}_d \mathcal{H}_{N})\,  s^d t^N = { 1  + \mathbb{E}(t) s \over 1- \mathbb{O}(t) s + \mathbb{S}(t) s^2 - \mathbb{S}(t) s^4}\ ,$$ where $\mathbb{E}(t) =\textstyle {t^2 \over 1-t^2}$, $\mathbb{O}(t) =\textstyle{t^3 \over 1-t^2}$, and $\mathbb{S}(t) =\textstyle{t^{12} \over (1-t^4)(1-t^6)} .$*

Note that equation $(\ref{BKconj})$ specializes to $(\ref{dNdef})$ on setting $s$ equal to $1$. The series $\mathbb{E}(t)$ and $\mathbb{O}(t)$ are the generating series for the dimensions of the spaces of even and odd single motivic zeta values. The interpretation of $\mathbb{S}(t)$ as the generating series for cusp forms for $\mathrm{SL}_2(\mathbb{Z})$ suggests a deeper connection with modular forms which is well understood in depth two. By work of Zagier, and Goncharov, formula $(\ref{BKconj})$ has been confirmed in depths $2$ and $3$ (i.e., modulo $s^4$).

An interpretation for conjecture $(\ref{BKconj})$ in terms of the structure of $\mathrm{gr}_{\mathcal{D}} \mathfrak{g}$, as well as a complete conjectural description of generators and relations of $\mathrm{gr}_{\mathcal{D}} \mathfrak{g}$ in terms of modular forms for $\mathrm{SL}_2(\mathbb{Z})$ was given in [@BrDepth]. A deeper geometric understanding of this conjecture would seem to require a framework which places multiple zeta values and modular forms on an equal footing, which is the topic of §6.

# Multiple modular values

In this final paragraph, I want suggest applying the philosophy of §1.4 to iterated integrals on (orbifold) quotients of the upper half plane $$\mathbb{H}= \{ \tau \in \mathbb{C}: \mathrm{Im\, } (\tau) > 0 \}$$ by finite index subgroups $\Gamma \leq \mathrm{SL}_2(\mathbb{Z})$. Iterated integrals of modular forms were first studied by Manin [@Ma1; @Ma2]. Here, I shall only consider the case $\Gamma = \mathrm{SL}_2(\mathbb{Z})$.

## Eichler-Shimura integrals

Denote the space of homogenous polynomials of degree $n\geq 0$ with rational coefficients by $$V_n = \bigoplus_{i+j =n}   \mathbb{Q}X^i Y^j$$ It admits a right action of $\Gamma$ via the formula $(X,Y)|_{\gamma} = (aX+bY, cX+dY)$, where $\gamma = \left( \begin{smallmatrix} a&b\\ c&d \end{smallmatrix} \right)$. Let $f(\tau)$ be a modular form of weight $k$ for $\Gamma$. Define $$\underline{f}(\tau) = (2 \pi i)^{k-1} f(\tau) (X - \tau Y)^{k-2} d\tau \qquad \in \qquad \Gamma(\mathbb{H}, \Omega^1_{\mathbb{H}} \otimes V_{k-2})$$ It satisfies the invariance property $\underline{f}(\gamma(\tau))\big|_{\gamma} = \underline{f}(\tau)$ for all $\gamma \in \Gamma$. For $f$ a cusp form, the classical Eichler-Shimura integral (see, e.g., [@KZ]) is $$\label{ESintegral}
 \int_0^{\infty} \underline{f}(\tau)  =  \sum_{n=1}^{k-1}  c_n L(f,n) X^{k-n-1} Y^{n-1}$$ where $c_n$ are certain explicit constants (rational multiples of a power of $\pi$) and $L(f,s)$ is the analytic continuation of the $L$-function $L(f,s) = \sum_{n\geq 1} {a_n \over n^s}$ of $f$, where $f(\tau) = \sum_{n\geq 1} a_n q^n$ and $q=e^{2 \pi i \tau}$. Manin showed that if $f$ is a Hecke eigenform, there exist $\omega^{+}_f, \omega^{-}_f \in \mathbb{R}$ such that $$\int_0^{\infty} \underline{f}(\tau)  = \omega^+_f P_f^+(X,Y) + \omega^-_f P_f^-(X,Y)$$ where $P_f^{\pm}(X,Y) \in V_{k-2}\otimes \overline{\mathbb{Q}}$ are polynomials with algebraic coefficients which are invariant (resp. anti-invariant) with respect to $(X,Y) \mapsto (-X,Y)$.

Recall that the Eisenstein series of weight $2k$, for $k\geq 2$, is defined by $$\nonumber
e_{2k} (q) = - {B_{2k} \over 4k} + \sum_{ n \geq 1} \sigma_{2k-1}(n) q^n \ , \qquad q=e^{2 \pi i \tau}$$ where $B_{2k}$ is the $2k^{\mathrm{th}}$ Bernoulli number, and $\sigma$ denotes the divisor function. The corresponding integrals for Eisenstein series diverges. Zagier showed how to extend the definition of the Eichler-Shimura integrals to the case $e_{2k}$, giving [@KZ]

$$\quad { (2k-2)!  \over 2} \zeta(2k-1)  (Y^{2k-2} - X^{2k-2})   - {  (2\pi i)^{2k-1} \over  4k (2k-1)} \sum_{a+b=2k, a, b\geq 1} \binom{2k}{a} B_a B_b X^{a-1} Y^{b-1}  \label{Zagint}$$

Manipulating this formula leads to expressions for the odd Riemann zeta values in terms of Lambert series similar to the following formula due to Ramanujan: $$\zeta(3) = {7 \over 180} \pi^3 - 2 \sum_{n \geq 1} {1 \over n^3 (e^{2n  \pi } -1)}\ .$$ It converges very rapidy. One wants to think of $(\ref{Zagint})$ as pointing towards a modular construction of $\zeta^{\mathfrak{m}}(2k-1)$.

## Regularisation

The theory of tangential base points ([@DeP1], §15) gives a general procedure for regularising iterated integrals on curves. If one applies this to the orbifold $\Gamma \backslash \!\!\backslash \mathbb{H}$, where $\Gamma = \mathrm{SL}_2(\mathbb{Z})$, one can show that it yields the completely explicit formulae below, which generalise Zagier's formula for a single Eisenstein series. I shall only state the final answer. Via the map $$\tau \mapsto q= \exp(2 i \pi \tau) : \mathbb{H}\longrightarrow   \{q \in \mathbb{C}: 0< |q| < 1 \}=D^{\times}$$ a natural choice of tangential base point (denoted $\overset{\rightarrow}{1}\!_{\infty}$) corresponds to the tangent vector $1$ at $q=0$. Since in this case we have explicit models $\mathbb{H}\subset \mathbb{C}$ for a universal covering space of $\Gamma \backslash \!\!\backslash \mathbb{H}$, and $\mathbb{C}$ for the universal covering of $D^{\times}$, one can compute all regularised iterated integrals by pulling them back to $\mathbb{C}$ as follows.

First, if $f= \sum_{n\geq 0 } f_n q^n$ is the Fourier expansion of $f$, write $$\label{finfinity}
\underline{f}^{\infty}(\tau) = (2  \pi i )^{k-1} f_0 (X- \tau Y) ^{k-2}  d \tau \qquad \in \qquad \Gamma(\mathbb{C}, \Omega^1_{\mathbb{C}} \otimes V_{k-2})$$ Define a linear operator $R$ on the tensor coalgebra on $\Gamma(\mathbb{C}, \Omega^1_{\mathbb{C}} \otimes V)$ by $$\begin{aligned}
R [  \omega_1 | \ldots | \omega_n] &  = \sum_{i=0}^n (-1)^{n-i} [\omega_1 | \ldots | \omega_i] \, \hbox{\rus x} \,[\omega_n^{\infty} | \ldots | \omega_{i+1}^{\infty}]  \nonumber \\
& = \sum_{i=1}^n (-1)^{n-i}\Big[ [\omega_1 | \ldots | \omega_{i-1}] \, \hbox{\rus x} \,[\omega_n^{\infty} | \ldots | \omega_{i+1}^{\infty}] \Big| \omega_i- \omega_i^{\infty}\Big]    \ .\nonumber
\end{aligned}$$ where $V= \bigoplus_k V_k$ and $\omega^{\infty}$ is the 'residue at infinity' of $\omega$ defined by $(\ref{finfinity})$. The regularised iterated integral can be expressed as *finite* integrals $$\int_{\tau}^{\overset{\rightarrow}{1}\!_{\infty}} [ \underline{\omega}_1 | \ldots | \underline{\omega}_n ] = \sum_{i=0}^n \int_{\tau}^{\infty} R  [ \underline{\omega}_1 | \ldots | \underline{\omega}_i] \int_{\tau}^{0}  [  \underline{\omega}^{\infty}_{i+1} | \ldots | \underline{\omega}_{n}^{\infty} ]$$ It takes values in $V_{k_1-2} \otimes \ldots \otimes V_{k_n-2}\otimes \mathbb{C}$ if $\omega_1, \ldots, \omega_n$ are of weights $k_1,\ldots k_n$, and hence admits a right action of $\Gamma$. The integrals in the right factor on the right-hand side are simply polynomials in $\tau$ and can be computed explicitly.

## Cocycles

Choose a basis of Hecke normalised eigenforms $f_i$ indexed by non-commuting symbols $A_i$, and form the generating series $$I(\tau; \infty) = \sum_{i_k, n\geq 0} A_{i_1} \ldots A_{i_n} \int_{\tau}^{\overset{\rightarrow}{1}\!_{\infty}} [ \underline{\omega}_{i_1} | \ldots | \underline{\omega}_{i_n} ]$$ For every $\gamma \in \Gamma$, there exists a formal power series $C_{\gamma}$ in the $A_i$ such that $$\label{Cdef}
I(\tau; \infty)  =  I(\gamma(\tau);\infty)|_{\gamma}\,  C_{\gamma}$$ which does not depend on $\tau$. It satisfies the cocycle relation $$C_{gh} = C_g\big|_h \, C_h \quad \hbox{ for all } g,h \in \Gamma\ .$$ The part of the cocycle $C$ which involves iterated integrals of cusp forms was previously considered by Manin [@Ma1; @Ma2]. Since the group $\Gamma$ is generated by $$S=
\left(
\begin{array}{cc}
  0   & -1  \\
   1  &   0
\end{array}
\right)\quad, \quad  T= \left(
\begin{array}{cc}
  1   &  1  \\
   0  &   1
\end{array}
\right)\ ,
\ $$ the cocycle $C$ is determined by $C_S$ and $C_T$. The series $C_T$ can be computed explicitly and its coefficients lie in $\mathbb{Q}[2\pi i]$.

**Definition 3**. *Define the ring of multiple modular values with respect to the group $\Gamma = \mathrm{SL}_2(\mathbb{Z})$ to be the subring of $\mathbb{C}$ generated by the coefficients of $C_S$.*

The series $C_S$ is a kind of analogue of Drinfeld's associator $\mathcal{Z}$. Its terms of degree 1 in the $A_i$ are precisely the Eichler-Shimura integrals $(\ref{ESintegral})$ and $(\ref{Zagint})$. Setting $\tau=i$ in $(\ref{Cdef})$ gives integrals which converge extremely fast and are very well suited to numerical computation.

## Galois action

One can mimic the Betti-de Rham aspects of the theory of the motivic fundamental group of $\mathbb{P}^1 \backslash\{0,1,\infty\}$ as follows:

1.  The coefficients of $C_S$ can be interpreted as certain periods of the relative unipotent completion of $\Gamma$. This was defined by Deligne as follows. Let $k$ be a field of characteristic $0$ and $S$ a reductive algebraic group over $k$. Suppose that $\Gamma$ is a discrete group equipped with a Zariski dense homomorphism $\rho: \Gamma \rightarrow S(k).$ The completion of $\Gamma$ relative to $\rho$ is an affine algebraic group scheme $\mathcal{G}_{\Gamma}$, which sits in an exact sequence $$1 \longrightarrow \mathcal{U}_{\Gamma} \longrightarrow \mathcal{G}_{\Gamma} \longrightarrow S \longrightarrow 1$$ where $\mathcal{U}_{\Gamma}$ is pro-unipotent. There is a natural map $\Gamma \rightarrow \mathcal{G}_{\Gamma}(k)$ which is Zariski dense, and whose projection onto $S(k)$ is the map $\rho$.

2.  In 'geometric' situations, one expects the relative completion to be the Betti realisation of something which is motivic. Indeed, Hain has shown [@HaMHS], [@HaGPS] that $\mathcal{O}(\mathcal{G}_{\Gamma})$ carries a mixed Hodge structure in this case. As a result, one can define Hodge-motivic periods and try to carry out §1.4.

3.  The action of the unipotent radical of the Tannaka group of mixed Hodge structures acts via the automorphism group of a space of non-abelian cocyles of $\Gamma$ with coefficients in $\mathcal{U}_{\Gamma}$. It is a certain semi-direct product of $\mathcal{U}_{\Gamma}$ with a group of non-commutative substitutions $\mathrm{Aut}(\mathcal{U}_{\Gamma})^S$. An inertia condition corresponds, in the case $\Gamma = \mathrm{SL}_2(\mathbb{Z})$, to the fact that $C_T$ is fixed, and there are further constraints coming from the action of Hecke operators. The explicit expression for $C_T$ yields precise information about the action of the Hodge-Galois group.

The following key example illustrates how multiple modular values for $\mathrm{SL}_2(\mathbb{Z})$ resolve the depth-defect for multiple zeta values as discussed in §5.

**Example 21**. *On $\mathbb{P}^1 \backslash \{0,1,\infty\}$ there are $2^{12}$ integrals of weight $12$, namely $$\int_{dch} \omega_{i_1} \ldots \omega_{i_{12}} \quad  \hbox{ where  }  \quad  \omega_{i_j} \in \{ {dt \over t}, {dt \over 1-t}\} \ .$$ However the space of multiple zeta values $\mathcal{Z}_{12}$ in weight $12$ has dimension at most $d_{12} = 12$, so there are a huge number of relations. Indeed, modulo products of multiple zeta values of lower weights, there are at most two elements of weight 12: $$\label{zetainweight12}
\zeta(3,3,2,2,2) \qquad \hbox{ and } \qquad  \zeta(3,2,3,2,2)$$ by the corollary to theorem 14. They are conjectured to be algebraically independent. Note that multiple zeta values of depths $\leq 2$ (or $\leq 3$ for that matter) will not suffice to span $\mathcal{Z}_{12}$ by equation $(\ref{exoticrel})$.*

*On the other hand, we can consider the coefficients of $C_S$ corresponding to regularised iterated integrals of Eisenstein series $$\label{eisint}
\int_0^{\overset{\rightarrow}{1}\!_{\infty}} \underline{e}_{2a}( X,Y)\underline{e}_{2b}( X,Y) \in \mathbb{C}[X,Y]$$ If we are interested in periods modulo products, there are just two relevant cases: $(2a,2b)  \in \{(4,10), (6,8)\}$. The description 3 above enables one to extract the relevant numbers from the coefficients of these polynomials. One finds experimentally that one obtains exactly the elements $(\ref{zetainweight12})$ modulo products, and that this is consistent with the coaction on the corresponding Hodge-motivic periods. Thus $\mathcal{Z}_{12}$ is spanned by exactly the right number of multiple modular values (which are linear combinations of the coefficients of $(\ref{eisint})$).*

The example shows that in weight $12$, there are exactly two multiple modular values (modulo products) which are multiple zeta values, and they conjecturally satisfy no relations. By contrast, multiple zeta values in weight 12 are hugely over-determined, and satisfy a vast number of relations. Furthermore, the depth-defect described in §5 can be directly related to the appearance of special values of $L$-functions of cusp forms amongst certain coefficients of (6.7).\
In conclusion, a rather optimistic hope is that a theory of motivic multiple modular values for congruence subgroups of $\mathrm{SL}_2(\mathbb{Z})$ might provide a more natural construction of the periods of mixed Tate motives over cyclotomic fields (and much more) than the motivic fundamental groupoid of the projective line minus Nth roots of unity, which suffers from the depth defect in the case N=1 (§5), and from absent periods in non-exceptional cases such as N=5 (§4).

# References

7

Y. André: *Une introduction aux motifs*, Panoramas et Synthèses 17, SMF (2004).

A. Borel: *Stable real cohomology of arithmetic groups*, Annales Ecole Normale Sup. 7, No. 4, (1974), 235-272.

A. Borel: *Cohomologie de $SL_{n}$ et valeurs de fonctions zêta aux points entiers*, Annali della Scuola Norm. di Pisa, (1976), 613-635, + erratum.

Belyi: *On Galois Extensions of a Maximal Cyclotomic Field*, Math. USSR-Izvestija 14:247-256 (1980)

F. Brown: *Mixed Tate motives over $\mathbb{Z}$*, Annals of Math., volume 175, no. 1, 949-976 (2012).

F. Brown: *Decomposition of motivic multiple zeta values*, 'Galois-Teichmuller theory and Arithmetic Geometry', Adv. Stud. Pure Math., 63, (2012).

F. Brown: *Depth-graded motivic multiple zeta values*, <http://arxiv.org/abs/1301.3053>.

P. Cartier: *Fonctions polylogarithmes, nombres polyztas et groupes pro-unipotents*, Sminaire Bourbaki, Astrisque No. 282 (2002), Exp. No. 885, 137-173.

P. Deligne: *Catégories Tannakiennes*, Grothendieck Festschrift, vol. II, Birkhäuser Progress in Math. 87 (1990), 111-195.

P. Deligne: *Le groupe fondamental de la droite projective moins trois points*, Galois groups over Q (Berkeley, CA, 1987), 79-297, Math. Sci. Res. Inst. Publ., 16 (1989)

P. Deligne: *Le groupe fondamental unipotent motivique de $\mathrm{G}_m - \mu_N$, pour $N=2,3,4,6$ ou $8$*, Publ. Math. Inst. Hautes Études Sci. 101 (2010).

P. Deligne: *Multizêtas*, Séminaire Bourbaki, expos 1048, Astrisque 352 (2013)

P. Deligne: *Letter to Brown and Zagier*, 28 april 2012.

P. Deligne, A. B. Goncharov: *Groupes fondamentaux motiviques de Tate mixte*, Ann. Sci. École Norm. Sup. 38 (2005), 1--56.

V. Drinfeld: *On quasi-triangular quasi-Hopf algebras and some group closely related with $\mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$*, Algebra i Analiz 2 (1990), no. 4, 149-181.

: *Four groups related to associators*, arXiv:1108.3389 (2011).

: *Double zeta values and modular forms*, Automorphic forms and zeta functions, 71-106, World Sci. Publ., Hackensack, NJ, 2006.

A. Goncharov: *Multiple polylogarithms and Mixed Tate Motives*, arXiv:0103059, (2001).

A. Goncharov, Y. Manin: *Multiple $\zeta$-motives and moduli spaces $\overline{\mathfrak{M}}_{0,n}$*, Compos. Math. 140 (2004), no. 1, 1-14.

A. B. Goncharov: *Galois symmetries of fundamental groupoids and noncommutative geometry*, Duke Math. J.128 (2005), 209-284.

A. Grothendieck : *Esquisse d'un programme*, <http://www.math.jussieu.fr/~leila/grothendieckcircle/EsquisseFr.pdf>

R. Hain, M. Matsumoto: *Weighted completion of Galois groups and Galois actions on the fundamental group of $\mathbb{P}^1\backslash \{0,1,\infty\}$*, Compositio Math. 139 (2003), no. 2, 119-167.

R. Hain: *The Hodge de Rham theory of the relative Malcev completion*, Ann. Sci. École Norm. Sup. 31 (1998), 47--92.

R. Hain: 'The Hodge-de Rham Theory of Modular Groups', http://arxiv.org/abs/1403.6443.

M. E. Hoffman: *The Algebra of Multiple Harmonic Series*, Journ. of Algebra 194 (1997), 477-495.

Y. Ihara: *The Galois representation arising from $\mathbb{P}^1-\{0,1,\infty\}$ and Tate twists of even degree*, Galois groups over $\mathbb{Q}$, 299-313, Math. Sci. Res. Inst. Publ., 16, (1989).

Y. Ihara: *Braids, Galois Groups, and Some Arithmetic Functions*, Proceedings of the International Congress of Mathematicians, Vol. I, II (Kyoto, 1990), 99-120.

: *Periods*, Mathematics unlimited-2001 and beyond, 771-808, Springer, Berlin, (2001).

*Modular forms with rational periods*, Modular forms (Durham, 1983), 197-249.

M. Levine: *Tate motives and the vanishing conjectures for algebraic K-theory*, Algebraic K-theory and algebraic topology (Lake Louise, AB, 1991), 167-188.

Z-H. Li: *Some identities in the harmonic algebra concerned with multiple zeta values*, Int. J. Number Theory 9 (2013), no. 3, 783- 798.

Y. Manin: *Iterated integrals of modular forms and non-commutative modular symbols*, Algebraic geometry and number theory, 565-597, Prog. Math. 253 (2006).

Y. Manin: *Iterated Shimura integrals*, Moscow Math. J. 5 (2005), 869-881

G. Racinet: *Doubles mélanges des polylogarithmes multiples aux racines de l'unité*, Publ. Math. Inst. Hautes Études Sci. 95 (2002), 185-231.

G. Shimura: *On the periods of modular forms*, Math. Annalen 229 (1977), 211-221.

T. Terasoma: *Geometry of multiple zeta values*, International Congress of Mathematicians. Vol. II, 627-635, (2006). T. Terasoma: *Brown-Zagier relation for associators*, arXiv:1301.7474 (2013)

D. B. Zagier: *Evaluation of the multiple zeta values $\zeta(2,\dots,2,3,2,\dots,2)$*, Ann. of Math. (2) 175 (2012), no. 2, 977-1000.

Z. Wojtkowiak : *Cosimplicial objects in algebraic geometry*, Algebraic K-theory and algebraic topology (Lake Louise, AB, 1991), 287-327, NATO Adv. Sci. Inst. Ser. C Math. Phys. Sci., 407, (1993).

[^1]: Beneficiary of ERC Grant 257638

[^2]: In the field of multiple zeta values, the 'weight' refers to one half of the Hodge-theoretic weight, so that $\mathbb{L}^{\mathfrak{m}}$ has degree $1$ instead of $2$. I shall adopt this terminology from here on.

[^3]: In fact, we should never need to compute relations explicitly using 'standard operations' such as those described in [@KoZa]; these are taken care of automatically by the Tannakian formalism, and the bound on the Ext groups of $\mathcal{MT}(\mathbb{Z})$ coming from Borel's theorems on algebraic $K$-theory.

[^4]: Grothendieck refers to $\mathrm{SL}_2(\mathbb{Z})$ as '*une machine à motifs'*

[^5]: It shall also be written $\pi_1^{dR}(X,x,y)$ but does not depend on the choice of base points. The fact that there is a canonical isomorphism $\pi_1^{dR}(X,x,y) = \pi_1^{dR}(X)$ is equivalent to saying that there is a 'canonical de Rham path' between the points $x$ and $y$.

[^6]: One can define a homomorphism $\mathcal{P}^{\mathfrak{m},+}_{\mathcal{MT}(\mathbb{Z}),\mathbb{R}} \rightarrow \mathcal{P}^{\mathfrak{u}}_{\mathcal{MT}(\mathbb{Z})}$ which sends $\zeta^{\mathfrak{m}}(n_1,\ldots, n_r)$ to $\zeta^{\mathfrak{u}}(n_1,\ldots, n_r)$ and prove that its kernel is the ideal generated by $\zeta^{\mathfrak{m}}(2)$.

[^7]: The conventions in [@DeRoots] are opposite to the ones used here

[^8]: recall that this is the subring of all motivic periods of the category $\mathcal{MT}(\mathbb{Z}[{1 \over 2}])$ which is generated by motives $M$ which have non-negative weights, i.e., $W_{-1}M=0$.

[^9]: 'most' of its coefficients are zero, see [@BrDepth], §8 for a closed formula for this element.
