(* z5ann.wl -- Annihilator / creative telescoping for the NEW compact weights.
   Objects (work/ZETA5_CLOSEDFORM.md):
     alpha = A1(k)-A1(l), beta = B1(k)-B1(l), Psi = alpha/2 + beta, S2 = A2(k)+A2(l)
     w3hat = H3[n+k] - Psi H2[n+k]                                 (8 distinct symbols, closure 15)
     w5    = H5[n+k] + (alpha-beta)/2 H4[n+k] + (S2/4 - alpha Psi/2) H3[n+k]   (13 symbols, closure 64)
   Env: WT (3|5), ORD (lk|kl), MEMCAP, SPLITCAP, ANNCAP, CT1CAP, LADDERCAP, DMAX, DIRECT (0|1), TAG
   Run: WT=3 MEMCAP=3000000000 math < z5ann.wl                                                    *)

DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/z5cf/";
$HistoryLength = 0;
getenv[v_, d_] := Module[{x = Environment[v]}, If[x === $Failed, d, ToExpression[x]]];
gets[v_, d_] := Module[{x = Environment[v]}, If[x === $Failed, d, x]];
WT = getenv["WT", 3];
ORD = gets["ORD", "lk"];
TAG = gets["TAG", "w" <> ToString[WT] <> "_" <> ORD];
MEMCAP = getenv["MEMCAP", 3000000000];
SPLITCAP = getenv["SPLITCAP", 1800];
ANNCAP = getenv["ANNCAP", 7200];
CT1CAP = getenv["CT1CAP", 5400];
LADDERCAP = getenv["LADDERCAP", 3600];
DMAX = getenv["DMAX", 6];
DIRECT = getenv["DIRECT", 1];
lf = OpenWrite[DIR <> "z5ann_" <> TAG <> ".log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], " WT=", WT, " ORD=", ORD, " TAG=", TAG, " MEMCAP=", MEMCAP, " SPLITCAP=", SPLITCAP, " ANNCAP=", ANNCAP, " CT1CAP=", CT1CAP, " DIRECT=", DIRECT];

Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded ", DateString[]];

TT = Binomial[n + k, n] Binomial[n, k]^2 Binomial[n + l, n] Binomial[n, l]^2 Binomial[n + k + l, n];
AA[r_, x_] := HarmonicNumber[n + x, r] - HarmonicNumber[x, r];
BB[r_, x_] := HarmonicNumber[n - x, r] - HarmonicNumber[x, r];
al = AA[1, k] - AA[1, l];
be = BB[1, k] - BB[1, l];
Psi = al/2 + be;
S2 = AA[2, k] + AA[2, l];
w3h = HarmonicNumber[n + k, 3] - Psi HarmonicNumber[n + k, 2];
w5 = HarmonicNumber[n + k, 5] + (1/2) (al - be) HarmonicNumber[n + k, 4] + (S2/4 - al Psi/2) HarmonicNumber[n + k, 3];
ww = If[WT === 3, w3h, w5];
nSym = Length[Union[Cases[ww, HarmonicNumber[__], Infinity]]];
nInst = Length[Cases[ww, HarmonicNumber[__], Infinity]];
log["weight ", WT, ": HarmonicNumber instances ", nInst, "   DISTINCT symbols ", nSym, "  (must be ", If[WT === 3, 8, 13], ")"];
If[nSym =!= If[WT === 3, 8, 13], log["SYMBOL COUNT WRONG -- ABORT."]; Close[lf]; Exit[]];
log["  symbols: ", ToString[InputForm[Union[Cases[ww, HarmonicNumber[__], Infinity]]]]];

(* --- non-circular numeric self-test against the exact ladder values --- *)
ref3 = {0, 101/4, 344923/96, 3710571371/4320};
ref5 = {0, 87/4, 1190161/384, 7682021239/10368};
refQ = {1, 21, 2989, 714549};
chk = Table[Sum[(TT ww) /. {n -> nn, k -> kk, l -> ll}, {kk, 0, nn}, {ll, 0, nn}], {nn, 0, 3}];
chkQ = Table[Sum[TT /. {n -> nn, k -> kk, l -> ll}, {kk, 0, nn}, {ll, 0, nn}], {nn, 0, 3}];
log["  self-test Sum_{k,l} T*w, n=0..3 : ", ToString[InputForm[chk]]];
log["  expected                        : ", ToString[InputForm[If[WT === 3, ref3, ref5]]]];
log["  Q self-test ", ToString[chkQ === refQ], "   weight self-test ", ToString[chk === If[WT === 3, ref3, ref5]]];
If[chk =!= If[WT === 3, ref3, ref5] || chkQ =!= refQ, log["SELF-TEST FAILED -- ABORT."]; Close[lf]; Exit[]];

obj = TT ww;
log["obj LeafCount ", LeafCount[obj], "  distinct symbols ", Length[Union[Cases[obj, HarmonicNumber[__], Infinity]]]];

ordOf[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]]; Max[Join[{0}, Cases[ap, FF[n + a_.] :> a, Infinity]]]];
SetAttributes[stage, HoldRest];
stage[file_, name_, cap_, body_] := Module[{r, t0}, t0 = AbsoluteTime[];
  If[FileExistsQ[DIR <> file], r = Get[DIR <> file]; log["  ", name, " : loaded checkpoint"]; r,
    r = TimeConstrained[MemoryConstrained[body, MEMCAP], cap, $TimedOut];
    Which[
      r === $Aborted, log["  ", name, " : MEMORY ABORT after ", Round[AbsoluteTime[] - t0], "s  peakRSSproxy=", Round[MaxMemoryUsed[]/10^9., 2], "GB  ", DateString[]]; $Aborted,
      r === $TimedOut, log["  ", name, " : TIME ABORT after ", Round[AbsoluteTime[] - t0], "s  peakRSSproxy=", Round[MaxMemoryUsed[]/10^9., 2], "GB  ", DateString[]]; $Aborted,
      True, Put[r, DIR <> file]; log["  ", name, " #", If[Head[r] === List, Length[r], "-"], " t=", Round[AbsoluteTime[] - t0], "s  (checkpointed)  maxmem=", Round[MaxMemoryUsed[]/10^9., 2], "GB  ", DateString[]]; r]]];

