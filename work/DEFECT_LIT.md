# DEFECT_LIT — Frobenius constants of Picard–Fuchs / Apéry-like operators at MUM points

Literature retrieval, 2026-07-24. Every claim tagged **[V]** = VERIFIED-FROM-PDF (text extracted from the
actual PDF, quoted below) or **[U]** = UNVERIFIED.

Local PDF/text copies used for this report live in the session scratchpad
`/tmp/claude-1000/-home-ubuntu-fable-episode-2-zeta-math-2/65d6d51f-5045-4f1b-98cc-77989fc30264/scratchpad/`
(`gz.pdf`, `gz2.pdf`, `bv.pdf`, `2206.15181.pdf`, `2008.03618.pdf`, `0908.1458.pdf` + `.txt` renderings).

---

## (A) Bibliographic identification

| # | Status | Reference |
|---|---|---|
| 1 | **[V]** exists | V. Golyshev, D. Zagier, *Proof of the gamma conjecture for Fano 3-folds of Picard rank one*. Izvestiya: Mathematics **80** (2016), 24–49; DOI `10.1070/IM8343`. Author PDF (19 pp., dated 2015-06-06): `https://people.mpim-bonn.mpg.de/zagier/files/tex/GammaConjecture/GammaConj.pdf`. **No arXiv posting found.** Cited below as **[GZ1]**. |
| 2 | **[V]** exists, title differs | S. Bloch, M. Vlasenko, *Gamma functions, monodromy and Frobenius constants*. arXiv:**1908.07501** (v1 2019-08-20, v2 2020-06-23), Comm. Number Theory Phys. **15** (2021), no. 1, 91–147, DOI `10.4310/CNTP.2021.v15.n1.a3`. Cited as **[BV]**. — **The guessed title "Motivic Gamma functions" is NOT the title.** v1 was circulated as *"Gamma functions, monodromy and Apéry constants"* (**[V]** — Kerr, Remark 6.2, records the rename). |
| 3 | **[V]** exists | V. Golyshev, *Deresonating a Tate period*, arXiv:**0908.1458** (2009-08-11), 13 pp. — **but it is about *Apéry constants/limits* (`lim b_n/a_n = c·L(s_0)`), NOT about Frobenius constants.** Different invariant. |
| 4 | **[V]** exists | M. Kerr, *Unipotent extensions and differential equations (after Bloch–Vlasenko)*, arXiv:**2008.03618** (2020-08-08), 38 pp. Cited as **[K]**. |
| 5 | **[V]** exists | B. Roy, M. Vlasenko, *Frobenius constants for families of elliptic curves*, arXiv:**2206.15181** (v4 2023-05-22), Quart. J. Math. **74** (2023), no. 4, 1571–…; `academic.oup.com/qjmath/article/74/4/1571/7248967`. Cited as **[RV]**. |
| 6 | **[V]** exists | V. Golyshev, D. Zagier, *Interpolated Apéry numbers, quasiperiods of modular forms, and motivic gamma functions*. In *Integrability, Quantization, and Geometry II*, Proc. Sympos. Pure Math. **103.2**, AMS (2021), 281–301. PDF: `https://people.mpim-bonn.mpg.de/zagier/files/tex/DubrovinVolume/GZ_AperyInterpolation.pdf` (21 pp.). Cited as **[GZ2]**. **This is the paper with the biggest explicit table.** |
| 7 | **[V]** exists | V. Golyshev, M. Kerr, T. Sasaki, *Apéry extensions*, arXiv:**2009.14762**, J. London Math. Soc. **109** (2024), e12825. (About *Apéry numbers* as limiting extension classes; adjacent, not a source of κ-values.) |
| 8 | **[U]** | F. Beukers, M. Vlasenko, *Frobenius structure and p-adic zeta values*, arXiv:2302.09603, Adv. Math. (2025). p-adic analogue — relevant to the DWORK gate; **not read in this session**. |

---

## (B) THE COMPUTATIONAL DEFINITION

Two equivalent packagings exist. They give the **same numbers** for the Apéry case (checked, §C).

### B.1 Golyshev–Zagier: "Frobenius limits" — at INFINITY, on the Borel/Laplace transform

