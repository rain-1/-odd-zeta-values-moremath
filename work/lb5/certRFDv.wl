(* certRFD.wl -- the DIRECT refold run: telescope  T * vtilde  itself.

   Companion to certRF.wl (which telescopes E(vtilde), 7 symbols, via the [CERTIFIED]
   Q-row).  This script telescopes the SUMMAND itself:  S = 10 distinct symbols,
   against 12 for the folded v and 17 for what3.

   WHY THIS IS THE SAFER OF THE TWO.  The ct2 box here is not merely bounded, it is
   KNOWN AND OCCUPIED: guessrec finds a unique (order 3, degree 9) recurrence for
   Sum_{k,l} T what3 in 0 s from 501 values, and it is exactly

       L_BZ = cc3[[1]] + cc3[[2]] S_n + cc3[[3]] S_n^2 + cc3[[4]] S_n^3 ,

   with cc3 as below (degree 9 in the leading coefficient).  checkrec.py confirms
   L_BZ (Sum T vtilde) = 0 exactly for n = 0..30.  So R4 is a finite linear solve in
   a box where the answer demonstrably lives -- unlike every piece-ct2 of sections
   17-18, which CERTS_RESUME section 10.7 shows were searching empty boxes.

   The finish is then immediate and needs NO Q-row and NO E-boundary lemma:
       L_BZ (Sum_{k,l} T vtilde) = 0   [this certificate]
       L_BZ Phat = 0                   [PROVED, section 3]
       D_n = Sum T vtilde - Phat_n = 0 for n = 0..300  [VERIFIED exact, seqdata300]
       lc(L_BZ) = 2(n+3)^5(2n+5)a0[n] has no integer root n >= 0  [PROVED]
   ==> D == 0, and Sum T what3 = Sum T vtilde because what3 - vtilde is in the
   PROVED kernel (Lemma-Phi species + k<->l folding, keyid.py).  THEOREM B.

   Boundary: T has a DOUBLE zero at every integer k > n and vtilde has at worst a
   SIMPLE pole there (from B1(k) = H_{n-k} - H_k) and none in l, so every boundary
   term of the k- and l-telescopings vanishes on the box 0 <= k,l <= K, K >= n+3.
   This is section 2's boundary lemma verbatim; vtilde's letters are a SUBSET of the
   pole types it covers (it has no C letter at all).

   Env: ORD, DMAX, MEMCAP, ANNCAP, CT1CAP, LADDERCAP, FREECAP.
   Run: ORD=lk MEMCAP=2500000000 math < certRFD.wl                                 *)

DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
$HistoryLength = 0;
ORD = Environment["ORD"]; If[ORD === $Failed, ORD = "lk"];
DMAX = Environment["DMAX"]; DMAX = If[DMAX === $Failed, 5, ToExpression[DMAX]];
MEMCAP = Environment["MEMCAP"];
MEMCAP = If[MEMCAP === $Failed, 2500000000, ToExpression[MEMCAP]];
ANNCAP = Environment["ANNCAP"]; ANNCAP = If[ANNCAP === $Failed, 2700, ToExpression[ANNCAP]];
CT1CAP = Environment["CT1CAP"]; CT1CAP = If[CT1CAP === $Failed, 3600, ToExpression[CT1CAP]];
LADDERCAP = Environment["LADDERCAP"];
LADDERCAP = If[LADDERCAP === $Failed, 3600, ToExpression[LADDERCAP]];
FREECAP = Environment["FREECAP"]; FREECAP = If[FREECAP === $Failed, 900, ToExpression[FREECAP]];
lf = OpenWrite[DIR <> "certRFV_" <> ORD <> ".log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], "  ORD=", ORD, " DMAX=", DMAX, " MEMCAP=", MEMCAP,
    " ANNCAP=", ANNCAP, " LADDERCAP=", LADDERCAP];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

TT = Binomial[n + k, n] Binomial[n, k]^2 Binomial[n + l, n] Binomial[n, l]^2 *
     Binomial[n + k + l, n];
