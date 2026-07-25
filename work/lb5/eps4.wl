DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf=OpenWrite[DIR<>"eps4.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf];Print[x]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded ",DateString[]];
TT = Binomial[n+k,n] Binomial[n,k]^2 Binomial[n+l,n] Binomial[n,l]^2 Binomial[n+k+l,n];
(* ---------- STAGE V: independent exact verification of the g0 certificates ---------- *)
ann0=Get[DIR<>"g0_ann.m"]; ct1=Get[DIR<>"g0_ct1.m"]; ct2=Get[DIR<>"g0_ct2.m"]; gb=Get[DIR<>"g0_gb.m"];
log["V: loaded ann #",Length[ann0]," ct1tel #",Length[ct1[[1]]]," ct2tel #",Length[ct2[[1]]]];
(* V1: the ANNIHILATOR is genuine:  op.T == 0 for every generator *)
Do[ r=Together[FunctionExpand[ApplyOreOperator[ann0[[i]],TT]/TT]];
    log["V1 ann gen ",i," -> ",ToString[InputForm[Simplify[r]]]], {i,1,Length[ann0]}];
(* V2: the k-step certificate:  tel.T + (S_k-1)(cert.T) == 0 *)
Do[ tl=ct1[[1,i]]; cf=ct1[[2,i]];
    a1=ApplyOreOperator[tl,TT]; a2=ApplyOreOperator[cf,TT];
    r=Together[FunctionExpand[(a1+(a2/.k->k+1)-a2)/TT]];
    log["V2 ct1 pair ",i," -> ",ToString[InputForm[Simplify[r]]]], {i,1,Length[ct1[[1]]]}];
(* V3: the final telescoper equals L_BZ up to a rational unit *)
a0[x_]:=41218 x^3+198849 x^2+320790 x+173057;
B8[x_]:=3874492 x^8+59373972 x^7+394148190 x^6+1481084196 x^5+3447878810 x^4+5095855458 x^3+4673546679 x^2+2433871008 x+551502039;
B9[x_]:=48802112 x^9+967468896 x^8+8488000862 x^7+43246197636 x^6+140983768422 x^5+304912330849 x^4+437406946975 x^3+401272692378 x^2+213593890911 x+50257929339;
LBZc={(n+1)^5 (n+2) a0[n+1], -2 (n+2) B8[n], -2 B9[n], 2 (n+3)^5 (2n+5) a0[n]};
ap=ApplyOreOperator[ct2[[1,1]],FF[n]];
cf3=Table[Coefficient[ap,FF[n+j]],{j,0,3}];
log["V3 telescoper coeffs vs L_BZ, ratio list = ",ToString[InputForm[Together[cf3/LBZc]]]];
log["V3 Expand[cf3 - unit*LBZ] = ",ToString[InputForm[Expand[cf3 - Together[cf3[[1]]/LBZc[[1]]] LBZc]]]];
log["STAGE V DONE ",DateString[]];
(* ---------- STAGE R: rational-parameter deformation, speed probe ---------- *)
GK[x_]:=Gamma[n+k+1+x]/(Gamma[n+1] Gamma[k+1+x]);
GL[x_]:=Gamma[n+l+1+x]/(Gamma[n+1] Gamma[l+1+x]);
HK[x_]:=(Gamma[n+1]/(Gamma[k+1+x] Gamma[n-k+1-x]))^2;
HL[x_]:=(Gamma[n+1]/(Gamma[l+1+x] Gamma[n-l+1-x]))^2;
CC[x_]:=Gamma[n+k+l+1+x]/(Gamma[n+1] Gamma[k+l+1+x]);
FF5[ak_,al_,bk_,bl_,g_]:=GK[ak] HK[bk] GL[al] HL[bl] CC[g];
probe[label_,summand_]:=Module[{ann,c1,gg,c2,t0,tot},
  tot=AbsoluteTime[]; log["--- ",label," ---"];
  t0=AbsoluteTime[]; ann=Annihilator[summand,{S[n],S[k],S[l]}];
  log[label," ann #",Length[ann]," t=",Round[AbsoluteTime[]-t0],"s"];
  t0=AbsoluteTime[]; c1=CreativeTelescoping[ann,S[k]-1,{S[n],S[l]}];
  log[label," ct1 #",Length[c1[[1]]]," t=",Round[AbsoluteTime[]-t0],"s"];
  t0=AbsoluteTime[]; gg=OreGroebnerBasis[c1[[1]],OreAlgebra[S[n],S[l]]];
  log[label," gb #",Length[gg]," t=",Round[AbsoluteTime[]-t0],"s"];
  t0=AbsoluteTime[]; c2=CreativeTelescoping[gg,S[l]-1,{S[n]}];
  log[label," ct2 #",Length[c2[[1]]]," t=",Round[AbsoluteTime[]-t0],"s  TOTAL=",Round[AbsoluteTime[]-tot],"s"];
  Put[c2,DIR<>label<>"_ct2.m"];
  ap2=ApplyOreOperator[c2[[1,1]],FF[n]];
  ord=Max[Cases[ap2,FF[n+a_.]:>a,Infinity]];
  log[label," telescoper ORDER=",ToString[ord]];
  c2];
pg1=probe["r_g17",  FF5[0,0,0,0,1/7]];
pa1=probe["r_ak17", FF5[1/7,0,0,0,0]];
log["ALL DONE ",DateString[]];
Close[lf];
Exit[];
