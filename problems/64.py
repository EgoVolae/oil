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

    answer = 1  # We know that 2 has an odd period, and the code below doesn't work for 2, so we start at 3

    for x in range(3, 10_001):

        if int(math.sqrt(x)) == math.sqrt(x):
            continue

        integers = []
        target_frac = mnt.RadicalFraction(1, 0, 0, 1, x)
        seen_fracs = [target_frac]

        while True:

            integer, fraction = target_frac.to_integer_and_fraction()
            recip = fraction.reciprocal
            transformed_frac = recip.transform()
            cancelled_frac = transformed_frac.cancel()
            target_frac = cancelled_frac

            integers.append(integer)

            if target_frac in seen_fracs:
                break

            seen_fracs.append(target_frac)

        period = len(integers) - 1

        print(f"{x=}, {period=}, {integers=}")

        if period % 2 == 1:
            answer += 1

    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")