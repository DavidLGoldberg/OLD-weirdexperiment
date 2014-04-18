#!/usr/bin/env python
import random, itertools

counts = {0: 0, 1: 0}

for _ in itertools.repeat(None, 1000000):
    counts[random.choice((0,1))] += 1

if counts[0] > counts[1]:
    print '0'
else:
    print '1'
