(* z5ann5b.wl -- weight 5 by an EXPLICIT closure chain instead of one Annihilator call.
   Rationale (PHASE2_CERTS section 18.2 / 19): the cost driver is the number of distinct
   harmonic symbols AND the coefficient size.  Annihilator[T*w5] sees 13 symbols at once;
   the chain below never sees more than 6 at a time, and every intermediate has small
   coefficients because T is multiplied in LAST.

     u1 = H5[n+k]                       (rank 2)
     u2 = (alpha-beta) H4[n+k]
     u3 = S2 H3[n+k]
     u4 = alpha Psi H3[n+k]
     w5 = u1 + u2/2 + u3/4 - u4/2       via DFinitePlus
     T*w5                               via DFiniteTimes with Annihilator[T]

   Env: MEMCAP, PCAP (per-piece cap), TAG
   Run: TAG=w5_lk MEMCAP=3000000000 math < z5ann5b.wl                                *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/z5cf/";
$HistoryLength = 0;
getenv[v_, d_] := Module[{x = Environment[v]}, If[x === $Failed, d, ToExpression[x]]];
gets[v_, d_] := Module[{x = Environment[v]}, If[x === $Failed, d, x]];
TAG = gets["TAG", "w5_lk"];
MEMCAP = getenv["MEMCAP", 3000000000];
PCAP = getenv["PCAP", 1200];
lf = OpenWrite[DIR <> "z5ann5b_" <> TAG <> ".log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], " TAG=", TAG, " MEMCAP=", MEMCAP, " PCAP=", PCAP];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded.  closure-property symbols available: ", ToString[Names["*DFinite*"]]];

TT = Binomial[n + k, n] Binomial[n, k]^2 Binomial[n + l, n] Binomial[n, l]^2 Binomial[n + k + l, n];
AA[r_, x_] := HarmonicNumber[n + x, r] - HarmonicNumber[x, r];
BB[r_, x_] := HarmonicNumber[n - x, r] - HarmonicNumber[x, r];
al = AA[1, k] - AA[1, l]; be = BB[1, k] - BB[1, l]; Psi = al/2 + be; S2 = AA[2, k] + AA[2, l];
w5 = HarmonicNumber[n + k, 5] + (1/2) (al - be) HarmonicNumber[n + k, 4] + (S2/4 - al Psi/2) HarmonicNumber[n + k, 3];
ref5 = {0, 87/4, 1190161/384, 7682021239/10368};
chk = Table[Sum[(TT w5) /. {n -> nn, k -> kk, l -> ll}, {kk, 0, nn}, {ll, 0, nn}], {nn, 0, 3}];
log["self-test Sum T*w5 n=0..3 : ", ToString[chk === ref5]];
If[chk =!= ref5, log["SELF-TEST FAILED -- ABORT."]; Close[lf]; Exit[]];

SetAttributes[stage, HoldRest];
stage[file_, name_, cap_, body_] := Module[{r, t0}, t0 = AbsoluteTime[];
  If[FileExistsQ[DIR <> file], r = Get[DIR <> file]; log["  ", name, " : loaded checkpoint (", Length[r], " gens)"]; r,
    r = TimeConstrained[MemoryConstrained[body, MEMCAP], cap, $TimedOut];
    Which[r === $Aborted, log["  ", name, " : MEMORY ABORT after ", Round[AbsoluteTime[] - t0], "s maxmem=", Round[MaxMemoryUsed[]/10^9., 2], "GB ", DateString[]]; $Aborted,
      r === $TimedOut, log["  ", name, " : TIME ABORT after ", Round[AbsoluteTime[] - t0], "s maxmem=", Round[MaxMemoryUsed[]/10^9., 2], "GB ", DateString[]]; $Aborted,
      True, Put[r, DIR <> file]; log["  ", name, " #", Length[r], " rank=", Length[UnderTheStaircase[r]], " t=", Round[AbsoluteTime[] - t0], "s leaf=", LeafCount[r], " maxmem=", Round[MaxMemoryUsed[]/10^9., 2], "GB ", DateString[]]; r]]];
bail[x_, nm_] := If[x === $Aborted, log[nm, " DID NOT RETURN. ALL DONE ", DateString[]]; Close[lf]; Exit[], x];

V = {S[n], S[k], S[l]};
aH5 = bail[stage["z5b_H5.m", "ann H5[n+k]", PCAP, Annihilator[HarmonicNumber[n + k, 5], V]], "H5"];
aH4 = bail[stage["z5b_H4.m", "ann H4[n+k]", PCAP, Annihilator[HarmonicNumber[n + k, 4], V]], "H4"];
aH3 = bail[stage["z5b_H3.m", "ann H3[n+k]", PCAP, Annihilator[HarmonicNumber[n + k, 3], V]], "H3"];
aAB = bail[stage["z5b_AB.m", "ann (alpha-beta)", PCAP, Annihilator[al - be, V]], "AB"];
aS2 = bail[stage["z5b_S2.m", "ann S2", PCAP, Annihilator[S2, V]], "S2"];
(* v2: NEVER let Annihilator see a product.  Annihilator[al*Psi] TIME-ABORTED at 1200 s
   with essentially zero memory (10:16:07); the same object built as
   DFiniteTimes[ann al, ann Psi] costs the two factors (0 s each) plus one closure step. *)
aAl = bail[stage["z5b_Al.m", "ann alpha", PCAP, Annihilator[al, V]], "Al"];
aPs = bail[stage["z5b_Ps.m", "ann Psi", PCAP, Annihilator[Psi, V]], "Ps"];
aAP = bail[stage["z5b_AP2.m", "aAP = DFiniteTimes[alpha, Psi]", PCAP, DFiniteTimes[aAl, aPs]], "AP"];
u2 = bail[stage["z5b_u2.m", "u2 = (al-be)*H4", PCAP, DFiniteTimes[aAB, aH4]], "u2"];
u3 = bail[stage["z5b_u3.m", "u3 = S2*H3", PCAP, DFiniteTimes[aS2, aH3]], "u3"];
u4 = bail[stage["z5b_u4.m", "u4 = al*Psi*H3", PCAP, DFiniteTimes[aAP, aH3]], "u4"];
s1 = bail[stage["z5b_s1.m", "s1 = u1 + u2", PCAP, DFinitePlus[aH5, u2]], "s1"];
s2 = bail[stage["z5b_s2.m", "s2 = s1 + u3", PCAP, DFinitePlus[s1, u3]], "s2"];
aw5 = bail[stage["z5b_w5.m", "ann w5 = s2 + u4", PCAP, DFinitePlus[s2, u4]], "w5"];
log["  ann[w5] rank = ", Length[UnderTheStaircase[aw5]], "   (must be 64)"];
annT = bail[stage["z5_" <> TAG <> "_annT.m", "ann T", 600, Annihilator[TT, V]], "annT"];
annS = bail[stage["z5_" <> TAG <> "_annS.m", "ann T*w5", 2 PCAP, DFiniteTimes[annT, aw5]], "annS"];
log["  FINAL ann[T*w5]: ", Length[annS], " generators, rank ", Length[UnderTheStaircase[annS]], ", LeafCount ", LeafCount[annS]];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
