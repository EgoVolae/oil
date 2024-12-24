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

    for a in range(2, 101):
        for b in range(2, 101):
            results.append(a ** b)
    
    print(len(set(results)))

__main__()
