#!/bin/bash
D=/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star
until [ -f $D/nsweepB_0_24.pkl ]; do sleep 30; done
sleep 5
cd $D
echo "=== emit3 (B-bot gauge) ==="
PYTHONDONTWRITEBYTECODE=1 python3 -u $D/emit3.py nsweepB_0_24.pkl 2>&1 | tail -8
echo "=== emit2 ==="
PYTHONDONTWRITEBYTECODE=1 python3 -u $D/emit2.py 2>&1 | tail -35
echo "=== check6 (exact Q, n,k,l <= 6) ==="
PYTHONDONTWRITEBYTECODE=1 timeout 3000 python3 -u $D/check6.py 6 2>&1 | tail -4
