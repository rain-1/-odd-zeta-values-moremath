#!/bin/bash
# Phase-2 sweeps with search4 (exact q1/q2 test + refined shift-invariant growth test).
cd /home/ubuntu/fable-episode-2/zeta-math-2/work/z7ss
run () {  # A B W Z tag nshard
  local A=$1 B=$2 W=$3 Z=$4 tag=$5 NS=$6
  rm -f hits_$tag_*.txt hits_$tag_*.txt.growth log_$tag_*.err
  for s in $(seq 0 $((NS-1))); do
    nohup ./search4 $A $B $W $Z hits_${tag}_$s.txt $s $NS >/dev/null 2> log_${tag}_$s.err &
  done
  wait
  echo "== $tag (A=$A B=$B W=$W Z=$Z) =="
  cat log_${tag}_*.err | awk '{for(i=1;i<=NF;i++){split($i,a,"=");
    if(a[1]=="leaves")L+=a[2]; if(a[1]=="valid")V+=a[2]; if(a[1]=="pruned")P+=a[2];
    if(a[1]=="q1hits")H1+=a[2]; if(a[1]=="q1q2hits")H2+=a[2]; if(a[1]=="growthcand")G+=a[2]}}
    END{print "  leaves="L"  growth-feasible="V"  pruned="P"  matched q1="H1"  matched q1&q2="H2"  growth-matched="G}'
  echo "  q1&q2 hits:"; cat hits_${tag}_*.txt 2>/dev/null | sed 's/^/    /'
  echo "  growth hits (first 25):"; cat hits_${tag}_*.txt.growth 2>/dev/null | head -25 | sed 's/^/    /'
  echo "  total growth hits: $(cat hits_${tag}_*.txt.growth 2>/dev/null | wc -l)"
}
run "$@"
