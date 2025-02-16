import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple, Set
import math
from tabulate import tabulate
import itertools
import numpy as np

import utils.misc_number_theory as mnt
import utils.misc_utils as mu


@mu.timer
def __main__():

    answer = 0
    min_diff = 1
    for b in reversed(range(1, 1_000_000)):

        if b == 7:
            continue

        potential_a = math.floor(b * 3 / 7)
        if potential_a == b * 3 / 7:
            continue
        frac = potential_a / b
        diff = 3 / 7 - frac
        if diff < min_diff:
            answer = potential_a, b
            min_diff = diff
            print(f"New lowest: {potential_a}/{b} with {diff=}")


    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")