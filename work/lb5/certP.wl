(* certP.wl -- the TAU-SPLIT route to the operator annihilating  F_n = Sum_{k,l} E(v).

   WHY.  certT3.wl (the monolithic rank-3 attack) was OOM-killed at 14.4 GB inside
   Annihilator: the rank is only 3, but the three coefficients of Eletters.m have
   66499 / 44011 / 22317 leaves and RISC's closure blows up on them.  certU/certUb
   have the same disease one letter at a time.  The coefficients are large only
   because they are SUMS over the five shift terms of E(v); each individual term is
   small.  So split E(v) by shift term BEFORE telescoping.

   With  v = H^(3)_n + 2 A3(k) - (1/2) A2(k) Psi ,  Psi = A1(k)+3B1(k)+(3/2)C1+(1/2)A1(l),
   certS.wl's definition of E(v) is  E(v) = Sum_tau G_tau * (tau.v - v)  over the five
   shifts tau, with hypergeometric weights

       G_{n_j} = c_j T(n+j,k,l)   (j = 1,2,3) ,
       G_{kk}  = -rho(n,k+1,l) T(n,k+1,l) ,
       G_{ll}  = -sigma(n,k,l+1) T(n,k,l+1) ,

   and, because tau(A2 Psi) - A2 Psi = A2 dPsi + dA2 (Psi + dPsi),

       tau.v - v  =  p_tau  +  q_tau A2(k)  +  r_tau Psi ,
       p_tau = h3_tau + 2 a3_tau - (1/2) dA2_tau dPsi_tau ,
       q_tau = -(1/2) dPsi_tau ,        r_tau = -(1/2) dA2_tau ,

   every one of h3, a3, dA2, dPsi a SHORT rational function.  Each  F_tau = G_tau *
   (p+q A2+r Psi)  is therefore d-finite of rank <= 3 with small coefficients, and
   Sum_tau F_tau = E(v) exactly.  (Consistency with PHASE2_CERTS section 11:
   alpha = Sum_tau (G_tau/T) r_tau = -Lambda/2, which section 11.4 already checked to 0.)

   A telescoper M_tau for each F_tau, then M = LCLM(M_tau), annihilates Sum_{k,l} E(v):
   no Abel correction is needed, because the letters are never factored out --
   the whole d-finite function is telescoped.

   TAUS, ORD, DMAX, MEMCAP from the environment.
   Run:  TAUS=ll,n1,n2,n3 math < certP.wl                                            *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
$HistoryLength = 0;
TAUS = Environment["TAUS"]; If[TAUS === $Failed, TAUS = "n1,n2,n3,kk,ll"];
ORD = Environment["ORD"]; If[ORD === $Failed, ORD = "kl"];
DMAX = Environment["DMAX"]; DMAX = If[DMAX === $Failed, 12, ToExpression[DMAX]];
MEMCAP = Environment["MEMCAP"];
MEMCAP = If[MEMCAP === $Failed, 4000000000, ToExpression[MEMCAP]];
TAG = StringReplace[TAUS, "," -> "_"];
lf = OpenWrite[DIR <> "certP_" <> TAG <> ".log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], "  TAUS=", TAUS, " ORD=", ORD, " DMAX=", DMAX,
    " MEMCAP=", MEMCAP];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

TT = Binomial[n + k, n] Binomial[n, k]^2 Binomial[n + l, n] Binomial[n, l]^2 *
     Binomial[n + k + l, n];
AA[r_, x_] := HarmonicNumber[n + x, r] - HarmonicNumber[x, r];
BB[r_, x_] := HarmonicNumber[n - x, r] - HarmonicNumber[x, r];
CC1 = HarmonicNumber[n + k + l] - HarmonicNumber[k + l];
a0[x_] := 41218 x^3 + 198849 x^2 + 320790 x + 173057;
B8[x_] := 3874492 x^8 + 59373972 x^7 + 394148190 x^6 + 1481084196 x^5 +
   3447878810 x^4 + 5095855458 x^3 + 4673546679 x^2 + 2433871008 x + 551502039;
B9[x_] := 48802112 x^9 + 967468896 x^8 + 8488000862 x^7 + 43246197636 x^6 +
   140983768422 x^5 + 304912330849 x^4 + 437406946975 x^3 + 401272692378 x^2 +
   213593890911 x + 50257929339;
cc3 = {(n + 1)^5 (n + 2) a0[n + 1], -2 (n + 2) B8[n], -2 B9[n],
       2 (n + 3)^5 (2 n + 5) a0[n]};
sh[e_, a_, b_, c_] := e /. {n -> n + a, k -> k + b, l -> l + c};
{rho, sigma} = Get[DIR <> "Qrow_rhosigma.m"];
log["rho,sigma loaded ", LeafCount[rho], " ", LeafCount[sigma]];

A2k = AA[2, k];
Psi = (AA[1, k] + 3 BB[1, k] + (3/2) CC1 + (1/2) AA[1, l]);
vw = (HarmonicNumber[n, 3] + 2 AA[3, k] - (1/2) A2k Psi);
log["HarmonicNumber counts A2k/Psi/vw (must be 2/8/13): ",
    Length[Cases[A2k, HarmonicNumber[__], Infinity]], "/",
    Length[Cases[Psi, HarmonicNumber[__], Infinity]], "/",
    Length[Cases[vw, HarmonicNumber[__], Infinity]]];

(* ---- the five shift terms: weight, and the rational data of tau.v - v ----
   NB: a line ENDING IN "<|" makes `math < file` emit Syntax::sntxf and silently
   drop the whole assignment (a new variant of the PHASE2_CERTS section 2 trap,
   which wlcheck.py does not catch).  Associations are therefore avoided here --
   everything is a Which[] whose first line cannot possibly parse alone.        *)
sumi[e_, j_] := Sum[e, {i, 1, j}];
tauNQ[tau_] := MemberQ[{"n1", "n2", "n3"}, tau];
tauJf[tau_] := Which[tau === "n1", 1, tau === "n2", 2, tau === "n3", 3, True, 0];
tauW[tau_] := Which[
   tauNQ[tau], cc3[[tauJf[tau] + 1]] sh[TT, tauJf[tau], 0, 0],
   tau === "kk", -(rho /. k -> k + 1) sh[TT, 0, 1, 0],
   True, -(sigma /. l -> l + 1) sh[TT, 0, 0, 1]];
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
Ftau[tau_] := tauW[tau] stuff[tau];
alltau = {"n1", "n2", "n3", "kk", "ll"};
log["weight LeafCounts (none may be 0/atomic): ",
    ToString[LeafCount /@ (tauW /@ alltau)]];

(* ---- ASSERTION: Sum_tau F_tau == E(v), at exact integer points ---- *)
EEref = (Sum[cc3[[j + 1]] sh[TT, j, 0, 0] (sh[vw, j, 0, 0] - vw), {j, 1, 3}]
   - (rho /. k -> k + 1) sh[TT, 0, 1, 0] (sh[vw, 0, 1, 0] - vw)
   - (sigma /. l -> l + 1) sh[TT, 0, 0, 1] (sh[vw, 0, 0, 1] - vw));
dif = Total[Ftau /@ alltau] - EEref;
splitres = Table[Simplify[dif /. {n -> pt[[1]], k -> pt[[2]], l -> pt[[3]]}],
   {pt, {{5, 2, 3}, {6, 1, 4}, {4, 3, 0}, {7, 0, 2}}}];
log["SPLIT CHECK (must all be 0): ", ToString[InputForm[splitres]]];
If[Union[splitres] =!= {0},
   log["SPLIT CHECK FAILED -- refusing to telescope a wrong object. ABORT."];
   Close[lf]; Exit[]];

ordOf[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]];
   Max[Join[{0}, Cases[ap, FF[n + a_.] :> a, Infinity]]]];
