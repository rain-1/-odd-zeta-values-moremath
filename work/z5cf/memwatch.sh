#!/bin/bash
# external RSS / free-memory watch for the z5cf kernels
D=/home/ubuntu/fable-episode-2/zeta-math-2/work/z5cf
while true; do
  TS=$(date +%H:%M:%S)
  FREE=$(free -m | awk '/^Mem:/{print $4"/"$7}')
  RSS=$(ps -eo pid,rss,args | grep -E 'WolframKernel' | grep -v grep | grep -v AgentTools | awk '{printf "%s:%.2fGB ", $1, $2/1048576}')
  echo "$TS free/avail=${FREE}M $RSS" >> $D/memwatch.log
  sleep 20
done
