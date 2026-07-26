#!/bin/bash
D=/home/ubuntu/fable-episode-2/zeta-math-2/work/z5star
until [ -f $D/nsweepB_0_24.pkl ]; do sleep 20; done
sleep 5
cd $D
echo "=== boundary solve over the whole sweep ==="
PYTHONDONTWRITEBYTECODE=1 python3 -u $D/bnd.py nsweepB_0_24.pkl 11 2>&1 | tail -6
echo "=== boundary lift ==="
PYTHONDONTWRITEBYTECODE=1 python3 -u $D/bndlift.py 2>&1 | tail -12
