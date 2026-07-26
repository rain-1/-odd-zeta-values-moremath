(* z5ct.wl -- SINGLE-SHOT creative telescoping in BOTH summation variables at once:
       CreativeTelescoping[ann, {S[k]-1, S[l]-1}, {S[n]}, Support -> {1,S[n],S[n]^2,S[n]^3}]
   This returns the telescoper L in n alone together with the pair (rho, sigma) directly,
   so no OreGroebnerBasis / OreReduce cofactor assembly is needed.  The support is bounded
   to the KNOWN, OCCUPIED L_BZ box (order 3) rather than laddered blindly.

   Reads the checkpointed annihilator z5_<TAG>_annS.m (or _annD.m).
   Env: TAG, MEMCAP, CTCAP, DMAX, SUPP (box|ladder)
   Run: TAG=w3_lk MEMCAP=4000000000 math < z5ct.wl                                    *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/z5cf/";
$HistoryLength = 0;
getenv[v_, d_] := Module[{x = Environment[v]}, If[x === $Failed, d, ToExpression[x]]];
gets[v_, d_] := Module[{x = Environment[v]}, If[x === $Failed, d, x]];
TAG = gets["TAG", "w3_lk"];
MEMCAP = getenv["MEMCAP", 3000000000];
CTCAP = getenv["CTCAP", 5400];
DMAX = getenv["DMAX", 5];
lf = OpenWrite[DIR <> "z5ct_" <> TAG <> ".log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], " TAG=", TAG, " MEMCAP=", MEMCAP, " CTCAP=", CTCAP, " DMAX=", DMAX];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

annfile = If[FileExistsQ[DIR <> "z5_" <> TAG <> "_annS.m"], "z5_" <> TAG <> "_annS.m", "z5_" <> TAG <> "_annD.m"];
ann = Get[DIR <> annfile];
log["ann loaded from ", annfile, " : ", Length[ann], " generators, LeafCount ", LeafCount[ann], ", rank ", Length[UnderTheStaircase[ann]]];

a0f[x_] := 41218 x^3 + 198849 x^2 + 320790 x + 173057;
B8f[x_] := 3874492 x^8 + 59373972 x^7 + 394148190 x^6 + 1481084196 x^5 + 3447878810 x^4 + 5095855458 x^3 + 4673546679 x^2 + 2433871008 x + 551502039;
B9f[x_] := 48802112 x^9 + 967468896 x^8 + 8488000862 x^7 + 43246197636 x^6 + 140983768422 x^5 + 304912330849 x^4 + 437406946975 x^3 + 401272692378 x^2 + 213593890911 x + 50257929339;
cc3 = {(n + 1)^5 (n + 2) a0f[n + 1], -2 (n + 2) B8f[n], -2 B9f[n], 2 (n + 3)^5 (2 n + 5) a0f[n]};
ordOf[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]]; Max[Join[{0}, Cases[ap, FF[n + a_.] :> a, Infinity]]]];

(* the telescoper is KNOWN to have order exactly 3 (L_BZ), so try d = 3 FIRST and only
   then widen; d = 0,1,2 are provably empty and are tried last, cheaply, for the record *)
DSTART = getenv["DSTART", 3];
ladder = DeleteDuplicates[Join[Range[DSTART, DMAX], Range[0, DSTART - 1]]];
log["ct ladder order: ", ToString[ladder]];
got = $Failed;
Do[If[got =!= $Failed, Continue[]];
  supp = Table[S[n]^i, {i, 0, d}]; t0 = AbsoluteTime[];
  r = Quiet[Check[TimeConstrained[MemoryConstrained[CreativeTelescoping[ann, {S[k] - 1, S[l] - 1}, {S[n]}, Support -> supp], MEMCAP], CTCAP, $TimedOut], $Failed]];
  log["  2-delta CT d=", d, " t=", Round[AbsoluteTime[] - t0], "s -> ", Which[r === $TimedOut, "TIME ABORT", r === $Aborted, "MEMORY ABORT", r === $Failed, "error", Head[r] === List && Length[r] >= 1 && Length[r[[1]]] >= 1, "FOUND order " <> ToString[ordOf[r[[1, 1]]]], True, "none"], "  maxmem=", Round[MaxMemoryUsed[]/10^9., 2], "GB  ", DateString[]];
  If[Head[r] === List && Length[r] >= 1 && Length[r[[1]]] >= 1, got = r],
 {d, ladder}];

If[got =!= $Failed,
  Put[got, DIR <> "z5_" <> TAG <> "_ct2d.m"];
  log["  SAVED z5_", TAG, "_ct2d.m  ntel=", Length[got[[1]]], "  ndelta=", Length[got] - 1];
  log["  telescoper order ", ordOf[got[[1, 1]]], "  LeafCount ", LeafCount[got[[1, 1]]]];
  Module[{cf, rat}, cf = Table[Coefficient[ApplyOreOperator[got[[1, 1]], FF[n]], FF[n + j]], {j, 0, ordOf[got[[1, 1]]]}]; rat = If[Length[cf] === 4, Together[cf/cc3], "order is not 3"]; log["  telescoper / L_BZ coefficientwise (must be 4 equal entries): ", ToString[InputForm[rat]]]];
  log["  certificate LeafCounts: ", ToString[Table[LeafCount[got[[i]]], {i, 2, Length[got]}]]],
  log["  NO 2-delta telescoper up to d=", DMAX, "."]];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
