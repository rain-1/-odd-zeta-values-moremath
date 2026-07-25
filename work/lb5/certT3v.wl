(* certT3v.wl -- RISC-FREE exact verification of the rank-3 single certificate

       M . E3  =  Delta_k( Ck . E3 )  +  Delta_l( Cl . E3 ) ,
       E3 = T * ( c0 + beta*A2(k) + alpha*Psi ) = E(v).

   Loads NO RISC package.  Everything is rebuilt by verifycore.wl:
     * T(n+a,k+b,l+c)/T(n,k,l) from the Gamma-product form (tratio);
     * every HarmonicNumber rewritten by its defining recurrence into
       hh[base,r] + rational (hnorm), the hh[.,.] treated as indeterminates.
   An expression that reduces to 0 in Q(n,k,l)[hh...] is an identity of functions.

   Checks performed
     V-0  the rank-3 letter form agrees with the independently stored canonical
          9-symbol form Ecanon.m                                (must be 0)
     V-1  the single-certificate identity above                 (must be 0)
     V-2  boundary: (Ck . E3)/T at k = 0  and  (Cl . E3)/T at l = 0   (must be 0)
     V-3  denominator factors of the two certificates (pole loci vs T's zeros)

   Load with  math < certT3v.wl  (it is wlcheck-clean) or Get[] in any kernel.    *)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
Get[DIR <> "verifycore.wl"];
lf = OpenWrite[DIR <> "certT3v.log"];
log[x__] := (WriteString[lf, x, "\n"]; Flush[lf]; Print[x]);
log["START ", DateString[], "   RISC absent: ",
    ToString[Names["HolonomicFunctions`*"] === {}]];

(* ---------- the rank-3 kernel ---------- *)
{c0L, alphaL, betaL, gammaL, deltaL, epsL} = Get[DIR <> "Eletters.m"];
log["Eletters LeafCounts ",
    ToString[LeafCount /@ {c0L, alphaL, betaL, gammaL, deltaL, epsL}]];
log["rank-3 ratio assertion (must be {3, 3/2, 1/2}): ",
    ToString[InputForm[Together /@ {gammaL/alphaL, deltaL/alphaL, epsL/alphaL}]]];

A2k = HarmonicNumber[n + k, 2] - HarmonicNumber[k, 2];
Psi = ((HarmonicNumber[n + k] - HarmonicNumber[k])
    + 3 (HarmonicNumber[n - k] - HarmonicNumber[k])
    + (3/2) (HarmonicNumber[n + k + l] - HarmonicNumber[k + l])
    + (1/2) (HarmonicNumber[n + l] - HarmonicNumber[l]));
log["HarmonicNumber counts (must be 2 and 8): ",
    Length[Cases[A2k, HarmonicNumber[__], Infinity]], " ",
    Length[Cases[Psi, HarmonicNumber[__], Infinity]]];

base3 = c0L + betaL A2k + alphaL Psi;
Er3[a_, b_, c_] := Er3[a, b, c] = Expand[tratio[a, b, c] *
   hnorm[base3 /. {n -> n + a, k -> k + b, l -> l + c}]];

(* ---------- V-0 : rank-3 form vs the canonical 9-symbol form ---------- *)
log["V-0 loadEcanon ", ToString[loadEcanon[DIR <> "Ecanon.m"]]];
log["V-0 ", ToString[zeroReport["E3 letter form == Ecanon", Er3[0, 0, 0] - Er[0, 0, 0]]]];

(* ---------- apply an ope[] operator to the kernel ---------- *)
applyOpe[ope[vars_, ts_], ker_, extra_] := Total[Table[
   Module[{co = t[[1]], ex = t[[2]], sh},
     sh = ex + extra;
     Expand[(co /. {n -> n + extra[[1]], k -> k + extra[[2]], l -> l + extra[[3]]}) *
            (ker @@ sh)]],
   {t, ts}]];

If[! FileExistsQ[DIR <> "T3_cert.m"],
   log["MISSING T3_cert.m (run certT3x.wl first)"]; Close[lf]; Exit[]];
{cf, CkO, ClO} = Get[DIR <> "T3_cert.m"];
dM = Length[cf] - 1;
log["telescoper order ", dM, "  Ck terms ", Length[CkO[[2]]],
    "  Cl terms ", Length[ClO[[2]]]];

(* ---------- V-1 : the certificate identity ---------- *)
LHS = Sum[cf[[j + 1]] Er3[j, 0, 0], {j, 0, dM}];
Xk0 = applyOpe[CkO, Er3, {0, 0, 0}];
Xk1 = applyOpe[CkO, Er3, {0, 1, 0}];
Xl0 = applyOpe[ClO, Er3, {0, 0, 0}];
Xl1 = applyOpe[ClO, Er3, {0, 0, 1}];
chk = LHS - (Xk1 - Xk0) - (Xl1 - Xl0);
log["V-1 ", ToString[zeroReport["M.E3 - Delta_k(Ck.E3) - Delta_l(Cl.E3)", chk]]];

(* ---------- V-2 : boundary at k = 0 and l = 0 ----------
   specialising k -> 0 must also act on the hh-symbols: the base cn*n+ck*k+cl*l
   becomes cn*n+cl*l, and H^(r)_0 = 0.                                            *)
setk0[e_] := Together[(e /. hh[{a_, b_, c_}, r_] :>
     If[{a, c} === {0, 0}, 0, hh[{a, 0, c}, r]]) /. k -> 0];
setl0[e_] := Together[(e /. hh[{a_, b_, c_}, r_] :>
     If[{a, b} === {0, 0}, 0, hh[{a, b, 0}, r]]) /. l -> 0];
log["V-2 ", ToString[zeroReport["(Ck.E3)/T at k=0", setk0[Xk0]]]];
log["V-2 ", ToString[zeroReport["(Cl.E3)/T at l=0", setl0[Xl0]]]];

(* ---------- V-3 : where the certificates can be singular ---------- *)
dens[e_] := Union[Flatten[{FactorList[Denominator[Together[#]]][[All, {1, 2}]] & /@
   If[hvars[e] === {}, {e}, Union[Flatten[{CoefficientList[Expand[e], hvars[e]]}]]]}, 1]];
log["V-3 denom factors of (Ck.E3)/T : ", ToString[InputForm[
   Union[DeleteCases[dens[Xk0], {_?NumberQ, _}]]]]];
log["V-3 denom factors of (Cl.E3)/T : ", ToString[InputForm[
   Union[DeleteCases[dens[Xl0], {_?NumberQ, _}]]]]];

log["ALL DONE ", DateString[]];
Close[lf];
