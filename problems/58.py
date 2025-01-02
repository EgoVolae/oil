import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
from tabulate import tabulate
import itertools
import numpy as np

import utils.misc_number_theory as mnt
import utils.misc_utils as mu


@mu.timer
def __main__():

    answer = 0
    
    target = 1
    side = 0
    layer = 1

    running_numerator = 0
    running_denominator = 1

    while True:

        while side < 4:

            target = target + 2 * layer
            
            if mnt.lazy_is_prime(target):
                running_numerator += 1
            else:
                running_numerator += 0
            side += 1

            running_denominator += 1
        
        side = 0
        layer += 1

        prime_proportion = running_numerator / running_denominator

        if prime_proportion < 0.1:
            answer = 2 * layer - 1
            break

    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")