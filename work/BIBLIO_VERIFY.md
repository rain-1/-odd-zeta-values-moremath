# BIBLIO_VERIFY — task W5, bibliography verification of the four paper drafts

Date: 2026-07-25.  Scope: `papers_out/lucas2nd`, `papers_out/padiclimits`,
`papers_out/frobenius`, `papers_out/sharp12`.

Rules followed: every entry below was resolved against a *fetched* source
(arXiv API metadata, publisher/NUMDAM/OEIS record, or the text of the cited
work itself).  Nothing was invented.  Where the citing sentence could not be
confirmed exactly as written, the sentence was softened rather than the entry
blessed; those cases are marked **DOWNGRADED**.

---

## 0. Summary

| paper | UNVERIFIED at start | resolved | softened | still marked |
|---|---|---|---|---|
| A `lucas2nd`      | 6 (brief said 7 — only 6 exist) + 5 title-less | 11 | 0 | 0 |
| B `padiclimits`   | 14 + 5 incomplete secondaries + initials everywhere | 19 | 1 | 0 |
| C `frobenius`     | 3 | 3 | 0 | 0 |
| D `sharp12`       | 0 (5 spot-checks requested) | 5/5 confirmed | 0 | 0 |

Compile status after edits (3 × pdflatex each): **all four clean, zero
undefined references or citations.**

Two bibliographic **errors** were found in already-"verified" entries and
corrected (§5).

---

## 1. Paper A — `papers_out/lucas2nd`

The brief said 7 UNVERIFIED keys; the draft contained **6**
(`grep -c 'bibitem{UNVERIFIED-'` = 6).  All 6 resolved; all 5 title-less
secondaries completed; surname-only entries given initials.

### 1.1 `UNVERIFIED-Gessel1982` → `Gessel1982` — RESOLVED

* Record: I. M. Gessel, *Some congruences for Apéry numbers*, J. Number
  Theory **14** (1982), no. 3, 362–368; DOI 10.1016/0022-314X(82)90071-3.
