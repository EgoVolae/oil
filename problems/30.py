import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
from tabulate import tabulate

from utils.misc_number_theory import get_all_factors, get_prime_decomposition
from utils.misc_utils import timer


@timer
def __main__():
    
    MAX_POSSIBLE = 6 * 9 ** 5

    solutions = []

    for n in range(2, MAX_POSSIBLE + 1):

        digits = [int(x) for x in list(str(n))]
        fifth_power_sum = sum([d ** 5 for d in digits])
        if fifth_power_sum == n:
            solutions.append(n)
    
    print(solutions)
    print(f"answer={sum(solutions)}")

__main__()
