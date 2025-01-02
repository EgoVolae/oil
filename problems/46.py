import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
from tabulate import tabulate

import utils.misc_number_theory as mnt
import utils.misc_utils as mu


@mu.timer
def __main__():

    x = 2
    answer = 0
    known_primes = []
    known_double_squares = [2]

    covered_composites = set()

    while x < 50_000:

        if math.sqrt(x) == int(math.sqrt(x)):
            known_double_squares.append(2 * x)

            for p in known_primes:
                covered_composites.add(p + 2 * x)
        
        if x % 2 == 0 and x != 2:
            x += 1
            continue

        if mnt.lazy_is_prime(x):
            known_primes.append(x)
            
            for ds in known_double_squares:
                covered_composites.add(x + ds)

            x += 1
            continue

        if x in covered_composites:
            x += 1
            continue

        answer = x
        break
        
    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")