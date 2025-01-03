import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from typing import Dict, List, Tuple, Set
import math
from tabulate import tabulate
import itertools
import numpy as np

import utils.misc_number_theory as mnt
import utils.misc_utils as mu


@mu.timer
def __main__():

    answer = 0

    cubes = set({404 ** 3})

    perm_to_xs: Dict[int, Set[int]] = {}

    x = 5000
    while x < 50000:

        cube = x ** 3

        x_cube_digits = mnt.get_digits(cube)
        added = False
        for perm, xs in perm_to_xs.items():

            if sorted(mnt.get_digits(perm)) == sorted(x_cube_digits):
                xs.add(x)
                if len(xs) == 5:
                    print(f"Found result: {perm}: {xs}")
                    for x in xs:
                        print(f"{x}^3={x ** 3}")
                    return min(xs)    
                added = True
                break
        
        if not added:
            perm_to_xs[cube] = {x}

        if x % 1_000 == 0:
            print(f"Max xs: {max([len(xs) for xs in perm_to_xs.values()])}")

        x += 1
    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")