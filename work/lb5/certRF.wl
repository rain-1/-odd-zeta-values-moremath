(* certRF.wl -- THE REFOLD RUN.  The monolithic telescoping of E(vtilde).

   work/REFOLD.md section 4.  The refolded weight

       vtilde = H^(3)_n + 2 A3(k) + (1/2) X Y ,
       X = A2(l) - A2(k) ,   Y = Psi_k = A1(k) + 3 B1(k)

   satisfies  Sum_{k,l} T vtilde = Phat_n  [VERIFIED exact over Q, n = 0..33,36,40]
   and  what3 - vtilde  lies in the PROVED kernel (Lemma-Phi species + k<->l folding),
   so certifying vtilde certifies THEOREM B itself.

   vtilde carries S = 10 distinct harmonic symbols and NO C letter; E(vtilde) carries
   E = 7.  Section 18.17's calibration of the letter-count law has data at 9 symbols
   (F_kk: OOM 7.8 GB / 85 min), 3 (kk:C route: 69 s through R1-R3) and 0 (34 s), and
   NOTHING at 7.  R1 of this script is that measurement.

   E is linear in the weight and its weights G_tau depend only on T, rho, sigma, L_BZ,
   so certP.wl's tauW[] and the [CERTIFIED] Q-row are reused verbatim:

       E(vtilde) = Sum_tau G_tau (tau.vtilde - vtilde)
                 = T ( c0 + beta X + alpha Y )        -- rank 3, REFOLD section 4.6
       alpha = Sum_tau (G_tau/T) (1/2) dX_tau
       beta  = Sum_tau (G_tau/T) (1/2) dY_tau
       c0    = Sum_tau (G_tau/T) ( dh3_tau + 2 da3_tau + (1/2) dX_tau dY_tau )

   WHY the ct2 box is known here and was empty for every piece.  guessrec finds a
   UNIQUE (order 3, degree 9) recurrence = L_BZ for the COMBINATION Sum_{k,l} T what3
   in 0 s from 501 values, while the single-letter PIECES have no recurrence at all
   with r <= 12, d <= 30 (CERTS_RESUME section 10.7).  The whole point of not
   splitting is that the operator exists.  Moreover Sum_{k,l} E(vtilde) = 0
   identically, so the IDEAL outcome is an order-0 telescoper -- the d = 0 rung.

   Stages, all checkpointed, all genuinely MemoryConstrained (HoldRest -- section 17.5):
     R1  ann  = Annihilator[Etil, {S[n],S[k],S[l]}]                 <- THE MEASUREMENT
     R2  ct1  = CreativeTelescoping[ann, S[V1]-1, {S[n],S[V2]}]
     R3  gb   = OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n],S[V2]]]  -> Ann[Sum_V1 Etil]
     R4  ct2  = CreativeTelescoping[gb, S[V2]-1, third, Support -> ladder]

   ORD = lk (default): eliminate l FIRST.  Section 2's rule is "eliminate first a
   variable that few letters depend on"; vtilde's l-side letter content is the SINGLE
   letter A2(l) (2 symbols) against 5 symbols on the k side, and there is no C letter
   coupling them at all.  That decoupling is the structural gain of the refold.

   Env: ORD (lk|kl), DMAX, MEMCAP, ANNCAP, CT1CAP, LADDERCAP, FREECAP.
   Run: ORD=lk MEMCAP=5000000000 math < certRF.wl                                  *)

DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
$HistoryLength = 0;
ORD = Environment["ORD"]; If[ORD === $Failed, ORD = "lk"];
DMAX = Environment["DMAX"]; DMAX = If[DMAX === $Failed, 4, ToExpression[DMAX]];
MEMCAP = Environment["MEMCAP"];
MEMCAP = If[MEMCAP === $Failed, 5000000000, ToExpression[MEMCAP]];
(* ANNCAP: seconds allowed for R1.  TimeConstrained is known NOT to interrupt
   CreativeTelescoping (section 0); whether it interrupts Annihilator is itself part
   of the measurement.  MemoryConstrained is the reliable brake. *)
ANNCAP = Environment["ANNCAP"]; ANNCAP = If[ANNCAP === $Failed, 2700, ToExpression[ANNCAP]];
CT1CAP = Environment["CT1CAP"]; CT1CAP = If[CT1CAP === $Failed, 3600, ToExpression[CT1CAP]];
LADDERCAP = Environment["LADDERCAP"];
LADDERCAP = If[LADDERCAP === $Failed, 2700, ToExpression[LADDERCAP]];
FREECAP = Environment["FREECAP"]; FREECAP = If[FREECAP === $Failed, 900, ToExpression[FREECAP]];
lf = OpenWrite[DIR <> "certRF_" <> ORD <> ".log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], "  ORD=", ORD, " DMAX=", DMAX, " MEMCAP=", MEMCAP,
    " ANNCAP=", ANNCAP, " CT1CAP=", CT1CAP, " LADDERCAP=", LADDERCAP, " FREECAP=", FREECAP];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

