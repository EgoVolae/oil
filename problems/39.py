import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
from tabulate import tabulate

from utils.misc_number_theory import get_pythagorean_triplets_up_to_x
from utils.misc_utils import timer


@timer
def __main__():
    
    triplets = get_pythagorean_triplets_up_to_x(1000)
    sums = [sum(triplet) for triplet in triplets]
    
    max_freq = 0
    for s in sums:
        if s > 1000:
            continue
        freq = len([x for x in sums if x == s])
        print(f"{s}: {freq}")
        max_freq = max(max_freq, freq)
    
    print(max_freq)

__main__()
