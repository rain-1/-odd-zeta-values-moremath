(* z5core.wl -- RISC-FREE kernel functions for the NEW compact weights of
   work/ZETA5_CLOSEDFORM.md.  Loads work/lb5/verifycore.wl (which loads NO RISC
   package) and adds the two shifted kernels

     W3r[a,b,c] = T(n+a,k+b,l+c) * w3hat(n+a,k+b,l+c) / T(n,k,l)
     W5r[a,b,c] = T(n+a,k+b,l+c) * w5    (n+a,k+b,l+c) / T(n,k,l)

   expressed in Q(n,k,l)[hh[...]] via verifycore's grat/tratio/hnorm.  A relation
   that reduces to 0 there is an identity of functions wherever the harmonic
   numbers are defined.                                                          *)

Get["/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/verifycore.wl"];

AAz[r_, x_, nn_] := HarmonicNumber[nn + x, r] - HarmonicNumber[x, r];
BBz[r_, x_, nn_] := HarmonicNumber[nn - x, r] - HarmonicNumber[x, r];
alz[nn_, kk_, ll_] := AAz[1, kk, nn] - AAz[1, ll, nn];
bez[nn_, kk_, ll_] := BBz[1, kk, nn] - BBz[1, ll, nn];
Psiz[nn_, kk_, ll_] := alz[nn, kk, ll]/2 + bez[nn, kk, ll];
S2z[nn_, kk_, ll_] := AAz[2, kk, nn] + AAz[2, ll, nn];
w3At[a_, b_, c_] := Module[{nn = n + a, kk = k + b, ll = l + c}, HarmonicNumber[nn + kk, 3] - Psiz[nn, kk, ll] HarmonicNumber[nn + kk, 2]];
w5At[a_, b_, c_] := Module[{nn = n + a, kk = k + b, ll = l + c}, HarmonicNumber[nn + kk, 5] + (1/2) (alz[nn, kk, ll] - bez[nn, kk, ll]) HarmonicNumber[nn + kk, 4] + (S2z[nn, kk, ll]/4 - alz[nn, kk, ll] Psiz[nn, kk, ll]/2) HarmonicNumber[nn + kk, 3]];

W3r[a_, b_, c_] := W3r[a, b, c] = Expand[tratio[a, b, c] hnorm[w3At[a, b, c]]];
W5r[a_, b_, c_] := W5r[a, b, c] = Expand[tratio[a, b, c] hnorm[w5At[a, b, c]]];

(* apply a hand-rolled ope[vars,terms] operator to the kernel ker (ker[a,b,c] =
   value at (n+a,k+b,l+c) divided by T(n,k,l)); same convention as verifycore's applyOp *)
applyOpe[ope[vars_, ts_], ker_, extra_: {0, 0, 0}] := Module[{slot}, slot = {S[n], S[k], S[l]} /. Thread[vars -> Range[Length[vars]]];
  Total[Table[Module[{co = t[[1]], ex = t[[2]], sh}, sh = Table[If[IntegerQ[slot[[i]]], ex[[slot[[i]]]], 0], {i, 3}] + extra;
     Expand[(co /. {n -> n + extra[[1]], k -> k + extra[[2]], l -> l + extra[[3]]}) ker @@ sh]], {t, ts}]]];
