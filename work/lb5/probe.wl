lf=OpenWrite["/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/probe.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf]);
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["usage CT: ",ToString[CreativeTelescoping::usage]];
log["usage Ann: ",ToString[Annihilator::usage]];
log["opts CT: ",ToString[InputForm[Options[CreativeTelescoping]]]];
log["names: ",ToString[Names["HolonomicFunctions`*"]]];
Close[lf];Exit[];
