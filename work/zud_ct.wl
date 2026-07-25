lf=OpenWrite["/home/ubuntu/fable-episode-2/zeta-math-2/work/zud_ct.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
If[Head[Annihilator[nn!,{S[nn]}]]=!=List, log["FATAL load"];Close[lf];Exit[]];
log["HF ok ",DateString[]];

charInfo[rec_, qq_] := Module[{ord, coeffs, D0, cp},
  ord = Max[Cases[rec, S[nn]^a_.:>a, Infinity] /. {}->{0}];
  coeffs = Table[Coefficient[rec /. S[nn]->SS, SS, k], {k,0,ord}];
  D0 = Max[Exponent[coeffs, nn]];
  cp = Sum[Coefficient[coeffs[[k+1]], nn, D0]*lam^k, {k,0,ord}];
  {ord, D0, cp}];

(* ---------- GATE: Apery zeta(3) as a WELL-POISED SUM (r=1,q=5) ---------- *)
(* h0=3n+2, hj=n+1; summand Rt = (h0+2t) Gamma[h0+t] prod Gamma[hj+t] / (Gamma[1+t] prod Gamma[1+h0-hj+t]) *)
log["=== GATE Apery zeta3 (sum form) ==="];
rA = 1; qA = 5; etA = {3,1,1,1,1,1};
h0A = etA[[1]] nn + 2; hjA = Table[etA[[j+1]] nn + 1, {j,1,qA}];
termA = (h0A+2 tt) Gamma[h0A+tt]^rA Product[Gamma[hjA[[j]]+tt],{j,1,qA}] /
        (Gamma[1+tt]^rA Product[Gamma[1+h0A-hjA[[j]]+tt],{j,1,qA}]);
t0=AbsoluteTime[];
annA = Annihilator[termA, {S[nn], S[tt]}];
log["Apery ann ready #",Length[annA]," in ",Round[AbsoluteTime[]-t0],"s"];
t0=AbsoluteTime[];
ctA = TimeConstrained[CreativeTelescoping[annA, S[tt]-1, {S[nn]}], 600, "TIMECAP"];
If[ctA==="TIMECAP", log["Apery TIMECAP"],
  recA = ctA[[1,1]];
  {ordA,DA,cpA} = charInfo[recA, q];
  log["Apery telescoper order=",ToString[ordA]," deg=",ToString[DA]," in ",Round[AbsoluteTime[]-t0],"s"];
  log["Apery charpoly: ",ToString[InputForm[Simplify[cpA]]]];
  log["Apery char roots: ",ToString[InputForm[N[lam/.Solve[cpA==0,lam],8]]]];
  log["Apery expected: order 2, roots ~ 33.97 and 0.0294 ((1+-sqrt2)^4)"]];

(* ---------- REAL: Zudilin r=3, q=13 (zeta5..zeta11) ---------- *)
log["=== ZUDILIN r=3 q=13 (zeta5..11) ==="];
rZ = 3; qZ = 13; etZ = {91,27,27,27,29,30,31,32,33,34,35,36,37,38};
h0Z = etZ[[1]] nn + 2; hjZ = Table[etZ[[j+1]] nn + 1, {j,1,qZ}];
termZ = (h0Z+2 tt) Gamma[h0Z+tt]^rZ Product[Gamma[hjZ[[j]]+tt],{j,1,qZ}] /
        (Gamma[1+tt]^rZ Product[Gamma[1+h0Z-hjZ[[j]]+tt],{j,1,qZ}]);
t0=AbsoluteTime[];
annZ = TimeConstrained[Annihilator[termZ, {S[nn], S[tt]}], 900, "TIMECAP"];
If[annZ==="TIMECAP", log["Zud ann TIMECAP"]; Close[lf]; Exit[]];
log["Zud ann ready #",Length[annZ]," in ",Round[AbsoluteTime[]-t0],"s ",DateString[]];
t0=AbsoluteTime[];
ctZ = TimeConstrained[MemoryConstrained[CreativeTelescoping[annZ, S[tt]-1, {S[nn]}], 12*10^9,"MEMCAP"], 3000, "TIMECAP"];
If[MatchQ[ctZ,"TIMECAP"|"MEMCAP"],
  log["Zud CT HIT ",ToString[ctZ]," after ",Round[AbsoluteTime[]-t0],"s MaxMem=",ToString[N[MaxMemoryUsed[]/10^9,3]],"GB"],
  recZ = ctZ[[1,1]];
  {ordZ,DZ,cpZ} = charInfo[recZ, q];
  log["Zud telescoper ORDER=",ToString[ordZ]," DEG=",ToString[DZ]," in ",Round[AbsoluteTime[]-t0],"s MaxMem=",ToString[N[MaxMemoryUsed[]/10^9,3]],"GB"];
  log["Zud charpoly: ",ToString[InputForm[Simplify[cpZ]]]];
  log["Zud char roots: ",ToString[InputForm[N[lam/.Solve[cpZ==0,lam],10]]]]];
log["DONE ",DateString[]];
Close[lf]; Exit[];
