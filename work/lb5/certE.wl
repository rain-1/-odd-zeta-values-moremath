(* certE.wl -- Support-constrained creative telescoping.
   With Support -> {...} the telescoper ansatz is FIXED, so the computation is
   finite linear algebra and terminates (success or failure) instead of searching.
   Target: a single-shot double-sum certificate
       L . W  +  (S_k-1)(X . W)  +  (S_l-1)(Y . W) = 0,     L of order <= 3 in S[n],
   for W = T (sanity) and W = T*w3hat (Theorem B). *)
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf=OpenWrite[DIR<>"certE.log"];
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

sup[d_] := Table[S[n]^j, {j, 0, d}];

joint[lab_, ann_, d_] := Module[{t0, r},
  log["--- ",lab," joint delta, Support S[n]^0..^",d," --- ",DateString[]];
  t0 = AbsoluteTime[];
  r = CreativeTelescoping[ann, {S[k]-1, S[l]-1}, {}, Support -> sup[d]];
  log[lab," t=",Round[AbsoluteTime[]-t0],"s  head=",ToString[Head[r]],
      "  len=",ToString[If[Head[r]===List,Length[r],"-"]]];
  If[Head[r]===List && Length[r]>=2 && Length[r[[1]]]>0,
     Put[r, DIR<>lab<>"_joint.m"];
     log[lab," SUCCESS ntel=",Length[r[[1]]]," ORDER=",ToString[ord[r[[1,1]]]]],
     log[lab," no telescoper for this support"]];
  r];

t0=AbsoluteTime[];
ann0 = Annihilator[TT, {S[n],S[k],S[l]}];
log["ann0 #",Length[ann0]," t=",Round[AbsoluteTime[]-t0],"s"];
joint["E1", ann0, 3];

t0=AbsoluteTime[];
annW = Annihilator[TT w3hat, {S[n],S[k],S[l]}];
log["annW #",Length[annW]," t=",Round[AbsoluteTime[]-t0],"s"];
Put[annW, DIR<>"w3h_ann.m"];
joint["E2", annW, 3];
joint["E3", annW, 5];
joint["E4", annW, 8];
log["ALL DONE ",DateString[]];
Close[lf]; Exit[];
