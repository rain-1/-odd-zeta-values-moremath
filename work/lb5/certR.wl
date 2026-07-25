(* certR.wl -- ROUTE R: weight-graded reduction.
   NOTE: `math < file.wl` reads line by line, so EVERY multi-line expression here is
   wrapped in parentheses -- otherwise it is silently truncated at the first
   syntactically complete line. *)
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf=OpenWrite[DIR<>"certR.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf];Print[x]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

TT = Binomial[n+k,n] Binomial[n,k]^2 Binomial[n+l,n] Binomial[n,l]^2 Binomial[n+k+l,n];
AA[r_,x_]:=HarmonicNumber[n+x,r]-HarmonicNumber[x,r];
BB[r_,x_]:=HarmonicNumber[n-x,r]-HarmonicNumber[x,r];
CC1 = HarmonicNumber[n+k+l]-HarmonicNumber[k+l];
a0[x_]:=41218 x^3+198849 x^2+320790 x+173057;
B8[x_]:=3874492 x^8+59373972 x^7+394148190 x^6+1481084196 x^5+3447878810 x^4+5095855458 x^3+4673546679 x^2+2433871008 x+551502039;
B9[x_]:=48802112 x^9+967468896 x^8+8488000862 x^7+43246197636 x^6+140983768422 x^5+304912330849 x^4+437406946975 x^3+401272692378 x^2+213593890911 x+50257929339;
cc3 = {(n+1)^5 (n+2) a0[n+1], -2 (n+2) B8[n], -2 B9[n], 2 (n+3)^5 (2n+5) a0[n]};
sh[e_,a_,b_,c_] := e /. {n->n+a, k->k+b, l->l+c};

(* the folded weight-3 weight; Sum_{k,l} T v = Sum_{k,l} T w3hat by the k<->l symmetry *)
vw = (HarmonicNumber[n,3] + 2 AA[3,k] - (1/2) AA[2,k] AA[1,k] - (3/2) AA[2,k] BB[1,k] - (3/4) AA[2,k] CC1 - (1/4) AA[2,k] AA[1,l]);
log["TRUNCATION CHECK: #HarmonicNumber in vw = ",
    Length[Cases[vw, HarmonicNumber[__], Infinity]], "  (must be 19)"];
If[Length[Cases[vw, HarmonicNumber[__], Infinity]] =!= 19,
   log["*** vw TRUNCATED -- abort ***"]; Close[lf]; Exit[]];

(* ---------- rho, sigma: reuse if already certified, else recompute ---------- *)
If[FileExistsQ[DIR<>"Qrow_rhosigma.m"],
   {rho,sigma} = Get[DIR<>"Qrow_rhosigma.m"]; log["rho,sigma loaded from disk"],
   Module[{ann0,ct1,alg2,gb,ct2,QQ,RR,pp,red,ff,ccf,XT,RT,apQ,cfQ,uu},
     ann0 = Annihilator[TT, {S[n],S[k],S[l]}];
     ct1 = CreativeTelescoping[ann0, S[k]-1, {S[n],S[l]}];
     alg2 = OreAlgebra[S[n],S[l]];
     gb  = OreGroebnerBasis[ct1[[1]], alg2];
     ct2 = CreativeTelescoping[gb, S[l]-1, {S[n]}];
     QQ = ct2[[1,1]]; RR = ct2[[2,1]];
     pp  = QQ + ToOrePolynomial[S[l]-1, alg2] ** RR;
     red = OreReduce[pp, gb, Extended->True];
     ff = red[[2]]; ccf = red[[3]];
     XT = Together[FunctionExpand[Total[Table[ApplyOreOperator[ccf[[i]] ** ct1[[2,i]], TT],
                                              {i, Length[ccf]}]] / (ff TT)]];
     RT = Together[FunctionExpand[ApplyOreOperator[RR, TT]/TT]];
     apQ = ApplyOreOperator[QQ, FF[n]];
     cfQ = Table[Coefficient[apQ, FF[n+j]], {j,0,3}];
     uu  = Together[cfQ[[1]]/cc3[[1]]];
     rho = Together[-XT/uu]; sigma = Together[-RT/uu];
     Put[{rho,sigma}, DIR<>"Qrow_rhosigma.m"]; log["rho,sigma recomputed"]]];
log["LeafCount rho/sigma = ",LeafCount[rho]," / ",LeafCount[sigma]];

(* ---------- re-check the Q-row single certificate ---------- *)
tsh[a_,b_,c_] := Together[FunctionExpand[(TT /. {n->n+a, k->k+b, l->l+c})/TT]];
chk = Together[FunctionExpand[(Sum[cc3[[j+1]] tsh[j,0,0], {j,0,3}] - ((rho /. k->k+1) tsh[0,1,0] - rho) - ((sigma /. l->l+1) tsh[0,0,1] - sigma))]];
log["*** Q-ROW SINGLE-CERTIFICATE CHECK: ", ToString[InputForm[chk]], " ***"];
If[chk =!= 0, log["Q-row certificate FAILED -- abort"]; Close[lf]; Exit[]];

(* ---------- E(v) ---------- *)
EE = (Sum[cc3[[j+1]] sh[TT,j,0,0] (sh[vw,j,0,0] - vw), {j,1,3}] - (rho /. k->k+1) sh[TT,0,1,0] (sh[vw,0,1,0] - vw) - (sigma /. l->l+1) sh[TT,0,0,1] (sh[vw,0,0,1] - vw));
log["E built, LeafCount=",LeafCount[EE]," #Harmonic=",
    Length[Cases[EE, HarmonicNumber[__], Infinity]]];
Put[EE, DIR<>"R_E.m"];

t0=AbsoluteTime[];
annE = Annihilator[EE, {S[n],S[k],S[l]}];
log["annE #",Length[annE]," t=",Round[AbsoluteTime[]-t0],"s ",DateString[]];
Put[annE, DIR<>"R_annE.m"];

box[A_,B_] := Flatten[Table[S[n]^a S[k]^b, {a,0,A},{b,0,B}]];
got={};
Do[Module[{A=bx[[1]],B=bx[[2]],t1,r},
   log["--- R step1 (elim l) box(",A,",",B,") --- ",DateString[]];
   t1=AbsoluteTime[];
   r = CreativeTelescoping[annE, S[l]-1, {}, Support -> box[A,B]];
   log["   t=",Round[AbsoluteTime[]-t1],"s ntel=",
       ToString[If[Head[r]===List,Length[r[[1]]],Head[r]]]," ",DateString[]];
   If[Head[r]===List && Length[r[[1]]]>0, AppendTo[got,r];
      Put[r, DIR<>"R_ct1_"<>ToString[A]<>ToString[B]<>".m"]; log["   SAVED"]]],
 {bx,{{1,1},{2,2},{3,3},{4,4},{5,5},{6,6}}}];
If[got==={}, log["R: no step-1 telescoper"]; Close[lf]; Exit[]];
tels = Union[Flatten[got[[All,1]]]];
gbE = OreGroebnerBasis[tels, OreAlgebra[S[n],S[k]]];
log["R gbE #",Length[gbE]];
Put[{got,gbE}, DIR<>"R_ct1all.m"];
Do[Module[{t1,r},
   log["--- R step2 Support S[n]^0..^",d," --- ",DateString[]];
   t1=AbsoluteTime[];
   r = CreativeTelescoping[gbE, S[k]-1, {}, Support -> Table[S[n]^j,{j,0,d}]];
   log["   d=",d," t=",Round[AbsoluteTime[]-t1],"s ntel=",
       ToString[If[Head[r]===List,Length[r[[1]]],Head[r]]]];
   If[Head[r]===List && Length[r[[1]]]>0, Put[r, DIR<>"R_ct2.m"];
      log["   SUCCESS ",DateString[]]; Close[lf]; Exit[]]],
 {d,{0,1,2,3,4,5,6}}];
log["ALL DONE ",DateString[]];
Close[lf]; Exit[];
