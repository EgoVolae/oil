import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import Dict, List
import math
from utils.misc_number_theory import get_all_factors


cached_results = {(1,2): 3}


def get_num_paths_for_grid(m: int, n: int) -> int:
    """
    Returns the number of lattice paths for a grid with m rows and n columns
    """

    if (m,n) in cached_results.keys():
        return cached_results[(m,n)]

    if m == 1 or n == 1:
        return m + n
    
    first_piece = get_num_paths_for_grid(m-1, n)
    if (m-1,n) not in cached_results:
        cached_results[(m-1,n)] = first_piece

    second_piece = get_num_paths_for_grid(m, n-1)
    if (m, n-1) not in cached_results:
        cached_results[(m, n-1)] = second_piece

    return first_piece + second_piece


answer = get_num_paths_for_grid(20, 20)
print(answer)
    

