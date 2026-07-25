#!/bin/bash
# FINAL long continuation of the ONE live route (PHASE2_CERTS 19.4/19.10).
# Justification: Annihilator[T*vtilde] is TIME-bound, not memory-bound -- at 74 min it
# was at 3.87 GB against a 9 GB cap, i.e. the 5400 s ANNCAP fires first. This is the
# only object in the campaign with that diagnosis. Fires ONLY if the 5400 s run
# time-aborted; exits immediately if it returned or checkpointed.
DIR=/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5
cd "$DIR" || exit 1
for i in $(seq 1 200); do
  [ -s "$DIR/RFD_ann.m" ] && exit 0
  grep -q "TIME ABORT" "$DIR/certRFD_lk.log" && break
  sleep 20
done
[ -s "$DIR/RFD_ann.m" ] && exit 0
grep -q "TIME ABORT" "$DIR/certRFD_lk.log" || exit 0
cp certRFD_lk.log certRFD_lk_ANNCAP5400.log
cp memwatch3.log memwatch_run4.log
echo "certRFD LONG ORD=lk MEMCAP=9G ANNCAP=20000 START $(date)" >> "$DIR/certRF_launch.trace"
ORD=lk DMAX=5 MEMCAP=9000000000 ANNCAP=20000 CT1CAP=5400 LADDERCAP=3600 FREECAP=900 \
  timeout 24000 math < certRFD.wl > certRFD_lk.stdout 2>&1
echo "certRFD LONG exited rc=$? at $(date)" >> "$DIR/certRF_launch.trace"
