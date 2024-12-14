import math

first_100_nat = [i for i in range(1,101)]

sum_of_squares = sum([i**2 for i in first_100_nat])
squared_sum = sum(first_100_nat) ** 2

result = squared_sum - sum_of_squares
print(result)