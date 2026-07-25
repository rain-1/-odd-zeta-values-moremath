lf=OpenWrite["/home/ubuntu/fable-episode-2/zeta-math-2/work/zud_ct2.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF ok"];

(* extraction via ApplyOreOperator to a symbolic sequence F[nn] *)
charInfo[opList_] := Module[{rec=opList[[1]], ap, ord, coeffs, D0, cp},
  ap = ApplyOreOperator[rec, F[nn]];
  ord = Max[Cases[ap, F[nn+a_.]:>a, Infinity]];
  coeffs = Table[Coefficient[ap, F[nn+k]], {k,0,ord}];
  D0 = Max[Exponent[coeffs, nn]];
  cp = Sum[Coefficient[coeffs[[k+1]], nn, D0]*lam^k, {k,0,ord}];
  {ord, D0, cp, coeffs}];

(* ---- Apery gate ---- *)
log["=== APERY gate ==="];
rA=1; qA=5; etA={3,1,1,1,1,1};
h0A=etA[[1]] nn+2; hjA=Table[etA[[j+1]] nn+1,{j,1,qA}];
termA=(h0A+2 tt) Gamma[h0A+tt]^rA Product[Gamma[hjA[[j]]+tt],{j,1,qA}]/
      (Gamma[1+tt]^rA Product[Gamma[1+h0A-hjA[[j]]+tt],{j,1,qA}]);
annA=Annihilator[termA,{S[nn],S[tt]}]; log["Apery ann #",Length[annA]];
ctA=CreativeTelescoping[annA,S[tt]-1,{S[nn]}];
log["Apery telescoper computed; #ops=",Length[ctA[[1]]]];
{oA,dA,cpA,coA}=charInfo[ctA[[1]]];
log["Apery ORDER=",ToString[oA]," DEG=",ToString[dA]];
log["Apery charpoly=",ToString[InputForm[Simplify[cpA]]]];
log["Apery roots=",ToString[InputForm[N[lam/.Solve[cpA==0,lam],8]]]];

(* ---- Zudilin: probe Annihilator step, small time budget ---- *)
log["=== ZUDILIN Annihilator probe ==="];
rZ=3; qZ=13; etZ={91,27,27,27,29,30,31,32,33,34,35,36,37,38};
h0Z=etZ[[1]] nn+2; hjZ=Table[etZ[[j+1]] nn+1,{j,1,qZ}];
termZ=(h0Z+2 tt) Gamma[h0Z+tt]^rZ Product[Gamma[hjZ[[j]]+tt],{j,1,qZ}]/
      (Gamma[1+tt]^rZ Product[Gamma[1+h0Z-hjZ[[j]]+tt],{j,1,qZ}]);
log["term built"];
t0=AbsoluteTime[];
annZ=TimeConstrained[Annihilator[termZ,{S[nn],S[tt]}],600,"TIMECAP"];
log["Zud Annihilator -> ",If[ListQ[annZ],"OK #"<>ToString[Length[annZ]],ToString[annZ]]," in ",Round[AbsoluteTime[]-t0],"s"];
If[ListQ[annZ],
  t0=AbsoluteTime[];
  ctZ=TimeConstrained[MemoryConstrained[CreativeTelescoping[annZ,S[tt]-1,{S[nn]}],11*10^9,"MEMCAP"],2400,"TIMECAP"];
  If[MatchQ[ctZ,"TIMECAP"|"MEMCAP"],
    log["Zud CT ",ToString[ctZ]," after ",Round[AbsoluteTime[]-t0],"s MaxMem=",ToString[N[MaxMemoryUsed[]/10^9,3]]],
    {oZ,dZ,cpZ,coZ}=charInfo[ctZ[[1]]];
    log["Zud ORDER=",ToString[oZ]," DEG=",ToString[dZ]," in ",Round[AbsoluteTime[]-t0],"s MaxMem=",ToString[N[MaxMemoryUsed[]/10^9,3]]];
    log["Zud charpoly=",ToString[InputForm[Simplify[cpZ]]]];
    log["Zud roots=",ToString[InputForm[N[lam/.Solve[cpZ==0,lam],10]]]]]];
log["DONE ",DateString[]];
Close[lf]; Exit[];
