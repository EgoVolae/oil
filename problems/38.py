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
    
    for x in reversed(range(9182, 10000)):

        digits_x = get_digits(x)
        digits_2x = get_digits(2 * x)

        if (len(digits_x) != len(set(digits_x))) or (len(digits_2x) != len(set(digits_2x))):
            continue
        
        if len(set(digits_x).intersection(set(digits_2x))) != 0:
            continue
        
        if "0" in digits_x or "0" in digits_2x:
            continue

        print(digits_x, digits_2x)
        digits_x.extend(digits_2x)
        answer = "".join(digits_x)
        print(f"answer={answer}")
        break

__main__()
