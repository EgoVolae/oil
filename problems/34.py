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
    
    UPPER_LIMIT = 10 ** 7

    factorials = {i: math.factorial(i) for i in range(10)}

    results = []

    for x in range(3, UPPER_LIMIT + 1):

        digits = [int(i) for i in list(str(x))]

        factorial_sum = sum([factorials[i] for i in digits])

        if factorial_sum == x:
            print(f"Found {x}")
            results.append(x)

    print(sum(results))


__main__()
