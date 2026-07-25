(* certZ.wl -- FINAL ASSEMBLY for Theorem B, in the corrected (Abel) form of
   PHASE2_CERTS section 9.2 and the rank-3 form of section 11.

       E(v)/T = c0 + beta*A2(k) + alpha*Psi ,   Psi = A1(k)+3B1(k)+(3/2)C1+(1/2)A1(l).

   Input:  U_alpha.m, U_beta.m, U_c0.m           (certU / certUb : telescopers)
           alpha_rhosigma.m, beta_rhosigma.m, c0_rhosigma.m   (certX : certificates)
   Steps:
     1  M    = LCLM(M_c0, M_beta, M_alpha)                       (order D)
     2  P_m  with  P_m ** M_m == M                               (OreReduce cofactors)
     3  Xhat_m = (P_m . (rho_m e_m T)) / T   and  Yhat_m likewise (rational functions)
        -- these are the certificates of M itself, since Delta_k, Delta_l commute with P_m
     4  R = G/T  with the ABEL corrections included (this is the step section 5.3 omitted)
     5  N = a rank-1 telescoper for the hypergeometric term  G = R*T
     6  L' = N ** M   annihilates  F_n = sum_{k,l} E(v);  F_n = 0 is known exactly for
        n <= 147 (seqdata150.json), so ord(L') <= 147 with a leading coefficient without
        integer roots in range closes Theorem B.

   Run:  math < certZ.wl                                                              *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf = OpenWrite[DIR <> "certZ.log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

TT = Binomial[n + k, n] Binomial[n, k]^2 Binomial[n + l, n] Binomial[n, l]^2 *
     Binomial[n + k + l, n];
{c0, alpha, beta, gamma, delta, eps} = Get[DIR <> "Eletters.m"];
log["section 11 ratio assertion (must be {3, 3/2, 1/2}): ",
    ToString[InputForm[Together /@ {gamma/alpha, delta/alpha, eps/alpha}]]];
emap = <|"c0" -> c0, "beta" -> beta, "alpha" -> alpha|>;
algn = OreAlgebra[S[n]];
labs = {"c0", "beta", "alpha"};

ordOf[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]];
   Max[Join[{0}, Cases[ap, FF[n + a_.] :> a, Infinity]]]];
coefsOf[c_] := Module[{ap, d}, ap = ApplyOreOperator[c, FF[n]]; d = ordOf[c];
   Table[Together[Coefficient[ap, FF[n + j]]], {j, 0, d}]];

(* ---------- 1. the telescopers and the LCLM ---------- *)
Ms = <||>; RS = <||>;
Do[Module[{u, rs},
   If[! FileExistsQ[DIR <> "U_" <> lb <> ".m"], log["MISSING U_", lb, ".m"]; Abort[]];
   If[! FileExistsQ[DIR <> lb <> "_rhosigma.m"],
      log["MISSING ", lb, "_rhosigma.m (run certX.wl first)"]; Abort[]];
   u = Get[DIR <> "U_" <> lb <> ".m"];
   Ms[lb] = u[[4, 1, 1]];
   RS[lb] = Get[DIR <> lb <> "_rhosigma.m"];
   log[lb, " : telescoper order ", ordOf[Ms[lb]]]],
 {lb, labs}];

MM = Ms["c0"];
Do[MM = LCLM[MM, Ms[lb]];
   log["LCLM after ", lb, " : order ", ordOf[MM], " LeafCount ", LeafCount[MM]],
 {lb, {"beta", "alpha"}}];
Put[MM, DIR <> "Z_M.m"];
DD = ordOf[MM];
log["*** M = LCLM, order ", DD, " ***"];
Mc = coefsOf[MM];

(* ---------- 2. right cofactors  P_m ** M_m == M ---------- *)
Pm = <||>;
Do[Module[{red},
   red = OreReduce[MM, {Ms[lb]}, Extended -> True];
   If[red[[1]] =!= 0 && ! (Head[red[[1]]] === OrePolynomial && red[[1]][[1]] === {}),
      log["WARNING cofactor remainder for ", lb, " : ", ToString[Short[red[[1]], 1]]]];
   Pm[lb] = red[[3, 1]] / red[[2]];
   log["cofactor ", lb, " : order ", ordOf[red[[3, 1]]], "  ff=",
       ToString[InputForm[red[[2]]]]]],
 {lb, labs}];
Put[Pm, DIR <> "Z_cof.m"];

(* ---------- 3. certificates of M itself ---------- *)
tr[a_, b_, c_] := tr[a, b, c] =
   Together[FunctionExpand[(TT /. {n -> n + a, k -> k + b, l -> l + c})/TT]];
Xh = <||>; Yh = <||>;
Do[Module[{rr, ss, em},
   {_, rr, ss} = RS[lb]; em = emap[lb];
   Xh[lb] = Together[FunctionExpand[
      ApplyOreOperator[Pm[lb], rr em TT]/TT]];
   Yh[lb] = Together[FunctionExpand[
      ApplyOreOperator[Pm[lb], ss em TT]/TT]];
   log["Xhat/Yhat ", lb, " LeafCount ", LeafCount[Xh[lb]], " / ", LeafCount[Yh[lb]]]],
 {lb, labs}];
Put[{Xh, Yh}, DIR <> "Z_XY.m"];

(* ---------- 4. the Abel-corrected hypergeometric remainder  R = G/T ---------- *)
dkA2 = 1/(n + k + 1)^2 - 1/(k + 1)^2;
dlA2 = 0;
dkPsi = ((1/(n + k + 1) - 1/(k + 1)) + 3 (-1/(n - k) - 1/(k + 1))
       + (3/2) (1/(n + k + l + 1) - 1/(k + l + 1)));
dlPsi = ((3/2) (1/(n + k + l + 1) - 1/(k + l + 1))
       + (1/2) (1/(n + l + 1) - 1/(l + 1)));
dnA2[j_] := Sum[1/(n + i + k)^2, {i, 1, j}];
dnPsi[j_] := Sum[1/(n + i + k) + 3/(n + i - k) + (3/2)/(n + i + k + l)
                 + (1/2)/(n + i + l), {i, 1, j}];

RR = Together[
   - ( dkA2 (Xh["beta"] /. k -> k + 1) + dkPsi (Xh["alpha"] /. k -> k + 1) ) tr[0, 1, 0]
   - ( dlA2 (Yh["beta"] /. l -> l + 1) + dlPsi (Yh["alpha"] /. l -> l + 1) ) tr[0, 0, 1]
   + Sum[Mc[[j + 1]] tr[j, 0, 0] (
        (beta /. n -> n + j) dnA2[j] + (alpha /. n -> n + j) dnPsi[j]), {j, 0, DD}]];
log["R = G/T LeafCount ", LeafCount[RR]];
Put[RR, DIR <> "Z_R.m"];

(* ---------- 5. a rank-1 telescoper for G = R*T ---------- *)
t0 = AbsoluteTime[];
annG = Annihilator[RR TT, {S[n], S[k], S[l]}];
log["Annihilator[G] #", Length[annG], " t=", Round[AbsoluteTime[] - t0], "s ", DateString[]];
Put[annG, DIR <> "Z_annG.m"];
t0 = AbsoluteTime[];
ct1G = CreativeTelescoping[annG, S[k] - 1, {S[n], S[l]}];
log["ct1[G] #", Length[ct1G[[1]]], " t=", Round[AbsoluteTime[] - t0], "s ", DateString[]];
Put[ct1G, DIR <> "Z_ct1G.m"];
t0 = AbsoluteTime[];
gbG = OreGroebnerBasis[ct1G[[1]], OreAlgebra[S[n], S[l]]];
log["gb[G] #", Length[gbG], " t=", Round[AbsoluteTime[] - t0], "s gb===ct1? ",
    ToString[gbG === ct1G[[1]]]];
Put[gbG, DIR <> "Z_gbG.m"];
NN = $Failed;
Do[Module[{supp, r},
   supp = Table[S[n]^i, {i, 0, d}];
   t0 = AbsoluteTime[];
   r = Quiet[Check[CreativeTelescoping[gbG, S[l] - 1, {}, Support -> supp], $Failed]];
   log["ct2[G] Support d=", d, " t=", Round[AbsoluteTime[] - t0], "s -> ",
       If[Head[r] === List && Length[r] >= 1 && Length[r[[1]]] >= 1,
          "FOUND order " <> ToString[ordOf[r[[1, 1]]]], "none"], "  ", DateString[]];
   If[Head[r] === List && Length[r] >= 1 && Length[r[[1]]] >= 1,
      NN = r; Put[r, DIR <> "Z_ct2G.m"]; Break[]]],
 {d, 0, 12}];

(* ---------- 6. the final operator ---------- *)
If[NN =!= $Failed,
  Module[{LP},
   LP = NN[[1, 1]] ** MM;
   log["*** FINAL OPERATOR  L' = N ** M : order ", ordOf[LP], " ***"];
   log["    ord(N) = ", ordOf[NN[[1, 1]]], "   ord(M) = ", DD];
   log["    order budget: F_n = 0 known exactly for n <= 147 (seqdata150.json)"];
   log["    leading coefficient = ", ToString[InputForm[Last[coefsOf[LP]]]]];
   Put[LP, DIR <> "Z_Lfinal.m"]],
  log["no telescoper N found for G up to d = 12"]];

log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
