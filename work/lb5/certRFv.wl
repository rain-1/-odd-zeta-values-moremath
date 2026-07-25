(* certRFv.wl -- RISC-FREE exact verification of the refold certificate.

   Loads NO RISC package.  verifycore.wl rebuilds everything from scratch: the
   Gamma-shift calculus (tratio), the harmonic normaliser (hnorm, which uses ONLY
   H^(r)_{x+1} = H^(r)_x + 1/(x+1)^r), and a hand-rolled Ore algebra.  An identity
   that reduces to 0 in Q(n,k,l)[hh...] holds as an identity of functions wherever
   the harmonic numbers are defined.

   V-A  (WHICH=E only) the rank-3 letter form of E(vtilde) equals the RAW definition
        Sum_tau W_tau (tau.vtilde - vtilde) -- SYMBOLICALLY, not at sample points.
   V-B  the single certificate:  M . F = Delta_k( X . F ) + Delta_l( Y . F ).
   V-C  (WHICH=D only) M is L_BZ, coefficientwise.
   V-D  boundary at the near edge:  (X . F)|_{k=0} = 0  and  (Y . F)|_{l=0} = 0.
        This is the step CERTS_RESUME section 4.0 flags as "easiest to assume and
        hardest to notice missing".  There is exactly ONE pair of it here, because
        the object was never split.
   V-E  denominator factors of the boundary data, for the far-edge pole count
        (T has a DOUBLE zero at every integer k > n; vtilde has at worst a SIMPLE
        pole there, from B1(k), and none in l).

   Env: WHICH = D (default) | E.
   Run: WHICH=D math < certRFv.wl                                                  *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
$HistoryLength = 0;
WHICH = Environment["WHICH"]; If[WHICH === $Failed, WHICH = "D"];
Get[DIR <> "verifycore.wl"];
lf = OpenWrite[DIR <> "certRFv_" <> WHICH <> ".log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], "  WHICH=", WHICH, "   RISC absent: ",
    ToString[Names["HolonomicFunctions`*"] === {}]];

AA[r_, x_] := HarmonicNumber[n + x, r] - HarmonicNumber[x, r];
BB[r_, x_] := HarmonicNumber[n - x, r] - HarmonicNumber[x, r];
a0[x_] := 41218 x^3 + 198849 x^2 + 320790 x + 173057;
B8[x_] := 3874492 x^8 + 59373972 x^7 + 394148190 x^6 + 1481084196 x^5 +
   3447878810 x^4 + 5095855458 x^3 + 4673546679 x^2 + 2433871008 x + 551502039;
B9[x_] := 48802112 x^9 + 967468896 x^8 + 8488000862 x^7 + 43246197636 x^6 +
   140983768422 x^5 + 304912330849 x^4 + 437406946975 x^3 + 401272692378 x^2 +
   213593890911 x + 50257929339;
cc3 = {(n + 1)^5 (n + 2) a0[n + 1], -2 (n + 2) B8[n], -2 B9[n],
       2 (n + 3)^5 (2 n + 5) a0[n]};
{rho, sigma} = Get[DIR <> "Qrow_rhosigma.m"];
shx[e_, a_, b_, c_] := e /. {n -> n + a, k -> k + b, l -> l + c};

X2 = AA[2, l] - AA[2, k];
Y1 = AA[1, k] + 3 BB[1, k];
vt = (HarmonicNumber[n, 3] + 2 AA[3, k] + (1/2) X2 Y1);
log["vtilde symbols (must be 10): ",
    Length[Union[Cases[vt, HarmonicNumber[__], Infinity]]]];

(* ---- the five shift terms, as prefactor u_tau x T-shift s_tau ---- *)
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
dh3f[tau_] := If[tauNQ[tau], sumi[1/(n + i)^3, tauJf[tau]], 0];
da3f[tau_] := Which[
   tauNQ[tau], sumi[1/(n + i + k)^3, tauJf[tau]],
   tau === "kk", 1/(n + k + 1)^3 - 1/(k + 1)^3,
   True, 0];
dXf[tau_] := Which[
   tauNQ[tau], sumi[1/(n + i + l)^2 - 1/(n + i + k)^2, tauJf[tau]],
   tau === "kk", -(1/(n + k + 1)^2 - 1/(k + 1)^2),
   True, 1/(n + l + 1)^2 - 1/(l + 1)^2];
dYf[tau_] := Which[
   tauNQ[tau], sumi[1/(n + i + k) + 3/(n + i - k), tauJf[tau]],
   tau === "kk", (1/(n + k + 1) - 1/(k + 1)) - 3 (1/(n - k) + 1/(k + 1)),
   True, 0];
alltau = {"n1", "n2", "n3", "kk", "ll"};
pT[tau_] := Together[dh3f[tau] + 2 da3f[tau] + (1/2) dXf[tau] dYf[tau]];
qT[tau_] := Together[(1/2) dYf[tau]];
rT[tau_] := Together[(1/2) dXf[tau]];
wro[tau_] := wro[tau] = Together[uf[tau] tratio @@ sf[tau]];
base = (Together[Sum[wro[tau] pT[tau], {tau, alltau}]]
      + Together[Sum[wro[tau] qT[tau], {tau, alltau}]] X2
      + Together[Sum[wro[tau] rT[tau], {tau, alltau}]] Y1);
If[Length[Union[Cases[base, HarmonicNumber[__], Infinity]]] =!= 7,
   log["E(vtilde) letter form MALFORMED (symbols != 7) -- ABORT."];
   Close[lf]; Exit[]];

(* ---- V-A : the letter form against the RAW definition, symbolically ---- *)
If[WHICH === "E",
   rawE = Total[Table[Module[{s = sf[tau]},
      Expand[uf[tau] (tratio @@ s) hnorm[shx[vt, s[[1]], s[[2]], s[[3]]] - vt]]],
     {tau, alltau}]];
   log["V-A ", ToString[zeroReport[
      "E(vtilde)/T letter form - Sum_tau (W_tau/T)(tau.vtilde - vtilde)",
      Expand[hnorm[base]] - rawE]]]];

(* ---- the kernel  ker[a,b,c] = F(n+a,k+b,l+c) / T(n,k,l) ---- *)
kerf = If[WHICH === "D", vt, base];
ker[a_, b_, c_] := ker[a, b, c] =
   Expand[tratio[a, b, c] hnorm[shx[kerf, a, b, c]]];

applyOpe[ope[vars_, ts_], kk_, extra_] := Total[Table[
   Module[{co = t[[1]], ex = t[[2]], sh}, sh = ex + extra;
     Expand[shx[co, extra[[1]], extra[[2]], extra[[3]]] (kk @@ sh)]], {t, ts}]];

CF = DIR <> "RF" <> WHICH <> "_composed.m";
If[! FileExistsQ[CF],
   log["MISSING ", CF, " (run certRFy.wl first)"]; Close[lf]; Exit[]];
{cf, Xope, Yope} = Get[CF];
dM = Length[cf] - 1;
log["telescoper order ", dM, "   X terms ", Length[Xope[[2]]],
    "   Y terms ", Length[Yope[[2]]]];

(* ---- V-C : is M exactly L_BZ ? ---- *)
If[WHICH === "D" && dM === 3,
   log["V-C  M / L_BZ coefficientwise (must be 4 equal nonzero entries): ",
       ToString[InputForm[Together[cf/cc3]]]]];

(* ---- V-B : the single certificate ---- *)
LHS = Sum[cf[[j + 1]] ker[j, 0, 0], {j, 0, dM}];
x0 = applyOpe[Xope, ker, {0, 0, 0}]; x1 = applyOpe[Xope, ker, {0, 1, 0}];
y0 = applyOpe[Yope, ker, {0, 0, 0}]; y1 = applyOpe[Yope, ker, {0, 0, 1}];
log["V-B ", ToString[zeroReport["M.F - Delta_k(X.F) - Delta_l(Y.F)",
     LHS - (x1 - x0) - (y1 - y0)]]];

(* ---- V-D : the near-edge boundary, the step that is easiest to skip ---- *)
setk0[e_] := Together[(e /. hh[{a_, b_, c_}, r_] :>
     If[{a, c} === {0, 0}, 0, hh[{a, 0, c}, r]]) /. k -> 0];
setl0[e_] := Together[(e /. hh[{a_, b_, c_}, r_] :>
     If[{a, b} === {0, 0}, 0, hh[{a, b, 0}, r]]) /. l -> 0];
log["V-D ", ToString[zeroReport["(X.F)/T at k=0", setk0[x0]]]];
log["V-D ", ToString[zeroReport["(Y.F)/T at l=0", setl0[y0]]]];

(* ---- V-E : denominators, for the far-edge pole count ---- *)
dens[e_] := Union[Flatten[{FactorList[Denominator[Together[#]]][[All, {1, 2}]] & /@
   If[hvars[e] === {}, {e}, Union[Flatten[{CoefficientList[Expand[e], hvars[e]]}]]]}, 1]];
log["V-E denom factors of X.F : ",
    ToString[InputForm[Union[DeleteCases[dens[x0], {_?NumberQ, _}]]]]];
log["V-E denom factors of Y.F : ",
    ToString[InputForm[Union[DeleteCases[dens[y0], {_?NumberQ, _}]]]]];
log["ALL DONE ", DateString[]];
Close[lf];
