import os
import random
import statistics
from heapq import heapify, heappop, heappush
from decimal import *

# print(os.getcwd())

# print(random.sample(range(100), 10))

# print(random.random())

# print(random.randrange(24))

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

print(statistics.mean(data))

print(statistics.median(data))

print(statistics.variance(data))

data = [1, 2, 3, 5, 7, 9, 11]
heapify(data)
heappush(data, 6)
print([heappop(data) for i in range(8)])

print(sum([Decimal("0.1")] * 10) == Decimal("1.0"))

print(sum([0.1] * 10) == 1.0)
