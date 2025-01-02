import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
import itertools
from tabulate import tabulate

import utils.misc_number_theory as mnt
import utils.misc_utils as mu


@mu.timer
def __main__():

    answer = 0

    pentagonal_numbers = []

    diffs: Dict[tuple, bool] = {}
    sums: Dict[tuple, bool] = {}

    n = 1

    pairs_to_check = []

    while n < 10000:

        p_n = int((n * (3 * n - 1)) / 2)
        print(p_n)
        pentagonal_numbers.append(p_n)


        if len(pentagonal_numbers) == 1:
            n += 1
            continue

        for j in range(1, n):
            pair = (j, n)
            p_j = pentagonal_numbers[j - 1]
            p_k = pentagonal_numbers[n - 1]
            diff = p_k - p_j
            
            if diff in pentagonal_numbers:
                
                sum = p_k + p_j

                pairs_to_check.append(pair)
            
        n += 1

        for pair in pairs_to_check:
            
            j, k = pair[0], pair[1]
            p_j = pentagonal_numbers[j - 1]
            p_k = pentagonal_numbers[k - 1]
            sum = p_k + p_j

            if sum > p_n:
                continue
            
            if sum == p_n:
                print(j, k, p_j, p_k, sum)
                return (j, k, p_k - p_j)

            # pairs_to_check = [p for p in pairs_to_check if p != pair]

    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")


# WLOG let P_j < P_k
# We have that P_k - P-j = P_a and P_k + P_j = P_b
# Thus 2 * P_k = P_a + P_b
# k * (3k - 1) = (a * (3a - 1) + b * (3b - 1)) / 2