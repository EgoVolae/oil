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
    min_ratio = 2

    # We know that we want only two primes in the decomposition
    # We want these two primes to be very large. So they must both be quite close to sqrt(10_000_000)===3162
    eligible_primes = [p for p in mnt.get_all_primes_up_to(math.floor(10_000_000 / 1_000)) if abs(p - math.sqrt(10_000_000)) < 1_000]

    for i, j in itertools.product(eligible_primes, eligible_primes):
        x = i * j
        if x > 10_000_000:
            continue

        totient = mnt.totient_fast(x)

        x_digits = mnt.get_digits(x)
        totient_digits = mnt.get_digits(totient)
        
        if sorted(x_digits) == sorted(totient_digits):

            ratio = x / totient
            if ratio < min_ratio:
                min_ratio = ratio
                answer = x
                print(f"New lowest ratio: {x=}, {totient=}, ratio={x / totient}")

    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")