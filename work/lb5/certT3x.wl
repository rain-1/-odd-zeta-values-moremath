(* certT3x.wl -- compose the TWO-STEP certificate produced by certT3.wl into
   SINGLE-certificate form, for the RANK-3 form of E(v).

       E3 := T * ( c0 + beta*A2(k) + alpha*Psi )   ( = E(v), PHASE2_CERTS section 11 )

   certT3.wl produced, in this order,
       T3_ann.m  ann  = Annihilator[E3, {S[n],S[k],S[l]}]
       T3_ct1.m  ct1  = CreativeTelescoping[ann, S[l]-1, {S[n],S[k]}]
                        so that  ct1[[1,i]] + (S[l]-1) ** ct1[[2,i]]  is in ann
       T3_gb.m   gb   = OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n],S[k]]]   (= ct1[[1]])
       T3_ct2.m  ct2  = CreativeTelescoping[gb, S[k]-1, {}, Support -> ...]
                        so that  M + (S[k]-1) ** RR  is in the ideal of gb,
                        M = ct2[[1,1]], RR = ct2[[2,1]].

   With  OreReduce[M + (S[k]-1)**RR, gb, Extended->True] = {0, ff, ccf}, i.e.
       ff * ( M + (S[k]-1)**RR )  =  Sum_i ccf_i ** gb_i ,
   and  gb_i . E3 = -Delta_l( ct1[[2,i]] . E3 )  (Delta_l commutes with S[n], S[k]):

       M . E3  =  Delta_k( Ck . E3 )  +  Delta_l( Cl . E3 ) ,
       Ck  =  -RR ,
       Cl  =  -(1/ff) Sum_i ccf_i ** ct1[[2,i]] .

   The operator product is done with verifycore.wl's OWN hand-rolled Ore algebra
   (opTimes), not with RISC's **, so that the certificate that gets checked in
   certT3v.wl has not passed through the package whose output is being verified.
   RISC is used here only for OreReduce (a search step).

   Output: T3_cert.m = {cf, CkO, ClO}  where cf = coefficient list of M in S[n]
           and CkO, ClO are ope[{S[n],S[k],S[l]}, {{coef,expvec},...}] objects.

   Run:  math < certT3x.wl                                                        *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf = OpenWrite[DIR <> "certT3x.log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

need = {"T3_ann.m", "T3_ct1.m", "T3_gb.m", "T3_ct2.m"};
Do[If[! FileExistsQ[DIR <> f], log["MISSING ", f]; Close[lf]; Exit[]], {f, need}];
ann = Get[DIR <> "T3_ann.m"];
ct1 = Get[DIR <> "T3_ct1.m"];
gb = Get[DIR <> "T3_gb.m"];
ct2 = Get[DIR <> "T3_ct2.m"];
log["loaded: ann #", Length[ann], " ct1tel #", Length[ct1[[1]]],
    " gb #", Length[gb], " ct2tel #", Length[ct2[[1]]]];

alg2 = OreAlgebra[S[n], S[k]];
alg3 = OreAlgebra[S[n], S[k], S[l]];
ordOf[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]];
   Max[Join[{0}, Cases[ap, FF[n + a_.] :> a, Infinity]]]];

MM = ct2[[1, 1]];
RR = ct2[[2, 1]];
dM = ordOf[MM];
log["telescoper M : order ", dM, "  LeafCount ", LeafCount[MM]];

If[gb =!= ct1[[1]],
   log["NOTE gb =!= ct1 telescopers -- the Groebner cofactor chain IS needed;"];
   log["     this script assumes gb === ct1[[1]].  ABORTING."]; Close[lf]; Exit[]];

pp = MM + ToOrePolynomial[S[k] - 1, alg2] ** RR;
red = OreReduce[pp, gb, Extended -> True];
log["OreReduce remainder = ", ToString[InputForm[red[[1]]]],
    "   ff = ", ToString[InputForm[red[[2]]]]];
ff = red[[2]]; ccf = red[[3]];

(* ---- hand-rolled (RISC-free) assembly of the two certificate operators ---- *)
Get[DIR <> "verifycore.wl"];
vars3 = {S[n], S[k], S[l]};
CkO = opScal[-1, toOpe[RR, vars3]];
ClO = opScal[-1/ff,
   Fold[opPlus, ope[vars3, {}],
     Table[opTimes[toOpe[ccf[[i]], vars3], toOpe[ct1[[2, i]], vars3]],
           {i, Length[ccf]}]]];
log["Ck terms ", Length[CkO[[2]]], "  LeafCount ", LeafCount[CkO]];
log["Cl terms ", Length[ClO[[2]]], "  LeafCount ", LeafCount[ClO]];

cf = Table[Together[Coefficient[ApplyOreOperator[MM, FF[n]], FF[n + j]]], {j, 0, dM}];
log["M coefficient LeafCounts ", ToString[LeafCount /@ cf]];
Put[{cf, CkO, ClO}, DIR <> "T3_cert.m"];
log["saved T3_cert.m"];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
