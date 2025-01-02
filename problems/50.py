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

    primes = []

    current_leader = (0,0,0,0)

    primes = sorted(frozenset([x for x in range(5000) if mnt.lazy_is_prime(x)]))

    for chain_length in range(21, len(primes)):
        for idx in range(len(primes) - chain_length):

            candidate = sum(primes[idx: idx + chain_length])

            if candidate > 1_000_000:
                continue

            if mnt.lazy_is_prime(candidate):                
                if chain_length > current_leader[0]:
                    current_leader = (chain_length, candidate, primes[idx], primes[idx + chain_length - 1])

    answer = current_leader

    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")