#!/bin/bash
# Properly-resourced rerun: the 1991s abort was on a 2.5GB cap set defensively while
# the E-route run was co-resident. RSS was growing 0.036 GB/min (0.92 -> 2.10 GB over
# 33 min), i.e. NOT diverging -- unlike E(vtilde), which ran at 3.6 GB/min. The box is
# now empty, so give the single sanctioned direct attempt a real budget.
DIR=/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5
cd "$DIR" || exit 1
echo "certRFD RESOURCED ORD=lk MEMCAP=9G ANNCAP=5400 START $(date)" >> "$DIR/certRF_launch.trace"
ORD=lk DMAX=5 MEMCAP=9000000000 ANNCAP=5400 CT1CAP=3600 LADDERCAP=3600 FREECAP=900 \
  timeout 11000 math < certRFD.wl > certRFD_lk.stdout 2>&1
echo "certRFD RESOURCED exited rc=$? at $(date)" >> "$DIR/certRF_launch.trace"
