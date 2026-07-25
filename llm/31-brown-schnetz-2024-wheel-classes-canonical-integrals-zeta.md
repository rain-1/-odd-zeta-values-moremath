---
title: "The wheel classes in the locally finite homology of $\\mathrm{GL}_n(\\mathbb{Z})$, canonical integrals and zeta values"
authors:
  - "Francis Brown"
  - "Oliver Schnetz"
arxiv_id: "2402.06757v3"
arxiv_url: "https://arxiv.org/abs/2402.06757"
published: "2024-02-09"
journal_ref: "Geom. Topol. 29 (2025) 4389-4447"
doi: "10.2140/gt.2025.29.4389"
source: "papers/31-brown-schnetz-2024-wheel-classes-canonical-integrals-zeta/main.tex"
conversion: pandoc-flat
---

# The wheel classes in the locally finite homology of $\mathrm{GL}_n(\mathbb{Z})$, canonical integrals and zeta values

**Francis Brown, Oliver Schnetz** — Geom. Topol. 29 (2025) 4389-4447

## Abstract

We compute the canonical integrals associated to wheel graphs, and prove that they are proportional to odd zeta values. From this we deduce that wheel classes define explicit non-zero classes in: the locally finite homology of the general linear group $\GL_n(\ZZ)$ in both odd and even ranks, the homology of the moduli spaces of tropical curves, and the moduli space of tropical abelian varieties. We deduce the existence of a doubly infinite family of auxiliary classes in the even commutative graph complex.

---
# Introduction

Let $G$ be a finite connected graph. Assign a variable $x_e$ to each of the edges $e\in E(G)$ of $G$, and let $\sigma_{G}   \subset  {\mathbb P}^{E(G)}({\mathbb R})$ denote the unit coordinate simplex in the projective space of dimension $|E(G)|-1$ with coordinates $x_e, e\in E(G)$. It is defined by the region where all $x_e\geq 0$. We consider integrals over $\sigma_G$ of certain differential forms which are indexed by a positive integer $k$ and defined as follows.

For any family of invertible matrices $X$ consider the differential $k$ form: $$\label{intro:omegandef}
 \omega_X^{k} = \mathrm{tr}\,((X^{-1} \mathrm{d}X)^k)\ .$$ It defines a closed projective differential form in the entries of $X$ which is invariant under left and right multiplication by constant invertible matrices. If the matrices $X$ are symmetric, then $\omega_X^k$ vanishes unless $k\equiv 1 \pmod{4}$. The forms $\omega^{4k+1}_X$, when $X$ ranges over positive definite $n\times n$ symmetric matrices, represent the Borel classes in the stable cohomology [@Borel] of the general linear group $\mathrm{GL}_n({\mathbb Z})$ as $n\rightarrow \infty$.

Now let $\Lambda_{G}$ denote a graph Laplacian matrix associated to $G$. It is a symmetric $h_G \times h_G$ matrix whose entries are linear forms in the $x_e$, where $h_G$ is the number of independent cycles of $G$ (see Section 1.1). Let $n>1$ be odd, and suppose that $G$ has $2n$ edges. In this paper we study the projective integrals $$\label{intro: IGdef} I_{G} (\omega^{2n-1}) =  \int_{\sigma_{G}}  \omega^{2n-1}_{\Lambda_G} \ .$$ It was shown in [@BrSigma] that these integrals are well-defined and always finite. They are generalised Feynman integrals of the kind studied in quantum field theory.

For any $n \geq 3$ let $W_n$ be the wheel graph with $n$ spokes and $2n$ edges. It will be oriented in such a way that, with our conventions, the integral (intro: IGdef) is positive or zero.

**Theorem 1**. *For all odd $n\geq 3$, $$\label{wheelseq}
I_{W_n}(\omega^{2n-1})=n\genfrac(){0pt}{}{2n}{n}\zeta(n).$$*

A much weaker version of this theorem, namely $I_{W_n}(\omega^{2n-1})\neq 0$, already has a considerable number of consequences for the homology of graph complexes, the general linear group, the moduli spaces of tropical curves and abelian varieties, and also for the cohomology of the moduli stacks of curves and abelian varieties. The integrals (intro: IGdef) are closely related to regulator integrals in algebraic $K$-theory and are periods of the graph motives introduced in [@BEK]. A selection of these consequences will be summarised here, and others discussed in greater detail in Section 2.

## Discussion and examples of wheel canonical integrals

The version of the graph Laplacian which we consider is defined as follows. Consider the inner product on ${\mathbb Z}^{E(G)}$ which satisfies $\langle e, e'\rangle = \delta_{e,e'} x_e$, for any pair of edges $e,e'$, where $x_e$ is the variable associated to edge $e$ as defined above. The graph Laplacian is its restriction to the first homology $H_1(G;{\mathbb Z}) \subset {\mathbb Z}^{E_G}$, and in any choice of basis of the free ${\mathbb Z}$-module $H_1(G;{\mathbb Z})$ defines an $h_G \times h_G$ matrix whose entries are linear forms in the $x_e.$ Concretely, if one chooses an orientation on each edge of $e$, and correspondingly a cycle basis $c_1,\ldots, c_{h_G} \in {\mathbb Z}^{E(G)}$ of $H_1(G;{\mathbb Z})$, then the $i,j$th entry of $\Lambda_G$ is $\langle c_i, c_j\rangle$.

<figure id="fig:W3Wn">

<figcaption>The wheel <span class="math inline"><em>W</em><sub>3</sub></span> and the general wheel <span class="math inline"><em>W</em><sub><em>n</em></sub></span>.</figcaption>
</figure>

Let $W_3$ denote the wheel with three spokes graph, with its cycle basis as shown in Figure 1: $$c_1 = e_1 +e_4 - e_6 \  , \ c_2 = e_2+e_5-e_4 \ , \ c_3 = e_3 + e_6 -e_5\ .$$ Then the graph Laplacian, with respect to this basis, is $$\Lambda_{W_3} = \begin{pmatrix}  x_1+x_4+x_6 & -x_4  & -x_6 \\
 -x_4 & x_2+x_4+x_5 & -x_5 \\
 -x_6 & -x_5  & x_3+x_5+x_6
\end{pmatrix}\ .$$ For general $W_n$, we number the edges in the rim from 1 to $n$, oriented in the anticlockwise direction, and the spokes $n+1,\ldots, 2n$, oriented inwards, such that the spoke $n+i$ meets edges $i,i+1$ (where $i$ is taken modulo $n$). Take the cycle basis $c_i$ consisting of the positively oriented triangles with edges $1,n+1,2n$ (for $c_1)$, and $i,n+i,n+i-1$ (for $c_i$, where $i\leq 2 \leq n$): thus $c_1=e_1+e_{n+1}-e_{2n}$ and $c_i=e_i+e_{n+i}-e_{n+i-1}$ for $i \geq 2.$ With this choice of basis the Laplacian $\Lambda_{W_n}$ is

$$\label{introLambdaW}
\left(\begin{array}{cccccc}\!x_1\!+\!x_{n+1}\!+\!x_{2n}&-x_{n+1}&0&\ldots&0&-x_{2n}\\
-x_{n+1}&\!\!x_2\!+\!x_{n+1}\!+\!x_{n+2}&-x_{n+2}&\ldots&0&0\\
0&-x_{n+2}&\!\!x_3\!+\!x_{n+2}\!+\!x_{n+3}&\ldots&0&0\\
0&  0 & -  x_{n+3}& &0&0\\
\vdots&\vdots&\vdots&\ddots&&\vdots\\
0&0&0&\ldots& -x_{2n-2}& 0 \\
0&0&0&\ldots& x_{n-1}\!+\!x_{2n-2}\!+\!x_{2n-1}&-x_{2n-1}\\
-x_{2n}&0&0&\ldots&-x_{2n-1}&\!\!x_n\!+\!x_{2n-1}\!+\!x_{2n}\end{array}\!\!\right)\ .$$

It defines a family of symmetric, positive-definite matrices for all $x_e>0.$ Changing the choice of homology basis for $H_1(W_n;{\mathbb Z})$ results in a different, but equivalent matrix $P^T \Lambda_{W_n} P$ for some $P \in \mathrm{GL}_n({\mathbb Z}).$

With the help of a computer[^1] one may check that $$\omega^5_{W_3} = -10 \frac{\Omega_{W_3}}{\det(\Lambda_{W_3})^2}\ ,$$ where we write $\Omega_G = \sum_{i=1}^{2n} (-1)^i x_i \mathrm{d}x_1  \wedge \ldots \wedge \widehat{\mathrm{d}x}_i\wedge  \ldots \wedge \mathrm{d}x_{2n}$. Two more examples of canonical wheel integrands were previously known [@BrSigma §10] (with a different sign convention), see Corollary 58 and Lemma 59 below: $$\omega^9_{W_5} = 18 \left( \frac{1}{\det(\Lambda_{W_5})^2} + 12 \,\frac{ x_6x_7x_8x_9x_{10}}{ \det(\Lambda_{W_5})^3} \right) \Omega_{W_5}\ ,$$ $$\omega^{13}_{W_7} = -26 \left( \frac{1}{\det(\Lambda_{W_7})^2} +60 \,\frac{ x_8x_9\ldots x_{14}}{ \det(\Lambda_{W_7})^3}
+360 \,\frac{ (x_8x_9\ldots x_{14})^2}{ \det(\Lambda_{W_7})^4}\right) \Omega_{W_7}$$ from which one notices that the integral is non-vanishing since the integrand is strictly positive or strictly negative on the region of integration. The canonical integral of the graph $W_3$ is $10$ times the Feynman residue of $W_3$ (see (IFeynWndef) below) which implies that $I_{W_3}(\omega^5) = 60 \zeta(3).$ The two computations above, via [@BorinskySchnetz] yielded $$I_{W_5}(\omega^9) = 1260 \, \zeta(5) \quad , \quad I_{W_7}(\omega^{13}) = 24024 \, \zeta(7)$$ which led to the conjectured form of the previous theorem. Note that these are not equal to the corresponding Feynman residues, since they have lower weight (for instance, for $W_5$ and $W_7$ the usual Feynman residues are proportional to $\zeta(7)$ and $\zeta(11)$, respectively).

## Applications to graph homology

Let $\mathcal{GC}_2$ be the commutative, even graph complex. By [@BrSigma Corollary 8.8], the non-vanishing of $I_{W_n}(\omega^{2n-1})$ immediately implies:

**Corollary 2**. *Let $n>1$ be odd. The wheel classes are non-zero in homology: $$0\neq [W_n]  \in H_{0}\left(\mathcal{GC}_2\right) \ .$$*

**Remark 3**. *This corollary was previously proved by Rossi-Willwacher [@RossiWillwacher] by computing a certain 'Kontsevich weight' associated to the wheel graphs. The value of the weight they obtain is proportional to the canonical integral above. This suggests that the canonical integrals may be related to the Rossi-Willwacher weights via a version of the Schwinger trick for Feynman integrals.*

Using the techniques of [@BrSigma] we may also deduce the existence of infinitely many non-zero classes $$\Xi_{m,n} \in H_{k_{m,n}} (\mathcal{GC}_2)$$ for all odd integers $1<m<n$, for some odd number $1 \leq k_{m,n} \leq 2m-3$, whose associated 'canonical integrals' with integrand $\omega^{2m-1} \wedge \omega^{2n-1}$ are a product of two odd zeta values $\zeta(m)\zeta(n)$, see Theorem 11 below. This result supports a conjecture made in [@BrSigma] which in particular implies the existence of an embedding of the graded exterior algebra on the canonical forms $\omega^{4k+1}$ into the cohomology of $\mathcal{GC}_2$.

  ------- ----- ---------------------------- ---------------------------- ---------------------------- ---------------------------- ---------------------------- ---------------------------- ---------------------------- ---------------------------- ----------------------------
   $H_8$                                                                                                                                                                                                                                                 $\color{blue}{\mathsf{0}}$
   $H_7$                                                                                                                                                                                                                    $\color{blue}{\mathsf{0}}$               1
   $H_6$                                                                                                                                                                                       $\color{blue}{\mathsf{0}}$               0                            0
   $H_5$                                                                                                                                                          $\color{blue}{\mathsf{0}}$               0                            0                            0
   $H_4$                                                                                                                             $\color{blue}{\mathsf{0}}$               0                            0                            0                            0
   $H_3$                                                                                                $\color{blue}{\mathsf{0}}$          $\Xi_{3,5}$                       0                       $\Xi_{3,7}$                       1                            2
   $H_2$                                                                   $\color{blue}{\mathsf{0}}$               0                            0                            0                            0                            0                            0
   $H_1$                                      $\color{blue}{\mathsf{0}}$               0                            0                            0                            0                            0                            0                            0
   $H_0$         $\color{blue}{\mathsf{0}}$                                            0                                                         0                                                    $\xi_{3,5}$                                               $\xi_{3,7}$
   $h_G$   $1$              $2$                          $3$                          $4$                          $5$                          $6$                          $7$                          $8$                          $9$                          $10$
  ------- ----- ---------------------------- ---------------------------- ---------------------------- ---------------------------- ---------------------------- ---------------------------- ---------------------------- ---------------------------- ----------------------------

  : A number indicates the dimension of $H_k(\mathcal{GC}_2)$ at low loop order obtained by computer [@GraphComplexComputations]. All entries above the blue line of zeros necessarily vanish. All named entries (such as '$W_n$') indicate a one-dimensional vector space, generated by the named element. In this range, the location of some of the new classes $\Xi_{m,n}$ can be pinned down exactly. If we furthermore assume that $H_1(\mathcal{GC}_2)$ vanishes at $h_G=11$ (or more weakly, that the images $\delta \xi_{5,7}$, $\delta \xi_{3,9}$ of homology classes denoted by $\xi_{5,7}$ and $\xi_{3,9}$ in $h_G=12$ under the edge deletion differential $\delta$ vanish), then we can also deduce that the two dimensional space $H_3(\mathcal{GC}_2)$ at $h_G=10$ in the right-most column is spanned by $\Xi_{5,7}$ and $\Xi_{3,9}$.

