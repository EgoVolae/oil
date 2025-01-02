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

    x = 100_000

    while True:

        x_digits = sorted(mnt.get_digits(x))

        for k in range(2, 7):

            multiple = k * x
            multiple_digits = sorted(mnt.get_digits(multiple))

            if multiple_digits != x_digits:                
                break

            if k == 6:
                
                multiples = [k * x for k in range(2, 7)]

                print(f"Found answer for {x=}, multiples are: {multiples}")

                return x
        
        x += 1

    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")