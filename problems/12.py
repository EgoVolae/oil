import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.misc_number_theory import get_all_factors

num_factors = 0
target_triangular_num = 1
counter = 2
while num_factors < 500:
    
    factors = get_all_factors(target_triangular_num)
    num_factors = len(factors)
    target_triangular_num += counter
    counter += 1

print(target_triangular_num)