import math
import numpy

hits = list()

for num in range(1, 1000):
    if num % 3 == 0 or num % 5 == 0:
        hits.append(num)

print(hits)
print(sum(hits))