(* ================= A0: split route  ann(T) (x) ann(w)  ================= *)
log["=== A0 Annihilator[T] === ", DateString[]];
annT = stage["z5_" <> TAG <> "_annT.m", "A0 annT", 600, Annihilator[TT, {S[n], S[k], S[l]}]];
log["=== A0b Annihilator[w] (harmonic part alone) === ", DateString[]];
annW = stage["z5_" <> TAG <> "_annW.m", "A0b annW", SPLITCAP, Annihilator[ww, {S[n], S[k], S[l]}]];
annS = $Aborted;
If[annT =!= $Aborted && annW =!= $Aborted, log["=== A1s DFiniteTimes[annT, annW] === ", DateString[]]; annS = stage["z5_" <> TAG <> "_annS.m", "A1s annS", SPLITCAP, DFiniteTimes[annT, annW]]];

(* ================= A1d: the direct monolithic measurement =================
   Run it up front only if the split route failed; otherwise it is deferred to
   the end of the script so that the pipeline is not blocked by a measurement.  *)
annD = $Aborted;
If[DIRECT >= 1 && annS === $Aborted, log["=== A1d Annihilator[T*w]  (monolithic, the calibration measurement) === ", DateString[]]; annD = stage["z5_" <> TAG <> "_annD.m", "A1d annD", ANNCAP, Annihilator[obj, {S[n], S[k], S[l]}]]];

ann = Which[annS =!= $Aborted, log["USING annS (split route), ", Length[annS], " generators"]; annS, annD =!= $Aborted, log["USING annD (direct), ", Length[annD], " generators"]; annD, True, $Aborted];
If[ann === $Aborted, log["NO ANNIHILATOR. ALL DONE ", DateString[]]; Close[lf]; Exit[]];
log["  ann generators ", Length[ann], "  LeafCount ", LeafCount[ann], "  rank(under staircase) ", Length[UnderTheStaircase[ann]]];

{V1, V2} = If[ORD === "lk", {l, k}, {k, l}];
log["=== A2 ct1 (eliminate ", ToString[V1], ") === ", DateString[]];
ct1 = stage["z5_" <> TAG <> "_ct1.m", "A2 ct1", CT1CAP, CreativeTelescoping[ann, S[V1] - 1, {S[n], S[V2]}]];
If[ct1 === $Aborted, log["A2 DID NOT RETURN. ALL DONE ", DateString[]]; Close[lf]; Exit[]];
log["  ct1 telescopers: ", Length[ct1[[1]]], "  LeafCount ", LeafCount[ct1[[1]]], "  certs LeafCount ", LeafCount[ct1[[2]]]];

