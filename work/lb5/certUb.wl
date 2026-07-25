(* certUb.wl -- CHECKPOINTED + Support-BOUNDED variant of certU.wl.

   Same six rank-1 problems, but
     (i)  ann / ct1 / gb are Put to disk the moment each finishes, so a kill never
          costs more than the stage in flight;
     (ii) the second creative-telescoping step (eliminate l) is run as a bounded
          Support ladder  {1, S[n], ..., S[n]^d}, d = DMIN..DMAX, which is a finite
          linear solve and therefore TERMINATES -- unlike the unconstrained call,
          which cannot be interrupted (TimeConstrained does not bite on it).

   LABS, DMIN, DMAX come from the environment.
   Run:  LABS=beta,gamma DMIN=3 DMAX=12 math < certUb.wl                            *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
LABS = Environment["LABS"]; If[LABS === $Failed, LABS = "alpha"];
DMIN = Environment["DMIN"]; DMIN = If[DMIN === $Failed, 0, ToExpression[DMIN]];
DMAX = Environment["DMAX"]; DMAX = If[DMAX === $Failed, 12, ToExpression[DMAX]];
TAG = StringReplace[LABS, "," -> "_"];
lf = OpenWrite[DIR <> "certUb_" <> TAG <> ".log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], "  LABS=", LABS, " DMIN=", DMIN, " DMAX=", DMAX];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

TT = Binomial[n + k, n] Binomial[n, k]^2 Binomial[n + l, n] Binomial[n, l]^2 *
     Binomial[n + k + l, n];
{c0, alpha, beta, gamma, delta, eps} = Get[DIR <> "Eletters.m"];
log["Eletters loaded ", ToString[LeafCount /@ {c0, alpha, beta, gamma, delta, eps}]];
cmap = <|"alpha" -> alpha, "beta" -> beta, "gamma" -> gamma, "delta" -> delta,
         "eps" -> eps, "c0" -> c0|>;

ordOf[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]];
   Max[Join[{0}, Cases[ap, FF[n + a_.] :> a, Infinity]]]];

(* cached stage: recompute only if the checkpoint file is absent *)
stage[file_, lab_, name_, body_] := Module[{r, t0},
  If[FileExistsQ[DIR <> file],
    r = Get[DIR <> file]; log["  ", lab, " ", name, " : loaded checkpoint"]; r,
    t0 = AbsoluteTime[]; r = body;
    Put[r, DIR <> file];
    log["  ", lab, " ", name, " #", Length[r], " t=", Round[AbsoluteTime[] - t0],
        "s  (checkpointed)"]; r]];

(* ORD = "kl" : eliminate k first then l (certU.wl's order);
   ORD = "lk" : eliminate l first then k.  Section 2 of PHASE2_CERTS shows the
   elimination order changes the cost by orders of magnitude, so this is the
   substantive hedge, not a cosmetic option.                                   *)
ORD = Environment["ORD"]; If[ORD === $Failed, ORD = "kl"];
{V1, V2} = If[ORD === "lk", {l, k}, {k, l}];
log["elimination order: ", ORD, "  (first ", ToString[V1], ", then ", ToString[V2], ")"];

rank1b[lab_] := Module[{phi, ann, ct1, gb, ct2, d, supp, t0, got},
  phi = cmap[lab];
  log["=== rank-1 (bounded, ", ORD, ") for ", lab, " === ", DateString[]];
  ann = stage["Ub_" <> lab <> "_ann.m", lab, "ann",
              Annihilator[TT phi, {S[n], S[k], S[l]}]];
  ct1 = stage["Ub_" <> lab <> "_" <> ORD <> "_ct1.m", lab, "ct1",
              CreativeTelescoping[ann, S[V1] - 1, {S[n], S[V2]}]];
  gb  = stage["Ub_" <> lab <> "_" <> ORD <> "_gb.m", lab, "gb",
              OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n], S[V2]]]];
  log["  ", lab, " gb === ct1tel ? ", ToString[gb === ct1[[1]]]];
  got = $Failed;
  Do[supp = Table[S[n]^i, {i, 0, d}];
     t0 = AbsoluteTime[];
     ct2 = Quiet[Check[CreativeTelescoping[gb, S[V2] - 1, {}, Support -> supp],
                       $Failed]];
     log["  ", lab, " ct2 Support d=", d, " t=", Round[AbsoluteTime[] - t0], "s  -> ",
         If[Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1,
            "FOUND " <> ToString[Length[ct2[[1]]]] <> " telescoper(s), order " <>
              ToString[ordOf[ct2[[1, 1]]]],
            "none"], "  ", DateString[]];
     If[Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1,
        got = ct2; Break[]],
   {d, DMIN, DMAX}];
  If[got =!= $Failed,
     Put[{ann, ct1, gb, got}, DIR <> "U_" <> lab <> ".m"];
     log["  ", lab, " SAVED U_", lab, ".m  telescoper order ", ordOf[got[[1, 1]]]],
     log["  ", lab, " NO telescoper up to d=", DMAX]];
  got];

Do[rank1b[lb], {lb, StringSplit[LABS, ","]}];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
