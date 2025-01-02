import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
from tabulate import tabulate
from itertools import permutations

from utils.misc_number_theory import get_all_factors, get_prime_decomposition, lazy_is_prime
from utils.misc_utils import timer


@timer
def __main__():
    
    for upper in reversed(range(2, 10)):

        digits = [str(x) for x in range(1, upper)]

        for p in permutations(digits):

            number = int("".join(p))
            if number % 2 == 0 or number % 3 == 0:
                continue

            if not lazy_is_prime(number):
                continue

            print(number)

__main__()
