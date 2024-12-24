import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
from tabulate import tabulate

from utils.misc_number_theory import lazy_is_prime
from utils.misc_utils import timer


@timer
def __main__():
    
    max_n = 0
    a_for_max, b_for_max = 0, 0
    
    a_candidates = [x for x in range(-1000, 1001) if x % 2 == 1]
    b_candidates = [x for x in range(1001) if lazy_is_prime(x)]

    for a in a_candidates:
        for b in b_candidates:

            b_mod_3 = b % 3
            a_mod_3 = a % 3

            if b_mod_3 == 1 and a_mod_3 == 1:
                continue

            print(f"Trying {a=}, {b=}")

            n = 0
            while True:
                
                result = n ** 2 + a * n + b
                if result <= 0:
                    break
                if not lazy_is_prime(result):
                    break
                n += 1
            
            if n > max_n:
                max_n = n
                a_for_max, b_for_max = a, b

    print(f"Max consecutive primes: {max_n}, when a={a_for_max} and b={b_for_max}")

    answer = a_for_max * b_for_max
    print(f"{answer=}")

__main__()