[]{#table:knownresults label="table:knownresults"}

Recent results of Chan, Galatius and Payne [@CGP] imply that the top weight cohomology of the moduli stack $\mathcal{M}_g$ of curves of genus $g$ is computed by the homology of the graph complex $\mathcal{GC}_2$ for $h_G=g.$ Thus the existence of the classes above give rise to top-weight classes in the cohomology of $\mathcal{M}_g$.

## Homology of $\mathrm{GL}_n({\mathbb Z})$.

Let $\mathcal{P}_n$ denote the space of positive-definite real symmetric $n\times n$ matrices. It has a right action $$\begin{aligned}
\mathcal{P}_n \times \mathrm{GL}_n({\mathbb Z}) & \longrightarrow& \mathcal{P}_n \nonumber  \\
X. P & \mapsto & P^T X P  \ . \nonumber
\end{aligned}$$ Now let $n>1$ be odd and consider the region $\tau_{W_n} \subset \mathcal{P}_n$ defined by: $$\tau_{W_n} = \{ \Lambda_{W_n} (x_e) :  x_e >0 \} \ .$$ It consists of the subspace of symmetric positive-definite matrices of banded form as depicted in (introLambdaW). Its diagonal elements are positive, off-diagonals are negative, and all row and column sums are positive.

**Theorem 4**. *Let $H^{\mathrm{lf}}$ denote locally finite, or Borel-Moore, homology (which is dual to compactly supported cohomology). Let $n>1$ be odd.*

*(i) The region $\tau_{W_n}$ defines a closed, locally finite chain which is non-zero in homology: $$\label{tauWinlf} [\tau_{W_n}]  \ \in \   H^{\mathrm{lf}}_{2n} \left( \mathcal{P}_{n}/\mathrm{GL}_{n}({\mathbb Z})\right) \ .$$*

*(ii) Its inflation $\mathrm{ifl}(\tau_{W_n})$ defined in [@TopWeightAg], is a closed locally finite chain which is non-zero in homology: $$\label{inflationClasses} [\mathrm{ifl}(\tau_{W_n})]  \ \in \   H^{\mathrm{lf}}_{2n+1} \left( \mathcal{P}_{n+1}/\mathrm{GL}_{n+1}({\mathbb Z})\right) \ .$$*

A conjecture of Church-Farb-Putman [@ChurchFarbPutman] implies that if $n$ is even, then $H^{\mathrm{lf}}_{k} \left( \mathcal{P}_{n}/\mathrm{GL}_{n}({\mathbb Z})\right)$ should vanish for $k\leq  2n-2 .$[^2] The theorem above provides an explicit non-vanishing class (inflationClasses) in degree $k=2n-1$. Some of these classes have recently been constructed by Ash [@AshSharblies] via a completely different method.

<figure id="fig:2">
<p><span class="math display">$$\begin{array}{c|cccccccccccccccccc}
n    &amp;
 \\ \hline
2  &amp;         \\
 3 &amp;  \color{red}{H^{\mathrm{lf}}_6} \quad    \\
 4 &amp;   \quad \color{blue}{H^{\mathrm{lf}}_7}    \\
 5 &amp;   &amp; &amp; \color{red}{H^{\mathrm{lf}}_{10}}  \quad   &amp; &amp; &amp;   H^{\mathrm{lf}}_{15} \quad   \\
 6 &amp;    &amp; &amp;  \quad \color{blue}{H^{\mathrm{lf}}_{11}} &amp; H^{\mathrm{lf}}_{12} \quad  &amp; &amp;\quad  H^{\mathrm{lf}}_{16}  \\
 7 &amp;   &amp; &amp;   &amp;  \quad  H^{\mathrm{lf}}_{13} &amp; \color{red}{H^{\mathrm{lf}}_{14}} &amp;&amp;&amp; &amp;   H^{\mathrm{lf}}_{19} &amp; &amp; H^{\mathrm{lf}}_{23} &amp; &amp;&amp; H^{\mathrm{lf}}_{28}  \\
\end{array}$$</span></p>
<figcaption>Locally-finite homology of <span class="math inline">𝒫<sub><em>n</em></sub>/GL<sub><em>n</em></sub>(ℤ)</span> in the known ranges <span class="citation" data-cites="SouleSL3 LeeSzczarba ElbazVincentGanglSoule"></span>. See also <span class="citation" data-cites="GL8"></span> for some partial results for <span class="math inline"><em>n</em> = 8</span>. An entry <span class="math inline"><em>H</em><sub><em>i</em></sub><sup>lf</sup></span> in the table indicates that <span class="math inline"><em>H</em><sub><em>i</em></sub><sup>lf</sup>(𝒫<sub><em>n</em></sub>/GL<sub><em>n</em></sub>(ℤ);ℝ)</span> is non-zero and of dimension <span class="math inline">1</span>. The classes in red are spanned by <span class="math inline"><em>τ</em><sub><em>W</em><sub>3</sub></sub>, <em>τ</em><sub><em>W</em><sub>5</sub></sub>, <em>τ</em><sub><em>W</em><sub>7</sub></sub>, …</span>; the classes indicated in blue are their images under inflation. </figcaption>
</figure>

By a theorem of [@AlexeevBrunyate; @MeloViviani] the cell $\tau_{W_n}$ is the Voronoi cell associated to a positive-definite quadratic form. Indeed, it is an interesting exercise to check that the quadratic form $$Q_n (z_1,\ldots, z_n)= (z_1+\ldots + z_n)^2 + \sum_{i\in {\mathbb Z}/n{\mathbb Z}} \left(z_i^2 + (z_i+z_{i+1})^2\right)$$ has $4n$ non-zero minimal vectors $\pm{\underline{e}}_i$ and $\pm ({\underline{e}}_i-{\underline{e}}_{i+1})$ where $i\in {\mathbb Z}/n{\mathbb Z}$ and ${\underline{e}}_i=(0,\ldots, 0, 1, 0,\ldots, 0)$ has a single $1$ in the $i^{\mathrm{th}}$ slot. These minimal vectors have length $4$ with respect to the norm $Q_n$, and hence the associated Voronoi cell, which is the convex hull of the set of symmetric matrices $\xi\xi^T$, where $\xi$ ranges over the set of such minimal vectors of $Q_n$, is precisely $\tau_{W_n}$.

**Corollary 5**. *The infinite families (tauWinlf) and (inflationClasses) of classes in the locally finite homology of the general linear group constructed above may be represented by a single cographical cone.*

We are not aware of any other classes with this property.

**Remark 6**. *It is reasonable to expect that the class in $H_{15}^{\mathrm{lf}}(\mathcal{P}_5/\mathrm{GL}_5({\mathbb Z}))$, which is known by [@brown2023bordifications] to pair non-trivially with the class of the form $\omega^5 \wedge \omega^9$ (denoted by $[\omega^5 \wedge \omega_c^9]$ in *loc. cit.*) can be related to the class $\Xi_{3,5}$ in the graph complex by application of Stokes theorem [@BrSigma Theorem 8.5]. We expect that $\Xi_{3,7}$ and the class in $H_{19}^{\mathrm{lf}}(\mathcal{P}_7/\mathrm{GL}_7({\mathbb Z}))$ depicted in Figure 2 are related in a similar way.*

When $n$ is odd, the orbifold $\mathcal{P}_n /\mathrm{GL}_n({\mathbb Z})$ is orientable, and Poincaré duality implies that: $$H^{\mathrm{lf}}_k(\mathcal{P}_n /\mathrm{GL}_n({\mathbb Z});{\mathbb R}) = H_{d_n- k} (\mathcal{P}_n /\mathrm{GL}_n({\mathbb Z});{\mathbb R})^{\vee} = H_{d_n- k} (\mathrm{GL}_n({\mathbb Z});{\mathbb R})^{\vee}$$ where $d_n = \frac{n(n+1)}{2}$ is the dimension of $\mathcal{P}_n$.

## Homology of the moduli spaces of tropical curves and abelian varieties

Let $\mathcal{M}^{\mathrm{trop}}_g$ denote the moduli space of tropical curves of genus $g$. Denote its link by $L\mathcal{M}^{\mathrm{trop}}_g$, which is obtained by gluing together quotients of simplices $\sigma_G/\mathrm{Aut}(G)$ along common faces, where $G$ ranges over all stable vertex-weighted graphs of genus $g$. In particular, there is a natural continuous map $$i: \sigma_{W_n} \longrightarrow L\mathcal{M}_{n}^{\mathrm{trop}}$$ for all odd $n>1$. Let $\partial L\mathcal{M}_n^{\mathrm{trop}} \subset L\mathcal{M}_n^{\mathrm{trop}}$ denote the subspace generated by graphs with at least one vertex of weight $>0$. An equivalent formulation of Corollary 2 is that $$[i \sigma_{W_n} ] \ \in \  H_{2n-1} ( L\mathcal{M}_n^{\mathrm{trop}}, \partial  L\mathcal{M}_n^{\mathrm{trop}} )$$ is non-zero for all $n>1$ odd, since the relative homology group is computed by the graph complex. However, it is easy to show, since the wheel is built out of triangles, that the image of $\sigma_{W_n}$ has no boundary. Thus we have:

**Corollary 7**. *The image $i \sigma_{W_n}$ in $L\mathcal{M}_n^{\mathrm{trop}}$ is a closed chain whose homology class is non-zero: $$0 \neq  [i \sigma_{W_n}] \ \in \ H_{2n-1}( L\mathcal{M}_n^{\mathrm{trop}})  \ .$$*

Now consider $\mathcal{A}^{\mathrm{trop}}_g$, the moduli space of tropical abelian varieties in genus $g$, and let $L\mathcal{A}_g^{\mathrm{trop}}$ denote its link. As a set, the former is in bijection with $\mathcal{P}^{\mathrm{rt}}_g/\mathrm{GL}_g({\mathbb Z})$ where $\mathcal{P}^{\mathrm{rt}}_g$ is the rational closure of $\mathcal{P}_g$, which consists of positive semi-definite matrices with rational kernel. The boundary $\partial \mathcal{A}^{\mathrm{trop}}_g$ is the image of $\mathcal{P}_g^{\mathrm{rt}}\setminus \mathcal{P}_g$, consisting of matrices with vanishing determinant, modulo $\mathrm{GL}_g({\mathbb Z})$. Thus one has $$\mathcal{A}_g^{\mathrm{trop}} \setminus \partial \mathcal{A}_g^{\mathrm{trop}}   \cong   \mathcal{P}_g / \mathrm{GL}_g({\mathbb Z})\ .$$ The link $L\mathcal{A}_g^{\mathrm{trop}}$ of $\mathcal{A}_g^{\mathrm{trop}}$ is canonically identified, as a set, with ${\mathbb R}_{>0}^{\times} \setminus \left(\mathcal{P}^{\mathrm{rt}}_g \setminus \{0\}\right)/\mathrm{GL}_g({\mathbb Z})$.

The tropical Torelli map [@Nagnibeda; @Baker; @CaporasoViviani; @MikhalinZharkov; @BMV] is a continuous map $$\label{intro: TropTorelli}  \lambda:  \mathcal{M}_g^{\mathrm{trop}} \longrightarrow\mathcal{A}_g^{\mathrm{trop}}$$ which, to a stable weighted metric graph associates the class of any graph Laplacian matrix. It restricts to a map $\mathcal{M}_g^{\mathrm{red},\mathrm{trop}} \rightarrow \mathcal{A}_g^{\mathrm{trop}}$ on the locus $\mathcal{M}_g^{\mathrm{red},\mathrm{trop}}  \subset  \mathcal{M}_g^{\mathrm{trop}}$ spanned by 3-connected graphs and passes to a map between their links, denoted by the same symbol $\lambda: L\mathcal{M}_g^{\mathrm{red}, \mathrm{trop}} \rightarrow L\mathcal{A}_g^{\mathrm{trop}}$. The wheel graphs (and all their quotients) are 3-connected, and hence $i\sigma_{W_n} \subset L\mathcal{M}_n^{\mathrm{red}, \mathrm{trop}}$.

**Theorem 8**. *For all odd $n>1$, the image of the wheel cycle $\lambda i\sigma_{W_n}$ defines a closed chain in $L\mathcal{A}_n^{\mathrm{trop}}$ whose homology class is non-zero: $$0  \ \neq \  [   \lambda  i  \sigma_{W_n}  ]  \  \in \  H_{2n-1} \left(   L\mathcal{A}_n^{\mathrm{trop}}\right)  \ .$$ It pairs non-trivially with the class $[\omega_c^{2n-1} ] \in H_ {\mathrm{dR}}^{2n-1} \left(L\mathcal{A}_n^{\mathrm{trop}} \right)$ defined in [@brown2023bordifications] to give the canonical integral $I_{W_n}(\omega^{2n-1})$ (wheelseq).*

It was shown in [@TopWeightAg; @OdakaOshima] that the top weight cohomology of $\mathcal{A}_g$ is computed by the homology of $L\mathcal{A}_g^{\mathrm{trop}}.$ Thus the previous theorem gives rise to a family of top-weight classes in $L\mathcal{A}_g^{\mathrm{trop}}$. A very interesting question is whether the periods $I_{W_n}(\omega^{2n-1})$ are the periods of extension classes in the cohomology of $\mathcal{A}_g$, as seems to be the case for $g=3$. Indeed, Hain proved in [@Hain3folds], using results of [@Looijenga], that the class in $\mathrm{gr}^W_6 H^6 (\mathcal{A}_3)$ sits in a non-trivial extension of ${\mathbb Q}(-3)$ by ${\mathbb Q}(0)$.

## Wheel motives and periods

The wheel motives were defined in [@BEK]. For any finite connected graph, let us denote the graph polynomial by $$\label{intro: psiGdef}\Psi_{G} (x_e) = \det \Lambda_{G} \  \in \  {\mathbb Z}[x_e, e\in E_G] \ .$$ It is also known as the first Symanzik or Kirchhoff polynomial. The graph hypersurface $X_G \subset {\mathbb P}^{E_G}$ is defined to be its zero locus in projective space. There exists a canonical 'wonderful' compactification $$\pi_G: P^G \longrightarrow{\mathbb P}^{E_G}$$ obtained by blowing up certain linear subspaces of ${\mathbb P}^{E_G}$ which are contained in $X_G$, in increasing order of dimension. Let $Y_G \subset P^G$ denote the strict transform of $X_G$, and let $B \subset P^G$ denote the total transform of the coordinate hyperplanes $x_e=0$ in ${\mathbb P}^{E_G}$. Then $B$ is a simple normal crossings divisor and the graph 'motive' is defined to be the object $$\mathrm{mot}_G = H^{|E_G|-1} \left(P^G \setminus Y_G , B \setminus (B \cap Y_G)  \right)$$ in a suitable abelian category of (realisations of) motives. It was shown in [@BEK] that if $\widetilde{\sigma}_G$ denotes the topological closure of $\pi_G^{-1}(\overset{\circ}{\sigma}_G)$ inside $P_G({\mathbb R})$ then $\widetilde{\sigma}_G$ does not meet $Y_G.$ Thus in particular it defines a relative homology class $$[\widetilde{\sigma}_G] \  \in  (\mathrm{mot}_G^B)^{\vee}=  H_{|E_G|-1} \left(P^G \setminus  Y_G({\mathbb C}) , B \setminus  (B \cap Y_G)  ({\mathbb C}) \right) \  .$$ Theorem 1 is deduced by first proving Formula (intro: omegaformula) in the following theorem.

**Theorem 9**. *Let $n>1$ be odd. The canonical form $\omega^{2n-1}_{\Lambda_{W_n}}$ defines a non-vanishing cohomology class $$[\omega^{2n-1}_{W_n} ]  \ \in \    \mathrm{mot}_{W_n}^ {\mathrm{dR}} =H_ {\mathrm{dR}}^{2n-1} \left(P^{W_n} \setminus Y_{W_n} , B \setminus (B \cap Y_{W_n})  \right)$$ which pairs non-trivially with $[\widetilde{\sigma}_{W_n}]$ to give the integral (wheelseq). We may write the form explicitly as $$\label{intro: omegaformula} \omega^{2n-1}_{W_n} =  \sum^{\frac{n-3}{2}}_{k=0}   c_k    \left(\frac{x_{n+1}\ldots x_{2n}}{\Psi_{W_n}}\right)^k \frac{\Omega_{2n}}{\Psi^2_{W_n}}\ ,$$ where $x_{n+1},\ldots, x_{2n}$ are the edge variables associated to the $n$ spokes of $W_n$, $\Omega_{2n}$ is the differential form $\sum_{i=1}^{2n} (-1)^i x_i \mathrm{d}x_1 \wedge \ldots \wedge  \widehat{\mathrm{d}x_i} \wedge \ldots \wedge \mathrm{d}x_{2n}$, and the coefficients $c_k=(-1)^{(n-1)/2}(2n-1)2^{k+1}c_{n-1,k+1}$ are given explicitly in (ceq1).*

## Computations of canonical integrals for other graphs

Using the formulae derived in this paper, we were able to calculate the canonical forms (intro:omegandef) $$\omega^{|E_G|-1}_G = \mathrm{tr}\,( (\Lambda_G^{-1} \mathrm{d}\Lambda_G )^{|E_G|-1})$$ for all graphs $G$ with $h_G\leq7$ independent cycles. It was shown in [@BrSigma] that $\omega_G^{|E_G|-1}$ vanishes unless $|E_G| = 2h_G$ and $h_G$ is odd. The graphs were generated using `nauty` [@NAUTY].

All calculations were performed using the computer algebra system Maple. The actual integration is based on algorithms which are contained in the Maple package `HyperlogProcedures` [@hlog][^3]

For $h_G\leq5$ only three non-zero canonical integrals exist, and were computed in [@BrSigma]: $$I_{W_3}(\omega^5)=60\zeta(3),\qquad I_{W_5}(\omega^9)=1260\zeta(5),\qquad I_{Z_5}(\omega^9)=630\zeta(5),$$ where $Z_n$ denotes the (closed) zig-zag graph with $n$ independent cycles.

For graphs $G$ with seven independent cycles, we used Formula ((formula2)) below to compute the associated invariant forms $\omega^{13}_G$. The non-zero cases involve a number of monomials which ranges between 3 (for $W_7$) and 61942. We were able to calculate the invariant integrals analytically for the subset of all *constructible* graphs, of which there are 37. This class of graphs was defined in [@schnetz2014graphical; @BorinskySchnetz] and has period integrals (or graphical functions) which are easier to compute than the general case. The results for the 37 constructible canonical integrals with $h_G=7$ independent cycles are $$\label{IGAnsatz}
I_G = N(G)\,3003\zeta(7)\qquad\text{with}\qquad N(G)\in\{0,1,2,3,4,6,8\}.$$ In particular, $I_{Z_7}(\omega^{13})=9009\zeta(7).$ Assuming that a similar pattern continues for non-constructible graphs, we ran numerical evaluations of the remaining canonical integrals using M. Borinsky's tropical Monte-Carlo method [@BorinskyTMCQ], and obtained numerical confirmations of the ansatz (IGAnsatz) with half-integer values of $N(G)$ for all graphs $G$ with $h_G=7.$ In total we found 56 non-zero canonical integrals with frequencies listed in Table 2. Note that $W_7$ is the only graph with $N(G)=8$. The only graph with $N(G)=6$ is the closed graph in Figure 3. It too forms part of an infinite family.

  -------------- ------- ----- ------- ----- ------- ----- ----- ----- -----
  $N(G)$          $1/2$   $1$   $3/2$   $2$   $5/2$   $3$   $4$   $6$   $8$
  \# of graphs      8     20      6      8      1      8     3     1     1
  -------------- ------- ----- ------- ----- ------- ----- ----- ----- -----

  : Invariant integrals of graphs with seven independent cycles. Some integrals are obtained by an exact numerical method.

<figure id="fig1">
<div class="center">

</div>
<figcaption>The closed graph with <span class="math inline"><em>I</em><sub><em>G</em></sub>(<em>ω</em><sup>13</sup>) = 18018<em>ζ</em>(7)</span>.</figcaption>
</figure>

A list of all graphs up to seven loops with their canonical integrals is included in `HyperlogProcedures`.

For $h_G\geq9$ one would need optimizations to calculate all the invariant forms. We do not expect that the general picture is significantly different for $h_G=9$, although the existence of multiple zeta values in weight $11$ and depth 3 suggests that more interesting canonical integrals might arise for $h_G=11$. A conjecture due to Panzer and Portner [@Portner Conjecture 1.2] states that the canonical integrals of primitive forms $\omega^{4k+1}$ are equal to suitably normalised Rossi-Willwacher integrals. The latter are single-valued multiple zeta values, which follows from their definition and [@BrownDupont; @SchlottererSchnetz; @VanhoveZerbini; @BanksPanzerPym].

**Remark 10**. *The canonical primitive forms $\omega^{4k+1}_G$ vanish unless $|E_G| =2 h_G =4k+2$, which corresponds to homological degree $0$ in the graph complex $\mathcal{GC}_2$. By Willwacher [@WillwacherGRT], $H_0(\mathcal{GC}_2)$ is isomorphic to the dual of the Grothendieck-Teichmüller Lie algebra $\mathfrak{grt}$, which admits a map from the motivic Lie algebra $\mathfrak{g}^{\mathfrak{m}} \rightarrow  \mathfrak{grt}$. It is injective [@BrMTZ], as conjectured by Deligne [@deligneP1]. The motivic Lie algebra $\mathfrak{g}^{\mathfrak{m}}$ is isomorphic to the free Lie algebra with one generator in every odd degree $\geq 3$. A question of Drinfeld [@Drinfeld] asks whether $\mathfrak{g}^{\mathfrak{m}}\rightarrow \mathfrak{grt}$ is surjective. If so, then this would imply that every closed and primitive element in $H_0(\mathcal{GC}_2)$ is proportional to a wheel class. This would suggest the following consequence for canonical integrals: if $X \in \mathcal{GC}_2$ is closed with $4k+2$ edges and $2k+1$ loops where $k\geq 1$, and the homology class $[X]$ is primitive, then $I_X(\omega^{4k+1})  \in  {\mathbb Q}\zeta(2k+1).$*

*For completely general canonical integrals of exterior products of forms $\omega^{4k+1}$ over domains $\sigma_G$, an optimistic scenario along the lines of [@BrSigma §9.5], is that they are periods of mixed Tate motives over ${\mathbb Z}$. This is certainly consistent with all the current evidence. However, [@BelkaleBrosnan] and the modular counter-examples of [@BrownSchnetz] provide evidence of Feynman residues which are [not] multiple zeta values, and so it is also possible that canonical integrals are just as complicated. The number-theoretic nature of canonical integrals, therefore, is an open question and an interesting topic for further investigation.*

## Strategy of proof of Theorem 1 and contents

Section 2 discusses further applications of Theorem 1 and questions for future research. It contains the proofs of theorems 4 and 8, as well as a discussion on graph homology, wheel motives, and the subtle relationship between the canonical wheel integrals and the Borel regulator.

The rest of the paper, starting in Section 3.1, is concerned with computing the invariant differential forms $$\omega_{\Lambda_G}^{4k+1} = \mathrm{tr}\,\left( (\Lambda_G^{-1} \mathrm{d}\Lambda_G)^{4k+1} \right)\ ,$$ where $G$ is a graph with $4k+2$ edges and $2k+1$ loops, and hence $\Lambda_G$ is $(2k+1)\times (2k+1)$ symmetric matrix whose entries are linear forms in the variables $x_e$ for $e\in E_G$. It turns out that this problem is surprisingly complicated, but very highly structured. Part of the difficulty is the total absence of theorems for working with matrices whose entries anti-commute, and so we are obliged to use linear algebra concepts (determinants, permanents, *etc*) which have historically been developed for studying matrices with *commuting* entries, but whose non-commuting analogues do not yet seem to have been studied (we hope that the results in this paper are a useful first step in this direction).

The strategy of this paper, starting from Section 3, is to solve a more general problem concerning matrices whose entries are 1-forms, and proceed by successive specialisation. Every specialisation produces additional structure which can be exploited at each stage.

1.  First of all, we let $B=(b_{ij})_{1\leq i, j\leq n}$ be an $n\times n$ matrix with generic entries, and $\Omega= (\omega_{ij})_{1\leq i, j\leq n}$ an $n\times n$ matrix whose entries are generic one-forms. One can prove that since $(B \Omega)^{2n}$ vanishes identically, the matrix $(B \Omega)^{k}$ in the maximal non-vanishing degree $k=2n-1$ has additional structure; for example one sees immediately that all its entries must be divisible by $\det(B)$. The first goal in Section 3 is to explain the terms which go into the formula: $$(B \Omega)^{2n-1}  = \det(B) \sum_{\nu} \Phi_{\nu}(B) \omega_{\nu}$$ and illustrate them with examples. The formula itself is proven in Section 9 since its proof is somewhat technical, but may be of independent interest. The terms $\omega_{\nu}$ are $2n-1$ forms obtained as exterior products of entries of $\Omega$; the terms $\Phi_{\nu}(B)$ are matrices whose entries are certain polynomials in the entries of $B$ which are the permanents of certain additional auxiliary matrices constructed out of $B$. Our formula for $(B\Omega)^{2n-1}$ implies a general formula for the anti-symmetrisation of a product of $2n-1$ matrices of rank $n$ which is proven in the Appendix, and extends the classical Amitsur-Levitzki theorem. It too may be of independent interest.

2.  The second reduction is to assume that $B$ and $\Omega$ are generic *symmetric*. This induces cancellations between the permanents in our formula for the trace of $(B\Omega)^{2n-1}$. The passage to the symmetric case is discussed in Section 5, and the main result is Theorem 44. This is the first point at which our formulae cease to be fully general: Theorem 44 only concerns components of a particular (diagonal) type, but we expect that the general case can be derived similarly. The main simplification at this step occurs by applying a crucial identity which expresses a signed linear combination of permanents as a combination of *determinants*. This enables us to replace all permanents in our formula with determinants in the symmetric case. The key identity is explained in Section 4, Theorem 40, and may be of independent interest. Its proof is given in Section 10. Our first proof was representation-theoretic, but we settled for a recursive proof since it is ultimately shorter.

3.  The next step, which is the most straightforward, is to specialise further to the case when $B= A^{-1}$ and $\Omega =\mathrm{d}A$, for $A$ a generic invertible $n\times n$ symmetric matrix. This is done in Section 6. A key point is that since our formula at the previous step only involves determinants of minors of $B$, they can be efficiently related to determinants of minors of $A$ by an identity due to Jacobi (Lemma 48). This leads to a formula for the 'leading terms' of $\omega^{2n-1}_{A}$ which only involves the matrix $A$, and not its inverse (Theorem 49). Section 7 specialises to the case when $A= \Lambda_G$ is a Laplacian matrix. Theorem 50 provides a fully general and efficient formula for the canonical integrand associated to a graph which only involves determinants of minors of its graph Laplacian matrix.

4.  The final step, in Section 8, is to consider the specific case when $G=W_{n}$ is the wheel with $n$ spokes, which reduces the canonical integral to an explicit linear combination of Feynman periods. The formula for the integrand of the canonical wheel integrals is given in Corollary 58 and involves certain coefficients given in (ceq1). This formula already proves that the canonical integral is positive which suffices for most of the applications in the introduction. The actual wheel integrals are finally computed in the remainder of this section using results on graphical functions from [@BorinskySchnetz].

## Acknowledgements

Francis Brown thanks Trinity College, Dublin for a Simons visiting Professorship during which much of this work was carried out, the University of Geneva, where it was completed, and M. Chan, S. Galatius, S. Grushevsky and S. Payne for discussions on the moduli space of tropical abelian varieties. Both authors thank Michael Borinsky, Erik Panzer, Peter Patzt and Thomas Willwacher for helpful feedback. This project has received funding from the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation programme (grant agreement no. 724638).

# Further geometric applications and their proofs {#sect: Consequences}

We now describe in further detail some of the consequences of Theorem 1.

## Graph homology

In [@BrSigma], the non-vanishing of the wheel integrals for $W_3, W_5$ was used to deduce the existence of a non-trivial class $\Xi_{3,5}$ in the homology of the graph complex $\mathcal{GC}_2$ (or equivalently, $\mathcal{GC}_0$). In view of Theorem 1, this argument may now be generalised to all orders.

**Theorem 11**. *For all odd integers $3\leq m<n$, there exists a linear combination of oriented graphs in the commutative even graph complex with edge degree $2(m+n)-1$, denoted by: $$\Xi_{m,n} \in \mathcal{GC}_0\ ,$$ which is closed, i.e. $\mathrm{d}\ \Xi_{m,n} =0$, and whose canonical integral satisfies $$I_{\Xi_{m,n}}(\omega^{2m-1}\wedge \omega^{2n-1})=\int_{\sigma_{\Xi_{m,n}}} \omega^{2m-1} \wedge \omega^{2n-1} = \zeta(m) \zeta(n)\ .$$ It defines a non-trivial element in graph homology $$0 \neq [\Xi_{m,n} ] \ \in \  H_{2(m+n)-1}  (\mathcal{GC}_0)\ .$$ Equivalently, it defines a non-zero class in $[\Xi_{m,n} ]  \in  H_{k}  (\mathcal{GC}_2)$ in some (unknown) odd degree $k>0$.*

*Proof.* By Willwacher [@WillwacherGRT], the zeroth cohomology of the graph complex $\mathcal{GC}_2$ is isomorphic to the Grothendieck-Teichmüller Lie algebra, which, by [@BrMTZ] contains the free graded Lie algebra generated by one element $\sigma_{2k+1}$ in degree $-(2k+1)$ for every $k\geq 1$. By Rossi-Willwacher [@RossiWillwacher], the element $\sigma_{2k+1}$ pairs non-trivially with the wheel homology class $W_{2k+1}$. We deduce the existence of a closed element $\xi_{m,n} \in \mathcal{GC}_2$ in degree zero, which is dual to $[\sigma_m, \sigma_n]$ and whose reduced coproduct satisfies $\Delta'  [\xi_{m,n}] =[W_m] \otimes [W_n] - [W_n] \otimes [W_m]$ in graph homology. The argument now proceeds as in [@BrSigma Section 10.3]. First, by applying the Stokes formula of [@BrSigma §8], we deduce from Theorem 1 that $$\int_{\delta  \xi_{m,n}} \omega^{2m-1} \wedge \omega^{2n-1} = 2 \int_{W_m} \omega^{2m-1} \int_{W_n} \omega^{2n-1}   \ \in  \  {\mathbb Q}^{\times}  \zeta(m)\zeta(n)\ ,$$ where $\delta$ denotes the 'second differential' in the graph complex [@SpectralSequenceGC2] (and arises as a component of $\Delta'$). Repeated application of Stokes' formula using Corollary 8.10 of [@BrSigma] produces a sequence of elements in the graph complex which terminates with a non-trivial homology class $\Xi_{m,n}$ whose canonical integral is in ${\mathbb Q}^{\times}  \zeta(m)\zeta(n)$. The element $\Xi_{m,n}$ may be normalised so that its canonical integral is as stated. Since it has edge degree $2(n+m)-1$ it may be viewed as a non-zero homology class in $\mathcal{GC}_0$ in that degree. The degree of $[\Xi_{m,n}]$ in $\mathcal{GC}_2$ is given by $k=2(m+n)-1-2g$, where $g$ is its loop number (genus). It follows that $k$ is odd. ◻

**Remark 12**. *This argument is closely related to the 'waterfall' spectral sequence of [@SpectralSequenceGC2] but contains the additional information about the value of the canonical period integral. There is some limited control on the genus (loop number) in which the class $\Xi_{m,n}$ lies. Indeed, the vanishing of the forms $\omega^{2m-1}, \omega^{2n-1}$ provide a lower bound: the class $\Xi_{m,n}$ must occur in genus $g$ where $g$ satisfies $\mathrm{max}\{m,n\}+1  \leq g \leq m+n-1$ by [@BrSigma Lemma 8.4], i.e., strictly to the right of both $W_m$ and $W_n$ in Table 1. Equivalently, $[\Xi_{m,n}]\in H_k(\mathcal{GC}_2)$ where $1\leq k \leq 2 \min \{m,n\}-3$ is odd.*

The theorem provides infinitely many classes of odd degree in the homology of $\mathcal{GC}_2$ which can also be deduced from [@SpectralSequenceGC2]. By [@CGP], each one provides an odd degree class in the cohomology of a moduli stack of curves $\mathcal{M}_g$.

## Homology of $\mathrm{GL}_n({\mathbb Z})$: Theorems 4 and 8

### Proof of Theorem 4(i)

There is a canonical isomorphism which identifies the reduced homology of the genus $g$ component of the graph complex $\mathcal{GC}^{(g)}_0$ with the relative homology of the link $L\mathcal{M}^{\mathrm{trop}}_g$: $$\widetilde{H_{\bullet}} (\mathcal{GC}^{(g)}_0)   \cong  H_{\bullet-1} (L\mathcal{M}_g^{\mathrm{trop}}, \partial L\mathcal{M}_g^{\mathrm{trop}}  ) \ .$$ It associates to an oriented stable graph $G$ with $h_G=g$ the image of the oriented projective simplex $\sigma_G$. The link $\lambda:  L\mathcal{M}_g^{\mathrm{red},\mathrm{trop}} \rightarrow  L\mathcal{A}_g^{\mathrm{trop}}$ of the restriction of the tropical Torelli map (intro: TropTorelli) induces a map on homology: $$\lambda:  H_{\bullet} (L\mathcal{M}_g^{\mathrm{red},\mathrm{trop}}, \partial L\mathcal{M}_g^{\mathrm{red}, \mathrm{trop}}  ) \longrightarrow H_{\bullet} (L\mathcal{A}_g^{\mathrm{trop}}, \partial L\mathcal{A}_g^{\mathrm{trop}}  )   \cong H^{\mathrm{lf}}_{\bullet} (L\mathcal{A}_g^{\circ, \mathrm{trop}} )  \ .$$ The open $L\mathcal{A}_g^{\circ, \mathrm{trop}}=  L\mathcal{A}_g^{\mathrm{trop}}\setminus   \partial L\mathcal{A}_g^{\mathrm{trop}}$ may be canonically identified with the space ${\mathbb R}^{\times}_{>0} \setminus \mathcal{P}_g /\mathrm{GL}_g({\mathbb Z})$. Since for all odd $n>1$ the wheel $W_n$ is closed in the homology of the graph complex and is 3-connected, we deduce that the link of the image $\tau_{W_n}$ of the corresponding chain in $\mathcal{P}^{\mathrm{rt}}_n /\mathrm{GL}_n({\mathbb Z})$, which equals $\lambda i \sigma_{W_n}$, is closed and hence defines a homology class: $$[ L  \tau_{W_n} ]   \  \in  \   H^{\mathrm{lf}}_{\bullet} ({\mathbb R}^{\times}_{>0} \setminus \mathcal{P}_n /\mathrm{GL}_n({\mathbb Z}))\ .$$ By [@brown2023bordifications], the canonical form $\omega^{2n-1}$ defines a relative cohomology class $$[(\omega^{2n-1},0)] \in   H_{\mathrm{dR}}^{2n-1} \left(L\mathcal{A}_n^{\mathrm{trop}}, \partial L\mathcal{A}_n^{\mathrm{trop}} \right)$$ which has a compactly supported representative $\omega_c^{2n-1}$ of $\omega^{2n-1}$ on ${\mathbb R}^{\times}_{>0} \setminus \mathcal{P}_n /\mathrm{GL}_n({\mathbb Z})$. By Theorem 1 it pairs non-trivially with $\sigma_{W_n}$, which proves, via the de Rham theorem of [@brown2023bordifications] for relative (co)homology, that both $[L\tau_{W_n}] \in  H_{2n-1} (L\mathcal{A}_n^{\mathrm{trop}}, \partial L\mathcal{A}_n^{\mathrm{trop}}  )$ and $[\omega_c^{2n-1}] \in H^{2n-1}_c({\mathbb R}^{\times}_{>0} \setminus \mathcal{P}_n /\mathrm{GL}_n({\mathbb Z}))$ are non-zero. The latter fact was already established in *loc. cit.* by different means. Since $\mathcal{P}_n /\mathrm{GL}_n({\mathbb Z})$ is an ${\mathbb R}^{\times}_{>0}$ fibration over ${\mathbb R}^{\times}_{>0} \setminus \mathcal{P}_n /\mathrm{GL}_n({\mathbb Z})$ and $H_c^{1}({\mathbb R}^{\times}_{>0}) \cong {\mathbb R}$ and vanishes in all other degrees, we deduce that $[\tau_{W_n}]$ is non-vanishing in $H^{2n}_c(\mathcal{P}_n /\mathrm{GL}_n({\mathbb Z})) \cong      H^{2n-1}_c({\mathbb R}^{\times}_{>0} \setminus \mathcal{P}_n /\mathrm{GL}_n({\mathbb Z}))$.

### Proof of Theorem 8

Theorem 8 may be proved by a similar method. The cellular homology of $L\mathcal{M}_g^{\mathrm{red}, \mathrm{trop}}$ is computed by a variant of the graph complex, which we shall denote by $\mathcal{GC}'_0$, in which one considers only 3-connected graphs, and tadpole graphs are not quotiented out. Since the wheel graphs have the property that every edge lies in a triangle, they are already closed in the complex $\mathcal{GC}'_0.$ It follows that the cell $i \sigma_{W_n}$ associated to the wheel graph defines a closed cycle of degree $2n-1$ in $L\mathcal{M}_n^{\mathrm{red}, \mathrm{trop}}$. Its image under the tropical Torelli map therefore defines a closed cycle $\lambda i\sigma_{W_n}$, which is the image of $\tau_{W_n}$ in $L\mathcal{A}_n^{\mathrm{trop}}$, whose class is $$[\lambda i \sigma_{W_n}] \in H_{2n-1} (L\mathcal{A}_n^{\mathrm{trop}}) \ .$$ It is non-zero since its image in $H_{2n-1} (L\mathcal{A}_n^{\mathrm{trop}},\partial L\mathcal{A}_n^{\mathrm{trop}})$ is non-zero by Theorem 4 $(i)$.

### Proof of Theorem 4 (ii).

A certain subcomplex of the perfect cone complex, called the inflation complex, was defined in [@TopWeightAg] and was shown to be acyclic. This result implies that the long exact relative homology sequence: $$\ldots \longrightarrow H_{k}(\partial L\mathcal{A}_g^{\mathrm{trop}}) \longrightarrow H_k(L\mathcal{A}_g^{\mathrm{trop}}) \longrightarrow H_k\left(L\mathcal{A}_g^{\mathrm{trop}}, \partial L\mathcal{A}_g^{\mathrm{trop}}\right) \longrightarrow H_{k-1}(\partial L\mathcal{A}_g^{\mathrm{trop}})\longrightarrow\ldots$$ splits into short exact sequences, since the inclusion of the boundary $\partial L\mathcal{A}_g^{\mathrm{trop}}$, which is isomorphic to $L\mathcal{A}_{g-1}^{\mathrm{trop}}$, into $L\mathcal{A}_g^{\mathrm{trop}}$ is trivial in homology. Thus we obtain short exact sequences $$0 \longrightarrow H_k(L\mathcal{A}_g^{\mathrm{trop}}) \longrightarrow H_k\left(L\mathcal{A}_g^{\mathrm{trop}}, \partial L\mathcal{A}_g^{\mathrm{trop}}\right) \overset{\partial}{\longrightarrow} H_{k-1}(L\mathcal{A}_{g-1}^{\mathrm{trop}})\longrightarrow 0   \ .$$ Apply this to $g=n+1$ and $k=2n+1$. The inflation $\mathrm{ifl}( \lambda i\sigma_{W_n})$ defines a chain in $L\mathcal{A}_{n+1}^{\mathrm{trop}}$ whose boundary is the image of $\lambda i \sigma_{W_n}$ in $L\mathcal{A}_{n}^{\mathrm{trop}} \cong \partial L\mathcal{A}_{n+1}^{\mathrm{trop}}$. Thus one has $$\begin{aligned}
   \partial: H_{2n+1}\left(L\mathcal{A}_{n+1}^{\mathrm{trop}}, \partial L\mathcal{A}_{n+1}^{\mathrm{trop}}\right) & \longrightarrow&  H_{2n}(L\mathcal{A}_{n}^{\mathrm{trop}})   \nonumber \\
{[}\mathrm{ifl}(\lambda  i \sigma_{W_n})] & \mapsto & [\lambda i\sigma_{W_n}]\ . \nonumber
\end{aligned}$$ Since, by Theorem 8, the class $[\lambda i \sigma_{W_n}]$ is non-vanishing, the same is true of ${[}\mathrm{ifl}(\lambda  i \sigma_{W_n})]$. We conclude by identifying $H_{2n+1}\left(L\mathcal{A}_{n+1}^{\mathrm{trop}}, \partial L\mathcal{A}_{n+1}^{\mathrm{trop}}\right)$ with $H_{2n+1}^{\mathrm{lf}}({\mathbb R}_{>0}^{\times} \setminus \mathcal{P}_{n+1}/\mathrm{GL}_{n+1}({\mathbb Z})) \cong  H_{2n+2}^{\mathrm{lf}}( \mathcal{P}_{n+1}/\mathrm{GL}_{n+1}({\mathbb Z}))$ and by noting that $\mathrm{ifl}(\lambda  i \sigma_{W_n})$ is the link of $\mathrm{ifl}(\tau_{W_n})$.

## Questions meriting further investigation

### Other graph complexes

It would be very interesting to apply the techniques of this paper to try to prove the non-vanishing of homology classes in other graph complexes (see [@Kontsevich93; @ConantVogtmann]).

### Alternative approaches to Theorem 1

A theorem of Bismut-Lott [@BismutLott] implies that the canonical form $\omega^{2n-1}$ is zero in the cohomology of ${\mathbb R}^{\times}_{>0} \setminus \mathcal{P}_{n}/\mathrm{GL}_{n}({\mathbb Z})$. It would be very interesting to write down an explicit primitive $\alpha^{2n}$ such that $\omega^{2n-1} = \mathrm{d}\alpha^{2n}$. In this case, Stokes' formula would imply that the canonical integral $I_{W_n}(\omega^{2n-1})$ may be computed by the integral of $\alpha^{2n}$ over the boundary of the blow-up $\widetilde{\sigma}_{W_n}$ of the simplex $\sigma_{W_n}$ associated to $W_n$, which admits a combinatorial description in terms of sub- and quotient graphs of $W_n$, which are particularly simple. This, together with [@Grobner], suggests that there may be an automorphic (and simpler) proof of Theorem 1 via residues of generalised Eisenstein series.

### Wheel motives and relation between canonical integrals and Feynman residues

