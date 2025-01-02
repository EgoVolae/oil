import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
from tabulate import tabulate
import itertools

import utils.misc_number_theory as mnt
import utils.misc_utils as mu


@mu.timer
def __main__():

    answer = 0

    candidate_four_digit_primes = set()

    four_digit_prime_collections = dict()

    for x in range(1_000, 10_000):

        if not mnt.lazy_is_prime(x):
            x += 1
            continue
        
        unique_digits = frozenset(mnt.get_digits(x))

        if unique_digits not in four_digit_prime_collections.keys():
            four_digit_prime_collections[unique_digits] = {x}
            x += 1
            continue

        four_digit_prime_collections[unique_digits].add(x)

        x += 1
    
    for digits, elements in four_digit_prime_collections.items():
        if len(elements) < 3:
            continue

        for combination in itertools.combinations(elements, r=3):
            combination = sorted(combination)

            if 1487 in combination:
                continue

            if combination[2] - combination[1] == combination[1] - combination[0]:
                answer = "".join([str(elem) for elem in combination])
                print(combination)
                break

    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")