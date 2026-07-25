(* certX.wl -- compose each rank-1 certificate produced by certU into
   single-certificate form and check it exactly.

   For a label LAB in {alpha,beta,gamma,delta,eps,c0}, U_<LAB>.m holds {ann,ct1,gb,ct2}
   for the HYPERGEOMETRIC summand  H = T * e_LAB.  Because gb === ct1-telescopers for
   all of these (logged by certU), the only cofactors needed come from OreReduce, and
   the composition is identical to the Q-row one:

        M . H  =  Delta_k( rhoL H )  +  Delta_l( sigmaL H ) ,
        rhoL   = -(1/ff) Sum_i ccf_i ** ct1cert_i  applied to H, over H,
        sigmaL = -(ct2cert applied to H)/H .

   The check  Sum_j M_j (H(n+j)/H) - ((rhoL|k+1) H(n,k+1,l)/H - rhoL)
                                    - ((sigmaL|l+1) H(n,k,l+1)/H - sigmaL)  ==  0
   is exact rational arithmetic.  Results go to <LAB>_rhosigma.m for certV/verifycore. *)
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf=OpenWrite[DIR<>"certX.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf];Print[x]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];
TT = Binomial[n+k,n] Binomial[n,k]^2 Binomial[n+l,n] Binomial[n,l]^2 Binomial[n+k+l,n];
{c0, alpha, beta, gamma, delta, eps} = Get[DIR<>"Eletters.m"];
coef = <|"alpha"->alpha, "beta"->beta, "gamma"->gamma, "delta"->delta,
         "eps"->eps, "c0"->c0|>;
alg2 = OreAlgebra[S[n],S[l]];
ord[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]];
   Max[Join[{0}, Cases[ap, FF[n+a_.] :> a, Infinity]]]];

doone[lab_] := Module[{ann,ct1,gb,ct2,QQ,RR,pp,red,ff,ccf,HH,XT,RT,rr,ss,cf,d,chk,hsh},
  If[!FileExistsQ[DIR<>"U_"<>lab<>".m"], log[lab," : no U_ file, skipped"]; Return[]];
  {ann,ct1,gb,ct2} = Get[DIR<>"U_"<>lab<>".m"];
  HH = TT coef[lab];
  QQ = ct2[[1,1]]; RR = ct2[[2,1]];
  d = ord[QQ];
  log["=== ",lab," : telescoper order ",d," ==="];
  If[gb =!= ct1[[1]], log[lab," gb != ct1tel -- needs the Groebner cofactor chain"]; Return[]];
  pp  = QQ + ToOrePolynomial[S[l]-1, alg2] ** RR;
  red = OreReduce[pp, gb, Extended->True];
  ff = red[[2]]; ccf = red[[3]];
  log[lab," OreReduce remainder ",ToString[Short[red[[1]],1]],"  ff=",ToString[InputForm[ff]]];
  XT = Together[FunctionExpand[Total[Table[ApplyOreOperator[ccf[[i]] ** ct1[[2,i]], HH],
                                           {i, Length[ccf]}]] / (ff HH)]];
  RT = Together[FunctionExpand[ApplyOreOperator[RR, HH]/HH]];
  rr = Together[-XT]; ss = Together[-RT];
  cf = Table[Coefficient[ApplyOreOperator[QQ, FF[n]], FF[n+j]], {j,0,d}];
  hsh[a_,b_,c_] := Together[FunctionExpand[(HH /. {n->n+a,k->k+b,l->l+c})/HH]];
  chk = Together[FunctionExpand[(Sum[cf[[j+1]] hsh[j,0,0], {j,0,d}] - ((rr /. k->k+1) hsh[0,1,0] - rr) - ((ss /. l->l+1) hsh[0,0,1] - ss))]];
  log["*** ",lab," SINGLE-CERTIFICATE CHECK: ",ToString[InputForm[chk]]," ***"];
  Put[{cf, rr, ss}, DIR<>lab<>"_rhosigma.m"];
  log[lab," saved; leafcounts ",LeafCount[rr]," / ",LeafCount[ss],"  ",DateString[]]];

Do[doone[lab], {lab, {"alpha","beta","gamma","delta","eps","c0"}}];
log["ALL DONE ",DateString[]];
Close[lf]; Exit[];
