(* m2bnd.wl -- M2: exact eps-regularised confirmation of the boundary lemma.

   LOAD WITH  Get["..../m2bnd.wl"]  -- never with  math < m2bnd.wl  (line trap).

   Everything is evaluated at  n = n0 + eps,  k = k0, l = l0 integers, and each
   HarmonicNumber is rewritten with ONLY  H^(r)_{x+1} = H^(r)_x + (x+1)^-r  into
      hs[r] ( = H^(r)_{n0+eps}, analytic )  +  explicit rational function of eps.
   hs[r] is then expanded as  hv[r] + sum_m dd[r,m] eps^m  with hv, dd free
   symbols, so a vanishing result is an identity in the Taylor data of H^(r),
   not a numerical coincidence.

   E(v) = sum_{j=0}^{3} c_j W(n+j,k,l)
          - rho(n,k+1,l) W(n,k+1,l) + rho(n,k,l) W(n,k,l)
          - sig(n,k,l+1) W(n,k,l+1) + sig(n,k,l) W(n,k,l),      W = T v.
*)

DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf = OpenWrite[DIR <> "m2bnd.log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]);
log["START ", DateString[]];

{rho, sigma} = Get[DIR <> "Qrow_rhosigma.m"];
log["rho,sigma LeafCount ", ToString[LeafCount /@ {rho, sigma}]];
log["denom(rho) = ", ToString[InputForm[FactorList[Denominator[Together[rho]]][[All, {1, 2}]]]]];
log["denom(sig) = ", ToString[InputForm[FactorList[Denominator[Together[sigma]]][[All, {1, 2}]]]]];

a0f[x_] := 41218 x^3 + 198849 x^2 + 320790 x + 173057;
B8f[x_] := 3874492 x^8 + 59373972 x^7 + 394148190 x^6 + 1481084196 x^5 +
   3447878810 x^4 + 5095855458 x^3 + 4673546679 x^2 + 2433871008 x + 551502039;
B9f[x_] := 48802112 x^9 + 967468896 x^8 + 8488000862 x^7 + 43246197636 x^6 +
   140983768422 x^5 + 304912330849 x^4 + 437406946975 x^3 + 401272692378 x^2 +
   213593890911 x + 50257929339;
LBZc[x_] := {(x + 1)^5 (x + 2) a0f[x + 1], -2 (x + 2) B8f[x], -2 B9f[x],
   2 (x + 3)^5 (2 x + 5) a0f[x]};

(* ---- harmonic normalisation relative to hs[r] = H^(r)_{nn}, nn = n0+eps ---- *)
hgen[a_Integer, r_] := hs[r] +
   If[a >= 0, Sum[1/(nn + i)^r, {i, 1, a}], -Sum[1/(nn - i)^r, {i, 0, -a - 1}]];

(* v(n+j, k0, l0) *)
vAt[j_Integer, k0_Integer, l0_Integer] :=
  Module[{A3k, A2k, A1k, B1k, C1, A1l},
   A3k = hgen[j + k0, 3] - HarmonicNumber[k0, 3];
   A2k = hgen[j + k0, 2] - HarmonicNumber[k0, 2];
   A1k = hgen[j + k0, 1] - HarmonicNumber[k0, 1];
   B1k = hgen[j - k0, 1] - HarmonicNumber[k0, 1];
   C1  = hgen[j + k0 + l0, 1] - HarmonicNumber[k0 + l0, 1];
   A1l = hgen[j + l0, 1] - HarmonicNumber[l0, 1];
   hgen[j, 3] + 2 A3k - (1/2) A2k A1k - (3/2) A2k B1k - (3/4) A2k C1 -
    (1/4) A2k A1l];

(* T(n+j, k0, l0) as a POLYNOMIAL in nn *)
Tp[j_Integer, k0_Integer, l0_Integer] :=
  Pochhammer[nn + j + 1, k0] Pochhammer[nn + j + 1, l0] *
   Pochhammer[nn + j + 1, k0 + l0] Pochhammer[nn + j - k0 + 1, k0]^2 *
   Pochhammer[nn + j - l0 + 1, l0]^2 / (k0!^3 l0!^3 (k0 + l0)!);

Wf[j_Integer, k0_Integer, l0_Integer] := Tp[j, k0, l0] vAt[j, k0, l0];

Ecell[k0_Integer, l0_Integer] :=
  Sum[LBZc[nn][[j + 1]] Wf[j, k0, l0], {j, 0, 3}] -
   rhoAt[k0 + 1, l0] Wf[0, k0 + 1, l0] + rhoAt[k0, l0] Wf[0, k0, l0] -
   sigAt[k0, l0 + 1] Wf[0, k0, l0 + 1] + sigAt[k0, l0] Wf[0, k0, l0];

NEGMIN = -10;
hexp[r_] := hv[r] + Sum[dd[r, m] eps^m, {m, 1, 4}];

cellData[k0_Integer, l0_Integer] :=
  Module[{ser, neg, val},
   ser = Series[Ecell[k0, l0] /. hs[r_] :> hexp[r], {eps, 0, 0}];
   neg = Table[Together[SeriesCoefficient[ser, {eps, 0, m}]], {m, NEGMIN, -1}];
   val = Together[SeriesCoefficient[ser, {eps, 0, 0}]];
   {neg, val}];

runN[n0_Integer] :=
  Module[{K, cells, negs, vals, tneg, tval, ddv, sing, drop, t0},
   t0 = AbsoluteTime[];
   nn = n0 + eps;
   Clear[rhoAt, sigAt];
   rhoAt[a_, b_] := rhoAt[a, b] = Together[rho /. {n -> nn, k -> a, l -> b}];
   sigAt[a_, b_] := sigAt[a, b] = Together[sigma /. {n -> nn, k -> a, l -> b}];
   K = n0 + 3;
   log["=== n0 = ", n0, ", box [0,", K, "]^2 , ", (K + 1)^2, " cells ==="];
   cells = Flatten[Table[{k0, l0}, {k0, 0, K}, {l0, 0, K}], 1];
   negs = {}; vals = {}; sing = {};
   Do[Module[{cd = cellData[c[[1]], c[[2]]]},
      AppendTo[negs, cd[[1]]]; AppendTo[vals, cd[[2]]];
      If[Union[cd[[1]]] =!= {0},
       AppendTo[sing, {c, NEGMIN - 1 +
          First[Flatten[Position[cd[[1]], x_ /; x =!= 0, {1},
             Heads -> False]]]}]]],
    {c, cells}];
   tneg = Together /@ Total[negs];
   tval = Expand[Total[vals]];
   ddv = Union[Cases[tval, dd[_, _], Infinity]];
   drop = Expand[tval - (tval /. Thread[ddv -> 0])];
   log["  cells with a nonzero negative eps-power: ", Length[sing], " of ", Length[cells]];
   If[sing =!= {}, log["    (cell, leading eps exponent): ",
      ToString[InputForm[sing]]]];
   log["  TOTAL negative eps-coefficients (must all be 0): ",
    ToString[InputForm[Union[tneg]]]];
   log["  TOTAL eps^0: dd-symbols present in the total: ", ToString[InputForm[ddv]]];
   log["  TOTAL eps^0: dd-dependent part (must be 0): ", ToString[InputForm[Together[drop]]]];
   log["  TOTAL eps^0 with hv[r] -> H^(r)_", n0, " : ",
    ToString[InputForm[
      Together[(tval /. Thread[ddv -> 0]) /. hv[r_] :> HarmonicNumber[n0, r]]]]];
   log["  as a POLYNOMIAL in hv (before substituting): ",
    ToString[InputForm[Together[tval /. Thread[ddv -> 0]]]]];
   log["  time ", Round[AbsoluteTime[] - t0], " s   ", DateString[]];
   {n0, Length[sing], Union[tneg],
    Together[(tval /. Thread[ddv -> 0]) /. hv[r_] :> HarmonicNumber[n0, r]]}];

RES = Table[runN[n0], {n0, NLIST}];
log["RESULT ", ToString[InputForm[RES]]];
log["ALL DONE ", DateString[]];
Close[lf];
RES