The wheel motives have not to our knowledge been completely worked out at the time of writing but some partial information is known [@BEK]. One expects that $\mathrm{mot}_{W_n}$ is a mixed Tate motive over ${\mathbb Z}$ whose weight-graded pieces are ${\mathbb Q}(0)$, and ${\mathbb Q}(-2k-1)$ for $1\leq k\leq 2n.$ It is known that the Feynman residue for *any* $n\geq 3$ satisfies $$\label{IFeynWndef} I^{\mathrm{Feyn}}_{W_n} =  \int_{\sigma_{W_n}}  \frac{\Omega_{2n}}{\Psi^2_{W_n}}  = \genfrac(){0pt}{}{2n-2}{n-1}\zeta(2n-3)$$ and that $[ \frac{\Omega_{2n}}{\Psi^2_{W_n}}]$ spans a copy of ${\mathbb Q}(-2n+3)$ in the highest weight quotient of $\mathrm{mot}_ {\mathrm{dR}}$. It would be interesting to show that for all $n>1$ odd:

1.  $[\omega^{2n-1}_{W_n} ]$ lies in $\mathcal{W}_{2n} \cap F^n \,  \mathrm{mot}_ {\mathrm{dR}}$ (where $\mathcal{W}$, $F$ denote the weight and Hodge filtrations), and spans a copy of ${\mathbb Q}(-n)$. This should follow from the fact that it is the pullback of the Borel class.

2.  For weight reasons, it vanishes in the ordinary cohomology group $H_ {\mathrm{dR}}^{2n-1} \left(P^{W_n} \setminus Y_{W_n}\right)$ (as opposed to the relative cohomology which defines the graph motive).

3.  Therefore by repeated application of Stokes' formula [@BrSigma] the canonical wheel integral for $W_n$ can be reduced to a multiple of the Feynman residue for a *different* wheel graph $W_{\frac{n+3}{2}}$.

These ideas are discussed from a slightly different perspective in [@BrSigma §9.5.1].

## Regulators

The relationship between regulators and the integrals (intro: IGdef) is subtle, since the Borel regulator involves the pairing between *stable* homology and cohomology classes, whereas (wheelseq) involves *unstable*, *locally finite* classes. To compare the two, let $n>1$ be odd.

On the one hand, the wheel integral for $\zeta(n)$ is the integration pairing between $$\label{WheelSetUp}
[\sigma_{W_n}]\in H^{\mathrm{lf}}_{2n-1}(L\mathcal{P}_n/ \mathrm{GL}_n({\mathbb Z}))   \quad \hbox{ and }  \quad  \omega^{2n-1}  \ ,$$ where the latter differential form represents a relative cohomology class. The regulator $$\label{regulator} r_{2n-1}: K_{2n-1}({\mathbb Z}) \otimes_{{\mathbb Z}}{\mathbb Q}\rightarrow {\mathbb C}\ ,$$ on the other hand, is obtained as the pairing between a rational homology class: $$\label{RegulatorSetUp}
[\gamma_n] \in H_{2n-1}^{\mathrm{lf}}(L\mathcal{P}_g/ \mathrm{GL}_g({\mathbb Z})) \qquad \hbox{ and } \qquad  [\omega^{2n-1}] \in H^{2n-1} (L \mathcal{P}_g/\mathrm{GL}_g({\mathbb Z}))\ ,$$ for any $g$ in the stable range. Since the $\omega^{2n-1}$ form a compatible projective system on the $L \mathcal{P}_g/\mathrm{GL}_g({\mathbb Z})$ with respect to the stabilisation maps $L \mathcal{P}_g/\mathrm{GL}_g({\mathbb Z}) \rightarrow L \mathcal{P}_{g+1}/\mathrm{GL}_{g+1}({\mathbb Z})$, the strongest possible result is obtained when $g$ is as small as possible, provided that one can define $\gamma_n$ as in (RegulatorSetUp). Note that, in order to compute the regulator, Borel takes $g$ very large. The smallest possible value of $g$ satisfies $n<g\leq n+2$, since by [@BismutLott], we know that $\omega^{2n-1}$ is trivial in the cohomology of $L \mathcal{P}_g/\mathrm{GL}_g({\mathbb Z})$ for $g=n$, but non-zero in its cohomology for all $g\geq n+2$ (by [@brown2023bordifications]). It is expected that $g=n+2$ is optimal. The upshot of this discussion is that the regulator and the wheel integrals (or even their inflations) necessarily take place in different locally symmetric spaces $L \mathcal{P}_g/\mathrm{GL}_g({\mathbb Z})$ for different values of $g$.

For instance, when $n=3$ the wheel integral for $\zeta(3)$ may be computed on $\mathrm{GL}_3({\mathbb Z})$ (or, at a push, after inflation on $\mathrm{GL}_4({\mathbb Z})$), but the regulator may only be computed on $\mathrm{GL}_g({\mathbb Z})$ for $g\geq 5.$

Nevertheless, it is in fact possible to relate the wheel and regulator integrals, in the following way. Let $g>3$ be odd and let $\mathcal{F}_g \in H^{\mathrm{lf}}_{d_g}( {\mathbb R}_{>0}^{\times} \setminus P_g / \mathrm{GL}_g({\mathbb Z}))$ denote the fundamental class in locally finite homology. We shall use the coaction on homology which is dual to the cup-product between compactly supported and non-compactly supported cohomology. Denote it by $$\Delta:    H^{\mathrm{lf}}_{d_g}  \longrightarrow\bigoplus_{m+n= d_g} H^{\mathrm{lf}}_m \otimes H_n \ .$$ Let $\alpha_g \in  H^{d_g-2g+3}(L\mathcal{P}_g/\mathrm{GL}_g({\mathbb Z});{\mathbb Q})$ denote a non-zero rational (singular) cohomology class which is proportional (over ${\mathbb R}^{\times}$) to the class of the form $\omega^5 \wedge \omega^9 \wedge \ldots \wedge \omega^{2g-5}$. The latter is non-zero by [@brown2023bordifications].

We deduce the existence of a rational homology class $$\label{rhoclass}   \rho_g: = \left( \mathrm{id} \otimes  \alpha_g\right)  \Delta \mathcal{F}_g  \ \in  \  H^{\mathrm{lf}}_{2g-1}( L\mathcal{P}_g/\mathrm{GL}_g({\mathbb Z});{\mathbb Q})$$ which has the property that $$\mathrm{vol}(\mathcal{F}_g)  = \int_{\mathcal{F}_g} \omega^5 \wedge \omega^9 \wedge \ldots \wedge \omega^{2g-1} =  \int_{\rho_g} \omega^{2g-1}  \times  \int_{\phi_g}  \omega^5 \wedge \omega^9 \wedge \ldots \wedge \omega^{2g-5}$$ for some rational homology class $\phi_g$. The class $\phi_g$ may in turn be decomposed via the coproduct on ordinary homology (dual to the cup-product on cohomology) into classes $$[\gamma_{2n-1} ]  \ \in \ H_{2n-1} (L\mathcal{P}_g / \mathrm{GL}_g({\mathbb Z});{\mathbb Q})$$ such that $$\int_{\phi_g}  \omega^5 \wedge \omega^9 \wedge \ldots \wedge \omega^{2g-5}  = \int_{\gamma_5} \omega^5 \times \ldots  \times \int_{\gamma_{2g-5}} \omega^{2g-5} \ ,$$ which, by the above discussion, is proportional over ${\mathbb Q}^{\times}$ to a product of regulators $r_5 r_9 \ldots r_{2g-5}$ (where we denote by $r_{2n-1}$ the value of (regulator) on a generator). Putting the pieces together, we deduce that $$\int_{\rho_g} \omega^{2g-1}   = \frac{   \mathrm{vol}(\mathcal{F}_g)   } {\int_{\phi_g}    \omega^5 \wedge \omega^9 \wedge \ldots \wedge \omega^{2g-5}      } = \frac{   \mathrm{vol}(\mathcal{F}_g)   } { r_5 r_9 \ldots r_{2g-5}}  \ .$$ By Minkowski, $\mathrm{vol}(\mathcal{F}_g)$ is proportional to $\zeta(3)\zeta(5) \ldots \zeta(2g-1)$. By Borel, the regulator $r_{2n-1}$ for $n>1$ odd is proportional to $\zeta(n)$. Thus we conclude that, up to a non-zero rational multiple $$\int_{\rho_g} \omega^{2g-1}   =  \frac{ \zeta(3) \zeta(5) \ldots \zeta(2g-1)}{\zeta(3) \zeta(5)\ldots \zeta(2g-5)} = \zeta(2g-1) \ .$$ We expect that the class $\rho_g$ constructed in this manner out of the locally finite fundamental class is proportional to the wheel class $[\sigma_{W_g}]$. It is true for $g=3,5,7$ since in this case $H^{\mathrm{lf}}_{g}(\mathrm{GL}_g({\mathbb Z});{\mathbb Q})$ is one-dimensional (see Table 1). Then the previous calculation provides a conceptual explanation for why the wheel integrals are single zeta values, and a connection between them and regulators: in brief, from this point of view, the wheel integrals are dual to a product of regulators.

The argument may of course be reversed and gives a computation of Borel regulators in terms of wheel integrals. The first interesting case (where $\sim_{{\mathbb Q}^{\times}}$ denotes equality up to an element in ${\mathbb Q}^{\times}$) is $$r_5 \sim_{{\mathbb Q}^{\times}}  \frac{\mathrm{vol}(\mathcal{F}_7)}{ I_{W_5}} \sim_{{\mathbb Q}^{\times}}   \frac{\zeta(3) \zeta(5)}{\zeta(5)} \sim_{{\mathbb Q}^{\times}}   \zeta(3) \ .$$

**Remark 13**. *Curiously, the interpretation of wheel integrals as periods of the wheel motives gives a different way to relate them to algebraic $K$-theory. Indeed, one expects that the wheel period integrals correspond to a simple extension of ${\mathbb Q}(-n)$ by ${\mathbb Q}(0)$, which corresponds to a class in $K_{2n-1}({\mathbb Z})\otimes_{{\mathbb Z}} {\mathbb Q}$.*

This completes our discussion of cohomological implications of Theorem 1.

# Formula for generic $(B\Omega)^{2n-1}$ {#sec: 3}

In this section we state a formula for $(B\Omega)^{2n-1}$ where $B$ is an $n\times n$ matrix with generic entries $b_{ij}$ and $\Omega$ is an $n\times n$ matrix whose entries are generic differential one-forms $\omega_{ij}.$ The formula breaks up into isotypical pieces indexed by *types* $\nu$, involving differential forms $\omega_{\nu}$ of degree $2n-1$ in the entries of $\Omega$, and matrices $\Phi_{\nu}(B)$ whose entries are *permanent polynomials* in the $b_{ij}$. More precisely: $$(B\Omega)^{2n-1} = \left( \det B\right) \sum_{\nu} \Phi_{\nu}(B) \,\omega_\nu \ .$$ The following example may give a sense of the content of this formula.

**Example 14**. *For $n=2$, let $$B  = \begin{pmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{pmatrix}
\qquad \hbox{ and } \qquad   \Omega=   \begin{pmatrix} \omega_{11} & \omega_{12} \\ \omega_{21} & \omega_{22} \end{pmatrix} \ .$$ Then the formula above reduces to the following expression for $(B\Omega)^3 = B \Omega B \Omega B \Omega$: $$\begin{aligned}
(B\Omega)^3 &= (\det B) \Bigg(\left(\begin{array}{cc}2b_{11}&0\\b_{21}&b_{11}\end{array}\right)
\omega_{11}\wedge\omega_{12}\wedge\omega_{21}
+\left(\begin{array}{cc}b_{21}&b_{11}\\0&2b_{21}
\end{array}\right)
\omega_{11}\wedge\omega_{12}\wedge\omega_{22}\\
&\qquad\quad\,+\,\left(\begin{array}{cc}2b_{12}&0\\b_{22}&b_{12}\end{array}\right)
(-\omega_{11}\wedge\omega_{21}\wedge\omega_{22})
+\left(\begin{array}{cc}b_{22}&b_{12}\\0&2b_{22}\end{array}\right)
(-\omega_{12}\wedge\omega_{21}\wedge\omega_{22})\Bigg).
\end{aligned}$$*

Although it will not be required for the time being, we record the following statement, which follows from the same method of proof of [@BrSigma Proposition 4.5].

**Proposition 15**. *For $B, \Omega$ as above, $(B \Omega)^{2n}=0$.*

This section is therefore devoted to computing the highest non-vanishing power of $(B \Omega)$.

## Basic set-up and notations {#sec: BOmeganotations}

### Matrices

Let $I, J$ be ordered sets, with possible repeats, of equal length $n\geq 1$. We denote by $$B_{I,J} = (b_{ij})_{i\in I, j\in J}$$ the $n\times n$ matrix whose entries are indexed by the elements of $I,J$ in order. For example, we have $$B_{12,23}=\left(\begin{array}{cc}b_{12}&b_{13}\\b_{22}&b_{23}\end{array}\right),\quad B_{22,23}=\left(\begin{array}{cc}b_{22}&b_{23}\\b_{22}&b_{23}\end{array}\right) \ .$$ When the integer $n\geq 1$ is clear from the context, we shall simply write $$B = B_{\{1,\ldots, n\}, \{1,\ldots, n \}} = (b_{ij})_{1\leq i,j\leq n}\ $$ to be the $n\times n$ matrix with (generic) entries $b_{ij}$ in row $i$ and column $j$.

### Forms

Let $\Omega= (\omega_{ij})_{1\leq i, j \leq n}$ denote the $n\times n$ matrix whose entries are generic one-forms. To make sense of the product $B\Omega$, and its powers, we work in the graded-commutative graded algebra (or DGA with zero differential) $R= \bigoplus_{m\geq 0} R^m$, where $R^0 = {\mathbb Q}[b_{ij}]$ is the polynomial ring generated by the entries of $B$, and $R^1= \bigoplus_{i,j} R^0 \omega_{ij}$ is the free $R^0$-module generated by the entries of $\Omega.$ The degree $m$ component $R^m$ is generated by exterior products of degree $m$ in the elements of $\Omega$. The entries of $(B\Omega)^{2n-1}$ lie in the component of degree $2n-1$: $$R^{2n-1}  =  \bigoplus_{\nu}  \left(  R^0  \!  \bigwedge_{(i,j) \in \nu } \omega_{ij} \right)\ ,$$ where $\nu$ is a *type* of rank $n$, which is defined to be a subset $$\label{defn: nu} \nu  \ \subset \  \{ (i,j): 1\leq i, j\leq n\}$$ of cardinality $2n-1$.

**Remark 16**. *A type may be interpreted as a bipartite graph with $2n$ vertices (indexed by two sets of integers numbered from $1$ to $n$), with $2n-1$ edges between them. (Note that in Section 9.2, we shall interpret a type differently, namely as an oriented graph with $n$ vertices (and self-loops), where a pair $(i,j)$ is an edge from vertex $i$ to vertex $j$.)*

### Isotypical components

There is a natural projection of graded algebras $R \rightarrow  R_{\nu}$, where $R_{\nu} \subset R$ is the graded subalgebra generated over $R_0$ by the $\omega_{ij}$ for only those $(i,j) \in \nu$. It is defined by sending $\omega_{kl}$ to zero for all $(k,l) \notin \nu.$ It extends to a map on matrices whose elements are in $R$ $$M_{n\times n}(R) \longrightarrow M_{n\times n}(R_{\nu})\ ,$$ which we denote by $X\mapsto X_{\nu}$. Since this map is an algebra homomorphism we immediately deduce:

**Proposition 17**. *The following identity holds in the ring $M_{n\times n}(R)$: $$\label{BOmegaAsSumIsotypical} (B \Omega)^{2n-1}  =  \sum_{\nu}  (B \Omega_{\nu})^{2n-1} \ ,$$ where $\Omega_{\nu}$ is the $n\times n$ matrix whose entries are all zero except for $\omega_{ij}$ in position $(i,j)$ whenever $(i,j) \in \nu$.*

In particular, it suffices to find a formula for $(B \Omega_{\nu})^{2n-1}$.

**Example 18**. *Consider the following three types of rank $3$: $$\nu_1 = \{11,12,22,23,33\} \ , \   \nu_2 = \{11,12,13,22,33\} \ ,  \  \nu_3 = \{13,23,33,31,32\}\ .$$ The corresponding matrices of one-forms are $$\Omega_{\nu_1} = \begin{pmatrix} \omega_{11} & \omega_{12} & \\ & \omega_{22} & \omega_{23} \\ & & \omega_{33}
\end{pmatrix} \quad , \quad
\Omega_{\nu_2} = \begin{pmatrix} \omega_{11} & \omega_{12} &  \omega_{13}\\ & \omega_{22} &  \\ & & \omega_{33}
\end{pmatrix} \quad  , \quad   \Omega_{\nu_3} = \begin{pmatrix} & &  \omega_{13} \\
&&\omega_{23}\\
\omega_{31} &\omega_{32}& \omega_{33}
\end{pmatrix}\ ,$$ where here, and elsewhere, blank entries in a matrix denote an entry which is zero.*

## Weights and differential forms associated to a type {#sect: weightsoftypes}

To any type $\nu$ of rank $n$ we will associate a pair of weight vectors, which will play a prominent role in the theory.

**Definition 19**. *To any type $\nu = \{(i_k,j_k): k=1,\ldots, 2n-1\}$ of rank $n$, we define its *weight vectors* $$w(\nu) = ({\underline{p}}(\nu), {\underline{q}}(\nu))\ ,$$ where ${\underline{p}}(\nu) = ({\underline{p}}(\nu)_1,\ldots, {\underline{p}}(\nu)_n)$, and ${\underline{q}}(\nu) = ({\underline{q}}(\nu)_1,\ldots,{\underline{q}}(\nu)_n)$ are row vectors of length $n$ defined by $${\underline{p}}(\nu)_i =  \left|\{i: (i,j) \in \nu \hbox{ for some } j \}  \right|\qquad \ , \qquad  {\underline{q}}(\nu)_j =  \left| \{j: (i,j) \in \nu \hbox{ for some } i  \} \right| \ .$$*

**Remark 20**. *As in Remark 16, the entries in the weight vectors of a type are simply the degrees of each vertex in the corresponding bipartite graph.*

For the three types considered in Example 18 we have $$w(\nu_1) = ((2,2,1),(1,2,2))\ ,\qquad
 w(\nu_2) = ((3,1,1),(1,2,2))\ ,\qquad
 w(\nu_3) = ((1,1,3),(1,1,3)) \ .$$

We next associate a differential form $\omega_{\nu}$ to a type $\nu$ as follows.

**Definition 21**. *Choose any ordering on the elements in $\nu$ (for instance, the lexicographic ordering).*

*(i). Define a $(2n-1) \times 2n$ matrix $M_{\nu}$ whose rows are indexed by the elements in $\nu$. In the $kth$ row indexed by $(i_k,j_k) \in \nu$, place a $-1$ in column $i_k$, a $1$ in column $n+j_k$, and a zero in every other column.*

*(ii). Define a differential $(2n-1)$-form $\eta_{\nu} \in R^{2n-1}$ to be $$\eta_{\nu} = \omega_{i_1,j_1} \wedge \omega_{i_2,j_2} \wedge \ldots \wedge\omega_{i_{2n-1}, j_{2n-1}}$$ where $\nu = ((i_1,j_1), (i_2,j_2), \ldots ,  (i_{2n-1},j_{2n-1}) )$, in that order.*

*(iii). Choose any $1    \leq k \leq 2n$, and let $M_{\nu}^{\emptyset,k}$ be the $(2n-1) \times (2n-1)$ matrix obtained by deleting the $k^{\mathrm{th}}$ column from $M_{\nu}$. Finally, define $$\label{omeganudefnANDepsilonk}
\omega_{\nu} = (-1)^{\binom{n}{2}+k-1}\det(M_{\nu}^{\emptyset,k})\, \eta_{\nu}.$$*

**Remark 22**. *As in Remark 16, the matrix $M_{\nu}$ is simply the (signed) edge-vertex incidence matrix of the bipartite graph $\Gamma_{\nu}$ associated to $\nu$, after choosing some ordering on the edges. It follows from the exact sequence $0 \rightarrow H_1(\Gamma_{\nu};{\mathbb Z}) \rightarrow {\mathbb Z}^{E_{\Gamma_{\nu}}} \overset{M_{\nu}^T}{\rightarrow} {\mathbb Z}^{V_{\Gamma_{\nu}}} \rightarrow H_0(\Gamma_{\nu};{\mathbb Z}) \rightarrow 0$ that the incidence matrix has rank $2n-1-b_1=2n-b_0$, where $b_i = \mathrm{rank}\, H_i(\Gamma_{\nu};{\mathbb Z})$ ($i=0,1$) are the Betti numbers of $\Gamma_{\nu}$. In particular, $\omega_{\nu}$ is non-zero if and only if $\Gamma_{\nu}$ is connected and cycle-free, in which case it is a tree. This implies Lemma 24 (ii), (iv), and (v) stated below.*

**Example 23**. *For the three types considered in Example 18 we have $$M_{\nu_1}
= \left(\begin{array}{ccc|ccc}
\!\!-1  &  &   &\!1  & &   \\
\!\!-1  &  &   &  & 1 &   \\
  & \!\!\!\!-1 & &   &1  &   \\
  & \!\!\!\!-1 & &  & &1   \\
  &  & \!\!\!\!-1\!&  & & 1
\end{array} \right)
, \
M_{\nu_2}
= \left(\begin{array}{ccc|ccc}
\!\!-1  &  &   &\!1  & &   \\
\!\!-1  &  &   &  & 1 &   \\
\!\!-1  &  & &   &  & 1   \\
  & \!\!\!\!-1 & &  & 1&    \\
  &   & \!\!\!\!-1\!&  & & 1
\end{array} \right)
, \
M_{\nu_3}
= \left(\begin{array}{ccc|ccc}
\!\!-1  &  &   &  & & 1  \\
  & \!\!\!\!-1 &   &  &  & 1  \\
  &  & \!\!\!\!-1\!&   &  & 1   \\
  & & \!\!\!\!-1\!&\! 1 &  &    \\
  &  & \!\!\!\!-1\!&  & 1 &
\end{array} \right).$$ The vertical lines are merely visual aids. The reader may check that the sums of the entries in each column give back the weight vectors $w(\nu)$ (with $-{\underline{p}}(\nu)$ to the left of the vertical line, and ${\underline{q}}(\nu)$ to the right).*

*The corresponding differential forms are $$\begin{aligned}
\omega_{\nu_1}&=\omega_{11}\wedge\omega_{12}\wedge\omega_{22}\wedge\omega_{23}\wedge\omega_{33} \ ,\\
\omega_{\nu_2}&=-\omega_{11}\wedge\omega_{12}\wedge\omega_{13}\wedge\omega_{22}\wedge\omega_{33}  \ ,\\
\omega_{\nu_3}&=-\omega_{13}\wedge\omega_{23}\wedge\omega_{33}\wedge\omega_{31}\wedge\omega_{32}  \ .
\end{aligned}$$*

**Lemma 24**. *The differential form $\omega_\nu$ has the following fundamental properties:*

*$(i).$ It does not depend on any choices.*

*$(ii).$ If ${\underline{p}}(\nu)_i=0$ or ${\underline{q}}(\nu)_i=0$ for some $i\in\{1,\ldots,n\}$, then $\omega_\nu=0$.*

*$(iii).$ For any $\nu$, we have $\det(M_{\nu}^{\emptyset,k})\in\{-1,0,1\}$.*

*$(iv).$ If there exist $i_1,i_2, j_1,j_2$ such that $\{ (i_1,j_1), (i_1,j_2), (i_2,j_1), (i_2,j_2)\} \in \nu$, or equivalently, if $\Omega_\nu$ contains a two-by-two submatrix consisting of non-zero entries, then $\omega_\nu=0$.*

*$(v).$ If $\Omega_\nu$ is block-diagonal with $\geq 2$ blocks then $\omega_\nu=0$.*

*$(vi).$ For any set $\bar\nu$ of $2n$ pairs in $\{1,\ldots,n\}$ and any $i\in\{1,\ldots,n\}$ we have $$\label{Onubar1}
\sum_{k:(i,k)\in\bar\nu}\omega_{ik}\wedge\omega_{\bar\nu\setminus (i,k)}=0=\sum_{k:(k,i)\in\bar\nu}\omega_{ki}\wedge\omega_{\bar\nu\setminus (k,i)}\ .$$*

*$(vii)$. Suppose that $\nu$ contains $(i,i), (j,j)$ and $(i,j)$ but not $(j,i)$ for some indices $i\neq j$. Let $\nu'$ denote the type obtained from $\nu$ by replacing $(i,j)$ with $(j,i)$. Then there exists a $(2n-2)$-form $\alpha$ such that: $$\label{flipomegaij} \omega_{\nu} = \omega_{ij} \wedge \alpha  \qquad \hbox{ and } \qquad \omega_{\nu'} = -  \omega_{ji} \wedge \alpha\ .$$ In other words, replacing $(i,j)$ with $(j,i)$ in $\nu$ replaces $\omega_{ij}$ with $-\omega_{ji}$.*

*Proof.* $(i).$ Consider the matrix obtained from $M_\nu$ by adding an additional row $(1,0,\dots,0,-1,0,\ldots,0)$ where the entry $-1$ is in the $k^{\mathrm{th}}$ position. This yields a $2n\times 2n$ matrix $\bar M_\nu$ which annihilates the column vector $(1,\ldots, 1)^T$. It follows that $\det(\bar M_{\nu})=0$. Expansion along the final row shows that $\omega_\nu$ does not depend on the choice of $k$. Furthermore, $\omega_{\nu}$ does not depend on the choice of ordering of $\nu$, since changing the ordering by a permutation $\sigma$ corresponds to performing a row permutation on $M_{\nu}$, which multiplies $\det(M_{\nu}^{\emptyset,k})$ by $\mathrm{sign}(\sigma)$. Likewise, permuting the factors in $\eta_{\nu}$ by $\sigma$ has the exact same effect. These two effects cancel since $\mathrm{sign}(\sigma)^2=1.$

$(ii).$ If ${\underline{p}}(\nu)_i=0$ then $M_{\nu}^{\emptyset,k}$ has zero column $i$ for $k\neq i$. If ${\underline{q}}(\nu)_i=0$ then $M_{\nu}^{\emptyset,k}$ has zero column $n+i$ for $k\neq n+i$. In either case $\det(M_\nu^{\emptyset,k})=0$.

$(iii).$ Either one column of $M_{\nu}^{\emptyset,k}$ for $k>n$ is empty or there exists a column $i\neq k$, $i\leq n$ with a single non-zero entry in some row corresponding to a pair $(i,j)\in\nu$. In the first case $\det(M_{\nu}^{\emptyset,k})=0$. In the second case we expand the determinant along this column yielding $\det(M_{\nu}^{\emptyset,k})=\pm\det(M_{\nu\setminus(i,j)}^{\emptyset,k-1})$. Proceed by induction to obtain the result.

$(iv).$ The alternating sum of the four rows of $M_{\nu}^{\emptyset,k}$ labelled by $(i_1,j_1), (i_1,j_2), (i_2,j_2), (i_2,j_1)$ is zero. Therefore $\det(M_{\nu}^{\emptyset,k})=0$.

$(v).$ Assume $\Omega_\mu$ has two blocks corresponding to a disjoint union $\nu = \nu_1  \cup \nu_2$ where $\nu_1$ (resp. $\nu_2$) are the row labels of the first (resp. second) block. Then $M_{\nu}  = M_{\nu_1} \oplus M_{\nu_2}$ where $M_{\nu_i}$ is the submatrix of $M_{\nu}$ with rows in $\nu_i$. Since both $M_{\nu_1}$ and $M_{\nu_2}$ have corank $\geq 1$, it follows that $M_{\nu}$ has corank $\geq 2$.

$(vi).$ Consider the $2n\times 2n$ matrix $M_{\bar \nu}$, defined in a similar manner to $M_{\nu}$, whose rows correspond to $\bar\nu=\{(i,j_1),(i,j_2),\ldots\}$ ordered such that all indices of the form $(i,k) \in \bar \nu$ with initial term $i$ occur before all indices of the form $(j,k)$ with $j\neq i.$ We have $\det(M_{\bar\nu})=0$ because $M_{\bar\nu}$ annihilates the column vector $(1,\ldots, 1)^T$. Expanding $\det(M_{\bar\nu})=0$ along column $i$ yields $\sum_{k:(i,j_k)\in\bar\nu}(-1)^{i+k}\det(M_{\bar\nu\setminus (i,j_k)}^{\emptyset,i})=0$. Multiplying this equation with $\eta_{\bar\nu}$ implies the identity on the left, because moving $\omega_{ij_k}$ in $\eta_{\bar\nu}$ to the first slot produces a sign $(-1)^{k-1}$ which compensates the $k$-dependence of the sign in the sum. To prove the second identity we reorder $\bar\nu$ to start with pairs whose second entry is $i$ and expand along column $n+i$.

