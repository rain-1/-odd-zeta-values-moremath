#!/bin/bash
# S1/S2/S3 of P1e session 6 -- the decisive monolithic run on the refold vtilde.
DIR=/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5
cd "$DIR" || exit 1
echo "certRF ORD=lk START $(date)" >> "$DIR/certRF_launch.trace"
ORD=lk DMAX=4 MEMCAP=5000000000 ANNCAP=2700 CT1CAP=3600 LADDERCAP=2700 FREECAP=900 \
  timeout 13000 math < certRF.wl > certRF_lk.stdout 2>&1
echo "certRF ORD=lk exited rc=$? at $(date)" >> "$DIR/certRF_launch.trace"
