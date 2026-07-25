#!/bin/bash
# Wait for a Wolfram licence seat to free (cap is 3: MCP + two compute kernels),
# then run certQ2.wl on the given JOBS list.  Written as a FILE because the
# harness collapses newlines in `bash -c` strings, which silently turned an
# earlier inline version into one long `echo`.
DIR=/home/ubuntu/fable-episode-2/zeta-math-2/work/lb5
TRACE=$DIR/certQ2_launch.trace
JOBLIST="${JOBS:-n1:A,n1:C,n1:B,n1:D,kk:C,kk:B,kk:A,kk:D}"
WAIT_PIDS="${WAITPIDS:-1205156 1246566}"

while true; do
  alive=0
  for p in $WAIT_PIDS; do
    if kill -0 "$p" 2>/dev/null; then alive=$((alive+1)); fi
  done
  # fire as soon as ANY of the watched kernels has exited
  n=0; for p in $WAIT_PIDS; do n=$((n+1)); done
  if [ "$alive" -lt "$n" ]; then break; fi
  sleep 15
done

echo "seat freed at $(date); launching JOBS=$JOBLIST" >> "$TRACE"
cd "$DIR" || exit 1
JOBS="$JOBLIST" DMAX=10 MEMCAP=3000000000 timeout 14000 math < certQ2.wl > certQ2_run1.stdout 2>&1
echo "certQ2 exited rc=$? at $(date)" >> "$TRACE"
