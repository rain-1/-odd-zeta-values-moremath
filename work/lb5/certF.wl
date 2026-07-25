(* certF.wl -- Chyzak with a NON-Groebner uncoupling (OreSys).  The default
   uncoupling (SolveCoupledSystem via Groebner bases) is what hangs on the
   harmonic-weighted summands; Zuercher / AbramovZima are often far faster. *)
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf=OpenWrite[DIR<>"certF.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf];Print[x]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
Get["/home/ubuntu/riscergosum/RISC/OreSys.m"];
log["HF+OreSys loaded ",DateString[]];

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

go[lab_, wt_, first_, second_, meth_]:=Module[{ann,ct1,gb,ct2,t0,rest},
  log["=== ",lab," elim ",ToString[first],"->",ToString[second]," Method=",ToString[meth]," === ",DateString[]];
  t0=AbsoluteTime[];
  ann = Annihilator[TT wt, {S[n],S[k],S[l]}];
  log[lab," ann #",Length[ann]," t=",Round[AbsoluteTime[]-t0],"s"];
  Put[ann, DIR<>lab<>"_ann.m"];
  rest = If[first===k, {S[n],S[l]}, {S[n],S[k]}];
  t0=AbsoluteTime[];
  ct1 = CreativeTelescoping[ann, S[first]-1, rest, Method->meth];
  log[lab," ct1 #",Length[ct1[[1]]]," t=",Round[AbsoluteTime[]-t0],"s ",DateString[]];
  Put[ct1, DIR<>lab<>"_ct1.m"];
  t0=AbsoluteTime[];
  gb = OreGroebnerBasis[ct1[[1]], OreAlgebra@@rest, Extended->True];
  log[lab," gb(ext) #",Length[gb[[1]]]," t=",Round[AbsoluteTime[]-t0],"s"];
  Put[gb, DIR<>lab<>"_gbx.m"];
  t0=AbsoluteTime[];
  ct2 = CreativeTelescoping[gb[[1]], S[second]-1, {S[n]}, Method->meth];
  log[lab," ct2 #",Length[ct2[[1]]]," t=",Round[AbsoluteTime[]-t0],"s"];
  Put[ct2, DIR<>lab<>"_ct2.m"];
  log[lab," ORDER=",ToString[ord[ct2[[1,1]]]]," ",DateString[]];
  ct2];

(* calibration: the case that hung >40 min with the default uncoupling *)
go["Z1", CC1, k, l, Zuercher];
(* the money shot *)
go["ZW", w3hat, k, l, Zuercher];
log["ALL DONE ",DateString[]];
Close[lf]; Exit[];
