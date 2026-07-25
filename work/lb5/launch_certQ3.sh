#!/bin/bash
# Waits for pid $WAITPID to exit, then runs certQ3.wl on $JOBS.
DIR=/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5
TRACE=$DIR/certQ3_launch.trace
JOBLIST="${JOBS:-n2:A,n2:C,n2:B,n2:D,n3:C,n3:B,n3:A,n3:D}"
WAITPID="${WAITPID:-1205156}"
while kill -0 "$WAITPID" 2>/dev/null; do sleep 15; done
echo "seat freed (pid $WAITPID gone) at $(date); launching JOBS=$JOBLIST" >> "$TRACE"
cd "$DIR" || exit 1
JOBS="$JOBLIST" DMAX=10 MEMCAP=3000000000 LADDERCAP=2700 FREECAP=600 \
  timeout 13000 math < certQ3.wl > certQ3_run1.stdout 2>&1
echo "certQ3 exited rc=$? at $(date)" >> "$TRACE"
