(* certH.wl -- Support-CONSTRAINED first elimination for the full w3hat summand.
   With Support -> {S[n]^a S[l]^b} fixed, step 1 is a bounded linear solve and
   terminates; run over a ladder of boxes until enough telescopers are found to
   generate an ideal that step 2 can eliminate l from. *)
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf=OpenWrite[DIR<>"certH.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf];Print[x]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

TT = Binomial[n+k,n] Binomial[n,k]^2 Binomial[n+l,n] Binomial[n,l]^2 Binomial[n+k+l,n];
AA[r_,x_]:=HarmonicNumber[n+x,r]-HarmonicNumber[x,r];
BB[r_,x_]:=HarmonicNumber[n-x,r]-HarmonicNumber[x,r];
CC1 = HarmonicNumber[n+k+l]-HarmonicNumber[k+l];
w3hat = (HarmonicNumber[n,3] + AA[3,k] + AA[3,l]
        - (1/4)(AA[2,k] AA[1,k] + AA[2,l] AA[1,l])
        - (3/4)(AA[2,k] BB[1,k] + AA[2,l] BB[1,l])
        - (3/8)(AA[2,k] + AA[2,l]) CC1
        - (1/8)(AA[2,k] AA[1,l] + AA[2,l] AA[1,k]));
ord[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]];
   Max[Join[{0}, Cases[ap, FF[n+a_.] :> a, Infinity]]]];

ann = If[FileExistsQ[DIR<>"w3h_ann.m"], Get[DIR<>"w3h_ann.m"],
         Annihilator[TT w3hat, {S[n],S[k],S[l]}]];
log["ann #",Length[ann]];

(* sanity first: the undeformed T, where we know a (1,1)-support telescoper exists *)
ann0 = Annihilator[TT, {S[n],S[k],S[l]}];
box[A_,B_] := Flatten[Table[S[n]^a S[l]^b, {a,0,A}, {b,0,B}]];
t0=AbsoluteTime[];
s0 = CreativeTelescoping[ann0, S[k]-1, {}, Support -> box[1,1]];
log["SANITY undeformed, box(1,1): t=",Round[AbsoluteTime[]-t0],"s head=",ToString[Head[s0]],
    If[Head[s0]===List, "  ntel="<>ToString[Length[s0[[1]]]], ""]];

res = None;
Do[Module[{A=bx[[1]], B=bx[[2]], t1, r},
   log["--- w3hat step1 box(",A,",",B,") --- ",DateString[]];
   t1=AbsoluteTime[];
   r = CreativeTelescoping[ann, S[k]-1, {}, Support -> box[A,B]];
   log["   t=",Round[AbsoluteTime[]-t1],"s head=",ToString[Head[r]],
       If[Head[r]===List, "  ntel="<>ToString[Length[r[[1]]]], ""]," ",DateString[]];
   If[Head[r]===List && Length[r[[1]]]>0,
      Put[r, DIR<>"H_ct1_"<>ToString[A]<>ToString[B]<>".m"];
      log["   SAVED H_ct1_",A,B,".m"]]],
 {bx, {{1,1},{2,2},{3,3},{2,4},{4,4}}}];
log["ALL DONE ",DateString[]];
Close[lf]; Exit[];
