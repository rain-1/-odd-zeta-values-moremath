(* certA.wl -- direct two-step CT on the FULL w3hat-weighted summand.
   Goal: telescoper for R_n = Sum_{k,l} T(n,k,l) w3hat(n,k,l).  Expect L_BZ (order 3). *)
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf=OpenWrite[DIR<>"certA.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf];Print[x]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded ",DateString[]];

TT = Binomial[n+k,n] Binomial[n,k]^2 Binomial[n+l,n] Binomial[n,l]^2 Binomial[n+k+l,n];
AA[r_,x_]:=HarmonicNumber[n+x,r]-HarmonicNumber[x,r];
BB[r_,x_]:=HarmonicNumber[n-x,r]-HarmonicNumber[x,r];
CC1 = HarmonicNumber[n+k+l]-HarmonicNumber[k+l];
w3hat = (HarmonicNumber[n,3] + AA[3,k] + AA[3,l]
        - (1/4)(AA[2,k] AA[1,k] + AA[2,l] AA[1,l])
        - (3/4)(AA[2,k] BB[1,k] + AA[2,l] BB[1,l])
        - (3/8)(AA[2,k] + AA[2,l]) CC1
        - (1/8)(AA[2,k] AA[1,l] + AA[2,l] AA[1,k]));

lab="w3h";
t0=AbsoluteTime[];
ann = Annihilator[TT w3hat, {S[n],S[k],S[l]}];
log[lab," ann #",Length[ann]," t=",Round[AbsoluteTime[]-t0],"s ",DateString[]];
Put[ann, DIR<>lab<>"_ann.m"];
log[lab," ann ords=",ToString[Map[Exponent[ToOrePolynomial[#],{S[n],S[k],S[l]}]&,ann]]];

t0=AbsoluteTime[];
ct1 = CreativeTelescoping[ann, S[k]-1, {S[n],S[l]}];
log[lab," ct1 #",Length[ct1[[1]]]," t=",Round[AbsoluteTime[]-t0],"s ",DateString[]];
Put[ct1, DIR<>lab<>"_ct1.m"];

t0=AbsoluteTime[];
gb = OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n],S[l]]];
log[lab," gb #",Length[gb]," t=",Round[AbsoluteTime[]-t0],"s ",DateString[]];
Put[gb, DIR<>lab<>"_gb.m"];

t0=AbsoluteTime[];
ct2 = CreativeTelescoping[gb, S[l]-1, {S[n]}];
log[lab," ct2 #",Length[ct2[[1]]]," t=",Round[AbsoluteTime[]-t0],"s ",DateString[]];
Put[ct2, DIR<>lab<>"_ct2.m"];
ap = ApplyOreOperator[ct2[[1,1]], FF[n]];
log[lab," ORDER=",ToString[Max[Cases[ap,FF[n+a_.]:>a,Infinity]]]];
log["ALL DONE ",DateString[]];
Close[lf]; Exit[];
