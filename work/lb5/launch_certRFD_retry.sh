#!/bin/bash
# If certRFD D1 hits the 2700s TIME cap while memory is FLAT (~1.7GB, i.e. not
# diverging), the cap was too tight, not a verdict. Relaunch once with a real budget.
DIR=/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5
cd "$DIR" || exit 1
for i in $(seq 1 400); do
  grep -q "TIME ABORT" "$DIR/certRFD_lk.log" && break
  grep -q "ALL DONE" "$DIR/certRFD_lk.log" && exit 0
  [ -s "$DIR/RFD_ann.m" ] && exit 0
  sleep 15
done
grep -q "TIME ABORT" "$DIR/certRFD_lk.log" || exit 0
cp certRFD_lk.log certRFD_lk_ANNCAP2700.log
echo "certRFD RELAUNCH ANNCAP=5400 START $(date)" >> "$DIR/certRF_launch.trace"
ORD=lk DMAX=5 MEMCAP=6000000000 ANNCAP=5400 CT1CAP=3600 LADDERCAP=3600 FREECAP=900 \
  timeout 12000 math < certRFD.wl > certRFD_lk.stdout 2>&1
echo "certRFD RELAUNCH exited rc=$? at $(date)" >> "$DIR/certRF_launch.trace"
