#!/bin/bash
DIR=/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5
cd "$DIR" || exit 1
echo "certRF RETRY MEMCAP=8.5G START $(date)" >> "$DIR/certRF_launch.trace"
ORD=lk DMAX=4 MEMCAP=8500000000 ANNCAP=2700 CT1CAP=3600 LADDERCAP=2700 FREECAP=900 \
  timeout 9000 math < certRF.wl > certRF_lk.stdout 2>&1
echo "certRF RETRY exited rc=$? at $(date)" >> "$DIR/certRF_launch.trace"
