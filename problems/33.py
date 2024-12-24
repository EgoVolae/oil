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
    
    results = [] 

    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                for d in range(1, 10):

                    numer = 10 * a + b
                    denom = 10 * c + d
                    frac = numer / denom

                    if numer >= denom:
                        continue

                    if a == b and c == d:
                        continue

                    if a == d and b / c == frac:
                        print(f"{numer}/{denom}")
                    
                    if b == c and a / d == frac:
                        print(f"{numer}/{denom}")
__main__()
