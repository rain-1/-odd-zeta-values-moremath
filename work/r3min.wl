lf=OpenWrite["/home/ubuntu/fable-episode-2/zeta-math-2/work/r3min.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"]; log["HF ok"];
run[label_,rZ_,qZ_,etZ_]:=Module[{h0Z,hjZ,NN,term,ann,ct,ap,ord,coeffs,D0,cp,t0},
  h0Z=etZ[[1]] nn+2; hjZ=Table[etZ[[j+1]] nn+1,{j,1,qZ}];
  NN=Product[(h0Z-2 hjZ[[j]])!,{j,rZ+1,qZ}]/Product[(hjZ[[j]]-1)!^2,{j,1,rZ}];
  term=NN (h0Z+2 tt) Gamma[h0Z+tt]^rZ Product[Gamma[hjZ[[j]]+tt],{j,1,qZ}]/
       (Gamma[1+tt]^rZ Product[Gamma[1+h0Z-hjZ[[j]]+tt],{j,1,qZ}]);
  ann=TimeConstrained[Annihilator[term,{S[nn],S[tt]}],200,"T"];
  If[ann==="T",log[label," ann TIMECAP"];Return[]];
  log[label," ann #",Length[ann]];
  t0=AbsoluteTime[];
  ct=TimeConstrained[CreativeTelescoping[ann,S[tt]-1,{S[nn]}],700,"T"];
  If[MatchQ[ct,"T"|"M"],log[label," CT ",ToString[ct]," after ",Round[AbsoluteTime[]-t0],"s"];Return[]];
  ap=ApplyOreOperator[ct[[1,1]],F[nn]];
  ord=Max[Cases[ap,F[nn+a_.]:>a,Infinity]];
  coeffs=Table[Coefficient[ap,F[nn+k]],{k,0,ord}]; D0=Max[Exponent[coeffs,nn]];
  cp=Sum[Coefficient[coeffs[[k+1]],nn,D0]*lam^k,{k,0,ord}];
  log[label," ORDER=",ToString[ord]," in ",Round[AbsoluteTime[]-t0],"s"];
  log[label," charpoly=",ToString[InputForm[Simplify[cp]]]];
  log[label," roots=",ToString[InputForm[N[lam/.Solve[cp==0,lam],8]]]]; ];
run["r3q7 eta0=4 all1 (zeta5 only)", 3,7, Join[{4},Table[1,{7}]]];
log["--after r3q7--"];
run["r3q9 eta0=5 all1 (zeta5,7)", 3,9, Join[{5},Table[1,{9}]]];
log["ALLDONE ",DateString[]]; Close[lf]; Exit[];
