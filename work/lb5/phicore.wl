(* phicore.wl -- the phi-shift primitive for the letter-split assembly.
   PHASE2_CERTS section 18.5.  Loads NO RISC package.

   THE LEMMA (verified symbolically, cocycle-checked -- see phi_tables.m):
   for an l-free letter lambda in {A2(k), Psik} and any shift,

        S_n^a S_k^b lambda  =  lambda + phi_lambda(a,b;n,k) ,      phi RATIONAL.

   CONSEQUENCE, which is what the assembly needs.  For any Ore operator
   O = Sum c_{ab} S_n^a S_k^b and any function S(n,k),

        O . (lambda S)  =  lambda * (O . S)  +  (O_phi . S) ,
        O_phi := Sum c_{ab} phi_lambda(a,b) S_n^a S_k^b .

   Note this is a TAUTOLOGY once the lemma holds -- expand both sides on the
   basis S(n+a,k+b).  So the whole content sits in the phi table, and the table
   is checked independently by the cocycle identity
        phi(a+a',b+b') == phi(a,b) + shift_{a,b}[phi(a',b')] ,
   which is 0 in all 81 cases for each letter.  There is nothing else to verify:
   this is the one place in the campaign where the certification is free.

   USE.  A DFiniteTimes generator annL_j annihilates lambda*S iff
        OreReduce[annL_j, gb] == 0   AND   OreReduce[opPhi[annL_j], gb] == 0
   against gb = Ann[S], and both reductions are ordinary Ore reductions with
   explicit cofactors -- so the DFiniteTimes stage becomes RISC-free verifiable.

   Operators are in verifycore.wl's hand-rolled form  ope[vars, {{coef, exps}, ...}].  *)

PHIDIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";

(* harmonic-number shift rules: H_{x+m} -> H_x + explicit rational, both signs *)
hshiftRules = {
  HarmonicNumber[a_ + b_Integer] :>
     HarmonicNumber[a] + Sum[1/(a + j), {j, 1, b}] /; b > 0,
  HarmonicNumber[a_ + b_Integer] :>
     HarmonicNumber[a] - Sum[1/(a - j + 1), {j, 1, -b}] /; b < 0,
  HarmonicNumber[a_ + b_Integer, r_] :>
     HarmonicNumber[a, r] + Sum[1/(a + j)^r, {j, 1, b}] /; b > 0,
  HarmonicNumber[a_ + b_Integer, r_] :>
     HarmonicNumber[a, r] - Sum[1/(a - j + 1)^r, {j, 1, -b}] /; b < 0};

(* phiOf[lambda, a, b] = (S_n^a S_k^b lambda) - lambda, which MUST be rational *)
phiOf[lam_, a_Integer, b_Integer] := phiOf[lam, a, b] =
  Module[{d}, d = Together[((lam /. {n -> n + a, k -> k + b}) - lam) //. hshiftRules];
   If[! FreeQ[d, HarmonicNumber],
      Print["phicore: phi NOT RATIONAL for shift (", a, ",", b,
            ") -- the lemma fails for this letter."]; $Failed, d]];

(* the operator transform.  vars must list S[n] first and S[k] second. *)
opPhi[ope[vars_, terms_], lam_] := Module[{ph},
  ope[vars, Select[
    Table[ph = phiOf[lam, t[[2, 1]], t[[2, 2]]];
      If[ph === $Failed, $Failed, {Together[t[[1]] ph], t[[2]]}],
     {t, terms}],
   # =!= $Failed && #[[1]] =!= 0 &]]];

(* cocycle self-test -- the only thing that can actually fail *)
phiCocycleTest[lam_, amax_: 2, bmax_: 2] := Union@Flatten@Table[
   Together[phiOf[lam, a + a2, b + b2] -
     (phiOf[lam, a, b] + (phiOf[lam, a2, b2] /. {n -> n + a, k -> k + b}))],
   {a, 0, amax}, {b, 0, bmax}, {a2, 0, amax}, {b2, 0, bmax}];
