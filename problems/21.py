import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import Dict, List
import math
from utils.misc_number_theory import get_all_factors

num_to_factor_sum = {
    x : sum(get_all_factors(x, proper=True)) for x in range(0,10_001)
}

results = []

for x in range(1, 10_001):
    factor_sum = num_to_factor_sum[x]
    
    if factor_sum > 10_000:
        continue
    that_number_factor_sum = num_to_factor_sum[factor_sum]
    if that_number_factor_sum == x:
        if that_number_factor_sum == factor_sum:
            continue

        results.append(x)

print(sum(results))