(* Independent derivation of the Apery certificate by ansatz.
   Seek G(n,k) = A(n,k) R(n,k), R(n,k) = k^4 T(n,k) / ((n+1-k)^2 (n+k)^2),
   satisfying  (n+1)^3 A(n+1,k) - p(n) A(n,k) + n^3 A(n-1,k) = G(n,k+1)-G(n,k).
   Reduces to:  T(n,k+1)(n+1-k)^2(n+k)^2 - k^4 T(n,k) = RHSpoly.  *)
p[n_] := 34n^3+51n^2+27n+5;
RHSpoly = Expand[(n+1)^3 (n+k+1)^2 (n+k)^2 - p[n](n+1-k)^2(n+k)^2 + n^3 (n-k)^2 (n+1-k)^2];
Do[
  T = Sum[cc[i] k^i, {i,0,d}];
  eq = Expand[(T /. k->k+1)*(n+1-k)^2 (n+k)^2 - k^4 T - RHSpoly];
  sol = Solve[Thread[CoefficientList[eq,k]==0], Table[cc[i],{i,0,d}]];
  Print["d=",d,"  solutions: ", Length[sol]];
  If[Length[sol]>0,
    Tsol = Simplify[T /. First[sol] /. cc[_]->0];
    Print["  T = ", InputForm[Factor[Tsol]]];
    (* verify *)
    chk = Simplify[(Tsol/.k->k+1)*(n+1-k)^2(n+k)^2 - k^4 Tsol - RHSpoly];
    Print["  check zero: ", chk];
    Break[];
  ],
{d,2,8}];
