(* certW.wl -- certificate COMPOSITION (search side; RISC is used here only to FIND
   the cofactors).  Reads <LAB>_ct1.m, <LAB>_ct2.m produced by a two-step run with
   elimination order FIRST then SECOND, recomputes the Groebner basis with cofactors,
   and exports a self-contained certificate package <LAB>_pkg.m containing

     q[i], r[i]   : first-step telescoper/certificate pairs,
                    q[i].W + (S[FIRST]-1)(r[i].W) = 0
     QQ, RR       : second-step telescoper/certificate,
     ff, w[i]     : cofactors with  ff*(QQ + (S[SECOND]-1)*RR) = Sum_i w[i]*q[i]

   Everything in the package is re-checked afterwards by certV.wl, which loads no
   RISC package at all.                                                          *)
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
LAB = Environment["LAB"]; If[LAB === $Failed, LAB = "Y1"];
FIRST = ToExpression[Environment["FIRST"]]; If[Head[FIRST]=!=Symbol, FIRST = l];
SECOND = If[FIRST === k, l, k];
lf=OpenWrite[DIR<>"certW_"<>LAB<>".log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf];Print[x]);
log["START ",DateString[]," LAB=",LAB," FIRST=",ToString[FIRST]," SECOND=",ToString[SECOND]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

alg2 = OreAlgebra[S[n], S[SECOND]];
ct1 = Get[DIR<>LAB<>"_ct1.m"];
ct2 = Get[DIR<>LAB<>"_ct2.m"];
log["ct1 ntel=",Length[ct1[[1]]],"  ct2 ntel=",Length[ct2[[1]]]];

t0=AbsoluteTime[];
gbx = OreGroebnerBasis[ct1[[1]], alg2, Extended->True];
log["gbx t=",Round[AbsoluteTime[]-t0],"s  Length=",Length[gbx],
    "  shapes=",ToString[Map[If[ListQ[#],Length[#],Head[#]]&,gbx]]];
Put[gbx, DIR<>LAB<>"_gbx.m"];
gb = gbx[[1]];
cof = gbx[[2]];            (* expected: gb[[j]] = Sum_i cof[[j,i]] ** ct1tel[[i]] *)
log["gb #",Length[gb],"  cof dims=",ToString[Dimensions[cof]]];

QQ = ct2[[1,1]]; RR = ct2[[2,1]];
dl = ToOrePolynomial[S[SECOND] - 1, alg2];
pp = QQ + dl ** RR;
log["pp head=",ToString[Head[pp]]];
t0=AbsoluteTime[];
red = OreReduce[pp, gb, Extended->True];
log["OreReduce t=",Round[AbsoluteTime[]-t0],"s  remainder zero? ",
    ToString[red[[1]] === 0 || (Head[red[[1]]]===OrePolynomial && red[[1,1]]==={})]];
log["red shapes=",ToString[Map[Head,red]]];
ff = red[[2]]; cc = red[[3]];
log["ff=",ToString[InputForm[ff]],"  #cc=",Length[cc]];

(* w[i] = Sum_j cc[[j]] ** cof[[j,i]] *)
ww = Table[Total[Table[cc[[j]] ** cof[[j,i]], {j, Length[cc]}]], {i, Length[ct1[[1]]]}];
log["ww built, #=",Length[ww]];

pkg = <| "lab"->LAB, "first"->ToString[FIRST], "second"->ToString[SECOND],
         "q"->ct1[[1]], "r"->ct1[[2]], "QQ"->QQ, "RR"->RR, "ff"->ff, "w"->ww,
         "gb"->gb, "cof"->cof, "cc"->cc |>;
Put[pkg, DIR<>LAB<>"_pkg.m"];
log["package written ",DIR,LAB,"_pkg.m  ",DateString[]];
Close[lf]; Exit[];
