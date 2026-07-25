#!/bin/bash
DIR=/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5
TRACE=$DIR/certQ3_launch.trace
WAITPID=1311963
while kill -0 "$WAITPID" 2>/dev/null; do sleep 15; done
echo "certQ2 seat freed at $(date); launching kk pieces" >> "$TRACE"
cd "$DIR" || exit 1
JOBS=kk:C,kk:B,kk:A,kk:D DMAX=10 MEMCAP=3000000000 LADDERCAP=1800 FREECAP=420 \
  timeout 11000 math < certQ3.wl > certQ3_kk.stdout 2>&1
echo "certQ3 kk exited rc=$? at $(date)" >> "$TRACE"
