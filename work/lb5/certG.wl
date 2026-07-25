(* certG.wl -- full w3hat, two-step CT, default uncoupling for step 1 (patience),
   Support-CONSTRAINED step 2 (we know the answer should be L_BZ, order 3).
   Reuses w3h_ann.m if present. *)
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf=OpenWrite[DIR<>"certG.log"];
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

t0=AbsoluteTime[];
ann = If[FileExistsQ[DIR<>"w3h_ann.m"], Get[DIR<>"w3h_ann.m"],
         Annihilator[TT w3hat, {S[n],S[k],S[l]}]];
log["ann #",Length[ann]," t=",Round[AbsoluteTime[]-t0],"s"];
Put[ann, DIR<>"w3h_ann.m"];

t0=AbsoluteTime[];
ct1 = CreativeTelescoping[ann, S[k]-1, {S[n],S[l]}];
log["G ct1 #",Length[ct1[[1]]]," t=",Round[AbsoluteTime[]-t0],"s ",DateString[]];
Put[ct1, DIR<>"G_ct1.m"];

t0=AbsoluteTime[];
gb = OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n],S[l]]];
log["G gb #",Length[gb]," t=",Round[AbsoluteTime[]-t0],"s"];
Put[gb, DIR<>"G_gb.m"];

Do[
 Module[{t1, r},
  log["--- step2 Support S[n]^0..^",d," --- ",DateString[]];
  t1 = AbsoluteTime[];
  r = CreativeTelescoping[gb, S[l]-1, {}, Support -> Table[S[n]^j,{j,0,d}]];
  log["  d=",d," t=",Round[AbsoluteTime[]-t1],"s head=",ToString[Head[r]]];
  If[Head[r]===List && Length[r[[1]]]>0,
    Put[r, DIR<>"G_ct2.m"];
    log["  SUCCESS d=",d," ORDER=",ToString[ord[r[[1,1]]]]," ",DateString[]];
    log["ALL DONE ",DateString[]]; Close[lf]; Exit[]]],
 {d, {3, 4, 5, 6, 8}}];

log["Support route exhausted; falling back to unconstrained step 2 ",DateString[]];
t0=AbsoluteTime[];
ct2 = CreativeTelescoping[gb, S[l]-1, {S[n]}];
log["G ct2 #",Length[ct2[[1]]]," t=",Round[AbsoluteTime[]-t0],"s ORDER=",ToString[ord[ct2[[1,1]]]]];
Put[ct2, DIR<>"G_ct2.m"];
log["ALL DONE ",DateString[]];
Close[lf]; Exit[];
