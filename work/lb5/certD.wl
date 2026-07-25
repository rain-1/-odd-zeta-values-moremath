(* certD.wl -- ordering experiment.  For a summand T*m where m does not involve l,
   the l-direction is rank 1, so eliminate l FIRST (cheap) and k second.
   Also dumps the usage strings so the Support option syntax can be learned. *)
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf=OpenWrite[DIR<>"certD.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf];Print[x]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];
log["USAGE CT: ", ToString[CreativeTelescoping::usage]];
log["USAGE OGB: ", ToString[OreGroebnerBasis::usage]];
log["USAGE OreReduce: ", ToString[OreReduce::usage]];

TT = Binomial[n+k,n] Binomial[n,k]^2 Binomial[n+l,n] Binomial[n,l]^2 Binomial[n+k+l,n];
AA[r_,x_]:=HarmonicNumber[n+x,r]-HarmonicNumber[x,r];
BB[r_,x_]:=HarmonicNumber[n-x,r]-HarmonicNumber[x,r];
CC1 = HarmonicNumber[n+k+l]-HarmonicNumber[k+l];

go[lab_, wt_, first_, second_]:=Module[{ann,ct1,gb,ct2,t0,ap,rest},
  log["=== ",lab," (elim ",ToString[first]," then ",ToString[second],") === ",DateString[]];
  t0=AbsoluteTime[];
  ann = Annihilator[TT wt, {S[n],S[k],S[l]}];
  log[lab," ann #",Length[ann]," t=",Round[AbsoluteTime[]-t0],"s"];
  Put[ann, DIR<>lab<>"_ann.m"];
  rest = If[first===k, {S[n],S[l]}, {S[n],S[k]}];
  t0=AbsoluteTime[];
  ct1 = CreativeTelescoping[ann, S[first]-1, rest];
  log[lab," ct1 #",Length[ct1[[1]]]," t=",Round[AbsoluteTime[]-t0],"s"];
  Put[ct1, DIR<>lab<>"_ct1.m"];
  t0=AbsoluteTime[];
  gb = OreGroebnerBasis[ct1[[1]], OreAlgebra@@rest];
  log[lab," gb #",Length[gb]," t=",Round[AbsoluteTime[]-t0],"s  gb===ct1tel? ",ToString[gb === ct1[[1]]]];
  Put[gb, DIR<>lab<>"_gb.m"];
  t0=AbsoluteTime[];
  ct2 = CreativeTelescoping[gb, S[second]-1, {S[n]}];
  log[lab," ct2 #",Length[ct2[[1]]]," t=",Round[AbsoluteTime[]-t0],"s"];
  Put[ct2, DIR<>lab<>"_ct2.m"];
  ap = ApplyOreOperator[ct2[[1,1]], FF[n]];
  log[lab," ORDER=",ToString[Max[Cases[ap,FF[n+a_.]:>a,Infinity]]]," ",DateString[]];
  ct2];

go["Y1", AA[1,k], l, k];         (* weight 1, rank 2, l-first *)
go["Y3", AA[3,k], l, k];         (* weight 3, rank 2, l-first  = U1 *)
go["Y2", AA[2,k] AA[1,k], l, k]; (* weight 3, rank 4, l-first  = U2 *)
go["Y4", AA[2,k] BB[1,k], l, k]; (* weight 3, rank 4, l-first  = U3 *)
log["ALL DONE ",DateString[]];
Close[lf]; Exit[];
