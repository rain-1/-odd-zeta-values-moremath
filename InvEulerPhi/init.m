(* This package is a .m form of a notebook due to Maxim Rytin and *)
(* freely available from http://library.wolfram.com/infocenter/MathSource/696/ *)

BeginPackage["InvEulerPhi`"]

InvEulerPhi::usage = "InvEulerPhi[m] gives the inverse of the Euler totient
function. The procedure is due to Maxim Rytin and freely available from
http://library.wolfram.com/infocenter/MathSource/696/"

Begin["`Private`"]

InvEulerPhi[m_Integer] :=
  Module[{Lp, Lq, r, s, r0, Mdiv},

         Switch[m,
                0, Return[{0}],
                1, Return[{1, 2}],
                _?(OddQ[#] || Negative[#]&), Return[{}]
               ];
         {Lp, Lq, r, s, r0, Mdiv} = init[m];
         Return[Sort[main[m, Lp, Lq, r, s, r0, Mdiv]]]
        ]

init[m_] :=
  Module[{Lb, Lpq, Lp, Lq, r, s, r0, Mdiv},
         {Lq, Lb} = Transpose[FactorInteger[m]];
         Lp = genp[Lb, Lq];
         Lpq = Intersection[Lp, Lq];
         {Lp, Lq} = Join[Lpq, Complement[#, Lpq]]& /@ {Lp, Lq};
         {r, s, r0} = Length /@ {Lp, Lq, Lpq};
         Mdiv = Cases[Range[r], x_ /; Mod[Lp[[x]] - 1, #] == 0]& /@ Lq;
	 Return[{Lp, Lq, r, s, r0, Mdiv}]
        ]

genp[Lb_, Lq_] :=
  Module[{Lpow, tmp, Lp},
         Lpow = MapThread[Table[#1^i, {i, 0, #2}]&, {Lq, Lb}];
         Lp = {};
         Outer[If[PrimeQ[tmp = Times[##] + 1],
                  Lp = {Lp, tmp}
                 ]&,
               Sequence @@ Lpow
              ];
         Lp = Flatten[Lp];
	 Return[Lp]
        ]

main[m_, Lp_, Lq_, r_, s_, r0_, Mdiv_] :=
  Module[{ans = {}, wrk, threshold = 100, Lstate, Ladd, quo, indx, i},
         wrk = {{Table[0, {r}], m}};
         wrk[[1, 1, 1]] = -1;
         For[i = 1, i <= Length[wrk], i++,
             If[i == threshold + 1,
                ans = {ans, genans[m, Take[wrk, threshold], Lp, Lq, s, r0]};
                wrk = Drop[wrk, threshold];
                i = 1
               ];
             {Lstate, quo} = wrk[[i]];
             indx = bestcand[Lstate, quo, Lq, s, r0, Mdiv];
             Ladd = gencand[Lstate, indx, r, r0, Mdiv];
             wrk = Join[wrk, addcand[Lstate, quo, Ladd, Lp, r] ]
            ];
         Flatten[{ans, genans[m, wrk, Lp, Lq, s, r0]}]
        ]

genans[m_, L_, Lp_, Lq_, s_, r0_] :=
  Module[{ans = {}, Lstate, quo, res, add2, i, j},
         For[i = 1, i <= Length[L], i++,
             {Lstate, quo} = L[[i]];
             For[add2 = 0, add2 <= 1, add2++,
                 If[add2 == 1,
                    Lstate[[1]] = 1
                   ];
                 For[j = 1, j <= s, j++,

                     If[((j <= r0 && Lstate[[j]] != 1) || j > r0) &&
                        Mod[quo, Lq[[j]] ] == 0,
                        Break[]
                       ]
                    ];
                 If[j != s + 1,
                    Continue[]
                   ];
                 res = Cases[Transpose[{Lp, Lstate}], {x_, 1} -> x];
                 res = m Times @@ res / Times @@ (res - 1);
                 ans = {ans, res}
                ]
            ];
         ans
        ]

bestcand[Lstate_, quo_, Lq_, s_, r0_, Mdiv_] :=
  Module[{len = Infinity, indx = 0, cur, i},
         For[i = 1, i <= s, i++,
             If[((i <= r0 && Lstate[[i]] != 1) || i > r0) &&
                Mod[quo, Lq[[i]]] == 0,
                cur = Length[Mdiv[[i]]];
                If[cur < len,
                   len = cur;
                   indx = i
                  ]
               ]
            ];
         indx
        ]

gencand[Lstate_, indx_, r_, r0_, Mdiv_] :=
  Module[{Ladd},
         Ladd = If[indx != 0,
                   If[indx <= r0,
                      Prepend[Mdiv[[indx]], indx],
                      Mdiv[[indx]]
                     ],
                   Range[r]
                  ];
         Select[Ladd, Lstate[[#]] == 0&]
        ]

addcand[Lstate_, quo_, Ladd_, Lp_, r_] :=
  Module[{ans = {}, Lstate2, quo2, len, i},
         len = Length[Ladd];
         For[i = 1, i <= len, i++,
             Lstate2 = ReplacePart[Lstate, 1, Ladd[[i]]];
             quo2 = quo / (Lp[[Ladd[[i]]]] - 1);
             (Lstate2[[Ladd[[#]]]] = -1)& /@ Range[i - 1];

             If[Lstate2[[#]] == 0 && Mod[quo2, Lp[[#]] - 1] != 0,
                Lstate2[[#]] = -1
	       ]& /@ Range[r];
             AppendTo[ans, {Lstate2, quo2}]
            ];
         ans
        ]


End[]
EndPackage[]
