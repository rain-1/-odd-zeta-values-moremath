(* certVU.wl -- RISC-FREE exact verification of the per-letter rank-1 certificates.

   Input (produced by certX.wl):  <lab>_rhosigma.m = {cf, rr, ss}  meaning
       sum_j cf_j (e_m T)(n+j,k,l) = Delta_k( rr * e_m T ) + Delta_l( ss * e_m T ).
   Everything below is a rational-function identity, so the whole check is
       Together[ ... ] === 0
   in Q(n,k,l), using ONLY verifycore.wl's independently rebuilt Gamma-shift
   calculus (tratio).  No RISC package is loaded, and the saved certificates are
   read as inert data.

   Also emits the data the boundary argument needs, in the REGULARISED sense of
   PHASE2_CERTS section 8.4: the value at k=0 and l=0, and the denominator factors
   (which show where poles sit relative to T's double zeros at integer k,l > n).

   Load with  Get["..../certVU.wl"]  -- never with  math < file.                   *)

DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
Get[DIR <> "verifycore.wl"];
lf = OpenWrite[DIR <> "certVU.log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], "  (no RISC package loaded: ",
    ToString[Names["HolonomicFunctions`*"] === {}], ")"];

EL = Get[DIR <> "Eletters.m"];
emap = <|"c0" -> EL[[1]], "alpha" -> EL[[2]], "beta" -> EL[[3]],
         "gamma" -> EL[[4]], "delta" -> EL[[5]], "eps" -> EL[[6]]|>;

(* kernel for the hypergeometric summand H = e_m T, divided by T(n,k,l) *)
mkKer[em_] := Function[{a, b, c},
   Together[(em /. {n -> n + a, k -> k + b, l -> l + c}) tratio[a, b, c]]];

checkLab[lab_] := Module[{cf, rr, ss, em, ker, d, chk, b0k, b0l},
  If[! FileExistsQ[DIR <> lab <> "_rhosigma.m"],
    log[lab, " : no <lab>_rhosigma.m, skipped"]; Return[$Failed]];
  {cf, rr, ss} = Get[DIR <> lab <> "_rhosigma.m"];
  em = emap[lab];
  ker = mkKer[em];
  d = Length[cf] - 1;
  chk = Together[
     Sum[cf[[j + 1]] ker[j, 0, 0], {j, 0, d}]
      - ((rr /. k -> k + 1) ker[0, 1, 0] - rr ker[0, 0, 0])
      - ((ss /. l -> l + 1) ker[0, 0, 1] - ss ker[0, 0, 0])];
  log["*** ", lab, " RISC-FREE single-certificate check (order ", d, "): ",
      ToString[InputForm[chk]], " ***"];
  b0k = Together[(rr em) /. k -> 0];
  b0l = Together[(ss em) /. l -> 0];
  log["  ", lab, " boundary  (rho_m e_m)|_{k=0} = ", ToString[InputForm[b0k]],
      "   (sigma_m e_m)|_{l=0} = ", ToString[InputForm[b0l]]];
  log["  ", lab, " denom(rho_m e_m) factors = ",
      ToString[InputForm[FactorList[Denominator[Together[rr em]]][[All, {1, 2}]]]]];
  log["  ", lab, " denom(sigma_m e_m) factors = ",
      ToString[InputForm[FactorList[Denominator[Together[ss em]]][[All, {1, 2}]]]]];
  {lab, d, chk, b0k === 0, b0l === 0}];

RESVU = Table[checkLab[lb],
   {lb, {"alpha", "beta", "gamma", "delta", "eps", "c0"}}];
log["SUMMARY {lab, order, check, rho|k=0 == 0, sigma|l=0 == 0}:"];
log[ToString[InputForm[RESVU]]];
log["ALL DONE ", DateString[]];
Close[lf];
RESVU
