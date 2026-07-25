(* certY.wl -- harvest the six rank-1 telescopers produced by certU.wl, take the
   LCLM, and report order/degree data plus the right-factor relation to L_BZ.

   Reads  U_<lab>.m = {ann, ct1, gb, ct2}  for every label that has completed;
   the telescoper of label lab is  ct2[[1,1]]  (an OrePolynomial in S[n]).

   Outputs
     U_Mlist.m  = {{lab, Mlab}, ...}
     U_M.m      = the LCLM
     U_cof.m    = {{lab, P_lab}, ...} with  P_lab ** M_lab == LCLM   (right cofactors)
   and logs order, degree, and whether L_BZ is a right factor of the LCLM.

   Run:  math < certY.wl   (a standalone kernel; needs RISC).                     *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf = OpenWrite[DIR <> "certY.log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

algn = OreAlgebra[S[n]];

ordOf[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]];
   Max[Join[{0}, Cases[ap, FF[n + a_.] :> a, Infinity]]]];
coefsOf[c_] := Module[{ap, d}, ap = ApplyOreOperator[c, FF[n]]; d = ordOf[c];
   Table[Together[Coefficient[ap, FF[n + j]]], {j, 0, d}]];
degOf[c_] := Max[Join[{0}, Exponent[Numerator[Together[#]], n] & /@ coefsOf[c]]];

(* Only three of the six letters give distinct problems: PHASE2_CERTS section 11 proves
   gamma = 3 alpha, delta = (3/2) alpha, eps = (1/2) alpha exactly, so
   M_gamma = M_delta = M_eps = M_alpha and including them in the LCLM is a no-op.
   Set LABSY in the environment to override.                                        *)
labs = Environment["LABSY"];
labs = If[labs === $Failed, {"alpha", "beta", "c0"}, StringSplit[labs, ","]];
have = Select[labs, FileExistsQ[DIR <> "U_" <> # <> ".m"] &];
log["labels with a saved U_ file: ", ToString[have]];

Ms = {};
Do[Module[{u, M},
   u = Get[DIR <> "U_" <> lb <> ".m"];
   If[Length[u] < 4 || Length[u[[4]]] < 1 || Length[u[[4, 1]]] < 1,
     log[lb, " : U_ file has no ct2 telescoper, skipped"],
     M = u[[4, 1, 1]];
     log[lb, " : telescoper order ", ordOf[M], "  degree ", degOf[M],
         "  LeafCount ", LeafCount[M]];
     AppendTo[Ms, {lb, M}]]],
 {lb, have}];
Put[Ms, DIR <> "U_Mlist.m"];
log["harvested ", Length[Ms], " telescopers"];

(* pairwise identity check: do any two letters share the same telescoper? *)
Do[If[i < j && Ms[[i, 2]] === Ms[[j, 2]],
   log["  NOTE ", Ms[[i, 1]], " and ", Ms[[j, 1]], " have IDENTICAL telescopers"]],
 {i, Length[Ms]}, {j, Length[Ms]}];

(* ---- iterated LCLM ---- *)
If[Length[Ms] >= 2,
 Module[{MM, t0},
  MM = Ms[[1, 2]];
  Do[t0 = AbsoluteTime[];
     MM = LCLM[MM, Ms[[i, 2]]];
     log["LCLM after ", Ms[[i, 1]], " : order ", ordOf[MM], "  degree ", degOf[MM],
         "  LeafCount ", LeafCount[MM], "  t=", Round[AbsoluteTime[] - t0], "s"],
   {i, 2, Length[Ms]}];
  Put[MM, DIR <> "U_M.m"];
  log["*** LCLM: order ", ordOf[MM], " degree ", degOf[MM], " ***"];

  (* right cofactors  P_lab ** M_lab == MM *)
  Module[{cof = {}},
   Do[Module[{red},
      red = OreReduce[MM, {Ms[[i, 2]]}, Extended -> True];
      log["  cofactor ", Ms[[i, 1]], " : remainder ", ToString[Short[red[[1]], 1]],
          "  ff=", ToString[InputForm[red[[2]]]]];
      AppendTo[cof, {Ms[[i, 1]], red}]],
    {i, Length[Ms]}];
   Put[cof, DIR <> "U_cof.m"]];

  (* is L_BZ a right factor of the LCLM? *)
  Module[{a0f, B8f, B9f, LBZ, red},
   a0f[x_] := 41218 x^3 + 198849 x^2 + 320790 x + 173057;
   B8f[x_] := 3874492 x^8 + 59373972 x^7 + 394148190 x^6 + 1481084196 x^5 +
      3447878810 x^4 + 5095855458 x^3 + 4673546679 x^2 + 2433871008 x + 551502039;
   B9f[x_] := 48802112 x^9 + 967468896 x^8 + 8488000862 x^7 + 43246197636 x^6 +
      140983768422 x^5 + 304912330849 x^4 + 437406946975 x^3 + 401272692378 x^2 +
      213593890911 x + 50257929339;
   LBZ = ToOrePolynomial[(n + 1)^5 (n + 2) a0f[n + 1] + (-2 (n + 2) B8f[n]) S[n] +
      (-2 B9f[n]) S[n]^2 + (2 (n + 3)^5 (2 n + 5) a0f[n]) S[n]^3, algn];
   log["L_BZ: order ", ordOf[LBZ], " degree ", degOf[LBZ]];
   red = OreReduce[MM, {LBZ}, Extended -> True];
   log["*** L_BZ right factor of LCLM?  remainder = ",
       ToString[InputForm[red[[1]]]], " ***"];
   Put[{LBZ, red}, DIR <> "U_LBZred.m"]]]];

log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
