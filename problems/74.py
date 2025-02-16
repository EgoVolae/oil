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

    not_eligible = set()

    for x in range(2, 1_000_000):

        if x in not_eligible:
            continue

        start = x
        chain = [start]
        while True:
            digits = mnt.get_digits(chain[-1])
            sum_fact = sum([math.factorial(int(d)) for d in digits])
            if sum_fact in chain:
                break
            chain.append(sum_fact)

        if len(chain) < 60:
            not_eligible.update(set([y for y in chain if y > x]))
        if len(chain) == 60:
            answer += 1
        # if len(chain) > 60:
        #     not_eligible.update(set(chain[-60:]))
        # print(f"{x}: chain is: {chain}")
    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")