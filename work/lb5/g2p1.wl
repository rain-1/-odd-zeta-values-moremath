lf=OpenWrite["/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/g2p1.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";

(* BZ certified order-3 operator, c0 Y_n + c1 Y_{n+1} + c2 Y_{n+2} + c3 Y_{n+3} = 0 *)
a0[x_]:=41218 x^3+198849 x^2+320790 x+173057;
B8[x_]:=3874492 x^8+59373972 x^7+394148190 x^6+1481084196 x^5+3447878810 x^4+5095855458 x^3+4673546679 x^2+2433871008 x+551502039;
B9[x_]:=48802112 x^9+967468896 x^8+8488000862 x^7+43246197636 x^6+140983768422 x^5+304912330849 x^4+437406946975 x^3+401272692378 x^2+213593890911 x+50257929339;
cc0[x_]:=(x+1)^5 (x+2) a0[x+1];
cc1[x_]:=-2 (x+2) B8[x];
cc2[x_]:=-2 B9[x];
cc3[x_]:=2 (x+3)^5 (2x+5) a0[x];
LBZ = cc0[n] + cc1[n] SS + cc2[n] SS^2 + cc3[n] SS^3;   (* SS is a formal shift symbol *)

opToPoly[op_] := Module[{ap,ord,coeffs},
  ap = ApplyOreOperator[op, FF[n]];
  ord = Max[Cases[ap, FF[n+a_.]:>a, Infinity]/.{}->{0}];
  coeffs = Table[Coefficient[ap, FF[n+j]], {j,0,ord}];
  {ord, Sum[coeffs[[j+1]] SS^j, {j,0,ord}]}];

(* ---------------- part 1: inspect the Q-telescoper ---------------- *)
log["=== part 1: Q double sum ==="];
Tsum = Binomial[n+k,n] Binomial[n,k]^2 Binomial[n+l,n] Binomial[n,l]^2 Binomial[n+k+l,n];
annQ = Annihilator[Tsum,{S[n],S[k],S[l]}];
t0=AbsoluteTime[];
ctQ = CreativeTelescoping[annQ,{S[k]-1,S[l]-1},{S[n]}];
log["CT done in ",Round[AbsoluteTime[]-t0],"s"];
log["Length ctQ = ",ToString[Length[ctQ]],"  Length ctQ[[1]] = ",ToString[Length[ctQ[[1]]]]];
Do[
  {ordi, poli} = opToPoly[ctQ[[1,i]]];
  log["  telescoper ",ToString[i]," order=",ToString[ordi]];
  log["    poly = ",ToString[InputForm[Factor[poli]]]];
  rem = PolynomialRemainder[LBZ, poli, SS];
  log["    LBZ mod this (in SS) = ",ToString[InputForm[Together[rem]]]];
 ,{i,1,Length[ctQ[[1]]]}];
Put[ctQ, DIR<>"ctQ.m"];

log["DONE1 ",DateString[]];
Close[lf];Exit[];
