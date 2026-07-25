(* certV.wl -- INDEPENDENT verification of a certificate package.
   Loads NO RISC package.  Everything here is re-derived from the definition of
   T and of the harmonic numbers; the package contents are treated as untrusted
   data.  Run as:   LAB=Y1 math < certV.wl                                       *)
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
LAB = Environment["LAB"]; If[LAB === $Failed, LAB = "Y1"];
KER = Environment["KER"]; If[KER === $Failed, KER = "w3hat"];
lf=OpenWrite[DIR<>"certV_"<>LAB<>".log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf];Print[x]);
log["START ",DateString[]," LAB=",LAB," KER=",KER];
Get[DIR<>"verifycore.wl"];
log["verifycore loaded (no RISC)"];

pkg = Get[DIR<>LAB<>"_pkg.m"];
first  = ToExpression[pkg["first"]];
second = ToExpression[pkg["second"]];
qs = pkg["q"]; rs = pkg["r"]; QQ = pkg["QQ"]; RR = pkg["RR"]; ff = pkg["ff"]; ws = pkg["w"];
log["package: #q=",Length[qs]," first=",ToString[first]," second=",ToString[second]];

ker = Switch[KER, "w3hat", Wr, "T", Qr, _, Wr];
e1 = Switch[first, n, {1,0,0}, k, {0,1,0}, l, {0,0,1}];
e2 = Switch[second, n, {1,0,0}, k, {0,1,0}, l, {0,0,1}];

(* ---- V-A: first-step telescoper/certificate pairs, at the level of functions ---- *)
log["--- V-A: q[i].W + (S_",ToString[first],"-1)(r[i].W) = 0 ---"];
vaok = True;
Do[ Module[{e},
     e = applyOp[qs[[i]], ker] + applyOp[rs[[i]], ker, e1] - applyOp[rs[[i]], ker];
     rep = zeroReport["q"<>ToString[i], e];
     log["  V-A pair ",i,": #hvars=",rep[[2]]," #coeffs=",rep[[3]]," #nonzero=",rep[[4]],
         "  -> ",If[rep[[4]]==0,"ZERO","*** FAIL ***"]];
     If[rep[[4]] != 0, vaok = False; log["     first bad coeff: ",ToString[InputForm[rep[[5]]]]]]],
  {i, Length[qs]}];
log["V-A overall: ", If[vaok, "PASS", "FAIL"]];

(* ---- V-B: operator identity  ff*(QQ + (S_second-1)*RR) = Sum_i w[i]*q[i] ---- *)
log["--- V-B: Ore-algebra cofactor identity ---"];
vars = {S[n], S[second]};
one = opOne[vars];
dl  = opPlus[opGen[vars, S[second]], opScal[-1, one]];
lhs0 = opPlus[toOpe[QQ, vars], opTimes[dl, toOpe[RR, vars]]];
lhs  = If[Head[ff] === List || MatchQ[ff, _[_List, _, _]],
          opTimes[toOpe[ff, vars], lhs0], opScal[ff, lhs0]];
rhs  = Fold[opPlus, ope[vars, {}],
        Table[opTimes[toOpe[ws[[i]], vars], toOpe[qs[[i]], vars]], {i, Length[qs]}]];
diff = opPlus[lhs, opScal[-1, rhs]];
log["V-B: ", If[opZeroQ[diff], "PASS (identity holds in Q(n,"<>ToString[second]<>")<S[n],S["<>ToString[second]<>"]>)",
                "FAIL, residual terms = " <> ToString[Length[opNorm[diff][[2]]]]]];

(* ---- V-C: is the telescoper L_BZ ? ---- *)
a0[x_]:=41218 x^3+198849 x^2+320790 x+173057;
B8[x_]:=3874492 x^8+59373972 x^7+394148190 x^6+1481084196 x^5+3447878810 x^4+5095855458 x^3+4673546679 x^2+2433871008 x+551502039;
B9[x_]:=48802112 x^9+967468896 x^8+8488000862 x^7+43246197636 x^6+140983768422 x^5+304912330849 x^4+437406946975 x^3+401272692378 x^2+213593890911 x+50257929339;
LBZc = {(n+1)^5 (n+2) a0[n+1], -2 (n+2) B8[n], -2 B9[n], 2 (n+3)^5 (2n+5) a0[n]};
Qo = toOpe[QQ, {S[n]}];
maxo = Max[Join[{0}, Qo[[2]][[All,2,1]]]];
cf = Table[Module[{t = Select[Qo[[2]], #[[2]] === {j} &]},
            If[t === {}, 0, t[[1,1]]]], {j, 0, maxo}];
log["V-C: telescoper order = ", maxo];
If[maxo == 3,
  log["V-C: ratio to L_BZ = ", ToString[InputForm[Together[cf/LBZc]]]];
  log["V-C: Expand[cf - (cf1/LBZ1) L_BZ] = ",
      ToString[InputForm[Together[cf - Together[cf[[1]]/LBZc[[1]]] LBZc]]]],
  log["V-C: order != 3; L_BZ divisibility must be checked separately"]];

(* ---- V-D: boundary factors of the certificates ---- *)
log["--- V-D: boundary behaviour of the certificates ---"];
bnd[p_, lab_] := Module[{e, den, num},
  e = Together[applyOp[p, ker]];
  log["  ",lab," : denominator factors = ",
      ToString[InputForm[FactorList[Denominator[e]][[All,1]]]]]];
Do[bnd[rs[[i]], "r["<>ToString[i]<>"]"], {i, Length[rs]}];
bnd[RR, "RR"];
log["ALL DONE ",DateString[]];
Close[lf]; Exit[];