$(vii)$. Consider $\bar\nu=\nu\cup (j,i)=\nu'\cup (i,j)$. Because of $(iv)$ the sums in ((Onubar1)) only have the two non-zero terms $k=i,j$. We define the $(2n-2)$-form $\alpha$ by $\omega_{ij}\wedge\omega_{ji}\wedge\alpha=\omega_{ii}\wedge\omega_{\bar\nu\setminus (i,i)}$ and obtain $$\omega_{ij}\wedge\omega_{\nu'}=-\omega_{ij}\wedge\omega_{ji}\wedge\alpha=
\omega_{ji}\wedge\omega_{\nu} \ .$$ Equation ((flipomegaij)) follows. ◻

Although $(vi)$ is not directly used in this paper, it may be of use in subsequent applications since it expresses the compatibility of our formula for $\Omega^{2n-1}_{\nu}$ with the equation $\Omega_{\bar\nu}^{2n}=0$.

**Proposition 25**. *Let $\nu$ be a type of rank $n$. Assume the matrix $\Omega_\nu$ has a column $c$ containing a single non-zero entry $\omega_{ic}$. Further assume that after deletion of column $c$ the matrix $\Omega_\nu^{\emptyset,c}$ has a row $r$ with a single non-zero entry $\omega_{rj}$. Then $$\omega_\nu=(-1)^{c+r}\omega_{ic}\wedge\omega_{rj}\wedge\omega_{\nu\setminus\{(i,c),(r,j)\}}\ ,$$ where $\nu\setminus\{(i,c),(r,j)\}$ is considered of rank $n-1$ with no row $r$ and no column $c$. If either assumption does not hold then $\omega_\nu=0$.*

