import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple, Set
import math
from tabulate import tabulate
from collections import defaultdict
import itertools
import numpy as np

import utils.misc_number_theory as mnt
import utils.misc_utils as mu


@mu.timer
def __main__():

    answer = 0

    L = 1_500_000
    relevant_triplets = mnt.get_pythagorean_triplets_up_to_x(math.floor(L / 2))

    results = defaultdict(int)

    for triplet in relevant_triplets:
        a, b, c = triplet
        p = a + b + c
        if p <= L:
            print(a, b, c, p)
            results[p] += 1

    answer = len([p for p, count in results.items() if count == 1])

    # L = 150_000

    # results = defaultdict(int)

    # for b in range(2, math.floor(L / 2)):
    #     ub_for_a = min(L - 2 * b, b)
    #     for a in range(2, ub_for_a):
    #         c = math.sqrt(a**2 + b**2)
            
    #         if c % 1 != 0:
    #             continue
            
    #         p = a + b + c

    #         if p > L:
    #             continue

    #         results[p] += 1
    
    # answer = len([p for p, count in results.items() if count == 1])

    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")