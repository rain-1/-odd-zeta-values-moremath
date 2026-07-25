lf=OpenWrite["/home/ubuntu/fable-episode-2/zeta-math-2/work/proxy_ct.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf]);
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"]; log["HF ok ",DateString[]];
run[label_,rZ_,qZ_,etZ_]:=Module[{h0Z,hjZ,NN,term,ann,ct,ap,ord,coeffs,degs,D0,cp,t0},
  h0Z=etZ[[1]] nn+2; hjZ=Table[etZ[[j+1]] nn+1,{j,1,qZ}];
  NN=Product[(h0Z-2 hjZ[[j]])!,{j,rZ+1,qZ}]/Product[(hjZ[[j]]-1)!^2,{j,1,rZ}];
  term=NN (h0Z+2 tt) Gamma[h0Z+tt]^rZ Product[Gamma[hjZ[[j]]+tt],{j,1,qZ}]/
       (Gamma[1+tt]^rZ Product[Gamma[1+h0Z-hjZ[[j]]+tt],{j,1,qZ}]);
  t0=AbsoluteTime[];
  ann=TimeConstrained[Annihilator[term,{S[nn],S[tt]}],600,"T"];
  If[ann==="T",log[label," ann TIMECAP"];Return[]];
  log[label," ann #",Length[ann]," in ",Round[AbsoluteTime[]-t0],"s"];
  t0=AbsoluteTime[];
  ct=TimeConstrained[MemoryConstrained[CreativeTelescoping[ann,S[tt]-1,{S[nn]}],11*10^9,"M"],1500,"T"];
  If[MatchQ[ct,"T"|"M"],log[label," CT ",ToString[ct]," after ",Round[AbsoluteTime[]-t0],"s"];Return[]];
  ap=ApplyOreOperator[ct[[1,1]],F[nn]];
  ord=Max[Cases[ap,F[nn+a_.]:>a,Infinity]];
  coeffs=Table[Coefficient[ap,F[nn+k]],{k,0,ord}]; degs=Exponent[coeffs,nn]; D0=Max[degs];
  cp=Sum[Coefficient[coeffs[[k+1]],nn,D0]*lam^k,{k,0,ord}];
  log[label," ORDER=",ToString[ord]," in ",Round[AbsoluteTime[]-t0],"s; coeff-degs=",ToString[degs]];
  log[label," charpoly=",ToString[InputForm[Simplify[cp]]]];
  log[label," roots=",ToString[InputForm[N[lam/.Solve[cp==0,lam],8]]]];
];
run["PROXY-a eta0=3 all1", 3,13, Join[{3},Table[1,{13}]]];
run["PROXY-b eta0=7 mix", 3,13, {7,1,1,1,2,2,2,2,3,3,3,3,3}];
log["ALLDONE ",DateString[]]; Close[lf]; Exit[];
