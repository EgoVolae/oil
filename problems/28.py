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
    
    answer = 1 + sum([(4 * n ** 2 - 6 * n + 6) for n in range(3, 1003, 2)])
    print(f"{answer=}")

__main__()
