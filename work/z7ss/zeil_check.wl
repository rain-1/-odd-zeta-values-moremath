Get["/home/ubuntu/riscergosum/RISC/fastZeil.m"];
Print["--- fastZeil loaded ---"];
ap = Binomial[n, k]^2*Binomial[n + k, k]^2;
r1 = Zb[ap, {k, 0, n}, n, 2];
Print["Apery zeta(3) telescoper: ", r1];
q5 = Binomial[n + k, n]*Binomial[n, k]^2;
r2 = Zb[q5, {k, 0, n}, n, 3];
Print["inner weight-5 weight telescoper: ", r2];
Print["--- done ---"];
