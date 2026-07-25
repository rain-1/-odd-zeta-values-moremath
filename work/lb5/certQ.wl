(* certQ.wl -- the LETTER-OUT route for the tau-split, session 4.

   MEASUREMENT that motivates this (MCP kernel, PHASE2_CERTS section 17.2):
   writing  F_tau = G_tau (p_tau + q_tau A2(k) + r_tau Psi),  the rational
   cofactors  G_tau x / T  have LeafCounts

        tau |  G p/T |  G q/T |  G r/T
        n1  |    429 |    215 |    121
        n2  |   4262 |    935 |    151
        n3  |  15027 |   2810 |    190
        kk  |  10905 |  10758 |  10611
        ll  |      0 |   1913 |      0     <---- p_ll = r_ll = 0 EXACTLY

   So  F_ll = (G_ll q_ll) * A2(k)  with  G_ll q_ll  a RATIONAL MULTIPLE OF T
   (pure hypergeometric, rank 1) and  A2(k) = H^(2)_{n+k} - H^(2)_k  INDEPENDENT
   OF l.  Therefore the l-sum factors EXACTLY,

        Sum_l F_ll  =  A2(k) * Sum_l (G_ll q_ll) ,

   with no Abel correction of any kind (the section 9.1 gap cannot arise here:
   the letter is not pulled through a Delta, it simply does not depend on the
   summation variable).  Hence the FIRST elimination -- the step certP2.wl has
   been unable to finish on the rank-2 object -- can be run on a RANK-1 object
   instead.  That is the Q-row class of computation.

   Stages (all checkpointed, all MemoryConstrained):
     Q1  ann1 = Annihilator[G_ll q_ll, {S[n],S[k],S[l]}]      (expect 3 gens, rank 1)
     Q2  ct1  = CreativeTelescoping[ann1, S[l]-1, {S[n],S[k]}] (rank-1 elimination)
     Q3  gb   = OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n],S[k]]]
                -> annihilator of  H(n,k) := Sum_l G_ll q_ll
     Q4  annH = DFiniteTimes[gb, Annihilator[A2(k), {S[n],S[k]}]]
                -> annihilator of  A2(k) H(n,k)               (rank 2 in TWO variables)
     Q5  ct2  = CreativeTelescoping[annH, S[k]-1, {}, Support -> {1..S[n]^d}]
                -> M_ll  with  M_ll . Sum_{k,l} F_ll = 0
   Boundary obligations are NOT discharged here; they are the same pole-order
   comparisons as PHASE2_CERTS section 8 and are listed in the log.

   Env: DMAX (default 12), MEMCAP (default 3.0e9), TAU (default "ll").
   Run:  DMAX=10 MEMCAP=3000000000 math < certQ.wl                                *)

DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
$HistoryLength = 0;
DMAX = Environment["DMAX"]; DMAX = If[DMAX === $Failed, 12, ToExpression[DMAX]];
MEMCAP = Environment["MEMCAP"];
MEMCAP = If[MEMCAP === $Failed, 3000000000, ToExpression[MEMCAP]];
lf = OpenWrite[DIR <> "certQ.log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], "  DMAX=", DMAX, " MEMCAP=", MEMCAP];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

TT = (Binomial[n + k, n] Binomial[n, k]^2 Binomial[n + l, n] Binomial[n, l]^2 *
      Binomial[n + k + l, n]);
AA[r_, x_] := HarmonicNumber[n + x, r] - HarmonicNumber[x, r];
sh[e_, a_, b_, c_] := e /. {n -> n + a, k -> k + b, l -> l + c};
{rho, sigma} = Get[DIR <> "Qrow_rhosigma.m"];
log["rho,sigma loaded ", LeafCount[rho], " ", LeafCount[sigma]];

A2k = AA[2, k];
(* the ll shift term of certP.wl, with p_ll = r_ll = 0 *)
Gll = (-(sigma /. l -> l + 1) sh[TT, 0, 0, 1]);
qll = Together[-(1/2) ((3/2) (1/(n + k + l + 1) - 1/(k + l + 1)) +
                       (1/2) (1/(n + l + 1) - 1/(l + 1)))];
GQ = Gll qll;
log["LeafCount Gll=", LeafCount[Gll], "  qll=", LeafCount[qll],
    "  GQ/T=", LeafCount[Together[GQ/TT]]];

(* --- ASSERTION 1: GQ is letter-free (no HarmonicNumber anywhere) --- *)
nhh = Length[Cases[GQ, HarmonicNumber[__], Infinity]];
log["HarmonicNumber count in GQ (must be 0): ", nhh];
If[nhh =!= 0,
   log["GQ IS NOT LETTER-FREE -- ABORT."]; Close[lf]; Exit[]];

(* --- ASSERTION 2: GQ*A2k reproduces certP.wl's F_ll at exact integer points --- *)
Fllref = (-(sigma /. l -> l + 1) sh[TT, 0, 0, 1]) *
   (Together[-(1/2) ((3/2) (1/(n + k + l + 1) - 1/(k + l + 1)) +
                     (1/2) (1/(n + l + 1) - 1/(l + 1)))] A2k);
chk = Table[Simplify[(GQ A2k - Fllref) /. {n -> pt[[1]], k -> pt[[2]], l -> pt[[3]]}],
   {pt, {{5, 2, 3}, {6, 1, 4}, {4, 3, 0}, {7, 0, 2}}}];
log["F_ll SPLIT CHECK (must all be 0): ", ToString[InputForm[chk]]];
If[Union[chk] =!= {0},
   log["SPLIT CHECK FAILED -- ABORT."]; Close[lf]; Exit[]];

ordOf[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]];
   Max[Join[{0}, Cases[ap, FF[n + a_.] :> a, Infinity]]]];
