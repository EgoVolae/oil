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


def b_gen_func(n: int) -> int:
    
    if n == 0:
        return 2

    if n == 1:
        return 1
    
    if n % 3 != 2:
        return 1
    
    return int(2 * ((n + 1) / 3))


@mu.timer
def __main__():

    answer = 0

    As, Bs = mnt.get_first_m_continued_fractions(100, b_gen_func)
    answer = sum([int(x) for x in mnt.get_digits(As[-1])])

    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")