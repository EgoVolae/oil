import math
from itertools import product

squares = [i ** 2 for i in range(1, 1001)]

trips = []
for x, y in product(squares, squares):
    if abs(x - y) not in squares:
        continue
    triplet = {int(math.sqrt(x)), int(math.sqrt(y)), int(math.sqrt(abs(x-y)))}
    if triplet not in trips:
        trips.append(triplet)

for triplet in trips:
    if sum(triplet) == 1000:
        print(math.prod(triplet))
        break
