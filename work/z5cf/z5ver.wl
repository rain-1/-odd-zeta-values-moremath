(* z5ver.wl -- INDEPENDENT, RISC-FREE verification of a certificate package for the
   new compact weights.  Loads NO RISC package: everything is re-derived from the
   definition of T and of the harmonic numbers (work/lb5/verifycore.wl via z5core.wl);
   the package contents are treated as untrusted inert data.
   Run:  TAG=w3_lk KER=w3 math < z5ver.wl                                            *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/z5cf/";
gets[v_, d_] := Module[{x = Environment[v]}, If[x === $Failed, d, x]];
TAG = gets["TAG", "w3_lk"]; KER = gets["KER", "w3"];
lf = OpenWrite[DIR <> "z5ver_" <> TAG <> ".log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], " TAG=", TAG, " KER=", KER];
Get[DIR <> "z5core.wl"];
log["z5core loaded (NO RISC package in this kernel)"];

pkg = Get[DIR <> "z5_" <> TAG <> "_pkg.m"];
first = ToExpression[pkg["first"]]; second = ToExpression[pkg["second"]];
qs = pkg["q"]; rs = pkg["r"]; QQ = pkg["QQ"]; RR = pkg["RR"]; ff = pkg["ff"]; ws = pkg["w"];
log["package: #q=", Length[qs], " first=", ToString[first], " second=", ToString[second]];
ker = Switch[KER, "w3", W3r, "w5", W5r, "T", Qr, _, W3r];
e1 = Switch[first, n, {1, 0, 0}, k, {0, 1, 0}, l, {0, 0, 1}];

(* ---- V-A: first-step pairs at the level of FUNCTIONS ---- *)
log["--- V-A: q[i].F + (S_", ToString[first], "-1)(r[i].F) = 0 ---"];
vaok = True;
Do[Module[{e, rep}, e = applyOp[qs[[i]], ker] + applyOp[rs[[i]], ker, e1] - applyOp[rs[[i]], ker];
   rep = zeroReport["q" <> ToString[i], e];
   log["  V-A pair ", i, ": #hvars=", rep[[2]], " #coeffs=", rep[[3]], " #nonzero=", rep[[4]], "  -> ", If[rep[[4]] == 0, "ZERO", "*** FAIL ***"]];
   If[rep[[4]] != 0, vaok = False; log["     first bad coeff: ", ToString[InputForm[rep[[5]]]]]]], {i, Length[qs]}];
log["V-A overall: ", If[vaok, "PASS", "FAIL"]];

(* ---- V-B: operator cofactor identity, hand-rolled Ore algebra ---- *)
log["--- V-B: ff*(QQ + (S_", ToString[second], "-1)*RR) = Sum_i w[i]**q[i] ---"];
vars = {S[n], S[second]};
one = opOne[vars]; dl = opPlus[opGen[vars, S[second]], opScal[-1, one]];
lhs0 = opPlus[toOpe[QQ, vars], opTimes[dl, toOpe[RR, vars]]];
lhs = If[Head[ff] === List || MatchQ[ff, _[_List, _, _]], opTimes[toOpe[ff, vars], lhs0], opScal[ff, lhs0]];
rhs = Fold[opPlus, ope[vars, {}], Table[opTimes[toOpe[ws[[i]], vars], toOpe[qs[[i]], vars]], {i, Length[qs]}]];
diff = opPlus[lhs, opScal[-1, rhs]];
log["V-B: ", If[opZeroQ[diff], "PASS", "FAIL, residual terms = " <> ToString[Length[opNorm[diff][[2]]]]]];

(* ---- V-C: is the telescoper L_BZ ? ---- *)
a0[x_] := 41218 x^3 + 198849 x^2 + 320790 x + 173057;
B8[x_] := 3874492 x^8 + 59373972 x^7 + 394148190 x^6 + 1481084196 x^5 + 3447878810 x^4 + 5095855458 x^3 + 4673546679 x^2 + 2433871008 x + 551502039;
B9[x_] := 48802112 x^9 + 967468896 x^8 + 8488000862 x^7 + 43246197636 x^6 + 140983768422 x^5 + 304912330849 x^4 + 437406946975 x^3 + 401272692378 x^2 + 213593890911 x + 50257929339;
LBZc = {(n + 1)^5 (n + 2) a0[n + 1], -2 (n + 2) B8[n], -2 B9[n], 2 (n + 3)^5 (2 n + 5) a0[n]};
Qo = toOpe[QQ, {S[n]}];
maxo = Max[Join[{0}, Qo[[2]][[All, 2, 1]]]];
cf = Table[Module[{t = Select[Qo[[2]], #[[2]] === {j} &]}, If[t === {}, 0, t[[1, 1]]]], {j, 0, maxo}];
log["V-C: telescoper order = ", maxo];
If[maxo == 3, log["V-C: ratio to L_BZ = ", ToString[InputForm[Together[cf/LBZc]]]]; log["V-C: cf - (cf1/LBZ1) L_BZ = ", ToString[InputForm[Together[cf - Together[cf[[1]]/LBZc[[1]]] LBZc]]]], log["V-C: order != 3"]];

(* ---- V-D: the ASSEMBLED single pair (rho,sigma), end-to-end at function level ----
   From V-A  q[i].F = -(S_first-1)(r[i].F)  and V-B  ff*(QQ+(S_second-1)RR) = Sum w[i]**q[i]:
       ff*QQ.F  =  Delta_second(-RR.F) + Delta_first(-sigma.F),   sigma = Sum_i w[i]**r[i].
   This block re-checks that single identity directly, with no reference to V-A/V-B.      *)
log["--- V-D: assembled single pair,  ff*QQ.F + Delta_", ToString[second], "(RR.F) + Delta_", ToString[first], "(sigma.F) = 0 ---"];
v3 = {S[n], S[k], S[l]};
e2 = Switch[second, n, {1, 0, 0}, k, {0, 1, 0}, l, {0, 0, 1}];
ffop = If[Head[ff] === List || MatchQ[ff, _[_List, _, _]], toOpe[ff, v3], opScal[ff, opOne[v3]]];
sigop = Fold[opPlus, ope[v3, {}], Table[opTimes[toOpe[ws[[i]], v3], toOpe[rs[[i]], v3]], {i, Length[ws]}]];
Put[{ffop, toOpe[QQ, v3], toOpe[RR, v3], sigop}, DIR <> "z5_" <> TAG <> "_rhosigma.m"];
log["  sigma terms = ", Length[sigop[[2]]], "  LeafCount ", LeafCount[sigop], "   rho(=-RR) LeafCount ", LeafCount[RR]];
eD = applyOpe[opTimes[ffop, toOpe[QQ, v3]], ker] + (applyOp[RR, ker, e2] - applyOp[RR, ker]) + (applyOpe[sigop, ker, e1] - applyOpe[sigop, ker]);
repD = zeroReport["assembled", eD];
log["  V-D: #hvars=", repD[[2]], " #coeffs=", repD[[3]], " #nonzero=", repD[[4]], "  -> ", If[repD[[4]] == 0, "ZERO -- CERTIFICATE VERIFIED RISC-FREE", "*** FAIL ***"]];
If[repD[[4]] != 0, log["     first bad coeff: ", ToString[InputForm[repD[[5]]]]]];

(* ---- V-E: boundary factors ---- *)
log["--- V-E: denominators of the certificates (boundary data) ---"];
bnd[p_, lab_] := Module[{e}, e = Together[applyOp[p, ker]]; log["  ", lab, " : denominator factors = ", ToString[InputForm[FactorList[Denominator[e]][[All, 1]]]]]];
Do[bnd[rs[[i]], "r[" <> ToString[i] <> "]"], {i, Length[rs]}];
bnd[RR, "RR"];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
