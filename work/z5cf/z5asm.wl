(* z5asm.wl -- certificate COMPOSITION for the new compact weights (search side).
   RISC is used here ONLY to find the cofactors; everything it writes is re-checked
   afterwards by z5ver.wl, which loads no RISC package at all.

   Reads   z5_<TAG>_ct1.m   (first-step telescoper/certificate pairs, eliminating FIRST)
           z5_<TAG>_cert.m  ({ann, ct1, gb, ct2})
   Writes  z5_<TAG>_pkg.m   with
             q[i], r[i] : q[i].F + (S[FIRST]-1)(r[i].F) = 0
             QQ, RR     : second-step telescoper / certificate
             ff, w[i]   : ff*(QQ + (S[SECOND]-1)*RR) = Sum_i w[i]**q[i]
   Run: TAG=w3_lk FIRST=l math < z5asm.wl                                          *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/z5cf/";
gets[v_, d_] := Module[{x = Environment[v]}, If[x === $Failed, d, x]];
TAG = gets["TAG", "w3_lk"];
FIRST = ToExpression[gets["FIRST", "l"]];
SECOND = If[FIRST === k, l, k];
lf = OpenWrite[DIR <> "z5asm_" <> TAG <> ".log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], " TAG=", TAG, " FIRST=", ToString[FIRST], " SECOND=", ToString[SECOND]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

alg2 = OreAlgebra[S[n], S[SECOND]];
ct1 = Get[DIR <> "z5_" <> TAG <> "_ct1.m"];
cert = Get[DIR <> "z5_" <> TAG <> "_cert.m"];
ct2 = cert[[4]];
log["ct1 ntel=", Length[ct1[[1]]], "  ct2 ntel=", Length[ct2[[1]]]];

t0 = AbsoluteTime[];
gbx = OreGroebnerBasis[ct1[[1]], alg2, Extended -> True];
log["gbx t=", Round[AbsoluteTime[] - t0], "s  Length=", Length[gbx]];
Put[gbx, DIR <> "z5_" <> TAG <> "_gbx.m"];
gb = gbx[[1]]; cof = gbx[[2]];
log["gb #", Length[gb], "  cof dims=", ToString[Dimensions[cof]]];

QQ = ct2[[1, 1]]; RR = ct2[[2, 1]];
dl = ToOrePolynomial[S[SECOND] - 1, alg2];
pp = QQ + dl ** RR;
t0 = AbsoluteTime[];
red = OreReduce[pp, gb, Extended -> True];
log["OreReduce t=", Round[AbsoluteTime[] - t0], "s  remainder zero? ", ToString[red[[1]] === 0 || (Head[red[[1]]] === OrePolynomial && red[[1, 1]] === {})]];
ff = red[[2]]; cc = red[[3]];
log["ff=", ToString[InputForm[ff]], "  #cc=", Length[cc]];
ww = Table[Total[Table[cc[[j]] ** cof[[j, i]], {j, Length[cc]}]], {i, Length[ct1[[1]]]}];
log["ww built, #=", Length[ww]];
pkg = <|"lab" -> TAG, "first" -> ToString[FIRST], "second" -> ToString[SECOND], "q" -> ct1[[1]], "r" -> ct1[[2]], "QQ" -> QQ, "RR" -> RR, "ff" -> ff, "w" -> ww, "gb" -> gb, "cof" -> cof, "cc" -> cc|>;
Put[pkg, DIR <> "z5_" <> TAG <> "_pkg.m"];
log["package written ", DIR, "z5_", TAG, "_pkg.m  ", DateString[]];
Close[lf]; Exit[];
