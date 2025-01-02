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

    T_xs= [x * (x + 1) / 2 for x in range(286, 100_000)]
    P_xs= [x * (3 * x - 1) / 2 for x in range(100_000)]
    H_xs= [x * (2 * x - 1) for x in range(100_000)]

    intersection = set(T_xs).intersection(set(P_xs)).intersection(set(H_xs))
    answer = int(list(intersection)[0])

    return answer


answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")