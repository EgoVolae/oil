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

    figures = set()

    for x in range(1, 20):
        power = 1
        while power < 50:
            candidate = x ** power
            if len(str(candidate)) == power:
                print(f"{x=}, {power=}, {candidate=}")
                figures.add(candidate)
            power += 1
    answer = len(figures)
    print(9 ** 22)
    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")