#!/bin/bash
# Sanctioned ORD swap. Waits for RFD_ann.m so it LOADS the checkpoint rather than
# recomputing it (Annihilator is ORD-independent; only ct1/ct2 differ), and so two
# kernels never write the same checkpoint file.
DIR=/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5
cd "$DIR" || exit 1
for i in $(seq 1 400); do [ -s "$DIR/RFD_ann.m" ] && break; sleep 15; done
[ -s "$DIR/RFD_ann.m" ] || { echo "RFD_ann.m never appeared; ORD swap not launched at $(date)" >> "$DIR/certRF_launch.trace"; exit 0; }
sleep 20
echo "certRFD ORD=kl START $(date)" >> "$DIR/certRF_launch.trace"
ORD=kl DMAX=5 MEMCAP=3000000000 ANNCAP=2700 CT1CAP=3600 LADDERCAP=3600 FREECAP=900 \
  timeout 10000 math < certRFD.wl > certRFD_kl.stdout 2>&1
echo "certRFD ORD=kl exited rc=$? at $(date)" >> "$DIR/certRF_launch.trace"
