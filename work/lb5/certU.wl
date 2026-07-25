(* certU.wl -- SECOND weight-lowering: everything becomes RANK-1 telescoping.

   E(v)/T = c0 + alpha A1(k) + beta A2(k) + gamma B1(k) + delta C1 + eps A1(l).
   For an operator M = sum_j M_j S_n^j,
       M . E  =  sum_m [ sum_j M_j e_m(n+j) T(n+j) ] . m
               +  sum_j M_j T(n+j) [ c0(n+j) + sum_m e_m(n+j) d_m^(j) ] ,
   where d_m^(j) = m(n+j) - m is a RATIONAL function (each m is a single letter).
   So if M is a telescoper for the HYPERGEOMETRIC double sum  sum_{k,l} e_m T
   for every letter m -- i.e. M in the intersection of the five telescoper ideals,
   i.e. M = LCLM(M_alpha,...,M_eps) -- then
       M . E  =  Delta_k(...) + Delta_l(...) + G ,      G hypergeometric,
   hence  M . F = sum_{k,l} G  with F = sum_{k,l} E, and a rank-1 telescoper N for
   sum G gives  N M . F = 0.  Since F = 0 is already known exactly for n <= 42,
   ord(N M) <= 42 finishes Theorem B.

   Every creative-telescoping call here is on a rank-1 (hypergeometric) summand,
   which costs ~4 s (the Q-row calibration).                                       *)
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
LABS = Environment["LABS"]; If[LABS === $Failed, LABS = "alpha,beta,gamma,delta,eps,c0"];
lf=OpenWrite[DIR<>"certU_"<>StringReplace[LABS,","->"_"]<>".log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf];Print[x]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

TT = Binomial[n+k,n] Binomial[n,k]^2 Binomial[n+l,n] Binomial[n,l]^2 Binomial[n+k+l,n];
{c0, alpha, beta, gamma, delta, eps} = Get[DIR<>"Eletters.m"];
log["Eletters loaded ",ToString[LeafCount/@{c0,alpha,beta,gamma,delta,eps}]];
ord[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]];
   Max[Join[{0}, Cases[ap, FF[n+a_.] :> a, Infinity]]]];

rank1[lab_, phi_] := Module[{ann,ct1,gb,ct2,t0},
  log["=== rank-1 CT for ",lab," === ",DateString[]];
  t0=AbsoluteTime[];
  ann = Annihilator[TT phi, {S[n],S[k],S[l]}];
  log["  ",lab," ann #",Length[ann]," t=",Round[AbsoluteTime[]-t0],"s"];
  t0=AbsoluteTime[];
  ct1 = CreativeTelescoping[ann, S[k]-1, {S[n],S[l]}];
  log["  ",lab," ct1 #",Length[ct1[[1]]]," t=",Round[AbsoluteTime[]-t0],"s"];
  t0=AbsoluteTime[];
  gb = OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n],S[l]]];
  log["  ",lab," gb #",Length[gb]," t=",Round[AbsoluteTime[]-t0],"s gb===ct1? ",
      ToString[gb === ct1[[1]]]];
  t0=AbsoluteTime[];
  ct2 = CreativeTelescoping[gb, S[l]-1, {S[n]}];
  log["  ",lab," ct2 #",Length[ct2[[1]]]," t=",Round[AbsoluteTime[]-t0],
      "s ORDER=",ToString[ord[ct2[[1,1]]]]," ",DateString[]];
  Put[{ann,ct1,gb,ct2}, DIR<>"U_"<>lab<>".m"];
  ct2[[1,1]]];

cmap = <|"alpha"->alpha, "beta"->beta, "gamma"->gamma, "delta"->delta, "eps"->eps, "c0"->c0|>;
labs = StringSplit[LABS, ","];
log["labels: ",ToString[labs]];
Ms = Table[rank1[lb, cmap[lb]], {lb, labs}];
log["orders: ",ToString[ord /@ Ms]];
Put[Ms, DIR<>"U_Ms_"<>StringReplace[LABS,","->"_"]<>".m"];

If[Length[Ms] >= 5,
  t0=AbsoluteTime[];
  MM = LCLM @@ Take[Ms, 5];
  log["LCLM of the five letter telescopers: ORDER=",ToString[ord[MM]],
      " t=",Round[AbsoluteTime[]-t0],"s ",DateString[]];
  Put[MM, DIR<>"U_M.m"]];
log["ALL DONE ",DateString[]];
Close[lf]; Exit[];
