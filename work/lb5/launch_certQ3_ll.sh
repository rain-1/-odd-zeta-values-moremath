#!/bin/bash
# ll:B is NOT blocked -- §18.18 showed its 37-min DFiniteTimes failure was the old
# pipeline's 4.8 MB gb.  Re-run it through certQ3.wl, where the gb will be small.
DIR=/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5
TRACE=$DIR/certQ3_launch.trace
WAITPID="${WAITPID:-1332392}"
while kill -0 "$WAITPID" 2>/dev/null; do sleep 15; done
echo "seat freed (pid $WAITPID gone) at $(date); launching ll:B + n3" >> "$TRACE"
cd "$DIR" || exit 1
JOBS=ll:B,n3:C,n3:B DMAX=10 MEMCAP=3000000000 LADDERCAP=1800 FREECAP=420 \
  timeout 10000 math < certQ3.wl > certQ3_ll.stdout 2>&1
echo "certQ3 ll exited rc=$? at $(date)" >> "$TRACE"
