(* certT3f.wl -- FINAL step for Theorem B on the rank-3 direct route.  RISC-FREE.

   Input   T3_cert.m = {cf, CkO, ClO}   (certT3x.wl), cf = coefficients of the
           telescoper M in S[n], already verified by certT3v.wl.

   Builds, with verifycore.wl's own one-variable Ore arithmetic (no RISC):

       L''  =  M ** L_BZ          ord(L'') = ord(M) + 3

   and reports
     * ord(L'')                                     -> initial values required
     * the leading coefficient of L'' and its integer roots n >= 0
     * the count of exact consecutive zeros of D_n = Sum T*w3hat - Phat_n available
       from seqdata300.json                          (301: n = 0..300)

   Logic: L_BZ.R = F (regularised reduction, PHASE2_CERTS 8.4), M.F = 0 (certificate
   + boundary), so L''.R = 0; L_BZ.Phat = 0 by construction of the ladder, so
   L''.Phat = 0; hence L''.D = 0 and D == 0 follows from ord(L'') consecutive zeros
   together with non-vanishing of lc(L'') on the propagation range.

   Run:  math < certT3f.wl                                                         *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
Get[DIR <> "verifycore.wl"];
lf = OpenWrite[DIR <> "certT3f.log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], "   RISC absent: ",
    ToString[Names["HolonomicFunctions`*"] === {}]];

(* CERTFILE = T3_cert.m (rank-3 direct route) or P_cert.m (tau-split route);
   only the telescoper's coefficient list -- the first element -- is used here. *)
CERTFILE = Environment["CERTFILE"];
If[CERTFILE === $Failed,
   CERTFILE = If[FileExistsQ[DIR <> "P_cert.m"], "P_cert.m", "T3_cert.m"]];
log["CERTFILE = ", CERTFILE];
If[! FileExistsQ[DIR <> CERTFILE],
   log["MISSING ", CERTFILE]; Close[lf]; Exit[]];
cf = First[Get[DIR <> CERTFILE]];
dM = Length[cf] - 1;
log["ord(M) = ", dM];

vn = {S[n]};
Mope = opNorm[ope[vn, Table[{cf[[j + 1]], {j}}, {j, 0, dM}]]];

a0f[x_] := 41218 x^3 + 198849 x^2 + 320790 x + 173057;
B8f[x_] := 3874492 x^8 + 59373972 x^7 + 394148190 x^6 + 1481084196 x^5 +
   3447878810 x^4 + 5095855458 x^3 + 4673546679 x^2 + 2433871008 x + 551502039;
B9f[x_] := 48802112 x^9 + 967468896 x^8 + 8488000862 x^7 + 43246197636 x^6 +
   140983768422 x^5 + 304912330849 x^4 + 437406946975 x^3 + 401272692378 x^2 +
   213593890911 x + 50257929339;
LBZc = {(n + 1)^5 (n + 2) a0f[n + 1], -2 (n + 2) B8f[n], -2 B9f[n],
        2 (n + 3)^5 (2 n + 5) a0f[n]};
LBZope = ope[vn, Table[{LBZc[[j + 1]], {j}}, {j, 0, 3}]];

LPP = opTimes[Mope, LBZope];
dF = Max[LPP[[2, All, 2, 1]]];
log["*** L'' = M ** L_BZ : order ", dF, " ***"];
lc = Together[First[Select[LPP[[2]], #[[2]] === {dF} &]][[1]]];
log["leading coefficient LeafCount ", LeafCount[lc]];
Put[LPP, DIR <> "T3_Lfinal.m"];

nz = Union[Cases[n /. Solve[Numerator[lc] == 0, n], _Integer]];
log["integer roots of lc(L'') : ", ToString[nz]];
log["integer roots with n >= 0 : ", ToString[Select[nz, # >= 0 &]]];

log["initial values required : ", dF, "   available (exact, seqdata300.json) : 301"];
log["SUFFICIENT : ", ToString[dF <= 301 && Select[nz, # >= 0 &] === {}]];
log["ALL DONE ", DateString[]];
Close[lf]; Exit[];
