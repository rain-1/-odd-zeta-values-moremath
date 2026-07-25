(* certT.wl -- creative telescoping on E(v) in LETTER form (rank 6).

   Eletters.m holds {c0, alpha, beta, gamma, delta, eps} with
       E(v)/T = c0 + alpha A1(k) + beta A2(k) + gamma B1(k) + delta C1 + eps A1(l),
   all coefficients explicit rational functions of (n,k,l) (leafcounts 22963, 4336,
   9035, 4337, 4339, 4339).  Under S_l only C1 and A1(l) move, each by a rational --
   so l is the cheap elimination direction.

   Theorem B  <=>  Sum_{k,l} E(v) = 0  (PHASE2_CERTS.md 4quater, PROVED).
   It suffices to certify ANY operator L' annihilating F_n := Sum_{k,l} E(v):
   F_n is known to be 0 for n <= 42 exactly, so ord(L') <= 42 finishes.

   Env: MODE=unc (unconstrained step 1) or MODE=box (Support ladder).            *)
DIR="/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
MODE = Environment["MODE"]; If[MODE === $Failed, MODE = "box"];
lf=OpenWrite[DIR<>"certT_"<>MODE<>".log"];
log[x__]:=(WriteString[lf,x,"\n"];Flush[lf];Print[x]);
log["START ",DateString[]," MODE=",MODE];
Get["/home/ubuntu/riscergosum/RISC/HolonomicFunctions.m"];
log["HF loaded"];

TT = Binomial[n+k,n] Binomial[n,k]^2 Binomial[n+l,n] Binomial[n,l]^2 Binomial[n+k+l,n];
AA[r_,x_]:=HarmonicNumber[n+x,r]-HarmonicNumber[x,r];
BB[r_,x_]:=HarmonicNumber[n-x,r]-HarmonicNumber[x,r];
CC1 = HarmonicNumber[n+k+l]-HarmonicNumber[k+l];
{c0, alpha, beta, gamma, delta, eps} = Get[DIR<>"Eletters.m"];
log["Eletters loaded, leafcounts ",ToString[LeafCount/@{c0,alpha,beta,gamma,delta,eps}]];
ES = TT (c0 + alpha AA[1,k] + beta AA[2,k] + gamma BB[1,k] + delta CC1 + eps AA[1,l]);
ord[c_] := Module[{ap}, ap = ApplyOreOperator[c, FF[n]];
   Max[Join[{0}, Cases[ap, FF[n+a_.] :> a, Infinity]]]];

t0=AbsoluteTime[];
annE = Annihilator[ES, {S[n],S[k],S[l]}];
log["annE #",Length[annE]," t=",Round[AbsoluteTime[]-t0],"s ",DateString[]];
Put[annE, DIR<>"T_annE.m"];

box[A_,B_] := Flatten[Table[S[n]^a S[k]^b, {a,0,A},{b,0,B}]];
If[MODE === "unc",
  t0=AbsoluteTime[];
  ct1 = CreativeTelescoping[annE, S[l]-1, {S[n],S[k]}];
  log["ct1 #",Length[ct1[[1]]]," t=",Round[AbsoluteTime[]-t0],"s ",DateString[]];
  Put[ct1, DIR<>"T_ct1.m"];
  t0=AbsoluteTime[];
  gbE = OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n],S[k]]];
  log["gbE #",Length[gbE]," t=",Round[AbsoluteTime[]-t0],"s"];
  Put[gbE, DIR<>"T_gb.m"],
(* else: Support ladder *)
  got={};
  Do[Module[{A=bx[[1]],B=bx[[2]],t1,r},
     log["--- step1 (elim l) box(",A,",",B,") --- ",DateString[]];
     t1=AbsoluteTime[];
     r = CreativeTelescoping[annE, S[l]-1, {}, Support -> box[A,B]];
     log["   t=",Round[AbsoluteTime[]-t1],"s ntel=",
         ToString[If[Head[r]===List,Length[r[[1]]],Head[r]]]," ",DateString[]];
     If[Head[r]===List && Length[r[[1]]]>0, AppendTo[got,r];
        Put[r, DIR<>"T_ct1_"<>ToString[A]<>ToString[B]<>".m"]; log["   SAVED"]]],
   {bx,{{1,1},{2,2},{3,3},{4,4},{5,5},{6,6}}}];
  If[got==={}, log["no step-1 telescoper in any box"]; Close[lf]; Exit[]];
  ct1 = {Union[Flatten[got[[All,1]]]], Union[Flatten[got[[All,2]]]]};
  Put[ct1, DIR<>"T_ct1.m"];
  gbE = OreGroebnerBasis[ct1[[1]], OreAlgebra[S[n],S[k]]];
  log["gbE #",Length[gbE]];
  Put[gbE, DIR<>"T_gb.m"]];

Do[Module[{t1,r},
   log["--- step2 (elim k) Support S[n]^0..^",d," --- ",DateString[]];
   t1=AbsoluteTime[];
   r = CreativeTelescoping[gbE, S[k]-1, {}, Support -> Table[S[n]^j,{j,0,d}]];
   log["   d=",d," t=",Round[AbsoluteTime[]-t1],"s ntel=",
       ToString[If[Head[r]===List,Length[r[[1]]],Head[r]]]];
   If[Head[r]===List && Length[r[[1]]]>0, Put[r, DIR<>"T_ct2.m"];
      log["   *** SUCCESS *** ORDER=",ToString[ord[r[[1,1]]]]," ",DateString[]];
      log["ALL DONE ",DateString[]]; Close[lf]; Exit[]]],
 {d,{0,1,2,3,4,5,6,8,10}}];
log["step2 not found in the supports tried; trying unconstrained ",DateString[]];
t0=AbsoluteTime[];
ct2 = CreativeTelescoping[gbE, S[k]-1, {S[n]}];
log["ct2 #",Length[ct2[[1]]]," t=",Round[AbsoluteTime[]-t0],"s ORDER=",ToString[ord[ct2[[1,1]]]]];
Put[ct2, DIR<>"T_ct2.m"];
log["ALL DONE ",DateString[]];
Close[lf]; Exit[];
