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
    current_max_x = 0

    # print(mnt.get_prime_decomposition(649))
    # print(mnt.get_prime_decomposition(180))
    # print(mnt.get_prime_decomposition(335159612))
    # print(mnt.get_prime_decomposition(42912791))
    # print(mnt.lazy_is_prime(42912791))
    # raise SystemExit
    for a in range(60):
        if a ** 2 % 60 == 1:
            print(a)
    raise SystemExit

    for D in range(61, 62):

        if mnt.is_perfect_square(D):
            continue
        
        print(f"Finding solution for {D=}")

        permissible_mods = [a for a in range(D) if a **2 % D == 1]
        print(permissible_mods)

        k = 1
        found = False
        while True:
            
            for a in permissible_mods:
                # x
                y_squared = (x ** 2 - 1) / D
                print(f"{k=},{a=},{x=}")
                
                if mnt.is_perfect_square(y_squared):
                    found = True
                    y = int(math.sqrt(y_squared))
                    print(f"{y=}, {y_squared=}, {x=}")
                    if x > current_max_x:
                        answer = D
                        current_max_x = x
                    break
            
            if found:
                break

            k += 1

        # print(f"Nothing found for {x=}")
    print(f"{current_max_x=}")
    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")