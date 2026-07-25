(* certT3.wl -- the DIRECT route on the RANK-3 form of E(v).

   PHASE2_CERTS section 11:   E(v)/T = c0 + beta*A2(k) + alpha*Psi ,
       Psi = A1(k) + 3 B1(k) + (3/2) C1 + (1/2) A1(l) ,
   and the shift-closure of  T*(c0 + beta A2(k) + alpha Psi)  is spanned by
       { T , T*A2(k) , T*Psi }
   because every shift sends A2(k) -> A2(k) + rational and Psi -> Psi + rational
   (A2(k) is S_l-invariant).  So the module has rank exactly 3, against the rank 6
   that certT.wl fed to Annihilator and the rank 12 / 19 of certJ / certA.

   This is the cheapest DIRECT attack available and it is worth one kernel-slot
   before committing to the LCLM+Abel assembly of section 9: if it returns a
   telescoper, sections 9-11 are unnecessary.

   MODE=box : eliminate l first, then k with a Support ladder (each step terminates)
   MODE=unc : unconstrained, l first
   Run:  MODE=box math < certT3.wl                                                  *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
MODE = Environment["MODE"]; If[MODE === $Failed, MODE = "box"];
lf = OpenWrite[DIR <> "certT3_" <> MODE <> ".log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], "  MODE=", MODE];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

TT = Binomial[n + k, n] Binomial[n, k]^2 Binomial[n + l, n] Binomial[n, l]^2 *
     Binomial[n + k + l, n];
{c0, alpha, beta, gamma, delta, eps} = Get[DIR <> "Eletters.m"];
(* assert the section 11 relations before using them *)
log["ratio checks (must be {3, 3/2, 1/2}): ",
    ToString[InputForm[Together /@ {gamma/alpha, delta/alpha, eps/alpha}]]];

Psi = ((HarmonicNumber[n + k] - HarmonicNumber[k])
    + 3 (HarmonicNumber[n - k] - HarmonicNumber[k])
    + (3/2) (HarmonicNumber[n + k + l] - HarmonicNumber[k + l])
    + (1/2) (HarmonicNumber[n + l] - HarmonicNumber[l]));
A2k = HarmonicNumber[n + k, 2] - HarmonicNumber[k, 2];
log["Psi HarmonicNumber count (must be 8): ",
    Length[Cases[Psi, HarmonicNumber[__], Infinity]]];

EE3 = TT (c0 + beta A2k + alpha Psi);
log["EE3 LeafCount ", LeafCount[EE3]];

t0 = AbsoluteTime[];
ann = Annihilator[EE3, {S[n], S[k], S[l]}];
log["Annihilator #", Length[ann], "  t=", Round[AbsoluteTime[] - t0], "s  ", DateString[]];
Put[ann, DIR <> "T3_ann.m"];

t0 = AbsoluteTime[];
ct1 = CreativeTelescoping[ann, S[l] - 1, {S[n], S[k]}];
log["ct1 (elim l) #", Length[ct1[[1]]], "  t=", Round[AbsoluteTime[] - t0], "s  ",
    DateString[]];
Put[ct1, DIR <> "T3_ct1.m"];

t0 = AbsoluteTime[];
gb = OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n], S[k]]];
log["gb #", Length[gb], "  t=", Round[AbsoluteTime[] - t0], "s  gb===ct1tel? ",
    ToString[gb === ct1[[1]]]];
Put[gb, DIR <> "T3_gb.m"];

ordOf[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]];
   Max[Join[{0}, Cases[ap, FF[n + a_.] :> a, Infinity]]]];

If[MODE === "unc",
  t0 = AbsoluteTime[];
  ct2 = CreativeTelescoping[gb, S[k] - 1, {S[n]}];
  log["ct2 (elim k, unconstrained) #", Length[ct2[[1]]], " t=",
      Round[AbsoluteTime[] - t0], "s order ", ordOf[ct2[[1, 1]]], "  ", DateString[]];
  Put[ct2, DIR <> "T3_ct2.m"],
  Do[Module[{supp, r},
     supp = Table[S[n]^i, {i, 0, d}];
     t0 = AbsoluteTime[];
     r = Quiet[Check[CreativeTelescoping[gb, S[k] - 1, {}, Support -> supp], $Failed]];
     log["ct2 Support d=", d, " t=", Round[AbsoluteTime[] - t0], "s -> ",
         If[Head[r] === List && Length[r] >= 1 && Length[r[[1]]] >= 1,
            "FOUND order " <> ToString[ordOf[r[[1, 1]]]], "none"], "  ", DateString[]];
     If[Head[r] === List && Length[r] >= 1 && Length[r[[1]]] >= 1,
        Put[r, DIR <> "T3_ct2.m"];
        log["*** TELESCOPER FOUND, saved T3_ct2.m ***"]; Break[]]],
   {d, 0, 12}]];

log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