(* HoldRest is ESSENTIAL and was missing until 2026-07-25 (PHASE2_CERTS section 17.5).
   Without it `body` evaluates BEFORE stage is entered, so (i) MemoryConstrained wraps an
   already-computed value and can never abort -- which is why MEMCAP never fired on any of
   the OOM runs -- and (ii) the FileExistsQ branch prints "loaded checkpoint" only after
   redoing the whole computation and throwing it away, so checkpoints saved nothing. *)
SetAttributes[stage, HoldRest];
stage[file_, lab_, name_, body_] := Module[{r, t0},
  If[FileExistsQ[DIR <> file],
    r = Get[DIR <> file]; log["  ", lab, " ", name, " : loaded checkpoint"]; r,
    t0 = AbsoluteTime[]; r = MemoryConstrained[body, MEMCAP];
    If[r === $Aborted, log["  ", lab, " ", name, " : MEMORY ABORT after ",
        Round[AbsoluteTime[] - t0], "s"]; $Aborted,
      Put[r, DIR <> file];
      log["  ", lab, " ", name, " #", Length[r], " t=", Round[AbsoluteTime[] - t0],
          "s  (checkpointed)  mem=", Round[MaxMemoryUsed[]/10^9., 2], "GB"]; r]]];

{V1, V2} = If[ORD === "lk", {l, k}, {k, l}];
doTau[tau_] := Module[{FF0, ann, ct1, gb, ct2, supp, t0, got},
  log["=== tau ", tau, " (ORD=", ORD, ") === ", DateString[]];
  FF0 = Ftau[tau];
  log["  ", tau, " LeafCount ", LeafCount[FF0]];
  ann = stage["P_" <> tau <> "_ann.m", tau, "ann",
              Annihilator[FF0, {S[n], S[k], S[l]}]];
  If[ann === $Aborted, Return[$Failed]];
  ct1 = stage["P_" <> tau <> "_" <> ORD <> "_ct1.m", tau, "ct1",
              CreativeTelescoping[ann, S[V1] - 1, {S[n], S[V2]}]];
  If[ct1 === $Aborted, Return[$Failed]];
  gb = stage["P_" <> tau <> "_" <> ORD <> "_gb.m", tau, "gb",
             OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n], S[V2]]]];
  If[gb === $Aborted, Return[$Failed]];
  log["  ", tau, " gb === ct1tel ? ", ToString[gb === ct1[[1]]]];
  got = $Failed;
  Do[supp = Table[S[n]^i, {i, 0, d}];
     t0 = AbsoluteTime[];
     ct2 = Quiet[Check[MemoryConstrained[
             CreativeTelescoping[gb, S[V2] - 1, {}, Support -> supp], MEMCAP], $Failed]];
     log["  ", tau, " ct2 d=", d, " t=", Round[AbsoluteTime[] - t0], "s -> ",
         If[Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1,
            "FOUND order " <> ToString[ordOf[ct2[[1, 1]]]], "none"], "  ", DateString[]];
     If[Head[ct2] === List && Length[ct2] >= 1 && Length[ct2[[1]]] >= 1,
        got = ct2; Break[]],
   {d, 0, DMAX}];
  If[got =!= $Failed,
     Put[{ann, ct1, gb, got}, DIR <> "P_" <> tau <> ".m"];
     log["  ", tau, " SAVED P_", tau, ".m  telescoper order ", ordOf[got[[1, 1]]]],
     log["  ", tau, " NO telescoper up to d=", DMAX]];
  got];

Do[doTau[tt], {tt, StringSplit[TAUS, ","]}];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
