import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
from tabulate import tabulate

from utils.misc_number_theory import get_base_2, is_palindrome
from utils.misc_utils import timer


@timer
def __main__():
    
    results = []

    for x in range(1, 1_000_000):

        if is_palindrome(x) and is_palindrome(get_base_2(x)):
            results.append(x)
    
    print(results)
    answer = sum(results)
    print(answer)

__main__()
