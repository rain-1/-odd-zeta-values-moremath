lf=OpenWrite["/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/gate3.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";

a0[x_]:=41218 x^3+198849 x^2+320790 x+173057;
B8[x_]:=3874492 x^8+59373972 x^7+394148190 x^6+1481084196 x^5+3447878810 x^4+5095855458 x^3+4673546679 x^2+2433871008 x+551502039;
B9[x_]:=48802112 x^9+967468896 x^8+8488000862 x^7+43246197636 x^6+140983768422 x^5+304912330849 x^4+437406946975 x^3+401272692378 x^2+213593890911 x+50257929339;
LBZ = (n+1)^5 (n+2) a0[n+1] + (-2 (n+2) B8[n]) SS + (-2 B9[n]) SS^2 + (2 (n+3)^5 (2n+5) a0[n]) SS^3;

opToPoly[op_] := Module[{ap,ord,coeffs},
  ap = ApplyOreOperator[op, FF[n]];
  ord = Max[Join[{0},Cases[ap, FF[n+a_.]:>a, Infinity]]];
  coeffs = Table[Coefficient[ap, FF[n+j]], {j,0,ord}];
  {ord, Sum[coeffs[[j+1]] SS^j, {j,0,ord}]}];

Tsum = Binomial[n+k,n] Binomial[n,k]^2 Binomial[n+l,n] Binomial[n,l]^2 Binomial[n+k+l,n];

doit[label_, summand_, tcap1_, tcap2_] := Module[{ann,ct1,gb,ct2,res,t0,i,ordi,poli},
  log["=== ",label," ==="];
  t0=AbsoluteTime[];
  ann = TimeConstrained[Annihilator[summand,{S[n],S[k],S[l]}],tcap1,"T"];
  If[ann==="T", log[label," Annihilator TIMECAP"]; Return[$Failed]];
  log[label," ann #",Length[ann]," in ",Round[AbsoluteTime[]-t0],"s"];
  t0=AbsoluteTime[];
  ct1 = TimeConstrained[CreativeTelescoping[ann,S[k]-1,{S[n],S[l]}],tcap1,"T"];
  If[ct1==="T"||ct1===$Failed, log[label," CT-k failed: ",ToString[ct1]]; Return[$Failed]];
  log[label," CT-k done in ",Round[AbsoluteTime[]-t0],"s, #q=",ToString[Length[ct1[[1]]]]];
  Put[ct1, DIR<>label<>"_ct1.m"];
  t0=AbsoluteTime[];
  gb = TimeConstrained[OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n],S[l]]],tcap1,"T"];
  If[gb==="T", log[label," GB TIMECAP"]; Return[$Failed]];
  log[label," GB #",Length[gb]," in ",Round[AbsoluteTime[]-t0],"s"];
  t0=AbsoluteTime[];
  ct2 = TimeConstrained[CreativeTelescoping[gb,S[l]-1,{S[n]}],tcap2,"T"];
  If[ct2==="T"||ct2===$Failed, log[label," CT-l failed: ",ToString[ct2]]; Return[$Failed]];
  log[label," CT-l done in ",Round[AbsoluteTime[]-t0],"s, #q=",ToString[Length[ct2[[1]]]]];
  Put[ct2, DIR<>label<>"_ct2.m"];
  Do[
    {ordi,poli} = opToPoly[ct2[[1,i]]];
    log[label,"  telescoper ",ToString[i]," ORDER=",ToString[ordi]];
    log[label,"    factored = ",ToString[InputForm[Factor[poli]]]];
    If[ordi>=3,
      log[label,"    PolynomialRemainder[LBZ, poli, SS] = ",ToString[InputForm[Together[PolynomialRemainder[LBZ,poli,SS]]]]];
      log[label,"    PolynomialRemainder[poli, LBZ, SS] = ",ToString[InputForm[Together[PolynomialRemainder[poli,LBZ,SS]]]]]];
   ,{i,1,Length[ct2[[1]]]}];
  ct2];

doit["Q", Tsum, 900, 1800];

Ar[r_,x_]:=HarmonicNumber[n+x,r]-HarmonicNumber[x,r];
Br[r_,x_]:=HarmonicNumber[n-x,r]-HarmonicNumber[x,r];
CC1 = HarmonicNumber[n+k+l,1]-HarmonicNumber[k+l,1];
w3 = HarmonicNumber[n,3] + Ar[3,k] + Ar[3,l]
     - 1/4 (Ar[2,k] Ar[1,k] + Ar[2,l] Ar[1,l])
     - 3/4 (Ar[2,k] Br[1,k] + Ar[2,l] Br[1,l])
     - 3/8 (Ar[2,k] + Ar[2,l]) CC1
     - 1/8 (Ar[2,k] Ar[1,l] + Ar[2,l] Ar[1,k]);
doit["W3", Tsum w3, 3600, 7200];

log["DONE ",DateString[]];
Close[lf];Exit[];
