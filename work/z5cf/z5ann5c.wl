(* z5ann5c.wl -- BISECT the weight-5 wall.
   Measured so far: Annihilator[alpha*Psi] TIME ABORT 1200 s / ~0 GB, and
   DFiniteTimes[ann alpha, ann Psi] TIME ABORT 1200 s / ~0 GB.  So the wall is the
   product of two LETTER-BEARING modules, in either implementation -- whereas
   DFiniteTimes[ann T, ann w3hat] (rank 1 x rank 15) cost 30 s.  This script finds
   the smallest product that stalls, then gives the real target a long clock.
   Run: MEMCAP=4000000000 math < z5ann5c.wl                                        *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/z5cf/";
$HistoryLength = 0;
getenv[v_, d_] := Module[{x = Environment[v]}, If[x === $Failed, d, ToExpression[x]]];
MEMCAP = getenv["MEMCAP", 4000000000];
SMALLCAP = getenv["SMALLCAP", 900];
BIGCAP = getenv["BIGCAP", 7200];
lf = OpenWrite[DIR <> "z5ann5c.log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], " MEMCAP=", MEMCAP, " SMALLCAP=", SMALLCAP, " BIGCAP=", BIGCAP];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];
AA[r_, x_] := HarmonicNumber[n + x, r] - HarmonicNumber[x, r];
BB[r_, x_] := HarmonicNumber[n - x, r] - HarmonicNumber[x, r];
al = AA[1, k] - AA[1, l]; be = BB[1, k] - BB[1, l]; Psi = al/2 + be;
V = {S[n], S[k], S[l]};
SetAttributes[stage, HoldRest];
stage[file_, name_, cap_, body_] := Module[{r, t0}, t0 = AbsoluteTime[];
  If[FileExistsQ[DIR <> file], r = Get[DIR <> file]; log["  ", name, " : loaded checkpoint"]; r,
    r = TimeConstrained[MemoryConstrained[body, MEMCAP], cap, $TimedOut];
    Which[r === $Aborted, log["  ", name, " : MEMORY ABORT after ", Round[AbsoluteTime[] - t0], "s"]; $Aborted,
      r === $TimedOut, log["  ", name, " : TIME ABORT after ", Round[AbsoluteTime[] - t0], "s maxmem=", Round[MaxMemoryUsed[]/10^9., 2], "GB ", DateString[]]; $Aborted,
      True, Put[r, DIR <> file]; log["  ", name, " #", Length[r], " rank=", Length[UnderTheStaircase[r]], " t=", Round[AbsoluteTime[] - t0], "s leaf=", LeafCount[r], " maxmem=", Round[MaxMemoryUsed[]/10^9., 2], "GB ", DateString[]]; r]]];

aAl = stage["z5b_Al.m", "ann alpha", 300, Annihilator[al, V]];
aBe = stage["z5b_Be.m", "ann beta", 300, Annihilator[be, V]];
aPs = stage["z5b_Ps.m", "ann Psi", 300, Annihilator[Psi, V]];
(* one-variable probes: how much of the cost is the number of shift generators? *)
log["=== 1-var probes: is the cost the 3-variable Ore algebra? === ", DateString[]];
aAl1 = stage["z5c_Al_k.m", "ann alpha, {S[k]} only", 300, Annihilator[al, {S[k]}]];
aPs1 = stage["z5c_Ps_k.m", "ann Psi, {S[k]} only", 300, Annihilator[Psi, {S[k]}]];
If[aAl1 =!= $Aborted && aPs1 =!= $Aborted, stage["z5c_AP_k.m", "DFiniteTimes[alpha,Psi] in {S[k]} only", SMALLCAP, DFiniteTimes[aAl1, aPs1]]];
log["=== bisection: smallest stalling product === ", DateString[]];
stage["z5c_AlAl.m", "alpha^2  = DFiniteTimes[alpha,alpha]", SMALLCAP, DFiniteTimes[aAl, aAl]];
stage["z5c_AlBe.m", "alpha*beta = DFiniteTimes[alpha,beta]", SMALLCAP, DFiniteTimes[aAl, aBe]];
log["=== the real target, long clock === ", DateString[]];
stage["z5b_AP2.m", "alpha*Psi = DFiniteTimes[alpha,Psi]", BIGCAP, DFiniteTimes[aAl, aPs]];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
