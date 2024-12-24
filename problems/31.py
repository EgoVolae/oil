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

    def get_breakdowns_for_n(n: int, pieces: List[int]) -> List[List[int]]:
        
        if n < min(pieces):
            return []

        pieces = sorted(pieces)
        
        to_ret = []

        for piece in reversed(pieces):

            if n < piece:
                continue

            if n == piece:
                to_ret.append([piece])
            
            if n > piece:

                breakdowns = get_breakdowns_for_n(n - piece, [p for p in pieces if p <= piece])
                if len(breakdowns) == 0:
                    continue
                for b in breakdowns:
                    b.extend([piece])
                to_ret.extend(breakdowns)
        
        return to_ret

    b = get_breakdowns_for_n(200, [1,2,5,10,20,50,100,200])
    print(b)
    print(f"answer={len(b)}")

__main__()
