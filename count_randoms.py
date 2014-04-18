import random

counts = {0: 0, 1: 0}

for i in range(1000000):
    counts[random.randint(0,1)] += 1

print 'zero:' + str(counts[0]) + ' ' + 'one:' + str(counts[1])
print 'difference ======> ' + str(abs(counts[0] - counts[1]))
