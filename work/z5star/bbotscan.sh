#!/bin/bash
cd /home/ubuntu/fable-episode-2/zeta-math-2/work/z5star
for A in "M2 16" "M7 12" "F1 10" "G1 12" "M0 24"; do
  set -- $A
  PYTHONDONTWRITEBYTECODE=1 timeout 1200 python3 -u bbotdiag3.py 9 $1 $2 8 2>&1 | grep -E "class 1 |ALL classes" | sed "s/^/[$1 s$2] /"
done
