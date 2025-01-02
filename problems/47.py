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

    answer = 0
    running = 0
    x = 1

    while True:
        distinct_prime_factors = set(mnt.get_prime_decomposition(x))
        if len(distinct_prime_factors) >= 4:
            running += 1
        else:
            running = 0
        
        if running == 4:
            answer = x - 3
            break

        x += 1

    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")