(* z5ann5d.wl -- weight 5 annihilator with the rank-7 factor ELIMINATED ALGEBRAICALLY.

   Measured walls (z5ann5b_w5_lk.log, z5ann5c.log):
     Annihilator[alpha*Psi]                TIME ABORT 1200 s, ~0 GB
     DFiniteTimes[ann alpha, ann Psi]      TIME ABORT 1200 s, ~0 GB      (ranks 5 x 7)
     DFiniteTimes[ann alpha, ann alpha]    31 s, rank 15, 513 408 leaves (ranks 5 x 5)
     DFiniteTimes[ann alpha, ann Psi] in {S[k]} only   6 s (ranks 3 x 4)

   So: cost is driven by the PRODUCT OF THE TWO MODULE RANKS.  Psi = alpha/2 + beta gives
       alpha*Psi = alpha^2/2 + alpha*beta
   and both of those are rank 5 x rank 5.  No product in this script has a factor of rank > 5
   other than the final multiplication by T, whose annihilator has rank 1.

   Target check: UnderTheStaircase[ann w5] must be 64 -- the shift closure computed
   independently and RISC-free in Z5CF_CERT.md section 2.3.

   Run: MEMCAP=6000000000 PCAP=3600 math < z5ann5d.wl                                     *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/z5cf/";
$HistoryLength = 0;
getenv[v_, d_] := Module[{x = Environment[v]}, If[x === $Failed, d, ToExpression[x]]];
MEMCAP = getenv["MEMCAP", 6000000000];
PCAP = getenv["PCAP", 3600];
lf = OpenWrite[DIR <> "z5ann5d.log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], " MEMCAP=", MEMCAP, " PCAP=", PCAP];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded.  DFinite* available: ", ToString[Names["*DFinite*"]]];
TT = Binomial[n + k, n] Binomial[n, k]^2 Binomial[n + l, n] Binomial[n, l]^2 Binomial[n + k + l, n];
AA[r_, x_] := HarmonicNumber[n + x, r] - HarmonicNumber[x, r];
BB[r_, x_] := HarmonicNumber[n - x, r] - HarmonicNumber[x, r];
al = AA[1, k] - AA[1, l]; be = BB[1, k] - BB[1, l]; Psi = al/2 + be; S2 = AA[2, k] + AA[2, l];
w5 = HarmonicNumber[n + k, 5] + (1/2) (al - be) HarmonicNumber[n + k, 4] + (S2/4 - al Psi/2) HarmonicNumber[n + k, 3];
ref5 = {0, 87/4, 1190161/384, 7682021239/10368};
If[Table[Sum[(TT w5) /. {n -> nn, k -> kk, l -> ll}, {kk, 0, nn}, {ll, 0, nn}], {nn, 0, 3}] =!= ref5, log["SELF-TEST FAILED -- ABORT."]; Close[lf]; Exit[]];
log["self-test Sum T*w5 n=0..3 : True"];
V = {S[n], S[k], S[l]};
SetAttributes[stage, HoldRest];
stage[file_, name_, cap_, body_] := Module[{r, t0}, t0 = AbsoluteTime[];
  If[FileExistsQ[DIR <> file], r = Get[DIR <> file]; log["  ", name, " : loaded checkpoint  rank=", Length[UnderTheStaircase[r]], " leaf=", LeafCount[r]]; r,
    r = TimeConstrained[MemoryConstrained[body, MEMCAP], cap, $TimedOut];
    Which[r === $Aborted, log["  ", name, " : MEMORY ABORT after ", Round[AbsoluteTime[] - t0], "s ", DateString[]]; $Aborted,
      r === $TimedOut, log["  ", name, " : TIME ABORT after ", Round[AbsoluteTime[] - t0], "s maxmem=", Round[MaxMemoryUsed[]/10^9., 2], "GB ", DateString[]]; $Aborted,
      True, Put[r, DIR <> file]; log["  ", name, " #", Length[r], " rank=", Length[UnderTheStaircase[r]], " t=", Round[AbsoluteTime[] - t0], "s leaf=", LeafCount[r], " maxmem=", Round[MaxMemoryUsed[]/10^9., 2], "GB ", DateString[]]; r]]];
bail[x_, nm_] := If[x === $Aborted, log[nm, " DID NOT RETURN. ALL DONE ", DateString[]]; Close[lf]; Exit[], x];

aH5 = bail[stage["z5b_H5.m", "ann H5[n+k]", 300, Annihilator[HarmonicNumber[n + k, 5], V]], "H5"];
aH4 = bail[stage["z5b_H4.m", "ann H4[n+k]", 300, Annihilator[HarmonicNumber[n + k, 4], V]], "H4"];
aH3 = bail[stage["z5b_H3.m", "ann H3[n+k]", 300, Annihilator[HarmonicNumber[n + k, 3], V]], "H3"];
aAB = bail[stage["z5b_AB.m", "ann (alpha-beta)", 300, Annihilator[al - be, V]], "AB"];
aS2 = bail[stage["z5b_S2.m", "ann S2", 300, Annihilator[S2, V]], "S2"];
aAl = bail[stage["z5b_Al.m", "ann alpha", 300, Annihilator[al, V]], "Al"];
aBe = bail[stage["z5b_Be.m", "ann beta", 300, Annihilator[be, V]], "Be"];
(* --- the two rank-5 x rank-5 products that replace the rank-7 factor --- *)
aA2 = bail[stage["z5c_AlAl.m", "alpha^2", PCAP, DFiniteTimes[aAl, aAl]], "AlAl"];
aAB2 = bail[stage["z5c_AlBe.m", "alpha*beta", PCAP, DFiniteTimes[aAl, aBe]], "AlBe"];
aAP = bail[stage["z5d_AP.m", "alpha*Psi = DFinitePlus[alpha^2, alpha*beta]", PCAP, DFinitePlus[aA2, aAB2]], "AP"];
log["  CHECK: does aAP annihilate al*Psi ?  ", ToString[Union[Table[Simplify[ApplyOreOperator[g, al Psi]], {g, aAP}]] === {0}]];
(* --- assemble w5 --- *)
u2 = bail[stage["z5d_u2.m", "u2 = (al-be)*H4", PCAP, DFiniteTimes[aAB, aH4]], "u2"];
u3 = bail[stage["z5d_u3.m", "u3 = S2*H3", PCAP, DFiniteTimes[aS2, aH3]], "u3"];
u4 = bail[stage["z5d_u4.m", "u4 = al*Psi*H3", PCAP, DFiniteTimes[aAP, aH3]], "u4"];
s1 = bail[stage["z5d_s1.m", "s1 = H5 + u2", PCAP, DFinitePlus[aH5, u2]], "s1"];
s2 = bail[stage["z5d_s2.m", "s2 = s1 + u3", PCAP, DFinitePlus[s1, u3]], "s2"];
aw5 = bail[stage["z5d_w5.m", "ann w5 = s2 + u4", PCAP, DFinitePlus[s2, u4]], "w5"];
log["  ann[w5] rank = ", Length[UnderTheStaircase[aw5]], "   (independent RISC-free shift closure says 64)"];
log["  CHECK: does ann[w5] annihilate w5 ?  ", ToString[Union[Table[Simplify[ApplyOreOperator[g, w5]], {g, aw5}]] === {0}]];
annT = bail[stage["z5_w5_lk_annT.m", "ann T", 300, Annihilator[TT, V]], "annT"];
annS = bail[stage["z5_w5_lk_annS.m", "ann T*w5 = DFiniteTimes[annT, ann w5]", 2 PCAP, DFiniteTimes[annT, aw5]], "annS"];
log["  FINAL ann[T*w5]: ", Length[annS], " generators, rank ", Length[UnderTheStaircase[annS]], ", LeafCount ", LeafCount[annS]];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
