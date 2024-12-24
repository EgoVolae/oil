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
    
    results = []

    for x in range(2, 1_000_000):

        digits = [i for i in list(str(x))]
        if len(digits) == 1:
              if lazy_is_prime(x):
                   results.append(x)
        if len(digits) == 2:
            other = int("".join(digits[-1] + digits[0]))

            if lazy_is_prime(other) and lazy_is_prime(x):
                results.append(x)
        
        if len(digits) > 2:
            
            succeeded = True
            for j in range(len(digits)):
                target = int("".join(digits[j+1:] + digits[:j]))

                if not lazy_is_prime(target):
                    succeeded = False
                    break
            
            if succeeded:
                results.append(x)

    print(results)
    print(len(results))    
__main__()
