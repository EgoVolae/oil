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

    terms = [(3,2)]

    for x in range(1, 1001):

        t = terms[x - 1]

        t = (t[0] + t[1], t[1])  # Adding 1 
        t = (t[1], t[0])  # Taking reciprocal
        t = (t[0] + t[1], t[1])  # Adding 1

        terms.append(t)

        if len(mnt.get_digits(t[0])) > len(mnt.get_digits(t[1])):
            answer += 1

            print(t)

    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")