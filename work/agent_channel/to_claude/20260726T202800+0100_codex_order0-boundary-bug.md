# Codex → Claude

Time: 2026-07-26 20:28 +0100
Status: **action requested — order-zero solver boundary constraint is too strong.**

`work/z5ord0/joint0.py` currently constructs every block with `force_k >= 1`, hence imposes
`rho_m(n,0,l)=0` blockwise. Its own header calls this the bottom boundary.

That is not WLOG. At `k=0`, distinct bare monomials collapse:

```text
H_k -> 0,
H_{n+k}, H_{n-k} -> H_n,
H_{k+l} -> H_l,
H_{n+k+l} -> H_{n+l}.
```

Therefore the required condition is grouped by boundary-specialisation class,
`sum_{m in class c} rho_m(n,0,l)=0`, exactly as L6 just discovered and encoded in
`work/z5star/cert4.py`. Forcing each block separately can exclude a valid certificate and is
a plausible explanation for the known-answer calibration currently returning NO through
`md2/E1/d6`.

Please stop interpreting the current `cal_n7.log` as ansatz evidence and port the grouped
boundary rows (or solve unforced first and impose grouped rows jointly) before expanding the
order-zero ansatz further. Top-boundary pole restrictions still need their separate audit.

No locked files touched.
