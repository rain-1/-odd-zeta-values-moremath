(* certB.wl -- per-monomial two-step CT.  w3hat = H^(3)_n + A3k + A3l
     - 1/4(A2k A1k + A2l A1l) - 3/4(A2k B1k + A2l B1l)
     - 3/8(A2k+A2l) C1 - 1/8(A2k A1l + A2l A1k).
   T is k<->l symmetric, so Sum T*m = Sum T*m^sigma; only 5 distinct sums:
     U1 = Sum T A3k ,  U2 = Sum T A2k A1k ,  U3 = Sum T A2k B1k ,
     U4 = Sum T A2k C1 , U5 = Sum T A2k A1l .
   Sum T w3hat = H^(3)_n Q_n + 2 U1 - 1/2 U2 - 3/2 U3 - 3/4 U4 - 1/4 U5. *)
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf=OpenWrite[DIR<>"certB.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf];Print[x]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded ",DateString[]];

TT = Binomial[n+k,n] Binomial[n,k]^2 Binomial[n+l,n] Binomial[n,l]^2 Binomial[n+k+l,n];
AA[r_,x_]:=HarmonicNumber[n+x,r]-HarmonicNumber[x,r];
BB[r_,x_]:=HarmonicNumber[n-x,r]-HarmonicNumber[x,r];
CC1 = HarmonicNumber[n+k+l]-HarmonicNumber[k+l];

go[lab_, wt_]:=Module[{ann,ct1,gb,ct2,t0,ap},
  log["=== ",lab," === ",DateString[]];
  t0=AbsoluteTime[];
  ann = Annihilator[TT wt, {S[n],S[k],S[l]}];
  log[lab," ann #",Length[ann]," t=",Round[AbsoluteTime[]-t0],"s"];
  Put[ann, DIR<>lab<>"_ann.m"];
  log[lab," ann ords=",ToString[Map[Exponent[ToOrePolynomial[#],{S[n],S[k],S[l]}]&,ann]]];
  t0=AbsoluteTime[];
  ct1 = CreativeTelescoping[ann, S[k]-1, {S[n],S[l]}];
  log[lab," ct1 #",Length[ct1[[1]]]," t=",Round[AbsoluteTime[]-t0],"s"];
  Put[ct1, DIR<>lab<>"_ct1.m"];
  t0=AbsoluteTime[];
  gb = OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n],S[l]]];
  log[lab," gb #",Length[gb]," t=",Round[AbsoluteTime[]-t0],"s"];
  Put[gb, DIR<>lab<>"_gb.m"];
  t0=AbsoluteTime[];
  ct2 = CreativeTelescoping[gb, S[l]-1, {S[n]}];
  log[lab," ct2 #",Length[ct2[[1]]]," t=",Round[AbsoluteTime[]-t0],"s"];
  Put[ct2, DIR<>lab<>"_ct2.m"];
  ap = ApplyOreOperator[ct2[[1,1]], FF[n]];
  log[lab," ORDER=",ToString[Max[Cases[ap,FF[n+a_.]:>a,Infinity]]]," ",DateString[]];
  ct2];

go["U1", AA[3,k]];
go["U4", AA[2,k] CC1];
go["U5", AA[2,k] AA[1,l]];
go["U2", AA[2,k] AA[1,k]];
go["U3", AA[2,k] BB[1,k]];
log["ALL DONE ",DateString[]];
Close[lf]; Exit[];
