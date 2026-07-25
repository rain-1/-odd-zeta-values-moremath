# ζ(5), ζ(7) irrationality — source library

LaTeX sources (from arXiv `e-print`) and a few PDF-only items, plus an
LLM-readable Markdown conversion of the whole corpus.

```
llm/               <- read this: 37 Markdown files, ~865k tokens, YAML front matter
llm/INDEX.md       <- manifest (per-file token counts, conversion mode, provenance)
papers/            <- original arXiv LaTeX sources, one directory per paper
books-and-surveys/ <- items with no public TeX source, as PDF
tools/             <- the conversion scripts; rerun to regenerate llm/
```

Regenerate: `python3 tools/tex2llm.py && python3 tools/pdf2llm.py && python3 tools/make_index.py`

**Conversion caveats.** 31 of 32 arXiv papers went through pandoc with math preserved
as LaTeX (`$…$`, `$$…$$`) — these are faithful. One (`03`, Zudilin's Russian source
with `\char"` transliteration macros) is included as verbatim LaTeX instead. Of the 9
PDFs, 5 extracted as text — **formulas there are flattened and lossy**, so check the
PDF before relying on any displayed equation. The remaining 4 use Type-3 bitmap fonts
and yield nothing extractable; they stay PDF-only and are listed at the bottom of
`llm/INDEX.md`.

## State of the art (what is actually known)

- ζ(3) irrational (Apéry 1978). **Nothing is known about any single ζ(2k+1) for k ≥ 2.**
- Infinitely many ζ(2k+1) are irrational (Rivoal 2000; Ball–Rivoal 2001):
  dim_Q span{1, ζ(3), …, ζ(2n+1)} ≫ log n.
- At least one of ζ(5), ζ(7), ζ(9), ζ(11) is irrational (Zudilin 2001) — still the
  narrowest window containing ζ(5).
- At least two of ζ(5), ζ(7), …, ζ(35) are irrational (Lai–Zhou 2021).
- ≥ 2^((1−ε) log s / log log s) irrationals among ζ(3), …, ζ(s) (Fischler–Sprang–Zudilin 2018).

## `papers/` — arXiv LaTeX sources

### The classical odd-zeta line (Rivoal / Zudilin)

