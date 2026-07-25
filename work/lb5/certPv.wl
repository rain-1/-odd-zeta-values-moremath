(* certPv.wl -- RISC-FREE exact verification of the tau-split certificate chain.

   Loads NO RISC package; everything is rebuilt by verifycore.wl (Gamma-shift
   calculus tratio, harmonic normaliser hnorm, hh-symbols as indeterminates).

   V-0a  Sum_tau F_tau / T  ==  E(v)/T in the certified letter form of Eletters.m
         -- SYMBOLIC (not just at integer points), so the tau split is exact.
   V-0b  the letter form == the independently stored canonical 9-symbol Ecanon.m
   V-1   per tau:  M . F_tau = Delta_k( Xhat_tau . F_tau ) + Delta_l( Yhat_tau . F_tau )
   V-2   boundary: Sum_tau (Xhat_tau . F_tau)|_{k=0}  and  Sum_tau (Yhat_tau . F_tau)|_{l=0}
   V-3   denominator factors of the boundary data

   V-0a + V-1 summed over tau give   M . E(v) = Delta_k(...) + Delta_l(...),
   and with V-2 (plus T's double zeros at the far edge)  M . F_n = 0,
   F_n = Sum_{k,l} E(v).

   Run:  math < certPv.wl                                                          *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
$HistoryLength = 0;
Get[DIR <> "verifycore.wl"];
lf = OpenWrite[DIR <> "certPv.log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], "   RISC absent: ",
    ToString[Names["HolonomicFunctions`*"] === {}]];

AA[r_, x_] := HarmonicNumber[n + x, r] - HarmonicNumber[x, r];
BB[r_, x_] := HarmonicNumber[n - x, r] - HarmonicNumber[x, r];
CC1 = HarmonicNumber[n + k + l] - HarmonicNumber[k + l];
A2k = AA[2, k];
Psi = (AA[1, k] + 3 BB[1, k] + (3/2) CC1 + (1/2) AA[1, l]);
log["HarmonicNumber counts A2k/Psi (must be 2/8): ",
    Length[Cases[A2k, HarmonicNumber[__], Infinity]], "/",
    Length[Cases[Psi, HarmonicNumber[__], Infinity]]];

a0[x_] := 41218 x^3 + 198849 x^2 + 320790 x + 173057;
B8[x_] := 3874492 x^8 + 59373972 x^7 + 394148190 x^6 + 1481084196 x^5 +
   3447878810 x^4 + 5095855458 x^3 + 4673546679 x^2 + 2433871008 x + 551502039;
B9[x_] := 48802112 x^9 + 967468896 x^8 + 8488000862 x^7 + 43246197636 x^6 +
   140983768422 x^5 + 304912330849 x^4 + 437406946975 x^3 + 401272692378 x^2 +
   213593890911 x + 50257929339;
cc3 = {(n + 1)^5 (n + 2) a0[n + 1], -2 (n + 2) B8[n], -2 B9[n],
       2 (n + 3)^5 (2 n + 5) a0[n]};
{rho, sigma} = Get[DIR <> "Qrow_rhosigma.m"];
log["rho,sigma loaded ", LeafCount[rho], " ", LeafCount[sigma]];

sumi[e_, j_] := Sum[e, {i, 1, j}];
tauNQ[tau_] := MemberQ[{"n1", "n2", "n3"}, tau];
tauJf[tau_] := Which[tau === "n1", 1, tau === "n2", 2, tau === "n3", 3, True, 0];
(* prefactor u_tau and the T-shift s_tau with  W_tau = u_tau * T(n+s1,k+s2,l+s3) *)
uf[tau_] := Which[
   tauNQ[tau], cc3[[tauJf[tau] + 1]],
   tau === "kk", -(rho /. k -> k + 1),
   True, -(sigma /. l -> l + 1)];
sf[tau_] := Which[
   tauNQ[tau], {tauJf[tau], 0, 0},
   tau === "kk", {0, 1, 0},
   True, {0, 0, 1}];
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

shx[e_, a_, b_, c_] := e /. {n -> n + a, k -> k + b, l -> l + c};
(* Erx[tau][a,b,c] = F_tau(n+a,k+b,l+c) / T(n,k,l) *)
Erx[tau_] := Erx[tau] = Module[{u = uf[tau], s = sf[tau], st = stuff[tau]},
   Function[{a, b, c}, Expand[shx[u, a, b, c] *
      tratio[a + s[[1]], b + s[[2]], c + s[[3]]] hnorm[shx[st, a, b, c]]]]];
alltau = {"n1", "n2", "n3", "kk", "ll"};

(* ---------- V-0 ---------- *)
{c0L, alphaL, betaL, gammaL, deltaL, epsL} = Get[DIR <> "Eletters.m"];
log["rank-3 ratio assertion (must be {3, 3/2, 1/2}): ",
    ToString[InputForm[Together /@ {gammaL/alphaL, deltaL/alphaL, epsL/alphaL}]]];
base3 = c0L + betaL A2k + alphaL Psi;
Er3[a_, b_, c_] := Er3[a, b, c] = Expand[tratio[a, b, c] hnorm[shx[base3, a, b, c]]];
sumtau0 = Total[Table[Erx[tau][0, 0, 0], {tau, alltau}]];
log["V-0a ", ToString[zeroReport["Sum_tau F_tau/T - E(v)/T (letter form)",
     sumtau0 - Er3[0, 0, 0]]]];
log["V-0b loadEcanon ", ToString[loadEcanon[DIR <> "Ecanon.m"]]];
log["V-0b ", ToString[zeroReport["letter form - Ecanon", Er3[0, 0, 0] - Er[0, 0, 0]]]];

(* ---------- the certificate ---------- *)
applyOpe[ope[vars_, ts_], ker_, extra_] := Total[Table[
   Module[{co = t[[1]], ex = t[[2]], sh},
     sh = ex + extra;
     Expand[shx[co, extra[[1]], extra[[2]], extra[[3]]] (ker @@ sh)]],
   {t, ts}]];

If[! FileExistsQ[DIR <> "P_cert.m"],
   log["MISSING P_cert.m (run certPy.wl first)"]; Close[lf]; Exit[]];
{cf, XY} = Get[DIR <> "P_cert.m"];
dM = Length[cf] - 1;
log["telescoper order ", dM, "   taus in certificate: ",
    ToString[XY[[All, 1]]]];

(* ---------- V-1, per tau ---------- *)
Xk0T = 0; Yl0T = 0;
Do[Module[{tau = XY[[i, 1]], Xo = XY[[i, 2]], Yo = XY[[i, 3]], ker, L, x0, x1, y0, y1},
   ker = Erx[tau];
   L = Sum[cf[[j + 1]] ker[j, 0, 0], {j, 0, dM}];
   x0 = applyOpe[Xo, ker, {0, 0, 0}]; x1 = applyOpe[Xo, ker, {0, 1, 0}];
   y0 = applyOpe[Yo, ker, {0, 0, 0}]; y1 = applyOpe[Yo, ker, {0, 0, 1}];
   log["V-1 ", ToString[zeroReport[
      "M.F_" <> tau <> " - Delta_k(Xhat.F) - Delta_l(Yhat.F)",
      L - (x1 - x0) - (y1 - y0)]]];
   Xk0T = Xk0T + x0; Yl0T = Yl0T + y0],
 {i, Length[XY]}];

(* ---------- V-2 boundary ---------- *)
setk0[e_] := Together[(e /. hh[{a_, b_, c_}, r_] :>
     If[{a, c} === {0, 0}, 0, hh[{a, 0, c}, r]]) /. k -> 0];
setl0[e_] := Together[(e /. hh[{a_, b_, c_}, r_] :>
     If[{a, b} === {0, 0}, 0, hh[{a, b, 0}, r]]) /. l -> 0];
log["V-2 ", ToString[zeroReport["Sum_tau (Xhat.F_tau)/T at k=0", setk0[Xk0T]]]];
log["V-2 ", ToString[zeroReport["Sum_tau (Yhat.F_tau)/T at l=0", setl0[Yl0T]]]];

(* ---------- V-3 ---------- *)
dens[e_] := Union[Flatten[{FactorList[Denominator[Together[#]]][[All, {1, 2}]] & /@
   If[hvars[e] === {}, {e}, Union[Flatten[{CoefficientList[Expand[e], hvars[e]]}]]]}, 1]];
log["V-3 denom factors of Sum_tau Xhat.F_tau : ",
    ToString[InputForm[Union[DeleteCases[dens[Xk0T], {_?NumberQ, _}]]]]];
log["V-3 denom factors of Sum_tau Yhat.F_tau : ",
    ToString[InputForm[Union[DeleteCases[dens[Yl0T], {_?NumberQ, _}]]]]];

log["ALL DONE ", DateString[]];
Close[lf];
