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
    current_max_x = 0

    for D in range(2, 1001):

        if int(math.sqrt(D)) == math.sqrt(D):
            continue

        b_series = []
        target_frac = mnt.RadicalFraction(1, 0, 0, 1, D)
        seen_fracs = [target_frac]

        while True:

            integer, fraction = target_frac.to_integer_and_fraction()
            recip = fraction.reciprocal
            transformed_frac = recip.transform()
            cancelled_frac = transformed_frac.cancel()
            target_frac = cancelled_frac

            b_series.append(integer)

            if target_frac in seen_fracs:
                break

            seen_fracs.append(target_frac)

        period = len(b_series) - 1
        r = period - 1

        def b_gen_func(x: int) -> int:

            if x < len(b_series):
                return b_series[x]

            if x % period == 0:
                return b_series[-1]
            else:
                return b_series[x % period]
        
        A_series, B_series = mnt.get_first_m_continued_fractions(2 * period + 1 + 1, b_gen_func)

        continued_frac_index = r if r % 2 == 1 else 2 * r + 1
        x, y = A_series[continued_frac_index], B_series[continued_frac_index]

        print(f"{D=}, {x=}, {y=}")

        if x > current_max_x:
            answer = D
            current_max_x = x        
       
    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")