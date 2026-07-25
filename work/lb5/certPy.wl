(* certPy.wl -- ASSEMBLY for the tau-split route.

   Reads P_<tau>.m = {ann, ct1, gb, ct2} for each tau that certP.wl completed, and

     1  composes each two-step certificate into single-certificate form
            M_tau . F_tau = Delta_k( Ck_tau . F_tau ) + Delta_l( Cl_tau . F_tau ) ,
        which for ORD = "kl" (ct1 eliminates k, ct2 eliminates l) reads
            Ck_tau = -(1/ff) Sum_i ccf_i ** ct1[[2,i]] ,   Cl_tau = -RR ,
            {0, ff, ccf} = OreReduce[M_tau + (S[l]-1)**RR, gb_tau, Extended->True] ;
     2  M = LCLM over the taus, with right cofactors P_tau ** M_tau == M ;
     3  Xhat_tau = P_tau ** Ck_tau , Yhat_tau = P_tau ** Cl_tau , so that
            M . E(v) = Delta_k( Sum_tau Xhat_tau . F_tau )
                     + Delta_l( Sum_tau Yhat_tau . F_tau )
        because Sum_tau F_tau = E(v) and P_tau in Q(n)[S_n] commutes with Delta_k,l.

   The operator products are done with verifycore.wl's own hand-rolled Ore algebra,
   so the object handed to the verifier has not passed through RISC's ** .
   RISC is used here only for OreReduce and LCLM (search steps).

   Output  P_cert.m = {cf, {{tau, XopeTau, YopeTau}, ...}}   for certPv.wl.
   Run:  math < certPy.wl                                                          *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
$HistoryLength = 0;
(* ORD must match the run that produced the P_<tau>.m files -- the sign convention
   of the composition depends on it.  Auto-detected from the ct1 checkpoint names. *)
ORD = Environment["ORD"];
If[ORD === $Failed,
   ORD = If[FileNames["P_*_lk_ct1.m", DIR] =!= {}, "lk", "kl"]];
lf = OpenWrite[DIR <> "certPy.log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], "  ORD=", ORD];
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

alltau = {"n1", "n2", "n3", "kk", "ll"};
have = Select[alltau, FileExistsQ[DIR <> "P_" <> # <> ".m"] &];
log["taus with a saved P_ file: ", ToString[have]];
If[Length[have] < 5,
   log["INCOMPLETE: need all five taus before the sum Sum_tau F_tau = E(v) is usable."];
   log["missing: ", ToString[Complement[alltau, have]]]];

Ms = {}; CkA = {}; ClA = {};
Do[Module[{ann, ct1, gb, ct2, MT, RR, pp, red, ff, ccf},
   {ann, ct1, gb, ct2} = Get[DIR <> "P_" <> tau <> ".m"];
   MT = ct2[[1, 1]]; RR = ct2[[2, 1]];
   log["=== ", tau, " : telescoper order ", ordOf[MT], "  LeafCount ", LeafCount[MT]];
   If[gb =!= ct1[[1]],
      log[tau, " : gb =!= ct1 telescopers -- Groebner cofactor chain needed, ABORT"];
      Close[lf]; Exit[]];
   pp = MT + ToOrePolynomial[S[V2] - 1, alg2] ** RR;
   red = OreReduce[pp, gb, Extended -> True];
   log["  ", tau, " OreReduce remainder ", ToString[InputForm[red[[1]]]],
       "  ff=", ToString[InputForm[red[[2]]]]];
   ff = red[[2]]; ccf = red[[3]];
   AppendTo[Ms, {tau, MT}];
   (* c1o certifies Delta_{V1} (it comes from the ct1 cofactor chain),
      c2o certifies Delta_{V2} (it is -RR, from ct2).  For ORD = "kl",
      V1 = k and V2 = l; for ORD = "lk" the two are exchanged.            *)
   c1o = opScal[-1/ff, Fold[opPlus, ope[vars3, {}],
      Table[opTimes[toOpe[ccf[[i]], vars3], toOpe[ct1[[2, i]], vars3]],
            {i, Length[ccf]}]]];
   c2o = opScal[-1, toOpe[RR, vars3]];
   AppendTo[CkA, {tau, If[ORD === "lk", c2o, c1o]}];
   AppendTo[ClA, {tau, If[ORD === "lk", c1o, c2o]}]],
 {tau, have}];

(* ---- LCLM ---- *)
MM = Ms[[1, 2]];
Do[Module[{t0 = AbsoluteTime[]},
   MM = LCLM[MM, Ms[[i, 2]]];
   log["LCLM after ", Ms[[i, 1]], " : order ", ordOf[MM], "  LeafCount ", LeafCount[MM],
       "  t=", Round[AbsoluteTime[] - t0], "s"]],
 {i, 2, Length[Ms]}];
DD = ordOf[MM];
log["*** M = LCLM over ", Length[Ms], " taus : order ", DD, " ***"];
Put[MM, DIR <> "P_M.m"];

(* ---- right cofactors and the two total certificates ---- *)
XY = {};
Do[Module[{red, PT, PTo},
   red = OreReduce[MM, {Ms[[i, 2]]}, Extended -> True];
   log["cofactor ", Ms[[i, 1]], " : remainder ", ToString[InputForm[red[[1]]]],
       "  ff=", ToString[InputForm[red[[2]]]], "  order ", ordOf[red[[3, 1]]]];
   PT = red[[3, 1]];
   PTo = opScal[1/red[[2]], toOpe[PT, vars3]];
   AppendTo[XY, {Ms[[i, 1]],
      opTimes[PTo, CkA[[i, 2]]], opTimes[PTo, ClA[[i, 2]]]}];
   log["  Xhat/Yhat ", Ms[[i, 1]], " terms ", Length[XY[[-1, 2, 2]]], " / ",
       Length[XY[[-1, 3, 2]]]]],
 {i, Length[Ms]}];

cf = coefsOf[MM];
Put[{cf, XY}, DIR <> "P_cert.m"];
log["saved P_cert.m ; ord(M) = ", DD, " ; ord(L'') = ord(M)+3 = ", DD + 3];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
