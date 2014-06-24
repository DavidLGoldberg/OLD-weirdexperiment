Nothing to see here!

This project does nothing.  It was just some experiments on using gnu parallel.

Command to run:

➜  weirdexperiment git:(master) ✗ cat results | grep Same | cut -d' ' -f 2 | awk '{s+=$1} END {print s}'
