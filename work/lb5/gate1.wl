lf=OpenWrite["/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/gate1.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded ",DateString[]];

(* --- test 0: does Annihilator handle HarmonicNumber ? --- *)
t0=AbsoluteTime[];
h1=TimeConstrained[Annihilator[HarmonicNumber[n],S[n]],120,"T"];
log["Ann[H_n] = ",ToString[InputForm[h1]]," in ",Round[AbsoluteTime[]-t0],"s"];
h2=TimeConstrained[Annihilator[HarmonicNumber[n+k,2],{S[n],S[k]}],120,"T"];
log["Ann[H^(2)_{n+k}] = ",ToString[InputForm[h2]]];
h3=TimeConstrained[Annihilator[Binomial[n+k,n]Binomial[n,k]^2 HarmonicNumber[n+k,2],{S[n],S[k]}],240,"T"];
log["Ann[bin*H2] len= ",ToString[If[ListQ[h3],Length[h3],h3]]];

(* --- GATE 1: creative telescoping for the BZ double sum Q_n --- *)
log["=== GATE1: Q_n double sum CT ==="];
Tsum = Binomial[n+k,n] Binomial[n,k]^2 Binomial[n+l,n] Binomial[n,l]^2 Binomial[n+k+l,n];
t0=AbsoluteTime[];
annQ=TimeConstrained[Annihilator[Tsum,{S[n],S[k],S[l]}],900,"T"];
If[annQ==="T", log["annQ TIMECAP"]; Close[lf]; Exit[]];
log["annQ #",Length[annQ]," in ",Round[AbsoluteTime[]-t0],"s"];
log["annQ = ",ToString[InputForm[annQ]]];
t0=AbsoluteTime[];
ctQ=TimeConstrained[MemoryConstrained[CreativeTelescoping[annQ,{S[k]-1,S[l]-1},{S[n]}],20*10^9,"M"],3000,"T"];
If[MatchQ[ctQ,"T"|"M"],
  log["GATE1 CT ",ToString[ctQ]," after ",Round[AbsoluteTime[]-t0],"s"],
  log["GATE1 CT done in ",Round[AbsoluteTime[]-t0],"s; #telescopers=",ToString[Length[ctQ[[1]]]]];
  Put[ctQ,"/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/ctQ.m"];
  ap=ApplyOreOperator[ctQ[[1,1]],F[n]];
  log["applied = ",ToString[InputForm[ap]]];
];
log["DONE ",DateString[]];
Close[lf];Exit[];
