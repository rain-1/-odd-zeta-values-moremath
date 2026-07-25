(* certS.wl -- Route R, with E(v) put into CANONICAL form first.

   E(v) is linear in the harmonic letters (every bracket in its definition is a
   DIFFERENCE of the weight, and v is a sum of products of at most two letters, so
   the differences are single letters times rationals).  Feeding the raw expression
   to Annihilator makes it re-discover that; instead we normalise every
   HarmonicNumber to a base argument using only H^(r)_{x+1} = H^(r)_x + (x+1)^-r,
   collect, and hand HolonomicFunctions
        T * ( c0 + sum_L c_L * L ),   L in {A1(k),A2(k),B1(k),C1,A1(l)},
   which is a hypergeometric term times a rank-6 d-finite factor.

   All multi-line expressions are parenthesised (line-based stdin parsing!).       *)
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
lf=OpenWrite[DIR<>"certS.log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf];Print[x]);
log["START ",DateString[]];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

TT = Binomial[n+k,n] Binomial[n,k]^2 Binomial[n+l,n] Binomial[n,l]^2 Binomial[n+k+l,n];
AA[r_,x_]:=HarmonicNumber[n+x,r]-HarmonicNumber[x,r];
BB[r_,x_]:=HarmonicNumber[n-x,r]-HarmonicNumber[x,r];
CC1 = HarmonicNumber[n+k+l]-HarmonicNumber[k+l];
a0[x_]:=41218 x^3+198849 x^2+320790 x+173057;
B8[x_]:=3874492 x^8+59373972 x^7+394148190 x^6+1481084196 x^5+3447878810 x^4+5095855458 x^3+4673546679 x^2+2433871008 x+551502039;
B9[x_]:=48802112 x^9+967468896 x^8+8488000862 x^7+43246197636 x^6+140983768422 x^5+304912330849 x^4+437406946975 x^3+401272692378 x^2+213593890911 x+50257929339;
cc3 = {(n+1)^5 (n+2) a0[n+1], -2 (n+2) B8[n], -2 B9[n], 2 (n+3)^5 (2n+5) a0[n]};
sh[e_,a_,b_,c_] := e /. {n->n+a, k->k+b, l->l+c};
vw = (HarmonicNumber[n,3] + 2 AA[3,k] - (1/2) AA[2,k] AA[1,k] - (3/2) AA[2,k] BB[1,k] - (3/4) AA[2,k] CC1 - (1/4) AA[2,k] AA[1,l]);
If[Length[Cases[vw,HarmonicNumber[__],Infinity]]=!=19, log["vw TRUNCATED"];Close[lf];Exit[]];

(* --- normalise HarmonicNumber arguments to one of nine base linear forms --- *)
basetab = {{1,1,0}->n+k, {0,1,0}->k, {1,-1,0}->n-k, {1,0,1}->n+l, {0,0,1}->l,
           {1,0,-1}->n-l, {1,1,1}->n+k+l, {0,1,1}->k+l, {1,0,0}->n};
ssum[x_,d_,r_] := Which[d==0, 0, d>0, Sum[1/(x+i)^r,{i,1,d}], True, -Sum[1/(x-i)^r,{i,0,-d-1}]];
hb1[u_,r_] := Module[{cn,ck,cl,d,key,x},
  cn=Coefficient[u,n]; ck=Coefficient[u,k]; cl=Coefficient[u,l];
  d=Expand[u-cn n-ck k-cl l]; key={cn,ck,cl};
  x = key /. basetab;
  If[!IntegerQ[d] || x===key, log["BAD harmonic argument ",ToString[u]]; Abort[]];
  HarmonicNumber[x,r] + ssum[x,d,r]];
hb[e_] := e /. {HarmonicNumber[u_,r_] :> hb1[u,r], HarmonicNumber[u_] :> hb1[u,1]};

{rho,sigma} = Get[DIR<>"Qrow_rhosigma.m"];
log["rho,sigma loaded ",LeafCount[rho]," ",LeafCount[sigma]];

EE = (Sum[cc3[[j+1]] sh[TT,j,0,0] (sh[vw,j,0,0] - vw), {j,1,3}] - (rho /. k->k+1) sh[TT,0,1,0] (sh[vw,0,1,0] - vw) - (sigma /. l->l+1) sh[TT,0,0,1] (sh[vw,0,0,1] - vw));
log["EE LeafCount=",LeafCount[EE]," #H=",Length[Cases[EE,HarmonicNumber[__],Infinity]]];

t0=AbsoluteTime[];
EN = Expand[hb[EE]];
hvars = Union[Cases[EN, HarmonicNumber[__], Infinity]];
log["after hb: #distinct HarmonicNumber = ",Length[hvars]," t=",Round[AbsoluteTime[]-t0],"s"];
log["  they are: ",ToString[InputForm[hvars]]];
deg = Max[Table[Exponent[EN, hvars[[i]]], {i,Length[hvars]}]];
log["  max degree in a single harmonic symbol = ",deg];

(* coefficient of each harmonic symbol, and the constant part, all divided by T *)
t0=AbsoluteTime[];
cofs = Table[Together[FunctionExpand[Coefficient[EN, hvars[[i]]]/TT]], {i,Length[hvars]}];
c0   = Together[FunctionExpand[(EN /. Table[hvars[[i]]->0,{i,Length[hvars]}])/TT]];
log["coefficients over T computed t=",Round[AbsoluteTime[]-t0],"s; leafcounts ",
    ToString[LeafCount/@cofs]," const ",LeafCount[c0]];
Put[{hvars,cofs,c0}, DIR<>"S_Ecanon.m"];

(* rebuild and CHECK that nothing was lost *)
EN2 = TT (c0 + Sum[cofs[[i]] hvars[[i]], {i,Length[hvars]}]);
chk = Together[FunctionExpand[(EN - EN2)/TT]];
log["*** E CANONICAL-FORM CHECK (must be 0): ",ToString[InputForm[Simplify[chk]]]," ***"];

ES = TT (c0 + Sum[cofs[[i]] hvars[[i]], {i,Length[hvars]}]);
t0=AbsoluteTime[];
annE = Annihilator[ES, {S[n],S[k],S[l]}];
log["annE #",Length[annE]," t=",Round[AbsoluteTime[]-t0],"s ",DateString[]];
Put[annE, DIR<>"S_annE.m"];

box[A_,B_] := Flatten[Table[S[n]^a S[k]^b, {a,0,A},{b,0,B}]];
got={};
Do[Module[{A=bx[[1]],B=bx[[2]],t1,r},
   log["--- S step1 (elim l) box(",A,",",B,") --- ",DateString[]];
   t1=AbsoluteTime[];
   r = CreativeTelescoping[annE, S[l]-1, {}, Support -> box[A,B]];
   log["   t=",Round[AbsoluteTime[]-t1],"s ntel=",
       ToString[If[Head[r]===List,Length[r[[1]]],Head[r]]]," ",DateString[]];
   If[Head[r]===List && Length[r[[1]]]>0, AppendTo[got,r];
      Put[r, DIR<>"S_ct1_"<>ToString[A]<>ToString[B]<>".m"]; log["   SAVED"]]],
 {bx,{{1,1},{2,2},{3,3},{4,4},{5,5},{6,6}}}];
If[got==={}, log["S: no step-1 telescoper"]; Close[lf]; Exit[]];
tels = Union[Flatten[got[[All,1]]]];
gbE = OreGroebnerBasis[tels, OreAlgebra[S[n],S[k]]];
log["S gbE #",Length[gbE]];
Put[{got,gbE}, DIR<>"S_ct1all.m"];
Do[Module[{t1,r},
   log["--- S step2 Support S[n]^0..^",d," --- ",DateString[]];
   t1=AbsoluteTime[];
   r = CreativeTelescoping[gbE, S[k]-1, {}, Support -> Table[S[n]^j,{j,0,d}]];
   log["   d=",d," t=",Round[AbsoluteTime[]-t1],"s ntel=",
       ToString[If[Head[r]===List,Length[r[[1]]],Head[r]]]];
   If[Head[r]===List && Length[r[[1]]]>0, Put[r, DIR<>"S_ct2.m"];
      log["   SUCCESS ",DateString[]]; Close[lf]; Exit[]]],
 {d,{0,1,2,3,4,5,6}}];
log["ALL DONE ",DateString[]];
Close[lf]; Exit[];
