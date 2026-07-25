(* certC.wl -- cost ladder + API probe.  Find where two-step CT on T*(harmonic letter)
   stops being cheap, and learn whether cofactors are available for certificate composition. *)
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf=OpenWrite[DIR<>"certC.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf];Print[x]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];
log["Options[CreativeTelescoping] = ",ToString[InputForm[Options[CreativeTelescoping]]]];
log["Options[OreReduce] = ",ToString[InputForm[Options[OreReduce]]]];
log["Options[OreGroebnerBasis] = ",ToString[InputForm[Options[OreGroebnerBasis]]]];
log["Options[Annihilator] = ",ToString[InputForm[Options[Annihilator]]]];

TT = Binomial[n+k,n] Binomial[n,k]^2 Binomial[n+l,n] Binomial[n,l]^2 Binomial[n+k+l,n];
AA[r_,x_]:=HarmonicNumber[n+x,r]-HarmonicNumber[x,r];
BB[r_,x_]:=HarmonicNumber[n-x,r]-HarmonicNumber[x,r];
CC1 = HarmonicNumber[n+k+l]-HarmonicNumber[k+l];

go[lab_, wt_, first_, second_]:=Module[{ann,ct1,gb,ct2,t0,ap,rest},
  log["=== ",lab," (elim ",ToString[first],") === ",DateString[]];
  t0=AbsoluteTime[];
  ann = Annihilator[TT wt, {S[n],S[k],S[l]}];
  log[lab," ann #",Length[ann]," t=",Round[AbsoluteTime[]-t0],"s ords=",
      ToString[Map[Exponent[ToOrePolynomial[#],{S[n],S[k],S[l]}]&,ann]]];
  Put[ann, DIR<>lab<>"_ann.m"];
  rest = If[first===k, {S[n],S[l]}, {S[n],S[k]}];
  t0=AbsoluteTime[];
  ct1 = CreativeTelescoping[ann, S[first]-1, rest];
  log[lab," ct1 #",Length[ct1[[1]]]," t=",Round[AbsoluteTime[]-t0],"s"];
  Put[ct1, DIR<>lab<>"_ct1.m"];
  t0=AbsoluteTime[];
  gb = OreGroebnerBasis[ct1[[1]], OreAlgebra@@rest];
  log[lab," gb #",Length[gb]," t=",Round[AbsoluteTime[]-t0],"s  gb===ct1tel? ",
      ToString[gb === ct1[[1]]]];
  Put[gb, DIR<>lab<>"_gb.m"];
  t0=AbsoluteTime[];
  ct2 = CreativeTelescoping[gb, S[second]-1, {S[n]}];
  log[lab," ct2 #",Length[ct2[[1]]]," t=",Round[AbsoluteTime[]-t0],"s"];
  Put[ct2, DIR<>lab<>"_ct2.m"];
  ap = ApplyOreOperator[ct2[[1,1]], FF[n]];
  log[lab," ORDER=",ToString[Max[Cases[ap,FF[n+a_.]:>a,Infinity]]]," ",DateString[]];
  ct2];

go["X0", 1, k, l];                       (* sanity: undeformed *)
go["X1", CC1, k, l];                     (* weight 1, coupling letter *)
go["X2", AA[1,k], l, k];                 (* weight 1, k-letter -- eliminate l FIRST (rank 1 in l) *)
go["X3", AA[1,k], k, l];                 (* same, k first, for comparison *)
go["X4", AA[3,k], l, k];                 (* weight 3, single letter, l first *)
go["X5", AA[2,k] AA[1,l], l, k];
log["ALL DONE ",DateString[]];
Close[lf]; Exit[];
