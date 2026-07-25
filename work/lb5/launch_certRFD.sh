#!/bin/bash
DIR=/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5
cd "$DIR" || exit 1
echo "certRFD ORD=lk START $(date)" >> "$DIR/certRF_launch.trace"
ORD=lk DMAX=5 MEMCAP=2500000000 ANNCAP=2700 CT1CAP=3600 LADDERCAP=3600 FREECAP=900 \
  timeout 12000 math < certRFD.wl > certRFD_lk.stdout 2>&1
echo "certRFD ORD=lk exited rc=$? at $(date)" >> "$DIR/certRF_launch.trace"