AA[r_, x_] := HarmonicNumber[n + x, r] - HarmonicNumber[x, r];
BB[r_, x_] := HarmonicNumber[n - x, r] - HarmonicNumber[x, r];
a0[x_] := 41218 x^3 + 198849 x^2 + 320790 x + 173057;
B8[x_] := 3874492 x^8 + 59373972 x^7 + 394148190 x^6 + 1481084196 x^5 +
   3447878810 x^4 + 5095855458 x^3 + 4673546679 x^2 + 2433871008 x + 551502039;
B9[x_] := 48802112 x^9 + 967468896 x^8 + 8488000862 x^7 + 43246197636 x^6 +
   140983768422 x^5 + 304912330849 x^4 + 437406946975 x^3 + 401272692378 x^2 +
   213593890911 x + 50257929339;
cc3 = {(n + 1)^5 (n + 2) a0[n + 1], -2 (n + 2) B8[n], -2 B9[n],
       2 (n + 3)^5 (2 n + 5) a0[n]};

(* the OTHER proved fold: certP.wl's  v , 12 symbols, WITH the C letter.
   Annihilator[T*v] is MEASURED at 124 s / 7 generators (CERTS_RESUME section 1),
   so this probe tests the (3,9) box on the representative whose blocking stage is
   already known to clear.  Sum T v = Sum T what3 by the k<->l folding [PROVED]. *)
CC1 = HarmonicNumber[n + k + l] - HarmonicNumber[k + l];
PsiV = (AA[1, k] + 3 BB[1, k] + (3/2) CC1 + (1/2) AA[1, l]);
vt = (HarmonicNumber[n, 3] + 2 AA[3, k] - (1/2) AA[2, k] PsiV);
nInst = Length[Cases[vt, HarmonicNumber[__], Infinity]];
nDist = Length[Union[Cases[vt, HarmonicNumber[__], Infinity]]];
log["vtilde HarmonicNumber instances (v: must be 13): ", nInst,
    "   distinct symbols S (v: must be 12): ", nDist];
If[nInst =!= 13 || nDist =!= 12,
   log["VTILDE MALFORMED -- ABORT."]; Close[lf]; Exit[]];
log["vtilde has a C letter ? ",
    ToString[! FreeQ[vt, HarmonicNumber[k + l + n] | HarmonicNumber[k + l]]],
    "   (v: must be True)"];

obj = TT vt;
log["obj = T*vtilde  LeafCount ", LeafCount[obj], "  distinct symbols ",
    Length[Union[Cases[obj, HarmonicNumber[__], Infinity]]]];

ordOf[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]];
   Max[Join[{0}, Cases[ap, FF[n + a_.] :> a, Infinity]]]];
SetAttributes[stage, HoldRest];
stage[file_, name_, cap_, body_] := Module[{r, t0},
  t0 = AbsoluteTime[];
  If[FileExistsQ[DIR <> file],
    r = Get[DIR <> file]; log["  ", name, " : loaded checkpoint"]; r,
    r = TimeConstrained[MemoryConstrained[body, MEMCAP], cap, $TimedOut];
    Which[
      r === $Aborted,
        log["  ", name, " : MEMORY ABORT after ", Round[AbsoluteTime[] - t0], "s  ",
            DateString[]]; $Aborted,
      r === $TimedOut,
        log["  ", name, " : TIME ABORT after ", Round[AbsoluteTime[] - t0], "s  ",
            DateString[]]; $Aborted,
      True,
        Put[r, DIR <> file];
        log["  ", name, " #", Length[r], " t=", Round[AbsoluteTime[] - t0],
            "s  (checkpointed)  mem=", Round[MaxMemoryUsed[]/10^9., 2], "GB  ",
            DateString[]]; r]]];

{V1, V2} = If[ORD === "lk", {l, k}, {k, l}];
log["=== D1 Annihilator[T*vtilde] === ", DateString[]];
ann = stage["RFV_ann.m", "D1 ann", ANNCAP, Annihilator[obj, {S[n], S[k], S[l]}]];
If[ann === $Aborted, log["D1 DID NOT RETURN."]; log["ALL DONE ", DateString[]];
   Close[lf]; Exit[]];
