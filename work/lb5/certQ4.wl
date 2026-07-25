(* certQ2.wl -- the TAU-SPLIT x LETTER-SPLIT route, generalised from certQ.wl.

   PHASE2_CERTS section 17.2/17.3 and section 18 (this session).  Writing

       Psi = Psik + Psil ,   Psik = A1(k) + 3 B1(k)          (FREE of l)
                             Psil = (3/2) C1 + (1/2) A1(l)   (depends on l)

   and  F_tau = W_tau (P_tau + Q_tau A2(k) + R_tau Psi)  with P,Q,R RATIONAL,
   every F_tau splits into FOUR pieces whose sum is F_tau EXACTLY:

       A :  W_tau P_tau              lambda = 1        letter-free   RANK 1
       B :  W_tau Q_tau  * A2(k)     lambda = A2(k)    l-free letter RANK 1 in l
       C :  W_tau R_tau  * Psik      lambda = Psik     l-free letter RANK 1 in l
       D :  W_tau R_tau * Psil       lambda = 1        l-dep letter  RANK 2

   For A,B,C the l-elimination is run on the LETTER-FREE object W x (rank 1), and
   the l-free letter lambda(n,k) is re-attached AFTERWARDS by DFiniteTimes at the
   (n,k) level.  That is the only lever that has ever turned a "no return" into a
   return in this campaign (section 17.3: rank 2 -> 67 min no return, twice;
   rank 1 -> 9 min, returned).

   RATIONAL-COFACTOR SIZES  (LeafCount of  W_tau X_tau / T,  MCP-measured):

        tau |   A (W P/T) |   B (W Q/T) |  C,D (W R/T)
        n1  |         429 |         215 |          121
        n2  |        4262 |         935 |          151
        n3  |       15027 |        2810 |          190
        kk  |       10905 |       10758 |        10611
        ll  |           0 |        1913 |            0   <- p_ll = r_ll = 0

   so 13 non-zero rank-1 problems (A,B,C for n1,n2,n3,kk plus B for ll) and
   4 rank-2 remnants (D for n1,n2,n3,kk).  ll has NO remnant at all.

   Stages, all checkpointed, all genuinely MemoryConstrained (HoldRest):
     R1  ann  = Annihilator[obj, {S[n],S[k],S[l]}]
     R2  ct1  = CreativeTelescoping[ann, S[l]-1, {S[n],S[k]}]
     R3  gb   = OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n],S[k]]]   -> Ann[Sum_l obj]
     R4  annL = DFiniteTimes[gb, Annihilator[lambda, {S[n],S[k]}]]  (identity if lambda==1)
     R5  ct2  = CreativeTelescoping[annL, S[k]-1, {}, Support -> ladder]  -> M_piece
   Boundary obligations are NOT discharged here; they are listed in the log.

   Env:  JOBS  (default "n1:C,n1:B,n1:A,n1:D"), colon-separated tau:piece pairs
         DMAX (default 10), MEMCAP (default 3.0e9)
   Run:  JOBS=n1:C,n1:B DMAX=10 MEMCAP=3000000000 math < certQ2.wl                  *)

DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
$HistoryLength = 0;
JOBS = Environment["JOBS"]; If[JOBS === $Failed, JOBS = "n1:C,n1:B,n1:A,n1:D"];
DMAX = Environment["DMAX"]; DMAX = If[DMAX === $Failed, 10, ToExpression[DMAX]];
(* LADDERCAP: total wall-clock seconds allowed in one job's ct2 Support ladder.
   certQ2.wl had no such cap and does not checkpoint ct2, so a single job whose
   ladder runs long starves every later job in JOBS.  Default 45 min, matching the
   session's per-stage budget. *)
LADDERCAP = Environment["LADDERCAP"];
LADDERCAP = If[LADDERCAP === $Failed, 2700, ToExpression[LADDERCAP]];
(* FREECAP: seconds allowed for the unconstrained ct2 attempt before falling back
   to the Support ladder. *)
FREECAP = Environment["FREECAP"];
FREECAP = If[FREECAP === $Failed, 600, ToExpression[FREECAP]];
(* RUNGCAP: seconds allowed for ONE Support-ladder rung.  Without it a single rung
   is uninterruptible and LADDERCAP is vacuous -- see the note at the ct2 ladder. *)
RUNGCAP = Environment["RUNGCAP"];
RUNGCAP = If[RUNGCAP === $Failed, 900, ToExpression[RUNGCAP]];
MEMCAP = Environment["MEMCAP"];
MEMCAP = If[MEMCAP === $Failed, 3000000000, ToExpression[MEMCAP]];
TAG = StringReplace[JOBS, {"," -> "_", ":" -> ""}];
lf = OpenWrite[DIR <> "certQ2_" <> TAG <> ".log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], "  JOBS=", JOBS, " DMAX=", DMAX, " MEMCAP=", MEMCAP];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

(* ------------------------------------------------------------------ *)
(* certP.wl's definitions, verbatim -- the pieces must be rebuilt from *)
(* THESE, not from any assertion of our own (section 16 circularity).  *)
(* ------------------------------------------------------------------ *)
TT = Binomial[n + k, n] Binomial[n, k]^2 Binomial[n + l, n] Binomial[n, l]^2 *
     Binomial[n + k + l, n];
AA[r_, x_] := HarmonicNumber[n + x, r] - HarmonicNumber[x, r];
BB[r_, x_] := HarmonicNumber[n - x, r] - HarmonicNumber[x, r];
CC1 = HarmonicNumber[n + k + l] - HarmonicNumber[k + l];
a0[x_] := 41218 x^3 + 198849 x^2 + 320790 x + 173057;
B8[x_] := 3874492 x^8 + 59373972 x^7 + 394148190 x^6 + 1481084196 x^5 +
   3447878810 x^4 + 5095855458 x^3 + 4673546679 x^2 + 2433871008 x + 551502039;
B9[x_] := 48802112 x^9 + 967468896 x^8 + 8488000862 x^7 + 43246197636 x^6 +
   140983768422 x^5 + 304912330849 x^4 + 437406946975 x^3 + 401272692378 x^2 +
   213593890911 x + 50257929339;
cc3 = {(n + 1)^5 (n + 2) a0[n + 1], -2 (n + 2) B8[n], -2 B9[n],
       2 (n + 3)^5 (2 n + 5) a0[n]};
sh[e_, a_, b_, c_] := e /. {n -> n + a, k -> k + b, l -> l + c};
{rho, sigma} = Get[DIR <> "Qrow_rhosigma.m"];
log["rho,sigma loaded ", LeafCount[rho], " ", LeafCount[sigma]];

A2k = AA[2, k];
Psik = AA[1, k] + 3 BB[1, k];
Psil = (3/2) CC1 + (1/2) AA[1, l];
Psi = (AA[1, k] + 3 BB[1, k] + (3/2) CC1 + (1/2) AA[1, l]);
vw = (HarmonicNumber[n, 3] + 2 AA[3, k] - (1/2) A2k Psi);

sumi[e_, j_] := Sum[e, {i, 1, j}];
tauNQ[tau_] := MemberQ[{"n1", "n2", "n3"}, tau];
tauJf[tau_] := Which[tau === "n1", 1, tau === "n2", 2, tau === "n3", 3, True, 0];
tauW[tau_] := Which[
   tauNQ[tau], cc3[[tauJf[tau] + 1]] sh[TT, tauJf[tau], 0, 0],
   tau === "kk", -(rho /. k -> k + 1) sh[TT, 0, 1, 0],
   True, -(sigma /. l -> l + 1) sh[TT, 0, 0, 1]];
dA2f[tau_] := Which[
   tauNQ[tau], sumi[1/(n + i + k)^2, tauJf[tau]],
   tau === "kk", 1/(n + k + 1)^2 - 1/(k + 1)^2,
   True, 0];
dPsif[tau_] := Which[
   tauNQ[tau], sumi[1/(n + i + k) + 3/(n + i - k) + (3/2)/(n + i + k + l) +
                    (1/2)/(n + i + l), tauJf[tau]],
   tau === "kk", (1/(n + k + 1) - 1/(k + 1)) + 3 (-1/(n - k) - 1/(k + 1)) +
                 (3/2) (1/(n + k + l + 1) - 1/(k + l + 1)),
   True, (3/2) (1/(n + k + l + 1) - 1/(k + l + 1)) + (1/2) (1/(n + l + 1) - 1/(l + 1))];
h3f[tau_] := If[tauNQ[tau], sumi[1/(n + i)^3, tauJf[tau]], 0];
a3f[tau_] := Which[
   tauNQ[tau], sumi[1/(n + i + k)^3, tauJf[tau]],
   tau === "kk", 1/(n + k + 1)^3 - 1/(k + 1)^3,
   True, 0];
stuff[tau_] := Module[{dA2 = dA2f[tau], dPsi = dPsif[tau]},
   Together[h3f[tau] + 2 a3f[tau] - (1/2) dA2 dPsi]
   + Together[-(1/2) dPsi] A2k + Together[-(1/2) dA2] Psi];
Ftau[tau_] := tauW[tau] stuff[tau];

(* ---- the three rational cofactors of the letter split ---- *)
Pf[tau_] := Together[h3f[tau] + 2 a3f[tau] - (1/2) dA2f[tau] dPsif[tau]];
Qf[tau_] := Together[-(1/2) dPsif[tau]];
Rf[tau_] := Together[-(1/2) dA2f[tau]];

(* ------------------------------------------------------------------ *)
(* ASSERTIONS -- non-circular.  Each rebuilds certP.wl's own stuff[]/  *)
(* Ftau[] and compares it against the four pieces.  ABORT on failure.  *)
(* ------------------------------------------------------------------ *)
chkTau[tau_] := chkTau[tau] = Module[{sym, nh, pts},
  (* (i) Psi really is Psik + Psil *)
  If[Simplify[Psi - (Psik + Psil)] =!= 0,
     log["PSI SPLIT FAILED -- ABORT."]; Close[lf]; Exit[]];
  (* (ii) the l-free letters really are free of l *)
  If[! (FreeQ[A2k, l] && FreeQ[Psik, l]),
     log["A2k / Psik NOT l-FREE -- ABORT."]; Close[lf]; Exit[]];
  (* (iii) the three cofactors carry NO letter *)
  nh = Length[Cases[{tauW[tau] Pf[tau], tauW[tau] Qf[tau], tauW[tau] Rf[tau]},
                    HarmonicNumber[__], Infinity]];
  (* (iv) SYMBOLIC identity against certP.wl's stuff[] -- this is the whole claim *)
  sym = Simplify[stuff[tau] - (Pf[tau] + Qf[tau] A2k + Rf[tau] (Psik + Psil))];
  (* (v) and the same on the full F_tau at exact integer points *)
  pts = Table[Simplify[(Ftau[tau] - (tauW[tau] Pf[tau] + tauW[tau] Qf[tau] A2k +
        tauW[tau] Rf[tau] Psik + tauW[tau] Rf[tau] Psil)) /.
        {n -> pt[[1]], k -> pt[[2]], l -> pt[[3]]}],
     {pt, {{5, 2, 3}, {6, 1, 4}, {4, 3, 0}, {7, 0, 2}, {9, 4, 1}}}];
  log["  CHECK ", tau, " : letters-in-cofactors=", nh, " symbolic=",
      ToString[InputForm[sym]], " points=", ToString[InputForm[pts]]];
  If[nh =!= 0 || sym =!= 0 || Union[pts] =!= {0},
     log["  LETTER SPLIT CHECK FAILED for ", tau, " -- ABORT."];
     Close[lf]; Exit[]];
  True];

(* ---- piece -> (object, lambda) ---- *)
objOf[tau_, pc_] := Which[
   pc === "A", tauW[tau] Pf[tau],
   pc === "B", tauW[tau] Qf[tau],
   pc === "C", tauW[tau] Rf[tau],
   True, tauW[tau] Rf[tau] Psil];
lamOf[tau_, pc_] := Which[pc === "A", 1, pc === "B", A2k, pc === "C", Psik, True, 1];

ordOf[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]];
   Max[Join[{0}, Cases[ap, FF[n + a_.] :> a, Infinity]]]];

(* HoldRest is ESSENTIAL -- PHASE2_CERTS section 17.5.  Without it `body` is
   evaluated BEFORE stage is entered, so MemoryConstrained wraps a finished value
   and can never abort, and the checkpoint branch redoes the work first. *)
SetAttributes[stage, HoldRest];
stage[file_, lab_, name_, body_] := Module[{r, t0},
  t0 = AbsoluteTime[];
  If[FileExistsQ[DIR <> file],
    r = Get[DIR <> file]; log["  ", lab, " ", name, " : loaded checkpoint"]; r,
    r = MemoryConstrained[body, MEMCAP];
    If[r === $Aborted, log["  ", lab, " ", name, " : MEMORY ABORT after ",
        Round[AbsoluteTime[] - t0], "s  ", DateString[]]; $Aborted,
      Put[r, DIR <> file];
      log["  ", lab, " ", name, " #", Length[r], " t=", Round[AbsoluteTime[] - t0],
          "s  (checkpointed)  mem=", Round[MaxMemoryUsed[]/10^9., 2], "GB  ",
          DateString[]]; r]]];

doJob[tau_, pc_] := Module[{pre, obj, lam, ann, ct1, gb, annL, annlam, ct2, supp, t0,
                            got, tLad, nAborted},
  pre = "R_" <> tau <> "_" <> pc <> "_";
  log["=== JOB ", tau, ":", pc, " === ", DateString[]];
  (* a finished job is never redone -- the ct2 ladder is the expensive part and
     certQ2.wl did not checkpoint it *)
  If[FileExistsQ[DIR <> "R_" <> tau <> "_" <> pc <> ".m"],
     log["  ", tau, ":", pc, " ALREADY COMPLETE -- skipping."];
     Return[Get[DIR <> "R_" <> tau <> "_" <> pc <> ".m"][[5]]]];
  chkTau[tau];
  obj = objOf[tau, pc]; lam = lamOf[tau, pc];
  If[Together[obj] === 0,
     log["  ", tau, ":", pc, " is IDENTICALLY ZERO -- nothing to telescope."];
     Return["zero"]];
  log["  obj LeafCount ", LeafCount[obj], "  obj/T ", LeafCount[Together[obj/TT]],
      "  lambda ", ToString[InputForm[lam /. HarmonicNumber[a__] :> HH[a]]]];
  ann = stage[pre <> "ann.m", tau <> ":" <> pc, "ann",
              Annihilator[obj, {S[n], S[k], S[l]}]];
  If[ann === $Aborted, Return[$Failed]];
  log["  ann rank-ish: ", Length[ann], " generators"];
  ct1 = stage[pre <> "ct1.m", tau <> ":" <> pc, "ct1",
              CreativeTelescoping[ann, S[l] - 1, {S[n], S[k]}]];
  If[ct1 === $Aborted, Return[$Failed]];
  log["  ct1 telescopers: ", Length[ct1[[1]]]];
  gb = stage[pre <> "gb.m", tau <> ":" <> pc, "gb",
             OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n], S[k]]]];
  If[gb === $Aborted, Return[$Failed]];
  log["  gb === ct1tel ? ", ToString[gb === ct1[[1]]]];
  If[lam === 1,
     annL = gb; log["  lambda = 1, no DFiniteTimes"],
     annlam = Annihilator[lam, {S[n], S[k]}];
     log["  ann(lambda) #", Length[annlam]];
     annL = stage[pre <> "annL.m", tau <> ":" <> pc, "annL",
                  DFiniteTimes[gb, annlam]];
     If[annL === $Aborted, Return[$Failed]]];
  (* CT2V: CERTS_RESUME 9.4 records that passing {} as the third argument can make
     EVERY rung report "none" in ~0 s (the certP2.wl bug).  So run the ladder twice,
     with {} and then with {S[n]}, and take whichever finds a telescoper. *)
  (* FREE ct2 first.  The Support ladder costs ~3.8x per rung (measured on n1:A:
     1,6,15,49,185 s for d=0..4), so it cannot reach d >= 6.  An unconstrained
     CreativeTelescoping finds the MINIMAL telescoper directly and, on objects this
     small, may beat the whole ladder.  Time-capped so it cannot become the new wall. *)
  got = $Failed; tLad = AbsoluteTime[]; nAborted = 0;
  t0 = AbsoluteTime[];
  (* same nesting rule as the ladder rungs below: Check INSIDE, so a timeout cannot be
     relabelled "none".  A capped call that reports "none" would otherwise be read as
     "no telescoper of this order exists", which is a different and much stronger claim. *)
  ct2 = TimeConstrained[
          Quiet[Check[MemoryConstrained[
            CreativeTelescoping[annL, S[k] - 1, {S[n]}], MEMCAP], $Failed]],
          FREECAP, rungTimedOut];
  log["  ct2 FREE t=", Round[AbsoluteTime[] - t0], "s -> ",
      Which[
        ct2 === rungTimedOut,
          "FREECAP TIMEOUT (" <> ToString[FREECAP] <> "s) -- NOT an exclusion",
        ct2 === $Aborted, "MEMCAP ABORT -- NOT an exclusion",
        Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1,
          "FOUND order " <> ToString[ordOf[ct2[[1, 1]]]],
        True, "none"], "  ", DateString[]];
  If[Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1, got = ct2];
  If[got === $Failed,
  Do[Do[supp = Table[S[n]^i, {i, 0, d}];
     If[AbsoluteTime[] - tLad > LADDERCAP,
        log["  ct2 LADDERCAP ", LADDERCAP, "s exhausted at d=", d,
            " -- abandoning ", tau, ":", pc, "  ", DateString[]]; Break[]];
     t0 = AbsoluteTime[];
     (* RUNGCAP: LADDERCAP is only tested BETWEEN rungs, so it bounds how many rungs
        are STARTED, not the time spent inside one.  Measured failure: kk:C sat in the
        d=0 rung for >55 min with no log line and no way to interrupt it.  Each rung
        therefore needs its own TimeConstrained. *)
     (* The timeout marker MUST be distinguishable from a genuine empty search.
        With TimeConstrained[..., RUNGCAP, $Failed] the log printed "none" in both
        cases, so the cap would fire INVISIBLY -- the same defect class as the three
        in PHASE2_CERTS 18.22.  rungTimedOut is a unique inert symbol. *)
     (* NESTING ORDER IS LOAD-BEARING.  With Check OUTSIDE TimeConstrained, an abort
        that emits any message is caught by Check and turned into $Failed -- which the
        logger then prints as "none", i.e. a TIMEOUT MASQUERADING AS AN EXCLUSION.
        Measured: the d=0 rung truly costs 16 s, yet at RUNGCAP=3 and RUNGCAP=1 it
        reported "none" at t=3s / t=1s.  Check must be INSIDE, guarding only the
        computation, so TimeConstrained's default value cannot be intercepted. *)
     ct2 = TimeConstrained[
             Quiet[Check[MemoryConstrained[
               CreativeTelescoping[annL, S[k] - 1, third, Support -> supp], MEMCAP],
               $Failed]],
             RUNGCAP, rungTimedOut];
     log["  ct2 third=", ToString[third], " d=", d, " t=",
         Round[AbsoluteTime[] - t0], "s -> ",
         Which[
           ct2 === rungTimedOut,
             "RUNGCAP TIMEOUT (" <> ToString[RUNGCAP] <> "s) -- rung ABORTED",
           ct2 === $Aborted, "MEMCAP ABORT",
           Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1,
             "FOUND order " <> ToString[ordOf[ct2[[1, 1]]]],
           True, "none"], "  ", DateString[]];
     If[ct2 === rungTimedOut || ct2 === $Aborted, nAborted = nAborted + 1];
     If[Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1,
        got = ct2; Break[]],
   {d, 0, DMAX}];
   If[got =!= $Failed, Break[]],
  {third, {{}, {S[n]}}}]];
  If[got =!= $Failed,
     Put[{ann, ct1, gb, annL, got}, DIR <> "R_" <> tau <> "_" <> pc <> ".m"];
     log["  SAVED R_", tau, "_", pc, ".m  telescoper order ", ordOf[got[[1, 1]]],
         "  LeafCount ", LeafCount[got[[1, 1]]]];
     log["  BOUNDARY OBLIGATIONS for ", tau, ":", pc,
         " -- (i) the l-telescoping of R2 at l = 0 and l = n+3; ",
         "(ii) the k-telescoping of R5 at k = 0 and k = n+3."],
     If[nAborted > 0,
        log["  NO telescoper found up to d=", DMAX, " BUT ", nAborted,
            " rung(s) were ABORTED by RUNGCAP/MEMCAP -- this is NOT an exclusion. ",
            "Re-run with a larger RUNGCAP before treating any order as ruled out."],
        log["  NO telescoper up to d=", DMAX,
            " (all rungs ran to completion -- a genuine exclusion)"]]];
  got];

Do[Module[{p = StringSplit[j, ":"]},
   doJob[p[[1]], p[[2]]]], {j, StringSplit[JOBS, ","]}];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
