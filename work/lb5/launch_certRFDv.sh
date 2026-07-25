#!/bin/bash
DIR=/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5
cd "$DIR" || exit 1
echo "certRFDv (fold v, 12 symbols) START $(date)" >> "$DIR/certRF_launch.trace"
ORD=lk DMAX=4 MEMCAP=3000000000 ANNCAP=600 CT1CAP=600 LADDERCAP=300 FREECAP=180 \
  timeout 790 math < certRFDv.wl > certRFDv_lk.stdout 2>&1
echo "certRFDv exited rc=$? at $(date)" >> "$DIR/certRF_launch.trace"
