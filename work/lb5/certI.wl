(* certI.wl -- RANK REDUCTION by the k<->l symmetry.

   T is k<->l symmetric, so under Sum_{k,l} every l-letter monomial of w3hat may be
   folded onto its k-mirror:
     Sum T w3hat = Sum T v,
     v = H^(3)_n + 2 A3(k) - 1/2 A2(k)A1(k) - 3/2 A2(k)B1(k)
                 - 3/4 A2(k) C1 - 1/4 A2(k) A1(l).
   The shift-closure of T*v spans 12 monomials
     {1, A1(k), A2(k), A3(k), B1(k), C1, A1(l), N3, A2A1(k), A2B1(k), A2(k)C1, A2(k)A1(l)}
   versus 19 for T*w3hat.  Since Sum T v = P-hat_n, the minimal telescoper is still
   L_BZ (order 3), so Support -> {1,S[n],S[n]^2,S[n]^3} is correct for step 2.

   Both steps are Support-bounded, hence finite linear algebra: they terminate. *)
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf=OpenWrite[DIR<>"certI.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf];Print[x]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

TT = Binomial[n+k,n] Binomial[n,k]^2 Binomial[n+l,n] Binomial[n,l]^2 Binomial[n+k+l,n];
AA[r_,x_]:=HarmonicNumber[n+x,r]-HarmonicNumber[x,r];
BB[r_,x_]:=HarmonicNumber[n-x,r]-HarmonicNumber[x,r];
CC1 = HarmonicNumber[n+k+l]-HarmonicNumber[k+l];
v = (HarmonicNumber[n,3] + 2 AA[3,k] - (1/2) AA[2,k] AA[1,k] - (3/2) AA[2,k] BB[1,k]
    - (3/4) AA[2,k] CC1 - (1/4) AA[2,k] AA[1,l]);
ord[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]];
   Max[Join[{0}, Cases[ap, FF[n+a_.] :> a, Infinity]]]];

t0=AbsoluteTime[];
ann = Annihilator[TT v, {S[n],S[k],S[l]}];
log["I ann #",Length[ann]," t=",Round[AbsoluteTime[]-t0],"s ords=",
    ToString[Map[Exponent[ToOrePolynomial[#],{S[n],S[k],S[l]}]&,ann]]];
Put[ann, DIR<>"I_ann.m"];

box[A_,B_] := Flatten[Table[S[n]^a S[l]^b, {a,0,A}, {b,0,B}]];
got = {};
Do[Module[{A=bx[[1]], B=bx[[2]], t1, r},
   log["--- step1 box(",A,",",B,") --- ",DateString[]];
   t1=AbsoluteTime[];
   r = CreativeTelescoping[ann, S[k]-1, {}, Support -> box[A,B]];
   log["   t=",Round[AbsoluteTime[]-t1],"s head=",ToString[Head[r]],
       If[Head[r]===List, "  ntel="<>ToString[Length[r[[1]]]], ""]," ",DateString[]];
   If[Head[r]===List && Length[r[[1]]]>0,
      Put[r, DIR<>"I_ct1_"<>ToString[A]<>ToString[B]<>".m"];
      AppendTo[got, r]; log["   SAVED I_ct1_",A,B,".m"]]],
 {bx, {{1,1},{2,2},{2,3},{3,3}}}];

If[got === {}, log["no step-1 telescoper found in the boxes tried"]; Close[lf]; Exit[]];

tels = Union[Flatten[got[[All,1]]]];
log["step1 telescopers collected: ",Length[tels]];
t0=AbsoluteTime[];
gb = OreGroebnerBasis[tels, OreAlgebra[S[n],S[l]]];
log["gb #",Length[gb]," t=",Round[AbsoluteTime[]-t0],"s"];
Put[gb, DIR<>"I_gb.m"];
Put[got, DIR<>"I_ct1all.m"];

Do[Module[{t1,r},
   log["--- step2 Support S[n]^0..^",d," --- ",DateString[]];
   t1=AbsoluteTime[];
   r = CreativeTelescoping[gb, S[l]-1, {}, Support -> Table[S[n]^j,{j,0,d}]];
   log["   d=",d," t=",Round[AbsoluteTime[]-t1],"s head=",ToString[Head[r]]];
   If[Head[r]===List && Length[r[[1]]]>0,
      Put[r, DIR<>"I_ct2.m"];
      log["   SUCCESS ORDER=",ToString[ord[r[[1,1]]]]," ",DateString[]];
      log["ALL DONE ",DateString[]]; Close[lf]; Exit[]]],
 {d, {3,4,5,6}}];
log["ALL DONE (step 2 not found) ",DateString[]];
Close[lf]; Exit[];
