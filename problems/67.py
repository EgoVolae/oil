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

    project_root_dir = Path(__file__).parent.parent

    with open(project_root_dir / "data_items/67_triangle.txt") as f:
        rows = f.readlines()

    # We have 100 rows, each with r elements
    # Index the elements of each row as 1, 2, ..., r
    # Let the ith element in the rth row be called x_{r,i}
    # So we can move from x_{r,i} to x_{r+1,i} or x_{r+1,i+1}
    # Going from  r=99 -> r=1, we should "fold up" the maximum path below, i.e:
    # x_{r,i} = x_{r,i} + max(x_{r+1,i}, x_{r+1,i+1})

    folded_up_rows = []

    for r in reversed(range(99)):
        
        if r == 98:
            row_below = rows[r + 1].split(" ")
            row_below[-1] = row_below[-1].removesuffix("\n")
            row_below = list(map(int, row_below))
        
        else:
            row_below = folded_up_rows[0]

        row = rows[r].split(" ")
        row[-1] = row[-1].removesuffix("\n")
        row = list(map(int, row))

        new_row = [
            row[idx] + max(row_below[idx], row_below[idx + 1]) for idx in range(len(row))
        ]

        folded_up_rows.insert(0, new_row)

    answer = folded_up_rows[0][0]

    return answer

answer = __main__()

question_num = __file__.split("\\")[-1].split(".")[0]
print(f"Question: {question_num} Answer: {answer}")