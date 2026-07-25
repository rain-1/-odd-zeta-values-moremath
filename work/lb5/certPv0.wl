(* certPv0.wl -- the V-0 half of certPv.wl, with no Exit[] and no dependence on the
   telescopers, so it can be Get[] inside the MCP kernel while certP.wl is running.

   V-0a  Sum_tau F_tau / T  ==  E(v)/T = c0 + beta A2(k) + alpha Psi   (Eletters.m)
   V-0b  that letter form   ==  the canonical 9-symbol form            (Ecanon.m)

   Both SYMBOLIC in Q(n,k,l)[hh...], RISC-free (verifycore.wl only).
   Returns {V0a, V0b} zeroReport tuples.                                          *)
DIRP = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
Get[DIRP <> "verifycore.wl"];

AA[r_, x_] := HarmonicNumber[n + x, r] - HarmonicNumber[x, r];
BB[r_, x_] := HarmonicNumber[n - x, r] - HarmonicNumber[x, r];
CC1 = HarmonicNumber[n + k + l] - HarmonicNumber[k + l];
A2k = AA[2, k];
Psi = (AA[1, k] + 3 BB[1, k] + (3/2) CC1 + (1/2) AA[1, l]);
a0[x_] := 41218 x^3 + 198849 x^2 + 320790 x + 173057;
B8[x_] := 3874492 x^8 + 59373972 x^7 + 394148190 x^6 + 1481084196 x^5 +
   3447878810 x^4 + 5095855458 x^3 + 4673546679 x^2 + 2433871008 x + 551502039;
B9[x_] := 48802112 x^9 + 967468896 x^8 + 8488000862 x^7 + 43246197636 x^6 +
   140983768422 x^5 + 304912330849 x^4 + 437406946975 x^3 + 401272692378 x^2 +
   213593890911 x + 50257929339;
cc3 = {(n + 1)^5 (n + 2) a0[n + 1], -2 (n + 2) B8[n], -2 B9[n],
       2 (n + 3)^5 (2 n + 5) a0[n]};
{rho, sigma} = Get[DIRP <> "Qrow_rhosigma.m"];

sumi[e_, j_] := Sum[e, {i, 1, j}];
tauNQ[tau_] := MemberQ[{"n1", "n2", "n3"}, tau];
tauJf[tau_] := Which[tau === "n1", 1, tau === "n2", 2, tau === "n3", 3, True, 0];
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
Erx[tau_] := Erx[tau] = Module[{u = uf[tau], s = sf[tau], st = stuff[tau]},
   Function[{a, b, c}, Expand[shx[u, a, b, c] *
      tratio[a + s[[1]], b + s[[2]], c + s[[3]]] hnorm[shx[st, a, b, c]]]]];
alltau = {"n1", "n2", "n3", "kk", "ll"};

{c0L, alphaL, betaL, gammaL, deltaL, epsL} = Get[DIRP <> "Eletters.m"];
ratio3 = Together /@ {gammaL/alphaL, deltaL/alphaL, epsL/alphaL};
base3 = c0L + betaL A2k + alphaL Psi;
Er3[a_, b_, c_] := Er3[a, b, c] = Expand[tratio[a, b, c] hnorm[shx[base3, a, b, c]]];
V0a = zeroReport["Sum_tau F_tau/T - E(v)/T",
   Total[Table[Erx[tau][0, 0, 0], {tau, alltau}]] - Er3[0, 0, 0]];
V0b = Module[{q = loadEcanon[DIRP <> "Ecanon.m"]},
   {q, zeroReport["letter form - Ecanon", Er3[0, 0, 0] - Er[0, 0, 0]]}];
{ratio3, V0a, V0b}
