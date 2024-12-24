import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
from tabulate import tabulate
from itertools import product

from utils.misc_number_theory import get_all_factors, get_prime_decomposition, lazy_is_prime, get_digits
from utils.misc_utils import timer


@timer
def __main__():
    
    candidate_digits = ["1","3","7","9"]
    known_primes = []
    results = []
    for l in range(2, 9):

        for digits in product(candidate_digits, repeat=l):
            
            if (digits[0] in ("1", "9")) or (digits[-1] in ("1", "9")):
                continue

            number = int("".join(digits))
            if not lazy_is_prime(number):
                continue
                    
            failed = False
            for i in range(1, len(digits)):
                right_trunc = int("".join(digits[:-i]))
                left_trunc = int("".join(digits[i:]))

                right_trunc_is_prime = lazy_is_prime(right_trunc)
                left_trunc_is_prime = lazy_is_prime(left_trunc)

                if (not right_trunc_is_prime) or (not left_trunc_is_prime):
                    failed = True
                    break
            
            if not failed:
                results.append(number)

            
    print(results)



__main__()