* Evidence: publisher record via search; independently, the bibliography of
  Malik–Straub (arXiv:1508.00297, PDF fetched) reads verbatim
  "`[Ges82] I. M. Gessel. Some congruences for Apéry numbers. Journal of
  Number Theory, 14(3):362–368, June 1982.`"
* Claim check (`sec-intro.tex:18`, `sec-weight3.tex:251`: "This is classical"
  for `a_{ap+r} ≡ a_a a_r (mod p)`): the Malik–Straub abstract states "In
  1982, Gessel showed that the Apéry numbers associated to the irrationality
  of ζ(3) satisfy Lucas congruences."  **Supported.**

### 1.2 `UNVERIFIED-vdPoorten1979` → `vdPoorten1979` — RESOLVED (strongest evidence in the set)

* Record: A. van der Poorten, *A proof that Euler missed… Apéry's proof of
  the irrationality of ζ(3)*, Math. Intelligencer **1**:4 (1978/79), 195–203.
* Evidence: full scan fetched (`ega-math.narod.ru/Apery1.pdf`), plus the
  bibliography of Fischler's Bourbaki exposé (repo copy) and of Osburn–Sahu.
* Claim check (`sec-minimal.tex:539–558`).  §8 of the scan is titled
  "**Some Rather Complicated but Ingenious Explanations**" and contains,
  verbatim:
  - "The following is principally due to **Zagier and Cohen**."
  - `B_{n,k} = 4(2n+1)(k(2k+1) − (2n+1)^2) (n k)^2 (n+k k)^2`
  - `A_{n,k} = B_{n,k}C_{n,k} + 5(2n+1)(−1)^{k−1}k/(n(n+1)) (n k)(n+k k)`
  - "After some massive **reorganisation** (9) becomes `A_{n,k} − A_{n,k−1}`"
  **All four match the draft exactly.**
* **Quotation fix applied:** the draft quoted "reorganization"; the source
  reads "reorganisation".  Corrected in `sec-minimal.tex:549` (this is a
  direct quotation, so the spelling is load-bearing).

### 1.3 `UNVERIFIED-Nesterenko1996` → `Nesterenko1996` — RESOLVED

* Record: Yu. V. Nesterenko, *A few remarks on ζ(3)*, Mat. Zametki **59**
  (1996), no. 6, 865–880; English transl. Math. Notes **59** (1996), 625–636.
* Evidence: two independent published bibliographies — Fischler Bourbaki
  (repo copy, `[Ne2]`) and Zudilin arXiv:math/0202159 (PDF fetched, `[Ne]`),
  both giving 59(6), 865–880 [625–636].
* Claim check ("Nesterenko's Lemma 1, reproduced as formula (3) of
  [Zudilin0202159], amounts to the weight `H^{(3)}_k + (2H_k − H_{n+k} −
  H_{n−k})H^{(2)}_k`"):
  - Zudilin math/0202159 states "**Lemma 1 (cf. [Ne, Lemma 1])**" and its
    formula **(3)** is `u_n = 2Σ A_{2k}`,
    `v_n = 2Σ_k A_{2k} Σ_{l≤k} l^{-3} + Σ_k A_{1k} Σ_{l≤k} l^{-2}`.
  - The identification of the weight requires `A_{1k} = 2A_{2k}(2H_k −
    H_{n+k} − H_{n−k})`.  Verified symbolically (sympy, exact residues of
    `R_n`) for all `0 ≤ k ≤ n`, `n = 1..4`: exact match in every case.
  **Supported.**

### 1.4 `UNVERIFIED-PauleSchneider2003` → `PauleSchneider2003` — RESOLVED

* Record: P. Paule and C. Schneider, *Computer proofs of a new family of
  harmonic number identities*, Adv. Appl. Math. **31** (2003), no. 2,
  359–378; DOI 10.1016/S0196-8858(03)00016-2 (dblp record fetched).
* Evidence for the claim: RISC preprint PDF fetched
  (`www3.risc.jku.at/publications/download/risc_200/HarmonicNumberIds.pdf`).
  Its identity **(4)** is, verbatim,
  `Σ_{j=0}^n (1 − 4jH_j + 4jH_{n−j}) (n j)^4 = (−1)^n (2n n)`
  — exactly the identity attributed in `sec-minimal.tex:569`.
* "Ahlgren's": the preprint says "This motivated **S. Ahlgren** to do a
  heuristic search… The result of this study was a family of conjectured
  identities, namely (1)–(5) above."  **Supported.**
* "only weight-one identities; `H^{(3)}` never appears there": confirmed —
  the paper defines only `H_n = 1 + 1/2 + … + 1/n`; the only superscripts
  `(α)` in the text are the exponent index of `R_n^{(α)}, S_n^{(α)}`, not
  harmonic orders.  **Supported.**

### 1.5 `UNVERIFIED-Fischler2004` → `Fischler2004` — RESOLVED (flagged ready-to-promote; confirmed and promoted)

* Record: S. Fischler, *Irrationalité de valeurs de zêta (d'après Apéry,
  Rivoal, …)*, Séminaire Bourbaki exp. 910, Astérisque **294** (2004),
  27–62; arXiv:math/0303066.
* Evidence: NUMDAM item `SB_2002-2003__45__27_0` fetched — "Astérisque,
  no. 294 (2004), Exposé no. 910, pp. **27–62**"; arXiv API journal-ref
  confirms the same string and the arXiv id read from the repo metadata.
* Claim check (`sec-minimal.tex:550`, "Fischler [§1.2] likewise calls it
  'une simple vérification'"): the repo copy of the source
  (`papers/05-fischler-2003-bourbaki-survey/exposearxiv.tex`) has §1.2
  = "Formules explicites", which contains the same `B_{n,k}` and `A_{n,k}`
  and then: "La démonstration donnée ci-dessus … n'est qu'**une simple
  vérification**, à condition d'être capable d'exhiber les suites doubles
  `B_{n,k}` et `A_{n,k}`".  **Supported, verbatim.**

### 1.6 `UNVERIFIED-Schneider2007` → `Schneider2007` — RESOLVED

* Record: C. Schneider, *Apéry's Double Sum is Plain Sailing Indeed*,
  Electron. J. Combin. **14** (2007), #N5, 3 pp.; DOI 10.37236/1006.
  (PDF fetched from combinatorics.org; the printed footer reads "the
  electronic journal of combinatorics 14 (2007), #N5", 3 pages.)
* Claim check (`sec-minimal.tex:539`):
  - "creative telescoping": the paper's eq. (4) is introduced as "the
    **creative telescoping equation**".  **Supported.**
  - "Karr's ΠΣ difference fields": the paper itself says only "Using the
    summation package **Sigma**".  Sigma *is* Schneider's extension of Karr's
    difference-field summation — stated explicitly by the same author in
    Paule–Schneider 2003 ("based on an extension of **Karr's** summation
    algorithm in difference fields"), which I read.  **Supported indirectly**;
    recorded here rather than softened, since the attribution is the author's
    own.
  - "a certificate whose numerator, after `n ↦ n−1`, is exactly the numerator
    of our `G(n,k)`": the paper's certificate has
    `p_0(n,k) = 4k^4(n+1)^2(n+2)(2n+3)(2k^2 − 3k − 4n^2 − 12n − 8)`.
    Substituting `n ↦ n−1` gives the factor
    `4(2n+1)(2k^2 − 3k − 4n(n+1)) = 4(2n+1)[(k−1)(2(k−1)+1) − (2n+1)^2]`,
    i.e. the numerator of van der Poorten's `B_{n,k−1}` — which is the
    draft's `G(n,k)`.  **Supported** (checked by hand from the fetched text).

### 1.7 Title-less / initial-less secondaries — COMPLETED

All from a single arXiv API batch query (`export.arxiv.org/api/query`):

| key | completion |
|---|---|
| `Cooper2302` | S. Cooper, *Apéry-like sequences defined by four-term recurrence relations* |
| `Gorodetsky` | O. Gorodetsky, *New representations for all sporadic Apéry-like sequences, with applications to congruences*, Exp. Math. **32** (2023), no. 4, 641–656 |
| `MirrorNote` | **A. Adolphson and S. Sperber** (the entry had *no author at all*), *A note on the integrality of mirror maps* |
| `OsburnSahu` | R. Osburn and B. Sahu, *Supercongruences for Apéry-like numbers*, Adv. Appl. Math. **47** (2011), no. 3, 631–638 (the draft had only the descriptive phrase "survey on supercongruences") |
| `Zudilin0202159` | W. Zudilin, *An elementary proof of Apéry's theorem* |

Initials added, and journal data completed where the arXiv record carries a
journal-ref, for: `ChamStraub` (Amer. Math. Monthly **128** (2021), no. 9,
811–824 — publisher record also checked), `Delaygue` (Adv. Math. **234**
(2013), 414–452), `DRR`, `HenningsenStraub`, `MalikStraub`, `MellitVlasenko`,
`Straub1401` (Algebra Number Theory **8** (2014), 1985–2008), `VMmum`,
`VMcanon`, `BVone`/`BVtwo`/`BVthree` (IMRN volumes/pages; `BVthree` given its
full subtitle).

---

## 2. Paper B — `papers_out/padiclimits`

All 14 UNVERIFIED keys resolved; 5 incomplete secondaries completed; author
initials supplied throughout (the draft's header comment said "Author
initials are omitted throughout because the sources record surnames only" —
that comment is now removed, since the initials have been obtained).

Keys were renamed (`UNVERIFIED-X` → a real key) at all citation sites.

### 2.1 The 14

| old key | resolved to | evidence |
|---|---|---|
| `UNVERIFIED-Apery` | R. Apéry, *Irrationalité de ζ(2) et ζ(3)*, in: Journées Arithmétiques (Luminy, 1978), Astérisque **61** (1979), 11–13 | three independent fetched bibliographies (LSZ 2025 repo tex `[Ape1979]`, Osburn–Sahu `[1]`, Schneider EJC `[1]`) + OEIS A005259 |
| `UNVERIFIED-Beukers` | **split into two** — see §2.2 | |
| `UNVERIFIED-Supercong` | F. Beukers, *Some congruences for the Apéry numbers*, J. Number Theory **21** (1985), 141–155; M. J. Coster, *Supercongruences*, PhD thesis, Univ. Leiden, 1988; T. Ishikawa, *Super congruence for the Apéry numbers*, Nagoya Math. J. **118** (1990), 195–202 | Osburn–Sahu PDF bibliography `[4]`,`[8]`; Malik–Straub PDF `[Beu85]`,`[Cos88]`; Project Euclid record for Ishikawa |
| `UNVERIFIED-Cooper` | S. Cooper, *Sporadic sequences, modular forms and new series for 1/π*, Ramanujan J. **29** (2012), no. 1–3, 163–183 | Malik–Straub PDF `[Coo12]` + Springer record |
| `UNVERIFIED-Gessel` | as §1.1 | as §1.1 |
| `UNVERIFIED-GrossKoblitz` | B. H. Gross and N. Koblitz, *Gauss sums and the p-adic Γ-function*, Ann. of Math. (2) **109** (1979), no. 3, 569–581 | publisher/secondary records |
| `UNVERIFIED-Kazandzidis` | V. Brun, J. O. Stubban, J. E. Fjeldstad, R. Tambs Lyche, K. E. Aubert, W. Ljunggren and E. Jacobsthal, *On the divisibility of the difference between two binomial coefficients*, Den 11te Skand. Matematikerkongress (Trondheim 1949), Oslo 1952, 42–54; G. S. Kazandzidis, *Congruences on the binomial coefficients*, Bull. Soc. Math. Grèce (N.S.) **9** (fasc. 1) (1968), 1–12 | Meštrović survey arXiv:1111.3057 (PDF fetched), refs `[12]`, `[48]` |
| `UNVERIFIED-KrattenthalerRivoal` | C. Krattenthaler and T. Rivoal, *Hypergéométrie et fonction zêta de Riemann*, Mem. Amer. Math. Soc. **186** (2007), no. 875, x+87 pp. | LSZ 2025 repo tex `[KR2007]` |
| `UNVERIFIED-KubotaLeopoldt` | T. Kubota and H. W. Leopoldt, *Eine p-adische Theorie der Zetawerte. Teil I*, J. Reine Angew. Math. **214/215** (1964), 328–339; DOI 10.1515/crll.1964.214-215.328 | EUDML/De Gruyter records |
| `UNVERIFIED-Morita` | Y. Morita, *A p-adic analogue of the Γ-function*, J. Fac. Sci. Univ. Tokyo Sect. IA Math. **22** (1975), no. 2, 255–266 | publisher/secondary records |
| `UNVERIFIED-RhinViola` | G. Rhin and C. Viola, Acta Arith. **77** (1996), no. 1, 23–56 and Acta Arith. **97** (2001), no. 3, 269–293 | LSZ 2025 repo tex `[RV2001]`; Brown–Zudilin repo tex `[RV96]`,`[RV01]` |
| `UNVERIFIED-Sprang` | **DOWNGRADED** — see §2.3 | |
| `UNVERIFIED-Zagier` | D. Zagier, *Integral solutions of Apéry-like recurrence equations*, in: Harnad–Winternitz (eds.), Groups and Symmetries, CRM Proc. Lecture Notes **47**, AMS 2009, 349–366 | Osburn–Sahu PDF `[18]` |
| `UNVERIFIED-ASvSZ` | G. Almkvist, D. van Straten and W. Zudilin, *Apéry limits of differential equations of order 4 and 5*, Fields Inst. Commun. **54**, AMS 2008, 105–123 | full PDF fetched from uni-mainz |

Claim checks worth recording:

* **Kazandzidis** (`:669`, `:1174`): the Meštrović survey states the
  Jacobsthal–Kazandzidis congruence `(np mp) ≡ (n m) (mod p^t)`, `t =
  v_p(p^3 nm(n−m))`, and explicitly derives the iterated `p^a`-version.  This
  is exactly what "the limit exists … at 3 digits per level" needs.
  **Supported.**
* **Morita** (`:1202`): Morita 1975 defines Γ_p; the *displayed product*
  `n! = p^{v_p(n!)} Π_i (−1)^{n_i+1} Γ_p(n_i+1)` is the standard iterate of
  Morita's relation `Γ_p(n+1) = (−1)^{n+1} n!/(p^{⌊n/p⌋}⌊n/p⌋!)`.  Verified
  numerically (exact integer arithmetic) for `p ∈ {3,5,7}`, `n ∈
  {1,5,17,40,123}` — exact in all cases.  A parenthetical noting that the
  product form is the iterate has been added to the bib entry.
  **Supported.**
* **Krattenthaler–Rivoal** (`:1697`): LSZ 2025 (repo tex, line 734 and the
  Prop. at line 595) apply "the Andrews transformation `\cite[Théorème
  8]{KR2007}`" to a very-well-poised `₉V₈` differentiated in ε, and obtain
  `ρ_n = Σ_{0≤i≤k≤n} 2^{4(n−k)} (2i i)^2 (2n−2i n−i)(2k−2i k−i)(2k k)^2
  (2n−2k n−k)`, with `ρ_{n,3} = 768ρ_n`.  Character-for-character the same
  display as the draft.  **Supported.**  (The draft's bib note said "in the
  form used by [LSZ2025] (their Theorem 8)"; "Théorème 8" is
  Krattenthaler–Rivoal's, not LSZ's — the entry now says so.)
* **Cooper** (`:159`, "Cooper's three additional cases"): Cooper's own
  Ramanujan J. abstract says "*Two* new sequences".  Malik–Straub, which is
  the labelling source this paper uses, says "**Cooper also found three
  additional sporadic solutions**, including `s_18(n) = …`, as well as `s_7`
  and `s_10`", all cited to `[Coo12]`.  **Supported via the labelling
  source**; a parenthetical recording that attribution has been added to the
  entry.
* **Supercong** (`:182`): the *exact* displayed form `A(mp^r) ≡ A(mp^{r−1})
  (mod p^{3r})` is Coster's (Straub, arXiv:2301.12248, §3: "further studied
  by Coster [Cos88] who showed that the Apéry numbers satisfy `A(p^r n) ≡
  A(p^{r−1} n) (mod p^{3r})` for all primes `p ≥ 5`"); Beukers 1985 has the
  `mp^r − 1` variant.  The draft's grouped attribution "of Beukers, Coster
  and Ishikawa and their descendants" is accurate as a group.  **Supported.**
* **ASvSZ** (`tab:families` caption): confirmed better than the draft's hedge
  — §2.3 of the fetched PDF tabulates Apéry limits for the third-order
  sporadic operators under the same Greek labels (α)…(κ), e.g. `7/24 ζ(3)`,
  `1/6 ζ(3)`, `7/32 ζ(3)`, `1/3 L(χ_3,3)`.  The hedge "presumably" was left
  as the author wrote it.
* **Gessel** (`:532`): Gessel 1982 covers the Apéry ζ(3) numbers only; the
  "for all fifteen families" is carried by the co-cited `MalikStraub`.  The
  joint citation is correct as written.  **Supported.**
* **Kubota–Leopoldt** (`:1632`): the 1964 paper is the origin of the p-adic
  Dirichlet L-function; the citation is attributional — the paper's own
  appendix *derives* the interpolation formula rather than importing it.  I
  could not fetch the 1964 German original, so the record is from the
  publisher/EUDML metadata only; noted here for honesty, no softening needed
  since no claim rests on the source's internal content.
* **Gross–Koblitz** (`:1434`): the Gross–Koblitz formula does express Γ_p at
  rational arguments via Gauss sums, hence the algebraicity used.
  **Supported.**

### 2.2 `UNVERIFIED-Beukers` — SPLIT (the single entry covered three different papers)

The entry's note claimed it stood for the Bull. LMS integral proof *and* the
p-adic irrationality measures *and* the η-product congruence.  The Bull. LMS
paper is **never actually cited** anywhere in the text, so it was dropped;
the two live citation sites were split:

* `:985` (the weight-4 level-8 newform `η(2z)^4 η(4z)^4` attached to the
  Apéry numbers) → **`Beukers1987`**: F. Beukers, *Another congruence for the
  Apéry numbers*, J. Number Theory **25** (1987), no. 2, 201–210 (OEIS
  A005259 and Malik–Straub `[Beu87]` both give this record), with a
  cross-reference to F. Beukers, *Irrationality proofs using modular forms*,
  Astérisque **147–148** (1987), 271–283 (NUMDAM record fetched), where the
  mod-`p^2` form of the η-product congruence is conjectured.  Corroboration
  that the form is weight 4 level 8: the Golyshev–Zagier abstract calls it
  "the unique normalized cusp form of weight 4 on Γ_0(8)".
* `:1755–1756` (the published measures `μ(ζ_2(3)) ≤ 7.177398…`,
  `μ(ζ_3(3)) ≤ 22.281447…`) → **`Beukers2008`**: F. Beukers, *Irrationality
  of some p-adic L-values*, Acta Math. Sin. (Engl. Ser.) **24** (2008),
  no. 4, 663–686.  LSZ 2025 (repo tex, lines 165–171) gives exactly
  `μ(ζ_2(3)) ≤ 12log2/(6log2−3) = 7.177398…` and
  `μ(ζ_3(3)) ≤ 6log3/(3log3−3) = 22.281447…`, and says these "can be
  extracted from Calegari's work [Cal2005] … alternatively, from Beukers'
  result **[Beu2008, Theorem 11.2]**".  The table's α, β and μ columns are
  arithmetically consistent with those two expressions.  **Supported.**

### 2.3 `UNVERIFIED-Sprang` — **DOWNGRADED**

* Draft sentence (`:1708`): "the smallness exponent α = 16 log 2 comes from
  **Sprang's Δ-operator estimate** `v_2(∫f) ≥ Δ(f)−1` [UNVERIFIED-Sprang]".
* What the source actually says (LSZ 2025, repo tex, lines 227–248): the
  characteristic Δ(f) "was first introduced by the second author in
  **[Spr2020]**", but the estimate `v_p(∫_{Z_p} f dt) ≥ Δ(f) − 1` is stated
  as `Lemma [Lai2025, Lemma 2.4]` — i.e. the *operator* is Sprang's, the
  *estimate* is Lai's.
* Action: sentence softened to "Sprang's Δ-operator \cite{Sprang2020} in the
  estimate `v_2(∫f) ≥ Δ(f)−1` of \cite[Lemma 2.4]{Lai2025}".  Two entries
  now carry it:
  - J. Sprang, *Linear independence result for p-adic L-values*, Duke
    Math. J. **169** (2020), no. 18, 3439–3476;
  - L. Lai, *On the irrationality of certain 2-adic zeta values*, Int. J.
    Number Theory **21** (2025), no. 1, 207–235.
  Both records taken verbatim from the LSZ bibliography in the repo.

### 2.4 The 5 incomplete secondaries — COMPLETED

| key | was | now |
|---|---|---|
| `Calegari2005` | no title ("the title is not recorded in the sources available to us") | F. Calegari, *Irrationality of certain p-adic periods for small p*, Int. Math. Res. Not. (2005), no. 20, 1235–1249 — from the LSZ bibliography `[Cal2005]` |
| `ChamberlandStraub` | arXiv id only | M. Chamberland and A. Straub, *Apéry limits: experiments and proofs*, Amer. Math. Monthly **128** (2021), no. 9, 811–824 |
| `MalikStraub` | arXiv id only | A. Malik and A. Straub, *Divisibility properties of sporadic Apéry-like numbers* |
| `Straub2023` | arXiv id only | A. Straub, *Gessel–Lucas congruences for sporadic sequences*, Monatsh. Math. (2023) |
| `GolyshevZagier` | truncated title, no venue | V. Golyshev and D. Zagier, *Interpolated Apéry numbers, quasiperiods of modular forms, and motivic gamma functions*, Proc. Sympos. Pure Math. **103.2**, AMS 2021, 281–301 |

Author initials were also supplied for `BV2025`, `BVdwork3`,
`BrownZudilin2022`, `Brown2014`, `Fischler2003`, `FSZ2018`, `Kerr`,
`LaiSprang2023`, `LSZ2025`, `RoyVlasenko` (all from the arXiv API batch).

`BV2025` is now confirmed at the *content* level too: `\cite[Prop. 1.3]` and
`\cite[eq. (2)]` are genuinely Proposition 1.3 and equation (2) of
arXiv:2302.09603 (PDF fetched), the latter being
`log Γ_p(x) = Γ_p'(0)x − Σ_{m≥2} ζ_p(m)x^m/m`.

