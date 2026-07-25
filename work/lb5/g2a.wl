lf=OpenWrite["/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/gate2.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
log["ping"]; Close[lf]; Exit[];
