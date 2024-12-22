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

    ONE_MILLION = 1_000_000
    DIGITS = [x for x in range(10)]

    coefficients_for_1m = {i: 0 for i in range(1, 10)}

    remainder = ONE_MILLION
    for i in reversed(range(1, 10)):

        factorial = math.factorial(i)
        
        print(remainder)
        while remainder > factorial:

            remainder -= factorial
            coefficients_for_1m[i] += 1
        
        coefficient = coefficients_for_1m[i]

    answer = []

    remaining_digits = DIGITS
    for x in reversed(range(1,10)):

        coefficient = coefficients_for_1m[x]
        digit = remaining_digits[coefficient]
        answer.append(str(digit))
        remaining_digits = [y for y in remaining_digits if y != remaining_digits[coefficient]]
    
    answer = "".join(answer)
    print(answer)


__main__()
