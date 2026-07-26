(* z5phi.wl -- transport a RISC certificate to the POLE-FREE base Phi and emit the
   J polynomial identities that LEAN_Z5_SCAFFOLD section S5 asks for.  Loads NO RISC package.

   Input : z5_<TAG>_rhosigma.m  =  {ffop, Lop, RRop, sigop}   (hand-rolled ope[] form,
           written by z5ver.wl), meaning       ff*L.F = Delta_k(-RR.F) + Delta_l(-sigma.F)
   Output: z5_<TAG>_phicert.m   =  <| "M"->basis, "r"->r_i, "s"->s_i, ... |>
           with   R_w = Phi * Sum_i r_i M_i ,  S_w = Phi * Sum_i s_i M_i .

   The key fact that makes the transport cure the interior poles:
     R_w / Phi  =  Sum_j rho_j(n,k,l) * P_0(n,k,l) * ( T(n+j,k,l)/T(n,k,l) ) * w(n+j,k,l)
                =  P_0 * Sum_j rho_j * Wr[j,0,0]
   and  P_0 = [(n+1-k)(n+2-k)(n+3-k)]^2 [(n+1-l)(n+2-l)(n+3-l)]^2  has DOUBLE zeros at
   exactly the interior points k,l = n+1,n+2,n+3 where the T-base cofactors have poles.

   Run: TAG=w3_lk KER=w3 math < z5phi.wl                                              *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/z5cf/";
gets[v_, d_] := Module[{x = Environment[v]}, If[x === $Failed, d, x]];
TAG = gets["TAG", "w3_lk"]; KER = gets["KER", "w3"];
lf = OpenWrite[DIR <> "z5phi_" <> TAG <> ".log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], " TAG=", TAG, " KER=", KER];
Get[DIR <> "z5core.wl"];
log["z5core loaded (NO RISC package in this kernel)"];
ker = Switch[KER, "w3", W3r, "w5", W5r, _, W3r];

P0 = ((n + 1 - k) (n + 2 - k) (n + 3 - k))^2 ((n + 1 - l) (n + 2 - l) (n + 3 - l))^2;
Pi[i_] := Product[(n + j) (n + k + j) (n + l + j) (n + k + l + j), {j, 1, i}] Product[n + j - k, {j, i + 1, 3}]^2 Product[n + j - l, {j, i + 1, 3}]^2;
log["P_i degrees (must all be 12): ", ToString[Table[Exponent[Expand[Pi[i]], {n, k, l}] // Total, {i, 0, 3}]]];
log["P_0 == Pi[0] ? ", ToString[Expand[P0 - Pi[0]] === 0]];

{ffop, Lop, RRop, sigop} = Get[DIR <> "z5_" <> TAG <> "_rhosigma.m"];
log["loaded rhosigma: ff terms ", Length[ffop[[2]]], "  L terms ", Length[Lop[[2]]], "  RR terms ", Length[RRop[[2]]], "  sigma terms ", Length[sigop[[2]]]];

(* value of an ope[] applied to the summand, DIVIDED BY Phi(n,k,l) instead of T(n,k,l) *)
overPhi[op_] := Together[P0 applyOpe[op, ker]];
Rw = Together[-overPhi[RRop]];
Sw = Together[-overPhi[sigop]];
log["R_w/Phi LeafCount ", LeafCount[Rw], "   S_w/Phi LeafCount ", LeafCount[Sw]];

basis = Union[hvars[Rw], hvars[Sw]];
log["letter basis size J = ", Length[basis]];
coeffs[e_] := Module[{cr = CoefficientRules[Expand[e], basis]}, Association[Table[(Times @@ (basis^c[[1]])) -> Together[c[[2]]], {c, cr}]]];
rc = coeffs[Rw]; sc = coeffs[Sw];
log["R_w has ", Length[rc], " nonzero letter monomials; S_w has ", Length[sc]];

(* --- pole audit: no denominator may vanish at k or l in {n+1,n+2,n+3} or at k,l = n+4 --- *)
badfac[e_] := Select[FactorList[Denominator[Together[e]]][[All, 1]], (! FreeQ[#, k] || ! FreeQ[#, l]) && Or @@ Table[Together[# /. {k -> n + t}] === 0 || Together[# /. {l -> n + t}] === 0, {t, 1, 4}] &];
bads = DeleteDuplicates[Flatten[{badfac /@ Values[rc], badfac /@ Values[sc]}]];
log["POLE AUDIT at k,l = n+1..n+4 : ", If[bads === {}, "CLEAN -- no cofactor has a pole at an interior or top boundary point", "*** POLES PRESENT: " <> ToString[InputForm[bads]] <> " ***"]];
log["  all denominator factors present: ", ToString[InputForm[DeleteDuplicates[Flatten[FactorList[Denominator[#]][[All, 1]] & /@ Join[Values[rc], Values[sc]]]]]]];

(* --- (B-bot): R_w(n,0,l) = 0 and S_w(n,k,0) = 0 --- *)
b1 = Union[Together[# /. k -> 0] & /@ Values[rc]];
b2 = Union[Together[# /. l -> 0] & /@ Values[sc]];
log["(B-bot) R_w(n,0,l) coefficients all zero ? ", ToString[b1 === {0} || b1 === {}]];
log["(B-bot) S_w(n,k,0) coefficients all zero ? ", ToString[b2 === {0} || b2 === {}]];
If[b1 =!= {0} && b1 =!= {}, log["   nonzero R_w(n,0,l) coeffs: ", Length[DeleteCases[b1, 0]]]];
If[b2 =!= {0} && b2 =!= {}, log["   nonzero S_w(n,k,0) coeffs: ", Length[DeleteCases[b2, 0]]]];

Put[<|"tag" -> TAG, "ker" -> KER, "basis" -> basis, "r" -> rc, "s" -> sc, "P0" -> P0, "Pi" -> Table[Pi[i], {i, 0, 3}]|>, DIR <> "z5_" <> TAG <> "_phicert.m"];
log["written z5_", TAG, "_phicert.m"];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
