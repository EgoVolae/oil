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
    n = 1111
    for B in range(1, n+1):
        for r in range(n + 1):

            if B == 1:
                answer += 1
                continue

            c = math.comb(n, r)

            factors = sorted(mnt.get_all_factors(c), reverse=True)

            for f in factors:
                
                if f == 1:
                    answer += 1
                    break
                print(f"{r=}, {B=}, {c=}, {f=}")
                prime_decomp = mnt.get_prime_decomposition(f)
                if max(prime_decomp) <= B:

                    print(f"For decomposing {c}, we have that factor {f} is {B}-smooth")
                    answer += f
                    break

    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")