*Proof.* We write $\nu=\{(i,c),(r,j)\}\cup\nu'$ in this order, where the union is disjoint ($\nu'$ consists of all pairs $(k,\ell) \in \nu$ where $k\neq r$, $\ell \neq c$). In the definition (omeganudefnANDepsilonk) of $\omega_\nu$ we choose $k=2n-\delta$ where $\delta=0$ if $c<n$ and $\delta=1$ if $c=n$. (The column labelled by $n+c$ in $M_{\nu}$ is therefore retained in $M^{\emptyset,k}_\nu$.) We expand the determinant of $M_{\nu}^{\emptyset, k}$ along column $n+c-\delta$ which has the single entry $1$ in row $1$. After passing to the corresponding minor (delete the first row and $(n+c-\delta)$th column) the resulting matrix has a single non-zero entry $-1$ in column $r$ and row $1$. Deleting this row and column gives the minor $M_{\nu'}^{\emptyset, 2n-2}$. We therefore obtain $$\omega_\nu=(-1)^{\binom{n}2+k-1} (-1)^{1+n+c-\delta}(-1)^{r}\det(M_{\nu'}^{\emptyset,2n-2})\,\omega_{ic}\wedge\omega_{rj}\wedge\eta_{\nu'}\ ,$$ where $k=2n-\delta$. Because $\binom{n}2=\binom{n-1}2+n-1$, the result follows from ((omeganudefnANDepsilonk)).

If $\Omega_{\nu}$ has a zero row or column, then $\omega_\nu=0$ by Lemma 24 $(ii)$. It remains to consider the case when the row $r$ and column $c$ share a common element $\omega_{rc}$ and all other rows and columns have two non-zero entries (adding up to $2n-1$ entries in total). In this case we choose $k\neq r,n+c$ in Definition 21 and find that the column in $M_\nu^{\emptyset,k}$ which refers to $r$ is the negative of the column that refers to $c$ (namely $(0,\ldots,0,-1,0,\ldots,0)^T$). Therefore the corank of $M_\nu^{\emptyset,k}$ is $\geq1$ and $\omega_\nu=0$. ◻

Proposition 25 describes an inductive way to compute $\omega_\nu$.

**Example 26**. *[]{#n2ex label="n2ex"} (i). For $n=2$ there are four possible types: $$\begin{aligned}
\omega_{\{11,12,21\}}=\omega_{11}\wedge\omega_{12}\wedge\omega_{21},&\qquad\omega_{\{11,12,22\}}=\omega_{11}\wedge\omega_{12}\wedge\omega_{22},\\
\omega_{\{11,21,22\}}=-\omega_{11}\wedge\omega_{21}\wedge\omega_{22},&\qquad\omega_{\{12,21,22\}}=-\omega_{12}\wedge\omega_{21}\wedge\omega_{22}.
\end{aligned}$$*

*(ii). Let $\nu=\{11,22,\ldots,nn,12,23,\ldots,(n-1)n\}$ so that $\Omega_\nu$ has non-zero entries along the diagonal and the line immediately above the diagonal. Proposition 25 gives $$\begin{aligned}
\label{oWn}
\omega_{\nu} &= & \omega_{11}\wedge\omega_{12}\wedge\omega_{22}\wedge\omega_{23}\wedge\ldots\wedge\omega_{nn} \nonumber \\
 &=&(-1)^{\binom{n}2}\,\omega_{11}\wedge \omega_{22} \wedge \ldots\wedge\omega_{nn}\wedge\omega_{12} \wedge \omega_{23} \wedge\ldots
\wedge\omega_{(n-1)n}.
\end{aligned}$$*

*(iii). It can happen that $\omega_{\nu}$ is non-zero, even though the matrix $\Omega_{\nu}^{2n-1}$ is identically zero. An example is given by the type $\nu=\nu_2$ considered in Example 18.*

## Permanents associated to $B$

Recall that the permanent of an $n\times n$ matrix $A = (a_{ij})$ equals: $$\mathrm{perm}\,(A)  =   \sum_{\sigma\in \Sigma_n}  \, a_{1 ,\sigma(1)}a_{2 ,\sigma(2)} \ldots a_{n,\sigma(n)} \ ,$$ where $\Sigma_n$ denotes the symmetric group of order $n$.

**Definition 27**. *Let ${\underline{p}}=(p_1,\ldots, p_k)$ and ${\underline{q}}=(q_1,\ldots, q_k)$ be vectors of integers $p_i,q_i \geq 0$ satisfying $\sum_{i} p_i = \sum_i q_i$. Let $S_{{\underline{p}}}=\{ 1^{p_1}, \ldots, k^{p_k}\}$ denote the multiset with $p_1$ one's, $p_2$ two's, $\ldots$, and $p_k$ copies of $k$. Define the *permanent polynomial* of weights $({\underline{p}},{\underline{q}})$ to be: $$\label{Pdef}
P_{{\underline{p}}, {\underline{q}}}(B)=\mathrm{perm}\,(B_{S_{\underline{p}},S_{\underline{q}}}) \ .$$ It is a homogeneous polynomial in $R^0$ of degree $p_1+\ldots+p_k$ in the indeterminates $b_{ij}$. In the case where ${\underline{p}}$ (or ${\underline{q}}$) has a negative component $p_i<0$ (or $q_i<0$), we shall set $P_{({\underline{p}},{\underline{q}})}(B)=0.$*

**Example 28**. *Referring to the examples given in Section 3.1.1, the definition gives $$P_{(1,1,0),(0,1,1)} (B)= \mathrm{perm}\,(B_{12,23}) = b_{12}b_{23}+b_{13}b_{22}
\ , \qquad
P_{(0,2,0),(0,1,1)} (B)= \mathrm{perm}\,(B_{22,23}) =  2 b_{22}b_{23}  \ .$$*

We shall define a matrix of permanents associated to a type as follows.

**Definition 29**. *Let $\nu$ be a type of rank $n$. Define $\Phi_{\nu}(B)$ in $M_{n\times n}(R_0)$ to be the matrix whose entries for $1 \leq i , j \leq n$ are $$\label{Phidef}
\left( \Phi_{\nu}(B)\right)_{ij} =    ({\underline{q}}(\nu)_j+\delta_{i,j}-1)
P_{{\underline{q}}(\nu)+{\underline{e}}_i-{\underline{e}}_j-{\underline{1}},{\underline{p}}(\nu)-{\underline{1}}}(B)\ ,$$ where $\delta_{ij}$ is the Kronecker delta, ${\underline{e}}_i=(0,\ldots, 1, \ldots 0)$ is the row vector of length $n$ with a single $1$ in the $i^{\mathrm{th}}$ slot, and ${\underline{1}}=(1,\ldots,1)$ is the vector of length $n$ with all entries 1.*

**Example 30**. *Let $\nu= (11,12,22)$ with weight vectors ${\underline{p}}(\nu)= (2,1)$ and ${\underline{q}}(\nu)=(1,2)$. Then $$\Phi_{\nu}(B) = \begin{pmatrix}   1 \times P_{(0,1), (1,0)}(B)  &   1 \times  P_{(1,0), (1,0)}(B)  \\
    0 \times   P_{(-1,2), (1,0)} (B)   &   2 \times  P_{(0,1), (1,0)}(B)  \\
\end{pmatrix} =   \begin{pmatrix}  \mathrm{perm}\,((b_{21})) &  \mathrm{perm}\,((b_{11})) \\
0 &  2  \mathrm{perm}\,((b_{21}))
\end{pmatrix}\ .$$ This matrix occurs in the second term of Example 14.*

## Statement of the identity {#sect: statementid}

**Theorem 31**. *Let $B$ and $\Omega$ be as above. We have $$\label{eqthm1a}
(B\Omega_{\nu})^{2n-1} = \left( \det B\right) \, \Phi_{\nu}(B) \,\omega_\nu,$$*

The proof of this theorem is postponed to Section 9. Using Proposition 17, the theorem gives a closed formula for $(B\Omega)^{2n-1} = \sum_{\nu} (B\Omega_{\nu})^{2n-1}$.

**Example 32**. *Let $\nu_1,\nu_2,\nu_3$ be as in Example 18. Then $$\begin{aligned}
  (B \Omega_{\nu_1} )^5  &= &    \det(B) \begin{pmatrix}   b_{21}b_{32}+b_{22}b_{31} &
b_{11}b_{3 2}+b_{1 2}b_{3 1}   &   b_{1 1}b_{2 2}+b_{1 2}b_{2 1}   \\
 0 &  2  (b_{21}b_{32}+b_{22}b_{31})   & 2 b_{21}b_{2 2} \\
0 &  2 b_{31} b_{32}  &   2(b_{21}b_{32}+b_{22}b_{31})  \\
 \end{pmatrix} \omega_{\nu_1} \ ,  \nonumber \\
  (B \Omega_{\nu_2} )^5 & =  &   \det(B) \begin{pmatrix}   2 b_{21}b_{3 1}  & 2  b_{1 1} b_{3 1} & 2 b_{11} b_{21} \\
  0 & 4b_{21}b_{3 1}   & 2b_{21}^2 \\
  0 &  2 b_{3 1}^2 &   4 b_{21}b_{31}
  \end{pmatrix} \omega_{\nu_2}\ ,\nonumber \\
   (B \Omega_{\nu_3} )^5 & =  &   \det(B)
   \begin{pmatrix}
    2 b_{33}^2 &  0 & 4 b_{13} b_{33}  \\
    0 &  2 b_{33}^2  &  4 b_{23} b_{33} \\
    0 &  0 &   6 b_{33}^2
   \end{pmatrix}  \omega_{\nu_3} \ .\nonumber

\end{aligned}$$*

**Corollary 33**. *By taking the trace of (eqthm1a) we obtain: $$\label{eqtr}
\mathrm{tr}\,\left( \left( B\Omega_{\nu}\right)^{2n-1}\right)  =(2n-1)\det(B)  \,
P_{{\underline{q}}(\nu)-{\underline{1}},{\underline{p}}(\nu)-{\underline{1}}}(B)\,\omega_\nu .$$*

*Proof.* Since $\sum_{i=1}^n{\underline{q}}(\nu)_i=2n-1$, one has $\mathrm{tr}\,\,\Phi_{\nu}(B) = (2n-1) P_{{\underline{q}}(\nu)-{\underline{1}},{\underline{p}}(\nu)-{\underline{1}}}(B)$. ◻

# Antisymmetrised Permanents {#sect: AntiSymPerm}

The next step in the reduction from generic to symmetric matrices will require a formula for antisymmetrised permanents which we state here. Its proof is in Section 10.

## Notation

Let $m>0$ and let $S_m = \{s_1,\ldots, s_m\}$, $T_m = \{t_1,\ldots, t_m\}$ be two sets with $m$ elements. We work in the polynomial ring over ${\mathbb Z}$ generated by symbols $b_{uv}$, for $u,v \in S_m \cup T_m$, subject to the relation $b_{uv} = b_{vu}$. We fix an order in $S_m$ and $T_m$ and consider the generic symmetric $m \times m$ matrix $$B_{S_m,T_m}  =  (b_{s_it_j})_{i,j},$$ which is indexed by the (generic) sets $S_m$ and $T_m$.

### Antisymmetrisation

Consider the involutions $$g_1,\ldots, g_m   \ \in \  \Sigma_{S_m \cup T_m}$$ acting on the set $S_m \cup T_m$, where $g_i$ interchanges $s_i$ and $t_i$, and leaves all other elements fixed. These automorphisms generate a group $G_m \cong \left( {\mathbb Z}/2{\mathbb Z}\right)^m$ which acts on ${\mathbb Z}[b_{uv}, u,v \in S_m \cup T_m]$ by permuting indices. Consider the character $\chi : G_m  \rightarrow  {\mathbb Z}^{\times} = \{\pm 1\},$ which is defined by $\chi( g_i) =  -1$ for each $i$. For any subgroup $G<G_m$ we define $$\pi_{G} = \sum_{g\in G} \chi(g) g$$ to be the projector onto the $\chi$-isotypical part of a $G$-representation, i.e., which is anti-invariant with respect to every $g_i\in G$. If $G$ is generated by $g_i$, $i\in I\subseteq\{1,\ldots,m\}$, we shall simply write $\pi_I$ for $\pi_G$. Note that $\pi_i = 1-g_i$, for any $i\in\{1,\ldots,m\}$.

**Definition 34**. *We denote the fully antisymmetrised generic permanent by $$\mathrm{perm}\,B_{[S_m,T_m]}  =  \pi_{\{1,\ldots,m\}}\, \mathrm{perm}\,B_{S_m,T_m} \ .$$ It is the image of $\mathrm{perm}\,B_{S_m,T_m}$ under the full antisymmetrisation operator $\pi_{G_m}$.*

Our goal is to give a formula for $\mathrm{perm}\,B_{[S_m,T_m]}$ in terms of determinants of matrices obtained from $B_{S_m,T_m}.$ Consider the following examples for $m\leq 2$.

**Example 35**. *Let $m=1$. Then $$B_{S_1,T_1} = \begin{pmatrix} b_{s_1t_1} \end{pmatrix}$$ and therefore $\mathrm{perm}\,(B_{S_1,T_1})  = b_{s_1t_1}$ which is symmetric with respect to the operator $g_1$ which interchanges $s_1$ and $t_1$. Therefore its antisymmetrisation $B_{[S_1,T_1]}=\pi_1 \mathrm{perm}\,(B_{S_1,T_1})=0$ vanishes.*

*Now let $m=2$, for which $$B_{S_2,T_2} = \begin{pmatrix} b_{s_1t_1} & b_{s_1t_2} \\ b_{s_2t_1} & b_{s_2t_2} \end{pmatrix} \qquad \hbox{ with } \qquad \mathrm{perm}\,B_{S_2,T_2}  =  b_{s_1t_1}b_{s_2t_2} + b_{s_1t_2}b_{s_2t_1}\ .$$ We find that the antisymmetrised permanent can be rewritten as a determinant of a different matrix: $$\pi_{1,2}   \, \mathrm{perm}\,(B_{S_2,T_2}) =  2 \left(  b_{s_1t_2} b_{s_2t_1} - b_{s_1s_2} b_{t_1t_2} \right)= -  2 \det B_{s_1t_1, s_2t_2}.$$ Thus we obtain $$\label{N2ex}
 \mathrm{perm}\,\, B_{[S_2,T_2]}=-2 \det B_{s_1t_1, s_2t_2}.$$*

We generalise this formula to matrices of all ranks below. It will turn out that all antisymmetrised permanents of odd rank vanish, leaving only those of even rank $m$.

### Indexing sets

To state our formula, we need to define some indexing sets.

**Definition 36**. *Let $m\geq 2$ even. For all $k\geq 1$, define $\mathcal{D}^k_{m}$ to be the set of (unordered) $k$-tuples $$\{\{I_1,J_1\} , \ldots, \{ I_k, J_k\} \}$$ such that:*

1.  *$\{1,\ldots,m\}$ is the disjoint union of $I_1,\ldots, I_k, J_1, \ldots J_k$.*

2.  *$I_i$ and $J_i$ are non-empty, and have the same cardinality $|I_i|=|J_i|$, for all $1\leq i \leq k.$*

*Since $I_i$, $J_i$ are subsets of $\{1,\ldots, m\}$, they inherit an ordering on their elements. The formulae below do not ultimately depend upon this ordering.*

One may construct the set $\mathcal{D}^k_{m}$ in two stages. First, partition $\{1,\ldots, m\} = A_1 \cup \ldots \cup A_k$ into a disjoint union of $k$ sets, each of which has an even number of elements and is non-empty. Second, choose a decomposition of $A_i= I_i \cup J_i$ as a disjoint union of two sets of equal size $|I_i|= |J_i|$, for every $1 \leq i \leq k$.

**Example 37**. *Note that $\mathcal{D}^k_{m}$ is empty unless $k\leq\frac{m}2$.*

-   *Let $m=2$. Then $\mathcal{D}^1_2$ has a unique element, given by $\{I_1,J_1\}= \{\{1\},\{2\}\}.$*

-   *Let $m=4$. Then $\mathcal{D}^1_4$ has three elements, given by $$\{I_1,J_1\} :   \quad  \{\{1,2\}, \{3,4\}\} \ , \  \{\{1,3\}, \{2,4\}\} \ , \  \{\{1,4\}, \{2,3\}\}$$ corresponding to the three partitions of $\{1,\ldots, 4\}$ into two sets with two elements, and $\mathcal{D}^2_4$ also has three elements where $\{ \{I_1,J_1\}  , \{I_2,J_2\} \}$ equals: $$\{   \{\{1\}, \{2\}\}   \  , \  \{\{3\}, \{4\}\}  \}    \quad , \quad     \{   \{\{1\}, \{3\}\}   \ , \ \{\{2\}, \{4\}\}  \}  \quad , \quad   \{   \{\{1\}, \{4\}\}   \ , \ \{\{2\}, \{3\}\}  \}\ .$$*

If $I$ is the ordered set $\{i_1,\ldots, i_k\}$ one may equip the set $S_I \cup T_I$ with the ordering $s_{i_1}, t_{i_1}, \ldots, s_{i_k}, t_{i_k}$, or alternatively, as $s_{i_1},\ldots, s_{i_k}, t_{i_1}, \ldots, t_{i_k}$. We shall do the former, but either convention, when applied consistently, leads to the same formula for $\Sigma$ as a polynomial of determinants in the following definition.

**Definition 38**. *Let $B_{S_{m},T_{m}}$ be as above. Define the polynomial: $$\label{eq: Sigma}
\Sigma(B,S_{m}\cup T_{m}) = \sum_{k=1}^{m/2}   (-2)^k\,  k! \,     \sum_{  \{\{I_1,J_1\} , \ldots, \{ I_k, J_k\} \} \in \mathcal{D}^k_{m}  }
\det(B_{S_{I_1}\cup T_{I_1}, S_{J_1}\cup T_{J_1} })   \cdots \det(B_{S_{I_k}\cup T_{I_k}, S_{J_k}\cup T_{J_k} })   \ .$$ The right-hand side is well-defined because $B$ is symmetric, so $\det(B_{S_I\cup T_I,S_J\cup T_J}) = \det(B_{S_J\cup T_J,S_I\cup T_I})$.*

**Example 39**. *For $m=2$ we obtain $$\Sigma(B,\{s_1,t_1,s_2,t_2\})= -2\det\left(\begin{array}{cc}b_{s_1s_2}&b_{s_1t_2}\\b_{t_1s_2}&b_{t_1t_2}\end{array}\right).$$ This is exactly the right-hand side of (N2ex). For $m=4$ we obtain $$\begin{aligned}
&\Sigma(B,\{s_1,t_1,s_2,t_2,s_3,t_3,s_4,t_4\})=-2\det\left(\begin{array}{cccc}
b_{s_1s_3}&b_{s_1t_3}&b_{s_1s_4}&b_{s_1t_4}\\
b_{t_1s_3}&b_{t_1t_3}&b_{t_1s_4}&b_{t_1t_4}\\
b_{s_2s_3}&b_{s_2t_3}&b_{s_2s_4}&b_{s_2t_4}\\
b_{t_2s_3}&b_{t_2t_3}&b_{t_2s_4}&b_{t_2t_4}\end{array}\right)\\
&\quad-2\det\left(\begin{array}{cccc}
b_{s_1s_2}&b_{s_1t_2}&b_{s_1s_4}&b_{s_1t_4}\\
b_{t_1s_2}&b_{t_1t_2}&b_{t_1s_4}&b_{t_1t_4}\\
b_{s_3s_2}&b_{s_3t_2}&b_{s_3s_4}&b_{s_3t_4}\\
b_{t_3s_2}&b_{t_3t_2}&b_{t_3s_4}&b_{t_3t_4}\end{array}\right)
-2\det\left(\begin{array}{cccc}
b_{s_1s_2}&b_{s_1t_2}&b_{s_1s_3}&b_{s_1t_3}\\
b_{t_1s_2}&b_{t_1t_2}&b_{t_1s_3}&b_{t_1t_3}\\
b_{s_4s_2}&b_{s_4t_2}&b_{s_4s_3}&b_{s_4t_3}\\
b_{t_4s_2}&b_{t_4t_2}&b_{t_4s_3}&b_{t_4t_3}\end{array}\right)\\
&\quad +8\det\left(\begin{array}{cc}b_{s_1s_2}&b_{s_1t_2}\\b_{t_1s_2}&b_{t_1t_2}\end{array}\right)\det\left(\begin{array}{cc}b_{s_3s_4}&b_{s_3t_4}\\b_{t_3s_4}&b_{t_3t_4}\end{array}\right)+8\det\left(\begin{array}{cc}b_{s_1s_3}&b_{s_1t_3}\\b_{t_1s_3}&b_{t_1t_3}\end{array}\right)\det\left(\begin{array}{cc}b_{s_2s_4}&b_{s_2t_4}\\b_{t_2s_4}&b_{t_2t_4}\end{array}\right)\\
&\quad +8\det\left(\begin{array}{cc}b_{s_1s_4}&b_{s_1t_4}\\b_{t_1s_4}&b_{t_1t_4}\end{array}\right)\det\left(\begin{array}{cc}b_{s_2s_3}&b_{s_2t_3}\\b_{t_2s_3}&b_{t_2t_3}\end{array}\right).
\end{aligned}$$*

## Statement of the theorem for antisymmetrised permanents

**Theorem 40**. *Let $B_{S_m,T_m}$ be as above. If $m$ is odd then $\mathrm{perm}\,B_{[S_m,T_m]}$ vanishes. If $m$ is even, then $$\label{genericPermasSigma} \mathrm{perm}\,B_{[S_m,T_m]} =  \Sigma(B,S_m\cup T_m)\ .$$*

The proof of this theorem is postponed to Section 10.

### Restriction to a specific type

Theorem 40 may be specialised to the cases when the matrices are not generic, by applying a ring homomorphism from ${\mathbb Z}[b_{uv}]$ to another ring. Typically we shall allow the indexing sets $S_{m},T_{m}$ to have repeat indices. When this happens, many determinants in the formula for $\Sigma$ vanish. To express this efficiently, we need some more notation.

**Definition 41**. *Let $\mathcal{E}\subset \{(i,j): 1\leq i\leq j\leq n\}$ be an ordered set of $m$ pairs, and let $I \subset \{1,\ldots, m\}$. Define an ordered tuple with $2|I|$ elements: $$\mathcal{E}_I = ( \mathcal{E}_{i})_{i\in I}\ ,$$ where the elements in each pair $\mathcal{E}_i=(s_i,t_i)$, for $i \in I$, $s_i,t_i\in\{1,\ldots,n\}$, are taken in that order: thus, if $I=\{i_1,\ldots, i_k\}$ in increasing order, then $\mathcal{E}_I=(s_{i_1},t_{i_1},\ldots, s_{i_k},t_{i_k})$.*

If $I$ is a singleton, the notation $\mathcal{E}_i$ is consistent with the usual notation for elements in a set $\mathcal{E}$.

**Example 42**. *Let $n=3$, $m=2$ and let $\mathcal{E}=( (1,2), (2,3))$. Then $\mathcal{D}^1_{2}$ corresponds to $$\mathcal{E}_{\{1\}}\ ,\ \mathcal{E}_{\{2\}}     =   (1,2) \ ,\ (2,3)\ .$$*

*Let $n=5$, $m=4$ and let $\mathcal{E}=( (1,2), (2,3), (3,4), (4,5))$. The three elements of $\mathcal{D}^1_{4}$ correspond to:*

  ----------------------------------------------------- ----- -----------------------------
   *$\mathcal{E}_{\{1,2\}}$ , $\mathcal{E}_{\{3,4\}}$*   *=*   *$(1,2,2,3)$ , $(3,4,4,5)$*
   *$\mathcal{E}_{\{1,3\}}$ , $\mathcal{E}_{\{2,4\}}$*   *=*   *$(1,2,3,4)$ , $(2,3,4,5)$*
   *$\mathcal{E}_{\{1,4\}}$ , $\mathcal{E}_{\{2,3\}}$*   *=*   *$(1,2,4,5)$ , $(2,3,3,4)$*
  ----------------------------------------------------- ----- -----------------------------

*and the three elements of $\mathcal{D}^2_{4}$ correspond to:*

  ------------------------------------------------- ------------------------------------------------- ----- --------------------- -----------------------
   *$\mathcal{E}_{\{1\}}$ , $\mathcal{E}_{\{2\}}$*   *$\mathcal{E}_{\{3\}}$ , $\mathcal{E}_{\{4\}}$*   *=*   *$(1,2)$ , $(2,3)$*  *$(3,4)$ , $(4, 5)$*
   *$\mathcal{E}_{\{1\}}$ , $\mathcal{E}_{\{3\}}$*   *$\mathcal{E}_{\{2\}}$ , $\mathcal{E}_{\{4\}}$*   *=*   *$(1,2)$ , $(3,4)$*  *$(2,3)$ , $(4,5)$*
   *$\mathcal{E}_{\{1\}}$ , $\mathcal{E}_{\{4\}}$*   *$\mathcal{E}_{\{2\}}$ , $\mathcal{E}_{\{3\}}$*   *=*   *$(1,2)$ , $(4,5)$*  *$(2,3)$ , $(3,4)$ ,*
  ------------------------------------------------- ------------------------------------------------- ----- --------------------- -----------------------

*where the vertical bars are merely visual aids and have no mathematical significance.*

**Lemma 43**. *Let $B$ be an $n\times n$ symmetric matrix, and let $\mathcal{E}\subset \{(i,j): 1\leq i\leq j\leq n\}$ denote a set of an even number $m$ of pairs. It follows that with these conventions, for any ordering on $\mathcal{E}$, one has $$\label{Sigmadef1}
\Sigma(B,\mathcal{E}) =  \sum_{k=1}^{m/2}   (-2)^k\,  k! \,     \sum_{  \{\{I_1,J_1\} , \ldots, \{ I_k, J_k\} \} \in \mathcal{D}^k_{m}  }   \det B_{\mathcal{E}_{I_1}, \mathcal{E}_{J_1}} \ldots \det B_{\mathcal{E}_{I_k}, \mathcal{E}_{J_k}}\ .$$ Note that the right-hand side does not depend on the choice of ordering of $\mathcal{E}$.*

*Proof.* This follows from specialisation of the definition of $\Sigma(B,{S_{m}\cup T_{m}}).$ ◻

# Reduction to the symmetric case

We use (eqthm1a) to derive a formula for $\mathrm{tr}\,(B \Upsilon)^{2n-1}$, where both $B$ and $\Upsilon$ are *symmetric* $n\times n$ matrices with entries $B=(b_{ij})$, $b_{ij}=b_{ji}$, and $\Upsilon_{ij}=\Upsilon_{ji}=\omega_{ij}$ for $1\leq i\leq j \leq n$. Applying Corollary 33 leads to a formula for the leading terms of $\mathrm{tr}\,(B \Upsilon)^{2n-1}$ in the form of an antisymmetrised permanent.

## Symmetric Case

The analogue of Proposition 17 gives $$\label{BUpsilonSumoverTypes}
(B \Upsilon)^{2n-1} = \sum_{\nu}  (B\Upsilon_{\nu})^{2n-1}\ ,$$ where the sum is over all types $\nu$ of rank $n$. Note that in this formula $\Upsilon_{\nu}$ contains many more non-zero entries than $\Omega_{\nu}$ since it is symmetric. The terms $(B\Upsilon_{\nu})^{2n-1}$ are typically complicated, but there are many cancellations in the case when $\nu$ contains the diagonal elements $$\label{eqdiag}
\mathrm{diag}_n  = \{ (1,1), (2,2), \ldots, (n,n) \}  \ .$$ We shall say that a type $\nu$ of rank $n$ is *upper-triangular* if $\mathrm{diag}_n \subset \nu$ and furthermore $$\label{nuisUT} \nu \ \subset \  \{(i,j): 1\leq i\leq j\leq n\}  \ .$$

**Theorem 44**. *Let $\nu$ be a type of rank $n$ which is upper-triangular. If $n$ is odd then $$\mathrm{tr}\,\left( (B \Upsilon_{\nu})^{2n-1}\right) =(2n-1) \det(B) \,  \Sigma(B,{\nu}\setminus\mathrm{diag}_n) \, \omega_{\nu} \ .$$ If $n$ is even then $\mathrm{tr}\,\left( (B \Upsilon_{\nu})^{2n-1}\right)$ vanishes.*

**Example 45**. *Let $n=3$. Consider the type $\nu=\{(1,1),(1,2),(2,2), (2,3),(3,3)\}$. Then with $$B =  \begin{pmatrix}
b_{11} & b_{12}  & b_{13}  \\
b_{12} & b_{22} & b_{23}  \\
 b_{13} & b_{23} & b_{33}
\end{pmatrix}  \quad  \hbox{ and } \quad  \Upsilon_{\nu} = \begin{pmatrix}
\omega_{11} & \omega_{12}  & 0  \\
\omega_{12} & \omega_{22} & \omega_{23}  \\
 0 & \omega_{23} & \omega_{33}
\end{pmatrix}$$ Equation (BUpsilonSumoverTypes) provides the formula (see Example 42): $$\mathrm{tr}\,(B\Upsilon_{\nu})^5 =   - 10 \, \det(B)  \det(B_{12,23})\,
 \omega_{11} \wedge \omega_{22} \wedge \omega_{33} \wedge \omega_{12} \wedge \omega_{23},$$ where $\det(B_{12,23})=b_{12} b_{23}  -  b_{13}b_{22}$.*

Theorem 44 only gives a partial description of $(B \Upsilon)^{2n-1}$. It would be interesting, but is not needed for our purposes, to extend Theorem 44 to cover all cases, including when $\nu$ does not contain $\mathrm{diag}_n$.

**Example 46**. *Let $n$ be odd and let $\nu = \mathrm{diag}_n \cup \{12,23,\ldots,(n-1)n\}$. By Example 26, $$\label{w3eq}
\mathrm{tr}\,\left( (B \Upsilon_{\nu})^{2n-1}\right)=(-1)^{\binom{n}2}(2n-1)\det  (B)  \,   \Sigma(B,\{12,23,\ldots,(n-1)n\}) \,
\omega_{11}\wedge\ldots\wedge\omega_{nn}\wedge\omega_{12}\wedge\ldots\wedge\omega_{(n-1)n}\ .$$*

## Proof of Theorem 44

Consider the set of types $\nu$ of rank $n$ with the property: $$\label{nucondition} (i,j) \in \nu  \hbox{ implies that }  (j,i) \notin \nu , \hbox{  whenever  }  i\neq j \ .$$ We say that two such types $\nu_1$, $\nu_2$ are equivalent, denoted by $\nu_1 \sim \nu_2$, if they are equal as sets of unordered pairs $\{i,j\}$, or in other words, for all $1\leq i,j \leq n$: $$(i,j ) \hbox{ or } (j,i)  \in \nu_1       \Longleftrightarrow  (j,i) \hbox{ or } (i,j) \in \nu_2$$ In particular, every type $\nu$ satisfying (nucondition) is equivalent to a unique type satisfying (nuisUT).

We shall work in the differential graded algebra $R^{\mathrm{sym}}$ which is defined to be the quotient of $R$ modulo the ideal generated by the relations $\omega_{ij}=\omega_{ji}$. If $\nu$ satisfies (nucondition), then the following identity holds in $R^{\mathrm{sym}}$. $$\Upsilon_{\nu} = \sum_{\nu' \sim \nu} \Omega_{\nu'} \ ,$$ and consequently, for every $\nu$ satisfying (nuisUT), we have: $$(B\Upsilon_{\nu})^{2n-1} = \sum_{\nu' \sim \nu} (B \Omega_{\nu'})^{2n-1} \ .$$ We deduce from Corollary 33 that $$\mathrm{tr}\,\left( (B\Upsilon_{\nu})^{2n-1}\right) = (2n-1) \det(B) \sum_{\nu' \sim \nu} P_{{\underline{q}}(\nu')-{\underline{1}}, {\underline{p}}(\nu')-{\underline{1}}}(B)  \, \omega_{\nu'} \ .$$

Suppose that $\nu$ contains $\mathrm{diag}_n$. In this case we may write $\nu= \mathrm{diag}_n \cup \mathcal{E}$ as a disjoint union, where $\mathcal{E}= \{(i_1,j_1), \ldots, (i_{n-1},j_{n-1})\}$ with $i_k<j_k$. Then $$P_{{\underline{q}}(\nu')-{\underline{1}}, {\underline{p}}(\nu')-{\underline{1}}} = \mathrm{perm}\,B_{S_{n-1},T_{n-1}} \Big|_{(s_k,t_k) = \mathcal{E}_k}$$ is a specialisation of the generic permanent of indexing sets $S_{n-1}=\{s_1,\ldots, s_{n-1}\}, T_{n-1}=\{t_1,\ldots, t_{n-1}\}$, on setting $s_k=i_k$, $t_k=j_k$ for $1\leq k \leq n-1$. It does not depend on the ordering of elements in $\mathcal{E}$.

Lemma 24 $(vii)$ implies the following identity in $R^{\mathrm{sym}}$: $$\label{omegasignflip} \omega_{\nu'} = -  \omega_{\nu}$$ whenever $\nu'\sim \nu$ is obtained from $\nu$ by replacing a single off-diagonal element $(i,j)$ in $\nu$ with $(j,i)$. Let $G$ be the group of order $2^{n-1}$ generated by the elements $g_i$, for $1\leq i\leq n-1$, which act upon $S_{n-1} \cup T_{n-1}$ by interchanging $s_i$ and $t_i$ and leaving all other elements fixed. Let $\nu= \mathrm{diag}_n \cup \mathcal{E}$ be of the form (nuisUT). Fixing an order on $\mathcal{E}$ we deduce that $$\mathrm{tr}\,\left((B\Upsilon_{\nu})^{2n-1}\right) = (2n-1) \det(B) \left( \sum_{ g \in G }   \chi(g) \, g (  \mathrm{perm}\,B_{S_{n-1},T_{n-1}})\right)\Bigg|_{(s_k,t_k)=\mathcal{E}_k}  \,    \omega_{\nu} \ ,$$ where the term $\chi(g)$ accounts for the sign in (omegasignflip), since the types $\nu'$ equivalent to $\nu$ are in one-to-one correspondence with elements of $G$. The statement follows from Theorem 40 and Lemma 43.

# A formula for the invariant form

In this section, we further specialize to the case when $B=A^{-1}$ and $\Omega=\mathrm{d}A$, where $A$ is a symmetric invertible $n \times n$ matrix, and give a closed formula for the leading terms of $\omega_A^{2n-1}=\mathrm{tr}\,(A^{-1}\mathrm{d}A)^{2n-1}$.

## Notation

Let $M$ be an $n\times n$ matrix. Let $I=(i_1,i_2, \ldots, i_k)$ and $J=(j_1, j_2, \ldots, j_k)$ be $k$-tuples of distinct elements in $\{1,\ldots, n\}$. Let us denote by $$M_{I,J} : \hbox{ the submatrix spanned by rows } I , \hbox{ columns } J.$$ $$M^{I,J} : \hbox{ the matrix obtained from $M$ by deleting  rows } I , \hbox{  and columns } J.$$ We will need a sign convention for ordered subsets of $\{1,\ldots, n\}$.

**Definition 47**. *Let $I= (i_1,\ldots, i_k)$ where $1\leq i_1,\ldots, i_k \leq n$ are distinct. Define $$\sigma(I)=(-1)^{i_1+ \ldots + i_k} \mathrm{sgn}\,\pi_I\ ,$$ where $\pi_I$ is the unique permutation of $I$ such that $\pi(i_1)<  \ldots < \pi(i_k)$ are in increasing order. In the case when $I$ has repeat indices, we define $\sigma(I)=0$.*

The following lemma is a reformulation of an identity due to Jacobi (see, e.g., Lemma 28 in [@PeriodsFeynman]) and, crucially, enables one to remove all occurrences of the inverse matrix in our formulae.

**Lemma 48**. *Let $A$ be an invertible $n\times n$ matrix and $I$, $J$ as above. $$\label{deteqgen}
\det\,(A^{-1})_{I,J}=\frac{\sigma(I)\sigma(J)}{\det A}\det A^{J,I}.$$*

**Theorem 49**. *Let $A=(a_{ij})$ be a symmetric, invertible $n\times n$ matrix. If $n=m+1$ is odd, then $$\begin{gathered}
\label{formula2A}
\omega_A^{2n-1}=(2n-1)\sum_{\genfrac{}{}{0pt}{}{\mathcal{E}\subseteq\{(i,j): 1\leq i<j\leq n\}}{|\mathcal{E}|=m}}\sum_{k=1}^{m/2} (-2)^k k! \, \frac{ Q_k(A,\mathcal{E})}{\det (A)^{k+1}}\; \omega_{\mathrm{diag}_n\cup\mathcal{E}}(A) \\
+ \left(\text{terms of degree } <n \hbox{ in }\mathrm{d}a_{11},\mathrm{d}a_{22},\ldots,\mathrm{d}a_{nn}\right),
\end{gathered}$$*

*where $\omega_{\nu}(A)$ is defined to be $\omega_{\nu}\big|_{\Omega=\mathrm{d}A}$ for any type $\nu$, and $Q_k(A,\mathcal{E})\in{\mathbb Z}[a_{ij}]$ are the polynomials: $$\label{Qdef}
Q_k(A,\mathcal{E})= \sum_{  \{\{I_1,J_1\} , \ldots, \{ I_k, J_k\} \} \in \mathcal{D}^k_{m}  }  \prod_{i=1}^k\sigma(\mathcal{E}_{I_i})\sigma(\mathcal{E}_{J_i})\det A^{\mathcal{E}_{I_i},\mathcal{E}_{J_i}}.$$ If $n$ is even then all terms in $\omega_A^{2n-1}$ are of degree $<n$ in $\mathrm{d}a_{11},\ldots,\mathrm{d}a_{nn}$.*

*Proof.* After using ((BUpsilonSumoverTypes)) we specialise Theorem 44 to the case $B=A^{-1}$ and $\Omega=\mathrm{d}A$. The result follows from substituting ((deteqgen)) in ((Sigmadef1)) and the fact that $\det A^{\mathcal{E}_{J_i},\mathcal{E}_{I_i}}=\det A^{\mathcal{E}_{I_i},\mathcal{E}_{J_i}}$ since $A$ is symmetric. ◻

The point of Theorem 49 is that $\omega_A^{2n-1}$ is expressed in terms of determinants of co-factors of $A$ without use of its inverse. The polynomials $Q_k(A,\mathcal{E})$ may be computed quite efficiently.

# The invariant form of a graph Laplacian

Let $G$ be a finite connected graph. The invariant forms $\omega^{2n-1}_{\Lambda_G} = \mathrm{tr}\,(\Lambda_G^{-1} \mathrm{d}\Lambda_G)^{2n-1}$ do not, of course, depend on the choice of graph Laplacian $\Lambda_G$, but the formulae we have derived above, do. For this reason there is much to gain by choosing a particularly simple form for $\Lambda_G$.

To this end, suppose that $h_G=n$ and choose a spanning tree $T$ in $G$. It is well-known that there exist closed cycles $c_1,\ldots, c_n \in {\mathbb Z}^{E_G}$ whose images in $H_1(G;{\mathbb Z})$ are independent, with the property that $c_i$ meets the complement of $T$ in a single edge which we denote by $e_i$, for $i=1,\ldots, n$. The graph Laplacian with respect to this basis of $H_1(G;{\mathbb Z})$ has the property that the variables $x_i$ corresponding to edge $e_i$ for $i=1,\ldots,n$ occur exactly once in the matrix, with $x_i$ in the $i^{\mathrm{th}}$ row and column.

We may assume that $G$ has $2n$ edges (otherwise the corresponding invariant form vanishes). Let $T\subset G$ be a spanning tree, and choose any edge in $T$ which we may assume is numbered $2n$. Let $\Lambda_G(T)$ denote a choice of graph Laplacian, as above, in which we set $x_{2n}=1$. Since the invariant form $\omega^{2n-1}_G$ is projective, it is uniquely determined by restriction to the affine chart $x_{2n}=1$. Since it is proportional to $\mathrm{d}x_{1}\wedge \ldots \wedge \mathrm{d}x_{2n-1}$, the 'lower order terms' in Theorem 49 vanish.

**Theorem 50**. *Let $G$ be a finite connected graph with $n=h_G$ independent cycles and $2n$ edges. Let $T$ be a spanning tree in $G$ and $\Lambda_G(T)$ a choice of graph Laplacian as above. If $n=m-1$ is odd, then $$\begin{aligned}
\label{formula2}
\omega_G^{2n-1}&=(2n-1)\sum_{\genfrac{}{}{0pt}{}{\mathcal{E}\subseteq\{(i,j): 1\leq i<j\leq n\}}{|\mathcal{E}|=m}}\sum_{k=1}^{m/2}  (-2)^k k!\, \frac{ Q_k(\Lambda_G(T),\mathcal{E})}{\Psi_G^{k+1}}\;\omega_{\mathrm{diag}_n \cup \mathcal{E}} (\mathrm{d}\Lambda_G(T)),\quad\text{where}\nonumber\\
&\quad
Q_k(\Lambda_G(T),\mathcal{E})= \sum_{  \{\{I_1,J_1\} , \ldots, \{ I_k, J_k\} \} \in \mathcal{D}^k_{m}  }  \prod_{i=1}^k\sigma(\mathcal{E}_{I_i})\sigma(\mathcal{E}_{J_i})\det \Lambda_G(T)^{\mathcal{E}_{I_i},\mathcal{E}_{J_i}}.
\end{aligned}$$ If $n$ is even then $\omega_G^{2n-1}=0$.*

*Proof.* Substitute $A = \Lambda_G(T)$ into Theorem 49. Note that $\det\Lambda_G(T)=\Psi_G$ is the graph polynomial. ◻

**Remark 51**. *In practice it seems beneficial to choose a tree $T$ with many leaves.*

**Example 52**. *For the wheel with $n$ spokes $W_n$, choose $T$ to be the spokes numbered from $n+1, \ldots, 2n$ in cyclic order. The spoke $n+i$ meets edges $i$ and $i+1$ (mod $n$) from the rim. Every consecutive pair of spokes, together with a unique edge in the rim, forms a triangle, which we orient counter-clockwise and take as our cycle basis. We obtain the matrix ((introLambdaW)) for $\Lambda_{W_n}(T)$ and set $x_{2n}=1$.*

*We shall assume that $n$ is odd. By inspection of this matrix, one verifies that there is a unique subset $\mathcal{E}\subset \{(i,j): 1\leq i<j\leq n\}$ such that $\omega_{\mathrm{diag}_n\cup\mathcal{E}}(\mathrm{d}\Lambda_{W_n}(T))$ is non-zero, namely $$\mathcal{E}=\{(1,2) \ , \ (2,3) \ , \ \ldots, \ (n-1,n)\} \ .$$ Because $\mathcal{E}$ consists of consecutive pairs, one checks that either $\sigma(\mathcal{E}_{I_i})=\sigma(\mathcal{E}_{J_i})=(-1)^{|I_i|}$ or vanishes (in the case when $\mathcal{E}_{I_i}$ has repeated elements) for all the terms occurring in (formula2). By ((oWn)), we have $$\omega_{\mathrm{diag}\cup\mathcal{E}}  (\mathrm{d}\Lambda_{W_n}(T))=(-1)^{\binom{n}2}\mathrm{d}x_1\wedge\ldots\wedge\mathrm{d}x_n\wedge(-\mathrm{d}x_{n+1})\wedge\ldots\wedge(-\mathrm{d}x_{2n-1})=(-1)^{\binom{n}2}\mathrm{d}x_1\wedge\ldots\wedge\mathrm{d}x_{2n-1},$$ where we reduced (by antisymmetry) the terms $\mathrm{d}x_i+\mathrm{d}x_{n+i-1}+\mathrm{d}x_{n+i}$ on the diagonal of $\mathrm{d}\Lambda_{W_n}$ to $\mathrm{d}x_i$. The sum over $I_i$, $J_i$ in ((formula2)) can be restricted to sets $\mathcal{E}_{I_i}, \mathcal{E}_{J_j}$ with distinct elements which considerably reduces the number of terms in the formula. Examples for $I_i$ and $J_i$ are in Example 42.*

## Example: the wheel with 5 spokes {#sect: 5spokes}

Let $n=5$. As is the case for all wheel graphs, the first sum of (formula2) reduces to a single term $\mathcal{E}= \{(1,2),(2,3),(3,4),(4,5)\}$. There are a priori 6 terms occurring in the formula, corresponding to the 3 terms in $\mathcal{D}^1_4$ and $\mathcal{D}^2_4$ (Example 37). With the above ordering on the elements of $\mathcal{E}$, we obtain the six products of determinants corresponding to the terms in Example 42. The first and third involve repeated indices, and therefore vanish, leaving only one term from $\mathcal{D}^1_4$: $$\det \left(\Lambda_{W_5}^{1234, 2345} \right) = (\Lambda_{W_5})_{5,1} =-1  \ .$$ The three terms coming from $\mathcal{D}^2_4$ are all equal: $$\begin{aligned}
\det \left(\Lambda_{W_5}^{12,23}\right)  \det \left( \Lambda_{W_5}^{34,45} \right)
&= &
\begin{vmatrix}
    0 & -x_8 &  0 \\
    0 &x_4+x_8+ x_9 & -x_9 \\
    -1 & -x_9 & x_5+ x_9 +1
\end{vmatrix}
\begin{vmatrix}
    x_1 +x_6 +1  & -x_6 &  0 \\
     - x_6 &x_2+x_6+ x_7 & -x_7 \\
    -1 & 0 & 0
\end{vmatrix} \\
& = &  x_6x_7x_8 \nonumber
x_9\ ,\\
\det  \left( \Lambda_{W_5}^{12,34} \right) \det  \left(\Lambda_{W_5}^{23,45} \right)&=& x_6x_7x_8
x_9\ ,\qquad
\det  \left(\Lambda_{W_5}^{12,45} \right) \det \left(\Lambda_{W_5}^{23, 34}\right)\;=\; x_6x_7x_8
x_9\ .
\end{aligned}$$ Taking all contributions together gives $$\omega^9_{W_5} \big|_{x_{10}=1} = \left( 18 \, \frac{1} {\Psi^2_{W_5}} +   216 \, \frac{x_6x_7x_8x_9x_{10}}{\Psi_{W_5}^3} \right)\Bigg|_{x_{10}=1} \mathrm{d}x_1 \wedge \ldots \wedge \mathrm{d}x_9 \ ,$$ in agreement with [@BrSigma].

## Remarks on convergence and MZVs

Each monomial $M(x)$ in $Q_k(\Lambda_G(T),\mathcal{E})$ provides the parametric representation $M(x)/\Psi^{k+1}$ of a graphical function $f_{G(M)}^{(k)}$ in $2k+2$ dimensions [@schnetz2014graphical; @GolzPanzerSchnetz; @BorinskySchnetz] whose underlying graph is $G$ but with differing edge weights. An exponent $k-1,k-2,\ldots,0$ of $x_i$ in the homogenisation of $M(x)$ corresponds to an edge-weight $1/k, 2/k,\ldots, 1$ of the edge associated to $x_i$.

**Remark 53**. *It was shown in [@BrSigma] that $\omega_G^{2n-1}$ is convergent. In fact, very extensive numerical evidence suggests a much stronger statement: for every monomial $M(x)$ in $Q_k(\Lambda_G(T),\mathcal{E})$ the graphical function $f_{G(M)}^{(k)}$ is convergent. In particular, we expect that $Q_1(T)=0$ if the graph $G$ has a sub-divergence in four spacetime dimensions (i.e. $G$ is not primitive).*

**Theorem 54**. *Let $G$ be a *constructible* graph with $n$ independent cycles and $2n$ edges. Suppose that $f_{G(M)}^{(k)}$ is indeed convergent for every monomial $M(x)$. Then $I_G(\omega^{2n-1})$ is a multiple zeta value (MZV).*

*Proof.* In Theorem 45 of [@BorinskySchnetz] it is proved (using Theorem 93 of [@schnetz2021generalized]) that any period of a constructible graph in even dimensions $\geq4$ is an MZV. ◻

**Remark 55**. *It is expected that Theorem 54 holds unconditionally after regularizing graphical functions to deal with divergent terms, for instance in dimensional regularization [@Schnetznumfunct; @7loops]. Experiments confirm that all Laurent coefficients in the regulator $\epsilon$ for constructible graphs with subdivergences are MZVs, and the poles in $\epsilon$ cancel after taking the sum of all terms, leaving a finite part equal to the canonical integral.*

# Restriction to wheel cycles and proof of main theorem

Henceforth let $G=W_n$ be the wheel with $n$ spokes. We use the set of spokes, labelled $n+1,\ldots, 2n$ as a spanning tree $T$, and label the edges of the rim $1,\ldots,n$ as in the previous section. The graph Laplacian will be the matrix ((introLambdaW)). Denote the product of all spokes by $$\label{Sdef}
S(x)=\prod_{r=1}^nx_{n+r}\ .$$

## Calculation of the wheel integrands

**Lemma 56**. *Let $I,J\subseteq\{(1,2) ,(2,3) ,\ldots,(n-1,n)\}$ be two disjoint non-empty sets with $|I|=|J|=p$ elements. The sets $I,J$ may be ordered as follows: $$I=\{(i_1, i_1+1),\ldots, (i_p,i_p+1)\} \ , \   J=\{(j_1, j_1+1),\ldots,(j_p, j_p+1)\}\ ,$$ where $i_1<\ldots<i_p$, $j_1<\ldots<j_p$. By interchanging $I$ and $J$ if necessary, we may assume that $i_1<j_1$.*

*In the notation of Example 52 we have $$\label{detLeq}
\det\Lambda_{W_n}(T)^{I,J}=\left\{\begin{array}{cl}-\frac{S(x)}{\prod_{k=1}^px_{n+i_k}x_{n+j_k}}&\text{, if }i_1<j_1<i_2<j_2<\ldots<i_p<j_p,\\
0&\text{, otherwise.}\end{array}\right.$$ In other words, the determinant is non-zero if and only if the sets $I,J$ are interlaced.*

*Proof.* Consider the matrix $L=\Lambda_{W_n}(T)$ as given in ((introLambdaW)) (a worked example is in Section 7.1). If one deletes the two consecutive rows $i_1,i_1+1$, then column $i_1+1$ contains a unique non-zero entry $-x_{n+i_1+1}$ in row $i_1+2$ (henceforth, the numbering of rows and columns refer to the numbering in the matrix $L$, even when we consider minors of $L$ obtained by deleting rows and columns). If $j_1>i_1+1$, then this column occurs in $L^{I,J}$ and we may perform an expansion of $\det(L^{I,J})$ with respect to column $i_1+1$. We obtain a factor $x_{n+i_1+1}$ multiplied by the determinant of $L^{I\cup (i_1+2),J\cup (i_1+1)}$. Now, in column $i_1+2$ the only non-zero entry is $-x_{n+i_1+2}$ in row $i_1+3$. We continue expanding the determinant along columns in this manner until the first entry $(i_1+k+1,i_1+k)$ is not in the matrix $L^{I,J}$. There are two ways this may happen. The first is if $i_1+k+1 \in I$, which implies that $i_2=i_1+k+1$. In this case, column $i_1+k+1$ is zero in $L^{I,J}$ and $\det L^{I,J}=0$. Let us assume that this does not occur. The second is if $i_1+k \in J$ which, having ruled out the first situation, therefore implies that $j_1=i_1+k$ and hence $j_1<i_2$. The expansion of the determinant $\det(L^{I,J})$ has so far produced a factor $x_{n+i_1+1}\ldots x_{n+j_1-1}$ (which is $1$ if $j_1=i_1+1$) obtained by multiplying elements immediately under the diagonal. We continue to expand the determinant, this time by removing the pair of consecutive columns $j_1,j_1+1$ and expanding along row $j_1+1$. This either gives zero (if $i_2\geq j_2$) or gives a factor $x_{n+j_1+1}\ldots x_{n+i_2-1}$ obtained by multiplying elements of $L$ which lie above the diagonal. Continue in this manner (in both directions as there may be entries above the rows we have eliminated first if $i_1\geq2$), alternately multiplying consecutive sequences along the lines immediately above and below the diagonal. We find that the determinant vanishes if the sets $I,J$ do not interlace, and in the case that they do, we are left eventually with the $1\times1$ matrix $(-x_{2n})$. Altogether we obtain the product of all $x_{n+r}$, for $r=1, \ldots, n$ except for $r=i_k, j_k$, where $k=1,\ldots,p$. A careful analysis of the signs yields an overall minus sign in ((detLeq)) which comes from $\det((-x_{2n}))$. ◻

The interlacing sets $I,J$ corresponding to non-vanishing determinants in the previous lemma are in one-to-one correspondence with subsets $K$ of $\{1,2,\ldots, n-1 \}$ with $2p$ elements $\{i_1,j_1,\ldots, i_p, j_p\}$. Conversely, to any such set $K = \{k_1,\ldots, k_{2p}\}$ with $k_1<k_2<\ldots< k_{2p}$ we can associate $$I_K = \{ (k_1, k_1+1), \ldots, (k_{2p-1}, k_{2p-1}+1)\}   \qquad \hbox{ and } \qquad   J_K = \{ (k_2, k_2+1), \ldots, (k_{2p}, k_{2p}+1)\} \ .$$ The corresponding determinant is simply $$\label{detminorforK} \det\Lambda_{W_n}(T)^{I_K,J_K} = -\frac{S(x)}{\prod_{k\in K}x_{n+k} } \ .$$

**Lemma 57**. *Let $G=W_n$ and $T$ as above, where $n=m+1$ is odd. In the notation of Theorem 50 we have $$\label{sumprodeq}
Q_k(\Lambda_{W_n}(T),\mathcal{E})=(-1)^k \frac{c_{m,k}}{k!} S(x)^{k-1}x_{2n}\ ,$$ where $$\label{sumprodeq2}
c_{m,k}=\sum_{\genfrac{}{}{0pt}{}{p_1,\ldots,p_k \geq1}{\sum_i 2p_i=m}} \binom{m}{2p_1, 2p_2,\ldots, 2p_k}=\sum_{\genfrac{}{}{0pt}{}{p_1,\ldots,p_k \geq1}{\sum_i 2p_i=m}}\frac{ m!}{\prod_{i=1}^k (2p_i)!} \ .$$*

*Proof.* Recall that $\mathcal{E}= \{(1,2), (2,3), \ldots, (n-1,n)\}.$ By Lemma 56 and the discussion which follows, the sets $\{\{I_1,J_1\}, \ldots, \{I_k, J_k\}\}$ in $\mathcal{D}^k_{m}$ which give rise to non-zero determinants $\det \Lambda_{W_n}^{\mathcal{E}_{I_i}, \mathcal{E}_{J_i}}$ are in one-to-one correspondence with disjoint unions $$\label{inproofKunion} \{1,2,\ldots, n-1\} = K_1 \cup K_2 \cup \ldots \cup K_{k}\ ,$$ where each $K_i$ has an even number of elements. The set $K_i$ is given by the initial entries of all elements of $\mathcal{E}_{I_i}$ and $\mathcal{E}_{J_i}$. By (detminorforK) we have $$\prod_{i=1}^k \det \Lambda_{W_n}^{\mathcal{E}_{I_i}, \mathcal{E}_{J_i}}    =  \prod_{i=1}^k \frac{(-S(x))}{\prod_{k_i\in K_i}x_{n+k_i}}=(-1)^k S(x)^{k-1}x_{2n}\ .$$

By Example 52, $\sigma(I_i)=\sigma(J_i)=(-1)^{|I_i|}$. Therefore the calculation of $Q_\lambda(\Lambda_{W_n}(T),\mathcal{E})$ reduces to counting the number of ways of writing $\{1,\ldots, m\}$ as an unordered disjoint union of $k$ sets of size $2p_1,\ldots, 2p_k$. This is simply given by $1/k!$ times a multinomial coefficient: $$\frac{1}{k!}  \binom{m}{2p_1,\ldots, 2p_k} =  \frac{1}{k!} \frac{m!}{(2p_1)! \ldots (2p_k)!} \ .$$ The result follows. ◻

**Corollary 58**. *We deduce that for $n=m+1$ odd, $$\omega_{W_n}^{2n-1}\big|_{x_{2n}=1} = (-1)^{m/2}(2n-1) \sum_{k=1}^{m/2}2^kc_{m,k}\frac{S(x)^{k-1}}{\Psi^{k+1}_{W_n}} \, \mathrm{d}x_1\wedge \ldots \wedge \mathrm{d}x_{2n-1}\ .$$ In particular, $(-1)^{m/2}\omega_{W_n}^{2n-1}$ is positive and the canonical integral $I_{W_n}$ is non-zero.*

*Proof.* Substitute ((oWn)) and ((sumprodeq)) into Equation ((formula2)). ◻

## The coefficients $c_{m,k}$

The coefficients $c_{m,k}$ count the number of ordered partitions of a set of size $m$ into $k$ subsets, each of which has a positive even number of elements.

**Lemma 59**. *Let $m\geq2$ be even. Then $$\label{ceq1}
c_{m,k}  =    \frac{2}{2^k}   \sum_{r=1}^k (-1)^{k-r} \binom{2k}{k-r} r^{m}  \ .$$*

*Proof.* Consider the exponential generating series $$C_k(x)= \sum_{m\geq0\;\text{even}} \frac{c_{m,k}}{m!} x^m\ .$$ By definition of $c_{m,k}$ and multiplicative properties of exponential generating series, one has $$C_k(x) = C_1(x)^k \ .$$ Since $c_{0,1}=0$ and $c_{m,1}=1$ for $m\geq2$ we have $$C_1(x) = \frac{e^x + e^{-x}}{2} -1 =   \frac{1}{2} (e^{x} -1)^2 \, e^{-x}\ .$$ The following identity follows from rearranging the terms in the binomial theorem: $$\left(y-1\right)^{2k} y^{-k} =(-1)^{k} \binom{2k}{k} +   \sum_{r=1}^k (-1)^{k-r} \binom{2k}{k-r}(y^r+y^{-r})\ .$$ Applying it with $y=e^x$ gives $$2^k  C_k(x) =     (e^{x} -1)^{2k} \, e^{-kx} = (-1)^{k} \binom{2k}{k} +   \sum_{r=1}^k (-1)^{k-r} \binom{2k}{k-r}(e^{rx}+e^{-rx})\ .$$ Reading off the coefficient of the term $x^m$ gives the stated formula. ◻

**Example 60**. *For all even $m\geq 2$ we have $c_{m,1}=1$ and $$c_{m,2} = \frac{2^m}{2}-2\   \qquad  , \qquad  \ c_{m,3}= \frac{3^m}{4} -3 \frac{2^m}{2}+ \frac{15}{4}\  .$$*

## Edge-weighted Feynman integrals for wheel graphs

The calculations above imply that the canonical wheel integrals are linear combinations of Feynman integrals for graphs with weighted edges.

**Definition 61**. *Let $G$ be a finite connected graph with a choice of weighting $\nu_e>0$, for every edge $e\in E_G$. Define an associated Feynman integral for $\lambda\in{\mathbb R}$, whenever it converges, by $$\label{pareq}
P_G=\frac{\Gamma(\lambda+1)}{\prod_e\Gamma(\lambda\nu_e)}\int_{\sigma_G} \Omega_G\,\frac{\prod_ex_e^{\lambda(1-\nu_e)}}{\Psi_G^{\lambda+1}}\ ,$$ where $\Psi_G$ is the graph polynomial of $G$, $\sigma_G$ is the positive coordinate simplex, and $$\Omega_G=\sum_{i=1}^{|E_G|}(-1)^ix_i\mathrm{d}x_1\wedge\ldots\wedge\widehat{\mathrm{d}x_i}\wedge\ldots\wedge\mathrm{d}x_{|E_G|}\ .$$*

This definition is equivalent to that of the weighted period of a graph in $2\lambda+2$ dimensions in [@BorinskySchnetz] by applying the change of variables $x_e \mapsto x_e^{-1}.$

Let $W_{n,2\lambda+2}$ denote the edge-weighted wheel graph with $n$ spokes $W_n$, where the edges along the rim have weight $1$, and the spokes have weight $\lambda^{-1}$. A formula for $P_{W_m,2k+2}$ is derived in [@BorinskySchnetz], using the fact that the dimension of the corresponding Feynman integrals are $2k+2$, which is even.

**Theorem 62**. *If $1\leq k\leq n-2$, the Feynman period $P_{W_n,2k+2}$ of the weighted wheel with $n$ spokes is $$\label{PWeq}
P_{W_{n,2k+2}}=\frac{\genfrac(){0pt}{}{2n-2}{n-1}}{(2k-1)!(k-1)!^{n-1}}\sum_{r=1}^\infty\frac{\prod_{\ell=1}^{k-1}(r^2-\ell^2)}{r^{2n-3}} \ .$$*

*Proof.* This is in Example 87 of [@BorinskySchnetz]. ◻

**Corollary 63**. *Let $n=m+1$ be odd. Then the canonical wheel integral is a linear combination of edge-weighted Feynman integrals, $$\label{IWeq}
I_{W_n}=(2n-1)\sum_{k=1}^{m/2}\frac{2^kc_{m,k}(k-1)!^n}{k!}P_{W_n,2k +2}\ .$$*

*Proof.* This follows from Corollary 58 and the definition of $P_{W_n,2k+2}$, upon restricting the integrand to the affine chart $x_{2n}=1$. Note that the prefactor in front of the integral ((pareq)) for $P_{W_n,2k +2}$ is $k!/(k-1)!^n$. By definition we orient the domain of integration such that $I_{W_n}\geq0$. ◻

## Completing the proof

**Lemma 64**. *Let us set $p_0(x)=1$, $p_2(x)= x^2-1$, $p_4(x)=(x^2-1)(x^2-4)$, and $$p_{2k}(x) =\prod^{k}_{\ell=1} (x^2-\ell^2) \ .$$ Let $m\geq2$ be even. Then $$\label{psasxs} \sum_{k=1}^{m/2}  \frac{2^k}{(2k)!} c_{m,k}\, p_{2k-2}(x) = x^{m-2} \ .$$*

*Proof.* Let $m=2\mu$, $\mu\geq1$. The set of polynomials $p_{2k}$ for $k\geq 0$ form a basis for the free ${\mathbb Z}$-module ${\mathbb Z}[x^2]$. Therefore there exist unique integers $t_{\mu,k}$ such that $$\sum_{k=1}^{\mu}  t_{\mu,k} p_{2k-2} = x^{2\mu-2}\ .$$ The matrix $T=(t_{\mu,k})$ satisfies $T (p_0,p_2,\ldots,p^{2k},\ldots )^T = (1,x^2,x^4,\ldots , x^{2k},\ldots)^T$, viz: $$T=  \begin{pmatrix} t_{1,1}  &   & &  &\\ t_{2,1} & t_{2,2} &  & &&   \\ t_{3,1} & t_{3,2} & t_{3,3}  & &&  \\   t_{4,1} & t_{4,2} & t_{4,3} & t_{4,4}  & &\\
    t_{5,1} &   t_{5,2} & t_{5,3} &  t_{5,4} &   t_{5,5} &\\
    t_{6,1} &   t_{6,2} &  t_{6,3} &  t_{6,4} &  t_{6,5} &  t_{6,6}  \\
    \vdots & & & & & &  \ddots
    \end{pmatrix}  = \begin{pmatrix} 1  & & & &  &\\ 1& 1 &  & &&   \\ 1& 5 & 1  & &&  \\   1 & 21 & 14 & 1  & &\\
    1 &   85 & 147 &  30 &   1 &\\
    1 &   341 &  1408 &  627 &  55 &  1 \\
      \vdots & & & & & &  \ddots
    \end{pmatrix}\ .$$ The numbers $t_{\mu,k}$ are known as the central factorial numbers with closed formula $2^k/(2k)!$ times (ceq1) [@Sloane], A036969. ◻

**Theorem 65**. *Let $n\geq3$ be an odd integer. Then $$\label{IWeq3}
I_{W_n}=n\genfrac(){0pt}{}{2n}{n}\zeta(n).$$*

*Proof.* Let $n=m+1$ be odd. Since $n\geq3$, $m/2 \leq n-2$, and Theorem 62 applies. Corollary 63 yields $$\begin{aligned}
I_{W_n} & = & (2n-1)\sum_{k=1}^{m/2} \frac{2^kc_{m,k}\genfrac(){0pt}{}{2n-2}{n-1}}{(2k-1)!k}\sum_{r=1}^\infty\frac{\prod_{\ell=1}^{k-1}(r^2-\ell^2)}{r^{2n-3}}\\
&=& (2n-1)\binom{2n-2}{n-1}  \sum_{r=1}^\infty \frac{1}{r^{2n-3}}  \sum_{k=1}^{m/2}\frac{2^{k+1}c_{m,k}}{(2k)!} p_{2k-2}(r)
=n\genfrac(){0pt}{}{2n}{n}\sum_{r=1}^\infty\frac{r^{m-2}}{r^{2n-3}}
=n\genfrac(){0pt}{}{2n}{n}\zeta(n)\ ,
\end{aligned}$$ where we have used (psasxs). ◻

# An identity for $(B \Omega)^{2n-1}$.

Let $B$, $\Omega$ be $n\times n$ matrices of $0$ and $1$-forms respectively, and set $$\label{Xdef}
X(B,\Omega) =  (B \Omega)^{2n-1} \ .$$ Employing the same notations as in Section 3.1, we denote by $$\label{Ydef}
Y(B,\Omega)=\sum_{\genfrac{}{}{0pt}{}{\nu\subseteq \{(i,j): 1\leq i, j \leq n\}}{|\nu|=2n-1}}\Phi_{\nu}(B)\,\omega_\nu \ ,$$ where $\omega_{\nu}$ was defined in Definition 21 in the case of the generic matrix $\Omega_{ij}=(\omega_{ij})$. In general it is defined to be the corresponding exterior product of 1-forms in the entries $\Omega_{ij}$ of $\Omega$. In this section we prove that $X(B, \Omega) = \det(B)\, Y(B,\Omega)$. The strategy is first to establish equality in the case when $B=I_n$ is the identity matrix, and then use covariance properties of both $X(B,\Omega)$ and $Y(B,\Omega)$ with respect to $B, \Omega$ to deduce the identity for all $B$.

## Properties of $X(B,\Omega)$

### Weights and types

In this subsection we derive a structural result for $X(B,\Omega)$ from first principles, which will not be required for our later results, but may be of conceptual value to the reader.

From the definition ((Xdef)) it is evident that for any invertible matrices $A_1,A_2\in\mathrm{GL}_n(R^0)$ we have $$\label{bicov}
X(A_1BA_2,A_2^{-1}\Omega A_1^{-1})=A_1X(B,\Omega)A_1^{-1}\ .$$ Let us specialise ((bicov)) to the case when $A_1=D_1$ is diagonal with entries $\lambda_1,\ldots, \lambda_n$, and $A_2=D_2$ is diagonal with entries $\mu_1,\ldots, \mu_n$. The action $B \mapsto D_1 B D_2$ (resp. $\Omega\mapsto D_2^{-1} \Omega D_1^{-1}$) defines an action of $\mathbb{G}_m^n \times \mathbb{G}^n_m$ on ${\mathbb Z}[b_{ij}]$ given by $b_{ij} \mapsto  \lambda_i b_{ij} \mu_j$ (resp. on the differential graded algebra $R$ defined in Section 3.1.2 via $\omega_{ij} \mapsto \mu_i^{-1} \omega_{ij} \lambda^{-1}_j$.) Decompose $X(B,\Omega)$ by type (see Definition 21) $$\label{Xdecomp}
X(B,\Omega) =  \sum_{\nu}  F_{\nu}(B)\,\eta_{\nu}\ ,$$ where $F_{\nu}(B)\in M_{n\times n}({\mathbb Z}[b_{ij}])$, and $\nu$ ranges over all types of rank $n$. As in Section 3.2, denote its weights by $w(\nu) = ({\underline{p}}(\nu), {\underline{q}}(\nu))$. If we assign to $b_{ij}$ the multi-degree $({\underline{e}}_i,{\underline{e}}_j)$, it follows from (bicov) that the $(k,\ell)$th entry $(F_{\nu}(B))_{k, \ell} \in {\mathbb Z}[b_{ij}]$ necessarily has multi-degrees $({\underline{q}}(\nu)+{\underline{e}}_k-{\underline{e}}_{\ell}, {\underline{p}}(\nu))$ (see Example 32 where $\det B$ has multi-degree $({\underline{1}},{\underline{1}})$).

### Factorisation of the determinant

**Lemma 66**. *All entries of the matrix $X(B,\Omega)$ have a factor of $\det(B)$. Thus we may write: $$\label{detB}
X(B,\Omega)=(\det B) X'(B,\Omega)$$ for some matrix $X'(B,\Omega)$ of $(2n-1)$-forms whose coefficients are homogeneous polynomials in ${\mathbb Z}[b_{ij}]$ of total degree $n-1$.*

*Proof.* Write $X(B,\Omega)= \sum_{\nu} F_{\nu}(B)\, \eta_{\nu}$ as above. It suffices to show that $X(B,\Omega)$ vanishes if $\det(B)=0$, since in that case each $F_{\nu}(B) \in {\mathbb Z}[b_{ij}]$ is a polynomial which vanishes whenever $\det(B)$ vanishes. It is therefore divisible by $\det(B)$, using the well-known fact that $\det(B)$ is irreducible (this follows easily from the fact that the determinant is of degree at most one in each entry of $B$). Now observe that if $\det(B)$ vanishes, then the matrix $B$, and hence $B\Omega$, has rank $m<n$. It follows from Proposition 15 that *a fortiori* $(B\Omega)^{2m}=0$ and hence $X(B, \Omega)=0$. ◻

**Corollary 67**. *If we write the coefficients in (Xdecomp) in the form $F_{\nu}(B) = \det(B) f_{\nu}(B)$, then it follows that $f_{\nu}(B) \in {\mathbb Z}[b_{ij}]$ has multi-degree $({\underline{q}}(\nu)- {\underline{1}}+ e_k-e_{\ell}, {\underline{p}}(\nu)-{\underline{1}}).$ Naturally, if one of these degrees is negative, then $f_{\nu}(B)$ must vanish.*

### Elementary transformations

We consider the behaviour of $Y(B,\Omega)$ with respect to the action of elementary transformations $T_{ij}=I_n+E_{ij}$, where $(E_{ij})_{ab}=\delta_{a,i}\delta_{b,j}$ are elementary matrices.

**Lemma 68**. *Let ${\underline{p}}= (p_1,\ldots, p_n)$ and ${\underline{q}}=(q_1,\ldots, q_n)$, where $p_i,q_i \geq 0$ such that $\sum_{i=1}^n p_i = \sum_{i=1}^n q_i$. Let $i,j\in \{1,\ldots n\}$. With notations as in Section 3.1 we have $$\label{PTij}
P_{{\underline{p}},{\underline{q}}}(BT_{ij})=\sum_{k=0}^{q_j}\genfrac(){0pt}{}{q_j}{k}P_{{\underline{p}},{\underline{q}}+k({\underline{e}}_i-{\underline{e}}_j)}(B)\ .$$*

*Proof.* Right multiplication $B \mapsto B T_{ij}$ adds column $i$ to column $j$ in $B$. It follows that $(BT_{ij})_{S_{\underline{p}}, S_{\underline{q}}}$ has a copy of the column of $B$ indexed by $i$ added to all $q_j$ columns indexed by $j$. Since the permanent is invariant under permutations of columns, it suffices to consider the permanent of a matrix with column vectors $(\underline{a} , \ldots, \underline{a}, \underline{c}_1, \ldots, \underline{c}_r)$, where $\underline{a}$ occurs with multiplicity $q$. By multilinearity of the permanent, $$\mathrm{perm}\,( \underbrace{\underline{a} +\underline{b}, \ldots,  \underline{a}+\underline{b}}_q, \underline{c}_1, \ldots, \underline{c_r})  = \sum_{k=0}^q \binom{q}{k}   \mathrm{perm}\,( \underbrace{\underline{a} , \ldots,  \underline{a}}_k, \underbrace{ \underline{b} ,\ldots,   \underline{b}}_{q-k}, \underline{c}_1, \ldots, \underline{c_r})\ ,$$ where the right-hand side follows from invariance under column permutations. Equation ((PTij)) follows by applying this identity to the matrix $(BT_{ij})_{S_{\underline{p}}, S_{\underline{q}}}$, where $q=q_j$, $\underline{a}$ is the $i^{\mathrm{th}}$ column of $B$, $\underline{b}$ is the $j^{\mathrm{th}}$ column of $B$, and $\underline{c}_1,\ldots, \underline{c}_r$ denote the $n-q_j$ remaining columns of $B$. ◻

**Lemma 69**. *Let $\mu, \nu \subset \{(i,j): 1\leq i, j \leq n\}$ where $|\mu|= |\nu|=2n-1$. Let $i,j\in \{1,\ldots, n\}$ be distinct and $\omega_{\mu}(T_{ij} \Omega)$ be the differential form obtained from $\omega_\mu$ by replacing every form $\omega_{ab}$, for $(a,b)\in \mu$ in its definition as an exterior product with the corresponding entry $(T_{ij} \Omega)_{ab}$ of the matrix $T_{ij} \Omega$. Let $(\omega_{\mu}(T_{ij} \Omega))_{\nu}$ be the $\nu$-isotypical component of $\omega_{\mu}(T_{ij} \Omega)$.*

*(i). Then $(\omega_{\mu}(T_{ij} \Omega))_{\nu}=0$ unless for some $r\geq 1$ $$\label{munusubst} \mu = \nu \cup \{ (i,k_1),\ldots, (i,k_r)\} \setminus  \{(j,k_1), \ldots, (j,k_r) \} \ ,$$ where $(j,k_\ell) \in \nu$ and $(i,k_\ell) \notin \nu$ for $1\leq \ell \leq r$. In other words, $\mu$ is obtained from $\nu$ by replacing a number of elements of the form $(j,k)$ with $(i,k)$. In particular, ${\underline{q}}(\mu) = {\underline{q}}(\nu)$ and ${\underline{p}}(\mu) = {\underline{p}}(\nu) + r ({\underline{e}}_i -{\underline{e}}_j)\ .$*

*(ii). Let $S_r(\nu)$ denote the set of types $\mu$ satisfying (munusubst). Then $$\label{eq: TijOmega}
\sum_{\mu \in S_r(\nu)}  (\omega_{\mu} (T_{ij} \Omega))_{\nu} = \binom{{\underline{p}}(\nu)_j-1}{r}\, \omega_{\nu} \ .$$*

*Proof.* The matrix $T_{ij} \Omega$ is obtained from $\Omega$ by adding row $j$ to row $i$. Therefore $T_{ij} \Omega = \pi^* \Omega$ where $$\pi^*  \omega_{ab} = \begin{cases}  \omega_{ab} &\hbox{, if } a \neq i \\
\omega_{ib}+ \omega_{jb}    &\hbox{, if } a = i \ . \end{cases}$$ Thus $\omega_{\mu}(T_{ij} \Omega) =  \pi^* \omega_{\mu}$, and in particular there exists an $\varepsilon \in \{-1,1\}$ such that by antisymmetry of the exterior product $$\label{eq: muTijO}
\omega_{\mu}(T_{ij}\Omega )   = \varepsilon \bigwedge_{(a,b) \in \mu, a\neq i}  \omega_{ab} \wedge \bigwedge_{(i,b) \in \mu} (\omega_{ib} + \omega_{jb})= \varepsilon \bigwedge_{(a,b) \in \mu, a\neq i}  \omega_{ab} \wedge\bigwedge_{(i,b),(j,b), \in \mu}  \omega_{ib} \wedge \bigwedge_{(i,b) \in \mu,(j,b) \notin \mu,} (\omega_{ib} + \omega_{jb}) \ .$$

By expanding out this expression, one sees that a $\nu$ with a non-trivial $\nu$-isotypical component differs from $\mu$ by replacing $(i,b)$ with $(j,b)$ for some $b$. This proves $(i)$.

For $(ii)$, we may choose the order in Definition 21 consistently for all $\mu \in S_r(\nu)$ by replacing elements $(j,k)$ with $(i,k)$ and respecting their order. Consequently, the coefficient of $\eta_{\nu}$ in $\eta_{\mu}(T_{ij}\Omega)$ does not depend on $\mu$. The identity to be proven then reduces to a statement about determinants of matrices $M^{\emptyset,c}_{\mu}$ for any $c$. The matrix $M_{\mu}$, for $\mu \in S_{r}(\nu)$, is related to that of $M_\nu$ by removing a $-1$ in row $(j,k_\ell)$ and column $j$, and replacing it with a $-1$ in the same row (now indexed by $(i,k_{\ell})$) in column $i$ for $\ell =1, \ldots, r$. Thus, in effect, $r$ matrix entries move from column $j$ to column $i$. If we choose $c=i$ and delete column $i$ from all these matrices $M_{\mu}$, then we obtain $|S_r(\nu)|$ matrices which differ only in a single column $j$. Since the determinant is multilinear with respect to columns, we deduce that: $$\sum_{\mu \in S_{r}(\nu)}\det M_{\mu}^{\emptyset,i}=\det \left(\sum_{\mu \in S_{r}(\nu)} M_{\mu}^{\emptyset,i}\right) \ .$$ We may extend the sum to the larger set $S'_r(\nu)$ consisting of $\mu$ of the form (munusubst), without the condition that $(i,k_\ell) \notin \nu$. Such a $\mu$ has repeated pairs $(i,k_\ell)$ and defines, as in Definition 21, a matrix $M_{\mu}$ with at least two repeated rows, and hence $\det M^{\emptyset,i}_{\mu}=0$. We deduce that $$\sum_{\mu\in S_r(\nu)}\det M_{\mu}^{\emptyset,i}=\det \left(\sum_{\mu \in S'_r(\nu)} M_{\mu}^{\emptyset,i}\right)=\frac{{\underline{p}}(\nu)_j-r}{{\underline{p}}(\nu)_j}
\binom{{\underline{p}}(\nu)_j}{r}  \det M^{\emptyset,i}_\nu=\binom{{\underline{p}}(\nu)_j-1}{r}  \det M^{\emptyset,i}_\nu,$$ since $S'_r(\nu)$ has $\binom{{\underline{p}}(\nu)_j}{r}$ elements, and because the sum over all $\mu$ uniformly distributes $({\underline{p}}(\nu)_j-r)\genfrac(){0pt}{}{{\underline{p}}(\nu)_j}r$ entries $-1$ over the ${\underline{p}}(\nu)_j$ slots in row $(j,k_{\ell})$ and column $j$. We deduce that by Definition 21 $$\sum_{\mu \in S_r(\nu)}  (\omega_{\mu} (T_{ij} \Omega))_{\nu} =   \sum_{\mu \in S_r(\nu)} \epsilon \det M^{\emptyset, i}_{\mu}\,    \eta_{\nu} =     \binom{{\underline{p}}(\nu)_j-1}{r}  \epsilon \det M^{\emptyset, i}_{\nu}\,    \eta_{\nu} =  \binom{{\underline{p}}(\nu)_j-1}{r}  \omega_{\nu}\  ,$$ with $\epsilon=(-1)^{\binom{n}2+i-1}$. ◻

**Example 70**. *Consider the case $r=1$ in Lemma 69, $$\mu=\nu_k=\nu\cup(i,k)\setminus(j,k)\ .$$ The types $\nu$ and $\nu_k$ are identical except for the pair $(j,k)$ in $\nu$ which is replaced by $(i,k)$. From ((eq: muTijO)) we see that $\omega_{\nu_k}(T_{ij}\Omega)$ is obtained from $\omega_{\nu_k}$ by replacing $\omega_{ib}$ with $\omega_{ib}+\omega_{jb}$ for all pairs $(i,b)\in\nu_k$ with $(j,b)\notin\nu_k$. If we project this onto its $\nu$-isotypical component, then for $b\neq k$ we have $(j,b)\notin \nu$, so that we can in effect set $\omega_{jb}=0$ in $\omega_{ib}+\omega_{jb}$. In other words $\left(\omega_{\nu_k}(T_{ij}\Omega)\right)_{\nu}$ is obtained from $\omega_{\nu_k}$ by replacing the single entry $\omega_{ik}$ with $\omega_{ik}+\omega_{jk}$. We obtain $$(\omega_{\nu_k}(T_{ij}\Omega))_\nu=\left.\nu_k\right|_{\omega_{ik}\mapsto\omega_{jk}}\ .$$ By summing over all $k$ we obtain from Equation ((eq: TijOmega)), $$\sum_{\mu \in S_1(\nu)}  (\omega_{\mu} (T_{ij} \Omega))_{\nu} =
\sum_{k:(j,k)\in\nu,(i,k)\notin\nu}  (\omega_{\nu_k} (T_{ij} \Omega))_{\nu} =
({\underline{p}}(\nu)_j-1)\, \omega_{\nu} \ .$$*

## Case when $B=I_n$.

Let us write $F_{\nu}= F_{\nu}(I_n)$. Then (Xdecomp) takes the form: $$\label{Fij1}
X(I_n,\Omega_\nu)=F_\nu\, \eta_\nu\ .$$

### Hamiltonian circuits

Since $$\Omega = \sum_{1 \leq i, j \leq n}  \omega_{ij} E_{ij}$$ it follows from the identity $E_{ij} E_{k\ell} = \delta_{jk} E_{i\ell}$ that $$\label{XInucycles} X(I_n, \Omega)_{ij} = \left(\Omega^{2n-1} \right)_{ij} = \sum_{k_1,\ldots, k_{2n-2}} \omega_{i k_1} \wedge \omega_{k_1 k_2} \wedge \ldots \wedge \omega_{k_{2n-2} j}  \ ,$$ whose $\nu$-isotypical component is $$\label{XInucycles1}
X(I_n, \Omega_\nu)_{ij} = \sum_{(k_r,k_{r+1})\in\nu}
\omega_{i k_1} \wedge \omega_{k_1 k_2} \wedge \ldots \wedge \omega_{k_{2n-2} j}\ ,$$ where $r$ runs from $0$ to $2n-2$, and $k_0=i$, $k_{2n-1}=j$.

**Lemma 71**. *(i). The matrix $F_{\nu}$ vanishes unless one of the following two situations occurs:*

1.  *If ${\underline{p}}(\nu)={\underline{q}}(\nu)$, in which case $F_\nu$ is diagonal.*

2.  *If ${\underline{p}}(\nu)-{\underline{q}}(\nu)={\underline{e}}_i-{\underline{e}}_j$ for $i\neq j$, then $F_\nu$ is a multiple of the elementary matrix $E_{ij}$.*

*(ii). If there exists a $k\in\{1,\ldots,n\}$ such that ${\underline{p}}(\nu)_k=0$ or ${\underline{q}}(\nu)_k=0$, then $F_\nu=0$.*

*Proof.* For $(i)$ notice that the set of second indices for each form $\omega_{\bullet \bullet}$ occurring in ((XInucycles)) match the first indices with the exception of $i$ and $j$.

$(ii).$ Let ${\underline{p}}(\nu)_k=0$. The statement is invariant under permuting labels. We hence may assume without restriction that $k=1$. This implies that $\Omega$ has zero first row. For any integer $r\geq1$ we obtain $$\Omega^r=\left(\begin{array}{cc}0&0\\
(\Omega^{11})^{r-1}\wedge\underline{\alpha}&(\Omega^{11})^r\end{array}\right)\ ,$$ where $\Omega^{11}$ is $\Omega$ with first row and column deleted and $\underline{\alpha}$ is the column vector $(\omega_{21},\ldots, \omega_{n1})^T$. We set $r=2n-1$ and use $(\Omega^{11})^{2n-2}=0$, which follows from the last sentence in the proof of Lemma 66, to deduce the result.

The result for ${\underline{q}}(\nu)_k=0$ follows by transposition. ◻

To any type $\nu$, consider the oriented graph $G_\nu$ which has vertices $1,\ldots,n$ and an edge from vertex $i$ to vertex $j$ for every pair $(i,j) \in\nu$, (the second construction of Remark 16). A term $\omega_{ik_1}\wedge\omega_{k_1k_2}\wedge\ldots\wedge\omega_{k_{2n-2}j}$ in (XInucycles) corresponds to an oriented path from $i$ to $j$ through all $2n-1$ edges of $G_\nu$. The coefficients in the matrices $F_{\nu}$ therefore count the number of such paths between edges of $G_{\nu}$. Using (XInucycles), we may write $$\label{sumpath}
(F_\nu)_{ij}=\sum_{\gamma_{ij}\in\nu}\mathrm{sgn}\,(\gamma_{ij})\ ,$$ where the sum is over all oriented $(2n-1)$-paths $\gamma_{ij}$ from $i$ to $j$ and $\mathrm{sgn}\,(\gamma_{ij}) \in \{1,-1\}$ is the sign of the ordering of the edges in this path relative to $\nu$.

Now we specialize to the case $i=j$, so that $\gamma_{ii}$ becomes a closed path from $i$ to $i$. Let $\gamma$ be any closed oriented path in $G_{\nu}$, which passes through vertices $\gamma_1,\ldots, \gamma_{2n-1},\gamma_1$ in order. Since there are $2n-1$ terms in the wedge product we have $$\omega_{\gamma_1 \gamma_2}  \wedge   \omega_{\gamma_2 \gamma_3} \wedge \ldots \wedge \omega_{\gamma_{2n-1} \gamma_{1}} =    \omega_{\gamma_2 \gamma_3}  \wedge \ldots \wedge \omega_{\gamma_{2n-1} \gamma_{1}} \wedge \omega_{\gamma_1 \gamma_2}\ ,$$ which is therefore invariant under cyclic permutations of $(\gamma_1, \gamma_2, \ldots, \gamma_{2n-1})$. It follows that the sign $\mathrm{sgn}\,(\gamma_{ii})=\mathrm{sgn}\,([\gamma])$ in ((sumpath)) only depends on the closed oriented loop $[\gamma]$ (defined to be the equivalence class of oriented closed paths with different base points with respect to cyclic, but not dihedral, permutations). We may thus define $$\eta_{[\gamma]} = \bigwedge_{e\in E(\gamma)}  \omega_{e}\ ,$$ where the wedge product is over the oriented edges in a representative $\gamma$ of $[\gamma]$, taken in the order in which they appear in $\gamma$, starting with any edge. The closed loop $[\gamma]$ may be broken open at any of the vertices $i=1,\ldots, 2n-1$ to obtain a total of $2n-1$ paths, of which there are exactly ${\underline{p}}(\nu)_i$ starting and ending at vertex $i$. This is because ${\underline{p}}(\nu)_i=|\{j: \gamma_j=i\}|$ is equal to the number of oriented edges in $G_{\nu}$ whose source is vertex $i$. It follows that $$\label{eq: HamCyc}
X(I_n,\Omega_\nu)_{ii}={\underline{p}}(\nu)_i\sum_{[\gamma]\in\nu}\eta_{[\gamma]}\qquad\text{and}\qquad
(F_\nu)_{ii}={\underline{p}}(\nu)_i\sum_{[\gamma]\in\nu}\mathrm{sgn}\,([\gamma])\ ,$$ where the sums are over all oriented Hamiltonian loops $[\gamma]$ in $G_{\nu}$.

### Formula for $X(I_n, \Omega)$.

Let ${\underline{p}}=(p_1,\ldots, p_n)$, where all $p_1,\ldots, p_n\geq 0$ are integers. Define

$$\label{cdef}
c({\underline{p}})_i=\prod_{r:p_r+\delta_{i,r}\geq1}(p_r+\delta_{i,r}-1)!\ ,$$ where the empty product is 1.

**Proposition 72**. *For all $1\leq i, j\leq n$, we have: $$\label{eq: Xid}
   X(I_n,\Omega_\nu)_{ij}= \delta_{{\underline{p}}(\nu)-{\underline{e}}_i,{\underline{q}}(\nu)-{\underline{e}}_j}c({\underline{p}}(\nu))_j \, \omega_{\nu}\ .$$*

## Proof of Proposition 72

The proof is by induction over $n$. If ${\underline{p}}(\nu)-{\underline{q}}(\nu)\neq{\underline{e}}_i-{\underline{e}}_j$, then both sides of ((eq: Xid)) are zero, see Lemma 71 $(i)$. We hence may assume that ${\underline{p}}(\nu)-{\underline{q}}(\nu)={\underline{e}}_i-{\underline{e}}_j$.

The case $n=1$ is trivial. The induction step from $n-1$ to $n$ has two stages. In the first, we establish the case ${\underline{p}}(\nu)={\underline{q}}(\nu)$ (i.e. $i=j$) using the induction hypothesis for $n-1.$ In the second, we reduce the case when $i\neq j$ to the case ${\underline{p}}(\nu)={\underline{q}}(\nu)$.

### The case ${\underline{p}}(\nu)={\underline{q}}(\nu)$ {#sect: casepnuisqnu}

Throughout this subsection assume ${\underline{p}}(\nu)={\underline{q}}(\nu)$. From Lemma 71 $(i)$ we obtain that $X(I_n,\Omega_\nu)_{ij}=0$ for $i\neq j$. We hence may restrict ourselves to the case $i=j$.

If $\Omega_\nu$ has a zero row, then Equation ((eq: Xid)) is trivial by Lemma 71 $(ii)$ and Lemma 24 $(ii)$. If not, then, since $\Omega_{\nu}$ contains $2n-1$ non-zero entries, there must exist a row $r$ containing a single non-zero entry $\omega_{ra}$ and hence ${\underline{p}}(\nu)_r=1$. Because ${\underline{q}}(\nu)_r={\underline{p}}(\nu)_r=1$, column $r$ of $\Omega_\nu$ also has a single non-zero entry $\omega_{br}$ lying in some row $1\leq b \leq n$.

The Hamiltonian path $(i,k_1,\ldots, k_{2n-2}, i)$ corresponding to each summand of ((XInucycles1)) has the same start and end point, so that we can express $X(I_n,\Omega_\nu)_{ii}$ as a sum over Hamiltonian loops $[\gamma]$, see ((eq: HamCyc)). Since ${\underline{p}}(\nu)_r={\underline{q}}(\nu)_r=1$, every such loop $[\gamma]$ runs through the vertex $r$ exactly once. Since $G_{\nu}$ has a unique edge entering and leaving $r$, we may open all such loops $[\gamma]$ at the vertex $r$ to obtain $$X(I_n,\Omega_\nu)_{ii}={\underline{p}}(\nu)_i\,\omega_{ra}\wedge X(I_{n-1},\Omega_{\nu\setminus\{(r,a),(b,r)\}})_{ab}\wedge\omega_{br}\ ,$$ on applying ((XInucycles1)) in the situation $i=a$, $j=b$. The type $\nu\setminus\{(r,a),(b,r)\}$, is a subset of $2n-3$ pairs of the $n-1$ element set $\{1,\ldots, r-1,r+1,\ldots, n\}$. Note that $\Omega_{\nu\setminus\{(r,a),(b,r)\}}\cong  (\Omega_{\nu}^{r,r})$.

By induction hypothesis we may apply (eq: Xid) to $X(I_{n-1},\Omega_{\nu\setminus\{(r,a),(b,r)\}})_{ab}$ to deduce that $$\label{Xii}
X(I_n,\Omega_\nu)_{ii}={\underline{p}}(\nu)_i\,
c({\underline{p}}(\nu\setminus\{(r,a),(b,r)\}))_b\,\omega_{ra}\wedge\omega_{\nu\setminus\{(r,a),(b,r)\}}\wedge\omega_{br}\ ,$$ since ${\underline{p}}(\nu\setminus\{(r,a),(b,r)\})  -  {\underline{q}}(\nu\setminus\{(r,a),(b,r)\}) = {\underline{p}}(\nu) -{\underline{q}}(\nu) +{\underline{e}}_a-{\underline{e}}_b={\underline{e}}_a-{\underline{e}}_b$ and so the Kronecker delta in the formula is $1$. For $k\neq r$ we have ${\underline{p}}(\nu\setminus\{(r,a),(b,r)\})_k={\underline{p}}(\nu)_k-\delta_{k,b}$. We obtain $${\underline{p}}(\nu)_i\,c({\underline{p}}(\nu\setminus\{(r,a),(b,r)\}))_b={\underline{p}}(\nu)_i\,\prod_{k\neq r:{\underline{p}}(\nu)_k\geq1}({\underline{p}}(\nu)_k-1)!=c({\underline{p}}(\nu))_i\ ,$$ where we have used ${\underline{p}}(\nu)_r=1$ and ${\underline{p}}(\nu)_i\geq1$ for all $i.$ We may reorder the exterior product of forms in ((Xii)) to place $\omega_{br}$ on the far left, which multiplies by a factor $(-1)^{2n-2}=1.$ Proposition 25 implies that $$\omega_{br}\wedge\omega_{ra}\wedge\omega_{\nu\setminus\{(r,a),(b,r)\}}=\omega_\nu\ .$$ Equation ((eq: Xid)) follows.

### The case ${\underline{p}}(\nu)-{\underline{q}}(\nu)={\underline{e}}_i-{\underline{e}}_j$ for $i\neq j$

Equation ((XInucycles1)) leads to the decomposition $$\label{XInurecursion}
X(I_n, \Omega_\nu)_{ij} = \sum_{k:(i,k)\in\nu} \omega_{ik}\wedge X_{kj}\ ,$$ where $$\label{XInucycles2}
X_{kj} = \sum_{(k_r,k_{r+1})\in\nu\setminus(i,k)}\omega_{k k_2} \wedge \ldots \wedge \omega_{k_{2n-2} j}\ ,$$ with $1\leq r\leq 2n-2$ and $k_1=k$, $k_{2n-1}=j$. Fix a choice of $k$ (which may be equal to $j$) and consider $X_{kj}$. We distinguish two cases: $(j,k)\in\nu\setminus(i,k)$ or $(j,k)\notin\nu\setminus(i,k)$. If $(j,k)\in\nu\setminus(i,k)$, then for each summand $\sigma$ in ((XInucycles2)) there exists a unique $r=r_{\sigma}$ such that $(k_r, k_{r+1})=(j,k)$. One can only have $r_\sigma=1$, or $r_\sigma=2n-2$, if $j=k$. For every term $\sigma$ in ((XInucycles2)) we may uniquely write $$\sigma =   \underbrace{ \omega_{k k_2}\wedge\ldots\wedge\omega_{k_{r_\sigma-1} j}}_{\alpha_{\sigma}} \wedge \omega_{jk} \wedge \underbrace{\omega_{k k_{r_\sigma+2}} \wedge\ldots\wedge \omega_{k_{2n-2} j}}_{\beta_{\sigma}} = \alpha_{\sigma} \wedge \omega_{jk} \wedge \beta_{\sigma}\ ,$$ where $\alpha_\sigma=1$ for $r_\sigma=1$ and $\beta_\sigma=1$ for $r_\sigma=2n-2$. Since $\deg(\alpha_{\sigma})=r_\sigma-1$ and $\deg(\beta_{\sigma})=2n-2-r_\sigma$, $$\sigma =  (-1)^{r_\sigma-1}  \omega_{jk}  \wedge \alpha_{\sigma}\wedge  \beta_{\sigma} =  (-1)^{r_\sigma-1}(-1)^{ r_\sigma(2n-2-r_\sigma)}    \beta_{\sigma}  \wedge\omega_{jk} \wedge \alpha_{\sigma}\ ,$$ Since $r_\sigma-1  + r_\sigma (2n-2-r_\sigma) \equiv r_\sigma(r_\sigma+1)+1 \equiv 1 \mod 2$, the sign is always $-1$. The $(2n-2)$-form $\beta_{\sigma}  \wedge\omega_{jk} \wedge \alpha_{\sigma}$ corresponds to a Hamiltonian path from $k$ to $j$ and hence to a unique summand $\sigma'$ in ((XInucycles2)). The map $\sigma\mapsto \sigma'$ which corresponds to interchanging $\beta_{\sigma'}=\alpha_{\sigma}$ and $\alpha_{\sigma'}=\beta_{\sigma}$ is involutive and necessarily a bijection between summands of ((XInucycles2)). The above identity implies that the contributions from $\sigma$ and $\sigma'$ have opposite signs in ((XInucycles2)) and thus cancel. It follows that $X_{kj}$ vanishes in the case when $(j,k)\in\nu\setminus(i,k)$.

Now suppose that $(j,k)\notin\nu\setminus(i,k)$. In this case we can define a new set of pairs $\nu_k=\nu\cup (j,k)\setminus(i,k)$. It satisfies ${\underline{p}}(\nu_k)={\underline{p}}(\nu)+{\underline{e}}_j-{\underline{e}}_i$ and ${\underline{q}}(\nu_k)={\underline{q}}(\nu)$. Since ${\underline{p}}(\nu)-{\underline{q}}(\nu) = {\underline{e}}_i-{\underline{e}}_j$, we deduce that ${\underline{p}}(\nu_k)={\underline{q}}(\nu_k)$ and we may apply the results of Section 9.3.1 to obtain: $$\label{inproof: XIOmega1}
    X(I_n,\Omega_{\nu_k})_{jj}=c({\underline{p}}(\nu_k))_j\,\omega_{\nu_k}\ .$$ Since $(j,k) \in \nu_k$, there exists a unique $(2n-2)$-form $\alpha_k$ not involving $\omega_{jk}$ such that $$\omega_{\nu_k}=\omega_{jk}\wedge\alpha_k \ .$$ We may open all Hamiltonian loops ((eq: HamCyc)) for $X(I_n,\Omega_{\nu_k})_{jj}$ at the edge $(j,k)$. This yields $$\label{inproof: XIOmega2}
    X(I_n,\Omega_{\nu_k})_{jj}={\underline{p}}(\nu_k)_j\,\omega_{jk}\wedge X_{kj},$$ where $X_{kj}$ is defined in (XInucycles2). Since $(j,k) \in \nu_k$ we have ${\underline{p}}(\nu_k)_j>0$. By equating (inproof: XIOmega1) and (inproof: XIOmega2), we obtain $$X_{kj}=\frac{c({\underline{p}}(\nu_k))_j}{{\underline{p}}(\nu_k)_j}\,\alpha_k=\Big(\prod_{s:{\underline{p}}(\nu_k)_s\geq1}({\underline{p}}(\nu_k)_s-1)!\Big)\,\alpha_k.$$ This formula holds for all $k$. Therefore in Formula ((XInurecursion)) we may apply this for every $k$ after discarding all terms $X_{kj}$ for $k$ such that $(j,k)\in \nu$, which vanish by the previous argument. This leads to the formula: $$\label{XInurecursion1}
X(I_n, \Omega_\nu)_{ij} =\Big(\prod_{s:{\underline{p}}(\nu_k)_s\geq1}({\underline{p}}(\nu_k)_s-1)!\Big) \sum_{k:(i,k)\in\nu,(j,k)\notin\nu} \omega_{ik}\wedge\alpha_k\ .$$ For each $k$ in this formula, the expression $\omega_{ik}\wedge\alpha_k$ is obtained by replacing the one-form $\omega_{jk}$ in $\omega_{\nu_k}$ by $\omega_{ik}$. By Example 70 with $i,j$ interchanged, the sum on the right hand side of ((XInurecursion1)) equals $({\underline{p}}(\nu)_i-1)\,\omega_\nu$.

If ${\underline{p}}(\nu)_i=1$, then ${\underline{q}}(\nu)_i=0$ and both sides of ((eq: Xid)) vanish by Lemma 71 $(ii)$ and Lemma 24 $(ii)$. Otherwise, ${\underline{p}}(\nu)_i>1$ and we conclude that $$({\underline{p}}(\nu)_i-1)\prod_{s:{\underline{p}}(\nu_k)_s\geq1}({\underline{p}}(\nu_k)_s-1)!=
({\underline{p}}(\nu)_i-1)\prod_{s:{\underline{p}}(\nu)_s+\delta_{j,s}-\delta_{i,s}\geq1}({\underline{p}}(\nu)_s+\delta_{j,s}-\delta_{i,s}-1)!=c({\underline{p}}(\nu))_j \ .$$ Equation ((eq: Xid)) follows and completes the induction step.

## Properties of $Y(B, \Omega)$

It follows from (Ydef) that $$\label{Ynu}
Y(B,\Omega_{\nu})=\Phi_{\nu}(B)\,\omega_\nu \ .$$

**Proposition 73**. *We have the identity $X(I_n, \Omega_{\nu}) = Y(I_n,\Omega_{\nu})$.*

*Proof.* Let ${\underline{p}}=(p_1,\ldots, p_n)$ and ${\underline{q}}=(q_1,\ldots, q_n)$ be the frequency vectors of the multisets $S_{\underline{p}}$ and $S_{\underline{q}}$. It follows from the definition that $P_{{\underline{p}},{\underline{q}}}(I_n)$ is the number of bijections between the multisets $S_{\underline{p}}$ and $S_{\underline{q}}$ mapping $i\in S_{\underline{p}}$ to $i\in S_{\underline{q}}$ for all $i\in\{1,\ldots,n\}$. If there exist an $r\in\{1,\ldots,n\}$, such that $p_r\neq q_r$, then no such bijection exists and $P_{{\underline{p}},{\underline{q}}}(I_n)=0$. Otherwise every such bijection may be identified with a product of $n$ permutations on $p_r=q_r$ elements. We obtain $$P_{{\underline{p}},{\underline{q}}}(I_n)= \prod_{r=1}^n   \delta_{p_r,q_r} \, q_r! =   \delta_{{\underline{p}},{\underline{q}}}  \prod_{r=1}^n    \, q_r!\ .$$ By (Phidef) we deduce that if ${\underline{p}}(\nu)_r\geq1$ for all $r$, then $$Y(I_n,\Omega_\nu)_{ij}=\delta_{{\underline{q}}(\nu)+{\underline{e}}_i-{\underline{e}}_j,{\underline{p}}(\nu)}
({\underline{q}}(\nu)_j+\delta_{i,j}-1)\Big(\prod_{r=1}^n({\underline{p}}(\nu)_r-1)!\Big)\,\omega_\nu.$$ Suppose that ${\underline{q}}(\nu)+{\underline{e}}_i-{\underline{e}}_j={\underline{p}}(\nu)$. Then taking $j^{\mathrm{th}}$ components gives ${\underline{q}}(\nu)_j+\delta_{i,j}-1
={\underline{p}}(\nu)_j$. The previous expression simplifies with ((cdef)) to $$Y(I_n,\Omega_\nu)_{ij}=
\delta_{{\underline{p}}(\nu)-{\underline{e}}_i,{\underline{q}}(\nu)-{\underline{e}}_j}
c({\underline{p}}(\nu))_j\,\omega_\nu\ .$$ This is equal to $X(I_n,\Omega_\nu)_{ij}$ by Proposition 72. If ${\underline{q}}(\nu)+{\underline{e}}_i-{\underline{e}}_j\neq{\underline{p}}(\nu)$, then $X(I_n,\Omega_\nu)=0$ by Lemma 71 $(i)$. If there exists an $r$ such that ${\underline{p}}(\nu)_r=0$ then $X(I_n,\Omega_\nu)=0$ by Lemma 71 $(ii)$ and $Y(I_n,\Omega_\nu)=0$ by Lemma 24 $(ii)$. In both cases the identity holds trivially. ◻

### Action of elementary transformations

**Proposition 74**. *Let $n\geq2$, and $i\neq j$ where $i,j \in \{1,\ldots, n\}$. Then $$\label{Tij}
Y(BT_{ij},\Omega)=Y(B,T_{ij}\Omega) \ .$$*

*Proof.* Let $\nu$ be a type of rank $n$. By taking $\nu$-isotypical components (Tij) is equivalent to $$\label{eq: phinuphimu}
\Phi_{\nu}(B T_{ij})\,  \omega_{\nu} =     \sum_{\mu}  \Phi_{\mu}(B) \, (\omega_{\mu}(T_{ij} \Omega))_{\nu}\ ,$$ where the sum is over all types $\mu$. The $(a,b)$th entry of the right-hand side is by definition $$\sum_{\mu}  ( {\underline{q}}(\mu)_{b} + \delta_{a,b}-1)     P_{{\underline{q}}(\mu) + {\underline{e}}_a -{\underline{e}}_b-{\underline{1}}, {\underline{p}}(\mu)-{\underline{1}}}(B)
  \,  (\omega_{\mu}(T_{ij} \Omega))_{\nu} \ .$$ By Lemma 69 $(i)$ this reduces to $$( {\underline{q}}(\nu)_{b} + \delta_{a,b}-1)  \sum_{r\geq 0 }  \sum_{\mu \in S_r(\nu)}      P_{{\underline{q}}(\nu) + {\underline{e}}_a -{\underline{e}}_b-{\underline{1}}, {\underline{p}}(\nu)+r({\underline{e}}_i -{\underline{e}}_j)-{\underline{1}}}(B)
  \,  (\omega_{\mu}(T_{ij} \Omega))_{\nu}\ .$$ We move the sum over $\mu$ past the permanent and obtain from Lemma 69 $(ii)$ $$( {\underline{q}}(\nu)_{b} + \delta_{a,b}-1)  \sum_{r\geq 0 }   \binom{{\underline{p}}(\nu)_j-1}{r}     P_{{\underline{q}}(\nu) + {\underline{e}}_a -{\underline{e}}_b-{\underline{1}}, {\underline{p}}(\nu)+r({\underline{e}}_i -{\underline{e}}_j)-{\underline{1}}}(B)      \nonumber
  \,  \omega_{\nu} \ .$$ By Lemma 68 this equals $$( {\underline{q}}(\nu)_{b} + \delta_{a,b}-1) P_{{\underline{q}}(\nu) + {\underline{e}}_a -{\underline{e}}_b-{\underline{1}}, {\underline{p}}(\nu)-{\underline{1}}}(BT_{ij})\,\omega_\nu\ ,$$ which is the $(a,b)$th entry of the left-hand side of ((eq: phinuphimu)). ◻

### Completion of the proof

**Theorem 75**. *For $B, \Omega$ as above, $$\label{XisYthm} X(B,\Omega) = \det(B) Y(B,\Omega) \ .$$*

*Proof.* The case when $B=I_n$ was established in Proposition 73. For any elementary transformation $T_{ij}$, where $1\leq i,j \leq n$, one has $X(BT_{ij},\Omega)=X(B, T_{ij}\Omega)$ by definition. The substitution $B\mapsto B (T_{ij})^k$, $\Omega\mapsto (T_{ij})^k\Omega$ for $k\in{\mathbb Z}$ in this equation and in ((Tij)) ensures that (XisYthm) holds for all $B$ in the subgroup $\Gamma_n \leq \mathrm{SL}_n({\mathbb Z})$ generated by elementary column transformations (it is easy to see that $\Gamma_n=\mathrm{SL}_n({\mathbb Z})$).

Lemma 66 and Equation ((Ynu)) imply that (XisYthm) is equivalent to proving that $$\label{Xnu}
X'(B,\Omega_\nu) = \Phi_{\nu}(B)\,\omega_\nu$$ holds for all $B, \nu$. For each $\nu$, the $(i,j)$th entry of (Xnu) reduces to an identity of polynomials in the entries of $B$ with rational coefficients, which we have already established for all $B\in \Gamma_n$. Since $\Gamma_n$ is Zariski-dense in the algebraic group $\mathrm{SL}_n$, we deduce that the identity of polynomials holds in the ring $$\mathcal{O}(\mathrm{SL}_n) = {\mathbb Q}[b_{ij}] / (\det(B) - 1) \ ,$$ i.e., that the entries of the matrices on both sides of (Xnu) coincide up to powers of $\det(B)$. However, since their entries have total degree $n-1$, which is strictly less than the degree of $\det(B)$, this proves that (Xnu) must hold exactly (i.e., in the ring ${\mathbb Q}[b_{ij}]$), which proves (XisYthm). ◻

# A determinantal identity for antisymmetrised permanents

In this section we prove Theorem 40.

## Preliminaries

Let notations be as in Section 4.

### Preliminary lemmas

We use the following notation. For $\sigma \in \Sigma_m$, we write $$b_{\sigma} = b_{s_1t_{\sigma(1)}} b_{s_2t_{\sigma(2)}} \ldots  b_{s_mt_{\sigma(m)}} \ .$$

**Lemma 76**. *Let $m\geq1$, $k\in\{0,1,\ldots, m\}$ and $\sigma \in \Sigma_m$ be a permutation. Then $$g_1g_2\cdots g_k\pi_{k+1,\ldots,m} \, b_{\sigma}=(-1)^{m-k}\pi_{k+1,\ldots,m} \, b_{\sigma^{-1} }\ .$$*

*Proof.* The case $k=m$ holds because $$g_1\cdots g_m b_\sigma=
b_{ s_{\sigma(1)t_1 }}b_{ s_{\sigma(2)t_2}} \cdots b_{ s_{\sigma(m)t_m}} =b_{s_1t_{\sigma^{-1}(1)}}b_{s_2t_{\sigma^{-1}(2)}} \cdots b_{s_mt_{\sigma^{-1}(m)}} \ .$$ For any element $x$ in the polynomial ring generated by $b_{uv}$ with $u,v \in S_m \cup T_m$, and $g \in G<G_m$, we have $\pi_G (gx) = \chi(g) \pi_G(x)$. In particular, since $\chi(g_i)=-1$, we have $\pi_G(x)=- \pi_G(g_ix)$ if $g_i\in G$. It follows that $$\pi_{k+1,\ldots,m}\, b_\sigma=
(-1)^{m-k}\pi_{k+1,\ldots,m}g_{k+1}\cdots g_mb_\sigma\ .$$ Multiply on the left by $g_1\cdots g_k$ (which commutes with $\pi_{k+1,\ldots,m}$) and apply the case $k=m$ to conclude. ◻

**Lemma 77**. *Let $m\geq1$. Then $$\mathrm{perm}\,B_{[S_m,T_m]} =\left\{\begin{array}{cl}0&,\ m\text{ odd}\\
2\, \pi_{2,\ldots,m}\,\mathrm{perm}\,B_{S_m,T_m}&,\ m\text{ even.}\end{array}\right.$$*

*Proof.* For odd $m$ we take the sum over $\sigma\in\Sigma_m$ of the case $k=0$ in the previous lemma, yielding $\mathrm{perm}\,B_{[S_m,T_m]}=(-1)^m \mathrm{perm}\,B_{[S_m,T_m]}$. For even $m$, the case $k=1$ of the lemma implies that $$g_1\pi_{2,\ldots,m}\,\mathrm{perm}\,B_{S_m,T_m}=-\pi_{2,\ldots,m}\,\mathrm{perm}\,B_{S_m,T_m}\ .$$ Since $\pi_{1,\ldots,m}=(1-g_1)\pi_{2,\ldots,m}$ the result follows. ◻

## A recursion for $\mathrm{perm}\,\, B_{[S_m,T_m]}$

**Proposition 78**. *Let $m\geq2$ even. We define $\mathrm{perm}\,B_{\emptyset,\emptyset}=\mathrm{perm}\,B_{[\emptyset,\emptyset]}=1$. Then $$\label{permrec}
\mathrm{perm}\,B_{[S_m,T_m]} =-\frac12\sum_{i,j=2}^{m}\pi_{i,j} \left(\det B_{s_1t_1,s_it_j}
\left.\mathrm{perm}\,B_{[S_{m}\setminus  \{s_1,s_i\},T_{m}\setminus \{t_1,t_i\}]}\right|_{t_j=t_i}\right)  \ .$$*

*Proof.* We expand $\mathrm{perm}\,B_{S_m,T_m}$ with respect to row 1 followed by column 1 yielding $$B_{S_m,T_m}=\sum_{j=1}^mb_{s_1t_j}\mathrm{perm}\,B_{S_m,T_m}^{1,j}\\
=b_{s_1t_1}\mathrm{perm}\,B_{S_m,T_m}^{1,1}+
\sum_{i,j=2}^mb_{s_1t_j}b_{s_it_1}\mathrm{perm}\,B_{S_m,T_m}^{1i,1j}\ ,$$ where $B^{I,J}$ denotes the matrix $B$ with rows indexed by $I$ and columns indexed by $J$ removed. The antisymmetriser $\pi_1$ annihilates the term $b_{s_1t_1}\mathrm{perm}\,B_{S_m,T_m}^{1,1}$ which is symmetric with respect to $g_1$. The sum on the right-hand side may in turn be written as a sum of two terms: $$\label{inproof:sumtwoterms} \sum_{i=2}^m  b_{s_1t_i}b_{s_it_1}\mathrm{perm}\,B_{S_m,T_m}^{1i,1i}  + \sum_{2 \leq i\neq j \leq m }b_{s_1t_j}b_{s_it_1}\mathrm{perm}\,B_{S_m,T_m}^{1i,1j}  \ .$$ Applying the antisymmetrisation operators to the summands in the sum on the left gives: $$\begin{aligned}
\pi_{1,\ldots,m}b_{s_1t_i}b_{s_it_1}\mathrm{perm}\,B_{S_m,T_m}^{1i,1i} & = &
\left(\pi_{1,i}b_{s_1t_i}b_{s_it_1} \right) \pi_{2,\ldots,\hat{i},\ldots,m}\mathrm{perm}\,B_{S_m\setminus \{s_1,s_i\},T_m\setminus \{t_1,t_i\}}   \nonumber \\
& = & -2 \det B_{s_1t_1,s_it_i}   \mathrm{perm}\,B_{[S_m\setminus \{s_1,s_i\},T_m\setminus \{t_1,t_i\}]}  \nonumber
\end{aligned}$$ by Example 35, and by definition of the antisymmetrised permanent. Now consider the diagonal terms $i=j$ in the sum in the right hand side of ((permrec)). They can be written in the form: $$-\frac{1}{2} \pi^2_{i} \left(\det B_{s_1t_1,s_it_i} \mathrm{perm}\,B_{[S_{m}\setminus  \{s_1,s_i\},T_{m}\setminus \{t_1,t_i\}]}\right)  =   -2  \, \det B_{s_1t_1,s_it_i}   \mathrm{perm}\,B_{[S_{m}\setminus  \{s_1,s_i\},T_{m}\setminus \{t_1,t_i\}]}$$ since $g_i$ acts trivially on $\det B_{s_1t_1,s_it_i}$ and hence $\pi_{i,i}=\pi_i^2$ multiplies it by $4$. It follows that the terms $i=j$ in the right hand side of ((permrec)) come from the left hand sum in (inproof:sumtwoterms) in the expansion of $\mathrm{perm}\,B_{S_m,T_m}$.

There remain the cases $i\neq j$. Antisymmetrising the terms in the right hand sum of (inproof:sumtwoterms) gives $$\pi_{i,j}\left(\pi_1b_{s_1t_j}b_{s_it_1}\right)\left(\pi_{2,\ldots,\hat{i},\hat{j},\ldots,m}\mathrm{perm}\,
B_{S_m\setminus \{s_1,s_i\},T_m\setminus \{t_1,t_j\}}   \right)\ .$$ The second factor simplifies to $\pi_1b_{s_1t_j}b_{s_it_1}=-\det B_{s_1t_1,s_it_j}$, which can be confirmed by direct calculation. Using the invariance of the permanent with respect to column permutations, we may write $$\begin{aligned}
 \pi_{2,\ldots,\hat{i},\hat{j},\ldots,m}\mathrm{perm}\,
B_{S_m\setminus \{s_1,s_i\},T_m\setminus \{t_1,t_j\}}  & = &   \pi_{2,\ldots,\hat{i},\hat{j},\ldots,m}\mathrm{perm}\,
B_{S_m\setminus \{s_1,s_i\},T_m\setminus \{t_1,t_i\}} \Big|_{t_j=t_i}    \nonumber \\
& = &  \frac{1}{2}\,   B_{[S_m\setminus \{s_1,s_i\}],[T_m\setminus \{t_1,t_i\}]} \Big|_{t_j=t_i}       \nonumber
\end{aligned}$$ upon applying Lemma 77 with respect to the index set $i,2,\ldots,\hat{i},\hat{j},\ldots,m$. This recovers the remaining terms $i\neq j$ in the right-hand side of (permrec) and completes the proof. ◻

## A sum of determinants

**Definition 79**. *Let $B$ be a symmetric $m\times m$ matrix and $\mathcal{E}=\{(s_i,t_i),\,i=1,\ldots,m\}$ be a set of pairs with $m$ even. For $\mathcal{E}=\emptyset$ we define $\Sigma(B,\emptyset)=1$. Otherwise $\Sigma(B,\mathcal{E})=\Sigma(B,S_m\cup T_m)$ in Definition 38. Moreover we denote the second sum in ((eq: Sigma)) by $$\label{Tdef}
T_k(B, \mathcal{E}) = \sum_{\genfrac{}{}{0pt}{}{\mathcal{E}=\bigcup_{i=1}^kI_i\cup J_i}{|I_i|=|J_i|}}\det B_{I_1,J_1}\cdots\det B_{I_k,J_k}\ ,$$ where the sum is over all decompositions of $\mathcal{E}$ into (unordered) pairs of sets (of pairs $(s_k,t_k)$) $I_i, J_i$ of equal size. We consider $I_k$, $J_k$ as ordered sets in which each $s_i$ is followed by $t_i$ as in Definition 41.*

**Remark 80**. *The expression on the right hand side of ((Tdef)) is well-defined. It does not depend on the order of the pairs in $I_i$ or $J_i$ as swapping two pairs amounts to swapping pairs of rows or columns in $B_{I_i,J_i}$. Any such permutation is even. It is also invariant on interchanging $I_i\leftrightarrow J_i$ since $B$ is symmetric.*

## A recursion for $\Sigma(B,\mathcal{E})$

Let $I,J$ such that $|I| = |J|$ and $1\in I$. Let $E=\{(s_i,t_i),i\in I\}$ and $F=\{(s_j,t_j),j\in J\}$ and consider the matrix $B_{E,F}$, where $E$ stands for $\{s_{i_1},t_{i_1},\ldots , s_{i_k},t_{i_k}\}$ where $I=\{i_1,\ldots, i_k\}$ and likewise $F$, along the lines of Definition 41. Note that $\det B_{E,F}$ does not depend on the order of the pairs of elements in $E$ and $F$, see Remark 80.

**Lemma 81**. *With the above notation we have $$\begin{gathered}
\label{expandeq}
\det B_{E,F}=\sum_{j\in J}\det B_{s_1t_1,s_jt_j}\det B_{E\setminus(s_1,t_1),F\setminus (s_j,t_j)} \\
 -\sum_{i<j\in J}\pi_{i,j}\left( \det B_{s_1t_1,s_it_j}\det B_{E\setminus (s_1,t_1),F\cup (s_j,t_i)\setminus \{(s_i,t_i),(s_j,t_j)\}} \right),
\end{gathered}$$ where the second sum is over ordered pairs in $J$.*

*Proof.* Recall that for any $n\times n$ matrix $A$, with $n\geq 2$, an expansion along the first two rows leads to the following formula for its determinant: $$\label{detA2x2}
\det A = \sum_{1\leq a<b\leq n}  (-1)^{a+b+1} \det(A_{12,ab}) \det(A^{12,ab})\ ,$$ where $A_{12,ab}$ denotes the $2\times 2$ minor of $A$ with rows $1,2$ and columns $a,b$, and $A^{12,ab}$ denotes the complementary $(n-2)\times(n-2)$ minor obtained by removing rows $1,2$ and columns $a,b$ from $A$.

Apply this formula to $A= B_{E,F}$. The columns are indexed by elements of $F$ and are given by $\{s_j, t_j\}_{j\in J}.$ The indices $a,b$ in (detA2x2), which correspond to elements of $F$, may therefore be as follows:

$(i).$ $(a,b) = (s_j,t_j)$ for some index $j\in J$. Since $a$ is in odd position and $j$ is in even position, the sign $(-1)^{a+b+1}$ equals $1$ and we obtain the first term in (expandeq).

$(ii).$ All remaining terms may be collected in groups of four: $$(a,b) =  (s_i, s_j) \ , (s_i, t_j) \ , \ (t_i, s_j) \ , (t_i, t_j)$$ for every $i<j \in J$. The signs $(-1)^{a+b+1}$ are, respectively, $-1,1,1,-1$. These four terms are the orbit of $(s_i,t_j)$ under the group $\langle g_i,g_j\rangle$ and therefore the total contribution from these four terms comes from the action of $\pi_{i,j}$ on a single term. It suffices to consider, then, the term $(s_i,t_j)$. We may order the pairs in $J$ such that $(s_i,t_i)$ is followed by $(s_j,t_j)$. Deletion of the columns corresponding to $s_i$ and $t_j$ leaves a sequence of columns in the order: $\ldots,t_i,s_j,\ldots$ which, after interchanging $t_i$ and $s_j,$ corresponds to the term $\det B_{E\setminus (s_1,t_1),F\cup (s_j,t_i)\setminus \{(s_i,t_i),(s_j,t_j)\}}$. The minus sign in the second line of (expandeq) comes from the fact that interchanging $t_i$ and $s_j$ multiplies this determinant by $-1$. We thus obtain the second term in (expandeq). ◻

**Proposition 82**. *Let $m\geq2$ even, $B$ be a symmetric $m\times m$ matrix and $\mathcal{E}=\{(s_i,t_i),\,i=1,\ldots,m\}$ be a set of ordered pairs. Then $$\label{sumdetrec}
\Sigma(B,\mathcal{E})=-\frac12\sum_{i,j=2}^m\pi_{i,j} \, \left( \det B_{s_1t_1,s_it_j}\Sigma(B,\mathcal{E}\cup (s_j,t_i)\setminus  \{(s_1,t_1),(s_i,t_i),(s_j,t_j)\})\right)   \  ,$$ where, in the case $i=j$, $\mathcal{E}\cup (s_j,t_i)\setminus  \{(s_1,t_1),(s_i,t_i),(s_j,t_j)\}$ simplifies to $\mathcal{E}\setminus \{(s_1,t_1), (s_j,t_j)\}$.*

*Proof.* We use Formula ((eq: Sigma)) for $\Sigma(B,\mathcal{E})=\Sigma(B,S_m\cup T_m)$, where the second sum is denoted by $T_k(B,\mathcal{E})$ as in Definition 79. The pair $(s_1,t_1)$ in $\mathcal{E}$ lies in exactly one of the sets $I_i,J_i$ for some $i$. By Remark 80, we may assume that $(s_1,t_1)$ is contained in the set $I_1$ and split the decomposition of $\mathcal{E}$ into $I_1\cup J_1$ and a decomposition of $\mathcal{E}'=\mathcal{E}\setminus (I_1\cup J_1)$ into $k-1$ pairs of equal size. We expand out the factor $\det B_{I_1,J_1}$ by applying Lemma 81 with $E=I_1$, $F=J_1$. Then we interchange the sums over $j$ and $i<j$ in equation (expandeq) with the sum over the possible choices for $I_1$ and $J_1$ in $\mathcal{E}$ to obtain $$\begin{gathered}
 \label{TkBexpression}
T_k(B,\mathcal{E})=\sum_{j=2}^m\det B_{s_1t_1,s_jt_j}\sum_{\genfrac{}{}{0pt}{}{I_1\cup J_1\subseteq\mathcal{E},\,\mathcal{E}'=\bigcup_{i=2}^kI_i\cup J_i}{(s_1,t_1)\in I_1,\,(s_j,t_j)\in J_1}}\det B_{I_1\setminus(s_1,t_1),J_1\setminus(s_j,t_j)}X\\
-\sum_{2\leq i<j\leq m}\pi_{i,j}\Big(\det B_{s_1t_1,s_it_j}\sum_{\genfrac{}{}{0pt}{}{I_1\cup J_1\subseteq\mathcal{E},\,\mathcal{E}'=\bigcup_{i=2}^kI_i\cup J_i}{(s_1,t_1)\in I_1,\,(s_i,t_i),(s_j,t_j)\in J_1}}\det B_{I_1\setminus (s_1,t_1),J_1\cup (s_j,t_i)\setminus \{(s_i,t_i),(s_j,t_j)\}}X\Big)\ ,\\
\end{gathered}$$ where $X=\det B_{I_2,J_2}\cdots\det B_{I_k,J_k}$ and all pairs of sets $I_i$, $J_i$ satisfy $|I_i|=|J_i|$.

We first consider the sums in the first line of (TkBexpression), and distinguish the two cases when $I_1=(s_1,t_1)$, and $J_1=(s_j,t_j)$ consist of single pairs, or when $I_1,J_1$ have $\geq 2$ pairs. In the first case $\mathcal{E}'$ is a decomposition of $\mathcal{E}^{1j}:=\mathcal{E}\setminus\{(s_1,t_1),(s_j,t_j)\}$ into $k-1$ pairs of equal size and we have $\det B_{I_1\setminus(s_1,t_1),J_1\setminus(s_j,t_j)}=1$. Therefore this part of the inner sum on the first line of (TkBexpression) reduces to $T_{k-1}(B,\mathcal{E}^{1j})$. These terms contribute $$\sum_{j=2}^m (\det B_{s_1t_1,s_jt_j}) T_{k-1}(B, \mathcal{E}^{1j})$$ to the first line. In the second case, the choice of $I_1$ and $J_1$ may be combined with the partition of $\mathcal{E}'$ to form a partition of $\mathcal{E}^{1j}= \mathcal{E}' \cup (I_1 \setminus (s_1,t_1)) \cup (J_1 \setminus (s_j,t_j))$ into $k$ pairs $I'_{\ell}, J'_{\ell}$ (with $1\leq \ell \leq k$), where $|I'_k| = |J'_k|$. Amongst these $k$ pairs there are $2k$ possibilities for $J_1\setminus(s_j,t_j)$, namely one of $\{I'_1, J'_1, \ldots ,I'_k ,J'_k\}$. This choice uniquely determines $I_1$ and $J_1$ (since if $J_1 =J'_\ell\cup (s_j,t_j)$ then $I_1 =I'_\ell\cup (s_1,t_1)$, or similar with $I'_{\ell}, J'_{\ell}$ interchanged). In this case, therefore, the contribution to the first line of (TkBexpression) is: $$\sum_{j=2}^m (\det B_{s_1t_1,s_jt_j})  2kT_k(B, \mathcal{E}^{1j})\ .$$

Now consider the second line of (TkBexpression). The terms in the inner sum are in bijection with a decomposition of $\mathcal{E}^{1ij}:=\mathcal{E}\cup (s_j,t_i)\setminus \{(s_1,t_1),(s_i,t_i),(s_j,t_j)\}$ into $k$ pairs of equal size. The term which comes from the set $J_1$ is uniquely determined since it is the set which contains the pair $(s_j,t_i)$ (in particular, it cannot be empty). The second sum is hence equivalent to an unordered partition of $\mathcal{E}^{1ij}$ into $k$ pairs of equal size. The inner sum therefore reduces to $T_k(B,\mathcal{E}^{1ij})$ and the second line of (TkBexpression) is $$\sum_{2\le i<j\leq m} (\det B_{s_1t_1,s_it_j})  T_k(B, \mathcal{E}^{1ij})\ .$$

Combining the above yields the following expression for $\Sigma(B,\mathcal{E})=\sum_k (-2)^k k!T_k(B,\mathcal{E})$ (by (eq: Sigma)): $$\sum_{k=1}^{m/2}(-2)^kk!\Bigg(\sum_{j=2}^m\det B_{s_1t_1,s_jt_j}(T_{k-1}(B,\mathcal{E}^{1j})+2kT_k(B,\mathcal{E}^{1j}))-\sum_{2\leq i<j\leq m}\pi_{i,j}(\det B_{s_1t_1,s_it_j}T_k(B,\mathcal{E}^{1ij}))\Bigg)\ ,$$ where the term $T_0(B,\mathcal{E}^{1j})$ vanishes, as do $T_{m/2}(B,\mathcal{E}^{1 j})$ and $T_{m/2}(B,\mathcal{E}^{1 i j})$, because $\mathcal{E}^{1 j}$ and $\mathcal{E}^{1 i j}$ only have a total of $m-2$ pairs.

The term in brackets consists of two sums. In the first sum we shift $k\mapsto k+1$ in the first summand and use $(-2)^{k+1}(k+1)!+2k(-1)^kk!=-2(-2)^kk!$ to obtain $$-2\sum_{k=1}^{m/2-1}(-2)^kk!\sum_{j=2}^m\det B_{s_1t_1,s_jt_j}T_k(B,\mathcal{E}^{1j})\ .$$ We interchange the sums and use $\pi_{j,j}\det B_{s_1t_1,s_jt_j}=4\det B_{s_1t_1,s_jt_j}$ to see that the first term reproduces the summands corresponding to the case $i=j$ in (sumdetrec).

In the second term the summands are invariant under the action of $g_ig_j$ since $\chi(g_ig_j)=1$. Because $B$ is symmetric, the action of $g_ig_j$ is equivalent to swapping $i\leftrightarrow j$. We may hence extend the sum over $i<j$ to all $i\neq j$ if we introduce a factor $1/2$. This provides the summands with $i\neq j$ in ((sumdetrec)) and the result follows. ◻

## Proof of Theorem 40

If $m$ is even, we prove the theorem by induction over $m$ in steps of two. For $m=0$ both sides of (genericPermasSigma) are $1$ (for $m=2$ see examples 35 and 39). For $m\geq2$ we obtain from propositions 78 and 82 that both sides obey the same recursion because $\mathcal{E}\cup(s_j,t_i)\setminus\{(s_1,t_1),(s_i,t_i),(s_j,t_j)\})=\mathcal{E}\setminus \{(s_1,t_1),(s_i,t_i)\}|_{t_j=t_i}$. The case of odd $m$ was proved in Lemma 77.

# Appendix: A matrix identity of Amitsur-Levitzki type

## The Amitsur-Levitzki theorem

Let $R$ be a commutative ring and let $A_1,\ldots, A_{2n} \in M_{n\times n}(R)$ be a set of $2 n$ square matrices with $n$ rows and columns. A famous theorem of Amitsur-Levitzki states that the complete antisymmetrisation of the product of $2n$ matrices vanishes: $$\sum_{\pi \in \Sigma_{2n}} \mathrm{sgn}\,(\pi) A_{\pi(1)}\cdots A_{\pi(2n)} = 0 \ .$$ It was observed by Rosset [@Rosset76; @Procesi] that this formula is equivalent to the identity $\Omega^{2n}=0$, where $\Omega$ is a certain $n\times n$ matrix whose entries are one-forms (see below). A by-product of the results of this paper is an explicit formula for the antisymmetrisation of $2n-1$ such matrices.

## Antisymmetrisation of $k$ matrices

More generally, given $k$ matrices $A_i\in M_{n\times n}(R)$ as above, it is interesting to ask for a formula for the antisymmetrisation $$[A_1,\ldots,A_k] =  \sum_{\pi \in \Sigma_k} \mathrm{sgn}\,(\pi) A_{\pi(1)}\cdots A_{\pi(k)} \ .$$ The case $k=2$ is simply the commutator $[A_1,A_2]= A_1A_2-A_2A_1$.

Following Definition 21 we choose any ordering on ordered pairs of elements in $\{1,\ldots,n\}$ and define types $\nu=((i_1,j_1),\ldots,(i_k,j_k))$ to be sets of $k$ distinct such pairs in the chosen order. Let $\Omega \in M_{n\times n} (R^1)$ be an $n\times n$ matrix whose entries are $1$-forms in a differential graded algebra $R^{\bullet}= \bigoplus_{n\geq 0} R^n$ where $R^0=R$. Its $k$-fold product $\Omega^k\in M_{n\times n}(R^k)$ is a matrix of $k$-forms and may be expanded by type: $$\label{Omegakexpansion} \Omega^k=\sum_{\nu}F_\nu\eta_\nu\ ,$$ as in ((Xdecomp)), where $F_\nu\in M_{n\times n}(R)$ and $\eta_\nu=\Omega_{i_1j_1}\wedge\ldots\wedge\Omega_{i_kj_k}$ if $\nu=((i_1,j_1),\ldots,(i_k,j_k))$ (see Definition 21 $(ii)$ for the case $k=2n-1$).

**Proposition 83**. *In the above notation we have $$\label{eq: AMk}
[A_1,\ldots,A_k]=\sum_{\nu}F_\nu\det \Big((A_r)_{ij}\Big)_{r,ij\in\nu}\ ,$$ where $((A_r)_{ij})_{r,ij\in\nu}$ is the $k\times k$ matrix with entries $(A_r)_{ij}$ in row $r=1,\ldots,k$ and column $(i,j)$, where $(i,j)$ ranges over the $k$ elements in $\nu$ in order.*

*Proof.* Following Rosset, consider the graded exterior algebra $R^{\bullet}=\bigwedge \bigoplus^k_{i=1} R e_i$ where $e_1,\ldots, e_k$ are generators in degree $1$. We have $R^0=R$ and $R^k =  R \, e_1\wedge \ldots \wedge e_k.$ Consider the matrix $$\Omega = \sum_{r=1}^k  A_r e_r  \quad \in \quad M_{n\times n} \left( R^1\right)  \ .$$ Then by antisymmetry, we have $$\Omega^k=[A_1,\ldots, A_k]  \, e_1\wedge\ldots \wedge e_k\ .$$ Now the $(i,j)$th entry of $\Omega$ may be written $$\Omega_{ij}= (A_1)_{ij}e_1 + \ldots +(A_k)_{ij}e_k\ .$$ Substituting into $\eta_\nu$ for $\nu=((i_1,j_1),\ldots,(i_k,j_k))$ yields $$\eta_\nu(e_1,\ldots,e_k)=\sum_{r_1,\ldots,r_k=1}^k
(A_{r_1})_{i_1j_1}e_{r_1}\wedge\ldots\wedge(A_{r_k})_{i_kj_k}e_{r_k}\ .$$ By antisymmetry again, this expression reduces to a determinant and (Omegakexpansion) yields $$\Omega^k=\sum_{\nu}F_\nu\det \Big((A_r)_{ij}\Big)_{r=1,\ldots,k,ij\in\nu}e_1\wedge\ldots\wedge e_k\ .$$ Comparing the coefficients of $e_1\wedge\ldots\wedge e_k$ gives the result. ◻

It is an interesting question to find formulae for the coefficients $F_{\nu}$ in (Omegakexpansion), and hence for $[A_1,\ldots,A_k]$. The theorem of Amitsur-Levitzki is equivalent to the statement that all $F_{\nu}$ vanish when $k=2n$. The results obtained in this paper give an explicit formula in the case $k=2n-1.$

## Antisymmetrisation of $2n-1$ matrices of rank $n$

Recall that the weight $w(\nu)=({\underline{p}}(\nu),{\underline{q}}(\nu))$ of $\nu$ is defined by (see Definition 19) $${\underline{p}}(\nu)=|\{i:(i,j)\in\nu\}|\ ,\qquad{\underline{q}}(\nu)=|\{j:(i,j)\in\nu\}|\ .$$ The pairs in $\nu$ have entries from $1$ to $n$, where $n$ is the rank of $\nu$.

**Theorem 84**. *The $(i,j)$th component of the antisymmetrization of the $2n-1$ generic matrices $A_1,$ $\ldots,$ $A_{2n-1}\in M_{n\times n}(R)$ is given by $$_{ij}=(-1)^{\binom{n}{2}+s-1}\sum_{\nu:{\underline{p}}(\nu)-{\underline{q}}(\nu)={\underline{e}}_i-{\underline{e}}_j}\det(M_{\nu}^{\emptyset,s})\,\Big(\prod_{r=1}^{2n-1}({\underline{p}}(\nu)_r+\delta_{j,r}-1)!\Big)\det \Big((A_r)_{ij}\Big)_{r,ij\in\nu}\ ,$$ where $s$ is any number in $\{1,\ldots,2n\}$ (the formula does not depend on which one), the sum is over types $\nu$ of rank $n$, and the factorial of a negative number is defined to be $1$. The matrix $M_\nu$ and the notation $M_{\nu}^{\emptyset,s}$ are defined in Definition 21 $(i)$ and $(iii)$.*

*Proof.* Use propositions 17 (with $B=I_n$) and 72, and substitute ((omeganudefnANDepsilonk)) into the formula for $\Omega^{2n-1}$. The result follows from Proposition 83. ◻

**Example 85**. *Let $A,B,C$ be three $2 \times 2$ matrices. The antisymmetrisation $$[A,B,C]=   ABC- BAC +BCA - CBA+CAB- ACB$$ is given by determinants of the following $3\times 3$ matrices (see Example 14 with $B=I_2$): $$X_1= \begin{pmatrix}   a_{11} & a_{12} & a_{21} \\
b_{11} & b_{12} & b_{21} \\
c_{11} & c_{12} & c_{21} \\
\end{pmatrix}
\ , \
X_2  = \begin{pmatrix}   a_{11} & a_{12} & a_{22} \\
b_{11} & b_{12} & b_{22} \\
c_{11} & c_{12} & c_{22} \\
\end{pmatrix}
\ , \
X_3  = \begin{pmatrix}   a_{11} & a_{21} & a_{22} \\
b_{11} & b_{21} & b_{22} \\
c_{11} & c_{21} & c_{22} \\
\end{pmatrix}
\ , \
X_4  = \begin{pmatrix}   a_{12} & a_{21} & a_{22} \\
b_{12} & b_{21} & b_{22} \\
c_{12} & c_{21} & c_{22} \\
\end{pmatrix}$$ as $$[A,B,C] = \begin{pmatrix}
2 \det X_1 - \det X_4 &  \det X_2 \\
-\det X_3 &  \det X_1 - 2 \det X_4
\end{pmatrix}\ .$$*

It would be interesting to see to what extent our methods in Section 9 can be used to derive results for $\Omega^k$ in the case $k<2n-1$.

[^1]: using ad-hoc code written in Maple by the first author. See Section 1.6 for a discussion on the use of computer algebra.

[^2]: To make the connection precise, note that by Poincaré duality $$H^{\mathrm{lf}}_k( \mathcal{P}_n/\mathrm{GL}_n({\mathbb Z});{\mathbb R}) \cong \begin{cases}  H^{\binom{n+1}{2}-k}(\mathcal{P}_n/\mathrm{GL}_n({\mathbb Z});{\mathbb R}) \quad\;\;\, \hbox{ if  n is odd\ ,} \\
      H^{\binom{n+1}{2}-k}(\mathcal{P}_n/\mathrm{GL}_n({\mathbb Z});\det) \quad \hbox{ if  n is even\ .}
    \end{cases}$$ By [@ElbazVincentGanglSoule §7.2], $H^k(\mathrm{SL}_n({\mathbb Z});{\mathbb R}) = H^k(\mathrm{GL}_n({\mathbb Z});{\mathbb R})$ if $n$ is odd, and $H^k(\mathrm{SL}_n({\mathbb Z});{\mathbb R}) = H^k(\mathrm{GL}_n({\mathbb Z});{\mathbb R}) \oplus H^k(\mathrm{GL}_n({\mathbb Z});\det)$ if $n$ is even. It follows that $H^{\mathrm{lf}}_k( \mathcal{P}_n/\mathrm{GL}_n({\mathbb Z});{\mathbb R})$ is a summand of $H^{\binom{n+1}{2}-k}(\mathrm{SL}_n({\mathbb Z});{\mathbb R})$ in both cases $n$ odd and even. Church-Farb-Putman conjecture that $H^{\binom{n-1}{2}-i}(\mathrm{SL}_n({\mathbb Z});{\mathbb R})=0$ for all $i \leq n-2$.

[^3]: The extra procedures which are specific to the calculation of canonical forms and integrals are in the file '`CanonicalIntegrals`' which is attached to the article as supplementary material. After the download of `HyperlogProcedures` and `CanonicalIntegrals` one can reproduce all canonical integrals up to five loops with Maple using the commands `read(CanonicalIntegrals)` and `dograph(<loop number>,<graph number>)`. So, e.g., `dograph(3,1)` calculates the canonical integral of $W_3$. For most graphs at seven loops `dograph` is too slow, so that it is necessary to parallelize the computations or even resort to exact numerical methods (see below). Of course, the algorithms can equally well be implemented in any other computer algebra system.