(* ---------------- certP.wl's definitions, verbatim ---------------- *)
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
sh[e_, a_, b_, c_] := e /. {n -> n + a, k -> k + b, l -> l + c};
{rho, sigma} = Get[DIR <> "Qrow_rhosigma.m"];
log["rho,sigma loaded ", LeafCount[rho], " ", LeafCount[sigma]];

(* ---------------- the refolded weight vtilde ---------------- *)
X = AA[2, l] - AA[2, k];
Y = AA[1, k] + 3 BB[1, k];
h3 = HarmonicNumber[n, 3];
a3 = AA[3, k];
vt = (h3 + 2 a3 + (1/2) X Y);
nInst = Length[Cases[vt, HarmonicNumber[__], Infinity]];
nDist = Length[Union[Cases[vt, HarmonicNumber[__], Infinity]]];
log["vtilde HarmonicNumber instances (must be 11): ", nInst,
    "   distinct symbols S (must be 10): ", nDist];
If[nInst =!= 11 || nDist =!= 10,
   log["VTILDE MALFORMED -- the line-truncation trap.  ABORT."]; Close[lf]; Exit[]];

(* ---------------- the five shift terms and REFOLD section 4.6's tables -------- *)
sumi[e_, j_] := Sum[e, {i, 1, j}];
tauNQ[tau_] := MemberQ[{"n1", "n2", "n3"}, tau];
tauJf[tau_] := Which[tau === "n1", 1, tau === "n2", 2, tau === "n3", 3, True, 0];
tauW[tau_] := Which[
   tauNQ[tau], cc3[[tauJf[tau] + 1]] sh[TT, tauJf[tau], 0, 0],
   tau === "kk", -(rho /. k -> k + 1) sh[TT, 0, 1, 0],
   True, -(sigma /. l -> l + 1) sh[TT, 0, 0, 1]];
tauSh[e_, tau_] := Which[
   tauNQ[tau], sh[e, tauJf[tau], 0, 0],
   tau === "kk", sh[e, 0, 1, 0],
   True, sh[e, 0, 0, 1]];
dh3f[tau_] := If[tauNQ[tau], sumi[1/(n + i)^3, tauJf[tau]], 0];
da3f[tau_] := Which[
   tauNQ[tau], sumi[1/(n + i + k)^3, tauJf[tau]],
   tau === "kk", 1/(n + k + 1)^3 - 1/(k + 1)^3,
   True, 0];
dXf[tau_] := Which[
   tauNQ[tau], sumi[1/(n + i + l)^2 - 1/(n + i + k)^2, tauJf[tau]],
   tau === "kk", -(1/(n + k + 1)^2 - 1/(k + 1)^2),
   True, 1/(n + l + 1)^2 - 1/(l + 1)^2];
dYf[tau_] := Which[
   tauNQ[tau], sumi[1/(n + i + k) + 3/(n + i - k), tauJf[tau]],
   tau === "kk", (1/(n + k + 1) - 1/(k + 1)) - 3 (1/(n - k) + 1/(k + 1)),
   True, 0];
alltau = {"n1", "n2", "n3", "kk", "ll"};

(* ASSERTION A3 -- the tables of REFOLD section 4.6 against the ACTUAL shift of
   vtilde.  Non-circular: the right-hand side is built from HarmonicNumber. *)
tabchk = Table[{tau,
    Simplify[FunctionExpand[tauSh[h3, tau] - h3 - dh3f[tau]]],
    Simplify[FunctionExpand[tauSh[a3, tau] - a3 - da3f[tau]]],
    Simplify[FunctionExpand[tauSh[X, tau] - X - dXf[tau]]],
    Simplify[FunctionExpand[tauSh[Y, tau] - Y - dYf[tau]]]}, {tau, alltau}];
log["TABLE CHECK dh3/da3/dX/dY (all must be 0): ", ToString[InputForm[tabchk]]];
If[Union[Flatten[tabchk[[All, 2 ;; 5]]]] =!= {0},
   log["SHIFT TABLE CHECK FAILED -- ABORT."]; Close[lf]; Exit[]];

(* ---------------- E(vtilde) in rank-3 letter form ---------------- *)
wr[tau_] := wr[tau] = Together[FunctionExpand[tauW[tau]/TT]];
log["W_tau/T LeafCounts: ", ToString[Table[LeafCount[wr[tau]], {tau, alltau}]]];
If[! And @@ Table[FreeQ[wr[tau], Binomial] && FreeQ[wr[tau], Gamma] &&
       FreeQ[wr[tau], HarmonicNumber], {tau, alltau}],
   log["W_tau/T IS NOT A RATIONAL FUNCTION -- ABORT."]; Close[lf]; Exit[]];
pT[tau_] := pT[tau] = Together[dh3f[tau] + 2 da3f[tau] + (1/2) dXf[tau] dYf[tau]];
qT[tau_] := qT[tau] = Together[(1/2) dYf[tau]];
rT[tau_] := rT[tau] = Together[(1/2) dXf[tau]];
c0oT = Together[Sum[wr[tau] pT[tau], {tau, alltau}]];
betoT = Together[Sum[wr[tau] qT[tau], {tau, alltau}]];
alpoT = Together[Sum[wr[tau] rT[tau], {tau, alltau}]];
log["E/T coefficients  c0=", LeafCount[c0oT], "  beta=", LeafCount[betoT],
    "  alpha=", LeafCount[alpoT], "   (E(v) for comparison: 66499 / 44011 / 22317)"];
Etil = TT (c0oT + betoT X + alpoT Y);
eDist = Length[Union[Cases[Etil, HarmonicNumber[__], Infinity]]];
log["E(vtilde) distinct symbols E (must be 7): ", eDist, "   ",
    ToString[InputForm[Union[Cases[Etil, HarmonicNumber[__], Infinity]]]]];
If[eDist =!= 7,
   log["E(vtilde) SYMBOL COUNT WRONG -- ABORT."]; Close[lf]; Exit[]];

(* ASSERTION A4 -- the letter form against the raw definition, exact integer points *)
EErefT = Sum[tauW[tau] (tauSh[vt, tau] - vt), {tau, alltau}];
pts = {{5, 2, 3}, {6, 1, 4}, {4, 3, 0}, {7, 0, 2}, {9, 4, 1}, {8, 3, 5}};
splitres = Table[Simplify[(Etil - EErefT) /. {n -> pt[[1]], k -> pt[[2]], l -> pt[[3]]}],
   {pt, pts}];
log["SPLIT CHECK (must all be 0): ", ToString[InputForm[splitres]]];
If[Union[splitres] =!= {0},
   log["SPLIT CHECK FAILED -- refusing to telescope a wrong object.  ABORT."];
   Close[lf]; Exit[]];
log["ALL ASSERTIONS PASS.  Etil LeafCount ", LeafCount[Etil], "  ", DateString[]];

ordOf[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]];
   Max[Join[{0}, Cases[ap, FF[n + a_.] :> a, Infinity]]]];