| dir | paper |
|---|---|
| `01-rivoal-2000-infinite-irrational-odd` | Rivoal, *La fonction zêta de Riemann prend une infinité de valeurs irrationnelles aux entiers impairs*, CRAS 331 (2000). [math/0008051] — the announcement. |
| `02-rivoal-2001-one-of-zeta5-to-zeta21` | Rivoal, *Irrationalité d'au moins un des neuf nombres ζ(5), ζ(7), …, ζ(21)*, Acta Arith. 103 (2002). [math/0104221] — **the first ζ(5)-window result.** |
| `03-zudilin-2001-irrationality-of-zeta-values` | Zudilin, *Irrationality of values of zeta-function* [math/0104249]. Source is Russian (`\lowercase` transliteration macros); English version in `books-and-surveys/zudilin-2002-irrationality-riemann-zeta-izvestiya.pdf`. |
| `04-zudilin-2002-arithmetic-of-linear-forms` | Zudilin, *Arithmetic of linear forms involving odd zeta values*, J. Théor. Nombres Bordeaux 16 (2004). [math/0206176] — **the full, detailed proof of the one-of-ζ(5),ζ(7),ζ(9),ζ(11) theorem.** Start here for the machinery: well-poised hypergeometry + the arithmetic (denominator) method. |
| `05-fischler-2003-bourbaki-survey` | Fischler, *Irrationalité de valeurs de zêta (d'après Apéry, Rivoal, …)*, Séminaire Bourbaki 910. [math/0303066] — the best single orientation document; read before the primary sources. |

### The 2018 "elementary means" wave

| dir | paper |
|---|---|
| `06-zudilin-2018-zeta5-to-zeta25-elementary` | Zudilin, *One of the odd zeta values from ζ(5) to ζ(25) is irrational. By elementary means*, SIGMA 14 (2018). [1801.09895] — weaker than the 2001 result but the proof needs only PNT + Stirling. Good entry point. |
| `07-krattenthaler-zudilin-2018-hypergeometry-irrationality` | Krattenthaler–Zudilin, *Hypergeometry inspired by irrationality questions* [1802.08856]. |
| `08-sprang-2018-infinitely-many-elementary` | Sprang, *Infinitely many odd zeta values are irrational. By elementary means* [1802.09410]. |
| `09-rivoal-zudilin-2018-note-on-odd-zeta` | Rivoal–Zudilin, *A note on odd zeta values* [1803.03160]. |
| `10-fischler-sprang-zudilin-2018-many-odd-zeta` | Fischler–Sprang–Zudilin, *Many odd zeta values are irrational*, Compositio 154 (2018). [1803.08905] — the 2^(log s/log log s) bound; breaks the log-barrier of Ball–Rivoal. |
| `11-zudilin-2018-hypergeometric-integrals-linear-forms` | Zudilin, *Some hypergeometric integrals for linear forms in zeta values* [1804.04129] — short, useful for the integral representations. |

### Modern quantitative work (Lai, Fischler)

| dir | paper |
|---|---|
| `12-lai-yu-2019-number-of-irrational-odd-zeta` | Lai–Yu [1911.08458]. |
| `13-lai-zhou-2021-at-least-two-zeta5-to-zeta35` | Lai–Zhou, *At least two of ζ(5), ζ(7), …, ζ(35) are irrational* [2103.00904] — **the sharpest "two irrationals in a window" statement.** |
| `14-fischler-2021-siegel-lemma-linear-independence` | Fischler, *Linear independence of odd zeta values using Siegel's lemma* [2109.10136] — replaces explicit constructions with a pigeonhole/Siegel-lemma argument; conceptually the biggest recent shift. |
| `15-lai-sprang-2023-many-p-adic-odd-zeta` | Lai–Sprang, *Many p-adic odd zeta values are irrational* [2306.10393]. |
| `16-lai-2024-improvements-ball-rivoal` | Lai, *Small improvements on the Ball–Rivoal theorem and its p-adic variant* [2407.14236]. |
| `17-lai-2025-number-of-irrational-odd-zeta-II` | Lai, *A note on the number of irrational odd zeta values, II* [2501.05321]. |
| `18-lai-sprang-zudilin-2025-irrationality-zeta2-of-5` | Lai–Sprang–Zudilin, *A note on the irrationality of ζ₂(5)* [2505.05005] — the 2-adic ζ(5) analogue **is** provably irrational; instructive contrast with the archimedean case. |

### Francis Brown — motivic / geometric approach

| dir | paper |
|---|---|
| `19-brown-2014-irrationality-proofs-moduli-dinner-parties` | Brown, *Irrationality proofs for zeta values, moduli spaces and dinner parties* [1412.6508] — **the key conceptual paper**: reinterprets Apéry-type proofs via M_{0,n} cell integrals, and explains structurally why ζ(5) resists. |
| `20-brown-zudilin-2022-cellular-rational-approx-zeta5` | Brown–Zudilin, *On cellular rational approximations to ζ(5)* [2210.03391] — the most direct modern attack on ζ(5) itself. |
| `21-brown-2026-mellin-transfinite-diameter-rational-approx` | Brown, *Mellin transforms, transfinite diameter and rational approximations of integrals* [2604.20741] — newest (Apr 2026), new determinant/transfinite-diameter criterion. |
| `31-brown-schnetz-2024-wheel-classes-canonical-integrals-zeta` | Brown–Schnetz, *The wheel classes in the locally finite homology of GL_n(Z), canonical integrals and zeta values* [2402.06757]. |
| `32-brown-2026-nonlinear-geometry-of-mzv` | Brown, *Non-linear geometry of multiple zeta values* [2604.22735] — newest (Apr 2026). |

### Multiple zeta values (structure theory)

| dir | paper |
|---|---|
| `25-brown-2011-mixed-tate-motives-over-Z` | Brown, *Mixed Tate motives over Z*, Annals 175 (2012). [1102.1312] — every MZV is a Q-linear combination of ζ(2,3,…)-words; Hoffman basis. |
| `26-brown-2011-decomposition-motivic-mzv` | Brown, *On the decomposition of motivic multiple zeta values* [1102.1310] — the computational companion. |
| `27-brown-2013-depth-graded-motivic-mzv` | Brown, *Depth-graded motivic multiple zeta values* [1301.3053]. |
| `28-brown-2013-single-valued-periods-and-mzv` | Brown, *Single-valued periods and multiple zeta values* [1309.5309]. |
| `29-brown-2015-notes-on-motivic-periods` | Brown, *Notes on motivic periods* [1512.06410] — readable introduction to the period formalism. |
| `30-brown-2014-motivic-periods-P1-minus-3-points` | Brown, *Motivic periods and P¹ ∖ {0,1,∞}* (ICM 2014) [1407.5165] — best survey-level entry into Brown's programme. |

### MZV ↔ irrationality bridge (Cresson–Fischler–Rivoal)

| dir | paper |
|---|---|
| `22-cresson-fischler-rivoal-multiple-hypergeom-polyzetas` | *Séries hypergéométriques multiples et polyzêtas* [math/0609743]. |
| `23-cresson-fischler-rivoal-symmetry-linear-forms-polyzetas` | *Phénomènes de symétrie dans des formes linéaires en polyzêtas* [math/0609744]. |
| `24-fischler-rivoal-2013-mzv-pade-vasilyev` | Fischler–Rivoal, *Multiple zeta values, Padé approximation and Vasilyev's conjecture* [1309.2534] — why MZVs show up inside the ζ(5)-type constructions. |

## `books-and-surveys/` — PDF only

- `zudilin-MZV-tasting-notes.pdf` — Zudilin, *Multiple Zeta Values: Tasting Notes* (2025), from his homepage.
- `ball-rivoal-2001-inventiones-irrationalite-infinite-zeta.pdf` — Ball–Rivoal, Invent. Math. 146 (2001). **Not on arXiv**; this is the published paper.
- `zudilin-2001-one-of-zeta5-7-9-11-is-irrational.pdf` — the 2-page Russian Math. Surveys announcement of the headline theorem. Also not on arXiv.
- `zudilin-2001-one-of-eight-zeta5-to-zeta19.pdf` — the intermediate ζ(5)…ζ(19) result.
- `zudilin-2002-irrationality-riemann-zeta-izvestiya.pdf` — English version of `papers/03`.
- `zudilin-2001-irrationality-odd-integer-points-brief.pdf`
- `zudilin-2003-algebraic-relations-for-mzv-survey.pdf` — 30-page MZV survey.
- `zudilin-2004-well-poised-hypergeometric-service.pdf` — the well-poised toolkit, condensed.
- `zudilin-2011-arithmetic-hypergeometric-series-survey.pdf`

## Deliberately excluded

- Suman, *A note on the irrationality of ζ(5) and higher odd zeta values* [2407.07121] —
  claims outright irrationality of ζ(5); **withdrawn by the author** (v7, May 2025).
- Apéry (1979) and Beukers (1979) are paywalled with no preprint; both are fully
  reconstructed inside `papers/05-fischler-2003-bourbaki-survey`.

## Suggested reading order for ζ(5)/ζ(7)

1. `05` Fischler's Bourbaki survey (orientation)
2. `06` Zudilin's elementary SIGMA paper (mechanics, minimal prerequisites)
3. `04` Zudilin's full one-of-four proof (the real machinery)
4. `19` Brown's dinner-parties paper (why the machinery stalls at ζ(5))
5. `20` Brown–Zudilin cellular approximations to ζ(5), then `21` and `14`
