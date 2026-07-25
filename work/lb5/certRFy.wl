(* certRFy.wl -- ASSEMBLY for the refold route (certRF.wl / certRFD.wl).

   Reads  RF_<ORD>_cert.m  or  RFD_<ORD>_cert.m  = {ann, ct1, gb, ct2}  and composes
   the TWO-step creative telescoping into single-certificate form

       M . F  =  Delta_k( Ck . F )  +  Delta_l( Cl . F ) ,

   exactly as certPy.wl does per tau, but with ONE object and therefore NO LCLM and
   NO right cofactors -- the whole point of not splitting.  With ORD = "lk" (ct1
   eliminates l, ct2 eliminates k):

       Cl = -(1/ff) Sum_i ccf_i ** ct1[[2,i]] ,   Ck = -RR ,
       {0, ff, ccf} = OreReduce[ M + (S[k]-1) ** RR , gb, Extended -> True ] .

   The operator products use verifycore.wl's hand-rolled Ore algebra, so the object
   handed to the verifier has never passed through RISC's ** .  RISC is used here
   only for OreReduce, which is a search step whose OUTPUT is checked downstream.

   Env: WHICH = D (direct, T*vtilde -- default) | E (E(vtilde)) ;  ORD (default lk).
   Out: RF<WHICH>_composed.m = {cf, Xope, Yope}.
   Run: WHICH=D math < certRFy.wl                                                  *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
$HistoryLength = 0;
WHICH = Environment["WHICH"]; If[WHICH === $Failed, WHICH = "D"];
ORD = Environment["ORD"]; If[ORD === $Failed, ORD = "lk"];
PRE = If[WHICH === "D", "RFD_", "RF_"];
lf = OpenWrite[DIR <> "certRFy_" <> WHICH <> ".log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], "  WHICH=", WHICH, " ORD=", ORD];
If[! FileExistsQ[DIR <> PRE <> ORD <> "_cert.m"],
   log["MISSING ", PRE, ORD, "_cert.m -- nothing to assemble."]; Close[lf]; Exit[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];
Get[DIR <> "verifycore.wl"];
vars3 = {S[n], S[k], S[l]};
{V1, V2} = If[ORD === "lk", {l, k}, {k, l}];
alg2 = OreAlgebra[S[n], S[V2]];
ordOf[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]];
   Max[Join[{0}, Cases[ap, FF[n + a_.] :> a, Infinity]]]];
coefsOf[c_] := Module[{ap, d}, ap = ApplyOreOperator[c, FF[n]]; d = ordOf[c];
   Table[Together[Coefficient[ap, FF[n + j]]], {j, 0, d}]];

{ann, ct1, gb, ct2} = Get[DIR <> PRE <> ORD <> "_cert.m"];
MT = ct2[[1, 1]]; RR = ct2[[2, 1]];
log["telescoper M : order ", ordOf[MT], "  LeafCount ", LeafCount[MT]];
If[gb =!= ct1[[1]],
   log["gb =!= ct1 telescopers -- a Groebner cofactor chain would be needed. ABORT."];
   Close[lf]; Exit[]];
pp = MT + ToOrePolynomial[S[V2] - 1, alg2] ** RR;
red = OreReduce[pp, gb, Extended -> True];
log["OreReduce remainder (must be 0): ", ToString[InputForm[red[[1]]]],
    "   ff = ", ToString[InputForm[red[[2]]]]];
If[red[[1]] =!= 0 && ! (Head[red[[1]]] === OrePolynomial && red[[1]][[1]] === {}),
   log["OreReduce remainder is NOT zero -- the composition is invalid. ABORT."];
   Close[lf]; Exit[]];
ff = red[[2]]; ccf = red[[3]];
c1o = opScal[-1/ff, Fold[opPlus, ope[vars3, {}],
   Table[opTimes[toOpe[ccf[[i]], vars3], toOpe[ct1[[2, i]], vars3]],
         {i, Length[ccf]}]]];
c2o = opScal[-1, toOpe[RR, vars3]];
Xope = If[ORD === "lk", c2o, c1o];   (* certifies Delta_k *)
Yope = If[ORD === "lk", c1o, c2o];   (* certifies Delta_l *)
log["Xope terms ", Length[Xope[[2]]], "   Yope terms ", Length[Yope[[2]]]];
cf = coefsOf[MT];
Put[{cf, Xope, Yope}, DIR <> "RF" <> WHICH <> "_composed.m"];
log["saved RF", WHICH, "_composed.m ; ord(M) = ", Length[cf] - 1];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
