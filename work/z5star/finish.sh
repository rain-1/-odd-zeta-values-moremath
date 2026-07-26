#!/bin/bash
D=/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star
until [ -f $D/nsweep_6_24.pkl ] && [ $D/lift_Q.pkl -nt $D/nsweep_6_24.pkl ]; do sleep 30; done
cd $D
echo "=== emit2 ==="
PYTHONDONTWRITEBYTECODE=1 python3 -u $D/emit2.py 2>&1 | tail -35
echo "=== check6 (exact Q residual, n,k,l small) ==="
PYTHONDONTWRITEBYTECODE=1 timeout 3000 python3 -u $D/check6.py 4 2>&1 | tail -8