(* HoldRest is ESSENTIAL -- PHASE2_CERTS section 17.5. *)
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
log["=== R1 Annihilator[E(vtilde)] -- THE MEASUREMENT === ", DateString[]];
ann = stage["RF_ann.m", "R1 ann", ANNCAP, Annihilator[Etil, {S[n], S[k], S[l]}]];
If[ann === $Aborted,
   log["R1 DID NOT RETURN.  This is the verdict: the 7-symbol point on the ",
       "letter-count calibration is NOT reachable on this hardware."];
   log["ALL DONE ", DateString[]]; Close[lf]; Exit[]];
log["  ann: ", Length[ann], " generators"];

log["=== R2 ct1 (eliminate ", ToString[V1], ") === ", DateString[]];
ct1 = stage["RF_" <> ORD <> "_ct1.m", "R2 ct1", CT1CAP,
            CreativeTelescoping[ann, S[V1] - 1, {S[n], S[V2]}]];
If[ct1 === $Aborted, log["R2 DID NOT RETURN."]; log["ALL DONE ", DateString[]];
   Close[lf]; Exit[]];
log["  ct1 telescopers: ", Length[ct1[[1]]]];

log["=== R3 OreGroebnerBasis === ", DateString[]];
gb = stage["RF_" <> ORD <> "_gb.m", "R3 gb", CT1CAP,
           OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n], S[V2]]]];
If[gb === $Aborted, log["R3 DID NOT RETURN."]; log["ALL DONE ", DateString[]];
   Close[lf]; Exit[]];
log["  gb === ct1tel ? ", ToString[gb === ct1[[1]]]];

(* ---- R4  ct2: the KNOWN, NON-EMPTY (3,9) box.  d = 0 is the ideal outcome
        (Sum_{k,l} E(vtilde) = 0 identically), d <= 3 is L_BZ's own order. ---- *)
log["=== R4 ct2 (eliminate ", ToString[V2], ") in the KNOWN (3,9) box === ",
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
   Put[{ann, ct1, gb, got}, DIR <> "RF_" <> ORD <> "_cert.m"];
   log["  SAVED RF_", ORD, "_cert.m  telescoper order ", ordOf[got[[1, 1]]],
       "  LeafCount ", LeafCount[got[[1, 1]]]];
   log["  BOUNDARY OBLIGATIONS: (i) the ", ToString[V1],
       "-telescoping of R2 at ", ToString[V1], " = 0 and ", ToString[V1],
       " = n+3; (ii) the ", ToString[V2], "-telescoping of R4 at ", ToString[V2],
       " = 0 and ", ToString[V2], " = n+3."],
   log["  NO telescoper up to d=", DMAX, " by either method."]];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
