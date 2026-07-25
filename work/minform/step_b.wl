$RISC = "/home/ubuntu/fable-episode-2/zeta-math-2/RISC/";
Get[$RISC<>"fastZeil.m"];
A[n_,k_] := Binomial[n,k]^2 Binomial[n+k,k]^2;
res = Zb[Binomial[n,k]^2 Binomial[n+k,k]^2, {k,0,n}, n, 2];
Print["Zb result: ", InputForm[res]];
