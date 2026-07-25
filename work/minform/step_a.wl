(* Step A: exact verification B_min(n) == b_n for n <= 40 *)
A[n_,k_] := Binomial[n,k]^2 Binomial[n+k,k]^2;
H3[m_] := Sum[1/j^3,{j,1,m}];
u[n_,m_] := (-1)^(m-1)/(2 m^3 Binomial[n,m] Binomial[n+m,m]);
c[n_,k_] := H3[n] + Sum[u[n,m],{m,1,k}];
Bmin[n_] := Sum[A[n,k](2 H3[n] - H3[k]),{k,0,n}];
bcl[n_]  := Sum[A[n,k] c[n,k],{k,0,n}];
diffs = Table[Bmin[n]-bcl[n],{n,0,40}];
Print["Bmin - b, n=0..40 all zero? ", Union[diffs]];
Print["b_1,b_2,b_3,b_5 = ", {bcl[1],bcl[2],bcl[3],bcl[5]}];
Print["Bmin_1,2,3,5      = ", {Bmin[1],Bmin[2],Bmin[3],Bmin[5]}];
a[n_] := Sum[A[n,k],{k,0,n}];
Print["a_n n=0..6: ", Table[a[n],{n,0,6}]];
(* Apery recurrence check on Bmin numerically *)
p[n_] := 34n^3+51n^2+27n+5;
L[u_] := Table[(n+1)^3 u[[n+2]] - p[n] u[[n+1]] + n^3 u[[n]], {n,1,38}];
bl = Table[Bmin[n],{n,0,40}];
Print["L[Bmin] zero? ", Union[L[bl]]];
al = Table[a[n],{n,0,40}];
Print["L[a] zero? ", Union[L[al]]];
