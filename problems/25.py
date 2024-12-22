import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List
import math
from utils.misc_number_theory import get_all_factors, get_prime_decomposition
from utils.misc_utils import timer

@timer
def __main__():
    index = 3 

    f_n = 0
    f_n_minus_2 = 1
    f_n_minus_1 = 2
    while f_n < 10 ** 999:
        f_n = f_n_minus_1 + f_n_minus_2
        f_n_minus_2 = f_n_minus_1
        f_n_minus_1 = f_n
        index += 1
    print(f_n, index)
__main__()