log["=== A3 OreGroebnerBasis === ", DateString[]];
gb = stage["z5_" <> TAG <> "_gb.m", "A3 gb", CT1CAP, OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n], S[V2]]]];
If[gb === $Aborted, log["A3 DID NOT RETURN. ALL DONE ", DateString[]]; Close[lf]; Exit[]];
log["  gb === ct1tel ? ", ToString[gb === ct1[[1]]], "  LeafCount ", LeafCount[gb]];

a0f[x_] := 41218 x^3 + 198849 x^2 + 320790 x + 173057;
B8f[x_] := 3874492 x^8 + 59373972 x^7 + 394148190 x^6 + 1481084196 x^5 + 3447878810 x^4 + 5095855458 x^3 + 4673546679 x^2 + 2433871008 x + 551502039;
B9f[x_] := 48802112 x^9 + 967468896 x^8 + 8488000862 x^7 + 43246197636 x^6 + 140983768422 x^5 + 304912330849 x^4 + 437406946975 x^3 + 401272692378 x^2 + 213593890911 x + 50257929339;
cc3 = {(n + 1)^5 (n + 2) a0f[n + 1], -2 (n + 2) B8f[n], -2 B9f[n], 2 (n + 3)^5 (2 n + 5) a0f[n]};

log["=== A4 ct2 (eliminate ", ToString[V2], ") in the KNOWN, OCCUPIED (3,9) box === ", DateString[]];
got = $Failed; tLad = AbsoluteTime[];
Do[Do[supp = Table[S[n]^i, {i, 0, d}];
   If[AbsoluteTime[] - tLad > LADDERCAP, log["  ct2 LADDERCAP ", LADDERCAP, "s exhausted at d=", d, "  ", DateString[]]; Break[]];
   t0 = AbsoluteTime[];
   ct2 = Quiet[Check[MemoryConstrained[CreativeTelescoping[gb, S[V2] - 1, third, Support -> supp], MEMCAP], $Failed]];
   log["  ct2 third=", ToString[third], " d=", d, " t=", Round[AbsoluteTime[] - t0], "s -> ", If[Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1, "FOUND order " <> ToString[ordOf[ct2[[1, 1]]]], "none"], "  ", DateString[]];
   If[Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1, got = ct2; Break[]],
  {d, 0, DMAX}]; If[got =!= $Failed, Break[]], {third, {{}, {S[n]}}}];
If[got === $Failed, t0 = AbsoluteTime[];
   ct2 = Quiet[Check[TimeConstrained[MemoryConstrained[CreativeTelescoping[gb, S[V2] - 1, {S[n]}], MEMCAP], 1800], $Failed]];
   log["  ct2 FREE t=", Round[AbsoluteTime[] - t0], "s -> ", If[Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1, "FOUND order " <> ToString[ordOf[ct2[[1, 1]]]], "none"], "  ", DateString[]];
   If[Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1, got = ct2]];

If[got =!= $Failed,
   Put[{ann, ct1, gb, got}, DIR <> "z5_" <> TAG <> "_cert.m"];
   log["  SAVED z5_", TAG, "_cert.m   telescoper order ", ordOf[got[[1, 1]]], "  LeafCount ", LeafCount[got[[1, 1]]]];
   Module[{cf, rat}, cf = Table[Coefficient[ApplyOreOperator[got[[1, 1]], FF[n]], FF[n + j]], {j, 0, ordOf[got[[1, 1]]]}]; rat = If[Length[cf] === 4, Together[cf/cc3], "order is not 3"]; log["  telescoper / L_BZ coefficientwise (must be 4 equal entries): ", ToString[InputForm[rat]]]],
   log["  NO telescoper up to d=", DMAX, " by either method."]];

(* deferred monolithic measurement -- the T1 calibration number, run last *)
If[DIRECT >= 2 && annD === $Aborted, log["=== A1d(deferred) Annihilator[T*w]  monolithic === ", DateString[]]; annD = stage["z5_" <> TAG <> "_annD.m", "A1d annD", ANNCAP, Annihilator[obj, {S[n], S[k], S[l]}]]; If[annD =!= $Aborted, log["  annD generators ", Length[annD], "  LeafCount ", LeafCount[annD], "  rank ", Length[UnderTheStaircase[annD]]]]];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