log["  ann: ", Length[ann], " generators"];

log["=== D2 ct1 (eliminate ", ToString[V1], ") === ", DateString[]];
ct1 = stage["RFV_" <> ORD <> "_ct1.m", "D2 ct1", CT1CAP,
            CreativeTelescoping[ann, S[V1] - 1, {S[n], S[V2]}]];
If[ct1 === $Aborted, log["D2 DID NOT RETURN."]; log["ALL DONE ", DateString[]];
   Close[lf]; Exit[]];
log["  ct1 telescopers: ", Length[ct1[[1]]]];

log["=== D3 OreGroebnerBasis === ", DateString[]];
gb = stage["RFV_" <> ORD <> "_gb.m", "D3 gb", CT1CAP,
           OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n], S[V2]]]];
If[gb === $Aborted, log["D3 DID NOT RETURN."]; log["ALL DONE ", DateString[]];
   Close[lf]; Exit[]];
log["  gb === ct1tel ? ", ToString[gb === ct1[[1]]]];

log["=== D4 ct2 (eliminate ", ToString[V2], ") in the KNOWN, OCCUPIED (3,9) box === ",
    DateString[]];
got = $Failed; tLad = AbsoluteTime[];
Do[Do[supp = Table[S[n]^i, {i, 0, d}];
   If[AbsoluteTime[] - tLad > LADDERCAP,
      log["  ct2 LADDERCAP ", LADDERCAP, "s exhausted at d=", d, "  ", DateString[]];
      Break[]];
   t0 = AbsoluteTime[];
   ct2 = Quiet[Check[MemoryConstrained[
           CreativeTelescoping[gb, S[V2] - 1, third, Support -> supp], MEMCAP], $Failed]];
   log["  ct2 third=", ToString[third], " d=", d, " t=", Round[AbsoluteTime[] - t0],
       "s -> ", If[Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1,
          "FOUND order " <> ToString[ordOf[ct2[[1, 1]]]], "none"], "  ", DateString[]];
   If[Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1,
      got = ct2; Break[]],
  {d, 0, DMAX}];
  If[got =!= $Failed, Break[]],
 {third, {{}, {S[n]}}}];
If[got === $Failed,
   t0 = AbsoluteTime[];
   ct2 = Quiet[Check[TimeConstrained[MemoryConstrained[
           CreativeTelescoping[gb, S[V2] - 1, {S[n]}], MEMCAP], FREECAP], $Failed]];
   log["  ct2 FREE t=", Round[AbsoluteTime[] - t0], "s -> ",
       If[Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1,
          "FOUND order " <> ToString[ordOf[ct2[[1, 1]]]], "none"], "  ", DateString[]];
   If[Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1, got = ct2]];

If[got =!= $Failed,
   Put[{ann, ct1, gb, got}, DIR <> "RFV_" <> ORD <> "_cert.m"];
   log["  SAVED RFD_", ORD, "_cert.m  telescoper order ", ordOf[got[[1, 1]]],
       "  LeafCount ", LeafCount[got[[1, 1]]]];
   (* is it L_BZ ?  compare coefficient ratios *)
   Module[{cf, rat},
     cf = Table[Coefficient[ApplyOreOperator[got[[1, 1]], FF[n]], FF[n + j]],
                {j, 0, ordOf[got[[1, 1]]]}];
     rat = If[Length[cf] === 4, Together[cf/cc3], "order is not 3"];
     log["  telescoper / L_BZ coefficientwise (must be 4 equal entries): ",
         ToString[InputForm[rat]]]];
   log["  BOUNDARY OBLIGATIONS: the ", ToString[V1], "- and ", ToString[V2],
       "-telescopings at 0 and at n+3; discharged by section 2's pole count ",
       "(T double zero at integer k > n, vtilde at worst a simple pole, none in l)."],
   log["  NO telescoper up to d=", DMAX, " by either method."]];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
