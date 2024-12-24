import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
from tabulate import tabulate

from utils.misc_number_theory import get_all_factors, get_prime_decomposition, get_digits
from utils.misc_utils import timer


@timer
def __main__():

    decimal_expansion = []
    for i in range(1, 10 ** 6):
        decimal_expansion.extend(get_digits((i)))

    product = 1
    for x in range(7):
        digit = int(decimal_expansion[10 ** x - 1])
        print(f"For {10 ** x}, digit is {digit}")
        product *= digit
    
    print(product)

__main__()