---

## 3. Paper C — `papers_out/frobenius`

All three resolved.  Appendix "Citation discipline" was rewritten to match
(it previously announced that three references "could not be checked").

### 3.1 `UNVERIFIED-BeukersVlasenko` → `BeVl25` — RESOLVED, and the claim confirmed

* Record: F. Beukers and M. Vlasenko, *Frobenius structure and p-adic zeta
  values*, Adv. Math. **480** (2025), Part C, Paper No. 110512;
  arXiv:2302.09603; DOI 10.1016/j.aim.2025.110512 (arXiv API journal-ref).
* Claim check (`:472`, "the Frobenius structure constants of [BV] are the
  Taylor coefficients of the same `G` at 0"): PDF fetched.  Theorem 1.4:
  "The constants α_j defining the Frobenius structure via (1) are given by
  α_j = coefficient of x^j in `Γ_p(x)/Γ_p(x/(n+1))^{n+1}`".  Equation (2):
  `log Γ_p(x) = Γ_p'(0)x − Σ_{m≥2} ζ_p(m)x^m/m`, so
  `Γ_p(x)/Γ_p(x/(n+1))^{n+1} = G(x)/G(x/(n+1))^{n+1}` with
  `G(x) = Γ_p(x)e^{−Γ_p'(0)x}` exactly as the draft defines it (the
  `e^{Γ_p'(0)x}` factors cancel).  **Supported** — the draft's hedged
  framing in §`sec:padic` is if anything conservative.

### 3.2 `UNVERIFIED-Birkhoff` → `BT33` — RESOLVED

* G. D. Birkhoff and W. J. Trjitzinsky, *Analytic theory of singular
  difference equations*, Acta Math. **60** (1933), 1–89 (Project
  Euclid/Acta record).  Cited attributionally only; the construction is
  derived in the paper's own Proposition `prop:birkhoff`.  Note kept in the
  entry.

### 3.3 `UNVERIFIED-PSLQ` → `FBA99` — RESOLVED

* H. R. P. Ferguson, D. H. Bailey and S. Arno, *Analysis of PSLQ, an integer
  relation finding algorithm*, Math. Comp. **68** (1999), no. 225, 351–369
  (AMS record); the algorithm was introduced in H. R. P. Ferguson and
  D. H. Bailey, *A polynomial time, numerically stable integer relation
  algorithm*, RNR Technical Report RNR-91-032, NASA Ames (1992).
  Note: the draft listed only Ferguson and Bailey; **Arno** is a co-author of
  the published analysis, so both items are now given.

---

## 4. Paper D — `papers_out/sharp12` — 5 spot-checks, all clean

sharp12 claims zero unverified entries.  Its bibliography is BZ-sourced: all
of `Ap79, Be79, Br09, Br16, BZ, Du18, Ko10, MZ20, RV96, RV01, WZ92, Ze91,
Zu02a, Zu02b, Zu04` agree character-for-character with the bibliography of
the repo copy of Brown–Zudilin
(`papers/20-brown-zudilin-2022-cellular-rational-approx-zeta5/2026-01-26_CellZeta.tex`).
Five were then checked **against the actual papers / publisher records**:

| key | checked against | verdict |
|---|---|---|
| `Br09` | NUMDAM `ASENS_2009_4_42_3_371_0` | Ann. Sci. Éc. Norm. Supér. (4) **42** (2009), no. 3, 371–489 — **exact** |
| `Du18` | Compositio/arXiv:1601.00950 records | Compos. Math. **154** (2018), no. 2, 342–379, "with a joint appendix with D. Zagier" — **exact** |
| `MZ20` | Cambridge Core / arXiv:1905.12579 | Proc. Edinburgh Math. Soc. **63** (2020), 374–397 — **exact** |
| `WZ92` | reference list of Schneider, EJC 14 (2007) #N5 (PDF fetched) | Invent. Math. **108** (1992), no. 3, 575–633 — **exact** |
| `Ze91` | same source | J. Symbolic Comput. **11** (1991), no. 3, 195–204 — **exact** |

No edits made to `sharp12`.

---

## 5. Errors found in entries that were *already* marked verified

1. **`FSZ2018` / `FSZ` — wrong volume and year.**  Both `padiclimits` and
   `frobenius` had "Compos. Math. **154** (2018)".  The correct record is
   **Compositio Math. 155 (2019), no. 5, 938–952** — confirmed twice
   independently: the arXiv API journal-ref for 1803.08905, and the LSZ 2025
   bibliography in the repo (`[FSZ2019] … Compos. Math. 155 (2019), no. 5,
   938–952`).  **Corrected in both papers.**
2. **`UNVERIFIED-PSLQ` missing a co-author** (S. Arno) — see §3.3.
   **Corrected.**
3. Quotation spelling in `lucas2nd/sec-minimal.tex` — see §1.2.
   **Corrected.**

Not corrected (out of scope, recorded only): `padiclimits` `DRR` carries
"Mem. Amer. Math. Soc. 246" without an issue number; `lucas2nd` keeps the
same.  Neither is wrong, merely incomplete, and the issue number was not
confirmed from a fetched source.

---

## 6. Evidence trail — artefacts fetched

Downloaded and read (scratchpad
`/tmp/claude-1000/-home-ubuntu-fable-episode-2-zeta-math-2/…/scratchpad/`):
`vdp.pdf` (van der Poorten scan), `hni.pdf` (Paule–Schneider RISC preprint),
`sch07c.pdf` (Schneider EJC 2007), `os.pdf` (Osburn–Sahu), `str2301.pdf`
(Straub), `wolst.pdf` (Meštrović Wolstenholme survey), `bv.pdf`
(Beukers–Vlasenko 2302.09603), `asvsz.pdf` (Almkvist–van Straten–Zudilin),
`arx.xml` (arXiv API batch, 22 ids), Malik–Straub and Zudilin math/0202159
PDFs (WebFetch cache under `tool-results/`).

Read from the repo itself: `papers/05-fischler-2003-bourbaki-survey/`,
`papers/18-lai-sprang-zudilin-2025-irrationality-zeta2-of-5/`,
`papers/20-brown-zudilin-2022-cellular-rational-approx-zeta5/`.

Symbolic/numeric checks run: Nesterenko weight identity (sympy, exact),
Morita product formula (exact integer arithmetic), Ahlgren identity (4) at
n = 1, 2 (by hand).

---

## 7. Compile status (3 × pdflatex, after all edits)

| paper | output | undefined refs/citations | errors |
|---|---|---|---|
| `lucas2nd` (`./build.sh`) | main.pdf, 39 pp. | 0 | none |
| `padiclimits` | padic-apery-limits.pdf, 29 pp. | 0 | none |
| `frobenius` | frobenius.pdf, 25 pp. | 0 | none |
| `sharp12` (untouched) | sharp12.pdf, 42 pp. | 0 | none |
