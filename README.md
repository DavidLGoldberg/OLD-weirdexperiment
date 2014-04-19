Command to run:

➜  weirdexperiment git:(master) ✗ cat results | grep Same | cut -d' ' -f 2 | awk '{s+=$1} END {print s}'
