(* verifycore.wl -- INDEPENDENT exact verification kernel for the LB5 CT certificates.

   Loads NO RISC package.  It reads the saved OrePolynomial expressions purely as
   inert data (their internal list form) and re-does all arithmetic from scratch:

     * T(n+a,k+b,l+c)/T(n,k,l)  from the Gamma-product form of T, expanded by hand
       into a rational function via  grat[x,d] = Gamma[x+d]/Gamma[x];
     * every HarmonicNumber[u,r] is rewritten, using ONLY the defining recurrence
       H^(r)_{x+1} = H^(r)_x + 1/(x+1)^r, as  hh[base,r] + explicit rational,
       where base is one of the nine linear forms n+k, k, n-k, n+l, l, n-l,
       n+k+l, k+l, n; the hh[.,.] are then treated as independent indeterminates.

   An identity that reduces to 0 in Q(n,k,l)[hh...] is therefore an identity of
   functions wherever the harmonic numbers are defined.
*)

(* ---------- Gamma ratio: grat[x,d] = Gamma[x+d]/Gamma[x], d an integer ---------- *)
grat[x_, d_Integer] := Which[
  d == 0, 1,
  d > 0, Product[x + i, {i, 0, d - 1}],
  True, 1/Product[x - i, {i, 1, -d}]];

(* ---------- T(n+a,k+b,l+c)/T(n,k,l) ----------
   T = G[n+k+1] G[n+l+1] G[n+k+l+1] G[n+1] /
       ( G[k+1]^3 G[n-k+1]^2 G[l+1]^3 G[n-l+1]^2 G[k+l+1] )                      *)
tratio[a_, b_, c_] := tratio[a, b, c] = Together[
  grat[n + k + 1, a + b] grat[n + l + 1, a + c] grat[n + k + l + 1, a + b + c] grat[n + 1, a] /
  (grat[k + 1, b]^3 grat[n - k + 1, a - b]^2 grat[l + 1, c]^3 grat[n - l + 1, a - c]^2 *
   grat[k + l + 1, b + c])];

(* ---------- harmonic-number normalisation ---------- *)
bases = {{1, 1, 0} -> n + k, {0, 1, 0} -> k, {1, -1, 0} -> n - k,
         {1, 0, 1} -> n + l, {0, 0, 1} -> l, {1, 0, -1} -> n - l,
         {1, 1, 1} -> n + k + l, {0, 1, 1} -> k + l, {1, 0, 0} -> n};
baserule = Association[bases];

shiftsum[x_, d_Integer, r_] := Which[
  d == 0, 0,
  d > 0, Sum[1/(x + i)^r, {i, 1, d}],
  True, -Sum[1/(x - i)^r, {i, 0, -d - 1}]];

hnorm1[u_, r_] := Module[{cn, ck, cl, d, key, x},
  cn = Coefficient[u, n]; ck = Coefficient[u, k]; cl = Coefficient[u, l];
  d = Expand[u - cn n - ck k - cl l];
  key = {cn, ck, cl};
  If[! IntegerQ[d] || ! KeyExistsQ[baserule, key],
     Print["hnorm1: UNRECOGNISED harmonic argument ", u]; Abort[]];
  x = baserule[key];
  hh[key, r] + shiftsum[x, d, r]];

hnorm[e_] := e /. {HarmonicNumber[u_, r_] :> hnorm1[u, r],
                   HarmonicNumber[u_] :> hnorm1[u, 1]};

(* ---------- the weight-3 harmonic weight, shifted ---------- *)
AAf[r_, x_, nn_] := HarmonicNumber[nn + x, r] - HarmonicNumber[x, r];
BBf[r_, x_, nn_] := HarmonicNumber[nn - x, r] - HarmonicNumber[x, r];
w3hatAt[a_, b_, c_] := Module[{nn = n + a, kk = k + b, ll = l + c},
  HarmonicNumber[nn, 3] + AAf[3, kk, nn] + AAf[3, ll, nn]
  - (1/4) (AAf[2, kk, nn] AAf[1, kk, nn] + AAf[2, ll, nn] AAf[1, ll, nn])
  - (3/4) (AAf[2, kk, nn] BBf[1, kk, nn] + AAf[2, ll, nn] BBf[1, ll, nn])
  - (3/8) (AAf[2, kk, nn] + AAf[2, ll, nn]) (HarmonicNumber[nn + kk + ll] - HarmonicNumber[kk + ll])
  - (1/8) (AAf[2, kk, nn] AAf[1, ll, nn] + AAf[2, ll, nn] AAf[1, kk, nn])];

(* Wr[a,b,c] = W(n+a,k+b,l+c)/T(n,k,l),  W = T*w3hat, in hh-symbols *)
Wr[a_, b_, c_] := Wr[a, b, c] = Expand[tratio[a, b, c] hnorm[w3hatAt[a, b, c]]];

(* Q-row: only the T factor *)
Qr[a_, b_, c_] := tratio[a, b, c];

