lf=OpenWrite["/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/gate2.log"];
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

(* ---------------- part 2: the w3hat-weighted double sum ---------------- *)
log["=== part 2: w3hat double sum ==="];
Ar[r_,x_]:=HarmonicNumber[n+x,r]-HarmonicNumber[x,r];
Br[r_,x_]:=HarmonicNumber[n-x,r]-HarmonicNumber[x,r];
C1 = HarmonicNumber[n+k+l,1]-HarmonicNumber[k+l,1];
w3 = HarmonicNumber[n,3] + Ar[3,k] + Ar[3,l]
     - 1/4 (Ar[2,k] Ar[1,k] + Ar[2,l] Ar[1,l])
     - 3/4 (Ar[2,k] Br[1,k] + Ar[2,l] Br[1,l])
     - 3/8 (Ar[2,k] + Ar[2,l]) C1
     - 1/8 (Ar[2,k] Ar[1,l] + Ar[2,l] Ar[1,k]);
summand = Tsum w3;
t0=AbsoluteTime[];
annW = TimeConstrained[MemoryConstrained[Annihilator[summand,{S[n],S[k],S[l]}],25*10^9,"M"],2400,"T"];
If[MatchQ[annW,"T"|"M"], log["annW ",ToString[annW]," after ",Round[AbsoluteTime[]-t0],"s"]; Close[lf]; Exit[]];
log["annW #",Length[annW]," in ",Round[AbsoluteTime[]-t0],"s"];
Put[annW, DIR<>"annW.m"];
log["annW leading exps: ",ToString[InputForm[Map[Exponent[ApplyOreOperator[#,FF[n,k,l]],1]&,{}]]]];
t0=AbsoluteTime[];
ctW = TimeConstrained[MemoryConstrained[CreativeTelescoping[annW,{S[k]-1,S[l]-1},{S[n]}],25*10^9,"M"],3600,"T"];
If[MatchQ[ctW,"T"|"M"], log["ctW ",ToString[ctW]," after ",Round[AbsoluteTime[]-t0],"s"]; Close[lf]; Exit[]];
log["ctW done in ",Round[AbsoluteTime[]-t0],"s; #telescopers=",ToString[Length[ctW[[1]]]]];
Put[ctW, DIR<>"ctW.m"];
Do[
  {ordi, poli} = opToPoly[ctW[[1,i]]];
  log["  W-telescoper ",ToString[i]," order=",ToString[ordi]];
  log["    poly = ",ToString[InputForm[Factor[poli]]]];
  If[ordi>=3, log["    LBZ mod = ",ToString[InputForm[Together[PolynomialRemainder[LBZ,poli,SS]]]]];
              log["    poli mod LBZ = ",ToString[InputForm[Together[PolynomialRemainder[poli,LBZ,SS]]]]]];
 ,{i,1,Length[ctW[[1]]]}];
log["DONE ",DateString[]];
Close[lf];Exit[];
