(* certJ.wl -- rank-12 folded weight v, eliminate l FIRST (the cheap direction:
   only C1, A1(l), A2(k)C1, A2(k)A1(l) move under S_l, and only by one level),
   then k with a Support-bounded ansatz (the answer must be L_BZ, order 3).     *)
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf=OpenWrite[DIR<>"certK.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf];Print[x]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];
TT = Binomial[n+k,n] Binomial[n,k]^2 Binomial[n+l,n] Binomial[n,l]^2 Binomial[n+k+l,n];
AA[r_,x_]:=HarmonicNumber[n+x,r]-HarmonicNumber[x,r];
BB[r_,x_]:=HarmonicNumber[n-x,r]-HarmonicNumber[x,r];
CC1 = HarmonicNumber[n+k+l]-HarmonicNumber[k+l];
v = (HarmonicNumber[n,3] + 2 AA[3,k] - (1/2) AA[2,k] AA[1,k] - (3/2) AA[2,k] BB[1,k] - (3/4) AA[2,k] CC1 - (1/4) AA[2,k] AA[1,l]);
log["TRUNCATION CHECK #Harmonic in v = ",Length[Cases[v,HarmonicNumber[__],Infinity]]," (must be 19)"];
If[Length[Cases[v,HarmonicNumber[__],Infinity]]=!=19, log["*** v TRUNCATED ***"]; Close[lf]; Exit[]];
ord[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]];
   Max[Join[{0}, Cases[ap, FF[n+a_.] :> a, Infinity]]]];
t0=AbsoluteTime[];
ann = If[FileExistsQ[DIR<>"I_ann.m"], Get[DIR<>"I_ann.m"], Annihilator[TT v, {S[n],S[k],S[l]}]];
log["K ann #",Length[ann]," t=",Round[AbsoluteTime[]-t0],"s"];
Put[ann, DIR<>"I_ann.m"];
t0=AbsoluteTime[];
box[A_,B_] := Flatten[Table[S[n]^a S[k]^b, {a,0,A}, {b,0,B}]];
got={};
Do[Module[{A=bx[[1]],B=bx[[2]],t1,r},
   log["--- K step1 box(",A,",",B,") --- ",DateString[]];
   t1=AbsoluteTime[];
   r = CreativeTelescoping[ann, S[l]-1, {}, Support -> box[A,B]];
   log["   t=",Round[AbsoluteTime[]-t1],"s head=",ToString[Head[r]],
       If[Head[r]===List, "  ntel="<>ToString[Length[r[[1]]]], ""]," ",DateString[]];
   If[Head[r]===List && Length[r[[1]]]>0, AppendTo[got,r];
      Put[r, DIR<>"K_ct1_"<>ToString[A]<>ToString[B]<>".m"]; log["   SAVED"]]],
 {bx,{{2,2},{3,3},{4,4},{5,5},{6,6}}}];
If[got==={}, log["K: no step-1 telescoper in any box"]; Close[lf]; Exit[]];
ct1 = {Union[Flatten[got[[All,1]]]], Union[Flatten[got[[All,2]]]]};
log["K ct1 #",Length[ct1[[1]]]," t=",Round[AbsoluteTime[]-t0],"s ",DateString[]];
Put[ct1, DIR<>"K_ct1.m"];
t0=AbsoluteTime[];
gb = OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n],S[k]]];
log["K gb #",Length[gb]," t=",Round[AbsoluteTime[]-t0],"s"];
Put[gb, DIR<>"K_gb.m"];
Do[Module[{t1,r},
   log["--- J step2 Support S[n]^0..^",d," --- ",DateString[]];
   t1=AbsoluteTime[];
   r = CreativeTelescoping[gb, S[k]-1, {}, Support -> Table[S[n]^j,{j,0,d}]];
   log["   d=",d," t=",Round[AbsoluteTime[]-t1],"s head=",ToString[Head[r]]];
   If[Head[r]===List && Length[r[[1]]]>0, Put[r, DIR<>"K_ct2.m"];
      log["   SUCCESS ORDER=",ToString[ord[r[[1,1]]]]," ",DateString[]];
      log["ALL DONE ",DateString[]]; Close[lf]; Exit[]]],
 {d,{3,4,5,6}}];
log["K step2 fallback unconstrained ",DateString[]];
t0=AbsoluteTime[];
ct2 = CreativeTelescoping[gb, S[k]-1, {S[n]}];
log["K ct2 #",Length[ct2[[1]]]," t=",Round[AbsoluteTime[]-t0],"s ORDER=",ToString[ord[ct2[[1,1]]]]];
Put[ct2, DIR<>"K_ct2.m"];
log["ALL DONE ",DateString[]]; Close[lf]; Exit[];
