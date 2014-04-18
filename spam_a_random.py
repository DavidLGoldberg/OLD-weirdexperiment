#!/usr/bin/env python
import random, itertools

rand = random.choice((0, 1))

for _ in itertools.repeat(None, 1000000):
    print rand