stage[file_, name_, body_] := Module[{r, t0},
  If[FileExistsQ[DIR <> file],
    r = Get[DIR <> file]; log["  ", name, " : loaded checkpoint"]; r,
    t0 = AbsoluteTime[]; r = MemoryConstrained[body, MEMCAP];
    If[r === $Aborted,
      log["  ", name, " : MEMORY ABORT after ", Round[AbsoluteTime[] - t0], "s"];
      $Aborted,
      Put[r, DIR <> file];
      log["  ", name, " #", Length[r], " t=", Round[AbsoluteTime[] - t0],
          "s  (checkpointed)  mem=", Round[MaxMemoryUsed[]/10^9., 2], "GB"];
      r]]];

log["=== Q1 Annihilator[GQ] (rank 1 expected: 3 first-order generators) === ",
    DateString[]];
ann1 = stage["Q_ll_ann1.m", "ann1", Annihilator[GQ, {S[n], S[k], S[l]}]];
If[ann1 === $Aborted, log["ABORT at Q1"]; Close[lf]; Exit[]];

log["=== Q2 ct1: eliminate l on the RANK-1 object === ", DateString[]];
ct1 = stage["Q_ll_ct1.m", "ct1",
            CreativeTelescoping[ann1, S[l] - 1, {S[n], S[k]}]];
If[ct1 === $Aborted, log["ABORT at Q2"]; Close[lf]; Exit[]];
log["  ct1 telescopers: ", Length[ct1[[1]]]];

log["=== Q3 OreGroebnerBasis of the telescopers === ", DateString[]];
gb = stage["Q_ll_gb.m", "gb",
           OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n], S[k]]]];
If[gb === $Aborted, log["ABORT at Q3"]; Close[lf]; Exit[]];
log["  gb === ct1tel ? ", ToString[gb === ct1[[1]]]];

log["=== Q4 DFiniteTimes with A2(k) === ", DateString[]];
annA2 = Annihilator[A2k, {S[n], S[k]}];
log["  annA2 #", Length[annA2]];
annH = stage["Q_ll_annH.m", "annH", DFiniteTimes[gb, annA2]];
If[annH === $Aborted, log["ABORT at Q4"]; Close[lf]; Exit[]];

log["=== Q5 ct2: eliminate k, Support ladder === ", DateString[]];
got = $Failed;
Do[supp = Table[S[n]^i, {i, 0, d}];
   t0 = AbsoluteTime[];
   ct2 = Quiet[Check[MemoryConstrained[
           CreativeTelescoping[annH, S[k] - 1, {}, Support -> supp], MEMCAP], $Failed]];
   log["  ct2 d=", d, " t=", Round[AbsoluteTime[] - t0], "s -> ",
       If[Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1,
          "FOUND order " <> ToString[ordOf[ct2[[1, 1]]]], "none"], "  ", DateString[]];
   If[Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1,
      got = ct2; Break[]],
 {d, 0, DMAX}];

If[got =!= $Failed,
   Put[{ann1, ct1, gb, annH, got}, DIR <> "Q_ll.m"];
   log["SAVED Q_ll.m  M_ll order ", ordOf[got[[1, 1]]]];
   log["BOUNDARY OBLIGATIONS still to discharge: (i) the l-telescoping of Q2 at ",
       "l = 0 and l = n+3 (certificate rho_l, same pole comparison as section 8); ",
       "(ii) the k-telescoping of Q5 at k = 0 and k = n+3."],
   log["NO telescoper up to d=", DMAX]];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