**[V] [GZ1] §6, eqns (6.1)–(6.4).** Setup for the Apéry ζ(3) case (they state "the definitions given here
work the same way for all cases"):

> We consider the Frobenius deformation of Apéry's recursion, i.e., the sequence of power series
> `A_n(ε) = Σ_{j≥0} A_n^{(j)} ε^j ∈ Q[[ε]]` defined by the initial condition `A_{−1}(ε) = 0, A_0(ε) = 1`
> and the recursion
> `(n + ε + 1)^3 A_{n+1}(ε) − P(n + ε) A_n(ε) + (n + ε)^3 A_{n−1}(ε) = 0`,  (6.1)

i.e. **you deform the recurrence by shifting `n → n + ε` everywhere** and solve with `A_0(ε) = 1`.
Then (6.2)/(6.4):

> `Φ^an(t,ε) = Σ_n A_n(ε) t^n`,  `Φ(t,ε) = t^ε Φ^an(t,ε) = Σ_{j≥0} Φ_j(t) ε^j`,
> `Φ_j(t) = Σ_{i=0}^{j} Φ_i^an(t) (log t)^{j−i}/(j−i)!`

**[V]** so `Φ_0, Φ_1, Φ_2` are the classical Frobenius basis (`Φ_j ~ (log t)^j/j!`) and (6.5)

> `L Φ(t,ε) = ε^3 t^ε`,  `L Φ_j(t) = (log t)^{j−3}/(j−3)!`

so the **higher** `Φ_j` (`j ≥ m`) solve *inhomogeneous* equations. Same construction on the Laplace side:
`a_n = A_n/n!`, `Ψ(z) = Σ a_n z^n`, deformed recursion `(n+1+ε)^4 a_{n+1}(ε) + P(n+ε) a_n(ε) + (n+ε)^2 a_{n−1}(ε) = 0`
(6.7), and `Ψ(z,ε) = z^ε Ψ^an(z,ε) = Σ Ψ_j(z) ε^j` (6.9).

**Definition [V] [GZ1] (0.3):**

> `κ_j := lim_{z→∞} Ψ_j(z) / Ψ(z)`

— a limit **at the irregular singularity z = ∞** of the order-4 Borel transform `L̃ = D_z^4 − zP(D_z) + z^2(D_z+1)^2`.
No `2πi` and no Γ-factor in this normalization; `κ_0 = 1` and `Ψ = Ψ_0` is the holomorphic solution.

**Numerical recipe [V] [GZ1] §9** (the practical one, and the one I re-implemented):

> `κ_0(ε) = C^{−ε} lim_{n→∞} A_n(ε)/A(n) = lim_{n→∞} A_n(ε)/A(n+ε)`

where `C` is the exponential growth rate of `A_n` (`C = 17 + 12√2` in the Apéry case) and
`A(n) = 2^{−9/4} π^{−3/2} C^{n+1/2}(n+1/2)^{−3/2} P(1/(64(n+1/2)^2))` is the Birkhoff–Trjitzinsky asymptotic
(`P(X) = 1 + 30X + 274X^2 − 17132X^3 + …`). Convergence with `A(n+ε)` is faster than any power of `n`;
GZ report **300 digits from 100 terms of P and n = 100, in under 10 s.**
The plain ratio `C^{−ε}A_n(ε)/A_n` converges only like `1/n` (Richardson extrapolation works — I used it).

**Relation to the Gamma class [V] [GZ1] (3.10):**

> `Γ(1+ε)^{−1} Σ_{j≥0} κ_j ε^j = 1 − (2/(d^2 N)) π^2 ε^2 + (μ_N/(d^3 N)) ζ(3) ε^3 + O(ε^4)`

(signs reconstructed from Theorem 2 + verified numerically). So **dividing the κ-series by `Γ(1+ε)` is exactly
what strips the Euler-γ's and leaves the arithmetic content** — this is the "modified/normalized gamma class".
The gamma class itself is the multiplicative class of `Γ(1+x) = 1 − γx + ((γ^2+ζ(2))/2)x^2 + …`, and
`A_X = Σ_{j=0}^{3} κ_j c_1^j` is the *principal asymptotic class* **[V]**.

### B.2 Bloch–Vlasenko: "Frobenius constants" — at a CONIFOLD (reflection) point

**[V] [BV] §3.** `L = q_0(t)D^r + … + q_r(t)`, `D = t d/dt`, indicial polynomial `I(s) = Σ q_j(0)s^{r−j}`,
`a_n(s) ∈ k(s)` defined by `a_n = 0 (n<0)`, `a_0 = 1`, `Σ_{j=0}^n p_j(n+s−j)a_{n−j}(s) = 0`, and (18)–(19):

> `Φ(s,t) = Σ_{n≥0} a_n(s) t^{n+s}` satisfies `LΦ = I(s) t^s`

Frobenius functions (21):

> `φ_{ρ,k}(t) = (1/k!) ∂^k Φ(s,t)/∂s^k |_{s=ρ} = Σ_{j=0}^{k} ((log t)^j/j!) Σ_{n≥0} (a_n^{(k−j)}(ρ)/(k−j)!) t^{n+ρ}`

**Definition 22 [V] — quoted verbatim:**

> "Assume that `c ≠ 0, ∞` is a special reflection point of `L`. Let `γ` be a path from 0 to `c` going through
> regular points of `L`. Fixing a branch of `t^s` along `γ`, we have a collection of Frobenius functions
> `{φ_{ρ,n}(t)}` defined by the analytic continuation of (21) along `γ`. The collection of Frobenius constants
> `{κ_{ρ,n}}_{ρ∈R,n≥0}` is defined by
> `(σ_c − 1) φ_{ρ,n}(t) = κ_{ρ,n} δ(t)`,  `κ_{ρ,n} ∈ C`."

Here `σ_c` = local monodromy at `c`, and `δ(t)` spans the 1-dimensional `Image(σ_c − 1)` (**Definition 21** [V]:
a *special reflection point* = regular singularity where `σ_c − 1` has rank 1 **and** all `σ_c`-invariant
solutions of `L^∨` are analytic at `c`). **So: this is at a CONIFOLD point, not at infinity.**

**Normalization [V]:** `κ` depends on the homotopy class of `γ`; `δ ↦ λδ` rescales `κ ↦ λ^{−1}κ`; changing the
branch of `t^s` multiplies the generating series by a power of `e^{2πis}`. In practice one **normalizes `κ_0 = 1`**.

**The numerical recipe [V] [BV] Lemma 24** — the cleanest "how to actually compute it":

> Suppose the special reflection point `t = c` is the singularity closest to 0, `c ∈ R_{>0}`, `|φ_{ρ,0}(t)| → ∞`
> as `t → c^−`, `a_n(ρ)` eventually of one sign, and `λ_k := lim_{n→∞} a_n^{(k)}(ρ)/(k! a_n(ρ))` exists. Then
> `κ_{ρ,0} ≠ 0` and
> `κ_{ρ,k}/κ_{ρ,0} = Σ_{j=0}^{k} (log c)^j/j! · λ_{k−j}`.

Equivalently, with `Λ(ε) := lim_{n→∞} A_n(ε)/A_n(0)` (the same deformed recurrence as GZ):

> **`κ(ε) = Σ_k κ_k ε^k = c^{ε} · Λ(ε)`.**

Since `c = 1/C`, this is *identical* to GZ's `κ_0(ε) = C^{−ε} lim A_n(ε)/A_n`. **[V] by computation** — the two
definitions agree numerically to all digits tested (§C). This is the bridge between (B.1) and (B.2).

**Main theorem [V] [BV] Theorem 30:** there is a generator `Γ_{ξ_0}(s)` of the `K[e^{±2πis}]`-module of gamma
functions for `L^∨` with

> `(I(s)/R(e^{−2πis})) Γ_{ξ_0}(s) = Σ_{n≥0} κ_{ρ,n}(s−ρ)^n`

(`I` = indicial polynomial, `R` = minimal poly with `R(σ_0)` killing `Image(σ_c−1|Sol(L^∨))`).
**Corollary 31 [V]: for `L` Picard–Fuchs, the `κ_{ρ,n}` lie in the algebra of periods with `2πi` inverted.**

**Kerr's normalized version [V] [K] Theorem 8.2** (this is where `2πi` appears explicitly):

> `κ(s) = (Q_0 (2πi)^n s^r) / (Q_c (1 − e^{2πis})^r) · Γ_c(s)`

with `Q_0, Q_c` polarization constants. **[K] Definition 6.1** `(T_c − I)Φ(s,t) =: κ(s)ψ(t)`, `κ_0 = 1`.

**Mellin-transform form [V] [RV] (1), (6):** for the Legendre family, with `δ(t)` the period analytic at `t=1`
continued to `t=0`,

> `κ(s) = s^2 ∫_0^1 t^{s−1} δ(t) dt = Σ_{n≥0} κ_n s^n`,
> "The coefficients `κ_0, κ_1, …` of its power series expansion are called Frobenius constants."

i.e. **κ(s) is (up to `s^r`) the Mellin transform / motivic Γ-function of the continued period.**
General [RV] Theorem 3 form: `κ(s) = 2πi s^2 ∫_0^∞ t(z)^{s−1} z f(z) dt(z)`.

**Hypergeometric closed form [V] [BV] Prop. 26** — for `L = ∏(D+β_j−1) − t∏(D+α_j)`, `A(s) = ∏Γ(s+α_j)/∏Γ(s+β_j)`,
path 0→1 along R:

> `1/A(s) = Σ_{n≥0} κ_{ρ,n}(s−ρ)^n`,  `ρ ∈ R`.

Kerr's equivalent **[V] [K] Ex. 6.7:** for `L = D^r + tP_1(D)`, `P_1(D) = −∏(D+a_j)`, conifold at `c=1`:
`κ(s)^{−1} = ∏_{j=1}^{r} Γ(s+a_j)/(Γ(s+1)Γ(a_j))`.

**Weight statement [V] [GZ1] abstract:** "The Gamma Conjecture for Fano 3-folds always contains a rational
multiple of the number ζ(3). We present numerical evidence suggesting that higher Frobenius limits of
Apéry-like differential equations may be related to multiple zeta values."
**[V] [BV] p.21:** "We do *not* expect the Frobenius constants of a Gauß–Manin connection to be expressible as
Q-linear combinations of products of zeta or multiple zeta values in general."

---

## (C) KNOWN VALUES — the Apéry operators. **PRIOR CONFIRMED.**

### C.1 Apéry ζ(3) operator — order 3, MUM at 0, conifold at `c = 17 − 12√2`

`L = D^3 − t(34D^3 + 51D^2 + 27D + 5) + t^2(D+1)^3` (annihilates `Σ_n A_n t^n`, `A_n = Σ_k C(n,k)^2C(n+k,k)^2`).

**[V] [BV] Example 29 — verbatim:**
> "In [8] Golyshev and Zagier computed the Frobenius constants `κ_n = κ_{0,n}` along with the first higher one
> for the direct path joining `t = 0` and `t = c`:
> `κ_0 = 1, κ_1 = 0, κ_2 = −π^2/3 = −2ζ(2), κ_3 = (17/6) ζ(3)`."

> **⇒ THE PRIOR IS CONFIRMED: the Frobenius constant of the Apéry ζ(3) operator at its conifold point
> `c = 17−12√2` is `κ_3 = (17/6)·ζ(3)` — a rational multiple of ζ(3).**
> **The normalization is `κ_0 = 1` (i.e. `δ` scaled so the holomorphic solution's constant is 1), path = the
> real segment `[0, 17−12√2]`, and there is NO `(2πi)^3` and NO Γ-factor.** The guessed form `ζ(3)/(2πi)^3`
> is **wrong** for this normalization. (`2πi` enters only via [K] Thm 8.2 when `κ` is written in terms of the
> conifold Γ-function `Γ_c`, or via [BV] Cor. 31 "periods with 2πi inverted".)

Confirmed independently three ways:
* **[V] [K] Example 9.8:** "Its Picard–Fuchs operator `L = D^3 − t(34D^3+51D^2+27D+5) + t^2(D+1)^3` is
  self-adjoint, and we have `κ_1 = 0, κ_2 = −2ζ(2), κ_3 = (17/6)ζ(3)` [GZ]."
* **[V] [GZ2] §7 eq. (47)** (full table, below).
* **[V] my own numerics** (deformed recurrence + Richardson): `κ_3 = 3.4058278922…` vs `(17/6)ζ(3) = 3.4058278923…`

**Full table [V] [GZ2] (47) — Apéry ζ(3), `κ^{(0)}_j`, verbatim:**

```
κ0 = 1                κ1 = 0               κ2 = −π²/3            κ3 = (17/6) ζ(3)
κ4 = π⁴/45            κ5 = −(17/18)π²ζ(3) + (7/3)ζ(5)
κ6 = (4/945)π⁶ + 4ζ(3)²
κ7 = −(7/9)π²ζ(5) + (7/108)π⁴ζ(3) − (5/3)ζ(7)
κ8 = −(11/37800)π⁸ + 6ζ(5)ζ(3) − (4/3)π²ζ(3)²
κ9 = (8/9)ζ(9) + (34/9)ζ(3)³ + (5/9)π²ζ(7) + (149/11340)π⁶ζ(3) + (5/54)π⁴ζ(5)
κ10 = −(107/249480)π¹⁰ − 4ζ(5)² − 8ζ(3)ζ(7) + (4/45)π⁴ζ(3)² − 2π²ζ(3)ζ(5)
κ11 = −(503/680400)π⁸ζ(3) + (199/5670)π⁶ζ(5) + (49/270)π⁴ζ(7) − (34/27)π²ζ(3)³
      − (8/27)π²ζ(9) + (28/3)ζ(3)²ζ(5) + 66ζ(11) + (2/3) ζ(3,5,3)
```
Weight is homogeneous (`κ_j` has weight `j`). `κ_11` is the **first** to need an MZV.
**[V] [GZ1] §9** gives the same data as `log κ(ε) = Σ λ_j ε^j`:
`λ1=0, λ2=−2ζ(2), λ3=(17/6)ζ(3), λ4=−3ζ(4), λ5=(7/3)ζ(5), λ6=−(2/3)ζ(6)−(1/72)ζ(3)²,
λ7=−(5/3)ζ(7)+(1/6)ζ(3)ζ(4), λ8=(29/12)ζ(8)−(11/18)ζ(3)ζ(5),
λ9=(8/9)ζ(9)+(5/3)ζ(3)ζ(6)+(11/3)ζ(4)ζ(5)+(17/648)ζ(3)³,
λ10=−(147/5)ζ(10)−(59/18)ζ(3)ζ(7)−(121/18)ζ(5)²−(17/36)ζ(4)ζ(3)²,
λ11=66ζ(11)+(59/3)ζ(4)ζ(7)+(110/3)ζ(5)ζ(6)+(215/36)ζ(8)ζ(3)+(187/108)ζ(3)²ζ(5)+(2/3)ζ(3,5,3)`.
**[V] by computation:** `exp(Σλ_jε^j)` reproduces (47) **exactly** (agreement to 30 digits, j ≤ 8), and both
match my independent Richardson extrapolation to ~1e-9.

**⚠ ERRATUM FOUND [V]:** **[BV] Example 29 misprints `κ_5`.** BV print
`κ_5 = (7/5)ζ(5) − (17/3)ζ(2)ζ(3)`. The correct value is
**`κ_5 = (7/3)ζ(5) − (17/3)ζ(2)ζ(3)`** (= `−(17/18)π²ζ(3) + (7/3)ζ(5)`, [GZ2] (47)).
Numerically `κ_5 = −8.78522655786…`; `(7/3)`-version `= −8.7852265564`, `(7/5)`-version `= −9.7530257945`.
BV's other listed values (`κ_4 = π⁴/45 = (4/5)ζ(2)² = 2ζ(4)`, `κ_11 ∋ (2/3)ζ(3,5,3)`) are correct.

### C.2 Apéry ζ(2) operator — order 2, `c = (−11 + 5√5)/2`

`L = D^2 − t(11D^2 + 11D + 3) − t^2(D+1)^2`, recurrence `(n+1)^2 u_{n+1} = (11n^2+11n+3)u_n + n^2 u_{n−1}`.
This is Beauville family **case D** (`Γ_1(5)`) in [RV] and BV's Example 28.

**[V] [BV] Example 28** (path `0 → (−11+5√5)/2`) and **[V] [RV] Table 2, case D** agree:
```
κ0 = 1,  κ1 = 0,  κ2 = −(7/5)ζ(2) = −(7/30)π²,  κ3 = 2 ζ(3),
κ4 = (1/2)ζ(4) = π⁴/180,   κ5 = ζ(5) − 3ζ(2)ζ(3) = ζ(5) − (π²/2)ζ(3),
κ6 = (87/16)ζ(6) + (5/2)ζ(3)²,
κ7 = −(55/8)ζ(7) − (5/2)ζ(5)ζ(2) − (5/4)ζ(3)ζ(4).
```
**⚠ SECOND ERRATUM [V]:** **[BV] Example 28 prints `κ_6 = (87/16)ζ(6) − (5/2)ζ(3)²`; the sign is wrong.**
Numerically `κ_6 = 9.1441548958`; `+` version `= 9.1441548956`, `−` version `= 1.9194509035`.
(`κ_2,κ_3,κ_4,κ_5,κ_7` as printed by BV all check out.)

**Separate notion, don't confuse:** [K] Theorem 10.10 / Example: for this same operator the **Apéry constant**
(= Apéry *limit* `lim b_n/a_n`) is `κ(1) = ζ(2)/5` **[V]**; and for the ζ(3) operator [GZ2] notes the Apéry limit
is `(1/6)ζ(3)` **[V]** (= [GZ2] (48) `κ^{(0)}_{1,0} = (1/6)ζ(3)`, "a rewording of Apéry's original discovery").

---

## (D) TABLES

### D.1 All 17 rank-1 Fano 3-folds — [V] [GZ1] Theorem 2 (verbatim structure)

> Let `Ψ_0 = Ψ, Ψ_1, Ψ_2, Ψ_3` be the Frobenius solutions of the 4th order equation satisfied by
> `Ψ(z) = Σ A_n z^n/n!`, where `F_{N,d}(τ) = Σ A_n t_{N,d}(τ)^n` for one of the 17 pairs `(N,d)`. Then
> `κ_1 = −γ`,
> `κ_2 = γ²/2 − (12/(d²N) − 1/2) ζ(2)`,
> `κ_3 = −γ³/6 + (12/(d²N) − 1/2) γζ(2) + (μ_N/(d³N) − 1/3) ζ(3)`.

with `μ_N = 62` (N=1) or `(1/2)Σ_{M|N} M h_M` (N>1). **[V] Table 1** gives
`μ_1=62, μ_2=40, μ_3=30, μ_4=24, μ_5=20, μ_6=17, μ_7=15, μ_8=13, μ_9=12, μ_11=10`.
Apéry case `(N,d)=(6,1)`: `κ_1=−γ, κ_2=γ²/2−(3/2)ζ(2), κ_3=−γ³/6+(3/2)γζ(2)+(5/2)ζ(3)` [V] (0.4).
(Note: **these `κ_j` are on the `z=∞`/Borel side and carry Euler-γ**; the `γ`-free constants of §C are
`Γ(1+ε)^{−1}`-normalized, eq. (3.10). E.g. `5/2 = μ_6/6 − 1/3` and after the `Γ(1+ε)^{−1}` twist it becomes `17/6`.)

### D.2 Beauville's stable elliptic families — [V] [RV] Table 2 ("conjectural, numerically to 75 digits")

Operators `L = θ² − t[Aθ(θ+1) + λ] + Bt²(θ+1)²`; `*` = not identified.

| Zagier label | (A,B,λ) | group | c | κ0 | κ1 | κ2 | κ3 | κ4 | κ5 |
|---|---|---|---|---|---|---|---|---|---|
| A | (7,−8,2) | Γ0(6) | 1/8 | 1 | 0 | −π²/6 | ζ(3) | π⁴/80 | −(7/16)ζ(5) − (5/16)π²ζ(3) |
| C | (10,9,3) | Γ0(6) | 1/9 | 1 | 0 | −π²/6 | (2/3)ζ(3) | * | * |
| D | (11,−1,3) | Γ1(5) | (−11+5√5)/2 | 1 | 0 | −(7/30)π² | 2ζ(3) | π⁴/180 | ζ(5) − (π²/2)ζ(3) |
| E | (12,32,4) | Γ0(8) | 1/8 | 1 | 0 | −π²/12 | −(5/4)ζ(3) | * | * |
| F | (17,72,6) | h⁻¹Γ0(6)h | 1/9 | 1 | 0 | 0 | −(11/3)ζ(3) | * | * |
| G | (0,−16,0) | Γ0(8) | 1/4 | 1 | 0 | −π²/12 | (1/2)ζ(3) | −π⁴/720 | (3/8)ζ(5) − (π²/24)ζ(3) |

**[V] [RV] (12), case G in closed form (proved):**
`κ_G(s) = exp( 2 Σ_{k≥2} (ζ(k)/k)(2^{1−k} − 1)(−s)^k ) = 1 − (π²/12)s² + (ζ(3)/2)s³ + …`
**[V] [RV] Theorem 3:** `κ_{2+m} = [ (4π²/b) (1/m!) ∫_{z_0/(bz_0+1)}^{z_0} log^m(t(z)) g(z) dz ]_reg`, with
`g = (1/2πi)(t'/t)f` a **weight-3 modular form** — i.e. these κ's are **iterated integrals of modular forms**.

### D.3 The 14 hypergeometric CY operators

**No paper found that tabulates them under the name "Frobenius constants."** But they are *completely
determined in closed form* by **[V] [BV] Prop. 26 / [K] Ex. 6.7**: with `β = (1,1,1,1)` and exponents
`a = (a_1,…,a_4)`, the conifold (`t=1`) Frobenius constants at `ρ=0` are the Taylor coefficients of
`κ(s) = ∏_{j} Γ(1+s)Γ(a_j)/Γ(s+a_j)`, so
`log κ(s) = Σ_{k≥2} ((−1)^k/k)( 4ζ(k) − Σ_j ζ(k, a_j) ) s^k` (Hurwitz), which is a **Q-combination of ζ-values
whenever the `a_j` run over a full set of `j/N` with `gcd(j,N)=1`** (Gauss multiplication).

**[V] [K] Ex. 6.7, mirror quintic worked out** (`r=4`, `a=(1/5,2/5,3/5,4/5)`): expanding
`∏_{j=1}^{4} Γ(s+j/5)/(Γ(s+1)Γ(j/5))` gives the LMHS column
`(1, −5log5, 10ζ(2) + (25/2)log²5, −40ζ(3) − 50(log5)ζ(2) − (125/6)log³5)`;
after renormalizing by `t/5^5` this is `(1, 0, 10ζ(2), −40ζ(3))`, and in the integral basis
`(ε_0, ε_1, 5ε_2, 5ε_3)` the invariants are **`50ζ(2)` and `−200ζ(3)`**.

### D.4 Zagier's sporadic Apéry-like operators
No table of Frobenius constants for the full sporadic list found. [RV] covers the 6 **second-order**
(Beauville/`(A,B,λ)`) sporadic cases minus case B (excluded because `t(0)` is not a singularity **[V]**).

---

## (E) HIGHER WEIGHT — ζ(5) and beyond. **YES, it exists, in two forms.**

1. **Higher Frobenius constants of the order-3 Apéry ζ(3) operator already contain ζ(5) [V]:**
   `κ_5 = (7/3)ζ(5) − (17/18)π²ζ(3)` — exactly the "mixed ζ(3)/ζ(5)" datum. Then `κ_7 ∋ −(5/3)ζ(7)`,
   `κ_8 ∋ 6ζ(5)ζ(3)`, `κ_9 ∋ (8/9)ζ(9)`, `κ_{10} ∋ −4ζ(5)²`, `κ_{11} ∋ 66ζ(11) + (2/3)ζ(3,5,3)`.
   These come from the `j ≥ m` **higher** Frobenius functions, which solve *inhomogeneous* PF equations
   ([GZ1] (6.5), [BV] (22) `(D−ρ)^{k−m+1}Lφ_{ρ,k}=0`), so they are not periods of the original VHS —
   **[V] [BV]:** "there is no reason to expect that the operators `(D−ρ)^j L` with `j > 0` are geometric.
   From this point of view, it is surprising that the higher Frobenius constants in the above examples are periods."
   Theorem 30 is what explains it.

2. **A structural higher-weight conjecture [V] [GZ2] §7.** GZ compute a *second* expansion, at `ε = 1`:
   `κ^{(0)}_{1,j} := (1/j!) d^j/dx^j [ κ^{(0)}(x)/(1+x)^3 ] |_{x=1}`, finding
   `κ_{1,0} = (1/6)ζ(3)`, `κ_{1,1} = −π⁴/90`, `κ_{1,2} = −(1/18)π²ζ(3) + (11/3)ζ(5)`,
   `κ_{1,3} = −(13/1890)π⁶`, `κ_{1,4} = (59/3)ζ(7) + (19/540)π⁴ζ(3) − (11/9)π²ζ(5)`,
   `κ_{1,5} = −(29/56700)π⁸ − 10ζ(3)ζ(5) − 4ζ(3,5)`.
   And **[V]** they state: "we predicted in [GZ1] that the top-weight components of the leading expansion
   coefficients of kappa at 0 and at 1, namely the numbers `κ^{(0)}_j` for `j = 0,…,10` and `κ^{(0)}_{1,j}` for
   `j = 0,…,4`, should be equal to the expansion coefficients of the **normalized gamma class of the orthogonal
   Grassmannian OG(5,10)**", with
   `Γ̂^norm(V) = ∏_α Γ(1+r_α) / Γ(1 + (−K_V)/d)^d`.
   **This is the "higher-weight analogue": the higher κ's of the order-3 Apéry operator are conjecturally the
   gamma class of a higher-dimensional Fano (OG(5,10)), whose gamma class naturally contains ζ(5), ζ(7), ….**

3. **Motivic gamma function at higher weight [V] [GZ2] (31)/(32):**
   `Γ^mot_H(s) := ∫ Φ(t) t^s dt/t`, and "the comparison of higher derivatives rather than values …
   `d^r Γ^mot_H(s)/ds^r = ∫ Φ(t) t^s log(t)^r dt/t` is an equally important subject, pertaining now to the study
   of mixed, rather than pure, motives."

4. **Not found:** no paper found stating that an order-3 operator has its *first non-trivial* Frobenius constant
   equal to a rational multiple of ζ(5) (the ζ(5) analogue of `κ_3 = (17/6)ζ(3)`). **[U]** — this appears to be
   an open slot. The nearest things are (a) the `κ_5` entries above, (b) [RV] Table 2's `κ_5` column for
   *second*-order operators (case D: `κ_5 = ζ(5) − (π²/2)ζ(3)`; case A: `−(7/16)ζ(5) − (5/16)π²ζ(3)`;
   case G: `(3/8)ζ(5) − (π²/24)ζ(3)`).

---

## Other pointers found (not fully read)

* **[U]** F. Beukers, M. Vlasenko, *Frobenius structure and p-adic zeta values*, arXiv:2302.09603 →
  Adv. Math. 2025. p-adic Frobenius structure of CY operators at a MUM point, entries = Q-combinations of
  `ζ_p(k)`. Relevant to the DWORK gate; **read next**.
* **[U]** D. Broadhurst found MZV expressions for the Apéry `κ_n` up to `n = 15` (cited in [BV] as ref [5]).
* **[U]** S. Galkin, *Apéry constants of homogeneous varieties*, arXiv:1604.04652 (table of Apéry constants —
  the `lim b_n/a_n` notion, not Frobenius constants).
* **[V]** Golyshev–Kerr–Sasaki, *Apéry extensions*, arXiv:2009.14762 / JLMS 109 (2024) e12825 — Apéry numbers as
  limiting extension classes of higher cycles on LG models; "Apéry motive".
* **[U]** Malmendier–Schultz, *On Mirror Symmetry and Irrationality of Zeta Values*, arXiv:2403.07349 — GZ's
  17 families from a virtual-instanton/Eichler-integral viewpoint. No new κ-values in the abstract.

## Verification script

The deformed-recurrence + Richardson computation that confirmed §C is at
`…/scratchpad/frob2.py` (mpmath, `K=8` ε-truncation, `n ≤ 6000`, ~1e-9 accuracy).
Recipe: run `(n+ε+1)^m A_{n+1} = P(n+ε)A_n ∓ (n+ε)^m A_{n−1}` as a truncated ε-series with `A_0 = 1`,
normalize `u_n = A_n(ε)/A_n(0)` at every step (keeps floats O(1)), Richardson-extrapolate `u_n → Λ(ε)`
in `1/n`, then `κ(ε) = c^ε Λ(ε)`.
