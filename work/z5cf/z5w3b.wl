(* z5w3b.wl -- second attempt at the weight-3 elimination.
   Diagnosis from the first attempt: ct1 (eliminate l) TIME-ABORTED at 5402 s with a peak
   of only 2 GB, i.e. it is CLOCK-bound, not memory-bound; and the annihilator handed to it
   has LeafCount 5 596 298 for rank 15.  PHASE2_CERTS section 18.18's lesson is that the
   decisive quantity is the SIZE of the basis handed to the next stage, so:

     B0  reduce the annihilator first: OreGroebnerBasis over the full 3-variable algebra
     B1  probe the multi-delta CreativeTelescoping signature with messages VISIBLE
     B2  ct1 on the reduced basis, elimination order from ORD, with a large clock

   Env: ORD (kl|lk), MEMCAP, GBCAP, CT1CAP
   Run: ORD=kl MEMCAP=5000000000 CT1CAP=14400 math < z5w3b.wl                            *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/z5cf/";
$HistoryLength = 0;
getenv[v_, d_] := Module[{x = Environment[v]}, If[x === $Failed, d, ToExpression[x]]];
gets[v_, d_] := Module[{x = Environment[v]}, If[x === $Failed, d, x]];
ORD = gets["ORD", "kl"];
MEMCAP = getenv["MEMCAP", 5000000000];
GBCAP = getenv["GBCAP", 2400];
CT1CAP = getenv["CT1CAP", 14400];
lf = OpenWrite[DIR <> "z5w3b_" <> ORD <> ".log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], " ORD=", ORD, " MEMCAP=", MEMCAP, " GBCAP=", GBCAP, " CT1CAP=", CT1CAP];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];
ann = Get[DIR <> "z5_w3_lk_annS.m"];
log["ann: ", Length[ann], " generators, LeafCount ", LeafCount[ann], ", rank ", Length[UnderTheStaircase[ann]]];

SetAttributes[stage, HoldRest];
stage[file_, name_, cap_, body_] := Module[{r, t0}, t0 = AbsoluteTime[];
  If[FileExistsQ[DIR <> file], r = Get[DIR <> file]; log["  ", name, " : loaded checkpoint"]; r,
    r = TimeConstrained[MemoryConstrained[body, MEMCAP], cap, $TimedOut];
    Which[r === $Aborted, log["  ", name, " : MEMORY ABORT after ", Round[AbsoluteTime[] - t0], "s maxmem=", Round[MaxMemoryUsed[]/10^9., 2], "GB ", DateString[]]; $Aborted,
      r === $TimedOut, log["  ", name, " : TIME ABORT after ", Round[AbsoluteTime[] - t0], "s maxmem=", Round[MaxMemoryUsed[]/10^9., 2], "GB ", DateString[]]; $Aborted,
      True, Put[r, DIR <> file]; log["  ", name, " OK t=", Round[AbsoluteTime[] - t0], "s LeafCount ", LeafCount[r], " maxmem=", Round[MaxMemoryUsed[]/10^9., 2], "GB ", DateString[]]; r]]];

(* --- B0: reduce the annihilator --- *)
log["=== B0 OreGroebnerBasis over the full 3-variable algebra === ", DateString[]];
gb3 = stage["z5_w3_gb3.m", "B0 gb3", GBCAP, OreGroebnerBasis[ann, OreAlgebra[S[n], S[k], S[l]]]];
base = If[gb3 === $Aborted, ann, gb3];
If[gb3 =!= $Aborted, log["  reduction factor on LeafCount: ", N[LeafCount[ann]/Max[1, LeafCount[gb3]], 4], "x   #gens ", Length[gb3], "  rank ", Length[UnderTheStaircase[gb3]]]];

(* --- B1: probe the multi-delta signature, messages VISIBLE --- *)
log["=== B1 multi-delta CreativeTelescoping signature probe === ", DateString[]];
pr = TimeConstrained[Check[CreativeTelescoping[base, {S[k] - 1, S[l] - 1}, {S[n]}, Support -> Table[S[n]^i, {i, 0, 3}]], "CHECK-FAILED"], 240, "TIMEOUT"];
log["  probe result head: ", ToString[Head[pr]], "  -> ", ToString[Short[pr, 4]]];
If[Head[pr] === List && Length[pr] >= 1 && Length[pr[[1]]] >= 1, Put[pr, DIR <> "z5_w3_lk_ct2d.m"]; log["  MULTI-DELTA CT SUCCEEDED -- saved z5_w3_lk_ct2d.m"]];

(* --- B2: ct1 with the chosen elimination order and a large clock --- *)
{V1, V2} = If[ORD === "lk", {l, k}, {k, l}];
log["=== B2 ct1 (eliminate ", ToString[V1], ") on the reduced basis === ", DateString[]];
ct1 = stage["z5_w3_" <> ORD <> "_ct1b.m", "B2 ct1", CT1CAP, CreativeTelescoping[base, S[V1] - 1, {S[n], S[V2]}]];
If[ct1 === $Aborted, log["B2 DID NOT RETURN. ALL DONE ", DateString[]]; Close[lf]; Exit[]];
log["  ct1 telescopers: ", Length[ct1[[1]]], "  LeafCount ", LeafCount[ct1[[1]]], "  certs LeafCount ", LeafCount[ct1[[2]]]];
log["=== B3 OreGroebnerBasis in (n,", ToString[V2], ") === ", DateString[]];
gb = stage["z5_w3_" <> ORD <> "_gbb.m", "B3 gb", GBCAP, OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n], S[V2]]]];
If[gb =!= $Aborted, log["  gb === ct1tel ? ", ToString[gb === ct1[[1]]]]];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
