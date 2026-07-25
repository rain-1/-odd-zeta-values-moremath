(* expel.wl -- export the six coefficients e_m = {c0,alpha,beta,gamma,delta,eps}
   of  E(v)/T  as numerator/denominator coefficient tables mod p, for the
   independent modular order-prediction of the rank-1 telescopers (Python side).

   Format (plain text, one polynomial per block):
       # <label> <num|den> <nterms>
       dn dk dl c
       ...
*)
DIR = "/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5/";
PP = 33554393;
labs = {"c0", "alpha", "beta", "gamma", "delta", "eps"};
EL = Get[DIR <> "Eletters.m"];
st = OpenWrite[DIR <> "Ecoef.txt"];
Do[Module[{tg, u, v},
   tg = Together[EL[[i]]];
   u = PolynomialMod[Numerator[tg], PP];
   v = PolynomialMod[Denominator[tg], PP];
   Do[Module[{q = If[w === "num", u, v], cr},
      cr = CoefficientRules[q, {n, k, l}];
      WriteString[st, "# ", labs[[i]], " ", w, " ", Length[cr], "\n"];
      Do[WriteString[st,
         ToString[r[[1, 1]]], " ", ToString[r[[1, 2]]], " ", ToString[r[[1, 3]]],
         " ", ToString[Mod[r[[2]], PP]], "\n"], {r, cr}]],
    {w, {"num", "den"}}]],
 {i, 6}];
Close[st];
Print["Ecoef.txt written"];