(* ---------- inert reading of an OrePolynomial ---------- *)
(* OrePolynomial[{{coef,{e1,..}},...}, OreAlgebraObject[{S[..],..},...], order] *)
opTerms[p_] := p[[1]];
opVars[p_] := p[[2, 1]];

(* apply operator p (in variables vars, a permutation of {S[n],S[k],S[l]} or a subset)
   to the "kernel function" ker, where ker[a,b,c] is the value of the function at
   (n+a,k+b,l+c) divided by T(n,k,l).  extra = {da,db,dc} a global pre-shift.       *)
applyOp[p_, ker_, extra_: {0, 0, 0}] := Module[{vars, terms, slot},
  vars = opVars[p];
  slot = {S[n], S[k], S[l]} /. Thread[vars -> Range[Length[vars]]];
  Total[Table[
    Module[{co = t[[1]], ex = t[[2]], sh},
      sh = Table[If[IntegerQ[slot[[i]]], ex[[slot[[i]]]], 0], {i, 3}] + extra;
      Expand[(co /. {n -> n + extra[[1]], k -> k + extra[[2]], l -> l + extra[[3]]}) *
             ker @@ sh]],
    {t, opTerms[p]}]]];

(* ---------- zero test ---------- *)
hvars[e_] := Union[Cases[e, hh[_, _], Infinity]];
zeroQ[e_] := Module[{hv, cl, bad},
  hv = hvars[e];
  cl = If[hv === {}, {Together[e]}, Union[Flatten[{CoefficientList[Expand[e], hv]}]]];
  bad = Select[Together /@ cl, # =!= 0 &];
  bad === {}];
zeroReport[lab_, e_] := Module[{hv, cl, bad, nb},
  hv = hvars[e];
  cl = If[hv === {}, {Together[e]}, Union[Flatten[{CoefficientList[Expand[e], hv]}]]];
  bad = Select[Together /@ cl, # =!= 0 &];
  nb = Length[bad];
  {lab, Length[hv], Length[cl], nb, If[nb > 0, Short[First[bad], 3], "OK"]}];

(* ================= hand-rolled Ore algebra (RISC-free) =================
   An operator is  ope[vars, {{coef, expvec}, ...}]  where vars is a list of
   shift generators S[x] and expvec the matching exponent vector; the base
   variables are the x's.  Commutation:  S[x] * f(x) = f(x+1) * S[x].       *)

opShift[c_, vars_, e_] := Module[{bv = vars /. S[x_] :> x},
   c /. MapThread[Rule, {bv, bv + e}]];

opNorm[ope[vars_, ts_]] := Module[{g},
  g = GatherBy[ts, Last];
  ope[vars, DeleteCases[
    {Together[Total[#[[All, 1]]]], #[[1, 2]]} & /@ g, {0, _}]]];

opPlus[ope[v_, a_], ope[v_, b_]] := opNorm[ope[v, Join[a, b]]];
opTimes[ope[v_, a_], ope[v_, b_]] := opNorm[ope[v,
   Flatten[Table[{Together[t1[[1]] opShift[t2[[1]], v, t1[[2]]]], t1[[2]] + t2[[2]]},
                 {t1, a}, {t2, b}], 1]]];
opScal[c_, ope[v_, a_]] := opNorm[ope[v, {Together[c #[[1]]], #[[2]]} & /@ a]];
opZeroQ[ope[v_, a_]] := (opNorm[ope[v, a]][[2]] === {});

(* convert a saved OrePolynomial (read inertly) into ope[] over a chosen
   variable list vars; the OrePolynomial's own variables are p[[2,1]].       *)
toOpe[p_, vars_] := Module[{pv, pos, slot},
  pv = p[[2, 1]];
  slot = Table[pos = Position[pv, vars[[i]]];
               If[pos === {}, 0, pos[[1, 1]]], {i, Length[vars]}];
  ope[vars, Table[{t[[1]], Table[If[slot[[i]] === 0, 0, t[[2, slot[[i]]]]],
                                 {i, Length[vars]}]}, {t, p[[1]]}]]];
opOne[vars_] := ope[vars, {{1, Table[0, {Length[vars]}]}}];
opGen[vars_, g_] := ope[vars, {{1, Table[If[vars[[i]] === g, 1, 0], {i, Length[vars]}]}}];

(* ---------- kernel for a canonical-form E, as written by certS.wl ----------
   S_Ecanon.m holds {hvars, cofs, c0} with  E = T * ( c0 + Sum_i cofs[[i]] hvars[[i]] ).
   loadEcanon defines Er[a,b,c] = E(n+a,k+b,l+c) / T(n,k,l) in hh-symbols.        *)
loadEcanon[file_] := Module[{hv, cf, cz, base},
  {hv, cf, cz} = Get[file];
  base = cz + Sum[cf[[i]] hv[[i]], {i, Length[hv]}];
  Clear[Er];
  Er[a_, b_, c_] := Er[a, b, c] = Expand[tratio[a, b, c] *
     hnorm[base /. {n -> n + a, k -> k + b, l -> l + c}]];
  {Length[hv], LeafCount[base]}];
