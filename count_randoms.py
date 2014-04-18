#!/usr/bin/env python
import random, itertools

counts = {0: 0, 1: 0}

for _ in itertools.repeat(None, 10000000):
    counts[random.choice((0,1))] += 1

print 'zero:' + str(counts[0]) + ' ' + 'one:' + str(counts[1])
print 'difference ======> ' + str(abs(counts[0] - counts[1]))
