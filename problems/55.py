import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple
import math
from tabulate import tabulate
import itertools
import numpy as np

import utils.misc_number_theory as mnt
import utils.misc_utils as mu


@mu.timer
def __main__():

    known_lychrel = set()
    known_non_lychrel = set()

    for x in range(1, 10_001):

        chain = {x}
        target = x
        while len(chain) < 50:

            reversed_target = int("".join(reversed(mnt.get_digits(target))))            
            result = target + reversed_target
            if mnt.is_palindrome(result):
                known_non_lychrel = known_non_lychrel.union(chain)
                break
            chain.add(result)
            target = result
        
        if len(chain) == 50:
            known_lychrel.add(x)
        
    print(known_lychrel)

    return len(known_lychrel)

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")