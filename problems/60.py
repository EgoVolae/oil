import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
from tabulate import tabulate
import itertools
import numpy as np
import collections

import utils.misc_number_theory as mnt
import utils.misc_utils as mu


@mu.timer
def __main__():

    answer = 0

    primes = set()
    valid_pairs = set()

    x = 2
    while x < 10000:
        
        x_partners = list()

        primes_to_add = {x}

        if x not in primes:
            if not mnt.lazy_is_prime(x):
                x += 1
                continue

        x_digits = mnt.get_digits(x)

        for p in primes:

            if p > x:
                continue

            p_digits = mnt.get_digits(p)

            first_concat = int("".join(x_digits + p_digits))
            second_concat = int("".join(p_digits + x_digits))

            if first_concat not in primes:
                if not mnt.lazy_is_prime(first_concat):
                    continue
                primes_to_add.add(first_concat)
                
            if second_concat not in primes:
                if not mnt.lazy_is_prime(second_concat):
                    continue
                primes_to_add.add(second_concat)
            
            valid_pairs.add(frozenset({x, p}))

            x_partners.append(p)

        if len(x_partners) >= 4:
            print(f"{x=}, {x_partners=}")

            for comb in itertools.combinations(x_partners, r=4):
                successes = 0
                for pair in itertools.combinations(comb, r=2):

                    if frozenset(pair) in valid_pairs:
                        successes += 1
                
                if successes == 6:
                    print(f"FOUND IT")
                    print(f"{x=}, {comb=}")
                    return x + sum(comb)

        primes = primes.union(primes_to_add)
        x += 1

    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")